import { ChevronRight } from 'lucide-react';
import { useMemo, useState } from 'react';
import { NavLink } from 'react-router';
import { ancestorsOf, site } from '../content/site.ts';
import { useLang } from '../i18n.ts';
import { cn } from '../lib/cn.ts';
import type { NavNode } from '../shared/types.ts';
import { pagePath } from '../shared/page-id.ts';

interface SidebarProps {
  activeId?: string;
  onNavigate?: () => void;
}

/** Navigation tree. The active page's ancestors are expanded automatically. */
export function Sidebar({ activeId, onNavigate }: SidebarProps) {
  // Explicit user choices win; otherwise the active page and its ancestors are open.
  const [toggled, setToggled] = useState<ReadonlyMap<string, boolean>>(new Map());
  const autoOpen = useMemo(() => new Set(activeId ? [...ancestorsOf(activeId).map((a) => a.id), activeId] : []), [activeId]);
  const isOpen = (id: string) => toggled.get(id) ?? autoOpen.has(id);
  const toggle = (id: string) => setToggled((prev) => new Map(prev).set(id, !(prev.get(id) ?? autoOpen.has(id))));

  return (
    <nav className="text-sm">
      <Tree nodes={site.nav} depth={0} activeId={activeId} isOpen={isOpen} toggle={toggle} onNavigate={onNavigate} />
    </nav>
  );
}

interface TreeProps {
  nodes: NavNode[];
  depth: number;
  activeId?: string;
  isOpen: (id: string) => boolean;
  toggle: (id: string) => void;
  onNavigate?: () => void;
}

function Tree({ nodes, depth, activeId, isOpen, toggle, onNavigate }: TreeProps) {
  const lang = useLang();
  return (
    <ul className={cn(depth > 0 && 'ml-3 border-l border-border pl-2')}>
      {nodes.map((node) => {
        const open = isOpen(node.id);
        const hasChildren = node.children.length > 0;
        const placeholder = node.status[lang] === 'empty';
        return (
          <li key={node.id}>
            <div className="flex items-start">
              {hasChildren ? (
                <button
                  type="button"
                  onClick={() => toggle(node.id)}
                  className="mt-1 rounded p-0.5 text-muted-foreground hover:bg-accent"
                  aria-label={node.title[lang]}
                  aria-expanded={open}
                >
                  <ChevronRight size={14} className={cn('transition-transform', open && 'rotate-90')} />
                </button>
              ) : (
                <span className="w-[18px] shrink-0" />
              )}
              <NavLink
                to={pagePath(lang, node.id)}
                onClick={onNavigate}
                className={({ isActive }) =>
                  cn(
                    'flex-1 rounded px-1.5 py-1 leading-snug transition-colors hover:bg-accent hover:text-foreground',
                    isActive || node.id === activeId ? 'bg-accent font-medium text-foreground' : 'text-muted-foreground',
                    placeholder && 'opacity-60',
                  )
                }
                end
              >
                <span className="mr-1.5 font-mono text-xs opacity-70">{node.id}</span>
                {node.title[lang]}
              </NavLink>
            </div>
            {hasChildren && open && (
              <Tree nodes={node.children} depth={depth + 1} activeId={activeId} isOpen={isOpen} toggle={toggle} onNavigate={onNavigate} />
            )}
          </li>
        );
      })}
    </ul>
  );
}
