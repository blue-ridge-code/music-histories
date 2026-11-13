#!/usr/bin/env python3
"""Parse the ASD-STE100 Issue 9 dictionary (Part 2) into a grep-target
markdown lookup table.

Input : .extract-tmp/ste-table.txt  -- regenerated automatically with
          pdftotext -f 149 -l 434 -enc UTF-8 -table <PDF>  if missing.
          (PDF pages 149-434 = book pages 2-1-A1 .. 2-1-Y2, the dictionary.
           `-table` mode keeps the 4 columns row-aligned, unlike the raw
           reading-order extract where each page's columns come as separate
           blocks.)
Output: .agents/skills/language-persona/references/ste-100-dictionary.md

Model: per page, column cut positions are taken from the header line
"(part of speech)  ALTERNATIVES  STE EXAMPLE  Non-STE example".  Every
content line is sliced into 4 cells.  Column-1 cells assemble into entries
(headword, possibly wrapped / hyphen-split; (pos) tag; verb & adjective
forms).  Columns 2-4 lines attach to the entry whose row-band they fall in
(everything after the entry's headword line, before the next headword line).
Anything the state machine cannot classify confidently is emitted in a
"Needs manual review" section -- never guessed.
"""
import re
import subprocess
import sys
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
PDF = ROOT / ".agents/skills/language-persona/references/ASD-STE100_ISSUE9.pdf"
TABLE_TXT = HERE / "ste-table.txt"
OUT = ROOT / ".agents/skills/language-persona/references/ste-100-dictionary.md"

POS = r"(?:n|v|adj|adv|prep|conj|pron|det|art|num|prefix|TN|TV)"
TAG_RE = re.compile(r"^(?P<head>.*?)\s*\((?P<pos>" + POS + r")\)(?P<tail>.*)$")
POS_ONLY_RE = re.compile(r"^\((" + POS + r")\)$")
ALT_RE = re.compile(r"^[A-Z0-9][A-Z0-9 .,&/'+\-\[\]]*\(" + POS + r"\)[.,]?$")
ALTNP_RE = re.compile(r"^[A-Z0-9][A-Z0-9 ,&/'+\-\[\]]*$")
MARKER_RE = re.compile(r"^For other meanings, use:?\s*(?P<rest>.*)$", re.I)
# col1 forms lines: OCCURRED / ABSORBS, / (EASIER, / EASIEST) / IS, WAS,
FORMSY_RE = re.compile(
    r"^(\([A-Z0-9 ,')-]*\)?,?|[A-Z0-9'-]+\)?,?|"
    r"[A-Z0-9'-]+(?:, [A-Z0-9'-]+)+,?)$")
FORMS_NOTE_RE = re.compile(r"^(No other\b.*|\(also [A-Z ,]+\)|forms?\.?)$")
NOISE_RE = re.compile(
    r"(Part 2 - Dictionary|Page 2-\d|^\s*Issue 9|^\s*2025-01-15|"
    r"Simplified Technical\s+English|Blank Page|"
    r"^\s*Word\s+Approved|^\s*\(part of speech\)|STE EXAMPLE)")


def ensure_table_txt():
    if TABLE_TXT.exists():
        return
    subprocess.run(
        ["pdftotext", "-f", "149", "-l", "434", "-enc", "UTF-8", "-table",
         str(PDF), str(TABLE_TXT)], check=True)


def norm(s):
    # U+F0B0 is the degree glyph from the PDF's symbol font; U+00B0 is the
    # same character in standard encoding
    return re.sub(r"\s+", " ", s).strip().replace("\uf0b0", "°")


def join_lines(lines):
    """Join wrapped cell lines.  A line that ends with '-' continues the
    word on the next line without an intervening space ('TRICHLORO-' +
    'ETHYLENE', 'double-' + 'sided'); all other breaks join with a space."""
    out = ""
    for s in lines:
        if out.endswith("-"):
            out += s
        else:
            out = (out + " " + s) if out else s
    return norm(out)


