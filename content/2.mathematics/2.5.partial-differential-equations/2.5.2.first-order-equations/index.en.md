---
title: First-Order Equations and the Method of Characteristics
---

First-order equations are the simplest partial differential equations, and the only ones that can be solved, in principle, by ordinary differential equations alone. The key idea is already in [2.4.14](/2.4.14): a solution of the linear homogeneous equation $\sum f_iu_{x_i}=0$ is constant along the **characteristic curves**, the integral curves of the vector field $\boldsymbol{f}$, so solving the partial differential equation reduces to solving the characteristic system and prescribing one value on each characteristic. This chapter develops that idea into the *method of characteristics*. We begin with the transport equation, where the characteristics are the paths of particles carried by a flow; then we treat general quasilinear equations and the Cauchy problem, where data are given on a curve and the decisive condition is that the curve be transversal to the characteristics. Nonlinearity brings a new phenomenon: for the Burgers equation the characteristics cross in finite time, the smooth solution breaks down, and a shock wave forms. We end with fully nonlinear equations and Charpit's method, which completes the discussion of complete integrals begun with the Clairaut equation in [2.4.14](/2.4.14#sec-14.5). Characteristics remain central for second-order equations: for the wave equation ([2.5.3](/2.5.3)) they are the lines $x\pm ct=\text{const}$ found in [2.5.1](/2.5.1#sec-1.5.2).

## 2.1. The Transport Equation

### 2.1.1. Constant Speed

Consider a pollutant dissolved in water flowing along a straight channel with constant speed $c$, and let $u(x,t)$ be its concentration. If the pollutant neither diffuses nor decays, its concentration profile is simply carried along with the water. In terms of conservation of mass, the amount in an interval $[a,b]$ changes only through the flux $cu$ entering at $a$ and leaving at $b$: $\frac{\mathrm{d}}{\mathrm{d}t}\int_a^bu\,\mathrm{d}x=cu(a,t)-cu(b,t)$. Differentiating with respect to $b$ gives $u_t=-cu_x$.

**Definition 2.1.1 (Transport Equation)** The equation

$$
u_t+cu_x=0,\qquad x\in\mathbb{R},\ t>0,\tag{2.1}
$$
with a constant $c$, is called the **transport equation** (or advection equation).

The left-hand side of Eq. (2.1) is the **directional derivative** of $u$ in the direction $(c,1)$ of the $(x,t)$-plane, multiplied by $\sqrt{1+c^2}$. So the equation says that $u$ is constant along every line $x-ct=x_0$: these lines are the characteristic curves of Eq. (2.1).

**Theorem 2.1.1** For every $f\in C^1(\mathbb{R})$, the initial value problem $u_t+cu_x=0$, $u(x,0)=f(x)$ has exactly one $C^1$ solution, namely

$$
u(x,t)=f(x-ct).\tag{2.2}
$$

**Proof** The function (2.2) is $C^1$, and $u_t+cu_x=-cf'(x-ct)+cf'(x-ct)=0$, $u(x,0)=f(x)$. Conversely, let $u$ be any $C^1$ solution, and fix $x_0$. Along the characteristic line, $v(t)=u(x_0+ct,t)$ satisfies $v'(t)=cu_x+u_t=0$, so $v(t)=v(0)=f(x_0)$. Every point $(x,t)$ lies on the line with $x_0=x-ct$, hence $u(x,t)=f(x-ct)$. $\square$

The graph of $u(\cdot,t)$ is the graph of $f$ shifted by $ct$: the initial profile travels to the right with speed $c$ (to the left if $c<0$) without changing shape. Solutions of the form $f(x-ct)$ are called traveling waves.

Formula (2.2) makes sense for any function $f$, even a discontinuous one. It is then not a classical solution, but it is the limit of classical solutions with smooth data approximating $f$; such generalized solutions are needed whenever the data have corners or jumps, and they show that for the transport equation a discontinuity in the data propagates along a characteristic.

When there is a source, the same idea works: along a characteristic the equation becomes an ordinary differential equation.

**Theorem 2.1.2** Let $f\in C^1(\mathbb{R})$ and let $g$ and $g_x$ be continuous. The unique $C^1$ solution of

$$
u_t+cu_x=g(x,t),\qquad u(x,0)=f(x)
$$
is

$$
u(x,t)=f(x-ct)+\int_0^tg\big(x-c(t-s),s\big)\,\mathrm{d}s.\tag{2.3}
$$

