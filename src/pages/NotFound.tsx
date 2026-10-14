import { Link } from 'react-router';
import { useLang, useStrings } from '../i18n.ts';
import { homePath } from '../shared/page-id.ts';

export function NotFound() {
  const lang = useLang();
  const t = useStrings();
  return (
    <main className="mx-auto max-w-xl px-4 py-24 text-center">
      <h1 className="text-3xl font-bold">{t.notFoundTitle}</h1>
      <p className="mt-3 text-muted-foreground">{t.notFoundBody}</p>
      <Link to={homePath(lang)} className="mt-6 inline-block rounded-md border border-border px-4 py-2 text-sm hover:bg-accent">
        {t.backHome}
      </Link>
    </main>
  );
}
