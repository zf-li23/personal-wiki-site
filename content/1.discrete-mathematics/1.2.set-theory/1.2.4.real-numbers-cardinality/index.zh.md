---
title: 实数集合与集合的基数
---

本章先在集合论中依次构造整数、有理数和实数，再用双射比较任意集合的大小：引入等势、有限集合与无限集合、基数及其运算和比较，最后讨论可数集合与连续统假设。第 1 章中有限集合的基数（定义 1.6.1）在这里推广到任意集合。

## 4.1. 实数集合

**定义 4.1.1（整数）** 对自然数集合 $\mathbb{N}$，令

$$
\begin{aligned}
\mathbb{Z}_+ &= \mathbb{N} - \{0\}, \\
\mathbb{Z}_- &= \{\langle 0, n \rangle \mid n \in \mathbb{Z}_+\}, \\
\mathbb{Z} &= \mathbb{Z}_- \cup \{0\} \cup \mathbb{Z}_+,
\end{aligned}
$$

则称 $\mathbb{Z}_+$ 的元素为正整数，$\mathbb{Z}_-$ 的元素为负整数，$\mathbb{Z}$ 的元素为整数。

**定义 4.1.2（相反数）** 整数的相反数定义为

$$
\begin{aligned}
-n &= \langle 0, n \rangle, \quad n \in \mathbb{Z}_+, \\
-0 &= 0, \\
-\langle 0, n \rangle &= n, \quad n \in \mathbb{Z}_+.
\end{aligned}
$$

**定义 4.1.3（整数的大小）** 在集合 $\mathbb{Z}$ 上定义小于等于关系 $\leq$：对任意的 $x, y \in \mathbb{Z}$，$x \leq y$ 当且仅当

$$
(x \in \mathbb{N} \land y \in \mathbb{N} \land x \leq y) \lor (x \in \mathbb{Z}_- \land y \in \mathbb{N}) \lor (x \in \mathbb{Z}_- \land y \in \mathbb{Z}_- \land -y \leq -x),
$$

其中 $x, y \in \mathbb{N}$ 时的 $\leq$ 是自然数的小于等于关系（定义 1.7.5）。在集合 $\mathbb{Z}$ 上定义小于关系 $<$：对任意的 $x, y \in \mathbb{Z}$，

$$
x < y \Leftrightarrow (x \leq y \land x \neq y).
$$

**定义 4.1.4（$Q_1$ 上的关系 $\approx$）** 对整数集合 $\mathbb{Z}$，令

$$
Q_1 = \mathbb{Z} \times (\mathbb{Z} - \{0\}) = \{\langle a, b \rangle \mid a \in \mathbb{Z} \land b \in \mathbb{Z} \land b \neq 0\},
$$

称 $Q_1$ 是 $\mathbb{Z}$ 上的分式的集合。对 $\langle a, b \rangle \in Q_1$，可以用 $a/b$ 代替 $\langle a, b \rangle$。在 $Q_1$ 上定义关系 $\approx$：对任意的 $a/b \in Q_1$，$c/d \in Q_1$，

$$
a/b \approx c/d \Leftrightarrow a \cdot d = b \cdot c,
$$

其中 $\cdot$ 是 $\mathbb{Z}$ 上的乘法，$=$ 是 $\mathbb{Z}$ 上的相等关系。

**定理 4.1.1** $Q_1$ 上的关系 $\approx$ 是等价关系。

**定义 4.1.5（有理数）** 令 $\mathbb{Q} = Q_1/{\approx}$，即 $\mathbb{Q}$ 是 $Q_1$ 关于等价关系 $\approx$ 的商集，则称 $\mathbb{Q}$ 的元素为有理数。一般用 $a/b$ 表示 $\mathbb{Q}$ 中的元素 $[\langle a, b \rangle]_{\approx}$，并习惯上取 $a, b$ 为互素的整数，且 $b > 0$。

**定义 4.1.6（有理数的大小）** 在 $\mathbb{Q}$ 上定义小于等于关系 $\leq$：对任意的 $a/b, c/d \in \mathbb{Q}$（其中 $b > 0$，$d > 0$），

