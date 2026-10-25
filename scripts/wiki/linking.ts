/**
 * Cross-page linking, run after every page has been rendered (it needs all of them):
 *
 *  1. Statement index: numbered statements and tagged equations per course,
 *     so "定理 13.2.1" / "Theorem 13.2.1" / "式 (13.2)" in plain text link to their anchor.
 *     Numbers are course-scoped: references are only resolved within the same course.
 *  2. Concept definition sites (registry in glossary.ts), found in each page's source language:
 *       - a 定义 statement whose name is the concept:  **定义 13.1.1（依分布收敛）**
 *       - a bold concept name inside a 定义 statement:  **定义 1.1.1** 称 ……为**合取**
 *       - outside definitions, an annotated occurrence:  依分布收敛（convergence in distribution）
 *         in Chinese, an italic occurrence in English:  *convergence in distribution*
 *     English names match case-insensitively and in the plural (**groups** → group).
 *     A concept may be defined on one page only.
 *  3. Concept links: a bold run whose whole text is a concept name (**群**, **依分布收敛**)
 *     links to the definition (or, if there is none yet, becomes a hover card). Running text
 *     is never matched: authors bold what they want to emphasise.
 *
 * The page trees are mutated in place; build.ts stringifies them afterwards.
 */
import type { Element, ElementContent, Root, RootContent, Text } from 'hast';
import { toString as hastToString } from 'hast-util-to-string';
import { BASE_PATH, type Lang } from '../../site.config.ts';
import type { Diagnostics } from './diagnostics.ts';
import { type Concept, inScope } from './glossary.ts';
import type { RenderOutput } from './markdown.ts';
import { REFERENCE_RE, courseOf, kindOfWord, pageRole, parseStatementLabel } from './numbering.ts';
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
  /** Bold runs that are neither a concept name nor a statement label (for `pnpm wiki terms --bold`). */
  plainBold: { text: string; inDefinition: boolean }[];
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
  // Chinese text writes many concepts by their Latin abbreviation (**ReLU**, **LSTM**), so a
  // Chinese page accepts every alias; an English page only the non-Han ones.
  const names = lang === 'zh' ? [concept.zh, ...concept.aliases] : [concept.en, ...concept.aliases.filter((a) => !isHan(a))];
  return [...new Set(names)].filter(Boolean);
}

/** Lookup keys of a written name: itself, and for English lower-cased with plural forms undone. */
function nameKeys(text: string, lang: Lang): string[] {
  const t = text.trim().replace(/\s+/g, ' ');
  if (lang !== 'en') return [t];
  const l = t.toLowerCase();
  const keys = [l];
  // Any one word may be plural: "groups", "discontinuities of the first kind".
  const words = l.split(' ');
  words.forEach((w, i) => {
    for (const s of singulars(w)) keys.push([...words.slice(0, i), s, ...words.slice(i + 1)].join(' '));
  });
  return keys;
}

function singulars(w: string): string[] {
  const out: string[] = [];
  if (w.endsWith('ies')) out.push(`${w.slice(0, -3)}y`);
  if (w.endsWith('ices')) out.push(`${w.slice(0, -4)}ix`, `${w.slice(0, -4)}ex`); // matrices, vertices
  if (w.endsWith('ses')) out.push(`${w.slice(0, -2)}is`); // bases, hypotheses
  if (/(s|x|z|ch|sh)es$/.test(w)) out.push(w.slice(0, -2));
  if (w.endsWith('s') && !w.endsWith('ss')) out.push(w.slice(0, -1));
  return out;
}

/** An abbreviation in capitals (letters, digits, hyphens; no lower case): "CI", "GAG", "V(D)J" is not one. */
function isAbbreviation(name: string): boolean {
  return /^[A-Z0-9-]*[A-Z][A-Z0-9-]*$/.test(name);
}

