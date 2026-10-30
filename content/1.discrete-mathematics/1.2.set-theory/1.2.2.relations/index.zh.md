---
title: 关系
---

关系刻画集合元素之间的联系。本章把关系定义为有序对的集合（见定义 1.3.4），介绍关系的表示（矩阵与图）、运算（逆、合成、限制、象）、基本性质（自反、对称、反对称、传递）与闭包，然后讨论三类重要的关系：等价关系及其与划分的对应、相容关系与覆盖、偏序关系与偏序集。下一章的函数就是一类特殊的关系。

## 2.1. 二元关系

如果一个集合是空集，或者它的元素都是**有序对**，则称该集合为一个**二元关系**（binary relation），简称关系，常记作 $R$。对二元关系 $R$，若 $\langle x, y \rangle \in R$，也记作 $xRy$。

**定义 2.1.1（$A$ 到 $B$ 的二元关系）** 设 $A, B$ 为集合，$A \times B$ 的任一子集所定义的二元关系称为 $A$ 到 $B$ 的二元关系。特别地，当 $A = B$ 时，$A \times A$ 的任一子集称为 $A$ 上的一个二元关系。

**定义 2.1.2（$n$ 元关系）** 若 $n \in \mathbb{N}$，$n > 1$，$A_1, A_2, \cdots, A_n$ 是 $n$ 个集合，则 $A_1 \times A_2 \times \cdots \times A_n$ 的任一子集称为 $A_1, A_2, \cdots, A_n$ 上的一个 **$n$ 元关系**，它是 $n$ 元组的集合。

设 $A$ 是集合族，$A$ 上的包含关系和真包含关系分别定义为

$$
\begin{aligned}
R_{\subseteq} &= \{\langle x, y \rangle \mid x \in A \land y \in A \land x \subseteq y\}, \\
R_{\subset} &= \{\langle x, y \rangle \mid x \in A \land y \in A \land x \subset y\}.
\end{aligned}
$$

例如，对任意的集合 $A$，**幂集** $\mathcal{P}(A)$ 上的包含关系为 $\{\langle x, y \rangle \mid x \in \mathcal{P}(A) \land y \in \mathcal{P}(A) \land x \subseteq y\}$。

**定义 2.1.3（恒等关系、全域关系和空关系）** 对任意的集合 $A$，

1. $A$ 上的**恒等关系** $I_A = \{\langle x, x \rangle \mid x \in A\}$；
2. $A$ 上的**全域关系**（全关系）$E_A = \{\langle x, y \rangle \mid x \in A \land y \in A\} = A \times A$；
3. 空集 $\varnothing$ 是 $A \times A$ 的子集，称为 $A$ 上的**空关系**。

**定义 2.1.4（定义域和值域）** 设 $R$ 是 $A$ 到 $B$ 的二元关系，

1. $R$ 中所有有序对的第一元素构成的集合称为 $R$ 的**定义域**，记作 $\operatorname{dom}(R) = \{x \mid (\exists y)(\langle x, y \rangle \in R)\}$；
2. $R$ 中所有有序对的第二元素构成的集合称为 $R$ 的**值域**，记作 $\operatorname{ran}(R) = \{y \mid (\exists x)(\langle x, y \rangle \in R)\}$；
3. $R$ 的定义域和值域的并集称为 $R$ 的域，记作 $\operatorname{fld}(R) = \operatorname{dom}(R) \cup \operatorname{ran}(R)$。

## 2.2. 关系矩阵和关系图

**定义 2.2.1（关系矩阵）** 设集合 $X = \{x_1, x_2, \cdots, x_m\}$，$Y = \{y_1, y_2, \cdots, y_n\}$，$R$ 是 $X$ 到 $Y$ 的一个关系，则 $R$ 的**关系矩阵**是 $m \times n$ 矩阵 $M(R) = (r_{ij})_{m \times n}$，其中

$$
r_{ij} =
\begin{cases}
1, & \langle x_i, y_j \rangle \in R, \\
0, & \langle x_i, y_j \rangle \notin R,
\end{cases}
\qquad 1 \leq i \leq m,\ 1 \leq j \leq n.
$$

若 $R$ 是 $X$ 上的关系，则 $R$ 的关系矩阵是 $m \times m$ 方阵，定义与上述类似。

**定义 2.2.2（关系图）** 设集合 $X = \{x_1, x_2, \cdots, x_m\}$，$Y = \{y_1, y_2, \cdots, y_n\}$。

1. 若 $R$ 是 $X$ 到 $Y$ 的一个关系，则 $R$ 的**关系图**是一个有向图 $G(R) = (V, E)$，它的顶点集是 $V = X \cup Y$；从 $x_i$ 到 $y_j$ 的有向边 $e_{ij} \in E$ 当且仅当 $\langle x_i, y_j \rangle \in R$。
2. 若 $R$ 是 $X$ 上的一个关系，则 $R$ 的关系图是上述情形的特例，顶点集为 $X$。

