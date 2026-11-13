"""Durable, reviewer-routed human review queue and bounded action bridge."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
from collections import Counter, defaultdict
from datetime import date, datetime, timezone
from pathlib import Path
from typing import Any, Callable
from urllib.parse import urlparse


ROOT = Path(__file__).resolve().parent.parent
ENTRY_REQUIRED = {
    "id", "kind", "title", "project", "issue", "ticket", "touchpoint",
    "due", "version", "criteria", "steps", "media", "question", "options",
    "recommendation", "record", "decision_type", "human_owned_category",
    "reversible", "routing", "agent_action",
}
ACTION_REQUIRED = {"enabled", "group", "job", "tool", "categories", "output", "boundary"}


class QueueError(ValueError):
    """Reject invalid or conflicting queue operations."""


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


def read_json(path: Path, default: Any = None) -> Any:
    if not path.exists():
        return default
    with path.open(encoding="utf-8") as handle:
        return json.load(handle)


def atomic_write_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    handle, temp_name = tempfile.mkstemp(prefix=f".{path.name}.", suffix=".tmp", dir=path.parent)
    try:
        with os.fdopen(handle, "w", encoding="utf-8", newline="\n") as stream:
            json.dump(value, stream, indent=2, ensure_ascii=False)
            stream.write("\n")
        os.replace(temp_name, path)
    finally:
        if os.path.exists(temp_name):
            os.unlink(temp_name)


def slug(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")[:64] or "response"


def validate_basic_entry(entry: dict[str, Any]) -> None:
    missing = sorted(ENTRY_REQUIRED - set(entry))
    if missing:
        raise QueueError(f"queue entry missing required fields: {missing}")
    if entry["touchpoint"] not in {"A", "B"}:
        raise QueueError("queue entries must be actionable Type A or B touchpoints")
    if not isinstance(entry["criteria"], list) or not entry["criteria"]:
        raise QueueError("criteria must be a non-empty list")
    if not isinstance(entry["steps"], list) or not entry["steps"]:
        raise QueueError("steps must be a non-empty list")
    media = entry["media"]
    if not isinstance(media, dict) or media.get("type") not in {"video", "audio", "image", "link", "none"}:
        raise QueueError("media must use type video, audio, image, link, or none")
    if media["type"] in {"video", "audio", "image"} and not media.get("src"):
        raise QueueError(f"media type {media['type']} requires src")
    if media["type"] == "link":
        if not media.get("href"):
            raise QueueError("media type link requires href")
        target = urlparse(str(media["href"]))
        secure = target.scheme == "https" and bool(target.netloc)
        loopback = target.scheme == "http" and target.hostname in {"127.0.0.1", "localhost"}
        if not (secure or loopback):
            raise QueueError("media link must use HTTPS or loopback HTTP")
    options = entry["options"]
    if not isinstance(options, list) or len(options) < 2:
        raise QueueError("options must contain at least two choices")
    values = [option.get("value") for option in options]
    if any(not value for value in values) or len(values) != len(set(values)):
        raise QueueError("option values must be present and unique")
    if len([option for option in options if option.get("recommended")]) != 1:
        raise QueueError("each entry must have exactly one recommended option")
    for option in options:
        if not option.get("label") or not option.get("effect"):
            raise QueueError("each option requires label and effect")
        if option.get("route", "advance") not in {"advance", "complete", "stop"}:
            raise QueueError("option route must be advance, complete, or stop")
    action = entry["agent_action"]
    missing_action = sorted(ACTION_REQUIRED - set(action))
    if missing_action:
        raise QueueError(f"agent_action missing required fields: {missing_action}")


class ReviewerRegistry:
    def __init__(self, path: Path):
        data = read_json(path)
        if not data or not isinstance(data.get("reviewers"), list):
            raise QueueError(f"invalid reviewer registry: {path}")
        self.reviewers = {item["id"]: item for item in data["reviewers"]}
        if len(self.reviewers) != len(data["reviewers"]):
            raise QueueError("reviewer IDs must be unique")
        for reviewer_id, reviewer in self.reviewers.items():
            if slug(reviewer_id) != reviewer_id:
                raise QueueError(f"reviewer ID must be lowercase slug: {reviewer_id}")
            if not isinstance(reviewer.get("roles"), list):
                raise QueueError(f"reviewer roles must be a list: {reviewer_id}")
            parent = reviewer.get("parent_id")
            if parent and parent not in self.reviewers:
                raise QueueError(f"unknown parent reviewer {parent}: {reviewer_id}")
        for reviewer_id in self.reviewers:
            seen: set[str] = set()
            current: str | None = reviewer_id
            while current:
                if current in seen:
                    raise QueueError(f"reviewer parent cycle includes {current}")
                seen.add(current)
                current = self.reviewers[current].get("parent_id")

    def active(self, reviewer_id: str) -> bool:
        return bool(self.reviewers.get(reviewer_id, {}).get("active"))

    def public(self) -> list[dict[str, str]]:
        return [
            {"id": item["id"], "display_name": item["display_name"]}
            for item in self.reviewers.values() if item.get("active")
        ]

    def stages(self, routing: dict[str, Any]) -> list[dict[str, Any]]:
        mode = routing.get("mode")
        if mode == "parent_chain":
            start = routing.get("start_reviewer_id")
            if start not in self.reviewers or not self.active(start):
                raise QueueError(f"parent chain starts with inactive or unknown reviewer: {start}")
            ids: list[str] = []
            current: str | None = start
            while current:
                ids.append(current)
                current = self.reviewers[current].get("parent_id")
            if not routing.get("include_start", True):
                ids = ids[1:]
            if not ids:
                raise QueueError("parent chain resolved to no reviewers")
            return [{"id": f"stage-{index + 1}", "reviewer_ids": [item], "approvals_required": 1}
                    for index, item in enumerate(ids)]
        if mode != "stages" or not isinstance(routing.get("stages"), list) or not routing["stages"]:
            raise QueueError("routing must define stages or a parent_chain")
        stages: list[dict[str, Any]] = []
        stage_ids: set[str] = set()
        for raw in routing["stages"]:
            stage_id = raw.get("id")
            if not stage_id or stage_id in stage_ids:
                raise QueueError("routing stage IDs must be present and unique")
            stage_ids.add(stage_id)
            assigned = set(raw.get("reviewer_ids") or [])
            roles = set(raw.get("roles") or [])
            assigned.update(
                reviewer_id for reviewer_id, reviewer in self.reviewers.items()
                if reviewer.get("active") and roles.intersection(reviewer.get("roles") or [])
            )
            inactive = [item for item in assigned if not self.active(item)]
            if inactive:
                raise QueueError(f"stage {stage_id} contains inactive or unknown reviewers: {inactive}")
            quorum = int(raw.get("approvals_required", 1))
            if quorum < 1 or quorum > len(assigned):
                raise QueueError(f"stage {stage_id} has invalid approvals_required")
            stages.append({"id": stage_id, "reviewer_ids": sorted(assigned), "approvals_required": quorum})
        return stages


class ProjectQueue:
    def __init__(
        self,
        root: Path = ROOT,
        source_id: str | None = None,
        source_name: str | None = None,
        command_runner: Callable[..., subprocess.CompletedProcess[str]] | None = None,
        enable_dispatch: bool = True,
    ) -> None:
        self.root = Path(root).resolve()
        self.queue_dir = self.root / "review-queue"
        self.config = read_json(self.queue_dir / "config.json")
        if not self.config:
            raise QueueError(f"missing review queue config: {self.queue_dir / 'config.json'}")
        self.source_id = source_id or self.config["project"]["id"]
        self.source_name = source_name or self.config["project"]["name"]
        self.registry = ReviewerRegistry(self.queue_dir / "reviewers.json")
        self.seed_path = self.queue_dir / "queue.json"
        self.runtime_dir = self.queue_dir / ".runtime"
        self.runtime_queue_path = self.runtime_dir / "queue.json"
        self.responses_dir = self.runtime_dir / "responses"
        self.actions_dir = self.runtime_dir / "actions"
        recording = self.config["recording"]
        self.log_dir = self.root / recording["log_dir"]
        self.profile_path = self.root / recording["profile_path"]
        self.command_runner = command_runner or subprocess.run
        self.gh_executable = "gh" if command_runner else self._resolve_gh()
        self.enable_dispatch = enable_dispatch

    @staticmethod
    def _resolve_gh() -> str:
        found = shutil.which("gh")
        if found:
            return found
        for variable in ("ProgramFiles", "ProgramW6432"):
            base = os.environ.get(variable)
            candidate = Path(base) / "GitHub CLI" / "gh.exe" if base else None
            if candidate and candidate.exists():
                return str(candidate)
        return "gh"

    def load_queue(self) -> dict[str, Any]:
        source = self.runtime_queue_path if self.runtime_queue_path.exists() else self.seed_path
        queue = read_json(source)
        if not queue or not isinstance(queue.get("entries"), list):
            raise QueueError(f"invalid queue file: {source}")
        for entry in queue["entries"]:
            self.validate_entry(entry)
        if source == self.seed_path:
            atomic_write_json(self.runtime_queue_path, queue)
        return queue

    def validate_entry(self, entry: dict[str, Any]) -> list[dict[str, Any]]:
        validate_basic_entry(entry)
        return self.registry.stages(entry["routing"])

    def entries_by_id(self) -> dict[str, dict[str, Any]]:
        return {entry["id"]: entry for entry in self.load_queue()["entries"]}

    def enqueue(self, entry: dict[str, Any]) -> dict[str, Any]:
        entry = dict(entry)
        self.validate_entry(entry)
        queue = self.load_queue()
        if any(existing["id"] == entry["id"] for existing in queue["entries"]):
            raise QueueError(f"queue entry already exists: {entry['id']}")
        entry.setdefault("enqueued_at", utc_now())
        queue["entries"].append(entry)
        atomic_write_json(self.runtime_queue_path, queue)
        return entry

    def _all_responses(self, entry_id: str | None = None) -> list[dict[str, Any]]:
        result = []
        for path in sorted(self.responses_dir.glob("*.json")):
            item = read_json(path)
            if item and (entry_id is None or item.get("entry_id") == entry_id):
                result.append(item)
        return result

    @staticmethod
    def _option(entry: dict[str, Any], choice: str) -> dict[str, Any]:
        if choice == "other":
            return {
                "value": "other", "label": "Other", "recommended": False,
                "effect": "Apply the reviewer's written disposition.",
                "route": "stop", "dispatch": bool(entry.get("other_dispatch", False)),
            }
        for option in entry["options"]:
            if option["value"] == choice:
                return option
        raise QueueError(f"unknown choice {choice!r} for {entry['id']}")

    def progress(self, entry: dict[str, Any]) -> dict[str, Any]:
        stages = self.registry.stages(entry["routing"])
        completed = [item for item in self._all_responses(entry["id"]) if item.get("status") == "completed"]
        history: list[dict[str, Any]] = []
        terminal = False
        conflict = False
        terminal_choice: str | None = None
        current_stage: dict[str, Any] | None = None
        for index, stage in enumerate(stages):
            stage_responses = [item for item in completed if item.get("stage_id") == stage["id"]]
            unique = {item["reviewer_id"]: item for item in stage_responses}
            counts = Counter(item["choice"] for item in unique.values())
            winner = next((choice for choice, count in counts.items() if count >= stage["approvals_required"]), None)
            history.extend(sorted(unique.values(), key=lambda item: item["completed_at"]))
            if winner:
                option = self._option(entry, winner)
                last = index == len(stages) - 1
                route = option.get("route", "complete" if last else "advance")
                if route in {"stop", "complete"} or last:
                    terminal = True
                    terminal_choice = winner
                    break
                continue
            if len(unique) == len(stage["reviewer_ids"]):
                if index == len(stages) - 1:
                    terminal = True
                    conflict = True
                    break
                continue
            current_stage = stage
            break
        if not terminal and current_stage is None:
            terminal = True
        return {
            "status": "conflict" if conflict else ("completed" if terminal else "pending"),
            "terminal": terminal,
            "conflict": conflict,
            "terminal_choice": terminal_choice,
            "current_stage": current_stage,
            "history": history,
        }

    def respond(self, payload: dict[str, Any], reviewer_id: str, source: str = "web") -> dict[str, Any]:
        entries = self.entries_by_id()
        entry_id = str(payload.get("entry_id", ""))
        if entry_id not in entries:
            raise QueueError(f"unknown queue entry: {entry_id}")
        entry = entries[entry_id]
        status = str(payload.get("status", "completed"))
        choice = str(payload.get("choice", "")).strip()
        notes = str(payload.get("notes", "")).strip()
        if status not in {"pending", "completed"}:
            raise QueueError("status must be pending or completed")
        if status == "completed" and not choice:
            raise QueueError("a completed response requires a choice")
        option = self._option(entry, choice) if choice else None
        if choice == "other" and not notes:
            raise QueueError("Other requires a written response")
        progress = self.progress(entry)
        stage = progress["current_stage"]
        assigned_here = bool(stage and reviewer_id in stage["reviewer_ids"])
        reviewer_completed = [
            item for item in self._all_responses(entry_id)
            if item.get("reviewer_id") == reviewer_id and item.get("status") == "completed"
        ]
        same = [
            item for item in reviewer_completed
            if item["choice"] == choice and item.get("notes", "") == notes
            and (not assigned_here or item.get("stage_id") == stage["id"])
        ]
        if same:
            return same[-1]
        if not assigned_here:
            if reviewer_completed:
                raise QueueError("reviewer already completed this routing stage; create a new reviewed version to change it")
            raise QueueError(f"entry is not assigned to reviewer {reviewer_id}")
        prior = [item for item in self._all_responses(entry_id) if item.get("stage_id") == stage["id"]
                 and item.get("reviewer_id") == reviewer_id and item.get("status") == "completed"]
        if prior:
            same = [item for item in prior if item["choice"] == choice and item.get("notes", "") == notes]
            if same:
                return same[-1]
            raise QueueError("reviewer already completed this routing stage; create a new reviewed version to change it")
        completed_at = str(payload.get("completed_at") or utc_now())
        material = json.dumps(
            [self.source_id, entry_id, stage["id"], reviewer_id, status, choice, notes],
            ensure_ascii=False, separators=(",", ":"),
        )
        response_id = f"{slug(entry_id)}-{hashlib.sha256(material.encode()).hexdigest()[:12]}"
        path = self.responses_dir / f"{response_id}.json"
        existing = read_json(path)
        if existing:
            return existing
        response = {
            "schema_version": 1,
            "response_id": response_id,
            "source_id": self.source_id,
            "entry_id": entry_id,
            "stage_id": stage["id"],
            "reviewer_id": reviewer_id,
            "status": status,
            "choice": choice,
            "choice_label": option["label"] if option else None,
            "notes": notes,
            "completed_at": completed_at if status == "completed" else None,
            "received_at": utc_now(),
            "source": source,
            "reviewed_version": entry["version"],
            "criteria": entry["criteria"],
            "ticket": entry["ticket"],
        }
        atomic_write_json(path, response)
        if status == "completed":
            record_path = self._write_decision(entry, option, response)
            response["decision_record"] = str(record_path.relative_to(self.root)).replace("\\", "/")
            atomic_write_json(path, response)
            after = self.progress(entry)
            if after["terminal"]:
                self._write_action(entry, option, response, after)
            self.build_profile()
        return response

    def import_legacy(self, legacy: dict[str, Any], reviewer_id: str) -> list[dict[str, Any]]:
        imported = []
        for entry_id, item in (legacy.get("responses") or {}).items():
            if item.get("status") != "completed":
                continue
            imported.append(self.respond({
                "entry_id": entry_id,
                "choice": item.get("choice", ""),
                "notes": item.get("notes", ""),
                "status": "completed",
                "completed_at": item.get("completedAt") or utc_now(),
            }, reviewer_id, source="legacy-session-migration"))
        return imported

    def _write_decision(self, entry: dict[str, Any], option: dict[str, Any], response: dict[str, Any]) -> Path:
        recommended = next(item for item in entry["options"] if item.get("recommended"))
        outcome = "accepted_recommendation" if option["value"] == recommended["value"] else (
            "modified" if option["value"] == "other" else "chose_alternative"
        )
        decision_id = f"{response['completed_at'][:10]}-{response['response_id']}"
        path = self.log_dir / f"{decision_id}.json"
        record = {
            "decision_id": decision_id,
            "date": response["completed_at"][:10],
            "source_id": self.source_id,
            "ticket": entry["ticket"],
            "decision_type": entry["decision_type"],
            "question": entry["question"],
            "options_considered": [item["label"] for item in entry["options"]] + ["Other"],
            "agent_recommendation": {"option": recommended["label"], "reasoning": entry["recommendation"]},
            "reviewer_id": response["reviewer_id"],
            "routing_stage": response["stage_id"],
            "human_decision": option["label"] + (f": {response['notes']}" if response["notes"] else ""),
            "outcome": outcome,
            "rationale": response["notes"] or "Selected after the listed review path in the human review queue.",
            "autonomy_level": 0,
            "touchpoint_type": entry["touchpoint"],
            "reversible": entry["reversible"],
            "human_owned_category": entry["human_owned_category"],
            "review_queue_entry_id": entry["id"],
            "review_queue_response_id": response["response_id"],
            "reviewed_version": entry["version"],
            "review_criteria": entry["criteria"],
            "capture_source": response["source"],
            "completed_at": response["completed_at"],
        }
        existing = read_json(path)
        if existing and existing != record:
            raise QueueError(f"append-only decision record conflict: {path}")
        if not existing:
            atomic_write_json(path, record)
        return path

    def _write_action(self, entry: dict[str, Any], option: dict[str, Any], response: dict[str, Any], progress: dict[str, Any]) -> None:
        if not entry["agent_action"]["enabled"]:
            return
        path = self.actions_dir / f"{response['response_id']}.json"
        if path.exists():
            return
        dispatch_allowed = bool(option.get("dispatch", True)) and not progress["conflict"]
        action = {
            "schema_version": 1,
            "action_id": response["response_id"],
            "response_id": response["response_id"],
            "entry_id": entry["id"],
            "group": entry["agent_action"]["group"],
            "status": "pending",
            "dispatch_required": dispatch_allowed,
            "created_at": utc_now(),
            "updated_at": utc_now(),
            "attempts": 0,
            "last_error": None,
            "github_comment_url": None,
            "dispatch_issue_url": None,
        }
        atomic_write_json(path, action)

    def build_profile(self) -> None:
        records = [read_json(path) for path in sorted(self.log_dir.glob("*.json"))]
        lines = [
            "# Human review decision profile (non-canonical synthesis)", "",
            f"Regenerated {date.today().isoformat()} from {len(records)} append-only record(s).",
            "This profile is evidence. It does not authorize unattended decisions or actions.", "",
        ]
        if records:
            lines.extend(["## By decision type", "", "| Decision type | Count | Accepted recommendation | Modified | Alternative |", "|---|---:|---:|---:|---:|"])
            grouped: dict[str, list[dict[str, Any]]] = defaultdict(list)
            for record in records:
                grouped[record["decision_type"]].append(record)
            for kind, items in sorted(grouped.items()):
                outcomes = Counter(item["outcome"] for item in items)
                lines.append(f"| {kind} | {len(items)} | {outcomes['accepted_recommendation']} | {outcomes['modified']} | {outcomes['chose_alternative']} |")
            lines.extend(["", "## Full log", "", "| Date | Reviewer | Stage | Type | Outcome |", "|---|---|---|---|---|"])
            for record in records:
                lines.append(f"| {record['date']} | {record.get('reviewer_id', 'unknown')} | {record.get('routing_stage', 'legacy')} | {record['decision_type']} | {record['outcome']} |")
        self.profile_path.parent.mkdir(parents=True, exist_ok=True)
        self.profile_path.write_text("\n".join(lines) + "\n", encoding="utf-8")

    def _run_gh(self, args: list[str]) -> str:
        result = self.command_runner(
            [self.gh_executable, *args], cwd=self.root, text=True, encoding="utf-8",
            capture_output=True, check=False,
            creationflags=getattr(subprocess, "CREATE_NO_WINDOW", 0),
        )
        if result.returncode != 0:
            raise QueueError(result.stderr.strip() or result.stdout.strip() or "gh command failed")
        return result.stdout.strip()

    def _staged_tempfile(self, content: str, suffix: str) -> str:
        """Stage content to a file gh can read via --body-file. Prefers a repo-local
        scratch directory (review-queue/.runtime/tmp/, already gitignored) so this
        works when system temp access is restricted; falls back to the system temp
        directory only if the repo-local one can't be created or written."""
        repo_local_dir = self.root / "review-queue" / ".runtime" / "tmp"
        try:
            repo_local_dir.mkdir(parents=True, exist_ok=True)
            handle = tempfile.NamedTemporaryFile(
                mode="w", encoding="utf-8", suffix=suffix, dir=repo_local_dir, delete=False,
            )
        except OSError:
            handle = tempfile.NamedTemporaryFile(mode="w", encoding="utf-8", suffix=suffix, delete=False)
        with handle:
            handle.write(content)
            return handle.name

    def process_pending_actions(self) -> list[dict[str, Any]]:
        pending = [read_json(path) for path in sorted(self.actions_dir.glob("*.json"))]
        pending = [item for item in pending if item and item["status"] == "pending"]
        if not pending or not self.enable_dispatch:
            return pending
        grouped: dict[str, list[dict[str, Any]]] = defaultdict(list)
        for action in pending:
            grouped[action["group"]].append(action)
        completed = []
        for actions in grouped.values():
            completed.extend(self._process_action_group(actions))
        return completed

    def _process_action_group(self, actions: list[dict[str, Any]]) -> list[dict[str, Any]]:
        adapter = self.config["dispatch"].get("adapter", "none")
        if adapter not in {"none", "github_issue"}:
            raise QueueError(f"unsupported dispatch adapter: {adapter}")
        entries = self.entries_by_id()
        contexts = []
        for action in actions:
            entry = entries[action["entry_id"]]
            response = read_json(self.responses_dir / f"{action['response_id']}.json")
            contexts.append((entry, response, self._option(entry, response["choice"])))
        marker_hash = hashlib.sha256("|".join(sorted(item["response_id"] for _, item, _ in contexts)).encode()).hexdigest()[:16]
        marker = f"human-review-action:{marker_hash}"
        dispatch_required = any(item["dispatch_required"] for item in actions)
        dispatch_url = None
        try:
            if adapter == "github_issue":
                repository = self.config["dispatch"]["repository"]
                label = self.config["dispatch"]["label"]
                if repository != self.config["project"]["repository"]:
                    raise QueueError("dispatch repository must match the configured project repository")
                if dispatch_required:
                    matches = json.loads(self._run_gh(["search", "issues", marker_hash, "--repo", repository, "--match", "body", "--state", "open", "--json", "number,url,body"]) or "[]")
                    if matches:
                        dispatch_url = matches[0]["url"]
                    else:
                        body = self._action_body(contexts, marker)
                        body_path = self._staged_tempfile(body, ".md")
                        try:
                            title = f"Apply {len(contexts)} human review response(s)" if len(contexts) > 1 else f"Apply {contexts[0][0]['id']}: {contexts[0][2]['label']}"
                            dispatch_url = self._run_gh(["issue", "create", "--repo", repository, "--title", title, "--body-file", body_path, "--label", label]).splitlines()[-1]
                        finally:
                            os.unlink(body_path)
                self._comment_governing_issues(contexts, dispatch_url, marker, repository)
            for action in actions:
                action["status"] = "queued" if adapter == "github_issue" and dispatch_required else "recorded"
                action["dispatch_issue_url"] = dispatch_url
                action["updated_at"] = utc_now()
                action["attempts"] += 1
                action["last_error"] = None
                atomic_write_json(self.actions_dir / f"{action['action_id']}.json", action)
            return actions
        except Exception as exc:
            for action in actions:
                action["attempts"] += 1
                action["last_error"] = str(exc)
                action["updated_at"] = utc_now()
                atomic_write_json(self.actions_dir / f"{action['action_id']}.json", action)
            return actions

    def _action_body(self, contexts: list[tuple[dict[str, Any], dict[str, Any], dict[str, Any]]], marker: str) -> str:
        instructions = [f"- {entry['agent_action']['job']} Decision: {option['label']}." for entry, _, option in contexts]
        details = []
        boundaries = {self.config["dispatch"]["fixed_boundary"]}
        for entry, response, option in contexts:
            action = entry["agent_action"]
            boundaries.add(action["boundary"])
            details.append(
                f"Queue entry: {entry['id']}\nResponse: {response['response_id']}\nReviewer: {response['reviewer_id']}\n"
                f"Reviewed version: {entry['version']}\nDecision: {option['label']}\nNotes: {response['notes'] or 'None'}\n"
                f"Job: {action['job']}\nTool: {action['tool']}\nCategories: {', '.join(action['categories'])}\nOutput: {action['output']}\nBoundary: {action['boundary']}"
            )
        return "## Instruction\n\n" + "\n".join(instructions) + "\n\n## Context\n\n" + "\n\n---\n\n".join(details) + "\n\nShared boundary:\n- " + "\n- ".join(sorted(boundaries)) + f"\n\n<!-- {marker} -->\n"

    def _comment_governing_issues(self, contexts, dispatch_url: str | None, marker: str, repository: str) -> None:
        for ticket in sorted({entry["ticket"] for entry, _, _ in contexts}):
            issue_number = ticket.rstrip("/").rsplit("/", 1)[-1]
            if not issue_number.isdigit():
                continue
            comment_marker = f"<!-- {marker}:{issue_number} -->"
            comments = json.loads(self._run_gh(["issue", "view", issue_number, "--repo", repository, "--json", "comments"])).get("comments", [])
            if any(comment_marker in (item.get("body") or "") for item in comments):
                continue
            lines = ["## Human review responses recorded", ""]
            for entry, response, option in contexts:
                if entry["ticket"] == ticket:
                    lines.append(f"- **{entry['id']}** - {option['label']} by `{response['reviewer_id']}` for `{entry['version']}`")
            lines.extend(["", f"Agent follow-up: {dispatch_url or 'No dispatch required.'}", "", comment_marker])
            self._run_gh(["issue", "comment", issue_number, "--repo", repository, "--body", "\n".join(lines)])

    def state(self, reviewer_id: str | None = None) -> dict[str, Any]:
        entries = []
        responses: dict[str, Any] = {}
        actions: dict[str, Any] = {}
        for entry in self.load_queue()["entries"]:
            progress = self.progress(entry)
            history = progress["history"]
            assigned = (progress["current_stage"] or {}).get("reviewer_ids", [])
            visible = reviewer_id is None or reviewer_id in assigned or any(item["reviewer_id"] == reviewer_id for item in history)
            if not visible:
                continue
            public = dict(entry)
            key = f"{self.source_id}:{entry['id']}"
            public["entry_key"] = key
            public["source_id"] = self.source_id
            public["source_name"] = self.source_name
            public["routing_state"] = {
                "status": progress["status"],
                "current_stage": progress["current_stage"],
                "history": [{
                    "reviewer_id": item["reviewer_id"], "stage_id": item["stage_id"],
                    "choice": item["choice"], "choice_label": item["choice_label"],
                    "notes": item["notes"], "completed_at": item["completed_at"],
                } for item in history],
            }
            entries.append(public)
            reviewer_items = [item for item in self._all_responses(entry["id"]) if reviewer_id is None or item.get("reviewer_id") == reviewer_id]
            if reviewer_items:
                responses[key] = max(reviewer_items, key=lambda item: item["received_at"])
            entry_actions = [read_json(path) for path in self.actions_dir.glob("*.json")]
            entry_actions = [item for item in entry_actions if item and item["entry_id"] == entry["id"]]
            if entry_actions:
                actions[key] = max(entry_actions, key=lambda item: item["updated_at"])
        return {"entries": entries, "responses": responses, "actions": actions}


