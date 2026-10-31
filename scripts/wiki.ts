/**
 * Wiki command line. Run with `pnpm wiki <command>` (Node >= 22.18 runs TypeScript directly).
 *
 *   build [--strict]                 content/ -> .generated/ ; exits 1 on errors (and on warnings with --strict)
 *   lint <id>...                     fast check for writers: renders only the pages' courses, reports problems
 *                                    in those pages and bold text outside definitions that does not link
 *   status [--all]                   translation status per page (stale / untranslated / ...)
 *   stamp <id>... [--from <lang>] | --all
 *                                    mark translations as up to date with the current source text;
 *                                    --from names the source language when both files are written
 *                                    and neither is stamped yet (a page may be written in either language)
 *   new <parent-id|root> <slug> <zh-title> <en-title>
 *                                    create the next page under a parent, with both language files
 *   terms                            concept report: concepts without a definition, uses before the definition
 *   terms <id-prefix>...             a course's checklist: concepts used there without a definition site (exit 1)
 *   terms --bold [<id-prefix>...]    list bold text that is not a concept name (and so does not link)
 *   fix [<id>...] [--dry-run]        rewrite heading / statement-label formats and formula notation into the canonical form
 *   freeze <plots/script.py>...      render once and commit the images; the script is never run again
 *   unfreeze <plots/script.py>...    delete the frozen images; the script renders normally again
 *   check-r [<id-prefix>...]         run the R companions (plots/*.R) with Rscript, if installed (local check only)
 */
import { spawnSync } from 'node:child_process';
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import { LANGUAGES, type Lang, isLang } from '../site.config.ts';
import { compareIds, idSegments } from '../src/shared/page-id.ts';
import { courseOf } from './wiki/numbering.ts';
import { buildContent, sourceHash, translationStatus } from './wiki/build.ts';
import { Diagnostics } from './wiki/diagnostics.ts';
import { fixMarkdown } from './wiki/fix.ts';
import { serializePageFile } from './wiki/frontmatter.ts';
import { CONTENT_DIR, GENERATED_PUBLIC_DIR, PUBLIC_PATHS, REPO_ROOT, rel } from './wiki/paths.ts';
import { removeFrozen, renderPlots, writeFrozen } from './wiki/plots.ts';
import { type PageSource, pageFileName, scanContent } from './wiki/scan.ts';
import type { ConceptEntry } from '../src/shared/types.ts';

const [command, ...args] = process.argv.slice(2);
const flags = new Set(args.filter((a) => a.startsWith('--')));
const positional = args.filter((a, i) => !a.startsWith('--') && args[i - 1] !== '--from');

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

/**
 * Fast check of some pages for writers: renders and links only their courses (both languages),
 * reports the problems in the given pages, and the bold runs outside definitions that do not link.
 * Definition sites in other courses are compared with the concept registry of the last full build
 * (`.generated/`), so a second definition of a concept defined in another course is reported here;
 * the authoritative site-wide checks still come from a full `build`.
 */
async function lint() {
  if (!positional.length) fail('usage: pnpm wiki lint <id>...  (a chapter, a course, or a discipline)');
  const started = Date.now();
  const tree = scanOrFail();
  const under = (id: string, p: string) => id === p || id.startsWith(`${p}.`);
  for (const p of positional) if (!tree.pages.has(p)) fail(`unknown page id "${p}"`);
  const courses = positional.map((p) => courseOf(p));
  const only = new Set([...tree.pages.keys()].filter((id) => courses.some((c) => under(id, c))));
  const { diag, plainBold, concepts } = await buildContent({ only });
  const dirs = positional.map((p) => `${rel(tree.pages.get(p)!.dir)}/`);
  const report = new Diagnostics();
  report.items.push(...diag.items.filter((d) => dirs.some((dir) => d.file.startsWith(dir))));
  for (const [key, list] of plainBold) {
    const [, id] = key.split('/') as [Lang, string];
    if (!positional.some((p) => under(id, p))) continue;
    const page = tree.pages.get(id)!;
    const outside = list.filter((b) => !b.inDefinition).map((b) => `**${b.text}**`);
    if (outside.length) report.warn(page.files[key.split('/')[0] as Lang]!.path, `bold outside definitions that is not a concept name (make it a concept, rephrase, or drop the bold): ${outside.join('  ')}`);
  }
  for (const w of crossCourseDefinitions(tree, concepts, only, positional, under)) report.warn(w.file, w.message);
  if (report.items.length) console.log(report.format());
  const summary = `${only.size} pages rendered, ${report.errorCount} error(s), ${report.warningCount} warning(s) in ${positional.join(', ')} (${((Date.now() - started) / 1000).toFixed(1)}s)`;
  if (report.items.length) fail(`lint: ${summary}`);
  console.log(`\x1b[32mlint ok:\x1b[0m ${summary}`);
}

