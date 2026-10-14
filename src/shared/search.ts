/**
 * Full-text search over SearchEntry[] (pure; used by the client and tested in scripts/wiki/wiki.test.ts).
 * Plain substring matching works for Chinese without a tokenizer. Every whitespace-separated
 * term must match the title, a heading, the body or the ancestor trail.
 */
import type { SearchEntry } from './types.ts';

export interface SearchHit {
  entry: SearchEntry;
  score: number;
  /** Text around the first body match, or the matching heading. */
  snippet: string;
}

export function search(entries: SearchEntry[], query: string, limit = 30): SearchHit[] {
  const terms = query.toLowerCase().split(/\s+/).filter(Boolean);
  if (!terms.length) return [];
  const hits: SearchHit[] = [];
  for (const entry of entries) {
    const title = `${entry.id} ${entry.title}`.toLowerCase();
    const headings = entry.headings.map((h) => h.toLowerCase());
    const text = entry.text.toLowerCase();
    let score = 0;
    let snippet = '';
    let matchedAll = true;
    for (const term of terms) {
      let s = 0;
      if (title.includes(term)) s += 20;
      const h = headings.findIndex((x) => x.includes(term));
      if (h >= 0) {
        s += 6;
        snippet ||= entry.headings[h];
      }
      const at = text.indexOf(term);
      if (at >= 0) {
        s += 1 + Math.min(4, text.split(term).length - 2);
        if (!snippet || s < 20) snippet = excerpt(entry.text, at, term.length);
      }
      if (!s && !entry.trail.toLowerCase().includes(term)) matchedAll = false;
      score += s;
    }
    if (matchedAll && score > 0) hits.push({ entry, score, snippet });
  }
  return hits.sort((a, b) => b.score - a.score).slice(0, limit);
}

function excerpt(text: string, at: number, len: number): string {
  const start = Math.max(0, at - 40);
  const end = Math.min(text.length, at + len + 80);
  return `${start > 0 ? '…' : ''}${text.slice(start, end)}${end < text.length ? '…' : ''}`;
}
