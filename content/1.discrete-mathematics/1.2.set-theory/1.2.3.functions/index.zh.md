---
title: 函数
---

函数是一类特殊的**二元关系**：定义域中的每个元素恰好对应值域中的一个元素。本章在上一章关系理论的基础上定义函数及单射、满射、双射，讨论函数的合成与逆、函数的相容性，再用函数的语言介绍实数集上的开集与闭集，最后由特征函数引出模糊子集。双射是下一章比较集合大小（等势与基数）的基本工具。

## 3.1. 函数和选择公理

**定义 3.1.1（函数）** 对集合 $A$ 到集合 $B$ 的关系 $f$，若满足下列条件：

1. 对任意的 $x \in \operatorname{dom}(f)$，存在唯一的 $y \in \operatorname{ran}(f)$，使 $xfy$ 成立；
2. $\operatorname{dom}(f) = A$，

则称 $f$ 为从 $A$ 到 $B$ 的函数，或称 $f$ 把 $A$ 映射到 $B$（有的书中也称为全函数、映射或变换），记作 $f\colon A \rightarrow B$。这时若 $xfy$，则记作 $f\colon x \mapsto y$ 或 $f(x) = y$。

函数的两个条件可以写成

$$
\begin{aligned}
& (\forall x)(\forall y_1)(\forall y_2)((xfy_1 \land xfy_2) \rightarrow y_1 = y_2), \\
& (\forall x)(x \in A \rightarrow (\exists y)(y \in B \land xfy)).
\end{aligned}
$$

**定义 3.1.2（从 $A$ 到 $B$ 的函数的集合）** 对集合 $A$ 和 $B$，从 $A$ 到 $B$ 的所有函数组成的集合记作 ${}^{A}B$（有的书记作 $B^A$），即

$$
{}^{A}B = \{f \mid f\colon A \rightarrow B\}.
$$

若 $A$ 和 $B$ 是有限集合，$|A| = m$，$|B| = n$，则 $|{}^{A}B| = n^m$。

**定义 3.1.3（象与完全原象）** 设 $f\colon A \rightarrow B$，$A_1 \subseteq A$，$B_1 \subseteq B$。$A_1$ 在 $f$ 下的**象** $f[A_1]$ 与 $B_1$ 在 $f$ 下的**完全原象** $f^{-1}[B_1]$ 分别定义为

$$
\begin{aligned}
f[A_1] &= \{y \mid (\exists x)(x \in A_1 \land y = f(x))\}, \\
f^{-1}[B_1] &= \{x \mid x \in A \land f(x) \in B_1\}.
\end{aligned}
$$

$f[A]$ 称为函数 $f$ 的象。

**定义 3.1.4（满射、单射、双射）** 设 $f\colon A \rightarrow B$，

1. 若 $\operatorname{ran}(f) = B$，则称 $f$ 是**满射**（surjection）的，或称 $f$ 是 $A$ 到 $B$ 上的；
2. 若对任意的 $x_1, x_2 \in A$，$x_1 \neq x_2$，都有 $f(x_1) \neq f(x_2)$，则称 $f$ 是**单射**（injection）的，或内射的、一对一的；
3. 若 $f$ 既是满射的又是单射的，则称 $f$ 是**双射**（bijection）的，或一对一 $A$ 到 $B$ 上的，简称双射。

**例 3.1.1** 设 $f, g, h\colon \mathbb{N} \rightarrow \mathbb{N}$，$f(n) = 2n$，$g(n) = \lfloor n/2 \rfloor$，$h(n) = n + (-1)^n$（即交换 $0$ 与 $1$、$2$ 与 $3$……）。则 $f$ 是单射但不是满射（奇数不在值域中）；$g$ 是满射但不是单射（$g(0) = g(1) = 0$）；$h$ 是双射。

**定义 3.1.5（常函数）** 设 $f\colon A \rightarrow B$。如果存在 $y \in B$，使得对所有的 $x \in A$，有 $f(x) = y$，即 $f[A] = \{y\}$，则称 $f$ 为**常函数**。

**定义 3.1.6（恒等函数）** $A$ 上的恒等关系 $I_A\colon A \rightarrow A$ 称为**恒等函数**。对任意的 $x \in A$，有 $I_A(x) = x$。

**定义 3.1.7（单调函数）** 设 $f\colon \mathbb{R} \rightarrow \mathbb{R}$。如果对任意的 $x, y \in \mathbb{R}$，$x \leq y \rightarrow f(x) \leq f(y)$，则称 $f$ 为**单调递增**的；如果 $x < y \rightarrow f(x) < f(y)$，则称 $f$ 为**严格单调递增**的。类似可定义单调递减和严格单调递减的函数。