# ---------------------------------------------------------------- slicing

def iter_cells():
    """Yield (page_idx, c1, c2, c3, c4) for every content line."""
    pages = TABLE_TXT.read_text(encoding="utf-8").split("\f")
    for pi, page in enumerate(pages):
        lines = page.split("\n")
        cuts = None
        for l in lines:
            if "STE EXAMPLE" in l and "ALTERNATIVES" in l:
                cuts = (l.find("ALTERNATIVES"), l.find("STE EXAMPLE"),
                        l.find("Non-STE example"))
        if cuts is None:
            continue  # header/footer-only page (e.g. blank back page)
        c2x, c3x, c4x = cuts
        for l in lines:
            if NOISE_RE.search(l):
                continue
            cells = []
            for a, b in ((0, c2x), (c2x, c3x), (c3x, c4x), (c4x, None)):
                seg = l[a:b] if b is not None else l[a:]
                cells.append(norm(seg) if len(l) > a else "")
            if any(cells):
                yield pi, *cells


# ------------------------------------------------------------- col1 entries

def new_entry(page):
    return {"page": page, "head": "", "pos": "", "forms": [],
            "c2": [], "c3": [], "c4": [], "flags": []}


def assemble_entries():
    """Global line stream -> entries.

    col1 line cases:
      - has (pos) tag and a headword            -> new entry
      - has (pos) tag, no headword              -> completes the pending
        headword entry (headword line came first, tag on the next line)
      - has (pos) tag and a headword while a headword is pending -> hyphen
        wrap ("COUNTERCLOCK-" + "WISE (adv)") and parenthetical wraps
        ("chance" + "(by chance) (n)") join; a tag headword that sorts
        before the pending word also joins ("DOWNSTREAM" + "OF (prep)");
        otherwise the pending entry is pos-less (flagged) and the tag line
        starts a new entry ("such as" + "suck (v)")
      - no tag, current entry has no tag yet    -> headword wrap continuation
      - no tag, current entry complete          -> verb/adjective forms, or
        the start of the next entry's (pending) headword
    col2/3/4 lines always attach to the current (last created) entry, so a
    pending headword immediately opens a new row-band.
    """
    entries = []
    cur = None
    forms_open = False   # previous forms line ended with a comma
    stream = list(iter_cells())

    def next_c1_is_bare_tag(idx):
        # a lone uppercase token followed by a bare "(pos)" line is a wrapped
        # headword, not a verb form ("COMMUNICATION" + "(n)"); a bare tag
        # always completes the immediately preceding col1 token
        for _, n1, _, _, _ in stream[idx + 1:]:
            if n1:
                return bool(POS_ONLY_RE.match(n1))
        return False

    def note_open():
        # the forms lines include an unfinished "No other ..." note
        return (any(f.startswith("No other") for f in cur["forms"])
                and not cur["forms"][-1].endswith("."))

    for idx, (pi, c1, c2, c3, c4) in enumerate(stream):
        if c1:
            m = TAG_RE.match(c1)
            if m:
                head, pos, tail = m.group("head").strip(), m.group("pos"), \
                    m.group("tail").strip()
                if cur is not None and cur["pos"] == "":
                    pend = cur["head"]
                    if not head:
                        cur["pos"] = pos        # completes pending headword
                    elif pend.endswith("-") or head.startswith("(") or \
                            pend.count("(") > pend.count(")") or \
                            (pend[:1].isupper() and head[:1].isupper()):
                        # hyphen wrap ("COUNTERCLOCK-" + "WISE (adv)"),
                        # parenthetical wrap ("chance" + "(by chance) (n)"),
                        # uppercase multi-word wrap ("DOWNSTREAM" + "OF
                        # (prep)"); a lowercase head after a lowercase
                        # pending is a new entry ("such as" + "suck (v)")
                        if pend.endswith("-"):
                            cur["head"] = pend[:-1] + head
                        else:
                            cur["head"] = norm(pend + " " + head)
                        cur["pos"] = pos
                    else:
                        cur["flags"].append("no-pos")
                        cur = new_entry(pi)
                        cur["head"], cur["pos"] = head, pos
                        entries.append(cur)
                elif not head:
                    cur = new_entry(pi)         # stray tag, no headword seen
                    cur["pos"] = pos
                    cur["flags"].append("orphan-pos-tag")
                    entries.append(cur)
                else:
                    cur = new_entry(pi)
                    cur["head"], cur["pos"] = head, pos
                    entries.append(cur)
                if tail:
                    t = tail.lstrip(", ")
                    if t:
                        cur["forms"].append(t)
                    forms_open = tail.rstrip().endswith(",")
                else:
                    forms_open = False
            elif cur is not None and cur["pos"] == "":
                # headword wraps over another line
                if cur["head"].endswith("-"):
                    cur["head"] = cur["head"][:-1] + c1
                else:
                    cur["head"] = norm(cur["head"] + " " + c1)
            elif c1.endswith("-"):
                cur = new_entry(pi)             # hyphen-wrapped headword
                cur["head"] = c1
                entries.append(cur)
                forms_open = False
            elif cur is not None and is_forms_line(cur, c1, forms_open,
                                                   note_open(), idx,
                                                   next_c1_is_bare_tag):
                cur["forms"].append(c1)
                if not FORMS_NOTE_RE.match(c1):
                    forms_open = c1.rstrip().endswith(",")
            else:
                cur = new_entry(pi)             # pending headword
                cur["head"] = c1
                entries.append(cur)
                forms_open = False
        if cur is not None:
            if c2:
                cur["c2"].append(c2)
            if c3:
                cur["c3"].append(c3)
            if c4:
                cur["c4"].append(c4)
        elif c2 or c3 or c4:
            orphan = new_entry(pi)
            orphan["flags"].append("orphan-cells-no-entry")
            orphan["c2"] = [c2] if c2 else []
            orphan["c3"] = [c3] if c3 else []
            orphan["c4"] = [c4] if c4 else []
            entries.append(orphan)
            cur = orphan
    return entries


