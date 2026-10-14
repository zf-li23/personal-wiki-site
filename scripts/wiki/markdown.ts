/**
 * Markdown -> HTML for one page in one language. This is the only Markdown
 * parser in the project: the client receives finished HTML and never parses
 * Markdown itself.
 *
 * Pipeline: remark-parse -> gfm -> math -> (checks) -> rehype -> raw HTML ->
 * wiki transforms (ids, links, images, plots, mermaid) -> highlight -> KaTeX ->
 * finalize (code-block chrome, KaTeX error reporting) -> HTML string.
 */
import path from 'node:path';
import GithubSlugger from 'github-slugger';
import type { Element, ElementContent, Root as HastRoot, RootContent } from 'hast';
import { toHtml } from 'hast-util-to-html';
import { toString as hastToString } from 'hast-util-to-string';
import latex from 'highlight.js/lib/languages/latex';
// Registers \ce / \pu (chemistry) on the KaTeX instance rehype-katex uses (versions are pinned equal, see tests).
import 'katex/contrib/mhchem';
import matlab from 'highlight.js/lib/languages/matlab';
import { common } from 'lowlight';
import type { Root as MdastRoot } from 'mdast';
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
import type { Diagnostics } from './diagnostics.ts';
import { PUBLIC_PATHS } from './paths.ts';
import type { PlotResult, PlotResults } from './plots.ts';
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
  /** Collected while rendering: plot scripts and assets referenced by the body. */
  usedPlots: Set<string>;
  usedAssets: Set<string>;
}

export interface PageLink {
  targetId: string;
  anchor?: string;
  line?: number;
}

export interface RenderOutput {
  html: string;
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
function remarkWikiChecks(state: State) {
  return (tree: MdastRoot, file: VFile) => {
    const source = String(file.value);
    visit(tree, (node) => {
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
      if (node.type === 'text' && node.position) {
        const raw = source.slice(node.position.start.offset, node.position.end.offset);
        if (/(?<!\\)\\\(/.test(raw)) {
          state.ctx.diag.error(state.ctx.file, 'use $...$ for inline math (\\( ... \\) is not supported)', line);
        } else if (/(?<!\\)\\\[/.test(raw)) {
          state.ctx.diag.warn(state.ctx.file, 'found "\\[": use $$...$$ for display math (\\[ ... \\] is not supported)', line);
        }
      }
    });
  };
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
    return replaceParagraph(plotFigure(path.basename(script), alt, result));
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

function plotFigure(scriptName: string, alt: string, result: PlotResult): Element {
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
  children.push(
    el('details', { className: ['wiki-plot-source'] }, [
      el('summary', {}, [text(`Python · ${scriptName}`)]),
      el('pre', {}, [el('code', { className: ['language-python'] }, [text(result.source.trimEnd())])]),
    ]),
  );
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

/** After highlighting and KaTeX: code-block chrome. */
function rehypeFinalize() {
  return (tree: HastRoot) => {
    visit(tree, 'element', (node, index, parent) => {
      if (node.tagName === 'pre' && parent && index !== undefined && !(parent.type === 'element' && hasClass(parent, 'wiki-mermaid'))) {
        const code = node.children.find((c): c is Element => c.type === 'element' && c.tagName === 'code');
        const cls = (code?.properties?.className as string[] | undefined) ?? [];
        const lang = cls.find((c) => c.startsWith('language-'))?.slice('language-'.length);
        const header: ElementContent[] = [];
        if (lang && lang !== 'math') header.push(el('span', { className: ['code-lang'] }, [text(lang)]));
        header.push(el('button', { type: 'button', className: ['copy-button'], dataCopy: '' }, [text('Copy')]));
        (parent.children as RootContent[])[index] = el('div', { className: ['code-block'] }, [
          el('div', { className: ['code-block-header'] }, header),
          node,
        ]);
        return 'skip';
      }
      return undefined;
    });
  };
}

/* -------------------------------------------------------------------- entry */

export async function renderMarkdown(body: string, ctx: RenderContext): Promise<RenderOutput> {
  const out: RenderOutput = { html: '', headings: [], anchors: new Set(), links: [], localAnchors: [], text: '', excerpt: '' };
  const state: State = { ctx, out };
  const processor = unified()
    .use(remarkParse)
    .use(remarkGfm)
    .use(remarkMath)
    .use(remarkWikiChecks, state)
    .use(remarkRehype, { allowDangerousHtml: true })
    .use(rehypeRaw)
    .use(rehypeWiki, state)
    .use(rehypeHighlight, { languages: { ...common, matlab, latex }, plainText: ['text', 'txt', 'plain', 'math'] })
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
  out.html = toHtml(hast);
  return out;
}