## 2.3. 关系的逆、合成、限制和象

**定义 2.3.1（关系的逆、合成、限制和象）** 对 $X$ 到 $Y$ 的关系 $R$ 和 $Y$ 到 $Z$ 的关系 $S$，定义

1. $R$ 的逆 $R^{-1}$ 为 $Y$ 到 $X$ 的关系：
   $$
   R^{-1} = \{\langle y, x \rangle \mid \langle x, y \rangle \in R\};
   $$
2. $R$ 与 $S$ 的**合成** $S \circ R$（有些书中称为关系的左复合）为 $X$ 到 $Z$ 的关系：
   $$
   S \circ R = \{\langle x, z \rangle \mid (\exists y)(\langle x, y \rangle \in R \land \langle y, z \rangle \in S)\};
   $$
3. 对任意的集合 $A$，$R$ 在 $A$ 上的**限制** $R \upharpoonright A$ 为 $A$ 到 $Y$ 的关系：
   $$
   R \upharpoonright A = \{\langle x, y \rangle \mid \langle x, y \rangle \in R \land x \in A\};
   $$
4. $A$ 在 $R$ 下的象 $R[A]$ 为集合
   $$
   R[A] = \{y \mid (\exists x)(x \in A \land \langle x, y \rangle \in R)\}.
   $$

合成的关系矩阵可以用矩阵的逻辑乘计算。设 $A$ 是有限集合，$|A| = n$，$R$ 和 $S$ 都是 $A$ 上的关系，关系矩阵分别为 $n \times n$ 方阵 $M(R) = (r_{ij})$ 和 $M(S) = (s_{ij})$，则

$$
M(S \circ R) = M(R) \cdot M(S) = (w_{ij})_{n \times n}, \qquad w_{ij} = \bigvee_{k=1}^{n} (r_{ik} \land s_{kj}),
$$

其中 $\cdot$ 表示逻辑乘（与普通矩阵乘法类似，只是把乘法换成 $\land$、加法换成 $\lor$）。注意因子的次序：$S \circ R$ 先作 $R$ 后作 $S$，对应的矩阵是 $M(R)$ 在左、$M(S)$ 在右。

**定理 2.3.1（逆关系的性质）** 对 $X$ 到 $Y$ 的关系 $R$ 和 $Y$ 到 $Z$ 的关系 $S$，有

$$
\begin{aligned}
\operatorname{dom}(R^{-1}) &= \operatorname{ran}(R), & \operatorname{ran}(R^{-1}) &= \operatorname{dom}(R), \\
(R^{-1})^{-1} &= R, & (S \circ R)^{-1} &= R^{-1} \circ S^{-1}.
\end{aligned}
$$

**定理 2.3.2（关系合成的结合律）** 对 $X$ 到 $Y$ 的关系 $Q$、$Y$ 到 $Z$ 的关系 $S$ 和 $Z$ 到 $W$ 的关系 $R$，有

$$
(R \circ S) \circ Q = R \circ (S \circ Q).
$$

**定理 2.3.3（关系合成的其他性质）** 对 $X$ 到 $Y$ 的关系 $R_2, R_3$ 和 $Y$ 到 $Z$ 的关系 $R_1$，有

$$
\begin{aligned}
R_1 \circ (R_2 \cup R_3) &= R_1 \circ R_2 \cup R_1 \circ R_3, \\
R_1 \circ (R_2 \cap R_3) &\subseteq R_1 \circ R_2 \cap R_1 \circ R_3;
\end{aligned}
$$

对 $X$ 到 $Y$ 的关系 $R_3$ 和 $Y$ 到 $Z$ 的关系 $R_1, R_2$，有

$$
\begin{aligned}
(R_1 \cup R_2) \circ R_3 &= R_1 \circ R_3 \cup R_2 \circ R_3, \\
(R_1 \cap R_2) \circ R_3 &\subseteq R_1 \circ R_3 \cap R_2 \circ R_3.
\end{aligned}
$$

这里规定关系的合成运算优先于集合运算。两个包含式一般不能改为等式，例如取 $X = Y = Z = \{a, b\}$，$R_1 = \{\langle a, a \rangle, \langle b, a \rangle\}$，$R_2 = \{\langle a, a \rangle\}$，$R_3 = \{\langle a, b \rangle\}$，则 $R_2 \cap R_3 = \varnothing$，而 $R_1 \circ R_2 \cap R_1 \circ R_3 = \{\langle a, a \rangle\}$。

**定理 2.3.4（集合在关系下的象的性质）** 对 $X$ 到 $Y$ 的关系 $R$、集合 $A, B$ 和集合族 $\mathcal{A}$，有

