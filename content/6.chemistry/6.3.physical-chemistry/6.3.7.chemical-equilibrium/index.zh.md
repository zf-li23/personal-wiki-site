---
title: 化学平衡
---

[6.1.8](/6.1.8) 从经验平衡常数出发，借助理想气体与稀溶液的近似写出了**化学反应等温式**与 $\Delta_{\mathrm{r}}G^\circ_{\mathrm{m}} = -RT\ln K^\circ$，并讨论了浓度、压力、温度对平衡的影响。有了**化学势**（[6.3.4](/6.3.4)）与**活度**（[6.3.6](/6.3.6)），这些结论可以对任意系统严格导出。本章回答三个问题：为什么化学反应一般不能进行到底，平衡的条件是什么（7.1）；标准平衡常数如何由化学势定义，它对气体、溶液与多相反应分别是什么形式（7.2–7.3）；$\Delta_{\mathrm{r}}G^\circ_{\mathrm{m}}$ 怎样求、怎样用（7.4）。然后在严格的框架下重新讨论平衡的移动，包括 $\Delta_{\mathrm{r}}C_p \ne 0$ 时的 van 't Hoff 方程、高压下的逸度修正与 Le Chatelier 原理的准确表述（7.5），最后讨论同时平衡与耦合反应，以 ATP 水解驱动的生化反应为例（7.6）。

本章沿用 [6.1.8](/6.1.8) 的记号：反应写作 $0 = \sum_{\mathrm{B}}\nu_{\mathrm{B}}\mathrm{B}$（**化学计量数** $\nu_{\mathrm{B}}$ 对产物为正、对反应物为负），**反应进度**为 $\xi$，任意状态下的活度积（**反应商**）记作 $Q$（不少教材记作 $J$）。$Q$ 与热量同形，本章中不出现热量，不致混淆。

## 7.1. 化学反应的平衡条件

### 7.1.1. 反应为什么不能进行到底

考虑等温等压下的理想气体反应 $\mathrm{A(g)} \ce{<=>} \mathrm{B(g)}$，从 $1\,\mathrm{mol}$ A 出发，反应进度为 $\xi$ 时系统的 Gibbs 自由能为

$$
G(\xi) = (1 - \xi)\mu_{\mathrm{A}} + \xi\mu_{\mathrm{B}} = \underbrace{(1 - \xi)\mu^*_{\mathrm{A}} + \xi\mu^*_{\mathrm{B}}}_{\text{纯物质，不混合}} + \underbrace{RT[(1 - \xi)\ln(1 - \xi) + \xi\ln\xi]}_{\Delta_{\mathrm{mix}}G},
$$
其中 $\mu^*_{\mathrm{B}}$ 是纯 B 在 $T$、$p$ 下的化学势，第二项用了理想气体混合物中 $\mu_{\mathrm{B}} = \mu^*_{\mathrm{B}} + RT\ln x_{\mathrm{B}}$（[6.3.4](/6.3.4)）。第一项是 $\xi$ 的线性函数：如果反应物与产物始终各自保持纯态，$G$ 沿直线单调变化，反应要么进行到底，要么完全不进行。第二项是混合 Gibbs 自由能（[6.3.5](/6.3.5)），在 $0 < \xi < 1$ 内为负，且在两端的斜率分别为 $-\infty$ 与 $+\infty$。两者相加，$G(\xi)$ 在 $0 < \xi < 1$ 内部必有极小。所以，只要反应物与产物能够混合，反应就停在两者共存的某一组成：化学平衡是混合熵的结果。

![理想气体异构化 A ⇌ B（ΔrG° = −3.0 kJ/mol，298.15 K，p°）的 G(ξ)：虚线为不混合时的直线，点线为混合 Gibbs 自由能，两者之和在 ξ = K°/(1 + K°) 处取极小](./plots/gibbs-mixing-extent.py)

反应物与产物不能混合时情形不同。$\ce{CaCO3(s) <=> CaO(s) + CO2(g)}$ 中两种固体是各自独立的纯相，在给定的 $T$ 与 $p_{\ce{CO2}}$ 下 $G$ 随 $\xi$ 线性变化：$p_{\ce{CO2}}$ 低于分解压（7.2.3）时 $\ce{CaCO3}$ 分解完全，高于分解压时完全不分解，只有恰好等于分解压时三相才能共存。

### 7.1.2. 摩尔反应 Gibbs 自由能

一般地，对只做体积功的多组分封闭系统，$\mathrm{d}G = -S\,\mathrm{d}T + V\,\mathrm{d}p + \sum_{\mathrm{B}}\mu_{\mathrm{B}}\,\mathrm{d}n_{\mathrm{B}}$（[6.3.4](/6.3.4)）。反应进度改变 $\mathrm{d}\xi$ 时 $\mathrm{d}n_{\mathrm{B}} = \nu_{\mathrm{B}}\,\mathrm{d}\xi$，等温等压下 $\mathrm{d}G = \left(\sum_{\mathrm{B}}\nu_{\mathrm{B}}\mu_{\mathrm{B}}\right)\mathrm{d}\xi$。

**定义 7.1.1（摩尔反应 Gibbs 自由能）** 等温等压、无非体积功时系统 Gibbs 自由能随反应进度的变化率

$$
\Delta_{\mathrm{r}}G_{\mathrm{m}} = \left(\frac{\partial G}{\partial\xi}\right)_{T,p} = \sum_{\mathrm{B}}\nu_{\mathrm{B}}\mu_{\mathrm{B}} \tag{7.1}
$$
称为**摩尔反应 Gibbs 自由能**，单位 $\mathrm{J\,mol^{-1}}$。

它有两种理解：$G$–$\xi$ 曲线在当前组成处的斜率；或者，在一个无限大的系统中进行 $1\,\mathrm{mol}$ 反应进度（组成不变）时 $G$ 的变化。符号 $\Delta$ 不表示"始态与终态之差"：$\Delta_{\mathrm{r}}G_{\mathrm{m}}$ 是系统当前状态（$T$、$p$ 与组成）的函数，是状态量，不是过程量。

由 Gibbs 判据，等温等压、无非体积功时：

$$
\Delta_{\mathrm{r}}G_{\mathrm{m}} < 0：\text{反应正向自发}; \qquad \Delta_{\mathrm{r}}G_{\mathrm{m}} = 0：\text{平衡}; \qquad \Delta_{\mathrm{r}}G_{\mathrm{m}} > 0：\text{逆向自发}.
$$

### 7.1.3. 平衡条件

**定理 7.1.1** 化学反应达到平衡的条件是

$$
\sum_{\mathrm{B}}\nu_{\mathrm{B}}\mu_{\mathrm{B}}^{\mathrm{eq}} = 0. \tag{7.2}
$$
它不仅适用于等温等压，也适用于等温等容等其他约束条件，并且适用于多相反应。

**证明** 等温等压时由式 (7.1) 与 $G$ 取极小即得。等温等容时用 Helmholtz 自由能，$\mathrm{d}A = -S\,\mathrm{d}T - p\,\mathrm{d}V + \sum_{\mathrm{B}}\mu_{\mathrm{B}}\,\mathrm{d}n_{\mathrm{B}}$，平衡时 $A$ 取极小，$(\partial A/\partial\xi)_{T,V} = \sum_{\mathrm{B}}\nu_{\mathrm{B}}\mu_{\mathrm{B}} = 0$，条件相同。孤立系统中用 $\mathrm{d}S = \frac{1}{T}\mathrm{d}U + \frac{p}{T}\mathrm{d}V - \frac{1}{T}\sum_{\mathrm{B}}\mu_{\mathrm{B}}\,\mathrm{d}n_{\mathrm{B}}$ 与熵极大，也得到同一条件。多相系统中，同一物质在它存在的各相中化学势相等（**相平衡**条件，[6.3.8](/6.3.8)），所以式中 $\mu_{\mathrm{B}}$ 取哪一相的值都一样。$\square$

