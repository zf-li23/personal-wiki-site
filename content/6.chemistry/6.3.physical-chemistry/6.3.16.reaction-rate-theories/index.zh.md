---
title: 反应速率理论
---

[6.3.15](/6.3.15) 把速率常数当作由实验确定的参数。速率理论要回答的是：能否由分子的性质（大小、质量、结构、相互作用势能）计算速率常数？一个合格的理论至少要给出**质量作用定律**与 **Arrhenius 方程**，并说明活化能与**指前因子**的物理意义。[6.1.7](/6.1.7#sec-7.2) 已经给出了**碰撞理论**与**过渡态理论**的定性图像；本章把它们定量化。

碰撞理论（16.1）把分子看成硬球，用 [5.2.1](/5.2.1) 的 **Maxwell 速率分布**对碰撞截面积分，结果直观，却无法计算临界能与**方位因子**。过渡态理论把反应看成在势能面上越过一个鞍点（16.2），假设反应物与活化络合物处于平衡，用 [6.3.10](/6.3.10)–[6.3.11](/6.3.11) 的**配分函数**与统计热力学计算这个"平衡常数"（16.3），从而原则上能由分子结构算出速率常数，并给出活化焓、活化熵这些可以与实验比较的热力学量。单分子反应理论（16.4）说明一个分子"自己"分解时如何获得能量，是 [6.3.15](/6.3.15) 稳态近似的一个经典应用。最后简要介绍从单次碰撞研究反应的分子反应动态学（16.5）。溶液中的反应与催化见 [6.3.17](/6.3.17)。

## 16.1. 碰撞理论

### 16.1.1. 基本假设与碰撞数

碰撞理论的要点：

1. 反应物分子必须碰撞才能反应。
2. 分子是没有内部结构的硬球；碰撞分为弹性碰撞（只交换动量）、非弹性碰撞（内部运动加剧）与反应碰撞，只有足够剧烈的碰撞才是**有效碰撞**。
3. 碰撞的剧烈程度用相对平动能衡量，它超过某一与温度无关的临界值时才能反应。
4. 分子速率服从 Maxwell–Boltzmann 分布，反应不破坏这一分布。

**定义 16.1.1** 把分子 A、B 看成直径为 $d_{\mathrm{A}}$、$d_{\mathrm{B}}$ 的硬球，两球心能接近的最小距离 $d_{\mathrm{AB}} = \frac12(d_{\mathrm{A}} + d_{\mathrm{B}})$ 称为**碰撞直径**。单位体积、单位时间内 A 与 B 分子碰撞的总次数 $Z_{\mathrm{AB}}$ 称为**碰撞数**（碰撞频率因子），单位 $\mathrm{m^{-3}\,s^{-1}}$。

一个 A 分子相对 B 以速率 $v_{\mathrm{rel}}$ 运动，单位时间扫过一个截面为**碰撞截面** $\sigma = \pi d_{\mathrm{AB}}^2$、长为 $v_{\mathrm{rel}}$ 的圆柱，中心落在其中的 B 分子都与它相碰（[5.2.2](/5.2.2#def-2.3.1) 的**平均碰撞频率**用的是同一方法）。对相对速率的分布取平均（16.1.3），

$$
Z_{\mathrm{AB}} = \pi d_{\mathrm{AB}}^2\bar v_{\mathrm{rel}}n_{\mathrm{A}}n_{\mathrm{B}}, \qquad \bar v_{\mathrm{rel}} = \sqrt{\frac{8k_{\mathrm{B}}T}{\pi\mu}} = \sqrt{\frac{8RT}{\pi M_\mu}},
$$
其中 $n_{\mathrm{A}}, n_{\mathrm{B}}$ 是数密度，$\mu = \frac{m_{\mathrm{A}}m_{\mathrm{B}}}{m_{\mathrm{A}} + m_{\mathrm{B}}}$ 是**约化质量**，$M_\mu = N_{\mathrm{A}}\mu$ 是约化摩尔质量。初等的推导由两分子的平均速率"以 $90^\circ$ 相碰"得到 $\bar v_{\mathrm{rel}} = (\bar v_{\mathrm{A}}^2 + \bar v_{\mathrm{B}}^2)^{1/2}$，结果相同；严格的推导是相对速度同样服从 Maxwell 分布，只是质量换成 $\mu$（16.1.3）。同种分子碰撞时每次碰撞被计数两次，$Z_{\mathrm{AA}} = \frac12\pi d_{\mathrm{A}}^2\bar v_{\mathrm{rel}}n_{\mathrm{A}}^2$，$\mu = m_{\mathrm{A}}/2$，即 $Z_{\mathrm{AA}} = 2d_{\mathrm{A}}^2n_{\mathrm{A}}^2\sqrt{\pi RT/M_{\mathrm{A}}}$。

若每次碰撞都反应，常温常压下气相双分子反应将在约 $10^{-9}\,\mathrm{s}$ 内完成（数量级估计见 [6.1.7](/6.1.7#sec-7.2.1)）；只有很小一部分碰撞是有效的。

### 16.1.2. 碰撞参数与反应截面

两个分子的总动能可以分成质心运动的动能与相对运动的动能：

$$
\frac12m_{\mathrm{A}}v_{\mathrm{A}}^2 + \frac12m_{\mathrm{B}}v_{\mathrm{B}}^2 = \frac12(m_{\mathrm{A}} + m_{\mathrm{B}})v_{\mathrm{g}}^2 + \frac12\mu v_{\mathrm{rel}}^2.
$$
**质心**的运动在碰撞中不变，对反应没有贡献；只有相对平动能 $\varepsilon = \frac12\mu v_{\mathrm{rel}}^2$ 可以用来克服能垒。但即使 $\varepsilon$ 足够大，擦边而过的碰撞也不会引起反应。

**定义 16.1.2** 过 A 球心作平行于相对速度 $\boldsymbol{v}_{\mathrm{rel}}$ 的直线，B 球心的运动直线与它的距离 $b$ 称为**碰撞参数**。$b = 0$ 是迎头碰撞，$b \ge d_{\mathrm{AB}}$ 时不碰撞。

设碰撞时连心线与 $\boldsymbol{v}_{\mathrm{rel}}$ 的夹角为 $\theta$，则 $b = d_{\mathrm{AB}}\sin\theta$。硬球碰撞中，相对速度沿连心线的分量 $v_{\mathrm{rel}}\cos\theta$ 决定撞击的剧烈程度，相应的动能

$$
\varepsilon' = \frac12\mu(v_{\mathrm{rel}}\cos\theta)^2 = \varepsilon\left(1 - \frac{b^2}{d_{\mathrm{AB}}^2}\right).
$$
对所有 $b$ 积分，$\int_0^{d_{\mathrm{AB}}}2\pi b\,\mathrm{d}b = \pi d_{\mathrm{AB}}^2$，就是碰撞截面。

**定义 16.1.3** 只有沿连心线的相对平动能 $\varepsilon'$ 超过某一临界值 $\varepsilon_{\mathrm{c}}$ 的碰撞才能引起反应，$\varepsilon_{\mathrm{c}}$ 称为**阈能**（临界能），按摩尔计 $E_{\mathrm{c}} = N_{\mathrm{A}}\varepsilon_{\mathrm{c}}$。相对平动能为 $\varepsilon$ 时，能引起反应的碰撞参数满足 $b < b_{\mathrm{r}}$，$\varepsilon(1 - b_{\mathrm{r}}^2/d_{\mathrm{AB}}^2) = \varepsilon_{\mathrm{c}}$，面积

$$
\sigma_{\mathrm{r}}(\varepsilon) = \pi b_{\mathrm{r}}^2 = \begin{cases}\pi d_{\mathrm{AB}}^2\left(1 - \dfrac{\varepsilon_{\mathrm{c}}}{\varepsilon}\right), & \varepsilon > \varepsilon_{\mathrm{c}},\\[2mm] 0, & \varepsilon \le \varepsilon_{\mathrm{c}}\end{cases}
$$
称为**反应截面**。

反应截面从阈能处由零开始增大，$\varepsilon \to \infty$ 时趋于碰撞截面。它是一个微观量，可以用交叉分子束（16.5）在确定的相对能量下直接测量；硬球模型只是它最简单的一种形式。

### 16.1.3. 由反应截面求速率常数

考虑相对速率为 $v_{\mathrm{rel}}$ 的 A 分子束射入 B 中。单位体积内 A 与 B 单位时间发生的反应次数为 $\sigma_{\mathrm{r}}(v_{\mathrm{rel}})v_{\mathrm{rel}}n_{\mathrm{A}}n_{\mathrm{B}}$，所以对确定的相对速率，微观速率常数 $k(v_{\mathrm{rel}}) = v_{\mathrm{rel}}\sigma_{\mathrm{r}}(v_{\mathrm{rel}})$。宏观速率常数是它对相对速率分布的平均：

$$
k(T) = \int_0^\infty v_{\mathrm{rel}}\sigma_{\mathrm{r}}(v_{\mathrm{rel}})f(v_{\mathrm{rel}})\,\mathrm{d}v_{\mathrm{rel}}, \qquad f(v) = 4\pi\left(\frac{\mu}{2\pi k_{\mathrm{B}}T}\right)^{3/2}v^2\mathrm{e}^{-\mu v^2/2k_{\mathrm{B}}T}.
$$

**定理 16.1.1（硬球碰撞理论的速率常数）** 在上述假设下，双分子反应 $\ce{A + B -> P}$ 的速率常数为

$$
k(T) = \pi d_{\mathrm{AB}}^2\sqrt{\frac{8k_{\mathrm{B}}T}{\pi\mu}}\,\mathrm{e}^{-\varepsilon_{\mathrm{c}}/k_{\mathrm{B}}T} \quad(\text{每对分子}), \qquad k = N_{\mathrm{A}}\pi d_{\mathrm{AB}}^2\sqrt{\frac{8RT}{\pi M_\mu}}\,\mathrm{e}^{-E_{\mathrm{c}}/RT} \quad(\text{按摩尔}). \tag{16.1}
$$

**证明** 换成相对平动能 $\varepsilon = \frac12\mu v^2$ 作积分变量：$\mathrm{d}\varepsilon = \mu v\,\mathrm{d}v$，$v^3\,\mathrm{d}v = \frac{2\varepsilon}{\mu^2}\mathrm{d}\varepsilon$，于是

$$
vf(v)\,\mathrm{d}v = 4\pi\left(\frac{\mu}{2\pi k_{\mathrm{B}}T}\right)^{3/2}\frac{2\varepsilon}{\mu^2}\mathrm{e}^{-\varepsilon/k_{\mathrm{B}}T}\,\mathrm{d}\varepsilon = \left(\frac{8}{\pi\mu}\right)^{1/2}(k_{\mathrm{B}}T)^{-3/2}\varepsilon\,\mathrm{e}^{-\varepsilon/k_{\mathrm{B}}T}\,\mathrm{d}\varepsilon.
$$
代入反应截面，

$$
k(T) = \left(\frac{8}{\pi\mu}\right)^{1/2}(k_{\mathrm{B}}T)^{-3/2}\pi d_{\mathrm{AB}}^2\int_{\varepsilon_{\mathrm{c}}}^\infty(\varepsilon - \varepsilon_{\mathrm{c}})\mathrm{e}^{-\varepsilon/k_{\mathrm{B}}T}\,\mathrm{d}\varepsilon.
$$
令 $\varepsilon - \varepsilon_{\mathrm{c}} = k_{\mathrm{B}}Tu$，积分等于 $(k_{\mathrm{B}}T)^2\mathrm{e}^{-\varepsilon_{\mathrm{c}}/k_{\mathrm{B}}T}\int_0^\infty u\mathrm{e}^{-u}\,\mathrm{d}u = (k_{\mathrm{B}}T)^2\mathrm{e}^{-\varepsilon_{\mathrm{c}}/k_{\mathrm{B}}T}$（$\int_0^\infty u\mathrm{e}^{-u}\,\mathrm{d}u$ 是 **Gamma 函数** $\Gamma(2) = 1$）。整理即得式 (16.1)；乘 $N_{\mathrm{A}}$ 把每对分子的速率常数（$\mathrm{m^3\,s^{-1}}$）换成按摩尔计的速率常数（$\mathrm{m^3\,mol^{-1}\,s^{-1}}$）。$\square$

$\varepsilon_{\mathrm{c}} = 0$ 时 $k = \pi d_{\mathrm{AB}}^2\bar v_{\mathrm{rel}}$，即每次碰撞都反应，回到 16.1.1 的碰撞数；所以 $\mathrm{e}^{-E_{\mathrm{c}}/RT}$ 就是有效碰撞分数。值得注意的是，这个分数并不是"相对平动能超过 $E_{\mathrm{c}}$ 的分子对所占的比例"。记 $x = E_{\mathrm{c}}/RT$：相对平动能超过 $E_{\mathrm{c}}$ 的分子对占 $2\sqrt{x/\pi}\,\mathrm{e}^{-x} + \operatorname{erfc}\sqrt{x}$；按碰撞通量加权（快分子碰撞更频繁，因子 $v$）后，能量超过 $E_{\mathrm{c}}$ 的碰撞占 $(1 + x)\mathrm{e}^{-x}$；再扣除擦边碰撞（反应截面的因子 $1 - \varepsilon_{\mathrm{c}}/\varepsilon$），才恰好得到简单的 **Boltzmann 因子** $\mathrm{e}^{-x}$。

![硬球模型：左为反应截面随相对平动能的变化；右为按通量加权的相对平动能分布 ε exp(−ε/kBT)（蓝）与它乘以反应截面后的被积函数（红），取 εc = 4kBT 时数值积分给出反应分数 e⁻⁴，与定理 16.1.1 一致](./plots/collision-cross-section.py)

对同种分子 $\ce{2A -> P}$，按 $v = -\frac12\frac{\mathrm{d}c_{\mathrm{A}}}{\mathrm{d}t} = kc_{\mathrm{A}}^2$ 定义，$k = \frac12N_{\mathrm{A}}\pi d_{\mathrm{A}}^2\sqrt{\frac{16RT}{\pi M_{\mathrm{A}}}}\mathrm{e}^{-E_{\mathrm{c}}/RT} = 2N_{\mathrm{A}}d_{\mathrm{A}}^2\sqrt{\frac{\pi RT}{M_{\mathrm{A}}}}\mathrm{e}^{-E_{\mathrm{c}}/RT}$。

### 16.1.4. 与 Arrhenius 方程的比较

式 (16.1) 可写成 $k = BT^{1/2}\mathrm{e}^{-E_{\mathrm{c}}/RT}$，$B$ 与温度无关。由活化能的定义

$$
E_{\mathrm{a}} = RT^2\frac{\mathrm{d}\ln k}{\mathrm{d}T} = E_{\mathrm{c}} + \frac12RT, \qquad A = N_{\mathrm{A}}\pi d_{\mathrm{AB}}^2\sqrt{\frac{8RT}{\pi M_\mu}}\,\mathrm{e}^{1/2}.
$$
$298\,\mathrm{K}$ 时 $\frac12RT = 1.2\,\mathrm{kJ\,mol^{-1}}$，一般反应的 $E_{\mathrm{a}}$ 大得多，所以 $E_{\mathrm{c}} \approx E_{\mathrm{a}}$。因为 $E_{\mathrm{c}}$ 被假设为常数，$E_{\mathrm{a}}$ 与 $A$ 都随温度缓慢变化。

碰撞理论算出的指前因子对简单反应大致正确，对复杂分子则往往偏大，于是引入**方位因子** $P$（[6.1.7](/6.1.7#def-7.2.2)），$k = PN_{\mathrm{A}}\pi d_{\mathrm{AB}}^2\bar v_{\mathrm{rel}}\mathrm{e}^{-E_{\mathrm{c}}/RT}$。几个反应的指前因子（单位 $\mathrm{L\,mol^{-1}\,s^{-1}}$，数据取自 Atkins 的教材）：

| 反应 | $A_{\text{实验}}$ | $A_{\text{理论}}$ | $P$ |
|---|---|---|---|
| $\ce{2NOCl -> 2NO + 2Cl}$ | $9.4 \times 10^9$ | $5.9 \times 10^{10}$ | 0.16 |
| $\ce{2ClO -> Cl2 + O2}$ | $6.3 \times 10^7$ | $2.5 \times 10^{10}$ | $2.5 \times 10^{-3}$ |
| $\ce{H2 + C2H4 -> C2H6}$ | $1.24 \times 10^6$ | $7.3 \times 10^{11}$ | $1.7 \times 10^{-6}$ |
| $\ce{K + Br2 -> KBr + Br}$ | $1.0 \times 10^{12}$ | $2.1 \times 10^{11}$ | 4.8 |

**例 16.1.1** 取 $\ce{H2}$ 与 $\ce{C2H4}$ 的碰撞截面 $0.27$ 与 $0.64\,\mathrm{nm^2}$，估计 $628\,\mathrm{K}$ 时 $\ce{H2 + C2H4}$ 的理论指前因子（不含因子 $\mathrm{e}^{1/2}$）。

**解** $d_{\ce{H2}} = (0.27/\pi)^{1/2}\,\mathrm{nm} = 0.293\,\mathrm{nm}$，$d_{\ce{C2H4}} = 0.451\,\mathrm{nm}$，$d_{\mathrm{AB}} = 0.372\,\mathrm{nm}$，$\sigma = \pi d_{\mathrm{AB}}^2 = 0.435\,\mathrm{nm^2}$。$M_\mu = \frac{2.016 \times 28.05}{30.07}\,\mathrm{g\,mol^{-1}} = 1.881\,\mathrm{g\,mol^{-1}}$，

$$
\bar v_{\mathrm{rel}} = \sqrt{\frac{8 \times 8.314 \times 628}{\pi \times 1.881 \times 10^{-3}}}\,\mathrm{m\,s^{-1}} = 2.66 \times 10^3\,\mathrm{m\,s^{-1}},
$$

$$
\sigma\bar v_{\mathrm{rel}}N_{\mathrm{A}} = 0.435 \times 10^{-18} \times 2.66 \times 10^3 \times 6.022 \times 10^{23}\,\mathrm{m^3\,mol^{-1}\,s^{-1}} = 7.0 \times 10^{11}\,\mathrm{L\,mol^{-1}\,s^{-1}},
$$
与表中的理论值一致；与实验值比较得 $P \approx 2 \times 10^{-6}$：加氢要求 $\ce{H2}$ 的两个 H 原子同时与 C=C 双键作用，几何要求极严。

$P > 1$ 的 $\ce{K + Br2}$ 用"鱼叉机理"解释：K 原子在远大于硬球碰撞直径的距离上就把价电子"投"给 $\ce{Br2}$，形成的 $\ce{K+}$ 与 $\ce{Br2-}$ 靠 Coulomb 吸引拉到一起，有效反应截面比几何截面大得多。

碰撞理论的成功在于直观地给出了质量作用定律和 Arrhenius 方程的形式，并正确地估计了指前因子的数量级；它的根本缺陷是阈能与方位因子都无法由理论计算，硬球模型也不涉及化学键怎样变化。克服这两点需要势能面与过渡态理论。

## 16.2. 势能面与反应坐标

### 16.2.1. 双原子分子的势能曲线

按 Born–Oppenheimer 近似，电子运动远快于核运动，核在电子提供的势能 $E_{\mathrm{p}}$ 中运动，$E_{\mathrm{p}}$ 是核坐标的函数。双原子分子的势能只依赖核间距 $r$。

**定义 16.2.1（Morse 势）** 经验势能函数

$$
E_{\mathrm{p}}(r) = D_{\mathrm{e}}\left[\mathrm{e}^{-2a(r - r_{\mathrm{e}})} - 2\mathrm{e}^{-a(r - r_{\mathrm{e}})}\right]
$$
称为 **Morse 势**，其中 $r_{\mathrm{e}}$ 是平衡核间距，$D_{\mathrm{e}}$ 是势阱的深度（以分开的原子为能量零点），$a$ 是与势阱宽度有关的常数。

在 $r_{\mathrm{e}}$ 附近展开，$E_{\mathrm{p}} \approx -D_{\mathrm{e}} + D_{\mathrm{e}}a^2(r - r_{\mathrm{e}})^2$，与谐振子的 $\frac12\mu\omega^2(r - r_{\mathrm{e}})^2$ 比较得 $a = \omega\sqrt{\mu/2D_{\mathrm{e}}}$，$\omega = 2\pi\nu$ 是谐振频率。$D_{\mathrm{e}}$ 是势阱深度而不是能垒：$r \to \infty$ 时势能单调趋于零，解离没有能垒。实际的解离能要从振动基态算起，$D_0 = D_{\mathrm{e}} - \frac12h\nu$（**零点能**，见 [5.5.5](/5.5.5#sec-5.3.3) 的振动能级）。Morse 势比谐振子更好地描述了大振幅振动：能级间隔随振动量子数减小，并在 $D_{\mathrm{e}}$ 处收敛。

### 16.2.2. 三原子反应的势能面

以 $\ce{A + B-C -> A-B + C}$ 为例（如 $\ce{H + H2}$、$\ce{H + Br2 -> HBr + Br}$）。三原子体系的势能是三个内坐标的函数，$E_{\mathrm{p}}(r_{\mathrm{AB}}, r_{\mathrm{BC}}, \angle\mathrm{ABC})$。若 A 沿 BC 的轴线进攻（共线碰撞，$\angle\mathrm{ABC} = 180^\circ$），势能只依赖两个核间距，可以画成一张曲面。

**定义 16.2.2** 势能作为核坐标的函数在坐标空间中构成的曲面（多原子体系是超曲面）称为**势能面**。反应物与产物位于势能面上的两个山谷中，连接两个山谷、每一点都是垂直于路径方向上的能量极小的路径称为**最小能量路径**；它经过两谷之间山脊上的最低点，即势能面的**鞍点**（[2.2.11](/2.2.11#def-11.5.2)）。

鞍点沿路径方向是极大，在垂直方向上是极小，它对应的构型就是**过渡态** $[\mathrm{A\cdots B\cdots C}]^{\ddagger}$。沿最小能量路径量出的弧长就是**反应坐标**（[6.1.7](/6.1.7#def-7.2.3)），势能沿它的变化（势能剖面）就是 [6.1.7](/6.1.7#sec-7.2.2) 中的势能图。最小能量路径应在质量加权坐标中计算：这样定义的最速下降路径才是无限缓慢运动的体系实际走的路径。

势能面上的几个特征区域：

- 反应物谷（$r_{\mathrm{BC}} \approx r_{\mathrm{e}}$，$r_{\mathrm{AB}}$ 很大）与产物谷；
- 原点附近两个核间距都很小，原子核相互排斥，势能急剧升高；
- $r_{\mathrm{AB}}$、$r_{\mathrm{BC}}$ 都很大时是三个孤立原子，势能平缓地升高到一个高原。

![共线 H + H2 → H2 + H 的 LEPS 势能面（Sato 形式：H2 的 Morse 参数 De = 4.747 eV、a = 19.42 nm⁻¹、re = 0.0742 nm，Sato 参数 0.135 使鞍点高度与精确的量子化学计算值约 40 kJ/mol 相符）。左：等势线与质量加权坐标中的最小能量路径，鞍点在 rAB = rBC = 0.093 nm；右：沿路径的势能剖面](./plots/leps-surface.py)

势能面由量子化学计算（求解一系列核构型下的电子 Schrödinger 方程）得到。1931 年 Eyring 与 Polanyi 用半经验方法构造了第一张 $\ce{H + H2}$ 的势能面；上图所用的 LEPS（London–Eyring–Polanyi–Sato）方法把三原子体系的能量用三个双原子对的 Coulomb 积分与交换积分表示，参数取自双原子的光谱数据，是最简单而仍有定量意义的模型。今天的从头计算给出 $\ce{H + H2}$ 鞍点高度约 $40\,\mathrm{kJ\,mol^{-1}}$、鞍点处 $r = 0.0930\,\mathrm{nm}$。

### 16.2.3. 势垒高度与零点能

势能剖面上鞍点与反应物谷底的势能差 $E_{\mathrm{b}}$ 是经典势垒，可以由量子化学算出。分子总有零点振动能，真正需要的能量是活化络合物与反应物各自零点能级之差：

$$
E_0 = E_{\mathrm{b}} + N_{\mathrm{A}}\left[\sum_i\tfrac12h\nu_i^{\ddagger} - \sum_j\tfrac12h\nu_j(\text{反应物})\right],
$$
其中活化络合物的求和不包括沿反应坐标的那个"振动"（它在鞍点处是虚频，16.3.1）。$E_0$ 是 0 K 时的活化能，同位素取代通过零点能改变 $E_0$，这是**动力学同位素效应**的主要来源（[6.1.13](/6.1.13)）；轻原子（H）还可以借**隧道效应**穿过能垒而不必越过它。

## 16.3. 过渡态理论

### 16.3.1. 基本假设与 Eyring 方程

过渡态理论（又称活化络合物理论）由 Eyring、Evans 与 Polanyi 在 1935 年提出。基本假设：

1. 反应物沿最小能量路径越过鞍点生成产物，鞍点附近的构型就是活化络合物 $\mathrm{X}^{\ddagger}$；
2. 活化络合物与反应物处于热力学平衡（准平衡），其浓度可以用统计热力学计算；
3. 越过鞍点的活化络合物不再返回，它分解为产物的速率就是反应速率。

对 $\ce{A + B-C <=> [A\cdots B\cdots C]^{\ddagger} -> A-B + C}$，三原子的线形活化络合物有 3 个平动、2 个转动、4 个振动自由度。四个振动中，两个弯曲振动与对称伸缩振动不导致分解；不对称伸缩振动（A–B 靠近时 B–C 拉长）沿反应坐标方向，它的一次"振动"就使络合物分解为产物。

由统计热力学（[6.3.11](/6.3.11) 末节由配分函数求平衡常数），以数密度表示的平衡常数为

$$
K_c^{\ddagger} = \frac{[\mathrm{X}^{\ddagger}]}{[\ce{A}][\ce{BC}]} = \frac{q^{\ddagger}/V}{(q_{\ce{A}}/V)(q_{\ce{BC}}/V)}\,\mathrm{e}^{-\varepsilon_0/k_{\mathrm{B}}T},
$$
其中 $q$ 是以各自基态为能量零点的**分子配分函数**，$\varepsilon_0 = E_0/N_{\mathrm{A}}$。从 $q^{\ddagger}$ 中分出沿反应坐标的振动（频率 $\nu$），它的**振动配分函数**在 $h\nu \ll k_{\mathrm{B}}T$（这一模式很"软"）时

$$
q_\nu = \frac{1}{1 - \mathrm{e}^{-h\nu/k_{\mathrm{B}}T}} \approx \frac{k_{\mathrm{B}}T}{h\nu}, \qquad q^{\ddagger} = \frac{k_{\mathrm{B}}T}{h\nu}q^{\ddagger\prime}.
$$
络合物以频率 $\nu$ 分解，$v = \nu[\mathrm{X}^{\ddagger}] = \nu K_c^{\ddagger}[\ce{A}][\ce{BC}]$，$\nu$ 消去：

$$
k = \frac{k_{\mathrm{B}}T}{h}\,\frac{q^{\ddagger\prime}/V}{(q_{\ce{A}}/V)(q_{\ce{BC}}/V)}\,\mathrm{e}^{-E_0/RT}.
$$

**定义 16.3.1（Eyring 方程）** 把去掉反应坐标的自由度之后的平衡常数记作 $K^{\ddagger}$，过渡态理论的速率常数

$$
k = \kappa\frac{k_{\mathrm{B}}T}{h}K^{\ddagger} \tag{16.2}
$$
称为 **Eyring 方程**。$\kappa$ 是透射系数，计入越过鞍点后又折回的轨迹（使 $\kappa < 1$）以及隧穿（使 $\kappa$ 可以大于 1），简单反应中常取 $\kappa = 1$。

普适因子 $k_{\mathrm{B}}T/h$ 在 $298\,\mathrm{K}$ 时为 $6.21 \times 10^{12}\,\mathrm{s^{-1}}$，是活化络合物越过能垒的频率尺度，与任何具体的分子性质无关。对一般基元反应，$k = \frac{k_{\mathrm{B}}T}{h}\frac{q^{\ddagger\prime}/V}{\prod_{\mathrm{B}}(q_{\mathrm{B}}/V)}\mathrm{e}^{-E_0/RT}$，按摩尔浓度计时每个反应物分子多一个因子 $N_{\mathrm{A}}$（双分子反应乘 $N_{\mathrm{A}}$）。

把"振动"当作反应坐标的处理并不严格（$h\nu \ll k_{\mathrm{B}}T$ 的极限是人为的）。更严格的推导把鞍点附近长为 $\delta$ 的一段反应坐标看作一维平动：其配分函数 $(2\pi m^{\ddagger}k_{\mathrm{B}}T)^{1/2}\delta/h$，络合物向产物方向的平均速率 $(k_{\mathrm{B}}T/2\pi m^{\ddagger})^{1/2}$，通过这段距离的速率常数为 $(k_{\mathrm{B}}T/2\pi m^{\ddagger})^{1/2}/\delta$，相乘后 $\delta$ 与 $m^{\ddagger}$ 都消去，同样得到 $k_{\mathrm{B}}T/h$。

**例 16.3.1（碰撞理论作为特例）** 两个原子 A、B 反应，活化络合物是核间距为 $d$ 的双原子分子。原子只有平动配分函数 $q_{\mathrm{t}}/V = (2\pi mk_{\mathrm{B}}T)^{3/2}/h^3$；络合物有质量 $m_{\mathrm{A}} + m_{\mathrm{B}}$ 的平动与转动惯量 $I = \mu d^2$ 的转动，$q_{\mathrm{r}} = 8\pi^2Ik_{\mathrm{B}}T/h^2$，唯一的振动就是反应坐标。代入，

$$
k = \frac{k_{\mathrm{B}}T}{h}\cdot\frac{8\pi^2\mu d^2k_{\mathrm{B}}T}{h^2}\cdot\frac{h^3}{(2\pi\mu k_{\mathrm{B}}T)^{3/2}}\,\mathrm{e}^{-E_0/RT} = \pi d^2\sqrt{\frac{8k_{\mathrm{B}}T}{\pi\mu}}\,\mathrm{e}^{-E_0/RT},
$$
正是硬球碰撞理论的结果式 (16.1)。对多原子分子，反应物的转动自由度在络合物中变成了振动，而振动配分函数（约 1–10）远小于转动配分函数（约 $10$–$100$ 每个自由度），所以过渡态理论给出的指前因子比碰撞理论小，粗略估计非线形分子之间的反应 $P \sim (q_{\mathrm{v}}/q_{\mathrm{r}})^5 \sim 10^{-5}$：方位因子由此得到了统计解释。

### 16.3.2. 热力学形式

由 $K^{\ddagger}$ 可以定义活化的热力学量。对 $n$ 分子反应，$K^{\ddagger}$ 以浓度表示，与量纲一的标准平衡常数的关系是 $K^{\ddagger} = K^{\ddagger\circ}(c^\circ)^{1-n}$。

**定义 16.3.2** 由 $\Delta^{\ddagger}G^\circ = -RT\ln K^{\ddagger\circ}$ 定义的量称为（标准摩尔）**活化 Gibbs 自由能**；由 $\Delta^{\ddagger}G^\circ = \Delta^{\ddagger}H^\circ - T\Delta^{\ddagger}S^\circ$ 分出的 $\Delta^{\ddagger}H^\circ$ 与 $\Delta^{\ddagger}S^\circ$ 分别称为**活化焓**与**活化熵**。它们是从反应物到活化络合物（去掉反应坐标）的标准摩尔变化。

代入 Eyring 方程（$\kappa = 1$），

$$
k = \frac{k_{\mathrm{B}}T}{h}(c^\circ)^{1-n}\exp\left(-\frac{\Delta^{\ddagger}G^\circ}{RT}\right) = \frac{k_{\mathrm{B}}T}{h}(c^\circ)^{1-n}\exp\left(\frac{\Delta^{\ddagger}S^\circ}{R}\right)\exp\left(-\frac{\Delta^{\ddagger}H^\circ}{RT}\right). \tag{16.3}
$$
气相反应若以 $p^\circ$ 为标准态，$(c^\circ)^{1-n}$ 换成 $(p^\circ/RT)^{1-n}$，相应的活化量数值不同，引用时必须说明标准态。

活化能与活化焓的关系可以这样求：对式 (16.2) 取对数求导，$E_{\mathrm{a}} = RT^2\frac{\mathrm{d}\ln k}{\mathrm{d}T} = RT + RT^2\frac{\mathrm{d}\ln K^{\ddagger}}{\mathrm{d}T}$。以浓度表示的平衡常数满足 $\frac{\mathrm{d}\ln K_c}{\mathrm{d}T} = \frac{\Delta U}{RT^2}$（理想体系），所以

$$
E_{\mathrm{a}} = \Delta^{\ddagger}U + RT = \Delta^{\ddagger}H - \Delta^{\ddagger}(pV) + RT.
$$
凝聚相中 $\Delta^{\ddagger}(pV) \approx 0$，$E_{\mathrm{a}} = \Delta^{\ddagger}H^\circ + RT$；理想气体中 $\Delta^{\ddagger}(pV) = \Delta^{\ddagger}\nu RT = (1 - n)RT$，$E_{\mathrm{a}} = \Delta^{\ddagger}H^\circ + nRT$。代回式 (16.3)，与 Arrhenius 方程比较得指前因子

$$
A = \frac{\mathrm{e}\,k_{\mathrm{B}}T}{h}(c^\circ)^{1-n}\mathrm{e}^{\Delta^{\ddagger}S^\circ/R}\ \ (\text{凝聚相}), \qquad A = \frac{\mathrm{e}^n k_{\mathrm{B}}T}{h}(c^\circ)^{1-n}\mathrm{e}^{\Delta^{\ddagger}S^\circ/R}\ \ (\text{气相}).
$$

指前因子由活化熵决定：活化络合物比反应物"有序"（双分子结合、成环、溶剂被极化而定向）时 $\Delta^{\ddagger}S^\circ < 0$，指前因子小；单分子分解中键变松、转动变自由时 $\Delta^{\ddagger}S^\circ > 0$。溶液中双分子缔合反应（如 Diels–Alder 反应）的 $\Delta^{\ddagger}S^\circ$ 常在 $-100$ 至 $-150\,\mathrm{J\,mol^{-1}\,K^{-1}}$；酶的作用之一就是把底物预先结合、定向，减少反应时的熵损失（[6.3.17](/6.3.17)）。

**例 16.3.2** $\ce{N2O5}$ 在 $\ce{CCl4}$ 中的一级分解，$298.15\,\mathrm{K}$ 时 $k = 4.69 \times 10^{-5}\,\mathrm{s^{-1}}$，$E_{\mathrm{a}} = 102\,\mathrm{kJ\,mol^{-1}}$（[6.1.7 的例 7.3.10](/6.1.7#ex-7.3.10)）。求活化 Gibbs 自由能、活化焓与活化熵。

**解** 单分子反应 $n = 1$，$(c^\circ)^{1-n} = 1$：

$$
\Delta^{\ddagger}G^\circ = RT\ln\frac{k_{\mathrm{B}}T}{hk} = 8.314 \times 298.15 \times \ln\frac{6.21 \times 10^{12}}{4.69 \times 10^{-5}}\,\mathrm{J\,mol^{-1}} = 97.7\,\mathrm{kJ\,mol^{-1}},
$$

$$
\Delta^{\ddagger}H^\circ = E_{\mathrm{a}} - RT = 99.5\,\mathrm{kJ\,mol^{-1}}, \qquad \Delta^{\ddagger}S^\circ = \frac{\Delta^{\ddagger}H^\circ - \Delta^{\ddagger}G^\circ}{T} = +6\,\mathrm{J\,mol^{-1}\,K^{-1}}.
$$
活化熵很小，接近零而略正，符合活化络合物结构与反应物相近、只有一个键开始松弛的单分子分解。

### 16.3.3. 三种处理的比较

| | Arrhenius 方程 | 碰撞理论 | 过渡态理论 |
|---|---|---|---|
| 速率常数 | $A\mathrm{e}^{-E_{\mathrm{a}}/RT}$ | $PN_{\mathrm{A}}\pi d_{\mathrm{AB}}^2\bar v_{\mathrm{rel}}\mathrm{e}^{-E_{\mathrm{c}}/RT}$ | $\frac{k_{\mathrm{B}}T}{h}(c^\circ)^{1-n}\mathrm{e}^{\Delta^{\ddagger}S^\circ/R}\mathrm{e}^{-\Delta^{\ddagger}H^\circ/RT}$ |
| 能量参数 | $E_{\mathrm{a}}$（经验） | $E_{\mathrm{c}} = E_{\mathrm{a}} - \frac12RT$ | $\Delta^{\ddagger}H^\circ = E_{\mathrm{a}} - RT$（凝聚相）或 $E_{\mathrm{a}} - nRT$（气相） |
| 指前因子的来源 | 经验 | 碰撞数 × 方位因子 | 活化熵（配分函数） |
| 能算什么 | 只是拟合 | 无结构分子的数量级 | 原则上由势能面与分子常数算出全部 |

过渡态理论的优点：形象地描述了基元反应的过程；原则上可以从分子结构与光谱数据计算速率常数；对指前因子给出了统计解释（活化熵）；说明了反应为什么需要活化能。缺点与改进：准平衡与"不返回"假设并不总成立（透射系数，变分过渡态理论把分割面放在使速率最小的位置）；不计量子效应（隧穿使低温下的 $k$ 比预测大，轻原子转移中尤其明显）；多原子体系的势能面计算困难。尽管如此，过渡态理论至今仍是讨论化学反应速率的基本语言，有机化学与酶学中的活化参数、Hammond 假设、过渡态类似物抑制剂都以它为基础。

## 16.4. 单分子反应理论

### 16.4.1. 实验事实

**定义 16.4.1** 只有一个反应物分子参与、通过分解或异构化生成产物的基元反应称为**单分子反应**，如环丙烷异构化为丙烯、$\ce{C2H5F -> C2H4 + HF}$、$\ce{N2O5}$ 的分解。

气相单分子反应在高压下是一级反应，在低压下却变为二级反应，速率常数在中间压力区逐渐下降（降变区，fall-off）。这类反应的活化能一般大于 $150\,\mathrm{kJ\,mol^{-1}}$，这样大的能量从哪里来、为什么级数随压力变化，需要一个理论解释。

### 16.4.2. Lindemann 机理

**定义 16.4.2（Lindemann 机理）** 1922 年 Lindemann 提出：反应物分子 A 通过与其他分子 M（可以是 A 本身或惰性气体）碰撞而被活化为高能分子 $\ce{A^*}$，$\ce{A^*}$ 或在下一次碰撞中失活，或经过一段时滞后分解为产物：

$$
\ce{A + M <=>[k_1][k_{-1}] A^* + M}, \qquad \ce{A^* ->[k_2] P}.
$$

时滞是 $\ce{A^*}$ 把获得的能量在分子内部重新分配、集中到要断裂的键上所需的时间。对 $\ce{A^*}$ 用**稳态近似**（[6.3.15](/6.3.15#def-15.6.1)）：

$$
\frac{\mathrm{d}[\ce{A^*}]}{\mathrm{d}t} = k_1[\ce{A}][\ce{M}] - k_{-1}[\ce{A^*}][\ce{M}] - k_2[\ce{A^*}] = 0, \qquad [\ce{A^*}] = \frac{k_1[\ce{A}][\ce{M}]}{k_{-1}[\ce{M}] + k_2},
$$

$$
v = k_2[\ce{A^*}] = k_{\mathrm{uni}}[\ce{A}], \qquad k_{\mathrm{uni}} = \frac{k_1k_2[\ce{M}]}{k_{-1}[\ce{M}] + k_2}. \tag{16.4}
$$

- 高压（$k_{-1}[\ce{M}] \gg k_2$）：$k_{\mathrm{uni}} \to k_\infty = \frac{k_1k_2}{k_{-1}}$，一级反应。活化与失活很快，$\ce{A^*}$ 与 A 处于前平衡，分解是速控步。
- 低压（$k_{-1}[\ce{M}] \ll k_2$）：$k_{\mathrm{uni}} \to k_1[\ce{M}]$；当 M 就是 A 时 $v = k_1[\ce{A}]^2$，二级反应。几乎每个被活化的分子都来得及分解，活化碰撞是速控步。

所以单分子反应不是"自发"的，分子仍需通过碰撞获得能量。式 (16.4) 可写成

$$
\frac{k_{\mathrm{uni}}}{k_\infty} = \frac{1}{1 + k_2/(k_{-1}[\ce{M}])} = \frac{1}{1 + p_{1/2}/p}, \qquad \frac{1}{k_{\mathrm{uni}}} = \frac{1}{k_\infty} + \frac{1}{k_1[\ce{M}]},
$$
其中 $k_{\mathrm{uni}} = k_\infty/2$ 时的压力 $p_{1/2}$ 满足 $k_{-1}[\ce{M}]_{1/2} = k_2$。第二式说明 $1/k_{\mathrm{uni}}$ 对 $1/p$ 应是直线（Lindemann 作图），截距 $1/k_\infty$，斜率给出 $k_1$。

![Lindemann 机理：左为降变曲线 kuni/k∞ 随 p/p1/2 的变化（低压二级、高压一级）；右为 Lindemann 作图，1/kuni 对 1/[M] 呈直线](./plots/lindemann-falloff.py)

偶氮甲烷在 $603\,\mathrm{K}$ 的热分解、环丙烷的异构化等都显示了这种降变。第三体的效率与其分子大小有关：多原子分子一次碰撞能交换更多能量。双原子复合 $\ce{I + I + M -> I2 + M}$ 是它的逆过程：两个原子结合放出的能量必须由第三体带走，否则新生成的分子在一次振动内又会解离。

### 16.4.3. RRK 与 RRKM 理论

Lindemann 机理定性上正确，定量上却有两个问题：用碰撞理论估计 $k_1$（只考虑沿连心线的两个平方项能量），得到的 $p_{1/2}$ 比实验值大几个数量级；实验的 $1/k_{\mathrm{uni}}$–$1/p$ 图也不是直线。改进的关键在于认识到分子的能量可以储存在许多振动模式中：

- Hinshelwood 指出，能量分布在 $s$ 个振动模式中时，分子能量超过 $E_0$ 的概率近似为 $\frac{1}{(s-1)!}\left(\frac{E_0}{k_{\mathrm{B}}T}\right)^{s-1}\mathrm{e}^{-E_0/k_{\mathrm{B}}T}$，比只考虑两个平方项大得多，$k_1$ 因此增大。
- Rice、Ramsperger 与 Kassel（RRK，1927–1928）进一步指出，$k_2$ 依赖于 $\ce{A^*}$ 的能量 $E$：能量在 $s$ 个振子之间随机流动，集中到反应坐标上超过 $E_0$ 的概率为 $(1 - E_0/E)^{s-1}$，$k_2(E) = \nu(1 - E_0/E)^{s-1}$。能量越高的分子分解越快，降变曲线因此比 Lindemann 的预测更宽。

**定义 16.4.3** Marcus（1952）把 RRK 的思想与过渡态理论结合，用活化络合物在能量 $E$ 下可及的量子态数与反应物的态密度之比计算微观速率常数 $k_2(E) = \frac{N^{\ddagger}(E - E_0)}{h\rho(E)}$，再对 $\ce{A^*}$ 的能量分布积分得到 $k_{\mathrm{uni}}(p, T)$，这一理论称为 **RRKM 理论**（Rice–Ramsperger–Kassel–Marcus 理论）。

RRKM 理论的核心假设是分子内的能量重新分配远快于反应（统计假设），它能定量地预测降变曲线，至今仍是燃烧与大气化学中计算压力相关速率常数的标准方法，也用于质谱中离子碎裂的分析。

## 16.5. 分子反应动态学简介

**定义 16.5.1** 从单次分子碰撞出发，研究反应概率与碰撞能量、取向的关系，能量在反应中怎样交换与分配，以及产物在各平动、转动、振动状态上的分布的学科称为**分子反应动态学**。确定量子态 $i$ 的 A 与确定量子态 $j$ 的 BC 反应，生成确定量子态 $m$、$n$ 的产物，

$$
\mathrm{A}(i) + \mathrm{BC}(j) \to \mathrm{AB}(m) + \mathrm{C}(n),
$$
这样的反应称为**态–态反应**。

宏观速率常数是态–态反应截面对各种能量与状态的平均（16.1.3 是其最简单的例子），平均会丢掉大部分微观信息。研究态–态反应的主要实验方法有：

**定义 16.5.2** 把两束速率与量子态经过选择的分子束在高真空（约 $10^{-4}\,\mathrm{Pa}$，分子的平均自由程达数十米）中交叉，使分子只发生单次碰撞，用可转动的质谱检测器测量产物在不同散射角的通量与速率分布的方法称为**交叉分子束**。

由实验坐标系变换到质心坐标系，得到产物的"通量–速率–角度"等高图，它直接显示碰撞的动态：

- 抢夺模型：$\ce{K + I2 -> KI + I}$ 中 K 在较大的碰撞参数下从 $\ce{I2}$ 夺走一个 I 原子并继续向前，产物 KI 向前散射（这也是鱼叉机理，反应截面很大）。
- 回弹模型：$\ce{K + CH3I -> KI + CH3}$ 中只有近乎迎头的碰撞才反应，KI 向后弹回。
- 络合物模型：$\ce{Cs + RbCl -> CsCl + Rb}$ 中形成的中间络合物寿命为转动周期的几倍，转动若干圈后失去对入射方向的"记忆"，产物在质心坐标中前后对称地散射。

直接反应的碰撞时间短于转动周期（约 $10^{-12}\,\mathrm{s}$），能量来不及在分子内重新分配，这与 RRKM 的统计假设恰好相反。另外两种方法是红外化学发光（反应生成的振动、转动激发态产物在低压下发射红外辐射，由光谱推出产物的初始能态分布）与激光诱导荧光（用可调激光把某一振动、转动能级上的产物激发到上一电子态，测其荧光）。

这些实验给出了反应动态与势能面形状的联系，称为 Polanyi 规则（Polanyi rules）：能垒位于反应物一侧（早能垒）的放热反应，平动能更有利于越过能垒，放出的能量多以产物的振动能出现（因此可以用于化学激光器）；能垒位于产物一侧（晚能垒）时，反应物的振动能更有效。Herschbach、李远哲（交叉分子束）与 Polanyi（红外化学发光）因此获得 1986 年 Nobel 化学奖；Zewail 用飞秒激光直接观察化学键断裂与过渡态区域的运动（飞秒化学），获 1999 年 Nobel 化学奖。

## 小结

| 内容 | 要点 |
|---|---|
| 碰撞数 | $Z_{\mathrm{AB}} = \pi d_{\mathrm{AB}}^2\bar v_{\mathrm{rel}}n_{\mathrm{A}}n_{\mathrm{B}}$，$\bar v_{\mathrm{rel}} = \sqrt{8k_{\mathrm{B}}T/\pi\mu}$ |
| 反应截面 | $\sigma_{\mathrm{r}} = \pi d_{\mathrm{AB}}^2(1 - \varepsilon_{\mathrm{c}}/\varepsilon)$；对 Maxwell–Boltzmann 分布积分得 $k = \pi d_{\mathrm{AB}}^2\bar v_{\mathrm{rel}}\mathrm{e}^{-E_{\mathrm{c}}/RT}$ |
| 碰撞理论与 Arrhenius | $E_{\mathrm{a}} = E_{\mathrm{c}} + \frac12RT$；$P$ 无法计算 |
| 势能面 | 反应物谷、产物谷、鞍点、最小能量路径；$E_0 = E_{\mathrm{b}} + \Delta(\text{零点能})$ |
| Eyring 方程 | $k = \kappa\frac{k_{\mathrm{B}}T}{h}K^{\ddagger}$，$K^{\ddagger}$ 由配分函数计算（去掉反应坐标） |
| 热力学形式 | $k = \frac{k_{\mathrm{B}}T}{h}(c^\circ)^{1-n}\mathrm{e}^{\Delta^{\ddagger}S^\circ/R}\mathrm{e}^{-\Delta^{\ddagger}H^\circ/RT}$；$E_{\mathrm{a}} = \Delta^{\ddagger}H^\circ + RT$（凝聚相）、$+nRT$（气相） |
| 单分子反应 | Lindemann：$k_{\mathrm{uni}} = \frac{k_1k_2[\ce{M}]}{k_{-1}[\ce{M}] + k_2}$，高压一级、低压二级；RRKM 计入能量在振动模式间的分配 |
| 分子反应动态学 | 态–态反应；交叉分子束（抢夺、回弹、络合物）、红外化学发光、激光诱导荧光 |

## 思考题

1. 为什么碰撞理论的有效碰撞分数是 $\mathrm{e}^{-E_{\mathrm{c}}/RT}$，而不是相对平动能超过 $E_{\mathrm{c}}$ 的分子对的分数？

   **答** 见 16.1.3：通量加权与反应截面的能量依赖合起来，恰好给出 Boltzmann 因子。

2. 过渡态理论的速率常数中，$k_{\mathrm{B}}T/h$ 的物理意义是什么？它为什么与分子种类无关？

   **答** 它是活化络合物沿反应坐标越过鞍点的频率尺度；推导中反应坐标的频率（或质量）恰好消去。

3. 单分子反应在低压下变为二级，这是否说明它变成了双分子反应？

   **答** 不是。速控步从分解变为活化碰撞，后者是双分子的；分解这一步始终是单分子的。
