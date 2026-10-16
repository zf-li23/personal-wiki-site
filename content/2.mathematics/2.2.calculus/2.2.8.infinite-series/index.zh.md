---
title: 数项级数
---

无穷多个数相加有没有意义？$1 + \frac12 + \frac14 + \cdots$ 应当等于 $2$，而 $1 - 1 + 1 - 1 + \cdots$ 似乎什么都不等于。本章把无穷和定义为部分和**数列**的极限，于是级数的收敛就是[第 2 章](/2.2.2)的数列极限，**Cauchy 收敛准则**、**单调收敛定理**都可以直接使用。

本章的主线是判断收敛性，按级数的类型分两步。8.2 讨论各项非负的正项级数：部分和单调，收敛当且仅当有界，由此得到比较判别法、比值与根值判别法、积分判别法；它们与[第 7 章](/2.2.7) 7.7 节的反常积分判别法几乎一一对应（$p$ 级数对应 $\int_1^{+\infty}x^{-p}\,\mathrm{d}x$）。8.3 讨论一般的级数：交错级数的 Leibniz 判别法、绝对收敛与条件收敛的区别，以及 Abel、Dirichlet 判别法。绝对收敛的级数可以像有限和一样任意交换次序、相乘；条件收敛的级数则不行，重排可以改变它的和。下一章把这些结论推广到每一项都是函数的级数，那里会用到本章的全部判别法。

## 8.1. 数项级数的概念和性质

### 8.1.1. 基本概念

**定义 8.1.1（级数）** 设 $\{u_n\}$ 是一个数列，称

$$
\sum_{n=1}^\infty u_n = u_1 + u_2 + \cdots + u_n + \cdots
$$
为（数项）级数，$u_n$ 称为它的通项或一般项。称 $S_n = u_1 + \cdots + u_n$ 为级数的前 $n$ 项**部分和**，$\{S_n\}$ 为部分和数列。若 $\lim_{n\to\infty}S_n = S$ 存在，则称级数收敛，$S$ 称为级数的和，记作 $\sum_{n=1}^\infty u_n = S$；否则称级数发散。

级数与数列可以互相转换：$u_n = S_n - S_{n-1}$。所以级数理论不是新的极限理论，而是用通项 $u_n$（而不是部分和）来判断部分和数列是否收敛。

**例 8.1.1** $\sum_{n=1}^\infty\frac{1}{n(n+1)}$：由 $\frac{1}{n(n+1)} = \frac1n - \frac{1}{n+1}$，部分和 $S_n = 1 - \frac{1}{n+1} \to 1$，级数收敛，和为 $1$。这种相邻项相消的求和叫作裂项相消。

**例 8.1.2** $\sum_{n=1}^\infty\frac{1}{\sqrt n}$：$S_n \ge n\cdot\frac{1}{\sqrt n} = \sqrt n \to +\infty$，级数发散，尽管通项趋于 $0$。

### 8.1.2. 级数的性质

**性质 8.1.1（收敛的必要条件）** 若 $\sum u_n$ 收敛，则 $\lim_{n\to\infty}u_n = 0$。

**证明** $u_n = S_n - S_{n-1} \to S - S = 0$。$\square$

逆命题不成立（例 8.1.2）。常用的是逆否形式：通项不趋于 $0$ 的级数一定发散，例如 $\sum(-1)^n$、$\sum\frac{n}{2n+1}$。

**性质 8.1.2（线性）** 若 $\sum u_n$、$\sum v_n$ 收敛，则对常数 $\alpha, \beta$，$\sum(\alpha u_n + \beta v_n)$ 收敛，且 $\sum(\alpha u_n + \beta v_n) = \alpha\sum u_n + \beta\sum v_n$。

**性质 8.1.3（结合律）** 若 $\sum u_n$ 收敛，则不改变各项顺序、任意加括号后得到的级数仍收敛，且和不变。

**证明** 加括号后的级数的部分和数列是 $\{S_n\}$ 的一个**子列**，收敛数列的子列收敛到同一极限。$\square$

逆命题不成立：$\sum_{n=1}^\infty(-1)^n$ 发散，但 $\sum_{k=1}^\infty\bigl[(-1)^{2k-1} + (-1)^{2k}\bigr] = 0$ 收敛。所以发散级数不能随意加括号，收敛级数不能随意去括号。

**性质 8.1.4** 增加、删除或改变级数的有限项，不改变级数的敛散性（但收敛时可能改变和）。

**证明** 由数列的 **Cauchy 收敛准则**，$\sum u_n$ 收敛 $\iff$ 对任意 $\varepsilon > 0$，存在 $N$，当 $n > m > N$ 时 $|S_n - S_m| = |u_{m+1} + \cdots + u_n| < \varepsilon$。这个条件只涉及充分靠后的项。$\square$