约束条件只决定哪一个热力学势取极值，不改变平衡条件本身：式 (7.2) 是平衡态的性质。不同约束下的区别在于平衡的位置（例如恒压与恒容下的平衡组成不同）。

## 7.2. 标准平衡常数与化学反应等温式

### 7.2.1. 由化学势导出

把化学势的通式 $\mu_{\mathrm{B}} = \mu^\circ_{\mathrm{B}}(T) + RT\ln a_{\mathrm{B}}$（[6.3.6](/6.3.6) 式 (6.3)，凝聚相的压力项已略去）代入式 (7.1)：

$$
\Delta_{\mathrm{r}}G_{\mathrm{m}} = \sum_{\mathrm{B}}\nu_{\mathrm{B}}\mu^\circ_{\mathrm{B}} + RT\sum_{\mathrm{B}}\nu_{\mathrm{B}}\ln a_{\mathrm{B}}.
$$

**定义 7.2.1（标准摩尔反应 Gibbs 自由能）** 

$$
\Delta_{\mathrm{r}}G^\circ_{\mathrm{m}}(T) = \sum_{\mathrm{B}}\nu_{\mathrm{B}}\mu^\circ_{\mathrm{B}}(T)
$$
称为反应的**标准摩尔反应 Gibbs 自由能**：各物质都处于各自的标准态时，进行 $1\,\mathrm{mol}$ 反应进度的 Gibbs 自由能变化。

$\Delta_{\mathrm{r}}G^\circ_{\mathrm{m}}$ 只依赖于温度，以及两个"主观"的选择：各物质标准态的选法、反应方程式的写法（$\nu_{\mathrm{B}}$）。

**定理 7.2.1（化学反应等温式）** 任意化学反应在任意状态下

$$
\Delta_{\mathrm{r}}G_{\mathrm{m}} = \Delta_{\mathrm{r}}G^\circ_{\mathrm{m}} + RT\ln Q, \qquad Q = \prod_{\mathrm{B}}a_{\mathrm{B}}^{\nu_{\mathrm{B}}}. \tag{7.3}
$$

平衡时 $\Delta_{\mathrm{r}}G_{\mathrm{m}} = 0$，$Q$ 等于一个只与温度有关的常数：

**定义 7.2.2（标准平衡常数）** 

$$
K^\circ(T) = \exp\left(-\frac{\Delta_{\mathrm{r}}G^\circ_{\mathrm{m}}}{RT}\right) = \prod_{\mathrm{B}}\left(a_{\mathrm{B}}^{\mathrm{eq}}\right)^{\nu_{\mathrm{B}}}. \tag{7.4}
$$

第一个等号是 $K^\circ$ 的热力学定义，第二个等号是它与平衡组成的关系。这一推导不依赖于反应的机理，也不需要假定气体或溶液是理想的：非理想性全部包含在活度中。代回式 (7.3)，

$$
\Delta_{\mathrm{r}}G_{\mathrm{m}} = RT\ln\frac{Q}{K^\circ}:
$$
$Q < K^\circ$ 时正向自发，$Q = K^\circ$ 时平衡，$Q > K^\circ$ 时逆向自发（等温等压或等温等容都可用）。

若保留凝聚相化学势中的压力项 $\int_{p^\circ}^{p}V^{\mathrm{ref}}_{\mathrm{B}}\,\mathrm{d}p$，平衡关系严格地写作 $K^\circ = \prod_{\mathrm{B}}(a_{\mathrm{B}}^{\mathrm{eq}})^{\nu_{\mathrm{B}}}\exp\left(\sum_{\mathrm{B}}\nu_{\mathrm{B}}\int_{p^\circ}^{p}V^{\mathrm{ref}}_{\mathrm{B}}\,\mathrm{d}p/RT\right)$，后一因子在压力不很高时与 1 相差极小（例如水溶液反应在 $10\,\mathrm{MPa}$、$\sum\nu_{\mathrm{B}}V_{\mathrm{B}} = 20\,\mathrm{cm^3\,mol^{-1}}$ 时为 $1.08$）。深海与高压生物化学中这一项不能忽略。

$K^\circ$ 的性质：

