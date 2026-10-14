/** Loads <base>/data/search/<lang>.json on first use; matching lives in shared/search.ts. */
import type { Lang, SearchEntry } from '../shared/types.ts';
import { site } from './site.ts';

const indexes = new Map<Lang, Promise<SearchEntry[]>>();

export function loadSearchIndex(lang: Lang): Promise<SearchEntry[]> {
  let p = indexes.get(lang);
  if (!p) {
    p = fetch(`${import.meta.env.BASE_URL}data/search/${lang}.json?v=${site.buildId}`).then((r) => {
      if (!r.ok) throw new Error(`HTTP ${r.status}`);
      return r.json() as Promise<SearchEntry[]>;
    });
    p.catch(() => indexes.delete(lang));
    indexes.set(lang, p);
  }
  return p;
}

export { type SearchHit, search } from '../shared/search.ts';
