import { Search, X } from 'lucide-react';
import { useEffect, useMemo, useRef, useState } from 'react';
import { useNavigate } from 'react-router';
import { type SearchHit, loadSearchIndex, search } from '../content/search.ts';
import { useLang, useStrings } from '../i18n.ts';
import { cn } from '../lib/cn.ts';
import { pagePath } from '../shared/page-id.ts';
import type { SearchEntry } from '../shared/types.ts';

export function SearchDialog({ open, onClose }: { open: boolean; onClose: () => void }) {
  const lang = useLang();
  const t = useStrings();
  const navigate = useNavigate();
  const input = useRef<HTMLInputElement>(null);
  const [index, setIndex] = useState<{ lang: string; entries: SearchEntry[] } | null>(null);
  const entries = index?.lang === lang ? index.entries : null;
  const [query, setQuery] = useState('');
  const [selected, setSelected] = useState(0);

  useEffect(() => {
    if (!open) return;
    let alive = true;
    loadSearchIndex(lang).then(
      (e) => alive && setIndex({ lang, entries: e }),
      () => alive && setIndex({ lang, entries: [] }),
    );
    input.current?.focus();
    return () => {
      alive = false;
    };
  }, [open, lang]);

  const hits: SearchHit[] = useMemo(() => (entries ? search(entries, query) : []), [entries, query]);

  if (!open) return null;

  const go = (hit: SearchHit | undefined) => {
    if (!hit) return;
    onClose();
    navigate(pagePath(lang, hit.entry.id));
  };

  return (
    <div className="fixed inset-0 z-50 bg-background/70 backdrop-blur-sm" onClick={onClose} role="presentation">
      <div
        role="dialog"
        aria-modal="true"
        aria-label={t.search}
        className="mx-auto mt-[10vh] w-[min(42rem,calc(100%-2rem))] overflow-hidden rounded-xl border border-border bg-card shadow-2xl"
        onClick={(e) => e.stopPropagation()}
      >
        <div className="flex items-center gap-2 border-b border-border px-4">
          <Search size={18} className="text-muted-foreground" />
          <input
            ref={input}
            value={query}
            onChange={(e) => {
              setQuery(e.target.value);
              setSelected(0);
            }}
            onKeyDown={(e) => {
              if (e.key === 'Escape') onClose();
              else if (e.key === 'ArrowDown') {
                e.preventDefault();
                setSelected((s) => Math.min(s + 1, hits.length - 1));
              } else if (e.key === 'ArrowUp') {
                e.preventDefault();
                setSelected((s) => Math.max(s - 1, 0));
              } else if (e.key === 'Enter') go(hits[selected]);
            }}
            placeholder={t.searchPlaceholder}
            className="h-12 flex-1 bg-transparent text-base outline-none placeholder:text-muted-foreground"
          />
          <button type="button" onClick={onClose} className="rounded p-1 text-muted-foreground hover:bg-accent" aria-label="Close">
            <X size={18} />
          </button>
        </div>
        <div className="max-h-[60vh] overflow-y-auto p-2">
          {!entries && <p className="p-3 text-sm text-muted-foreground">{t.searchLoading}</p>}
          {entries && query.trim() && !hits.length && <p className="p-3 text-sm text-muted-foreground">{t.searchNoResults}</p>}
          <ul>
            {hits.map((hit, i) => (
              <li key={hit.entry.id}>
                <button
                  type="button"
                  onMouseEnter={() => setSelected(i)}
                  onClick={() => go(hit)}
                  className={cn('block w-full rounded-md px-3 py-2 text-left', i === selected && 'bg-accent')}
                >
                  <span className="block text-sm font-medium">
                    <span className="mr-2 font-mono text-xs text-muted-foreground">{hit.entry.id}</span>
                    {hit.entry.title}
                  </span>
                  {hit.entry.trail && <span className="block text-xs text-muted-foreground">{hit.entry.trail}</span>}
                  {hit.snippet && <span className="mt-1 line-clamp-2 block text-xs text-muted-foreground">{hit.snippet}</span>}
                </button>
              </li>
            ))}
          </ul>
        </div>
        <p className="border-t border-border px-4 py-2 text-xs text-muted-foreground">{t.searchHint}</p>
      </div>
    </div>
  );
}
