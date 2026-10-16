---
title: Separable Equations, Linear Equations and Elementary Transformations
source_hash: b64faa75ee3b
---

This chapter treats several classes of first-order equations that can be solved by elementary integration, together with the theoretical questions attached to them. Separable equations and first-order linear equations are the two most basic classes. The solutions of the former can be written down rigorously through inverse functions, and uniqueness can fail only where the right-hand side vanishes; the latter have an explicit solution formula, which allows a complete answer to the question of existence of periodic and bounded solutions. Homogeneous equations, Bernoulli equations and Riccati equations are reduced to these two classes by changes of variables. The Riccati equation is one of the simplest nonlinear equations; it is equivalent to a second-order linear equation and in general cannot be solved by quadratures. The last section uses these methods to find isogonal and orthogonal trajectories of families of curves.

The routine solution methods and examples were given in calculus, [2.2.15](/2.2.15) (separable equations and equations reducible to them in [Section 15.2](/2.2.15#sec-15.2), first-order linear equations and Bernoulli equations in [Section 15.3](/2.2.15#sec-15.3)); here we keep them brief and concentrate on proofs and special topics. All of these equations can be regarded as special cases of the exact equations of the previous chapter: a separable equation has the integrating factor $\dfrac{1}{X_1(x)Y_1(y)}$ (Example 2.3.2), and a first-order linear equation has the integrating factor $\mathrm{e}^{\int p\,\mathrm{d}x}$ (Example 2.3.1).

## 3.1. Separable Equations

**Definition 3.1.1** An equation of the form

$$
\frac{\mathrm{d}y}{\mathrm{d}x}=f(x)g(y),\tag{3.1}
$$
or an equation in the symmetric form $X(x)Y_1(y)\,\mathrm{d}x+X_1(x)Y(y)\,\mathrm{d}y=0$, is called a **separable equation**.

**Theorem 3.1.1** Let $f$ be continuous on an interval $I$ and $g$ continuous on an open interval $J$, with $x_0\in I$, $y_0\in J$ and $g(y_0)\ne0$. Then the initial value problem (3.1), $y(x_0)=y_0$ has a unique solution in some neighborhood of $x_0$, determined by

$$
\int_{y_0}^y\frac{\mathrm{d}s}{g(s)}=\int_{x_0}^xf(t)\,\mathrm{d}t.\tag{3.2}
$$

**Proof** Let $J_0\subset J$ be the largest open interval containing $y_0$ on which $g\ne0$. Since $g$ does not change sign on $J_0$, the function $G(y)=\displaystyle\int_{y_0}^y\frac{\mathrm{d}s}{g(s)}$ is continuously differentiable and strictly monotonic on $J_0$ with $G(y_0)=0$; it maps $J_0$ onto an open interval $G(J_0)$ containing $0$ and has a continuously differentiable inverse $G^{-1}$. Let $F(x)=\int_{x_0}^xf(t)\,\mathrm{d}t$. It is continuous with $F(x_0)=0$, so $F(x)\in G(J_0)$ in some neighborhood $I_0$ of $x_0$.

Existence: let $\varphi=G^{-1}\circ F$. Then $G(\varphi(x))=F(x)$, and differentiating both sides gives $\dfrac{\varphi'(x)}{g(\varphi(x))}=f(x)$, so $\varphi$ is a solution, and $\varphi(x_0)=G^{-1}(0)=y_0$.

Uniqueness: let $\psi$ be another solution with $\psi(x_0)=y_0$. By continuity, $\psi(x)\in J_0$ near $x_0$, so $\dfrac{\mathrm{d}}{\mathrm{d}x}G(\psi(x))=\dfrac{\psi'(x)}{g(\psi(x))}=f(x)$ and $G(\psi(x))=F(x)$, that is, $\psi=G^{-1}\circ F=\varphi$. $\square$

Thus uniqueness for a separable equation can fail only on the lines $y=c$ with $g(c)=0$, and $y\equiv c$ is itself always a solution. Dividing by $g(y)$ when separating variables loses these solutions, so they must be checked separately ([2.2.15 Example 15.2.1](/2.2.15#ex-15.2.1)).

**Remark 3.1.1** Suppose $g(c)=0$ and $g$ is positive just to the right of $c$. By (3.2), a solution starting from $y>c$ reaches $c$ at a finite $x$ only if $\displaystyle\int_c^{c+\varepsilon}\frac{\mathrm{d}s}{g(s)}<+\infty$. Therefore:

- if this integral diverges (for example, if $g$ satisfies a **Lipschitz condition** near $c$, $\lvert g(s)\rvert\le L\lvert s-c\rvert$, or if $g(s)=(s-c)\lvert\ln(s-c)\rvert$), no other solution meets $y=c$, and the solution through each point of $y=c$ is unique;
- if the integral converges (for example $g(y)=3y^{2/3}$, $c=0$), a solution can reach $y=c$ at a finite point, follow it for a while and then leave it again, so uniqueness fails ([2.2.15 Example 15.1.5](/2.2.15#ex-15.1.5)).

This criterion is precisely the prototype of the Osgood uniqueness theorem in [2.4.4](/2.4.4).

## 3.2. First-Order Linear Equations

### 3.2.1. The Solution Formula

The standard form of a first-order linear equation is

$$
y'+p(x)y=q(x);\tag{3.3}
$$
when $q\equiv0$ it is called a homogeneous linear equation. The derivation of the solution formula (by an integrating factor or the **variation of constants formula**) is in [2.2.15 Theorem 15.3.1](/2.2.15#thm-15.3.1); here we state it in the form of an initial value problem.

**Theorem 3.2.1** Let $p$ and $q$ be continuous on an interval $I$ and $x_0\in I$. Then for every $y_0$, the solution of Eq. (3.3) satisfying $y(x_0)=y_0$ exists and is unique on the whole interval $I$, and it is given by

$$
y(x)=y_0\mathrm{e}^{-\int_{x_0}^xp(t)\,\mathrm{d}t}+\int_{x_0}^xq(s)\mathrm{e}^{-\int_s^xp(t)\,\mathrm{d}t}\,\mathrm{d}s.\tag{3.4}
$$

**Proof** Let $\mu(x)=\mathrm{e}^{\int_{x_0}^xp(t)\,\mathrm{d}t}$; then $\mu'=p\mu$ and $\mu>0$. For any solution $y$ on any subinterval of $I$,

$$
(\mu y)'=\mu(y'+py)=\mu q.
$$
Integrating from $x_0$ to $x$ gives $\mu(x)y(x)-y_0=\int_{x_0}^x\mu(s)q(s)\,\mathrm{d}s$, and dividing by $\mu(x)$ gives (3.4). Hence any solution must be given by (3.4), which proves uniqueness. Conversely, the right-hand side of (3.4) is defined on all of $I$, and a direct check shows that it satisfies the equation and the initial condition. $\square$

### 3.2.2. Properties of Solutions

**Proposition 3.2.1** Let $p$ and $q$ be continuous on an interval $I$.

1. Every solution of Eq. (3.3) can be extended to the whole interval $I$ (global existence).
2. A solution of the homogeneous equation $y'+p(x)y=0$ either vanishes identically or vanishes nowhere.
3. The set of all solutions of the homogeneous equation is the one-dimensional linear space $\big\{C\mathrm{e}^{-\int_{x_0}^xp}\mid C\in\mathbb{R}\big\}$; the set of all solutions of Eq. (3.3) is $y^*+\big\{C\mathrm{e}^{-\int_{x_0}^xp}\big\}$, where $y^*$ is any particular solution. In particular, the general solution contains all solutions.
4. (**Superposition principle**) If $y_k$ is a solution of $y'+py=q_k$ ($k=1,2$), then $\alpha y_1+\beta y_2$ is a solution of $y'+py=\alpha q_1+\beta q_2$.

**Proof** Parts 1 and 3 follow directly from Theorem 3.2.1 (formula (3.4) is affine in $y_0$). Part 2: the solutions of the homogeneous equation are $y_0\mathrm{e}^{-\int_{x_0}^xp}$, and the exponential factor is positive everywhere. Part 4: the operator $L(y)=y'+py$ is linear. $\square$

Property 1 is an important feature distinguishing linear from nonlinear equations: the right-hand side of $y'=y^2$ is smooth on the whole plane, yet its solutions $\dfrac{1}{C-x}$ tend to infinity at a finite point. How far the solutions of nonlinear equations can be extended is the question of [2.4.5](/2.4.5).

**Proposition 3.2.2** If $u_1,u_2,u_3$ are three distinct solutions of Eq. (3.3) on an interval $I$, then

$$
\frac{u_1(x)-u_3(x)}{u_2(x)-u_3(x)}\equiv C\quad(\text{constant}).
$$

**Proof** Both $u_1-u_3$ and $u_2-u_3$ are solutions of the homogeneous equation, so by part 3 of Proposition 3.2.1, $u_k-u_3=C_k\mathrm{e}^{-\int_{x_0}^xp}$ ($k=1,2$), with $C_2\ne0$ since $u_2\ne u_3$; by part 2, $u_2-u_3$ vanishes nowhere. The ratio equals $C_1/C_2$. $\square$

Geometrically, Proposition 3.2.2 says that any three integral curves of a first-order linear equation cut every vertical line in segments with a fixed ratio. The Riccati equation of a later section has an analogous result involving four solutions.

## 3.3. Periodic and Bounded Solutions

In this section we consider the equation defined on the whole real line,

$$
y'+p(x)y=q(x),\qquad x\in\mathbb{R},\tag{3.5}
$$
with $p$ and $q$ continuous. Write $P(x)=\int_0^xp(t)\,\mathrm{d}t$. By (3.4), the solution satisfying $y(0)=y_0$ is

$$
y(x)=\mathrm{e}^{-P(x)}\Big(y_0+\int_0^xq(s)\mathrm{e}^{P(s)}\,\mathrm{d}s\Big).\tag{3.6}
$$

### 3.3.1. Bounded Solutions

**Proposition 3.3.1** Let $p(x)\equiv\alpha>0$ be a constant and let $q$ be continuous and bounded on $\mathbb{R}$, $\lvert q\rvert\le M$. Then Eq. (3.5) has a unique solution bounded on $\mathbb{R}$,

$$
y^*(x)=\int_{-\infty}^xq(s)\mathrm{e}^{-\alpha(x-s)}\,\mathrm{d}s,\qquad\lvert y^*(x)\rvert\le\frac M\alpha,\tag{3.7}
$$
and every solution $y$ satisfies $y(x)-y^*(x)\to0$ as $x\to+\infty$.

**Proof** Since $\lvert q(s)\mathrm{e}^{-\alpha(x-s)}\rvert\le M\mathrm{e}^{-\alpha(x-s)}$, the integral (3.7) converges, and

$$
\lvert y^*(x)\rvert\le\int_{-\infty}^xM\mathrm{e}^{-\alpha(x-s)}\,\mathrm{d}s=\frac M\alpha.
$$
Writing $y^*(x)=\mathrm{e}^{-\alpha x}\int_{-\infty}^xq(s)\mathrm{e}^{\alpha s}\,\mathrm{d}s$ and differentiating gives $y^{*\prime}=-\alpha y^*+q$, so $y^*$ is a bounded solution; it is the solution (3.6) with $y_0=\int_{-\infty}^0q(s)\mathrm{e}^{\alpha s}\,\mathrm{d}s$. By Proposition 3.2.1, every solution has the form $y=y^*+C\mathrm{e}^{-\alpha x}$. For $C\ne0$, $\lvert C\mathrm{e}^{-\alpha x}\rvert\to+\infty$ as $x\to-\infty$, so the solution is unbounded; hence the bounded solution is unique. Moreover $C\mathrm{e}^{-\alpha x}\to0$ as $x\to+\infty$, so all solutions approach $y^*$. $\square$

The condition $\alpha>0$ means that the system is damped: the influence $C\mathrm{e}^{-\alpha x}$ of the initial value decays with time, and after a long time only the response $y^*$ determined by the forcing $q$ remains. In (3.7), $y^*(x)$ accumulates all past forcing $q(s)$ ($s\le x$) with weight $\mathrm{e}^{-\alpha(x-s)}$; the more remote the forcing, the smaller its weight.

### 3.3.2. Periodic Solutions

**Definition 3.3.1** Let $T>0$. If a solution $y(x)$ of an equation is defined on $\mathbb{R}$ and $y(x+T)\equiv y(x)$, then $y$ is called a **periodic solution** of the equation with period $T$, or a $T$-periodic solution.

**Proposition 3.3.2** Let $p$ and $q$ be continuous functions with period $T$.

1. If $y(x)$ is a solution of Eq. (3.5), so is $y(x+T)$;
2. a solution $y$ is $T$-periodic if and only if $y(T)=y(0)$.

**Proof** Part 1: $y'(x+T)+p(x)y(x+T)=y'(x+T)+p(x+T)y(x+T)=q(x+T)=q(x)$. Part 2: necessity is obvious. For sufficiency, $z(x)=y(x+T)-y(x)$ is a solution of the homogeneous equation $z'+p(x)z=0$ with $z(0)=0$, so $z\equiv0$ by part 2 of Proposition 3.2.1. $\square$

The problem of periodic solutions thus reduces to an algebraic equation for the initial value $y_0=y(0)$. By (3.6), $y(T)=y(0)$ means

$$
y_0\big(\mathrm{e}^{P(T)}-1\big)=\int_0^Tq(s)\mathrm{e}^{P(s)}\,\mathrm{d}s.\tag{3.8}
$$

**Theorem 3.3.1** Let $p$ and $q$ be continuous functions with period $T$, and let $\displaystyle\bar p=\frac1T\int_0^Tp(x)\,\mathrm{d}x$ be the mean value of $p$.

1. The homogeneous equation $y'+p(x)y=0$ has a nonzero $T$-periodic solution if and only if $\bar p=0$; in that case all of its solutions are $T$-periodic.
2. If $\bar p\ne0$, Eq. (3.5) has a unique $T$-periodic solution, namely the solution (3.6) with

$$
y_0=\frac{\int_0^Tq(s)\mathrm{e}^{P(s)}\,\mathrm{d}s}{\mathrm{e}^{P(T)}-1}.
$$
3. If $\bar p=0$, then all solutions of Eq. (3.5) are $T$-periodic when $\displaystyle\int_0^Tq(s)\mathrm{e}^{P(s)}\,\mathrm{d}s=0$, and otherwise Eq. (3.5) has no $T$-periodic solution.

**Proof** Note that $P(T)=T\bar p$. Part 1: for $q=0$, (3.8) reads $y_0(\mathrm{e}^{P(T)}-1)=0$, which has a nonzero solution $y_0$ if and only if $P(T)=0$, in which case it holds for every $y_0$. Part 2: if $P(T)\ne0$, (3.8) determines $y_0$ uniquely. Part 3: if $P(T)=0$, the left-hand side of (3.8) is zero, so (3.8) holds either for every $y_0$ or for none, according to whether the right-hand side vanishes. In each case part 2 of Proposition 3.3.2 translates the result into a statement about periodic solutions. $\square$

The uniqueness in part 2 can also be seen as follows: the difference of two $T$-periodic solutions is a $T$-periodic solution of the homogeneous equation, which must be zero when $\bar p\ne0$.

**Corollary 3.3.1** Let $p\equiv\alpha>0$ and let $q$ be a continuous function with period $T$. Then the bounded solution (3.7) of Proposition 3.3.1 is the unique $T$-periodic solution of Eq. (3.5).

**Proof** Uniqueness follows from part 2 of Theorem 3.3.1. For periodicity, substitute $s=t+T$ in (3.7):

$$
y^*(x+T)=\int_{-\infty}^{x+T}q(s)\mathrm{e}^{-\alpha(x+T-s)}\,\mathrm{d}s=\int_{-\infty}^xq(t+T)\mathrm{e}^{-\alpha(x-t)}\,\mathrm{d}t=y^*(x).\qquad\square
$$

**Example 3.3.1** Consider $y'+y=\sin x$. Here $\alpha=1$, and the periodic solution is

$$
y^*(x)=\int_{-\infty}^x\sin s\,\mathrm{e}^{-(x-s)}\,\mathrm{d}s=\frac{\sin x-\cos x}{2}=\frac{1}{\sqrt2}\sin\Big(x-\frac\pi4\Big);
$$
the general solution is $y=y^*+C\mathrm{e}^{-x}$. All solutions approach this periodic solution exponentially fast; its amplitude is $1/\sqrt2$ times that of the forcing, and its phase lags by $\pi/4$.

![Several solutions of y' + y = sin x (thin lines, initial values y(0) from -3 to 3) all approach the unique periodic solution y* = (sin x - cos x)/2 (thick line) at the rate e^{-x}; looking to the left, every solution other than y* diverges exponentially](./plots/periodic-solution.py)

## 3.4. Homogeneous Equations and Bernoulli Equations

The following two classes of equations are reduced to the types of the previous two sections by a change of the unknown function. For solution methods and examples, see [2.2.15 Algorithm 15.2.2](/2.2.15#alg-15.2.2) and [Algorithm 15.3.2](/2.2.15#alg-15.3.2).

Homogeneous equations $y'=f\Big(\dfrac yx\Big)$: setting $y=xu$ gives the separable equation $xu'=f(u)-u$. The roots of $f(u_0)=u_0$ give the solutions $y=u_0x$, which are lost when separating variables; by Theorem 3.1.1, solutions are unique where $f(u)\ne u$. The equation is invariant under the dilations $(x,y)\mapsto(\lambda x,\lambda y)$, so scaling an integral curve about the origin produces another integral curve; this is why the substitution $u=y/x$ reduces the complexity.

The **Bernoulli equation** $y'+p(x)y=q(x)y^n$ ($n\ne0,1$): where $y\ne0$, multiply both sides by $(1-n)y^{-n}$ and set $z=y^{1-n}$ to obtain the linear equation

$$
z'+(1-n)p(x)z=(1-n)q(x).
$$
Having found $z$, we get $y=z^{1/(1-n)}$ (when $y^{1-n}$ is defined only for $y>0$, we solve in the region $y>0$). For $n>0$, $y\equiv0$ is also a solution. When $0<n<1$, $y^n$ does not satisfy a Lipschitz condition at $y=0$; by the same analysis as in Remark 3.1.1, solutions can reach $y=0$ at a finite point, and uniqueness may fail. For example, $y'=y^{1/2}$ has the solutions $y\equiv0$ and $y=\dfrac{(x-c)^2}{4}$ for $x\ge c$ (and zero before $c$).

## 3.5. The Riccati Equation

### 3.5.1. Definition and Elementary Transformations

**Definition 3.5.1** An equation of the form

$$
y'=p(x)y^2+q(x)y+r(x),\tag{3.9}
$$
where $p,q,r$ are continuous on an interval $I$ and $p\not\equiv0$, is called a **Riccati equation**.

The right-hand side is a quadratic polynomial in $y$, so the Riccati equation is the simplest nonlinear equation, "next to linear". When $r\equiv0$ it is a Bernoulli equation ($n=2$). The right-hand side is continuously differentiable in $y$ and satisfies a local Lipschitz condition, so the solution through each point is unique ([2.4.4](/2.4.4)) and distinct solutions never intersect; in general, however, solutions cannot be extended to all of $I$ (for example $y'=y^2$).

**Proposition 3.5.1** Let $Q(x)=\mathrm{e}^{\int_{x_0}^xq(t)\,\mathrm{d}t}$ and $y=Q(x)z$. Then Eq. (3.9) becomes

$$
z'=p(x)Q(x)z^2+\frac{r(x)}{Q(x)}.
$$
Hence we may always assume $q\equiv0$.

**Proof** We have $Q'=qQ$ and $y'=qQz+Qz'$; substituting into (3.9) gives $qQz+Qz'=pQ^2z^2+qQz+r$, that is, $Qz'=pQ^2z^2+r$. $\square$

### 3.5.2. Solution When a Particular Solution Is Known

**Theorem 3.5.1** Let $y=\varphi(x)$ be a solution of Eq. (3.9). Then the substitution $y=\varphi(x)+\dfrac{1}{u}$ transforms Eq. (3.9) into the first-order linear equation

$$
u'+\big(2p(x)\varphi(x)+q(x)\big)u+p(x)=0.\tag{3.10}
$$
Hence the remaining solutions of Eq. (3.9) are $y=\varphi+\dfrac1u$, where $u$ ranges over the solutions of (3.10) (on intervals where $u\ne0$).

**Proof** Let $z=y-\varphi$. Then

$$
z'=p(y^2-\varphi^2)+q(y-\varphi)=p\big((z+\varphi)^2-\varphi^2\big)+qz=pz^2+(2p\varphi+q)z,
$$
which is a Bernoulli equation with $n=2$. Since solutions do not intersect, $z$ vanishes nowhere when $y\ne\varphi$. Setting $u=1/z$ gives $u'=-z'/z^2=-p-(2p\varphi+q)u$, which is (3.10). $\square$

So once one particular solution is known, two more quadratures (solving a linear equation) give the general solution. When more particular solutions are known, the number of quadratures can be reduced further.

**Theorem 3.5.2** Let $y_1$ and $y_2$ be two distinct solutions of Eq. (3.9). Then the remaining solutions $y$ satisfy

$$
\frac{y-y_1}{y-y_2}=C\exp\Big(\int p(x)\big(y_1(x)-y_2(x)\big)\,\mathrm{d}x\Big),\tag{3.11}
$$
which requires only one quadrature.

**Proof** Let $w=\dfrac{y-y_1}{y-y_2}$. By (3.9), $y'-y_k'=p(y^2-y_k^2)+q(y-y_k)$, so $\dfrac{y'-y_k'}{y-y_k}=p(y+y_k)+q$. Hence

$$
\frac{w'}{w}=\frac{y'-y_1'}{y-y_1}-\frac{y'-y_2'}{y-y_2}=p(y_1-y_2),
$$
and integration gives (3.11). $\square$

**Theorem 3.5.3** If $y_1,y_2,y_3,y_4$ are four distinct solutions of Eq. (3.9) on an interval $J\subset I$, then their cross-ratio is constant:

$$
\frac{y_3-y_1}{y_4-y_1}\cdot\frac{y_4-y_2}{y_3-y_2}\equiv C.\tag{3.12}
$$

**Proof** Solutions do not intersect, so all the differences vanish nowhere. Take $\varphi=y_4$ in Theorem 3.5.1 and let $u_k=\dfrac{1}{y_k-y_4}$ ($k=1,2,3$); these are three distinct solutions of the linear equation (3.10). Since $y_k-y_4=1/u_k$,

$$
\frac{y_3-y_1}{y_4-y_1}=\frac{\frac1{u_3}-\frac1{u_1}}{-\frac1{u_1}}=-\frac{u_1-u_3}{u_3},\qquad\frac{y_4-y_2}{y_3-y_2}=\frac{-\frac1{u_2}}{\frac1{u_3}-\frac1{u_2}}=-\frac{u_3}{u_2-u_3}.
$$
Multiplying the two gives $\dfrac{u_1-u_3}{u_2-u_3}$, which is constant by Proposition 3.2.2. $\square$

**Corollary 3.5.1** If three distinct solutions $y_1,y_2,y_3$ of Eq. (3.9) are known, the remaining solutions $y$ are given by the algebraic relation

$$
\frac{y_3-y_1}{y-y_1}\cdot\frac{y-y_2}{y_3-y_2}=C,
$$
and no quadrature is needed.

Theorems 3.5.1–3.5.3 admit a unified interpretation: the solutions correspond one-to-one to the solutions of (3.10), that is, to the points of a line, and $y=\varphi+1/u$ is a linear fractional transformation. Solutions of a linear equation preserve the ratio determined by three points, and linear fractional transformations preserve the cross-ratio of four points.

**Example 3.5.1** Solve $y'=y^2-\dfrac{2}{x^2}$ ($x>0$). Trying $y=\dfrac ax$ gives $-\dfrac{a}{x^2}=\dfrac{a^2-2}{x^2}$, so $a^2+a-2=0$ and $a=1$ or $a=-2$. Take $y_1=\dfrac1x$, $y_2=-\dfrac2x$ and $p=1$. By (3.11),

$$
\frac{y-\frac1x}{y+\frac2x}=C\exp\int\frac3x\,\mathrm{d}x=Cx^3,\qquad\text{that is,}\qquad y=\frac{1+2Cx^3}{x\,(1-Cx^3)}.
$$
The value $C=0$ gives $y_1$, and $y_2$ corresponds to $C=\infty$.

### 3.5.3. Relation to Second-Order Linear Equations

**Proposition 3.5.2** (1) Where $y\ne0$, the substitution $z=\dfrac{y'}{y}$ (that is, $y=\mathrm{e}^{\int z\,\mathrm{d}x}$) transforms the second-order homogeneous linear equation $y''+P(x)y'+Q(x)y=0$ into the Riccati equation

$$
z'+z^2+P(x)z+Q(x)=0.
$$
(2) Conversely, if $p$ is continuously differentiable and nowhere zero, the substitution $y=-\dfrac{u'}{p(x)u}$ transforms the Riccati equation (3.9) into the second-order linear equation

$$
u''-\Big(q(x)+\frac{p'(x)}{p(x)}\Big)u'+p(x)r(x)u=0.
$$

**Proof** (1) We have $y'=zy$ and $y''=(z'+z^2)y$; substitute and divide by $y$. (2) A direct computation from $y=-\dfrac{u'}{pu}$ gives

$$
y'=-\frac{u''}{pu}+\frac{p'u'}{p^2u}+\frac{u'^2}{pu^2},\qquad py^2=\frac{u'^2}{pu^2},\qquad qy=-\frac{qu'}{pu},
$$
so $y'=py^2+qy+r$ is equivalent to $-\dfrac{u''}{pu}+\dfrac{p'u'}{p^2u}=-\dfrac{qu'}{pu}+r$; multiplying both sides by $-pu$ gives the result. $\square$

Solving a Riccati equation and solving a second-order homogeneous linear equation are therefore one and the same problem. Second-order linear equations generally cannot be solved in elementary functions either, which explains the difficulty of the Riccati equation from another angle. For example, the substitution $y=-\dfrac{u'}{u}$ transforms $y'=x^2+y^2$ into $u''+x^2u=0$, whose solutions can be expressed through Bessel functions as $\sqrt{x}\,J_{\pm1/4}\Big(\dfrac{x^2}{2}\Big)$ ([2.4.10](/2.4.10)) rather than through elementary functions. Part (1) of Proposition 3.5.2 is also useful in Sturm theory: zeros of solutions of the second-order equation correspond to blow-up of solutions of the Riccati equation ([2.4.12](/2.4.12)).

### 3.5.4. Liouville's Theorem

**Theorem 3.5.4 (Liouville)** Let $a\ne0$ and $b\ne0$. The Riccati equation

$$
y'+ay^2=bx^m
$$
can be solved by finitely many quadratures of elementary functions if and only if

$$
m=0,\qquad m=-2,\qquad m=\frac{-4k}{2k+1},\qquad m=\frac{-4k}{2k-1}\qquad(k=1,2,\dots).
$$

We only outline the idea of the sufficiency proof here (the proof of necessity is long and is omitted). Rescaling the independent variable, we may assume $a=1$. For $m=0$ the equation $y'=b-y^2$ is separable. For $m=-2$, setting $u=xy$ transforms the equation into $xu'=b+u-u^2$, which is again separable (Example 3.5.1 is of this type). In the remaining cases, two substitutions lower $k$:

- $T_1$: $\xi=x^{m+1}$, $y=\dfrac{b}{m+1}\cdot\dfrac1\eta$ transforms $y'+y^2=bx^m$ into $\dfrac{\mathrm{d}\eta}{\mathrm{d}\xi}+\eta^2=\dfrac{b}{(m+1)^2}\xi^{n}$ with $n=-\dfrac{m}{m+1}$; it takes $m=\dfrac{-4k}{2k+1}$ to $n=\dfrac{-4k}{2k-1}$.
- $T_2$: $x=\dfrac1t$, $y=t-zt^2$ transforms $y'+y^2=cx^n$ into $\dfrac{\mathrm{d}z}{\mathrm{d}t}+z^2=ct^{-n-4}$; it takes $n=\dfrac{-4k}{2k-1}$ to $\dfrac{-4(k-1)}{2(k-1)+1}$.

Starting from $m=\dfrac{-4k}{2k+1}$ and applying $T_1$ and $T_2$ alternately (starting with $T_2$ if $m=\dfrac{-4k}{2k-1}$), the exponent becomes $0$ after $k$ rounds.

Liouville's theorem (1841) shows that even the simple-looking equation $y'=x^2+y^2$ ($m=2$ is not in the list above) cannot be solved by quadratures. This was an important turning point at which the study of differential equations shifted from "finding the general solution" toward existence theory and qualitative theory ([2.4.1](/2.4.1#sec-1.3)).

## 3.6. Isogonal and Orthogonal Trajectories

**Definition 3.6.1** Let a one-parameter family of plane curves be given. If a curve $L$ meets every curve of the family at a constant angle $\alpha$ (the angle between the tangent lines at the point of intersection), then $L$ is called an **isogonal trajectory** of the family; when $\alpha=\dfrac\pi2$ it is called an **orthogonal trajectory**.

Isogonal trajectories are common in physics: the lines of force of an electrostatic field are the orthogonal trajectories of the family of equipotential lines, as are the streamlines of a potential flow; in heat conduction, the heat flow lines are the orthogonal trajectories of the isotherms.

Suppose the family satisfies a first-order equation $y'=f(x,y)$ (obtained by eliminating the parameter from the equation of the family), and the required trajectories satisfy $y'=g(x,y)$. At a point of intersection, let $\theta_1$ be the inclination of the tangent to the curve of the family and $\theta_2$ that of the tangent to the trajectory, so that $\alpha=\theta_2-\theta_1$. When $\alpha\ne\dfrac\pi2$, write $k=\tan\alpha$; then

$$
k=\tan(\theta_2-\theta_1)=\frac{\tan\theta_2-\tan\theta_1}{1+\tan\theta_1\tan\theta_2}=\frac{g-f}{1+gf},
$$
and solving for $g$ gives the equation of the isogonal trajectories,

$$
y'=\frac{f(x,y)+k}{1-kf(x,y)};\tag{3.13}
$$
when $\alpha=\dfrac\pi2$ we have $fg=-1$, and the equation of the orthogonal trajectories is

$$
y'=-\frac{1}{f(x,y)}.\tag{3.14}
$$
If the family is given implicitly by $F(x,y,y')=0$, then since $f=\dfrac{g-k}{1+kg}$, the isogonal trajectories satisfy

$$
F\Big(x,y,\frac{y'-k}{1+ky'}\Big)=0,
$$
and the orthogonal trajectories satisfy $F\Big(x,y,-\dfrac{1}{y'}\Big)=0$.

**Example 3.6.1** Find the isogonal and orthogonal trajectories of the family of lines $y=Cx$.

Eliminating $C$ from $y=Cx$ gives $f=\dfrac yx$. Substituting into (3.13),

$$
y'=\frac{k+\frac yx}{1-k\frac yx},
$$
which is a homogeneous equation. Setting $y=xu$,

$$
xu'=\frac{k+u}{1-ku}-u=\frac{k(1+u^2)}{1-ku},\qquad\frac{\mathrm{d}u}{1+u^2}-\frac{ku\,\mathrm{d}u}{1+u^2}=\frac{k\,\mathrm{d}x}{x}.
$$
Integration gives $\arctan u-\dfrac k2\ln(1+u^2)=k\ln\lvert x\rvert+c$, and substituting back $u=y/x$,

$$
\arctan\frac yx=k\ln\sqrt{x^2+y^2}+c.
$$
In polar coordinates this is $\rho=C\mathrm{e}^{\theta/k}$ ($C>0$), a logarithmic spiral: a logarithmic spiral meets every ray through the origin at a constant angle, which is why it is also called the equiangular spiral. For $\alpha=\dfrac\pi2$, (3.14) gives $y'=-\dfrac xy$, that is, $x\,\mathrm{d}x+y\,\mathrm{d}y=0$, so the orthogonal trajectories are the concentric circles $x^2+y^2=C^2$.

![The family of lines y = Cx (gray) and its isogonal trajectories: for the angle alpha = pi/3 they are the logarithmic spirals rho = C e^{theta/k}, k = tan alpha (blue); for alpha = pi/2 they are concentric circles (red, dashed)](./plots/isogonal-spirals.py)

**Example 3.6.2** Find the orthogonal trajectories of the family of ellipses $\dfrac{x^2}{a^2}+\dfrac{y^2}{b^2}=C^2$ ($C>0$, with $a,b$ fixed).

Differentiating with respect to $x$ gives $\dfrac{2x}{a^2}+\dfrac{2yy'}{b^2}=0$, so $f=-\dfrac{b^2x}{a^2y}$. By (3.14),

$$
\frac{\mathrm{d}y}{\mathrm{d}x}=\frac{a^2y}{b^2x},\qquad\frac{\mathrm{d}y}{y}=\frac{a^2}{b^2}\cdot\frac{\mathrm{d}x}{x},
$$
and integration gives $y=C\lvert x\rvert^{a^2/b^2}$ ($C$ an arbitrary constant); in addition, $x=0$ (the $y$-axis) is also an orthogonal trajectory. The orthogonal trajectories form a family of power curves, all emanating from the origin (the common center of the ellipses). When $a=b$ the ellipses are concentric circles and the orthogonal trajectories degenerate into lines through the origin, in agreement with Example 3.6.1.

![The family of ellipses x^2/a^2 + y^2/b^2 = C^2 (a = 2, b = 1, gray), its orthogonal trajectories y = C|x|^{a^2/b^2} = C x^4 (blue; the x-axis for C = 0) and the y-axis](./plots/orthogonal-ellipses.py)

## Summary

| Equation | Transformation | Key points |
|---|---|---|
| Separable $y'=f(x)g(y)$ | $\int\frac{\mathrm{d}y}{g}=\int f\,\mathrm{d}x$ | Unique solution where $g(y_0)\ne0$; $g(c)=0$ gives the solution $y=c$, and uniqueness there depends on whether $\int\frac{\mathrm{d}s}{g}$ diverges at $c$ |
| First-order linear $y'+py=q$ | Integrating factor $\mathrm{e}^{\int p}$ | Formula (3.4); global existence; the solution set is a one-dimensional affine space |
| Periodic coefficients | $y(T)=y(0)$ | $\bar p\ne0$: unique periodic solution; $\bar p=0$: all solutions periodic or none |
| Homogeneous $y'=f(y/x)$ | $y=xu$ | Reduces to a separable equation |
| Bernoulli | $z=y^{1-n}$ | Reduces to a linear equation |
| Riccati | $y=\varphi+1/u$ | One particular solution: two quadratures; two: one; three: an algebraic relation; invariant cross-ratio; equivalent to a second-order linear equation |
| Isogonal trajectories | $y'=\frac{f+k}{1-kf}$; orthogonal: $y'=-\frac1f$ | Lines → logarithmic spirals; ellipses → power curves |
