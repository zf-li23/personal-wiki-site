/** Unit tests for the content pipeline. Run: pnpm test */
import assert from 'node:assert/strict';
import { spawnSync } from 'node:child_process';
import fs from 'node:fs';
import { createRequire } from 'node:module';
import os from 'node:os';
import path from 'node:path';
import { describe, it } from 'node:test';
import { BASE_PATH } from '../../site.config.ts';
import { compareIds, isPageId, parentIdOf } from '../../src/shared/page-id.ts';
import { search } from '../../src/shared/search.ts';
import { sourceLines } from '../../src/shared/sources.ts';
import { fixMarkdown } from './fix.ts';
import { checkHeadings, parseHeadingNumber, parseStatementLabel } from './numbering.ts';
import { sourceHash, translationStatus } from './build.ts';
import { Diagnostics } from './diagnostics.ts';
import { parsePageFile, serializePageFile } from './frontmatter.ts';
import type { Concept } from './glossary.ts';
import { buildLinkIndex, linkPage } from './linking.ts';
import { type RenderContext, renderHtml, renderMarkdown } from './markdown.ts';
import type { PlotResults } from './plots.ts';
import { lintPlotScript, plotImagePath, renderPlots, resolvePython, scriptHash } from './plots.ts';
import { PLOT_RENDERER } from './paths.ts';
import { type ContentTree, type PageSource, scanContent } from './scan.ts';

describe('page ids', () => {
  it('accepts purely numeric hierarchical ids only', () => {
    for (const ok of ['1', '7.4', '3.1.15', '10.2.33']) assert.ok(isPageId(ok), ok);
    for (const bad of ['0', '01', '3.1.13a', '1.', '.1', '1..2', 'a', '']) assert.ok(!isPageId(bad), bad);
  });
  it('orders numerically and finds parents', () => {
    assert.deepEqual(['7.10', '7.2', '7', '7.2.1'].sort(compareIds), ['7', '7.2', '7.2.1', '7.10']);
    assert.equal(parentIdOf('7.4.1'), '7.4');
    assert.equal(parentIdOf('7'), null);
  });
});

describe('front matter', () => {
  it('parses and round-trips', () => {
    const { value, errors } = parsePageFile('---\ntitle: 数理逻辑\n---\n\n## A\n', 'zh');
    assert.deepEqual(errors, []);
    assert.equal(value!.frontMatter.title, '数理逻辑');
    assert.equal(value!.bodyLineOffset, 3);
    assert.equal(serializePageFile(value!.frontMatter, value!.body), '---\ntitle: 数理逻辑\n---\n\n## A\n');
  });
  it('rejects unknown keys, missing titles and source_hash on the source language', () => {
    assert.match(parsePageFile('---\ntitle: x\ntags: [a]\n---\n', 'en').errors[0], /unknown front matter key "tags"/);
    assert.match(parsePageFile('---\ndescription: x\n---\n', 'en').errors[0], /"title" is required/);
    assert.match(parsePageFile('---\ntitle: x\nsource_hash: abc\n---\n', 'zh').errors[0], /unknown front matter key "source_hash"/);
    assert.match(parsePageFile('no front matter', 'zh').errors[0], /missing front matter/);
  });
});

function tempContent(files: Record<string, string>): string {
  const dir = fs.mkdtempSync(path.join(os.tmpdir(), 'wiki-test-'));
  for (const [rel, text] of Object.entries(files)) {
    fs.mkdirSync(path.dirname(path.join(dir, rel)), { recursive: true });
    fs.writeFileSync(path.join(dir, rel), text);
  }
  return dir;
}

const page = (title: string) => `---\ntitle: ${title}\n---\n`;

