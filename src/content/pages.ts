/**
 * Page payload loading with an in-memory cache.
 * Payloads are static JSON written by the content pipeline: <base>/data/pages/<lang>/<id>.json
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

async function loadOnce(key: string) {
  try {
    const res = await fetch(`${import.meta.env.BASE_URL}data/pages/${key}.json?v=${buildId}`);
    if (!res.ok) throw new Error(`HTTP ${res.status}`);
    cache.set(key, { payload: (await res.json()) as PagePayload });
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