$$
\begin{aligned}
R[A \cup B] &= R[A] \cup R[B], \\
R\left[\textstyle\bigcup \mathcal{A}\right] &= \textstyle\bigcup \{R[B] \mid B \in \mathcal{A}\}, \\
R[A \cap B] &\subseteq R[A] \cap R[B], \\
R\left[\textstyle\bigcap \mathcal{A}\right] &\subseteq \textstyle\bigcap \{R[B] \mid B \in \mathcal{A}\} \quad (\mathcal{A} \neq \varnothing), \\
R[A] - R[B] &\subseteq R[A - B].
\end{aligned}
$$

## 2.4. 关系的性质

**定义 2.4.1（自反性与非自反性）** 设 $R$ 为集合 $A$ 上的关系。若 $A$ 中每个元素 $x$ 都有 $xRx$，则称 $R$ 在 $A$ 上是自反的，或称 $R$ 是 $A$ 上的**自反关系**；若 $A$ 中没有元素 $x$ 使 $xRx$，则称 $R$ 在 $A$ 上是非自反的，或称 $R$ 是**非自反关系**。符号化表示为

$$
\begin{aligned}
R \text{ 在 } A \text{ 上是自反的} &\Leftrightarrow (\forall x)(x \in A \to \langle x, x \rangle \in R), \\
R \text{ 在 } A \text{ 上是非自反的} &\Leftrightarrow (\forall x)(x \in A \to \langle x, x \rangle \notin R).
\end{aligned}
$$

**定义 2.4.2（对称性与反对称性）** 设 $R$ 为集合 $A$ 上的关系。若对 $A$ 中任意的 $x, y$，由 $xRy$ 总能推出 $yRx$，则称 $R$ 是对称的，或称 $R$ 是 $A$ 上的**对称关系**；若 $xRy$ 与 $yRx$ 同时成立时必有 $x = y$，则称 $R$ 是反对称的，或称 $R$ 是 $A$ 上的**反对称关系**。符号化表示为

$$
\begin{aligned}
R \text{ 是对称的} &\Leftrightarrow (\forall x)(\forall y)((x \in A \land y \in A \land \langle x, y \rangle \in R) \to \langle y, x \rangle \in R), \\
R \text{ 是反对称的} &\Leftrightarrow (\forall x)(\forall y)((x \in A \land y \in A \land \langle x, y \rangle \in R \land \langle y, x \rangle \in R) \to x = y).
\end{aligned}
$$

反对称性的另一种等价定义为

$$
R \text{ 是反对称的} \Leftrightarrow (\forall x)(\forall y)((x \in A \land y \in A \land \langle x, y \rangle \in R \land x \neq y) \to \langle y, x \rangle \notin R).
$$

**定义 2.4.3（传递性）** 设 $R$ 为集合 $A$ 上的关系。若由 $xRy$ 与 $yRz$ 总能推出 $xRz$，则称 $R$ 是传递的，或称 $R$ 是 $A$ 上的**传递关系**。符号化表示为

$$
R \text{ 是传递的} \Leftrightarrow (\forall x)(\forall y)(\forall z)((x, y, z \in A \land \langle x, y \rangle \in R \land \langle y, z \rangle \in R) \to \langle x, z \rangle \in R).
$$

**定理 2.4.1（自反性的保持）** 设 $R_1, R_2$ 是 $A$ 上的自反关系，则 $R_1^{-1}$、$R_1 \cap R_2$、$R_1 \cup R_2$ 也是 $A$ 上的自反关系。

**定理 2.4.2（对称性的保持）** 设 $R_1, R_2$ 是 $A$ 上的对称关系，则 $R_1^{-1}$、$R_1 \cap R_2$、$R_1 \cup R_2$ 也是 $A$ 上的对称关系。

**定理 2.4.3（传递性的保持）** 设 $R_1, R_2$ 是 $A$ 上的传递关系，则 $R_1^{-1}$、$R_1 \cap R_2$ 是 $A$ 上的传递关系，但 $R_1 \cup R_2$ 不一定是传递的。

例如在 $A = \{a, b, c\}$ 上，$R_1 = \{\langle a, b \rangle\}$ 与 $R_2 = \{\langle b, c \rangle\}$ 都是传递的，但 $R_1 \cup R_2$ 含 $\langle a, b \rangle$、$\langle b, c \rangle$ 而不含 $\langle a, c \rangle$，不是传递的。

**定理 2.4.4（反对称性的保持）** 设 $R_1, R_2$ 是 $A$ 上的反对称关系，则 $R_1^{-1}$、$R_1 \cap R_2$ 是 $A$ 上的反对称关系，但 $R_1 \cup R_2$ 不一定是反对称的。

例如 $R_1 = \{\langle a, b \rangle\}$ 与 $R_2 = \{\langle b, a \rangle\}$ 都是反对称的，而 $R_1 \cup R_2$ 不是。