**Proof** Along the characteristic through $(x,t)$, parametrized as $X(s)=x-c(t-s)$, $0\le s\le t$, the function $v(s)=u(X(s),s)$ satisfies $v'(s)=cu_x+u_t=g(X(s),s)$ and $v(0)=f(x-ct)$; integrating from $0$ to $t$ gives Eq. (2.3), and this also proves uniqueness. That (2.3) is indeed a solution can be checked by **differentiation under the integral sign**. $\square$

The integral in Eq. (2.3) collects the contributions of the source along the path of the fluid particle that arrives at $x$ at time $t$. This is the simplest instance of Duhamel's principle, which reappears for the wave equation in [2.5.3](/2.5.3#sec-3.3).

**Example 2.1.1** A pollutant that decays at rate $\lambda>0$ while being carried by the flow satisfies $u_t+cu_x=-\lambda u$, $u(x,0)=f(x)$. Along a characteristic $X(s)=x_0+cs$ we have $\frac{\mathrm{d}}{\mathrm{d}s}u(X(s),s)=-\lambda u$, so $u$ decays exponentially along each characteristic, and

$$
u(x,t)=f(x-ct)\,\mathrm{e}^{-\lambda t}.
$$

### 2.1.2. Variable Speed

If the speed of the flow depends on position and time, the equation becomes

$$
u_t+a(x,t)u_x=0,\tag{2.4}
$$
with $a$ continuously differentiable. Along a curve $x=X(t)$ we have $\frac{\mathrm{d}}{\mathrm{d}t}u(X(t),t)=u_x X'+u_t$, which vanishes when $X'(t)=a(X(t),t)$. So the characteristic curves of Eq. (2.4) are the solutions of the ordinary differential equation

$$
\frac{\mathrm{d}x}{\mathrm{d}t}=a(x,t),\tag{2.5}
$$
the paths of the fluid particles, and $u$ is constant along each of them. By the **existence and uniqueness theorem**, exactly one characteristic passes through each point, so characteristics never cross. To solve the initial value problem with $u(x,0)=f(x)$, we follow the characteristic through $(x,t)$ back to the time $t=0$, where it starts at some point $x_0(x,t)$, and set $u(x,t)=f(x_0(x,t))$.

**Example 2.1.2** Solve $u_t+xu_x=0$, $u(x,0)=f(x)$.

**Solution** The characteristics satisfy $\frac{\mathrm{d}x}{\mathrm{d}t}=x$, so $x=x_0\mathrm{e}^t$, and following them back gives $x_0=x\mathrm{e}^{-t}$. Hence

$$
u(x,t)=f(x\mathrm{e}^{-t}).
$$
Check: $u_t=-x\mathrm{e}^{-t}f'(x\mathrm{e}^{-t})$ and $xu_x=x\mathrm{e}^{-t}f'(x\mathrm{e}^{-t})$. The flow $a(x,t)=x$ moves particles away from the origin ever faster, so the initial profile is stretched by the factor $\mathrm{e}^t$.

![Transport along characteristics. Left: for u_t + u_x = 0 the characteristics are parallel lines and the profile moves rigidly. Right: for u_t + x u_x = 0 the characteristics x = x₀eᵗ fan out and the profile is stretched](./plots/transport-characteristics.py)

## 2.2. Quasilinear Equations

### 2.2.1. Characteristic Curves and Integral Surfaces

We now consider the general quasilinear equation in two independent variables

$$
P(x,y,u)\,u_x+Q(x,y,u)\,u_y=R(x,y,u),\tag{2.6}
$$
where $P,Q,R$ are continuously differentiable and $P,Q$ do not vanish simultaneously. A solution $u(x,y)$ is represented geometrically by its graph $z=u(x,y)$ in $(x,y,z)$-space, called an integral surface of Eq. (2.6). At each point the vector $(u_x,u_y,-1)$ is a **normal vector** of the surface, and Eq. (2.6) says

$$
(P,Q,R)\cdot(u_x,u_y,-1)=0.
$$
That is, the vector field $(P,Q,R)$ on $(x,y,z)$-space, called the characteristic direction field, is tangent to every integral surface.

**Definition 2.2.1 (Characteristics of a Quasilinear Equation)** The integral curves of the system

