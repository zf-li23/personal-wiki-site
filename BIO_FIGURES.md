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
| `plant` | 花图式与花程式（`floral_diagram`；`floral_diagram_from_formula` 由花程式生成花图式；`floral_formula(..., style="cn")` 按中国教材写法画花程式，`floral_formula_tex` 给出页面正文用的同一 KaTeX 写法）；生活史类型（`life_cycle`：单倍体型、二倍体型、单双倍体型（世代交替）、红藻三相；`alternation_of_generations`）；真菌（`hypha` 有隔、无隔与锁状联合，`ascus`、`basidium` 按发育阶段，`paraphysis`，`hymenium` 沿任意曲线的子实层，`ascocarp` 子囊盘、子囊壳、闭囊壳、假囊壳剖面，`mushroom` 伞菌纵切或外形，`gill_section` 菌褶横切）；蕨类（`pinnule` 孢子囊群与囊群盖的类型，`leptosporangium` 环带与裂口，闭合、开裂、弹射；`frond`、`prothallus`、`sporangium`）；球果（`cone_scale` 苞鳞–种鳞复合体与小孢子叶，`cone` 松的雌雄球果、石松与卷柏、木贼的孢子叶球，纵切或外形） | 7.12 |
| `zoology` | 动物体制横切面与胚层 | 7.17 |
| `behaviour` | 边际值定理、鹰鸽博弈与复制者动力学；定向、节律、实验装置、群体运动与信号检测见独立模块 `wikibehav`（§4.2） | 7.18 |
| `botany` | 参数化植物形态：叶形、叶尖、叶基、叶缘、叶脉、复叶、叶序与黄金角、花序（含复穗状、多歧聚伞、轮伞、隐头花序）、茎根叶横切（逐个细胞）、气孔表面观（`stoma`：肾形与哑铃形保卫细胞，开与闭，不规则型、不等细胞型、平列型、横列型、四细胞型、辐射型副卫细胞）与表皮装片（`epidermis`：双子叶、单子叶、禾本科）、地衣横切（`lichen_section`：异层与同层）、次生生长与木材、L 系统与空间殖民的树形 | 7.12、7.13 |
| `zoomorph` | 参数化动物形态：按目生成的昆虫（触角、口器、足、翅脉）、Raup 贝壳模型与缝合线、辐射对称体制、前肢同源骨 | 7.10、7.17 |
| `ecology` | 循环图（`cycle`，也用于细胞周期）、食物网、生态金字塔、年龄金字塔 | 7.19 |

原生绘制的元素可以任意缩放、着色、组合，**优先用原生元素**；器官、组织、生物个体、实验器材等复杂形象用图标（§5）。颜色标记可以用语义别名（`palette.ALIASES`，如 `actin`、`mhc`、`peptide`）：脚本写所画的对象，别名以后需要独立的颜色时只改调色板一处。

扩展 wikibio 的约定（写给维护者与智能体）：
- 颜色只用 `palette` 的标记；填充色上的文字用 `P.on_fill()`。
- 透明的面用 `PathPatch(..., fill=False)`，`alpha` 只在小于 1 时传：否则深色主题的重着色会把它变成不透明。
- 函数确定性（随机形状用固定种子或由文字生成种子），坐标单位与画布一致，返回关键锚点供箭头连接。
- 每个公开函数写英文文档字符串；新增功能后在样张（§7）里加一例，浅色、深色都要看过。
- wikibio 是绘图辅助包（`PLOT_HELPERS`）：修改它会使所有用到它的图重新渲染。

### 4.1 脊椎动物比较解剖：vertskel

动物学（7.17）的脊椎动物类群章（7.17.44–54）与比较解剖章（7.17.55–67）画头骨、咽弓、椎骨、带骨、肢骨、动脉弓与肾管时，一律用绘图辅助模块 `vertskel`（`scripts/wiki/plot/vertskel.py`，与 wikibio 并列，`import vertskel as vs`）。它的核心是一张**同源配色表**：同一块骨（或同源的一串骨）在全课程永远同一颜色，读者可以在不同章节、不同类群之间追踪它。它是独立的辅助模块（`PLOT_HELPERS`）：修改它只使导入它的图重新渲染；它导入 wikibio，所以 wikibio 变化时这些图也会重新渲染。

