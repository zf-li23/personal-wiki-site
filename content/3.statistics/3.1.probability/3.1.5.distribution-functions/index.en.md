---
title: Distribution Functions and Functions of Random Variables
description: The distribution function, its relation to the probability mass function and the density, its characteristic properties (monotone, limits at infinity, right-continuous) and how it determines the type of a random variable; the standard normal distribution function and the 3σ rule, geometric versus exponential distributions, mixed and singular distributions; distributions of functions of discrete and continuous random variables, with density formulas for monotone and general transformations.
source_hash: 17248cad7cd4
---

In [3.1.4](/3.1.4) discrete random variables were described by probability mass functions and continuous ones by densities, but each tool has a limited range: some random variables are neither discrete nor continuous. This chapter introduces the distribution function $F(x)=\mathbb{P}(X\le x)$, which applies to every random variable. It determines the distribution completely, places discrete and continuous distributions in a common framework (so that, for instance, the geometric and exponential distributions can be compared directly), and tells us which type a random variable is. The second half of the chapter treats the distribution of a function $Y=g(X)$: the general method is to compute the distribution function of $Y$ and then differentiate, and for monotone or piecewise monotone $g$ there are formulas that pass directly from the density of $X$ to that of $Y$. These methods are extended to random vectors and their functions in [3.1.6](/3.1.6) and [3.1.7](/3.1.7).

## 5.1. Distribution Functions

### 5.1.1. Definition and Relation to Mass Functions and Densities

Our goal is to capture all the information carried by a random variable. Of the tools available so far, the probability mass function applies only to discrete random variables and the density only to continuous ones. Recall the requirement in the definition of a random variable: $\{X\le x\}$ is an event for every $x\in\mathbb{R}$. Hence $\mathbb{P}(X\le x)$ makes sense for every random variable.

**Definition 5.1.1 (Distribution Function)** For a random variable $X$, the function of $x$

$$
F(x)=\mathbb{P}(X\le x),\qquad x\in\mathbb{R}
$$
is called the probability distribution function or cumulative distribution function (CDF) of $X$, or simply its **distribution function**. When several random variables are involved we write $F_X$.

The distribution function gives the probability that $X$ falls in any interval, for example $\mathbb{P}(a<X\le b)=F(b)-F(a)$ and $\mathbb{P}(X>a)=1-F(a)$. Measure theory shows further that $F$ determines $\mathbb{P}(X\in A)$ for every Borel set $A$, so the distribution function describes the distribution of $X$ completely. Two random variables are identically distributed precisely when their distribution functions coincide.

For a discrete random variable $X$ with probability mass function $p_k=\mathbb{P}(X=x_k)$, $k=1,2,\dots$,

$$
F(x)=\mathbb{P}(X\le x)=\mathbb{P}\Big(\bigcup_{j\colon x_j\le x}\{X=x_j\}\Big)=\sum_{j\colon x_j\le x}p_j.
$$
Thus $F$ is a nondecreasing step function with a jump of size $p_j$ at each $x_j$; we call it the distribution function of the mass function $\{p_j\}$. For instance, if $\mathbb{P}(X=1)=0.2$ and $\mathbb{P}(X=2)=0.5$, then $F(1.5)=0.2$; conversely, $F$ recovers $\mathbb{P}(X=2)=F(2)-F(2-)=0.5$, where $F(x-)=\lim_{t\uparrow x}F(t)$ denotes the left limit. If $\{x_k\}$ is increasing, then $p_k=F(x_k)-F(x_{k-1})$. With the Heaviside function $H(x)=\boldsymbol{1}_{[0,\infty)}(x)$ we can write

$$
F(x)=\sum_{k=1}^\infty p_kH(x-x_k).\tag{5.1}
$$
A distribution function that can be written in the form (5.1) is called discrete.

For a continuous random variable $X$ with density $f$,

