/**
 * Renders a page's pre-built HTML (see scripts/wiki/markdown.ts for the markup
 * contract) and adds the few interactive behaviours it needs:
 *   button[data-copy]   copies the code of its .code-block
 *   button[data-code-tab]  switches code tabs (C++ / Python, a plot's Python / R); the chosen
 *                       language applies to every tab group and is remembered
 *   a[data-internal]    client-side navigation between wiki pages
 *   .wiki-mermaid       rendered with Mermaid (lazy-loaded), re-rendered on theme change
 */
import { memo, useEffect, useRef } from 'react';
import { useNavigate } from 'react-router';
import { BASE_PATH } from '../../site.config.ts';
import { useStrings } from '../i18n.ts';
import { useTheme } from '../lib/theme.tsx';
import { renderMermaidBlocks } from '../lib/mermaid.ts';
import type { Lang } from '../../site.config.ts';
import { ARTICLE_CLASS } from '../shared/article.ts';
import { LinkPreviewCard, useLinkPreview } from './LinkPreview.tsx';

interface ArticleProps {
  html: string;
  /** Language of the HTML (the source language on untranslated pages). */
  lang: string;
}

const CODE_LANG_KEY = 'wiki-code-lang';

/** Show `lang` in every tab group of the article that has it. */
function selectCodeTab(root: HTMLElement, lang: string): void {
  for (const group of root.querySelectorAll<HTMLElement>('.wiki-code-tabs')) {
    const tabs = [...group.querySelectorAll<HTMLButtonElement>(':scope > .wiki-code-tablist > button[data-code-tab]')];
    if (!tabs.some((b) => b.dataset.codeTab === lang)) continue;
    for (const b of tabs) {
      const on = b.dataset.codeTab === lang;
      b.classList.toggle('active', on);
      b.setAttribute('aria-selected', String(on));
    }
    for (const p of group.querySelectorAll<HTMLElement>(':scope > [data-code-panel]')) p.hidden = p.dataset.codePanel !== lang;
  }
}

// Memoised on `html` so React never re-applies innerHTML (which would discard rendered diagrams).
const ArticleBody = memo(function ArticleBody({ html, lang }: ArticleProps) {
  return <div className={ARTICLE_CLASS} lang={lang} dangerouslySetInnerHTML={{ __html: html }} />;
});

export function Article({ html, lang, readerLang, pageId }: ArticleProps & { readerLang: Lang; pageId: string }) {
  const ref = useRef<HTMLDivElement>(null);
  const navigate = useNavigate();
  const t = useStrings();
  const { theme } = useTheme();

  useEffect(() => {
    const root = ref.current;
    if (!root) return;
    // The build emits English button labels; localise them.
    for (const b of root.querySelectorAll<HTMLButtonElement>('button[data-copy]')) b.textContent = t.copy;
    try {
      const preferred = localStorage.getItem(CODE_LANG_KEY);
      if (preferred) selectCodeTab(root, preferred);
    } catch {
      // storage unavailable: keep the first tab
    }
    const onClick = (e: MouseEvent) => {
      const target = e.target as HTMLElement;
      const copy = target.closest<HTMLButtonElement>('button[data-copy]');
      if (copy) {
        const code = copy.closest('.code-block')?.querySelector('pre')?.textContent ?? '';
        navigator.clipboard?.writeText(code).then(
          () => {
            copy.textContent = t.copied;
            window.setTimeout(() => (copy.textContent = t.copy), 1500);
          },
          () => undefined,
        );
        return;
      }
      const tab = target.closest<HTMLButtonElement>('button[data-code-tab]');
      if (tab?.dataset.codeTab) {
        selectCodeTab(root, tab.dataset.codeTab);
        try {
          localStorage.setItem(CODE_LANG_KEY, tab.dataset.codeTab);
        } catch {
          // storage unavailable: the choice lasts for this page only
        }
        return;
      }
      const link = target.closest<HTMLAnchorElement>('a[data-internal]');
      if (link && e.button === 0 && !e.metaKey && !e.ctrlKey && !e.shiftKey && !e.altKey) {
        const href = link.getAttribute('href') ?? '';
        if (href.startsWith(BASE_PATH)) {
          e.preventDefault();
          navigate(`/${href.slice(BASE_PATH.length)}`);
        }
      }
    };
    root.addEventListener('click', onClick);
    return () => root.removeEventListener('click', onClick);
  }, [navigate, t, html]);

  useEffect(() => {
    if (ref.current) void renderMermaidBlocks(ref.current, theme);
  }, [html, theme]);

  const { preview, keep, close, dismiss } = useLinkPreview(ref, readerLang, pageId);

  return (
    <div ref={ref}>
      {preview && <LinkPreviewCard preview={preview} onEnter={keep} onLeave={close} onNavigate={dismiss} />}
      <ArticleBody html={html} lang={lang} />
    </div>
  );
}
