---
title: 不变子空间与 Jordan 标准形
---

[第 6 章](/2.1.6)提出了**相似**分类的问题：在 $\{P^{-1}AP \mid P \text{ 可逆}\}$ 中找一个最简单的代表。**可对角化**的矩阵可以化成对角阵，但亏损的矩阵不行，第 6 章只陈述了答案（定理 6.10.1）：每个复方阵都相似于一个 **Jordan 标准形**，在不计块的顺序时唯一。本章给出这个定理的完整证明，并把 Jordan 形与 Jordan 基的计算整理成一条标准流程。

同一个问题有两种说法。设 $V$ 是 $n$ 维复空间，**线性变换** $T\colon V \to V$ 在基 $v_1, \dots, v_n$ 下的矩阵为 $A$，即 $(Tv_1, \dots, Tv_n) = (v_1, \dots, v_n)A$。

| 线性变换语言 | 矩阵语言 |
|---|---|
| 求一组新基 $w_1, \dots, w_n$，使 $T$ 的矩阵最简单 | 求可逆阵 $P$，$(w_1, \dots, w_n) = (v_1, \dots, v_n)P$ |
| $T$ 在新基下的矩阵为 $J$ | $J = P^{-1}AP$ |
| 对 $\dim V$ 归纳，把 $V$ 分解成不变子空间的直和 | 对阶数归纳，化成分块对角阵 |

证明的路线分三步：用 Schur 定理把 $A$ 相似于上三角阵；用根子空间分解把它化成分块对角阵，每一块只有一个特征值；最后用幂零变换的循环子空间分解把每一块化成 Jordan 块。每一步都只用到可以机械执行的运算：求特征多项式的根（[第 9 章](/2.1.9)的多项式理论）、用消元法计算秩、解线性方程组。特别地，Jordan 形本身只由一列秩 $\operatorname{rank}\left((A - \mu I)^k\right)$ 决定，不必先求出 $P$。本章的 Jordan 形是[下一章](/2.1.11)计算矩阵函数 $f(A) = Pf(J)P^{-1}$ 的基础。

## 10.1. 子空间的直和

[第 8 章](/2.1.8)讨论了两个子空间的和与直和，Jordan 形的证明需要把空间分解成多个子空间。

**定义 10.1.1（直和）** 设 $V_1, \dots, V_k$ 是复空间 $V$ 的子空间。称

$$
V_1 + \cdots + V_k = \{v_1 + \cdots + v_k \mid v_i \in V_i\}
$$

为它们的和，它仍是子空间。若和中每个向量写成 $v_1 + \cdots + v_k$（$v_i \in V_i$）的方式唯一，则称这个和为直和，记作 $V_1 \oplus \cdots \oplus V_k$。

**定理 10.1.1** $V_1 + \cdots + V_k$ 是直和的以下条件等价：

1. $\dim V_1 + \cdots + \dim V_k = \dim(V_1 + \cdots + V_k)$；
2. $V_1, \dots, V_k$ 的基的不交并是 $V_1 + \cdots + V_k$ 的基；
3. 零向量的表示唯一：若 $0 = v_1 + \cdots + v_k$，$v_i \in V_i$，则 $v_1 = \cdots = v_k = 0$；
4. 对每个 $i$，$V_i \cap \sum_{j \ne i} V_j = \{0\}$。

**证明** 直和 $\Leftrightarrow$ 3：两种表示相减就得到零向量的一种表示。3 $\Leftrightarrow$ 2：各 $V_i$ 的基合起来总是张成和空间，条件 3 恰好说明它们线性无关。2 $\Leftrightarrow$ 1：基的并的个数等于 $\sum \dim V_i$，它是和空间的基当且仅当这个数等于和空间的维数。3 $\Leftrightarrow$ 4：若 $0 \ne v \in V_i \cap \sum_{j\ne i} V_j$，写 $v = \sum_{j \ne i} v_j$，则 $0 = -v + \sum_{j\ne i} v_j$ 是零向量的非平凡表示；反之亦然。 $\square$

$k = 2$ 时条件 4 就是 $V_1 \cap V_2 = \{0\}$。但 $k \ge 3$ 时两两相交为零不够：$\mathbb{C}^2$ 中三条不同的直线两两交于零，和却不是直和。

**例 10.1.1** 在 $\mathbb{C}^3$ 中，$V_1$ 为 $xOy$ 平面、$V_2$ 为 $yOz$ 平面，则 $V_1 + V_2 = \mathbb{C}^3$，但 $\dim V_1 + \dim V_2 = 4 > 3$，不是直和；事实上 $(0, 1, 0)$ 同时属于两者。

**例 10.1.2** 设 $A = \begin{bmatrix} 1 & 3 & 2 \\ 1 & 7 & 2 \\ -2 & -14 & -4 \end{bmatrix}$。$\mathcal{N}(A^{\mathsf T})$ 的基为 $\boldsymbol{\alpha}_1 = (0, 2, 1)^{\mathsf T}$，**列空间** $\mathcal{R}(A)$ 的基为 $\boldsymbol{\alpha}_2 = (1, 1, -2)^{\mathsf T}$、$\boldsymbol{\alpha}_3 = (3, 7, -14)^{\mathsf T}$。三者线性无关，由条件 2 得 $\mathbb{C}^3 = \mathcal{N}(A^{\mathsf T}) \oplus \mathcal{R}(A)$。对实矩阵这总是成立的（$\mathcal{N}(A^{\mathsf T})$ 是 $\mathcal{R}(A)$ 的**正交补**，[第 4 章](/2.1.4)）；对复矩阵，与 $\mathcal{R}(A)$ 互补的是 $\mathcal{N}(A^{\mathsf H})$，$\mathcal{N}(A^{\mathsf T}) \cap \mathcal{R}(A)$ 可能非零（例如 $A = \begin{bmatrix} 1 & \mathrm{i} \\ \mathrm{i} & -1 \end{bmatrix}$ 时两者都等于 $\operatorname{span}\{(1, \mathrm{i})^{\mathsf T}\}$），原因见 [第 12 章](/2.1.12)的复内积。

## 10.2. 不变子空间

先看 $A$ 相似于分块对角阵意味着什么。若 $A \in \mathbb{C}^{3\times 3}$ 且 $P^{-1}AP = \begin{bmatrix} b_{11} & 0 & 0 \\ 0 & b_{22} & b_{23} \\ 0 & b_{32} & b_{33} \end{bmatrix}$，$P = (\boldsymbol{p}_1, \boldsymbol{p}_2, \boldsymbol{p}_3)$，比较 $AP = PB$ 的各列：

$$
A\boldsymbol{p}_1 = b_{11}\boldsymbol{p}_1, \qquad A\boldsymbol{p}_2 = b_{22}\boldsymbol{p}_2 + b_{32}\boldsymbol{p}_3, \qquad A\boldsymbol{p}_3 = b_{23}\boldsymbol{p}_2 + b_{33}\boldsymbol{p}_3.
$$

所以 $V_1 = \operatorname{span}\{\boldsymbol{p}_1\}$ 与 $V_2 = \operatorname{span}\{\boldsymbol{p}_2, \boldsymbol{p}_3\}$ 都被 $A$ 映到自身，且 $\mathbb{C}^3 = V_1 \oplus V_2$。化简矩阵就是寻找这样的子空间。

**定义 10.2.1（不变子空间）** 设 $T\colon V \to V$ 是线性变换，$W \subseteq V$ 是子空间。若对任意 $w \in W$ 都有 $T(w) \in W$，则称 $W$ 是 $V$ 的 $T$-不变子空间。此时 $T$ 在 $W$ 上的限制 $T|_W\colon W \to W$ 是 $W$ 上的线性变换。

**不变子空间**的概念在表示论中已经出现（[1.3.6](/1.3.6)），那里要求子空间对一族变换同时不变；这里只考虑一个变换。

**例 10.2.1** $T\colon \mathbb{C}^2 \to \mathbb{C}^2$，$(x, y)^{\mathsf T} \mapsto (y, x)^{\mathsf T}$。$x$ 轴不是 $T$-不变的：$(1, 0)^{\mathsf T} \mapsto (0, 1)^{\mathsf T}$。而对任意 $A \in \mathbb{C}^{n\times n}$ 和 $T(\boldsymbol{x}) = A\boldsymbol{x}$，$\mathcal{R}(A)$ 与 $\mathcal{N}(A)$ 都是 $T$-不变的：$\boldsymbol{y} = A\boldsymbol{x} \Rightarrow A\boldsymbol{y} = A(A\boldsymbol{x}) \in \mathcal{R}(A)$；$A\boldsymbol{x} = \boldsymbol{0} \Rightarrow A(A\boldsymbol{x}) = \boldsymbol{0}$。

**性质 10.2.1** 设 $T\colon V \to V$ 是线性变换。

