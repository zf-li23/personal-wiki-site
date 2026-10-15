/**
 * Cross-page linking, run after every page has been rendered (it needs all of them):
 *
 *  1. Statement index: numbered statements and tagged equations per course,
 *     so "定理 13.2.1" / "Theorem 13.2.1" / "式 (13.2)" in plain text link to their anchor.
 *     Numbers are course-scoped: references are only resolved within the same course.
 *  2. Concept definition sites (registry in glossary.ts), found in the source-language pages:
 *       - a 定义 statement whose name is the concept:  **定义 13.1.1（依分布收敛）**
 *       - an annotated occurrence:  依分布收敛（convergence in distribution）
 *     A concept may be defined on one page only.
 *  3. Concept links: the first mention of each concept on every other page links to its
 *     definition (or, if it has none yet, becomes a hover card without a link).
 *
 * The page trees are mutated in place; build.ts stringifies them afterwards.
 */
import type { Element, ElementContent, Root, RootContent, Text } from 'hast';
import { toString as hastToString } from 'hast-util-to-string';
import { BASE_PATH, type Lang } from '../../site.config.ts';
import type { Diagnostics } from './diagnostics.ts';
import { type Concept, inScope } from './glossary.ts';
import type { RenderOutput } from './markdown.ts';
import { REFERENCE_RE, courseOf, kindOfWord } from './numbering.ts';
import type { ContentTree } from './scan.ts';

export interface Target {
  pageId: string;
  anchor: string;
}

export interface LinkIndex {
  /** `${course}|${kind}|${number}` → where the statement / equation lives. */
  statements: Map<string, Target>;
  concepts: Concept[];
  /** Concept id → definition site. */
  conceptSites: Map<string, Target>;
}

export interface LinkResult {
  /** Pages this page links to (explicit links, references, concept links). */
  targets: Set<string>;
  /** Concepts mentioned or defined on this page. */
  concepts: Set<string>;
  /** Concepts mentioned here before they are defined (in reading order). */
  forwardUses: string[];
}

const SKIP_TAGS = new Set(['a', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'code', 'pre', 'script', 'style', 'dfn', 'svg']);
const SKIP_CLASSES = ['wiki-label-text', 'katex', 'katex-display', 'wiki-mermaid', 'wiki-stmt-label', 'wiki-dfn', 'heading-anchor', 'wiki-plot-source'];

function skippable(node: Element): boolean {
  if (SKIP_TAGS.has(node.tagName)) return true;
  const cls = node.properties?.className;
  return Array.isArray(cls) && cls.some((c) => SKIP_CLASSES.includes(String(c)));
}

/** Visit every text node that may receive links, with the ability to replace it by several nodes. */
function eachText(root: Root | Element, fn: (node: Text) => ElementContent[] | null): void {
  const walk = (parent: Root | Element) => {
    const children = parent.children as (RootContent | ElementContent)[];
    for (let i = 0; i < children.length; i++) {
      const child = children[i];
      if (child.type === 'element') {
        if (!skippable(child)) walk(child);
      } else if (child.type === 'text') {
        const replacement = fn(child);
        if (replacement) {
          children.splice(i, 1, ...replacement);
          i += replacement.length - 1;
        }
      }
    }
  };
  walk(root);
}

function escapeRe(s: string): string {
  return s.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
}

function el(tagName: string, properties: Element['properties'], children: ElementContent[]): Element {
  return { type: 'element', tagName, properties, children };
}

function hrefTo(target: Target, linkLang: Lang, fromPage: string): string {
  return target.pageId === fromPage ? `#${target.anchor}` : `${BASE_PATH}${linkLang}/${target.pageId}/#${target.anchor}`;
}

function conceptNames(concept: Concept, lang: Lang): string[] {
  const isHan = (s: string) => /\p{Script=Han}/u.test(s);
  const names = lang === 'zh' ? [concept.zh, ...concept.aliases.filter(isHan)] : [concept.en, ...concept.aliases.filter((a) => !isHan(a))];
  return [...new Set(names)].filter(Boolean);
}

/** Longest-first alternation so 分岔图 is not matched as 分岔. */
function namesRegex(concepts: Concept[], lang: Lang): { re: RegExp | null; byName: Map<string, string> } {
  const byName = new Map<string, string>();
  // Single Chinese characters (群, 环, 域, 格) are never matched in running text: without word
  // boundaries they would hit 循环, 定义域, …. Such concepts still get definition sites and cards.
  for (const c of concepts) {
    for (const n of conceptNames(c, lang)) if (lang === 'en' || [...n].length > 1) byName.set(lang === 'en' ? n.toLowerCase() : n, c.id);
  }
  const names = [...byName.keys()].sort((a, b) => b.length - a.length).map(escapeRe);
  if (!names.length) return { re: null, byName };
  const body = names.join('|');
  return { re: lang === 'en' ? new RegExp(`\\b(?:${body})\\b`, 'gi') : new RegExp(body, 'g'), byName };
}

/* ------------------------------------------------------------------ index */

interface SiteCandidate extends Target {
  file: string;
}