$$
a/b \leq c/d \Leftrightarrow a \cdot d \leq b \cdot c.
$$

分母取正是必要的：$1/2 \leq 1/1$，但若写成 $1/2$ 与 $(-1)/(-1)$，则 $1 \cdot (-1) \leq 2 \cdot (-1)$ 不成立。

**定义 4.1.7（基本函数）** 如果 $f: \mathbb{N} \rightarrow \mathbb{Q}$ 满足条件：

1. $(\exists x)(x \in \mathbb{Q} \land (\forall n)(n \in \mathbb{N} \rightarrow f(n) \leq x))$；
2. $(\exists n)(n \in \mathbb{N} \land (\forall m)(\forall i)((m \in \mathbb{N} \land i \in \mathbb{N} \land n \leq m \leq i) \rightarrow f(m) \leq f(i)))$，

即 $f$ 有上界，并且从某一项起单调不减，则称 $f$ 是一个基本函数，或有界非递减函数。当 $f$ 是一个基本函数时，函数值序列

$$
f(0), f(1), f(2), \cdots, f(n), \cdots
$$

称为一个基本序列，有时写为 $r_0, r_1, r_2, \cdots, r_n, \cdots$。以下用 $B$ 表示所有基本函数组成的集合，用 $BF(f)$ 表示 $f$ 是一个基本函数。

**定理 4.1.2** 当 $f: \mathbb{N} \rightarrow \mathbb{Q}$ 取常数值时，$f$ 是基本函数。即对任意的 $r \in \mathbb{Q}$，$r, r, r, \cdots$ 是一个基本序列。

**定理 4.1.3** 存在不是常值函数的基本函数。

**定义 4.1.8（基本函数的等价）** 对基本函数的集合 $B$，定义 $B$ 上的关系 $\sim$：对任意的 $f, g \in B$，$f \sim g$ 当且仅当

$$
(\forall \varepsilon)((\varepsilon \in \mathbb{Q} \land \varepsilon > 0) \rightarrow (\exists n)(n \in \mathbb{N} \land (\forall m)((m \in \mathbb{N} \land n \leq m) \rightarrow |f(m) - g(m)| < \varepsilon))).
$$

直观上说，$f \sim g$ 表示 $f$ 和 $g$ 对应的序列有相同的极限。

**定理 4.1.4** $B$ 上的关系 $\sim$ 是等价关系。

**定理 4.1.5** 设 $f: \mathbb{N} \rightarrow \mathbb{Q}$ 和 $g: \mathbb{N} \rightarrow \mathbb{Q}$ 都是常值函数，且 $f \sim g$，则 $f = g$。

**定义 4.1.9（实数）** 令 $\mathbb{R} = B/{\sim}$，即 $\mathbb{R}$ 是集合 $B$ 关于等价关系 $\sim$ 的商集，则称 $\mathbb{R}$ 的元素为实数，称 $\mathbb{R}$ 为实数集合。

由定理 4.1.5，不同的有理数 $r$ 对应的常值序列属于不同的等价类，因此可以把有理数看作特殊的实数。

**定义 4.1.10（基本函数的大小）** 在 $B$ 上定义小于关系 $<_B$：对任意的 $f, g \in B$，$f <_B g$ 当且仅当

$$
(\exists \varepsilon)(\varepsilon \in \mathbb{Q} \land \varepsilon > 0 \land (\exists n)(n \in \mathbb{N} \land (\forall m)((m \in \mathbb{N} \land n \leq m) \rightarrow g(m) - f(m) > \varepsilon))).
$$

并定义 $f \leq_B g$ 当且仅当 $f <_B g$ 或 $f \sim g$。

**定义 4.1.11（实数的大小）** 在 $\mathbb{R}$ 上定义小于等于关系 $\leq_{\mathbb{R}}$ 和小于关系 $<_{\mathbb{R}}$：对任意的 $f, g \in B$，

