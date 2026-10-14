/**
 * Per-visitor preferences in localStorage. Storage can be unavailable (private
 * mode, blocked cookies), so every access is guarded and has a default.
 */
import { type Lang, isLang, siteConfig } from '../../site.config.ts';

export type Theme = 'light' | 'dark';

const KEYS = { theme: 'wiki-theme', lang: 'wiki-lang' } as const;

function read(key: string): string | null {
  try {
    return localStorage.getItem(key);
  } catch {
    return null;
  }
}

function write(key: string, value: string) {
  try {
    localStorage.setItem(key, value);
  } catch {
    // ignore: preference simply is not remembered
  }
}

/** Mirrors the inline script in index.html that applies the theme before first paint. */
export function initialTheme(): Theme {
  const stored = read(KEYS.theme);
  if (stored === 'light' || stored === 'dark') return stored;
  return window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light';
}

export function storeTheme(theme: Theme) {
  write(KEYS.theme, theme);
}

/** Stored choice, else the browser language (Chinese -> zh, anything else -> en). */
export function preferredLang(): Lang {
  const stored = read(KEYS.lang);
  if (isLang(stored)) return stored;
  const nav = typeof navigator !== 'undefined' ? navigator.languages?.[0] ?? navigator.language : '';
  if (!nav) return siteConfig.defaultLanguage;
  return nav.toLowerCase().startsWith('zh') ? 'zh' : 'en';
}

export function storeLang(lang: Lang) {
  write(KEYS.lang, lang);
}
