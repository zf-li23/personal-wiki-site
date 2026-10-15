---
title: Hermite 变换、双线性型与张量
---

[上一章](/2.1.12)证明了正规变换恰好是能在标准正交基下对角化的变换。正规矩阵与复数之间有一个清楚的对应：正规矩阵中特征值全为实数的一类（Hermite 矩阵）相当于实数，特征值模为 $1$ 的一类（酉矩阵）相当于单位复数。本章前半部分沿着这个类比，把复数的极形式 $z = re^{i\theta}$ 推广为矩阵的极分解 $A = Re^{iM}$；再把 [第 7 章](/2.1.7)的实**二次型**、**合同**、**Sylvester 惯性定律**与正定矩阵搬到复数域上，得到 Hermite 二次型与复相合；最后叙述复矩阵的**奇异值分解**，并说明它与极分解的关系。这些结论的证明多与实情形相同，只简述。

后半部分换一个角度。内积 $(a, b), (c, d) \mapsto ac + bd$ 与平面上的有向面积 $(a, b), (c, d) \mapsto ad - bc$（二阶**行列式**）都是"两个向量 $\mapsto$ 一个数"、对每个变量都线性的映射。本章在一般线性空间上研究这类映射——双线性型，它们在换基下按 $P^{\mathsf T}GP$ 变化，这正是合同关系的来源。对称的非退化双线性型给出"广义内积"（如狭义相对论中的 Lorentz 型），反对称的给出辛空间；保持它们的变换构成正交群与辛群。最后用[第 8 章](/2.1.8)的**对偶空间**引入张量：从数（$0$ 阶）到线性函数（$1$ 阶）、双线性型（$2$ 阶），再到多重线性型。

本章仍贯穿"化为标准问题"的思路：Hermite 二次型化规范形就是酉对角化；判定正定可以归结为特征值、顺序主子式或一次 Cholesky 分解，三者代价不同；双线性型的分类就是表示矩阵在合同下的标准形，换基只需计算 $P^{\mathsf T}GP$。

## 13.1. 自伴随算子与 Hermite 矩阵

**定义 13.1.1** 设 $V$ 是内积空间，$T: V \to V$ 是线性变换。若 $T$ 的伴随 $T^*$ 存在且 $T = T^*$，即 $\langle T\alpha, \beta \rangle = \langle \alpha, T\beta \rangle$ 对一切 $\alpha, \beta$ 成立，则称 $T$ 为**自伴随算子**。欧氏空间上的自伴随算子称为对称变换，酉空间上的自伴随算子称为 **Hermite 变换**。

**定义 13.1.2** 设 $A \in M_n(\mathbb{C})$。若 $A^{\mathsf H} = A$，则称 $A$ 为 **Hermite 矩阵**；若 $A^{\mathsf H} = -A$，则称 $A$ 为**反 Hermite 矩阵**。

由定理 12.6.2，$T$ 是 Hermite 变换（对称变换）当且仅当它在标准正交基下的矩阵是 Hermite 矩阵（实对称矩阵）。Hermite 矩阵的对角元满足 $a_{ii} = \bar a_{ii}$，都是实数。Hermite 变换显然是正规变换。

**例 13.1.1** $\mathbb{R}^n$ 上 $x \mapsto Ax$，$A$ 实对称，是对称变换。$\mathbb{C}^2$ 上 $x \mapsto \begin{pmatrix} 2 & 1 + i \\ 1 - i & 3 \end{pmatrix}x$ 是 Hermite 变换：在标准正交基 $e_1, e_2$ 下矩阵为 $A$，$A^{\mathsf H} = A$。

**定理 13.1.1** 设 $A$ 是 Hermite 矩阵。

1. $A$ 的特征值都是实数；
2. 存在酉矩阵 $U$ 使 $U^{\mathsf H}AU = \operatorname{diag}(\lambda_1, \dots, \lambda_n)$，$\lambda_i \in \mathbb{R}$；
3. 反之，特征值全为实数的正规矩阵是 Hermite 矩阵；
4. 反 Hermite 矩阵的特征值是纯虚数或零；$A$ 是 Hermite 矩阵 $\Leftrightarrow$ $iA$ 是反 Hermite 矩阵。

**证明** 1：设 $A\alpha = \lambda\alpha$，$\alpha \ne 0$，则 $\lambda\langle \alpha, \alpha \rangle = \langle A\alpha, \alpha \rangle = \langle \alpha, A\alpha \rangle = \bar\lambda\langle \alpha, \alpha \rangle$，故 $\lambda = \bar\lambda$。2：$A$ 正规，由**谱定理**与 1。3：$A = U\Lambda U^{\mathsf H}$，$\Lambda$ 实，则 $A^{\mathsf H} = U\bar\Lambda U^{\mathsf H} = A$。4：类似 1，$\lambda = -\bar\lambda$。 $\square$

**例 13.1.2** 正交投影是自伴随算子。设 $V = W \oplus W^\perp$，$v = v_1 + v_2$，$w = w_1 + w_2$（$v_1, w_1 \in W$，$v_2, w_2 \in W^\perp$），$Tv = v_1$。则

$$
\langle Tv, w \rangle = \langle v_1, w_1 + w_2 \rangle = \langle v_1, w_1 \rangle = \langle v_1 + v_2, w_1 \rangle = \langle v, Tw \rangle.
$$

**例 13.1.3** 设 $V = \operatorname{span}\{1, \cos x, \sin x\}$，$\langle f, g \rangle = \int_0^{2\pi}f(x)g(x)\,\mathrm{d}x$，$D: f \mapsto f'$。$e_1 = \frac{1}{\sqrt{2\pi}}$，$e_2 = \frac{\cos x}{\sqrt\pi}$，$e_3 = \frac{\sin x}{\sqrt\pi}$ 是标准正交基，$De_1 = 0$，$De_2 = -e_3$，$De_3 = e_2$，所以

