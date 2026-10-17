---
title: 独立性、随机变量
description: 两个事件的独立性与条件独立性，一组事件的相互独立与两两独立，Borel–Cantelli 引理的第二部分，赌徒破产模型；随机变量的定义、Borel 集与可测函数；随机变量的相互独立性、独立同分布序列及其函数的独立性。
---

上一章 [3.1.2](/3.1.2) 的条件概率刻画了一个事件的信息对另一个事件的影响。本章先讨论"没有影响"的情形，即事件的独立性：它看似简单，却有几处容易混淆的细节——独立与不相容、独立与条件独立、相互独立与两两独立。独立性使许多计算化简为乘法，赌徒破产模型则展示了全概率公式与递推的配合。本章后半引入随机变量：把试验结果数值化，使我们可以用函数、运算和分布来描述随机现象，并把独立性推广到随机变量。下一章 [3.1.4](/3.1.4) 介绍常见的离散型与连续型随机变量，[3.1.5](/3.1.5) 用分布函数统一地刻画随机变量。

## 3.1. 事件的独立性

### 3.1.1. 两个事件的独立性

**例 3.1.1** 一枚有偏的硬币，正面朝上的概率为 $p$，连续抛掷 3 次。用序贯树形图建模时，每一次抛掷的分枝概率都是 $p$ 与 $1-p$，与之前的结果无关。记 $H_i$、$T_i$ 为第 $i$ 次得到正面、反面，则 $\mathbb{P}(H_2\mid H_1)=\mathbb{P}(H_2\mid T_1)=p$，由全概率公式 $\mathbb{P}(H_2)=\mathbb{P}(H_2\mid H_1)\mathbb{P}(H_1)+\mathbb{P}(H_2\mid T_1)\mathbb{P}(T_1)=p$。即第一次的结果不改变第二次得到正面的概率。

直观地，若事件 $B$ 的发生没有给事件 $A$ 带来新的信息，即 $\mathbb{P}(A\mid B)=\mathbb{P}(A)$，就称 $A$ 与 $B$ 独立。把它改写成乘积的形式，就得到对称且不要求 $\mathbb{P}(B)>0$ 的定义。

**定义 3.1.1（独立性）** 设 $(\Omega,\mathcal{F},\mathbb{P})$ 是概率空间，$A,B\in\mathcal{F}$。若

$$
\mathbb{P}(A\cap B)=\mathbb{P}(A)\mathbb{P}(B),
$$
则称 $A$ 与 $B$ **相互独立**，简称**独立**。

这一定义关于 $A$、$B$ 对称，对 $\mathbb{P}(B)=0$ 也适用；当 $\mathbb{P}(B)>0$ 时它等价于 $\mathbb{P}(A\mid B)=\mathbb{P}(A)$。由定义，不可能事件 $\varnothing$ 与必然事件 $\Omega$ 与任何事件独立；更一般地，概率为 0 或 1 的事件与任何事件独立。

**性质 3.1.1** 若 $A$ 与 $B$ 独立，则 $A$ 与 $B^{\mathsf c}$、$A^{\mathsf c}$ 与 $B$、$A^{\mathsf c}$ 与 $B^{\mathsf c}$ 也都独立。

**证明** $A=(A\cap B)\cup(A\cap B^{\mathsf c})$ 是不相容的并，所以

$$
\mathbb{P}(A\cap B^{\mathsf c})=\mathbb{P}(A)-\mathbb{P}(A\cap B)=\mathbb{P}(A)-\mathbb{P}(A)\mathbb{P}(B)=\mathbb{P}(A)\mathbb{P}(B^{\mathsf c}).
$$
对 $(A,B^{\mathsf c})$、$(B^{\mathsf c},A)$ 再用这一结论即得其余两个。 $\square$

**注 3.1.1** 独立与互不相容是完全不同的概念。若 $A\cap B=\varnothing$ 且 $\mathbb{P}(A)>0$、$\mathbb{P}(B)>0$，则 $\mathbb{P}(A\cap B)=0\ne\mathbb{P}(A)\mathbb{P}(B)$，$A$ 与 $B$ 一定不独立：知道 $A$ 发生，就知道 $B$ 不发生。

什么情况下会出现独立的事件？同一个试验中可以有独立的事件（例如掷一枚均匀骰子，"点数为偶数"与"点数不超过 2"独立）；互不相干的不同试验更会产生独立的事件。