$$
\frac{\mathrm{d}x}{\mathrm{d}s}=P(x,y,z),\qquad\frac{\mathrm{d}y}{\mathrm{d}s}=Q(x,y,z),\qquad\frac{\mathrm{d}z}{\mathrm{d}s}=R(x,y,z)\tag{2.7}
$$
in $(x,y,z)$-space are called the **characteristic curves** of Eq. (2.6), and their projections onto the $(x,y)$-plane are called the projected characteristics. Eliminating the parameter $s$, the system takes the symmetric form $\dfrac{\mathrm{d}x}{P}=\dfrac{\mathrm{d}y}{Q}=\dfrac{\mathrm{d}z}{R}$.

For a linear equation ($P,Q$ independent of $z$), the projected characteristics do not depend on the solution; for a quasilinear equation they do, because $P$ and $Q$ depend on $z=u$. The following theorem is the geometric heart of the method.

**Theorem 2.2.1** Let $u\in C^2$ be a solution of Eq. (2.6) with integral surface $S$. If a characteristic curve has one point on $S$, it lies entirely on $S$ (as long as it stays in the domain of $u$). Consequently every integral surface is a union of characteristic curves.

**Proof** Let $(x(s),y(s),z(s))$ be the characteristic curve with $z(0)=u(x(0),y(0))$, and set $U(s)=z(s)-u(x(s),y(s))$. Then $(x,y,U)$ solves the system

$$
x'=P(x,y,u+U),\qquad y'=Q(x,y,u+U),\qquad U'=R(x,y,u+U)-u_x(x,y)P(x,y,u+U)-u_y(x,y)Q(x,y,u+U),
$$
where $u,u_x,u_y$ are evaluated at $(x,y)$. Its right-hand side is $C^1$, since $u\in C^2$. On the other hand, let $(\tilde x(s),\tilde y(s))$ solve $\tilde x'=P(\tilde x,\tilde y,u(\tilde x,\tilde y))$, $\tilde y'=Q(\tilde x,\tilde y,u(\tilde x,\tilde y))$ with the same initial point. Because $u$ solves Eq. (2.6), $(\tilde x,\tilde y,0)$ also solves the system above, with the same initial values $U(0)=0$. By the existence and uniqueness theorem the two solutions coincide, so $U\equiv0$: the characteristic stays on $S$. $\square$

Conversely, a surface swept out by a one-parameter family of characteristic curves is an integral surface, since the characteristic direction is tangent to it. This is the method of characteristics: build the solution surface out of characteristic curves. If two independent **first integrals** $\Psi_1(x,y,z)$ and $\Psi_2(x,y,z)$ of the system (2.7) are known, each characteristic is given by $\Psi_1=C_1$, $\Psi_2=C_2$, and a one-parameter family of them is obtained by imposing a relation between the constants; this gives Lagrange's general solution

