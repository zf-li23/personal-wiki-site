import { useParams, Link } from 'react-router-dom';
import { wikiData, findPageByPath } from '@/data/wikiData';
import WikiSidebar from '@/components/WikiSidebar';
import MarkdownRenderer from '@/components/MarkdownRenderer';
import { extractHeaders } from '@/lib/utils';
import { useMemo, useState, useEffect } from 'react';
import { Menu, X } from 'lucide-react';

export default function Wiki() {
  const params = useParams();
  const path = params['*'] || '';
  const [isMobileMenuOpen, setIsMobileMenuOpen] = useState(false);

  const result = useMemo(() => findPageByPath(path), [path]);
  const page = result?.page;
  const ancestors = result?.ancestors || [];
  
  const toc = useMemo(() => {
    if (page?.content) {
      return extractHeaders(page.content);
    }
    return [];
  }, [page]);

  // Scroll to top on path change
  useEffect(() => {
    window.scrollTo(0, 0);
    setIsMobileMenuOpen(false);
  }, [path]);

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

  return (
    <div className="flex min-h-[calc(100vh-3.5rem)] relative">
      {/* Mobile Menu Toggle */}
      <button 
        className="md:hidden fixed bottom-6 right-6 z-50 p-3 bg-primary text-primary-foreground rounded-full shadow-lg hover:bg-primary/90 transition-colors"
        onClick={() => setIsMobileMenuOpen(!isMobileMenuOpen)}
        aria-label="Toggle navigation"
      >
        {isMobileMenuOpen ? <X className="h-6 w-6" /> : <Menu className="h-6 w-6" />}
      </button>

      {/* Mobile Sidebar Overlay */}
      {isMobileMenuOpen && (
        <div className="fixed inset-0 z-40 bg-background/80 backdrop-blur-sm md:hidden" onClick={() => setIsMobileMenuOpen(false)}>
          <aside 
            className="absolute left-0 top-14 bottom-0 w-3/4 max-w-xs bg-background border-r border-border overflow-y-auto p-4 shadow-xl" 
            onClick={e => e.stopPropagation()}
          >
             <WikiSidebar data={wikiData} toc={toc} />
          </aside>
        </div>
      )}

      {/* Desktop Sidebar */}
      <aside className="w-80 border-r border-border hidden md:block py-6 pr-4 pl-2 bg-muted/10 sticky top-14 h-[calc(100vh-3.5rem)] overflow-y-auto">
         <WikiSidebar data={wikiData} toc={toc} />
      </aside>

      <main className="flex-1 p-4 md:p-10 min-w-0 overflow-x-hidden">
        <div className="max-w-4xl mx-auto w-full">
          {!path ? (
             <div className="py-10 text-center">
                <h1 className="text-3xl font-bold mb-4">Welcome to the Wiki</h1>
                <p className="text-muted-foreground mb-8">Select a page from the sidebar to start reading.</p>
                <div className="grid gap-4 sm:grid-cols-2 text-left">
                    {wikiData.map(rootPage => (
                        <Link 
                          key={rootPage.slug}
                          to={rootPage.slug}
                          className="block p-4 rounded-lg border border-border bg-card hover:bg-accent/50 transition-colors group"
                        >
                          <h3 className="font-semibold text-lg mb-1 group-hover:text-primary transition-colors">
                            {rootPage.title}
                          </h3>
                          <p className="text-sm text-muted-foreground">
                            {rootPage.children && rootPage.children.length > 0 
                              ? `${rootPage.children.length} 个子章节` 
                              : '文档'}
                          </p>
                        </Link>
                    ))}
                </div>
             </div>
          ) : !page ? (
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

              {/* Automatic Directory for Folder Pages */}
              {page.children && page.children.length > 0 && (
                <div className="mt-12 pt-8 border-t border-border">
                  <h2 className="text-2xl font-bold mb-6">目录</h2>
                  <div className="grid gap-4 sm:grid-cols-2">
                    {page.children.map(child => {
                      // Extract numbering from slug (e.g. "1.1.Logic" -> "1.1")
                      const childNumbering = child.slug.split('/').pop()?.match(/^([\d\.]+)/)?.[1] || '';
                      // If title doesn't start with numbering, prepend it
                      const displayTitle = childNumbering && !child.title.startsWith(childNumbering) 
                        ? `${childNumbering} ${child.title}` 
                        : child.title;

                      return (
                        <Link 
                          key={child.slug}
                          to={child.slug}
                          className="block p-4 rounded-lg border border-border bg-card hover:bg-accent/50 transition-colors group"
                        >
                          <h3 className="font-semibold text-lg mb-1 group-hover:text-primary transition-colors">
                            {displayTitle}
                          </h3>
                          <p className="text-sm text-muted-foreground">
                            {child.children && child.children.length > 0 
                              ? `${child.children.length} 个子章节` 
                              : '文档'}
                          </p>
                        </Link>
                      );
                    })}
                  </div>
                </div>
              )}
            </>
          )}
        </div>
      </main>
    </div>
  );
}
