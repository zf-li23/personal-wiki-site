---
title: 常见随机变量
description: 离散型随机变量与分布列，两点、二项、几何、Pascal、负二项、超几何、负超几何与 Poisson 分布；连续型随机变量与概率密度，均匀、指数与正态分布；Beta、Gamma、Weibull、卡方、t、Cauchy 与 F 分布；分布之间的关系。
---

上一章 [3.1.3](/3.1.3) 引入了随机变量。本章介绍两类最重要的随机变量：只取有限个或可列个值的离散型随机变量，用分布列描述；有概率密度的连续型随机变量，用密度的积分计算概率。每一种常见分布都来自一个典型的随机试验：独立重复试验中成功的次数（二项分布）、首次成功所需的次数（几何分布）、无放回抽样中次品的个数（超几何分布）、稀有事件发生的次数（Poisson 分布）、无老化元件的寿命（指数分布）、大量微小误差的累积（正态分布）。理解这些试验背景，就能理解分布之间的关系：二项分布可以用 Poisson 分布近似，超几何分布可以用二项分布近似，几何分布与指数分布都具有无记忆性。下一章 [3.1.5](/3.1.5) 用分布函数统一处理这两类随机变量，并讨论随机变量函数的分布；它们的期望与方差见 [3.1.8](/3.1.8)。

## 4.1. 离散型随机变量

### 4.1.1. 分布列

**定义 4.1.1（离散型随机变量）** 如果随机变量 $X$ 只取有限个值 $x_1,\dots,x_m$ 或可列个值 $x_1,x_2,\dots$，则称 $X$ 是**离散型随机变量**，简称离散随机变量。

例如连续掷两次四面体骰子，$X$ 为两次点数中的最大者，则 $X$ 把 16 个样本点映射到 $\{1,2,3,4\}$ 上，是离散型随机变量。

**定义 4.1.2（分布列）** 设 $X$ 为离散型随机变量，称

$$
\mathbb{P}(X=x_k)=p_k,\qquad k\ge1
$$
为 $X$ 的概率分布，称 $\{p_k\}$ 为 $X$ 的概率分布列，简称**分布列**（probability mass function，PMF）。

当分布列 $\{p_k\}$ 的规律性不够明显时，常把概率分布写成表格

$$
\begin{array}{c|cccc}
X & x_1 & x_2 & x_3 & \cdots\\
\hline
\mathbb{P} & p_1 & p_2 & p_3 & \cdots
\end{array}
$$

分布列满足 $p_k\ge0$ 与 $\sum_kp_k=1$（由可列可加性，因为 $\bigcup_k\{X=x_k\}=\Omega$）；反过来，满足这两条的数列都是某个离散型随机变量的分布列。对任意 Borel 集 $A$，$\mathbb{P}(X\in A)=\sum_{k\colon x_k\in A}p_k$。

### 4.1.2. 两点分布

任何试验，当只考虑成功与否（产品是否合格、是否健康、电话机是否待机等）时，都可以用随机变量 $X=1$（成功）、$X=0$（不成功）描述。

**定义 4.1.3（两点分布）** 如果 $X$ 只取值 0 或 1，概率分布是 $\mathbb{P}(X=1)=p=1-\mathbb{P}(X=0)$，则称 $X$ 服从**两点分布**，也称 **Bernoulli 分布**，记作 $X\sim\mathrm{Ber}(p)$（也记作 $\mathrm{Bin}(1,p)$）。其分布列为

$$
\begin{array}{c|cc}
X & 0 & 1\\
\hline
\mathbb{P} & 1-p & p
\end{array}
$$

事件 $A$ 的指示函数 $\boldsymbol{1}_A$ 服从 $\mathrm{Ber}(\mathbb{P}(A))$。只有两种结果、每次成功概率都是 $p$ 且相互独立的重复试验，称为 Bernoulli 试验（Bernoulli trials）。

### 4.1.3. 二项分布

**例 4.1.1** 设试验 $S$ 成功的概率为 $p$，将试验 $S$ 独立地重复 $n$ 次，用 $X$ 表示成功的次数，求 $\mathbb{P}(X=k)$。用 $A_j$ 表示第 $j$ 次试验成功，则 $A_1,\dots,A_n$ 相互独立，$\mathbb{P}(A_j)=p$。从 $n$ 次试验中选定 $k$ 次的方法共有 $\binom nk$ 种；对第 $i$ 种选法，设选出的是第 $j_1,\dots,j_k$ 次，令

$$
B_i=A_{j_1}\cap\cdots\cap A_{j_k}\cap A_{j_{k+1}}^{\mathsf c}\cap\cdots\cap A_{j_n}^{\mathsf c}
$$
表示第 $j_1,\dots,j_k$ 次成功、其余不成功。则 $\{B_i\}$ 互不相容，$\{X=k\}=\bigcup_{i=1}^{\binom nk}B_i$，且由独立性 $\mathbb{P}(B_i)=p^k(1-p)^{n-k}$。由有限可加性，

$$
\mathbb{P}(X=k)=\sum_{i=1}^{\binom nk}\mathbb{P}(B_i)=\binom nkp^k(1-p)^{n-k}.
$$
它恰是二项展开式 $1=\{p+(1-p)\}^n=\sum_{k=0}^n\binom nkp^k(1-p)^{n-k}$ 的第 $k+1$ 项，"二项分布"由此得名。

**定义 4.1.4（二项分布）** 如果随机变量 $X$ 的概率分布为

$$
\mathbb{P}(X=k)=\binom nkp^k(1-p)^{n-k},\qquad k=0,1,\dots,n,
$$
其中 $p\in(0,1)$，则称 $X$ 服从**二项分布**，记作 $X\sim\mathrm{Bin}(n,p)$。

由例 4.1.1：如果随机变量 $X_1,\dots,X_n$ 相互独立，都服从 $\mathrm{Ber}(p)$，则 $S=X_1+\cdots+X_n\sim\mathrm{Bin}(n,p)$。由此，若 $X\sim\mathrm{Bin}(n,p)$、$Y\sim\mathrm{Bin}(m,p)$ 且相互独立，则 $X+Y\sim\mathrm{Bin}(m+n,p)$：$X+Y$ 可以看作 $m+n$ 次独立重复试验中成功的次数。

