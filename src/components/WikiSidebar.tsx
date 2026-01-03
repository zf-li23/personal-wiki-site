import { Link, useLocation } from 'react-router-dom';
import { WikiPage } from '@/data/wikiData';
import { TOCItem, cn } from '@/lib/utils';
import { useState, useEffect } from 'react';
import { ChevronRight, ChevronDown } from 'lucide-react';

interface WikiSidebarProps {
  data: WikiPage[];
  toc?: TOCItem[];
  basePath?: string;
  level?: number;
  indexPrefix?: string;
}

export default function WikiSidebar({ 
  data, 
  toc, 
  basePath = '/wiki', 
  level = 0,
  indexPrefix = ''
}: WikiSidebarProps) {
  const location = useLocation();
  
  // State to track expanded items
  // We use a map of path -> boolean
  const [expanded, setExpanded] = useState<Record<string, boolean>>({});

  // Auto-expand active path on mount and when location changes
  useEffect(() => {
    const currentPath = location.pathname;
    
    const parts = currentPath.split('/').filter(Boolean);
    
    const keysToExpand: Record<string, boolean> = {};
    let pathAccumulator = '';
    
    parts.forEach((part, index) => {
        if (index === 0 && part === 'wiki') {
            pathAccumulator = '/wiki';
        } else {
            pathAccumulator = `${pathAccumulator}/${part}`;
        }
        // Expand this path
        keysToExpand[pathAccumulator] = true;
    });
    
    setExpanded(prev => ({ ...prev, ...keysToExpand }));
  }, [location.pathname]);

  const toggleExpand = (path: string, e: React.MouseEvent) => {
    e.preventDefault();
    e.stopPropagation();
    setExpanded(prev => ({
      ...prev,
      [path]: !prev[path]
    }));
  };

  const handleLinkClick = (path: string, hasChildren: boolean) => {
    if (hasChildren) {
        setExpanded(prev => ({
            ...prev,
            [path]: true
        }));
    }
  };

  return (
    <nav className={cn("space-y-1", level > 0 && "mt-1")}>
      {data.map((page, index) => {
        const currentPath = `${basePath}/${page.slug}`;
        // Decode location.pathname to ensure matching works with Chinese characters
        const decodedLocationPath = decodeURIComponent(location.pathname);
        // Also handle potential trailing slashes for robustness
        const normalize = (p: string) => p.replace(/\/$/, '');
        const isActive = normalize(decodedLocationPath) === normalize(currentPath);
        
        const currentIndex = indexPrefix ? `${indexPrefix}.${index + 1}` : `${index + 1}`;
        const hasChildren = page.children && page.children.length > 0;
        const isExpanded = expanded[currentPath]; // Use raw path for state keys

        return (
          <div key={page.id} className="relative">
            <div className="flex items-center group">
                {hasChildren && (
                    <button 
                        onClick={(e) => toggleExpand(currentPath, e)}
                        className="absolute left-0 p-1 hover:bg-accent rounded-sm text-muted-foreground z-10"
                        style={{ left: `${level * 12}px` }}
                    >
                        {isExpanded ? <ChevronDown className="h-3 w-3" /> : <ChevronRight className="h-3 w-3" />}
                    </button>
                )}
                <Link
                  to={currentPath}
                  onClick={() => handleLinkClick(currentPath, !!hasChildren)}
                  className={cn(
                    "flex-1 block py-1.5 pr-2 text-sm hover:text-primary transition-colors rounded-r-md relative",
                    isActive 
                      ? "font-medium text-primary bg-accent/50 border-l-2 border-primary -ml-[1px]" 
                      : "text-muted-foreground border-l border-transparent"
                  )}
                  style={{ paddingLeft: `${level * 12 + (hasChildren ? 20 : 12)}px` }}
                >
                  <span className="mr-2 opacity-70 text-xs font-mono">{currentIndex}</span>
                  {page.title}
                </Link>
            </div>
            
            {/* Render TOC if active and has items */}
            {isActive && toc && toc.length > 0 && (
              <div className="my-1 space-y-1 border-l border-border ml-4" style={{ marginLeft: `${level * 12 + 12}px` }}>
                {toc.map((item) => (
                  <a
                    key={item.id}
                    href={`#${item.id}`}
                    onClick={(e) => {
                      e.preventDefault();
                      const element = document.getElementById(item.id);
                      if (element) {
                        element.scrollIntoView({ behavior: 'smooth' });
                      }
                    }}
                    className={cn(
                      "block py-1 text-xs hover:text-primary transition-colors text-muted-foreground pl-4 border-l border-transparent hover:border-muted-foreground/50 truncate",
                      item.level === 3 && "pl-6"
                    )}
                    title={item.text}
                  >
                    {item.text}
                  </a>
                ))}
              </div>
            )}

            {hasChildren && isExpanded && (
              <WikiSidebar 
                data={page.children!} 
                toc={toc} 
                basePath={currentPath} 
                level={level + 1}
                indexPrefix={currentIndex}
              />
            )}
          </div>
        );
      })}
    </nav>
  );
}