### 8.1.3. 几何级数与 p 级数

两类最基本的级数是后面各种比较判别法的"标尺"。

设 $a \ne 0$，称 $\sum_{n=1}^\infty aq^{n-1} = a + aq + aq^2 + \cdots$ 为几何级数（geometric series），也叫等比级数。$q \ne 1$ 时 $S_n = \frac{a(1 - q^n)}{1 - q}$，于是

- $|q| < 1$ 时级数收敛，和为 $\dfrac{a}{1-q}$；
- $|q| \ge 1$ 时通项不趋于 $0$，级数发散。

设 $p$ 为常数，称 $\sum_{n=1}^\infty\frac{1}{n^p} = 1 + \frac{1}{2^p} + \frac{1}{3^p} + \cdots$ 为 p 级数（p-series）；$p = 1$ 时的 $\sum\frac1n$ 称为调和级数（harmonic series）。

**定理 8.1.1** $p$ 级数当 $p > 1$ 时收敛，当 $p \le 1$ 时发散。

**证明** $p \le 0$ 时通项不趋于 $0$。设 $p > 0$，$x^{-p}$ 单调减少，于是对 $k \ge 2$，

$$
\int_k^{k+1}\frac{\mathrm{d}x}{x^p} \le \frac{1}{k^p} \le \int_{k-1}^k\frac{\mathrm{d}x}{x^p}.
$$

$p > 1$ 时，$S_n \le 1 + \int_1^n x^{-p}\,\mathrm{d}x \le 1 + \frac{1}{p-1}$，正项级数的部分和单调增加且有上界，收敛。$0 < p \le 1$ 时，$S_n \ge \int_1^{n+1}x^{-p}\,\mathrm{d}x \to +\infty$（**无穷积分**发散），级数发散。$\square$

这个证明的思路在 8.2.3 节推广为积分判别法。对调和级数，它还给出 $\ln(n+1) \le 1 + \frac12 + \cdots + \frac1n \le 1 + \ln n$：调和级数发散，但发散得极慢，前一百万项之和还不到 $15$。

## 8.2. 正项级数的收敛判别法

**定义 8.2.1（正项级数）** 每一项都非负的级数称为正项级数。

正项级数的部分和数列单调不减，由**单调收敛定理**：

$$
\text{正项级数收敛} \iff \text{部分和数列有上界}.
$$

正项级数只有收敛到有限和、发散到 $+\infty$ 两种可能，下面的判别法都建立在这个事实上。$p$ 级数、几何级数（$a > 0$，$q \ge 0$）都是正项级数。

### 8.2.1. 比较判别法和比阶判别法

以下 $\sum u_n$、$\sum v_n$ 都是正项级数。

**定理 8.2.1（比较判别法）** 设存在 $M > 0$ 与正整数 $N$，当 $n > N$ 时 $u_n \le Mv_n$。

1. 若 $\sum v_n$ 收敛，则 $\sum u_n$ 收敛；
2. 若 $\sum u_n$ 发散，则 $\sum v_n$ 发散。

**证明** 由性质 8.1.4 不妨设对一切 $n$ 都有 $u_n \le Mv_n$，则 $\sum_{k=1}^n u_k \le M\sum_{k=1}^\infty v_k$，部分和有上界。2 是 1 的逆否命题。$\square$

**例 8.2.1**

1. $\sum\frac{3}{n^2 - 5n + 5}$：$n \ge 9$ 时 $n^2 - 5n + 5 \ge \frac{n^2}{2}$，于是通项 $\le \frac{6}{n^2}$，由 $\sum\frac1{n^2}$ 收敛知它收敛。
2. $\sum\frac{1}{\sqrt{n^2 + 2n + 100}}$：$n \ge 2$ 时 $n^2 + 2n + 100 \le 100n^2$，通项 $\ge \frac{1}{10n}$，由调和级数发散知它发散。
3. $\sum\frac{n!}{n^n}$：$\frac{n!}{n^n} = \frac1n\cdot\frac2n\cdots\frac nn \le \frac{2}{n^2}$（$n \ge 2$），收敛。

取 $p$ 级数作比较对象，得到：

**推论 8.2.1（比阶判别法）** 设 $\sum u_n$ 是正项级数，$M > 0$。

1. 若存在 $p > 1$，使 $n$ 充分大时 $u_n \le \frac{M}{n^p}$，则 $\sum u_n$ 收敛；
2. 若存在 $p \le 1$，使 $n$ 充分大时 $u_n \ge \frac{M}{n^p}$，则 $\sum u_n$ 发散。

不等式往往不好直接写出，极限形式更方便：只需比较通项趋于零的速度。

**定理 8.2.2（比较判别法的极限形式）** 设 $v_n > 0$，$\lim_{n\to\infty}\frac{u_n}{v_n} = q$。

