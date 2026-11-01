---
title: 随机动力学：主方程与噪声
description: 细胞内化学反应的概率描述：Poisson 过程与等待时间，化学主方程与倾向函数，用母函数精确求解的生灭过程，矩方程，双态启动子与作为机制指纹的 Fano 因子，蛋白质爆发与 Gamma 分布，Gillespie 算法，化学 Langevin 方程与线性噪声近似，噪声诱导的稳态间切换，以及由母函数导出的 Luria–Delbrück 分布。
source_hash: 0d814d548829
---

前面各章的速率方程把浓度当作时间的光滑函数。在细菌中，一个基因只有一两个拷贝，它的 mRNA 只有寥寥几个，许多调控因子也只有几十个；结合、转录、翻译、降解的每一个事件都是随机的碰撞，分子数在随机的时刻以 1 为单位跳变。于是在同一培养基中，两个遗传上完全相同的细胞也会不同，而这些差异携带着信息：它们的大小与统计性质反映产生它们的过程的速率和结构。本章发展小数目化学的数学。我们从最简单的随机过程，即独立事件的到达出发（32.1），写出反应分子的一般**主方程**（32.2），用母函数与矩方程求解可以精确求解的问题（32.2–32.4），转向精确模拟（32.5），以及数目适中时成立的 Gauss 近似（32.6），并用这些工具处理噪声诱导的稳态间切换，以及由涨落推断动力学（32.7），最后讨论经典的 Luria–Delbrück 分布（32.8）。

