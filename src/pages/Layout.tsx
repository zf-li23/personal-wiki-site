import { useEffect, useState } from 'react';
import { Outlet, useOutletContext, useParams } from 'react-router';
import { isLang } from '../../site.config.ts';
import { Header } from '../components/Header.tsx';
import { SearchDialog } from '../components/SearchDialog.tsx';
import { NotFound } from './NotFound.tsx';

export interface LayoutContext {
  menuOpen: boolean;
  setMenuOpen: (open: boolean) => void;
}

const HTML_LANG = { zh: 'zh-Hans', en: 'en' } as const;

/** Shell for every /:lang route: header, search dialog, keyboard shortcuts. */
export function Layout() {
  const { lang, id } = useParams();
  const [searchOpen, setSearchOpen] = useState(false);
  const [menuOpen, setMenuOpen] = useState(false);

  useEffect(() => {
    if (isLang(lang)) document.documentElement.lang = HTML_LANG[lang];
  }, [lang]);

  useEffect(() => {
    const onKey = (e: KeyboardEvent) => {
      const typing = e.target instanceof HTMLElement && /^(INPUT|TEXTAREA|SELECT)$/.test(e.target.tagName);
      if ((e.key === 'k' && (e.metaKey || e.ctrlKey)) || (e.key === '/' && !typing)) {
        e.preventDefault();
        setSearchOpen(true);
      }
    };
    window.addEventListener('keydown', onKey);
    return () => window.removeEventListener('keydown', onKey);
  }, []);

  if (!isLang(lang)) return <NotFound />;

  return (
    <div className="min-h-screen bg-background text-foreground">
      <Header onOpenSearch={() => setSearchOpen(true)} onOpenMenu={id ? () => setMenuOpen(true) : undefined} />
      <Outlet context={{ menuOpen, setMenuOpen } satisfies LayoutContext} />
      <SearchDialog open={searchOpen} onClose={() => setSearchOpen(false)} />
    </div>
  );
}

export function useLayout(): LayoutContext {
  return useOutletContext<LayoutContext>();
}