describe('scan', () => {
  it('builds the tree from a valid layout', () => {
    const dir = tempContent({
      '1.logic/index.zh.md': page('逻辑'),
      '1.logic/index.en.md': page('Logic'),
      '1.logic/1.1.propositions/index.zh.md': page('命题'),
      '1.logic/1.1.propositions/index.en.md': page('Propositions'),
      '1.logic/1.1.propositions/assets/fig.png': '',
    });
    const diag = new Diagnostics();
    const tree = scanContent(diag, dir);
    assert.deepEqual(diag.items, []);
    assert.deepEqual(tree.rootIds, ['1']);
    assert.deepEqual(tree.pages.get('1')!.childIds, ['1.1']);
    assert.deepEqual(tree.pages.get('1.1')!.assets, ['fig.png']);
  });
  it('reports bad names, misplaced ids, missing translations and stray files', () => {
    const dir = tempContent({
      '1.logic/index.zh.md': page('逻辑'),
      '1.logic/index.en.md': page('Logic'),
      '1.logic/2.1.wrong-parent/index.zh.md': page('x'),
      '1.logic/1.2a.letter/index.zh.md': page('x'),
      '1.logic/1.1.only-zh/index.zh.md': page('x'),
      '1.logic/notes.txt': '',
    });
    const diag = new Diagnostics();
    scanContent(diag, dir);
    const messages = diag.items.map((d) => d.message).join('\n');
    assert.match(messages, /page id "2.1" does not match its location/);
    assert.match(messages, /page directory name must be "<id>.<slug>"/);
    assert.match(messages, /missing index.en.md/);
    assert.match(messages, /unexpected file in a page directory/);
  });
});

function fakePage(id: string, extra: Partial<PageSource> = {}): PageSource {
  return { id, slug: 'p', dir: `/content/${id}.p`, parentId: null, files: {}, assets: [], plotFiles: [], childIds: [], ...extra };
}

async function render(body: string, opts: { pages?: PageSource[]; plots?: PlotResults; page?: PageSource } = {}) {
  const current = opts.page ?? fakePage('3.1.13');
  const pages = new Map([[current.id, current], ...(opts.pages ?? []).map((p) => [p.id, p] as const)]);
  const tree: ContentTree = { pages, rootIds: [...pages.keys()] };
  const diag = new Diagnostics();
  const ctx: RenderContext = {
    page: current,
    tree,
    plots: opts.plots ?? new Map(),
    diag,
    file: '/content/1.p/index.zh.md',
    lineOffset: 3,
    linkLang: 'en',
    contentLang: 'zh',
    usedPlots: new Set(),
    usedAssets: new Set(),
  };
  const out = await renderMarkdown(body, ctx);
  return { out, html: renderHtml(out), diag, messages: diag.items.map((d) => `${d.level}:${d.line}:${d.message}`) };
}