/** Concepts by name in one language (only those in scope for the page, when given). */
function nameIndex(concepts: Concept[], lang: Lang, pageId?: string): (text: string) => Concept | undefined {
  const map = new Map<string, Concept>();
  // English abbreviations (CI, GAL, GAG, PCR) match only as written, in capitals: lower-case italics
  // are gene names and Latin words (*gal*, *gag*, *cis*), not the abbreviation.
  const abbreviations = new Map<string, Concept>();
  // Scoped concepts last, so that inside their scope they win over an unscoped homonym.
  const ordered = [...concepts].sort((a, b) => Number(!!a.scope?.length) - Number(!!b.scope?.length));
  for (const c of ordered) {
    if (pageId && !inScope(c, pageId)) continue;
    for (const n of conceptNames(c, lang)) {
      if (lang === 'en' && isAbbreviation(n)) abbreviations.set(n, c);
      else map.set(nameKeys(n, lang)[0], c);
    }
  }
  return (text) => {
    const t = text.trim();
    const abbreviation = abbreviations.get(t) ?? (t.endsWith('s') ? abbreviations.get(t.slice(0, -1)) : undefined);
    if (abbreviation) return abbreviation;
    for (const k of nameKeys(text, lang)) {
      const c = map.get(k);
      if (c) return c;
    }
    return undefined;
  };
}

/**
 * Unscoped concepts that a scoped homonym overrides on this page (the lattice "complement"
 * inside its scope): only the scoped one may take a definition site there.
 */
function shadowedConcepts(concepts: Concept[], pageId: string): Set<string> {
  const keys = (c: Concept) => [...conceptNames(c, 'zh'), ...conceptNames(c, 'en').map((n) => nameKeys(n, 'en')[0])];
  const scopedNames = new Set(concepts.filter((c) => c.scope?.length && inScope(c, pageId)).flatMap(keys));
  return new Set(concepts.filter((c) => !c.scope?.length && keys(c).some((k) => scopedNames.has(k))).map((c) => c.id));
}

/* ------------------------------------------------------------------ index */

interface SiteCandidate extends Target {
  file: string;
  /** A named non-definition statement: used only when there is no other candidate. */
  fallback?: boolean;
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
  // "名称（English，简称 X）" does not mark a definition; reported if the concept ends up with none.
  const nearMisses: { concept: Concept; file: string; text: string }[] = [];

  for (const [pageId, out] of sourceRenders) {
    const course = courseOf(pageId);
    const file = sourceFiles.get(pageId) ?? pageId;
    const lookup = nameIndex(concepts, out.contentLang, pageId);
    for (const s of out.statements) {
      statements.set(`${course}|${s.kind}|${s.number}`, { pageId, anchor: s.anchor });
      // A named definition defines its concept; a named theorem, algorithm… (not an example or
      // remark) does so only when the concept is defined nowhere else ("Lagrange 定理").
      const concept = s.name && s.kind !== 'ex' && s.kind !== 'rem' ? lookup(s.name) : undefined;
      if (concept) add(concept.id, { pageId, anchor: s.anchor, file, fallback: s.kind !== 'def' });
    }
    // A bold concept name inside a 定义 statement is the term being defined there.
    eachStrong(out.hast, (strong, _parent, _i, def) => {
      const concept = def ? lookup(hastToString(strong)) : undefined;
      if (concept && def) add(concept.id, { pageId, anchor: def, file });
    });
    const mayBeMarked = annotationCandidates(out.hast, out.contentLang);
    const shadowed = shadowedConcepts(concepts, pageId);
    for (const concept of concepts) {
      if (!inScope(concept, pageId) || shadowed.has(concept.id) || !mayBeMarked(concept)) continue;
      const anchor = markAnnotatedDefinition(out.hast, concept, out.contentLang);
      if (anchor) {
        out.anchors.add(anchor);
        add(concept.id, { pageId, anchor, file });
      } else if (out.contentLang === 'zh') {
        const text = nearMissAnnotation(hastToString(out.hast), concept);
        if (text) nearMisses.push({ concept, file, text });
      }
    }
  }

  const order = new Map(readingOrder.map((id, i) => [id, i]));
  const conceptSites = new Map<string, Target>();
  for (const concept of concepts) {
    const all = candidates.get(concept.id) ?? [];
    const list = all.some((c) => !c.fallback) ? all.filter((c) => !c.fallback) : all;
    if (!list.length) continue;
    // A statement definition beats an annotation on the same page; across pages the earliest wins.
    const pages = [...new Set(list.map((c) => c.pageId))].sort((a, b) => (order.get(a) ?? 0) - (order.get(b) ?? 0));
    const onFirst = list.filter((c) => c.pageId === pages[0]);
    const chosen = onFirst.find((c) => !c.anchor.startsWith('concept-')) ?? onFirst[0];
    conceptSites.set(concept.id, { pageId: chosen.pageId, anchor: chosen.anchor });
    // Restating a definition in a later chapter (a 定义 label) is normal; a second English
    // annotation is not, because the annotation marks *the* definition.
    for (const extra of list.filter((c) => c.pageId !== chosen.pageId && c.anchor.startsWith('concept-'))) {
      diag.error(extra.file, `concept "${concept.zh}（${concept.en}）" is already defined on page ${chosen.pageId}; keep the defining mark (English annotation, or italics in English) only at the definition`);
    }
  }
  for (const { concept, file, text } of nearMisses) {
    if (conceptSites.has(concept.id)) continue;
    diag.warn(file, `"${text}" is not recognized as the definition of "${concept.zh}", which is defined nowhere: write ${concept.zh}（${concept.en}） with nothing else inside the parentheses, and put "简称…" or other notes outside`);
  }
  void tree;
  return { statements, concepts, conceptSites };
}

