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
import { sourceHash, translationStatus } from './build.ts';
import { Diagnostics } from './diagnostics.ts';
import { parsePageFile, serializePageFile } from './frontmatter.ts';
import { findUnannotatedTerms } from './glossary.ts';
import { type RenderContext, renderMarkdown } from './markdown.ts';
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
  const current = opts.page ?? fakePage('1');
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
    usedPlots: new Set(),
    usedAssets: new Set(),
  };
  const out = await renderMarkdown(body, ctx);
  return { out, diag, messages: diag.items.map((d) => `${d.level}:${d.line}:${d.message}`) };
}

describe('markdown rendering', () => {
  it('rewrites internal links into the reader language and checks targets', async () => {
    const { out, messages } = await render('[a](/2#x) and [b](/9)', { pages: [fakePage('2')] });
    assert.match(out.html, new RegExp(`href="${BASE_PATH}en/2/#x" data-internal`));
    assert.ok(messages.some((m) => m.includes('link to unknown page "9"')));
    assert.deepEqual(out.links.map((l) => [l.targetId, l.anchor]), [['2', 'x'], ['9', undefined]]);
  });

  it('assigns heading ids (custom {#id} wins) and builds the TOC from h2/h3', async () => {
    const { out } = await render('## 条件期望 $E(X)$ {#cond-exp}\n\n### Sub\n\n#### Deep');
    assert.deepEqual(out.headings, [
      { id: 'cond-exp', text: '条件期望 E(X)', depth: 2 },
      { id: 'sub', text: 'Sub', depth: 3 },
    ]);
    assert.match(out.html, /<h2 id="cond-exp">/);
    assert.ok(!out.html.includes('{#cond-exp}'));
  });

  it('rejects legacy syntax with file line numbers', async () => {
    const { messages } = await render('# Title\n\ntext \\(x\\)\n\n```python-plot\nx\n```');
    assert.ok(messages.some((m) => m.startsWith('error:4:do not use "# " headings')));
    assert.ok(messages.some((m) => m.startsWith('error:6:use $...$')));
    assert.ok(messages.some((m) => m.startsWith('error:8:inline ```python-plot')));
  });

  it('embeds plots as themed figures with source', async () => {
    const pg = fakePage('1', { plotFiles: ['growth.py'] });
    const plots: PlotResults = new Map([
      [path.join(pg.dir, 'plots/growth.py'), { key: 'abc', imageDir: '/tmp/abc', imagePrefix: '', frozen: false, figures: [{ width: 800, height: 600 }], source: 'import numpy' }],
    ]);
    const { out, diag } = await render('![增长曲线](./plots/growth.py)', { page: pg, plots });
    assert.equal(diag.errorCount, 0);
    assert.match(out.html, /<figure class="wiki-plot">/);
    assert.match(out.html, new RegExp(`src="${BASE_PATH}plots/abc/0-light.webp"[^>]*width="400" height="300"`));
    assert.match(out.html, /0-dark\.webp/);
    assert.match(out.html, /<figcaption>增长曲线<\/figcaption>/);
    assert.match(out.html, /<details class="wiki-plot-source">/);
    assert.ok(!out.html.includes('<p><figure'), 'figure must replace the paragraph');
  });

  it('resolves assets, wraps tables, reports bad images and KaTeX errors', async () => {
    const pg = fakePage('1', { assets: ['a.png'] });
    const { out, messages } = await render('![图](./assets/a.png)\n\n![](missing.png)\n\n| a |\n|---|\n| 1 |\n\n$\\frac{1}$', { page: pg });
    assert.match(out.html, new RegExp(`<figure class="wiki-figure"><img src="${BASE_PATH}media/1/a.png"`));
    assert.match(out.html, /<div class="table-wrap"><table>/);
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
    const { out } = await render('```mermaid\ngraph TD; A-->B;\n```\n\n```python\nprint(1)\n```');
    assert.match(out.html, /<div class="wiki-mermaid"><pre class="wiki-mermaid-source">graph TD; A-->B;/);
    assert.match(out.html, /<div class="code-block"><div class="code-block-header"><span class="code-lang">python<\/span><button type="button" class="copy-button" data-copy="">Copy<\/button>/);
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

describe('glossary', () => {
  const terms = [{ zh: '中心极限定理', en: 'central limit theorem' }];
  it('accepts an annotated first use and ignores headings/code', () => {
    assert.deepEqual(findUnannotatedTerms('## 中心极限定理\n\n`中心极限定理`\n\n中心极限定理（Central Limit Theorem）说明……再次提到中心极限定理。', terms), []);
  });
  it('reports an unannotated first use', () => {
    assert.equal(findUnannotatedTerms('由中心极限定理可知……', terms).length, 1);
  });
});
