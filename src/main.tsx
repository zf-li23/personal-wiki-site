import { StrictMode } from 'react';
import { createRoot } from 'react-dom/client';
import { App } from './App.tsx';
import { seedPage } from './content/pages.ts';
import { ThemeProvider } from './lib/theme.tsx';
import type { PagePayload } from './shared/types.ts';
import 'katex/dist/katex.min.css';
import './styles/index.css';

// Prerendered pages (scripts/wiki/prerender.ts) embed the page they were served with;
// adopt it so the first render needs no fetch.
const initial = document.getElementById('wiki-initial');
const article = document.getElementById('wiki-prerendered');
if (initial && article) {
  try {
    const { meta } = JSON.parse(initial.textContent ?? '') as { meta: Omit<PagePayload, 'html'> };
    seedPage({ ...meta, html: article.innerHTML });
  } catch {
    // fall back to fetching the page
  }
}

createRoot(document.getElementById('root')!).render(
  <StrictMode>
    <ThemeProvider>
      <App />
    </ThemeProvider>
  </StrictMode>,
);