$$
\begin{aligned}
[f]_\sim \leq_{\mathbb{R}} [g]_\sim &\Leftrightarrow f \leq_B g, \\
[f]_\sim <_{\mathbb{R}} [g]_\sim &\Leftrightarrow f <_B g.
\end{aligned}
$$

## 4.2. 集合的等势

**定义 4.2.1（等势）** 对集合 $A$ 和 $B$，如果存在从 $A$ 到 $B$ 的双射函数，就称 $A$ 和 $B$ 等势，记作 $A \approx B$；否则称 $A$ 和 $B$ 不等势，记作 $A \not\approx B$。

**定理 4.2.1** 对任意的集合 $A$，有

$$
P(A) \approx {}^{A}2,
$$

其中 $2 = \{0, 1\}$，${}^{A}2$ 是从 $A$ 到 $\{0, 1\}$ 的所有函数的集合。

把每个子集 $B \subseteq A$ 对应到它的特征函数 $\chi_B$（定义 3.1.10），就得到 $P(A)$ 到 ${}^{A}2$ 的双射。

**定理 4.2.2** 对任意的集合 $A$、$B$ 和 $C$，

1. $A \approx A$；
2. 若 $A \approx B$，则 $B \approx A$；
3. 若 $A \approx B$ 且 $B \approx C$，则 $A \approx C$。

**定理 4.2.3（Cantor 定理）**

1. $\mathbb{N} \not\approx \mathbb{R}$；
2. 对任意的集合 $A$，$A \not\approx P(A)$。

**证明** (2) 设 $f: A \rightarrow P(A)$ 是任一函数，令

$$
D = \{x \mid x \in A \land x \notin f(x)\} \in P(A).
$$

若存在 $a \in A$ 使 $f(a) = D$，则 $a \in D \Leftrightarrow a \notin f(a) \Leftrightarrow a \notin D$，矛盾。所以 $D \notin \operatorname{ran}(f)$，$f$ 不是满射，更不是双射。

(1) 用对角线法：设 $f: \mathbb{N} \rightarrow \mathbb{R}$ 是任一函数。对每个 $n$，若 $f(n) \in [0, 1)$，把它写成十进制小数 $0.a_{n0}a_{n1}a_{n2}\cdots$（不以 $9$ 无限循环结尾，这样的写法唯一），否则令 $a_{nn} = 0$。令 $b_n = 5$（若 $a_{nn} \neq 5$），$b_n = 4$（若 $a_{nn} = 5$），则 $b = 0.b_0b_1b_2\cdots \in [0, 1)$。对每个 $n$，若 $f(n) \in [0, 1)$，则 $b$ 与 $f(n)$ 的第 $n$ 位小数不同（$b$ 的各位都不是 $0$ 或 $9$，其十进制写法也唯一），故 $b \neq f(n)$；若 $f(n) \notin [0, 1)$，显然 $b \neq f(n)$。所以 $b \notin \operatorname{ran}(f)$，$f$ 不是满射，从而 $\mathbb{N} \not\approx \mathbb{R}$。$\square$

## 4.3. 有限集合与无限集合

**定义 4.3.1（有限集合与无限集合）** 集合 $A$ 是有限集合，当且仅当存在 $n \in \mathbb{N}$，使 $n \approx A$。集合 $A$ 是无限集合，当且仅当 $A$ 不是有限集合，即不存在 $n \in \mathbb{N}$ 使 $n \approx A$。

这里的自然数 $n$ 按定义 1.7.4 就是集合 $\{0, 1, \cdots, n - 1\}$，因此与定义 1.6.2 一致。

**定理 4.3.1** 不存在与自己的真子集等势的自然数。

**推论 4.3.1** 不存在与自己的真子集等势的有限集合。

**推论 4.3.2** 任何与自己的真子集等势的集合是无限集合。$\mathbb{N}$ 和 $\mathbb{R}$ 都是无限集合。

例如 $f(n) = n + 1$ 是 $\mathbb{N}$ 到其真子集 $\mathbb{N} - \{0\}$ 的双射。

**推论 4.3.3** 任何有限集合只与唯一的自然数等势。