$$
F(x)=\mathbb{P}(X\le x)=\int_{-\infty}^xf(t)\,\mathrm{d}t,\qquad x\in\mathbb{R}
$$
is a continuous function, and $F'(x)=f(x)$ at every point $x$ where $f$ is continuous (the **fundamental theorem of calculus**); we call $F$ the distribution function of $f$. For example, the distribution function of $\mathrm{U}(a,b)$ equals $\frac{x-a}{b-a}$ on $(a,b)$, $0$ for $x\le a$ and $1$ for $x\ge b$. The mass function and the distribution function determine each other; the density determines the distribution function, but the distribution function determines the density only "almost": the value of a density may be changed arbitrarily at isolated points.

**Example 5.1.1 (Standard Normal Distribution Function)** The distribution function of the standard normal distribution is denoted by

$$
\Phi(x)=\int_{-\infty}^x\varphi(t)\,\mathrm{d}t=\int_{-\infty}^x\frac1{\sqrt{2\pi}}\mathrm{e}^{-t^2/2}\,\mathrm{d}t.
$$
It has no expression in elementary functions, and its values are read from a standard normal table (for example $\Phi(0.84)=0.7995$). By the symmetry of $\varphi$, $\Phi(x)+\Phi(-x)=1$, that is, $\Phi(-x)=1-\Phi(x)$, so tables list only $x\ge0$. For a general normal variable $X\sim\mathcal{N}(\mu,\sigma^2)$ the substitution $y=(x-\mu)/\sigma$ gives

$$
\mathbb{P}(X\le a)=\frac1{\sigma\sqrt{2\pi}}\int_{-\infty}^a\exp\Big\{-\frac{(x-\mu)^2}{2\sigma^2}\Big\}\,\mathrm{d}x=\frac1{\sqrt{2\pi}}\int_{-\infty}^{(a-\mu)/\sigma}\mathrm{e}^{-y^2/2}\,\mathrm{d}y=\Phi\Big(\frac{a-\mu}\sigma\Big).
$$
Consequently

$$
\begin{aligned}
\mathbb{P}(\lvert X-\mu\rvert\le\sigma)&=2\Phi(1)-1=68.27\%,\\
\mathbb{P}(\lvert X-\mu\rvert\le2\sigma)&=2\Phi(2)-1=95.45\%,\\
\mathbb{P}(\lvert X-\mu\rvert\le3\sigma)&=2\Phi(3)-1=99.73\%,\\
\mathbb{P}(\lvert X-\mu\rvert\le6\sigma)&=2\Phi(6)-1=99.9999998\%.
\end{aligned}
$$
A normal random variable almost always lies within $\mu\pm3\sigma$. The $3\sigma$ and $6\sigma$ rules of quality management require that the conformance rate of a product, the reliability of a performance characteristic or the satisfaction rate of a service reach $\mathbb{P}(\lvert X-\mu\rvert\le3\sigma)$ or $\mathbb{P}(\lvert X-\mu\rvert\le6\sigma)$.

### 5.1.2. What Distribution Functions Can Do

Because distribution functions exist for all random variables, they let us study the relation between discrete and continuous random variables.

**Example 5.1.2 (Geometric and Exponential Distributions)** Let $X_1\sim\mathrm{Geo}(p)$ with $\mathbb{P}(X_1=k)=p(1-p)^{k-1}$, and write $n=\lfloor x\rfloor$. For $x\ge1$,

$$
F_1(x)=F_1(n)=\sum_{k=1}^np(1-p)^{k-1}=p\cdot\frac{1-(1-p)^n}{1-(1-p)}=1-(1-p)^n.
$$
Let $X_2\sim\mathrm{Exp}(\lambda)$; then $F_2(x)=\int_0^x\lambda\mathrm{e}^{-\lambda t}\,\mathrm{d}t=1-\mathrm{e}^{-\lambda x}$ for $x>0$. Put $\delta=-\ln(1-p)/\lambda$, so that $\mathrm{e}^{-\lambda\delta}=1-p$; then $F_1(n)=F_2(n\delta)$ for $n=1,2,\dots$. Think of tossing a coin rapidly, once every $\delta$ seconds, with probability $p$ of heads on each toss: $X_1$ is the number of tosses needed for the first head and $X_1\delta$ is the time at which it occurs. The distribution functions show that for small $\delta$ the distribution of $X_1\delta$ is close to that of $X_2$: the exponential distribution is the limit of the geometric distribution as time becomes continuous.

