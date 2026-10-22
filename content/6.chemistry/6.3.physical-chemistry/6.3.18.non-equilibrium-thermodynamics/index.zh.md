---
title: 非平衡态热力学
description: 熵流与熵产生、局域平衡与熵平衡方程；线性区的唯象关系、Onsager 倒易关系、交叉效应、膜输运与主动运输、最小熵产生原理；远离平衡的耗散结构、Brusselator 振荡与 Hopf 分岔、BZ 反应、Turing 斑图；生命系统的负熵流。
---

前面各章的热力学只处理平衡态，以及由平衡态连成的可逆过程：对不可逆过程，它只给出方向（$\Delta S_{\text{孤立}} > 0$、$\Delta G < 0$），不回答"多快"和"怎样耦合"。可是自然界中引人注目的现象几乎都发生在非平衡条件下：沿温度梯度的热传导、膜两侧的物质输运、持续进行的化学反应，以及化学振荡、空间斑图和生命本身。本章把热力学推广到非平衡系统。18.1 节把熵的变化分解为熵流与熵产生，并在局域平衡假设下写出熵平衡方程，熵产生由此表示为"通量 × 力"之和；18.2 节讨论近平衡的线性区：唯象关系、Onsager 倒易关系及其微观依据、热电与热扩散等交叉效应、膜输运方程与生物膜上的主动运输，以及最小熵产生原理；18.3 节进入远离平衡的非线性区，用前三章的动力学（[6.3.15](/6.3.15)–[6.3.17](/6.3.17)）和常微分方程的稳定性理论（[2.4.11](/2.4.11)）分析化学振荡与 Turing 斑图，说明有序结构怎样靠持续的耗散维持；18.4 节回到生命系统，与物理中的**熵增加原理**（[5.2.4](/5.2.4#thm-4.6.2)）和 [6.3.2](/6.3.2) 末尾的引子呼应。本章是物理化学与生物物理衔接最紧的一章：细胞是开放的、远离平衡的系统，它的能量转换、输运和计时都要用这里的语言描述。

## 18.1. 熵流与熵产生

### 18.1.1. 平衡、稳态与远离平衡

热力学的发展大致经历三个阶段：

| 阶段 | 研究对象 | 核心结果 |
|---|---|---|
| 平衡态热力学（经典热力学） | 平衡态，可逆过程；不可逆过程只判断方向 | 四个定律，状态函数，自由能判据 |
| 线性非平衡态热力学 | 近平衡的开放系统，通量与力成线性关系 | 局域平衡，Onsager 倒易关系，最小熵产生原理 |
| 非线性非平衡态热力学 | 远离平衡的开放系统，非线性的不可逆过程 | 稳定性理论，耗散结构，涨落与分岔 |

平衡态与**稳定态**必须区分（[5.2.1](/5.2.1)）：两端接在不同温度热库上的金属杆，经过足够长时间后各点温度不再变化，但始终有热流通过，这是稳定态而不是平衡态。平衡态没有任何宏观的流，也不产生熵；稳定态要靠外界持续供给而维持，内部始终在产生熵。本章所说的"非平衡稳态"都是这个意义。

19 世纪的经典热力学留下了两个困惑。一是 Clausius（1867）把熵增加原理推广到整个宇宙，得出"热寂"的结论：宇宙的熵趋于极大，一切宏观变化终将停止。Boltzmann 指出平衡态本身伴随着涨落；今天看来，这一推广的前提——宇宙是有限的孤立系统、存在通常意义上的平衡态——都不清楚（宇宙在膨胀，自引力系统没有通常意义上的平衡态），热寂论只是一个外推。二是自然界中大量的有序现象似乎与"熵增加就是走向无序"矛盾：生物的进化从简单到复杂；生物膜、叶片与蝴蝶翅膀的花纹是规则的结构；化学中有组分浓度随时间周期变化的化学振荡（chemical oscillation）、在空间中周期分布的 Turing 结构（Turing，1952）、在不搅拌的薄层溶液中传播的化学波，以及同一组外界条件下出现几个稳态的多重定态现象。解决这两个困惑的关键是分清孤立系统与**开放系统**：熵增加原理只约束孤立系统；开放系统的熵可以减少，只要它向环境输出足够多的熵。

### 18.1.2. 熵流与熵产生

对任意系统，把熵的变化分成两部分。

**定义 18.1.1** 系统的熵变写成

$$
\mathrm{d}S = \mathrm{d}_{\mathrm{e}}S + \mathrm{d}_{\mathrm{i}}S,
\tag{18.1}
$$
其中 $\mathrm{d}_{\mathrm{e}}S$ 称为**熵流**，是系统与环境交换能量和物质引起的熵变；$\mathrm{d}_{\mathrm{i}}S$ 称为**熵产生**，是系统内部的不可逆过程（传热、扩散、黏性流动、化学反应、电流通过电阻等）引起的熵变。对封闭系统，$\mathrm{d}_{\mathrm{e}}S = \delta Q/T$，$T$ 是热量穿过边界处的温度；对开放系统还要加上物质带入的熵，$\mathrm{d}_{\mathrm{e}}S = \delta Q/T + \sum_{\mathrm{B}} S_{\mathrm{B}}\,\mathrm{d}_{\mathrm{e}}n_{\mathrm{B}}$（$S_{\mathrm{B}}$ 为偏摩尔熵，$\mathrm{d}_{\mathrm{e}}n_{\mathrm{B}}$ 为从环境流入的物质的量）。

熵流可正可负：系统放热或排出高熵的物质时 $\mathrm{d}_{\mathrm{e}}S < 0$。熵产生则受第二定律约束。

**定理 18.1.1** 对任意系统的任意过程，

$$
\mathrm{d}_{\mathrm{i}}S \ge 0,
\tag{18.2}
$$
等号只对可逆过程成立。

对封闭系统，式 (18.2) 就是 **Clausius 不等式** $\mathrm{d}S \ge \delta Q/T$；对孤立系统，$\mathrm{d}_{\mathrm{e}}S = 0$，它化为熵增加原理 $\mathrm{d}S \ge 0$。所以式 (18.2) 是第二定律不局限于孤立系统的一般表述：它对开放系统同样成立，因为把系统连同与之交换物质和能量的环境合起来是孤立的，而交换本身（在边界上温度、化学势连续时）不产生熵。由此有三条推论：

1. 局域性：把系统分成若干部分，每一部分的熵产生都不为负，不能用一处的负熵产生抵消另一处的正熵产生。这比"总熵产生不为负"强得多，是 18.1.4 节写出局域形式 $\sigma \ge 0$ 的依据。
2. 耦合：同一处同时进行几个不可逆过程时，其中某一个过程单独算出的熵产生可以为负，只要总和不为负。这就是一个过程"逆着自身的推动力"进行的热力学条件，18.2.5 节的主动运输即是例子；它与 [6.3.7](/6.3.7) 的**耦合反应**同理。
3. 开放系统的有序化：$\mathrm{d}_{\mathrm{i}}S \ge 0$ 时，只要 $\mathrm{d}_{\mathrm{e}}S < 0$ 且 $\lvert\mathrm{d}_{\mathrm{e}}S\rvert > \mathrm{d}_{\mathrm{i}}S$，就有 $\mathrm{d}S < 0$。在稳态，$\mathrm{d}S = 0$，$\mathrm{d}_{\mathrm{e}}S = -\mathrm{d}_{\mathrm{i}}S < 0$：维持一个非平衡稳态，就必须不断地向环境输出熵。

**例 18.1.1** 一根导热杆连接温度为 $T_1$、$T_2$（$T_1 > T_2$）的两个热库，达到稳态时单位时间内通过的热量为 $\Phi$。求杆的熵产生速率。

解：稳态时杆的状态不变，$\mathrm{d}S/\mathrm{d}t = 0$。杆在高温端得到熵 $\Phi/T_1$，在低温端失去熵 $\Phi/T_2$，熵流 $\mathrm{d}_{\mathrm{e}}S/\mathrm{d}t = \Phi/T_1 - \Phi/T_2 < 0$，所以

$$
\frac{\mathrm{d}_{\mathrm{i}}S}{\mathrm{d}t} = -\frac{\mathrm{d}_{\mathrm{e}}S}{\mathrm{d}t} = \Phi\left(\frac{1}{T_2} - \frac{1}{T_1}\right) > 0.
$$
杆本身的熵不变，它把从热库产生的熵全部"转运"到低温热库：这正是 [6.3.2](/6.3.2) 中不可逆传热使大孤立系统熵增加的那一部分，只是现在它被定位到发生不可逆过程的地方——杆的内部。

### 18.1.3. 化学反应的熵产生与亲和势

[6.3.4](/6.3.4) 的例 4.3.1 已经看到，绝热刚性容器中的反应没有热交换，熵却增加，增加的熵完全来自反应的不可逆性。一般地，设封闭系统中只进行一个反应，**反应进度**为 $\xi$，系统与环境只交换热和体积功。由组成可变系统的基本方程 $\mathrm{d}U = T\,\mathrm{d}S - p\,\mathrm{d}V + \sum_{\mathrm{B}}\mu_{\mathrm{B}}\,\mathrm{d}n_{\mathrm{B}}$ 与 $\mathrm{d}U = \delta Q - p\,\mathrm{d}V$（可逆的体积功），

$$
\mathrm{d}S = \frac{\delta Q}{T} - \frac{1}{T}\sum_{\mathrm{B}}\nu_{\mathrm{B}}\mu_{\mathrm{B}}\,\mathrm{d}\xi .
$$
第一项是熵流，第二项是熵产生。

**定义 18.1.2（亲和势）** 反应的**亲和势**定义为

$$
\mathcal{A} = -\sum_{\mathrm{B}}\nu_{\mathrm{B}}\mu_{\mathrm{B}} = -\Delta_{\mathrm{r}}G_{\mathrm{m}},
\tag{18.3}
$$
于是化学反应的熵产生为 $\mathrm{d}_{\mathrm{i}}S = \mathcal{A}\,\mathrm{d}\xi/T \ge 0$。

（亲和势的概念由 De Donder 于 1920 年代引入，IUPAC 符号为 $A$；本章写 $\mathcal{A}$，以免与 Helmholtz 自由能混淆。）式 (18.3) 说明 $\mathcal{A}$ 与反应速率 $\mathrm{d}\xi/\mathrm{d}t$ 必须同号：$\mathcal{A} > 0$ 时反应只能正向进行，平衡时 $\mathcal{A} = 0$。由**化学反应等温式**，$\mathcal{A} = RT\ln(K^\circ/Q)$，$Q$ 为反应商。$\mathcal{A}$ 与 $\Delta_{\mathrm{r}}G_{\mathrm{m}}$ 只差一个符号，但含义更一般：$\Delta_{\mathrm{r}}G_{\mathrm{m}}$ 作为判据要求等温等压，而 $\mathcal{A}\,\mathrm{d}\xi/T$ 是任何条件下的熵产生。在等温等压下，$T\,\mathrm{d}_{\mathrm{i}}S = \mathcal{A}\,\mathrm{d}\xi = -\mathrm{d}G$，**Gibbs 自由能**的减少就是 $T$ 乘以熵产生，[6.3.3](/6.3.3#sec-3.1.3) 的 Gibbs 自由能判据因此是定理 18.1.1 的特例。

几个反应同时进行时，$\mathrm{d}_{\mathrm{i}}S = \sum_r \mathcal{A}_r\,\mathrm{d}\xi_r/T \ge 0$；按推论 2，其中一个反应可以 $\mathcal{A}_r\,\mathrm{d}\xi_r < 0$，即逆着自己的亲和势进行，前提是它与另一个反应在机理上耦合（如 ATP 水解驱动的磷酸化）。

### 18.1.4. 局域平衡假设

热力学量（$T$、$p$、$\mu_{\mathrm{B}}$、$S$）是对平衡态定义的。非平衡系统中温度、浓度随位置和时间变化，要使用它们，需要一个假设。

**定义 18.1.3（局域平衡假设）** 把宏观系统划分为许多小体积元，每个体积元宏观上足够小，使其中的性质可以看作均匀；微观上足够大，包含大量分子，使涨落可以忽略（相对涨落 $\propto N^{-1/2}$）。若体积元内部的弛豫时间 $\tau_{\text{micro}}$、观测的时间尺度 $t$ 与整个系统趋于平衡的弛豫时间 $\tau_{\text{macro}}$ 满足

$$
\tau_{\text{micro}} \ll t \ll \tau_{\text{macro}},
$$
就假定每个体积元在任一时刻都处于平衡态，其状态由局域的 $T(\boldsymbol{r}, t)$、$p(\boldsymbol{r}, t)$、$c_{\mathrm{B}}(\boldsymbol{r}, t)$ 确定，局域的热力学函数之间满足平衡态的全部关系，特别是 Gibbs 关系

$$
T\,\mathrm{d}s = \mathrm{d}u - \sum_{\mathrm{B}}\mu_{\mathrm{B}}\,\mathrm{d}c_{\mathrm{B}},
\tag{18.4}
$$
其中 $s$、$u$ 是单位体积的熵和内能，$c_{\mathrm{B}}$ 是物质的量浓度（不可压缩的稀溶液或忽略体积变化时）。

局域平衡的条件是：在分子碰撞的尺度上（气体中是**平均自由程**，液体中是几个分子直径）宏观量的相对变化很小，例如 $\bar\lambda\,\lvert\nabla T\rvert/T \ll 1$；在分子的碰撞时间内宏观量几乎不变。对常见的输运过程这很容易满足：即使是 $10^3\,\mathrm{K\,cm^{-1}}$ 的温度梯度，常压气体中一个平均自由程（约 $0.1\,\mu\mathrm{m}$）上的温差也只有 $10^{-2}\,\mathrm{K}$。它失效的场合是激波、极稀薄气体、超快激光激发之类的过程。

对化学反应，局域平衡只要求反应比能量的交换慢得多，使反应中分子的速度分布与能级分布仍然是平衡分布（Boltzmann 分布），而并不要求反应接近化学平衡：一个亲和势很大、远离化学平衡的反应，只要不是极快，仍满足局域平衡。下一节的"线性"才要求接近化学平衡，两者不要混淆。

### 18.1.5. 熵平衡方程

在局域平衡下，可以写出熵的局域收支，并求出熵产生的具体形式。熵是广延量，它在每个体积元中的变化来自两部分：经过表面的熵流和内部的熵产生。

**定义 18.1.4** 局域的熵平衡方程写成

$$
\frac{\partial s}{\partial t} = -\nabla\cdot\boldsymbol{J}_S + \sigma,
\tag{18.5}
$$
$\boldsymbol{J}_S$ 称为熵流密度，$\sigma$ 称为（单位体积的）熵产生速率，第二定律要求 $\sigma \ge 0$。整个系统的熵产生速率为 $P = \mathrm{d}_{\mathrm{i}}S/\mathrm{d}t = \int_V \sigma\,\mathrm{d}V$。

以热传导、扩散与化学反应同时存在的静止流体为例（不考虑对流与黏性，力学平衡），推导 $\boldsymbol{J}_S$ 与 $\sigma$。能量与物质的局域守恒写成

$$
\frac{\partial u}{\partial t} = -\nabla\cdot\boldsymbol{J}_u, \qquad
\frac{\partial c_{\mathrm{B}}}{\partial t} = -\nabla\cdot\boldsymbol{J}_{\mathrm{B}} + \sum_r \nu_{\mathrm{B}r}v_r,
$$
其中 $\boldsymbol{J}_u$ 是能流密度，$\boldsymbol{J}_{\mathrm{B}}$ 是 B 的物质流密度（$\mathrm{mol\,m^{-2}\,s^{-1}}$），$v_r$ 是第 $r$ 个反应单位体积的**反应速率**。把它们代入式 (18.4) 对时间的导数：

$$
\frac{\partial s}{\partial t} = \frac{1}{T}\frac{\partial u}{\partial t} - \sum_{\mathrm{B}}\frac{\mu_{\mathrm{B}}}{T}\frac{\partial c_{\mathrm{B}}}{\partial t}
= -\frac{1}{T}\nabla\cdot\boldsymbol{J}_u + \sum_{\mathrm{B}}\frac{\mu_{\mathrm{B}}}{T}\nabla\cdot\boldsymbol{J}_{\mathrm{B}} - \sum_r\frac{v_r}{T}\sum_{\mathrm{B}}\nu_{\mathrm{B}r}\mu_{\mathrm{B}} .
$$
用 $f\,\nabla\cdot\boldsymbol{J} = \nabla\cdot(f\boldsymbol{J}) - \boldsymbol{J}\cdot\nabla f$ 把前两项中的散度移到外面，并用式 (18.3)：

$$
\frac{\partial s}{\partial t} = -\nabla\cdot\left(\frac{\boldsymbol{J}_u - \sum_{\mathrm{B}}\mu_{\mathrm{B}}\boldsymbol{J}_{\mathrm{B}}}{T}\right)
+ \boldsymbol{J}_u\cdot\nabla\frac{1}{T} + \sum_{\mathrm{B}}\boldsymbol{J}_{\mathrm{B}}\cdot\left(-\nabla\frac{\mu_{\mathrm{B}}}{T}\right) + \sum_r v_r\frac{\mathcal{A}_r}{T}.
$$
与式 (18.5) 比较，散度项是熵流，其余是熵产生：

$$
\boldsymbol{J}_S = \frac{1}{T}\Big(\boldsymbol{J}_u - \sum_{\mathrm{B}}\mu_{\mathrm{B}}\boldsymbol{J}_{\mathrm{B}}\Big), \qquad
\sigma = \boldsymbol{J}_u\cdot\nabla\frac{1}{T} + \sum_{\mathrm{B}}\boldsymbol{J}_{\mathrm{B}}\cdot\left(-\nabla\frac{\mu_{\mathrm{B}}}{T}\right) + \sum_r v_r\frac{\mathcal{A}_r}{T}.
\tag{18.6}
$$

熵流由能流和物质流携带；熵产生是若干乘积之和，每一项都是一种"流"乘以引起它的"梯度"。这种结构是普遍的。

**定义 18.1.5** 把熵产生速率写成双线性形式

$$
\sigma = \sum_k J_k X_k,
\tag{18.7}
$$
其中 $J_k$ 称为**热力学通量**，描述不可逆过程的快慢；与之相乘的 $X_k$ 称为与 $J_k$ 共轭的**热力学力**，描述引起这一过程的不均匀性或偏离平衡的程度。平衡时所有的力和通量同时为零。

| 不可逆过程 | 通量 $J_k$ | 共轭的力 $X_k$ | 张量阶数 |
|---|---|---|---|
| 热传导 | 能流（热流）密度 $\boldsymbol{J}_q$ | $\nabla(1/T) = -\nabla T/T^2$ | 矢量 |
| 扩散（等温） | 物质流密度 $\boldsymbol{J}_{\mathrm{B}}$ | $-\nabla\mu_{\mathrm{B}}/T$ | 矢量 |
| 离子迁移、导电（等温） | $\boldsymbol{J}_{\mathrm{B}}$ 或电流密度 $\boldsymbol{J}_{\mathrm{e}}$ | $-\nabla\tilde\mu_{\mathrm{B}}/T$ 或 $\boldsymbol{E}/T$ | 矢量 |
| 化学反应 | 反应速率 $v_r$ | $\mathcal{A}_r/T$ | 标量 |
| 黏性流动 | 黏性应力张量 | 速度梯度（对称部分）$/T$ | 二阶张量 |

对带电的组分，扩散的力中的化学势要换成**电化学势** $\tilde\mu_{\mathrm{B}} = \mu_{\mathrm{B}} + z_{\mathrm{B}}F\varphi$（[6.3.13](/6.3.13)）：等温时离子的熵产生为 $\sum_{\mathrm{B}}\boldsymbol{J}_{\mathrm{B}}\cdot(-\nabla\tilde\mu_{\mathrm{B}})/T$，其中电势梯度的部分合起来就是 $\boldsymbol{J}_{\mathrm{e}}\cdot\boldsymbol{E}/T$，即 Joule 热除以温度。通量与力的划分不是唯一的：例如可以用扣除了物质携带的焓之后的"热流" $\boldsymbol{J}_q' = \boldsymbol{J}_u - \sum_{\mathrm{B}}H_{\mathrm{B}}\boldsymbol{J}_{\mathrm{B}}$ 作通量，相应的扩散力变为 $-(\nabla\mu_{\mathrm{B}})_T/T$；只要 $\sigma$ 不变，不同的选法在物理上等价。

## 18.2. 线性非平衡热力学

### 18.2.1. 唯象关系

平衡时 $X_k = 0$、$J_k = 0$。偏离平衡不远时，把每个通量对所有的力作 Taylor 展开并只保留一次项：

**定义 18.2.1** 近平衡区的线性关系

$$
J_k = \sum_l L_{kl}X_l
\tag{18.8}
$$
称为线性唯象关系，系数 $L_{kl}$ 称为**唯象系数**：$L_{kk}$ 描述力 $X_k$ 引起其共轭通量的直接效应，$L_{kl}$（$k \ne l$）描述力 $X_l$ 引起另一种通量的交叉效应。唯象系数可以依赖于局域的状态（$T$、$p$、组成），但不依赖于力。

熟悉的输运定律都是只有直接效应时的特例：

- 热传导：$\boldsymbol{J}_q = L_{qq}\nabla(1/T) = -(L_{qq}/T^2)\nabla T$，即 **Fourier 定律**，导热系数 $\kappa = L_{qq}/T^2$（[5.2.2](/5.2.2#sec-2.4)）。
- 扩散：对等温的理想稀溶液，$\mu_{\mathrm{B}} = \mu^\circ_{\mathrm{B}} + RT\ln(c_{\mathrm{B}}/c^\circ)$，$\boldsymbol{J}_{\mathrm{B}} = -L_{\mathrm{BB}}\nabla\mu_{\mathrm{B}}/T = -(L_{\mathrm{BB}}R/c_{\mathrm{B}})\nabla c_{\mathrm{B}}$，即 **Fick 定律**，扩散系数 $D = L_{\mathrm{BB}}R/c_{\mathrm{B}}$。用化学势梯度而不是浓度梯度作推动力，非理想溶液的扩散、以及逆浓度梯度的"上坡扩散"（在相分离的混合物中出现）都有了统一的解释。
- 导电：$\boldsymbol{J}_{\mathrm{e}} = (L_{\mathrm{ee}}/T)\boldsymbol{E}$，即 **Ohm 定律**的微分形式。

第二定律对唯象系数加了限制：对任意的力，$\sigma = \sum_{k,l}L_{kl}X_kX_l \ge 0$。这是一个关于 $X$ 的**二次型**，所以 $L$ 的对称部分 $\frac12(L + L^{\mathsf T})$ 必须是**半正定矩阵**（[2.1.7](/2.1.7#sec-7.3)）。特别地，$L_{kk} \ge 0$（导热系数、扩散系数、电导都为正），且 $L_{kk}L_{ll} \ge \frac14(L_{kl} + L_{lk})^2$：交叉系数的大小受直接系数限制。

化学反应的线性区很窄。对一个基元反应 $\ce{A <=> B}$，正、逆反应速率之比由**细致平衡原理**确定：$v_+/v_- = \exp(\mathcal{A}/RT)$（平衡时 $\mathcal{A} = 0$、$v_+ = v_-$；对理想溶液，$v_+/v_- = (k_+/k_-)(c_{\mathrm{A}}/c_{\mathrm{B}}) = K^\circ/Q$）。因此净速率

$$
v = v_+ - v_- = v_+\left(1 - \mathrm{e}^{-\mathcal{A}/RT}\right) \approx \frac{v_{\mathrm{eq}}}{R}\,\frac{\mathcal{A}}{T}\qquad(\lvert\mathcal{A}\rvert \ll RT),
\tag{18.9}
$$
$v_{\mathrm{eq}}$ 是平衡时正（逆）反应的速率。只有 $\lvert\mathcal{A}\rvert$ 远小于 $RT$（$298\,\mathrm{K}$ 时 $2.5\,\mathrm{kJ\,mol^{-1}}$）时反应速率才与亲和势成正比，$L = v_{\mathrm{eq}}/R$。细胞中 ATP 水解的亲和势约 $50\,\mathrm{kJ\,mol^{-1}}$（[6.3.7](/6.3.7#sec-7.6.2)），是 $RT$ 的 20 倍，远在线性区之外。相比之下，热传导与扩散在宏观上很大的梯度下仍是线性的，因为在分子尺度上这些梯度极小（18.1.4 节）。线性非平衡热力学的结论对输运过程广泛适用，对化学反应则只适用于接近平衡的情形。

### 18.2.2. Onsager 倒易关系

交叉效应的系数之间存在普遍的对称性。

**定理 18.2.1（Onsager 倒易关系）** 若通量与力按式 (18.7) 选取（彼此独立，且 $\sigma = \sum J_kX_k$），则在没有磁场、系统不转动时，唯象系数矩阵是对称的：

$$
L_{kl} = L_{lk}.
\tag{18.10}
$$
存在磁场 $\boldsymbol{B}$（或以角速度 $\boldsymbol{\omega}$ 转动）时，$L_{kl}(\boldsymbol{B}) = L_{lk}(-\boldsymbol{B})$（Onsager–Casimir 关系；若某个变量在时间反演下变号，还要乘上相应的符号）。

Onsager 在 1931 年证明了这一结果，并因此获得 1968 年 Nobel 化学奖。它的意义在于：力 $X_l$ 引起通量 $J_k$ 的能力，等于力 $X_k$ 引起通量 $J_l$ 的能力。两个看起来毫不相干的交叉效应（如热电效应中的 Seebeck 效应与 Peltier 效应，18.2.3 节）由同一个系数描述，独立系数的个数从 $n^2$ 减为 $n(n+1)/2$。

倒易关系不能从宏观热力学推出，它的依据是微观力学的时间反演对称性与平衡涨落理论。推导的思路如下。

设 $\alpha_1, \dots, \alpha_n$ 是一组宏观变量偏离平衡值的偏差（如两部分之间的能量差、物质的量之差）。平衡附近系统的熵可展开为

$$
\Delta S = -\frac12\sum_{i,j}g_{ij}\alpha_i\alpha_j,
$$
$g = (g_{ij})$ 对称正定（平衡是熵的极大）。熵产生率 $\mathrm{d}\Delta S/\mathrm{d}t = \sum_i \dot\alpha_i X_i$，其中 $X_i = \partial\Delta S/\partial\alpha_i = -\sum_j g_{ij}\alpha_j$，所以 $J_i = \dot\alpha_i$ 与 $X_i$ 是一组共轭的通量与力。

1. 平衡涨落：由 **Boltzmann 熵公式** $S = k_{\mathrm{B}}\ln\Omega$（[5.2.4](/5.2.4#fml-4.8.1)），偏差为 $\boldsymbol{\alpha}$ 的宏观态的概率 $\propto \Omega \propto \exp(\Delta S/k_{\mathrm{B}})$（Einstein 涨落公式），这是一个多元正态分布。对它分部积分得 $\langle\alpha_iX_j\rangle = -k_{\mathrm{B}}\delta_{ij}$：

$$
\langle \alpha_i X_j\rangle = \int \alpha_i\,\frac{\partial \Delta S}{\partial\alpha_j}\,\frac{\mathrm{e}^{\Delta S/k_{\mathrm{B}}}}{Z}\,\mathrm{d}\boldsymbol{\alpha}
= k_{\mathrm{B}}\int \alpha_i\,\frac{\partial}{\partial\alpha_j}\frac{\mathrm{e}^{\Delta S/k_{\mathrm{B}}}}{Z}\,\mathrm{d}\boldsymbol{\alpha}
= -k_{\mathrm{B}}\delta_{ij}.
$$
2. 回归假设：自发涨落产生的偏差，平均而言按宏观的唯象规律衰减，即在给定初始偏差的条件下，$\langle\dot\alpha_i\rangle = \sum_k L_{ik}X_k$。
3. 微观可逆性：分子运动方程在时间反演下不变，平衡态中"先出现 $\alpha_i$、时间 $\tau$ 后出现 $\alpha_j$"与"先出现 $\alpha_j$、时间 $\tau$ 后出现 $\alpha_i$"的概率相同（对在时间反演下不变号的变量），所以 $\langle\alpha_i(0)\alpha_j(\tau)\rangle = \langle\alpha_j(0)\alpha_i(\tau)\rangle$。

对 $\tau$ 求导并令 $\tau \to 0^+$，得 $\langle\alpha_i\dot\alpha_j\rangle = \langle\alpha_j\dot\alpha_i\rangle$。代入第 2 条与第 1 条：

$$
\sum_k L_{jk}\langle\alpha_iX_k\rangle = \sum_k L_{ik}\langle\alpha_jX_k\rangle
\quad\Longrightarrow\quad -k_{\mathrm{B}}L_{ji} = -k_{\mathrm{B}}L_{ij}.
$$
这就是式 (18.10)。磁场中带电粒子的运动方程只在同时反转 $\boldsymbol{B}$ 时才是时间反演不变的，所以得到 Onsager–Casimir 形式。同一思路给出唯象系数与平衡涨落的直接联系（Green–Kubo 公式）：$L_{ij} = \frac{1}{k_{\mathrm{B}}}\int_0^\infty \langle J_i(0)J_j(t)\rangle\,\mathrm{d}t$，耗散的大小由平衡时自发涨落的时间关联决定。**Brown 运动**的扩散系数与摩擦系数之间的 Einstein 关系 $D = k_{\mathrm{B}}T/f$（$f$ 为摩擦系数）（[6.3.21](/6.3.21)）是它最早的例子，统称涨落–耗散定理。

**例 18.2.1** 三角反应 $\ce{A <=> B}$（1）、$\ce{B <=> C}$（2）、$\ce{C <=> A}$（3）在封闭的理想溶液中进行，接近平衡。验证倒易关系。

解：三个亲和势满足 $\mathcal{A}_1 + \mathcal{A}_2 + \mathcal{A}_3 = 0$（绕一圈回到 A），只有两个是独立的。由式 (18.9)，每个反应的净速率 $v_r = \ell_r\mathcal{A}_r/T$，$\ell_r = v_{r,\mathrm{eq}}/R > 0$；这里用到了细致平衡：平衡时每一个反应各自正逆速率相等，因此每个 $v_r$ 只依赖自己的 $\mathcal{A}_r$。熵产生

$$
T\sigma = v_1\mathcal{A}_1 + v_2\mathcal{A}_2 + v_3\mathcal{A}_3 = (v_1 - v_3)\mathcal{A}_1 + (v_2 - v_3)\mathcal{A}_2 ,
$$
所以独立的通量是 $J_1 = v_1 - v_3$、$J_2 = v_2 - v_3$，共轭的力是 $X_1 = \mathcal{A}_1/T$、$X_2 = \mathcal{A}_2/T$。代入 $\mathcal{A}_3 = -\mathcal{A}_1 - \mathcal{A}_2$：

$$
J_1 = (\ell_1 + \ell_3)X_1 + \ell_3X_2, \qquad J_2 = \ell_3X_1 + (\ell_2 + \ell_3)X_2 ,
$$
交叉系数 $L_{12} = L_{21} = \ell_3$。若平衡时允许存在 $\ce{A -> B -> C -> A}$ 的净循环流（违反细致平衡），这一对称性就不成立。Onsager 正是用这个例子说明倒易关系与细致平衡（**微观可逆性原理**，[6.3.15](/6.3.15)）的联系。

最后一个普遍限制来自对称性。

**定理 18.2.2（Curie 原理）** 在各向同性的介质中，张量阶数不同的通量与力之间不发生线性耦合。

（陈述。）理由是：各向同性介质中唯象系数在任意转动下不变，一个标量力（如亲和势）乘以一个不变的系数，不可能得到一个有方向的矢量通量。因此在各向同性的溶液中，化学反应不能直接驱动扩散，热传导与扩散（同为矢量）之间则可以耦合。这对生物学有重要的推论：细胞要用化学反应（标量）驱动定向的跨膜输运（矢量），就必须有各向异性的结构——镶嵌在膜中、有确定取向的蛋白质。18.2.5 节的离子泵正是这样的结构。

### 18.2.3. 交叉效应：热电效应与热扩散

先看热电效应。在导体中同时存在温度梯度与电流时（一维，略去矢量记号），取热流 $J_q$ 与电流密度 $J_{\mathrm{e}}$ 为通量，共轭的力为 $\partial_x(1/T)$ 与 $-\partial_x\varphi/T$（这里 $\varphi$ 理解为电子的电化学势除以电荷，电压表测量的正是它的差）：

$$
J_q = L_{qq}\,\partial_x\frac1T + L_{q\mathrm{e}}\left(-\frac{\partial_x\varphi}{T}\right), \qquad
J_{\mathrm{e}} = L_{\mathrm{e}q}\,\partial_x\frac1T + L_{\mathrm{ee}}\left(-\frac{\partial_x\varphi}{T}\right).
$$

- Peltier 效应（Peltier effect）：温度均匀（$\partial_xT = 0$）时，电流携带热流 $J_q = (L_{q\mathrm{e}}/L_{\mathrm{ee}})J_{\mathrm{e}}$，比例系数 $\Pi = L_{q\mathrm{e}}/L_{\mathrm{ee}}$ 称为 Peltier 系数；两种导体的接头处 $\Pi$ 不连续，于是吸热或放热，这就是半导体制冷片的原理。
- **Seebeck 效应**（[5.3.5](/5.3.5#sec-5.4.3)）：开路（$J_{\mathrm{e}} = 0$）时温度梯度产生电势梯度。由第二式，$L_{\mathrm{ee}}\partial_x\varphi/T = L_{\mathrm{e}q}\partial_x(1/T) = -L_{\mathrm{e}q}\partial_xT/T^2$，即 $\partial_x\varphi = -\alpha_{\mathrm{S}}\,\partial_xT$，Seebeck 系数 $\alpha_{\mathrm{S}} = L_{\mathrm{e}q}/(TL_{\mathrm{ee}})$。

由 Onsager 关系 $L_{q\mathrm{e}} = L_{\mathrm{e}q}$，

$$
\Pi = T\alpha_{\mathrm{S}} .
\tag{18.11}
$$
这是 W. Thomson（Kelvin）在 1854 年用一个把可逆与不可逆部分强行分开的论证得到的第二 Thomson 关系，Onsager 理论给了它严格的基础；它已被大量金属与半导体的测量证实。式 (18.11) 把一个电学测量（开路电压）与一个热学测量（接头吸放热）联系起来，是倒易关系最经典的验证。

热扩散与 Dufour 效应是另一对交叉效应。在二组分混合物中加温度梯度，即使开始时组成均匀，也会出现浓度梯度，一种组分在冷端富集，这称为热扩散（thermal diffusion），又称 Soret 效应；它的倒易效应是浓度梯度引起热流（Dufour 效应）。达到 $J_{\mathrm{B}} = 0$ 的稳态时，热扩散造成的组成差与温差成正比，比例系数（Soret 系数）通常只有 $10^{-3}$–$10^{-2}\,\mathrm{K^{-1}}$ 量级，但可以在热扩散柱中累积放大，曾用于同位素分离。在溶液中，带电的胶粒与生物大分子沿温度梯度的定向运动称为热泳，生物化学中用它测定分子间的结合常数（微量热泳动）。

类似的交叉效应还有电动现象：电场驱动液体流过毛细管或多孔塞（**电渗**），压力驱动液体流动产生电势差（流动电势），两者的系数也满足倒易关系（Saxén 关系，[6.3.21](/6.3.21)）。

### 18.2.4. 膜输运：Kedem–Katchalsky 方程

生物膜和人工膜既让水通过、也让溶质以不同程度通过，**半透膜**只是理想的极限。考虑一张膜隔开同一种溶质 s 的两份稀水溶液，温度相同，两侧的压力差为 $\Delta p$，**渗透压**之差为 $\Delta\varPi = RT\Delta c_{\mathrm{s}}$（[6.3.5](/6.3.5#sec-5.3.4)）。单位膜面积的耗散函数 $\Phi = T\sigma$（对膜的厚度积分）为

$$
\Phi = J_{\mathrm{w}}\Delta\mu_{\mathrm{w}} + J_{\mathrm{s}}\Delta\mu_{\mathrm{s}},
$$
$J_{\mathrm{w}}$、$J_{\mathrm{s}}$ 是水和溶质的物质流密度，$\Delta\mu$ 为膜两侧化学势之差（高的一侧减低的一侧，与流的正向一致）。稀溶液中 $\Delta\mu_{\mathrm{w}} = V_{\mathrm{w}}(\Delta p - \Delta\varPi)$，$\Delta\mu_{\mathrm{s}} = V_{\mathrm{s}}\Delta p + \Delta\varPi/\bar c_{\mathrm{s}}$（$V$ 为偏摩尔体积，$\bar c_{\mathrm{s}}$ 为两侧浓度的对数平均，近似为算术平均）。代入并重新组合：

$$
\Phi = \underbrace{(J_{\mathrm{w}}V_{\mathrm{w}} + J_{\mathrm{s}}V_{\mathrm{s}})}_{J_V}\Delta p + \underbrace{\left(\frac{J_{\mathrm{s}}}{\bar c_{\mathrm{s}}} - J_{\mathrm{w}}V_{\mathrm{w}}\right)}_{J_{\mathrm{D}}}\Delta\varPi .
$$
$J_V$ 是体积流（单位面积的体积流量），$J_{\mathrm{D}}$ 是溶质相对于水的"交换流"。在这一组通量与力下写出唯象关系并用 Onsager 关系 $L_{p\mathrm{D}} = L_{\mathrm{D}p}$：

$$
J_V = L_p\Delta p + L_{p\mathrm{D}}\Delta\varPi, \qquad J_{\mathrm{D}} = L_{p\mathrm{D}}\Delta p + L_{\mathrm{D}}\Delta\varPi .
$$
定义反射系数（reflection coefficient）$\sigma_{\mathrm{r}} = -L_{p\mathrm{D}}/L_p$（Staverman，1951；通常记作 $\sigma$，这里加下标以免与熵产生混淆），第一式成为

$$
J_V = L_p(\Delta p - \sigma_{\mathrm{r}}\Delta\varPi).
\tag{18.12}
$$
由 $\Delta p = J_V/L_p + \sigma_{\mathrm{r}}\Delta\varPi$ 消去第二式中的 $\Delta p$，得 $J_{\mathrm{D}} = -\sigma_{\mathrm{r}}J_V + (L_{\mathrm{D}} - \sigma_{\mathrm{r}}^2L_p)\Delta\varPi$；再用 $J_{\mathrm{s}} \approx \bar c_{\mathrm{s}}(J_V + J_{\mathrm{D}})$（稀溶液中 $J_V \approx J_{\mathrm{w}}V_{\mathrm{w}}$），

$$
J_{\mathrm{s}} = \omega\,\Delta\varPi + (1 - \sigma_{\mathrm{r}})\bar c_{\mathrm{s}}J_V, \qquad \omega = \bar c_{\mathrm{s}}(L_{\mathrm{D}} - \sigma_{\mathrm{r}}^2L_p).
\tag{18.13}
$$
式 (18.12)、(18.13) 是 Kedem 与 Katchalsky 在 1958 年得到的，称为 Kedem–Katchalsky 方程（Kedem–Katchalsky equations）。膜的输运性质由三个可测的系数描述：水力渗透系数 $L_p$、反射系数 $\sigma_{\mathrm{r}}$、溶质渗透系数 $\omega$；没有倒易关系则需要四个。第二定律（$L_pL_{\mathrm{D}} \ge L_{p\mathrm{D}}^2$）保证 $\omega \ge 0$。

- $\sigma_{\mathrm{r}} = 1$：膜完全不让溶质通过（$\omega = 0$），体积流在 $\Delta p = \Delta\varPi$ 时停止，即 van 't Hoff 的渗透平衡；这是**反渗透**的理想极限。
- $\sigma_{\mathrm{r}} = 0$：膜对溶质没有选择性，溶质随水流一起通过，不产生有效的渗透压。
- $0 < \sigma_{\mathrm{r}} < 1$：有效渗透压只有 $\sigma_{\mathrm{r}}\Delta\varPi$。毛细血管壁对小分子溶质的 $\sigma_{\mathrm{r}}$ 接近 0，对血浆白蛋白接近 1，所以决定血浆与组织液之间水分交换的是蛋白质的渗透压（胶体渗透压）；生理学中的 Starling 方程 $J_V = L_p[(p_{\mathrm{c}} - p_{\mathrm{i}}) - \sigma_{\mathrm{r}}(\varPi_{\mathrm{c}} - \varPi_{\mathrm{i}})]$ 正是式 (18.12)。

### 18.2.5. 能量耦合与主动运输

推论 2 说，一个过程可以逆着自己的推动力进行，只要它与另一个过程耦合。线性理论把这一点定量化。考虑两个耦合的过程：

$$
J_1 = L_{11}X_1 + L_{12}X_2, \qquad J_2 = L_{12}X_1 + L_{22}X_2 ,
$$
过程 1 "下坡"（$J_1X_1 > 0$），过程 2 被驱动"上坡"（$J_2X_2 < 0$）。总熵产生 $\sigma = J_1X_1 + J_2X_2 \ge 0$，所以上坡过程的输出不能超过下坡过程的输入。

**定义 18.2.2** 称

$$
q = \frac{L_{12}}{\sqrt{L_{11}L_{22}}}, \qquad \lvert q\rvert \le 1
$$
为两个过程的**耦合度**；能量转换的效率为 $\eta = -J_2X_2/(J_1X_1)$。

（$\lvert q\rvert \le 1$ 来自 $L$ 半正定。）引入约化的力之比 $x = \sqrt{L_{22}/L_{11}}\,X_2/X_1$，直接代入得

$$
\eta = -\frac{x(x + q)}{1 + qx}.
$$
对 $q > 0$，只有 $-q < x < 0$ 时才有输出：$x = 0$ 时没有阻力，不做功；$x = -q$ 时上坡通量停止（"静态头"，如离子泵在梯度最大时不再净转运）。对 $x$ 求极值，最大效率为

$$
\eta_{\max} = \frac{q^2}{\left(1 + \sqrt{1 - q^2}\right)^2},
$$
在 $x = (\sqrt{1 - q^2} - 1)/q$ 处取得（Kedem 与 Caplan，1965）。只有完全耦合（$q = 1$）才能达到 $\eta \to 1$，但这时通量趋于零：高效率与高功率不可兼得，这与 Carnot 热机效率只在无限缓慢时达到上限是同一个道理。

![线性两通量能量转换器的效率：左为不同耦合度下效率随约化力之比的变化，右为最大效率随耦合度的变化](./plots/coupling-efficiency.py)

物质顺着自身电化学势梯度的跨膜运动是被动运输，自发进行；逆着电化学势梯度的运动称为主动运输（active transport），必须与一个熵产生为正的过程耦合。按 Curie 原理，这种耦合只能发生在有取向的膜蛋白中。最重要的例子是 $\ce{Na+}$/$\ce{K+}$-ATP 酶（钠钾泵，Skou 发现，1997 年 Nobel 化学奖）：每水解 1 个 ATP，把 3 个 $\ce{Na+}$ 泵出细胞、2 个 $\ce{K+}$ 泵入细胞，两种离子都是逆着电化学势梯度运动。

**例 18.2.2** 哺乳动物细胞内外的典型浓度为：$[\ce{Na+}]_{\text{内}} = 12\,\mathrm{mmol\,L^{-1}}$，$[\ce{Na+}]_{\text{外}} = 145\,\mathrm{mmol\,L^{-1}}$，$[\ce{K+}]_{\text{内}} = 140\,\mathrm{mmol\,L^{-1}}$，$[\ce{K+}]_{\text{外}} = 4\,\mathrm{mmol\,L^{-1}}$，**膜电势** $\varphi_{\text{内}} - \varphi_{\text{外}} = -70\,\mathrm{mV}$，$T = 310\,\mathrm{K}$。估计钠钾泵每个循环所需的最小 Gibbs 自由能，并与 ATP 水解提供的自由能比较（以浓度代替活度）。

解：$RT = 2.58\,\mathrm{kJ\,mol^{-1}}$，$F\times 0.070\,\mathrm{V} = 6.75\,\mathrm{kJ\,mol^{-1}}$。把 1 mol $\ce{Na+}$ 从胞内移到胞外，电化学势的增加为

$$
\Delta\tilde\mu_{\ce{Na+}} = RT\ln\frac{145}{12} + F(\varphi_{\text{外}} - \varphi_{\text{内}}) = 6.42 + 6.75 = 13.2\,\mathrm{kJ\,mol^{-1}};
$$
把 1 mol $\ce{K+}$ 从胞外移到胞内，

$$
\Delta\tilde\mu_{\ce{K+}} = RT\ln\frac{140}{4} + F(\varphi_{\text{内}} - \varphi_{\text{外}}) = 9.16 - 6.75 = 2.4\,\mathrm{kJ\,mol^{-1}}.
$$
每个循环需要 $3 \times 13.2 + 2 \times 2.4 = 44.4\,\mathrm{kJ\,mol^{-1}}$。由 [6.3.7](/6.3.7#sec-7.6.2)，细胞中 ATP 水解的 $\Delta_{\mathrm{r}}G_{\mathrm{m}} \approx -52.7\,\mathrm{kJ\,mol^{-1}}$（红细胞，$37\,^\circ\mathrm{C}$），足以驱动一个循环，热力学效率约 $44.4/52.7 \approx 84\%$，接近但不超过 1，第二定律得到满足。$\ce{K+}$ 的浓度梯度虽大，却几乎被膜电势抵消，泵的大部分自由能花在 $\ce{Na+}$ 上；每个循环净移出一个正电荷，泵本身也对膜电势有贡献（生电泵）。

钠钾泵建立的 $\ce{Na+}$ 电化学势梯度又被用来驱动别的输运，称为继发性主动运输（secondary active transport）。小肠上皮的 $\ce{Na+}$–葡萄糖同向转运体每转运 1 个葡萄糖分子伴随 2 个 $\ce{Na+}$ 进入细胞，按例 18.2.2 的数据，$\ce{Na+}$ 进入时电化学势降低 $13.2\,\mathrm{kJ\,mol^{-1}}$，两个共 $26.4\,\mathrm{kJ\,mol^{-1}}$，葡萄糖在胞内外的浓度比最高可达 $\exp(26.4/2.58) \approx 3\times10^4$。线粒体与叶绿体中则是电子传递链把 $\ce{H+}$ 泵过内膜，跨膜的 $\ce{H+}$ 电化学势差（质子动力势）再驱动 ATP 合酶合成 ATP（Mitchell 的化学渗透学说，1978 年 Nobel 化学奖）：一个反应驱动一个流，这个流再驱动另一个反应，生物能量学就是这样一串耦合。

在生物物理中，常用式 (18.8) 形式的线性方程（以电化学势差和亲和势为力）描述离子泵与转运体，称为线性能量转换器。需要注意的是，ATP 水解的亲和势约为 $20RT$，严格说来远离线性区（18.2.1 节），线性方程只能在实际工作点附近作为经验的线性化使用；分子水平的描述要用循环的动力学模型（每一步满足细致平衡，整个循环在 ATP 的驱动下有净流）。

### 18.2.6. 最小熵产生原理

在线性区，非平衡稳态有一个变分性质。设系统有 $n$ 个力，其中 $X_1, \dots, X_m$ 由边界条件固定（例如两端热库的温度、膜两侧的浓度），其余 $X_{m+1}, \dots, X_n$ 可以自由调整。

**定理 18.2.3（最小熵产生原理）** 若唯象系数是常数且满足 Onsager 倒易关系，则在 $X_1, \dots, X_m$ 固定的条件下，自由通量为零（$J_k = 0$，$k > m$）的稳态，恰好是熵产生速率 $P = \sum_{k,l}L_{kl}X_kX_l$ 对自由的力取极小的状态。

**证明** 对自由的力 $X_k$（$k > m$）求偏导：

$$
\frac{\partial P}{\partial X_k} = \sum_l (L_{kl} + L_{lk})X_l = 2\sum_l L_{kl}X_l = 2J_k ,
$$
第二个等号用了 $L_{kl} = L_{lk}$。所以 $P$ 的驻点就是 $J_k = 0$（$k > m$）的状态；$P$ 是半正定二次型（在自由的力上正定时），驻点是极小。$\square$

例如两个耦合过程中 $X_1$ 固定、$X_2$ 自由，稳态 $J_2 = 0$ 给出 $X_2 = -(L_{12}/L_{22})X_1$，此时 $P = (L_{11} - L_{12}^2/L_{22})X_1^2$ 最小。热扩散的稳态（温度梯度固定，物质流为零，浓度梯度自行调整）就是这样的状态。Prigogine 在 1945 年提出这一原理，并进一步证明在同样条件下 $\mathrm{d}P/\mathrm{d}t \le 0$：$P$ 是稳态的 **Lyapunov 函数**（[2.4.11](/2.4.11#sec-11.4)），所以线性区的非平衡稳态是稳定的，偏离之后会回到稳态。

这一原理的适用条件必须记清：

1. 系统处于线性区，并且唯象系数在所考虑的范围内可以视为常数。例如导热杆的稳态温度分布：若 $L_{qq} = \kappa T^2$ 为常数，最小熵产生给出的分布与热方程的稳态解一致；若实际上是 $\kappa$ 为常数（温差较大时更接近实际），稳态的温度线性分布并不严格使 $P$ 极小，两者相差温差的高阶小量。
2. 倒易关系成立（证明中关键的一步）。
3. 边界条件不随时间变化。

远离平衡时，没有普遍适用的、类似的极值原理：稳态不一定使熵产生极小，也可以不稳定。常见的"最大熵产生原理"之类的说法只是对某些系统的经验假说，没有普遍的证明。线性区的另一个推论更为重要：既然稳态总是稳定的，线性区内就不会自发地出现新的有序结构，由平衡态连续延伸出来的均匀稳态，即热力学分支（thermodynamic branch），不会失稳。要得到有序结构，必须远离平衡。

## 18.3. 远离平衡：耗散结构

### 18.3.1. 稳定性与耗散结构

在近平衡区，稳态的稳定性由熵的二阶变分保证。Glansdorff 与 Prigogine（1971）把它推广到远离平衡的稳态：在局域平衡下，熵对稳态的二阶偏差 $\delta^2 s$ 总是负定的，$-\delta^2 s$ 可以作为 Lyapunov 函数，而

$$
\frac12\frac{\partial}{\partial t}\delta^2 s = \sum_k \delta J_k\,\delta X_k
$$
（陈述），右边称为超熵产生（excess entropy production）。若对一切小扰动 $\sum\delta J_k\delta X_k > 0$，稳态稳定；它可以变负时稳态可能失稳。在线性区 $\sum\delta J\delta X = \sum L_{kl}\delta X_k\delta X_l \ge 0$，总是稳定的。远离平衡时，若反应网络中有正反馈——最典型的是自催化（autocatalysis），即产物加速自身的生成，如 $\ce{A + X -> 2X}$；或两种物质互相催化——超熵产生可以为负。这时随着离平衡的距离（由外界供给的物质浓度、能流等控制参数度量）增大，原来的均匀稳态在某个临界值处失稳，系统分岔到新的状态：浓度随时间振荡、在空间中形成斑图，或在几个稳态之间切换。

**定义 18.3.1（耗散结构）** 开放系统在远离平衡的条件下，通过与外界持续交换能量和物质、由内部的非线性过程形成并维持的时间或空间上的有序状态，称为**耗散结构**。

耗散结构的概念由 Prigogine 提出（1977 年 Nobel 化学奖），它有四个要素：开放系统；远离平衡（控制参数越过临界值）；非线性的相互作用（自催化、反馈）；涨落（失稳时由微小的**涨落**选出新状态的具体形式，例如斑图的位置、振荡的相位）。耗散结构与晶体这类平衡结构根本不同：晶体是 Gibbs 自由能的极小，切断与外界的联系后依然存在；耗散结构要靠持续的熵产生维持，切断物质与能量的供给，它就衰减回均匀的平衡态。"非平衡是有序之源"（Prigogine）指的就是这一点：在一定条件下，封闭系统自发地从有序趋向无序，开放的远离平衡系统却可以自发地从无序趋向有序。物理中的例子是 Rayleigh–Bénard 对流：从下方加热的液层在温差超过临界值时形成规则的六角形对流元胞；化学与生物中的例子是下面的化学振荡、化学波与 Turing 斑图。

一个容易误解的地方：在封闭系统中，化学反应可以表现出暂时的振荡（如在烧杯中进行的 BZ 反应），但这不违反第二定律。封闭系统等温等压下 $G$ 单调减小，振荡的只是中间物的浓度，而不是 $G$；当反应物耗尽、系统接近平衡时，振荡必然停止。更严格地说，在平衡附近，由式 (18.8) 与倒易关系得到的弛豫方程 $\dot{\boldsymbol{\alpha}} = -Lg\boldsymbol{\alpha}$ 中，$L$ 对称半正定、$g$ 对称正定，$Lg$ 与对称矩阵 $g^{1/2}Lg^{1/2}$ 相似，所有**特征值**都是非负实数：平衡附近只有单调的弛豫，连衰减振荡都不会出现。持续的化学振荡只能出现在远离平衡、并且不断有物质供给的开放系统中。

### 18.3.2. 化学振荡：Brusselator

*Brusselator* 是 Prigogine 与 Lefever（1968）在布鲁塞尔提出的模型，用最简单的机理说明化学振荡的条件：

$$
\begin{aligned}
&\ce{A -> X}, && k_1, \\
&\ce{2X + Y -> 3X}, && k_2, \\
&\ce{B + X -> Y + D}, && k_3, \\
&\ce{X -> E}, && k_4 .
\end{aligned}
$$
总反应是 $\ce{A + B -> D + E}$；$\ce{A}$、$\ce{B}$ 由外界不断补充、浓度保持不变，产物 $\ce{D}$、$\ce{E}$ 不断移走，系统是开放的。第二步是三分子的自催化步骤（真实的振荡反应中，自催化是由几个基元步骤组合出来的）。所有步骤都按不可逆处理，这相当于系统处于无限远离平衡的状态。把每一步当作**基元反应**，由**质量作用定律**写出 X、Y 的**速率方程**：

$$
\frac{\mathrm{d}[\ce{X}]}{\mathrm{d}t} = k_1[\ce{A}] - k_3[\ce{B}][\ce{X}] + k_2[\ce{X}]^2[\ce{Y}] - k_4[\ce{X}], \qquad
\frac{\mathrm{d}[\ce{Y}]}{\mathrm{d}t} = k_3[\ce{B}][\ce{X}] - k_2[\ce{X}]^2[\ce{Y}].
$$
令 $\tau = k_4t$，$[\ce{X}] = \sqrt{k_4/k_2}\,x$，$[\ce{Y}] = \sqrt{k_4/k_2}\,y$，方程化为只含两个参数的无量纲形式

$$
\dot x = a - (b + 1)x + x^2y, \qquad \dot y = bx - x^2y,
\tag{18.14}
$$
其中 $a = (k_1[\ce{A}]/k_4)\sqrt{k_2/k_4}$，$b = k_3[\ce{B}]/k_4$，点表示对 $\tau$ 求导。

**例 18.3.1** 求式 (18.14) 的稳态并分析其稳定性。

解：令右边为零，第二式给出 $x^2y = bx$，代入第一式得 $a - x = 0$，唯一的稳态（**平衡点**）为 $(x^*, y^*) = (a, b/a)$。在该点的 **Jacobi 矩阵**为

$$
J = \begin{bmatrix} b - 1 & a^2 \\ -b & -a^2 \end{bmatrix}, \qquad
\operatorname{tr}J = b - 1 - a^2, \qquad \det J = a^2 > 0 .
$$
由线性化判据（[2.4.11](/2.4.11#sec-11.3) 的 Lyapunov 第一方法），$\det J > 0$ 时，$\operatorname{tr}J < 0$ 则稳态渐近稳定，$\operatorname{tr}J > 0$ 则不稳定。所以稳态在

$$
b < b_{\mathrm{c}} = 1 + a^2
$$
时稳定，$b > b_{\mathrm{c}}$ 时失稳。在 $b = b_{\mathrm{c}}$ 处，$J$ 的一对共轭复特征值 $\lambda = \frac12\operatorname{tr}J \pm \mathrm{i}\sqrt{\det J - (\operatorname{tr}J)^2/4}$ 以 $\mathrm{d}(\operatorname{Re}\lambda)/\mathrm{d}b = \frac12 \ne 0$ 的速度穿过虚轴，这正是 Hopf 分岔的条件（[2.4.11](/2.4.11#sec-11.6.4)）。分岔点处特征值为 $\pm\mathrm{i}a$，产生的小振幅振荡周期约为 $2\pi/a$。

$b > b_{\mathrm{c}}$ 时稳态不稳定，但轨线并不跑向无穷：可以构造相平面中一个包含稳态的有界区域，轨线进入后不再离开；区域中唯一的平衡点是不稳定的，由 [2.4.11 的 Poincaré–Bendixson 定理](/2.4.11#thm-11.6.1)，区域内存在一条闭轨线，即稳定的**极限环**。数值计算表明它是唯一的、吸引附近所有轨线的极限环：无论初始浓度如何，最终都进入同一个振幅与周期的振荡。这是化学振荡与无阻尼谐振子（或 Lotka–Volterra 模型）的本质区别：后者的振幅由初始条件决定，受扰动后不能恢复；极限环的振幅与周期由系统本身决定，是稳健的"化学钟"。

![Brusselator（a = 1）在 Hopf 点两侧的行为：上为浓度随时间的变化，下为相平面中的轨线、零斜率线与极限环](./plots/brusselator-oscillation.py)

从图中还可以看出 $b$ 较大时振荡的形状：$y$ 缓慢积累，$x$ 在自催化作用下突然爆发、又迅速回落，这种"慢积累、快释放"的弛豫振荡是许多化学与生物振荡器的共同特征。分岔图给出振幅随控制参数的变化：$b$ 刚越过 $b_{\mathrm{c}}$ 时振幅从零开始连续增大（大致 $\propto\sqrt{b - b_{\mathrm{c}}}$，超临界 Hopf 分岔），周期从线性理论的 $2\pi/a$ 开始增长。

![Brusselator 的 Hopf 分岔（a = 1）：左为吸引子上 x 的极大值与极小值随 b 的变化，右为极限环周期随 b 的变化](./plots/brusselator-bifurcation.py)

从热力学的角度看，控制参数 $b \propto [\ce{B}]$ 度量系统离平衡有多远：$b < b_{\mathrm{c}}$ 时系统停留在热力学分支上，熵产生虽然很大，宏观上却是均匀、静止的；$b > b_{\mathrm{c}}$ 时热力学分支失稳，振荡出现。若把四步都写成可逆的并让 $\ce{A}$、$\ce{B}$、$\ce{D}$、$\ce{E}$ 接近平衡比例，按 18.3.1 节末的论证，振荡就会消失。

### 18.3.3. BZ 反应与生物振荡

1951 年 Belousov 发现，柠檬酸被溴酸钾在硫酸中氧化、以铈离子为催化剂时，溶液的颜色在无色（$\ce{Ce^3+}$）与黄色（$\ce{Ce^4+}$）之间周期变化。当时人们普遍认为这违反第二定律，他的论文被拒稿，直到 1959 年才以摘要的形式发表。1960 年代 Zhabotinsky 改用丙二酸，后来又以邻二氮菲亚铁（试亚铁灵，红色/蓝色）作催化剂与指示剂，使现象清晰可见，这类反应统称 Belousov–Zhabotinsky 反应（Belousov–Zhabotinsky reaction），简称 BZ 反应。Field、Kőrös 与 Noyes（1972）给出了它的机理（FKN 机理），可概括为三个过程：

1. 过程 A：$\ce{Br-}$ 浓度高时，溴酸根被 $\ce{Br-}$ 还原，$\ce{BrO3- + 2Br- + 3H+ -> 3HOBr}$（经由 $\ce{HBrO2}$ 等中间物），消耗 $\ce{Br-}$；
2. 过程 B：$\ce{Br-}$ 降到临界浓度以下时，亚溴酸 $\ce{HBrO2}$ 的自催化生成接管，净反应为 $\ce{BrO3- + HBrO2 + 3H+ + 2Ce^3+ -> 2HBrO2 + 2Ce^4+ + H2O}$，$\ce{HBrO2}$ 指数增长，催化剂被迅速氧化（颜色突变）；
3. 过程 C：$\ce{Ce^4+}$ 氧化丙二酸及其溴代物，被还原为 $\ce{Ce^3+}$，同时释放 $\ce{Br-}$；$\ce{Br-}$ 积累后过程 A 重新占优，抑制自催化。

$\ce{Br-}$ 起延迟的负反馈作用，$\ce{HBrO2}$ 提供自催化的正反馈，两者结合给出振荡；把 FKN 机理简化为五步得到的 Oregonator 模型，在数学上与 Brusselator 同类。在不搅拌的薄层溶液中，局部的自催化爆发通过扩散传给邻近区域，形成向外传播的同心圆波（靶形波）与螺旋波，即"Zhabotinsky 花纹"。这类可激发介质中的波在生物中普遍存在：心肌中的螺旋波与心律失常有关，盘基网柄菌（*Dictyostelium discoideum*）聚集时 cAMP 信号形成螺旋波。

生物体内的振荡同样普遍。酵母细胞及其提取液中，糖酵解中间物（如 NADH）的浓度以几十秒到几分钟的周期振荡，这称为糖酵解振荡（glycolytic oscillation）。关键在于磷酸果糖激酶（PFK）：它的产物 ADP（及由其产生的 AMP）是它的别构激活剂，构成自催化式的正反馈。其他例子有细胞内 $\ce{Ca^2+}$ 浓度的振荡、细胞周期，以及由基因转录–翻译的延迟负反馈构成的昼夜节律钟。它们的数学结构与 Brusselator 相同：开放系统（持续供给葡萄糖、ATP）、远离平衡、非线性反馈，振荡在控制参数越过 Hopf 分岔时出现；能量的持续耗散是生物钟走动的代价。数学上的系统讨论见 [7.4.4](/7.4.4)。

### 18.3.4. Turing 斑图

Turing 在 1952 年的论文《形态发生的化学基础》中提出：两种相互反应的物质若扩散速度相差足够大，原本稳定的均匀状态可以因扩散而失稳，自发形成静止的空间周期斑图。这与直觉相反——扩散本来使一切均匀化。把 Brusselator 放在空间中，X、Y 同时扩散，就得到**反应扩散方程**

$$
\frac{\partial x}{\partial t} = a - (b + 1)x + x^2y + D_x\Delta x, \qquad
\frac{\partial y}{\partial t} = bx - x^2y + D_y\Delta y .
\tag{18.15}
$$
对均匀稳态 $(a, b/a)$ 加正比于 $\mathrm{e}^{\mathrm{i}\boldsymbol{q}\cdot\boldsymbol{r} + \lambda t}$ 的扰动，增长率 $\lambda$ 是矩阵 $J - q^2\operatorname{diag}(D_x, D_y)$ 的特征值（$q = \lvert\boldsymbol{q}\rvert$）。[2.5.7](/2.5.7#sec-7.5.2) 已经推出：当 $\operatorname{tr}J < 0$、$\det J > 0$（均匀系统稳定）时，失稳发生在

$$
h(q^2) = D_xD_yq^4 - (D_yJ_{11} + D_xJ_{22})q^2 + \det J
$$
对某个 $q$ 变负时，条件是 $D_yJ_{11} + D_xJ_{22} > 2\sqrt{D_xD_y\det J}$。

**例 18.3.2** 求 Brusselator 发生 Turing 失稳的条件与斑图的特征波长。

解：$J_{11} = b - 1$，$J_{22} = -a^2$，$\det J = a^2$。条件化为 $D_y(b - 1) - D_xa^2 > 2a\sqrt{D_xD_y}$，两边除以 $D_y$ 并记 $\eta = \sqrt{D_x/D_y}$：

$$
b - 1 > 2a\eta + a^2\eta^2 \quad\Longleftrightarrow\quad b > b_{\mathrm{T}} = (1 + a\eta)^2 .
$$
在阈值处 $h$ 的极小点 $q_{\mathrm{c}}^2 = \sqrt{\det J/(D_xD_y)} = a/\sqrt{D_xD_y}$，斑图的特征波长为 $2\pi/q_{\mathrm{c}}$，由反应速率与扩散系数决定，与容器大小无关。要使 Turing 失稳先于 Hopf 失稳出现（$b_{\mathrm{T}} < b_{\mathrm{c}} = 1 + a^2$），需要 $(1 + a\eta)^2 < 1 + a^2$，即 $\eta < (\sqrt{1 + a^2} - 1)/a$：抑制子 Y 必须比激活子 X 扩散得快得多。取 $a = 4.5$、$D_x = 2$、$D_y = 16$，$\eta = 0.354$，$b_{\mathrm{T}} = 6.71$，远小于 $b_{\mathrm{c}} = 21.25$。

![Brusselator 的 Turing 失稳（a = 4.5，Dx = 2，Dy = 16）：左为不同 b 时扰动增长率随波数的变化，右为 b = 7.5 时从微小随机扰动长成的二维斑图](./plots/brusselator-turing.py)

物理上，X 是扩散慢的自催化"激活子"，Y 是扩散快的"抑制子"（X 的生长消耗 Y，Y 的减少反过来限制 X）：X 的局部涨落自我放大，而它引起的 Y 的亏缺迅速扩散到周围，在周围抑制 X，于是形成间距一定的峰。图中的二维模拟从均匀态加 $10^{-2}$ 的随机扰动开始，长成条纹与斑点交织的"迷宫"状图样；斑图的具体排布由初始涨落决定，波长则由 $q_{\mathrm{c}}$ 决定，这正是耗散结构"由涨落触发、由系统选择"的特征。

Turing 斑图的实验验证晚了近 40 年：困难在于溶液中小分子的扩散系数都接近（约 $10^{-9}\,\mathrm{m^2\,s^{-1}}$）。1990 年 De Kepper 等在凝胶反应器中用亚氯酸盐–碘化物–丙二酸（CIMA）反应首次得到稳定的 Turing 斑图：碘离子与凝胶中的淀粉络合，有效扩散被大大减慢，满足了扩散系数差异的条件。在生物中，Turing 机制（或其推广：细胞间信号、力学反馈）被用来解释动物皮毛与鱼类体表的花纹、毛囊与羽毛原基的间距、指（趾）骨的周期排列等；这些系统中"激活子"与"抑制子"往往是分泌的信号蛋白，或是相互作用的细胞本身。生物数学中的系统讨论与捕食者–猎物系统中的斑图见 [7.4.5](/7.4.5#sec-5.6)。

## 18.4. 生命系统的热力学

### 18.4.1. 生命以负熵为食

Schrödinger 在《生命是什么》（1944）中写道："生命以负熵为食"：生物体靠不断地从环境中汲取负熵（negentropy），即向环境输出熵，来抵消自身的熵产生，维持高度有序的状态。用本章的语言，生物体是处于非平衡稳态的开放系统：

$$
\frac{\mathrm{d}S}{\mathrm{d}t} = \frac{\mathrm{d}_{\mathrm{e}}S}{\mathrm{d}t} + \frac{\mathrm{d}_{\mathrm{i}}S}{\mathrm{d}t} \approx 0, \qquad \frac{\mathrm{d}_{\mathrm{i}}S}{\mathrm{d}t} > 0, \qquad \frac{\mathrm{d}_{\mathrm{e}}S}{\mathrm{d}t} < 0 .
$$
它摄入低熵的物质（碳水化合物、$\ce{O2}$），排出高熵的物质（$\ce{CO2}$、水和其他排泄物）与热。以葡萄糖的完全氧化为例（$298\,\mathrm{K}$ 标准态，CRC 数据）：$\ce{C6H12O6(s) + 6O2(g) -> 6CO2(g) + 6H2O(l)}$，$\Delta_{\mathrm{r}}H^\circ_{\mathrm{m}} = -2803\,\mathrm{kJ\,mol^{-1}}$，$\Delta_{\mathrm{r}}S^\circ_{\mathrm{m}} = +259\,\mathrm{J\,mol^{-1}\,K^{-1}}$，$\Delta_{\mathrm{r}}G^\circ_{\mathrm{m}} = -2879\,\mathrm{kJ\,mol^{-1}}$。若这些自由能全部耗散，每摩尔葡萄糖在 $310\,\mathrm{K}$ 下产生约 $2879/310 \approx 9.3\,\mathrm{kJ\,K^{-1}}$ 的熵，其中物质本身的熵增只有 $0.26\,\mathrm{kJ\,K^{-1}}$，绝大部分以热的形式（$\lvert\Delta H\rvert/T$）输出到环境。可见生物体向外输出熵的主要途径是放热，"负熵"的来源是食物中可以利用的 Gibbs 自由能。一个静息的成年人基础代谢功率约 $100\,\mathrm{W}$，相应的熵产生速率约 $100/310 \approx 0.3\,\mathrm{W\,K^{-1}}$。

食物链的起点是光合作用，$\ce{6CO2(g) + 6H2O(l) -> C6H12O6(s) + 6O2(g)}$，$\Delta_{\mathrm{r}}S^\circ_{\mathrm{m}} = -259\,\mathrm{J\,mol^{-1}\,K^{-1}}$，$\Delta_{\mathrm{r}}G^\circ_{\mathrm{m}} = +2879\,\mathrm{kJ\,mol^{-1}}$：它由光驱动（$W' \ne 0$），产生低熵、高自由能的物质。光合作用的"负熵"最终来自太阳辐射：地球吸收来自约 $5800\,\mathrm{K}$ 的太阳表面的辐射，以约 $255\,\mathrm{K}$ 的红外**热辐射**发射同样多的能量；辐射的熵流为 $\frac43E/T$，所以每吸收并重新发射 $1\,\mathrm{J}$ 的能量，地球向太空净输出约 $\frac43(1/255 - 1/5800) \approx 5\times10^{-3}\,\mathrm{J\,K^{-1}}$ 的熵。地球上的大气环流、水循环与全部生命活动，都在这个熵的出口与太阳这个低熵的入口之间进行。

### 18.4.2. 细胞：开放的、远离平衡的系统

细胞的非平衡性在每个层次上都可以看到：

- 能量货币：ATP/ADP 的浓度比被维持在比平衡值高约 $10^9$ 倍（[6.3.7](/6.3.7#sec-7.6.2)），ATP 水解的亲和势约 $50\,\mathrm{kJ\,mol^{-1}}$，是驱动其他过程的统一的"力"。
- 输运：跨膜的离子梯度与膜电势（18.2.5 节）是由离子泵维持的非平衡稳态；神经冲动就是这种储存的电化学势能在局部的快速释放，静息电位要靠钠钾泵持续地耗散 ATP 来恢复。
- 计时与图案：生物振荡与发育中的斑图（18.3 节）都是耗散结构。
- 精度：Hopfield（1974）指出，蛋白质合成与 DNA 复制的出错率（约 $10^{-4}$ 与 $10^{-8}$ 以下）远低于仅靠正确与错误底物的结合自由能之差 $\Delta\Delta G$ 所能达到的平衡区分 $\mathrm{e}^{-\Delta\Delta G/RT}$。细胞用消耗 GTP 或 ATP 的不可逆步骤让底物经过多次"校对"，这称为动力学校对（kinetic proofreading），每一步的区分作用相乘，代价是能量的耗散。精度、速度与耗散之间的权衡是当代生物物理的一个中心问题。

### 18.4.3. 熵与信息

"熵"这个词今天有三层含义：

1. Clausius 熵：由 $\mathrm{d}S = \delta Q_{\mathrm{r}}/T$ 定义的状态函数，判断宏观过程的方向（[5.2.4](/5.2.4)、[6.3.2](/6.3.2)）；
2. Boltzmann 熵：$S = k_{\mathrm{B}}\ln\Omega$，度量宏观态所对应的微观态的多少，即无序的程度（[5.2.4](/5.2.4#fml-4.8.1)、[6.3.10](/6.3.10)）；
3. Shannon 熵（1948）：$H = -\sum_i p_i\log_2 p_i$，度量对系统状态的不确定性，即获得完整信息所需的信息量（[4.5.6](/4.5.6)）；量子系统的推广是 von Neumann 熵。

三者在统计力学中是统一的：Gibbs 熵 $S = -k_{\mathrm{B}}\sum_i p_i\ln p_i$ 对平衡分布等于 Clausius 熵，对等概率分布化为 Boltzmann 熵，它与 Shannon 熵只差一个因子 $k_{\mathrm{B}}\ln 2$。信息的处理因此有热力学代价。1961 年提出的 Landauer 原理（Landauer's principle）指出：在温度 $T$ 下擦除 1 比特信息，至少要向环境耗散 $k_{\mathrm{B}}T\ln 2$ 的热量（$310\,\mathrm{K}$ 时约 $3\times10^{-21}\,\mathrm{J}$，相当于 ATP 水解自由能的约 $1/30$）。这一原理解决了"Maxwell 妖"的佯谬：妖为了分拣分子必须记录并最终擦除信息，由此产生的熵不少于它使气体减少的熵。细胞感知环境、复制遗传信息、做出决策，都在这个热力学下限之上运行；从这个角度看，生命既是一种耗散结构，也是一种以能量耗散为代价处理信息的机器。

## 小结

| 主题 | 要点 |
|---|---|
| 熵流与熵产生 | $\mathrm{d}S = \mathrm{d}_{\mathrm{e}}S + \mathrm{d}_{\mathrm{i}}S$；$\mathrm{d}_{\mathrm{i}}S \ge 0$ 对任意系统成立，且局域成立；开放系统只要负熵流足够大，熵可以减少 |
| 化学反应 | 亲和势 $\mathcal{A} = -\sum\nu_{\mathrm{B}}\mu_{\mathrm{B}}$，熵产生 $\mathcal{A}\,\mathrm{d}\xi/T$；等温等压下 $T\,\mathrm{d}_{\mathrm{i}}S = -\mathrm{d}G$ |
| 局域平衡与熵平衡 | $\partial s/\partial t = -\nabla\cdot\boldsymbol{J}_S + \sigma$，$\sigma = \sum J_kX_k \ge 0$；力：$\nabla(1/T)$、$-\nabla\mu_{\mathrm{B}}/T$、$\boldsymbol{E}/T$、$\mathcal{A}/T$ |
| 线性区 | $J_k = \sum L_{kl}X_l$，$L$ 的对称部分半正定；化学反应只在 $\lvert\mathcal{A}\rvert \ll RT$ 时线性 |
| Onsager 倒易关系 | $L_{kl} = L_{lk}$（磁场中 $L_{kl}(\boldsymbol{B}) = L_{lk}(-\boldsymbol{B})$），依据是微观可逆性与涨落回归；例：$\Pi = T\alpha_{\mathrm{S}}$ |
| Curie 原理 | 各向同性介质中不同阶张量不耦合；化学反应驱动定向输运需要有取向的膜蛋白 |
| 膜输运 | $J_V = L_p(\Delta p - \sigma_{\mathrm{r}}\Delta\varPi)$，$J_{\mathrm{s}} = \omega\Delta\varPi + (1 - \sigma_{\mathrm{r}})\bar c_{\mathrm{s}}J_V$ |
| 能量耦合 | 耦合度 $q = L_{12}/\sqrt{L_{11}L_{22}}$，$\eta_{\max} = q^2/(1 + \sqrt{1 - q^2})^2$；钠钾泵约 $44\,\mathrm{kJ\,mol^{-1}}$ 对 ATP 约 $53\,\mathrm{kJ\,mol^{-1}}$ |
| 最小熵产生原理 | 线性区、常系数、倒易关系、定常边界条件下，稳态使 $P$ 极小且稳定；线性区不产生有序结构 |
| 耗散结构 | 开放、远离平衡、非线性（自催化）、涨落；靠持续耗散维持 |
| Brusselator | 稳态 $(a, b/a)$；$b > 1 + a^2$ 时 Hopf 分岔，出现稳定极限环 |
| Turing 斑图 | $b > (1 + a\sqrt{D_x/D_y})^2$；波长 $2\pi/q_{\mathrm{c}}$，$q_{\mathrm{c}}^2 = a/\sqrt{D_xD_y}$；需要抑制子扩散快得多 |
| 生命系统 | 非平衡稳态的开放系统；熵主要以热的形式输出；ATP、离子梯度、振荡与校对都以耗散为代价 |

## 思考题

1. 一杯热水在室温下冷却，熵减少了。用 $\mathrm{d}_{\mathrm{e}}S$ 与 $\mathrm{d}_{\mathrm{i}}S$ 分析这一过程，并指出熵产生发生在何处。
2. 为什么说 Gibbs 自由能判据是定理 18.1.1 的特例？在等温等容、非体积功不为零（如电池放电做电功）时，熵产生应怎样写？
3. 设 $\ce{A <=> B}$ 在 $298\,\mathrm{K}$ 下 $\mathcal{A} = 5\,\mathrm{kJ\,mol^{-1}}$。用式 (18.9) 的精确形式与线性近似分别计算 $v/v_+$，线性近似的相对误差有多大？
4. 若某转运体每转运 1 个葡萄糖只伴随 1 个 $\ce{Na+}$，按例 18.2.2 的数据，葡萄糖在胞内外的最大浓度比是多少？
5. Brusselator 中若 $a = 2$，Hopf 分岔发生在 $b$ 为多少时？分岔点附近振荡的周期约为多少（以无量纲时间计）？
6. 为什么 Turing 斑图要求抑制子比激活子扩散快？若 $D_x = D_y$，Brusselator 能否出现 Turing 失稳？
