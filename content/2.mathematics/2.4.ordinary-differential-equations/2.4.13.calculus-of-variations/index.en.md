---
title: Introduction to the Calculus of Variations
source_hash: 1894a564a332
---

Extremum problems in calculus ask for the points at which a function attains an extremum. Many problems in geometry and physics ask instead for the **functions** or curves at which some quantity attains an extremum: the shortest curve joining two points, the curve whose surface of revolution has the least area, the track along which a particle slides down fastest, the curve of given length enclosing the largest area. Such "functions of functions" are called functionals, and the study of their extrema is called the calculus of variations. Its basic result is that an extremal curve must satisfy a second-order ordinary differential equation, the Euler–Lagrange equation. A variational problem thus reduces to a boundary value problem for a differential equation, which is why this chapter belongs in a course on ordinary differential equations; conversely, the equations of motion of mechanics can be viewed as the Euler–Lagrange equations of a functional (Hamilton's principle).

The chapter first gives examples of functionals and variational problems, then derives the Euler–Lagrange equation from the fundamental lemma of the calculus of variations and discusses several cases in which its order can be reduced. We then solve three classical problems: the minimal surface of revolution, the brachistochrone and geodesics on the sphere. Finally we sketch the case of several unknown functions and the constrained isoperimetric problem, which is the infinite-dimensional analogue of the **method of Lagrange multipliers** ([2.2.11](/2.2.11#sec-11.6)).

## 13.1. Functionals and Variational Problems

**Definition 13.1.1 (Functional)** Let $D$ be a class of functions (for example, all $C^1$ functions on $[a,b]$ satisfying given boundary conditions). If to each $y\in D$ there corresponds a real number $J[y]$, then $J$ is called a **functional** on $D$, and $D$ is called the class of admissible functions.

The functionals in this chapter are all of integral type:

$$
J[y]=\int_a^bF\big(x,y(x),y'(x)\big)\,\mathrm{d}x,\qquad D=\{y\in C^1[a,b]\mid y(a)=A,\ y(b)=B\},\tag{13.1}
$$
where $F(x,y,p)$ is a given function of three variables, called the integrand (or Lagrangian). If there exist $y_0\in D$ and $\delta>0$ such that $J[y]\ge J[y_0]$ (or $\le$) for all $y\in D$ with $\max_{[a,b]}|y-y_0|+\max_{[a,b]}|y'-y_0'|<\delta$, then $J$ is said to attain a minimum (or maximum) at $y_0$. Finding the extrema of a functional is called a variational problem, and the subject that studies such problems is the *calculus of variations*.

**Example 13.1.1 (Shortest Curve)** The length of a curve $y=y(x)$ joining two points $(a,A)$ and $(b,B)$ of the plane is

$$
J[y]=\int_a^b\sqrt{1+y'^2}\,\mathrm{d}x.
$$

**Example 13.1.2 (Minimal Surface of Revolution)** Given two points $A(a_1,b_1)$ and $B(a_2,b_2)$ in the upper half-plane with $a_1<a_2$ and $b_1,b_2>0$, rotate a smooth curve $y=y(x)>0$ joining $A$ and $B$ once about the $x$-axis. The area of the resulting surface of revolution is ([2.2.7](/2.2.7))

$$
S[y]=2\pi\int_{a_1}^{a_2}y\sqrt{1+y'^2}\,\mathrm{d}x.\tag{13.2}
$$
Which curve minimizes the area?

**Example 13.1.3 (Brachistochrone)** Let $A,B$ be two points not on the same vertical line, with $A$ higher than $B$. A particle starts from rest at $A$ and slides without friction under gravity along a smooth track joining $A$ and $B$. Which track takes the least time? This problem was posed by Johann Bernoulli in 1696, and the calculus of variations was born from it.

Take $A$ as the origin with the $y$-axis pointing vertically downward, and let $B=(x_B,y_B)$ with $x_B,y_B>0$. By conservation of energy, after the particle has descended a height $y$ its speed is $v=\sqrt{2gy}$; the arc length element is $\mathrm{d}s=\sqrt{1+y'^2}\,\mathrm{d}x$, and the time taken is $\mathrm{d}t=\mathrm{d}s/v$. Hence the total time is

$$
T[y]=\frac{1}{\sqrt{2g}}\int_0^{x_B}\frac{\sqrt{1+y'^2}}{\sqrt y}\,\mathrm{d}x,\tag{13.3}
$$
where $g$ is the gravitational acceleration.

## 13.2. The Euler–Lagrange Equation

### 13.2.1. The Fundamental Lemma of the Calculus of Variations

**Lemma 13.2.1 (Fundamental Lemma of the Calculus of Variations)** Let $f\in C[a,b]$. If

$$
\int_a^bf(x)\eta(x)\,\mathrm{d}x=0
$$
for every $\eta\in C^1[a,b]$ with $\eta(a)=\eta(b)=0$, then $f\equiv0$ on $[a,b]$.

**Proof** Suppose $f(x_0)\ne0$. By continuity we may assume $x_0\in(a,b)$ and $f(x_0)>0$, and there is $\delta>0$ such that $(x_0-\delta,x_0+\delta)\subset[a,b]$ and $f>0$ on this interval. Take

$$
\eta(x)=\begin{cases}(x-x_0+\delta)^2(x_0+\delta-x)^2,&|x-x_0|<\delta,\\0,&\text{otherwise}.\end{cases}
$$
Then $\eta\in C^1[a,b]$, $\eta(a)=\eta(b)=0$ and $\eta>0$ on $(x_0-\delta,x_0+\delta)$, so $\int_a^bf\eta\,\mathrm{d}x=\int_{x_0-\delta}^{x_0+\delta}f\eta\,\mathrm{d}x>0$, a contradiction. $\square$

The lemma says that a continuous function whose integral against "every" test function vanishes must itself be zero. Replacing the squares by higher powers makes $\eta$ smooth to any desired order, so the class of test functions can be taken smaller without changing the conclusion.

### 13.2.2. The Necessary Condition

**Theorem 13.2.1 (Euler–Lagrange Equation)** Suppose $F(x,y,p)$ has continuous second-order partial derivatives, the functional (13.1) attains an extremum at $y_0\in D$, and $y_0\in C^2[a,b]$. Then $y_0$ satisfies

$$
F_y\big(x,y,y'\big)-\frac{\mathrm{d}}{\mathrm{d}x}F_{y'}\big(x,y,y'\big)=0.\tag{13.4}
$$
Here $F_y$ and $F_{y'}$ denote the partial derivatives of $F(x,y,p)$ with respect to its second and third variables, evaluated at $p=y'(x)$.

**Proof** Take any $\eta\in C^1[a,b]$ with $\eta(a)=\eta(b)=0$. Then $y_0+\varepsilon\eta\in D$ for every real $\varepsilon$. The function of one variable $\Phi(\varepsilon)=J[y_0+\varepsilon\eta]$ attains an extremum at $\varepsilon=0$, so $\Phi'(0)=0$. By **differentiation under the integral sign**,

$$
\Phi'(0)=\int_a^b\big(F_y\eta+F_{y'}\eta'\big)\,\mathrm{d}x=0.
$$
Integrating the second term by parts and using $\eta(a)=\eta(b)=0$:

$$
\int_a^bF_{y'}\eta'\,\mathrm{d}x=\Big[F_{y'}\eta\Big]_a^b-\int_a^b\frac{\mathrm{d}}{\mathrm{d}x}F_{y'}\,\eta\,\mathrm{d}x=-\int_a^b\frac{\mathrm{d}}{\mathrm{d}x}F_{y'}\,\eta\,\mathrm{d}x.
$$
Hence $\int_a^b\big(F_y-\frac{\mathrm{d}}{\mathrm{d}x}F_{y'}\big)\eta\,\mathrm{d}x=0$ for all such $\eta$, and Lemma 13.2.1 gives Eq. (13.4). $\square$

The quantity $\Phi'(0)$ is called the *first variation* of the functional $J$ at $y_0$ in the direction $\eta$, denoted $\delta J$. The theorem says that "the first variation vanishes at an extremum", in complete analogy with "the derivative of a differentiable function vanishes at an extremum". Eq. (13.4) is called the *Euler–Lagrange equation* of the functional (13.1), and each of its solutions is called an *extremal* of the functional. Note that it is only a necessary condition: an extremal need not make the functional attain an extremum, just as a stationary point need not be an extremum.

Expanding $\frac{\mathrm{d}}{\mathrm{d}x}F_{y'}$, Eq. (13.4) becomes

$$
F_{y'y'}\,y''+F_{yy'}\,y'+F_{xy'}-F_y=0.
$$
When $F_{y'y'}\ne0$ this is a second-order ordinary differential equation whose general solution contains two arbitrary constants, determined by the boundary conditions $y(a)=A$ and $y(b)=B$. Thus a variational problem becomes a two-point boundary value problem for a second-order equation ([2.4.12](/2.4.12#sec-12.4)).

Two remarks on regularity. First, the assumption $y_0\in C^2$ in the theorem serves only to justify the integration by parts. If we assume only $y_0\in C^1$, we can integrate the first term by parts instead and use the du Bois-Reymond lemma to obtain the integrated form $F_{y'}=\int_a^xF_y\,\mathrm{d}t+C$; one can then show that if $F_{y'y'}\ne0$ along $y_0$, then $y_0$ automatically belongs to $C^2$. Second, the necessary conditions for a minimum also include the Legendre condition $F_{y'y'}\big(x,y_0,y_0'\big)\ge0$; sufficient conditions require the second variation and the Jacobi condition, which we do not discuss here.

### 13.2.3. Cases Allowing Reduction of Order

The Euler–Lagrange equation is in general a nonlinear second-order equation and hard to solve. In the following cases its order can be reduced; they correspond to the types of equations admitting reduction of order in [2.4.7](/2.4.7).

1. $F$ does not contain $y'$: $F=F(x,y)$. Eq. (13.4) becomes $F_y(x,y)=0$, a functional equation rather than a differential equation, which in general cannot satisfy the boundary conditions; the variational problem usually has no solution.
2. $F$ does not contain $y$: $F=F(x,y')$. Eq. (13.4) becomes $\frac{\mathrm{d}}{\mathrm{d}x}F_{y'}=0$, which gives the first integral $F_{y'}(x,y')=C$, a first-order equation not containing $y$.
3. $F$ does not contain $x$: $F=F(y,y')$. Then the Beltrami identity below gives the first-order equation $F-y'F_{y'}=C$.
4. $F$ contains only $y'$: $F=F(y')$. Eq. (13.4) becomes $F_{y'y'}(y')\,y''=0$, so either $y''=0$ or $y'$ is a (constant) root of the equation $F_{y'y'}(p)=0$; in both cases the extremals are straight lines.

**Theorem 13.2.2 (Beltrami Identity)** If $F=F(y,y')$ does not contain $x$ explicitly, then for every $y\in C^2$ satisfying the Euler–Lagrange equation (13.4),

$$
F(y,y')-y'F_{y'}(y,y')=C\tag{13.5}
$$
is constant. Conversely, every $C^2$ function satisfying Eq. (13.5) with $y'\ne0$ is a solution of Eq. (13.4).

**Proof** Since $F$ does not contain $x$, $\frac{\mathrm{d}}{\mathrm{d}x}F_{y'}=F_{yy'}y'+F_{y'y'}y''$. A direct computation gives

$$
\frac{\mathrm{d}}{\mathrm{d}x}\big(F-y'F_{y'}\big)=F_yy'+F_{y'}y''-y''F_{y'}-y'\frac{\mathrm{d}}{\mathrm{d}x}F_{y'}=y'\Big(F_y-\frac{\mathrm{d}}{\mathrm{d}x}F_{y'}\Big),
$$
from which both directions follow. $\square$

In mechanics $x$ is time, and when $F$ does not contain time explicitly, Eq. (13.5) is conservation of energy (§13.4.1); it is a first integral of the Euler–Lagrange equation ([2.4.14](/2.4.14)).

Example 13.1.1 belongs to case 4: $F=\sqrt{1+y'^2}$ and $F_{y'y'}=(1+y'^2)^{-3/2}>0$, so $y''=0$: the extremal between two points is a straight line segment.

## 13.3. Classical Problems

### 13.3.1. The Minimal Surface of Revolution and the Catenary

**Example 13.3.1** Find the extremals in Example 13.1.2.

**Solution** $F=y\sqrt{1+y'^2}$ does not contain $x$, so by Eq. (13.5),

$$
y\sqrt{1+y'^2}-\frac{yy'^2}{\sqrt{1+y'^2}}=\frac{y}{\sqrt{1+y'^2}}=C\quad(C>0).
$$
Setting $y'=p$, we have $y=C\sqrt{1+p^2}$ and $\mathrm{d}x=\frac{\mathrm{d}y}{p}=\frac{C\,\mathrm{d}p}{\sqrt{1+p^2}}$, and integration gives $x=C\ln\big(p+\sqrt{1+p^2}\big)+C'$. Let $t=\ln\big(p+\sqrt{1+p^2}\big)$, that is, $p=\sinh t$; then $\sqrt{1+p^2}=\cosh t$, and the curve has the parametric equations $x=Ct+C'$, $y=C\cosh t$. Eliminating $t$:

$$
y=C\cosh\frac{x-C'}{C}.\tag{13.6}
$$
This is the *catenary*, with constants $C,C'$ determined by $A$ and $B$; the surface obtained by rotating it about the $x$-axis is called the *catenoid*.

The two constants are determined by nonlinear equations, and the number of solutions depends on the endpoints. Take symmetric endpoints $(\pm a,h)$: by symmetry $C'=0$, and the condition is $C\cosh\frac aC=h$. With $s=a/C$, this reads $\frac{\cosh s}{s}=\frac ha$. The minimum of $\frac{\cosh s}{s}$ on $s>0$ is about $1.5089$ (attained where $s\tanh s=1$, $s\approx1.1997$). Therefore:

- For $h/a>1.5089$ there are two catenaries; the "flatter" one (with larger $C$) gives a local minimum of the area, and the deeper one is not a minimum;
- For $h/a=1.5089$ there is exactly one;
- For $h/a<1.5089$ no catenary joins the two endpoints. In this case the infimum of the area is given by the two end disks together with the segment on the $x$-axis (the Goldschmidt solution), which is not a smooth curve and does not belong to the admissible class.

This shows that the boundary value problem for the Euler–Lagrange equation may have several solutions or none, and that the solution of a variational problem need not lie in the class of functions fixed in advance. Soap films make this visible: when two rings are pulled apart beyond a certain distance, the catenoidal soap film suddenly breaks into two disks.

![Catenaries joining (-1, h) and (1, h): two when h exceeds the critical value, one when h equals it, none when h is smaller](./plots/catenary-solutions.py)

### 13.3.2. The Brachistochrone and the Cycloid

**Example 13.3.2** Find the extremals in Example 13.1.3.

**Solution** $F=\frac{\sqrt{1+y'^2}}{\sqrt y}$ does not contain $x$ (the constant factor $1/\sqrt{2g}$ does not affect the extremals). By Eq. (13.5),

$$
\frac{\sqrt{1+y'^2}}{\sqrt y}-\frac{y'^2}{\sqrt{y(1+y'^2)}}=\frac{1}{\sqrt{y(1+y'^2)}}=C_1,
$$
that is, $y(1+y'^2)=C$ with $C=1/C_1^2>0$. Setting $y'=\cot t$,

$$
y=\frac{C}{1+\cot^2t}=C\sin^2t=\frac C2(1-\cos2t),\qquad\mathrm{d}x=\frac{\mathrm{d}y}{y'}=\frac{2C\sin t\cos t\,\mathrm{d}t}{\cot t}=C(1-\cos2t)\,\mathrm{d}t,
$$
and integration gives $x=\frac C2(2t-\sin2t)+C'$. Since $A$ is the origin, $C'=0$; with $\theta=2t$ and $R=C/2$:

$$
x=R(\theta-\sin\theta),\qquad y=R(1-\cos\theta).\tag{13.7}
$$
This is the path traced by a point on a circle of radius $R$ rolling along the $x$-axis (below it), called the *cycloid*. The radius $R$ is determined by $B$ (the equation $\frac{\theta-\sin\theta}{1-\cos\theta}=\frac{x_B}{y_B}$ has a unique solution $\theta\in(0,2\pi)$).

The time needed to slide along the cycloid (13.7) from $A$ to the point with parameter $\theta_B$ is $T=\theta_B\sqrt{R/g}$. The straight line, although shortest, is too gentle at the start, so the speed builds up slowly; the cycloid is steep at first and then flattens out, trading a little extra distance for a higher speed. The figure below compares the times along three tracks for $B=(\pi,2)$ ($R=1$, $\theta_B=\pi$). The cycloid is also tautochronous: released from rest at any point of the cycloid, a particle reaches the lowest point in time $\pi\sqrt{R/g}$, independent of the starting point.

![Three tracks from A = (0, 0) to B = (π, 2) (y-axis pointing down): the cycloid, the straight line and a circular arc; the legend gives the descent times for g = 1](./plots/brachistochrone.py)

### 13.3.3. Geodesics on the Sphere

**Example 13.3.3** Find the shortest curve joining two points on a sphere.

**Solution** On the sphere of radius $R$ use spherical coordinates $x=R\sin\theta\cos\varphi$, $y=R\sin\theta\sin\varphi$, $z=R\cos\theta$, $\theta\in[0,\pi]$, $\varphi\in[0,2\pi)$. Writing the curve as $\varphi=\varphi(\theta)$, we have

$$
\mathrm{d}x^2+\mathrm{d}y^2+\mathrm{d}z^2=R^2\big(1+\varphi'^2\sin^2\theta\big)\,\mathrm{d}\theta^2,\qquad J[\varphi]=R\int_{\theta_1}^{\theta_2}\sqrt{1+\varphi'^2\sin^2\theta}\,\mathrm{d}\theta.
$$
The integrand does not contain $\varphi$ (case 2), so

$$
F_{\varphi'}=\frac{R\,\varphi'\sin^2\theta}{\sqrt{1+\varphi'^2\sin^2\theta}}=RC.
$$
By the symmetry of the sphere, we may choose coordinates so that the starting point $A$ is the north pole $\theta=0$. Since $\Big|\dfrac{u\sin^2\theta}{\sqrt{1+u^2\sin^2\theta}}\Big|\le|\sin\theta|$ for every real $u$, letting $\theta\to0^+$ gives $C=0$, hence $\varphi'\equiv0$ and $\varphi=\varphi_0$ is constant: the curve is the meridian $x=R\sin\theta\cos\varphi_0$, $y=R\sin\theta\sin\varphi_0$, $z=R\cos\theta$, that is, the intersection of the sphere with the plane through $A$, $B$ and the center, an arc of a great circle. If $A$ is not taken to be a pole, $C$ is in general nonzero, and the result is still a great circle, only with a more complicated equation.

Such "locally shortest curves" are called *geodesics*. This is why long-haul flight routes follow great circles and appear curved on a Mercator map.

## 13.4. Generalizations

### 13.4.1. Several Unknown Functions and Hamilton's Principle

Suppose the functional depends on $n$ unknown functions $y_1,\dots,y_n$:

$$
J[y_1,\dots,y_n]=\int_a^bF\big(x,y_1,\dots,y_n,y_1',\dots,y_n'\big)\,\mathrm{d}x,
$$
with the values at both ends prescribed. Varying one function at a time, $y_i+\varepsilon\eta_i$, while keeping the others fixed, the proof of Theorem 13.2.1 gives the system of Euler–Lagrange equations

$$
F_{y_i}-\frac{\mathrm{d}}{\mathrm{d}x}F_{y_i'}=0,\qquad i=1,\dots,n.\tag{13.8}
$$
Variational problems for space curves (such as geodesics on a surface or the brachistochrone in space) are all of this kind.

The most important example in mechanics is Hamilton's principle. Let a mechanical system have generalized coordinates $q_1,\dots,q_n$, kinetic energy $T$ and potential energy $V$, and let $\mathcal{L}=T-V$ be the Lagrangian. The actual motion of the system makes the action $\int_{t_1}^{t_2}\mathcal{L}(t,q,\dot q)\,\mathrm{d}t$ stationary, and Eq. (13.8) gives Lagrange's equations

$$
\frac{\mathrm{d}}{\mathrm{d}t}\frac{\partial\mathcal{L}}{\partial\dot q_i}-\frac{\partial\mathcal{L}}{\partial q_i}=0,\qquad i=1,\dots,n.
$$
For example, for a pendulum of length $l$ with $q=\theta$, $\mathcal{L}=\frac12ml^2\dot\theta^2+mgl\cos\theta$, and Lagrange's equation is $ml^2\ddot\theta+mgl\sin\theta=0$, that is, $\ddot\theta+\frac gl\sin\theta=0$. When $\mathcal{L}$ does not contain $t$ explicitly, the generalization of the Beltrami identity, $\sum_i\dot q_i\frac{\partial\mathcal{L}}{\partial\dot q_i}-\mathcal{L}=$ const, is $T+V=$ const (for systems whose kinetic energy is a quadratic form in $\dot q$), that is, conservation of mechanical energy.

### 13.4.2. The Isoperimetric Problem

**Example 13.4.1 (Dido's Problem)** Among all curves of length $l$ with both ends on the $x$-axis, which one encloses the largest area together with the $x$-axis? We must maximize $J[y]=\int_a^by\,\mathrm{d}x$ subject to the constraint

$$
K[y]=\int_a^b\sqrt{1+y'^2}\,\mathrm{d}x=l.
$$
A variational problem constrained by another integral functional in this way is called an *isoperimetric problem*.

**Theorem 13.4.1** Suppose $F,G$ have continuous second-order partial derivatives, and $y_0\in C^2$ makes $J[y]=\int_a^bF(x,y,y')\,\mathrm{d}x$ attain an extremum subject to the constraint $K[y]=\int_a^bG(x,y,y')\,\mathrm{d}x=l$ and the boundary conditions $y(a)=A$, $y(b)=B$, and that $y_0$ is not an extremal of $K$. Then there is a constant $\lambda$ such that $y_0$ is an extremal of the functional

$$
\int_a^b\big(F+\lambda G\big)\,\mathrm{d}x,
$$
that is, $y_0$ satisfies $(F+\lambda G)_y-\frac{\mathrm{d}}{\mathrm{d}x}(F+\lambda G)_{y'}=0$.

Idea of the proof: take two test functions and form the two-parameter variation $y_0+\varepsilon_1\eta_1+\varepsilon_2\eta_2$. Then $(\varepsilon_1,\varepsilon_2)=(0,0)$ is a constrained extremum of $J$, as a function of two variables, subject to $K=l$, and the method of Lagrange multipliers for functions of two variables ([2.2.11](/2.2.11#sec-11.6)) yields the multiplier; the hypothesis that "$y_0$ is not an extremal of $K$" ensures that the gradient of the constraint is nonzero and that the multiplier does not depend on the choice of test functions. The general solution contains two constants of integration and the multiplier $\lambda$, which are determined by the two boundary conditions and the constraint.

**Solution** (of Example 13.4.1) $F+\lambda G=y+\lambda\sqrt{1+y'^2}$ does not contain $x$, so by Eq. (13.5),

$$
y+\lambda\sqrt{1+y'^2}-\frac{\lambda y'^2}{\sqrt{1+y'^2}}=y+\frac{\lambda}{\sqrt{1+y'^2}}=c_2,
$$
that is, $(y-c_2)^2(1+y'^2)=\lambda^2$. Setting $y'=\tan t$ gives $y-c_2=\lambda\cos t$ and $\mathrm{d}x=\frac{\mathrm{d}y}{y'}=-\lambda\cos t\,\mathrm{d}t$, so $x-c_1=-\lambda\sin t$, and hence

$$
(x-c_1)^2+(y-c_2)^2=\lambda^2:
$$
the extremals are circular arcs. This is a variational form of the isoperimetric theorem (among closed curves of given length, the circle encloses the largest area).

**Example 13.4.2 (The Catenary)** A flexible rope of length $l$ and uniform linear density, fixed at both ends, hangs at rest under gravity in the shape that minimizes the potential energy $\int_a^b\rho gy\sqrt{1+y'^2}\,\mathrm{d}x$ subject to the constraint $\int_a^b\sqrt{1+y'^2}\,\mathrm{d}x=l$. By Theorem 13.4.1, $F+\lambda G=(y+\lambda)\sqrt{1+y'^2}$ (with $\rho g$ absorbed into the scale of $\lambda$). Setting $Y=y+\lambda$, the problem is exactly that of Example 13.3.1, and we obtain

$$
y+\lambda=c\cosh\frac{x-c'}{c}.
$$
A hanging rope and the generating curve of the minimal surface of revolution are the same kind of curve, which is where the name "catenary" (from the Latin for chain) comes from.

## Summary

| Problem | Integrand $F$ | Reduction | Extremals |
|---|---|---|---|
| Shortest curve | $\sqrt{1+y'^2}$ | Contains only $y'$ | Straight lines |
| Minimal surface of revolution | $y\sqrt{1+y'^2}$ | No $x$: $\frac{y}{\sqrt{1+y'^2}}=C$ | Catenary $y=C\cosh\frac{x-C'}{C}$ |
| Brachistochrone | $\frac{\sqrt{1+y'^2}}{\sqrt y}$ | No $x$: $y(1+y'^2)=C$ | Cycloid $x=R(\theta-\sin\theta)$, $y=R(1-\cos\theta)$ |
| Geodesics on the sphere | $\sqrt{1+\varphi'^2\sin^2\theta}$ | No $\varphi$: $F_{\varphi'}=C$ | Great circles |
| Isoperimetric problem | $y+\lambda\sqrt{1+y'^2}$ | Multiplier + no $x$ | Circular arcs |
| Hanging rope | $(y+\lambda)\sqrt{1+y'^2}$ | Multiplier + no $x$ | Catenary |

The basic route of the calculus of variations is: extremum ⟹ vanishing first variation ⟹ (fundamental lemma of the calculus of variations) Euler–Lagrange equation ⟹ boundary value problem for a second-order equation. When the integrand does not contain $x$, the Beltrami identity reduces it to a first-order equation; when there is an integral constraint, a Lagrange multiplier first absorbs the constraint into the integrand.
