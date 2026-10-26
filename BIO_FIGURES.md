# 生物学插图规范

生物学模块像一本教材：插图和正文同等重要。本文件规定生物学（7.x，以及化学生物学 6.6 等用到生物元素的页面）插图的**视觉语言、绘图工具、图标来源与许可、写作流程**。它是 CONTENT_GUIDE §4（绘图脚本）的补充；两者冲突时以 CONTENT_GUIDE 为准。

所有生物插图都是 `plots/*.py` 绘图脚本，用 `import wikibio as bio`（`scripts/wiki/plot/wikibio/`）绘制，和其他绘图一样由构建渲染浅色、深色两版并缓存。**不截图、不搬运其他教材的图**。

## 1. 总体风格

- **柔和、扁平、有轮廓**（接近 BioRender）：每个对象一个柔和的填充色，配同色相、更深的轮廓线；少量高光；不用渐变、阴影和立体透视（结构示意除外）。
- **两种主题都要好看**：对象的填充色在深色背景上同样清楚；区室（细胞质、核质、液泡）的浅底在深色主题中自动变成同色相的暗色调。**颜色只通过调色板标记取用**（§2），不在脚本里写死颜色；这样两种主题、全站风格一致。
- **信息优先**：一张图讲一件事；元素按重要程度分级（主角饱满、配角淡化、背景最淡）；不画与论点无关的装饰。
- **图中文字一律英文**（图片由中英文页面共用）；图注（Markdown 中的 `![图注]`）用页面语言写清每一步。基因名斜体（`italic=True`）、蛋白质正体；物种学名斜体。

## 2. 颜色（调色板标记）

`bio.P.fill(token)`、`bio.P.edge(token)`、`bio.P.light(token)` 取用；`bio.P.ink()` 是文字与线条色，`bio.P.muted()` 是次要文字与引线，`bio.P.on_fill()` 是画在填充色上的文字（两种主题都是深色）。全部标记见 `palette.py` 的 `TOKENS`，主要的：

| 类别 | 标记 | 用于 |
|---|---|---|
| 核酸 | `dna`、`dna2`（互补链）、`rna`/`mrna`、`trna`、`rrna` | DNA 蓝，RNA 橙 |
| 膜 | `lipid_head`、`lipid_tail`、`membrane`、`cell_wall` | 磷脂头部橙、尾部米色；细胞壁绿 |
| 大分子 | `protein`、`enzyme`、`receptor`、`channel`、`antibody`、`carbohydrate`、`lipid`、`metabolite`、`atp`、`drug` | 无名的多个蛋白依次用 `bio.P.protein(i)` |
| 离子 | `ca`、`na`、`k`、`cl`、`h`、`mg` | `bio.ion()` |
| 区室与细胞器 | `cytoplasm`、`extracellular`、`nucleus`、`nucleolus`、`chromatin`、`mitochondrion`、`matrix`、`er`、`golgi`、`lysosome`、`peroxisome`、`vesicle`、`chloroplast`、`thylakoid`、`vacuole` | |
| 生物与组织 | `bacterium`、`virus`、`blood`、`plant`、`animal`、`neuron`、`muscle`、`bone` | 剪影着色 |
| 语义 | `positive`（激活、获得、野生型）、`negative`（抑制、缺失、突变）、`highlight`、`neutral` | 对比、强调 |

固定的配色方案：核苷酸 A 绿、C 蓝、G 橙、T/U 红（`P.NUCLEOTIDE`，与序列 logo 惯例一致）；氨基酸按性质分四类（`P.AMINO_ACID_CLASS`）；原子沿用化学课程的 CPK 色（wikichem）。

**同一对象全站同色**：DNA 永远是蓝色，线粒体永远是橙红色。新增对象时先在 `TOKENS` 加标记（两种主题都检查），再使用。

## 3. 图形语法

### 3.1 箭头（SBGN 语义）