1. $\{0\}$、$V$、**核** $\mathcal{N}(T)$、**象** $\mathcal{R}(T)$ 都是 $T$-不变子空间；更一般地，对任意 $a \in \mathbb{C}$ 与正整数 $k$，$\mathcal{N}\big((T - a\,\mathrm{id})^k\big)$ 与 $\mathcal{R}\big((T - a\,\mathrm{id})^k\big)$ 都是 $T$-不变的（$T$ 与 $T - a\,\mathrm{id}$ 可交换）。
2. 特征值 $\lambda_0$ 的**特征子空间** $V_{\lambda_0} = \mathcal{N}(T - \lambda_0 \mathrm{id})$ 是 $T$-不变的。
3. 一维不变子空间恰好是一个**特征向量**张成的子空间：若 $W = \operatorname{span}\{w_0\}$ 不变，则 $T(w_0) = \lambda_0 w_0$。
4. 复空间 $V$ 的每个非零 $T$-不变子空间 $W$ 都含有 $T$ 的特征向量。

**证明** 只证 4。取 $W$ 的基 $\alpha_1, \dots, \alpha_r$，由不变性 $(T\alpha_1, \dots, T\alpha_r) = (\alpha_1, \dots, \alpha_r)B$，$B$ 是 $T|_W$ 的矩阵。由**代数基本定理**，$B$ 有特征值 $\lambda_0$ 与特征向量 $\boldsymbol{x} = (x_1, \dots, x_r)^{\mathsf T} \ne \boldsymbol{0}$。令 $v = x_1\alpha_1 + \cdots + x_r\alpha_r \in W$，则 $v \ne 0$ 且

$$
T(v) = (T\alpha_1, \dots, T\alpha_r)\boldsymbol{x} = (\alpha_1, \dots, \alpha_r)B\boldsymbol{x} = \lambda_0 (\alpha_1, \dots, \alpha_r)\boldsymbol{x} = \lambda_0 v. \qquad \square
$$

性质 4 依赖于复数域：实空间上的旋转 $\begin{bmatrix} 0 & -1 \\ 1 & 0 \end{bmatrix}$ 没有一维不变子空间。

**定理 10.2.1** 设 $V$ 是 $n$ 维复空间，$T\colon V \to V$ 是线性变换，$V_1$ 是 $T$-不变子空间。

1. 存在子空间 $V_2$ 使 $V = V_1 \oplus V_2$（把 $V_1$ 的基扩充为 $V$ 的基即可）。
2. 设 $v_1, \dots, v_r$ 是 $V_1$ 的基，$w_1, \dots, w_{n-r}$ 是 $V_2$ 的基，则 $T$ 在基 $v_1, \dots, v_r, w_1, \dots, w_{n-r}$ 下的矩阵形如 $\begin{bmatrix} B_{11} & B_{12} \\ O & B_{22} \end{bmatrix}$，$B_{11}$ 是 $T|_{V_1}$ 的 $r$ 阶矩阵。
3. 若 $V_2$ 也是 $T$-不变的，则 $B_{12} = O$，矩阵是**分块对角矩阵**。

于是：$A$ 相似于分块上三角阵 $\Leftrightarrow$ 有非平凡的不变子空间；$A$ 相似于分块对角阵 $\Leftrightarrow$ 空间能分解成两个不变子空间的直和。

**例 10.2.2** 设 $A = \begin{bmatrix} 4 & -5 & 2 \\ 5 & -7 & 3 \\ 6 & -9 & 4 \end{bmatrix}$，$T(\boldsymbol{x}) = A\boldsymbol{x}$。$\mathcal{N}(A)$ 是 $T$-不变的，基为 $(1, 2, 3)^{\mathsf T}$。把它扩充为 $\mathbb{C}^3$ 的基 $(1, 2, 3)^{\mathsf T}, \boldsymbol{e}_2, \boldsymbol{e}_3$，计算各基向量的像在这组基下的坐标：

$$
A\begin{bmatrix}1\\2\\3\end{bmatrix} = \boldsymbol{0}, \quad A\boldsymbol{e}_2 = \begin{bmatrix}-5\\-7\\-9\end{bmatrix} = -5\begin{bmatrix}1\\2\\3\end{bmatrix} + 3\boldsymbol{e}_2 + 6\boldsymbol{e}_3, \quad A\boldsymbol{e}_3 = \begin{bmatrix}2\\3\\4\end{bmatrix} = 2\begin{bmatrix}1\\2\\3\end{bmatrix} - \boldsymbol{e}_2 - 2\boldsymbol{e}_3,
$$

所以 $P = \begin{bmatrix} 1 & 0 & 0 \\ 2 & 1 & 0 \\ 3 & 0 & 1 \end{bmatrix}$ 使 $P^{-1}AP = \begin{bmatrix} 0 & -5 & 2 \\ 0 & 3 & -1 \\ 0 & 6 & -2 \end{bmatrix}$，左上角的 $1 \times 1$ 块对应 $\mathcal{N}(A)$。

## 10.3. Schur 定理

反复使用定理 10.2.1，每次取出一个一维不变子空间（特征向量），就把矩阵化成上三角形。

**定理 10.3.1（Schur 定理）** 设 $A \in \mathbb{C}^{n\times n}$，$\det(\lambda I_n - A) = (\lambda - \mu_1)^{n_1} \cdots (\lambda - \mu_s)^{n_s}$，$\mu_1, \dots, \mu_s$ 互不相同。则存在可逆阵 $P$ 使 $P^{-1}AP = U$ 是**上三角矩阵**，且 $U$ 的对角元依次为 $n_1$ 个 $\mu_1$、$n_2$ 个 $\mu_2$、……、$n_s$ 个 $\mu_s$（顺序可任意指定）。$P$ 与 $U$ 都不唯一。

**证明** 对 $n$ 归纳，$n = 1$ 显然。取 $A$ 关于 $\mu_1$ 的特征向量 $\boldsymbol{p}_1$，扩充为 $\mathbb{C}^n$ 的基 $\boldsymbol{p}_1, \dots, \boldsymbol{p}_n$，令 $P_1 = (\boldsymbol{p}_1, \dots, \boldsymbol{p}_n)$，则 $P_1^{-1}AP_1 = \begin{bmatrix} \mu_1 & \boldsymbol{\alpha}^{\mathsf T} \\ \boldsymbol{0} & A_1 \end{bmatrix}$，$A_1$ 的特征多项式为 $\det(\lambda I - A)/(\lambda - \mu_1)$。由归纳假设有可逆阵 $Q$ 使 $Q^{-1}A_1Q$ 是上三角阵，令 $P = P_1 \begin{bmatrix} 1 & \boldsymbol{0}^{\mathsf T} \\ \boldsymbol{0} & Q \end{bmatrix}$，则

$$
P^{-1}AP = \begin{bmatrix} 1 & \boldsymbol{0}^{\mathsf T} \\ \boldsymbol{0} & Q^{-1} \end{bmatrix}\begin{bmatrix} \mu_1 & \boldsymbol{\alpha}^{\mathsf T} \\ \boldsymbol{0} & A_1 \end{bmatrix}\begin{bmatrix} 1 & \boldsymbol{0}^{\mathsf T} \\ \boldsymbol{0} & Q \end{bmatrix} = \begin{bmatrix} \mu_1 & \boldsymbol{\alpha}^{\mathsf T}Q \\ \boldsymbol{0} & Q^{-1}A_1Q \end{bmatrix}
$$

是上三角阵。每一步先取哪个特征值可以自由选择，故对角元的顺序可以任意指定。 $\square$

[第 6 章](/2.1.6)用同样的结论证明了 **Cayley–Hamilton 定理**（定理 6.9.2），10.6 节将给出另一个证明。这里的 Schur 定理与表示论中的 **Schur 引理**（[1.3.6](/1.3.6)）无关。证明本身就是一个逐步降维的算法：

**算法 10.3.1（Schur 三角化）** 输入 $A \in \mathbb{C}^{n\times n}$。

1. 求 $A$ 的一个特征值 $\mu$ 及特征向量 $\boldsymbol{p}_1$（多项式求根、解齐次方程组）。
2. 把 $\boldsymbol{p}_1$ 扩充为 $\mathbb{C}^n$ 的基，构成 $P_1$，计算 $P_1^{-1}AP_1 = \begin{bmatrix} \mu & \ast \\ \boldsymbol{0} & A_1 \end{bmatrix}$。
3. 对 $n - 1$ 阶矩阵 $A_1$ 重复以上步骤得到 $Q$，令 $P = P_1\operatorname{diag}(1, Q)$；$A_1$ 是 $1$ 阶时停止。

**例 10.3.1** 对例 10.2.2 的 $A$，$\det(\lambda I_3 - A) = \lambda^2(\lambda - 1)$。

