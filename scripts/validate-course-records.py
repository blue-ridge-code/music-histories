#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
# Copyright (c) 2026 Music Histories contributors
"""Validate portable course registers; no network access or third-party packages."""
import argparse
import csv
import hashlib
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ERRORS = []


def require(condition, message):
    if not condition:
        ERRORS.append(message)


def rows(path):
    with path.open(newline='', encoding='utf-8') as stream:
        reader = csv.DictReader(stream)
        result = list(reader)
        require(all(None not in row and None not in row.values() for row in result),
                f'{path}: malformed CSV row')
        return reader.fieldnames, result


def unique(records, key, label):
    values = [r.get(key) for r in records]
    require(all(values) and len(values) == len(set(values)), f'{label}: missing/duplicate {key}')
    return set(values)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--with-local-assets', action='store_true')
    args = parser.parse_args()
    catalog = json.loads((ROOT / 'courses/catalog.json').read_text())
    require(catalog.get('schema_version') == 1, 'Unsupported catalog schema')
    courses = catalog['courses']
    unique(courses, 'course_id', 'catalog')
    for course in courses:
        editions = course['editions']
        edition_ids = unique(editions, 'edition_id', course['course_id'])
        for entry in editions:
            base = ROOT / 'courses' / course['path'] / entry['path']
            metadata = json.loads((base / 'edition.json').read_text())
            cid, eid = course['course_id'], entry['edition_id']
            require(metadata.get('schema_version') == 1, f'{eid}: unsupported schema')
            require(metadata.get('course_id') == cid and metadata.get('edition_id') == eid,
                    f'{eid}: metadata identity mismatch')
            require(metadata.get('status') == entry['status'], f'{eid}: catalog status mismatch')
            predecessor = metadata.get('based_on')
            require(predecessor is None or predecessor in edition_ids and predecessor != eid,
                    f'{eid}: invalid predecessor')
            data = {}
            for template in sorted((ROOT / 'templates/course-edition/records').glob('*.csv')):
                name = template.stem
                header, records = rows(base / metadata['records'][name])
                expected, _ = rows(template)
                require(header == expected, f'{eid}/{name}: schema/header mismatch')
                data[name] = records
            films, listening, pages, sources, decisions = [data[k] for k in
                ['films','listening','chapters-pages','sources-rights','decisions']]
            film_ids = unique(films, 'film_id', eid)
            listening_ids = unique(listening, 'listening_id', eid)
            unique(pages, 'record_id', eid)
            source_ids = unique(sources, 'source_id', eid)
            decision_ids = unique(decisions, 'decision_id', eid)
            chapter_ids = {p['record_id'] for p in pages if p['record_type'] == 'chapter'}
            require(bool(chapter_ids), f'{eid}: no chapter records')
            core = [f for f in films if f['selection_type'] == 'core']
            require(len(core) == len(chapter_ids) and
                    {f['chapter_id'] for f in core} == chapter_ids,
                    f'{eid}: core films must map one-to-one to chapters')
            for records in [films, listening, pages, decisions]:
                for row in records:
                    require(row['course_id'] == cid and row['edition_id'] == eid,
                            f'{eid}: row belongs to another course/edition')
                    require(bool(row['reviewer']), f'{eid}: missing reviewer')
            for records in data.values():
                for row in records:
                    require(bool(row['source_refs']), f'{eid}: missing source reference')
                    for ref in row['source_refs'].split(';'):
                        source_id = ref.split('#')[0]
                        if re.fullmatch(r'S\d+|A-CONCEPT-\d+', source_id):
                            require(source_id in source_ids, f'{eid}: unknown source {source_id}')
                    if row.get('evidence_path'):
                        require((base / row['evidence_path']).is_file(),
                                f'{eid}: missing evidence {row["evidence_path"]}')
                    if row.get('chapter_id'):
                        require(row['chapter_id'] in chapter_ids, f'{eid}: invalid chapter link')
            sequences = [f['sequence'] for f in core]
            require(len(set(sequences)) == len(sequences), f'{eid}: duplicate core sequence')
            for row in listening:
                require(row['selected_url'] == (row['manual_override_url'] or row['candidate_url']),
                        f'{row["listening_id"]}: manual override precedence broken')
                require(set(filter(None, row['roles'].split(';'))) <=
                        {'Before','Inside','Beside','After','Bridge'}, 'Unknown normalized role')
                require(row['role_review'] in {'resolved','needs_review'}, 'Invalid role review')
                require(row['scope_status'] != 'verified' or
                        bool(row['assigned_excerpt'] and row['duration_seconds']),
                        f'{row["listening_id"]}: verified scope lacks excerpt/duration')
                require(not row['duration_seconds'] or
                        row['duration_seconds'].isdigit() and int(row['duration_seconds']) > 0,
                        f'{row["listening_id"]}: invalid duration')
            for row in pages:
                require(row['record_type'] in {'chapter','page'}, 'Unknown chapter/page record type')
                require(row['film_id'] in film_ids, f'{eid}: invalid page film reference')
                for lid in filter(None, row['listening_ids'].split(';')):
                    require(lid in listening_ids, f'{eid}: invalid listening link {lid}')
                require(bool(row['deliverable'] and row['acceptance_criteria']),
                        f'{row["record_id"]}: missing deliverable/criteria')
            for row in sources:
                if row['retrieval_status'] == 'recovered':
                    require(bool(re.fullmatch('[0-9a-f]{64}', row['sha256'])),
                            f'{row["source_id"]}: invalid hash')
                    require(row['bytes'].isdigit(), f'{row["source_id"]}: missing byte count')
                    if args.with_local_assets:
                        asset = ROOT / row['local_asset_ref']
                        require(asset.is_file(), f'{row["source_id"]}: missing local original')
                        if asset.is_file():
                            content = asset.read_bytes()
                            require(hashlib.sha256(content).hexdigest() == row['sha256'] and
                                    len(content) == int(row['bytes']),
                                    f'{row["source_id"]}: original checksum/size mismatch')
            for row in decisions:
                require(row['status'] in {'provisional','source_recorded','approved','rejected','superseded'},
                        f'{eid}: unknown decision status')
                require(not row['supersedes'] or row['supersedes'] in decision_ids,
                        f'{eid}: unknown superseded decision')
                if row['status'] == 'approved':
                    require(bool(row['decided_by'] and row['decided_on'] and row['evidence_path']),
                            f'{eid}: approved decision lacks owner/date/evidence')
            if metadata['status'] == 'released':
                require(all(metadata.get(k) for k in ['approved_by','approved_on','release_tag']),
                        f'{eid}: release lacks approval or tag')
                require(metadata.get('publication_status') == 'authorized',
                        f'{eid}: release not authorized')
            print(f'{eid}: {len(films)} films; {len(listening)} selections; {len(pages)} chapter/page records')
            print(f'  Draft review: {sum(r["role_review"] == "needs_review" for r in listening)} role labels; '
                  f'{sum(r["scope_status"] != "verified" for r in listening)} unverified listening scopes; '
                  f'{sum(r["rights_status"] == "not_assessed" for r in sources)} rights assessments outstanding')
    for error in ERRORS:
        print('FAIL:', error)
    print('FAIL' if ERRORS else 'PASS: record structure and references valid; content approval remains separate')
    return bool(ERRORS)


if __name__ == '__main__':
    raise SystemExit(main())
