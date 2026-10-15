---
title: 逆矩阵、分块矩阵与 LU 分解
---

上一章把线性方程组的求解归结为消元。本章用矩阵乘法重新表述消元：每一次初等行变换都是左乘一个初等矩阵，于是"能否消元成单位矩阵"就成为"矩阵是否可逆"，求逆矩阵与解方程组本质上是同一个问题。随后把矩阵按块看待，块与块之间的运算规则与元素之间的相同；分块消元给出 Schur 补和 Sherman–Morrison–Woodbury 公式，它们说明低秩修改后的逆矩阵可以廉价地更新。最后把 Gauss 消元的全过程记录成矩阵分解 $A = LU$，以及它的变形 $LDU$ 与 $PLU$ 分解：分解一次、反复使用，是数值线性代数"标准化求解"的典型做法。

本章用到的映射概念（**单射**、**满射**、**双射**、左逆与右逆）来自 [1.2.3](/1.2.3)，**等价关系**来自 [1.2.2](/1.2.2)。可逆矩阵的全体构成 1.3 中的**一般线性群**。[第 3 章](/2.1.3)将用秩把本章的可逆条件推广到一般的 $m \times n$ 矩阵。

## 2.1. 初等矩阵

消元法中的三类初等行变换都是 $\mathbb{R}^n$ 上的线性变换，按定义 1.3.2，它们的表示矩阵就是对 $I_n$ 的各列（即对 $I_n$ 本身）做同样的变换。

**定义 2.1.1（初等矩阵）** 对单位矩阵 $I_n$ 做一次初等变换得到的矩阵统称为**初等矩阵**，共三类：

1. 对换矩阵 $P_{ij}$：互换 $I_n$ 的第 $i, j$ 行（也是互换第 $i, j$ 列）；
2. 倍乘矩阵 $E_{ii;k}$（$k \ne 0$）：$I_n$ 的第 $i$ 行乘 $k$（也是第 $i$ 列乘 $k$）；
3. 倍加矩阵 $E_{ji;k}$：把 $I_n$ 的第 $i$ 行的 $k$ 倍加到第 $j$ 行（也是把第 $j$ 列的 $k$ 倍加到第 $i$ 列），即 $E_{ji;k} = I_n + k\boldsymbol{e}_j\boldsymbol{e}_i^{\mathsf T}$。

以 $n = 3$ 为例，