![二项分布 Bin(n, p) 的分布列（折线图），p = 0.2, 0.5, 0.8，n 从 3 到 30](./plots/binomial-pmf.py)

从图中看到，分布列先增后减，峰值的位置大约在 $np$ 处。记 $b(k;n,p)=\mathbb{P}(X=k)$，则

$$
\frac{b(k;n,p)}{b(k-1;n,p)}=\frac{(n-k+1)p}{k(1-p)}=1+\frac{(n+1)p-k}{k(1-p)}.
$$
所以当 $k<(n+1)p$ 时 $b(k;n,p)>b(k-1;n,p)$，$b(k;n,p)$ 随 $k$ 增大而增大；当 $k>(n+1)p$ 时 $b(k;n,p)$ 随 $k$ 增大而减小；当 $k=(n+1)p$ 时两项相等。这就证明了：

**定理 4.1.1（二项分布的最可能值）** 二项分布的最可能值 $k_0$，即满足 $b(k_0;n,p)=\max_{0\le k\le n}b(k;n,p)$ 的整数，存在，且

$$
k_0=\begin{cases}(n+1)p\ \text{与}\ (n+1)p-1, & (n+1)p\ \text{为整数},\\ \lfloor(n+1)p\rfloor, & (n+1)p\ \text{不是整数}.\end{cases}
$$
即 $(n+1)p$ 为整数时 $b((n+1)p;n,p)$ 与 $b((n+1)p-1;n,p)$ 都是最大项，否则 $b(\lfloor(n+1)p\rfloor;n,p)$ 是唯一的最大项。$b(k_0;n,p)$ 称为二项分布的中心项。

**例 4.1.2** 一个人向同一目标连打 9 枪，每次射击相互独立，击中的概率都是 $0.3$。求有两次以上击中目标的概率，以及最可能击中目标的次数。设 $X$ 为击中目标的次数，则 $X\sim\mathrm{Bin}(9,0.3)$，

$$
\mathbb{P}(X>2)=1-\sum_{k=0}^2\binom9k(0.3)^k(0.7)^{9-k}=1-0.4628=0.5372.
$$
又 $(n+1)p=10\times0.3=3$ 为整数，所以最可能击中目标的次数是 3 或 2。

### 4.1.4. 几何分布

**例 4.1.3** 甲向一个目标射击，直到击中为止，每次击中的概率是 $p>0$，各次射击相互独立。用 $X$ 表示首次击中目标时的射击次数，求 $\mathbb{P}(X=k)$。用 $A_j$ 表示第 $j$ 次没有击中，由独立性，

$$
\mathbb{P}(X=k)=\mathbb{P}(A_1\cap\cdots\cap A_{k-1}\cap A_k^{\mathsf c})=(1-p)^{k-1}p,\qquad k=1,2,\dots
$$
注意 $\mathbb{P}(X<\infty)=\sum_{k=1}^\infty(1-p)^{k-1}p=1$：一直射击下去总有击中的时候，独立重复试验一直做下去总会成功。

**定义 4.1.5（几何分布）** 如果随机变量 $X$ 的概率分布为

$$
\mathbb{P}(X=k)=(1-p)^{k-1}p,\qquad k=1,2,\dots,
$$
其中 $0<p\le1$，则称 $X$ 服从参数为 $p$ 的**几何分布**，记作 $X\sim\mathrm{Geo}(p)$。

名称来自**几何级数**：分布列是公比为 $1-p$ 的等比数列。几何分布的一个特征是：已知前 $k$ 次都失败，此后还需要的次数 $X-k$ 与 $X$ 同分布，好像过去的失败被"忘记"了。

**定理 4.1.2（几何分布的无记忆性）** 取正整数值的随机变量 $X$ 服从几何分布 $\mathrm{Geo}(p)$ 的充要条件是：对每个 $k\ge1$（使 $\mathbb{P}(X>k)>0$），

$$
\mathbb{P}(X=k+1\mid X>k)=\mathbb{P}(X=1).
$$
这一性质称为无记忆性（memorylessness）。

**证明** 必要性。由条件概率的定义，

$$
\mathbb{P}(X=k+1\mid X>k)=\frac{\mathbb{P}(X=k+1)}{\mathbb{P}(X>k)}=\frac{(1-p)^kp}{\sum_{j=k+1}^\infty(1-p)^{j-1}p}=\frac{(1-p)^kp}{(1-p)^k}=p=\mathbb{P}(X=1).
$$
充分性。记 $p=\mathbb{P}(X=1)$，$r_k=\mathbb{P}(X>k)$，则 $r_0=1$。由 $\{X=k+1\}=\{X>k\}\setminus\{X>k+1\}$，

$$
p=\mathbb{P}(X=k+1\mid X>k)=\frac{r_k-r_{k+1}}{r_k}=1-\frac{r_{k+1}}{r_k},
$$
所以 $r_{k+1}=(1-p)r_k=\cdots=(1-p)^{k+1}r_0=(1-p)^{k+1}$。因此 $\mathbb{P}(X=k)=r_{k-1}-r_k=(1-p)^{k-1}p$。 $\square$

等价地，对任意正整数 $m,k$，$\mathbb{P}(X>m+k\mid X>m)=\mathbb{P}(X>k)$。

### 4.1.5. Pascal 分布与负二项分布

**例 4.1.4** 甲向一个目标射击，直到击中 $r$ 次为止，每次击中的概率是 $p\in(0,1)$，各次独立。用 $X$ 表示射击停止时的射击次数。$X=k$ 当且仅当第 $k$ 次击中，且前 $k-1$ 次中恰有 $r-1$ 次击中，所以 $\mathbb{P}(X=k)=\binom{k-1}{r-1}(1-p)^{k-r}p^r$，$k=r,r+1,\dots$。

**定义 4.1.6（Pascal 分布）** 如果随机变量 $X$ 的概率分布为