def is_forms_line(cur, c1, forms_open, note_open, idx, bare_tag_next):
    """Decide whether a no-tag col1 line continues the current entry's
    forms.  Only approved (UPPERCASE) entries carry forms.  A line that
    ends with a comma is always forms; otherwise a forms-shaped token is
    forms only if the NEXT col1 line is not a bare (pos) tag (a bare tag
    always pairs with the token right before it -- that token is then a
    wrapped headword, not a form)."""
    if not cur["head"].upper() == cur["head"]:
        return False
    if forms_open and c1.rstrip().endswith(","):
        return True
    if not forms_open and not cur["forms"] \
            and c1.strip(",") == cur["head"].split()[0]:
        return False  # identical to the headword and no forms sequence
        # started: it is the next entry's repeated headword
        # ("DOWNSTREAM (adv)" followed by "DOWNSTREAM OF (prep)")
    if FORMS_NOTE_RE.match(c1):
        return True
    if note_open and c1[:1].islower():
        return True
    if (forms_open or cur["pos"] in ("v", "adj", "adv")) \
            and FORMSY_RE.match(c1) and not bare_tag_next(idx):
        return True
    # forms of a multi-word verb keep its particle: "COME ON (v)" ->
    # "COMES ON," / "CAME ON" -- these carry no comma, so match the tail word
    if cur["pos"] == "v" and " " in cur["head"] \
            and ALTNP_RE.match(c1) and "(" not in c1 \
            and c1.split()[-1].rstrip(",") == cur["head"].split()[-1] \
            and not bare_tag_next(idx):
        return True
    return False


# ------------------------------------------------------- col2 item assembly