export function buildLinkIndex(
  tree: ContentTree,
  sourceRenders: Map<string, RenderOutput>,
  sourceFiles: Map<string, string>,
  concepts: Concept[],
  readingOrder: string[],
  diag: Diagnostics,
): LinkIndex {
  const statements = new Map<string, Target>();
  const candidates = new Map<string, SiteCandidate[]>();
  const add = (id: string, c: SiteCandidate) => candidates.set(id, [...(candidates.get(id) ?? []), c]);
  const byZhName = new Map<string, Concept>();
  for (const c of concepts) for (const n of conceptNames(c, 'zh')) byZhName.set(n, c);

  for (const [pageId, out] of sourceRenders) {
    const course = courseOf(pageId);
    const file = sourceFiles.get(pageId) ?? pageId;
    for (const s of out.statements) {
      statements.set(`${course}|${s.kind}|${s.number}`, { pageId, anchor: s.anchor });
      const named = s.kind === 'def' && s.name ? byZhName.get(s.name) : undefined;
      const concept = named && inScope(named, pageId) ? named : undefined;
      if (concept) add(concept.id, { pageId, anchor: s.anchor, file });
    }
    for (const concept of concepts) {
      if (!inScope(concept, pageId)) continue;
      const anchor = markAnnotatedDefinition(out.hast, concept);
      if (anchor) {
        out.anchors.add(anchor);
        add(concept.id, { pageId, anchor, file });
      }
    }
  }

  const order = new Map(readingOrder.map((id, i) => [id, i]));
  const conceptSites = new Map<string, Target>();
  for (const concept of concepts) {
    const list = candidates.get(concept.id);
    if (!list?.length) continue;
    // A statement definition beats an annotation on the same page; across pages the earliest wins.
    const pages = [...new Set(list.map((c) => c.pageId))].sort((a, b) => (order.get(a) ?? 0) - (order.get(b) ?? 0));
    const onFirst = list.filter((c) => c.pageId === pages[0]);
    const chosen = onFirst.find((c) => !c.anchor.startsWith('concept-')) ?? onFirst[0];
    conceptSites.set(concept.id, { pageId: chosen.pageId, anchor: chosen.anchor });
    // Restating a definition in a later chapter (a 定义 label) is normal; a second English
    // annotation is not, because the annotation marks *the* definition.
    for (const extra of list.filter((c) => c.pageId !== chosen.pageId && c.anchor.startsWith('concept-'))) {
      diag.error(extra.file, `concept "${concept.zh}（${concept.en}）" is already defined on page ${chosen.pageId}; keep the English annotation only at the definition`);
    }
  }
  void tree;
  return { statements, concepts, conceptSites };
}

/**
 * Find "名称（English）" (or a bold 名称 followed by （English）) in a source page and turn the
 * name into <dfn id="concept-…">. Returns the anchor, or null when the page has no annotation.
 */
function markAnnotatedDefinition(root: Root, concept: Concept): string | null {
  const anchor = `concept-${concept.id}`;
  const enRe = new RegExp(`^\\s*[（(]\\s*${escapeRe(concept.en)}\\s*[）)]`, 'i');
  let found = false;

  const dfn = (children: ElementContent[]): Element => el('dfn', { id: anchor, className: ['wiki-dfn'], dataConcept: concept.id }, children);

  const walk = (parent: Root | Element) => {
    const children = parent.children as (RootContent | ElementContent)[];
    for (let i = 0; i < children.length && !found; i++) {
      const child = children[i];
      const next = children[i + 1];
      if (child.type === 'element') {
        // **名称**（English）: wrap the bold run itself.
        if (/^(strong|em|b)$/.test(child.tagName) && conceptNames(concept, 'zh').includes(hastToString(child).trim()) && next?.type === 'text' && enRe.test(next.value)) {
          children[i] = dfn([child]);
          found = true;
          return;
        }
        if (!skippable(child)) walk(child);
        continue;
      }
      if (child.type !== 'text') continue;
      for (const name of conceptNames(concept, 'zh')) {
        const re = new RegExp(`${escapeRe(name)}(?=\\s*[（(]\\s*${escapeRe(concept.en)}\\s*[）)])`, 'i');
        const m = re.exec(child.value);
        if (!m) continue;
        const before = child.value.slice(0, m.index);
        const after = child.value.slice(m.index + name.length);
        const parts: ElementContent[] = [];
        if (before) parts.push({ type: 'text', value: before });
        parts.push(dfn([{ type: 'text', value: name }]));
        if (after) parts.push({ type: 'text', value: after });
        children.splice(i, 1, ...parts);
        found = true;
        return;
      }
    }
  };
  walk(root);
  return found ? anchor : null;
}

/* ------------------------------------------------------------------- pass */

export interface LinkPageInput {
  pageId: string;
  out: RenderOutput;
  /** Reader language: links point to pages in this language. */
  linkLang: Lang;
  tree: ContentTree;
  index: LinkIndex;
  readingOrder: Map<string, number>;
  /** Unresolvable references are reported here (pass a throwaway for fallback renders). */
  diag: Diagnostics;
  file: string;
}