$$
\mathbb{P}(X=k)=\binom{k-1}{r-1}(1-p)^{k-r}p^r,\qquad k=r,r+1,\dots,
$$
则称 $X$ 服从 **Pascal 分布**，记作 $X\sim\mathrm{Pascal}(r,p)$。当 $r=1$ 时，Pascal 分布就是几何分布。

在例 4.1.4 中，令 $Y=X-r$，则 $Y$ 是射击停止时失败（未击中）的次数。

**定义 4.1.7（负二项分布）** 如果随机变量 $Y$ 的概率分布为

$$
\mathbb{P}(Y=k)=\binom{k+r-1}{r-1}(1-p)^kp^r,\qquad k=0,1,\dots,\tag{4.1}
$$
则称 $Y$ 服从**负二项分布**，记作 $Y\sim\mathrm{NB}(r,p)$。

名称有两个来源。其一是"负指数的二项展开式"：对 $\lvert x\rvert<1$，

$$
(1-x)^{-r}=\sum_{k=0}^\infty\frac{(-r)(-r-1)\cdots(-r-k+1)}{k!}(-x)^k=\sum_{k=0}^\infty\binom{k+r-1}{r-1}x^k,
$$
令 $x=1-p$ 并乘以 $p^r$，得 $1=\sum_{k=0}^\infty\binom{k+r-1}{r-1}(1-p)^kp^r$，这也验证了式 (4.1) 确实是分布列。其二是试验方式与二项分布"反其道而行之"：二项分布定下试验次数 $n$，把成功次数作为随机变量；负二项分布定下成功次数 $r$，把所需的试验次数（减去 $r$）作为随机变量。

**例 4.1.5** 为了检查某厂产品的废品率 $p$，有两个方案：一是有放回地抽取 $n$ 个产品，检查其中的废品数，这导致二项分布；二是先指定自然数 $r$，一个一个有放回地抽样，直到发现第 $r$ 个废品为止，记录已检出的合格品个数 $X\sim\mathrm{NB}(r,p)$。$p$ 小时 $X$ 倾向于取较大的值，反之倾向于取较小的值，所以 $X$ 也可以用来研究 $p$。

### 4.1.6. 超几何分布与负超几何分布

**定义 4.1.8（超几何分布）** 在包含 $N$ 个元素的总体中，$M$ 个是红的，$N-M$ 个是黑的。任取 $n$ 个元素（无放回），其中红元素的个数 $X$ 的概率分布为

$$
\mathbb{P}(X=k)=\frac{\binom Mk\binom{N-M}{n-k}}{\binom Nn},\qquad k=0,1,\dots,\min\{n,M\},
$$
称 $X$ 服从**超几何分布**（hypergeometric distribution），记作 $X\sim\mathrm{H}(n,M,N)$。这里约定 $m>l$ 时 $\binom lm=0$，所以 $k<n-(N-M)$ 时概率为零。

超几何分布用于质量检测（$N$ 件产品中恰有 $M$ 件次品，从中任取 $n$ 件，次品数服从 $\mathrm{H}(n,M,N)$）和捕获–再捕获模型（估计湖中鱼的数量）。如果产品充分多，无放回抽取和有放回抽取应当没有多大差别；有放回抽取时次品数 $\tilde X\sim\mathrm{Bin}(n,p_N)$，$p_N=M/N$ 是次品率。

**定理 4.1.3（超几何分布的二项近似）** 设 $X_N\sim\mathrm{H}(n,M,N)$，$n$ 固定，$N\to\infty$ 时 $M/N\to p$，则对每个 $m=0,1,\dots,n$，

$$
\lim_{N\to\infty}\mathbb{P}(X_N=m)=\binom nmp^m(1-p)^{n-m}.
$$

**证明** 展开组合数，

$$
\mathbb{P}(X_N=m)=\binom nm\cdot\frac{M(M-1)\cdots(M-m+1)}{N^m}\cdot\frac{(N-M)\cdots(N-M-n+m+1)}{N^{n-m}}\cdot\frac{N^n}{N(N-1)\cdots(N-n+1)}.
$$
$N\to\infty$ 时，第二个因子的 $m$ 个分式都趋于 $p$，第三个因子的 $n-m$ 个分式都趋于 $1-p$，最后一个因子趋于 1。 $\square$

实际问题中，对较大的 $N$，计算 $\binom Nn$、$\binom Mm$、$\binom{N-M}{n-m}$ 比计算 $\binom nm$ 费时得多；而抽样个数 $n$ 一般不大，所以对较大的 $N$ 和 $M$，采用近似 $\mathrm{H}(n,M,N)\approx\mathrm{Bin}(n,M/N)$ 往往更方便。

**定义 4.1.9（负超几何分布）** 在上述总体中，每次无放回地抽取一个元素，直到抽到 $r$ 个红元素为止（$1\le r\le M$）。此时已抽到的黑元素个数 $X$ 的概率分布为

$$
\mathbb{P}(X=k)=\frac{\binom{k+r-1}k\binom{N-k-r}{M-r}}{\binom NM},\qquad k=0,1,\dots,N-M,
$$
称 $X$ 服从**负超几何分布**（negative hypergeometric distribution），记作 $X\sim\mathrm{NH}(r,M,N)$。

推导：把 $N$ 个元素全部依次排开，红元素位置的组合有 $\binom NM$ 种，等可能。$X=k$ 当且仅当第 $r$ 个红元素位于第 $k+r$ 位，即前 $k+r-1$ 位中恰有 $r-1$ 个红元素（$\binom{k+r-1}{r-1}=\binom{k+r-1}k$ 种），后 $N-k-r$ 位中恰有 $M-r$ 个红元素（$\binom{N-k-r}{M-r}$ 种）。与定理 4.1.3 类似，$N\to\infty$、$M/N\to p$ 时，$\mathrm{NH}(r,M,N)$ 趋于 $\mathrm{NB}(r,p)$。

### 4.1.7. Poisson 分布

**定义 4.1.10（Poisson 分布）** 如果随机变量 $X$ 的概率分布为

