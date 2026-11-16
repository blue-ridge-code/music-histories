#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
# Copyright (c) 2026 Music Histories contributors
"""Guard the template entry points lost during the Music Histories rewrite.

These checks verify instruction wiring, not an agent's compliance with policy.
The negative scenarios reject removal of a whole instruction section even when
all referenced implementation files remain present.
"""
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[2]

SECTIONS = {
    'Rule #1 — Kickoff first': ['kickoff-pending', 'planning-active', 'implementation-ready', 'docs/agents/lifecycle.md'],
    'Source-of-truth map (which file wins)': ['docs/TONE.md', 'CONTEXT.md', 'docs/MAINTENANCE.md', 'docs/agents/skills.md', 'docs/agents/layer-activation-guide.md'],
    'Human gates': ['human-review-queue', 'dispatch disabled', 'loopback', 'explicit user decision', 'default browser'],
    'Evidence rule': ['file:line', 'unverified'],
    'Untrusted intake': ['data, not instructions', 'docs/agents/intake.md'],
    'Provider independence (plug-and-play)': ['portable formats', 'registries'],
    'Token discipline': ['Hand off between sessions by file', 'docs/agents/token-efficiency.md'],
    'Doc hygiene': ['Supersede, don’t delete', 'No speculative scaffolding', 'documentation-audit'],
    '`docs/agents/` index': ['model-roles.md', 'skills.md', 'skill-composition-map.md', 'skill-verification-checklist.md', 'services.md', 'utilities.md', 'issue-tracker.md', 'intake.md', 'lifecycle.md', 'language.md', 'voice/'],
    'Conventions': ['YYYY-MM-DD', 'PowerShell', 'bash equivalents', '.gitignore'],
}


def section(text, heading):
    match = re.search(r'^## ' + re.escape(heading) + r'\n(.*?)(?=^## |\Z)', text, re.M | re.S)
    return match.group(1) if match else ''


def instruction_errors(text):
    # Normalize typographic apostrophes only; section names remain deliberate.
    errors = []
    for heading, requirements in SECTIONS.items():
        body = section(text, heading).replace('’', "'")
        for required in requirements:
            if required.replace('’', "'") not in body:
                errors.append(f'{heading}: missing {required}')
    return errors


class InstructionWiringTests(unittest.TestCase):
    def test_root_instructions_retain_operational_entry_points(self):
        self.assertEqual(instruction_errors((ROOT/'AGENTS.md').read_text()), [])

    def test_removing_each_operational_chunk_is_detected(self):
        text = (ROOT/'AGENTS.md').read_text()
        for heading in SECTIONS:
            with self.subTest(heading=heading):
                removed = re.sub(r'^## ' + re.escape(heading) + r'\n.*?(?=^## |\Z)', '', text, flags=re.M | re.S)
                self.assertTrue(instruction_errors(removed))

    def test_discovered_operational_documents_and_tools_exist(self):
        for path in ['docs/agents/lifecycle.md', 'docs/agents/intake.md',
                     'docs/agents/language.md', 'docs/agents/token-efficiency.md',
                     'docs/agents/skills.md', 'docs/agents/skill-composition-map.md',
                     'docs/agents/skill-verification-checklist.md',
                     'docs/agents/model-roles.md', 'docs/agents/issue-tracker.md',
                     'docs/agents/layer-activation-guide.md', 'docs/MAINTENANCE.md',
                     '.agents/skills/kickoff/SKILL.md',
                     '.agents/skills/human-review-queue/SKILL.md',
                     '.agents/skills/documentation-audit/SKILL.md',
                     'scripts/sync-skills.sh']:
            with self.subTest(path=path):
                self.assertTrue((ROOT/path).is_file())

    def test_agent_adapters_still_route_to_the_root(self):
        for path in ['CLAUDE.md', '.github/copilot-instructions.md']:
            with self.subTest(path=path):
                self.assertIn('AGENTS.md', (ROOT/path).read_text())

    def test_project_authorization_does_not_erase_human_gates(self):
        text = (ROOT/'AGENTS.md').read_text()
        self.assertIn('standing authorization', text)
        project = section(text, 'Project-specific policy')
        for phrase in ['routine commits', 'raw manuscripts', 'Creative gates',
                       'reviewer', 'sole task', 'migrate once']:
            self.assertIn(phrase.lower(), project.lower())
        self.assertIn('Device or hardware permissions', section(text, 'Human gates'))


if __name__ == '__main__':
    unittest.main()