**配色**（`vs.ELEMENTS`：键 → 英文名、系列、颜色；`vs.color(键)`、`vs.edge(键)`、`vs.name(键)`）：

| 系列 | 色相 | 元素（键） |
|---|---|---|
| 边缘系（有齿的上颌骨） | 橙 | `premaxilla`、`maxilla`、`septomaxilla` |
| 顶盖系 | 蓝 | `nasal`、`frontal`、`parietal`、`postparietal`（= `interparietal`） |
| 眶周系 | 绿 | `lacrimal`、`prefrontal`、`postfrontal`、`postorbital`、`jugal` |
| 颞系 | 紫 | `squamosal`、`quadratojugal`、`intertemporal`、`supratemporal`、`tabular` |
| 腭系 | 青 | `vomer`、`palatine`、`pterygoid`、`ectopterygoid`、`parasphenoid` |
| 鳃盖系 | 灰蓝 | `operculum`、`preoperculum`、`suboperculum`、`interoperculum`、`gular`、`branchiostegal` |
| 下颌膜骨 | 棕褐；隅骨柠檬绿 | `dentary`、`splenial`、`surangular`、`prearticular`（= `goniale`）、`coronoid`；`angular` = `tympanic` |
| 软颅及其骨化 | 沙色 | `chondrocranium`、`nasal_capsule`（= `ethmoid`）、`optic_capsule`、`otic_capsule`（= `petrosal`）、`prootic`、`opisthotic`、`trabecula`、`parachordal`、`orbitosphenoid`、`basisphenoid`、`occipital`、`basioccipital`、`exoccipital`、`supraoccipital` |
| 颌弓（第 1 弓） | 金、珊瑚红 | `palatoquadrate` = `quadrate` = `incus`；`epipterygoid` = `alisphenoid`；`meckel` = `articular` = `malleus` |
| 舌弓（第 2 弓） | 品红 | `hyomandibula` = `columella` = `stapes`；`symplectic`、`interhyal`、`epihyal`（= `styloid`）、`ceratohyal`、`hypohyal`、`basihyal`（= `hyoid`） |
| 鳃弓（第 3–7 弓） | 天蓝到灰紫，每弓一色 | `arch_3`（= `thyrohyal`）、`arch_4`（= `thyroid_cartilage`）、`arch_5`、`arch_6`（= `cricoid`、`arytenoid`）、`arch_7`、`basibranchial` |
| 椎骨 | | `centrum` = `pleurocentrum` 蓝，`intercentrum` 橙，`neural_arch`、`neural_spine`、`zygapophysis`、`transverse_process` 绿，`haemal_arch`（= `chevron`）、`haemal_spine` 粉，`rib` 棕褐，`notochord` 淡黄 |
| 肩带 | 软骨内骨冷色、膜骨暖色 | `scapula`、`suprascapula`、`coracoid`、`procoracoid`、`scapulocoracoid`；`cleithrum`、`clavicle`、`interclavicle`、`supracleithrum`、`posttemporal`；`sternum` |
| 腰带 | | `ilium` 紫、`ischium` 绿、`pubis` 橙、`puboischiadic` |
| 肢骨 | 与 `zoomorph.forelimb`、`limbdev` 相同 | `humerus` = `femur` = `stylopod`，`radius` = `tibia` = `zeugopod`，`ulna` = `fibula`，`carpals` = `tarsals`，`metacarpals` = `metatarsals`，`phalanges` = `autopod`；鳍：`metapterygium`、`mesopterygium`、`propterygium`、`radials`、`fin_rays` |
| 动脉弓 | 每弓一色 | `aortic_1` 金、`aortic_2` 浅绿、`aortic_3`（= `carotid`）青、`aortic_4`（= `systemic_arch`）红、`aortic_5` 紫、`aortic_6`（= `pulmonary_artery`、`ductus_arteriosus`）蓝；`dorsal_aorta`、`ventral_aorta`、`heart` |
| 肾与管 | 与 `mesoderm` 相同（Müller 管除外） | `pronephros` 橙、`mesonephros`（= `opisthonephros`、`epididymis`）淡紫、`metanephros` 绿、`gonad`；`archinephric_duct`（= `vas_deferens`，别名 `wolffian_duct`）蓝、`ureter` 青、`mullerian_duct`（= `oviduct`）粉、`bladder`、`cloaca` |