1. 取 $\mu = 1$ 的特征向量 $\boldsymbol{p}_1 = (1, 1, 1)^{\mathsf T}$，扩充为基 $\boldsymbol{p}_1, \boldsymbol{e}_2, \boldsymbol{e}_3$。由 $A\boldsymbol{e}_2 = (-5, -7, -9)^{\mathsf T} = -5\boldsymbol{p}_1 - 2\boldsymbol{e}_2 - 4\boldsymbol{e}_3$，$A\boldsymbol{e}_3 = (2, 3, 4)^{\mathsf T} = 2\boldsymbol{p}_1 + \boldsymbol{e}_2 + 2\boldsymbol{e}_3$，得 $P_1 = \begin{bmatrix} 1 & 0 & 0 \\ 1 & 1 & 0 \\ 1 & 0 & 1 \end{bmatrix}$，$P_1^{-1}AP_1 = \begin{bmatrix} 1 & -5 & 2 \\ 0 & -2 & 1 \\ 0 & -4 & 2 \end{bmatrix}$。
2. $A_1 = \begin{bmatrix} -2 & 1 \\ -4 & 2 \end{bmatrix}$ 有特征向量 $\boldsymbol{q}_1 = (1, 2)^{\mathsf T}$（$A_1\boldsymbol{q}_1 = \boldsymbol{0}$），扩充为 $\boldsymbol{q}_1, \boldsymbol{e}_2$，$Q = \begin{bmatrix} 1 & 0 \\ 2 & 1 \end{bmatrix}$，$Q^{-1}A_1Q = \begin{bmatrix} 0 & 1 \\ 0 & 0 \end{bmatrix}$。
3. $P = P_1\operatorname{diag}(1, Q) = \begin{bmatrix} 1 & 0 & 0 \\ 1 & 1 & 0 \\ 1 & 2 & 1 \end{bmatrix}$，$P^{-1}AP = \begin{bmatrix} 1 & -1 & 2 \\ 0 & 0 & 1 \\ 0 & 0 & 0 \end{bmatrix}$。

[第 12 章](/2.1.12)将把 Schur 定理加强为：$P$ 可以取成酉矩阵。

## 10.4. 广义特征向量与根子空间

亏损矩阵的特征向量不够张成全空间，需要把特征向量推广。下面设 $A \in \mathbb{C}^{n\times n}$，$\det(\lambda I_n - A) = (\lambda - \mu_1)^{n_1}\cdots(\lambda - \mu_s)^{n_s}$，$\mu_i$ 互不相同。

**定义 10.4.1** 设 $\lambda_0 \in \mathbb{C}$。若非零向量 $\boldsymbol{v} \in \mathbb{C}^n$ 满足 $(A - \lambda_0 I_n)^k \boldsymbol{v} = \boldsymbol{0}$（某个 $k \ge 1$），则称 $\boldsymbol{v}$ 为 $A$ 关于 $\lambda_0$ 的**广义特征向量**；$k = 1$ 时就是特征向量。零向量与全体关于 $\lambda_0$ 的广义特征向量构成的集合称为 $\lambda_0$ 的**根子空间**（也称广义特征子空间）：

$$
G_{\lambda_0} = \{\boldsymbol{v} \in \mathbb{C}^n \mid \text{存在 } k \ge 1 \text{ 使 } (A - \lambda_0 I_n)^k \boldsymbol{v} = \boldsymbol{0}\}.
$$

记 $N_{\lambda_0, k} = \mathcal{N}\left((A - \lambda_0 I_n)^k\right)$，则

$$
V_{\lambda_0} = N_{\lambda_0, 1} \subseteq N_{\lambda_0, 2} \subseteq \cdots \subseteq \mathbb{C}^n, \qquad G_{\lambda_0} = \bigcup_{k \ge 1} N_{\lambda_0, k}, \qquad \dim N_{\lambda_0, k} = n - \operatorname{rank}\left((A - \lambda_0 I_n)^k\right).
$$

**性质 10.4.1**

1. $G_{\lambda_0}$ 是子空间（若 $(A - \lambda_0 I)^{k_1}\boldsymbol{v}_1 = \boldsymbol{0} = (A - \lambda_0 I)^{k_2}\boldsymbol{v}_2$，则 $(A - \lambda_0 I)^{k_1 + k_2}(\boldsymbol{v}_1 + \boldsymbol{v}_2) = \boldsymbol{0}$），且是 $A$-不变子空间（$A$ 与 $(A - \lambda_0 I)^k$ 可交换）。
2. 若某个 $l$ 使 $N_{\lambda_0, l} = N_{\lambda_0, l+1}$，则 $N_{\lambda_0, l} = N_{\lambda_0, l+1} = N_{\lambda_0, l+2} = \cdots = G_{\lambda_0}$。
3. 因此链在某一步之后稳定；最小的稳定位置 $l$ 由秩序列决定：$N_{\lambda_0, k} = N_{\lambda_0, k+1} \Leftrightarrow \operatorname{rank}\left((A - \lambda_0 I)^k\right) = \operatorname{rank}\left((A - \lambda_0 I)^{k+1}\right)$。

**证明** 2：设 $\boldsymbol{v} \in N_{\lambda_0, l+2}$，则 $(A - \lambda_0 I)^{l+1}\left((A - \lambda_0 I)\boldsymbol{v}\right) = \boldsymbol{0}$，即 $(A - \lambda_0 I)\boldsymbol{v} \in N_{\lambda_0, l+1} = N_{\lambda_0, l}$，于是 $(A - \lambda_0 I)^{l+1}\boldsymbol{v} = \boldsymbol{0}$，$\boldsymbol{v} \in N_{\lambda_0, l+1}$。归纳即得。由于各 $N_{\lambda_0,k}$ 的维数不超过 $n$，严格增长不能无限进行，得 3。 $\square$

**例 10.4.1** $A = \begin{bmatrix} 1 & 1 & 0 & 0 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & 2 \end{bmatrix}$，$\det(\lambda I_4 - A) = (\lambda - 1)^3(\lambda - 2)$。$\operatorname{rank}(A - I) = 2 > \operatorname{rank}\left((A - I)^2\right) = 1 = \operatorname{rank}\left((A - I)^3\right)$，所以

$$
N_{1,1} \subsetneq N_{1,2} = N_{1,3} = \cdots = G_1, \qquad \dim N_{1,1} = 2, \quad \dim G_1 = 3,
$$

最小的稳定位置是 $l = 2$。注意 $\dim G_1$ 恰好等于 $1$ 的代数重数 $3$，这不是巧合。

## 10.5. 根子空间分解定理

先准备几个关于矩阵多项式的简单事实。对 $g(x) = a_kx^k + \cdots + a_0 \in \mathbb{C}[x]$，记 $g(A) = a_kA^k + \cdots + a_1A + a_0I_n$。

**引理 10.5.1** 设 $f, g \in \mathbb{C}[x]$，$A \in \mathbb{C}^{n\times n}$，$P$ 可逆。

1. $f(A)g(A) = g(A)f(A)$；
2. $P^{-1}f(A)P = f(P^{-1}AP)$（因为 $P^{-1}A^kP = (P^{-1}AP)^k$）；
3. 若 $A\boldsymbol{v} = \lambda_0 \boldsymbol{v}$，则 $g(A)\boldsymbol{v} = g(\lambda_0)\boldsymbol{v}$。

**引理 10.5.2** 属于不同特征值的广义特征向量线性无关：若 $\boldsymbol{v}_i \in G_{\mu_i}$（$i = 1, \dots, s$）且 $\boldsymbol{v}_1 + \cdots + \boldsymbol{v}_s = \boldsymbol{0}$，则每个 $\boldsymbol{v}_i = \boldsymbol{0}$。

**证明** 设 $c_1\boldsymbol{v}_1 + \cdots + c_s\boldsymbol{v}_s = \boldsymbol{0}$，$\boldsymbol{v}_i \in G_{\mu_i}$ 非零，固定 $i$ 证 $c_i = 0$。取足够大的 $K$ 使 $(A - \mu_j I)^K \boldsymbol{v}_j = \boldsymbol{0}$ 对所有 $j$ 成立，令 $g(x) = \prod_{j \ne i}(x - \mu_j)^K$，则 $g(A)\boldsymbol{v}_j = \boldsymbol{0}$（$j \ne i$），从而 $c_i g(A)\boldsymbol{v}_i = \boldsymbol{0}$。设 $k$ 是使 $(A - \mu_i I)^k \boldsymbol{v}_i = \boldsymbol{0}$ 的最小正整数，$\boldsymbol{w} = (A - \mu_i I)^{k-1}\boldsymbol{v}_i \ne \boldsymbol{0}$ 是特征向量。用 $(A - \mu_i I)^{k-1}$ 作用并交换次序，得 $c_i g(A)\boldsymbol{w} = c_i g(\mu_i)\boldsymbol{w} = \boldsymbol{0}$。而 $g(\mu_i) \ne 0$，故 $c_i = 0$。 $\square$

