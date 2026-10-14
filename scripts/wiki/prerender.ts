/**
 * After `vite build`: write one static HTML file per route so GitHub Pages serves
 * real pages (HTTP 200, correct <title>/lang/description, readable without JS):
 *
 *   dist/<lang>/index.html          language home
 *   dist/<lang>/<id>/index.html     page
 *   dist/404.html                   SPA shell for unknown URLs
 *   dist/sitemap.xml, robots.txt
 *
 * The client boots on top of the static article (see src/content/initial.ts).
 */
import fs from 'node:fs';
import path from 'node:path';
import { BASE_PATH, LANGUAGES, type Lang, siteConfig } from '../../site.config.ts';
import { homePath, pagePath } from '../../src/shared/page-id.ts';
import { ARTICLE_CLASS } from '../../src/shared/article.ts';
import type { PagePayload } from '../../src/shared/types.ts';
import type { BuildResult } from './build.ts';

const HTML_LANG: Record<Lang, string> = { zh: 'zh-Hans', en: 'en' };

function esc(s: string): string {
  return s.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;');
}

function absolute(routePath: string): string {
  return new URL(routePath.replace(/^\//, ''), siteConfig.siteUrl).href;
}

interface RouteHead {
  lang: Lang;
  title: string;
  description: string;
  /** Router path per language, for canonical + hreflang links. */
  alternates: Record<Lang, string>;
  /** Language whose URL is canonical (an untranslated page points at the source language). */
  canonicalLang?: Lang;
}

function renderHead(template: string, head: RouteHead): string {
  const links = [
    `<link rel="canonical" href="${absolute(head.alternates[head.canonicalLang ?? head.lang])}" />`,
    ...LANGUAGES.map((l) => `<link rel="alternate" hreflang="${HTML_LANG[l]}" href="${absolute(head.alternates[l])}" />`),
    `<meta name="description" content="${esc(head.description)}" />`,
    `<meta property="og:title" content="${esc(head.title)}" />`,
    `<meta property="og:description" content="${esc(head.description)}" />`,
    `<meta property="og:type" content="article" />`,
  ].join('\n    ');
  return template
    .replace(/<html lang="[^"]*"/, `<html lang="${HTML_LANG[head.lang]}"`)
    .replace(/<title>[^<]*<\/title>/, `<title>${esc(head.title)}</title>\n    ${links}`);
}

function withBody(html: string, body: string): string {
  return html.replace('<div id="root"></div>', `<div id="root">${body}</div>`);
}

function staticPage(payload: PagePayload): string {
  const site = siteConfig.title[payload.lang];
  const { html, ...meta } = payload;
  // The client seeds its page cache from this, so it does not refetch the page it was served with.
  const initial = JSON.stringify({ key: `${payload.lang}/${payload.id}`, meta }).replace(/</g, '\\u003c');
  return [
    `<header class="prerender-header"><a href="${BASE_PATH}${payload.lang}/">${esc(site)}</a></header>`,
    `<main class="prerender-main"><h1>${esc(`${payload.id} ${payload.title}`)}</h1>`,
    `<article id="wiki-prerendered" class="${ARTICLE_CLASS}" lang="${HTML_LANG[payload.contentLang]}">${html}</article></main>`,
    `<script type="application/json" id="wiki-initial">${initial}</script>`,
  ].join('');
}

export function prerender(outDir: string, result: BuildResult): number {
  const template = fs.readFileSync(path.join(outDir, 'index.html'), 'utf8');
  const write = (routePath: string, html: string) => {
    const file = path.join(outDir, routePath, 'index.html');
    fs.mkdirSync(path.dirname(file), { recursive: true });
    fs.writeFileSync(file, html);
  };
  const urls: string[] = [];
  const homes = Object.fromEntries(LANGUAGES.map((l) => [l, homePath(l)])) as Record<Lang, string>;

  for (const lang of LANGUAGES) {
    const head = { lang, title: siteConfig.title[lang], description: siteConfig.description[lang], alternates: homes };
    const nav = result.site.nav
      .map((n) => `<li><a href="${BASE_PATH}${lang}/${n.id}/">${esc(`${n.id} ${n.title[lang]}`)}</a></li>`)
      .join('');
    write(homePath(lang), withBody(renderHead(template, head), `<main class="prerender-main"><h1>${esc(head.title)}</h1><ul>${nav}</ul></main>`));
    urls.push(absolute(homePath(lang)));
  }

  for (const payload of result.payloads.values()) {
    const alternates = Object.fromEntries(LANGUAGES.map((l) => [l, pagePath(l, payload.id)])) as Record<Lang, string>;
    const head = {
      lang: payload.lang,
      title: `${payload.title} · ${siteConfig.title[payload.lang]}`,
      description: payload.description || siteConfig.description[payload.lang],
      alternates,
      canonicalLang: payload.status === 'untranslated' ? payload.contentLang : payload.lang,
    };
    write(pagePath(payload.lang, payload.id), withBody(renderHead(template, head), staticPage(payload)));
    if (payload.status !== 'untranslated') urls.push(absolute(pagePath(payload.lang, payload.id)));
  }

  fs.writeFileSync(path.join(outDir, '404.html'), template);
  fs.writeFileSync(
    path.join(outDir, 'sitemap.xml'),
    `<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n${urls.map((u) => `  <url><loc>${esc(u)}</loc></url>`).join('\n')}\n</urlset>\n`,
  );
  fs.writeFileSync(path.join(outDir, 'robots.txt'), `User-agent: *\nAllow: /\nSitemap: ${absolute('/sitemap.xml')}\n`);
  return urls.length;
}
