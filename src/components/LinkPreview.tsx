/**
 * Hover previews inside articles, like an e-book's footnote popups:
 *   a.wiki-ref / a[data-internal][href*="#"]   → the target statement, equation or section
 *   .concept-ref                                → the concept (zh / en) and its definition
 * Content comes from the target page's payload (cached), so no extra build data is needed.
 */
import { useEffect, useRef, useState } from 'react';
import { createPortal } from 'react-dom';
import { useNavigate } from 'react-router';
import { BASE_PATH, type Lang } from '../../site.config.ts';
import { loadConcepts } from '../content/concepts.ts';
import { fetchPage } from '../content/pages.ts';
import { findNode } from '../content/site.ts';
import { strings } from '../i18n.ts';
import { ARTICLE_CLASS } from '../shared/article.ts';

interface Preview {
  title?: string;
  html?: string;
  footer?: string;
  /** Anchor rectangle of the hovered link (viewport coordinates). */
  rect: DOMRect;
}

const SHOW_DELAY = 250;
const HIDE_DELAY = 200;
const docs = new Map<string, Document>();

function parsePayloadHtml(key: string, html: string): Document {
  let doc = docs.get(key);
  if (!doc) {
    doc = new DOMParser().parseFromString(`<body>${html}</body>`, 'text/html');
    docs.set(key, doc);
  }
  return doc;
}

/** The block a preview shows for an anchor: the statement/equation wrapper, or a heading plus what follows it. */
function excerptFor(root: ParentNode, anchor: string): string | null {
  const target = root.querySelector<HTMLElement>(`[id="${CSS.escape(anchor)}"]`);
  if (!target) return null;
  let block: Element = target;
  if (target.tagName === 'DFN') block = target.closest('p, li, .wiki-stmt') ?? target;
  const clone = block.cloneNode(true) as HTMLElement;
  let html = clone.outerHTML;
  if (/^H[2-6]$/.test(target.tagName)) {
    const next = target.nextElementSibling;
    html = `<p><strong>${target.textContent?.replace(/#$/, '') ?? ''}</strong></p>${next ? next.outerHTML : ''}`;
  }
  // Ids would duplicate the page's own anchors.
  return html.replace(/\sid="[^"]*"/g, '');
}

function parseHref(href: string, currentLang: Lang): { lang: Lang; id?: string; anchor: string } | null {
  if (href.startsWith('#')) return { lang: currentLang, anchor: decodeURIComponent(href.slice(1)) };
  if (!href.startsWith(BASE_PATH)) return null;
  const m = /^(zh|en)\/([\d.]+)\/#(.+)$/.exec(href.slice(BASE_PATH.length));
  return m ? { lang: m[1] as Lang, id: m[2], anchor: decodeURIComponent(m[3]) } : null;
}

async function buildPreview(el: HTMLElement, lang: Lang, pageId: string, root: HTMLElement): Promise<Omit<Preview, 'rect'> | null> {
  const t = strings[lang];
  const conceptId = el.dataset.concept;
  if (conceptId) {
    const concept = (await loadConcepts()).get(conceptId);
    if (!concept) return null;
    const title = lang === 'zh' ? `${concept.zh}（${concept.en}）` : `${concept.en} · ${concept.zh}`;
    if (!concept.site) return { title, footer: t.conceptUndefined };
    const where = findNode(concept.site.pageId);
    const footer = t.definedIn(`${concept.site.pageId} ${where?.title[lang] ?? ''}`);
    const payload = await fetchPage(lang, concept.site.pageId);
    const body = excerptFor(parsePayloadHtml(`${lang}/${payload.id}`, payload.html).body, concept.site.anchor);
    return { title, html: body ?? undefined, footer };
  }
  const target = parseHref(el.getAttribute('href') ?? '', lang);
  if (!target) return null;
  if (!target.id || target.id === pageId) {
    const body = excerptFor(root, target.anchor);
    return body ? { html: body } : null;
  }
  const payload = await fetchPage(target.lang, target.id);
  const body = excerptFor(parsePayloadHtml(`${target.lang}/${payload.id}`, payload.html).body, target.anchor);
  const where = findNode(target.id);
  return body ? { html: body, footer: `${target.id} ${where?.title[target.lang] ?? ''}` } : null;
}


