---
title: 概率空间、条件概率
description: 事件域（σ-代数）、概率测度与概率空间；单调事件列与概率的连续性，事件列的上下极限与 Borel–Cantelli 引理；条件概率及以它为基础的乘法公式、全概率公式与 Bayes 公式。
---

上一章 [3.1.1](/3.1.1) 用"样本空间 + 满足公理的概率"描述随机试验，但留下一个问题：样本空间的任意子集都能分配概率吗？本章先回答它：把事件限制在一个对可列次集合运算封闭的子集族（事件域）中，概率就是定义在事件域上的测度，三者合起来构成概率空间，这是 Kolmogorov 公理体系的核心。可列可加性的第一个推论是概率的连续性，由它可以讨论事件列的极限，得到 Borel–Cantelli 引理。本章后半引入条件概率：获得新信息后如何更新对事件的信念。由条件概率得到的乘法公式、全概率公式和 Bayes 公式是计算概率最常用的三个工具。下一章 [3.1.3](/3.1.3) 用条件概率定义独立性，并引入随机变量。

## 2.1. 概率空间

### 2.1.1. 问题的提出

回顾例 1.2.6 的几何概型：$\Omega=[0,1]^2$，$\mathbb{P}(A)$ 为 $A$ 的面积。每个单点 $\{(x,y)\}$ 的面积为零，而 $\Omega=\bigcup_{(x,y)\in\Omega}\{(x,y)\}$。如果对这个并使用可加性，就得到

$$
1=\mathbb{P}(\Omega)=\sum_{(x,y)\in\Omega}\mathbb{P}(\{(x,y)\})=0,
$$
矛盾。错误在于这是不可列个事件的并，而可加性只对可列个事件成立。这个例子也说明，概率为 1 的事件未必是 $\Omega$：$\mathbb{P}\big((x,y)\ne(0,0)\big)=1$，但 $(0,0)$ 仍可能出现。

更深的问题是：样本空间的任意子集都能分配概率吗？对不可列的样本空间，答案是否定的（例 2.1.5）。因此需要先划定哪些子集算作事件，这就是事件域。

### 2.1.2. 事件域

**定义 2.1.1（σ-代数）** 设 $\Omega$ 是样本空间，$\mathcal{F}$ 是由 $\Omega$ 的某些子集构成的集族。若 $\mathcal{F}$ 满足下面三条，则称 $\mathcal{F}$ 是 $\Omega$ 上的**事件域**，也称 **σ-代数**或 σ-域，称 $\mathcal{F}$ 中的元素为事件，称 $(\Omega,\mathcal{F})$ 为**可测空间**：

1. $\Omega\in\mathcal{F}$；
2. 若 $A\in\mathcal{F}$，则 $A^{\mathsf c}\in\mathcal{F}$；
3. 若 $A_n\in\mathcal{F}$，$n=1,2,\dots$，则 $\bigcup_{n=1}^\infty A_n\in\mathcal{F}$。

**注 2.1.1** (1) $\mathcal{F}$ 中的每个事件都是可以分配概率的，$\mathcal{F}$ 圈定了我们关心的全部事件的范围；$\Omega$ 的子集未必是事件，只有 $\mathcal{F}$ 中的元素才称为事件。(2) 由定义，$\varnothing=\Omega^{\mathsf c}\in\mathcal{F}$；由 De Morgan 律，$\bigcap_nA_n=(\bigcup_nA_n^{\mathsf c})^{\mathsf c}\in\mathcal{F}$；取 $A_{n+1}=A_{n+2}=\cdots=\varnothing$ 可知有限并、有限交也在 $\mathcal{F}$ 中，$A\setminus B=A\cap B^{\mathsf c}\in\mathcal{F}$。所以 $\mathcal{F}$ 对可列次的交、并、补、差运算都封闭，也包括下一节的事件列的极限运算。(3) $\mathcal{F}$ 中任选一个事件，其概率能否算出取决于已知条件；有时某个事件很复杂，只能用容易计算的事件去逼近它，或用不等式给出上下界。

对固定的 $\Omega$，可以构造许多不同的事件域。

**例 2.1.1** (1) $\mathcal{F}=\{\Omega,\varnothing\}$ 是平凡的 σ-代数，也是最小的 σ-代数。(2) $\Omega$ 的全体子集构成的**幂集** $\mathcal{P}(\Omega)$（也记作 $2^\Omega$）是最大的 σ-代数。(3) 对 $A\subset\Omega$，$\{\Omega,\varnothing,A,A^{\mathsf c}\}$ 是包含 $A$ 的最小 σ-代数。

一般地，任意多个 σ-代数的交仍是 σ-代数（逐条验证定义即可）。因此对 $\Omega$ 的任一子集族 $\mathcal{A}$，所有包含 $\mathcal{A}$ 的 σ-代数之交是包含 $\mathcal{A}$ 的最小 σ-代数，称为由 $\mathcal{A}$ 生成的 σ-代数（generated σ-algebra），记作 $\sigma(\mathcal{A})$。例 2.1.1 (3) 即 $\sigma(\{A\})$。

**例 2.1.2** 设 $A,B\subset\Omega$。四个集合 $AB$、$AB^{\mathsf c}$、$A^{\mathsf c}B$、$A^{\mathsf c}B^{\mathsf c}$ 两两不交，并为 $\Omega$；$\sigma(\{A,B\})$ 恰由它们中若干个（含零个）的并组成。当这四个集合都非空时，$\sigma(\{A,B\})$ 有 $2^4=16$ 个元素：

