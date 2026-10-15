import { useEffect } from 'react';
import { Link } from 'react-router';
import { readingOrder, site } from '../content/site.ts';
import { useLang, useStrings } from '../i18n.ts';
import { cn } from '../lib/cn.ts';
import { pagePath } from '../shared/page-id.ts';

export function HomePage() {
  const lang = useLang();
  const t = useStrings();
  // Each page is written in one language (status "source") and translated into the others.
  const written = readingOrder.filter((n) => Object.values(n.status).includes('source')).length;
  const translated = readingOrder.filter((n) => Object.values(n.status).some((s) => s === 'translated' || s === 'stale')).length;

  useEffect(() => {
    document.title = t.siteTitle;
  }, [t]);

  return (
    <main className="mx-auto max-w-6xl px-4 py-12 md:py-16">
      <section className="max-w-3xl">
        <h1 className="text-4xl font-bold tracking-tight sm:text-5xl">{t.siteTitle}</h1>
        <p className="mt-4 text-lg leading-relaxed text-muted-foreground">{t.siteDescription}</p>
        <p className="mt-2 text-sm text-muted-foreground">{t.pagesWritten(written, readingOrder.length, translated)}</p>
      </section>

      <section className="mt-12 grid gap-5 md:grid-cols-2">
        {site.nav.map((root, i) => (
          <article
            key={root.id}
            // An odd last card spans the full row instead of leaving a hole in the two-column grid.
            className={cn('rounded-xl border border-border bg-card p-5', i === site.nav.length - 1 && i % 2 === 0 && 'md:col-span-2')}
          >
            <Link to={pagePath(lang, root.id)} className="group block">
              <span className="font-mono text-xs text-muted-foreground">{root.id}</span>
              <h2 className="text-xl font-semibold tracking-tight group-hover:underline">{root.title[lang]}</h2>
            </Link>
            {root.children.length > 0 && (
              <ul className="mt-3 flex flex-wrap gap-1.5">
                {root.children.map((child) => (
                  <li key={child.id}>
                    <Link
                      to={pagePath(lang, child.id)}
                      className="inline-block rounded-md border border-border px-2 py-1 text-sm text-muted-foreground transition-colors hover:bg-accent hover:text-foreground"
                    >
                      {child.title[lang]}
                    </Link>
                  </li>
                ))}
              </ul>
            )}
          </article>
        ))}
      </section>
    </main>
  );
}
