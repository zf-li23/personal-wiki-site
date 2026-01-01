import { Link, useLocation } from 'react-router-dom';
import { WikiPage } from '@/data/wikiData';
import { TOCItem, cn } from '@/lib/utils';

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

  return (
    <nav className={cn("space-y-1", level > 0 && "mt-1")}>
      {data.map((page, index) => {
        const currentPath = `${basePath}/${page.slug}`;
        const isActive = location.pathname === currentPath;
        const currentIndex = indexPrefix ? `${indexPrefix}.${index + 1}` : `${index + 1}`;

        return (
          <div key={page.id} className="relative">
            <Link
              to={currentPath}
              className={cn(
                "block py-1.5 pr-2 text-sm hover:text-primary transition-colors rounded-r-md",
                isActive 
                  ? "font-medium text-primary bg-accent/50 border-l-2 border-primary -ml-[1px]" 
                  : "text-muted-foreground border-l border-transparent"
              )}
              style={{ paddingLeft: `${level * 12 + 12}px` }}
            >
              <span className="mr-2 opacity-70 text-xs font-mono">{currentIndex}</span>
              {page.title}
            </Link>
            
            {isActive && toc && toc.length > 0 && (
              <div className="my-1 space-y-1 border-l border-border ml-4" style={{ marginLeft: `${level * 12 + 12}px` }}>
                {toc.map((item) => (
                  <a
                    key={item.id}
                    href={`#${item.id}`}
                    className={cn(
                      "block py-1 text-xs hover:text-primary transition-colors text-muted-foreground pl-4 border-l border-transparent hover:border-muted-foreground/50",
                      item.level === 3 && "pl-6"
                    )}
                  >
                    {item.text}
                  </a>
                ))}
              </div>
            )}

            {page.children && (
              <WikiSidebar 
                data={page.children} 
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
