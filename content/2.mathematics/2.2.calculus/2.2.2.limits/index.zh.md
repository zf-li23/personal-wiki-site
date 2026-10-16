---
title: 极限论
---

极限是微积分的基本语言：导数是差商的极限，定积分是和式的极限，级数的和是部分和的极限。本章先讨论最简单的情形——数列的极限，用 $\varepsilon$-$N$ 语言把"无限接近"说精确，建立极限的性质、四则运算和几个存在定理（夹逼定理、单调收敛定理、Cauchy 收敛准则）；再把这些结果推广到函数的六种极限过程，证明两个重要极限；最后用无穷小量的阶比较极限过程的快慢，得到求极限最常用的等价无穷小替换。

本章依赖[第 1 章](/2.2.1)的**确界存在定理**（单调收敛定理由它推出）和**去心邻域**。Cauchy 收敛准则充分性的证明要用到列紧性定理，放在[第 3 章](/2.2.3#sec-3.2)。概率论中各种随机变量序列的收敛（[3.1](/3.1)）都建立在本章的数列极限之上。

## 2.1. 数列极限的定义与性质

### 2.1.1. 数列极限的定义

**定义 2.1.1（数列）** 按正整数顺序排列的一列数 $a_1, a_2, \dots, a_n, \dots$ 称为**数列**，简记为 $\{a_n\}$，$a_n$ 称为通项。数列可以看作定义在 $\mathbb{N}_+$ 上的函数 $f(n) = a_n$。

观察几个数列当 $n$ 增大时的变化趋势：

$$
a_n = \frac{(-1)^n}{n}, \qquad b_n = \frac{n - 1}{n}, \qquad c_n = 2^n, \qquad d_n = \frac{(-1)^{n+1}}{\sqrt n}.
$$
$a_n, d_n$ 无限接近 $0$，$b_n$ 无限接近 $1$，$c_n$ 越来越大。"无限接近"不能理解为"越来越近"：$a_n$ 与 $0$ 的距离单调减小，而 $d_n$ 一会儿在 $0$ 的左边、一会儿在右边，但总趋势仍是无限接近 $0$。"$a_n$ 无限接近 $A$"的确切含义是：距离 $|a_n - A|$ 可以任意小，要多小有多小——无论给定多小的正数 $\varepsilon$（比如万分之一），从某一项以后，所有的项与 $A$ 的距离都小于 $\varepsilon$。

**定义 2.1.2（数列极限）** 设 $\{a_n\}$ 为数列，$A$ 为常数。如果对任意 $\varepsilon > 0$，都存在 $N \in \mathbb{N}_+$，使得当 $n > N$ 时都有

$$
|a_n - A| < \varepsilon,
$$
则称 $A$ 为数列 $\{a_n\}$ 的极限，记为 $\lim\limits_{n \to \infty} a_n = A$ 或 $a_n \to A$（$n \to \infty$），并称数列 $\{a_n\}$ 收敛于 $A$。没有极限的数列称为**发散数列**。

- $\varepsilon$ 是任意给定的，$N$ 依赖于 $\varepsilon$，但不唯一：找到一个满足要求的 $N$ 就够了，任何更大的 $N$ 也满足要求。
- 几何意义：无论 $\varepsilon > 0$ 多么小，从第 $N + 1$ 项起所有的项都落在邻域 $N(A, \varepsilon)$ 内，邻域外只有有限多项。
- 与"聚点"的区别：$A$ 的每个邻域都含有数列的无穷多项，并不足以保证 $a_n \to A$。例如 $(-1)^n$ 的子列分别趋于 $1$ 与 $-1$，$\pm1$ 的每个邻域都含有无穷多项，但数列发散。极限的要求是邻域外只有有限多项。
- 定义中的 $\varepsilon > 0$ 可以只取 $(0, 1)$ 中的值，$|a_n - A| < \varepsilon$ 可以换成 $|a_n - A| < M\varepsilon$（$M$ 为正常数）或 $|a_n - A| \leq \varepsilon$，$n > N$ 可以换成 $n \geq N$：这些改写都与原定义等价。

![ε-N 定义的几何意义：数列 a_n = 1 + (-1)^n/n 在 n > N 后全部落在带 (1 − ε, 1 + ε) 内；ε 越小，所需的 N 越大](./plots/epsilon-n-band.py)

**算法 2.1.1（用定义验证数列极限）** 验证 $\lim\limits_{n \to \infty} a_n = A$：

1. 任给 $\varepsilon > 0$，对 $|a_n - A|$ 作恒等变形并适当放大，得到一个形式简单、随 $n$ 单调减小且趋于 $0$ 的上界 $g(n)$，即 $|a_n - A| \leq g(n)$（放大时可以先假设 $n$ 大于某个固定数）；
2. 解不等式 $g(n) < \varepsilon$，得到充分条件 $n > X(\varepsilon)$；
3. 取 $N = \lfloor X \rfloor$（或任意更大的正整数），则当 $n > N$ 时 $|a_n - A| \leq g(n) < \varepsilon$。

找 $N$ 不等于解不等式 $|a_n - A| < \varepsilon$：只需要一个充分条件，放大正是为了让不等式容易解。

**例 2.1.1** 证明 $\lim\limits_{n \to \infty} \frac{2n + 1}{n + 1} = 2$，$\lim\limits_{n \to \infty} \frac{2n^2 + 1}{n^2 + 2n - 1} = 2$。

**证明** 第一式：$\left|\frac{2n+1}{n+1} - 2\right| = \frac{1}{n+1} < \frac1n$。任给 $\varepsilon > 0$，取 $N = \left\lfloor \frac1\varepsilon \right\rfloor$，当 $n > N$ 时 $\frac1n < \varepsilon$。第二式：$n \geq 1$ 时 $n^2 + 2n - 1 \geq n^2$，故

$$
\left|\frac{2n^2 + 1}{n^2 + 2n - 1} - 2\right| = \frac{4n - 3}{n^2 + 2n - 1} < \frac{4n}{n^2} = \frac4n,
$$
取 $N = \left\lfloor \frac4\varepsilon \right\rfloor$ 即可。$\square$

**例 2.1.2** 证明 $\lim\limits_{n \to \infty} q^n = 0$（$|q| < 1$）。

**证明** $q = 0$ 时显然。设 $0 < |q| < 1$，任给 $\varepsilon \in (0, 1)$，$|q^n - 0| = |q|^n < \varepsilon \iff n\ln|q| < \ln\varepsilon \iff n > \frac{\ln\varepsilon}{\ln|q|}$（注意 $\ln|q| < 0$）。取 $N = \left\lfloor \frac{\ln\varepsilon}{\ln|q|} \right\rfloor$ 即可。$\square$

**例 2.1.3** 设 $a > 1$，证明 $\lim\limits_{n \to \infty} \sqrt[n]{a} = 1$。

**证明** 由 $a - 1 = \bigl(\sqrt[n]a - 1\bigr)\bigl(1 + a^{1/n} + a^{2/n} + \cdots + a^{(n-1)/n}\bigr)$，右边括号中每一项都 $\geq 1$，故

$$
0 < \sqrt[n]a - 1 \leq \frac{a - 1}{n}.
$$
任给 $\varepsilon > 0$，取 $N = \left\lfloor \frac{a - 1}{\varepsilon} \right\rfloor$ 即可。$0 < a < 1$ 时对 $\frac1a$ 用此结论并取倒数（四则运算见 §2.2.1）。$\square$

**例 2.1.4** 证明 $\lim\limits_{n \to \infty} \sqrt[n]{n} = 1$。

**证明** 记 $\sqrt[n]n = 1 + t_n$，$t_n \geq 0$。由二项式定理，$n \geq 2$ 时

$$
n = (1 + t_n)^n \geq \binom n2 t_n^2 = \frac{n(n-1)}{2}t_n^2, \quad\text{故}\quad 0 \leq t_n \leq \sqrt{\frac{2}{n - 1}}.
$$
任给 $\varepsilon > 0$，要 $\sqrt{\frac2{n-1}} < \varepsilon$，只要 $n > \frac2{\varepsilon^2} + 1$，取 $N = \left\lfloor \frac2{\varepsilon^2} \right\rfloor + 1$ 即可。$\square$

**例 2.1.5** 设 $a > 1$，证明 $\lim\limits_{n \to \infty} \frac{n}{a^n} = 0$。

**证明** 记 $a = 1 + b$，$b > 0$。$n \geq 2$ 时 $a^n \geq \binom n2 b^2$，故 $0 < \frac{n}{a^n} \leq \frac{2}{(n - 1)b^2}$，取 $N = \left\lfloor \frac{2}{\varepsilon b^2} \right\rfloor + 1$ 即可。$\square$

用同样的方法（展开到 $b^{k+1}$ 项）可证 $\lim\limits_{n \to \infty} \frac{n^k}{a^n} = 0$（$a > 1$，$k \in \mathbb{N}_+$）：指数增长快于任何多项式增长。例 2.1.2–例 2.1.5 是最常用的四个基本极限：

$$
\lim_{n \to \infty} q^n = 0 \ (|q| < 1), \qquad \lim_{n \to \infty} \sqrt[n]a = 1 \ (a > 0), \qquad \lim_{n \to \infty} \sqrt[n]n = 1, \qquad \lim_{n \to \infty} \frac{n^k}{a^n} = 0 \ (a > 1).
$$

**例 2.1.6** 证明 $\lim\limits_{n \to \infty} \arctan n = \frac\pi2$。

**证明** 任给 $\varepsilon \in (0, 1)$。$\left|\arctan n - \frac\pi2\right| = \frac\pi2 - \arctan n < \varepsilon$ 等价于 $\tan\left(\frac\pi2 - \arctan n\right) < \tan\varepsilon$，即 $\cot(\arctan n) = \frac1n < \tan\varepsilon$。取 $N = \left\lfloor \frac1{\tan\varepsilon} \right\rfloor$ 即可。$\square$

同理 $\lim\limits_{n \to \infty} \arctan(-n) = -\frac\pi2$，$\lim\limits_{n \to \infty} \operatorname{arccot} n = 0$，$\lim\limits_{n \to \infty} \operatorname{arccot}(-n) = \pi$。

直接由定义可以得到下面的等价关系，它们把一般的极限问题化为"趋于 $0$"的问题：

$$
\lim_{n \to \infty} a_n = 0 \iff \lim_{n \to \infty} |a_n| = 0; \qquad
\lim_{n \to \infty} a_n = A \iff \lim_{n \to \infty} (a_n - A) = 0 \iff \lim_{n \to \infty} |a_n - A| = 0.
$$

**例 2.1.7** 若 $\lim\limits_{n \to \infty} a_n = A$，则 $\lim\limits_{n \to \infty} \frac{a_1 + a_2 + \cdots + a_n}{n} = A$。

**证明** 令 $b_n = a_n - A$，则 $b_n \to 0$，且 $\frac{a_1 + \cdots + a_n}{n} - A = \frac{b_1 + \cdots + b_n}{n}$，只需对 $A = 0$ 证明。任给 $\varepsilon > 0$，存在 $N_1$，当 $n > N_1$ 时 $|b_n| < \varepsilon$。于是 $n > N_1$ 时

$$
\left|\frac{b_1 + \cdots + b_n}{n}\right| \leq \frac{|b_1 + \cdots + b_{N_1}|}{n} + \frac{n - N_1}{n}\varepsilon < \frac{|b_1 + \cdots + b_{N_1}|}{n} + \varepsilon.
$$
$N_1$ 固定后第一项的分子是常数，存在 $N_2$ 使 $n > N_2$ 时第一项小于 $\varepsilon$。取 $N = \max\{N_1, N_2\}$，$n > N$ 时上式小于 $2\varepsilon$。$\square$

这个证明的"分段估计"是常用技巧：前有限项用"分子固定、分母趋于无穷"控制，后面的项用极限的定义控制。逆命题不成立：$a_n = (-1)^n$ 发散，而其算术平均趋于 $0$。

### 2.1.2. 数列极限的性质

**定理 2.1.1（唯一性）** 收敛数列的极限是唯一的。

**证明** 设 $a_n \to A$，$a_n \to B$，且 $A \ne B$。取 $\varepsilon = \frac12|A - B| > 0$，存在 $N_1, N_2$，使 $n > N_1$ 时 $|a_n - A| < \varepsilon$，$n > N_2$ 时 $|a_n - B| < \varepsilon$。取 $n > \max\{N_1, N_2\}$，则

$$
|A - B| \leq |a_n - A| + |a_n - B| < 2\varepsilon = |A - B|,
$$
矛盾。$\square$

**定理 2.1.2（有界性）** 收敛数列是有界的：若 $\lim\limits_{n \to \infty} a_n = A$，则存在 $M > 0$，使得 $|a_n| \leq M$ 对所有 $n \in \mathbb{N}_+$ 成立。

**证明** 对 $\varepsilon = 1$，存在 $N$，当 $n > N$ 时 $|a_n - A| < 1$，从而 $|a_n| < |A| + 1$。令 $M = \max\{|a_1|, \dots, |a_N|, |A| + 1\}$ 即可。$\square$

有界是收敛的必要条件而非充分条件：$(-1)^n$ 有界但发散。

**定理 2.1.3（与有限项无关）** 在数列中任意增加、删去或改变有限多项，不改变数列的收敛性，也不改变极限值。

数列极限描述的是 $n$ 充分大以后的项的变化趋势，所以讨论收敛性时可以只考虑"充分大的 $n$"。

**定理 2.1.4（保号性）** 设 $\lim\limits_{n \to \infty} a_n = A$。

1. 若 $A > 0$（$A < 0$），则对充分大的 $n$，恒有 $a_n > 0$（$a_n < 0$）；
2. 若对充分大的 $n$ 恒有 $a_n \geq 0$（$a_n \leq 0$），则 $A \geq 0$（$A \leq 0$）。

**证明** 1. 设 $A > 0$，取 $\varepsilon = \frac A2$，存在 $N$，当 $n > N$ 时 $|a_n - A| < \frac A2$，于是 $a_n > A - \frac A2 = \frac A2 > 0$。2. 是 1 的逆否命题。$\square$

结论 2 中的 $\geq$ 不能改为 $>$：$a_n = \frac1n > 0$，但极限 $0$ 不是正数。取极限时严格不等号可能变成等号。

**定理 2.1.5（保序性）** 设 $\lim\limits_{n \to \infty} a_n = A$，$\lim\limits_{n \to \infty} b_n = B$。

1. 若存在 $N$ 使 $n > N$ 时恒有 $a_n \leq b_n$，则 $A \leq B$；
2. 若 $A < B$，则存在 $N$ 使 $n > N$ 时恒有 $a_n < b_n$；
3. 若 $A < B$，则存在 $N$ 使 $n > N$ 时恒有 $a_n < B$。

**证明** 对 $b_n - a_n \to B - A$（四则运算见定理 2.2.1）应用定理 2.1.4 得到 1 与 2；在 2 中取 $b_n \equiv B$ 得到 3。$\square$

### 2.1.3. 数列的子列

**定义 2.1.3（子列）** 设 $\{a_n\}$ 为数列，$n_1 < n_2 < \cdots < n_j < \cdots$ 是一列严格单调增加的正整数，则称数列 $\{a_{n_j}\}_{j=1}^\infty$ 为 $\{a_n\}$ 的一个**子列**。

子列有两个特征：包含原数列中的无穷多项，并且保持原有的先后顺序。由 $n_j$ 严格增加得 $n_j \geq j$。

**定理 2.1.6** $\lim\limits_{n \to \infty} a_n = A$ 的充分必要条件是：$\{a_n\}$ 的任意子列都收敛，且极限都是 $A$。

**证明** 必要性：任给 $\varepsilon > 0$，存在 $N$ 使 $n > N$ 时 $|a_n - A| < \varepsilon$。对任意子列，$j > N$ 时 $n_j \geq j > N$，故 $|a_{n_j} - A| < \varepsilon$。充分性：$\{a_n\}$ 本身是自己的子列。$\square$

把定义否定一下就看出定理的用处：

$$
\lim_{n \to \infty} a_n \ne A \iff \exists \varepsilon_0 > 0,\ \text{存在子列 } \{a_{n_j}\} \text{ 使 } |a_{n_j} - A| \geq \varepsilon_0 \ (j = 1, 2, \dots),
$$
即 $N(A, \varepsilon_0)$ 外有无穷多项。因此定理 2.1.6 常用于证明数列发散：构造两个极限不相等的子列，或一个发散的子列。

**例 2.1.8** $a_n = \cos(n\pi) = (-1)^n$ 发散：$a_{2k} = 1 \to 1$，$a_{2k+1} = -1 \to -1$。

**定理 2.1.7** $\lim\limits_{n \to \infty} a_n = A$ 当且仅当 $\lim\limits_{k \to \infty} a_{2k} = A$ 且 $\lim\limits_{k \to \infty} a_{2k+1} = A$。

**证明** 必要性由定理 2.1.6 得到。充分性：任给 $\varepsilon > 0$，存在 $K_1$ 使 $k > K_1$ 时 $|a_{2k} - A| < \varepsilon$，存在 $K_2$ 使 $k > K_2$ 时 $|a_{2k+1} - A| < \varepsilon$。取 $N = 2\max\{K_1, K_2\} + 1$，则 $n > N$ 时无论 $n$ 是奇是偶都有 $|a_n - A| < \varepsilon$。$\square$

### 2.1.4. 无穷小量、无穷大量与无界量

**定义 2.1.4（无穷小量）** 若 $\lim\limits_{n \to \infty} a_n = 0$，则称 $\{a_n\}$ 为**无穷小量**（无穷小数列），简称无穷小。

例如 $\frac1n$、$q^n$（$|q| < 1$）都是无穷小。无穷小是一个趋于 $0$ 的数列，而不是一个"很小的数"。

**定义 2.1.5（无穷大量）** 若对任意 $M > 0$，都存在 $N \in \mathbb{N}_+$，使得当 $n > N$ 时都有 $|a_n| > M$，则称 $\{a_n\}$ 为**无穷大量**（无穷大数列），简称无穷大，记为 $a_n \to \infty$（$n \to \infty$）。若把 $|a_n| > M$ 换成 $a_n > M$（$a_n < -M$），则称 $\{a_n\}$ 为正（负）无穷大，记为 $a_n \to +\infty$（$-\infty$）。

例如 $n + 1 \to +\infty$，$-n^2 \to -\infty$，$(-1)^n n \to \infty$。无穷大数列是发散的，记号 $\lim a_n = \infty$ 只表示一种特定的发散方式。设 $a_n \ne 0$，则

$$
\{a_n\} \text{ 是无穷大} \iff \left\{\frac1{a_n}\right\} \text{ 是无穷小},
$$
因为 $|a_n| > M$ 与 $\left|\frac1{a_n}\right| < \frac1M$ 等价，而 $M$ 任意大与 $\frac1M$ 任意小是一回事。

**定义 2.1.6（无界数列）** 若对任意 $M > 0$，总存在某一项 $a_k$ 使 $|a_k| > M$，则称 $\{a_n\}$ 为**无界数列**。

无穷大要求 $n > N$ 后的所有项都超过 $M$，无界只要求有某一项超过 $M$。因此无穷大必无界，反之不然：$a_n = n + (-1)^n n$ 的偶数项为 $2n$、奇数项为 $0$，$b_n = n^{(-1)^n}$ 的偶数项为 $n$、奇数项为 $\frac1n$，它们都无界但不是无穷大。可以证明：无界数列必有子列趋于 $\infty$（逐个选取 $|a_{n_j}| > j$ 且 $n_j > n_{j-1}$ 的项即可）。

## 2.2. 数列极限的四则运算与存在的充分条件

### 2.2.1. 数列极限的四则运算

**定理 2.2.1（四则运算）** 设 $\lim\limits_{n \to \infty} a_n = A$，$\lim\limits_{n \to \infty} b_n = B$，则

1. $\lim\limits_{n \to \infty} c\,a_n = cA$（$c$ 为常数）；
2. $\lim\limits_{n \to \infty} (a_n \pm b_n) = A \pm B$；
3. $\lim\limits_{n \to \infty} a_nb_n = AB$；
4. $\lim\limits_{n \to \infty} \frac{a_n}{b_n} = \frac AB$（$B \ne 0$）；
5. $\lim\limits_{n \to \infty} a_n^m = A^m$（$m \in \mathbb{Z}$；$m < 0$ 时要求 $A \ne 0$）；
6. $\lim\limits_{n \to \infty} \sqrt[m]{a_n} = \sqrt[m]{A}$（$m \in \mathbb{N}_+$；$m$ 为偶数时要求 $a_n \geq 0$）。

**证明** 3. 由定理 2.1.2，存在 $M > 0$ 使 $|a_n| \leq M$。任给 $\varepsilon > 0$，存在 $N$，使 $n > N$ 时

$$
|a_n - A| < \frac{\varepsilon}{2(1 + |B|)}, \qquad |b_n - B| < \frac{\varepsilon}{2M},
$$
于是

$$
|a_nb_n - AB| \leq |a_n|\,|b_n - B| + |B|\,|a_n - A| < M \cdot \frac{\varepsilon}{2M} + |B| \cdot \frac{\varepsilon}{2(1 + |B|)} < \varepsilon.
$$
分母写 $1 + |B|$ 而不写 $|B|$，是为了在 $B = 0$ 时也成立。

4. 由 3，只需证 $\frac1{b_n} \to \frac1B$。由保号性的证明，$n$ 充分大时 $|b_n| > \frac{|B|}2$，于是 $\left|\frac1{b_n} - \frac1B\right| = \frac{|b_n - B|}{|b_n|\,|B|} < \frac{2}{B^2}|b_n - B|$，后者可以任意小。

6. 设 $A > 0$（$A = 0$ 的情形直接由定义验证，$A < 0$ 且 $m$ 为奇数时考虑 $-a_n$），由保号性可设 $a_n > 0$。由 $x^m - y^m = (x - y)(x^{m-1} + x^{m-2}y + \cdots + y^{m-1})$，

$$
\left|\sqrt[m]{a_n} - \sqrt[m]{A}\right| = \frac{|a_n - A|}{a_n^{\frac{m-1}m} + a_n^{\frac{m-2}m}A^{\frac1m} + \cdots + A^{\frac{m-1}m}} \leq \frac{|a_n - A|}{A^{\frac{m-1}m}},
$$
后者趋于 $0$。1、2、5 类似。$\square$

注意定理的前提是 $\{a_n\}$、$\{b_n\}$ 都收敛。$a_n \pm b_n$ 收敛并不意味着 $a_n$、$b_n$ 分别收敛；项数随 $n$ 增加的和（如 $\sum_{k=1}^n \frac{1}{n^2 + k}$）也不能逐项取极限。

**例 2.2.1（有理分式的极限）** 设 $a_0 \ne 0$，$b_0 \ne 0$，$k, l \in \mathbb{N}$，则

$$
\lim_{n \to \infty} \frac{a_0n^k + a_1n^{k-1} + \cdots + a_k}{b_0n^l + b_1n^{l-1} + \cdots + b_l} = \begin{cases} \dfrac{a_0}{b_0}, & k = l, \\[1ex] 0, & k < l, \\[0.5ex] \infty, & k > l. \end{cases}
$$
做法是分子分母同除以 $n^{\max\{k, l\}}$，再用 $\frac1{n^j} \to 0$ 与四则运算。例如 $\lim\limits_{n \to \infty} \frac{n^2 - n + 1}{2n^2 + 3n - 2} = \lim\limits_{n \to \infty} \frac{1 - \frac1n + \frac1{n^2}}{2 + \frac3n - \frac2{n^2}} = \frac12$。

**例 2.2.2** 求极限：

$$
\text{(1)}\ \lim_{n \to \infty} \Bigl(1 - \frac1{2^2}\Bigr)\Bigl(1 - \frac1{3^2}\Bigr)\cdots\Bigl(1 - \frac1{n^2}\Bigr); \qquad
\text{(2)}\ \lim_{n \to \infty} \frac{5^n + 4^n}{5^{n+1} + 4^{n+1}}; \qquad
\text{(3)}\ \lim_{n \to \infty} \frac{1 + a + \cdots + a^n}{1 + b + \cdots + b^n} \ (|a|, |b| < 1).
$$

**解** (1) $1 - \frac1{k^2} = \frac{(k-1)(k+1)}{k \cdot k}$，连乘时相邻因子相消，乘积等于 $\frac12 \cdot \frac{n+1}{n} \to \frac12$。(2) 分子分母同除以 $5^n$：$\frac{1 + (4/5)^n}{5 + 4(4/5)^n} \to \frac15$。(3) 由等比数列求和，分子 $= \frac{1 - a^{n+1}}{1 - a} \to \frac1{1-a}$，分母 $\to \frac1{1-b}$，极限为 $\frac{1 - b}{1 - a}$。

### 2.2.2. 数列极限存在的充分条件

前面的方法都是先猜出极限 $A$ 再验证，或由已知极限经四则运算得到。很多数列（如 $\left(1 + \frac1n\right)^n$）的极限事先无从猜起，需要不依赖极限值的存在判据。

#### 2.2.2.1. 夹逼定理

**定理 2.2.2（夹逼定理）** 设数列 $\{a_n\}$、$\{b_n\}$、$\{c_n\}$ 满足 $a_n \leq b_n \leq c_n$（$n$ 充分大），且 $\lim\limits_{n \to \infty} a_n = \lim\limits_{n \to \infty} c_n = A$，则 $\lim\limits_{n \to \infty} b_n = A$。

**证明** 由 $a_n - A \leq b_n - A \leq c_n - A$ 得 $|b_n - A| \leq \max\{|a_n - A|, |c_n - A|\}$。任给 $\varepsilon > 0$，存在 $N$ 使 $n > N$ 时 $|a_n - A| < \varepsilon$ 且 $|c_n - A| < \varepsilon$，从而 $|b_n - A| < \varepsilon$。$\square$

**例 2.2.3** 求下列数列的极限：

$$
\text{(1)}\ x_n = \sqrt{n + 1} - \sqrt n; \quad \text{(2)}\ x_n = \sum_{k=1}^n \frac{1}{n^2 + k}; \quad \text{(3)}\ x_n = \frac{5^n}{n!}; \quad \text{(4)}\ x_n = \sqrt[n]{a_1^n + a_2^n + \cdots + a_m^n} \ (a_i > 0).
$$

**解** (1) $0 < x_n = \frac{1}{\sqrt{n+1} + \sqrt n} < \frac1{\sqrt n} \to 0$，故 $x_n \to 0$。

(2) 每一项介于 $\frac1{n^2 + n}$ 与 $\frac1{n^2 + 1}$ 之间，故 $\frac{n}{n^2 + n} \leq x_n \leq \frac{n}{n^2 + 1}$，两边都趋于 $0$，$x_n \to 0$。

(3) 由 $(n!)^2 = \prod_{k=1}^n k(n + 1 - k) \geq n^n$（每个因子 $k(n+1-k) \geq n$）得 $n! \geq n^{n/2}$，于是 $0 < x_n \leq \frac{5^n}{n^{n/2}} = \left(\frac{25}{n}\right)^{n/2}$；$n > 50$ 时右边 $\leq 2^{-n/2} \to 0$，故 $x_n \to 0$。

(4) 记 $a = \max\{a_1, \dots, a_m\}$，则 $a^n \leq a_1^n + \cdots + a_m^n \leq m a^n$，于是 $a \leq x_n \leq \sqrt[n]m\, a$。由例 2.1.3，$\sqrt[n]m \to 1$，故 $x_n \to a = \max\{a_1, \dots, a_m\}$。

**例 2.2.4** 设 $a_n > 0$，$\lim\limits_{n \to \infty} \frac{a_{n+1}}{a_n} = q < 1$，则 $\lim\limits_{n \to \infty} a_n = 0$。

**证明** 取 $\varepsilon_0 > 0$ 使 $r = q + \varepsilon_0 < 1$。存在 $N$，当 $n \geq N$ 时 $\frac{a_{n+1}}{a_n} < r$，于是 $n > N$ 时 $0 < a_n < r a_{n-1} < \cdots < r^{n-N}a_N$。右边 $= \frac{a_N}{r^N} r^n \to 0$，由夹逼定理 $a_n \to 0$。$\square$

由此立即得到 $\frac{n^k}{a^n} \to 0$（$a > 1$）、$\frac{a^n}{n!} \to 0$ 等结论：比值分别趋于 $\frac1a$ 与 $0$。这是[第 8 章](/2.2.8)比值判别法的雏形。

**例 2.2.5** 求曲线 $y = x^2$、直线 $x = 1$ 与 $x$ 轴围成的区域 $D$ 的面积 $S$。

**解** 把 $[0, 1]$ 分成 $n$ 等份，第 $k$ 个小区间 $\left[\frac{k-1}n, \frac kn\right]$ 上的窄条面积 $S_k$ 介于两个矩形面积之间：$\frac1n\left(\frac{k-1}n\right)^2 \leq S_k \leq \frac1n\left(\frac kn\right)^2$。求和并用 $\sum_{k=1}^n k^2 = \frac{n(n+1)(2n+1)}6$：

$$
\frac{(n - 1)n(2n - 1)}{6n^3} \leq S \leq \frac{n(n + 1)(2n + 1)}{6n^3}.
$$
两边都趋于 $\frac13$，由夹逼定理（$S$ 是常数）$S = \frac13$。这正是[第 7 章](/2.2.7)定积分 $\int_0^1 x^2\,\mathrm{d}x$ 的思想。

#### 2.2.2.2. 单调收敛定理

**定理 2.2.3（单调收敛定理）** 单调有界数列必收敛。具体地：

1. 若 $\{a_n\}$ 单调非减且有上界，则 $\lim\limits_{n \to \infty} a_n = \sup\{a_n\}$；
2. 若 $\{a_n\}$ 单调非增且有下界，则 $\lim\limits_{n \to \infty} a_n = \inf\{a_n\}$。

**证明** 只证 1。由**确界存在定理**，$A = \sup\{a_n\}$ 存在。任给 $\varepsilon > 0$，由确界的刻画（定理 1.1.4），存在 $N$ 使 $a_N > A - \varepsilon$。由于 $\{a_n\}$ 单调非减，对所有 $n > N$，$A - \varepsilon < a_N \leq a_n \leq A$，即 $|a_n - A| < \varepsilon$。$\square$

单调收敛定理只断言极限存在，不给出极限值。它的威力在于不需要事先知道极限，下面用它定义自然常数。

**例 2.2.6** 数列 $a_n = \left(1 + \frac1n\right)^n$ 单调增加且有上界 $3$，因而收敛。

**证明** 由二项式定理，

$$
a_n = 1 + \sum_{k=1}^n \binom nk \frac1{n^k} = 1 + \sum_{k=1}^n \frac1{k!}\Bigl(1 - \frac1n\Bigr)\Bigl(1 - \frac2n\Bigr)\cdots\Bigl(1 - \frac{k-1}n\Bigr).
$$
把 $n$ 换成 $n + 1$ 时，每个括号 $1 - \frac jn$ 变大为 $1 - \frac j{n+1}$，并且多出第 $n + 1$ 项（正数），所以 $a_n < a_{n+1}$。又每个括号都小于 $1$，

$$
a_n < 1 + \sum_{k=1}^n \frac1{k!} \leq 1 + 1 + \sum_{k=2}^n \frac1{k(k-1)} = 2 + \sum_{k=2}^n \Bigl(\frac1{k-1} - \frac1k\Bigr) = 3 - \frac1n < 3.
$$
由单调收敛定理，$\{a_n\}$ 收敛。$\square$

**定义 2.2.1（自然常数）** 称极限

$$
\mathrm{e} = \lim_{n \to \infty} \Bigl(1 + \frac1n\Bigr)^n \approx 2.71828
$$
为**自然常数**（Euler 数），以 $\mathrm{e}$ 为底的对数称为自然对数，记为 $\ln x$。

类似可证 $b_n = \left(1 + \frac1n\right)^{n+1}$ 单调减少且也以 $\mathrm{e}$ 为极限，于是对一切 $n \in \mathbb{N}_+$

$$
\Bigl(1 + \frac1n\Bigr)^n < \mathrm{e} < \Bigl(1 + \frac1n\Bigr)^{n+1}, \qquad\text{取对数得}\qquad \frac{1}{n + 1} < \ln\Bigl(1 + \frac1n\Bigr) < \frac1n. \tag{2.1}
$$
不等式 (2.1) 在级数中会再次出现：它说明 $1 + \frac12 + \cdots + \frac1n - \ln n$ 单调且有界（[第 5 章](/2.2.5)）。

**例 2.2.7** 设 $a > 0$，$a_n = \underbrace{\sqrt{a + \sqrt{a + \cdots + \sqrt a}}}_{n \text{ 重根号}}$，证明 $\{a_n\}$ 收敛并求其极限。

**解** 数列满足递推式 $a_1 = \sqrt a$，$a_{n+1} = \sqrt{a + a_n}$。单调性：$a_2 = \sqrt{a + \sqrt a} > a_1$；若 $a_n > a_{n-1}$，则 $a_{n+1} = \sqrt{a + a_n} > \sqrt{a + a_{n-1}} = a_n$。有界性：$a_1 < \sqrt a + 1$；若 $a_n < \sqrt a + 1$，则 $a_{n+1} < \sqrt{a + \sqrt a + 1} < \sqrt{a + 2\sqrt a + 1} = \sqrt a + 1$。由单调收敛定理，$a_n \to k$。在递推式两边取极限（左边是子列，极限也是 $k$）：$k = \sqrt{a + k}$，即 $k^2 - k - a = 0$。由 $k > 0$ 得

$$
\lim_{n \to \infty} a_n = \frac{1 + \sqrt{1 + 4a}}{2}.
$$

**例 2.2.8** 设 $a_1 = \sqrt2$，$a_n = \sqrt{2a_{n-1}}$（$n \geq 2$），则 $a_n$ 单调增加（归纳：$a_n > a_{n-1} \implies a_{n+1} = \sqrt{2a_n} > \sqrt{2a_{n-1}} = a_n$）且 $a_n < 2$（归纳：$a_n < 2 \implies a_{n+1} < \sqrt4 = 2$），故收敛。设极限为 $k$，由 $k = \sqrt{2k}$ 与 $k \geq a_1 > 0$ 得 $k = 2$。

**算法 2.2.1（求递推数列 $a_{n+1} = f(a_n)$ 的极限）**

1. 用数学归纳法证明 $\{a_n\}$ 单调（比较 $a_2$ 与 $a_1$，再由 $f$ 的单调性传递）；
2. 用数学归纳法证明 $\{a_n\}$ 有界（界通常就是猜出的极限，或稍大的数）；
3. 由单调收敛定理，$a_n \to k$；在递推式两边取极限得到方程 $k = f(k)$（需要 $f$ 连续，见[第 3 章](/2.2.3)）；
4. 解方程，并用保号性、保序性（如 $k \geq a_1$）舍去不合要求的根。

第 3 步之前必须先证明极限存在：例如 $a_1 = 2$，$a_{n+1} = a_n^2$，若直接设极限为 $k$ 会得到 $k = k^2$，而数列实际上趋于 $+\infty$。

#### 2.2.2.3. Cauchy 收敛准则

单调收敛定理只适用于单调数列。我们希望有一个对所有数列都适用、又不涉及极限值的收敛判据。收敛数列的项彼此越来越接近；Cauchy 准则说，反过来"项彼此越来越接近"也足以保证收敛。

**定义 2.2.2（Cauchy 数列）** 设 $\{x_n\}$ 为数列。若对任意 $\varepsilon > 0$，存在 $N \in \mathbb{N}_+$，使得对所有 $m, n > N$ 都有 $|x_n - x_m| < \varepsilon$，则称 $\{x_n\}$ 为 **Cauchy 数列**（基本列）。等价地：对任意 $\varepsilon > 0$，存在 $N$，使得对所有 $n > N$ 及所有 $p \in \mathbb{N}_+$ 都有 $|x_{n+p} - x_n| < \varepsilon$。

例如 $\left\{\frac1n\right\}$、$\left\{\frac1{2^n}\right\}$、$\{q^n\}$（$|q| < 1$）都是 Cauchy 数列，$\{n\}$、$\{(-1)^n\}$ 不是。否定形式在证明发散时使用：

$$
\{x_n\} \text{ 不是 Cauchy 数列} \iff \exists \varepsilon_0 > 0,\ \forall j \in \mathbb{N}_+,\ \exists n_j > j,\ p_j \in \mathbb{N}_+,\ |x_{n_j + p_j} - x_{n_j}| \geq \varepsilon_0.
$$

**定理 2.2.4（Cauchy 收敛准则）** 数列 $\{x_n\}$ 收敛的充分必要条件是 $\{x_n\}$ 为 Cauchy 数列。

**证明** 必要性：设 $x_n \to A$。任给 $\varepsilon > 0$，存在 $N$ 使 $n > N$ 时 $|x_n - A| < \frac\varepsilon2$，于是 $m, n > N$ 时 $|x_n - x_m| \leq |x_n - A| + |x_m - A| < \varepsilon$。

充分性的证明需要列紧性定理，见[第 3 章](/2.2.3#sec-3.2)定理 3.2.3。$\square$

Cauchy 准则是**实数的完备性**的又一种表述：在有理数中，逼近 $\sqrt2$ 的有理数列（如 $1, 1.4, 1.41, 1.414, \dots$）是 Cauchy 数列，但在 $\mathbb{Q}$ 中没有极限。[1.2.4](/1.2.4#sec-4.1) 正是用有理 Cauchy 数列的等价类来构造实数的。

**例 2.2.9** 证明 $x_n = \sum_{k=1}^n \frac{\sin k}{k^2}$ 收敛。

**证明** 对任意 $n, p \in \mathbb{N}_+$，

$$
|x_{n+p} - x_n| = \left|\sum_{k=n+1}^{n+p} \frac{\sin k}{k^2}\right| \leq \sum_{k=n+1}^{n+p} \frac1{k^2} < \sum_{k=n+1}^{n+p} \frac1{(k-1)k} = \frac1n - \frac1{n+p} < \frac1n.
$$
任给 $\varepsilon > 0$，取 $N = \left\lfloor \frac1\varepsilon \right\rfloor$，则 $n > N$ 时对一切 $p$ 都有 $|x_{n+p} - x_n| < \varepsilon$。故 $\{x_n\}$ 是 Cauchy 数列，从而收敛。$\square$

**例 2.2.10** 证明 $a_n = \sum_{k=1}^n \frac{(-1)^{k-1}}{k}$ 收敛。

**证明** 对任意 $n, p$，

$$
|a_{n+p} - a_n| = \left|\frac1{n+1} - \frac1{n+2} + \frac1{n+3} - \cdots + \frac{(-1)^{p-1}}{n+p}\right|.
$$
这是一个各项绝对值单调减小的交错和。从第一项起两两配对 $\left(\frac1{n+1} - \frac1{n+2}\right) + \left(\frac1{n+3} - \frac1{n+4}\right) + \cdots$，每对非负，故和 $\geq 0$；从第二项起配对 $\frac1{n+1} - \left(\frac1{n+2} - \frac1{n+3}\right) - \cdots$，故和 $\leq \frac1{n+1}$。于是 $|a_{n+p} - a_n| \leq \frac1{n+1}$，任给 $\varepsilon > 0$，取 $N = \left\lfloor \frac1\varepsilon \right\rfloor$ 即可。$\square$

**例 2.2.11** 证明 $a_n = \sum_{k=1}^n \frac1k$ 发散。

**证明** 取 $\varepsilon_0 = \frac12$。对任意 $j \in \mathbb{N}_+$，取 $n_j = j$，$p_j = j$，则

$$
|a_{2j} - a_j| = \sum_{k=j+1}^{2j} \frac1k \geq j \cdot \frac1{2j} = \frac12 = \varepsilon_0.
$$
故 $\{a_n\}$ 不是 Cauchy 数列，从而发散。又 $\{a_n\}$ 单调增加，由单调收敛定理它无上界，即 $a_n \to +\infty$。$\square$

例 2.2.10 与例 2.2.11 是[第 8 章](/2.2.8)交错级数与调和级数的雏形。

## 2.3. 函数极限的概念和性质

把数列极限的思想推广到函数，得到函数极限（limit of a function）。数列的自变量 $n$ 只能趋于 $+\infty$，函数的自变量 $x$ 则有六种变化过程：$x \to +\infty$、$x \to -\infty$、$x \to \infty$、$x \to x_0$、$x \to x_0^-$、$x \to x_0^+$。

### 2.3.1. 函数在无穷远处的极限

**定义 2.3.1（$x \to +\infty$ 时的极限）** 设 $f$ 在 $(a, +\infty)$ 上有定义，$A \in \mathbb{R}$。若对任意 $\varepsilon > 0$，存在 $X > 0$，使得当 $x > X$ 时都有 $|f(x) - A| < \varepsilon$，则称 $x$ 趋于 $+\infty$ 时 $f$ 的极限为 $A$，记为 $\lim\limits_{x \to +\infty} f(x) = A$ 或 $f(x) \to A$（$x \to +\infty$）。

与数列极限对比，唯一的区别是 $N \in \mathbb{N}_+$ 换成了实数 $X$，$n > N$ 换成了 $x > X$。把 $x > X$ 换成 $x < -X$，得到 $\lim\limits_{x \to -\infty} f(x) = A$ 的定义。

**定义 2.3.2（$x \to \infty$ 时的极限）** 设 $f$ 在 $\{x \mid |x| > a\}$ 上有定义，$A \in \mathbb{R}$。若对任意 $\varepsilon > 0$，存在 $X > 0$，使得当 $|x| > X$ 时都有 $|f(x) - A| < \varepsilon$，则记 $\lim\limits_{x \to \infty} f(x) = A$。

显然 $\lim\limits_{x \to \infty} f(x) = A \iff \lim\limits_{x \to +\infty} f(x) = A$ 且 $\lim\limits_{x \to -\infty} f(x) = A$。例如 $\lim\limits_{x \to \infty} \arctan x$ 不存在，因为两个方向的极限分别是 $\pm\frac\pi2$（例 2.3.1）。

**例 2.3.1** 证明 $\lim\limits_{x \to +\infty} \arctan x = \frac\pi2$，$\lim\limits_{x \to -\infty} \arctan x = -\frac\pi2$。

**证明** 任给 $\varepsilon \in (0, 1)$。$\left|\arctan x - \frac\pi2\right| = \frac\pi2 - \arctan x < \varepsilon \iff \arctan x > \frac\pi2 - \varepsilon \iff x > \tan\left(\frac\pi2 - \varepsilon\right)$。取 $X = \tan\left(\frac\pi2 - \varepsilon\right)$ 即可。第二式由奇函数性得到。$\square$

同理 $\lim\limits_{x \to +\infty} \operatorname{arccot} x = 0$，$\lim\limits_{x \to -\infty} \operatorname{arccot} x = \pi$。

**例 2.3.2** 证明 $\lim\limits_{x \to \infty} \frac{x^2 - 1}{x^2 + 1} = 1$。

**证明** $\left|\frac{x^2 - 1}{x^2 + 1} - 1\right| = \frac2{x^2 + 1} < \frac2{x^2}$。任给 $\varepsilon > 0$，要 $\frac2{x^2} < \varepsilon$，只要 $|x| > \sqrt{2/\varepsilon}$，取 $X = \sqrt{2/\varepsilon}$。$\square$

验证 $\lim\limits_{x \to \infty} f(x) = A$ 的方法与算法 2.1.1 相同：把 $|f(x) - A|$ 放大成 $k|x|^{-m}$（$k, m > 0$）的形式，再取 $X = (k/\varepsilon)^{1/m}$。

### 2.3.2. 函数在一点的极限

**定义 2.3.3（$x \to x_0$ 时的极限）** 设 $f$ 在 $x_0$ 的某个去心邻域内有定义，$A \in \mathbb{R}$。若对任意 $\varepsilon > 0$，存在 $\delta > 0$，使得当 $0 < |x - x_0| < \delta$（即 $x \in N^*(x_0, \delta)$）时都有

$$
|f(x) - A| < \varepsilon,
$$
则称 $x \to x_0$ 时 $f(x)$ 的极限为 $A$，记为 $\lim\limits_{x \to x_0} f(x) = A$ 或 $f(x) \to A$（$x \to x_0$）。

条件 $0 < |x - x_0|$ 排除了 $x = x_0$：函数在一点的极限与函数在这一点的值无关（$f$ 甚至可以在 $x_0$ 无定义），也与函数在这一点某个邻域之外的值无关。

![ε-δ 定义的几何意义：当 x 落在 x_0 的去心 δ 邻域（竖带）内时，f(x) 落在 A 的 ε 邻域（横带）内；f(x_0) 的值不影响极限](./plots/epsilon-delta.py)

**定义 2.3.4（单侧极限）** 设 $f$ 在 $(x_0 - \rho, x_0)$ 内有定义，$A \in \mathbb{R}$。若对任意 $\varepsilon > 0$，存在 $\delta > 0$，使得当 $x_0 - \delta < x < x_0$ 时都有 $|f(x) - A| < \varepsilon$，则称 $A$ 为 $f$ 在 $x_0$ 处的左极限，记为 $\lim\limits_{x \to x_0^-} f(x) = A$ 或 $f(x_0 - 0) = A$。把条件换成 $x_0 < x < x_0 + \delta$，得到右极限 $\lim\limits_{x \to x_0^+} f(x) = f(x_0 + 0)$。左、右极限统称为**单侧极限**。

由定义直接得到

$$
\lim_{x \to x_0} f(x) = A \iff \lim_{x \to x_0^-} f(x) = A \ \text{且}\ \lim_{x \to x_0^+} f(x) = A.
$$
分段函数在分段点处的极限，通常要分别求左、右极限。

**例 2.3.3** 验证：(1) $\lim\limits_{x \to x_0} \cos x = \cos x_0$，$\lim\limits_{x \to x_0} \sin x = \sin x_0$；(2) $\lim\limits_{x \to 1} \ln x = 0$；(3) $\lim\limits_{x \to 0} a^x = 1$（$a > 0$）。

**证明** (1) 利用 $|\sin t| \leq |t|$：

$$
|\cos x - \cos x_0| = 2\left|\sin\frac{x + x_0}{2}\right|\left|\sin\frac{x - x_0}{2}\right| \leq 2\left|\sin\frac{x - x_0}2\right| \leq |x - x_0|,
$$
任给 $\varepsilon > 0$ 取 $\delta = \varepsilon$ 即可；$\sin x$ 同理。

(2) 任给 $\varepsilon > 0$，$|\ln x| < \varepsilon \iff \mathrm{e}^{-\varepsilon} < x < \mathrm{e}^\varepsilon \iff \mathrm{e}^{-\varepsilon} - 1 < x - 1 < \mathrm{e}^\varepsilon - 1$。取 $\delta = \min\{\mathrm{e}^\varepsilon - 1, 1 - \mathrm{e}^{-\varepsilon}\}$。

(3) 设 $a > 1$（$0 < a < 1$ 时用 $a^x = 1/(1/a)^x$，$a = 1$ 时显然）。任给 $\varepsilon \in (0, 1)$，$|a^x - 1| < \varepsilon \iff \log_a(1 - \varepsilon) < x < \log_a(1 + \varepsilon)$。取 $\delta = \min\{\log_a(1 + \varepsilon), -\log_a(1 - \varepsilon)\}$。$\square$

**例 2.3.4** 证明 $\lim\limits_{x \to 1^-} \arcsin x = \frac\pi2$。

**证明** 设 $\frac12 \leq x < 1$，记 $t = \frac\pi2 - \arcsin x \in \left(0, \frac\pi3\right]$。由 $t < \tan t$（$0 < t < \frac\pi2$），

$$
\frac\pi2 - \arcsin x < \tan t = \cot(\arcsin x) = \frac{\sqrt{1 - x^2}}{x} \leq 2\sqrt{(1 - x)(1 + x)} \leq 2\sqrt2\sqrt{1 - x}.
$$
任给 $\varepsilon > 0$，要右边小于 $\varepsilon$，只要 $1 - x < \frac{\varepsilon^2}8$。取 $\delta = \min\left\{\frac{\varepsilon^2}8, \frac12\right\}$，则 $1 - \delta < x < 1$ 时 $\left|\arcsin x - \frac\pi2\right| < \varepsilon$。$\square$

同理 $\lim\limits_{x \to -1^+} \arcsin x = -\frac\pi2$。证明中用到的不等式

$$
\sin x < x < \tan x, \quad x \in \Bigl(0, \frac\pi2\Bigr) \tag{2.2}
$$
来自单位圆中三角形与扇形面积的比较（见例 2.4.3 的证明）。

**例 2.3.5** 求 $\lim\limits_{x \to 1} \frac{x^2 - 1}{x^2 - x}$。

**解** $x \ne 1$ 时 $\frac{x^2 - 1}{x^2 - x} = \frac{x + 1}{x} = 1 + \frac1x$，猜测极限为 $2$。验证：$\left|1 + \frac1x - 2\right| = \frac{|x - 1|}{|x|}$。限制 $|x - 1| < \frac12$，则 $x > \frac12$，上式 $< 2|x - 1|$。任给 $\varepsilon > 0$，取 $\delta = \min\left\{\frac12, \frac\varepsilon2\right\}$，则 $0 < |x - 1| < \delta$ 时 $\left|\frac{x^2 - 1}{x^2 - x} - 2\right| < \varepsilon$。

这里"先把 $x$ 限制在 $x_0$ 的一个固定邻域内"是放大时的常用技巧：它让分母等因子有了确定的界，最后 $\delta$ 取两个限制中较小的一个。一般地，把 $|f(x) - A|$ 放大成 $k|x - x_0|^m$（$k, m > 0$），取 $\delta = (\varepsilon/k)^{1/m}$（再与先前的限制取最小值）。

函数趋于无穷大也可用同样的语言描述。例如

$$
\lim_{x \to x_0} f(x) = \infty \iff \forall M > 0,\ \exists \delta > 0,\ 0 < |x - x_0| < \delta \implies |f(x)| > M;
$$

$$
\lim_{x \to \infty} f(x) = +\infty \iff \forall M > 0,\ \exists X > 0,\ |x| > X \implies f(x) > M.
$$
把六种自变量过程与 $f(x) \to A, \infty, +\infty, -\infty$ 四种结果组合，就得到全部 24 种极限的定义，读者可以逐一写出。与数列一样，$\lim f(x) = \infty$ 是极限不存在的一种特殊情形。

### 2.3.3. 函数极限的性质

函数极限有六种形式，常用 $x \to \square$ 泛指其中之一。下面的性质以 $x \to x_0$ 为例叙述和证明，对其他五种形式有类似的结论（"$x_0$ 的去心邻域"相应地换成"$(X, +\infty)$""$x_0$ 的左侧"等）。

**性质 2.3.1（唯一性）** 函数极限如果存在，则唯一。

**性质 2.3.2（局部有界性）** 若 $\lim\limits_{x \to x_0} f(x)$ 存在，则 $f$ 在 $x_0$ 的某个去心邻域内有界：存在 $\delta > 0$ 和 $M > 0$，使 $|f(x)| \leq M$，$x \in N^*(x_0, \delta)$。

**证明** 设极限为 $A$。对 $\varepsilon = 1$，存在 $\delta > 0$，当 $x \in N^*(x_0, \delta)$ 时 $|f(x) - A| < 1$，从而 $|f(x)| < |A| + 1$。$\square$

与数列不同，这里只有局部有界：$\lim\limits_{x \to 1} \frac1x = 1$，但 $\frac1x$ 在 $(0, 1)$ 上无界。

**性质 2.3.3（局部保号性）**

1. 若 $\lim\limits_{x \to x_0} f(x) > 0$（$< 0$），则存在 $\delta > 0$，当 $x \in N^*(x_0, \delta)$ 时 $f(x) > 0$（$< 0$）；
2. 若 $f$ 在 $x_0$ 的某个去心邻域内非负（非正），且 $\lim\limits_{x \to x_0} f(x)$ 存在，则 $\lim\limits_{x \to x_0} f(x) \geq 0$（$\leq 0$）。

下面的定理把函数极限与数列极限联系起来，从而可以把数列极限的结论移植到函数极限上。

**定理 2.3.6（Heine 定理）** $\lim\limits_{x \to x_0} f(x) = A$ 的充分必要条件是：对每个满足 $x_n \to x_0$ 且 $x_n \ne x_0$（$n \in \mathbb{N}_+$）的数列 $\{x_n\}$（$x_n$ 在 $f$ 的定义域中），都有 $\lim\limits_{n \to \infty} f(x_n) = A$。

**证明** 必要性：任给 $\varepsilon > 0$，存在 $\delta > 0$，当 $0 < |x - x_0| < \delta$ 时 $|f(x) - A| < \varepsilon$。对这个 $\delta$，存在 $N$ 使 $n > N$ 时 $|x_n - x_0| < \delta$，又 $x_n \ne x_0$，故 $|f(x_n) - A| < \varepsilon$。

充分性（反证）：若 $\lim\limits_{x \to x_0} f(x) = A$ 不成立，则存在 $\varepsilon_0 > 0$，对任意 $\delta > 0$ 都有 $x \in N^*(x_0, \delta)$ 使 $|f(x) - A| \geq \varepsilon_0$。依次取 $\delta = 1, \frac12, \dots, \frac1n, \dots$，得到 $x_n \in N^*\left(x_0, \frac1n\right)$ 使 $|f(x_n) - A| \geq \varepsilon_0$。于是 $x_n \to x_0$，$x_n \ne x_0$，但 $f(x_n) \not\to A$，矛盾。$\square$

Heine 定理对其他五种极限过程同样成立，例如 $\lim\limits_{x \to +\infty} f(x) = A$ 当且仅当对每个 $x_n \to +\infty$ 都有 $f(x_n) \to A$。它最常见的用途是证明函数极限不存在：构造两个数列 $x_n \to x_0$、$y_n \to x_0$（$x_n, y_n \ne x_0$），使 $\lim f(x_n) \ne \lim f(y_n)$，或使某个 $\lim f(x_n)$ 不存在。

**例 2.3.6** 证明 $\lim\limits_{x \to 0} \sin\frac1x$ 不存在。

**证明** 取 $x_n = \frac1{2n\pi}$，$y_n = \frac1{2n\pi + \frac\pi2}$，两者都趋于 $0$ 且不等于 $0$，但 $\sin\frac1{x_n} = 0 \to 0$，$\sin\frac1{y_n} = 1 \to 1$。由 Heine 定理，极限不存在。$\square$

## 2.4. 函数极限的运算法则

### 2.4.1. 函数极限的四则运算

**定理 2.4.1（四则运算）** 设 $\lim\limits_{x \to \square} f(x) = A$，$\lim\limits_{x \to \square} g(x) = B$，则

1. $\lim\limits_{x \to \square} c f(x) = cA$（$c \in \mathbb{R}$）；
2. $\lim\limits_{x \to \square} [f(x) \pm g(x)] = A \pm B$；
3. $\lim\limits_{x \to \square} f(x)g(x) = AB$；
4. $\lim\limits_{x \to \square} \frac{f(x)}{g(x)} = \frac AB$（$B \ne 0$）；
5. $\lim\limits_{x \to \square} f(x)^k = A^k$（$k \in \mathbb{Q}$，$A > 0$）。

证明可以仿照定理 2.2.1，也可以由 Heine 定理直接从数列的结论得到。

**例 2.4.1** 求极限（$m, n \in \mathbb{N}_+$）：

$$
\text{(1)}\ \lim_{x \to 0} \frac{(1 + mx)^n - (1 + nx)^m}{x^2}; \qquad
\text{(2)}\ \lim_{x \to 1} \frac{x^m - 1}{x^n - 1}; \qquad
\text{(3)}\ \lim_{x \to 1} \frac{x^{n+1} - (n + 1)x + n}{(x - 1)^2}; \qquad
\text{(4)}\ \lim_{x \to +\infty} \frac{\sqrt{x + \sqrt{x + \sqrt x}}}{\sqrt{x + 1}}.
$$

**解** (1) 用二项式定理展开到 $x^2$ 项：$(1 + mx)^n = 1 + nmx + \binom n2 m^2x^2 + x^3(\cdots)$，$(1 + nx)^m = 1 + mnx + \binom m2 n^2x^2 + x^3(\cdots)$，相减后一次项抵消，

$$
\lim_{x \to 0} \frac{(1 + mx)^n - (1 + nx)^m}{x^2} = \frac{n(n-1)m^2 - m(m-1)n^2}{2} = \frac{mn(n - m)}{2}.
$$

(2) 约去公因子 $x - 1$：$\frac{x^m - 1}{x^n - 1} = \frac{1 + x + \cdots + x^{m-1}}{1 + x + \cdots + x^{n-1}} \to \frac mn$。

(3) $x^{n+1} - (n+1)x + n = x(x^n - 1) - n(x - 1) = (x - 1)\bigl[(x - 1) + (x^2 - 1) + \cdots + (x^n - 1)\bigr]$（把 $x(1 + x + \cdots + x^{n-1}) - n$ 逐项配对），再约去一个 $x - 1$：

$$
\lim_{x \to 1} \frac{(x - 1) + (x^2 - 1) + \cdots + (x^n - 1)}{x - 1} = 1 + 2 + \cdots + n = \frac{n(n + 1)}{2}.
$$

(4) 分子分母同除以 $\sqrt x$：$\frac{\sqrt{1 + \sqrt{1/x + 1/x^{3/2}}}}{\sqrt{1 + 1/x}} \to 1$。

**例 2.4.2（指数与对数函数的极限）** 设 $a > 0$，$x_0 \in \mathbb{R}$，$y_0 > 0$，则 $\lim\limits_{x \to x_0} a^x = a^{x_0}$，$\lim\limits_{x \to y_0} \ln x = \ln y_0$。

**证明** 由例 2.3.3，$\lim\limits_{t \to 0} a^t = 1$，于是 $a^x - a^{x_0} = a^{x_0}(a^{x - x_0} - 1) \to 0$（$x \to x_0$）。类似地 $\ln x - \ln y_0 = \ln\frac{x}{y_0}$，而 $x \to y_0$ 时 $\frac{x}{y_0} \to 1$，由例 2.3.3 与复合极限定理（§2.4.4）$\ln\frac x{y_0} \to 0$。$\square$

### 2.4.2. 夹逼定理

**定理 2.4.2（夹逼定理）** 设 $f, g, h$ 在 $x_0$ 的某个去心邻域 $N^*(x_0, \delta_0)$ 内满足 $f(x) \leq h(x) \leq g(x)$，且 $\lim\limits_{x \to x_0} f(x) = \lim\limits_{x \to x_0} g(x) = A$，则 $\lim\limits_{x \to x_0} h(x) = A$。

**证明** 任给 $\varepsilon > 0$，存在 $\delta_1, \delta_2 > 0$，使 $0 < |x - x_0| < \delta_1$ 时 $|f(x) - A| < \varepsilon$，$0 < |x - x_0| < \delta_2$ 时 $|g(x) - A| < \varepsilon$。取 $\delta = \min\{\delta_0, \delta_1, \delta_2\}$，则 $0 < |x - x_0| < \delta$ 时 $|h(x) - A| \leq \max\{|f(x) - A|, |g(x) - A|\} < \varepsilon$。$\square$

夹逼定理对另外五种极限过程同样成立。一个典型应用是"无穷小乘有界量"：$|x\sin\frac1x| \leq |x|$，故 $\lim\limits_{x \to 0} x\sin\frac1x = 0$，尽管 $\sin\frac1x$ 本身没有极限（例 2.3.6）。

![左：sin(1/x) 在 0 附近无限振荡，沿两个数列取到不同的极限；右：x sin(1/x) 被夹在 −|x| 与 |x| 之间，由夹逼定理趋于 0](./plots/sin-one-over-x.py)

**例 2.4.3（第一个重要极限）** 证明 $\lim\limits_{x \to 0} \frac{\sin x}{x} = 1$。

**证明** 先证右极限。设 $0 < x < \frac\pi2$，在单位圆中取圆心角为 $x$ 的扇形 $OAB$（$B$ 在 $x$ 轴上），过 $B$ 作切线交 $OA$ 的延长线于 $C$。三角形 $OAB$、扇形 $OAB$、三角形 $OBC$ 的面积依次增大：

$$
\frac{\sin x}{2} < \frac x2 < \frac{\tan x}{2}.
$$
这就是不等式 (2.2)。各项除以 $\frac{\sin x}2$ 并取倒数，得 $\cos x < \frac{\sin x}{x} < 1$。由例 2.3.3，$\cos x \to 1$，由夹逼定理 $\lim\limits_{x \to 0^+} \frac{\sin x}x = 1$。$\frac{\sin x}x$ 是偶函数，故左极限也是 $1$。$\square$

由它可以得到

$$
\lim_{x \to 0} \frac{\tan x}{x} = \lim_{x \to 0} \frac{\sin x}{x} \cdot \frac{1}{\cos x} = 1, \qquad
\lim_{x \to 0} \frac{\arcsin x}{x} = \lim_{y \to 0} \frac{y}{\sin y} = 1, \qquad
\lim_{x \to 0} \frac{\arctan x}{x} = \lim_{y \to 0} \frac{y}{\tan y} = 1,
$$
后两式令 $y = \arcsin x$、$y = \arctan x$（$x \to 0$ 时 $y \to 0$，用复合极限定理 2.4.4）。

### 2.4.3. 单调函数的极限

单调收敛定理（定理 2.2.3）的函数版本是：单调函数在每一点的单侧极限都存在。

**定理 2.4.3（单调函数的单侧极限）**

1. 设 $f$ 在 $(a, x_0]$ 上单调非减，则 $\lim\limits_{x \to x_0^-} f(x)$ 存在，且等于 $\sup\limits_{a < x < x_0} f(x) \leq f(x_0)$；
2. 设 $f$ 在 $[x_0, b)$ 上单调非减，则 $\lim\limits_{x \to x_0^+} f(x)$ 存在，且等于 $\inf\limits_{x_0 < x < b} f(x) \geq f(x_0)$；
3. 设 $f$ 在 $(a, +\infty)$ 上单调且有界，则 $\lim\limits_{x \to +\infty} f(x)$ 存在；在 $(-\infty, b)$ 上单调且有界，则 $\lim\limits_{x \to -\infty} f(x)$ 存在。

单调非增时，1、2 中的上确界与下确界互换，不等号反向。

**证明** 1. $f$ 在 $(a, x_0)$ 上以 $f(x_0)$ 为上界，由确界存在定理，$A = \sup\limits_{a < x < x_0} f(x)$ 存在且 $A \leq f(x_0)$。任给 $\varepsilon > 0$，$A - \varepsilon$ 不是上界，存在 $x_1 \in (a, x_0)$ 使 $f(x_1) > A - \varepsilon$。由单调性，对一切 $x \in (x_1, x_0)$，$A - \varepsilon < f(x_1) \leq f(x) \leq A$。取 $\delta = x_0 - x_1$ 即得 $\lim\limits_{x \to x_0^-} f(x) = A$。2、3 类似。$\square$

于是，若 $f$ 在 $(a, b)$ 上单调非减，则对每个 $x_0 \in (a, b)$ 有 $f(x_0 - 0) \leq f(x_0) \leq f(x_0 + 0)$；单调非增时不等号反向。单调函数只可能有"跳跃"，这在[第 3 章](/2.2.3)讨论间断点时会用到。

**例 2.4.4（第二个重要极限）** 证明 $\lim\limits_{x \to \infty} \left(1 + \frac1x\right)^x = \mathrm{e}$。

**证明** 先设 $x \to +\infty$。记 $n = \lfloor x \rfloor$，则 $n \leq x < n + 1$，$n \to +\infty$，且

$$
\Bigl(1 + \frac1{n + 1}\Bigr)^n \leq \Bigl(1 + \frac1x\Bigr)^x \leq \Bigl(1 + \frac1n\Bigr)^{n+1}.
$$
其中右边 $= \left(1 + \frac1n\right)^n\left(1 + \frac1n\right)$，左边 $= \left(1 + \frac1{n+1}\right)^{n+1}\left(1 + \frac1{n+1}\right)^{-1}$。由定义 2.2.1，两边作为整数 $n$ 的数列都趋于 $\mathrm{e}$：任给 $\varepsilon > 0$，存在 $N_0$，使整数 $n > N_0$ 时两边都落在 $(\mathrm{e} - \varepsilon, \mathrm{e} + \varepsilon)$ 内。于是 $x > N_0 + 1$ 时 $n = \lfloor x \rfloor > N_0$，夹在中间的 $\left(1 + \frac1x\right)^x$ 也落在这个区间内，即 $\lim\limits_{x \to +\infty} \left(1 + \frac1x\right)^x = \mathrm{e}$。

再设 $x \to -\infty$，令 $z = -x \to +\infty$：

$$
\Bigl(1 + \frac1x\Bigr)^x = \Bigl(1 - \frac1z\Bigr)^{-z} = \Bigl(\frac{z}{z - 1}\Bigr)^z = \Bigl(1 + \frac1{z - 1}\Bigr)^{z-1}\Bigl(1 + \frac1{z-1}\Bigr) \to \mathrm{e}. \qquad \square
$$

变形可得以下常用形式：

$$
\lim_{x \to 0} (1 + x)^{1/x} = \mathrm{e}, \qquad \lim_{x \to \infty} \Bigl(1 - \frac1x\Bigr)^x = \frac1{\mathrm{e}}, \qquad \lim_{x \to 0} (1 - x)^{1/x} = \frac1{\mathrm{e}}.
$$

### 2.4.4. 复合函数的极限

**定理 2.4.4（复合极限定理）** 设 $\lim\limits_{t \to t_0} g(t) = x_0$，$\lim\limits_{x \to x_0} f(x) = A$，且在 $t_0$ 的某个去心邻域内 $g(t) \ne x_0$，则 $\lim\limits_{t \to t_0} f(g(t)) = A$。

**证明** 任给 $\varepsilon > 0$，存在 $\eta > 0$，当 $0 < |x - x_0| < \eta$ 时 $|f(x) - A| < \varepsilon$。对这个 $\eta$，存在 $\delta > 0$，当 $0 < |t - t_0| < \delta$ 时 $|g(t) - x_0| < \eta$，又 $g(t) \ne x_0$，故 $0 < |g(t) - x_0| < \eta$，从而 $|f(g(t)) - A| < \varepsilon$。$\square$

这就是求极限时"换元"的依据：令 $x = g(t)$，$\lim\limits_{t \to t_0} f(g(t)) = \lim\limits_{x \to x_0} f(x)$。条件 $g(t) \ne x_0$ 不能去掉：设 $f(x) = 1$（$x \ne 0$），$f(0) = 0$，$g(t) \equiv 0$，则 $\lim\limits_{x \to 0} f(x) = 1$，而 $f(g(t)) \equiv 0$。但若 $f$ 在 $x_0$ 处满足 $\lim\limits_{x \to x_0} f(x) = f(x_0)$（即连续，见[第 3 章](/2.2.3)），则这个条件可以去掉，结论写成 $\lim\limits_{t \to t_0} f(g(t)) = f\bigl(\lim\limits_{t \to t_0} g(t)\bigr)$。

**推论 2.4.1（幂指函数的极限）** 设 $\lim\limits_{x \to x_0} u(x) = a > 0$，$\lim\limits_{x \to x_0} v(x) = b$，则 $\lim\limits_{x \to x_0} u(x)^{v(x)} = a^b$。

**证明** $u(x)^{v(x)} = \mathrm{e}^{v(x)\ln u(x)}$。由例 2.4.2 与复合极限定理，$\ln u(x) \to \ln a$，故 $v(x)\ln u(x) \to b\ln a$；再用一次复合极限定理与 $\mathrm{e}^y$ 的极限，$\mathrm{e}^{v(x)\ln u(x)} \to \mathrm{e}^{b\ln a} = a^b$。$\square$

**例 2.4.5** 计算：(1) $\lim\limits_{x \to +\infty} \arcsin\frac{x - 1}{x + 1}$；(2) $\lim\limits_{x \to 0} \frac{\sin(\tan x)}{\sin x}$；(3) $\lim\limits_{x \to x_0} x^p$（$x_0 > 0$）。

**解** (1) 令 $u = \frac{x - 1}{x + 1} \to 1^-$，而 $\lim\limits_{u \to 1^-} \arcsin u = \frac\pi2$（例 2.3.4），故极限为 $\frac\pi2$。

(2) $\frac{\sin(\tan x)}{\sin x} = \frac{\sin(\tan x)}{\tan x} \cdot \frac{1}{\cos x}$。令 $u = \tan x$，$x \to 0$ 时 $u \to 0$ 且 $u \ne 0$，故第一个因子 $\to 1$，极限为 $1$。

(3) $x^p = \mathrm{e}^{p\ln x} \to \mathrm{e}^{p\ln x_0} = x_0^p$。

$u(x) \to 1$、$v(x) \to \infty$ 时 $u^v$ 是 $1^\infty$ 型不定式，推论 2.4.1 不适用，需要借助第二个重要极限。

**算法 2.4.1（$1^\infty$ 型极限）** 设 $u(x) \to 1$，$v(x) \to \infty$。

1. 写成 $u^v = \Bigl[\bigl(1 + (u - 1)\bigr)^{\frac1{u-1}}\Bigr]^{v(u - 1)}$；
2. 方括号内 $\to \mathrm{e}$（第二个重要极限与复合极限定理）；
3. 若 $\lim v(x)\bigl(u(x) - 1\bigr) = c$，则由推论 2.4.1，$\lim u^v = \mathrm{e}^c$。

**例 2.4.6** 计算：

$$
\text{(1)}\ \lim_{x \to 0} (1 + 2\sin x)^{\csc x}; \quad
\text{(2)}\ \lim_{x \to 0} (\cos 2x)^{1/x^2}; \quad
\text{(3)}\ \lim_{x \to \infty} \Bigl(\frac2{x^2} + \cos\frac1x\Bigr)^{x^2}; \quad
\text{(4)}\ \lim_{x \to \pi/4} (\tan x)^{\tan 2x}.
$$

**解** (1) $v(u - 1) = \csc x \cdot 2\sin x = 2$，极限为 $\mathrm{e}^2$。

(2) $\cos 2x - 1 = -2\sin^2 x$，$v(u - 1) = -\frac{2\sin^2 x}{x^2} \to -2$，极限为 $\mathrm{e}^{-2}$。

(3) 令 $t = \frac1x \to 0$，$v(u - 1) = \frac{2t^2 + \cos t - 1}{t^2} = 2 - \frac{2\sin^2(t/2)}{t^2} \to 2 - \frac12 = \frac32$，极限为 $\mathrm{e}^{3/2}$。

(4) $\tan 2x = \frac{2\tan x}{1 - \tan^2 x}$，故 $v(u - 1) = \frac{2\tan x(\tan x - 1)}{(1 - \tan x)(1 + \tan x)} = -\frac{2\tan x}{1 + \tan x} \to -1$，极限为 $\mathrm{e}^{-1}$。

**例 2.4.7** 设 $x \in \mathbb{R}$，求 $\lim\limits_{n \to \infty} \underbrace{\sin\sin\cdots\sin}_{n \text{ 重}} x$。

**解** 记 $a_n$ 为 $n$ 重复合，$a_n = \sin a_{n-1}$。若 $0 < x \leq \pi$，则 $a_1 = \sin x \in (0, 1]$，由 $0 < \sin t < t$（$t > 0$）归纳得 $0 < a_n < a_{n-1}$，$\{a_n\}$ 单调减少且有下界 $0$，收敛于某个 $\alpha \geq 0$。由 Heine 定理与 $\lim\limits_{t \to \alpha} \sin t = \sin\alpha$，在 $a_n = \sin a_{n-1}$ 两边取极限得 $\alpha = \sin\alpha$，只能 $\alpha = 0$。$\pi < x < 2\pi$ 时 $a_1 \in [-1, 0)$，由奇函数性同理 $a_n \to 0$；$x = k\pi$ 时 $a_n \equiv 0$。再由周期性，对一切 $x$ 极限都是 $0$。

## 2.5. 无穷小量与阶的比较

### 2.5.1. 无穷小量与无穷大量

**定义 2.5.1（无穷小量）** 若 $\lim\limits_{x \to \square} f(x) = 0$，则称 $x \to \square$ 时 $f(x)$ 为**无穷小量**，简称无穷小。

例如 $x \to 0$ 时 $x^2$、$\sin x$、$x\sin\frac1x$ 都是无穷小；$x \to \infty$ 时 $\frac1x$、$\frac1{\ln|x|}$ 是无穷小，$x \to +\infty$ 时 $\mathrm{e}^{-x}$ 是无穷小。说一个函数是无穷小，必须指明自变量的变化过程。

**定义 2.5.2（无穷大量）** 若 $x \to \square$ 时 $f(x)$（$-f(x)$，$|f(x)|$）无限增大，即 $\lim\limits_{x \to \square} f(x) = +\infty$（$-\infty$，$\infty$），则称 $x \to \square$ 时 $f(x)$ 为正无穷大量（负无穷大量，无穷大量）。

例如 $x \to 0^+$ 时 $\frac1x$ 是正无穷大，$x \to 0^-$ 时是负无穷大，$x \to 0$ 时是无穷大。要区分无界量与无穷大量：$x \to +\infty$ 时 $x\sin x$ 无界（在 $x = 2n\pi + \frac\pi2$ 处取值 $2n\pi + \frac\pi2$），但不是无穷大（在 $x = n\pi$ 处取值 $0$）。

**性质 2.5.1（无穷小与无穷大的运算）** 在同一变化过程 $x \to \square$ 中：

1. 两个无穷小的和、差、积都是无穷小，常数与无穷小的积是无穷小；
2. 两个无穷大的积是无穷大，非零常数与无穷大的积是无穷大；
3. $f(x)$ 是无穷小（且 $f(x) \ne 0$）当且仅当 $\frac1{f(x)}$ 是无穷大；
4. 无穷小与有界函数的积是无穷小。

两个无穷大的和不一定是无穷大（$x$ 与 $-x$），无穷小与无穷大的积可以是任何结果（$x^2 \cdot \frac1x$，$x \cdot \frac1x$，$x \cdot \frac1{x^2}$）：这些"不定式"留到[第 5 章](/2.2.5)用 L'Hôpital 法则处理。

### 2.5.2. 阶的比较

同是趋于 $0$，$x$、$x^2$、$\sin x$ 趋于 $0$ 的速度不同。用它们的比值的极限来比较快慢。

**定义 2.5.3（无穷小的阶）** 设 $x \to \square$ 时 $f(x)$、$g(x)$ 都是无穷小，且 $g(x) \ne 0$。

1. 若 $\lim\limits_{x \to \square} \frac{f(x)}{g(x)} = c \ne 0$，则称 $x \to \square$ 时 $f$ 与 $g$ 是**同阶无穷小**；特别地，若 $c = 1$，则称 $f$ 与 $g$ 是**等价无穷小**，记为 $f(x) \sim g(x)$（$x \to \square$）。
2. 若 $\lim\limits_{x \to \square} \frac{f(x)}{g(x)} = 0$，则称 $x \to \square$ 时 $f$ 是 $g$ 的**高阶无穷小**，记为 $f(x) = o\bigl(g(x)\bigr)$（$x \to \square$）。

例如 $x \to 0$ 时 $\sin x \sim x$，$1 - \cos x$ 与 $x^2$ 同阶，$x^2 = o(x)$。记号 $o(g)$ 表示"某个比 $g$ 高阶的无穷小"，不是一个确定的函数，因此 $o(x) - o(x) = o(x)$，而不是 $0$。等价无穷小与高阶无穷小的关系是

$$
f(x) \sim g(x) \iff f(x) = g(x) + o\bigl(g(x)\bigr) \quad (x \to \square), \tag{2.3}
$$
因为 $\frac fg \to 1$ 与 $\frac{f - g}{g} \to 0$ 等价。式 (2.3) 把等价关系写成"主部加高阶余项"，这就是[第 5 章](/2.2.5) Taylor 公式的思想。

**例 2.5.1** 证明 $x \to 0$ 时 $\ln(1 + x) \sim x$，$\mathrm{e}^x - 1 \sim x$，$a^x - 1 \sim x\ln a$（$a > 0$，$a \ne 1$）。

**证明** 由推论 2.4.1 与 $(1 + x)^{1/x} \to \mathrm{e}$，$\frac{\ln(1 + x)}{x} = \ln(1 + x)^{1/x} \to \ln\mathrm{e} = 1$。令 $u = \mathrm{e}^x - 1$，则 $x = \ln(1 + u)$，$x \to 0$ 时 $u \to 0$ 且 $u \ne 0$，故 $\frac{\mathrm{e}^x - 1}{x} = \frac{u}{\ln(1 + u)} \to 1$。最后 $\frac{a^x - 1}{x\ln a} = \frac{\mathrm{e}^{x\ln a} - 1}{x\ln a} \to 1$。$\square$

由此及 §2.4.2，得到常用的等价无穷小（$x \to 0$）：

| 无穷小 | 等价于 | 无穷小 | 等价于 |
|---|---|---|---|
| $\sin x$，$\tan x$ | $x$ | $\ln(1 + x)$ | $x$ |
| $\arcsin x$，$\arctan x$ | $x$ | $\mathrm{e}^x - 1$ | $x$ |
| $1 - \cos x$ | $\frac12 x^2$ | $a^x - 1$ | $x\ln a$ |
| $(1 + x)^\alpha - 1$（$\alpha \in \mathbb{R}$，$\alpha \ne 0$） | $\alpha x$ | $\sqrt[k]{1 + x} - 1$ | $\frac xk$ |

其中 $(1 + x)^\alpha - 1 = \mathrm{e}^{\alpha\ln(1 + x)} - 1 \sim \alpha\ln(1 + x) \sim \alpha x$，对任意实数 $\alpha \ne 0$ 都成立；表中 $x$ 可以换成任何趋于 $0$ 的函数 $u(x)$，例如 $x \to 0$ 时 $\sin x^2 \sim x^2$。

**定理 2.5.1（等价无穷小替换）** 设 $x \to \square$ 时 $f(x) \sim g(x)$，则

$$
\lim_{x \to \square} f(x)h(x) = \lim_{x \to \square} g(x)h(x), \qquad \lim_{x \to \square} \frac{h(x)}{f(x)} = \lim_{x \to \square} \frac{h(x)}{g(x)},
$$
即一边的极限存在（或为 $\infty$）时，另一边的极限也存在且相等。

**证明** $f(x)h(x) = \frac{f(x)}{g(x)} \cdot g(x)h(x)$，而 $\frac fg \to 1$，由四则运算即得第一式；第二式同理。$\square$

因此求极限时，乘除中的无穷小因子可以换成与之等价的、更简单的无穷小。但加减中的项不能随意替换：替换只对整个因子成立。

**例 2.5.2** 计算 $\lim\limits_{x \to 0} \frac{\tan x - \sin x}{x^3}$。

**解** 先把分子化成乘积：$\tan x - \sin x = \tan x\,(1 - \cos x)$，再对因子替换：

$$
\lim_{x \to 0} \frac{\tan x\,(1 - \cos x)}{x^3} = \lim_{x \to 0} \frac{x \cdot \frac12x^2}{x^3} = \frac12.
$$
若直接把 $\tan x$、$\sin x$ 都换成 $x$，会得到错误的答案 $0$：$\tan x - \sin x$ 的主部是 $\frac12x^3$，替换丢掉的高阶项恰好决定了结果。

**例 2.5.3** 计算 $\lim\limits_{x \to 0} \frac{\sqrt[3]{1 + x^4} - \sqrt[4]{1 - 2x^4}}{\tan x\,\sin x\,(1 - \cos x)}$。

**解** 分母 $\sim x \cdot x \cdot \frac12x^2 = \frac12x^4$。分子拆成两个分别有极限的部分：

$$
\lim_{x \to 0} \frac{\sqrt[3]{1 + x^4} - 1}{\frac12x^4} + \lim_{x \to 0} \frac{1 - \sqrt[4]{1 - 2x^4}}{\frac12x^4} = \frac{\frac13}{\frac12} + \frac{\frac12}{\frac12} = \frac23 + 1 = \frac53.
$$
这里先用四则运算把分子拆开（拆开后的两个极限都存在），再在每个分式中对因子做等价替换，因而是正确的。

无穷大也可以比较阶：设 $x \to \square$ 时 $f, g$ 都是无穷大，若 $\lim\frac fg = c \ne 0$，称 $f$ 与 $g$ 是同阶无穷大；若 $\lim\frac fg = 0$，称 $g$ 是比 $f$ 高阶的无穷大。由 §2.2 的例子，$n \to \infty$ 时

$$
\ln n \ll n^\alpha \ (\alpha > 0) \ll a^n \ (a > 1) \ll n! \ll n^n,
$$
其中 $f \ll g$ 表示 $g$ 是比 $f$ 高阶的无穷大（$\frac{\ln n}{n^\alpha} \to 0$ 的证明见[第 5 章](/2.2.5)）。

## 小结

| 内容 | 要点 |
|---|---|
| 数列极限 | $\forall \varepsilon > 0$，$\exists N$，$n > N \implies |a_n - A| < \varepsilon$；邻域外只有有限项 |
| 函数极限 | $\forall \varepsilon > 0$，$\exists \delta > 0$，$0 < |x - x_0| < \delta \implies |f(x) - A| < \varepsilon$；与 $f(x_0)$ 无关；六种过程 |
| 性质 | 唯一性、（局部）有界性、（局部）保号性、保序性；取极限时 $>$ 可能变为 $\geq$ |
| 子列与 Heine 定理 | 收敛 $\iff$ 一切子列（一切 $x_n \to x_0$）趋于同一极限；常用于证明不存在 |
| 四则运算 | 前提是各部分的极限都存在；项数随 $n$ 增加的和不能逐项取极限 |
| 存在判据 | 夹逼定理；单调收敛定理（单调有界必收敛）；Cauchy 收敛准则（收敛 $\iff$ Cauchy 数列） |
| 基本极限 | $q^n \to 0$，$\sqrt[n]a \to 1$，$\sqrt[n]n \to 1$，$\frac{n^k}{a^n} \to 0$；$\frac{\sin x}x \to 1$，$\left(1 + \frac1x\right)^x \to \mathrm{e}$ |
| 复合与幂指 | 换元需 $g(t) \ne x_0$（或 $f$ 连续）；$u^v \to a^b$（$a > 0$）；$1^\infty$ 型：$\lim u^v = \mathrm{e}^{\lim v(u - 1)}$ |
| 无穷小的阶 | 同阶、等价（$\sim$）、高阶（$o$）；$f \sim g \iff f = g + o(g)$ |
| 等价替换 | 只在乘除的因子中替换；常用表：$\sin x, \tan x, \ln(1 + x), \mathrm{e}^x - 1 \sim x$，$1 - \cos x \sim \frac12x^2$，$(1 + x)^\alpha - 1 \sim \alpha x$ |
| 方法 | 算法 2.1.1（$\varepsilon$-$N$ 验证）、算法 2.2.1（递推数列）、算法 2.4.1（$1^\infty$ 型） |
