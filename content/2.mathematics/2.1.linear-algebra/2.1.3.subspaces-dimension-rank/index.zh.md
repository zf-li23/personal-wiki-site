---
title: 子空间、维数与秩
---

[第 1 章](/2.1.1)的判定定理回答了线性方程组"有没有解、解是否唯一"，但没有回答"解不唯一时，解集是什么样子"。本章从列的观点看 $A\boldsymbol{x} = \boldsymbol{b}$：方程组有解，就是 $\boldsymbol{b}$ 能被 $A$ 的列向量线性表示。围绕"线性表示"依次提出四个问题：一组向量能表示出哪些向量（子空间与线性生成）？表示是否唯一（线性无关）？哪些向量是关键的（极大线性无关部分组与基）？什么量在变换中保持不变（秩与维数）？回答这些问题之后，矩阵的秩把前两章的结论统一起来：解集等于一个特解加上零空间，零空间的维数是 $n - \operatorname{rank}(A)$；四个基本子空间的维数由秩完全决定。

本章只在 $\mathbb{R}^m$ 中讨论；[第 8 章](/2.1.8)把这些概念推广到一般的线性空间，证明基本不变。四个基本子空间之间的正交关系在[第 4 章](/2.1.4)讨论。

## 3.1. 线性映射的像与原像

矩阵 $A$ 确定线性映射 $T_A\colon \mathbb{R}^n \to \mathbb{R}^m$，$\boldsymbol{x} \mapsto A\boldsymbol{x}$。方程组 $A\boldsymbol{x} = \boldsymbol{b}$ 解的存在与唯一，直接对应于这个映射的像与原像的性质。

**命题 3.1.1** 设 $A$ 是 $m \times n$ 矩阵。

1. $T_A$ 是**单射**，当且仅当齐次方程组 $A\boldsymbol{x} = \boldsymbol{0}_m$ 只有零解 $\boldsymbol{0}_n$；
2. $T_A$ 是**满射**，当且仅当对任意 $\boldsymbol{b} \in \mathbb{R}^m$，方程组 $A\boldsymbol{x} = \boldsymbol{b}$ 有解。

**证明** 第 1 条：$T_A$ 是单射，即由 $A\boldsymbol{x}_1 = A\boldsymbol{x}_2$ 能推出 $\boldsymbol{x}_1 = \boldsymbol{x}_2$，也就是由 $A(\boldsymbol{x}_1 - \boldsymbol{x}_2) = \boldsymbol{0}$ 能推出 $\boldsymbol{x}_1 - \boldsymbol{x}_2 = \boldsymbol{0}$。第 2 条就是满射的定义。$\square$

所以判断线性映射是否为单射，只需看零向量的原像是否唯一。由此引入两个集合：

$$
\mathcal{R}(A) = \{A\boldsymbol{x} \mid \boldsymbol{x} \in \mathbb{R}^n\} \subseteq \mathbb{R}^m, \qquad \mathcal{N}(A) = \{\boldsymbol{x} \in \mathbb{R}^n \mid A\boldsymbol{x} = \boldsymbol{0}\} \subseteq \mathbb{R}^n.
$$

$\mathcal{R}(A)$ 是 $T_A$ 的**值域**，即 $A$ 的列向量的全体线性组合；$\mathcal{N}(A)$ 是齐次方程组 $A\boldsymbol{x} = \boldsymbol{0}$ 的解集。总有 $\boldsymbol{0}_m \in \mathcal{R}(A)$，$\boldsymbol{0}_n \in \mathcal{N}(A)$；方程组 $A\boldsymbol{x} = \boldsymbol{b}$ 有解当且仅当 $\boldsymbol{b} \in \mathcal{R}(A)$。

**命题 3.1.2** 设 $A$ 是 $m \times n$ 矩阵，则 $T_A$ 是满射当且仅当 $\mathcal{R}(A) = \mathbb{R}^m$；$T_A$ 是单射当且仅当 $\mathcal{N}(A) = \{\boldsymbol{0}\}$。

**例 3.1.1** 对 $A = \begin{bmatrix} 1 & 0 & 1 \\ 0 & 1 & 1 \\ 0 & 0 & 0 \end{bmatrix}$，

$$
\mathcal{R}(A) = \left\{ x_1\begin{bmatrix} 1 \\ 0 \\ 0 \end{bmatrix} + x_2\begin{bmatrix} 0 \\ 1 \\ 0 \end{bmatrix} + x_3\begin{bmatrix} 1 \\ 1 \\ 0 \end{bmatrix} \right\} = \left\{ \begin{bmatrix} x_1 \\ x_2 \\ 0 \end{bmatrix} \;\middle|\; x_1, x_2 \in \mathbb{R} \right\}, \qquad
\mathcal{N}(A) = \left\{ k\begin{bmatrix} -1 \\ -1 \\ 1 \end{bmatrix} \;\middle|\; k \in \mathbb{R} \right\}.
$$

$T_A$ 既不是单射也不是满射。这两个集合都在线性运算下封闭，这引出子空间的概念；它们中的向量都能由有限个向量线性表示，这引出基的概念。

## 3.2. 子空间

**定义 3.2.1（子空间）** 设 $M$ 是 $\mathbb{R}^m$ 的非空子集。若 $M$ 对加法和数乘封闭，即对任意 $\boldsymbol{a}, \boldsymbol{b} \in M$ 和 $k \in \mathbb{R}$ 都有 $\boldsymbol{a} + \boldsymbol{b} \in M$ 且 $k\boldsymbol{a} \in M$，则称 $M$ 为 $\mathbb{R}^m$ 的一个（线性）**子空间**。

两个条件可以合并为：对任意 $\boldsymbol{a}, \boldsymbol{b} \in M$，$k, \ell \in \mathbb{R}$，$k\boldsymbol{a} + \ell\boldsymbol{b} \in M$。取 $k = 0$ 知任意子空间都包含零向量。$\{\boldsymbol{0}\}$ 与 $\mathbb{R}^m$ 是 $\mathbb{R}^m$ 的子空间，称为平凡子空间，其余的称为非平凡子空间。

**例 3.2.1** 下面的集合都不是子空间：$\mathbb{R}^2$ 的第一象限（对数乘不封闭）；$\mathbb{R}^2$ 中 $x_1$ 轴与 $x_2$ 轴的并集（对加法不封闭）；$\mathbb{R}^3$ 中的平面 $x_1 + x_2 + x_3 = 1$（不含零向量）；$\mathbb{R}^3$ 中的锥面 $x_1^2 + x_2^2 = x_3^2$（对加法不封闭）。$\mathbb{R}^2$ 的非平凡子空间恰是过原点的直线，$\mathbb{R}^3$ 的非平凡子空间恰是过原点的直线与平面（由 3.6 节的维数理论可知）。

**定义 3.2.2（列空间与零空间）** 对 $m \times n$ 矩阵 $A$，称 $\mathcal{R}(A)$ 为 $A$ 的**列空间**，称 $\mathcal{N}(A)$ 为 $A$ 的**零空间**（也称为 $A\boldsymbol{x} = \boldsymbol{0}$ 的解空间）。

**命题 3.2.1** $\mathcal{R}(A)$ 是 $\mathbb{R}^m$ 的子空间，$\mathcal{N}(A)$ 是 $\mathbb{R}^n$ 的子空间。

**证明** 对 $\boldsymbol{b}_1 = A\boldsymbol{x}_1$，$\boldsymbol{b}_2 = A\boldsymbol{x}_2 \in \mathcal{R}(A)$，$k_1\boldsymbol{b}_1 + k_2\boldsymbol{b}_2 = A(k_1\boldsymbol{x}_1 + k_2\boldsymbol{x}_2) \in \mathcal{R}(A)$。对 $\boldsymbol{x}_1, \boldsymbol{x}_2 \in \mathcal{N}(A)$，$A(k_1\boldsymbol{x}_1 + k_2\boldsymbol{x}_2) = k_1A\boldsymbol{x}_1 + k_2A\boldsymbol{x}_2 = \boldsymbol{0}$。$\square$

非齐次方程组 $A\boldsymbol{x} = \boldsymbol{b}$（$\boldsymbol{b} \ne \boldsymbol{0}$）的解集不含零向量，不是子空间。

## 3.3. 线性生成与线性相关

**定义 3.3.1（线性生成）** 设 $S: \boldsymbol{a}_1, \dots, \boldsymbol{a}_n$ 是 $\mathbb{R}^m$ 中的向量组，它的全体线性组合

$$
\operatorname{span}(S) = \operatorname{span}(\boldsymbol{a}_1, \dots, \boldsymbol{a}_n) = \{k_1\boldsymbol{a}_1 + \cdots + k_n\boldsymbol{a}_n \mid k_1, \dots, k_n \in \mathbb{R}\}
$$

