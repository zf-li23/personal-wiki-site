---
title: Continuation of Solutions and Comparison Theorems
source_hash: 2eea228bbc14
---

The Picard and Peano theorems of the previous chapter guarantee only that a solution exists on an interval $\lvert x-x_0\rvert\le h$ around the initial point, where $h=\min\{a,b/M\}$ depends on the chosen rectangle and is often much smaller than the range on which the solution actually exists. In this chapter we pass from local to global solutions. The extension theorem states that in an open region where $f$ is continuous, an integral curve can be continued all the way to the boundary of the region: the maximal interval of existence of a solution is open, and at its endpoints the solution either tends to infinity or approaches the boundary of the region. When $f$ grows at most linearly in $y$, solutions exist on the whole interval. To estimate the maximal interval of existence we then establish comparison theorems: if the right-hand sides of two equations are ordered, so are their solutions through a common point. Without uniqueness, comparison has to be carried out through maximal and minimal solutions. The results of this chapter are generalized to systems in [2.4.7](/2.4.7).

Throughout this chapter $G$ is a plane **region** (a connected open set), and $f$ is continuous in $G$.

## 5.1. Continuation of Solutions

### 5.1.1. Noncontinuable Solutions and the Maximal Interval of Existence

**Definition 5.1.1** Let $y=\varphi(x)$ be a solution of the equation $y'=f(x,y)$ on an interval $J$. If a solution $y=\psi(x)$ is defined on an interval $J_1$ properly containing $J$ and $\psi=\varphi$ on $J$, then $\psi$ is called an **extension** of $\varphi$. A solution that admits no extension is called a **noncontinuable solution**, and its interval of definition is called the **maximal interval of existence**.

Without uniqueness, one and the same solution may have different noncontinuable extensions, possibly with different maximal intervals of existence; with uniqueness the noncontinuable extension is unique (Corollary 5.1.2).

**Lemma 5.1.1** The maximal interval of existence of a noncontinuable solution is open.

**Proof** Suppose the interval of definition of a noncontinuable solution $\varphi$ contains its right endpoint $\beta$. The graph of the solution lies in $G$, so $(\beta,\varphi(\beta))\in G$. Take a rectangle centered at this point and contained in $G$. By the Peano existence theorem (Theorem 4.4.1) there is a solution $\chi$ on $[\beta,\beta+h_1]$ with $\chi(\beta)=\varphi(\beta)$. Let $\psi=\varphi$ for $x\le\beta$ and $\psi=\chi$ for $x\ge\beta$. The left and right derivatives of $\psi$ at $\beta$ both equal $f(\beta,\varphi(\beta))$, so $\psi$ is an extension of $\varphi$, contradicting noncontinuability. The left endpoint is treated in the same way. $\square$

**Lemma 5.1.2 (Uniform Local Existence)** Let $K\subset G$ be a bounded closed set. Then there is an $\eta>0$, depending only on $K$, such that for every $(\xi,\zeta)\in K$ the solution satisfying $y(\xi)=\zeta$ exists on $[\xi-\eta,\xi+\eta]$.

