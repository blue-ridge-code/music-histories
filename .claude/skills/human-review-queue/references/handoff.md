# Human gate handoff

Use this order when work pauses for a human response.

```markdown
Human action needed: <verb> <specific object>

Why this needs you: <blocked work, human-only reason, and Type A or B>

Review path:
1. <open the exact URL, file, timecode, or control>
2. <inspect the exact evidence>
3. <compare it with the named criteria>

Decision: <one bounded question>

- <choice> (Recommended) - <reason>
- <choice> - <effect>
- Other - <required detail>

Reply with: No IDE reply is required when the queue confirms "Response recorded."

Fallback if the queue is unavailable: `<copy-ready response>`

What each answer does: <unlock, revision, hold, stop, and new-review behavior>

Recorded in: <tracker and decision-record destination>
Queue: <URL, reviewer page, and entry ID>
```

Before the pause:

1. Enqueue the validated entry.
2. Confirm the exact item is inspectable.
3. Confirm the assigned reviewer and route.
4. Confirm all Agent Action fields and the fixed project boundary.
5. Release the current tracker claim when the repo requires it.
6. Verify HTTP 200.
7. Open the review link in the default browser so the reviewer does not copy-paste it
   (`Start-Process <url>` on Windows; `open <url>` on macOS; `xdg-open <url>` on Linux).
8. Tell the reviewer that the queue records the response before follow-up.

Do not combine unrelated decisions. Batch related consequential decisions only at a natural checkpoint. A Review Decision applies only to the named version and criteria.
