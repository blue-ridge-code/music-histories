#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Reject unsafe or misleading stable-link updates before they can be deployed."""
from copy import deepcopy
import importlib.util
import json
from pathlib import Path
import unittest

ROOT=Path(__file__).resolve().parents[2]
spec=importlib.util.spec_from_file_location('link_build',ROOT/'scripts/build-link-site.py')
module=importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


class LinkRegistryTests(unittest.TestCase):
    def setUp(self):
        self.data=json.loads((ROOT/'links/resources.json').read_text())
        self.target=next(r['destinations'][0] for r in self.data['resources'] if r['destinations'])

    def test_current_registry_has_valid_references(self):
        resources,destinations=module.validate(self.data)
        self.assertGreater(resources,0)
        self.assertGreater(destinations,0)

    def test_rejects_script_private_and_credential_urls(self):
        for url in ['javascript:alert(1)','http://example.com/video','https://127.0.0.1/a','https://user:secret@example.com/a']:
            with self.subTest(url=url):
                self.target['url']=url
                with self.assertRaises(ValueError):module.validate(self.data)

    def test_rejects_unknown_country(self):
        self.target['countries']=['ZZ']
        with self.assertRaises(ValueError):module.validate(self.data)

    def test_available_claim_requires_human_country_and_date(self):
        self.target['availability']='reported_available'
        self.target['last_verified_on']=None
        self.target['verified_country']=None
        with self.assertRaises(ValueError):module.validate(self.data)

    def test_rejects_duplicate_resource_identity(self):
        self.data['resources'].append(deepcopy(self.data['resources'][0]))
        with self.assertRaises(ValueError):module.validate(self.data)

    def test_rejects_dangling_course_record_reference(self):
        self.data['resources']=[]
        with self.assertRaises(ValueError):module.validate(self.data)


if __name__=='__main__':unittest.main()
