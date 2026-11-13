import json
import shutil
import subprocess
import tempfile
import threading
import unittest
import urllib.error
import urllib.request
from copy import deepcopy
from pathlib import Path

from human_review_queue import ProjectQueue, QueueError, ReviewHub, ReviewerRegistry, read_json
from human_review_queue_server import ReviewQueueHandler, ReviewQueueServer, build_logger


SOURCE_ROOT = Path(__file__).resolve().parent.parent


class FakeCommandRunner:
    def __init__(self):
        self.calls = []
        self.created_body = ""

    def __call__(self, args, **kwargs):
        self.calls.append(args)
        if args[1:4] == ["search", "issues", args[3]]:
            stdout = "[]"
        elif args[1:4] == ["issue", "create", "--repo"]:
            body_path = Path(args[args.index("--body-file") + 1])
            self.created_body = body_path.read_text(encoding="utf-8")
            stdout = "https://github.com/example/sample-project/issues/99\n"
        elif args[1:4] == ["issue", "view", "1"]:
            stdout = json.dumps({"comments": []})
        elif args[1:4] == ["issue", "comment", "1"]:
            stdout = "https://github.com/example/sample-project/issues/1#issuecomment-1\n"
        else:
            stdout = ""
        return subprocess.CompletedProcess(args, 0, stdout=stdout, stderr="")


def write_json(path: Path, value) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2) + "\n", encoding="utf-8")


