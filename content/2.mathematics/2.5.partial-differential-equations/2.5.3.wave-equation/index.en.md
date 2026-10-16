---
title: The Wave Equation
---

The **wave equation** $u_{tt}=c^2\Delta u$ ([2.5.1](/2.5.1#sec-1.2.1)) is the prototype of a hyperbolic equation. In one space dimension it can be solved completely: every solution is the sum of two waves traveling in opposite directions with speed $c$, and d'Alembert's formula expresses the solution of the initial value problem explicitly in terms of the initial position and velocity. From this formula we read off the defining features of hyperbolic equations: information travels along the characteristics $x\pm ct=\text{const}$ at a finite speed, the value of the solution at a point depends only on the data in a bounded interval, and singularities of the data are neither smoothed nor amplified but carried along. Boundaries are handled by reflection, sources by Duhamel's principle, and energy conservation gives uniqueness and stability, so the problem is well-posed. In three dimensions the method of spherical means leads to Kirchhoff's formula, and in two dimensions the method of descent leads to Poisson's formula. The comparison between them reveals a striking difference: sharp signals stay sharp in three dimensions (Huygens' principle), but leave a lingering tail in two. Finite strings, where reflections at both ends produce standing waves, are treated by separation of variables in [2.5.4](/2.5.4), and the Fourier transform gives yet another approach in [2.5.6](/2.5.6).

## 3.1. The Infinite String: d'Alembert's Formula

### 3.1.1. The General Solution

The one-dimensional wave operator factors into two transport operators:

$$
u_{tt}-c^2u_{xx}=\Big(\frac{\partial}{\partial t}-c\frac{\partial}{\partial x}\Big)\Big(\frac{\partial}{\partial t}+c\frac{\partial}{\partial x}\Big)u.
$$
Each factor is a **directional derivative** along one family of characteristics, so we expect solutions built from the solutions $f(x-ct)$ and $g(x+ct)$ of the transport equations ([2.5.2](/2.5.2#sec-2.1)).

**Theorem 3.1.1** Every solution $u\in C^2(\mathbb{R}^2)$ of $u_{tt}=c^2u_{xx}$ has the form

$$
u(x,t)=F(x+ct)+G(x-ct)\tag{3.1}
$$
with $F,G\in C^2(\mathbb{R})$; conversely, every such function is a solution.

**Proof** Introduce the characteristic coordinates $\xi=x+ct$, $\eta=x-ct$ and write $u(x,t)=w(\xi,\eta)$. By the chain rule, $u_x=w_\xi+w_\eta$, $u_t=c(w_\xi-w_\eta)$, and

$$
u_{xx}=w_{\xi\xi}+2w_{\xi\eta}+w_{\eta\eta},\qquad u_{tt}=c^2\big(w_{\xi\xi}-2w_{\xi\eta}+w_{\eta\eta}\big),
$$
so $u_{tt}-c^2u_{xx}=-4c^2w_{\xi\eta}$; this is the canonical form of [2.5.1](/2.5.1#thm-1.5.2). Hence $w_{\xi\eta}=0$, and as in [2.5.1](/2.5.1#sec-1.1.2), $w=F(\xi)+G(\eta)$. The converse is a direct computation. $\square$

The term $G(x-ct)$ is a wave of fixed shape moving to the right with speed $c$, and $F(x+ct)$ one moving to the left; such solutions are **traveling wave solutions**. So $c$ is indeed the speed of propagation, as claimed in [2.5.1](/2.5.1#sec-1.2.1).

### 3.1.2. d'Alembert's Formula

**Theorem 3.1.2 (d'Alembert's Formula)** Let $\varphi\in C^2(\mathbb{R})$ and $\psi\in C^1(\mathbb{R})$. The initial value problem

$$
u_{tt}=c^2u_{xx},\quad x\in\mathbb{R},\ t>0,\qquad u(x,0)=\varphi(x),\quad u_t(x,0)=\psi(x)\tag{3.2}
$$
has exactly one solution $u\in C^2(\mathbb{R}\times[0,+\infty))$, given by

$$
u(x,t)=\frac12\big[\varphi(x+ct)+\varphi(x-ct)\big]+\frac{1}{2c}\int_{x-ct}^{x+ct}\psi(s)\,\mathrm{d}s.\tag{3.3}
$$

**Proof** By Theorem 3.1.1 (whose proof works equally well on the half-plane $t\ge0$), any solution has the form $u=F(x+ct)+G(x-ct)$. The initial conditions require

$$
F(x)+G(x)=\varphi(x),\qquad c\big(F'(x)-G'(x)\big)=\psi(x).
$$
Integrating the second equation from $0$ to $x$ gives $F(x)-G(x)=\frac1c\int_0^x\psi(s)\,\mathrm{d}s+K$ with a constant $K$, and therefore

$$
F(x)=\frac12\varphi(x)+\frac{1}{2c}\int_0^x\psi\,\mathrm{d}s+\frac K2,\qquad G(x)=\frac12\varphi(x)-\frac{1}{2c}\int_0^x\psi\,\mathrm{d}s-\frac K2.
$$
Substituting $x+ct$ into $F$ and $x-ct$ into $G$ and adding, the constants cancel and we obtain Eq. (3.3). So any solution must be given by Eq. (3.3), which proves uniqueness. Conversely, under the stated regularity Eq. (3.3) defines a $C^2$ function of the form (3.1), hence a solution, and it satisfies $u(x,0)=\varphi(x)$ and $u_t(x,0)=\frac12\big[c\varphi'(x)-c\varphi'(x)\big]+\frac{1}{2c}\big[c\psi(x)+c\psi(x)\big]=\psi(x)$. $\square$

The formula has a simple reading: the initial displacement splits into two halves that travel in opposite directions, and the initial velocity contributes the average of $\psi$ over the interval $[x-ct,x+ct]$, multiplied by $t$.

**Example 3.1.1** Solve Eq. (3.2) with $\varphi(x)=x^2$ and $\psi(x)=\sin x$.

**Solution** By Eq. (3.3),

$$
u=\frac12\big[(x+ct)^2+(x-ct)^2\big]+\frac{1}{2c}\big[\cos(x-ct)-\cos(x+ct)\big]=x^2+c^2t^2+\frac1c\sin x\,\sin ct.
$$
Check: $u_{tt}=2c^2-c\sin x\sin ct=c^2u_{xx}$.

**Example 3.1.2 (The Plucked String)** Let $\psi=0$ and let $\varphi$ be a triangle of height $h$ on $[-a,a]$: $\varphi(x)=h(1-\lvert x\rvert/a)$ for $\lvert x\rvert\le a$ and $0$ otherwise. Then $u=\frac12[\varphi(x+ct)+\varphi(x-ct)]$: the triangle splits into two triangles of height $h/2$ moving apart; they separate completely at time $t=a/c$, after which the string between them is at rest.

**Example 3.1.3 (The Hammer Blow)** Let $\varphi=0$ and $\psi=1$ on $(-a,a)$, $\psi=0$ elsewhere (a hammer strikes the segment $(-a,a)$). Then

$$
u(x,t)=\frac{1}{2c}\,\big\lvert(x-ct,x+ct)\cap(-a,a)\big\rvert,
$$
where $\lvert\cdot\rvert$ is the length of an interval. For $t>a/c$, the profile is a trapezoid of height $a/c$ whose flat top $\lvert x\rvert<ct-a$ widens with speed $c$: unlike the plucked string, the struck string does not return to rest, it is displaced permanently.

![d'Alembert's formula. Left: a plucked string splits into two half-height pulses. Right: a pulse on a semi-infinite string with a fixed end at x = 0 is reflected upside down (odd extension)](./plots/dalembert-reflection.py)

In these two examples the data are not $C^2$ (the triangle has corners, the velocity jumps), so Eq. (3.3) is not a classical solution. It is a generalized solution: the uniform limit of classical solutions with smoothed data, and a solution in the integral sense. The examples show what happens to singularities: the corners of the triangle travel along the characteristics through the corners at $t=0$. For the wave equation, singularities of the data persist and propagate along characteristics, in contrast to the heat equation, which smooths them out instantly ([2.5.4](/2.5.4#sec-4.2)).

### 3.1.3. Domain of Dependence and Range of Influence

Eq. (3.3) shows that $u(x_0,t_0)$ depends only on the values of $\varphi$ at the two points $x_0\pm ct_0$ and of $\psi$ on the interval between them.

**Definition 3.1.1 (Domain of Dependence, Domain of Determinacy and Range of Influence)** For the wave equation $u_{tt}=c^2u_{xx}$:

1. the interval $[x_0-ct_0,x_0+ct_0]$ on the $x$-axis is called the **domain of dependence** of the point $(x_0,t_0)$;
2. for an interval $[a,b]$, the triangle $\{(x,t)\colon a+ct\le x\le b-ct,\ t\ge0\}$ bounded by the characteristics $x-ct=a$ and $x+ct=b$ is called the **domain of determinacy** of $[a,b]$;
3. the region $\{(x,t)\colon a-ct\le x\le b+ct,\ t\ge0\}$ is called the **range of influence** of $[a,b]$.

The data on $[a,b]$ determine the solution in the domain of determinacy completely, whatever the data outside; and data on $[a,b]$ can affect the solution only in its range of influence. In particular, if $\varphi$ and $\psi$ vanish outside $[a,b]$, then $u(x,t)=0$ for $x>b+ct$ and $x<a-ct$: disturbances travel at most with speed $c$. This *finite speed of propagation* is the hallmark of hyperbolic equations.

![Left: the domain of dependence of (x₀, t₀) is the base of the characteristic triangle. Middle: the domain of determinacy of [a, b]. Right: the range of influence of [a, b], bounded by the characteristics x = a - ct and x = b + ct](./plots/dependence-influence.py)

## 3.2. The Semi-Infinite String and the Method of Reflection

### 3.2.1. A Fixed End

Now let the string occupy $x\ge0$, with the end $x=0$ held fixed:

$$
\begin{cases}u_{tt}=c^2u_{xx},&x>0,\ t>0,\\u(0,t)=0,&t\ge0,\\u(x,0)=\varphi(x),\quad u_t(x,0)=\psi(x),&x\ge0.\end{cases}\tag{3.4}
$$
The idea is to extend the data to the whole line so that the solution of the extended problem automatically vanishes at $x=0$. Take the **odd extensions**

$$
\varphi_{\mathrm{o}}(x)=\begin{cases}\varphi(x),&x\ge0,\\-\varphi(-x),&x<0,\end{cases}\qquad\psi_{\mathrm{o}}(x)=\begin{cases}\psi(x),&x\ge0,\\-\psi(-x),&x<0.\end{cases}
$$
If $u$ solves the initial value problem with odd data, so does $-u(-x,t)$; by uniqueness, $u(-x,t)=-u(x,t)$, and in particular $u(0,t)=0$. Applying d'Alembert's formula to $\varphi_{\mathrm{o}},\psi_{\mathrm{o}}$ and rewriting it in terms of $\varphi,\psi$ (for $x<ct$, the part of the integral over $[x-ct,ct-x]$ cancels by oddness) gives the following.

**Theorem 3.2.1** Let $\varphi\in C^2[0,+\infty)$ and $\psi\in C^1[0,+\infty)$ satisfy the compatibility conditions $\varphi(0)=\varphi''(0)=\psi(0)=0$. Then problem (3.4) has a unique $C^2$ solution:

$$
u(x,t)=\begin{cases}\dfrac12\big[\varphi(x+ct)+\varphi(x-ct)\big]+\dfrac{1}{2c}\displaystyle\int_{x-ct}^{x+ct}\psi(s)\,\mathrm{d}s,&x\ge ct,\\[2ex]\dfrac12\big[\varphi(x+ct)-\varphi(ct-x)\big]+\dfrac{1}{2c}\displaystyle\int_{ct-x}^{x+ct}\psi(s)\,\mathrm{d}s,&0\le x<ct.\end{cases}\tag{3.5}
$$

The compatibility conditions are exactly what makes the odd extensions $C^2$ and $C^1$: the odd extension of a function is continuous at $0$ only if the function vanishes there; its first derivative is then automatically continuous, but its second derivative is odd, so it is continuous at $0$ only if $\varphi''(0)=0$. (They are also necessary: $u(0,t)=0$ for all $t$ forces $u_{tt}(0,t)=0$, hence $c^2\varphi''(0)=u_{tt}(0,0)=0$.)

In the region $x\ge ct$, the characteristics through $(x,t)$ have not yet reached the boundary, and the end has no effect. For $x<ct$, the term $-\frac12\varphi(ct-x)$ is a left-moving wave that has been reflected at $x=0$: a fixed end reflects a pulse with the opposite sign, as in the right part of the figure in §3.1.2.

### 3.2.2. A Free End

If instead the end slides freely ($u_x(0,t)=0$, the Neumann condition, [2.5.1](/2.5.1#sec-1.3.2)), the **even extensions** of $\varphi,\psi$ produce a solution that is even in $x$, hence has $u_x(0,t)=0$. For $0\le x<ct$ this gives

$$
u(x,t)=\frac12\big[\varphi(x+ct)+\varphi(ct-x)\big]+\frac{1}{2c}\Big[\int_0^{x+ct}\psi(s)\,\mathrm{d}s+\int_0^{ct-x}\psi(s)\,\mathrm{d}s\Big],\tag{3.6}
$$
with compatibility conditions $\varphi'(0)=\psi'(0)=0$. At a free end, a pulse is reflected with the same sign.

### 3.2.3. A Finite String

For a string $0\le x\le l$ fixed at both ends, the data are reflected at both ends: extend $\varphi$ and $\psi$ to be odd about $x=0$ and about $x=l$, which makes them odd and $2l$-periodic. d'Alembert's formula applied to these extensions solves the problem. Since the extended data are $2l$-periodic, the solution is periodic in time with period $2l/c$: a pulse travels to one end, is reflected, travels to the other end, is reflected again, and returns to its original shape. The same solution is written as a **Fourier sine series** in [2.5.4](/2.5.4#sec-4.1).

## 3.3. The Nonhomogeneous Equation: Duhamel's Principle

Consider a string driven by an external force:

$$
u_{tt}=c^2u_{xx}+f(x,t),\quad x\in\mathbb{R},\ t>0,\qquad u(x,0)=\varphi(x),\quad u_t(x,0)=\psi(x).\tag{3.7}
$$
By the **superposition principle**, $u=u_1+u_2$, where $u_1$ solves the homogeneous equation with the given data (d'Alembert's formula) and $u_2$ solves Eq. (3.7) with zero data. The second problem is reduced to the first by the following idea: the force acting during the short time interval $[s,s+\mathrm{d}s]$ changes the velocity of the string by $f(x,s)\,\mathrm{d}s$ without changing its position; this velocity then propagates as a free wave. The solution is the superposition of all these free waves.

**Theorem 3.3.1 (Duhamel's Principle)** Suppose that for each $s\ge0$ the function $w(x,t;s)$ solves the homogeneous problem

$$
w_{tt}=c^2w_{xx}\ \ (t>s),\qquad w(x,s;s)=0,\qquad w_t(x,s;s)=f(x,s),
$$
and that $w$, $w_t$, $w_{tt}$ and $w_{xx}$ are continuous in $(x,t,s)$. Then

$$
u(x,t)=\int_0^tw(x,t;s)\,\mathrm{d}s\tag{3.8}
$$
solves $u_{tt}=c^2u_{xx}+f$ with $u(x,0)=u_t(x,0)=0$.

**Proof** By **differentiation under the integral sign** with a variable upper limit, and $w(x,t;t)=0$,

$$
u_t=w(x,t;t)+\int_0^tw_t(x,t;s)\,\mathrm{d}s=\int_0^tw_t(x,t;s)\,\mathrm{d}s.
$$
Differentiating again and using $w_t(x,t;t)=f(x,t)$,

$$
u_{tt}=f(x,t)+\int_0^tw_{tt}(x,t;s)\,\mathrm{d}s=f(x,t)+c^2\int_0^tw_{xx}(x,t;s)\,\mathrm{d}s=f(x,t)+c^2u_{xx}.
$$
Clearly $u(x,0)=0$, and $u_t(x,0)=0$ by the first formula. $\square$

By d'Alembert's formula (with time origin $s$), $w(x,t;s)=\frac{1}{2c}\int_{x-c(t-s)}^{x+c(t-s)}f(y,s)\,\mathrm{d}y$. Adding the solution of the homogeneous problem gives the complete solution of Eq. (3.7).

**Theorem 3.3.2** Let $\varphi\in C^2(\mathbb{R})$, $\psi\in C^1(\mathbb{R})$, and let $f$ and $f_x$ be continuous. The unique $C^2$ solution of problem (3.7) is

$$
u(x,t)=\frac12\big[\varphi(x+ct)+\varphi(x-ct)\big]+\frac{1}{2c}\int_{x-ct}^{x+ct}\psi(y)\,\mathrm{d}y+\frac{1}{2c}\iint_{\Delta(x,t)}f(y,s)\,\mathrm{d}y\,\mathrm{d}s,\tag{3.9}
$$
where $\Delta(x,t)=\{(y,s)\colon0\le s\le t,\ \lvert y-x\rvert\le c(t-s)\}$ is the characteristic triangle with vertex $(x,t)$.

The domain of dependence now includes the whole characteristic triangle: the solution at $(x,t)$ feels the force only at points from which a signal traveling with speed at most $c$ can reach $(x,t)$. Uniqueness follows from the energy method of §3.4.

**Example 3.3.1** Solve $u_{tt}=c^2u_{xx}+\sin x$ with $u(x,0)=u_t(x,0)=0$.

**Solution** By Eq. (3.9),

$$
u=\frac{1}{2c}\int_0^t\Big[\cos\big(x-c(t-s)\big)-\cos\big(x+c(t-s)\big)\Big]\,\mathrm{d}s=\frac{\sin x}{c}\int_0^t\sin c(t-s)\,\mathrm{d}s=\frac{\sin x\,(1-\cos ct)}{c^2}.
$$
Check: $u_{tt}=\sin x\cos ct$ and $c^2u_{xx}+\sin x=-\sin x\,(1-\cos ct)+\sin x=\sin x\cos ct$. The string oscillates about the static deflection $\frac{\sin x}{c^2}$, which solves $c^2u_{xx}+\sin x=0$.

## 3.4. Energy and Uniqueness

### 3.4.1. Conservation of Energy

For a string with density $\rho$ and tension $T=\rho c^2$, the kinetic energy of the piece $[x,x+\mathrm{d}x]$ is $\frac12\rho u_t^2\,\mathrm{d}x$, and its potential energy (the work done against the tension in stretching it from length $\mathrm{d}x$ to $\sqrt{1+u_x^2}\,\mathrm{d}x\approx(1+\frac12u_x^2)\,\mathrm{d}x$) is $\frac12Tu_x^2\,\mathrm{d}x$. Dividing by $\rho$, we define the energy of a solution on an interval $I$ as

$$
E(t)=\frac12\int_I\big(u_t^2+c^2u_x^2\big)\,\mathrm{d}x.\tag{3.10}
$$

**Theorem 3.4.1 (Conservation of Energy)** Let $u\in C^2([0,l]\times[0,T])$ solve $u_{tt}=c^2u_{xx}$ and satisfy at each end either the Dirichlet condition $u=0$ or the Neumann condition $u_x=0$. Then $E(t)=\frac12\int_0^l(u_t^2+c^2u_x^2)\,\mathrm{d}x$ is constant. The same holds on $I=\mathbb{R}$ for a solution that vanishes for $\lvert x\rvert$ large at each time (for example, when $\varphi$ and $\psi$ have bounded support).

**Proof** Differentiating under the integral sign, using the equation and integrating by parts,

$$
E'(t)=\int_0^l\big(u_tu_{tt}+c^2u_xu_{xt}\big)\,\mathrm{d}x=c^2\int_0^l\big(u_tu_{xx}+u_xu_{xt}\big)\,\mathrm{d}x=c^2\int_0^l\big(u_tu_x\big)_x\,\mathrm{d}x=c^2\Big[u_tu_x\Big]_{x=0}^{x=l}.
$$
At a Dirichlet end $u=0$ for all $t$, hence $u_t=0$; at a Neumann end $u_x=0$. In either case the boundary term vanishes. On $\mathbb{R}$, the boundary term vanishes because $u$ vanishes outside a bounded set at each time (by finite propagation speed). $\square$

For a Robin end $u_x(l,t)+\alpha u(l,t)=0$ with $\alpha>0$, the boundary term is $c^2u_tu_x=-\frac{c^2\alpha}{2}\frac{\mathrm{d}}{\mathrm{d}t}u(l,t)^2$, so the conserved quantity is $E(t)+\frac{c^2\alpha}{2}u(l,t)^2$, the energy of the string plus the potential energy of the spring.

**Theorem 3.4.2 (Uniqueness)** The initial-boundary value problem

$$
u_{tt}=c^2u_{xx}+f,\quad0<x<l,\qquad u(x,0)=\varphi(x),\quad u_t(x,0)=\psi(x),
$$
with a Dirichlet, Neumann or Robin ($\alpha>0$) condition at each end, has at most one solution $u\in C^2([0,l]\times[0,T])$.

**Proof** The difference $w$ of two solutions solves the homogeneous equation with homogeneous boundary conditions and zero initial data. Its energy (with the spring terms in the Robin case) is conserved and equals $0$ at $t=0$. Since the energy is a sum of nonnegative terms, $w_t\equiv0$ and $w_x\equiv0$, so $w$ is constant, and $w(x,0)=0$ gives $w\equiv0$. $\square$

This is the *energy method*: to prove uniqueness, find a nonnegative quantity that vanishes initially and does not increase.

### 3.4.2. Energy in a Shrinking Interval

For the initial value problem on the whole line, with no decay assumption on the data, a local version of the energy argument gives uniqueness and finite speed of propagation at the same time.

**Theorem 3.4.3** Let $u\in C^2$ solve $u_{tt}=c^2u_{xx}$, and fix $(x_0,t_0)$ with $t_0>0$. Then the energy in the shrinking interval

$$
e(t)=\frac12\int_{x_0-c(t_0-t)}^{x_0+c(t_0-t)}\big(u_t^2+c^2u_x^2\big)\,\mathrm{d}x,\qquad0\le t\le t_0,
$$
is nonincreasing. In particular, if $\varphi=\psi=0$ on the domain of dependence $[x_0-ct_0,x_0+ct_0]$, then $u=0$ in the whole characteristic triangle with vertex $(x_0,t_0)$.

**Proof** Write $\alpha(t)=x_0-c(t_0-t)$ and $\beta(t)=x_0+c(t_0-t)$, so $\alpha'=c$ and $\beta'=-c$. Differentiating the integral with variable limits and integrating by parts as in Theorem 3.4.1,

$$
e'(t)=c^2\Big[u_tu_x\Big]_\alpha^\beta-\frac c2\big(u_t^2+c^2u_x^2\big)\Big|_{\beta}-\frac c2\big(u_t^2+c^2u_x^2\big)\Big|_{\alpha}=-\frac c2\big(u_t-cu_x\big)^2\Big|_{\beta}-\frac c2\big(u_t+cu_x\big)^2\Big|_{\alpha}\le0.
$$
If the data vanish on the base, then $e(0)=0$, hence $e(t)=0$ for $0\le t\le t_0$; so $u_t=u_x=0$ in the triangle, and $u$ is constant there, equal to its value $0$ on the base. $\square$

Applied to the difference of two solutions, Theorem 3.4.3 shows that the solution of the initial value problem (3.2) is unique without any condition at infinity, and that the values in a characteristic triangle are determined by the data on its base. The same argument works for variable coefficients and in higher dimensions (with cones in place of triangles), where no explicit formula is available; this is why energy estimates are the basic tool of the theory of hyperbolic equations.

### 3.4.3. Continuous Dependence

**Theorem 3.4.4** Let $u_1,u_2$ be the solutions of the initial value problem (3.2) with data $(\varphi_1,\psi_1)$ and $(\varphi_2,\psi_2)$. Then for $0\le t\le T$,

$$
\sup_{x}\lvert u_1(x,t)-u_2(x,t)\rvert\le\sup_x\lvert\varphi_1-\varphi_2\rvert+T\sup_x\lvert\psi_1-\psi_2\rvert.
$$

**Proof** Apply d'Alembert's formula to $u_1-u_2$, which solves Eq. (3.2) with data $(\varphi_1-\varphi_2,\psi_1-\psi_2)$: the first term is bounded by $\sup\lvert\varphi_1-\varphi_2\rvert$, and the integral by $\frac{1}{2c}\cdot2ct\sup\lvert\psi_1-\psi_2\rvert$. $\square$

Together with Theorem 3.1.2, this shows that the initial value problem for the one-dimensional wave equation is well-posed ([2.5.1](/2.5.1#def-1.4.1)) on every finite time interval. In higher dimensions, the energy

$$
E(t)=\frac12\iiint_{\mathbb{R}^3}\big(u_t^2+c^2\lvert\nabla u\rvert^2\big)\,\mathrm{d}V
$$
is conserved by the same computation, with integration by parts replaced by **Green's first identity** ([2.2.14](/2.2.14#thm-14.5.2)), and gives uniqueness for initial-boundary value problems in bounded regions.

## 3.5. Waves in Three and Two Dimensions

### 3.5.1. Spherical Means and Kirchhoff's Formula

In three dimensions we cannot factor the wave operator, but we can reduce the problem to one dimension by averaging over spheres. For a continuous function $g$ on $\mathbb{R}^3$, a point $x$ and $r>0$, the *spherical mean* is

$$
M_g(x,r)=\frac{1}{4\pi r^2}\iint_{\lvert y-x\rvert=r}g(y)\,\mathrm{d}S_y=\frac{1}{4\pi}\iint_{\lvert\omega\rvert=1}g(x+r\omega)\,\mathrm{d}S_\omega,
$$
the average of $g$ over the sphere of radius $r$ centered at $x$. As $r\to0$, $M_g(x,r)\to g(x)$.

**Lemma 3.5.1** Let $u\in C^2$ solve $u_{tt}=c^2\Delta u$ in $\mathbb{R}^3\times\mathbb{R}$, and let $M(r,t)=M_{u(\cdot,t)}(x,r)$ for a fixed $x$. Then

$$
M_{tt}=c^2\Big(M_{rr}+\frac2rM_r\Big),\tag{3.11}
$$
and consequently $v(r,t)=rM(r,t)$ solves the one-dimensional wave equation $v_{tt}=c^2v_{rr}$ for $r>0$, with $v(0,t)=0$.

**Proof** Differentiating the second form of the mean under the integral sign and applying the **divergence theorem** to the ball $B_r=\{\lvert y-x\rvert<r\}$,

$$
M_r=\frac1{4\pi}\iint_{\lvert\omega\rvert=1}\nabla u(x+r\omega)\cdot\omega\,\mathrm{d}S_\omega=\frac{1}{4\pi r^2}\iint_{\partial B_r}\frac{\partial u}{\partial\boldsymbol{n}}\,\mathrm{d}S=\frac{1}{4\pi r^2}\iiint_{B_r}\Delta u\,\mathrm{d}V=\frac{1}{4\pi c^2r^2}\iiint_{B_r}u_{tt}\,\mathrm{d}V.
$$
Thus $r^2M_r=\frac{1}{4\pi c^2}\int_0^r\Big(\iint_{\lvert y-x\rvert=\rho}u_{tt}\,\mathrm{d}S\Big)\mathrm{d}\rho$, and differentiating in $r$,

$$
\big(r^2M_r\big)_r=\frac{1}{4\pi c^2}\iint_{\lvert y-x\rvert=r}u_{tt}\,\mathrm{d}S=\frac{r^2}{c^2}M_{tt},
$$
which is Eq. (3.11). Finally $v_{rr}=rM_{rr}+2M_r$, so Eq. (3.11) multiplied by $r$ reads $v_{tt}=c^2v_{rr}$; and $v(0,t)=0$ since $M$ is bounded near $r=0$. $\square$

Eq. (3.11) is the wave equation for radial functions: $M_{rr}+\frac2rM_r$ is the Laplacian of a radial function in **spherical coordinates** ([2.2.14](/2.2.14#sec-14.6)).

**Theorem 3.5.1 (Kirchhoff's Formula)** Let $\varphi\in C^3(\mathbb{R}^3)$ and $\psi\in C^2(\mathbb{R}^3)$. The solution of

$$
u_{tt}=c^2\Delta u,\quad x\in\mathbb{R}^3,\ t>0,\qquad u(x,0)=\varphi(x),\quad u_t(x,0)=\psi(x)
$$
is

$$
u(x,t)=\frac{\partial}{\partial t}\bigg(\frac{1}{4\pi c^2t}\iint_{\lvert y-x\rvert=ct}\varphi(y)\,\mathrm{d}S_y\bigg)+\frac{1}{4\pi c^2t}\iint_{\lvert y-x\rvert=ct}\psi(y)\,\mathrm{d}S_y.\tag{3.12}
$$

**Proof** (Derivation.) Fix $x$ and let $v=rM$ as in Lemma 3.5.1. Then $v$ solves the wave equation on the half-line $r>0$ with a fixed end at $r=0$ and the initial data $v(r,0)=rM_\varphi(x,r)$, $v_t(r,0)=rM_\psi(x,r)$. By the reflection formula (3.5), for $0\le r<ct$,

$$
v(r,t)=\frac12\Big[(ct+r)M_\varphi(x,ct+r)-(ct-r)M_\varphi(x,ct-r)\Big]+\frac1{2c}\int_{ct-r}^{ct+r}\rho\,M_\psi(x,\rho)\,\mathrm{d}\rho.
$$
Now $u(x,t)=\lim_{r\to0}M(r,t)=\lim_{r\to0}\frac{v(r,t)}{r}=v_r(0,t)$, and differentiating at $r=0$,

$$
u(x,t)=\frac{\mathrm{d}}{\mathrm{d}\rho}\big[\rho M_\varphi(x,\rho)\big]_{\rho=ct}+t\,M_\psi(x,ct)=\frac{\partial}{\partial t}\big[t\,M_\varphi(x,ct)\big]+t\,M_\psi(x,ct).
$$
Since $tM_g(x,ct)=\frac{1}{4\pi c^2t}\iint_{\lvert y-x\rvert=ct}g\,\mathrm{d}S$, this is Eq. (3.12). One verifies directly that Eq. (3.12) defines a $C^2$ solution under the stated hypotheses. $\square$

For example, $\varphi=0$ and $\psi\equiv1$ give $u=\frac{4\pi c^2t^2}{4\pi c^2t}=t$, as they should. Note the loss of regularity: $\varphi\in C^3$ is needed for $u\in C^2$, because the first term involves a derivative of the spherical mean. In three dimensions, unlike in one, a singularity of the data can be focused and become stronger.

The striking feature of Kirchhoff's formula is that $u(x,t)$ depends only on the data on the sphere $\lvert y-x\rvert=ct$, not on the data inside it. Suppose the data vanish outside a ball of radius $a$ about a point at distance $R>a$ from $x$. Then $u(x,t)=0$ for $t<(R-a)/c$, because the sphere has not yet reached the ball, and again for $t>(R+a)/c$, because it has passed beyond it. A sharp signal arrives with a sharp front and leaves with a sharp back. This is *Huygens' principle* (in its strong form), and it is the reason why sound in three-dimensional space carries speech and music undistorted.

**Example 3.5.1** Let $\varphi=0$ and $\psi=1$ in the ball $\lvert y\rvert<a$, $\psi=0$ outside. At the center, the sphere $\lvert y\rvert=ct$ lies inside the ball for $ct<a$ and outside for $ct>a$, so

$$
u(0,t)=\begin{cases}t,&0<t<a/c,\\0,&t>a/c.\end{cases}
$$
The center moves up with unit speed and then stops abruptly and returns to its rest position at the instant $t=a/c$, when the wave from the boundary of the ball arrives. (The solution is discontinuous because the data are; with smoothed data, it is smooth.)

### 3.5.2. The Method of Descent: Two Dimensions

A solution of the two-dimensional wave equation can be regarded as a solution of the three-dimensional equation that does not depend on $x_3$. Applying Kirchhoff's formula to such data and projecting the sphere $\lvert y-x\rvert=ct$ onto the plane, each hemisphere is the graph of a function over the disk $\lvert y-x\rvert\le ct$ with surface element $\mathrm{d}S=\frac{ct}{\sqrt{c^2t^2-\lvert y-x\rvert^2}}\,\mathrm{d}y$. The two hemispheres together give the following formula; this is Hadamard's *method of descent*.

**Theorem 3.5.2 (Poisson's Formula)** Let $\varphi\in C^3(\mathbb{R}^2)$ and $\psi\in C^2(\mathbb{R}^2)$. The solution of $u_{tt}=c^2(u_{x_1x_1}+u_{x_2x_2})$, $u(x,0)=\varphi(x)$, $u_t(x,0)=\psi(x)$ is

$$
u(x,t)=\frac{\partial}{\partial t}\bigg(\frac{1}{2\pi c}\iint_{\lvert y-x\rvert<ct}\frac{\varphi(y)\,\mathrm{d}y}{\sqrt{c^2t^2-\lvert y-x\rvert^2}}\bigg)+\frac{1}{2\pi c}\iint_{\lvert y-x\rvert<ct}\frac{\psi(y)\,\mathrm{d}y}{\sqrt{c^2t^2-\lvert y-x\rvert^2}}.\tag{3.13}
$$

Now the domain of dependence of $(x,t)$ is the whole disk $\lvert y-x\rvert\le ct$, not just its boundary. A localized disturbance still arrives with a sharp front at $t=(R-a)/c$, but it never stops completely.

**Example 3.5.2** Let $\varphi=0$ and $\psi=1$ in the disk $\lvert y\rvert<a$, $\psi=0$ outside. At the center, in polar coordinates,

$$
u(0,t)=\frac{1}{2\pi c}\int_0^{b}\frac{2\pi r\,\mathrm{d}r}{\sqrt{c^2t^2-r^2}}=\frac1c\Big(ct-\sqrt{c^2t^2-b^2}\Big),\qquad b=\min(ct,a).
$$
For $ct<a$ this is $t$, as in three dimensions; but for $ct>a$ it is $t-\sqrt{t^2-a^2/c^2}\approx\frac{a^2}{2c^2t}$, which decays only like $1/t$. This is the behavior of ripples on a pond after a stone is thrown in: the surface keeps trembling long after the main wave has passed. Huygens' principle holds in odd dimensions $n\ge3$ and fails in all even dimensions; in one dimension, the struck string of Example 3.1.3 is the extreme case of a permanent displacement.

![Response at a point at distance R = 3 from a region of radius a = 1 given unit initial velocity (c = 1). In 3D the signal is confined to R - a < t < R + a (Huygens' principle); in 2D it has a long tail; in 1D the displacement is permanent](./plots/huygens-dimensions.py)

## Summary

| Problem | Formula | Key facts |
|---|---|---|
| General solution in 1D | $u=F(x+ct)+G(x-ct)$ | two traveling waves; characteristics $x\pm ct=\text{const}$ |
| Initial value problem in 1D | d'Alembert's formula (3.3) | domain of dependence $[x-ct,x+ct]$; finite speed of propagation; singularities propagate along characteristics |
| Half-line | odd (fixed end) or even (free end) extension, formulas (3.5), (3.6) | reflection with or without change of sign; compatibility conditions |
| Source term | Duhamel's principle, Eq. (3.9) | the force acts through the characteristic triangle |
| Uniqueness and stability | energy $\frac12\int(u_t^2+c^2u_x^2)$ conserved; nonincreasing on shrinking intervals | well-posedness |
| 3D | Kirchhoff's formula (3.12): averages over the sphere $\lvert y-x\rvert=ct$ | Huygens' principle: sharp fronts and backs |
| 2D | Poisson's formula (3.13): weighted averages over the disk | sharp front, slowly decaying tail |
