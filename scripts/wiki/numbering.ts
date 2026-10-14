/**
 * Numbering rules shared by the checker (markdown.ts), the fixer (`pnpm wiki fix`) and tests.
 *
 * Page roles: depth 1 = discipline, depth 2 = course, depth 3 = chapter (a "page").
 * Inside a chapter page every number starts with the chapter's own number, i.e. the page id
 * without its first two segments: page 3.1.13 → prefix "13".
 *
 *   headings     ## 13.1. Title   ### 13.1.2. Title      (number, trailing dot, one space)
 *   statements   **定理 13.2.1（名称）**  /  **Theorem 13.2.1 (Name)**
 *   formulas     $$ … \tag{13.2} $$, referenced as 式 (13.2) / Eq. (13.2)
 *
 * Numbers are scoped to a course: "定理 13.2.1" in course 3.1 always means page 3.1.13.
 */

export type PageRole = 'discipline' | 'course' | 'chapter';

export function pageRole(id: string): PageRole | null {
  const depth = id.split('.').length;
  return depth === 1 ? 'discipline' : depth === 2 ? 'course' : depth === 3 ? 'chapter' : null;
}

/** "3.1.13" → ["13"]; the course part ("3.1") is implied. */
export function numberPrefix(id: string): string[] {
  return id.split('.').slice(2);
}

export function courseOf(id: string): string {
  return id.split('.').slice(0, 2).join('.');
}

/* ----------------------------------------------------------------- headings */

export interface HeadingNumber {
  /** Number segments, e.g. ["13", "1", "2"]; absent for unnumbered headings. */
  number?: string[];
  title: string;
  /** False when a number is present but not written as "13.1. Title". */
  wellFormed: boolean;
}

const CANONICAL_HEADING = /^(\d+(?:\.\d+)*)\. (\S.*)$/;
// A number followed by "." or whitespace, then a title ("2025年" is a title, not a number).
const LOOSE_HEADING = /^\**\s*(\d+(?:\.\d+)*)(?:\.\s*|\s+)(\S.*?)\**$/;

export function parseHeadingNumber(text: string): HeadingNumber {
  const t = text.trim();
  const m = CANONICAL_HEADING.exec(t);
  if (m) return { number: m[1].split('.'), title: m[2], wellFormed: true };
  const loose = LOOSE_HEADING.exec(t);
  if (loose) return { number: loose[1].split('.'), title: loose[2].replace(/^\*\*(.*)\*\*$/, '$1').trim(), wellFormed: false };
  return { title: t, wellFormed: true };
}

export function formatHeading(number: string[], title: string): string {
  return `${number.join('.')}. ${title}`;
}

export interface HeadingInput {
  depth: number;
  text: string;
  line?: number;
}

export interface NumberingProblem {
  line?: number;
  message: string;
}

/**
 * Structural rules for the headings of a chapter page:
 *  - no skipped levels (#### directly under ##)
 *  - a numbered heading at depth d has prefix + (d - 1) segments, starts with its parent's number
 *    and continues its siblings' sequence (13.1, 13.2, …)
 *  - unnumbered headings are allowed at ## (summary, exercises, …) and under unnumbered parents only
 */
export function checkHeadings(headings: HeadingInput[], prefix: string[]): NumberingProblem[] {
  const problems: NumberingProblem[] = [];
  // stack[d] = number of the most recent heading at depth d (null = unnumbered)
  const stack: (string[] | null)[] = [];
  const lastChild = new Map<string, number>();
  let prevDepth = 1;
  for (const h of headings) {
    const { depth, line } = h;
    if (depth > prevDepth + 1) problems.push({ line, message: `heading level skipped: ${'#'.repeat(depth)} directly after ${'#'.repeat(prevDepth)}` });
    prevDepth = depth;
    const parsed = parseHeadingNumber(h.text);
    stack.length = depth;
    const parent = depth === 2 ? prefix : stack[depth - 1];
    if (!parsed.number) {
      if (depth > 2 && parent) problems.push({ line, message: `heading "${h.text}" is inside numbered section ${parent.join('.')}. and must be numbered too` });
      stack[depth] = null;
      continue;
    }
    if (!parsed.wellFormed) problems.push({ line, message: `write heading numbers as "${formatHeading(parsed.number, parsed.title)}" (number, dot, space; \`pnpm wiki fix\` does this)` });
    const num = parsed.number;
    const expectedLen = prefix.length + depth - 1;
    if (parent === undefined) {
      // parent level was skipped; already reported above
    } else if (parent === null) {
      problems.push({ line, message: `numbered heading ${num.join('.')}. is inside an unnumbered section` });
    } else if (num.length !== expectedLen || num.slice(0, parent.length).join('.') !== parent.join('.')) {
      const example = [...parent, 'n'].join('.');
      problems.push({ line, message: `heading number ${num.join('.')}. does not fit here: a ${'#'.repeat(depth)} heading in this section is numbered ${example}.` });
    } else {
      const key = parent.join('.');
      const expected = (lastChild.get(key) ?? 0) + 1;
      const actual = Number(num.at(-1));
      if (actual !== expected) problems.push({ line, message: `heading number ${num.join('.')}. breaks the sequence: expected ${[...parent, expected].join('.')}.` });
      lastChild.set(key, actual);
    }
    stack[depth] = num;
  }
  return problems;
}