**定义 3.1.8（$n$ 元运算）** 对集合 $A$ 和 $n \in \mathbb{N}$，函数 $f\colon A^n \rightarrow A$ 称为 $A$ 上的 **$n$ 元运算**，其中 $A^n$ 是 $A$ 的 $n$ 阶笛卡儿积。

**定义 3.1.9（泛函）** 设 $A, B, C$ 是集合，${}^{B}C$ 为从 $B$ 到 $C$ 的所有函数的集合，则 $F\colon A \rightarrow {}^{B}C$ 称为一个**泛函**（有时也将 $G\colon {}^{B}C \rightarrow A$ 称为一个泛函）。

**定义 3.1.10（集合的特征函数）** 设 $E$ 是全集，对任意的 $A \subseteq E$，$A$ 的**特征函数** $\chi_A$ 定义为

$$
\chi_A\colon E \rightarrow \{0, 1\}, \qquad \chi_A(a) =
\begin{cases}
1, & a \in A, \\
0, & a \notin A.
\end{cases}
$$

**定义 3.1.11（典型映射）** 设 $R$ 是 $A$ 上的等价关系，令 $g\colon A \rightarrow A/R$，$g(a) = [a]_R$，则称 $g$ 为从 $A$ 到商集 $A/R$ 的**典型映射**或自然映射。

**选择公理**（形式 1）对任意的关系 $R$，存在函数 $f$，使得

$$
f \subseteq R \quad \text{且} \quad \operatorname{dom}(f) = \operatorname{dom}(R).
$$

