---
title: 真实气体与输运过程
---

上一章的**理想气体**有两个理想化：分子没有大小，分子之间除碰撞外没有作用。本章去掉这两个理想化，在两个方向上走出理想气体。一是**平衡态**的**物态方程**：高压、低温下分子的体积与分子间的引力不可忽略，气体会偏离 $pV = nRT$，并最终液化；van der Waals 方程用两个参数同时描述了这种偏离、液化与临界点。二是非平衡态：分子有大小才会相互碰撞，碰撞决定了平均自由程，进而决定了热传导、黏滞与扩散这三种输运过程的快慢。输运过程的宏观规律（Fourier 定律、Fick 定律）是偏微分方程课程中热方程的物理来源（[2.5.1](/2.5.1)），这里从分子运动论求出其中的系数。下一章 [5.2.3](/5.2.3) 回到平衡态，转向热力学的方法。

## 2.1. 真实气体的等温线

在常温常压下，实际气体近似满足理想气体物态方程；压强很高或**温度**很低时，偏离变得显著。1869 年 Andrews 测量了 $\ce{CO2}$ 在不同温度下的等温线（$p$–$V_{\mathrm{m}}$ 曲线），揭示了气液转变的全貌：

- 温度较高（如 $48.1\,{}^\circ\mathrm{C}$）时，等温线接近理想气体的双曲线，无论怎样压缩都不会液化。
- 温度较低（如 $13\,{}^\circ\mathrm{C}$、$21\,{}^\circ\mathrm{C}$）时，等温压缩到某一体积，气体开始液化；继续压缩，压强保持不变，液体越来越多，直到全部液化；此后体积几乎不随压强变化（液体难以压缩）。等温线中的水平段对应汽液共存。
- 温度升高，水平段缩短；在 $31.1\,{}^\circ\mathrm{C}$ 的等温线上，水平段缩成一点，称为临界点。

**定义 2.1.1** 等温线上水平段缩成一点的状态称为**临界点**，这条等温线称为临界等温线，它的温度 $T_{\mathrm{c}}$ 称为**临界温度**，临界点的压强 $p_{\mathrm{c}}$ 与摩尔体积 $V_{\mathrm{m,c}}$ 称为临界压强与临界摩尔体积。汽液共存时的压强称为该温度下的**饱和蒸气压**。

$\ce{CO2}$ 的临界参量为 $T_{\mathrm{c}} \approx 304.1\,\mathrm{K}$（$31.0\,{}^\circ\mathrm{C}$）、$p_{\mathrm{c}} \approx 7.38\,\mathrm{MPa}$、$V_{\mathrm{m,c}} \approx 94\,\mathrm{cm^3\,mol^{-1}}$。在临界点，液体与气体的摩尔体积相同，二者不再有区别；在临界点附近，密度**涨落**变得很大，散射光使物质呈乳白色（临界乳光）。

$p$–$V_{\mathrm{m}}$ 图按状态分为四个区域：

| 区域 | 位置 | 性质 |
|---|---|---|
| 气态 | 临界等温线以上 | 只靠等温压缩不能液化 |
| 汽态 | 临界等温线以下、共存区右侧 | 等温压缩可以液化（"汽"即可液化的气） |
| 汽液共存 | 钟形的共存区内 | 压强等于饱和蒸气压，只与温度有关，与体积无关 |
| 液态 | 共存区左侧 | 几乎不可压缩 |

饱和蒸气压随温度升高而增大。液体在加热时，当它的饱和蒸气压等于外界压强时，液体内部也能形成气泡，即沸腾；因此外界压强越高，沸点越高。在 $101.325\,\mathrm{kPa}$ 下恒压加热水：水温升高到 $100\,{}^\circ\mathrm{C}$（严格地说是 $99.97\,{}^\circ\mathrm{C}$）时开始沸腾；继续加热，温度不变，水吸收汽化热，直到全部变成水蒸气；此后水蒸气的温度才继续升高。在高原上外界气压低，水不到 $100\,{}^\circ\mathrm{C}$ 就沸腾，温度升不上去；高压锅提高锅内压强，从而提高沸点。

