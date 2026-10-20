---
title: 随机数生成
description: 伪随机数发生器（线性同余发生器、满周期条件、格点结构、Mersenne Twister、随机性检验），以及用离散逆变换、逆变换法、拒绝抽样、条件化、密度图下的均匀抽样、变换、均匀比、和与混合生成非均匀随机变量。
source_hash: 0dc48da9e8f0
---

本课程中的每一次模拟，从**蒙特卡洛方法**（[3.1.12](/3.1.12)）、**自助法**（[3.5.7](/3.5.7)）到 [3.5.9](/3.5.9) 的 Markov 链 Monte Carlo，都要消耗随机数。本章说明确定性的计算机如何产生随机数，以及如何把它们变成服从给定分布的样本。本章分两部分。第一部分构造均匀伪随机数：一个序列"随机"意味着什么，线性同余发生器及其周期与格点结构，以及现代的 Mersenne Twister。第二部分生成其他分布的随机变量：离散分布、逆变换法（理论见 [3.1.7](/3.1.7)）、拒绝抽样及其变体，以及变换法，包括 **Box–Muller 方法**和借助 **Cholesky 分解**（[3.5.3](/3.5.3)）的多元正态抽样。本章中"随机数"指 $\mathrm{U}(0,1)$ 随机变量，"随机变量值"（random variate）指其他任何分布的抽样。贯穿全章的问题是：确定性算法如何"伪造"随机性；对任意的（可能很复杂、没有闭式分布函数的）目标分布有哪些通用的抽样方法；它们的效率瓶颈在哪里。

## 8.1. 均匀伪随机数

### 8.1.1. 随机数与伪随机数

> In a sense, there is no such thing as a random number; for example, is 2 a random number? Rather, we speak of a sequence of independent random numbers with a specified distribution. (D. E. Knuth, *The Art of Computer Programming*, Vol. 2)

Knuth 的意思是：在某种意义上并不存在"一个随机数"（2 是随机数吗？），我们谈论的是服从指定分布的独立随机数序列。这样的序列中每个数都纯属偶然得到，与其他数无关，并以指定的概率落入任一给定范围。物理装置可以产生这样的序列：骰子、纸牌、编号的球、旋转圆盘、电噪声电路（为英国有奖债券开奖的 ERNIE 机器）、对 γ 射线计数，或已出版的随机数表。它们的缺点是需要额外硬件、速度慢，尤其是不可重复。

**定义 8.1.1（伪随机数发生器）** **伪随机数发生器**（PRNG），又称确定性随机比特发生器，是一种确定性算法：它从称为**种子**的初值 $x_0$ 出发，输出一个可以代替真随机数独立同分布序列使用的数列；这个序列是确定且可重复的，却能通过随机性的统计检验。

有限状态空间上的发生器终将重复。输出序列由一个初始段（尾部）和随后的循环组成；从该种子出发的循环长度就是发生器的周期。伪随机数发生器快速且可重复，因而是蒙特卡洛模拟、贝叶斯分析中的计算以及电子游戏与密码学的核心。与理论和实验一起，模拟已成为推进自然科学的第三种途径。

均匀伪随机数发生器是基本的构件：假定它的输出是独立同分布的 $\mathrm{U}(0,1)$ 序列，其他一切分布都由它变换得到。每一种变换方法的正确性都强烈依赖于这一假定。

### 8.1.2. 线性同余发生器

**定义 8.1.2（线性同余发生器）** **线性同余发生器**（LCG）由 D. H. Lehmer 于 1949 年提出，按递推

$$
X_{i+1}\equiv aX_i+c \pmod m,\qquad i=0,1,\dots
$$
产生整数，其中 $a$ 为乘数，$c$ 为增量，$m$ 为模数，$X_0$ 为种子。于是 $X_i\in\{0,1,\dots,m-1\}$，随机数取 $R_i=X_i/m$。若 $c=0$，称为**乘同余发生器**（MCG）。

**例 8.1.1** 取 $m=8$，$a=5$，$c=1$，$X_0=5$：

$$
X_1\equiv5\cdot5+1=26\equiv2,\quad X_2\equiv11\equiv3,\quad X_3\equiv16\equiv0,\quad X_4\equiv1,
$$
接着 $X_5=6$，$X_6=7$，$X_7=4$，$X_8=5$，$X_9=2$。随机数为 $R_1,\dots,R_9=0.25,\ 0.375,\ 0,\ 0.125,\ 0.75,\ 0.875,\ 0.5,\ 0.625,\ 0.25$。这个序列"看起来"随机，但 $X_i$ 只能取 $m$ 个值 $0,1,\dots,m-1$，而且 $8$ 步之后就重复。

一般地有三点观察。

- 序列是周期的。整数 $X_i$ 非负且小于 $m$，所以序列以不超过 $m$ 的周期循环。生成比周期更多的数并不会产生新的点。
- 它可能产生 $0$（乘同余发生器一旦到达 $0$ 就永远停在 $0$），而随机数应当落在开区间 $(0,1)$ 中。
- 相继的数对 $(R_i,R_{i+1})$ 总是落在一个格点上；格点的疏密取决于 $a$。

若 LCG（对每个种子）的循环长度都是 $m$，称它达到满周期。

**定理 8.1.1（Hull–Dobell 定理）** LCG 有满周期 $m$ 当且仅当：

1. $\gcd(m,c)=1$；
2. 整除 $m$ 的每个素数 $q$ 也整除 $a-1$；
3. 若 $4\mid m$，则 $4\mid a-1$。

**定理 8.1.2** 对乘同余发生器，$X_i\equiv a^iX_0\pmod m$，可能的最大周期是 $m-1$；当 $m$ 为素数且 $a$ 是模 $m$ 的原根时达到。若 $m=2^n$，$n\ge3$，则周期至多为 $2^{n-2}$，当 $X_0$ 为奇数且 $a\equiv3$ 或 $5\pmod 8$ 时达到。

公式 $X_i\equiv a^iX_0$ 由归纳法得到：$X_{i+1}\equiv aX_i\equiv a\cdot a^iX_0$。它还允许发生器向前跳跃：$a^k \bmod m$ 可以用反复平方计算。

**例 8.1.2** 对 $X_{i+1}\equiv11X_i+5\pmod{16}$，$X_0=1$，可能的最大周期是 $m=16$。条件 1（$\gcd(16,5)=1$）与条件 2（素数 $2$ 整除 $a-1=10$）成立，但 $4\mid16$ 而 $4\nmid10$，条件 3 不成立，所以达不到满周期。实际上序列为 $0,5,12,9,8,13,4,1,0,\dots$，周期为 $8$。

**例 8.1.3** 几个著名的 LCG：