$$
\mathbb{P}(X=k)=\frac{\lambda^k}{k!}\mathrm{e}^{-\lambda},\qquad k=0,1,2,\dots,
$$
其中 $\lambda$ 是正常数，则称 $X$ 服从参数为 $\lambda$ 的 **Poisson 分布**，记作 $X\sim\mathrm{Poi}(\lambda)$。

由 $\mathrm{e}^\lambda$ 的 **Taylor 级数**，$\sum_k\lambda^k\mathrm{e}^{-\lambda}/k!=1$。Poisson 分布描述单位时间（或单位面积、体积）内稀有事件发生的次数：某段高速公路上一年内的交通事故数，某市场一天中到达的顾客数，某办公室一天中收到的电话数，某大学一天中上课迟到的总人数，一张纸上的雨点数等。参数 $\lambda$ 是事件发生的平均次数（见 [3.1.8](/3.1.8)）。

**例 4.1.6（放射性衰变）** 1910 年，Rutherford 和 Geiger 观察放射性物质钋放射 $\alpha$ 粒子的情况：进行了 $N=2608$ 次观测，每次 7.5 秒，一共观察到 10094 个 $\alpha$ 粒子。用 $X$ 表示 7.5 秒内放射出的 $\alpha$ 粒子数，$m_k$ 表示观察到 $k$ 个粒子的次数，取 $\lambda=10094/2608\approx3.87$（7.5 秒内放射出 $\alpha$ 粒子的平均数），$Y\sim\mathrm{Poi}(3.87)$：

| $k$ | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | $\ge10$ |
|---|---|---|---|---|---|---|---|---|---|---|---|
| $m_k$ | 57 | 203 | 383 | 525 | 532 | 408 | 273 | 139 | 45 | 27 | 16 |
| $m_k/N$ | 0.022 | 0.078 | 0.147 | 0.201 | 0.204 | 0.156 | 0.105 | 0.053 | 0.017 | 0.010 | 0.006 |
| $\mathbb{P}(Y=k)$ | 0.021 | 0.081 | 0.156 | 0.201 | 0.195 | 0.151 | 0.097 | 0.054 | 0.026 | 0.011 | 0.007 |

事件 $\{X=k\}$ 在 2608 次重复观测中发生的频率与 $\mathbb{P}(Y=k)$ 基本相同。为什么会有这样的规律？设想把 $t=7.5$ 秒等分成 $n$ 段，每段 $\delta_n=t/n$ 秒，对充分大的 $n$ 假定：

1. 在每个 $\delta_n$ 内最多只有一个 $\alpha$ 粒子放出，放出一个粒子的概率是 $p_n=\mu\delta_n=\mu t/n$，$\mu$ 是正常数；
2. 各个小时间段内是否放出 $\alpha$ 粒子相互独立。

在这些假定下，放出的粒子数 $X\sim\mathrm{Bin}(n,p_n)$。令 $n\to\infty$，由下面的定理 4.1.4（取 $\lambda=\mu t$）得 $X\sim\mathrm{Poi}(\lambda)$。

**定理 4.1.4（Poisson 定理）** 若 $n\to\infty$ 时 $np_n\to\lambda>0$，则对每个 $k=0,1,2,\dots$，

$$
\lim_{n\to\infty}\binom nkp_n^k(1-p_n)^{n-k}=\frac{\lambda^k}{k!}\mathrm{e}^{-\lambda}.
$$

**证明** 记 $\lambda_n=np_n$，则

$$
\binom nkp_n^k(1-p_n)^{n-k}=\frac{\lambda_n^k}{k!}\cdot\frac{n(n-1)\cdots(n-k+1)}{n^k}\cdot\Big(1-\frac{\lambda_n}n\Big)^{n}\cdot\Big(1-\frac{\lambda_n}n\Big)^{-k}.
$$
$n\to\infty$ 时，第二个因子趋于 1，最后一个因子趋于 1；由 $\lim_{x\to0}(1+x)^{1/x}=\mathrm{e}$，第三个因子趋于 $\mathrm{e}^{-\lambda}$。 $\square$

所以如果 $n$ 很大，$p$ 很小，$np\approx\lambda$ 是大小适当的常数，可以用 $\mathrm{Poi}(\lambda)$ 近似 $\mathrm{Bin}(n,p)$；当 $n$ 无法确定（例如路上的车辆数）而只知道平均次数时，就应该使用 Poisson 分布。

![左：Poisson 分布 Poi(λ) 的分布列，λ = 1, …, 6；中：Bin(n, 3/n) 随 n 增大趋于 Poi(3)；右：Rutherford–Geiger 实验中 α 粒子数的频率与 Poi(3.87) 的比较](./plots/poisson-approximation.py)

## 4.2. 连续型随机变量

### 4.2.1. 概率密度

测量误差、元件寿命、身高等随机变量可以在一个区间内连续取值，每个单点的概率都是零，需要用"概率在实数轴上的分布密度"来描述。

**定义 4.2.1（连续型随机变量）** 设 $X$ 是随机变量。如果存在非负函数 $f(x)$，使得对任意 $a<b$，

$$
\mathbb{P}(a<X\le b)=\int_a^bf(x)\,\mathrm{d}x,
$$
则称 $X$ 是**连续型随机变量**（continuous random variable），称 $f(x)$ 是 $X$ 的概率密度函数，简称**概率密度**或密度（probability density function，PDF）。

**性质 4.2.1** 设 $f(x)$ 是 $X$ 的概率密度，则

1. $\int_{-\infty}^\infty f(x)\,\mathrm{d}x=1$；
2. 对任意 Borel 集 $A$，$\mathbb{P}(X\in A)=\int_Af(x)\,\mathrm{d}x$；
3. 对任意 $a\in\mathbb{R}$，$\mathbb{P}(X=a)=0$，从而 $\mathbb{P}(a<X\le b)=\mathbb{P}(a\le X\le b)=\mathbb{P}(a<X<b)$。

**证明** (1) 事件 $A_n=\{X\in(-n,n]\}$ 单调递增，$\bigcup_nA_n=\Omega$。由概率的连续性（[3.1.2](/3.1.2) 定理 2.2.1），

