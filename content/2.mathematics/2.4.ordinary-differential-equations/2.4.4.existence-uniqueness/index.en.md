---
title: Existence and Uniqueness Theorems
source_hash: 8cc6ab7aed07
---

Most differential equations cannot be solved by elementary integration, but this does not mean that they have no solutions. This chapter answers the first fundamental question of the theory of ordinary differential equations: under what conditions does the **initial value problem** for an explicit first-order equation $y'=f(x,y)$ have a solution, and when it does, is the solution unique? In [2.2.15](/2.2.15) the **existence and uniqueness theorem** (Theorem 15.1.1) was only stated; here we give complete proofs. First, Picard's successive approximations yield existence and uniqueness simultaneously under a Lipschitz condition. Next, the condition for uniqueness is weakened to the Osgood condition. Finally, we drop every regularity assumption in $y$, requiring only that $f$ be continuous, and prove the Peano existence theorem with Euler polygons and the Arzelà–Ascoli theorem. The solutions obtained here exist only on a small interval around the initial point; extending them to intervals as large as possible is the content of the next chapter, and the generalization to systems and higher-order equations is in [2.4.7](/2.4.7).

Throughout this chapter we consider the initial value problem

$$
y'=f(x,y),\qquad y(x_0)=y_0, \tag{4.1}
$$
where $f$ is continuous on the rectangle $R=\{(x,y)\mid\lvert x-x_0\rvert\le a,\ \lvert y-y_0\rvert\le b\}$, and we write $M=\max_R\lvert f\rvert$.

## 4.1. The Lipschitz Condition and the Equivalent Integral Equation

### 4.1.1. The Lipschitz Condition

**Definition 4.1.1 (Lipschitz Condition)** If there is a constant $L\ge0$ such that for any two points $(x,y_1)$, $(x,y_2)$ in $R$

$$
\lvert f(x,y_1)-f(x,y_2)\rvert\le L\lvert y_1-y_2\rvert,
$$
then $f$ is said to satisfy a **Lipschitz condition** with respect to $y$ on $R$, and $L$ is called a Lipschitz constant.

**Definition 4.1.2 (Local Lipschitz Condition)** Let $f$ be defined on a region $G$. If every point of $G$ has a neighborhood (a rectangle) on which $f$ satisfies a Lipschitz condition with respect to $y$ (the constant may vary with the neighborhood), then $f$ is said to satisfy a **local Lipschitz condition** with respect to $y$ in $G$.

**Proposition 4.1.1** If $f$ and $f_y$ are continuous on $R$, then $f$ satisfies a Lipschitz condition with respect to $y$ on $R$, and one may take $L=\max_R\lvert f_y\rvert$. Consequently, if $f$ and $f_y$ are continuous on a region $G$, then $f$ satisfies a local Lipschitz condition in $G$.

**Proof** For fixed $x$, the **mean value theorem** gives $f(x,y_1)-f(x,y_2)=f_y(x,\xi)(y_1-y_2)$ with $\xi$ between $y_1$ and $y_2$, so that $(x,\xi)$ is still in $R$. $\square$

The Lipschitz condition lies between "continuous" and "continuously differentiable": $f(y)=\lvert y\rvert$ is not differentiable at $y=0$ but satisfies a Lipschitz condition ($L=1$); $f(y)=\sqrt{\lvert y\rvert}$ is continuous, but $\lvert f(y)-f(0)\rvert/\lvert y\rvert=\lvert y\rvert^{-1/2}$ is unbounded near $0$, so it does not satisfy a Lipschitz condition.

### 4.1.2. The Equivalent Integral Equation

**Lemma 4.1.1** Let $\varphi$ be continuous on an interval $I\ni x_0$ with graph in $R$. Then $\varphi$ is a solution of the initial value problem (4.1) on $I$ if and only if it satisfies the integral equation

$$
\varphi(x)=y_0+\int_{x_0}^x f(t,\varphi(t))\,\mathrm{d}t,\qquad x\in I. \tag{4.2}
$$

**Proof** If $\varphi$ is a solution, then $\varphi'(t)=f(t,\varphi(t))$ is continuous; integrating from $x_0$ to $x$ and using $\varphi(x_0)=y_0$ gives (4.2). Conversely, if $\varphi$ satisfies (4.2), the integrand $f(t,\varphi(t))$ is continuous, so by the differentiation formula for an integral with a variable upper limit, $\varphi$ is differentiable with $\varphi'(x)=f(x,\varphi(x))$; moreover $\varphi(x_0)=y_0$. $\square$