$$
\begin{aligned}
\sigma(\{A,B\})=\{&\Omega,\ \varnothing,\ A,\ A^{\mathsf c},\ B,\ B^{\mathsf c},\ AB,\ AB^{\mathsf c},\ A^{\mathsf c}B,\ A^{\mathsf c}B^{\mathsf c},\\
&A\cup B,\ A^{\mathsf c}\cup B,\ A\cup B^{\mathsf c},\ A^{\mathsf c}\cup B^{\mathsf c},\ AB\cup A^{\mathsf c}B^{\mathsf c},\ AB^{\mathsf c}\cup A^{\mathsf c}B\}.
\end{aligned}
$$
若其中某些集合为空（例如 $B=A^{\mathsf c}$，或 $B\subset A$），元素个数相应减少。

**例 2.1.3** 两个 σ-代数的并不一定是 σ-代数。设 $\Omega=\{a,b,c\}$，$\mathcal{F}=\{\Omega,\varnothing,\{a\},\{b,c\}\}$，$\mathcal{G}=\{\Omega,\varnothing,\{c\},\{a,b\}\}$，则 $\mathcal{F}\cup\mathcal{G}=\{\Omega,\varnothing,\{a\},\{c\},\{a,b\},\{b,c\}\}$，但 $\{a\}\cup\{c\}=\{a,c\}\notin\mathcal{F}\cup\mathcal{G}$。（若 $\mathcal{F}\subset\mathcal{G}$，则 $\mathcal{F}\cup\mathcal{G}=\mathcal{G}$ 当然是 σ-代数。）验证一个集族是 σ-代数通常用定义；否定它通常找一个不封闭的运算。

### 2.1.3. 概率测度与概率空间

**定义 2.1.2（概率测度）** 设 $(\Omega,\mathcal{F})$ 是可测空间，$\mathbb{P}$ 是定义在 $\mathcal{F}$ 上的函数。若 $\mathbb{P}$ 满足下面三条，则称 $\mathbb{P}$ 为 $\mathcal{F}$ 上的**概率测度**，简称概率，称 $(\Omega,\mathcal{F},\mathbb{P})$ 为**概率空间**：

1. （非负性）对任意 $A\in\mathcal{F}$，$\mathbb{P}(A)\ge0$；
2. （规范性）$\mathbb{P}(\Omega)=1$；
3. （可列可加性）对 $\mathcal{F}$ 中两两互不相容的事件 $A_1,A_2,\dots$，
$$
\mathbb{P}\Big(\bigcup_{n=1}^\infty A_n\Big)=\sum_{n=1}^\infty\mathbb{P}(A_n).
$$

请注意区分事件域 $\mathcal{F}$、可测空间 $(\Omega,\mathcal{F})$ 与概率空间 $(\Omega,\mathcal{F},\mathbb{P})$：同一个 $\Omega$ 上可以有不同的事件域，同一个可测空间上可以有不同的概率。[3.1.1](/3.1.1) 中由公理推出的所有性质在概率空间上都成立，规范的写法是"若 $A\in\mathcal{F}$，则 $\mathbb{P}(A^{\mathsf c})=1-\mathbb{P}(A)$"。

**例 2.1.4** (1) 掷一枚硬币：$\Omega=\{H,T\}$，$\mathcal{F}=\{\Omega,\varnothing,\{H\},\{T\}\}$，$\mathbb{P}(\{H\})=0.6$，$\mathbb{P}(\{T\})=0.4$。

(2) 掷一枚骰子：$\Omega=\{1,\dots,6\}$，$\mathcal{F}=\mathcal{P}(\Omega)$，$\mathbb{P}(\{i\})=1/6$；对任意 $A\in\mathcal{F}$，$\mathbb{P}(A)=\#A/6$。

(3) 反复掷一枚硬币（每次正面朝上的概率为 $p\in(0,1)$），直到出现正面：$\Omega=\{T^nH\colon n\ge0\}\cup\{T^\infty\}$，其中 $T^nH$ 表示先出现 $n$ 次反面再出现正面，$T^\infty$ 表示永远不出现正面。$\mathbb{P}(\{T^nH\})=(1-p)^np$，由可列可加性 $\sum_{n\ge0}(1-p)^np=1$，所以 $\mathbb{P}(\{T^\infty\})=0$；也可以由下一节的连续性得到 $\mathbb{P}(\{T^\infty\})=\lim_{n\to\infty}(1-p)^n=0$。

若 $\Omega$ 是可列集，给每个样本点分配概率 $p_\omega\ge0$、$\sum_\omega p_\omega=1$，令 $\mathbb{P}(A)=\sum_{\omega\in A}p_\omega$，则 $\Omega$ 的任一子集都可以分配概率，$\mathcal{F}$ 可以取 $\mathcal{P}(\Omega)$。若 $\Omega$ 不可列，则可能存在无法合理分配概率的子集，这些子集就不能当作事件。

**例 2.1.5（不可测集）** 在 $\Omega=[-2,2]$ 上，几何概型 $\mathbb{P}(A)=\operatorname{length}(A)/4$ 不能定义在全部子集上，使之既满足可列可加性又在平移下不变。对 $x,y\in[0,1]$，规定 $x\sim y$ 当且仅当 $x-y\in\mathbb{Q}$，这是等价关系，把 $[0,1]$ 分成互不相交的等价类。由选择公理，存在 $E\subset[0,1]$，它恰含每个等价类中的一个元素。把 $[-1,1]\cap\mathbb{Q}$ 排成 $r_1,r_2,\dots$，令 $E_n=r_n+E$。

1. $m\ne n$ 时 $E_m\cap E_n=\varnothing$：若 $x\in E_m\cap E_n$，则 $x-r_m$、$x-r_n$ 是 $E$ 中两个不同的元素，而它们的差 $r_n-r_m\in\mathbb{Q}$，即它们属于同一等价类，与 $E$ 的构造矛盾。
2. $[0,1]\subset\bigcup_nE_n\subset[-1,2]$：对 $x\in[0,1]$，取 $E$ 中与 $x$ 等价的 $y$，则 $x-y\in[-1,1]\cap\mathbb{Q}$，即 $x-y=r_n$ 对某个 $n$ 成立，$x\in E_n$；后一个包含关系显然。