临界温度高于室温的气体（$\ce{CO2}$、$\ce{NH3}$）在室温下加压即可液化；临界温度很低的气体（$\ce{O2}$ 为 $155\,\mathrm{K}$，$\ce{N2}$ 为 $126\,\mathrm{K}$）必须先降温到临界温度以下才能液化，这类气体曾被称为"永久气体"。最难液化的是氦（$T_{\mathrm{c}} \approx 5.2\,\mathrm{K}$），1908 年 Kamerlingh Onnes 首先把它液化，并在 1911 年用液氦冷却汞时发现了超导电性：低温技术的突破带来了新的物理。

## 2.2. van der Waals 方程

### 2.2.1. 分子间的作用力

分子之间的作用力本质上是电磁力，形式复杂，但总的特点是"远引近斥"：

- 分子间距 $r$ 大于有效作用距离 $s$（约 $10^{-9}\,\mathrm{m}$，几个到十个分子直径）时，作用力可以忽略；
- $r$ 较小时表现为引力；
- 在平衡距离 $r_0$（与分子的有效直径 $d \sim 10^{-10}\,\mathrm{m}$ 同数量级）处合力为零；
- $r < r_0$ 时斥力随距离减小而急剧增大。

常用的模型是 Lennard-Jones 势
$$
E_{\mathrm{p}}(r) = E_0\left[\left(\frac{r_0}{r}\right)^{12} - 2\left(\frac{r_0}{r}\right)^6\right],
$$
其中 $r^{-6}$ 项是分子的瞬时偶极与诱导偶极之间的**色散**引力，$r^{-12}$ 项是电子云重叠产生的斥力的经验写法。**势能**在平衡距离 $r_0$ 处取极小值 $-E_0$，力 $F = -\mathrm{d}E_{\mathrm{p}}/\mathrm{d}r$ 在此为零（**势能曲线**与力的关系见 [5.1.4](/5.1.4)）。

![Intermolecular potential and force: Lennard-Jones model (left) and the attracting hard-sphere model used by van der Waals (right)](./plots/lennard-jones.py)

### 2.2.2. van der Waals 气体模型

van der Waals（1873）对理想气体模型做两点修正，得到有引力的刚球模型（右图）：

1. 分子是直径为 $d$ 的刚球（考虑分子的体积）；
2. 在 $d < r < s$ 的范围内，分子之间有恒定的引力（考虑分子间的引力）。

### 2.2.3. van der Waals 方程

先考虑 $1\,\mathrm{mol}$ 气体，$p$ 为实测压强，$V_{\mathrm{m}}$ 为容器的容积。

体积修正：分子有大小，每个分子能自由活动的空间小于 $V_{\mathrm{m}}$，设为 $V_{\mathrm{m}} - b$，于是 $p = \frac{RT}{V_{\mathrm{m}} - b}$。常量 $b$ 与分子自身的体积有关：两个刚球中心的距离不能小于 $d$，一对分子互相排斥的体积是半径为 $d$ 的球，由此可得 $b = 4N_{\mathrm{A}} \cdot \frac{\pi d^3}{6}$，即 $1\,\mathrm{mol}$ 分子自身体积的 4 倍。

引力修正：容器内部的分子受周围分子的引力，各方向抵消；靠近器壁（距离小于 $s$）的分子受到指向内部的净引力，碰壁时的**动量**减小，实测压强比 $\frac{RT}{V_{\mathrm{m}} - b}$ 小一个内压强 $p_{\mathrm{in}}$。$p_{\mathrm{in}}$ 既正比于单位时间碰壁的分子数，又正比于每个分子受到的净引力，二者都正比于数密度，所以 $p_{\mathrm{in}} \propto n_V^2 \propto 1/V_{\mathrm{m}}^2$，记为 $p_{\mathrm{in}} = a/V_{\mathrm{m}}^2$。

