# Contributing to Music Histories

Read [AGENTS.md](AGENTS.md), the [scope](docs/SCOPE.md), and the
[record contract](records/README.md). Use a branch and a pull request describing
the deliverable, sources, acceptance criteria, and requested reviewer.
Owner review is required for creative approvals; a passing check is not approval.

Original creative contributions use CC BY 4.0; original production software uses
MIT as described in [LICENSE.md](LICENSE.md). By submitting material for inclusion,
confirm you have the rights to contribute it under the applicable license.
Retain source attribution and clearly identify any third-party exceptions.
Do not submit private source links, credentials, or excluded raw assets.

Credit contributors using [the attribution guidance](ATTRIBUTION.md). Add your
preferred public credit to CONTRIBUTORS.md if desired, and preserve other
contributors' notices. No copyright assignment or custom license amendment is
requested.

Before review, run from the repository root:

- `PYTHONDONTWRITEBYTECODE=1 python3 scripts/tests/run_all.py`
- `python3 scripts/validate-course-records.py`
- `git diff --check`

If you have the ignored source originals locally, also run
`python3 scripts/validate-course-records.py --with-local-assets`.
Do not redistribute a referenced film, recording, image, or manuscript merely
because a record points to it.
