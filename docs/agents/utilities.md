# utilities.md — work utilities registry

Local tools for heavy file work. Install a utility **only when the project type needs it** —
no speculative installs. Python tools require Python 3.10+; verify with `python --version`.

> Pricing and package status rot fast — **re-check every entry before relying on it.**

## Registry

| Name | Role | Current pick | Alternatives | Cost | Last evaluated | Swap when |
|---|---|---|---|---|---|---|
| PDF → Markdown | High-fidelity conversion | Docling (MIT) | MarkItDown (lightweight), Mathpix (paid STEM) | Free | 2026-08-07 | MarkItDown for breadth over fidelity; Mathpix when equations/tables break free tools |
| Audio transcription | wav/mp3 → text | Docling ASR | faster-whisper (local batch) | Free | 2026-08-07 | faster-whisper for offline bulk jobs |
| Plain-text extraction | Fast text-only pull from PDF | poppler `pdftotext` | Python libs | Free | 2026-08-07 | Docling when layout/tables matter |
| Archives | Pack/unpack | 7-Zip | built-in zip | Free | 2026-08-07 | Never |

## Install & use

### PDF → Markdown — Docling (current pick)

Requires Python 3.10+. Verified on this machine 2026-08-07 (`pip install docling`).

```powershell
pip install docling
docling file.pdf        # writes file.md next to the source
```

Handles layout, tables, OCR, and ASR; works on Windows. Also ships an MCP server (see
[services.md](services.md)) — adopt it only if agents need repeated conversions.

### Lightweight alternative — MarkItDown (Microsoft)

```powershell
pip install 'markitdown[all]'
markitdown file.pdf -o out.md
```

Broad format coverage — docx, xlsx, pptx, YouTube transcripts — at lower fidelity than
Docling.

### Paid STEM alternative — Mathpix

Best equations and tables. Costs money — the human gate applies before subscribing.

### Audio transcription

- Docling ASR for single wav/mp3 files.
- `faster-whisper` for local batch transcription.

### Fast plain text

poppler `pdftotext` when only the words matter, not the layout.

### Archives

7-Zip for everything pack/unpack.

## Adding a utility

1. Pick from this registry first.
2. New or swapped tool: log a proposal in [`docs/decisions.md`](../decisions.md) before
   installing.
3. Install into an isolated environment (venv) when the tool pulls heavy dependencies.
4. Update the registry row: pick, cost, last-evaluated date, swap criteria.