## 4.4. 集合的基数

**定义 4.4.1（基数）** 对任意的集合 $A$ 和 $B$，它们的基数分别用 $\operatorname{card}(A)$ 和 $\operatorname{card}(B)$ 表示，并且

$$
\operatorname{card}(A) = \operatorname{card}(B) \Leftrightarrow A \approx B.
$$

有时把 $\operatorname{card}(A)$ 记作 $|A|$ 或 $\#(A)$。对有限集合 $A$ 和 $n \in \mathbb{N}$，若 $A \approx n$，则 $\operatorname{card}(A) = n$。

自然数集合 $\mathbb{N}$ 的基数不是自然数，因为 $\mathbb{N}$ 不与任何自然数等势。通常沿用 Cantor 的记法，把 $\operatorname{card}(\mathbb{N})$ 记作 $\aleph_0$，读作"阿列夫零"。可以证明

$$
\operatorname{card}(\mathbb{Z}) = \operatorname{card}(\mathbb{Q}) = \operatorname{card}(\mathbb{N} \times \mathbb{N}) = \aleph_0.
$$

例如 $f(\langle m, n \rangle) = \dfrac{(m + n)(m + n + 1)}{2} + m$ 是 $\mathbb{N} \times \mathbb{N}$ 到 $\mathbb{N}$ 的双射（按 $m + n$ 的值逐条斜线编号）。

实数集合 $\mathbb{R}$ 的基数不是自然数，也不是 $\aleph_0$（因为 $\mathbb{N} \not\approx \mathbb{R}$）。通常把 $\operatorname{card}(\mathbb{R})$ 记作 $\aleph$（也记作 $\mathfrak{c}$），称为连续统的基数。可以证明

$$
\operatorname{card}([0, 1]) = \operatorname{card}((0, 1)) = \operatorname{card}(\mathbb{R}_+) = \aleph = 2^{\aleph_0}.
$$

有的教材把 $\operatorname{card}(\mathbb{R})$ 记作 $\aleph_1$；但 $\aleph_1$ 通常指大于 $\aleph_0$ 的最小基数，"$\operatorname{card}(\mathbb{R}) = \aleph_1$"正是 4.7 节的连续统假设，不能作为定义。

## 4.5. 基数的算术运算

**定义 4.5.1（基数的运算）** 对任意的基数 $k$ 和 $l$，取集合 $K$ 和 $L$ 使 $\operatorname{card}(K) = k$，$\operatorname{card}(L) = l$，定义

1. 若 $K \cap L = \emptyset$，则 $k + l = \operatorname{card}(K \cup L)$；
2. $k \cdot l = \operatorname{card}(K \times L)$；
3. $k^l = \operatorname{card}({}^{L}K)$，其中 ${}^{L}K$ 是从 $L$ 到 $K$ 的所有函数的集合。

这些定义与 $K$、$L$ 的选取无关；求和时总可以取到不相交的 $K$、$L$（例如用 $K \times \{0\}$ 和 $L \times \{1\}$ 代替）。由定理 4.2.1，$\operatorname{card}(P(A)) = 2^{\operatorname{card}(A)}$。

**定理 4.5.1** 对任意的基数 $k$、$l$ 和 $m$，

1. $k + l = l + k$，$k \cdot l = l \cdot k$；
2. $k + (l + m) = (k + l) + m$，$k \cdot (l \cdot m) = (k \cdot l) \cdot m$；
3. $k \cdot (l + m) = k \cdot l + k \cdot m$；
4. $k^{l + m} = k^l \cdot k^m$；
5. $(k \cdot l)^m = k^m \cdot l^m$；
6. $(k^l)^m = k^{l \cdot m}$。

## 4.6. 基数的比较

**定义 4.6.1（基数的大小）** 对集合 $K$ 和 $L$，$\operatorname{card}(K) = k$，$\operatorname{card}(L) = l$，如果存在从 $K$ 到 $L$ 的单射函数，则称集合 $L$ 优于 $K$，记作 $K \preceq L$，并称基数 $k$ 不大于基数 $l$，记作 $k \leq l$。