这就是 **ZF 公理系统**中的第 10 条公理（见 [1.7 节](/1.2.1#sec-1.7)）。直观地说：对 $\operatorname{dom}(R)$ 中的每个 $x$，可以从 $\{y \mid xRy\}$ 中同时"选出"一个 $f(x)$。

## 3.2. 函数的合成与函数的逆

函数的合成就是关系的合成（定义 2.3.1），函数的逆就是关系的逆。

**定理 3.2.1（函数的合成）** 设 $g\colon A \rightarrow B$，$f\colon B \rightarrow C$，则

1. $f \circ g$ 是函数 $f \circ g\colon A \rightarrow C$；
2. 对任意的 $x \in A$，有 $(f \circ g)(x) = f(g(x))$。

**定理 3.2.2（函数合成的性质 1）** 设 $g\colon A \rightarrow B$，$f\colon B \rightarrow C$，

1. 若 $f, g$ 是满射的，则 $f \circ g$ 是满射的；
2. 若 $f, g$ 是单射的，则 $f \circ g$ 是单射的；
3. 若 $f, g$ 是双射的，则 $f \circ g$ 是双射的。

**定理 3.2.3（函数合成的性质 2）** 设 $g\colon A \rightarrow B$，$f\colon B \rightarrow C$，

1. 若 $f \circ g$ 是满射的，则 $f$ 是满射的；
2. 若 $f \circ g$ 是单射的，则 $g$ 是单射的；
3. 若 $f \circ g$ 是双射的，则 $f$ 是满射的，$g$ 是单射的。

**证明** (1) 对任意 $z \in C$，由 $f \circ g$ 满射，存在 $x \in A$ 使 $f(g(x)) = z$，于是 $g(x) \in B$ 是 $z$ 在 $f$ 下的原象，故 $f$ 是满射的。(2) 若 $g(x_1) = g(x_2)$，则 $(f \circ g)(x_1) = (f \circ g)(x_2)$，由 $f \circ g$ 单射得 $x_1 = x_2$，故 $g$ 是单射的。(3) 由 (1)(2) 即得。$\square$

结论不能加强：取 $A = C = \{0\}$，$B = \{0, 1\}$，$g(0) = 0$，$f(0) = f(1) = 0$，则 $f \circ g = I_{\{0\}}$ 是双射，但 $f$ 不是单射，$g$ 不是满射。

**定理 3.2.4** 设 $f\colon A \rightarrow B$，则 $f = f \circ I_A = I_B \circ f$。

**定理 3.2.5（函数的逆）** 若 $f\colon A \rightarrow B$ 是双射的，则 $f^{-1}$ 是函数 $f^{-1}\colon B \rightarrow A$。

**定义 3.2.1（反函数）** 设 $f\colon A \rightarrow B$ 是双射的，则称 $f^{-1}\colon B \rightarrow A$ 为 $f$ 的反函数。

**定理 3.2.6** 若 $f\colon A \rightarrow B$ 是双射的，则 $f^{-1}\colon B \rightarrow A$ 是双射的。

**定理 3.2.7** 若 $f\colon A \rightarrow B$ 是双射的，则对任意的 $x \in A$，有 $f^{-1}(f(x)) = x$；对任意的 $y \in B$，有 $f(f^{-1}(y)) = y$。即 $f^{-1} \circ f = I_A$，$f \circ f^{-1} = I_B$。

**定义 3.2.2（左逆和右逆）** 设 $f\colon A \rightarrow B$，$g\colon B \rightarrow A$。如果 $g \circ f = I_A$，则称 $g$ 为 $f$ 的**左逆**；如果 $f \circ g = I_B$，则称 $g$ 为 $f$ 的**右逆**。

**定理 3.2.8** 设 $f\colon A \rightarrow B$，$A \neq \varnothing$，则

1. $f$ 存在左逆，当且仅当 $f$ 是单射的；
2. $f$ 存在右逆，当且仅当 $f$ 是满射的；
3. $f$ 既存在左逆又存在右逆，当且仅当 $f$ 是双射的；
4. 若 $f$ 是双射的，则 $f$ 的左逆等于右逆（都等于 $f^{-1}$）。

由定理 3.2.3 立即得到 (1)(2) 的必要性。(1) 的充分性：取定 $a_0 \in A$，令 $g(y) = f^{-1}(y)$（$y \in \operatorname{ran}(f)$，由单射性唯一确定），$g(y) = a_0$（$y \notin \operatorname{ran}(f)$），这里用到 $A \neq \varnothing$。(2) 的充分性要对每个 $y \in B$ 从非空集合 $f^{-1}[\{y\}]$ 中选一个元素作为 $g(y)$，需要用**选择公理**。(4)：若 $g$ 是左逆、$h$ 是右逆，则 $g = g \circ I_B = g \circ (f \circ h) = (g \circ f) \circ h = I_A \circ h = h$。

## 3.3. 函数的性质

**定义 3.3.1（函数的相容性）** 设 $f\colon A \rightarrow B$，$g\colon C \rightarrow D$，如果对任意的 $x \in A \cap C$，都有 $f(x) = g(x)$，就说 $f$ 和 $g$ 是**相容**的。

**定义 3.3.2（函数集的相容性）** 设 $\mathcal{C}$ 是由一些函数组成的集合，如果 $\mathcal{C}$ 中任意两个函数都是相容的，就说 $\mathcal{C}$ 是相容的。

**定理 3.3.1** 设 $f\colon A \rightarrow B$，$g\colon C \rightarrow D$，则 $f$ 和 $g$ 是相容的当且仅当 $f \cup g$ 是函数。

**定理 3.3.2** 设 $f\colon A \rightarrow B$，$g\colon C \rightarrow D$，则 $f$ 与 $g$ 是相容的当且仅当

$$
f \upharpoonright (A \cap C) = g \upharpoonright (A \cap C).
$$

**定理 3.3.3** 对函数的集合 $\mathcal{C}$，若 $\mathcal{C}$ 是相容的，且 $F = \bigcup \mathcal{C}$，则 $F$ 是函数 $F\colon \operatorname{dom}(F) \rightarrow \operatorname{ran}(F)$，并且

$$
\operatorname{dom}(F) = \textstyle\bigcup \{\operatorname{dom}(f) \mid f \in \mathcal{C}\}.
$$

**定义 3.3.3（关系与函数的相容性）** 设 $R$ 是 $A$ 上的等价关系，$f\colon A \rightarrow A$。如果对任意的 $x, y \in A$，有 $\langle x, y \rangle \in R \Rightarrow \langle f(x), f(y) \rangle \in R$，则称关系 $R$ 与函数 $f$ 是相容的。

**定理 3.3.4** 设 $R$ 是 $A$ 上的等价关系，$f\colon A \rightarrow A$。如果 $R$ 与 $f$ 是相容的，则存在唯一的函数 $F\colon A/R \rightarrow A/R$，使 $F([x]_R) = [f(x)]_R$；如果 $R$ 与 $f$ 不相容，则不存在这样的函数 $F$。

相容性保证了 $F$ 的定义与代表元的选取无关。例如在 $\mathbb{Z}$ 上取模 $3$ 同余关系 $R$：$f(x) = x + 1$ 与 $R$ 相容，诱导出 $F([x]) = [x + 1]$；而 $f(x) = \lfloor x/2 \rfloor$ 与 $R$ 不相容，因为 $0 R 3$，但 $f(0) = 0$ 与 $f(3) = 1$ 不同余。

## 3.4. 开集与闭集

**定义 3.4.1（距离）** 对实数集 $\mathbb{R}$，定义 $\rho\colon \mathbb{R} \times \mathbb{R} \rightarrow \mathbb{R}$ 为 $\rho(\langle x, y \rangle) = |x - y|$，其中 $|x - y|$ 是 $x - y$ 的绝对值，称 $\rho$ 为 $\mathbb{R}$ 上的**距离函数**。对任意 $\langle x, y \rangle \in \mathbb{R} \times \mathbb{R}$，$\rho(\langle x, y \rangle)$ 称为 $x$ 和 $y$ 的距离，也写作 $\rho(x, y) = |x - y|$。

**定义 3.4.2（邻域）** 设 $x_0 \in \mathbb{R}$，$\varepsilon \in \mathbb{R}$ 且 $\varepsilon > 0$。$x_0$ 的 **$\varepsilon$ 邻域**是集合

$$
\{x \mid x \in \mathbb{R} \land \rho(x_0, x) < \varepsilon\}.
$$

**定义 3.4.3（极限点）** 设 $A \subseteq \mathbb{R}$，$x_0 \in \mathbb{R}$。如果在 $x_0$ 的任一 $\varepsilon$ 邻域中都存在不等于 $x_0$ 的 $A$ 的元素，则称 $x_0$ 是 $A$ 的一个**极限点**（或凝聚点）。定义的条件可以写成

$$
(\forall \varepsilon)((\varepsilon \in \mathbb{R} \land \varepsilon > 0) \rightarrow (\exists x)(x \in A \land x \neq x_0 \land \rho(x, x_0) < \varepsilon)).
$$

**定理 3.4.1** 设 $A \subseteq \mathbb{R}$，$x_0 \in \mathbb{R}$，则 $x_0$ 是 $A$ 的极限点，当且仅当在 $A$ 中存在两两不同且都不等于 $x_0$ 的点列 $\{x_n\}$（即 $x_n \in A$，$x_n \neq x_0$，$m \neq n \rightarrow x_m \neq x_n$），使得 $\lim_{n \to \infty} x_n = x_0$。

**定理 3.4.2** 若 $A \subseteq \mathbb{R}$ 是有界无限集，则 $A$ 具有极限点。

**定义 3.4.4（孤立点）** 设 $A \subseteq \mathbb{R}$，$x_0 \in A$。若 $x_0$ 不是 $A$ 的极限点，则称 $x_0$ 为 $A$ 的**孤立点**。

**定义 3.4.5（导集与闭集）** 设 $A \subseteq \mathbb{R}$，$A$ 的所有极限点组成的集合称为 $A$ 的**导集**，记作 $A'$。如果 $A' \subseteq A$，则称 $A$ 为**闭集**。

**定理 3.4.3** 设 $A \subseteq \mathbb{R}$，则 $A'$ 是闭集，即 $(A')' \subseteq A'$。

