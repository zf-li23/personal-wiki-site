---
title: Basic Concepts
source_hash: 7dbbe2c22f1b
---

This chapter fixes the basic language of ordinary differential equations: the order and classification of equations, solutions and implicit solutions, general solutions and the independence of the arbitrary constants they contain, initial value problems, and the geometric interpretation of first-order equations through direction fields and integral curves. These notions already appeared in calculus ([2.2.15](/2.2.15)); here we restate them rigorously as definitions and add two points not discussed there: the precise meaning of "mutually independent arbitrary constants" in a general solution (the Jacobian criterion), and how direction fields and isoclines reveal the shape of solutions without solving the equation. The last section describes the three kinds of questions this course sets out to answer; they determine the arrangement of the chapters that follow.

## 1.1. Differential Equations and Their Solutions

### 1.1.1. Classification

**Definition 1.1.1** A relation connecting an independent variable, an unknown function and its derivatives is called a **differential equation**. If the unknown function is a function of one variable, the equation is an **ordinary differential equation**; if it is a function of several variables, so that partial derivatives occur, the equation is a **partial differential equation**. The highest order of the derivatives of the unknown function occurring in the equation is the order of the equation.

The general (implicit) form of an $n$th-order ordinary differential equation is

$$
F\big(x,y,y',\dots,y^{(n)}\big)=0,\tag{1.1}
$$
where $F$ is a given function on some region and genuinely depends on $y^{(n)}$. An equation solved for the highest derivative,

$$
y^{(n)}=f\big(x,y,y',\dots,y^{(n-1)}\big),\tag{1.2}
$$
is said to be in normal form. By the **implicit function theorem**, near points where $\partial F/\partial y^{(n)}\ne0$, Eq. (1.1) can locally be brought into the form (1.2); points where $\partial F/\partial y^{(n)}=0$ give rise to special solutions, and this phenomenon for implicit first-order equations (singular solutions) is studied in [2.4.6](/2.4.6). Unless stated otherwise, "equation" means an ordinary differential equation.

**Definition 1.1.2** If $F$ in Eq. (1.1) is of the first degree in $y,y',\dots,y^{(n)}$, that is, if the equation has the form

$$
a_0(x)y^{(n)}+a_1(x)y^{(n-1)}+\cdots+a_{n-1}(x)y'+a_n(x)y=f(x),
$$
it is called an $n$th-order **linear differential equation**; otherwise it is called a nonlinear differential equation. If $f\equiv0$ it is called a homogeneous linear equation, otherwise a nonhomogeneous linear equation.

"Linear" refers only to the unknown function and its derivatives; the coefficients may be arbitrary functions of $x$. The word "homogeneous" has two unrelated uses in differential equations: here it means that a linear equation has no forcing term, whereas the first-order equation $y'=f(y/x)$ is called a homogeneous equation because its right-hand side is a **homogeneous function** of degree zero ([2.2.15](/2.2.15#sec-15.2.2); in this course, [2.4.3](/2.4.3)).

Besides single equations we also consider systems of equations in $n$ unknown functions $y_1,\dots,y_n$. A first-order system in normal form is written in vector form as

$$
\boldsymbol{y}'=\boldsymbol{f}(x,\boldsymbol{y}),\qquad\boldsymbol{y}=(y_1,\dots,y_n)^{\mathsf T}.
$$
Setting $y_1=y$, $y_2=y'$, …, $y_n=y^{(n-1)}$ turns the normal-form equation (1.2) into such a system, so first-order systems are the most general object of study ([2.4.7](/2.4.7)); linear systems are the subject of [2.4.8](/2.4.8).

### 1.1.2. Solutions and Implicit Solutions

**Definition 1.1.3** Suppose the function $y=\varphi(x)$ has derivatives up to order $n$ on an interval $J$, the point $\big(x,\varphi(x),\dots,\varphi^{(n)}(x)\big)$ lies in the domain of $F$ for every $x\in J$, and

$$
F\big(x,\varphi(x),\varphi'(x),\dots,\varphi^{(n)}(x)\big)=0,\qquad x\in J.
$$
Then $y=\varphi(x)$ is called a solution of Eq. (1.1) on the interval $J$. If the implicit function $y=\varphi(x)$ determined by a relation $\Phi(x,y)=0$ is a solution of Eq. (1.1), then $\Phi(x,y)=0$ is called an implicit solution of the equation.

A solution always comes together with its interval of definition: the same formula may give different solutions on different intervals. For example, $y=\dfrac{1}{C-x}$ solves $y'=y^2$, but its interval of definition can only be one of $(-\infty,C)$ and $(C,+\infty)$; the two pieces are separated by the vertical asymptote at $x=C$ and are two different solutions. The interval $J$ may be open, closed or infinite; at an endpoint belonging to $J$, derivatives are one-sided.

Geometrically, solutions of first-order equations often do not appear as graphs of functions $y$ of $x$. For example, the implicit solution $x^2+y^2=R^2$ of $x\,\mathrm{d}x+y\,\mathrm{d}y=0$ determines an upper and a lower semicircle, each of which is a solution of $y'=-x/y$ on $(-R,R)$. When the equation is written in the symmetric form

$$
P(x,y)\,\mathrm{d}x+Q(x,y)\,\mathrm{d}y=0,\tag{1.3}
$$
the variables $x$ and $y$ play equal roles: a solution may be $y=\varphi(x)$ or $x=\psi(y)$, and the whole circle is regarded as an integral curve.

### 1.1.3. General Solutions and Independence of Arbitrary Constants

Integrating $y^{(n)}=f(x)$ $n$ times produces $n$ arbitrary constants. For a general $n$th-order equation one can also often find a family of solutions with $n$ arbitrary constants, but the constants must be counted by how many actually take effect: $y=C_1\mathrm{e}^{x+C_2}=(C_1\mathrm{e}^{C_2})\mathrm{e}^x$ seems to contain two constants but really contains only one. The following definition gives the precise criterion.

**Definition 1.1.4** Suppose that for every $(C_1,\dots,C_n)$ in a parameter region $\Omega\subset\mathbb{R}^n$, $y=\varphi(x,C_1,\dots,C_n)$ is a solution of the $n$th-order equation (1.1), that $\varphi$ has continuous derivatives with respect to $x$ up to order $n-1$, and that these are continuously differentiable with respect to $C_1,\dots,C_n$. If

$$
\frac{\partial\big(\varphi,\varphi',\dots,\varphi^{(n-1)}\big)}{\partial(C_1,\dots,C_n)}=\begin{vmatrix}
\dfrac{\partial\varphi}{\partial C_1}&\cdots&\dfrac{\partial\varphi}{\partial C_n}\\
\vdots&&\vdots\\
\dfrac{\partial\varphi^{(n-1)}}{\partial C_1}&\cdots&\dfrac{\partial\varphi^{(n-1)}}{\partial C_n}
\end{vmatrix}\ne0,\tag{1.4}
$$
where $\varphi^{(k)}$ denotes the derivative with respect to $x$, then $C_1,\dots,C_n$ are said to be mutually independent, and $y=\varphi(x,C_1,\dots,C_n)$ is called a **general solution** of the equation. If a general solution is given implicitly as $\Phi(x,y,C_1,\dots,C_n)=0$, it is called a **general integral** of the equation. A solution obtained by assigning definite values to the constants in a general solution is called a **particular solution**.

Condition (1.4) says that a **Jacobian determinant** is nonzero. Its meaning is explained by the following theorem: independent constants are exactly enough to satisfy $n$ initial conditions.

**Theorem 1.1.1** Let $y=\varphi(x,\boldsymbol{C})$ satisfy the hypotheses of Definition 1.1.4, and suppose (1.4) holds at $(x_0,\boldsymbol{C}^0)$. Write $\eta_k^0=\varphi^{(k)}(x_0,\boldsymbol{C}^0)$ ($k=0,\dots,n-1$). Then there is a neighborhood $U$ of $\boldsymbol{\eta}^0=(\eta_0^0,\dots,\eta_{n-1}^0)$ such that for every $(\eta_0,\dots,\eta_{n-1})\in U$ there is a unique set of constants $\boldsymbol{C}$ near $\boldsymbol{C}^0$ for which the solution $\varphi(x,\boldsymbol{C})$ satisfies the initial conditions

$$
y(x_0)=\eta_0,\quad y'(x_0)=\eta_1,\quad\dots,\quad y^{(n-1)}(x_0)=\eta_{n-1}.
$$

**Proof** Consider the map $\boldsymbol{C}\mapsto\big(\varphi(x_0,\boldsymbol{C}),\varphi'(x_0,\boldsymbol{C}),\dots,\varphi^{(n-1)}(x_0,\boldsymbol{C})\big)$. It is continuously differentiable, and its Jacobian determinant at $\boldsymbol{C}^0$ is the value of (1.4) at $x=x_0$, which is nonzero. By the **inverse function theorem** (the $n$-dimensional case of [2.2.10](/2.2.10#thm-10.8.4)), it maps some neighborhood of $\boldsymbol{C}^0$ bijectively onto some neighborhood $U$ of $\boldsymbol{\eta}^0$, so for every set of initial values in $U$ we can solve uniquely for $\boldsymbol{C}$. $\square$

Conversely, if (1.4) vanishes identically, the constants cannot adjust the $n$ initial values freely: they are functionally related, and fewer than $n$ constants actually take effect. Thus "a general solution contains $n$ independent constants" means that locally it can satisfy any prescribed (nearby) initial conditions.

**Example 1.1.1** For $y''+y=0$ and $\varphi=C_1\cos x+C_2\sin x$,

$$
\frac{\partial(\varphi,\varphi')}{\partial(C_1,C_2)}=\begin{vmatrix}\cos x&\sin x\\-\sin x&\cos x\end{vmatrix}=1\ne0,
$$
so this is a general solution. For $y''=y$, $\varphi=C_1\mathrm{e}^{x+C_2}$ is a family of solutions, but $\varphi'=\varphi$ and

$$
\frac{\partial(\varphi,\varphi')}{\partial(C_1,C_2)}=\begin{vmatrix}\mathrm{e}^{x+C_2}&C_1\mathrm{e}^{x+C_2}\\\mathrm{e}^{x+C_2}&C_1\mathrm{e}^{x+C_2}\end{vmatrix}\equiv0,
$$
so it is not a general solution (every solution in this family satisfies $y'(x_0)=y(x_0)$ and cannot meet general initial conditions); the general solution of $y''=y$ is $C_1\mathrm{e}^x+C_2\mathrm{e}^{-x}$.

A general solution need not contain all solutions of the equation. The general solution $y=\dfrac{1}{C-x}$ of $y'=y^2$ does not contain the solution $y\equiv0$ ([2.2.15 Example 15.2.1](/2.2.15#ex-15.2.1)); more drastically, the singular solutions of [2.4.6](/2.4.6) are tangent at every point to some solution in the general solution, yet do not belong to it. For linear equations the general solution contains all solutions ([2.4.3](/2.4.3), [2.4.8](/2.4.8)).

### 1.1.4. Initial Value Problems

**Definition 1.1.5** The problem of finding a solution of the normal-form equation (1.2) satisfying the initial conditions

$$
y(x_0)=y_0,\quad y'(x_0)=y_0^{(1)},\quad\dots,\quad y^{(n-1)}(x_0)=y_0^{(n-1)}
$$
is called an **initial value problem** (Cauchy problem). Here $\big(x_0,y_0,y_0^{(1)},\dots,y_0^{(n-1)}\big)$ lies in the domain of $f$, and the $y_0^{(k)}$ are given numbers. The initial value problem for a first-order equation is

$$
y'=f(x,y),\qquad y(x_0)=y_0.\tag{1.5}
$$

A solution of an initial value problem is required to satisfy the equation on some interval containing $x_0$. Whether a solution exists, whether it is unique and how far it can be extended are the subjects of [2.4.4](/2.4.4) and [2.4.5](/2.4.5); [2.2.15](/2.2.15#sec-15.1.3) already stated the **existence and uniqueness theorem** under a **Lipschitz condition**, and its proof is given in [2.4.4](/2.4.4). Physically, an initial value problem corresponds to "knowing the present state, predict the future": Newton's equation of motion, which is of second order, needs two conditions, the initial position and the initial velocity.

The auxiliary conditions may also be imposed at the two ends of an interval, for example $y''=f(x,y,y')$, $y(a)=A$, $y(b)=B$; this is called a boundary value problem. Its behavior is very different from that of an initial value problem: it may have no solution or infinitely many, see [2.4.12](/2.4.12).

## 1.2. Geometric Interpretation: Direction Fields and Integral Curves

### 1.2.1. Direction Fields

Let $f(x,y)$ be continuous on a plane region $G$. The equation

$$
y'=f(x,y)\tag{1.6}
$$
assigns a slope $f(P)$ to every point $P(x,y)\in G$. The short segment $l(P)$ through $P$ with slope $f(P)$ is called the line element of the equation at $P$; the region $G$ together with all its line elements is the **direction field** of the equation (also called the field of line elements). If $y=\varphi(x)$ is a solution, its graph is a smooth curve, an **integral curve**, and at every point $\big(x_0,\varphi(x_0)\big)$ of the curve

$$
\varphi'(x_0)=f\big(x_0,\varphi(x_0)\big),
$$
that is, the tangent line $y=y_0+f(x_0,y_0)(x-x_0)$ of the integral curve at that point is exactly the line carrying the line element there.

**Proposition 1.2.1** Let $f$ be continuous on $G$. A differentiable function $y=\varphi(x)$ on an interval $J$ (with graph in $G$) is a solution of Eq. (1.6) if and only if its graph is tangent to the direction field at every point.

**Proof** Both statements are equivalent to $\varphi'(x)=f\big(x,\varphi(x)\big)$ for all $x\in J$. Since $f$ is continuous, $\varphi'$ is continuous as well, so integral curves are smooth curves. $\square$

Solving Eq. (1.6) therefore means finding curves that are everywhere tangent to a given direction field. This point of view does not depend on solution formulas: even when an equation cannot be solved by elementary integration (for example $y'=x^2+y^2$ below), the direction field shows the rough course of the integral curves. At points where $Q=0$ and $P\ne0$, the symmetric form (1.3) prescribes the vertical direction; the integral curve then has a vertical tangent there, and $x$ should be regarded as a function of $y$. Points where $P=Q=0$ prescribe no direction at all.

### 1.2.2. Isoclines

Drawing line elements point by point is tedious. A curve consisting of the points of the direction field with the same slope,

$$
L_k:\ f(x,y)=k,
$$
is called an *isocline* of Eq. (1.6). All line elements on $L_k$ are parallel, with slope $k$. Drawing several isoclines and short segments of the common direction on each gives a sketch of the direction field, along whose line elements we can then trace the integral curves.

**Example 1.2.1** (1) $y'=\dfrac yx$: the isoclines are the lines $y=kx$ through the origin, and the line elements on such a line also have slope $k$. The line elements coincide with the isocline, so the isoclines themselves are integral curves: the integral curves are the rays emanating from the origin (halves with $x>0$ and $x<0$).

(2) $y'=-\dfrac xy$: the isoclines $y=-\dfrac xk$ are again lines through the origin, but the product of the slope $k$ of the line elements and the slope $-1/k$ of the isocline is $-1$. The line elements are perpendicular to the isoclines, so the integral curves are circles centered at the origin.

Neither direction field is defined at the origin: all the rays converge to the origin, and all the circles surround it. In the symmetric forms $x\,\mathrm{d}y-y\,\mathrm{d}x=0$ and $x\,\mathrm{d}x+y\,\mathrm{d}y=0$, the origin is a point where $P=Q=0$. The behavior of integral curves near such points (nodes, centers and so on) is the object of the qualitative theory, see [2.4.11](/2.4.11).

![Left: the direction field of y' = y/x; the line elements point along the isoclines y = kx, and the integral curves are rays from the origin. Right: the direction field of y' = -x/y; the line elements are perpendicular to the isoclines, and the integral curves are concentric circles](./plots/isoclines-lines-circles.py)

**Example 1.2.2** The equation $y'=x^2+y^2$ cannot be solved by elementary integration (it is a Riccati equation, see [2.4.3](/2.4.3)), but its isoclines $x^2+y^2=k$ ($k>0$) are circles centered at the origin with radius $\sqrt k$. From them we can read off properties of the integral curves:

- the slope is nonnegative everywhere and vanishes only at the origin, so every integral curve is strictly increasing;
- the slope grows with the distance from the origin. In the region $x\ge1$ we have $y'\ge1+y^2$, and the solutions $\tan(x-c)$ of $y'=1+y^2$ tend to $+\infty$ within a finite interval. From this one can prove (by the comparison theorems of [2.4.5](/2.4.5)) that every integral curve tends to $+\infty$ at some finite $x$ to the right and to $-\infty$ at some finite $x$ to the left, so every solution exists only on a bounded interval;
- since $y''=2x+2yy'=2x+2y(x^2+y^2)$, the convexity of the integral curves is separated by the curve $x+y(x^2+y^2)=0$: integral curves are convex ($y''>0$) on the side where $x+y(x^2+y^2)>0$ and concave on the other side.

![The direction field of y' = x^2 + y^2 with isoclines (dashed circles x^2 + y^2 = k, k = 1, 4) and several numerically computed integral curves; each integral curve is increasing and tends to infinity at both ends of a bounded interval](./plots/riccati-isoclines.py)

The direction field point of view is equally fundamental in numerical computation: Euler's method starts from the initial point, takes a small step along the line element, then takes the next step along the line element at the new point, and so on. In [2.4.4](/2.4.4) we use Euler polygons to prove the Peano existence theorem.

## 1.3. The Basic Questions of This Course

For a given differential equation we can ask three kinds of questions, which form the main thread of this course.

| Question | Content | Chapters |
|---|---|---|
| Solving | Expressing solutions through elementary functions and finitely many integrations (quadratures); higher-order equations whose order can be reduced; the structure of solutions of linear equations and explicit solutions of constant-coefficient equations; power series solutions | [2.4.2](/2.4.2), [2.4.3](/2.4.3), [2.4.7](/2.4.7)–[2.4.10](/2.4.10) |
| Existence and uniqueness | When an initial value problem has a solution and when it is unique; how far solutions extend; how solutions vary with initial values and parameters; singular solutions | [2.4.4](/2.4.4)–[2.4.7](/2.4.7) |
| Qualitative theory | Determining properties of solutions directly from the equation without solving it: stability, the behavior of trajectories near equilibrium points, periodic solutions and limit cycles, the distribution of zeros | [2.4.11](/2.4.11), [2.4.12](/2.4.12) |

The first kind of question is historically the oldest, but in 1841 Liouville proved that even the simple-looking Riccati equation $y'=x^2+y^2$ cannot be solved by quadratures ([2.4.3](/2.4.3)); equations solvable by elementary integration are rare exceptions. The second kind of question is therefore the foundation of the theory: it guarantees that the object of study, the solution, actually exists and is uniquely determined by its initial values, which is precisely what makes differential equations usable for predicting physical processes. The third kind was initiated by Poincaré and Lyapunov at the end of the nineteenth century. It answers the questions that matter most in applications (where the system goes after a long time, whether an equilibrium state is stable) without writing down formulas for the solutions. The calculus of variations ([2.4.13](/2.4.13)) and first integrals ([2.4.14](/2.4.14)) connect ordinary differential equations with extremum problems and with partial differential equations.

## Summary

| Concept | Key points |
|---|---|
| Order, linearity | Order of the highest derivative; linear if of the first degree in $y,y',\dots,y^{(n)}$ |
| Solution | Always together with its interval of definition; implicit solution $\Phi(x,y)=0$ |
| General solution | $n$ independent constants: $\partial(\varphi,\dots,\varphi^{(n-1)})/\partial(C_1,\dots,C_n)\ne0$, which guarantees that any nearby initial values can be met; need not contain all solutions |
| Initial value problem | $y^{(k)}(x_0)$ ($k<n$) prescribed; an $n$th-order equation needs $n$ conditions |
| Direction field | Solution ⇔ curve tangent to the line elements everywhere; isoclines $f(x,y)=k$ for sketching |
