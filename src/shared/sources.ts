/**
 * One wording for knowledge sources (front matter `courses` / `textbooks`), shared by the client
 * and the static prerender so every page shows them in the same place and format.
 */
import type { Lang } from '../../site.config.ts';
import type { CourseRef, TextbookRef } from './types.ts';

const ORDINAL = ['th', 'st', 'nd', 'rd'];

function ordinal(n: number): string {
  const v = n % 100;
  return `${n}${ORDINAL[(v - 20) % 10] ?? ORDINAL[v] ?? ORDINAL[0]}`;
}

const HAN = /\p{Script=Han}/u;

export function formatCourse(c: CourseRef, lang: Lang): string {
  const base = `${c.code} ${lang === 'en' && c.name_en ? c.name_en : c.name}`;
  const note = lang === 'en' ? (c.note_en ?? c.note) : c.note;
  if (!note) return base;
  return lang === 'zh' ? `${base}（${note}）` : `${base} (${note})`;
}

export function formatTextbook(b: TextbookRef, lang: Lang): string {
  const edition = b.edition === undefined ? '' : typeof b.edition === 'number' ? (lang === 'zh' ? `第 ${b.edition} 版` : `${ordinal(b.edition)} ed.`) : String(b.edition);
  if (lang === 'zh') {
    const title = b.title_zh ?? b.title;
    return [HAN.test(title) ? `《${title}》` : title, b.author, edition].filter(Boolean).join('，');
  }
  if (!b.title_en) return [b.title, b.author, edition].filter(Boolean).join(', ');
  // A translated title is not the book's real title: say which language the book is in.
  return `${[b.title_en, b.author_en ?? b.author, edition].filter(Boolean).join(', ')}${HAN.test(b.title) ? ' (in Chinese)' : ''}`;
}

export function sourceLines(courses: CourseRef[] | undefined, textbooks: TextbookRef[] | undefined, lang: Lang): { label: string; value: string }[] {
  const sep = lang === 'zh' ? '；' : '; ';
  const lines: { label: string; value: string }[] = [];
  if (courses?.length) lines.push({ label: lang === 'zh' ? '对应课程' : 'Course', value: courses.map((c) => formatCourse(c, lang)).join(sep) });
  if (textbooks?.length) lines.push({ label: lang === 'zh' ? '参考书' : 'References', value: textbooks.map((b) => formatTextbook(b, lang)).join(sep) });
  return lines;
}