| `kind` | 箭头 | 含义 |
|---|---|---|
| `process` | 实心三角 | 转化、运输、反应的一步 |
| `activation` | 空心箭头 | 促进、激活（正调控） |
| `inhibition` | 横杠 ⊣ | 抑制（负调控） |
| `catalysis` | 空心圆 | 催化 |
| `necessary` | 横杠加空心箭头 | 必需的促进 |
| `modulation` | 空心菱形 | 调节、作用方向未知 |
| `link` | 无头 | 结合、关联、引线 |

虚线（`dashed=True`）表示间接作用或推测的作用；空心箭头画在有底色的区室上时传 `bg=bio.P.fill(区室)`；`bend` 画弧形箭头。代谢图中的辅底物用 `bio.reaction(ax, a, b, side=("ATP", "ADP"))`：一条弧，前一个进入、后一个离开。

### 3.2 采用的国际标准

| 图的类型 | 标准 | wikibio |
|---|---|---|
| 信号通路、调控网络、代谢通路 | SBGN（Systems Biology Graphical Notation）：活性流（AF）与过程描述（PD） | `network` 模块 |
| 遗传构建、质粒、合成生物学线路 | SBOL Visual 3（启动子、RBS、编码区、终止子、操纵子等图元） | `genetics.construct`、`genetics.plasmid` |
| 系谱图 | NSGC 标准系谱符号（Bennett 等 2008，2022 修订） | `genetics.pedigree` |
| 系统发育树 | 根在左或下，枝长按比例时加标尺；类群用 PhyloPic 剪影 | `phylo.tree` |
| 花的结构 | 花图式（floral diagram）与花程式 | `plant.floral_diagram` |
| 序列 | IUPAC 碱基与氨基酸代码，logo 按信息量（bit） | `sequence` 模块 |

### 3.3 文字与标注

- 字号层级：`title`（图内小标题）、`normal`（主要标注）、`small`（次要标注、引线标签）、`tiny`（5′/3′、结构内部的小字）。
- 引线标注用 `bio.callout(ax, 点, 文字位置, "Nucleus")`：细引线、末端小圆点，文字在引线外侧，引线尽量不交叉。
- 子图字母 `bio.panel(ax, "A", xy)`；比例尺 `bio.scale_bar`。
- 方向与极性必须标出：核酸的 5′/3′，膜的胞内外（`extracellular` / `cytoplasm` 或文字 "Outside" / "Inside"），时间轴的方向。

## 4. 绘图工具 wikibio

```python
import wikibio as bio

fig, ax = bio.canvas(12, 6)                       # 0..12 × 0..6，单位自定（默认 0.45 英寸/单位）
bio.cell(ax, (6, 3), 5, 2.6, kind="animal")       # animal / plant / bacterium
bio.nucleus(ax, (5, 3.2), 1.2)
bio.mitochondrion(ax, (8, 2), 1.6, 0.6, angle=20)
bio.bilayer(ax, [(0, 1), (12, 1)])                # 放大的脂双层（任意折线）
bio.receptor(ax, 4, 1, "gpcr", text="GPCR")       # gpcr / rtk / channel
bio.dna(ax, (1, 5), (6, 5), style="helix")        # helix / duplex / line
bio.strand(ax, (7, 5), (11, 5), cap=True, polya=True)
bio.protein(ax, (3, 4), 1.0, 0.8, "enzyme", text="PKA")
bio.arrow(ax, (3.5, 4), (5, 4), kind="activation")
bio.icon(ax, "servier/heart", at=(10, 3), height=2)
```

基础模块（`import wikibio as bio` 后直接用 `bio.…`）：`core`（画布、文字、箭头、框、平滑曲线）、`cell`（膜、细胞、细胞器）、`molecules`（核酸、蛋白、受体、离子、小分子）、`structures`（核糖体、微丝与微管、抗体、病毒、神经元、突触）、`icons`（图标）。

组合图模块（`from wikibio import genetics as G` 这样导入，用法见各模块开头的说明）：