若 $\mathbb{P}(E)$ 有定义，由平移不变性 $\mathbb{P}(E_n)=\mathbb{P}(E)$，由单调性与可列可加性，

$$
0<\frac14=\mathbb{P}([0,1])\le\sum_{n=1}^\infty\mathbb{P}(E)\le\mathbb{P}([-1,2])=\frac34.
$$
右边的不等式迫使 $\mathbb{P}(E)=0$，左边的不等式又要求 $\mathbb{P}(E)>0$，矛盾。所以 $E$ 不能分配概率。实际使用的几何概型取 $\mathcal{F}$ 为由全体区间生成的 σ-代数，其中的集合称为 Borel 集（Borel set）；或取更大的 Lebesgue 可测集族。

**定义 2.1.3（几乎必然）** 若 $A\in\mathcal{F}$，$\mathbb{P}(A)=1$，称 $A$ 以概率 1 发生，也称**几乎必然**发生或几乎处处发生，记作 a.s.（almost surely）。

## 2.2. 概率的连续性

### 2.2.1. 单调事件列

对事件列 $\{A_n\}$，若 $A_1\subset A_2\subset\cdots$，称它单调递增；若 $A_1\supset A_2\supset\cdots$，称它单调递减；两者统称单调事件列。对单调递增的事件列，定义 $\lim_{n\to\infty}A_n=\bigcup_{n=1}^\infty A_n$；对单调递减的事件列，定义 $\lim_{n\to\infty}A_n=\bigcap_{n=1}^\infty A_n$。这与单调数列的极限类似。

**定理 2.2.1（概率的连续性）** 设 $(\Omega,\mathcal{F},\mathbb{P})$ 是概率空间，$A_n,B_n\in\mathcal{F}$。

1. 若 $\{A_n\}$ 单调递增，则 $\mathbb{P}(\lim_{n\to\infty}A_n)=\lim_{n\to\infty}\mathbb{P}(A_n)$；
2. 若 $\{B_n\}$ 单调递减，则 $\mathbb{P}(\lim_{n\to\infty}B_n)=\lim_{n\to\infty}\mathbb{P}(B_n)$。

**证明** (1) 令 $A_0=\varnothing$。由单调性，$\bigcup_{i=1}^\infty A_i=\bigcup_{i=1}^\infty(A_i\setminus A_{i-1})$，右端各项两两互不相容，且 $\mathbb{P}(A_i\setminus A_{i-1})=\mathbb{P}(A_i)-\mathbb{P}(A_{i-1})$。由可列可加性，

$$
\mathbb{P}\Big(\lim_{n\to\infty}A_n\Big)=\sum_{i=1}^\infty\big[\mathbb{P}(A_i)-\mathbb{P}(A_{i-1})\big]=\lim_{n\to\infty}\sum_{i=1}^n\big[\mathbb{P}(A_i)-\mathbb{P}(A_{i-1})\big]=\lim_{n\to\infty}\mathbb{P}(A_n).
$$

(2) $\{B_n^{\mathsf c}\}$ 单调递增，且由 De Morgan 律 $(\bigcap_nB_n)^{\mathsf c}=\bigcup_nB_n^{\mathsf c}$。由 (1)，

$$
1-\mathbb{P}\Big(\lim_{n\to\infty}B_n\Big)=\mathbb{P}\Big(\lim_{n\to\infty}B_n^{\mathsf c}\Big)=\lim_{n\to\infty}\mathbb{P}(B_n^{\mathsf c})=1-\lim_{n\to\infty}\mathbb{P}(B_n).\qquad\square
$$

反过来，若一个满足非负性、规范性与有限可加性的集函数具有连续性 (1)，它就满足可列可加性：对互不相容的 $A_i$，令 $C_n=\bigcup_{i\le n}A_i$ 即可。因此连续性与可列可加性是等价的要求。

### 2.2.2. 事件列的上极限与下极限

**定义 2.2.1（事件列的上极限与下极限）** 设 $\{A_n\}$ 是事件列。称

$$
\limsup_{n\to\infty}A_n=\bigcap_{n=1}^\infty\bigcup_{k=n}^\infty A_k=\{\omega\in\Omega\colon\omega\text{ 属于无穷多个 }A_k\}
$$
为 $\{A_n\}$ 的**上极限**，称

$$
\liminf_{n\to\infty}A_n=\bigcup_{n=1}^\infty\bigcap_{k=n}^\infty A_k=\{\omega\in\Omega\colon\omega\text{ 属于除有限个以外的所有 }A_k\}
$$
为 $\{A_n\}$ 的**下极限**。若 $\liminf_nA_n=\limsup_nA_n$，称事件列 $\{A_n\}$ 的极限存在，记作 $\lim_{n\to\infty}A_n$。

上极限常读作"$A_n$ 无穷多次发生"（$A_n$ i.o.），下极限读作"$A_n$ 终究总是发生"。显然 $\liminf_nA_n\subset\limsup_nA_n$，并且 $(\limsup_nA_n)^{\mathsf c}=\liminf_nA_n^{\mathsf c}$。对单调事件列，上、下极限都等于 2.2.1 节定义的极限。

**定理 2.2.2** 对任意事件列 $\{A_n\}$，

$$
\mathbb{P}\Big(\limsup_{n\to\infty}A_n\Big)\ge\limsup_{n\to\infty}\mathbb{P}(A_n),\qquad\mathbb{P}\Big(\liminf_{n\to\infty}A_n\Big)\le\liminf_{n\to\infty}\mathbb{P}(A_n).
$$

