---
title: 热力学第二定律与熵
description: 自发过程的共同特征与第二定律的表述；Carnot 定理与 Brayton 循环；熵、积分因子与 Clausius 不等式；熵增加原理与环境熵变；理想气体 pVT 变化、传热、混合与相变的熵变计算；Nernst 热定理、完美晶体与热力学第三定律，量热熵与 Debye T³ 外推；化学反应的熵变；熵与能量退降。
---

热力学第一定律说明能量守恒，却不能回答过程的方向：气体不会自动从低压流向高压，热不会自动从低温物体传到高温物体，$\ce{H2(g) + 1/2O2(g) -> H2O(l)}$ 放出 $286\,\mathrm{kJ\,mol^{-1}}$ 的热，把这些热还给水却不能使它分解；能量既然守恒，为什么还会有"能源危机"？回答这些问题的是热力学第二定律。它在物理中已经从热机效率出发建立起来（[5.2.4](/5.2.4)）：两种表述、Carnot 定理、Clausius 熵与 Boltzmann 熵。本章从化学的需要出发重新组织这些内容，重点是可以操作的计算：在什么条件下可以用哪个判据，怎样为不可逆过程设计可逆途径来计算熵变，怎样由量热数据与第三定律得到物质的规定熵，从而算出化学反应的熵变。熵判据要求同时考虑系统与环境，使用不便；下一章（[6.3.3](/6.3.3)）由它导出只涉及系统的 Helmholtz 自由能与 Gibbs 自由能判据。熵的统计意义（$S = k_{\mathrm{B}}\ln\Omega$）在 [6.3.10](/6.3.10) 中定量展开，开放系统的熵产生与熵流见 [6.3.18](/6.3.18)。

## 2.1. 自发过程与热力学第二定律

### 2.1.1. 自发过程的共同特征

