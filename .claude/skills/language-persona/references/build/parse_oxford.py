#!/usr/bin/env python3
"""Parse .extract-tmp/oxford.txt (pdftotext -layout dump of American_Oxford_3000.pdf)
into .agents/skills/language-persona/references/oxford-3000-wordlist.md.

Layout facts about the source dump (verified by inspection, see generation report):
- ISO-8859-1 text, CRLF; 4-column layout, columns separated by 2+ spaces.
- Each cell is `word pos. LEVEL` where LEVEL in {A1, A2, B1, B2}; a cell may carry
  several (pos, level) groups, e.g. `young adj. A1, n. B1`, and pos may itself be a
  list sharing one level, e.g. `about prep., adv. A1`.
- Footer lines contain `(C) Oxford University Press`, the title, and `N / 11` page
  markers; some page markers/titles leaked onto their own lines.
- Form feeds (\\x0c) prefix the first data line of pages 2..11.
- 5 long cells were wrapped by the extraction: the head stays on its row and the
  orphaned tail lands 1-3 lines lower in the same column. All 5 were verified
  against the raw PDF text stream (`pdftotext` without -layout).

Run from the repo root:  python .extract-tmp/parse_oxford.py
Exits non-zero and writes nothing if any cell fails to parse.
"""

import random
import re
import sys
from collections import defaultdict
from pathlib import Path

SRC = Path(".extract-tmp/oxford.txt")
OUT = Path(".agents/skills/language-persona/references/oxford-3000-wordlist.md")

LEVEL = r"(?:A1|A2|B1|B2)"
# Part-of-speech atoms actually occurring in the source (enumerated by a scan of the
# dump; anything new makes the parse fail loudly rather than guess).
ATOM = (
    r"(?:n\.|noun\.|v\.|adj\.|adv\.|prep\.|conj\.|pron\.|det\.|exclam\.|number"
    r"|article|marker|modal|auxiliary|indefinite|definite|infinitive)"
)
# A pos phrase: atoms joined by ", " (list sharing a level), " " (e.g. "modal v.",
# "indefinite article") or "/" (e.g. "det./pron.", "conj./prep.").
POSSEQ = rf"{ATOM}(?:(?:, |/| ){ATOM})*"
# One (pos, level) group. \s* before the level because the source dump has two
# cells with a missing space ("adv.B1", "n.B1").
GROUP = rf"{POSSEQ}\s*{LEVEL}"
TAIL_RE = re.compile(rf"(?P<groups>{GROUP}(?:, {GROUP})*)$")
GROUP_RE = re.compile(rf"(?P<pos>{POSSEQ})\s*(?P<level>{LEVEL})")
ORPHAN_RE = re.compile(rf"^(?:{GROUP}(?:, {GROUP})*|{LEVEL})$")  # tail fragment, no word
# Truncated head: word + optional complete groups + optional trailing level-less
# pos fragment, ending mid-cell (possibly with a dangling "," or "/").
HEAD_RE = re.compile(rf"^.+?\s+(?:{GROUP}(?:, {GROUP})*)?(?:, ?)?(?:{POSSEQ}[,/]?)?$")
PAGE_MARK_RE = re.compile(r"^\d+ / 11$")


def blank_out(line, span):
    """Replace a junk span with spaces, preserving x positions of later cells."""
    return line[: span[0]] + " " * (span[1] - span[0]) + line[span[1] :]


def split_cells(line):
    """Split one layout line into (x_start, cell_text) pairs."""
    out = []
    for m in re.finditer(r"\S(?:.*?\S)?(?=\s{2,}|$)", line):
        out.append((m.start(), m.group(0).strip()))
    return out


def clean_lines(text):
    """Yield (line_no, [(x, cell), ...]) for data lines, junk filtered."""
    for ln, raw in enumerate(text.split("\r\n")):
        line = raw.lstrip("\x0c")
        if not line.strip():
            continue
        if "\xa9" in line:  # page footer; may still carry a real word cell
            for pat in (r"\xa9 Oxford University Press",
                        r"The Oxford 3000TM \(American English\)",
                        r"\d+ / 11"):
                for m in re.finditer(pat, line):
                    line = blank_out(line, m.span())
        cells = [
            (x, c)
            for x, c in split_cells(line)
            if c
            and not c.startswith("The Oxford 3000")  # doc title/description/TM title
            and not PAGE_MARK_RE.match(c)
        ]
        if cells:
            yield ln, cells


