/**
 * Markdown -> HTML for one page in one language. This is the only Markdown
 * parser in the project: the client receives finished HTML and never parses
 * Markdown itself.
 *
 * Pipeline: remark-parse -> gfm -> math -> (checks, incl. heading numbering) -> rehype ->
 * raw HTML -> wiki transforms (ids, links, images, plots, mermaid) -> chemical structures -> statements and
 * equations -> highlight -> KaTeX -> finalize (code-block chrome, code tabs).
 *
 * The result keeps the HAST: cross-page references and concept links need every page
 * rendered first, so linking.ts mutates the trees and only then are they stringified.
 */
import path from 'node:path';
import GithubSlugger from 'github-slugger';
import type { Element, ElementContent, Root as HastRoot, RootContent } from 'hast';
import { toHtml } from 'hast-util-to-html';
import { toString as hastToString } from 'hast-util-to-string';
import { toString as mdastToString } from 'mdast-util-to-string';
import latex from 'highlight.js/lib/languages/latex';
// Registers \ce / \pu (chemistry) on the KaTeX instance rehype-katex uses (versions are pinned equal, see tests).
import katex from 'katex';
import 'katex/contrib/mhchem';
import dockerfile from 'highlight.js/lib/languages/dockerfile';
import http from 'highlight.js/lib/languages/http';
import matlab from 'highlight.js/lib/languages/matlab';
import protobuf from 'highlight.js/lib/languages/protobuf';
import tcl from 'highlight.js/lib/languages/tcl';
import verilog from 'highlight.js/lib/languages/verilog';
import vhdl from 'highlight.js/lib/languages/vhdl';
import { common } from 'lowlight';
import type { Code, Root as MdastRoot, RootContent as MdastContent } from 'mdast';
import rehypeHighlight from 'rehype-highlight';
import rehypeKatex from 'rehype-katex';
import rehypeRaw from 'rehype-raw';
import remarkGfm from 'remark-gfm';
import remarkMath from 'remark-math';
import remarkParse from 'remark-parse';
import remarkRehype from 'remark-rehype';
import { unified } from 'unified';
import { visit } from 'unist-util-visit';
import { VFile } from 'vfile';
import { BASE_PATH, type Lang } from '../../site.config.ts';
import type { TocHeading } from '../../src/shared/types.ts';
import { drawStructure, parseChemBlock } from './chem.ts';
import type { Diagnostics } from './diagnostics.ts';
import {
  type HeadingInput,
  type StatementKind,
  checkHeadings,
  checkEndSections,
  endSection,
  ANSWER_LABEL,
  equationAnchor,
  formatStatementLabel,
  numberPrefix,
  pageRole,
  parseHeadingNumber,
  parseStatementLabel,
  sectionAnchor,
  statementAnchor,
} from './numbering.ts';
import { checkNotation } from './notation.ts';
import { PUBLIC_PATHS } from './paths.ts';
import { iconCredits, SHARE_ALIKE, type PlotResult, type PlotResults } from './plots.ts';
import type { ContentTree, PageSource } from './scan.ts';

export interface RenderContext {
  page: PageSource;
  tree: ContentTree;
  plots: PlotResults;
  diag: Diagnostics;
  /** Markdown file being rendered (for diagnostics). */
  file: string;
  /** Lines before the body in `file`. */
  lineOffset: number;
  /** Language that internal links point to (the reader's language, not necessarily the body's). */
  linkLang: Lang;
  /** Language the Markdown body is written in. */
  contentLang: Lang;
  /** Collected while rendering: plot scripts and assets referenced by the body. */
  usedPlots: Set<string>;
  usedAssets: Set<string>;
}

export interface PageLink {
  targetId: string;
  anchor?: string;
  line?: number;
}

export interface StatementInfo {
  /** Statement kind, or 'eq' for a display equation with \tag{…}. */
  kind: StatementKind | 'eq';
  /** Dotted number, e.g. "13.2.1". */
  number: string;
  name?: string;
  anchor: string;
  line?: number;
}

export interface RenderOutput {
  /** Final tree; stringified by build.ts after linking.ts has resolved references. */
  hast: HastRoot;
  /** Language of the Markdown that was rendered (the source language for untranslated pages). */
  contentLang: Lang;
  /** Numbered statements (定理 13.2.1 …) on this page, in order. */
  statements: StatementInfo[];
  headings: TocHeading[];
  /** Every element id in the page, for validating `#anchor` links. */
  anchors: Set<string>;
  /** Links to other pages, validated after all pages are rendered. */
  links: PageLink[];
  /** Same-page `#anchor` links. */
  localAnchors: { anchor: string; line?: number }[];
  /** Plain text without code and math (search index). */
  text: string;
  /** First paragraph as plain text (meta description fallback). */
  excerpt: string;
}

interface State {
  ctx: RenderContext;
  out: RenderOutput;
}