**定理 10.5.1（根子空间分解定理）** 设 $A \in \mathbb{C}^{n\times n}$，$\det(\lambda I_n - A) = (\lambda - \mu_1)^{n_1}\cdots(\lambda - \mu_s)^{n_s}$，$\mu_i$ 互不相同。则

1. $\dim G_{\mu_i} = n_i$，即根子空间的维数等于**代数重数**；
2. $G_{\mu_i} = \mathcal{N}\left((A - \mu_i I_n)^{n_i}\right)$；
3. $\mathbb{C}^n = G_{\mu_1} \oplus \cdots \oplus G_{\mu_s}$。

**证明** 1、2：以 $\mu_1$ 为例。由 Schur 定理，存在 $P$ 使 $P^{-1}AP = \begin{bmatrix} B_{11} & B_{12} \\ O & B_{22} \end{bmatrix}$，其中 $B_{11}$ 是对角元全为 $\mu_1$ 的 $n_1$ 阶上三角阵，$B_{22}$ 是对角元都不等于 $\mu_1$ 的上三角阵。于是

$$
P^{-1}(A - \mu_1 I)^k P = \begin{bmatrix} C_{11}^k & \ast \\ O & C_{22}^k \end{bmatrix}, \qquad C_{11} = B_{11} - \mu_1 I, \quad C_{22} = B_{22} - \mu_1 I,
$$

$C_{11}$ 是严格上三角阵，$C_{11}^{n_1} = O$；$C_{22}$ 可逆。当 $k \ge n_1$ 时右边形如 $\begin{bmatrix} O & \ast \\ O & C_{22}^k \end{bmatrix}$，秩为 $n - n_1$。所以 $\dim N_{\mu_1, k} = n_1$ 对一切 $k \ge n_1$ 成立，链在 $k = n_1$ 处已经稳定，$G_{\mu_1} = N_{\mu_1, n_1}$，维数为 $n_1$。

3：由引理 10.5.2，零向量在 $G_{\mu_1} + \cdots + G_{\mu_s}$ 中的表示唯一，所以和是直和（定理 10.1.1 条件 3），维数为 $n_1 + \cdots + n_s = n$，它就是 $\mathbb{C}^n$。 $\square$

把各根子空间的基拼起来作为新基，得到矩阵形式。

**定理 10.5.2** 在定理 10.5.1 的条件下，设 $\boldsymbol{v}_{i1}, \dots, \boldsymbol{v}_{in_i}$ 是 $G_{\mu_i}$ 的基，$P = (\boldsymbol{v}_{11}, \dots, \boldsymbol{v}_{1n_1}, \dots, \boldsymbol{v}_{s1}, \dots, \boldsymbol{v}_{sn_s})$，则

$$
P^{-1}AP = \operatorname{diag}(A_1, \dots, A_s), \qquad A(\boldsymbol{v}_{i1}, \dots, \boldsymbol{v}_{in_i}) = (\boldsymbol{v}_{i1}, \dots, \boldsymbol{v}_{in_i})A_i,
$$

$A_i$ 是 $n_i$ 阶矩阵，且只有一个特征值 $\mu_i$：$\det(\lambda I_{n_i} - A_i) = (\lambda - \mu_i)^{n_i}$。

**证明** 分块对角来自 $G_{\mu_i}$ 的不变性（定理 10.2.1）。若 $A_i$ 有特征值 $\lambda_0$，对应特征向量 $\boldsymbol{x}$，则 $\boldsymbol{w} = (\boldsymbol{v}_{i1}, \dots, \boldsymbol{v}_{in_i})\boldsymbol{x} \in G_{\mu_i}$ 非零且 $A\boldsymbol{w} = \lambda_0 \boldsymbol{w}$。由 $(A - \mu_i I)^{n_i}\boldsymbol{w} = \boldsymbol{0}$ 与引理 10.5.1 的第 3 条，$(\lambda_0 - \mu_i)^{n_i}\boldsymbol{w} = \boldsymbol{0}$，故 $\lambda_0 = \mu_i$。 $\square$

**推论 10.5.1** $A$ 可对角化 $\Leftrightarrow$ $\mathbb{C}^n = V_{\mu_1} \oplus \cdots \oplus V_{\mu_s}$ $\Leftrightarrow$ 每个特征值的代数重数等于**几何重数** $\Leftrightarrow$ 对每个 $i$，$G_{\mu_i} = V_{\mu_i}$。

**例 10.5.1** $A = \begin{bmatrix} 0 & 1 & 0 \\ 0 & 0 & 1 \\ 2 & -5 & 4 \end{bmatrix}$（**友矩阵**），$\det(\lambda I_3 - A) = (\lambda - 1)^2(\lambda - 2)$。

$$
G_1 = \mathcal{N}\left((A - I)^2\right) = \mathcal{N}\begin{bmatrix} 1 & -2 & 1 \\ 2 & -4 & 2 \\ 4 & -8 & 4 \end{bmatrix} = \operatorname{span}\left\{\begin{bmatrix}2\\1\\0\end{bmatrix}, \begin{bmatrix}1\\0\\-1\end{bmatrix}\right\}, \qquad G_2 = \mathcal{N}(A - 2I) = \operatorname{span}\left\{\begin{bmatrix}1\\2\\4\end{bmatrix}\right\}.
$$

令 $P = \begin{bmatrix} 2 & 1 & 1 \\ 1 & 0 & 2 \\ 0 & -1 & 4 \end{bmatrix}$，由 $A(2,1,0)^{\mathsf T} = (1, 0, -1)^{\mathsf T}$，$A(1, 0, -1)^{\mathsf T} = (0, -1, -2)^{\mathsf T} = -(2,1,0)^{\mathsf T} + 2(1,0,-1)^{\mathsf T}$，得

$$
P^{-1}AP = \begin{bmatrix} A_1 & \\ & A_2 \end{bmatrix}, \qquad A_1 = \begin{bmatrix} 0 & -1 \\ 1 & 2 \end{bmatrix}, \quad A_2 = (2).
$$

$A_1$ 的特征多项式是 $(\lambda - 1)^2$，与定理 10.5.2 一致。

## 10.6. Cayley–Hamilton 定理与极小多项式

**定义 10.6.1** 设 $g \in \mathbb{C}[x]$。若 $g(A) = O$，则称 $g$ 是 $A$ 的**化零多项式**。

**定理 10.6.1（Cayley–Hamilton 定理）** 设 $f(\lambda) = \det(\lambda I_n - A) = \lambda^n + a_1\lambda^{n-1} + \cdots + a_n$ 是 $A$ 的**特征多项式**，则 $f(A) = A^n + a_1A^{n-1} + \cdots + a_nI_n = O$。

**证明** 由定理 10.5.2，$P^{-1}AP = B = \operatorname{diag}(A_1, \dots, A_s)$，$A_i$ 只有特征值 $\mu_i$。由 Schur 定理，$A_i - \mu_i I$ 相似于严格上三角阵，所以 $(A_i - \mu_i I)^{n_i} = O$。于是

$$
P^{-1}f(A)P = f(B) = (B - \mu_1 I)^{n_1}\cdots(B - \mu_s I)^{n_s}
$$

是分块对角阵，第 $i$ 个对角块是 $n_i$ 阶矩阵 $\prod_j (A_i - \mu_j I)^{n_j}$。这些因子可交换，其中含有 $(A_i - \mu_i I)^{n_i} = O$，所以每个对角块都是零，$f(A) = O$。 $\square$

特征多项式是 $n$ 次的化零多项式。次数最低的化零多项式包含更多信息。

**定义 10.6.2** $A$ 的次数最低、首项系数为 $1$ 的化零多项式称为 $A$ 的**极小多项式**，记作 $m_A(x)$。

**性质 10.6.1**

1. 若 $g(A) = O$，则 $m_A \mid g$。特别地 $m_A$ 整除特征多项式。
2. $m_A$ 唯一。
3. 相似矩阵有相同的极小多项式。
4. 若 $A = \operatorname{diag}(A_1, \dots, A_s)$，则 $m_A$ 是 $m_{A_1}, \dots, m_{A_s}$ 的首一最小公倍式。
5. 设 $\det(\lambda I_n - A) = \prod_{i=1}^s (\lambda - \mu_i)^{n_i}$，则 $m_A(x) = \prod_{i=1}^s (x - \mu_i)^{m_i}$，其中 $1 \le m_i \le n_i$，$m_i$ 是使 $N_{\mu_i, l} = G_{\mu_i}$ 的最小 $l$，即秩序列 $\operatorname{rank}\left((A - \mu_i I)^k\right)$ 第一次停止下降的位置。
6. $A$ 可对角化 $\Leftrightarrow$ $m_A$ 没有**重根**。