def assign_pages_and_columns(line_cells):
    """Group data lines into pages (split at form-feed boundaries is already lost,
    so pages are delimited by the footer positions we saw) and cluster each page's
    cell x-starts into columns. Returns list of (ln, col, cell)."""
    # Footer line numbers delimit pages; recover them from the raw text instead of
    # hardcoding: a page break is wherever a footer line (containing \xa9) or a bare
    # page-marker line sits. We already filtered those lines out, so instead use
    # gaps: pages start right after each filtered footer/marker line. Simplest
    # robust proxy: x-cluster per maximal run of consecutive data lines.
    items = []  # (ln, col, cell)
    run = []
    prev_ln = None
    runs = []
    for ln, cells in line_cells:
        if prev_ln is not None and ln > prev_ln + 1:
            runs.append(run)
            run = []
        run.append((ln, cells))
        prev_ln = ln
    if run:
        runs.append(run)

    for ri, run in enumerate(runs):
        # Column centers = the 4 most frequent x-starts (each column repeats on
        # ~60+ lines with small jitter; outliers are rare one-off cells).
        freq = defaultdict(int)
        for _, cells in run:
            for x, _ in cells:
                freq[x] += 1
        centers = []
        pool = dict(freq)
        for _ in range(4):
            if not pool:
                break
            cx = max(pool, key=lambda x: (pool[x], -x))
            centers.append(cx)
            pool = {x: n for x, n in pool.items() if abs(x - cx) > 10}
        centers.sort()
        col_of = {x: min(range(len(centers)), key=lambda i: abs(x - centers[i]))
                  for x in freq}
        print(
            f"  run {ri}: lines {run[0][0]}-{run[-1][0]}, "
            f"column centers {centers}, x-jitter "
            f"{sorted({x: c for x, c in col_of.items() if abs(x - centers[c]) > 4}) or 'none'}"
        )
        if len(centers) != 4:
            print(f"  WARNING: run {ri} has {len(centers)} column centers (expected 4)")
        for ln, cells in run:
            for x, c in cells:
                items.append((ln, col_of[x], ri, c))
    return items


def parse_cell(cell):
    """Parse a complete cell -> (word, [(pos, level), ...]) or None."""
    m = re.match(rf"^(?P<word>.+?)\s+(?P<tail>{GROUP}(?:, {GROUP})*)$", cell)
    if not m:
        return None
    groups = [(g.group("pos"), g.group("level")) for g in GROUP_RE.finditer(m.group("tail"))]
    return m.group("word"), groups