**例 3.1.2** 设 $\Omega_1=\{\mu_1,\dots,\mu_n\}$、$\Omega_2=\{\eta_1,\dots,\eta_m\}$ 分别是互不相干的试验 $S_1$、$S_2$ 的样本空间，各自的样本点等可能。把两个试验合起来看作一个试验，样本空间为 $\Omega=\Omega_1\times\Omega_2$，$nm$ 个样本点等可能。对 $A\subset\Omega_1$、$B\subset\Omega_2$，事件"$S_1$ 的结果在 $A$ 中"与"$S_2$ 的结果在 $B$ 中"分别是 $A\times\Omega_2$ 与 $\Omega_1\times B$，于是

$$
\mathbb{P}\big((A\times\Omega_2)\cap(\Omega_1\times B)\big)=\frac{\#A\cdot\#B}{nm}=\frac{\#A}n\cdot\frac{\#B}m=\mathbb{P}(A\times\Omega_2)\,\mathbb{P}(\Omega_1\times B),
$$
即两者独立。

### 3.1.2. 条件独立性

**定义 3.1.2（条件独立性）** 设 $(\Omega,\mathcal{F},\mathbb{P})$ 是概率空间，$A,B,C\in\mathcal{F}$，$\mathbb{P}(C)>0$。若

$$
\mathbb{P}(A\cap B\mid C)=\mathbb{P}(A\mid C)\mathbb{P}(B\mid C),
$$
则称 $A$ 与 $B$ 在给定 $C$ 之下**条件独立**。

条件独立就是在概率测度 $\mathbb{P}_C=\mathbb{P}(\cdot\mid C)$ 下的独立。独立性与条件独立性互不蕴含，下面两个例子分别说明。

**例 3.1.3（独立但不条件独立）** 抛掷两次均匀硬币，四个结果等可能。令 $H_1$ 为"第一次正面朝上"，$H_2$ 为"第二次正面朝上"，$D$ 为"两次结果不同"。$H_1$ 与 $H_2$ 独立，但

$$
\mathbb{P}(H_1\mid D)=\mathbb{P}(H_2\mid D)=\frac12,\qquad\mathbb{P}(H_1\cap H_2\mid D)=0,
$$
所以 $\mathbb{P}(H_1\cap H_2\mid D)\ne\mathbb{P}(H_1\mid D)\mathbb{P}(H_2\mid D)$，$H_1$ 与 $H_2$ 在给定 $D$ 之下不条件独立。

**例 3.1.4（条件独立但不独立）** 有两枚不均匀的硬币 $A$ 与 $B$，抛掷时正面朝上的概率分别为 $0.9$ 与 $0.1$。等可能地选择其中一枚，然后用它连续抛掷两次。若已知选的是硬币 $A$，两次抛掷是独立的：$\mathbb{P}(H_1\cap H_2\mid A)=0.81=\mathbb{P}(H_1\mid A)\mathbb{P}(H_2\mid A)$。若不知道是哪枚硬币，由全概率公式

$$
\mathbb{P}(H_1)=\mathbb{P}(H_2)=\frac12(0.9+0.1)=\frac12,\qquad\mathbb{P}(H_1\cap H_2)=\frac12(0.81+0.01)=0.41\ne\frac14,
$$
两次抛掷不独立：$\mathbb{P}(H_2\mid H_1)=0.82$，第一次得到正面使我们更相信选中的是硬币 $A$。

### 3.1.3. 一组事件的独立性

"一组事件相互独立"的直观含义是：其中任意一些事件的信息都不改变其余事件发生的概率，例如 $\mathbb{P}\big(A_1\cap(A_2^{\mathsf c}\cup A_3)\mid A_5\cap A_6^{\mathsf c}\big)=\mathbb{P}\big(A_1\cap(A_2^{\mathsf c}\cup A_3)\big)$。

**定义 3.1.3（相互独立）** 设 $(\Omega,\mathcal{F},\mathbb{P})$ 是概率空间，$A_1,\dots,A_n\in\mathcal{F}$。若对 $\{1,\dots,n\}$ 的任意非空子集 $S$，都有

$$
\mathbb{P}\Big(\bigcap_{i\in S}A_i\Big)=\prod_{i\in S}\mathbb{P}(A_i),
$$
则称 $A_1,\dots,A_n$ **相互独立**。若事件列 $A_1,A_2,\dots$ 中任意有限个事件都相互独立，称这个事件列相互独立。

定义要求 $2^n-n-1$ 个等式同时成立。

**定义 3.1.4（两两独立）** 设 $A_1,\dots,A_n\in\mathcal{F}$。若对任意 $i\ne j$，$\mathbb{P}(A_i\cap A_j)=\mathbb{P}(A_i)\mathbb{P}(A_j)$，则称 $A_1,\dots,A_n$ **两两独立**。

相互独立蕴含两两独立，反之不然。

**例 3.1.5（Bernstein 四面体）** 把一个均匀正四面体的第一面染上红、黄、蓝三色，其余三面分别染上红色、黄色、蓝色。设 $A$、$B$、$C$ 分别表示掷一次四面体时有红色、黄色、蓝色的面与桌面接触。则

$$
\mathbb{P}(A)=\mathbb{P}(B)=\mathbb{P}(C)=\frac12,\qquad\mathbb{P}(A\cap B)=\mathbb{P}(B\cap C)=\mathbb{P}(A\cap C)=\frac14,
$$
所以 $A,B,C$ 两两独立；但 $\mathbb{P}(A\cap B\cap C)=\frac14\ne\frac18=\mathbb{P}(A)\mathbb{P}(B)\mathbb{P}(C)$，它们不相互独立。

反过来，只要求"全体事件之交"的乘积公式也不够。例如掷两枚均匀骰子，$A=\{$第一枚为 1、2 或 3$\}$，$B=\{$第一枚为 3、4 或 5$\}$，$C=\{$两枚点数之和为 9$\}$，则 $\mathbb{P}(A\cap B\cap C)=\frac1{36}=\frac12\cdot\frac12\cdot\frac19$，但 $\mathbb{P}(A\cap B)=\frac16\ne\frac14$。所以定义 3.1.3 必须对任意非空子集 $S$ 要求乘积公式。

**定理 3.1.1** 若 $A_1,\dots,A_n$ 相互独立，则把其中任意多个事件换成各自的对立事件后，所得的 $n$ 个事件仍相互独立。

**证明** 只需证明把 $A_1$ 换成 $A_1^{\mathsf c}$ 的情形，其余由反复使用得到。对不含 1 的子集 $S$，乘积公式不变；对含 1 的子集 $S=\{1\}\cup S'$，记 $B=\bigcap_{i\in S'}A_i$，则