The advantage of the integral equation is that it requires only continuity of $\varphi$, and integration is stable under uniform limits. Both constructions below (the Picard iteration and Euler polygons) first produce approximate solutions of (4.2) and then pass to the limit.

## 4.2. Picard's Theorem

**Theorem 4.2.1 (Picard Theorem)** Let $f$ be continuous on $R$ and satisfy a Lipschitz condition with respect to $y$. Let

$$
h=\min\Big\{a,\frac bM\Big\}
$$
(with $h=a$ if $M=0$). Then the initial value problem (4.1) has exactly one solution on the interval $I=[x_0-h,x_0+h]$.

The choice of $h$ has an intuitive geometric meaning. The slope of the integral curve is at most $M$ in absolute value, so the curve stays in the wedge with vertex $(x_0,y_0)$ bounded by the two lines of slopes $\pm M$. When $M$ is small, the integral curve is flat and reaches the left and right sides of $R$ first, so $h=a$; when $M$ is large, the curve is steep and may hit the top or bottom side first, so we can only take $h=b/M<a$.

**Proof** We prove the result on the right half-interval $[x_0,x_0+h]$; the left half is analogous. The proof has four steps.

Step 1: construct the *Picard iteration*. Let $\varphi_0(x)\equiv y_0$ and

$$
\varphi_{n+1}(x)=y_0+\int_{x_0}^x f(t,\varphi_n(t))\,\mathrm{d}t,\qquad n=0,1,2,\dots \tag{4.3}
$$
We show by induction that every $\varphi_n$ is defined and continuous on $I$ and satisfies $\lvert\varphi_n(x)-y_0\rvert\le M(x-x_0)\le b$. The case $n=0$ is clear. If $\varphi_n$ has these properties, then $f(t,\varphi_n(t))$ is defined and continuous, $\varphi_{n+1}$ is continuous, and

$$
\lvert\varphi_{n+1}(x)-y_0\rvert\le\int_{x_0}^x\lvert f(t,\varphi_n(t))\rvert\,\mathrm{d}t\le M(x-x_0)\le Mh\le b.
$$
Thus no step of (4.3) leaves $R$, which is exactly why we take $h\le b/M$.

Step 2: estimate the differences of consecutive terms. We show by induction that

$$
\lvert\varphi_{n+1}(x)-\varphi_n(x)\rvert\le\frac{ML^n(x-x_0)^{n+1}}{(n+1)!},\qquad x\in[x_0,x_0+h]. \tag{4.4}
$$
For $n=0$ this is the estimate $\lvert\varphi_1-\varphi_0\rvert\le M(x-x_0)$ of Step 1. If (4.4) holds for $n$, then by the Lipschitz condition

$$
\lvert\varphi_{n+2}(x)-\varphi_{n+1}(x)\rvert\le\int_{x_0}^x L\lvert\varphi_{n+1}(t)-\varphi_n(t)\rvert\,\mathrm{d}t\le L\int_{x_0}^x\frac{ML^n(t-x_0)^{n+1}}{(n+1)!}\,\mathrm{d}t=\frac{ML^{n+1}(x-x_0)^{n+2}}{(n+2)!}.
$$

Step 3: uniform convergence to a solution. $\varphi_n=\varphi_0+\sum_{k=0}^{n-1}(\varphi_{k+1}-\varphi_k)$ is a partial sum of a series of functions whose terms, by (4.4), are dominated by the convergent numerical series $\sum_k\dfrac{ML^kh^{k+1}}{(k+1)!}$. By the **Weierstrass M-test**, the sequence $\{\varphi_n\}$ is **uniformly convergent** on $[x_0,x_0+h]$ to a continuous function $\varphi$, and $\lvert\varphi(x)-y_0\rvert\le M(x-x_0)\le b$. By the Lipschitz condition,

$$
\lvert f(t,\varphi_n(t))-f(t,\varphi(t))\rvert\le L\lvert\varphi_n(t)-\varphi(t)\rvert,
$$
so $f(t,\varphi_n(t))$ converges uniformly to $f(t,\varphi(t))$, and we may pass to the limit under the integral in (4.3), which shows that $\varphi$ satisfies the integral equation (4.2). By Lemma 4.1.1, $\varphi$ is a solution of (4.1).