export function useLinkPreview(root: React.RefObject<HTMLElement | null>, lang: Lang, pageId: string) {
  const [preview, setPreview] = useState<Preview | null>(null);
  const showTimer = useRef<number | undefined>(undefined);
  const hideTimer = useRef<number | undefined>(undefined);
  const current = useRef<Element | null>(null);

  useEffect(() => {
    const el = root.current;
    // Hover previews only make sense with a mouse.
    if (!el || !window.matchMedia('(hover: hover)').matches) return;
    const trigger = (e: Event) => (e.target as HTMLElement).closest<HTMLElement>('.concept-ref, a.wiki-ref, a[data-internal][href*="#"], a[href^="#"]:not(.heading-anchor)');
    const over = (e: MouseEvent) => {
      const link = trigger(e);
      if (!link || link === current.current) return;
      current.current = link;
      window.clearTimeout(hideTimer.current);
      window.clearTimeout(showTimer.current);
      showTimer.current = window.setTimeout(async () => {
        try {
          const content = await buildPreview(link, lang, pageId, el);
          if (content && current.current === link) setPreview({ ...content, rect: link.getBoundingClientRect() });
        } catch {
          // a missing preview is not worth an error
        }
      }, SHOW_DELAY);
    };
    const out = (e: MouseEvent) => {
      if (!trigger(e)) return;
      window.clearTimeout(showTimer.current);
      current.current = null;
      hideTimer.current = window.setTimeout(() => setPreview(null), HIDE_DELAY);
    };
    el.addEventListener('mouseover', over);
    el.addEventListener('mouseout', out);
    return () => {
      el.removeEventListener('mouseover', over);
      el.removeEventListener('mouseout', out);
      window.clearTimeout(showTimer.current);
      window.clearTimeout(hideTimer.current);
    };
  }, [lang, pageId, root]);

  const keep = () => window.clearTimeout(hideTimer.current);
  const close = () => (hideTimer.current = window.setTimeout(() => setPreview(null), HIDE_DELAY));
  return { preview, keep, close, dismiss: () => setPreview(null) };
}

export function LinkPreviewCard({ preview, onEnter, onLeave, onNavigate }: { preview: Preview; onEnter: () => void; onLeave: () => void; onNavigate: () => void }) {
  const navigate = useNavigate();
  const width = Math.min(480, window.innerWidth - 32);
  const left = Math.max(16, Math.min(preview.rect.left, window.innerWidth - width - 16));
  const below = preview.rect.bottom + 8;
  const placeAbove = below + 320 > window.innerHeight && preview.rect.top > 340;
  const style: React.CSSProperties = placeAbove
    ? { left, width, bottom: window.innerHeight - preview.rect.top + 8 }
    : { left, width, top: below };
  return createPortal(
    <div
      role="tooltip"
      className="fixed z-50 max-h-80 overflow-hidden rounded-lg border border-border bg-card p-4 text-sm shadow-xl"
      style={style}
      onMouseEnter={onEnter}
      onMouseLeave={onLeave}
      onClick={(e) => {
        const a = (e.target as HTMLElement).closest('a[data-internal]');
        const href = a?.getAttribute('href');
        if (href?.startsWith(BASE_PATH)) {
          e.preventDefault();
          onNavigate();
          navigate(`/${href.slice(BASE_PATH.length)}`);
        }
      }}
    >
      {preview.title && <p className="mb-2 font-semibold">{preview.title}</p>}
      {preview.html && <div className={`${ARTICLE_CLASS} wiki-preview text-sm`} dangerouslySetInnerHTML={{ __html: preview.html }} />}
      {preview.footer && <p className="mt-2 border-t border-border pt-2 text-xs text-muted-foreground">{preview.footer}</p>}
    </div>,
    document.body,
  );
}
