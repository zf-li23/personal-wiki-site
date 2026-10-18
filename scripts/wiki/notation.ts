/**
 * Notation rules for formulas (CONTENT_GUIDE §7). Each rule finds a written form that the
 * conventions replace, inside math only. The build warns about every match; `pnpm wiki fix`
 * rewrites the matches of rules that have a `fix` (those are unambiguous). Rules without a fix
 * need a human or an agent to decide (e.g. whether a `d` is a differential).
 *
 * Fonts carry meaning (ISO 80000-2): upright e, i, d; \mathbb{P}, \mathbb{E}; bold italic vectors;
 * \mathsf{T} for the transpose; \operatorname for multi-letter operators.
 */

import remarkMath from 'remark-math';
import remarkParse from 'remark-parse';
import { unified } from 'unified';
import { visit } from 'unist-util-visit';

export interface NotationRule {
  id: string;
  /** What to write instead (shown in the warning). */
  advice: string;
  /** Global regex over the TeX source of one formula. */
  pattern: RegExp;
  /** Replacement for `pnpm wiki fix`; omitted when the rewrite needs judgement. */
  fix?: string | ((match: string, ...groups: string[]) => string);
  /** Page-id prefixes where the rule applies (default: everywhere). */
  scope?: string[];
  /** The rule applies only to formulas matching this. */
  onlyIn?: RegExp;
}

// Not preceded by a letter or a backslash (so `\exp`, `\Pr`, `ae^` are not touched).
const START = String.raw`(?<![\\A-Za-z])`;
const OPERATORS: Record<string, string> = { var: 'Var', cov: 'Cov', corr: 'Corr', sign: 'sgn' };
const GREEK: Record<string, string> = Object.fromEntries(
  [...'αβγδεζηθικλμνξοπρστυφχψω'].map((c, i) => [c, ['alpha', 'beta', 'gamma', 'delta', 'varepsilon', 'zeta', 'eta', 'theta', 'iota', 'kappa', 'lambda', 'mu', 'nu', 'xi', 'o', 'pi', 'rho', 'sigma', 'tau', 'upsilon', 'varphi', 'chi', 'psi', 'omega'][i]]),
);
for (const [c, n] of Object.entries({ Γ: 'Gamma', Δ: 'Delta', Θ: 'Theta', Λ: 'Lambda', Ξ: 'Xi', Π: 'Pi', Σ: 'Sigma', Φ: 'Phi', Ψ: 'Psi', Ω: 'Omega' })) GREEK[c] = n;
const op = (name: string) => `\\operatorname{${OPERATORS[name.toLowerCase()] ?? (/^(Var|Cov|Corr)$/i.test(name) ? name[0].toUpperCase() + name.slice(1).toLowerCase() : name)}}`;