"=" 表示共用一种颜色（同源）。同一系列的元素是同一色相的不同明暗；需要按系列或按头骨的三个组成着色时传 `level="series"` 或 `level="component"`（膜颅蓝、软颅沙色、咽颅暖色）。表中没有的骨先在 `ELEMENTS` 加一行（按所属系列取同一色相，两种主题都看过），不要在脚本里写颜色。

**接口**：

- 形状（返回顶点，坐标由脚本决定）：`vs.rod(a, b, w, w2=None)` 骨干，`vs.oval(center, rx, ry, angle=0)`，`vs.smooth(points)` 平滑轮廓，`vs.poly(points)` 骨片（尖角、骨缝）。
- `vs.bone(ax, key, vertices, state="bone", level="element", text=None)` 画一块骨，返回中心。`state`："bone"（同源色）、"cartilage"（浅色加点纹，软骨的通行画法）、"context"（中性灰，非本图主角的骨）、"lost"（虚线轮廓：该类群已丢失，仅作对照）、"highlight"（粗轮廓）。
- `vs.draw(ax, parts, at=(0, 0), scale=1.0, flip=False)`：`parts` 是 `(键, 顶点)` 或 `(键, 顶点, {"state": …, "text": …, "z": …})` 的列表，后画的在上层；返回 `{键: 中心}`，供 `vs.callout(ax, 点, 文字位置, 键或文字)` 引线标注（键自动写成英文名）。
- `vs.panels(n, panel_w, panel_h, titles=…, subtitles=…, ncols=None, legend_rows=0)`：同一结构跨类群的系列图，返回 `(fig, ax, boxes)`，`boxes[i] = (x, y, w, h)`；`vs.legend(ax, entries, at, width, ncols=None)` 在下方画共用图例，同源的一串写成一项：`("quadrate", "palatoquadrate / quadrate / incus")`，第三项可写状态（`("meckel", "cartilage", "cartilage")`）。
- `vs.aortic_arches(ax, at, width, height, arches={…}, carotid_duct=True, roots=True, ductus=True, pulmonary=False, labels=None)`：腹面观（前端朝上，心脏在下；动物的左侧在读者右侧，图中标 L/R）的六对动脉弓。每弓的状态为 "present"、"gill"（经鳃毛细血管，分入鳃、出鳃两段）、"reduced"、"absent"（虚线），左右不同时写成 `(左, 右)`，如鸟 `{4: ("absent", "present")}`、哺乳类 `{4: ("present", "reduced")}`；`ductus="ligament"` 画闭合后的动脉韧带。返回各弓中点 `{(弓, "L"|"R"): 点}`。
- `vs.kidney_series(ax, at, width, height, stages={…}, ducts={…}, opisthonephros=False, gonad=False, bladder=False, rename={…})`：一侧的前肾、中肾、后肾与原肾管、输尿管、Müller 管，前端朝上。器官与管的状态为 "functional"、"embryonic"（虚线浅色，胚胎期短暂存在）、"modified"（浅色实线，如中肾成为附睾）、"absent"；`opisthonephros=True` 画无羊膜类的后位肾；`rename` 改标签（`{"archinephric_duct": "vas deferens"}`）。

约定：头骨与骨骼侧视时前端朝左；图是示意，类群之间不按比例（图注写明）。头骨的具体形状由各章脚本给出：先在 `vs.panels` 的每个面板里按局部坐标写出各骨的顶点，再 `vs.draw(..., at=(x, y))` 放入面板。

### 4.2 动物行为：wikibehav

动物行为学（7.18）的定向、节律、实验装置、群体运动与信号检测图用绘图辅助模块 `wikibehav`（`scripts/wiki/plot/wikibehav.py`，与 wikibio 并列，`import wikibehav as wb`）。它是独立的辅助模块（`PLOT_HELPERS`）：修改它只使导入它的图重新渲染；它导入 wikibio，颜色与字号与 wikibio 一致。完整接口见模块开头的说明，样张为 `gallery/c7.18-*.py`。

