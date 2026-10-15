/**
 * Concept registry: content/glossary.yaml lists the concepts ("词条") shared across courses.
 *
 *   terms:
 *     - { zh: 中心极限定理, en: central limit theorem, aliases: [CLT] }
 *     - { zh: 特征函数, en: characteristic function, scope: ["3"] }   # only statistics pages
 *
 * A concept's id is its English name in kebab-case (central-limit-theorem). Where a concept is
 * *defined* is found in the content, not stored here (see linking.ts), so the registry cannot drift.
 */
import fs from 'node:fs';
import { parse as parseYaml } from 'yaml';
import type { Diagnostics } from './diagnostics.ts';
import { GLOSSARY_FILE } from './paths.ts';

export interface Concept {
  id: string;
  zh: string;
  en: string;
  /** Other spellings (either language) that count as the same concept. */
  aliases: string[];
  /**
   * Page-id prefixes (disciplines or courses, e.g. "3" or "1.2") where the concept is recognised.
   * Use it when the same word means something else elsewhere (特征函数 in probability vs. sets).
   */
  scope?: string[];
}

/** Whether a concept applies on a page (no scope = everywhere). */
export function inScope(concept: Concept, pageId: string): boolean {
  return !concept.scope?.length || concept.scope.some((s) => pageId === s || pageId.startsWith(`${s}.`));
}

export function conceptId(en: string): string {
  return en
    .toLowerCase()
    .normalize('NFKD')
    .replace(/[\u0300-\u036f]/g, '')
    .replace(/'s\b/g, 's')
    .replace(/[^a-z0-9]+/g, '-')
    .replace(/^-|-$/g, '');
}

export function loadConcepts(diag: Diagnostics, file = GLOSSARY_FILE): Concept[] {
  if (!fs.existsSync(file)) return [];
  let data: unknown;
  try {
    data = parseYaml(fs.readFileSync(file, 'utf8'));
  } catch (e) {
    diag.error(file, `invalid YAML: ${(e as Error).message}`);
    return [];
  }
  const terms = (data as { terms?: unknown })?.terms;
  if (!Array.isArray(terms)) {
    diag.error(file, 'expected a top-level "terms:" list');
    return [];
  }
  const ids = new Map<string, string>();
  const names = new Map<string, string>();
  const out: Concept[] = [];
  terms.forEach((t, i) => {
    const term = t as { zh?: unknown; en?: unknown; aliases?: unknown; scope?: unknown };
    for (const k of Object.keys(term)) if (!['zh', 'en', 'aliases', 'scope'].includes(k)) diag.error(file, `terms[${i}]: unknown field "${k}" (allowed: zh, en, aliases, scope)`);
    if (typeof term?.zh !== 'string' || typeof term?.en !== 'string') {
      diag.error(file, `terms[${i}] needs string "zh" and "en" fields`);
      return;
    }
    const aliases = Array.isArray(term.aliases) ? term.aliases.filter((a): a is string => typeof a === 'string') : [];
    const id = conceptId(term.en);
    if (ids.has(id)) diag.error(file, `"${term.en}" duplicates the concept "${ids.get(id)}"`);
    ids.set(id, term.en);
    for (const name of [term.zh, ...aliases]) {
      if (names.has(name)) diag.error(file, `name "${name}" is used by two concepts (${names.get(name)} and ${term.en})`);
      names.set(name, term.en);
    }
    const scope = Array.isArray(term.scope) ? term.scope.map(String) : [];
    if (term.scope !== undefined && !scope.length) diag.error(file, `"${term.en}": scope must be a list of page ids, e.g. scope: ["3"]`);
    out.push({ id, zh: term.zh, en: term.en, aliases, ...(scope.length ? { scope } : {}) });
  });
  return out;
}