- RANDU，$X_{i+1}\equiv65539X_i\pmod{2^{31}}$（乘同余发生器），因运行快而在 20 世纪 60 年代被广泛采用。它的二维格点尚可，三维格点却很差：由于 $65539=2^{16}+3$，

  $$
  a^2=(2^{16}+3)^2=2^{32}+6\cdot2^{16}+9\equiv6(2^{16}+3)-9=6a-9\pmod{2^{31}},
  $$
  所以 $X_{i+2}\equiv6X_{i+1}-9X_i$，$9R_i-6R_{i+1}+R_{i+2}$ 是整数。它严格介于 $-6$ 与 $10$ 之间，因此所有三元组 $(R_i,R_{i+1},R_{i+2})$ 只落在 $15$ 个平行平面上。这一发现使人们怀疑 20 世纪 60、70 年代用 RANDU 得到的蒙特卡洛结果。
- $X_{i+1}\equiv16807X_i\pmod{2^{31}-1}$，由 Lewis、Goodman 和 Miller（1969）为 IBM System/360 提出。模数是素数，$16807=7^5$ 是原根，所以周期为 $2^{31}-2$。由于它在经验检验中的表现和易于实现，Park 和 Miller（1988）把它作为与其他发生器比较的"最低标准"；它被内置于操作系统、IMSL 程序库、MATLAB 和许多模拟软件中。

更一般地，Marsaglia（1968）证明了任何 LCG 的 $d$ 元组 $(R_i,\dots,R_{i+d-1})$ 都落在至多 $(d!\,m)^{1/d}$ 个平行超平面上。取 $m=2^{31}$、$d=10$，只有约 $39$ 个，所以 LCG 不适用于高维的蒙特卡洛模拟。

![LCG 的格点结构。左、中：m = 101 的满周期发生器在 a = 3（三条直线）与 a = 12（较细的格点）时的相继数对。右：RANDU 三元组在其平面法向 (9, -6, 1) 上的投影只取 15 个值，而 Mersenne Twister 的三元组连续地散开。](./plots/lcg-lattice.py)

### 8.1.3. 伪随机数的检验

"伪"意味着用已知方法生成数字就排除了真随机的可能。可能偏离理想随机性的情形有：

- 数字不服从均匀分布，或取离散值而非连续值，或均值、方差偏高或偏低；
- 数字之间相关：自相关，连续比相邻数大或小的游程，若干个高于均值的数后面跟着若干个低于均值的数。

因此发生器要接受两类统计检验。

- 均匀性检验，$H_0\colon R_i\sim\mathrm{U}(0,1)$ 对 $H_1\colon R_i\not\sim\mathrm{U}(0,1)$，例如对 $[0,1)$ 的划分作卡方拟合优度检验，或 Kolmogorov–Smirnov 检验。
- 独立性检验，$H_0$：$R_i$ 相互独立，对 $H_1$：不独立，例如游程检验、自相关检验和序列检验（对 $[0,1)^d$ 中的 $d$ 元组作卡方检验）。

不能拒绝 $H_0$ 只意味着没有发现不均匀或相关的证据。Diehard、TestU01 等检验组合把数百个这样的检验组合在一起。

### 8.1.4. Mersenne Twister

Mersenne Twister（Matsumoto 与 Nishimura，1998）是现代伪随机数发生器的标杆。它的状态是一个 $19937$ 比特的向量（624 个 32 位字）；每一步通过移位、异或和 $\mathbb{F}_2$ 上的线性变换"扭转"状态，并输出一个经过调和（tempering）的 32 位数。它的周期是 Mersenne 素数 $2^{19937}-1$，远超 LCG 的 $2^{31}-1$。

- 高维结构：它在至多 $623$ 维中均匀分布（32 位精度），避免了 LCG 在低维中的粗格点。
- 统计性质：它通过几乎所有标准的随机性检验（如 Diehard）。
- 速度：虽然复杂，经优化后效率很高。它是 R、MATLAB 和 Python `random` 模块的默认发生器；NumPy 的旧接口 `RandomState` 使用它，而 NumPy 新的 `Generator` 默认使用 PCG64。

它不适用于密码学：输出是状态的线性函数，从 $624$ 个连续输出就能重构状态。

```r
RNGkind()        # "Mersenne-Twister" "Inversion" "Rejection"
set.seed(2024)   # the seed makes a simulation reproducible
runif(3)
?.Random.seed    # details about the state of the default generator
```

## 8.2. 离散分布与逆变换法

从现在起假定有一个独立同分布 $\mathrm{U}(0,1)$ 随机数的发生器，即 R 中的 `runif`。最基本的任务——从有限总体中抽取简单随机样本——已经需要离散均匀分布；R 的 `sample` 完成这件事，并且对每个标准分布 R 都提供四个函数：

```r
sample(0:1, size = 10, replace = TRUE)          # toss some coins
sample(1:100, size = 6, replace = FALSE)        # choose some lottery numbers
sample(letters)                                 # a random permutation of a-z
x <- sample(1:3, size = 100, replace = TRUE, prob = c(.2, .3, .5))
table(x)                                        # one run gave 14, 31, 55

dbinom(x, size, prob, log = FALSE)              # probability mass function or density
pbinom(q, size, prob, lower.tail = TRUE)        # cumulative distribution function
qbinom(p, size, prob, lower.tail = TRUE)        # quantile function
rbinom(n, size, prob)                           # random generator
```

### 8.2.1. 离散分布

**引理 8.2.1** 设 $U\sim\mathrm{U}(0,1)$，$n\in\mathbb{N}_+$，令 $X=\lfloor nU\rfloor$。则 $X$ 在 $\{0,1,\dots,n-1\}$ 上均匀分布。

**证明** 对 $k=0,1,\dots,n-1$，
$\mathbb{P}(X=k)=\mathbb{P}(\lfloor nU\rfloor=k)=\mathbb{P}(nU\in[k,k+1))=\mathbb{P}(U\in[k/n,(k+1)/n))=1/n$。 $\square$

**引理 8.2.2** 设 $p\in[0,1]$，$U\sim\mathrm{U}(0,1)$，$E=\{U\le p\}$。则 $\mathbb{P}(E)=p$；特别地 $\boldsymbol{1}_E\sim\mathrm{Ber}(p)$。

**引理 8.2.3** 设 $A=\{a_i\mid i\in I\}$，$I=\{1,\dots,n\}$ 或 $I=\mathbb{N}_+$，且 $i\ne j$ 时 $a_i\ne a_j$；设 $p_i\ge0$，$\sum_{i\in I}p_i=1$。令 $U\sim\mathrm{U}(0,1)$，

$$
K=\min\Bigl\{k\in I\Bigm|\sum_{i=1}^kp_i\ge U\Bigr\}.
$$
则 $X=a_K$ 对一切 $k\in I$ 满足 $\mathbb{P}(X=a_k)=p_k$。

**证明** $\mathbb{P}(X=a_k)=\mathbb{P}(K=k)=\mathbb{P}\bigl(\sum_{i=1}^{k-1}p_i<U\le\sum_{i=1}^kp_i\bigr)=p_k$。 $\square$

这就是离散分布的逆变换：$K$ 是分布函数的广义逆在 $U$ 处的值。按 $p_i$ 从大到小排列取值可以减少比较次数的期望。

**例 8.2.1** **几何分布** $\mathrm{Geo}(p)$ 是成功概率为 $p$ 的独立试验直到首次成功所需的次数 $X$，$p_i=\mathbb{P}(X=i)=(1-p)^{i-1}p$，$i\in\mathbb{N}_+$。取 $a_i=i$，$\sum_{i=1}^kp_i=1-(1-p)^k$，且

