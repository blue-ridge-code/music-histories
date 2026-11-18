#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
# Copyright (c) 2026 Music Histories contributors
"""Validate the stable-link registry and build the dependency-free static site."""
import argparse
import csv
from datetime import date
import ipaddress
import json
from pathlib import Path
import re
import shutil
from urllib.parse import urlsplit

ROOT=Path(__file__).resolve().parents[1]
COUNTRIES=set(re.search(r"COUNTRIES = '([^']+)'",(ROOT/'site/route.mjs').read_text()).group(1).split())


def check(condition, message):
    if not condition:
        raise ValueError(message)


def validate(data):
    check(data.get('schema_version')==1,'Unknown link schema')
    ids=set(); destinations=set()
    for resource in data['resources']:
        rid=resource['id']
        check(bool(re.fullmatch(r'[A-Z0-9]+(?:-[A-Z0-9]+)*',rid)) and rid not in ids,'Invalid/duplicate resource ID')
        ids.add(rid)
        check(resource['kind'] in ['film','listening'] and bool(resource['title']),'Missing resource type/title')
        check(bool(resource['source_refs']),'Missing source provenance')
        check(isinstance(resource['retired'],bool),'Retired must be boolean')
        for d in resource['destinations']:
            check(d['id'].startswith(rid+'-D') and d['id'] not in destinations,'Invalid/duplicate destination ID')
            destinations.add(d['id'])
            u=urlsplit(d['url'])
            check(u.scheme=='https' and bool(u.hostname) and not u.username and not u.password and u.port in [None,443],'Use public HTTPS URLs without credentials')
            check(u.hostname not in ['localhost'] and not u.hostname.endswith(('.local','.internal')),'Private host not allowed')
            try: ip=ipaddress.ip_address(u.hostname)
            except ValueError: ip=None
            check(ip is None or ip.is_global,'Private IP not allowed')
            check(isinstance(d['priority'],int) and d['priority']>=0,'Invalid priority')
            check(bool(d['label']),'Missing destination label')
            check(d['relationship'] in ['curated_recording','same_recording','same_film','alternative_performance'],'Unknown relationship')
            check((resource['kind']=='film')==(d['relationship']=='same_film'),'Destination type mismatches resource')
            check(bool(d['countries']) and set(d['countries'])<=COUNTRIES|{'*'},'Invalid country coverage')
            check(set(d['excluded_countries'])<=COUNTRIES,'Invalid excluded country')
            check(d['availability'] in ['unknown','reported_available','unavailable','retired'],'Unknown availability')
            check(d['access'] in ['unknown','free','subscription','rental','purchase','library'],'Unknown access type')
            check(d['verified_country'] is None or d['verified_country'] in COUNTRIES,'Invalid verified country')
            if d['last_verified_on']:
                date.fromisoformat(d['last_verified_on'])
                check(bool(d['verified_country']),'Country required for human playback check')
            if d['availability']=='reported_available':
                check(bool(d['last_verified_on'] and d['verified_country']),'Available claim needs country/date evidence')
    for course in json.loads((ROOT/'courses/catalog.json').read_text())['courses']:
        for edition in course['editions']:
            base=ROOT/'courses'/course['path']/edition['path']/'records'
            for filename in ['films.csv','listening.csv']:
                with (base/filename).open(newline='',encoding='utf-8') as f:
                    for row in csv.DictReader(f):
                        check(row.get('stable_link_id') in ids,f'Missing stable resource for {filename}')
    return len(ids),len(destinations)


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check',action='store_true')
    args=parser.parse_args()
    data=json.loads((ROOT/'links/resources.json').read_text())
    count,destinations=validate(data)
    config=json.loads((ROOT/'links/config.json').read_text())
    check(config['site_url'].startswith('https://') and config['site_url'].endswith('/'),'Site URL must be HTTPS with trailing slash')
    if not args.check:
        out=ROOT/'dist'
        out.mkdir(exist_ok=True)
        for file in ['index.html','app.mjs','route.mjs','style.css']:
            shutil.copyfile(ROOT/'site'/file,out/file)
        shutil.copyfile(ROOT/'links/resources.json',out/'resources.json')
        (out/'.nojekyll').touch()
    print(f'PASS: {count} stable resources; {destinations} destinations; '+('validated' if args.check else 'built dist/'))


if __name__=='__main__':
    main()