**定理 2.4.5（对称性与反对称性的刻画）** 设 $R$ 是 $A$ 上的关系，则

1. $R$ 是对称的 $\Leftrightarrow R = R^{-1}$；
2. $R$ 是反对称的 $\Leftrightarrow R \cap R^{-1} \subseteq I_A$。

## 2.5. 关系的闭包

**定义 2.5.1（关系的幂）** 设 $R$ 为 $A$ 上的关系，$n \in \mathbb{N}$，关系 $R$ 的 $n$ 次幂定义为

$$
\begin{aligned}
R^0 &= I_A = \{\langle x, x \rangle \mid x \in A\}, \\
R^{n+1} &= R^n \circ R \quad (n \geq 0).
\end{aligned}
$$

**定理 2.5.1（有限集合上关系的幂必有重复）** 设 $A$ 是有限集合，$|A| = n$，$R$ 是 $A$ 上的关系，则存在自然数 $s$ 和 $t$，$s \neq t$，使得 $R^s = R^t$。

这是因为 $A$ 上只有 $2^{n^2}$ 个不同的关系，而 $R^0, R^1, R^2, \cdots$ 有无穷多项。

**定理 2.5.2（关系的幂运算律）** 设 $R$ 是 $A$ 上的关系，$m$ 和 $n$ 是自然数，则

$$
R^m \circ R^n = R^{m+n}, \qquad (R^m)^n = R^{mn}.
$$

**定理 2.5.3（有限集合上关系的幂序列具有周期性）** 设 $A$ 是有限集合，$R$ 是 $A$ 上的关系。若存在自然数 $s$ 和 $t$，$s < t$，使得 $R^s = R^t$，则

1. $R^{s+k} = R^{t+k}$，其中 $k \in \mathbb{N}$；
2. $R^{s+lp+i} = R^{s+i}$，其中 $l, i \in \mathbb{N}$，$p = t - s$；
3. 令 $B = \{R^0, R^1, \cdots, R^{t-1}\}$，则 $R$ 的各次幂均为 $B$ 的元素，即对任意的 $q \in \mathbb{N}$，有 $R^q \in B$。

**定义 2.5.2（闭包）** 设 $R$ 是非空集合 $A$ 上的关系。$R$ 的**自反闭包**（**对称闭包**、**传递闭包**）是 $A$ 上满足下列条件的关系 $R'$：

1. $R'$ 是自反的（对称的、传递的）；
2. $R \subseteq R'$；
3. 对 $A$ 上任何包含 $R$ 的自反的（对称的、传递的）关系 $R''$，有 $R' \subseteq R''$。

$R$ 的自反闭包记作 $r(R)$，对称闭包记作 $s(R)$，传递闭包记作 $t(R)$。它们分别是包含 $R$ 且具有自反性（对称性、传递性）的最小关系。

**定理 2.5.4（闭包的性质 1）** 对非空集合 $A$ 上的关系 $R$，有

1. $R$ 是自反的 $\Leftrightarrow r(R) = R$；
2. $R$ 是对称的 $\Leftrightarrow s(R) = R$；
3. $R$ 是传递的 $\Leftrightarrow t(R) = R$。

**定理 2.5.5（闭包的性质 2）** 对非空集合 $A$ 上的关系 $R_1, R_2$，若 $R_1 \subseteq R_2$，则

$$
r(R_1) \subseteq r(R_2), \qquad s(R_1) \subseteq s(R_2), \qquad t(R_1) \subseteq t(R_2).
$$

**定理 2.5.6（闭包的性质 3）** 对非空集合 $A$ 上的关系 $R_1, R_2$，

$$
\begin{aligned}
r(R_1) \cup r(R_2) &= r(R_1 \cup R_2), \\
s(R_1) \cup s(R_2) &= s(R_1 \cup R_2), \\
t(R_1) \cup t(R_2) &\subseteq t(R_1 \cup R_2).
\end{aligned}
$$

**定理 2.5.7（自反闭包的构造方法）** 对非空集合 $A$ 上的关系 $R$，有

$$
r(R) = R \cup I_A.
$$

**定理 2.5.8（对称闭包的构造方法）** 对非空集合 $A$ 上的关系 $R$，有

$$
s(R) = R \cup R^{-1}.
$$

**定理 2.5.9（传递闭包的构造方法）** 对非空集合 $A$ 上的关系 $R$，有

$$
t(R) = R \cup R^2 \cup R^3 \cup \cdots = \bigcup_{i=1}^{\infty} R^i.
$$

**定理 2.5.10（传递闭包的有限构造方法）** 设 $A$ 为非空有限集合，$|A| = n$，$R$ 是 $A$ 上的关系，则存在正整数 $k \leq n$，使得

$$
t(R) = R \cup R^2 \cup \cdots \cup R^k.
$$

