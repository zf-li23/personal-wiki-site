/**
 * UI strings. Every user-visible string in src/ comes from here, so the two
 * languages cannot drift. Add a key to BOTH dictionaries (TypeScript enforces it).
 */
import { useParams } from 'react-router';
import { type Lang, isLang, siteConfig } from '../site.config.ts';

const zh = {
  siteTitle: siteConfig.title.zh,
  siteDescription: siteConfig.description.zh,
  home: '首页',
  search: '搜索',
  searchPlaceholder: '搜索标题、章节与正文…',
  searchLoading: '正在加载索引…',
  searchNoResults: '没有找到匹配的页面',
  searchHint: '↑↓ 选择 · Enter 打开 · Esc 关闭',
  onThisPage: '本页目录',
  inThisSection: '本章内容',
  previous: '上一篇',
  next: '下一篇',
  menu: '目录',
  closeMenu: '关闭目录',
  toggleTheme: '切换深色/浅色模式',
  switchLanguage: 'English',
  switchLanguageLabel: 'Switch to English',
  loading: '加载中…',
  loadError: '页面加载失败',
  retry: '重试',
  emptyPage: '本页内容尚未撰写。',
  untranslated: '本页尚无中文版本，以下显示原文。',
  stale: '原文已更新，本译文可能已过时。',
  notFoundTitle: '页面不存在',
  notFoundBody: '找不到这个地址对应的页面。',
  backHome: '返回首页',
  copy: '复制',
  copied: '已复制',
  pagesWritten: (done: number, total: number, _translated: number) => `已撰写 ${done} / ${total} 页`,
  subsections: (n: number) => `${n} 个子章节`,
  devDiagnostics: (n: number) => `构建发现 ${n} 个问题（仅开发模式可见）`,
};

const en: typeof zh = {
  siteTitle: siteConfig.title.en,
  siteDescription: siteConfig.description.en,
  home: 'Home',
  search: 'Search',
  searchPlaceholder: 'Search titles, sections and text…',
  searchLoading: 'Loading index…',
  searchNoResults: 'No matching pages',
  searchHint: '↑↓ to select · Enter to open · Esc to close',
  onThisPage: 'On this page',
  inThisSection: 'In this section',
  previous: 'Previous',
  next: 'Next',
  menu: 'Contents',
  closeMenu: 'Close contents',
  toggleTheme: 'Toggle dark/light mode',
  switchLanguage: '中文',
  switchLanguageLabel: '切换到中文',
  loading: 'Loading…',
  loadError: 'Failed to load this page',
  retry: 'Retry',
  emptyPage: 'This page has not been written yet.',
  untranslated: 'This page has not been translated into English yet. The Chinese original is shown below.',
  stale: 'The Chinese original has changed since this translation was made; it may be out of date.',
  notFoundTitle: 'Page not found',
  notFoundBody: 'There is no page at this address.',
  backHome: 'Back to home',
  copy: 'Copy',
  copied: 'Copied',
  pagesWritten: (done: number, total: number, translated: number) => `${done} of ${total} pages written · ${translated} translated into English`,
  subsections: (n: number) => `${n} subsection${n === 1 ? '' : 's'}`,
  devDiagnostics: (n: number) => `The build found ${n} problem(s) (shown in dev mode only)`,
};

export type Strings = typeof zh;
export const strings: Record<Lang, Strings> = { zh, en };

/** The other language, for the language toggle. */
export function otherLang(lang: Lang): Lang {
  return lang === 'zh' ? 'en' : 'zh';
}

/** Current UI language from the URL (falls back to the default language outside /:lang routes). */
export function useLang(): Lang {
  const { lang } = useParams();
  return isLang(lang) ? lang : siteConfig.defaultLanguage;
}

export function useStrings(): Strings {
  return strings[useLang()];
}
