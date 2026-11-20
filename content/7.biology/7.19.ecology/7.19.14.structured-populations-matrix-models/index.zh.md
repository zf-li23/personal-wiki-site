---
title: 结构化种群：矩阵模型
description: 年龄与阶段结构种群的种群投影矩阵：Leslie 矩阵与 Lefkovitch 矩阵、生活周期图、含证明的 Perron–Frobenius 定理、稳定阶段分布、繁殖价值与阻尼比；含推导的敏感度与弹性分析；虎鲸、蠵龟与 royal catchfly；瞬变动态、McKendrick–von Foerster 方程与积分投影模型。
source_hash: 010d14a6bdd7
---

不同年龄、大小或阶段的个体对种群增长的贡献各不相同：土壤中的种子、莲座丛植株和开花植株面临不同的风险，产生的后代数也不同。像 [7.19.10](/7.19.10)–[7.19.13](/7.19.13) 的模型那样只数总数，就把这些信息丢掉了。矩阵种群模型保留了这些信息，对于生活周期可以用少数几个类别描述的生物，它是保护与害虫管理的主要定量工具。本章从最简单的例子，即 Fibonacci 的兔子出发，经由 [7.10.15](/7.10.15) 的 **Leslie 矩阵**，建立一般的阶段分类矩阵；证明支配其长期行为的 Perron–Frobenius 定理；推导增长率的敏感度与弹性，告诉管理者应当在生活周期的哪个环节干预；并把这些结果应用于虎鲸、蠵龟和一种草原植物。最后一节讨论瞬变动态，以及同一思想的连续年龄（McKendrick–von Foerster）与连续大小（积分投影）版本。所用的线性代数见 [2.1.6](/2.1.6)；同样的量在演化上的解释（适合度、选择的力度）见 [7.10.15](/7.10.15)，用于生存力分析的这些模型的随机版本见 [7.19.15](/7.19.15)。

## 14.1. 从 Fibonacci 到年龄结构

Fibonacci 的兔子问题（1202）是最早的年龄结构种群模型。每对成年兔每月生一对小兔；小兔一个月后成熟；没有兔子死亡。设 $A_t$ 与 $J_t$ 为第 $t$ 月成年与幼年兔的对数，则 $A_{t+1} = A_t + J_t$，$J_{t+1} = A_t$，写成矩阵形式为

$$
\boldsymbol{n}(t + 1) = \begin{bmatrix} 1 & 1 \\ 1 & 0 \end{bmatrix}\boldsymbol{n}(t), \qquad \boldsymbol{n}(t) = \begin{bmatrix} A_t \\ J_t \end{bmatrix}.
$$
总数 $F_t = A_t + J_t$ 满足 $F_{t+1} = F_t + F_{t-1}$，即 Fibonacci 递推。该矩阵的特征方程为 $\lambda^2 - \lambda - 1 = 0$，根为 $\lambda_1 = (1 + \sqrt5)/2 \approx 1.618$ 与 $\lambda_2 = (1 - \sqrt5)/2 \approx -0.618$。把 $\boldsymbol{n}(0)$ 写在**特征向量**的基下，$\boldsymbol{n}(t) = c_1\lambda_1^t\boldsymbol{w}_1 + c_2\lambda_2^t\boldsymbol{w}_2$，由于 $\lvert\lambda_2\rvert < \lambda_1$，第二项可以忽略：种群以黄金分割比 $\lambda_1$ 的速率几何增长，成年与幼年之比趋近特征向量 $\boldsymbol{w}_1 = (\lambda_1, 1)^{\mathsf T}$ 的比值，也是黄金分割比。左特征向量 $\boldsymbol{v}_1^{\mathsf T} = (\lambda_1, 1)$ 表明，一对成年兔对未来增长的价值相当于 $\lambda_1$ 对幼年兔，因为它早一个月繁殖。增长率、稳定结构和各类别的相对价值：主特征值及其左右特征向量这三个量，是每个矩阵模型都给出的结果。

## 14.2. 投影矩阵

### 14.2.1. 年龄与阶段分类的模型

