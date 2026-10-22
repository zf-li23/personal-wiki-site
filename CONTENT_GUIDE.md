# 内容写作与双语约定

本文件是写作 `content/` 的唯一规范，人和智能体都按它执行。规则大多由 `pnpm wiki build` 自动检查：违反"错误"级规则会让构建失败，"警告"会让 `pnpm check` 失败。开发服务器（`pnpm dev`）会在页面顶部用红框显示当前页的问题。

## 1. 层级、目录与编号

知识库只有三级，像一套教材：

| 级别 | 例子 | 角色 | 内容 |
|---|---|---|---|
| 一级：学科大类 | `3` 统计学 | 上级页面 | 概括性文字，**不写任何标题** |
| 二级：课程（学科） | `3.1` 概率论 | 上级页面 | 概括性文字，**不写任何标题** |
| 三级：章节 | `3.1.13` 中心极限定理 | **页面** | 正文，按 §3 的编号规则写标题 |

本规范中"页面"默认指三级的章节页。一门课程的总结、导论之类也是章节（如 `3.1.16` 课程总结）。不允许第四级；更细的结构用页内标题表达。

```
content/
  glossary.yaml                      词条库（见 §6）
  3.statistics/                      目录：<编号>.<slug>
    index.zh.md                      中文（源语言，必需）
    index.en.md                      英文（必需，正文可以为空）
    3.1.probability/
      3.1.13.central-limit-theorem/
        index.zh.md  index.en.md
        assets/                      本页图片等静态文件（可选，扁平、ASCII 文件名）
        plots/                       本页绘图脚本 *.py（可选，见 §4）
```

- **编号是页面的身份**，也是 URL：`/zh/3.1.13/`、`/en/3.1.13/`。编号只能由正整数组成（`3.1.13`，不能写 `3.1.13a` 或 `01`）。
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

译文文件额外有 `source_hash`（由 `pnpm wiki stamp` 写入，不要手改；它同时标明哪个文件是译文，见 §5）。

**知识来源**（只写在源语言文件里，中英文页面都会在标题下方以统一格式显示，相当于版权声明）。一般写在课程页（二级），也可写在学科大类或章节页：

```yaml
---
title: 概率论
courses:                     # 对应课程：课程号 + 课程名，可多门；note 可选（note_en：英文页显示的备注）
  - { code: "40160713", name: 初等概率论 }
  - { code: "10420803", name: 概率论与数理统计, note: 概率论部分 }
  - { code: "20240023", name: 离散数学(2), name_en: Discrete Mathematics (2) }   # name_en：英文页显示的课程名
textbooks:                   # 参考书：原书的书名、作者、版次（版次可省略）
  - { title: 概率论基础, author: 李贤平, edition: 3 }
  - { title: 图论与代数结构, author: 崔勇、张小平, edition: 2,
      title_en: Graph Theory and Algebraic Structures, author_en: "Yong Cui, Xiaoping Zhang" }  # 英文页用，自动注明 (in Chinese)
---
```

中文页显示为"对应课程：40160713 初等概率论；10420803 概率论与数理统计（概率论部分）"和"参考书：《概率论基础》，李贤平，第 3 版"；英文页显示 `name_en`、`title_en`、`author_en`（缺省时显示原文），中文书后注明 (in Chinese)。英文原版书写原书名和作者（作者保持原文），可加 `title_zh` 作为中文页显示的译名，如 `{ title: Applied Multivariate Statistical Analysis, author: "Richard A. Johnson, Dean W. Wichern", edition: 6, title_zh: 实用多元统计分析 }`。没有对应课程或参考书就不写该字段；不要把这些信息写进正文。翻译时补上 `name_en`、`title_en`、`author_en`（作者用拼音，名在前、姓在后）。

## 3. 正文写法