**定理 3.4.4** 任意个闭集的交集是闭集，有限个闭集的并集是闭集。

**定义 3.4.6（内点）** 设 $A \subseteq \mathbb{R}$，$x_0 \in \mathbb{R}$。如果存在 $x_0$ 的某个 $\varepsilon$ 邻域，其中全是 $A$ 的元素，则称 $x_0$ 为 $A$ 的一个**内点**。定义的条件可以写成

$$
(\exists \varepsilon)(\varepsilon \in \mathbb{R} \land \varepsilon > 0 \land (\forall x)((x \in \mathbb{R} \land \rho(x, x_0) < \varepsilon) \rightarrow x \in A)).
$$

**定义 3.4.7（开集）** 设 $A \subseteq \mathbb{R}$，若 $A$ 的元素都是 $A$ 的内点，则称 $A$ 为**开集**。

**定理 3.4.5** 任意个开集的并集是开集，有限个开集的交集是开集。

"有限个"不能去掉：开集 $(-1/n, 1/n)$（$n = 1, 2, \cdots$）的交集是 $\{0\}$，不是开集；闭集 $[1/n, 1]$ 的并集是 $(0, 1]$，不是闭集。

**定理 3.4.6** 设 $A \subseteq \mathbb{R}$，

1. 若 $A$ 是开集，则 $\mathbb{R} - A$ 是闭集；
2. 若 $A$ 是闭集，则 $\mathbb{R} - A$ 是开集。

## 3.5. 模糊子集

**定理 3.5.1（特征函数的性质）** 设 $E$ 是**论域**（全集），$A \subseteq E$，$B \subseteq E$，$+$、$-$、$\cdot$ 是算术加、减、乘法，$A^{\mathsf c} = E - A$ 是 $A$ 的绝对补集，则（第 5–8 条对任意的 $x \in E$ 成立）：

