---
title: Stability and Qualitative Theory
source_hash: 1fa2925554af
---

Most nonlinear equations cannot be solved in closed form, yet in applications what matters is often not a formula for the solution but its long-term behavior: whether an equilibrium recovers from a small perturbation, whether the system settles into a sustained oscillation, where the trajectories eventually go. Qualitative theory answers these questions directly from the equation, without solving it. The approach was founded by Poincaré and Lyapunov at the end of the nineteenth century and today underlies dynamical systems, control theory and mathematical biology.

This chapter first defines Lyapunov stability, uses the linear theory of the previous chapters ([2.4.8](/2.4.8)) to characterize completely the stability of linear systems with constant coefficients, and gives the Routh–Hurwitz criterion, which looks only at the coefficients of the characteristic polynomial. We then prove that the stability of an equilibrium of a nonlinear system can be decided from its linear approximation (Lyapunov's first method), and present the method of Lyapunov functions, which needs no linearization (the second method). The second half treats planar autonomous systems: the phase plane and trajectories, the classification of equilibria of planar linear systems, and limit cycles and the Poincaré–Bendixson theorem, with the van der Pol equation as an example. The equilibria and phase portraits of population competition and predator–prey models ([Ecology](/7.19)) are direct applications of these methods.

## 11.1. Lyapunov Stability

### 11.1.1. Definitions

Consider the system

$$
\boldsymbol{x}'=\boldsymbol{f}(t,\boldsymbol{x}),\tag{11.1}
$$
where $\boldsymbol{f}$ is continuous on $t\ge t_0$, $\|\boldsymbol{x}\|<H$ and satisfies a local **Lipschitz condition** in $\boldsymbol{x}$, so that solutions of the initial value problem exist and are unique ([2.4.4](/2.4.4), [2.4.7](/2.4.7)). We want to study how a given solution $\boldsymbol{\varphi}(t)$ behaves under perturbations of the initial value. Setting $\boldsymbol{y}=\boldsymbol{x}-\boldsymbol{\varphi}(t)$ gives $\boldsymbol{y}'=\boldsymbol{f}(t,\boldsymbol{y}+\boldsymbol{\varphi})-\boldsymbol{f}(t,\boldsymbol{\varphi})$, whose right-hand side vanishes at $\boldsymbol{y}=\boldsymbol{0}$, and $\boldsymbol{\varphi}$ corresponds to the zero solution. We may therefore always assume $\boldsymbol{f}(t,\boldsymbol{0})\equiv\boldsymbol{0}$ and study the zero solution $\boldsymbol{x}\equiv\boldsymbol{0}$. We write $\boldsymbol{x}(t;t_0,\boldsymbol{x}_0)$ for the solution satisfying $\boldsymbol{x}(t_0)=\boldsymbol{x}_0$.

**Definition 11.1.1** Suppose $\boldsymbol{f}(t,\boldsymbol{0})\equiv\boldsymbol{0}$.

1. If for every $\varepsilon>0$ there exists $\delta>0$ such that, whenever $\|\boldsymbol{x}_0\|<\delta$, the solution $\boldsymbol{x}(t;t_0,\boldsymbol{x}_0)$ exists on $[t_0,+\infty)$ and satisfies $\|\boldsymbol{x}(t;t_0,\boldsymbol{x}_0)\|<\varepsilon$ for $t\ge t_0$, then the zero solution is said to be **Lyapunov stable** (or simply stable);
2. If the zero solution is stable and there exists $\delta_0>0$ such that $\lim_{t\to+\infty}\boldsymbol{x}(t;t_0,\boldsymbol{x}_0)=\boldsymbol{0}$ whenever $\|\boldsymbol{x}_0\|<\delta_0$, then the zero solution is said to be **asymptotically stable**;
3. If the zero solution is not stable, it is said to be unstable.

Stability means that "a small perturbation of the initial value causes only a small deviation of the solution over the entire infinite time interval". This is much stronger than continuous dependence of solutions on initial values, which holds only on finite intervals ([2.4.7](/2.4.7)).

**Example 11.1.1** Here are a few one-dimensional examples.

- $x'=-x$: $x=x_0\mathrm{e}^{-(t-t_0)}$, and the zero solution is asymptotically stable;
- $x'=0$: $x\equiv x_0$, which is stable but not asymptotically stable;
- $x'=x$: $x=x_0\mathrm{e}^{t-t_0}$, which is unstable;
- $x'=-x^3$: $x^{-2}=x_0^{-2}+2(t-t_0)$, so $\lvert x\rvert$ decreases monotonically to $0$; the zero solution is asymptotically stable, but the decay is slower than exponential. The zero solution of $x'=x^3$ is unstable (solutions blow up in finite time).

The last two equations both have the linear approximation $x'=0$, which shows that the linear approximation sometimes cannot decide stability (the critical case of Theorem 11.4.1).

The stability requirement in the definition of asymptotic stability cannot be dropped: there are planar autonomous systems in which every solution tends to the origin, yet some solutions starting arbitrarily close to the origin first move away to a fixed distance before returning (Vinograd's example).

### 11.1.2. Stability of Linear Systems

For a linear system $\boldsymbol{x}'=A(t)\boldsymbol{x}+\boldsymbol{f}(t)$, the difference of two solutions satisfies the homogeneous system, so the stability of any solution is the same as that of the zero solution of the homogeneous system, and we may speak of "a stable linear system".

**Theorem 11.1.1** Let $A(t)$ be continuous on $[t_0,+\infty)$ and let $\Phi(t)$ be a fundamental matrix of $\boldsymbol{x}'=A(t)\boldsymbol{x}$. Then the zero solution is

1. stable $\Leftrightarrow$ all solutions are bounded on $[t_0,+\infty)$ $\Leftrightarrow$ $\Phi(t)$ is bounded on $[t_0,+\infty)$;
2. asymptotically stable $\Leftrightarrow$ all solutions tend to $\boldsymbol{0}$ as $t\to+\infty$ $\Leftrightarrow$ $\Phi(t)\to O$.

**Proof** The solutions are $\boldsymbol{x}(t)=\Phi(t)\Phi^{-1}(t_0)\boldsymbol{x}_0$. If $\|\Phi(t)\|\le K$, then $\|\boldsymbol{x}(t)\|\le K\|\Phi^{-1}(t_0)\|\,\|\boldsymbol{x}_0\|$, and taking $\delta=\varepsilon/(K\|\Phi^{-1}(t_0)\|+1)$ gives stability. Conversely, if the zero solution is stable, take the $\delta$ corresponding to $\varepsilon=1$; then $\|\boldsymbol{x}(t)\|<1$ for $\|\boldsymbol{x}_0\|<\delta$, so by linearity every solution is bounded, and so are the columns of $\Phi$. Part 2 is similar: for a linear system, "solutions with small initial values tend to zero" is equivalent to "all solutions tend to zero". $\square$

For systems with constant coefficients, the structure of $\Phi=\mathrm{e}^{tA}$ is given by Corollary 8.5.1, and hence:

**Theorem 11.1.2** The zero solution of the constant-coefficient system $\boldsymbol{x}'=A\boldsymbol{x}$ is

1. asymptotically stable $\Leftrightarrow$ all **eigenvalues** of $A$ have negative real parts; in this case there exist $C,\alpha>0$ with $\|\mathrm{e}^{tA}\|\le C\mathrm{e}^{-\alpha t}$ for $t\ge0$, which is called exponential stability;
2. stable $\Leftrightarrow$ all eigenvalues have real parts $\le0$, and the eigenvalues with zero real part are all **semisimple eigenvalues** (their Jordan blocks are all of size one);
3. unstable in all other cases.

**Proof** By Corollary 8.5.1, the entries of $\mathrm{e}^{tA}$ are linear combinations of $t^k\mathrm{e}^{\lambda_jt}$, with $k$ less than the size of the largest Jordan block of $\lambda_j$. If all $\operatorname{Re}\lambda_j<0$, take $0<\alpha<-\max\operatorname{Re}\lambda_j$; the estimate of Corollary 8.5.1 (with $\varepsilon=-\max\operatorname{Re}\lambda_j-\alpha$) gives the exponential bound. If the real parts are $\le0$ and the purely imaginary eigenvalues have only blocks of size one, every term is bounded. Conversely, if some $\operatorname{Re}\lambda>0$, an eigenvector $\boldsymbol{r}$ gives the unbounded solution $\mathrm{e}^{\lambda t}\boldsymbol{r}$; if some $\lambda$ with $\operatorname{Re}\lambda=0$ has a Jordan block of size at least two, a Jordan chain gives the unbounded solution $\mathrm{e}^{\lambda t}(t\boldsymbol{p}_1+\boldsymbol{p}_2)$; and if some $\operatorname{Re}\lambda\ge0$, then $\mathrm{e}^{\lambda t}\boldsymbol{r}$ does not tend to zero. The conclusion follows from Theorem 11.1.1. $\square$

The stability of an $n$th-order equation with constant coefficients $y^{(n)}+a_1y^{(n-1)}+\cdots+a_ny=0$ means the stability of the system for $\boldsymbol{x}=(y,\dots,y^{(n-1)})^{\mathsf T}$. Each eigenvalue of the companion matrix has only one Jordan block (Proposition 9.4.1), so: all solutions (together with their derivatives) tend to zero $\Leftrightarrow$ all **characteristic roots** have negative real parts; all solutions are bounded $\Leftrightarrow$ the characteristic roots have real parts $\le0$ and those with zero real part are simple.

**Example 11.1.2** For $y''+py'+qy=0$ ($p,q$ real constants), we discuss the behavior of solutions as $x\to+\infty$. The characteristic roots are $\lambda_{1,2}=-\frac p2\pm\sqrt{\Delta}$ with $\Delta=\frac{p^2-4q}{4}$.

1. All solutions $\to0$ $\Leftrightarrow$ $p>0$ and $q>0$. If $\Delta>0$, both real roots are negative $\Leftrightarrow$ their sum $-p<0$ and product $q>0$; if $\Delta=0$, the double root $-\frac p2<0$ $\Leftrightarrow$ $p>0$ (and then $q=\frac{p^2}4>0$); if $\Delta<0$, the real part $-\frac p2<0$ $\Leftrightarrow$ $p>0$, while $\Delta<0$ implies $q>0$.
2. All solutions are bounded on $[0,+\infty)$ $\Leftrightarrow$ $p\ge0$, $q\ge0$, and $p,q$ are not both zero. Compared with 1, the additional cases are $p=0,q>0$ (roots $\pm\mathrm{i}\sqrt q$, simple) and $p>0,q=0$ (roots $0,-p$, with $0$ simple); for $p=q=0$ there is the solution $y=x$.
3. All solutions are bounded on $(-\infty,+\infty)$ $\Leftrightarrow$ $p=0$ and $q>0$. Applying 2 to $x$ and to $-x$ (under which the equation becomes $y''-py'+qy=0$) requires $p\ge0$, $-p\ge0$, $q\ge0$ and $(p,q)\ne(0,0)$, that is, $p=0,q>0$; then $y=A\sin(\sqrt q\,x+\theta)$ is periodic and indeed bounded.

## 11.2. The Routh–Hurwitz Criterion

By Theorem 11.1.2, asymptotic stability of a constant-coefficient equation reduces to whether all roots of the characteristic polynomial lie in the left half-plane. The Routh–Hurwitz criterion decides this without computing the roots.

**Definition 11.2.1** A real polynomial all of whose roots have negative real parts is called a **stable polynomial** (or Hurwitz polynomial).

**Proposition 11.2.1** If $f(\lambda)=\lambda^n+a_1\lambda^{n-1}+\cdots+a_n$ is a stable polynomial, then all $a_k>0$.

**Proof** A real polynomial factors into linear factors $\lambda+c$ (real root $-c<0$, so $c>0$) and quadratic factors $(\lambda-\alpha)^2+\beta^2=\lambda^2-2\alpha\lambda+\alpha^2+\beta^2$ (complex roots $\alpha\pm\mathrm{i}\beta$ with $\alpha<0$). Each factor has positive coefficients, and so does their product. $\square$

For $n\le2$ the condition is also sufficient (Example 11.1.2), but for $n\ge3$ it is not: $\lambda^3+\lambda^2+\lambda+1=(\lambda+1)(\lambda^2+1)$ has purely imaginary roots.

**Theorem 11.2.1 (Hurwitz)** Let $f(\lambda)=\lambda^n+a_1\lambda^{n-1}+\cdots+a_n$ be a real polynomial, and set $a_0=1$ and $a_k=0$ for $k<0$ or $k>n$. Form the $n\times n$ Hurwitz matrix $H=(a_{2i-j})_{i,j=1}^n$:

$$
H=\begin{bmatrix}a_1&a_0&0&0&\cdots&0\\a_3&a_2&a_1&a_0&\cdots&0\\a_5&a_4&a_3&a_2&\cdots&0\\\vdots&\vdots&\vdots&\vdots&&\vdots\\0&0&0&0&\cdots&a_n\end{bmatrix}.
$$
Then $f$ is a stable polynomial if and only if all leading principal minors of $H$ are positive:

$$
\Delta_1=a_1>0,\quad\Delta_2=\begin{vmatrix}a_1&1\\a_3&a_2\end{vmatrix}>0,\quad\Delta_3=\begin{vmatrix}a_1&1&0\\a_3&a_2&a_1\\a_5&a_4&a_3\end{vmatrix}>0,\quad\dots,\quad\Delta_n=a_n\Delta_{n-1}>0.
$$

The proof is long and relies on the argument principle of complex analysis or on Sturm sequences; we omit it. The last column of $H$ has only one nonzero entry, $a_n$ in the lower right corner, so $\Delta_n=a_n\Delta_{n-1}$.

**Example 11.2.1** Stability conditions for low-degree polynomials:

| $n$ | Necessary and sufficient condition for $f(\lambda)$ to be stable |
|---|---|
| 2 | $a_1>0$, $a_2>0$ |
| 3 | $a_1>0$, $a_3>0$, $a_1a_2>a_3$ |
| 4 | $a_1>0$, $a_4>0$, $a_1a_2>a_3$, $a_1a_2a_3>a_1^2a_4+a_3^2$ |
| 5 | $a_1>0$, $a_5>0$, $a_1a_2>a_3$, $a_1(a_2a_3-a_1a_4+a_5)>a_3^2$, $a_1(a_2a_3a_4-a_2^2a_5-a_1a_4^2+2a_4a_5)-a_3^2a_4+a_2a_3a_5-a_5^2>0$ |

For example, for $n=3$ we have $\Delta_2=a_1a_2-a_3$ and $\Delta_3=a_3\Delta_2$, and the three conditions $a_1>0$, $\Delta_2>0$, $a_3>0$ already imply $a_2>0$. In general, stability of a polynomial of degree $n$ is characterized by $n$ independent inequalities.

In practice one often uses the equivalent Routh array. The first two rows are $a_0,a_2,a_4,\dots$ and $a_1,a_3,a_5,\dots$, and each subsequent row is computed from the two rows above it: if these are $u_1,u_2,\dots$ and $v_1,v_2,\dots$, the new row is $w_i=\dfrac{v_1u_{i+1}-u_1v_{i+1}}{v_1}$ (missing entries are taken to be 0). The polynomial $f$ is stable if and only if all entries of the first column of the array ($n+1$ numbers in all) are positive.

**Example 11.2.2** Find the condition for $y'''+2y''+3y'+ky=0$ to be asymptotically stable. Here $a_1=2$, $a_2=3$, $a_3=k$, and the conditions are $k>0$ and $2\cdot3>k$, that is, $0<k<6$. With the Routh array:

$$
\begin{matrix}1&3\\2&k\\\frac{6-k}{2}&0\\k&\end{matrix}
$$
The first column $1,2,\frac{6-k}2,k$ is positive exactly when $0<k<6$, as before. For $k=6$, $f(\lambda)=(\lambda+2)(\lambda^2+3)$ has the purely imaginary roots $\pm\sqrt3\,\mathrm{i}$, and the solutions contain sustained oscillations; this is the typical way in which too high a gain destabilizes a control system.

## 11.3. Stability from the Linear Approximation

Suppose the system can be written as

$$
\boldsymbol{x}'=A\boldsymbol{x}+\boldsymbol{g}(t,\boldsymbol{x}),\qquad\|\boldsymbol{g}(t,\boldsymbol{x})\|\le\gamma(\|\boldsymbol{x}\|)\,\|\boldsymbol{x}\|,\quad\lim_{r\to0^+}\gamma(r)=0,\tag{11.2}
$$
that is, $\boldsymbol{g}$ is $o(\|\boldsymbol{x}\|)$ uniformly in $t$; here $A$ is a constant matrix and $\boldsymbol{g}$ is continuous and locally Lipschitz in $\boldsymbol{x}$. The system $\boldsymbol{x}'=A\boldsymbol{x}$ is called the linear approximation (first approximation) of Eq. (11.2).

**Theorem 11.3.1 (Lyapunov's First Method)** 

1. If all eigenvalues of $A$ have negative real parts, the zero solution of Eq. (11.2) is asymptotically stable, and there exist $\delta,C,\beta>0$ such that $\|\boldsymbol{x}(t)\|\le C\|\boldsymbol{x}_0\|\mathrm{e}^{-\beta(t-t_0)}$ whenever $\|\boldsymbol{x}_0\|<\delta$;
2. If $A$ has an eigenvalue with positive real part, the zero solution of Eq. (11.2) is unstable;
3. If all eigenvalues have real parts $\le0$ and some have zero real part, the linear approximation cannot decide stability (the critical case).

**Proof** 1: By Theorem 11.1.2 there exist $C\ge1$ and $\alpha>0$ with $\|\mathrm{e}^{tA}\|\le C\mathrm{e}^{-\alpha t}$ for $t\ge0$. Choose $r_0>0$ such that $\gamma(r)\le\frac{\alpha}{2C}$ for $0<r\le r_0$, and let $\delta=r_0/C$. Let $\|\boldsymbol{x}_0\|<\delta$. As long as the solution satisfies $\|\boldsymbol{x}(s)\|\le r_0$ for $t_0\le s\le t$, the variation of constants formula (8.5) gives

$$
\|\boldsymbol{x}(t)\|\le C\mathrm{e}^{-\alpha(t-t_0)}\|\boldsymbol{x}_0\|+\int_{t_0}^tC\mathrm{e}^{-\alpha(t-s)}\frac{\alpha}{2C}\|\boldsymbol{x}(s)\|\,\mathrm{d}s.
$$
Setting $u(t)=\mathrm{e}^{\alpha(t-t_0)}\|\boldsymbol{x}(t)\|$, we get $u(t)\le C\|\boldsymbol{x}_0\|+\frac\alpha2\int_{t_0}^tu(s)\,\mathrm{d}s$. By Grönwall's inequality ([2.4.7](/2.4.7)), $u(t)\le C\|\boldsymbol{x}_0\|\mathrm{e}^{\frac\alpha2(t-t_0)}$, that is,

$$
\|\boldsymbol{x}(t)\|\le C\|\boldsymbol{x}_0\|\mathrm{e}^{-\frac\alpha2(t-t_0)}<r_0.
$$
Hence the solution never reaches the sphere $\|\boldsymbol{x}\|=r_0$ (if $t_1$ were the first time it did, the estimate would hold on $[t_0,t_1]$, giving $\|\boldsymbol{x}(t_1)\|<r_0$, a contradiction). By the extension theorem ([2.4.5](/2.4.5)), the solution exists on $[t_0,+\infty)$ and the estimate holds for all $t\ge t_0$, with $\beta=\frac\alpha2$. For stability, given $\varepsilon>0$ take $\delta'=\min(r_0,\varepsilon)/C$.

The proof of 2 uses the instability theorem of the next section with a quadratic Lyapunov function; we omit it. For 3, see Examples 11.1.1 and 11.4.2. $\square$

Now consider an autonomous system $\boldsymbol{x}'=\boldsymbol{f}(\boldsymbol{x})$ with $\boldsymbol{f}\in C^1$.

**Definition 11.3.1** A point $\boldsymbol{x}^*$ with $\boldsymbol{f}(\boldsymbol{x}^*)=\boldsymbol{0}$ is called an **equilibrium point** (or singular point) of the autonomous system; $\boldsymbol{x}\equiv\boldsymbol{x}^*$ is a constant solution. If the **Jacobian matrix** $D\boldsymbol{f}(\boldsymbol{x}^*)$ has no eigenvalues with zero real part, $\boldsymbol{x}^*$ is called a **hyperbolic equilibrium point**.

Setting $\boldsymbol{y}=\boldsymbol{x}-\boldsymbol{x}^*$, Taylor's formula gives $\boldsymbol{f}(\boldsymbol{x}^*+\boldsymbol{y})=D\boldsymbol{f}(\boldsymbol{x}^*)\boldsymbol{y}+o(\|\boldsymbol{y}\|)$, which is of the form (11.2). Therefore:

**Corollary 11.3.1** Let $\boldsymbol{f}\in C^1$ and let $\boldsymbol{x}^*$ be an equilibrium point. If all eigenvalues of $D\boldsymbol{f}(\boldsymbol{x}^*)$ have negative real parts, then $\boldsymbol{x}^*$ is asymptotically stable; if some eigenvalue has positive real part, then $\boldsymbol{x}^*$ is unstable.

Near a hyperbolic equilibrium point, the trajectories of the nonlinear system have the same structure as those of the linear approximation up to a homeomorphism (the Hartman–Grobman theorem, stated without proof).

**Example 11.3.1** The damped pendulum $\theta''+k\theta'+\sin\theta=0$ ($k\ge0$) can be written as $x'=y$, $y'=-\sin x-ky$. The equilibrium points are $(m\pi,0)$, $m\in\mathbb{Z}$.

- At $(0,0)$, $D\boldsymbol{f}=\begin{bmatrix}0&1\\-1&-k\end{bmatrix}$ with characteristic polynomial $\lambda^2+k\lambda+1$. For $k>0$ the real parts are negative and the hanging equilibrium is asymptotically stable; for $k=0$ the eigenvalues are $\pm\mathrm{i}$, the critical case (by Example 11.4.1 it is stable).
- At $(\pi,0)$, $D\boldsymbol{f}=\begin{bmatrix}0&1\\1&-k\end{bmatrix}$ with $\det=-1<0$, so there is a positive eigenvalue and the inverted equilibrium is unstable.

![Phase portraits of the pendulum. Left: undamped, θ'' + sin θ = 0; the orbits near the origin are closed (a center), (±π, 0) are saddles, and the thick curves are the separatrices joining the saddles. Right: damped, k = 0.25; the origin becomes a stable focus, and the separatrices divide the phase plane into regions tending to different equilibria (2mπ, 0)](./plots/pendulum-phase-portrait.py)

## 11.4. The Method of Lyapunov Functions

### 11.4.1. Stability Theorems

The linear approximation fails in the critical case, and it also gives no information on the size of the region of attraction. Lyapunov's second method generalizes the idea of energy: if some "energy" does not increase along trajectories, the equilibrium is stable. Consider the autonomous system

$$
\boldsymbol{x}'=\boldsymbol{f}(\boldsymbol{x}),\qquad\boldsymbol{f}(\boldsymbol{0})=\boldsymbol{0},\tag{11.3}
$$
where $\boldsymbol{f}$ is locally Lipschitz in a neighborhood $\Omega$ of the origin.

**Definition 11.4.1** Let $V$ be continuously differentiable in $\Omega$ with $V(\boldsymbol{0})=0$. If $V(\boldsymbol{x})>0$ for $\boldsymbol{x}\ne\boldsymbol{0}$, then $V$ is called a **positive definite function**; if $-V$ is positive definite, $V$ is called negative definite; if $V\ge0$ ($V\le0$), $V$ is called positive semidefinite (negative semidefinite). The function

$$
\dot V(\boldsymbol{x})=\nabla V(\boldsymbol{x})\cdot\boldsymbol{f}(\boldsymbol{x})=\sum_i\frac{\partial V}{\partial x_i}f_i(\boldsymbol{x})
$$
is called the derivative of $V$ along the system (11.3) (the orbital derivative).

By the chain rule, for a solution $\boldsymbol{x}(t)$ of Eq. (11.3) we have $\frac{\mathrm{d}}{\mathrm{d}t}V(\boldsymbol{x}(t))=\dot V(\boldsymbol{x}(t))$: we know how $V$ changes along solutions without having to find them.

**Theorem 11.4.1 (Lyapunov)** Let $V$ be positive definite in $\Omega$.

1. If $\dot V(\boldsymbol{x})\le0$ for $\boldsymbol{x}\in\Omega$, the zero solution is stable;
2. If $\dot V$ is negative definite, the zero solution is asymptotically stable.

A function $V$ satisfying 1 or 2 is called a *Lyapunov function*.

**Proof** 1: Take any $\varepsilon>0$ such that the closed ball $\|\boldsymbol{x}\|\le\varepsilon$ lies in $\Omega$. On the sphere $\|\boldsymbol{x}\|=\varepsilon$, $V$ is continuous and positive, with minimum $m>0$. Since $V(\boldsymbol{0})=0$ and $V$ is continuous, there is $\delta\in(0,\varepsilon)$ such that $V(\boldsymbol{x})<m$ for $\|\boldsymbol{x}\|<\delta$. Let $\|\boldsymbol{x}_0\|<\delta$. As long as the solution stays in the ball, $V(\boldsymbol{x}(t))$ is nonincreasing, so $V(\boldsymbol{x}(t))\le V(\boldsymbol{x}_0)<m$ and the solution never reaches the sphere. Hence the solution remains in a compact set, extends to $[t_0,+\infty)$, and satisfies $\|\boldsymbol{x}(t)\|<\varepsilon$.

2: By 1 the zero solution is stable; take $\varepsilon$ and the corresponding $\delta$, and let $\|\boldsymbol{x}_0\|<\delta$. Then $V(\boldsymbol{x}(t))$ decreases monotonically and has a limit $c\ge0$. If $c>0$, continuity of $V$ gives $\rho>0$ with $\|\boldsymbol{x}(t)\|\ge\rho$ for all $t$; on the compact set $\rho\le\|\boldsymbol{x}\|\le\varepsilon$, $\dot V$ has a negative maximum $-\mu$, so $V(\boldsymbol{x}(t))\le V(\boldsymbol{x}_0)-\mu(t-t_0)\to-\infty$, a contradiction. Hence $V(\boldsymbol{x}(t))\to0$. For any $\eta\in(0,\varepsilon)$, $V$ has a positive minimum on $\eta\le\|\boldsymbol{x}\|\le\varepsilon$, and $V(\boldsymbol{x}(t))$ eventually falls below it, so $\|\boldsymbol{x}(t)\|$ is eventually less than $\eta$; that is, $\boldsymbol{x}(t)\to\boldsymbol{0}$. $\square$

**Theorem 11.4.2 (Instability, Chetaev)** Let $V$ be continuously differentiable in $\Omega$ with $V(\boldsymbol{0})=0$, suppose every neighborhood of the origin contains points where $V>0$, and suppose $\dot V$ is positive definite in $\Omega$. Then the zero solution is unstable.

**Proof** (Sketch.) Take $\boldsymbol{x}_0$ arbitrarily close to the origin with $V(\boldsymbol{x}_0)>0$. Since $V(\boldsymbol{x}(t))$ increases monotonically, the solution leaves some neighborhood of the origin; otherwise $\dot V$ would have a positive lower bound in the region where $V\ge V(\boldsymbol{x}_0)$, and $V(\boldsymbol{x}(t))\to+\infty$, contradicting the boundedness of $V$ on a compact set. $\square$

**Theorem 11.4.3 (LaSalle's Invariance Principle)** Let $V$ be positive definite with $\dot V\le0$, and suppose the set $E=\{\boldsymbol{x}\in\Omega:\dot V(\boldsymbol{x})=0\}$ contains no entire positive semi-trajectory of Eq. (11.3) other than the origin. Then the zero solution is asymptotically stable (stated without proof).

### 11.4.2. Examples

**Example 11.4.1** For the pendulum $x'=y$, $y'=-\sin x-ky$ ($k\ge0$), the energy $V=\frac12y^2+(1-\cos x)$ is positive definite in $\lvert x\rvert<2\pi$, and

$$
\dot V=y\cdot(-\sin x-ky)+\sin x\cdot y=-ky^2\le0.
$$
By Theorem 11.4.1 the origin is stable, which settles the critical case $k=0$. For $k>0$, $\dot V$ is only negative semidefinite (it vanishes on the $x$-axis), so part 2 of Theorem 11.4.1 does not apply. However, on the $x$-axis we have $y=0$ and $y'=-\sin x\ne0$ ($x\ne0$), so no trajectory can stay in $E=\{y=0\}$, and by LaSalle's invariance principle the origin is asymptotically stable, in agreement with Example 11.3.1.

**Example 11.4.2** The linear approximation $\begin{bmatrix}0&-1\\1&0\end{bmatrix}$ of the system

$$
x'=-y-x^3,\qquad y'=x-y^3
$$
has eigenvalues $\pm\mathrm{i}$, which is the critical case. Taking $V=x^2+y^2$,

$$
\dot V=2x(-y-x^3)+2y(x-y^3)=-2(x^4+y^4)
$$
is negative definite, so the zero solution is asymptotically stable: the center of the linearization is turned into a stable focus by the nonlinear terms. Replacing $-x^3,-y^3$ by $+x^3,+y^3$ gives $\dot V=2(x^4+y^4)$, which is positive definite, and the zero solution is unstable by Chetaev's theorem. The linear approximations are identical but the stability is opposite; this is what "the critical case cannot be decided" means.

**Example 11.4.3** For the linear system $\boldsymbol{x}'=A\boldsymbol{x}$, consider a quadratic Lyapunov function $V=\boldsymbol{x}^{\mathsf T}P\boldsymbol{x}$: then $\dot V=\boldsymbol{x}^{\mathsf T}(A^{\mathsf T}P+PA)\boldsymbol{x}$. One can show that all eigenvalues of $A$ have negative real parts if and only if, for some (equivalently, every) **positive definite matrix** $Q$, the Lyapunov equation $A^{\mathsf T}P+PA=-Q$ has a positive definite solution $P$ (stated without proof). This $V$ remains a Lyapunov function near the origin for the nonlinear system (11.2), which gives another proof of part 1 of Theorem 11.3.1, and every small ellipsoid $V<c$ lies in the region of attraction.

There is no general method for constructing Lyapunov functions. For physical systems one often takes the energy, and for ecological models functions such as $\sum_i(x_i-x_i^*-x_i^*\ln\frac{x_i}{x_i^*})$.

## 11.5. Planar Autonomous Systems

### 11.5.1. The Phase Plane and Trajectories

In this section and the next we consider the planar autonomous system

$$
x'=P(x,y),\qquad y'=Q(x,y),\tag{11.4}
$$
where $P,Q$ are continuously differentiable in a region $G\subset\mathbb{R}^2$.

**Definition 11.5.1** The plane of the variables $(x,y)$ is called the **phase plane** of Eq. (11.4). The oriented curve traced out in the phase plane by a solution $(x(t),y(t))$ of Eq. (11.4) is called a **trajectory**, and its part with $t\ge t_0$ is called a positive semi-trajectory. The picture of all trajectories is called the **phase portrait** of Eq. (11.4).

A solution is an **integral curve** in $(t,x,y)$-space, and the trajectory is its projection onto the phase plane. Since the right-hand side of an autonomous system does not depend on $t$, the vector field $(P,Q)$ gives the tangent direction of the trajectory at each point, which gives trajectories good properties:

**Theorem 11.5.1** 

1. If $(x(t),y(t))$ is a solution, then so is $(x(t+c),y(t+c))$ for every constant $c$, and the two have the same trajectory;
2. Through each point of $G$ there passes exactly one trajectory, and distinct trajectories do not intersect;
3. An equilibrium point is itself a trajectory; a trajectory starting at a non-equilibrium point cannot reach an equilibrium point in finite time;
4. A trajectory (other than an equilibrium point) is a closed curve if and only if the corresponding solution is a nonconstant periodic solution.

**Proof** 1: $(x(t+c))'=P(x(t+c),y(t+c))$, and the right-hand side does not contain $t$ explicitly. 2: If two trajectories both pass through a point $\boldsymbol{p}$, say $\boldsymbol{x}_1(t_1)=\boldsymbol{x}_2(t_2)=\boldsymbol{p}$, then $\boldsymbol{x}_1(t+t_1-t_2)$ and $\boldsymbol{x}_2(t)$ are solutions with the same value at $t_2$; by uniqueness they are equal, and the trajectories coincide. 3: If $\boldsymbol{x}(t_1)=\boldsymbol{x}^*$, then $\boldsymbol{x}\equiv\boldsymbol{x}^*$ by uniqueness. 4: If the trajectory is closed, there is $T>0$ with $\boldsymbol{x}(t_0+T)=\boldsymbol{x}(t_0)$; then $\boldsymbol{x}(t+T)$ and $\boldsymbol{x}(t)$ have the same value at $t_0$ and are equal by uniqueness. $\square$

Where $P\ne0$, the trajectories satisfy the first-order equation $\dfrac{\mathrm{d}y}{\mathrm{d}x}=\dfrac{Q(x,y)}{P(x,y)}$, so they can be found by the methods of the earlier chapters (but without the time parametrization). For example, the trajectories of $x'=y$, $y'=-x$ satisfy $x\,\mathrm{d}x+y\,\mathrm{d}y=0$, that is, they are the circles $x^2+y^2=C$. In general, if $H(x,y)$ is constant along solutions (a first integral, [2.4.14](/2.4.14)), the trajectories lie on the level curves $H=C$. The energy of the undamped pendulum and the conserved quantity of the Lotka–Volterra predator–prey model are functions of this kind, which is why their equilibria are surrounded by closed trajectories ([Ecology](/7.19)).

### 11.5.2. Classification of Equilibria of Planar Linear Systems

Consider $\boldsymbol{x}'=A\boldsymbol{x}$, where $A$ is a real $2\times2$ matrix with $\det A\ne0$ (so the origin is an isolated equilibrium). Let

$$
p=\operatorname{tr}(A),\qquad q=\det A,\qquad\Delta=p^2-4q;
$$
the eigenvalues are $\lambda_{1,2}=\frac{p\pm\sqrt\Delta}{2}$, with $\lambda_1+\lambda_2=p$ and $\lambda_1\lambda_2=q$. A real invertible linear change of variables $\boldsymbol{x}=T\boldsymbol{\xi}$ transforms the system into $\boldsymbol{\xi}'=T^{-1}AT\boldsymbol{\xi}$ and only deforms the phase portrait linearly, so it suffices to consider the real canonical forms of $T^{-1}AT$:

$$
\text{(i)}\ \begin{bmatrix}\lambda_1&0\\0&\lambda_2\end{bmatrix}\ (\lambda_1,\lambda_2\text{ real}),\qquad\text{(ii)}\ \begin{bmatrix}\lambda&1\\0&\lambda\end{bmatrix},\qquad\text{(iii)}\ \begin{bmatrix}\alpha&-\beta\\\beta&\alpha\end{bmatrix}\ (\beta\ne0).
$$

**Theorem 11.5.2** The origin of the planar linear system $\boldsymbol{x}'=A\boldsymbol{x}$ ($q=\det A\ne0$) is classified by $p,q$ as follows.

| Condition | Eigenvalues | Type | Stability |
|---|---|---|---|
| $q<0$ | Real, of opposite signs | *Saddle* | Unstable |
| $q>0$, $\Delta>0$ | Real, distinct, of the same sign | *Node* | Asymptotically stable for $p<0$, unstable for $p>0$ |
| $q>0$, $\Delta=0$, $A=\lambda I$ | Real double root, two blocks of size one | Star node (proper node) | Same as above |
| $q>0$, $\Delta=0$, $A\ne\lambda I$ | Real double root, one block of size two | Degenerate node (improper node) | Same as above |
| $q>0$, $\Delta<0$, $p\ne0$ | Complex conjugate, real part $\frac p2\ne0$ | *Focus* | Asymptotically stable for $p<0$, unstable for $p>0$ |
| $q>0$, $p=0$ | Purely imaginary, $\pm\mathrm{i}\sqrt q$ | *Center* | Stable, not asymptotically stable |

**Proof** Stability follows from Theorem 11.1.2; we describe the shape of the trajectories.

(i) $\xi=c_1\mathrm{e}^{\lambda_1t}$, $\eta=c_2\mathrm{e}^{\lambda_2t}$. If $\lambda_1\lambda_2>0$, eliminating $t$ gives $\lvert\eta\rvert=C\lvert\xi\rvert^{\lambda_2/\lambda_1}$, a family of "parabolas", and all trajectories enter (or leave) the origin. If $\lvert\lambda_1\rvert<\lvert\lambda_2\rvert$, the exponent is $>1$, and every trajectory except those on the $\eta$-axis is tangent at the origin to the $\xi$-axis (the slow direction, the eigenvector of $\lambda_1$). This is a node; when $\lambda_1=\lambda_2$ the trajectories are rays, and the origin is called a star node. If $\lambda_1<0<\lambda_2$, then $\lvert\eta\rvert=C\lvert\xi\rvert^{-\lvert\lambda_2/\lambda_1\rvert}$, a family of "hyperbolas"; only the trajectories on the $\xi$-axis enter the origin and only those on the $\eta$-axis leave it. These four half-axes are called separatrices, and the origin is a saddle.

(ii) $\xi=(c_1+c_2t)\mathrm{e}^{\lambda t}$, $\eta=c_2\mathrm{e}^{\lambda t}$. For $c_2\ne0$, $\xi/\eta=c_1/c_2+t$, and $\xi/\eta\to\infty$ as $t\to\mp\infty$ (for $\lambda\gtrless0$): all trajectories are tangent at the origin to the $\xi$-axis (the only eigenvector direction), and they "turn around" the origin on one side. This is a degenerate node.

(iii) In polar coordinates $\xi=r\cos\theta$, $\eta=r\sin\theta$ the system becomes $r'=\alpha r$, $\theta'=\beta$, so $r=r_0\mathrm{e}^{\alpha t}$ and $\theta=\theta_0+\beta t$; the trajectories are the logarithmic spirals $r=r_0\mathrm{e}^{\frac\alpha\beta(\theta-\theta_0)}$, which are circles when $\alpha=0$. In the original coordinates the spirals and circles become general spirals and ellipses. The former case is a focus, the latter a center. $\square$

The direction of rotation of a focus or center can be read off directly: at the point $(1,0)$ the velocity is $(a_{11},a_{21})$, and the rotation is counterclockwise if $a_{21}>0$. The six phase portraits are shown in [Section 11.9 of 2.1.11](/2.1.11#sec-11.9), and the figure below draws the classification in the $(p,q)$-plane.

![Classification of planar linear systems in the trace–determinant plane (p, q) = (tr A, det A): saddles for q < 0; foci above the parabola p^2 = 4q and nodes below it (q > 0); asymptotically stable for p < 0 and unstable for p > 0; centers on the positive q-axis; star nodes or degenerate nodes on the parabola itself](./plots/trace-determinant-plane.py)

**Example 11.5.1** Classify the origin in each case. (1) $A=\begin{bmatrix}1&2\\3&2\end{bmatrix}$: $q=-4<0$, a saddle. (2) $A=\begin{bmatrix}-1&1\\-4&-1\end{bmatrix}$: $p=-2$, $q=5$, $\Delta=-16<0$, a stable focus; $a_{21}=-4<0$, so the rotation is clockwise. (3) $A=\begin{bmatrix}-3&1\\1&-3\end{bmatrix}$: $p=-6$, $q=8$, $\Delta=4>0$, a stable node with eigenvalues $-2,-4$; the trajectories are tangent at the origin to the slow direction $(1,1)^{\mathsf T}$.

For the nonlinear system (11.4), we classify an equilibrium by its Jacobian matrix. If $P,Q\in C^2$ and the linear approximation is a saddle, a node with distinct eigenvalues or a focus, then near the equilibrium the nonlinear system has the same type of trajectories and the same stability as its linear approximation. If the linear approximation is a center, the nonlinear system may be a center (as for the undamped pendulum) or a focus (Example 11.4.2), and must be examined separately.

## 11.6. Limit Cycles

### 11.6.1. Definition and Examples

The closed trajectories of a linear system always come in families (a center), so they cannot describe the phenomenon that "whatever the initial value, the system eventually settles into the same oscillation", as in heartbeats, electronic oscillators and the sustained oscillations of predator–prey populations. This requires isolated closed trajectories.

**Definition 11.6.1 (Limit Cycle)** A closed trajectory $\Gamma$ of a planar autonomous system is called a **limit cycle** if it is isolated (there is an annular neighborhood of $\Gamma$ containing no other closed trajectory). It is called stable if nearby trajectories on both sides tend to $\Gamma$ as $t\to+\infty$, unstable if they tend to $\Gamma$ as $t\to-\infty$, and semistable if they approach it on one side and recede on the other.

**Example 11.6.1** In polar coordinates the system

$$
x'=-y+x(1-x^2-y^2),\qquad y'=x+y(1-x^2-y^2)
$$
becomes $r'=r(1-r^2)$, $\theta'=1$. Solving gives $r(t)=\big(1+C\mathrm{e}^{-2t}\big)^{-1/2}$: for both $r_0<1$ and $r_0>1$ we have $r\to1$, and the trajectories spiral toward the unit circle. The unit circle is a stable limit cycle, and the origin (whose linear approximation has eigenvalues $1\pm\mathrm{i}$) is an unstable focus.

### 11.6.2. Criteria for Existence and Nonexistence

**Definition 11.6.2** Let the positive semi-trajectory $\gamma^+$ correspond to the solution $\boldsymbol{x}(t)$, $t\ge t_0$. If there exist $t_k\to+\infty$ with $\boldsymbol{x}(t_k)\to\boldsymbol{p}$, then $\boldsymbol{p}$ is called an $\omega$-limit point of $\gamma^+$, and the set of all $\omega$-limit points is the $\omega$-**limit set**.

**Theorem 11.6.1 (Poincaré–Bendixson)** Suppose a positive semi-trajectory $\gamma^+$ of the planar autonomous system (11.4) is contained in a bounded closed set $K\subset G$ that contains no equilibrium points. Then the $\omega$-limit set of $\gamma^+$ is a closed trajectory: either $\gamma^+$ is itself a closed trajectory, or it spirals toward a closed trajectory (stated without proof).

A commonly used form: if an annular region $K$ contains no equilibrium points and the vector field points into $K$ everywhere on its boundary ($K$ is a positively invariant "trapping region"), then $K$ contains at least one closed trajectory. In Example 11.6.1 we can take $K=\{\frac12\le r\le2\}$: $r'>0$ at $r=\frac12$ and $r'<0$ at $r=2$. This theorem is specific to the plane (it relies on the Jordan curve theorem); autonomous systems of dimension three or more can have chaotic bounded trajectories, as in the Lorenz equations.

**Theorem 11.6.2 (Bendixson's Criterion)** Let $D\subset G$ be a simply connected region. If $\dfrac{\partial P}{\partial x}+\dfrac{\partial Q}{\partial y}$ does not change sign in $D$ and does not vanish identically on any subregion of $D$, then Eq. (11.4) has no closed trajectory in $D$.

**Proof** Suppose $\Gamma\subset D$ is a closed trajectory with period $T$, enclosing the region $\Sigma$ (by simple connectedness $\Sigma\subset D$). By **Green's theorem**,

$$
\iint_\Sigma\Big(\frac{\partial P}{\partial x}+\frac{\partial Q}{\partial y}\Big)\mathrm{d}x\,\mathrm{d}y=\oint_\Gamma P\,\mathrm{d}y-Q\,\mathrm{d}x=\pm\int_0^T\big(P\,y'-Q\,x'\big)\,\mathrm{d}t=\pm\int_0^T(PQ-QP)\,\mathrm{d}t=0,
$$
whereas the integrand on the left does not change sign and does not vanish identically, so the integral is nonzero, a contradiction. $\square$

More generally, the conclusion still holds if there is a $C^1$ function $B(x,y)$ such that $\frac{\partial(BP)}{\partial x}+\frac{\partial(BQ)}{\partial y}$ satisfies the same conditions (Dulac's criterion). For example, the damped oscillator $x'=y$, $y'=-g(x)-ky$ ($k>0$) has divergence $-k<0$ and therefore no closed trajectories.

### 11.6.3. The van der Pol Equation

**Example 11.6.2** The van der Pol equation

$$
x''-\mu(1-x^2)x'+x=0\qquad(\mu>0)
$$
describes an oscillating circuit with a nonlinear resistance: for $\lvert x\rvert<1$ the damping is negative and the amplitude is amplified; for $\lvert x\rvert>1$ the damping is positive and the amplitude is reduced. We write it as $x'=y$, $y'=-x+\mu(1-x^2)y$.

- The only equilibrium is the origin, with Jacobian matrix $\begin{bmatrix}0&1\\-1&\mu\end{bmatrix}$, $p=\mu>0$ and $q=1$: an unstable focus ($\mu<2$) or an unstable node ($\mu>2$).
- The energy $E=\frac12(x^2+y^2)$ satisfies $\dot E=\mu(1-x^2)y^2$: it increases in the strip $\lvert x\rvert<1$ and can decrease outside it. One can prove (Liénard's theorem, stated without proof) that the equation has a unique limit cycle, which is stable and attracts every nonzero solution.
- For small $\mu$ the limit cycle is close to the circle of radius 2 and the oscillation is nearly simple harmonic; for large $\mu$ it is a "relaxation oscillation", in which slow drifts alternate with fast jumps, with period approximately $(3-2\ln2)\mu$.

![The van der Pol equation. Left: the phase plane for μ = 1; trajectories starting inside (near the unstable focus) and outside both tend to the same limit cycle (thick curve). Right: x(t) is close to a sinusoidal oscillation for μ = 1 and is a relaxation oscillation, with slow drifts alternating with fast jumps, for μ = 5](./plots/van-der-pol.py)

### 11.6.4. The Hopf Bifurcation

When a parameter of a parameter-dependent system passes through a critical value and the topological structure of the phase portrait (the number and stability of equilibria and closed trajectories) changes, we speak of a *bifurcation*. Consider

$$
r'=r(\mu-r^2),\qquad\theta'=1.
$$
For $\mu<0$ the origin is a stable focus and there are no closed trajectories; for $\mu>0$ the origin becomes an unstable focus and a stable limit cycle of radius $\sqrt\mu$ appears. The linear approximation at the origin has eigenvalues $\mu\pm\mathrm{i}$, and as $\mu$ increases, a pair of complex eigenvalues crosses the imaginary axis from left to right. In general, when a pair of complex eigenvalues at an equilibrium of a planar system crosses the imaginary axis with nonzero speed, then under a nondegeneracy condition a limit cycle of small amplitude is created or destroyed; this is called the *Hopf bifurcation* (stated without proof). The same happens for the van der Pol equation as $\mu$ passes through $0$ from negative to positive values. In biological models, the transition of populations from stable coexistence to sustained oscillation is often exactly this bifurcation ([Ecology](/7.19)).

## Summary

| Topic | Result |
|---|---|
| Stability | Small perturbations cause only small deviations on $[t_0,\infty)$; asymptotic stability also requires convergence to zero |
| Linear systems | Stable $\Leftrightarrow$ $\Phi$ bounded; constant coefficients: asymptotically stable $\Leftrightarrow$ $\operatorname{Re}\lambda<0$; stable $\Leftrightarrow$ $\operatorname{Re}\lambda\le0$ and purely imaginary eigenvalues semisimple |
| Routh–Hurwitz | Stable polynomial $\Leftrightarrow$ all leading principal minors of the Hurwitz matrix are positive; necessary condition: all coefficients positive |
| Linear approximation | All $\operatorname{Re}\lambda<0$ $\Rightarrow$ asymptotically stable; some $\operatorname{Re}\lambda>0$ $\Rightarrow$ unstable; otherwise the critical case |
| Lyapunov functions | $V$ positive definite, $\dot V\le0$ $\Rightarrow$ stable; $\dot V$ negative definite $\Rightarrow$ asymptotically stable; LaSalle's principle handles negative semidefinite $\dot V$ |
| Planar linear systems | $q<0$: saddle; for $q>0$: $\Delta>0$ node, $\Delta<0$ focus, $p=0$ center; the sign of $p$ determines stability |
| Limit cycles | Isolated closed trajectories; Poincaré–Bendixson guarantees existence, the Bendixson–Dulac criteria rule it out; the van der Pol equation has a unique stable limit cycle |