1. 量纲一，只是温度的函数，与压力和组成无关（标准态的压力固定为 $p^\circ$）。
2. 与标准态的选择有关：溶液反应中溶质用 $x$、$b$ 或 $c$ 标度时 $K^\circ$ 数值不同（7.2.2）。
3. 与方程式的写法有关：方程式乘以 $n$，$\Delta_{\mathrm{r}}G^\circ_{\mathrm{m}}$ 乘以 $n$，$K^\circ$ 变为 $n$ 次方；正逆反应的 $K^\circ$ 互为倒数；反应相加，$K^\circ$ 相乘（[6.1.8](/6.1.8#thm-8.2.1)）。所以给出 $K^\circ$ 时必须同时给出方程式、温度，溶液反应还要注明标准态。

### 7.2.2. 各类反应的标准平衡常数

$K^\circ$ 的定义是唯一的，它与平衡组成的具体关系随系统而定：

| 系统 | 活度 | $K^\circ$ |
|---|---|---|
| 理想气体 | $p_{\mathrm{B}}/p^\circ$ | $\prod(p_{\mathrm{B}}/p^\circ)^{\nu_{\mathrm{B}}}$，平衡分压积 |
| 实际气体 | $f_{\mathrm{B}}/p^\circ = \varphi_{\mathrm{B}}p_{\mathrm{B}}/p^\circ$ | $\prod(\varphi_{\mathrm{B}}p_{\mathrm{B}}/p^\circ)^{\nu_{\mathrm{B}}}$，平衡逸度积 |
| 理想液态混合物 | $x_{\mathrm{B}}$ | $\prod x_{\mathrm{B}}^{\nu_{\mathrm{B}}}$ |
| 理想稀溶液（各物种都是溶质） | $x_{\mathrm{B}}$、$b_{\mathrm{B}}/b^\circ$ 或 $c_{\mathrm{B}}/c^\circ$ | $\prod x_{\mathrm{B}}^{\nu_{\mathrm{B}}}$、$\prod(b_{\mathrm{B}}/b^\circ)^{\nu_{\mathrm{B}}}$ 或 $\prod(c_{\mathrm{B}}/c^\circ)^{\nu_{\mathrm{B}}}$ |
| 实际溶液 | $\gamma_{\mathrm{B}}x_{\mathrm{B}}$ 等 | 平衡活度积 |
| 有纯固体、纯液体参加 | 纯凝聚相 $a = 1$ | 只含气体与溶液中的物种 |

几点说明：

- 溶液中溶剂（如水）作为反应物或产物时，按 Raoult 定律 $a_{\ce{H2O}} = \gamma_{\mathrm{A}}x_{\mathrm{A}} \approx 1$，所以稀水溶液中它不写入 $K^\circ$；浓溶液或非水溶剂中则不能省略（[6.1.8](/6.1.8#sec-8.2.2)）。
- 同一溶液反应用不同的溶质标度，$K^\circ$ 之间的换算由 $\mu^\circ_{b,\mathrm{B}} = \mu^\circ_{x,\mathrm{B}} + RT\ln(M_{\mathrm{A}}b^\circ)$（[6.3.5](/6.3.5)）得到：$K^\circ_x = K^\circ_b(M_{\mathrm{A}}b^\circ)^{\sum\nu_{\mathrm{B}}}$，求和只对溶质进行。水溶液中 $K^\circ$ 通常按 $b^\circ = 1\,\mathrm{mol\,kg^{-1}}$（或 $c^\circ$）给出，这也是热力学数据表中水合物种所用的标准态。
- 纯固体的活度为 1，严格的理由是：它的参考态就是同温同压下的纯固体本身，$\mu^*_{\mathrm{B}}(\mathrm{s}, T, p) = \mu^\circ_{\mathrm{B}}(\mathrm{s}, T) + \int_{p^\circ}^{p}V^*_{\mathrm{m}}\,\mathrm{d}p$，与 $\mu^\circ + RT\ln a$ 比较，压力项可略时 $a = 1$。

例如：

$$
\ce{NH4Cl(s) <=> NH3(g) + HCl(g)}: \quad K^\circ = \frac{p_{\ce{NH3}}}{p^\circ}\cdot\frac{p_{\ce{HCl}}}{p^\circ}; \qquad \ce{C2H4(g) + H2O(l) <=> C2H5OH(aq)}: \quad K^\circ = \frac{a_{b}(\ce{C2H5OH})}{p_{\ce{C2H4}}/p^\circ}.
$$
后者是气相、液相与溶液的多相平衡：乙烯按理想气体，水是溶剂（$a \approx 1$），乙醇按 $b$ 标度的溶质。

### 7.2.3. 分解压

**定义 7.2.3** 一定温度下，纯凝聚态物质分解为气体（与其他纯凝聚相）的反应达到平衡时，气体产物的分压之和称为该物质的**分解压**。

由于凝聚相的活度为 1，$K^\circ$ 只含气体的分压，分解压在一定温度下有定值。$\ce{CaCO3}$ 的分解压就是平衡时 $\ce{CO2}$ 的压力，$K^\circ = p_{\ce{CO2}}/p^\circ$；$\ce{NH4Cl}$ 分解生成等量的两种气体，分解压 $p = 2p_{\ce{NH3}}$，$K^\circ = (p/2p^\circ)^2$。分解压等于外压（如 $101.325\,\mathrm{kPa}$）时的温度称为分解温度。

**例 7.2.1** 由 $298.15\,\mathrm{K}$ 的 $\Delta_{\mathrm{f}}G^\circ$（$\ce{NH4Cl}$(s) $-202.9$，$\ce{NH3}$(g) $-16.4$，HCl(g) $-95.3\,\mathrm{kJ\,mol^{-1}}$，CRC Handbook）求 $\ce{NH4Cl}$ 在 $298.15\,\mathrm{K}$ 的分解压。

**解** $\Delta_{\mathrm{r}}G^\circ_{\mathrm{m}} = -16.4 - 95.3 + 202.9 = 91.2\,\mathrm{kJ\,mol^{-1}}$，$K^\circ = \exp(-91200/(8.314 \times 298.15)) = 1.05 \times 10^{-16}$，$p = 2\sqrt{K^\circ}\,p^\circ = 2.1 \times 10^{-8}\,\mathrm{bar} = 2\,\mathrm{mPa}$。常温下 $\ce{NH4Cl}$ 几乎不分解；它加热时"升华"（约 $610\,\mathrm{K}$ 起分解压达到 $1\,\mathrm{atm}$），在冷处重新化合成固体。

### 7.2.4. 经验平衡常数

用平衡分压、摩尔分数或浓度直接写出的乘积 $K_p = \prod p_{\mathrm{B}}^{\nu_{\mathrm{B}}}$、$K_x = \prod x_{\mathrm{B}}^{\nu_{\mathrm{B}}}$、$K_c = \prod c_{\mathrm{B}}^{\nu_{\mathrm{B}}}$ 称为经验**平衡常数**（[6.1.8](/6.1.8#def-8.2.1)），一般有单位。对理想气体反应，记 $\Delta\nu_{\mathrm{g}} = \sum_{\mathrm{B(g)}}\nu_{\mathrm{B}}$，

$$
K^\circ = K_p(p^\circ)^{-\Delta\nu_{\mathrm{g}}} = K_x\left(\frac{p}{p^\circ}\right)^{\Delta\nu_{\mathrm{g}}} = K_c\left(\frac{c^\circ RT}{p^\circ}\right)^{\Delta\nu_{\mathrm{g}}}. \tag{7.5}
$$
$K^\circ$、$K_p$、$K_c$ 只与温度有关；$K_x$ 还与总压有关（$\Delta\nu_{\mathrm{g}} \ne 0$ 时），压力正是通过它影响平衡组成（7.5.2）。实际气体的 $K_p$ 不再是常数，随压力变化。

## 7.3. 平衡组成的计算

衡量平衡位置的量有两个：平衡**转化率**（某反应物平衡时已转化的量占投入量的分数）与平衡产率（平衡时某产物的量占原料全部转化时理论产量的分数）。有副反应时两者不同：转化的原料不一定全部变成所需产物。

计算平衡组成的步骤：(1) 用反应进度 $\xi$ 写出各物质的量与总量；(2) 写出活度（分压、摩尔分数等）；(3) 代入 $K^\circ$ 得到关于 $\xi$ 的方程并求解。方程一般是高次的，用数值求根最方便：$\xi$ 的取值范围由各物质的量非负确定，在该区间内 $\ln Q(\xi)$ 单调增加（7.5.4），所以根唯一，可以用 `scipy.optimize.brentq` 在区间端点之间求根（[4.4.4](/4.4.4#sec-4.2.2)）。有几个独立反应时变量是几个反应进度，用 `scipy.optimize.fsolve` 解联立方程，或直接对 $G$ 求约束极小（7.6.1）。

```python
from scipy.optimize import brentq

K = 6.4e-3          # 1/2 N2 + 3/2 H2 <=> NH3 at 723 K
def residual(x, p):  # x = mol N2 reacted from 1 N2 + 3 H2; p in bar
    return 2 * x * (4 - 2 * x) / (3**1.5 * (1 - x)**2) / p - K

for p in (1, 300):
    x = brentq(residual, 1e-12, 1 - 1e-12, args=(p,))
    print(p, x, 2 * x / (4 - 2 * x))   # conversion and NH3 mole fraction
```

## 7.4. 标准摩尔反应 Gibbs 自由能

### 7.4.1. 意义与 $\Delta_{\mathrm{r}}G_{\mathrm{m}}$ 的区别

| | $\Delta_{\mathrm{r}}G_{\mathrm{m}} = \sum\nu_{\mathrm{B}}\mu_{\mathrm{B}}$ | $\Delta_{\mathrm{r}}G^\circ_{\mathrm{m}} = \sum\nu_{\mathrm{B}}\mu^\circ_{\mathrm{B}} = -RT\ln K^\circ$ |
|---|---|---|
| 意义 | 当前组成下反应的推动力 | 各物质都在标准态时的推动力；决定平衡的位置 |
| 依赖 | $T$、$p$、组成 | 只依赖 $T$（与标准态、方程式写法） |
| 平衡时 | 等于零 | 一般不为零 |
| 用途 | 判断方向 | 计算 $K^\circ$；粗估反应的可能性 |

两个常见的误解：$\Delta_{\mathrm{r}}G^\circ_{\mathrm{m}}$ 不是"平衡时的 $\Delta_{\mathrm{r}}G_{\mathrm{m}}$"（平衡时后者为零）；在 $101.325\,\mathrm{kPa}$（甚至 $p^\circ$）下进行的气相反应，其 $\Delta_{\mathrm{r}}G_{\mathrm{m}}$ 也不等于 $\Delta_{\mathrm{r}}G^\circ_{\mathrm{m}}$，因为标准态要求每种气体单独处于 $p^\circ$，而混合物中各组分的分压小于总压。同理，$\Delta_{\mathrm{r}}G^\circ_{\mathrm{m}}$ 也不能写成 $(\partial G/\partial\xi)_{T,p^\circ}$。

### 7.4.2. 求法

1. 由 $\Delta_{\mathrm{r}}G^\circ_{\mathrm{m}} = \Delta_{\mathrm{r}}H^\circ_{\mathrm{m}} - T\Delta_{\mathrm{r}}S^\circ_{\mathrm{m}}$：$\Delta_{\mathrm{r}}H^\circ_{\mathrm{m}}$ 由**标准摩尔生成焓**、$\Delta_{\mathrm{r}}S^\circ_{\mathrm{m}}$ 由**标准摩尔熵**求得（[6.1.6](/6.1.6)），其他温度用 **Kirchhoff 定律**（[6.3.1](/6.3.1)）校正：

$$
\Delta_{\mathrm{r}}H^\circ_{\mathrm{m}}(T) = \Delta_{\mathrm{r}}H^\circ_{\mathrm{m}}(298.15\,\mathrm{K}) + \int_{298.15\,\mathrm{K}}^{T}\Delta_{\mathrm{r}}C_{p,\mathrm{m}}\,\mathrm{d}T, \qquad \Delta_{\mathrm{r}}S^\circ_{\mathrm{m}}(T) = \Delta_{\mathrm{r}}S^\circ_{\mathrm{m}}(298.15\,\mathrm{K}) + \int_{298.15\,\mathrm{K}}^{T}\frac{\Delta_{\mathrm{r}}C_{p,\mathrm{m}}}{T}\,\mathrm{d}T.
$$
也可以由 **Gibbs–Helmholtz 方程** $\frac{\Delta G(T_2)}{T_2} - \frac{\Delta G(T_1)}{T_1} = -\int_{T_1}^{T_2}\frac{\Delta H}{T^2}\,\mathrm{d}T$ 直接换算。粗略估算时取 $\Delta_{\mathrm{r}}H^\circ_{\mathrm{m}}$、$\Delta_{\mathrm{r}}S^\circ_{\mathrm{m}}$ 为 $298.15\,\mathrm{K}$ 的值。
2. 由**标准摩尔生成 Gibbs 自由能**：$\Delta_{\mathrm{r}}G^\circ_{\mathrm{m}} = \sum\nu_{\mathrm{B}}\Delta_{\mathrm{f}}G^\circ_{\mathrm{m}}(\mathrm{B})$（[6.1.6](/6.1.6#def-6.4.4)）。参考态单质的 $\Delta_{\mathrm{f}}G^\circ = 0$；溶液中的物种用 $b^\circ$ 标准态，并规定 $\Delta_{\mathrm{f}}G^\circ(\ce{H+}, \mathrm{aq}) = 0$（正负离子不能单独存在，只能确定离子的组合，这一规定给出了单个离子的数值表）。
3. 由已知反应组合：$\Delta_{\mathrm{r}}G^\circ_{\mathrm{m}}$ 像 $\Delta_{\mathrm{r}}H^\circ_{\mathrm{m}}$ 一样服从 **Hess 定律**，相应的 $K^\circ$ 相乘除。例如 $\ce{C(s) + 1/2O2(g) -> CO(g)}$ 的平衡常数难以直接测定（总有 $\ce{CO2}$ 生成），可由 $\ce{C + O2 -> CO2}$ 与 $\ce{CO + 1/2O2 -> CO2}$ 相减求得：$K^\circ_3 = K^\circ_1/K^\circ_2$。
4. 由可逆电池的电动势：$\Delta_{\mathrm{r}}G^\circ_{\mathrm{m}} = -zFE^\circ_{\mathrm{cell}}$（[6.1.11](/6.1.11)、[6.3.13](/6.3.13)）。
5. 由光谱数据与配分函数（[6.3.11](/6.3.11)）。

**例 7.4.1** 已知固体丁二酸在 $298.15\,\mathrm{K}$ 的 $\Delta_{\mathrm{f}}G^\circ(\mathrm{s})$ 与其饱和水溶液的质量摩尔浓度 $b_{\mathrm{sat}} = 0.715\,\mathrm{mol\,kg^{-1}}$，求溶质丁二酸（$b^\circ$ 标准态）的 $\Delta_{\mathrm{f}}G^\circ(\mathrm{aq})$。这是由离子的 $\Delta_{\mathrm{f}}G^\circ$ 计算其第一解离常数 $\ce{C4H6O4(aq) <=> C4H5O4^-(aq) + H+(aq)}$ 的关键一步。

**解** 设计途径：$\ce{C4H6O4(s)} \to$ 饱和溶液中的 $\ce{C4H6O4}$（$b_{\mathrm{sat}}$）$\to$ 标准态的 $\ce{C4H6O4(aq)}$（$b^\circ$）。第一步是固液平衡，$\Delta G_1 = 0$。第二步是溶质的浓度变化，忽略活度因子，$\Delta G_2 = RT\ln(b^\circ/b_{\mathrm{sat}}) = 8.314 \times 298.15 \times \ln(1/0.715) = 0.83\,\mathrm{kJ\,mol^{-1}}$。所以

$$
\Delta_{\mathrm{f}}G^\circ(\mathrm{aq}) = \Delta_{\mathrm{f}}G^\circ(\mathrm{s}) + RT\ln\frac{b^\circ}{b_{\mathrm{sat}}} = \Delta_{\mathrm{f}}G^\circ(\mathrm{s}) + 0.83\,\mathrm{kJ\,mol^{-1}}.
$$
同样的思路可以由饱和蒸气压把纯液体的 $\Delta_{\mathrm{f}}G^\circ(\mathrm{l})$ 换算成气体的 $\Delta_{\mathrm{f}}G^\circ(\mathrm{g})$：$\Delta_{\mathrm{f}}G^\circ(\mathrm{g}) = \Delta_{\mathrm{f}}G^\circ(\mathrm{l}) + RT\ln(p^\circ/p^*)$。$0.7\,\mathrm{mol\,kg^{-1}}$ 的溶液中活度因子并不严格为 1，这是该方法的主要误差。

### 7.4.3. 用 $\Delta_{\mathrm{r}}G^\circ_{\mathrm{m}}$ 估计反应的可能性

判断方向的是 $\Delta_{\mathrm{r}}G_{\mathrm{m}} = \Delta_{\mathrm{r}}G^\circ_{\mathrm{m}} + RT\ln Q$。但 $\lvert\Delta_{\mathrm{r}}G^\circ_{\mathrm{m}}\rvert$ 很大时，$RT\ln Q$ 在通常的组成范围内改变不了它的符号，于是可以用 $\Delta_{\mathrm{r}}G^\circ_{\mathrm{m}}$ 粗估：$298\,\mathrm{K}$ 时 $\Delta_{\mathrm{r}}G^\circ_{\mathrm{m}} = +40\,\mathrm{kJ\,mol^{-1}}$ 对应 $K^\circ = 1.0 \times 10^{-7}$，要使反应正向进行需 $Q < 10^{-7}$，一般做不到，可认为基本不能进行；$\Delta_{\mathrm{r}}G^\circ_{\mathrm{m}} < -40\,\mathrm{kJ\,mol^{-1}}$ 时基本进行完全；介于两者之间的反应可以通过改变条件（移去产物、改变温度、压力）使之向需要的方向进行。这一界限（有的教材取 $41.84\,\mathrm{kJ\,mol^{-1}} = 10\,\mathrm{kcal\,mol^{-1}}$）只是数量级的经验：它与方程式的写法（$\nu_{\mathrm{B}}$ 的大小）和温度有关，而且只回答热力学上的可能性，不涉及速率。

### 7.4.4. 转折温度

$\Delta_{\mathrm{r}}G^\circ_{\mathrm{m}}(T) = 0$（$K^\circ = 1$）的温度称为转折温度：$\Delta_{\mathrm{r}}H^\circ_{\mathrm{m}}$ 与 $\Delta_{\mathrm{r}}S^\circ_{\mathrm{m}}$ 同号时，反应在标准态下的方向在此处改变。忽略 $\Delta_{\mathrm{r}}C_p$ 时 $T_{\text{转折}} \approx \Delta_{\mathrm{r}}H^\circ_{\mathrm{m}}(298.15\,\mathrm{K})/\Delta_{\mathrm{r}}S^\circ_{\mathrm{m}}(298.15\,\mathrm{K})$。$\ce{CaCO3}$ 分解的估算值为 $1119\,\mathrm{K}$（[6.1.6 例 6.4.5](/6.1.6#ex-6.4.5) 的数据），而实测 $\ce{CO2}$ 分解压达到 $p^\circ$ 的温度约 $1170\,\mathrm{K}$；差别来自 $\Delta_{\mathrm{r}}H^\circ_{\mathrm{m}}$ 与 $\Delta_{\mathrm{r}}S^\circ_{\mathrm{m}}$ 在近 $900\,\mathrm{K}$ 的温度范围内的变化。对分解反应，转折温度就是分解压等于 $p^\circ$ 的温度。

## 7.5. 影响平衡的因素

平衡移动的问题，实质上都是"新状态"下反应方向的判断：比较新状态的 $Q$ 与新温度下的 $K^\circ$。温度主要改变 $K^\circ$；压力、惰性组分与浓度改变 $Q$。

### 7.5.1. 温度

**定理 7.5.1（van 't Hoff 方程）** 

$$
\frac{\mathrm{d}\ln K^\circ}{\mathrm{d}T} = \frac{\Delta_{\mathrm{r}}H^\circ_{\mathrm{m}}}{RT^2}. \tag{7.6}
$$

**证明** $\ln K^\circ = -\Delta_{\mathrm{r}}G^\circ_{\mathrm{m}}/RT$。$\Delta_{\mathrm{r}}G^\circ_{\mathrm{m}} = \sum\nu_{\mathrm{B}}\mu^\circ_{\mathrm{B}}(T)$ 只是温度的函数，对每种物质用 Gibbs–Helmholtz 方程 $\frac{\mathrm{d}(\mu^\circ_{\mathrm{B}}/T)}{\mathrm{d}T} = -\frac{H^\circ_{\mathrm{B}}}{T^2}$（$H^\circ_{\mathrm{B}}$ 为 B 在标准态的摩尔焓，溶质为无限稀时的偏摩尔焓），求和得 $\frac{\mathrm{d}(\Delta_{\mathrm{r}}G^\circ_{\mathrm{m}}/T)}{\mathrm{d}T} = -\frac{\Delta_{\mathrm{r}}H^\circ_{\mathrm{m}}}{T^2}$，即式 (7.6)。$\square$

这一推导没有用到 $\Delta_{\mathrm{r}}H^\circ_{\mathrm{m}}$ 为常数的假设，它比 [6.1.8](/6.1.8#thm-8.4.1) 的推导更一般。积分时分两种情况：

1. $\Delta_{\mathrm{r}}C_{p,\mathrm{m}} \approx 0$ 或温度范围不大：$\ln\frac{K^\circ_2}{K^\circ_1} = \frac{\Delta_{\mathrm{r}}H^\circ_{\mathrm{m}}}{R}\left(\frac{1}{T_1} - \frac{1}{T_2}\right)$，$\ln K^\circ$ 对 $1/T$ 为直线。
2. 温度范围大：把 $\Delta_{\mathrm{r}}H^\circ_{\mathrm{m}}(T)$ 用 Kirchhoff 定律表示后积分。若 $C_{p,\mathrm{m}} = a + bT + c/T^2$，则 $\Delta_{\mathrm{r}}H^\circ_{\mathrm{m}}(T) = \Delta H_0 + \Delta a\,T + \frac{\Delta b}{2}T^2 - \frac{\Delta c}{T}$（$\Delta H_0$ 为积分常数，由 $298.15\,\mathrm{K}$ 的值确定），代入式 (7.6) 积分：

$$
\ln K^\circ = -\frac{\Delta H_0}{RT} + \frac{\Delta a}{R}\ln T + \frac{\Delta b}{2R}T + \frac{\Delta c}{2RT^2} + I,
$$
积分常数 $I$ 由某一温度的 $K^\circ$ 确定。实际计算中直接对 $\Delta_{\mathrm{r}}C_{p,\mathrm{m}}$ 数值积分更方便。

**例 7.5.1** 由 [6.1.8](/6.1.8) 的数据（$\Delta_{\mathrm{f}}H^\circ(\ce{NH3}) = -45.9\,\mathrm{kJ\,mol^{-1}}$，$S^\circ_{\mathrm{m}}$：$\ce{NH3}$ 192.8，$\ce{N2}$ 191.6，$\ce{H2}$ $130.7\,\mathrm{J\,mol^{-1}\,K^{-1}}$）与热容经验式（$C_{p,\mathrm{m}}/(\mathrm{J\,mol^{-1}\,K^{-1}}) = a + bT + c/T^2$；$\ce{NH3}$：29.75，$25.10 \times 10^{-3}$，$-1.55 \times 10^5$；$\ce{N2}$：28.58，$3.77 \times 10^{-3}$，$-0.50 \times 10^5$；$\ce{H2}$：27.28，$3.26 \times 10^{-3}$，$0.50 \times 10^5$）求 $\ce{1/2N2(g) + 3/2H2(g) <=> NH3(g)}$ 在 $723\,\mathrm{K}$ 的 $K^\circ$。

**解** $298.15\,\mathrm{K}$ 时 $\Delta_{\mathrm{r}}H^\circ_{\mathrm{m}} = -45.9\,\mathrm{kJ\,mol^{-1}}$，$\Delta_{\mathrm{r}}S^\circ_{\mathrm{m}} = -99.05\,\mathrm{J\,mol^{-1}\,K^{-1}}$，$\Delta_{\mathrm{r}}C_{p,\mathrm{m}} = -22.3\,\mathrm{J\,mol^{-1}\,K^{-1}}$（$723\,\mathrm{K}$ 时为 $-12.6$）。数值积分 Kirchhoff 定律：$\Delta_{\mathrm{r}}H^\circ_{\mathrm{m}}(723\,\mathrm{K}) = -53.1\,\mathrm{kJ\,mol^{-1}}$，$\Delta_{\mathrm{r}}S^\circ_{\mathrm{m}}(723\,\mathrm{K}) = -114.8\,\mathrm{J\,mol^{-1}\,K^{-1}}$，$\Delta_{\mathrm{r}}G^\circ_{\mathrm{m}} = 29.8\,\mathrm{kJ\,mol^{-1}}$，$K^\circ = 7.0 \times 10^{-3}$。若忽略 $\Delta_{\mathrm{r}}C_p$，$\Delta_{\mathrm{r}}G^\circ_{\mathrm{m}} = -45.9 + 723 \times 0.09905 = 25.7\,\mathrm{kJ\,mol^{-1}}$，$K^\circ = 1.4 \times 10^{-2}$，偏大一倍。文献中 $723\,\mathrm{K}$ 的实验值约为 $6.4 \times 10^{-3}$；$\Delta_{\mathrm{r}}G^\circ_{\mathrm{m}}$ 有 $1\,\mathrm{kJ\,mol^{-1}}$ 的误差，$K^\circ$ 在这一温度就差 $18\%$，所以高温平衡常数对数据的精度要求很高。

![合成氨（½N₂ + 3/2H₂ ⇌ NH₃）的 van 't Hoff 作图：忽略 ΔrCp 的直线与计入热容的曲线在高温下明显分开（左）；反应热容随温度的变化（右）](./plots/ammonia-heat-capacity.py)

定性结论：吸热反应升温使 $K^\circ$ 增大，放热反应升温使 $K^\circ$ 减小。一个常见的疑问：$\Delta_{\mathrm{r}}H^\circ_{\mathrm{m}} > 0$、$\Delta_{\mathrm{r}}S^\circ_{\mathrm{m}} < 0$ 的反应，升温时 $\Delta_{\mathrm{r}}G^\circ_{\mathrm{m}} = \Delta_{\mathrm{r}}H^\circ_{\mathrm{m}} - T\Delta_{\mathrm{r}}S^\circ_{\mathrm{m}}$ 增大，$K^\circ$ 是否因此减小？不是：决定 $K^\circ$ 的是 $\Delta_{\mathrm{r}}G^\circ_{\mathrm{m}}/T = \Delta_{\mathrm{r}}H^\circ_{\mathrm{m}}/T - \Delta_{\mathrm{r}}S^\circ_{\mathrm{m}}$，它随 $T$ 升高而减小，所以 $K^\circ$ 增大，与 van 't Hoff 方程一致（尽管 $K^\circ$ 始终小于 1）。放热反应低温有利于平衡，但生产上不能一味降温：温度太低反应太慢，要在平衡与速率之间折中（合成氨，[6.1.8](/6.1.8)）。

### 7.5.2. 压力

压力不改变 $K^\circ$，但改变 $Q$。对理想气体反应，由式 (7.5)，$K_x = K^\circ(p/p^\circ)^{-\Delta\nu_{\mathrm{g}}}$：$\Delta\nu_{\mathrm{g}} < 0$ 时加压使 $K_x$ 增大，平衡向气体分子数减少的方向移动；$\Delta\nu_{\mathrm{g}} > 0$ 时相反；$\Delta\nu_{\mathrm{g}} = 0$ 时不受压力影响。凝聚相反应受压力影响很小，影响的方向由 $\Delta_{\mathrm{r}}V$ 决定（7.5.4），高压下才显著（如石墨转变为金刚石，[6.3.3](/6.3.3)）。

高压下气体不理想，要用逸度：

$$
K^\circ = \prod_{\mathrm{B}}\left(\frac{\varphi_{\mathrm{B}}p_{\mathrm{B}}}{p^\circ}\right)^{\nu_{\mathrm{B}}} = K_x\left(\frac{p}{p^\circ}\right)^{\Delta\nu_{\mathrm{g}}}\prod_{\mathrm{B}}\varphi_{\mathrm{B}}^{\nu_{\mathrm{B}}}.
$$
混合物中各组分的逸度因子按 **Lewis–Randall 规则**近似取同温同压下纯气体的值，后者由对比参量从普遍化逸度因子图查得，或由物态方程计算（[6.3.4](/6.3.4)）。

**例 7.5.2** $723\,\mathrm{K}$ 时 $\ce{1/2N2(g) + 3/2H2(g) <=> NH3(g)}$ 的 $K^\circ = 6.4 \times 10^{-3}$（例 7.5.1 末尾的实验值），原料按 $n(\ce{N2}) : n(\ce{H2}) = 1 : 3$。(1) 总压保持 $100\,\mathrm{kPa}$，求平衡转化率；(2) 总压 $30\,\mathrm{MPa}$，按理想气体计算；(3) 总压 $30\,\mathrm{MPa}$，取逸度因子 $\varphi(\ce{N2}) = 1.15$，$\varphi(\ce{H2}) = 1.09$，$\varphi(\ce{NH3}) = 0.87$。

**解** 设 $\ce{N2}$ 反应了 $x$（以 $1\,\mathrm{mol}$ $\ce{N2}$ 计）：$\ce{N2}$ $1 - x$，$\ce{H2}$ $3(1 - x)$，$\ce{NH3}$ $2x$，总量 $4 - 2x$。

$$
K^\circ = \frac{2x(4 - 2x)}{3^{3/2}(1 - x)^2}\cdot\frac{p^\circ}{p}\cdot\frac{\varphi_{\ce{NH3}}}{\varphi_{\ce{N2}}^{1/2}\varphi_{\ce{H2}}^{3/2}}.
$$
(1) $p = p^\circ$，$\varphi = 1$：$x = 0.0041$，转化率 $0.41\%$。(2) $p = 300p^\circ$：$x = 0.465$，转化率 $46.5\%$，$y(\ce{NH3}) = 0.303$。(3) $\prod\varphi_{\mathrm{B}}^{\nu_{\mathrm{B}}} = 0.87/(1.15^{1/2} \times 1.09^{3/2}) = 0.713$，相当于把 $K_x$ 放大 $1/0.713 = 1.40$ 倍：$x = 0.529$，转化率 $52.9\%$，$y(\ce{NH3}) = 0.359$。实测 $450\,^\circ\mathrm{C}$、约 $30\,\mathrm{MPa}$ 下平衡氨含量约 $36\%$，与逸度修正后的结果相符。$\ce{NH3}$ 的逸度因子小于 1（分子间吸引强），$\ce{N2}$、$\ce{H2}$ 的大于 1（远高于临界温度，以排斥为主），非理想性使平衡进一步右移。

![723 K、1 : 3 投料时平衡氨摩尔分数随总压的变化：理想气体与逸度修正（逸度因子按 30 MPa 的值、ln φ 随压力线性外推的近似）](./plots/ammonia-fugacity.py)

### 7.5.3. 惰性组分

不参加反应的气体（如 Ar、$\ce{CH4}$、水蒸气）称为惰性组分。等温等压下加入惰性组分，反应气体的分压按同一比例降低，相当于对反应系统减压：平衡向气体分子数增加的方向移动。等温等容下加入惰性组分，对理想气体反应各分压不变，平衡不移动；对高压气体，逸度因子随总压改变，平衡会有少许移动。

**例 7.5.3** $900\,\mathrm{K}$ 时乙苯脱氢 $\ce{C6H5C2H5(g) <=> C6H5C2H3(g) + H2(g)}$ 的 $K^\circ = 2.7$。由 $1\,\mathrm{mol}$ 乙苯出发，求平衡时苯乙烯的量：(a) 总压 $p^\circ$；(b) 总压 $0.1p^\circ$；(c) 总压 $p^\circ$，加入 $10\,\mathrm{mol}$ 水蒸气。

**解** 设生成苯乙烯 $x\,\mathrm{mol}$，乙苯剩 $1 - x$，$\ce{H2}$ 为 $x$，总量 $1 + x + n_{\mathrm{inert}}$。

$$
K^\circ = \frac{x^2}{(1 - x)(1 + x + n_{\mathrm{inert}})}\cdot\frac{p}{p^\circ}.
$$
(a) $n_{\mathrm{inert}} = 0$，$p = p^\circ$：$x^2/(1 - x^2) = 2.7$，$x = 0.85\,\mathrm{mol}$。(b) $p = 0.1p^\circ$：$x = 0.98\,\mathrm{mol}$。(c) $n_{\mathrm{inert}} = 10$：$x = 0.97\,\mathrm{mol}$。加入水蒸气与减压效果相当，而且在常压下操作，避免了负压设备与空气漏入的危险；工业上还利用水蒸气供热、抑制积炭。

### 7.5.4. 浓度与 Le Chatelier 原理

加入反应物或移去产物使 $Q$ 减小，平衡正向移动；工业上常让廉价原料过量，或不断移去产物（如结晶、蒸馏、吸收），以提高贵重原料的转化率。但恒压下加入某一反应物并不一定使平衡正向移动：加入的物质同时稀释了其他组分。[6.1.8 的例 8.4.2](/6.1.8#ex-8.4.2) 已经证明，向合成氨平衡系统中等温等压加入 $\ce{N2}$，当 $x(\ce{N2}) > 1/2$ 时平衡反而左移。

**例 7.5.4** 某温度、总压 $p^\circ$ 下 $\ce{N2(g) + 3H2(g) <=> 2NH3(g)}$ 平衡时 $n(\ce{N2}) = 3.00\,\mathrm{mol}$，$n(\ce{H2}) = n(\ce{NH3}) = 1.00\,\mathrm{mol}$。保持温度与总压不变，(1) 加入 $0.10\,\mathrm{mol}$ $\ce{N2}$；(2) 把 $\ce{H2}$ 增加到 $3.10\,\mathrm{mol}$，平衡各向哪个方向移动？

**解** 平衡时摩尔分数为 $0.6$、$0.2$、$0.2$，$K^\circ = \frac{0.2^2}{0.6 \times 0.2^3} = 8.33$（$p = p^\circ$）。(1) 总量 $5.1\,\mathrm{mol}$，$Q = \frac{(1/5.1)^2}{(3.1/5.1)(1/5.1)^3} = 8.39 > K^\circ$，平衡左移：这里 $x(\ce{N2}) = 0.6 > 1/2$。(2) 总量 $7.1\,\mathrm{mol}$，$Q = \frac{(1/7.1)^2}{(3/7.1)(3.1/7.1)^3} = 0.564 < K^\circ$，平衡右移。多种因素同时改变时不能简单套用定性结论，可靠的方法始终是比较新状态的 $Q$ 与 $K^\circ$。

Le Chatelier 在 1884 年把平衡移动的规律概括为一条经验原理（**Le Chatelier 原理**，[6.1.8](/6.1.8#sec-8.4.4)）。它的定性表述在什么条件下严格成立，可以由热力学推出。

**定理 7.5.2（Le Chatelier 原理）** 设系统在 $T$、$p$ 下处于稳定的化学平衡，则

$$
\left(\frac{\partial\xi_{\mathrm{eq}}}{\partial T}\right)_p = \frac{\Delta_{\mathrm{r}}H_{\mathrm{m}}}{TG_{\xi\xi}}, \qquad \left(\frac{\partial\xi_{\mathrm{eq}}}{\partial p}\right)_T = -\frac{\Delta_{\mathrm{r}}V_{\mathrm{m}}}{G_{\xi\xi}}, \qquad G_{\xi\xi} = \left(\frac{\partial^2G}{\partial\xi^2}\right)_{T,p} > 0,
$$
其中 $\Delta_{\mathrm{r}}H_{\mathrm{m}} = \sum\nu_{\mathrm{B}}H_{\mathrm{B}}$、$\Delta_{\mathrm{r}}V_{\mathrm{m}} = \sum\nu_{\mathrm{B}}V_{\mathrm{B}}$ 为平衡组成下的摩尔反应焓与摩尔反应体积（偏摩尔量之和）。所以升温使平衡向吸热方向移动，加压使平衡向体积减小的方向移动。

**证明** 平衡位置由 $\Delta_{\mathrm{r}}G_{\mathrm{m}}(T, p, \xi_{\mathrm{eq}}) = 0$ 确定。沿平衡线微分：

$$
\left(\frac{\partial\Delta_{\mathrm{r}}G_{\mathrm{m}}}{\partial T}\right)_{p,\xi}\mathrm{d}T + \left(\frac{\partial\Delta_{\mathrm{r}}G_{\mathrm{m}}}{\partial p}\right)_{T,\xi}\mathrm{d}p + G_{\xi\xi}\,\mathrm{d}\xi_{\mathrm{eq}} = 0.
$$
由 $(\partial\mu_{\mathrm{B}}/\partial T)_{p,n} = -S_{\mathrm{B}}$、$(\partial\mu_{\mathrm{B}}/\partial p)_{T,n} = V_{\mathrm{B}}$，前两个系数分别是 $-\Delta_{\mathrm{r}}S_{\mathrm{m}}$ 与 $\Delta_{\mathrm{r}}V_{\mathrm{m}}$；平衡时 $\Delta_{\mathrm{r}}G_{\mathrm{m}} = \Delta_{\mathrm{r}}H_{\mathrm{m}} - T\Delta_{\mathrm{r}}S_{\mathrm{m}} = 0$，所以 $\Delta_{\mathrm{r}}S_{\mathrm{m}} = \Delta_{\mathrm{r}}H_{\mathrm{m}}/T$。代入即得两式。平衡是 $G$ 的极小，稳定性要求 $G_{\xi\xi} > 0$（对理想混合物，由混合 Gibbs 自由能的凸性这总是成立的）。$\square$

定理说明，对温度与压力这类强度量，Le Chatelier 原理是严格的：系统的响应（吸热、体积缩小）"减弱"外界的改变，符号由稳定性条件 $G_{\xi\xi} > 0$ 保证。对理想气体，$\Delta_{\mathrm{r}}V_{\mathrm{m}} = \Delta\nu_{\mathrm{g}}RT/p$，回到 7.5.2 的结论。但对"加入某一组分的物质的量"这种广度量，没有一般的符号规律：加入的物质会改变所有组分的摩尔分数，结果取决于组成（上面的例子）。这就是原理的局限，也说明它只是热力学结论的一个定性概括。

催化剂同等程度地降低正逆反应的活化能，不改变 $K^\circ$，平衡不移动，只缩短达到平衡的时间。

## 7.6. 同时平衡与耦合反应

### 7.6.1. 同时平衡

**定义 7.6.1** 一个系统中同时进行几个反应，有的物种同时参与其中两个以上反应，所有反应同时达到平衡的状态称为**同时平衡**。

平衡时每一个独立反应都满足自己的条件 $\sum_{\mathrm{B}}\nu_{\mathrm{B}j}\mu_{\mathrm{B}} = 0$，因而有自己的 $K^\circ_j$，同一物种在各个平衡常数表达式中的活度相同。独立反应的数目等于化学计量系数矩阵 $(\nu_{\mathrm{B}j})$ 的秩：其他反应是独立反应的线性组合，它们的平衡条件自动满足（这一数目也决定相律中的独立组分数，[6.3.8](/6.3.8)）。计算时把几个反应进度作为未知量联立求解；等价的做法是在元素守恒的约束下直接求 $G$ 的极小，这正是化工与地球化学中复杂平衡计算（Gibbs 自由能最小化）的方法。

例如二氧化钛的氯化（$298.15\,\mathrm{K}$，CRC 数据）：

$$
\begin{aligned}
&(1)\ \ce{TiO2(s) + 2Cl2(g) -> TiCl4(l) + O2(g)}, && \Delta_{\mathrm{r}}G^\circ_{\mathrm{m}} = +151.6\,\mathrm{kJ\,mol^{-1}}, \\
&(2)\ \ce{C(s) + O2(g) -> CO2(g)}, && \Delta_{\mathrm{r}}G^\circ_{\mathrm{m}} = -394.4\,\mathrm{kJ\,mol^{-1}}, \\
&(3) = (1) + (2)\ \ce{TiO2(s) + C(s) + 2Cl2(g) -> TiCl4(l) + CO2(g)}, && \Delta_{\mathrm{r}}G^\circ_{\mathrm{m}} = -242.8\,\mathrm{kJ\,mol^{-1}}.
\end{aligned}
$$
单独的反应 (1) 在热力学上不利，加入碳后总反应 (3) 十分有利，这是工业上由金红石制取 $\ce{TiCl4}$（进而制钛）的方法。常把它说成反应 (2) "带动"了反应 (1)，但从热力学看，这是一个同时平衡：在炽热的碳存在时，$\ce{O2}$ 的分压被压到极低，反应 (1) 的 $Q$ 极小，它的 $\Delta_{\mathrm{r}}G_{\mathrm{m}} = \Delta_{\mathrm{r}}G^\circ_{\mathrm{m}} + RT\ln Q$ 本身就已为负；两个反应各自自发地向右进行，碳的作用是不断移走产物 $\ce{O2}$。

### 7.6.2. 耦合反应

**定义 7.6.2** 两个反应通过共同的中间物或同一个反应机理联系在一起，使一个反应只能伴随另一个反应按一定比例进行，这样的一对反应称为**耦合反应**。借助 $\Delta_{\mathrm{r}}G_{\mathrm{m}}$ 很负的反应，可以推动 $\Delta_{\mathrm{r}}G_{\mathrm{m}} > 0$ 的反应进行。

热力学只要求耦合后的总反应满足 $\Delta_{\mathrm{r}}G_{\mathrm{m}}(1) + \Delta_{\mathrm{r}}G_{\mathrm{m}}(2) < 0$（按耦合的计量比计）。"耦合"本身是机理上的事实，热力学不能保证它发生：两个反应在同一容器中各自进行并不会互相推动，必须有共同的中间物（如磷酸化的底物）或分子机器把它们的进度锁定在一起。不完全耦合时两个反应的速率之比可以变化，这种情形属于非平衡热力学中通量的耦合（[6.3.18](/6.3.18)）。

生物体内最重要的耦合是 ATP 的水解。生物化学中采用生化标准态：$\mathrm{pH} = 7$（即 $a_{\ce{H+}} = 10^{-7}$ 而不是 1），水的活度取 1，并规定 $\ce{Mg^2+}$ 浓度与离子强度；相应的标准摩尔反应 Gibbs 自由能记作 $\Delta_{\mathrm{r}}G^{\circ\prime}_{\mathrm{m}}$。对有 $\ce{H+}$ 参与的反应，$\Delta_{\mathrm{r}}G^{\circ\prime}_{\mathrm{m}} = \Delta_{\mathrm{r}}G^\circ_{\mathrm{m}} + \nu_{\ce{H+}}RT\ln 10^{-7}$，这只是标准态的改变（[6.3.6](/6.3.6)），等温式的形式不变。

$$
\begin{aligned}
&\text{ATP} + \ce{H2O} \longrightarrow \text{ADP} + \mathrm{P_i}, && \Delta_{\mathrm{r}}G^{\circ\prime}_{\mathrm{m}} = -30.5\,\mathrm{kJ\,mol^{-1}}, \\
&\text{葡萄糖} + \mathrm{P_i} \longrightarrow \text{葡萄糖-6-磷酸} + \ce{H2O}, && \Delta_{\mathrm{r}}G^{\circ\prime}_{\mathrm{m}} = +13.8\,\mathrm{kJ\,mol^{-1}}, \\
&\text{葡萄糖} + \text{ATP} \longrightarrow \text{葡萄糖-6-磷酸} + \text{ADP}, && \Delta_{\mathrm{r}}G^{\circ\prime}_{\mathrm{m}} = -16.7\,\mathrm{kJ\,mol^{-1}}.
\end{aligned}
$$
（$\mathrm{P_i}$ 为无机磷酸。）糖酵解的第一步由己糖激酶催化，磷酰基直接从 ATP 转移到葡萄糖上：酶把"ATP 水解"与"葡萄糖磷酸化"合成了一个反应，单独的磷酸化（$K^{\circ\prime} = 4 \times 10^{-3}$）因此变成 $K^{\circ\prime} = 8 \times 10^2$ 的有利反应。这里的耦合是化学计量上的：两个"半反应"从不单独发生。

细胞中的推动力由实际浓度决定。以人的红细胞为例，$[\text{ATP}] = 2.25\,\mathrm{mmol\,L^{-1}}$，$[\text{ADP}] = 0.25\,\mathrm{mmol\,L^{-1}}$，$[\mathrm{P_i}] = 1.65\,\mathrm{mmol\,L^{-1}}$，$37\,^\circ\mathrm{C}$ 时

$$
\Delta_{\mathrm{r}}G_{\mathrm{m}} = \Delta_{\mathrm{r}}G^{\circ\prime}_{\mathrm{m}} + RT\ln\frac{[\text{ADP}][\mathrm{P_i}]}{[\text{ATP}]\,c^\circ} = -30.5 + 2.58\ln\frac{0.25 \times 10^{-3} \times 1.65 \times 10^{-3}}{2.25 \times 10^{-3}} = -52.7\,\mathrm{kJ\,mol^{-1}},
$$
比标准值负得多：细胞通过呼吸作用不断再生 ATP，使 ATP/ADP 比远离平衡（在上述 $[\mathrm{P_i}]$ 下，平衡时 $[\text{ATP}]/[\text{ADP}]$ 只有约 $10^{-8}$，细胞中却约为 9），ATP 水解的推动力因此保持在约 $-50\,\mathrm{kJ\,mol^{-1}}$。生命系统是开放系统，靠持续的物质与能量流维持这种远离平衡的状态（[6.3.18](/6.3.18)）。常说的"高能磷酸键"是误称：$-30.5\,\mathrm{kJ\,mol^{-1}}$ 是整个反应在水溶液中的 Gibbs 自由能变化，来自产物的共振稳定化、电荷排斥的减小与溶剂化，而不是储存在某一根键里的能量（断键总是吸热的）。

## 小结

| 内容 | 要点 |
|---|---|
| 平衡的本质 | $G(\xi)$ = 线性项 + $\Delta_{\mathrm{mix}}G$，混合使极小落在内部；纯凝聚相之间的反应可以进行到底 |
| 平衡条件 | $\Delta_{\mathrm{r}}G_{\mathrm{m}} = (\partial G/\partial\xi)_{T,p} = \sum\nu_{\mathrm{B}}\mu_{\mathrm{B}} = 0$，与约束条件无关，适用于多相 |
| 等温式与 $K^\circ$ | $\Delta_{\mathrm{r}}G_{\mathrm{m}} = \Delta_{\mathrm{r}}G^\circ_{\mathrm{m}} + RT\ln Q$；$K^\circ = \exp(-\Delta_{\mathrm{r}}G^\circ_{\mathrm{m}}/RT) = \prod(a_{\mathrm{B}}^{\mathrm{eq}})^{\nu_{\mathrm{B}}}$；与 $T$、标准态、方程式写法有关，与压力无关 |
| 各类系统 | 气体 $f/p^\circ$，溶液 $\gamma x$ 或 $\gamma b/b^\circ$，纯凝聚相 $a = 1$；分解压；$K^\circ = K_x(p/p^\circ)^{\Delta\nu_{\mathrm{g}}}$ |
| $\Delta_{\mathrm{r}}G^\circ_{\mathrm{m}}$ | 由 $\Delta H^\circ - T\Delta S^\circ$（Kirchhoff 校正）、$\Delta_{\mathrm{f}}G^\circ$、反应组合、电动势、配分函数求得；$\pm 40\,\mathrm{kJ\,mol^{-1}}$ 粗估；转折温度 $\Delta H^\circ/\Delta S^\circ$ |
| 温度 | $\mathrm{d}\ln K^\circ/\mathrm{d}T = \Delta_{\mathrm{r}}H^\circ_{\mathrm{m}}/RT^2$；宽温度范围须计入 $\Delta_{\mathrm{r}}C_p$ |
| 压力与惰性组分 | 改变 $Q$ 不改变 $K^\circ$；高压用逸度；恒压加惰性组分相当于减压 |
| Le Chatelier 原理 | 对 $T$、$p$ 严格：$(\partial\xi/\partial T)_p \propto \Delta_{\mathrm{r}}H$，$(\partial\xi/\partial p)_T \propto -\Delta_{\mathrm{r}}V$；对加入组分无一般规律 |
| 同时平衡与耦合 | 每个独立反应各自满足平衡条件；耦合需要共同中间物或机理，总的 $\Delta_{\mathrm{r}}G < 0$；ATP 水解在细胞中约 $-50\,\mathrm{kJ\,mol^{-1}}$ |

## 思考题

1. 对反应 $\ce{2H2(g) + O2(g) <=> 2H2O(g)}$，若三种物质的量之比分别为 $1:1:1$ 与 $2:1:2$，其他条件相同，$K^\circ$、$Q$、$\Delta_{\mathrm{r}}G^\circ_{\mathrm{m}}$、$\Delta_{\mathrm{r}}G_{\mathrm{m}}$ 中哪些相同？
   答：$K^\circ$ 与 $\Delta_{\mathrm{r}}G^\circ_{\mathrm{m}}$ 只与温度有关，相同；$Q$ 与 $\Delta_{\mathrm{r}}G_{\mathrm{m}}$ 随组成而变，不同。
2. "若选不同的标准态，$\mu^\circ_{\mathrm{B}}$ 不同，所以 $\Delta_{\mathrm{r}}G^\circ_{\mathrm{m}}$ 不同，但 $\Delta_{\mathrm{r}}G_{\mathrm{m}}$ 相同"对吗？"平衡移动了，平衡常数一定改变"对吗？
   答：前者对，$\Delta_{\mathrm{r}}G_{\mathrm{m}} = \sum\nu_{\mathrm{B}}\mu_{\mathrm{B}}$ 由系统的状态决定；后者错，改变压力或浓度可使平衡移动而 $K^\circ$ 不变。
3. 能否说所有化学反应都存在化学平衡，"不能反应"的平衡常数为零，"完全反应"的平衡常数为无穷大？
   答：不能。$K^\circ = \exp(-\Delta_{\mathrm{r}}G^\circ_{\mathrm{m}}/RT)$ 总是有限的正数，只是可以极大或极小。另一方面，反应物与产物都是互不混合的纯凝聚相时（7.1.1），系统没有组成可以调节，除了 $K^\circ$ 恰好等于 1 的温度外不存在平衡态，反应要么进行到底，要么不进行。
