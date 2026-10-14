import { parse as parseYaml, stringify as stringifyYaml } from 'yaml';
import type { Lang } from '../../site.config.ts';
import { siteConfig } from '../../site.config.ts';
import type { CourseRef, TextbookRef } from '../../src/shared/types.ts';

/**
 * Front matter schema of `index.<lang>.md`:
 *
 *   title        required  page title in this language
 *   description  optional  one-sentence summary used for search engines and link previews
 *   courses      optional  source language only: where the knowledge comes from (shown under the title)
 *                            courses: [{ code: "20240013", name: 离散数学(1), note: 可选备注 }]
 *   textbooks    optional  source language only: reference books (shown under the title)
 *                            textbooks: [{ title: 离散数学, author: 屈婉玲, edition: 3 }]
 *   source_hash  optional  translations only: `sourceHash()` of the source-language body this
 *                          translation was made from (written by `pnpm wiki stamp <id>`)
 */
export interface FrontMatter {
  title: string;
  description?: string;
  courses?: CourseRef[];
  textbooks?: TextbookRef[];
  source_hash?: string;
}

function checkList(value: unknown, key: string, fields: Record<string, 'required' | 'optional'>, errors: string[]): void {
  if (!Array.isArray(value) || !value.length) {
    errors.push(`front matter "${key}" must be a non-empty list`);
    return;
  }
  value.forEach((item, i) => {
    if (typeof item !== 'object' || item === null || Array.isArray(item)) {
      errors.push(`${key}[${i}] must be a mapping like { ${Object.keys(fields).join(', ')} }`);
      return;
    }
    const rec = item as Record<string, unknown>;
    for (const k of Object.keys(rec)) if (!(k in fields)) errors.push(`${key}[${i}]: unknown field "${k}" (allowed: ${Object.keys(fields).join(', ')})`);
    for (const [k, need] of Object.entries(fields)) {
      const v = rec[k];
      if (v === undefined) {
        if (need === 'required') errors.push(`${key}[${i}]: "${k}" is required`);
      } else if (!(typeof v === 'string' && v.trim()) && !(typeof v === 'number' && Number.isInteger(v) && v > 0)) {
        errors.push(`${key}[${i}]: "${k}" must be a non-empty string${k === 'edition' || k === 'code' ? ' or a number' : ''}`);
      }
    }
  });
}

export interface ParsedPageFile {
  frontMatter: FrontMatter;
  body: string;
  /** Number of lines before the body (front matter block), for mapping body lines to file lines. */
  bodyLineOffset: number;
}

const FM_RE = /^---\n([\s\S]*?)\n---\n?/;

export function parsePageFile(raw: string, lang: Lang): { value?: ParsedPageFile; errors: string[] } {
  const text = raw.replace(/^\uFEFF/, '').replace(/\r\n?/g, '\n');
  const m = FM_RE.exec(text);
  if (!m) return { errors: ['missing front matter block (--- title: ... ---) at the top of the file'] };
  let data: unknown;
  try {
    data = parseYaml(m[1]);
  } catch (e) {
    return { errors: [`front matter is not valid YAML: ${(e as Error).message}`] };
  }
  const errors: string[] = [];
  if (typeof data !== 'object' || data === null || Array.isArray(data)) {
    return { errors: ['front matter must be a YAML mapping'] };
  }
  const record = data as Record<string, unknown>;
  const allowed = lang === siteConfig.sourceLanguage ? ['title', 'description', 'courses', 'textbooks'] : ['title', 'description', 'source_hash'];
  for (const key of Object.keys(record)) {
    if (!allowed.includes(key)) errors.push(`unknown front matter key "${key}" (allowed: ${allowed.join(', ')})`);
  }
  for (const key of ['title', 'description', 'source_hash']) {
    if (key in record && (typeof record[key] !== 'string' || !(record[key] as string).trim())) {
      errors.push(`front matter "${key}" must be a non-empty string`);
    }
  }
  if (!('title' in record)) errors.push('front matter "title" is required');
  if ('courses' in record) checkList(record.courses, 'courses', { code: 'required', name: 'required', note: 'optional' }, errors);
  if ('textbooks' in record) checkList(record.textbooks, 'textbooks', { title: 'required', author: 'required', edition: 'optional' }, errors);
  if (errors.length) return { errors };

  const fmLines = m[0].split('\n').length - 1;
  return {
    value: {
      frontMatter: record as unknown as FrontMatter,
      body: text.slice(m[0].length),
      bodyLineOffset: fmLines,
    },
    errors,
  };
}

/** Serialise front matter + body back into a page file, with a stable key order. */
export function serializePageFile(fm: FrontMatter, body: string): string {
  const ordered: Record<string, unknown> = { title: fm.title };
  if (fm.description) ordered.description = fm.description;
  if (fm.courses) ordered.courses = fm.courses;
  if (fm.textbooks) ordered.textbooks = fm.textbooks;
  if (fm.source_hash) ordered.source_hash = fm.source_hash;
  const yaml = stringifyYaml(ordered, { lineWidth: 0, collectionStyle: 'block', flowCollectionPadding: true }).trimEnd();
  const trimmed = body.replace(/^\n+/, '').replace(/\s+$/, '');
  return `---\n${yaml}\n---\n${trimmed ? `\n${trimmed}\n` : ''}`;
}