1. 若 $0 \le q < +\infty$ 且 $\sum v_n$ 收敛，则 $\sum u_n$ 收敛；
2. 若 $0 < q \le +\infty$ 且 $\sum v_n$ 发散，则 $\sum u_n$ 发散。

特别地，$0 < q < +\infty$ 时两者同敛散；当 $u_n$ 与 $v_n$ 是**等价无穷小**时更是如此。

**证明** 1. $n$ 充分大时 $u_n/v_n < q + 1$，由定理 8.2.1。2. $q < +\infty$ 时 $n$ 充分大有 $u_n > \frac q2v_n$，$q = +\infty$ 时 $u_n > v_n$，由定理 8.2.1。$\square$

**例 8.2.2**

1. $\sum 2^n\sin\frac{1}{3^n}$：$\lim\frac{2^n\sin(1/3^n)}{(2/3)^n} = 1$，几何级数 $\sum(2/3)^n$ 收敛，故收敛。
2. $\sum\ln\left(1 + \frac1n\right)$：$\ln(1 + \frac1n) \sim \frac1n$，发散。
3. $\sum\ln\left(2 - \cos\frac1n\right)$：$\ln\left(1 + \left(1 - \cos\frac1n\right)\right) \sim 1 - \cos\frac1n \sim \frac{1}{2n^2}$，收敛。

**推论 8.2.2（比阶判别法的极限形式）** 设 $\sum u_n$ 是正项级数。

1. 若存在 $p > 1$，使 $\lim_{n\to\infty}n^pu_n$ 存在（有限），则 $\sum u_n$ 收敛；
2. 若存在 $p \le 1$，使 $\lim_{n\to\infty}n^pu_n$ 存在且不为零，或为 $+\infty$，则 $\sum u_n$ 发散。

