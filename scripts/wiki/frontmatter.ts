import { parse as parseYaml, stringify as stringifyYaml } from 'yaml';
import type { Lang } from '../../site.config.ts';
import { siteConfig } from '../../site.config.ts';

/**
 * Front matter schema of `index.<lang>.md`:
 *
 *   title        required  page title in this language
 *   description  optional  one-sentence summary used for search engines and link previews
 *   source_hash  optional  translations only: `sourceHash()` of the source-language body this
 *                          translation was made from (written by `pnpm wiki stamp <id>`)
 */
export interface FrontMatter {
  title: string;
  description?: string;
  source_hash?: string;
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
  const allowed = lang === siteConfig.sourceLanguage ? ['title', 'description'] : ['title', 'description', 'source_hash'];
  for (const key of Object.keys(record)) {
    if (!allowed.includes(key)) errors.push(`unknown front matter key "${key}" (allowed: ${allowed.join(', ')})`);
  }
  for (const key of ['title', 'description', 'source_hash']) {
    if (key in record && (typeof record[key] !== 'string' || !(record[key] as string).trim())) {
      errors.push(`front matter "${key}" must be a non-empty string`);
    }
  }
  if (!('title' in record)) errors.push('front matter "title" is required');
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
  const ordered: Record<string, string> = { title: fm.title };
  if (fm.description) ordered.description = fm.description;
  if (fm.source_hash) ordered.source_hash = fm.source_hash;
  const yaml = stringifyYaml(ordered, { lineWidth: 0 }).trimEnd();
  const trimmed = body.replace(/^\n+/, '').replace(/\s+$/, '');
  return `---\n${yaml}\n---\n${trimmed ? `\n${trimmed}\n` : ''}`;
}