$$
\int_{-\infty}^\infty f(x)\,\mathrm{d}x=\lim_{n\to\infty}\int_{-n}^nf(x)\,\mathrm{d}x=\lim_{n\to\infty}\mathbb{P}(A_n)=\mathbb{P}\Big(\bigcup_{n=1}^\infty A_n\Big)=1.
$$
(2) 需要测度论（两个概率测度在全体区间上相等，则在全体 Borel 集上相等），这里从略。(3) 对任意 $\varepsilon>0$，$\mathbb{P}(X=a)\le\mathbb{P}(a-\varepsilon<X\le a)=\int_{a-\varepsilon}^af(x)\,\mathrm{d}x\to0$（$\varepsilon\downarrow0$）。 $\square$

反过来，任何满足 $f\ge0$、$\int_{-\infty}^\infty f(x)\,\mathrm{d}x=1$ 的函数都是某个连续型随机变量的密度。要注意几点：

- 密度不是概率，$f(x)$ 可以大于 1；$f(x)\,\delta$ 近似是 $X$ 落在 $(x,x+\delta]$ 中的概率。
- 密度函数未必有界。例如 $f(x)=\dfrac1{2\sqrt x}$，$x\in(0,1]$（其余处为 0）是密度，但 $\lim_{x\downarrow0}f(x)=+\infty$。
- 密度不唯一：在有限个（甚至可列个）点上改变 $f$ 的值不影响积分。
- "连续型随机变量"并不是说 $X(\omega)$ 是 $\omega$ 的连续函数：样本空间 $\Omega$ 没有任何拓扑结构，谈不上连续性。它的意思是 $X$ 的分布函数绝对连续（见 [3.1.5](/3.1.5)）。

### 4.2.2. 均匀分布

**定义 4.2.2（均匀分布）** 对 $a<b$，如果 $X$ 的概率密度是

$$
f(x)=\begin{cases}\dfrac1{b-a}, & x\in(a,b),\\ 0, & x\notin(a,b),\end{cases}
$$
称 $X$ 服从区间 $(a,b)$ 上的**均匀分布**（uniform distribution），记作 $X\sim\mathrm{U}(a,b)$。

由性质 4.2.1 (3)，区间 $(a,b)$ 写成 $(a,b]$、$[a,b)$ 或 $[a,b]$ 都不影响分布。密度也可以用指示函数写成 $f(x)=\frac1{b-a}\boldsymbol{1}_{(a,b)}(x)$。对 $(a,b)$ 的子区间 $(c,d)$，$\mathbb{P}(c<X<d)=\frac{d-c}{b-a}$ 只与子区间的长度有关，这正是 [3.1.1](/3.1.1) 的几何概型。

一般地，对 $\mathbb{R}^r$ 中体积 $0<m(A)=\int_A1\,\mathrm{d}x<\infty$ 的 Borel 集 $A$，若 $X$ 的密度是 $f(x)=\frac1{m(A)}\boldsymbol{1}_A(x)$，称 $X$ 服从 $A$ 上的均匀分布，记作 $X\sim\mathrm{U}(A)$。此时对任意 Borel 集 $B$，$\mathbb{P}(X\in B)=m(A\cap B)/m(A)$。

### 4.2.3. 指数分布

**定义 4.2.3（指数分布）** 对正常数 $\lambda$，如果 $X$ 的概率密度是

$$
f(x)=\begin{cases}\lambda\mathrm{e}^{-\lambda x}, & x\ge0,\\ 0, & x<0,\end{cases}
$$
称 $X$ 服从参数为 $\lambda$ 的**指数分布**（exponential distribution），记作 $X\sim\mathrm{Exp}(\lambda)$。

指数分布描述到发生某个事件为止所用的时间、一台仪器的使用寿命等。$X$ 超过某个值的概率随着这个值的增加按指数递减：对 $a\ge0$，$\mathbb{P}(X>a)=\int_a^\infty\lambda\mathrm{e}^{-\lambda y}\,\mathrm{d}y=\mathrm{e}^{-\lambda a}$。$\lambda$ 称为速率参数（rate parameter），$1/\lambda$ 是平均寿命；另一种常见的参数化是 $f(x)=\frac1\theta\mathrm{e}^{-x/\theta}\boldsymbol{1}_{(0,\infty)}(x)$，$\theta=1/\lambda$ 是尺度参数（scale parameter）。若 $X\sim\mathrm{Exp}(\lambda)$，则 $\lambda X\sim\mathrm{Exp}(1)$（见 [3.1.5](/3.1.5) 的线性变换）。当 $\mathbb{P}(X<0)=0$ 时，称 $X$ 是非负随机变量。

**定理 4.2.1（指数分布的无记忆性）** 设 $X$ 是连续型非负随机变量，则 $X$ 服从指数分布的充要条件是 $X$ 有无记忆性，即对任意 $s,t\ge0$，

$$
\mathbb{P}(X>s+t\mid X>s)=\mathbb{P}(X>t).\tag{4.2}
$$

**证明** 必要性。设 $X\sim\mathrm{Exp}(\lambda)$，则 $\mathbb{P}(X>x)=\mathrm{e}^{-\lambda x}$，

$$
\mathbb{P}(X>s+t\mid X>s)=\frac{\mathbb{P}(X>s+t,\,X>s)}{\mathbb{P}(X>s)}=\frac{\mathrm{e}^{-\lambda(s+t)}}{\mathrm{e}^{-\lambda s}}=\mathrm{e}^{-\lambda t}=\mathbb{P}(X>t).
$$
充分性。令 $G(x)=\mathbb{P}(X>x)$，则 $G$ 单调非增、右连续，$G(0)=1$（$X$ 连续非负，$\mathbb{P}(X=0)=0$），$G(x)\to0$（$x\to\infty$）。由式 (4.2)，$G(s+t)=G(s)G(t)$ 对一切 $s,t\ge0$ 成立。于是 $G(1)=G(1/n)^n$，$G(m/n)=G(1)^{m/n}$；记 $G(1)=\mathrm{e}^{-\lambda}$，由 $G(x)\to0$ 知 $G(1)<1$；若 $G(1)=0$，则 $G(1/n)=0$ 对一切 $n$ 成立，由右连续性 $G(0)=0$，矛盾。所以 $0<\lambda<\infty$，对一切正有理数 $x$ 有 $G(x)=\mathrm{e}^{-\lambda x}$，再由单调性推广到一切 $x\ge0$。最后，对 $0\le a<b$，