**证明** 记 $B_n=\bigcup_{k=n}^\infty A_k$，则 $\{B_n\}$ 单调递减，$\lim_nB_n=\limsup_nA_n$。由连续性，$\mathbb{P}(\limsup_nA_n)=\lim_n\mathbb{P}(B_n)$。又由单调性，对一切 $k\ge n$，$\mathbb{P}(B_n)\ge\mathbb{P}(A_k)$，即 $\mathbb{P}(B_n)\ge\sup_{k\ge n}\mathbb{P}(A_k)$。令 $n\to\infty$（右端是关于 $n$ 单调递减的数列，极限存在）即得第一个不等式。对 $C_n=\bigcap_{k=n}^\infty A_k$ 同理可得第二个。 $\square$

### 2.2.3. Borel–Cantelli 引理

**定理 2.2.3（Borel–Cantelli 引理）** 设 $\{A_n\}$ 是事件列。

1. 若 $\sum_{n=1}^\infty\mathbb{P}(A_n)<\infty$，则 $\mathbb{P}(\limsup_{n\to\infty}A_n)=0$；
2. 若 $\{A_n\}$ 相互独立，且 $\sum_{n=1}^\infty\mathbb{P}(A_n)=\infty$，则 $\mathbb{P}(\limsup_{n\to\infty}A_n)=1$。

**证明** (1) 对每个 $n$，$\limsup_kA_k\subset\bigcup_{k=n}^\infty A_k$。由单调性和可列次可加性，$\mathbb{P}(\limsup_kA_k)\le\sum_{k=n}^\infty\mathbb{P}(A_k)$，而收敛级数的尾和当 $n\to\infty$ 时趋于零。(2) 用到事件列的独立性，证明见 [3.1.3](/3.1.3) 的定理 3.1.2。 $\square$

第 (1) 部分不需要任何独立性假设，是证明"几乎必然"成立的结论（如强大数定律，见 [3.1.12](/3.1.12)）的基本工具。

**例 2.2.1** 抛掷一枚均匀硬币无穷多次（样本空间是所有正反面无穷序列），记 $H_n$ 为"第 $n$ 次得到正面"，各次抛掷相互独立，$\mathbb{P}(H_n)=1/2$，$\sum_n\mathbb{P}(H_n)=\infty$。由 Borel–Cantelli 引理 (2)，$\mathbb{P}(\limsup_nH_n)=1$，即以概率 1 会出现无穷多次正面。能否从某次以后一直是正面呢？同理 $\mathbb{P}(\limsup_nH_n^{\mathsf c})=1$，于是

$$
\mathbb{P}\Big(\liminf_{n\to\infty}H_n\Big)=1-\mathbb{P}\Big(\limsup_{n\to\infty}H_n^{\mathsf c}\Big)=0,
$$
这几乎不可能。反之，若第 $n$ 次出现正面的概率是 $1/n^2$，则 $\sum_n1/n^2<\infty$，由 (1) 以概率 1 只出现有限次正面。

## 2.3. 条件概率

### 2.3.1. 定义

获得了新的信息之后，应当如何更新对事件的认识？

**例 2.3.1** 从 52 张扑克牌中任取一张，已知抽到梅花，求抽到 5 的概率。记 $A$ 为"抽到梅花"，$B$ 为"抽到 5"。不考虑条件时 $\mathbb{P}(A)=13/52$，$\mathbb{P}(A\cap B)=1/52$。已知 $A$ 发生后，可能的结果只剩 13 张梅花，且它们仍然等可能，所以所求概率为 $1/13$，记作 $\mathbb{P}(B\mid A)=1/13$。注意

$$
\mathbb{P}(B\mid A)=\frac1{13}=\frac{1/52}{13/52}=\frac{\mathbb{P}(A\cap B)}{\mathbb{P}(A)}.
$$

一般地，给定试验、样本空间和概率，若已知事件 $A$ 发生，希望知道事件 $B$ 发生的可能性，就构造一个新的概率，它顾及了 $A$ 发生的信息。

**定义 2.3.1（条件概率）** 设 $(\Omega,\mathcal{F},\mathbb{P})$ 是概率空间，$A,B\in\mathcal{F}$，$\mathbb{P}(A)>0$。称

$$
\mathbb{P}(B\mid A)=\frac{\mathbb{P}(A\cap B)}{\mathbb{P}(A)}
$$
为在事件 $A$ 发生的条件下事件 $B$ 发生的**条件概率**。

$\mathbb{P}(A)=0$ 时条件概率没有定义（有时根据需要把它规定为 $[0,1]$ 中的任意常数）。以概率为零的事件为条件的情形，将在 [3.1.9](/3.1.9) 的条件分布中借助密度处理。

**例 2.3.2** 连续两次抛掷均匀的四面体骰子，16 个结果等可能，$X$、$Y$ 为两次的点数。求 $\mathbb{P}(A\mid B)$，其中 $A=\{\max(X,Y)=m\}$，$B=\{\min(X,Y)=2\}$。$B=\{(2,2),(2,3),(2,4),(3,2),(4,2)\}$，$\#B=5$；$\#(A\cap B)$ 在 $m=1,2,3,4$ 时分别为 $0,1,2,2$。所以 $\mathbb{P}(A\mid B)$ 在 $m=1$ 时为 $0$，$m=2$ 时为 $1/5$，$m=3,4$ 时为 $2/5$。

### 2.3.2. 条件概率是概率测度

**定理 2.3.1** 设 $(\Omega,\mathcal{F},\mathbb{P})$ 是概率空间，$A\in\mathcal{F}$，$\mathbb{P}(A)>0$，则