在一定的环境条件下不需要外界做功就能自动进行的过程称为**自发过程**（[6.1.6 定义 6.4.1](/6.1.6#def-6.4.1)），通常说的"过程的方向"就是自发过程的方向：水从高处流向低处，热从高温物体传向低温物体，溶质从高浓度处扩散到低浓度处。一切自发过程都有确定的方向，它们的逆过程不能自动进行。

以 $273\,\mathrm{K}$ 的 $1\,\mathrm{m^3}$、$4\,\mathrm{kPa}$ 的 $\ce{N2}$ 为例：向真空膨胀到 $1\,\mathrm{kPa}$（体积 $4\,\mathrm{m^3}$）是自发的，$W = Q = 0$。要让它复原，可以在恒定外压 $4\,\mathrm{kPa}$ 下等温压缩，环境做功 $W = 4\,\mathrm{kPa} \times 3\,\mathrm{m^3} = 12\,\mathrm{kJ}$，系统放热 $12\,\mathrm{kJ}$ 给热源。系统复原了，环境却"失功得热"；只有把这 $12\,\mathrm{kJ}$ 的热全部变回功而不留下其他变化，环境才能复原。自发过程的共同特征是：

1. 自发过程单向地从不平衡趋向平衡，它的限度是平衡态；
2. 自发过程都有做功的本领（[6.1.6](/6.1.6#sec-6.4.1)），可以设计装置利用它对外做功；
3. 自发过程都是**不可逆过程**：让它返回时，环境无一例外要付出代价。

每一种自发过程的不可逆性都可以归结为同一件事：功可以无代价地全部变为热，热却不能无代价地全部变为功。注意不是热不能全部变成功（理想气体等温可逆膨胀就把吸收的热全部变成了功），而是这样做必然留下其他变化（这里是气体的体积增大）。

### 2.1.2. 第二定律的表述

**热力学第二定律**有几种等价的表述（[5.2.4 定理 4.2.1](/5.2.4#thm-4.2.1)）：

- **Clausius 表述**：热不可能从低温物体传到高温物体而不引起其他变化；
- **Kelvin 表述**：不可能从单一热源取出热使之完全变为功而不发生其他变化；
- Ostwald 表述：**第二类永动机**是不可能造成的。

它们是大量经验的总结，等价性用反证法证明（[5.2.4](/5.2.4#sec-4.2.2)）。任何不可逆过程都可以通过适当的途径与热功转换的不可逆性联系起来，所以第二定律可以用来判断一切过程的方向。但直接用文字表述判断需要很强的技巧，我们需要一个定量的判据，这要从热机效率说起。

在两个热源之间循环工作的热机，从高温热源 $T_{\mathrm{h}}$ 吸热 $Q_1 > 0$，向低温热源 $T_{\mathrm{c}}$ 放热 $Q_2 < 0$，对外做功 $-W = Q_1 + Q_2$，效率 $\eta = -W/Q_1 = 1 + Q_2/Q_1$。**Carnot 定理**（[5.2.4 定理 4.4.1](/5.2.4#thm-4.4.1)）说：工作于同样两个热源之间的一切热机，以可逆热机的效率最高；一切可逆热机的效率都相等，与工作物质无关，等于 **Carnot 循环**的效率。写成数学形式：

$$
1 + \frac{Q_2}{Q_1} \le 1 - \frac{T_{\mathrm{c}}}{T_{\mathrm{h}}} \quad\Longleftrightarrow\quad \frac{Q_1}{T_{\mathrm{h}}} + \frac{Q_2}{T_{\mathrm{c}}} \le 0,
\tag{2.1}
$$

等号对可逆循环成立，不等号对不可逆循环成立。它的实际意义是给出了热机效率的上限，指出提高效率的根本途径是增大两个热源的温差；理论意义则是 Clausius 由它发现了熵。

**例 2.1.1（Brayton 循环）** 燃气轮机按 Brayton 循环工作：(1) 压缩机吸入温度为 $T_1$ 的环境空气，绝热压缩到 $T_{\mathrm{comp}}$；(2) 压缩空气在燃烧室中等压升温到 $T_2$；(3) 高温高压气体绝热膨胀推动涡轮做功，降温到 $T_3$；(4) 废气在低压下等压放热，回到 $T_1$。把空气看作理想气体、各步可逆，求循环效率；给定 $T_1$ 与燃烧室温度 $T_2$，效率最高能达到多少？

解：两个等压过程中，吸热 $Q_1 = nC_{p,\mathrm{m}}(T_2 - T_{\mathrm{comp}})$，放热 $Q_2 = -nC_{p,\mathrm{m}}(T_3 - T_1)$。两个绝热过程在相同的两个压力之间进行，由绝热方程 $T^\gamma p^{1-\gamma} = $ 常数（[6.3.1](/6.3.1)），$T_{\mathrm{comp}}/T_1 = T_2/T_3 = (p_{\text{高}}/p_{\text{低}})^{(\gamma-1)/\gamma}$，即 $T_3 = T_1T_2/T_{\mathrm{comp}}$。于是

$$
\eta = 1 + \frac{Q_2}{Q_1} = 1 - \frac{T_3 - T_1}{T_2 - T_{\mathrm{comp}}} = 1 - \frac{T_1}{T_{\mathrm{comp}}}.
$$

效率只由压缩比决定。$T_{\mathrm{comp}}$ 不能超过燃烧室温度 $T_2$，所以 $\eta < 1 - T_1/T_2$：$T_{\mathrm{comp}} \to T_2$ 时效率趋于工作在 $T_1$、$T_2$ 之间的 Carnot 效率，但此时燃烧室几乎不再加热，每摩尔空气的净功 $nC_{p,\mathrm{m}}[(T_2 - T_3) - (T_{\mathrm{comp}} - T_1)]$ 趋于零。因此"最大效率 $1 - T_1/T_2$"只是一个达不到的上限；实际设计关心的是净功最大的工况：对 $T_{\mathrm{comp}}$ 求极值得 $T_{\mathrm{comp}} = \sqrt{T_1T_2}$，此时 $\eta = 1 - \sqrt{T_1/T_2}$。取 $T_1 = 300\,\mathrm{K}$、$T_2 = 1500\,\mathrm{K}$，Carnot 上限为 $0.80$，净功最大时效率为 $0.55$，压缩比约 $17$。Brayton 循环的效率低于 Carnot 效率，原因是它在一个温度范围内吸热、在另一个温度范围内放热，而不是只与两个恒温热源交换热量。

![Ideal Brayton cycle between ambient 300 K and burner 1500 K: the efficiency rises towards the Carnot limit as the compression outlet temperature Tcomp approaches T2, while the net work per mole of air vanishes there; the work is largest at Tcomp = √(T1T2)](./plots/brayton-cycle.py)

## 2.2. 熵与 Clausius 不等式

### 2.2.1. 熵

式 (2.1) 对两个热源之间的可逆循环给出"热温商"之和为零：$Q_1/T_{\mathrm{h}} + Q_2/T_{\mathrm{c}} = 0$。任意可逆循环可以用许多微小的 Carnot 循环拼成（相邻小循环的公共绝热线上来回各走一次，相互抵消），小循环无限多时得到 **Clausius 等式**（[5.2.4 定理 4.5.1](/5.2.4#thm-4.5.1)）

$$
\oint\left(\frac{\delta Q}{T}\right)_{\mathrm{r}} = 0.
$$

设系统从状态 A 经可逆途径 $\mathrm{R}_1$ 到达 B，再经另一可逆途径 $\mathrm{R}_2$ 回到 A，则 $\int_{\mathrm{A}}^{\mathrm{B}}(\delta Q/T)_{\mathrm{R}_1} = \int_{\mathrm{A}}^{\mathrm{B}}(\delta Q/T)_{\mathrm{R}_2}$：两个平衡态之间可逆过程的热温商之和与途径无关。所以存在一个状态函数，Clausius 在 1865 年把它命名为**熵**（[5.2.4 定义 4.5.1](/5.2.4#def-4.5.1)）：

$$
\mathrm{d}S = \frac{\delta Q_{\mathrm{r}}}{T}, \qquad \Delta S = S_2 - S_1 = \int_1^2\frac{\delta Q_{\mathrm{r}}}{T}.
\tag{2.2}
$$

用微分方程的语言说，$\delta Q_{\mathrm{r}}$ 不是全微分，$1/T$ 是它的**积分因子**（[2.2.15 定义 15.4.2](/2.2.15#def-15.4.2)）。以理想气体为例，$\delta Q_{\mathrm{r}} = \mathrm{d}U - \delta W_{\mathrm{r}} = C_V\,\mathrm{d}T + \frac{nRT}{V}\,\mathrm{d}V$，交叉偏导数 $\partial C_V/\partial V = 0$ 而 $\partial(nRT/V)/\partial T = nR/V$，两者不等，所以 $\delta Q_{\mathrm{r}}$ 不是任何函数的全微分；除以 $T$ 后

$$
\frac{\delta Q_{\mathrm{r}}}{T} = \frac{C_V}{T}\,\mathrm{d}T + \frac{nR}{V}\,\mathrm{d}V, \qquad \frac{\partial}{\partial V}\left(\frac{C_V}{T}\right) = 0 = \frac{\partial}{\partial T}\left(\frac{nR}{V}\right),
$$

满足全微分条件，它就是 $\mathrm{d}S$。第二定律的内容可以概括为：对任何系统，$\delta Q_{\mathrm{r}}$ 都有一个只依赖于温度、而且对一切物质都相同的积分因子 $1/T$。

关于熵：它是第二定律的基本状态函数，是广延量，单位 $\mathrm{J\,K^{-1}}$；系统经历任何过程（可逆或不可逆）都有确定的熵变，它在数值上等于始态与终态之间任一可逆途径的热温商之和。不可逆过程的热温商则不等于熵变，下面看它们之间的关系。

### 2.2.2. Clausius 不等式

由式 (2.1)，两个热源之间的不可逆循环 $Q_1/T_{\mathrm{h}} + Q_2/T_{\mathrm{c}} < 0$；推广到与一系列热源接触的任意不可逆循环，$\sum_i\delta Q_i/T_i < 0$，$T_i$ 是与系统交换热量 $\delta Q_i$ 的热源的温度。设系统从状态 1 经一个不可逆过程到达状态 2，再经可逆过程回到 1，构成一个不可逆循环：

$$
\int_1^2\left(\frac{\delta Q}{T_{\mathrm{sur}}}\right)_{\mathrm{ir}} + \int_2^1\left(\frac{\delta Q}{T}\right)_{\mathrm{r}} < 0 \quad\Longrightarrow\quad \Delta S = S_2 - S_1 > \int_1^2\left(\frac{\delta Q}{T_{\mathrm{sur}}}\right)_{\mathrm{ir}}.
$$

与可逆的情形合在一起，就是 **Clausius 不等式**（[5.2.4 定理 4.6.1](/5.2.4#thm-4.6.1)）：

$$
\Delta S \ge \int_1^2\frac{\delta Q}{T_{\mathrm{sur}}}, \qquad \mathrm{d}S \ge \frac{\delta Q}{T_{\mathrm{sur}}} \qquad (> \text{不可逆},\ = \text{可逆}).
\tag{2.3}
$$

关于式 (2.3) 要注意：

1. 它描述封闭系统中任意过程的熵变与热温商的关系，是第二定律的数学表达式，与"第二类永动机不可能"等价：封闭系统中不可能发生熵变小于热温商的过程。
2. 分母 $T_{\mathrm{sur}}$ 是环境（热源）的温度。不可逆过程中系统可能根本没有统一的温度；只有取等号（可逆过程）时，$T_{\mathrm{sur}} = T$，才可以理解为系统的温度。
3. 用途：比较一个过程的熵变与热温商，就能判断它是不可逆的（$>$）、可逆的（$=$）还是不可能发生的（$<$）。缺点是要同时计算 $\Delta S$ 与热温商，而热温商与过程有关，计算往往很麻烦。

### 2.2.3. 熵增加原理与熵判据

对绝热系统，$\delta Q = 0$，式 (2.3) 化为

$$
\Delta S_{\text{绝热}} \ge 0 \qquad (> \text{不可逆},\ = \text{可逆}):
$$

绝热系统的熵不可能减少，这就是**熵增加原理**（[5.2.4 定理 4.6.2](/5.2.4#thm-4.6.2)）；绝热可逆过程是**等熵过程**。**孤立系统**当然是绝热的，而且孤立系统中发生的不可逆过程不受外界推动，一定是自发的，所以

$$
\Delta S_{\text{孤立}} \ge 0 \qquad (> \text{自发},\ = \text{可逆，即平衡}).
$$

孤立系统中的过程总是朝着熵增加的方向进行，限度是熵达到极大值的平衡态。这个熵判据同时解决了孤立系统中过程的方向与限度问题；从宏观上看，熵是孤立系统稳定性的标度。

实际的系统很少是孤立的。处理办法是把系统与和它有相互作用的环境合在一起，看作一个"大孤立系统"：

$$
\Delta S_{\text{孤立}} = \Delta S_{\text{系统}} + \Delta S_{\text{环境}} \ge 0.
$$

环境通常是一个温度为 $T_{\mathrm{sur}}$ 的巨大热源（大气、恒温槽），有限的热量流入或流出不改变它的温度，也不破坏它内部的平衡，对环境自身而言这种传热总可以看作可逆的；环境吸收的热就是系统放出的实际热 $-Q_{\text{系统}}$。因此

$$
\Delta S_{\text{环境}} = \frac{Q_{\text{环境}}}{T_{\mathrm{sur}}} = -\frac{Q_{\text{系统}}}{T_{\mathrm{sur}}}.
\tag{2.4}
$$

式中的 $Q_{\text{系统}}$ 是实际过程的热，而不是计算系统熵变时所设计的可逆途径的热。把式 (2.4) 代入熵判据，$\Delta S_{\text{系统}} - Q_{\text{系统}}/T_{\mathrm{sur}} \ge 0$，与 Clausius 不等式 (2.3) 一致（$T_{\mathrm{sur}}$ 恒定时）。三种判据的适用范围：

| 判据 | 形式 | 适用于 |
|---|---|---|
| Clausius 不等式 | $\Delta S \ge \int\delta Q/T_{\mathrm{sur}}$ | 封闭系统的任意过程：判断可逆与否 |
| 熵增加原理 | $\Delta S \ge 0$ | 绝热系统：判断可逆与否 |
| 熵判据 | $\Delta S_{\text{系统}} + \Delta S_{\text{环境}} \ge 0$ | 孤立系统（或系统加环境）：判断自发与平衡 |

## 2.3. 熵变的计算

### 2.3.1. 基本方法

由式 (2.2)，熵变只能沿可逆途径计算：过程可逆，直接用 $\Delta S = \int\delta Q_{\mathrm{r}}/T$；过程不可逆，就在相同的始态与终态之间设计一条可逆途径（由等温、等压、等容的可逆步骤与可逆相变组成）来计算。熵是广延量，复杂系统的熵变等于各部分熵变之和。需要计算的过程分三类：简单物理变化（$pVT$ 变化、传热），复杂物理变化（混合、相变），化学反应（§2.4.3）。

### 2.3.2. 简单 $pVT$ 变化

等温可逆过程 $\Delta S = Q_{\mathrm{r}}/T$；对理想气体 $Q_{\mathrm{r}} = -W_{\mathrm{r}} = nRT\ln(V_2/V_1)$。等容或等压的简单变温过程，$\delta Q_{\mathrm{r}} = C_V\,\mathrm{d}T$ 或 $C_p\,\mathrm{d}T$：

$$
\Delta S = \int_{T_1}^{T_2}\frac{C_V}{T}\,\mathrm{d}T \quad(\text{等容}), \qquad \Delta S = \int_{T_1}^{T_2}\frac{C_p}{T}\,\mathrm{d}T \quad(\text{等压}),
$$

即 $(\partial S/\partial T)_V = C_V/T$、$(\partial S/\partial T)_p = C_p/T$：温度升高熵增大，每升高 $1\,\mathrm{K}$ 熵增加 $C/T$。热容为常数时 $\Delta S = C\ln(T_2/T_1)$。这两个式子对凝聚相与实际气体同样适用。理想气体的 $p$、$V$、$T$ 同时变化时，设计两步：先等温、后等压（或先等温、后等容，或先等压、后等容），得

$$
\Delta S = nR\ln\frac{p_1}{p_2} + nC_{p,\mathrm{m}}\ln\frac{T_2}{T_1} = nR\ln\frac{V_2}{V_1} + nC_{V,\mathrm{m}}\ln\frac{T_2}{T_1} = nC_{p,\mathrm{m}}\ln\frac{V_2}{V_1} + nC_{V,\mathrm{m}}\ln\frac{p_2}{p_1}
\tag{2.5}
$$

（$C_{V,\mathrm{m}}$ 为常数）。三种形式由 $pV = nRT$ 相互换算，不必记忆，掌握设计途径的方法即可。理想气体的任意等温过程（可逆与否）都有 $\Delta S = nR\ln(p_1/p_2)$。

**例 2.3.1** $1\,\mathrm{mol}$ He（理想气体，$C_{V,\mathrm{m}} = \frac{3}{2}R$）从 $273.15\,\mathrm{K}$、$1\,\mathrm{MPa}$ 分别经下列过程变到 $100\,\mathrm{kPa}$：(1) 等温可逆；(2) 在恒外压 $100\,\mathrm{kPa}$ 下等温膨胀；(3) 等容降温；(4) 绝热可逆；(5) 在恒外压 $100\,\mathrm{kPa}$ 下绝热膨胀。求各过程的熵变。

解：(1) $\Delta S = R\ln(p_1/p_2) = R\ln 10 = 19.14\,\mathrm{J\,K^{-1}}$。

(2) 终态与 (1) 相同，熵是状态函数，$\Delta S = 19.14\,\mathrm{J\,K^{-1}}$。实际过程的热 $Q = -W = p_2(V_2 - V_1) = RT(1 - p_2/p_1) = 2044\,\mathrm{J}$，热温商 $Q/T = 7.48\,\mathrm{J\,K^{-1}} < \Delta S$，过程不可逆。环境的熵变 $-Q/T = -7.48\,\mathrm{J\,K^{-1}}$，孤立系统的熵增加 $11.66\,\mathrm{J\,K^{-1}}$；而过程 (1) 中环境的熵变为 $-19.14\,\mathrm{J\,K^{-1}}$，总熵变为零。

(3) 等容下压力降为原来的十分之一，$T_2 = 27.3\,\mathrm{K}$，$\Delta S = C_{V,\mathrm{m}}\ln(T_2/T_1) = \frac{3}{2}R\ln 0.1 = -28.72\,\mathrm{J\,K^{-1}}$。

(4) 绝热可逆，$\Delta S = 0$。

(5) 由 [6.3.1 例 1.4.1](/6.3.1#sec-1.4.3) 的方法，$T_2 = \frac{C_{V,\mathrm{m}} + Rp_2/p_1}{C_{p,\mathrm{m}}}T_1 = 174.8\,\mathrm{K}$。设计途径：先在 $273.15\,\mathrm{K}$ 等温可逆膨胀到 $100\,\mathrm{kPa}$，再等压可逆降温到 $174.8\,\mathrm{K}$，由式 (2.5)

$$
\Delta S = R\ln 10 + \frac{5}{2}R\ln\frac{174.8}{273.15} = 19.14 - 9.28 = 9.87\,\mathrm{J\,K^{-1}} > 0.
$$

绝热过程的熵增大，过程不可逆，与熵增加原理一致。

这个例子解释了 [6.3.1](/6.3.1#sec-1.4.3) 中的结论"从同一始态出发，绝热可逆与绝热不可逆过程不能到达同一终态"：前者 $\Delta S = 0$，后者 $\Delta S > 0$，两个终态的熵不同。膨胀到相同的终压时，由 $(\partial S/\partial T)_p = C_p/T > 0$，熵大的终态温度高，$T_{2,\mathrm{ir}} > T_{2,\mathrm{r}}$；再由 $W = \Delta U = nC_{V,\mathrm{m}}(T_2 - T_1)$，绝热可逆膨胀降温最多，对外做功也最多。

### 2.3.3. 传热

**例 2.3.2** 绝热容器被一块固定的绝热隔板分为两部分，分别装有 $1\,\mathrm{mol}$ He（$200\,\mathrm{K}$）与 $1\,\mathrm{mol}$ $\ce{H2}$（$300\,\mathrm{K}$），压力都是 $100\,\mathrm{kPa}$。把隔板换成固定的铝板（导热，热容可忽略），求达到平衡后的 $\Delta H$ 与 $\Delta S$。He 的 $C_{V,\mathrm{m}} = \frac{3}{2}R$，$\ce{H2}$ 的 $C_{V,\mathrm{m}} = \frac{5}{2}R$。

解：先确定终态。以两种气体为系统，$Q = 0$，$W = 0$，故 $\Delta U = \Delta U(\mathrm{He}) + \Delta U(\ce{H2}) = 0$：

$$
\tfrac{3}{2}R(T_2 - 200\,\mathrm{K}) + \tfrac{5}{2}R(T_2 - 300\,\mathrm{K}) = 0, \qquad T_2 = 262.5\,\mathrm{K}.
$$

两种气体都经历等容变温：

$$
\begin{aligned}
\Delta H &= \tfrac{5}{2}R(262.5 - 200)\,\mathrm{K} + \tfrac{7}{2}R(262.5 - 300)\,\mathrm{K} = 207.9\,\mathrm{J},\\
\Delta S &= \tfrac{3}{2}R\ln\frac{262.5}{200} + \tfrac{5}{2}R\ln\frac{262.5}{300} = 3.39 - 2.78 = 0.62\,\mathrm{J\,K^{-1}} > 0.
\end{aligned}
$$

系统是孤立的，熵增加，热传导是自发的不可逆过程。注意孤立系统的 $\Delta U = 0$ 而 $\Delta H \ne 0$：$\Delta H = \Delta U + V\Delta p$，两侧压力都变了。

一般地，两个等压热容为 $C_p$ 的相同物体，温度分别为 $T_{\mathrm{h}}$ 与 $T_{\mathrm{c}}$，接触后达到 $T_2 = (T_{\mathrm{h}} + T_{\mathrm{c}})/2$，

$$
\Delta S = C_p\ln\frac{T_2}{T_{\mathrm{h}}} + C_p\ln\frac{T_2}{T_{\mathrm{c}}} = C_p\ln\frac{(T_{\mathrm{h}} + T_{\mathrm{c}})^2}{4T_{\mathrm{h}}T_{\mathrm{c}}} > 0,
$$

由算术–几何平均不等式，只要 $T_{\mathrm{h}} \ne T_{\mathrm{c}}$ 就有 $\Delta S > 0$：有限温差下的传热总是不可逆的。

**例 2.3.3** 系统与初态同例 2.3.2，但把隔板换成一块导热的、可以无摩擦移动的理想活塞。求 $\Delta S$。

解：仍有 $Q = 0$、$W = 0$（以两种气体为系统，活塞是内部的），$\Delta U = 0$，理想气体的内能只依赖温度，所以 $T_2 = 262.5\,\mathrm{K}$ 与例 2.3.2 相同。不同的是终态两侧压力相等。总体积 $V = R(200 + 300)\,\mathrm{K}/p^\circ = 0.04157\,\mathrm{m^3}$，终态压力 $p_2 = 2RT_2/V = 105.0\,\mathrm{kPa}$。每种气体的 $p$、$V$、$T$ 都变了，由式 (2.5) 的第一种形式

$$
\begin{aligned}
\Delta S(\mathrm{He}) &= \tfrac{5}{2}R\ln\frac{262.5}{200} - R\ln\frac{105.0}{100} = 5.65 - 0.41 = 5.24\,\mathrm{J\,K^{-1}},\\
\Delta S(\ce{H2}) &= \tfrac{7}{2}R\ln\frac{262.5}{300} - R\ln\frac{105.0}{100} = -3.89 - 0.41 = -4.29\,\mathrm{J\,K^{-1}},
\end{aligned}
$$

$\Delta S = 0.96\,\mathrm{J\,K^{-1}}$，比例 2.3.2 多出来的部分来自压力不平衡推动的活塞运动这一不可逆过程。

### 2.3.4. 混合熵

不同气体的混合是不可逆过程，计算熵变同样要设计可逆途径（例如用只让一种气体透过的理想半透膜，[6.3.4](/6.3.4)）。理想气体混合物中，各组分的分子互不影响：每种气体的性质与它单独占据整个容器时相同，混合物的 $U$、$H$、$S$ 等广延性质（体积除外）都可以按组分加和。所以混合熵就是各组分从各自的初态单独变到它在混合物中的状态的熵变之和。在等温等压下混合时，组分 B 从压力 $p$ 变为分压 $p_{\mathrm{B}} = x_{\mathrm{B}}p$，$\Delta S_{\mathrm{B}} = n_{\mathrm{B}}R\ln(p/p_{\mathrm{B}}) = -n_{\mathrm{B}}R\ln x_{\mathrm{B}}$。

**定义 2.3.1（混合熵）** 由各自处于相同温度与压力的纯物质混合成混合物时系统的熵变称为**混合熵**，记作 $\Delta_{\mathrm{mix}}S$。对理想气体，

$$
\Delta_{\mathrm{mix}}S = -R\sum_{\mathrm{B}}n_{\mathrm{B}}\ln x_{\mathrm{B}}.
\tag{2.6}
$$

$x_{\mathrm{B}} < 1$，所以 $\Delta_{\mathrm{mix}}S > 0$。等物质的量的两种气体混合，每摩尔混合物 $\Delta_{\mathrm{mix}}S_{\mathrm{m}} = R\ln 2 = 5.76\,\mathrm{J\,mol^{-1}\,K^{-1}}$。式 (2.6) 的统计解释是：混合后每个分子可以出现的空间扩大了，微观态数增多（[5.2.4](/5.2.4#sec-4.8)）。它只与组成有关，与气体的种类无关；但两份相同的气体"混合"时熵变为零，因为抽去隔板前后系统的宏观状态并无区别（Gibbs 佯谬，它的解答在于全同粒子不可区分，见 [6.3.10](/6.3.10)）。同一公式也适用于理想液态混合物（[6.3.5](/6.3.5)）。

温度、压力不同的气体混合时，仍按组分分别计算：确定每种气体的终态（温度、它在混合物中的分压或占据的体积），各自按式 (2.5) 计算再相加。

**例 2.3.4** 系统与初态同例 2.3.2，把隔板直接抽走，求 $\Delta S$。

解：$Q = 0$、$W = 0$，$T_2 = 262.5\,\mathrm{K}$ 不变。He 从 $V_{\mathrm{He}} = R(200\,\mathrm{K})/p^\circ = 0.01663\,\mathrm{m^3}$ 扩展到整个容器 $V = 0.04157\,\mathrm{m^3}$，$\ce{H2}$ 从 $0.02494\,\mathrm{m^3}$ 扩展到 $V$。由式 (2.5) 的第二种形式

$$
\begin{aligned}
\Delta S &= \left(\tfrac{3}{2}R\ln\frac{262.5}{200} + R\ln\frac{0.04157}{0.01663}\right) + \left(\tfrac{5}{2}R\ln\frac{262.5}{300} + R\ln\frac{0.04157}{0.02494}\right)\\
&= (3.39 + 7.62) + (-2.78 + 4.25) = 12.48\,\mathrm{J\,K^{-1}}.
\end{aligned}
$$

其中 $0.62\,\mathrm{J\,K^{-1}}$ 来自传热（同例 2.3.2），$11.86\,\mathrm{J\,K^{-1}}$ 来自混合。

**例 2.3.5** $273.15\,\mathrm{K}$ 下，$2\,\mathrm{mol}$ $\ce{N2}$（$10^5\,\mathrm{Pa}$）与 $1\,\mathrm{mol}$ $\ce{O2}$（$10^4\,\mathrm{Pa}$）分装在容器两侧，抽去隔板等温混合。求 $\Delta S$。

解：$V(\ce{N2}) = 2RT/10^5\,\mathrm{Pa} = 0.0454\,\mathrm{m^3}$，$V(\ce{O2}) = RT/10^4\,\mathrm{Pa} = 0.2271\,\mathrm{m^3}$，总体积 $0.2725\,\mathrm{m^3}$。两种气体各自等温膨胀到总体积：

$$
\Delta S = 2R\ln\frac{0.2725}{0.0454} + R\ln\frac{0.2725}{0.2271} = 2R\ln 6 + R\ln 1.2 = 29.79 + 1.52 = 31.31\,\mathrm{J\,K^{-1}}.
$$

这里大部分熵变来自 $\ce{N2}$ 的膨胀而不是"混合"本身：两种气体初态压力不同，式 (2.6) 不能直接使用。

### 2.3.5. 相变的熵变

可逆相变在两相平衡的温度与压力下进行，一般 $W' = 0$，$Q_{\mathrm{r}} = Q_p = \Delta_{\mathrm{trs}}H$，所以

$$
\Delta_{\mathrm{trs}}S = \frac{\Delta_{\mathrm{trs}}H}{T_{\mathrm{trs}}},
$$

$\Delta_{\mathrm{trs}}H$ 是可逆**相变焓**，$T_{\mathrm{trs}}$ 是可逆相变温度。熔化、蒸发、升华都吸热，熵增加；正常沸点的摩尔蒸发熵对许多非极性液体约为 $85$–$88\,\mathrm{J\,mol^{-1}\,K^{-1}}$（**Trouton 规则**，[6.1.1](/6.1.1)）。不可逆相变的熵变要设计包含一步可逆相变的途径来计算。

**例 2.3.6** $273.15\,\mathrm{K}$ 时冰的摩尔熔化焓 $\Delta_{\mathrm{fus}}H_{\mathrm{m}} = 6.01\,\mathrm{kJ\,mol^{-1}}$，$263.15$–$273.15\,\mathrm{K}$ 之间 $\ce{H2O(l)}$ 与 $\ce{H2O(s)}$ 的 $C_{p,\mathrm{m}}$ 分别为 $75.3$ 与 $37.6\,\mathrm{J\,mol^{-1}\,K^{-1}}$。计算 $100\,\mathrm{kPa}$ 下 $1\,\mathrm{mol}$ 水在 (1) $273.15\,\mathrm{K}$、(2) $263.15\,\mathrm{K}$ 结冰的熵变，并判断过程 (2) 能否自发进行。

解：(1) 可逆相变：$\Delta S = -\Delta_{\mathrm{fus}}H_{\mathrm{m}}/T = -6010/273.15 = -22.0\,\mathrm{J\,K^{-1}}$。熵减小并不说明过程不能发生：系统不是孤立的，熵增加原理不能直接用于它；这是一个可逆过程，环境的熵增加 $22.0\,\mathrm{J\,K^{-1}}$，总熵变为零。

(2) 过冷水结冰是不可逆相变，设计途径：过冷水等压可逆升温到 $273.15\,\mathrm{K}$，可逆结冰，冰再等压可逆降温到 $263.15\,\mathrm{K}$。

$$
\Delta S_{\text{系统}} = 75.3\ln\frac{273.15}{263.15} - \frac{6010}{273.15} + 37.6\ln\frac{263.15}{273.15} = 2.81 - 22.00 - 1.40 = -20.6\,\mathrm{J\,K^{-1}}.
$$

判断方向要计算环境的熵变。实际过程在 $263.15\,\mathrm{K}$ 等压进行，系统放出的热是 $263.15\,\mathrm{K}$ 的凝固焓，由 Kirchhoff 定律（[6.3.1 定理 1.7.1](/6.3.1#thm-1.7.1)）

$$
\Delta H(263.15\,\mathrm{K}) = -6010 + (37.6 - 75.3)(263.15 - 273.15) = -5633\,\mathrm{J},
$$

由式 (2.4)，$\Delta S_{\text{环境}} = 5633/263.15 = 21.41\,\mathrm{J\,K^{-1}}$，

$$
\Delta S_{\text{孤立}} = -20.6 + 21.41 = +0.81\,\mathrm{J\,K^{-1}} > 0,
$$

过冷水结冰是自发的不可逆过程。系统的熵减小，但凝固放出的热使环境的熵增加得更多。也可以直接用 Clausius 不等式：$\Delta S = -20.6\,\mathrm{J\,K^{-1}} > Q/T_{\mathrm{sur}} = -21.41\,\mathrm{J\,K^{-1}}$，过程不可逆。

![Freezing of 1 mol of water at 100 kPa as a function of temperature: the entropy decrease of the water and the entropy increase of the surroundings nearly cancel; their sum is positive below 273.15 K (freezing is spontaneous) and negative above it (melting is spontaneous)](./plots/supercooled-freezing.py)

上图把例 2.3.6 推广到其他温度：$\Delta S_{\text{孤立}}$ 只在 $273.15\,\mathrm{K}$ 时为零，这正是两相平衡的温度；离平衡温度越远，结冰（或熔化）的推动力越大。$\Delta S_{\text{孤立}}$ 乘以 $-T$ 就是下一章的 $\Delta G$（[6.3.3](/6.3.3)）。

**例 2.3.7** $1\,\mathrm{mol}$ 水在正常沸点（$373.12\,\mathrm{K}$、$101.325\,\mathrm{kPa}$）向真空容器蒸发，终态为同温同压的水蒸气。求 $\Delta S$、$\Delta S_{\text{环境}}$，并判断过程能否自发。$\Delta_{\mathrm{vap}}H_{\mathrm{m}} = 40.65\,\mathrm{kJ\,mol^{-1}}$。

解：始态与终态与可逆相变相同，$\Delta S = 40650/373.12 = 108.95\,\mathrm{J\,K^{-1}}$。实际过程向真空蒸发，$W = 0$，$Q = \Delta U = \Delta H - \Delta(pV) \approx \Delta H - RT = 37.55\,\mathrm{kJ}$，

$$
\Delta S_{\text{环境}} = -\frac{37550}{373.12} = -100.63\,\mathrm{J\,K^{-1}}, \qquad \Delta S_{\text{孤立}} = 8.31\,\mathrm{J\,K^{-1}} > 0,
$$

过程自发。$\Delta S_{\text{孤立}}$ 恰好等于 $R$：与可逆蒸发相比，向真空蒸发少做了 $pV = RT$ 的功，少吸收了同样多的热。

## 2.4. 热力学第三定律与规定熵

化学反应的熵变 $\Delta_{\mathrm{r}}S_{\mathrm{m}} = \sum_{\mathrm{B}}\nu_{\mathrm{B}}S_{\mathrm{m}}(\mathrm{B})$ 需要各物质的熵值，而由式 (2.2) 只能得到熵的变化。反应物与产物由不同的物质组成，不能通过 $pVT$ 变化相互转换，所以需要为熵选定一个各物质共同的零点。这个零点由热力学第三定律给出。

### 2.4.1. Nernst 热定理与第三定律

1902 年 Richards 测定低温下一些原电池反应的电动势，发现温度降低时反应的 $\Delta G$ 与 $\Delta H$ 越来越接近。Nernst 由此在 1906 年提出：

**定理 2.4.1（Nernst 热定理）** 凝聚系统中进行的等温过程（包括化学反应），其熵变在温度趋于 $0\,\mathrm{K}$ 时趋于零：

$$
\lim_{T \to 0\,\mathrm{K}}(\Delta S)_T = 0.
$$

这说明 $0\,\mathrm{K}$ 时各种凝聚态物质的熵（相对于由相同元素组成的其他凝聚态物质）都相同。Planck 在 1911 年进一步假设：$0\,\mathrm{K}$ 时一切纯凝聚态物质的熵都等于零。这个假设有反例：甘油的玻璃态在 $0\,\mathrm{K}$ 附近的熵比晶体大约 $19\,\mathrm{J\,mol^{-1}\,K^{-1}}$，两者不可能都为零。1920 年 Lewis 与 Gibson 指出，Planck 的假设只适用于完美晶体。

**定义 2.4.1（完美晶体）** 原子或分子在晶格中只有一种有序排列方式的纯物质晶体称为**完美晶体**。

**定理 2.4.2（热力学第三定律）** $0\,\mathrm{K}$ 时，一切纯物质的完美晶体的熵都等于零：$\lim_{T \to 0\,\mathrm{K}}S(\text{完美晶体}) = 0$。

这就是**热力学第三定律**（[6.1.6 定理 6.4.1](/6.1.6#thm-6.4.1)）的 Planck–Lewis 表述。从统计观点看，完美晶体在 $0\,\mathrm{K}$ 时所有粒子都处于基态，只有一个微观态，$S = k_{\mathrm{B}}\ln 1 = 0$。玻璃态与含有无序排列的晶体（CO、$\ce{N2O}$、冰）在 $0\,\mathrm{K}$ 仍有一定的熵，称为**残余熵**（[6.3.11](/6.3.11)）。第三定律的另一种表述是"不可能用有限的步骤使物体冷却到 $0\,\mathrm{K}$"（绝对零度不能达到原理），两种表述在热力学中可以相互推出。

### 2.4.2. 规定熵与量热熵

**定义 2.4.2（规定熵）** 以 $0\,\mathrm{K}$ 完美晶体的熵为零，纯物质 B 在状态 $(T, p)$ 的熵，即 B 从 $0\,\mathrm{K}$ 的完美晶体变到该状态的熵变，称为 B 在该状态的**规定熵**（第三定律熵）：

$$
S_{\mathrm{B}}(T, p) = \Delta S_{\mathrm{B}}(0\,\mathrm{K},\ \text{完美晶体} \to T, p).
$$
由低温热容与相变焓的测量数据按这一途径计算得到的规定熵称为**量热熵**。$1\,\mathrm{mol}$ 物质在标准态下的规定熵就是**标准摩尔熵** $S^\circ_{\mathrm{m}}(T)$（[6.1.6 定义 6.4.2](/6.1.6#def-6.4.2)），各物质 $298.15\,\mathrm{K}$ 的值可以查表。

例如 $\ce{H2O(g)}$ 在 $423\,\mathrm{K}$ 的规定熵是下面一系列步骤的熵变之和：冰从 $0\,\mathrm{K}$ 加热到 $273.15\,\mathrm{K}$，熔化，液态水加热到正常沸点，汽化，水蒸气加热到 $423\,\mathrm{K}$：

$$
S_{\mathrm{m}}(T) = \int_0^{T_{\mathrm{fus}}}\frac{C_{p,\mathrm{m}}(\mathrm{s})}{T}\,\mathrm{d}T + \frac{\Delta_{\mathrm{fus}}H_{\mathrm{m}}}{T_{\mathrm{fus}}} + \int_{T_{\mathrm{fus}}}^{T_{\mathrm{b}}}\frac{C_{p,\mathrm{m}}(\mathrm{l})}{T}\,\mathrm{d}T + \frac{\Delta_{\mathrm{vap}}H_{\mathrm{m}}}{T_{\mathrm{b}}} + \int_{T_{\mathrm{b}}}^{T}\frac{C_{p,\mathrm{m}}(\mathrm{g})}{T}\,\mathrm{d}T.
\tag{2.7}
$$

固态如有晶型转变，还要加上相应的相变熵。式 (2.7) 中的积分要用实测的热容数据数值计算：以前在 $C_{p,\mathrm{m}}/T$–$T$ 图上求面积（图解积分），现在直接对数据插值后用梯形公式或 Simpson 公式积分（`scipy.integrate`，[4.4.4](/4.4.4)）。

$20\,\mathrm{K}$ 以下晶体的热容很难测准，需要外推。低温下非金属晶体的热容服从 Debye T³ 定律（Debye T³ law）：

$$
C_{V,\mathrm{m}} = \frac{12\pi^4}{5}R\left(\frac{T}{\Theta_{\mathrm{D}}}\right)^3 = aT^3 \qquad (T \ll \Theta_{\mathrm{D}}),
$$

$\Theta_{\mathrm{D}}$ 是晶体的 Debye 温度，$a$ 是晶体的特性参数（金属还要加上电子的贡献 $\gamma_{\mathrm{e}}T$）。低温下固体的 $C_p \approx C_V$。若最低的测量温度为 $T^*$，$0$–$T^*$ 段的熵为

$$
S_{\mathrm{m}}(T^*) = \int_0^{T^*}\frac{aT^3}{T}\,\mathrm{d}T = \frac{aT^{*3}}{3} = \frac{C_{p,\mathrm{m}}(T^*)}{3},
$$

只需测出 $T^*$ 处的热容，不必知道 $\Theta_{\mathrm{D}}$。

**例 2.4.1** 估算水蒸气在 $423.15\,\mathrm{K}$、$101.325\,\mathrm{kPa}$ 下的量热熵。

解：冰的低温热容积分（数值计算，$10\,\mathrm{K}$ 以下按 $T^3$ 外推）给出 $S_{\mathrm{m}}(\text{冰}, 273.15\,\mathrm{K}) = 38.1\,\mathrm{J\,mol^{-1}\,K^{-1}}$；熔化 $+6010/273.15 = 22.0$；液态水从 $273.15$ 到 $373.12\,\mathrm{K}$（$C_{p,\mathrm{m}} = 75.3$）$+23.5$；汽化 $+40650/373.12 = 108.9$；水蒸气从 $373.12$ 到 $423.15\,\mathrm{K}$（$C_{p,\mathrm{m}} \approx 33.8$）$+4.3$。合计 $S_{\mathrm{m}} \approx 196.8\,\mathrm{J\,mol^{-1}\,K^{-1}}$；换算到标准压力再加 $R\ln(101.325/100) = 0.11$。汽化一项占总熵的一半以上：气体的熵远大于凝聚相。

![Calorimetric entropy of water from 0 K to 423 K (approximate heat capacities). Upper panel: Cp,m/T, whose area gives the heating contributions; lower panel: Sm(T), with jumps of ΔfusH/Tfus at the melting point and ΔvapH/Tb at the boiling point](./plots/water-entropy.py)

由光谱数据与统计热力学算出的 $\ce{H2O(g)}$ 的熵（约 $200.7\,\mathrm{J\,mol^{-1}\,K^{-1}}$，$423\,\mathrm{K}$）比上面的量热熵大 $3$–$4\,\mathrm{J\,mol^{-1}\,K^{-1}}$。差别主要来自冰中氢原子位置的无序：冰不是完美晶体，$0\,\mathrm{K}$ 时仍有约 $R\ln\frac{3}{2} = 3.4\,\mathrm{J\,mol^{-1}\,K^{-1}}$ 的残余熵（Pauling 1935），量热法测不到这一部分。热力学数据表中的 $S^\circ_{\mathrm{m}}$ 已经计入了它（[6.3.11](/6.3.11)）。

### 2.4.3. 化学反应的熵变

$298.15\,\mathrm{K}$、各物质处于标准态时，由标准摩尔熵直接计算（[6.1.6](/6.1.6#sec-6.4.5)）：

$$
\Delta_{\mathrm{r}}S^\circ_{\mathrm{m}}(298.15\,\mathrm{K}) = \sum_{\mathrm{B}}\nu_{\mathrm{B}}S^\circ_{\mathrm{m}}(\mathrm{B}, 298.15\,\mathrm{K}).
$$

这里与反应焓一样采用"反应进行到底、反应物与产物互不混合"的反应模型。其他温度的反应熵变，与 Kirchhoff 定律同样地设计途径：反应物从 $T$ 变到 $298.15\,\mathrm{K}$，反应，产物再变回 $T$。在 $298.15\,\mathrm{K}$–$T$ 之间各物质无相变时，

$$
\Delta_{\mathrm{r}}S^\circ_{\mathrm{m}}(T) = \Delta_{\mathrm{r}}S^\circ_{\mathrm{m}}(298.15\,\mathrm{K}) + \int_{298.15\,\mathrm{K}}^{T}\frac{\Delta_{\mathrm{r}}C^\circ_{p,\mathrm{m}}}{T}\,\mathrm{d}T,
\qquad
\left(\frac{\partial\Delta_{\mathrm{r}}S^\circ_{\mathrm{m}}}{\partial T}\right)_p = \frac{\Delta_{\mathrm{r}}C^\circ_{p,\mathrm{m}}}{T}.
\tag{2.8}
$$

有相变时分段积分并加上相变熵；非标准压力时再计入压力对熵的影响（对理想气体 $-R\ln(p/p^\circ)$）。由 Kirchhoff 定律与式 (2.8)，若在一定温度范围内 $\Delta_{\mathrm{r}}C_{p,\mathrm{m}} = 0$，则 $\Delta_{\mathrm{r}}H^\circ_{\mathrm{m}}$ 与 $\Delta_{\mathrm{r}}S^\circ_{\mathrm{m}}$ 都与温度无关，$\Delta_{\mathrm{r}}G^\circ_{\mathrm{m}} = \Delta_{\mathrm{r}}H^\circ_{\mathrm{m}} - T\Delta_{\mathrm{r}}S^\circ_{\mathrm{m}}$ 则是温度的线性函数。

**例 2.4.2** 合成氨 $\ce{N2(g) + 3H2(g) -> 2NH3(g)}$ 的 $\Delta_{\mathrm{r}}S^\circ_{\mathrm{m}}(298.15\,\mathrm{K}) = 2(192.8) - 191.6 - 3(130.7) = -198.1\,\mathrm{J\,mol^{-1}\,K^{-1}}$。用 [6.3.1](/6.3.1#sec-1.3.2) 表中的热容参数求 $723\,\mathrm{K}$ 的值。

解：$\Delta_{\mathrm{r}}C^\circ_{p,\mathrm{m}} = \Delta a + \Delta b\,T + \Delta c'/T^2$，$\Delta a = -50.92$，$\Delta b = 36.65 \times 10^{-3}$，$\Delta c' = -4.10 \times 10^5$（[6.3.1 例 1.7.1](/6.3.1#sec-1.7.3)）。

$$
\int_{298.15}^{723}\frac{\Delta_{\mathrm{r}}C^\circ_{p,\mathrm{m}}}{T}\,\mathrm{d}T = \Delta a\ln\frac{723}{298.15} + \Delta b(723 - 298.15) - \frac{\Delta c'}{2}\left(\frac{1}{723^2} - \frac{1}{298.15^2}\right) = -31.4\,\mathrm{J\,mol^{-1}\,K^{-1}},
$$

$\Delta_{\mathrm{r}}S^\circ_{\mathrm{m}}(723\,\mathrm{K}) = -229.5\,\mathrm{J\,mol^{-1}\,K^{-1}}$。熵减小，高温不利于合成氨；与例 1.7.1 的 $\Delta_{\mathrm{r}}H^\circ_{\mathrm{m}}(723\,\mathrm{K})$ 一起，可以算出这一温度的平衡常数（[6.3.7](/6.3.7)）。

## 2.5. 熵与能量退降

第一定律说，一个实际过程发生后能量的总值不变；第二定律说，一个不可逆过程发生后熵的总值增加。能量的总量没有变，熵的增加却使其中一部分能量失去了做功的能力，这称为**能量退降**（[5.2.4](/5.2.4#sec-4.10)）。

设有三个热源，$T_{\mathrm{A}} > T_{\mathrm{B}} > T_{\mathrm{C}}$，$T_{\mathrm{C}}$ 是可用的最低温度（环境）。热量 $Q$ 在 $T_{\mathrm{A}}$ 热源中时，用可逆热机在 $T_{\mathrm{A}}$ 与 $T_{\mathrm{C}}$ 之间工作，最多能得到功 $W_1 = Q(1 - T_{\mathrm{C}}/T_{\mathrm{A}})$。若先让 $Q$ 不可逆地从 $T_{\mathrm{A}}$ 传到 $T_{\mathrm{B}}$，再在 $T_{\mathrm{B}}$ 与 $T_{\mathrm{C}}$ 之间利用，最多只能得到 $W_2 = Q(1 - T_{\mathrm{C}}/T_{\mathrm{B}})$。两者之差

$$
W_1 - W_2 = T_{\mathrm{C}}\left(\frac{Q}{T_{\mathrm{B}}} - \frac{Q}{T_{\mathrm{A}}}\right) = T_{\mathrm{C}}\,\Delta S_{\text{孤立}} > 0,
$$

其中 $Q/T_{\mathrm{B}} - Q/T_{\mathrm{A}}$ 正是这次不可逆传热引起的总熵变。这个结果是普遍的：不可逆过程使孤立系统的熵增加 $\Delta S_{\text{孤立}}$，就有 $T_0\Delta S_{\text{孤立}}$ 的能量从可以做功的形式变成不能做功的形式（$T_0$ 为环境温度，[5.2.4 公式 4.10.1](/5.2.4#sec-4.10)）。由此可以说，孤立系统的熵变是其能量不可利用程度的量度。

能量因此有"品质"之分：功是品质最高的能量，可以无条件地全部变成热；热的品质随温度降低而下降，同样数量的热，温度越高，能转化为功的部分越多。自然界的实际过程总是朝着能量品质降低的方向进行，"能源危机"说的正是可用能量的减少，而不是能量总量的减少。

熵判据在原则上解决了过程方向的问题，但使用起来有三点不便：用 Clausius 不等式需要同时计算 $\Delta S$ 与热温商；熵增加原理只适用于绝热或孤立系统；把系统与环境合成大孤立系统，有时所答非所问——例如电解水，把电源也划入大孤立系统后得到的结论是"整个过程自发"，却不能直接回答"水能否自己分解"。化学中的过程大多在等温等容或等温等压下进行，下一章（[6.3.3](/6.3.3)）由 Clausius 不等式导出只用系统自身性质表示的 Helmholtz 自由能与 Gibbs 自由能判据。

最后，熵增加原理只对孤立系统成立；对一般的系统，可以把熵的变化分成两部分：与环境交换能量和物质带来的熵流，以及系统内部的不可逆过程产生的熵，前者可正可负，后者永不为负。只要从环境流入的"负熵"足够多，开放系统的熵就可以减少，系统可以自发地从无序走向有序。生物体正是这样的开放系统：它摄入低熵的食物（或吸收太阳光），排出高熵的废物与热，维持并发展高度有序的结构，即 Schrödinger 所说的"生命以负熵为食"。化学振荡、Turing 斑图等远离平衡的有序结构也属于这一类。这些内容构成非平衡态热力学，在学过化学动力学之后于 [6.3.18](/6.3.18) 系统讨论。

## 小结

| 过程 | 熵变 | 条件 |
|---|---|---|
| 理想气体等温 | $nR\ln(V_2/V_1) = nR\ln(p_1/p_2)$ | 可逆与否均可 |
| 等容、等压变温 | $\int C_V\,\mathrm{d}T/T$，$\int C_p\,\mathrm{d}T/T$ | 无相变与反应 |
| 理想气体 $pVT$ 变化 | 式 (2.5) | $C_{V,\mathrm{m}}$ 为常数 |
| 理想气体等温等压混合 | $-R\sum n_{\mathrm{B}}\ln x_{\mathrm{B}}$ | 不同气体 |
| 可逆相变 | $\Delta_{\mathrm{trs}}H/T_{\mathrm{trs}}$ | 两相平衡的 $T$、$p$ |
| 环境 | $-Q_{\text{系统}}/T_{\mathrm{sur}}$ | 环境为大热源，$Q$ 为实际热 |
| 反应 | $\sum\nu_{\mathrm{B}}S^\circ_{\mathrm{m}}(\mathrm{B})$，温度校正用式 (2.8) | 反应模型，无相变 |

## 思考题

1. 判断正误：(A) 自发过程都是不可逆过程；(B) 不可逆过程都是自发过程；(C) 功可以全部变为热，但热不能全部变为功；(D) 系统在自发过程中的熵变都大于零；(E) 绝热可逆过程是等熵过程。
   答：A、E 正确。B 错：环境做功推动的不可逆压缩就不是自发的。C 错：热可以全部变为功，但必然引起其他变化（如理想气体等温膨胀）。D 错：只有孤立系统的熵在自发过程中必定增加，例 2.3.6 中过冷水结冰自发，系统的熵却减小。
2. 有人说："氢气与氧气在室温下化合成水是自发过程，所以 $\Delta S > Q/T$；那么室温下电解水就是 $\Delta S < Q/T$。"对吗？
   答：不对。Clausius 不等式对一切实际（不可逆）过程都给出 $\Delta S > Q/T_{\mathrm{sur}}$，电解水虽然要靠外界做电功才能进行，它仍是不可逆过程，$\Delta S > Q/T_{\mathrm{sur}}$。$\Delta S < Q/T_{\mathrm{sur}}$ 的过程不可能发生。
3. 判断正误：(A) 在一定温度范围内，若某反应的 $\Delta_{\mathrm{r}}H^\circ_{\mathrm{m}}$ 与温度无关，则 $\Delta_{\mathrm{r}}S^\circ_{\mathrm{m}}$ 也与温度无关；(B) 系统从始态到终态，只有经过可逆过程才有熵变；(C) 第三定律说 $0\,\mathrm{K}$ 时任何晶体的熵都等于零。
   答：A 正确（两者都由 $\Delta_{\mathrm{r}}C_{p,\mathrm{m}} = 0$ 保证）。B 错：熵是状态函数，任何过程都有熵变，只是要沿可逆途径计算。C 错：只适用于完美晶体。
4. 绝热容器中用固定的绝热隔板隔开 $1\,\mathrm{mol}$ He（$400\,\mathrm{K}$，$5p^\circ$）与 $1\,\mathrm{mol}$ $\ce{H2}$（$200\,\mathrm{K}$，$10p^\circ$），抽去隔板后求终态温度、$\Delta S$ 与 $\Delta H$。
   答：$\Delta U = 0$ 给出 $T = 275\,\mathrm{K}$。初始体积之比 $V_{\mathrm{He}} : V_{\ce{H2}} = 4 : 1$，各自扩展到总体积：$\Delta S(\mathrm{He}) = \frac{3}{2}R\ln\frac{275}{400} + R\ln\frac{1}{0.8} = -2.82\,\mathrm{J\,K^{-1}}$，$\Delta S(\ce{H2}) = \frac{5}{2}R\ln\frac{275}{200} + R\ln\frac{1}{0.2} = 20.00\,\mathrm{J\,K^{-1}}$，$\Delta S = 17.18\,\mathrm{J\,K^{-1}}$；$\Delta H = \frac{5}{2}R(275 - 400) + \frac{7}{2}R(275 - 200) = -415.7\,\mathrm{J}$。
