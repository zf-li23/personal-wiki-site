/** Small presentational pieces of a wiki page. */
import { AlertTriangle, ArrowLeft, ArrowRight, Languages } from 'lucide-react';
import { Link } from 'react-router';
import { ancestorsOf, neighbours } from '../content/site.ts';
import { useLang, useStrings } from '../i18n.ts';
import { homePath, pagePath } from '../shared/page-id.ts';
import type { Diagnostic, NavNode, TranslationStatus } from '../shared/types.ts';

export function Breadcrumbs({ id }: { id: string }) {
  const lang = useLang();
  const t = useStrings();
  return (
    <nav aria-label="Breadcrumb" className="mb-3 flex flex-wrap items-center gap-x-1.5 text-sm text-muted-foreground">
      <Link to={homePath(lang)} className="hover:text-foreground">
        {t.home}
      </Link>
      {ancestorsOf(id).map((a) => (
        <span key={a.id} className="flex items-center gap-x-1.5">
          <span aria-hidden>/</span>
          <Link to={pagePath(lang, a.id)} className="hover:text-foreground">
            {a.title[lang]}
          </Link>
        </span>
      ))}
    </nav>
  );
}

export function StatusBanner({ status }: { status: TranslationStatus }) {
  const t = useStrings();
  if (status !== 'untranslated' && status !== 'stale') return null;
  return (
    <div className="mb-6 flex items-start gap-2 rounded-lg border border-amber-500/40 bg-amber-500/10 px-4 py-3 text-sm">
      <Languages size={16} className="mt-0.5 shrink-0 text-amber-600 dark:text-amber-400" />
      <span>{status === 'untranslated' ? t.untranslated : t.stale}</span>
    </div>
  );
}

/** Dev only: build problems for this page, so writers see them without reading the terminal. */
export function DevDiagnostics({ items }: { items?: Diagnostic[] }) {
  const t = useStrings();
  if (!items?.length) return null;
  return (
    <details open className="mb-6 rounded-lg border border-red-500/40 bg-red-500/10 px-4 py-3 text-sm">
      <summary className="flex cursor-pointer items-center gap-2 font-medium">
        <AlertTriangle size={16} className="text-red-600 dark:text-red-400" />
        {t.devDiagnostics(items.length)}
      </summary>
      <ul className="mt-2 space-y-1 font-mono text-xs">
        {items.map((d, i) => (
          <li key={i}>
            <span className={d.level === 'error' ? 'text-red-600 dark:text-red-400' : 'text-amber-600 dark:text-amber-400'}>{d.level}</span>{' '}
            {d.file}
            {d.line ? `:${d.line}` : ''} — {d.message}
          </li>
        ))}
      </ul>
    </details>
  );
}

export function ChildList({ node }: { node: NavNode }) {
  const lang = useLang();
  const t = useStrings();
  if (!node.children.length) return null;
  return (
    <section className="mt-12 border-t border-border pt-8">
      <h2 className="mb-4 text-lg font-semibold">{t.inThisSection}</h2>
      <ul className="grid gap-3 sm:grid-cols-2">
        {node.children.map((child) => (
          <li key={child.id}>
            <Link
              to={pagePath(lang, child.id)}
              className="block h-full rounded-lg border border-border bg-card p-4 transition-colors hover:border-foreground/30 hover:bg-accent"
            >
              <span className="block font-mono text-xs text-muted-foreground">{child.id}</span>
              <span className="mt-1 block font-medium">{child.title[lang]}</span>
              {child.children.length > 0 && <span className="mt-1 block text-xs text-muted-foreground">{t.subsections(child.children.length)}</span>}
            </Link>
          </li>
        ))}
      </ul>
    </section>
  );
}

export function PrevNext({ id }: { id: string }) {
  const lang = useLang();
  const t = useStrings();
  const { prev, next } = neighbours(id);
  const card = 'flex flex-1 flex-col rounded-lg border border-border p-4 transition-colors hover:bg-accent';
  return (
    <nav className="mt-12 flex flex-col gap-3 sm:flex-row">
      {prev ? (
        <Link to={pagePath(lang, prev.id)} className={card}>
          <span className="flex items-center gap-1 text-xs text-muted-foreground">
            <ArrowLeft size={12} /> {t.previous}
          </span>
          <span className="mt-1 text-sm font-medium">
            {prev.id} {prev.title[lang]}
          </span>
        </Link>
      ) : (
        <span className="flex-1" />
      )}
      {next ? (
        <Link to={pagePath(lang, next.id)} className={`${card} items-end text-right`}>
          <span className="flex items-center gap-1 text-xs text-muted-foreground">
            {t.next} <ArrowRight size={12} />
          </span>
          <span className="mt-1 text-sm font-medium">
            {next.id} {next.title[lang]}
          </span>
        </Link>
      ) : (
        <span className="flex-1" />
      )}
    </nav>
  );
}