**证明** 1：作**带余除法** $g = qm_A + r$，$\deg r < \deg m_A$。代入 $A$ 得 $r(A) = O$，由 $m_A$ 次数最低知 $r = 0$。2：两个首一极小多项式互相整除，故相等。3：若 $B = P^{-1}AP$，则 $m_A(B) = P^{-1}m_A(A)P = O$，故 $m_B \mid m_A$；同理 $m_A \mid m_B$。4：$g(A) = \operatorname{diag}(g(A_1), \dots, g(A_s))$，所以 $g(A) = O \Leftrightarrow$ 每个 $m_{A_i} \mid g$。

5：由 3、4 与定理 10.5.2，$m_A = m_B$ 是各 $m_{A_i}$ 的最小公倍式。由 $(A_i - \mu_i I)^{n_i} = O$ 和 1，$m_{A_i} = (x - \mu_i)^{m_i}$，$m_i \le n_i$ 是使 $(A_i - \mu_i I)^k = O$ 的最小 $k$；各 $m_{A_i}$ **互素**，最小公倍式就是乘积。最后，$A_j - \mu_i I$（$j \ne i$）可逆，所以

$$
\operatorname{rank}\left((A - \mu_i I)^k\right) = \operatorname{rank}\left((A_i - \mu_i I)^k\right) + \sum_{j \ne i} n_j,
$$

秩序列停止下降的位置就是 $(A_i - \mu_i I)^k$ 第一次为零的位置（幂零阵的幂的秩严格下降直到零，由性质 10.4.1 的第 2 条），即 $m_i$。

6：由推论 10.5.1，可对角化 $\Leftrightarrow$ $G_{\mu_i} = N_{\mu_i, 1}$ $\Leftrightarrow$ 所有 $m_i = 1$。 $\square$

**例 10.6.1** $A = \operatorname{diag}(1, 1, 2)$ 的特征多项式是 $(x - 1)^2(x - 2)$，极小多项式是 $(x - 1)(x - 2)$；$\begin{bmatrix} 1 & 1 \\ 0 & 1 \end{bmatrix}$ 的极小多项式是 $(x - 1)^2$，有重根，所以不可对角化。

**例 10.6.2** 若 $A^2 = I_n$，则 $x^2 - 1 = (x - 1)(x + 1)$ 是化零多项式，$m_A$ 整除它而没有重根，故 $A$ 可对角化。同理，满足 $A^2 = A$（投影）或 $A^k = I$ 的复矩阵都可对角化。

