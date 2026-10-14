import type { Diagnostic } from '../../src/shared/types.ts';
import { rel } from './paths.ts';

/**
 * Collects problems found while building. Errors fail every build; warnings fail
 * `--strict` builds (used by `pnpm check` and CI).
 */
export class Diagnostics {
  readonly items: Diagnostic[] = [];

  error(file: string, message: string, line?: number): void {
    this.items.push({ level: 'error', file: rel(file), line, message });
  }

  warn(file: string, message: string, line?: number): void {
    this.items.push({ level: 'warning', file: rel(file), line, message });
  }

  get errorCount(): number {
    return this.items.filter((d) => d.level === 'error').length;
  }

  get warningCount(): number {
    return this.items.filter((d) => d.level === 'warning').length;
  }

  forFile(file: string): Diagnostic[] {
    const r = rel(file);
    return this.items.filter((d) => d.file === r);
  }

  format(): string {
    const sorted = [...this.items].sort(
      (a, b) => a.file.localeCompare(b.file) || (a.line ?? 0) - (b.line ?? 0),
    );
    return sorted
      .map((d) => {
        const where = d.line ? `${d.file}:${d.line}` : d.file;
        const tag = d.level === 'error' ? '\x1b[31merror\x1b[0m' : '\x1b[33mwarning\x1b[0m';
        return `${tag} ${where}\n  ${d.message}`;
      })
      .join('\n');
  }
}