称为由 $\boldsymbol{a}_1, \dots, \boldsymbol{a}_n$ **线性生成**（张成）的集合，$\boldsymbol{a}_1, \dots, \boldsymbol{a}_n$ 称为它的一组生成向量。

**命题 3.3.1** $\operatorname{span}(S)$ 是 $\mathbb{R}^m$ 的子空间；若 $S$ 中的向量都属于某个子空间 $M$，则 $\operatorname{span}(S) \subseteq M$。

因此 $\operatorname{span}(S)$ 是包含 $S$ 的最小子空间。对 $A = [\boldsymbol{a}_1\ \cdots\ \boldsymbol{a}_n]$，$\mathcal{R}(A) = \operatorname{span}(\boldsymbol{a}_1, \dots, \boldsymbol{a}_n)$。

**定义 3.3.2（线性相关与线性无关）** 给定 $\mathbb{R}^m$ 中的向量组 $\boldsymbol{a}_1, \dots, \boldsymbol{a}_n$。若存在不全为零的数 $k_1, \dots, k_n$ 使得 $k_1\boldsymbol{a}_1 + \cdots + k_n\boldsymbol{a}_n = \boldsymbol{0}$，则称这个向量组**线性相关**；否则，即由 $k_1\boldsymbol{a}_1 + \cdots + k_n\boldsymbol{a}_n = \boldsymbol{0}$ 一定推出 $k_1 = \cdots = k_n = 0$，称这个向量组**线性无关**。

记 $A = [\boldsymbol{a}_1\ \cdots\ \boldsymbol{a}_n]$，则

$$
\boldsymbol{a}_1, \dots, \boldsymbol{a}_n\ \text{线性无关} \iff \text{零向量的线性表示唯一} \iff A\boldsymbol{x} = \boldsymbol{0}\ \text{只有零解} \iff \mathcal{N}(A) = \{\boldsymbol{0}\},
$$

线性相关则等价于 $A\boldsymbol{x} = \boldsymbol{0}$ 有非零解。由定义直接可得：含零向量的向量组线性相关；线性无关向量组的任意部分组线性无关；线性相关向量组的任意扩充组线性相关。

**例 3.3.1** 设 $A = [\boldsymbol{a}\ \boldsymbol{b}]$，$\boldsymbol{a}, \boldsymbol{b} \in \mathbb{R}^2$。

1. 若 $\boldsymbol{a}, \boldsymbol{b}$ 线性无关（不共线），则 $\mathcal{R}(A) = \mathbb{R}^2$，$\mathcal{N}(A) = \{\boldsymbol{0}\}$，$A$ 可逆。
2. 若 $\boldsymbol{a}, \boldsymbol{b}$ 线性相关且不全为零，不妨设 $\boldsymbol{a} \ne \boldsymbol{0}$，$\boldsymbol{b} = k\boldsymbol{a}$，则 $\mathcal{R}(A) = \operatorname{span}(\boldsymbol{a})$，$\mathcal{N}(A) = \operatorname{span}([k\ \ {-1}]^{\mathsf T})$，二者都是过原点的直线。
3. 若 $\boldsymbol{a} = \boldsymbol{b} = \boldsymbol{0}$，则 $\mathcal{R}(A) = \{\boldsymbol{0}\}$，$\mathcal{N}(A) = \mathbb{R}^2$。

三种情形中 $\mathcal{R}(A)$ 与 $\mathcal{N}(A)$ 的"维数"之和都是 $2$——这是定理 3.11.1 的一个特例。

**命题 3.3.2** 在 $\mathbb{R}^m$ 中，若 $n > m$，则任意 $n$ 个向量都线性相关。

**证明** 设 $A = [\boldsymbol{a}_1\ \cdots\ \boldsymbol{a}_n]$。齐次方程组 $A\boldsymbol{x} = \boldsymbol{0}$ 有 $m$ 个方程、$n > m$ 个未知量，由推论 1.8.2 有非零解。$\square$

**命题 3.3.3** 设 $\boldsymbol{b}$ 可以被 $\boldsymbol{a}_1, \dots, \boldsymbol{a}_n$ 线性表示，则表示法唯一当且仅当 $\boldsymbol{a}_1, \dots, \boldsymbol{a}_n$ 线性无关。

**证明** 记 $A = [\boldsymbol{a}_1\ \cdots\ \boldsymbol{a}_n]$，设 $A\boldsymbol{x}_0 = \boldsymbol{b}$。若向量组线性相关，存在 $\boldsymbol{y} \ne \boldsymbol{0}$ 使 $A\boldsymbol{y} = \boldsymbol{0}$，则 $A(\boldsymbol{x}_0 + \boldsymbol{y}) = \boldsymbol{b}$ 是另一种表示。反之若 $A\boldsymbol{x}_0 = A\boldsymbol{x}_1 = \boldsymbol{b}$，$\boldsymbol{x}_0 \ne \boldsymbol{x}_1$，则 $A(\boldsymbol{x}_0 - \boldsymbol{x}_1) = \boldsymbol{0}$ 说明向量组线性相关。$\square$

**命题 3.3.4** 设 $\boldsymbol{a}_1, \dots, \boldsymbol{a}_n$ 线性无关，则对任意向量 $\boldsymbol{b}$：

1. $\boldsymbol{b}$ 能被 $\boldsymbol{a}_1, \dots, \boldsymbol{a}_n$ 线性表示，当且仅当 $\boldsymbol{a}_1, \dots, \boldsymbol{a}_n, \boldsymbol{b}$ 线性相关；
2. $\boldsymbol{a}_1, \dots, \boldsymbol{a}_n, \boldsymbol{b}$ 线性无关，当且仅当 $\boldsymbol{b}$ 不能被 $\boldsymbol{a}_1, \dots, \boldsymbol{a}_n$ 线性表示。

**证明** 第 2 条是第 1 条的逆否形式。若 $\boldsymbol{b} = \sum k_i\boldsymbol{a}_i$，则 $\sum k_i\boldsymbol{a}_i - \boldsymbol{b} = \boldsymbol{0}$ 是系数不全为零（$\boldsymbol{b}$ 的系数为 $-1$）的线性关系。反之，设 $\sum k_i\boldsymbol{a}_i + k\boldsymbol{b} = \boldsymbol{0}$，系数不全为零。若 $k = 0$，则与 $\boldsymbol{a}_1, \dots, \boldsymbol{a}_n$ 线性无关矛盾；所以 $k \ne 0$，$\boldsymbol{b} = -\sum (k_i/k)\boldsymbol{a}_i$。$\square$

这个命题说明：向一个线性无关组添加一个它不能表示的向量，得到的仍是线性无关组。这是下面筛选法和基扩充定理的关键。

## 3.4. 子空间的基

**定义 3.4.1（基）** 设 $M$ 是 $\mathbb{R}^m$ 的子空间。若 $M$ 中的向量组 $\boldsymbol{a}_1, \dots, \boldsymbol{a}_n$ 满足：(1) $M = \operatorname{span}(\boldsymbol{a}_1, \dots, \boldsymbol{a}_n)$，即 $M$ 中任意向量都能被它线性表示；(2) $\boldsymbol{a}_1, \dots, \boldsymbol{a}_n$ 线性无关，则称 $\boldsymbol{a}_1, \dots, \boldsymbol{a}_n$ 为 $M$ 的一组**基**。

由命题 3.3.3，条件 (2) 可以换成"$M$ 中任意向量的表示法唯一"；由命题 3.3.2，$\mathbb{R}^m$ 的子空间的基不可能多于 $m$ 个向量。

**命题 3.4.1** 设 $A = [\boldsymbol{a}_1\ \cdots\ \boldsymbol{a}_m]$ 是 $m$ 阶方阵，则 $\boldsymbol{a}_1, \dots, \boldsymbol{a}_m$ 是 $\mathbb{R}^m$ 的一组基当且仅当 $A$ 可逆。

**证明** 若它们是基，则线性无关，$A\boldsymbol{x} = \boldsymbol{0}$ 只有零解，由定理 2.3.1 $A$ 可逆。反之若 $A$ 可逆，则 $A\boldsymbol{x} = \boldsymbol{0}$ 只有零解（线性无关），且对任意 $\boldsymbol{b}$，$A\boldsymbol{x} = \boldsymbol{b}$ 有解（生成 $\mathbb{R}^m$）。$\square$

**定义 3.4.2（标准基）** 由命题 3.4.1（取 $A = I_m$），标准坐标向量组 $\boldsymbol{e}_1, \dots, \boldsymbol{e}_m$ 是 $\mathbb{R}^m$ 的一组基，称为 $\mathbb{R}^m$ 的**标准基**。

