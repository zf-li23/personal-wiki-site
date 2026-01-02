import { useParams, Navigate } from 'react-router-dom';
import { wikiData, findPageByPath } from '@/data/wikiData';
import WikiSidebar from '@/components/WikiSidebar';
import MarkdownRenderer from '@/components/MarkdownRenderer';
import { extractHeaders } from '@/lib/utils';
import { useMemo } from 'react';

export default function Wiki() {
  const params = useParams();
  const path = params['*'] || '';

  const result = useMemo(() => findPageByPath(path), [path]);
  const page = result?.page;
  const ancestors = result?.ancestors || [];
  
  const toc = useMemo(() => {
    if (page?.content) {
      return extractHeaders(page.content);
    }
    return [];
  }, [page]);

  // Construct Composite Title
  // Format: Grandparent(Clean) - Parent(Clean) - File(Number-trimmed + Name)
  const compositeTitle = useMemo(() => {
    if (!page) return '';
    
    const parts: string[] = [];
    
    // Add ancestors (Clean titles)
    ancestors.forEach(ancestor => {
       parts.push(ancestor.title);
    });
    
    // Add current page
    // Logic: "Ancestor1 - Ancestor2 - RelativeNumbering.Title"
    // Only keep the first 2 ancestors as prefix.
    
    const prefixParts = parts.slice(0, 2);
    
    const pageSlug = page.slug; // "1.1.1.Title"
    let displayTitle = page.title; // "Title" (Cleaned by wikiData)
    
    // Extract numbering from slug
    // Slug is the full path segments joined by /
    // We want the last segment's numbering
    const lastSegment = pageSlug.split('/').pop() || '';
    const slugMatch = lastSegment.match(/^([\d\.]+)\.?/);
    let pageNumbering = slugMatch ? slugMatch[1] : ''; // "1.1.1" or "1.1.1."
    
    // Remove trailing dot if it exists in the captured group
    if (pageNumbering.endsWith('.')) {
        pageNumbering = pageNumbering.slice(0, -1);
    }
    
    if (pageNumbering) {
        let relativeNumbering = pageNumbering;
        
        // "去除前两个标号" -> Remove the first two components of the numbering
        // e.g. "1.1.1" -> remove "1.1" -> "1"
        // "1.1.2.1" -> remove "1.1" -> "2.1"
        // "1.2" -> remove "1.2" -> "" (Wait, if depth is 2, do we show numbering?)
        // User said: "离散数学 - 数理逻辑 - 2.1.命题逻辑的等值" (Depth 4: 1.1.2.1)
        // Ancestors: 1.离散, 1.1.数理, 1.1.2.等值
        // Wait, "1.1.2.1" relative to "1.1" is "2.1".
        
        const numberingParts = pageNumbering.split('.');
        if (numberingParts.length > 2) {
             relativeNumbering = numberingParts.slice(2).join('.');
        } else {
             // If depth <= 2, maybe we don't show numbering or show full?
             // User example: "离散数学 - 数理逻辑 - 1.命题的基本概念" (Depth 3: 1.1.1)
             // 1.1.1 -> slice(2) -> "1". Correct.
             relativeNumbering = numberingParts.slice(2).join('.');
        }
        
        if (relativeNumbering) {
            displayTitle = `${relativeNumbering}.${displayTitle}`;
        }
    }
    
    // Combine: Prefix (max 2) + DisplayTitle
    const finalParts = [...prefixParts, displayTitle];
    return finalParts.join(' - ');
  }, [page, ancestors]);

  // Redirect to first page if at root /wiki
  if (!path && wikiData.length > 0) {
     const firstPage = wikiData[0];
     return <Navigate to={`/wiki/${firstPage.slug}`} replace />;
  }

  return (
    <div className="flex min-h-[calc(100vh-3.5rem)]">
      <aside className="w-80 border-r border-border hidden md:block py-6 pr-4 pl-2 bg-muted/10 sticky top-14 h-[calc(100vh-3.5rem)] overflow-y-auto">
         <WikiSidebar data={wikiData} toc={toc} />
      </aside>
      <main className="flex-1 p-4 md:p-10 min-w-0 overflow-x-hidden">
        <div className="max-w-4xl mx-auto w-full">
          {!page ? (
            <div className="py-10">
              <h1 className="text-2xl font-bold text-destructive">Page Not Found</h1>
              <p className="mt-4 text-muted-foreground">The requested wiki page "{path}" could not be found.</p>
            </div>
          ) : (
            <>
              <div className="mb-8 pb-4 border-b border-border">
                <h1 className="text-4xl font-bold tracking-tight">{compositeTitle}</h1>
              </div>
              {page.content ? (
                <MarkdownRenderer content={page.content} currentPath={page.slug} />
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