Step 4: uniqueness. Let $\psi$ be any solution of (4.1) on $[x_0,x_0+c]$ ($0<c\le h$) with graph in $R$. Exactly as in Step 2, induction shows that

$$
\lvert\psi(x)-\varphi_n(x)\rvert\le\frac{ML^n(x-x_0)^{n+1}}{(n+1)!}:
$$
for $n=0$ we have $\lvert\psi(x)-y_0\rvert=\Big\lvert\int_{x_0}^xf(t,\psi(t))\,\mathrm{d}t\Big\rvert\le M(x-x_0)$, and the induction step uses only the fact that $\psi$ satisfies the integral equation (4.2). Letting $n\to\infty$, the right-hand side tends to $0$, so $\psi=\lim\varphi_n=\varphi$. $\square$

Taking $\psi=\varphi$ in Step 4 gives an error estimate for successive approximations.

**Corollary 4.2.1 (Error Estimate)** Under the hypotheses of Theorem 4.2.1, for $x\in I$,

$$
\lvert\varphi(x)-\varphi_n(x)\rvert\le\frac{ML^n\lvert x-x_0\rvert^{n+1}}{(n+1)!}\le\frac{ML^nh^{n+1}}{(n+1)!}.
$$

**Remark 4.2.1** The proof can also be phrased in the language of contraction mappings. Define the operator $(T\varphi)(x)=y_0+\int_{x_0}^xf(t,\varphi(t))\,\mathrm{d}t$ on a space of continuous functions. The integral equation (4.2) is then the fixed-point equation $\varphi=T\varphi$, and the Picard iteration is the iteration $\varphi_{n+1}=T\varphi_n$. The factorial in estimate (4.4) shows that high powers of $T$ are contractions, so there is no need to choose $h$ with $Lh<1$.

**Example 4.2.1** For $y'=y$, $y(0)=1$, the function $f(x,y)=y$ satisfies a Lipschitz condition on the whole plane ($L=1$). The Picard iteration is

$$
\varphi_0=1,\quad\varphi_1=1+x,\quad\varphi_2=1+x+\frac{x^2}{2},\quad\dots,\quad\varphi_n=\sum_{k=0}^n\frac{x^k}{k!},
$$
which are precisely the Taylor polynomials of $\mathrm{e}^x$; they converge uniformly to the solution $\mathrm{e}^x$ on every bounded interval.