describe('markdown rendering', () => {
  it('rewrites internal links into the reader language and checks targets', async () => {
    const { out, html, messages } = await render('[a](/3.1.12#x) and [b](/9)', { pages: [fakePage('3.1.12')] });
    assert.match(html, new RegExp(`href="${BASE_PATH}en/3.1.12/#x" data-internal`));
    assert.ok(messages.some((m) => m.includes('link to unknown page "9"')));
    assert.deepEqual(out.links.map((l) => [l.targetId, l.anchor]), [['3.1.12', 'x'], ['9', undefined]]);
  });

  it('assigns heading ids (custom {#id} wins) and builds the TOC from h2/h3', async () => {
    const { out, html } = await render('## 13.1. 条件期望 $E(X)$ {#cond-exp}\n\n### 13.1.1. Sub\n\n#### 13.1.1.1. Deep\n\n## 小结');
    assert.deepEqual(out.headings, [
      { id: 'cond-exp', text: '13.1. 条件期望 E(X)', depth: 2 },
      { id: 'sec-13.1.1', text: '13.1.1. Sub', depth: 3 },
      { id: '小结', text: '小结', depth: 2 },
    ]);
    assert.match(html, /<h4 id="sec-13.1.1.1">/);
    assert.match(html, /<h2 id="cond-exp">/);
    assert.ok(!html.includes('{#cond-exp}'));
  });

  it('rejects legacy syntax with file line numbers', async () => {
    const { messages } = await render('# Title\n\ntext \\(x\\)\n\n```python-plot\nx\n```');
    assert.ok(messages.some((m) => m.startsWith('error:4:do not use "# " headings')));
    assert.ok(messages.some((m) => m.startsWith('error:6:use $...$')));
    assert.ok(messages.some((m) => m.startsWith('error:8:inline ```python-plot')));
  });

  it('embeds plots as themed figures with source', async () => {
    const pg = fakePage('3.1.13', { plotFiles: ['growth.py'] });
    const plots: PlotResults = new Map([
      [path.join(pg.dir, 'plots/growth.py'), { key: 'abc', imageDir: '/tmp/abc', imagePrefix: '', frozen: false, figures: [{ width: 800, height: 600 }], source: 'import numpy' }],
    ]);
    const { html, diag } = await render('![增长曲线](./plots/growth.py)', { page: pg, plots });
    assert.equal(diag.errorCount, 0);
    assert.match(html, /<figure class="wiki-plot">/);
    assert.match(html, new RegExp(`src="${BASE_PATH}plots/abc/0-light.webp"[^>]*width="400" height="300"`));
    assert.match(html, /0-dark\.webp/);
    assert.match(html, /<figcaption>增长曲线<\/figcaption>/);
    assert.match(html, /<details class="wiki-plot-source">/);
    assert.ok(!html.includes('<p><figure'), 'figure must replace the paragraph');
  });

  it('resolves assets, wraps tables, reports bad images and KaTeX errors', async () => {
    const pg = fakePage('3.1.13', { assets: ['a.png'] });
    const { html, messages } = await render('![图](./assets/a.png)\n\n![](missing.png)\n\n| a |\n|---|\n| 1 |\n\n$\\frac{1}$', { page: pg });
    assert.match(html, new RegExp(`<figure class="wiki-figure"><img src="${BASE_PATH}media/3.1.13/a.png"`));
    assert.match(html, /<div class="table-wrap"><table>/);
    assert.ok(messages.some((m) => m.includes('unsupported image source "missing.png"')));
    assert.ok(messages.some((m) => m.startsWith('warning:') && m.includes('KaTeX could not render')));
  });

  it('renders mhchem chemistry with the same KaTeX version the client styles with', async () => {
    const { diag } = await render('$\\ce{A + B -> C}$');
    assert.equal(diag.warningCount, 0);
    const req = createRequire(import.meta.url);
    const own = req('katex/package.json').version;
    const viaRehype = createRequire(req.resolve('rehype-katex'))('katex/package.json').version;
    assert.equal(own, viaRehype, 'package.json "katex" must equal the version rehype-katex renders with');
  });

  it('turns mermaid fences into diagram placeholders and adds code-block chrome', async () => {
    const { html } = await render('```mermaid\ngraph TD; A-->B;\n```\n\n```python\nprint(1)\n```');
    assert.match(html, /<div class="wiki-mermaid"><pre class="wiki-mermaid-source">graph TD; A-->B;/);
    assert.match(html, /<div class="code-block"><div class="code-block-header"><span class="code-lang">python<\/span><button type="button" class="copy-button" data-copy="">Copy<\/button>/);
  });
});

describe('plot script lint', () => {
  it('flags CJK text, savefig and plt.show', () => {
    const diag = new Diagnostics();
    lintPlotScript('/x.py', "plt.title('增长')\nplt.savefig('a.png')\nplt.show()\n# plt.show() in a comment is fine\n", diag);
    assert.deepEqual(diag.items.map((d) => d.line), [1, 2, 3]);
  });
});