$$
\mathbb{P}(a<X\le b)=G(a)-G(b)=\mathrm{e}^{-\lambda a}-\mathrm{e}^{-\lambda b}=\int_a^b\lambda\mathrm{e}^{-\lambda y}\,\mathrm{d}y,
$$
即 $X\sim\mathrm{Exp}(\lambda)$。 $\square$

从可靠性的角度看，元件在时刻 $t$ 尚能正常工作的条件下，单位时间内失效的概率（失效率）为

$$
\lim_{\Delta t\to0}\frac{\mathbb{P}(t<X\le t+\Delta t\mid X>t)}{\Delta t}=\lim_{\Delta t\to0}\frac{1-\mathrm{e}^{-\lambda\Delta t}}{\Delta t}=\lambda,
$$
与 $t$ 无关。所以无记忆性就是说元件的失效率总保持为常数 $\lambda$。指数分布描述了元件无老化时的寿命分布；"无老化"是不可能的，因而这只是一种近似，但对一些寿命长的元件，在初期阶段老化现象很小，指数分布比较确切地描述了这一阶段的寿命。几何分布与指数分布的关系见 [3.1.5](/3.1.5)。

### 4.2.4. 正态分布

正态分布有三个来源。其一，de Moivre（1733）与 Laplace（1812）发现，若 $X_n\sim\mathrm{Bin}(n,p)$，则

$$
\lim_{n\to\infty}\mathbb{P}\bigg(\frac{X_n-np}{\sqrt{np(1-p)}}\le x\bigg)=\int_{-\infty}^x\frac1{\sqrt{2\pi}}\mathrm{e}^{-t^2/2}\,\mathrm{d}t,
$$
这就是 de Moivre–Laplace **中心极限定理**（[3.1.13](/3.1.13)）。其二，天文学中的测量误差：Simpson 曾尝试用三角形分布、Laplace（1774）曾用密度 $\frac\theta2\mathrm{e}^{-\theta\lvert x\rvert}$ 描述误差；Gauss（1809）假设观测值 $X=\theta+\varepsilon$（$\theta$ 是未知的真值，$\varepsilon$ 是随机误差），并要求 $\theta$ 的**极大似然估计**恰好是观测值的平均，由此得到正态分布。正态分布因此又称 Gauss 分布。其三，在 Brown 运动的研究中人们也得到了正态分布；事实表明，产品的许多质量指标、生物的许多生理指标都服从或近似服从正态分布，大量独立同分布的随机变量之和也近似服从正态分布。

**定义 4.2.4（正态分布）** 如果 $X$ 的密度是

$$
f(x)=\frac1{\sigma\sqrt{2\pi}}\exp\Big\{-\frac{(x-\mu)^2}{2\sigma^2}\Big\},\qquad x\in\mathbb{R},\tag{4.3}
$$
其中 $\mu\in\mathbb{R}$，$\sigma>0$，称 $X$ 服从参数为 $(\mu,\sigma^2)$ 的**正态分布**（normal distribution），也称 Gauss 分布，记作 $X\sim\mathcal{N}(\mu,\sigma^2)$。特别地，当 $X\sim\mathcal{N}(0,1)$ 时，称 $X$ 服从**标准正态分布**，其密度记作

$$
\varphi(x)=\frac1{\sqrt{2\pi}}\exp\Big\{-\frac{x^2}2\Big\},\qquad x\in\mathbb{R}.
$$

$\varphi$ 确实是密度：利用极坐标，

$$
\Big(\int_{-\infty}^\infty\varphi(x)\,\mathrm{d}x\Big)^2=\frac1{2\pi}\int_{-\infty}^\infty\int_{-\infty}^\infty\mathrm{e}^{-(x^2+y^2)/2}\,\mathrm{d}x\,\mathrm{d}y=\frac1{2\pi}\int_0^{2\pi}\mathrm{d}\theta\int_0^\infty r\mathrm{e}^{-r^2/2}\,\mathrm{d}r=1,
$$
这就是 **Gauss 积分**。作变换 $y=(x-\mu)/\sigma$ 即知式 (4.3) 中的 $f$ 也是密度。正态分布的密度呈钟形，又称钟形分布，具有以下性质：

1. $f(x)$ 关于 $x=\mu$ 对称；
2. $f(\mu)=(\sigma\sqrt{2\pi})^{-1}$ 是最大值，$\sigma$ 越小峰越高越窄；
3. $f(x)$ 在 $x=\mu\pm\sigma$ 处有拐点。

正态分布在理论上有许多优良的性质（例如独立正态变量的线性组合仍是正态的、给定方差时熵最大），在概率论和统计中有特殊的地位。标准正态分布函数 $\Phi$ 与"$3\sigma$ 原则"见 [3.1.5](/3.1.5)，多元推广见 [3.1.15](/3.1.15)。

![常见连续型分布的密度：指数分布、正态分布、Beta 分布和 Gamma 分布（速率 λ = 1）](./plots/continuous-densities.py)

## 4.3. 其他连续型分布

本节的分布将在后续各章陆续用到（随机变量函数的分布、次序统计量、抽样分布），集中列在这里便于查阅。

### 4.3.1. Beta 分布与 Gamma 分布

**定义 4.3.1（Beta 分布）** 设 $\alpha,\beta$ 是正常数。如果 $X$ 的密度是

$$
f(x)=\frac1{\mathrm{B}(\alpha,\beta)}x^{\alpha-1}(1-x)^{\beta-1},\qquad0<x<1,
$$
其中 $\mathrm{B}(\alpha,\beta)=\dfrac{\Gamma(\alpha)\Gamma(\beta)}{\Gamma(\alpha+\beta)}$ 是 **Beta 函数**，则称 $X$ 服从参数为 $(\alpha,\beta)$ 的 **Beta 分布**，记作 $X\sim\mathrm{Beta}(\alpha,\beta)$。