## 3.5. 极大线性无关部分组与向量组的秩

$\mathbb{R}^m$ 的子空间是否一定有基？如何求一组基？先考虑 $\operatorname{span}(\boldsymbol{a}_1, \dots, \boldsymbol{a}_n)$，也就是列空间 $\mathcal{R}(A)$：基可以从生成向量中挑出来。

**定义 3.5.1（向量组之间的线性表示）** 设 $S, T$ 是 $\mathbb{R}^m$ 中的两个向量组。若 $S$ 中每个向量都能被 $T$ 线性表示，则称向量组 $S$ 可以被 $T$ 线性表示。

**定义 3.5.2（极大线性无关部分组）** 设 $\boldsymbol{a}_{i_1}, \dots, \boldsymbol{a}_{i_r}$ 是向量组 $\boldsymbol{a}_1, \dots, \boldsymbol{a}_n$ 的一个部分组。若 (1) $\boldsymbol{a}_{i_1}, \dots, \boldsymbol{a}_{i_r}$ 线性无关，(2) $\boldsymbol{a}_1, \dots, \boldsymbol{a}_n$ 可以被 $\boldsymbol{a}_{i_1}, \dots, \boldsymbol{a}_{i_r}$ 线性表示，则称 $\boldsymbol{a}_{i_1}, \dots, \boldsymbol{a}_{i_r}$ 为 $\boldsymbol{a}_1, \dots, \boldsymbol{a}_n$ 的一个**极大线性无关部分组**。

由定义，极大线性无关部分组就是 $\operatorname{span}(\boldsymbol{a}_1, \dots, \boldsymbol{a}_n)$ 的一组基。

**算法 3.5.1（筛选法）** 输入不全为零的向量组 $\boldsymbol{a}_1, \dots, \boldsymbol{a}_n$。依次考察 $\boldsymbol{a}_1, \boldsymbol{a}_2, \dots$：若当前向量不能被已选出的向量线性表示（对第一个非零向量，即它不为零），就把它选入；否则舍去。输出选出的部分组。

由命题 3.3.4，每一步选出的向量组都线性无关；被舍去的向量都能被已选出的向量表示，所以全部向量都能被输出的部分组表示。因此：

**命题 3.5.1** 任意有限个不全为零的向量组成的向量组都有极大线性无关部分组，筛选法给出其中一个。

**例 3.5.1** 对 $\boldsymbol{a}_1 = [1\ {-1}\ 0]^{\mathsf T}$，$\boldsymbol{a}_2 = [1\ 0\ {-1}]^{\mathsf T}$，$\boldsymbol{a}_3 = [0\ 1\ {-1}]^{\mathsf T}$：$\boldsymbol{a}_1 \ne \boldsymbol{0}$，选入；$\boldsymbol{a}_2$ 不是 $\boldsymbol{a}_1$ 的倍数，选入；$\boldsymbol{a}_3 = -\boldsymbol{a}_1 + \boldsymbol{a}_2$，舍去。$\boldsymbol{a}_1, \boldsymbol{a}_2$ 是一个极大线性无关部分组。事实上这里任意两个向量都构成极大线性无关部分组，所以极大线性无关部分组一般不唯一。

筛选法每一步都要判断一次线性表示，即解一个方程组；3.7 节给出只需一次消元的方法。为比较不同的极大线性无关部分组，先讨论向量组之间的线性表示。

**命题 3.5.2** 设 $S: \boldsymbol{a}_1, \dots, \boldsymbol{a}_n$ 与 $T: \boldsymbol{b}_1, \dots, \boldsymbol{b}_p$ 是 $\mathbb{R}^m$ 中的向量组，以下叙述等价：

1. $S$ 可以被 $T$ 线性表示；
2. 存在 $p \times n$ 矩阵 $U$ 使得 $[\boldsymbol{a}_1\ \cdots\ \boldsymbol{a}_n] = [\boldsymbol{b}_1\ \cdots\ \boldsymbol{b}_p]\,U$；
3. $\operatorname{span}(\boldsymbol{a}_1, \dots, \boldsymbol{a}_n) \subseteq \operatorname{span}(\boldsymbol{b}_1, \dots, \boldsymbol{b}_p)$。

**证明** $1 \Rightarrow 2$：设 $\boldsymbol{a}_j = u_{1j}\boldsymbol{b}_1 + \cdots + u_{pj}\boldsymbol{b}_p = [\boldsymbol{b}_1\ \cdots\ \boldsymbol{b}_p][u_{1j}\ \cdots\ u_{pj}]^{\mathsf T}$，令 $U = [u_{ij}]_{p \times n}$。$2 \Rightarrow 3$：任意 $\boldsymbol{c} \in \operatorname{span}(S)$ 可写成 $\boldsymbol{c} = [\boldsymbol{a}_1\ \cdots\ \boldsymbol{a}_n]\boldsymbol{x} = [\boldsymbol{b}_1\ \cdots\ \boldsymbol{b}_p](U\boldsymbol{x}) \in \operatorname{span}(T)$。$3 \Rightarrow 1$：显然。$\square$

**命题 3.5.3（传递性）** 若向量组 $S$ 可以被 $T$ 线性表示，$T$ 可以被 $R$ 线性表示，则 $S$ 可以被 $R$ 线性表示。

**证明** 记三个向量组排成的矩阵为 $A, B, C$。由命题 3.5.2 存在 $U, V$ 使 $A = BU$，$B = CV$，于是 $A = C(VU)$。$\square$

**命题 3.5.4** 设向量组 $\boldsymbol{a}_1, \dots, \boldsymbol{a}_n$ 可以被 $\boldsymbol{b}_1, \dots, \boldsymbol{b}_p$ 线性表示。

1. 若 $n > p$，则 $\boldsymbol{a}_1, \dots, \boldsymbol{a}_n$ 线性相关；
2. 若 $\boldsymbol{a}_1, \dots, \boldsymbol{a}_n$ 线性无关，则 $n \le p$。

**证明** 第 2 条是第 1 条的逆否形式。记 $A = [\boldsymbol{a}_1\ \cdots\ \boldsymbol{a}_n]$，$B = [\boldsymbol{b}_1\ \cdots\ \boldsymbol{b}_p]$，有 $A = BC$，$C$ 是 $p \times n$ 矩阵。$n > p$ 时 $C\boldsymbol{x} = \boldsymbol{0}$ 的未知量多于方程，有非零解 $\boldsymbol{k}$，于是 $A\boldsymbol{k} = BC\boldsymbol{k} = \boldsymbol{0}$。$\square$

直观地说，线性相关的向量组在线性生成的意义下有"多余"的向量：$n$ 个向量线性相关时，它的极大线性无关部分组少于 $n$ 个向量。

**定义 3.5.3（线性等价）** 若两个向量组可以互相线性表示，则称它们线性等价。若一个向量组与某一个向量线性等价，则称这个向量组中的向量共线。

**例 3.5.2** 设 $\boldsymbol{u} \in \mathbb{R}^m$，$\boldsymbol{v} \in \mathbb{R}^n$ 是非零向量，则

$$
\boldsymbol{u}\boldsymbol{v}^{\mathsf T} = [v_1\boldsymbol{u}\ \ v_2\boldsymbol{u}\ \cdots\ v_n\boldsymbol{u}] = \begin{bmatrix} u_1\boldsymbol{v}^{\mathsf T} \\ \vdots \\ u_m\boldsymbol{v}^{\mathsf T} \end{bmatrix},
$$

它的列向量组与 $\boldsymbol{u}$ 共线，行向量（转置后）组与 $\boldsymbol{v}$ 共线。

**命题 3.5.5** 向量组的线性等价是**等价关系**；两个向量组 $S, T$ 线性等价当且仅当 $\operatorname{span}(S) = \operatorname{span}(T)$。

**证明** 自反性、对称性由定义得到，传递性即命题 3.5.3。第二个结论由命题 3.5.2 的 $1 \Leftrightarrow 3$ 得到。$\square$

线性生成的子空间是这个等价关系的不变量。一个向量组与它的任意极大线性无关部分组线性等价，所以任意两个极大线性无关部分组彼此线性等价。

**命题 3.5.6** 若线性无关的向量组 $\boldsymbol{a}_1, \dots, \boldsymbol{a}_n$ 与 $\boldsymbol{b}_1, \dots, \boldsymbol{b}_p$ 线性等价，则 $n = p$。

**证明** 对两个方向分别用命题 3.5.4 的第 2 条，得 $n \le p$ 且 $p \le n$。$\square$

因此一个向量组的任意两个极大线性无关部分组所含向量个数相同。

