import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


SCRIPT = Path(__file__).resolve().parent / "install_review_queue.py"


class InstallerTest(unittest.TestCase):
    def test_installs_safe_single_reviewer_default(self):
        with tempfile.TemporaryDirectory() as temporary:
            repo = Path(temporary)
            result = subprocess.run([
                sys.executable,
                str(SCRIPT),
                "--repo", str(repo),
                "--project-id", "sample",
                "--project-name", "Sample Project",
                "--repository", "example/sample",
                "--reviewer-id", "owner",
                "--reviewer-name", "Project Owner",
            ], text=True, capture_output=True, check=False)
            self.assertEqual(result.returncode, 0, result.stderr)
            config = json.loads((repo / "review-queue" / "config.json").read_text(encoding="utf-8"))
            reviewers = json.loads((repo / "review-queue" / "reviewers.json").read_text(encoding="utf-8"))
            control_plane = json.loads((repo / "review-queue" / "control-plane.json").read_text(encoding="utf-8"))
            self.assertEqual(config["dispatch"]["adapter"], "none")
            self.assertEqual(config["server"]["identity_mode"], "single_local")
            self.assertEqual(reviewers["reviewers"][0]["id"], "owner")
            self.assertEqual(control_plane["integration_version"], "1.0.0")
            self.assertEqual(control_plane["repository"]["canonical_repository"], "example/sample")
            self.assertIsNone(control_plane["repository"]["github_repository_id"])
            self.assertEqual(control_plane["mode_default"], "disabled")
            self.assertEqual(control_plane["adapters"]["response_write"], "disabled")
            self.assertTrue((repo / "scripts" / "human_review_queue.py").exists())
            self.assertIn("review-queue/.runtime/", (repo / ".gitignore").read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
