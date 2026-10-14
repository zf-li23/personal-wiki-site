/**
 * Page ids and URLs. Shared by the content pipeline and the client so both agree
 * on what a valid id is and where a page lives.
 *
 * A page id is a dot-separated list of positive integers without leading zeros:
 * "7", "7.4", "7.4.1.5". A child's id is its parent's id plus one more segment.
 */
import type { Lang } from '../../site.config.ts';

export const PAGE_ID_RE = /^[1-9]\d*(?:\.[1-9]\d*)*$/;

/** Directory name of a page: "<id>.<slug>", slug is lowercase kebab-case ASCII. */
export const PAGE_DIR_RE = /^([1-9]\d*(?:\.[1-9]\d*)*)\.([a-z0-9]+(?:-[a-z0-9]+)*)$/;

export function isPageId(value: string): boolean {
  return PAGE_ID_RE.test(value);
}

export function parentIdOf(id: string): string | null {
  const i = id.lastIndexOf('.');
  return i === -1 ? null : id.slice(0, i);
}

export function idSegments(id: string): number[] {
  return id.split('.').map(Number);
}

/** Numeric ordering: 7.2 < 7.10, 7.4 < 7.4.1. */
export function compareIds(a: string, b: string): number {
  const sa = idSegments(a);
  const sb = idSegments(b);
  for (let i = 0; i < Math.min(sa.length, sb.length); i++) {
    if (sa[i] !== sb[i]) return sa[i] - sb[i];
  }
  return sa.length - sb.length;
}

/** Router path of a page (without the site base), e.g. "/en/7.4.1.5/". */
export function pagePath(lang: Lang, id: string): string {
  return `/${lang}/${id}/`;
}

/** Router path of a language home page, e.g. "/en/". */
export function homePath(lang: Lang): string {
  return `/${lang}/`;
}