$$
(De_1, De_2, De_3) = (e_1, e_2, e_3)A, \qquad A = \begin{pmatrix} 0 & 0 & 0 \\ 0 & 0 & 1 \\ 0 & -1 & 0 \end{pmatrix}, \qquad A^{\mathsf T} = -A.
$$

故 $D^* = -D$，$D$ 不是自伴随的，而是反自伴随的，特征值为 $0, \pm i$（对应复函数 $1, e^{\pm ix}$）。背后的原因是分部积分：对周期函数，$\langle f', g \rangle = -\langle f, g' \rangle$。相应地 $-D^2 = -\frac{\mathrm{d}^2}{\mathrm{d}x^2}$ 是自伴随的，这是偏微分方程中 Fourier 级数方法的出发点。

任一复方阵都可以唯一地写成 $A = H + K$，$H = \frac12(A + A^{\mathsf H})$ 是 Hermite 矩阵，$K = \frac12(A - A^{\mathsf H})$ 是反 Hermite 矩阵，这是 $z = a + bi$ 分成实部与虚部的类比。展开 $AA^{\mathsf H}$ 与 $A^{\mathsf H}A$ 可知，$A$ 正规 $\Leftrightarrow$ $HK = KH$。

## 13.2. 极分解

复数与矩阵的对应关系如下表（复数 $z = a + bi$ 本身对应 2 阶实正规矩阵 $\begin{pmatrix} a & -b \\ b & a \end{pmatrix}$，[第 9 章](/2.1.9)）。

| 复数 | 矩阵 |
|---|---|
| **共轭复数** $\bar z$ | **共轭转置** $A^{\mathsf H}$ |
| $z\bar z = \bar zz$ | 正规：$AA^{\mathsf H} = A^{\mathsf H}A$ |
| 实数 $z = \bar z$ | Hermite 矩阵 $A = A^{\mathsf H}$ |
| 纯虚数 $z = -\bar z$ | 反 Hermite 矩阵 $A = -A^{\mathsf H}$ |
| $\lvert z\rvert = 1$，即 $\bar zz = 1$ | 酉矩阵 $A^{\mathsf H}A = I$ |
| $r \ge 0$ | 半正定 Hermite 矩阵（特征值 $\ge 0$） |
| $e^{i\theta}$，$\theta$ 实 | $e^{iM}$，$M$ 为 Hermite 矩阵（例 12.3.3） |
| 极形式 $z = re^{i\theta}$ | $A = Re^{iM}$ |

**定理 13.2.1** 设 $A$ 是 $n$ 阶正规矩阵，则存在半正定 Hermite 矩阵 $R$ 与 Hermite 矩阵 $M$，使 $A = Re^{iM}$，且 $RM = MR$。

**证明** 由谱定理，存在酉矩阵 $U$ 使 $U^{\mathsf H}AU = \operatorname{diag}(\lambda_1, \dots, \lambda_n)$。把每个特征值写成**复数的极形式** $\lambda_j = r_je^{i\theta_j}$，$r_j \ge 0$，$\theta_j \in \mathbb{R}$，令

$$
R = U\operatorname{diag}(r_1, \dots, r_n)U^{\mathsf H}, \qquad M = U\operatorname{diag}(\theta_1, \dots, \theta_n)U^{\mathsf H}.
$$

$R$ 是特征值非负的 Hermite 矩阵，$M$ 是 Hermite 矩阵，二者被同一个 $U$ 对角化，所以可交换。由矩阵函数的性质 $e^{iM} = U\operatorname{diag}(e^{i\theta_1}, \dots, e^{i\theta_n})U^{\mathsf H}$，于是 $Re^{iM} = U\operatorname{diag}(r_je^{i\theta_j})U^{\mathsf H} = A$。 $\square$

称 $A = Re^{iM}$ 为正规矩阵 $A$ 的极分解（polar decomposition）。由 $A^{\mathsf H}A = e^{-iM}R^2e^{iM} = R^2$，$R = (A^{\mathsf H}A)^{1/2}$ 由 $A$ 唯一确定（取半正定的平方根）；$M$ 不唯一，各 $\theta_j$ 可以相差 $2\pi$ 的整数倍，$A$ 不可逆时零特征值的辐角也可任取。这兑现了[第 11 章](/2.1.11)开头提出的问题。

**例 13.2.1** 复数 $z = re^{i\theta}$ 对应的矩阵 $A = \begin{pmatrix} r\cos\theta & -r\sin\theta \\ r\sin\theta & r\cos\theta \end{pmatrix}$ 的极分解为 $R = rI$，$M = \begin{pmatrix} 0 & i\theta \\ -i\theta & 0 \end{pmatrix}$：$M$ 是 Hermite 矩阵，$iM = \theta\begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}$，$e^{iM}$ 就是转角为 $\theta$ 的旋转矩阵（例 11.8.1）。矩阵的极分解与复数的极形式在这里完全重合。

一般方阵（不必正规）也有极分解 $A = UP$（$U$ 为酉矩阵，$P$ 为半正定 Hermite 矩阵），但 $U$ 与 $P$ 不一定可交换，见 13.5 节。

## 13.3. Hermite 二次型

**定义 13.3.1** 设 $a_{ij} = \bar a_{ji}$（$1 \le i, j \le n$），称 $n$ 个复变量的函数 $f(x_1, \dots, x_n) = \sum_{i,j=1}^n a_{ij}\bar x_ix_j$ 为 $n$ 元 **Hermite 二次型**。记 $A = (a_{ij})$，则 $A$ 是 Hermite 矩阵，$f = x^{\mathsf H}Ax$，$A$ 称为 $f$ 的矩阵。

**例 13.3.1** $f(x_1, x_2) = i\bar x_1x_2 - i\bar x_2x_1$ 的矩阵为 $\begin{pmatrix} 0 & i \\ -i & 0 \end{pmatrix}$。$x = (1, i)^{\mathsf T}$ 时 $f = i \cdot i - i \cdot (-i) \cdot 1 = -2$。