1. 对任意 $B\in\mathcal{F}$，$\mathbb{P}(B\mid A)\ge0$；
2. $\mathbb{P}(\Omega\mid A)=1$；
3. 对两两互不相容的事件列 $\{B_i\}$，$\mathbb{P}\big(\bigcup_{i=1}^\infty B_i\mid A\big)=\sum_{i=1}^\infty\mathbb{P}(B_i\mid A)$。

**证明** (1)(2) 由定义直接得到。(3) 事件 $A\cap B_i$ 两两互不相容，由可列可加性，$\mathbb{P}(A\cap\bigcup_iB_i)=\mathbb{P}(\bigcup_i(A\cap B_i))=\sum_i\mathbb{P}(A\cap B_i)$，两边除以 $\mathbb{P}(A)$。 $\square$

记 $\mathbb{P}_A(\cdot)=\mathbb{P}(\cdot\mid A)$，则 $(\Omega,\mathcal{F},\mathbb{P}_A)$ 也是概率空间，所以 [3.1.1](/3.1.1) 中概率的所有性质对条件概率都成立，例如 $\mathbb{P}(B^{\mathsf c}\mid A)=1-\mathbb{P}(B\mid A)$。由于 $\mathbb{P}(A\mid A)=1$，条件概率完全集中在 $A$ 上，也可以把 $A$ 以外的结果排除掉，把 $(A,\ A\cap\mathcal{F},\ \mathbb{P}_A)$ 看作新的概率空间，其中 $A\cap\mathcal{F}=\{A\cap B\colon B\in\mathcal{F}\}$。例如在古典概型 $\Omega=\{1,2,3\}$ 中取 $A=\{1,2\}$，则 $\mathbb{P}(\{2\})=1/3$，而 $\mathbb{P}_A(\{2\})=1/2$，$\mathbb{P}_A(\{3\})=0$。

### 2.3.3. 条件概率与无条件概率

$\mathbb{P}(B\mid A)$ 与 $\mathbb{P}(B)$ 的大小关系不确定：当 $B\subset A$ 时，$\mathbb{P}(B\mid A)=\mathbb{P}(B)/\mathbb{P}(A)\ge\mathbb{P}(B)$；当 $A\cap B=\varnothing$ 时，$\mathbb{P}(B\mid A)=0\le\mathbb{P}(B)$。条件所含的信息越具体，对结论的影响可能越大，下面两个例子说明需要仔细地写出条件事件。

**例 2.3.3（二孩问题）** 一个家庭有两个孩子，样本空间 $\{(G,G),(G,B),(B,G),(B,B)\}$（按长幼排列，$G$ 为女孩，$B$ 为男孩）的四个结果等可能。

1. 已知老大是女孩，两个都是女孩的概率：条件事件为 $\{(G,G),(G,B)\}$，所求概率为 $1/2$。
2. 问父亲"你至少有一个女儿吗"，回答"是"。条件事件为 $\{(G,G),(G,B),(B,G)\}$，所求概率为 $1/3$。
3. 问父亲"你至少有一个叫 Lilia 的女儿吗"，回答"是"。设每个女孩独立地以很小的概率 $a$ 取名 Lilia，男孩不叫此名。记 $L$ 为"至少有一个叫 Lilia 的女儿"，$G_2$ 为"两个都是女孩"。每个孩子是叫 Lilia 的女孩的概率为 $a/2$，所以 $\mathbb{P}(L)=1-(1-a/2)^2=a-a^2/4$；两个都是女孩时至少一个叫 Lilia 的概率为 $1-(1-a)^2=2a-a^2$，所以 $\mathbb{P}(G_2\cap L)=\frac14(2a-a^2)$。于是
$$
\mathbb{P}(G_2\mid L)=\frac{(2a-a^2)/4}{a-a^2/4}=\frac{2-a}{4-a}\approx\frac12\quad(a\to0).
$$
罕见名字是关于某一个孩子的具体信息，效果接近于"指定了是哪一个孩子"，所以答案从 $1/3$ 变为接近 $1/2$。

**例 2.3.4** 抛掷一枚硬币两次。已知第一次是正面时两次都是正面的概率，不小于已知至少一次是正面时两次都是正面的概率吗？记 $A$、$B$ 为第一、二次是正面，则

$$
\mathbb{P}(A\cap B\mid A)=\frac{\mathbb{P}(A\cap B)}{\mathbb{P}(A)}\ge\frac{\mathbb{P}(A\cap B)}{\mathbb{P}(A\cup B)}=\mathbb{P}(A\cap B\mid A\cup B),
$$
无论硬币是否均匀都成立（均匀时两者为 $1/2$ 与 $1/3$）。一般地，若 $B\subset C$ 且 $A\cap B=A\cap C$，则 $\mathbb{P}(A\mid B)\ge\mathbb{P}(A\mid C)$。

## 2.4. 乘法公式

### 2.4.1. 乘法公式与序贯树形图

许多概率模型是用条件概率搭建的：先给出第一步的概率，再给出在第一步结果下第二步的条件概率，依此类推。

**例 2.4.1** 一台雷达探测其上空区域是否有飞机。记 $A$ 为"飞机出现"，$B$ 为"雷达报警"。已知 $\mathbb{P}(A)=0.05$，$\mathbb{P}(B\mid A)=0.99$，$\mathbb{P}(B\mid A^{\mathsf c})=0.10$。则 $\mathbb{P}(A\cap B)=\mathbb{P}(A)\mathbb{P}(B\mid A)=0.0495$，$\mathbb{P}(B)=0.05\times0.99+0.95\times0.10=0.1445$，雷达报警时确有飞机的概率为 $\mathbb{P}(A\mid B)=0.0495/0.1445\approx0.34$。