$$
G\big(\Psi_1(x,y,u),\Psi_2(x,y,u)\big)=0\tag{2.8}
$$
with an arbitrary function $G$, as in [2.4.14](/2.4.14#sec-14.2). The general solution is rarely the end of the matter: in practice $G$ must be determined from data.

### 2.2.2. The Cauchy Problem

**Definition 2.2.2 (Cauchy Problem)** Let $\Gamma_0\colon x=x_0(\tau)$, $y=y_0(\tau)$ ($\tau\in I$) be a $C^1$ curve in the $(x,y)$-plane and $u_0(\tau)$ a $C^1$ function. The Cauchy problem for Eq. (2.6) is to find a solution $u$ defined near $\Gamma_0$ with

$$
u\big(x_0(\tau),y_0(\tau)\big)=u_0(\tau),\qquad\tau\in I.
$$
Geometrically, we seek an integral surface containing the space curve $\Gamma\colon(x_0(\tau),y_0(\tau),u_0(\tau))$. The curve $\Gamma_0$ is said to satisfy the **noncharacteristic condition** at $\tau$ if

$$
P\big(x_0,y_0,u_0\big)\,y_0'(\tau)-Q\big(x_0,y_0,u_0\big)\,x_0'(\tau)\ne0,\tag{2.9}
$$
that is, if the projected characteristic through that point is not tangent to $\Gamma_0$.

The initial value problem $u(x,0)=f(x)$ of §2.1 is the special case $x_0(\tau)=\tau$, $y_0(\tau)=0$ (with $y$ playing the role of $t$); then (2.9) reads $Q\ne0$, which holds for Eq. (2.1) since $Q=1$.

**Theorem 2.2.2 (Local Existence and Uniqueness)** Let $P,Q,R\in C^1$, let $x_0,y_0,u_0\in C^1(I)$, and suppose the noncharacteristic condition (2.9) holds at $\tau=\tau_0$. Then in a neighborhood of the point $(x_0(\tau_0),y_0(\tau_0))$ the Cauchy problem has exactly one $C^1$ solution.

**Proof** For each $\tau$ solve the characteristic system (2.7) with the initial values $(x_0(\tau),y_0(\tau),u_0(\tau))$ at $s=0$. This gives functions $x(s,\tau)$, $y(s,\tau)$, $z(s,\tau)$ that are $C^1$ in both variables by the differentiable dependence of solutions on initial values ([2.4.7](/2.4.7)). At $s=0$ their Jacobian determinant is

$$
\frac{\partial(x,y)}{\partial(s,\tau)}\bigg|_{s=0}=x_sy_\tau-y_sx_\tau=P\,y_0'-Q\,x_0'\ne0.
$$
By the **inverse function theorem**, near $(0,\tau_0)$ the map $(s,\tau)\mapsto(x,y)$ has a $C^1$ inverse $s=s(x,y)$, $\tau=\tau(x,y)$. Set $u(x,y)=z(s(x,y),\tau(x,y))$. For $s=0$ this gives the data. Moreover, by the chain rule and Eq. (2.7),

$$
R=z_s=u_xx_s+u_yy_s=Pu_x+Qu_y,
$$
so $u$ solves Eq. (2.6). Uniqueness: if $u$ is a $C^2$ solution with the given data, its integral surface contains $\Gamma$, and by Theorem 2.2.1 it contains every characteristic curve through $\Gamma$, so it coincides with the surface just constructed. (Uniqueness also holds for $C^1$ solutions, by a slightly more careful argument.) $\square$

If $\Gamma_0$ is characteristic, that is, $Py_0'-Qx_0'\equiv0$ along it, the data cannot be prescribed freely: if $\Gamma$ itself is a characteristic curve, there are infinitely many integral surfaces through it; if $\Gamma_0$ is a projected characteristic but $\Gamma$ is not a characteristic curve, there is no solution, because the equation already determines how $u$ varies along $\Gamma_0$.

### 2.2.3. Examples

**Example 2.2.1** Solve $u_x+2xu_y=y$, $u(0,y)=f(y)$.

**Solution** The data curve is $x_0=0$, $y_0=\tau$, $u_0=f(\tau)$, and $Py_0'-Qx_0'=1\ne0$: noncharacteristic everywhere. The characteristic system is $x_s=1$, $y_s=2x$, $z_s=y$, with solution

$$
x=s,\qquad y=\tau+s^2,\qquad z=f(\tau)+\tau s+\frac{s^3}{3}.
$$
Inverting, $s=x$ and $\tau=y-x^2$, hence

$$
u(x,y)=f(y-x^2)+(y-x^2)x+\frac{x^3}{3}=f(y-x^2)+xy-\frac23x^3.
$$
Check: $u_x=-2xf'+y-2x^2$ and $u_y=f'+x$, so $u_x+2xu_y=y$. The projected characteristics are the parabolas $y-x^2=\text{const}$, each crossing the $y$-axis exactly once.

**Example 2.2.2 (Characteristic Data)** Consider $yu_x-xu_y=0$. The characteristic system $x_s=y$, $y_s=-x$, $z_s=0$ shows that the projected characteristics are the circles $x^2+y^2=r^2$ (the equation says that $u$ is invariant under rotations about the origin), and $u$ is constant on each. With data on the positive $x$-axis, $u(x,0)=f(x)$ for $x>0$, the unique solution is $u=f\big(\sqrt{x^2+y^2}\big)$. If the data are prescribed on the whole $x$-axis, every circle meets it twice, so a solution exists only if $f(-x)=f(x)$. At the origin the noncharacteristic condition fails: $Py_0'-Qx_0'=y_0\cdot0+x_0\cdot1=x_0=0$ there.

**Example 2.2.3** Solve $(y+u)u_x+yu_y=x-y$ with $u=1+x$ on the line $y=1$.

**Solution** The data curve $x_0=\tau$, $y_0=1$ gives $Py_0'-Qx_0'=-y_0=-1\ne0$: noncharacteristic. We find first integrals of $\frac{\mathrm{d}x}{y+z}=\frac{\mathrm{d}y}{y}=\frac{\mathrm{d}z}{x-y}$ by integrable combinations ([2.4.14](/2.4.14#sec-14.1.3)). Adding the first and third ratios, $\frac{\mathrm{d}(x+z)}{x+z}=\frac{\mathrm{d}y}{y}$, so $\Psi_1=\frac{x+z}{y}$. Subtracting them, $\frac{\mathrm{d}(x-z)}{\mathrm{d}s}=2y-(x-z)$ with $y=C\mathrm{e}^s$, which gives $x-z=y+C'\mathrm{e}^{-s}$ and hence $\Psi_2=y(x-z-y)$. On the data curve, $\Psi_2=1\cdot(\tau-1-\tau-1)=-2$, for every $\tau$. So the integral surface through $\Gamma$ is $y(x-u-y)=-2$, that is,

$$
u(x,y)=x-y+\frac2y,\qquad y>0.
$$
Check: $u_x=1$, $u_y=-1-\frac2{y^2}$, and $(y+u)-y-\frac2y=x-y$. Here the data determined $G$ in Eq. (2.8) to be $G(\Psi_1,\Psi_2)=\Psi_2+2$.

For $n$ independent variables everything carries over: the equation $\sum_{i=1}^nP_i(x,u)u_{x_i}=R(x,u)$ has the characteristic system $\frac{\mathrm{d}x_i}{\mathrm{d}s}=P_i$, $\frac{\mathrm{d}z}{\mathrm{d}s}=R$, the data are given on a hypersurface of dimension $n-1$, and the noncharacteristic condition says that the projected characteristic direction $(P_1,\dots,P_n)$ is not tangent to it.

## 2.3. The Inviscid Burgers Equation and Shock Waves

### 2.3.1. Breaking of Waves

The simplest nonlinear version of the transport equation lets the speed depend on the transported quantity itself.

**Definition 2.3.1 (Burgers Equation)** The quasilinear equation

$$
u_t+uu_x=0\tag{2.10}
$$
is called the inviscid **Burgers' equation**. (With a viscous term $\nu u_{xx}$ on the right-hand side it is the viscous Burgers equation.)

It describes a one-dimensional stream of particles that do not interact, each moving with constant velocity: $u(x,t)$ is the velocity of the particle at $x$ at time $t$, and $u_t+uu_x$ is its acceleration. The characteristic system $\frac{\mathrm{d}t}{\mathrm{d}s}=1$, $\frac{\mathrm{d}x}{\mathrm{d}s}=u$, $\frac{\mathrm{d}u}{\mathrm{d}s}=0$ shows that $u$ is constant along each characteristic, so the characteristics are straight lines. For the initial condition $u(x,0)=f(x)$, the characteristic starting at $x_0$ is

$$
x=x_0+f(x_0)\,t,\qquad\text{with}\qquad u=f(x_0)\ \text{on it},\tag{2.11}
$$
and eliminating $x_0$ gives the implicit form of the solution, $u=f(x-ut)$. Faster parts of the profile overtake slower parts. If $f$ is increasing, the characteristics fan out and the wave spreads; if $f$ decreases somewhere, the characteristics from that part converge and eventually cross, and at a crossing point two different values of $u$ are carried in: the solution can no longer be single-valued.

**Theorem 2.3.1 (Breaking Time)** Let $f\in C^1(\mathbb{R})$ with $f$ and $f'$ bounded.

1. If $f'\ge0$ everywhere, the initial value problem for Eq. (2.10) with $u(x,0)=f(x)$ has a unique $C^1$ solution for all $t\ge0$.
2. If $\inf f'<0$, a $C^1$ solution exists for $0\le t<T^*$, where

$$
T^*=-\frac{1}{\inf_{x}f'(x)},\tag{2.12}
$$
and it cannot be continued as a $C^1$ solution beyond $T^*$: if the infimum is attained at $x_0$, then $u_x\to-\infty$ along the characteristic from $x_0$ as $t\to T^*$.

**Proof** For fixed $t$, consider the map $x_0\mapsto x=x_0+f(x_0)t$. Its derivative is $1+f'(x_0)t$, which is positive for all $x_0$ if $f'\ge0$, or if $0\le t<T^*$. Since $f$ is bounded, $x\to\pm\infty$ as $x_0\to\pm\infty$, so the map is a $C^1$ bijection of $\mathbb{R}$ with $C^1$ inverse $x_0(x,t)$: through every point $(x,t)$ passes exactly one characteristic. Set $u(x,t)=f(x_0(x,t))$. Differentiating $x_0+f(x_0)t=x$ gives

$$
\frac{\partial x_0}{\partial x}=\frac{1}{1+f'(x_0)t},\qquad\frac{\partial x_0}{\partial t}=-\frac{f(x_0)}{1+f'(x_0)t},
$$
hence

$$
u_t+uu_x=f'(x_0)\frac{\partial x_0}{\partial t}+f(x_0)f'(x_0)\frac{\partial x_0}{\partial x}=0,\qquad u_x=\frac{f'(x_0)}{1+f'(x_0)t}.\tag{2.13}
$$
Uniqueness follows from Theorem 2.2.1, since every solution is constant along the characteristics (2.11). Finally, if $f'(x_0)=\inf f'<0$, Eq. (2.13) shows $u_x\to-\infty$ along that characteristic as $t\to T^*$. $\square$

**Example 2.3.1** For $f(x)=\mathrm{e}^{-x^2}$ we have $f'(x)=-2x\mathrm{e}^{-x^2}$, whose minimum is attained at $x=\frac{1}{\sqrt2}$ and equals $-\sqrt2\,\mathrm{e}^{-1/2}$. The breaking time is

$$
T^*=\frac{\mathrm{e}^{1/2}}{\sqrt2}=\sqrt{\frac{\mathrm e}{2}}\approx1.166.
$$
The front of the hump steepens, becomes vertical at $t=T^*$, and afterwards the formula (2.11) describes a multivalued "breaking wave", like a wave overturning on a beach.

![Burgers' equation with u(x, 0) = exp(-x²). Left: the characteristics x = x₀ + f(x₀)t cross after the breaking time T* ≈ 1.17. Right: the profile steepens and becomes multivalued for t > T*; the shock (dashed) replaces the overturned part](./plots/burgers-breaking.py)

### 2.3.2. Conservation Laws and Shocks

For a physical quantity, a multivalued profile is meaningless; what actually forms is a discontinuity, a *shock wave*. To describe it we must return to the integral form of the balance law, from which the differential equation was derived. Eq. (2.10) can be written as $u_t+\big(\frac12u^2\big)_x=0$, a special case of

$$
u_t+F(u)_x=0,\tag{2.14}
$$
which is called a *conservation law* with flux $F$: integrating over $[a,b]$,

$$
\frac{\mathrm{d}}{\mathrm{d}t}\int_a^bu(x,t)\,\mathrm{d}x=F\big(u(a,t)\big)-F\big(u(b,t)\big),\tag{2.15}
$$
so the total amount of $u$ in $[a,b]$ changes only through the fluxes at the ends. The integral form (2.15) makes sense for discontinuous $u$. A function that satisfies Eq. (2.15) for all $a<b$ (and is piecewise $C^1$) is called a *weak solution* of Eq. (2.14); it satisfies the differential equation wherever it is smooth.

**Theorem 2.3.2 (Rankine–Hugoniot Condition)** Let $u$ be a weak solution of Eq. (2.14) that is $C^1$ on both sides of a $C^1$ curve $x=\xi(t)$, with one-sided limits $u_l$ (left) and $u_r$ (right) on the curve. Then

$$
\xi'(t)=\frac{F(u_l)-F(u_r)}{u_l-u_r}.\tag{2.16}
$$
For the Burgers equation, $F(u)=\frac12u^2$ and the shock speed is $\xi'=\frac12(u_l+u_r)$.

**Proof** Take $a<\xi(t)<b$ and split $\int_a^b=\int_a^{\xi(t)}+\int_{\xi(t)}^b$. Differentiating with respect to $t$ (the variable limits contribute $\xi'u_l$ and $-\xi'u_r$) and using $u_t=-F(u)_x$ on each side,

$$
\frac{\mathrm{d}}{\mathrm{d}t}\int_a^bu\,\mathrm{d}x=\xi'u_l+\big[F(u(a,t))-F(u_l)\big]-\xi'u_r+\big[F(u_r)-F(u(b,t))\big].
$$
Comparing with Eq. (2.15) gives $\xi'(u_l-u_r)=F(u_l)-F(u_r)$. $\square$

**Example 2.3.2 (Riemann Problems)** Solve the Burgers equation with the piecewise constant initial data $u(x,0)=u_l$ for $x<0$ and $u(x,0)=u_r$ for $x>0$.

1. $u_l=1$, $u_r=0$. The characteristics $x=x_0+t$ from $x_0<0$ run into the vertical characteristics from $x_0>0$. A shock with speed $\frac12(1+0)=\frac12$ resolves the conflict:

$$
u(x,t)=\begin{cases}1,&x<t/2,\\0,&x>t/2.\end{cases}
$$
2. $u_l=0$, $u_r=1$. The same formula with the shock $x=t/2$ is again a weak solution, but in it characteristics emanate from the shock, as if information were created there. The other weak solution is the continuous *rarefaction wave*

$$
u(x,t)=\begin{cases}0,&x\le0,\\x/t,&0<x<t,\\1,&x\ge t,\end{cases}
$$
in which a fan of characteristics through the origin fills the gap (check: $u=x/t$ gives $u_t+uu_x=-\frac{x}{t^2}+\frac xt\cdot\frac1t=0$). This is the physically correct solution: it is the limit of solutions of the viscous Burgers equation as $\nu\to0$, and it is what one observes.

![Riemann problems for Burgers' equation in the (x, t)-plane. Left: u_l = 1 > u_r = 0, the characteristics run into a shock x = t/2. Right: u_l = 0 < u_r = 1, a rarefaction fan u = x/t](./plots/riemann-problems.py)

Weak solutions are therefore not unique, and an additional selection principle is needed. For the Burgers equation it is the *entropy condition* $u_l>\xi'>u_r$: characteristics must run into a shock from both sides, never out of it. With this condition the initial value problem for Eq. (2.14) with convex flux $F$ has exactly one weak solution (Oleinik, Kruzhkov), and its theory is a large part of modern gas dynamics.

The same mathematics describes traffic. If $\rho(x,t)$ is the density of cars on a road and the speed of the cars is $v(\rho)=v_{\max}(1-\rho/\rho_{\max})$, conservation of cars gives $\rho_t+F(\rho)_x=0$ with $F(\rho)=\rho\,v(\rho)$. A shock is the sudden braking at the back of a traffic jam; a rarefaction wave is the gradual dissolution of a queue at a traffic light that turns green.

## 2.4. Fully Nonlinear Equations

A fully nonlinear first-order equation in two variables has the form

$$
F(x,y,u,p,q)=0,\qquad p=u_x,\quad q=u_y.\tag{2.17}
$$
Now the equation does not prescribe a direction at each point of the solution surface, but only a one-parameter family of possible tangent planes (a "Monge cone"). The method of characteristics still works if the unknowns along a characteristic are taken to be not only $(x,y,u)$ but also the tangent plane $(p,q)$: a curve together with a field of tangent planes along it is called a characteristic strip. Differentiating Eq. (2.17) along a strip leads to the Lagrange–Charpit system

$$
\frac{\mathrm{d}x}{F_p}=\frac{\mathrm{d}y}{F_q}=\frac{\mathrm{d}u}{pF_p+qF_q}=-\frac{\mathrm{d}p}{F_x+pF_u}=-\frac{\mathrm{d}q}{F_y+qF_u}.\tag{2.18}
$$
For a quasilinear equation $F=Pp+Qq-R$, the first three ratios reduce to the system (2.7).

Instead of the general Cauchy problem we describe how Eq. (2.18) yields a **complete integral**, a two-parameter family of solutions $u=\Phi(x,y;a,b)$ ([2.4.14](/2.4.14#sec-14.5)); all other solutions can then be obtained as envelopes.

*Charpit's method* consists of three steps.

1. Find one first integral $\Phi(x,y,u,p,q)=a$ of the system (2.18), independent of $F$ (often from the last two ratios).
2. Solve $F=0$ and $\Phi=a$ for $p=p(x,y,u;a)$ and $q=q(x,y,u;a)$.
3. The **Pfaffian equation** $\mathrm{d}u=p\,\mathrm{d}x+q\,\mathrm{d}y$ is then **completely integrable** (this is what the first integral guarantees); integrating it gives the complete integral, with a second constant $b$.

**Example 2.4.1 (Eikonal Equation)** Find a complete integral of $u_x^2+u_y^2=1$.

**Solution** Here $F=p^2+q^2-1$, so $F_x=F_y=F_u=0$, and the last two ratios of Eq. (2.18) give $\mathrm{d}p=\mathrm{d}q=0$: $p$ is a first integral. Setting $p=\cos\alpha$ gives $q=\sin\alpha$, and $\mathrm{d}u=\cos\alpha\,\mathrm{d}x+\sin\alpha\,\mathrm{d}y$ integrates to the complete integral

$$
u=x\cos\alpha+y\sin\alpha+b,
$$
a family of planes of slope $1$. The envelope of the one-parameter subfamily $b=0$ is obtained from $\frac{\partial}{\partial\alpha}(x\cos\alpha+y\sin\alpha)=0$, that is, $\tan\alpha=\frac yx$, and gives $u=\pm\sqrt{x^2+y^2}$: the distance to the origin, a cone. In geometric optics, $u$ is the travel time of light in a homogeneous medium, its level curves are wave fronts, and the projected characteristics, the rays, are straight lines perpendicular to the fronts.

**Example 2.4.2** Find a complete integral of $u_xu_y=u$.

**Solution** Here $F=pq-u$, $F_p=q$, $F_q=p$, $F_u=-1$, $F_x=F_y=0$, and the last two ratios of Eq. (2.18) are $\frac{\mathrm{d}p}{p}=\frac{\mathrm{d}q}{q}$. Hence $\frac pq=a$ is a first integral. From $p=aq$ and $pq=u$ we get $q=\sqrt{u/a}$ and $p=\sqrt{au}$ (for $a,u>0$), so

$$
\mathrm{d}u=\sqrt{au}\,\mathrm{d}x+\sqrt{\frac ua}\,\mathrm{d}y,\qquad\frac{\mathrm{d}u}{\sqrt u}=\sqrt a\,\mathrm{d}x+\frac{\mathrm{d}y}{\sqrt a}.
$$
Integrating, $2\sqrt u=\sqrt a\,x+\frac{y}{\sqrt a}+b$, that is,

$$
u=\frac{(ax+y+c)^2}{4a},\qquad c=b\sqrt a.
$$
Check: $u_x=\frac{ax+y+c}{2}$ and $u_y=\frac{ax+y+c}{2a}$, whose product is $u$.

For the **Clairaut equation** $u=xp+yq+f(p,q)$ ([2.4.14](/2.4.14#sec-14.5)), Eq. (2.18) gives $\mathrm{d}p=\mathrm{d}q=0$ directly, which explains why its complete integral is the family of planes $u=ax+by+f(a,b)$. The Hamilton–Jacobi equation of classical mechanics, $S_t+H(x,\nabla S)=0$, is a fully nonlinear first-order equation of the same kind; for it the characteristic system (2.18) is exactly Hamilton's equations of motion.

## Summary

| Equation | Characteristics | Solution |
|---|---|---|
| $u_t+cu_x=g$ | lines $x-ct=\text{const}$ | $u=f(x-ct)+\int_0^tg(x-c(t-s),s)\,\mathrm{d}s$ |
| $u_t+a(x,t)u_x=0$ | particle paths $\frac{\mathrm{d}x}{\mathrm{d}t}=a$ | $u=f(x_0(x,t))$, constant along characteristics |
| $Pu_x+Qu_y=R$ | $\frac{\mathrm{d}x}{P}=\frac{\mathrm{d}y}{Q}=\frac{\mathrm{d}u}{R}$ | general solution $G(\Psi_1,\Psi_2)=0$; Cauchy problem solvable near noncharacteristic data, $Py_0'-Qx_0'\ne0$ |
| $u_t+uu_x=0$ | lines $x=x_0+f(x_0)t$ | $u=f(x-ut)$ until $T^*=-1/\inf f'$; then shocks with speed $\frac12(u_l+u_r)$, or rarefaction fans |
| $F(x,y,u,p,q)=0$ | characteristic strips, system (2.18) | complete integral by Charpit's method; other solutions as envelopes |

- Integral surfaces are unions of characteristic curves (Theorem 2.2.1); this gives both the construction and the uniqueness of solutions.
- Data on a characteristic curve cannot be prescribed freely; transversality of the data curve to the characteristics is what makes the Cauchy problem well-posed.
- For nonlinear equations the characteristics depend on the solution and can cross; the classical solution then ceases to exist, and the integral form of the conservation law, the Rankine–Hugoniot condition and the entropy condition determine the shock.
