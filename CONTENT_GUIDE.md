# 内容写作与双语约定

本文件是写作 `content/` 的唯一规范，人和智能体都按它执行。规则大多由 `pnpm wiki build` 自动检查：违反"错误"级规则会让构建失败，"警告"会让 `pnpm check` 失败。开发服务器（`pnpm dev`）会在页面顶部用红框显示当前页的问题。

## 1. 目录与编号

```
content/
  glossary.yaml                      术语表（见 §6）
  7.biology/                         页面目录：<编号>.<slug>
    index.zh.md                      中文（源语言，必需）
    index.en.md                      英文（必需，正文可以为空）
    assets/                          本页图片等静态文件（可选，扁平、ASCII 文件名）
    plots/                           本页绘图脚本 *.py（可选，见 §4）
    7.4.mathematical-modeling-in-biology/
      ...
```

- **编号是页面的身份**，也是 URL：`/zh/7.4.1.5/`、`/en/7.4.1.5/`。编号只能由正整数组成（`3.1.13`，不能写 `3.1.13a` 或 `01`）。
- 子页面编号 = 父编号 + `.n`；同级从 1 开始连续编号（不连续会警告）。
- slug 是小写英文 kebab-case（`central-limit-theorem`），只用于让目录可读，不出现在 URL 里。
- 新建页面用命令，不要手工建目录：
  ```bash
  pnpm wiki new 3.1 bayes-theorem "贝叶斯定理" "Bayes' Theorem"   # 追加为 3.1 的下一个子页
  pnpm wiki new root music "音乐" "Music"                          # 新的一级目录
  ```
- **编号一旦发布尽量不改**：改编号会改变 URL，并使所有 `/旧编号` 链接失效（构建会报错列出它们）。插入新内容优先追加到末尾；确需重排时，同时修复报错的链接。

## 2. 页面文件

每个 `index.<lang>.md` 以 front matter 开头，只允许以下字段：

```markdown
---
title: 中心极限定理
description: 可选。一句话摘要，用于搜索引擎和链接预览；缺省时取正文第一段。
---

正文……
```

英文文件额外允许 `source_hash`（由 `pnpm wiki stamp` 写入，不要手改，见 §5）。

## 3. 正文写法

| 内容 | 写法 | 说明 |
|---|---|---|
| 标题 | 从 `##` 开始 | 页面标题由 front matter 生成 H1，正文禁止 `#` |
| 固定锚点 | `## 条件期望 {#conditional-expectation}` | 可选。中英文用同一个 id，切换语言时可停在同一节 |
| 行内公式 | `$E(X)$` | 不支持 `\( \)` |
| 行间公式 | 独占几行的 `$$ … $$` | 不支持 `\[ \]` |
| 代码 | ```` ```python ```` | 写明语言以获得高亮；代码注释用英文 |
| 流程图 | ```` ```mermaid ```` | 文字随语言各写一份（见 §5） |
| 站内链接 | `[中心极限定理](/3.1.13)`、`[某节](/3.1.13#cond-exp)` | 只写编号；自动指向读者当前语言；目标不存在会报错 |
| 外部链接 | `[KaTeX](https://katex.org)` | 自动在新标签页打开 |
| 图片 | `![图注](./assets/name.png)` | 文件放 `assets/`；**图注必写**；单独成段时显示为带图注的图 |
| 绘图 | `![图注](./plots/name.py)` | 必须单独成段（前后空行），见 §4 |

不要使用：`python-plot` 代码块（旧语法）、`../` 相对链接、指向其他页面 `assets/` 的路径。

## 4. 绘图脚本（plots/）

- 一个 `.py` 文件 = 一张或多张图：脚本运行结束时**所有仍打开的 matplotlib figure** 都会被保存，按创建顺序显示。
- 渲染器会分别以浅色、深色主题运行脚本两次，固定随机种子 0，工作目录为脚本所在目录（可读取同目录的数据文件）。
- 禁止：`plt.show()`、`savefig()`、`matplotlib.use()`、全局 `style.use` / 字体设置、任何中文字符（包括注释）——**图片由中英文页面共用，图中文字一律英文**。
- 不要硬编码背景色；深色模式下显式的纯黑线条/文字会自动改为浅色。
- 结果按内容哈希缓存（`.cache/plots/`），只有脚本、同目录数据或渲染环境变化时才重新渲染。渲染超过 5 分钟会在日志中提示，请尽量调小参数。
- **冻结（freeze）**：渲染极慢的脚本可以冻结——`pnpm wiki freeze content/…/plots/name.py` 把图片写成 `name.frozen.json` 与 `name.frozen.<i>-<主题>.webp` 并随仓库提交，之后任何构建都不再运行该脚本。冻结后修改脚本会产生警告（`pnpm check` 失败），此时要么再次 `freeze`（会重新渲染），要么撤销修改；`pnpm wiki unfreeze …` 恢复正常渲染。目前冻结的：`7.4.2.4/plots/advection-competition-coexistence.py`（约 25 分钟）。
- 第一次使用前安装 Python 环境：`pnpm setup:python`（需要 uv）。

## 5. 双语约定

**中文是源语言，英文是翻译。** 两种语言共用同一棵目录树、同一套编号和同一批图片/绘图。

1. 每个页面都有 `index.en.md`。正文为空时，英文页显示中文原文并提示"尚未翻译"；导航中英文标题始终来自 `index.en.md` 的 `title`。
2. 翻译完成后执行 `pnpm wiki stamp <编号>`，把当前中文正文的哈希写入英文文件的 `source_hash`。
3. 之后若中文正文改动，该页状态变为 `stale`，英文页显示"原文已更新"提示。`pnpm wiki status` 列出所有 `untranslated` / `stale` 页面。
4. 图片（`assets/`）与绘图（`plots/`）两种语言共用：新增图片必须是英文或无文字。Mermaid 与表格是文本，随语言分别书写。
5. 代码块两种语言保持完全一致（因此代码注释用英文）。公式不翻译。
6. 需要跨语言保持的锚点，用 `{#english-id}` 显式指定。

### 翻译流程（给执行翻译的智能体）

1. `pnpm wiki status` 选择页面；读中文 `index.zh.md` 与 `content/glossary.yaml`。
2. 在 `index.en.md` 写译文：保留全部结构（标题层级、`{#id}`、公式、代码、图片与绘图引用、站内链接编号），图注与 Mermaid 文字译为英文；术语用术语表中的 `en`。
3. `pnpm wiki stamp <编号>`，再 `pnpm check`。

## 6. 术语标注

- `content/glossary.yaml` 收录需要中英对照的核心概念。
- 中文页面中，术语在**正文**（不含标题、代码、公式）中**第一次出现**时写成 `中心极限定理（Central Limit Theorem）`，之后不再重复。不在术语表中的重要概念也建议照此标注，并顺手加进术语表。
- 检查：`pnpm wiki terms`（全部）或 `pnpm wiki terms 3.1.13`（单页）。此检查不阻断构建。

## 7. 提交前

```bash
pnpm check     # 内容（严格模式）+ 类型检查 + lint + 单元测试
```
