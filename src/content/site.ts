/** Navigation queries over the build-time SiteData. */
import site from 'virtual:wiki/site';
import type { NavNode } from '../shared/types.ts';

export { site };

const byId = new Map<string, NavNode>();
const parentById = new Map<string, NavNode | null>();
/** Every page in reading order (depth-first). */
export const readingOrder: NavNode[] = [];

(function index(nodes: NavNode[], parent: NavNode | null) {
  for (const node of nodes) {
    byId.set(node.id, node);
    parentById.set(node.id, parent);
    readingOrder.push(node);
    index(node.children, node);
  }
})(site.nav, null);

export function findNode(id: string): NavNode | undefined {
  return byId.get(id);
}

/** Ancestors from the root down, excluding the node itself. */
export function ancestorsOf(id: string): NavNode[] {
  const out: NavNode[] = [];
  let cur = parentById.get(id) ?? null;
  while (cur) {
    out.unshift(cur);
    cur = parentById.get(cur.id) ?? null;
  }
  return out;
}

export function neighbours(id: string): { prev?: NavNode; next?: NavNode } {
  const i = readingOrder.findIndex((n) => n.id === id);
  return i < 0 ? {} : { prev: readingOrder[i - 1], next: readingOrder[i + 1] };
}
