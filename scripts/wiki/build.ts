/**
 * Content build: content/ -> .generated/
 *
 *   .generated/site.json                         SiteData (navigation tree), also served to the client
 *   .generated/public/                           Vite publicDir (served at the site base URL)
 *     data/pages/<lang>/<id>.json                PagePayload per page and language
 *     data/search/<lang>.json                    SearchEntry[] per language
 *     data/concepts.json                         ConceptEntry[] (both languages)
 *     media/<id>/<file>                          files from content/<page>/assets/
 *     plots/<key>/<i>-<light|dark>.webp          rendered plots
 *     (everything in public/)
 */
import crypto from 'node:crypto';
import fs from 'node:fs';
import path from 'node:path';
import { LANGUAGES, type Lang } from '../../site.config.ts';
import type { ConceptEntry, NavNode, PagePayload, SearchEntry, SiteData, TranslationStatus } from '../../src/shared/types.ts';
import { Diagnostics } from './diagnostics.ts';
import { acquireBuildLock } from './lock.ts';
import { loadConcepts } from './glossary.ts';
import { type LinkResult, buildLinkIndex, linkPage } from './linking.ts';
import { type RenderOutput, emptyRender, renderHtml, renderMarkdown } from './markdown.ts';
import { GENERATED_DIR, GENERATED_PUBLIC_DIR, GLOSSARY_FILE, PUBLIC_DIR, PUBLIC_PATHS, SITE_DATA_FILE, rel } from './paths.ts';
import { type PlotResults, plotImagePath, renderPlots } from './plots.ts';
import { type ContentTree, type PageSource, ancestorsOf, scanContent } from './scan.ts';

export interface BuildOptions {
  /** Dev builds attach per-page diagnostics to payloads so they show up in the browser. */
  dev?: boolean;
  /** Skip writing .generated/ (used by checks that only need diagnostics). */
  dryRun?: boolean;
  log?: (message: string) => void;
  /**
   * Render and link only these pages (`pnpm wiki lint`): fast, no output written, no build lock.
   * Checks that need the whole site (definition sites in other courses) are left to full builds.
   */
  only?: Set<string>;
}

export interface BuildResult {
  diag: Diagnostics;
  tree: ContentTree;
  site: SiteData;
  /** Keyed by `${lang}/${id}`. */
  payloads: Map<string, PagePayload>;
  concepts: ConceptEntry[];
  /** Concepts mentioned on a page that comes before their definition in reading order. */
  forwardUses: { pageId: string; conceptId: string }[];
  /** Per `${lang}/${pageId}` (own-language renders only): bold runs that are neither a concept nor a label. */
  plainBold: Map<string, LinkResult['plainBold']>;
}

/** Hash of a source-language body; a translation is up to date when its `source_hash` equals this. */
export function sourceHash(body: string): string {
  const normalized = body.replace(/\r\n?/g, '\n').replace(/[ \t]+$/gm, '').trim();
  return crypto.createHash('sha256').update(normalized).digest('hex').slice(0, 12);
}

export function translationStatus(page: PageSource, lang: Lang): TranslationStatus {
  const src = page.sourceLang;
  const source = page.files[src]?.body.trim() ?? '';
  const own = page.files[lang]?.body.trim() ?? '';
  if (lang === src) return source ? 'source' : 'empty';
  if (!own) return source ? 'untranslated' : 'empty';
  return page.files[lang]?.frontMatter.source_hash === sourceHash(page.files[src]!.body) ? 'translated' : 'stale';
}

function titleOf(page: PageSource, lang: Lang): string {
  return page.files[lang]?.frontMatter.title ?? page.files[page.sourceLang]?.frontMatter.title ?? page.slug;
}

export async function buildContent(opts: BuildOptions = {}): Promise<BuildResult> {
  if (opts.only) return buildContentLocked({ ...opts, dryRun: true });
  const release = acquireBuildLock(opts.log ?? console.log);
  try {
    return await buildContentLocked(opts);
  } finally {
    release();
  }
}

