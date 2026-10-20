#!/usr/bin/env python3
"""Prepare course materials in sources/ for writer agents (orchestrator tool, AUTHORING.md §4).

Reading slides as page images is what makes writing expensive, so the orchestrator runs this once
per course and agents read text first:

  sources/text/<file>.txt     extracted text, one "=== p. N [flags] ===" header per page
  sources/pages/<file>/p-NNN.png
                              low-resolution images of only the pages whose text is not enough:
                              raster figures, formulas that extract badly, pages with little text
  sources/text/INDEX.md       per file: pages, flagged pages and why, scanned files

PPTX/DOCX are converted with markitdown (via uv); their embedded pictures go to
sources/pages/<file>/media/. Scanned PDFs (no text layer) are only listed, not rendered:
the orchestrator decides how to split them (or passes --scanned to render every page).

Usage: python3 scripts/prep_sources.py [--dpi 80] [--scanned] [files or dirs ...]
       (default: everything under sources/slides, sources/notes, sources/textbooks)
"""
import argparse
import re
import shutil
import subprocess
import sys
import zipfile
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SOURCES = ROOT / "sources"
TEXT_DIR = SOURCES / "text"
PAGES_DIR = SOURCES / "pages"

GARBLE = re.compile("[�-]")
MATH_ALNUM = re.compile("[\U0001d400-\U0001d7ff]")
MATH_SYMBOL = re.compile(r"[∑∏∫√∞≤≥≠≈∈∉⊂⊆∪∩∀∃∂∇→⇒⇔±×÷^_]")


def run(cmd: list[str]) -> str:
    return subprocess.run(cmd, check=True, capture_output=True, text=True, errors="replace").stdout


def stem_of(path: Path) -> str:
    """A flat, readable name for a source file: its path below sources/, without the extension."""
    rel = path.resolve().relative_to(SOURCES) if path.resolve().is_relative_to(SOURCES) else Path(path.name)
    return re.sub(r"[\\/\s]+", "_", str(rel.with_suffix("")))