export const NOTATION_RULES: NotationRule[] = [
  { id: 'vector-arrow', advice: String.raw`\boldsymbol{x} for vectors (not \vec)`, pattern: /\\vec\s*\{/g, fix: String.raw`\boldsymbol{` },
  { id: 'vector-arrow', advice: String.raw`\boldsymbol{x} for vectors (not \vec)`, pattern: /\\vec\s+([A-Za-z])/g, fix: (_m, x) => `\\boldsymbol{${x}}` },
  { id: 'number-set', advice: String.raw`\mathbb{R} for number sets`, pattern: /\\(?:mathbf|Bbb|bf)\s*\{?\s*([NZQRC])\s*\}?(?![A-Za-z])/g, fix: (_m, s) => `\\mathbb{${s}}` },
  { id: 'bold-upright', advice: String.raw`\boldsymbol{x} for bold (not \mathbf / \bm)`, pattern: /\\(?:mathbf|bm)\s*\{(?!\s*[NZQRC]\s*\})/g, fix: String.raw`\boldsymbol{` },
  {
    id: 'transpose',
    advice: String.raw`A^{\mathsf T} for the transpose (and A^{\mathsf H} for the conjugate transpose)`,
    // `^T` takes the single token T, so `x^TAx` is x^{T}Ax as well. A bare T counts only after a
    // matrix-like base (capital letter, `}` of \boldsymbol{x}, `)`), not after a subscript
    // (\int_{-T}^T, \sum_{t=1}^T) or a lowercase letter (n^T is a power).
    pattern: /(?<!_\{[^{}]*\}|_[A-Za-z0-9])(?<=[A-Z)\]}])\^\s*(?:\{\s*(?:T|\\top|\\intercal|\\mathrm\s*\{T\}|\\rm\s*T|\\text\s*\{T\})\s*\}|T)|\^\s*(?:\\top|\\intercal)/g,
    fix: String.raw`^{\mathsf T}`,
  },
  { id: 'transpose', advice: String.raw`A^{\mathsf H} for the conjugate transpose`, pattern: /(?<!_\{[^{}]*\}|_[A-Za-z0-9])(?<=[A-Z)\]}])\^\s*(?:\{\s*(?:H|\\mathrm\s*\{H\}|\\text\s*\{H\})\s*\}|H)/g, fix: String.raw`^{\mathsf H}` },
  // A space after \dots only when a letter follows (`...x` → `\dots x`, not `\dotsx`).
  { id: 'ellipsis', advice: String.raw`\dots or \cdots (not ...)`, pattern: /\.\.\.(?=([A-Za-z])?)/g, fix: (_m, letter) => (letter ? '\\dots ' : '\\dots') },
  {
    id: 'operator',
    advice: String.raw`\operatorname{Var}, \operatorname{tr}, … for multi-letter operators`,
    pattern: /\\(?:text|mathrm|mathop|rm)\s*\{\s*(Var|var|Cov|cov|Corr|corr|tr|rank|span|diag|sgn|sign)\s*\}/g,
    fix: (_m, name) => op(name),
  },
  // Not in discrete mathematics, where tr(R) is the composite closure t(r(R)).
  { id: 'operator', advice: String.raw`\operatorname{Var}, \operatorname{tr}, … for multi-letter operators`, pattern: new RegExp(String.raw`${START}(?<!\{)(Var|var|Cov|cov|Corr|corr|tr|rank|diag|span)(?=\s*[(\[])`, 'g'), fix: (_m, name) => op(name), scope: ['2', '3', '7'] },
  { id: 'operator', advice: String.raw`\operatorname{tr}, \operatorname{sgn} (short names)`, pattern: /\\operatorname\s*\{\s*(trace|sign)\s*\}/g, fix: (_m, name) => (name === 'trace' ? '\\operatorname{tr}' : '\\operatorname{sgn}') },
  { id: 'operator', advice: String.raw`\operatorname{Re}, \operatorname{Im}`, pattern: /\\(?:text|mathrm)\s*\{\s*(Re|Im)\s*\}/g, fix: (_m, name) => `\\operatorname{${name}}` },
  { id: 'group-name', advice: String.raw`\operatorname{GL}, \operatorname{SO}, … for classical groups`, pattern: new RegExp(String.raw`${START}(?<!\{)(GL|SL|SO|SU|Sp|SE)(?=\s*[(_])`, 'g'), fix: (_m, name) => `\\operatorname{${name}}` },
  { id: 'frobenius', advice: String.raw`\|A\|_{\mathrm{F}} for the Frobenius norm`, pattern: /(\\\||\\Vert)\s*_\s*(?:F|\{\s*F\s*\})(?![A-Za-z])/g, fix: (_m, bar) => `${bar}_{\\mathrm{F}}` },
  { id: 'stackrel', advice: String.raw`\overset{a}{b} (not \stackrel)`, pattern: /\\stackrel(?![A-Za-z])/g, fix: String.raw`\overset` },
  { id: 'empty-set', advice: String.raw`\varnothing for the empty set`, pattern: /\\emptyset(?![A-Za-z])/g, fix: String.raw`\varnothing` },
  { id: 'epsilon', advice: String.raw`\varepsilon (not \epsilon)`, pattern: /\\epsilon(?![A-Za-z])/g, fix: String.raw`\varepsilon` },
  { id: 'arrow', advice: String.raw`\to (not \rightarrow)`, pattern: /\\rightarrow(?![A-Za-z])/g, fix: String.raw`\to` },
  { id: 'unicode-greek', advice: String.raw`\alpha, \beta, … (not Unicode Greek letters in formulas)`, pattern: /[α-ωΑ-Ω]/g, fix: (m) => `\\${GREEK[m] ?? m} ` },
  { id: 'accent-braces', advice: String.raw`\bar{\boldsymbol{x}} (an accent needs braces around a command argument)`, pattern: /\\(bar|hat|tilde|dot|ddot|vec)\s*\\(boldsymbol|mathbf|mathrm|mathcal|mathbb)\s*\{([^{}]*)\}/g, fix: (_m, acc, font, arg) => `\\${acc}{\\${font}{${arg}}}` },
  { id: 'probability', advice: String.raw`\mathbb{P} for probability`, pattern: /\\Pr\b/g, fix: String.raw`\mathbb{P}` },
  // Not in discrete mathematics, where e is also the identity element of a group (e^{-1} = e).
  { id: 'euler-e', advice: String.raw`\mathrm{e} for Euler's number`, pattern: /(?<!\\(?:boldsymbol|mathbf|mathrm|operatorname|text)\{)(?<!\\[A-Za-z]*)e(?=\s*\^)(?!\s*\^\s*\{?\s*(?:\*|\\ast|\\prime|\\dagger|\\mathsf))/g, fix: String.raw`\mathrm{e}`, scope: ['2', '3', '7'] },
  { id: 'indicator', advice: String.raw`\boldsymbol{1}_A for the indicator (KaTeX has no blackboard 1)`, pattern: /\\mathbb\s*\{\s*1\s*\}/g, fix: String.raw`\boldsymbol{1}` },
  {
    id: 'differential',
    advice: String.raw`\mathrm{d}x for differentials`,
    pattern: /\\frac\s*\{\s*d(\^\s*\{?\d+\}?)?\s*([A-Za-z]?)\s*\}\s*\{\s*d\s*([A-Za-z])(\^\s*\{?\d+\}?)?\s*\}/g,
    fix: (_m, p1 = '', y = '', x, p2 = '') => `\\frac{\\mathrm{d}${p1}${y}}{\\mathrm{d}${x}${p2}}`,
  },
  {
    id: 'differential',
    advice: String.raw`\mathrm{d}x for differentials`,
    pattern: /(\\[,;!:]|[\s)}\]])d(\\[A-Za-z]+|[A-Za-z])(?![A-Za-z])/g,
    fix: (_m, before, x) => `${before}\\mathrm{d}${x}`,
    onlyIn: /\\i+nt|\\oint/,
  },
  { id: 'expectation', advice: String.raw`\mathbb{E} for expectation`, pattern: new RegExp(String.raw`${START}(?<![{_^])E(?=\s*[(\[]|[A-Z](?![A-Za-z]))`, 'g'), fix: String.raw`\mathbb{E}`, scope: ['3'] },
  { id: 'probability', advice: String.raw`\mathbb{P} for probability`, pattern: new RegExp(String.raw`${START}(?<![{_^])P(?=\s*(?:[(\[]|\\\{|\\left|\\big))(?!\s*\(\s*\\(?:lambda|theta|mu)\s*\))`, 'g'), fix: String.raw`\mathbb{P}`, scope: ['3'] },
];

