import { useEffect, useMemo, useState } from 'react';
import { Link } from 'react-router';
import { useConcepts } from '../content/concepts.ts';
import { findNode } from '../content/site.ts';
import { useLang, useStrings } from '../i18n.ts';
import { pagePath } from '../shared/page-id.ts';

/** The book's index: every concept with its definition site, sorted by pinyin (zh) or alphabetically (en). */
export function ConceptsPage() {
  const lang = useLang();
  const t = useStrings();
  const concepts = useConcepts();
  const [filter, setFilter] = useState('');

  useEffect(() => {
    document.title = `${t.concepts} · ${t.siteTitle}`;
  }, [t]);

  const list = useMemo(() => {
    if (!concepts) return [];
    const collator = new Intl.Collator(lang === 'zh' ? 'zh-Hans-u-co-pinyin' : 'en', { sensitivity: 'base' });
    const q = filter.trim().toLowerCase();
    return [...concepts.values()]
      .filter((c) => !q || c.zh.includes(q) || c.en.toLowerCase().includes(q))
      .sort((a, b) => collator.compare(lang === 'zh' ? a.zh : a.en, lang === 'zh' ? b.zh : b.en));
  }, [concepts, filter, lang]);

  return (
    <main className="mx-auto max-w-4xl px-4 py-10">
      <h1 className="text-3xl font-bold tracking-tight">{t.concepts}</h1>
      <p className="mt-3 text-muted-foreground">{t.conceptsIntro}</p>
      <input
        value={filter}
        onChange={(e) => setFilter(e.target.value)}
        placeholder={t.conceptsFilter}
        className="mt-6 h-10 w-full rounded-md border border-border bg-card px-3 text-sm outline-none focus:border-foreground/40"
      />
      <ul className="mt-6 divide-y divide-border">
        {list.map((c) => (
          <li key={c.id} id={c.id} className="flex flex-col gap-1 py-3 sm:flex-row sm:items-baseline sm:justify-between">
            <span>
              <span className="font-medium">{lang === 'zh' ? c.zh : c.en}</span>
              <span className="ml-2 text-sm text-muted-foreground">{lang === 'zh' ? c.en : c.zh}</span>
            </span>
            <span className="text-sm text-muted-foreground">
              {c.site ? (
                <Link to={`${pagePath(lang, c.site.pageId)}#${c.site.anchor}`} className="hover:text-foreground hover:underline">
                  {t.definedIn(`${c.site.pageId} ${findNode(c.site.pageId)?.title[lang] ?? ''}`)}
                </Link>
              ) : (
                t.notDefinedYet
              )}
              {c.usedIn.length > 0 && <span className="ml-3">{t.usedOnPages(c.usedIn.length)}</span>}
            </span>
          </li>
        ))}
      </ul>
    </main>
  );
}