本章以若干其他章节为基础。一般的**主方程**、**Fokker–Planck 方程**、**首达时间**与 Kramers 速率已在 [7.6.5](/7.6.5#sec-5.5) 中引入；随机基因表达的生物学，包括电报模型的结果、蛋白质爆发、内在噪声与**外在噪声**以及三阶段噪声公式（[7.2.22](/7.2.22#sec-22.5)），属于分子生物学，这里推导并使用这些结果，而不再重述。分布与母函数来自[概率论](/3.1)，Markov 链来自 [3.5.9](/3.5.9)，**Gillespie 算法**的实现见 [4.4.7](/4.4.7)。反馈回路、开关与振子的确定性动力学是下一章 [7.6.33](/7.6.33) 的主题；噪声在网络中的传播与控制属于[系统生物学](/7.9)。

## 32.1. 小数目带来的随机性

### 32.1.1. 多小才算小

*E. coli* 细胞的体积约为 $1\,\mathrm{fL}$，所以每个细胞一个分子对应的浓度为 $1/(N_{\mathrm{A}} \times 10^{-15}\,\mathrm{L}) \approx 1.7\,\mathrm{nM}$（[7.6.20](/7.6.20)）。典型基因只有一两个拷贝，在 Taniguchi 等人（2010）的单分子普查中，大多数 *E. coli* 基因平均每个细胞不足一个 mRNA，蛋白质数在 $0.1$ 到 $10^4$ 之间。若分子彼此独立地产生与消失，数目 $N$ 的相对涨落为 $N^{-1/2}$ 量级：十个分子时为 $30\,\%$，一千个时为 $3\,\%$。细胞正是在这样的数目下做决定：是否表达某个**操纵子**，是否形成芽孢，是否裂解。

第一个直接的证明是 Elowitz、Levine、Siggia 与 Swain（2002）的双色实验：把驱动青色与黄色荧光蛋白的同一**启动子**的两个拷贝放在 *E. coli* 染色体上的等价位置。若没有随机性，每个细胞的青色与黄色应当相同；实际上细胞的颜色从绿到红不等，这是两个拷贝之间不相关的**内在噪声**叠加在对二者影响相同的**外在噪声**之上的标志（[7.2.22](/7.2.22#sec-22.5.4)）。要预测这样的变异，就需要用概率描述化学。

### 32.1.2. Poisson 过程

最简单的随机事件序列是事件以恒定速率独立发生的序列：组成型启动子的转录起始、稳定光源发出的光子、放射性核的衰变。

**定义 32.1.1（Poisson 过程）** 速率为 $\lambda$ 的 **Poisson 过程**是一个计数过程 $N(t)$（$[0, t]$ 内的事件数），满足 $N(0) = 0$，在不相交区间上的增量相互独立，并且在短区间 $\mathrm{d}t$ 内以概率 $\lambda\,\mathrm{d}t + o(\mathrm{d}t)$ 增加 1，以概率 $o(\mathrm{d}t)$ 增加多于 1。

**定理 32.1.1（Poisson 过程的计数与等待时间）** 对速率为 $\lambda$ 的 Poisson 过程：

1. $N(t)$ 服从均值为 $\lambda t$ 的 **Poisson 分布**，$\mathbb{P}(N(t) = n) = (\lambda t)^n\mathrm{e}^{-\lambda t}/n!$；
2. 相继事件之间的等待时间相互独立，服从速率为 $\lambda$ 的**指数分布**，$\mathbb{P}(\tau > t) = \mathrm{e}^{-\lambda t}$；
3. 第 $k$ 个事件的时间 $T_k$ 服从 **Gamma 分布** $\Gamma(k, \lambda)$，密度为 $\lambda(\lambda t)^{k-1}\mathrm{e}^{-\lambda t}/(k-1)!$，均值 $k/\lambda$，方差 $k/\lambda^2$。

**证明** 令 $p_n(t) = \mathbb{P}(N(t) = n)$。对最后一个区间 $\mathrm{d}t$ 取条件，得 $p_n(t + \mathrm{d}t) = p_n(t)(1 - \lambda\,\mathrm{d}t) + p_{n-1}(t)\lambda\,\mathrm{d}t$，故 $\mathrm{d}p_n/\mathrm{d}t = \lambda(p_{n-1} - p_n)$，其中 $p_{-1} \equiv 0$。乘以 $z^n$ 并求和，**概率母函数** $G(z, t) = \sum_n z^np_n(t)$（[3.1.11](/3.1.11)）满足 $\partial G/\partial t = \lambda(z - 1)G$，$G(z, 0) = 1$，所以 $G = \mathrm{e}^{\lambda t(z - 1)}$，这是均值为 $\lambda t$ 的 Poisson 分布的母函数。长为 $t$ 的区间内没有事件的概率是 $p_0(t) = \mathrm{e}^{-\lambda t}$；由增量的独立性，这在每个事件之后都成立，由此得 (2)。最后，$\mathbb{P}(T_k > t) = \mathbb{P}(N(t) < k) = \sum_{n<k}(\lambda t)^n\mathrm{e}^{-\lambda t}/n!$，对 $t$ 求导，和式相消，得到 (3) 中的 Gamma 密度。$\square$

指数等待时间是无记忆的：已经等了 $s$ 而没有事件，并不改变剩余等待的分布，$\mathbb{P}(\tau > s + t \mid \tau > s) = \mathrm{e}^{-\lambda t}$。下一个事件取决于隐藏的中间步骤的过程是有记忆的，这是涨落揭示机制的第一种方式。若每个事件需要 $k$ 个速率相同的连续步骤，等待时间服从 $\Gamma(k, \lambda)$，其变异系数的平方 $\operatorname{Var}(\tau)/\mathbb{E}[\tau]^2 = 1/k$ 恰好数出步骤的个数：这就是用来数分子马达循环中隐藏步骤的随机性参数（[7.6.27](/7.6.27)）。速率不等时，这个比值介于 $1/k$ 与 $1$ 之间，所以它的倒数是步骤数的下界。

![mRNA 的生灭过程（合成 k = 20，每个分子的降解 γ = 1；时间以 mRNA 寿命为单位），用 Gillespie 算法模拟。A：从没有 mRNA 开始的五条轨迹，精确均值 k(1 − e^{−γt})（深色线）及其周围一个标准差的带；由定理 32.2.1，任何时刻分布都是 Poisson 分布。B：长时间模拟得到的平稳分布（柱）与均值为 k/γ 的 Poisson 分布（点）；模拟的 Fano 因子为 0.99。C：相继合成事件之间的等待时间（橙色）服从速率为 k 的指数分布，每隔四个事件的等待时间（紫色）服从 Gamma 分布 Γ(4, k)，如定理 32.1.1](./plots/birth-death.py)

## 32.2. 化学主方程

### 32.2.1. 状态、反应与倾向函数

考虑体积 $V$ 的均匀混合体系中的 $S$ 种分子，**拷贝数**为 $\boldsymbol{n} = (n_1, \dots, n_S)$，以及 $R$ 个反应。反应 $j$ 使状态改变一个固定的向量 $\boldsymbol{\nu}_j$，它是**化学计量矩阵**的第 $j$ 列（对 $\ce{A + B -> C}$，$\boldsymbol{\nu} = (-1, -1, +1)$）。

**定义 32.2.1（倾向函数）** 反应 $j$ 的**倾向函数** $a_j(\boldsymbol{n})$ 定义如下：已知 $t$ 时刻的状态为 $\boldsymbol{n}$，则反应 $j$ 在 $[t, t + \mathrm{d}t)$ 内发生一次的概率为 $a_j(\boldsymbol{n})\,\mathrm{d}t$。

对基元反应，倾向函数由对反应物分子的不同组合计数得到，这是质量作用定律的随机形式：

| 反应 | 倾向 | 与确定性速率常数 $k$ 的关系 |
|---|---|---|
| $\varnothing \to \ce{A}$（合成） | $c$ | 速率 $k$ 的单位为 $\mathrm{M\,s^{-1}}$ 时 $c = kN_{\mathrm{A}}V$；以单位时间的分子数计，$c = k$ |
| $\ce{A} \to \cdots$（一级） | $c\,n_{\mathrm{A}}$ | $c = k$，与体积无关 |
| $\ce{A + B} \to \cdots$ | $c\,n_{\mathrm{A}}n_{\mathrm{B}}$ | $c = k/(N_{\mathrm{A}}V)$ |
| $\ce{2A} \to \cdots$ | $c\,n_{\mathrm{A}}(n_{\mathrm{A}} - 1)/2$ | 反应速率 $v = k[\ce{A}]^2$ 时 $c = 2k/(N_{\mathrm{A}}V)$ |

在 $V = 1\,\mathrm{fL}$ 中，双分子速率常数 $10^8\,\mathrm{M^{-1}\,s^{-1}}$（扩散限制，[7.6.5](/7.6.5#sec-5.2.3)）给出每对分子 $c = 0.17\,\mathrm{s^{-1}}$：单个转录因子仅靠三维扩散就能在约 $6\,\mathrm{s}$ 内找到单个位点。

**定义 32.2.2（化学主方程）** **化学主方程**是反应混合物拷贝数的概率 $P(\boldsymbol{n}, t)$ 所满足的主方程（[7.6.5](/7.6.5) 的定义 5.5.1）：
$$
\frac{\partial P(\boldsymbol{n}, t)}{\partial t} = \sum_{j=1}^{R}\Bigl[a_j(\boldsymbol{n} - \boldsymbol{\nu}_j)\,P(\boldsymbol{n} - \boldsymbol{\nu}_j, t) - a_j(\boldsymbol{n})\,P(\boldsymbol{n}, t)\Bigr]. \tag{32.1}
$$
第一项是由反应 $j$ 转变为 $\boldsymbol{n}$ 的那个状态流入 $\boldsymbol{n}$ 的流，第二项是反应 $j$ 使之流出 $\boldsymbol{n}$ 的流。

Gillespie（1992）由稀薄均匀的气体或溶液的物理推出式 (32.1)：当非反应性碰撞或扩散使分子混合得比反应快得多，以致分子在两次反应之间忘记了自己的位置时，它是精确的。扩散不够快时，如膜上的反应或梯度中的反应，必须把体积划分为若干隔室并允许分子在隔室间跳跃（反应–扩散主方程），于是出现 [7.6.36](/7.6.36) 的空间图案。

**注 32.2.1** 把式 (32.1) 乘以 $\boldsymbol{n}$ 并求和，得到均值的精确方程，
$$
\frac{\mathrm{d}\langle\boldsymbol{n}\rangle}{\mathrm{d}t} = \sum_j\boldsymbol{\nu}_j\,\langle a_j(\boldsymbol{n})\rangle .
$$
若所有倾向都是 $\boldsymbol{n}$ 的线性函数，则 $\langle a_j(\boldsymbol{n})\rangle = a_j(\langle\boldsymbol{n}\rangle)$，均值精确地满足确定性速率方程。对双分子反应，$\langle n_{\mathrm{A}}n_{\mathrm{B}}\rangle = \langle n_{\mathrm{A}}\rangle\langle n_{\mathrm{B}}\rangle + \operatorname{Cov}(n_{\mathrm{A}}, n_{\mathrm{B}})$：均值依赖于二阶矩，二阶矩依赖于三阶矩，这个层级不封闭。此时速率方程是浓度固定、体积趋于无穷的极限（Kurtz，1972），其中协方差比均值之积小一个 $1/V$ 量级的因子。

### 32.2.2. 生灭过程

最简单的化学主方程描述组成型基因的 mRNA：以恒定速率 $k$ 合成，每个分子以速率常数 $\gamma$ 降解。这是拷贝数 $m$ 上的**生灭过程**：
$$
\frac{\mathrm{d}P(m)}{\mathrm{d}t} = k\bigl[P(m - 1) - P(m)\bigr] + \gamma\bigl[(m + 1)P(m + 1) - mP(m)\bigr], \tag{32.2}
$$
其中 $P(-1) \equiv 0$。

**定理 32.2.1（生灭过程的解）** 从 $t = 0$ 时有 $m_0$ 个分子出发，式 (32.2) 的母函数为
$$
G(z, t) = \bigl[1 + (z - 1)\mathrm{e}^{-\gamma t}\bigr]^{m_0}\exp\Bigl[\frac{k}{\gamma}(z - 1)\bigl(1 - \mathrm{e}^{-\gamma t}\bigr)\Bigr]. \tag{32.3}
$$
分子数是两个独立部分之和：初始分子中的幸存者，服从 $m_0$ 次试验、存活概率 $\mathrm{e}^{-\gamma t}$ 的二项分布；以及 $t = 0$ 以来新合成的分子，服从均值为 $(k/\gamma)(1 - \mathrm{e}^{-\gamma t})$ 的 Poisson 分布。在稳态下 $m$ 服从均值为 $k/\gamma$ 的 Poisson 分布。

**证明** 把式 (32.2) 乘以 $z^m$ 并对 $m$ 求和，合成项给出 $k(z - 1)G$，降解项给出 $\gamma\sum_m[(m+1)P(m+1) - mP(m)]z^m = \gamma(1 - z)\,\partial G/\partial z$。因此
$$
\frac{\partial G}{\partial t} + \gamma(z - 1)\frac{\partial G}{\partial z} = k(z - 1)G,
$$
这是一阶线性偏微分方程。沿特征线 $\mathrm{d}z/\mathrm{d}t = \gamma(z - 1)$，即 $z - 1 = (z_0 - 1)\mathrm{e}^{\gamma t}$，方程变为 $\mathrm{d}\ln G/\mathrm{d}t = k(z_0 - 1)\mathrm{e}^{\gamma t}$，故 $\ln G = \ln G(z_0, 0) + (k/\gamma)(z_0 - 1)(\mathrm{e}^{\gamma t} - 1)$。以 $G(z_0, 0) = z_0^{m_0}$ 与 $z_0 - 1 = (z - 1)\mathrm{e}^{-\gamma t}$ 代入，即得式 (32.3)。第一个因子是 $\mathrm{Bin}(m_0, \mathrm{e}^{-\gamma t})$ 的母函数，第二个是 Poisson 分布的母函数，而母函数之积是独立随机变量之和的母函数。当 $t \to \infty$ 时第一个因子趋于 1。$\square$

平稳分布也无需母函数即可得到。生灭链没有环，所以在稳态下相邻状态之间的净流为零：$kP(m) = (m + 1)\gamma P(m + 1)$，从 $P(0)$ 起递推得 $P(m) = P(0)(k/\gamma)^m/m!$。同样的论证给出任何合成为 $f(m)$、降解为 $g(m)$ 的一维链的平稳分布，
$$
P(m) = P(0)\prod_{i=1}^{m}\frac{f(i - 1)}{g(i)}, \tag{32.4}
$$
我们在 32.6 与 32.7 中会用到它。

### 32.2.3. 矩方程与 Fano 因子

大多数主方程无法求解，但把方程乘以 $\boldsymbol{n}$ 的幂并求和，可以导出低阶矩的方程。对式 (32.2)，乘以 $m$ 与 $m^2$ 并移动求和指标，得
$$
\frac{\mathrm{d}\langle m\rangle}{\mathrm{d}t} = k - \gamma\langle m\rangle, \qquad \frac{\mathrm{d}\operatorname{Var}(m)}{\mathrm{d}t} = k + \gamma\langle m\rangle - 2\gamma\operatorname{Var}(m). \tag{32.5}
$$
方差方程有简单的解读：每个反应事件，无论合成还是降解，都使方差增加一个单位（源项 $k + \gamma\langle m\rangle$），而降解以速率 $\gamma$ 使偏差弛豫，使方差以速率 $2\gamma$ 减小。在稳态下 $\operatorname{Var}(m) = \langle m\rangle = k/\gamma$，**Fano 因子** $F = \operatorname{Var}/\langle m\rangle$（[7.2.22](/7.2.22#sec-22.5.2)）等于 1。实测的 mRNA 计数的 **Fano 因子**以特征性的方式偏离 1，本章其余部分在很大程度上就是在讨论这些偏离的含义。

**例 32.2.1** 典型的 *E. coli* 基因每分钟产生约 $10$ 个 mRNA，其 mRNA 的寿命略多于一分钟。式 (32.5) 给出每个细胞约 $10$ 个 mRNA 的稳态，标准差为 $\sqrt{10} \approx 3$，并以时间常数 $1/\gamma$（约 $1\,\mathrm{min}$）弛豫到该稳态。由于以约 $50\,\mathrm{nt\,s^{-1}}$ 延伸时，$1\,\mathrm{kb}$ 的基因需要 $20\,\mathrm{s}$，任何时刻约有三个聚合酶在转录这个基因。

## 32.3. 启动子状态与 Fano 指纹

### 32.3.1. 双态启动子

启动子在活跃态 A（以速率 $r$ 合成 mRNA）与失活态 I（沉默）之间切换，这就是 [7.2.22](/7.2.22#sec-22.5.2) 的电报模型。设激活（I $\to$ A）速率为 $k_+$，失活（A $\to$ I）速率为 $k_-$。状态现在是（启动子状态，$m$）这一对，方便起见把两个概率合成向量 $\boldsymbol{p}(m) = (p_{\mathrm{A}}(m), p_{\mathrm{I}}(m))^{\mathsf T}$（Sanchez 等，2011）。令
$$
K = \begin{bmatrix} -k_- & k_+ \\ k_- & -k_+ \end{bmatrix}, \qquad R = \begin{bmatrix} r & 0 \\ 0 & 0 \end{bmatrix}, \qquad \Gamma = \gamma I_2,
$$
主方程为
$$
\frac{\mathrm{d}\boldsymbol{p}(m)}{\mathrm{d}t} = (K - R - m\Gamma)\,\boldsymbol{p}(m) + R\,\boldsymbol{p}(m - 1) + (m + 1)\Gamma\,\boldsymbol{p}(m + 1). \tag{32.6}
$$
任何启动子结构都可以写成同样的形式：状态更多就扩大 $K$、$R$ 与 $\Gamma$，调控因子通过 $K$ 中的速率进入。

**定理 32.3.1（双态启动子的矩）** 在式 (32.6) 的稳态下，令 $\lambda = k_+ + k_-$，
$$
\langle m\rangle = \frac{r}{\gamma}\,\frac{k_+}{\lambda}, \qquad F = \frac{\operatorname{Var}(m)}{\langle m\rangle} = 1 + \frac{r\,k_-}{\lambda(\lambda + \gamma)}. \tag{32.7}
$$

**证明** 定义部分矩 $\boldsymbol{\mu}_j = \sum_m m^j\boldsymbol{p}(m)$ 与 $\boldsymbol{u} = (1, 1)$，则 $\langle m^j\rangle = \boldsymbol{u}\cdot\boldsymbol{\mu}_j$。把式 (32.6) 乘以 $1$、$m$ 与 $m^2$ 并求和，令时间导数为零，得
$$
K\boldsymbol{\mu}_0 = \boldsymbol{0}, \qquad (K - \Gamma)\boldsymbol{\mu}_1 + R\boldsymbol{\mu}_0 = \boldsymbol{0}, \qquad (K - 2\Gamma)\boldsymbol{\mu}_2 + (2R + \Gamma)\boldsymbol{\mu}_1 + R\boldsymbol{\mu}_0 = \boldsymbol{0}.
$$
第一个方程连同 $\boldsymbol{u}\cdot\boldsymbol{\mu}_0 = 1$ 给出占据概率 $\boldsymbol{\mu}_0 = (k_+, k_-)/\lambda$。由于 $\boldsymbol{u}K = \boldsymbol{0}$（$K$ 的各列之和为零），对第二个方程作用 $\boldsymbol{u}$，得 $\gamma\langle m\rangle = r\mu_{0,\mathrm{A}}$，即均值。它的 A 分量为 $-(k_- + \gamma)\mu_{1,\mathrm{A}} + k_+\mu_{1,\mathrm{I}} + rk_+/\lambda = 0$；利用 $\mu_{1,\mathrm{A}} + \mu_{1,\mathrm{I}} = \langle m\rangle$，得 $\mu_{1,\mathrm{A}} = (k_+\langle m\rangle + rk_+/\lambda)/(\lambda + \gamma)$。对第三个方程作用 $\boldsymbol{u}$，得 $2\gamma\langle m^2\rangle = 2r\mu_{1,\mathrm{A}} + \gamma\langle m\rangle + r\mu_{0,\mathrm{A}}$，即 $\langle m^2\rangle = \langle m\rangle + (r/\gamma)\mu_{1,\mathrm{A}}$。代入并利用 $r k_+/\lambda = \gamma\langle m\rangle$，
$$
\operatorname{Var}(m) = \langle m\rangle + \frac{r}{\gamma}\,\frac{k_+\langle m\rangle + \gamma\langle m\rangle}{\lambda + \gamma} - \langle m\rangle^2 = \langle m\rangle\Bigl[1 + \frac{r}{\gamma}\,\frac{k_+ + \gamma}{\lambda + \gamma} - \frac{r}{\gamma}\,\frac{k_+}{\lambda}\Bigr],
$$
方括号化简为 $1 + rk_-/(\lambda(\lambda + \gamma))$。$\square$

这就是 [7.2.22](/7.2.22#sec-22.5.2) 中引用的电报模型结果，现在得到了推导。推导表明了为什么矩是实用的工具：式 (32.6) 的完整分布是合流超几何函数（Peccoud 与 Ycart，1995），而实验最可靠地测得的前两阶矩只需要线性代数。

**例 32.3.1** Golding、Paulsson、Zawilski 与 Cox（2005）在单个 *E. coli* 细胞中追踪用 MS2–GFP 标记的 mRNA。被标记的转录本因结合的 MS2 蛋白而稳定，只通过稀释被去除，$\gamma = 0.014\,\mathrm{min^{-1}}$（寿命 $70\,\mathrm{min}$，即细胞周期）；启动子以 $k_+ = 0.03\,\mathrm{min^{-1}}$ 开启，以 $k_- = 0.2\,\mathrm{min^{-1}}$ 关闭，故有 $13\,\%$ 的时间处于活跃，每次约持续 $5\,\mathrm{min}$；均值为 $\langle m\rangle = 10$。于是 $r = \gamma\langle m\rangle\lambda/k_+ = 1.1\,\mathrm{min^{-1}}$，式 (32.7) 给出 $F = 1 + 1.1 \times 0.2/(0.23 \times 0.244) \approx 4.8$，与由计数方差得到的约 $4$ 的 Fano 因子接近。

### 32.3.2. 三种极限

双态启动子有三种区域，由切换速率相对于 $\gamma$ 与 $r$ 的大小决定（见下图 B 栏）。

| 区域 | 条件 | $m$ 的分布 | Fano 因子 |
|---|---|---|---|
| 快速切换 | $k_\pm \gg \gamma$，$rk_-/\lambda^2 \ll 1$ | 均值为 $(r/\gamma)k_+/\lambda$ 的 Poisson 分布：启动子被平均掉 | $\approx 1$ |
| 慢速切换 | $k_\pm \ll \gamma$ | 混合分布：以概率 $k_+/\lambda$ 为均值 $r/\gamma$ 的 Poisson 分布，否则为零 | $\approx 1 + (r/\gamma)k_-/\lambda$ |
| 爆发 | $k_- \gg k_+, \gamma$ | 爆发大小 $b = r/k_-$、频率 $k_+$ 的负二项分布 | $\approx 1 + b$ |

在慢速切换的极限下，$m$ 的分布是零膨胀的 Poisson 分布：
$$
P(0) = \frac{k_-}{\lambda} + \frac{k_+}{\lambda}\,\mathrm{e}^{-r/\gamma}, \qquad P(m) = \frac{k_+}{\lambda}\,\frac{(r/\gamma)^m\mathrm{e}^{-r/\gamma}}{m!}\quad (m \geq 1).
$$
由测得的这种形状的分布，可以直接从 Poisson 峰的位置和多出的零计数得到两个比值 $r/\gamma$ 与 $k_+/\lambda$。

Chong、Chen、Ge 与 Xie（2014）用这一思路找出 *E. coli* 中转录爆发的原因。转录使聚合酶前方的 DNA 过度缠绕、后方缠绕不足（[7.2.3](/7.2.3)）；在被锚定为拓扑封闭结构域的染色体中，正超螺旋会累积。拓扑异构酶 I 能高效地去除负超螺旋，但去除正超螺旋的 DNA 旋转酶很稀少，每个结构域约只有一个分子。在体外和细胞内的单分子实验中，随着正超螺旋的积累，来自某个结构域的转录停止，当一个旋转酶结合后才恢复：爆发基因的 ON 与 OFF 状态就是它所在结构域结合旋转酶与不结合旋转酶的状态。如双态模型所预言，提高旋转酶浓度使爆发频率增大。

### 32.3.3. 从噪声读出机制

基因表达的均值由速率之积决定；Fano 因子则取决于活性在时间上如何分布，均值相同的不同结构有不同的 Fano 因子（Sanchez 等，2011；Jones、Brewster 与 Phillips，2014）。在简单阻遏中，**阻遏物**以正比于其浓度的速率 $k_{\mathrm{on}}$ 结合操纵基因，并以速率 $k_{\mathrm{off}}$ 离开；操纵基因空闲时启动子活跃，所以 $k_- = k_{\mathrm{on}}$，$k_+ = k_{\mathrm{off}}$。表达相对于未被阻遏的启动子的倍数变化为 $\mathrm{FC} = k_{\mathrm{off}}/(k_{\mathrm{off}} + k_{\mathrm{on}})$，这正是 [7.2.11](/7.2.11) 热力学模型所预言的量。把 $\lambda = k_{\mathrm{off}}/\mathrm{FC}$ 与 $k_{\mathrm{on}} = k_{\mathrm{off}}(1 - \mathrm{FC})/\mathrm{FC}$ 代入式 (32.7)，

$$
F = 1 + \frac{r\,\mathrm{FC}(1 - \mathrm{FC})}{k_{\mathrm{off}} + \gamma\,\mathrm{FC}}. \tag{32.8}
$$
倍数变化固定时，噪声只通过 $k_{\mathrm{off}}$ 依赖于操纵基因：阻遏物很少离开的强操纵基因给出很长的沉默期和很大的 Fano 因子；阻遏物在不到一秒内就离开的弱操纵基因则给出近乎 Poisson 的表达。因此，测量不同阻遏物浓度下 mRNA 计数的均值与 Fano 因子，可以区分平衡测量无法区分的模型；未受调控的启动子残余的 Fano 因子略高于 1，主要被归因于细胞周期中基因拷贝数的加倍，而不是启动子动力学（Jones 等，2014）。

![Fano 因子作为启动子动力学的指纹。A：简单阻遏，mRNA 由空闲启动子以 r = 0.33 s⁻¹ 合成并以 γ = 0.011 s⁻¹ 降解：三种强度不同的 lac 操纵基因的 Fano 因子随倍数变化的曲线，阻遏物平均分别在 7 min（Oid）、2.4 min（O1）和 0.47 s（O3）后解离。线：式 (32.8)；点：O1 的 Gillespie 模拟。在平均表达相同时，强操纵基因产生长的沉默期和大的 Fano 因子；弱操纵基因给出近乎 Poisson 的统计。B：32.3.2 中三种区域下双态启动子的稳态分布（柱：模拟；点：极限分布）：快速切换（k₊ = k₋ = 50γ）给出 Poisson 分布，慢速切换（k₊ = k₋ = 0.02γ）给出近一半细胞为空的零膨胀 Poisson 分布，活跃期短（k₋ = 19k₊ = 38γ）给出负二项分布；三者的均值都接近 20](./plots/promoter-fano.py)

## 32.4. 爆发与 Gamma 分布

### 32.4.1. 一个 mRNA 产生的蛋白质

[7.2.22](/7.2.22#sec-22.5.3) 中的蛋白质爆发来自两个指数分布。一个 mRNA 存活的时间 $T$ 服从速率为 $\gamma_m$ 的指数分布；存活期间它以速率 $k_p$ 作为 Poisson 过程被翻译。给定 $T$，蛋白质数服从均值为 $k_pT$ 的 Poisson 分布；对 $T$ 求平均，
$$
\mathbb{P}(n) = \int_0^\infty\gamma_m\mathrm{e}^{-\gamma_m t}\,\frac{(k_pt)^n\mathrm{e}^{-k_pt}}{n!}\,\mathrm{d}t = \frac{\gamma_m}{k_p + \gamma_m}\Bigl(\frac{k_p}{k_p + \gamma_m}\Bigr)^n, \qquad n = 0, 1, 2, \dots,
$$
这是均值为 $b = k_p/\gamma_m$ 的**几何分布**，$b$ 即爆发大小。直观上这是一场竞赛：下一个事件以概率 $q = k_p/(k_p + \gamma_m)$ 是一次翻译，否则是 mRNA 的死亡，爆发在第一次死亡时结束。

### 32.4.2. 带跳跃的主方程

当 mRNA 的寿命比蛋白质短得多（$\gamma_m \gg \gamma_p$）时，每个 mRNA 可以用一次瞬时的爆发代替。于是蛋白质以速率 $k_m$（转录速率）成批到来，批的大小服从几何分布 $\mathbb{P}(j) = (1 - q)q^j$，并以速率常数 $\gamma_p$ 降解或被稀释：
$$
\frac{\partial P(n)}{\partial t} = \gamma_p\bigl[(n + 1)P(n + 1) - nP(n)\bigr] + k_m\sum_{j=0}^{n}(1 - q)q^j P(n - j) - k_mP(n). \tag{32.9}
$$

**定理 32.4.1（爆发式合成给出负二项分布）** 式 (32.9) 的稳态是**负二项分布**，其母函数为
$$
G(z) = \Bigl(\frac{1 - q}{1 - qz}\Bigr)^{a}, \qquad a = \frac{k_m}{\gamma_p}, \qquad \langle n\rangle = ab, \qquad F = 1 + b. \tag{32.10}
$$

**证明** 爆发大小的母函数为 $\sum_j(1 - q)q^jz^j = (1 - q)/(1 - qz)$，而式 (32.9) 中的和是卷积，其母函数是乘积。因此在稳态下 $0 = \gamma_p(1 - z)G'(z) + k_m[(1 - q)/(1 - qz) - 1]G(z)$。由于 $(1 - q)/(1 - qz) - 1 = -q(1 - z)/(1 - qz)$，因子 $(1 - z)$ 约去，$G'/G = aq/(1 - qz)$，所以 $\ln G = -a\ln(1 - qz) + C$，而 $G(1) = 1$ 定出 $C = a\ln(1 - q)$。均值为 $G'(1) = aq/(1 - q) = ab$，由 $G''(1) = a(a + 1)q^2/(1 - q)^2$ 得 $\operatorname{Var}(n) = ab(1 + b)$。$\square$

参数有直接的含义：$a$ 是每个蛋白质寿命内的爆发次数，$b$ 是每次爆发产生的蛋白质数。当蛋白质稳定、只通过稀释被去除时，$1/\gamma_p$ 是细胞周期除以 $\ln 2$，$a$ 约等于每个细胞周期中合成的 mRNA 数。

### 32.4.3. 连续极限与反馈

当 $b$ 很大时，蛋白质数可看作连续变量 $x$，它确定性地衰减，$\dot x = -\gamma_px$，并以速率 $k_m$ 跳跃，跳跃量服从均值为 $b$ 的指数分布（几何分布的连续版本）。Friedman、Cai 与 Xie（2006）写出了密度 $p(x, t)$ 的相应方程，
$$
\frac{\partial p}{\partial t} = \frac{\partial}{\partial x}\bigl[\gamma_p x\,p\bigr] + k_m\int_0^x w(x - x')\,p(x')\,\mathrm{d}x' - k_m\,p(x), \qquad w(y) = \frac{1}{b}\,\mathrm{e}^{-y/b}. \tag{32.11}
$$

**定理 32.4.2（爆发式表达的 Gamma 分布）** 式 (32.11) 的稳态是形状参数 $a = k_m/\gamma_p$、尺度参数 $b$ 的 Gamma 分布，
$$
p(x) = \frac{x^{a-1}\mathrm{e}^{-x/b}}{\Gamma(a)\,b^a}, \qquad \langle x\rangle = ab, \qquad \eta^2 = \frac{\operatorname{Var}(x)}{\langle x\rangle^2} = \frac{1}{a}. \tag{32.12}
$$
若爆发频率依赖于蛋白质水平，$k_m = k(x)$（如转录自调控），则稳态为
$$
p(x) = \frac{A}{x}\,\mathrm{e}^{-x/b}\exp\Bigl[\int^x\frac{k(x')}{\gamma_px'}\,\mathrm{d}x'\Bigr], \tag{32.13}
$$
其中 $A$ 由归一化确定。

**证明** 对常数 $k_m$，取 **Laplace 变换** $L(s) = \int_0^\infty\mathrm{e}^{-sx}p(x)\,\mathrm{d}x$。漂移项经分部积分变为 $-\gamma_psL'(s)$；卷积项变为 $k_mL(s)/(1 + bs)$，因为 $w$ 的变换是 $1/(1 + bs)$。稳态要求 $-\gamma_psL' - k_mbs\,L/(1 + bs) = 0$，故 $L'/L = -ab/(1 + bs)$，$L(s) = (1 + bs)^{-a}$，这是 Gamma 密度 (32.12) 的 Laplace 变换。对可变的 $k(x)$，把式 (32.11) 从 $0$ 到 $x$ 积分：稳态意味着穿过 $x$ 的向下概率流（由衰减产生，$\gamma_pxp(x)$）等于向上的概率流（由从 $x$ 以下开始、在 $x$ 以上结束的爆发产生，$\int_0^xk(x')p(x')\mathrm{e}^{-(x - x')/b}\,\mathrm{d}x'$）。把这个积分记为 $J(x)$，则 $J' = k(x)p(x) - J/b$，$J = \gamma_pxp$，所以 $J'/J = k(x)/(\gamma_px) - 1/b$；积分得 $J$，而 $p = J/(\gamma_px)$ 就是式 (32.13)。$\square$

对爆发频率的负自调控，$k(x) = k_0/(1 + (x/K)^h)$，积分是初等的，式 (32.13) 变为 $p(x) \propto x^{a_0 - 1}\mathrm{e}^{-x/b}(1 + (x/K)^h)^{-a_0/h}$，其中 $a_0 = k_0/\gamma_p$：反馈截断了分布的上尾（图 B 栏）。

### 32.4.4. 由分布推断

定理 32.4.2 把测得的稳态分布变成动力学参数：$b = \operatorname{Var}(x)/\langle x\rangle$，$a = \langle x\rangle^2/\operatorname{Var}(x)$。Cai、Friedman 与 Xie（2006）以及 Yu、Xiao、Ren、Lao 与 Xie（2006）通过逐个计数新合成的分子，直接测量了爆发的大小和频率，其值与对稳态水平拟合 Gamma 分布得到的值一致（[7.2.22](/7.2.22#sec-22.5.1)）。在 Taniguchi 等人（2010）的普查中，约 $1000$ 个 *E. coli* 基因中几乎所有基因的蛋白质分布都可用 Gamma 分布拟合；它们的噪声在低表达时遵循 $\eta^2 \propto 1/\langle n\rangle$，即式 (32.12) 的内在项，在高表达时趋于 $\eta^2 \approx 0.1$ 的下限，即所有基因共有的外在噪声。蛋白质分布是随机过程的时间平均，有了模型，它无需任何时间分辨的测量就能揭示动力学；没有模型，它什么也揭示不了，因为许多机制都产生类似 Gamma 的分布。

![蛋白质爆发与 Gamma 分布（时间以蛋白质寿命为单位）。A：频率 a = 3、几何分布大小均值 b = 8 的爆发，用 Gillespie 算法模拟（柱），对比定理 32.4.1 的负二项分布（点）及其连续极限，即定理 32.4.2 的 Gamma 分布（线）。B：爆发频率的负自调控 a(n) = a₀/(1 + (n/K)²)，a₀ = 10，b = 10，K = 30：模拟（柱）与 Friedman、Cai 和 Xie 的公式式 (32.13)（线）；虚线是无反馈时的分布。C：300 个模拟基因的噪声对均值，爆发大小与频率随机，每个细胞乘以一个所有基因共有的、变异系数平方为 0.1 的因子：低表达时 η² = (1 + b)/⟨n⟩（b = 1 与 30 的线），高表达时为外在噪声的下限（水平线），这两种区域都见于 *E. coli* 的普查](./plots/burst-gamma.py)

## 32.5. 精确模拟：Gillespie 算法

没有解析解时，可以对主方程进行精确抽样。Gillespie（1976, 1977）注意到，在状态 $\boldsymbol{n}$ 下，下一个反应的发生时间及其种类有简单的联合分布。令 $a_0 = \sum_ja_j(\boldsymbol{n})$。$[t, t + \tau)$ 内没有反应发生的概率满足 $P_0(\tau + \mathrm{d}\tau) = P_0(\tau)(1 - a_0\,\mathrm{d}\tau)$，故 $P_0(\tau) = \mathrm{e}^{-a_0\tau}$，下一个反应在 $t + \tau$ 发生且是反应 $j$ 的概率密度为
$$
p(\tau, j) = a_j\,\mathrm{e}^{-a_0\tau} = \underbrace{a_0\mathrm{e}^{-a_0\tau}}_{\text{when}}\cdot\underbrace{\frac{a_j}{a_0}}_{\text{which}}. \tag{32.14}
$$
两个因子相互独立：等待时间服从以总速率为参数的指数分布，而反应按其倾向的比例选取。

**算法 32.5.1（Gillespie 直接法）** 给定 $t = 0$ 时的初始状态 $\boldsymbol{n}$：

1. 计算所有倾向 $a_j(\boldsymbol{n})$ 及其和 $a_0$；若 $a_0 = 0$ 则停止。
2. 抽取两个独立的 $(0, 1)$ 均匀随机数 $u_1, u_2$。
3. 令 $\tau = \ln(1/u_1)/a_0$，这是速率为 $a_0$ 的指数随机数。
4. 选取反应 $j$，它是使 $\sum_{i \le j}a_i > u_2a_0$ 的最小指标。
5. 更新 $t \leftarrow t + \tau$ 与 $\boldsymbol{n} \leftarrow \boldsymbol{n} + \boldsymbol{\nu}_j$，记录，并回到第 1 步。

```python
import numpy as np

def gillespie(n0, nu, propensities, t_max, rng=np.random.default_rng()):
    """Exact stochastic simulation of a reaction network.

    n0: initial copy numbers (length S); nu: stoichiometric changes (R x S);
    propensities: function n -> array of R propensities.
    Returns the jump times and the states after each jump.
    """
    t, n = 0.0, np.array(n0, dtype=int)
    times, states = [t], [n.copy()]
    while t < t_max:
        a = propensities(n)
        a0 = a.sum()
        if a0 == 0:
            break
        t += rng.exponential(1.0 / a0)               # when: exponential with total rate
        j = np.searchsorted(np.cumsum(a), rng.random() * a0)   # which: in proportion to a_j
        n += nu[j]
        times.append(t)
        states.append(n.copy())
    return np.array(times), np.array(states)

# birth-death process of mRNA: production k, degradation gamma per molecule
k, gamma = 20.0, 1.0
nu = np.array([[1], [-1]])
times, states = gillespie([0], nu, lambda n: np.array([k, gamma * n[0]]), t_max=50.0)
```

每条轨迹是一个细胞可能的一段历史。对平稳态的平均，既可以对许多条轨迹取，也可以（对遍历系统）沿一条长轨迹按时间取，此时每个状态按停留的时间（等待时间 $\tau$）而不是访问次数加权。该算法是精确的，但每个反应事件要花一步，当某些组分丰富且频繁反应时，代价过高。有两类标准的改进：Gibson 与 Bruck（2000）的下一反应法，它只更新受每个反应影响的倾向，并用优先队列管理下一次的时间；以及 $\tau$ 跳跃（Gillespie，2001），它每次前进固定的区间 $\tau$，在其中每个反应 $j$ 触发的次数服从均值为 $a_j\tau$ 的 Poisson 分布，适用于在 $\tau$ 内没有倾向发生明显变化的情形。混合方法对丰富的组分用下一节的 **Langevin 方程**处理，对稀少的组分精确处理。直接法在 Python 中的性能，包括编译版本与并行版本，在 [4.4.7](/4.4.7#sec-7.3) 中测量。

## 32.6. 化学 Langevin 方程与线性噪声近似

### 32.6.1. 从跳跃到 Gauss 噪声

若在时间 $\mathrm{d}t$ 内每个反应都触发许多次，而倾向变化很小，则反应 $j$ 的触发次数服从均值 $a_j\,\mathrm{d}t$ 很大的 Poisson 分布，因而近似为同均值同方差的 Gauss 分布。把所有反应的变化相加，就得到一个随机微分方程。

**定义 32.6.1（化学 Langevin 方程）** 把拷贝数 $\boldsymbol{X}(t)$ 看作连续量，其**化学 Langevin 方程**为
$$
\mathrm{d}\boldsymbol{X} = \sum_{j=1}^{R}\boldsymbol{\nu}_j\,a_j(\boldsymbol{X})\,\mathrm{d}t + \sum_{j=1}^{R}\boldsymbol{\nu}_j\sqrt{a_j(\boldsymbol{X})}\,\mathrm{d}W_j(t), \tag{32.15}
$$
其中 $W_j$ 是相互独立的 Wiener 过程，每个反应一个（Gillespie，2000）。

漂移项就是确定性的速率方程；每个反应各自加入强度等于其倾向的**白噪声**。等价的 **Fokker–Planck 方程**（[7.6.5](/7.6.5) 的定义 5.5.2）的漂移为 $\boldsymbol{A}(\boldsymbol{x}) = \sum_j\boldsymbol{\nu}_ja_j$，扩散矩阵为 $B(\boldsymbol{x}) = \sum_j\boldsymbol{\nu}_j\boldsymbol{\nu}_j^{\mathsf T}a_j$；它是式 (32.1) 的 Kramers–Moyal 展开在二阶处截断的结果。式 (32.15) 是 Brown 运动的 **Langevin 方程**在化学中的对应，但有一个原则上的区别：噪声不是由外界以温度决定的强度加入的，而是由反应本身产生的，所以在反应停止的地方噪声消失，在系统更活跃的地方噪声更大。

### 32.6.2. 线性噪声近似

化学 Langevin 方程是非线性的，很少能求解，但在大体积下涨落比均值小得多，可以线性化。van Kampen 的系统尺度展开把 $\boldsymbol{n}$ 写成 $\boldsymbol{n} = \Omega\boldsymbol{\phi}(t) + \Omega^{1/2}\boldsymbol{\xi}$，其中 $\Omega$ 是体积（或典型拷贝数的任何度量），$\boldsymbol{\phi}$ 是浓度，$\boldsymbol{\xi}$ 是涨落，并按 $\Omega$ 的幂归并。在领头阶，$\boldsymbol{\phi}$ 服从速率方程；在次阶，$\boldsymbol{\xi}$ 服从线性 Langevin 方程，即多元 **Ornstein–Uhlenbeck 过程**。

**定义 32.6.2（线性噪声近似）** **线性噪声近似**把拷贝数在速率方程 $\dot{\boldsymbol{x}} = \sum_j\boldsymbol{\nu}_ja_j(\boldsymbol{x})$ 的稳定稳态 $\boldsymbol{x}^*$ 附近的涨落描述为均值为零的 Gauss 过程，其协方差矩阵 $C$ 满足
$$
\frac{\mathrm{d}C}{\mathrm{d}t} = JC + CJ^{\mathsf T} + D, \qquad J = \frac{\partial}{\partial\boldsymbol{x}}\sum_j\boldsymbol{\nu}_ja_j\Big|_{\boldsymbol{x}^*}, \qquad D = \sum_j\boldsymbol{\nu}_j\boldsymbol{\nu}_j^{\mathsf T}a_j(\boldsymbol{x}^*), \tag{32.16}
$$
稳态下满足 Lyapunov 方程 $JC + CJ^{\mathsf T} + D = 0$；平稳自协方差为 $\langle\delta\boldsymbol{x}(t + \tau)\,\delta\boldsymbol{x}(t)^{\mathsf T}\rangle = \mathrm{e}^{J\tau}C$（$\tau \geq 0$）。

式 (32.16) 是涨落被确定性弛豫耗散（$J$，在稳定状态下其特征值实部为负）与被反应产生（$D$）之间的平衡，是 [7.6.5](/7.6.5#sec-5.4) 的涨落–耗散关系在化学中的类比。对倾向为线性的网络，它对任意大小的体系的二阶矩都是精确的，因为此时矩的层级是封闭的（注 32.2.1）；[7.2.22](/7.2.22#sec-22.5) 中三阶段噪声公式的证明恰好就是求解这样一个 Lyapunov 方程。对非线性网络，它是对速率方程的第一个修正，在 $J$ 变为奇异的分岔点附近，以及分子只有几个拷贝时失效。

**例 32.6.1（mRNA 与蛋白质）** 设 mRNA $m$ 以速率 $k_m$ 合成、以 $\gamma_m$ 降解，蛋白质 $p$ 以速率 $k_pm$ 合成、以 $\gamma_p$ 降解。取 $\boldsymbol{x} = (m, p)$，
$$
J = \begin{bmatrix} -\gamma_m & 0 \\ k_p & -\gamma_p\end{bmatrix}, \qquad D = \begin{bmatrix} 2\gamma_m\langle m\rangle & 0 \\ 0 & 2\gamma_p\langle p\rangle\end{bmatrix},
$$
因为在稳态下每种组分的合成与降解速率相等。Lyapunov 方程的三个独立分量依次求解：$C_{mm} = \langle m\rangle$；$k_pC_{mm} - (\gamma_m + \gamma_p)C_{mp} = 0$，故 $C_{mp} = k_p\langle m\rangle/(\gamma_m + \gamma_p)$；$2k_pC_{mp} - 2\gamma_pC_{pp} + 2\gamma_p\langle p\rangle = 0$，故
$$
\frac{\operatorname{Var}(p)}{\langle p\rangle^2} = \frac{1}{\langle p\rangle} + \frac{1}{\langle m\rangle}\,\frac{\gamma_p}{\gamma_m + \gamma_p}, \qquad F_p = 1 + \frac{k_p}{\gamma_m + \gamma_p},
$$
这是 Thattai 与 van Oudenaarden（2001）的结果。当 $\gamma_m \gg \gamma_p$ 时 Fano 因子为 $1 + b$，与定理 32.4.1 一致。mRNA 与蛋白质的相关系数为 $C_{mp}/\sqrt{C_{mm}C_{pp}} = \sqrt{\gamma_p/(\gamma_m + \gamma_p)}\cdot\sqrt{b'/(1 + b')}$，其中 $b' = k_p/(\gamma_m + \gamma_p)$：mRNA 寿命短时，蛋白质水平与瞬时的 mRNA 水平相关性很差，因为蛋白质在其自身的寿命内对 mRNA 的历史进行积分。这是同一基因的单细胞 mRNA 与蛋白质计数相关性很弱的原因之一（Taniguchi 等，2010）。

### 32.6.3. 反馈与 Fano 因子

对以速率 $f(x)$ 合成、以 $\gamma x$ 降解的单一组分，式 (32.16) 中 $J = f'(x^*) - \gamma$，$D = f(x^*) + \gamma x^* = 2\gamma x^*$，所以
$$
F = \frac{\operatorname{Var}(x)}{x^*} = \frac{\gamma}{\gamma - f'(x^*)} = \frac{1}{1 + H}, \qquad H = -\frac{f'(x^*)}{\gamma}. \tag{32.17}
$$
无量纲增益 $H$ 是合成对水平的**对数灵敏度**，相对于清除的对数灵敏度而言。负自调控（$H > 0$）把噪声压低到 Poisson 水平以下；正自调控（$H < 0$）放大噪声，当 $H \to -1$，即稳态失去稳定性、体系成为双稳态的点（[7.6.33](/7.6.33)）时，方差与弛豫时间 $1/(\gamma(1 + H))$ 一起发散。大涨落与慢弛豫这两个特征都预告着分岔的临近。Becskei 与 Serrano（2000）在 *E. coli* 中观察到合成 TetR 回路的负自调控降低了细胞间的变异。蛋白质成批合成时噪声源更大，但式 (32.17) 的衰减因子对慢涨落同样适用；然而负反馈无法消除比它响应更快的噪声，Lestas、Vinnicombe 与 Paulsson（2010）证明，对源于少数分子的噪声，任何反馈能够抑制的程度都有信息论的下界。

![自调控基因的线性噪声近似，一条合成为 f(n)、降解为 n 的生灭链，其精确平稳分布为式 (32.4)。A：Fano 因子随确定性稳态处反馈增益 H = −f′(x*)/γ 的变化：点是精确值，负自调控 f = β/(1 + (n/20)⁴)，β 递增（H > 0），正自调控 f = 2 + β₁n/(40 + n)，β₁ 递增（H < 0）；线是线性噪声近似的预言 F = 1/(1 + H)，式 (32.17)。B：强负反馈（紫色，H = 3.9）与 H = −0.6 的正反馈（红色）的精确分布，以及同均值的 Poisson 分布（线）：负反馈使分布比 Poisson 宽度更窄，正反馈使之变宽](./plots/lna.py)

## 32.7. 稳态之间的切换

### 32.7.1. 双稳态加噪声

协同地激活自身转录的基因可以有两个稳定的稳态，关与开（[7.3.18](/7.3.18#sec-18.4.3) 的正反馈模块；确定性分析见 [7.6.33](/7.6.33)）。有噪声时，处于一个状态的细胞最终会越过到另一个，克隆群体成为混合物：平稳分布是双峰的，确定性的**双稳态**就变成关于两个长寿命状态以及二者之间跳跃速率的陈述。对一维链，平稳分布由式 (32.4) 精确给出，并定义一个有效势 $\Phi(n) = -\ln P(n)$，其极小点是稳定状态，极大点靠近确定性的阈值。切换的平均等待时间同样可以精确求出。

**定理 32.7.1（生灭链的平均首达时间）** 对出生速率为 $f(n)$、死亡速率为 $g(n)$、在 $0$ 处反射的链，设其平稳分布 $P_{\mathrm{s}}(n)$ 由式 (32.4) 给出，则从 $n_0$ 到 $n_1 > n_0$ 的平均首达时间为
$$
T(n_0 \to n_1) = \sum_{k=n_0}^{n_1 - 1}\frac{1}{f(k)P_{\mathrm{s}}(k)}\sum_{i=0}^{k}P_{\mathrm{s}}(i). \tag{32.18}
$$

**证明** 令 $T_k$ 为首次从 $k$ 到 $k + 1$ 的平均时间。从 $k$ 出发，下一个事件在平均时间 $1/(f(k) + g(k))$ 之后发生，是出生的概率为 $f(k)/(f(k) + g(k))$；若是死亡，链必须先回到 $k$。因此 $T_k = 1/(f(k) + g(k)) + [g(k)/(f(k) + g(k))](T_{k-1} + T_k)$，即 $f(k)T_k = 1 + g(k)T_{k-1}$，$T_0 = 1/f(0)$。乘以 $P_{\mathrm{s}}(k)$，并利用式 (32.4) 的 $g(k)P_{\mathrm{s}}(k) = f(k-1)P_{\mathrm{s}}(k-1)$，量 $y_k = f(k)P_{\mathrm{s}}(k)T_k$ 满足 $y_k = P_{\mathrm{s}}(k) + y_{k-1}$，所以 $y_k = \sum_{i \le k}P_{\mathrm{s}}(i)$。把 $T_k$ 从 $n_0$ 加到 $n_1 - 1$，即得式 (32.18)。$\square$

这个和由势垒附近 $P_{\mathrm{s}}$ 最小的状态主导，切换时间近似为 $\mathrm{e}^{\Delta\Phi}$ 乘以一个前因子，这是 **Kramers 速率**（[7.6.5](/7.6.5) 的定理 5.6.2）的离散对应。在化学体系的势中，势垒 $\Delta\Phi$ 不是能量除以 $k_{\mathrm{B}}T$，而是与体系大小成正比地增长：若所有拷贝数都按 $\Omega$ 标度，$\Phi(n) \approx \Omega\,\phi(n/\Omega)$，其中准势 $\phi$ 与 $\Omega$ 无关，切换时间按 $\mathrm{e}^{\Omega\Delta\phi}$ 增长。由几十个分子构成的开关在几个寿命内就翻转；由几百个分子构成的开关可能比生物体的寿命还稳定。化学 Langevin 方程能再现这种指数依赖，但通常势垒不对，因为越过势垒的罕见路径由跳跃过程的大偏差构成，而 Gauss 近似无法表示它们；切换速率必须从主方程本身或用大偏差方法计算。

![双稳态自激活基因的随机切换：合成为 f(n) = Ω[0.05 + s⁴/(1 + s⁴)]、s = n/(0.4Ω)，降解为 n（时间以蛋白质寿命为单位）的生灭链，因此体系大小 Ω 决定开启状态下的分子数。A：Ω = 30 的一条 Gillespie 轨迹，在 n ≈ 1（关）与 n ≈ 30（开）附近有长时间停留，二者之间快速转变。B：精确平稳分布，式 (32.4)（线），与 A 中轨迹按时间加权的分布（柱）；有效势 −ln P(n)（虚线，右轴）在确定性阈值附近有一个势垒。C：从关到开的平均切换时间随 Ω 的变化，每个点由 30 次模拟的切换得到（点），以及由定理 32.7.1 得到（线）：切换时间随体系大小指数增长](./plots/switching.py)

### 32.7.2. 实例

**例 32.7.1（lac 操纵子）** 在中等浓度的不可代谢诱导物下，*E. coli* 的克隆群体分裂为完全诱导和未诱导的细胞，因为由该操纵子表达的透性酶 LacY 会把自己的诱导物运入细胞（确定性的双稳态分析见 [7.6.33](/7.6.33)）。Choi、Cai、Frieda 与 Xie（2008）问：是什么使未诱导的细胞发生切换？通过计数单个 LacY 分子，他们发现有两类爆发：频繁的小爆发，只有一个或几个分子，当四聚体 LacI 阻遏物短暂地释放其 DNA 环的两个操纵基因之一并立即重新结合时产生；以及罕见的大爆发，有几十个分子，当阻遏物从 DNA 上完全解离、必须重新寻找操纵基因时产生。只有大爆发才产生足够的透性酶，越过正反馈的阈值。因此开关是由单分子事件触发的，即一个阻遏物的完全解离，切换速率由该事件的速率和阈值决定，而不是由平均表达水平决定。

**例 32.7.2（溶原状态）** 噬菌体 λ 的原噬菌体状态由阻遏物 CI 维持，它激活自己的启动子并阻遏 Cro（[7.2.11](/7.2.11)）。它异常稳定：在缺少 RecA 的细胞中，无法诱导破坏 CI 的 SOS 反应，测得自发转为裂解的概率每代少于 $10^7$ 个细胞中的一个（Little、Shepley 与 Wert，1999）。每个细胞有几百个 CI 分子时，这种稳定性与切换时间对分子数的指数依赖一致，它是遗传开关随机模型的经典检验案例（Aurell 与 Sneppen，2002）。

**例 32.7.3（单通道）** 如具有关闭与开放两个状态的通道这样的**两态系统**是最小的开关（[7.6.4](/7.6.4)）。它的开放与关闭停留时间都服从指数分布，均值等于速率的倒数。若关闭类包含若干由跃迁相连的状态，则关闭时间的分布成为指数之和，类中每个状态一项（Colquhoun 与 Hawkes，1981），因此实测停留时间直方图中的分量数是隐藏状态数的下界，门控方案正是这样由单通道记录推断出来的（[7.6.30](/7.6.30)）。

## 32.8. 涨落作为动力学信息的来源

### 32.8.1. 统计量揭示什么

本章的各个例子用的是同一原理：确定性模型预言的是平均值，只能由此推断速率的组合；而涨落的统计量分别依赖于各个速率和各步骤的顺序。

| 统计量 | 模型 | 揭示的内容 |
|---|---|---|
| mRNA 计数的 Fano 因子 | 双态启动子，定理 32.3.1 | 爆发大小；切换相对于降解的快慢；均值固定时操纵基因的强度（式 (32.8)） |
| 蛋白质分布的形状 | 爆发式合成，定理 32.4.1–32.4.2 | 由一张快照得到爆发频率 $a$ 与大小 $b$ |
| 等待时间分布 | 连续步骤，定理 32.1.1 | 限速步骤数（由变异系数的平方得 $1/k$） |
| 单分子的停留时间直方图 | 构象的 Markov 链 | 隐藏状态数（指数的个数） |
| 单个细胞中涨落的自相关 | 线性噪声近似，$\mathrm{e}^{J\tau}C$ | 不扰动细胞而得到的寿命与反馈 |
| 两个报告基因的互相关 | 双色实验 | 内在噪声与外在噪声（[7.2.22](/7.2.22#sec-22.5.4)）；由时间滞后得到的调控方向 |
| 突变体在各培养物中的分布 | Luria–Delbrück | 突变先于选择；**突变率** |

对**生灭过程**，涨落的自相关按 $\mathrm{e}^{-\gamma\tau}$ 衰减，而受负反馈调控的基因弛豫得更快，速率为 $\gamma(1 + H)$：Austin 等人（2006）利用合成自调控基因噪声的频率成分来测量反馈的效果，Dunlop、Cox、Levine、Murray 与 Elowitz（2008）则利用基因间涨落互相关中的时间滞后推断谁调控谁。这些方法把噪声看作细胞对自身施加的天然扰动。

### 32.8.2. 由母函数得到 Luria–Delbrück 分布

用涨落来裁决一个生物学问题，最早也最有影响的例子是 Luria 与 Delbrück（1943）的**波动试验**，其设计、历史与估计量见 [7.4.12](/7.4.12#sec-12.4)：若对噬菌体的抗性是在生长期间由突变产生的，则平行培养物中抗性细胞数的方差远大于其均值，而由暴露诱导的抗性则给出 Poisson 统计。这里我们把分布本身作为随机过程推导出来，这是对母函数的一次练习。

设野生型群体确定性地增长，$N(u) = N_0\mathrm{e}^u$（时间以增长速率的倒数为单位），突变以速率 $\mu N(u)$ 作为 Poisson 过程发生，$\mu$ 为每个细胞每单位时间的突变概率。每个突变体建立一个克隆，按纯出生（Yule）过程增长；在终点前 $s$ 时刻开始的克隆，其大小服从几何分布，$\mathbb{P}(k) = x(1 - x)^{k-1}$（$k \geq 1$），其中 $x = \mathrm{e}^{-s}$（Lea 与 Coulson，1949）。

**定理 32.8.1（Luria–Delbrück 分布的母函数）** 在 $N_0/N_t \to 0$ 的极限下，设 $m = \mu N_t$ 为期望突变数，培养物中的突变体数 $r$ 的母函数为
$$
G(z) = \exp\Bigl[m\,\frac{1 - z}{z}\,\ln(1 - z)\Bigr]. \tag{32.19}
$$
其概率满足递推 $p_0 = \mathrm{e}^{-m}$，$p_r = \frac{m}{r}\sum_{k=0}^{r-1}\frac{p_k}{r - k + 1}$，且当 $r$ 很大时 $p_r \approx m/r^2$。

**证明** 突变体数是复合 Poisson 和：突变在时刻 $u$ 以速率 $\mu N_0\mathrm{e}^u$ 发生，每次突变贡献一个独立的克隆，其母函数为 $g_s(z) = xz/(1 - (1 - x)z)$，$x = \mathrm{e}^{-s}$，$s = t - u$。对这样的和，$\ln G = \int(\text{速率})\,(g - 1)\,\mathrm{d}u$。利用 $\mu N_0\mathrm{e}^{u} = m\mathrm{e}^{-s}$ 与 $\mathrm{d}s = -\mathrm{d}x/x$，
$$
\ln G = \int_{\mathrm{e}^{-t}}^{1}m\,(g - 1)\,\mathrm{d}x \to -m(1 - z)\int_0^1\frac{\mathrm{d}x}{1 - z + zx} = m\,\frac{1 - z}{z}\ln(1 - z),
$$
因为 $g - 1 = -(1 - z)/(1 - z + zx)$。变量代换显示出一个简单的结构：突变克隆服从几何分布，其成功参数 $x$ 在 $(0, 1)$ 上均匀分布，这是因为细胞数以及突变机会的数目增长的速度，恰好与较早开始的克隆超过较晚开始的克隆的速度相同。对于递推，写 $\ln G = m\,h(z)$，$h(z) = \frac{1 - z}{z}\ln(1 - z) = -1 + \sum_{k\geq1}\frac{z^k}{k(k + 1)}$；则 $G' = mh'G$，用 $h'(z) = \sum_{k\geq1}z^{k-1}/(k + 1)$ 比较 $z^{r-1}$ 的系数，得 $rp_r = m\sum_{k=0}^{r-1}p_k/(r - k + 1)$。$h$ 在 $z = 1$ 处的奇点 $h \approx -(1 - z)\ln(1 - z)$，由标准的奇点分析推出尾部 $p_r \approx m/r^2$，因此 $\mathbb{P}(R \geq r) \approx m/r$。$\square$

尾部 $m/r^2$ 在无限大培养物的极限下均值无穷：在有限的培养物中均值为 $m\ln(N_t/N_0)$（[7.4.12](/7.4.12#sec-12.4.2)），由最早的突变产生的“头奖”主导，所以样本均值不能作为 $m$ 的估计量，标准做法是基于该递推的极大似然法。模型的假设，即野生型确定性增长、突变体同样增长、突变为 Poisson 过程、没有表型滞后，每一条都可以放宽（Zheng，1999），而用微流控对单个细胞中突变的直接观察已经表明，突变确实在时间上作为 Poisson 过程发生（Robert 等，2018）。

![由母函数式 (32.19) 得到的 Luria–Delbrück 分布。A：由定理 32.8.1 的递推得到的精确概率，每个培养物的期望突变数 m = 1（蓝）与 m = 4（红）（线），以及 10⁵ 个模拟培养物的频率（点），其中泊松数目的每次突变建立一个几何分布大小的克隆，成功概率如证明中那样在 (0, 1) 上均匀抽取；虚线是渐近线 m/r²，点线是均值为 m 的 Poisson 分布，数目相当的诱导机制会给出这样的分布。B：至少有 r 个突变体的概率及其重尾 m/r（虚线）：含有数百或数千个突变体的培养物并不罕见](./plots/luria-delbruck.py)

## 小结

- Poisson 过程（定义 32.1.1，定理 32.1.1）：计数服从 Poisson 分布，等待时间服从指数分布且无记忆，第 $k$ 个事件服从 Gamma 分布；$\operatorname{Var}(\tau)/\mathbb{E}[\tau]^2 = 1/k$ 数出连续步骤数。
- 化学主方程（定义 32.2.1–32.2.2，式 (32.1)）：倾向来自随机形式的质量作用定律；对均匀混合体系是精确的；只有倾向为线性时，均值才精确地服从速率方程（注 32.2.1）。

| 工具 | 结果 | 位置 |
|---|---|---|
| 母函数 | 生灭过程：二项分布的幸存者 + Poisson 分布的新增者，平稳态为 Poisson 分布 | 定理 32.2.1 |
| 链的细致平衡 | $P(m) \propto \prod f(i - 1)/g(i)$ | 式 (32.4) |
| 矩方程 | 生灭过程 $F = 1$；双态启动子 $F = 1 + rk_-/(\lambda(\lambda + \gamma))$ | 式 (32.5)，定理 32.3.1 |
| Fano 指纹 | 简单阻遏 $F = 1 + r\,\mathrm{FC}(1 - \mathrm{FC})/(k_{\mathrm{off}} + \gamma\mathrm{FC})$ | 式 (32.8) |
| 爆发主方程 | 负二项分布，$\langle n\rangle = ab$，$F = 1 + b$ | 定理 32.4.1 |
| 连续爆发 | Gamma 分布 $(a, b)$；有反馈时见式 (32.13) | 定理 32.4.2 |
| 精确模拟 | 以 $a_0$ 为速率的指数等待时间，以概率 $a_j/a_0$ 选取反应 | 算法 32.5.1 |
| Gauss 近似 | 化学 Langevin 方程；线性噪声近似 $JC + CJ^{\mathsf T} + D = 0$ | 定义 32.6.1–32.6.2 |
| 反馈 | $F = 1/(1 + H)$：负反馈为亚 Poisson，正反馈在分岔点发散 | 式 (32.17) |
| 首达 | 链的精确切换时间，$\propto \mathrm{e}^{\Omega\Delta\phi}$ | 定理 32.7.1 |
| 复合 Poisson | Luria–Delbrück $G(z) = \exp[m(1 - z)z^{-1}\ln(1 - z)]$，尾部 $m/r^2$ | 定理 32.8.1 |

- 涨落携带着平均值不包含的动力学信息：爆发参数、隐藏步骤与状态的数目、寿命与反馈，以及突变与选择的先后顺序（32.8.1）。

## 思考题

1. 一个组成型基因产生的蛋白质，在 *E. coli* 群体中 $\langle p\rangle = 50$，$\operatorname{Var}(p) = 500$。用爆发模型解释这些数字，并估计该基因每个细胞周期产生多少个 mRNA。用什么测量可以检验这一解释？

   **答** 由定理 32.4.1，$F = 1 + b = 10$ 给出爆发大小 $b = 9$ 个蛋白质/每个 mRNA，爆发频率 $a = \langle p\rangle/b \approx 5.6$ 次/每个蛋白质寿命。若蛋白质稳定、只通过稀释被清除，则寿命为 $T_{\mathrm{cycle}}/\ln 2$，所以该基因每个细胞周期约产生 $5.6\ln 2 \approx 3.9$ 个 mRNA。外在噪声也对方差有贡献，因此这个 $b$ 是上界。直接的检验是在延时成像中计数新合成的分子（如 Yu 等人所做），这样可独立地得到 $a$ 与 $b$；或者用 smFISH 测量 mRNA 的分布（均值约为每个细胞 $a\gamma_p/\gamma_m$，组成型启动子为 Poisson 分布）。

2. 证明对生灭过程，mRNA 数的平稳自相关为 $\langle\delta m(t + \tau)\delta m(t)\rangle = (k/\gamma)\mathrm{e}^{-\gamma\lvert\tau\rvert}$，并解释这如何使人能在未受扰动的细胞中测量 mRNA 的寿命。

   **答** 对 $m(t)$ 取条件，$m(t + \tau)$ 的均值服从式 (32.5)：$\mathbb{E}[m(t + \tau)\mid m(t)] = k/\gamma + (m(t) - k/\gamma)\mathrm{e}^{-\gamma\tau}$。乘以 $\delta m(t)$ 并取平均，得 $\operatorname{Var}(m)\mathrm{e}^{-\gamma\tau} = (k/\gamma)\mathrm{e}^{-\gamma\tau}$，而平稳过程的这个函数关于 $\tau$ 是偶函数。这就是定义 32.6.2 中 $J = -\gamma$ 的 $\mathrm{e}^{J\tau}C$。因此，单个细胞时间进程中涨落自相关的衰减时间就是 mRNA 的寿命，无需用药物阻断转录（那会扰动细胞）。实际中，测得的信号还被报告分子自身的寿命滤波，必须加以考虑。

3. 由式 (32.2) 推导式 (32.5)，并推广到以速率 $f(x)$ 合成、以速率 $g(x)$ 清除的组分在线性噪声近似下的方差方程。

   **答** 把式 (32.2) 乘以 $m$ 并求和，移位的和给出 $\sum mP(m-1) = \langle m\rangle + 1$ 与 $\sum m(m+1)P(m+1) = \langle m^2\rangle - \langle m\rangle$，所以 $\mathrm{d}\langle m\rangle/\mathrm{d}t = k - \gamma\langle m\rangle$。乘以 $m^2$：$\sum m^2P(m-1) = \langle m^2\rangle + 2\langle m\rangle + 1$，$\sum m^2(m+1)P(m+1) = \langle m^3\rangle - 2\langle m^2\rangle + \langle m\rangle$，所以 $\mathrm{d}\langle m^2\rangle/\mathrm{d}t = k(2\langle m\rangle + 1) + \gamma(\langle m\rangle - 2\langle m^2\rangle)$；减去 $\mathrm{d}\langle m\rangle^2/\mathrm{d}t = 2\langle m\rangle(k - \gamma\langle m\rangle)$ 即得方差方程。一般地，$\mathrm{d}\operatorname{Var}/\mathrm{d}t = 2(f'(x^*) - g'(x^*))\operatorname{Var} + f(x^*) + g(x^*)$，即式 (32.16) 的一维形式。

4. *E. coli* 细胞（$1\,\mathrm{fL}$）中有 $20$ 个转录因子分子，它以扩散限制的速率常数 $10^8\,\mathrm{M^{-1}\,s^{-1}}$、$K_{\mathrm{D}} = 1\,\mathrm{nM}$ 结合其操纵基因。计算结合与解离的倾向、操纵基因被占据的时间分数，以及结合期与自由期的平均持续时间。若启动子自由时以 $r = 0.5\,\mathrm{min^{-1}}$ 产生 mRNA，mRNA 寿命为 $3\,\mathrm{min}$，启动子会表现出爆发性吗？

   **答** $c_{\mathrm{on}} = k_{\mathrm{on}}/(N_{\mathrm{A}}V) = 10^8/(6.0\times10^{8}) = 0.17\,\mathrm{s^{-1}}$（每个分子），所以结合倾向为 $20 \times 0.17 = 3.3\,\mathrm{s^{-1}}$；$k_{\mathrm{off}} = k_{\mathrm{on}}K_{\mathrm{D}} = 0.1\,\mathrm{s^{-1}}$。占据率 $= 3.3/(3.3 + 0.1) = 0.97$（等价地，$20$ 个分子是 $33\,\mathrm{nM}$，$33/(33 + 1) = 0.97$）。结合期平均持续 $10\,\mathrm{s}$，自由期 $0.3\,\mathrm{s}$。两者都远短于 mRNA 寿命（$\lambda = 3.4\,\mathrm{s^{-1}} \gg \gamma = 0.0056\,\mathrm{s^{-1}}$），且 $rk_-/(\lambda(\lambda+\gamma)) = (0.0083 \times 3.3)/(3.4 \times 3.4) \approx 0.002$，故 $F \approx 1$：切换被平均掉，表达是 Poisson 的，均值为 $(r/\gamma)\times 0.03 = 1.5 \times 0.029 \approx 0.04$ 个 mRNA/每个细胞。要表现出爆发性，需要结合期与 mRNA 寿命相当或更长，也就是 $k_{\mathrm{off}}$ 小得多（更强的操纵基因，如式 (32.8)）。

5. 对二聚化反应 $\ce{2A <=> A2}$，共有 $N = 20$ 个单体，$c_1 = 0.05$（缔合倾向 $c_1n_{\mathrm{A}}(n_{\mathrm{A}} - 1)/2$），$c_2 = 1$（解离倾向 $c_2n_{\mathrm{A_2}}$），实现算法 32.5.1。把二聚体数的平稳均值与确定性预言比较，并解释差别。

   **答** 有 $d$ 与 $d + 1$ 个二聚体的状态之间的细致平衡给出精确的平稳分布：$P(d + 1)/P(d) = c_1(N - 2d)(N - 2d - 1)/(2c_2(d + 1))$，由此（或由模拟）得 $\langle d\rangle \approx 3.76$。确定性方程 $c_1n_{\mathrm{A}}^2/2 = c_2d$（$n_{\mathrm{A}} = N - 2d$）把 $n(n-1)$ 当作 $n^2$ 并忽略涨落，给出 $d \approx 3.82$。随机均值较低，是因为分子不能与自身二聚化，这由因子 $n(n-1)$ 计入而 $n^2$ 没有，其相对大小为 $1/n_{\mathrm{A}}$；对非线性倾向，$\langle a(n)\rangle \neq a(\langle n\rangle)$（注 32.2.1）。浓度固定、$N \to \infty$ 时差别消失。

   ```python
   import numpy as np
   N, c1, c2 = 20, 0.05, 1.0
   w = [1.0]
   for d in range(N // 2):
       nA = N - 2 * d
       w.append(w[-1] * c1 * nA * (nA - 1) / (2 * c2 * (d + 1)))
   w = np.array(w) / sum(w)
   print((np.arange(w.size) * w).sum())      # exact stochastic mean, about 3.76
   from scipy.optimize import brentq
   print(brentq(lambda d: c1 * (N - 2 * d) ** 2 / 2 - c2 * d, 0, N / 2))   # deterministic, about 3.82
   ```

6. 用线性噪声近似证明增益为 $H$ 的负自调控使涨落的弛豫加快 $1 + H$ 倍，并使方差减小同样的倍数。为什么在平均水平相同时，简单地提高未调控蛋白质的降解速率不能同时达到这两点？

   **答** 取 $J = -\gamma(1 + H)$，自相关以 $\gamma(1 + H)$ 衰减，$C = D/(2\gamma(1 + H)) = x^*/(1 + H)$。对未调控的蛋白质，在均值固定时提高 $\gamma$ 需要按比例提高合成速率：弛豫同样加快，但方差仍等于均值（Poisson），因为噪声源 $D = 2\gamma x^*$ 与耗散增长得一样快。反馈不同，它增大耗散（恢复斜率），却不增加作为噪声源的反应事件数。代价是制造和维持调控回路的成本，而且对比反馈环路更快的噪声，衰减是有限的。

7. 在一次**波动试验**中，$50$ 个培养物各有 $10^8$ 个细胞，其中 $18$ 个培养物没有抗性突变体。估计 $m$ 与**突变率**，并用定理 32.8.1 的渐近式估计预期有多少个培养物含有超过 $100$ 个突变体。

   **答** $p_0 = 18/50 = 0.36 = \mathrm{e}^{-m}$ 给出 $m = 1.02$，$\mu = m/N_t = 1.0 \times 10^{-8}$（每个细胞每代）。尾部 $\mathbb{P}(R \geq r) \approx m/r$ 给出 $\mathbb{P}(R > 100) \approx 0.01$，所以 $50$ 个培养物中约有 $0.5$ 个，即每两次这样的实验出现一次头奖。（精确递推给出相近的值；有限的培养物大小只在 $r \sim N_t/N_0$ 附近截断尾部。）

8. （开放题）某基因的蛋白质在克隆群体中呈双峰分布。列出三种可能产生双峰的不同机制，并运用本章的思想设计区分它们的测量。

   **答** (1) 正反馈产生的双稳态（32.7）：两个状态寿命很长；把两个峰的细胞分别分选出来重新培养，会显示出记忆，随后以依赖于诱导物和分子数的速率缓慢弛豫到双峰混合物；若打断反馈环（例如使反馈组分组成型表达），双峰即消失。(2) 无反馈的慢启动子切换（32.3.2 的慢切换极限，用快速报告分子代替长寿命蛋白质）：mRNA 计数中出现零膨胀的 Poisson 分布；延时成像显示 ON 与 OFF 期的持续时间服从指数分布且与表达水平无关，打断反馈并不消除它。(3) 外在的异质性，例如细胞周期阶段、生长速率或受别处控制的某个调控因子不同的两个亚群：另一个不相关启动子的第二个报告基因与第一个共变（双色相关，32.8.1），按细胞大小或阶段取条件后双峰消失。区分 (1) 与 (2) 要利用停留时间对蛋白质水平的依赖以及反馈的效果；把二者与 (3) 区分开则用内在–外在噪声的分解。

9. 对双态启动子，直接由定理 32.3.1 证明：在均值 $\langle m\rangle$ 与活跃时间分数 $f = k_+/\lambda$ 固定时，Fano 因子随切换速率 $\lambda$ 的增大而单调减小，并求其极限。

   **答** 令 $r = \gamma\langle m\rangle/f$，$k_- = (1 - f)\lambda$，则 $F = 1 + \gamma\langle m\rangle(1 - f)/(f(\lambda + \gamma))$，它随 $\lambda$ 单调减小。当 $\lambda \to 0$，$F \to 1 + \langle m\rangle(1 - f)/f = 1 + (r/\gamma)(1 - f)$，即慢切换（零膨胀）极限；当 $\lambda \to \infty$，$F \to 1$，即 Poisson 极限。噪声在两个极限之间减半时的切换速率为 $\lambda = \gamma$：当启动子的切换发生在 mRNA 寿命的时间尺度上或更慢时，启动子动力学才影响噪声。
