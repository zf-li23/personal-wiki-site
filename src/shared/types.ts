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

/** A course the knowledge on a page comes from (front matter `courses`). */
export interface CourseRef {
  code: string | number;
  /** The course name as the institution gives it. */
  name: string;
  /** English name, shown on English pages when `name` is not English. */
  name_en?: string;
  /** e.g. "概率论部分" when the page covers only part of the course. */
  note?: string;
}

/** A reference book (front matter `textbooks`). */
export interface TextbookRef {
  /** Original title and author(s), as printed in the book. */
  title: string;
  author: string;
  edition?: string | number;
  /** For a book not in English: English title / romanised authors, shown on English pages. */
  title_en?: string;
  author_en?: string;
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
  /** Knowledge sources from the source-language front matter (shown in every language). */
  courses?: CourseRef[];
  textbooks?: TextbookRef[];
  /** Pages that link here (references, concept links, explicit links), in reading order. */
  backlinks: string[];
  /** Concept ids mentioned or defined on this page. */
  concepts: string[];
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

/** One entry of `<base>/data/concepts.json` (concept registry joined with where it is defined and used). */
export interface ConceptEntry {
  /** Kebab-case English name, e.g. "central-limit-theorem". */
  id: string;
  zh: string;
  en: string;
  /** Definition site; absent while no page defines the concept. */
  site?: { pageId: string; anchor: string };
  /** Pages (source language) that mention or define it, in reading order. */
  usedIn: string[];
}