**性质 13.3.1**

1. Hermite 二次型取实值：$\overline{f} = \overline{x^{\mathsf H}Ax} = (x^{\mathsf H}Ax)^{\mathsf H} = x^{\mathsf H}A^{\mathsf H}x = f$。
2. $n$ 阶 Hermite 矩阵与 $n$ 元 Hermite 二次型一一对应：若 $x^{\mathsf H}Cx = 0$ 对一切 $x \in \mathbb{C}^n$ 成立，则 $C = O$。取 $x = e_j$ 得 $c_{jj} = 0$；取 $x = e_j + e_k$ 与 $x = e_j + ie_k$ 得 $c_{jk} + c_{kj} = 0$ 与 $i(c_{jk} - c_{kj}) = 0$，所以 $c_{jk} = 0$。

作可逆变量替换 $x = Py$，$f = x^{\mathsf H}Ax = y^{\mathsf H}(P^{\mathsf H}AP)y$，矩阵按下面的关系变化。

**定义 13.3.2** 设 $A, B \in M_n(\mathbb{C})$。若存在可逆矩阵 $P$ 使 $P^{\mathsf H}AP = B$，则称 $A$ 与 $B$ **复相合**。

复相合是等价关系，它是实矩阵合同（$P^{\mathsf T}AP$）的复版本。由于酉矩阵满足 $P^{\mathsf H} = P^{-1}$，酉相似既是相似也是复相合，所以化 Hermite 二次型的标准方法就是酉对角化。

**定理 13.3.1（惯性定律）** 任一 Hermite 二次型 $f = x^{\mathsf H}Ax$ 都可以经可逆线性替换 $x = Cz$ 化为规范形

$$
f = \bar z_1z_1 + \cdots + \bar z_pz_p - \bar z_{p+1}z_{p+1} - \cdots - \bar z_rz_r,
$$

其中 $r = \operatorname{rank}(A)$，正惯性指数 $p$ 等于 $A$ 的正特征值的个数，且 $p$、$r$ 由 $f$ 唯一确定。矩阵形式：Hermite 矩阵复相合于 $\operatorname{diag}(I_p, -I_{r-p}, O)$，两个 Hermite 矩阵复相合当且仅当它们的秩与正惯性指数分别相同。

**证明** 存在性：由定理 13.1.1，有酉矩阵 $U$ 使 $U^{\mathsf H}AU = \operatorname{diag}(d_1, \dots, d_r, 0, \dots, 0)$，$d_1, \dots, d_p > 0 > d_{p+1}, \dots, d_r$。令 $D = \operatorname{diag}(|d_1|^{-1/2}, \dots, |d_r|^{-1/2}, 1, \dots, 1)$，$C = UD$ 即可。唯一性的证明与实对称矩阵的情形（定理 7.3.3）相同：若 $f$ 有两个正惯性指数不同的规范形，用维数公式可以找到一个非零向量，在一个规范形下 $f > 0$，在另一个下 $f \le 0$，矛盾。 $\square$

$p$ 与 $r - p$ 称为 $f$ 的正、负**惯性指数**。

**例 13.3.2** $A = \begin{pmatrix} 1 & i & 1 \\ -i & 0 & 0 \\ 1 & 0 & 0 \end{pmatrix}$，求可逆阵 $C$ 使 $f = x^{\mathsf H}Ax$ 化为规范形。

1. $\det(\lambda I - A) = (\lambda - 2)(\lambda + 1)\lambda$，特征值 $2, -1, 0$。对应的特征向量为 $(2, -i, 1)^{\mathsf T}$、$(-1, -i, 1)^{\mathsf T}$、$(0, i, 1)^{\mathsf T}$，它们属于不同特征值，自动正交，单位化得
$$
q_1 = \tfrac{1}{\sqrt6}(2, -i, 1)^{\mathsf T}, \qquad q_2 = \tfrac{1}{\sqrt3}(-1, -i, 1)^{\mathsf T}, \qquad q_3 = \tfrac{1}{\sqrt2}(0, i, 1)^{\mathsf T}.
$$
2. $P = (q_1, q_2, q_3)$ 是酉矩阵，$P^{\mathsf H}AP = \operatorname{diag}(2, -1, 0)$。令 $x = Py$，$f = 2\bar y_1y_1 - \bar y_2y_2$。
3. 令 $y = Dz$，$D = \operatorname{diag}(\frac{1}{\sqrt2}, 1, 1)$，则 $f = \bar z_1z_1 - \bar z_2z_2$。$C = PD$，$p = 1$，$r = 2$。

## 13.4. 正定 Hermite 矩阵

**定义 13.4.1（正定矩阵）** 设 $A$ 是 $n$ 阶 Hermite 矩阵。若对一切 $x \ne 0$ 有 $x^{\mathsf H}Ax > 0$，则称 $A$ 为正定 Hermite 矩阵，$f = x^{\mathsf H}Ax$ 为正定 Hermite 二次型；若 $x^{\mathsf H}Ax \ge 0$，则称 $A$ 为半正定 Hermite 矩阵。

由[上一章](/2.1.12)的度量矩阵，$\mathbb{C}^n$ 上的内积与 $n$ 阶正定 Hermite 矩阵 $G$ 一一对应：$\langle \alpha, \beta \rangle = \alpha^{\mathsf T}G\bar\beta$。$G = I$ 就是标准内积。

**性质 13.4.1** 对任意 $A \in \mathbb{C}^{m \times n}$，$A^{\mathsf H}A$ 与 $AA^{\mathsf H}$ 都是半正定 Hermite 矩阵；若 $A$ 列满秩，则 $A^{\mathsf H}A$ 正定；若 $A$ 行满秩，则 $AA^{\mathsf H}$ 正定。

