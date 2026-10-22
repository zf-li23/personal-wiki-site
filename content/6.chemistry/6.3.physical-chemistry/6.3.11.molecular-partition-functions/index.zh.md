---
title: 分子配分函数与理想气体的热力学性质
description: 分子配分函数按平动、转动、振动、电子与核运动析因；热波长、转动与振动特征温度、对称数与转动配分函数的修正级数；理想气体的内能、热容与 Einstein 函数；Sackur–Tetrode 方程与统计熵，统计熵与量热熵的比较和残余熵；由统计熵求蒸气压；由配分函数计算标准平衡常数（I₂ 解离、H₂ + D₂ 交换）。
---

上一章（[6.3.10](/6.3.10)）建立了统计热力学的框架：只要知道分子的能级，就能算出**分子配分函数** $q$，进而由系统配分函数 $Z = q^N/N!$ 得到理想气体的全部热力学函数。本章完成这一程序。分子的能量可以近似分解为平动、转动、振动、电子运动与核运动五部分，$q$ 相应地分解为五个因子，每个因子都可以由分子的质量、转动惯量、振动频率与电子能级算出，这些数据都来自光谱（[5.5.5](/5.5.5#sec-5.3)）。由此得到的结果解释了热容随温度的变化（能量均分定理在什么时候成立、为什么振动在常温下"冻结"），给出了与量热法相互独立、往往更准确的统计熵，并揭示了残余熵的来源。最后一节由配分函数直接计算标准平衡常数：它把 [6.3.7](/6.3.7) 的 $K^\circ$ 与分子结构联系起来，也是 [6.3.16](/6.3.16) 中过渡态理论的出发点。

本章的分子能级取自量子物理：势箱中的粒子与量子谐振子（[5.5.3](/5.5.3)）、电子自旋与光谱项（[5.5.4](/5.5.4)）、双原子分子的转动与振动能级（[5.5.5](/5.5.5#sec-5.3)）。按分子光谱与化学的惯例，转动量子数写 $J$、转动惯量写 $I$、振动量子数写 $v$（[5.5.5 注 5.3.1](/5.5.5#rem-5.3.1)）。各运动的配分函数一律以该运动的基态为能量零点，需要时显式写出 $0\,\mathrm{K}$ 的能量 $U_0$（[6.3.10](/6.3.10#sec-10.4.3)）。数值计算中的常量取 CODATA 2022，光谱常数取文献值。

## 11.1. 配分函数的析因

把分子的能量写成各种运动的能量之和，简并度写成各自简并度之积：

$$
\varepsilon_i = \varepsilon_{\mathrm{t}} + \varepsilon_{\mathrm{r}} + \varepsilon_{\mathrm{v}} + \varepsilon_{\mathrm{e}} + \varepsilon_{\mathrm{n}}, \qquad g_i = g_{\mathrm{t}}\,g_{\mathrm{r}}\,g_{\mathrm{v}}\,g_{\mathrm{e}}\,g_{\mathrm{n}}.
$$
平动是质心的运动（外部运动），其余四种是内部运动。这种分解是近似：Born–Oppenheimer 近似把电子运动与核运动分开（[5.5.5](/5.5.5#sec-5.3.1)），刚性转子与谐振子模型忽略了转动与振动的耦合和振动的非谐性，同核分子的核自旋还与转动耦合（11.5 节）。在这些近似下，

**定理 11.1.1** 分子配分函数等于各运动配分函数之积：

$$
q = q_{\mathrm{t}}\,q_{\mathrm{r}}\,q_{\mathrm{v}}\,q_{\mathrm{e}}\,q_{\mathrm{n}}, \qquad q_{\mathrm{t}} = \sum_{\mathrm{t}} g_{\mathrm{t}}\,\mathrm{e}^{-\varepsilon_{\mathrm{t}}/(k_{\mathrm{B}}T)},\ \dots
\tag{11.1}
$$

**证明** 分子的一个能级由各运动的能级 $(i_{\mathrm{t}}, i_{\mathrm{r}}, \dots)$ 独立组合而成。指数函数把和变成积，对独立指标的多重求和等于各自求和之积：

$$
q = \sum_{i_{\mathrm{t}}}\sum_{i_{\mathrm{r}}}\cdots\ g_{\mathrm{t}}g_{\mathrm{r}}\cdots\ \mathrm{e}^{-(\varepsilon_{\mathrm{t}} + \varepsilon_{\mathrm{r}} + \cdots)/(k_{\mathrm{B}}T)} = \left(\sum_{i_{\mathrm{t}}} g_{\mathrm{t}}\mathrm{e}^{-\varepsilon_{\mathrm{t}}/(k_{\mathrm{B}}T)}\right)\left(\sum_{i_{\mathrm{r}}} g_{\mathrm{r}}\mathrm{e}^{-\varepsilon_{\mathrm{r}}/(k_{\mathrm{B}}T)}\right)\cdots. \qquad \square
$$

于是 $\ln q$ 是各项之和，由 $\ln q$ 的导数给出的 $U$、$C_V$ 都是各运动贡献之和。熵与 Helmholtz 自由能中还有 $-k_{\mathrm{B}}\ln N!$，它来自分子不可区分，而分子能够交换位置正是由于平动，所以习惯上把它归入平动项：

$$
\ln\frac{q^N}{N!} = \ln\frac{q_{\mathrm{t}}^N}{N!} + N\ln q_{\mathrm{r}} + N\ln q_{\mathrm{v}} + N\ln q_{\mathrm{e}} + N\ln q_{\mathrm{n}}.
$$

各运动的能级间隔相差悬殊，决定了它们的配分函数怎样计算（$298\,\mathrm{K}$ 时与 $k_{\mathrm{B}}T$ 的比较，以 $\ce{N2}$ 为例）：

| 运动 | 能级间隔 / $k_{\mathrm{B}}T$ | 处理方法 | 室温下的状态 |
|---|---|---|---|
| 平动（$10\,\mathrm{cm}$ 容器） | $\sim10^{-19}$ | 求和换成积分 | 大量能级被占据 |
| 转动 | $2\Theta_{\mathrm{r}}/T \approx 0.02$ | 一般可换成积分（$\ce{H2}$ 等例外） | 大量能级被占据 |
| 振动 | $\Theta_{\mathrm{v}}/T \approx 11$ | 必须求和（等比级数） | 几乎都在基态 |
| 电子 | $\gtrsim 10^2$ | 通常只取基态 | 基态（少数例外） |
| 核 | $\gg 10^5$ | 只取基态 | 基态 |

## 11.2. 平动配分函数

一维势箱中的能级为 $\varepsilon_{\mathrm{t}} = \frac{h^2}{8ma^2}n_x^2$，$n_x = 1, 2, \dots$，各能级不简并（[5.5.3](/5.5.3#sec-3.2.2)）。令 $\lambda^2 = \frac{h^2}{8mk_{\mathrm{B}}Ta^2}$，对宏观容器 $\lambda \sim 10^{-10}$，相邻项几乎相等，求和可以换成积分（从 $0$ 还是从 $1$ 开始积分只差 $O(\lambda)$ 的相对误差）：

$$
q_{\mathrm{t},x} = \sum_{n_x = 1}^{\infty}\mathrm{e}^{-\lambda^2n_x^2} \approx \int_0^{\infty}\mathrm{e}^{-\lambda^2n_x^2}\,\mathrm{d}n_x = \frac{\sqrt{\pi}}{2\lambda} = \frac{(2\pi mk_{\mathrm{B}}T)^{1/2}}{h}\,a,
$$
最后一步用了 **Gauss 积分**（[2.2.12](/2.2.12#sec-12.2.5)）。三维平动的能级 (10.1) 是三个方向之和，配分函数是三个一维配分函数之积（定理 11.1.1 的同一论证），$abc = V$：

**公式 11.2.1（平动配分函数）**

$$
q_{\mathrm{t}} = \left(\frac{2\pi mk_{\mathrm{B}}T}{h^2}\right)^{3/2}V = \frac{V}{\Lambda^3}.
\tag{11.2}
$$

**定义 11.2.1** 长度

$$
\Lambda = \frac{h}{\sqrt{2\pi mk_{\mathrm{B}}T}}
$$
称为分子的**热波长**（热 de Broglie 波长）。

$\Lambda$ 大致是热运动能量下分子的 de Broglie 波长，$q_{\mathrm{t}} = V/\Lambda^3$ 可以理解为"容器中能放下多少个边长为 $\Lambda$ 的小立方体"。10.2.3 节的条件 $g_i \gg N_i$ 等价于 $N/q_{\mathrm{t}} = N\Lambda^3/V \ll 1$：分子间的平均距离远大于热波长时，量子效应可以忽略，Boltzmann 统计适用。

**例 11.2.1** 计算 $298.15\,\mathrm{K}$、$p^\circ = 10^5\,\mathrm{Pa}$ 下 $1\,\mathrm{mol}$ $\ce{N2}$ 的平动配分函数。

**解** $m = 28.013\,\mathrm{u} = 4.652\times10^{-26}\,\mathrm{kg}$，$\Lambda = h/\sqrt{2\pi mk_{\mathrm{B}}T} = 1.91\times10^{-11}\,\mathrm{m} = 19.1\,\mathrm{pm}$，$V = RT/p^\circ = 2.479\times10^{-2}\,\mathrm{m^3}$，

$$
q_{\mathrm{t}} = \frac{V}{\Lambda^3} = 3.56\times10^{30}, \qquad \frac{q_{\mathrm{t}}}{N_{\mathrm{A}}} = 5.9\times10^6 \gg 1.
$$
（不少教材取 $V = 0.0245\,\mathrm{m^3}$，这对应旧的标准压力 $101.325\,\mathrm{kPa}$，而不是现行的 $p^\circ$。）每个分子平均有约 $6\times10^6$ 个可及的平动量子态，Boltzmann 统计完全适用。反过来，金属中的传导电子质量小、数密度大，$N\Lambda^3/V \sim 10^3$，必须用 Fermi–Dirac 统计（[5.5.6](/5.5.6)）。

由 $\ln q_{\mathrm{t}} = \frac{3}{2}\ln T + \ln V + $ 常数，平动对内能与热容的贡献为

$$
U_{\mathrm{t}} = Nk_{\mathrm{B}}T^2\left(\frac{\partial\ln q_{\mathrm{t}}}{\partial T}\right)_V = \frac{3}{2}Nk_{\mathrm{B}}T, \qquad C_{V,\mathrm{t}} = \frac{3}{2}Nk_{\mathrm{B}},
$$
与**能量均分定理**（[5.2.1](/5.2.1)）一致：平动能级极密，平动是完全"经典"的。

## 11.3. 转动配分函数

### 11.3.1. 异核双原子分子

把双原子分子看作刚性转子，转动惯量 $I = \mu r_{\mathrm{e}}^2$（$\mu$ 是**约化质量**），能级与简并度为（[5.5.5 公式 5.3.1](/5.5.5#fml-5.3.1)）

$$
\varepsilon_{\mathrm{r}} = J(J + 1)\frac{h^2}{8\pi^2I}, \qquad g_{\mathrm{r}} = 2J + 1, \qquad J = 0, 1, 2, \dots
$$
简并度来自角动量在空间的取向：角动量的 $z$ 分量量子数 $m_J = -J, -J + 1, \dots, J$，共 $2J + 1$ 个。

**定义 11.3.1** 称

$$
\Theta_{\mathrm{r}} = \frac{h^2}{8\pi^2Ik_{\mathrm{B}}} = \frac{hc\tilde B}{k_{\mathrm{B}}}
$$
为分子的**转动特征温度**，$\tilde B = h/(8\pi^2cI)$ 是以波数表示的转动常量。

于是 $q_{\mathrm{r}} = \sum_{J}(2J + 1)\mathrm{e}^{-J(J + 1)\Theta_{\mathrm{r}}/T}$。除 $\ce{H2}$、$\ce{HD}$ 等很轻的分子外，常温下 $\Theta_{\mathrm{r}} \ll T$，可以把求和换成积分：令 $x = J(J + 1)$，$\mathrm{d}x = (2J + 1)\,\mathrm{d}J$，

$$
q_{\mathrm{r}} \approx \int_0^\infty \mathrm{e}^{-x\Theta_{\mathrm{r}}/T}\,\mathrm{d}x = \frac{T}{\Theta_{\mathrm{r}}} = \frac{8\pi^2Ik_{\mathrm{B}}T}{h^2} \qquad (\text{异核}，T \gg \Theta_{\mathrm{r}}).
\tag{11.3}
$$

常见双原子分子的特征温度（由基态转动常数 $\tilde B_0$ 与振动基频 $\tilde\nu$ 计算；$\Theta_{\mathrm{v}}$ 见 11.4 节）：

| 分子 | $\ce{H2}$ | $\ce{N2}$ | $\ce{O2}$ | $\ce{CO}$ | $\ce{HCl}$ | $\ce{I2}$ |
|---|---|---|---|---|---|---|
| $\tilde B_0/\mathrm{cm^{-1}}$ | 59.32 | 1.990 | 1.438 | 1.923 | 10.44 | 0.0374 |
| $\Theta_{\mathrm{r}}/\mathrm{K}$ | 85.3 | 2.86 | 2.07 | 2.77 | 15.0 | 0.054 |
| $\tilde\nu/\mathrm{cm^{-1}}$ | 4161 | 2330 | 1556 | 2143 | 2886 | 214.5* |
| $\Theta_{\mathrm{v}}/\mathrm{K}$ | 5987 | 3352 | 2239 | 3084 | 4152 | 308 |

（* $\ce{I2}$ 取谐振常数 $\tilde\omega_{\mathrm{e}}$，基频 $213.3\,\mathrm{cm^{-1}}$ 给出 $307\,\mathrm{K}$。）

### 11.3.2. 对称数

同核双原子分子（$\ce{N2}$、$\ce{O2}$）绕垂直于键轴的轴转过 $180^\circ$ 后，与原来的构型完全不能区分。经典地看，式 (11.3) 的积分把每个可区分的取向数了两次；量子力学中，核的交换对称性使 $\ce{N2}$ 的偶数 $J$ 与奇数 $J$ 能级带不同的核自旋权重，$T \gg \Theta_{\mathrm{r}}$ 时效果是总和减半（11.5 节）。一般地，

**定义 11.3.2** 分子经过（真）转动所能达到的、彼此不可区分的空间取向数，称为分子的**对称数**，记作 $\sigma$。

$$
q_{\mathrm{r}} = \frac{T}{\sigma\Theta_{\mathrm{r}}} = \frac{8\pi^2Ik_{\mathrm{B}}T}{\sigma h^2} \qquad (\text{线形分子}，T \gg \Theta_{\mathrm{r}}).
\tag{11.4}
$$
异核双原子分子与 $\ce{N2O}$（$\ce{NNO}$）$\sigma = 1$，同核双原子分子与 $\ce{CO2}$ $\sigma = 2$；非线形分子中 $\ce{H2O}$、$\ce{SO2}$ 为 2，$\ce{NH3}$ 为 3，$\ce{CH4}$、$\ce{C6H6}$ 为 12。$\sigma$ 等于分子点群中纯转动操作（含恒等操作）的个数，用群论可以系统地求出。

**例 11.3.1** $\ce{N2}$ 的 $\Theta_{\mathrm{r}} = 2.86\,\mathrm{K}$（$I = h^2/(8\pi^2k_{\mathrm{B}}\Theta_{\mathrm{r}}) = 1.41\times10^{-46}\,\mathrm{kg\,m^2}$），$298.15\,\mathrm{K}$ 时

$$
q_{\mathrm{r}} = \frac{298.15}{2\times2.86} = 52.1.
$$
11.6.2 节表中 $\ce{N2}$ 的转动熵 $41.18\,\mathrm{J\,mol^{-1}\,K^{-1}}$ 就是由这个值算出的。

### 11.3.3. 求和与积分：修正级数

$\Theta_{\mathrm{r}}/T$ 不太小时，积分近似 (11.3) 偏低。用 Euler–Maclaurin 公式处理求和，得到 Mulholland 展开

$$
q_{\mathrm{r}} = \frac{T}{\sigma\Theta_{\mathrm{r}}}\left[1 + \frac{1}{3}\frac{\Theta_{\mathrm{r}}}{T} + \frac{1}{15}\left(\frac{\Theta_{\mathrm{r}}}{T}\right)^2 + \frac{4}{315}\left(\frac{\Theta_{\mathrm{r}}}{T}\right)^3 + \cdots\right].
\tag{11.5}
$$
$\ce{HCl}$（$\Theta_{\mathrm{r}} = 15.0\,\mathrm{K}$）在 $298.15\,\mathrm{K}$ 时精确求和得 $q_{\mathrm{r}} = 20.19$，积分近似给出 $19.85$（偏低 $1.7\%$，主要就是第二项 $\frac{1}{3}$），式 (11.5) 给出 $20.19$。$T \lesssim \Theta_{\mathrm{r}}$ 时级数失效，只能直接求和；同核分子在这个温度范围内还要考虑核自旋（11.5 节）。

![左：HCl 的转动配分函数，积分近似 T/Θr 与 Mulholland 展开（四项）相对于精确求和的比值，随 T/Θr 变化；右：298.15 K 时 HCl 与 CO 的转动能级布居，峰值位于 J ≈ (T/2Θr)^½ − ½](./plots/rotational-partition-function.py)

由 Boltzmann 分布，转动能级 $J$ 上的分子分数为 $(2J + 1)\mathrm{e}^{-J(J + 1)\Theta_{\mathrm{r}}/T}/q_{\mathrm{r}}$，在 $J_{\max} \approx \sqrt{T/(2\Theta_{\mathrm{r}})} - \frac{1}{2}$ 处最大：$298\,\mathrm{K}$ 时 $\ce{HCl}$ 为 $J = 3$，$\ce{CO}$ 为 $J = 7$。这正是红外振转光谱中 P 支与 R 支强度分布的来历（[5.5.5](/5.5.5#sec-5.3.3)）。

### 11.3.4. 非线形分子

非线形分子绕三个主轴转动，主转动惯量为 $I_A$、$I_B$、$I_C$，相应的特征温度 $\Theta_X = h^2/(8\pi^2I_Xk_{\mathrm{B}})$。高温下

$$
q_{\mathrm{r}} = \frac{\sqrt{\pi}}{\sigma}\left(\frac{T^3}{\Theta_A\Theta_B\Theta_C}\right)^{1/2} = \frac{\sqrt{\pi}}{\sigma}\left(\frac{8\pi^2k_{\mathrm{B}}T}{h^2}\right)^{3/2}\left(I_AI_BI_C\right)^{1/2}.
\tag{11.6}
$$
例如 $\ce{H2O}$ 的转动常量为 $27.88$、$14.51$、$9.28\,\mathrm{cm^{-1}}$，$\Theta = 40.1$、$20.9$、$13.4\,\mathrm{K}$，$\sigma = 2$，$298.15\,\mathrm{K}$ 时 $q_{\mathrm{r}} \approx 43$。

由 $q_{\mathrm{r}} \propto T$（线形）或 $T^{3/2}$（非线形），高温下转动的内能为 $Nk_{\mathrm{B}}T$ 或 $\frac{3}{2}Nk_{\mathrm{B}}T$，与能量均分定理一致。

## 11.4. 振动配分函数

双原子分子的振动看作简谐振动，能级是**量子谐振子**的能级（[5.5.3](/5.5.3#sec-3.4.2)），不简并：

$$
\varepsilon_{\mathrm{v}} = \left(v + \frac{1}{2}\right)h\nu, \qquad g_{\mathrm{v}} = 1, \qquad v = 0, 1, 2, \dots
$$

**定义 11.4.1** 称 $\Theta_{\mathrm{v}} = h\nu/k_{\mathrm{B}} = hc\tilde\nu/k_{\mathrm{B}}$ 为分子的**振动特征温度**。

振动能级等间隔且间隔大（11.3.1 节的表：$\Theta_{\mathrm{v}}$ 是数千开），不能换成积分，但求和是等比级数。以势能曲线的极小值为零点，振动配分函数（vibrational partition function）为

$$
q_{\mathrm{v}} = \sum_{v = 0}^\infty\mathrm{e}^{-(v + 1/2)\Theta_{\mathrm{v}}/T} = \frac{\mathrm{e}^{-\Theta_{\mathrm{v}}/(2T)}}{1 - \mathrm{e}^{-\Theta_{\mathrm{v}}/T}};
$$
以振动基态（$v = 0$）为零点，零点能 $\frac{1}{2}h\nu$ 归入 $U_0$，

$$
q_{\mathrm{v}}^{(0)} = \frac{1}{1 - \mathrm{e}^{-\Theta_{\mathrm{v}}/T}}.
\tag{11.7}
$$
后者更常用。

**例 11.4.1** $\ce{N2}$ 的振动基频 $\tilde\nu = 2329.9\,\mathrm{cm^{-1}}$，$\Theta_{\mathrm{v}} = 3352\,\mathrm{K}$。$298.15\,\mathrm{K}$ 时 $\Theta_{\mathrm{v}}/T = 11.24$，$q_{\mathrm{v}}^{(0)} = 1.000013$，处于 $v = 1$ 的分子只占 $1.3\times10^{-5}$：$\ce{N2}$ 的振动在常温下几乎完全"冻结"。

若改用 $\ce{N2}$ 的谐振常数 $\tilde\omega_{\mathrm{e}} = 2358.6\,\mathrm{cm^{-1}}$，则 $\Theta_{\mathrm{v}} = 3394\,\mathrm{K}$，比由基频算出的稍高；文献中两种取法都有，所以不同资料中的 $\Theta_{\mathrm{v}}$ 常略有出入。用谐振子模型描述真实分子时，取实测基频（$v = 0 \to 1$ 的间隔）能使最重要的低能级间隔准确，本章一律取基频；两种取法的差别只在高温下才明显，这时非谐性本身也必须考虑。

多原子分子有多个振动模式。$n$ 个原子共有 $3n$ 个自由度，减去 3 个平动与 3 个（线形分子 2 个）转动，剩下 $3n - 6$（线形 $3n - 5$）个**简正模式**，每个都是一个独立的谐振子：

$$
q_{\mathrm{v}}^{(0)} = \prod_{j = 1}^{3n - 6\ (3n - 5)}\frac{1}{1 - \mathrm{e}^{-\Theta_{\mathrm{v},j}/T}}.
$$
频率低的弯曲振动对室温热力学性质的贡献最大，例如 $\ce{CO2}$ 二重简并的弯曲振动 $667\,\mathrm{cm^{-1}}$（$\Theta_{\mathrm{v}} = 960\,\mathrm{K}$）。

## 11.5. 电子与核配分函数

电子能级没有统一的公式，大多数分子的第一激发态比基态高几个 $\mathrm{eV}$，$\Delta\varepsilon/(k_{\mathrm{B}}T) \gtrsim 10^2$。以基态为零点，

$$
q_{\mathrm{e}} = g_{\mathrm{e},0} + g_{\mathrm{e},1}\mathrm{e}^{-\Delta\varepsilon_1/(k_{\mathrm{B}}T)} + \cdots \approx g_{\mathrm{e},0}.
$$
基态的简并度由电子态决定：

- 原子：$g_{\mathrm{e},0} = 2J + 1$，$J$ 是基态**光谱项** $^{2S+1}L_J$ 的总角动量量子数（[5.5.4](/5.5.4#sec-4.2.4)）。例如 He、Ar（$^1\mathrm{S}_0$）为 1，Na（$^2\mathrm{S}_{1/2}$）为 2，卤素原子（$^2\mathrm{P}_{3/2}$）为 4，O 原子（$^3\mathrm{P}_2$）为 5。
- 分子：轨道角动量在键轴上的分量为零的 $\Sigma$ 态，$g_{\mathrm{e},0} = 2S + 1$（$S$ 是总自旋量子数）。闭壳层分子为 1，有一个未成对电子的自由基为 2，$\ce{O2}$（$^3\Sigma_{\mathrm{g}}^-$）为 3。$\Pi$、$\Delta$ 等态另有二重的轨道简并。

常见的经验规则"$g_{\mathrm{e},0} = n + 1$（$n$ 为未成对电子数）"只对 $\Sigma$ 态成立（$S = n/2$），并且只适用于激发态足够高的情形。$\ce{NO}$ 是一个反例：

**例 11.5.1** $\ce{NO}$ 的基态是 $^2\Pi_{1/2}$（$g = 2$），自旋–轨道耦合使 $^2\Pi_{3/2}$（$g = 2$）只高 $119.8\,\mathrm{cm^{-1}}$（$172\,\mathrm{K}$）。$298.15\,\mathrm{K}$ 时

$$
q_{\mathrm{e}} = 2 + 2\,\mathrm{e}^{-172/298.15} = 3.12,
$$
而不是 2。这对二能级在 $70\,\mathrm{K}$ 附近给 $\ce{NO}$ 的热容一个 Schottky 型的峰（[6.3.10 例 10.3.1](/6.3.10#ex-10.3.1)）。卤素原子的 $^2\mathrm{P}_{1/2}$ 激发态（碘原子高 $7603\,\mathrm{cm^{-1}}$）在 $1000\,\mathrm{K}$ 也贡献不到 $10^{-4}$，可以忽略。

原子核的激发能为 $\mathrm{MeV}$ 量级，除核反应外核总处于基态。以基态为零点，核配分函数只是核自旋的简并度：

$$
q_{\mathrm{n}} = \prod_k(2s_k + 1),
$$
$s_k$ 是分子中第 $k$ 个原子核的自旋量子数。质子数与中子数都是偶数的核 $s = 0$（$^{12}\mathrm{C}$、$^{16}\mathrm{O}$、$^{32}\mathrm{S}$）；一个为奇数、另一个为偶数时 $s$ 为半整数（$^1\mathrm{H}$、$^{13}\mathrm{C}$、$^{31}\mathrm{P}$ 为 $\frac{1}{2}$，$^7\mathrm{Li}$、$^{11}\mathrm{B}$、$^{35}\mathrm{Cl}$ 为 $\frac{3}{2}$）；两者都是奇数时 $s$ 为整数（$^2\mathrm{H}$、$^6\mathrm{Li}$、$^{14}\mathrm{N}$ 为 1）。$s \neq 0$ 的核是核磁共振的研究对象。化学反应不改变原子核，$q_{\mathrm{n}}$ 在反应前后的乘积相同，在平衡常数和反应熵中相消，所以通常略去。

例外是低温下的同核双原子分子。$\ce{H2}$ 的两个质子是费米子，总波函数对交换两核必须反对称：核自旋三重态（权重 3）只能与奇数 $J$ 组合，这种 $\ce{H2}$ 称为正氢（orthohydrogen）；核自旋单重态（权重 1）只能与偶数 $J$ 组合，称为仲氢（parahydrogen）。高温下奇数 $J$ 与偶数 $J$ 的转动求和各约为全部求和的一半，$q_{\mathrm{r}}q_{\mathrm{n}} \approx (3 + 1)\cdot\frac{1}{2}\cdot\frac{T}{\Theta_{\mathrm{r}}}$，效果正是对称数 $\sigma = 2$ 与 $q_{\mathrm{n}} = 4$；低温下必须分别计算两种 $\ce{H2}$。没有催化剂时两者的相互转化极慢，普通氢气在低温下是正氢与仲氢 $3:1$ 的亚稳混合物，它的热容与按平衡计算的结果不同（[5.2.3](/5.2.3) 中 $\ce{H2}$ 热容的讨论）。

## 11.6. 理想气体的热力学性质

### 11.6.1. 内能与热容

由 $U = Nk_{\mathrm{B}}T^2(\partial\ln q/\partial T)_V + U_0$ 与各配分函数，$1\,\mathrm{mol}$ 理想气体的内能为

$$
U_{\mathrm{m}} = U_{0,\mathrm{m}} + \frac{3}{2}RT + \underbrace{RT\ \text{或}\ \frac{3}{2}RT}_{\text{转动，线形或非线形}} + \sum_j\frac{R\Theta_{\mathrm{v},j}}{\mathrm{e}^{\Theta_{\mathrm{v},j}/T} - 1} + U_{\mathrm{e},\mathrm{m}},
\tag{11.8}
$$
其中振动项由 $\ln q_{\mathrm{v}}^{(0)} = -\ln(1 - \mathrm{e}^{-\Theta_{\mathrm{v}}/T})$ 求导得到。各项都只与 $T$ 有关：理想气体的 $U$ 只是温度的函数，而它的具体形式由分子的结构（$\Theta_{\mathrm{v}}$ 等）决定。对 $T$ 求导，单原子气体 $C_{V,\mathrm{m}} = \frac{3}{2}R$（电子激发态可以忽略时，在任何温度下都成立）；双原子气体

$$
C_{V,\mathrm{m}} = \frac{5}{2}R + R\,\frac{(\Theta_{\mathrm{v}}/T)^2\,\mathrm{e}^{\Theta_{\mathrm{v}}/T}}{\left(\mathrm{e}^{\Theta_{\mathrm{v}}/T} - 1\right)^2} \qquad (T \gg \Theta_{\mathrm{r}}).
\tag{11.9}
$$
振动项中的函数 $E(x) = x^2\mathrm{e}^x/(\mathrm{e}^x - 1)^2$（$x = \Theta_{\mathrm{v}}/T$）称为 Einstein 函数（Einstein function），Einstein 在 1907 年用它解释了固体热容在低温下的下降。它的两个极限说明了能量均分定理的适用范围：

- $T \ll \Theta_{\mathrm{v}}$（$x \gg 1$）：$E(x) \approx x^2\mathrm{e}^{-x} \to 0$，振动被"冻结"，双原子气体 $C_{V,\mathrm{m}} = \frac{5}{2}R$。常温下大多数双原子气体处于这一情形（[6.3.1](/6.3.1)）。
- $T \gg \Theta_{\mathrm{v}}$（$x \to 0$）：$E(x) \to 1$，每个振动模式贡献 $R$（动能与势能各 $\frac{1}{2}R$），$C_{V,\mathrm{m}} \to \frac{7}{2}R$，即能量均分定理的结果。

能量均分定理只在能级间隔远小于 $k_{\mathrm{B}}T$ 时成立；这是量子能级在热力学中最直接的表现（[5.5.3](/5.5.3#sec-3.4.2)、[5.2.3](/5.2.3)）。例如 $\ce{N2}$ 在 $1000\,\mathrm{K}$ 时 $E(3.35) = 0.42$，$C_{V,\mathrm{m}} = 24.30\,\mathrm{J\,mol^{-1}\,K^{-1}}$，实测（$C_{p,\mathrm{m}} - R$）为 $24.39\,\mathrm{J\,mol^{-1}\,K^{-1}}$，剩下的差别来自非谐性与振转耦合。$\Theta_{\mathrm{v}}$ 低的重分子（$\ce{I2}$、$\ce{Br2}$）在室温下振动已经相当程度地激发。

![左：理想气体 HCl 的 CV,m/R 及其平动、转动、振动贡献（刚性转子–谐振子模型，转动按精确求和），点线标出 Θr 与 Θv；右：I₂、N₂、HCl 的振动贡献（Einstein 函数），竖线为 298.15 K](./plots/heat-capacity-contributions.py)

图中转动热容在 $T \approx 0.8\,\Theta_{\mathrm{r}}$ 附近略高于 $R$，这是能级分立的效应；实际上 $\ce{HCl}$ 在这个温度下早已凝结，只有 $\ce{H2}$、$\ce{D2}$ 能在气相中观测到转动热容的变化。

### 11.6.2. 统计熵

**定义 11.6.1** 由分子的光谱数据（质量、转动惯量、振动频率、电子能级）通过配分函数计算的熵称为**统计熵**（光谱熵）。

按 $S = k_{\mathrm{B}}\ln(q^N/N!) + U/T$，统计熵可以分解为平动、转动、振动与电子的贡献（核自旋的贡献在化学中略去，11.5 节）。平动熵把 $\ln N!$ 包含在内：

$$
S_{\mathrm{t}} = k_{\mathrm{B}}\ln\frac{q_{\mathrm{t}}^N}{N!} + \frac{U_{\mathrm{t}}}{T} = Nk_{\mathrm{B}}\left(\ln\frac{q_{\mathrm{t}}}{N} + 1\right) + \frac{3}{2}Nk_{\mathrm{B}}.
$$
再用 $q_{\mathrm{t}}/N = V/(N\Lambda^3) = k_{\mathrm{B}}T/(p\Lambda^3)$，就得到

**定理 11.6.1（Sackur–Tetrode 方程）** 理想气体的摩尔平动熵为

$$
S_{\mathrm{m},\mathrm{t}} = R\left[\ln\left(\frac{(2\pi mk_{\mathrm{B}}T)^{3/2}}{h^3}\cdot\frac{k_{\mathrm{B}}T}{p}\right) + \frac{5}{2}\right].
\tag{11.10}
$$

它对单原子与多原子气体都适用（$m$ 是分子的质量）；单原子气体的熵就是它（加上电子项 $R\ln g_{\mathrm{e},0}$）。方程说明：平动熵随 $T$ 升高、$p$ 降低（$V$ 增大）而增大；随分子质量增大而增大，因为质量越大，平动能级越密，可及的状态越多。方程中出现了 Planck 常量：经典统计只能确定熵的差，熵的绝对值需要量子力学提供"状态的单位"。

其他运动的熵由 $S = Nk_{\mathrm{B}}\ln q + U/T$ 得到（线形分子，$x = \Theta_{\mathrm{v}}/T$）：

$$
S_{\mathrm{m},\mathrm{r}} = R\left(\ln\frac{T}{\sigma\Theta_{\mathrm{r}}} + 1\right), \qquad S_{\mathrm{m},\mathrm{v}} = R\left[\frac{x}{\mathrm{e}^x - 1} - \ln\left(1 - \mathrm{e}^{-x}\right)\right], \qquad S_{\mathrm{m},\mathrm{e}} = R\ln g_{\mathrm{e},0}.
\tag{11.11}
$$

**例 11.6.1** $298.15\,\mathrm{K}$、$p^\circ$ 下几种气体的统计熵（$\mathrm{J\,mol^{-1}\,K^{-1}}$），与热力学数据表（CRC）中的 $S^\circ_{\mathrm{m}}$ 比较：

| 气体 | $S_{\mathrm{m},\mathrm{t}}$ | $S_{\mathrm{m},\mathrm{r}}$ | $S_{\mathrm{m},\mathrm{v}}$ | $S_{\mathrm{m},\mathrm{e}}$ | 合计 | 表值 $S^\circ_{\mathrm{m}}$ |
|---|---|---|---|---|---|---|
| He | 126.15 | — | — | 0 | 126.15 | 126.15 |
| Ar | 154.85 | — | — | 0 | 154.85 | 154.85 |
| $\ce{N2}$ | 150.42 | 41.18 | 0.001 | 0 | 191.60 | 191.61 |
| $\ce{O2}$ | 152.08 | 43.88 | 0.04 | 9.13 | 205.13 | 205.15 |

对于这样简单的分子，统计熵与表值吻合到 $0.01$–$0.02\,\mathrm{J\,mol^{-1}\,K^{-1}}$：事实上，气体的表值多半就是由光谱数据计算的。平动熵占绝大部分；$\ce{O2}$ 的三重态基态贡献 $R\ln 3 = 9.13$，不计入它就会差得很远。（按旧的标准压力 $101.325\,\mathrm{kPa}$ 计算，各值小 $R\ln 1.01325 = 0.11$，例如 He 为 $126.04$。）

**例 11.6.2** $\ce{N2}$ 与 $\ce{CO}$ 的摩尔质量几乎相同（$28.01$），转动惯量也很接近，常温下振动与电子都未激发，为什么 $S^\circ_{\mathrm{m}}(\ce{CO}) = 197.66$ 比 $S^\circ_{\mathrm{m}}(\ce{N2}) = 191.61\,\mathrm{J\,mol^{-1}\,K^{-1}}$ 大 $6.05$？

**解** 主要是**对称数**：$\ce{N2}$ 的 $\sigma = 2$，$\ce{CO}$ 的 $\sigma = 1$，转动熵相差 $R\ln 2 = 5.76$。其余 $0.3$ 来自 $\Theta_{\mathrm{r}}$（$2.77$ 与 $2.86\,\mathrm{K}$）与振动频率的微小差别。

**例 11.6.3** $1\,\mathrm{mol}$ He 从 $(T_1, V_1)$ 变到 $(T_2, V_2)$，求 $\Delta S$。

**解** 只有平动熵变化。由式 (11.10)（用 $V$ 表示），$S_{\mathrm{m}} = R\ln(T^{3/2}V) + $ 常数，

$$
\Delta S_{\mathrm{m}} = \frac{3}{2}R\ln\frac{T_2}{T_1} + R\ln\frac{V_2}{V_1},
$$
与经典热力学设计可逆途径（等容变温加等温变容，$C_{V,\mathrm{m}} = \frac{3}{2}R$，[6.3.2](/6.3.2#sec-2.3.2)）的结果相同。

理想气体等温等压混合时（[6.3.2 定义 2.3.1](/6.3.2#def-2.3.1)），每种分子的活动范围由 $V_{\mathrm{B}}$ 扩大到 $V$，平动配分函数按 $V/V_{\mathrm{B}} = 1/x_{\mathrm{B}}$ 增大，转动、振动等不变，所以**混合熵**全部来自平动熵：$\Delta_{\mathrm{mix}}S = \sum_{\mathrm{B}} n_{\mathrm{B}}R\ln(V/V_{\mathrm{B}}) = -R\sum_{\mathrm{B}} n_{\mathrm{B}}\ln x_{\mathrm{B}}$。若两边是同一种气体，抽去隔板后分子不可区分，$q^N/N!$ 中的 $N!$ 使熵变为零（Gibbs 佯谬的解决）。

### 11.6.3. 统计熵与量热熵：残余熵

量热熵（[6.3.2](/6.3.2#sec-2.4.2)）以 $0\,\mathrm{K}$ 完美晶体的熵为零，由热容与相变焓积分得到；统计熵直接由气体分子的能级算出。两者原本独立，对大多数物质在实验误差内相等，这是第三定律最有力的证据。但有些物质的统计熵明显大于量热熵。

**定义 11.6.2** 同一物质在同一状态下的统计熵与量热熵之差 $S_{\text{统计}} - S_{\text{量热}}$ 称为**残余熵**。它是 $0\,\mathrm{K}$ 时晶体中仍然存在的无序所对应的熵，量热法测不到这一部分。

**例 11.6.4（CO）** $298.15\,\mathrm{K}$、$p^\circ$ 下 $\ce{CO}$ 的统计熵为 $197.7$，量热熵约为 $193.3\,\mathrm{J\,mol^{-1}\,K^{-1}}$，残余熵约 $4.4$。$\ce{CO}$ 分子两端相似，电偶极矩很小（约 $0.1\,\mathrm{D}$），在晶体中以 CO 或 OC 两种取向排列的能量几乎相同。凝固时取向被随机冻结，低温下分子没有足够的能量翻转，排列不再趋于有序。若每个分子都有两种取向、完全随机，$\Omega = 2^{N_{\mathrm{A}}}$，

$$
S_{\text{残余},\mathrm{m}} = k_{\mathrm{B}}\ln 2^{N_{\mathrm{A}}} = R\ln 2 = 5.76\,\mathrm{J\,mol^{-1}\,K^{-1}}.
$$
实测值略小于它，说明冻结时已有部分有序。

其他典型例子：

- $\ce{N2O}$（NNO 与 ONN 两种取向）：约 $4.8$，同样接近 $R\ln 2$。
- 冰：氢原子位置的无序，Pauling 估计为 $R\ln\frac{3}{2} = 3.37$，实测约 $3.4$（[6.3.2](/6.3.2#sec-2.4.2)）。
- $\ce{NO}$：晶体由 $\ce{(NO)2}$ 二聚体组成，每个二聚体有两种取向，每摩尔 $\ce{NO}$ 约 $\frac{1}{2}R\ln 2 = 2.9$，实测约 $3$。
- $\ce{H2}$：差别来自正氢与仲氢在低温下不能达到平衡（11.5 节），不是取向的无序。

热力学数据表中这些物质的 $S^\circ_{\mathrm{m}}$ 采用统计熵：在这一点上统计热力学比量热法更可靠。

### 11.6.4. 例：由统计熵求蒸气压

**例 11.6.5** 已知 $84\,\mathrm{K}$ 时固态 Ar 的摩尔熵为 $38.3\,\mathrm{J\,mol^{-1}\,K^{-1}}$，摩尔升华焓为 $7940\,\mathrm{J\,mol^{-1}}$。设 Ar 蒸气是理想气体，求 $84\,\mathrm{K}$ 时固态 Ar 的平衡蒸气压 $p$。

**解** 固气平衡时 $\Delta_{\mathrm{sub}}G_{\mathrm{m}} = 0$，$\Delta_{\mathrm{sub}}S_{\mathrm{m}} = \Delta_{\mathrm{sub}}H_{\mathrm{m}}/T$，所以蒸气在平衡压力 $p$ 下的摩尔熵为（固体的熵受压力的影响可以忽略）

$$
S_{\mathrm{m}}(\mathrm{g}, p) = S_{\mathrm{m}}(\mathrm{s}) + \frac{\Delta_{\mathrm{sub}}H_{\mathrm{m}}}{T} = 38.3 + \frac{7940}{84} = 132.8\,\mathrm{J\,mol^{-1}\,K^{-1}}.
$$
另一方面，由 Sackur–Tetrode 方程 (11.10)，$84\,\mathrm{K}$、$p^\circ$ 下 $S_{\mathrm{m}}(\mathrm{g}, p^\circ) = 128.5\,\mathrm{J\,mol^{-1}\,K^{-1}}$，且 $S_{\mathrm{m}}(\mathrm{g}, p) = S_{\mathrm{m}}(\mathrm{g}, p^\circ) - R\ln(p/p^\circ)$。于是

$$
\ln\frac{p}{p^\circ} = \frac{128.5 - 132.8}{8.314} = -0.52, \qquad p \approx 0.60\,p^\circ = 60\,\mathrm{kPa}.
$$
Ar 的三相点为 $83.81\,\mathrm{K}$、$68.9\,\mathrm{kPa}$，计算值偏低约 $14\%$。$\ln p$ 的误差 $0.14$ 只对应熵的误差 $0.14R = 1.2\,\mathrm{J\,mol^{-1}\,K^{-1}}$，在所给数据的精度之内：由熵求蒸气压对数据非常敏感。这个例子的意义在于，它只用了凝聚相的量热数据与气体分子的质量，就从"第一原理"给出了蒸气压的正确量级。

## 11.7. 由配分函数求平衡常数

### 11.7.1. 理想气体的标准化学势

由式 (10.15)，理想气体中分子 B 的化学势为 $\mu_{\mathrm{B}} = -k_{\mathrm{B}}T\ln(q_{\mathrm{B}}/N_{\mathrm{B}})$，其中 $q_{\mathrm{B}}$ 的能量必须从所有物种共同的零点算起。记 B 的分子基态能量为 $\varepsilon_{0,\mathrm{B}}$，以基态为零点的配分函数为 $q_{\mathrm{B}}^{(0)}$，则 $q_{\mathrm{B}} = q_{\mathrm{B}}^{(0)}\mathrm{e}^{-\varepsilon_{0,\mathrm{B}}/(k_{\mathrm{B}}T)}$。乘以 $N_{\mathrm{A}}$ 得摩尔量（$U_{0,\mathrm{m}}(\mathrm{B}) = N_{\mathrm{A}}\varepsilon_{0,\mathrm{B}}$）：

$$
\mu_{\mathrm{B}} = U_{0,\mathrm{m}}(\mathrm{B}) - RT\ln\frac{q_{\mathrm{B}}^{(0)}}{N_{\mathrm{B}}}.
$$
$q_{\mathrm{B}}^{(0)}$ 只通过平动因子与 $V$ 成正比，而理想气体混合物中 $N_{\mathrm{B}}/V = p_{\mathrm{B}}/(k_{\mathrm{B}}T)$，所以

$$
\frac{q_{\mathrm{B}}^{(0)}}{N_{\mathrm{B}}} = \frac{q_{\mathrm{B}}^{(0)}}{V}\cdot\frac{k_{\mathrm{B}}T}{p_{\mathrm{B}}} = \frac{q_{\mathrm{B}}^\circ}{N_{\mathrm{A}}}\cdot\frac{p^\circ}{p_{\mathrm{B}}}, \qquad q_{\mathrm{B}}^\circ = q_{\mathrm{B}}^{(0)}\Big|_{V = V^\circ_{\mathrm{m}} = RT/p^\circ},
$$
$q_{\mathrm{B}}^\circ$ 是 B 在标准摩尔体积中的分子配分函数。代入并与 $\mu_{\mathrm{B}} = \mu_{\mathrm{B}}^\circ + RT\ln(p_{\mathrm{B}}/p^\circ)$（[6.3.4](/6.3.4#sec-4.4.2)）比较，

$$
\mu_{\mathrm{B}}^\circ(T) = U_{0,\mathrm{m}}(\mathrm{B}) - RT\ln\frac{q_{\mathrm{B}}^\circ}{N_{\mathrm{A}}}.
\tag{11.12}
$$
标准化学势只与温度有关；$q_{\mathrm{B}}^\circ/N_{\mathrm{A}}$ 是标准态下每个分子可及的量子态数（$\ce{N2}$ 在 $298\,\mathrm{K}$ 约为 $6\times10^6\times52\approx3\times10^8$）。热力学数据表中的"Gibbs 自由能函数" $[G^\circ_{\mathrm{m}}(T) - H^\circ_{\mathrm{m}}(0\,\mathrm{K})]/T = -R\ln(q^\circ/N_{\mathrm{A}})$ 就是这样由光谱数据算出的。

### 11.7.2. 标准平衡常数

**定理 11.7.1** 理想气体反应 $0 = \sum_{\mathrm{B}}\nu_{\mathrm{B}}\mathrm{B}$ 的**标准平衡常数**为

$$
K^\circ = \prod_{\mathrm{B}}\left(\frac{q_{\mathrm{B}}^\circ}{N_{\mathrm{A}}}\right)^{\nu_{\mathrm{B}}}\exp\left(-\frac{\Delta_{\mathrm{r}}U_0}{RT}\right), \qquad \Delta_{\mathrm{r}}U_0 = \sum_{\mathrm{B}}\nu_{\mathrm{B}}U_{0,\mathrm{m}}(\mathrm{B}).
\tag{11.13}
$$

**证明** 由**标准摩尔反应 Gibbs 自由能**的定义与式 (11.12)，$\Delta_{\mathrm{r}}G^\circ_{\mathrm{m}} = \sum_{\mathrm{B}}\nu_{\mathrm{B}}\mu^\circ_{\mathrm{B}} = \Delta_{\mathrm{r}}U_0 - RT\sum_{\mathrm{B}}\nu_{\mathrm{B}}\ln(q^\circ_{\mathrm{B}}/N_{\mathrm{A}})$；再由 $K^\circ = \exp(-\Delta_{\mathrm{r}}G^\circ_{\mathrm{m}}/(RT))$（[6.3.7 定义 7.2.2](/6.3.7#def-7.2.2)）即得。$\square$

$\Delta_{\mathrm{r}}U_0$ 是反应在 $0\,\mathrm{K}$ 的能量变化，即产物与反应物的振动基态能量之差，可由光谱或量子化学计算得到；对双原子分子的解离 $\ce{A2 -> 2A}$，$\Delta_{\mathrm{r}}U_0 = N_{\mathrm{A}}D_0$，$D_0$ 是从振动基态算起的解离能（比势能曲线的阱深 $D_{\mathrm{e}}$ 少零点能 $\frac{1}{2}h\nu$）。

式 (11.13) 清楚地显示了决定平衡的两个因素：指数因子是能量，偏向能量低的一方；配分函数之比是可及状态数，偏向状态多的一方（熵）。温度升高，能量因子的作用减弱，平衡移向配分函数大的一方，例如分子解离成原子（原子的平动配分函数大）。它也是 [6.3.16](/6.3.16) 中过渡态理论的出发点：把活化络合物看作与反应物处于准平衡的物种，用式 (11.13) 写出这一"平衡常数"，只是要把沿反应坐标的那个振动单独处理。

### 11.7.3. 例题

**例 11.7.1（碘的解离）** 计算 $\ce{I2(g) <=> 2I(g)}$ 在 $1000\,\mathrm{K}$ 的 $K^\circ$。已知 $\ce{I2}$：$\tilde B = 0.03737\,\mathrm{cm^{-1}}$（$\Theta_{\mathrm{r}} = 0.0538\,\mathrm{K}$），$\tilde\omega_{\mathrm{e}} = 214.5\,\mathrm{cm^{-1}}$（$\Theta_{\mathrm{v}} = 308.6\,\mathrm{K}$），基态不简并，$D_0 = 12441\,\mathrm{cm^{-1}}$（$148.8\,\mathrm{kJ\,mol^{-1}}$）；I 原子基态为 $^2\mathrm{P}_{3/2}$（$g = 4$）。

**解** 逐项计算（$T = 1000\,\mathrm{K}$，$p^\circ = 10^5\,\mathrm{Pa}$）：

| 量 | I | $\ce{I2}$ |
|---|---|---|
| $q_{\mathrm{t}}^\circ/N_{\mathrm{A}} = k_{\mathrm{B}}T/(p^\circ\Lambda^3)$ | $1.173\times10^9$ | $3.318\times10^9$ |
| $q_{\mathrm{r}} = T/(2\Theta_{\mathrm{r}})$ | — | $9299$ |
| $q_{\mathrm{v}}^{(0)} = 1/(1 - \mathrm{e}^{-\Theta_{\mathrm{v}}/T})$ | — | $3.766$ |
| $q_{\mathrm{e}}$ | $4$ | $1$ |

$$
K^\circ = \frac{(1.173\times10^9\times4)^2}{3.318\times10^9\times9299\times3.766}\,\exp\left(-\frac{hcD_0}{k_{\mathrm{B}}T}\right) = 1.89\times10^5\times\mathrm{e}^{-17.90} = 3.19\times10^{-3}.
$$
作为对照，由 CRC 的 $298.15\,\mathrm{K}$ 热力学数据（$\Delta_{\mathrm{f}}H^\circ$、$S^\circ_{\mathrm{m}}$、$C_{p,\mathrm{m}}$）按 **Kirchhoff 定律**校正到 $1000\,\mathrm{K}$，得 $\Delta_{\mathrm{r}}G^\circ_{\mathrm{m}} = 47.8\,\mathrm{kJ\,mol^{-1}}$，$K^\circ = 3.2\times10^{-3}$，两者一致。总压为 $p^\circ$ 时解离度 $\alpha = \sqrt{K^\circ/(K^\circ + 4)} = 0.028$。配分函数之比约 $2\times10^5$，几乎全部来自两个 I 原子的平动（每个原子在标准体积中有 $10^9$ 个状态）对 $\ce{I2}$ 的平动、转动、振动；它与很小的能量因子 $\mathrm{e}^{-17.9}$ 竞争，决定了解离只在高温下显著。

```python
import numpy as np

h, kB, NA, c = 6.62607015e-34, 1.380649e-23, 6.02214076e23, 299792458.0
c2 = h * c * 100 / kB                      # hc/kB in cm K
T, p0 = 1000.0, 1e5


def qt_per_molecule(M):                    # q_t / N_A at the standard molar volume
    m = M * 1e-3 / NA
    return (2 * np.pi * m * kB * T / h**2) ** 1.5 * kB * T / p0


q_I = qt_per_molecule(126.904) * 4                                   # 2P3/2 ground level
q_I2 = (qt_per_molecule(253.809) * T / (2 * c2 * 0.03737)
        / (1 - np.exp(-c2 * 214.5 / T)))                             # rotation, vibration
K = q_I**2 / q_I2 * np.exp(-c2 * 12440.9 / T)
print(f"K = {K:.3g}")                                                # K = 0.00319
```

![I₂(g) ⇌ 2I(g)。左：lg K° 随 1000 K/T 的变化，由配分函数计算（实线）与由 298.15 K 热力学数据按恒定 ΔrCp（虚线）或 ΔrCp = 0（点线）外推的结果；右：总压为 p° 时的解离度](./plots/iodine-dissociation.py)

**例 11.7.2（同位素交换）** 对 $\ce{H2 + D2 <=> 2HD}$，$\Delta\nu = 0$，配分函数中的 $V$、$T$ 因子大部分相消。高温下各配分函数都取经典形式，质量与转动惯量的因子恰好全部相消，只剩下对称数：

$$
K^\circ \to \frac{\sigma(\ce{H2})\,\sigma(\ce{D2})}{\sigma(\ce{HD})^2} = 4.
$$
这就是 H、D 原子随机配对的组合数之比（$\ce{HD}$ 有两种"排法"）。按 $\ce{H2}$、$\ce{D2}$、$\ce{HD}$ 的光谱常数与零点能逐项计算，$298\,\mathrm{K}$ 时 $K^\circ = 3.26$，$1000\,\mathrm{K}$ 时 $3.90$，与实验值相符。低温下偏离 4，是因为三种分子的零点能不同（$\Delta_{\mathrm{r}}U_0 > 0$）：这种量子效应是同位素分馏与动力学同位素效应的根源。

## 小结

| 运动 | 配分函数（以基态为零点） | 对 $U_{\mathrm{m}}$ 的贡献（高温极限） | 对 $S_{\mathrm{m}}$ 的贡献 |
|---|---|---|---|
| 平动 | $V/\Lambda^3$，$\Lambda = h/\sqrt{2\pi mk_{\mathrm{B}}T}$ | $\frac{3}{2}RT$ | Sackur–Tetrode 方程 (11.10) |
| 转动（线形） | $T/(\sigma\Theta_{\mathrm{r}})$；修正见 (11.5) | $RT$ | $R[\ln(T/\sigma\Theta_{\mathrm{r}}) + 1]$ |
| 转动（非线形） | 式 (11.6) | $\frac{3}{2}RT$ | $R[\ln q_{\mathrm{r}} + \frac{3}{2}]$ |
| 振动（每个模式） | $1/(1 - \mathrm{e}^{-\Theta_{\mathrm{v}}/T})$ | $R\Theta_{\mathrm{v}}/(\mathrm{e}^{\Theta_{\mathrm{v}}/T} - 1) \to RT$ | 式 (11.11) |
| 电子 | $g_{\mathrm{e},0}$（激发态低时加项） | 0 | $R\ln g_{\mathrm{e},0}$ |
| 核 | $\prod(2s_k + 1)$，化学中略去 | 0 | 略去 |

- 能量均分定理只对能级间隔 $\ll k_{\mathrm{B}}T$ 的运动成立：常温下平动、转动是经典的，振动多半被冻结，电子与核只处于基态。
- 统计熵与量热熵一般吻合；残余熵来自 $0\,\mathrm{K}$ 时冻结的无序（$\ce{CO}$ 接近 $R\ln 2$）。
- $K^\circ = \prod_{\mathrm{B}}(q^\circ_{\mathrm{B}}/N_{\mathrm{A}})^{\nu_{\mathrm{B}}}\mathrm{e}^{-\Delta_{\mathrm{r}}U_0/(RT)}$：平衡由能量与可及状态数的竞争决定。

## 思考题

1. 单原子理想气体的 Sackur–Tetrode 方程能否用来计算双原子气体的平动熵？标准压力下摩尔平动熵与哪些因素有关？
   答：能，平动只涉及质心的运动，$m$ 取分子的质量即可。$p = p^\circ$ 给定时，$S^\circ_{\mathrm{m},\mathrm{t}}$ 只与 $T$ 和分子质量 $m$ 有关；体积已由 $V^\circ_{\mathrm{m}} = RT/p^\circ$ 确定，不是独立的因素。
2. 为什么 $\ce{H2}$ 的转动配分函数在常温下也不宜用 $T/(\sigma\Theta_{\mathrm{r}})$ 计算？
   答：$\Theta_{\mathrm{r}} = 85.3\,\mathrm{K}$，$298\,\mathrm{K}$ 时 $\Theta_{\mathrm{r}}/T \approx 0.29$，积分近似的误差约 $10\%$，需用修正级数 (11.5) 或直接求和；温度更低时还必须分别处理正氢与仲氢。
3. 零点能的选择会不会影响由配分函数计算的反应 $\Delta_{\mathrm{r}}G^\circ_{\mathrm{m}}$？
   答：只要所有物种的能量从同一零点算起就不会。各物种都以自己的基态为零点计算 $q^{(0)}$ 时，必须补上 $\Delta_{\mathrm{r}}U_0$ 一项，否则结果毫无意义。
4. 由例 11.7.1 的数据说明，为什么升高温度、降低压力都有利于 $\ce{I2}$ 的解离？
   答：$\Delta_{\mathrm{r}}U_0 > 0$，温度升高使 $\mathrm{e}^{-\Delta_{\mathrm{r}}U_0/(RT)}$ 增大（吸热反应，van 't Hoff 方程）；$\Delta\nu_{\mathrm{g}} = 1$，降低压力相当于增大每个分子可及的平动状态数，有利于分子数增加的一方。