/**
 * Definition marks in the linted pages for concepts that the last full build places in another
 * course: in a full build one of the two marks is an error (an annotation or italics marks *the*
 * definition; restating a 定义 label is allowed, so two statement sites are not reported).
 */
function crossCourseDefinitions(
  tree: ReturnType<typeof scanOrFail>,
  concepts: ConceptEntry[],
  only: Set<string>,
  targets: string[],
  under: (id: string, p: string) => boolean,
): { file: string; message: string }[] {
  const registry = path.join(GENERATED_PUBLIC_DIR, PUBLIC_PATHS.concepts);
  if (!fs.existsSync(registry)) return [];
  let previous: ConceptEntry[];
  try {
    previous = JSON.parse(fs.readFileSync(registry, 'utf8')) as ConceptEntry[];
  } catch {
    return [];
  }
  const before = new Map(previous.map((c) => [c.id, c.site]));
  const out: { file: string; message: string }[] = [];
  for (const c of concepts) {
    const here = c.site;
    const there = before.get(c.id);
    if (!here || !there || only.has(there.pageId) || !targets.some((t) => under(here.pageId, t))) continue;
    if (!here.anchor.startsWith('concept-') && !there.anchor.startsWith('concept-')) continue;
    const page = tree.pages.get(here.pageId);
    const file = page?.files[page.sourceLang]?.path ?? here.pageId;
    out.push({ file, message: `concept "${c.zh}（${c.en}）" is already defined on page ${there.pageId} (last full build): drop the defining mark here and bold the name to link there, or move the definition deliberately` });
  }
  return out;
}