**定义 2.2.1（van der Waals 方程）** 物态方程
$$
\left(p + \frac{a}{V_{\mathrm{m}}^2}\right)(V_{\mathrm{m}} - b) = RT
\tag{2.1}
$$
称为 **van der Waals 方程**；对物质的量为 $n$、体积为 $V$ 的气体，它写成 $\left(p + \frac{n^2a}{V^2}\right)(V - nb) = nRT$。其中常量 $a$（与分子间引力有关）和 $b$（与分子体积有关）因气体而异，由实验确定。满足它的气体称为 van der Waals 气体。

常温常压下 $b/V_{\mathrm{m}}$ 与 $p_{\mathrm{in}}/p$ 都只有 $10^{-3}$ 量级，两项修正可以忽略，方程回到理想气体。下表是 $\ce{N2}$ 在 $273\,\mathrm{K}$ 的实验数据（$RT \approx 2271\,\mathrm{J\,mol^{-1}}$）：

| $p/\mathrm{MPa}$ | $V_{\mathrm{m}}/(\mathrm{L\,mol^{-1}})$ | $pV_{\mathrm{m}}/(\mathrm{J\,mol^{-1}})$ | $(p + a/V_{\mathrm{m}}^2)(V_{\mathrm{m}} - b)/(\mathrm{J\,mol^{-1}})$ |
|---|---|---|---|
| 0.101 | 22.41 | 2271 | 2271 |
| 10.13 | 0.2224 | 2253 | 2254 |
| 50.66 | 0.06235 | 3159 | 2285 |
| 91.19 | 0.04825 | 4400 | 2265 |

最后一列取 $a = 0.079\,\mathrm{Pa\,m^6\,mol^{-2}}$、$b = 3.0 \times 10^{-5}\,\mathrm{m^3\,mol^{-1}}$（按这组数据拟合）。在 $900$ 个大气压下 $pV_{\mathrm{m}}$ 已比 $RT$ 大近一倍，van der Waals 方程仍与 $RT$ 相差不到 $1\%$。但 $a$、$b$ 的最佳值依赖于拟合的范围：由临界参量定出的值（$\ce{N2}$ 为 $a \approx 0.137\,\mathrm{Pa\,m^6\,mol^{-2}}$，$b \approx 3.9 \times 10^{-5}\,\mathrm{m^3\,mol^{-1}}$）在这样的高压下就有百分之几十的偏差。van der Waals 方程的价值主要在于定性：它用最简单的物理模型同时给出了气液转变与临界点（§2.2.5）；定量计算多用位力展开或其他经验物态方程。

器壁分子对气体分子的吸引不影响压强：它使飞向器壁的分子加速、离开器壁的分子减速，这两部分**冲量**相互抵消；而且压强按定义就是气体作用在器壁上的力，器壁分子对气体的作用不在其中。

### 2.2.4. van der Waals 气体的内能

理想气体的**内能**只依赖温度：$U = \frac{i}{2}nRT$。van der Waals 气体的分子之间有引力，体积增大时内压强做负**功**，分子间势能增加。取 $V \to \infty$ 时势能为零，则
$$
E_{\mathrm{p}}(V) = -\int_V^{\infty} p_{\mathrm{in}}\,\mathrm{d}V' = -\int_V^{\infty}\frac{n^2a}{V'^2}\,\mathrm{d}V' = -\frac{n^2a}{V},
$$
$$
U = \frac{i}{2}nRT - \frac{n^2a}{V} = U(T, V).
$$
所以 van der Waals 气体向真空自由膨胀时（内能不变），温度会降低（[5.2.3](/5.2.3)）。

### 2.2.5. van der Waals 等温线

把式 (2.1) 展开为 $V_{\mathrm{m}}$ 的三次方程 $pV_{\mathrm{m}}^3 - (pb + RT)V_{\mathrm{m}}^2 + aV_{\mathrm{m}} - ab = 0$：温度高时只有一个实根，等温线单调；温度低时在一定压强范围内有三个实根，等温线出现一个"回弯"。三个根合而为一的温度就是临界温度：临界点是等温线的拐点，$\left(\frac{\partial p}{\partial V_{\mathrm{m}}}\right)_T = 0$、$\left(\frac{\partial^2 p}{\partial V_{\mathrm{m}}^2}\right)_T = 0$，由此解得

