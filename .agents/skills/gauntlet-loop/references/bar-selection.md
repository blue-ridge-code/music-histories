# Choosing the bar

The bar is the part that fails most often, and when it fails the whole run is theatre: the critic invents a comparison, passes everything, and you get a confident ledger full of nothing.

## The three tests

A bar must pass all three before the loop starts.

**Named.** A specific thing, not a category. "Stripe's pricing page" not "great SaaS design". "Django's `contrib/auth` implementation" not "clean architecture". "The 95th-percentile latency of the current service" not "fast".

**Fetchable.** The critic can actually get it, this run, with the tools it has: screenshot the page, clone the repo, read the post, run the benchmark, open the PDF. Test this before launching. If the reference sits behind a login, a paywall, or a robots block, either mirror it locally into `gauntlet/reference/` or pick a different one.

**Comparable.** The two can sit side by side and a judge can pick one. A React app and a Figma file are not comparable. A rendered screenshot of the React app and a screenshot of the Figma frame are.

## Set it out of reach

The bar does not need to be realistically achievable and generally should not be. Shumer's game never became better than Call of Duty; the point was that the reference kept the agent from stopping at "pretty good for AI". A reachable bar gets reached in round two and the loop ends early with a mediocre artifact and a passing verdict.

Pick something you would be delighted to match and expect not to.

## Mirror it locally

Before launching, save the reference into `gauntlet/reference/` — screenshots at the viewport sizes that matter, the fetched article, the cloned repo, the recorded benchmark. Three reasons: the critic gets identical evidence every round instead of whatever the network returned that minute, live sites change under you, and you can prove afterwards what was actually being compared.

## What a bar looks like by domain

| Work | Weak bar | Strong bar |
|---|---|---|
| Landing page | "modern and clean" | Linear's homepage, screenshotted at 1440px and 390px, in `gauntlet/reference/` |
| Long-form writing | "engaging and clear" | Three named essays by a specific writer, plus a stated test: which one does a non-specialist finish faster |
| API service | "production ready" | A named reference implementation, plus p95 latency under Xms on a stated load, plus its own test suite passing |
| Data pipeline | "robust" | A recorded failure-injection run the current pipeline survives |
| Research brief | "thorough" | A named analyst report on an adjacent topic, judged on: could a reader act on this without asking a follow-up |
| Slide deck | "professional" | A specific published deck, compared slide-for-slide on information per slide |
| Internal tool UI | "intuitive" | A named tool doing the same job, compared on clicks-to-outcome for three named tasks |

## Two bars are better than one where taste is involved

For subjective work, pair a taste bar with a measurable one — a named page *and* a Lighthouse score, a named essay *and* a reading-level ceiling. The measurable bar is the anchor the critic cannot rationalize around; the taste bar is what you actually want. Either alone drifts: pure taste drifts toward whatever the model finds pretty, pure measurement drifts toward a good number attached to a bad artifact.

## Turning the bar into questions

Give each piece three to five specific questions rather than a general instruction to compare. Decomposing evaluation into targeted questions measurably beats holistic judging, and questions written for the particular piece beat generic dimensions — the effect is large enough to be the main lever you have on critic quality.

A usable question is answerable by looking at the artifact, and answerable yes/no or as a pick against the reference.

| Instead of | Ask |
|---|---|
| "Is the design good?" | "Placed beside the reference, which page's primary action is found faster?" |
| "Is the writing clear?" | "Does any paragraph require re-reading to parse? Quote it." |
| "Is the code clean?" | "Can the error path be traced from entry to log line without opening a third file?" |
| "Does it feel premium?" | "Which of the two has more consistent spacing between sections?" |

Note what the bad column has in common: it invites a general impression, which is where verbosity bias and generic polish live. The good column names something observable.

One warning: a set of narrow questions is bad at noticing what is missing entirely. That is why the protocol runs a separate holistic critic per wave asking only about absence. Do not try to cover omissions with a question — decomposition is the wrong tool for it.

## When you do not know the bar

Make finding it the first task. Ask the agent to propose two or three concrete references, explain in one sentence why each is a useful bar, and confirm it can actually fetch each one — then you pick. Do not delegate the choice itself. The bar is where your taste enters the system, and it is the only place it does.