**证明** $x^{\mathsf H}A^{\mathsf H}Ax = \|Ax\|^2 \ge 0$；$A$ 列满秩时 $x \ne 0 \Rightarrow Ax \ne 0$，不等式严格。 $\square$

**定理 13.4.1** 设 $A$ 是 $n$ 阶 Hermite 矩阵，以下条件等价：

1. $A$ 正定；
2. $A$ 的特征值全为正数；
3. 存在可逆矩阵 $P$ 使 $A = P^{\mathsf H}P$；
4. $A$ 复相合于 $I_n$；
5. $A$ 的所有**顺序主子式**都大于零；
6. 存在对角元为正实数的上三角矩阵 $R$，使 $A = R^{\mathsf H}R$，且 $R$ 唯一（复的 **Cholesky 分解**）。

**证明** 1 $\Rightarrow$ 2：$A\alpha = \lambda\alpha$ 时 $0 < \alpha^{\mathsf H}A\alpha = \lambda\|\alpha\|^2$。2 $\Rightarrow$ 3：$A = U\Lambda U^{\mathsf H} = (\Lambda^{1/2}U^{\mathsf H})^{\mathsf H}(\Lambda^{1/2}U^{\mathsf H})$。3 $\Rightarrow$ 1：$x^{\mathsf H}Ax = \|Px\|^2 > 0$（$x \ne 0$）。3 $\Leftrightarrow$ 4：$A = P^{\mathsf H}IP$。1 $\Rightarrow$ 5：左上角的 $k$ 阶子矩阵 $A_k$ 也正定（取后 $n - k$ 个分量为零的 $x$），由 2，$\det A_k$ 是正特征值之积。5 $\Rightarrow$ 6：顺序主子式非零保证 **LU 分解**存在且唯一，Hermite 性给出 $A = LDL^{\mathsf H}$，$D$ 的对角元是相邻顺序主子式之比，都为正，令 $R = D^{1/2}L^{\mathsf H}$。6 $\Rightarrow$ 3 显然。 $\square$

[第 7 章](/2.1.7)的实 Cholesky 分解写成 $A = LL^{\mathsf T}$，$L = R^{\mathsf T}$ 是下三角阵，二者是同一回事。几种判别法的代价相差很大：求特征值需要迭代算法，即使只求 Hermite 矩阵的特征值也约需 $\frac43n^3$ 次运算；逐个计算顺序主子式若用行列式展开代价极高，用一次 **Gauss 消元法**则主元之积就给出全部顺序主子式；Cholesky 分解约 $\frac13n^3$ 次运算（LU 分解的一半），失败（出现非正的主元）当且仅当 $A$ 不正定。所以实际中判定正定的标准做法就是尝试一次 Cholesky 分解。

半正定的情形有类似的结论：$A$ 半正定 $\Leftrightarrow$ 特征值全非负 $\Leftrightarrow$ $A = C^{\mathsf H}C$（$C$ 不必可逆）$\Leftrightarrow$ $A$ 复相合于 $\operatorname{diag}(I_r, O)$。但顺序主子式全非负不能推出半正定：$\operatorname{diag}(0, -1)$ 的顺序主子式为 $0, 0$，它却不是半正定的；正确的条件是所有主子式（不只是顺序主子式）都非负。

**例 13.4.1** $A = \begin{pmatrix} 2 & 1 + i \\ 1 - i & 3 \end{pmatrix}$。顺序主子式 $2 > 0$，$\det A = 6 - |1 + i|^2 = 4 > 0$，所以 $A$ 正定（特征值为 $1$ 与 $4$）。Cholesky 分解：$r_{11} = \sqrt2$，$r_{11}r_{12} = 1 + i \Rightarrow r_{12} = \frac{1 + i}{\sqrt2}$，$r_{22} = \sqrt{3 - |r_{12}|^2} = \sqrt2$，

$$
A = R^{\mathsf H}R, \qquad R = \begin{pmatrix} \sqrt2 & \frac{1 + i}{\sqrt2} \\ 0 & \sqrt2 \end{pmatrix}.
$$

## 13.5. 复矩阵的奇异值分解

[第 7 章](/2.1.7)对实矩阵证明了奇异值分解（定理 7.4.1），并讨论了 **Moore–Penrose 广义逆**与低秩逼近。把转置换成共轭转置，证明逐字照搬。

**定理 13.5.1（奇异值分解）** 设 $A \in \mathbb{C}^{m \times n}$，$\operatorname{rank}(A) = r$，则存在 $m$ 阶酉矩阵 $U$、$n$ 阶酉矩阵 $V$，使

$$
A = U\Sigma V^{\mathsf H}, \qquad \Sigma = \begin{pmatrix} \operatorname{diag}(\sigma_1, \dots, \sigma_r) & O \\ O & O \end{pmatrix}_{m \times n}, \qquad \sigma_1 \ge \cdots \ge \sigma_r > 0.
$$

$\sigma_i$ 是 $A^{\mathsf H}A$ 的正特征值的算术平方根，称为 $A$ 的**奇异值**。

**证明** $A^{\mathsf H}A$ 是半正定 Hermite 矩阵（性质 13.4.1），由定理 13.1.1 有酉矩阵 $V = (v_1, \dots, v_n)$ 使 $V^{\mathsf H}A^{\mathsf H}AV = \operatorname{diag}(\sigma_1^2, \dots, \sigma_r^2, 0, \dots, 0)$。$i > r$ 时 $\|Av_i\|^2 = 0$。令 $u_i = \frac{1}{\sigma_i}Av_i$（$i \le r$），则 $\langle u_j, u_i \rangle = \frac{1}{\sigma_i\sigma_j}v_i^{\mathsf H}A^{\mathsf H}Av_j = \frac{\sigma_j^2}{\sigma_i\sigma_j}\delta_{ij} = \delta_{ij}$。把 $u_1, \dots, u_r$ 扩充为 $\mathbb{C}^m$ 的标准正交基，得酉矩阵 $U$，且 $AV = U\Sigma$。 $\square$