它与无穷积分的比阶判别法（[定理 7.7.5](/2.2.7#thm-7.7.5)）完全平行：通项是比 $\frac1n$ 更高阶的无穷小（至少像 $n^{-p}$，$p > 1$）时收敛。

**例 8.2.3**

1. $\sum\frac{\ln n}{n^p}$（$p > 1$）：取 $1 < q < p$，$n^q\cdot\frac{\ln n}{n^p} = \frac{\ln n}{n^{p-q}} \to 0$，收敛。对数因子不影响"幂次严格大于 1"的判断。
2. $\sum\frac{1}{\sqrt[3]{n^2 + n + 7}}$：$n^{2/3}u_n \to 1$，$p = \frac23 \le 1$，发散。
3. $\sum\frac{1}{\sqrt n}\tan\frac1n$：$n^{3/2}u_n \to 1$，收敛。

**例 8.2.4** $\sum\left[\frac1n - \ln\left(1 + \frac1n\right)\right]$：由**泰勒公式** $\ln(1 + x) = x - \frac{x^2}{2} + o(x^2)$，通项 $= \frac{1}{2n^2} + o\left(\frac{1}{n^2}\right) > 0$，$n^2u_n \to \frac12$，收敛。由此 $1 + \frac12 + \cdots + \frac1n - \ln(n+1) = \sum_{k=1}^n\left[\frac1k - \ln\left(1 + \frac1k\right)\right]$ 收敛，其极限就是 Euler 常数 $\gamma \approx 0.5772$。

用 Taylor 公式求通项的主部，再用比阶判别法，是判断这类级数最有效的方法。

### 8.2.2. 比值判别法与根值判别法

与自身比较：若 $u_n$ 像几何级数那样衰减，相邻项之比或 $n$ 次根就会稳定在某个小于 $1$ 的数附近。

**定理 8.2.3（比值判别法）** 设 $u_n > 0$，$\lim_{n\to\infty}\frac{u_{n+1}}{u_n} = q$（或 $+\infty$）。

1. 若 $q < 1$，则 $\sum u_n$ 收敛；
2. 若 $q > 1$ 或 $q = +\infty$，则 $\sum u_n$ 发散。

$q = 1$ 时不能判断。

**证明** 1. 取 $r$ 满足 $q < r < 1$，存在 $N$ 使 $n > N$ 时 $\frac{u_{n+1}}{u_n} < r$，于是 $u_{N+k} \le u_{N+1}r^{k-1}$，由比较判别法与几何级数 $\sum r^k$ 的收敛得证。2. 取 $1 < r < q$，$n$ 充分大时 $u_{n+1} > ru_n > u_n$，通项单调增加、不趋于零，发散。$\square$

**例 8.2.5**

1. $\sum\frac{n^2}{3^n}$：$\frac{u_{n+1}}{u_n} = \frac{(n+1)^2}{3n^2} \to \frac13$，收敛。
2. $\sum\frac{1}{3^n - n^3}$：比值 $\to \frac13$，收敛。
3. $\sum\frac{(n!)^2}{(2n)!}$：$\frac{u_{n+1}}{u_n} = \frac{(n+1)^2}{(2n+2)(2n+1)} \to \frac14$，收敛。

含阶乘、指数的通项适合用比值判别法。$q = 1$ 时它失效：$\sum\frac1n$ 与 $\sum\frac1{n^2}$ 的比值极限都是 $1$，前者发散、后者收敛，此时改用比阶判别法。

**定理 8.2.4（根值判别法）** 设 $u_n \ge 0$，$\lim_{n\to\infty}\sqrt[n]{u_n} = q$（或 $+\infty$）。

1. 若 $q < 1$，则 $\sum u_n$ 收敛；
2. 若 $q > 1$ 或 $q = +\infty$，则 $\sum u_n$ 发散。

$q = 1$ 时不能判断。

**证明** 1. 取 $q < r < 1$，$n$ 充分大时 $u_n < r^n$，与几何级数比较。2. $n$ 充分大时 $u_n > 1$，通项不趋于零。$\square$

**例 8.2.6**

1. $\sum\frac{n^2}{3^n + 2^n}$：$\sqrt[n]{u_n} \to \frac13$，收敛。
2. $\sum\left(\frac{n+1}{n}\right)^{n^2}\frac{1}{3^n}$：$\sqrt[n]{u_n} = \left(1 + \frac1n\right)^n\cdot\frac13 \to \frac{\mathrm{e}}{3} < 1$，收敛。
3. $\sum\frac{n\,[\sqrt2 + (-1)^n]^n}{3^n}$：通项 $\le \frac{n(\sqrt2 + 1)^n}{3^n}$，后者的 $n$ 次根 $\to \frac{\sqrt2 + 1}{3} < 1$，由比较判别法收敛。这里相邻项之比 $u_{n+1}/u_n$ 在 $n$ 为奇数、偶数时分别趋于 $+\infty$ 与 $0$，比值判别法无法使用。

一般地，比值极限存在时根值极限也存在且相等，所以根值判别法适用的范围更广；但比值往往更容易计算。两者都只能判断"像几何级数一样快"收敛的级数，对 $p$ 级数一类的级数总是 $q = 1$。

### 8.2.3. 积分判别法

定理 8.1.1 的证明把级数与无穷积分夹在一起，一般化就是：

**定理 8.2.7（积分判别法）** 设 $f$ 在 $[1, +\infty)$ 上连续、非负且单调减少，$u_n = f(n)$，则

$$
\sum_{n=1}^\infty u_n \text{ 收敛} \iff \int_1^{+\infty}f(x)\,\mathrm{d}x \text{ 收敛}.
$$

**证明** 由单调性，$u_k \le \int_{k-1}^k f(x)\,\mathrm{d}x \le u_{k-1}$（$k \ge 2$）。对 $k = 2, \dots, n$ 求和，记 $S_n = \sum_{k=1}^n u_k$，$Y_n = \int_1^n f$，得

$$
S_n - u_1 \le Y_n \le S_{n-1}.
$$

$\{S_n\}$ 与 $\{Y_n\}$ 都单调不减，由上式，一个有界当且仅当另一个有界。又 $f \ge 0$，$\int_1^A f$ 关于 $A$ 单调，故 $\int_1^{+\infty}f$ 收敛 $\iff \{Y_n\}$ 有界。$\square$

![积分判别法：f(n) 构成的两组矩形把曲线下的面积夹在中间，p = 1 时级数与积分同时发散，p = 2 时同时收敛](./plots/integral-test.py)

**例 8.2.7** Bertrand 级数 $\sum_{n=2}^\infty\frac{1}{n(\ln n)^p}$ 收敛当且仅当 $p > 1$（起点改为 $2$ 不影响证明）。

**证明** $f(x) = \frac{1}{x(\ln x)^p}$ 在 $[2, +\infty)$ 上非负，$p \ge 0$ 时单调减少（$p < 0$ 时级数的通项 $\ge \frac1n$，显然发散）。令 $u = \ln x$，$\int_2^{+\infty}\frac{\mathrm{d}x}{x(\ln x)^p} = \int_{\ln2}^{+\infty}\frac{\mathrm{d}u}{u^p}$，它收敛当且仅当 $p > 1$。$\square$

$\sum\frac{1}{n\ln n}$ 发散，但它的通项比 $\frac1n$ 更快地趋于零：比阶判别法对它失效（$n^pu_n$ 在 $p > 1$ 时趋于 $+\infty$，在 $p \le 1$ 时趋于 $0$，两条都不适用），积分判别法则能判断。

## 8.3. 任意项级数

各项符号不定时，部分和不再单调。最简单的情形是正负交替。

### 8.3.1. 交错级数

**定义 8.3.1（交错级数）** 设 $u_n > 0$，称 $\sum_{n=1}^\infty(-1)^{n-1}u_n = u_1 - u_2 + u_3 - \cdots$ 为交错级数。

**定理 8.3.1（Leibniz 判别法）** 若交错级数 $\sum(-1)^{n-1}u_n$ 中 $\{u_n\}$ 单调减少且 $u_n \to 0$，则

1. $\sum(-1)^{n-1}u_n$ 收敛；
2. 其和 $S$ 满足 $0 \le S \le u_1$；
3. 余项 $r_n = \sum_{k=n+1}^\infty(-1)^{k-1}u_k$ 满足 $|r_n| \le u_{n+1}$。

**证明** 1. 偶数项部分和 $S_{2n+2} = S_{2n} + (u_{2n+1} - u_{2n+2}) \ge S_{2n}$，单调增加；又

$$
S_{2n} = u_1 - (u_2 - u_3) - \cdots - (u_{2n-2} - u_{2n-1}) - u_{2n} \le u_1,
$$
有上界，故 $S_{2n} \to S$。$S_{2n-1} = S_{2n} + u_{2n} \to S$。奇偶子列极限相同，$S_n \to S$。

2. 由 $0 \le S_{2n} \le u_1$ 取极限。

3. $r_n = (-1)^n(u_{n+1} - u_{n+2} + \cdots)$，括号内是满足同样条件的交错级数，由 2 得 $|r_n| \le u_{n+1}$。$\square$

余项估计说明：用部分和近似交错级数的和，误差不超过第一个被略去的项。例如 $\sum\frac{(-1)^{n-1}}{n} = \ln2$（[第 9 章](/2.2.9)），取前 $1000$ 项误差小于 $10^{-3}$。

**例 8.3.1** $\sum\frac{(-1)^n}{n}$、$\sum\frac{(-1)^n}{\sqrt n}$、$\sum_{n=2}^\infty\frac{(-1)^n}{n\ln n}$ 都满足 Leibniz 判别法的条件，因而收敛。

单调性不能省略：$u_{2k-1} = \frac1k$，$u_{2k} = \frac{1}{k^2}$ 时 $u_n \to 0$，但 $\sum(-1)^{n-1}u_n$ 的前 $2n$ 项之和 $= \sum_{k=1}^n\left(\frac1k - \frac1{k^2}\right) \to +\infty$。

### 8.3.2. 绝对收敛与条件收敛

**定理 8.3.2（级数的 Cauchy 收敛准则）** $\sum u_n$ 收敛 $\iff$ 对任意 $\varepsilon > 0$，存在正整数 $N$，当 $n > N$ 时，对一切正整数 $p$，

$$
|u_{n+1} + u_{n+2} + \cdots + u_{n+p}| < \varepsilon.
$$

**证明** 这就是部分和数列 $\{S_n\}$ 的 **Cauchy 收敛准则**：$|S_{n+p} - S_n| < \varepsilon$。$\square$

**定义 8.3.2（绝对收敛）** 若 $\sum|u_n|$ 收敛，则称 $\sum u_n$ **绝对收敛**；若 $\sum u_n$ 收敛而 $\sum|u_n|$ 发散，则称 $\sum u_n$ **条件收敛**。

这与 7.7.3 节反常积分的绝对收敛、条件收敛是同一个概念：级数可以看成阶梯函数的无穷积分。

**定理 8.3.3** 绝对收敛的级数必收敛。

**证明** $|u_{n+1} + \cdots + u_{n+p}| \le |u_{n+1}| + \cdots + |u_{n+p}|$，由定理 8.3.2。$\square$

于是判断一般级数时，先看 $\sum|u_n|$：它是正项级数，8.2 节的判别法都可以用；若 $\sum|u_n|$ 发散，再用 Leibniz 判别法或 8.3.4 节的判别法判断是否条件收敛。

**例 8.3.2** $\sum\frac{(-1)^n}{n}$、$\sum\frac{(-1)^n}{\sqrt n}$、$\sum\frac{(-1)^n}{\ln(n+1)}$ 都条件收敛；$\sum\frac{(-1)^n}{n^2}$、$\sum\frac{(-1)^n}{n\sqrt n}$、$\sum\frac{(-1)^n}{n^p\ln n}$（$p > 1$）都绝对收敛。

**例 8.3.3** 讨论 $\sum_{n=1}^\infty(-1)^n\frac{a^n}{n^p}$（$p > 0$）的敛散性。

**解** 对 $\sum\frac{|a|^n}{n^p}$ 用比值判别法，$\frac{|u_{n+1}|}{|u_n|} = \frac{n^p}{(n+1)^p}|a| \to |a|$。

| 情形 | 结论 | 理由 |
|---|---|---|
| $\lvert a\rvert < 1$ | 绝对收敛 | 比值判别法 |
| $\lvert a\rvert > 1$ | 发散 | 通项不趋于 $0$ |
| $a = 1$：$\sum\frac{(-1)^n}{n^p}$ | $p > 1$ 绝对收敛；$0 < p \le 1$ 条件收敛 | $p$ 级数；Leibniz 判别法 |
| $a = -1$：$\sum\frac{1}{n^p}$ | $p > 1$ 收敛（绝对收敛）；$0 < p \le 1$ 发散 | $p$ 级数 |

### 8.3.3. 绝对收敛级数的性质

有限和可以随意交换次序、加括号、相乘展开。对无穷和，绝对收敛恰好是保证这些运算合法的条件。

**性质 8.3.1** 若 $\sum u_n$、$\sum v_n$ 都绝对收敛，则 $\sum(au_n + bv_n)$ 也绝对收敛。

**证明** $|au_n + bv_n| \le |a||u_n| + |b||v_n|$，由比较判别法。$\square$

**性质 8.3.2（交换律）** 若 $\sum u_n$ 绝对收敛，则任意交换求和次序得到的级数 $\sum v_n$（$v_n = u_{i_n}$，$n \mapsto i_n$ 是正整数集上的一个**双射**）也绝对收敛，且和不变。

**证明** 1. 先设 $u_n \ge 0$。记 $m = \max\{i_1, \dots, i_n\}$，则 $\sum_{k=1}^n v_k \le S_m \le \sum_{k=1}^\infty u_k$，故 $\sum v_n$ 收敛且 $\sum v_n \le \sum u_n$；反过来 $\sum u_n$ 也是 $\sum v_n$ 的重排，$\sum u_n \le \sum v_n$。

2. 一般情形，令 $p_n = \frac{|u_n| + u_n}{2}$，$q_n = \frac{|u_n| - u_n}{2}$，则 $u_n = p_n - q_n$，$0 \le p_n, q_n \le |u_n|$，$\sum p_n$、$\sum q_n$ 都收敛。$\sum v_n$ 的正部与负部分别是 $\sum p_n$、$\sum q_n$ 的重排，由 1，$\sum v_n = \sum p_{i_n} - \sum q_{i_n} = \sum p_n - \sum q_n = \sum u_n$。$\square$

条件收敛的级数不满足交换律。交错调和级数 $1 - \frac12 + \frac13 - \frac14 + \cdots = \ln2$ 条件收敛，把它重排为"一个正项、两个负项"：

$$
\left(1 - \frac12\right) - \frac14 + \left(\frac13 - \frac16\right) - \frac18 + \cdots + \left(\frac{1}{2k-1} - \frac{1}{2(2k-1)}\right) - \frac{1}{4k} + \cdots = \frac12\left(1 - \frac12 + \frac13 - \frac14 + \cdots\right) = \frac12\ln2.
$$

![调和级数、1/n^2 与交错调和级数的部分和（左）；交错调和级数重排后收敛到原来的一半（右）](./plots/partial-sums.py)

事实上条件收敛级数可以重排出任何结果。

**定理 8.3.4（Riemann 重排定理）** 若 $\sum u_n$ 条件收敛，则对任意 $S \in [-\infty, +\infty]$，存在 $\sum u_n$ 的一个重排，其和为 $S$；也存在使部分和振荡发散的重排。

证明的思想：条件收敛时正项之和与负项之和都发散到无穷（否则 $\sum|u_n|$ 收敛或 $\sum u_n$ 发散），而 $u_n \to 0$。于是先取正项直到部分和超过 $S$，再取负项直到低于 $S$，如此往复，部分和在 $S$ 两侧的摆动幅度不超过最后取的那一项，趋于零。

绝对收敛级数还可以像多项式一样相乘。把 $\left(\sum_{n=0}^\infty u_n\right)\left(\sum_{n=0}^\infty v_n\right)$ 展开，得到所有乘积 $u_iv_j$，按 $i + j$ 分组就是：

**定义 8.3.3（Cauchy 乘积）** 级数 $\sum_{n=0}^\infty u_n$ 与 $\sum_{n=0}^\infty v_n$ 的 Cauchy 乘积是 $\sum_{n=0}^\infty c_n$，其中 $c_n = \sum_{k=0}^n u_kv_{n-k} = u_0v_n + u_1v_{n-1} + \cdots + u_nv_0$。

**性质 8.3.3** 若 $\sum u_n = U$、$\sum v_n = V$ 都绝对收敛，则它们的 Cauchy 乘积 $\sum c_n$ 也绝对收敛，且 $\sum c_n = UV$。

两个幂级数相乘（[第 9 章](/2.2.9)）就是 Cauchy 乘积：$\sum a_nx^n\cdot\sum b_nx^n = \sum\left(\sum_{k=0}^n a_kb_{n-k}\right)x^n$。绝对收敛的条件不能随意去掉：$\sum_{n=0}^\infty\frac{(-1)^n}{\sqrt{n+1}}$ 条件收敛，但它与自身的 Cauchy 乘积满足 $|c_n| = \sum_{k=0}^n\frac{1}{\sqrt{(k+1)(n-k+1)}} \ge \sum_{k=0}^n\frac{2}{n+2} = \frac{2(n+1)}{n+2}$（**算术–几何平均不等式**），通项不趋于零，发散。

**例 8.3.4** 证明 $\left(\sum_{n=0}^\infty\frac{1}{n!}\right)\left(\sum_{n=0}^\infty\frac{(-1)^n}{n!}\right) = 1$。

**证明** 两个级数都绝对收敛（比值判别法）。Cauchy 乘积的通项 $c_0 = 1$，$n \ge 1$ 时

$$
c_n = \sum_{k=0}^n\frac{1}{k!}\cdot\frac{(-1)^{n-k}}{(n-k)!} = \frac{1}{n!}\sum_{k=0}^n\binom nk(-1)^{n-k} = \frac{(1-1)^n}{n!} = 0.
$$

故乘积为 $1$，即 $\mathrm{e}\cdot\mathrm{e}^{-1} = 1$。$\square$

**例 8.3.5** 求 $I = \sum_{n=0}^\infty\frac{1}{2^n}\cos\frac{2n\pi}{3}$。

**解** 级数绝对收敛，可以按 $n$ 模 $3$ 的余数分成三组分别求和：

$$
I = \sum_{k=0}^\infty\frac{1}{8^k}\left(1 + \frac12\cos\frac{2\pi}{3} + \frac14\cos\frac{4\pi}{3}\right) = \frac87\left(1 - \frac14 - \frac18\right) = \frac57.
$$

### 8.3.4. Abel 判别法与 Dirichlet 判别法

形如 $\sum a_nb_n$ 的级数，若 $\{a_n\}$ 单调、$\sum b_n$ 的部分和受控，可以用"分部求和"把它化为绝对收敛的级数，这是分部积分的离散版本。

**引理 8.3.1（Abel 变换）** 记 $B_k = b_1 + \cdots + b_k$，$B_0 = 0$，则

$$
\sum_{k=1}^n a_kb_k = a_nB_n - \sum_{k=1}^{n-1}(a_{k+1} - a_k)B_k.
$$

若 $\{a_k\}$ 单调，且 $|B_k| \le M$（$1 \le k \le n$），则 $\left|\sum_{k=1}^n a_kb_k\right| \le M(|a_1| + 2|a_n|)$。

**证明** 把 $b_k = B_k - B_{k-1}$ 代入左边并重新组合，得到恒等式。$a_k$ 单调时 $a_{k+1} - a_k$ 不变号，$\sum_{k=1}^{n-1}|a_{k+1} - a_k| = |a_n - a_1|$，于是左边 $\le M|a_n| + M|a_n - a_1| \le M(|a_1| + 2|a_n|)$。$\square$

**定理 8.3.5（Abel 判别法）** 若数列 $\{a_n\}$ 单调有界，$\sum b_n$ 收敛，则 $\sum a_nb_n$ 收敛。

**定理 8.3.6（Dirichlet 判别法）** 若数列 $\{a_n\}$ 单调且 $\lim_{n\to\infty}a_n = 0$，$\sum b_n$ 的部分和数列有界，则 $\sum a_nb_n$ 收敛。

**证明** 对段 $\sum_{k=m+1}^{m+p}a_kb_k$ 用引理 8.3.1（从 $k = m+1$ 起算部分和），验证 Cauchy 收敛准则。

- Dirichlet：设 $|B_n| \le M$，则 $|b_{m+1} + \cdots + b_{m+j}| \le 2M$，段和 $\le 2M(|a_{m+1}| + 2|a_{m+p}|) \le 6M|a_{m+1}| \to 0$（$|a_n|$ 单调减少趋于 $0$）。
- Abel：设 $|a_n| \le K$；对 $\varepsilon > 0$，$m$ 充分大时 $|b_{m+1} + \cdots + b_{m+j}| < \varepsilon$ 对一切 $j$ 成立，段和 $\le 3K\varepsilon$。$\square$

Leibniz 判别法是 Dirichlet 判别法的特例（$b_n = (-1)^{n-1}$，部分和为 $0$ 或 $1$）。Dirichlet 判别法要求的是 $\sum b_n$ 的部分和有界，不是 $\sum b_n$ 收敛；"$\{a_n\}$ 单调趋于零、$\sum b_n$ 收敛"只是 Abel 判别法的特例。

**例 8.3.6** 对任意 $x$，$\sum_{n=1}^\infty\frac{\sin nx}{n}$ 收敛。$x = 2k\pi$ 时各项为零。否则 $\sin\frac x2 \ne 0$，由积化和差，

$$
\sum_{k=1}^n\sin kx = \frac{\cos\frac x2 - \cos\left(n + \frac12\right)x}{2\sin\frac x2}, \qquad \left|\sum_{k=1}^n\sin kx\right| \le \frac{1}{\left|\sin\frac x2\right|},
$$
部分和有界，而 $\frac1n$ 单调趋于零，由 Dirichlet 判别法收敛。$x \ne k\pi$ 时它条件收敛：$|\sin nx| \ge \sin^2nx = \frac12(1 - \cos2nx)$，而 $\sum\frac1{2n}$ 发散、$\sum\frac{\cos2nx}{2n}$ 收敛（同理）。这个级数是[第 9 章](/2.2.9)中 Fourier 级数的一个典型例子。

**例 8.3.7** $\sum\frac{(-1)^n}{n}\left(1 + \frac1n\right)^n$ 收敛：$\sum\frac{(-1)^n}{n}$ 收敛，$\left(1 + \frac1n\right)^n$ 单调增加且有界（趋于 $\mathrm{e}$），由 Abel 判别法。

把本章的方法串起来，就是判断收敛性的一般流程。

**算法 8.3.1（判断数项级数的敛散性）**

1. 看通项：$u_n \not\to 0$ 则发散。
2. 正项级数（或考察 $\sum|u_n|$）：用 Taylor 公式或等价无穷小求通项的主部，与 $p$ 级数、几何级数比较；含 $n!$、$a^n$ 用比值判别法，含 $n$ 次幂用根值判别法；形如 $f(n)$ 且 $f$ 单调、易积分时用积分判别法。
3. $\sum|u_n|$ 收敛则原级数绝对收敛；否则对原级数用 Leibniz、Dirichlet、Abel 判别法，收敛则为条件收敛。
4. 必要时直接研究部分和（裂项相消、已知级数的和）。

## 小结

| 判别法 | 适用 | 条件与结论 | 失效 |
|---|---|---|---|
| 比较判别法 | 正项级数 | $u_n \le Mv_n$：$\sum v_n$ 收敛 $\Rightarrow$ $\sum u_n$ 收敛 | 找不到合适的 $v_n$ |
| 极限形式 | 正项级数 | $u_n/v_n \to q \in (0, +\infty)$：同敛散 | — |
| 比阶判别法 | 正项级数 | $n^pu_n$ 有极限，$p > 1$：收敛；极限非零，$p \le 1$：发散 | $\frac{1}{n\ln n}$ 型 |
| 比值判别法 | 正项级数 | $u_{n+1}/u_n \to q$：$q < 1$ 收敛，$q > 1$ 发散 | $q = 1$ |
| 根值判别法 | 正项级数 | $\sqrt[n]{u_n} \to q$：$q < 1$ 收敛，$q > 1$ 发散 | $q = 1$ |
| 积分判别法 | $u_n = f(n)$，$f$ 非负单减 | 与 $\int_1^{+\infty}f$ 同敛散 | $f$ 不单调 |
| Leibniz 判别法 | 交错级数 | $u_n$ 单减趋于 $0$：收敛，$\lvert r_n\rvert \le u_{n+1}$ | $u_n$ 不单调 |
| Dirichlet 判别法 | $\sum a_nb_n$ | $a_n$ 单调趋于 $0$，$\sum b_n$ 部分和有界 | — |
| Abel 判别法 | $\sum a_nb_n$ | $a_n$ 单调有界，$\sum b_n$ 收敛 | — |

| 标准级数 | 收敛条件 |
|---|---|
| 几何级数 $\sum aq^{n-1}$ | $\lvert q\rvert < 1$，和为 $\frac{a}{1-q}$ |
| $p$ 级数 $\sum\frac{1}{n^p}$ | $p > 1$ |
| Bertrand 级数 $\sum\frac{1}{n(\ln n)^p}$ | $p > 1$ |
| $\sum\frac{(-1)^n}{n^p}$ | $p > 1$ 绝对收敛，$0 < p \le 1$ 条件收敛 |

| 运算 | 收敛级数 | 绝对收敛级数 |
|---|---|---|
| 线性组合 | 可以 | 可以 |
| 加括号 | 可以（去括号不行） | 可以 |
| 交换次序 | 不可以（Riemann 重排定理） | 可以，和不变 |
| Cauchy 乘积 | 不一定收敛 | 收敛到乘积 |
