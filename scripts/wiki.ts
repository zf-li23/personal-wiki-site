/**
 * Wiki command line. Run with `pnpm wiki <command>` (Node >= 22.18 runs TypeScript directly).
 *
 *   build [--strict]                 content/ -> .generated/ ; exits 1 on errors (and on warnings with --strict)
 *   status [--all]                   translation status per page (stale / untranslated / ...)
 *   stamp <id>... | --all            mark translations as up to date with the current source text
 *   new <parent-id|root> <slug> <zh-title> <en-title>
 *                                    create the next page under a parent, with both language files
 *   terms [<id>...]                  glossary check: first use of each term must carry its English name
 *   freeze <plots/script.py>...      render once and commit the images; the script is never run again
 *   unfreeze <plots/script.py>...    delete the frozen images; the script renders normally again
 */
import fs from 'node:fs';
import path from 'node:path';
import { LANGUAGES, siteConfig } from '../site.config.ts';
import { compareIds, idSegments } from '../src/shared/page-id.ts';
import { buildContent, sourceHash, translationStatus } from './wiki/build.ts';
import { Diagnostics } from './wiki/diagnostics.ts';
import { serializePageFile } from './wiki/frontmatter.ts';
import { findUnannotatedTerms, loadGlossary } from './wiki/glossary.ts';
import { CONTENT_DIR, REPO_ROOT, rel } from './wiki/paths.ts';
import { removeFrozen, renderPlots, writeFrozen } from './wiki/plots.ts';
import { pageFileName, scanContent } from './wiki/scan.ts';

const [command, ...args] = process.argv.slice(2);
const flags = new Set(args.filter((a) => a.startsWith('--')));
const positional = args.filter((a) => !a.startsWith('--'));

function fail(message: string): never {
  console.error(`\x1b[31m${message}\x1b[0m`);
  process.exit(1);
}

function scanOrFail() {
  const diag = new Diagnostics();
  const tree = scanContent(diag);
  if (diag.errorCount) {
    console.error(diag.format());
    fail('content structure has errors; fix them first (pnpm wiki build shows all problems)');
  }
  return tree;
}

async function build() {
  const started = Date.now();
  const { diag, tree } = await buildContent({ log: (m) => console.log(m) });
  if (diag.items.length) console.log(diag.format());
  const summary = `${tree.pages.size} pages, ${diag.errorCount} error(s), ${diag.warningCount} warning(s) in ${((Date.now() - started) / 1000).toFixed(1)}s`;
  if (diag.errorCount || (flags.has('--strict') && diag.warningCount)) fail(`content build failed: ${summary}`);
  console.log(`\x1b[32mcontent build ok:\x1b[0m ${summary}`);
}

function status() {
  const tree = scanOrFail();
  const rows: string[] = [];
  const counts: Record<string, number> = {};
  const ids = [...tree.pages.keys()].sort(compareIds);
  for (const id of ids) {
    const page = tree.pages.get(id)!;
    for (const lang of LANGUAGES) {
      if (lang === siteConfig.sourceLanguage) continue;
      const s = translationStatus(page, lang);
      counts[s] = (counts[s] ?? 0) + 1;
      if (flags.has('--all') || s === 'stale' || s === 'untranslated') {
        const chars = page.files[siteConfig.sourceLanguage]?.body.trim().length ?? 0;
        rows.push(`${lang}  ${s.padEnd(12)} ${id.padEnd(10)} ${String(chars).padStart(7)} chars  ${page.files[siteConfig.sourceLanguage]?.frontMatter.title ?? ''}`);
      }
    }
  }
  if (rows.length) console.log(rows.join('\n'));
  console.log(Object.entries(counts).map(([k, v]) => `${k}: ${v}`).join(', '));
}

function stamp() {
  const tree = scanOrFail();
  const ids = flags.has('--all') ? [...tree.pages.keys()] : positional;
  if (!ids.length) fail('usage: pnpm wiki stamp <id>... | --all');
  for (const id of ids) {
    const page = tree.pages.get(id) ?? fail(`unknown page id "${id}"`);
    const source = page.files[siteConfig.sourceLanguage];
    for (const lang of LANGUAGES) {
      if (lang === siteConfig.sourceLanguage) continue;
      const file = page.files[lang];
      if (!source || !file || !file.body.trim()) {
        if (!flags.has('--all')) console.log(`skip ${id} (${lang}): no translation body`);
        continue;
      }
      const hash = sourceHash(source.body);
      if (file.frontMatter.source_hash === hash) continue;
      fs.writeFileSync(file.path, serializePageFile({ ...file.frontMatter, source_hash: hash }, file.body));
      console.log(`stamped ${rel(file.path)} (${hash})`);
    }
  }
}

