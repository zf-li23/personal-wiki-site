---
title: 高阶线性微分方程
---

$n$ 阶线性方程 $y^{(n)}+p_1(x)y^{(n-1)}+\cdots+p_n(x)y=f(x)$ 是物理与工程中最常见的方程类型：振动、电路、梁的弯曲、量子力学的定态方程都属于此类。令 $\boldsymbol{x}=(y,y',\dots,y^{(n-1)})^{\mathsf T}$，它化为一阶**线性微分方程组**，系数矩阵是**友矩阵**。因此上一章的全部理论直接适用：解的整体存在唯一性、解空间、Wronski 行列式与 Liouville 公式、常数变易公式。本章把这些结论翻译成 $n$ 阶方程的语言，重点是两个在应用中很有用的公式：用余子式写出的常数变易公式，以及由它得到的 Cauchy 核 $K(x,t)$，它把非齐次方程的特解写成 $\int K(x,t)f(t)\,\mathrm{d}t$。

已知齐次方程的一部分解时可以降阶；常系数方程与 Euler 方程可以完全解出，具体解法在微积分中已经详细讨论（[2.2.16](/2.2.16)），这里只补充理论上的说明。最后讨论 $y''+M^2y=f$ 的周期解，这是"共振"现象的精确表述。二阶方程零点的定性理论与边值问题见 [2.4.12](/2.4.12)，变系数方程的级数解见下一章。

## 9.1. 作为方程组的特例

### 9.1.1. 化为方程组与存在唯一性

本章总设 $p_1(x),\dots,p_n(x),f(x)$ 在区间 $I$ 上连续，记

$$
L(y)=y^{(n)}+p_1(x)y^{(n-1)}+\cdots+p_{n-1}(x)y'+p_n(x)y,
$$
考虑非齐次方程与齐次方程

$$
L(y)=f(x),\tag{9.1}
$$

$$
L(y)=0.\tag{9.2}
$$
$y$ 是 (9.1) 的解当且仅当 $\boldsymbol{x}=(y,y',\dots,y^{(n-1)})^{\mathsf T}$ 是方程组

$$
\boldsymbol{x}'=C(x)\boldsymbol{x}+f(x)\boldsymbol{e}_n,\qquad C(x)=\begin{bmatrix}0&1&&\\&\ddots&\ddots&\\&&0&1\\-p_n&-p_{n-1}&\cdots&-p_1\end{bmatrix}\tag{9.3}
$$
的解，$\boldsymbol{e}_n=(0,\dots,0,1)^{\mathsf T}$。由定理 8.1.1：

**定理 9.1.1** 对任意 $x_0\in I$ 与 $\eta_0,\dots,\eta_{n-1}\in\mathbb{C}$，方程 (9.1) 满足 $y^{(k)}(x_0)=\eta_k$（$k=0,\dots,n-1$）的解在整个 $I$ 上存在且唯一。

### 9.1.2. 基本解组与 Wronski 行列式

$y_1,\dots,y_n$ 是 (9.2) 的解，当且仅当 $(y_k,y_k',\dots,y_k^{(n-1)})^{\mathsf T}$ 是 (9.3) 的齐次方程组的解；数值函数组的线性相关性与对应向量函数组的线性相关性相同（第一个分量的线性关系求导后对其余分量也成立）。对应的解矩阵的行列式就是函数组的 **Wronski 行列式**

$$
W(x)=W[y_1,\dots,y_n](x)=\begin{vmatrix}y_1&y_2&\cdots&y_n\\y_1'&y_2'&\cdots&y_n'\\\vdots&\vdots&&\vdots\\y_1^{(n-1)}&y_2^{(n-1)}&\cdots&y_n^{(n-1)}\end{vmatrix}.
$$
友矩阵的迹为 $-p_1$，由定理 8.2.2—定理 8.2.4 得到：

**定理 9.1.2** 

1. 齐次方程 (9.2) 的解构成 $n$ 维线性空间，$y\mapsto(y(x_0),\dots,y^{(n-1)}(x_0))$ 是它到 $\mathbb{C}^n$ 的同构；
2. (9.2) 的 $n$ 个解 $y_1,\dots,y_n$ 线性无关（构成**基本解组**）$\Leftrightarrow$ $W\ne0$ 在某一点成立 $\Leftrightarrow$ $W\ne0$ 在每一点成立；
3. （**Liouville 公式**）$W(x)=W(x_0)\exp\Big(-\displaystyle\int_{x_0}^xp_1(t)\,\mathrm{d}t\Big)$；
4. 若 $y_1,\dots,y_n$ 是基本解组，$y^*$ 是 (9.1) 的一个解，则 (9.1) 的全部解为 $y=y^*+C_1y_1+\cdots+C_ny_n$。

对一般函数组，$W\equiv0$ 不能推出线性相关（[2.2.16 的命题 16.1.1](/2.2.16#prop-16.1.1) 之后的例子）；第 2 条说明解的情形不同。二阶方程的 Liouville 公式也可以直接验证：$W'=y_1y_2''-y_1''y_2=-p_1(y_1y_2'-y_1'y_2)$。

### 9.1.3. 由基本解组确定方程

反过来，线性无关的函数组决定唯一的齐次线性方程。

**命题 9.1.1** 设 $y_1,\dots,y_n\in C^n(I)$ 且 $W[y_1,\dots,y_n]$ 在 $I$ 上处处不为零，则以 $y_1,\dots,y_n$ 为基本解组、首项系数为 1 的 $n$ 阶线性方程是唯一的，为

$$
\frac{W[y_1,\dots,y_n,y](x)}{W[y_1,\dots,y_n](x)}=0,
$$
其中 $W[y_1,\dots,y_n,y]$ 是 $n+1$ 个函数的 Wronski 行列式。特别地 $p_1=-W'/W$。

**证明** 按最后一列展开，$W[y_1,\dots,y_n,y]=W\cdot y^{(n)}+(\text{低阶导数的线性组合})$，所以左边是首项系数为 1 的 $n$ 阶线性微分算子作用于 $y$；系数连续。$y=y_k$ 时行列式有两列相同，等于零，所以 $y_k$ 都是解。唯一性：若两个这样的方程 $L_1(y)=0$、$L_2(y)=0$ 有同一基本解组，则 $L_1-L_2$ 是至多 $n-1$ 阶的算子，有 $n$ 个线性无关的解；若它不是零算子，设其阶数为 $m<n$、首项系数在某点 $x_1$ 非零，在 $x_1$ 附近它的解空间只有 $m$ 维，矛盾。$p_1=-W'/W$ 由 Liouville 公式得到。 $\square$

**例 9.1.1** 以 $x$ 与 $\mathrm{e}^x$ 为基本解组（在 $x\ne1$ 的区间上，$W=(x-1)\mathrm{e}^x\ne0$）的方程为

$$
\frac{1}{(x-1)\mathrm{e}^x}\begin{vmatrix}x&\mathrm{e}^x&y\\1&\mathrm{e}^x&y'\\0&\mathrm{e}^x&y''\end{vmatrix}=0,\qquad\text{即}\qquad y''-\frac{x}{x-1}y'+\frac{1}{x-1}y=0,
$$
也就是 $(x-1)y''-xy'+y=0$（[2.2.16 的例 16.1.2](/2.2.16#ex-16.1.2)）。

## 9.2. 常数变易公式与 Cauchy 核

### 9.2.1. 余子式形式的常数变易公式

对方程组 (9.3) 应用定理 8.3.1，并取第一个分量，就得到 $n$ 阶方程的特解公式。

**定理 9.2.1** 设 $y_1,\dots,y_n$ 是 (9.2) 的基本解组，$W(x)$ 是它们的 Wronski 行列式，$W_k(x)$ 是把 $W(x)$ 的第 $k$ 列换成 $(0,\dots,0,1)^{\mathsf T}$ 所得的行列式（即 $W$ 中第 $n$ 行第 $k$ 列元素的代数余子式）。则

$$
y^*(x)=\int_{x_0}^x\sum_{k=1}^n\frac{y_k(x)W_k(t)}{W(t)}f(t)\,\mathrm{d}t\tag{9.4}
$$
是 (9.1) 的解，并且满足 $y^*(x_0)=(y^*)'(x_0)=\cdots=(y^*)^{(n-1)}(x_0)=0$。(9.1) 的通解为 $y=C_1y_1+\cdots+C_ny_n+y^*$。

**证明** 以 $(y_k,\dots,y_k^{(n-1)})^{\mathsf T}$ 为列的 $\Phi(x)$ 是 (9.3) 的齐次方程组的基解矩阵，$\det\Phi=W$。由定理 8.3.1，方程组 (9.3) 满足 $\boldsymbol{x}(x_0)=\boldsymbol{0}$ 的解为

$$
\boldsymbol{x}(x)=\int_{x_0}^x\Phi(x)\Phi^{-1}(t)\boldsymbol{e}_nf(t)\,\mathrm{d}t.
$$
由**伴随矩阵**公式 $\Phi^{-1}=\frac{1}{W}\operatorname{adj}\Phi$，$\Phi^{-1}(t)\boldsymbol{e}_n$ 是 $\operatorname{adj}\Phi(t)$ 的第 $n$ 列除以 $W(t)$，它的第 $k$ 个分量是 $\Phi(t)$ 中 $(n,k)$ 元素的代数余子式除以 $W(t)$，即 $W_k(t)/W(t)$。$\boldsymbol{x}(x)$ 的第一个分量是 $\Phi(x)$ 的第一行 $(y_1(x),\dots,y_n(x))$ 乘以这个向量，得 (9.4)。$\boldsymbol{x}(x_0)=\boldsymbol{0}$ 就是关于 $y^*$ 及其导数的初始条件。 $\square$

这就是 [2.2.16 的算法 16.2.1](/2.2.16#alg-16.2.1) 的一般形式：那里由 Cramer 法则解出的 $C_k'$ 正是 $W_kf/W$。$n=3$ 时

$$
W_1=\begin{vmatrix}0&y_2&y_3\\0&y_2'&y_3'\\1&y_2''&y_3''\end{vmatrix},\qquad W_2=\begin{vmatrix}y_1&0&y_3\\y_1'&0&y_3'\\y_1''&1&y_3''\end{vmatrix},\qquad W_3=\begin{vmatrix}y_1&y_2&0\\y_1'&y_2'&0\\y_1''&y_2''&1\end{vmatrix}.
$$

### 9.2.2. Cauchy 核

**定义 9.2.1（Cauchy 核）** 设 $y_1,\dots,y_n$ 是 (9.2) 的基本解组，称

$$
K(x,t)=\sum_{k=1}^n\frac{y_k(x)W_k(t)}{W(t)}=\frac{1}{W(t)}\begin{vmatrix}y_1(t)&\cdots&y_n(t)\\\vdots&&\vdots\\y_1^{(n-2)}(t)&\cdots&y_n^{(n-2)}(t)\\y_1(x)&\cdots&y_n(x)\end{vmatrix}\qquad(x,t\in I)
$$
为方程 (9.2) 的 **Cauchy 核**（Cauchy 函数）。

第二个等号：把 $W(t)$ 的最后一行换成 $(y_1(x),\dots,y_n(x))$，按最后一行展开，系数恰好是 $W_k(t)$。

**定理 9.2.2** 

1. 对固定的 $t\in I$，$K(x,t)$ 作为 $x$ 的函数是 (9.2) 满足初始条件

$$
K(t,t)=\partial_xK(t,t)=\cdots=\partial_x^{n-2}K(t,t)=0,\qquad\partial_x^{n-1}K(t,t)=1
$$
的解。因此 $K$ 与基本解组的选取无关。

2. (9.1) 满足 $y(x_0)=\cdots=y^{(n-1)}(x_0)=0$ 的解为

$$
y^*(x)=\int_{x_0}^xK(x,t)f(t)\,\mathrm{d}t.\tag{9.5}
$$

**证明** 1：$K(x,t)$ 是 $y_1(x),\dots,y_n(x)$ 的常系数（依赖于 $t$）线性组合，所以是解。$\partial_x^jK(x,t)$ 在 $x=t$ 处的值是把行列式最后一行换成 $(y_1^{(j)}(t),\dots,y_n^{(j)}(t))$：$j\le n-2$ 时与前面某行相同，为 $0$；$j=n-1$ 时就是 $W(t)$，商为 $1$。由唯一性，满足这组初始条件的解只有一个。2 是 (9.4)。 $\square$

所以 $K(x,t)$ 是"在时刻 $t$ 给第 $n-1$ 阶导数一个单位冲量"所产生的响应，(9.5) 把非齐次项看作这些冲量的叠加。这与上一章的 $R(t,s)=\Phi(t)\Phi^{-1}(s)$ 是同一个对象：$K(x,t)$ 就是 $R(x,t)$ 的 $(1,n)$ 元素。

$n=2$ 时

$$
K(x,t)=\frac{1}{W(t)}\begin{vmatrix}y_1(t)&y_2(t)\\y_1(x)&y_2(x)\end{vmatrix}=\frac{y_1(t)y_2(x)-y_1(x)y_2(t)}{y_1(t)y_2'(t)-y_1'(t)y_2(t)},
$$
由 Liouville 公式，分母可以换成 $W(x_0)\exp\big(-\int_{x_0}^tp_1\big)$，于是只需在一点算 Wronski 行列式：

$$
y^*(x)=\frac{1}{W(x_0)}\int_{x_0}^x\big(y_1(t)y_2(x)-y_1(x)y_2(t)\big)\,\mathrm{e}^{\int_{x_0}^tp_1(s)\,\mathrm{d}s}f(t)\,\mathrm{d}t.
$$

**例 9.2.1** 解 $x^2y''-2xy'+2y=x^3$（$x>0$）。标准形式为 $y''-\frac2xy'+\frac2{x^2}y=x$。齐次方程是 Euler 方程，有解 $y_1=x$，$y_2=x^2$，$W(t)=t^2$，

$$
K(x,t)=\frac{tx^2-t^2x}{t^2}=\frac{x^2}{t}-x,\qquad y^*=\int_1^x\Big(\frac{x^2}{t}-x\Big)t\,\mathrm{d}t=\frac{x^3}{2}-x^2+\frac{x}{2}.
$$
去掉齐次解，特解可取 $\frac{x^3}{2}$，通解 $y=C_1x+C_2x^2+\frac{x^3}{2}$。

### 9.2.3. 常系数方程的 Cauchy 核

常系数方程有时间平移不变性，$K(x,t)$ 只依赖于 $x-t$：$K(x,t)=k(x-t)$，其中 $k$ 是齐次方程满足 $k(0)=\cdots=k^{(n-2)}(0)=0$、$k^{(n-1)}(0)=1$ 的解（$k(x-t)$ 作为 $x$ 的函数满足定理 9.2.2 第 1 条的条件）。于是 (9.5) 成为卷积

$$
y^*(x)=\int_{x_0}^xk(x-t)f(t)\,\mathrm{d}t.
$$
对二阶方程 $y''+ay'+by=f$，设特征根为 $\lambda_1,\lambda_2$：

| 特征根 | $k(s)$ | 特解 $y^*(x)$ |
|---|---|---|
| 实根 $\lambda_1\ne\lambda_2$ | $\dfrac{\mathrm{e}^{\lambda_2s}-\mathrm{e}^{\lambda_1s}}{\lambda_2-\lambda_1}$ | $\displaystyle\int_{x_0}^x\frac{\mathrm{e}^{\lambda_2(x-t)}-\mathrm{e}^{\lambda_1(x-t)}}{\lambda_2-\lambda_1}f(t)\,\mathrm{d}t$ |
| 重根 $\lambda$ | $s\,\mathrm{e}^{\lambda s}$ | $\displaystyle\int_{x_0}^x(x-t)\mathrm{e}^{\lambda(x-t)}f(t)\,\mathrm{d}t$ |
| 复根 $\alpha\pm\mathrm{i}\beta$ | $\dfrac{\mathrm{e}^{\alpha s}\sin\beta s}{\beta}$ | $\displaystyle\int_{x_0}^x\frac{\mathrm{e}^{\alpha(x-t)}\sin\beta(x-t)}{\beta}f(t)\,\mathrm{d}t$ |

特别地，$y''+n^2y=f$（$n>0$）的特解为

$$
y^*(x)=\frac1n\int_{x_0}^x\sin n(x-t)f(t)\,\mathrm{d}t=\frac{\sin nx}{n}\int_{x_0}^x\cos nt\,f(t)\,\mathrm{d}t-\frac{\cos nx}{n}\int_{x_0}^x\sin nt\,f(t)\,\mathrm{d}t.
$$

**例 9.2.2** 解 $y''-2y'+y=\dfrac{\mathrm{e}^x}{x}$（$x>0$）。$1$ 是二重根，$k(s)=s\mathrm{e}^s$，

$$
y^*=\int_1^x(x-t)\mathrm{e}^{x-t}\frac{\mathrm{e}^t}{t}\,\mathrm{d}t=\mathrm{e}^x\int_1^x\Big(\frac xt-1\Big)\mathrm{d}t=\mathrm{e}^x(x\ln x-x+1).
$$
去掉齐次解 $(1-x)\mathrm{e}^x$，通解 $y=(C_1+C_2x)\mathrm{e}^x+x\mathrm{e}^x\ln x$。待定系数法对这个右端不适用，而核公式没有限制。

## 9.3. 已知部分解时的降阶

### 9.3.1. 二阶方程

设 $\varphi$ 是 $y''+p(x)y'+q(x)y=0$ 在 $I$ 上的一个非零解（且在所考虑的区间上 $\varphi\ne0$）。与 $\varphi$ 线性无关的解 $y$ 可以直接由 Liouville 公式求出：$W[\varphi,y]=\varphi y'-\varphi'y=W(x_0)\mathrm{e}^{-\int_{x_0}^xp}$ 是 $y$ 的一阶线性方程，两边除以 $\varphi^2$ 得

$$
\Big(\frac{y}{\varphi}\Big)'=\frac{W(x_0)}{\varphi^2(x)}\mathrm{e}^{-\int_{x_0}^xp(t)\,\mathrm{d}t}.
$$
积分得 $y=\varphi\Big(\dfrac{y(x_0)}{\varphi(x_0)}+W(x_0)\displaystyle\int_{x_0}^x\frac{\mathrm{e}^{-\int_{x_0}^tp(s)\,\mathrm{d}s}}{\varphi^2(t)}\,\mathrm{d}t\Big)$，这给出了全部解。取 $y(x_0)=0$、$W(x_0)=1$：

**命题 9.3.1** 若 $\varphi$ 是 $y''+py'+qy=0$ 的一个处处非零的解，则

$$
\psi(x)=\varphi(x)\int_{x_0}^x\frac{1}{\varphi^2(t)}\exp\Big(-\int_{x_0}^tp(s)\,\mathrm{d}s\Big)\mathrm{d}t\tag{9.6}
$$
是与 $\varphi$ 线性无关的解，通解为 $y=C_1\varphi+C_2\psi$；$W[\varphi,\psi](x_0)=1$。

这与 [2.2.16 的 16.2.1 节](/2.2.16#sec-16.2.1)令 $y=\varphi z$ 降阶的结果相同。有了 $\varphi,\psi$，非齐次方程的特解由定义 9.2.1 中的核给出，所以已知一个齐次解就能解出非齐次方程。

**例 9.3.1** 求解下列各题。（1）$y''+py'+\frac{p^2}{4}y=0$（$p$ 为实常数）：$\varphi=\mathrm{e}^{\lambda x}$，$\lambda=-\frac p2$。由 (9.6)（$x_0=0$），被积函数为 $\mathrm{e}^{-2\lambda t}\mathrm{e}^{-pt}=1$，$\psi=x\mathrm{e}^{\lambda x}$。这就是常系数方程重根时 $x\mathrm{e}^{\lambda x}$ 的来源。

（2）Euler 方程 $x^2y''+pxy'+\frac{(p-1)^2}{4}y=0$（$x>0$）：设 $y=x^\lambda$ 得 $\lambda^2+(p-1)\lambda+\frac{(p-1)^2}{4}=0$，二重根 $\lambda=\frac{1-p}{2}$。标准形式中 $p(x)=\frac px$，取 $x_0=1$，由 $2\lambda+p=1$，

$$
\psi=x^\lambda\int_1^x\frac{t^{-p}}{t^{2\lambda}}\,\mathrm{d}t=x^\lambda\int_1^x\frac{\mathrm{d}t}{t}=x^\lambda\ln x.
$$
这就是 Euler 方程重根时 $x^\lambda\ln x$ 的来源。

### 9.3.2. $n$ 阶方程

设 $\varphi$ 是 (9.2) 的一个处处非零的解。令 $y=\varphi z$，由 Leibniz 公式 $y^{(k)}=\sum_{j=0}^k\binom kj\varphi^{(j)}z^{(k-j)}$，代入 (9.2)。$z$ 本身的系数是 $L(\varphi)=0$，所以 $z$ 不出现，除以 $\varphi$ 后得

$$
z^{(n)}+P_1(x)z^{(n-1)}+\cdots+P_{n-1}(x)z'=0,\qquad P_1=p_1+n\frac{\varphi'}{\varphi},\quad P_2=p_2+(n-1)p_1\frac{\varphi'}{\varphi}+\binom n2\frac{\varphi''}{\varphi},\quad\dots
$$
再令 $u=z'$，就得到 $u$ 的 $n-1$ 阶线性齐次方程。若 $u_1,\dots,u_{n-1}$ 是它的基本解组，则 $\varphi,\ \varphi\int u_1,\ \dots,\ \varphi\int u_{n-1}$ 是 (9.2) 的基本解组。一般地，已知 $k$ 个线性无关的解，可以把方程降低 $k$ 阶（每降一阶，已知解的个数减少一个：$y_j=\varphi z_j$ 给出 $u$-方程的解 $(y_j/\varphi)'$）。

三阶方程 $y'''+py''+qy'+ry=0$ 的情形：

$$
u''+\Big(\frac{3\varphi'}{\varphi}+p\Big)u'+\Big(\frac{3\varphi''}{\varphi}+\frac{2p\varphi'}{\varphi}+q\Big)u=0.
$$

**例 9.3.2** $x^3y'''-3x^2y''+6xy'-6y=0$（$x>0$）有解 $\varphi=x$。标准形式 $p=-\frac3x$，$q=\frac{6}{x^2}$，代入上式：$u'$ 的系数为 $\frac3x-\frac3x=0$，$u$ 的系数为 $0+2\cdot(-\frac3x)\cdot\frac1x+\frac{6}{x^2}=0$。所以 $u''=0$，$u=c_1+c_2x$，$z=c_1x+\frac{c_2}2x^2+c_3$，

$$
y=\varphi z=C_1x+C_2x^2+C_3x^3.
$$
（这是 Euler 方程，指标方程 $(\lambda-1)(\lambda-2)(\lambda-3)=0$，见 9.5 节。）

## 9.4. 常系数方程

常系数方程 $y^{(n)}+a_1y^{(n-1)}+\cdots+a_ny=0$ 对应的方程组 (9.3) 是常系数的，系数矩阵是友矩阵 $C$，它的**特征多项式**就是 $P(\lambda)=\lambda^n+a_1\lambda^{n-1}+\cdots+a_n$（[2.1.6](/2.1.6)）。上一章的推论 8.5.1 说明解是 $p_j(x)\mathrm{e}^{\lambda_jx}$ 之和，多项式 $p_j$ 的次数由 $\lambda_j$ 的 Jordan 块的阶数控制。对友矩阵，这个阶数恰好等于代数重数：

**命题 9.4.1** 友矩阵的每个**特征值**的几何重数都是 1，因而每个特征值只对应一个 Jordan 块，其阶数等于该特征值作为**特征根**的重数。

**证明** 删去 $C-\lambda I$ 的第一列和最后一行，剩下的 $n-1$ 阶子式是对角线为 1 的下三角形（上次对角线的 1 移到了对角线上），等于 $1$。所以 $\operatorname{rank}(C-\lambda I)\ge n-1$，特征子空间至多一维。 $\square$

因此 $m$ 重特征根 $\lambda$ 恰好贡献 $\mathrm{e}^{\lambda x},x\mathrm{e}^{\lambda x},\dots,x^{m-1}\mathrm{e}^{\lambda x}$，这就是 [2.2.16 的定理 16.3.1](/2.2.16#thm-16.3.1) 的结构上的原因。友矩阵关于 $\lambda$ 的特征向量是 $(1,\lambda,\dots,\lambda^{n-1})^{\mathsf T}$，对应解 $\mathrm{e}^{\lambda x}$。

求解的具体方法（**特征方程**、待定系数法、**微分算子法**）见 [2.2.16 的 16.3、16.4 节](/2.2.16#sec-16.3)；非齐次项不是指数型函数时用 9.2.3 节的核公式。解在 $x\to+\infty$ 时的有界性与趋于零的条件见 [2.4.11](/2.4.11)。

## 9.5. Euler 方程

**定义 9.5.1（Euler 方程）** 形如

$$
x^ny^{(n)}+a_1x^{n-1}y^{(n-1)}+\cdots+a_{n-1}xy'+a_ny=f(x)\qquad(a_k\text{ 为实常数})\tag{9.7}
$$
的方程称为 **Euler 方程**。

$x=0$ 是系数的奇点，以下在 $x>0$ 上讨论（$x<0$ 时令 $x=-\mathrm{e}^t$，结果中的 $x$ 换成 $\lvert x\rvert$）。令 $x=\mathrm{e}^t$，$\mathrm{D}=\frac{\mathrm{d}}{\mathrm{d}t}$，则

$$
x\frac{\mathrm{d}y}{\mathrm{d}x}=\mathrm{D}y,\qquad x^2\frac{\mathrm{d}^2y}{\mathrm{d}x^2}=\mathrm{D}(\mathrm{D}-1)y,\qquad\dots,\qquad x^k\frac{\mathrm{d}^ky}{\mathrm{d}x^k}=\mathrm{D}(\mathrm{D}-1)\cdots(\mathrm{D}-k+1)y,
$$
（归纳证明见 [2.2.16 的命题 16.4.2](/2.2.16#prop-16.4.2)），(9.7) 化为常系数方程。由此，齐次 Euler 方程有形如 $y=\mathrm{e}^{\lambda t}=x^\lambda$ 的解，可以直接代入：$x^ky^{(k)}=\lambda(\lambda-1)\cdots(\lambda-k+1)x^\lambda$，得到

$$
F(\lambda)=\lambda(\lambda-1)\cdots(\lambda-n+1)+a_1\lambda(\lambda-1)\cdots(\lambda-n+2)+\cdots+a_{n-1}\lambda+a_n=0.\tag{9.8}
$$

**定理 9.5.1** 设 $F(\lambda)=0$ 的实根 $\lambda_0$ 是 $m$ 重根，复根对 $\alpha\pm\mathrm{i}\beta$（$\beta>0$）是 $m$ 重根。它们分别对应齐次 Euler 方程在 $x>0$ 上的 $m$ 个与 $2m$ 个实解

$$
x^{\lambda_0},\ x^{\lambda_0}\ln x,\ \dots,\ x^{\lambda_0}\ln^{m-1}x;
$$

$$
x^\alpha\ln^jx\cos(\beta\ln x),\quad x^\alpha\ln^jx\sin(\beta\ln x),\qquad j=0,1,\dots,m-1,
$$
全部根对应的 $n$ 个函数构成基本解组。

**证明** 令 $x=\mathrm{e}^t$ 后得到特征多项式为 $F$ 的常系数方程，由 [2.2.16 的定理 16.3.1](/2.2.16#thm-16.3.1)，$t^j\mathrm{e}^{\lambda_0t}$ 与 $t^j\mathrm{e}^{\alpha t}\cos\beta t$、$t^j\mathrm{e}^{\alpha t}\sin\beta t$ 构成它的基本解组，代回 $t=\ln x$。 $\square$

**例 9.5.1** 求解下列各题。（1）$x^2y''-xy'+y=0$：$F(\lambda)=\lambda(\lambda-1)-\lambda+1=(\lambda-1)^2$，通解 $y=(C_1+C_2\ln x)x$。

（2）$x^2y''+3xy'+5y=0$：$F(\lambda)=\lambda^2+2\lambda+5$，根 $-1\pm2\mathrm{i}$，通解 $y=\dfrac1x\big(C_1\cos(2\ln x)+C_2\sin(2\ln x)\big)$。

非齐次 Euler 方程化为常系数方程后用 9.2.3 节的核公式或待定系数法求解（[2.2.16 的例 16.4.10](/2.2.16#ex-16.4.10)）。Euler 方程是下一章正则奇点理论的原型：指标方程就是 (9.8) 的二阶情形。

## 9.6. $y''+M^2y=f$ 的周期解

设 $f$ 是 $\mathbb{R}$ 上连续的 $T$ 周期函数（$T>0$），$M>0$。考虑

$$
y''+M^2y=f(x),\qquad x\in\mathbb{R}.\tag{9.9}
$$
它描述受周期外力作用的无阻尼振子。问题是：什么时候有周期为 $T$ 的解？

**定理 9.6.1（9.9）** 的解 $y$ 是 $T$ 周期函数，当且仅当 $y(0)=y(T)$ 且 $y'(0)=y'(T)$。

**证明** 必要性显然。充分性：由 $f(x+T)=f(x)$，$y(x+T)$ 也是 (9.9) 的解。令 $z(x)=y(x+T)-y(x)$，则 $z''+M^2z=f(x+T)-f(x)=0$，且 $z(0)=z'(0)=0$。由定理 9.1.1 的唯一性 $z\equiv0$，即 $y(x+T)\equiv y(x)$。 $\square$

证明只用到了方程的线性与系数的周期性，所以对系数为 $T$ 周期函数的任意线性方程组同样成立：解是 $T$ 周期的当且仅当 $\boldsymbol{x}(0)=\boldsymbol{x}(T)$。

**定理 9.6.2** 

1. （非共振）若 $MT\notin2\pi\mathbb{Z}$，则 (9.9) 有唯一的 $T$ 周期解；
2. （共振）若 $MT=2\pi k$（$k$ 为正整数），则 (9.9) 有 $T$ 周期解当且仅当

$$
\int_0^Tf(t)\cos Mt\,\mathrm{d}t=\int_0^Tf(t)\sin Mt\,\mathrm{d}t=0,
$$
此时 (9.9) 的所有解都是 $T$ 周期的；否则所有解都无界。

**证明** 通解为 $y=c_1\cos Mx+c_2\sin Mx+y^*(x)$，$y^*(x)=\frac1M\int_0^x\sin M(x-t)f(t)\,\mathrm{d}t$，$y^*(0)=(y^*)'(0)=0$。由定理 9.6.1，$y$ 是 $T$ 周期的当且仅当

$$
\begin{cases}c_1(\cos MT-1)+c_2\sin MT=-y^*(T),\\-c_1M\sin MT+c_2M(\cos MT-1)=-(y^*)'(T).\end{cases}
$$
系数行列式为 $M\big((\cos MT-1)^2+\sin^2MT\big)=2M(1-\cos MT)$。

1：$MT\notin2\pi\mathbb{Z}$ 时行列式非零，$(c_1,c_2)$ 唯一存在。

2：$MT=2\pi k$ 时系数全为零，方程组可解当且仅当 $y^*(T)=(y^*)'(T)=0$。由 $\sin M(T-t)=-\sin Mt$，$\cos M(T-t)=\cos Mt$，

$$
y^*(T)=-\frac1M\int_0^T\sin Mt\,f(t)\,\mathrm{d}t,\qquad(y^*)'(T)=\int_0^T\cos M(T-t)f(t)\,\mathrm{d}t=\int_0^T\cos Mt\,f(t)\,\mathrm{d}t,
$$
得到所述条件，此时每一组 $(c_1,c_2)$ 都满足方程组。若条件不成立，记 $\boldsymbol{d}=(y(T)-y(0),y'(T)-y'(0))$，它与 $c_1,c_2$ 无关且不为零；$z(x)=y(x+T)-y(x)$ 是齐次方程的解，满足 $(z(0),z'(0))=\boldsymbol{d}$，它是周期为 $T$ 的非零函数，于是 $y(x+jT)=y(x)+\sum_{i<j}z(x+iT)=y(x)+jz(x)$ 无界。 $\square$

条件 2 的意义：把 $f$ 展开为 Fourier 级数，$\cos Mt$、$\sin Mt$ 正是频率等于固有频率 $M$ 的那一项。外力中含有固有频率的分量时发生**共振**（[2.2.16 的 16.5.2 节](/2.2.16#sec-16.5.2)），振幅线性增长；不含这一分量时，即使 $MT\in2\pi\mathbb{Z}$ 也没有共振。

**例 9.6.1** 求解下列各题。（1）$y''+2y=\cos x$，$T=2\pi$，$M=\sqrt2$，$MT\notin2\pi\mathbb{Z}$：唯一的 $2\pi$ 周期解是 $\cos x$。其余的解是它加上 $c_1\cos\sqrt2x+c_2\sin\sqrt2x$，是概周期的而不是周期的。

（2）$y''+y=\cos x$，$T=2\pi$，$M=1$：$\int_0^{2\pi}\cos^2t\,\mathrm{d}t=\pi\ne0$，没有周期解。通解 $y=c_1\cos x+c_2\sin x+\frac x2\sin x$，振幅线性增长。

（3）$y''+4y=\sin x$，$T=2\pi$，$M=2$：$\int_0^{2\pi}\sin t\cos2t\,\mathrm{d}t=\int_0^{2\pi}\sin t\sin2t\,\mathrm{d}t=0$，所有解 $y=c_1\cos2x+c_2\sin2x+\frac13\sin x$ 都是 $2\pi$ 周期的。

![y'' + M^2 y = f 的解（初值都取 y(0) = y'(0) = 0 与另一组初值）：左，非共振 y'' + 2y = cos x，解在唯一的 2π 周期解 cos x（粗线）附近振荡而不周期；中，共振 y'' + y = cos x，振幅线性增长；右，y'' + 4y = sin x，虽然 MT ∈ 2πZ，外力不含固有频率，所有解都是 2π 周期的](./plots/periodic-forcing.py)

## 小结

| 主题 | 结论 |
|---|---|
| 化为方程组 | $\boldsymbol{x}=(y,\dots,y^{(n-1)})^{\mathsf T}$，系数矩阵为友矩阵，$\operatorname{tr}=-p_1$ |
| 解的结构 | 解空间 $n$ 维；$n$ 个解无关 $\Leftrightarrow$ $W$ 在一点非零；$W(x)=W(x_0)\mathrm{e}^{-\int_{x_0}^xp_1}$ |
| 方程由解确定 | $W[y_1,\dots,y_n,y]/W[y_1,\dots,y_n]=0$（命题 9.1.1） |
| 常数变易公式 | $y^*=\int_{x_0}^x\sum_ky_k(x)W_k(t)f(t)/W(t)\,\mathrm{d}t$，$W_k$ 为第 $n$ 行的代数余子式 |
| Cauchy 核 | $K(\cdot,t)$ 是满足 $\partial_x^jK(t,t)=\delta_{j,n-1}$ 的齐次解；常系数时 $K=k(x-t)$，特解为卷积 |
| 降阶 | 二阶：$\psi=\varphi\int\varphi^{-2}\mathrm{e}^{-\int p}$；$n$ 阶：$y=\varphi z$，$u=z'$ 降一阶 |
| 常系数方程 | 友矩阵每个特征值只有一个 Jordan 块，$m$ 重根给出 $x^j\mathrm{e}^{\lambda x}$（$j<m$） |
| Euler 方程 | $y=x^\lambda$，$F(\lambda)=0$；$m$ 重根给出 $x^\lambda\ln^jx$ |
| 周期解 | $T$ 周期 $\Leftrightarrow$ $\boldsymbol{x}(0)=\boldsymbol{x}(T)$；$MT\notin2\pi\mathbb{Z}$ 时唯一；共振时需 $f$ 与 $\cos Mt$、$\sin Mt$ 正交 |