![Step distribution function of the geometric distribution on the lattice nδ compared with the exponential distribution function 1 − e^(−x), for δ = 0.5 and δ = 0.1](./plots/geometric-exponential.py)

Distribution functions can also describe random variables that are neither discrete nor continuous.

**Example 5.1.3 (A Mixed Random Variable)** Toss a fair coin. On heads you receive 0.5 yuan; on tails you spin a prize wheel and receive an amount distributed as $\mathrm{U}(0,1)$ (in yuan). The amount $X$ received has distribution function

$$
F(x)=\begin{cases}0, & x<0,\\ x/2, & 0\le x<1/2,\\ 1/2+x/2, & 1/2\le x<1,\\ 1, & x\ge1.\end{cases}
$$
$F$ jumps by $1/2$ at $x=1/2$ (so $\mathbb{P}(X=1/2)=1/2$) and increases continuously elsewhere. Such a random variable has neither a mass function nor a density and can only be described by its distribution function.

### 5.1.3. Properties of Distribution Functions

**Theorem 5.1.1 (Properties of Distribution Functions)** The distribution function $F$ of a random variable $X$ satisfies:

1. $F$ is nondecreasing;
2. $F(-\infty)=\lim_{x\to-\infty}F(x)=0$ and $F(\infty)=\lim_{x\to\infty}F(x)=1$;
3. $F$ is right-continuous, that is, $\lim_{t\downarrow x}F(t)=F(x)$ for every $x$.

**Proof** (1) For any $x<y$, $F(y)-F(x)=\mathbb{P}(x<X\le y)\ge0$.

(2) By monotonicity it suffices to take limits along the integers. The events $\{X\le n\}$ increase with union $\{X<\infty\}=\Omega$, so by continuity of probability ([3.1.2](/3.1.2), Theorem 2.2.1)

$$
F(\infty)=\lim_{n\to\infty}\mathbb{P}(X\le n)=\mathbb{P}\Big(\bigcup_{n=1}^\infty\{X\le n\}\Big)=\mathbb{P}(X<\infty)=1.
$$
Likewise, the events $\{X\le-n\}$ decrease with intersection $\varnothing$, so $F(-\infty)=0$.

(3) By monotonicity it suffices to take the limit along $x+n^{-1}$. The events $\{X\le x+n^{-1}\}$ decrease with intersection $\{X\le x\}$, hence

$$
\lim_{n\to\infty}F(x+n^{-1})=\mathbb{P}\Big(\bigcap_{n=1}^\infty\{X\le x+n^{-1}\}\Big)=\mathbb{P}(X\le x)=F(x).\qquad\square
$$

The same argument gives the left limit $F(x-)=\mathbb{P}(X<x)$, so $\mathbb{P}(X=x)=F(x)-F(x-)$ is the jump of $F$ at $x$. Conversely, one can show that every function satisfying (1)–(3) is the distribution function of some random variable, so these three properties characterize distribution functions. Since a monotone function has at most countably many discontinuities, every random variable has at most countably many values that it takes with positive probability.

### 5.1.4. Determining the Type of a Random Variable

**Theorem 5.1.2** If $\mathbb{P}(X=x)=0$ for every $x\in\mathbb{R}$, then the distribution function $F(x)=\mathbb{P}(X\le x)$ is continuous.

**Proof** By continuity of probability,

$$
0=\mathbb{P}(X=x)=\mathbb{P}\Big(\bigcap_{m=1}^\infty\Big\{x-\frac1m<X\le x\Big\}\Big)=\lim_{m\to\infty}\big[F(x)-F(x-m^{-1})\big]=F(x)-F(x-),
$$
so $F$ is left-continuous. Being also right-continuous, $F$ is continuous. $\square$

Hence, if $F$ is discontinuous, $X$ cannot be a continuous random variable (a continuous random variable takes each value with probability zero). Conversely, when $F$ is continuous and differentiable almost everywhere, a density can be obtained from the derivative.

**Theorem 5.1.3** Let the distribution function $F$ of $X$ be continuous, and let $A$ be a set of numbers any two of which are at distance greater than some fixed $\delta>0$. If the derivative $F'(x)$ exists and is continuous on $A^{\mathsf c}$, then

