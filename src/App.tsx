/**
 * Routes (all relative to the site base, see site.config.ts):
 *   /              -> redirect to /<preferred lang>/
 *   /:lang/        -> HomePage
 *   /:lang/concepts/ -> ConceptsPage (concept index)
 *   /:lang/:id/    -> WikiPage (id = numeric page id, e.g. 3.1.13)
 *   anything else  -> NotFound
 */
import { Navigate, RouterProvider, createBrowserRouter } from 'react-router';
import { BASE_PATH } from '../site.config.ts';
import { preferredLang } from './lib/preferences.ts';
import { ConceptsPage } from './pages/ConceptsPage.tsx';
import { HomePage } from './pages/HomePage.tsx';
import { Layout } from './pages/Layout.tsx';
import { NotFound } from './pages/NotFound.tsx';
import { WikiPage } from './pages/WikiPage.tsx';

const router = createBrowserRouter(
  [
    { path: '/', element: <Navigate to={`/${preferredLang()}/`} replace /> },
    {
      path: '/:lang',
      element: <Layout />,
      children: [
        { index: true, element: <HomePage /> },
        { path: 'concepts', element: <ConceptsPage /> },
        { path: ':id', element: <WikiPage /> },
      ],
    },
    { path: '*', element: <NotFound /> },
  ],
  { basename: BASE_PATH.replace(/\/$/, '') },
);

export function App() {
  return <RouterProvider router={router} />;
}
