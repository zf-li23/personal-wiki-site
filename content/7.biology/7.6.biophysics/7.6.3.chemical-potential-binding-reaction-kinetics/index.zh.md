---
title: 化学势、结合与反应动力学
description: 由稀溶液的格点模型得到化学势；气体、Henry 定律与氧级联；植物中的水势；电化学势；平衡条件与质量作用定律、由配分函数得到的平衡常数、细胞中 ATP 水解的自由能；作为统计力学的配体–受体结合与 Hill 函数；质子动力势以及由 c 环决定的 H⁺/ATP 比；两态弛豫、细致平衡、Arrhenius 与 Eyring 速率，以及偏离平衡的反应的耗散。
source_hash: af01fa576bf6
---

细胞是化学系统：其中的分子不断被制造和消耗、结合与解离、穿过膜、发生反应，数目并不固定。上一章处理的是粒子数守恒的系统；本章加入支配粒子交换的变量，即化学势，并把它用于几乎是课程中所有后续模型之基础的三种操作：物种之间的平衡（反应与结合），顺化学势与**电化学势**梯度的输运，以及趋向平衡的速率。本章通过格点模型引入化学势，并把它用于气体、植物中的水和离子（3.1），导出**质量作用定律**以及细胞中 ATP 水解的自由能（3.2），把配体结合作为统计力学处理（3.3），给出质子动力势的数值（3.4），最后转向动力学、细致平衡与能垒（3.5）。本章使用而不再重新推导 [6.3.4](/6.3.4)、[6.3.5](/6.3.5) 和 [6.3.7](/6.3.7) 的热力学以及 [6.3.16](/6.3.16) 的速率理论；结合的生物化学见 [7.1.7](/7.1.7)，生物能学见 [7.1.16](/7.1.16)，化学渗透偶联见 [7.1.23](/7.1.23)。本章的模型是 [7.6.4](/7.6.4) 的两态系统和 [7.2.22](/7.2.22) 的基因调控模型的基本构件。

## 3.1. 化学势

### 3.1.1. 来来去去的粒子

