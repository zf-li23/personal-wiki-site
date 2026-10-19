/**
 * Renders a page's pre-built HTML (see scripts/wiki/markdown.ts for the markup
 * contract) and adds the few interactive behaviours it needs:
 *   button[data-copy]   copies the code of its .code-block
 *   button[data-code-tab]  switches the Python / R tabs of a plot's source
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
      if (tab) {
        const group = tab.closest('.wiki-code-tabs');
        for (const b of group?.querySelectorAll<HTMLButtonElement>('button[data-code-tab]') ?? []) {
          const on = b === tab;
          b.classList.toggle('active', on);
          b.setAttribute('aria-selected', String(on));
        }
        for (const p of group?.querySelectorAll<HTMLElement>('[data-code-panel]') ?? []) p.hidden = p.dataset.codePanel !== tab.dataset.codeTab;
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