**定义 3.5.4（向量组的秩）** 向量组 $S$ 的任意一个极大线性无关部分组所含向量的个数称为 $S$ 的**秩**，记为 $\operatorname{rank}(S)$。只含零向量的向量组的秩规定为零。

向量组的秩也是线性等价这一等价关系的不变量。

## 3.6. 基的存在、扩充与维数

筛选法从生成向量中挑出基。对一般的子空间，可以反过来逐个添加向量。

**定理 3.6.1（基存在定理）** 设 $M$ 是 $\mathbb{R}^m$ 的子空间，$M \ne \{\boldsymbol{0}\}$，则 $M$ 有一组基，且基中向量个数不超过 $m$。

**证明** 任取非零向量 $\boldsymbol{a}_1 \in M$。若 $M = \operatorname{span}(\boldsymbol{a}_1)$，$\boldsymbol{a}_1$ 就是一组基；否则取 $\boldsymbol{a}_2 \in M \setminus \operatorname{span}(\boldsymbol{a}_1)$，由命题 3.3.4，$\boldsymbol{a}_1, \boldsymbol{a}_2$ 线性无关。若 $M = \operatorname{span}(\boldsymbol{a}_1, \boldsymbol{a}_2)$，就得到一组基；否则继续取 $\boldsymbol{a}_3 \in M \setminus \operatorname{span}(\boldsymbol{a}_1, \boldsymbol{a}_2)$，依此类推。每一步得到的向量组都线性无关，由命题 3.3.2 其个数不超过 $m$，所以这个过程至多 $m$ 步就终止，终止时得到线性无关的 $\boldsymbol{a}_1, \dots, \boldsymbol{a}_r$（$r \le m$），且 $M = \operatorname{span}(\boldsymbol{a}_1, \dots, \boldsymbol{a}_r)$。$\square$

于是 $\mathbb{R}^m$ 的任意子空间都由有限个向量生成，都是某个矩阵的列空间：$M = \mathcal{R}([\boldsymbol{a}_1\ \cdots\ \boldsymbol{a}_r])$，$\{\boldsymbol{0}\} = \mathcal{R}(O)$。$M$ 的任意两组基线性等价且都线性无关，由命题 3.5.6，它们所含向量个数相同。

**定理 3.6.2（基扩充定理）** 设 $M, N$ 是 $\mathbb{R}^m$ 的子空间，$M \ne \{\boldsymbol{0}\}$，$M \subseteq N$，则 $M$ 的任意一组基都能扩充成 $N$ 的一组基。特别地，$\mathbb{R}^m$ 的子空间的任意一组基都能扩充成 $\mathbb{R}^m$ 的一组基。

**证明** 设 $\boldsymbol{a}_1, \dots, \boldsymbol{a}_r$ 是 $M$ 的一组基。若 $N = \operatorname{span}(\boldsymbol{a}_1, \dots, \boldsymbol{a}_r)$，它也是 $N$ 的基；否则取 $\boldsymbol{a}_{r+1} \in N \setminus \operatorname{span}(\boldsymbol{a}_1, \dots, \boldsymbol{a}_r)$，由命题 3.3.4 扩充后的向量组线性无关。依此类推，与定理 3.6.1 的证明相同，有限步后得到 $N$ 的一组基。$\square$

注意方向：先取定 $M$ 的基才能扩充；若先取定 $N$ 的一组基，它与 $M$ 一般没有关系（$N$ 的基向量可能都不在 $M$ 中）。

**定义 3.6.1（维数）** 子空间 $M$ 的任意一组基所含向量的个数称为 $M$ 的**维数**，记为 $\dim M$。规定 $\dim\{\boldsymbol{0}\} = 0$。维数为 $r$ 的子空间称为 $r$ 维子空间。

**命题 3.6.1**

1. $\dim\mathbb{R}^m = m$；
2. 若 $M$ 是 $\mathbb{R}^m$ 的子空间，则 $\dim M \le m$；
3. 若 $M \subseteq N$ 是 $\mathbb{R}^m$ 的子空间，则 $\dim M \le \dim N$；若还有 $\dim M = \dim N$，则 $M = N$。

**证明** 第 1 条由标准基得到，第 2 条由定理 3.6.1 得到。第 3 条：把 $M$ 的基扩充成 $N$ 的基（定理 3.6.2），得 $\dim M \le \dim N$；维数相等时不需要添加任何向量，$M$ 的基已生成 $N$，故 $M = N$。（$M = \{\boldsymbol{0}\}$ 的情形是平凡的。）$\square$

第 3 条的逆命题不成立：$\dim M \le \dim N$ 不能推出 $M \subseteq N$，例如 $\mathbb{R}^2$ 中两条不同的过原点的直线。

已知维数时，判断一组向量是否为基可以少验证一个条件。

**命题 3.6.2（基的判定）** 设 $M$ 是 $\mathbb{R}^m$ 的 $r$ 维子空间，$\boldsymbol{a}_1, \dots, \boldsymbol{a}_r$ 是 $M$ 中的 $r$ 个向量。

1. 若 $\boldsymbol{a}_1, \dots, \boldsymbol{a}_r$ 线性无关，则它们是 $M$ 的一组基；
2. 若 $M = \operatorname{span}(\boldsymbol{a}_1, \dots, \boldsymbol{a}_r)$，则它们是 $M$ 的一组基。

一般地，(i) $\dim M = r$，(ii) $M$ 中的 $\boldsymbol{a}_1, \dots, \boldsymbol{a}_r$ 线性无关，(iii) $M = \operatorname{span}(\boldsymbol{a}_1, \dots, \boldsymbol{a}_r)$ 三个条件中任意两个都能推出第三个。

**证明** 1. $\operatorname{span}(\boldsymbol{a}_1, \dots, \boldsymbol{a}_r) \subseteq M$，二者维数都是 $r$，由命题 3.6.1 相等。2. 若 $\boldsymbol{a}_1, \dots, \boldsymbol{a}_r$ 线性相关，则 $\dim M = \operatorname{rank}(\boldsymbol{a}_1, \dots, \boldsymbol{a}_r) < r$，矛盾。最后，(ii) 与 (iii) 合起来就是基的定义，可推出 (i)。$\square$

## 3.7. 矩阵的秩与列空间的基

**定义 3.7.1（矩阵的秩）** 矩阵 $A$ 的列空间的维数 $\dim\mathcal{R}(A)$ 称为 $A$ 的**秩**，记为 $\operatorname{rank}(A)$。

$\operatorname{rank}(A)$ 就是 $A$ 的列向量组的秩。用筛选法求列向量组的极大线性无关部分组需要多次判断线性关系。注意到列向量之间的线性关系就是 $A\boldsymbol{x} = \boldsymbol{0}$ 的解，而解集是左相抵的不变量（2.4 节），所以初等行变换不改变列向量组的线性关系。

**命题 3.7.1** 设 $A = [\boldsymbol{a}_1\ \cdots\ \boldsymbol{a}_n]$ 与 $B = [\boldsymbol{b}_1\ \cdots\ \boldsymbol{b}_n]$ 左相抵，则

1. 部分组 $\boldsymbol{a}_{i_1}, \dots, \boldsymbol{a}_{i_r}$ 线性无关当且仅当对应的部分组 $\boldsymbol{b}_{i_1}, \dots, \boldsymbol{b}_{i_r}$ 线性无关；
2. $\boldsymbol{a}_j = k_1\boldsymbol{a}_{i_1} + \cdots + k_r\boldsymbol{a}_{i_r}$ 当且仅当 $\boldsymbol{b}_j = k_1\boldsymbol{b}_{i_1} + \cdots + k_r\boldsymbol{b}_{i_r}$（系数相同）；
3. $\boldsymbol{a}_{i_1}, \dots, \boldsymbol{a}_{i_r}$ 是 $A$ 的列向量组的极大线性无关部分组，当且仅当 $\boldsymbol{b}_{i_1}, \dots, \boldsymbol{b}_{i_r}$ 是 $B$ 的列向量组的极大线性无关部分组。

**证明** 由命题 2.4.1，存在可逆矩阵 $P$ 使 $B = PA$，即 $\boldsymbol{b}_j = P\boldsymbol{a}_j$。记 $A_1 = [\boldsymbol{a}_{i_1}\ \cdots\ \boldsymbol{a}_{i_r}]$，$B_1 = PA_1$。1. $A_1\boldsymbol{x} = \boldsymbol{0}$ 当且仅当 $PA_1\boldsymbol{x} = \boldsymbol{0}$。2. 若 $\boldsymbol{a}_j = A_1\boldsymbol{k}$，则 $\boldsymbol{b}_j = PA_1\boldsymbol{k} = B_1\boldsymbol{k}$；反之左乘 $P^{-1}$。3. 由前两条得到。$\square$

