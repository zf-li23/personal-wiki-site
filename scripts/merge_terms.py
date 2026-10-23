#!/usr/bin/env python3
"""Merge writer agents' glossary proposals into content/glossary.yaml (orchestrator tool, AUTHORING.md §10).

  python3 scripts/merge_terms.py proposals.yaml "<exact section comment>"          # dry run
  python3 scripts/merge_terms.py proposals.yaml "<exact section comment>" --apply  # write

proposals.yaml is a flat YAML list of { zh, en, aliases?, scope?, defined_on? }. New entries are
appended at the end of the section. Existing entries are never changed: a proposal that shares a
Chinese name, alias or English name with an entry is reported as a CONFLICT and not added. Decide
each by hand: the same concept (add an alias, or nothing), or a homonym (give both a `scope`).
"""
import re
import sys
from pathlib import Path

import yaml

GLOSSARY = Path(__file__).resolve().parent.parent / "content" / "glossary.yaml"
ENTRY = re.compile(r"^  - (\{.*\})\s*(#.*)?$")


def quote(s) -> str:
    s = str(s)
    return f'"{s}"' if re.search(r"[:'#,\[\]{}*]", s) or s.lower() in ("null", "yes", "no", "true", "false", "on", "off") else s


def fmt(e: dict) -> str:
    parts = [f"zh: {quote(e['zh'])}", f"en: {quote(e['en'])}"]
    if e.get("aliases"):
        parts.append("aliases: [" + ", ".join(quote(a) for a in e["aliases"]) + "]")
    if e.get("scope"):
        parts.append("scope: [" + ", ".join(f'"{s}"' for s in e["scope"]) + "]")
    return "  - { " + ", ".join(parts) + " }"


def names(e: dict) -> set[str]:
    aliases = [str(a) for a in e.get("aliases") or []]
    return {e["zh"], *aliases, str(e["en"]).lower(), *(a.lower() for a in aliases)}


def main() -> None:
    args = [a for a in sys.argv[1:] if a != "--apply"]
    if len(args) != 2:
        sys.exit(__doc__)
    proposals, section = yaml.safe_load(Path(args[0]).read_text(encoding="utf-8")) or [], args[1]
    for p in proposals:  # YAML turns bare NULL / yes / 1.0 into non-strings
        p["aliases"] = [str(a) if a is not None else "NULL" for a in p.get("aliases", [])]
    lines = GLOSSARY.read_text(encoding="utf-8").split("\n")
    existing = [(i, yaml.safe_load(m.group(1))) for i, l in enumerate(lines) if (m := ENTRY.match(l))]
    added, conflicts, seen = [], 0, set()
    for p in proposals:
        hits = [e for _, e in existing if names(e) & names(p)]
        if any(e["zh"] == p["zh"] and e["en"].lower() == p["en"].lower() and e.get("scope") == p.get("scope") for e in hits):
            print(f"present   {p['zh']} | {p['en']}")
            continue
        if hits or names(p) & seen:
            conflicts += 1
            print(f"CONFLICT  proposed {fmt(p).strip()}  (defined_on {p.get('defined_on', '?')})")
            for e in hits:
                print(f"          existing {fmt(e).strip()}")
            if not hits:
                print("          (clashes with another proposal in this file)")
            continue
        seen |= names(p)
        added.append(fmt(p))
        print(f"add       {fmt(p).strip()}")
    try:
        h = next(i for i, l in enumerate(lines) if l.strip() == section)
    except StopIteration:
        sys.exit(f'section comment not found: "{section}"')
    end = next((i for i in range(h + 1, len(lines)) if lines[i].startswith("  #")), len(lines))
    while not lines[end - 1].strip():
        end -= 1
    print(f"{len(added)} to add, {conflicts} conflict(s) to decide by hand")
    if "--apply" in sys.argv:
        lines[end:end] = added
        GLOSSARY.write_text("\n".join(lines), encoding="utf-8")
        print(f"wrote {GLOSSARY.name}")
    else:
        print("dry run: pass --apply to write")


if __name__ == "__main__":
    main()