/* --------------------------------------------------------------- statements */

/** Numbered statement kinds; the key is the language-neutral anchor prefix (thm-13.2.1). */
export const STATEMENT_KINDS = {
  def: { zh: '定义', en: 'Definition' },
  thm: { zh: '定理', en: 'Theorem' },
  lem: { zh: '引理', en: 'Lemma' },
  prop: { zh: '命题', en: 'Proposition' },
  cor: { zh: '推论', en: 'Corollary' },
  pty: { zh: '性质', en: 'Property' },
  ex: { zh: '例', en: 'Example' },
  rem: { zh: '注', en: 'Remark' },
  alg: { zh: '算法', en: 'Algorithm' },
  fml: { zh: '公式', en: 'Formula' },
} as const;

export type StatementKind = keyof typeof STATEMENT_KINDS;

const WORD_TO_KIND = new Map<string, StatementKind>();
for (const [kind, words] of Object.entries(STATEMENT_KINDS) as [StatementKind, { zh: string; en: string }][]) {
  WORD_TO_KIND.set(words.zh, kind);
  WORD_TO_KIND.set(words.en.toLowerCase(), kind);
}
const KIND_WORDS = [...WORD_TO_KIND.keys()].sort((a, b) => b.length - a.length).map(escapeRe).join('|');

export interface StatementLabel {
  kind: StatementKind;
  word: string;
  number?: string[];
  name?: string;
  /** Written exactly as **定理 13.2.1（名称）** / **Theorem 13.2.1 (Name)**. */
  canonical: boolean;
}

// word, optional number (optionally followed by "."), optional name in （）/() or as trailing text, optional final "." / "：".
const LABEL_RE = new RegExp(`^(${KIND_WORDS})(?![\\p{Script=Han}A-Za-z])\\s*(\\d+(?:\\.\\d+)*)?\\.?\\s*(?:[（(]\\s*(.+?)\\s*[）)]|(.*?))\\s*[.:：]?$`, 'iu');

/** Parse the text of a bold run at the start of a paragraph; null when it is not a statement label. */
export function parseStatementLabel(text: string): StatementLabel | null {
  const t = text.trim();
  const m = LABEL_RE.exec(t);
  if (!m) return null;
  const word = m[1];
  const kind = WORD_TO_KIND.get(word.toLowerCase()) ?? WORD_TO_KIND.get(word);
  if (!kind) return null;
  const number = m[2]?.split('.');
  const name = (m[3] ?? m[4] ?? '').trim() || undefined;
  if (!number && name && !m[3]) return null; // "**定理证明**"-like bold text, not a label
  const zhWord = /\p{Script=Han}/u.test(word);
  return { kind, word, number, name, canonical: t === formatStatementLabel({ kind, word, number, name }, zhWord ? 'zh' : 'en') };
}

export function formatStatementLabel(label: Pick<StatementLabel, 'kind' | 'number' | 'name'> & { word?: string }, lang: 'zh' | 'en'): string {
  const word = lang === 'zh' ? STATEMENT_KINDS[label.kind].zh : STATEMENT_KINDS[label.kind].en;
  const num = label.number ? ` ${label.number.join('.')}` : '';
  const name = label.name ? (lang === 'zh' ? `（${label.name}）` : ` (${label.name})`) : '';
  return `${word}${num}${name}`;
}

export function statementAnchor(kind: StatementKind, number: string[]): string {
  return `${kind}-${number.join('.')}`;
}

export function sectionAnchor(number: string[]): string {
  return `sec-${number.join('.')}`;
}

export function equationAnchor(tag: string): string {
  return `eq-${tag}`;
}

/** Plain-text references: "定理 13.2.1", "Theorem 13.2.1", "式 (13.2)", "Eq. (13.2)". Numbers need at least one dot. */
export const REFERENCE_RE = new RegExp(
  `(${KIND_WORDS})\\s?(\\d+(?:\\.\\d+)+)(?![\\d.]*\\d)|(?:式|公式|Eq\\.|Equation)\\s?[（(](\\d+(?:\\.\\d+)+)[）)]`,
  'giu',
);

export function kindOfWord(word: string): StatementKind | undefined {
  return WORD_TO_KIND.get(word.toLowerCase()) ?? WORD_TO_KIND.get(word);
}

function escapeRe(s: string): string {
  return s.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
}