**例 13.5.1** 秩为 $1$ 的矩阵 $A = uv^{\mathsf H}$（$u \in \mathbb{C}^m$，$v \in \mathbb{C}^n$ 非零）只有一个奇异值 $\sigma_1 = \|u\|\,\|v\|$，$u_1 = u / \|u\|$，$v_1 = v / \|v\|$，$A = \sigma_1u_1v_1^{\mathsf H}$，其余列任意扩充。例如 $3 \times 2$ 的全 $1$ 矩阵 $A = (1, 1, 1)^{\mathsf T}(1, 1)$，$\sigma_1 = \sqrt3 \cdot \sqrt2 = \sqrt6$，$u_1 = \frac{1}{\sqrt3}(1, 1, 1)^{\mathsf T}$，$v_1 = \frac{1}{\sqrt2}(1, 1)^{\mathsf T}$。

奇异值分解把正规矩阵的谱分解推广到任意矩阵：代价是左右用两个不同的酉矩阵。由它立即得到一般方阵的极分解。

**定理 13.5.2（极分解）** 设 $A \in M_n(\mathbb{C})$，则存在酉矩阵 $U$ 与半正定 Hermite 矩阵 $P$，使 $A = UP$。$P = (A^{\mathsf H}A)^{1/2}$ 唯一；若 $A$ 可逆，$U$ 也唯一。$A$ 正规 $\Leftrightarrow$ 可以取 $U$ 使 $UP = PU$，此时它就是定理 13.2.1 中的 $A = Re^{iM}$（$R = P$，$e^{iM} = U$）。

**证明** 由 $A = W\Sigma V^{\mathsf H}$（$W, V$ 为酉矩阵，$\Sigma$ 为非负对角阵），$A = (WV^{\mathsf H})(V\Sigma V^{\mathsf H})$，令 $U = WV^{\mathsf H}$，$P = V\Sigma V^{\mathsf H}$。由 $A^{\mathsf H}A = P^2$ 与半正定平方根的唯一性，$P$ 唯一（$(A^{\mathsf H}A)^{1/2}$ 是[第 11 章](/2.1.11)意义下的矩阵函数 $\sqrt z$，取非负分支）；$A$ 可逆时 $P$ 可逆，$U = AP^{-1}$ 唯一。若 $UP = PU$，则 $AA^{\mathsf H} = UP^2U^{\mathsf H} = P^2 = A^{\mathsf H}A$；反之由定理 13.2.1。 $\square$

同样 $A = (W\Sigma W^{\mathsf H})(WV^{\mathsf H}) = P'U$，$P' = (AA^{\mathsf H})^{1/2}$。几何上，极分解把任意线性变换拆成"沿正交方向伸缩"（$P$）与"保长度的转动或反射"（$U$），这是复数 $z = r \cdot e^{i\theta}$ 的完整推广。下面的代码由 SVD 计算极分解，并与 SciPy 的结果比较。

```python
import numpy as np
from scipy.linalg import polar

rng = np.random.default_rng(0)
A = rng.standard_normal((4, 4)) + 1j * rng.standard_normal((4, 4))
W, s, Vh = np.linalg.svd(A)                      # A = W diag(s) V^H
U = W @ Vh                                       # unitary factor
P = Vh.conj().T @ np.diag(s) @ Vh                # positive semidefinite factor
U2, P2 = polar(A)                                # SciPy: A = U2 @ P2
print(np.allclose(U, U2), np.allclose(P, P2))    # True True
print(np.allclose(U.conj().T @ U, np.eye(4)))    # True
```

奇异值分解与极分解的应用很广，这里只列几类。低秩逼近：截断 $A = \sum\sigma_iu_iv_i^{\mathsf H}$ 的前 $k$ 项是谱范数与 Frobenius 范数下最好的秩 $k$ 逼近（Eckart–Young 定理，定理 7.6.2），这是数据压缩与主成分分析的基础——中心化数据矩阵的右奇异向量就是主方向。最小二乘与广义逆：$A^+ = V\Sigma^+U^{\mathsf H}$ 给出长度最小的最小二乘解；$\sigma_1 / \sigma_r$ 衡量问题的病态程度，很小的奇异值说明矩阵"数值上"秩亏。极分解：$U$ 是在 Frobenius 范数下离 $A$ 最近的酉矩阵，用于把有误差的旋转矩阵"正交化"（正交 Procrustes 问题）；连续介质力学把形变梯度分解为旋转与伸缩，也是这个分解。量子信息中，两体纯态的 Schmidt 分解就是其系数矩阵的奇异值分解。

## 13.6. 双线性型

**定义 13.6.1** 设 $V$ 是数域 $F$ 上的线性空间。若映射 $g: V \times V \to F$ 对每个变量都是线性的，即 $g(c_1\alpha_1 + c_2\alpha_2, \beta) = c_1g(\alpha_1, \beta) + c_2g(\alpha_2, \beta)$ 且 $g(\beta, c_1\alpha_1 + c_2\alpha_2) = c_1g(\beta, \alpha_1) + c_2g(\beta, \alpha_2)$，则称 $g$ 为 $V$ 上的**双线性型**。若 $g(\alpha, \beta) = g(\beta, \alpha)$ 对一切 $\alpha, \beta$ 成立，称 $g$ 为**对称双线性型**；若 $g(\alpha, \beta) = -g(\beta, \alpha)$，称 $g$ 为**反对称双线性型**。

反对称时 $g(\alpha, \alpha) = -g(\alpha, \alpha)$，故 $g(\alpha, \alpha) = 0$。任一双线性型可以唯一地写成对称型与反对称型之和：$g(\alpha, \beta) = \frac12[g(\alpha, \beta) + g(\beta, \alpha)] + \frac12[g(\alpha, \beta) - g(\beta, \alpha)]$。复内积对第二个变量是共轭线性的，不是双线性型；它的推广是上面的 Hermite 型。下面的双线性型主要考虑实空间。