![The Picard iterates phi_0, ..., phi_4 for the initial value problem y' = y, y(0) = 1 and the exact solution e^x: the iterates first fit the solution near the initial point, and the range of good approximation widens as n increases](./plots/picard-iterates.py)

**Example 4.2.2** For $y'=x^2+y^2$, $y(0)=0$, take $R:\lvert x\rvert\le1$, $\lvert y\rvert\le1$. Then $M=2$, $L=\max_R\lvert2y\rvert=2$ and $h=\min\{1,1/2\}=\dfrac12$. The first iterates are

$$
\varphi_1=\frac{x^3}{3},\qquad\varphi_2=\frac{x^3}{3}+\frac{x^7}{63},
$$
and by Corollary 4.2.1, $\lvert\varphi-\varphi_2\rvert\le\dfrac{2\cdot2^2\cdot(1/2)^3}{3!}=\dfrac16$ on $\lvert x\rvert\le\dfrac12$. This error bound is very conservative: the actual error is less than $10^{-4}$. The solution of this equation cannot be expressed in elementary functions, but the theorem guarantees that it exists and is unique; for its actual interval of existence see Example 5.4.1.

## 4.3. Osgood's Uniqueness Theorem

The Lipschitz condition is only a sufficient condition for uniqueness. No uniqueness condition is known that is both necessary and sufficient and also easy to verify; the Osgood condition below is weaker than the Lipschitz condition and is optimal in a certain sense (Remark 4.3.1).

**Definition 4.3.1 (Osgood Condition)** Let $f$ be continuous on a region $G$. If for any two points $(x,y_1)$, $(x,y_2)$ in $G$

$$
\lvert f(x,y_1)-f(x,y_2)\rvert\le F(\lvert y_1-y_2\rvert),
$$
where $F(r)$ is a positive continuous function for $r>0$ such that for some $r_1>0$ the improper integral

$$
\int_0^{r_1}\frac{\mathrm{d}r}{F(r)}=+\infty,
$$
then $f$ is said to satisfy the **Osgood condition** with respect to $y$ in $G$.

The Lipschitz condition is the special case $F(r)=Lr$: $\int_0^{r_1}\frac{\mathrm{d}r}{Lr}=+\infty$.

**Theorem 4.3.1 (Osgood's Theorem)** If $f$ satisfies the Osgood condition with respect to $y$ in a region $G$, then through each point of $G$ there passes at most one solution of $y'=f(x,y)$.

**Proof** Suppose two solutions $y=y_1(x)$ and $y=y_2(x)$ both pass through a point $(x_0,y_0)\in G$, and there is an $x_1$ with $y_1(x_1)\ne y_2(x_1)$. Without loss of generality let $x_1>x_0$ and $y_1(x_1)>y_2(x_1)$ (the case $x_1<x_0$ is analogous). Let

$$
\bar x=\sup\{x\in[x_0,x_1]\mid y_1(x)=y_2(x)\}.
$$
By continuity $y_1(\bar x)=y_2(\bar x)$, so $x_0\le\bar x<x_1$, and $r(x)=y_1(x)-y_2(x)$ satisfies $r(\bar x)=0$ and $r(x)>0$ for $\bar x<x\le x_1$. On $(\bar x,x_1]$,

$$
r'(x)=f(x,y_1(x))-f(x,y_2(x))\le F(\lvert y_1(x)-y_2(x)\rvert)=F(r(x)),
$$
that is, $\dfrac{r'(x)}{F(r(x))}\le1$. For $\bar x<\xi<x_1$, integrating from $\xi$ to $x_1$ and substituting $r=r(x)$ gives

$$
\int_{r(\xi)}^{r(x_1)}\frac{\mathrm{d}r}{F(r)}\le x_1-\xi.
$$
As $\xi\to\bar x^+$ we have $r(\xi)\to0^+$, so the left-hand side tends to $\int_0^{r(x_1)}\frac{\mathrm{d}r}{F(r)}=+\infty$ (since $F$ is positive and continuous on $(0,+\infty)$, divergence of the integral depends only on the behavior near $0$), while the right-hand side is bounded, a contradiction. $\square$

**Example 4.3.1** Discuss whether the solution of $y'=\lvert y\rvert^\alpha$ ($\alpha>0$) with $y(0)=0$ is unique. Note that $y\equiv0$ is always a solution.

(1) $\alpha\ge1$: $f(y)=\lvert y\rvert^\alpha$ satisfies a Lipschitz condition on $\lvert y\rvert\le1$ ($L=1$ for $\alpha=1$; for $\alpha>1$, $f$ is continuously differentiable and $L=\alpha$), so the zero solution is unique, and no nonzero solution ever vanishes. For example, for $\alpha>1$ and $y(0)=y_0>0$, separation of variables gives

$$
y=\frac{y_0}{\big(1-(\alpha-1)y_0^{\alpha-1}x\big)^{1/(\alpha-1)}},
$$
which tends to infinity as $x\to\dfrac{1}{(\alpha-1)y_0^{\alpha-1}}$ but stays positive on its interval of existence; for $\alpha=1$ the solutions are $y=y_0\mathrm{e}^x$ ($y_0>0$) or $y=y_0\mathrm{e}^{-x}$ ($y_0<0$).

(2) $0<\alpha<1$: $f$ does not satisfy a Lipschitz condition near $y=0$, and for $F(r)=r^\alpha$ we have $\int_0^{r_1}r^{-\alpha}\,\mathrm{d}r=\dfrac{r_1^{1-\alpha}}{1-\alpha}<+\infty$, so the Osgood condition fails as well. Uniqueness is indeed lost: for any $c_1\le0\le c_2$,

$$
y=\begin{cases}-\big((1-\alpha)(c_1-x)\big)^{1/(1-\alpha)},&x<c_1,\\0,&c_1\le x\le c_2,\\\big((1-\alpha)(x-c_2)\big)^{1/(1-\alpha)},&x>c_2\end{cases}
$$
is a solution with $y(0)=0$. Since $y'=\lvert y\rvert^\alpha\ge0$, every solution must be nondecreasing, so only the negative branch can occur on the side $x<0$.

![The family of solutions of y' = |y|^{1/2} through the origin: after following the x-axis for a while, a solution branches off to the right at any c_2 >= 0 as y = (x - c_2)^2/4, and to the left at any c_1 <= 0 as y = -(c_1 - x)^2/4; all solutions are nondecreasing](./plots/osgood-nonuniqueness.py)

**Example 4.3.2** For the equation

$$
y'=f(y)=\begin{cases}y\ln\lvert y\rvert,&y\ne0,\\0,&y=0,\end{cases}
$$
the solution with $y(0)=0$ is unique, although $f$ does not satisfy a Lipschitz condition near $y=0$: $\dfrac{\lvert f(y)-f(0)\rvert}{\lvert y\rvert}=\lvert\ln\lvert y\rvert\rvert\to+\infty$. In the strip $\lvert y\rvert<\dfrac14$, using the monotonicity and concavity of $-t\ln t$ on $(0,\mathrm{e}^{-1})$, one can verify that $\lvert f(y_1)-f(y_2)\rvert\le F(\lvert y_1-y_2\rvert)$ with $F(r)=2r\lvert\ln r\rvert$ ($0<r<\frac12$), and

$$
\int_0^{r_1}\frac{\mathrm{d}r}{r\lvert\ln r\rvert}=\Big[-\ln\lvert\ln r\rvert\Big]_0^{r_1}=+\infty,
$$
so the Osgood condition holds and the zero solution is unique; where $y\ne0$, $f$ is continuously differentiable and a local Lipschitz condition holds. In fact the solution with $y(0)=y_0\ne0$ is $y=\operatorname{sgn}(y_0)\exp\!\big(\mathrm{e}^x\ln\lvert y_0\rvert\big)$, which never vanishes. This example shows that the Lipschitz condition is not necessary for uniqueness.

**Remark 4.3.1** For equations whose right-hand side depends only on $y$, the Osgood condition is optimal. Let $F$ be continuous with $F(0)=0$ and $F(r)>0$ for $r>0$. If $\int_0^{r_1}\frac{\mathrm{d}r}{F(r)}<+\infty$, then $y'=F(\lvert y\rvert)$, $y(0)=0$ has a solution other than the zero solution: take $0$ for $x\le0$, and for $x>0$ take the positive function $y(x)$ obtained by inverting $x=\int_0^y\frac{\mathrm{d}r}{F(r)}$. Uniqueness is lost; Example 4.3.1 (2) is of this type.

## 4.4. The Peano Existence Theorem

If we drop the Lipschitz condition and require only that $f$ be continuous, solutions still exist, though they may not be unique (Example 4.3.1). The Picard iteration may then fail to converge, so we need a different kind of approximate solution, and compactness takes the place of contraction.

### 4.4.1. Euler Polygons

We keep $h=\min\{a,b/M\}$. In view of the geometric meaning of the **direction field**, the most natural approximate solutions are polygonal paths that follow the line elements.

**Definition 4.4.1 (Euler Polygon)** Divide $[x_0,x_0+h]$ into $n$ equal parts with division points $x_k=x_0+kh/n$. Starting from the initial value $y_0$, let

$$
y_{k+1}=y_k+f(x_k,y_k)(x_{k+1}-x_k),\qquad k=0,1,\dots,n-1.
$$
The polygonal path $y=\varphi_n(x)$ obtained by joining $(x_0,y_0),(x_1,y_1),\dots,(x_n,y_n)$ in order is called the **Euler polygon** of the initial value problem (4.1). The polygon on $[x_0-h,x_0]$ is constructed in the same way to the left.

On each piece $(x_k,x_{k+1})$ we have $\varphi_n'(x)=f(x_k,\varphi_n(x_k))$: at each division point the polygon sets off in the direction of the line element there. This is Euler's method, the simplest method of numerical analysis.

**Lemma 4.4.1** The Euler polygon $\varphi_n$ is defined on $[x_0,x_0+h]$, and

1. $\lvert\varphi_n(x)-y_0\rvert\le M(x-x_0)\le b$, that is, the polygon does not leave $R$;
2. $\lvert\varphi_n(x)-\varphi_n(x')\rvert\le M\lvert x-x'\rvert$;
3. $\varphi_n(x)=y_0+\displaystyle\int_{x_0}^xf(t,\varphi_n(t))\,\mathrm{d}t+\delta_n(x)$, where $\delta_n\to0$ uniformly on $[x_0,x_0+h]$.

**Proof** (1) By induction on $k$: if $(x_j,y_j)\in R$ for $j\le k$, then the slope of each piece is at most $M$ in absolute value, so $\lvert y_{k+1}-y_0\rvert\le M(x_{k+1}-x_0)\le Mh\le b$; hence $(x_{k+1},y_{k+1})\in R$ and $f(x_{k+1},y_{k+1})$ is defined. (2) The slope of each piece of the polygon is at most $M$ in absolute value.

(3) Let $g_n(t)=f(x_k,\varphi_n(x_k))$ for $x_k\le t<x_{k+1}$. Then $\varphi_n(x)=y_0+\int_{x_0}^xg_n(t)\,\mathrm{d}t$, so

$$
\delta_n(x)=\int_{x_0}^x\big(g_n(t)-f(t,\varphi_n(t))\big)\,\mathrm{d}t.
$$
The function $f$ is **uniformly continuous** on the bounded closed set $R$: for every $\varepsilon>0$ there is $\eta>0$ such that $\lvert f(t,y)-f(s,z)\rvert<\varepsilon$ whenever $\lvert t-s\rvert<\eta$ and $\lvert y-z\rvert<\eta$. When $n$ is so large that $\dfrac hn<\eta$ and $\dfrac{Mh}n<\eta$, for $x_k\le t<x_{k+1}$ we have $\lvert t-x_k\rvert<\eta$ and $\lvert\varphi_n(t)-\varphi_n(x_k)\rvert\le M\dfrac hn<\eta$, hence $\lvert g_n(t)-f(t,\varphi_n(t))\rvert<\varepsilon$ and $\lvert\delta_n(x)\rvert\le\varepsilon h$. $\square$

![Euler polygons (n = 2, 4, 8, 16) on [0, 1] for the initial value problem y' = x + y, y(0) = 0 and the exact solution y = e^x - x - 1: the polygons approximate the solution uniformly as n increases](./plots/euler-polygons.py)

### 4.4.2. The Arzelà–Ascoli Theorem

The sequence of Euler polygons need not converge (when solutions are not unique, different subsequences may approach different solutions), but it has a convergent subsequence. What guarantees this is compactness of sequences of functions.

**Definition 4.4.2** Let $\{g_n\}$ be a sequence of functions on an interval $I$.

1. If there is a constant $K$ with $\lvert g_n(x)\rvert\le K$ for all $n$ and all $x\in I$, then $\{g_n\}$ is said to be **uniformly bounded** on $I$.
2. If for every $\varepsilon>0$ there is a $\delta>0$, independent of $n$, such that $\lvert g_n(x)-g_n(x')\rvert<\varepsilon$ for all $n$ whenever $x,x'\in I$ and $\lvert x-x'\rvert<\delta$, then $\{g_n\}$ is said to be **equicontinuous** on $I$.

For example, a sequence satisfying a common Lipschitz estimate $\lvert g_n(x)-g_n(x')\rvert\le M\lvert x-x'\rvert$ is equicontinuous (take $\delta=\varepsilon/M$).

**Lemma 4.4.2 (Arzelà–Ascoli Theorem)** If a sequence of functions $\{g_n\}$ is uniformly bounded and equicontinuous on a bounded closed interval $I$, then it has a subsequence that converges uniformly on $I$.

**Proof** Step 1: convergence on a countable dense set. Enumerate the rational points of $I$ as $r_1,r_2,\dots$. The sequence $\{g_n(r_1)\}$ is bounded, so by the **Bolzano–Weierstrass theorem** it has a convergent subsequence $\{g_{1,n}\}$; the sequence $\{g_{1,n}(r_2)\}$ is bounded, so from it we can again select a subsequence $\{g_{2,n}\}$ converging at $r_2$; and so on. The $k$th subsequence $\{g_{k,n}\}$ converges at $r_1,\dots,r_k$ and is a subsequence of the previous one. Take the diagonal sequence $G_n=g_{n,n}$. From its $k$th term on, it is a subsequence of $\{g_{k,n}\}$, so it converges at every $r_k$.

Step 2: uniform convergence. Given $\varepsilon>0$, take $\delta$ as in the definition of equicontinuity. Since $I$ is bounded and closed, it can be covered by finitely many subintervals of length less than $\delta$; choosing a rational point in each gives finitely many points $r_{k_1},\dots,r_{k_N}$ such that every point of $I$ is within distance $\delta$ of one of them. By Step 1 there is $N_0$ such that $\lvert G_m(r_{k_j})-G_n(r_{k_j})\rvert<\varepsilon$ ($j=1,\dots,N$) for $m,n\ge N_0$. For any $x\in I$, choose $j$ with $\lvert x-r_{k_j}\rvert<\delta$; then

$$
\lvert G_m(x)-G_n(x)\rvert\le\lvert G_m(x)-G_m(r_{k_j})\rvert+\lvert G_m(r_{k_j})-G_n(r_{k_j})\rvert+\lvert G_n(r_{k_j})-G_n(x)\rvert<3\varepsilon.
$$
By the Cauchy criterion for uniform convergence, $\{G_n\}$ converges uniformly on $I$. $\square$

In analysis this result is the core of the Arzelà–Ascoli theorem, which characterizes the relatively compact subsets of the space of continuous functions on a bounded closed interval.

### 4.4.3. The Peano Existence Theorem

**Theorem 4.4.1 (Peano Existence Theorem)** If $f$ is continuous on the rectangle $R$, then the initial value problem (4.1) has at least one solution on $I=[x_0-h,x_0+h]$, where $h=\min\{a,b/M\}$.

**Proof** Consider first the right half-interval. By Lemma 4.4.1, the sequence of Euler polygons $\{\varphi_n\}$ is uniformly bounded on $[x_0,x_0+h]$ ($\lvert\varphi_n\rvert\le\lvert y_0\rvert+b$) and equicontinuous (with the common Lipschitz constant $M$). By the Arzelà–Ascoli theorem, a subsequence $\varphi_{n_k}$ converges uniformly to a continuous function $\varphi$ with $\lvert\varphi(x)-y_0\rvert\le M(x-x_0)\le b$. Since $f$ is uniformly continuous on $R$, $f(t,\varphi_{n_k}(t))$ converges uniformly to $f(t,\varphi(t))$; moreover $\delta_{n_k}\to0$ uniformly. Letting $k\to\infty$ in

$$
\varphi_{n_k}(x)=y_0+\int_{x_0}^xf(t,\varphi_{n_k}(t))\,\mathrm{d}t+\delta_{n_k}(x),
$$
we find that $\varphi$ satisfies the integral equation (4.2), so by Lemma 4.1.1 it is a solution on the right half-interval. In the same way we obtain a solution on the left half-interval. Both take the value $y_0$ at $x_0$, so the function obtained by joining them satisfies (4.2) on all of $I$ and is therefore a solution of (4.1). $\square$

**Corollary 4.4.1** Under the hypotheses of Theorem 4.4.1, if the solution of the initial value problem (4.1) on $I$ is unique, then the whole sequence of Euler polygons converges uniformly to this solution.

**Proof** Otherwise there are $\varepsilon>0$ and a subsequence $\varphi_{n_k}$ with $\max_I\lvert\varphi_{n_k}-\varphi\rvert\ge\varepsilon$. Applying the Arzelà–Ascoli theorem to this subsequence, it has a uniformly convergent subsequence whose limit, by the proof of the theorem, is a solution of (4.1), and hence equals $\varphi$ by uniqueness, a contradiction. $\square$

Thus under a Lipschitz condition Euler's method is a convergent numerical method; without uniqueness, different subsequences of Euler polygons may approach different solutions.

## Summary

| Theorem | Hypotheses | Conclusion | Method |
|---|---|---|---|
| Picard's theorem (Theorem 4.2.1) | $f$ continuous and Lipschitz in $y$ | Existence and uniqueness on $[x_0-h,x_0+h]$ | Successive approximations, Weierstrass M-test |
| Osgood's theorem (Theorem 4.3.1) | $f$ continuous, satisfying the Osgood condition | At most one solution through each point | Contradiction, comparison with $\int\frac{\mathrm{d}r}{F(r)}$ |
| Peano's theorem (Theorem 4.4.1) | $f$ continuous | Existence on $[x_0-h,x_0+h]$ | Euler polygons, Arzelà–Ascoli theorem |

The conclusions of all three theorems are local: $h=\min\{a,b/M\}$ may be much smaller than the actual interval of existence of the solution. In the next chapter, the extension theorem extends local solutions to solutions on the maximal interval of existence, and comparison theorems are used to estimate this interval.