async function buildContentLocked(opts: BuildOptions): Promise<BuildResult> {
  const log = opts.log ?? (() => {});
  const diag = new Diagnostics();
  const tree = scanContent(diag);
  const plots = await renderPlots(tree, diag, { log, pages: opts.only });
  const included = (id: string) => !opts.only || opts.only.has(id);

  const rendered = new Map<string, RenderOutput>();
  const renderDiag = new Map<string, Diagnostics>();
  const usedPlots = new Set<string>();
  const usedAssets = new Map<string, Set<string>>();

  // 1. render every page in every language
  for (const page of tree.pages.values()) {
    if (!included(page.id)) continue;
    usedAssets.set(page.id, new Set());
    for (const lang of LANGUAGES) {
      const status = translationStatus(page, lang);
      // Untranslated pages show the source text, with links pointing at the reader's language.
      const contentLang = status === 'untranslated' ? page.sourceLang : lang;
      const file = page.files[contentLang];
      // The fallback render repeats the source render, so its diagnostics would be duplicates.
      const pageDiag = contentLang === lang ? diag : new Diagnostics();
      renderDiag.set(`${lang}/${page.id}`, pageDiag);
      const ctx = {
        page,
        tree,
        plots,
        diag: pageDiag,
        file: file?.path ?? path.join(page.dir, `index.${contentLang}.md`),
        lineOffset: file?.bodyLineOffset ?? 0,
        linkLang: lang,
        contentLang,
        usedPlots,
        usedAssets: usedAssets.get(page.id)!,
      };
      const out = file && file.body.trim() ? await renderMarkdown(file.body, ctx) : emptyRender(contentLang);
      rendered.set(`${lang}/${page.id}`, out);
    }
  }

  // 2. index statements and concept definitions across the site, 3. link every page
  const fullOrder = tree.rootIds.flatMap(function walk(id: string): string[] {
    return [id, ...tree.pages.get(id)!.childIds.flatMap(walk)];
  });
  const readingOrder = fullOrder.filter(included);
  const order = new Map(readingOrder.map((id, i) => [id, i]));
  const concepts = loadConcepts(diag);
  for (const c of concepts) {
    for (const s of opts.only ? [] : (c.scope ?? [])) if (!tree.pages.has(s)) diag.error(GLOSSARY_FILE, `"${c.en}": scope "${s}" is not a page id`);
  }
  const sourceKey = (id: string) => `${tree.pages.get(id)!.sourceLang}/${id}`;
  const sourceRenders = new Map(readingOrder.map((id) => [id, rendered.get(sourceKey(id))!]));
  const sourceFiles = new Map(readingOrder.map((id) => [id, tree.pages.get(id)!.files[tree.pages.get(id)!.sourceLang]?.path ?? tree.pages.get(id)!.dir]));
  const index = buildLinkIndex(tree, sourceRenders, sourceFiles, concepts, readingOrder, diag);
  const links = new Map<string, LinkResult>();
  for (const [key, out] of rendered) {
    const [lang, pageId] = key.split('/') as [Lang, string];
    const page = tree.pages.get(pageId)!;
    const file = page.files[out.contentLang]?.path ?? page.dir;
    links.set(key, linkPage({ pageId, out, linkLang: lang, tree, index, readingOrder: order, diag: renderDiag.get(key)!, file }));
  }

  // backlinks come from the source language (translations mirror its structure)
  const backlinks = new Map<string, Set<string>>();
  for (const id of readingOrder) {
    for (const target of links.get(sourceKey(id))!.targets) backlinks.set(target, (backlinks.get(target) ?? new Set()).add(id));
  }

  const payloads = new Map<string, PagePayload>();
  for (const [key, out] of rendered) {
    const [lang, pageId] = key.split('/') as [Lang, string];
    const page = tree.pages.get(pageId)!;
    payloads.set(key, {
      id: pageId,
      lang,
      title: titleOf(page, lang),
      status: translationStatus(page, lang),
      contentLang: out.contentLang,
      html: renderHtml(out),
      headings: out.headings,
      description: page.files[lang]?.frontMatter.description ?? truncate(out.excerpt, 160),
      ...(page.files[page.sourceLang]?.frontMatter.courses ? { courses: page.files[page.sourceLang]!.frontMatter.courses } : {}),
      ...(page.files[page.sourceLang]?.frontMatter.textbooks ? { textbooks: page.files[page.sourceLang]!.frontMatter.textbooks } : {}),
      backlinks: [...(backlinks.get(pageId) ?? [])].sort((a, b) => (order.get(a) ?? 0) - (order.get(b) ?? 0)),
      concepts: [...links.get(key)!.concepts],
    });
  }

  const usedIn = new Map<string, string[]>();
  const forwardUses: BuildResult['forwardUses'] = [];
  for (const id of readingOrder) {
    const result = links.get(sourceKey(id))!;
    for (const c of result.concepts) usedIn.set(c, [...(usedIn.get(c) ?? []), id]);
    for (const c of result.forwardUses) forwardUses.push({ pageId: id, conceptId: c });
  }
  const conceptEntries: ConceptEntry[] = concepts.map((c) => ({
    id: c.id,
    zh: c.zh,
    en: c.en,
    site: index.conceptSites.get(c.id),
    usedIn: usedIn.get(c.id) ?? [],
  }));

  checkCrossPageAnchors(tree, rendered, diag);
  // Concept links in every language point at the definition site; a translation must keep it.
  for (const [id, site] of index.conceptSites) {
    for (const lang of LANGUAGES) {
      const out = rendered.get(`${lang}/${site.pageId}`);
      if (!out || out.contentLang !== lang || out.anchors.has(site.anchor) || !site.anchor.startsWith('concept-')) continue;
      const page = tree.pages.get(site.pageId)!;
      diag.warn(page.files[lang]?.path ?? page.dir, `the definition of concept "${id}" is not marked in this translation (italicise *term* in English, or write 名称（English） in Chinese, at the defining occurrence)`);
    }
  }
  checkUnused(tree, plots, usedPlots, usedAssets, diag);

  const site: SiteData = {
    buildId: '',
    nav: (opts.only ? [] : tree.rootIds).map((id) => navNode(tree, id)),
  };
  site.buildId = crypto
    .createHash('sha256')
    .update(JSON.stringify(site.nav))
    .update(JSON.stringify([...payloads.values()].map((p) => p.html)))
    .update(JSON.stringify(conceptEntries))
    .digest('hex')
    .slice(0, 12);

  if (opts.dev) {
    for (const payload of payloads.values()) {
      const dir = rel(tree.pages.get(payload.id)!.dir) + '/';
      const own = diag.items.filter((d) => d.file.startsWith(dir) && isOwnDiagnostic(d.file, dir));
      if (own.length) payload.diagnostics = own;
    }
  }

  if (!opts.dryRun) writeOutputs(tree, plots, site, payloads, rendered, conceptEntries);
  const plainBold = new Map([...links].filter(([key]) => rendered.get(key)!.contentLang === key.split('/')[0]).map(([key, r]) => [key, r.plainBold]));
  return { diag, tree, site, payloads, concepts: conceptEntries, forwardUses, plainBold };
}