describe('plot renderer (needs the Python env; skipped without it)', () => {
  const python = resolvePython();
  const available = spawnSync(python, ['-c', 'import matplotlib, PIL'], { encoding: 'utf8' }).status === 0;
  it('keeps dark surfaces dark and turns explicit black ink light', { skip: !available }, () => {
    const dir = fs.mkdtempSync(path.join(os.tmpdir(), 'wiki-plot-'));
    const script = path.join(dir, 'p.py');
    fs.writeFileSync(script, "import matplotlib.pyplot as plt\nfig, ax = plt.subplots(figsize=(2, 2))\nax.plot([0, 1], [0, 1], 'k-', lw=8, label='a')\nax.legend(loc='upper left')\n");
    const r = spawnSync(python, [PLOT_RENDERER, script, path.join(dir, 'out')], { encoding: 'utf8' });
    assert.equal(r.status, 0, r.stderr);
    const probe = spawnSync(python, ['-c', [
      'from PIL import Image; im = Image.open(__import__("sys").argv[1]).convert("RGB"); w, h = im.size',
      'print(im.getpixel((w * 3 // 4, h * 3 // 4)), im.getpixel((w // 2, h // 2)))',
    ].join('\n'), path.join(dir, 'out', '0-dark.webp')], { encoding: 'utf8' });
    const [bg, line] = [...probe.stdout.matchAll(/\((\d+), (\d+), (\d+)\)/g)].map((m) => m.slice(1).map(Number));
    assert.ok(Math.max(...bg) < 60, `axes background should stay dark, got ${bg}`);
    assert.ok(Math.min(...line) > 180, `black ink should become light, got ${line}`);
  });
});

describe('frozen plots', () => {
  it('uses committed images without running the script, and warns once the script changes', async () => {
    const dir = tempContent({
      '1.p/index.zh.md': page('页'),
      '1.p/index.en.md': page('Page'),
      // Would fail if executed: proves a frozen script is never run.
      '1.p/plots/slow.py': 'raise SystemExit(1)\n',
      '1.p/plots/slow.frozen.0-light.webp': 'L',
      '1.p/plots/slow.frozen.0-dark.webp': 'D',
    });
    const script = path.join(dir, '1.p/plots/slow.py');
    const meta = { figures: [{ width: 10, height: 10 }], sourceHash: scriptHash('raise SystemExit(1)\n') };
    fs.writeFileSync(path.join(dir, '1.p/plots/slow.frozen.json'), JSON.stringify(meta));
    const run = async () => {
      const diag = new Diagnostics();
      const results = await renderPlots(scanContent(diag, dir), diag, { prune: false });
      return { diag, result: results.get(script)! };
    };
    const first = await run();
    assert.deepEqual(first.diag.items, []);
    assert.ok(first.result.frozen && !first.result.error);
    assert.equal(plotImagePath(first.result, 0, 'dark'), path.join(dir, '1.p/plots/slow.frozen.0-dark.webp'));
    fs.appendFileSync(script, '# edited\n');
    const second = await run();
    assert.match(second.diag.items[0].message, /script changed since it was frozen/);
    assert.equal(second.result.key, first.result.key, 'the published images stay the same');
  });
});

describe('translation status', () => {
  const withFiles = (zh: string, en: string, hash?: string): PageSource =>
    fakePage('1', {
      files: {
        zh: { path: 'zh', frontMatter: { title: 'z' }, body: zh, bodyLineOffset: 3 },
        en: { path: 'en', frontMatter: { title: 'e', source_hash: hash }, body: en, bodyLineOffset: 3 },
      },
    });
  it('derives status from bodies and source_hash', () => {
    assert.equal(translationStatus(withFiles('', ''), 'en'), 'empty');
    assert.equal(translationStatus(withFiles('中文', ''), 'en'), 'untranslated');
    assert.equal(translationStatus(withFiles('中文', 'English', 'nope'), 'en'), 'stale');
    assert.equal(translationStatus(withFiles('中文', 'English', sourceHash('中文\n')), 'en'), 'translated');
    assert.equal(translationStatus(withFiles('中文', ''), 'zh'), 'source');
  });
});