$$
f(x)=\begin{cases}F'(x), & x\notin A,\\ 0, & x\in A\end{cases}
$$
is a density of $X$.

**Proof** For any $a<b$, the interval $(a,b)$ contains only finitely many points of $A$ (consecutive points are more than $\delta$ apart), say $a_1<\cdots<a_k$; put $a_0=a$ and $a_{k+1}=b$. On each $[a_j,a_{j+1}]$, $F$ is continuous and continuously differentiable in the interior, so by the **fundamental theorem of calculus** (the Newton–Leibniz formula, with limits at the endpoints justified by continuity of $F$)

$$
\mathbb{P}(a<X\le b)=\sum_{j=0}^k\big[F(a_{j+1})-F(a_j)\big]=\sum_{j=0}^k\int_{a_j}^{a_{j+1}}f(t)\,\mathrm{d}t=\int_a^bf(t)\,\mathrm{d}t.
$$
Therefore $f$ is a probability density of $X$. $\square$

**Remark 5.1.1** The continuity of $F$ in Theorem 5.1.3 is essential. If $X\sim\mathrm{Bin}(n,p)$, then $F'(x)=0$ except at finitely many points, yet $X$ has no density. On the other hand, continuity of $F$ does not guarantee that $X$ is a continuous random variable, as the next example shows; the example also shows that the restriction on the set $A$ in the theorem cannot be dropped.