**例 2.5.1** 设 $A = \{a, b, c\}$，$R = \{\langle a, b \rangle, \langle b, c \rangle, \langle c, a \rangle\}$。则

$$
\begin{aligned}
R^2 &= \{\langle a, c \rangle, \langle b, a \rangle, \langle c, b \rangle\}, \\
R^3 &= \{\langle a, a \rangle, \langle b, b \rangle, \langle c, c \rangle\} = I_A,
\end{aligned}
$$

于是 $t(R) = R \cup R^2 \cup R^3 = A \times A$，这里 $k = 3 = n$。又 $R^4 = R^3 \circ R = R$，即 $R^1 = R^4$，幂序列以 $p = 3$ 为周期（定理 2.5.3）。

**定理 2.5.11（闭包同时具有的多种性质 1）** 对非空集合 $A$ 上的关系 $R$，有

1. 若 $R$ 是自反的，则 $s(R)$ 和 $t(R)$ 是自反的；
2. 若 $R$ 是对称的，则 $r(R)$ 和 $t(R)$ 是对称的；
3. 若 $R$ 是传递的，则 $r(R)$ 是传递的。

注意 $R$ 传递时 $s(R)$ 未必传递：$R = \{\langle a, b \rangle\}$ 是传递的，而 $s(R) = \{\langle a, b \rangle, \langle b, a \rangle\}$ 不含 $\langle a, a \rangle$，不是传递的。

**定理 2.5.12（闭包同时具有的多种性质 2）** 对非空集合 $A$ 上的关系 $R$，有

1. $rs(R) = sr(R)$；
2. $rt(R) = t r(R)$；
3. $st(R) \subseteq ts(R)$，

其中 $rs(R) = r(s(R))$，其他类似。

## 2.6. 等价关系和划分

**定义 2.6.1（等价关系）** 设 $R$ 为非空集合 $A$ 上的关系，如果 $R$ 是自反的、对称的和传递的，则称 $R$ 为 $A$ 上的**等价关系**。

**定义 2.6.2（等价类）** 设 $R$ 为非空集合 $A$ 上的等价关系，对任意的 $x \in A$，称集合

$$
[x]_R = \{y \mid y \in A \land xRy\}
$$

为 $x$ 关于 $R$ 的**等价类**，简称 $x$ 的等价类，也可简记作 $[x]$ 或 $\overline{x}$。

**定理 2.6.1（等价类的性质）** 设 $R$ 是非空集合 $A$ 上的等价关系，对任意的 $x, y \in A$，有

1. $[x]_R \neq \varnothing$ 且 $[x]_R \subseteq A$，即 $[x]_R$ 是 $A$ 的非空子集；
2. 若 $xRy$，则 $[x]_R = [y]_R$；
3. 若 $\langle x, y \rangle \notin R$，则 $[x]_R \cap [y]_R = \varnothing$；
4. $\bigcup \{[x]_R \mid x \in A\} = A$。

**定义 2.6.3（商集）** 设 $R$ 为非空集合 $A$ 上的等价关系，以 $R$ 的所有等价类为元素的集合称为 $A$ 关于 $R$ 的**商集**，记作 $A/R$，即

$$
A/R = \{[x]_R \mid x \in A\}.
$$

**定义 2.6.4（划分）** 设 $A$ 为非空集合。$A$ 的一个**划分**是满足下列条件的集合 $\pi$，$\pi$ 中的元素称为 $A$ 的**划分块**：

1. $(\forall x)(x \in \pi \to x \subseteq A)$；
2. $\varnothing \notin \pi$；
3. $\bigcup \pi = A$；
4. $(\forall x)(\forall y)((x \in \pi \land y \in \pi \land x \neq y) \to x \cap y = \varnothing)$。

**定理 2.6.2（等价关系诱导的划分）** 对非空集合 $A$ 上的等价关系 $R$，商集 $A/R$ 是 $A$ 的划分，称为由等价关系 $R$ 诱导出的 $A$ 的划分，记作 $\pi_R$。

**定理 2.6.3（划分诱导的等价关系）** 对非空集合 $A$ 的一个划分 $\pi$，令 $A$ 上的关系

$$
R_\pi = \{\langle x, y \rangle \mid (\exists z)(z \in \pi \land x \in z \land y \in z)\},
$$

则 $R_\pi$ 为 $A$ 上的等价关系，称为划分 $\pi$ 诱导出的 $A$ 上的等价关系。

**定理 2.6.4（划分与等价关系一一对应）** 对非空集合 $A$ 的一个划分 $\pi$ 和 $A$ 上的等价关系 $R$，$\pi$ 诱导 $R$ 当且仅当 $R$ 诱导 $\pi$，即 $R_\pi = R \Leftrightarrow A/R = \pi$。

