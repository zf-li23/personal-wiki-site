/**
 * Page payload loading with an in-memory cache.
 * Payloads are static JSON written by the content pipeline: <base>/data/pages/<lang>/<id>.json;
 * in production the article HTML comes from the route page <base>/<lang>/<id>/ (see fetchArticle).
 */
import { useEffect, useSyncExternalStore } from 'react';
import type { Lang, PagePayload } from '../shared/types.ts';
import { site } from './site.ts';

type Entry = { payload: PagePayload } | { error: string };

const cache = new Map<string, Entry>();
const listeners = new Set<() => void>();
let buildId = site.buildId;

function notify() {
  for (const l of listeners) l();
}

function subscribe(listener: () => void) {
  listeners.add(listener);
  return () => listeners.delete(listener);
}

export function pageKey(lang: Lang, id: string): string {
  return `${lang}/${id}`;
}

/** Used at boot to adopt the payload of a prerendered page without refetching it. */
export function seedPage(payload: PagePayload) {
  cache.set(pageKey(payload.lang, payload.id), { payload });
}

/** Forget a cached page (e.g. after a failed load) so it is fetched again. */
export function reloadPage(lang: Lang, id: string) {
  cache.delete(pageKey(lang, id));
  notify();
}

const pending = new Map<string, Promise<void>>();

function load(key: string): Promise<void> {
  let p = pending.get(key);
  if (!p) {
    p = loadOnce(key).finally(() => pending.delete(key));
    pending.set(key, p);
  }
  return p;
}

/**
 * The published JSON carries only metadata; the article itself is in the page's prerendered
 * route HTML (scripts/wiki/prerender.ts), so it is shipped once. The dev server has no routes
 * and still puts `html` in the JSON.
 */
async function fetchArticle(key: string): Promise<string> {
  const res = await fetch(`${import.meta.env.BASE_URL}${key}/?v=${buildId}`);
  if (!res.ok) throw new Error(`HTTP ${res.status}`);
  const doc = new DOMParser().parseFromString(await res.text(), 'text/html');
  const article = doc.getElementById('wiki-prerendered');
  if (!article) throw new Error('article not found');
  return article.innerHTML;
}

async function loadOnce(key: string) {
  try {
    const res = await fetch(`${import.meta.env.BASE_URL}data/pages/${key}.json?v=${buildId}`);
    if (!res.ok) throw new Error(`HTTP ${res.status}`);
    const payload = (await res.json()) as Omit<PagePayload, 'html'> & { html?: string };
    const html = typeof payload.html === 'string' ? payload.html : await fetchArticle(key);
    cache.set(key, { payload: { ...payload, html } });
  } catch (e) {
    cache.set(key, { error: e instanceof Error ? e.message : String(e) });
  } finally {
    notify();
  }
}

/** Promise-based access to a page (used by link previews). Shares the cache with usePage. */
export async function fetchPage(lang: Lang, id: string): Promise<PagePayload> {
  const key = pageKey(lang, id);
  if (!cache.has(key)) await load(key);
  const entry = cache.get(key);
  if (!entry || 'error' in entry) throw new Error(entry && 'error' in entry ? entry.error : 'not found');
  return entry.payload;
}

export function usePage(lang: Lang, id: string): Entry | undefined {
  const key = pageKey(lang, id);
  const entry = useSyncExternalStore(subscribe, () => cache.get(key));
  useEffect(() => {
    if (!cache.has(key)) void load(key);
  }, [key, entry]);
  return entry;
}

// Dev: the Vite plugin announces content rebuilds; drop the cache so the open page refetches.
if (import.meta.hot) {
  import.meta.hot.on('wiki:content', (data: { buildId: string }) => {
    buildId = data.buildId;
    cache.clear();
    notify();
  });
}