**定理 2.4.1（乘法公式）** 设 $(\Omega,\mathcal{F},\mathbb{P})$ 是概率空间，$A_1,\dots,A_n\in\mathcal{F}$，$\mathbb{P}(A_1\cap\cdots\cap A_{n-1})>0$，则

$$
\mathbb{P}\Big(\bigcap_{i=1}^nA_i\Big)=\mathbb{P}(A_1)\prod_{i=2}^n\mathbb{P}(A_i\mid A_1\cap\cdots\cap A_{i-1}).
$$

**证明** 由单调性，$\mathbb{P}(A_1)\ge\mathbb{P}(A_1\cap A_2)\ge\cdots\ge\mathbb{P}(A_1\cap\cdots\cap A_{n-1})>0$，所以式中的条件概率都有定义。把每个条件概率按定义写成两个概率之比，右端的乘积逐项相消，恰为 $\mathbb{P}(A_1\cap\cdots\cap A_n)$。 $\square$

由于事件的顺序可以任意调换，乘法公式实际上是 $n!$ 个公式；选择合适的顺序，使各个条件概率容易计算，是解题的关键。乘法公式对应序贯树形图的计算规则：

1. 画出序贯树形图，让关心的事件位于末端（叶子）；从根到叶子的路径上每个结点代表一个事件，关心的事件是沿路径一系列事件依次发生的结果；
2. 在每个分枝上写出相应的条件概率；
3. 叶子所代表事件的概率等于路径上各分枝条件概率的乘积。

例如统计语言模型把一个句子的概率写成逐词的条件概率之积：$\mathbb{P}(\text{Where are we going})=\mathbb{P}(\text{Where})\,\mathbb{P}(\text{are}\mid\text{Where})\,\mathbb{P}(\text{we}\mid\text{Where are})\,\mathbb{P}(\text{going}\mid\text{Where are we})$。

### 2.4.2. 配对问题

**例 2.4.2（配对问题）** 某人写了 $n$ 封信和 $n$ 个信封，把信随机装入信封（每个信封一封），求 (1) 没有一封信装对的概率 $q_0(n)$；(2) 恰有 $r$ 封信装对的概率 $q_r(n)$。

(1) 设 $A_i$ 为"第 $i$ 封信装对"。由乘法公式，$\mathbb{P}(A_i)=\frac1n$，$i<j$ 时 $\mathbb{P}(A_iA_j)=\mathbb{P}(A_i)\mathbb{P}(A_j\mid A_i)=\frac1n\cdot\frac1{n-1}=\frac{(n-2)!}{n!}$；一般地，任意指定的 $k$ 封都装对的概率为 $\frac{(n-k)!}{n!}$。由容斥恒等式（[3.1.1](/3.1.1) 性质 1.3.6），

$$
\mathbb{P}\Big(\bigcup_{i=1}^nA_i\Big)=\sum_{k=1}^n(-1)^{k-1}\binom nk\frac{(n-k)!}{n!}=\sum_{k=1}^n\frac{(-1)^{k-1}}{k!}=1-\frac1{2!}+\frac1{3!}-\cdots+\frac{(-1)^{n-1}}{n!},
$$
所以

$$
q_0(n)=1-\mathbb{P}\Big(\bigcup_{i=1}^nA_i\Big)=\sum_{k=0}^n\frac{(-1)^k}{k!}\ \longrightarrow\ \mathrm{e}^{-1}=0.36787944\cdots\quad(n\to\infty).
$$
$n$ 较大时 $q_0(n)\approx0.37$，几乎与 $n$ 无关。

(2) 指定的 $r$ 封（不妨设前 $r$ 封）都装对的概率相当于从 $n$ 个不同编号的球中无放回地取 $r$ 个、恰好依次取到前 $r$ 号的概率 $\frac1{n(n-1)\cdots(n-r+1)}$；在此条件下，其余 $n-r$ 封都装错的概率由 (1) 为 $q_0(n-r)$。再乘以选出这 $r$ 封的方法数 $\binom nr$，得

$$
q_r(n)=\binom nr\frac{1}{n(n-1)\cdots(n-r+1)}\sum_{k=0}^{n-r}\frac{(-1)^k}{k!}=\frac1{r!}\sum_{k=0}^{n-r}\frac{(-1)^k}{k!}\ \longrightarrow\ \frac{\mathrm{e}^{-1}}{r!}.
$$
极限正是 [3.1.4](/3.1.4) 中参数为 1 的 Poisson 分布。

![配对问题：左图为没有一封信装对的概率 q0(n) 迅速收敛到 1/e；右图为 n = 10 时装对封数的精确分布、极限 e^(-1)/r! 与 20000 次随机排列的频率](./plots/matching-problem.py)

## 2.5. 全概率公式

### 2.5.1. 定理

计算一个复杂事件的概率时，常按某种"原因"把样本空间分成几种情形，分别计算后再加权求和。

**定理 2.5.1（全概率公式）** 设 $(\Omega,\mathcal{F},\mathbb{P})$ 是概率空间，$A_1,\dots,A_n\in\mathcal{F}$ 是 $\Omega$ 的一个**划分**（$\bigcup_{i=1}^nA_i=\Omega$，$i\ne j$ 时 $A_i\cap A_j=\varnothing$），且 $\mathbb{P}(A_i)>0$。则对任意 $B\in\mathcal{F}$，

$$
\mathbb{P}(B)=\mathbb{P}(A_1)\mathbb{P}(B\mid A_1)+\cdots+\mathbb{P}(A_n)\mathbb{P}(B\mid A_n).
$$

**证明** $B=\bigcup_{i=1}^n(B\cap A_i)$，各项两两互不相容。由有限可加性和乘法公式，$\mathbb{P}(B)=\sum_i\mathbb{P}(B\cap A_i)=\sum_i\mathbb{P}(A_i)\mathbb{P}(B\mid A_i)$。 $\square$