判断能否对角化只需要检验一个多项式有没有重根，而后者又可以用 $\gcd(m_A, m_A')$ 判断（[第 9 章](/2.1.9)的**最大公因式**），不需要求出任何特征向量。

## 10.7. 幂零变换与循环子空间

由定理 10.5.2，只需把每个只有一个特征值的块 $A_i$ 化简。$A_i - \mu_iI$ 是幂零的，所以问题归结为幂零变换的最简形。

**定义 10.7.1** 设 $V$ 是 $n$ 维复空间，$T\colon V \to V$ 是线性变换。若存在 $m \ge 1$ 使 $T^m = O$ 而 $T^{m-1} \ne O$，则称 $T$ 是**幂零变换**，$m$ 称为 $T$ 的**幂零指数**。若 $m = \dim V$，则称 $T$ 是**循环变换**。

本课程中的"循环变换"专指幂零指数等于维数的幂零变换。一般文献中，cyclic operator 指存在向量 $v$ 使 $v, Tv, T^2v, \dots$ 张成 $V$ 的任意线性变换；对幂零变换两种说法一致。

**性质 10.7.1** 设 $T$ 在某组基下的矩阵为 $A$。

1. $T$ 幂零 $\Leftrightarrow$ $A$ 是**幂零矩阵**，且幂零指数相同，$m_A(x) = x^m$；
2. $T$ 幂零 $\Leftrightarrow$ $T$ 的特征值只有 $0$；
3. 若 $T$ 幂零，则 $T^n = O$，即幂零指数不超过 $n$。

**证明** 1：$T^k$ 的矩阵是 $A^k$。2：由 Schur 定理 $A$ 相似于上三角阵 $U$，$U^k$ 的对角元是 $\lambda_i^k$；若 $A^k = O$ 则所有 $\lambda_i = 0$；反之对角元全为零的上三角阵满足 $U^n = O$。3：由 2，特征多项式是 $\lambda^n$，再用 Cayley–Hamilton 定理。 $\square$

**例 10.7.1** $T\colon \mathbb{C}^4 \to \mathbb{C}^4$，$(z_1, z_2, z_3, z_4)^{\mathsf T} \mapsto (0, z_1, z_2, z_3)^{\mathsf T}$。$T^3 \ne O$，$T^4 = O$，幂零指数 $4 = \dim \mathbb{C}^4$，是循环变换；$\boldsymbol{e}_1, T\boldsymbol{e}_1 = \boldsymbol{e}_2, T^2\boldsymbol{e}_1 = \boldsymbol{e}_3, T^3\boldsymbol{e}_1 = \boldsymbol{e}_4$ 构成一组基。而 $(z_1, \dots, z_5)^{\mathsf T} \mapsto (0, z_1, 0, z_3, 0)^{\mathsf T}$ 满足 $T^2 = O$，是幂零的但不是循环的。

**定义 10.7.2** 设 $T\colon V \to V$ 幂零，$v \ne 0$，$k$ 是使 $T^kv = 0$ 的最小正整数。称 $C_v = \operatorname{span}\{T^{k-1}v, T^{k-2}v, \dots, Tv, v\}$ 为由 $v$ 生成的**循环子空间**，$T^{k-1}v, \dots, Tv, v$ 称为 $C_v$ 的**循环基**。

**性质 10.7.2**

1. $T^{k-1}v, \dots, Tv, v$ 线性无关，$\dim C_v = k$；
2. $C_v$ 是 $T$-不变子空间，$T|_{C_v}$ 是循环变换，它在循环基下的矩阵为

$$
J_{0,k} = \begin{bmatrix} 0 & 1 & & \\ & 0 & \ddots & \\ & & \ddots & 1 \\ & & & 0 \end{bmatrix}_{k \times k};
$$

3. 称 $C_v$ 是极大的，若不存在 $w$ 使 $C_v \subsetneq C_w$。则 $C_v$ 极大 $\Leftrightarrow$ $v \notin \mathcal{R}(T)$。

**证明** 1：设 $c_1T^{k-1}v + \cdots + c_{k-1}Tv + c_kv = 0$，用 $T^{k-1}$ 作用得 $c_kT^{k-1}v = 0$，$c_k = 0$；再用 $T^{k-2}$ 作用得 $c_{k-1} = 0$，依此类推。2：$T(T^{k-1}v) = 0$，$T(T^jv) = T^{j+1}v$，矩阵的第 $j+1$ 列是第 $j$ 个基向量的坐标。3：若 $v = Tw$，则 $C_v \subsetneq C_w$。反之设 $v \notin \mathcal{R}(T)$ 且 $C_v \subseteq C_w$，$\dim C_w = l$。写 $v = a_0w + a_1Tw + \cdots + a_{l-1}T^{l-1}w$，因 $v \notin \mathcal{R}(T)$ 有 $a_0 \ne 0$，于是 $T^{l-1}v = a_0T^{l-1}w \ne 0$，$\dim C_v \ge l$，故 $C_v = C_w$。 $\square$

$J_{0,k}$ 就是特征值为 $0$ 的 **Jordan 块**。教材与课件称它为"循环矩阵"，但通行用法中"循环矩阵"指另一类矩阵（circulant matrix，每一行是上一行的循环移位），本站称 $J_{0,k}$ 为幂零 Jordan 块或移位矩阵。

**例 10.7.2** $A = J_{0,4}$ 时，$\boldsymbol{v} = \boldsymbol{e}_4 \notin \mathcal{R}(A)$，$C_{\boldsymbol{e}_4} = \mathbb{C}^4$ 极大；$\boldsymbol{w} = \boldsymbol{e}_3 = A\boldsymbol{e}_4 \in \mathcal{R}(A)$ 生成的 $C_{\boldsymbol{e}_3} = \operatorname{span}\{\boldsymbol{e}_1, \boldsymbol{e}_2, \boldsymbol{e}_3\} \subsetneq C_{\boldsymbol{e}_4}$。

## 10.8. 幂零变换的循环子空间分解

本节是 Jordan 定理的核心：幂零变换总能把空间分解成极大循环子空间的直和。证明要用到**秩–零化度定理** $\dim V = \dim \mathcal{R}(T) + \dim \mathcal{N}(T)$。由它，若 $T$ 幂零，则 $\mathcal{N}(T) \ne \{0\}$，从而 $\dim \mathcal{R}(T) < \dim V$，可以对维数归纳。

**定理 10.8.1** 设 $V$ 是 $n$ 维复空间，$T\colon V \to V$ 幂零。则存在 $v_1, \dots, v_t \in V$ 使

$$
V = C_{v_1} \oplus \cdots \oplus C_{v_t},
$$

且 $v_1, \dots, v_t \notin \mathcal{R}(T)$（各循环子空间都是极大的）。

**证明** 先注意一个事实：若 $V = C_{x_1} \oplus \cdots \oplus C_{x_t}$，则 $T$ 在每个 $C_{x_i}$ 上是移位，$\mathcal{N}(T)$ 由各循环基的第一个向量（$T$ 的特征向量）张成，所以 $\dim \mathcal{N}(T) = t$。

对 $n$ 归纳。$n = 1$ 时 $T = O$，$V = C_v$（$v \ne 0$）。设结论对维数小于 $n$ 的空间成立。若 $T = O$，取 $V$ 的任一组基 $w_1, \dots, w_n$，$V = C_{w_1} \oplus \cdots \oplus C_{w_n}$ 即可。设 $T \ne O$，令 $V_1 = \mathcal{R}(T)$，它是不变子空间，$0 < \dim V_1 < n$，$T|_{V_1}$ 幂零。由归纳假设，

$$
V_1 = C_{u_1} \oplus \cdots \oplus C_{u_s}, \qquad u_i \notin T(V_1) = \mathcal{R}(T^2).
$$

设 $\dim C_{u_i} = b_i$。因 $u_i \in \mathcal{R}(T)$，取 $v_i$ 使 $Tv_i = u_i$，则 $C_{v_i}$ 的循环基为 $T^{b_i}v_i, \dots, Tv_i, v_i$，$\dim C_{v_i} = b_i + 1$；且 $v_i \notin \mathcal{R}(T)$（否则 $u_i \in \mathcal{R}(T^2)$）。

向量 $T^{b_i - 1}u_i = T^{b_i}v_i$（$i = 1, \dots, s$）属于 $\mathcal{N}(T) \cap \mathcal{R}(T)$，由开头的事实，它们恰是 $\mathcal{N}(T|_{V_1}) = \mathcal{N}(T) \cap \mathcal{R}(T)$ 的基。把它们扩充为 $\mathcal{N}(T)$ 的基 $T^{b_1}v_1, \dots, T^{b_s}v_s, w_1, \dots, w_r$，则 $w_j \notin \mathcal{R}(T)$（否则 $w_j \in \mathcal{N}(T) \cap \mathcal{R}(T)$，与扩充矛盾）。下证

$$
\mathcal{B} = \{T^jv_i \mid 1 \le i \le s, 0 \le j \le b_i\} \cup \{w_1, \dots, w_r\}
$$

是 $V$ 的基，从而 $V = C_{v_1} \oplus \cdots \oplus C_{v_s} \oplus C_{w_1} \oplus \cdots \oplus C_{w_r}$（$\dim C_{w_j} = 1$）。

个数：$\sum_i (b_i + 1) + r = \dim V_1 + s + r = \dim \mathcal{R}(T) + \dim \mathcal{N}(T) = n$。线性无关：设 $\sum_{i,j} c_{ij}T^jv_i + \sum_k d_kw_k = 0$，用 $T$ 作用得 $\sum_i \sum_{j < b_i} c_{ij}T^ju_i = 0$，而 $\{T^ju_i\}$ 是 $V_1$ 的基，故 $c_{ij} = 0$（$j < b_i$）。剩下 $\sum_i c_{ib_i}T^{b_i}v_i + \sum_k d_kw_k = 0$，这是 $\mathcal{N}(T)$ 的基的组合，系数全为零。 $\square$

证明给出的是一个自下而上的构造：先分解 $\mathcal{R}(T)$，再把每个循环基"向上延长一格"，最后用 $\mathcal{N}(T)$ 中剩下的方向补齐。

**推论 10.8.1** 在定理 10.8.1 中，

1. 循环子空间的个数 $t = \dim \mathcal{N}(T)$，即特征值 $0$ 的几何重数；
2. 循环子空间的最大维数等于 $T$ 的幂零指数。

## 10.9. Jordan 标准形的存在性与结构

把定理 10.8.1 翻译成矩阵语言：每个循环基对应一个幂零 Jordan 块。

**定理 10.9.1** 设 $A \in \mathbb{C}^{n\times n}$ 幂零，则存在可逆阵 $P$ 使

$$
P^{-1}AP = J = \operatorname{diag}(J_{0,b_1}, \dots, J_{0,b_t}),
$$

其中 $t = \dim \mathcal{N}(A) = n - \operatorname{rank}(A)$。$J$ 称为幂零阵 $A$ 的 Jordan 标准形，$P$ 由各循环子空间的循环基依次排列而成。

**定义 10.9.1** 设 $\mu \in \mathbb{C}$。若 $\boldsymbol{v} \ne \boldsymbol{0}$ 满足 $(A - \mu I)^k\boldsymbol{v} = \boldsymbol{0}$ 而 $(A - \mu I)^{k-1}\boldsymbol{v} \ne \boldsymbol{0}$，则称向量组 $(A - \mu I)^{k-1}\boldsymbol{v}, (A - \mu I)^{k-2}\boldsymbol{v}, \dots, (A - \mu I)\boldsymbol{v}, \boldsymbol{v}$ 为 $A$ 关于 $\mu$ 的一条长度为 $k$ 的 **Jordan 链**；第一个向量是特征向量，其余是广义特征向量。由若干条 Jordan 链组成、使 $P^{-1}AP$ 为 Jordan 标准形的基称为 **Jordan 基**。

**定义 10.9.2（Jordan 块）** 称 $k$ 阶矩阵

$$
J_{\lambda,k} = \lambda I_k + J_{0,k} = \begin{bmatrix} \lambda & 1 & & \\ & \lambda & \ddots & \\ & & \ddots & 1 \\ & & & \lambda \end{bmatrix}
$$

为关于 $\lambda$ 的 $k$ 阶 Jordan 块（第 6 章记作 $J_k(\lambda)$）。它的特征多项式与极小多项式都是 $(x - \lambda)^k$。

比较 $AP = PJ$ 的各列可知：$J$ 中的一个 $k$ 阶 Jordan 块 $J_{\mu,k}$ 恰好对应 $P$ 中的一条长度为 $k$ 的 Jordan 链。例如 $J = \operatorname{diag}(J_{1,2}, J_{1,1}, J_{2,2})$，$P = (\boldsymbol{p}_1, \dots, \boldsymbol{p}_5)$ 时，$(A - I)\boldsymbol{p}_1 = \boldsymbol{0}$，$(A - I)\boldsymbol{p}_2 = \boldsymbol{p}_1$，$(A - I)\boldsymbol{p}_3 = \boldsymbol{0}$，$(A - 2I)\boldsymbol{p}_4 = \boldsymbol{0}$，$(A - 2I)\boldsymbol{p}_5 = \boldsymbol{p}_4$：三条链分别是 $\boldsymbol{p}_1, \boldsymbol{p}_2$；$\boldsymbol{p}_3$；$\boldsymbol{p}_4, \boldsymbol{p}_5$。

**定理 10.9.2（Jordan 标准形）** 设 $A \in \mathbb{C}^{n\times n}$，$\det(\lambda I_n - A) = (\lambda - \mu_1)^{n_1}\cdots(\lambda - \mu_s)^{n_s}$，$\mu_i$ 互不相同。则存在可逆阵 $P$ 使

$$
P^{-1}AP = J = \operatorname{diag}(J_{\mu_1}, \dots, J_{\mu_s}), \qquad J_{\mu_i} = \operatorname{diag}(J_{\mu_i, m_{i1}}, \dots, J_{\mu_i, m_{it_i}}),
$$

其中 $J_{\mu_i}$ 是 $n_i$ 阶矩阵，$m_{i1} \ge \cdots \ge m_{it_i} \ge 1$，关于 $\mu_i$ 的块数 $t_i = n - \operatorname{rank}(A - \mu_iI)$ 等于 $\mu_i$ 的几何重数。$J$ 在不计 Jordan 块的排列顺序时由 $A$ 唯一确定。

**证明** 存在性：由定理 10.5.2，$\mathbb{C}^n = G_{\mu_1} \oplus \cdots \oplus G_{\mu_s}$，$A - \mu_iI$ 在 $G_{\mu_i}$ 上是幂零变换。对它用定理 10.9.1，得到 $G_{\mu_i}$ 的一组基，在这组基下 $(A - \mu_iI)|_{G_{\mu_i}}$ 的矩阵是幂零 Jordan 块的直和，于是 $A|_{G_{\mu_i}}$ 的矩阵是 $J_{\mu_i}$。块数等于 $\dim \mathcal{N}\big((A - \mu_iI)|_{G_{\mu_i}}\big) = \dim V_{\mu_i}$。唯一性由下面的定理 10.9.3 得到：各阶块的个数由秩决定，而秩在相似下不变。 $\square$

**定理 10.9.3** 设 $A$ 如定理 10.9.2，$d \ge 1$。则 $A$ 关于 $\mu_i$ 的 Jordan 块中，

$$
\text{阶数} \ge d \text{ 的块数} = \operatorname{rank}\left((A - \mu_iI)^{d-1}\right) - \operatorname{rank}\left((A - \mu_iI)^d\right),
$$

$$
\text{阶数} = d \text{ 的块数} = \operatorname{rank}\left((A - \mu_iI)^{d-1}\right) - 2\operatorname{rank}\left((A - \mu_iI)^d\right) + \operatorname{rank}\left((A - \mu_iI)^{d+1}\right),
$$

其中 $(A - \mu_iI)^0 = I$。特别地，幂零阵 $A$ 的 Jordan 块数为 $n - \operatorname{rank}(A)$，最大块的阶数等于幂零指数，阶数为 $d$ 的块数为 $\operatorname{rank}(A^{d-1}) + \operatorname{rank}(A^{d+1}) - 2\operatorname{rank}(A^d)$。

**证明** $\operatorname{rank}\left((A - \mu_iI)^k\right) = \operatorname{rank}\left((J - \mu_iI)^k\right)$。$J - \mu_iI$ 中关于 $\mu_j$（$j \ne i$）的块可逆，贡献的秩恒为 $n_j$；关于 $\mu_i$ 的块变成幂零块，而 $\operatorname{rank}(J_{0,b}^k) = \max(b - k, 0)$。所以

$$
\operatorname{rank}\left((A - \mu_iI)^k\right) = \sum_{j \ne i} n_j + \sum_{l=1}^{t_i} \max(m_{il} - k, 0),
$$

$k = d - 1$ 与 $k = d$ 两式相减，每个阶数 $\ge d$ 的块恰好贡献 $1$，其余贡献 $0$，得第一式。第二式是第一式对 $d$ 与 $d + 1$ 之差。 $\square$

**推论 10.9.1**

1. 极小多项式 $m_A(x) = \prod (x - \mu_i)^{m_i}$ 中，$m_i$ 等于关于 $\mu_i$ 的最大 Jordan 块的阶数；
2. 两个 $n$ 阶复方阵相似 $\Leftrightarrow$ 它们有相同的特征值，且对每个特征值 $\mu$ 与每个 $k$，$\operatorname{rank}\left((A - \mu I)^k\right) = \operatorname{rank}\left((B - \mu I)^k\right)$。

于是判定相似、求 Jordan 形都化成了算秩，也就是消元。

**例 10.9.1** $A = (\boldsymbol{0}, \boldsymbol{e}_1, \boldsymbol{0}, 2\boldsymbol{e}_2, \boldsymbol{0}, \boldsymbol{e}_3) \in \mathbb{C}^{6\times 6}$（按列写出），则 $A^2 = (\boldsymbol{0}, \boldsymbol{0}, \boldsymbol{0}, 2\boldsymbol{e}_1, \boldsymbol{0}, \boldsymbol{0})$，$A^3 = O$，$\operatorname{rank}(A) = 3$，$\operatorname{rank}(A^2) = 1$，$\operatorname{rank}(A^3) = 0$。阶数 $\ge 1, \ge 2, \ge 3$ 的块数分别为 $6 - 3 = 3$、$3 - 1 = 2$、$1 - 0 = 1$，所以 $J = \operatorname{diag}(J_{0,3}, J_{0,2}, J_{0,1})$。

把每条 Jordan 链竖着画成一列、链底的特征向量放在最下面，就得到下图右侧的点图：第 $d$ 行的点数是阶数 $\ge d$ 的块数，也就是秩序列相邻两项之差。点图的各列长度给出 Jordan 形，各行长度给出秩序列，两者互相决定。

![例 10.9.1 的幂零阵：左为秩序列 r_k = rank(A^k)，每一步下降的量等于阶数不小于 k 的 Jordan 块数；右为对应的三条 Jordan 链（阶数 3、2、1），箭头表示作用 A，第 d 行的点数等于 r_{d-1} - r_d](./plots/rank-sequence-dot-diagram.py)

**例 10.9.2** $A = \begin{bmatrix} 1 & 2 & 2 & 0 & 0 \\ 2 & 1 & 2 & 0 & 0 \\ 2 & 2 & 1 & 0 & 0 \\ 0 & 0 & 0 & 5 & 0 \\ 0 & 0 & 0 & 2 & 5 \end{bmatrix}$，$\det(\lambda I_5 - A) = (\lambda + 1)^2(\lambda - 5)^3$。$\operatorname{rank}(A + I) = 3$，关于 $-1$ 有 $5 - 3 = 2$ 个块，而 $-1$ 的代数重数是 $2$，所以是两个 $1$ 阶块。$\operatorname{rank}(A - 5I) = 3$，关于 $5$ 也有 $2$ 个块，总阶数为 $3$，只能是 $2 + 1$。故 $J = \operatorname{diag}(-1, -1, J_{5,2}, 5)$。

**例 10.9.3** 设 $n \ge 2$，求 $J_{0,n}^2$ 的 Jordan 形。$J_{0,n}^2$ 的特征值全为 $0$，$\operatorname{rank}(J_{0,n}^2) = n - 2$，所以有两个块。$J_{0,n}^k$ 在 $k \ge n$ 时为零。$n = 2m$ 时 $(J_{0,n}^2)^m = O \ne (J_{0,n}^2)^{m-1}$，极小多项式为 $x^m$，最大块阶数为 $m$，Jordan 形为 $\operatorname{diag}(J_{0,m}, J_{0,m})$；$n = 2m + 1$ 时极小多项式为 $x^{m+1}$，Jordan 形为 $\operatorname{diag}(J_{0,m+1}, J_{0,m})$。直观上，$J_{0,n}^2$ 把 $\boldsymbol{e}_n \mapsto \boldsymbol{e}_{n-2} \mapsto \cdots$ 与 $\boldsymbol{e}_{n-1} \mapsto \boldsymbol{e}_{n-3} \mapsto \cdots$ 分成奇偶两条链。

## 10.10. Jordan 基的计算

Jordan 形只需要秩，而 Jordan 基 $P$ 需要逐条构造 Jordan 链。构造时要保证不同链合起来线性无关，这是计算中唯一需要小心的地方。

**算法 10.10.1（Jordan 标准形与 Jordan 基）** 输入 $A \in \mathbb{C}^{n\times n}$。

1. 特征值：求特征多项式的根 $\mu_1, \dots, \mu_s$ 及代数重数 $n_1, \dots, n_s$。
2. 块的结构：对每个 $\mu_i$，计算 $r_k = \operatorname{rank}\left((A - \mu_iI)^k\right)$，$k = 1, 2, \dots$，直到 $r_k = n - n_i$；阶数 $\ge k$ 的块数为 $r_{k-1} - r_k$（$r_0 = n$）。由此写出 $J$。
3. Jordan 链（自上而下）：记 $N_k = \mathcal{N}\left((A - \mu_iI)^k\right)$，$m_i$ 为最大块阶数。对 $k = m_i, m_i - 1, \dots, 1$，在 $N_k$ 中选取向量 $\boldsymbol{y}$，个数等于 $k$ 阶块的个数，使它们与 $N_{k-1}$ 的基、以及已选的更高层向量 $\boldsymbol{y}'$（层数 $j > k$）的像 $(A - \mu_iI)^{j-k}\boldsymbol{y}'$ 合起来线性无关。每个 $\boldsymbol{y}$ 生成一条链 $(A - \mu_iI)^{k-1}\boldsymbol{y}, \dots, (A - \mu_iI)\boldsymbol{y}, \boldsymbol{y}$。
4. 拼装：把所有链按 $J$ 中块的顺序排成 $P$（每条链先写特征向量），则 $P^{-1}AP = J$。

第 1 步是多项式求根，第 2 步是一系列消元，第 3 步是解齐次线性方程组并检验线性无关（仍是算秩）。第 3 步的无关性条件不能省：选错了顶端向量，不同链的特征向量会重合，$P$ 不可逆（见例 10.10.2）。对小矩阵也常用自下而上的做法：在 $\mathcal{N}(A - \mu_iI) \cap \mathcal{R}\left((A - \mu_iI)^{k-1}\right)$ 中取链底的特征向量，再依次解 $(A - \mu_iI)\boldsymbol{x} = $（上一个向量）向上延长。

**例 10.10.1** $A = \begin{bmatrix} 3 & 0 & 8 \\ 3 & -1 & 6 \\ -2 & 0 & -5 \end{bmatrix}$，$\det(\lambda I - A) = (\lambda + 1)^3$。$\operatorname{rank}(A + I) = 1$，$(A + I)^2 = O$，所以有 $3 - 1 = 2$ 个块、最大阶数 $2$：$J = \operatorname{diag}(J_{-1,2}, -1)$。自下而上：$A + I = \begin{bmatrix} 4 & 0 & 8 \\ 3 & 0 & 6 \\ -2 & 0 & -4 \end{bmatrix}$ 的列空间由 $(4, 3, -2)^{\mathsf T}$ 张成，它也在 $\mathcal{N}(A + I)$ 中，取 $\boldsymbol{p}_1 = (4, 3, -2)^{\mathsf T}$；解 $(A + I)\boldsymbol{x} = \boldsymbol{p}_1$ 得 $\boldsymbol{p}_2 = (1, 0, 0)^{\mathsf T}$；再取 $\mathcal{N}(A + I)$ 中与 $\boldsymbol{p}_1$ 无关的 $\boldsymbol{p}_3 = (0, 1, 0)^{\mathsf T}$。$P = (\boldsymbol{p}_1, \boldsymbol{p}_2, \boldsymbol{p}_3)$ 使 $P^{-1}AP = J$。

**例 10.10.2** 求 $A = \begin{bmatrix} 1 & 1 & 1 & 1 & 1 & 1 \\ 0 & 2 & 0 & 1 & 2 & 3 \\ 0 & 0 & 2 & 0 & 1 & -1 \\ 0 & 0 & 0 & 2 & 1 & 2 \\ 0 & 0 & 0 & 0 & 2 & 0 \\ 0 & 0 & 0 & 0 & 0 & 2 \end{bmatrix}$ 的 Jordan 形与 Jordan 基。

1. $\det(\lambda I_6 - A) = (\lambda - 1)(\lambda - 2)^5$。
2. 记 $N = A - 2I$。$\operatorname{rank}(N) = 4$，$\operatorname{rank}(N^2) = 2$，$\operatorname{rank}(N^3) = 1 = 6 - 5$，停止。关于 $2$ 的阶数 $\ge 1, \ge 2, \ge 3$ 的块数分别为 $6 - 4 = 2$、$4 - 2 = 2$、$2 - 1 = 1$，即一个 $3$ 阶块和一个 $2$ 阶块：$J = \operatorname{diag}(1, J_{2,3}, J_{2,2})$。
3. $\mu = 1$：$\boldsymbol{p}_1 = \boldsymbol{e}_1$。$\mu = 2$ 的第 $3$ 层：取 $\boldsymbol{y} = (-2, 0, 0, 0, 1, 0)^{\mathsf T} \in N_3 \setminus N_2$，链为 $N^2\boldsymbol{y} = (1, 1, 0, 0, 0, 0)^{\mathsf T}$，$N\boldsymbol{y} = (3, 2, 1, 1, 0, 0)^{\mathsf T}$，$\boldsymbol{y}$。第 $2$ 层：$N_2$ 由 $N_1 = \operatorname{span}\{(1,1,0,0,0,0)^{\mathsf T}, (1,0,1,0,0,0)^{\mathsf T}\}$ 及 $\boldsymbol{e}_4$、$(3, 0, 0, 0, -2, 1)^{\mathsf T}$ 张成。$\boldsymbol{e}_4$ 不能选：$\boldsymbol{e}_4 = N\boldsymbol{y} - 2(1,1,0,0,0,0)^{\mathsf T} - (1,0,1,0,0,0)^{\mathsf T}$ 落在 $N_1 + \operatorname{span}\{N\boldsymbol{y}\}$ 中，它的链底 $N\boldsymbol{e}_4 = N^2\boldsymbol{y}$ 与第一条链重合。取 $\boldsymbol{z} = (3, 0, 0, 0, -2, 1)^{\mathsf T}$，链为 $N\boldsymbol{z} = (-4, -1, -3, 0, 0, 0)^{\mathsf T}$，$\boldsymbol{z}$。
4. $P = (\boldsymbol{e}_1, N^2\boldsymbol{y}, N\boldsymbol{y}, \boldsymbol{y}, N\boldsymbol{z}, \boldsymbol{z}) = \begin{bmatrix} 1 & 1 & 3 & -2 & -4 & 3 \\ 0 & 1 & 2 & 0 & -1 & 0 \\ 0 & 0 & 1 & 0 & -3 & 0 \\ 0 & 0 & 1 & 0 & 0 & 0 \\ 0 & 0 & 0 & 1 & 0 & -2 \\ 0 & 0 & 0 & 0 & 0 & 1 \end{bmatrix}$，$\det P = -3 \ne 0$，$P^{-1}AP = J$。

Jordan 形是理论上的最简形，却不适合浮点计算：它不是矩阵元素的连续函数。下面的代码把 $J_{0,10}$ 的一个元素改动 $10^{-10}$，特征值就从全为 $0$ 变成模都等于 $(10^{-10})^{1/10} = 0.1$ 的十个不同的数，Jordan 形从一个 $10$ 阶块变成对角阵。

```python
import numpy as np

n, eps = 10, 1e-10
J = np.diag(np.ones(n - 1), k=1)       # nilpotent Jordan block J_{0,10}
Jp = J.copy()
Jp[-1, 0] = eps                         # perturb a single entry by 1e-10
print(np.abs(np.linalg.eigvals(J)).max())    # 0.0
print(np.abs(np.linalg.eigvals(Jp)))         # all about eps**(1/n) = 0.1
```

一般地，扰动 $J_{0,k}$ 的左下角元素为 $\varepsilon$ 时，特征多项式变为 $\lambda^k - \varepsilon$，特征值是 $\varepsilon$ 的 $k$ 个 $k$ 次方根，变化量为 $\varepsilon^{1/k}$，块越大越敏感；而对正规矩阵 $A$（[第 12 章](/2.1.12)），$A + E$ 的每个特征值与 $A$ 的某个特征值相距不超过 $\|E\|_2$（Bauer–Fike 定理）。

![左：10 阶幂零 Jordan 块的左下角元素改为 ε 后，特征值从 0 跳到半径为 ε 的十次方根的圆上，三种 ε 分别对应半径 0.1、0.25、0.5；右：k 阶 Jordan 块的特征值变化量 ε^(1/k) 与正规矩阵的变化上界 ε 的比较（对数坐标）](./plots/jordan-perturbation.py)

因此数值软件计算的是 Schur 形（[第 12 章](/2.1.12)的酉三角化），Jordan 形主要用于理论推导、精确计算和[下一章](/2.1.11)的矩阵函数。

## 小结

| 对象 | 内容 | 如何计算 |
|---|---|---|
| 直和 | 定义 10.1.1；四个等价条件（定理 10.1.1） | 比较维数，或检验基的并线性无关 |
| 不变子空间 | 定义 10.2.1；不变子空间 $\Leftrightarrow$ 分块上三角，不变补 $\Leftrightarrow$ 分块对角（定理 10.2.1） | 核、象、特征子空间、根子空间都是不变的 |
| Schur 定理 | 复方阵相似于上三角阵（定理 10.3.1） | 算法 10.3.1：取特征向量、扩充、对右下块递归 |
| 根子空间 | $G_\mu = \mathcal{N}\left((A - \mu I)^{n_\mu}\right)$，$\dim G_\mu$ = 代数重数 | 秩序列 $\operatorname{rank}\left((A - \mu I)^k\right)$ |
| 根子空间分解 | $\mathbb{C}^n = \bigoplus G_{\mu_i}$，$A$ 相似于每块只有一个特征值的分块对角阵（定理 10.5.1、10.5.2） | 各 $\mathcal{N}\left((A - \mu_iI)^{n_i}\right)$ 的基拼成 $P$ |
| 极小多项式 | $m_A = \prod (x - \mu_i)^{m_i}$，$m_i$ = 最大块阶数；可对角化 $\Leftrightarrow$ 无重根（性质 10.6.1） | 秩序列停止下降的位置 |
| 幂零变换 | 循环子空间分解（定理 10.8.1），块数 $= \dim\mathcal{N}(T)$，最大块 = 幂零指数 | 对 $\mathcal{R}(T)$ 归纳 |
| Jordan 形 | 存在且唯一（定理 10.9.2）；块数公式（定理 10.9.3）；相似 $\Leftrightarrow$ 秩序列相同 | 只用秩 |
| Jordan 基 | 由 Jordan 链组成 | 算法 10.10.1：自上而下选链顶，保证无关 |

整章把"相似意义下的最简形"拆成了三个标准问题：多项式求根、算秩、解线性方程组。其中只有求根需要数值迭代，块的结构完全由有限次消元决定。Jordan 形的数值不稳定性则说明，理论上的最简形与计算上的好形式未必相同，后者通常是用酉变换得到的 Schur 形。
