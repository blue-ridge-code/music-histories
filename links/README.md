# Stable film and listening links

A workbook points to a persistent resource ID rather than a provider's current
URL. Maintainers can repair or add destinations without changing printed links.
Country choices filter the available publications; exact assignments stay visible.

## Address and deployment

Planned base: `https://blue-ridge-code.github.io/music-histories/`.
Example: `https://blue-ridge-code.github.io/music-histories/?id=MH-C001-L005`.
This is a deployment target, not a claim that the site is live. Do not print URLs
or QR codes until the deployed address is verified.

The [Pages workflow](../.github/workflows/stable-links.yml) validates/builds changes
and deploys only from main. In repository Settings → Pages, select **GitHub Actions**
as the source. Merge the implementation, then run the Stable links workflow if a
deployment was not already triggered. A stable HTTPS domain owned by the project
would make future repository/hosting moves easier; no domain has been purchased.
Update config.json and preserve existing addresses/redirects before any migration.

The site is static: no account system, server, paid geolocation service, analytics,
or collection of precise location. Choose a country once; it is saved only in the
browser. A URL may explicitly include `&country=DE`. Browser language is not treated
as physical location. Automatic IP-based selection would require a later hosting
or geolocation-service decision; readers must still be able to override it.

## Maintaining a destination

Edit [resources.json](resources.json) on a branch or through GitHub's pencil editor.
Find the resource ID from the workbook/site. Submit a PR with the country, service,
date checked, access cost and recording/film identity. A maintainer reviews and
merges it. Readers can also use the site's report form to open a GitHub issue;
reporting requires a GitHub account, viewing the directory does not.

- Keep resource IDs forever. Reordering a course must not change them. Retired
  resources keep their landing page and explanation; IDs are never reassigned.
- The original 60 curated listening URLs are imported as availability unknown.
  Sixteen film resources intentionally have no viewing destinations yet. No
  regional sources or playback checks have been invented.
- Repair a removed upload with the same film/version or curated performance where
  possible. Keep the old destination as retired and add a new destination ID.
- If another performance is offered, label it `alternative_performance`. A new
  intended recording/assignment needs a new stable resource ID; old printed links
  must not silently change their pedagogical meaning. Editions may share an ID
  only while the intended film/recording and assignment remain the same.
- Preserve preferred recording versus actual curated choice; imported selection
  notes explain differences. The source spreadsheet's Manual Override is retained.
- Keep the full work/recording container separate from the assigned excerpt.
  MH-C001-L005 is only the Commendatore scene, not the full-opera assignment.
- Store only public provider URLs, never private account/signed URLs or credentials.

Each destination records `id`, `url`, `label`, `relationship`, `countries`,
`excluded_countries`, `access`, `availability`, `priority`, `last_verified_on`,
`verified_country`, and `notes`.

Countries use ISO two-letter codes (`US`, `GB`, `DE`, etc.). `countries: ["*"]`
means an unspecified fallback, **not verified worldwide availability**. For a
known country-specific publication, use e.g. `["DE", "AT"]`. Exclusions override
inclusions. Country-specific sources appear first, then unspecified fallbacks;
within each group lower priority numbers appear first. No automatic redirect hides
the choice, access cost, recording differences or uncertainty from the reader.

`availability` is `unknown`, `reported_available`, `unavailable`, or `retired`.
Unavailable/retired destinations are hidden but preserved. An availability report
requires a human check date and country. That one check does not prove other
countries work. Each claimed country needs its own evidence in notes or the PR.
Expired human checks should be rechecked; no age threshold turns them into a new
availability claim. Empty matches show a clear report/suggestion route.

## Community review checklist

1. Correct resource ID, exact film/recording/version and assigned excerpt?
2. Legitimate publication, explicit alternative if different, no restrictions bypass?
3. Country, date, service and free/subscription/rental/purchase/library access noted?
4. Public HTTPS URL; existing IDs/history preserved; rights not inferred from a link?
5. Validator/tests pass; maintainer reviewed the actual destination where possible?

Film and recording rights remain with their owners. The resolver links to
publications; it does not mirror media or bypass paywalls/geographic restrictions.

## Monitoring and validation

Run from the repository root:

```sh
python3 scripts/validate-course-records.py
python3 scripts/build-link-site.py
node --test scripts/tests/link-routing.test.mjs
python3 -m http.server 8765 --bind 127.0.0.1 --directory dist
```

The build validates destination data, country codes and register references.
Country/exclusion/priority/retirement behavior is covered by nine routing tests.
Browser testing during implementation exercised country persistence, mobile fit,
the exact Commendatore assignment, unknown IDs, empty film destinations, and a
synthetic country-specific alternative. Synthetic sources are not in the registry.

The [health workflow](../.github/workflows/link-health.yml) runs weekly on Monday
at 08:20 UTC and manually on demand. It stores a dated JSON observation artifact
for 90 days and never rewrites the registry or silently substitutes recordings.
Download the artifact from the Actions run and review suspicious observations.
Compare dated observations to measure actual decay; no failure rate is assumed.

HTTP checks use an explicit provider-host allowlist in config.json, follow only
allowlisted HTTPS redirects, and limit concurrency/read size/time. Add a new
provider to that list when monitoring it is appropriate. A 200 response only
means the page responded: login walls, removed-video pages and regional playback
failures can still return 200. Network errors are inconclusive. Human country and
playback reports remain necessary. GitHub Actions schedules are best effort.

Course-record schema 2 adds stable_link_id to film/listening manifests. The raw
selected_url remains source evidence; the separately maintained resolver is the
current destination authority. New editions/templates use these references.

Original site/monitoring code uses MIT; original registry content/documentation
uses CC BY 4.0, subject to third-party exclusions in LICENSE.md.
