/**
 * Plot rendering: every `content/<page>/plots/*.py` script is executed by
 * scripts/wiki/plot/render_plot.py and its open figures are saved as PNGs in a
 * light and a dark theme. Results are cached in .cache/plots/<key>/ where the key
 * hashes the script, its sibling data files, the renderer and the Python
 * requirements, so a render happens only when one of those changes.
 *
 * Frozen plots: for scripts too slow to re-render, `pnpm wiki freeze <script>` commits the
 * rendered images next to the script as `<name>.frozen.json` + `<name>.frozen.<i>-<theme>.webp`.
 * A frozen script is never executed; editing it afterwards produces a warning until it is
 * re-frozen (`pnpm wiki freeze`) or unfrozen (`pnpm wiki unfreeze`).
 */
import { spawn, spawnSync } from 'node:child_process';
import crypto from 'node:crypto';
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import type { Diagnostics } from './diagnostics.ts';
import { PLOT_CACHE_DIR, PLOT_RENDERER, PLOT_REQUIREMENTS, REPO_ROOT, rel } from './paths.ts';
import type { ContentTree } from './scan.ts';

/** Bump to invalidate every cached plot (e.g. after changing how results are post-processed). */
const RENDERER_VERSION = '1';
const TIMEOUT_MS = Number(process.env.WIKI_PLOT_TIMEOUT_MS ?? 30 * 60_000);
/** Renders slower than this are called out in the log (they slow down cold builds and CI). */
const SLOW_MS = 5 * 60_000;

export interface PlotFigure {
  width: number;
  height: number;
}

export interface PlotResult {
  /** Content hash; also the published directory name (plots/<key>/). */
  key: string;
  /** Directory holding the images: a cache entry, or the script's plots/ folder when frozen. */
  imageDir: string;
  /** File name prefix of the images inside imageDir ('' for cache entries, '<name>.frozen.' when frozen). */
  imagePrefix: string;
  frozen: boolean;
  figures: PlotFigure[];
  source: string;
  /** Optional companion `<name>.R`: the same figure in R, shown next to the Python source (never run). */
  rSource?: string;
  error?: string;
}

export type PlotTheme = 'light' | 'dark';

export function plotImagePath(result: PlotResult, index: number, theme: PlotTheme): string {
  return path.join(result.imageDir, `${result.imagePrefix}${index}-${theme}.webp`);
}

const FROZEN_RE = /\.frozen\./;

export function frozenPrefix(script: string): string {
  return `${path.basename(script, '.py')}.frozen.`;
}

interface FrozenMeta {
  figures: PlotFigure[];
  /** scriptHash() of the script the images were rendered from. */
  sourceHash: string;
}

export function scriptHash(source: string): string {
  return crypto.createHash('sha256').update(source).digest('hex').slice(0, 16);
}

/** Absolute script path -> result. */
export type PlotResults = Map<string, PlotResult>;

const CJK_RE = /[\u3000-\u303F\u3400-\u9FFF\uFF00-\uFFEF]/;

/** Static checks that keep plot scripts deterministic and language-neutral. */
/** R companions are shown on both language versions, so like plot scripts they are English-only. */
export function lintRCompanion(file: string, source: string, diag: Diagnostics): void {
  source.split('\n').forEach((line, i) => {
    if (/\p{Script=Han}/u.test(line)) diag.warn(file, 'R companion contains Chinese characters (keep code and comments English)', i + 1);
  });
}