def main():
    text = SRC.read_bytes().decode("latin-1")
    line_cells = list(clean_lines(text))
    print(f"data lines kept: {len(line_cells)}")

    items = assign_pages_and_columns(line_cells)
    print(f"cells after junk filtering: {len(items)}")

    # --- pass 1: classify cells. Orphan-looking cells are deferred: a cell like
    # "number n. A1" is a real entry (word "number") even though it also matches
    # the orphan shape, so orphan-hood is decided by whether a truncated head is
    # waiting for it in the same column.
    entries = []  # [run, col, ln, cell_text, word, groups, repaired]
    heads = []    # cells that parse as word + incomplete tail
    orphan_cands = []
    failures = []
    for ln, col, ri, cell in items:
        if ORPHAN_RE.match(cell):  # includes a bare level like "B1"
            orphan_cands.append((ri, col, ln, cell))
            continue
        parsed = parse_cell(cell)
        if parsed:
            word, groups = parsed
            entries.append([ri, col, ln, cell, word, groups, False])
        elif HEAD_RE.match(cell):
            heads.append((ri, col, ln, cell))
        else:
            failures.append((ln, cell))

    print(f"complete cells: {len(entries)}")
    print(f"truncated heads: {len(heads)} -> {[c for _, _, _, c in heads]}")
    print(f"orphan candidates: {len(orphan_cands)} -> {[c for _, _, _, c in orphan_cands]}")
    if failures:
        print(f"FAILED CELLS: {len(failures)}")
        for ln, c in failures:
            print(f"  line {ln}: {c!r}")
        sys.exit(1)

    # --- pass 2: pair each orphan candidate with the nearest unmatched head above
    # it in the same run/column (within 3 lines); no waiting head -> real entry ---
    used_heads = set()
    repairs = {}  # joined cell -> (head cell, head ln, orphan cell, orphan ln)
    for ri, col, ln, ocell in orphan_cands:
        cands = [
            (hln, hcell)
            for hri, hcol, hln, hcell in heads
            if hri == ri and hcol == col and 0 < ln - hln <= 3 and hln not in used_heads
        ]
        if not cands:
            parsed = parse_cell(ocell)
            if not parsed:
                print(f"ORPHAN-LOOKING CELL DOES NOT PARSE AS ENTRY: {ocell!r} line {ln}")
                sys.exit(1)
            word, groups = parsed
            entries.append([ri, col, ln, ocell, word, groups, False])
            print(f"orphan-shaped but real entry (no head waiting): {ocell!r} line {ln}")
            continue
        if len(cands) != 1:
            print(f"PAIRING FAILURE for orphan {ocell!r} at line {ln}: candidates {cands}")
            sys.exit(1)
        hln, hcell = cands[0]
        used_heads.add(hln)
        joined = hcell + ("" if hcell.endswith("/") else " ") + ocell
        parsed = parse_cell(joined)
        if not parsed:
            print(f"REPAIRED CELL STILL FAILS: {joined!r}")
            sys.exit(1)
        word, groups = parsed
        entries.append([ri, col, hln, joined, word, groups, True])
        repairs[joined] = (hcell, hln, ocell, ln)
    if len(used_heads) != len(heads):
        print("UNPAIRED HEADS:", [h for h in heads if h[2] not in used_heads])
        sys.exit(1)
    print("repaired wrapped cells (verified against raw PDF text stream):")
    for joined, (hcell, hln, ocell, oln) in repairs.items():
        print(f"  lines {hln}+{oln}: {joined}")

    # --- order: page (run), then column, then line -> the published A-Z order ---
    entries.sort(key=lambda e: (e[0], e[1], e[2]))

    # --- emit rows: one per (word, pos, level) group ---
    rows = []  # (word, pos, level, source_cell, source_line, repaired)
    for ri, col, ln, cell, word, groups, repaired in entries:
        for pos, level in groups:
            rows.append((word, pos, level, cell, ln, repaired))
    print(f"word entries (cells): {len(entries)}")
    print(f"table rows (one per pos/level group): {len(rows)}")

    # --- alphabetical validation (source order is authoritative; we just report) ---
    seq = [w.casefold() for w, *_ in rows]
    dips = [(i, rows[i - 1][0], rows[i][0]) for i in range(1, len(seq)) if seq[i] < seq[i - 1]]
    print(f"casefold dips vs source order (publisher conventions, informational): {len(dips)}")
    for i, a, b in dips:
        print(f"  row {i}: {a!r} -> {b!r}")

    # Publisher's ordering, modeled: letter-by-letter on [a-z] with a space ranking
    # BEFORE any letter ("nothing before something": "all right" < "allow"), other
    # punctuation and homonym digits ignored ("o'clock" -> "oclock",
    # "long1" -> "long" < "longterm"). Same-headword homonym groups
    # ("bear (deal with)" before "bear (animal)") are editorial - exempt.
    def alpha_key(word):
        s = re.sub(r"[^a-z ]", "", word.casefold())
        return s.replace(" ", "\x00")

    violations = []
    homonym_pairs = []
    for i in range(1, len(rows)):
        prev, cur = rows[i - 1][0], rows[i][0]
        if alpha_key(cur) < alpha_key(prev):
            if cur.split(" ", 1)[0].split("(", 1)[0] == prev.split(" ", 1)[0].split("(", 1)[0]:
                homonym_pairs.append((i, prev, cur))
            else:
                violations.append((i, prev, cur))
    print(f"same-headword homonym pairs in publisher's editorial order: {len(homonym_pairs)}")
    for i, a, b in homonym_pairs:
        print(f"  row {i}: {a!r} -> {b!r}")
    if violations:
        print(f"ALPHABETICAL VIOLATIONS: {len(violations)}")
        for i, a, b in violations:
            print(f"  row {i}: {a!r} -> {b!r}")
        sys.exit(1)
    print("alphabetical order (publisher model): monotonic - OK")

    # --- spot-check 10 random rows against the RAW source lines ---
    raw_lines = text.split("\r\n")
    random.seed(42)
    picks = sorted(random.sample(range(len(rows)), 10))
    print("spot-check (10 random rows vs raw source line):")
    ok = True
    for i in picks:
        word, pos, level, cell, ln, repaired = rows[i]
        if repaired:
            # joined cell spans two raw lines; both fragments must be verbatim
            hcell, hln, ocell, oln = repairs[cell]
            hit = hcell in raw_lines[hln] and ocell in raw_lines[oln]
        else:
            # unrepaired cells must appear verbatim in the raw line they came from
            hit = cell in raw_lines[ln]
        # and the row's own fields must be consistent with the cell text
        hit = hit and cell.startswith(word) and pos in cell and level in cell
        ok = ok and hit
        print(
            f"  row {i}: | {word} | {pos} | {level} |  <= line {ln}: {cell!r}"
            f"  {'OK' if hit else 'MISMATCH'}"
        )
    if not ok:
        sys.exit(1)

    # --- distinct pos phrases for the record ---
    phrases = sorted({pos for _, pos, *_ in rows})
    print(f"distinct part-of-speech phrases ({len(phrases)}): {phrases}")

    # --- write the markdown ---
    n_words = len({w for w, *_ in rows})
    header = f"""# Oxford 3000 word list (American English) — agent lookup table

> Provenance: factual derivative of `American_Oxford_3000.pdf` ("The Oxford 3000™
> (American English)", © Oxford University Press) — a licensed standard kept beside
> this file; redistribute nothing but these facts. Generated by
> `.extract-tmp/parse_oxford.py` from the PDF text extraction; the PDF is the
> standard of record — do not hand-edit this file, regenerate it.

## What this list is

The Oxford 3000 is the list of the 3000 most important words to learn in English,
from A1 to B2 level (CEFR). This file is the American English edition as a flat
table: {len(rows)} rows covering {n_words} word entries, alphabetical A–Z (the
published order of the source list).

## How agents use it in this template

- **Persuasive register** (see `docs/agents/language.md` + `docs/TONE.md`): prefer
  on-list words when drafting for a general audience.
- **Before using an off-list word, grep this file first**, e.g.
  `grep -iF '| alleviate |' .agents/skills/language-persona/references/oxford-3000-wordlist.md`
  (`alleviate` is off-list — no output). A hit needs no justification.
- **Off-list is acceptable** when the word is settled project vocabulary from
  `CONTEXT.md` (which overrides this list) or load-bearing jargon the audience
  expects — flag it, don't silently swap in a plainer word.
- **The Level column supports tuning**: A1/A2 = safest for the widest audiences;
  B1/B2 fine for fluent or professional readers.

## Conventions kept from the source

- Homonym numbers (`close1`/`close2`), sense disambiguators (`bank (money)` vs
  `bank (river)`), and multi-part-of-speech entries appear exactly as published.
- One row per (word, part-of-speech, level) group: `young adj. A1, n. B1` becomes
  two rows — `young | adj. | A1` and `young | n. | B1`.
- The Part of speech column lists every pos sharing one level, e.g.
  `about | prep., adv. | A1`; `a, an | indefinite article | A1`.

| Word | Part of speech | Level |
| --- | --- | --- |
"""
    body = "".join(f"| {w} | {p} | {l} |\n" for w, p, l, *_ in rows)
    OUT.write_text(header + body, encoding="utf-8", newline="\n")
    print(f"wrote {OUT} ({len(rows)} rows)")


if __name__ == "__main__":
    main()