**例 13.6.1** 设 $A \in M_n(F)$，$g(\alpha, \beta) = \alpha^{\mathsf T}A\beta$ 是 $F^n$ 上的双线性型。

1. $A$ 对称时 $g$ 对称：$\alpha^{\mathsf T}A\beta = (\alpha^{\mathsf T}A\beta)^{\mathsf T} = \beta^{\mathsf T}A\alpha$；$A$ 反对称时 $g$ 反对称。
2. $A$ 是实对称正定矩阵时，$g$ 是 $\mathbb{R}^n$ 上的内积；$A = I$ 时是标准内积。
3. $\mathbb{R}^4$ 上取 $A = \operatorname{diag}(1, 1, 1, -c^2)$，$\alpha_k = (x_k, y_k, z_k, t_k)^{\mathsf T}$，得 Lorentz 型 $g(\alpha_1, \alpha_2) = x_1x_2 + y_1y_2 + z_1z_2 - c^2t_1t_2$，它是狭义相对论中时空的"度量"，$g(\alpha, \alpha)$ 可正可负可为零。
4. $\mathbb{R}^2$ 上 $g\left((a, b)^{\mathsf T}, (c, d)^{\mathsf T}\right) = ad - bc$ 是反对称型，$A = \begin{pmatrix} 0 & 1 \\ -1 & 0 \end{pmatrix}$。

**定义 13.6.2** 设 $v_1, \dots, v_n$ 是 $V$ 的基，$g$ 是双线性型。称 $G = (g(v_i, v_j))_{n \times n}$ 为 $g$ 在这组基下的矩阵（度量矩阵）。若 $G$ 可逆，则称 $g$ 为**非退化双线性型**。

**定理 13.6.1** 设 $\alpha = \sum x_iv_i$，$\beta = \sum y_jv_j$，则 $g(\alpha, \beta) = \sum_{i,j}x_iy_jg(v_i, v_j) = x^{\mathsf T}Gy$。设 $(w_1, \dots, w_n) = (v_1, \dots, v_n)P$，$g$ 在两组基下的矩阵分别为 $G_1$、$G_2$，则

$$
G_2 = P^{\mathsf T}G_1P.
$$

**证明** 第一式由双线性展开。若 $\alpha$ 在两组基下的坐标为 $x$、$x'$，则 $x = Px'$，同理 $y = Py'$，于是 $g(\alpha, \beta) = x^{\mathsf T}G_1y = x'^{\mathsf T}(P^{\mathsf T}G_1P)y'$；与 $x'^{\mathsf T}G_2y'$ 对一切 $x', y'$ 比较即得。 $\square$

所以双线性型在不同基下的矩阵是合同的，正如线性变换在不同基下的矩阵是相似的（[第 8 章](/2.1.8)小结中的对照表）。$\det G_2 = (\det P)^2\det G_1$，因此非退化与基的选取无关。非退化等价于：若 $g(\alpha, \beta) = 0$ 对一切 $\beta$ 成立，则 $\alpha = 0$；也等价于映射 $\alpha \mapsto g(\alpha, \cdot)$ 是 $V$ 到对偶空间 $V^*$ 的同构。

内积是非退化对称型，这个同构就是 Riesz 表示定理（定理 12.6.1）中的 $\Phi: u \mapsto \langle \cdot, u \rangle$。借助它可以看清伴随变换与**对偶映射** $T^{\mathsf t}: V^* \to V^*$（$T^{\mathsf t}f = f \circ T$）的关系：$T^{\mathsf t}(\Phi u) = \langle T\cdot, u \rangle = \langle \cdot, T^*u \rangle = \Phi(T^*u)$，即 $T^* = \Phi^{-1}T^{\mathsf t}\Phi$。在欧氏空间的标准正交基下二者的矩阵都是 $A^{\mathsf T}$；在酉空间中 $\Phi$ 是共轭线性的，伴随的矩阵变成 $A^{\mathsf H}$，而对偶映射的矩阵仍是 $A^{\mathsf T}$。

**例 13.6.2** $\mathcal{P}_2(\mathbb{R})$ 上 $g(f, h) = \int_0^1 f(x)h(x)\,\mathrm{d}x$ 在基 $1, x, x^2$ 下的矩阵为

$$
G = \begin{pmatrix} 1 & \frac12 & \frac13 \\ \frac12 & \frac13 & \frac14 \\ \frac13 & \frac14 & \frac15 \end{pmatrix}, \qquad g_{ij} = \int_0^1 x^{i+j-2}\,\mathrm{d}x = \frac{1}{i + j - 1}.
$$

这是 Hilbert 矩阵。$n$ 阶 Hilbert 矩阵是著名的病态矩阵，$n = 10$ 时条件数约为 $1.6 \times 10^{13}$：单项式基 $1, x, \dots, x^{n-1}$ 在 $[0, 1]$ 上"几乎线性相关"。若改用 $[0, 1]$ 上正交化得到的多项式（平移的 Legendre 多项式，参见例 12.4.2）作基，度量矩阵就是 $I$。选一组好的基，往往比改进算法更能提高计算的稳定性。

## 13.7. 对称型与反对称型的标准形

本节取 $F = \mathbb{R}$。由定理 13.6.1，给 $g$ 找一组使矩阵最简单的基，就是在合同关系下化简 $G$。

**定理 13.7.1** 设 $g$ 是 $n$ 维实空间 $V$ 上的非退化对称双线性型，则存在一组基使 $g$ 的矩阵为 $\operatorname{diag}(I_p, -I_q)$，$p + q = n$，且 $(p, q)$ 由 $g$ 唯一确定。