$\alpha=\beta=1$ 时为均匀分布 $\mathrm{U}(0,1)$；$\alpha=2,\beta=1$ 时密度 $2x$ 是直线；$\alpha=\beta=1/2$ 时密度呈 U 形（两端趋于无穷）；$\alpha=\beta=2$ 时密度 $6x(1-x)$ 呈倒 U 形。Beta 分布是 $\mathrm{U}(0,1)$ 次序统计量的分布（[3.1.7](/3.1.7)），也常在贝叶斯统计中作为比例参数的**先验分布**：若 $X\mid p\sim\mathrm{Bin}(n,p)$，$p$ 的先验为 $\mathrm{Beta}(\alpha,\beta)$，则观测 $X$ 后 $p$ 的**后验分布**是 $\mathrm{Beta}(\alpha+X,\beta+n-X)$（见 [3.2.7](/3.2.7)）。

**定义 4.3.2（Gamma 分布）** 设 $\alpha,\lambda$ 是正常数。如果 $X$ 的密度是

$$
f(x)=\frac{\lambda^\alpha}{\Gamma(\alpha)}x^{\alpha-1}\mathrm{e}^{-\lambda x},\qquad x>0,
$$
称 $X$ 服从参数为 $(\alpha,\lambda)$ 的 **Gamma 分布**，记作 $X\sim\Gamma(\alpha,\lambda)$。这里 $\Gamma(\alpha)=\int_0^\infty x^{\alpha-1}\mathrm{e}^{-x}\,\mathrm{d}x$ 是 **Gamma 函数**，它满足 $\Gamma(\alpha+1)=\alpha\Gamma(\alpha)$，$\Gamma(n)=(n-1)!$，$\Gamma(1/2)=\sqrt\pi$。

$\alpha$ 称为形状参数（shape parameter），$\lambda$ 称为速率参数（rate parameter），$1/\lambda$ 是尺度参数。$\alpha=1$ 时为指数分布 $\mathrm{Exp}(\lambda)$；$\alpha$ 为正整数时称为 Erlang 分布（Erlang distribution），用于排队论（它是 $\alpha$ 个独立的 $\mathrm{Exp}(\lambda)$ 之和的分布，见 [3.1.7](/3.1.7)）。Karl Pearson 在研究物理、生物及经济中的随机变量时发现，很多只取非负值的连续型随机变量不服从正态分布，Gamma 分布就是他研究的 Pearson 分布族中的一类；在气象学中，干旱地区的年、季或月降水量被认为服从 Gamma 分布。

### 4.3.2. Weibull 分布

**定义 4.3.3（Weibull 分布）** 设 $\alpha,\lambda>0$。如果 $X$ 的密度是

$$
f(x)=\lambda\alpha x^{\alpha-1}\exp\{-\lambda x^\alpha\},\qquad x\ge0,
$$
称 $X$ 服从参数为 $(\alpha,\lambda)$ 的 **Weibull 分布**。

$\mathbb{P}(X>x)=\exp\{-\lambda x^\alpha\}$。$\alpha=1$ 时为指数分布；$\alpha=2$、$\lambda=1/(2\sigma^2)$ 时为 Rayleigh 分布（Rayleigh distribution），密度为 $f(x;\sigma)=\frac x{\sigma^2}\exp\{-\frac{x^2}{2\sigma^2}\}$，$x\ge0$。Weibull 分布的失效率 $\lambda\alpha x^{\alpha-1}$ 在 $\alpha>1$ 时随时间增大（老化），在 $\alpha<1$ 时减小，所以它与指数分布一起在可靠性分析中占有重要地位。

### 4.3.3. 卡方分布、t 分布、Cauchy 分布与 F 分布

这四个分布是统计推断中最重要的抽样分布，它们与正态分布的关系在 [3.1.7](/3.1.7) 与 [3.2.2](/3.2.2) 中证明。

**定义 4.3.4（卡方分布）** 设 $\nu>0$。如果 $X$ 的密度是

$$
f(x)=\frac1{2^{\nu/2}\Gamma(\nu/2)}x^{\nu/2-1}\mathrm{e}^{-x/2},\qquad x>0,
$$
称 $X$ 服从参数（**自由度**）为 $\nu$ 的**卡方分布**（chi-squared distribution），记作 $X\sim\chi^2_\nu$。

比较密度可知 $\chi^2_\nu=\Gamma(\nu/2,1/2)$。若 $Z_1,\dots,Z_n\overset{\text{iid}}{\sim}\mathcal{N}(0,1)$，则 $Z_1^2+\cdots+Z_n^2\sim\chi^2_n$：$n=1$ 的情形见 [3.1.5](/3.1.5) 的例 5.2.3，一般情形由 Gamma 分布的可加性得到。

**定义 4.3.5（t 分布）** 设 $\nu>0$。如果 $X$ 的密度是

$$
f(x)=\frac{\Gamma\big(\frac{\nu+1}2\big)}{\sqrt{\nu\pi}\,\Gamma\big(\frac\nu2\big)}\Big(1+\frac{x^2}\nu\Big)^{-\frac{\nu+1}2},\qquad x\in\mathbb{R},
$$
称 $X$ 服从参数为 $\nu$ 的 Student $t$ 分布，简称 **t 分布**，记作 $X\sim t_\nu$。

若 $Z\sim\mathcal{N}(0,1)$、$Y\sim\chi^2_n$ 且相互独立，则 $T=Z/\sqrt{Y/n}\sim t_n$。t 分布关于 0 对称（$T\sim t_\nu$ 时 $-T\sim t_\nu$），比正态分布重尾；$\nu$ 很大时，$t_\nu$ 和标准正态分布很接近（可以用大数定律证明，见 [3.1.12](/3.1.12)）。$\nu=1$ 是性质特殊的 Cauchy 分布。

