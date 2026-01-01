# Personal Wiki Site

A personal knowledge base and portfolio website built with React, Vite, and Tailwind CSS. Designed to be easily deployed to GitHub Pages.

## Features

- **Wiki System**: Hierarchical documentation with automatic sidebar generation.
- **Markdown Support**: Write content in Markdown with syntax highlighting and GFM support.
- **Table of Contents**: Automatic in-page TOC generation in the sidebar for the active page.
- **Dark/Light Mode**: System-aware theme toggling.
- **Responsive Design**: Mobile-friendly layout (Sidebar hidden on small screens, TODO: Add mobile drawer).
- **GitHub Pages Ready**: Pre-configured for easy deployment.

## Tech Stack

- **Framework**: React 18 + Vite
- **Language**: TypeScript
- **Styling**: Tailwind CSS + Tailwind Typography
- **Routing**: React Router DOM v6
- **Markdown**: react-markdown, remark-gfm, rehype-highlight
- **Icons**: Lucide React

## Project Structure

```
personal-wiki-site/
├── public/              # Static assets
├── src/
│   ├── components/      # Reusable UI components
│   │   ├── Layout.tsx   # Main layout with Header
│   │   ├── MarkdownRenderer.tsx # Markdown rendering logic
│   │   ├── ThemeToggle.tsx # Dark mode toggle
│   │   └── WikiSidebar.tsx # Recursive sidebar navigation
│   ├── data/
│   │   └── wikiData.ts  # Wiki content and structure definition
│   ├── lib/
│   │   └── utils.ts     # Utility functions (cn, extractHeaders)
│   ├── pages/
│   │   ├── Home.tsx     # Landing page
│   │   └── Wiki.tsx     # Wiki page layout and logic
│   ├── App.tsx          # App entry and routing
│   ├── main.tsx         # React entry point
│   └── index.css        # Global styles and Tailwind directives
├── index.html           # HTML entry point
├── package.json         # Dependencies and scripts
├── tailwind.config.js   # Tailwind configuration
├── tsconfig.json        # TypeScript configuration
└── vite.config.ts       # Vite configuration
```

## Setup & Development

1.  **Install Dependencies**
    ```bash
    pnpm install
    ```

2.  **Start Development Server**
    ```bash
    pnpm dev
    ```

3.  **Build for Production**
    ```bash
    pnpm build
    ```

## Deployment (GitHub Pages)

This project is configured to be deployed to GitHub Pages.

1.  Update `vite.config.ts` `base` URL if you are deploying to a project page (e.g., `/repo-name/`). Currently set to `./` for relative paths which usually works for both user sites and project sites if configured correctly, but explicit base is better for routing.
    *   If your repo is `username.github.io`, `base: '/'` is fine.
    *   If your repo is `username.github.io/repo`, set `base: '/repo/'`.

2.  **Deploy Script**
    The `package.json` includes a `deploy` script using `gh-pages`.
    ```bash
    pnpm run deploy
    ```
    This will build the project and push the `dist` folder to the `gh-pages` branch.

## Data Management (API)

The wiki content is currently managed in `src/data/wikiData.ts`.

### `WikiPage` Interface

```typescript
interface WikiPage {
  id: string;       // Unique identifier
  title: string;    // Display title
  slug: string;     // URL segment (e.g., 'react')
  content?: string; // Markdown content
  children?: WikiPage[]; // Nested pages
}
```

To add a new page:
1.  Open `src/data/wikiData.ts`.
2.  Add a new object to the `wikiData` array or the `children` array of an existing page.
3.  Ensure the `slug` is unique among siblings.

## Future Improvements

- [ ] Mobile Sidebar (Drawer)
- [ ] Search functionality
- [ ] Backend integration (API calls)
- [ ] Dynamic content loading (fetch Markdown from files instead of string literals)