**证明** $g$ 在任一基下的矩阵 $G$ 是可逆实对称矩阵，由**惯性定律**（定理 7.3.3），$G$ 合同于 $\operatorname{diag}(I_p, -I_q)$，$p$ 与 $q$ 唯一；设 $P^{\mathsf T}GP = \operatorname{diag}(I_p, -I_q)$，用 $P$ 换基即可。 $\square$

$(p, q)$ 称为 $g$ 的符号（signature）。例 13.6.1 中的 Lorentz 型的符号是 $(3, 1)$。

**定理 13.7.2** 设 $g$ 是 $n$ 维实空间 $V$ 上的非退化反对称双线性型，则 $n = 2m$ 是偶数，且存在基 $e_1, f_1, \dots, e_m, f_m$，使 $g(e_i, f_i) = 1 = -g(f_i, e_i)$，其余基向量对的值为零。即 $g$ 的矩阵为

$$
\operatorname{diag}(J, \dots, J), \qquad J = \begin{pmatrix} 0 & 1 \\ -1 & 0 \end{pmatrix}.
$$

这样的基称为辛基。

**证明** 对 $n$ 归纳。取 $e_1 \ne 0$。由非退化，存在 $\beta$ 使 $g(e_1, \beta) \ne 0$，适当伸缩得 $f_1$ 使 $g(e_1, f_1) = 1$。$e_1, f_1$ 线性无关（否则 $g(e_1, f_1) = 0$）。令 $W = \operatorname{span}\{e_1, f_1\}$，$W' = \{v \mid g(v, e_1) = g(v, f_1) = 0\}$。对任意 $v$，$v - g(v, f_1)e_1 + g(v, e_1)f_1 \in W'$，所以 $V = W + W'$；而 $W \cap W' = \{0\}$（若 $ae_1 + bf_1 \in W'$，则 $g(ae_1 + bf_1, f_1) = a = 0$，$g(ae_1 + bf_1, e_1) = -b = 0$）。于是 $V = W \oplus W'$，$g$ 在 $W'$ 上仍是非退化反对称的，对 $W'$ 用归纳假设。$n = 1$ 时反对称型 $g(\alpha, \alpha) = 0$ 恒为零，不可能非退化，所以维数必为偶数。 $\square$

偶数维也可以直接看出：$G^{\mathsf T} = -G$，$\det G = \det G^{\mathsf T} = (-1)^n\det G$，$\det G \ne 0$ 时 $n$ 必为偶数。

**定义 13.7.1** 设 $g$ 是 $V$ 上的非退化双线性型。$g$ 对称时称 $(V, g)$ 为正交空间，$g$ 反对称时称 $(V, g)$ 为**辛空间**。保持 $g$ 的线性同构全体 $\operatorname{Isom}(V, g) = \{T \mid g(T\alpha, T\beta) = g(\alpha, \beta), \forall \alpha, \beta\}$ 称为 $(V, g)$ 的等距群；正交空间的等距群称为**正交群**，辛空间的等距群称为**辛群**。

$\operatorname{Isom}(V, g)$ 关于复合构成群：等距变换的复合与逆仍是等距变换。设 $T$ 在某组基下的矩阵为 $M$，$g$ 的矩阵为 $G$，则 $T \in \operatorname{Isom}(V, g) \Leftrightarrow M^{\mathsf T}GM = G$。取标准形的基：

| $g$ 的矩阵 $G$ | 等距群 | 条件 |
|---|---|---|
| $I_n$（内积） | 正交群 $O(n)$ | $M^{\mathsf T}M = I$，即[上一章](/2.1.12)的正交变换 |
| $\operatorname{diag}(I_p, -I_q)$ | 不定正交群 $O(p, q)$ | $M^{\mathsf T}\operatorname{diag}(I_p, -I_q)M = \operatorname{diag}(I_p, -I_q)$ |
| $\operatorname{diag}(J, \dots, J)$ | 辛群 $Sp(2m, \mathbb{R})$ | $M^{\mathsf T}GM = G$ |

**例 13.7.1** 在 $\mathbb{R}^4$ 上取例 13.6.1 的 Lorentz 型。设 $0 < v < c$，$E_0 = \sqrt{1 - v^2/c^2}$，

$$
T: (x, y, z, t)^{\mathsf T} \mapsto (x', y', z', t')^{\mathsf T}, \qquad x' = \frac{x - vt}{E_0}, \quad y' = y, \quad z' = z, \quad t' = \frac{t - vx/c^2}{E_0}.
$$

直接计算 $(x - vt)^2 - c^2\left(t - \frac{vx}{c^2}\right)^2 = \left(1 - \frac{v^2}{c^2}\right)(x^2 - c^2t^2)$，除以 $E_0^2$ 得 $x'^2 - c^2t'^2 = x^2 - c^2t^2$，所以 $g(T\alpha, T\alpha) = g(\alpha, \alpha)$；由对称双线性型的极化，$g(T\alpha_1, T\alpha_2) = g(\alpha_1, \alpha_2)$。$T$ 是 Lorentz 变换，Lorentz 型的等距群 $O(3, 1)$ 称为 Lorentz 群（Lorentz group）。

**例 13.7.2** $\mathbb{R}^2$ 上的有向面积 $g(\alpha, \beta) = \det(\alpha, \beta)$ 是辛型。对 2 阶实矩阵有恒等式 $M^{\mathsf T}JM = (\det M)J$，所以 $M \in Sp(2, \mathbb{R})$ $\Leftrightarrow$ $\det M = 1$：二维的辛变换就是保持有向面积的线性变换。高维时辛条件比保持体积强得多。Hamilton 力学的相空间带有自然的辛型，系统随时间的演化保持这个辛型。

在等距群中取单参数子群 $e^{tX}$ 并在 $t = 0$ 处求导，条件 $M^{\mathsf T}GM = G$ 变成 $X^{\mathsf T}G + GX = O$。$G = I$ 时得到反对称矩阵 $\mathfrak{so}(n)$，$G$ 为辛矩阵时得到 $\mathfrak{sp}(2m)$，它们都是 [1.3.5](/1.3.5) 中的**典型李代数**。