- **定向**（方位角：从正北顺时针的度数）：`wb.vonmises(mean, kappa, n, seed)` 抽样；`wb.mean_direction(a)` 平均方向与平均合向量长度 $r$；`wb.rayleigh(a)` Rayleigh 检验（返回 $r$、$z = nr^2$、$p$）；`wb.v_test(a, expected)` V 检验；`wb.emlen_funnel(ax, 中心, 半径, 划痕方位, sectors=24)` Emlen 漏斗俯视（漏斗壁、墨垫、划痕、计数扇区）；`wb.circular_plot(ax, 中心, 半径, a, token=…, expected=…, expected_text=…)` 圆形数据图（个体方向堆叠成点、平均向量箭头、期望方向虚线、"n, r, p" 一行）。
- **节律**：`wb.simulate_activity(days, tau, onset, alpha, taus=[(天, 周期)], shifts=[(天, 小时)], seed)` 模拟活动计数（先 LD 牵引、后 DD 自由运转、相移）；`act = wb.Actogram(ax, (x0, y0, w, h), t, counts, light=(6, 18), dd_from=…, ll_from=…, pulses=[(天, 时)])` 双重绘图的活动图（上方 LD 条，光期浅黄、暗期灰，光脉冲为星号）；`act.onsets(onsets)` 画活动起始线，`act.xy(天, 时)` 给出画布坐标。
- **实验装置**（俯视的线条图，墙为墨色、地面浅色，均返回锚点供引线标注）：`wb.t_maze`、`wb.y_maze`（`reward="left"|"right"`）、`wb.plus_maze`（高架十字迷宫，开放臂无墙）、`wb.radial_maze`（八臂迷宫，`baited`、`visited`）、通用的 `wb.arm_maze`；`wb.water_maze(ax, 中心, 半径, platform=(方位, 距离), path=wb.swim_path(platform, start, kind="direct"|"search"|"thigmotaxis"))` Morris 水迷宫（象限、隐藏平台、远端线索、游泳轨迹）；`wb.operant_box(ax, 中心, w, h, lever, light, key, hopper, speaker)` 操作箱侧视（提示灯、杠杆、啄键、食槽与外部颗粒分配器、栅格地板）。动物用图标放入（`bio.icon(ax, "phylopic/rat", at=box["inside"], …)`，图标 id 写在脚本里，以便注明来源）。
- **群体运动与导航**：`wb.couzin(n, steps, rr, ro, ra, blind, …)` Couzin 区域模型（排斥、对齐、吸引、后方盲区），`wb.COUZIN_REGIMES` 给出 swarm、torus、parallel 三组参数；`wb.polarization`、`wb.milling` 序参量；`wb.zones(ax, 中心, rr, ro, ra)` 区域示意；`wb.path_integration(steps, error, displace, search)` 沙漠蚁的路径整合（外出随机游走、沿整合向量归巢、位移实验的虚拟巢、扩展搜索环）；`to = wb.fit(点集, 框)` 把模拟坐标放入画布框；`wb.trail(ax, to(路径), fade=True, arrows=3)` 渐隐轨迹，`wb.school(ax, pos, head, to)` 画群体某一帧，`wb.agent` 画单个个体。
- **信号检测**（在 `quant.Plot` 上）：`wb.sdt_panel(p, d, xc)` 噪声与信号分布、判据、击中与虚报阴影、$d'$；`wb.roc_panel(q, dprimes, points)` ROC 曲线；`wb.sdt_rates`、`wb.dprime`、`wb.bias`。

## 5. 图标库与许可

图标是从开源图库下载的 SVG，经 `scripts/icons.py` 转成矢量数据（`scripts/wiki/plot/icons/<来源>/<名称>.json`），并在 `icons/manifest.json` 登记作者、许可与来源网址。

| 来源 | 许可 | 内容 |
|---|---|---|
| Servier Medical Art（经 bioicons.com） | CC BY 3.0 / 4.0 | 器官、组织、细胞、细胞器、实验器材，风格接近 BioRender |
| DBCLS TogoTV（经 bioicons.com） | CC BY 4.0 | 生物、实验、分子 |
| bioicons.com 其他作者 | CC0、CC BY、CC BY-SA、MIT、BSD | |
| PhyloPic | CC0、公有领域、CC BY、CC BY-SA | 各类群的生物剪影（系统发育树、动植物、微生物） |
| Wikimedia Commons | 公有领域、CC0、CC BY、CC BY-SA | 动植物形态与解剖图解（如 LadyofHats 的公有领域图解），用作带部件的模板（§5.1） |
| ViralZone（SIB） | CC BY 4.0 | 各病毒科的病毒体与复制周期示意（含冠状病毒）；署名 "ViralZone, SIB Swiss Institute of Bioinformatics" |
| IAN 符号库（UMCES，ian.umces.edu/media-library） | CC BY-SA 4.0 | 生态与多样性的扁平符号：植物、藻类、真菌与地衣、原生生物、细菌与古菌、病毒、生境（用到即整图按 CC BY-SA） |
| Reactome 图标库 | CC BY 4.0 | 蛋白、受体、通道、细胞器、细胞类型 |
| NIH BioArt（NIAID） | 多为公有领域，少数 CC BY（逐条核实） | 病原体、免疫细胞、实验器材 |
| SciDraw 等 | CC BY、公有领域 | 实验动物、行为装置（`svg:` 来源，许可由添加者从原页面核实） |