function applies(rule: NotationRule, tex: string, pageId: string): boolean {
  if (rule.scope && !rule.scope.some((s) => pageId === s || pageId.startsWith(`${s}.`))) return false;
  return !rule.onlyIn || rule.onlyIn.test(tex);
}

/** Rules violated by one formula (one entry per rule id). */
export function checkNotation(tex: string, pageId: string): NotationRule[] {
  const seen = new Map<string, NotationRule>();
  for (const rule of NOTATION_RULES) {
    if (seen.has(rule.id) || !applies(rule, tex, pageId)) continue;
    if (new RegExp(rule.pattern.source, rule.pattern.flags).test(tex)) seen.set(rule.id, rule);
  }
  return [...seen.values()];
}

/** Apply every rule with a fix to one formula. */
export function fixNotation(tex: string, pageId: string): string {
  let out = tex;
  for (const rule of NOTATION_RULES) {
    if (!rule.fix || !applies(rule, out, pageId)) continue;
    const re = new RegExp(rule.pattern.source, rule.pattern.flags);
    out = typeof rule.fix === 'string' ? out.replace(re, rule.fix) : out.replace(re, rule.fix as (m: string, ...g: string[]) => string);
  }
  return out;
}

/** Rewrite the formulas of a Markdown body. Formulas are located by the same parser the build uses. */
export function fixNotationInMarkdown(body: string, pageId: string): { text: string; changes: number } {
  const tree = unified().use(remarkParse).use(remarkMath).parse(body);
  const spans: { start: number; end: number }[] = [];
  visit(tree, (node) => {
    if ((node.type === 'math' || node.type === 'inlineMath') && node.position?.start.offset !== undefined && node.position.end.offset !== undefined) {
      spans.push({ start: node.position.start.offset, end: node.position.end.offset });
    }
  });
  let text = body;
  let changes = 0;
  for (const { start, end } of spans.sort((a, b) => b.start - a.start)) {
    const tex = text.slice(start, end);
    const fixed = fixNotation(tex, pageId);
    if (fixed === tex) continue;
    text = text.slice(0, start) + fixed + text.slice(end);
    changes++;
  }
  return { text, changes };
}