describe('search', () => {
  const entries = [
    { id: '3.1.13', title: '中心极限定理', trail: '统计学 / 概率论', headings: ['基本定理'], text: '独立同分布的随机变量之和' },
    { id: '3.1.12', title: '大数定律', trail: '统计学 / 概率论', headings: [], text: '与中心极限定理不同，大数定律描述样本均值' },
    { id: '2.1', title: 'Linear Algebra', trail: 'Mathematics', headings: ['Eigenvalues'], text: 'matrices' },
  ];
  it('ranks title matches above body matches and requires every term', () => {
    assert.deepEqual(search(entries, '中心极限').map((h) => h.entry.id), ['3.1.13', '3.1.12']);
    assert.deepEqual(search(entries, '概率论 大数').map((h) => h.entry.id), ['3.1.12']);
    assert.deepEqual(search(entries, 'EIGEN').map((h) => h.entry.id), ['2.1']);
    assert.deepEqual(search(entries, '   '), []);
  });
});

describe('knowledge sources', () => {
  it('validates courses/textbooks and formats them identically everywhere', () => {
    const fm = '---\ntitle: 概率论\ncourses:\n  - { code: "40160713", name: 初等概率论 }\n  - { code: "10420803", name: 概率论与数理统计, note: 概率论部分 }\ntextbooks:\n  - { title: 概率论基础, author: 李贤平, edition: 3 }\n---\n';
    const parsed = parsePageFile(fm, 'zh');
    assert.deepEqual(parsed.errors, []);
    const { courses, textbooks } = parsed.value!.frontMatter;
    assert.deepEqual(sourceLines(courses, textbooks, 'zh'), [
      { label: '对应课程', value: '40160713 初等概率论；10420803 概率论与数理统计（概率论部分）' },
      { label: '参考书', value: '《概率论基础》，李贤平，第 3 版' },
    ]);
    assert.equal(sourceLines(undefined, textbooks, 'en')[0].value, '概率论基础, 李贤平, 3rd ed.');
    assert.equal(serializePageFile(parsed.value!.frontMatter, '').includes('note: 概率论部分'), true);
    assert.match(parsePageFile('---\ntitle: x\ntextbooks:\n  - { title: A }\n---\n', 'zh').errors[0], /"author" is required/);
    assert.match(parsePageFile('---\ntitle: x\ncourses: []\n---\n', 'en').errors[0], /unknown front matter key "courses"/);
  });
});

describe('numbering rules', () => {
  it('parses heading numbers and flags non-canonical formats', () => {
    assert.deepEqual(parseHeadingNumber('13.1. 基本概念'), { number: ['13', '1'], title: '基本概念', wellFormed: true });
    assert.equal(parseHeadingNumber('13.1 基本概念').wellFormed, false);
    assert.equal(parseHeadingNumber('2025年').number, undefined);
  });
  it('checks levels, prefixes and sequences of chapter headings', () => {
    const problems = (hs: [number, string][]) => checkHeadings(hs.map(([depth, text]) => ({ depth, text })), ['13']).map((p) => p.message);
    assert.deepEqual(problems([[2, '13.1. A'], [3, '13.1.1. B'], [3, '13.1.2. C'], [2, '13.2. D'], [2, '小结'], [3, '要点']]), []);
    assert.match(problems([[2, '13.1. A'], [3, '13.1.1. B'], [3, '13.1.3. C']])[0], /breaks the sequence: expected 13.1.2./);
    assert.match(problems([[2, '13.1. A'], [4, '13.1.1.1. B']])[0], /heading level skipped/);
    assert.match(problems([[2, '12.1. A']])[0], /does not fit here/);
    assert.match(problems([[2, '13.1. A'], [3, '背景']])[0], /must be numbered too/);
  });
  it('parses statement labels in both languages and rejects ordinary bold text', () => {
    assert.deepEqual(parseStatementLabel('定理 13.2.1（中心极限定理）'), { kind: 'thm', word: '定理', number: ['13', '2', '1'], name: '中心极限定理', canonical: true });
    assert.equal(parseStatementLabel('Theorem 2.1 (CLT)')?.canonical, true);
    assert.equal(parseStatementLabel('定理1.')?.canonical, false);
    for (const plain of ['注意', '例子', '定理证明']) assert.equal(parseStatementLabel(plain), null, plain);
  });
  it('fix rewrites formats only, never code blocks', () => {
    const { text } = fixMarkdown(['## 13.1 基本概念', '### **13.1.1 背景**', '- **推论1**（标准化平方和）：若', '**定义 8 (充分统计量).** 如果', '```', '## 1.1 code', '```'].join('\n'), 'zh');
    assert.deepEqual(text.split('\n'), ['## 13.1. 基本概念', '### 13.1.1. 背景', '- **推论 1（标准化平方和）**：若', '**定义 8（充分统计量）** 如果', '```', '## 1.1 code', '```']);
  });
});