1. $(\forall x)(\chi_A(x) = 0) \Leftrightarrow A = \varnothing$；
2. $(\forall x)(\chi_A(x) = 1) \Leftrightarrow A = E$；
3. $(\forall x)(\chi_A(x) \leq \chi_B(x)) \Leftrightarrow A \subseteq B$；
4. $(\forall x)(\chi_A(x) = \chi_B(x)) \Leftrightarrow A = B$；
5. $\chi_{A \cap B}(x) = \chi_A(x) \cdot \chi_B(x)$；
6. $\chi_{A \cup B}(x) = \chi_A(x) + \chi_B(x) - \chi_{A \cap B}(x)$；
7. $\chi_{A - B}(x) = \chi_A(x) - \chi_{A \cap B}(x)$；
8. $\chi_{A^{\mathsf c}}(x) = 1 - \chi_A(x)$。

普通子集由取值于 $\{0, 1\}$ 的特征函数完全确定。把取值范围放宽到区间 $[0, 1]$，就得到模糊子集。

**定义 3.5.1（模糊子集与隶属函数）** 设 $E$ 是论域，$E$ 上的一个**模糊子集** $A$ 是指：给定一个函数 $\mu_A\colon E \rightarrow [0, 1]$，$\mu_A(x)$ 表示 $x$ 属于 $A$ 的程度，称 $\mu_A$ 为 $A$ 的**隶属函数**。$E$ 上所有模糊子集组成的集合记作 $F(E)$。

**定义 3.5.2（模糊子集的运算）** 设 $E$ 是全集，$A, B \in F(E)$，$A \cup B$、$A \cap B$、$A^{\mathsf c}$ 分别是具有下列隶属函数的模糊子集，依次称为 $A$ 与 $B$ 的并集、交集和 $A$ 的绝对补集：

$$
\begin{aligned}
\mu_{A \cup B}(x) &= \max(\mu_A(x), \mu_B(x)), \\
\mu_{A \cap B}(x) &= \min(\mu_A(x), \mu_B(x)), \\
\mu_{A^{\mathsf c}}(x) &= 1 - \mu_A(x).
\end{aligned}
$$

**定义 3.5.3（截集）** 设 $E$ 是全集，$A \in F(E)$，$\lambda \in [0, 1]$。$A$ 的 **$\lambda$ 截集** $(A)_\lambda$（也写作 $A_\lambda$）定义为

$$
(A)_\lambda = \{x \mid x \in E \land \mu_A(x) \geq \lambda\}.
$$

它是 $E$ 的普通子集。

**定理 3.5.2** 设 $E$ 是全集，$A, B \in F(E)$，$\lambda \in [0, 1]$，则

1. $(A \cup B)_\lambda = A_\lambda \cup B_\lambda$；
2. $(A \cap B)_\lambda = A_\lambda \cap B_\lambda$。

**定理 3.5.3** 设 $E$ 是全集，$A \in F(E)$，$\lambda, \sigma \in [0, 1]$，则

1. $\lambda \leq \sigma \Rightarrow A_\sigma \subseteq A_\lambda$；
2. $A_0 = E$。

**定理 3.5.4（分解定理）** 设 $E$ 是全集，$A \in F(E)$，$\chi_{A_\lambda}$ 是截集 $A_\lambda$ 的特征函数，则对任意的 $u \in E$，

$$
\mu_A(u) = \sup_{\lambda \in [0, 1]} \min(\lambda, \chi_{A_\lambda}(u)),
$$

其中 $\sup$ 表示**上确界**。

事实上，当 $\lambda \leq \mu_A(u)$ 时 $u \in A_\lambda$，$\min(\lambda, \chi_{A_\lambda}(u)) = \lambda$；当 $\lambda > \mu_A(u)$ 时该值为 $0$。所以右端等于 $\sup\{\lambda \mid \lambda \leq \mu_A(u)\} = \mu_A(u)$。分解定理说明模糊子集由它的全体截集确定。

**定义 3.5.4（支集、核、边界、正规模糊集）** 设 $E$ 是全集，$A \in F(E)$。集合 $\operatorname{supp} A = \{u \mid u \in E \land \mu_A(u) > 0\}$ 称为 $A$ 的**支集**，截集 $A_1$ 称为 $A$ 的核，$(\operatorname{supp} A) - A_1$ 称为 $A$ 的边界。若 $A_1 \neq \varnothing$，就称 $A$ 为**正规模糊集**；若 $A_1 = \varnothing$，就称 $A$ 为非正规模糊集。

核 $A_1$ 的元素完全隶属于 $A$，边界上的元素则部分隶属于 $A$。