**定理 3.7.1** 把 $A$ 化成阶梯形（或行简化阶梯形），则

1. 主列对应的 $A$ 的列构成 $A$ 的列向量组的一个极大线性无关部分组，即 $\mathcal{R}(A)$ 的一组基，$\operatorname{rank}(A)$ 等于阶梯数；
2. $A$ 的每个自由列被这组基线性表示的系数，就是行简化阶梯形中对应列的前 $r$ 个元素。

**证明** 设 $R = \operatorname{rref}(A)$ 有 $r$ 个主元，则 $R$ 的主列依次是 $\boldsymbol{e}_1, \dots, \boldsymbol{e}_r$，线性无关；由于 $R$ 的后 $m - r$ 行全为零，每个自由列 $[c_1\ \cdots\ c_r\ 0\ \cdots\ 0]^{\mathsf T} = c_1\boldsymbol{e}_1 + \cdots + c_r\boldsymbol{e}_r$。所以 $R$ 的主列构成 $R$ 的列向量组的极大线性无关部分组。由命题 3.7.1，这些结论对 $A$ 的对应列成立。阶梯形与行简化阶梯形的主列位置相同。$\square$

**推论 3.7.1** 矩阵的行简化阶梯形是唯一的。

**证明** 设 $R, R'$ 都是 $A$ 的行简化阶梯形，则 $R$ 与 $R'$ 左相抵，由命题 3.7.1，二者的列向量组有相同的线性关系。在行简化阶梯形中，第 $j$ 列是主列当且仅当它不能被前面的列线性表示（主列是一个新的 $\boldsymbol{e}_k$，前面的列都属于 $\operatorname{span}(\boldsymbol{e}_1, \dots, \boldsymbol{e}_{k-1})$；自由列能被前面的主列表示）。所以 $R$ 与 $R'$ 的主列位置相同，主列依次都是 $\boldsymbol{e}_1, \dots, \boldsymbol{e}_r$。每个自由列被主列线性表示的方式唯一（命题 3.3.3），而它的元素就是表示系数，在 $R$ 与 $R'$ 中相同。故 $R = R'$。$\square$

于是左相抵的标准形（2.4 节）唯一，两个 $m \times n$ 矩阵左相抵当且仅当它们的行简化阶梯形相同。

**算法 3.7.1（列向量组的极大线性无关部分组）** 输入 $A = [\boldsymbol{a}_1\ \cdots\ \boldsymbol{a}_n]$。

1. 用初等行变换把 $A$ 化成行简化阶梯形 $R$（只需判断秩时，化成阶梯形即可）；
2. 主列的序号为 $j_1 < \cdots < j_r$，则 $\boldsymbol{a}_{j_1}, \dots, \boldsymbol{a}_{j_r}$ 是一个极大线性无关部分组，$\operatorname{rank}(A) = r$；
3. 若 $R$ 的第 $j$ 列为 $[c_1\ \cdots\ c_r\ 0\ \cdots\ 0]^{\mathsf T}$，则 $\boldsymbol{a}_j = c_1\boldsymbol{a}_{j_1} + \cdots + c_r\boldsymbol{a}_{j_r}$。

**例 3.7.1** 对例 1.8.1 的系数矩阵

$$
A = [\boldsymbol{a}_1\ \cdots\ \boldsymbol{a}_5] = \begin{bmatrix} 1 & 1 & 0 & -3 & -1 \\ 1 & -1 & 2 & -1 & 0 \\ 4 & -2 & 6 & 3 & -4 \\ 2 & 4 & -2 & 4 & -7 \end{bmatrix}, \qquad
\operatorname{rref}(A) = \begin{bmatrix} 1 & 0 & 1 & 0 & -\frac76 \\ 0 & 1 & -1 & 0 & -\frac56 \\ 0 & 0 & 0 & 1 & -\frac13 \\ 0 & 0 & 0 & 0 & 0 \end{bmatrix}.
$$

主列是第 $1, 2, 4$ 列，所以 $\boldsymbol{a}_1, \boldsymbol{a}_2, \boldsymbol{a}_4$ 是一个极大线性无关部分组，$\operatorname{rank}(A) = 3$，且

$$
\boldsymbol{a}_3 = \boldsymbol{a}_1 - \boldsymbol{a}_2, \qquad \boldsymbol{a}_5 = -\tfrac76\boldsymbol{a}_1 - \tfrac56\boldsymbol{a}_2 - \tfrac13\boldsymbol{a}_4.
$$

计算机代数系统按同样的方法做精确计算。数值计算中则要小心：浮点数的舍入会把"恰好为零"的主元变成很小的非零数，用消元判断秩是不可靠的，数值软件改用奇异值（[第 7 章](/2.1.7)）并设定容差：

```python
import numpy as np
import sympy as sp

A = sp.Matrix([[1, 1, 0, -3, -1],
               [1, -1, 2, -1, 0],
               [4, -2, 6, 3, -4],
               [2, 4, -2, 4, -7]])
R, pivots = A.rref()           # exact Gauss-Jordan elimination
print(pivots)                  # (0, 1, 3): columns a1, a2, a4
print(A.rank())                # 3

# A perturbation of size 1e-12 makes the matrix "exactly" full rank,
# while a tolerance-based numerical rank still reports 3
B = np.array(A.tolist(), dtype=float)
B[3, 4] += 1e-12
print(np.linalg.matrix_rank(B), np.linalg.matrix_rank(B, tol=1e-8))  # 4 3
```

## 3.8. 行空间与满秩

**定义 3.8.1（行空间）** 设 $A$ 是 $m \times n$ 矩阵，$\mathbb{R}^n$ 的子空间 $\mathcal{R}(A^{\mathsf T})$（由 $A$ 的行向量转置后生成）称为 $A$ 的**行空间**。

$A$ 的行向量对应于方程组 $A\boldsymbol{x} = \boldsymbol{0}$ 的方程，行空间的维数 $\operatorname{rank}(A^{\mathsf T})$ 描述了"有效"方程的个数。

**例 3.8.1** 把例 3.7.1 的 $A$ 化成阶梯形 $B$，并记录每一行是原来哪些行的组合（$\tilde{\boldsymbol{a}}_i^{\mathsf T}$ 是 $A$ 的第 $i$ 行）：

$$
B = \begin{bmatrix} 1 & 1 & 0 & -3 & -1 \\ 0 & -2 & 2 & 2 & 1 \\ 0 & 0 & 0 & 9 & -3 \\ 0 & 0 & 0 & 0 & 0 \end{bmatrix}
\begin{matrix} \tilde{\boldsymbol{a}}_1^{\mathsf T} \\ \tilde{\boldsymbol{a}}_2^{\mathsf T} - \tilde{\boldsymbol{a}}_1^{\mathsf T} \\ \tilde{\boldsymbol{a}}_3^{\mathsf T} - 3\tilde{\boldsymbol{a}}_2^{\mathsf T} - \tilde{\boldsymbol{a}}_1^{\mathsf T} \\ \tilde{\boldsymbol{a}}_4^{\mathsf T} - \frac43\tilde{\boldsymbol{a}}_3^{\mathsf T} + 5\tilde{\boldsymbol{a}}_2^{\mathsf T} - \frac53\tilde{\boldsymbol{a}}_1^{\mathsf T} \end{matrix}
$$

由零行得 $\tilde{\boldsymbol{a}}_4 = \frac53\tilde{\boldsymbol{a}}_1 - 5\tilde{\boldsymbol{a}}_2 + \frac43\tilde{\boldsymbol{a}}_3$：例 1.8.1 中第 4 个方程是"多余"的。

**命题 3.8.1** 若 $A$ 与 $B$ 左相抵，则 $\mathcal{R}(A^{\mathsf T}) = \mathcal{R}(B^{\mathsf T})$。特别地，$A$ 化成的阶梯形的非零行（转置后）构成 $\mathcal{R}(A^{\mathsf T})$ 的一组基，$\operatorname{rank}(A^{\mathsf T})$ 等于阶梯数。

**证明** 设 $B = PA$，$P$ 可逆，则 $B^{\mathsf T} = A^{\mathsf T}P^{\mathsf T}$，由命题 3.5.2 得 $\mathcal{R}(B^{\mathsf T}) \subseteq \mathcal{R}(A^{\mathsf T})$；由 $A = P^{-1}B$ 得反向包含。阶梯形的非零行生成行空间；它们线性无关：若 $\sum_i k_i\tilde{\boldsymbol{b}}_i = \boldsymbol{0}$，看第一个主元所在的列，只有第 1 行在该列非零，得 $k_1 = 0$；再看第二个主元所在的列，得 $k_2 = 0$，依此类推。$\square$