特别地，若 $0<\mathbb{P}(A)<1$，则 $\mathbb{P}(B)=\mathbb{P}(A)\mathbb{P}(B\mid A)+\mathbb{P}(A^{\mathsf c})\mathbb{P}(B\mid A^{\mathsf c})$。由可列可加性，定理中的 $n$ 可以换成 $\infty$（可列划分）。应用的关键是找到合适的划分，它通常与问题的背景有关：在序贯树形图中，全概率公式就是把通向 $B$ 的所有叶子的概率相加。

### 2.5.2. 应用

**例 2.5.1** 袋中有 $n$ 个白球与 $m$ 个黑球，无放回地连续抽取，求第 $k$ 次取得黑球的概率（$1\le k\le n+m$）。设 $A_k$ 为"第 $k$ 次取得黑球"。

解法一（计数）：把球编号，从 $n+m$ 个球中依次取 $k$ 个排成一行，共 $P_{n+m}^k$ 种取法；第 $k$ 个位置是黑球有 $m$ 种取法，前 $k-1$ 个位置是其余 $n+m-1$ 个球中任意 $k-1$ 个的排列，有 $P_{n+m-1}^{k-1}$ 种。所以 $\mathbb{P}(A_k)=\dfrac{mP_{n+m-1}^{k-1}}{P_{n+m}^k}=\dfrac m{n+m}$。

解法二（归纳法与全概率公式）：对总次数归纳证明命题"无论开始时黑、白球各有多少，第 $k$ 次取得黑球的概率都等于开始时黑球的比例"。$k=1$ 显然。设命题对 $k$ 成立，按第一次的结果划分：

$$
\mathbb{P}(A_{k+1})=\frac m{n+m}\mathbb{P}(A_{k+1}\mid A_1)+\frac n{n+m}\mathbb{P}(A_{k+1}\mid A_1^{\mathsf c}).
$$
$\mathbb{P}(A_{k+1}\mid A_1)$ 是在 $m-1$ 个黑球与 $n$ 个白球的袋中第 $k$ 次取得黑球的概率，由归纳假设等于 $\frac{m-1}{n+m-1}$；同理 $\mathbb{P}(A_{k+1}\mid A_1^{\mathsf c})=\frac m{n+m-1}$。代入得 $\mathbb{P}(A_{k+1})=\frac{m(m-1)+nm}{(n+m)(n+m-1)}=\frac m{n+m}$。

结论（抽签与顺序无关）：无放回抽样时，每一次抽到黑球的概率都等于初始的黑球比例。

**例 2.5.2（Pólya 坛子）** Pólya 坛子（Pólya urn）里有 $b$ 个黑球、$r$ 个红球，每次任取一球，放回并再放入 $c$ 个与取出的球同色的球。记 $A_k$ 为"第 $k$ 次取出黑球"。用与例 2.5.1 解法二相同的归纳论证（按第一次的结果划分，归纳假设用于 $b+c$ 个黑球或 $r+c$ 个红球的坛子），可得对一切 $k$，$\mathbb{P}(A_k)=\frac b{b+r}$：

$$
\mathbb{P}(A_{k+1})=\frac b{b+r}\cdot\frac{b+c}{b+r+c}+\frac r{b+r}\cdot\frac b{b+r+c}=\frac b{b+r}.
$$
由乘法公式，前两次都取出黑球的概率为 $\frac b{b+r}\cdot\frac{b+c}{b+r+c}$。$c=-1$ 即无放回抽样，$c=0$ 即放回抽样。Pólya 坛子是传染病传播的一个简单模型：每次"感染"都使下一次同类事件更容易发生。

**例 2.5.3（敏感问题调查）** 调查家庭暴力（或服用兴奋剂等敏感问题）在家庭中所占的比例 $p$ 时，被调查者往往不愿如实回答。随机化回答（randomized response）的做法是：袋中红球的比例为 $p_0$，白球的比例为 $q_0=1-p_0$；被调查者从袋中任取一球、看后放回，约定取到红球就如实回答"是否有家庭暴力"，取到白球就回答相反的答案，并在匿名的调查表中只填"是"或"否"。没有人知道被调查者取到的是什么球。设每个家庭回答"是"的概率为 $p_1$。用 $B$ 表示回答"是"，$A$ 表示取到红球，由全概率公式，

$$
p_1=\mathbb{P}(B)=\mathbb{P}(A)\mathbb{P}(B\mid A)+\mathbb{P}(A^{\mathsf c})\mathbb{P}(B\mid A^{\mathsf c})=p_0p+q_0(1-p)=q_0+(p_0-q_0)p.
$$
所以只要 $p_0\ne q_0$，就有 $p=\dfrac{p_1-q_0}{p_0-q_0}$。实际中 $p_1$ 未知，若调查 $n$ 个家庭中有 $k$ 个回答"是"，可用 $\hat p_1=k/n$ 估计 $p_1$，从而用 $\hat p=\dfrac{\hat p_1-q_0}{p_0-q_0}$ 估计 $p$。例如袋中有 30 个红球、50 个白球，调查 320 个家庭有 195 个回答"是"，则 $p_0=3/8$，$q_0=5/8$，

$$
\hat p=\frac{195/320-5/8}{3/8-5/8}=6.25\%.
$$
$\lvert p_0-q_0\rvert$ 越大，估计越可靠（误差被 $1/\lvert p_0-q_0\rvert$ 放大得越少），但调查方案也越不容易被接受。