function newPage() {
  const [parent, slug, zhTitle, enTitle] = positional;
  if (!parent || !slug || !zhTitle || !enTitle) fail('usage: pnpm wiki new <parent-id|root> <slug> <zh-title> <en-title>');
  if (!/^[a-z0-9]+(-[a-z0-9]+)*$/.test(slug)) fail('slug must be lowercase kebab-case ASCII, e.g. "central-limit-theorem"');
  const tree = scanOrFail();
  const siblings = parent === 'root' ? tree.rootIds : (tree.pages.get(parent) ?? fail(`unknown parent id "${parent}"`)).childIds;
  const next = siblings.length ? Math.max(...siblings.map((s) => idSegments(s).at(-1)!)) + 1 : 1;
  const id = parent === 'root' ? String(next) : `${parent}.${next}`;
  const dir = path.join(parent === 'root' ? CONTENT_DIR : tree.pages.get(parent)!.dir, `${id}.${slug}`);
  fs.mkdirSync(dir);
  const titles = { zh: zhTitle, en: enTitle } as const;
  for (const lang of LANGUAGES) fs.writeFileSync(path.join(dir, pageFileName(lang)), serializePageFile({ title: titles[lang] }, ''));
  console.log(`created ${rel(dir)} (page id ${id})`);
}

function terms() {
  const diag = new Diagnostics();
  const glossary = loadGlossary(diag);
  const tree = scanOrFail();
  if (diag.errorCount) fail(diag.format());
  const ids = positional.length ? positional : [...tree.pages.keys()].sort(compareIds);
  let total = 0;
  for (const id of ids) {
    const page = tree.pages.get(id) ?? fail(`unknown page id "${id}"`);
    const file = page.files[siteConfig.sourceLanguage];
    if (!file) continue;
    for (const f of findUnannotatedTerms(file.body, glossary)) {
      total++;
      const line = f.line ? `:${f.line + file.bodyLineOffset}` : '';
      console.log(`${rel(file.path)}${line}\n  first use of "${f.term.zh}" should be written "${f.term.zh}（${f.term.en}）"`);
    }
  }
  console.log(`${glossary.length} glossary terms, ${total} unannotated first use(s)`);
}

function scriptArgs(): string[] {
  if (!positional.length) fail(`usage: pnpm wiki ${command} content/<page>/plots/<name>.py ...`);
  return positional.map((p) => {
    const abs = path.resolve(REPO_ROOT, p);
    if (!abs.endsWith('.py') || path.basename(path.dirname(abs)) !== 'plots' || !fs.existsSync(abs)) fail(`not a plot script: ${p}`);
    return abs;
  });
}

async function freeze() {
  const scripts = scriptArgs();
  const tree = scanOrFail();
  const diag = new Diagnostics();
  const results = await renderPlots(tree, diag, { ignoreFrozen: new Set(scripts), log: (m) => console.log(m) });
  for (const script of scripts) {
    const result = results.get(script);
    if (!result || result.error || result.frozen) fail(`could not render ${rel(script)}:\n${diag.format()}`);
    for (const f of writeFrozen(script, result)) console.log(`wrote ${rel(f)}`);
  }
  console.log('commit these files; the frozen scripts will not be executed by later builds');
}

function unfreeze() {
  for (const script of scriptArgs()) {
    const removed = removeFrozen(script);
    console.log(removed.length ? removed.map((f) => `removed ${rel(f)}`).join('\n') : `${rel(script)} was not frozen`);
  }
}

const commands: Record<string, () => void | Promise<void>> = { build, status, stamp, new: newPage, terms, freeze, unfreeze };
const run = commands[command ?? ''] ?? (() => fail(`unknown command "${command ?? ''}". Commands: ${Object.keys(commands).join(', ')}`));
await run();