class QueueFixture(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.root = Path(self.temporary.name)
        shutil.copytree(
            SOURCE_ROOT / "review-queue",
            self.root / "review-queue",
            ignore=shutil.ignore_patterns(".runtime", "__pycache__"),
        )
        (self.root / "docs" / "agents" / "review-decisions").mkdir(parents=True)
        self.entry = read_json(self.root / "review-queue" / "entry.example.json")
        self.queue = ProjectQueue(self.root, enable_dispatch=False)
        self.queue.enqueue(self.entry)

    def tearDown(self):
        self.temporary.cleanup()

    def response(self, **overrides):
        payload = {
            "entry_id": "RD-001",
            "choice": "approve",
            "notes": "The exact version meets both criteria.",
            "status": "completed",
            "completed_at": "2026-08-15T18:00:00Z",
        }
        payload.update(overrides)
        return payload


class ReviewQueueTestCase(QueueFixture):
    def test_seed_is_copied_to_machine_local_runtime(self):
        self.assertTrue((self.root / "review-queue" / ".runtime" / "queue.json").exists())
        self.assertEqual(len(self.queue.state("owner")["entries"]), 1)

    def test_link_rejects_unsafe_protocol(self):
        entry = deepcopy(self.entry)
        entry["id"] = "RD-UNSAFE"
        entry["media"] = {"type": "link", "label": "unsafe", "href": "javascript:alert(1)"}
        with self.assertRaisesRegex(QueueError, "HTTPS or loopback HTTP"):
            self.queue.validate_entry(entry)

    def test_completed_response_writes_decision_profile_and_action(self):
        response = self.queue.respond(self.response(), "owner")
        self.assertIn("decision_record", response)
        self.assertTrue((self.root / response["decision_record"]).exists())
        self.assertTrue(self.queue.profile_path.exists())
        action = read_json(self.queue.actions_dir / f"{response['response_id']}.json")
        self.assertEqual(action["status"], "pending")
        self.assertTrue(action["dispatch_required"])

    def test_same_response_is_idempotent_and_changed_response_is_rejected(self):
        first = self.queue.respond(self.response(), "owner")
        second = self.queue.respond(self.response(completed_at="2026-08-15T18:05:00Z"), "owner")
        self.assertEqual(first["response_id"], second["response_id"])
        with self.assertRaisesRegex(QueueError, "already completed"):
            self.queue.respond(self.response(choice="revise"), "owner")

    def test_other_requires_notes_and_never_dispatches_by_default(self):
        with self.assertRaisesRegex(QueueError, "Other requires"):
            self.queue.respond(self.response(choice="other", notes=""), "owner")
        response = self.queue.respond(self.response(choice="other", notes="Use a smaller change."), "owner")
        action = read_json(self.queue.actions_dir / f"{response['response_id']}.json")
        self.assertFalse(action["dispatch_required"])

    def test_draft_does_not_write_a_decision(self):
        response = self.queue.respond(self.response(status="pending", completed_at=None), "owner")
        self.assertNotIn("decision_record", response)
        self.assertFalse(self.queue.log_dir.exists())

    def test_parent_chain_routes_to_owner_and_preserves_prior_decision(self):
        registry = read_json(self.root / "review-queue" / "reviewers.json")
        registry["reviewers"].append({
            "id": "editor", "display_name": "Editor", "active": True,
            "roles": ["editor"], "parent_id": "owner",
        })
        write_json(self.root / "review-queue" / "reviewers.json", registry)
        entry = read_json(self.queue.runtime_queue_path)
        entry["entries"][0]["routing"] = {
            "mode": "parent_chain", "start_reviewer_id": "editor", "include_start": True,
        }
        entry["entries"][0]["options"][0]["route"] = "advance"
        write_json(self.queue.runtime_queue_path, entry)
        queue = ProjectQueue(self.root, enable_dispatch=False)
        queue.respond(self.response(), "editor")
        progress = queue.progress(queue.entries_by_id()["RD-001"])
        self.assertEqual(progress["current_stage"]["reviewer_ids"], ["owner"])
        self.assertEqual(progress["history"][0]["reviewer_id"], "editor")
        queue.respond(self.response(notes="Owner confirms the exact version."), "owner")
        self.assertEqual(queue.progress(queue.entries_by_id()["RD-001"])["status"], "completed")

    def test_reviewer_parent_cycle_fails_closed(self):
        path = self.root / "review-queue" / "reviewers.json"
        data = read_json(path)
        data["reviewers"][0]["parent_id"] = "editor"
        data["reviewers"].append({
            "id": "editor", "display_name": "Editor", "active": True,
            "roles": ["editor"], "parent_id": "owner",
        })
        write_json(path, data)
        with self.assertRaisesRegex(QueueError, "parent cycle"):
            ReviewerRegistry(path)

    def test_none_adapter_records_without_external_dispatch(self):
        response = self.queue.respond(self.response(), "owner")
        self.queue.enable_dispatch = True
        actions = self.queue.process_pending_actions()
        self.assertEqual(actions[0]["status"], "recorded")
        self.assertIsNone(actions[0]["dispatch_issue_url"])

    def test_github_bridge_uses_fixed_repository_and_boundary(self):
        config = read_json(self.root / "review-queue" / "config.json")
        config["dispatch"]["adapter"] = "github_issue"
        write_json(self.root / "review-queue" / "config.json", config)
        runner = FakeCommandRunner()
        queue = ProjectQueue(self.root, command_runner=runner, enable_dispatch=True)
        queue.respond(self.response(), "owner")
        actions = queue.process_pending_actions()
        self.assertEqual(actions[0]["status"], "queued")
        self.assertIn("Do not push, merge, publish", runner.created_body)
        repository = config["project"]["repository"]
        self.assertTrue(any(repository in call for call in runner.calls))


class ReviewHubTestCase(QueueFixture):
    def test_hub_combines_assigned_entries_from_two_sources(self):
        other = self.root / "other"
        shutil.copytree(
            SOURCE_ROOT / "review-queue",
            other / "review-queue",
            ignore=shutil.ignore_patterns(".runtime", "__pycache__"),
        )
        other_config = read_json(other / "review-queue" / "config.json")
        other_config["project"] = {"id": "other", "name": "Other Project", "repository": "example/other"}
        other_config["dispatch"]["repository"] = "example/other"
        write_json(other / "review-queue" / "config.json", other_config)
        other_queue = ProjectQueue(other, source_id="other", source_name="Other Project", enable_dispatch=False)
        other_entry = read_json(other / "review-queue" / "entry.example.json")
        other_entry["id"] = "RD-OTHER"
        other_queue.enqueue(other_entry)
        hub = read_json(self.root / "review-queue" / "hub.json")
        hub["sources"].append({"id": "other", "name": "Other Project", "root": "other", "enabled": True})
        write_json(self.root / "review-queue" / "hub.json", hub)
        state = ReviewHub(self.root, enable_dispatch=False).state("owner")
        self.assertEqual({item["source_id"] for item in state["entries"]}, {self.queue.source_id, "other"})
        self.assertEqual(len({item["entry_key"] for item in state["entries"]}), 2)


class ReviewQueueHttpTestCase(QueueFixture):
    def setUp(self):
        super().setUp()
        hub = ReviewHub(self.root, enable_dispatch=False)
        logger = build_logger(self.root / "review-queue" / ".runtime" / "test.log")
        self.server = ReviewQueueServer(("127.0.0.1", 0), ReviewQueueHandler, hub, "test-token", logger)
        self.thread = threading.Thread(target=self.server.serve_forever, daemon=True)
        self.thread.start()
        self.base = f"http://127.0.0.1:{self.server.server_port}"

    def tearDown(self):
        self.server.shutdown()
        self.server.server_close()
        self.thread.join(timeout=3)
        for handler in list(self.server.logger.handlers):
            handler.close()
            self.server.logger.removeHandler(handler)
        super().tearDown()

    def test_get_state_and_csrf_protection(self):
        state = json.load(urllib.request.urlopen(f"{self.base}/api/review-queue"))
        self.assertEqual(state["csrf_token"], "test-token")
        self.assertEqual(state["reviewer"]["id"], "owner")
        request = urllib.request.Request(
            f"{self.base}/api/review-queue/retry", data=b"{}", method="POST",
            headers={"Content-Type": "application/json"},
        )
        with self.assertRaises(urllib.error.HTTPError) as caught:
            urllib.request.urlopen(request)
        self.assertEqual(caught.exception.code, 403)
        caught.exception.close()

    def test_server_does_not_serve_arbitrary_repo_files(self):
        (self.root / "secret.txt").write_text("not public", encoding="utf-8")
        with self.assertRaises(urllib.error.HTTPError) as caught:
            urllib.request.urlopen(f"{self.base}/secret.txt")
        self.assertEqual(caught.exception.code, 404)
        caught.exception.close()

    def test_static_page_and_media_ranges_are_served(self):
        page = urllib.request.urlopen(f"{self.base}/review-queue/").read().decode("utf-8")
        self.assertIn("Human review queue", page)
        media = self.root / "media" / "sample.bin"
        media.parent.mkdir()
        media.write_bytes(b"abcdef")
        request = urllib.request.Request(
            f"{self.base}/media/{self.queue.source_id}/media/sample.bin",
            headers={"Range": "bytes=1-3"},
        )
        with urllib.request.urlopen(request) as response:
            self.assertEqual(response.status, 206)
            self.assertEqual(response.headers["Content-Range"], "bytes 1-3/6")
            self.assertEqual(response.read(), b"bcd")


if __name__ == "__main__":
    unittest.main()
