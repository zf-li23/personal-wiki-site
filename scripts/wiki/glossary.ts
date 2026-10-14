/**
 * Terminology: content/glossary.yaml lists key concepts as { zh, en } pairs.
 * Rule for source-language (zh) pages: the FIRST occurrence of a glossary term in
 * body text (not headings, code or math) is followed by its English name in
 * full-width parentheses, e.g. "中心极限定理（Central Limit Theorem）".
 * `pnpm wiki terms` reports violations; translators use the glossary for consistent wording.
 */
import fs from 'node:fs';
import type { Root } from 'mdast';
import remarkGfm from 'remark-gfm';
import remarkMath from 'remark-math';
import remarkParse from 'remark-parse';
import { unified } from 'unified';
import { visit } from 'unist-util-visit';
import { parse as parseYaml } from 'yaml';
import type { Diagnostics } from './diagnostics.ts';
import { GLOSSARY_FILE } from './paths.ts';

export interface GlossaryTerm {
  zh: string;
  en: string;
  /** Other zh spellings that count as the same term. */
  aliases?: string[];
}

export function loadGlossary(diag: Diagnostics): GlossaryTerm[] {
  if (!fs.existsSync(GLOSSARY_FILE)) return [];
  let data: unknown;
  try {
    data = parseYaml(fs.readFileSync(GLOSSARY_FILE, 'utf8'));
  } catch (e) {
    diag.error(GLOSSARY_FILE, `invalid YAML: ${(e as Error).message}`);
    return [];
  }
  const terms = (data as { terms?: unknown })?.terms;
  if (!Array.isArray(terms)) {
    diag.error(GLOSSARY_FILE, 'expected a top-level "terms:" list');
    return [];
  }
  const seen = new Set<string>();
  const out: GlossaryTerm[] = [];
  terms.forEach((t, i) => {
    const term = t as GlossaryTerm;
    if (typeof term?.zh !== 'string' || typeof term?.en !== 'string') {
      diag.error(GLOSSARY_FILE, `terms[${i}] needs string "zh" and "en" fields`);
      return;
    }
    if (seen.has(term.zh)) diag.error(GLOSSARY_FILE, `duplicate term "${term.zh}"`);
    seen.add(term.zh);
    out.push(term);
  });
  return out;
}

export interface TermFinding {
  term: GlossaryTerm;
  line?: number;
}

/** Terms whose first body occurrence is not annotated with the English name. */
export function findUnannotatedTerms(body: string, terms: GlossaryTerm[]): TermFinding[] {
  const tree = unified().use(remarkParse).use(remarkGfm).use(remarkMath).parse(body) as Root;
  const segments: { value: string; line?: number }[] = [];
  visit(tree, (node) => {
    if (node.type === 'heading' || node.type === 'code' || node.type === 'math' || node.type === 'html') return 'skip';
    if (node.type === 'text') segments.push({ value: node.value, line: node.position?.start.line });
    return undefined;
  });
  const findings: TermFinding[] = [];
  for (const term of terms) {
    const names = [term.zh, ...(term.aliases ?? [])];
    for (const seg of segments) {
      const hit = names.map((n) => ({ n, i: seg.value.indexOf(n) })).filter((h) => h.i >= 0).sort((a, b) => a.i - b.i)[0];
      if (!hit) continue;
      const after = seg.value.slice(hit.i + hit.n.length);
      const annotated = new RegExp(`^\\s*[（(]\\s*${escapeRe(term.en)}`, 'i').test(after);
      if (!annotated) findings.push({ term, line: seg.line });
      break;
    }
  }
  return findings;
}

function escapeRe(s: string): string {
  return s.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
}