**公式 2.2.1**
$$
V_{\mathrm{m,c}} = 3b, \qquad T_{\mathrm{c}} = \frac{8a}{27Rb}, \qquad p_{\mathrm{c}} = \frac{a}{27b^2}, \qquad \frac{p_{\mathrm{c}}V_{\mathrm{m,c}}}{RT_{\mathrm{c}}} = \frac{3}{8}.
$$

实际气体的 $p_{\mathrm{c}}V_{\mathrm{m,c}}/(RT_{\mathrm{c}})$ 多在 $0.23$–$0.31$ 之间，比 $0.375$ 小，这又一次说明方程只是定性正确。用约化变量 $p_{\mathrm{r}} = p/p_{\mathrm{c}}$、$V_{\mathrm{r}} = V_{\mathrm{m}}/V_{\mathrm{m,c}}$、$T_{\mathrm{r}} = T/T_{\mathrm{c}}$，方程化为不含 $a$、$b$ 的形式
$$
\left(p_{\mathrm{r}} + \frac{3}{V_{\mathrm{r}}^2}\right)(3V_{\mathrm{r}} - 1) = 8T_{\mathrm{r}},
$$
即各种气体在相同的约化温度与约化压强下有相同的约化体积（对应态定律），这对实际气体近似成立。

![Van der Waals isotherms in reduced variables; below the critical temperature the horizontal line is drawn by the equal-area rule](./plots/van-der-waals-isotherms.py)

临界温度以下，van der Waals 等温线的回弯与实验的水平段不同。把实际的水平段画在回弯上（图中实线），它与等温线交于汽侧与液侧两点：

- 水平段右侧的大体积部分是汽态，左侧的小体积部分是液态，与实验一致；
- 回弯的极小点与极大点之间 $\left(\frac{\partial p}{\partial V}\right)_T > 0$：压强随体积增大而增大，任何微小的扰动都会被放大，这种状态是不稳定的，实际上不存在；
- 汽侧交点到极大点之间是过饱和蒸气（压强高于饱和蒸气压而未液化），液侧交点到极小点之间是过热液体（温度高于沸点而未沸腾）。它们是亚稳态：没有凝结核或气化核时可以存在一段时间，一旦有了扰动就迅速转为汽液共存。

水平段的高度（饱和蒸气压）由 Maxwell 等面积法则确定：水平线与回弯所围的上下两块面积相等（这等价于两相的化学势相等，属于物理化学的内容）。

亚稳态在粒子物理中有重要的应用。Wilson 云室中是过饱和蒸气，带电粒子使经过的气体电离，离子成为凝结核，留下一串雾滴；Glaser 的气泡室中是过热液体，粒子的径迹上产生一串气泡。拍下这些径迹，就可以研究粒子的种类、动量与相互作用。

## 2.3. 气体分子的平均自由程

分子的**速率**为每秒数百米，但气体的扩散却很慢（打开香水瓶，要过一会儿才能在远处闻到），原因是分子不断碰撞，每次碰撞都改变运动方向，走的是一条曲折的路。碰撞是使非平衡态趋于平衡态的根本原因。

**定义 2.3.1** 一个分子在单位时间内与其他分子碰撞的平均次数称为**平均碰撞频率** $\bar z$；分子在相邻两次碰撞之间飞行的平均路程称为**平均自由程** $\bar\lambda$。显然 $\bar\lambda = \bar v/\bar z$。

计算 $\bar z$ 的模型：只有一种分子，分子是直径为 $d$ 的刚球。先设其他分子都静止，被考察的分子以相对速率运动：中心位于以它的轨迹为轴、半径为 $d$ 的圆柱内的分子都会被它碰到。这个圆柱的截面积
$$
\sigma = \pi d^2
$$
称为碰撞截面（collision cross section）。单位时间内圆柱扫过的体积为 $\sigma\bar v_{\mathrm{rel}}$，其中 $\bar v_{\mathrm{rel}}$ 是分子间的平均相对速率，因此 $\bar z = \sigma\bar v_{\mathrm{rel}}n_V$。