export function linkPage({ pageId, out, linkLang, tree, index, readingOrder, diag, file }: LinkPageInput): LinkResult {
  const result: LinkResult = { targets: new Set(out.links.map((l) => l.targetId)), concepts: new Set(), forwardUses: [] };
  const course = courseOf(pageId);
  const lang = out.contentLang;

  // 1. statement / equation references
  eachText(out.hast, (node) => {
    const re = new RegExp(REFERENCE_RE.source, REFERENCE_RE.flags);
    const parts: ElementContent[] = [];
    let last = 0;
    for (const m of node.value.matchAll(re)) {
      const kind = m[1] ? kindOfWord(m[1]) : 'eq';
      const number = m[2] ?? m[3];
      if (!kind || !number) continue;
      const target = index.statements.get(`${course}|${kind}|${number}`);
      if (!target) {
        const chapter = `${course}.${number.split('.')[0]}`;
        if (tree.pages.has(chapter)) diag.warn(file, `"${m[0]}" does not match any numbered ${kind === 'eq' ? 'equation' : 'statement'} on page ${chapter}`);
        continue;
      }
      if (m.index > last) parts.push({ type: 'text', value: node.value.slice(last, m.index) });
      parts.push(el('a', { href: hrefTo(target, linkLang, pageId), className: ['wiki-ref'], ...(target.pageId !== pageId ? { dataInternal: '' } : {}) }, [{ type: 'text', value: m[0] }]));
      if (target.pageId !== pageId) result.targets.add(target.pageId);
      last = m.index + m[0].length;
    }
    if (!parts.length) return null;
    if (last < node.value.length) parts.push({ type: 'text', value: node.value.slice(last) });
    return parts;
  });

  // 2. concepts: definitions on this page count as mentioned; first other mention links to the definition
  for (const [id, site] of index.conceptSites) {
    if (site.pageId === pageId) {
      result.concepts.add(id);
      if (site.anchor.startsWith('concept-') && !out.anchors.has(site.anchor)) {
        // Translation of the defining page: mark the first English mention as the definition.
        const concept = index.concepts.find((c) => c.id === id)!;
        markFirstMention(out.hast, conceptNames(concept, lang), lang, site.anchor, id);
        out.anchors.add(site.anchor);
      }
    }
  }
  const { re, byName } = namesRegex(index.concepts.filter((c) => inScope(c, pageId)), lang);
  const excluded = new Map(index.concepts.map((c) => [c.id, c.exclude ?? []]));
  if (re) {
    const seen = new Set(result.concepts);
    eachText(out.hast, (node) => {
      const parts: ElementContent[] = [];
      let last = 0;
      for (const m of node.value.matchAll(new RegExp(re.source, re.flags))) {
        const id = byName.get(lang === 'en' ? m[0].toLowerCase() : m[0]);
        if (!id || seen.has(id) || insideExcluded(node.value, m.index, m[0].length, excluded.get(id))) continue;
        seen.add(id);
        result.concepts.add(id);
        const site = index.conceptSites.get(id);
        if (m.index > last) parts.push({ type: 'text', value: node.value.slice(last, m.index) });
        const label: ElementContent[] = [{ type: 'text', value: m[0] }];
        if (site) {
          parts.push(el('a', { href: hrefTo(site, linkLang, pageId), className: ['concept-ref'], dataConcept: id, dataInternal: '' }, label));
          result.targets.add(site.pageId);
          if ((readingOrder.get(pageId) ?? 0) < (readingOrder.get(site.pageId) ?? 0)) result.forwardUses.push(id);
        } else {
          parts.push(el('span', { className: ['concept-ref'], dataConcept: id }, label));
        }
        last = m.index + m[0].length;
      }
      if (!parts.length) return null;
      if (last < node.value.length) parts.push({ type: 'text', value: node.value.slice(last) });
      return parts;
    });
  }
  result.targets.delete(pageId);
  return result;
}

/** Whether text[at, at+len) lies inside one of the excluded compounds (e.g. 分岔 inside 分岔图). */
function insideExcluded(text: string, at: number, len: number, words: string[] | undefined): boolean {
  for (const w of words ?? []) {
    for (let i = text.indexOf(w); i !== -1; i = text.indexOf(w, i + 1)) {
      if (i <= at && at + len <= i + w.length) return true;
    }
  }
  return false;
}

function markFirstMention(root: Root, names: string[], lang: Lang, anchor: string, id: string): void {
  if (!names.length) return;
  const body = names.map(escapeRe).join('|');
  const re = lang === 'en' ? new RegExp(`\\b(?:${body})\\b`, 'i') : new RegExp(body);
  let done = false;
  eachText(root, (node) => {
    if (done) return null;
    const m = re.exec(node.value);
    if (!m) return null;
    done = true;
    const parts: ElementContent[] = [];
    if (m.index) parts.push({ type: 'text', value: node.value.slice(0, m.index) });
    parts.push(el('dfn', { id: anchor, className: ['wiki-dfn'], dataConcept: id }, [{ type: 'text', value: m[0] }]));
    const rest = node.value.slice(m.index + m[0].length);
    if (rest) parts.push({ type: 'text', value: rest });
    return parts;
  });
}