NOTE_OPEN_TAIL_RE = re.compile(r"(,|\buse:?|\bmean)$")
NOTE_OPEN_BODY_RE = re.compile(r"\buse:?\b|\bmean\b")


def note_open_item(it):
    """True while an item is a usage note that still lists alternative words:
    'For safety instructions, use:' / 'Do not use this word to mean BECOME,
    GO,' -- open until the sentence ends with a period.  The 'For other
    meanings, use:' marker is NOT a note: its alternatives are items."""
    if MARKER_RE.match(it):
        return False
    if NOTE_OPEN_TAIL_RE.search(it):
        return True
    return bool(NOTE_OPEN_BODY_RE.search(it)) and not it.endswith(".")


def col2_items(lines, entry):
    """Join wrapped col2 lines into items; classify each item.

    Returns (items, runs) where items = [(kind, text)] and runs = list of
    [start, end) index spans of consecutive no-pos uppercase items that were
    NOT terminated by a glued (pos) tag -- ambiguous: either one alternative
    wrapped over several lines, or several one-line alternatives.
    """
    raw = []
    glued = set()   # indices that received a (pos)-only glue line
    for s in lines:
        if POS_ONLY_RE.match(s):
            if raw:
                raw[-1] += " " + s
                glued.add(len(raw) - 1)
            else:
                entry["flags"].append("col2-tag-glue-without-prev")
                raw.append(s)
        elif raw and (s[:1].islower() or s[:1] in "“\""):
            raw[-1] += " " + s
        elif raw and note_open_item(raw[-1]):
            raw[-1] += " " + s
        else:
            raw.append(s)
    # absorb a no-pos uppercase run into a following glued alternative:
    # "REMOVE" + "CONTAMINATION (TN)" is one wrapped alternative
    i = 0
    while i < len(raw):
        if i in glued:
            j = i - 1
            while j >= 0 and j not in glued and ALTNP_RE.match(raw[j]) \
                    and "(" not in raw[j]:
                j -= 1
            if j < i - 1:
                raw[j + 1:i + 1] = [" ".join(raw[j + 1:i + 1])]
                glued = {g if g <= j else g - (i - j - 1)
                         for g in glued if g <= j or g > i}
                i = j + 1
                continue
        i += 1
    items = []
    for it in raw:
        mm = MARKER_RE.match(it)
        if mm:
            items.append(("MARKER", "For other meanings, use:"))
            rest = mm.group("rest").strip()
            if rest:
                items.append((classify(rest), rest))
            continue
        items.append((classify(it), it))
    runs = []
    k = 0
    while k < len(items):
        if items[k][0] == "ALTNP":
            j = k
            while j < len(items) and items[j][0] == "ALTNP":
                j += 1
            if j - k >= 2:
                runs.append((k, j))
            k = j
        else:
            k += 1
    return items, runs


def classify(it):
    if ALT_RE.match(it):
        return "ALT"
    if ALTNP_RE.match(it) and len(it) <= 40:
        return "ALTNP"
    return "TEXT"


def sent_count(text):
    return len(re.findall(r"\.(?:\s|$)", text))


# ---------------------------------------------------------------- row build

def esc(s):
    return s.replace("|", "\\|")


NOTE_START_RE = re.compile(r"^(Do not use |For .*\buse\b|Refer to )")