例 3.8.1 中，$B$ 的三个非零行是行空间的一组基；由于 $\tilde{\boldsymbol{a}}_4$ 能被前三行表示，$\tilde{\boldsymbol{a}}_1, \tilde{\boldsymbol{a}}_2, \tilde{\boldsymbol{a}}_3$ 也是一组基。结合定理 3.7.1 立得：

**定理 3.8.1** 对 $m \times n$ 矩阵 $A$，$\operatorname{rank}(A^{\mathsf T}) = \operatorname{rank}(A)$，都等于 $A$ 化成的阶梯形的阶梯数。因此 $\operatorname{rank}(A) \le \min\{m, n\}$。

注意 $\mathcal{R}(A) \subseteq \mathbb{R}^m$ 与 $\mathcal{R}(A^{\mathsf T}) \subseteq \mathbb{R}^n$ 是不同空间中的子空间，只是维数相同。

**定义 3.8.2（满秩）** 设 $A$ 是 $m \times n$ 矩阵。若 $\operatorname{rank}(A) = n$（列向量组线性无关），称 $A$ **列满秩**；若 $\operatorname{rank}(A) = m$，称 $A$ **行满秩**；若 $\operatorname{rank}(A) = m = n$，称 $A$ **满秩**。

列满秩矩阵满足 $n \le m$（"高"矩阵），行满秩矩阵满足 $m \le n$（"宽"矩阵），满秩矩阵一定是方阵；行满秩或列满秩的方阵一定满秩。

**命题 3.8.2** 设 $A$ 是 $m \times n$ 矩阵，$T_A\colon \boldsymbol{x} \mapsto A\boldsymbol{x}$，则

1. $T_A$ 是满射当且仅当 $A$ 行满秩；
2. $T_A$ 是单射当且仅当 $A$ 列满秩；
3. $T_A$ 是**双射**当且仅当 $A$ 满秩。

**证明** 1. 满射即 $\mathcal{R}(A) = \mathbb{R}^m$；由 $\mathcal{R}(A) \subseteq \mathbb{R}^m$ 和命题 3.6.1，这等价于 $\dim\mathcal{R}(A) = m$。2. 单射即 $A\boldsymbol{x} = \boldsymbol{0}$ 只有零解，即列向量组线性无关，即 $\operatorname{rank}(A) = n$。3. 由前两条得到。$\square$