**Example 5.1.4 (Cantor Distribution)** The Cantor set $C$ is what remains of $[0,1]$ after removing the open middle third $(1/3,2/3)$, then the open middle third of each remaining interval, and so on indefinitely. Define $F(x)=0$ for $x\le0$ and $F(x)=1$ for $x\ge1$; let $F=1/2$ on the interval $[1/3,2/3]$ removed in the first step, $F=1/4$ and $3/4$ on the intervals $[1/9,2/9]$ and $[7/9,8/9]$ removed in the second step, and, on the $2^{n-1}$ intervals removed in step $n$, the values $\frac1{2^n},\frac3{2^n},\dots,\frac{2^n-1}{2^n}$ from left to right. One can show that $F$ extends to all of $\mathbb{R}$ as a nondecreasing continuous function with $F(-\infty)=0$ and $F(\infty)=1$, so it is a distribution function, called the Cantor function (Lebesgue's singular function). At every point outside $C$ we have $F'(x)=0$, and the total length of $C$ is $1-\sum_{n\ge1}2^{n-1}/3^n=0$, so $F'=0$ almost everywhere. If $X$ had a density $f$, then $f=F'=0$ almost everywhere and $\int f=0\ne1$, a contradiction. A random variable with the Cantor distribution therefore takes each value with probability zero, and yet it is not a continuous random variable.

A distribution function that is continuous, not constant, and differentiable almost everywhere with derivative zero almost everywhere is called singular. One can show that every distribution function decomposes uniquely as a convex combination of a discrete, an absolutely continuous (that is, having a density) and a singular part (the Lebesgue decomposition); elementary probability meets only the first two and their mixtures.

![Four kinds of distribution functions: discrete (a step function), continuous (U(1, 4) and the integral of another density), mixed (Example 5.1.3) and the singular Cantor function](./plots/cdf-types.py)

## 5.2. Distributions of Functions of Random Variables

If $X$ is a random variable and $g$ is a measurable function, then $Y=g(X)$ is also a random variable ([3.1.3](/3.1.3), Theorem 3.2.2). Given the distribution of $X$, how do we find that of $Y$? There are two routes. The general method computes the distribution function of $Y$ from that of $X$ and then obtains the mass function or density of $Y$ from it; in special cases (for instance, monotone $g$) the mass function or density of $Y$ can be written down directly from that of $X$.

### 5.2.1. Functions of Discrete Random Variables

If $X$ is discrete, so is $Y=g(X)$, and it suffices to compute $\mathbb{P}(Y=y)=\sum_{k\colon g(x_k)=y}\mathbb{P}(X=x_k)$ for each possible value $y$ of $Y$: several distinct $x_k$ may be mapped to the same $y$.

**Example 5.2.1** Let $X$ have the distribution

$$
\begin{array}{c|ccccc}
X & -2 & -1 & 0 & 1 & 3\\
\hline
\mathbb{P} & 0.1 & 0.2 & 0.3 & 0.2 & 0.2
\end{array}
$$
and find the distribution of $Y=X^2$. The possible values of $Y$ are $0,1,4,9$, with $\mathbb{P}(Y=0)=\mathbb{P}(X=0)=0.3$, $\mathbb{P}(Y=1)=\mathbb{P}(X=-1)+\mathbb{P}(X=1)=0.4$, $\mathbb{P}(Y=4)=\mathbb{P}(X=-2)=0.1$ and $\mathbb{P}(Y=9)=\mathbb{P}(X=3)=0.2$. The mass function of $Y$ is therefore

$$
\begin{array}{c|cccc}
Y & 0 & 1 & 4 & 9\\
\hline
\mathbb{P} & 0.3 & 0.4 & 0.1 & 0.2
\end{array}
$$

### 5.2.2. Functions of Continuous Random Variables: The Distribution Function Method

Let $X$ have density $f_X$ and consider $Y=g(X)$. The general method has two steps:

1. compute the distribution function $F_Y(y)=\mathbb{P}(Y\le y)=\mathbb{P}(g(X)\le y)=\int_{\{x\colon g(x)\le y\}}f_X(x)\,\mathrm{d}x$;
2. differentiate to get $f_Y(y)=\dfrac{\mathrm{d}F_Y(y)}{\mathrm{d}y}$ (and check with Theorem 5.1.3 that this is indeed a density).

**Example 5.2.2 (Standardization)** If $X\sim\mathcal{N}(\mu,\sigma^2)$, then $Y=(X-\mu)/\sigma\sim\mathcal{N}(0,1)$. Indeed, with $t=(x-\mu)/\sigma$,

$$
\mathbb{P}(Y\le y)=\mathbb{P}(X\le\mu+\sigma y)=\int_{-\infty}^{\mu+\sigma y}\frac1{\sigma\sqrt{2\pi}}\exp\Big\{-\frac{(x-\mu)^2}{2\sigma^2}\Big\}\,\mathrm{d}x=\int_{-\infty}^y\varphi(t)\,\mathrm{d}t=\Phi(y).
$$

**Example 5.2.3** Let $X\sim\mathcal{N}(0,1)$; find the density of $Y=X^2$. Since $Y\ge0$, $F_Y(y)=0$ for $y\le0$; for $y>0$,

$$
F_Y(y)=\mathbb{P}(-\sqrt y\le X\le\sqrt y)=\Phi(\sqrt y)-\Phi(-\sqrt y)=2\Phi(\sqrt y)-1,
$$
which is continuous, and continuously differentiable for $y>0$. By Theorem 5.1.3 the density of $Y$ is

$$
f_Y(y)=F_Y'(y)=2\varphi(\sqrt y)\frac1{2\sqrt y}=\frac1{\sqrt{2\pi y}}\mathrm{e}^{-y/2},\qquad y>0.
$$
Comparing with the densities in [3.1.4](/3.1.4) (and using $\Gamma(1/2)=\sqrt\pi$), we see that $Y\sim\Gamma(1/2,1/2)=\chi^2_1$.

### 5.2.3. Linear and Monotone Transformations

In some special cases $f_Y$ can be obtained directly from $f_X$ without computing distribution functions.

**Theorem 5.2.1 (Linear Transformation)** Let $X$ have density $f_X$, let $a\ne0$, and let $Y=aX+b$. Then

$$
f_Y(y)=\frac1{\lvert a\rvert}f_X\Big(\frac{y-b}a\Big).
$$

**Proof** If $a>0$, $F_Y(y)=\mathbb{P}(X\le(y-b)/a)=F_X((y-b)/a)$; if $a<0$, $F_Y(y)=\mathbb{P}(X\ge(y-b)/a)=1-F_X((y-b)/a)$ (since $X$ takes any single value with probability zero). In both cases, writing $F_X$ as an integral and changing variables gives the result. $\square$

Geometrically, the density of $aX$ stretches the graph of $f_X$ horizontally by the factor $\lvert a\rvert$ (reflecting it when $a<0$) and compresses its height by $1/\lvert a\rvert$, so that the total area remains $1$; adding $b$ shifts it. Theorem 5.2.1 gives Example 5.2.2 again, and also shows that $aX+b\sim\mathcal{N}(a\mu+b,a^2\sigma^2)$ if $X\sim\mathcal{N}(\mu,\sigma^2)$, and $cX\sim\mathrm{Exp}(\lambda/c)$ if $X\sim\mathrm{Exp}(\lambda)$ and $c>0$.

**Theorem 5.2.2 (Strictly Monotone Transformation)** Let $X$ have density $f_X$, let $g$ be strictly monotone and continuously differentiable on the interval $I$ of values of $X$, and let $h$ be the inverse function of $g$. Then $Y=g(X)$ has density

$$
f_Y(y)=f_X\big(h(y)\big)\,\lvert h'(y)\rvert,\qquad y\in g(I),
$$
and $f_Y(y)=0$ outside $g(I)$.

**Proof** If $g$ is strictly increasing, so is $h$, and $F_Y(y)=\mathbb{P}(X\le h(y))=F_X(h(y))$; differentiating gives $f_Y(y)=f_X(h(y))h'(y)$. If $g$ is strictly decreasing, $F_Y(y)=1-F_X(h(y))$, and differentiating gives $f_Y(y)=-f_X(h(y))h'(y)=f_X(h(y))\lvert h'(y)\rvert$. $\square$

Intuitively, the event $\{x<X\le x+\delta\}$ equals $\{g(x)<Y\le g(x+\delta)\}$, and the latter interval has length approximately $\delta\lvert g'(x)\rvert$; hence $\delta f_X(x)\approx\delta f_Y(g(x))\lvert g'(x)\rvert$, so the density changes by the local stretching factor $\lvert g'(x)\rvert$.

### 5.2.4. General Transformations

If $g$ is not monotone, a value $y$ may have several preimages ("many-to-one"). Solve $g(x)=y$ and count the solutions: each solution corresponds to a branch of the inverse, and the contributions of the branches add up. For example, with $g(x)=x^2$ each $y>0$ has the two preimages $x_1=\sqrt y$ and $x_2=-\sqrt y$, so

$$
f_Y(y)=f_X(x_1)\Big\lvert\frac{\mathrm{d}x_1}{\mathrm{d}y}\Big\rvert+f_X(x_2)\Big\lvert\frac{\mathrm{d}x_2}{\mathrm{d}y}\Big\rvert=\frac1{2\sqrt y}\big[f_X(\sqrt y)+f_X(-\sqrt y)\big],
$$
which for $X\sim\mathcal{N}(0,1)$ is the result of Example 5.2.3. In general:

**Theorem 5.2.3** Let $X$ have density $f$, let $Y=g(X)$, and let $D\subset\mathbb{R}$ be an open interval with $\mathbb{P}(Y\in D)=1$. Suppose that

1. $\{Y=y\}=\bigcup_{i=1}^n\{X=h_i(y)\}$ for $y\in D$;
2. each $h_i$ is an invertible map from $D$ onto its range $D_i$ with a continuous derivative on $D$;
3. $D_1,\dots,D_n$ are pairwise disjoint.

Then $Y$ has density

$$
f_Y(y)=\begin{cases}\displaystyle\sum_{i=1}^nf\big(h_i(y)\big)\,\lvert h_i'(y)\rvert, & y\in D,\\ 0, & y\notin D.\end{cases}
$$

**Proof** By the assumptions, $\mathbb{P}(X\in\bigcup_iD_i)=\mathbb{P}(Y\in D)=1$. For an interval $(a,b]$ in $D$, the event $\{a<Y\le b\}$ differs from $\bigcup_i\{X\in h_i((a,b])\}$ by a set of probability zero, and the latter is a disjoint union. Each $h_i$ is continuous and invertible, hence strictly monotone, so the substitution $x=h_i(y)$ on each $D_i$ gives

$$
\mathbb{P}(a<Y\le b)=\sum_{i=1}^n\int_{h_i((a,b])}f(x)\,\mathrm{d}x=\sum_{i=1}^n\int_a^bf\big(h_i(y)\big)\lvert h_i'(y)\rvert\,\mathrm{d}y.\qquad\square
$$

**Example 5.2.4** Let $r$ be a positive constant and $X\sim\mathrm{U}(0,2\pi)$. Find the density of $Y=r\cos X$.

Method 1 (Theorem 5.2.3). Take $D=(-r,r)$, so that $\mathbb{P}(Y\in D)=1$. For $y\in D$,

$$
\{Y=y\}=\{\cos X=y/r,\ X\in(0,\pi)\}\cup\{\cos(2\pi-X)=y/r,\ X\in(\pi,2\pi)\}=\{X=\arccos(y/r)\}\cup\{X=2\pi-\arccos(y/r)\}.
$$
The functions $h_1(y)=\arccos(y/r)\colon D\to(0,\pi)$ and $h_2(y)=2\pi-\arccos(y/r)\colon D\to(\pi,2\pi)$ are invertible and continuously differentiable, with disjoint ranges. Using $f_X(x)=\frac1{2\pi}$ for $x\in(0,2\pi)$ and $[\arccos x]'=-\frac1{\sqrt{1-x^2}}$,

$$
f_Y(y)=\frac1{2\pi}\Big\lvert\frac{\mathrm{d}}{\mathrm{d}y}\arccos\frac yr\Big\rvert+\frac1{2\pi}\Big\lvert\frac{\mathrm{d}}{\mathrm{d}y}\Big[2\pi-\arccos\frac yr\Big]\Big\rvert=\frac1{\pi\sqrt{r^2-y^2}},\qquad y\in(-r,r).
$$

Method 2 (distribution functions). For $y\in(-r,r)$, $\{x\in(0,2\pi)\colon\cos x\le y/r\}=[\arccos(y/r),\,2\pi-\arccos(y/r)]$, so

$$
\mathbb{P}(Y\le y)=\int_{\{x\colon\cos x\le y/r\}}\frac1{2\pi}\,\mathrm{d}x=\frac1{2\pi}\big\{2\pi-2\arccos(y/r)\big\},
$$
and differentiation gives the same result. This is the arcsine distribution. Its density tends to infinity near $\pm r$, because the projection of a point rotating at constant speed spends the most time near the two ends.

![Left: y = r cos x on (0, 2π), where each y ∈ (−r, r) has two preimages h1(y) and h2(y); right: histogram of 100,000 simulated values of Y = r cos X with the density 1/(π√(r² − y²))](./plots/cosine-transform.py)

Either method may be used; what matters is solving the problem. The distribution function method always works; the density formulas are quicker but require finding every branch of the inverse correctly. Another useful technique is to recognize the "kernel" of a density: if the density obtained is proportional to a known density (such as $y^{-1/2}\mathrm{e}^{-y/2}$ in Example 5.2.3), normalization determines the constant and identifies the distribution.

## Summary

| Topic | Key points |
|---|---|
| Distribution function | $F(x)=\mathbb{P}(X\le x)$ exists for every random variable; nondecreasing, $F(-\infty)=0$, $F(\infty)=1$, right-continuous; jumps $F(x)-F(x-)=\mathbb{P}(X=x)$ |
| Relation to mass functions and densities | Discrete: $F(x)=\sum_{x_j\le x}p_j$ (a step function); continuous: $F(x)=\int_{-\infty}^xf(t)\,\mathrm{d}t$, $f=F'$ at continuity points; mixed and singular types also occur |
| Normal distribution function | $\Phi(-x)=1-\Phi(x)$, $\mathbb{P}(X\le a)=\Phi((a-\mu)/\sigma)$, the $3\sigma$ rule |
| Distributions of functions | Discrete: for each $y$, add the probabilities of its preimages; continuous: distribution function method (find $F_Y$, then differentiate), or the formula $f_Y(y)=\sum_if_X(h_i(y))\lvert h_i'(y)\rvert$ |