def build_rows(entries):
    rows, review = [], []
    pos_hist = Counter()
    for e in entries:
        word = e["head"]
        pos = e["pos"]
        pos_hist[pos] += 1
        forms = norm(" ".join(e["forms"])).strip(" ,")
        items, runs = col2_items(e["c2"], e)
        ste = join_lines(e["c3"])
        nonste = join_lines(e["c4"])
        approved = bool(word) and word.upper() == word
        wcell = f"{word} ({pos})" if pos else (word or "???")

        meanings = [t for k, t in items if k == "TEXT"]
        alts = [t for k, t in items if k in ("ALT", "ALTNP")]
        marker_seen = any(k == "MARKER" for k, _ in items)

        if approved:
            other = []
            if marker_seen:
                seen = False
                for k, t in items:
                    if k == "MARKER":
                        seen = True
                    elif seen and k in ("ALT", "ALTNP"):
                        other.append(t)
                    elif seen and k == "TEXT":
                        e["flags"].append("text-after-marker")
            elif alts:
                e["flags"].append("approved-alts-without-marker")
            notes = [t for t in meanings if NOTE_START_RE.match(t)]
            meanings = [t for t in meanings if not NOTE_START_RE.match(t)]
            if not meanings:
                e["flags"].append("approved-no-meaning")
            mcell = esc(" ".join(meanings))
            if other:
                notes.insert(0, "For other meanings, use: " +
                             "; ".join(other))
            if forms:
                notes.append("forms: " + forms)
            ncell = esc("; ".join(notes))
        else:
            if not word:
                e["flags"].append("no-headword")
            if not pos:
                e["flags"].append("no-pos")
            if marker_seen:
                e["flags"].append("marker-in-banned")
            if not alts and not meanings:
                e["flags"].append("banned-no-alts")
            # disambiguate uppercase runs: several one-line alternatives or
            # one wrapped alternative?  The STE examples pair 1:1 with the
            # alternatives, so the sentence count decides; if it cannot,
            # the entry goes to manual review.
            if runs and not e["flags"]:
                n_sent = sent_count(ste)
                if n_sent == len(alts):
                    pass                        # separate one-line alts
                else:
                    # merge each run at points where the joined phrase
                    # appears verbatim in the STE examples ("OPERATE" +
                    # "INCORRECTLY" -> "... TO OPERATE INCORRECTLY.")
                    ok = True
                    for a, b in reversed(runs):
                        words = [t for _, t in items[a:b]]
                        groups = []
                        gi = 0
                        while gi < len(words):
                            hit = None
                            for gj in range(len(words), gi, -1):
                                if " ".join(words[gi:gj]) in ste:
                                    hit = gj
                                    break
                            if hit is None:
                                ok = False
                                break
                            groups.append(" ".join(words[gi:hit]))
                            gi = hit
                        if not ok:
                            break
                        items[a:b] = [(classify(g), g) for g in groups]
                    new_alts = [t for k, t in items if k in ("ALT", "ALTNP")]
                    if ok and len(new_alts) == n_sent:
                        alts = new_alts
                    else:
                        e["flags"].append("altnp-run-ambiguous")
                        print(f"  AMBIG {word!r}: n_sent={n_sent} "
                              f"separate={len(alts)} grouped={ok and len(new_alts)} "
                              f"ste={ste[:100]!r}")
            mcell = "NOT APPROVED"
            parts = []
            if alts:
                parts.append("use: " + "; ".join(alts))
            if meanings:
                parts.append(" ".join(meanings))  # usage note(s)
            if len(alts) <= 1 and ste and nonste:
                parts.append(f'"{esc(nonste)}" \u2192 "{esc(ste)}"')
            if forms:
                parts.append("forms: " + forms)
            ncell = esc(" \u2014 ".join(parts))

        row = {"word": word, "pos": pos, "approved": approved,
               "wcell": wcell, "mcell": mcell, "ncell": ncell,
               "flags": list(dict.fromkeys(e["flags"])), "page": e["page"],
               "raw": e}
        (review if e["flags"] else rows).append(row)
    return rows, review, pos_hist


# ------------------------------------------------------------------- output