特别地，方阵 $A$ 可逆当且仅当 $A$ 满秩；$A = O$ 当且仅当 $\operatorname{rank}(A) = 0$。满秩条件也刻画了单边逆的存在，这与映射的**左逆**、**右逆**（[1.2.3 的定理 3.2.8](/1.2.3#thm-3.2.8)）相对应：

**命题 3.8.3（单边逆）** 设 $A$ 是 $m \times n$ 矩阵。$A$ 列满秩当且仅当存在 $n \times m$ 矩阵 $B$ 使 $BA = I_n$；$A$ 行满秩当且仅当存在 $n \times m$ 矩阵 $B$ 使 $AB = I_m$。

**证明** 若 $A$ 列满秩，则 $\operatorname{rref}(A) = \begin{bmatrix} I_n \\ O \end{bmatrix}$，即存在可逆矩阵 $P$ 使 $PA = \begin{bmatrix} I_n \\ O \end{bmatrix}$；取 $B = [I_n\ O]P$，则 $BA = I_n$。反之若 $BA = I_n$，由 $A\boldsymbol{x} = \boldsymbol{0}$ 得 $\boldsymbol{x} = BA\boldsymbol{x} = \boldsymbol{0}$，$A$ 列满秩。行满秩的情形对 $A^{\mathsf T}$ 应用前一结论，并用定理 3.8.1。$\square$

**命题 3.8.4（乘积的列空间与秩）** 设 $A, B$ 分别是 $\ell \times m$、$m \times n$ 矩阵，则

1. $\mathcal{R}(AB) \subseteq \mathcal{R}(A)$，若 $B$ 可逆则 $\mathcal{R}(AB) = \mathcal{R}(A)$；
2. $\operatorname{rank}(AB) \le \operatorname{rank}(A)$，$\operatorname{rank}(AB) \le \operatorname{rank}(B)$；若 $B$ 可逆则 $\operatorname{rank}(AB) = \operatorname{rank}(A)$，若 $A$ 可逆则 $\operatorname{rank}(AB) = \operatorname{rank}(B)$。

**证明** 1. $AB = [A\boldsymbol{b}_1\ \cdots\ A\boldsymbol{b}_n]$ 的每一列都属于 $\mathcal{R}(A)$。$B$ 可逆时，又有 $\mathcal{R}(A) = \mathcal{R}((AB)B^{-1}) \subseteq \mathcal{R}(AB)$。2. 由第 1 条得 $\operatorname{rank}(AB) \le \operatorname{rank}(A)$，$B$ 可逆时取等号。由定理 3.8.1，$\operatorname{rank}(AB) = \operatorname{rank}(B^{\mathsf T}A^{\mathsf T}) \le \operatorname{rank}(B^{\mathsf T}) = \operatorname{rank}(B)$。$A$ 可逆时 $AB$ 与 $B$ 左相抵，由命题 3.7.1 列向量组的秩相同。$\square$

从映射的角度看，$T_A \circ T_B$ 的像集包含在 $T_A$ 的像集中。一般 $\mathcal{R}(AB) \ne \mathcal{R}(B)$（二者甚至不在同一个空间中）。

## 3.9. 相抵与相抵标准形

**命题 3.9.1** 设 $A$ 是 $m \times n$ 矩阵，$P, Q$ 分别是 $m$ 阶、$n$ 阶可逆矩阵，则 $\operatorname{rank}(PAQ) = \operatorname{rank}(A)$。

**证明** 两次应用命题 3.8.4。$\square$

由于可逆矩阵恰是初等矩阵的乘积，这说明秩在初等行变换和初等列变换下都不变。

**定义 3.9.1（相抵）** 若矩阵 $A$ 可以经过一系列初等行变换和初等列变换化成矩阵 $B$，则称 $A$ 与 $B$ **相抵**。

**命题 3.9.2** 两个 $m \times n$ 矩阵 $A, B$ 相抵，当且仅当存在 $m$ 阶可逆矩阵 $P$ 和 $n$ 阶可逆矩阵 $Q$ 使得 $PAQ = B$。相抵是 $\mathbb{R}^{m \times n}$ 上的**等价关系**，初等行、列变换是它的等价变换，秩是它的不变量。

**定理 3.9.1（相抵标准形）** 设 $A$ 是 $m \times n$ 矩阵，$r = \operatorname{rank}(A)$，则存在 $m$ 阶可逆矩阵 $P$ 和 $n$ 阶可逆矩阵 $Q$，使得

$$
PAQ = D_r = \begin{bmatrix} I_r & O \\ O & O \end{bmatrix}.
$$

$D_r$ 称为 $A$ 的相抵标准形。

**证明** 先用初等行变换把 $A$ 化成行简化阶梯形 $R$，它有 $r$ 个主列，依次是 $\boldsymbol{e}_1, \dots, \boldsymbol{e}_r$，自由列都能被主列线性表示，因此可以用倍加列变换把自由列都化为零；再用对换列变换把 $\boldsymbol{e}_j$ 移到第 $j$ 列（$j = 1, \dots, r$），就得到 $D_r$。$\square$

**推论 3.9.1** 两个 $m \times n$ 矩阵相抵当且仅当它们的秩相等。$m \times n$ 矩阵在相抵关系下共有 $\min\{m, n\} + 1$ 个等价类（$r = 0, 1, \dots, \min\{m, n\}$）。

**证明** 秩相等时二者都相抵于同一个 $D_r$，由传递性相抵；反之由命题 3.9.1。$\square$

所以秩是相抵关系的完全不变量：一个数就刻画了矩阵在左右乘可逆矩阵下的全部信息。[第 8 章](/2.1.8)将看到，这对应于"适当选取定义域与陪域的基后，线性映射的矩阵可以化成 $D_r$"。

## 3.10. 线性方程组的解集

设 $A$ 是 $m \times n$ 矩阵，$\operatorname{rank}(A) = r$。齐次方程组 $A\boldsymbol{x} = \boldsymbol{0}$ 的解集就是零空间 $\mathcal{N}(A)$。把 $A$ 化成行简化阶梯形，有 $r$ 个主列和 $n - r$ 个自由列；自由变量的值一旦确定，主变量就唯一确定。设 $\boldsymbol{k}_i$（$i = 1, \dots, n - r$）是第 $i$ 个自由变量取 $1$、其余自由变量都取 $0$ 时得到的解。

**定理 3.10.1** 上述 $\boldsymbol{k}_1, \dots, \boldsymbol{k}_{n-r}$ 是 $\mathcal{N}(A)$ 的一组基。特别地，$\dim\mathcal{N}(A) = n - \operatorname{rank}(A)$。

**证明** 生成：显然 $\operatorname{span}(\boldsymbol{k}_1, \dots, \boldsymbol{k}_{n-r}) \subseteq \mathcal{N}(A)$。任取 $\boldsymbol{k} \in \mathcal{N}(A)$，设它在 $n - r$ 个自由变量上的取值依次为 $c_1, \dots, c_{n-r}$，令 $\boldsymbol{k}' = c_1\boldsymbol{k}_1 + \cdots + c_{n-r}\boldsymbol{k}_{n-r} - \boldsymbol{k}$。$\boldsymbol{k}' \in \mathcal{N}(A)$ 且在自由变量上的取值全为零，于是 $A\boldsymbol{k}' = \boldsymbol{0}$ 说明主列的一个线性组合为零；主列线性无关，所以 $\boldsymbol{k}'$ 在主变量上的取值也全为零，$\boldsymbol{k}' = \boldsymbol{0}$。线性无关：若 $c_1\boldsymbol{k}_1 + \cdots + c_{n-r}\boldsymbol{k}_{n-r} = \boldsymbol{0}$，比较第 $i$ 个自由变量所在的分量，得 $c_i = 0$。$\square$

**例 3.10.1** 例 1.8.1 中自由变量是 $x_3, x_5$。由通解 $x_1 = -x_3 + \frac76x_5$，$x_2 = x_3 + \frac56x_5$，$x_4 = \frac13x_5$，取 $(x_3, x_5) = (1, 0)$ 与 $(0, 1)$ 得

$$
\boldsymbol{k}_1 = \begin{bmatrix} -1 \\ 1 \\ 1 \\ 0 \\ 0 \end{bmatrix}, \qquad \boldsymbol{k}_2 = \begin{bmatrix} \frac76 \\ \frac56 \\ 0 \\ \frac13 \\ 1 \end{bmatrix},
$$

$\mathcal{N}(A) = \{x_3\boldsymbol{k}_1 + x_5\boldsymbol{k}_2 \mid x_3, x_5 \in \mathbb{R}\}$，$\dim\mathcal{N}(A) = 2 = 5 - 3$。

反过来，由零空间的一组基也能写出行简化阶梯形的非零行。例如已知 $4 \times 5$ 矩阵 $A$ 的零空间以上面的 $\boldsymbol{k}_1, \boldsymbol{k}_2$ 为基，则 $\mathcal{N}(A)$ 中的向量形如 $[-c_1 + \frac76c_2\ \ c_1 + \frac56c_2\ \ c_1\ \ \frac13c_2\ \ c_2]^{\mathsf T}$，即 $x_3 = c_1$，$x_5 = c_2$ 是自由变量，且 $x_1 + x_3 - \frac76x_5 = 0$，$x_2 - x_3 - \frac56x_5 = 0$，$x_4 - \frac13x_5 = 0$。这三个方程的系数就是 $\operatorname{rref}(A)$ 的三个非零行（由推论 3.7.1，行简化阶梯形由零空间唯一确定）。

非齐次方程组的解集不是子空间，但它是零空间的平移。设 $A\boldsymbol{x} = \boldsymbol{b}$ 有一个特解 $\boldsymbol{k}_0$，则 $\boldsymbol{k}$ 是解当且仅当 $A(\boldsymbol{k} - \boldsymbol{k}_0) = \boldsymbol{0}$。于是 $\boldsymbol{k} \mapsto \boldsymbol{k} - \boldsymbol{k}_0$ 是解集 $\{\boldsymbol{x} \mid A\boldsymbol{x} = \boldsymbol{b}\}$ 到 $\mathcal{N}(A)$ 的双射，逆映射为 $\boldsymbol{k}' \mapsto \boldsymbol{k}' + \boldsymbol{k}_0$。$A\boldsymbol{x} = \boldsymbol{0}$ 称为 $A\boldsymbol{x} = \boldsymbol{b}$ 的导出方程组。

**定理 3.10.2（非齐次方程组的解集）** 设 $A\boldsymbol{x} = \boldsymbol{b}$ 有特解 $\boldsymbol{k}_0$，$\boldsymbol{k}_1, \dots, \boldsymbol{k}_{n-r}$ 是 $\mathcal{N}(A)$ 的一组基，$r = \operatorname{rank}(A)$，则 $A\boldsymbol{x} = \boldsymbol{b}$ 的解集为

$$
\boldsymbol{k}_0 + \mathcal{N}(A) = \{\boldsymbol{k}_0 + c_1\boldsymbol{k}_1 + \cdots + c_{n-r}\boldsymbol{k}_{n-r} \mid c_1, \dots, c_{n-r} \in \mathbb{R}\}.
$$

几何上，$A\boldsymbol{x} = \boldsymbol{b}$ 的解集是把过原点的子空间 $\mathcal{N}(A)$ 平移 $\boldsymbol{k}_0$ 得到的集合，与 $\mathcal{N}(A)$ 平行、维数相同，但不过原点。例如方程组 $x_1 + x_2 + x_3 = 1$，$x_1 - x_2 = 0$ 中 $\operatorname{rank}(A) = 2$，$\mathcal{N}(A) = \operatorname{span}([1\ 1\ {-2}]^{\mathsf T})$ 是 $\mathbb{R}^3$ 中过原点的直线，一个特解是 $\boldsymbol{k}_0 = [\frac12\ \frac12\ 0]^{\mathsf T}$：

![方程组 x₁ + x₂ + x₃ = 1, x₁ − x₂ = 0 的解集：两个平面的交线 k₀ + N(A)（红）与零空间 N(A)（绿色虚线）平行，二者相差一个特解 k₀](./plots/solution-set-translate.py)

第 1 章的判定定理（定理 1.7.2）可以用秩重新叙述：

**定理 3.10.3（判定定理）** 对 $n$ 个未知量的线性方程组 $A\boldsymbol{x} = \boldsymbol{b}$：

1. 无解当且仅当 $\operatorname{rank}(A) < \operatorname{rank}([A\ \boldsymbol{b}])$，即 $\boldsymbol{b} \notin \mathcal{R}(A)$；有解当且仅当 $\operatorname{rank}(A) = \operatorname{rank}([A\ \boldsymbol{b}])$，即 $\boldsymbol{b} \in \mathcal{R}(A)$；
2. 有唯一解当且仅当 $\operatorname{rank}(A) = \operatorname{rank}([A\ \boldsymbol{b}]) = n$，即有解且 $\dim\mathcal{N}(A) = 0$；
3. 有无穷多组解当且仅当 $\operatorname{rank}(A) = \operatorname{rank}([A\ \boldsymbol{b}]) < n$，即有解且 $\dim\mathcal{N}(A) > 0$。

把这些结论合起来，就是求解线性方程组的完整标准流程：

**算法 3.10.1（线性方程组的通解）** 输入 $A\boldsymbol{x} = \boldsymbol{b}$。

1. 把 $[A\ \boldsymbol{b}]$ 化成行简化阶梯形，比较 $\operatorname{rank}(A)$ 与 $\operatorname{rank}([A\ \boldsymbol{b}])$；不等则无解，结束。
2. 令所有自由变量为 $0$，读出特解 $\boldsymbol{k}_0$（主变量的值就是最后一列的对应元素）。
3. 对每个自由变量，令它为 $1$、其余自由变量为 $0$，并把右端项换成零，得到 $\mathcal{N}(A)$ 的基向量 $\boldsymbol{k}_i$。
4. 通解为 $\boldsymbol{k}_0 + c_1\boldsymbol{k}_1 + \cdots + c_{n-r}\boldsymbol{k}_{n-r}$。

**例 3.10.2** 求 $\begin{cases} x_1 - x_2 + x_4 - x_5 = 1, \\ 2x_1 + x_3 - x_5 = 2, \\ 3x_1 - x_2 - x_3 - x_4 - x_5 = 0 \end{cases}$ 的解集。

$$
[A\ \boldsymbol{b}] = \begin{bmatrix} 1 & -1 & 0 & 1 & -1 & 1 \\ 2 & 0 & 1 & 0 & -1 & 2 \\ 3 & -1 & -1 & -1 & -1 & 0 \end{bmatrix} \to
\begin{bmatrix} 1 & 0 & 0 & -\frac12 & -\frac14 & \frac14 \\ 0 & 1 & 0 & -\frac32 & \frac34 & -\frac34 \\ 0 & 0 & 1 & 1 & -\frac12 & \frac32 \end{bmatrix}.
$$

$\operatorname{rank}(A) = \operatorname{rank}([A\ \boldsymbol{b}]) = 3 < 5$，有无穷多组解；第 $1, 2, 3$ 列是主列，$x_4, x_5$ 是自由变量。解满足 $x_1 = \frac14 + \frac12x_4 + \frac14x_5$，$x_2 = -\frac34 + \frac32x_4 - \frac34x_5$，$x_3 = \frac32 - x_4 + \frac12x_5$，解集为

$$
\left\{ \begin{bmatrix} \frac14 \\ -\frac34 \\ \frac32 \\ 0 \\ 0 \end{bmatrix} + c_1\begin{bmatrix} \frac12 \\ \frac32 \\ -1 \\ 1 \\ 0 \end{bmatrix} + c_2\begin{bmatrix} \frac14 \\ -\frac34 \\ \frac12 \\ 0 \\ 1 \end{bmatrix} \;\middle|\; c_1, c_2 \in \mathbb{R} \right\},
$$

第一个向量是 $x_4 = x_5 = 0$ 时的特解，后两个向量是 $\mathcal{N}(A)$ 的一组基。

## 3.11. 四个基本子空间与维数公式

前面出现了三个由矩阵导出的子空间：列空间 $\mathcal{R}(A)$、零空间 $\mathcal{N}(A)$、行空间 $\mathcal{R}(A^{\mathsf T})$。再补上第四个：

**定义 3.11.1（左零空间）** 设 $A$ 是 $m \times n$ 矩阵，$\mathbb{R}^m$ 的子空间 $\mathcal{N}(A^{\mathsf T})$ 称为 $A$ 的**左零空间**。

向量 $\boldsymbol{y} \in \mathcal{N}(A^{\mathsf T})$ 满足 $\boldsymbol{y}^{\mathsf T}A = (A^{\mathsf T}\boldsymbol{y})^{\mathsf T} = \boldsymbol{0}^{\mathsf T}$，即 $\boldsymbol{y}$ 给出 $A$ 的行向量之间的一个线性关系。

**定理 3.11.1（秩–零化度定理）** 设 $A$ 是 $m \times n$ 矩阵，则

$$
\dim\mathcal{R}(A) + \dim\mathcal{N}(A) = n, \qquad \dim\mathcal{R}(A^{\mathsf T}) + \dim\mathcal{N}(A^{\mathsf T}) = m.
$$

**证明** 第一式即定理 3.10.1。对 $A^{\mathsf T}$ 应用第一式，并用 $\operatorname{rank}(A^{\mathsf T}) = \operatorname{rank}(A)$（定理 3.8.1），得第二式。$\square$

这两式就是四个子空间的维数公式。从方程组的角度看：$\dim\mathcal{R}(A)$ 是主变量个数，$\dim\mathcal{N}(A)$ 是自由变量个数，相加是未知量总数 $n$；$\dim\mathcal{R}(A^{\mathsf T})$ 是有效方程个数，$\dim\mathcal{N}(A^{\mathsf T})$ 是多余方程个数（左零空间中的非零向量正是例 3.8.1 那样的行之间的线性关系），相加是方程总数 $m$。

| 子空间 | 所在空间 | 维数 | 一组基（由消元得到） |
|---|---|---|---|
| 列空间 $\mathcal{R}(A)$ | $\mathbb{R}^m$ | $r$ | $A$ 的主列（算法 3.7.1） |
| 零空间 $\mathcal{N}(A)$ | $\mathbb{R}^n$ | $n - r$ | 自由变量逐个取 $1$ 的解（定理 3.10.1） |
| 行空间 $\mathcal{R}(A^{\mathsf T})$ | $\mathbb{R}^n$ | $r$ | 阶梯形的非零行（命题 3.8.1） |
| 左零空间 $\mathcal{N}(A^{\mathsf T})$ | $\mathbb{R}^m$ | $m - r$ | 对 $A^{\mathsf T}$ 求零空间，或记录消元中零行的组合系数 |

对例 3.7.1 的 $4 \times 5$ 矩阵，四个子空间的维数依次是 $3, 2, 3, 1$，左零空间由 $[-\frac53\ \ 5\ \ {-\frac43}\ \ 1]^{\mathsf T}$ 生成（例 3.8.1 的零行）。[第 4 章](/2.1.4)将证明 $\mathcal{N}(A)$ 与 $\mathcal{R}(A^{\mathsf T})$、$\mathcal{N}(A^{\mathsf T})$ 与 $\mathcal{R}(A)$ 分别互为正交补，这是最小二乘法的几何基础。

下图以秩为 $1$ 的矩阵 $A = \begin{bmatrix} 1 & 2 \\ 3 & 6 \end{bmatrix}$ 为例画出四个基本子空间。定义域中的 $\boldsymbol{x}$ 可以分解成行空间中的 $\boldsymbol{x}_r$ 与零空间中的 $\boldsymbol{x}_n$ 之和（[第 4 章](/2.1.4)），由于 $A\boldsymbol{x}_n = \boldsymbol{0}$，$A\boldsymbol{x} = A\boldsymbol{x}_r$ 落在列空间中；与 $\boldsymbol{x}$ 相差一个零空间向量的所有向量有相同的像，它们构成 $A\boldsymbol{x} = \boldsymbol{b}$ 的解集。

![秩为 1 的矩阵 A（两行为 (1, 2) 与 (3, 6)）的四个基本子空间。左：定义域中的行空间与零空间，x = x_r + x_n，虚线是 Ax = b 的解集 x + N(A)；右：陪域中的列空间与左零空间，b = Ax 位于列空间中。图中两对子空间互相垂直，这将在第 4 章证明](./plots/four-subspaces.py)

## 小结

本章用"线性表示"的语言回答了解集的结构问题；核心不变量是秩。

| 类别 | 内容 |
|---|---|
| 定义 | 子空间（定义 3.2.1）；列空间与零空间（定义 3.2.2）；线性生成（定义 3.3.1）；线性相关与线性无关（定义 3.3.2）；基与标准基（定义 3.4.1、3.4.2）；向量组之间的线性表示、极大线性无关部分组、线性等价、向量组的秩（定义 3.5.1–3.5.4）；维数（定义 3.6.1）；矩阵的秩（定义 3.7.1）；行空间（定义 3.8.1）；行满秩、列满秩、满秩（定义 3.8.2）；相抵（定义 3.9.1）；左零空间（定义 3.11.1） |
| 定理 | 单射、满射与 $\mathcal{N}(A)$、$\mathcal{R}(A)$（命题 3.1.2）；$n > m$ 个向量必相关（命题 3.3.2）；表示唯一 $\Leftrightarrow$ 线性无关（命题 3.3.3）；方阵的列是基 $\Leftrightarrow$ 可逆（命题 3.4.1）；向量组的线性表示与个数（命题 3.5.2–3.5.6）；基存在定理与基扩充定理（定理 3.6.1、3.6.2）；基的判定（命题 3.6.2）；行变换保持列的线性关系（命题 3.7.1）；主列构成列空间的基（定理 3.7.1）；rref 唯一（推论 3.7.1）；$\operatorname{rank}(A^{\mathsf T}) = \operatorname{rank}(A)$（定理 3.8.1）；满秩与单射、满射、单边逆（命题 3.8.2、3.8.3）；乘积的秩（命题 3.8.4）；相抵标准形（定理 3.9.1）；零空间的基与 $\dim\mathcal{N}(A) = n - r$（定理 3.10.1）；解集 $= \boldsymbol{k}_0 + \mathcal{N}(A)$（定理 3.10.2）；基于秩的判定定理（定理 3.10.3）；秩–零化度定理（定理 3.11.1） |
| 算法 | 筛选法（算法 3.5.1）；用行简化阶梯形求极大线性无关部分组（算法 3.7.1）；线性方程组的通解（算法 3.10.1） |

| 条件（$A$ 是 $m \times n$ 矩阵，$r = \operatorname{rank}(A)$） | 映射 $\boldsymbol{x} \mapsto A\boldsymbol{x}$ | 方程组 | 逆 |
|---|---|---|---|
| $r = n$（列满秩） | 单射，$\mathcal{N}(A) = \{\boldsymbol{0}\}$ | $A\boldsymbol{x} = \boldsymbol{b}$ 至多一个解 | 存在左逆 $BA = I_n$ |
| $r = m$（行满秩） | 满射，$\mathcal{R}(A) = \mathbb{R}^m$ | 对任意 $\boldsymbol{b}$ 有解 | 存在右逆 $AB = I_m$ |
| $r = m = n$（满秩） | 双射 | 对任意 $\boldsymbol{b}$ 有唯一解 | 可逆 |