其他分子实际上也在运动。两个分子**速度**之差 $\boldsymbol{v}_1 - \boldsymbol{v}_2$ 的每个分量是两个独立的 $\mathcal{N}(0, k_{\mathrm{B}}T/m)$ 之差，服从 $\mathcal{N}(0, 2k_{\mathrm{B}}T/m)$，所以**相对速度**也服从 Maxwell 分布，只是 $m$ 换成**约化质量** $m/2$：$\bar v_{\mathrm{rel}} = \sqrt{2}\,\bar v$。（课件中的直观说法是：两分子的速度夹角平均为 $90^\circ$，相对速率约为 $\sqrt{2}\,\bar v$。）于是

**公式 2.3.1**
$$
\bar z = \sqrt{2}\,\pi d^2\bar v\,n_V, \qquad \bar\lambda = \frac{\bar v}{\bar z} = \frac{1}{\sqrt{2}\,\pi d^2 n_V} = \frac{k_{\mathrm{B}}T}{\sqrt{2}\,\pi d^2 p}.
$$

温度一定时 $\bar\lambda \propto 1/p$：

| $p$ | $\bar\lambda$（空气，$273\,\mathrm{K}$） | 例子 |
|---|---|---|
| $101\,\mathrm{kPa}$ | $\sim 7 \times 10^{-8}\,\mathrm{m}$ | 地面大气 |
| $10^{-2}\,\mathrm{Pa}$ | $\sim 0.7\,\mathrm{m}$ | 白炽灯泡内 |
| $10^{-6}\,\mathrm{Pa}$ | $\sim 7\,\mathrm{km}$ | 几百公里高空 |

**例 2.3.1** 氧气分子的有效直径 $d \approx 3.6 \times 10^{-10}\,\mathrm{m}$，求 $T = 273\,\mathrm{K}$、$p = 101\,\mathrm{kPa}$ 时的 $\bar z$ 与 $\bar\lambda$。

解：$\bar v = \sqrt{8RT/(\pi M)} \approx 425\,\mathrm{m\,s^{-1}}$，$n_V = p/(k_{\mathrm{B}}T) \approx 2.69 \times 10^{25}\,\mathrm{m^{-3}}$，
$$
\bar z = \sqrt{2}\,\pi d^2\bar v\,n_V \approx 6.6 \times 10^9\,\mathrm{s^{-1}}, \qquad \bar\lambda = \bar v/\bar z \approx 6.5 \times 10^{-8}\,\mathrm{m}.
$$
平均自由程约为分子直径的 200 倍、分子间平均距离（$n_V^{-1/3} \approx 3.3 \times 10^{-9}\,\mathrm{m}$）的 20 倍；一个分子每秒碰撞约 $10^{10}$ 次。

**注 2.3.1** 自由程本身是随机的。分子每走过 $\mathrm{d}x$ 被碰撞的概率为 $\mathrm{d}x/\bar\lambda$，与已经走过的路程无关，所以自由程服从**指数分布**：自由程大于 $x$ 的概率为 $\mathrm{e}^{-x/\bar\lambda}$，均值为 $\bar\lambda$。这与放射性衰变的寿命分布是同一个数学结构。

## 2.4. 输运过程

系统各部分的温度、流速或密度不均匀时，系统处于非平衡态。不受外界干扰时，系统会自发地向均匀的平衡态过渡，在此过程中能量、动量或质量从一处迁移到另一处，这类过程称为输运过程（transport process）。三种基本的输运过程是：

| 过程 | 不均匀的量 | 被迁移的量 | 宏观规律 | 输运系数 |
|---|---|---|---|---|
| 热传导 | 温度 $T$ | 热运动能量 | **Fourier 定律** | 导热系数 $\kappa$ |
| 黏滞（内摩擦） | 定向流速 $u$ | 定向运动的动量 | Newton 黏滞定律 | 黏度 $\eta$ |
| 扩散 | 密度 $\rho$ | 质量 | **Fick 定律** | 扩散系数 $D$ |

在气体中，三种迁移都由分子的**热运动**与碰撞完成：分子从一处带着那里的能量、动量或质量飞到另一处，经过碰撞把它们交给当地的分子。非平衡态的一般理论至今没有完全建立，下面只用平均自由程作简化的估算。

