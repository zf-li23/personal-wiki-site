/** Concept registry joined with definition sites: <base>/data/concepts.json, fetched on first use. */
import { useEffect, useState } from 'react';
import type { ConceptEntry } from '../shared/types.ts';
import { site } from './site.ts';

let promise: Promise<Map<string, ConceptEntry>> | null = null;

export function loadConcepts(): Promise<Map<string, ConceptEntry>> {
  promise ??= fetch(`${import.meta.env.BASE_URL}data/concepts.json?v=${site.buildId}`)
    .then((r) => {
      if (!r.ok) throw new Error(`HTTP ${r.status}`);
      return r.json() as Promise<ConceptEntry[]>;
    })
    .then((list) => new Map(list.map((c) => [c.id, c])));
  promise.catch(() => (promise = null));
  return promise;
}

export function useConcepts(): Map<string, ConceptEntry> | null {
  const [concepts, setConcepts] = useState<Map<string, ConceptEntry> | null>(null);
  useEffect(() => {
    let alive = true;
    loadConcepts().then((c) => alive && setConcepts(c), () => undefined);
    return () => {
      alive = false;
    };
  }, []);
  return concepts;
}