HEADER = """\
# STE-100 dictionary — grep-target lookup table

Derived from the **ASD-STE100 Issue 9** dictionary (Part 2), pages 2-1-A1 to
2-1-Y2. The PDF `ASD-STE100_ISSUE9.pdf` in this folder is the standard of
record; this file is a lookup aid generated from it. ASD-STE100 is a licensed
standard — this repository is private; do not redistribute this file or the PDF.

## How agents use this file

- **Never read this whole file.** Grep for one word at a time, e.g.
  `grep -i "^| accuracy " .agents/skills/language-persona/references/ste-100-dictionary.md`
  or `grep "^| AID (n) " ...`. Try both cases if unsure.
- **UPPERCASE word = APPROVED** in STE. Use it only as the listed part of
  speech; the middle column is its approved meaning (numbered when the word
  has several approved meanings).
- **lowercase word = NOT APPROVED.** The right column gives the approved
  alternative(s) to use instead, plus a "non-STE → STE" example pair when the
  entry has a single replacement.
- `(TN)` = technical noun, `(TV)` = technical verb: not listed as entries,
  but they appear as alternatives. A project's CONTEXT.md technical nouns and
  verbs are always permitted additions per STE rules 1.5 and 1.6.
- Restricted verb/adjective forms (conjugations, comparatives) are in the
  right column as `forms: ...` — use only those forms.
- Entries the parser could not classify confidently are under
  `## Needs manual review` at the bottom — verify them against the PDF.

| Word (pos) | Status / approved meaning | Use instead / notes |
|---|---|---|
"""


def write_markdown(rows, review):
    lines = [HEADER]
    for r in rows:
        lines.append(f"| {r['wcell']} | {r['mcell']} | {r['ncell']} |\n")
    lines.append("\n## Needs manual review\n\n")
    lines.append("Entries below could not be classified confidently by the "
                 "parser. Raw cell text is verbatim from the source; check "
                 "against the PDF (PDF page = 149 + page index).\n\n")
    for r in review:
        e = r["raw"]
        lines.append(f"### {r['wcell']} — flags: {', '.join(r['flags'])} "
                     f"(page index {r['page']})\n\n")
        head = " ".join([e["head"], e["pos"] and f"({e['pos']})" or "",
                         *e["forms"]])
        for label, vals in (("col1", [norm(head)]),
                            ("col2", e["c2"]), ("STE ex", e["c3"]),
                            ("non-STE ex", e["c4"])):
            vals = [v for v in vals if v]
            if vals:
                lines.append(f"- {label}: " + " / ".join(vals) + "\n")
        lines.append("\n")
    OUT.write_text("".join(lines), encoding="utf-8")


def main():
    ensure_table_txt()
    entries = assemble_entries()
    rows, review, pos_hist = build_rows(entries)
    appr = sum(1 for r in rows if r["approved"])
    banned = sum(1 for r in rows if not r["approved"])
    print(f"entries total: {len(entries)}")
    print(f"  approved rows: {appr}")
    print(f"  non-approved rows: {banned}")
    print(f"  needs review: {len(review)}")
    print("pos histogram:", dict(pos_hist))
    fc = Counter(f for r in review for f in r["flags"])
    print("flag counts:", dict(fc))
    # alphabetical order sanity (word-by-word: space sorts before letters)
    prev, breaks = "", 0
    for r in rows:
        key = re.sub(r"[^a-z0-9 ]", "", r["word"].lower()).replace(" ", "\x01")
        if key < prev:
            breaks += 1
            if breaks <= 10:
                print("  ORDER BREAK:", prev.replace("\x01", " "), "->",
                      r["word"])
        prev = max(prev, key)
    print(f"order breaks: {breaks}")
    # duplicate word+pos check
    dup = Counter((r["word"], r["pos"]) for r in rows)
    dups = {k: v for k, v in dup.items() if v > 1}
    print(f"duplicate word+pos: {len(dups)}")
    for k in list(dups)[:10]:
        print("  DUP:", k)
    for r in review:
        e = r["raw"]
        print(f"  REVIEW {r['wcell']!r} flags={r['flags']} c2={e['c2'][:6]}")
    write_markdown(rows, review)
    print(f"wrote {OUT}")


if __name__ == "__main__":
    main()