Leslie 矩阵（Leslie 1945；[定义 15.1.5](/7.10.15#def-15.1.5)，见 7.10.15）按年龄分类个体：每个时间步长内每个幸存者进入下一个年龄类，所以仅有的非零元是第一行的繁殖力与次对角线上的存活概率。对许多生物，年龄并不能很好地预测其命运。同龄的树木大小相差悬殊；海龟的存活机会取决于它是幼体、亚成体还是成体；多年生植物可以连续数年保持为莲座丛。Lefkovitch（1965）把 Leslie 矩阵推广到按阶段或大小定义的类别，其中个体可以停留在原类、前进、跳过某些类，甚至退回。

**定义 14.2.1（种群投影矩阵）** 对分成 $s$ 个类的种群，**种群投影矩阵**是一个非负的 $s \times s$ 矩阵 $A = (a_{ij})$，使得相继普查时各类个体数的向量 $\boldsymbol{n}(t)$ 满足

$$
\boldsymbol{n}(t + 1) = A\boldsymbol{n}(t), \qquad \text{所以} \qquad \boldsymbol{n}(t) = A^t\boldsymbol{n}(0).
\tag{14.1}
$$
元素 $a_{ij}$ 是每个时刻 $t$ 的第 $j$ 类个体在时刻 $t + 1$ 产生的第 $i$ 类个体的期望数：它是存活或转移概率（至多为 1）、繁殖力，或二者之和。按年龄分类的矩阵是 Leslie 矩阵；按阶段或大小分类的矩阵是 **Lefkovitch 矩阵**。$A$ 的**生活周期图**是这样的有向图：每个类对应一个顶点，每个 $a_{ij} > 0$ 对应一条标为 $a_{ij}$ 的弧 $j \to i$。

阶段分类矩阵的典型元素有 $P_i$（存活并留在第 $i$ 类，位于对角线上）、$G_i$（存活并长到第 $i + 1$ 类，位于次对角线上）和 $F_i$（繁殖力，位于第一行）。若 $\sigma_i$ 为第 $i$ 类的年存活率，$\gamma_i$ 为幸存者晋级的概率，则 $P_i = \sigma_i(1 - \gamma_i)$，$G_i = \sigma_i\gamma_i$；对于在稳定种群中持续固定 $T_i$ 年的阶段，常用近似 $\gamma_i = 1/T_i$。繁殖力取决于普查的时机：在繁殖刚结束后普查（如 [7.10.15](/7.10.15)），$F_i$ 是第 $i$ 类亲体存活到下一个繁殖季的概率乘以其后代数；在繁殖前普查，则是后代数乘以后代存活到下次普查的概率。这些约定不改变 $\lambda$，但会改变特征向量，混淆它们是构建矩阵模型时最常见的错误。

矩阵模型与 [7.19.10](/7.19.10) 的指数模型作同样的假定：生命率恒定（无**密度制约**，无环境变异），同一类中的个体相同，且只模拟雌性（或固定的性比）。它们是对现状持续下去会发生什么的投影，而不是预测（Caswell 把 $\lambda$ 比作速度计的读数）。其力量在于比较不同的条件、种群与管理方案。

**例 14.2.1（常驻型虎鲸）** 不列颠哥伦比亚与华盛顿沿海的常驻型虎鲸（*Orcinus orca*）生活在稳定的母系群中，可以通过照片逐头识别，所以自 1973 年以来一直在追踪其种群统计。Brault 与 Caswell（1993）把雌鲸分成当岁幼鲸、未成熟的幼体（已过第一年但尚未成熟）、繁殖成体与繁殖后成体，并由 1973–1987 年的普查估计出矩阵

$$
A = \begin{bmatrix}
0 & 0.0043 & 0.1132 & 0 \\
0.9775 & 0.9111 & 0 & 0 \\
0 & 0.0736 & 0.9534 & 0 \\
0 & 0 & 0.0452 & 0.9804
\end{bmatrix}.
$$
幼体每年以概率 $0.9111$ 仍为幼体，以概率 $0.0736$ 成熟（平均幼体期约 13 年）；繁殖雌鲸每年产 $0.1132$ 头雌性当岁幼鲸（每四到五年一头幼崽，一半为雌性），并以每年 $0.0452$ 的概率停止繁殖；繁殖后的雌鲸以 $0.9804$ 的概率存活。幼体的小繁殖力代表当年成熟并繁殖的雌鲸。

:::

![Brault 与 Caswell（1993）虎鲸模型的生活周期图。每个箭头 j → i 对应矩阵的一个非零元 a_ij：环为存活并留在某阶段的概率，向前的箭头为存活并成熟的概率，回到阶段 1 的箭头（红色）为繁殖力。没有箭头从阶段 4 回到其他阶段，所以阶段 4 对增长没有贡献](./plots/killer-whale-life-cycle.py)

### 14.2.2. 不可约性与本原性

生活周期图的两个性质控制着长期行为。若其生活周期图是强连通的，即每一类都能对其他每一类贡献后代，则矩阵 $A$ 是*不可约*的；多数没有繁殖后类别的生活周期都如此。不可约矩阵若再满足其图中各圈长度的最大公约数为 1，则是*本原*的。自环的长度为 1，所以任何对角元为正的不可约矩阵都是本原的。对 Leslie 矩阵（无自环），每个 $F_x > 0$ 闭合一个长度为 $x + 1$ 的圈 $0 \to 1 \to \cdots \to x \to 0$，当发生繁殖的年龄的最大公约数为 1（例如有两个相继的繁殖年龄）时，该矩阵是本原的（[定理 15.1.1](/7.10.15#thm-15.1.1)，见 7.10.15）。等价地，非负矩阵是本原的当且仅当某个幂 $A^k$ 严格为正，此时当 $k = s^2 - 2s + 2$ 时已有 $A^k > 0$（Wielandt）。

虎鲸矩阵是可约的，因为阶段 4 无法到达其他阶段。其动态由阶段 1–3 构成的块决定，该块不可约，并且因有自环而是本原的；阶段 4 只是积累阶段 3 的幸存者。

## 14.3. 长期行为

### 14.3.1. Perron–Frobenius 定理

对可对角化的 $A$，式 (14.1) 的通解为 $\boldsymbol{n}(t) = \sum_k c_k\lambda_k^t\boldsymbol{w}_k$，$\lvert\lambda_k\rvert$ 最大的项最终占主导（[2.1.6](/2.1.6)）。对一般矩阵，主特征值可能是复数或负数，或者有几个特征值的模同样最大，主特征向量也可能有负分量，这对种群毫无意义。Perron–Frobenius 定理排除了非负矩阵的这些情形。它对不可约矩阵的形式已在 [1.4.7](/1.4.7#thm-7.6.1) 中陈述；这里需要本原矩阵的较强形式，并给出证明。

**定理 14.3.1（本原矩阵的 Perron–Frobenius 定理）** 设 $A \ge 0$ 为 $s \times s$ 本原矩阵，则：

1. $A$ 有一个等于其**谱半径**的实特征值 $\lambda_1 > 0$，其右特征向量 $\boldsymbol{w} > 0$，左特征向量 $\boldsymbol{v} > 0$（所有分量严格为正）；
2. $\lambda_1$ 是代数单根，且对每个其他特征值 $\lambda$ 有 $\lambda_1 > \lvert\lambda\rvert$；
3. 没有其他特征值有非负的特征向量。

若 $A$ 不可约但不本原，则 1 与 3 仍成立且 $\lambda_1$ 是单根，但有 $h > 1$ 个特征值的模等于 $\lambda_1$，即 $\lambda_1\mathrm{e}^{2\pi\mathrm{i}k/h}$，$k = 0, \dots, h - 1$，其中 $h$ 是各圈长度的最大公约数。

**证明** 先对严格正的矩阵 $A > 0$ 证明 1–3，再把本原的情形化归于它。

*存在性。* 令 $S = \{\boldsymbol{x} \ge 0 : \sum_ix_i = 1\}$。映射 $f(\boldsymbol{x}) = A\boldsymbol{x}/\sum_i(A\boldsymbol{x})_i$ 是 $S$ 到 $S$ 的连续映射（因为 $A > 0$，分母为正），由 Brouwer 不动点定理它有不动点 $\boldsymbol{w}$：$A\boldsymbol{w} = \lambda_1\boldsymbol{w}$，其中 $\lambda_1 = \sum_i(A\boldsymbol{w})_i > 0$，且 $\boldsymbol{w} = A\boldsymbol{w}/\lambda_1 > 0$。对 $A^{\mathsf T}$ 作同样的论证，得到 $\boldsymbol{v} > 0$ 与 $\mu > 0$ 使 $\boldsymbol{v}^{\mathsf T}A = \mu\boldsymbol{v}^{\mathsf T}$；于是 $\mu\boldsymbol{v}^{\mathsf T}\boldsymbol{w} = \boldsymbol{v}^{\mathsf T}A\boldsymbol{w} = \lambda_1\boldsymbol{v}^{\mathsf T}\boldsymbol{w}$，而 $\boldsymbol{v}^{\mathsf T}\boldsymbol{w} > 0$，所以 $\mu = \lambda_1$。

*主导性。* 设 $A\boldsymbol{y} = \lambda\boldsymbol{y}$，$\boldsymbol{y} \ne \boldsymbol{0}$，并以 $\lvert\boldsymbol{y}\rvert$ 记模构成的向量。由三角不等式，逐分量有 $\lvert\lambda\rvert\,\lvert\boldsymbol{y}\rvert = \lvert A\boldsymbol{y}\rvert \le A\lvert\boldsymbol{y}\rvert$。左乘 $\boldsymbol{v}^{\mathsf T} > 0$ 得 $\lvert\lambda\rvert\,\boldsymbol{v}^{\mathsf T}\lvert\boldsymbol{y}\rvert \le \lambda_1\boldsymbol{v}^{\mathsf T}\lvert\boldsymbol{y}\rvert$，所以 $\lvert\lambda\rvert \le \lambda_1$，$\lambda_1$ 就是谱半径。若 $\lvert\lambda\rvert = \lambda_1$，则非负向量 $A\lvert\boldsymbol{y}\rvert - \lambda_1\lvert\boldsymbol{y}\rvert$ 满足 $\boldsymbol{v}^{\mathsf T}(A\lvert\boldsymbol{y}\rvert - \lambda_1\lvert\boldsymbol{y}\rvert) = 0$，因而为零；于是对每个 $i$ 有 $\lvert\sum_ja_{ij}y_j\rvert = \sum_ja_{ij}\lvert y_j\rvert$，而所有 $a_{ij} > 0$，三角不等式中的这一等号迫使所有 $y_j$ 有相同的辐角：$\boldsymbol{y} = \mathrm{e}^{\mathrm{i}\phi}\lvert\boldsymbol{y}\rvert$。于是 $\lambda\lvert\boldsymbol{y}\rvert = A\lvert\boldsymbol{y}\rvert = \lambda_1\lvert\boldsymbol{y}\rvert$，所以 $\lambda = \lambda_1$。

*单性。* 若 $A\boldsymbol{y} = \lambda_1\boldsymbol{y}$，$\boldsymbol{y}$ 为实向量且不是 $\boldsymbol{w}$ 的倍数，选取 $\varepsilon$ 使 $\boldsymbol{z} = \boldsymbol{w} - \varepsilon\boldsymbol{y} \ge 0$ 有一个零分量但 $\boldsymbol{z} \ne \boldsymbol{0}$。由于 $A > 0$，$\boldsymbol{z} = A\boldsymbol{z}/\lambda_1 > 0$，矛盾；所以特征空间是一维的。若有 Jordan 块，则需要 $\boldsymbol{u}$ 使 $(A - \lambda_1I)\boldsymbol{u} = \boldsymbol{w}$；左乘 $\boldsymbol{v}^{\mathsf T}$ 得 $0 = \boldsymbol{v}^{\mathsf T}\boldsymbol{w} > 0$，不可能。因此 $\lambda_1$ 是代数单根。

*没有其他非负特征向量。* 若 $A\boldsymbol{y} = \lambda\boldsymbol{y}$，$\boldsymbol{y} \ge 0$，$\boldsymbol{y} \ne \boldsymbol{0}$，则 $\lambda\boldsymbol{v}^{\mathsf T}\boldsymbol{y} = \lambda_1\boldsymbol{v}^{\mathsf T}\boldsymbol{y}$ 且 $\boldsymbol{v}^{\mathsf T}\boldsymbol{y} > 0$，所以 $\lambda = \lambda_1$。

*本原矩阵。* 若 $A$ 本原，则对某个 $k$ 有 $B = A^k > 0$。$B$ 的特征值是 $A$ 的特征值的 $k$ 次幂，特征向量相同。设 $\boldsymbol{w} > 0$ 为 $B$ 的 Perron 向量，特征值为 $\rho(B)$。由于 $A$ 与 $B$ 可交换，$A\boldsymbol{w}$ 也是 $B$ 对应 $\rho(B)$ 的特征向量（或为零），所以由单性，对某个 $\lambda_1$ 有 $A\boldsymbol{w} = \lambda_1\boldsymbol{w}$；因为 $A \ge 0$，$\boldsymbol{w} > 0$，且 $A$ 没有零列（它不可约），所以 $\lambda_1 > 0$，且 $\lambda_1^k = \rho(B)$。$A$ 的每个其他特征值 $\lambda$ 满足 $\lvert\lambda\rvert^k = \lvert\lambda^k\rvert < \rho(B)$，除非 $\lambda^k = \rho(B)$，此时其特征向量是 $\boldsymbol{w}$ 的倍数，这迫使 $\lambda = \lambda_1$。代数单性也同样传递，因为 $A$ 对应 $\lambda_1$ 的 Jordan 块会给出 $B$ 对应 $\rho(B)$ 的 Jordan 块。左特征向量由 $A^{\mathsf T}$ 得到，3 随之同前。非本原矩阵的结论在关于非负矩阵的著作中证明（Seneta 2006），下文不用。$\square$

**定理 14.3.2（强遍历定理）** 设 $A$ 本原，主特征值为 $\lambda_1$，正特征向量为 $\boldsymbol{w}$、$\boldsymbol{v}$，则对每个初始向量 $\boldsymbol{n}(0) \ge 0$，

$$
\lim_{t\to\infty}\frac{\boldsymbol{n}(t)}{\lambda_1^t} = \frac{\boldsymbol{v}^{\mathsf T}\boldsymbol{n}(0)}{\boldsymbol{v}^{\mathsf T}\boldsymbol{w}}\,\boldsymbol{w}.
\tag{14.2}
$$
特别地，无论初始结构如何（只要 $\boldsymbol{n}(0) \ne \boldsymbol{0}$），比例 $\boldsymbol{n}(t)/\sum_in_i(t)$ 都收敛到 $\boldsymbol{w}/\sum_iw_i$，误差以 $(\lvert\lambda_2\rvert/\lambda_1)^t$ 的速度衰减，其中 $\lambda_2$ 是模第二大的特征值。

**证明** 空间 $\mathbb{R}^s$ 是由 $\boldsymbol{w}$ 张成的直线与子空间 $U = \{\boldsymbol{x} : \boldsymbol{v}^{\mathsf T}\boldsymbol{x} = 0\}$ 的直和，两者在 $A$ 下都不变（若 $\boldsymbol{v}^{\mathsf T}\boldsymbol{x} = 0$，则 $\boldsymbol{v}^{\mathsf T}A\boldsymbol{x} = \lambda_1\boldsymbol{v}^{\mathsf T}\boldsymbol{x} = 0$）。写 $\boldsymbol{n}(0) = c\boldsymbol{w} + \boldsymbol{u}$，其中 $c = \boldsymbol{v}^{\mathsf T}\boldsymbol{n}(0)/\boldsymbol{v}^{\mathsf T}\boldsymbol{w}$，$\boldsymbol{u} \in U$。$A$ 限制在 $U$ 上的特征值是除 $\lambda_1$ 之外的特征值（因为 $\lambda_1$ 是单根），它们的模至多为 $\lvert\lambda_2\rvert < \lambda_1$。因此对任意 $\varepsilon > 0$ 有 $\lVert A^t\boldsymbol{u}\rVert \le C_\varepsilon(\lvert\lambda_2\rvert + \varepsilon)^t$（Gelfand 公式），从而 $A^t\boldsymbol{n}(0)/\lambda_1^t = c\boldsymbol{w} + A^t\boldsymbol{u}/\lambda_1^t \to c\boldsymbol{w}$。当 $\boldsymbol{n}(0) \ge 0$ 非零时，由于 $\boldsymbol{v} > 0$，常数 $c$ 为正。$\square$

式 (14.2) 是对各特征量作生物学解释的基础。

**定义 14.3.1（稳定年龄分布）** 具有本原投影矩阵 $A$ 的种群的**稳定年龄分布**（对阶段分类模型则是稳定阶段分布）是主特征值的右特征向量 $\boldsymbol{w}$，归一化使 $\sum_iw_i = 1$：当生命率保持不变时，任何种群趋近的各类比例。主特征值 $\lambda_1$ 是种群渐近的**周限增长率**，$r = \ln\lambda_1$ 是其渐近增长率；$\lambda_1 > 1$、$= 1$ 或 $< 1$ 时，种群分别增长、稳定或下降。

左特征向量 $\boldsymbol{v}$ 给出各类的**繁殖价值**（Fisher 1930；[定义 15.1.6](/7.10.15#def-15.1.6)，见 7.10.15）。式 (14.2) 表明了其含义：种群的渐近大小与 $\boldsymbol{v}^{\mathsf T}\boldsymbol{n}(0) = \sum_iv_in_i(0)$ 成正比，即初始成员的总繁殖价值。第 $i$ 类的一个个体对种群未来的“价值”相当于 $v_i/v_1$ 个新生个体。对虎鲸（图 4B），把 $v$ 对当岁幼鲸标度为 1，则幼体价值为 $1.05$，繁殖雌鲸为 $1.57$ 当岁幼鲸，而繁殖后的雌鲸为零。

### 14.3.2. 收敛速率

**定义 14.3.2（阻尼比）** 本原投影矩阵的**阻尼比**是 $\rho = \lambda_1/\lvert\lambda_2\rvert > 1$，即主特征值与其他特征值的最大模之比。

由定理 14.3.2，偏离稳定分布的程度大致按 $\rho^{-t}$ 缩小，所以把它缩小到十分之一所需的时间约为 $\ln 10/\ln\rho$。若 $\lambda_2$ 为复数，则趋近是振荡的，周期为 $2\pi/\arg\lambda_2$：一次生育高峰所扰动的年龄结构会回响数代。成熟缓慢的长寿物种阻尼比通常接近 1，收敛很慢，所以对它们瞬变动态很重要（14.6.1 节）。

对虎鲸，$\lambda_1 = 1.0254$（每年增长 2.5 %），稳定阶段分布为 $\boldsymbol{w} = (0.037, 0.316, 0.323, 0.324)$。第二特征值为 $0.9804$，即繁殖后雌鲸的存活率，所以 $\rho = 1.046$，偏离缩小到十分之一大约需要 51 年（图 3C）。年增长率在几十年内稳定下来，而繁殖后雌鲸的比例要一个世纪才稳定。

![以 10 头当岁幼鲸、60 头幼体、110 头繁殖雌鲸与 70 头繁殖后雌鲸为起点，对 Brault 与 Caswell（1993）的虎鲸种群所作的投影。A：50 年内各阶段及总数（对数尺度）。B：年增长率 N(t+1)/N(t) 收敛到 λ1 = 1.0254。C：各阶段的比例收敛到稳定阶段分布 w（虚线），收敛缓慢，因为第二特征值 0.9804 接近 λ1](./plots/killer-whale-projection.py)

### 14.3.3. 收敛失败时

若矩阵不可约但不本原，种群永远不会稳定到固定的结构。一种只在 3 岁繁殖的一次繁殖型昆虫，$A = \begin{bmatrix} 0 & 0 & 8 \\ 0.5 & 0 & 0 \\ 0 & 0.5 & 0 \end{bmatrix}$，有 $A^3 = 2I$：三个特征值的模都是 $2^{1/3}$，从单一同生群开始的种群作为一个整体依次通过各年龄类，比例永远以 3 为周期循环。这种“种群波”见于周期蝉以及某些由一个年级主导的鲑鱼洄游。繁殖年龄的任何微小变异（别处的一个正元素）都会使矩阵成为本原的，此时振荡缓慢衰减。

若矩阵是可约的，如虎鲸那样，定理 14.3.2 适用于含主特征值的不可约块，条件是块外的类别（这里是繁殖后雌鲸）自身的增长率较小；它们的繁殖价值为零。

## 14.4. 敏感度与弹性

### 14.4.1. 增长率的敏感度

管理者想知道哪些生命率最重要：应当保护巢、幼体还是成体？这类问题由 $\lambda_1$ 的扰动分析回答（Caswell 1978，2001），它也给出作用于各生命率的选择的强度（[7.10.15](/7.10.15#thm-15.1.2)）。

**定义 14.4.1（种群统计敏感度与弹性）** 对主特征值为 $\lambda_1 = \lambda$ 的本原投影矩阵 $A$，$\lambda$ 对元素 $a_{ij}$ 的**种群统计敏感度**是 $s_{ij} = \partial\lambda/\partial a_{ij}$，即其他元素不变时，$a_{ij}$ 每改变一个绝对单位所引起的增长率变化。**种群统计弹性**是相对敏感度

$$
e_{ij} = \frac{a_{ij}}{\lambda}\frac{\partial\lambda}{\partial a_{ij}} = \frac{\partial\ln\lambda}{\partial\ln a_{ij}} .
$$

**定理 14.4.1（敏感度公式）** 设 $\boldsymbol{w}$ 与 $\boldsymbol{v}$ 为 $\lambda$ 的右、左特征向量，则

$$
s_{ij} = \frac{v_iw_j}{\boldsymbol{v}^{\mathsf T}\boldsymbol{w}}, \qquad e_{ij} = \frac{a_{ij}v_iw_j}{\lambda\,\boldsymbol{v}^{\mathsf T}\boldsymbol{w}} .
\tag{14.3}
$$

**证明** 因为 $\lambda$ 是单特征值，$\lambda$ 与（适当归一化的）$\boldsymbol{w}$ 是 $A$ 的元素的可微函数（对 $\det(A - \lambda I) = 0$ 用隐函数定理）。对 $A\boldsymbol{w} = \lambda\boldsymbol{w}$ 求微分：

$$
(\mathrm{d}A)\boldsymbol{w} + A\,\mathrm{d}\boldsymbol{w} = (\mathrm{d}\lambda)\boldsymbol{w} + \lambda\,\mathrm{d}\boldsymbol{w}.
$$
左乘 $\boldsymbol{v}^{\mathsf T}$ 并利用 $\boldsymbol{v}^{\mathsf T}A = \lambda\boldsymbol{v}^{\mathsf T}$：含 $\mathrm{d}\boldsymbol{w}$ 的项相消，剩下 $\boldsymbol{v}^{\mathsf T}(\mathrm{d}A)\boldsymbol{w} = \mathrm{d}\lambda\,\boldsymbol{v}^{\mathsf T}\boldsymbol{w}$。对单个元素 $a_{ij}$ 的改变，$\boldsymbol{v}^{\mathsf T}(\mathrm{d}A)\boldsymbol{w} = v_iw_j\,\mathrm{d}a_{ij}$。$\square$

该公式的含义很清楚：改变从第 $j$ 类到第 $i$ 类的流量，其重要性与第 $j$ 类在稳定种群中有多常见（$w_j$）以及目的类 $i$ 有多宝贵（$v_i$）成正比。敏感度即使对为零的元素也有定义（它说明如果某种新的转移成为可能会发生什么），而且在上限为 1 的存活概率与可能很大的繁殖力之间不可比较。弹性解决了这两个问题。

**定理 14.4.2（弹性的性质）** 本原投影矩阵的弹性非负，对零元素为零，并且满足

$$
\sum_{i,j}e_{ij} = 1, \qquad \sum_ie_{ij} = \sum_ie_{ji} \quad \text{对每个类 } j .
$$

**证明** 由式 (14.3)，$\sum_{i,j}e_{ij} = \boldsymbol{v}^{\mathsf T}A\boldsymbol{w}/(\lambda\boldsymbol{v}^{\mathsf T}\boldsymbol{w}) = \lambda\boldsymbol{v}^{\mathsf T}\boldsymbol{w}/(\lambda\boldsymbol{v}^{\mathsf T}\boldsymbol{w}) = 1$。（等价地，$\lambda$ 是各元素的一次齐次函数，由齐次函数的 Euler 定理有 $\sum a_{ij}\partial\lambda/\partial a_{ij} = \lambda$。）对第二个恒等式，$\sum_ie_{ij} = w_j(\boldsymbol{v}^{\mathsf T}A)_j/(\lambda\boldsymbol{v}^{\mathsf T}\boldsymbol{w}) = v_jw_j/\boldsymbol{v}^{\mathsf T}\boldsymbol{w}$，而 $\sum_ie_{ji} = v_j(A\boldsymbol{w})_j/(\lambda\boldsymbol{v}^{\mathsf T}\boldsymbol{w}) = v_jw_j/\boldsymbol{v}^{\mathsf T}\boldsymbol{w}$。$\square$

第一个恒等式使弹性可以读作各转移对 $\lambda$ 的相对贡献；第二个恒等式说明弹性在生活周期图的每个顶点上守恒，就像流量一样：进入某类的弧的总弹性等于离开该类的弧的总弹性。因此，属于图中某个圈而不属于其他圈的所有转移，弹性相同。在虎鲸中（图 4C），从当岁幼鲸到幼体的转移（弹性 $0.042$）是离开当岁幼鲸类的唯一的弧，它等于进入该类的两个繁殖力之和（$0.0015 + 0.0407$）。

生命率常同时进入多个矩阵元素。若这些元素依赖于更底层的参数 $\theta$（存活率 $\sigma_i$、生长 $\gamma_i$、窝卵数），链式法则给出 $\partial\lambda/\partial\theta = \sum_{i,j}s_{ij}\,\partial a_{ij}/\partial\theta$。例如，对 $P_i = \sigma_i(1 - \gamma_i)$ 与 $G_i = \sigma_i\gamma_i$，$\lambda$ 对阶段存活率 $\sigma_i$ 的弹性为 $e_{P_i} + e_{G_i}$。

有两点需要注意。敏感度和弹性是局部的：它们预测小改变的效果，大改变（消除某个死亡来源）必须重新计算 $\lambda$ 来评价。而且弹性高的生命率如果变化很小或无法改变，实际上可能并不重要，因此需要回溯性的方法（生命表响应实验、λ 贡献分析；Caswell 1989，Sibly 与 Smith 1998）：把观测到的各年、各地点或各处理间 $\lambda$ 的差异分解为各生命率的贡献，以敏感度加权这些差异。

**例 14.4.1（蠵龟）** 在美国东南部筑巢的蠵龟（*Caretta caretta*）在二十世纪后期减少，而保护工作集中于保护海滩上的巢与稚龟。Crouse、Crowder 与 Caswell（1987）根据佐治亚州 Little Cumberland 岛的数据建立了一个七阶段矩阵（卵与稚龟、小幼体、大幼体、亚成体、新繁殖者、第一年复返者、成熟繁殖者）：

$$
A = \begin{bmatrix}
0 & 0 & 0 & 0 & 127 & 4 & 80 \\
0.6747 & 0.7370 & 0 & 0 & 0 & 0 & 0 \\
0 & 0.0486 & 0.6610 & 0 & 0 & 0 & 0 \\
0 & 0 & 0.0147 & 0.6907 & 0 & 0 & 0 \\
0 & 0 & 0 & 0.0518 & 0 & 0 & 0 \\
0 & 0 & 0 & 0 & 0.8091 & 0 & 0 \\
0 & 0 & 0 & 0 & 0 & 0.8091 & 0.8089
\end{bmatrix}.
$$
此处 $\lambda = 0.945$：种群每年约下降 5 %。弹性（图 5A）最大的是小幼体的存活（合计 $0.23$）、成熟繁殖者（$0.23$）、亚成体（$0.19$）和大幼体（$0.17$），而繁殖力（$0.05$）和卵与稚龟的存活（$0.05$）很小。对大改变重新计算 $\lambda$ 证实了这一结论：把卵与稚龟的死亡率减半，只使 $\lambda$ 升到 $0.956$，繁殖力增加 50 % 使之升到 $0.966$，而把大幼体的死亡率减半则给出 $0.992$（图 5B）。即使完美的巢保护也无法阻止下降。这一分析使保护的重心转向减少大幼体和亚成体在拖虾网中的死亡；让海龟从网中逃脱的海龟逃生装置在美国的捕虾业中被强制使用，后来的模型（Crowder 等 1994）预测它们可以逆转下降。

:::

![蠵龟的弹性分析（Crouse 等 1987 的矩阵，λ1 = 0.945）。A：λ1 的弹性按阶段与转移类型（繁殖力、留在阶段、长到下一阶段）加总；总和为 1。B：只把单个阶段的年死亡率减半，或繁殖力增加 50 % 之后重新计算的 λ1（实线：原来的 λ1；虚线：λ = 1）。改善幼体与亚成体的存活影响最大；保护卵与稚龟的作用很小](./plots/loggerhead-elasticity.py)

## 14.5. 更多案例

### 14.5.1. 再谈虎鲸

虎鲸模型体现了本章的所有量（图 4）。一个有 250 头雌鲸、起初全是繁殖成体的种群，相对于以 $\lambda_1$ 增长的情形，最终的大小是初始大小的 $1.79$ 倍；起初全是当岁幼鲸的种群则只有 $1.14$ 倍，先经历幼鲸成熟期间的初期下降；由繁殖后雌鲸构成的种群则会灭绝。由式 (14.2)，这些常数是 $v_j/\boldsymbol{v}^{\mathsf T}\boldsymbol{w}$（$\sum_iw_i = 1$）。弹性表明，$\lambda$ 压倒性地取决于繁殖雌鲸在其阶段中的存活（$e = 0.54$）与幼体的存活（$e = 0.34$）；繁殖力只占 4 %。这是寿命长、繁殖慢的动物的典型格局，也解释了它们对任何额外的成体死亡都很脆弱：由式 (14.3)，$\partial\lambda/\partial a_{33} = 0.58$，所以仅仅额外增加每年 4.4 % 的繁殖雌鲸死亡，就会使 $\lambda$ 从 $1.025$ 降到约 1。同一地区的南部常驻种群主要捕食数量在下降的大鳞大麻哈鱼（王鲑），事实上自 1990 年代以来一直在减少；现在用这类模型的随机版本分析它的种群统计（[7.19.15](/7.19.15)）。

![初始阶段与特征向量在虎鲸模型中的作用。A：四个各有 250 头雌鲸、起初全部处于同一阶段的种群，相对于渐近增长速率的总大小；每个都收敛到起始阶段的繁殖价值除以 v·w（虚线），而繁殖后雌鲸构成的种群会灭绝。B：稳定阶段分布 w（比例）与繁殖价值 v（当岁幼鲸 = 1）。C：λ1 对六个非零元素的弹性；总和为 1，成体与幼体的存活占主导](./plots/killer-whale-initial-conditions.py)

### 14.5.2. 一种草原植物与两种害虫

*Silene regia*（royal catchfly）是北美草原上的长寿多年生植物，成体存活率高，生长缓慢，常开花，补充则极不规律：多数种群在多数年份没有幼苗建成。Menges 与 Dolan（1998）为 16 个种群和若干年份建立了一个六阶段矩阵（幼苗、营养期、小型、中型与大型开花植株，以及“存活但未定义”，即割草或食草后没有大小数据的植株）。对一个用计划烧除管理的种群，在有补充的年份，矩阵（列：$t$ 时的阶段；行：$t + 1$ 时的阶段）为

$$
A = \begin{bmatrix}
0 & 0 & 5.32 & 12.74 & 30.88 & 0 \\
0.308 & 0.111 & 0 & 0 & 0 & 0 \\
0 & 0.566 & 0.506 & 0.137 & 0.167 & 0.367 \\
0 & 0.111 & 0.210 & 0.608 & 0.167 & 0.300 \\
0 & 0 & 0.012 & 0.039 & 0.667 & 0.167 \\
0 & 0.222 & 0.198 & 0.196 & 0 & 0.133
\end{bmatrix},
$$
其主特征值（由这些四舍五入的元素算得）为 $1.70$；发表值为 $1.67$。有补充的年份中 $\lambda > 1.35$ 的所有种群都被烧除过，且没有一个被预测会灭绝；而未烧除的种群 $\lambda$ 较低，在随机模拟中 1000 年内的灭绝概率为 10–100 %。火在植被中开出空隙，幼苗得以建成，管理建议由此直接得出。

矩阵模型同样服务于害虫管理。九带犰狳（*Dasypus novemcinctus*）是美国南部麻风的宿主，$\lambda$ 对成体存活的弹性接近 0.5，所以如需控制，应以成体为对象（Oli 等 2017）。对入侵杂草 *Carduus nutans*（nodding thistle），澳大利亚的弹性由小植株的存活与生长主导，新西兰则由种子生产与萌发主导；降低生长与存活的根冠象甲在澳大利亚有效，而在新西兰则需要减少结实的天敌（Shea 等 2005）。同一物种在不同地方可以有不同的脆弱点。

## 14.6. 瞬变与连续结构

### 14.6.1. 瞬变动态

渐近分析说明种群最终走向何处；管理者常常关心接下来的 10 年或 20 年，其间结构可能远离 $\boldsymbol{w}$。瞬变行为由次主特征值和初始结构决定。常用两种度量。相对于渐近增长的*放大*（或衰减）$\lim_t N(t)/(\lambda_1^tN(0)) = \boldsymbol{v}^{\mathsf T}\boldsymbol{n}(0)/(\boldsymbol{v}^{\mathsf T}\boldsymbol{w}\,\sum_in_i(0))$（$\sum_iw_i = 1$），说明具有给定结构的种群最终会比具有稳定结构的种群更大还是更小；对引入与再引入，它表明在个体数相同的情况下，释放繁殖成体比释放幼体得到的种群更大（图 4A）。*种群惯性*是种群生命率突然变为更替水平（$\lambda_1 = 1$）这一特殊情形：它由于年龄结构而继续增长（或下降）一段时间，最终大小为 $\boldsymbol{v}^{\mathsf T}\boldsymbol{n}(0)/\boldsymbol{v}^{\mathsf T}\boldsymbol{w}$，用新矩阵的特征向量计算。年龄结构年轻的人类种群在生育率降到更替水平之后还会继续增长数十年。矩阵还可能是*反应性的*：即使 $\lambda_1 < 1$，某些初始结构在短期内仍会增长（一批即将成熟的幼体），这可能误导短期的监测计划。

### 14.6.2. 连续年龄：McKendrick–von Foerster 方程

若年龄 $a$ 与时间 $t$ 是连续的，令 $n(t, a)$ 为时刻 $t$ 年龄为 $a$ 的个体密度，$\mu(a)$ 为年龄特异的死亡率，$m(a)$ 为出生率（每个雌体单位时间内的雌性出生数）。

**定义 14.6.1（McKendrick–von Foerster 方程）** **McKendrick–von Foerster 方程**是一阶偏微分方程

$$
\frac{\partial n}{\partial t} + \frac{\partial n}{\partial a} = -\mu(a)\,n, \qquad n(t, 0) = \int_0^\infty m(a)\,n(t, a)\,\mathrm{d}a, \qquad n(0, a) = n_0(a),
\tag{14.4}
$$
其中个体以单位速度变老，以速率 $\mu(a)$ 死亡，年龄为 0 处的边界条件汇集了出生。

它用**特征线法**（[2.5.2](/2.5.2)）求解。沿直线 $a - t = \text{const}$（一个随时间变老的同生群），$\mathrm{d}n/\mathrm{d}t = -\mu(a)n$，所以以存活率 $\ell(a) = \exp\bigl(-\int_0^a\mu(s)\,\mathrm{d}s\bigr)$，

$$
n(t, a) = \begin{cases} B(t - a)\,\ell(a), & a < t, \\ n_0(a - t)\,\ell(a)/\ell(a - t), & a \ge t, \end{cases}
$$
其中 $B(t) = n(t, 0)$ 为出生率。代入边界条件得到 Lotka（1922）的更新方程：

$$
B(t) = \int_0^tm(a)\ell(a)B(t - a)\,\mathrm{d}a + G(t),
\tag{14.5}
$$
其中 $G(t) = \int_t^\infty m(a)n_0(a - t)\ell(a)/\ell(a - t)\,\mathrm{d}a$ 是时刻 0 时已存活个体的贡献，当它们过了繁殖期就消失。在齐次方程中取 $B(t) = B_0\mathrm{e}^{rt}$，得连续的 **Euler–Lotka 方程**

$$
\int_0^\infty\mathrm{e}^{-ra}\ell(a)m(a)\,\mathrm{d}a = 1,
\tag{14.6}
$$
其左端（当 $\ell m$ 不恒为零时）随 $r$ 从 $+\infty$ 严格地降到 0，所以恰有一个实根 $r$；所有复根的实部更小，并且 $B(t) \sim B_0\mathrm{e}^{rt}$（Feller 1941）。稳定年龄分布为 $c(a) \propto \mathrm{e}^{-ra}\ell(a)$：年龄 $a$ 处的密度因存活而降低，也因为年长个体出生时种群较小而降低（图 6）。这是定理 14.3.2 的连续对应，而 [7.10.15](/7.10.15) 的离散 Euler–Lotka 方程则是其对年龄类按年划分的**生命表**的版本。方程 (14.4) 是生理结构模型的出发点，在这类模型中，大小或其他生理变量取代年龄，并以可能依赖于食物的速率增长。

![McKendrick–von Foerster 方程，常数死亡率 μ = 0.3 每年，2 至 6 岁之间的繁殖力为 1.2 每年，从 0–1 岁个体的一次脉冲开始。A：40 年内的年龄分布 n(t, a)/N(t)：各同生群沿特征线 a - t = const（白线）行进，初始脉冲的回响逐渐消失。B：四个时刻的年龄分布，以及由 Euler–Lotka 方程得到的稳定年龄分布 c(a) ∝ exp(-ra) l(a)，r = 0.121 每年（虚线）](./plots/mckendrick-characteristics.py)

### 14.6.3. 积分投影模型

当种群统计依赖于体重或植株大小这类连续性状时，任意划定的类别边界会丢失信息。积分投影模型（integral projection model）由 Easterling、Ellner 与 Dixon（2000）提出，它以核代替矩阵：

$$
n(z', t + 1) = \int_L^U K(z', z)\,n(z, t)\,\mathrm{d}z, \qquad K(z', z) = s(z)\,g(z' \mid z) + f(z)\,c(z'),
$$
其中 $s(z)$ 为大小为 $z$ 的个体的存活率，$g(z' \mid z)$ 为其明年大小 $z'$ 的概率密度，$f(z)$ 为其繁殖力，$c(z')$ 为后代的大小分布。每个函数都由对个体数据的回归估计（存活率用对大小的逻辑斯谛回归，生长用线性回归，等等），这充分利用了数据。数值上用中点法则在细网格上计算积分，这把 $K$ 变成一个大矩阵，本章的所有结果（主特征值、特征向量、敏感度，现在都是大小的函数）都可沿用。积分投影模型可以在生命率函数中包含密度制约与环境协变量；在圣基尔达岛的 Soay 羊中，它们把体重、种群密度与种群增长率联系起来（Coulson 2012）。

## 小结

- 投影矩阵 $A$（定义 14.2.1）按 $\boldsymbol{n}(t + 1) = A\boldsymbol{n}(t)$ 投影各类的数量；Leslie 矩阵按年龄分类，Lefkovitch 矩阵按阶段或大小分类，其元素有 $P_i = \sigma_i(1 - \gamma_i)$、$G_i = \sigma_i\gamma_i$ 与繁殖力 $F_i$，其中 $F_i$ 的定义取决于普查的时机。生活周期图显示结构；不可约性（强连通）与本原性（圈长的最大公约数为 1）控制长期行为。
- Perron–Frobenius 定理（定理 14.3.1）与强遍历定理（定理 14.3.2）：

  | 量 | 定义 | 含义 |
  |---|---|---|
  | $\lambda_1$ | 主特征值，为正的单根 | 渐近周限增长率；$r = \ln\lambda_1$ |
  | $\boldsymbol{w}$ | $A\boldsymbol{w} = \lambda_1\boldsymbol{w}$，$\boldsymbol{w} > 0$ | 稳定年龄（阶段）分布（定义 14.3.1） |
  | $\boldsymbol{v}$ | $\boldsymbol{v}^{\mathsf T}A = \lambda_1\boldsymbol{v}^{\mathsf T}$，$\boldsymbol{v} > 0$ | 繁殖价值；渐近大小 $\propto \boldsymbol{v}^{\mathsf T}\boldsymbol{n}(0)$，式 (14.2) |
  | $\rho = \lambda_1/\lvert\lambda_2\rvert$ | 阻尼比（定义 14.3.2） | 收敛速率；长寿物种收敛慢 |

  非本原矩阵给出持续的种群波；可约矩阵分解为块。
- 敏感度 $s_{ij} = v_iw_j/\boldsymbol{v}^{\mathsf T}\boldsymbol{w}$ 与弹性 $e_{ij} = a_{ij}s_{ij}/\lambda$（定义 14.4.1，定理 14.4.1）；弹性之和为 1，且在每个类处守恒（定理 14.4.2）。更底层的参数由链式法则得出；大的改变必须重新计算；回溯性分析（LTRE、λ 贡献）分解观测到的变异。
- 应用：虎鲸（$\lambda = 1.025$，成体存活占主导，收敛缓慢）、蠵龟（$\lambda = 0.945$；控制趋势的是幼体与亚成体的存活而不是巢保护：海龟逃生装置）、royal catchfly（烧除使补充得以发生）、犰狳与飞廉（管理对象因物种与地点而异）。
- 瞬变：放大、惯性与反应性通过 $\boldsymbol{v}$ 依赖于初始结构。连续年龄给出 McKendrick–von Foerster 方程（定义 14.6.1），沿特征线求解，导出 Lotka 更新方程 (14.5)、Euler–Lotka 方程 (14.6) 与稳定年龄分布 $c(a) \propto \mathrm{e}^{-ra}\ell(a)$。积分投影模型以连续性状代替类别。

## 思考题

1. 对 Fibonacci 矩阵 $\begin{bmatrix} 1 & 1 \\ 1 & 0 \end{bmatrix}$，计算 $\lambda_1$ 的敏感度与弹性，并检验定理 14.4.2。

   **答** 设 $\varphi = \lambda_1 = (1 + \sqrt5)/2$，$\boldsymbol{w} = (\varphi, 1)^{\mathsf T}$，$\boldsymbol{v} = (\varphi, 1)^{\mathsf T}$（矩阵对称），$\boldsymbol{v}^{\mathsf T}\boldsymbol{w} = \varphi^2 + 1$。敏感度为 $s_{11} = \varphi^2/(\varphi^2 + 1) = 0.724$，$s_{12} = s_{21} = \varphi/(\varphi^2 + 1) = 0.447$，$s_{22} = 1/(\varphi^2 + 1) = 0.276$。三个非零元素的弹性为 $e_{11} = s_{11}/\varphi = 0.447$，$e_{12} = e_{21} = s_{12}/\varphi = 0.276$，$e_{22} = 0$。它们之和为 $0.447 + 0.276 + 0.276 = 1$；在幼年类处，进入的弹性 $e_{21} = 0.276$ 等于离开的弹性 $e_{12} = 0.276$，符合守恒律：这两条弧构成一个不属于其他圈的长度为 2 的圈。

2. 在虎鲸模型中，设每年移走 $h$ 头繁殖雌鲸（例如由于误捕或为水族馆捕捉），而种群处于稳定结构，共 250 头雌鲸。由敏感度估计最大的可持续 $h$，并解释为什么这一估计只是近似的。

   **答** 移走繁殖雌鲸的恒定比例 $q$，使 $a_{33}$ 与 $a_{43}$（以及假定存活的繁殖力 $a_{13}$）都缩小为 $1 - q$ 倍。只用 $a_{33}$，$\Delta\lambda \approx -s_{33}a_{33}q = -0.579 \times 0.953\,q$，而 $\lambda$ 至少为 1 的条件是 $q \le 0.0254/0.552 \approx 0.046$；若计入另两个元素，第 3 列三个元素的总弹性为 $0.54 + 0.04 + 0.0 = 0.58$，给出 $\Delta\ln\lambda \approx -0.58q$，$q \le 0.025/0.58 \approx 0.043$（精确重算 $\lambda$ 得 $0.047$）。繁殖雌鲸有 $250 \times 0.323 \approx 81$ 头，这相当于每年约 $3.5$ 头；从稳定结构出发模拟 $\boldsymbol{n}(t + 1) = A\boldsymbol{n}(t) - \boldsymbol{h}$ 也给出约 $3.5$。估计只是近似，因为敏感度是线性近似；因为恒定数量的移走不同于恒定比例的移走（种群缩小时它成为越来越大的比例）；也因为模型忽略了随机性与密度制约；实际上，对这样小而繁殖缓慢的种群，任何捕获都是不可取的。

3. 证明只在 2 岁与 4 岁有繁殖力（且至 4 岁存活概率为正）的 Leslie 矩阵是不可约的但不是本原的。这对从只有新生个体开始的种群的年龄结构意味着什么？

   **答** 图中有一条穿过各年龄类的路径，以及从两个繁殖年龄回到第一类的弧，它们闭合出长度为 2 与 4 的圈。所有类互相可达，所以矩阵不可约；但每个圈的长度都是偶数，所以 $h = \gcd(2, 4) = 2$：存在一个与 $\lambda_1$ 模相同的特征值 $-\lambda_1$。从新生个体开始的种群只在偶数年产生后代，且只在偶数年龄类中，所以种群在两种不同的结构（奇数类与偶数类有个体）之间交替，永远不收敛到 $\boldsymbol{w}$；在奇数年龄的任何繁殖都使矩阵变成本原的，并使振荡衰减。

4. 把 $n(t, a) = \mathrm{e}^{rt}c(a)$ 代入式 (14.4)，直接推导 McKendrick–von Foerster 方程的稳定年龄分布。

   **答** 代入得 $rc(a) + c'(a) = -\mu(a)c(a)$，所以 $c(a) = c(0)\exp\bigl(-ra - \int_0^a\mu\bigr) = c(0)\mathrm{e}^{-ra}\ell(a)$。边界条件变为 $c(0) = \int m(a)c(0)\mathrm{e}^{-ra}\ell(a)\,\mathrm{d}a$，当 $c(0) \ne 0$ 时它就是 Euler–Lotka 方程 (14.6)。所以变量分离的解只对式 (14.6) 的根存在，而其中取实数 $r$ 的那个解有正的年龄分布。

5. 保护机构既可以保护海滩（把卵与稚龟的死亡率减半），也可以要求使用海龟逃生装置（把蠵龟大幼体与亚成体的死亡率减半）。利用例 14.4.1 的弹性，说明矩阵模型倾向于哪一种方案，以及管理者在决定之前还需要什么额外信息。

   **答** $\lambda$ 对卵与稚龟存活的弹性约为 $0.05$，而对大幼体与亚成体存活的合计弹性约为 $0.36$。死亡率减半对不同阶段的存活率改变的相对幅度不同（稚龟存活率 $0.67 \to 0.84$，增加 24 %；大幼体存活率 $0.68 \to 0.84$），所以应通过重新计算 $\lambda$ 来比较：保护海滩给出 $\lambda \approx 0.956$，对这两个阶段使用逃生装置给出约 $1.025$，足以逆转下降。管理者还需要知道每种行动的成本与可行性、生命率的不确定性（结论对估计误差的敏感性）、高丰度时可能的密度制约，以及（来自 1980 年代一处海滩的）矩阵是否代表现在的种群；弹性说明了努力可能在哪里有效，却不说明某个方案是否可行。

6. （开放题）在矩阵模型中，繁殖后虎鲸雌鲸的繁殖价值为零。讨论这是否意味着这样的雌鲸对种群不重要。

   **答** 要点：矩阵模型只计算对未来出生的直接贡献，所以按构造，繁殖后雌鲸的繁殖价值为零，其存活的敏感度也为零。然而在常驻型虎鲸中，繁殖后的母亲在食物短缺的年份带领其群体寻找鲑鱼，而繁殖后母亲的死亡会使其成年后代、尤其是儿子在随后几年的死亡率大大增加（Foster 等 2012；Brent 等 2015）。这些效应通过其他类别的存活起作用，而模型把它们当作常数；若在模型中让幼体或成体的存活依赖于祖母的存在，就会给繁殖后雌鲸以间接的繁殖价值。这个例子表明，矩阵模型的好坏取决于个体相互独立的假定，并与经由亲缘选择的更年期演化相联系（[7.10.16](/7.10.16)）。