$$
\mathbb{P}(A_1^{\mathsf c}\cap B)=\mathbb{P}(B)-\mathbb{P}(A_1\cap B)=\prod_{i\in S'}\mathbb{P}(A_i)-\mathbb{P}(A_1)\prod_{i\in S'}\mathbb{P}(A_i)=\mathbb{P}(A_1^{\mathsf c})\prod_{i\in S'}\mathbb{P}(A_i).\qquad\square
$$

### 3.1.4. 事件独立性的应用

独立性最常见的用法是计算"至少一个发生"的概率：由 De Morgan 律取补，化为交的概率，再用乘积公式。

**例 3.1.6** 设某地区某时期每人携带违禁品的概率为 $0.04\%$，用一张新的检测纸连续检测 20 人，求检测纸检出违禁品的概率。设 $A_i$ 为"第 $i$ 个人携带违禁品"，可以认为 $A_1,\dots,A_{20}$ 相互独立。由定理 3.1.1，$A_1^{\mathsf c},\dots,A_{20}^{\mathsf c}$ 也相互独立，所以

$$
\mathbb{P}\Big(\bigcup_{i=1}^{20}A_i\Big)=1-\mathbb{P}\Big(\bigcap_{i=1}^{20}A_i^{\mathsf c}\Big)=1-\prod_{i=1}^{20}\mathbb{P}(A_i^{\mathsf c})=1-(1-0.0004)^{20}\approx0.008.
$$
若连续检测 1000 人，这一概率为 $1-0.9996^{1000}\approx33\%$：小概率事件在大量独立重复中几乎必然会出现。

同样的论证给出 [3.1.2](/3.1.2) 中 Borel–Cantelli 引理的第二部分。

**定理 3.1.2（Borel–Cantelli 引理第二部分）** 若事件列 $\{A_n\}$ 相互独立，且 $\sum_{n=1}^\infty\mathbb{P}(A_n)=\infty$，则 $\mathbb{P}(\limsup_{n\to\infty}A_n)=1$。

**证明** 由 De Morgan 律，$(\limsup_nA_n)^{\mathsf c}=\bigcup_{n=1}^\infty\bigcap_{k=n}^\infty A_k^{\mathsf c}$，由可列次可加性只需证明对每个 $n$，$\mathbb{P}(\bigcap_{k=n}^\infty A_k^{\mathsf c})=0$。对 $m>n$，由独立性（定理 3.1.1）和不等式 $1-x\le\mathrm{e}^{-x}$，

$$
\mathbb{P}\Big(\bigcap_{k=n}^\infty A_k^{\mathsf c}\Big)\le\mathbb{P}\Big(\bigcap_{k=n}^mA_k^{\mathsf c}\Big)=\prod_{k=n}^m\big(1-\mathbb{P}(A_k)\big)\le\exp\Big\{-\sum_{k=n}^m\mathbb{P}(A_k)\Big\}.
$$
令 $m\to\infty$，右端趋于 0。 $\square$

**例 3.1.7（赌徒破产模型）** 甲有本金 $a$ 元，决心再赢 $b$ 元就停止赌博。设甲每局赢的概率是 $p=1/2$，各局输赢相互独立，每局输赢都是 1 元，甲输光后也停止赌博。求甲输光的概率 $q(a)$。

记 $N=a+b$，$B_k$ 为"甲有本金 $k$ 元时最终输光"，$q(k)=\mathbb{P}(B_k)$，$k=0,1,\dots,N$。边界条件为 $q(0)=1$，$q(N)=0$。用 $A$ 表示甲在下一局赢。由于各局独立，赢了一局之后的局面与"从本金 $k+1$ 元开始"的局面完全相同，所以 $\mathbb{P}(B_k\mid A)=q(k+1)$，同理 $\mathbb{P}(B_k\mid A^{\mathsf c})=q(k-1)$。由全概率公式得递推公式

$$
q(k)=\mathbb{P}(A)\mathbb{P}(B_k\mid A)+\mathbb{P}(A^{\mathsf c})\mathbb{P}(B_k\mid A^{\mathsf c})=\frac12\big[q(k+1)+q(k-1)\big],\qquad1\le k\le N-1.
$$
于是 $q(k+1)-q(k)=q(k)-q(k-1)=\cdots=q(1)-q(0)$，从而 $q(n)-1=n[q(1)-1]$。取 $n=N$，由 $q(N)=0$ 得 $q(1)-1=-1/N$，所以

$$
q(a)=1-\frac aN=\frac b{a+b}.
$$
当甲的本金 $a$ 有限时，贪心 $b$ 越大，输光的概率越大；如果一直赌下去（$b\to\infty$），甲以概率 1 输光。

一般地，若每局赢的概率为 $p\ne1/2$，记 $r=(1-p)/p$，同样的递推 $q(k)=pq(k+1)+(1-p)q(k-1)$ 给出 $q(k+1)-q(k)=r[q(k)-q(k-1)]$，解得

$$
q(a)=\frac{r^a-r^N}{1-r^N}.
$$
$p<1/2$ 时 $r>1$，即使 $b\to\infty$ 也有 $q(a)\to1$；$p>1/2$ 时 $r<1$，$q(a)\to r^a<1$。

![赌徒破产模型：左图为总资本 N = 20 时输光概率 q(k) 随初始本金 k 的变化（p = 0.45, 0.5, 0.55）；右图为从 a = 10 开始的 8 局公平赌博的资本轨迹，在到达 0 或 20 时停止](./plots/gamblers-ruin.py)

## 3.2. 随机变量

### 3.2.1. 为什么引进随机变量

在赌徒破产模型中，如果关心甲在第 $k$ 局之后恰有 $j$ 元，可以用事件 $A_{jk}$ 表示；对很多个时间点就需要很多个记号，若再关心"赌了多少局输光"，用事件表示就更加复杂。而如果用 $X_k$ 表示"甲在第 $k$ 局之后的本金"，用 $R=\min\{n\colon X_n=0\text{ 或 }X_n=a+b\}$ 表示赌博持续的局数，就简洁得多。

**例 3.2.1** 人的血压总在不断变化之中，设甲的收缩压的变化范围是 90–180 mmHg。用 $X$ 表示甲的收缩压的测量结果，$X=125$ 表示测得的收缩压为 125 mmHg。这里试验的样本空间是 $\Omega=[90,180]$，$X$ 是 $\Omega$ 上的函数 $X(\omega)=\omega$。

**例 3.2.2** 从一副 52 张的扑克牌中任取 1 张，样本空间的每个点表示 1 张牌。用 $X$ 表示所取牌的点数，$X$ 是样本空间到 $\mathbb{N}$ 的函数，例如

$$
\{X=3\}\overset{\text{def}}{=}\{\omega\colon X(\omega)=3\}=\{\clubsuit3,\diamondsuit3,\heartsuit3,\spadesuit3\}.
$$
对任意 $x\in\mathbb{R}$，$\{X\le x\}$ 都是事件；由于 $X$ 的取值是数，可以对它进行数学运算。

**例 3.2.3** 将一枚均匀硬币连续抛掷两次，$X$ 表示得到正面的次数：$\Omega=\{HH,HT,TH,TT\}$，$X$ 的取值范围是 $\{0,1,2\}$。一个家庭计划要两个孩子，各孩子的性别相互独立且男女等可能，$X$ 表示女孩的个数：$\Omega=\{BB,BG,GB,GG\}$，$X$ 的取值范围也是 $\{0,1,2\}$。两个试验不同，概率模型却完全相同。

这些例子说明引进随机变量的三点好处：

- 简化性：事件只描述某个现象是否出现，要说明较复杂的试验结果需要定义许多事件；随机变量把注意力集中在关心的数量上。
- 数值化：许多试验的结果本身就是数值（仪表读数、股票价格、气温），另一些结果虽非数值，却与某些数值紧密相连。
- 通用性：我们不仅关心出现什么结果，更关心这些结果以什么概率出现；不同的场景可以共用同一个模型（例 3.2.3），就像许多房子可以共用一张蓝图。

### 3.2.2. 定义

随机变量就是给每个可能的试验结果分配一个数，即从样本空间 $\Omega$ 到实数轴 $\mathbb{R}$ 的函数，取值可以是离散的，也可以是连续的。它和概率一样是映射，但定义域不同：概率是从事件域 $\mathcal{F}$ 到 $[0,1]$ 的函数，随机变量是从 $\Omega$ 到 $\mathbb{R}$ 的函数。随机性来自试验结果 $\omega$ 的随机性，而函数 $X$ 本身是确定的。对同一个样本空间可以定义许多不同的随机变量，每一个都是试验某一方面在数值上的总结。为了能计算 $\mathbb{P}(X\le x)$，还要求 $\{X\le x\}$ 是事件。

**定义 3.2.1（随机变量）** 设 $(\Omega,\mathcal{F})$ 是可测空间。若 $\Omega$ 上的实值函数 $X(\omega)$ 满足：对任意 $x\in\mathbb{R}$，

$$
\{\omega\colon X(\omega)\le x\}\in\mathcal{F},
$$
则称 $X$ 为 $(\Omega,\mathcal{F})$ 上的**随机变量**（random variable，简记 r.v.）。

习惯上用大写字母 $X,Y,Z,\dots$（或希腊字母 $\xi,\eta,\zeta$）表示随机变量，不够用时加下标 $X_1,X_2,\dots$；用 $\{X\le x\}$ 表示事件 $\{\omega\colon X(\omega)\le x\}$，并且只在必要时才写出自变量 $\omega$。由事件域对可列次运算的封闭性，

$$
\{X>x\}=\{X\le x\}^{\mathsf c},\quad\{X<x\}=\bigcup_{n=1}^\infty\Big\{X\le x-\frac1n\Big\},\quad\{X\ge x\}=\{X<x\}^{\mathsf c},\quad\{X=x\}=\{X\le x\}\setminus\{X<x\}
$$
也都是事件。反过来，定义中的条件"$\{X\le x\}\in\mathcal{F}$"可以换成 $\{X>x\}\in\mathcal{F}$、$\{X<x\}\in\mathcal{F}$ 或 $\{X\ge x\}\in\mathcal{F}$ 中的任何一个，得到的定义是等价的。若 $\Omega$ 可列且 $\mathcal{F}=\mathcal{P}(\Omega)$，$\Omega$ 上的任意实值函数都是随机变量。

**例 3.2.4** 从 52 张扑克牌中任取 13 张，求恰好有 5 张梅花的概率。用 $X$ 表示这 13 张牌中梅花的张数，关心的事件是 $\{X=5\}$。样本空间 $\Omega$ 由 $\binom{52}{13}$ 个等可能的样本点组成，每个样本点 $\omega$ 是不计次序的 13 张牌，$X(\omega)$ 是 $\omega$ 中的梅花数，$\{X=5\}=\{\omega\colon\omega\text{ 中有 5 张梅花}\}$。于是

$$
\mathbb{P}(X=5)=\binom{13}5\binom{39}8\Big/\binom{52}{13}.
$$
写出函数 $X(\omega)$ 对计算并没有多少帮助，所以通常不关心 $X$ 在 $\Omega$ 上如何具体定义，而关心它取各个值的概率。此后，相对于原来的概率空间 $(\Omega,\mathcal{F},\mathbb{P})$，我们更多地关注经过 $X$ 映射到实数轴上的概率空间。这需要确定实数轴上哪些集合 $A$ 能使 $\{X\in A\}$ 成为事件。

**定义 3.2.2（Borel 集）** 记 $\mathcal{C}$ 为 $\mathbb{R}$ 中全体左开右闭区间 $(a,b]$ 构成的集族，称由它生成的 σ-代数 $\mathcal{B}=\sigma(\mathcal{C})$ 为 $\mathbb{R}$ 上的 Borel σ-代数（Borel 域），称 $\mathcal{B}$ 中的元素为 **Borel 集**。

一切开区间、闭区间、单点集、可列集以及它们的可列并、交、补都是 Borel 集；实际中遇到的实数集合都是 Borel 集。

**定理 3.2.1** 设 $X$ 是可测空间 $(\Omega,\mathcal{F})$ 上的随机变量，则对任意 Borel 集 $A$，

$$
\{X\in A\}\overset{\text{def}}{=}\{\omega\colon X(\omega)\in A\}\in\mathcal{F}.
$$

**证明** 对 $A\subset\mathbb{R}$，记原像 $X^{-1}(A)=\{\omega\colon X(\omega)\in A\}$，令 $\mathcal{A}=\{A\subset\mathbb{R}\colon X^{-1}(A)\in\mathcal{F}\}$。原像运算保持集合运算：

$$
X^{-1}\Big(\bigcup_iA_i\Big)=\bigcup_iX^{-1}(A_i),\qquad X^{-1}\Big(\bigcap_iA_i\Big)=\bigcap_iX^{-1}(A_i),\qquad X^{-1}(A^{\mathsf c})=\big[X^{-1}(A)\big]^{\mathsf c}.
$$
先证 $\mathcal{A}$ 是 σ-代数：(a) $X^{-1}(\mathbb{R})=\Omega\in\mathcal{F}$，故 $\mathbb{R}\in\mathcal{A}$；(b) 若 $A\in\mathcal{A}$，则 $X^{-1}(A^{\mathsf c})=[X^{-1}(A)]^{\mathsf c}\in\mathcal{F}$，故 $A^{\mathsf c}\in\mathcal{A}$；(c) 若 $A_i\in\mathcal{A}$，则 $X^{-1}(\bigcup_iA_i)=\bigcup_iX^{-1}(A_i)\in\mathcal{F}$，故 $\bigcup_iA_i\in\mathcal{A}$。再证 $\mathcal{C}\subset\mathcal{A}$：$X^{-1}((a,b])=\{X\le b\}\setminus\{X\le a\}\in\mathcal{F}$。由于 $\mathcal{B}$ 是包含 $\mathcal{C}$ 的最小 σ-代数，$\mathcal{B}\subset\mathcal{A}$。 $\square$

于是对任意 Borel 集 $A$，$\mathbb{P}(X\in A)$ 都有定义；$P_X(A)=\mathbb{P}(X\in A)$ 是 $(\mathbb{R},\mathcal{B})$ 上的概率测度，称为 $X$ 的分布。$(\mathbb{R},\mathcal{B},P_X)$ 就是经过 $X$ 映射之后的概率空间：概率像沙子一样，从 $\Omega$ 转移到了实数轴上。

### 3.2.3. 随机变量的函数

**定义 3.2.3（可测函数）** 若实函数 $g\colon\mathbb{R}\to\mathbb{R}$ 满足：对任意 $a\in\mathbb{R}$，$\{x\colon g(x)\le a\}$ 是 Borel 集，则称 $g$ 为 Borel 可测函数，简称**可测函数**。类似地定义 $n$ 元可测函数 $g\colon\mathbb{R}^n\to\mathbb{R}$（用 $\mathbb{R}^n$ 上由矩形 $(a_1,b_1]\times\cdots\times(a_n,b_n]$ 生成的 $n$ 维 Borel σ-代数代替 $\mathcal{B}$）。

连续函数、阶梯函数、单调函数以及这些函数的线性组合都是可测函数。

**定理 3.2.2** 若 $X$ 是可测空间 $(\Omega,\mathcal{F})$ 上的随机变量，$g$ 是可测函数，则 $Y=g(X)$ 是 $(\Omega,\mathcal{F})$ 上的随机变量。

**证明** 对任意 $a\in\mathbb{R}$，令 $B=\{x\colon g(x)\le a\}$，则 $B\in\mathcal{B}$。由定理 3.2.1，

$$
\{Y\le a\}=\{\omega\colon g(X(\omega))\le a\}=\{\omega\colon X(\omega)\in B\}=\{X\in B\}\in\mathcal{F}.\qquad\square
$$

完全类似地可以证明：若 $X_1,\dots,X_n$ 都是 $(\Omega,\mathcal{F})$ 上的随机变量，$g$ 是 $n$ 元可测函数，则 $g(X_1,\dots,X_n)$ 也是随机变量。如无特殊说明，本课程以后用到的一元和多元实函数都是可测函数。由此得到构造随机变量的常用方式：

1. 四则运算：$aX+bY$、$XY$、$X/Y$（$Y\ne0$ 时），$a,b\in\mathbb{R}$；
2. 极限：$\sup_nX_n$、$\inf_nX_n$、$\limsup_nX_n$、$\liminf_nX_n$、$\lim_nX_n$（若存在）；
3. 变换：$\max\{X,Y\}$、$\min\{X,Y\}$、$\sin X$、$\mathrm{e}^X$、$X^+=\max\{X,0\}$、$X^-=\max\{-X,0\}$、$\lvert X\rvert^p$ 等；
4. 函数的复合。

例如事件 $A\in\mathcal{F}$ 的指示函数（示性函数）$\boldsymbol{1}_A(\omega)$（$\omega\in A$ 时为 1，否则为 0）是随机变量，因为 $\{\boldsymbol{1}_A\le x\}$ 只可能是 $\varnothing$、$A^{\mathsf c}$ 或 $\Omega$。

## 3.3. 随机变量的独立性

### 3.3.1. 定义

类比事件的独立性，两个随机变量独立应当意味着：关于一个随机变量取值的任何信息都不改变另一个随机变量取各个值的概率。由于随机变量由事件 $\{X\le x\}$ 刻画，可以这样定义：

**定义 3.3.1（随机变量的独立性）** 设 $X_1,\dots,X_n$ 是 $(\Omega,\mathcal{F},\mathbb{P})$ 上的随机变量。若对任意实数 $x_1,\dots,x_n$，

$$
\mathbb{P}(X_1\le x_1,\dots,X_n\le x_n)=\mathbb{P}(X_1\le x_1)\cdots\mathbb{P}(X_n\le x_n),
$$
则称随机变量 $X_1,\dots,X_n$ 相互独立。

这里 $\mathbb{P}(X_1\le x_1,\dots,X_n\le x_n)$ 是 $\mathbb{P}(\{X_1\le x_1\}\cap\cdots\cap\{X_n\le x_n\})$ 的简写。与事件的情形不同，这里只要求 $n$ 个随机变量全体的乘积公式，而不必对每个子集分别要求：子集的乘积公式可以由全体的乘积公式推出，因为令某个 $x_i\to+\infty$，事件 $\{X_i\le x_i\}$ 就单调递增地趋于 $\Omega$。以 $n=3$ 为例，由概率的连续性（[3.1.2](/3.1.2) 定理 2.2.1），

$$
\begin{aligned}
\mathbb{P}(X_1\le x_1,X_2\le x_2)&=\mathbb{P}\Big(\bigcup_{m=1}^\infty\{X_1\le x_1,X_2\le x_2,X_3\le m\}\Big)=\lim_{m\to\infty}\mathbb{P}(X_1\le x_1,X_2\le x_2,X_3\le m)\\
&=\mathbb{P}(X_1\le x_1)\mathbb{P}(X_2\le x_2)\lim_{m\to\infty}\mathbb{P}(X_3\le m)=\mathbb{P}(X_1\le x_1)\mathbb{P}(X_2\le x_2).
\end{aligned}
$$
事件的乘积公式中没有可以趋于 $\Omega$ 的参数，这就是两者的差别。

**定理 3.3.1** 设 $X_1,\dots,X_n$ 相互独立，则对任意 Borel 集 $A_1,\dots,A_n$，事件 $\{X_1\in A_1\},\dots,\{X_n\in A_n\}$ 相互独立。

这个定理的证明需要测度论中的单调类方法，这里从略。它说明随机变量的独立性确实蕴含了"关于各个随机变量的一切事件都独立"。例如若 $X,Y$ 独立，则 $\mathbb{P}(a<X\le b,\ Y>c)=\mathbb{P}(a<X\le b)\mathbb{P}(Y>c)$。

**例 3.3.1** 设 $X_1,X_2$ 相互独立，都在 $\{1,\dots,6\}$ 上等可能地取值（两枚均匀骰子的点数）。由定理 3.3.1，$\mathbb{P}(X_1\text{ 为偶数},\ X_2\ge5)=\frac12\cdot\frac13=\frac16$。而 $X_1$ 与 $S=X_1+X_2$ 不独立：$\mathbb{P}(X_1=1,S=12)=0\ne\mathbb{P}(X_1=1)\mathbb{P}(S=12)=\frac16\cdot\frac1{36}$。

### 3.3.2. 独立序列与独立同分布

**定义 3.3.2（独立序列）** 若对任意 $n$，随机变量 $X_1,\dots,X_n$ 相互独立，则称随机变量序列 $\{X_n\}$ 相互独立，也称 $\{X_n\}$ 为独立序列。

**定义 3.3.3（独立同分布）** 若随机变量 $X_1,X_2,\dots$ 相互独立，并且有相同的分布（即相同的**分布函数** $F(x)=\mathbb{P}(X_i\le x)$，见 [3.1.5](/3.1.5)），则称 $X_1,X_2,\dots$ **独立同分布**（independent and identically distributed，简记 i.i.d.），记作 $X_1,X_2,\dots\overset{\text{iid}}{\sim}F$。

独立同分布序列是重复试验的数学模型，也是统计学中简单随机样本的模型（[3.2.1](/3.2.1)），大数定律与中心极限定理（[3.1.12](/3.1.12)、[3.1.13](/3.1.13)）都讨论它。

**定理 3.3.2** 设随机变量 $X_1,\dots,X_n$ 相互独立，$g_1,\dots,g_n$ 是一元可测函数，$\varphi$ 是 $k$ 元可测函数（$k<n$），则

1. 随机变量 $g_1(X_1),\dots,g_n(X_n)$ 相互独立；
2. 随机变量 $\varphi(X_1,\dots,X_k),X_{k+1},\dots,X_n$ 相互独立。

**证明** (1) 对任意实数 $y_1,\dots,y_n$，令 $B_i=\{x\colon g_i(x)\le y_i\}$，它们是 Borel 集。由定理 3.3.1，

$$
\mathbb{P}\big(g_1(X_1)\le y_1,\dots,g_n(X_n)\le y_n\big)=\mathbb{P}(X_1\in B_1,\dots,X_n\in B_n)=\prod_{i=1}^n\mathbb{P}(X_i\in B_i)=\prod_{i=1}^n\mathbb{P}\big(g_i(X_i)\le y_i\big).
$$
(2) 的证明需要定理 3.3.1 的多元推广（随机向量 $(X_1,\dots,X_k)$ 与 $X_{k+1},\dots,X_n$ 独立），这里从略。 $\square$

定理 3.3.2 可以推广为：独立的随机变量分成互不相交的组之后，各组的函数仍相互独立。例如若 $(X_1,X_2)$ 与 $(X_3,X_4)$ 独立，则 $X_2/X_1^2$ 与 $(X_3+X_4)/2$ 独立。

## 小结

| 内容 | 要点 |
|---|---|
| 事件的独立性 | $\mathbb{P}(A\cap B)=\mathbb{P}(A)\mathbb{P}(B)$；与不相容不同；对取补封闭 |
| 条件独立 | 在 $\mathbb{P}(\cdot\mid C)$ 下独立；与独立性互不蕴含 |
| 一组事件 | 相互独立要求所有子集的乘积公式；两两独立不蕴含相互独立 |
| 随机变量 | $\Omega\to\mathbb{R}$ 的函数，$\{X\le x\}$ 是事件；$\{X\in A\}$ 对 Borel 集 $A$ 是事件；可测函数的复合仍是随机变量 |
| 随机变量的独立性 | $\mathbb{P}(X_1\le x_1,\dots,X_n\le x_n)=\prod\mathbb{P}(X_i\le x_i)$；独立随机变量的函数仍独立；i.i.d. 序列 |

对独立性、随机变量与随机变量的独立性，若尚不知道结论是否成立，要回到定义验证；已知成立时，可以直接使用性质进行推理。辨析概念的细微差别时常用反例（不同的独立性定义），掌握新概念时常用类比（从事件的独立性到随机变量的独立性），步数不确定的随机试验常用递推与归纳（赌徒破产模型）。
