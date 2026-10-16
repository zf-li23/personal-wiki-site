---
title: First-Order Differential Equations
source_hash: 06d1992f1ef6
---

Many problems in geometry and physics do not give the unknown function itself but a relation between the function and its derivatives: the slope of the tangent line at each point of a curve, the velocity and acceleration of a body, the growth rate of a population. Such a relation is a differential equation, and finding the functions that satisfy it is "solving the differential equation". Single-variable integration ([2.2.6](/2.2.6), [2.2.7](/2.2.7)) finds antiderivatives, which amounts to solving the simplest equation $y'=f(x)$; this chapter extends that task to the case where the unknown function also appears on the right-hand side.

We first set up the basic concepts (solutions, general solutions, initial value problems, integral curves) and state the existence and uniqueness theorem. We then present several classes of first-order equations whose solutions can be found in closed form by elementary integration: separable equations and equations reducible to them, first-order linear equations and Bernoulli equations, exact equations and integrating factors; finally we treat several classes of higher-order equations whose order can be reduced to one. The common idea behind all these methods is a change of variables that transforms the equation into a type we already know how to solve. Exact equations use the antiderivatives of differential forms from [2.2.10](/2.2.10) and the conservative fields of [2.2.14](/2.2.14). The [next chapter](/2.2.16) treats higher-order linear equations and linear systems, where the language of linear algebra takes the leading role. The general theory of ordinary differential equations (continuation of solutions, dependence on initial values, stability and so on) is left to [2.4](/2.4); ordinary differential equations in biological modeling appear in [7.4.4](/7.4.4).

## 15.1. Basic Concepts of Differential Equations

### 15.1.1. Motivating Examples

**Example 15.1.1** Find the curve through the point $(0,1)$ whose tangent slope at each point equals the abscissa of that point. Let the curve be $y=y(x)$. Then $y'=x$, and integration gives $y=\dfrac{x^2}{2}+C$; from $y(0)=1$ we get $C=1$, so the curve is $y=\dfrac{x^2}{2}+1$.

**Example 15.1.2 (Free Fall)** Let $s(t)$ be the distance a body has fallen. Then $s''(t)=g$. Integrating twice gives $s=\dfrac12gt^2+C_1t+C_2$. If the velocity is $v_0$ and the distance is $s_0$ at $t=0$, then $C_1=v_0$, $C_2=s_0$, and $s=\dfrac12gt^2+v_0t+s_0$.

**Example 15.1.3 (Catenary)** A uniform flexible cable fixed at both ends hangs freely under gravity; find its shape. Take the lowest point of the cable as the origin, let $\rho$ be the linear density of the cable and let the curve be $y=y(x)$. Consider the piece from the lowest point to the point $(x,y)$. It is acted on by the horizontal tension $H$ at the lowest point, the tension $T$ along the tangent at the endpoint, and its weight $\rho g l$, where $l$ is the arc length of the piece. If $\theta$ is the angle of inclination of the tangent, equilibrium requires $T\cos\theta=H$ and $T\sin\theta=\rho gl$, so

$$
y'=\tan\theta=\frac{\rho g}{H}\int_0^x\sqrt{1+y'(s)^2}\,\mathrm{d}s.
$$

