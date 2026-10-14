/**
 * Data contracts between the content pipeline (scripts/wiki) and the client (src).
 * The pipeline writes these shapes to .generated/; the client only reads them.
 * Changing a shape here requires updating both sides — `pnpm typecheck` catches mismatches.
 */
import type { Lang } from '../../site.config.ts';

export type { Lang };

/**
 * - source:       page in the source language (zh)
 * - translated:   translation exists and its source_hash matches the current source text
 * - stale:        translation exists but the source text changed since it was stamped
 * - untranslated: translation body is empty; the payload carries the source-language HTML instead
 * - empty:        neither language has body text yet (a placeholder page)
 */
export type TranslationStatus = 'source' | 'translated' | 'stale' | 'untranslated' | 'empty';

export interface NavNode {
  /** Page id, e.g. "7.4.1.5". Unique, purely numeric, hierarchical. */
  id: string;
  title: Record<Lang, string>;
  /** Whether the page has its own body text in each language (after fallback rules, see status). */
  status: Record<Lang, TranslationStatus>;
  children: NavNode[];
}

export interface SiteData {
  /** Changes on every content build; used to bust the client-side page cache. */
  buildId: string;
  nav: NavNode[];
}

export interface TocHeading {
  id: string;
  text: string;
  depth: 2 | 3;
}

export interface Diagnostic {
  level: 'error' | 'warning';
  file: string;
  line?: number;
  message: string;
}

/** Served at `<base>/data/pages/<lang>/<id>.json`. */
export interface PagePayload {
  id: string;
  lang: Lang;
  title: string;
  status: TranslationStatus;
  /** Language of `html`; differs from `lang` when an untranslated page falls back to the source. */
  contentLang: Lang;
  /** Pre-rendered article body (math, highlighting and plots already resolved at build time). */
  html: string;
  headings: TocHeading[];
  /** Plain-text excerpt for <meta name="description">. */
  description: string;
  /** Present only in dev builds: problems found while building this page. */
  diagnostics?: Diagnostic[];
}

/** One entry of `<base>/data/search/<lang>.json`. */
export interface SearchEntry {
  id: string;
  title: string;
  /** Ancestor titles, e.g. "Biology / Mathematical Modeling in Biology". */
  trail: string;
  headings: string[];
  /** Plain body text without code and math. */
  text: string;
}
