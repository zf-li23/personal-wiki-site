---
title: DNA 与染色质的聚合物物理
description: 把 DNA 与染色质当作聚合物的统计力学。自由连接链、Gauss 分布、回转半径与 Kuhn 长度；熵弹性与 Langevin 力–伸长定律；蠕虫链、持久长度、Kratky–Porod 由棒到线团的过渡与 Marko–Siggia 力–伸长定律；核酸的力学参数；排除体积、Flory 论证与 Flory 指数；基因组与染色体的大小及重叠；成环、环化与 J 因子（弯曲、熵与螺旋相位）；接触概率与 Hi-C、平衡球与分形球；噬菌体衣壳中 DNA 的包装，以及核小体的能量学与位点暴露。
source_hash: 8da575616372
---

DNA 分子只有几纳米粗，却可长达几厘米。在一个基因的尺度上它是一根刚性的棒；在整个基因组的尺度上它是一团随机线团，其形状不取决于化学，而取决于计数：在它可取的所有构象中，几乎全部都是蜷曲的。本章发展这种链的统计力学。最简单的模型，即由刚性链段构成的**随机行走**，已经给出溶液中基因组的大小、抵抗拉伸的熵弹簧，以及两个相距很远的位点相遇的概率（21.1–21.2 节）。弯曲刚度引入了一个长度尺度，即**持久长度**，并把随机行走变成**蠕虫链模型**，它描述从**核小体**到染色体的 DNA，并解释其**力–伸长曲线**（21.3 节）。**排除体积**使真实的链溶胀，并引出 Flory 指数（21.4 节）。本章其余部分把这些结果用于生物学：调控基因的 DNA 环的自由能与有效浓度（21.5 节），Hi-C 所测接触的标度及其对染色体折叠的说明（21.6 节），以及 DNA 在噬菌体衣壳与核小体中的包装，那里必须付出几十 $k_{\mathrm{B}}T$ 的弯曲能（21.7 节）。随机行走即 [7.6.5](/7.6.5) 的随机行走；持久长度与蠕虫链模型已在 [7.3.15](/7.3.15#sec-15.3.1) 中用于细胞骨架纤维，**染色质**的生物学见 [7.2.4](/7.2.4) 与 [7.3.17](/7.3.17)。用光镊与**磁镊**测量力–伸长曲线，以及 DNA 的过度拉伸与解链，是 [7.6.17](/7.6.17) 的主题；细胞骨架的纤维，也就是刚度更大的同一模型，将在 [7.6.26](/7.6.26) 中回来。

## 21.1. 作为随机行走的聚合物

### 21.1.1. 作为统计描述的结构

对折叠的蛋白质，“结构”是一组原子坐标，即 PDB 文件的内容（[7.6.10](/7.6.10)）。对溶液中的长 DNA 分子，没有这样的结构：热运动不断地使它重排，两个分子永远不会有相同的形状。可重复的是形状的分布，由几个平均值刻画：均方端到端距离 $\langle R^2\rangle$、**回转半径** $R_{\mathrm{g}}$（散射测得的大小，[7.6.9](/7.6.9#def-9.4.1)）以及链上两点靠近的概率。两个长度确定一条链：它的轮廓长度 $L$（B-DNA 每个碱基对 $0.34\,\mathrm{nm}$，所以 λ 噬菌体 48.5 kb 的基因组 $L = 16.5\,\mu\mathrm{m}$）与它保持笔直的长度。统计描述不是对无知的承认：对由数千个链段构成的线团，平均值是尖锐的，也正是实验所测量的。

### 21.1.2. 自由连接链

**定义 21.1.1（自由连接链）** **自由连接链**是由 $N$ 个长度为 $b$ 的刚性链段构成的链，各段连接成使每一段的方向 $\boldsymbol{u}_i$（$\lvert\boldsymbol{u}_i\rvert = 1$）与所有其他段独立，并在球面上均匀分布。它的端到端矢量为 $\boldsymbol{R} = b\sum_{i=1}^{N}\boldsymbol{u}_i$，轮廓长度为 $L = Nb$。

端到端矢量是 $N$ 步、步长为 $b$ 的**随机行走**（[7.6.5](/7.6.5#def-5.1.1)）的位置，所以随机行走的结果可以照搬。

**命题 21.1.1（自由连接链的大小与形状）** 对自由连接链，

$$
\langle\boldsymbol{R}\rangle = \boldsymbol{0}, \qquad \langle R^2\rangle = Nb^2 = Lb, \qquad R_{\mathrm{g}}^2 = \frac{Nb^2}{6} \quad (N \gg 1), \tag{21.1}
$$

且当 $N$ 很大时，端到端矢量的分布为

$$
P(\boldsymbol{R}) = \left(\frac{3}{2\pi Nb^2}\right)^{3/2}\exp\left(-\frac{3R^2}{2Nb^2}\right). \tag{21.2}
$$

**证明** 由于 $\langle\boldsymbol{u}_i\cdot\boldsymbol{u}_j\rangle = \delta_{ij}$，$\langle R^2\rangle = b^2\sum_{i,j}\langle\boldsymbol{u}_i\cdot\boldsymbol{u}_j\rangle = Nb^2$。$\boldsymbol{R}$ 的每个直角分量是 $N$ 个均值为 0、方差为 $b^2/3$ 的独立项之和，所以由**中心极限定理**（[3.1.13](/3.1.13)），它服从方差为 $Nb^2/3$ 的正态分布；三个分量不相关，且渐近独立，由此得式 (21.2)。对回转半径，写 $R_{\mathrm{g}}^2 = \frac{1}{N^2}\sum_{i<j}\langle r_{ij}^2\rangle$，其中 $r_{ij}$ 是关节 $i$ 与 $j$ 之间的距离（恒等式 $\frac1N\sum_i\lvert\boldsymbol{r}_i - \boldsymbol{r}_{\mathrm{cm}}\rvert^2 = \frac{1}{N^2}\sum_{i<j}r_{ij}^2$ 对任何点集都成立）。$i$ 与 $j$ 之间的一段本身是自由连接链，$\langle r_{ij}^2\rangle = \lvert j - i\rvert b^2$，而 $\sum_{i<j}(j - i) \approx N^3/6$，所以 $R_{\mathrm{g}}^2 \approx Nb^2/6$。$\square$

在大于一个链段的所有尺度上统计性质都由式 (21.2) 描述的链，称为理想链或 Gauss 链。有两点对生物学重要。第一，大小按 $\sqrt{N}$ 而不是 $N$ 增长：线团大部分是溶剂，长度加倍只使它增大 $\sqrt2$ 倍。第二，最可几的端到端矢量是 $\boldsymbol{R} = \boldsymbol{0}$；最可几的*距离* $R = \lvert\boldsymbol{R}\rvert$ 不为零，只是因为径向分布中的因子 $4\pi R^2$，它计入了方向的数目。

### 21.1.3. 真实的链与 Kuhn 长度

真实的聚合物不是自由连接的。碳链上相继的键以固定的角度相接；DNA 相继的碱基对几乎平行地堆叠。但方向之间的相关性沿链衰减，相关性范围有限的链，在远大于该范围的尺度上又是一个步长更大的随机行走。对由 $N$ 个长度为 $\ell$ 的键构成、每个键与前一个键成固定夹角的链，$\langle\boldsymbol{u}_i\cdot\boldsymbol{u}_{i+k}\rangle = \alpha^k$，其中 $\alpha = \cos\theta$，持续随机行走的计算（[7.6.5](/7.6.5#sec-5.1.2)）给出 $\langle R^2\rangle \approx N\ell^2(1 + \alpha)/(1 - \alpha)$。每一条这样的链在大尺度上都由一个数来刻画。

**定义 21.1.2（Kuhn 长度）** 对轮廓长度为 $L$、均方端到端距离为 $\langle R^2\rangle$ 的长链，**Kuhn 长度**为 $b = \lim_{L\to\infty}\langle R^2\rangle/L$。由 $N = L/b$ 个长度为 $b$ 的链段构成的自由连接链，轮廓长度与 $\langle R^2\rangle$ 都与之相同；它就是该聚合物的等效自由连接链。

在生理盐浓度下，DNA 的 $b \approx 100\,\mathrm{nm} \approx 300\,\mathrm{bp}$（21.3 节）；单链 DNA 与 RNA 约为 $1.5$–$3\,\mathrm{nm}$；未折叠的多肽约为 $0.8\,\mathrm{nm}$，大致是两个残基。用 Kuhn 链段取代化学细节完整的链，是本课程中最原始意义上的**粗粒化**的第一个例子（[7.6.1](/7.6.1)）：低于 Kuhn 长度的细节改变 $b$，但不改变大尺度定律的形式。

### 21.1.4. 溶液中基因组的大小

**例 21.1.1（从噬菌体与细菌中释放出的基因组）** 经渗透压休克的噬菌体 T2 的电镜照片显示其 DNA 铺展在空的头部周围。基因组约有 $1.5\times10^5\,\mathrm{bp}$，$L = 51\,\mu\mathrm{m}$，即 $N = L/b \approx 500$ 个 Kuhn 链段。由式 (21.1) 并取 $b = 2\ell_{\mathrm{p}}$（21.3 节），

$$
R_{\mathrm{g}} = \sqrt{\frac{Lb}{6}} = \sqrt{\frac{L\ell_{\mathrm{p}}}{3}} = \sqrt{\frac{5.1\times10^4\,\mathrm{nm}\times50\,\mathrm{nm}}{3}} \approx 0.9\,\mu\mathrm{m},
$$

这是照片中缠结物的尺度，而头部宽 $0.1\,\mu\mathrm{m}$。*E. coli* 的 $4.6\times10^6\,\mathrm{bp}$ 染色体（$L = 1.6\,\mathrm{mm}$）所占的线团 $R_{\mathrm{g}} \approx 5\,\mu\mathrm{m}$，比细胞还大。因此这两个基因组都被容器压缩，体积上分别压缩约 $10^3$ 倍（噬菌体）与 $10^2$ 倍（拟核），本章的很大一部分是关于这种压缩的代价。

Gauss 分布也说明线团被拉伸的可能性有多小。对 *E. coli* 基因组（$N \approx 1.6\times10^4$），一维端到端距离为 $500b$ 相对于零的概率密度为 $\mathrm{e}^{-500^2/2N} \approx 4\times10^{-4}$，对 $1000b$ 则为 $\mathrm{e}^{-31} \approx 3\times10^{-14}$：几乎所有构象相对于轮廓长度都是紧致的，把两端拉开就意味着只能从极小的一部分构象中挑选。这就是熵弹性的起源。

## 21.2. 熵弹性

### 21.2.1. 熵弹簧

把理想链的两端固定在间距 $\boldsymbol{R}$ 处。与此约束相容的构象数正比于 $P(\boldsymbol{R})$，所以**构象熵**为 $S(\boldsymbol{R}) = k_{\mathrm{B}}\ln P(\boldsymbol{R}) + \mathrm{const}$。对自由连接链，能量不依赖于构象，自由能纯粹是熵的。

**命题 21.2.1（熵弹簧）** 端到端矢量为 $\boldsymbol{R}$ 的理想链，其自由能与恢复力为

$$
F(\boldsymbol{R}) = -TS(\boldsymbol{R}) = \frac{3k_{\mathrm{B}}T}{2Nb^2}R^2 + \mathrm{const}, \qquad \boldsymbol{f} = -\frac{\partial F}{\partial\boldsymbol{R}} = -\frac{3k_{\mathrm{B}}T}{Nb^2}\boldsymbol{R}, \tag{21.3}
$$

这是劲度为 $k = 3k_{\mathrm{B}}T/(Lb)$ 的 Hooke 弹簧。

这是**熵力**（[7.6.2](/7.6.2#def-2.3.1)）的原型。它的标志是劲度正比于温度：受热的橡皮筋、这类链的网络会收缩。劲度还反比于长度，所以长链极软。对 λ DNA，$k = 3\times4.1\,\mathrm{pN\,nm}/(1.65\times10^4\,\mathrm{nm}\times100\,\mathrm{nm}) \approx 7\times10^{-6}\,\mathrm{pN\,nm^{-1}} = 7\,\mathrm{fN}\,\mu\mathrm{m}^{-1}$：$0.01\,\mathrm{pN}$ 的力就能把它拉长一微米以上。这就是为什么单分子实验中的 DNA 系链必须用至少零点几皮牛顿的力拉伸，其伸长才有明确的定义。

### 21.2.2. 受张力的自由连接链

式 (21.3) 预言恒力会使链无限伸长，这不可能是真的：伸长不能超过 $L$。Gauss 分布只在 $R = 0$ 附近成立。自由连接链对力 $\boldsymbol{F} = F\boldsymbol{e}_z$ 的精确响应，可以把功的项加到能量上得到：每个构象的能量为 $-\boldsymbol{F}\cdot\boldsymbol{R} = -Fb\sum_i\cos\theta_i$，各链段是独立的。

**定理 21.2.1（自由连接链的力–伸长）** 由 $N$ 个长度为 $b$ 的链段构成的自由连接链，在沿 $z$ 的力 $F$ 作用下，平均伸长为

$$
\langle z\rangle = Nb\,\mathcal{L}\!\left(\frac{Fb}{k_{\mathrm{B}}T}\right), \qquad \mathcal{L}(u) = \coth u - \frac{1}{u}, \tag{21.4}
$$

其中 $\mathcal{L}$ 是 Langevin 函数。在一维情形（链段只沿 $\pm z$ 方向），$\langle z\rangle = Nb\tanh(Fb/k_{\mathrm{B}}T)$。

**证明** **配分函数**可以因子化，$Z = Z_1^N$，其中

$$
Z_1 = \int_0^{2\pi}\!\mathrm{d}\varphi\int_0^{\pi}\mathrm{e}^{\beta Fb\cos\theta}\sin\theta\,\mathrm{d}\theta = 2\pi\int_{-1}^{1}\mathrm{e}^{\beta Fbx}\,\mathrm{d}x = \frac{4\pi\sinh(\beta Fb)}{\beta Fb},
$$

$\beta = 1/k_{\mathrm{B}}T$。平均伸长为 $\langle z\rangle = k_{\mathrm{B}}T\,\partial\ln Z/\partial F = Nk_{\mathrm{B}}T\,\partial\ln Z_1/\partial F = Nb\left[\coth(\beta Fb) - 1/(\beta Fb)\right]$。在一维情形 $Z_1 = 2\cosh(\beta Fb)$，同样求导得 $\tanh$。$\square$

在小力下 $\mathcal{L}(u) \approx u/3$，$\langle z\rangle = Nb^2F/(3k_{\mathrm{B}}T)$ 就是式 (21.3) 的线性弹簧；在大力下 $\mathcal{L}(u) \approx 1 - 1/u$，链趋近其轮廓长度，$1 - \langle z\rangle/L \approx k_{\mathrm{B}}T/(Fb)$。转折发生在 $F \approx k_{\mathrm{B}}T/b$：双链 DNA（$b = 100\,\mathrm{nm}$）约为 $0.04\,\mathrm{pN}$，而单链 DNA（$b \approx 1.5\,\mathrm{nm}$）约为 $3\,\mathrm{pN}$。因此对同样碱基数的双链和柔软的单链，刚性的双螺旋在低力下更容易拉伸，两条曲线在几皮牛顿处交叉，这一事实被用来在单分子实验中追踪解旋酶对 DNA 的解旋（[7.6.17](/7.6.17)）。双链 DNA 的实测曲线在低力下遵循式 (21.4)，但趋近完全伸长的速度较慢，为 $F^{-1/2}$ 而不是 $F^{-1}$；解释这一点，需要把自由关节换成连续的弯曲。

## 21.3. 蠕虫链

### 21.3.1. 弯曲能与持久长度

双螺旋更适合描述为一根平滑弯曲的细弹性棒。设 $\boldsymbol{r}(s)$ 为其轴线，以弧长 $s \in [0, L]$ 为参数，$\boldsymbol{t}(s) = \mathrm{d}\boldsymbol{r}/\mathrm{d}s$ 为单位切矢量。曲率为 $\lvert\mathrm{d}\boldsymbol{t}/\mathrm{d}s\rvert = 1/R_{\mathrm{c}}$，其中 $R_{\mathrm{c}}$ 是局部**曲率半径**。对 Young 模量为 $E$、截面二次矩为 $I$ 的棒的小形变，弹性理论给出弯曲能

$$
E_{\mathrm{bend}} = \frac{\kappa}{2}\int_0^L\left\lvert\frac{\mathrm{d}\boldsymbol{t}}{\mathrm{d}s}\right\rvert^2\mathrm{d}s, \qquad \kappa = EI, \tag{21.5}
$$

其中**抗弯刚度** $\kappa$ 的单位是能量乘长度。**蠕虫链模型**就是具有这一能量、再无其他相互作用的温度为 $T$ 的链（[7.3.15](/7.3.15#sec-15.3.1)）。把其中长度为 $\ell$ 的一段弯成半径为 $R_{\mathrm{c}}$ 的圆弧，代价为 $\kappa\ell/(2R_{\mathrm{c}}^2)$；特别地，把长度 $L$ 闭合成圆（$R_{\mathrm{c}} = L/2\pi$）的代价为

$$
E_{\mathrm{circle}} = \frac{2\pi^2\kappa}{L}. \tag{21.6}
$$

这一能量与热能的竞争，定义了链保持笔直的长度的上限。

**命题 21.3.1（蠕虫链的切向相关）** 在三维中，平衡态下蠕虫链的切矢量满足

$$
\langle\boldsymbol{t}(s)\cdot\boldsymbol{t}(s')\rangle = \mathrm{e}^{-\lvert s - s'\rvert/\ell_{\mathrm{p}}}, \qquad \ell_{\mathrm{p}} = \frac{\kappa}{k_{\mathrm{B}}T}. \tag{21.7}
$$

**证明** 记 $g(s) = \langle\boldsymbol{t}(0)\cdot\boldsymbol{t}(s)\rangle$。由于能量 (21.5) 是链的相继各段独立贡献之和，$[s_1, s_1 + s_2]$ 这一段的弯曲在统计上与 $s_1$ 处的方向无关。选坐标轴使 $\boldsymbol{t}(s_1)$ 沿 $z$；则 $\boldsymbol{t}(0)\cdot\boldsymbol{t}(s_1 + s_2)$ 对第二段的方位角取平均，得 $(\boldsymbol{t}(0)\cdot\boldsymbol{t}(s_1))(\boldsymbol{t}(s_1)\cdot\boldsymbol{t}(s_1 + s_2))$，所以 $g(s_1 + s_2) = g(s_1)g(s_2)$，$g$ 是指数函数，$g(s) = \mathrm{e}^{-s/\ell_{\mathrm{p}}}$。为求 $\ell_{\mathrm{p}}$，考虑长度为 $\Delta s$ 的短段弯过一个小角 $\theta$，其能量为 $\kappa\theta^2/(2\Delta s)$。该角有两个独立的分量（弯曲可以发生在两个平面内），各自的能量都是二次的，所以由**能量均分定理**，$\langle\theta^2\rangle = 2k_{\mathrm{B}}T\Delta s/\kappa$，而 $g(\Delta s) = \langle\cos\theta\rangle \approx 1 - \langle\theta^2\rangle/2 = 1 - \Delta s\,k_{\mathrm{B}}T/\kappa$。与 $\mathrm{e}^{-\Delta s/\ell_{\mathrm{p}}} \approx 1 - \Delta s/\ell_{\mathrm{p}}$ 比较，得 $\ell_{\mathrm{p}} = \kappa/k_{\mathrm{B}}T$。$\square$

因此**持久长度** $\ell_{\mathrm{p}}$ 就是把它弯成平缓圆弧大约花费一个 $k_{\mathrm{B}}T$ 的长度。对 DNA，$\ell_{\mathrm{p}} \approx 50\,\mathrm{nm} \approx 150\,\mathrm{bp}$，$\kappa = \ell_{\mathrm{p}}k_{\mathrm{B}}T \approx 200\,\mathrm{pN\,nm^2}$；取半径 $1\,\mathrm{nm}$（$I = \pi r^4/4$），对应 $E \approx 0.3\,\mathrm{GPa}$，是类似硬塑料的模量。肌动蛋白丝（$\ell_{\mathrm{p}} \approx 17\,\mu\mathrm{m}$）与微管（毫米量级）是 $\kappa$ 大得多的同一模型，因为 $I$ 按半径的四次方增长（[7.3.15](/7.3.15#sec-15.3.1)）。图中用模拟离散链检验了命题 21.3.1。

![三维离散蠕虫链的 Monte Carlo 构象（链段长 0.1 ℓp，弯曲角按弯曲能的 Boltzmann 分布抽取）。A：轮廓长度分别为 2、20 和 200 ℓp 的构象各一个，各自按自己的比例绘制，并附有长度 ℓp 的标尺（对 DNA 为 300 bp、3 kb 和 30 kb）：轻微弯曲的棒、蜿蜒的细丝与随机线团。B：长为 1、5 和 50 ℓp 的链（各 4000 条）的端到端距离 R 的分布，以均方根值为标度，并与均方值相同的 Gauss 分布比较：短链几乎是直的，其距离集中在轮廓长度附近；当 L ≫ ℓp 时恢复为 Gauss 链](./plots/wlc-conformations.py)

### 21.3.2. 从棒到线团

**公式 21.3.1（Kratky–Porod）** 轮廓长度为 $L$、持久长度为 $\ell_{\mathrm{p}}$ 的蠕虫链满足

$$
\langle R^2\rangle = 2\ell_{\mathrm{p}}L - 2\ell_{\mathrm{p}}^2\left(1 - \mathrm{e}^{-L/\ell_{\mathrm{p}}}\right), \tag{21.8}
$$

当 $L \ll \ell_{\mathrm{p}}$ 时它等于 $L^2$（棒），当 $L \gg \ell_{\mathrm{p}}$ 时等于 $2\ell_{\mathrm{p}}L$（线团），并且

$$
R_{\mathrm{g}}^2 = \frac{\ell_{\mathrm{p}}L}{3} - \ell_{\mathrm{p}}^2 + \frac{2\ell_{\mathrm{p}}^3}{L} - \frac{2\ell_{\mathrm{p}}^4}{L^2}\left(1 - \mathrm{e}^{-L/\ell_{\mathrm{p}}}\right). \tag{21.9}
$$

**证明** 由 $\boldsymbol{R} = \int_0^L\boldsymbol{t}(s)\,\mathrm{d}s$ 与命题 21.3.1，

$$
\langle R^2\rangle = \int_0^L\!\!\int_0^L\mathrm{e}^{-\lvert s - s'\rvert/\ell_{\mathrm{p}}}\,\mathrm{d}s\,\mathrm{d}s' = 2\int_0^L\mathrm{d}s\int_0^{L-s}\mathrm{e}^{-u/\ell_{\mathrm{p}}}\,\mathrm{d}u = 2\ell_{\mathrm{p}}\int_0^L\left(1 - \mathrm{e}^{-(L-s)/\ell_{\mathrm{p}}}\right)\mathrm{d}s,
$$

这就是式 (21.8)。式 (21.9) 由 $R_{\mathrm{g}}^2 = \frac{1}{L^2}\int_0^L\!\int_0^{s'}\langle\lvert\boldsymbol{r}(s') - \boldsymbol{r}(s)\rvert^2\rangle\,\mathrm{d}s\,\mathrm{d}s'$ 得出：代入长度为 $s' - s$ 的一段的式 (21.8) 并积分。$\square$

式 (21.8) 就是 [7.3.15](/7.3.15#sec-15.3.1) 中对纤维引用的蠕虫链公式，这里给出了推导。把它的长链极限与定义 21.1.2 比较，得到本章通篇使用的关系：

$$
b = 2\ell_{\mathrm{p}}. \tag{21.10}
$$

DNA 的 Kuhn 长度约为 $100\,\mathrm{nm}$。过渡是渐进的：在 $L = \ell_{\mathrm{p}}$ 时，$\langle R^2\rangle = 0.74L^2$，链仍然是棒状的；要超过约 $10\ell_{\mathrm{p}}$（1.5 kb 的 DNA）才趋近线团极限。因此核小体大小的 DNA 片段，或几百个碱基对的调控环，既不是棒也不是线团，其力学必须用完整的蠕虫链来计算。

![切向相关与由棒到线团的过渡。A：4 ℓp 的模拟蠕虫链（20000 条，圆点）上的切向相关，与 exp(−s/ℓp)（命题 21.3.1）的比较；在半对数坐标上衰减是斜率为 −1/ℓp 的直线。B：均方端到端距离相对于棒值 L² 与线团值 2ℓpL，随 L/ℓp 的变化，圆点为模拟，线为式 (21.8)；上方坐标轴换算成 DNA 的碱基对数（ℓp = 50 nm = 147 bp），并标出核小体中 DNA 的长度、lac O1–O2 环与 λ 基因组](./plots/wlc-crossover.py)

持久长度可以用几种独立的方法测量，对中等盐浓度下的 DNA，它们是一致的：由吸附在表面上并用电镜或原子力显微镜成像的分子的形状（在二维中，式 (21.7) 中的 $\ell_{\mathrm{p}}$ 换成 $2\ell_{\mathrm{p}}$）；由不同长度片段的光散射与流体力学（通过式 (21.9) 与**流体力学半径**，[7.6.8](/7.6.8)）；由环化速率（21.5 节）；以及由力–伸长曲线（21.3.3 小节）。

### 21.3.3. 受张力的蠕虫链

沿 $z$ 的力 $F$ 给能量 (21.5) 加上 $-F\int_0^L t_z\,\mathrm{d}s$。精确解把问题映射为量子转子（切矢量在单位球面上做随机行走，力的作用像一个场），伸长是 $\cos\theta$ 的基态期望值，必须数值计算。不过它的两个极限可以由简单的论证得到。

在小力下，线性响应给出 $\langle z\rangle = F\langle R_z^2\rangle/k_{\mathrm{B}}T$，对长链 $\langle R_z^2\rangle = \langle R^2\rangle/3 = 2\ell_{\mathrm{p}}L/3$，所以

$$
\langle z\rangle = \frac{2\ell_{\mathrm{p}}L}{3k_{\mathrm{B}}T}F, \tag{21.11}
$$

即 $b = 2\ell_{\mathrm{p}}$ 的熵弹簧 (21.3)。在大力下链几乎是直的，$\boldsymbol{t} \approx (t_x, t_y, 1 - t_\perp^2/2)$，能量到小横向分量的二阶为

$$
E = \int_0^L\left[\frac{\kappa}{2}\left(\frac{\mathrm{d}\boldsymbol{t}_\perp}{\mathrm{d}s}\right)^2 + \frac{F}{2}t_\perp^2\right]\mathrm{d}s - FL.
$$

把 $\boldsymbol{t}_\perp$ 展开为波数 $q$ 的 **Fourier 级数**模式，每个模式的两个分量各有能量 $\frac{L}{2}(\kappa q^2 + F)\lvert t_q\rvert^2$，由均分定理 $\langle\lvert t_q\rvert^2\rangle = k_{\mathrm{B}}T/[L(\kappa q^2 + F)]$。对模式求和（积分 $L\int\mathrm{d}q/2\pi$），

$$
\langle t_\perp^2\rangle = 2\int_{-\infty}^{\infty}\frac{\mathrm{d}q}{2\pi}\frac{k_{\mathrm{B}}T}{\kappa q^2 + F} = \frac{k_{\mathrm{B}}T}{\sqrt{\kappa F}},
\qquad
\frac{\langle z\rangle}{L} = 1 - \frac{\langle t_\perp^2\rangle}{2} = 1 - \frac12\sqrt{\frac{k_{\mathrm{B}}T}{F\ell_{\mathrm{p}}}}. \tag{21.12}
$$

以 $F^{-1/2}$ 缓慢趋近完全伸长，是连续弯曲的标志：力 $F$ 只抑制长于 $\sqrt{\kappa/F}$ 的热起伏，更短的起伏依然存在。Marko 与 Siggia（1995）把两个极限合成一个公式。

**公式 21.3.2（Marko–Siggia 内插）** 蠕虫链在力 $F$ 下的相对伸长 $z = \langle z\rangle/L$ 近似满足

$$
\frac{F\ell_{\mathrm{p}}}{k_{\mathrm{B}}T} = z + \frac{1}{4(1 - z)^2} - \frac14, \tag{21.13}
$$

它在 $z \ll 1$ 时化为式 (21.11)，在 $1 - z \ll 1$ 时化为式 (21.12)，在 $z \approx 0.5$ 附近与精确解至多相差约 10 %。

![理想链的力–伸长。A：一维与三维自由连接链（定理 21.2.1，Kuhn 长度 b = 2ℓp）、精确的蠕虫链（转子问题的基态）以及 Marko–Siggia 内插（公式 21.3.2）的相对伸长随无量纲力 Fℓp/kBT 的变化；小力时它们有相同的线性响应 z = 2Fℓp/3kBT，但大力时自由连接链按 1/F、蠕虫链按 F^(−1/2) 趋近完全伸长。B：物理单位下的 λ DNA（16.5 µm，ℓp = 50 nm），力取对数坐标：0.1 pN 以下分子是柔软的熵弹簧，1 至 10 pN 之间趋近其轮廓长度，约 10 pN 以上发生弹性拉伸（可伸长蠕虫链，拉伸模量 S = 1000 pN），约 65 pN 时过度拉伸（7.6.17）；自由连接链拟合低力数据，但拟合不了趋近完全伸长的行为](./plots/force-extension.py)

对 DNA 弹性的最初测量（Smith、Finzi 与 Bustamante，1992，用磁珠；后来用**光镊**）用式 (21.13) 拟合，得 $\ell_{\mathrm{p}} \approx 50\,\mathrm{nm}$，这使持久长度成为分子生物物理中测得最准的数之一。高于约 $10\,\mathrm{pN}$ 时双螺旋本身被拉伸，可伸长蠕虫链在式 (21.12) 上加一项 $F/S$，拉伸模量 $S \approx 1000\,\mathrm{pN}$。曲线如何测量，以及更远处会发生什么（过度拉伸平台与两条链的解开），连同仪器一起在 [7.6.17](/7.6.17) 中讨论。同样的公式给出拉伸所做的功：在恒力下，伸长到 $z$ 的链中储存的自由能为 $\Delta G = \int_0^{F}\langle z\rangle\,\mathrm{d}F'$，一个蛋白质的结合若使 DNA 或蛋白质系链变短或变长，其亲和力就改变 $\mathrm{e}^{\pm\beta\Delta G}$ 倍，这就是力调控结合的方式（[7.6.17](/7.6.17) 与 [7.6.31](/7.6.31) 的主题）。

### 21.3.4. 核酸的力学参数

| 量 | 双链 DNA | 单链 DNA | 备注 |
|---|---|---|---|
| 每单元的升高 | 每 bp $0.34\,\mathrm{nm}$ | 每核苷酸约 $0.6$–$0.7\,\mathrm{nm}$ | 同样碱基数时单链的轮廓更长 |
| 持久长度 $\ell_{\mathrm{p}}$ | $45$–$50\,\mathrm{nm}$（一价盐高于 $\sim 10\,\mathrm{mM}$） | 约 $1\,\mathrm{nm}$（依赖盐浓度） | dsRNA 约 $60\,\mathrm{nm}$ |
| Kuhn 长度 $b = 2\ell_{\mathrm{p}}$ | 约 $100\,\mathrm{nm} = 300\,\mathrm{bp}$ | 约 $2\,\mathrm{nm}$ | |
| **弯曲刚度** $\kappa = \ell_{\mathrm{p}}k_{\mathrm{B}}T$ | 约 $200\,\mathrm{pN\,nm^2}$ | | |
| 拉伸模量 $S$ | 约 $1000\,\mathrm{pN}$ | | 弹性范围 $10$–$50\,\mathrm{pN}$ |
| 扭转刚度 $C$ | $410$–$450\,\mathrm{pN\,nm^2}$（扭转持久长度 $C/k_{\mathrm{B}}T \approx 100\,\mathrm{nm}$） | 无（自由转动） | 与**超螺旋** DNA 有关（[7.2.3](/7.2.3)） |
| 特征力 | 过度拉伸约 $65\,\mathrm{pN}$；解链 $10$–$15\,\mathrm{pN}$ | | 在 [7.6.17](/7.6.17) 中测量 |

带电聚合物的持久长度含有静电部分。磷酸基沿骨架相互排斥，弯曲使它们靠近；排斥在 **Debye 长度** $\kappa_{\mathrm{D}}^{-1}$ 内被屏蔽，Odijk 与 Skolnick–Fixman 的理论给出，对处于 Manning 电荷密度（**反离子凝聚**，[7.6.6](/7.6.6)）的链，附加的持久长度为 $\ell_{\mathrm{el}} = 1/(4\kappa_{\mathrm{D}}^2\ell_{\mathrm{B}})$，其中 **Bjerrum 长度** $\ell_{\mathrm{B}} = 0.7\,\mathrm{nm}$。在 $10\,\mathrm{mM}$ 盐浓度下（$\kappa_{\mathrm{D}}^{-1} \approx 3\,\mathrm{nm}$）这只有约 $3\,\mathrm{nm}$，所以 DNA 的实测 $\ell_{\mathrm{p}}$ 在生理盐浓度下几乎不变，只在很低的盐浓度下才上升。对本身刚性很小的单链核酸与未折叠蛋白质，静电硬化与排除体积要重要得多。

## 21.4. 排除体积与 Flory 指数

### 21.4.1. 自回避链

理想链可以与自身相交：沿轮廓相距很远的两个链段可以占据空间中的同一点。真实的链不能这样，而在良溶剂中，链段更愿意与溶剂而不是彼此接触，它们在短程上相互排斥。禁止重访格点的随机行走，即自回避行走，比理想行走更为伸展，并且溶胀随长度增长，因为更长的行走有更多自我相交的机会。于是大小用另一个 $N$ 的幂来描述。

**定义 21.4.1（Flory 指数）** 若由 $N$ 个链段构成的聚合物，大小在 $N$ 很大时按 $R \propto N^{\nu}$ 变化，则指数 $\nu$ 称为它的 **Flory 指数**：理想链 $\nu = 1/2$；良溶剂中的自回避链，Flory 近似下 $\nu = 3/5$（三维中精确值为 $\nu = 0.588$）；不良溶剂中的致密球 $\nu = 1/3$。

**命题 21.4.1（Flory 论证）** 由 $N$ 个长度为 $b$ 的链段构成、每对链段的**排除体积**为 $v$、被限制在半径为 $R$ 的线团内的链，其自由能为

$$
\frac{F(R)}{k_{\mathrm{B}}T} \approx \frac{3R^2}{2Nb^2} + \frac{vN^2}{2R^3}, \tag{21.14}
$$

在 $R^5 = vb^2N^3/2$ 处最小，所以 $R \propto N^{3/5}$。

**证明** 第一项是命题 21.2.1 的熵弹簧，抵抗溶胀。第二项是对排斥的平均场估计：$N$ 个链段充满量级为 $R^3$ 的体积，浓度为 $N/R^3$；$N^2/2$ 对链段中每一对以概率 $v/R^3$ 重叠，代价为 $k_{\mathrm{B}}T$ 量级。令 $\partial F/\partial R = 3R/(Nb^2) - \frac32 vN^2/R^4 = 0$，得 $R^5 = vb^2N^3/2$。$\square$

这个论证高估了两项（弹性项忽略了排斥所造成的相关，排斥项忽略了链段密度并不均匀），高估的程度相近，所以得到的指数接近精确值。$v$ 的符号取决于溶剂。在链段相互吸引的不良溶剂中，$v < 0$，链塌缩成球，$R \propto N^{1/3}$，这是致密物体的标度。在 $\theta$ 温度下，吸引与硬核排斥相互抵消（$v = 0$），链是理想的；熔体中的聚合物，或是其他染色体之中的染色体，也近乎理想，因为其链段间的排斥被其他链所屏蔽（Flory 定理）。

![排除体积与 Flory 指数。A：简单立方格点上随机行走与自回避行走的均方端到端距离随步数的变化（用枢轴算法抽样）；随机行走遵循 N¹，自回避行走遵循 N^1.176（ν = 0.588），二者之比随长度增大。B：N = 100、300 和 1000（b = 1，v = 1）时式 (21.14) 的 Flory 自由能：最小值（圆点）按 N^(3/5) 向外移动](./plots/flory.py)

### 21.4.2. 蛋白质与无序链

这些指数是可以测量的。化学变性的蛋白质，对 $N$ 个残基遵循 $R_{\mathrm{g}} \approx 0.2\,\mathrm{nm}\times N^{0.59}$（Kohn 等，2004，由 SAXS，[7.6.9](/7.6.9)），这是良溶剂中自回避链的标度，而折叠的蛋白质遵循 $R_{\mathrm{g}} \approx 0.22\,\mathrm{nm}\times N^{0.38}$，接近致密指数 $1/3$。**内在无序蛋白**介于二者之间，$\nu$ 由其电荷与疏水性决定，约为 $0.45$ 到 $0.6$；由 SAXS 与单分子 FRET 测得的指数，是序列如何控制系综的一个简明总结（[7.6.16](/7.6.16)）。对 DNA，排除体积很弱，因为双螺旋很细（$2\,\mathrm{nm}$），而 Kuhn 长度很长（$100\,\mathrm{nm}$）：只有超过约 $10^3$–$10^4$ 个 Kuhn 长度的链，溶胀才变得明显，所以病毒的基因组以及实验中使用的较短片段接近理想链。

## 21.5. 成环与 J 因子

### 21.5.1. 两端相遇的概率

许多过程要求同一 DNA 分子上的两个位点接触：结合在两个操纵序列上的阻遏蛋白（[7.2.11](/7.2.11)）、与启动子相遇的增强子（[7.2.14](/7.2.14)）、连接成环的片段两端、由重组酶拉到一起的重组位点。相关的量是轮廓长度为 $L$ 的链的两端相距在一个小距离 $\delta$ 之内的概率。对理想链与 $\delta \ll \sqrt{Lb}$，Gauss 分布 (21.2) 在该小球内几乎为常数，

$$
p(\delta) \approx \frac{4\pi\delta^3}{3}P(\boldsymbol{0}) = \frac{4\pi\delta^3}{3}\left(\frac{3}{2\pi Lb}\right)^{3/2} \propto L^{-3/2}. \tag{21.15}
$$

随长度的衰减依赖于维数：在一维中，$N$ 步的行走回到原点的比例为 $\binom{N}{N/2}2^{-N} \approx \sqrt{2/\pi N}$，只按 $N^{-1/2}$ 下降，这可由 **Stirling 公式**看出。在三维中，长环很罕见，因为两端有空间游离开去。概率密度 $P(\boldsymbol{0})$ 的单位是体积的倒数，自然可以把它表示为浓度。

**定义 21.5.1（J 因子）** DNA 片段的 **J 因子**是它的一端在另一端附近的有效摩尔浓度，$J = P(\boldsymbol{R} = \boldsymbol{0})/N_{\mathrm{A}}$，其中 $P$ 是端到端矢量的概率密度（在需要两端有特定相对取向时，还要乘以相应的因子）。它是分子内缔合（环化、成环）的平衡常数与分离分子之间同样缔合的平衡常数之比。

第二句话解释了为什么 $J$ 是被测量的量。在环化实验中（Shore 与 Baldwin，1983），带互补单链末端的片段被 **DNA 连接酶**连接成环（反应速率正比于 $J$）或二聚体（正比于其他片段的浓度）；环与二聚体之比直接给出 $J$。在基因调控中，结合在一个操纵序列上的阻遏蛋白看到的第二个操纵序列的浓度是 $J$：若它对该位点的**解离常数**为 $K_{\mathrm{d}}$，则成环状态相对于单结合状态的统计权重是 $J/K_{\mathrm{d}}$。当 $J$ 超过 $K_{\mathrm{d}}$ 时成环是有利的，对纳摩尔的阻遏蛋白，这要求 $J$ 达到几十到几百纳摩尔。

对 Gauss 链，式 (21.15) 给出

$$
J_{\mathrm{G}}(L) = \frac{1}{N_{\mathrm{A}}}\left(\frac{3}{2\pi Lb}\right)^{3/2} \approx 0.53\,\mu\mathrm{M}\times n^{-3/2}, \qquad n = L/b, \tag{21.16}
$$

若 DNA 在该尺度上是柔性的，则长为一个 Kuhn 长度（300 bp）的环约为 $0.5\,\mu\mathrm{M}$。但它不是，短环必须弯曲。

### 21.5.2. 弯曲与熵

**命题 21.5.1（圆模型中的最优环长）** 把长度为 $L$ 的环的自由能近似为圆的弯曲能 (21.6)，加上使两端靠拢的熵代价，即式 (21.15) 的 $-k_{\mathrm{B}}T\ln P(\boldsymbol{0})$：

$$
\frac{\Delta G_{\mathrm{loop}}(L)}{k_{\mathrm{B}}T} = \frac{2\pi^2\ell_{\mathrm{p}}}{L} + \frac32\ln L + \mathrm{const}. \tag{21.17}
$$

$\Delta G_{\mathrm{loop}}$ 最小，从而 $J \propto \mathrm{e}^{-\Delta G_{\mathrm{loop}}/k_{\mathrm{B}}T}$ 最大，在 $L^* = 4\pi^2\ell_{\mathrm{p}}/3 \approx 13\ell_{\mathrm{p}}$ 处。

**证明** $\mathrm{d}\Delta G_{\mathrm{loop}}/\mathrm{d}L = k_{\mathrm{B}}T(-2\pi^2\ell_{\mathrm{p}}/L^2 + 3/2L) = 0$ 在 $L = 4\pi^2\ell_{\mathrm{p}}/3$ 处成立；那里二阶导数为正。$\square$

对 DNA，$2\pi^2\ell_{\mathrm{p}}/L \approx 3000/N_{\mathrm{bp}}$：把 150 bp 闭合成环的代价约为 $20\,k_{\mathrm{B}}T$，1.5 kb 只需 $2\,k_{\mathrm{B}}T$。该模型预言最优值在 $1900\,\mathrm{bp}$ 附近。环化测量把它定在 $500\,\mathrm{bp}$ 附近，最大 $J$ 约为 $10^{-7}\,\mathrm{M}$。这一差异的来源很简单：几个**持久长度**的环不必是圆。它的两端可以通过泪滴形等在关键处弯曲较少的形状相遇，而对所有闭合形状求和的完整蠕虫链，在中等长度处的闭合概率大得多。蠕虫链的数值结果可以用内插公式（Rippe，2001）很好地表示：

$$
J(L) \approx 0.53\,\mu\mathrm{M}\times n^{-3/2}\exp\left(-\frac{2.66}{n^2}\right), \qquad n = L/b, \tag{21.18}
$$

它对长环趋于式 (21.16)，在 $n \approx 1.9$ 处达到峰值，即约 $550\,\mathrm{bp}$，$J \approx 100\,\mathrm{nM}$。

![DNA 成环的 J 因子。A：DNA（ℓp = 50 nm）的 J 随环长的变化：Gauss 链（式 (21.16)），按 L^(−3/2) 下降；圆模型，即 Gauss 值乘以把 DNA 弯成圆的 Boltzmann 因子，最大值在 1900 bp 附近（命题 21.5.1）；以及蠕虫链（内插式 (21.18)），峰值在 550 bp 附近，约 100 nM，在几个 kb 以上与 Gauss 链一致；标出了 lac O1–O3 与 O1–O2 环的长度。B：必须使两个位点位于螺旋同一面的环的螺旋相位，扭转持久长度为 100 nm：J 随 10.5 bp 的螺旋重复周期振荡，在无相位要求的值与一个最小值之间，该最小值随长环更容易吸收不足一圈的扭转而升高](./plots/j-factor.py)

### 21.5.3. 扭转、相位与细胞中的成环

蛋白质结合在双螺旋的一个面上。要使 DNA 在同一面上的两个位点之间成环，这一段必须被扭转一个螺旋圈的分数部分 $\delta = N_{\mathrm{bp}}/10.5 - \operatorname{round}(N_{\mathrm{bp}}/10.5)$，对扭转持久长度 $C \approx 100\,\mathrm{nm}$，代价为 $2\pi^2C\delta^2k_{\mathrm{B}}T/L$，与式 (21.6) 类似。所以短环对其位点的螺旋相位敏感，这种敏感性按 $1/L$ 衰减。加上弯曲项与熵项，这就是 [7.2.11](/7.2.11#sec-11.6.4) 中用于乳糖操纵子的三项环自由能；阻遏随 10–11 bp 的周期振荡，在 70–80 bp 附近最强，是其实验标志。

有两个观察表明裸蠕虫链在哪里失效。第一，对 60–90 bp 的环，式 (21.18) 预言的 $J$ 远低于 $1\,\mathrm{nM}$，但 lac 阻遏在体内很强：HU 和 IHF 等结构蛋白使 DNA 急剧弯曲，负超螺旋把相距较远的位点拉到一起，阻遏蛋白四聚体本身也有柔性，所以体内的环比裸 DNA 中容易形成得多（Boedicker、Garcia 与 Phillips，2013，系统测量了体内环的自由能）。第二，曾有报道称短于约 100 bp 的裸片段的环化，比蠕虫链所允许的频繁得多（Cloutier 与 Widom，2004），而重复测量发现一直到约 105 bp 都与之相符（Du 等，2005），单分子 FRET 成环则又发现 100 bp 以下的成环增强（Vafabakhsh 与 Ha，2012）。高度弯曲的 DNA 是否通过瞬时的扭折或泡来释放应力，这会使其弯曲能在大曲率下比式 (21.5) 增长得更慢，仍有争论；答案对核小体很重要，因为那里 DNA 被弯到半径 $4\,\mathrm{nm}$。

## 21.6. 作为聚合物的染色体

### 21.6.1. 重叠与疆域

细胞核中的基因组比自由线团密得多。染色质的线性堆积密度与刚度不同于裸 DNA：对核小体纤维，约为 $\nu_{\ell} \approx 8\,\mathrm{bp\,nm^{-1}}$（若它是核小体链）或 $\nu_{\ell} \approx 100\,\mathrm{bp\,nm^{-1}}$（若它在体外折叠成 30 nm 纤维），Kuhn 长度为 $60$–$400\,\mathrm{nm}$ 量级。于是含 $N_{\mathrm{bp}}$ 个碱基对的一段有 $\langle R^2\rangle = N_{\mathrm{bp}}b/\nu_{\ell}$，而 $b/\nu_{\ell}$ 是染色质在大尺度上唯一的材料参数。

**例 21.6.1（酵母染色体会重叠吗？）** 出芽酵母的细胞核宽 $2\,\mu\mathrm{m}$，含有总计 12 Mb 的 16 条染色体，密度为 $3\,\mathrm{Mb}\,\mu\mathrm{m}^{-3}$。一条平均 750 kb 的染色体若是自由的核小体纤维（$\nu_{\ell} = 8\,\mathrm{bp\,nm^{-1}}$，$L = 94\,\mu\mathrm{m}$，$\ell_{\mathrm{p}} \approx 30\,\mathrm{nm}$），则 $R_{\mathrm{g}} = \sqrt{L\ell_{\mathrm{p}}/3} \approx 1\,\mu\mathrm{m}$，其线团内部的密度为 $750\,\mathrm{kb}/(\frac43\pi R_{\mathrm{g}}^3) \approx 0.2\,\mathrm{Mb}\,\mu\mathrm{m}^{-3}$，比核的密度低十倍以上。自由线团必须强烈地互相穿插，像碗里的意大利面。对人的染色体，同样的估算给出，在宽 $10\,\mu\mathrm{m}$ 的细胞核中平均染色体的 $R_{\mathrm{g}} \approx 13\,\mu\mathrm{m}$。

:::

间期染色体仍然各自占据不同的**染色体疆域**（[7.3.17](/7.3.17#def-17.7.1)），这并非平衡聚合物统计的结果；它需要与核膜和核仁的拴系，一段缓慢的非平衡历史（染色体从致密的有丝分裂棒状体解凝，没有时间混合），或二者兼有。聚合物物理也能解读被标记位点的位置。在 *Caulobacter crescentus* 中，每个位点沿细胞有明确的位置，标准差约 $0.2\,\mu\mathrm{m}$，与其基因组位置无关。若这种散布是两端被锚定、含 $N_{\mathrm{bp}}$ 个碱基对的 DNA 自由环的散布，$\sigma_x^2 = \langle R^2\rangle/3 = N_{\mathrm{bp}}b/(3\nu_{\ell})$，取 $b = 100\,\mathrm{nm}$、$\nu_{\ell} = 3\,\mathrm{bp\,nm^{-1}}$，得 $N_{\mathrm{bp}} \approx 4\,\mathrm{kb}$（对封闭环约为其两倍）：染色体的行为像一串约 10 kb 的结构域沿细胞被拴住，与用其他方法测得的细菌染色体拓扑结构域一致。

### 21.6.2. 接触概率与 Hi-C

**染色体构象捕获**及其全基因组版本 Hi-C（[7.2.4](/7.2.4#sec-4.3)）对每一对位点测量它们在细胞群体中被交联在一起的频率。对基因组取平均，得到接触概率 $P(s)$ 随基因组间隔 $s$ 的变化：这是对聚合物模型的直接检验，因为式 (21.15) 就是接触概率。

**定义 21.6.1（接触概率）** 聚合物的**接触概率** $P(s)$，是沿链相隔 $s$ 的两个单体的距离在固定捕获距离之内的概率，对所有这类单体对与所有构象取平均。

**命题 21.6.1（平均场接触标度）** 若 $s$ 个单体的一段的大小为 $R(s) \propto s^{\nu}$，其两端分布在量级为 $R(s)^3$ 的体积中，则

$$
P(s) \propto s^{-3\nu}: \qquad s^{-3/2}\ \text{（理想链）}, \qquad s^{-1}\ \text{（在所有尺度上致密的链）}. \tag{21.19}
$$

**证明** 一端落在另一端的捕获体积 $v_{\mathrm{c}}$ 之内的概率，是 $v_{\mathrm{c}}$ 乘以接触处端到端分布的密度，后者的量级为 $1/R(s)^3$。对理想链，这一点由式 (21.15) 精确成立。对致密的一段，$\nu = 1/3$。$\square$

这一标度可以区分染色质的模型。被限制在细胞核中的理想链，即平衡球，遵循 $s^{-3/2}$，直到一段充满可用的体积，然后趋平：相距很远的位点与任何其他位点一样频繁地相遇。酵母染色体在约 100 kb 以内遵循 $s^{-3/2}$。人的间期染色体则不然：Lieberman-Aiden 等（2009）发现在 $0.5$–$7\,\mathrm{Mb}$ 上 $P(s) \propto s^{-1.08}$，接近分形球的预言。

**定义 21.6.2（分形球）** **分形球**（又称褶皱球，Grosberg、Nechaev 与 Shakhnovich，1988）是长聚合物的一种致密、无结的非平衡构象，其中链的每一段本身都是致密的，$R(s) \propto s^{1/3}$，并占据自己的空间区域，如同链先塌缩成小球、再塌缩成球的球那样逐级塌缩。

分形球有一些对基因组很有吸引力的性质：每个位点可以为转录而解凝，不必解开邻近的位点，因为各段互不穿插，整条染色体的疆域化组织就是同一性质在最大尺度上的表现。这个模型并非定论。更高分辨率的 Hi-C 揭示了由**黏连蛋白**在 CTCF 位点停止的**环挤出**所形成的环与**拓扑关联域**（[7.2.4](/7.2.4#sec-4.3)），含挤出的聚合物模拟既重现了这些结构域，也重现了中间尺度上接近 $-1$ 的指数；被**凝缩蛋白**压缩成围绕轴的环阵列的有丝分裂染色体，在约 10 Mb 以内 $P(s) \propto s^{-0.5}$，更为平缓。如今解读接触图谱，常规做法是对带有这类主动、特异约束的聚合物做模拟，这正是本章模型的直接应用。

![接触概率与染色体折叠。A：16 × 16 格点上的两种致密折叠，沿链从一端到另一端着色：Hilbert 曲线是理想化的分形球，其中每一段占据自己的致密区域；受限的随机行走（平衡球），其各段互相穿插。B：对立方格点上 300 条 4096 步的随机行走的模拟，接触概率随沿链间隔的变化：自由行走遵循 s^(−3/2)（命题 21.6.1）；被限制在立方体中的行走遵循 s^(−3/2)，直到一段充满立方体，然后达到平台。图中还给出分形球的预言 s^(−1) 以及 Hi-C 在 0.5–7 Mb 上对人染色体测得的斜率（−1.08）作比较](./plots/contact-probability.py)

## 21.7. 包装 DNA：病毒与核小体

### 21.7.1. DNA 包装得有多紧？

轮廓长度与容器大小之比夸大了压缩的程度。更好的量度是堆积分数 $\phi$：DNA 本身的体积（直径 $2\,\mathrm{nm}$ 的圆柱，每个碱基对约 $1\,\mathrm{nm}^3$）除以其容器的体积。λ 噬菌体把 48.5 kb 包装进内半径约 $27\,\mathrm{nm}$ 的衣壳：$\phi \approx 4.85\times10^4\,\mathrm{nm}^3/(\frac43\pi\times27^3\,\mathrm{nm}^3) \approx 0.6$，接近 DNA 晶体的密度。*E. coli* 拟核（5 Mb 处于半径约 $0.25\,\mu\mathrm{m}$ 的区域）$\phi \approx 0.1$；人的精子头部（以鱼精蛋白包装，宽 $5\,\mu\mathrm{m}$）$\phi \approx 0.02$；人的体细胞核（$6\times10^9\,\mathrm{bp}$ 在半径 $5\,\mu\mathrm{m}$ 的球中）$\phi \approx 0.01$。只有在噬菌体中，DNA 才紧密到使其包装成为双螺旋尺度上的弹性与静电问题。

### 21.7.2. 包装噬菌体衣壳

有尾噬菌体与疱疹病毒先组装空的衣壳，然后用 ATP 驱动的马达通过门户蛋白把基因组泵入，噬菌体 φ29 中的马达是由 ASCE 家族的五个 ATP 酶组成的环。光镊测量（Smith 等，2001）表明，φ29 的马达在填充量低时每秒包装约 100 bp，随衣壳被填满而变慢，并要对抗随接近完成而上升到几十皮牛顿的阻力；马达在约 $57\,\mathrm{pN}$ 时停转，这使它成为已知最强的分子马达之一。其动力学（每个 ATP 2.5 bp，环每个周期以 10 bp 为一个爆发）是 [7.6.28](/7.6.28) 的主题。这里我们计算它必须克服的力。

**公式 21.7.1（反向线轴模型）** 设包装好的 DNA 缠成由衣壳壁向内的环线轴，六方堆积，轴间距为 $d_{\mathrm{s}}$，处于内半径为 $R$、高为 $z$ 的圆柱形衣壳中。当长度 $L$ 已被包装时，环的弯曲能与相邻螺旋的相互作用能为

$$
G_{\mathrm{bend}} = -\frac{\pi\ell_{\mathrm{p}}k_{\mathrm{B}}Tz}{\sqrt3\,d_{\mathrm{s}}^2}\ln\left(1 - \frac{\sqrt3\,d_{\mathrm{s}}^2L}{2\pi zR^2}\right), \qquad G_{\mathrm{int}} = \sqrt3\,F_0\left(c^2 + cd_{\mathrm{s}}\right)L\,\mathrm{e}^{-d_{\mathrm{s}}/c}, \tag{21.20}
$$

每个 $L$ 处的间距使 $G = G_{\mathrm{bend}} + G_{\mathrm{int}}$ 最小，阻力为 $F(L) = \mathrm{d}G/\mathrm{d}L$。

弯曲能由对各个环的能量 $\pi\ell_{\mathrm{p}}k_{\mathrm{B}}T/R_i$（式 (21.6) 取 $L = 2\pi R_i$）求和得出：半径为 $R'$ 的一层含 $z/d_{\mathrm{s}}$ 个环，各层相距 $\sqrt3 d_{\mathrm{s}}/2$，线轴从外半径向内填充，直到由已包装长度决定的内半径。相互作用项积分的是六方堆积 DNA 的实测渗透压 $\Pi(d_{\mathrm{s}}) = F_0\mathrm{e}^{-d_{\mathrm{s}}/c}$，在很宽的盐浓度范围内衰减长度 $c \approx 0.27\,\mathrm{nm}$（Rau 与 Parsegian，1984）；这几纳米间距上的排斥来自螺旋之间有结构的水与离子，即水合力，[7.6.6](/7.6.6) 的平均场静电学并未包含它。两项相互竞争：弯曲倾向于松散堆积，使内层的环不太紧；排斥倾向于间距均匀。该模型给出包装过程中从约 $4$ 减小到 $2.5\,\mathrm{nm}$ 的间距，与 X 射线与冷冻电镜的测量一致，并给出几十皮牛顿的力和完全包装时几十个大气压的内压。

![把 DNA 包装进噬菌体衣壳（反向线轴模型，公式 21.7.1，ℓp = 50 nm，F0 = 55000 pN nm⁻²，c = 0.27 nm）。A：λ 衣壳、*E. coli* 拟核、人的精子头部与人的细胞核中 DNA 的堆积分数（对数坐标）。B：使自由能最小的轴间距随已包装基因组分数的变化，对应 φ29（19.3 kb）与 λ（48.5 kb，体积与其衣壳相同的圆柱）；它降到约 2.5 nm，与 X 射线散射的测量一致。C：马达所受的阻力，在包装的最后三分之一急剧上升，并给出完全包装时的内压；点线标出 φ29 马达的停转力（约 57 pN）](./plots/phage-packing.py)

储存的能量对感染有影响。λ 噬菌体在约一分钟内把其基因组注入细胞，在体外，注入囊泡或由受体 LamB 触发后的注入，会被几十个大气压的外部渗透压部分或完全抑制（Evilevitch 等，2003）：衣壳内的压力驱动注入的第一部分，最后一部分则由宿主中的过程拉入，例如转录、结合蛋白以及细胞质的渗透梯度。

### 21.7.3. 核小体

**核小体核心颗粒**把 147 bp 以 1.65 圈左手螺旋缠绕在**组蛋白**八聚体周围，半径约 $4.2\,\mathrm{nm}$（[7.2.4](/7.2.4)）。由式 (21.5) 取均匀曲率，弯曲能为

$$
G_{\mathrm{bend}} = \frac{\ell_{\mathrm{p}}k_{\mathrm{B}}T}{2R^2}L = \frac{50\,\mathrm{nm}}{2\times(4.2\,\mathrm{nm})^2}\times50\,\mathrm{nm}\times k_{\mathrm{B}}T \approx 70\,k_{\mathrm{B}}T, \tag{21.21}
$$

约为每个碱基对 $0.5\,k_{\mathrm{B}}T$。它由磷酸骨架与组蛋白的精氨酸、赖氨酸在小沟朝向八聚体的 14 个位点上的接触来补偿；净的缠绕自由能是两个大数之间的小差值，约为每个碱基对零点几个 $k_{\mathrm{B}}T$。弯曲的代价依赖于序列：与螺旋重复同相的 AA/TT 步，在小沟朝内之处，使某些序列更易弯曲，这是**核小体定位**（[7.2.4](/7.2.4)）的序列偏好的基础。

净自由能很小，所以核小体是动态的。热涨落使 DNA 从两端瞬时剥离，使其内部的位点暴露给蛋白质：这就是位点暴露模型（Polach 与 Widom，1995）。

**命题 21.7.1（位点暴露）** 设蛋白质只有在 DNA 从较近的一端解开到该位点（距入口 $x$ 个碱基对）时才能结合到核小体内的位点上，并设解开每个碱基对要花费自由能 $g$，此外有一个初始解开平衡 $K_0$。则位点暴露的**平衡常数**为 $K_{\mathrm{exp}}(x) = K_0\mathrm{e}^{-gx/k_{\mathrm{B}}T}$，浓度为 $c$、对裸 DNA 的解离常数为 $K_{\mathrm{d}}$ 的蛋白质占据该位点的概率为

$$
p = \frac{K_{\mathrm{exp}}c/K_{\mathrm{d}}}{1 + K_{\mathrm{exp}}c/K_{\mathrm{d}}}, \tag{21.22}
$$

也就是说，表观解离常数为 $K_{\mathrm{d}}/K_{\mathrm{exp}}$（设 $K_{\mathrm{exp}} \ll 1$）。

**证明** 各状态为：缠绕的（权重 1）、解开到该位点且空着的（权重 $K_{\mathrm{exp}}$）、解开且结合的（权重 $K_{\mathrm{exp}}c/K_{\mathrm{d}}$）；结合的比例是最后一个权重与总和之比，当 $K_{\mathrm{exp}} \ll 1$ 时即式 (21.22)。$\square$

对已知位置的位点做限制性内切酶消化，得到的平衡常数从入口附近的约 $10^{-2}$ 降到核小体中部的约 $10^{-4}$–$10^{-5}$，与每个碱基对 $g \approx 0.1$–$0.2\,k_{\mathrm{B}}T$ 一致。单分子 FRET 揭示了动力学：核小体保持完全缠绕约 $250\,\mathrm{ms}$，然后瞬时解开 $10$–$50\,\mathrm{ms}$（Li、Levitus、Bustamante 与 Widom，2005）。位点暴露平衡也是协同性的一种机制：结合在同一核小体上位点的两个转录因子分摊解开的代价，所以一个的结合提高了另一个的占据率，二者之间无需任何接触。在力的作用下，外圈在几个皮牛顿时逐渐解开，内圈在 20–30 pN 时突然解开（[7.6.17](/7.6.17)），这正是聚合酶与重塑因子（[7.2.15](/7.2.15)）工作时的力。

![核小体的能量学与缠绕 DNA 的可及性。A：核小体 DNA 每个碱基对的自由能收支：半径 4.2 nm 处的弯曲代价约为每 bp +0.48 kBT（式 (21.21)），与组蛋白的黏附获得约每 bp −0.6 kBT，净值只是二者之一的一小部分。B：位点暴露模型（命题 21.7.1）：暴露一个位点的平衡常数随其距入口距离的变化，净解开代价分别取每 bp 0.1、0.15 和 0.2 kBT，并标出限制性内切酶可及性所测值的大致范围。C：蛋白质对一个位点的占据率随其浓度相对于对裸 DNA 的解离常数的变化，位点分别位于核小体内 10、30 和 60 bp（g = 每 bp 0.15 kBT）：缠绕使结合曲线移动 1/K_exp 倍，对中央位点最多可达五个数量级](./plots/nucleosome-accessibility.py)

## 小结

| 模型 | 主要结果 | 出处 |
|---|---|---|
| 自由连接链 | $\langle R^2\rangle = Nb^2$，Gauss 分布 $P(\boldsymbol{R})$，$R_{\mathrm{g}}^2 = Nb^2/6$ | 命题 21.1.1 |
| 大尺度上的真实链 | Kuhn 长度 $b = \langle R^2\rangle/L$；DNA $b \approx 100\,\mathrm{nm}$ | 定义 21.1.2 |
| 熵弹簧 | $k = 3k_{\mathrm{B}}T/(Lb)$，正比于 $T$ | 命题 21.2.1 |
| 受力的自由连接链 | $\langle z\rangle = L\,\mathcal{L}(Fb/k_{\mathrm{B}}T)$，$1 - z \propto F^{-1}$ | 定理 21.2.1 |
| 蠕虫链 | $\langle\boldsymbol{t}(s)\cdot\boldsymbol{t}(0)\rangle = \mathrm{e}^{-s/\ell_{\mathrm{p}}}$，$\ell_{\mathrm{p}} = \kappa/k_{\mathrm{B}}T$；$b = 2\ell_{\mathrm{p}}$ | 命题 21.3.1、式 (21.10) |
| 由棒到线团 | $\langle R^2\rangle = 2\ell_{\mathrm{p}}L - 2\ell_{\mathrm{p}}^2(1 - \mathrm{e}^{-L/\ell_{\mathrm{p}}})$ | 公式 21.3.1 |
| 受力的蠕虫链 | 线性 $2\ell_{\mathrm{p}}LF/3k_{\mathrm{B}}T$；$1 - z = \frac12(k_{\mathrm{B}}T/F\ell_{\mathrm{p}})^{1/2}$；Marko–Siggia | 式 (21.11)–(21.12)、公式 21.3.2 |
| 排除体积 | $R \propto N^{\nu}$：$\nu = 1/2$ 理想链，$0.588$ 良溶剂，$1/3$ 致密球 | 定义 21.4.1、命题 21.4.1 |
| 成环 | $J = P(\boldsymbol{0})/N_{\mathrm{A}}$；圆模型最优值 $13\ell_{\mathrm{p}}$；蠕虫链最优值 $\approx 550\,\mathrm{bp}$，$J \approx 100\,\mathrm{nM}$；10.5 bp 周期的相位效应 | 定义 21.5.1、命题 21.5.1、式 (21.18) |
| 染色体 | 自由线团会重叠（疆域需要拴系或历史）；$P(s) \propto s^{-3\nu}$：理想链 $s^{-3/2}$，分形球 $s^{-1}$，人的 Hi-C $s^{-1.08}$ | 例 21.6.1、命题 21.6.1、定义 21.6.2 |
| 噬菌体包装 | 弯曲加水合排斥；$d_{\mathrm{s}} \to 2.5\,\mathrm{nm}$，几十 pN 的力，几十个大气压的压强 | 公式 21.7.1 |
| 核小体 | 弯曲 $\approx 70\,k_{\mathrm{B}}T$，净缠绕为每 bp 零点几个 $k_{\mathrm{B}}T$；位点暴露 $K_0\mathrm{e}^{-gx}$ | 式 (21.21)、命题 21.7.1 |

关于 DNA 要记住的数：每 bp $0.34\,\mathrm{nm}$，$\ell_{\mathrm{p}} = 50\,\mathrm{nm} = 150\,\mathrm{bp}$，$b = 100\,\mathrm{nm}$，$k_{\mathrm{B}}T/\ell_{\mathrm{p}} \approx 0.08\,\mathrm{pN}$（DNA 开始被拉直的力标度），把长度 $L$ 弯成整圆的代价以 $k_{\mathrm{B}}T$ 为单位是 $3000/N_{\mathrm{bp}}$。

## 思考题

1. 一个蛋白质被变性为 200 个残基的链，Kuhn 长度为 $0.8\,\mathrm{nm}$，每个残基 $0.38\,\mathrm{nm}$。分别按理想链和用 $R_{\mathrm{g}} \approx 0.2\,\mathrm{nm}\times N^{0.59}$ 的自回避链估算其回转半径，并与折叠的蛋白质（$R_{\mathrm{g}} \approx 0.22\,\mathrm{nm}\times N^{0.38}$）比较。

   **答** 轮廓长度 $L = 76\,\mathrm{nm}$，理想链 $R_{\mathrm{g}} = \sqrt{Lb/6} = \sqrt{76\times0.8/6} = 3.2\,\mathrm{nm}$。自回避：$200^{0.59} = 22.8$，$R_{\mathrm{g}} \approx 4.6\,\mathrm{nm}$。折叠：$200^{0.38} = 7.5$，$R_{\mathrm{g}} \approx 1.7\,\mathrm{nm}$。良溶剂（尿素、胍盐）中的变性链因排除体积而溶胀到大于理想链，并且约为天然蛋白质的 2.7 倍，这正是 SAXS 在解折叠时所测得的。

2. 证明 λ DNA 的熵弹簧劲度约为 $7\,\mathrm{fN}\,\mu\mathrm{m}^{-1}$，并估算其端到端距离沿一个轴的均方根热涨落。为什么需要至少 $0.1\,\mathrm{pN}$ 的拉力才能得到明确的伸长？

   **答** $k = 3k_{\mathrm{B}}T/(Lb) = 3\times4.1/(1.65\times10^4\times100)\,\mathrm{pN\,nm^{-1}} = 7.5\times10^{-6}\,\mathrm{pN\,nm^{-1}} = 7.5\,\mathrm{fN}\,\mu\mathrm{m}^{-1}$。由均分，$\langle x^2\rangle = k_{\mathrm{B}}T/k = Lb/3$，所以 $\sigma_x = \sqrt{1.65\times10^4\times100/3}\,\mathrm{nm} \approx 0.74\,\mu\mathrm{m}$。力必须使链的伸长远大于此，也就是进入 $Fb \gtrsim k_{\mathrm{B}}T$、$F \gtrsim 0.04\,\mathrm{pN}$ 的非线性区；在 $0.1\,\mathrm{pN}$ 时蠕虫链的伸长约为 $L$ 的 53 %（公式 21.3.2），涨落只是其一部分。

3. 由公式 21.3.2，要把 DNA 拉伸到其轮廓长度的 90 % 需要多大的力？与 $b = 100\,\mathrm{nm}$ 的自由连接链的预言比较。

   **答** 取 $z = 0.9$：$F\ell_{\mathrm{p}}/k_{\mathrm{B}}T = 0.9 + 1/(4\times0.01) - 0.25 = 25.65$，$F = 25.65\times4.1/50 \approx 2.1\,\mathrm{pN}$。对自由连接链，$\mathcal{L}(u) = 0.9$ 要求 $u \approx 10$，$F = 10k_{\mathrm{B}}T/b \approx 0.41\,\mathrm{pN}$。自由连接链达到高伸长所需的力只有约五分之一，因为它缺少只有大力才能抑制的短波长起伏。

4. 推导式 (21.10) $b = 2\ell_{\mathrm{p}}$，并解释为什么 Kuhn 长度比持久长度长。

   **答** 对 $L \gg \ell_{\mathrm{p}}$，式 (21.8) 给出 $\langle R^2\rangle \to 2\ell_{\mathrm{p}}L$，而定义 21.1.2 给出 $b = \langle R^2\rangle/L = 2\ell_{\mathrm{p}}$。持久长度是从一点出发、沿一个方向的相关衰减长度；一个 Kuhn 链段必须取代两侧相关的各段，而 $\mathrm{e}^{-\lvert s\rvert/\ell_{\mathrm{p}}}$ 对所有 $s$ 的积分是 $2\ell_{\mathrm{p}}$。

5. 一个阻遏蛋白以 $K_{\mathrm{d}} = 10\,\mathrm{nM}$ 结合一个辅助操纵序列。用式 (21.18)，裸 DNA 的哪些环长使成环相对于未成环的单结合状态占优？体内 92 bp 的 lac O1–O3 环产生很强的阻遏，这意味着什么？

   **答** 当 $J > K_{\mathrm{d}} = 10\,\mathrm{nM}$ 时成环占优。解式 (21.18)，$J = 10\,\mathrm{nM}$ 在短的一侧出现于 $n \approx 0.78$（约 230 bp），在长的一侧出现于 $n \approx 14$（约 4 kb），最大值约 100 nM，在 550 bp 附近；在这两个长度之间，成环状态占优。在 92 bp（$n = 0.31$）时，裸 DNA 的值带有因子 $\mathrm{e}^{-2.66/0.31^2} \approx 10^{-12}$，可以忽略。因此体内很强的 O1–O3 环需要帮助：HU 与 IHF 的弯曲、超螺旋以及阻遏蛋白四聚体的柔性，使体内的 J 因子比裸 DNA 值高出许多个数量级。

6. 证明 $N$ 步的一维随机行走回到原点的概率约为 $\sqrt{2/(\pi N)}$，并解释为什么三维中的环化随长度下降得更快。

   **答** 回到原点要求每个方向各走 $N/2$ 步：$\binom{N}{N/2}2^{-N}$。由 Stirling 公式 $n! \approx \sqrt{2\pi n}(n/\mathrm{e})^n$，$\binom{N}{N/2} \approx 2^N\sqrt{2/(\pi N)}$。在 $d$ 维中，原点处的端到端密度按 $\langle R^2\rangle^{-d/2} \propto N^{-d/2}$ 标度，因为两端扩散到体积 $R^d$ 中；三维中为 $N^{-3/2}$。

7. 用 Flory 论证求 $d$ 维中的指数 $\nu$，并对 $d = 1, 2, 3, 4$ 求值。$d = 4$ 的结果说明什么？

   **答** $F/k_{\mathrm{B}}T \sim R^2/(Nb^2) + vN^2/R^d$；最小化得 $R^{d+2} \propto N^3$，$\nu = 3/(d + 2)$：一维为 $1$（精确：直线上的自回避行走是直的），二维为 $3/4$（精确），三维为 $3/5$（精确值 $0.588$），四维为 $1/2$。在四维以上达到理想值 $1/2$：随机行走在高维中很少与自身相交，所以排除体积变得无关紧要（四是上临界维数）。

8. 在酵母的细胞核中（例 21.6.1），染色质的 Kuhn 长度与堆积密度取什么值，才会使一条自由染色体的线团与细胞核一样致密？这合理吗？

   **答** 要求对 $N_{\mathrm{bp}} = 750\,\mathrm{kb}$，$N_{\mathrm{bp}}/(\frac43\pi R_{\mathrm{g}}^3) = 3\,\mathrm{Mb}\,\mu\mathrm{m}^{-3}$，即 $R_{\mathrm{g}} \approx 0.39\,\mu\mathrm{m}$，$R_{\mathrm{g}}^2 = N_{\mathrm{bp}}b/(6\nu_{\ell}) = 0.15\,\mu\mathrm{m}^2$，所以 $b/\nu_{\ell} \approx 1.2\,\mathrm{nm^2\,bp^{-1}}$。核小体纤维的 $b/\nu_{\ell} \approx 60/8 = 7.5\,\mathrm{nm^2\,bp^{-1}}$；即使 30 nm 纤维（$400/100 = 4$）也太硬或太伸展。染色体需要比任何自由纤维都致密几倍，这支持由限制导致的重叠或特异的压缩（环、拴系），而不是自由线团。

9. （设计）你想检验一个使 DNA 弯曲的蛋白质是否促进成环。提出一个环化或系链粒子实验，说明所用的 DNA 长度与预期的特征。

   **答** 制备 100–600 bp 带黏性末端的片段，用连接酶依赖的环化相对于二聚化来测量 J，分别在有蛋白质与没有蛋白质时进行（或用末端染料之间的单分子 FRET，或用成环蛋白做系链粒子运动实验）。选取在蠕虫链最优值（150–300 bp）附近及以下的长度，并以单个碱基对为步长改变长度来探测螺旋相位。弯曲蛋白应当在短长度处（弯曲占主导）使 J 提高最多，使最优值移向更短的环，若它引入了柔性，则会减弱相位振荡；在长度为几 kb 时，J 由熵决定，它应当几乎没有影响。对照：尺寸相近的不弯曲 DNA 结合蛋白，以及在没有蛋白质时对照式 (21.18) 测量 J。

10. 估算缠绕在核小体中的 DNA 每个碱基对的弯曲能与总弯曲能，并在 $g = 0.15\,k_{\mathrm{B}}T$ 每 bp、$K_0 = 0.1$ 时求暴露核小体内 40 bp 处一个位点的平衡常数。对裸 DNA 的 $K_{\mathrm{d}} = 1\,\mathrm{nM}$ 的转录因子，要使该位点一半时间被占据，浓度需要提高多少倍？

    **答** 每 bp：$\ell_{\mathrm{p}}\times0.34\,\mathrm{nm}/(2R^2) = 50\times0.34/(2\times17.6) = 0.48\,k_{\mathrm{B}}T$；147 bp 约 $71\,k_{\mathrm{B}}T$。$K_{\mathrm{exp}} = 0.1\,\mathrm{e}^{-6} = 2.5\times10^{-4}$。半占据需要 $c = K_{\mathrm{d}}/K_{\mathrm{exp}} = 4\,\mu\mathrm{M}$，是裸 DNA 的 4000 倍，除非有另一个因子或重塑因子把 DNA 解开。

11. 用公式 21.7.1 定性解释为什么抵抗包装的力只在填充的最后三分之一急剧上升，以及增大 $\ce{Mg^2+}$ 的浓度（它降低 $F_0$，并可使包装好的 DNA 相互吸引）会如何改变这个力。

    **答** 包装早期，DNA 堆积松散（$d_{\mathrm{s}} \approx 4\,\mathrm{nm}$）：排斥按 $\mathrm{e}^{-d_{\mathrm{s}}/c}$（$c = 0.27\,\mathrm{nm}$）衰减，可以忽略，外层的环半径大，所以每增加单位长度的弯曲能很小。随着线轴被填满，内半径缩小（每个环的弯曲代价 $\propto 1/R_i$），间距必须降向 $2.5\,\mathrm{nm}$，而指数形式的排斥每减小 $0.27\,\mathrm{nm}$ 就增大一个因子 $\mathrm{e}$，所以力急剧增长。较低的 $F_0$（更多的 $\ce{Mg^2+}$ 或多胺）降低相互作用项，从而降低力与内压；若出现净吸引，DNA 就会凝聚，马达主要对抗弯曲。实验确实表明，在多价离子存在下阻力较低，注入较慢。