| 模块 | 内容 | 主要用于 |
|---|---|---|
| `quant`、`charts` | 定量面板：`quant.Plot` 在画布坐标里画坐标轴与曲线（示意图与数据图同一张图时首选），`charts.axes_at` 放置真正的 matplotlib 坐标轴 | 全部课程 |
| `metabolism` | 代谢通路（`Pathway`：酶名、辅底物弧）、酶动力学、蛋白质拓扑图（β 折叠、螺旋、TOPS） | 7.1 |
| `molbio` | 复制叉、转录泡、翻译（核糖体 E/P/A 位、tRNA、肽链）、中心法则 | 7.2 |
| `cellbio` | 膜转运（通道、载体、泵）、细胞周期轮与检查点 | 7.3 |
| `genetics` | 系谱（NSGC）、Punnett 方格、染色体与核型、基因结构、SBOL 构建、质粒图谱、细胞分裂 | 7.4 |
| `development` | 形态发生素梯度与法国国旗模型、早期胚胎、果蝇体节基因 | 7.5 |
| `stats` | 生存分析（Kaplan–Meier、log-rank、Cox）、剂量–反应 4PL 拟合、稀释系列与孔板 | 7.7 |
| `physiology` | 分子马达与光镊、肌节与长度–张力、心动周期模型 | 7.6、7.14 |
| `sequence` | 多序列比对、序列 logo、基因组浏览器轨道、读段堆叠、点阵图 | 7.8 |
| `network` | SBGN 过程描述与活性流、调控网络模体、信号级联 | 7.9 及通路图 |
| `evolution` | Wright–Fisher 漂变与选择、固定概率、谱系图、性状选择（Lande–Arnold） | 7.10 |
| `microbio` | 细菌形态与鞭毛、革兰氏阳性/阴性细胞包膜、分批培养生长模型 | 7.11 |
| `phylo` | 系统发育树（Newick；矩形、斜线、环形；剪影、类群带、性状标记）、ICS 地质年代表 | 7.10、7.17 |
| `photosynthesis` | 类囊体膜复合体、Z 图式、Farquhar 光合模型、叶片气体交换 | 7.13 |
| `bioenergetics` | 线粒体内膜、呼吸链复合体 I–IV、ATP 合酶、结合变化与 c 环、质子动力势与 P/O 模型 | 7.1、7.3、7.6 |
| `immuno` | MHC I/II、TCR、CD4/CD8、BCR、免疫细胞、细胞因子 | 7.15 |
| `neuro` | 离子通道与膜片、电极、电路元件、Hodgkin–Huxley 与 LIF 模型 | 7.6、7.16 |
| `plant` | 花图式与花程式、蕨类等植物形态、世代交替 | 7.12 |
| `zoology` | 动物体制横切面与胚层 | 7.17 |
| `behaviour` | 边际值定理、鹰鸽博弈与复制者动力学 | 7.18 |
| `botany` | 参数化植物形态：叶形、叶尖、叶基、叶缘、叶脉、复叶、叶序与黄金角、花序、茎根叶横切（逐个细胞）、次生生长与木材、L 系统与空间殖民的树形 | 7.12、7.13 |
| `zoomorph` | 参数化动物形态：按目生成的昆虫（触角、口器、足、翅脉）、Raup 贝壳模型与缝合线、辐射对称体制、前肢同源骨 | 7.10、7.17 |
| `ecology` | 循环图（`cycle`，也用于细胞周期）、食物网、生态金字塔、年龄金字塔 | 7.19 |

原生绘制的元素可以任意缩放、着色、组合，**优先用原生元素**；器官、组织、生物个体、实验器材等复杂形象用图标（§5）。颜色标记可以用语义别名（`palette.ALIASES`，如 `actin`、`mhc`、`peptide`）：脚本写所画的对象，别名以后需要独立的颜色时只改调色板一处。