/**
 * A cheap necessary condition for markAnnotatedDefinition, so that it runs only for the few
 * concepts that can be marked on a page (instead of walking the page once per concept):
 * in English an emphasised run must spell one of the names, in Chinese the page text must
 * contain both a Chinese and an English name.
 */
function annotationCandidates(root: Root, lang: Lang): (concept: Concept) => boolean {
  if (lang === 'en') {
    const keys = new Set<string>();
    const walk = (parent: Root | Element) => {
      for (const child of parent.children) {
        if (child.type !== 'element' || skippable(child)) continue;
        if (child.tagName === 'em' || child.tagName === 'i') for (const k of nameKeys(hastToString(child), 'en')) keys.add(k);
        walk(child);
      }
    };
    walk(root);
    return (concept) => conceptNames(concept, 'en').some((n) => keys.has(nameKeys(n, 'en')[0]));
  }
  const text = hastToString(root);
  const lower = text.toLowerCase();
  const latin = annotationCandidates(root, 'en');
  return (concept) =>
    (!/\p{Script=Han}/u.test(concept.zh) && latin(concept)) ||
    (conceptNames(concept, 'zh').some((n) => text.includes(n)) && conceptNames(concept, 'en').some((n) => lower.includes(n.toLowerCase())));
}

/** "名称（English，简称 X）": an annotation with extra text inside the parentheses, which does not mark the definition. */
function nearMissAnnotation(text: string, concept: Concept): string | null {
  const en = conceptNames(concept, 'en').map(escapeRe).join('|');
  for (const name of conceptNames(concept, 'zh')) {
    const m = new RegExp(`${escapeRe(name)}[（(]\\s*(?:${en})\\s*[，,；;、][^）)]*[）)]`, 'i').exec(text);
    if (m) return m[0];
  }
  return null;
}

/**
 * Find the marked defining occurrence outside definitions and turn it into <dfn id="concept-…">:
 * in Chinese "名称（English）" (or a bold 名称 followed by （English）), in English the first
 * italic occurrence of the name. Returns the anchor, or null when the page has no such mark.
 */
