/**
 * Site-wide configuration. This is the ONLY place where the deployment URL,
 * languages and site titles are defined. It is imported by the content
 * pipeline (Node), vite.config.ts and the browser client.
 */

export const LANGUAGES = ['zh', 'en'] as const;
export type Lang = (typeof LANGUAGES)[number];

export const siteConfig = {
  /** Public URL of the deployed site, with trailing slash. Its path becomes Vite's `base`. */
  siteUrl: 'https://zf-li23.github.io/personal-wiki-site/',
  repoUrl: 'https://github.com/zf-li23/personal-wiki-site',
  /** Default source language of a page (used when it is not evident which file is the source, see scan.ts `sourceLangOf`). */
  sourceLanguage: 'zh' as Lang,
  /** Language used when the visitor has no stored preference and the browser language is unknown. */
  defaultLanguage: 'zh' as Lang,
  title: { zh: '个人知识库', en: 'Personal Wiki' } satisfies Record<Lang, string>,
  description: {
    zh: '本科阶段的数学、统计、计算机与生物学知识库。',
    en: 'An undergraduate knowledge base of mathematics, statistics, computer science and biology.',
  } satisfies Record<Lang, string>,
};

/** URL path prefix of the site, e.g. "/personal-wiki-site/" (always starts and ends with "/"). */
export const BASE_PATH = new URL(siteConfig.siteUrl).pathname.replace(/\/?$/, '/');

export function isLang(value: unknown): value is Lang {
  return typeof value === 'string' && (LANGUAGES as readonly string[]).includes(value);
}