describe('statements and page roles', () => {
  it('wraps numbered statements with their display math, anchors equations, and checks numbers', async () => {
    const { out, html, messages } = await render('## 13.2. 定理\n\n**定理 13.2.1（中心极限定理）** 设\n\n$$\nS_n \\tag{13.1}\n$$\n\n证明略。\n\n**定义 12.1.1** 错号');
    assert.deepEqual(out.statements.map((x) => [x.kind, x.number, x.anchor]), [['thm', '13.2.1', 'thm-13.2.1'], ['eq', '13.1', 'eq-13.1']]);
    assert.match(html, /<div class="wiki-stmt wiki-stmt-thm" id="thm-13.2.1" data-kind="thm"><p><strong class="wiki-stmt-label">定理 13.2.1（中心极限定理）<\/strong>/);
    assert.match(html, /<div class="wiki-eq" id="eq-13.1">/);
    assert.ok(/<\/div>\s*<p>证明略/.test(html), 'the proof paragraph is not part of the statement');
    assert.ok(messages.some((m) => m.includes('定义 12.1.1: numbers on this page start with 13.')));
  });
  it('rejects headings on discipline and course pages', async () => {
    const { messages } = await render('概述\n\n## 课程目标', { page: fakePage('3.1') });
    assert.ok(messages.some((m) => m.includes('course pages are overviews without headings')));
  });
});