function markAnnotatedDefinition(root: Root, concept: Concept, lang: Lang): string | null {
  const anchor = `concept-${concept.id}`;
  if (lang === 'en') return markEmphasis(root, concept, anchor, ['em', 'i']) ? anchor : null;
  // A concept whose Chinese name is the Latin name itself (NoSQL, Scrum) cannot take
  // "名称（English）" without repeating the name, so Chinese pages mark it with italics too.
  if (!/\p{Script=Han}/u.test(concept.zh) && markEmphasis(root, concept, anchor, ['em', 'i'])) return anchor;
  // The annotation may use the English name or any English alias, but not a bare abbreviation:
  // "常微分方程（ODE）" only introduces the abbreviation, it does not mark the definition.
  const en = conceptNames(concept, 'en')
    .filter((n) => n === concept.en || !/^[A-Z]{2,6}s?$/.test(n))
    .map(escapeRe)
    .join('|');
  const enRe = new RegExp(`^\\s*[（(]\\s*(?:${en})\\s*[）)]`, 'i');
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
        const re = new RegExp(`${escapeRe(name)}(?=\\s*[（(]\\s*(?:${en})\\s*[）)])`, 'i');
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
  const result: LinkResult = { targets: new Set(out.links.map((l) => l.targetId)), concepts: new Set(), forwardUses: [], plainBold: [] };
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

  // 2. concepts: only a bold run whose whole text is a concept name refers to the concept
  //    (authors bold what they want to emphasise; running text is never matched).
  for (const [id, site] of index.conceptSites) {
    if (site.pageId !== pageId) continue;
    result.concepts.add(id);
    if (site.anchor.startsWith('concept-') && !out.anchors.has(site.anchor)) {
      // Translation of the defining page: its own defining mark (annotation / italics),
      // or else its first bold mention, becomes the definition anchor.
      const concept = index.concepts.find((c) => c.id === id)!;
      const marked = markAnnotatedDefinition(out.hast, concept, lang) ?? (markFirstBold(out.hast, concept, lang, site.anchor) ? site.anchor : null);
      if (marked === site.anchor) out.anchors.add(site.anchor);
    }
  }
  const lookup = nameIndex(index.concepts, lang, pageId);
  eachStrong(out.hast, (strong, parent, i, def) => {
    const name = hastToString(strong).trim();
    // "**命题**：…" is an unnumbered statement label, not the concept 命题.
    const next = parent.children[i + 1];
    if (parseStatementLabel(name) && next?.type === 'text' && /^\s*[：:.]/.test(next.value)) return;
    const id = lookup(name)?.id;
    if (!id) {
      if (!PROOF_WORD.test(name) && !parseStatementLabel(name)) result.plainBold.push({ text: name, inDefinition: !!def });
      return;
    }
    result.concepts.add(id);
    const site = index.conceptSites.get(id);
    if (!site) {
      // No definition yet: a hover card only.
      strong.properties = { ...strong.properties, className: ['concept-ref'], dataConcept: id };
    } else if (site.pageId !== pageId) {
      parent.children[i] = el('a', { href: hrefTo(site, linkLang, pageId), className: ['concept-ref'], dataConcept: id, dataInternal: '' }, [strong]);
      result.targets.add(site.pageId);
      // Overview pages introduce what their chapters define; only chapters can use a concept too early.
      if (pageRole(pageId) === 'chapter' && (readingOrder.get(pageId) ?? 0) < (readingOrder.get(site.pageId) ?? 0)) result.forwardUses.push(id);
    }
  });
  result.targets.delete(pageId);
  return result;
}

/** Unnumbered proof / solution openers are labels, not emphasis. */
const PROOF_WORD = /^(证明|解|答|Proof|Solution|Answer)[:：.]?$/i;

/**
 * Visit bold runs that may refer to concepts (not labels, not inside links, headings or code).
 * `def` is the anchor of the enclosing 定义 statement (def-…), if any.
 */
function eachStrong(root: Root | Element, fn: (node: Element, parent: Root | Element, index: number, def: string | null) => void): void {
  const walk = (parent: Root | Element, def: string | null) => {
    const children = parent.children as (RootContent | ElementContent)[];
    children.forEach((child, i) => {
      if (child.type !== 'element' || skippable(child)) return;
      if (child.tagName === 'strong' || child.tagName === 'b') fn(child, parent, i, def);
      else {
        const id = child.properties?.id;
        walk(child, typeof id === 'string' && id.startsWith('def-') ? id : def);
      }
    });
  };
  walk(root, null);
}

/** Wrap the first emphasised (`tags`) occurrence of the concept's English name in <dfn id=anchor>. */
function markEmphasis(root: Root, concept: Concept, anchor: string, tags: string[]): boolean {
  const lookup = nameIndex([concept], 'en');
  let done = false;
  const walk = (parent: Root | Element) => {
    const children = parent.children as (RootContent | ElementContent)[];
    for (let i = 0; i < children.length && !done; i++) {
      const child = children[i];
      if (child.type !== 'element' || skippable(child)) continue;
      if (tags.includes(child.tagName) && lookup(hastToString(child))) {
        children[i] = el('dfn', { id: anchor, className: ['wiki-dfn'], dataConcept: concept.id }, [child]);
        done = true;
      } else walk(child);
    }
  };
  walk(root);
  return done;
}

/** In a translated defining page without a defining mark, wrap the first bold mention in <dfn id=anchor>. */
function markFirstBold(root: Root, concept: Concept, lang: Lang, anchor: string): boolean {
  const lookup = nameIndex([concept], lang);
  let done = false;
  eachStrong(root, (strong, parent, i) => {
    if (done || !lookup(hastToString(strong))) return;
    parent.children[i] = el('dfn', { id: anchor, className: ['wiki-dfn'], dataConcept: concept.id }, [strong]);
    done = true;
  });
  return done;
}
