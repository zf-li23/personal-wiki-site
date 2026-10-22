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
import { checkNotation, fixNotation, fixNotationInMarkdown } from './notation.ts';
import { checkHeadings, parseHeadingNumber, parseStatementLabel } from './numbering.ts';
import { sourceHash, translationStatus } from './build.ts';
import { Diagnostics } from './diagnostics.ts';
import type { Lang } from '../../site.config.ts';
import { parsePageFile, serializePageFile } from './frontmatter.ts';
import { type Concept, conceptId } from './glossary.ts';
import { buildLinkIndex, linkPage } from './linking.ts';
import { type RenderContext, renderHtml, renderMarkdown } from './markdown.ts';
import type { PlotResults } from './plots.ts';
import { lintPlotScript, plotImagePath, renderPlots, resolvePython, scriptHash } from './plots.ts';
import { PLOT_RENDERER } from './paths.ts';
import { type ContentTree, type PageSource, scanContent, sourceLangOf } from './scan.ts';

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
    const { value, errors } = parsePageFile('---\ntitle: 数理逻辑\n---\n\n## A\n');
    assert.deepEqual(errors, []);
    assert.equal(value!.frontMatter.title, '数理逻辑');
    assert.equal(value!.bodyLineOffset, 3);
    assert.equal(serializePageFile(value!.frontMatter, value!.body), '---\ntitle: 数理逻辑\n---\n\n## A\n');
  });
  it('rejects unknown keys, missing titles and source_hash on the source language', () => {
    assert.match(parsePageFile('---\ntitle: x\ntags: [a]\n---\n').errors[0], /unknown front matter key "tags"/);
    assert.match(parsePageFile('---\ndescription: x\n---\n').errors[0], /"title" is required/);
    assert.match(parsePageFile('no front matter').errors[0], /missing front matter/);
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

describe('source language', () => {
  const file = (body: string, source_hash?: string) => ({ path: 'x', body, bodyLineOffset: 0, frontMatter: { title: 't', ...(source_hash ? { source_hash } : {}) } });
  it('is the file without source_hash, else the only written file, else the default', () => {
    assert.equal(sourceLangOf({ zh: file('中文'), en: file('') }), 'zh');
    assert.equal(sourceLangOf({ zh: file(''), en: file('English') }), 'en');
    assert.equal(sourceLangOf({ zh: file('中文', 'abc'), en: file('English') }), 'en');
    assert.equal(sourceLangOf({ zh: file('中文'), en: file('English', 'abc') }), 'zh');
    assert.equal(sourceLangOf({ zh: file('中文'), en: file('English') }), 'zh');
    assert.equal(sourceLangOf({ zh: file(''), en: file('') }), 'zh');
    const withCourses = { ...file('English'), frontMatter: { title: 't', courses: [{ code: '1', name: 'c' }] } };
    assert.equal(sourceLangOf({ zh: file('中文'), en: withCourses }), 'en');
  });
});

function fakePage(id: string, extra: Partial<PageSource> = {}): PageSource {
  return { id, slug: 'p', dir: `/content/${id}.p`, parentId: null, files: {}, sourceLang: 'zh', assets: [], plotFiles: [], childIds: [], ...extra };
}

async function render(body: string, opts: { pages?: PageSource[]; plots?: PlotResults; page?: PageSource; lang?: Lang } = {}) {
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
    contentLang: opts.lang ?? 'zh',
    usedPlots: new Set(),
    usedAssets: new Set(),
  };
  const out = await renderMarkdown(body, ctx);
  return { out, html: renderHtml(out), diag, messages: diag.items.map((d) => `${d.level}:${d.line}:${d.message}`) };
}

describe('fix: sub-item markers', () => {
  it('keeps "（1）" after a label out of the statement name', () => {
    assert.equal(fixMarkdown('**例 1.2.5**（1）设 x', 'zh').text, '**例 1.2.5**（1）设 x');
    assert.equal(fixMarkdown('**定理 9.6.1**（9.9）的解', 'zh').text, '**定理 9.6.1**（9.9）的解');
    assert.equal(fixMarkdown('**推论1**（标准化平方和）：若', 'zh').text, '**推论 1（标准化平方和）**：若');
    assert.equal(fixMarkdown('**例 12.4.1**（Green 函数）求解', 'zh').text, '**例 12.4.1（Green 函数）** 求解');
  });
});

describe('notation', () => {
  it('rewrites unambiguous forms and respects scopes', () => {
    assert.equal(fixNotation(String.raw`\vec{x}^T A\vec x + Ae^{At} + a_1,...,a_n`, '2.1.1'), String.raw`\boldsymbol{x}^{\mathsf T} A\boldsymbol{x} + A\mathrm{e}^{At} + a_1,\dots,a_n`);
    assert.equal(fixNotation(String.raw`E(X)+EX+P\{X=1\}+\text{var}(X)+cov(X,Y)`, '3.1.8'), String.raw`\mathbb{E}(X)+\mathbb{E}X+\mathbb{P}\{X=1\}+\operatorname{Var}(X)+\operatorname{Cov}(X,Y)`);
    assert.equal(fixNotation(String.raw`\int f(x)dx + \frac{dy}{dx} + d(x,y)`, '2.2.4'), String.raw`\int f(x)\mathrm{d}x + \frac{\mathrm{d}y}{\mathrm{d}x} + d(x,y)`);
    // logic predicates, the group identity and power sets keep their letters
    assert.equal(fixNotation(String.raw`P(x) \land e^{-1} = e`, '1.3.2'), String.raw`P(x) \land e^{-1} = e`);
    assert.equal(fixNotation(String.raw`e^*_{b1} + e^{\prime} + e^{-t}`, '3.3.12'), String.raw`e^*_{b1} + e^{\prime} + \mathrm{e}^{-t}`);
    assert.deepEqual(checkNotation(String.raw`\mathbf{R}^n`, '2.1.1').map((r) => r.id), ['number-set']);
    // T as a variable: integral bounds, powers, the Poisson distribution, closures in set theory
    assert.equal(fixNotation(String.raw`\int_{-T}^T f + n^T + P(\lambda) + tr(R)`, '3.1.1'), String.raw`\int_{-T}^T f + n^T + P(\lambda) + \operatorname{tr}(R)`);
    assert.equal(fixNotation(String.raw`tr(R)`, '1.2.2'), 'tr(R)');
  });
  it('only touches formulas', () => {
    const { text, changes } = fixNotationInMarkdown('Text e^x and `A^T`.\n\n$$\nA^T\n$$\n\n```\nA^T\n```\n', '2.1.1');
    assert.equal(changes, 1);
    assert.equal(text, 'Text e^x and `A^T`.\n\n$$\nA^{\\mathsf T}\n$$\n\n```\nA^T\n```\n');
  });
});

describe('markdown rendering', () => {
  it('keeps a paragraph written directly under display math inside the statement', async () => {
    const { html } = await render('## 13.1. A\n\n**定义 13.1.1** 设\n\n$$\nAx = \\lambda x\n$$\n则称 $\\lambda$ 为**特征值**。\n\n另一段。');
    const block = html.slice(html.indexOf('id="def-13.1.1"'), html.indexOf('另一段'));
    assert.match(block, /则称/);
    assert.match(html, /<\/div>\s*<p>另一段/);
  });
  it('warns about Chinese text left on an English page', async () => {
    const { messages } = await render('## 13.1. Basics\n\nA set 集合 and $\\text{若}$.', { lang: 'en' });
    assert.equal(messages.filter((m) => m.includes('Chinese text on an English page')).length, 2);
    assert.equal((await render('## 13.1. 基本\n\n集合')).messages.length, 0);
  });
  it('groups adjacent ```<lang> tab blocks into one tabbed block', async () => {
    const { html, messages } = await render('```cpp tab\nint x = 1;\n```\n\n```python tab\nx = 1\n```\n\n```r\nx <- 1\n```\n\n```text\n1\n```\n\n```cpp tab\nalone\n```');
    assert.equal((html.match(/class="wiki-code-tabs"/g) ?? []).length, 1);
    assert.match(html, /<button type="button" role="tab" class="active" data-code-tab="cpp" aria-selected="true">C\+\+<\/button><button type="button" role="tab" data-code-tab="python" aria-selected="false">Python<\/button>/);
    assert.match(html, /<div data-code-panel="python" hidden><div class="code-block">/);
    assert.equal((html.match(/class="code-block"/g) ?? []).length, 5, 'untagged neighbours stay ordinary blocks');
    assert.deepEqual(messages.filter((m) => m.includes('tab block needs a neighbour')).length, 1);
  });
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
  it('draws ```smiles blocks as themable SVG at build time and reports bad SMILES', async () => {
    const { html, messages } = await render('```smiles\nCC(=O)O 1\n# comment\nCCO.CC(=O)O>>CC(=O)OCC.O\n```\n\n```smiles\nC1CC 化合物\n```');
    assert.equal((html.match(/class="wiki-chem-item"/g) ?? []).length, 2);
    assert.match(html, /<span class="wiki-chem-label">1<\/span>/);
    assert.match(html, /class='wiki-chem-svg'/);
    assert.doesNotMatch(html, /#000000|<\?xml/);
    assert.ok(messages.some((m) => m.includes('cannot parse the SMILES "C1CC"')));
    assert.ok(messages.some((m) => m.includes('must be language-neutral')));
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
  const chem = available && spawnSync(python, ['-c', 'import rdkit'], { encoding: 'utf8' }).status === 0;
  it('draws wikichem schemes (structures and curved arrows) in both themes', { skip: !chem }, () => {
    const dir = fs.mkdtempSync(path.join(os.tmpdir(), 'wiki-chem-'));
    const script = path.join(dir, 'm.py');
    fs.writeFileSync(script, 'from wikichem import Scheme\ns = Scheme()\na = s.molecule("[OH-]", at=(0, 0), lone_pairs=True)\nb = s.molecule("CC(=O)OC", at=(2.5, 0))\ns.curly(a.atom(0), b.atom(1))\ns.curly(b.bond(1, 2), b.atom(2))\ns.arrow((4.2, 0), (5.4, 0), kind="equilibrium")\ns.draw()\n');
    const r = spawnSync(python, [PLOT_RENDERER, script, path.join(dir, 'out')], { encoding: 'utf8' });
    assert.equal(r.status, 0, r.stderr);
    assert.deepEqual(fs.readdirSync(path.join(dir, 'out')).sort(), ['0-dark.webp', '0-light.webp', 'meta.json']);
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
    const parsed = parsePageFile(fm);
    assert.deepEqual(parsed.errors, []);
    const { courses, textbooks } = parsed.value!.frontMatter;
    assert.deepEqual(sourceLines(courses, textbooks, 'zh'), [
      { label: '对应课程', value: '40160713 初等概率论；10420803 概率论与数理统计（概率论部分）' },
      { label: '参考书', value: '《概率论基础》，李贤平，第 3 版' },
    ]);
    assert.equal(sourceLines(undefined, textbooks, 'en')[0].value, '概率论基础, 李贤平, 3rd ed.');
    const translated = [{ title: '图论与代数结构', author: '崔勇、张小平', edition: 2, title_en: 'Graph Theory and Algebraic Structures', author_en: 'Yong Cui, Xiaoping Zhang' }];
    assert.equal(sourceLines(undefined, translated, 'en')[0].value, 'Graph Theory and Algebraic Structures, Yong Cui, Xiaoping Zhang, 2nd ed. (in Chinese)');
    const foreign = [{ title: 'Applied Multivariate Statistical Analysis', author: 'Richard A. Johnson, Dean W. Wichern', edition: 6, title_zh: '实用多元统计分析' }];
    assert.equal(sourceLines(undefined, foreign, 'zh')[0].value, '《实用多元统计分析》，Richard A. Johnson, Dean W. Wichern，第 6 版');
    assert.equal(sourceLines(undefined, foreign, 'en')[0].value, 'Applied Multivariate Statistical Analysis, Richard A. Johnson, Dean W. Wichern, 6th ed.');
    assert.equal(sourceLines([{ code: 1, name: '离散数学(2)', name_en: 'Discrete Mathematics (2)' }], undefined, 'en')[0].value, '1 Discrete Mathematics (2)');
    assert.equal(sourceLines([{ code: 2, name: '大学物理B1', note: '力学部分', note_en: 'mechanics part' }], undefined, 'en')[0].value, '2 大学物理B1 (mechanics part)');
    assert.equal(sourceLines(undefined, [{ title: 'Algebra', author: 'Artin' }], 'zh')[0].value, 'Algebra，Artin');
    assert.equal(serializePageFile(parsed.value!.frontMatter, '').includes('note: 概率论部分'), true);
    assert.match(parsePageFile('---\ntitle: x\ntextbooks:\n  - { title: A }\n---\n').errors[0], /"author" is required/);
    assert.match(parsePageFile('---\ntitle: x\ncourses: []\n---\n').errors[0], /"courses" must be a non-empty list/);
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
  /** Pages by id; a body starting with "en:" is an English-source page. */
  async function site(pages: Record<string, string>) {
    const sources = Object.fromEntries(Object.keys(pages).map((id) => [id, fakePage(id)]));
    const tree: ContentTree = { pages: new Map(Object.entries(sources)), rootIds: [] };
    const rendered = new Map<string, Awaited<ReturnType<typeof render>>['out']>();
    for (const [id, body] of Object.entries(pages)) {
      const lang: Lang = body.startsWith('en:') ? 'en' : 'zh';
      rendered.set(id, (await render(body.replace(/^en:/, ''), { page: sources[id], pages: Object.values(sources), lang })).out);
    }
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
  it('finds definitions on English-source pages and matches English names case-insensitively and in the plural', async () => {
    concepts.push({ id: 'group', zh: '群', en: 'group', aliases: [] });
    const s = await site({
      '1.3.2': 'en:## 2.2. Groups\n\n**Definition 2.2.1** A set with one operation is a **group** if…\n\nA *law of large numbers* says…',
      '1.3.3': '## 3.1. 环\n\n每个**群**都有单位元。',
      '1.3.4': 'en:## 4.1. Lattices\n\nAll **Groups** and the **law of large numbers**.',
    });
    concepts.pop();
    assert.deepEqual(s.diag.items, []);
    assert.equal(s.index.conceptSites.get('group')?.anchor, 'def-2.2.1');
    assert.equal(s.index.conceptSites.get('law-of-large-numbers')?.anchor, 'concept-law-of-large-numbers');
    assert.match(s.html('1.3.2'), /<dfn id="concept-law-of-large-numbers" class="wiki-dfn" data-concept="law-of-large-numbers"><em>law of large numbers<\/em><\/dfn>/);
    assert.match(s.html('1.3.3'), /1\.3\.2\/#def-2\.2\.1" class="concept-ref"/);
    assert.equal((s.html('1.3.4').match(/class="concept-ref"/g) ?? []).length, 2);
  });
  it('does not take an unnumbered statement label for a concept of the same name', async () => {
    concepts.push({ id: 'proposition', zh: '命题', en: 'proposition', aliases: [] });
    const s = await site({ '1.1.1': '## 1.1. A\n\n**定义 1.1.1（命题）** 设……', '1.1.2': '## 2.1. B\n\n**命题**：任意……\n\n每个**命题**都有真值。' });
    concepts.pop();
    assert.equal((s.html('1.1.2').match(/class="concept-ref"/g) ?? []).length, 1);
  });
  it('lets a named theorem define its concept, and a scoped homonym win inside its scope', async () => {
    concepts.push({ id: 'lagranges-theorem', zh: 'Lagrange 定理', en: "Lagrange's theorem", aliases: [] });
    concepts.push({ id: 'big-numbers-1-2', zh: '大数', en: 'big numbers', aliases: ['大数定律'], scope: ['1.2'] });
    const s = await site({ '1.1.1': '## 1.1. A\n\n**定理 1.1.1（Lagrange 定理）** 设……', '1.2.1': '## 1.1. B\n\n由 **Lagrange 定理** 与**大数定律**。' });
    concepts.splice(-2);
    assert.equal(s.index.conceptSites.get('lagranges-theorem')?.anchor, 'thm-1.1.1');
    assert.match(s.html('1.2.1'), /data-concept="big-numbers-1-2"/);
  });
  it('recognises a scoped concept only inside its scope', async () => {
    concepts.push({ id: 'characteristic-function', zh: '特征函数', en: 'characteristic function', aliases: [], scope: ['3'] });
    const s = await site({ '1.2.3': '## 3.1. A\n\n**特征函数**', '3.1.11': '## 11.1. B\n\n**特征函数**' });
    concepts.pop();
    assert.ok(!s.html('1.2.3').includes('concept-ref'));
    assert.match(s.html('3.1.11'), /data-concept="characteristic-function"/);
  });
  it('finds annotated definitions whatever the case or plural of the English name', async () => {
    concepts.push({ id: 'matrix', zh: '矩阵', en: 'matrix', aliases: [] });
    const s = await site({
      '2.1.1': 'en:## 1.1. A\n\nRectangular arrays are *Matrices*.',
      '3.1.13': '## 13.1. B\n\n依分布收敛（Convergence in Distribution）是……',
    });
    concepts.pop();
    assert.equal(s.index.conceptSites.get('matrix')?.anchor, 'concept-matrix');
    assert.equal(s.index.conceptSites.get('convergence-in-distribution')?.anchor, 'concept-convergence-in-distribution');
  });
  it('warns about an annotation with extra text inside the parentheses', async () => {
    const s = await site({ '3.1.12': '## 12.1. A\n\n大数定律（law of large numbers，LLN）描述均值。' });
    assert.equal(s.index.conceptSites.get('law-of-large-numbers'), undefined);
    assert.match(s.diag.items[0]?.message ?? '', /not recognized as the definition of "大数定律"/);
  });
  it('links a bold Latin alias on a Chinese page', async () => {
    concepts.push({ id: 'relu', zh: '线性整流单元', en: 'rectified linear unit', aliases: ['ReLU'] });
    const s = await site({ '4.7.2': '## 2.1. A\n\n**定义 2.1.1（线性整流单元）** 设……', '4.7.3': '## 3.1. B\n\n每层之后接 **ReLU**。' });
    concepts.pop();
    assert.match(s.html('4.7.3'), /data-concept="relu"/);
  });
  it('marks a Latin-named concept with italics on a Chinese page', async () => {
    concepts.push({ id: 'nosql', zh: 'NoSQL', en: 'NoSQL', aliases: [] });
    const s = await site({ '4.13.1': '## 1.1. A\n\n*NoSQL* 系统放弃了关系模型。', '4.13.2': '## 2.1. B\n\n与 **NoSQL** 相比……' });
    concepts.pop();
    assert.deepEqual(s.diag.items, []);
    assert.equal(s.index.conceptSites.get('nosql')?.pageId, '4.13.1');
    assert.match(s.html('4.13.2'), /data-concept="nosql"/);
  });
  it('keeps "+" apart in concept ids', () => {
    assert.notEqual(conceptId('B+ tree'), conceptId('B-tree'));
  });
  it('lets only the scoped homonym take an annotated definition inside its scope', async () => {
    concepts.push({ id: 'rank', zh: '秩', en: 'rank', aliases: [] });
    concepts.push({ id: 'rank-4-3', zh: '秩', en: 'rank', aliases: [], scope: ['4.3'] });
    const s = await site({ '2.1.3': '## 3.1. A\n\n秩（rank）是……', '4.3.2': '## 2.1. B\n\n元素的秩（rank）是……' });
    concepts.splice(-2);
    assert.deepEqual(s.diag.items, []);
    assert.equal(s.index.conceptSites.get('rank')?.pageId, '2.1.3');
    assert.equal(s.index.conceptSites.get('rank-4-3')?.pageId, '4.3.2');
  });
  it('allows restating a definition but not a second English annotation', async () => {
    const s = await site({
      '3.1.12': '## 12.1. A\n\n大数定律（law of large numbers）',
      '3.1.14': '## 14.1. B\n\n大数定律（law of large numbers）再述',
    });
    assert.match(s.diag.items[0].message, /already defined on page 3.1.12/);
  });
});