**例 2.6.1** 在 $A = \{1, 2, \cdots, 8\}$ 上定义 $xRy \Leftrightarrow x \equiv y \pmod 3$，则 $R$ 是等价关系，商集

$$
A/R = \{\{1, 4, 7\}, \{2, 5, 8\}, \{3, 6\}\}
$$

就是 $A$ 的一个划分；反过来，由这个划分按定理 2.6.3 诱导出的等价关系正是 $R$。

## 2.7. 相容关系和覆盖

**定义 2.7.1（相容关系）** 对非空集合 $A$ 上的关系 $R$，如果 $R$ 是自反的、对称的，则称 $R$ 为 $A$ 上的**相容关系**。

**定义 2.7.2（相容类）** 对非空集合 $A$ 上的相容关系 $R$，若 $C \subseteq A$，且 $C$ 中任意两个元素 $x$ 和 $y$ 都有 $xRy$，则称 $C$ 是由相容关系 $R$ 产生的相容类，简称**相容类**。这个条件也可以写成

$$
(\forall x)(\forall y)((x \in C \land y \in C) \to xRy).
$$

**定义 2.7.3（最大相容类）** 对非空集合 $A$ 上的相容关系 $R$，一个相容类若不是任何相容类的真子集，就称为**最大相容类**，记作 $C_R$。最大相容类 $C_R$ 有下列性质：

$$
\begin{aligned}
& (\forall x)(\forall y)((x \in C_R \land y \in C_R) \to xRy), \\
& (\forall x)(x \in A - C_R \to (\exists y)(y \in C_R \land \lnot xRy)).
\end{aligned}
$$

即 $C_R$ 中任意两个元素相容，而 $C_R$ 之外的任一元素都与 $C_R$ 中某个元素不相容。

**定理 2.7.1（最大相容类的存在性）** 对非空有限集合 $A$ 上的相容关系 $R$，若 $C$ 是一个相容类，则存在一个最大相容类 $C_R$，使 $C \subseteq C_R$。

**定义 2.7.4（覆盖）** 设 $A$ 为非空集合。$A$ 的一个**覆盖**是满足下列条件的集合 $\Omega$，$\Omega$ 中的元素称为 $\Omega$ 的**覆盖块**：

1. $(\forall x)(x \in \Omega \to x \subseteq A)$；
2. $\varnothing \notin \Omega$；
3. $\bigcup \Omega = A$。

划分是覆盖块两两不相交的覆盖。

**定理 2.7.2（完全覆盖）** 对非空集合 $A$ 上的相容关系 $R$，所有最大相容类组成的集合是 $A$ 的一个覆盖，称为 $A$ 的完全覆盖，记作 $C_R(A)$，而且 $C_R(A)$ 是唯一的。

**定理 2.7.3（覆盖确定的相容关系）** 对非空集合 $A$ 的一个覆盖 $\Omega = \{A_1, A_2, \cdots, A_n\}$，由 $\Omega$ 确定的关系

$$
R = A_1 \times A_1 \cup A_2 \times A_2 \cup \cdots \cup A_n \times A_n
$$

是 $A$ 上的相容关系。

不同的覆盖可能确定同一个相容关系：例如在 $A = \{1, 2, 3\}$ 上，$\Omega_1 = \{\{1, 2\}, \{2, 3\}\}$ 与 $\Omega_2 = \{\{1, 2\}, \{2, 3\}, \{2\}\}$ 确定同一个相容关系。因此相容关系与覆盖之间没有像等价关系与划分那样的一一对应；与相容关系 $R$ 唯一对应的是完全覆盖 $C_R(A)$。

## 2.8. 偏序关系

**定义 2.8.1（偏序关系）** 对非空集合 $A$ 上的关系 $R$，如果 $R$ 是自反的、反对称的和传递的，则称 $R$ 为 $A$ 上的**偏序关系**。

在不会产生误解时，偏序关系 $R$ 通常记作 $\leq$；当 $xRy$ 时记作 $x \leq y$，读作"$x$ 小于等于 $y$"。偏序关系又称弱偏序关系或半序关系。

**定义 2.8.2（拟序关系）** 对非空集合 $A$ 上的关系 $R$，如果 $R$ 是非自反的和传递的，则称 $R$ 为 $A$ 上的**拟序关系**，又称强偏序关系。

在不会产生误解时，拟序关系 $R$ 通常记作 $<$；当 $xRy$ 时记作 $x < y$，读作"$x$ 小于 $y$"。

**定理 2.8.1** 若 $R$ 为 $A$ 上的拟序关系，则 $R$ 是反对称的。

**定理 2.8.2** 对 $A$ 上的拟序关系 $R$，$R \cup I_A$ 是 $A$ 上的偏序关系。

**定理 2.8.3** 对 $A$ 上的偏序关系 $R$，$R - I_A$ 是 $A$ 上的拟序关系。

