import { BookA, Languages, Menu, Moon, Search, Sun } from 'lucide-react';
import { Link, useLocation } from 'react-router';
import { otherLang, useLang, useStrings } from '../i18n.ts';
import { storeLang } from '../lib/preferences.ts';
import { useTheme } from '../lib/theme.tsx';
import { conceptsPath } from '../shared/page-id.ts';

interface HeaderProps {
  onOpenSearch: () => void;
  /** Present on pages with a sidebar: opens it as a drawer on small screens. */
  onOpenMenu?: () => void;
}

const iconButton =
  'inline-flex h-9 items-center justify-center gap-1.5 rounded-md px-2 text-sm text-muted-foreground transition-colors hover:bg-accent hover:text-foreground';

export function Header({ onOpenSearch, onOpenMenu }: HeaderProps) {
  const lang = useLang();
  const t = useStrings();
  const { theme, toggleTheme } = useTheme();
  const location = useLocation();
  const target = otherLang(lang);
  // Same page in the other language: swap the leading /<lang>/ segment, keep the rest.
  const switchTo = location.pathname.replace(/^\/[a-z]+(?=\/|$)/, `/${target}`) + location.hash;

  return (
    <header className="sticky top-0 z-40 border-b border-border bg-background/90 backdrop-blur">
      <div className="mx-auto flex h-14 max-w-[90rem] items-center gap-2 px-4">
        {onOpenMenu && (
          <button type="button" className={`${iconButton} lg:hidden`} onClick={onOpenMenu} aria-label={t.menu}>
            <Menu size={18} />
          </button>
        )}
        <Link to={`/${lang}/`} className="mr-auto truncate font-semibold tracking-tight">
          {t.siteTitle}
        </Link>
        <button
          type="button"
          onClick={onOpenSearch}
          className="inline-flex h-9 items-center gap-2 rounded-md border border-border px-3 text-sm text-muted-foreground transition-colors hover:bg-accent hover:text-foreground"
          aria-label={t.search}
        >
          <Search size={16} />
          <span className="hidden sm:inline">{t.search}</span>
          <kbd className="hidden rounded border border-border px-1.5 font-mono text-[10px] md:inline">Ctrl K</kbd>
        </button>
        <Link to={conceptsPath(lang)} className={iconButton} aria-label={t.concepts} title={t.concepts}>
          <BookA size={16} />
          <span className="hidden md:inline">{t.concepts}</span>
        </Link>
        <Link to={switchTo} className={iconButton} onClick={() => storeLang(target)} aria-label={t.switchLanguageLabel} hrefLang={target}>
          <Languages size={16} />
          <span>{t.switchLanguage}</span>
        </Link>
        <button type="button" className={iconButton} onClick={toggleTheme} aria-label={t.toggleTheme} title={t.toggleTheme}>
          {theme === 'dark' ? <Moon size={18} /> : <Sun size={18} />}
        </button>
      </div>
    </header>
  );
}