**定义 4.3.6（Cauchy 分布）** 如果 $X$ 的密度是

$$
f(x)=\frac1{\pi(1+x^2)},\qquad x\in\mathbb{R},
$$
称 $X$ 服从标准 **Cauchy 分布**，也记作 $X\sim t_1$。一般地，$\mathrm{Cauchy}(\theta)$ 的密度为 $\frac1{\pi(1+(x-\theta)^2)}$。

Cauchy 分布的密度曲线就是 Agnesi 的箕舌线。它的尾部很重：$\int\lvert x\rvert f(x)\,\mathrm{d}x=\infty$，所以按期望的严格定义它没有期望（[3.1.8](/3.1.8)）。它还有一个反直觉的性质：若 $Z_1,\dots,Z_n\overset{\text{iid}}{\sim}t_1$，则样本均值 $(Z_1+\cdots+Z_n)/n$ 仍服从 $t_1$（[3.1.11](/3.1.11)），平均并不能使它集中，大数定律对它不成立。

**定义 4.3.7（F 分布）** 设 $m,n$ 是正整数。如果 $X$ 的密度是

$$
f(x)=\frac{\Gamma\big(\frac{m+n}2\big)m^{m/2}n^{n/2}x^{m/2-1}}{\Gamma\big(\frac m2\big)\Gamma\big(\frac n2\big)(mx+n)^{(m+n)/2}},\qquad x>0,
$$
称 $X$ 服从参数为 $(m,n)$ 的 **F 分布**（Fisher–Snedecor distribution），记作 $X\sim F_{m,n}$。

若 $X_1,\dots,X_m,Y_1,\dots,Y_n\overset{\text{iid}}{\sim}\mathcal{N}(0,1)$，则

$$
F=\frac{\frac1m\sum_{i=1}^mX_i^2}{\frac1n\sum_{j=1}^nY_j^2}\sim F_{m,n}.
$$
F 分布由英国统计学家 Fisher 于 1924 年提出并以他的名字命名，在方差分析、线性回归中有重要应用。

### 4.3.4. 分布之间的关系

各个分布之间的联系可以从它们的试验背景理解：

| 关系 | 说明 |
|---|---|
| $\mathrm{Ber}(p)\to\mathrm{Bin}(n,p)$ | $n$ 个独立的 $\mathrm{Ber}(p)$ 之和（固定试验次数，数成功次数） |
| $\mathrm{Geo}(p)\to\mathrm{Pascal}(r,p)=r+\mathrm{NB}(r,p)$ | $r$ 个独立的 $\mathrm{Geo}(p)$ 之和（固定成功次数，数试验次数） |
| $\mathrm{H}(n,M,N)\to\mathrm{Bin}(n,p)$，$\mathrm{NH}(r,M,N)\to\mathrm{NB}(r,p)$ | $N\to\infty$，$M/N\to p$：无放回抽样近似为有放回抽样 |
| $\mathrm{Bin}(n,p)\to\mathrm{Poi}(\lambda)$ | $n\to\infty$，$np\to\lambda$：稀有事件 |
| $\mathrm{Bin}(n,p)$、$\mathrm{Poi}(\lambda)\to\mathcal{N}$ | $n\to\infty$ 或 $\lambda\to\infty$ 时标准化后近似正态（中心极限定理） |
| $\mathrm{Exp}(\lambda)\to\Gamma(n,\lambda)$ | $n$ 个独立的 $\mathrm{Exp}(\lambda)$ 之和 |
| $\mathrm{Geo}(p)$ 与 $\mathrm{Exp}(\lambda)$ | 唯一具有无记忆性的离散分布与连续分布；指数分布是几何分布的连续极限（[3.1.5](/3.1.5)） |
| $\mathrm{U}(0,1)$ 与 $\mathrm{Beta}(\alpha,\beta)$ | $\mathrm{Beta}(1,1)=\mathrm{U}(0,1)$；$\mathrm{U}(0,1)$ 的次序统计量服从 Beta 分布 |
| $\mathcal{N}(0,1)\to\chi^2_n,\ t_n,\ F_{m,n}$ | 标准正态变量的平方和、比值（抽样分布） |

## 小结

| 分布 | 分布列或密度 | 背景 |
|---|---|---|
| $\mathrm{Ber}(p)$ | $\mathbb{P}(X=1)=p$，$\mathbb{P}(X=0)=1-p$ | 一次试验是否成功 |
| $\mathrm{Bin}(n,p)$ | $\binom nkp^k(1-p)^{n-k}$，$k=0,\dots,n$ | $n$ 次独立重复试验中的成功次数 |
| $\mathrm{Geo}(p)$ | $(1-p)^{k-1}p$，$k=1,2,\dots$ | 首次成功所需的试验次数；无记忆性 |
| $\mathrm{NB}(r,p)$ | $\binom{k+r-1}{r-1}(1-p)^kp^r$，$k=0,1,\dots$ | 第 $r$ 次成功前的失败次数 |
| $\mathrm{H}(n,M,N)$ | $\binom Mk\binom{N-M}{n-k}/\binom Nn$ | 无放回抽样中的次品数 |
| $\mathrm{Poi}(\lambda)$ | $\lambda^k\mathrm{e}^{-\lambda}/k!$，$k=0,1,\dots$ | 稀有事件的发生次数 |
| $\mathrm{U}(a,b)$ | $\frac1{b-a}\boldsymbol{1}_{(a,b)}(x)$ | 几何概型 |
| $\mathrm{Exp}(\lambda)$ | $\lambda\mathrm{e}^{-\lambda x}\boldsymbol{1}_{[0,\infty)}(x)$ | 无老化的寿命；无记忆性 |
| $\mathcal{N}(\mu,\sigma^2)$ | $\frac1{\sigma\sqrt{2\pi}}\mathrm{e}^{-(x-\mu)^2/(2\sigma^2)}$ | 大量微小独立因素的累积 |

离散型的重点是两点、二项、几何与 Poisson 分布，连续型的重点是均匀、指数与正态分布。学习时应利用实际情景建立不同分布之间的关系，再利用这些关系理解每个分布的含义。
