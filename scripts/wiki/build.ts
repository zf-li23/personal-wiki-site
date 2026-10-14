/**
 * Content build: content/ -> .generated/
 *
 *   .generated/site.json                         SiteData (navigation tree), also served to the client
 *   .generated/public/                           Vite publicDir (served at the site base URL)
 *     data/pages/<lang>/<id>.json                PagePayload per page and language
 *     data/search/<lang>.json                    SearchEntry[] per language
 *     media/<id>/<file>                          files from content/<page>/assets/
 *     plots/<key>/<i>-<light|dark>.webp          rendered plots
 *     (everything in public/)
 */
import crypto from 'node:crypto';
import fs from 'node:fs';
import path from 'node:path';
import { LANGUAGES, type Lang, siteConfig } from '../../site.config.ts';
import type { NavNode, PagePayload, SearchEntry, SiteData, TranslationStatus } from '../../src/shared/types.ts';
import { Diagnostics } from './diagnostics.ts';
import { type RenderOutput, renderMarkdown } from './markdown.ts';
import { GENERATED_DIR, GENERATED_PUBLIC_DIR, PUBLIC_DIR, PUBLIC_PATHS, SITE_DATA_FILE, rel } from './paths.ts';
import { type PlotResults, plotImagePath, renderPlots } from './plots.ts';
import { type ContentTree, type PageSource, ancestorsOf, scanContent } from './scan.ts';

export interface BuildOptions {
  /** Dev builds attach per-page diagnostics to payloads so they show up in the browser. */
  dev?: boolean;
  /** Skip writing .generated/ (used by checks that only need diagnostics). */
  dryRun?: boolean;
  log?: (message: string) => void;
}

export interface BuildResult {
  diag: Diagnostics;
  tree: ContentTree;
  site: SiteData;
  /** Keyed by `${lang}/${id}`. */
  payloads: Map<string, PagePayload>;
}

const SOURCE = siteConfig.sourceLanguage;

/** Hash of a source-language body; a translation is up to date when its `source_hash` equals this. */
export function sourceHash(body: string): string {
  const normalized = body.replace(/\r\n?/g, '\n').replace(/[ \t]+$/gm, '').trim();
  return crypto.createHash('sha256').update(normalized).digest('hex').slice(0, 12);
}

export function translationStatus(page: PageSource, lang: Lang): TranslationStatus {
  const source = page.files[SOURCE]?.body.trim() ?? '';
  const own = page.files[lang]?.body.trim() ?? '';
  if (lang === SOURCE) return source ? 'source' : 'empty';
  if (!own) return source ? 'untranslated' : 'empty';
  if (!source) return 'translated';
  return page.files[lang]?.frontMatter.source_hash === sourceHash(page.files[SOURCE]!.body) ? 'translated' : 'stale';
}

function titleOf(page: PageSource, lang: Lang): string {
  return page.files[lang]?.frontMatter.title ?? page.files[SOURCE]?.frontMatter.title ?? page.slug;
}

export async function buildContent(opts: BuildOptions = {}): Promise<BuildResult> {
  const log = opts.log ?? (() => {});
  const diag = new Diagnostics();
  const tree = scanContent(diag);
  const plots = await renderPlots(tree, diag, { log });

  const rendered = new Map<string, RenderOutput>();
  const payloads = new Map<string, PagePayload>();
  const usedPlots = new Set<string>();
  const usedAssets = new Map<string, Set<string>>();

  for (const page of tree.pages.values()) {
    usedAssets.set(page.id, new Set());
    for (const lang of LANGUAGES) {
      const status = translationStatus(page, lang);
      // Untranslated pages show the source text, with links pointing at the reader's language.
      const contentLang = status === 'untranslated' ? SOURCE : lang;
      const file = page.files[contentLang];
      const ctx = {
        page,
        tree,
        plots,
        // The fallback render repeats the source render, so its diagnostics would be duplicates.
        diag: contentLang === lang ? diag : new Diagnostics(),
        file: file?.path ?? path.join(page.dir, `index.${contentLang}.md`),
        lineOffset: file?.bodyLineOffset ?? 0,
        linkLang: lang,
        usedPlots,
        usedAssets: usedAssets.get(page.id)!,
      };
      const out = file && file.body.trim() ? await renderMarkdown(file.body, ctx) : emptyRender();
      rendered.set(`${lang}/${page.id}`, out);
      const fmDescription = page.files[lang]?.frontMatter.description;
      payloads.set(`${lang}/${page.id}`, {
        id: page.id,
        lang,
        title: titleOf(page, lang),
        status,
        contentLang,
        html: out.html,
        headings: out.headings,
        description: fmDescription ?? truncate(out.excerpt, 160),
      });
    }
  }

  checkCrossPageAnchors(tree, rendered, diag);
  checkUnused(tree, plots, usedPlots, usedAssets, diag);

  const site: SiteData = {
    buildId: '',
    nav: tree.rootIds.map((id) => navNode(tree, id)),
  };
  site.buildId = crypto
    .createHash('sha256')
    .update(JSON.stringify(site.nav))
    .update(JSON.stringify([...payloads.values()].map((p) => p.html)))
    .digest('hex')
    .slice(0, 12);

  if (opts.dev) {
    for (const payload of payloads.values()) {
      const dir = rel(tree.pages.get(payload.id)!.dir) + '/';
      const own = diag.items.filter((d) => d.file.startsWith(dir) && isOwnDiagnostic(d.file, dir));
      if (own.length) payload.diagnostics = own;
    }
  }

  if (!opts.dryRun) writeOutputs(tree, plots, site, payloads, rendered);
  return { diag, tree, site, payloads };
}

/** A diagnostic belongs to a page if it is in the page's own files (not in a child page's directory). */
function isOwnDiagnostic(file: string, dir: string): boolean {
  const rest = file.slice(dir.length);
  return /^(index\.[a-z]+\.md|assets\/[^/]+|plots\/[^/]+)?$/.test(rest);
}

function emptyRender(): RenderOutput {
  return { html: '', headings: [], anchors: new Set(), links: [], localAnchors: [], text: '', excerpt: '' };
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