const MEDIA_ROOT = `${BASE_PATH}${PUBLIC_PATHS.media}`;
const PLOTS_ROOT = `${BASE_PATH}${PUBLIC_PATHS.plots}`;
const INTERNAL_LINK_RE = /^\/([1-9]\d*(?:\.[1-9]\d*)*)\/?(?:#(.+))?$/;
const CUSTOM_ID_RE = /\s*\{#([A-Za-z][A-Za-z0-9_-]*)\}\s*$/;

function el(tagName: string, properties: Element['properties'], children: ElementContent[] = []): Element {
  return { type: 'element', tagName, properties, children };
}

function text(value: string): ElementContent {
  return { type: 'text', value };
}

function hasClass(node: Element, name: string): boolean {
  const cls = node.properties?.className;
  return Array.isArray(cls) && cls.includes(name);
}

function lineOf(state: State, node: { position?: { start: { line: number } } }): number | undefined {
  return node.position ? node.position.start.line + state.ctx.lineOffset : undefined;
}

/* ------------------------------------------------------------------ remark */

/** Source-level rules that need the Markdown AST (code-aware). */
/** A fenced block marked as one tab of a group: ```cpp tab */
const isTabCode = (n: MdastContent): n is Code => n.type === 'code' && /(^|\s)tab(\s|$)/.test(n.meta ?? '');

/**
 * Adjacent ```cpp tab / ```python tab blocks become one block with a tab per language
 * (div.wiki-code-tabs; rehypeFinalize adds the tab list, Article.tsx switches the tabs).
 */
function remarkCodeTabs(state: State) {
  return (tree: MdastRoot) => {
    visit(tree, (node) => {
      if ((node.type as string) === 'codeTabs') return 'skip';
      if (!('children' in node)) return undefined;
      const children = node.children as MdastContent[];
      for (let i = 0; i < children.length; i++) {
        if (!isTabCode(children[i])) continue;
        let j = i;
        while (j + 1 < children.length && isTabCode(children[j + 1])) j++;
        const run = children.slice(i, j + 1) as Code[];
        const line = run[0].position ? run[0].position.start.line + state.ctx.lineOffset : undefined;
        const langs = run.map((c) => c.lang ?? '');
        if (run.length < 2) {
          state.ctx.diag.warn(state.ctx.file, 'a ```<lang> tab block needs a neighbour: write the tabs as adjacent code blocks (e.g. ```cpp tab then ```python tab)', line);
          continue;
        }
        if (langs.some((l) => !l) || new Set(langs).size !== langs.length) {
          state.ctx.diag.warn(state.ctx.file, `the code blocks of a tab group need different languages (got ${langs.map((l) => l || '(none)').join(', ')})`, line);
        }
        const group = { type: 'codeTabs', children: run, data: { hName: 'div', hProperties: { className: ['wiki-code-tabs'] } } };
        children.splice(i, run.length, group as unknown as MdastContent);
      }
      return undefined;
    });
  };
}

function remarkWikiChecks(state: State) {
  return (tree: MdastRoot, file: VFile) => {
    const source = String(file.value);
    const headings: HeadingInput[] = [];
    visit(tree, (node) => {
      if (node.type === 'heading' && node.depth >= 2 && node.position) {
        headings.push({ depth: node.depth, text: mdastToString(node).replace(CUSTOM_ID_RE, ''), line: node.position.start.line + state.ctx.lineOffset });
      }
      const line = node.position ? node.position.start.line + state.ctx.lineOffset : undefined;
      if (node.type === 'heading' && node.depth === 1) {
        state.ctx.diag.error(state.ctx.file, 'do not use "# " headings; the page title is the H1. Start sections at "## "', line);
      }
      if (node.type === 'code' && node.lang === 'python-plot') {
        state.ctx.diag.error(
          state.ctx.file,
          'inline ```python-plot blocks are no longer supported: move the code to plots/<name>.py and embed it with ![caption](./plots/<name>.py)',
          line,
        );
      }
      if ((node.type === 'math' || node.type === 'inlineMath') && typeof node.value === 'string') {
        for (const rule of checkNotation(node.value, state.ctx.page.id)) {
          state.ctx.diag.warn(state.ctx.file, `notation (${rule.id}): write ${rule.advice}${rule.fix ? ' — `pnpm wiki fix` does this' : ''} (CONTENT_GUIDE §7)`, line);
        }
      }
      if (state.ctx.contentLang === 'en' && hanText(node)) {
        state.ctx.diag.warn(state.ctx.file, `Chinese text on an English page: "${truncateText(hanText(node)!, 40)}" (translate it; sources belong in the front matter)`, line);
      }
      // The reader does not know which slides; sources belong in the front matter (AUTHORING §6).
      if (node.type === 'text' && typeof node.value === 'string' && SLIDE_MENTION.test(node.value)) {
        state.ctx.diag.warn(state.ctx.file, `the text mentions the course slides ("${SLIDE_MENTION.exec(node.value)![0]}"): state the fact or the convention itself; sources belong in the front matter`, line);
      }
      if (node.type === 'text' && node.position) {
        const raw = source.slice(node.position.start.offset, node.position.end.offset);
        if (/(?<!\\)\\\(/.test(raw)) {
          state.ctx.diag.error(state.ctx.file, 'use $...$ for inline math (\\( ... \\) is not supported)', line);
        } else if (/(?<!\\)\\\[/.test(raw)) {
          state.ctx.diag.warn(state.ctx.file, 'found "\\[": use $$...$$ for display math (\\[ ... \\] is not supported)', line);
        }
      }
    });
    checkPageHeadings(state, headings);
  };
}

const SLIDE_MENTION = /\b(?:course|lecture) slides?\b|\bthe slides\b|\bslides of the course\b|课件/i;

/** The text of a node that contains Han characters (prose, math, code, image alt), or null. */
function hanText(node: { type: string; value?: unknown; alt?: unknown }): string | null {
  const text = node.type === 'image' ? node.alt : /^(text|inlineMath|math|inlineCode|code)$/.test(node.type) ? node.value : null;
  return typeof text === 'string' && /\p{Script=Han}/u.test(text) ? text : null;
}

function truncateText(s: string, n: number): string {
  const t = s.replace(/\s+/g, ' ').trim();
  return t.length > n ? `${t.slice(0, n)}…` : t;
}

/** Upper pages (discipline, course) are overviews without headings; chapter pages follow the numbering rules. */
function checkPageHeadings(state: State, headings: HeadingInput[]) {
  const { ctx } = state;
  const role = pageRole(ctx.page.id);
  if (role === 'discipline' || role === 'course') {
    for (const h of headings) {
      ctx.diag.error(ctx.file, `"${h.text}": ${role} pages are overviews without headings; put sectioned content into a chapter page`, h.line);
    }
    return;
  }
  if (role !== 'chapter') return; // depth errors are reported by scan.ts
  for (const p of checkHeadings(headings, numberPrefix(ctx.page.id))) ctx.diag.error(ctx.file, p.message, p.line);
  for (const p of checkEndSections(headings, ctx.contentLang === 'en' ? 'en' : 'zh')) ctx.diag.warn(ctx.file, `${p.message} (CONTENT_GUIDE §3)`, p.line);
}

/* ------------------------------------------------------------------- rehype */

function rehypeWiki(state: State) {
  const { ctx, out } = state;
  return (tree: HastRoot) => {
    const slugger = new GithubSlugger();
    let excerptDone = false;

    visit(tree, 'element', (node, index, parent) => {
      const line = lineOf(state, node);
      const tag = node.tagName;

      if (typeof node.properties?.id === 'string') out.anchors.add(node.properties.id);

      if (tag === 'h1') {
        ctx.diag.error(ctx.file, 'do not use <h1>; the page title is the H1', line);
      }

      if (/^h[2-6]$/.test(tag)) {
        let id: string | undefined;
        const last = node.children.at(-1);
        if (last?.type === 'text') {
          const m = CUSTOM_ID_RE.exec(last.value);
          if (m) {
            id = m[1];
            last.value = last.value.slice(0, m.index);
            slugger.slug(id); // reserve it so generated slugs do not collide
          }
        }
        const label = hastToString(node).trim();
        const numbered = parseHeadingNumber(label);
        if (!id && numbered.number && numbered.wellFormed) {
          id = sectionAnchor(numbered.number);
          slugger.slug(id);
        }
        id ??= slugger.slug(label) || `section-${out.anchors.size + 1}`;
        if (out.anchors.has(id)) ctx.diag.error(ctx.file, `duplicate heading id "${id}"`, line);
        node.properties = { ...node.properties, id };
        out.anchors.add(id);
        if (tag === 'h2' || tag === 'h3') out.headings.push({ id, text: label, depth: tag === 'h2' ? 2 : 3 });
        node.children.push(el('a', { className: ['heading-anchor'], href: `#${id}`, ariaHidden: 'true', tabIndex: -1 }, [text('#')]));
        return undefined;
      }

      if (tag === 'pre') {
        const code = node.children.find((c): c is Element => c.type === 'element' && c.tagName === 'code');
        if (code && hasClass(code, 'language-mermaid') && parent && index !== undefined) {
          parent.children[index] = el('div', { className: ['wiki-mermaid'] }, [
            el('pre', { className: ['wiki-mermaid-source'] }, [text(hastToString(code))]),
          ]);
          return 'skip';
        }
        return 'skip';
      }

      if (tag === 'p' && !excerptDone) {
        const t = plainText(node).trim();
        if (t) {
          out.excerpt = t;
          excerptDone = true;
        }
      }

      if (tag === 'img') return transformImage(state, node, parent, line);
      if (tag === 'a') transformLink(state, node, line);

      if (tag === 'table' && parent && index !== undefined && !(parent.type === 'element' && hasClass(parent, 'table-wrap'))) {
        parent.children[index] = el('div', { className: ['table-wrap'] }, [node]);
      }
      return undefined;
    });

    out.text = plainText(tree).replace(/\s+/g, ' ').trim();
  };
}

const STATEMENT_GROUP: Record<StatementKind, string> = {
  def: 'def',
  thm: 'thm',
  lem: 'thm',
  prop: 'thm',
  cor: 'thm',
  pty: 'note',
  ex: 'ex',
  rem: 'note',
  alg: 'note',
  fml: 'note',
};

function isWhitespace(n: RootContent | ElementContent): boolean {
  return n.type === 'text' && !n.value.trim();
}

function isDisplayMath(n: RootContent | ElementContent): boolean {
  return n.type === 'element' && n.tagName === 'pre' && n.children.some((c) => c.type === 'element' && hasClass(c, 'math-display'));
}

/** Leading bold run of a paragraph, if the paragraph starts with one. */
function leadingStrong(p: Element): Element | undefined {
  const first = p.children.find((c) => !isWhitespace(c));
  return first?.type === 'element' && first.tagName === 'strong' ? first : undefined;
}

/**
 * Statements: a paragraph that starts with **定理 13.2.1（名称）** gets a language-neutral anchor
 * (thm-13.2.1). At the top level it is wrapped together with the display math, lists and tables
 * that directly follow it into <div class="wiki-stmt …">, which is also what previews show.
 * Display math with \tag{X} gets the anchor eq-X.
 */
/** ```smiles blocks: structures drawn by RDKit at build time (chem.ts), kept as pre-serialized SVG. */
const ANSWER_SUMMARY = { zh: '答案', en: 'Answer' } as const;
// Answer openers that are not the canonical **答** / **Answer** paragraph.
const LOOSE_ANSWER_RE = /^\s*(答案?|简答|解答?|Answers?|Solution)\s*[:：]/;
const LOOSE_ANSWER_WORD = /^(答案?|简答|解答?|Answers?|Solution)[:：.]?$/;

/**
 * "## 思考题" / "## Questions" is one numbered list; every item is a question followed by its answer:
 * the paragraph that starts with **答** / **Answer** and everything after it in the item, folded into
 * <details class="wiki-answer">.
 */
function rehypeQuestions(state: State) {
  const { ctx } = state;
  const lang = ctx.contentLang === 'en' ? 'en' : 'zh';
  return (tree: HastRoot) => {
    let inQuestions = false;
    for (const node of tree.children) {
      if (node.type !== 'element') continue;
      if (node.tagName === 'h2') {
        // rehypeWiki has appended the "#" heading anchor
        const title = node.children.filter((c) => !(c.type === 'element' && hasClass(c, 'heading-anchor')));
        inQuestions = endSection(title.map((c) => hastToString(c)).join('')) === 'questions';
        continue;
      }
      if (!inQuestions) continue;
      // Each question is an item of one numbered list; anything else here has lost its indentation.
      if (node.tagName !== 'ol') {
        ctx.diag.warn(ctx.file, 'write the questions as one numbered list; indent formulas, sub-items and answers under their question (CONTENT_GUIDE §3)', lineOf(state, node));
        continue;
      }
      for (const li of node.children) {
        if (li.type === 'element' && li.tagName === 'li') foldAnswer(state, li, lang);
      }
    }
  };
}

function foldAnswer(state: State, li: Element, lang: 'zh' | 'en') {
  const { ctx } = state;
  const line = lineOf(state, li);
  const isLabel = (n: ElementContent | undefined): n is Element =>
    n?.type === 'element' && n.tagName === 'strong' && hastToString(n).trim() === ANSWER_LABEL[lang];
  const at = li.children.findIndex((c) => {
    if (c.type !== 'element' || c.tagName !== 'p') return false;
    const first = c.children.find((k) => !(k.type === 'text' && !k.value.trim()));
    return isLabel(first);
  });
  if (at < 0) {
    // Answers written some other way: own-line "答：", a **解** label, or **答** inside the question paragraph.
    for (const c of li.children) {
      if (c.type === 'element' && (c.tagName === 'ol' || c.tagName === 'ul')) continue;
      const loose = c.type === 'text' ? LOOSE_ANSWER_RE.test(c.value) : c.type === 'element' && c.tagName === 'p' && LOOSE_ANSWER_RE.test(hastToString(c));
      let label = false;
      if (c.type === 'element') {
        visit(c, 'element', (s) => {
          if (s.tagName === 'strong' && (isLabel(s) || LOOSE_ANSWER_WORD.test(hastToString(s).trim()))) label = true;
        });
      }
      if (loose || label) {
        ctx.diag.warn(ctx.file, `write an answer as its own paragraph starting with **${ANSWER_LABEL[lang]}**, indented under the question (CONTENT_GUIDE §3)`, line);
        return;
      }
    }
    ctx.diag.warn(ctx.file, `question without an answer: add a paragraph starting with **${ANSWER_LABEL[lang]}** under it (CONTENT_GUIDE §3)`, line);
    return;
  }
  const question = li.children.slice(0, at);
  if (!question.some((c) => hastToString(c as Element).trim())) {
    ctx.diag.warn(ctx.file, `answer without a question: write the question first, then the **${ANSWER_LABEL[lang]}** paragraph (CONTENT_GUIDE §3)`, line);
  }
  const p = li.children[at] as Element;
  const labelIndex = p.children.findIndex((k) => isLabel(k));
  p.children.splice(0, labelIndex + 1);
  const head = p.children[0];
  if (head?.type === 'text') head.value = head.value.replace(/^\s*[:：]?\s*/, '');
  if (!p.children.length) li.children.splice(at, 1);
  const details = el('details', { className: ['wiki-answer'] }, [el('summary', {}, [text(ANSWER_SUMMARY[lang])]), ...li.children.slice(at)]);
  li.children = [...question, details];
}

function rehypeChem(state: State) {
  return async (tree: HastRoot) => {
    const jobs: Promise<void>[] = [];
    visit(tree, 'element', (node, index, parent) => {
      if (node.tagName !== 'pre' || !parent || index === undefined) return undefined;
      const code = node.children.find((c): c is Element => c.type === 'element' && c.tagName === 'code');
      if (!code || !hasClass(code, 'language-smiles')) return 'skip';
      const line = lineOf(state, node);
      const lines = parseChemBlock(hastToString(code));
      const block = el('div', { className: ['wiki-chem'] });
      parent.children[index] = block;
      if (!lines.length) state.ctx.diag.warn(state.ctx.file, 'empty smiles block', line);
      jobs.push(
        Promise.all(
          lines.map(async (l) => {
            if (l.label && /\p{Script=Han}/u.test(l.label)) {
              state.ctx.diag.warn(state.ctx.file, `structure label "${l.label}" must be language-neutral (both languages share the drawing)`, line);
            }
            const svg = await drawStructure(l);
            if (!svg) {
              state.ctx.diag.error(state.ctx.file, `RDKit cannot parse the ${l.reaction ? 'reaction ' : ''}SMILES "${l.smiles}"`, line);
              return undefined;
            }
            const raw = { type: 'raw', value: svg } as unknown as ElementContent;
            if (!l.label) return el('div', { className: ['wiki-chem-item'] }, [raw]);
            // Labels are formulas, ion charges or compound numbers: typeset them with mhchem (NO3- → NO₃⁻).
            const label = { type: 'raw', value: katex.renderToString(`\\ce{${l.label}}`, { output: 'html', throwOnError: false, strict: 'ignore' }) } as unknown as ElementContent;
            return el('div', { className: ['wiki-chem-item'] }, [raw, el('span', { className: ['wiki-chem-label'] }, [label])]);
          }),
        ).then((items) => {
          block.children = items.filter((i): i is Element => i !== undefined);
        }),
      );
      return 'skip';
    });
    await Promise.all(jobs);
  };
}

function rehypeStatements(state: State) {
  const { ctx, out } = state;
  return (tree: HastRoot) => {
    const prefix = pageRole(ctx.page.id) === 'chapter' ? numberPrefix(ctx.page.id) : null;
    const seen = new Set<string>();

    const register = (p: Element): Element | null => {
      const strong = leadingStrong(p);
      if (!strong) return null;
      const label = parseStatementLabel(hastToString(strong));
      if (!label) return null;
      const line = lineOf(state, p);
      const lang = ctx.contentLang;
      if (!label.canonical) {
        ctx.diag.warn(ctx.file, `write the label as **${formatStatementLabel(label, lang)}** (\`pnpm wiki fix\` does this)`, line);
      }
      if (!label.number) return null;
      const number = label.number.join('.');
      if (prefix && (label.number.length <= prefix.length || label.number.slice(0, prefix.length).join('.') !== prefix.join('.'))) {
        ctx.diag.error(ctx.file, `${label.word} ${number}: numbers on this page start with ${prefix.join('.')}. (e.g. ${prefix.join('.')}.1.1)`, line);
        return null;
      }
      const anchor = statementAnchor(label.kind, label.number);
      if (seen.has(anchor)) {
        ctx.diag.error(ctx.file, `${label.word} ${number} is numbered twice on this page`, line);
        return null;
      }
      seen.add(anchor);
      out.anchors.add(anchor);
      out.statements.push({ kind: label.kind, number, name: label.name, anchor, line });
      strong.properties = { ...strong.properties, className: ['wiki-stmt-label'] };
      return el('div', { className: ['wiki-stmt', `wiki-stmt-${STATEMENT_GROUP[label.kind]}`], id: anchor, dataKind: label.kind }, []);
    };

    // Top-level statements: wrap the label paragraph and what belongs to it.
    const children = tree.children;
    for (let i = 0; i < children.length; i++) {
      const node = children[i];
      if (node.type !== 'element' || node.tagName !== 'p') continue;
      const wrapper = register(node);
      if (!wrapper) continue;
      let end = i + 1;
      let last = i;
      while (end < children.length) {
        const c = children[end];
        if (isWhitespace(c)) {
          end++;
          continue;
        }
        if (c.type === 'element' && (isDisplayMath(c) || /^(ul|ol)$/.test(c.tagName) || hasClass(c, 'table-wrap'))) {
          last = end++;
          continue;
        }
        // A paragraph written directly under display math (no blank line) continues the statement:
        //   $$ … $$
        //   则称 λ 为 A 的特征值。
        const prev = children[last];
        if (c.type === 'element' && c.tagName === 'p' && isDisplayMath(prev) && !leadingStrong(c) && prev.position && c.position && c.position.start.line === prev.position.end.line + 1) {
          last = end++;
          continue;
        }
        break;
      }
      wrapper.children = children.slice(i, last + 1) as ElementContent[];
      children.splice(i, last - i + 1, wrapper);
    }

    // Statements inside lists/quotes: anchor the paragraph itself. Equations: anchor by \tag.
    visit(tree, 'element', (node, index, parent) => {
      // A paragraph in a list/quote, or a tight list item (whose text has no <p> around it).
      const inWrapper = parent?.type === 'element' && hasClass(parent, 'wiki-stmt');
      if ((node.tagName === 'p' && parent?.type === 'element' && !inWrapper) || (node.tagName === 'li' && !node.children.some((c) => c.type === 'element' && c.tagName === 'p'))) {
        const wrapper = register(node);
        if (wrapper) node.properties = { ...node.properties, id: wrapper.properties.id, className: ['wiki-stmt-inline'] };
        return undefined;
      }
      if (isDisplayMath(node) && parent && index !== undefined) {
        const tag = /\\tag\*?\{([^}]+)\}/.exec(hastToString(node))?.[1]?.trim();
        if (!tag) return 'skip';
        const anchor = equationAnchor(tag);
        if (out.anchors.has(anchor)) ctx.diag.error(ctx.file, `equation tag (${tag}) is used twice on this page`, lineOf(state, node));
        out.anchors.add(anchor);
        out.statements.push({ kind: 'eq', number: tag, anchor, line: lineOf(state, node) });
        parent.children[index] = el('div', { className: ['wiki-eq'], id: anchor }, [node]);
        return 'skip';
      }
      return undefined;
    });

    // A numbered label in the middle of a paragraph was meant to start a new statement.
    visit(tree, 'element', (node) => {
      if (node.tagName !== 'strong' || hasClass(node, 'wiki-stmt-label')) return;
      const label = parseStatementLabel(hastToString(node));
      if (!label?.number) return;
      // A bold mention of a statement that exists on this page is just an emphasised reference.
      if (out.anchors.has(statementAnchor(label.kind, label.number))) return;
      node.properties = { ...node.properties, className: ['wiki-label-text'] };
      ctx.diag.warn(ctx.file, `**${hastToString(node)}** is in the middle of a paragraph; start a new paragraph for it so it becomes a numbered statement`, lineOf(state, node));
    });
  };
}

/** Text content without code blocks, math and diagram sources. */
function plainText(node: HastRoot | Element): string {
  let s = '';
  visit(node, (n) => {
    if (n.type === 'element') {
      if (n.tagName === 'pre' || hasClass(n, 'math-inline') || hasClass(n, 'math-display') || hasClass(n, 'heading-anchor')) {
        return 'skip';
      }
      if (/^(p|li|h[2-6]|td|th|br|div|figcaption)$/.test(n.tagName)) s += ' ';
    }
    if (n.type === 'text') s += n.value;
    return undefined;
  });
  return s;
}

function stripDotSlash(src: string): string {
  return src.replace(/^\.\//, '');
}

function transformImage(state: State, node: Element, parent: HastRoot | Element | undefined, line?: number) {
  const { ctx } = state;
  const src = String(node.properties?.src ?? '');
  const alt = String(node.properties?.alt ?? '');
  const standalone =
    parent?.type === 'element' &&
    parent.tagName === 'p' &&
    parent.children.every((c) => c === node || (c.type === 'text' && !c.value.trim()));

  if (/^https?:\/\//.test(src)) {
    node.properties = { ...node.properties, loading: 'lazy', decoding: 'async' };
    return undefined;
  }

  const local = stripDotSlash(src);
  if (local.startsWith('plots/') && local.endsWith('.py')) {
    const script = path.join(ctx.page.dir, local);
    ctx.usedPlots.add(script);
    if (!standalone) {
      ctx.diag.error(ctx.file, `plot ${src} must be a paragraph of its own: put a blank line before and after it`, line);
      return undefined;
    }
    const result = ctx.plots.get(script);
    if (!result) {
      ctx.diag.error(ctx.file, `plot script not found: ${src} (expected ${path.join(path.basename(ctx.page.dir), local)})`, line);
      return undefined;
    }
    return replaceParagraph(plotFigure(path.basename(script), alt, result, state.ctx.contentLang));
  }

  if (local.startsWith('assets/')) {
    const name = local.slice('assets/'.length);
    if (!state.ctx.page.assets.includes(name)) {
      ctx.diag.error(ctx.file, `image not found: ${src} (put the file in ${path.basename(ctx.page.dir)}/assets/)`, line);
      return undefined;
    }
    ctx.usedAssets.add(name);
    node.properties = { ...node.properties, src: `${MEDIA_ROOT}/${ctx.page.id}/${encodeURIComponent(name)}`, loading: 'lazy', decoding: 'async' };
    if (!alt.trim()) ctx.diag.warn(ctx.file, `image ${src} has no alt text (write a caption: ![caption](${src}))`, line);
    if (standalone && alt.trim()) {
      return replaceParagraph(el('figure', { className: ['wiki-figure'] }, [{ ...node }, el('figcaption', {}, [text(alt)])]));
    }
    return undefined;
  }

  ctx.diag.error(ctx.file, `unsupported image source "${src}": use ./assets/<file> for images or ./plots/<script>.py for plots`, line);
  return undefined;

  /**
   * Turn the enclosing <p> (which contains only this image) into `replacement` in place,
   * and tell the visitor to continue after it so the generated nodes are not revisited.
   */
  function replaceParagraph(replacement: Element): number {
    const p = parent as Element;
    p.tagName = replacement.tagName;
    p.properties = replacement.properties;
    p.children = replacement.children;
    return p.children.length;
  }
}

function plotFigure(scriptName: string, alt: string, result: PlotResult, lang: Lang): Element {
  const images: ElementContent[] = [];
  if (result.error || !result.figures.length) {
    images.push(el('div', { className: ['wiki-plot-error'] }, [text(`Plot ${scriptName} could not be rendered. Run "pnpm wiki build" for details.`)]));
  }
  result.figures.forEach((fig, i) => {
    for (const theme of ['light', 'dark'] as const) {
      images.push(
        el('img', {
          className: [`plot-${theme}`],
          src: `${PLOTS_ROOT}/${result.key}/${i}-${theme}.webp`,
          alt: alt || scriptName,
          width: Math.round(fig.width / 2),
          height: Math.round(fig.height / 2),
          loading: 'lazy',
          decoding: 'async',
        }),
      );
    }
  });
  const children: ElementContent[] = [el('div', { className: ['wiki-plot-images'] }, images)];
  if (alt.trim()) children.push(el('figcaption', {}, [text(alt)]));
  // Icons from open libraries (BIO_FIGURES.md §5): CC BY requires naming the author and the licence.
  const credits = iconCredits(result.source);
  if (credits.length) {
    const parts: ElementContent[] = [text(lang === 'zh' ? '图标：' : 'Icons: ')];
    credits.forEach((c, i) => {
      if (i) parts.push(text(lang === 'zh' ? '；' : '; '));
      parts.push(text(`${c.author} (`));
      parts.push(c.url ? el('a', { href: c.url, target: '_blank', rel: ['noopener'] }, [text(c.license)]) : text(c.license));
      parts.push(text(')'));
    });
    if (credits.some((c) => c.license.startsWith('CC BY-SA'))) {
      parts.push(text(lang === 'zh' ? '。本图按 ' : '. This figure is licensed under '));
      parts.push(el('a', { href: SHARE_ALIKE.url, target: '_blank', rel: ['noopener'] }, [text(SHARE_ALIKE.license)]));
      parts.push(text(lang === 'zh' ? ' 发布' : ''));
    }
    children.push(el('p', { className: ['wiki-plot-credit'] }, parts));
  }
  const python = el('pre', {}, [el('code', { className: ['language-python'] }, [text(result.source.trimEnd())])]);
  if (result.rSource === undefined) {
    children.push(el('details', { className: ['wiki-plot-source'] }, [el('summary', {}, [text(`Python · ${scriptName}`)]), python]));
  } else {
    // Python draws the figure; the R companion shows the same analysis in R (Article.tsx switches the tabs).
    const r = el('pre', {}, [el('code', { className: ['language-r'] }, [text(result.rSource.trimEnd())])]);
    children.push(
      el('details', { className: ['wiki-plot-source'] }, [
        el('summary', {}, [text(`Python · R · ${scriptName.replace(/\.py$/, '')}`)]),
        el('div', { className: ['wiki-code-tabs'] }, [
          el('div', { className: ['wiki-code-tablist'], role: 'tablist' }, [
            el('button', { type: 'button', role: 'tab', className: ['active'], dataCodeTab: 'python', ariaSelected: 'true' }, [text('Python')]),
            el('button', { type: 'button', role: 'tab', dataCodeTab: 'r', ariaSelected: 'false' }, [text('R')]),
          ]),
          el('div', { dataCodePanel: 'python' }, [python]),
          el('div', { dataCodePanel: 'r', hidden: true }, [r]),
        ]),
      ]),
    );
  }
  return el('figure', { className: ['wiki-plot'] }, children);
}

function transformLink(state: State, node: Element, line?: number) {
  const { ctx, out } = state;
  const href = String(node.properties?.href ?? '');
  if (!href) return;
  if (href.startsWith('#')) {
    out.localAnchors.push({ anchor: decodeURIComponent(href.slice(1)), line });
    return;
  }
  if (/^(https?:|mailto:)/.test(href)) {
    node.properties = { ...node.properties, target: '_blank', rel: ['noopener', 'noreferrer'] };
    return;
  }
  const internal = INTERNAL_LINK_RE.exec(href);
  if (internal) {
    const [, targetId, anchor] = internal;
    if (!ctx.tree.pages.has(targetId)) {
      ctx.diag.error(ctx.file, `link to unknown page "${targetId}"`, line);
    }
    out.links.push({ targetId, anchor, line });
    node.properties = {
      ...node.properties,
      href: `${BASE_PATH}${ctx.linkLang}/${targetId}/${anchor ? `#${anchor}` : ''}`,
      dataInternal: '',
    };
    return;
  }
  const local = stripDotSlash(href);
  if (local.startsWith('assets/')) {
    const name = local.slice('assets/'.length);
    if (!ctx.page.assets.includes(name)) ctx.diag.error(ctx.file, `linked file not found: ${href}`, line);
    ctx.usedAssets.add(name);
    node.properties = { ...node.properties, href: `${MEDIA_ROOT}/${ctx.page.id}/${encodeURIComponent(name)}` };
    return;
  }
  ctx.diag.error(ctx.file, `unsupported link "${href}": link pages as /<page-id> (e.g. /7.4.1.5 or /7.4.1.5#section), files as ./assets/<file>`, line);
}

/** Tab labels for code languages (others show the fence name). */
const TAB_LABELS: Record<string, string> = { cpp: 'C++', 'c++': 'C++', c: 'C', python: 'Python', py: 'Python', r: 'R', js: 'JavaScript', javascript: 'JavaScript', ts: 'TypeScript', typescript: 'TypeScript', sql: 'SQL', bash: 'Bash', sh: 'Shell', verilog: 'Verilog', systemverilog: 'SystemVerilog', java: 'Java', rust: 'Rust', go: 'Go' };

const codeLang = (pre: Element): string | undefined => {
  const code = pre.children.find((c): c is Element => c.type === 'element' && c.tagName === 'code');
  const cls = (code?.properties?.className as string[] | undefined) ?? [];
  return cls.find((c) => c.startsWith('language-'))?.slice('language-'.length);
};

function codeBlock(pre: Element): Element {
  const lang = codeLang(pre);
  const header: ElementContent[] = [];
  if (lang && lang !== 'math') header.push(el('span', { className: ['code-lang'] }, [text(lang)]));
  header.push(el('button', { type: 'button', className: ['copy-button'], dataCopy: '' }, [text('Copy')]));
  return el('div', { className: ['code-block'] }, [el('div', { className: ['code-block-header'] }, header), pre]);
}

/** After highlighting and KaTeX: code-block chrome, and the tab list of code-tab groups. */
function rehypeFinalize() {
  return (tree: HastRoot) => {
    visit(tree, 'element', (node, index, parent) => {
      if (node.tagName === 'div' && hasClass(node, 'wiki-code-tabs') && node.children.some((c) => c.type === 'element' && c.tagName === 'pre')) {
        const pres = node.children.filter((c): c is Element => c.type === 'element' && c.tagName === 'pre');
        const langs = pres.map((p) => codeLang(p) ?? 'text');
        node.children = [
          el(
            'div',
            { className: ['wiki-code-tablist'], role: 'tablist' },
            langs.map((l, i) => el('button', { type: 'button', role: 'tab', ...(i === 0 ? { className: ['active'] } : {}), dataCodeTab: l, ariaSelected: String(i === 0) }, [text(TAB_LABELS[l] ?? l)])),
          ),
          ...pres.map((p, i) => el('div', { dataCodePanel: langs[i], ...(i ? { hidden: true } : {}) }, [codeBlock(p)])),
        ];
        return 'skip';
      }
      if (node.tagName === 'pre' && parent && index !== undefined && !(parent.type === 'element' && hasClass(parent, 'wiki-mermaid'))) {
        (parent.children as RootContent[])[index] = codeBlock(node);
        return 'skip';
      }
      // KaTeX output is final and linking skips it, but its element trees dominate the memory the build
      // holds for all pages at once; keep each formula as one pre-serialized node instead.
      if ((hasClass(node, 'katex-display') || hasClass(node, 'katex')) && parent && index !== undefined) {
        (parent.children as RootContent[])[index] = { type: 'raw', value: toHtml(node) };
        return 'skip';
      }
      return undefined;
    });
  };
}

/* -------------------------------------------------------------------- entry */

export async function renderMarkdown(body: string, ctx: RenderContext): Promise<RenderOutput> {
  const out: RenderOutput = {
    hast: { type: 'root', children: [] },
    contentLang: ctx.contentLang,
    statements: [],
    headings: [],
    anchors: new Set(),
    links: [],
    localAnchors: [],
    text: '',
    excerpt: '',
  };
  const state: State = { ctx, out };
  const processor = unified()
    .use(remarkParse)
    .use(remarkGfm)
    .use(remarkMath)
    .use(remarkWikiChecks, state)
    .use(remarkCodeTabs, state)
    .use(remarkRehype, { allowDangerousHtml: true })
    .use(rehypeRaw)
    .use(rehypeWiki, state)
    .use(rehypeQuestions, state)
    .use(rehypeChem, state)
    .use(rehypeStatements, state)
    .use(rehypeHighlight, { languages: { ...common, matlab, latex, verilog, vhdl, tcl, http, protobuf, dockerfile }, aliases: { verilog: ['systemverilog'] }, plainText: ['text', 'txt', 'plain', 'math', 'asm'] })
    .use(rehypeKatex, { strict: 'ignore', output: 'html' })
    .use(rehypeFinalize);

  const file = new VFile({ value: body, path: ctx.file });
  const mdast = processor.parse(file);
  const hast = (await processor.run(mdast, file)) as HastRoot;
  for (const msg of file.messages) {
    const line = msg.line ? msg.line + ctx.lineOffset : undefined;
    if (msg.ruleId === 'missing-language') {
      ctx.diag.warn(ctx.file, `${msg.reason} (no syntax highlighting)`, line);
    } else if (msg.source === 'rehype-katex') {
      const cause = msg.cause instanceof Error ? msg.cause.message : msg.reason;
      ctx.diag.warn(ctx.file, `KaTeX could not render: ${cause.replace(/^KaTeX parse error: /, '')}`, line);
    } else {
      ctx.diag.warn(ctx.file, msg.reason, line);
    }
  }
  for (const { anchor, line } of out.localAnchors) {
    if (!out.anchors.has(anchor)) ctx.diag.error(ctx.file, `link to missing anchor "#${anchor}" on this page`, line);
  }
  out.hast = hast;
  return out;
}

export function emptyRender(contentLang: Lang): RenderOutput {
  return {
    hast: { type: 'root', children: [] },
    contentLang,
    statements: [],
    headings: [],
    anchors: new Set(),
    links: [],
    localAnchors: [],
    text: '',
    excerpt: '',
  };
}

export function renderHtml(out: RenderOutput): string {
  return out.hast.children.length ? toHtml(out.hast, { allowDangerousHtml: true }) : '';
}
