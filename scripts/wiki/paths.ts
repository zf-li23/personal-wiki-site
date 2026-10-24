import path from 'node:path';
import { fileURLToPath } from 'node:url';

export const REPO_ROOT = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '../..');

/** Source of truth for all pages. */
export const CONTENT_DIR = path.join(REPO_ROOT, 'content');
export const GLOSSARY_FILE = path.join(CONTENT_DIR, 'glossary.yaml');
/** Static files copied verbatim to the site root (e.g. .nojekyll). */
export const PUBLIC_DIR = path.join(REPO_ROOT, 'public');

/** Build output of the content pipeline (gitignored). Vite serves `.generated/public` as its publicDir. */
export const GENERATED_DIR = path.join(REPO_ROOT, '.generated');
export const GENERATED_PUBLIC_DIR = path.join(GENERATED_DIR, 'public');
export const SITE_DATA_FILE = path.join(GENERATED_DIR, 'site.json');

/** Persistent render cache for plots (gitignored, cached in CI). */
export const PLOT_CACHE_DIR = path.join(REPO_ROOT, '.cache', 'plots');
export const PLOT_RENDERER = path.join(REPO_ROOT, 'scripts', 'wiki', 'plot', 'render_plot.py');
export const PLOT_REQUIREMENTS = path.join(REPO_ROOT, 'scripts', 'wiki', 'plot', 'requirements.txt');
/** Helper modules plot scripts may import (on the renderer's path); part of the cache key of scripts that use them. */
export const PLOT_HELPERS = [
  path.join(REPO_ROOT, 'scripts', 'wiki', 'plot', 'wikichem.py'),
  path.join(REPO_ROOT, 'scripts', 'wiki', 'plot', 'wikibio'), // a package: every .py file inside counts
];
/** Vector icons for biology figures (`wikibio.icon("<id>")`), converted from open SVG libraries; see BIO_FIGURES.md. */
export const ICON_DIR = path.join(REPO_ROOT, 'scripts', 'wiki', 'plot', 'icons');

/** Paths inside the published site (relative to the base URL). */
export const PUBLIC_PATHS = {
  pages: 'data/pages',
  search: 'data/search',
  concepts: 'data/concepts.json',
  media: 'media',
  plots: 'plots',
} as const;

export function rel(file: string): string {
  return path.relative(REPO_ROOT, file).split(path.sep).join('/');
}
