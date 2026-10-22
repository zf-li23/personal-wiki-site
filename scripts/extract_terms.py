"""Orchestrator helper: pull the YAML glossary proposals out of a writer agent's transcript.

Usage: python3 scripts/extract_terms.py <agent .output jsonl> <out.yaml>
Takes the last report that has a "词条提议" or "Glossary proposals" section and writes its `- { ... }` lines;
feed the result to scripts/merge_terms.py.
"""
import json
import re
import sys


def reports(path):
    for line in open(path, encoding="utf-8"):
        try:
            obj = json.loads(line)
        except ValueError:
            continue
        stack = [obj]
        while stack:
            x = stack.pop()
            if isinstance(x, dict):
                stack.extend(x.values())
            elif isinstance(x, list):
                stack.extend(x)
            elif isinstance(x, str) and ("词条提议" in x or "Glossary proposals" in x) and "```yaml" in x:
                yield x


def main():
    found = list(reports(sys.argv[1]))
    if not found:
        sys.exit("no glossary proposals found")
    text = found[-1]
    start = max(text.find("词条提议"), text.find("Glossary proposals"))
    blocks = re.findall(r"```yaml\n(.*?)```", text[start:], re.S)
    lines = [l.strip() for b in blocks for l in b.splitlines() if l.strip().startswith("- {")]
    with open(sys.argv[2], "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")
    print(len(lines), "proposals")


if __name__ == "__main__":
    main()