export function lintPlotScript(file: string, source: string, diag: Diagnostics): void {
  source.split('\n').forEach((line, i) => {
    const code = line.replace(/#.*$/, '');
    if (CJK_RE.test(line)) {
      diag.error(file, 'plot scripts must be English-only (figures are shared by every language; comments too)', i + 1);
    }
    if (/\bsavefig\s*\(/.test(code)) diag.error(file, 'do not call savefig(); every open figure is saved automatically', i + 1);
    if (/\bplt\.show\s*\(/.test(code)) diag.error(file, 'do not call plt.show(); leave figures open instead', i + 1);
    if (/\bmatplotlib\.use\s*\(/.test(code)) diag.error(file, 'do not call matplotlib.use(); the renderer selects the backend', i + 1);
    if (/style\.use\s*\(|font\.(sans-serif|family)/.test(code)) {
      diag.warn(file, 'avoid global styles and fonts; the renderer applies the light/dark themes', i + 1);
    }
  });
}

export function resolvePython(): string {
  if (process.env.WIKI_PYTHON) return process.env.WIKI_PYTHON;
  const venv = path.join(REPO_ROOT, '.venv', process.platform === 'win32' ? 'Scripts/python.exe' : 'bin/python');
  return fs.existsSync(venv) ? venv : 'python3';
}

function checkPython(python: string): string | null {
  const r = spawnSync(python, ['-c', 'import matplotlib, numpy'], { encoding: 'utf8' });
  if (r.error) return `cannot run "${python}": ${r.error.message}`;
  if (r.status !== 0) return `"${python}" cannot import matplotlib/numpy`;
  return null;
}

function hashFiles(parts: (string | Buffer)[]): string {
  const h = crypto.createHash('sha256');
  for (const p of parts) {
    h.update(p);
    h.update('\0');
  }
  return h.digest('hex').slice(0, 16);
}

function readMeta(dir: string, prefix = '', metaName = 'meta.json'): PlotFigure[] | null {
  try {
    const meta = JSON.parse(fs.readFileSync(path.join(dir, metaName), 'utf8')) as { figures: PlotFigure[] };
    const complete = meta.figures.every((_, i) =>
      ['light', 'dark'].every((t) => fs.existsSync(path.join(dir, `${prefix}${i}-${t}.webp`))),
    );
    return complete && meta.figures.length > 0 ? meta.figures : null;
  } catch {
    return null;
  }
}

function runRenderer(python: string, script: string, outDir: string): Promise<string | null> {
  return new Promise((resolve) => {
    const child = spawn(python, [PLOT_RENDERER, script, outDir], {
      env: { ...process.env, MPLBACKEND: 'Agg', PYTHONDONTWRITEBYTECODE: '1' },
      stdio: ['ignore', 'ignore', 'pipe'],
    });
    let stderr = '';
    child.stderr.on('data', (d: Buffer) => (stderr += d.toString()));
    const timer = setTimeout(() => {
      child.kill('SIGKILL');
      stderr += `\nkilled after ${TIMEOUT_MS / 1000}s (set WIKI_PLOT_TIMEOUT_MS to raise the limit)`;
    }, TIMEOUT_MS);
    child.on('close', (code) => {
      clearTimeout(timer);
      resolve(code === 0 ? null : stderr.trim().split('\n').slice(-12).join('\n') || `exit code ${code}`);
    });
    child.on('error', (e) => {
      clearTimeout(timer);
      resolve(e.message);
    });
  });
}

async function pool<T>(items: T[], size: number, fn: (item: T) => Promise<void>): Promise<void> {
  let next = 0;
  const workers = Array.from({ length: Math.min(size, items.length) }, async () => {
    while (next < items.length) await fn(items[next++]);
  });
  await Promise.all(workers);
}

export interface RenderPlotsOptions {
  /** Called with progress messages (renders only; cache hits are silent). */
  log?: (message: string) => void;
  /** Scripts to render normally even if frozen (used by `pnpm wiki freeze`). */
  ignoreFrozen?: Set<string>;
  /** Delete cache entries not used by this run (default true; tests on temporary trees pass false). */
  prune?: boolean;
  /** Only these pages' scripts (and no pruning); used by `pnpm wiki lint`. */
  pages?: Set<string>;
}

export async function renderPlots(tree: ContentTree, diag: Diagnostics, opts: RenderPlotsOptions = {}): Promise<PlotResults> {
  const log = opts.log ?? (() => {});
  const results: PlotResults = new Map();
  const common = [RENDERER_VERSION, fs.readFileSync(PLOT_RENDERER), fs.readFileSync(PLOT_REQUIREMENTS)];
  const todo: { script: string; result: PlotResult }[] = [];

  for (const page of tree.pages.values()) {
    if (!page.plotFiles.length || (opts.pages && !opts.pages.has(page.id))) continue;
    const plotDir = path.join(page.dir, 'plots');
    const dataFiles = page.plotFiles
      .filter((f) => !f.endsWith('.py') && !f.endsWith('.R') && !FROZEN_RE.test(f))
      .map((f) => fs.readFileSync(path.join(plotDir, f)));
    for (const name of page.plotFiles.filter((f) => f.endsWith('.R'))) {
      const file = path.join(plotDir, name);
      if (!page.plotFiles.includes(name.replace(/\.R$/, '.py'))) diag.warn(file, `R companion without a plot script: add ${name.replace(/\.R$/, '.py')} (the figure is always drawn by Python)`);
      lintRCompanion(file, fs.readFileSync(file, 'utf8'), diag);
    }
    for (const name of page.plotFiles.filter((f) => f.endsWith('.py'))) {
      const script = path.join(plotDir, name);
      const source = fs.readFileSync(script, 'utf8');
      const rName = name.replace(/\.py$/, '.R');
      const rSource = page.plotFiles.includes(rName) ? fs.readFileSync(path.join(plotDir, rName), 'utf8') : undefined;
      lintPlotScript(script, source, diag);
      const prefix = frozenPrefix(script);
      if (page.plotFiles.includes(`${prefix}json`) && !opts.ignoreFrozen?.has(script)) {
        results.set(script, { ...loadFrozen(script, source, plotDir, prefix, diag), rSource });
        continue;
      }
      const key = hashFiles([...common, source, ...dataFiles]);
      const cacheDir = path.join(PLOT_CACHE_DIR, key);
      const cached = readMeta(cacheDir);
      const result: PlotResult = { key, imageDir: cacheDir, imagePrefix: '', frozen: false, figures: cached ?? [], source, rSource };
      results.set(script, result);
      if (!cached) todo.push({ script, result });
    }
  }

  if (todo.length) {
    const python = resolvePython();
    const problem = checkPython(python);
    if (problem) {
      for (const { script, result } of todo) {
        result.error = 'Python environment unavailable';
        diag.error(script, `cannot render plot: ${problem}. Run \`pnpm setup:python\` (or set WIKI_PYTHON).`);
      }
    } else {
      const parallel = Math.max(1, Math.min(8, os.availableParallelism() - 1));
      log(`rendering ${todo.length} plot script(s) with ${python} (${parallel} in parallel)`);
      await pool(todo, parallel, async ({ script, result }) => {
        const started = Date.now();
        const tmp = `${result.imageDir}.tmp-${process.pid}`;
        fs.rmSync(tmp, { recursive: true, force: true });
        const error = await runRenderer(python, script, tmp);
        const figures = error ? null : readMeta(tmp);
        if (!figures) {
          fs.rmSync(tmp, { recursive: true, force: true });
          result.error = error ?? 'renderer produced no figures';
          diag.error(script, `plot script failed:\n${result.error.replace(/^/gm, '    ')}`);
          return;
        }
        fs.rmSync(result.imageDir, { recursive: true, force: true });
        fs.renameSync(tmp, result.imageDir);
        result.figures = figures;
        const elapsed = Date.now() - started;
        if (elapsed > SLOW_MS) {
          log(`  slow plot: ${rel(script)} took ${Math.round(elapsed / 1000)}s; consider coarser parameters or a faster solver`);
        }
        log(`  rendered ${rel(script)} (${figures.length} figure(s), ${((Date.now() - started) / 1000).toFixed(1)}s)`);
      });
    }
  }

  // Prune cache entries no longer referenced, but only when every plot is available,
  // so a broken environment never wipes a good cache.
  if (opts.prune !== false && !opts.pages && [...results.values()].every((r) => !r.error) && fs.existsSync(PLOT_CACHE_DIR)) {
    const live = new Set([...results.values()].filter((r) => !r.frozen).map((r) => r.key));
    for (const name of fs.readdirSync(PLOT_CACHE_DIR)) {
      if (!live.has(name)) fs.rmSync(path.join(PLOT_CACHE_DIR, name), { recursive: true, force: true });
    }
  }
  return results;
}

function loadFrozen(script: string, source: string, plotDir: string, prefix: string, diag: Diagnostics): PlotResult {
  const metaFile = path.join(plotDir, `${prefix}json`);
  const figures = readMeta(plotDir, prefix, `${prefix}json`);
  const base: PlotResult = { key: '', imageDir: plotDir, imagePrefix: prefix, frozen: true, figures: figures ?? [], source };
  if (!figures) {
    diag.error(metaFile, `frozen plot is incomplete (missing images); run \`pnpm wiki freeze ${rel(script)}\` again`);
    return { ...base, error: 'frozen plot incomplete' };
  }
  const meta = JSON.parse(fs.readFileSync(metaFile, 'utf8')) as FrozenMeta;
  if (meta.sourceHash !== scriptHash(source)) {
    diag.warn(script, `script changed since it was frozen; the old images are still used. Run \`pnpm wiki freeze ${rel(script)}\` to re-render (slow) or revert the edit`);
  }
  const images = figures.flatMap((_, i) => (['light', 'dark'] as const).map((t) => fs.readFileSync(path.join(plotDir, `${prefix}${i}-${t}.webp`))));
  return { ...base, key: hashFiles(['frozen', fs.readFileSync(metaFile), ...images]) };
}

/** Copy a rendered (cached) result next to its script as committed frozen files. */
export function writeFrozen(script: string, result: PlotResult): string[] {
  const dir = path.dirname(script);
  const prefix = frozenPrefix(script);
  for (const name of fs.readdirSync(dir)) if (name.startsWith(prefix)) fs.rmSync(path.join(dir, name));
  const written: string[] = [];
  result.figures.forEach((_, i) => {
    for (const theme of ['light', 'dark'] as const) {
      const dest = path.join(dir, `${prefix}${i}-${theme}.webp`);
      fs.copyFileSync(plotImagePath(result, i, theme), dest);
      written.push(dest);
    }
  });
  const meta: FrozenMeta = { figures: result.figures, sourceHash: scriptHash(result.source) };
  const metaFile = path.join(dir, `${prefix}json`);
  fs.writeFileSync(metaFile, `${JSON.stringify(meta, null, 2)}\n`);
  return [metaFile, ...written];
}

export function removeFrozen(script: string): string[] {
  const dir = path.dirname(script);
  const prefix = frozenPrefix(script);
  const removed = fs.readdirSync(dir).filter((n) => n.startsWith(prefix)).map((n) => path.join(dir, n));
  for (const f of removed) fs.rmSync(f);
  return removed;
}