def raster_images(pdf: Path, pages: int) -> Counter:
    """Pages with a sizeable raster image, ignoring logos and backgrounds repeated on most pages."""
    rows = []
    for line in run(["pdfimages", "-list", str(pdf)]).splitlines()[2:]:
        f = line.split()
        if len(f) > 4 and f[0].isdigit() and f[2] in ("image", "stencil"):
            rows.append((int(f[0]), int(f[3]), int(f[4])))
    by_size = Counter((w, h) for _, w, h in rows)
    counts: Counter = Counter()
    for page, w, h in rows:
        if w * h >= 150 * 150 and by_size[(w, h)] <= max(3, pages // 2):
            counts[page] += 1
    return counts


def page_flags(text: str, images: int) -> list[str]:
    flags = []
    body = re.sub(r"\s+", "", text)
    lines = [l.strip() for l in text.splitlines() if l.strip()]
    short = sum(1 for l in lines if len(l) <= 3)
    if images:
        flags.append("figure")
    if GARBLE.search(text) or MATH_ALNUM.search(text) or (len(lines) >= 6 and short / len(lines) > 0.3) or len(MATH_SYMBOL.findall(text)) >= 8:
        flags.append("formula")
    if len(body) < 40 and not images:
        flags.append("little-text")
    return flags


def prep_pdf(pdf: Path, dpi: int, scanned_ok: bool) -> dict:
    pages = int(re.search(r"^Pages:\s+(\d+)", run(["pdfinfo", str(pdf)]), re.M).group(1))
    texts = run(["pdftotext", "-layout", str(pdf), "-"]).split("\f")[:pages]
    texts += [""] * (pages - len(texts))
    images = raster_images(pdf, pages)
    name = stem_of(pdf)
    scanned = sum(1 for t in texts if len(re.sub(r"\s+", "", t)) < 40) > 0.8 * pages
    flagged: dict[int, list[str]] = {}
    out = []
    for i, t in enumerate(texts, start=1):
        flags = ["scanned"] if scanned else page_flags(t, images[i])
        if flags:
            flagged[i] = flags
        out.append(f"=== p. {i}{' [' + ', '.join(flags) + ']' if flags else ''} ===\n{t.rstrip()}\n")
    (TEXT_DIR / f"{name}.txt").write_text("\n".join(out), encoding="utf-8")
    render = [] if scanned and not scanned_ok else sorted(flagged)
    if render:
        dest = PAGES_DIR / name
        dest.mkdir(parents=True, exist_ok=True)
        for p in render:
            subprocess.run(["pdftoppm", "-r", str(dpi), "-png", "-f", str(p), "-l", str(p), "-singlefile", str(pdf), str(dest / f"p-{p:03d}")], check=True)
    return {"file": pdf, "name": name, "pages": pages, "flagged": flagged, "rendered": len(render), "scanned": scanned}


def prep_office(doc: Path) -> dict:
    name = stem_of(doc)
    try:
        text = run(["uv", "run", "--quiet", "--with", "markitdown[pptx,docx]", "markitdown", str(doc)])
    except (subprocess.CalledProcessError, FileNotFoundError) as e:
        text = f"(markitdown failed: {e})"
    (TEXT_DIR / f"{name}.txt").write_text(text, encoding="utf-8")
    media = 0
    if doc.suffix.lower() in (".pptx", ".docx"):
        dest = PAGES_DIR / name / "media"
        with zipfile.ZipFile(doc) as z:
            for info in z.infolist():
                if "/media/" in info.filename and info.file_size >= 5_000 and re.search(r"\.(png|jpe?g|gif|bmp|emf|wmf)$", info.filename, re.I):
                    dest.mkdir(parents=True, exist_ok=True)
                    (dest / Path(info.filename).name).write_bytes(z.read(info))
                    media += 1
    return {"file": doc, "name": name, "pages": None, "flagged": {}, "rendered": media, "scanned": False}


def ranges(nums: list[int]) -> str:
    out, start, prev = [], None, None
    for n in nums + [None]:
        if start is None:
            start = prev = n
        elif n == prev + 1:
            prev = n
        else:
            out.append(f"{start}" if start == prev else f"{start}–{prev}")
            start = prev = n
    return ", ".join(out)


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("paths", nargs="*", type=Path)
    ap.add_argument("--dpi", type=int, default=80, help="resolution of page images (default 80; raise for small print)")
    ap.add_argument("--scanned", action="store_true", help="also render every page of scanned PDFs")
    args = ap.parse_args()
    roots = args.paths or [SOURCES / d for d in ("slides", "notes", "textbooks")]
    files = sorted(f for r in roots for f in ([r] if r.is_file() else r.rglob("*")) if f.is_file())
    if TEXT_DIR.exists():
        shutil.rmtree(TEXT_DIR)
    if PAGES_DIR.exists():
        shutil.rmtree(PAGES_DIR)
    TEXT_DIR.mkdir(parents=True)
    results = []
    for f in files:
        ext = f.suffix.lower()
        if ext == ".pdf":
            results.append(prep_pdf(f, args.dpi, args.scanned))
        elif ext in (".pptx", ".ppt", ".docx", ".doc"):
            results.append(prep_office(f))
        elif ext in (".md", ".txt", ".tex", ".r", ".py"):
            continue  # already text: agents read it directly
        else:
            print(f"skipped {f}", file=sys.stderr)
            continue
        r = results[-1]
        print(f"{r['name']}: {r['pages'] or '-'} pages, {r['rendered']} image(s){' (scanned)' if r['scanned'] else ''}")

    lines = [
        "# Prepared sources",
        "",
        f"Text: `sources/text/<name>.txt` (page headers `=== p. N [flags] ===`). Page images ({args.dpi} dpi): "
        "`sources/pages/<name>/p-NNN.png`, only for flagged pages. Read the text first; open an image only when the "
        "text of that page is not enough (a figure you must redraw, a garbled formula or table). Flags are heuristics: "
        "vector-drawn figures are not detected, so look at a page when its text refers to a figure you cannot see.",
        "",
        "| File | Pages | figure | formula | little-text | Images |",
        "|---|---|---|---|---|---|",
    ]
    for r in results:
        by = {k: ranges([p for p, fl in r["flagged"].items() if k in fl]) for k in ("figure", "formula", "little-text")}
        if r["scanned"]:
            note = f"SCANNED: {r['rendered']} rendered" if r["rendered"] else "SCANNED (no text layer): not rendered"
            lines.append(f"| {r['name']} | {r['pages']} | {note} | | | |")
        else:
            lines.append(f"| {r['name']} | {r['pages'] or '(office)'} | {by['figure']} | {by['formula']} | {by['little-text']} | {r['rendered']} |")
    (TEXT_DIR / "INDEX.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"wrote {TEXT_DIR.relative_to(ROOT)}/INDEX.md")


if __name__ == "__main__":
    main()
