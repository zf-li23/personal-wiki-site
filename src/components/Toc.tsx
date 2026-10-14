import { useEffect, useState } from 'react';
import { useStrings } from '../i18n.ts';
import { cn } from '../lib/cn.ts';
import type { TocHeading } from '../shared/types.ts';

/** "On this page" list with the heading currently in view highlighted. */
export function Toc({ headings }: { headings: TocHeading[] }) {
  const t = useStrings();
  const [active, setActive] = useState<string | null>(null);

  useEffect(() => {
    const elements = headings.map((h) => document.getElementById(h.id)).filter((e): e is HTMLElement => !!e);
    if (!elements.length) return;
    const visible = new Set<string>();
    const observer = new IntersectionObserver(
      (entries) => {
        for (const e of entries) {
          if (e.isIntersecting) visible.add(e.target.id);
          else visible.delete(e.target.id);
        }
        const first = elements.find((el) => visible.has(el.id));
        if (first) setActive(first.id);
      },
      { rootMargin: '-64px 0px -60% 0px' },
    );
    for (const el of elements) observer.observe(el);
    return () => observer.disconnect();
  }, [headings]);

  if (!headings.length) return null;
  return (
    <nav className="text-sm" aria-label={t.onThisPage}>
      <p className="mb-2 font-medium">{t.onThisPage}</p>
      <ul className="space-y-1 border-l border-border">
        {headings.map((h) => (
          <li key={h.id}>
            <a
              href={`#${h.id}`}
              className={cn(
                '-ml-px block border-l py-0.5 leading-snug transition-colors hover:text-foreground',
                h.depth === 3 ? 'pl-6' : 'pl-3',
                active === h.id ? 'border-foreground text-foreground' : 'border-transparent text-muted-foreground',
              )}
            >
              {h.text}
            </a>
          </li>
        ))}
      </ul>
    </nav>
  );
}