扩展 wikibio 的约定（写给维护者与智能体）：
- 颜色只用 `palette` 的标记；填充色上的文字用 `P.on_fill()`。
- 透明的面用 `PathPatch(..., fill=False)`，`alpha` 只在小于 1 时传：否则深色主题的重着色会把它变成不透明。
- 函数确定性（随机形状用固定种子或由文字生成种子），坐标单位与画布一致，返回关键锚点供箭头连接。
- 每个公开函数写英文文档字符串；新增功能后在样张（§7）里加一例，浅色、深色都要看过。
- wikibio 是绘图辅助包（`PLOT_HELPERS`）：修改它会使所有用到它的图重新渲染。

## 5. 图标库与许可

图标是从开源图库下载的 SVG，经 `scripts/icons.py` 转成矢量数据（`scripts/wiki/plot/icons/<来源>/<名称>.json`），并在 `icons/manifest.json` 登记作者、许可与来源网址。

| 来源 | 许可 | 内容 |
|---|---|---|
| Servier Medical Art（经 bioicons.com） | CC BY 3.0 / 4.0 | 器官、组织、细胞、细胞器、实验器材，风格接近 BioRender |
| DBCLS TogoTV（经 bioicons.com） | CC BY 4.0 | 生物、实验、分子 |
| bioicons.com 其他作者 | CC0、CC BY、CC BY-SA、MIT、BSD | |
| PhyloPic | CC0、公有领域、CC BY、CC BY-SA | 各类群的生物剪影（系统发育树、动植物、微生物） |
| Wikimedia Commons | 公有领域、CC0、CC BY、CC BY-SA | 动植物形态与解剖图解（如 LadyofHats 的公有领域图解），用作带部件的模板（§5.1） |
| SciDraw、NIH BioArt、Reactome 等 | CC BY、公有领域 | 实验动物、行为装置、生物医学插图（`svg:` 来源，许可由添加者从原页面核实） |

许可：
- **可以用**：公有领域、CC0、CC BY、CC BY-SA（2.0 及以上）、MIT、BSD。
- **用了 CC BY-SA 部件的图，整张图片按 CC BY-SA 4.0 发布**：构建在图下的署名行自动注明。SA 只约束这张图片，不影响网站其他内容与代码。
- **不用**：任何 NC（非商用）、ND（禁止演绎）许可，只有 GFDL 的文件，以及 BioRender、**教材**、论文、网络图片等未授予许可的素材。从教材 PDF 中提取的矢量图也不行：能提取不等于可以使用。教材只用来确定画什么（哪些结构、什么视角、标注哪些部件），画法由我们的模板与原生元素组合，不描摹任何一张受版权保护的图。

- 查找与添加（需要网络与 uv）：

  ```bash
  uv run --with svgelements python scripts/icons.py search heart
  uv run --with svgelements python scripts/icons.py add bioicons:Human_physiology/Servier/heart-front --id servier/heart --tags organ,circulation
  uv run --with svgelements python scripts/icons.py add "phylopic:Mus musculus" --id phylopic/mouse --tags mammal,model-organism
  uv run --with svgelements python scripts/icons.py add "wikimedia:Mature flower diagram.svg" --id wikimedia/flower-section --drop '^label'
  uv run --with svgelements python scripts/icons.py add svg:https://…/mouse.svg --id scidraw/mouse-rearing \
      --license "CC BY 4.0" --author "…" --page https://scidraw.io/drawing/…
  ```

- PhyloPic 的首选图像许可不合格时，工具会自动在该类群的其他图像、再在整个类群中找许可合格的；`phylopic:"Taxon#2"` 取第 2 个合格图像。类群回退可能选到外形不符的近缘种，加入后要看图确认。`add` 对清单加锁，可以并行运行。
- 图标 id 是 `<来源>/<英文名>`，小写、连字符：`servier/heart`、`dbcls/zebrafish`、`phylopic/arabidopsis`。同一对象有多种画法时加后缀（`servier/neuron-pyramidal`）。
- 在脚本中**必须以字符串字面量**调用：`bio.icon(ax, "servier/heart", ...)`。构建据此把图标计入缓存键，并在图下方自动注明作者与许可（CC BY 要求署名）。
- 单色剪影（PhyloPic）用 `color=` 着色为调色板标记（`color="plant"`）；多色插图保持原色，深色主题中黑色轮廓自动变浅、明暗层保持。

