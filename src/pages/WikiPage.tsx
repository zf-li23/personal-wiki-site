import { X } from 'lucide-react';
import { useEffect, useLayoutEffect, useRef } from 'react';
import { useLocation, useParams } from 'react-router';
import { type Lang } from '../../site.config.ts';
import { Article } from '../components/Article.tsx';
import { Breadcrumbs, ChildList, DevDiagnostics, PrevNext, StatusBanner } from '../components/PageParts.tsx';
import { Sidebar } from '../components/Sidebar.tsx';
import { Toc } from '../components/Toc.tsx';
import { reloadPage, usePage } from '../content/pages.ts';
import { findNode } from '../content/site.ts';
import { useLang, useStrings } from '../i18n.ts';
import type { NavNode, PagePayload } from '../shared/types.ts';
import { useLayout } from './Layout.tsx';
import { NotFound } from './NotFound.tsx';

export function WikiPage() {
  const { id = '' } = useParams();
  const lang = useLang();
  const node = findNode(id);
  const { menuOpen, setMenuOpen } = useLayout();

  if (!node) return <NotFound />;

  return (
    <div className="mx-auto flex max-w-[90rem]">
      <aside className="sticky top-14 hidden h-[calc(100vh-3.5rem)] w-72 shrink-0 overflow-y-auto border-r border-border px-3 py-6 lg:block">
        <Sidebar activeId={id} />
      </aside>

      {menuOpen && (
        <div className="fixed inset-0 z-50 bg-background/70 backdrop-blur-sm lg:hidden" onClick={() => setMenuOpen(false)} role="presentation">
          <aside
            className="absolute inset-y-0 left-0 w-[min(20rem,85vw)] overflow-y-auto border-r border-border bg-background px-3 py-4 shadow-xl"
            onClick={(e) => e.stopPropagation()}
          >
            <div className="mb-2 flex justify-end">
              <button type="button" onClick={() => setMenuOpen(false)} className="rounded p-1 text-muted-foreground hover:bg-accent" aria-label="Close">
                <X size={18} />
              </button>
            </div>
            <Sidebar activeId={id} onNavigate={() => setMenuOpen(false)} />
          </aside>
        </div>
      )}

      <PageContent key={`${lang}/${id}`} lang={lang} node={node} />
    </div>
  );
}

function PageContent({ lang, node }: { lang: Lang; node: NavNode }) {
  const t = useStrings();
  const entry = usePage(lang, node.id);
  const payload: PagePayload | undefined = entry && 'payload' in entry ? entry.payload : undefined;
  useScrollToLocation(payload?.html);

  useEffect(() => {
    document.title = `${node.title[lang]} · ${t.siteTitle}`;
  }, [node, lang, t]);

  return (
    <>
      <main className="min-w-0 flex-1 px-4 py-8 md:px-10">
        <div className="mx-auto max-w-3xl">
          <Breadcrumbs id={node.id} />
          <h1 className="text-3xl font-bold tracking-tight sm:text-4xl">
            <span className="mr-3 font-mono text-xl text-muted-foreground sm:text-2xl">{node.id}</span>
            {node.title[lang]}
          </h1>
          <div className="mt-8">
            {!entry && <p className="text-muted-foreground">{t.loading}</p>}
            {entry && 'error' in entry && (
              <p className="text-red-600 dark:text-red-400">
                {t.loadError} ({entry.error}).{' '}
                <button type="button" className="underline" onClick={() => reloadPage(lang, node.id)}>
                  {t.retry}
                </button>
              </p>
            )}
            {payload && (
              <>
                <DevDiagnostics items={payload.diagnostics} />
                <StatusBanner status={payload.status} />
                {payload.html ? <Article html={payload.html} lang={payload.contentLang} /> : <p className="italic text-muted-foreground">{t.emptyPage}</p>}
              </>
            )}
          </div>
          <ChildList node={node} />
          <PrevNext id={node.id} />
        </div>
      </main>
      <aside className="sticky top-14 hidden h-[calc(100vh-3.5rem)] w-60 shrink-0 overflow-y-auto py-8 pr-4 xl:block">
        {payload && <Toc headings={payload.headings} />}
      </aside>
    </>
  );
}

/** New page: scroll to the #hash target once the article is in the DOM, else to the top. */
function useScrollToLocation(html: string | undefined) {
  const location = useLocation();
  const lastPath = useRef<string | null>(null);
  useLayoutEffect(() => {
    if (html === undefined) return;
    const hash = decodeURIComponent(location.hash.slice(1));
    const target = hash ? document.getElementById(hash) : null;
    if (target) target.scrollIntoView();
    else if (lastPath.current !== location.pathname) window.scrollTo(0, 0);
    lastPath.current = location.pathname;
  }, [html, location.pathname, location.hash]);
}