### 2.4.1. 热传导

设气体的温度沿 $x$ 方向变化，$T = T(x)$。实验表明，在 $\mathrm{d}t$ 内通过垂直于 $x$ 轴的面元 $\mathrm{d}S$ 的热量为
$$
\delta Q = -\kappa\left(\frac{\mathrm{d}T}{\mathrm{d}x}\right)_{x_0}\mathrm{d}S\,\mathrm{d}t,
\tag{2.2}
$$
负号表示热量沿温度降低的方向传递，比例系数 $\kappa$ 称为导热系数（thermal conductivity），又称热导率，单位 $\mathrm{W\,m^{-1}\,K^{-1}}$。三维中热流密度为 $\boldsymbol{q} = -\kappa\nabla T$，这就是 **Fourier 定律**；它与能量守恒结合就得到**热方程** $\rho c\,\partial_t T = \kappa\Delta T$（[2.5.1](/2.5.1)），其中 $\kappa/(\rho c)$ 是热扩散率。气体的导热系数很小：空气约 $0.026\,\mathrm{W\,m^{-1}\,K^{-1}}$，各种气体在 $10^{-2}$–$10^{-1}$ 量级（轻的 $\ce{H2}$、$\ce{He}$ 最大），金属则为 $10^2$ 量级。

微观解释：为了只有热传导而没有扩散，$\mathrm{d}S$ 两侧在 $\mathrm{d}t$ 内交换的分子数必须相等，设为 $\mathrm{d}N$。左侧来的分子平均能量为 $\bar\varepsilon_1$，右侧来的为 $\bar\varepsilon_2$，则通过 $\mathrm{d}S$ 的净能量为 $\delta Q = (\bar\varepsilon_1 - \bar\varepsilon_2)\,\mathrm{d}N$。作以下简化：

1. 计算 $\mathrm{d}N$ 时忽略温度差异，设分子都以 $\bar v$ 运动，且沿 $\pm x$、$\pm y$、$\pm z$ 六个方向各占 $1/6$，于是 $\mathrm{d}N = \frac{1}{6}n_V\bar v\,\mathrm{d}S\,\mathrm{d}t$；
2. 分子穿过 $\mathrm{d}S$ 之前的最后一次碰撞发生在距 $\mathrm{d}S$ 为 $\bar\lambda$ 处，并在那次碰撞中获得当地的平均能量。

于是 $\bar\varepsilon_1 - \bar\varepsilon_2 = -\frac{\mathrm{d}\bar\varepsilon}{\mathrm{d}T}\left(\frac{\mathrm{d}T}{\mathrm{d}x}\right)_{x_0}\cdot 2\bar\lambda$。分子的 $\frac{\mathrm{d}\bar\varepsilon}{\mathrm{d}T} = mc_V$，$c_V$ 是气体的定容比热容（[5.2.3](/5.2.3)）。代入并记 $\rho = n_Vm$：
$$
\delta Q = -\frac{1}{3}\rho c_V\bar v\bar\lambda\left(\frac{\mathrm{d}T}{\mathrm{d}x}\right)_{x_0}\mathrm{d}S\,\mathrm{d}t.
$$

**公式 2.4.1** 与式 (2.2) 比较，
$$
\kappa = \frac{1}{3}\rho c_V\bar v\bar\lambda.
$$

由于 $\rho \propto n_V$、$\bar\lambda \propto 1/n_V$，$\kappa$ 与压强（密度）无关，只随温度增大（$\bar v \propto \sqrt{T}$）。直观上，压强降低时传递能量的分子少了，但每个分子一次飞得更远，两者恰好抵消。实验证实了 $\kappa$ 在相当大的压强范围内与压强无关。

压强低到一定程度后实验结果不同：$\kappa \propto p$。原因是 $\bar\lambda$ 不能超过容器的线度 $l$：当 $p$ 低于使 $\bar\lambda = l$ 的压强 $p_{\mathrm{c}} = \frac{k_{\mathrm{B}}T}{\sqrt{2}\,\pi d^2 l}$ 时，$\bar\lambda = l$ 不再变化，于是 $\kappa \propto \rho \propto p$。