**定义 2.8.3（偏序集）** 集合 $A$ 与 $A$ 上的关系 $R$ 一起称为一个结构。集合 $A$ 与 $A$ 上的偏序关系 $R$ 一起称为一个偏序结构，或称**偏序集**，记作 $(A, R)$。

**定义 2.8.4（盖住关系）** 对偏序集 $(A, \leq)$，若 $x, y \in A$，$x \leq y$，$x \neq y$，且不存在 $z \in A$ 使得 $x \leq z \leq y$ 且 $z \neq x$、$z \neq y$，则称 $y$ **盖住** $x$。$A$ 上的**盖住关系**定义为

$$
\operatorname{cov} A = \{\langle x, y \rangle \mid x \in A \land y \in A \land y \text{ 盖住 } x\}.
$$

有限偏序集可以用盖住关系画出的哈斯图（Hasse diagram）表示：每个元素画成一个点，$y$ 盖住 $x$ 时把 $y$ 画在 $x$ 上方并连一条线。

![$\mathcal{P}(\{a, b, c\})$ 按包含关系的哈斯图：$y$ 盖住 $x$（$y$ 比 $x$ 多一个元素）时把 $y$ 画在上方并连线；同一层的子集大小相同、两两不可比](./plots/hasse-powerset.py)

**定义 2.8.5（最小元、最大元、极小元、极大元）** 对偏序集 $(A, \leq)$ 和 $B \subseteq A$，

1. 若 $y \in B \land (\forall x)(x \in B \to y \leq x)$，则称 $y$ 为 $B$ 的**最小元**；
2. 若 $y \in B \land (\forall x)(x \in B \to x \leq y)$，则称 $y$ 为 $B$ 的**最大元**；
3. 若 $y \in B \land (\forall x)((x \in B \land x \leq y) \to x = y)$，则称 $y$ 为 $B$ 的**极小元**；
4. 若 $y \in B \land (\forall x)((x \in B \land y \leq x) \to x = y)$，则称 $y$ 为 $B$ 的**极大元**。

最小元（最大元）若存在则唯一，并且一定是极小元（极大元）；反之不然。

**定义 2.8.6（上界、下界、上确界、下确界）** 对偏序集 $(A, \leq)$ 和 $B \subseteq A$，

1. 若 $y \in A \land (\forall x)(x \in B \to x \leq y)$，则称 $y$ 为 $B$ 的**上界**；
2. 若 $y \in A \land (\forall x)(x \in B \to y \leq x)$，则称 $y$ 为 $B$ 的**下界**；
3. 令 $C = \{y \mid y \text{ 是 } B \text{ 的上界}\}$，则 $C$ 的最小元称为 $B$ 的**上确界**或最小上界；
4. 令 $C = \{y \mid y \text{ 是 } B \text{ 的下界}\}$，则 $C$ 的最大元称为 $B$ 的**下确界**或最大下界。

**例 2.8.1** 在偏序集 $(\mathcal{P}(\{a, b\}), \subseteq)$ 中取 $B = \{\{a\}, \{b\}\}$。$B$ 没有最小元和最大元，$\{a\}$ 和 $\{b\}$ 既是 $B$ 的极小元又是极大元；$B$ 的上界只有 $\{a, b\}$，下界只有 $\varnothing$，因此上确界为 $\{a, b\}$，下确界为 $\varnothing$。

**定义 2.8.7（可比）** 对偏序集 $(A, \leq)$ 和 $x, y \in A$，若 $x \leq y$ 或 $y \leq x$，则称 $x$ 和 $y$ 是**可比**的。

**定义 2.8.8（全序关系与全序集）** 对偏序集 $(A, \leq)$，如果对任意的 $x, y \in A$，$x$ 和 $y$ 都可比，则称 $\leq$ 为 $A$ 上的**全序关系**，或称线序关系，并称 $(A, \leq)$ 为**全序集**。

**定义 2.8.9（链、反链）** 对偏序集 $(A, \leq)$ 和 $B \subseteq A$，

1. 如果对任意的 $x, y \in B$，$x$ 和 $y$ 都是可比的，则称 $B$ 为 $A$ 中的**链**，$B$ 中元素的个数称为链的长度；
2. 如果对任意的 $x, y \in B$，$x \neq y$ 时 $x$ 和 $y$ 都不可比，则称 $B$ 为 $A$ 中的**反链**，$B$ 中元素的个数称为反链的长度。

**定理 2.8.4（偏序集的分解定理）** 对有限偏序集 $(A, \leq)$，设 $A$ 中最长链的长度是 $n$，则将 $A$ 中元素分成不相交的反链时，反链的个数至少是 $n$；并且恰好可以分成 $n$ 个不相交的反链。

