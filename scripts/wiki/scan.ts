import fs from 'node:fs';
import path from 'node:path';
import { LANGUAGES, type Lang } from '../../site.config.ts';
import { PAGE_DIR_RE, compareIds, idSegments, parentIdOf } from '../../src/shared/page-id.ts';
import type { Diagnostics } from './diagnostics.ts';
import { type FrontMatter, parsePageFile } from './frontmatter.ts';
import { CONTENT_DIR, GLOSSARY_FILE } from './paths.ts';

export interface PageFile {
  path: string;
  frontMatter: FrontMatter;
  body: string;
  bodyLineOffset: number;
}

export interface PageSource {
  id: string;
  slug: string;
  dir: string;
  parentId: string | null;
  /** Parsed `index.<lang>.md`; missing when the file is absent or invalid (an error is reported). */
  files: Partial<Record<Lang, PageFile>>;
  /** File names inside `assets/`. */
  assets: string[];
  /** File names inside `plots/` (scripts and their data files). */
  plotFiles: string[];
  childIds: string[];
}

export interface ContentTree {
  pages: Map<string, PageSource>;
  rootIds: string[];
}

const PAGE_FILE_RE = /^index\.([a-z]+)\.md$/;
const IGNORED = (name: string) => name.startsWith('.') || name === '__pycache__';

export function pageFileName(lang: Lang): string {
  return `index.${lang}.md`;
}

/** Walk content/ and validate its structure. Never throws on content problems; reports them to `diag`. */
export function scanContent(diag: Diagnostics, contentDir = CONTENT_DIR): ContentTree {
  const pages = new Map<string, PageSource>();
  const rootIds: string[] = [];

  if (!fs.existsSync(contentDir)) {
    diag.error(contentDir, 'content directory does not exist');
    return { pages, rootIds };
  }

  for (const entry of fs.readdirSync(contentDir, { withFileTypes: true })) {
    if (IGNORED(entry.name)) continue;
    const full = path.join(contentDir, entry.name);
    if (entry.isFile() && full === GLOSSARY_FILE) continue;
    if (!entry.isDirectory()) {
      diag.error(full, 'unexpected file in content/ (only page directories and glossary.yaml are allowed)');
      continue;
    }
    const id = scanPage(full, null, pages, diag);
    if (id) rootIds.push(id);
  }
  rootIds.sort(compareIds);
  checkSiblings(rootIds, contentDir, null, diag);
  return { pages, rootIds };
}

function scanPage(dir: string, parentId: string | null, pages: Map<string, PageSource>, diag: Diagnostics): string | null {
  const name = path.basename(dir);
  const m = PAGE_DIR_RE.exec(name);
  if (!m) {
    diag.error(dir, `page directory name must be "<id>.<slug>" with a numeric id and a lowercase kebab-case slug, e.g. "7.4.1.software-tools"`);
    return null;
  }
  const [, id, slug] = m;
  if (parentIdOf(id) !== parentId) {
    const expected = parentId ? `"${parentId}.<n>"` : 'a single number';
    diag.error(dir, `page id "${id}" does not match its location: expected ${expected}`);
    return null;
  }
  if (id.split('.').length > 3) {
    diag.error(dir, `page ${id} is too deep: the wiki has three levels (discipline.course.chapter); merge it into its chapter page`);
    return null;
  }
  if (pages.has(id)) {
    diag.error(dir, `duplicate page id "${id}" (also used by ${pages.get(id)!.dir})`);
    return null;
  }

  const page: PageSource = { id, slug, dir, parentId, files: {}, assets: [], plotFiles: [], childIds: [] };
  pages.set(id, page);

  for (const entry of fs.readdirSync(dir, { withFileTypes: true })) {
    if (IGNORED(entry.name)) continue;
    const full = path.join(dir, entry.name);
    const fileMatch = PAGE_FILE_RE.exec(entry.name);
    if (entry.isFile() && fileMatch) {
      const lang = fileMatch[1];
      if (!(LANGUAGES as readonly string[]).includes(lang)) {
        diag.error(full, `unknown language "${lang}" (configured: ${LANGUAGES.join(', ')})`);
        continue;
      }
      const parsed = parsePageFile(fs.readFileSync(full, 'utf8'), lang as Lang);
      for (const e of parsed.errors) diag.error(full, e, 1);
      if (parsed.value) page.files[lang as Lang] = { path: full, ...parsed.value };
    } else if (entry.isDirectory() && entry.name === 'assets') {
      page.assets = listFlatDir(full, diag);
    } else if (entry.isDirectory() && entry.name === 'plots') {
      page.plotFiles = listFlatDir(full, diag);
    } else if (entry.isDirectory()) {
      const childId = scanPage(full, id, pages, diag);
      if (childId) page.childIds.push(childId);
    } else {
      diag.error(full, 'unexpected file in a page directory (allowed: index.<lang>.md, assets/, plots/, child pages)');
    }
  }

  for (const lang of LANGUAGES) {
    if (!fs.existsSync(path.join(dir, pageFileName(lang)))) {
      diag.error(path.join(dir, pageFileName(lang)), `missing ${pageFileName(lang)} (every page needs a file per language; a translation may have an empty body)`);
    }
  }
  page.childIds.sort(compareIds);
  checkSiblings(page.childIds, dir, id, diag);
  return id;
}

function listFlatDir(dir: string, diag: Diagnostics): string[] {
  const names: string[] = [];
  for (const entry of fs.readdirSync(dir, { withFileTypes: true })) {
    if (IGNORED(entry.name)) continue;
    if (!entry.isFile()) {
      diag.error(path.join(dir, entry.name), `${path.basename(dir)}/ must not contain subdirectories`);
      continue;
    }
    if (!/^[A-Za-z0-9][A-Za-z0-9._-]*$/.test(entry.name)) {
      diag.error(path.join(dir, entry.name), 'file names in assets/ and plots/ must be ASCII (letters, digits, ".", "_", "-")');
    }
    names.push(entry.name);
  }
  return names.sort();
}

function checkSiblings(ids: string[], dir: string, parentId: string | null, diag: Diagnostics): void {
  for (const [i, id] of ids.entries()) {
    if (idSegments(id).at(-1) !== i + 1) {
      const where = parentId ? `under ${parentId}` : 'at the top level';
      diag.warn(dir, `page numbers ${where} are not contiguous: expected ${parentId ? `${parentId}.` : ''}${i + 1}, found ${id}`);
      return;
    }
  }
}

/** Ancestors from the root down to (excluding) the page itself. */
export function ancestorsOf(tree: ContentTree, id: string): PageSource[] {
  const out: PageSource[] = [];
  let cur = tree.pages.get(id)?.parentId ?? null;
  while (cur) {
    const p = tree.pages.get(cur);
    if (!p) break;
    out.unshift(p);
    cur = p.parentId;
  }
  return out;
}