Differentiating both sides and writing $a=\rho g/H$, we obtain $y''=a\sqrt{1+y'^2}$ with $y(0)=0$, $y'(0)=0$. This equation involves the second derivative; Example 15.5.4 will solve it and obtain $y=\dfrac{\cosh ax-1}{a}$.

The first two examples require only integration. In the third, the derivatives of the unknown function are tied to one another, and new methods are needed.

### 15.1.2. Basic Concepts

**Definition 15.1.1** An equation involving an unknown function and its derivatives is called a **differential equation**. A differential equation whose unknown function is a function of one variable is called an **ordinary differential equation**; one whose unknown function is a function of several variables, so that partial derivatives appear, is called a **partial differential equation**. The highest order of derivative of the unknown function appearing in the equation is the order of the equation.

The general form of an $n$th-order ordinary differential equation is $F(x,y,y',\dots,y^{(n)})=0$. For example, $(y')^2+ay+b=0$ is a first-order equation and $y''+ay+b=0$ is a second-order equation; the catenary equation is of second order. From now on, "differential equation" means an ordinary differential equation.

**Definition 15.1.2** If the equation is of the first degree in the unknown function and all its derivatives, that is, if it has the form

$$
a_0(x)y^{(n)}+a_1(x)y^{(n-1)}+\cdots+a_{n-1}(x)y'+a_n(x)y=f(x),
$$
it is called an $n$th-order **linear differential equation**; otherwise it is called a nonlinear differential equation.

The coefficients of a linear equation may be arbitrary functions of $x$; "linear" refers only to the unknown function. The catenary equation $y''=a\sqrt{1+y'^2}$ is nonlinear.

**Definition 15.1.3** Suppose the function $\varphi(x)$ has derivatives up to order $n$ on an interval $I$ and $F(x,\varphi(x),\varphi'(x),\dots,\varphi^{(n)}(x))=0$ for all $x\in I$. Then $y=\varphi(x)$ is called a solution of the equation on $I$. A solution of an $n$th-order equation containing $n$ independent arbitrary constants is called a **general solution**; a solution containing no arbitrary constants is called a **particular solution**. Conditions that determine the constants in the general solution are called auxiliary conditions.

"Independent" means that the constants cannot be merged into fewer constants; for example, $C_1\mathrm{e}^{x+C_2}=C\mathrm{e}^x$ really contains only one constant. A general solution is a family of solutions, but it need not include all solutions of the equation; see Example 15.2.1.

**Definition 15.1.4** The equation together with the conditions $y(x_0)=y_0$, $y'(x_0)=y_1$, …, $y^{(n-1)}(x_0)=y_{n-1}$ is called an **initial value problem** (also a Cauchy problem), and these conditions are called initial conditions. The initial value problem for a first-order equation is written

$$
\begin{cases}y'=f(x,y),\\ y(x_0)=y_0.\end{cases}
$$
The auxiliary conditions may also be imposed at the two endpoints of an interval, for example $F(x,y,y',y'')=0$, $y(a)=A$, $y(b)=B$; this is called a boundary value problem.

**Definition 15.1.5** The graph of a solution $y=\varphi(x)$ of a differential equation is called an **integral curve** of the equation; the graph of the general solution is a family of curves, called the family of integral curves.

For example, the integral curves of $y'=2x$ form the family of parabolas $y=x^2+C$; the integral curves of $y'=-\dfrac{x}{y}$, that is, of $x\,\mathrm{d}x+y\,\mathrm{d}y=0$, are the concentric circles $x^2+y^2=R^2$.

The equation $y'=f(x,y)$ has an intuitive geometric meaning: at each point $(x,y)$ of the region it prescribes a slope $f(x,y)$. Drawing at each point a short segment with slope $f(x,y)$ gives the *direction field* of the equation; the integral curves are exactly the curves that are tangent to the direction field everywhere. Even when we cannot solve the equation, the direction field shows the overall behavior of its solutions.

![The direction field (short segments) of the equation y' = x - y and several integral curves y = x - 1 + C e^{-x}; as x increases, every integral curve approaches the line y = x - 1 (the solution with C = 0)](./plots/direction-field.py)

### 15.1.3. Existence and Uniqueness of Solutions

Before solving an equation, we should ask: does a solution exist? Is the solution through a given point unique?

**Definition 15.1.6 (Lipschitz Condition)** Let $f(x,y)$ be defined on a region $D$. If there is a constant $L>0$ such that for any two points $(x,y_1)$, $(x,y_2)$ in $D$

$$
\lvert f(x,y_1)-f(x,y_2)\rvert\le L\lvert y_1-y_2\rvert,
$$
then $f$ is said to satisfy a **Lipschitz condition** with respect to $y$ on $D$, and $L$ is called a Lipschitz constant.

If $f_y$ is continuous and bounded on a convex region $D$ (for example, a rectangle), then by the mean value theorem $f(x,y_1)-f(x,y_2)=f_y(x,\xi)(y_1-y_2)$, so $f$ satisfies a Lipschitz condition with respect to $y$. The condition therefore always holds for the usual smooth functions; exceptions occur where $f_y$ is unbounded.

**Theorem 15.1.1 (Existence and Uniqueness Theorem)** Suppose $f(x,y)$ is continuous on the rectangle $D=\{(x,y)\mid\lvert x-x_0\rvert\le a,\ \lvert y-y_0\rvert\le b\}$ and satisfies a Lipschitz condition with respect to $y$. Let $M=\max_D\lvert f(x,y)\rvert$ and $h=\min\{a,b/M\}$. Then the initial value problem $y'=f(x,y)$, $y(x_0)=y_0$ has exactly one solution on the interval $[x_0-h,x_0+h]$.

This course does not prove the theorem; the proof (by Picard iteration) is given in [2.4](/2.4). The choice of $h$ guarantees that the integral curve does not leave the rectangle for $\lvert x-x_0\rvert\le h$: the slope is at most $M$ in absolute value, so over a horizontal distance $h$ the curve rises or falls by at most $Mh\le b$. Geometrically, the theorem says that in a region where the hypotheses hold, exactly one integral curve passes through each point, and distinct integral curves do not intersect.

**Example 15.1.4** Let $p(x)$ be continuous on an interval $I$. If an integral curve of the equation $y'=p(x)y$ meets the $x$-axis, then it coincides with the $x$-axis.

**Proof** The function $f(x,y)=p(x)y$ satisfies $\lvert f(x,y_1)-f(x,y_2)\rvert=\lvert p(x)\rvert\lvert y_1-y_2\rvert$, and $\lvert p\rvert$ is bounded on every bounded closed subinterval of $I$, so the Lipschitz condition holds. Suppose the integral curve $y=\varphi(x)$ meets the $x$-axis at $x_0$, that is, $\varphi(x_0)=0$. Since $y\equiv0$ is also a solution satisfying $y(x_0)=0$, uniqueness gives $\varphi\equiv0$. $\square$

Hence a nonzero solution of $y'=p(x)y$ never vanishes and keeps a constant sign. When the Lipschitz condition fails, uniqueness may be lost.

**Example 15.1.5** The initial value problem $y'=3y^{2/3}$, $y(0)=0$ has infinitely many solutions. The function $y\equiv0$ is a solution; for $y\ne0$, separating variables gives $\dfrac{\mathrm{d}y}{3y^{2/3}}=\mathrm{d}x$, hence $y^{1/3}=x-c$, that is, $y=(x-c)^3$. For any $c\ge0$, the function

$$
y=\begin{cases}0,&x<c,\\(x-c)^3,&x\ge c\end{cases}
$$
is differentiable on $\mathbb{R}$, satisfies the equation and has $y(0)=0$. The reason is that $f(y)=3y^{2/3}$ has $\dfrac{\lvert f(y)-f(0)\rvert}{\lvert y\rvert}=3\lvert y\rvert^{-1/3}$ unbounded near $y=0$, so the Lipschitz condition fails: an integral curve can run along the $x$-axis for any length and then "leave" it at any moment.

![Several solutions of the initial value problem y' = 3y^{2/3}, y(0) = 0: each runs along the x-axis up to x = c and then branches off as the cubic (x - c)^3; c ranges over all nonnegative reals, so there are infinitely many solutions](./plots/nonuniqueness.py)

For a first-order linear equation $y'+p(x)y=q(x)$, as long as $p$ and $q$ are continuous on an interval $I$, the solution of the initial value problem exists and is unique on the whole of $I$ (the formula in Theorem 15.3.1 gives it explicitly).

## 15.2. Separable Equations and Equations Reducible to Them

### 15.2.1. Separable Equations

**Definition 15.2.1** An equation of the form $y'=f(x)g(y)$, or in the symmetric form $M_1(x)N_1(y)\,\mathrm{d}x+M_2(x)N_2(y)\,\mathrm{d}y=0$, is called a **separable equation**.

**Algorithm 15.2.1 (Separation of Variables)** To solve $y'=f(x)g(y)$:

1. Where $g(y)\ne0$, write the equation as $\dfrac{\mathrm{d}y}{g(y)}=f(x)\,\mathrm{d}x$ and integrate both sides: $\displaystyle\int\frac{\mathrm{d}y}{g(y)}=\int f(x)\,\mathrm{d}x+C$, where each indefinite integral stands for one antiderivative;
2. If $g(c)=0$, then the constant function $y=c$ is also a solution. Check whether it is already contained in the general solution from step 1; if not, list it separately.

Step 1 often yields an implicit solution $G(y)=F(x)+C$; when we can solve for $y$, we convert it to explicit form.

**Example 15.2.1** Solve $y'=y^2$. For $y\ne0$ we get $-\dfrac1y=x+C$, that is, $y=-\dfrac{1}{x+C}$; $y=0$ is also a solution, but it is not obtained from any value of $C$. So the general solution of this equation does not include all solutions, and $y=0$ must be written out separately. By contrast, separating variables in $y'=-2xy$ gives $\ln\lvert y\rvert=-x^2+C_1$, that is, $y=\pm\mathrm{e}^{C_1}\mathrm{e}^{-x^2}$; including $y=0$ as well, the general solution is $y=C\mathrm{e}^{-x^2}$ with $C$ an arbitrary real number, and here the general solution includes all solutions (in agreement with Example 15.1.4).

**Example 15.2.2** Solve $(x+1)^2y\,\mathrm{d}x+x^2(y-1)\,\mathrm{d}y=0$. Dividing both sides by $x^2y$:

$$
\Big(1+\frac2x+\frac1{x^2}\Big)\mathrm{d}x=-\Big(1-\frac1y\Big)\mathrm{d}y,
$$
and integrating gives $x+2\ln\lvert x\rvert-\dfrac1x+y-\ln\lvert y\rvert=C$. There are also the solutions $y=0$ and $x=0$ (regarding $x$ as a function of $y$).

**Example 15.2.3** Every segment of a tangent line to a curve $C$ lying between the two coordinate axes is bisected by the point of tangency; find $C$. Let the point of tangency be $(x,y)$. The tangent line meets the $x$-axis at $(2x,0)$, so its slope is $y'=\dfrac{0-y}{2x-x}=-\dfrac yx$. Separating variables gives $\ln\lvert y\rvert=-\ln\lvert x\rvert+C$, that is, $xy=K$ ($K\ne0$): the curve is a rectangular hyperbola.

**Example 15.2.4 (Logistic Equation)** If the growth rate of a population $P(t)$ is proportional to its current size but limited by the carrying capacity $K$ of the environment, then

$$
\frac{\mathrm{d}P}{\mathrm{d}t}=kP\Big(1-\frac PK\Big),\qquad k>0.
$$
This is a separable equation, and the constant solutions $P=0$ and $P=K$ are its two equilibria. For $0<P<K$ we have $\dfrac{K\,\mathrm{d}P}{P(K-P)}=\Big(\dfrac1P+\dfrac1{K-P}\Big)\mathrm{d}P=k\,\mathrm{d}t$, and integration gives $\ln\dfrac{P}{K-P}=kt+C$, so

$$
P(t)=\frac{K}{1+A\mathrm{e}^{-kt}},\qquad A=\frac{K-P_0}{P_0},
$$
where $P_0=P(0)$; the same formula holds for $P_0>K$. Whatever the initial value ($P_0>0$), $P(t)\to K$ as $t\to+\infty$. For $0<P_0<K/2$ the curve is S-shaped, with an inflection point at $P=K/2$, where growth is fastest. This is the *logistic growth* of biology (modelled in [7.4.3](/7.4.3)).

![Direction field and solution curves of the logistic equation P' = kP(1 - P/K) (k = 1, K = 1): P = 0 and P = K are equilibrium solutions, and every other positive solution tends monotonically to K; solutions starting from P_0 < K/2 are S-shaped and grow fastest at P = K/2](./plots/logistic.py)

### 15.2.2. Homogeneous Equations

**Definition 15.2.2** An equation of the form $y'=f\!\left(\dfrac yx\right)$ is called a **homogeneous equation**.

Here "homogeneous" means that the right-hand side is a **homogeneous function** of degree zero in $x$ and $y$ ([2.2.10](/2.2.10)): if $M$ and $N$ are homogeneous functions of the same degree, then $M\,\mathrm{d}x+N\,\mathrm{d}y=0$ is a homogeneous equation. This is not the same as the "homogeneous linear equation" of the next chapter.

**Algorithm 15.2.2** Let $u=\dfrac yx$, that is, $y=xu$. Then $y'=u+xu'$, and the equation becomes the separable equation

$$
x\frac{\mathrm{d}u}{\mathrm{d}x}=f(u)-u,\qquad\frac{\mathrm{d}u}{f(u)-u}=\frac{\mathrm{d}x}{x}.
$$
After solving for $u$, substitute back $u=y/x$; each root of $f(u_0)=u_0$ gives a solution $y=u_0x$.

**Example 15.2.5** Solve the following equations. (1) Solve $y'=\dfrac yx+\tan\dfrac yx$. Let $y=xu$; then $xu'=\tan u$, $\dfrac{\cos u}{\sin u}\mathrm{d}u=\dfrac{\mathrm{d}x}{x}$, so $\ln\lvert\sin u\rvert=\ln\lvert x\rvert+\ln\lvert C\rvert$, and the general solution is $\sin\dfrac yx=Cx$ ($C=0$ corresponds to the solutions $y=k\pi x$ with $u=k\pi$).

(2) Solve $xy'-y=\sqrt{x^2-y^2}$ ($x>0$). The equation becomes $y'=\dfrac yx+\sqrt{1-(y/x)^2}$; letting $y=xu$ gives $xu'=\sqrt{1-u^2}$, $\dfrac{\mathrm{d}u}{\sqrt{1-u^2}}=\dfrac{\mathrm{d}x}{x}$, and the general solution is $\arcsin\dfrac yx=\ln x+C$; there are also the solutions $y=\pm x$ ($u=\pm1$).

### 15.2.3. Equations Reducible to Separable Form

Type (1): $y'=f(ax+by+c)$ ($b\ne0$). Let $u=ax+by+c$. Then $u'=a+bf(u)$, which is separable.

**Example 15.2.6** Solve $y'=(2x+y+3)^2$. Let $u=2x+y+3$; then $u'=2+u^2$, $\dfrac{\mathrm{d}u}{2+u^2}=\mathrm{d}x$, $\dfrac{1}{\sqrt2}\arctan\dfrac{u}{\sqrt2}=x+C$, so the general solution is $2x+y+3=\sqrt2\tan(\sqrt2x+C)$.

Type (2): $y'=f\!\left(\dfrac{a_1x+b_1y+c_1}{a_2x+b_2y+c_2}\right)$. There are three cases:

- $c_1=c_2=0$: the right-hand side is a function of $y/x$, so the equation is homogeneous.
- $\begin{vmatrix}a_1&b_1\\a_2&b_2\end{vmatrix}\ne0$: the lines $a_ix+b_iy+c_i=0$ ($i=1,2$) meet at a point $(x_0,y_0)$. Translating the coordinates by $X=x-x_0$, $Y=y-y_0$ gives $a_ix+b_iy+c_i=a_iX+b_iY$, and the equation becomes the homogeneous equation $\dfrac{\mathrm{d}Y}{\mathrm{d}X}=f\!\left(\dfrac{a_1X+b_1Y}{a_2X+b_2Y}\right)$.
- $\begin{vmatrix}a_1&b_1\\a_2&b_2\end{vmatrix}=0$: $a_2x+b_2y$ is proportional to $a_1x+b_1y$, so the right-hand side is a function of $a_1x+b_1y$, which is case (1).

**Example 15.2.7** Solve $y'=\dfrac{2x-5y+3}{2x+4y-6}$. From $2x_0-5y_0+3=0$ and $2x_0+4y_0-6=0$ we get $x_0=y_0=1$. Letting $X=x-1$, $Y=y-1$ gives $\dfrac{\mathrm{d}Y}{\mathrm{d}X}=\dfrac{2-5w}{2+4w}$ with $w=\dfrac YX$. Now let $Y=Xw$:

$$
X\frac{\mathrm{d}w}{\mathrm{d}X}=\frac{2-5w}{2+4w}-w=\frac{2-7w-4w^2}{2+4w}=-\frac{(4w-1)(w+2)}{2+4w},
$$

hence

$$
\frac{(2+4w)\,\mathrm{d}w}{(4w-1)(w+2)}=-\frac{\mathrm{d}X}{X},\qquad\frac{2+4w}{(4w-1)(w+2)}=\frac{1}{3}\cdot\frac{4}{4w-1}+\frac{2}{3}\cdot\frac{1}{w+2}.
$$
Integration gives $\dfrac13\ln\lvert4w-1\rvert+\dfrac23\ln\lvert w+2\rvert=-\ln\lvert X\rvert+C$, that is, $(4w-1)(w+2)^2X^3=C$; substituting back $w=Y/X$ gives $(4Y-X)(Y+2X)^2=C$. The general solution is therefore

$$
(x-4y+3)(2x+y-3)^2=C.
$$

Type (3): $yf(xy)\,\mathrm{d}x+xg(xy)\,\mathrm{d}y=0$. Let $z=xy$. Then $y=\dfrac zx$ and $x\,\mathrm{d}y=\mathrm{d}z-\dfrac zx\,\mathrm{d}x$; substituting gives $\dfrac zxf(z)\,\mathrm{d}x+g(z)\Big(\mathrm{d}z-\dfrac zx\mathrm{d}x\Big)=0$, that is,

$$
\frac{\mathrm{d}x}{x}=\frac{g(z)\,\mathrm{d}z}{z\big(g(z)-f(z)\big)}.
$$

**Example 15.2.8** Solve $y(xy+1)\,\mathrm{d}x+x(1+xy+x^2y^2)\,\mathrm{d}y=0$. Here $f(z)=z+1$, $g(z)=1+z+z^2$ and $g-f=z^2$, so

$$
\frac{\mathrm{d}x}{x}=\frac{(1+z+z^2)\,\mathrm{d}z}{z^3}=\Big(\frac1{z^3}+\frac1{z^2}+\frac1z\Big)\mathrm{d}z,
$$
and integration gives $\ln\lvert x\rvert=-\dfrac1{2z^2}-\dfrac1z+\ln\lvert z\rvert+C$. Substituting back $z=xy$ and using $\ln\lvert z\rvert-\ln\lvert x\rvert=\ln\lvert y\rvert$, the general solution is

$$
\ln\lvert y\rvert-\frac{1}{2x^2y^2}-\frac1{xy}=C.
$$

## 15.3. First-Order Linear Equations and Bernoulli Equations

### 15.3.1. Structure of Solutions

The standard form of a first-order linear equation is

$$
y'+p(x)y=q(x),\tag{15.1}
$$
where $q(x)$ is called the nonhomogeneous term (forcing term). When $q\equiv0$,

$$
y'+p(x)y=0\tag{15.2}
$$
is called the homogeneous linear equation associated with Eq. (15.1); when $q\not\equiv0$, Eq. (15.1) is called a nonhomogeneous linear equation.

**Proposition 15.3.1** Let $p$ and $q$ be continuous on an interval $I$.

1. If $y_1$ and $y_2$ are solutions of Eq. (15.2), then $\alpha y_1+\beta y_2$ is also a solution of Eq. (15.2) for any constants $\alpha,\beta$;
2. If $y_1$ is a solution of Eq. (15.2) and $y^*$ is a solution of Eq. (15.1), then $y_1+y^*$ is a solution of Eq. (15.1); the difference of two solutions of Eq. (15.1) is a solution of Eq. (15.2).

**Proof** Write $L(y)=y'+p(x)y$. Then $L(\alpha y_1+\beta y_2)=\alpha L(y_1)+\beta L(y_2)$, that is, $L$ is a linear map. Both statements follow directly. $\square$

Therefore the general solution of Eq. (15.1) = one particular solution of Eq. (15.1) + the general solution of Eq. (15.2). This is exactly the structure of the solution set of a linear system $A\boldsymbol{x}=\boldsymbol{b}$ ([2.1.3](/2.1.3)), and the [next chapter](/2.2.16) extends it to order $n$.

The homogeneous equation (15.2) is separable: $\dfrac{\mathrm{d}y}{y}=-p(x)\,\mathrm{d}x$ gives $\ln\lvert y\rvert=-\int p(x)\,\mathrm{d}x+C_1$; together with the solution $y=0$, the general solution is

$$
y=C\mathrm{e}^{-\int p(x)\,\mathrm{d}x},\qquad C\in\mathbb{R}.
$$
Here $\int p(x)\,\mathrm{d}x$ denotes one antiderivative of $p$.

### 15.3.2. Variation of Parameters

Replacing the constant $C$ in the general solution of the homogeneous equation by an unknown function $C(x)$ and substituting into the nonhomogeneous equation is a general method for finding a particular solution of the nonhomogeneous equation, called **variation of parameters** (or variation of constants).

**Theorem 15.3.1** Let $p$ and $q$ be continuous on an interval $I$. Then the general solution of Eq. (15.1) is

$$
y=\mathrm{e}^{-\int p(x)\,\mathrm{d}x}\Big(\int q(x)\mathrm{e}^{\int p(x)\,\mathrm{d}x}\,\mathrm{d}x+C\Big).\tag{15.3}
$$
The solution satisfying $y(x_0)=y_0$ ($x_0\in I$) is unique and equals

$$
y=\mathrm{e}^{-\int_{x_0}^xp(t)\,\mathrm{d}t}\Big(y_0+\int_{x_0}^xq(s)\mathrm{e}^{\int_{x_0}^sp(t)\,\mathrm{d}t}\,\mathrm{d}s\Big).
$$

**Proof** Let $y=C(x)\mathrm{e}^{-\int p\,\mathrm{d}x}$. Then $y'=C'(x)\mathrm{e}^{-\int p\,\mathrm{d}x}-p(x)C(x)\mathrm{e}^{-\int p\,\mathrm{d}x}$; after substitution into Eq. (15.1) the two terms containing $C(x)$ cancel, leaving $C'(x)=q(x)\mathrm{e}^{\int p\,\mathrm{d}x}$, and integration gives Eq. (15.3). Conversely, if $y$ is any solution, let $C(x)=y\,\mathrm{e}^{\int p\,\mathrm{d}x}$; the same computation shows $C'(x)=q(x)\mathrm{e}^{\int p\,\mathrm{d}x}$, so $y$ has the form (15.3). The formula for the initial value problem results from taking the antiderivatives as integrals with variable upper limit, and $C=y_0$ is uniquely determined by the initial condition. $\square$

Another way to see this: multiplying both sides of the equation by $\mu(x)=\mathrm{e}^{\int p\,\mathrm{d}x}$ turns the left-hand side into exactly $(\mu y)'$, so $(\mu y)'=\mu q$, and integration gives the same formula. This $\mu$ is a special case of the **integrating factor** of Section 15.4.

**Algorithm 15.3.1 (First-Order Linear Equations)**

1. Put the equation in standard form $y'+p(x)y=q(x)$ (the coefficient of $y'$ is 1);
2. Compute $P(x)=\int p(x)\,\mathrm{d}x$ (one antiderivative, without a constant);
3. Substitute into formula (15.3): $y=\mathrm{e}^{-P}\big(\int q\,\mathrm{e}^{P}\,\mathrm{d}x+C\big)$; or carry out variation of parameters step by step;
4. If an initial condition is given, use it to determine $C$.

If an equation is not linear in $y$ but is linear in $x$, we may regard $x$ as a function of $y$ (Example 15.3.2).

**Example 15.3.1** Solve the following problems. (1) Solve $y'+2xy=4x$. Here $P=x^2$, and $y=\mathrm{e}^{-x^2}\big(\int4x\mathrm{e}^{x^2}\,\mathrm{d}x+C\big)=\mathrm{e}^{-x^2}(2\mathrm{e}^{x^2}+C)=2+C\mathrm{e}^{-x^2}$.

(2) Solve $xy'-y=x^3+3x^2-2x$. The standard form is $y'-\dfrac yx=x^2+3x-2$, with $P=-\ln\lvert x\rvert$ and $\mathrm{e}^{-P}=\lvert x\rvert$; the sign of the absolute value can be absorbed into the constant, so we take $\mathrm{e}^{-P}=x$:

$$
y=x\Big(\int\frac{x^2+3x-2}{x}\,\mathrm{d}x+C\Big)=x\Big(\frac{x^2}{2}+3x-2\ln\lvert x\rvert+C\Big).
$$

(3) Solve the initial value problem $y'+y\cot x=5\mathrm{e}^{\cos x}$, $y\big(\frac\pi2\big)=-4$. Here $P=\ln\sin x$ (on $0<x<\pi$), and

$$
y=\frac{1}{\sin x}\Big(\int5\mathrm{e}^{\cos x}\sin x\,\mathrm{d}x+C\Big)=\frac{C-5\mathrm{e}^{\cos x}}{\sin x}.
$$
From $y\big(\frac\pi2\big)=C-5=-4$ we get $C=1$, and the solution is $y=\dfrac{1-5\mathrm{e}^{\cos x}}{\sin x}$.

**Example 15.3.2** Solve $y'=\dfrac{1}{2x-y^2}$. The equation is not linear in $y$, but $\dfrac{\mathrm{d}x}{\mathrm{d}y}=2x-y^2$ is a linear equation for $x(y)$: $\dfrac{\mathrm{d}x}{\mathrm{d}y}-2x=-y^2$, so

$$
x=\mathrm{e}^{2y}\Big(-\int y^2\mathrm{e}^{-2y}\,\mathrm{d}y+C\Big)=C\mathrm{e}^{2y}+\frac{2y^2+2y+1}{4}.
$$

### 15.3.3. Bernoulli Equations

**Definition 15.3.1** An equation of the form $y'+p(x)y=q(x)y^n$ ($n\ne0,1$) is called a **Bernoulli equation**.

For $n=0$ or $1$ it is simply a linear equation.

**Algorithm 15.3.2** Divide both sides by $y^n$: $y^{-n}y'+p(x)y^{1-n}=q(x)$. Let $u=y^{1-n}$. Then $u'=(1-n)y^{-n}y'$, and the equation becomes the linear equation for $u$

$$
u'+(1-n)p(x)u=(1-n)q(x);
$$
find $u$ by formula (15.3) and substitute back. For $n>0$, $y=0$ is also a solution.

**Example 15.3.3** Solve the following equations. (1) Solve $y'-y=xy^5$. Let $u=y^{-4}$, so $u'=-4y^{-5}y'$; the equation $y^{-5}y'-y^{-4}=x$ becomes $-\dfrac14u'-u=x$, that is, $u'+4u=-4x$. By Eq. (15.3),

$$
u=\mathrm{e}^{-4x}\Big(\int(-4x)\mathrm{e}^{4x}\,\mathrm{d}x+C\Big)=\mathrm{e}^{-4x}\Big(-x\mathrm{e}^{4x}+\frac14\mathrm{e}^{4x}+C\Big),
$$
so $y^{-4}=-x+\dfrac14+C\mathrm{e}^{-4x}$; there is also the solution $y=0$.

(2) Solve $y'+2xy=xy^4$. Letting $u=y^{-3}$ gives $u'-6xu=-3x$, and $u=\mathrm{e}^{3x^2}\big(\int(-3x)\mathrm{e}^{-3x^2}\,\mathrm{d}x+C\big)=\dfrac12+C\mathrm{e}^{3x^2}$, that is, $\dfrac{1}{y^3}=\dfrac12+C\mathrm{e}^{3x^2}$; there is also the solution $y=0$.

(3) Solve $y'+\dfrac yx=ay^2\ln x$. Letting $u=y^{-1}$ gives $u'-\dfrac ux=-a\ln x$, and $u=x\big(-\int\frac{a\ln x}{x}\,\mathrm{d}x+C\big)=x\Big(C-\dfrac a2\ln^2x\Big)$, that is, $y=\dfrac{1}{x\big(C-\frac a2\ln^2x\big)}$; there is also the solution $y=0$.

Bernoulli equations illustrate the power of a change of variables: an equation that looks nonlinear becomes linear once we change the unknown function. As another example, multiplying both sides of $y'=1+\mathrm{e}^{-y}\sin x$ by $\mathrm{e}^y$ gives $(\mathrm{e}^y)'=\mathrm{e}^y+\sin x$, a linear equation for $u=\mathrm{e}^y$, whose solution is $\mathrm{e}^y=C\mathrm{e}^x-\dfrac12(\sin x+\cos x)$.

## 15.4. Exact Equations and Integrating Factors

### 15.4.1. Exact Equations

A first-order equation is often written in the symmetric form

$$
M(x,y)\,\mathrm{d}x+N(x,y)\,\mathrm{d}y=0,\tag{15.4}
$$
in which $x$ and $y$ play equal roles, and either may be taken as the independent variable.

**Definition 15.4.1** If there is a differentiable function $u(x,y)$ with $\mathrm{d}u=M\,\mathrm{d}x+N\,\mathrm{d}y$, that is, if $u$ is an antiderivative of the differential form $M\,\mathrm{d}x+N\,\mathrm{d}y$ ([2.2.10](/2.2.10#sec-10.5.4)), then Eq. (15.4) is called an **exact equation**. In this case the general solution of Eq. (15.4) is $u(x,y)=C$.

Indeed, along a solution curve $y=y(x)$ we have $\dfrac{\mathrm{d}}{\mathrm{d}x}u(x,y(x))=M+Ny'=0$, so $u$ is constant on solution curves; conversely, by the implicit function theorem (where $N\ne0$), the function determined by $u(x,y)=C$ satisfies the equation.

**Theorem 15.4.1** Suppose $M$ and $N$ have continuous partial derivatives on a **simply connected domain** $D$. Then Eq. (15.4) is exact if and only if

$$
\frac{\partial M}{\partial y}=\frac{\partial N}{\partial x}
$$
on $D$.

Necessity is just the equality of mixed partial derivatives (Proposition 10.5.1); sufficiency requires Green's theorem, namely the criterion for plane **conservative vector fields**, see [2.2.14](/2.2.14). The antiderivative can then be obtained by integrating along a broken line.

**Algorithm 15.4.1 (Solving Exact Equations)** First verify $M_y=N_x$, then find the antiderivative $u$ by one of the following methods:

1. Integration along a broken line: choose $(x_0,y_0)\in D$ such that the broken line $(x_0,y_0)\to(x,y_0)\to(x,y)$ lies in $D$; then $u(x,y)=\displaystyle\int_{x_0}^xM(s,y_0)\,\mathrm{d}s+\int_{y_0}^yN(x,t)\,\mathrm{d}t$;
2. Partial integration: $u=\int M(x,y)\,\mathrm{d}x+\varphi(y)$ (treating $y$ as a constant during integration); determine $\varphi'(y)$ from $u_y=N$ and integrate to obtain $\varphi(y)$;
3. Grouping terms: group the terms of $M\,\mathrm{d}x+N\,\mathrm{d}y$ and use familiar exact differentials to write down $\mathrm{d}u$ directly.

Some common exact differentials:

| Expression | Exact differential | Expression | Exact differential |
|---|---|---|---|
| $x\,\mathrm{d}y+y\,\mathrm{d}x$ | $\mathrm{d}(xy)$ | $x\,\mathrm{d}x+y\,\mathrm{d}y$ | $\frac12\mathrm{d}(x^2+y^2)$ |
| $\dfrac{x\,\mathrm{d}y-y\,\mathrm{d}x}{x^2}$ | $\mathrm{d}\big(\frac yx\big)$ | $\dfrac{y\,\mathrm{d}x-x\,\mathrm{d}y}{y^2}$ | $\mathrm{d}\big(\frac xy\big)$ |
| $\dfrac{x\,\mathrm{d}y-y\,\mathrm{d}x}{x^2+y^2}$ | $\mathrm{d}\big(\arctan\frac yx\big)$ | $\dfrac{x\,\mathrm{d}y-y\,\mathrm{d}x}{xy}$ | $\mathrm{d}\big(\ln\big\lvert\frac yx\big\rvert\big)$ |
| $\dfrac{x\,\mathrm{d}x+y\,\mathrm{d}y}{x^2+y^2}$ | $\frac12\mathrm{d}\ln(x^2+y^2)$ | $\dfrac{x\,\mathrm{d}y-y\,\mathrm{d}x}{x^2-y^2}$ | $\frac12\mathrm{d}\big(\ln\big\lvert\frac{x+y}{x-y}\big\rvert\big)$ |

**Example 15.4.1** Solve $(2x^3+3y)\,\mathrm{d}x+(3x+y-1)\,\mathrm{d}y=0$. Since $M_y=3=N_x$, the equation is exact. Three methods:

- Integration along a broken line: taking $(x_0,y_0)=(0,0)$, $u=\int_0^x2s^3\,\mathrm{d}s+\int_0^y(3x+t-1)\,\mathrm{d}t=\dfrac{x^4}2+3xy+\dfrac{y^2}2-y$;
- Partial integration: $u=\int(2x^3+3y)\,\mathrm{d}x=\dfrac{x^4}2+3xy+\varphi(y)$, and $u_y=3x+\varphi'(y)=3x+y-1$ gives $\varphi=\dfrac{y^2}2-y$;
- Grouping terms: $2x^3\,\mathrm{d}x+3(y\,\mathrm{d}x+x\,\mathrm{d}y)+(y-1)\,\mathrm{d}y=\mathrm{d}\Big(\dfrac{x^4}2+3xy+\dfrac{y^2}2-y\Big)$.

The general solution is $x^4+6xy+y^2-2y=C$.

**Example 15.4.2** Solve the following equations. (1) $2x(y\mathrm{e}^{x^2}-1)\,\mathrm{d}x+\mathrm{e}^{x^2}\,\mathrm{d}y=0$: $M_y=2x\mathrm{e}^{x^2}=N_x$. Grouping, $(2xy\mathrm{e}^{x^2}\,\mathrm{d}x+\mathrm{e}^{x^2}\,\mathrm{d}y)-2x\,\mathrm{d}x=\mathrm{d}(y\mathrm{e}^{x^2})-\mathrm{d}(x^2)$, so the general solution is $y\mathrm{e}^{x^2}-x^2=C$.

(2) $(\cos y+y\cos x)\,\mathrm{d}x+(\sin x-x\sin y)\,\mathrm{d}y=0$: grouping, $(\cos y\,\mathrm{d}x-x\sin y\,\mathrm{d}y)+(y\cos x\,\mathrm{d}x+\sin x\,\mathrm{d}y)=\mathrm{d}(x\cos y)+\mathrm{d}(y\sin x)$, so the general solution is $x\cos y+y\sin x=C$.

### 15.4.2. Integrating Factors

The equation $y\,\mathrm{d}x-x\,\mathrm{d}y=0$ is not exact ($M_y=1\ne-1=N_x$), but after multiplication by $\dfrac1{y^2}$ it becomes $\mathrm{d}\big(\frac xy\big)=0$. This suggests first multiplying by a factor that makes the equation exact.

**Definition 15.4.2** If there is a differentiable function $\mu(x,y)$, not identically zero, such that $\mu M\,\mathrm{d}x+\mu N\,\mathrm{d}y=0$ is exact, then $\mu$ is called an **integrating factor** of Eq. (15.4).

Where $\mu\ne0$, multiplying by $\mu$ does not change the solutions of the equation; the zeros and singularities of $\mu$ must be checked separately for solutions gained or lost. Integrating factors are not unique: by the table of common differentials above, $\dfrac1{y^2}$, $\dfrac1{x^2}$, $\dfrac1{xy}$ and $\dfrac1{x^2+y^2}$ are all integrating factors of $y\,\mathrm{d}x-x\,\mathrm{d}y=0$. By definition, $\mu$ is an integrating factor if and only if $(\mu M)_y=(\mu N)_x$, that is,

$$
N\mu_x-M\mu_y=(M_y-N_x)\mu.
$$
This is a partial differential equation for $\mu$, generally harder to solve than the original equation. But if we require $\mu$ to depend on only one variable, it reduces to an ordinary differential equation.

**Theorem 15.4.2** Suppose $M$ and $N$ have continuous partial derivatives.

1. If $\dfrac{M_y-N_x}{N}=f(x)$ depends only on $x$, then $\mu=\mathrm{e}^{\int f(x)\,\mathrm{d}x}$ is an integrating factor;
2. If $\dfrac{M_y-N_x}{M}=g(y)$ depends only on $y$, then $\mu=\mathrm{e}^{-\int g(y)\,\mathrm{d}y}$ is an integrating factor.

**Proof** (1) If $\mu=\mu(x)$, then $\mu_y=0$, and the condition $N\mu_x-M\mu_y=(M_y-N_x)\mu$ becomes $\mu'(x)=f(x)\mu$, which $\mu=\mathrm{e}^{\int f\,\mathrm{d}x}$ satisfies. (2) If $\mu=\mu(y)$, the condition becomes $-M\mu'(y)=(M_y-N_x)\mu$, that is, $\mu'=-g(y)\mu$. $\square$

For the first-order linear equation $\mathrm{d}y+(p(x)y-q(x))\,\mathrm{d}x=0$ we have $\dfrac{M_y-N_x}{N}=p(x)$, and the integrating factor $\mathrm{e}^{\int p\,\mathrm{d}x}$ is exactly the $\mu$ of Section 15.3.2.

**Theorem 15.4.3** If $M$ and $N$ are **homogeneous functions** of the same degree and $Mx+Ny\ne0$, then $\mu=\dfrac{1}{Mx+Ny}$ is an integrating factor of Eq. (15.4).

**Proof** Let $M$ and $N$ be homogeneous of degree $k$. By Euler's homogeneous function theorem (Theorem 10.7.2), $xM_x+yM_y=kM$ and $xN_x+yN_y=kN$. Write $S=Mx+Ny$ and compute directly:

$$
\Big(\frac MS\Big)_y-\Big(\frac NS\Big)_x=\frac{M_yS-MS_y-N_xS+NS_x}{S^2},
$$
where $S_y=xM_y+N+yN_y$ and $S_x=M+xM_x+yN_x$. Expanding, the numerator equals

$$
N(yM_y+xM_x)-M(xN_x+yN_y)=N\cdot kM-M\cdot kN=0.\qquad\square
$$

**Example 15.4.3** Solve the following equations. (1) Solve $(x^2+y^2+x)\,\mathrm{d}x+xy\,\mathrm{d}y=0$. Here $M_y-N_x=2y-y=y$ and $\dfrac{M_y-N_x}{N}=\dfrac1x$, so $\mu=x$ is an integrating factor. After multiplication by $x$, $(x^3+xy^2+x^2)\,\mathrm{d}x+x^2y\,\mathrm{d}y=0$ is exact, with general solution $\dfrac{x^4}4+\dfrac{x^3}3+\dfrac{x^2y^2}2=C$.

(2) Solve $(x^4+y^4)\,\mathrm{d}x-xy^3\,\mathrm{d}y=0$. $M$ and $N$ are homogeneous of degree 4 and $Mx+Ny=x^5$, so $\dfrac1{x^5}$ is an integrating factor:

$$
\frac{\mathrm{d}x}{x}+\Big(\frac{y^4}{x^5}\,\mathrm{d}x-\frac{y^3}{x^4}\,\mathrm{d}y\Big)=\mathrm{d}\Big(\ln\lvert x\rvert-\frac{y^4}{4x^4}\Big)=0,
$$
and the general solution is $\ln\lvert x\rvert-\dfrac{y^4}{4x^4}=C$, that is, $x=C\mathrm{e}^{y^4/(4x^4)}$. (It is also a homogeneous equation and can be solved by Algorithm 15.2.2.)

More often an integrating factor is found by inspection: separate out the terms of the equation that can be combined into one of the common differentials (the numerators in the table), and choose an integrating factor that makes them exact while keeping the remaining terms exact as well.

**Example 15.4.4** Solve the following equations. (1) $x\,\mathrm{d}y-y\,\mathrm{d}x-(1-x^2)\,\mathrm{d}x=0$: multiplying by $\dfrac1{x^2}$ gives $\mathrm{d}\big(\frac yx\big)-\Big(\dfrac1{x^2}-1\Big)\mathrm{d}x=0$, with general solution $\dfrac yx+\dfrac1x+x=C$.

(2) $x\,\mathrm{d}x+y\,\mathrm{d}y-4y^3(x^2+y^2)\,\mathrm{d}y=0$: multiplying by $\dfrac1{x^2+y^2}$ gives $\dfrac12\mathrm{d}\ln(x^2+y^2)-\mathrm{d}(y^4)=0$, with general solution $\dfrac12\ln(x^2+y^2)-y^4=C$.

(3) $x^2y'+xy+\sqrt{1-x^2y^2}=0$: write it as $x(x\,\mathrm{d}y+y\,\mathrm{d}x)+\sqrt{1-x^2y^2}\,\mathrm{d}x=0$; multiplying by $\dfrac{1}{x\sqrt{1-x^2y^2}}$ gives $\dfrac{\mathrm{d}(xy)}{\sqrt{1-(xy)^2}}+\dfrac{\mathrm{d}x}{x}=0$, with general solution $\arcsin(xy)+\ln\lvert x\rvert=C$.

(4) $(1+xy)y\,\mathrm{d}x+(1-xy)x\,\mathrm{d}y=0$: rearrange as $(y\,\mathrm{d}x+x\,\mathrm{d}y)+xy(y\,\mathrm{d}x-x\,\mathrm{d}y)=0$, that is, $\mathrm{d}(xy)+xy(y\,\mathrm{d}x-x\,\mathrm{d}y)=0$. Multiplying by $\dfrac{1}{x^2y^2}$ gives $\dfrac{\mathrm{d}(xy)}{(xy)^2}+\dfrac{\mathrm{d}x}{x}-\dfrac{\mathrm{d}y}{y}=0$, with general solution $\ln\Big\lvert\dfrac xy\Big\rvert-\dfrac1{xy}=C$.

## 15.5. Higher-Order Equations Reducible in Order

Higher-order equations are generally much harder than first-order ones, but for several classes the order can be lowered by changing the unknown function, reducing them to first-order equations.

### 15.5.1. $y^{(n)}=f(x)$

The right-hand side contains only $x$. Each integration lowers the order by one, and integrating $n$ times in succession gives a general solution with $n$ arbitrary constants.

**Example 15.5.1** Solve $y^{(4)}=\sin x+x$. Integrating successively:

$$
y'''=-\cos x+\frac{x^2}2+C_1,\quad y''=-\sin x+\frac{x^3}6+C_1x+C_2,\quad y'=\cos x+\frac{x^4}{24}+\frac{C_1}2x^2+C_2x+C_3,
$$
so $y=\sin x+\dfrac{x^5}{120}+\dfrac{C_1}6x^3+\dfrac{C_2}2x^2+C_3x+C_4$, where the constants $C_1/6$ and $C_2/2$ may be renamed as arbitrary constants.

### 15.5.2. Equations $y''=f(x,y')$ Not Containing $y$ Explicitly

Let $y'=p(x)$. Then $y''=p'$, and the equation becomes the first-order equation $p'=f(x,p)$. After solving for $p=\varphi(x,C_1)$, integrate once more. More generally, for an equation not containing $y,y',\dots,y^{(k-1)}$ we may let $p=y^{(k)}$.

**Example 15.5.2** Solve the following problems. (1) Solve $x^2y''+xy'=1$ ($x>0$). Let $p=y'$; then $p'+\dfrac px=\dfrac1{x^2}$, and by Eq. (15.3), $p=\dfrac1x\big(\int\frac1x\,\mathrm{d}x+C_1\big)=\dfrac{\ln x+C_1}{x}$, so $y=\dfrac12\ln^2x+C_1\ln x+C_2$.

(2) Solve $y^{(5)}=\dfrac1xy^{(4)}$. Let $p=y^{(4)}$; then $\dfrac{\mathrm{d}p}{p}=\dfrac{\mathrm{d}x}{x}$, $p=C_1x$, and four more integrations give $y=\dfrac{C_1}{120}x^5+C_2x^3+C_3x^2+C_4x+C_5$ (the coefficients $\frac16$, $\frac12$ produced by integration have been absorbed into the arbitrary constants).

(3) Solve the initial value problem $y''+2x(y')^2=0$, $y(0)=1$, $y'(0)=0$. Let $p=y'$; then $p'=-2xp^2$. For $p\ne0$ we get $\dfrac1p=x^2+C$; there is also the solution $p=0$. Since $p(0)=0$, we must take $p\equiv0$ (the $p$ obtained from $\frac1p=x^2+C$ never vanishes), so $y'\equiv0$ and $y\equiv1$. Had we dropped $p=0$ when separating variables, we would have missed this solution.

**Example 15.5.3** A plane curve of constant nonzero curvature $K$ is a circle. Let the curve be $y=y(x)$. By the formula for **curvature** ([2.2.7](/2.2.7)), $\dfrac{y''}{(1+y'^2)^{3/2}}=K$ (on a piece where $y''>0$, with the orientation chosen so that $K>0$). Let $p=y'$:

$$
\frac{\mathrm{d}p}{(1+p^2)^{3/2}}=K\,\mathrm{d}x,\qquad\frac{p}{\sqrt{1+p^2}}=K(x-C_1).
$$
Solving gives $p=\dfrac{K(x-C_1)}{\sqrt{1-K^2(x-C_1)^2}}$, and another integration gives $y=-\dfrac1K\sqrt{1-K^2(x-C_1)^2}+C_2$, that is,

$$
(x-C_1)^2+(y-C_2)^2=\frac1{K^2},
$$
a circle of radius $\dfrac1K$.

**Example 15.5.4 (Catenary, Continued from Example 15.1.3)** Solve $y''=a\sqrt{1+y'^2}$, $y(0)=y'(0)=0$. Let $p=y'$; then $\dfrac{\mathrm{d}p}{\sqrt{1+p^2}}=a\,\mathrm{d}x$. Putting $p=\sinh s$, the left-hand side becomes $\mathrm{d}s$, so $s=ax+c$; from $p(0)=0$ we get $c=0$, that is, $y'=\sinh ax$. Integrating again and using $y(0)=0$,

$$
y=\frac{\cosh ax-1}{a}.
$$
The catenary is the graph of a **hyperbolic function**; this is why the hyperbolic cosine is also called the "catenary function".

### 15.5.3. Equations $y''=f(y,y')$ Not Containing $x$ Explicitly

Take $y$ as the new independent variable and let $y'=p(y)$. Then by the chain rule

$$
y''=\frac{\mathrm{d}p}{\mathrm{d}y}\cdot\frac{\mathrm{d}y}{\mathrm{d}x}=p\frac{\mathrm{d}p}{\mathrm{d}y},
$$
and the equation becomes the first-order equation $p\dfrac{\mathrm{d}p}{\mathrm{d}y}=f(y,p)$ for $p$ as a function of $y$. After solving for $p=\varphi(y,C_1)$, the equation $\dfrac{\mathrm{d}y}{\varphi(y,C_1)}=\mathrm{d}x$ is separable.

Note that the substitutions for the two classes differ: when $y$ is absent, $p$ is a function of $x$ and $y''=\dfrac{\mathrm{d}p}{\mathrm{d}x}$; when $x$ is absent, $p$ is a function of $y$ and $y''=p\dfrac{\mathrm{d}p}{\mathrm{d}y}$.

**Example 15.5.5** Solve the following equations. (1) Solve $yy''-(y')^2=0$. Let $y'=p(y)$; then $yp\dfrac{\mathrm{d}p}{\mathrm{d}y}-p^2=0$, so $p=0$ or $y\dfrac{\mathrm{d}p}{\mathrm{d}y}=p$. The latter gives $p=C_1y$, that is, $y'=C_1y$ and $y=C_2\mathrm{e}^{C_1x}$; $p=0$ gives $y=C$, which is already included ($C_1=0$). Alternatively, group terms: dividing both sides by $y^2$ gives $\big(\frac{y'}{y}\big)'=0$.

(2) Solve $y''=(y')^3+y'$. Let $y'=p(y)$; then $p\dfrac{\mathrm{d}p}{\mathrm{d}y}=p^3+p$, so $p=0$ ($y=C$) or $\dfrac{\mathrm{d}p}{1+p^2}=\mathrm{d}y$, giving $\arctan p=y+C_1$ and $y'=\tan(y+C_1)$. Separating variables, $\cot(y+C_1)\,\mathrm{d}y=\mathrm{d}x$, so $\ln\lvert\sin(y+C_1)\rvert=x+\ln\lvert C_2\rvert$, and the general solution is $\sin(y+C_1)=C_2\mathrm{e}^x$.

## Summary

| Type of equation | Form | Method |
|---|---|---|
| Separable equation | $y'=f(x)g(y)$ | $\int\frac{\mathrm{d}y}{g(y)}=\int f\,\mathrm{d}x+C$; add the solutions $y=c$ with $g(c)=0$ |
| Homogeneous equation | $y'=f(y/x)$ | $y=xu$, $\frac{\mathrm{d}u}{f(u)-u}=\frac{\mathrm{d}x}{x}$ |
| Function of a linear combination | $y'=f(ax+by+c)$ | $u=ax+by+c$ |
| Ratio of linear expressions | $y'=f\big(\frac{a_1x+b_1y+c_1}{a_2x+b_2y+c_2}\big)$ | Nonzero determinant: translate to the intersection point, giving a homogeneous equation; zero determinant: reduce to the previous type |
| $xy$ type | $yf(xy)\,\mathrm{d}x+xg(xy)\,\mathrm{d}y=0$ | $z=xy$, $\frac{\mathrm{d}x}{x}=\frac{g\,\mathrm{d}z}{z(g-f)}$ |
| First-order linear equation | $y'+p(x)y=q(x)$ | Variation of parameters, Eq. (15.3) |
| Bernoulli equation | $y'+py=qy^n$ | $u=y^{1-n}$ gives a linear equation |
| Exact equation | $M\,\mathrm{d}x+N\,\mathrm{d}y=0$, $M_y=N_x$ | Find the antiderivative $u$ by broken-line integration, partial integration or grouping terms; $u=C$ |
| Integrating factor | $M_y\ne N_x$ | $\frac{M_y-N_x}{N}=f(x)$: $\mathrm{e}^{\int f\mathrm{d}x}$; $\frac{M_y-N_x}{M}=g(y)$: $\mathrm{e}^{-\int g\mathrm{d}y}$; homogeneous of the same degree: $\frac1{Mx+Ny}$; inspection |
| Reducible-order equation | $y^{(n)}=f(x)$; $y''=f(x,y')$; $y''=f(y,y')$ | Successive integration; $y'=p(x)$; $y'=p(y)$, $y''=p\frac{\mathrm{d}p}{\mathrm{d}y}$ |

A few common cautions: when separating variables or dividing by an expression, check the solutions given by the vanishing of the divisor (Example 15.2.1, Example 15.5.2); an implicit solution $u(x,y)=C$ is already an acceptable answer; a general solution need not include all solutions, but the general solution of a linear equation does (Theorem 15.3.1).