$$
\sum_{i=1}^kp_i\ge U\iff(1-p)^k\le1-U\iff k\ge\frac{\log(1-U)}{\log(1-p)}.
$$
因此

$$
X=K=\Bigl\lceil\frac{\log(1-U)}{\log(1-p)}\Bigr\rceil\sim\mathrm{Geo}(p),
$$
其中 $\lceil\cdot\rceil$ 表示向上取整。一个均匀随机数就代替了一整串 Bernoulli 试验；由于 $1-U\sim\mathrm{U}(0,1)$，也可以用 $\log U$ 代替 $\log(1-U)$。

### 8.2.2. 逆变换法

由**概率积分变换**，若 $X$ 是分布函数为 $F_X$ 的连续随机变量，则 $F_X(X)\sim\mathrm{U}(0,1)$。反过来，定义广义逆

$$
F_X^{-1}(u)=\inf\{x\in\mathbb{R}\colon F_X(x)\ge u\},\qquad0<u<1.
$$
则对任意分布函数，$F_X^{-1}(U)$ 与 $X$ 同分布（[3.1.7 的定理 7.3.1](/3.1.7#thm-7.3.1)），因为

$$
\mathbb{P}(F_X^{-1}(U)\le x)=\mathbb{P}\bigl(\inf\{t\colon F_X(t)\ge U\}\le x\bigr)=\mathbb{P}(U\le F_X(x))=F_X(x).
$$

**算法 8.2.1（逆变换法）**

1. 推导反函数 $F_X^{-1}(u)$。
2. 对所需的每个随机变量值：从 $\mathrm{U}(0,1)$ 生成 $u$，输出 $x=F_X^{-1}(u)$。

只要 $F_X^{-1}$ 容易计算，这个方法（**逆变换法**）就很容易使用。

**例 8.2.2** 若在 $(0,1)$ 上 $F_X(x)=x^3$，则 $F_X^{-1}(u)=u^{1/3}$，密度为 $f(x)=3x^2$：

```r
n <- 1000
u <- runif(n)
x <- u^(1/3)
hist(x, prob = TRUE, main = expression(f(x) == 3*x^2))   # density histogram of the sample
y <- seq(0, 1, .01)
lines(y, 3*y^2)                                          # density curve f(x)
```

**例 8.2.3** 参数为 $\sigma>0$ 的 **Rayleigh 分布**的密度为 $f(x)=\frac{x}{\sigma^2}\mathrm{e}^{-x^2/(2\sigma^2)}$，$x\ge0$。对 $a\ge0$，

$$
F(a)=\int_0^a\frac{x}{\sigma^2}\mathrm{e}^{-x^2/(2\sigma^2)}\,\mathrm{d}x=\Bigl[-\mathrm{e}^{-x^2/(2\sigma^2)}\Bigr]_0^a=1-\mathrm{e}^{-a^2/(2\sigma^2)},
$$
解 $u=F(x)$ 得 $x=\sqrt{-2\sigma^2\log(1-u)}$。

这个方法也适用于离散分布（引理 8.2.3），但有两个局限。它需要闭式且易于求逆的分布函数（指数、均匀、Bernoulli、Rayleigh、Cauchy 等）；对正态或 Gamma 分布，反函数必须数值计算。并且分布函数只存在于一维：对 $\mathbb{R}^d$（$d>1$）上的分布需要更复杂的方法。

## 8.3. 拒绝抽样

拒绝抽样（rejection sampling），又称舍选法、接受–拒绝法，是更高级也非常流行的方法。它常用于多阶段的方案：先用别的方法生成近似服从正确分布的样本，再用拒绝把它们变成精确服从目标分布的样本。它在非常一般的空间上都适用。代价是每个输出样本需要随机的、可能很多的输入样本，所以效率是主要的关注点。

### 8.3.1. 基本拒绝抽样

我们想生成密度（或概率质量函数）$f$ 很复杂的随机变量 $X$，而能够生成密度 $g$ 简单的随机变量。

**算法 8.3.1（基本拒绝抽样）** 输入：概率密度 $g$（提议密度（proposal density））以及取值于 $[0,1]$ 的函数 $p$（接受概率）。所用随机性：独立同分布、密度为 $g$ 的提议 $X_n$，以及独立同分布的 $U_n\sim\mathrm{U}(0,1)$。

1. 对 $n=1,2,3,\dots$：生成密度为 $g$ 的 $X_n$ 与 $U_n\sim\mathrm{U}(0,1)$。
2. 若 $U_n\le p(X_n)$，输出 $X_n$；否则丢弃。

**定理 8.3.1** 设 $Z=\int p(x)g(x)\,\mathrm{d}x>0$，$X_{N_k}$ 是第 $k$ 个输出，$k\in\mathbb{N}_+$。则：

1. 输出 $X_{N_1},X_{N_2},\dots$ 独立同分布，密度为
   $$
   f(x)=\frac1Zp(x)g(x);
   $$
2. 每个提议以概率 $Z$ 被接受，每个输出所需的提议数 $M_k=N_k-N_{k-1}$ 服从均值为 $1/Z$ 的几何分布。

**证明** (2) 对固定的 $n$，$\mathbb{P}(U_n\le p(X_n))=\int p(x)g(x)\,\mathrm{d}x=Z$。不同 $n$ 的接受与否相互独立，所以等到首次接受的时间服从 $\mathrm{Geo}(Z)$，均值为 $1/Z$。

(1) 令 $N_0=0$，$N_k=\min\{n>N_{k-1}\mid U_n\le p(X_n)\}$。对集合 $A$，$\mathbb{P}(U_n\le p(X_n),X_n\in A)=\int_Ap(x)g(x)\,\mathrm{d}x$。由各对 $(X_n,U_n)$ 的独立性，

$$
\begin{aligned}
\mathbb{P}(X_{N_k}\in A\mid N_{k-1}=n)&=\sum_{m=1}^\infty\mathbb{P}\bigl(N_k=n+m,\ X_{n+m}\in A\mid N_{k-1}=n\bigr)\\
&=\sum_{m=1}^\infty\mathbb{P}(U_{n+1}>p(X_{n+1}))\cdots\mathbb{P}(U_{n+m-1}>p(X_{n+m-1}))\,\mathbb{P}(U_{n+m}\le p(X_{n+m}),X_{n+m}\in A)\\
&=\sum_{m=1}^\infty(1-Z)^{m-1}\int_Ap(x)g(x)\,\mathrm{d}x=\frac1Z\int_Ap(x)g(x)\,\mathrm{d}x.
\end{aligned}
$$
它与 $n$ 无关，所以 $\mathbb{P}(X_{N_k}\in A)=\frac1Z\int_Ap(x)g(x)\,\mathrm{d}x$。用同样的方法对 $N_1=n_1,\dots,N_k=n_k$ 的各种情形求和，可得 $\mathbb{P}(X_{N_1}\in A_1,\dots,X_{N_k}\in A_k)=\prod_{i=1}^k\mathbb{P}(X_{N_i}\in A_i)$，即独立性。 $\square$

函数 $p$ 是给定提议 $X_n=x$ 时接受的条件概率，而 $Z$ 是边缘（平均）接受概率：记 $I=\boldsymbol{1}\{U_n\le p(X_n)\}$，则 $I\mid X_n=x\sim\mathrm{Ber}(p(x))$，$I\sim\mathrm{Ber}(Z)$。算法本身从不用到 $Z$ 的值；$Z$ 只影响效率，$Z$ 越大效率越高。

**例 8.3.1（Wigner 半圆分布）** Wigner 半圆分布

$$
f(x)=\frac{2}{\pi R^2}\sqrt{R^2-x^2}\,\boldsymbol{1}_{[-R,R]}(x)
$$
是一个经过伸缩的 Beta 分布；当矩阵阶数趋于无穷时，许多随机对称矩阵的特征值分布以它为极限。对 $R=1$，令 $X\sim\mathrm{U}(-1,1)$，以概率 $p(X)=\sqrt{1-X^2}$ 接受 $X$。则 $g(x)=\frac12\boldsymbol{1}_{[-1,1]}(x)$，

$$
Z=\int p(x)g(x)\,\mathrm{d}x=\frac12\int_{-1}^1\sqrt{1-x^2}\,\mathrm{d}x=\frac\pi4,
$$
被接受的样本的密度为 $\frac1Zp(x)g(x)=\frac2\pi\sqrt{1-x^2}\,\boldsymbol{1}_{[-1,1]}(x)$。

### 8.3.2. 包络拒绝抽样

**算法 8.3.2（包络拒绝抽样）** 输入：函数 $f\ge0$（目标密度，可以未归一化）、提议密度 $g$，以及常数 $c>0$，使得对一切 $x$ 有 $f(x)\le cg(x)$。

1. 生成密度为 $g$ 的 $X_n$ 与 $U_n\sim\mathrm{U}(0,1)$。
2. 若 $U_n\le f(X_n)/(cg(X_n))$，接受并输出 $X_n$；否则拒绝 $X_n$，回到第 1 步。

这就是取 $p(x)=f(x)/(cg(x))$（在 $g(x)=0$ 处取 $p(x)=1$）的基本算法。对离散目标，其正确性也可以由 **Bayes 公式**看出：$\mathbb{P}(\text{accept}\mid X=k)=\frac{f(k)}{cg(k)}$，所以对归一化的 $f$ 有 $\mathbb{P}(\text{accept})=\sum_k\frac{f(k)}{cg(k)}g(k)=\frac1c$，且

$$
\mathbb{P}(X=k\mid\text{accept})=\frac{\mathbb{P}(\text{accept}\mid X=k)\,g(k)}{\mathbb{P}(\text{accept})}=\frac{f(k)/c}{1/c}=f(k).
$$

**定理 8.3.2** 设 $Z_f=\int f(x)\,\mathrm{d}x$。算法 8.3.2 的输出独立同分布，密度为归一化的 $\tilde f(x)=f(x)/Z_f$；每个提议以概率 $Z_f/c$ 被接受，每个输出所需的提议数服从均值为 $c/Z_f$ 的几何分布。

**证明** 对 $p(x)=f(x)/(cg(x))$ 应用定理 8.3.1：$Z=\int\frac{f(x)}{cg(x)}g(x)\,\mathrm{d}x=\frac1c\int f(x)\,\mathrm{d}x=\frac{Z_f}{c}$，且 $\frac1Zp(x)g(x)=\frac{f(x)}{Z_f}$。 $\square$

几何直观解释了这个名称。给定 $X_n$，点 $(X_n,cg(X_n)U_n)$ 在包络 $cg$ 的图像下方均匀分布；提议被接受当且仅当 $f(X_n)\ge cg(X_n)U_n$，即该点落在 $f$ 的图像下方。算法只需要知道 $f$ 的一个常数倍，这正是它对后验密度如此有用的原因。

**例 8.3.2** 先抽样半正态分布，即以取正值为条件的**标准正态分布**，密度 $f(x)=\sqrt{2/\pi}\,\mathrm{e}^{-x^2/2}$，$x\ge0$，用 $\mathrm{Exp}(\lambda)$ 提议 $g(x)=\lambda\mathrm{e}^{-\lambda x}$，$x\ge0$。对 $x\ge0$，

$$
\frac{f(x)}{g(x)}=\frac{1}{\lambda}\sqrt{\frac2\pi}\exp\Bigl(-\frac{x^2}{2}+\lambda x\Bigr)\le\frac1\lambda\sqrt{\frac2\pi}\exp\Bigl(\frac{\lambda^2}{2}\Bigr)=:c,
$$
等号在 $x=\lambda$ 处成立。任何 $c^*\ge c$ 也满足 $f\le c^*g$，但计算量与 $c$ 成正比，所以 $c$ 应尽量小。接受条件为

$$
U_n\le\frac{f(X_n)}{cg(X_n)}=\exp\Bigl(-\frac12(X_n-\lambda)^2\Bigr).
$$
对 $\lambda$ 最小化 $c(\lambda)$ 得 $\lambda=1$，$c=\sqrt{2\mathrm{e}/\pi}\approx1.315$，接受率 $1/c\approx0.76$。最后给每个被接受的 $X_n$ 随机加上符号，以各 $1/2$ 的概率取 $+X_n$ 或 $-X_n$，就得到标准正态随机变量值。

![用 Exp(1) 提议对半正态密度作包络拒绝抽样。左：提议点 (X, c g(X) U) 在包络 c g 下方均匀分布，落在 f 下方的被接受。右：被接受的值加上随机符号后服从 N(0, 1)。](./plots/rejection-half-normal.py)

提议密度 $g$ 的选取以效率最大为目标。

- 由于 $f\le cg$，$g$ 的支撑必须包含 $f$ 的支撑。
- 生成一个样本的平均代价等于平均提议数乘以生成一个提议的代价。所以 $g$ 应当容易抽样，且 $c/Z_f$ 应当小，即 $g$ 的形状应尽量接近 $f$。

**注 8.3.1** 自适应拒绝抽样（Gilks 与 Wild，1992）对对数凹密度改进了这一想法：包络是由 $\log f$ 的切线构成的分段指数函数，每个被拒绝的点都用来收紧包络，于是接受率趋于 $1$。它被用于例如 Gibbs 抽样之中（[3.5.9](/3.5.9)）。

### 8.3.3. 条件分布

条件分布 $P_{X\mid X\in A}$ 描述了已知 $X\in A$ 发生后 $X$ 中剩余的随机性。

**算法 8.3.3（条件分布的抽样）** 输入：满足 $\mathbb{P}(X\in A)>0$ 的集合 $A$，以及 $X$ 的独立同分布拷贝 $X_n$（提议）。对 $n=1,2,\dots$：生成 $X_n$；若 $X_n\in A$，输出 $X_n$。

**定理 8.3.3** 算法 8.3.3 的输出独立同分布，对每个 $B$ 有 $\mathbb{P}(X_{N_k}\in B)=\mathbb{P}(X\in B\mid X\in A)$，每个输出所需的提议数服从均值为 $1/\mathbb{P}(X\in A)$ 的几何分布。

**证明** 这是取 $p(x)=\boldsymbol{1}_A(x)$ 的基本拒绝抽样。若 $X$ 有密度 $g$，则 $Z=\int\boldsymbol{1}_A(x)g(x)\,\mathrm{d}x=\mathbb{P}(X\in A)$，且

$$
\mathbb{P}(X_{N_k}\in B)=\frac{\int_B\boldsymbol{1}_A(x)g(x)\,\mathrm{d}x}{Z}=\frac{\mathbb{P}(X\in A\cap B)}{\mathbb{P}(X\in A)}=\mathbb{P}(X\in B\mid X\in A). \qquad\square
$$

当 $\mathbb{P}(X\in A)$ 较大时这个方法效果好；生成一个输出的时间与 $1/\mathbb{P}(X\in A)$ 成正比。

**例 8.3.3（截断正态分布）** 为生成以 $X\ge a>0$ 为条件的 $X\sim\mathcal{N}(0,1)$，重复：生成 $X\sim\mathcal{N}(0,1)$；若 $X\ge a$，输出 $X$。提议数的期望为 $\mathbb{E}(M_k)=1/(1-\Phi(a))$，在 R 中用 `1/(1-sapply(1:6, pnorm))` 计算：

| $a$ | $1$ | $2$ | $3$ | $4$ | $5$ | $6$ |
|---|---|---|---|---|---|---|
| $\mathbb{E}(M_k)$ | $6.3$ | $44$ | $741$ | $31\,574$ | $3\,488\,556$ | $1\,013\,594\,692$ |

即使 $a$ 不大，这个方法也很慢；$a\ge5$ 时已不实用。

包络版本要好得多。条件密度为 $\tilde f(x)=f(x)/Z_f$，$f(x)=\exp(-x^2/2)\boldsymbol{1}_{[a,\infty)}(x)$。用平移的指数提议 $X=\tilde X+a$，$\tilde X\sim\mathrm{Exp}(\lambda)$，密度 $g(x)=\lambda\mathrm{e}^{-\lambda(x-a)}\boldsymbol{1}_{[a,\infty)}(x)$。则对 $x\ge a$

$$
\frac{f(x)}{g(x)}=\frac1\lambda\exp\Bigl(-\frac{x^2}{2}+\lambda(x-a)\Bigr).
$$
一个简单的选择是 $\lambda=a$，它使 $g$ 在截断点处与 $f$ 以相同速率衰减；指数 $-\frac{x^2}{2}+a(x-a)=-\frac{(x-a)^2}{2}-\frac{a^2}{2}$ 在 $x=a$ 处最大，所以 $c=\frac1a\mathrm{e}^{-a^2/2}$，接受条件为 $U\le\exp(-(X-a)^2/2)$。（使 $c$ 最小的值是 $\lambda^*=\frac{a+\sqrt{a^2+4}}{2}$，略大于 $a$，效率几乎相同。）步骤为：

1. 生成 $\tilde X\sim\mathrm{Exp}(a)$ 与 $U\sim\mathrm{U}(0,1)$；
2. 令 $X=\tilde X+a$；
3. 若 $U\le\exp(-(X-a)^2/2)$，输出 $X$。

现在提议数的期望为

$$
\mathbb{E}(M_k)=\frac{c}{Z_f}=\frac{\frac1a\mathrm{e}^{-a^2/2}}{\int_a^\infty\mathrm{e}^{-x^2/2}\,\mathrm{d}x}=\frac{\mathrm{e}^{-a^2/2}}{a\sqrt{2\pi}\,(1-\Phi(a))}:
$$

| $a$ | $1$ | $2$ | $3$ | $4$ | $5$ | $6$ |
|---|---|---|---|---|---|---|
| $\mathbb{E}(M_k)$ | $1.53$ | $1.19$ | $1.09$ | $1.06$ | $1.04$ | $1.03$ |

截断点越远，指数尾部与正态尾部吻合得越好。

### 8.3.4. 均匀分布与密度

**定义 8.3.1（集合上的均匀分布）** 取值于 $\mathbb{R}^d$ 的随机变量 $X$ 称为在体积 $0<\lvert A\rvert<\infty$ 的集合 $A\subseteq\mathbb{R}^d$ 上均匀分布，如果对一切 $B\subseteq\mathbb{R}^d$ 有 $\mathbb{P}(X\in B)=\lvert A\cap B\rvert/\lvert A\rvert$。

**例 8.3.4** 设 $X_n,Y_n\sim\mathrm{U}(-1,1)$ 独立同分布；数对 $(X_n,Y_n)$ 在正方形 $Q=[-1,1]\times[-1,1]$ 上均匀分布（若 $X\sim\mathrm{U}(a,b)$ 与 $Y\sim\mathrm{U}(c,d)$ 独立，则 $(X,Y)$ 在 $[a,b]\times[c,d]$ 上均匀分布，因为联合密度在其上为常数）。保留满足 $X_n^2+Y_n^2\le1$ 的数对。由定理 8.3.3，保留下来的点构成在单位圆盘 $D=\{x\in\mathbb{R}^2\colon\lvert x\rvert\le1\}$ 上均匀分布的独立同分布序列。接受概率为 $\lvert D\rvert/\lvert Q\rvert=\pi/4\approx78.5\%$，平均每个点需要 $4/\pi\approx1.27$ 个提议。

**定理 8.3.4（模拟基本定理）** 设 $f\colon\mathbb{R}^d\to[0,\infty)$ 是概率密度，

$$
A=\{(x,y)\in\mathbb{R}^d\times[0,\infty)\mid0\le y<f(x)\}\subseteq\mathbb{R}^{d+1}.
$$
则 $\lvert A\rvert=1$，且下列两条等价：

1. $(X,Y)$ 在 $A$ 上均匀分布；
2. $X$ 的密度为 $f$，且 $Y=f(X)U$，其中 $U\sim\mathrm{U}(0,1)$ 与 $X$ 独立。

**证明** $\lvert A\rvert=\int_{\mathbb{R}^d}\int_0^{f(x)}\mathrm{d}y\,\mathrm{d}x=\int_{\mathbb{R}^d}f(x)\,\mathrm{d}x=1$。

(1) $\Rightarrow$ (2)：令 $U=Y/f(X)$。对集合 $C\subseteq\mathbb{R}^d$、$D\subseteq\mathbb{R}$，作代换 $y=f(x)u$，

$$
\mathbb{P}(X\in C,U\in D)=\Bigl\lvert A\cap\{(x,y)\colon x\in C,\ y/f(x)\in D\}\Bigr\rvert=\int_{\mathbb{R}^d}\int_0^{f(x)}\boldsymbol{1}_C(x)\boldsymbol{1}_D\Bigl(\frac{y}{f(x)}\Bigr)\mathrm{d}y\,\mathrm{d}x=\int_Cf(x)\,\mathrm{d}x\cdot\int_D\boldsymbol{1}_{[0,1]}(u)\,\mathrm{d}u.
$$
所以 $X$ 与 $U$ 独立，密度分别为 $f$ 与 $\boldsymbol{1}_{[0,1]}$。

(2) $\Rightarrow$ (1)：给定 $X=x$，$Y=f(x)U\sim\mathrm{U}(0,f(x))$。对 $B=C\times D$，$C\subseteq\mathbb{R}^d$，$D\subseteq[0,\infty)$，

$$
\mathbb{P}((X,Y)\in B)=\int_C\frac{\lvert D\cap[0,f(x)]\rvert}{f(x)}f(x)\,\mathrm{d}x=\int_C\lvert D\cap[0,f(x)]\rvert\,\mathrm{d}x=\lvert A\cap B\rvert.
$$
矩形决定分布，所以 $(X,Y)$ 在 $A$ 上均匀分布。 $\square$

因此，从一个密度中抽样，等同于在高一维的、它的图像下方的区域中均匀抽样。这正是包络拒绝有效的原因：$(X_k,cg(X_k)U_k)$ 在 $cg$ 下方均匀分布，被接受的点在 $f$ 下方均匀分布，所以它们的第一个坐标的密度为 $f$。

**例 8.3.5** 为抽样密度为 $p(x)=2x$（$0\le x\le1$）的 $X$，生成 $Y\sim\mathrm{U}(0,1)$ 与 $U_1\sim\mathrm{U}(0,1)$，令 $U=2U_1$；$(Y,U)$ 在盒子 $[0,1]\times[0,2]$ 上均匀分布，由于 $p(x)\in[0,2]$，它包含了密度的图像。曲线 $u=2y$ 下方的点就是我们要的：$X=Y\mid U<2Y$ 的密度为 $p$。用包络拒绝的语言，$g=1$，$f/g=2x\le2=c$，所以每个模拟值平均需要 $c=2$ 次试验。

一般地，为抽样满足 $f\le M$ 的密度 $f\colon[a,b]\to\mathbb{R}$：设 $(X_k,Y_k)$ 独立同分布、在矩形 $R=[a,b]\times[0,M]$ 上均匀分布，令 $A=\{(x,y)\in R\mid y\le f(x)\}$，$N=\min\{k\mid(X_k,Y_k)\in A\}$。则 $(X_N,Y_N)$ 在 $A$ 上均匀分布，$X_N$ 的密度为 $f$。当 $f$ 定义在无界集上时，把矩形换成包络下方的区域 $\{(x,y)\mid0\le y<cg(x)\}$，这又回到了包络拒绝抽样。

## 8.4. 变换法

### 8.4.1. 一般的变换定理

逆变换法是变换均匀随机变量的一个特例；一般地，我们用光滑双射变换随机向量。

**定理 8.4.1（随机变量的变换）** 设 $A,B\subseteq\mathbb{R}^d$ 是开集，$\varphi\colon A\to B$ 是可微且偏导数连续的双射，$g\colon B\to[0,\infty)$ 是概率密度。定义

$$
f(x)=g(\varphi(x))\,\lvert\det D\varphi(x)\rvert\,\boldsymbol{1}_A(x),
$$
其中 $D\varphi=\bigl(\partial\varphi_i/\partial x_j\bigr)$ 是 **Jacobi 矩阵**。则 $f$ 是概率密度，且 $X$ 的密度为 $f$ 当且仅当 $\varphi(X)$ 的密度为 $g$。

等价地，若 $X\sim g$ 且 $Y=\varphi(X)$，则 $f_Y(y)=g(\varphi^{-1}(y))\lvert\det D\varphi^{-1}(y)\rvert$：关键是 **Jacobi 行列式**（[3.1.7](/3.1.7)）。实践中用到许多变换，不必记忆：

- 若 $Z\sim\mathcal{N}(0,1)$，则 $V=Z^2\sim\chi^2_1$；
- 若 $U\sim\chi^2_m$ 与 $V\sim\chi^2_n$ 独立，则 $F=\frac{U/m}{V/n}\sim F_{m,n}$；
- 若 $Z\sim\mathcal{N}(0,1)$ 与 $V\sim\chi^2_n$ 独立，则 $T=Z/\sqrt{V/n}\sim t_n$；
- 若 $U,V\sim\mathrm{U}(0,1)$ 独立，则 $Z_1=\sqrt{-2\log U}\cos(2\pi V)$ 与 $Z_2=\sqrt{-2\log U}\sin(2\pi V)$ 是独立的标准正态变量；
- 若 $U\sim\Gamma(r,\lambda)$ 与 $V\sim\Gamma(s,\lambda)$ 独立，则 $X=U/(U+V)\sim\mathrm{Beta}(r,s)$；
- 若 $U,V\sim\mathrm{U}(0,1)$ 独立，则 $X=\Bigl\lfloor1+\dfrac{\log V}{\log(1-(1-\theta)^U)}\Bigr\rfloor$ 服从参数为 $\theta$ 的对数分布，$\mathbb{P}(X=x)=\dfrac{-\theta^x}{x\log(1-\theta)}$，$x\in\mathbb{N}_+$。

**例 8.4.1** 标准 **Cauchy 分布**是 $n=1$ 的 **t 分布**：

$$
f(x)=\frac{\Gamma\bigl(\frac{n+1}2\bigr)}{\sqrt{n\pi}\,\Gamma\bigl(\frac n2\bigr)}\Bigl(1+\frac{x^2}{n}\Bigr)^{-(n+1)/2}\overset{n=1}{=}\frac{\Gamma(1)}{\sqrt\pi\,\Gamma(\frac12)}\cdot\frac1{1+x^2}=\frac1{\pi(1+x^2)}.
$$
因此若 $Z_1,Z_2\sim\mathcal{N}(0,1)$ 独立同分布，则 $Y=Z_1/Z_2\sim t_1$ 是标准 Cauchy 分布。

### 8.4.2. Box–Muller 方法

我们要抽样标准二元正态密度 $g(x,y)=\frac1{2\pi}\exp\bigl(-\frac{x^2+y^2}2\bigr)$。用极坐标 $\varphi(r,\theta)=(r\cos\theta,r\sin\theta)$，$r>0$，$\theta\in(0,2\pi)$。在 $A=(0,\infty)\times(0,2\pi)$ 上，像集为 $B=\varphi(A)=\mathbb{R}^2\setminus\{(x,0)\mid x\ge0\}$，这是一个全测度集。Jacobi 矩阵为

$$
D\varphi(r,\theta)=\begin{bmatrix}\cos\theta&-r\sin\theta\\ \sin\theta&r\cos\theta\end{bmatrix},\qquad\det D\varphi(r,\theta)=r,
$$
由定理 8.4.1，$(R,\Theta)=\varphi^{-1}(X,Y)$ 的密度为

$$
f(r,\theta)=g(\varphi(r,\theta))\,\lvert\det D\varphi(r,\theta)\rvert=\frac1{2\pi}\cdot r\,\mathrm{e}^{-r^2/2}=f_1(\theta)f_2(r).
$$
于是 $\Theta\sim\mathrm{U}(0,2\pi)$ 与 $R$ 独立，$R$ 服从 $\sigma=1$ 的 Rayleigh 分布，由例 8.2.3 可用 $\sqrt{-2\log(1-U)}$，或等价地用 $\sqrt{-2\log U}$ 生成。

**算法 8.4.1（Box–Muller 方法）**

1. 独立地生成 $\Theta\sim\mathrm{U}(0,2\pi)$ 与 $U\sim\mathrm{U}(0,1)$。
2. 令 $R=\sqrt{-2\log U}$。
3. 则 $(X,Y)=\varphi(R,\Theta)=(R\cos\Theta,R\sin\Theta)$ 在 $\mathbb{R}^2$ 中服从标准正态分布：$X$ 与 $Y$ 是独立的 $\mathcal{N}(0,1)$。

这种把均匀样本对变成正态样本对的方法就是 **Box–Muller 方法**（Box 与 Muller，1958），在 [3.1.7](/3.1.7) 中作为变量替换的例子出现过。

### 8.4.3. 多元正态分布

设 $\boldsymbol{Z}\sim\mathcal{N}_d(\boldsymbol{0},I_d)$，即由独立标准正态变量组成的向量。为生成 $\boldsymbol{X}\sim\mathcal{N}_d(\boldsymbol\mu,\Sigma)$，分解 $\Sigma=CC^{\mathsf T}$，令 $\boldsymbol{X}=C\boldsymbol{Z}+\boldsymbol\mu$；则 $\boldsymbol{X}$ 服从正态分布，均值为 $\boldsymbol\mu$，协方差为 $C I_d C^{\mathsf T}=\Sigma$（**多元正态分布**，[3.1.15](/3.1.15)）。

实践中一次变换整个数据矩阵。设 $M=(Z_{ij})$ 是元素独立同分布于 $\mathcal{N}(0,1)$ 的 $n\times d$ 矩阵，它的行 $\boldsymbol{Z}_i^{\mathsf T}$ 是独立的 $\mathcal{N}_d(\boldsymbol 0,I_d)$ 向量。则

$$
X=\begin{bmatrix}\boldsymbol{X}_1^{\mathsf T}\\ \vdots\\ \boldsymbol{X}_n^{\mathsf T}\end{bmatrix}=\begin{bmatrix}\boldsymbol{Z}_1^{\mathsf T}C^{\mathsf T}+\boldsymbol\mu^{\mathsf T}\\ \vdots\\ \boldsymbol{Z}_n^{\mathsf T}C^{\mathsf T}+\boldsymbol\mu^{\mathsf T}\end{bmatrix}=MC^{\mathsf T}+\boldsymbol{1}\boldsymbol\mu^{\mathsf T}
$$
的各行是来自 $\mathcal{N}_d(\boldsymbol\mu,\Sigma)$ 的容量为 $n$ 的随机样本。

**算法 8.4.2（多元正态样本）**

1. 生成含 $nd$ 个独立 $\mathcal{N}(0,1)$ 随机变量值的 $n\times d$ 矩阵 $M$。
2. 计算分解 $\Sigma=CC^{\mathsf T}$。
3. 输出 $X=MC^{\mathsf T}+\boldsymbol{1}\boldsymbol\mu^{\mathsf T}$。

常用的分解有三种。

- **谱分解**：$\Sigma=P\Lambda P^{\mathsf T}$，$Q=\Sigma^{1/2}=P\Lambda^{1/2}P^{\mathsf T}$ 对称，所以 $C=C^{\mathsf T}=Q$。
- **奇异值分解**：对对称半正定矩阵，$\Sigma=UDV^{\mathsf T}$ 中 $U=V=P$，$Q=\Sigma^{1/2}=UD^{1/2}V^{\mathsf T}$ 是同一个平方根。
- **Cholesky 分解**：R 的 `chol(Sigma)` 返回上三角的 $Q$，$\Sigma=Q^{\mathsf T}Q$，所以 $C=Q^{\mathsf T}$，$X=MQ+\boldsymbol{1}\boldsymbol\mu^{\mathsf T}$。它是三者中计算量最小的。

**例 8.4.2** 用谱方法从 $\boldsymbol\mu=(0,0)^{\mathsf T}$、$\Sigma=\begin{bmatrix}1&0.9\\0.9&1\end{bmatrix}$ 的二元正态分布生成 $1000$ 个观测：

```r
rmvn.eigen <- function(n, mu, Sigma) {
  d <- length(mu)
  ev <- eigen(Sigma, symmetric = TRUE)
  lambda <- ev$values
  V <- ev$vectors
  Q <- V %*% diag(sqrt(lambda)) %*% t(V)            # Q = Sigma^(1/2)
  M <- matrix(rnorm(n*d), nrow = n, ncol = d)
  X <- M %*% Q + matrix(mu, n, d, byrow = TRUE)
  X
}
mu <- c(0, 0)
Sigma <- matrix(c(1, .9, .9, 1), nrow = 2, ncol = 2)
X <- rmvn.eigen(1000, mu, Sigma)                     # generate the sample
print(colMeans(X))
print(cor(X))
plot(X, xlab = "x", ylab = "y", pch = 20)

# SVD and Cholesky alternatives for the factor Q
S <- svd(Sigma); Q <- S$u %*% diag(sqrt(S$d)) %*% t(S$v)
Q <- chol(Sigma)                                     # Sigma = t(Q) %*% Q
```

```text
> print(colMeans(X))
[1] -0.001628189  0.023474775
> print(cor(X))
          [,1]      [,2]
[1,] 1.0000000 0.8931007
[2,] 0.8931007 1.0000000
```

样本均值接近 $0$，样本相关系数接近 $0.9$。现成的函数有程序包 `MASS` 中的 `mvrnorm` 和 `mvtnorm` 中的 `rmvnorm`；这个例子的要点是只需要 `rnorm`。

### 8.4.4. 均匀比方法

**定理 8.4.2（均匀比方法）** 设 $f\colon\mathbb{R}^d\to[0,\infty)$ 满足 $Z=\int_{\mathbb{R}^d}f(x)\,\mathrm{d}x<\infty$，$X=(X_0,X_1,\dots,X_d)$ 在

$$
A=\Bigl\{(x_0,x_1,\dots,x_d)\Bigm|x_0>0,\ \frac{x_0^{d+1}}{d+1}<f\Bigl(\frac{x_1}{x_0},\dots,\frac{x_d}{x_0}\Bigr)\Bigr\}\subseteq\mathbb{R}_+\times\mathbb{R}^d
$$
上均匀分布。则 $\boldsymbol{Y}=\bigl(\frac{X_1}{X_0},\dots,\frac{X_d}{X_0}\bigr)$ 在 $\mathbb{R}^d$ 上的密度为 $f/Z$。

**证明** 令 $B=\{(y_0,y_1,\dots,y_d)\mid0<y_0<f(y_1,\dots,y_d)/Z\}$，定义 $\varphi\colon\mathbb{R}_+\times\mathbb{R}^d\to\mathbb{R}_+\times\mathbb{R}^d$ 为

$$
\varphi(x_0,x_1,\dots,x_d)=\Bigl(\frac{x_0^{d+1}}{Z(d+1)},\frac{x_1}{x_0},\dots,\frac{x_d}{x_0}\Bigr).
$$
则 $x\in A\iff\varphi(x)\in B$，所以 $\varphi$ 把 $A$ 双射地映到 $B$ 上。Jacobi 矩阵是下三角的，对角元为 $x_0^d/Z,1/x_0,\dots,1/x_0$，所以 $\det D\varphi(x)=1/Z$。$X$ 的密度是 $\boldsymbol{1}_A(x)/\lvert A\rvert$；由定理 8.4.1，$\varphi(X)$ 的密度为 $\frac{\boldsymbol{1}_A(\varphi^{-1}(y))}{\lvert A\rvert}\cdot Z=\frac{Z}{\lvert A\rvert}\boldsymbol{1}_B(y)$，即在 $B$ 上均匀。对密度 $f/Z$ 应用定理 8.3.4，$\varphi(X)$ 的后 $d$ 个坐标 $\boldsymbol{Y}$ 的密度为 $f/Z$。 $\square$

**例 8.4.3** 对标准 Cauchy 密度 $f(x)=\frac1{\pi(1+x^2)}$ 与 $d=1$，

$$
A=\Bigl\{(x_0,x_1)\Bigm|x_0>0,\ \frac{x_0^2}{2}<\frac{1}{\pi(1+x_1^2/x_0^2)}\Bigr\}=\Bigl\{(x_0,x_1)\Bigm|x_0>0,\ x_0^2+x_1^2<\frac2\pi\Bigr\},
$$
这是 $(x_0,x_1)$ 平面中的一个半圆盘。

1. 在半圆盘 $A$ 上均匀地生成 $(X_0,X_1)$，例如从矩形 $(0,r)\times(-r,r)$（$r=\sqrt{2/\pi}$）中拒绝抽样，接受概率为 $\pi/4$。
2. 返回 $Y=X_1/X_0$。

由于只返回比值，$A$ 可以换成任意半径的半圆盘。对一般的 Cauchy 密度 $f(x;x_0,\gamma)=\dfrac{1}{\pi\gamma\bigl(1+((x-x_0)/\gamma)^2\bigr)}$，返回 $x_0+\gamma Y$。

### 8.4.5. 和与混合

和与混合是特殊类型的变换。

- **卷积**是独立随机变量之和 $S=X_1+\cdots+X_n$ 的分布。对整数 $\nu>0$，$\chi^2_\nu$ 是 $\nu$ 个独立同分布的标准正态变量平方的卷积；Pascal 分布 $\mathrm{Pascal}(r,p)$ 是 $r$ 个独立同分布的 $\mathrm{Geo}(p)$ 变量的卷积（减去 $r$ 得到**负二项分布** $\mathrm{NB}(r,p)$）；$r$ 个独立 $\mathrm{Exp}(\lambda)$ 变量的卷积是 $\Gamma(r,\lambda)$。模拟卷积时，生成 $x_1\sim X_1,\dots,x_n\sim X_n$，输出 $s=x_1+\cdots+x_n$。
- 混合分布（mixture distribution）的分布函数为 $F_X(x)=\sum_{i=1}^m\theta_iF_{X_i}(x)$，$\theta_i>0$，$\sum_i\theta_i=1$。模拟时先以 $\mathbb{P}(k=i)=\theta_i$ 生成整数 $k\in\{1,\dots,m\}$，再输出 $x\sim X_k$。与卷积不同，两个不同正态分布的混合明显不是正态的，例如可以是双峰的。

**例 8.4.4** 模拟混合 $F_X=\sum_{i=1}^5\theta_iF_{X_i}$，其中 $X_i\sim\Gamma(3,\lambda_i=1/i)$ 相互独立，$\theta_i=i/15$：

```r
n <- 5000
k <- sample(1:5, size = n, replace = TRUE, prob = (1:5)/15)
rate <- 1/k
x <- rgamma(n, shape = 3, rate = rate)
# plot the density of the mixture with the densities of the components
plot(density(x), xlim = c(0, 40), ylim = c(0, .3), lwd = 3, xlab = "x", main = "", col = 2)
for (i in 1:5)
  lines(density(rgamma(n, 3, 1/i)))   # density() computes kernel density estimates
```

![来自五个 Gamma 分布 Gamma(3, 速率 1/i)、权重 i/15 的混合的 5000 个样本值，以及混合密度与五个分量密度。](./plots/gamma-mixture.py)

## 小结

| 方法 | 目标 | 关键步骤 | 效率与注意事项 |
|---|---|---|---|
| LCG $X_{i+1}\equiv aX_i+c\pmod m$ | $\mathrm{U}(0,1)$ | $R_i=X_i/m$ | 周期 $\le m$（满周期见 Hull–Dobell 定理）；高维中有格点结构 |
| Mersenne Twister | $\mathrm{U}(0,1)$ | 扭转的 19937 比特状态 | 周期 $2^{19937}-1$；R 的默认发生器；不适用于密码学 |
| 离散逆变换 | 任意离散分布 | $K=\min\{k\colon\sum_{i\le k}p_i\ge U\}$ | 几何分布：$\lceil\log(1-U)/\log(1-p)\rceil$ |
| 逆变换法 | 一维、$F$ 可逆 | $x=F^{-1}(u)$ | 快，但需要 $F^{-1}$；只限一维 |
| 基本拒绝抽样 | $f\propto pg$ | 若 $U\le p(X)$ 则接受 | 接受概率 $Z$，平均 $1/Z$ 次试验 |
| 包络拒绝抽样 | 任意 $f\le cg$（可未归一化） | 若 $U\le f(X)/(cg(X))$ 则接受 | 接受率 $Z_f/c$；选与 $f$ 接近的 $g$，$c$ 要小 |
| 条件化 | $P_{X\mid X\in A}$ | 保留 $X\in A$ | 平均 $1/\mathbb{P}(X\in A)$ 次试验；$\mathbb{P}(A)$ 小时用包络 |
| 图像下方的均匀分布 | 任意密度 $f$ | $(X,f(X)U)$ 在 $\{0\le y<f(x)\}$ 上均匀 | 拒绝抽样背后的几何 |
| 变换法 | 借助 Jacobi 行列式的密度 | $f_Y(y)=g(\varphi^{-1}(y))\lvert\det D\varphi^{-1}(y)\rvert$ | Box–Muller：$\sqrt{-2\log U}(\cos2\pi V,\sin2\pi V)$ |
| 多元正态 | $\mathcal{N}_d(\boldsymbol\mu,\Sigma)$ | $X=MC^{\mathsf T}+\boldsymbol1\boldsymbol\mu^{\mathsf T}$，$\Sigma=CC^{\mathsf T}$ | Cholesky 分解最省 |
| 均匀比方法 | 密度 $f/Z$ | $X$ 在 $A$ 上均匀，返回 $X_1/X_0$ | Cauchy：半圆盘 |
| 混合、卷积 | $\sum\theta_iF_i$；和 | 先选分量再抽样；相加 | — |