以上四个图库（ViralZone、IAN、Reactome、NIH BioArt）经作者同意（2026-11-04）作为补充动植物、微生物与病毒的首选来源，均以 `svg:` 来源加入（`icons.py add svg:<url> --license … --author … --page …`）；加入前确认 SVG 能干净转换（无渐变、嵌入位图或文字）。IAN 符号的 SVG 地址形如 `ian.umces.edu/site/assets/files/<n>/<slug>.svg`；媒体库的站内搜索不可用，用 `ian.umces.edu/media-library/sitemap.xml` 查找。各类群的查找顺序：动物 PhyloPic → IAN → Wikimedia 模板；植物 IAN → PhyloPic → Wikimedia；真菌、原生生物与藻类 IAN → PhyloPic；细菌与古菌 Bioicons → IAN → NIH BioArt；病毒 ViralZone → NIH BioArt；细胞与分子 Reactome → Servier → NIH BioArt。不用：AI 生成、许可非 CC 的图库（如 huashu-bird-sticker，PolyForm Shield 许可，位图）；照片、历史图版与显微照片等位图来源（BHL、CDC PHIL、iNaturalist 等）目前管线不支持，需要时另行决定。

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

现有图库中没有合格图标、应在 wikibio 中原生绘制的对象（扩展时优先补这些）：溶酶体、过氧化物酶体与叶绿体以外的细胞器整体图（中心体、全细胞骨架）、星形胶质细胞、浆细胞、精子与卵细胞、卵裂各期胚胎；胎盘、肾上腺、甲状腺、生殖器官、全身骨骼与骨组织；双子叶与单子叶茎横切（用 `wikibio.botany` 逐细胞绘制）、C4 叶片的花环结构；地衣的三种生长型（壳状、叶状、枝状）与粉芽、裂芽；球菌、螺菌、弧菌与古菌细胞、冠状病毒；行为学装置中迷宫与操作箱以外的笼具（迷宫、水迷宫、操作箱已由 `wikibehav` 原生绘制，§4.2）。Western blot、GWAS、测序读段等用真实的数据图画，不用图标。

## 6. 写作流程

1. 写正文时先想清楚每张图要说明的一个论点，在任务单或报告中列出"需要的图"。
2. 先查 `scripts/icons.py list` 和各模块的函数；需要新图标时按 §5 添加，需要新的原生元素或组合图时扩展 wikibio（§4 的约定），并在报告中说明。
3. 写绘图脚本，`.venv/bin/python scripts/wiki/plot/render_plot.py <脚本> <输出目录>` 渲染，浅色、深色两张都用 Read 看过：标注不重叠、箭头指向正确、颜色语义正确。
4. 图注写清图中每个元素与每一步；涉及立体化学、序列、系谱的，核对其正确性（必要时用 RDKit、Biopython 或手算验证）。

## 7. 样张

`scripts/wiki/plot/wikibio/gallery/` 中的脚本是每门学科的示例图，也是 wikibio 的回归测试：修改 wikibio 后重新渲染全部样张，确认没有破坏已有的图。

## 8. 写作原则：定量化与符号化

生物学模块不设单独的"生物数学建模"课程；**定量化与符号化是所有生物学课程的写作原则**。凡是能写成方程、模型或算法的机制（酶动力学、信号转导、基因调控网络、神经元动力学、种群与群落动力学、演化动力学），都要给出模型、参数的生物学意义、数值求解或模拟的绘图脚本，并链接数学（2.x）、统计（3.x）、计算机（4.x）、物理（5.x）与化学（6.x）中的工具，不重复推导。