/** A diagnostic belongs to a page if it is in the page's own files (not in a child page's directory). */
function isOwnDiagnostic(file: string, dir: string): boolean {
  const rest = file.slice(dir.length);
  return /^(index\.[a-z]+\.md|assets\/[^/]+|plots\/[^/]+)?$/.test(rest);
}

function truncate(s: string, n: number): string {
  const t = s.replace(/\s+/g, ' ').trim();
  return t.length > n ? `${t.slice(0, n - 1)}…` : t;
}

function navNode(tree: ContentTree, id: string): NavNode {
  const page = tree.pages.get(id)!;
  const title = {} as Record<Lang, string>;
  const status = {} as Record<Lang, TranslationStatus>;
  for (const lang of LANGUAGES) {
    title[lang] = titleOf(page, lang);
    status[lang] = translationStatus(page, lang);
  }
  return { id, title, status, children: page.childIds.map((c) => navNode(tree, c)) };
}

function checkCrossPageAnchors(tree: ContentTree, rendered: Map<string, RenderOutput>, diag: Diagnostics): void {
  for (const page of tree.pages.values()) {
    if (!rendered.has(`${LANGUAGES[0]}/${page.id}`)) continue;
    for (const lang of LANGUAGES) {
      if (translationStatus(page, lang) === 'untranslated') continue; // reported for the source file
      const out = rendered.get(`${lang}/${page.id}`)!;
      const file = page.files[lang]?.path ?? page.dir;
      for (const link of out.links) {
        if (!link.anchor || !tree.pages.has(link.targetId)) continue;
        const target = rendered.get(`${lang}/${link.targetId}`);
        if (target && !target.anchors.has(decodeURIComponent(link.anchor))) {
          diag.error(file, `link to missing anchor "/${link.targetId}#${link.anchor}" (in the ${lang} version of ${link.targetId})`, link.line);
        }
      }
    }
  }
}

