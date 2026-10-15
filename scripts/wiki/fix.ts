/**
 * `pnpm wiki fix`: rewrite numbering *formats* into the canonical form (never renumbers):
 *   "## 13.1 Title" / "## 13.1.Title" / "## **13.1 Title**"  →  "## 13.1. Title"
 *   "**定理1.**" / "**定义 8 (充分统计量).**" / "**推论1**（名称）"  →  "**定理 1**" / "**定义 8（充分统计量）**" / "**推论 1（名称）**"
 *   formula notation (notation.ts rules with a fix): \vec{x} → \boldsymbol{x}, A^T → A^{\mathsf T}, …
 * Code blocks are left alone. Useful right after pasting Markdown converted from slides.
 */
import { fixNotationInMarkdown } from './notation.ts';
import { formatHeading, formatStatementLabel, parseHeadingNumber, parseStatementLabel } from './numbering.ts';

const FENCE = /^\s*(`{3,}|~{3,})/;
// optional list / quote marker, then a bold run, then an optional name in parentheses right after it
const LABEL_LINE = /^(\s*(?:[-*+]\s+|\d+\.\s+|>\s*)*)\*\*([^*]+?)\*\*(\s*[（(]([^）)]{1,40})[）)])?/;

export interface FixResult {
  text: string;
  changes: number;
}

export function fixMarkdown(body: string, lang: 'zh' | 'en', pageId = ''): FixResult {
  const notation = fixNotationInMarkdown(body, pageId);
  body = notation.text;
  let changes = notation.changes;
  let inFence = false;
  const lines = body.split('\n').map((line) => {
    if (FENCE.test(line)) {
      inFence = !inFence;
      return line;
    }
    if (inFence) return line;

    const heading = /^(#{2,6})\s+(.*?)\s*$/.exec(line);
    if (heading) {
      const raw = heading[2].replace(/^\*\*(.*)\*\*$/, '$1').trim();
      const parsed = parseHeadingNumber(raw);
      const title = parsed.title.replace(/^\*\*(.*)\*\*$/, '$1').trim();
      const next = `${heading[1]} ${parsed.number ? formatHeading(parsed.number, title) : title}`;
      if (next !== line) changes++;
      return next;
    }

    const m = LABEL_LINE.exec(line);
    if (!m) return line;
    const label = parseStatementLabel(m[2]);
    if (!label) return line;
    const name = label.name ?? m[4]?.trim();
    const canonical = `**${formatStatementLabel({ kind: label.kind, number: label.number, name }, lang)}**`;
    const replaced = m[1] + canonical + (label.name || !m[3] ? (m[3] ?? '') : '');
    if (replaced === m[0]) return line;
    changes++;
    return replaced + line.slice(m[0].length);
  });
  return { text: lines.join('\n'), changes };
}
