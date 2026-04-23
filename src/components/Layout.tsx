import { Link, Outlet } from 'react-router-dom';
import { ThemeToggle } from './ThemeToggle';

export default function Layout() {
  return (
    <div className="min-h-screen bg-background text-foreground flex flex-col">
      <header className="border-b border-border sticky top-0 z-50 bg-background/95 backdrop-blur supports-[backdrop-filter]:bg-background/60">
        <div className="container mx-auto px-4 h-14 flex items-center justify-between">
          <Link to="/" className="font-bold text-lg tracking-tight">My Personal Wiki</Link>
          <ThemeToggle />
        </div>
      </header>
      <main className="flex-1">
        <Outlet />
      </main>
      <footer className="border-t border-border py-6 md:py-0">
        <div className="container mx-auto px-4 flex flex-col md:flex-row items-center justify-between gap-4 md:h-14 text-sm text-muted-foreground">
          <p>© 2026 My Personal Wiki. Built with React & Vite.</p>
        </div>
      </footer>
    </div>
  );
}