**例 2.4.1（保温瓶）** 保温瓶胆夹层厚 $l = 5\,\mathrm{mm}$，要抽空到多大压强以下才能有效保温？

解：压强高于 $p_{\mathrm{c}}$ 时抽气并不减小导热；低于 $p_{\mathrm{c}}$ 后 $\kappa \propto p$，真空度越高，保温越好。取 $T = 350\,\mathrm{K}$、空气分子 $d \approx 3.3 \times 10^{-10}\,\mathrm{m}$，
$$
p_{\mathrm{c}} = \frac{k_{\mathrm{B}}T}{\sqrt{2}\,\pi d^2 l} \approx 2\,\mathrm{Pa},
$$
即约 $2 \times 10^{-5}$ 个大气压，夹层的压强要远低于这个值。

### 2.4.2. 黏滞

设气体沿 $x$ 方向定向流动，流速 $u(z)$ 随 $z$ 变化。相邻两层气体之间有一对大小相等、方向相反的切向力（内摩擦力），快的一层拖动慢的一层。实验表明，面积为 $\mathrm{d}S$ 的界面上的内摩擦力
$$
\mathrm{d}F = -\eta\frac{\mathrm{d}u}{\mathrm{d}z}\,\mathrm{d}S,
$$
称为 Newton 黏滞定律，$\eta$ 称为黏度（viscosity），又称动力黏度，单位 $\mathrm{Pa\,s}$。在分子图像中，内摩擦是定向动量的输运：分子从快层飞到慢层，带去较多的定向动量 $mu$，反之亦然。与热传导完全相同的论证（把每个分子携带的 $\bar\varepsilon$ 换成 $mu$）给出

**公式 2.4.2**
$$
\eta = \frac{1}{3}\rho\bar v\bar\lambda.
$$

$\eta$ 同样与压强无关、随温度升高而增大。这是 Maxwell 在 1860 年得到的意外预言（直觉以为稀薄气体的"黏性"更小），他随后用实验证实了它，成为气体动理论早期最有力的证据之一。注意液体的黏度随温度升高而减小，机制完全不同。

### 2.4.3. 扩散

设混合气体中某一组分的密度 $\rho$ 沿 $x$ 方向变化（总压强与温度均匀）。在 $\mathrm{d}t$ 内通过面元 $\mathrm{d}S$ 迁移的该组分质量为
$$
\mathrm{d}m = -D\frac{\mathrm{d}\rho}{\mathrm{d}x}\,\mathrm{d}S\,\mathrm{d}t,
$$
这就是 **Fick 定律**，$D$ 称为扩散系数，单位 $\mathrm{m^2\,s^{-1}}$。把携带的量换成质量 $m$，同样的论证给出

**公式 2.4.3**
$$
D = \frac{1}{3}\bar v\bar\lambda.
$$

$D \propto 1/p$、$D \propto T^{3/2}$。Fick 定律与质量守恒结合也得到热方程（扩散方程）；从微观看，扩散是分子的随机游走，均方**位移**随时间线性增长，$\overline{x^2} = 2Dt$。

三个输运系数之间有简单的关系 $\eta = \rho D$、$\kappa = \eta c_V$。平均自由程理论正确地给出了各系数对压强、温度的依赖，但数值系数只是近似：严格的理论（Chapman–Enskog）给出的 $\kappa/(\eta c_V)$ 对单原子气体约为 $2.5$，而不是 1，因为速率快的分子既飞得远又携带更多能量，简化模型忽略了这种关联。

## 思考题

1. 为什么降低压强在开始时不能减小气体的导热，而高真空却能很好地保温？
   提示：$\kappa = \frac{1}{3}\rho c_V\bar v\bar\lambda$ 中 $\rho\bar\lambda$ 与压强无关，直到 $\bar\lambda$ 达到容器线度（例 2.4.1）。
2. 液体与气体的黏度随温度的变化相反，为什么？
   提示：气体的内摩擦来自分子在层间的迁移，温度越高 $\bar v$ 越大；液体的内摩擦来自分子间的吸引，温度升高时分子更容易挣脱近邻。