describe('cross-page linking', () => {
  const concepts: Concept[] = [
    { id: 'convergence-in-distribution', zh: '依分布收敛', en: 'convergence in distribution', aliases: [] },
    { id: 'law-of-large-numbers', zh: '大数定律', en: 'law of large numbers', aliases: [] },
    { id: 'bifurcation', zh: '分岔', en: 'bifurcation', aliases: [] },
  ];
  async function site(pages: Record<string, string>) {
    const sources = Object.fromEntries(Object.keys(pages).map((id) => [id, fakePage(id)]));
    const tree: ContentTree = { pages: new Map(Object.entries(sources)), rootIds: [] };
    const rendered = new Map<string, Awaited<ReturnType<typeof render>>['out']>();
    for (const [id, body] of Object.entries(pages)) rendered.set(id, (await render(body, { page: sources[id], pages: Object.values(sources) })).out);
    const diag = new Diagnostics();
    const order = Object.keys(pages);
    const index = buildLinkIndex(tree, rendered, new Map(order.map((id) => [id, id])), concepts, order, diag);
    const results = new Map(order.map((id) => [id, linkPage({ pageId: id, out: rendered.get(id)!, linkLang: 'zh', tree, index, readingOrder: new Map(order.map((x, i) => [x, i])), diag, file: id })]));
    return { index, diag, html: (id: string) => renderHtml(rendered.get(id)!), results };
  }
  it('resolves statement references within the course and links bold concept names to definitions', async () => {
    const s = await site({
      '3.1.12': '## 12.1. 定律\n\n大数定律（law of large numbers）描述均值。由定理 13.2.1 可知。',
      '3.1.13': '## 13.1. 收敛\n\n**定义 13.1.1（依分布收敛）** 设……\n\n## 13.2. 定理\n\n**定理 13.2.1** 见定义 13.1.1。**大数定律**与大数定律，**分岔图**不是**分岔**，**分岔**。',
    });
    assert.deepEqual(s.diag.items, []);
    assert.equal(s.index.conceptSites.get('convergence-in-distribution')?.anchor, 'def-13.1.1');
    assert.equal(s.index.conceptSites.get('law-of-large-numbers')?.anchor, 'concept-law-of-large-numbers');
    assert.match(s.html('3.1.12'), /<dfn id="concept-law-of-large-numbers" class="wiki-dfn"/);
    assert.match(s.html('3.1.12'), new RegExp(`<a href="${BASE_PATH}zh/3.1.13/#thm-13.2.1" class="wiki-ref" data-internal="">定理 13.2.1</a>`));
    assert.match(s.html('3.1.13'), /<a href="#def-13.1.1" class="wiki-ref">定义 13.1.1<\/a>/);
    const p13 = s.html('3.1.13');
    assert.match(p13, new RegExp(`<a href="${BASE_PATH}zh/3.1.12/#concept-law-of-large-numbers" class="concept-ref" data-concept="law-of-large-numbers" data-internal=""><strong>大数定律</strong></a>与大数定律`), 'bold mention links, plain text does not');
    assert.equal((p13.match(/<strong class="concept-ref" data-concept="bifurcation">分岔<\/strong>/g) ?? []).length, 2, 'every bold mention of an undefined concept gets a hover card');
    assert.match(p13, /<strong>分岔图<\/strong>/, 'a longer bold phrase is not a mention');
    assert.deepEqual([...s.results.get('3.1.12')!.targets], ['3.1.13']);
  });
  it('treats single-character concepts like any other: only bold mentions link', async () => {
    concepts.push({ id: 'group', zh: '群', en: 'group', aliases: [] });
    const s = await site({ '1.3.2': '## 2.2. 群\n\n**定义 2.2.1（群）** 设……', '1.3.3': '## 3.1. 环\n\n每个**群**都有单位元，循环群也一样。' });
    concepts.pop();
    assert.equal(s.index.conceptSites.get('group')?.anchor, 'def-2.2.1');
    assert.equal((s.html('1.3.3').match(/class="concept-ref"/g) ?? []).length, 1);
  });
  it('takes a bold concept name inside a 定义 as its definition site, and reports other bold text', async () => {
    const s = await site({
      '1.1.1': '## 1.1. 联结词\n\n**定义 1.1.1** 称 $P \\land Q$ 为**依分布收敛**，其中 $P$ 为**前件**。\n\n**证明** 这是**重要的一点**。',
      '1.1.2': '## 2.1. A\n\n由**依分布收敛**可知。',
    });
    assert.equal(s.index.conceptSites.get('convergence-in-distribution')?.anchor, 'def-1.1.1');
    assert.match(s.html('1.1.2'), /href="[^"]*1\.1\.1\/#def-1\.1\.1" class="concept-ref"/);
    assert.deepEqual(s.results.get('1.1.1')!.plainBold, [
      { text: '前件', inDefinition: true },
      { text: '重要的一点', inDefinition: false },
    ]);
  });
  it('recognises a scoped concept only inside its scope', async () => {
    concepts.push({ id: 'characteristic-function', zh: '特征函数', en: 'characteristic function', aliases: [], scope: ['3'] });
    const s = await site({ '1.2.3': '## 3.1. A\n\n**特征函数**', '3.1.11': '## 11.1. B\n\n**特征函数**' });
    concepts.pop();
    assert.ok(!s.html('1.2.3').includes('concept-ref'));
    assert.match(s.html('3.1.11'), /data-concept="characteristic-function"/);
  });
  it('allows restating a definition but not a second English annotation', async () => {
    const s = await site({
      '3.1.12': '## 12.1. A\n\n大数定律（law of large numbers）',
      '3.1.14': '## 14.1. B\n\n大数定律（law of large numbers）再述',
    });
    assert.match(s.diag.items[0].message, /already defined on page 3.1.12/);
  });
});