| 内容 | 写法 | 说明 |
|---|---|---|
| 标题 | `## 13.1. 基本概念` | 见下方"标题编号" |
| 编号对象 | `**定理 13.2.1（中心极限定理）**` | 见 §3.1 |
| 行内公式 | `$E(X)$` | 不支持 `\( \)` |
| 行间公式 | 独占几行的 `$$ … $$` | 不支持 `\[ \]` |
| 代码 | ```` ```python ```` | 写明语言以获得高亮；代码注释用英文。统计学课程中课上的 R 代码写成 ```` ```r ```` 代码块，运行结果写成 ```` ```text ```` 或表格（构建不运行 R） |
| 多语言代码 | 相邻的 ```` ```cpp tab ````、```` ```python tab ```` 代码块 | 合成一个代码块，每种语言一个标签页；读者选一次语言，全站的标签页都跟着切换。用于同一段程序的不同语言实现（计算机课程的 C++ / Python），语言必须各不相同 |
| 流程图 | ```` ```mermaid ```` | 文字随语言各写一份（见 §5） |
| 化学结构 | ```` ```smiles ```` 代码块，每行一个 SMILES 或反应 SMILES（`A.B>>C`），可在空格后加标签 | 构建时由 RDKit 画成键线式（黑白、随主题变色、全站同一键长），同一块内的结构排成一行；标签两种语言共用，只写编号或式子（`1`、`(R)`）；化学式与反应式写 `$\ce{…}$`，反应机理用绘图脚本（§4） |
| 站内链接 | `[中心极限定理](/3.1.13)`、`[某节](/3.1.13#cond-exp)` | 只写编号；自动指向读者当前语言；目标不存在会报错 |
| 外部链接 | `[KaTeX](https://katex.org)` | 自动在新标签页打开 |
| 图片 | `![图注](./assets/name.png)` | 文件放 `assets/`；**图注必写**；单独成段时显示为带图注的图 |
| 绘图 | `![图注](./plots/name.py)` | 必须单独成段（前后空行），见 §4 |

不要使用：`python-plot` 代码块（旧语法）、`../` 相对链接、指向其他页面 `assets/` 的路径。

### 标题编号

章节页的标题从 `##` 开始（页面标题就是一级标题），编号**省略课程前缀**：页面 `3.1.13` 内的编号都以 `13` 开头。这样从课件转换来的 Markdown 不必改编号。

```markdown
## 13.1. 基本概念          ← 编号、尾点、一个空格、标题
### 13.1.1. 问题背景
### 13.1.2. 收敛模式
## 13.2. 基本定理
## 小结                    ← 不编号的标题只能是 ##（小结、习题、参考资料等）
```

检查规则（违反即构建错误）：标题层级不能跳级；`#` 的个数 = 编号段数（`##` 对应 `13.k`，`###` 对应 `13.k.m`）；同级连续编号；编号小节下的子标题也必须编号。编号标题的锚点与语言无关（`#sec-13.2.1`），中英文页面同一节锚点相同。上级页面（一级、二级）不允许出现任何标题。

格式问题（缺尾点、标题加粗等）用 `pnpm wiki fix [编号…]` 自动修正；它只改写格式，从不改动编号本身。粘贴课件转换的 Markdown 后先运行一次。

### 3.1 编号对象与引用

**定义、定理、引理、命题、推论、性质、例、注、算法、公式**（英文：Definition, Theorem, Lemma, Proposition, Corollary, Property, Example, Remark, Algorithm, Formula）写成段首粗体标签：

```markdown
**定义 13.1.1（依分布收敛）** 设 $Y_n, Y$ 的分布函数……
**定理 13.2.1（中心极限定理）** 设 $\{X_n\}$ 独立同分布……
**例 13.2.1** 掷硬币……
**定理**：不编号的标签也可以，只是不能被引用。
```

- 编号 = **所在二级标题的编号 + 该类型在本节内的序号**：13.2 节里依次是 定义 13.2.1、定理 13.2.1、定理 13.2.2。缺号允许（沿用教材编号时常见），同页重复、不属于所在小节都是错误。
- 名称写在全角括号里、放在粗体之内；`pnpm wiki fix` 会把 `**定理1.**`、`**推论1**（名称）` 等写法改成规范形式。
- 标签必须在段首；段落中间的粗体编号若不对应本页任何对象，会警告"另起一段"。
- 编号对象自动获得与语言无关的锚点（`#thm-13.2.1`、`#def-13.1.1`），并以色条区分类型；它后面紧跟的行间公式、列表、表格属于同一块，证明另起段落。行间公式下面**不空行**直接接着写的段落（"则称……""其中……"）也属于同一块，因此定义可以写成：

  ```markdown
  **定义 6.3.1** 设 $A$ 是 $n$ 阶方阵。若存在非零向量 $\boldsymbol{x}$ 使得

  $$
  A\boldsymbol{x} = \lambda\boldsymbol{x},
  $$
  则称 $\lambda$ 为 $A$ 的**特征值**。
  ```

  空一行再写的段落不属于该编号对象。
- 带编号的行间公式：`$$ … \tag{13.2} $$`，锚点 `#eq-13.2`。
- **引用**：正文直接写 `定理 13.2.1`、`定义 13.1.1`、`式 (13.2)`（英文 `Theorem 13.2.1`、`Eq. (13.2)`），构建会在**同一课程内**自动解析并链接（编号的第一段就是章，如 13 → `3.1.13`），鼠标悬停可预览内容。编号不跨课程沿用；跨课程引用请显式写链接 `[定理 13.2.1](/3.1.13#thm-13.2.1)`。引用了同一课程中不存在的编号会警告。

## 4. 绘图脚本（plots/）

- 一个 `.py` 文件 = 一张或多张图：脚本运行结束时**所有仍打开的 matplotlib figure** 都会被保存，按创建顺序显示。
- 渲染器会分别以浅色、深色主题运行脚本两次，固定随机种子 0，工作目录为脚本所在目录（可读取同目录的数据文件）。
- 禁止：`plt.show()`、`savefig()`、`matplotlib.use()`、全局 `style.use` / 字体设置、任何中文字符（包括注释）——**图片由中英文页面共用，图中文字一律英文**。
- 不要硬编码背景色；深色模式下显式的纯黑线条/文字会自动改为浅色。
- 结果按内容哈希缓存（`.cache/plots/`），只有脚本、同目录数据或渲染环境变化时才重新渲染。渲染超过 5 分钟会在日志中提示，请尽量调小参数。
- **冻结（freeze）**：渲染极慢的脚本可以冻结——`pnpm wiki freeze content/…/plots/name.py` 把图片写成 `name.frozen.json` 与 `name.frozen.<i>-<主题>.webp` 并随仓库提交，之后任何构建都不再运行该脚本。冻结后修改脚本会产生警告（`pnpm check` 失败），此时要么再次 `freeze`（会重新渲染），要么撤销修改；`pnpm wiki unfreeze …` 恢复正常渲染。目前冻结的：`7.4.5/plots/advection-competition-coexistence.py`（约 25 分钟）。
- **R 配套代码**（统计学课程）：图一律由 Python 脚本生成；展示统计分析的图（模拟、拟合、诊断图、数据可视化）可以在同一目录放一个同名的 `name.R`，写出同一分析与作图的 R 版本（base R 或 ggplot2，代码与注释英文）。构建不运行它，只在图下方的源码面板里与 Python 并列成两个标签页；它不影响绘图缓存。纯示意图（几何示意、概念图）不配 R 版本。`pnpm wiki check-r [编号…]` 在装有 R 时逐个运行这些文件检查能否跑通（本地检查，不在 CI 中）。
- **化学结构与反应机理**：绘图脚本可以 `from wikichem import Scheme`（`scripts/wiki/plot/wikichem.py`，RDKit 算坐标、matplotlib 画线）。`s.molecule(smiles, at=(x, y), lone_pairs=…)` 放置分子（坐标以键长为单位），`s.curly(起点, 终点, bend=…, single=…)` 画电子转移的弯箭头（`mol.atom(k)` 指原子，从朝向目标的孤对电子出发；`mol.bond(j, k)` 指键的中点；原子按 SMILES 顺序从 0 编号，或按原子映射号 `[CH3:1]`），`s.arrow(…, kind="forward"|"equilibrium"|"resonance"|"retro")` 画反应箭头，`s.text`、`s.plus` 写文字，最后 `s.draw()`。图中文字同样只用英文或式子。用法见模块开头的说明。
- 第一次使用前安装 Python 环境：`pnpm setup:python`（需要 uv）。

## 5. 双语约定

**每个页面先用一种语言写成（源语言），再翻译成另一种。** 资料是中文就先写中文，是英文就先写英文；翻译是写作流程的最后一步。两种语言共用同一棵目录树、同一套编号和同一批图片/绘图。

1. 每个页面都有 `index.zh.md` 和 `index.en.md`，未写的一方正文为空。只有一方有正文时，它就是源语言；另一种语言的页面显示原文并提示"尚未翻译"。导航标题始终来自各自文件的 `title`，所以两个文件都要写标题。
2. 翻译完成后执行 `pnpm wiki stamp <编号>`，把源语言正文的哈希写入译文文件的 `source_hash`。从此 `source_hash` 标明哪个文件是译文。若两个文件都已有正文、都还没有 `source_hash`，要写明源语言：`pnpm wiki stamp <编号> --from en`（在此之前，带 `courses` / `textbooks` 的文件被视为源语言）。
3. 之后若源语言正文改动，该页状态变为 `stale`，译文页显示"原文已更新"提示。`pnpm wiki status` 列出所有 `untranslated` / `stale` 页面（如 `zh→en  untranslated  1.1.1`）。修改内容时只改源语言文件，再更新译文并重新 stamp；不要只改译文。
4. 图片（`assets/`）与绘图（`plots/`）两种语言共用：新增图片必须是英文或无文字。Mermaid 与表格是文本，随语言分别书写。
5. 代码块两种语言保持完全一致（因此代码注释用英文）。公式不翻译。
6. 编号标题、编号对象和公式的锚点与语言无关，切换语言时停在同一处；不编号的标题如需固定锚点，可写 `## 小结 {#summary}`。

7. 中文页里重要的概念词在定义处带英文注释（§6）；英文页不写中文。

翻译的结构要求与质量标准见 AUTHORING.md §8。英文页面里出现汉字会产生警告（书名等专名请用 front matter 的来源字段）。

## 6. 概念（词条）

概念与编号对象不同：编号只在课程内有效，**概念跨课程通用**。`content/glossary.yaml` 是词条库，每条只写名称：

```yaml
terms:
  - { zh: 中心极限定理, en: central limit theorem }
  - { zh: 极大似然估计, en: maximum likelihood estimation, aliases: [最大似然估计] }
  - { zh: 特征函数, en: characteristic function, scope: ["3"] }   # 只在统计学中识别
```

**定义处**由构建从正文中找出，不写在词条库里：

1. 名称与概念相同的定义标签：`**定义 13.1.1（依分布收敛）**`；名称与概念相同的定理、引理、算法等标签（`**定理 2.6.3（Lagrange 定理）**`）在该概念别处没有定义时也算；
2. 定义块内加粗的概念名，即被定义的术语：`**定义 1.1.2** 称 $P \land Q$ 为 $P$ 与 $Q$ 的**合取**`（一个定义可以同时定义几个术语）；或
3. 不在定义块中时，标出定义处：中文写一次英文注释 `中心极限定理（Central Limit Theorem）`（英文写词条的 `en` 或其英文别名）；英文用斜体 `*central limit theorem*`（英文数学写作的惯例）。中文名就是拉丁字母名称的概念（NoSQL、Scrum），中文页面也用斜体标出，不写成"NoSQL（NoSQL）"。括号里只放英文名：简称、别名等写在括号外（`标准模板库（Standard Template Library），简称 STL`），否则不算定义处（概念因此没有定义处时构建会警告）。

定义处在源语言页面中确定；译文页对应的位置（定义块，或注释、斜体、第一处加粗）自动获得同一锚点。英文名不区分大小写，复数也能识别（`**groups**`、`**lattices**`）；冠词等其他词不能放进粗体（`**a group**` 不链接）。

**引用**由作者显式决定：**加粗、且加粗的文字恰好是某个概念名（或别名）**，就链接到它的定义处，例如 `**群**`、`**依分布收敛**`。普通文字从不自动匹配；`**分岔图**` 也不算提到"分岔"。**强调即链接**：正文需要说明、回顾或提醒读者某个概念时，就把它加粗——读者由此能悬停查看或跳转到定义；反过来，加粗本身就表示"这是一个值得查看定义的概念"。因此：

- **定义块内**：加粗被定义的术语（教材惯例）。值得独立查阅的术语应收入词条库，这样它就成为定义处；次要术语（如"前件"）可以不收，加粗只作标示。
- **定义块外**：加粗的只能是词条库中的概念名（或编号对象标签、`**证明**`）。提到前面章节或其他课程定义过的概念、且理解当前内容需要它时，加粗；同一概念在一段里只加粗第一次。
- 在定义块外第一次引入并解释一个概念时，要么把它写成编号的定义，要么用英文注释标出定义处，不要只加粗。
- 不为语气强调而加粗概念名以外的文字（小标题式的"**有限域的用途**"、整句结论等），改用句式、列表或不编号的 `##` 标题。

`pnpm wiki terms --bold [编号前缀…]` 列出不链接的粗体：定义块外的应当清零；定义块内的是尚未收入词条库的术语，供挑选。

- **英文注释只写在定义处**，全站一次；第二处注释是错误。后续章节用定义标签重述同一概念是允许的，定义处取阅读顺序中最早的一处。
- 加粗的概念名链接到定义处，悬停显示中英文名与定义内容；尚无定义处的概念只显示悬停卡片。定义所在页面内的加粗不再链接。页面底部列出"本页概念"和"引用本页的页面"，全站概念汇总在概念索引页（`/zh/concepts/`）。
- 同名异义：同一个词在不同学科里指不同概念时（概率论的"特征函数"与集合的特征函数，图论的"匹配"），给词条加 `scope: ["3"]`（页面编号前缀，可写学科或课程），它只在这些页面里被识别。中文名或英文名相同的两个词条，范围不能重叠；或者一个不加范围，此时在另一个的范围内以带范围的为准（格论的 complement 与集合的 complement）。
- 重要概念请加入词条库。`pnpm wiki terms` 列出尚无定义处的概念，以及"先使用、后定义"的情况（按阅读顺序，供调整章节顺序参考，不阻断构建）。

## 7. 符号约定

全站跨学科共用一套记号，以国际标准 **ISO 80000-2**（数学符号）、**ISO 80000-1**（物理量）和各领域通行教材为准：**字体表达语义**。同一个字母在不同学科表示不同对象时，尽量用不同字体区分（命题 $P$ 与概率 $\mathbb{P}$，边集 $E$ 与期望 $\mathbb{E}$）。确实无法避免的重名列在 §7.5。

构建会检查公式中可以机械识别的违例并警告（规则见 `scripts/wiki/notation.ts`），其中没有歧义的由 `pnpm wiki fix` 自动改写；字体的语义本身无法自动判断，写作和修缮时按下表逐条核对。

### 7.1 字体与含义

| 字体 | TeX | 用于 | 例子 |
|---|---|---|---|
| 斜体（默认） | `x` | 变量、函数名、物理量、命题与谓词 | $x, f, A, t, m, P(x)$ |
| 直立 | `\mathrm{}` | 数学常数、微分算子、单位、元素与粒子符号、单词构成的下标、分布名 | $\mathrm{e}, \mathrm{i}, \mathrm{d}x$；$\mathrm{mol}$；$x_{\max}$, $T_{\mathrm{c}}$；$\mathrm{Bin}(n,p)$ |
| 运算符 | `\operatorname{}` | 多字母运算与函数、典型群（`\det`、`\ker`、`\dim`、`\exp`、`\log` 等已有命令直接用） | $\operatorname{tr}, \operatorname{rank}, \operatorname{span}, \operatorname{diag}, \operatorname{sgn}, \operatorname{Re}, \operatorname{Var}, \operatorname{Cov}, \operatorname{MSE}$；$\operatorname{GL}_n, \operatorname{SO}(n), \operatorname{U}(n), \operatorname{Sp}(2m)$ |
| 粗斜体 | `\boldsymbol{}` | $\mathbb{F}^n$ 中的列向量（含零向量、向量值函数、参数向量）、随机向量、物理中的矢量、全 1 向量与示性函数 | $\boldsymbol{x}, \boldsymbol{0}, \boldsymbol{X}(t), \boldsymbol{\theta}, \boldsymbol{X}, \boldsymbol{F}, \boldsymbol{1}, \boldsymbol{1}_A$ |
| 黑板粗体 | `\mathbb{}` | 数集、一般数域、概率、期望 | $\mathbb{N}, \mathbb{Z}, \mathbb{Q}, \mathbb{R}, \mathbb{C}, \mathbb{F}$；$\mathbb{P}, \mathbb{E}$ |
| 花体 | `\mathcal{}` | 集族与 σ-代数、幂集、多重线性映射空间、线性映射与矩阵的像空间与零空间、正态分布 | $\mathcal{F}$, $\mathcal{P}(A)$, $\mathcal{L}(V,V;\mathbb{F})$, $\mathcal{R}(T), \mathcal{N}(A)$, $\mathcal{N}(\mu,\sigma^2)$ |
| 哥特体 | `\mathfrak{}` | 李代数、素理想与极大理想 | $\mathfrak{g}, \mathfrak{sl}_2, \mathfrak{p}, \mathfrak{m}$ |
| 无衬线 | `\mathsf{}` | 转置、共轭转置 | $A^{\mathsf T}, A^{\mathsf H}$ |
| 手写体 | `\mathscr{}` | 积分变换 | $\mathscr{L}\{f\}$, $\mathscr{F}\{f\}$ |

不要使用：`\vec`、`\mathbf`、`\bm`（向量一律 `\boldsymbol`；数集用 `\mathbb`）；`^T`、`^\top`、`'` 表示转置；`\Pr`；`\text{var}` 或裸写的 `var(`；公式里的 `...`；`\mathbb{1}`（KaTeX 不支持，示性函数写 $\boldsymbol{1}_A$）；`\emptyset`（写 `\varnothing`）；`\epsilon`（写 `\varepsilon`）；`\rightarrow`（写 `\to`）；`\stackrel`（写 `\overset`）；公式中的 Unicode 希腊字母（写 `\alpha`）；`C_n^k`（写 $\binom{n}{k}$）；取整 $[x]$（写 $\lfloor x\rfloor$）；集合差 $A - B$（写 $A \setminus B$）；`||x||`（写 $\|x\|$）。

排版细节：
- 省略号：逗号分隔的列表用 `\dots`（$a_1, \dots, a_n$），运算符之间用 `\cdots`（$a_1 + \cdots + a_n$）。
- 上横线：单个字母用 `\bar`（$\bar z$），较长的表达式用 `\overline`（$\overline{z_1 z_2}$）；重音作用于命令时加花括号：`\bar{\boldsymbol{y}}`（`\bar\boldsymbol{y}` 会出错）。
- 运算符的括号：$\operatorname{rank}(A)$、$\operatorname{tr}(A)$、$\operatorname{Var}(X)$ 带括号；$\det A$、$\dim V$、$\ker T$ 不带。
- 映射写 `f\colon A \to B`（不是 `f: A \to B`）。
- 单词或缩写构成的下标、标签直立：$e_{\mathrm{L}}$、$C_{3\mathrm{v}}$、$\rho_{\mathrm{in}}$、$\mathrm{SS}_A$、$\mathrm{BF}_{10}$；作为函数的统计量用 `\operatorname`：$\operatorname{MSE}(\hat\theta)$、$\operatorname{Bias}$。
- 特殊函数：$\Gamma(x)$、Beta 函数 $\mathrm{B}(\alpha,\beta)$。
- 表格单元格中的绝对值、范数写 `\lvert x \rvert`、`\Vert x \Vert`：裸的 `|` 会被当作列分隔符。
- 同一课程内矩阵统一用一种括号（线性代数用 `bmatrix`）。

### 7.2 数学

- **常数与算子**：自然常数 $\mathrm{e}$、虚数单位 $\mathrm{i}$、微分 $\mathrm{d}$ 直立（$\mathrm{e}^{\mathrm{i}\theta}$，$\int f(x)\,\mathrm{d}x$，$\frac{\mathrm{d}y}{\mathrm{d}x}$）；作下标、求和指标的 $i$ 与群的单位元 $e$ 是变量，用斜体。$\pi$ 照常写 `\pi`。
- **数集**：$\mathbb{N} = \{0, 1, 2, \dots\}$ 包含 0（ISO 80000-2），正整数写 $\mathbb{N}_+$；一般数域写 $\mathbb{F}$（不用中文教材常用的 $P$，以免与概率混淆）。
- **线性代数**：矩阵用斜体大写 $A$（不加粗），零矩阵 $O$，单位矩阵 $I_n$；$\mathbb{F}^n$ 中的向量用粗斜体 $\boldsymbol{x}$，零向量 $\boldsymbol{0}$，标准基 $\boldsymbol{e}_i$；矩阵 $A$ 对应的线性映射写 $T_A\colon \boldsymbol{x} \mapsto A\boldsymbol{x}$（不用粗体 $\boldsymbol{A}$ 表示映射）。抽象线性空间用斜体大写 $V, W$，其元素用普通斜体 $v, w$，零元 $0$（必要时 $0_V$），恒等映射 $\mathrm{id}_V$；坐标向量是粗体（$[v]_B$ 或课程中约定的 $\hat{\boldsymbol{x}}$）——粗体与否本身提示"具体还是抽象"。矩阵空间 $\mathbb{F}^{m\times n}$，线性映射空间 $\operatorname{Hom}(V,W)$，像与零空间 $\mathcal{R}(T)$、$\mathcal{N}(T)$（抽象代数中的同态核仍写 $\ker\varphi$、$\operatorname{Im}\varphi$）。转置 $A^{\mathsf T}$，共轭转置 $A^{\mathsf H}$，伴随变换 $T^*$，对偶映射 $T^{\mathsf t}$；内积 $\langle x, y\rangle$，范数 $\|x\|$，Frobenius 范数 $\|A\|_{\mathrm{F}}$；复共轭 $\bar z$。
- **分析**：$\lim$、$\sup$、$\inf$ 用已有命令；邻域 $N(x_0,\delta)$、去心邻域 $N^*(x_0,\delta)$；Riemann 可积函数类 $\mathcal{R}[a,b]$（不写易与 $\mathbb{R}$ 混淆的 $R[a,b]$），$C[a,b]$、$C^n(I)$；凸函数（convex，中文教材的"下凸"）与凹函数（concave，"上凸"）。$\mathbb{R}^n$ 中的点在分析、微分方程中写普通斜体 $x$、$P$、$M_0$（分析学惯例）；方向向量、法向量 $\boldsymbol{n}$、切向量、向量值函数 $\boldsymbol{r}(t)$、向量场 $\boldsymbol{F}$、坐标单位向量 $\boldsymbol{i},\boldsymbol{j},\boldsymbol{k}$ 加粗。偏导数 $f_x$、$\frac{\partial f}{\partial x}$；Jacobi 矩阵 $J_f$ 或 $\frac{\partial(y_1,\dots,y_m)}{\partial(x_1,\dots,x_n)}$，Hesse 矩阵 $H_f$。场论 $\operatorname{grad} f=\nabla f$、$\operatorname{div}\boldsymbol{v}=\nabla\cdot\boldsymbol{v}$、$\operatorname{rot}\boldsymbol{v}=\nabla\times\boldsymbol{v}$（英文写 curl）、Laplace 算子 $\Delta$；微分元 $\mathrm{d}\sigma$、$\mathrm{d}S$、$\mathrm{d}V$、$\mathrm{d}l$、$\mathrm{d}\boldsymbol{S}$，第二型曲面积分 $\mathrm{d}y\wedge\mathrm{d}z$。微分算子 $\mathrm{D}=\frac{\mathrm{d}}{\mathrm{d}x}$（直立），Wronski 行列式 $W(t)$，基解矩阵 $\Phi(t)$。
- **复分析**：$z = x + \mathrm{i}y$，$\operatorname{Re} z$、$\operatorname{Im} z$、$\lvert z\rvert$、共轭 $\bar z$；按英文文献的惯例，$\arg z$ 是多值的辐角、$\operatorname{Arg} z \in (-\pi, \pi]$ 是主值，$\log z$ 多值、$\operatorname{Log} z$ 是主支（中文教材常写作 $\operatorname{Ln}$ / $\ln$，正文中说明一次）；扩充复平面 $\hat{\mathbb{C}} = \mathbb{C} \cup \{\infty\}$（不写易与闭包混淆的 $\overline{\mathbb{C}}$）；圆盘 $D(z_0, r) = \{\lvert z - z_0\rvert < r\}$，单位圆盘 $\mathbb{D}$；留数 $\operatorname{Res}(f, z_0)$；Wirtinger 导数 $\frac{\partial f}{\partial z}$、$\frac{\partial f}{\partial \bar z}$；围道积分 $\oint_\gamma f(z)\,\mathrm{d}z$。
- **偏微分方程**：偏导数下标 $u_t$、$u_{xx}$；区域 $\Omega$，边界 $\partial\Omega$，外法向 $\boldsymbol{n}$，法向导数 $\frac{\partial u}{\partial \boldsymbol{n}}$；Laplace 算子 $\Delta$；Fourier 变换 $\hat f(\xi) = \mathscr{F}\{f\}(\xi) = \int_{\mathbb{R}} f(x)\,\mathrm{e}^{-\mathrm{i}\xi x}\,\mathrm{d}x$，逆变换带因子 $\frac{1}{2\pi}$；卷积 $f * g$；Green 函数 $G(x, y)$。
- **集合与映射**：$f\colon A \to B$；空集 $\varnothing$；补集 $A^{\mathsf c}$，差 $A \setminus B$，幂集 $\mathcal{P}(A)$；集合论中集合的特征函数可写 $\chi_A$；格与布尔代数中的补元写 $a'$。
- **逻辑**：命题变元用斜体小写 $p, q, r$，公式用斜体大写 $A, B$，谓词与公理模式中的 $P, Q, R$ 斜体；联结词 $\lnot, \land, \lor, \to, \leftrightarrow$。
- **代数结构**：群的单位元 $e$（斜体，是变量）；抽象代数中的一般域写 $F$（教材通行写法），作为线性代数标量域时写 $\mathbb{F}$；有限域 $\mathbb{F}_q$；李代数 $\mathfrak{g}$；典型群 $\operatorname{GL}_n(\mathbb{F})$、$\operatorname{SO}(n)$、$\operatorname{U}(n)$。

### 7.3 概率与统计

- 概率 $\mathbb{P}(A)$，期望 $\mathbb{E}[X]$（或 $\mathbb{E}X$），方差 $\operatorname{Var}(X)$，协方差 $\operatorname{Cov}(X, Y)$，相关系数 $\operatorname{Corr}(X,Y)$，示性函数 $\boldsymbol{1}_A$。
- 随机变量用斜体大写 $X$，观测值用小写 $x$；随机向量 $\boldsymbol{X}$，观测向量 $\boldsymbol{x}$；参数用希腊字母 $\theta, \mu, \sigma$，估计量加帽 $\hat\theta$，样本均值 $\bar X$。
- 参数向量加粗（$\boldsymbol{\theta}$、$\boldsymbol{\beta}$）；参数下的概率与期望 $\mathbb{P}_\theta$、$\mathbb{E}_\theta$，原假设下 $\mathbb{P}_{H_0}$、$\overset{H_0}{\sim}$。
- 分布（直立缩写，参数按下列约定）：

  | 分布 | 记号 | 约定 |
  |---|---|---|
  | 两点（Bernoulli） | $\mathrm{Ber}(p)$ | |
  | 二项 | $\mathrm{Bin}(n,p)$ | |
  | 几何 | $\mathrm{Geo}(p)$ | 取值 $1, 2, \dots$（首次成功所需次数） |
  | 负二项 | $\mathrm{NB}(r,p)$ | 第 $r$ 次成功前的失败次数，取值从 0 开始 |
  | Pascal | $\mathrm{Pascal}(r,p)$ | 第 $r$ 次成功所需次数，$= r + \mathrm{NB}(r,p)$ |
  | 超几何 / 负超几何 | $\mathrm{H}(n,M,N)$ / $\mathrm{NH}(r,M,N)$ | |
  | Poisson | $\mathrm{Poi}(\lambda)$ | |
  | 多项 | $\mathrm{Mult}(n,\boldsymbol{p})$ | |
  | 均匀 | $\mathrm{U}(a,b)$ | 不写 $\mathrm{U}[a,b]$ |
  | 指数 | $\mathrm{Exp}(\lambda)$ | $\lambda$ 是速率（均值 $1/\lambda$） |
  | Gamma | $\Gamma(\alpha,\lambda)$ | $\lambda$ 是速率 |
  | Beta | $\mathrm{Beta}(\alpha,\beta)$ | |
  | 正态 | $\mathcal{N}(\mu,\sigma^2)$，多元 $\mathcal{N}_p(\boldsymbol{\mu},\Sigma)$ | 第二个参数是方差 |
  | Cauchy | $\mathrm{Cauchy}(\theta)$ | 标准 Cauchy 即 $t_1$ |
  | $\chi^2$、$t$、$F$ | $\chi^2_n$、$t_n$、$F_{m,n}$ | 上 $\alpha$ 分位数 $z_\alpha$、$t_{n,\alpha}$、$\chi^2_{n,\alpha}$、$F_{m,n,\alpha}$ |

  独立同分布 $\overset{\text{iid}}{\sim}$，近似服从 $\overset{\cdot}{\sim}$ 或 $\overset{H_0}{\approx}$。
- 收敛：$\xrightarrow{d}$（依分布）、$\xrightarrow{p}$（依概率）、$\xrightarrow{\text{a.s.}}$（几乎必然）。

### 7.4 物理、化学与生物

物理与化学共用一套量、单位与符号，依据 SI（《国际单位制》第 9 版，2019 年起以固定常数定义）、**ISO 80000**（各部分的量与单位）和 IUPAC《物理化学中的量、单位和符号》（绿皮书）。物理课程先写成，化学课程沿用；资料（包括教材）的记号与下表不同时一律改写，必要时在第一次出现处用一句话说明教材的写法。

**写法**

- 物理量斜体（$m, t, E$），矢量粗斜体（$\boldsymbol{F}, \boldsymbol{v}$），其大小写普通斜体（$v = \lvert\boldsymbol{v}\rvert$）；单位矢量写 $\boldsymbol{e}_x$、$\boldsymbol{e}_r$、$\boldsymbol{e}_{\mathrm{t}}$、$\boldsymbol{e}_{\mathrm{n}}$（帽子只留给算符）；时间导数可写 $\dot{x}$、$\ddot{\boldsymbol{r}}$。
- 单位直立，与数值之间留细空格，乘积用细空格、除法用负指数：$9.8\,\mathrm{m\,s^{-2}}$、$8.314\,\mathrm{J\,mol^{-1}\,K^{-1}}$；百分号和角度符号紧跟数值（$30^\circ$）。表头与坐标轴写"量/单位"：$T/\mathrm{K}$、$p/\mathrm{kPa}$。只用 SI 及其认可的单位（$\mathrm{eV}$、$\mathrm{L}$、$\mathrm{min}$、$\mathrm{h}$、$\mathrm{d}$、$^\circ$、$\mathrm{u}$ 即 $\mathrm{Da}$）；atm、mmHg、cal、Å、Gs 等只在说明历史或资料时出现并给出换算。电磁学一律用 SI（不用 Gauss 制）。
- **量纲**按 ISO 80000-1 用无衬线正体：$\dim F = \mathsf{L}\,\mathsf{M}\,\mathsf{T}^{-2}$，七个基本量纲 $\mathsf{L}, \mathsf{M}, \mathsf{T}, \mathsf{I}, \Theta, \mathsf{N}, \mathsf{J}$，量纲一的量 $\dim Q = 1$。
- 常数斜体：$c, h, \hbar, e, k_{\mathrm{B}}, N_{\mathrm{A}}, R = N_{\mathrm{A}}k_{\mathrm{B}}, \varepsilon_0, \mu_0, G, m_{\mathrm{e}}, m_{\mathrm{p}}$；SI 定义常数（$c, h, e, k_{\mathrm{B}}, N_{\mathrm{A}}$ 等）是精确值，写数值时说明这一点。粒子与核素符号直立（$\mathrm{e}^-$、$\mathrm{p}$、$\mathrm{n}$、$^{133}\mathrm{Cs}$），光子在正文中直接写"光子"。
- 微分：全微分 $\mathrm{d}U$，过程量的无穷小写 $\delta Q$、$\delta W$；偏导数注明保持不变的量 $\left(\frac{\partial U}{\partial T}\right)_V$。平均值在物理中写 $\bar v$ 或 $\langle v\rangle$（统计物理与量子力学），概率论语境仍写 $\mathbb{E}$。
- 复共轭与厄米共轭按物理惯例写 $z^*$、$A^\dagger$；算符加帽 $\hat{H}$、$\hat{p}_x$。

**量的符号**（同一符号在不同学科的另一含义见 §7.5）

| 领域 | 符号 |
|---|---|
| 力学 | 位矢 $\boldsymbol{r}$，位移 $\Delta\boldsymbol{r}$，路程 $s$，速度 $\boldsymbol{v}$，加速度 $\boldsymbol{a}$，质量 $m$，密度 $\rho$，力 $\boldsymbol{F}$，动量 $\boldsymbol{p}$，冲量 $\boldsymbol{I}$，功 $W$，功率 $P$，动能 $E_{\mathrm{k}}$，势能 $E_{\mathrm{p}}$，机械能 $E$；角位置 $\theta$，角速度 $\boldsymbol{\omega}$，角加速度 $\boldsymbol{\alpha}$，力矩 $\boldsymbol{M}$，角动量 $\boldsymbol{L}$，转动惯量 $J$；劲度系数 $k$，周期 $T$，频率 $\nu$，角频率 $\omega$，约化质量 $\mu$，压强 $p$ |
| 振动与波 | 振幅 $A$，相位 $\varphi$（初相 $\varphi_0$），波长 $\lambda$，角波数 $k = 2\pi/\lambda$，波矢 $\boldsymbol{k}$，波数 $\tilde\nu = 1/\lambda$（光谱学），相速度 $u$，群速度 $v_{\mathrm{g}}$，强度 $I$，声强级 $L_I$（单位 $\mathrm{dB}$），品质因数 $Q$ |
| 相对论 | $\beta = v/c$，$\gamma = 1/\sqrt{1-\beta^2}$；质量 $m$ 只指不变质量，$\boldsymbol{p} = \gamma m\boldsymbol{v}$，$E = \gamma mc^2$，静能 $E_0 = mc^2$，$E^2 = p^2c^2 + m^2c^4$（不用"运动质量"，教材的 $m(v)$ 在注中说明） |
| 热学 | 热力学温度 $T$（$\mathrm{K}$），摄氏温度 $t$（$^\circ\mathrm{C}$），压强 $p$，体积 $V$，物质的量 $n$，分子数 $N$，数密度 $n_V$ 或 $n$（不与物质的量同时出现），摩尔质量 $M$，分子质量 $m$，摩尔体积 $V_{\mathrm{m}}$；热量 $Q$、功 $W$，**均以系统得到为正**：第一定律写 $\Delta U = Q + W$，体积功 $W = -\int p\,\mathrm{d}V$（系统对外做功为 $-W$，与 IUPAC、化学一致；物理教材的 $Q = \Delta U + W'$ 在 5.2 中说明一次）；热容 $C$，摩尔热容 $C_{p,\mathrm{m}}$、$C_{V,\mathrm{m}}$，比热容 $c$，$\gamma = C_p/C_V$；内能 $U$，焓 $H$，熵 $S$，Helmholtz 自由能 $A$，Gibbs 自由能 $G$，化学势 $\mu$；微观态数 $\Omega$（$S = k_{\mathrm{B}}\ln\Omega$），分布函数 $f(v)$，最概然速率 $v_{\mathrm{p}}$，平均速率 $\bar v$，方均根速率 $v_{\mathrm{rms}}$，平均自由程 $\bar\lambda$，效率 $\eta$，制冷系数 $\varepsilon$；标准态 $p^\circ = 10^5\,\mathrm{Pa}$，标准量加 $^\circ$（$\Delta_{\mathrm{r}}H^\circ$） |
| 电磁学 | 电荷 $q$、$Q$，电荷密度 $\rho$、$\sigma$、$\lambda$（体、面、线），电场强度 $\boldsymbol{E}$，电位移 $\boldsymbol{D} = \varepsilon_0\boldsymbol{E} + \boldsymbol{P}$，极化强度 $\boldsymbol{P}$，电势 $\varphi$，电压 $U$，电动势 $\mathcal{E}$，电通量 $\Phi_{\mathrm{e}}$，电偶极矩 $\boldsymbol{p}$，电容 $C$，电流 $I$，电流密度 $\boldsymbol{J}$，电阻 $R$，电阻率 $\rho$，电导率 $\sigma$；磁感应强度 $\boldsymbol{B}$，磁场强度 $\boldsymbol{H} = \boldsymbol{B}/\mu_0 - \boldsymbol{M}$，磁化强度 $\boldsymbol{M}$，磁通量 $\Phi$，磁矩 $\boldsymbol{m}$，自感 $L$，互感 $M$；相对电容率 $\varepsilon_{\mathrm{r}}$，相对磁导率 $\mu_{\mathrm{r}}$，电极化率 $\chi_{\mathrm{e}}$，磁化率 $\chi_{\mathrm{m}}$；能量密度 $w$，Poynting 矢量 $\boldsymbol{S}$ |
| 光学 | 折射率 $n$，光程差 $\Delta$，相位差 $\Delta\varphi$，光强 $I$，波长 $\lambda$（真空中 $\lambda_0$），频率 $\nu$，焦距 $f$，光栅常数 $d$ |
| 量子 | 波函数 $\Psi(\boldsymbol{r}, t)$，定态波函数 $\psi(\boldsymbol{r})$，算符 $\hat{x}, \hat{p}, \hat{H}$，期望值 $\langle \hat{A}\rangle$；能级 $E_n$，量子数 $n, l, m_l, s, m_s, j, m_j$（与化学的原子结构相同），轨道与壳层直立（$1\mathrm{s}$、$2\mathrm{p}$、$\mathrm{K}$ 壳层），光谱项 $^{2S+1}L_J$ 中的 $L$ 写直立字母（$^2\mathrm{P}_{3/2}$）；Bohr 半径 $a_0$，Rydberg 常量 $R_\infty$，Bohr 磁子 $\mu_{\mathrm{B}}$，功函数 $W_0$，Fermi 能 $E_{\mathrm{F}}$，禁带宽度 $E_{\mathrm{g}}$；分子光谱按 IUPAC：转动量子数 $J$、振动量子数 $v$、转动惯量 $I$、转动常量 $\tilde B$（波数），与化学一致 |

- **化学**：化学式与反应式写在 `\ce{}` 中（$\ce{H2O}$、$\ce{2H2 + O2 -> 2H2O}$），元素与电子 $\ce{e-}$ 自动直立；浓度 $[\ce{A}]$ 或 $c_{\mathrm{A}}$。热力学与量子的量沿用上表。
- **生物**（正文，不是公式）：基因名斜体（*lacZ*），蛋白质名正体（LacZ）；物种学名斜体（*Escherichia coli*）。

### 7.5 已知的重名

| 记号 | 含义 | 靠什么区分 |
|---|---|---|
| $e$ / $\mathrm{e}$ / $e$ | 群的单位元 / 自然常数 / 元电荷 | 字体与学科 |
| $\mathcal{N}(A)$ / $\mathcal{N}(\mu,\sigma^2)$ | 零空间 / 正态分布 | 参数 |
| $\bar z$ / $\bar X$ | 复共轭 / 样本均值 | 对象 |
| $V$ | 线性空间 / 图的顶点集 | 学科 |
| $\mathcal{L}$ | 多重线性映射空间 / 物理中的拉格朗日量 | 学科 |
| $P$ | 置换矩阵 / 可逆矩阵（相似变换 $P^{-1}AP$） | 语境；需要时写 $P_\sigma$ |
| $\sigma$ | 坐标同构（2.1.8）/ 矩阵的谱 $\sigma(A)$ / 标准差 | 学科与参数 |
| $F$ / $\mathbb{F}$ | 名为 $F$ 的矩阵、抽象代数中的域 / 线性代数的标量域 | 字体 |
| $\mathcal{E}$ | 集族 / 电动势 | 学科 |
| $T$ | 周期 / 热力学温度 / 动能（不用，写 $E_{\mathrm{k}}$） | 章节；同时出现时周期写 $\tau$ 并说明 |
| $M$、$\boldsymbol{M}$ | 摩尔质量、互感 / 力矩、磁化强度 | 学科；标量与矢量 |
| $\boldsymbol{p}$ / $p$ | 动量、电偶极矩 / 压强 | 学科；矢量与标量 |
| $\rho$、$\sigma$ | 质量密度、电荷密度、电阻率 / 面电荷密度、电导率、Stefan–Boltzmann 常量 | 章节，同一章内不混用 |
| $R$ | 摩尔气体常量 / 电阻 | 学科 |
| $\mu$ | 约化质量、化学势、磁导率 $\mu_0, \mu_{\mathrm{r}}$ / 期望 | 下标与学科 |
| $\boldsymbol{S}$ / $S$ | Poynting 矢量 / 熵 | 矢量与标量 |
| $J$ / $I$ | 力学中的转动惯量 $J$ / 分子光谱与化学中的转动量子数 $J$（此时转动惯量写 $I$） | 学科；分子光谱一节开头说明一次 |
| $\dim$ | 量纲 $\dim F$ / 线性空间的维数 $\dim V$ | 学科 |

## 8. 提交前

```bash
pnpm check     # 内容（严格模式）+ 类型检查 + lint + 单元测试
```
