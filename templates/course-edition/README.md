# Start a course edition

Copy this directory to courses/<course-key>/editions/<edition-key>/ locally.
Use a new course namespace for a new course, or preserve entity IDs when revising
an existing one. Replace placeholder metadata in edition.json; do not overwrite
the five CSV headers. Add the edition to courses/catalog.json.

Populate the five registers from documented sources. Empty rows are not required.
Set based_on for an edition derived from an existing edition. Start as draft with
publication_status not_authorized. Retain versions and references; do not copy
approval from a predecessor onto changed content.

Follow [the record contract](../../records/README.md) and run
`python3 scripts/validate-course-records.py` from the repository root.
Owner review and publication authorization remain separate from validation.