function checkUnused(
  tree: ContentTree,
  plots: PlotResults,
  usedPlots: Set<string>,
  usedAssets: Map<string, Set<string>>,
  diag: Diagnostics,
): void {
  for (const script of plots.keys()) {
    if (!usedPlots.has(script)) diag.warn(script, 'plot script is not referenced by any page (embed it with ![caption](./plots/<name>.py) or delete it)');
  }
  for (const page of tree.pages.values()) {
    if (!usedAssets.has(page.id)) continue;
    for (const name of page.assets) {
      if (!usedAssets.get(page.id)!.has(name)) diag.warn(path.join(page.dir, 'assets', name), 'asset is not referenced by the page');
    }
  }
}

function writeJson(file: string, data: unknown): void {
  fs.mkdirSync(path.dirname(file), { recursive: true });
  fs.writeFileSync(file, JSON.stringify(data));
}

function writeOutputs(
  tree: ContentTree,
  plots: PlotResults,
  site: SiteData,
  payloads: Map<string, PagePayload>,
  rendered: Map<string, RenderOutput>,
  concepts: ConceptEntry[],
): void {
  // Build into a sibling directory and swap, so a running dev server never sees a half-written tree.
  const tmp = `${GENERATED_PUBLIC_DIR}.tmp-${process.pid}`;
  fs.rmSync(tmp, { recursive: true, force: true });
  fs.mkdirSync(tmp, { recursive: true });
  if (fs.existsSync(PUBLIC_DIR)) fs.cpSync(PUBLIC_DIR, tmp, { recursive: true });

  for (const [key, payload] of payloads) writeJson(path.join(tmp, PUBLIC_PATHS.pages, `${key}.json`), payload);

  for (const lang of LANGUAGES) {
    const entries: SearchEntry[] = [];
    for (const page of tree.pages.values()) {
      const payload = payloads.get(`${lang}/${page.id}`)!;
      const out = rendered.get(`${lang}/${page.id}`)!;
      entries.push({
        id: page.id,
        title: payload.title,
        trail: ancestorsOf(tree, page.id).map((a) => titleOf(a, lang)).join(' / '),
        headings: out.headings.map((h) => h.text),
        text: out.text,
      });
    }
    writeJson(path.join(tmp, PUBLIC_PATHS.search, `${lang}.json`), entries);
  }

  writeJson(path.join(tmp, PUBLIC_PATHS.concepts), concepts);

  for (const page of tree.pages.values()) {
    for (const name of page.assets) {
      const dest = path.join(tmp, PUBLIC_PATHS.media, page.id, name);
      fs.mkdirSync(path.dirname(dest), { recursive: true });
      fs.copyFileSync(path.join(page.dir, 'assets', name), dest);
    }
  }

  for (const result of plots.values()) {
    if (result.error) continue;
    const dest = path.join(tmp, PUBLIC_PATHS.plots, result.key);
    fs.mkdirSync(dest, { recursive: true });
    result.figures.forEach((_, i) => {
      for (const theme of ['light', 'dark'] as const) {
        fs.copyFileSync(plotImagePath(result, i, theme), path.join(dest, `${i}-${theme}.webp`));
      }
    });
  }

  fs.mkdirSync(GENERATED_DIR, { recursive: true });
  const old = `${GENERATED_PUBLIC_DIR}.old-${process.pid}`;
  if (fs.existsSync(GENERATED_PUBLIC_DIR)) fs.renameSync(GENERATED_PUBLIC_DIR, old);
  fs.renameSync(tmp, GENERATED_PUBLIC_DIR);
  fs.rmSync(old, { recursive: true, force: true });
  fs.writeFileSync(SITE_DATA_FILE, JSON.stringify(site));
}
