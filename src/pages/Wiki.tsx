import { useParams, Navigate } from 'react-router-dom';
import { wikiData, findPageByPath } from '@/data/wikiData';
import WikiSidebar from '@/components/WikiSidebar';
import MarkdownRenderer from '@/components/MarkdownRenderer';
import { extractHeaders } from '@/lib/utils';
import { useMemo } from 'react';

export default function Wiki() {
  const params = useParams();
  const path = params['*'] || '';

  // Redirect to first page if at root /wiki
  if (!path && wikiData.length > 0) {
     const firstPage = wikiData[0];
     return <Navigate to={`/wiki/${firstPage.slug}`} replace />;
  }

  const page = useMemo(() => findPageByPath(path), [path]);
  
  const toc = useMemo(() => {
    if (page?.content) {
      return extractHeaders(page.content);
    }
    return [];
  }, [page]);

  return (
    <div className="flex h-[calc(100vh-3.5rem)]">
      <aside className="w-80 border-r border-border overflow-y-auto hidden md:block py-6 pr-4 pl-2 bg-muted/10">
         <WikiSidebar data={wikiData} toc={toc} />
      </aside>
      <main className="flex-1 overflow-y-auto p-6 md:p-10 scroll-smooth">
        <div className="max-w-4xl mx-auto">
          {!page ? (
            <div className="py-10">
              <h1 className="text-2xl font-bold text-destructive">Page Not Found</h1>
              <p className="mt-4 text-muted-foreground">The requested wiki page "{path}" could not be found.</p>
            </div>
          ) : (
            <>
              <div className="mb-8 pb-4 border-b border-border">
                <h1 className="text-4xl font-bold tracking-tight">{page.title}</h1>
              </div>
              {page.content ? (
                <MarkdownRenderer content={page.content} />
              ) : (
                <p className="text-muted-foreground italic">This page has no content yet.</p>
              )}
            </>
          )}
        </div>
      </main>
    </div>
  );
}