**定义 4.6.2** 对基数 $k$ 和 $l$，如果 $k \leq l$ 且 $k \neq l$，则称 $k$ 小于 $l$，记作 $k < l$。

由 Cantor 定理与定理 4.2.1，对任意的基数 $k$ 有 $k < 2^k$。

**定理 4.6.1** 对任意的基数 $k$、$l$ 和 $m$，

1. $k \leq k$；
2. 若 $k \leq l$ 且 $l \leq m$，则 $k \leq m$；
3. 若 $k \leq l$ 且 $l \leq k$，则 $k = l$；
4. $k \leq l$ 或 $l \leq k$。

第 3 条即 Schröder–Bernstein 定理：若存在 $K$ 到 $L$ 的单射和 $L$ 到 $K$ 的单射，则存在 $K$ 到 $L$ 的双射。它的证明不需要选择公理；第 4 条（基数的可比较性）则与选择公理等价。

**例 4.6.1** $\operatorname{card}((0, 1)) = \operatorname{card}([0, 1])$。$f(x) = x$ 是 $(0, 1)$ 到 $[0, 1]$ 的单射，$g(x) = \dfrac{x + 1}{3}$ 是 $[0, 1]$ 到 $[1/3, 2/3] \subseteq (0, 1)$ 的单射，由 Schröder–Bernstein 定理即得，无须直接构造双射。

**定理 4.6.2** 对任意的基数 $k$、$l$ 和 $m$，如果 $k \leq l$，则

1. $k + m \leq l + m$；
2. $k \cdot m \leq l \cdot m$；
3. $k^m \leq l^m$；
4. 若 $k \neq 0$ 或 $m \neq 0$，则 $m^k \leq m^l$。

第 4 条的条件不能去掉：$k = m = 0$，$l = 1$ 时，$m^k = 0^0 = 1$，而 $m^l = 0^1 = 0$。

**定理 4.6.3** 对基数 $k$ 和 $l$，如果 $k \leq l$，$k \neq 0$，$l$ 是无限基数，则

$$
k + l = k \cdot l = l = \max(k, l).
$$

**定理 4.6.4**

1. 对任意的无限集合 $K$，$\mathbb{N} \preceq K$；
2. 对任意的无限基数 $k$，$\aleph_0 \leq k$。

即 $\aleph_0$ 是最小的无限基数。

## 4.7. 可数集合与连续统假设

**定义 4.7.1（可数集合）** 对集合 $K$，如果 $\operatorname{card}(K) \leq \aleph_0$，则称 $K$ 是可数集合。

可数集合包括有限集合和基数为 $\aleph_0$ 的集合；后者又称可数无限集合，它们的元素可以排成一个无穷序列 $a_0, a_1, a_2, \cdots$。

**定理 4.7.1（可数集的性质）**

1. 可数集的任何子集是可数集；
2. 两个可数集的并集和笛卡儿积是可数集；
3. 若 $K$ 是无限集合，则 $P(K)$ 是不可数的；
4. 可数个可数集的并集是可数集，即：若 $A$ 是可数集，$A$ 的元素都是可数集，则 $\bigcup A$ 是可数集。

第 4 条的证明需要为每个元素集合选定一个枚举，要用到选择公理。

常见的几个基数按从小到大的次序排列为

$$
0 < 1 < \cdots < n < \cdots < \aleph_0 < \aleph < 2^{\aleph} < \cdots.
$$

**连续统假设** 不存在基数 $k$，使

$$
\aleph_0 < k < 2^{\aleph_0}.
$$

等价地说，$2^{\aleph_0} = \aleph_1$，即 $\mathbb{R}$ 的每个无限子集或者与 $\mathbb{N}$ 等势，或者与 $\mathbb{R}$ 等势。Gödel（1940）证明了在 ZFC 中不能否定连续统假设，Cohen（1963）证明了在 ZFC 中也不能证明它：根据现有的公理系统，既不能证明它是对的，也不能证明它是错的。