### 5.1 带部件的模板

结构复杂、视图标准的形态与解剖图（花的纵剖面、叶片横切、昆虫外形、骨骼、内部解剖）用**模板**：一张图标，其中的图形按部件命名。

- 转换时保留 SVG 中有意义的分组名（`id` 或 Inkscape 标签）作为部件名；编辑器自动生成的 id（`g123`、`path45`）忽略。`--drop` / `--keep` 按部件名的正则去掉标签、引线或只保留一部分。
- 原图分组没有语义时按颜色或序号命名：`icons.py colors <id>` 列出各填充色的图形与范围，`icons.py name <id> petal=#f4a9c4 sepal=#8bc34a stamen=12-30` 写入部件名。部件名用英文解剖学术语，小写、连字符（`petal`、`ovary`、`compound-eye`、`femur`）。
- 使用：`bio.icon(ax, id, …, parts={"stamen": "anther"}, mute="neutral")` 只给指定部件着色、其余淡化；`hide=[…]` 不画某些部件；`bio.icon_part(id, "ovary", <与 icon 相同的位置参数>)` 返回部件上的一点，供 `bio.callout` 引线标注。
- 模板里不能有文字：标签一律由脚本用 `bio.callout` 写（英文，随图注翻译）。原图的文字在转换时被跳过，残留的引线用 `--drop` 去掉。

### 5.2 图库的空缺（用原生元素画）

现有图库中没有合格图标、应在 wikibio 中原生绘制的对象（扩展时优先补这些）：溶酶体、过氧化物酶体与叶绿体以外的细胞器整体图（中心体、全细胞骨架）、星形胶质细胞、浆细胞、精子与卵细胞、卵裂各期胚胎；胎盘、肾上腺、甲状腺、生殖器官、全身骨骼与骨组织；花、种子、花粉与果实的写实图（模板，§5.1）；球菌、螺菌、弧菌与古菌细胞、冠状病毒；行为学装置（迷宫、笼）。Western blot、GWAS、测序读段等用真实的数据图画，不用图标。

## 6. 写作流程

1. 写正文时先想清楚每张图要说明的一个论点，在任务单或报告中列出"需要的图"。
2. 先查 `scripts/icons.py list` 和各模块的函数；需要新图标时按 §5 添加，需要新的原生元素或组合图时扩展 wikibio（§4 的约定），并在报告中说明。
3. 写绘图脚本，`.venv/bin/python scripts/wiki/plot/render_plot.py <脚本> <输出目录>` 渲染，浅色、深色两张都用 Read 看过：标注不重叠、箭头指向正确、颜色语义正确。
4. 图注写清图中每个元素与每一步；涉及立体化学、序列、系谱的，核对其正确性（必要时用 RDKit、Biopython 或手算验证）。

## 7. 样张

`scripts/wiki/plot/wikibio/gallery/` 中的脚本是每门学科的示例图，也是 wikibio 的回归测试：修改 wikibio 后重新渲染全部样张，确认没有破坏已有的图。

## 8. 写作原则：定量化与符号化

生物学模块不设单独的"生物数学建模"课程；**定量化与符号化是所有生物学课程的写作原则**。凡是能写成方程、模型或算法的机制（酶动力学、信号转导、基因调控网络、神经元动力学、种群与群落动力学、演化动力学），都要给出模型、参数的生物学意义、数值求解或模拟的绘图脚本，并链接数学（2.x）、统计（3.x）、计算机（4.x）、物理（5.x）与化学（6.x）中的工具，不重复推导。