**定理 2.8.5** 对偏序集 $(A, \leq)$，若 $A$ 中元素为 $mn + 1$ 个，则 $A$ 中或者存在一条长度为 $m + 1$ 的反链，或者存在一条长度为 $n + 1$ 的链。

**证明** 若 $A$ 中没有长度为 $n + 1$ 的链，则最长链的长度不超过 $n$，由定理 2.8.4，$A$ 可以分成至多 $n$ 个不相交的反链。$mn + 1$ 个元素分到至多 $n$ 个反链中，必有一个反链至少含 $m + 1$ 个元素。$\square$

**定义 2.8.10（良序关系与良序集）** 对偏序集 $(A, \leq)$，如果 $A$ 的任何非空子集都有最小元，则称 $\leq$ 为**良序关系**，称 $(A, \leq)$ 为**良序集**。

**定理 2.8.6** 一个良序集一定是全序集。

**定理 2.8.7** 一个有限的全序集一定是良序集。

**定理 2.8.8（良序定理）** 任意的集合都是可以良序化的。

良序定理（well-ordering theorem）与**选择公理**等价。$(\mathbb{N}, \leq)$ 是良序集，而 $(\mathbb{Z}, \leq)$ 与 $(\mathbb{R}, \leq)$ 是全序集但不是良序集。

**定义 2.8.11（区间）** 在全序集 $(\mathbb{R}, \leq)$ 上，对 $a, b \in \mathbb{R}$，$a < b$，

1. $[a, b] = \{x \mid x \in \mathbb{R} \land a \leq x \leq b\}$，称为从 $a$ 到 $b$ 的**闭区间**；
2. $(a, b) = \{x \mid x \in \mathbb{R} \land a < x < b\}$，称为从 $a$ 到 $b$ 的**开区间**；
3. $[a, b) = \{x \mid x \in \mathbb{R} \land a \leq x < b\}$ 和 $(a, b] = \{x \mid x \in \mathbb{R} \land a < x \leq b\}$ 都称为从 $a$ 到 $b$ 的**半开区间**；
4. 还可以定义无穷区间：$(-\infty, a] = \{x \mid x \in \mathbb{R} \land x \leq a\}$，$(-\infty, a) = \{x \mid x \in \mathbb{R} \land x < a\}$，$[a, +\infty) = \{x \mid x \in \mathbb{R} \land a \leq x\}$，$(a, +\infty) = \{x \mid x \in \mathbb{R} \land a < x\}$，$(-\infty, +\infty) = \mathbb{R}$。

## 小结

- 二元关系是笛卡儿积的子集（定义 2.1.1）；有限集合上的关系可以用关系矩阵或关系图表示（定义 2.2.1、定义 2.2.2）。关系的逆、合成、限制与象（定义 2.3.1）满足 $(S \circ R)^{-1} = R^{-1} \circ S^{-1}$（定理 2.3.1）和合成的结合律（定理 2.3.2）。
- 关系的性质（定义 2.4.1–2.4.3）在运算下的保持情况：

  | 运算 | 自反 | 对称 | 传递 | 反对称 |
  | :-- | :-: | :-: | :-: | :-: |
  | 逆 $R^{-1}$ | 保持 | 保持 | 保持 | 保持 |
  | 交 $R_1 \cap R_2$ | 保持 | 保持 | 保持 | 保持 |
  | 并 $R_1 \cup R_2$ | 保持 | 保持 | 不一定 | 不一定 |

  详见定理 2.4.1–2.4.4。
- 闭包（定义 2.5.2）是包含 $R$ 并具有某性质的最小关系：$r(R) = R \cup I_A$，$s(R) = R \cup R^{-1}$，$t(R) = \bigcup_{i \geq 1} R^i$（定理 2.5.7–2.5.9）；$\lvert A\rvert = n$ 时传递闭包只需并到 $R^k$，$k \leq n$（定理 2.5.10）。
- 三类重要关系：

  | 关系 | 性质 | 对应的结构 |
  | :-- | :-- | :-- |
  | 等价关系（定义 2.6.1） | 自反、对称、传递 | 等价类、商集 $A/R$；与划分一一对应（定理 2.6.4） |
  | 相容关系（定义 2.7.1） | 自反、对称 | 最大相容类组成完全覆盖（定理 2.7.2） |
  | 偏序关系（定义 2.8.1） | 自反、反对称、传递 | 偏序集与哈斯图；去掉 $I_A$ 得拟序（定理 2.8.3） |

- 偏序集中要区分最大（小）元与极大（小）元、上（下）界与上（下）确界（定义 2.8.5、定义 2.8.6）；有限偏序集可以分成最长链长度那么多个反链（定理 2.8.4），由此 $mn + 1$ 个元素中必有长 $m + 1$ 的反链或长 $n + 1$ 的链（定理 2.8.5）。良序集一定是全序集（定理 2.8.6），良序定理（定理 2.8.8）断言任何集合都可以良序化。