当某一物种的分子数可以改变时，自由能依赖于它，其导数就是**化学势**（[6.3.4](/6.3.4#sec-4.3.1)）：

$$
\mu_i = \left(\frac{\partial G}{\partial N_i}\right)_{T,p,N_{j\ne i}}, \qquad \mathrm{d}G = -S\,\mathrm{d}T + V\,\mathrm{d}p + \sum_i\mu_i\,\mathrm{d}N_i. \tag{3.1}
$$

它是增加一个分子的自由能代价（生物物理中通常指每个分子，以 $k_{\mathrm{B}}T$ 为单位；化学中指每摩尔，以 $RT$ 为单位；二者差一个 $N_{\mathrm{A}}$）。与温度和压强一样，它是**强度量**，也和它们一样在平衡时相等：分子从化学势高的区域、相或化合物移向化学势低的，直到数值相等。顺浓度梯度的扩散、**渗透**、氧进入血液、配体的结合和反应的进行，都是这同一条规则的实例。

在统计力学中，化学势作为粒子数约束的 Lagrange 乘子出现，正如 [7.6.2](/7.6.2#sec-2.2.2) 中的 $\beta$ 是能量的乘子。对一个能与温度为 $T$、化学势为 $\mu$ 的热库同时交换能量和分子的系统，能量为 $E_i$、含 $N_i$ 个分子的微观态的概率为

$$
p_i = \frac{\mathrm{e}^{-\beta(E_i - \mu N_i)}}{\mathcal{Z}}, \qquad \mathcal{Z} = \sum_i\mathrm{e}^{-\beta(E_i - \mu N_i)}, \qquad \langle N\rangle = k_{\mathrm{B}}T\,\frac{\partial\ln\mathcal{Z}}{\partial\mu}, \tag{3.2}
$$

这就是 Gibbs（巨正则）分布：化学势高的热库把分子推入系统。式 (3.2) 是 3.3 中用于结合的形式：**结合部位**是与溶液交换配体的小系统。

### 3.1.2. 稀溶液的格点推导

**公式 3.1.1（稀溶质的化学势）** 在理想稀溶液中，浓度为 $c$ 的溶质的化学势为

$$
\mu = \mu^\circ + k_{\mathrm{B}}T\ln\frac{c}{c^\circ}, \tag{3.3}
$$

其中 $c^\circ$ 是参考浓度（化学中为 $1\,\mathrm{M}$），$\mu^\circ$ 是标准化学势，即 $c = c^\circ$ 时的值。

**证明** 把溶液看作有 $N$ 个格点的格子，每个格点体积为 $v$，被 $N_p$ 个溶质分子和 $N - N_p$ 个溶剂分子占据，每个分子的能量分别为 $\varepsilon_p$ 和 $\varepsilon_s$，其中包含它们与周围溶剂的相互作用（稀溶液中每个溶质只被溶剂包围）。自由能为

$$
G = N_p\varepsilon_p + (N - N_p)\varepsilon_s - k_{\mathrm{B}}T\ln\binom{N}{N_p}.
$$

增加一个溶质分子即替换一个溶剂分子；用 Stirling 公式，$\partial\ln\binom{N}{N_p}/\partial N_p = \ln[(N - N_p)/N_p]$，所以

$$
\mu_p = \frac{\partial G}{\partial N_p} = \varepsilon_p - \varepsilon_s + k_{\mathrm{B}}T\ln\frac{N_p}{N - N_p} \approx \varepsilon_p - \varepsilon_s + k_{\mathrm{B}}T\ln(cv)
$$

在 $N_p \ll N$ 时成立，其中 $c = N_p/(Nv)$。写 $\ln(cv) = \ln(c/c^\circ) + \ln(c^\circ v)$，即得式 (3.3)，$\mu^\circ = \varepsilon_p - \varepsilon_s + k_{\mathrm{B}}T\ln(c^\circ v)$。$\square$

这个推导说明了两项的含义。对数项是熵的，即溶质的混合熵：物种越稀，放置它的方式越多，它的化学势越低。标准化学势则汇集了其余的一切：溶质与溶剂各自同周围环境相互作用能之差，以及一个依赖于 $c^\circ$ 的任意选取的项。只有在同一标准态下的化学势之差才有物理意义。与理想性的偏离，无论来自溶质分子之间的相互作用还是拥挤（7.6.23），都通过把 $c/c^\circ$ 换成**活度** $a = \gamma c/c^\circ$ 来吸收（[6.3.6](/6.3.6)）。

### 3.1.3. 气体与溶解的气体

对理想气体，用分压代替浓度作同样的推理，得到

$$
\mu = \mu^\circ + k_{\mathrm{B}}T\ln\frac{p}{p^\circ}, \qquad p^\circ = 10^5\,\mathrm{Pa}, \tag{3.4}
$$

采用 IUPAC 的**标准压力** $1\,\mathrm{bar}$（旧书用 $101\,325\,\mathrm{Pa}$，这使 $\mu^\circ$ 移动 $k_{\mathrm{B}}T\ln 1.013 = 0.013\,k_{\mathrm{B}}T$）。与液体接触的气体溶解，直到它在溶液中的化学势等于在气相中的；对溶解的气体用式 (3.3)，得到 **Henry 定律**（[6.3.5](/6.3.5#sec-5.2.1)），$c = k_{\mathrm{H}}p$：溶解的浓度正比于分压。对 $37\,^\circ\mathrm{C}$ 血浆中的氧，$k_{\mathrm{H}} \approx 1.4\,\mu\mathrm{M}$ 每 mmHg（$10\,\mu\mathrm{M\,kPa^{-1}}$）。

**例 3.1.1（氧级联）** 干燥空气含 20.95 % 的氧；在总压 $101.3\,\mathrm{kPa}$ 下，由 **Dalton 分压定律**，其分压为 $21.2\,\mathrm{kPa}$，即 $159\,\mathrm{mmHg}$。在通往线粒体的路上，分压一级一级下降：

| 位置 | $p_{\ce{O2}}$ / mmHg | 下降的原因 |
|---|---|---|
| 干燥空气 | $159$ | |
| 气管中的湿润空气 | $149$ | 水蒸气（$37\,^\circ\mathrm{C}$ 时 $47\,\mathrm{mmHg}$）稀释了气体 |
| 肺泡气 | 约 $100$ | 与每次呼吸未交换的气体混合，以及被血液摄取 |
| 动脉血 | 约 $95$ | 肺泡–动脉之间的小梯度 |
| 混合静脉血 | 约 $40$ | 被组织摄取 |
| 线粒体 | 约 $1$–$10$ | 细胞色素氧化酶的消耗 |

氧仅靠扩散沿这一级联下行。取 $5\,\mathrm{mmHg}$ 时，空气与线粒体之间的化学势差为每个分子 $k_{\mathrm{B}}T\ln(159/5) = 3.5\,k_{\mathrm{B}}T$（$8.9\,\mathrm{kJ\,mol^{-1}}$），与同一个分子被还原为水时释放的 $\sim 200\,k_{\mathrm{B}}T$ 相比很小。在动脉血浆中，Henry 定律只给出 $0.13\,\mathrm{mM}$ 的溶解氧；血红蛋白使血液的含氧量提高约七十倍，在高分压下协同地结合氧，在低分压下释放（[7.1.7](/7.1.7#sec-7.3)）。气体交换的生理学属于 [7.14](/7.14)。

### 3.1.4. 水势

水在土壤、根、茎、叶与空气之间流动而不需要泵：植物没有心脏，把水提升到树顶的能量来自叶面的蒸发。水流的方向由水的化学势决定，植物生理学家按单位体积来表示它。

**定义 3.1.1（水势）** 样品（细胞、土壤、木质部汁液、空气）的**水势**是其中水的化学势相对于同温度、大气压和零高度下的纯水的化学势，除以水的偏摩尔体积 $\bar V_{\mathrm{w}} = 18.0\,\mathrm{cm^3\,mol^{-1}}$：

$$
\Psi_{\mathrm{w}} = \frac{\mu_{\mathrm{w}} - \mu_{\mathrm{w}}^\circ}{\bar V_{\mathrm{w}}}. \tag{3.5}
$$

它的单位是压强，通常用兆帕表示；纯的自由水 $\Psi_{\mathrm{w}} = 0$，水自发地从较高的 $\Psi_{\mathrm{w}}$ 流向较低的。

溶质使水的化学势降低，压强使之升高，高度使之升高，与表面的结合使之降低；相应地

$$
\Psi_{\mathrm{w}} = \Psi_{\mathrm{s}} + \Psi_{\mathrm{p}} + \Psi_{\mathrm{g}} + \Psi_{\mathrm{m}}, \qquad
\Psi_{\mathrm{s}} = -cRT, \qquad \Psi_{\mathrm{g}} = \rho_{\mathrm{w}}gh. \tag{3.6}
$$

- 溶质（渗透）势 $\Psi_{\mathrm{s}} = -\Pi$ 是式 (2.10) 的**渗透压**（[7.6.2](/7.6.2#sec-2.3.3)）的负值，$c$ 是溶质粒子的总浓度：$20\,^\circ\mathrm{C}$ 下理想的 $1\,\mathrm{M}$ 溶液为 $-2.44\,\mathrm{MPa}$。真实溶液有偏差：$1\,\mathrm{M}$ 蔗糖约为 $-2.7\,\mathrm{MPa}$，$1\,\mathrm{M}$ $\ce{KCl}$ 解离成约 1.8 个有渗透效应的粒子，约为 $-4.5\,\mathrm{MPa}$，海水约为 $-2.5\,\mathrm{MPa}$。
- 压力势 $\Psi_{\mathrm{p}}$ 是高于大气压的静水压：膨胀的细胞压在细胞壁上时为正（膨压，通常 $0.3$–$1\,\mathrm{MPa}$），初始质壁分离时为零，蒸腾植物的木质部中为负（张力）。
- 重力势 $\Psi_{\mathrm{g}}$ 每米高度增加 $0.0098\,\mathrm{MPa}$：对草本植物可以忽略，在 $100\,\mathrm{m}$ 高的树顶约为 $1\,\mathrm{MPa}$。
- 基质势 $\Psi_{\mathrm{m}}$ 描述被束缚在表面和窄孔中的水（土壤颗粒、细胞壁）；它在干燥的土壤和种子中占主导，在水合的细胞中通常忽略。

空气是最强的汇。相对湿度为 $\mathrm{RH}$ 的水蒸气，由式 (3.4) 有 $\mu_{\mathrm{w}} - \mu_{\mathrm{w}}^\circ = RT\ln(\mathrm{RH})$，所以

$$
\Psi_{\mathrm{air}} = \frac{RT}{\bar V_{\mathrm{w}}}\ln(\mathrm{RH}), \qquad \frac{RT}{\bar V_{\mathrm{w}}} = 135\,\mathrm{MPa}\ \text{at}\ 20\,^\circ\mathrm{C}, \tag{3.7}
$$

相对湿度 $98\,\%$ 时为 $-2.7\,\mathrm{MPa}$，$50\,\%$ 时为 $-94\,\mathrm{MPa}$。

**例 3.1.2（水流过一棵树）** 在潮湿的日子，根周围的土壤 $\Psi_{\mathrm{w}} \approx -0.3\,\mathrm{MPa}$，根木质部约 $-0.6\,\mathrm{MPa}$，$10\,\mathrm{m}$ 高处的茎木质部约 $-0.8\,\mathrm{MPa}$（其中 $0.1\,\mathrm{MPa}$ 是重力项），叶木质部约 $-1.0\,\mathrm{MPa}$，叶肉细胞约 $-1.2\,\mathrm{MPa}$；湿度 50 % 的空气为 $-94\,\mathrm{MPa}$。水顺着这一梯度流过整个植物，由叶的蒸发拉动，并因氢键结合的水的内聚力而在张力下保持为连续的水柱（内聚力–张力机制）。最大的落差在叶与空气之间，横跨气孔，所以植物通过气孔的开闭来控制水分的散失。重力项和狭窄木质部导管中的流动摩擦随高度累加；在约 $120$–$130\,\mathrm{m}$ 处，树顶的水势会变得如此之负，以至叶细胞不能再扩张，水柱会因空穴化而断裂，这就是估计的树高上限。水分运输的生理学见 [7.13](/7.13)。

![蒸腾树木沿土壤–植物–大气连续体的水势，潮湿的日子（典型值，20 °C）。左：带取样点的示意树：土壤 −0.3 MPa，根木质部 −0.6 MPa，茎木质部 −0.8 MPa（含 10 m 处 0.1 MPa 的重力势），叶木质部 −1.0 MPa，叶肉细胞 −1.2 MPa，相对湿度 50 % 的空气 −94 MPa。右：沿路径依次排列的水势；水被动地从较高的 Ψw 流向较低的，远在刻度之外的空气值说明了驱动力的来源](./plots/water-potential.py)

### 3.1.5. 带电物种

对电荷为 $ze$、处于电势 $\varphi$ 的离子，增加一个离子的自由能包括电功 $ze\varphi$；相关的量是**电化学势**

$$
\tilde\mu = \mu^\circ + k_{\mathrm{B}}T\ln\frac{c}{c^\circ} + ze\varphi. \tag{3.8}
$$

跨越对该离子通透的膜，平衡要求 $\tilde\mu_{\mathrm{in}} = \tilde\mu_{\mathrm{out}}$，由此得到平衡电势的 **Nernst 方程**（[6.3.13](/6.3.13)），

$$
\varphi_{\mathrm{in}} - \varphi_{\mathrm{out}} = \frac{k_{\mathrm{B}}T}{ze}\ln\frac{c_{\mathrm{out}}}{c_{\mathrm{in}}} = \frac{61.5\,\mathrm{mV}}{z}\lg\frac{c_{\mathrm{out}}}{c_{\mathrm{in}}}\quad(37\,^\circ\mathrm{C}), \tag{3.9}
$$

其中 $310\,\mathrm{K}$ 时 $k_{\mathrm{B}}T/e = 26.7\,\mathrm{mV}$（$298\,\mathrm{K}$ 时为 $25.7\,\mathrm{mV}$，此时前因子为 $59.2\,\mathrm{mV}$）。一价离子的十倍浓度比相当于 $61.5\,\mathrm{mV}$，即每个离子 $2.3\,k_{\mathrm{B}}T$。膜电位及其在离子梯度和通透性中的来源是 7.6.30 的主题；这里把式 (3.8) 用于质子。

## 3.2. 化学平衡与质量作用定律

### 3.2.1. 平衡条件

把反应写成 $\sum_i\nu_i\mathrm{X}_i = 0$，化学计量数 $\nu_i$ 对反应物为负、对产物为正（$\mathrm{A} + \mathrm{B} \rightleftharpoons \mathrm{AB}$ 有 $\nu_{\mathrm{A}} = \nu_{\mathrm{B}} = -1$，$\nu_{\mathrm{AB}} = 1$）。反应前进一个事件时，$\mathrm{d}N_i = \nu_i$。

**定理 3.2.1（质量作用定律）** 在恒温恒压下，反应达到平衡时

$$
\sum_i\nu_i\mu_i = 0. \tag{3.10}
$$

对理想稀溶质，这等价于

$$
\prod_i\left(\frac{c_i}{c^\circ}\right)^{\nu_i} = K, \qquad K = \exp\!\left(-\frac{\sum_i\nu_i\mu_i^\circ}{k_{\mathrm{B}}T}\right) = \mathrm{e}^{-\Delta G^\circ/k_{\mathrm{B}}T}, \tag{3.11}
$$

其中平衡常数 $K$ 与浓度无关。

**证明** 一个事件使 $G$ 改变 $\mathrm{d}G = \sum_i\mu_i\,\mathrm{d}N_i = \sum_i\nu_i\mu_i$。平衡时 $G$ 对反应进度取极小，所以这个导数为零，即式 (3.10)。代入式 (3.3)，$\sum_i\nu_i\mu_i^\circ + k_{\mathrm{B}}T\sum_i\nu_i\ln(c_i/c^\circ) = 0$，取指数即得式 (3.11)。$\square$

式 (3.11) 是**标准平衡常数**的**质量作用定律**（[6.3.7](/6.3.7#sec-7.2.1)）。对结合 $\mathrm{A} + \mathrm{B} \rightleftharpoons \mathrm{AB}$，生物学家使用它的倒数并恢复量纲，即**解离常数**

$$
K_{\mathrm{d}} = \frac{[\mathrm{A}][\mathrm{B}]}{[\mathrm{AB}]} = c^\circ\,\mathrm{e}^{\Delta G^\circ_{\mathrm{bind}}/k_{\mathrm{B}}T}, \tag{3.12}
$$

它是一个浓度：使一半的 B 被结合时 A 的游离浓度。$-20.7\,k_{\mathrm{B}}T$ 的结合自由能（$310\,\mathrm{K}$ 时 $-53\,\mathrm{kJ\,mol^{-1}}$）对应 $K_{\mathrm{d}} = 1\,\mathrm{nM}$，每 $2.3\,k_{\mathrm{B}}T$ 使 $K_{\mathrm{d}}$ 改变十倍。

### 3.2.2. 偏离平衡的反应的自由能

如果浓度不在平衡，一个反应事件使 $G$ 改变

$$
\Delta G = \sum_i\nu_i\mu_i = \Delta G^\circ + k_{\mathrm{B}}T\ln Q, \qquad Q = \prod_i\left(\frac{c_i}{c^\circ}\right)^{\nu_i}, \tag{3.13}
$$

这是含**反应商** $Q$ 的**化学反应等温式**（[6.3.7](/6.3.7)）；$\Delta G = k_{\mathrm{B}}T\ln(Q/K)$。若 $\Delta G < 0$，即 $Q < K$，反应正向进行。标准自由能 $\Delta G^\circ$ 说明平衡偏向哪一边多远；实际的 $\Delta G$ 还依赖浓度，它说明反应将朝哪个方向进行以及能做多少功。仅凭 $\Delta G^\circ$ 判断细胞中反应的方向是常见的错误，因为细胞内的浓度远非 $1\,\mathrm{M}$。当在同样条件下比较相关的反应（突变对折叠或结合的影响）时，标准自由能作为稳定性的度量才有意义，7.6.8 和 7.6.16 就是这样使用它的。

### 3.2.3. 由配分函数得到平衡常数

标准化学势，从而 $K$，可由分子配分函数算出（[6.3.11](/6.3.11)）。对物种 $i$ 的 $N_i$ 个分子组成的理想气体或稀溶液，分子**配分函数**为 $q_i$，其自由能为 $-k_{\mathrm{B}}T\ln\prod_i(q_i^{N_i}/N_i!)$，所以 $\mu_i = -k_{\mathrm{B}}T\ln(q_i/N_i)$，式 (3.10) 变为

$$
\prod_i\left(\frac{N_i}{V}\right)^{\nu_i} = \prod_i\left(\frac{q_i}{V}\right)^{\nu_i}. \tag{3.14}
$$

平衡常数是产物与反应物单位体积可用状态数之比，每个状态按其 Boltzmann 因子加权（它包含在 $q_i$ 中，所有能量都从共同的零点量起）。较低的产物能量和较多的状态都有利于反应：两个分子比它们的复合物有更多的平动状态，所以结合必须克服 $1\,\mathrm{M}$ 时约 $10$–$15\,k_{\mathrm{B}}T$ 的平动与转动熵的损失（7.6.17）。

### 3.2.4. 细胞中的 ATP 水解

**例 3.2.1（一个 ATP 能提供多少自由能？）** 对 pH 7 下的 $\ce{ATP + H2O -> ADP + P_i}$，取生物化学**标准态**（除水和质子外，各物种为 $1\,\mathrm{M}$），$\Delta G^{\circ\prime} \approx -30.5\,\mathrm{kJ\,mol^{-1}}$，在 $310\,\mathrm{K}$ 下每个分子约 $-12\,k_{\mathrm{B}}T$（确切值依赖 $\ce{Mg^2+}$、pH 和离子强度；也有人引用接近 $-13\,k_{\mathrm{B}}T$ 的值）。在 *E. coli* 中，$[\mathrm{ATP}] \approx 5\,\mathrm{mM}$，$[\mathrm{ADP}] \approx 0.5\,\mathrm{mM}$，$[\mathrm{P_i}] \approx 10\,\mathrm{mM}$，

$$
Q = \frac{[\mathrm{ADP}][\mathrm{P_i}]}{[\mathrm{ATP}]} = \frac{(0.5\times10^{-3})(10^{-2})}{5\times10^{-3}} = 10^{-3}, \qquad
\Delta G \approx -12\,k_{\mathrm{B}}T + k_{\mathrm{B}}T\ln10^{-3} \approx -19\,k_{\mathrm{B}}T,
$$

约 $-48\,\mathrm{kJ\,mol^{-1}}$。在静息的肌肉中，游离 ADP 只有约 $20\,\mu\mathrm{M}$，$\Delta G \approx -24\,k_{\mathrm{B}}T$（$-61\,\mathrm{kJ\,mol^{-1}}$）。平衡时 $Q$ 应为 $K = \mathrm{e}^{11.8} \approx 1.4\times10^5$：活细胞中 $[\mathrm{ATP}]/[\mathrm{ADP}]$ 比其平衡值高八到九个数量级，正是这种偏离，而不是磷酸酐键本身的化学，使 ATP 成为自由能的储存。细胞条件下 ATP 水解的自由能，即**磷酸化势**（[7.1.16](/7.1.16#sec-16.3.2)），约为 $20\,k_{\mathrm{B}}T$，本课程通篇使用这个值。

![ATP 水解的自由能随质量作用比 Q = [ADP][Pi]/[ATP]（单位 M）的变化，ΔG = ΔG°′ + RT ln Q，310 K，ΔG°′ = −30.5 kJ/mol（约 −12 kBT），单位为 kBT（左）和 kJ/mol（右）。点：标准态（所有物种 1 M）、平衡（ΔG = 0，Q ≈ 1.4 × 10⁵ M）、*E. coli* 细胞（Q = 10⁻³ M，约 −19 kBT）和静息肌肉（Q ≈ 7.5 × 10⁻⁶ M，约 −24 kBT）；Q 每变化 10 倍，ΔG 改变 2.3 kBT](./plots/atp-free-energy.py)

## 3.3. 作为统计力学的结合

### 3.3.1. 配体格子中的受体

**配体**与受体的结合、转录因子与 DNA 的结合、氧与肌红蛋白的结合、药物与其靶标的结合，是生物学中最简单的反应，可以在一个玩具模型中从第一原理处理。

**定理 3.3.1（单个位点的占据率）** 设受体处于溶液中，溶液被模型化为 $\Omega$ 个格点的格子，含有 $L \ll \Omega$ 个配体分子。溶液中每个配体的能量为 $\varepsilon_{\mathrm{s}}$，结合在受体上的配体的能量为 $\varepsilon_{\mathrm{b}}$，$\Delta\varepsilon = \varepsilon_{\mathrm{b}} - \varepsilon_{\mathrm{s}}$。受体被占据的概率为

$$
p_{\mathrm{b}} = \frac{c/K_{\mathrm{d}}}{1 + c/K_{\mathrm{d}}} = \frac{c}{c + K_{\mathrm{d}}}, \qquad K_{\mathrm{d}} = c_0\,\mathrm{e}^{\Delta\varepsilon/k_{\mathrm{B}}T}, \tag{3.15}
$$

其中 $c = L/V$ 是配体浓度，$c_0 = \Omega/V$ 是格点的浓度。

**证明** 受体的两个宏观态是空与被占据。空：所有 $L$ 个配体都在溶液中，有 $\binom{\Omega}{L} \approx \Omega^L/L!$ 种排布，权重为 $(\Omega^L/L!)\mathrm{e}^{-\beta L\varepsilon_{\mathrm{s}}}$。被占据：一个配体结合，$L - 1$ 个在溶液中，权重为 $\mathrm{e}^{-\beta\varepsilon_{\mathrm{b}}}(\Omega^{L-1}/(L-1)!)\mathrm{e}^{-\beta(L-1)\varepsilon_{\mathrm{s}}}$。被占据与空的权重之比为 $(L/\Omega)\mathrm{e}^{-\beta\Delta\varepsilon} = (c/c_0)\mathrm{e}^{-\beta\Delta\varepsilon} = c/K_{\mathrm{d}}$，$p_{\mathrm{b}}$ 就是这个比值除以一加该比值。$\square$

结果是生物化学中的双曲线结合曲线，而模型说明了 $K_{\mathrm{d}}$ 是什么：一个浓度标度，由结合能（通过 Boltzmann 因子）和自由配体的熵（通过 $c_0$，即配体在溶液中的位置熵与在受体上同样小时的浓度）决定。近似 $\binom{\Omega}{L} \approx \Omega^L/L!$ 是稀的极限；精确的格点结果，即把 $c/K_{\mathrm{d}}$ 换成 $(L/(\Omega - L + 1))\mathrm{e}^{-\beta\Delta\varepsilon}$，只有当配体占满格子的相当大一部分时才偏离式 (3.15)。

**例 3.3.1（启动子处的 RNA 聚合酶）** 在 *E. coli* 中，约 $10^3$ 个 **RNA 聚合酶**分子几乎全部结合在 DNA 上，多数是非特异的。把基因组模型化为 $N_{\mathrm{NS}} \approx 5\times10^6$ 个结合能为 $\varepsilon_{\mathrm{NS}}$ 的非特异位点和一个能量为 $\varepsilon_{\mathrm{S}}$ 的**启动子**，由 $P$ 个聚合酶共享。按定理 3.3.1 计数排布，让非特异位点起格子的作用，且 $P \ll N_{\mathrm{NS}}$，启动子被占据的概率为

$$
p_{\mathrm{bound}} = \frac{1}{1 + \dfrac{N_{\mathrm{NS}}}{P}\,\mathrm{e}^{\Delta\varepsilon/k_{\mathrm{B}}T}}, \qquad \Delta\varepsilon = \varepsilon_{\mathrm{S}} - \varepsilon_{\mathrm{NS}}.
$$

取 $P = 500$ 个可用的聚合酶和 $\Delta\varepsilon = -5\,k_{\mathrm{B}}T$，$(N_{\mathrm{NS}}/P)\mathrm{e}^{\Delta\varepsilon} = 10^4\times6.7\times10^{-3} = 67$，$p_{\mathrm{bound}} \approx 0.015$；$\Delta\varepsilon = -12\,k_{\mathrm{B}}T$ 的强启动子有 94 % 的时间被占据。基因组本身起溶剂的作用，比值 $P/N_{\mathrm{NS}}$ 起浓度的作用，占据率随聚合酶数目上升，恰如结合曲线随配体浓度上升。结合在启动子旁边的调节因子改变它的有效 $\Delta\varepsilon$；这是基因调控的**热力学模型**（[7.2.11](/7.2.11)）的出发点。

![作为统计力学的配体结合。A、B：简单位点（n = 1）以及具有同样半饱和浓度 K 的、n = 2 和 4 个配体全或无结合的占据率 p_b = cⁿ/(cⁿ + Kⁿ)，分别采用线性（A）和对数（B）浓度轴；B 中的点线标出 10 % 和 90 % 的占据率，在其间 c 的变化对 n = 1 为 81 倍，n = 2 为 9 倍，n = 4 为 3 倍。C：定理 3.3.1 的格点模型，Ω = 1000 个格点，Δε = −2 kBT：配体稀时精确的占据率（点）遵循稀极限的结果 c/(c + K_d)（线），格子被占满时则高于它](./plots/binding-curves.py)

### 3.3.2. 通向同一结果的两条路

同样的占据率还可由另外两种描述得到，看到它们一致正是要点所在。

- 化学势：把位点看作与化学势为 $\mu = \mu^\circ + k_{\mathrm{B}}T\ln(c/c^\circ)$ 的热库交换配体的系统（式 (3.3)）。由式 (3.2)，取两个状态，空（$E = 0$，$N = 0$）和被占据（$E = \varepsilon_{\mathrm{b}}$，$N = 1$），$p_{\mathrm{b}} = \mathrm{e}^{-\beta(\varepsilon_{\mathrm{b}} - \mu)}/[1 + \mathrm{e}^{-\beta(\varepsilon_{\mathrm{b}} - \mu)}]$，这就是 $K_{\mathrm{d}} = c^\circ\mathrm{e}^{\beta(\varepsilon_{\mathrm{b}} - \mu^\circ)}$ 的式 (3.15)。
- 质量作用：对 $\mathrm{R} + \mathrm{L} \rightleftharpoons \mathrm{RL}$，$[\mathrm{R}][\mathrm{L}]/[\mathrm{RL}] = K_{\mathrm{d}}$（式 (3.12)），$p_{\mathrm{b}} = [\mathrm{RL}]/([\mathrm{R}] + [\mathrm{RL}]) = [\mathrm{L}]/([\mathrm{L}] + K_{\mathrm{d}})$。

统计力学的途径用能量给出 $K_{\mathrm{d}}$，热力学的途径用测得的标准自由能给出它。在基因调控模型中，把同样的推理用于有多个结合位点和聚合酶的启动子，就是 [7.2.11](/7.2.11) 的**热力学模型**。

### 3.3.3. Hill 函数

如果受体结合 $n$ 个配体，且配体数较少的中间态的布居可以忽略（全或无结合，$\mathrm{R} + n\mathrm{L} \rightleftharpoons \mathrm{RL}_n$），质量作用给出 $[\mathrm{R}][\mathrm{L}]^n/[\mathrm{RL}_n] = K^n$ 和

$$
p_{\mathrm{b}} = \frac{c^n}{c^n + K^n}, \tag{3.16}
$$

即 **Hill 方程**（[7.1.7](/7.1.7#sec-7.3.4)），$n > 1$ 时为 S 形。其陡峭程度由 **Hill 系数**度量：占据率从 10 % 到 90 % 的浓度比为 $81^{1/n}$，$n = 1$ 时 81 倍，$n = 2$ 时 9 倍，$n = 4$ 时 3 倍。真实的受体会布居其中间态，测得的 Hill 系数（半饱和处 $\ln[p_{\mathrm{b}}/(1 - p_{\mathrm{b}})]$ 对 $\ln c$ 的斜率）介于 1 和位点数之间；对有四个位点的血红蛋白约为 2.8。Hill 函数是唯象的描述；产生**协同性**的机制，即位点之间的相互作用与协同的构象变化，在 [7.6.4](/7.6.4) 中建模，而信号级联的陡峭响应，可以超过任何单个结合步骤的 Hill 系数，见 7.6.35。

### 3.3.4. 测量结合

结合曲线通过改变配体浓度并记录正比于结合分数的信号来测量：被标记的配体与较大的伴侣结合时荧光或**荧光各向异性**的变化（7.6.11），滴定每一步放出的热（**等温滴定量热法**，7.6.8），积聚在载有受体的表面上的质量（**表面等离子体共振**，7.6.17），或复合物滞留在滤膜上的放射性。只要 $c$ 是游离配体的浓度，拟合式 (3.15) 就给出 $K_{\mathrm{d}}$：如果受体浓度与 $K_{\mathrm{d}}$ 相当，结合会耗尽配体，总浓度必须用质量作用方程的二次解来修正。$K_{\mathrm{d}}$ 的温度依赖通过 van 't Hoff 关系给出结合焓，直接的量热测量则独立地给出它；二者的比较检验结合是否是简单的两态过程（7.6.8）。

## 3.4. 质子动力势的定量描述

### 3.4.1. 两个分量

Peter Mitchell 的**化学渗透学说**（[7.1.23](/7.1.23#sec-23.2.2)）指出，呼吸与光合的电子传递把质子泵过膜，所得梯度中储存的自由能驱动 **ATP 合酶**。由式 (3.8)，把一个质子从外侧（线粒体的膜间隙、细菌的周质、类囊体的腔）移到内侧，自由能改变 $\tilde\mu_{\mathrm{in}} - \tilde\mu_{\mathrm{out}} = k_{\mathrm{B}}T\ln(c_{\mathrm{in}}/c_{\mathrm{out}}) + e\,\Delta\Psi$，其中 $\Delta\Psi = \varphi_{\mathrm{in}} - \varphi_{\mathrm{out}}$。由 $\mathrm{pH} = -\lg a_{\ce{H+}}$，$\ln(c_{\mathrm{in}}/c_{\mathrm{out}}) = -2.303\,\Delta\mathrm{pH}$，其中 $\Delta\mathrm{pH} = \mathrm{pH}_{\mathrm{in}} - \mathrm{pH}_{\mathrm{out}}$。除以 $e$（或每摩尔除以 $F$）就得到一个电势。

**公式 3.4.1（质子动力势）** 跨膜的**质子动力势**为

$$
\Delta p = \Delta\Psi - \frac{2.303\,RT}{F}\,\Delta\mathrm{pH}, \qquad \frac{2.303\,RT}{F} = 61.5\,\mathrm{mV}\ (37\,^\circ\mathrm{C}),\ 59.2\,\mathrm{mV}\ (25\,^\circ\mathrm{C}), \tag{3.17}
$$

其中 $\Delta\Psi = \varphi_{\mathrm{in}} - \varphi_{\mathrm{out}}$，$\Delta\mathrm{pH} = \mathrm{pH}_{\mathrm{in}} - \mathrm{pH}_{\mathrm{out}}$。一摩尔质子向内流动所释放的自由能为 $\Delta G = F\,\Delta p$，对被激活的膜（内侧为负、偏碱性）为负。

常被引用的 59 mV 是 $25\,^\circ\mathrm{C}$ 的值；在体温下，每个 pH 单位的因子是 $61.5\,\mathrm{mV}$。两个分量可以互相转换：让反离子通过的膜使 $\Delta\Psi$ 崩溃而建立起 $\Delta\mathrm{pH}$，不同的膜两者的平衡不同。

### 3.4.2. 线粒体、细菌与叶绿体

**例 3.4.1（肝线粒体的质子动力势）** 取 $\Delta\Psi \approx -170\,\mathrm{mV}$（基质为负）和 $\Delta\mathrm{pH} \approx +0.5$（基质偏碱），式 (3.17) 给出

$$
\Delta p = -170\,\mathrm{mV} - 61.5\,\mathrm{mV}\times0.5 \approx -201\,\mathrm{mV},
$$

其中 85 % 是电的。每个进入基质的质子释放 $F\,\lvert\Delta p\rvert = 96\,485\,\mathrm{C\,mol^{-1}}\times0.201\,\mathrm{V} = 19.4\,\mathrm{kJ\,mol^{-1}}$，每个质子 $7.5\,k_{\mathrm{B}}T$。

在外部 pH 为 7 的 *E. coli* 中，质子动力势量级相同，主要是电的。在被光照的叶绿体中，它主要是化学的：类囊体膜对 $\ce{Cl-}$ 和 $\ce{Mg^2+}$ 通透，它们中和被泵出的质子的电荷，所以腔比基质酸化 2–3 个 pH 单位，而 $\Delta\Psi$ 仍然很小。

![质子动力势的定量描述（310 K）。A：典型的被激活的膜的电分量（ΔΨ）与化学分量（61.5 mV × ΔpH）：哺乳动物线粒体（170 mV 和 0.5 个 pH 单位，合计约 200 mV）、外部 pH 7 的 *E. coli*（140 mV 和 0.4，约 165 mV）和光照下的叶绿体类囊体（约 30 mV 和 2.5 个 pH 单位，约 185 mV）。B：具有 c 个 c 亚基的 c 环的 ATP 合酶所能维持的最大磷酸化势 (c/3)FΔp，Δp = 150 和 200 mV，与细胞中的磷酸化势（阴影，45–60 kJ/mol）比较；点标出已知的环大小：牛线粒体中的 c8，酵母线粒体和 *E. coli* 中的 c10，叶绿体中的 c14 和某些蓝细菌中的 c15](./plots/proton-motive-force.py)

### 3.4.3. 每个 ATP 需要几个质子？

要逆着磷酸化势 $\Delta G_{\mathrm{p}}$ 制造一个 ATP，ATP 合酶至少必须让 $n_{\min} = \Delta G_{\mathrm{p}}/(F\,\lvert\Delta p\rvert)$ 个质子通过。线粒体基质中 $\Delta G_{\mathrm{p}} \approx 50\,\mathrm{kJ\,mol^{-1}}$，所以 $n_{\min} \approx 50/19.4 \approx 2.6$：热力学要求每个 ATP 多于两个质子，而不是一个。

实际的数目由酶的结构决定（[7.1.23](/7.1.23#sec-23.3.4)）。每个通过 $\mathrm{F_o}$ 的质子使 c 环转过一个亚基，环与 γ 轴转一整圈在 $\mathrm{F_1}$ 的三个催化位点上制造三个 ATP（[7.1.23](/7.1.23#sec-23.3.3)）。因此含 $c$ 个亚基的环给出每个 ATP $c/3$ 个质子：动物线粒体的 c₈ 环为 $8/3 = 2.7$，酵母线粒体和 *E. coli* 为 $10/3 = 3.3$，叶绿体为 $14/3 = 4.7$。哺乳动物的酶工作在接近热力学极限处：$2.7\times19.4\,\mathrm{kJ\,mol^{-1}} = 52\,\mathrm{kJ\,mol^{-1}}$，刚好高于它所维持的磷酸化势。叶绿体的环更大，可以在每个质子较低的质子动力势下，或逆着更高的 $\Delta G_{\mathrm{p}}$ 制造 ATP。把每个 ATP 从基质输出到胞质还要多花约一个质子（磷酸载体随一个质子输入 $\mathrm{P_i}$，腺嘌呤核苷酸转位酶逆着膜电位交换 $\ce{ATP^4-}$ 与 $\ce{ADP^3-}$），所以胞质中的一个 ATP 约耗 $3.7$ 个质子，每氧化一个 NADH 泵出十个质子，由此得到约 $2.7$ 的 P/O 比（[7.1.23](/7.1.23#sec-23.3.5)）。

## 3.5. 速率

### 3.5.1. 两态反应的弛豫

平衡说明系统最终到哪里，而不说它多快到达。对最简单的反应 $\mathrm{S} \rightleftharpoons \mathrm{P}$，速率常数为 $k_+$（S 到 P）和 $k_-$（P 到 S），总浓度 $C = [\mathrm{S}] + [\mathrm{P}]$，分数 $x = [\mathrm{P}]/C$ 服从**一级反应**方程。

**公式 3.5.1（两态弛豫）** 处于状态 P 的分数满足

$$
\frac{\mathrm{d}x}{\mathrm{d}t} = k_+(1 - x) - k_-x, \qquad
x(t) = x_{\mathrm{eq}} + [x(0) - x_{\mathrm{eq}}]\,\mathrm{e}^{-t/\tau}, \qquad
x_{\mathrm{eq}} = \frac{k_+}{k_+ + k_-}, \quad \tau = \frac{1}{k_+ + k_-}. \tag{3.18}
$$

有两个特点是普遍的。**弛豫时间** $\tau$ 由两个速率常数之和决定，而不是由其中任何一个单独决定：反应的弛豫比其较慢方向所暗示的更快。并且平衡只依赖比值 $k_+/k_-$，弛豫只依赖和；因此同时测量平衡与弛豫（例如在温度跳变之后，即 [6.3.15](/6.3.15) 的**弛豫法**），就能确定两个速率常数。

![两态反应 S ⇌ P 的动力学。A：沿反应坐标的自由能剖面：P 比 S 低约 2 kBT，过渡态比 S 高约 12 kBT。B：P 中的分数 x 从 x = 0（实线）和从 x = 1（虚线）出发的弛豫，k₊ = 0.88，k₋ = 0.12（单位 1/τ）：两者都达到 x_eq = k₊/(k₊ + k₋) = 0.88，时间常数同为 τ = 1/(k₊ + k₋)。C：Eyring 速率 k = (kBT/h) e^(−ΔG‡/kBT)，310 K，随能垒的变化，并标出平均等待时间 1/k 为 1 ns、1 µs、1 ms、1 s、1 h 和 1 yr 之处：能垒每增加 2.3 kBT，反应变慢十倍](./plots/two-state-kinetics.py)

### 3.5.2. 细致平衡

平衡分数可以用三种方式算出：由动力学，$x_{\mathrm{eq}} = k_+/(k_+ + k_-)$；由质量作用，$[\mathrm{P}]/[\mathrm{S}] = K$；以及由宏观态的 Boltzmann 分布（式 (2.6)），$[\mathrm{P}]/[\mathrm{S}] = \mathrm{e}^{-\Delta G/k_{\mathrm{B}}T}$，$\Delta G = G_{\mathrm{P}} - G_{\mathrm{S}}$。它们必须一致。

**定理 3.5.1（反应的细致平衡）** 平衡时每个**基元反应**的正向与逆向通量相等，速率常数之比由热力学确定：

$$
k_+[\mathrm{S}]_{\mathrm{eq}} = k_-[\mathrm{P}]_{\mathrm{eq}}, \qquad \frac{k_+}{k_-} = K = \mathrm{e}^{-\Delta G^\circ/k_{\mathrm{B}}T}. \tag{3.19}
$$

对基元反应 $\sum_s\nu_s\mathrm{S}_s \rightleftharpoons \sum_p\nu_p\mathrm{P}_p$，质量作用通量为 $J_+ = k_+\prod_sc_s^{\nu_s}$ 和 $J_- = k_-\prod_pc_p^{\nu_p}$，平衡条件（$J_+ = J_-$）与式 (3.11) 结合，在 $c^\circ$ 的单位下给出 $k_+/k_- = K$。

这就是**细致平衡原理**（[3.5.9](/3.5.9)）：平衡时每一个过程都被它的逆过程所平衡，而不仅仅是每个物种的总产生与总消耗。它约束模型：在有闭合回路的反应网络中，平衡时绕回路的正向速率常数之积除以逆向速率常数之积必须等于 1（自由能是**状态函数**），所以循环中的速率常数不是独立的。细致平衡是平衡的性质。必须把它与**稳态**区分开来，稳态中浓度恒定，但净通量可以绕循环流动；ATP 维持的活细胞稳态，恰恰是细致平衡被打破的状态（3.5.4）。

### 3.5.3. 能垒：Arrhenius 与 Eyring

比值 $k_+/k_-$ 由自由能差决定，而速率本身由状态之间的能垒决定。过渡态理论（[6.3.16](/6.3.16#sec-16.3)）给出 **Eyring 方程**

$$
k = \kappa\,\frac{k_{\mathrm{B}}T}{h}\,\mathrm{e}^{-\Delta G^\ddagger/k_{\mathrm{B}}T}, \tag{3.20}
$$

其中透射系数 $\kappa \le 1$，$310\,\mathrm{K}$ 时 $k_{\mathrm{B}}T/h = 6.5\times10^{12}\,\mathrm{s^{-1}}$。两个方向穿过同一个过渡态，$\Delta G^\ddagger_- = \Delta G^\ddagger_+ - \Delta G$，所以式 (3.20) 自动满足式 (3.19)。$30\,k_{\mathrm{B}}T$ 的能垒给出每秒约一个事件，每多 $2.3\,k_{\mathrm{B}}T$ 使反应变慢十倍。

酶降低 $\Delta G^\ddagger$ 而不改变 $\Delta G$：它使两个方向加快同样的倍数，而不触动平衡。酶典型的 $10^{10}$ 的速率增强，相当于能垒降低 $23\,k_{\mathrm{B}}T$（[7.1.8](/7.1.8)）。

**例 3.5.1（温度系数）** 经验的 **Arrhenius 方程** $k = A\,\mathrm{e}^{-E_{\mathrm{a}}/RT}$ 给出 $310$ 与 $300\,\mathrm{K}$ 的速率之比，即 $Q_{10}$，为 $\exp[(E_{\mathrm{a}}/R)(1/300 - 1/310)\,\mathrm{K^{-1}}]$：$E_{\mathrm{a}} = 50\,\mathrm{kJ\,mol^{-1}}$ 时为 $1.9$，$100\,\mathrm{kJ\,mol^{-1}}$ 时为 $3.6$。多数酶促和生理速率的 $Q_{10}$ 在 2 到 3 之间，这就是外温动物的代谢在寒冷天气里慢下几倍的原因。陡峭得多的温度依赖，$Q_{10}$ 为 10 到 100，说明有单一能垒之外的东西：温度感觉中温度门控通道（7.6.4）或蛋白质解折叠（7.6.8）的大焓变。

对水中大分子的构象变化，式 (3.20) 的前因子 $k_{\mathrm{B}}T/h$，即气相中越过能垒的频率，并不合适：沿反应坐标的运动被溶剂过阻尼，前因子由摩擦决定。这种情形的理论，即 Kramers 理论，需要 Brown 运动的理论，在 7.6.5 中发展；它给出蛋白质折叠 $10^6$–$10^8\,\mathrm{s^{-1}}$ 的前因子，即 7.6.16 的“速度极限”。

### 3.5.4. 偏离平衡的反应

对质量作用通量为 $J_\pm$ 的基元反应，式 (3.11)、(3.13) 和 (3.19) 结合成通量与热力学驱动力 $\Delta\mu = -\Delta G = -\sum_i\nu_i\mu_i$（每个事件释放的自由能）之间的关系：

$$
\frac{J_+}{J_-} = \mathrm{e}^{\Delta\mu/k_{\mathrm{B}}T}, \qquad \dot W = (J_+ - J_-)\,\Delta\mu = k_{\mathrm{B}}T\,(J_+ - J_-)\ln\frac{J_+}{J_-} \ge 0. \tag{3.21}
$$

净通量沿 $\Delta\mu$ 的方向，自由能以速率 $\dot W$（每单位体积）被耗散，它只在平衡时为零。不等式成立是因为对任何正数 $a, b$ 有 $(a - b)\ln(a/b) \ge 0$：它就是对单个反应的第二定律 $\mathrm{d}_{\mathrm{i}}S \ge 0$（[7.6.2](/7.6.2#sec-2.5.1)）。

式 (3.21) 还显示了细胞如何利用 ATP。考虑一个酶，它循环经过三个状态：结合 ATP、水解它并释放产物。绕循环一周，细致平衡要求正向速率常数（各乘以相应的浓度）之积等于逆向速率常数之积；而 ATP 与 ADP 被保持在远离平衡的状态时，这个比值是 $\mathrm{e}^{\Delta\mu_{\mathrm{ATP}}/k_{\mathrm{B}}T} \approx \mathrm{e}^{20}$，循环优先朝一个方向转动。分子马达（7.6.27）、动力学校对（[7.2.22](/7.2.22#sec-22.7)、7.6.17）、感觉适应（7.6.35）和生化时钟（7.6.38）都是这类循环，而其通量与耗散的理论，即随机热力学，在 7.6.38 中发展。

### 3.5.5. 作为化工厂的细胞

组成恒定的细胞并不是静止的：其分子不断被制造和降解，代谢物在几秒内相互转化，连结构元件也在周转。速率方程描述这种通量。以速率 $\beta$ 产生、以速率 $\gamma$ 清除的分子的水平满足 $\mathrm{d}n/\mathrm{d}t = \beta - \gamma n$，这是朝稳态 $\beta/\gamma$ 的一级弛豫，时间常数为 $1/\gamma$（公式 3.5.1，固定一个状态）；在生长的细菌中，蛋白质主要靠稀释而被清除，$\gamma = \ln 2/\tau_{\mathrm{doubling}}$（[7.2.22](/7.2.22#sec-22.3)）。细胞骨架给出第二个例子。肌动蛋白丝在其刺端以速率 $k_{\mathrm{on}}c$ 添加单体、以速率 $k_{\mathrm{off}}$ 丢失单体，所以它的长度按

$$
\frac{\mathrm{d}L}{\mathrm{d}t} = \delta\,(k_{\mathrm{on}}c - k_{\mathrm{off}}), \qquad c_{\mathrm{c}} = \frac{k_{\mathrm{off}}}{k_{\mathrm{on}}}, \tag{3.22}
$$

变化，每个亚基 $\delta = 2.7\,\mathrm{nm}$：它在**临界浓度** $c_{\mathrm{c}}$ 之上生长，在其下缩短，并且由细致平衡，$c_{\mathrm{c}}$ 就是亚基从丝端的**解离常数**。取 $k_{\mathrm{on}} \approx 11\,\mu\mathrm{M^{-1}\,s^{-1}}$，$k_{\mathrm{off}} \approx 1.4\,\mathrm{s^{-1}}$，$c_{\mathrm{c}} \approx 0.13\,\mu\mathrm{M}$，在 $10\,\mu\mathrm{M}$ 肌动蛋白下，一根丝每秒增长约 $110$ 个亚基，即 $0.3\,\mu\mathrm{m}$，这正是爬行细胞前缘前进的速度。因为丝中的 ATP 水解使两端不同，细胞中丝的稳态不是平衡，丝会踏车（7.6.26）。

## 小结

- 化学势（3.1）：$\mu = \partial G/\partial N$ 是一个分子的自由能代价；稀溶质为 $\mu = \mu^\circ + k_{\mathrm{B}}T\ln(c/c^\circ)$（公式 3.1.1），源于格点模型的混合熵，气体为 $\mu^\circ + k_{\mathrm{B}}T\ln(p/p^\circ)$，$p^\circ = 10^5\,\mathrm{Pa}$，式 (3.4)。氧靠扩散沿分压级联从空气中的 $159\,\mathrm{mmHg}$ 下降到线粒体中的几 mmHg（例 3.1.1）。水势 $\Psi_{\mathrm{w}} = (\mu_{\mathrm{w}} - \mu^\circ_{\mathrm{w}})/\bar V_{\mathrm{w}}$（定义 3.1.1）是溶质、压力、重力和基质项之和，式 (3.6)，驱动水从土壤（$-0.3\,\mathrm{MPa}$）流向空气（50 % 湿度时 $-94\,\mathrm{MPa}$）（例 3.1.2）。对离子，电化学势增加 $ze\varphi$，式 (3.8)，并给出 Nernst 方程，$37\,^\circ\mathrm{C}$ 时每十倍 $61.5\,\mathrm{mV}$，式 (3.9)。
- 平衡（3.2）：$\sum\nu_i\mu_i = 0$ 给出质量作用定律 $\prod(c_i/c^\circ)^{\nu_i} = K = \mathrm{e}^{-\Delta G^\circ/k_{\mathrm{B}}T}$（定理 3.2.1）；$K_{\mathrm{d}} = 1\,\mathrm{nM}$ 对应 $-20.7\,k_{\mathrm{B}}T$，式 (3.12)。偏离平衡时 $\Delta G = \Delta G^\circ + k_{\mathrm{B}}T\ln Q$，式 (3.13)；$K$ 是配分函数之比，式 (3.14)。ATP 水解在标准态下释放约 $-12\,k_{\mathrm{B}}T$，在细胞中约 $-20\,k_{\mathrm{B}}T$，因为 $[\mathrm{ATP}]/[\mathrm{ADP}]$ 被保持在比平衡高 $10^8$–$10^9$ 倍的水平（例 3.2.1）。
- 结合（3.3）：配体格子中的受体被占据的概率为 $c/(c + K_{\mathrm{d}})$，$K_{\mathrm{d}} = c_0\mathrm{e}^{\Delta\varepsilon/k_{\mathrm{B}}T}$（定理 3.3.1），与由化学势或质量作用得到的结果相同；$n$ 个配体的全或无结合给出 Hill 函数，式 (3.16)，其 10–90 % 的范围为 $81^{1/n}$。RNA 聚合酶在启动子与数百万个非特异位点之间的分配遵循同一定律，以 $P/N_{\mathrm{NS}}$ 为浓度（例 3.3.1）；结合用荧光、量热或表面方法测量，须注意配体的耗尽（3.3.4）。
- 质子动力势（3.4）：$\Delta p = \Delta\Psi - 61.5\,\mathrm{mV}\,\Delta\mathrm{pH}$（公式 3.4.1）；线粒体中约 $-200\,\mathrm{mV}$，85 % 是电的，每个质子 $7.5\,k_{\mathrm{B}}T$（例 3.4.1）。每个 ATP 至少需要 2.6 个质子；c 环决定 $c/3$：2.7（c₈）、3.3（c₁₀）、4.7（c₁₄）。
- 速率（3.5）：两态弛豫的 $\tau = 1/(k_+ + k_-)$（公式 3.5.1）；细致平衡 $k_+/k_- = \mathrm{e}^{-\Delta G^\circ/k_{\mathrm{B}}T}$ 是平衡的性质，不是稳态的性质（定理 3.5.1）；Eyring 速率每 $2.3\,k_{\mathrm{B}}T$ 的能垒下降十倍，式 (3.20)，酶降低能垒而不移动平衡，典型活化能的 $Q_{10} \approx 2$–$3$（例 3.5.1）。偏离平衡时 $J_+/J_- = \mathrm{e}^{\Delta\mu/k_{\mathrm{B}}T}$，耗散 $(J_+ - J_-)\Delta\mu \ge 0$，式 (3.21)；ATP 驱动的循环破坏细致平衡。细胞是处于稳定通量中的化工厂：产生与清除以时间常数 $1/\gamma$ 弛豫，丝在临界浓度 $c_{\mathrm{c}} = k_{\mathrm{off}}/k_{\mathrm{on}}$ 之上生长，式 (3.22)。

## 思考题

1. 两个隔室含有氧的摩尔分数分别为 $0.5436$ 和 $0.2000$ 的气体混合物，总压和温度（$37\,^\circ\mathrm{C}$）相同。氧的化学势之差是多少，每个分子以 $k_{\mathrm{B}}T$ 为单位、每摩尔又是多少？氧会沿哪个方向通过对它通透的膜？

   **答** 总压相同时，$\Delta\mu = k_{\mathrm{B}}T\ln(0.5436/0.2000) = k_{\mathrm{B}}T\ln 2.718 = 1.00\,k_{\mathrm{B}}T$ 每分子，每摩尔 $RT = 2.58\,\mathrm{kJ\,mol^{-1}}$。氧从摩尔分数较高（分压较高、化学势较高）的隔室移向另一个，直到分压相等。

2. 一个叶细胞的溶质势为 $-1.5\,\mathrm{MPa}$，膨压为 $0.6\,\mathrm{MPa}$。把它放在 (a) 纯水中，(b) $\Psi_{\mathrm{w}} = -0.9\,\mathrm{MPa}$ 的溶液中，(c) $\Psi_{\mathrm{w}} = -2.0\,\mathrm{MPa}$ 的溶液中。每种情形下水是进入还是离开细胞，最终状态如何？

   **答** 细胞的水势为 $\Psi_{\mathrm{w}} = -1.5 + 0.6 = -0.9\,\mathrm{MPa}$。(a) 水进入（从 $0$ 到 $-0.9$）；细胞膨胀，直到细胞壁把膨压提高到约 $1.5\,\mathrm{MPa}$，此时 $\Psi_{\mathrm{w}} = 0$（细胞被稀释，溶质势也略有升高）。(b) 没有净流动：细胞已处于平衡。(c) 水离开；膨压降到零，并且由于 $\Psi_{\mathrm{s}}$ 仍高于 $-2.0\,\mathrm{MPa}$，原生质体收缩而脱离细胞壁（质壁分离），直到因失水而浓缩的溶质势达到 $-2.0\,\mathrm{MPa}$。

3. 最高的树约 $115\,\mathrm{m}$。树顶的重力对水势的贡献是多少？如果树顶的叶要生长就必须保持 $\Psi_{\mathrm{w}} \ge -2.0\,\mathrm{MPa}$，而木质部中的摩擦消耗与重力相当，土壤为 $-0.3\,\mathrm{MPa}$，这对树高提示什么极限？

   **答** $\rho gh = 1000\times9.8\times115\,\mathrm{Pa} = 1.13\,\mathrm{MPa}$。摩擦等于重力时，沿树干的落差为 $2\rho gh$；要求 $-0.3 - 2\rho gh/10^6 \ge -2.0$，得 $h \le 1.7/(2\times0.0098) \approx 87\,\mathrm{m}$。真实的树更高，因为在宽的导管中摩擦比重力小；对红杉的详细分析把极限定在约 $120$–$130\,\mathrm{m}$，此时树顶的叶在约 $-2\,\mathrm{MPa}$ 下几乎不能扩张。

4. 一个蛋白质在 $25\,^\circ\mathrm{C}$ 下以 $K_{\mathrm{d}} = 10\,\mu\mathrm{M}$ 结合配体。取 $c^\circ = 1\,\mathrm{M}$，结合的标准自由能是多少？一个突变使结合减弱 $1.4\,\mathrm{kcal\,mol^{-1}}$；新的 $K_{\mathrm{d}}$ 是多少，在 $10\,\mu\mathrm{M}$ 配体下占据率如何变化？

   **答** $\Delta G^\circ = RT\ln(K_{\mathrm{d}}/c^\circ) = 2.48\,\mathrm{kJ\,mol^{-1}}\times\ln10^{-5} = -28.5\,\mathrm{kJ\,mol^{-1}}$（$-11.5\,k_{\mathrm{B}}T$，$-6.8\,\mathrm{kcal\,mol^{-1}}$）。$1.4\,\mathrm{kcal\,mol^{-1}} = 5.86\,\mathrm{kJ\,mol^{-1}} = 2.36\,RT$，即因子 $\mathrm{e}^{2.36} = 10.6$：$K_{\mathrm{d}} \approx 106\,\mu\mathrm{M}$。$10\,\mu\mathrm{M}$ 下的占据率从 $0.50$ 降到 $10/116 = 0.086$。

5. 对有两个依次结合的位点的受体，$\mathrm{R} \rightleftharpoons \mathrm{RL} \rightleftharpoons \mathrm{RL}_2$，解离常数为 $K_1$ 和 $K_2$，写出被占据位点的平均分数 $\bar\theta$ 作为 $c$ 的函数。证明当两个位点独立且相同、位点解离常数为 $K$ 时，它化为简单的结合曲线；当 $K_2 \ll K_1$ 且 $K_1K_2$ 固定时，化为 $n = 2$ 的 Hill 函数。

   **答** R、RL 和 RL₂ 的权重为 $1$、$c/K_1$ 和 $c^2/(K_1K_2)$，所以 $\bar\theta = \dfrac{c/K_1 + 2c^2/(K_1K_2)}{2\left[1 + c/K_1 + c^2/(K_1K_2)\right]}$。对位点常数为 $K$ 的两个独立相同位点，宏观常数为 $K_1 = K/2$（结合第一个配体有两种方式）和 $K_2 = 2K$（失去第二个有两种方式），$\bar\theta$ 化简为 $c/(c + K)$。若 $K_2 \to 0$、$K_1 \to \infty$ 且 $K_1K_2 = K^2$ 固定，中间态消失，$\bar\theta \to c^2/(c^2 + K^2)$，即 $n = 2$ 的 Hill 函数：强的正协同性意味着第二个配体比第一个结合得紧得多。

6. 光照下类囊体腔的 pH 为 5.5，基质 pH 为 8.0，$\Delta\Psi \approx 0$（$25\,^\circ\mathrm{C}$）。计算质子动力势和每个质子的自由能。对 c₁₄ 环，叶绿体 ATP 合酶所能维持的最大磷酸化势是多少？

   **答** 以基质为“内”，$\Delta\mathrm{pH} = 8.0 - 5.5 = 2.5$，$\Delta p = -59.2\,\mathrm{mV}\times2.5 = -148\,\mathrm{mV}$；每个流入基质的质子释放 $F\times0.148\,\mathrm{V} = 14.3\,\mathrm{kJ\,mol^{-1}}$。每个 ATP 需要 $14/3 = 4.67$ 个质子，最大的 $\Delta G_{\mathrm{p}}$ 为 $4.67\times14.3 = 67\,\mathrm{kJ\,mol^{-1}}$，远高于基质中约 $45$–$55\,\mathrm{kJ\,mol^{-1}}$ 的磷酸化势：较大的环补偿了比线粒体更低的质子动力势。

7. 某个构象变化在 $25\,^\circ\mathrm{C}$ 下的速率常数为 $k_+ = 50\,\mathrm{s^{-1}}$ 和 $k_- = 5\,\mathrm{s^{-1}}$。两个状态之间的自由能差、平衡分数以及扰动后的弛豫时间各是多少？如果一种药物只通过减慢 $k_-$ 使产物态稳定 $2\,k_{\mathrm{B}}T$，这三个量怎样变化？

   **答** $\Delta G = -k_{\mathrm{B}}T\ln(k_+/k_-) = -2.30\,k_{\mathrm{B}}T$（$-5.7\,\mathrm{kJ\,mol^{-1}}$）；$x_{\mathrm{eq}} = 50/55 = 0.909$；$\tau = 1/55\,\mathrm{s} = 18\,\mathrm{ms}$。$k_-$ 减小 $\mathrm{e}^2 = 7.39$ 倍到 $0.68\,\mathrm{s^{-1}}$ 后：$\Delta G = -4.30\,k_{\mathrm{B}}T$，$x_{\mathrm{eq}} = 50/50.68 = 0.987$，$\tau = 19.7\,\mathrm{ms}$。平衡显著移动而弛豫时间几乎不变，因为它由较快的速率常数主导。

8. 证明式 (3.21) 的耗散速率 $\dot W$ 非负，并且在平衡附近它是驱动力的二次式：$\dot W \approx J_{\mathrm{eq}}\,\Delta\mu^2/k_{\mathrm{B}}T$，其中 $J_{\mathrm{eq}}$ 是平衡时的单向通量。净通量与力之间相应的线性关系是什么？

   **答** 取 $a = J_+$，$b = J_-$，$(a - b)\ln(a/b) \ge 0$，因为 $a - b$ 与 $\ln(a/b)$ 同号。在平衡附近写 $J_\pm = J_{\mathrm{eq}}(1 \pm \varepsilon/2)$，$\varepsilon$ 很小；则 $J_+ - J_- = J_{\mathrm{eq}}\varepsilon$，$\Delta\mu = k_{\mathrm{B}}T\ln(J_+/J_-) \approx k_{\mathrm{B}}T\varepsilon$，所以 $J_+ - J_- \approx (J_{\mathrm{eq}}/k_{\mathrm{B}}T)\Delta\mu$，是系数为 $J_{\mathrm{eq}}/k_{\mathrm{B}}T$ 的线性通量–力关系，而 $\dot W \approx (J_{\mathrm{eq}}/k_{\mathrm{B}}T)\Delta\mu^2$。这就是非平衡态热力学的线性区（[6.3.18](/6.3.18#sec-18.2.1)）；$\Delta\mu_{\mathrm{ATP}} \approx 20\,k_{\mathrm{B}}T$ 的细胞远远工作在它之外。

9. （设计题）你想知道，荧光观察到的蛋白质缓慢构象变化是否受单一能垒限制。提出速率随温度和稳定配体变化的测量，并说明什么结果支持单能垒模型。

   **答** 在几个温度下分别测量 $k_+$ 和 $k_-$（由平衡分数和温度或浓度跃变后的弛豫时间，公式 3.5.1）。单一能垒预言两者的 Arrhenius（或 Eyring）图都是直线，其活化焓之差等于平衡的 van 't Hoff 焓。加入结合其中一个状态的配体，应按结合常数改变 $k_+/k_-$（细致平衡，定理 3.5.1），$\ln k$ 与 $\ln K$ 呈线性关系，斜率定位两个端点状态之间的过渡态。弯曲的 Arrhenius 图、需要多于一个指数的弛豫或延迟相，表明有中间态或多个能垒。