**例 2.5.4（换信封的策略）** 两个信封中各装有一个正整数金额（单位：元），两数不同，但具体是多少未知（看作未知常数）。你随机选一个信封，看到金额后可以决定是否换。策略：反复抛掷均匀硬币，记 $N$ 为首次出现正面所需的次数，令 $X=N+\frac12$；若所见金额小于 $X$ 就换。设两个金额为 $a>b$。看到金额 $x$ 时换的概率为 $f(x)=\mathbb{P}(N\ge x)=(1/2)^{x-1}$，关于 $x$ 严格递减。按第一次选到哪个信封划分，最终拿到较大金额 $a$ 的概率为

$$
\frac12\big(1-f(a)\big)+\frac12f(b)=\frac12+\frac12\big(f(b)-f(a)\big)>\frac12.
$$
任何严格递减的"换"的概率 $f$ 都有这个效果：随机阈值恰好落在 $b$ 与 $a$ 之间时，策略总是做出正确的决定。

## 2.6. Bayes 公式

### 2.6.1. 定理

全概率公式从"原因"推"结果"；反过来，已知结果 $B$ 发生了，要修正对各个原因 $A_i$ 的信念程度，就需要计算 $\mathbb{P}(A_i\mid B)$。例如 $B$ 是"影像检查发现阴影"，可能的原因 $A_1,A_2,A_3$ 是恶性肿瘤、良性肿瘤与其他原因。

**定理 2.6.1（Bayes 公式）** 设 $(\Omega,\mathcal{F},\mathbb{P})$ 是概率空间，$A_1,\dots,A_n$ 是 $\Omega$ 的一个划分，$\mathbb{P}(A_i)>0$，$B\in\mathcal{F}$，$\mathbb{P}(B)>0$。则

$$
\mathbb{P}(A_i\mid B)=\frac{\mathbb{P}(A_i)\mathbb{P}(B\mid A_i)}{\sum_{j=1}^n\mathbb{P}(A_j)\mathbb{P}(B\mid A_j)},\qquad i=1,\dots,n.
$$
特别地，若 $0<\mathbb{P}(A)<1$，则

$$
\mathbb{P}(A\mid B)=\frac{\mathbb{P}(A)\mathbb{P}(B\mid A)}{\mathbb{P}(A)\mathbb{P}(B\mid A)+\mathbb{P}(A^{\mathsf c})\mathbb{P}(B\mid A^{\mathsf c})}.
$$

**证明** 由条件概率的定义与乘法公式，$\mathbb{P}(A_i\mid B)=\mathbb{P}(A_i\cap B)/\mathbb{P}(B)=\mathbb{P}(A_i)\mathbb{P}(B\mid A_i)/\mathbb{P}(B)$，分母用全概率公式展开。 $\square$

$\mathbb{P}(A_i)$ 是得到信息 $B$ 之前对原因 $A_i$ 的信念，称为先验概率（prior probability）；$\mathbb{P}(A_i\mid B)$ 是得到信息之后的信念，称为后验概率（posterior probability）。Bayes 公式说明后验概率正比于先验概率与"在该原因下观察到 $B$ 的概率"之积。若信息分两次得到（先 $B_1$ 后 $B_2$），可以把第一次的后验概率当作第二次的先验概率再用一次 Bayes 公式，结果与一次性以 $B_1\cap B_2$ 为条件相同，所以信息的先后顺序不影响结果。

### 2.6.2. 假阳性之谜

**例 2.6.1（假阳性之谜）** 某种少见疾病在某人群中的患病率为 $0.001$。某检验方法的准确率为 $0.95$：患者检验呈阳性的概率为 $0.95$，非患者检验呈阴性的概率也是 $0.95$。从这一人群中随机抽取一人检验，结果为阳性，问此人患病的概率。记 $A$ 为"此人患病"，$B$ 为"检验呈阳性"。由 Bayes 公式，

$$
\mathbb{P}(A\mid B)=\frac{0.001\times0.95}{0.001\times0.95+0.999\times0.05}=0.01866\cdots\approx1.87\%.
$$
即使检验为阳性，患病的概率也不到 2%。原因是患病率很低而检验的准确性不够高：一千个人中约有 1 个患者，却有约 50 个非患者被误判为阳性。图中的曲线表明，后验概率主要由患病率和检验的特异性决定。

![检验为阳性时确实患病的概率随患病率（对数坐标）的变化，三条曲线对应不同的检验准确率；红点是例 2.6.1 的情形](./plots/false-positive.py)

Bayes 公式是贝叶斯统计（见 [3.2.7](/3.2.7)）的出发点：把未知参数看作随机的，由先验分布和数据得到后验分布。它也是贝叶斯网络（用有向图表示变量间的条件依赖关系）和传染病传播预测等许多模型的基础。

## 小结

| 内容 | 要点 |
|---|---|
| 概率空间 | 事件域 $\mathcal{F}$ 对可列次交、并、补封闭；概率测度满足非负性、规范性、可列可加性；不可列样本空间上存在不能分配概率的子集 |
| 连续性 | 单调事件列 $\mathbb{P}(\lim A_n)=\lim\mathbb{P}(A_n)$；上极限"无穷多次发生"、下极限"终究总是发生"；Borel–Cantelli 引理 |
| 条件概率 | $\mathbb{P}(B\mid A)=\mathbb{P}(A\cap B)/\mathbb{P}(A)$，$\mathbb{P}(\cdot\mid A)$ 仍是概率测度 |
| 三大公式 | 乘法公式（序贯树形图）、全概率公式（由因求果）、Bayes 公式（由果溯因） |

处理新概念时，可以类比熟悉的概念（数列的极限与事件列的极限），用简单的例子逐层拆解复杂的定义（事件列的上下极限）；计算时把复杂问题拆成简单的小问题，并根据经验选择使计算简便的条件顺序和样本空间的划分。