$$
P_{12} = \begin{bmatrix} 0 & 1 & 0 \\ 1 & 0 & 0 \\ 0 & 0 & 1 \end{bmatrix}, \qquad
E_{22;k} = \begin{bmatrix} 1 & 0 & 0 \\ 0 & k & 0 \\ 0 & 0 & 1 \end{bmatrix}, \qquad
E_{31;k} = \begin{bmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ k & 0 & 1 \end{bmatrix}.
$$

初等矩阵的转置仍是同类初等矩阵：$P_{ij}^{\mathsf T} = P_{ij}$，$E_{ii;k}^{\mathsf T} = E_{ii;k}$，$E_{ji;k}^{\mathsf T} = E_{ij;k}$。

**命题 2.1.1（左行右列）** 设 $T$ 是由 $I_m$ 经过某一初等行变换得到的矩阵，则对任意 $m \times n$ 矩阵 $A$，$TA$ 等于对 $A$ 做同一初等行变换的结果。设 $T$ 是由 $I_n$ 经过某一初等列变换得到的矩阵，则 $AT$ 等于对 $A$ 做同一初等列变换的结果。

**证明** $T$ 是该行变换（一个线性变换）的表示矩阵，所以 $TA = [T\boldsymbol{a}_1\ \cdots\ T\boldsymbol{a}_n]$ 就是对 $A$ 的每一列做这一变换，也就是对 $A$ 做这一行变换。列的情形：$AT = (T^{\mathsf T}A^{\mathsf T})^{\mathsf T}$，而 $T^{\mathsf T}$ 是由 $I_n$ 经过相应初等行变换得到的，对 $A^{\mathsf T}$ 做行变换就是对 $A$ 做列变换。$\square$

例如，$P_{ij}A$ 互换 $A$ 的第 $i, j$ 行，$AP_{ij}$ 互换 $A$ 的第 $i, j$ 列；$E_{ji;k}A$ 把 $A$ 的第 $i$ 行的 $k$ 倍加到第 $j$ 行，$AE_{ji;k}$ 把 $A$ 的第 $j$ 列的 $k$ 倍加到第 $i$ 列。于是对 $A$ 做 Gauss（–Jordan）消元，就是找一列初等矩阵 $E_1, \dots, E_t$，使 $E_t\cdots E_2E_1A$ 是（行简化）阶梯形。

**例 2.1.1** 例 1.6.1 的消元过程写成矩阵乘法为

$$
\begin{bmatrix} 1 & -1 \\ 0 & 1 \end{bmatrix}\begin{bmatrix} 1 & 0 \\ 0 & \frac12 \end{bmatrix}\begin{bmatrix} 1 & 0 \\ -2 & 1 \end{bmatrix}\begin{bmatrix} 1 & 1 & 8 \\ 2 & 4 & 22 \end{bmatrix} = \begin{bmatrix} 1 & 0 & 5 \\ 0 & 1 & 3 \end{bmatrix},
$$

依次是 $E_{21;-2}$、$E_{22;1/2}$、$E_{12;-1}$。

## 2.2. 可逆映射与可逆矩阵

**定义 2.2.1（可逆映射）** 设 $f\colon X \to Y$ 是映射。若存在映射 $g\colon Y \to X$ 使得 $f \circ g = \mathrm{id}_Y$ 且 $g \circ f = \mathrm{id}_X$，则称 $f$ 可逆，称 $g$ 是 $f$ 的逆映射。

**命题 2.2.1** 可逆映射的逆映射唯一，记为 $f^{-1}$。

**证明** 设 $g, h$ 都是 $f$ 的逆映射，则 $g = \mathrm{id}_X \circ g = (h \circ f) \circ g = h \circ (f \circ g) = h \circ \mathrm{id}_Y = h$。$\square$

由 [1.2.3 的定理 3.2.8](/1.2.3#thm-3.2.8)（$X \ne \varnothing$）：$f$ 是**单射**当且仅当存在 $g$ 使 $g \circ f = \mathrm{id}_X$（$g$ 是 $f$ 的**左逆**）；$f$ 是**满射**当且仅当存在 $g$ 使 $f \circ g = \mathrm{id}_Y$（**右逆**）；$f$ 是**双射**（一一对应）当且仅当 $f$ 可逆。

**定义 2.2.2（可逆线性变换）** 设 $\boldsymbol{A}, \boldsymbol{B}$ 是 $\mathbb{R}^n$ 上的线性变换。若 $\boldsymbol{A} \circ \boldsymbol{B} = \boldsymbol{B} \circ \boldsymbol{A} = I$，则称 $\boldsymbol{A}$ 和 $\boldsymbol{B}$ 是可逆变换，$\boldsymbol{B} = \boldsymbol{A}^{-1}$ 是 $\boldsymbol{A}$ 的逆变换。

**命题 2.2.2** 若 $\boldsymbol{A}\colon \mathbb{R}^n \to \mathbb{R}^n$ 是可逆的线性变换，则逆映射 $\boldsymbol{A}^{-1}$ 也是线性变换。

**证明** 设 $\boldsymbol{y} = \boldsymbol{A}(\boldsymbol{x})$，$\boldsymbol{y}' = \boldsymbol{A}(\boldsymbol{x}')$，$k \in \mathbb{R}$。由 $\boldsymbol{A}$ 线性，$\boldsymbol{A}(\boldsymbol{x} + \boldsymbol{x}') = \boldsymbol{y} + \boldsymbol{y}'$，$\boldsymbol{A}(k\boldsymbol{x}) = k\boldsymbol{y}$，所以 $\boldsymbol{A}^{-1}(\boldsymbol{y} + \boldsymbol{y}') = \boldsymbol{x} + \boldsymbol{x}' = \boldsymbol{A}^{-1}(\boldsymbol{y}) + \boldsymbol{A}^{-1}(\boldsymbol{y}')$，$\boldsymbol{A}^{-1}(k\boldsymbol{y}) = k\boldsymbol{x} = k\boldsymbol{A}^{-1}(\boldsymbol{y})$。$\square$

对应到表示矩阵，就得到可逆矩阵的定义。

**定义 2.2.3（可逆矩阵）** 设 $A$ 是 $n$ 阶方阵。若存在 $n$ 阶方阵 $B$ 使得 $AB = BA = I_n$，则称 $A$ 是**可逆矩阵**（非奇异矩阵），称 $B$ 为 $A$ 的**逆矩阵**，记为 $A^{-1}$。不可逆的方阵称为**奇异矩阵**。

逆矩阵若存在则唯一：若 $B, \tilde{B}$ 都是 $A$ 的逆，则 $B = BI_n = B(A\tilde{B}) = (BA)\tilde{B} = \tilde{B}$。线性变换 $\boldsymbol{x} \mapsto A\boldsymbol{x}$ 可逆当且仅当矩阵 $A$ 可逆，此时 $\boldsymbol{A}^{-1}$ 的表示矩阵就是 $A^{-1}$。对正整数 $k$ 和可逆矩阵 $A$，定义负整数幂 $A^{-k} = (A^{-1})^k$。

**例 2.2.1**

- $I_n$ 可逆，$I_n^{-1} = I_n$；零矩阵不可逆，因为 $OB = O \ne I_n$。
- 初等矩阵都可逆，逆矩阵对应逆变换（命题 1.6.1）：$P_{ij}^{-1} = P_{ij}$，$E_{ii;k}^{-1} = E_{ii;1/k}$，$E_{ji;k}^{-1} = E_{ji;-k}$。例如 $\begin{bmatrix} 1 & 0 \\ k & 1 \end{bmatrix}^{-1} = \begin{bmatrix} 1 & 0 \\ -k & 1 \end{bmatrix}$。
- 对角矩阵 $D = \operatorname{diag}(d_1, \dots, d_n)$ 可逆当且仅当对角元素都不为零，此时 $D^{-1} = \operatorname{diag}(d_1^{-1}, \dots, d_n^{-1})$。若某个 $d_i = 0$，则对任意 $B$，$DB$ 的第 $i$ 行全为零，不可能等于 $I_n$。

**命题 2.2.3（可逆矩阵的性质）** 设 $A, B$ 是 $n$ 阶可逆矩阵，则

1. $A^{-1}$ 可逆，且 $(A^{-1})^{-1} = A$；
2. $A^{\mathsf T}$ 可逆，且 $(A^{\mathsf T})^{-1} = (A^{-1})^{\mathsf T}$，记为 $A^{-\mathsf T}$；
3. $AB$ 可逆，且 $(AB)^{-1} = B^{-1}A^{-1}$。

**证明** 第 1 条由定义的对称性得到。第 2 条：$(A^{-1})^{\mathsf T}A^{\mathsf T} = (AA^{-1})^{\mathsf T} = I$，$A^{\mathsf T}(A^{-1})^{\mathsf T} = (A^{-1}A)^{\mathsf T} = I$。第 3 条：$(B^{-1}A^{-1})(AB) = B^{-1}B = I$，$(AB)(B^{-1}A^{-1}) = AA^{-1} = I$。$\square$

一般地，$(A_1A_2\cdots A_k)^{-1} = A_k^{-1}\cdots A_2^{-1}A_1^{-1}$，特别地 $A^{-k} = (A^{-1})^k = (A^k)^{-1}$。因此全体 $n$ 阶实可逆矩阵在矩阵乘法下构成**群**，即**一般线性群** $\mathrm{GL}(n, \mathbb{R})$。

## 2.3. 可逆的等价条件与求逆

**定理 2.3.1（可逆的等价条件）** 设 $A$ 是 $n$ 阶方阵，以下叙述等价：

1. $A$ 可逆；
2. 对任意 $\boldsymbol{b} \in \mathbb{R}^n$，线性方程组 $A\boldsymbol{x} = \boldsymbol{b}$ 有唯一解；
3. 齐次线性方程组 $A\boldsymbol{x} = \boldsymbol{0}$ 只有零解；
4. $A$ 化成的阶梯形有 $n$ 个主元；
5. $A$ 的行简化阶梯形是 $I_n$；
6. $A$ 是有限个初等矩阵的乘积。

**证明** 采用轮转证法。$1 \Rightarrow 2$：$A$ 可逆，则 $\boldsymbol{x} \mapsto A\boldsymbol{x}$ 是可逆变换，因而是双射，每个 $\boldsymbol{b}$ 恰有一个原像（$\boldsymbol{x} = A^{-1}\boldsymbol{b}$）。$2 \Rightarrow 3$：取 $\boldsymbol{b} = \boldsymbol{0}$。$3 \Rightarrow 4$：由推论 1.8.1，只有零解当且仅当阶梯数等于 $n$。$4 \Rightarrow 5$：$n$ 阶方阵有 $n$ 个主元时，每一列都是主列，行简化后就是 $I_n$。$5 \Rightarrow 6$：存在初等矩阵 $E_1, \dots, E_t$ 使 $E_t\cdots E_1A = I_n$，于是 $A = E_1^{-1}\cdots E_t^{-1}$，而初等矩阵的逆仍是初等矩阵。$6 \Rightarrow 1$：初等矩阵可逆，可逆矩阵的乘积可逆（命题 2.2.3）。$\square$

**命题 2.3.1** 设 $A, B$ 是 $n$ 阶方阵。

1. 若 $BA = I_n$ 或 $AB = I_n$，则 $A, B$ 都可逆，且 $A^{-1} = B$，$B^{-1} = A$；
2. $AB$ 可逆当且仅当 $A, B$ 都可逆。

**证明** 1. 若 $BA = I_n$，则由 $A\boldsymbol{x} = \boldsymbol{0}$ 得 $\boldsymbol{x} = BA\boldsymbol{x} = \boldsymbol{0}$，由定理 2.3.1 $A$ 可逆，且 $B = BAA^{-1} = A^{-1}$；$AB = I_n$ 时对 $B$ 用同样的论证。2. 必要性：若 $AB$ 可逆，由 $B\boldsymbol{x} = \boldsymbol{0}$ 得 $AB\boldsymbol{x} = \boldsymbol{0}$，故 $\boldsymbol{x} = \boldsymbol{0}$，$B$ 可逆；于是 $A = (AB)B^{-1}$ 也可逆。充分性即命题 2.2.3。$\square$

所以对方阵验证逆矩阵只需验证一边。这对映射一般不成立（单射有左逆而未必有右逆），方阵的特殊之处在于定理 2.3.1 中条件 3（单射）就能推出条件 2（双射）。

定理 2.3.1 的证明同时给出了求逆的方法：若 $E_t\cdots E_1A = I_n$，记 $E = E_t\cdots E_1$，则 $E = A^{-1}$。把同样的初等行变换施加在 $I_n$ 上，就得到 $E$。

**算法 2.3.1（Gauss–Jordan 求逆）** 把 $A$ 与 $I_n$ 并排成 $n \times 2n$ 矩阵 $[A\ I_n]$，用 Gauss–Jordan 消元把左半部分化成行简化阶梯形。若左半部分化成 $I_n$，则

$$
E[A\ I_n] = [I_n\ E] = [I_n\ A^{-1}];
$$

若左半部分的主元少于 $n$ 个，则 $A$ 不可逆。同样的方法求解矩阵方程 $AX = B$：$[A\ B] \to [I_n\ A^{-1}B]$。

**例 2.3.1** 求 $A = \begin{bmatrix} 1 & 1 \\ 2 & 4 \end{bmatrix}$ 的逆：

$$
\begin{bmatrix} 1 & 1 & 1 & 0 \\ 2 & 4 & 0 & 1 \end{bmatrix} \to
\begin{bmatrix} 1 & 1 & 1 & 0 \\ 0 & 2 & -2 & 1 \end{bmatrix} \to
\begin{bmatrix} 1 & 1 & 1 & 0 \\ 0 & 1 & -1 & \frac12 \end{bmatrix} \to
\begin{bmatrix} 1 & 0 & 2 & -\frac12 \\ 0 & 1 & -1 & \frac12 \end{bmatrix},
\qquad A^{-1} = \begin{bmatrix} 2 & -\frac12 \\ -1 & \frac12 \end{bmatrix}.
$$

求逆约需 $2n^3$ 次浮点运算，是 Gauss 消元的 $3$ 倍（见 2.10 节的图）。所以解方程组 $A\boldsymbol{x} = \boldsymbol{b}$ 时不应先求 $A^{-1}$ 再算 $A^{-1}\boldsymbol{b}$，而应直接消元或用 LU 分解。

三角矩阵的结构在乘法与求逆下保持，这是 LU 分解的基础。

**性质 2.3.1** 两个 $n$ 阶上三角矩阵的乘积是上三角矩阵，其对角元素是两个因子对应对角元素的乘积。下三角矩阵、单位上（下）三角矩阵有同样的性质。

**证明** 设 $U = [u_{ij}]$，$V = [v_{ij}]$ 是上三角矩阵，$(UV)_{ik} = \sum_j u_{ij}v_{jk}$ 中非零项要求 $i \le j \le k$。所以 $i > k$ 时 $(UV)_{ik} = 0$，$i = k$ 时只剩 $u_{ii}v_{ii}$。$\square$

**命题 2.3.2（三角矩阵的逆）** 上三角矩阵可逆当且仅当它的对角元素都不为零。此时逆矩阵也是上三角矩阵，其对角元素是原矩阵对应对角元素的倒数。下三角矩阵有同样的性质。

**证明** 设 $U$ 是 $n$ 阶上三角矩阵。若对角元素都不为零，$U$ 本身是有 $n$ 个主元的阶梯形，由定理 2.3.1 可逆；$U^{-1}$ 的第 $j$ 列是 $U\boldsymbol{x} = \boldsymbol{e}_j$ 的解，用回代法求解时 $x_n = \cdots = x_{j+1} = 0$，$x_j = 1/u_{jj}$，所以 $U^{-1}$ 是上三角矩阵，对角元素为 $1/u_{jj}$。反之，若某个 $u_{kk} = 0$，则 $U$ 的前 $k$ 列只在前 $k-1$ 行有非零元素，齐次方程组 $[\boldsymbol{u}_1\ \cdots\ \boldsymbol{u}_k]\boldsymbol{y} = \boldsymbol{0}$ 实际上只有 $k-1$ 个方程，由推论 1.8.2 有非零解 $\boldsymbol{y}$，于是 $\boldsymbol{x} = [\boldsymbol{y}^{\mathsf T}\ \boldsymbol{0}^{\mathsf T}]^{\mathsf T} \ne \boldsymbol{0}$ 满足 $U\boldsymbol{x} = \boldsymbol{0}$，$U$ 不可逆。下三角矩阵取转置即可。$\square$

**定义 2.3.1（置换矩阵）** 单位矩阵经过一系列对换行变换得到的矩阵称为**置换矩阵**，即一系列对换矩阵的乘积。

**命题 2.3.3** 置换矩阵有如下性质：

1. 单位矩阵经一系列对换列变换得到的矩阵也是置换矩阵；
2. 置换矩阵就是把单位矩阵的行（或列）按某种次序重新排列得到的矩阵，每行、每列恰有一个 $1$；
3. $n$ 阶置换矩阵共有 $n!$ 个，与 $n$ 元**置换**一一对应；
4. 置换矩阵的乘积是置换矩阵；
5. 置换矩阵 $P$ 可逆，且 $P^{-1} = P^{\mathsf T}$，也是置换矩阵。

**证明** 对换列与对换行得到的矩阵相同（$P_{ij}$ 是对称的），故 1 成立。任意排列都可以由一系列对换得到，故 2、3 成立。4 由定义即得。5：$P$ 的列是互不相同的 $\boldsymbol{e}_{\sigma(1)}, \dots, \boldsymbol{e}_{\sigma(n)}$，$P^{\mathsf T}P$ 的 $(i, j)$ 元是 $\boldsymbol{e}_{\sigma(i)}^{\mathsf T}\boldsymbol{e}_{\sigma(j)}$，即 $I_n$；$P^{\mathsf T}$ 的行是 $P$ 的列，仍是 $I_n$ 的行的一个排列。$\square$

**定义 2.3.2（对角占优矩阵）** 若方阵 $A = [a_{ij}]_{n \times n}$ 对每个 $i = 1, \dots, n$ 都满足 $|a_{ii}| > \sum_{j \ne i}|a_{ij}|$，则称 $A$ 为（行）**对角占优矩阵**。

**命题 2.3.4** 对角占优矩阵一定可逆。

**证明** 只需证明 $A\boldsymbol{x} = \boldsymbol{0}$ 只有零解。用反证法，设 $\boldsymbol{x} \ne \boldsymbol{0}$ 满足 $A\boldsymbol{x} = \boldsymbol{0}$。取绝对值最大的分量 $x_i$，不妨设 $|x_i| = 1$，则 $|x_j| \le 1$。由第 $i$ 个方程 $a_{ii}x_i = -\sum_{j \ne i}a_{ij}x_j$，

$$
|a_{ii}| = |a_{ii}x_i| = \Bigl|\sum_{j \ne i}a_{ij}x_j\Bigr| \le \sum_{j \ne i}|a_{ij}||x_j| \le \sum_{j \ne i}|a_{ij}| < |a_{ii}|,
$$

矛盾。$\square$

对角占优矩阵常见于微分方程的离散化，它的可逆性只需检查元素的大小，不必消元。

## 2.4. 左相抵与等价关系

**定义 2.4.1（左相抵）** 若矩阵 $A$ 可以经过一系列初等行变换化成矩阵 $B$，则称 $A$ 与 $B$ **左相抵**。

**命题 2.4.1** 两个 $m \times n$ 矩阵 $A, B$ 左相抵，当且仅当存在 $m$ 阶可逆矩阵 $P$ 使得 $PA = B$。

**证明** $A$ 经过一系列初等行变换得到 $B$，当且仅当存在 $m$ 阶初等矩阵 $P_1, \dots, P_s$ 使 $P_s\cdots P_1A = B$；由定理 2.3.1，可逆矩阵恰是初等矩阵的乘积。$\square$

左相抵是 $\mathbb{R}^{m \times n}$ 上的**等价关系**：$A = I_mA$（自反）；$PA = B \Rightarrow A = P^{-1}B$（对称）；$PA = B$，$QB = C \Rightarrow (QP)A = C$（传递）。一般地，对集合 $S$ 上的等价关系，与元素 $a$ 等价的全体元素构成 $a$ 的**等价类**；两个不同的等价类不相交，$S$ 是全体等价类的无交并。把元素变成与它等价的元素的过程称为等价变换；同一等价类的元素共有的属性称为这个等价关系的不变量；同一等价类中形式最简单、性质最好的元素称为标准形。

对左相抵而言，初等行变换是等价变换；以左相抵的矩阵为系数矩阵的齐次方程组（或为增广矩阵的方程组）解集相同，这是不变量；行简化阶梯形是标准形，称为左相抵标准形（[第 3 章](/2.1.3)证明它唯一）。从这个角度看，Gauss–Jordan 消元就是把增广矩阵化成左相抵的标准形，从标准形上直接读出不变量——方程组的解集。引入等价关系、再用等价变换化简问题，是贯穿本课程的方法：后面还会遇到矩阵的相抵（[第 3 章](/2.1.3)）、相似（[第 6 章](/2.1.6)）与合同（[第 7 章](/2.1.7)）。

## 2.5. 分块矩阵

矩阵运算中常把矩阵写成列向量或行向量并排的形式。设 $A = [\boldsymbol{a}_1\ \cdots\ \boldsymbol{a}_m]$ 是 $\ell \times m$ 矩阵，行向量为 $\tilde{\boldsymbol{a}}_i^{\mathsf T}$；$B$ 是 $m \times n$ 矩阵，列向量为 $\boldsymbol{b}_k$，行向量为 $\tilde{\boldsymbol{b}}_j^{\mathsf T}$。则

$$
AB = \begin{bmatrix} \tilde{\boldsymbol{a}}_1^{\mathsf T}\boldsymbol{b}_1 & \cdots & \tilde{\boldsymbol{a}}_1^{\mathsf T}\boldsymbol{b}_n \\ \vdots & & \vdots \\ \tilde{\boldsymbol{a}}_\ell^{\mathsf T}\boldsymbol{b}_1 & \cdots & \tilde{\boldsymbol{a}}_\ell^{\mathsf T}\boldsymbol{b}_n \end{bmatrix} = [\boldsymbol{a}_1\ \cdots\ \boldsymbol{a}_m]\begin{bmatrix} \tilde{\boldsymbol{b}}_1^{\mathsf T} \\ \vdots \\ \tilde{\boldsymbol{b}}_m^{\mathsf T} \end{bmatrix} = \boldsymbol{a}_1\tilde{\boldsymbol{b}}_1^{\mathsf T} + \cdots + \boldsymbol{a}_m\tilde{\boldsymbol{b}}_m^{\mathsf T}.
$$

前者是"行乘列"（内积形式），后者是"列乘行"（$AB$ 写成 $m$ 个外积 $\boldsymbol{a}_j\tilde{\boldsymbol{b}}_j^{\mathsf T}$ 之和）。把向量作为基本单元，乘法规则与元素的规则形式相同。进一步把矩阵横竖切成块：

**定义 2.5.1（分块矩阵）** 用若干条横线和竖线把矩阵分割成若干子矩阵（块），把矩阵看作以这些块为元素的矩阵，称为**分块矩阵**。把 $A$ 分成 $r \times s$ 块、$B$ 分成 $s \times t$ 块：

$$
A = \begin{bmatrix} A_{11} & \cdots & A_{1s} \\ \vdots & & \vdots \\ A_{r1} & \cdots & A_{rs} \end{bmatrix}, \qquad B = \begin{bmatrix} B_{11} & \cdots & B_{1t} \\ \vdots & & \vdots \\ B_{s1} & \cdots & B_{st} \end{bmatrix},
$$

其中 $A_{ij}$ 是 $\ell_i \times m_j$ 矩阵，$B_{jk}$ 是 $m_j \times n_k$ 矩阵。

**命题 2.5.1（分块运算）** 在上述分块下，$AB$ 的 $(i, k)$ 块为 $\sum_{j=1}^s A_{ij}B_{jk}$；$A^{\mathsf T}$ 的 $(j, i)$ 块为 $A_{ij}^{\mathsf T}$。

分块乘法要求 $B$ 的行分块方式与 $A$ 的列分块方式相同，并且每一项 $A_{ij}B_{jk}$ 中左边的块一定在左边（块之间的乘法不可交换）；转置时块的位置要对调，块本身也要转置。按元素公式逐项比较即可验证。分块的线性运算是显然的；分块只是矩阵运算的另一种表示方法。例如 $2 \times 2$ 分块时，

$$
\begin{bmatrix} A_{11} & A_{12} \\ A_{21} & A_{22} \end{bmatrix}\begin{bmatrix} B_{11} & B_{12} \\ B_{21} & B_{22} \end{bmatrix} = \begin{bmatrix} A_{11}B_{11} + A_{12}B_{21} & A_{11}B_{12} + A_{12}B_{22} \\ A_{21}B_{11} + A_{22}B_{21} & A_{21}B_{12} + A_{22}B_{22} \end{bmatrix}, \qquad
\begin{bmatrix} A_{11} & A_{12} \\ A_{21} & A_{22} \end{bmatrix}^{\mathsf T} = \begin{bmatrix} A_{11}^{\mathsf T} & A_{21}^{\mathsf T} \\ A_{12}^{\mathsf T} & A_{22}^{\mathsf T} \end{bmatrix}.
$$

**例 2.5.1** 同一个矩阵可以有多种分块方式。对

$$
M = \begin{bmatrix} 1 & 1 & 0 & 0 \\ 1 & 1 & 0 & 0 \\ 0 & 0 & 2 & 2 \\ 0 & 0 & 2 & 2 \end{bmatrix},
$$

按前两行、前两列切开得到 $\begin{bmatrix} A & O \\ O & B \end{bmatrix}$，其中 $A = \begin{bmatrix} 1 & 1 \\ 1 & 1 \end{bmatrix}$，$B = 2A$；按第一行、第一列切开则得不到这种对角结构。好的分块应当暴露矩阵的结构。

**定义 2.5.2（分块对角矩阵）** 若矩阵 $A$ 的分块形如

$$
A = \begin{bmatrix} A_1 & & & \\ & A_2 & & \\ & & \ddots & \\ & & & A_s \end{bmatrix},
$$

非对角位置的块都是零矩阵，则称 $A$ 为**分块对角矩阵**，$A_1, \dots, A_s$ 称为对角块。对角块本身不必是对角矩阵，也不必是方阵。

把 $\boldsymbol{x}$ 按 $A$ 的列分块方式分成 $\boldsymbol{x}_1, \dots, \boldsymbol{x}_s$，则 $A\boldsymbol{x} = [(A_1\boldsymbol{x}_1)^{\mathsf T}\ \cdots\ (A_s\boldsymbol{x}_s)^{\mathsf T}]^{\mathsf T}$：分块对角矩阵的作用是在各块上独立进行的。当对角块都是可逆方阵时，$A$ 可逆，且 $A^{-1} = \operatorname{diag}(A_1^{-1}, \dots, A_s^{-1})$（直接相乘验证）。

## 2.6. 分块初等矩阵与 Schur 补

消元法也可以按块进行。下面只讨论 $2 \times 2$ 分块，$n_1, n_2$ 是块的阶数。类比三类初等矩阵，有三类分块初等矩阵：

| 类型 | 矩阵 | 逆矩阵 | 左乘 $\begin{bmatrix} A_1 \\ A_2 \end{bmatrix}$ | 右乘 $[B_1\ B_2]$ |
|---|---|---|---|---|
| 分块对换 | $\begin{bmatrix} O & I_{n_2} \\ I_{n_1} & O \end{bmatrix}$ | $\begin{bmatrix} O & I_{n_1} \\ I_{n_2} & O \end{bmatrix}$ | $\begin{bmatrix} A_2 \\ A_1 \end{bmatrix}$ | $[B_2\ B_1]$ |
| 分块倍乘（$P$ 可逆） | $\begin{bmatrix} I_{n_1} & O \\ O & P \end{bmatrix}$ | $\begin{bmatrix} I_{n_1} & O \\ O & P^{-1} \end{bmatrix}$ | $\begin{bmatrix} A_1 \\ PA_2 \end{bmatrix}$ | $[B_1\ B_2P]$ |
| 分块倍加 | $\begin{bmatrix} I_{n_1} & M \\ O & I_{n_2} \end{bmatrix}$ | $\begin{bmatrix} I_{n_1} & -M \\ O & I_{n_2} \end{bmatrix}$ | $\begin{bmatrix} A_1 + MA_2 \\ A_2 \end{bmatrix}$ | $[B_1\ \ B_1M + B_2]$ |

分块对换矩阵中 $I_{n_1}, I_{n_2}$ 的位置由被乘矩阵的分块方式决定。

**例 2.6.1（分块上三角矩阵）** 设 $A = \begin{bmatrix} A_{11} & A_{12} \\ O & A_{22} \end{bmatrix}$，$A_{11}, A_{22}$ 是方阵，则 $A$ 可逆当且仅当 $A_{11}, A_{22}$ 都可逆，此时

$$
\begin{bmatrix} A_{11} & A_{12} \\ O & A_{22} \end{bmatrix}^{-1} = \begin{bmatrix} A_{11}^{-1} & -A_{11}^{-1}A_{12}A_{22}^{-1} \\ O & A_{22}^{-1} \end{bmatrix}.
$$

若 $A_{11}$ 不可逆，取 $A_{11}\boldsymbol{x}_1 = \boldsymbol{0}$ 的非零解，则 $A\begin{bmatrix} \boldsymbol{x}_1 \\ \boldsymbol{0} \end{bmatrix} = \boldsymbol{0}$；若 $A_{11}$ 可逆而 $A_{22}$ 不可逆，取 $A_{22}\boldsymbol{y} = \boldsymbol{0}$ 的非零解，则 $A\begin{bmatrix} -A_{11}^{-1}A_{12}\boldsymbol{y} \\ \boldsymbol{y} \end{bmatrix} = \boldsymbol{0}$。两种情况 $A$ 都不可逆。若二者都可逆，对 $[A\ I]$ 做分块 Gauss–Jordan 消元：先左乘 $\operatorname{diag}(A_{11}^{-1}, A_{22}^{-1})$ 把对角块化为单位矩阵，再左乘 $\begin{bmatrix} I & -A_{11}^{-1}A_{12} \\ O & I \end{bmatrix}$ 消去右上角，就得到上式。注意块的乘法次序不能交换。分块下三角矩阵同理。

一般的 $2 \times 2$ 分块矩阵可以先消元成分块三角形。

**定义 2.6.1（Schur 补）** 设 $A = \begin{bmatrix} A_{11} & A_{12} \\ A_{21} & A_{22} \end{bmatrix}$，$A_{11}, A_{22}$ 是方阵。若 $A_{11}$ 可逆，称 $A_{22} - A_{21}A_{11}^{-1}A_{12}$ 为 $A_{11}$ 在 $A$ 中的 **Schur 补**；若 $A_{22}$ 可逆，称 $A_{11} - A_{12}A_{22}^{-1}A_{21}$ 为 $A_{22}$ 在 $A$ 中的 Schur 补。

Schur 补正是分块消元后剩下的块：

$$
\begin{bmatrix} I & O \\ -A_{21}A_{11}^{-1} & I \end{bmatrix}\begin{bmatrix} A_{11} & A_{12} \\ A_{21} & A_{22} \end{bmatrix} = \begin{bmatrix} A_{11} & A_{12} \\ O & A_{22} - A_{21}A_{11}^{-1}A_{12} \end{bmatrix}, \tag{2.1}
$$

$$
\begin{bmatrix} I & -A_{12}A_{22}^{-1} \\ O & I \end{bmatrix}\begin{bmatrix} A_{11} & A_{12} \\ A_{21} & A_{22} \end{bmatrix} = \begin{bmatrix} A_{11} - A_{12}A_{22}^{-1}A_{21} & O \\ A_{21} & A_{22} \end{bmatrix}. \tag{2.2}
$$

**命题 2.6.1** 在定义 2.6.1 的记号下，若 $A_{11}$ 可逆，则 $A$ 可逆当且仅当 $S = A_{22} - A_{21}A_{11}^{-1}A_{12}$ 可逆，此时

$$
A^{-1} = \begin{bmatrix} I & -A_{11}^{-1}A_{12} \\ O & I \end{bmatrix}\begin{bmatrix} A_{11}^{-1} & O \\ O & S^{-1} \end{bmatrix}\begin{bmatrix} I & O \\ -A_{21}A_{11}^{-1} & I \end{bmatrix} = \begin{bmatrix} A_{11}^{-1} + A_{11}^{-1}A_{12}S^{-1}A_{21}A_{11}^{-1} & -A_{11}^{-1}A_{12}S^{-1} \\ -S^{-1}A_{21}A_{11}^{-1} & S^{-1} \end{bmatrix}. \tag{2.3}
$$

若 $A_{22}$ 可逆，则 $A$ 可逆当且仅当 $T = A_{11} - A_{12}A_{22}^{-1}A_{21}$ 可逆，此时

$$
A^{-1} = \begin{bmatrix} I & O \\ -A_{22}^{-1}A_{21} & I \end{bmatrix}\begin{bmatrix} T^{-1} & O \\ O & A_{22}^{-1} \end{bmatrix}\begin{bmatrix} I & -A_{12}A_{22}^{-1} \\ O & I \end{bmatrix} = \begin{bmatrix} T^{-1} & -T^{-1}A_{12}A_{22}^{-1} \\ -A_{22}^{-1}A_{21}T^{-1} & A_{22}^{-1} + A_{22}^{-1}A_{21}T^{-1}A_{12}A_{22}^{-1} \end{bmatrix}. \tag{2.4}
$$

**证明** 只证第一条。式 (2.1) 左边第一个因子可逆，所以 $A$ 可逆当且仅当右边的分块上三角矩阵可逆，由例 2.6.1 当且仅当 $A_{11}$ 与 $S$ 都可逆。对式 (2.1) 两边求逆，并用例 2.6.1 写出分块上三角矩阵的逆

$$
\begin{bmatrix} A_{11} & A_{12} \\ O & S \end{bmatrix}^{-1} = \begin{bmatrix} I & -A_{11}^{-1}A_{12} \\ O & I \end{bmatrix}\begin{bmatrix} A_{11}^{-1} & O \\ O & S^{-1} \end{bmatrix},
$$

即得式 (2.3) 的因子形式；把三个因子乘出来就是右端。$\square$

## 2.7. Sherman–Morrison–Woodbury 公式

当 $A_{11}, A_{22}$ 及两个 Schur 补都可逆时，式 (2.3) 与式 (2.4) 是同一个 $A^{-1}$ 的两种表达式。比较左上角的块，得到

$$
(A_{11} - A_{12}A_{22}^{-1}A_{21})^{-1} = A_{11}^{-1} + A_{11}^{-1}A_{12}(A_{22} - A_{21}A_{11}^{-1}A_{12})^{-1}A_{21}A_{11}^{-1}. \tag{2.5}
$$

它给出可逆矩阵 $A_{11}$ 加上一个修正项 $-A_{12}A_{22}^{-1}A_{21}$ 之后的逆。取 $A_{11} = A$，$A_{12} = U$，$A_{21} = -V$，$A_{22} = C^{-1}$，就得到通常的形式：

**定理 2.7.1（Woodbury 公式）** 设 $A$ 是 $n$ 阶可逆矩阵，$C$ 是 $k$ 阶可逆矩阵，$U, V$ 分别是 $n \times k$、$k \times n$ 矩阵。若 $C^{-1} + VA^{-1}U$ 可逆，则 $A + UCV$ 可逆，且

$$
(A + UCV)^{-1} = A^{-1} - A^{-1}U(C^{-1} + VA^{-1}U)^{-1}VA^{-1}.
$$

**证明** 令 $M = \begin{bmatrix} A & U \\ -V & C^{-1} \end{bmatrix}$。$A$ 在 $M$ 中的 Schur 补是 $C^{-1} + VA^{-1}U$，由命题 2.6.1 $M$ 可逆；$C^{-1}$ 可逆，它在 $M$ 中的 Schur 补是 $A + UCV$，再由命题 2.6.1 它也可逆。于是式 (2.5) 的条件都满足，代入即得。$\square$

这个公式也称为 Sherman–Morrison–Woodbury 公式。它的价值在于 $k \ll n$ 时：已知 $A^{-1}$，对 $A$ 做秩不超过 $k$ 的修改后，只需求一个 $k$ 阶矩阵的逆，而不必重新对 $n$ 阶矩阵求逆。$k = 1$ 是最常用的特例：

**定理 2.7.2（Sherman–Morrison 公式）** 设 $A$ 是 $n$ 阶可逆矩阵，$\boldsymbol{u}, \boldsymbol{v} \in \mathbb{R}^n$，则 $A + \boldsymbol{u}\boldsymbol{v}^{\mathsf T}$ 可逆当且仅当 $1 + \boldsymbol{v}^{\mathsf T}A^{-1}\boldsymbol{u} \ne 0$，此时

$$
(A + \boldsymbol{u}\boldsymbol{v}^{\mathsf T})^{-1} = A^{-1} - \frac{A^{-1}\boldsymbol{u}\boldsymbol{v}^{\mathsf T}A^{-1}}{1 + \boldsymbol{v}^{\mathsf T}A^{-1}\boldsymbol{u}}.
$$

**证明** 考虑 $M = \begin{bmatrix} A & \boldsymbol{u} \\ -\boldsymbol{v}^{\mathsf T} & 1 \end{bmatrix}$。$A$ 的 Schur 补是数 $1 + \boldsymbol{v}^{\mathsf T}A^{-1}\boldsymbol{u}$，右下角 $1$ 的 Schur 补是 $A + \boldsymbol{u}\boldsymbol{v}^{\mathsf T}$。由命题 2.6.1，两者都等价于 $M$ 可逆，故可逆性的条件成立。公式可以直接验证：记 $\beta = 1 + \boldsymbol{v}^{\mathsf T}A^{-1}\boldsymbol{u}$，

$$
(A + \boldsymbol{u}\boldsymbol{v}^{\mathsf T})\left(A^{-1} - \frac{A^{-1}\boldsymbol{u}\boldsymbol{v}^{\mathsf T}A^{-1}}{\beta}\right) = I + \boldsymbol{u}\boldsymbol{v}^{\mathsf T}A^{-1} - \frac{\boldsymbol{u}(1 + \boldsymbol{v}^{\mathsf T}A^{-1}\boldsymbol{u})\boldsymbol{v}^{\mathsf T}A^{-1}}{\beta} = I. \qquad \square
$$

取 $A = I$：$I + \boldsymbol{u}\boldsymbol{v}^{\mathsf T}$ 可逆当且仅当 $1 + \boldsymbol{v}^{\mathsf T}\boldsymbol{u} \ne 0$，此时 $(I + \boldsymbol{u}\boldsymbol{v}^{\mathsf T})^{-1} = I - \dfrac{\boldsymbol{u}\boldsymbol{v}^{\mathsf T}}{1 + \boldsymbol{v}^{\mathsf T}\boldsymbol{u}}$。

**注 2.7.1** 若把 $M$ 的右下角换成非零数 $a$，同样的论证给出：$A + \frac1a\boldsymbol{u}\boldsymbol{v}^{\mathsf T}$ 可逆当且仅当 $a + \boldsymbol{v}^{\mathsf T}A^{-1}\boldsymbol{u} \ne 0$，此时

$$
\left(A + \frac1a\boldsymbol{u}\boldsymbol{v}^{\mathsf T}\right)^{-1} = A^{-1} - \frac{A^{-1}\boldsymbol{u}\boldsymbol{v}^{\mathsf T}A^{-1}}{a + \boldsymbol{v}^{\mathsf T}A^{-1}\boldsymbol{u}}.
$$

这不是新的结论，只是对 $\frac1a\boldsymbol{u}$ 和 $\boldsymbol{v}$ 用定理 2.7.2；条件 $a \ne 0$ 是使 $\frac1a$ 有意义所必需的。

**例 2.7.1（单个元素的扰动）** 设 $A$ 可逆，把 $(1, 1)$ 元从 $a_{11}$ 改为 $a_{11} + \delta$，新矩阵是 $A + \delta\boldsymbol{e}_1\boldsymbol{e}_1^{\mathsf T}$。由定理 2.7.2，它可逆当且仅当 $1 + \delta\,\boldsymbol{e}_1^{\mathsf T}A^{-1}\boldsymbol{e}_1 \ne 0$。所以只要 $|\delta| < 1/|\boldsymbol{e}_1^{\mathsf T}A^{-1}\boldsymbol{e}_1|$，新矩阵就可逆（若 $\boldsymbol{e}_1^{\mathsf T}A^{-1}\boldsymbol{e}_1 = 0$，则对任意 $\delta$ 都可逆），且

$$
(A + \delta\boldsymbol{e}_1\boldsymbol{e}_1^{\mathsf T})^{-1} = A^{-1} - \frac{\delta}{1 + \delta\,\boldsymbol{e}_1^{\mathsf T}A^{-1}\boldsymbol{e}_1}A^{-1}\boldsymbol{e}_1\boldsymbol{e}_1^{\mathsf T}A^{-1}.
$$

逆的变化只与 $A^{-1}$ 的第一列 $A^{-1}\boldsymbol{e}_1$ 和第一行 $\boldsymbol{e}_1^{\mathsf T}A^{-1}$ 有关。一般地，若 $(i, j)$ 元改变 $\delta$，

$$
(A + \delta\boldsymbol{e}_i\boldsymbol{e}_j^{\mathsf T})^{-1} = A^{-1} - \frac{\delta}{1 + \delta\,\boldsymbol{e}_j^{\mathsf T}A^{-1}\boldsymbol{e}_i}A^{-1}\boldsymbol{e}_i\boldsymbol{e}_j^{\mathsf T}A^{-1},
$$

逆的变化只与 $A^{-1}$ 的第 $i$ 列和第 $j$ 行有关。这样更新逆矩阵只需 $O(n^2)$ 次运算，而重新求逆需要约 $2n^3$ 次。

## 2.8. LU 分解

设 $n$ 阶方阵 $A$ 在 Gauss 消元中不需要对换行（称为 Gauss 顺序消元），则向下消元的过程是依次左乘倍加矩阵：

$$
(E_{n,n-1})\cdots(E_{n2}\cdots E_{32})(E_{n1}\cdots E_{31}E_{21})A = U,
$$

其中 $E_{ji}$（$j > i$）表示把第 $i$ 行的某个倍数加到第 $j$ 行，是单位下三角矩阵；$U$ 是 $A$ 的阶梯形，是上三角矩阵。由性质 2.3.1 和命题 2.3.2，单位下三角矩阵的乘积与逆仍是单位下三角矩阵。记左边这些倍加矩阵的乘积为 $L^{-1}$，则 $L^{-1}A = U$，即 $A = LU$。

**定义 2.8.1（LU 分解）** 把方阵 $A$ 写成 $A = LU$，其中 $L$ 是单位下三角矩阵、$U$ 是上三角矩阵，称为 $A$ 的 **LU 分解**。

**定理 2.8.1** 若 $n$ 阶方阵 $A$ 只用倍加行变换（Gauss 顺序消元）就能化成阶梯形，则存在 $n$ 阶单位下三角矩阵 $L$ 和 $n$ 阶上三角矩阵 $U$，使得 $A = LU$。

$L$ 总是可逆的，所以 $A$ 可逆当且仅当 $U = L^{-1}A$ 可逆。有了 LU 分解，方程组 $A\boldsymbol{x} = \boldsymbol{b}$ 化为两个三角方程组

$$
L\boldsymbol{y} = \boldsymbol{b}\ \ (\text{前代法}), \qquad U\boldsymbol{x} = \boldsymbol{y}\ \ (\text{回代法}).
$$

并不是所有方阵都有 LU 分解。例如 $\begin{bmatrix} 0 & 1 \\ 1 & 0 \end{bmatrix} = \begin{bmatrix} 1 & 0 \\ \ell & 1 \end{bmatrix}\begin{bmatrix} u_{11} & u_{12} \\ 0 & u_{22} \end{bmatrix}$ 要求 $u_{11} = 0$，于是左下角 $\ell u_{11} = 0 \ne 1$，矛盾。

**例 2.8.1** 不可逆的矩阵也可能有 LU 分解：

$$
\begin{bmatrix} 1 & 0 & 0 & 0 \\ 0 & 0 & 1 & 0 \\ 0 & 0 & 2 & 0 \\ 0 & 0 & 3 & 0 \end{bmatrix} = \begin{bmatrix} 1 & & & \\ 0 & 1 & & \\ 0 & 2 & 1 & \\ 0 & 3 & 0 & 1 \end{bmatrix}\begin{bmatrix} 1 & 0 & 0 & 0 \\ 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 \end{bmatrix}.
$$

这时 $U$ 的后两行为零，$L$ 的 $(4, 3)$ 元可以任意取，分解不唯一。

## 2.9. 可逆矩阵 LU 分解的存在与唯一

**定义 2.9.1（顺序主子阵）** 方阵 $A$ 左上角的 $k \times k$ 块称为 $A$ 的第 $k$ 个**顺序主子阵**，记为 $A_k$（$k = 1, \dots, n$）。

**定理 2.9.1（可逆矩阵的 LU 分解）** $n$ 阶可逆矩阵 $A$ 有 LU 分解，当且仅当 $A$ 的所有顺序主子阵都可逆。此时 $A$ 的 LU 分解唯一。

**证明** 必要性：设 $A = LU$，则 $L, U$ 都可逆，对角元素都不为零。对每个 $k$ 作分块

$$
A = \begin{bmatrix} L_{11} & O \\ L_{21} & L_{22} \end{bmatrix}\begin{bmatrix} U_{11} & U_{12} \\ O & U_{22} \end{bmatrix} = \begin{bmatrix} L_{11}U_{11} & L_{11}U_{12} \\ L_{21}U_{11} & L_{21}U_{12} + L_{22}U_{22} \end{bmatrix},
$$

其中 $L_{11}, U_{11}$ 是 $k$ 阶三角矩阵，对角元素不为零，因而可逆。所以第 $k$ 个顺序主子阵 $A_k = L_{11}U_{11}$ 可逆。

充分性：对 $n$ 用数学归纳法。$n = 1$ 时 $A = [a] = [1][a]$。设结论对 $n-1$ 阶成立，把 $A$ 分块为 $A = \begin{bmatrix} A_{n-1} & \boldsymbol{x} \\ \boldsymbol{y}^{\mathsf T} & a \end{bmatrix}$。$A_{n-1}$ 可逆，且它的顺序主子阵也是 $A$ 的顺序主子阵，都可逆，由归纳假设 $A_{n-1} = L_1U_1$，$L_1, U_1$ 可逆。由分块消元，

$$
A = \begin{bmatrix} I_{n-1} & \boldsymbol{0} \\ \boldsymbol{y}^{\mathsf T}A_{n-1}^{-1} & 1 \end{bmatrix}\begin{bmatrix} A_{n-1} & \boldsymbol{x} \\ \boldsymbol{0}^{\mathsf T} & a - \boldsymbol{y}^{\mathsf T}A_{n-1}^{-1}\boldsymbol{x} \end{bmatrix} = \begin{bmatrix} L_1 & \boldsymbol{0} \\ \boldsymbol{y}^{\mathsf T}U_1^{-1} & 1 \end{bmatrix}\begin{bmatrix} U_1 & L_1^{-1}\boldsymbol{x} \\ \boldsymbol{0}^{\mathsf T} & a - \boldsymbol{y}^{\mathsf T}A_{n-1}^{-1}\boldsymbol{x} \end{bmatrix},
$$

右端第一个因子是单位下三角矩阵，第二个是上三角矩阵（直接相乘可以验证最后一个等号）。

唯一性：设 $A = L_1U_1 = L_2U_2$，四个因子都可逆，则 $L_2^{-1}L_1 = U_2U_1^{-1}$。左边是单位下三角矩阵，右边是上三角矩阵，所以两边都是单位矩阵，$L_1 = L_2$，$U_1 = U_2$。$\square$

## 2.10. 计算 LU 分解

LU 分解就是 Gauss 消元的另一种记录方式：$U = L^{-1}A$ 是 $A$ 的阶梯形。最直接的算法是把 $L^{-1}$ 也一起算出来。

**算法 2.10.1（两步法）**

1. 对 $[A\ I]$ 做 Gauss 顺序消元（只用"把上面的行的倍数加到下面的行"的倍加变换），得到 $[U\ L^{-1}]$；
2. 对 $[L^{-1}\ I]$ 做 Gauss–Jordan 消元，得到 $[I\ L]$。

**例 2.10.1** 对 $A = \begin{bmatrix} 1 & 1 & 1 & 1 \\ 1 & 2 & 3 & 4 \\ 1 & 3 & 6 & 10 \\ 1 & 4 & 10 & 20 \end{bmatrix}$，第一步得到

$$
U = \begin{bmatrix} 1 & 1 & 1 & 1 \\ & 1 & 2 & 3 \\ & & 1 & 3 \\ & & & 1 \end{bmatrix}, \qquad L^{-1} = \begin{bmatrix} 1 & & & \\ -1 & 1 & & \\ 1 & -2 & 1 & \\ -1 & 3 & -3 & 1 \end{bmatrix},
$$

第二步得到 $L = \begin{bmatrix} 1 & & & \\ 1 & 1 & & \\ 1 & 2 & 1 & \\ 1 & 3 & 3 & 1 \end{bmatrix}$。这里 $U = L^{\mathsf T}$，原因是 $A$ 对称且 $U$ 的对角元素都是 $1$（见推论 2.11.1）；一般的对称矩阵只有 $U = DL^{\mathsf T}$，其中 $D$ 是 $U$ 的对角部分。

两步法要做两次消元。利用 $L^{-1}$ 的结构可以一次完成。不对换行时，记 $L_j^{-1} = E_{nj}\cdots E_{j+1,j}$（$j = 1, \dots, n-1$），它是第 $j$ 步消元所用倍加矩阵的乘积：

$$
L_j^{-1} = \begin{bmatrix} 1 & & & & & \\ & \ddots & & & & \\ & & 1 & & & \\ & & -\ell_{j+1,j} & 1 & & \\ & & \vdots & & \ddots & \\ & & -\ell_{nj} & & & 1 \end{bmatrix},
$$

只有第 $j$ 列有非零的非对角元素，称为初等单位下三角矩阵；左乘 $L_j^{-1}$ 表示把第 $j$ 行的 $-\ell_{ij}$ 倍加到第 $i$ 行（$i > j$）。令 $\boldsymbol{\ell}_j = [0\ \cdots\ 0\ \ell_{j+1,j}\ \cdots\ \ell_{nj}]^{\mathsf T}$（前 $j$ 个分量为零），则

$$
L_j^{-1} = I_n - \boldsymbol{\ell}_j\boldsymbol{e}_j^{\mathsf T}, \qquad L_j = I_n + \boldsymbol{\ell}_j\boldsymbol{e}_j^{\mathsf T},
$$

后者可以由 $\boldsymbol{e}_j^{\mathsf T}\boldsymbol{\ell}_j = 0$ 直接验证。消元过程 $L_{n-1}^{-1}\cdots L_2^{-1}L_1^{-1}A = U$ 给出 $A = LU$，其中

$$
L = L_1L_2\cdots L_{n-1} = (I_n + \boldsymbol{\ell}_1\boldsymbol{e}_1^{\mathsf T})\cdots(I_n + \boldsymbol{\ell}_{n-1}\boldsymbol{e}_{n-1}^{\mathsf T}) = I_n + \boldsymbol{\ell}_1\boldsymbol{e}_1^{\mathsf T} + \cdots + \boldsymbol{\ell}_{n-1}\boldsymbol{e}_{n-1}^{\mathsf T} = \begin{bmatrix} 1 & & & \\ \ell_{21} & 1 & & \\ \vdots & \vdots & \ddots & \\ \ell_{n1} & \ell_{n2} & \cdots & 1 \end{bmatrix}.
$$

展开乘积时，交叉项 $\boldsymbol{\ell}_i\boldsymbol{e}_i^{\mathsf T}\boldsymbol{\ell}_j\boldsymbol{e}_j^{\mathsf T}$（$i < j$）都含因子 $\boldsymbol{e}_i^{\mathsf T}\boldsymbol{\ell}_j = 0$。也就是说，$L$ 的元素就是消元时用过的乘数，不需要任何额外计算。注意次序：$L^{-1} = L_{n-1}^{-1}\cdots L_1^{-1}$ 的元素并不是 $-\ell_{ij}$（例 2.10.1 中 $L^{-1}$ 的 $(3, 1)$ 元是 $1$，而不是 $-1$）。

**算法 2.10.2（LU 分解：一次消元）** 输入 $n$ 阶方阵 $A$，令 $A^{(1)} = A$。对 $j = 1, \dots, n-1$：

1. 若主元 $a_{jj}^{(j)} = 0$，则顺序消元无法继续（需要对换行，见 2.11 节）；
2. 对 $i = j+1, \dots, n$，计算乘数 $\ell_{ij} = a_{ij}^{(j)} / a_{jj}^{(j)}$，并把第 $j$ 行的 $\ell_{ij}$ 倍从第 $i$ 行减去，得到 $A^{(j+1)}$。

最后 $U = A^{(n)}$，$L$ 是以 $\ell_{ij}$ 为严格下三角部分的单位下三角矩阵。实际实现中乘数 $\ell_{ij}$ 直接存放在被消成零的位置上，不需要额外存储。

**例 2.10.2** 对例 2.10.1 的矩阵：

$$
A^{(2)} = \begin{bmatrix} 1 & 1 & 1 & 1 \\ & 1 & 2 & 3 \\ & 2 & 5 & 9 \\ & 3 & 9 & 19 \end{bmatrix}\ (\ell_{21} = \ell_{31} = \ell_{41} = 1), \quad
A^{(3)} = \begin{bmatrix} 1 & 1 & 1 & 1 \\ & 1 & 2 & 3 \\ & & 1 & 3 \\ & & 3 & 10 \end{bmatrix}\ (\ell_{32} = 2,\ \ell_{42} = 3), \quad
A^{(4)} = U\ (\ell_{43} = 3),
$$

读出 $L$ 的下三角部分为 $(1, 1, 1)$、$(2, 3)$、$(3)$，与例 2.10.1 相同。

算法 2.10.2 第 $j$ 步要更新 $(n-j)^2$ 个元素，每个一次乘法一次减法，总计约 $\frac23n^3$ 次浮点运算；之后每解一个方程组只需两次三角求解，约 $2n^2$ 次。下图左边比较了几种计算的运算量，右边说明：当同一个系数矩阵要对许多右端项 $\boldsymbol{b}$ 求解时，"分解一次、反复回代"比每次重新消元便宜得多。

![左：LU 分解、两次三角求解与 Gauss–Jordan 求逆的浮点运算次数（灰线为渐近公式）；右：n = 200 时对 k 个右端项求解的总运算量](./plots/lu-operation-counts.py)

## 2.11. LDU 分解与 PLU 分解

把 LU 分解中 $U$ 的对角元素提出来，就得到更对称的形式。

**定理 2.11.1（LDU 分解）** 若 $n$ 阶可逆矩阵 $A$ 有 LU 分解，则存在唯一的一组 $n$ 阶单位下三角矩阵 $L$、对角元素均不为零的对角矩阵 $D$ 和单位上三角矩阵 $U$，使得 $A = LDU$，称为 $A$ 的 LDU 分解。

**证明** 存在性：设 $A = L\tilde{U}$，$\tilde{U}$ 可逆，其对角元素不为零。令 $D = \operatorname{diag}(\tilde{u}_{11}, \dots, \tilde{u}_{nn})$，$U = D^{-1}\tilde{U}$（即用倍乘行变换把阶梯形的主元化成 $1$），则 $U$ 是单位上三角矩阵，$A = LDU$。唯一性：设 $A = L_1D_1U_1 = L_2D_2U_2$，则 $L_2^{-1}L_1 = D_2U_2U_1^{-1}D_1^{-1}$，左边是单位下三角矩阵，右边是上三角矩阵，故都等于 $I$，$L_1 = L_2$；于是 $D_2^{-1}D_1 = U_2U_1^{-1}$，左边是对角矩阵，右边是单位上三角矩阵，故都等于 $I$，$D_1 = D_2$，$U_1 = U_2$。$\square$

**推论 2.11.1** 若对称矩阵 $A$ 有 LDU 分解 $A = LDU$，则 $U = L^{\mathsf T}$，即 $A = LDL^{\mathsf T}$。

**证明** $A = A^{\mathsf T} = U^{\mathsf T}DL^{\mathsf T}$ 也是 $A$ 的一个 LDU 分解（$U^{\mathsf T}$ 是单位下三角矩阵，$L^{\mathsf T}$ 是单位上三角矩阵），由唯一性 $L = U^{\mathsf T}$。$\square$

所以对称矩阵的 LU 分解中，上三角因子是 $DL^{\mathsf T}$；只有当所有主元都等于 $1$（$D = I$）时才有 $U = L^{\mathsf T}$。对称矩阵只需计算 $L$ 和 $D$，运算量约减半，这也是[第 7 章](/2.1.7)中 Cholesky 分解的出发点。

一般的可逆矩阵在顺序消元中可能遇到零主元，这时必须对换行。

**例 2.11.1** 对 $A = \begin{bmatrix} 1 & -1 & 1 \\ -1 & 1 & 0 \\ 2 & -1 & 2 \end{bmatrix}$ 消元，第一步倍加后第 $(2, 2)$ 位置为零，需要对换第 2、3 行：

$$
A \xrightarrow{\text{倍加}} \begin{bmatrix} 1 & -1 & 1 \\ 0 & 0 & 1 \\ 0 & 1 & 0 \end{bmatrix} \xrightarrow{\text{对换}} \begin{bmatrix} 1 & -1 & 1 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{bmatrix}.
$$

若先把对换作用在 $A$ 上，就只需倍加：$P_{23}A = \begin{bmatrix} 1 & -1 & 1 \\ 2 & -1 & 2 \\ -1 & 1 & 0 \end{bmatrix} = \begin{bmatrix} 1 & & \\ 2 & 1 & \\ -1 & 0 & 1 \end{bmatrix}\begin{bmatrix} 1 & -1 & 1 \\ & 1 & 0 \\ & & 1 \end{bmatrix}$，于是 $A = P_{23}LU$。

**定理 2.11.2（PLU 分解）** 对任意 $n$ 阶可逆矩阵 $A$，存在 $n$ 阶置换矩阵 $P$、单位下三角矩阵 $L$ 和对角元素都不为零的上三角矩阵 $U$，使得 $A = PLU$。

**证明** 对 $n$ 用数学归纳法，$n = 1$ 显然。设结论对 $n-1$ 阶成立。$A$ 可逆，第一列不全为零，取 $a_{i1} \ne 0$，令 $P_1 = P_{1i}$（$i = 1$ 时 $P_1 = I$），则 $P_1A = \begin{bmatrix} a & \boldsymbol{w}^{\mathsf T} \\ \boldsymbol{v} & A' \end{bmatrix}$，$a \ne 0$。分块消元得

$$
P_1A = \begin{bmatrix} 1 & \boldsymbol{0}^{\mathsf T} \\ \boldsymbol{v}/a & I \end{bmatrix}\begin{bmatrix} a & \boldsymbol{w}^{\mathsf T} \\ \boldsymbol{0} & S \end{bmatrix}, \qquad S = A' - \frac{\boldsymbol{v}\boldsymbol{w}^{\mathsf T}}{a}.
$$

由命题 2.6.1，Schur 补 $S$ 可逆，由归纳假设 $S = P'L'U'$。直接相乘可以验证

$$
P_1A = \begin{bmatrix} 1 & \boldsymbol{0}^{\mathsf T} \\ \boldsymbol{0} & P' \end{bmatrix}\begin{bmatrix} 1 & \boldsymbol{0}^{\mathsf T} \\ P'^{\mathsf T}\boldsymbol{v}/a & L' \end{bmatrix}\begin{bmatrix} a & \boldsymbol{w}^{\mathsf T} \\ \boldsymbol{0} & U' \end{bmatrix},
$$

（用到 $P'P'^{\mathsf T} = I$），于是 $A = PLU$，$P = P_1^{\mathsf T}\operatorname{diag}(1, P')$ 是置换矩阵（命题 2.3.3），$L$ 是单位下三角矩阵，$U$ 是对角元素非零的上三角矩阵。$\square$

证明中每一步只要求主元非零。数值计算中每一步选当前列中绝对值最大的元素作主元（部分选主元，partial pivoting），以控制舍入误差的放大；`scipy.linalg.lu` 等数值软件计算的就是这种 PLU 分解。

## 小结

本章的主线是"消元 = 左乘初等矩阵"：可逆性、求逆、LU 分解都是这一观点的推论。

| 类别 | 内容 |
|---|---|
| 定义 | 初等矩阵 $P_{ij}, E_{ii;k}, E_{ji;k}$（定义 2.1.1）；可逆映射、可逆线性变换（定义 2.2.1、2.2.2）；可逆矩阵、逆矩阵、奇异矩阵（定义 2.2.3）；置换矩阵（定义 2.3.1）；对角占优矩阵（定义 2.3.2）；左相抵（定义 2.4.1）；分块矩阵、分块对角矩阵（定义 2.5.1、2.5.2）；Schur 补（定义 2.6.1）；LU 分解（定义 2.8.1）；顺序主子阵（定义 2.9.1） |
| 定理 | 左行右列（命题 2.1.1）；可逆矩阵的性质（命题 2.2.3）；可逆的六个等价条件（定理 2.3.1）；单边逆即逆（命题 2.3.1）；三角矩阵的乘积与逆（性质 2.3.1、命题 2.3.2）；对角占优矩阵可逆（命题 2.3.4）；左相抵 $\Leftrightarrow PA = B$（命题 2.4.1）；分块求逆（命题 2.6.1）；Woodbury 公式与 Sherman–Morrison 公式（定理 2.7.1、2.7.2）；可逆矩阵 LU 分解的存在唯一（定理 2.9.1）；LDU 分解（定理 2.11.1）；对称矩阵 $A = LDL^{\mathsf T}$（推论 2.11.1）；PLU 分解（定理 2.11.2） |
| 算法 | Gauss–Jordan 求逆 $[A\ I] \to [I\ A^{-1}]$（算法 2.3.1，约 $2n^3$ 次）；LU 分解的两步法（算法 2.10.1）与一次消元法（算法 2.10.2，约 $\frac23n^3$ 次，之后每个右端项约 $2n^2$ 次） |

| 分解 | 形式 | 存在条件 | 唯一性 |
|---|---|---|---|
| LU | $A = LU$，$L$ 单位下三角，$U$ 上三角 | 顺序消元可行；可逆时当且仅当顺序主子阵都可逆 | 可逆时唯一 |
| LDU | $A = LDU$，$L$、$U$ 单位三角，$D$ 对角 | 可逆且有 LU 分解 | 唯一；对称时 $U = L^{\mathsf T}$ |
| PLU | $A = PLU$，$P$ 置换矩阵 | 任意可逆矩阵 | 一般不唯一 |