class ReviewHub:
    def __init__(self, root: Path = ROOT, enable_dispatch: bool = True, command_runner=None):
        self.root = Path(root).resolve()
        self.host_config = read_json(self.root / "review-queue" / "config.json")
        self.registry = ReviewerRegistry(self.root / "review-queue" / "reviewers.json")
        hub = read_json(self.root / "review-queue" / "hub.json", {"sources": [{"id": "current", "name": "Current", "root": ".", "enabled": True}]})
        self.sources: dict[str, ProjectQueue] = {}
        for source in hub.get("sources", []):
            if not source.get("enabled", True):
                continue
            source_root = Path(source["root"])
            if not source_root.is_absolute():
                source_root = (self.root / source_root).resolve()
            queue = ProjectQueue(source_root, source["id"], source.get("name"), command_runner, enable_dispatch)
            self.sources[source["id"]] = queue
        if not self.sources:
            raise QueueError("hub has no enabled sources")

    def state(self, reviewer_id: str) -> dict[str, Any]:
        merged = {"entries": [], "responses": {}, "actions": {}}
        for queue in self.sources.values():
            state = queue.state(reviewer_id)
            merged["entries"].extend(state["entries"])
            merged["responses"].update(state["responses"])
            merged["actions"].update(state["actions"])
        merged["reviewer"] = self.registry.reviewers[reviewer_id]
        merged["reviewers"] = self.registry.public()
        merged["identity_mode"] = self.host_config["server"]["identity_mode"]
        return merged

    def respond(self, payload: dict[str, Any], reviewer_id: str, source: str = "web") -> dict[str, Any]:
        source_id = str(payload.get("source_id", ""))
        if source_id not in self.sources:
            raise QueueError(f"unknown queue source: {source_id}")
        return self.sources[source_id].respond(payload, reviewer_id, source)

    def import_legacy(self, payload: dict[str, Any], reviewer_id: str) -> list[dict[str, Any]]:
        if len(self.sources) != 1:
            raise QueueError("legacy import requires a single-source hub")
        return next(iter(self.sources.values())).import_legacy(payload, reviewer_id)

    def process_pending_actions(self) -> list[dict[str, Any]]:
        results = []
        for queue in self.sources.values():
            results.extend(queue.process_pending_actions())
        return results


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    validate = sub.add_parser("validate", help="validate one entry")
    validate.add_argument("entry_json", type=Path)
    enqueue = sub.add_parser("enqueue", help="add one validated entry")
    enqueue.add_argument("entry_json", type=Path)
    scan = sub.add_parser("scan", help="show queue and action state")
    scan.add_argument("--json", action="store_true")
    scan.add_argument("--reviewer")
    sync = sub.add_parser("sync", help="retry pending action bridges")
    sync.add_argument("--no-dispatch", action="store_true")
    return parser


def main() -> int:
    args = build_parser().parse_args()
    try:
        queue = ProjectQueue(ROOT, enable_dispatch=not getattr(args, "no_dispatch", False))
        if args.command == "validate":
            stages = queue.validate_entry(read_json(args.entry_json))
            print(json.dumps({"valid": True, "stages": stages}, indent=2))
        elif args.command == "enqueue":
            print(json.dumps(queue.enqueue(read_json(args.entry_json)), ensure_ascii=False, indent=2))
        elif args.command == "scan":
            reviewer = args.reviewer or queue.config["server"].get("default_reviewer")
            state = ReviewHub(ROOT, enable_dispatch=False).state(reviewer)
            if args.json:
                print(json.dumps(state, ensure_ascii=False, indent=2))
            else:
                pending = sum(1 for item in state["actions"].values() if item["status"] == "pending")
                print(f"{len(state['entries'])} visible entry(s); {pending} pending action(s)")
        else:
            print(json.dumps(ReviewHub(ROOT, enable_dispatch=not args.no_dispatch).process_pending_actions(), ensure_ascii=False, indent=2))
        return 0
    except QueueError as exc:
        print(f"human review queue error: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
