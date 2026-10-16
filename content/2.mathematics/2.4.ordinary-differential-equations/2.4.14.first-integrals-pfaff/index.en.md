---
title: First Integrals and Pfaffian Equations
source_hash: 4539db37b208
---

The general integral $u(x,y)=C$ of a first-order equation $M\,\mathrm{d}x+N\,\mathrm{d}y=0$ is a function that stays constant along every integral curve ([2.4.2](/2.4.2)). This chapter extends this point of view to higher dimensions in two directions.

The first direction is systems of equations. For an $n$-dimensional autonomous system, a function that stays constant along solutions is called a first integral; energy, momentum and angular momentum in physics are all first integrals. If enough first integrals are known, the trajectories are the intersections of their level sets, and the system can be solved by quadratures. First integrals are precisely the solutions of a first-order linear partial differential equation, which is the starting point of the method of characteristics for partial differential equations ([2.5](/2.5)).

The second direction is the higher-dimensional form of "exact equations": the Pfaffian equation $P\,\mathrm{d}x+Q\,\mathrm{d}y+R\,\mathrm{d}z=0$. In two variables every such equation has (locally) an integrating factor; in three or more variables this is no longer true, and only equations satisfying an integrability condition have families of integral surfaces. Two notions must be distinguished here: exactness (the left-hand side is the **total differential** of some function, that is, the vector field is a **conservative vector field**, [2.2.14](/2.2.14#sec-14.4)) and complete integrability (exactness after multiplication by an integrating factor). Finally we discuss the Clairaut equation in several variables, an example of a first-order nonlinear partial differential equation that can be solved completely; the geometric meaning of its singular solution is the same as in the one-variable case ([2.4.6](/2.4.6)).

## 14.1. First Integrals

### 14.1.1. Definition and Criterion

Consider the $n$-dimensional autonomous system

$$
\boldsymbol{x}'=\boldsymbol{f}(\boldsymbol{x}),\qquad\boldsymbol{x}\in D\subset\mathbb{R}^n,\tag{14.1}
$$
where $\boldsymbol{f}=(f_1,\dots,f_n)$ is continuously differentiable on a region $D$. In components, $x_i'=f_i(x_1,\dots,x_n)$, $i=1,\dots,n$.

**Definition 14.1.1 (First Integral)** Let $\Phi\in C^1(D)$ be nonconstant on every open subset of $D$. If $\Phi(\boldsymbol{x}(t))$ is constant (independent of $t$) for every solution $\boldsymbol{x}(t)$ of Eq. (14.1) in $D$, then $\Phi$ is called a **first integral** of the system (14.1) on $D$; the relation $\Phi(\boldsymbol{x})=C$ is also called a first integral.

The term "first" comes from mechanics: a conservation law obtained by integrating a second-order equation of motion once (such as the energy integral) involves velocities but not accelerations; it is a "first integration" of the equation.

**Theorem 14.1.1** A function $\Phi\in C^1(D)$ (not locally constant) is a first integral of Eq. (14.1) if and only if

$$
\sum_{i=1}^nf_i(\boldsymbol{x})\frac{\partial\Phi}{\partial x_i}(\boldsymbol{x})=\nabla\Phi\cdot\boldsymbol{f}=0\tag{14.2}
$$
holds identically on $D$.

**Proof** Along a solution $\boldsymbol{x}(t)$, the chain rule gives $\frac{\mathrm{d}}{\mathrm{d}t}\Phi(\boldsymbol{x}(t))=\nabla\Phi(\boldsymbol{x}(t))\cdot\boldsymbol{f}(\boldsymbol{x}(t))$. If Eq. (14.2) holds, this derivative vanishes and $\Phi$ is constant along solutions. Conversely, for any $\boldsymbol{x}_0\in D$, the **existence and uniqueness theorem** gives a solution through $\boldsymbol{x}_0$; $\Phi$ is constant along it, and differentiating at $t=0$ shows that Eq. (14.2) holds at $\boldsymbol{x}_0$. $\square$

Geometrically, Eq. (14.2) says that the vector field $\boldsymbol{f}$ is everywhere tangent to the level sets of $\Phi$ (orthogonal to the **gradient** $\nabla\Phi$), so every trajectory lies on some level set $\Phi=C$.

**Example 14.1.1** The pendulum equation $\theta''+\sin\theta=0$ becomes the system $x'=y$, $y'=-\sin x$ (with $x=\theta$, $y=\theta'$). The function $\Phi(x,y)=\frac12y^2-\cos x$ satisfies $y\Phi_x-\sin x\,\Phi_y=y\sin x-y\sin x=0$, so it is a first integral: this is conservation of mechanical energy. The trajectories are the level curves of the energy: for $\Phi<1$ they are closed curves around the equilibrium (oscillation), for $\Phi>1$ they are the upper and lower wavy curves (rotation), and for $\Phi=1$ they are the separatrices joining the saddles $(\pm\pi,0)$.

![The trajectories of the pendulum x' = y, y' = -sin x are the level curves of the first integral y²/2 - cos x](./plots/pendulum-first-integral.py)

**Example 14.1.2** Consider the Lotka–Volterra predator–prey model $x'=x(\alpha-\beta y)$, $y'=y(-\gamma+\delta x)$ ($x,y>0$, positive parameters). Separating variables in $\frac{\mathrm{d}y}{\mathrm{d}x}=\frac{y(-\gamma+\delta x)}{x(\alpha-\beta y)}$ gives the first integral

$$
\Phi(x,y)=\delta x-\gamma\ln x+\beta y-\alpha\ln y,
$$
which can be verified directly with Eq. (14.2). $\Phi$ attains a strict minimum at the equilibrium $(\gamma/\delta,\alpha/\beta)$, and its level curves are closed curves around it, so every positive solution is periodic (see [7.4.4](/7.4.4)).

A nonautonomous system $\boldsymbol{x}'=\boldsymbol{f}(t,\boldsymbol{x})$ can be made autonomous by treating $t$ as an $(n+1)$st unknown function ($t'=1$). First integrals are then functions $\Phi(t,\boldsymbol{x})$, and the criterion becomes $\frac{\partial\Phi}{\partial t}+\sum_if_i\frac{\partial\Phi}{\partial x_i}=0$.

### 14.1.2. Independent First Integrals and Solving the System

**Definition 14.1.2** Let $\Phi_1,\dots,\Phi_k$ be first integrals of Eq. (14.1). If the Jacobian matrix $\frac{\partial(\Phi_1,\dots,\Phi_k)}{\partial(x_1,\dots,x_n)}$ has rank $k$ at the point $\boldsymbol{x}_0$, they are said to be **independent** near $\boldsymbol{x}_0$.

Since the gradients of first integrals are all orthogonal to $\boldsymbol{f}$, near a point where $\boldsymbol{f}(\boldsymbol{x}_0)\ne\boldsymbol{0}$ there are at most $n-1$ independent first integrals. In fact there are exactly that many:

**Theorem 14.1.2** If $\boldsymbol{f}(\boldsymbol{x}_0)\ne\boldsymbol{0}$, then in some neighborhood of $\boldsymbol{x}_0$ the system (14.1) has $n-1$ independent first integrals $\Phi_1,\dots,\Phi_{n-1}$; moreover, every first integral in this neighborhood can be written as $\Phi=G(\Phi_1,\dots,\Phi_{n-1})$ for some $C^1$ function $G$.

The idea of the proof is "straightening out": near $\boldsymbol{x}_0$ take an $(n-1)$-dimensional hyperplane transversal to $\boldsymbol{f}(\boldsymbol{x}_0)$. Each trajectory meets it in exactly one point, and the $n-1$ coordinates of this intersection point are quantities that stay constant along the trajectory; by differentiability of solutions with respect to initial values ([2.4.7](/2.4.7)) and the **implicit function theorem**, they are smooth functions of $\boldsymbol{x}$ and independent. Near an equilibrium ($\boldsymbol{f}(\boldsymbol{x}_0)=\boldsymbol{0}$) such first integrals do not exist in general: near a node, for instance, all trajectories tend to the same point, and a continuous first integral must be constant.

When $n-1$ independent first integrals are known, the trajectories of the system are the intersections $\Phi_1=C_1,\dots,\Phi_{n-1}=C_{n-1}$. Solving for $n-1$ of the variables (by the implicit function theorem) and substituting into the remaining equation $x_n'=f_n$, a single quadrature gives the relation between $t$ and $x_n$. Thus the number of known first integrals determines how far the system can be reduced: each first integral lowers the dimension by one. For a nonautonomous system $\boldsymbol{x}'=\boldsymbol{f}(t,\boldsymbol{x})$, $n$ independent first integrals $\Phi_i(t,\boldsymbol{x})=C_i$ give the **general solution** implicitly.

### 14.1.3. Symmetric Form and Integrable Combinations

Eliminating $t$, the system (14.1) can be written in the symmetric form

$$
\frac{\mathrm{d}x_1}{f_1}=\frac{\mathrm{d}x_2}{f_2}=\cdots=\frac{\mathrm{d}x_n}{f_n}.\tag{14.3}
$$
It describes the integral curves of the direction field $\boldsymbol{f}$ (without regard to parametrization), and all variables play equal roles. A common technique for finding first integrals is to form an *integrable combination*: by the properties of equal ratios, for arbitrary functions $\lambda_1,\dots,\lambda_n$,

$$
\frac{\mathrm{d}x_1}{f_1}=\cdots=\frac{\mathrm{d}x_n}{f_n}=\frac{\lambda_1\,\mathrm{d}x_1+\cdots+\lambda_n\,\mathrm{d}x_n}{\lambda_1f_1+\cdots+\lambda_nf_n}.
$$
If the $\lambda_i$ can be chosen so that the denominator $\sum\lambda_if_i=0$ while the numerator $\sum\lambda_i\,\mathrm{d}x_i$ is the total differential $\mathrm{d}\Phi$ of some function, then $\mathrm{d}\Phi=0$, and $\Phi=C$ is a first integral.

**Example 14.1.3** Find the integral curves of $\dfrac{\mathrm{d}x}{y-z}=\dfrac{\mathrm{d}y}{z-x}=\dfrac{\mathrm{d}z}{x-y}$.

**Solution** Take $\lambda=(1,1,1)$: the denominator is $(y-z)+(z-x)+(x-y)=0$, which gives $\mathrm{d}x+\mathrm{d}y+\mathrm{d}z=0$ and $\Phi_1=x+y+z$. Take $\lambda=(x,y,z)$: the denominator is $x(y-z)+y(z-x)+z(x-y)=0$, which gives $x\,\mathrm{d}x+y\,\mathrm{d}y+z\,\mathrm{d}z=0$ and $\Phi_2=x^2+y^2+z^2$. The two are independent where $\boldsymbol{f}\ne\boldsymbol{0}$, and the integral curves are

$$
x+y+z=C_1,\qquad x^2+y^2+z^2=C_2,
$$
the intersections of planes perpendicular to the line $x=y=z$ with spheres centered at the origin: circles with axis $x=y=z$. The system describes exactly a rigid rotation about the axis $(1,1,1)$, with $\boldsymbol{f}=(1,1,1)\times(x,y,z)$.

![Integral curves of dx/(y - z) = dy/(z - x) = dz/(x - y): the intersections of the planes x + y + z = C₁ with the spheres x² + y² + z² = C₂, all of them circles with axis x = y = z](./plots/symmetric-form-circles.py)

**Example 14.1.4** Find first integrals of $\dfrac{\mathrm{d}x}{xz}=\dfrac{\mathrm{d}y}{yz}=\dfrac{\mathrm{d}z}{-(x^2+y^2)}$.

**Solution** From the first two ratios, $\frac{\mathrm{d}x}{x}=\frac{\mathrm{d}y}{y}$, which gives $\Phi_1=\frac yx$. Taking $\lambda=(x,y,z)$, the denominator is $x^2z+y^2z-z(x^2+y^2)=0$, which gives $\Phi_2=x^2+y^2+z^2$. The integral curves are the intersections of the planes $y=C_1x$ through the $z$-axis with the spheres $x^2+y^2+z^2=C_2$ (parts of great circles).

## 14.2. First Integrals and First-Order Linear Partial Differential Equations

Condition (14.2) is itself an equation for the unknown function $\Phi$. Read the other way round, it is a first-order linear homogeneous **partial differential equation**

$$
\sum_{i=1}^nf_i(\boldsymbol{x})\frac{\partial u}{\partial x_i}=0,\tag{14.4}
$$
and Theorems 14.1.1 and 14.1.2 together give its solution:

**Theorem 14.2.1** Let $\boldsymbol{f}\in C^1(D)$ with $\boldsymbol{f}(\boldsymbol{x}_0)\ne\boldsymbol{0}$, and let $\Phi_1,\dots,\Phi_{n-1}$ be independent first integrals of the system of ordinary differential equations (14.3) near $\boldsymbol{x}_0$. Then near $\boldsymbol{x}_0$, a function $u\in C^1$ is a solution of Eq. (14.4) if and only if

$$
u=G\big(\Phi_1(\boldsymbol{x}),\dots,\Phi_{n-1}(\boldsymbol{x})\big),
$$
where $G$ is an arbitrary $C^1$ function.

**Definition 14.2.1 (Characteristic Curve)** The system of ordinary differential equations (14.3) is called the characteristic system of the partial differential equation (14.4), and its integral curves are called the **characteristic curves** of Eq. (14.4).

The geometric meaning of Theorem 14.2.1 is that solutions of Eq. (14.4) are constant along each characteristic curve. Solving a partial differential equation thus reduces to solving a system of ordinary differential equations and then prescribing "the constant along each characteristic" arbitrarily; initial or boundary conditions are satisfied through the choice of $G$. The general solution of a partial differential equation contains an arbitrary function rather than arbitrary constants.

**Example 14.2.1** Solve $x\dfrac{\partial u}{\partial x}+y\dfrac{\partial u}{\partial y}=0$ ($x\ne0$).

**Solution** The characteristic system is $\frac{\mathrm{d}x}{x}=\frac{\mathrm{d}y}{y}$, with first integral $y/x$, so the general solution is $u=G(y/x)$: a **homogeneous function** of degree zero. The characteristic curves are rays through the origin, and the solutions are constant along the rays.

For a quasilinear equation $\sum_if_i(\boldsymbol{x},u)\frac{\partial u}{\partial x_i}=g(\boldsymbol{x},u)$, we may treat $u$ as a variable as well: if $V(\boldsymbol{x},u)=0$ defines a solution $u$ implicitly, then $V$ satisfies the homogeneous equation in $n+1$ variables $\sum_if_i\frac{\partial V}{\partial x_i}+g\frac{\partial V}{\partial u}=0$, whose characteristic system is

$$
\frac{\mathrm{d}x_1}{f_1}=\cdots=\frac{\mathrm{d}x_n}{f_n}=\frac{\mathrm{d}u}{g}.
$$
Once $n$ independent first integrals $\Psi_1,\dots,\Psi_n$ are found, the general solution is $G(\Psi_1,\dots,\Psi_n)=0$.

**Example 14.2.2** Solve $x\dfrac{\partial u}{\partial x}+y\dfrac{\partial u}{\partial y}=u$ ($x\ne0$).

**Solution** The system $\frac{\mathrm{d}x}{x}=\frac{\mathrm{d}y}{y}=\frac{\mathrm{d}u}{u}$ has the first integrals $\frac yx$ and $\frac ux$, so the general solution is $G\big(\frac yx,\frac ux\big)=0$, that is, $u=x\,H\big(\frac yx\big)$ with $H$ arbitrary: a homogeneous function of degree one. This is exactly the converse of Euler's theorem on homogeneous functions.

## 14.3. Pfaffian Equations in Three Variables

### 14.3.1. Basic Concepts

**Definition 14.3.1 (Pfaffian Equation)** Let $P,Q,R$ be continuously differentiable on a region $D\subset\mathbb{R}^3$ and not simultaneously zero. The equation

$$
P(x,y,z)\,\mathrm{d}x+Q(x,y,z)\,\mathrm{d}y+R(x,y,z)\,\mathrm{d}z=0\tag{14.5}
$$
is called a **Pfaffian equation** in three variables (a total differential equation in three variables). A surface $S\subset D$ is called an **integral surface** of Eq. (14.5) if every tangent vector $(\mathrm{d}x,\mathrm{d}y,\mathrm{d}z)$ at every point of $S$ satisfies Eq. (14.5).

Writing $\boldsymbol{F}=(P,Q,R)$, Eq. (14.5) reads $\boldsymbol{F}\cdot\mathrm{d}\boldsymbol{r}=0$: integral surfaces are the surfaces everywhere orthogonal to the vector field $\boldsymbol{F}$, which is their normal vector. At each point Eq. (14.5) prescribes a plane (perpendicular to $\boldsymbol{F}$), and the question is whether these small planes can be "pieced together" into surfaces.

**Definition 14.3.2 (Exactness and Complete Integrability)** For the Pfaffian equation (14.5):

1. If there is a function $U$ with $\mathrm{d}U=P\,\mathrm{d}x+Q\,\mathrm{d}y+R\,\mathrm{d}z$, Eq. (14.5) is called **exact**;
2. If through every point of $D$ there passes (locally) an integral surface, and these integral surfaces can be written as one family $U(x,y,z)=C$, Eq. (14.5) is called **completely integrable**.

If the equation is exact, $U=C$ is a family of integral surfaces, so exactness implies complete integrability. By the criterion for conservative fields ([2.2.14](/2.2.14#thm-14.4.2)), on a surface-simply-connected region Eq. (14.5) is exact if and only if $\boldsymbol{F}$ is irrotational:

$$
\operatorname{rot}\boldsymbol{F}=\Big(\frac{\partial R}{\partial y}-\frac{\partial Q}{\partial z},\ \frac{\partial P}{\partial z}-\frac{\partial R}{\partial x},\ \frac{\partial Q}{\partial x}-\frac{\partial P}{\partial y}\Big)=\boldsymbol{0},
$$
and then $U$ is a **potential function** of $\boldsymbol{F}$. Complete integrability is much weaker. If $\mu\ne0$ makes $\mu(P\,\mathrm{d}x+Q\,\mathrm{d}y+R\,\mathrm{d}z)=\mathrm{d}U$ exact, $\mu$ is called an **integrating factor** of Eq. (14.5), and $U=C$ is then a family of integral surfaces. Conversely, if a family of integral surfaces $U=C$ (with $\nabla U\ne\boldsymbol{0}$) exists, then $\nabla U$ and $\boldsymbol{F}$ are both normal vectors of the integral surfaces, so $\nabla U=\mu\boldsymbol{F}$ and $\mu$ is an integrating factor. Therefore

$$
\text{completely integrable}\iff\text{an integrating factor exists (locally)}.
$$

A Pfaffian equation $P\,\mathrm{d}x+Q\,\mathrm{d}y=0$ in two variables is always (locally) completely integrable: it is equivalent to the first-order equation $\frac{\mathrm{d}y}{\mathrm{d}x}=-\frac PQ$, whose general integral $U(x,y)=C$ is the family of integral curves, and an integrating factor always exists ([2.4.2](/2.4.2)). In three variables this is no longer the case.

### 14.3.2. The Integrability Condition

**Theorem 14.3.1** The Pfaffian equation (14.5) (with $P,Q,R\in C^1$) is completely integrable if and only if

$$
\boldsymbol{F}\cdot\operatorname{rot}\boldsymbol{F}=P\Big(\frac{\partial R}{\partial y}-\frac{\partial Q}{\partial z}\Big)+Q\Big(\frac{\partial P}{\partial z}-\frac{\partial R}{\partial x}\Big)+R\Big(\frac{\partial Q}{\partial x}-\frac{\partial P}{\partial y}\Big)=0\tag{14.6}
$$
holds identically on $D$.

**Proof** (Necessity, first method.) Let $\mu\boldsymbol{F}=\nabla U$. By $\operatorname{rot}\nabla U=\boldsymbol{0}$ and the formula $\operatorname{rot}(\mu\boldsymbol{F})=\nabla\mu\times\boldsymbol{F}+\mu\operatorname{rot}\boldsymbol{F}$,

$$
\boldsymbol{0}=\nabla\mu\times\boldsymbol{F}+\mu\operatorname{rot}\boldsymbol{F}.
$$
Taking the dot product of both sides with $\boldsymbol{F}$ and using $(\nabla\mu\times\boldsymbol{F})\cdot\boldsymbol{F}=0$ gives $\mu\,\boldsymbol{F}\cdot\operatorname{rot}\boldsymbol{F}=0$, while $\mu\ne0$. $\square$

**Proof** (Necessity, second method.) Suppose $R\ne0$ at some point. Near it, Eq. (14.5) can be written as $\mathrm{d}z=-\frac PR\,\mathrm{d}x-\frac QR\,\mathrm{d}y$, and an integral surface $z=z(x,y)$ satisfies the system of first-order partial differential equations

$$
\frac{\partial z}{\partial x}=-\frac PR=:M_1(x,y,z),\qquad\frac{\partial z}{\partial y}=-\frac QR=:M_2(x,y,z).\tag{14.7}
$$
Since there is an integral surface through every point, $\frac{\partial^2z}{\partial x\partial y}=\frac{\partial^2z}{\partial y\partial x}$ holds at every point. Expanding by the chain rule and substituting Eq. (14.7):

$$
\frac{\partial M_2}{\partial x}+\frac{\partial M_2}{\partial z}M_1=\frac{\partial M_1}{\partial y}+\frac{\partial M_1}{\partial z}M_2.\tag{14.8}
$$
Substituting $M_1=-P/R$ and $M_2=-Q/R$, multiplying both sides by $R^3$ and simplifying gives exactly Eq. (14.6). Since there is an integral surface through every point, Eq. (14.8) holds at every point of $D$. $\square$

Sufficiency is a special case of the Frobenius theorem (Theorem 14.4.1), and its proof yields the following constructive method.

To find the integral surfaces, assume Eq. (14.6) holds and $R\ne0$. First treat $y$ as a constant ($\mathrm{d}y=0$) and solve the two-variable equation $P\,\mathrm{d}x+R\,\mathrm{d}z=0$, obtaining a general integral $V(x,y,z)=\varphi(y)$, in which the "arbitrary constant" $\varphi(y)$ may depend on $y$. Then require $V(x,y,z)=\varphi(y)$ to satisfy the original equation, which gives an equation for $\varphi$. The integrability condition (14.6) guarantees that $x$ and $z$ can be eliminated from this equation through $V$, leaving a first-order ordinary differential equation in $V$ and $y$ alone; solving it gives the family of integral surfaces.

### 14.3.3. Examples

**Example 14.3.1** Find the family of integral surfaces of $yz\,\mathrm{d}x+2xz\,\mathrm{d}y+xy\,\mathrm{d}z=0$.

**Solution** Here $\boldsymbol{F}=(yz,2xz,xy)$, $\operatorname{rot}\boldsymbol{F}=(x-2x,\,y-y,\,2z-z)=(-x,0,z)$ and $\boldsymbol{F}\cdot\operatorname{rot}\boldsymbol{F}=-xyz+xyz=0$, so the equation is completely integrable (but not exact, since $\operatorname{rot}\boldsymbol{F}\ne\boldsymbol{0}$). Multiplying by the integrating factor $\mu=\frac{1}{xyz}$:

$$
\frac{\mathrm{d}x}{x}+\frac{2\,\mathrm{d}y}{y}+\frac{\mathrm{d}z}{z}=0,
$$
and integration gives $xy^2z=C$.

**Example 14.3.2** Find the family of integral surfaces of $(y^2+yz)\,\mathrm{d}x+(xz+z^2)\,\mathrm{d}y+(y^2-xy)\,\mathrm{d}z=0$.

**Solution** A direct computation verifies Eq. (14.6). Setting $\mathrm{d}y=0$: $y(y+z)\,\mathrm{d}x+y(y-x)\,\mathrm{d}z=0$, that is, $(y+z)\,\mathrm{d}x-(x-y)\,\mathrm{d}z=0$. Dividing by $(y+z)^2$, the left-hand side becomes $\mathrm{d}\Big(\dfrac{x-y}{y+z}\Big)$ (with $y$ regarded as constant), so $V=\dfrac{x-y}{y+z}=\varphi(y)$.

Now regard $y$ as a variable too. A computation gives

$$
(y^2+yz)\,\mathrm{d}x+(xz+z^2)\,\mathrm{d}y+(y^2-xy)\,\mathrm{d}z=y(y+z)^2\,\mathrm{d}V+(x+z)(y+z)\,\mathrm{d}y.
$$
From $x=y+V(y+z)$ we get $x+z=(1+V)(y+z)$, so the original equation becomes $(y+z)^2\big[y\,\mathrm{d}V+(1+V)\,\mathrm{d}y\big]=0$, that is,

$$
\frac{\mathrm{d}V}{1+V}+\frac{\mathrm{d}y}{y}=0,\qquad y(1+V)=C.
$$
Substituting back for $V$, the family of integral surfaces is $\dfrac{y(x+z)}{y+z}=C$. (Correspondingly, $\mu=\frac{1}{(y+z)^2}$ is an integrating factor.)

**Example 14.3.3 (A Nonintegrable Example)** Consider $\mathrm{d}z-y\,\mathrm{d}x=0$. Here $\boldsymbol{F}=(-y,0,1)$, $\operatorname{rot}\boldsymbol{F}=(0,0,1)$ and $\boldsymbol{F}\cdot\operatorname{rot}\boldsymbol{F}=1\ne0$, so the equation is not completely integrable. Geometrically, the plane $\mathrm{d}z=y\,\mathrm{d}x$ at the point $(x,y,z)$ has slope $y$ in the $x$-direction: as we move along the $y$-axis, these planes keep turning about lines parallel to the $y$-axis and cannot be pieced together into surfaces. On the other hand, there are very many curves satisfying Eq. (14.5) (integral curves): one can show that any two points can be joined by such a curve. Equations of this kind are important in thermodynamics (Carathéodory's axiomatization of entropy) and in control theory.

## 14.4. Pfaffian Equations in $n$ Variables and the Frobenius Theorem

A Pfaffian equation in $n$ variables is

$$
\sum_{k=1}^nM_k(x_1,\dots,x_n)\,\mathrm{d}x_k=0.\tag{14.9}
$$
Exactness and complete integrability are defined as in the three-variable case: exactness means that the left-hand side is the total differential of some $U$, and complete integrability means that (locally) there is an integrating factor $\mu$ with $\mu\sum M_k\,\mathrm{d}x_k=\mathrm{d}U$, in which case $U=C$ is a family of $(n-1)$-dimensional integral hypersurfaces.

On a simply connected (for example, convex) region, Eq. (14.9) is exact if and only if

$$
\frac{\partial M_i}{\partial x_j}=\frac{\partial M_j}{\partial x_i},\qquad1\le i<j\le n,\tag{14.10}
$$
which is $\binom n2$ conditions. For $n=3$ this is just $\operatorname{rot}\boldsymbol{F}=\boldsymbol{0}$. Condition (14.10) is only sufficient for complete integrability, not necessary.

**Example 14.4.1** Find the integral surfaces of $\dfrac{m_1\,\mathrm{d}x_1}{x_1}+\dfrac{m_2\,\mathrm{d}x_2}{x_2}+\cdots+\dfrac{m_n\,\mathrm{d}x_n}{x_n}=0$, where $m_1,\dots,m_n$ are real constants and $x_k\ne0$.

**Solution** Each $M_k=m_k/x_k$ depends only on $x_k$, so $\frac{\partial M_i}{\partial x_j}=0=\frac{\partial M_j}{\partial x_i}$ ($i\ne j$) and the equation is exact. Integration gives $\sum_km_k\ln|x_k|=\ln C$, that is, the family of integral hypersurfaces

$$
|x_1|^{m_1}|x_2|^{m_2}\cdots|x_n|^{m_n}=C\quad(C>0).
$$

In general, the condition for complete integrability is stated most concisely in the language of exterior differential forms. Writing $\omega=\sum_kM_k\,\mathrm{d}x_k$, the integrability condition is $\omega\wedge\mathrm{d}\omega=0$; in coordinates, for all $i<j<k$,

$$
M_i\Big(\frac{\partial M_k}{\partial x_j}-\frac{\partial M_j}{\partial x_k}\Big)+M_j\Big(\frac{\partial M_i}{\partial x_k}-\frac{\partial M_k}{\partial x_i}\Big)+M_k\Big(\frac{\partial M_j}{\partial x_i}-\frac{\partial M_i}{\partial x_j}\Big)=0,\tag{14.11}
$$
that is, the three-variable condition (14.6) written out for every three variables $x_i,x_j,x_k$ (with the remaining variables treated as parameters).

**Theorem 14.4.1 (Frobenius Theorem)** Let $M_1,\dots,M_n\in C^1(D)$ be not simultaneously zero. Then the Pfaffian equation (14.9) is completely integrable if and only if Eq. (14.11) holds on $D$.

Necessity is proved in the same way as the first method for the necessity part of Theorem 14.3.1. The general form of the Frobenius theorem asks "when is a field of subspaces spanned by several vector fields the field of tangent spaces of a family of submanifolds"; Pfaffian equations are the case of codimension 1. It is a fundamental theorem of differential geometry.

Another common way of writing the equation is to solve for one variable $u=x_{n+1}$: writing the integral surface as $u=u(x_1,\dots,x_n)$, the equation becomes

$$
\mathrm{d}u=\sum_{k=1}^nM_k(x_1,\dots,x_n,u)\,\mathrm{d}x_k,
$$
which is equivalent to the system of first-order partial differential equations $\frac{\partial u}{\partial x_k}=M_k(\boldsymbol{x},u)$, $k=1,\dots,n$. As in the second method for the necessity part of Theorem 14.3.1, equality of mixed partial derivatives gives the necessary condition for complete integrability

$$
\frac{\partial M_j}{\partial x_i}+\frac{\partial M_j}{\partial u}M_i=\frac{\partial M_i}{\partial x_j}+\frac{\partial M_i}{\partial u}M_j,\qquad1\le i<j\le n,\tag{14.12}
$$
which by the Frobenius theorem is also sufficient: when Eq. (14.12) holds, for every initial value $u(\boldsymbol{x}_0)=u_0$ the system has a unique solution near $\boldsymbol{x}_0$. For $n=2$, Eq. (14.12) is just Eq. (14.8). When none of the $M_k$ depends on $u$, Eq. (14.12) reduces to the exactness condition (14.10).

## 14.5. The Clairaut Equation in Several Variables

The general solution of **Clairaut's equation** $y=xy'+f(y')$ in one variable is the family of lines $y=cx+f(c)$, and its singular solution is the **envelope** of this family ([2.4.6](/2.4.6)). Its generalization to several variables is the first-order nonlinear partial differential equation

$$
z=\sum_{k=1}^np_kx_k+f(p_1,\dots,p_n),\qquad p_k=\frac{\partial z}{\partial x_k},\tag{14.13}
$$
where $f$ is continuously differentiable.

**Definition 14.5.1 (Complete Integral and Singular Integral)** A family of solutions $z=\Phi(\boldsymbol{x};c_1,\dots,c_n)$ of a first-order partial differential equation $F(x_1,\dots,x_n,z,p_1,\dots,p_n)=0$ depending on $n$ independent arbitrary constants $c_1,\dots,c_n$ is called a **complete integral** of the equation; the envelope of the family of complete integrals (if it exists) is also a solution of the equation and is called a **singular integral**.

**Theorem 14.5.1** The Clairaut equation in several variables (14.13) has the complete integral (a family of hyperplanes)

$$
z=\sum_{k=1}^nc_kx_k+f(c_1,\dots,c_n);\tag{14.14}
$$
eliminating $c_1,\dots,c_n$ (when possible) from Eq. (14.14) and

$$
x_k=-\frac{\partial f}{\partial c_k}(c_1,\dots,c_n),\qquad k=1,\dots,n
$$
gives a singular integral.

**Proof** In Eq. (14.14), $p_k=c_k$, and substitution shows that Eq. (14.13) is satisfied. The envelope is found as in the one-variable case: differentiate with respect to the parameters and set the derivatives to zero, $\frac{\partial}{\partial c_k}\big[\sum c_jx_j+f(c)\big]=x_k+\frac{\partial f}{\partial c_k}=0$. On the envelope, $c$ becomes a function of $\boldsymbol{x}$, and these conditions give $\frac{\partial z}{\partial x_k}=c_k+\sum_j\big(x_j+\frac{\partial f}{\partial c_j}\big)\frac{\partial c_j}{\partial x_k}=c_k$, so the envelope also satisfies Eq. (14.13). $\square$

**Example 14.5.1** Find the complete integral and the singular integral of $z=xp+yq+pq$ ($p=z_x$, $q=z_y$).

**Solution** The complete integral is $z=ax+by+ab$. Differentiating with respect to $a,b$ gives $x+b=0$ and $y+a=0$, that is, $a=-y$ and $b=-x$; substituting gives the singular integral

$$
z=(-y)x+(-x)y+(-y)(-x)=-xy.
$$
Direct check: for $z=-xy$ we have $p=-y$, $q=-x$ and $xp+yq+pq=-xy-xy+xy=-xy$. The singular integral is a hyperbolic paraboloid, and every plane of the complete integral is one of its tangent planes.

**Example 14.5.2** Find the singular integral of $z=xp+yq+\sqrt{1+p^2+q^2}$.

**Solution** The complete integral is $z=ax+by+\sqrt{1+a^2+b^2}$. Writing $s=\sqrt{1+a^2+b^2}$, the envelope conditions are $x=-\frac as$ and $y=-\frac bs$, so $x^2+y^2=\frac{a^2+b^2}{s^2}=1-\frac1{s^2}$, while

$$
z=-\frac{a^2+b^2}{s}+s=\frac1s.
$$
Hence $x^2+y^2+z^2=1$ ($z>0$): the singular integral is the upper unit hemisphere. Geometrically, the complete integral consists of all planes at distance $1$ from the origin that lie above it (the distance from the origin to $z=ax+by+s$ is $s/\sqrt{1+a^2+b^2}=1$), and their envelope is naturally the unit sphere.

General first-order nonlinear partial differential equations can also be solved by the method of characteristics (the Lagrange–Charpit method), in which the theory of complete and singular integrals plays a central role; see [2.5](/2.5).

## Summary

| Object | Definition / condition | Method |
|---|---|---|
| First integral $\Phi$ | Constant along solutions ⟺ $\nabla\Phi\cdot\boldsymbol{f}=0$ | Integrable combinations; $n-1$ independent ones near a non-equilibrium point |
| Linear homogeneous PDE $\sum f_iu_{x_i}=0$ | Solutions = arbitrary functions of first integrals | Characteristic system $\frac{\mathrm{d}x_1}{f_1}=\cdots=\frac{\mathrm{d}x_n}{f_n}$ |
| Exact Pfaffian equation | $\omega=\mathrm{d}U$ ⟺ (simply connected) $\operatorname{rot}\boldsymbol{F}=\boldsymbol{0}$ or (14.10) | Find a potential function |
| Completely integrable Pfaffian equation | An integrating factor exists ⟺ $\boldsymbol{F}\cdot\operatorname{rot}\boldsymbol{F}=0$ or (14.11) (Frobenius) | Integrate with one variable fixed, then determine the "constant" |
| Clairaut equation in several variables | $z=\sum p_kx_k+f(\boldsymbol{p})$ | Complete integral: a family of hyperplanes; singular integral: its envelope |
