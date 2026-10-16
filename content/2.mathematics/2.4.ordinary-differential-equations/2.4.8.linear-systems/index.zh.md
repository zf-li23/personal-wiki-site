---
title: 线性微分方程组
---

本章研究一阶**线性微分方程组** $\boldsymbol{x}'=A(t)\boldsymbol{x}+\boldsymbol{f}(t)$。它是一阶线性方程 $x'=a(t)x+f(t)$ 的向量形式，二者的相似不只是形式上的：解的整体存在性、"特解加齐次通解"的结构、常数变易公式都原样推广过来，只是数 $\mathrm{e}^{\int a}$ 换成了矩阵 $\Phi(t)$。线性方程组又是非线性理论的基础：非线性方程在平衡点附近的行为由它的线性化决定（[2.4.11](/2.4.11)），解对初值的导数满足线性的变分方程（[2.4.7](/2.4.7)）。下一章把 $n$ 阶线性方程作为本章的特例处理。

微积分中已经介绍过这些结果与常用解法（[2.2.16 的 16.6 节](/2.2.16#sec-16.6)），线性代数中用矩阵函数求解过常系数方程组（[2.1.11 的 11.9 节](/2.1.11#sec-11.9)）。本章给出严格的理论：整体存在唯一性的证明、解空间与基解矩阵、Liouville 公式、一般的常数变易公式、矩阵指数的收敛与性质，以及由 Jordan 标准形得到的解的结构；例行的计算从简，并指向上述两章。

## 8.1. 整体存在唯一性

### 8.1.1. 方程组与范数

**定义 8.1.1（线性微分方程组）** 设 $A(t)=(a_{ij}(t))$ 是区间 $I$ 上的 $n$ 阶函数矩阵，$\boldsymbol{f}(t)$ 是 $n$ 维函数向量，称

$$
\boldsymbol{x}'=A(t)\boldsymbol{x}+\boldsymbol{f}(t)\tag{8.1}
$$
为**线性微分方程组**。$\boldsymbol{f}\equiv\boldsymbol{0}$ 时称为齐次方程组

$$
\boldsymbol{x}'=A(t)\boldsymbol{x},\tag{8.2}
$$
否则称为非齐次方程组；$A$ 为常数矩阵时称为常系数方程组。以下总设 $A(t)$、$\boldsymbol{f}(t)$ 在 $I$ 上连续，允许取复数值。

函数矩阵的连续、求导与积分都逐个元素进行（[2.1.11 的 11.1 节](/2.1.11#sec-11.1)），乘积法则 $(AB)'=A'B+AB'$ 成立，但要注意矩阵乘法的次序。

估计需要范数。$\mathbb{C}^n$ 上取一个范数 $\|\boldsymbol{x}\|$（例如 $\sum_i\lvert x_i\rvert$ 或 Euclid 范数，有限维空间上各种范数等价），矩阵取相应的算子范数 $\|A\|=\max_{\|\boldsymbol{x}\|=1}\|A\boldsymbol{x}\|$。它是一个**矩阵范数**，满足

$$
\|A\boldsymbol{x}\|\le\|A\|\,\|\boldsymbol{x}\|,\qquad\|A+B\|\le\|A\|+\|B\|,\qquad\|AB\|\le\|A\|\,\|B\|,
$$
并且对向量值函数有 $\big\|\int_a^b\boldsymbol{g}(s)\,\mathrm{d}s\big\|\le\int_a^b\|\boldsymbol{g}(s)\|\,\mathrm{d}s$。常用的 $\sum_{i,j}\lvert a_{ij}\rvert$ 不是算子范数，但同样满足后两条不等式，下面的论证对它也成立。

### 8.1.2. 存在唯一性定理

一般的**存在唯一性定理**（[2.4.4](/2.4.4)、[2.4.7](/2.4.7)）只给出局部的解。线性方程组的特点是解在系数连续的整个区间上存在：它的右端关于 $\boldsymbol{x}$ 至多线性增长，解不会在有限时间内趋于无穷。

**定理 8.1.1** 设 $A(t)$、$\boldsymbol{f}(t)$ 在区间 $I$ 上连续，则对任意 $t_0\in I$、$\boldsymbol{\eta}\in\mathbb{C}^n$，**初值问题**

$$
\boldsymbol{x}'=A(t)\boldsymbol{x}+\boldsymbol{f}(t),\qquad\boldsymbol{x}(t_0)=\boldsymbol{\eta}
$$
在整个 $I$ 上存在唯一的解。

**证明** 初值问题等价于积分方程 $\boldsymbol{x}(t)=\boldsymbol{\eta}+\int_{t_0}^t\big(A(s)\boldsymbol{x}(s)+\boldsymbol{f}(s)\big)\,\mathrm{d}s$。任取含 $t_0$ 的有界闭区间 $J\subset I$，记 $L=\max_J\|A(t)\|$。作 Picard 逐次逼近

$$
\boldsymbol{x}_0(t)=\boldsymbol{\eta},\qquad\boldsymbol{x}_{k+1}(t)=\boldsymbol{\eta}+\int_{t_0}^t\big(A(s)\boldsymbol{x}_k(s)+\boldsymbol{f}(s)\big)\,\mathrm{d}s.
$$
它们都在整个 $J$ 上有定义且连续（这与非线性情形不同：那里需要限制在保证 $\boldsymbol{x}_k$ 不离开定义域的小区间上）。记 $M=\max_J\|\boldsymbol{x}_1(t)-\boldsymbol{x}_0(t)\|$，归纳可得

$$
\|\boldsymbol{x}_{k+1}(t)-\boldsymbol{x}_k(t)\|\le\Big\lvert\int_{t_0}^tL\|\boldsymbol{x}_k(s)-\boldsymbol{x}_{k-1}(s)\|\,\mathrm{d}s\Big\rvert\le\frac{ML^k\lvert t-t_0\rvert^k}{k!},\qquad t\in J.
$$
右边之和 $M\mathrm{e}^{L\lvert J\rvert}$ 有限，由 Weierstrass 判别法，$\boldsymbol{x}_k$ 在 $J$ 上**一致收敛**到连续函数 $\boldsymbol{x}(t)$；在积分方程中取极限，$\boldsymbol{x}$ 是解。

唯一性：设 $\boldsymbol{x},\boldsymbol{y}$ 是 $J$ 上的两个解，$\boldsymbol{z}=\boldsymbol{x}-\boldsymbol{y}$ 满足 $\boldsymbol{z}(t)=\int_{t_0}^tA(s)\boldsymbol{z}(s)\,\mathrm{d}s$。记 $K=\max_J\|\boldsymbol{z}\|$，代入右端反复估计得 $\|\boldsymbol{z}(t)\|\le K L^k\lvert t-t_0\rvert^k/k!\to0$，所以 $\boldsymbol{z}\equiv\boldsymbol{0}$。

最后，$J$ 是 $I$ 中任意含 $t_0$ 的有界闭区间，不同 $J$ 上的解由唯一性在公共部分重合，拼起来就是 $I$ 上的唯一解。 $\square$

从证明还得到解的估计（也可由 Gronwall 不等式得到，[2.4.7](/2.4.7)）：

$$
\|\boldsymbol{x}(t)\|\le\Big(\|\boldsymbol{\eta}\|+\Big\lvert\int_{t_0}^t\|\boldsymbol{f}(s)\|\,\mathrm{d}s\Big\rvert\Big)\mathrm{e}^{L\lvert t-t_0\rvert},\qquad t\in J.
$$

**注 8.1.1** 线性是关键。$x'=x^2$ 的右端在全平面上光滑，但满足 $x(0)=1$ 的解 $x=\frac1{1-t}$ 只存在于 $t<1$。线性方程组的解则在 $I$ 内处处存在，奇性只能出现在系数的奇点处（例如 $t^2y''-2ty'+2y=0$ 化为标准形式后，系数在 $t=0$ 处不连续）。

复系数方程组的实部、虚部满足实系数方程组；反过来，$A$、$\boldsymbol{f}$ 为实值且 $\boldsymbol{\eta}$ 为实向量时，由唯一性解是实值的（它的共轭也是解）。

## 8.2. 齐次方程组的解空间

### 8.2.1. 解空间的维数

**定理 8.2.1（叠加原理）** 记 $\mathcal{L}\boldsymbol{x}=\boldsymbol{x}'-A(t)\boldsymbol{x}$，它是从 $C^1(I)$ 到 $C(I)$（向量值函数空间）的线性映射。因此

1. 齐次方程组 (8.2) 的解的线性组合仍是解；
2. 非齐次方程组 (8.1) 的两个解之差是齐次方程组 (8.2) 的解；若 $\boldsymbol{x}^*$ 是 (8.1) 的一个解，则 (8.1) 的全部解为 $\boldsymbol{x}^*+\boldsymbol{x}$，$\boldsymbol{x}$ 取遍 (8.2) 的解。

**定理 8.2.2** 齐次方程组 (8.2) 的全部解构成 $n$ 维线性空间 $S$。对任意 $t_0\in I$，映射

$$
\boldsymbol{x}\mapsto\boldsymbol{x}(t_0),\qquad S\to\mathbb{C}^n
$$
是线性同构（实系数且只考虑实解时为 $S\to\mathbb{R}^n$）。

**证明** 由叠加原理 $S$ 是线性空间，映射显然线性。由定理 8.1.1 的存在性它是满射，由唯一性它是单射。 $\square$

这个同构把关于解的问题化为关于初值向量的线性代数问题。特别地：

- $m$ 个解 $\boldsymbol{\varphi}_1,\dots,\boldsymbol{\varphi}_m$ 线性无关，当且仅当它们在某一点（从而在每一点）的值 $\boldsymbol{\varphi}_1(t_0),\dots,\boldsymbol{\varphi}_m(t_0)$ 线性无关；
- 一个解若在某点为 $\boldsymbol{0}$，则它恒为 $\boldsymbol{0}$。

### 8.2.2. 基解矩阵与 Liouville 公式

**定义 8.2.1（基解矩阵）** 齐次方程组 (8.2) 的 $n$ 个线性无关的解 $\boldsymbol{\varphi}_1,\dots,\boldsymbol{\varphi}_n$ 称为一个**基本解组**；以它们为列的矩阵 $\Phi(t)=(\boldsymbol{\varphi}_1(t),\dots,\boldsymbol{\varphi}_n(t))$ 称为一个**基解矩阵**，满足 $\Phi(t_0)=I$ 的基解矩阵称为（在 $t_0$ 处的）**标准基解矩阵**。$n$ 个解的 **Wronski 行列式**是 $W(t)=\det\Phi(t)$。

以 $n$ 个解为列的矩阵 $Y(t)$ 满足矩阵方程 $Y'=A(t)Y$（逐列看即可），称为解矩阵；反之，矩阵方程的解的每一列都是 (8.2) 的解。

**定理 8.2.3** 设 $Y(t)$ 是 (8.2) 的解矩阵，则下列条件等价：

1. $Y$ 的各列线性无关，即 $Y$ 是基解矩阵；
2. 对一切 $t\in I$，$\det Y(t)\ne0$；
3. 存在 $t_0\in I$，$\det Y(t_0)\ne0$。

因此解矩阵的 Wronski 行列式要么恒为零，要么处处不为零。

**证明** 由定理 8.2.2，各列线性无关当且仅当它们在任意一点的值线性无关，即 $\det Y(t)\ne0$；而这对某一点成立就对每一点成立。 $\square$

这一结论对任意函数向量不成立：$(t,1)^{\mathsf T}$ 与 $(t^2,t)^{\mathsf T}$ 在 $\mathbb{R}$ 上线性无关，但 $\det\begin{bmatrix}t&t^2\\1&t\end{bmatrix}\equiv0$。它们不可能是同一个连续系数齐次方程组的解。

Wronski 行列式满足一个一阶线性方程，因而有显式表达式。

**定理 8.2.4（Liouville 公式）** 设 $Y(t)$ 是 (8.2) 的解矩阵，$t_0\in I$，则

$$
\det Y(t)=\det Y(t_0)\exp\Big(\int_{t_0}^t\operatorname{tr}(A(s))\,\mathrm{d}s\Big).\tag{8.3}
$$

**证明** 行列式对每一行是线性的，由乘积法则，$\frac{\mathrm{d}}{\mathrm{d}t}\det Y$ 等于把 $\det Y$ 的第 $i$ 行换成该行的导数所得的 $n$ 个行列式之和。由 $Y'=AY$，$Y'$ 的第 $i$ 行是 $\sum_ja_{ij}\cdot(Y\text{ 的第 }j\text{ 行})$；在第 $i$ 个行列式中减去其他行的倍数，只剩 $a_{ii}\cdot(\text{第 }i\text{ 行})$，该行列式等于 $a_{ii}\det Y$。所以

$$
(\det Y)'=\big(a_{11}+\cdots+a_{nn}\big)\det Y=\operatorname{tr}(A(t))\det Y,
$$
解这个一阶线性方程即得 (8.3)。 $\square$

Liouville 公式重新证明了"$\det Y$ 恒为零或处处非零"。几何上，$\lvert\det Y(t)\rvert$ 是解的流把单位体积的初值集合送到时刻 $t$ 后的体积，$\operatorname{tr}(A)$ 是体积的瞬时膨胀率（向量场 $A\boldsymbol{x}$ 的散度）。

**定理 8.2.5** 设 $\Phi(t)$ 是 (8.2) 的基解矩阵。

1. 对任意可逆常数矩阵 $C$，$\Phi(t)C$ 也是基解矩阵；反之，任一基解矩阵 $\Psi(t)$ 都可写成 $\Psi=\Phi C$，$C=\Phi^{-1}(t_0)\Psi(t_0)$ 是可逆常数矩阵；
2. (8.2) 的通解为 $\boldsymbol{x}=\Phi(t)\boldsymbol{c}$，$\boldsymbol{c}$ 为任意常向量；满足 $\boldsymbol{x}(t_0)=\boldsymbol{\eta}$ 的解为 $\boldsymbol{x}(t)=\Phi(t)\Phi^{-1}(t_0)\boldsymbol{\eta}$。

**证明** 1：$(\Phi C)'=A\Phi C$，$\det(\Phi C)=\det\Phi\det C\ne0$。反之，由 $\Phi\Phi^{-1}=I$ 求导得 $(\Phi^{-1})'=-\Phi^{-1}\Phi'\Phi^{-1}=-\Phi^{-1}A$，于是

$$
(\Phi^{-1}\Psi)'=-\Phi^{-1}A\Psi+\Phi^{-1}A\Psi=O,
$$
$\Phi^{-1}\Psi$ 是常数矩阵。2：$\Phi\boldsymbol{c}$ 是解；任一解 $\boldsymbol{x}$ 与 $\Phi(t)\Phi^{-1}(t_0)\boldsymbol{x}(t_0)$ 在 $t_0$ 处的值相同，由唯一性二者相等。 $\square$

二元函数 $R(t,s)=\Phi(t)\Phi^{-1}(s)$ 与基解矩阵的选取无关（$\Phi C(\Phi C)^{-1}=\Phi\Phi^{-1}$），它是在 $s$ 处的标准基解矩阵，把时刻 $s$ 的状态送到时刻 $t$ 的状态，在控制理论中称为状态转移矩阵。由定义

$$
R(t,t)=I,\qquad R(t,s)R(s,r)=R(t,r),\qquad R(t,s)^{-1}=R(s,t).
$$

**例 8.2.1** 方程组

$$
\boldsymbol{x}'=\begin{bmatrix}0&1\\-\dfrac{2}{t^2}&\dfrac{2}{t}\end{bmatrix}\boldsymbol{x},\qquad t>0
$$
来自 Euler 方程 $t^2y''-2ty'+2y=0$（$\boldsymbol{x}=(y,y')^{\mathsf T}$），后者有解 $t$、$t^2$。于是

$$
\Phi(t)=\begin{bmatrix}t&t^2\\1&2t\end{bmatrix},\qquad\det\Phi(t)=t^2,
$$
与 Liouville 公式一致：$\operatorname{tr}(A)=\frac2t$，$\det\Phi(1)\exp\big(\int_1^t\frac2s\,\mathrm{d}s\big)=t^2$。在 $t_0=1$ 处的标准基解矩阵为 $\Phi(t)\Phi^{-1}(1)=\begin{bmatrix}2t-t^2&t^2-t\\2-2t&2t-1\end{bmatrix}$。

变系数方程组一般没有求基解矩阵的通用方法。一个容易误用的"公式"是 $\exp\big(\int_{t_0}^tA(s)\,\mathrm{d}s\big)$：只有当 $A(t)$ 与 $\int_{t_0}^tA(s)\,\mathrm{d}s$ 可交换时它才是基解矩阵（例如 $A(t)=a(t)B$，$B$ 为常数矩阵）。上例中 $A(1)$ 与 $\int_1^2A(s)\,\mathrm{d}s$ 不可交换。

## 8.3. 非齐次方程组与常数变易公式

**定理 8.3.1（常数变易公式）** 设 $\Phi(t)$ 是 (8.2) 的基解矩阵，则非齐次方程组 (8.1) 满足 $\boldsymbol{x}(t_0)=\boldsymbol{\eta}$ 的解为

$$
\boldsymbol{x}(t)=\Phi(t)\Phi^{-1}(t_0)\boldsymbol{\eta}+\int_{t_0}^t\Phi(t)\Phi^{-1}(s)\boldsymbol{f}(s)\,\mathrm{d}s,\tag{8.4}
$$
(8.1) 的通解为 $\boldsymbol{x}(t)=\Phi(t)\boldsymbol{c}+\Phi(t)\int_{t_0}^t\Phi^{-1}(s)\boldsymbol{f}(s)\,\mathrm{d}s$，$\boldsymbol{c}$ 为任意常向量。

**证明** 推导：仿照一阶线性方程，把齐次通解 $\Phi(t)\boldsymbol{c}$ 中的常向量换成函数 $\boldsymbol{c}(t)$。代入 (8.1)：$\Phi'\boldsymbol{c}+\Phi\boldsymbol{c}'=A\Phi\boldsymbol{c}+\boldsymbol{f}$，由 $\Phi'=A\Phi$ 得 $\Phi\boldsymbol{c}'=\boldsymbol{f}$。$\Phi(s)$ 处处可逆，所以 $\boldsymbol{c}'(s)=\Phi^{-1}(s)\boldsymbol{f}(s)$，积分并由 $\boldsymbol{c}(t_0)=\Phi^{-1}(t_0)\boldsymbol{\eta}$ 得 (8.4)。

验证：记 (8.4) 右端为 $\boldsymbol{x}(t)=\Phi(t)\boldsymbol{c}(t)$，$\boldsymbol{c}(t)=\Phi^{-1}(t_0)\boldsymbol{\eta}+\int_{t_0}^t\Phi^{-1}(s)\boldsymbol{f}(s)\,\mathrm{d}s$。则 $\boldsymbol{x}'=A\Phi\boldsymbol{c}+\Phi\Phi^{-1}(t)\boldsymbol{f}(t)=A\boldsymbol{x}+\boldsymbol{f}$，且 $\boldsymbol{x}(t_0)=\boldsymbol{\eta}$。由定理 8.1.1 的唯一性，它就是所求的解。通解的形式由定理 8.2.1 得到。 $\square$

通解公式有时被误写作 $\Phi(t)\big(\boldsymbol{c}+\Phi(t)\int_{t_0}^t\Phi^{-1}\boldsymbol{f}\big)$，括号内多了一个 $\Phi(t)$；正确的是 (8.4)。

式 (8.4) 有清楚的含义：解 = 初值经齐次方程组演化的结果 + 每一时刻 $s$ 的输入 $\boldsymbol{f}(s)\,\mathrm{d}s$ 从时刻 $s$ 演化到时刻 $t$ 的结果之和。$R(t,s)=\Phi(t)\Phi^{-1}(s)$ 就是在时刻 $s$ 施加单位"冲量"后系统的响应，这一叠加原则在物理中称为 Duhamel 原理。由 (8.4) 还可以看出：非齐次方程组的解在 $\boldsymbol{\eta}$ 与 $\boldsymbol{f}$ 两个输入上都是线性的。

**例 8.3.1** 二阶方程 $y''+\omega^2y=g(t)$（$\omega>0$）化为方程组 $\boldsymbol{x}=(y,y')^{\mathsf T}$，

$$
\boldsymbol{x}'=\begin{bmatrix}0&1\\-\omega^2&0\end{bmatrix}\boldsymbol{x}+\begin{bmatrix}0\\g(t)\end{bmatrix},\qquad\Phi(t)=\begin{bmatrix}\cos\omega t&\sin\omega t\\-\omega\sin\omega t&\omega\cos\omega t\end{bmatrix}.
$$
$\det\Phi=\omega$，$\Phi(t)\Phi^{-1}(s)$ 的右上角元素为 $\frac{1}{\omega}\sin\omega(t-s)$。由 (8.4) 取第一个分量，满足 $y(0)=y'(0)=0$ 的解为

$$
y(t)=\frac1\omega\int_0^t\sin\omega(t-s)\,g(s)\,\mathrm{d}s.
$$
下一章把这种"核"的写法推广到一般的 $n$ 阶线性方程（定义 9.2.1）。具体的数值例子见 [2.2.16 的例 16.6.2](/2.2.16#ex-16.6.2)。

## 8.4. 矩阵指数

### 8.4.1. 定义与收敛性

$n=1$ 时 $x'=ax$ 的解是 $\mathrm{e}^{at}x_0$。对常系数方程组 $\boldsymbol{x}'=A\boldsymbol{x}$，自然猜想解为 $\mathrm{e}^{tA}\boldsymbol{x}_0$，为此需要定义矩阵的指数。

**定义 8.4.1（矩阵指数）** 对 $A\in\mathbb{C}^{n\times n}$，定义

$$
\mathrm{e}^{A}=\exp A=\sum_{k=0}^\infty\frac{A^k}{k!}=I+A+\frac{A^2}{2!}+\cdots+\frac{A^k}{k!}+\cdots.
$$

**定理 8.4.1** 对任意 $A$，级数 $\sum_k\frac{t^kA^k}{k!}$ 在每个有界区间 $\lvert t\rvert\le T$ 上一致绝对收敛；它的和 $\mathrm{e}^{tA}$ 关于 $t$ 可微，且

$$
\frac{\mathrm{d}}{\mathrm{d}t}\mathrm{e}^{tA}=A\mathrm{e}^{tA}=\mathrm{e}^{tA}A.
$$

**证明** $\big\|\frac{t^kA^k}{k!}\big\|\le\frac{(T\|A\|)^k}{k!}$，而 $\sum_k\frac{(T\|A\|)^k}{k!}=\mathrm{e}^{T\|A\|}$ 收敛。由 Weierstrass 判别法（对每个元素也成立，因为元素的绝对值不超过某个常数乘以矩阵范数），级数在 $\lvert t\rvert\le T$ 上一致绝对收敛。逐项求导所得级数 $\sum_{k\ge1}\frac{t^{k-1}A^k}{(k-1)!}=A\sum_{j\ge0}\frac{t^jA^j}{j!}$ 同样一致收敛，所以可以逐项求导，导数为 $A\mathrm{e}^{tA}$；把 $A$ 提到右边同理。 $\square$

在 [2.1.11](/2.1.11#sec-11.8) 中，矩阵指数作为矩阵函数的特例，由谱定义或插值法计算；这里的级数定义与之一致。

### 8.4.2. 性质

**定理 8.4.2** 设 $A,B\in\mathbb{C}^{n\times n}$，$P$ 可逆，$s,t\in\mathbb{R}$。

1. 若 $AB=BA$，则 $\mathrm{e}^{A+B}=\mathrm{e}^A\mathrm{e}^B$；
2. $\mathrm{e}^{(s+t)A}=\mathrm{e}^{sA}\mathrm{e}^{tA}$；$\mathrm{e}^{A}$ 可逆且 $(\mathrm{e}^A)^{-1}=\mathrm{e}^{-A}$；
3. $\mathrm{e}^{PAP^{-1}}=P\mathrm{e}^AP^{-1}$；
4. $\det\mathrm{e}^{tA}=\mathrm{e}^{t\operatorname{tr}(A)}$。

**证明** 用微分方程的唯一性证明，避免重排级数。

1：$B$ 与 $A$ 的每个幂可交换，所以与 $\mathrm{e}^{tA}$ 可交换。令 $Z(t)=\mathrm{e}^{tA}\mathrm{e}^{tB}$，则

$$
Z'=A\mathrm{e}^{tA}\mathrm{e}^{tB}+\mathrm{e}^{tA}B\mathrm{e}^{tB}=(A+B)Z,\qquad Z(0)=I.
$$
$\mathrm{e}^{t(A+B)}$ 满足同一个矩阵初值问题（逐列看是 $\boldsymbol{x}'=(A+B)\boldsymbol{x}$ 的初值问题），由唯一性 $Z(t)=\mathrm{e}^{t(A+B)}$，取 $t=1$。

2：$sA$ 与 $tA$ 可交换，由 1 得第一式；取 $s=-t$ 得 $\mathrm{e}^{tA}\mathrm{e}^{-tA}=\mathrm{e}^{O}=I$。

3：$(PAP^{-1})^k=PA^kP^{-1}$，逐项相等。

4：$\mathrm{e}^{tA}$ 是 $\boldsymbol{x}'=A\boldsymbol{x}$ 的解矩阵（定理 8.4.1），由 Liouville 公式 $\det\mathrm{e}^{tA}=\det I\cdot\mathrm{e}^{\int_0^t\operatorname{tr}(A)\,\mathrm{d}s}$。 $\square$

可交换的条件不能去掉，反例见 [2.1.11 的定理 11.8.1](/2.1.11#thm-11.8.1) 之后。第 2 条说明 $t\mapsto\mathrm{e}^{tA}$ 是从加法群 $(\mathbb{R},+)$ 到可逆矩阵乘法群的同态，$\{\mathrm{e}^{tA}\}_{t\in\mathbb{R}}$ 称为单参数子群。

### 8.4.3. 常系数方程组的解

**定理 8.4.3** $\mathrm{e}^{tA}$ 是常系数方程组 $\boldsymbol{x}'=A\boldsymbol{x}$ 在 $t=0$ 处的标准基解矩阵。因此：

1. 满足 $\boldsymbol{x}(t_0)=\boldsymbol{\eta}$ 的解为 $\boldsymbol{x}(t)=\mathrm{e}^{(t-t_0)A}\boldsymbol{\eta}$；
2. 任一基解矩阵 $\Phi$ 满足 $\Phi(t)\Phi^{-1}(s)=\mathrm{e}^{(t-s)A}$，特别地 $\mathrm{e}^{tA}=\Phi(t)\Phi^{-1}(0)$；
3. $\boldsymbol{x}'=A\boldsymbol{x}+\boldsymbol{f}(t)$ 满足 $\boldsymbol{x}(t_0)=\boldsymbol{\eta}$ 的解为

$$
\boldsymbol{x}(t)=\mathrm{e}^{(t-t_0)A}\boldsymbol{\eta}+\int_{t_0}^t\mathrm{e}^{(t-s)A}\boldsymbol{f}(s)\,\mathrm{d}s.\tag{8.5}
$$

**证明** 由定理 8.4.1，$(\mathrm{e}^{tA})'=A\mathrm{e}^{tA}$，且 $\mathrm{e}^{0A}=I$。$\mathrm{e}^{tA}\mathrm{e}^{-sA}=\mathrm{e}^{(t-s)A}$ 是在 $s$ 处的标准基解矩阵，而 $\Phi(t)\Phi^{-1}(s)$ 与基解矩阵的选取无关，所以二者相等。1、3 由定理 8.2.5、定理 8.3.1 得到。 $\square$

$R(t,s)$ 只依赖于 $t-s$，这反映了常系数方程组的时间平移不变性：若 $\boldsymbol{x}(t)$ 是解，则 $\boldsymbol{x}(t+c)$ 也是解。式 (8.5) 就是 [2.1.11 的式 (11.3)](/2.1.11#eq-11.3)。

第 2 条给出计算 $\mathrm{e}^{tA}$ 的一种方法：先用特征向量等方法求出任意一个基解矩阵 $\Phi$，再算 $\Phi(t)\Phi^{-1}(0)$。

## 8.5. 用 Jordan 标准形计算 $\mathrm{e}^{tA}$

### 8.5.1. Jordan 块的指数

由**Jordan 标准形**，存在可逆矩阵 $P$ 使 $P^{-1}AP=J=\operatorname{diag}(J_1,\dots,J_s)$，其中 $J_i=J_{\lambda_i,m_i}$ 是 $m_i$ 阶 **Jordan 块**（[2.1.10](/2.1.10)）。由定理 8.4.2 的第 3 条，

$$
\mathrm{e}^{tA}=P\mathrm{e}^{tJ}P^{-1},\qquad\mathrm{e}^{tJ}=\operatorname{diag}\big(\mathrm{e}^{tJ_1},\dots,\mathrm{e}^{tJ_s}\big)
$$
（分块对角矩阵的幂按块计算）。

**定理 8.5.1** 设 $J_{\lambda,m}=\lambda I+N$，$N$ 是上次对角线为 1、其余为 0 的 $m$ 阶矩阵，则

$$
\mathrm{e}^{tJ_{\lambda,m}}=\mathrm{e}^{\lambda t}\sum_{k=0}^{m-1}\frac{t^k}{k!}N^k=\mathrm{e}^{\lambda t}\begin{bmatrix}1&t&\dfrac{t^2}{2!}&\cdots&\dfrac{t^{m-1}}{(m-1)!}\\&1&t&\cdots&\dfrac{t^{m-2}}{(m-2)!}\\&&\ddots&\ddots&\vdots\\&&&1&t\\&&&&1\end{bmatrix}.
$$

**证明** $\lambda I$ 与 $N$ 可交换，由定理 8.4.2 的第 1 条 $\mathrm{e}^{tJ}=\mathrm{e}^{\lambda t}\mathrm{e}^{tN}$。$N^k$ 是第 $k$ 条上对角线为 1 的矩阵，$N^m=O$，所以 $\mathrm{e}^{tN}$ 的级数只有前 $m$ 项。 $\square$

$P\mathrm{e}^{tJ}$ 也是基解矩阵（定理 8.2.5），它的列可以直接写出：$P$ 中对应于 $J_{\lambda,m}$ 的列 $\boldsymbol{p}_1,\dots,\boldsymbol{p}_m$ 是一条 **Jordan 链**（$(A-\lambda I)\boldsymbol{p}_1=\boldsymbol{0}$，$(A-\lambda I)\boldsymbol{p}_{k+1}=\boldsymbol{p}_k$），给出 $m$ 个解

$$
\mathrm{e}^{\lambda t}\boldsymbol{p}_1,\quad\mathrm{e}^{\lambda t}(t\boldsymbol{p}_1+\boldsymbol{p}_2),\quad\dots,\quad\mathrm{e}^{\lambda t}\sum_{j=1}^m\frac{t^{m-j}}{(m-j)!}\boldsymbol{p}_j.
$$
这就是 [2.1.11 的推论 11.9.1](/2.1.11#cor-11.9.1)。$A$ **可对角化**时所有块都是一阶的，基本解组为 $\mathrm{e}^{\lambda_kt}\boldsymbol{r}_k$（特征向量法，[2.2.16 的定理 16.6.5](/2.2.16#thm-16.6.5)）；实矩阵的复特征值取 $\mathrm{e}^{\lambda t}\boldsymbol{r}$ 的实部与虚部得实解。

### 8.5.2. 解的结构与增长估计

下面的推论是下一章常系数方程理论与第 11 章稳定性理论的基础。

**推论 8.5.1** 设 $A$ 的互不相同的特征值为 $\lambda_1,\dots,\lambda_r$，$\lambda_j$ 对应的最大 Jordan 块的阶数为 $m_j$（即 $\lambda_j$ 在极小多项式中的重数）。

1. $\mathrm{e}^{tA}$ 的每个元素（从而 $\boldsymbol{x}'=A\boldsymbol{x}$ 的每个解的每个分量）都形如 $\sum_{j=1}^rp_j(t)\mathrm{e}^{\lambda_jt}$，$p_j$ 是次数小于 $m_j$ 的多项式；
2. 记 $\mu=\max_j\operatorname{Re}\lambda_j$。对任意 $\varepsilon>0$，存在常数 $C$ 使

$$
\|\mathrm{e}^{tA}\|\le C\mathrm{e}^{(\mu+\varepsilon)t},\qquad t\ge0;
$$
若实部等于 $\mu$ 的特征值都是**半单特征值**（Jordan 块都是一阶的），可以取 $\varepsilon=0$。

**证明** 1：$\mathrm{e}^{tA}=P\mathrm{e}^{tJ}P^{-1}$，由定理 8.5.1，$\mathrm{e}^{tJ}$ 的元素是 $\frac{t^k}{k!}\mathrm{e}^{\lambda_jt}$（$k<m_j$）或 $0$，左乘、右乘常数矩阵后得到它们的线性组合。2：$\lvert t^k\mathrm{e}^{\lambda_jt}\rvert=t^k\mathrm{e}^{t\operatorname{Re}\lambda_j}\le C_\varepsilon\mathrm{e}^{(\mu+\varepsilon)t}$，因为 $t^k\mathrm{e}^{-\varepsilon t}$ 在 $t\ge0$ 上有界；若实部为 $\mu$ 的特征值只有一阶块，这些项中 $k=0$，不需要 $\varepsilon$。各元素有界推出范数有界。 $\square$

特征值决定了 $t\to+\infty$ 时的指数增长率，但不是全部信息：Jordan 块带来多项式因子 $t^k$，非正规矩阵（[2.1.12](/2.1.12)）还会使 $\|\mathrm{e}^{tA}\|$ 在衰减之前先经历可观的暂时增长（下图右）。

![左：Jordan 块 A = J_{-0.5,3} 的指数 e^{tA} 第一行的三个元素 e^{-t/2}、t e^{-t/2}、(t^2/2) e^{-t/2}，多项式因子使后两项先增长、后衰减；右：‖e^{tA}‖（谱范数）对 A = [[-1, a], [0, -2]] 的变化，两个特征值都是负的，a 越大暂时增长越明显，正规矩阵 a = 0 时单调衰减](./plots/matrix-exponential-growth.py)

### 8.5.3. 根子空间分解法

求 $P$ 与 $P^{-1}$ 往往很麻烦。只需要解 $\mathrm{e}^{tA}\boldsymbol{\eta}$ 时，可以用**根子空间**分解代替 Jordan 基。

**定理 8.5.2** 设 $A$ 的互不相同的特征值为 $\lambda_1,\dots,\lambda_r$，代数重数为 $n_1,\dots,n_r$，根子空间 $V_j=\mathcal{N}\big((A-\lambda_jI)^{n_j}\big)$。把初值分解为 $\boldsymbol{\eta}=\boldsymbol{\eta}_1+\cdots+\boldsymbol{\eta}_r$，$\boldsymbol{\eta}_j\in V_j$，则

$$
\mathrm{e}^{tA}\boldsymbol{\eta}=\sum_{j=1}^r\mathrm{e}^{\lambda_jt}\sum_{k=0}^{n_j-1}\frac{t^k}{k!}(A-\lambda_jI)^k\boldsymbol{\eta}_j.\tag{8.6}
$$

**证明** $\mathbb{C}^n=V_1\oplus\cdots\oplus V_r$（[2.1.10](/2.1.10)），所以分解存在且唯一。$\lambda_jI$ 与 $A-\lambda_jI$ 可交换，

$$
\mathrm{e}^{tA}\boldsymbol{\eta}_j=\mathrm{e}^{\lambda_jt}\mathrm{e}^{t(A-\lambda_jI)}\boldsymbol{\eta}_j=\mathrm{e}^{\lambda_jt}\sum_{k=0}^\infty\frac{t^k}{k!}(A-\lambda_jI)^k\boldsymbol{\eta}_j,
$$
而 $(A-\lambda_jI)^k\boldsymbol{\eta}_j=\boldsymbol{0}$（$k\ge n_j$），级数只有有限项。对 $j$ 求和即得。 $\square$

取 $\boldsymbol{\eta}$ 为标准基向量 $\boldsymbol{e}_1,\dots,\boldsymbol{e}_n$，就得到 $\mathrm{e}^{tA}$ 的各列。这一方法只需要解线性方程组求 $V_j$ 的基并分解向量，不需要求 Jordan 链。

**例 8.5.1** $A=\begin{bmatrix}3&-1\\1&1\end{bmatrix}$。特征多项式 $(\lambda-2)^2$，只有一个特征值，$V_1=\mathbb{C}^2$，$(A-2I)^2=O$（Cayley–Hamilton）。由 (8.6)

$$
\mathrm{e}^{tA}=\mathrm{e}^{2t}\big(I+t(A-2I)\big)=\mathrm{e}^{2t}\begin{bmatrix}1+t&-t\\t&1-t\end{bmatrix}.
$$
与 [2.2.16 的例 16.6.5](/2.2.16#ex-16.6.5) 用消元法得到的通解一致。

**例 8.5.2** 求 $\mathrm{e}^{tA}$，$A=\begin{bmatrix}2&1&1\\0&2&1\\0&0&3\end{bmatrix}$。特征值 $2$（二重）、$3$（单）。$N=A-2I=\begin{bmatrix}0&1&1\\0&0&1\\0&0&1\end{bmatrix}$，$N^2=\begin{bmatrix}0&0&2\\0&0&1\\0&0&1\end{bmatrix}$，$V_1=\mathcal{N}(N^2)=\operatorname{span}\{\boldsymbol{e}_1,\boldsymbol{e}_2\}$，$V_2=\mathcal{N}(A-3I)=\operatorname{span}\{(2,1,1)^{\mathsf T}\}$。

- $\boldsymbol{e}_1,\boldsymbol{e}_2\in V_1$：$\mathrm{e}^{tA}\boldsymbol{e}_1=\mathrm{e}^{2t}(\boldsymbol{e}_1+tN\boldsymbol{e}_1)=\mathrm{e}^{2t}\boldsymbol{e}_1$，$\mathrm{e}^{tA}\boldsymbol{e}_2=\mathrm{e}^{2t}(\boldsymbol{e}_2+t\boldsymbol{e}_1)$；
- $\boldsymbol{e}_3=(2,1,1)^{\mathsf T}+(-2,-1,0)^{\mathsf T}$，后者属于 $V_1$，$N(-2,-1,0)^{\mathsf T}=(-1,0,0)^{\mathsf T}$。所以 $\mathrm{e}^{tA}\boldsymbol{e}_3=\mathrm{e}^{3t}(2,1,1)^{\mathsf T}+\mathrm{e}^{2t}(-2-t,-1,0)^{\mathsf T}$。

合起来

$$
\mathrm{e}^{tA}=\begin{bmatrix}\mathrm{e}^{2t}&t\mathrm{e}^{2t}&2\mathrm{e}^{3t}-(2+t)\mathrm{e}^{2t}\\0&\mathrm{e}^{2t}&\mathrm{e}^{3t}-\mathrm{e}^{2t}\\0&0&\mathrm{e}^{3t}\end{bmatrix}.
$$
可以检验 $\det\mathrm{e}^{tA}=\mathrm{e}^{7t}=\mathrm{e}^{t\operatorname{tr}(A)}$。

用插值法求 $\mathrm{e}^{tA}$（[2.1.11 的 11.6 节](/2.1.11#sec-11.6)）是第三种途径：$\mathrm{e}^{tA}=r(A)$，$r$ 是在 $A$ 的谱上与 $\mathrm{e}^{tz}$ 的值及若干阶导数相同的多项式。三种方法给出同一个矩阵。

## 小结

| 内容 | 结论 |
|---|---|
| 存在唯一性 | 系数在 $I$ 上连续 $\Rightarrow$ 初值问题的解在整个 $I$ 上存在唯一（定理 8.1.1） |
| 解空间 | 齐次解构成 $n$ 维空间，$\boldsymbol{x}\mapsto\boldsymbol{x}(t_0)$ 是同构（定理 8.2.2） |
| 基解矩阵 | $\Phi'=A\Phi$ 且 $\det\Phi\ne0$；两个基解矩阵相差可逆常数矩阵因子；$\det\Phi$ 满足 Liouville 公式 (8.3) |
| 非齐次方程组 | $\boldsymbol{x}=\Phi(t)\Phi^{-1}(t_0)\boldsymbol{\eta}+\int_{t_0}^t\Phi(t)\Phi^{-1}(s)\boldsymbol{f}(s)\,\mathrm{d}s$（式 (8.4)） |
| 矩阵指数 | 级数在有界区间上一致绝对收敛；可交换时 $\mathrm{e}^{A+B}=\mathrm{e}^A\mathrm{e}^B$；$\det\mathrm{e}^{tA}=\mathrm{e}^{t\operatorname{tr}(A)}$ |
| 常系数方程组 | $\mathrm{e}^{tA}$ 是标准基解矩阵；$\mathrm{e}^{tA}=P\mathrm{e}^{tJ}P^{-1}$，Jordan 块给出 $t^k\mathrm{e}^{\lambda t}$ |
| 增长估计 | $\Vert\mathrm{e}^{tA}\Vert\le C\mathrm{e}^{(\mu+\varepsilon)t}$，$\mu=\max\operatorname{Re}\lambda$（推论 8.5.1） |
| 计算方法 | Jordan 基；根子空间分解 (8.6)；插值法；先求任一 $\Phi$ 再算 $\Phi(t)\Phi^{-1}(0)$ |