## 13.8. 张量

$V$ 上全体双线性型的集合 $L(V, V; F)$ 关于函数的加法与数乘构成 $F$ 上的线性空间。由定理 13.6.1，取定基后 $g \mapsto G$ 是 $L(V, V; F)$ 到 $M_n(F)$ 的线性同构，所以 $\dim L(V, V; F) = n^2$。它的一组自然的基可以由对偶空间构造。

**定义 13.8.1** 设 $\varphi_1, \varphi_2 \in V^*$。称双线性型 $(v_1, v_2) \mapsto \varphi_1(v_1)\varphi_2(v_2)$ 为 $\varphi_1$ 与 $\varphi_2$ 的**张量积**，记作 $\varphi_1 \otimes \varphi_2$。

**定理 13.8.1** 设 $v_1, \dots, v_n$ 是 $V$ 的基，$v_1^*, \dots, v_n^*$ 是**对偶基**。则 $\{v_i^* \otimes v_j^* \mid 1 \le i, j \le n\}$ 是 $L(V, V; F)$ 的基，且任一双线性型

$$
g = \sum_{i,j=1}^n g(v_i, v_j)\,v_i^* \otimes v_j^*.
$$

**证明** $(v_i^* \otimes v_j^*)(v_k, v_l) = \delta_{ik}\delta_{jl}$，所以 $v_i^* \otimes v_j^*$ 在基 $v_1, \dots, v_n$ 下的矩阵是矩阵单位 $E_{ij}$（第 $(i, j)$ 元为 $1$，其余为 $0$）。$\{E_{ij}\}$ 是 $M_n(F)$ 的基，经同构 $g \mapsto G$ 即得结论；展开式两边在每个 $(v_k, v_l)$ 上取值相同。 $\square$

更一般地，对每个变量都线性的映射 $g: V \times \cdots \times V \to F$（$k$ 个 $V$）称为 $k$ 重线性型。

**定义 13.8.2** 设 $k \ge 1$，对每个变量都线性的映射 $g: V^k \to F$ 称为 $V$ 上的 $k$ 阶**多重线性型**（$k$ 阶张量）。

与 $k = 2$ 的情形一样，$\{v_{i_1}^* \otimes \cdots \otimes v_{i_k}^*\}$ 是 $k$ 重线性型全体的基，维数为 $n^k$，$g$ 的坐标是 $k$ 维数组 $g_{i_1\cdots i_k} = g(v_{i_1}, \dots, v_{i_k})$。换基 $(w_1, \dots, w_n) = (v_1, \dots, v_n)P$ 时，每个指标都按 $P$ 变换：

$$
g'_{j_1\cdots j_k} = \sum_{i_1, \dots, i_k} g_{i_1\cdots i_k}\,p_{i_1j_1}\cdots p_{i_kj_k},
$$

$k = 2$ 时就是 $G' = P^{\mathsf T}GP$。于是"数 $\to$ 向量 $\to$ 矩阵 $\to$ 张量"有了统一的解释：数是 $0$ 阶，线性函数是 $1$ 阶，双线性型是 $2$ 阶，$k$ 重线性型是 $k$ 阶。$n$ 维空间上的行列式 $\det(\alpha_1, \dots, \alpha_n)$ 是一个 $n$ 重线性型，并且是交错的（交换两个变量变号），[第 5 章](/2.1.5)的公理化定义说的正是这一点。机器学习中所说的"张量"通常就是这样的多维数组，即取定基以后多重线性对象的坐标。

## 小结

| 主题 | 结论 |
|---|---|
| Hermite 矩阵 | 特征值为实数，可酉对角化为实对角阵；正规 + 实特征值 $\Leftrightarrow$ Hermite（定理 13.1.1） |
| 极分解 | 正规矩阵 $A = Re^{iM}$，$R$ 半正定、$M$ Hermite、可交换（定理 13.2.1）；一般方阵 $A = UP$，$P = (A^{\mathsf H}A)^{1/2}$（定理 13.5.2） |
| Hermite 二次型 | $f = x^{\mathsf H}Ax$ 取实值；换元 $x = Py$ 时矩阵复相合 $P^{\mathsf H}AP$；规范形与惯性定律（定理 13.3.1） |
| 正定 Hermite 矩阵 | 特征值全正 $\Leftrightarrow$ $A = P^{\mathsf H}P$ $\Leftrightarrow$ 顺序主子式全正 $\Leftrightarrow$ $A = R^{\mathsf H}R$（定理 13.4.1） |
| 复奇异值分解 | $A = U\Sigma V^{\mathsf H}$（定理 13.5.1）；应用于低秩逼近、广义逆、主成分分析 |
| 双线性型 | $g(\alpha, \beta) = x^{\mathsf T}Gy$，换基 $G_2 = P^{\mathsf T}G_1P$（定理 13.6.1）；非退化 $\Leftrightarrow$ $\det G \ne 0$ |
| 标准形 | 对称：$\operatorname{diag}(I_p, -I_q)$；反对称：辛基，维数为偶数（定理 13.7.1、13.7.2） |
| 等距群 | $M^{\mathsf T}GM = G$：正交群、Lorentz 群、辛群 |
| 张量 | $\{v_i^* \otimes v_j^*\}$ 是双线性型空间的基，维数 $n^2$（定理 13.8.1）；$k$ 重线性型的维数为 $n^k$ |

三种等价关系各自对应一类对象：相似 $P^{-1}AP$ 对应线性变换，合同 $P^{\mathsf T}GP$ 对应双线性型，复相合 $P^{\mathsf H}GP$ 对应 Hermite 型。在标准正交基下换基矩阵是正交（酉）矩阵，三者合而为一，这就是谱定理能同时化简线性变换与二次型的原因。课程至此从矩阵计算出发，经过线性空间与线性映射，到达了多重线性代数的入口。