function status() {
  const tree = scanOrFail();
  const rows: string[] = [];
  const counts: Record<string, number> = {};
  const ids = [...tree.pages.keys()].sort(compareIds);
  for (const id of ids) {
    const page = tree.pages.get(id)!;
    const source = page.files[page.sourceLang];
    for (const lang of LANGUAGES) {
      if (lang === page.sourceLang) continue;
      const s = translationStatus(page, lang);
      counts[s] = (counts[s] ?? 0) + 1;
      if (flags.has('--all') || s === 'stale' || s === 'untranslated') {
        const chars = source?.body.trim().length ?? 0;
        rows.push(`${page.sourceLang}→${lang}  ${s.padEnd(12)} ${id.padEnd(10)} ${String(chars).padStart(7)} chars  ${source?.frontMatter.title ?? ''}`);
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
    const from = fromLang(page);
    const source = page.files[from];
    for (const lang of LANGUAGES) {
      if (lang === from) continue;
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

/** Source language for `stamp`: --from, or the page's own when it is unambiguous. */
function fromLang(page: PageSource): Lang {
  const i = args.indexOf('--from');
  if (i >= 0) {
    const value = args[i + 1];
    if (!value || !isLang(value)) fail(`--from needs a language (${LANGUAGES.join(', ')})`);
    return value;
  }
  const written = LANGUAGES.filter((l) => page.files[l]?.body.trim());
  const stamped = written.some((l) => page.files[l]!.frontMatter.source_hash);
  if (written.length > 1 && !stamped && !flags.has('--all')) {
    fail(`${page.id}: both languages are written and neither is stamped; say which one is the source: pnpm wiki stamp ${page.id} --from ${LANGUAGES.join('|')}`);
  }
  return page.sourceLang;
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

async function terms() {
  const { diag, concepts, forwardUses, plainBold } = await buildContent({ dryRun: true });
  if (flags.has('--bold')) {
    // Bold = emphasis = link (CONTENT_GUIDE §6): outside definitions every bold run should be a
    // concept name or a label; inside a 定义 a bold run names the term being defined.
    const match = (id: string) => !positional.length || positional.some((p) => id === p || id.startsWith(`${p}.`));
    const counts = { outside: 0, inDefinition: 0 };
    for (const [key, list] of [...plainBold].sort(([a], [b]) => compareIds(a.split('/')[1], b.split('/')[1]) || a.localeCompare(b))) {
      if (!list.length || !match(key.split('/')[1])) continue;
      const outside = list.filter((b) => !b.inDefinition).map((b) => `**${b.text}**`);
      const inDef = list.filter((b) => b.inDefinition).map((b) => `**${b.text}**`);
      counts.outside += outside.length;
      counts.inDefinition += inDef.length;
      if (outside.length) console.log(`${key}  outside definitions: ${outside.join('  ')}`);
      if (inDef.length) console.log(`${key}  in definitions:      ${inDef.join('  ')}`);
    }
    console.log(
      `${counts.outside} bold run(s) outside definitions that are not concept names (make them concepts, rephrase, or drop the bold); ` +
        `${counts.inDefinition} defined term(s) not in the glossary (add the important ones)`,
    );
    return;
  }
  const own = diag.items.filter((d) => d.file.endsWith('glossary.yaml') || d.message.startsWith('concept "'));
  if (own.length) {
    const report = new Diagnostics();
    report.items.push(...own);
    console.log(report.format());
  }
  // `terms <id-prefix>...` narrows the report to concepts used on those pages (a course's checklist).
  const inScope = (id: string) => positional.some((p) => id === p || id.startsWith(`${p}.`));
  if (positional.length) {
    const missing = concepts.filter((c) => !c.site && c.usedIn.some(inScope));
    for (const c of missing) console.log(`  ${c.zh}（${c.en}）  used on ${c.usedIn.filter(inScope).join(', ')} but defined nowhere`);
    const early = forwardUses.filter((f) => inScope(f.pageId));
    for (const f of early) {
      const c = concepts.find((x) => x.id === f.conceptId)!;
      console.log(`  ${f.pageId} uses ${c.zh}（${c.en}） before its definition on ${c.site!.pageId}`);
    }
    console.log(`${missing.length} concept(s) used in ${positional.join(', ')} without a definition site (must be 0); ${early.length} forward use(s)`);
    if (missing.length) process.exitCode = 1;
    return;
  }
  const undefinedConcepts = concepts.filter((c) => !c.site);
  if (undefinedConcepts.length) {
    console.log('\nconcepts without a definition site (annotate the defining occurrence as 名称（English）, or name a 定义 after it):');
    for (const c of undefinedConcepts) console.log(`  ${c.zh}（${c.en}）  mentioned on ${c.usedIn.length} page(s)${c.usedIn.length ? `: ${c.usedIn.slice(0, 5).join(', ')}` : ''}`);
  }
  if (forwardUses.length) {
    console.log('\nconcepts used before the page that defines them (consider reordering or a forward pointer):');
    for (const f of forwardUses) {
      const c = concepts.find((x) => x.id === f.conceptId)!;
      console.log(`  ${f.pageId} uses ${c.zh}（${c.en}）, defined on ${c.site!.pageId}`);
    }
  }
  console.log(`\n${concepts.length} concepts: ${concepts.length - undefinedConcepts.length} defined, ${undefinedConcepts.length} without definition; ${forwardUses.length} forward use(s)`);
}

function fix() {
  const tree = scanOrFail();
  const ids = positional.length ? positional : [...tree.pages.keys()].sort(compareIds);
  let total = 0;
  for (const id of ids) {
    const page = tree.pages.get(id) ?? fail(`unknown page id "${id}"`);
    for (const lang of LANGUAGES) {
      const file = page.files[lang];
      if (!file) continue;
      const { text, changes } = fixMarkdown(file.body, lang, id);
      if (!changes) continue;
      total += changes;
      console.log(`${flags.has('--dry-run') ? 'would fix' : 'fixed'} ${changes} line(s) in ${rel(file.path)}`);
      if (!flags.has('--dry-run')) fs.writeFileSync(file.path, serializePageFile(file.frontMatter, text));
    }
  }
  console.log(`${total} line(s) ${flags.has('--dry-run') ? 'to fix' : 'fixed'}`);
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

/** R companions are never run by the build (CI has no R); this checks locally that they still run. */
function checkR() {
  const probe = spawnSync('Rscript', ['--version'], { encoding: 'utf8' });
  if (probe.error) {
    console.log('Rscript not found: install R to check the R companions (skipped)');
    return;
  }
  const tree = scanContent(new Diagnostics());
  const match = (id: string) => !positional.length || positional.some((p) => id === p || id.startsWith(`${p}.`));
  const failed: string[] = [];
  let count = 0;
  for (const page of [...tree.pages.values()].sort((a, b) => compareIds(a.id, b.id))) {
    if (!match(page.id)) continue;
    for (const name of page.plotFiles.filter((f) => f.endsWith('.R'))) {
      const file = path.join(page.dir, 'plots', name);
      // Run in a scratch directory so graphics devices (Rplots.pdf) never land in content/.
      const cwd = fs.mkdtempSync(path.join(os.tmpdir(), 'wiki-r-'));
      const res = spawnSync('Rscript', ['--vanilla', file], { cwd, encoding: 'utf8', timeout: 300_000 });
      fs.rmSync(cwd, { recursive: true, force: true });
      count++;
      if (res.status !== 0) {
        failed.push(rel(file));
        console.log(`FAIL ${rel(file)}\n${(res.stderr || res.error?.message || '').trim().split('\n').slice(-5).join('\n')}`);
      }
    }
  }
  console.log(`${count - failed.length}/${count} R companion(s) ran without error`);
  if (failed.length) process.exitCode = 1;
}

const commands: Record<string, () => void | Promise<void>> = { build, lint, status, stamp, new: newPage, terms, fix, freeze, unfreeze, 'check-r': checkR };
const run = commands[command ?? ''] ?? (() => fail(`unknown command "${command ?? ''}". Commands: ${Object.keys(commands).join(', ')}`));
await run();
