# Agent guide: personal-wiki-site

A bilingual (zh / en: each page is written in one language first, then translated) static knowledge base deployed to GitHub Pages.
**Writing content? Read [CONTENT_GUIDE.md](CONTENT_GUIDE.md) (format spec) and [AUTHORING.md](AUTHORING.md) (writer-agent workflow; dispatch writers as the `wiki-writer` agent).**
This file is for changing the code.

## Commands

| Command | What it does |
|---|---|
| `pnpm install` / `pnpm setup:python` | Node deps / Python env for plots (`.venv`, needs `uv`) |
| `pnpm dev` | Dev server; rebuilds content on every change under `content/` |
| `pnpm build` | `tsc`, then `vite build` (content pipeline + bundle + prerender) → `dist/` |
| `pnpm check` | Strict content build + typecheck + eslint + unit tests. Run before every commit |
| `pnpm wiki <cmd>` | Content CLI: `build [--strict]`, `lint <ids>` (fast: renders only those courses), `status`, `stamp <id>`, `new …`, `terms`, `freeze`/`unfreeze <script>`, `check-r` (see `scripts/wiki.ts`) |
| `pnpm test` | Pipeline unit tests (`node --test`) |
| `python3 scripts/prep_sources.py` | Orchestrator: extract `sources/` materials to text + low-res images of flagged pages (`sources/text/INDEX.md`) |
| `python3 scripts/merge_terms.py <yaml> "<section>" [--apply]` | Orchestrator: add glossary proposals; reports conflicts, never edits existing entries |

Node ≥ 22.18 runs the TypeScript in `scripts/` directly (type stripping): no build step for tooling.

## Architecture

```
content/**  ──scan──▶  ContentTree ──▶ plots (Python, cached) ──▶ Markdown→HAST per page×lang
   (source of truth)        scripts/wiki/scan.ts      plots.ts + plot/render_plot.py        markdown.ts
                                                                                              │
                     linking.ts: statement index, concept sites, references/concept links ◀──┘
                                                                                              │
         build.ts stringifies and writes .generated/  ◀───────────────────────────────────────┘
           site.json                    navigation (SiteData) → client via `virtual:wiki/site`
           public/data/pages/<lang>/<id>.json   PagePayload (pre-rendered HTML, TOC, status)
           public/data/search/<lang>.json       search index
           public/data/concepts.json            concept registry + definition sites + usage
           public/media/<id>/…  public/plots/<key>/…
                                    │
 vite-plugin.ts: publicDir=.generated/public, dev watcher, build hook, prerender (prerender.ts)
                                    │
 src/ (React 19 + React Router 7 + Tailwind 4): fetches payloads, injects HTML, adds behaviour
```

Key decisions (keep them):
- **One Markdown parser, at build time.** The client never parses Markdown, math or code; it receives HTML. KaTeX/highlight.js are not in the client bundle (only KaTeX CSS).
- **Page id = numeric hierarchy = URL** (`/<lang>/<id>/`). Validation lives in `src/shared/page-id.ts`, shared by pipeline and client.
- **Contracts are typed** in `src/shared/types.ts` (pipeline output ⇄ client input). Change both sides together.
- **Static per-route HTML** (`dist/<lang>/<id>/index.html`) so Pages serves 200s with real titles/hreflang; the client adopts the prerendered page from `#wiki-initial` without refetching.
- **R companions** (`plots/<name>.R`) are shown next to the Python source but never run by the build (CI has no R) and are excluded from the plot cache key; `pnpm wiki check-r` runs them locally when Rscript is installed.
- **Plots** run in a separate Python process per script, both themes, cached by content hash in `.cache/plots/`. Never commit rendered images, except *frozen* plots (`pnpm wiki freeze`, for scripts too slow to re-render; see CONTENT_GUIDE §4).
- Changing `scripts/wiki/plot/render_plot.py` or `requirements.txt` invalidates every cached plot (a full re-render takes ~30 min). Batch such changes. A helper in `PLOT_HELPERS` only invalidates the scripts that import it.
- **Site URL/base path** only in `site.config.ts`. Never hard-code `/personal-wiki-site/`; use `BASE_PATH` or `import.meta.env.BASE_URL`.

## Where to change what

| Task | Place |
|---|---|
| New Markdown syntax / HTML transform | `scripts/wiki/markdown.ts` (`rehypeWiki`, `rehypeStatements`), plus CSS in `src/styles/index.css`, plus a test |
| Chemical structures (```smiles, RDKit WASM at build time) / mechanism helper for plots | `scripts/wiki/chem.ts` / `scripts/wiki/plot/wikichem.py` (listed in `PLOT_HELPERS`, `paths.ts`: scripts that import it re-render when it changes) |
| Page roles, heading / statement numbering rules | `scripts/wiki/numbering.ts` (pure, shared by checker, `pnpm wiki fix` in `fix.ts`, tests) |
| Cross-page references, concept definitions & links, backlinks | `scripts/wiki/linking.ts` (runs after all pages render; then `build.ts` stringifies) |
| Hover previews, concept index, page connections | `src/components/LinkPreview.tsx`, `src/pages/ConceptsPage.tsx`, `src/components/PageParts.tsx` |
| Behaviour inside articles (copy, diagrams, link interception) | `src/components/Article.tsx` (event delegation on the injected HTML) |
| New content rule / lint | `scan.ts` (structure), `frontmatter.ts` (schema), `markdown.ts` (body), `plots.ts` (scripts); document it in CONTENT_GUIDE.md |
| UI strings | `src/i18n.ts` (both languages; TypeScript enforces parity) |
| Plot theme colours | `scripts/wiki/plot/render_plot.py` `THEMES` and the matching CSS tokens |
| Languages, site title, URL | `site.config.ts` |

## Invariants checked by `pnpm check`

- Content: directory names, id/parent consistency, front matter schema, internal links and anchors, asset/plot references, legacy syntax, plot script rules, KaTeX errors (warnings fail strict mode).
- Code: `tsc` (strict, `erasableSyntaxOnly`, explicit `.ts` import extensions), eslint (incl. react-hooks), unit tests in `scripts/wiki/wiki.test.ts`.

## Conventions

- Relative imports with explicit extensions (`./x.ts`, `./X.tsx`); `import type` for types.
- Code comments in English. User-visible strings only via `src/i18n.ts`.
- Generated directories (`.generated/`, `.cache/`, `dist/`) are disposable; never edit them.
- `sources/` holds the current course's copyrighted materials and is git-ignored except its README; never commit anything from it or copy it into `content/`.
- Deploy: push to `main` → `.github/workflows/deploy.yml` builds, checks and publishes to GitHub Pages (source: "GitHub Actions"). There is only the `main` branch; do not recreate `gh-pages`.