**Proof** Since $K$ is bounded and closed and $G$ is open, the distance $d$ from $K$ to the boundary of $G$ is positive (if $G$ is the whole plane, take $d=1$). The points at distance at most $d/2$ from $K$ form a bounded closed set $K'\subset G$; let $M'=\max_{K'}\lvert f\rvert+1$. For $(\xi,\zeta)\in K$, take $a=\dfrac{d}{2\sqrt2}$. The points of the square $\lvert x-\xi\rvert\le a$, $\lvert y-\zeta\rvert\le a$ are at distance at most $d/2$ from $(\xi,\zeta)$, so the square is contained in $K'$. By the Peano existence theorem, the solution exists on $\lvert x-\xi\rvert\le\eta$, where $\eta=\min\{a,a/M'\}$ does not depend on $(\xi,\zeta)$. $\square$

### 5.1.2. The Extension Theorem

**Theorem 5.1.1 (Extension Theorem)** Let $f$ be continuous in a region $G$.

1. Every solution of the equation $y'=f(x,y)$ can be extended to a noncontinuable solution.
2. Let $y=\varphi(x)$ be a noncontinuable solution with maximal interval of existence $(\alpha,\beta)$. Then as $x\to\beta^-$, the point $(x,\varphi(x))$ eventually leaves every bounded closed subset of $G$: for every bounded closed set $K\subset G$ there is $x_K<\beta$ such that $(x,\varphi(x))\notin K$ for $x_K<x<\beta$. The same holds as $x\to\alpha^+$.

Geometrically, the integral curve through any point of $G$ can be continued in both directions all the way to the boundary of $G$. "Reaching the boundary" covers three cases: $\beta=+\infty$; $\varphi(x)$ is unbounded; or the integral curve approaches a boundary point of $G$.

**Proof** We first prove (2). If $\beta=+\infty$, the abscissas of the points of $K$ are bounded and the conclusion is obvious. Assume $\beta<+\infty$.

Step 1: the integral curve cannot stay inside $K$ on an entire interval $(\beta-\varepsilon,\beta)$. Otherwise $\lvert\varphi'\rvert\le M_K=\max_K\lvert f\rvert$ there, so $\lvert\varphi(x)-\varphi(x')\rvert\le M_K\lvert x-x'\rvert$; by the Cauchy criterion, the limit $\gamma=\lim_{x\to\beta^-}\varphi(x)$ exists, and $(\beta,\gamma)\in K\subset G$ since $K$ is closed. Setting $\varphi(\beta)=\gamma$ and letting $x\to\beta^-$ in the integral equation $\varphi(x)=\varphi(x_1)+\int_{x_1}^xf(t,\varphi(t))\,\mathrm{d}t$, we see that $\varphi$ is still a solution on $(\alpha,\beta]$, contradicting noncontinuability.

Step 2: suppose the conclusion fails. Then there are $x_j\to\beta^-$ with $(x_j,\varphi(x_j))\in K$. Take $d$ and $K'$ as in the proof of Lemma 5.1.2 and $M'=\max_{K'}\lvert f\rvert+1$. Applying Step 1 to $K'$, we find $t_j\in(x_j,\beta)$ such that the point $P(x)=(x,\varphi(x))$ stays in $K'$ on $[x_j,t_j)$ while $P(t_j)$ is at distance exactly $d/2$ from $K$ (take the first such point). On $[x_j,t_j]$ the slope is at most $M'$, so

$$
\frac d2\le\lvert P(t_j)-P(x_j)\rvert\le(t_j-x_j)\sqrt{1+M'^2}\le(\beta-x_j)\sqrt{1+M'^2}\to0,
$$
a contradiction.

Now we prove (1); we discuss only extension to the right. Let $K_m=\{(x,y)\in G\mid x^2+y^2\le m^2,\ \operatorname{dist}\big((x,y),\partial G\big)\ge1/m\}$. Then $K_1\subset K_2\subset\cdots$ are bounded closed subsets of $G$, and every bounded closed subset of $G$ is contained in some $K_m$ (its distance to the boundary is positive). Let $\eta_m$ be the step length given by Lemma 5.1.2 for $K_m$. Starting from the given solution, we extend in rounds $m=1,2,\dots$: in round $m$, as long as the right endpoint $(b,\varphi(b))$ of the current solution lies in $K_m$, we attach the solution through this point that exists on $[b,b+\eta_m]$ (joining as in Lemma 5.1.1 again gives a solution). The abscissas of the points of $K_m$ are bounded, so each round consists of finitely many steps, and at its end the right endpoint is not in $K_m$; then the next round begins. In this way we obtain a solution $\varphi$ on $[x_0,\beta)$, where $\beta$ is the limit of the right endpoints of the steps (the right endpoint cannot stop changing after finitely many steps, since it belongs to some $K_m$).

If $\varphi$ could still be extended to $[x_0,\beta]$, its graph over $[x_0,\beta]$ would be a bounded closed subset of $G$, contained in some $K_{m_0}$. But for every $m\ge m_0$, the right endpoint at the end of round $m$ is a point of the graph of $\varphi$ with abscissa less than $\beta$ that does not lie in $K_m\supset K_{m_0}$, a contradiction. Hence $\varphi$ cannot be extended to the right; treating the left side in the same way gives a noncontinuable solution. $\square$

**Corollary 5.1.1** Let $f$ be continuous on the strip $S=\{(x,y)\mid a<x<b,\ y\in\mathbb{R}\}$ ($a$ may be $-\infty$ and $b$ may be $+\infty$), and let $\varphi$ be a noncontinuable solution with maximal interval of existence $(\alpha,\beta)$. If $\beta<b$, then $\lvert\varphi(x)\rvert\to+\infty$ as $x\to\beta^-$; similarly at the left endpoint.

**Proof** For any $N>0$, $K=[x_0,\beta]\times[-N,N]$ is a bounded closed subset of $S$. By the extension theorem, $(x,\varphi(x))\notin K$ for $x$ close to $\beta$, that is, $\lvert\varphi(x)\rvert>N$. $\square$

This is the phenomenon of blow-up: inside a strip, a solution can only terminate by tending to infinity.

**Corollary 5.1.2** If $f$ is continuous in $G$ and satisfies a local Lipschitz condition with respect to $y$, then through each point of $G$ there passes exactly one noncontinuable solution, and any two solutions of the same initial value problem coincide on their common interval.

**Proof** Let $\varphi_1$ and $\varphi_2$ be solutions of the same initial value problem on an interval $J$, and let $E=\{x\in J\mid\varphi_1(x)=\varphi_2(x)\}$. The set $E$ is nonempty and closed in $J$. For $x_1\in E$, the uniqueness part of Picard's theorem (Theorem 4.2.1) applied near the point $(x_1,\varphi_1(x_1))$ shows that $\varphi_1$ and $\varphi_2$ coincide on a neighborhood of $x_1$, so $E$ is also open. Since an interval is connected, $E=J$. Consequently, the union of all solutions (each taken on its own interval) defines a solution, and this is the unique noncontinuable solution. $\square$

**Example 5.1.1** The right-hand side of $y'=y^2$ is continuously differentiable on the whole plane, yet solutions need not exist on all of $\mathbb{R}$. The noncontinuable solution with $y(0)=y_0$ is

$$
y=\frac{y_0}{1-y_0x}.
$$
For $y_0>0$ the maximal interval of existence is $(-\infty,1/y_0)$, and $y\to+\infty$ as $x\to(1/y_0)^-$; for $y_0<0$ it is $(1/y_0,+\infty)$; for $y_0=0$ it is $\mathbb{R}$. The maximal interval of existence varies from solution to solution, and the larger the initial value, the sooner the solution blows up.

![Several noncontinuable solutions of y' = y^2: the solution starting from y(0) = y_0 > 0 blows up at x = 1/y_0 (dashed line), solutions with y_0 < 0 blow up to the left at x = 1/y_0, and the zero solution exists on the whole real line](./plots/blow-up.py)

**Example 5.1.2** Consider $y'=-\dfrac xy$ in the upper half-plane $G=\{y>0\}$. The noncontinuable solution through $(0,R)$ is the semicircle $y=\sqrt{R^2-x^2}$, with maximal interval of existence $(-R,R)$. Here the solution is bounded; as $x\to\pm R$ the integral curve approaches the boundary points $(\pm R,0)$ of $G$, where the right-hand side of the equation is undefined.

### 5.1.3. Global Existence

When $f$ grows at most linearly in $y$, blow-up cannot occur.

**Theorem 5.1.2** Let $f$ be continuous on the strip $S=\{(x,y)\mid\alpha<x<\beta,\ y\in\mathbb{R}\}$ and satisfy

$$
\lvert f(x,y)\rvert\le A(x)\lvert y\rvert+B(x),
$$
where $A(x),B(x)\ge0$ are continuous on $(\alpha,\beta)$. Then every noncontinuable solution of $y'=f(x,y)$ has $(\alpha,\beta)$ as its maximal interval of existence.

**Proof** Let a noncontinuable solution $\varphi$ pass through $(x_0,y_0)$, and suppose the right endpoint $\beta_1$ of its maximal interval of existence satisfies $\beta_1<\beta$. Since $A$ and $B$ are continuous on $[x_0,\beta_1]$, we may take $A_0=\max A+1$ and $B_0=\max B$. For $x\in[x_0,\beta_1)$,

$$
\lvert\varphi(x)\rvert\le\lvert y_0\rvert+\int_{x_0}^x\big(A_0\lvert\varphi(t)\rvert+B_0\big)\,\mathrm{d}t=:u(x).
$$
Then $u'=A_0\lvert\varphi\rvert+B_0\le A_0u+B_0$, so $\Big(\mathrm{e}^{-A_0(x-x_0)}\big(u+\frac{B_0}{A_0}\big)\Big)'\le0$ and

$$
\lvert\varphi(x)\rvert\le u(x)\le\Big(\lvert y_0\rvert+\frac{B_0}{A_0}\Big)\mathrm{e}^{A_0(\beta_1-x_0)}.
$$
Thus $\varphi$ is bounded near $\beta_1$, contradicting Corollary 5.1.1. The left endpoint is treated in the same way. $\square$

The argument in this proof, which derives an exponential bound from an integral inequality, is formalized as Grönwall's inequality in [2.4.7](/2.4.7).

**Example 5.1.3** (1) The first-order linear equation $y'=p(x)y+q(x)$ ($p,q$ continuous on $(\alpha,\beta)$) satisfies $\lvert f\rvert\le\lvert p\rvert\lvert y\rvert+\lvert q\rvert$, so all of its solutions exist on the whole interval $(\alpha,\beta)$, in agreement with the general solution formula of [2.2.15](/2.2.15); the corresponding result for linear systems is in [2.4.8](/2.4.8). (2) The right-hand side of $y'=\sin(xy)$ is bounded, so every solution exists on $\mathbb{R}$. (3) The function $y^2$ of Example 5.1.1 grows superlinearly, so the theorem does not apply, and solutions do blow up.

## 5.2. The First Comparison Theorem

The extension theorem alone often cannot estimate the maximal interval of existence; for that we need to compare the direction fields of equations. Comparison theorems are the general principle behind such estimates.

**Theorem 5.2.1 (First Comparison Theorem)** Let $f(x,y)$ and $F(x,y)$ be continuous in a region $G$ with

$$
f(x,y)<F(x,y),\qquad(x,y)\in G.
$$
Let $y=\varphi(x)$ and $y=\Phi(x)$ be solutions on an interval $(a,b)$ of the initial value problems

$$
y'=f(x,y),\ y(x_0)=y_0\qquad\text{and}\qquad y'=F(x,y),\ y(x_0)=y_0,
$$
respectively, where $(x_0,y_0)\in G$. Then

$$
\varphi(x)<\Phi(x)\quad(x_0<x<b),\qquad\varphi(x)>\Phi(x)\quad(a<x<x_0).
$$

**Proof** Let $g(x)=\Phi(x)-\varphi(x)$. Then $g(x_0)=0$ and $g'(x_0)=F(x_0,y_0)-f(x_0,y_0)>0$, so there is $\delta>0$ with $g(x)>0$ for $x_0<x<x_0+\delta$ and $g(x)<0$ for $x_0-\delta<x<x_0$.

If the conclusion on the right fails, $g$ has a zero in $(x_0,b)$. Let $\zeta$ be the smallest such zero (the zero set is closed, and its distance from $x_0$ is at least $\delta$). Then $g>0$ on $(x_0,\zeta)$ and $g(\zeta)=0$, so $g'(\zeta)=\lim\limits_{x\to\zeta^-}\dfrac{g(x)}{x-\zeta}\le0$. On the other hand, writing $\gamma=\varphi(\zeta)=\Phi(\zeta)$,

$$
g'(\zeta)=F(\zeta,\gamma)-f(\zeta,\gamma)>0,
$$
a contradiction. The left side is similar: if $g$ has a zero in $(a,x_0)$, take the largest zero $\zeta$; then $g<0$ on $(\zeta,x_0)$ and $g'(\zeta)=\lim\limits_{x\to\zeta^+}\dfrac{g(x)}{x-\zeta}\le0$, again a contradiction. $\square$

Geometrically: at an intersection point of the two integral curves, the integral curve of $y'=F$ is always steeper, so it can only cross from below to above, and once it has crossed it can never come back. The same argument handles different initial values.

**Corollary 5.2.1** Under the hypotheses of Theorem 5.2.1, if $\varphi(x_0)<\Phi(x_0)$ (the initial values are no longer required to coincide), then $\varphi(x)<\Phi(x)$ for $x_0<x<b$.

**Proof** The function $g=\Phi-\varphi$ is positive at $x_0$. If it had a zero in $(x_0,b)$, taking the smallest zero $\zeta$ would lead to a contradiction exactly as in the proof of the theorem. $\square$

The strict inequality $f<F$ cannot be weakened to $f\le F$: take $f=F=\lvert y\rvert^{1/2}$; by Example 4.3.1, two different solutions through the origin are not ordered in any definite way. To compare under the condition $f\le F$, we must single out the maximal and minimal solutions among the many solutions.

## 5.3. Maximal and Minimal Solutions

**Definition 5.3.1** Let $f$ be continuous on the rectangle $R$, and let $y=Z(x)$ be a solution on $[x_0,x_0+\sigma]$ of the initial value problem $y'=f(x,y)$, $y(x_0)=y_0$ (Eq. (4.1)). If every solution $y$ of (4.1) on any interval $[x_0,c]\subset[x_0,x_0+\sigma]$ satisfies $y\le Z$, then $Z$ is called the **right maximal solution** of (4.1); replacing $\le$ by $\ge$ defines the **right minimal solution**. The left maximal and left minimal solutions on $[x_0-\sigma,x_0]$ are defined in the same way. A solution on $[x_0-\sigma,x_0+\sigma]$ that is maximal (minimal) on both sides is called the **maximal solution** (**minimal solution**) of (4.1).

By definition, maximal and minimal solutions are unique if they exist.

**Theorem 5.3.1** Let $f$ be continuous on the rectangle $R$ and $\sigma=\min\{a,b/(M+1)\}$. Then the initial value problem (4.1) has a maximal solution $Z$ and a minimal solution $W$ on $[x_0-\sigma,x_0+\sigma]$, and every solution $y$ of (4.1) on a subinterval satisfies

$$
W(x)\le y(x)\le Z(x).
$$

**Proof** For $m=1,2,\dots$ consider the initial value problem $y'=f(x,y)+\dfrac1m$, $y(x_0)=y_0$. On $R$ we have $\lvert f+\frac1m\rvert\le M+1$, so by the Peano existence theorem it has a solution $Z_m$ on $[x_0-\sigma,x_0+\sigma]$ with graph in $R$. The sequence $\{Z_m\}$ is uniformly bounded with the common Lipschitz constant $M+1$, so by the Arzelà–Ascoli theorem (Lemma 4.4.2) a subsequence converges uniformly to some $\tilde Z$. Since $f+\frac1m$ converges uniformly to $f$, $\tilde Z$ is a solution of (4.1), as in the proof of Theorem 4.4.1.

Let $y$ be any solution of (4.1) on $[x_0,c]$. Since $f<f+\frac1m$, the first comparison theorem (whose proof uses only local properties near the initial point and at intersection points, and so applies equally on $R$) gives $y<Z_m$ on $(x_0,c]$, and passing to the limit gives $y\le\tilde Z$. On the left side, the first comparison theorem gives $y>Z_m$, so $y\ge\tilde Z$. Hence $\tilde Z$ is the right maximal solution and at the same time the left minimal solution.

Similarly, the limit of solutions of $y'=f-\frac1m$ gives a function $\tilde W$ that is the right minimal and left maximal solution. Let $Z$ be $\tilde Z$ on the right and $\tilde W$ on the left, and let $W$ be $\tilde W$ on the right and $\tilde Z$ on the left. Both take the value $y_0$ at $x_0$ and satisfy the integral equation (4.2) on both sides, so both are solutions of (4.1); they are the maximal and the minimal solution, respectively. $\square$

By the theorem, the solution of (4.1) is unique if and only if $Z\equiv W$. Maximal and minimal solutions can also be extended to the boundary of $G$ as in Theorem 5.1.1. Moreover, the values at $x$ of all solutions fill exactly the interval $[W(x),Z(x)]$ (Kneser's theorem): for $y'=\lvert y\rvert^{1/2}$ in Example 4.3.1, $Z$ and $W$ are the two curves in the figure that leave the $x$-axis earliest, and the remaining solutions fill the "funnel" between them.

## 5.4. The Second Comparison Theorem

**Lemma 5.4.1** Let $F$ be continuous in a region $G$, and let $\Phi$ be the right maximal solution on $[x_0,x_1]$ of the initial value problem $y'=F(x,y)$, $y(x_0)=y_0$. Let $\Phi_m$ be the noncontinuable solution of $y'=F(x,y)+\dfrac1m$, $y(x_0)=y_0$. Then for $m$ sufficiently large, $\Phi_m$ exists on $[x_0,x_1]$ and converges uniformly to $\Phi$ on $[x_0,x_1]$.

**Proof** The graph of $\Phi$ is a bounded closed subset of $G$, so we can choose $d>0$ such that the "tube" $K=\{(x,y)\mid x_0\le x\le x_1,\ \lvert y-\Phi(x)\rvert\le d\}$ is contained in $G$. Let $M_K=\max_K\lvert F\rvert+1$, and let $c_m$ be the largest $c\le x_1$ such that the graph of $\Phi_m$ over $[x_0,c)$ stays in $K$. Since $\lvert\Phi_m-\Phi\rvert\le2M_K(x-x_0)$ holds inside $K$, we have $c_m\ge x_0+\tau$, where $\tau=\min\{d/(2M_K),x_1-x_0\}$ does not depend on $m$.

We first show that $\varepsilon_m=\sup_{[x_0,c_m)}\lvert\Phi_m-\Phi\rvert\to0$. Otherwise there is a subsequence with $\varepsilon_m\ge\varepsilon>0$ and $c_m\to c^*$. Extending each $\Phi_m$ as a constant beyond $c_m$ gives a sequence on $[x_0,x_1]$ that is uniformly bounded with Lipschitz constant $M_K$, and by the Arzelà–Ascoli theorem a further subsequence converges uniformly to some $\psi$. For $x<c^*$ we have $x<c_m$ for $m$ large, and passing to the limit in the integral equation for $\Phi_m$ shows that $\psi$ is a solution of $y'=F$, $y(x_0)=y_0$ on $[x_0,c^*]$; by maximality, $\psi\le\Phi$. On the other hand, the first comparison theorem gives $\Phi<\Phi_m$, so $\psi\ge\Phi$. Hence $\psi=\Phi$ on $[x_0,c^*]$. Therefore on $[x_0,c_m)$,

$$
\lvert\Phi_m-\Phi\rvert\le\lvert\Phi_m-\psi\rvert+\lvert\psi-\Phi\rvert\le\lvert\Phi_m-\psi\rvert+2M_K\lvert c_m-c^*\rvert\to0
$$
uniformly, contradicting $\varepsilon_m\ge\varepsilon$.

Next we show that $c_m=x_1$ and $\Phi_m$ is defined at $x_1$ for $m$ sufficiently large. Choose $m$ with $\varepsilon_m<d/2$. Then on $[x_0,c_m)$ the graph of $\Phi_m$ stays in the smaller tube $\lvert y-\Phi\rvert\le d/2$, so by the extension theorem the maximal interval of existence of $\Phi_m$ extends beyond $c_m$, and by continuity the graph remains in $K$ for a short while after $c_m$, unless $c_m=x_1$. $\square$

**Theorem 5.4.1 (Second Comparison Theorem)** Let $f(x,y)$ and $F(x,y)$ be continuous in a region $G$ with

$$
f(x,y)\le F(x,y),\qquad(x,y)\in G.
$$
Let $y=\varphi(x)$ be a solution of $y'=f(x,y)$, $y(x_0)=y_0$ on $(a,b)$, and let $y=\Phi(x)$ be the right maximal and left minimal solution of $y'=F(x,y)$, $y(x_0)=y_0$ on $(a,b)$ (on every bounded closed subinterval of $(a,b)$ containing $x_0$). Then

$$
\varphi(x)\le\Phi(x)\quad(x_0\le x<b),\qquad\varphi(x)\ge\Phi(x)\quad(a<x\le x_0).
$$
The same conclusion holds if instead $\varphi$ is assumed to be the right minimal and left maximal solution of $y'=f$ (with no requirement on $\Phi$).

**Proof** Take any $x_1\in(x_0,b)$. By Lemma 5.4.1, the solutions $\Phi_m$ of $y'=F+\frac1m$ converge uniformly to $\Phi$ on $[x_0,x_1]$. Since $f\le F<F+\frac1m$, the first comparison theorem gives $\varphi<\Phi_m$ on $(x_0,x_1]$, and letting $m\to\infty$ gives $\varphi\le\Phi$. The argument on the left is symmetric: by the first comparison theorem, on the left $\Phi_m$ is less than every solution of $y'=F$, and the symmetric form of Lemma 5.4.1 shows that the $\Phi_m$ converge to the left minimal solution $\Phi$; since $\varphi>\Phi_m$, passing to the limit gives $\varphi\ge\Phi$. Under the second set of assumptions, we approximate $\varphi$ instead by solutions of $y'=f-\frac1m$. $\square$

When solutions are unique, the unique solution is of course both the maximal and the minimal solution, which gives the form used most often.

**Corollary 5.4.1** Let $f\le F$ be continuous in $G$, and let one of $f$ and $F$ satisfy a local Lipschitz condition with respect to $y$. If $\varphi$ and $\Phi$ are solutions of $y'=f$ and $y'=F$ respectively through $(x_0,y_0)$, then on their common interval $\varphi\le\Phi$ for $x\ge x_0$ and $\varphi\ge\Phi$ for $x\le x_0$.

**Example 5.4.1** Estimate the maximal interval of existence $(\alpha,\beta)$ of the initial value problem $y'=x^2+y^2$, $y(0)=0$. The right-hand side is continuously differentiable, so the solution $\varphi$ is unique; since $-\varphi(-x)$ is also a solution of the same initial value problem, $\varphi$ is an odd function and $\alpha=-\beta$. For $x>0$ we have $\varphi'\ge x^2>0$, so $\varphi(x)>0$.

Lower bound: take any $0<x_1<\sqrt{\pi/2}$. In the strip $G=\{\lvert x\rvert<x_1\}$ we have $x^2+y^2\le x_1^2+y^2$, and the solution $\Phi=x_1\tan(x_1x)$ of $y'=x_1^2+y^2$, $y(0)=0$ is bounded on $[0,x_1]$ (because $x_1^2<\pi/2$). By Corollary 5.4.1, $0<\varphi\le\Phi$ on $[0,\min\{\beta,x_1\})$. If $\beta<x_1$, then $\varphi$ would be bounded near $\beta$, contradicting Corollary 5.1.1. Hence $\beta\ge x_1$, and therefore $\beta\ge\sqrt{\pi/2}\approx1.253$.

Upper bound: from $\varphi'\ge x^2$ we get $\varphi(1)\ge\dfrac13$. In $G=\{x>0\}$ take $f(x,y)=\min\{x^2,1\}+y^2\le x^2+y^2$, which equals $1+y^2$ for $x\ge1$. The solution of $y'=1+y^2$, $y(1)=\varphi(1)$,

$$
\psi=\tan\big(x-1+\arctan\varphi(1)\big),
$$
tends to $+\infty$ at $x^*=1+\dfrac\pi2-\arctan\varphi(1)$. By Corollary 5.4.1, $\varphi\ge\psi$ for $x\ge1$, so $\varphi$ cannot pass beyond $x^*$:

$$
\beta\le1+\frac\pi2-\arctan\frac13\approx2.249.
$$
Numerical computation gives $\beta\approx2.003$. This solution cannot be expressed in elementary functions (it can be expressed through Bessel functions), yet the comparison theorems directly give two-sided estimates for its interval of existence.

![The (numerically computed) solution of y' = x^2 + y^2, y(0) = 0 lies between two comparison functions: the upper one, x_1 tan(x_1 x) with x_1 = 1.25, shows that the solution exists at least up to sqrt(pi/2); the lower one, tan(x - 1 + arctan phi(1)) starting at x = 1, shows that the solution blows up before 2.249](./plots/comparison-bounds.py)

## Summary

| Result | Hypotheses | Use |
|---|---|---|
| Extension theorem (Theorem 5.1.1) | $f$ continuous in an open region $G$ | The integral curve of a noncontinuable solution extends to the boundary of $G$ |
| Blow-up (Corollary 5.1.1) | $G$ a strip | A solution ending inside the strip must tend to infinity |
| Global existence (Theorem 5.1.2) | $\lvert f\rvert\le A(x)\lvert y\rvert+B(x)$ | Solutions exist on the whole interval |
| First comparison theorem (Theorem 5.2.1) | $f<F$ | Solutions through a common point: $\varphi<\Phi$ on the right, $\varphi>\Phi$ on the left |
| Maximal and minimal solutions (Theorem 5.3.1) | $f$ continuous | All solutions lie between $W$ and $Z$ |
| Second comparison theorem (Theorem 5.4.1) | $f\le F$, comparison with maximal (minimal) solutions | Estimates of solutions and of the maximal interval of existence |
