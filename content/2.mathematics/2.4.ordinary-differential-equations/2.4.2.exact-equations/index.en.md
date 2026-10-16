---
title: Exact Equations and Integrating Factors
source_hash: 071ead96cd40
---

The starting point of elementary integration is this: if the left-hand side of a first-order equation in symmetric form $P\,\mathrm{d}x+Q\,\mathrm{d}y=0$ happens to be the total differential of some function, the equation is "integrated" at once. In this chapter we first give a rigorous proof of the necessary and sufficient condition $\partial P/\partial y=\partial Q/\partial x$ for this to happen, together with two integration paths for constructing the potential and the common formulas for recognizing total differentials. We then study integrating factors, which turn a general equation into an exact one: the partial differential equation they satisfy, the necessary and sufficient condition for an integrating factor depending on one variable only, the set of all integrating factors, and the method of finding integrating factors by grouping terms. The separable and first-order linear equations of the next chapter, [2.4.3](/2.4.3), can be viewed as special cases of what is done here. The routine solution steps and more examples are in calculus, [2.2.15](/2.2.15#sec-15.4); here the emphasis is on the theory.

## 2.1. Exact Equations

### 2.1.1. Definition

Consider the first-order equation in symmetric form

$$
P(x,y)\,\mathrm{d}x+Q(x,y)\,\mathrm{d}y=0,\tag{2.1}
$$
where $P$ and $Q$ are continuous on a region $D$ and do not vanish simultaneously.

**Definition 2.1.1** If there is a differentiable function $\Phi(x,y)$ on $D$ such that

$$
\mathrm{d}\Phi(x,y)=P(x,y)\,\mathrm{d}x+Q(x,y)\,\mathrm{d}y,\quad\text{that is,}\quad\frac{\partial\Phi}{\partial x}=P,\quad\frac{\partial\Phi}{\partial y}=Q,\tag{2.2}
$$
then Eq. (2.1) is called an **exact equation** (**exact differential equation**).

**Theorem 2.1.1** Let Eq. (2.1) be exact, with $\Phi$ satisfying (2.2). Then in a region where $Q\ne0$, a differentiable function $y=\varphi(x)$ is a solution of Eq. (2.1) if and only if $\Phi\big(x,\varphi(x)\big)$ is constant. Hence $\Phi(x,y)=C$ is a general integral of Eq. (2.1), and the solution satisfying $y(x_0)=y_0$ is determined by $\Phi(x,y)=\Phi(x_0,y_0)$.

**Proof** By the chain rule,

$$
\frac{\mathrm{d}}{\mathrm{d}x}\Phi\big(x,\varphi(x)\big)=P\big(x,\varphi(x)\big)+Q\big(x,\varphi(x)\big)\varphi'(x),
$$
so $\varphi$ satisfies $P+Qy'=0$ if and only if the derivative of $\Phi(x,\varphi(x))$ vanishes identically, that is, if and only if it is constant. Conversely, where $Q=\Phi_y\ne0$, the **implicit function theorem** shows that $\Phi(x,y)=\Phi(x_0,y_0)$ determines, near $(x_0,y_0)$, a unique differentiable function $y=\varphi(x)$ with $\varphi(x_0)=y_0$, which is the required solution. The case $P\ne0$ is analogous, with $x$ regarded as a function of $y$. $\square$

Geometrically, the integral curves of an exact equation are the level curves of the function $\Phi$. The proof also shows that where $Q\ne0$ there is exactly one integral curve through each point, so the initial value problem has a unique solution.

### 2.1.2. The Criterion for Exactness

**Theorem 2.1.2** Let $P$ and $Q$ be continuous on the rectangle $D=\{(x,y)\mid a<x<b,\ c<y<d\}$ with continuous partial derivatives $\dfrac{\partial P}{\partial y}$ and $\dfrac{\partial Q}{\partial x}$. Then Eq. (2.1) is exact if and only if

$$
\frac{\partial P}{\partial y}(x,y)\equiv\frac{\partial Q}{\partial x}(x,y),\qquad(x,y)\in D.\tag{2.3}
$$
When this condition holds, for any $(x_0,y_0)\in D$ a general integral of the equation is

$$
\int_{x_0}^xP(s,y)\,\mathrm{d}s+\int_{y_0}^yQ(x_0,t)\,\mathrm{d}t=C\tag{2.4}
$$
or

$$
\int_{x_0}^xP(s,y_0)\,\mathrm{d}s+\int_{y_0}^yQ(x,t)\,\mathrm{d}t=C.\tag{2.5}
$$

**Proof** Necessity. If $\Phi$ satisfies (2.2), then

$$
\frac{\partial P}{\partial y}=\frac{\partial^2\Phi}{\partial y\,\partial x},\qquad\frac{\partial Q}{\partial x}=\frac{\partial^2\Phi}{\partial x\,\partial y}.
$$
By hypothesis both mixed partial derivatives are continuous, so they are equal ([2.2.10 Proposition 10.5.1](/2.2.10#prop-10.5.1)), which gives (2.3).

Sufficiency. Assume (2.3); we must construct $\Phi$ satisfying (2.2). To make the first equation hold, set

$$
\Phi(x,y)=\int_{x_0}^xP(s,y)\,\mathrm{d}s+\psi(y),
$$
with $\psi$ to be determined; since $D$ is a rectangle, the segment $[x_0,x]\times\{y\}$ lies in $D$. Because $P$ and $P_y$ are continuous on $D$, we may use **differentiation under the integral sign** (applied on a closed rectangle containing the point in question), and then (2.3):

$$
\frac{\partial\Phi}{\partial y}=\int_{x_0}^x\frac{\partial P}{\partial y}(s,y)\,\mathrm{d}s+\psi'(y)=\int_{x_0}^x\frac{\partial Q}{\partial x}(s,y)\,\mathrm{d}s+\psi'(y)=Q(x,y)-Q(x_0,y)+\psi'(y).
$$
For the second equation to hold, it suffices to take $\psi'(y)=Q(x_0,y)$, that is, $\psi(y)=\displaystyle\int_{y_0}^yQ(x_0,t)\,\mathrm{d}t$. The function so constructed,

$$
\Phi(x,y)=\int_{x_0}^xP(s,y)\,\mathrm{d}s+\int_{y_0}^yQ(x_0,t)\,\mathrm{d}t,
$$
satisfies (2.2), and Theorem 2.1.1 yields the general integral (2.4). In the same way (satisfying the second equation first) we can construct

$$
\Psi(x,y)=\int_{x_0}^xP(s,y_0)\,\mathrm{d}s+\int_{y_0}^yQ(x,t)\,\mathrm{d}t.
$$
$\Phi$ and $\Psi$ have the same total differential, so on the connected set $D$ they differ by a constant; since moreover $\Phi(x_0,y_0)=\Psi(x_0,y_0)=0$, we have $\Phi\equiv\Psi$, and (2.5) and (2.4) give the same general integral. $\square$

Formula (2.4) is the line integral of the second kind along the polygonal path $(x_0,y_0)\to(x_0,y)\to(x,y)$, and (2.5) is the one along $(x_0,y_0)\to(x,y_0)\to(x,y)$. The rectangle is used in the proof only to keep these paths inside $D$. The theorem also holds on a general **simply connected domain**: there, by **Green's theorem**, condition (2.3) makes the line integral path-independent, and $\Phi(x,y)=\int_{(x_0,y_0)}^{(x,y)}P\,\mathrm{d}x+Q\,\mathrm{d}y$ is a potential ($P\boldsymbol{i}+Q\boldsymbol{j}$ is a **conservative vector field**, [2.2.14](/2.2.14)). If the region is not simply connected, the conclusion may fail.

**Example 2.1.1** On the plane with the origin removed, the equation

$$
\frac{x\,\mathrm{d}y-y\,\mathrm{d}x}{x^2+y^2}=0
$$
satisfies (2.3): $P=\dfrac{-y}{x^2+y^2}$, $Q=\dfrac{x}{x^2+y^2}$, and $P_y=Q_x=\dfrac{y^2-x^2}{(x^2+y^2)^2}$. But the integral of the left-hand side once counterclockwise around the unit circle is $2\pi\ne0$, so there is no single-valued potential on the whole punctured plane, and the equation is not exact there. In any simply connected region that neither contains nor winds around the origin (for example the right half-plane) it is exact, with $\Phi=\arctan\dfrac yx$ (the polar angle). The integral curves are the rays $\theta=C$ from the origin, the same as for $y'=y/x$ in Example 1.2.1; the point is only that the general integral "polar angle" cannot be given continuous values on the whole punctured plane.

### 2.1.3. Examples

For the detailed steps of partial integration and of integration along polygonal paths, see [2.2.15 Algorithm 15.4.1](/2.2.15#alg-15.4.1).

**Example 2.1.2** Solve $(2x\sin y+3x^2y)\,\mathrm{d}x+(x^3+x^2\cos y+y^2)\,\mathrm{d}y=0$.

Since $P_y=2x\cos y+3x^2=Q_x$, the equation is exact. Integrating $\Phi_x=2x\sin y+3x^2y$ with respect to $x$ gives $\Phi=x^2\sin y+x^3y+\psi(y)$; substituting into $\Phi_y=x^2\cos y+x^3+\psi'(y)=x^3+x^2\cos y+y^2$ gives $\psi'(y)=y^2$, $\psi=\dfrac13y^3$. A general integral is

$$
x^2\sin y+x^3y+\frac13y^3=C.
$$
Alternatively, we can group terms into total differentials:

$$
(2x\sin y\,\mathrm{d}x+x^2\cos y\,\mathrm{d}y)+(3x^2y\,\mathrm{d}x+x^3\,\mathrm{d}y)+y^2\,\mathrm{d}y=\mathrm{d}(x^2\sin y)+\mathrm{d}(x^3y)+\mathrm{d}\Big(\frac13y^3\Big).
$$

![The integral curves of Example 2.1.2 are the level curves of Phi(x, y) = x^2 sin y + x^3 y + y^3/3; several curves Phi = C are shown, with color indicating the value of C](./plots/exact-level-curves.py)

**Example 2.1.3** Solve $(3x^2+6xy^2)\,\mathrm{d}x+(6x^2y+4y^3)\,\mathrm{d}y=0$. Here $P_y=12xy=Q_x$. Using (2.5) with $(x_0,y_0)=(0,0)$:

$$
\int_0^x3s^2\,\mathrm{d}s+\int_0^y(6x^2t+4t^3)\,\mathrm{d}t=x^3+3x^2y^2+y^4=C.
$$

## 2.2. Recognizing Total Differentials

### 2.2.1. Common Total Differentials

Many equations can be solved without checking (2.3): we group the terms on the left-hand side suitably and recognize total differentials directly with the following formulas. Each formula holds in regions where its denominator does not vanish.

| Differential form | Total differential | Differential form | Total differential |
|---|---|---|---|
| $y\,\mathrm{d}x+x\,\mathrm{d}y$ | $\mathrm{d}(xy)$ | $x\,\mathrm{d}x+y\,\mathrm{d}y$ | $\dfrac12\mathrm{d}(x^2+y^2)$ |
| $\dfrac{y\,\mathrm{d}x-x\,\mathrm{d}y}{y^2}$ | $\mathrm{d}\Big(\dfrac xy\Big)$ | $\dfrac{x\,\mathrm{d}y-y\,\mathrm{d}x}{x^2}$ | $\mathrm{d}\Big(\dfrac yx\Big)$ |
| $\dfrac{y\,\mathrm{d}x-x\,\mathrm{d}y}{xy}$ | $\mathrm{d}\Big(\ln\Big\lvert\dfrac xy\Big\rvert\Big)$ | $\dfrac{y\,\mathrm{d}x+x\,\mathrm{d}y}{xy}$ | $\mathrm{d}(\ln\lvert xy\rvert)$ |
| $\dfrac{y\,\mathrm{d}x-x\,\mathrm{d}y}{x^2+y^2}$ | $\mathrm{d}\Big(\arctan\dfrac xy\Big)$ | $\dfrac{x\,\mathrm{d}y-y\,\mathrm{d}x}{x^2+y^2}$ | $\mathrm{d}\Big(\arctan\dfrac yx\Big)$ |
| $\dfrac{y\,\mathrm{d}x-x\,\mathrm{d}y}{x^2-y^2}$ | $\dfrac12\mathrm{d}\Big(\ln\Big\lvert\dfrac{x-y}{x+y}\Big\rvert\Big)$ | $\dfrac{x\,\mathrm{d}x+y\,\mathrm{d}y}{x^2+y^2}$ | $\dfrac12\mathrm{d}\ln(x^2+y^2)$ |

The entries whose numerator is $y\,\mathrm{d}x-x\,\mathrm{d}y$ or $x\,\mathrm{d}y-y\,\mathrm{d}x$ show that one and the same differential form becomes a total differential after multiplication by different factors ($1/y^2$, $1/x^2$, $1/(xy)$, $1/(x^2\pm y^2)$). This is an instance of the non-uniqueness of integrating factors discussed in Section 2.3.

### 2.2.2. Examples

**Example 2.2.1** Solve $xf'(x^2+y^2)\,\mathrm{d}x+yf'(x^2+y^2)\,\mathrm{d}y=0$, where $f$ is continuously differentiable. The left-hand side equals $\dfrac12\mathrm{d}\big[f(x^2+y^2)\big]$, so a general integral is $f(x^2+y^2)=C$.

**Example 2.2.2** Solve $x\,\mathrm{d}x+\dfrac{(x+y)\,\mathrm{d}x-(x-y)\,\mathrm{d}y}{x^2+y^2}=0$. Splitting the fraction into two groups,

$$
x\,\mathrm{d}x+\frac{x\,\mathrm{d}x+y\,\mathrm{d}y}{x^2+y^2}+\frac{y\,\mathrm{d}x-x\,\mathrm{d}y}{x^2+y^2}=\mathrm{d}\Big[\frac{x^2}{2}+\frac12\ln(x^2+y^2)+\arctan\frac xy\Big]=0,
$$
so a general integral is $\dfrac{x^2}{2}+\dfrac12\ln(x^2+y^2)+\arctan\dfrac xy=C$ (in a region where $y\ne0$; across $y=0$, $\arctan\frac xy$ must be replaced by a continuous branch).

**Example 2.2.3** Solve the initial value problem $xy\,\mathrm{d}x+\dfrac12(x^2+y)\,\mathrm{d}y=0$, $y(0)=2$.

The left-hand side is $\Big(xy\,\mathrm{d}x+\dfrac{x^2}2\,\mathrm{d}y\Big)+\dfrac y2\,\mathrm{d}y=\mathrm{d}\Big(\dfrac{x^2y}{2}\Big)+\mathrm{d}\Big(\dfrac{y^2}{4}\Big)$, so a general integral is $2x^2y+y^2=C$. From $y(0)=2$ we get $C=4$. Solving the quadratic equation $y^2+2x^2y-4=0$ for $y$ and taking the root with $y(0)=2$:

$$
y=-x^2+\sqrt{x^4+4},\qquad x\in\mathbb{R}.
$$

![The family of integral curves 2x^2 y + y^2 = C of Example 2.2.3 (thin lines) and the solution y = -x^2 + sqrt(x^4 + 4) of the initial value problem y(0) = 2 (thick line), which exists on the whole real line and tends to 0 as |x| grows](./plots/ivp-family.py)

## 2.3. Integrating Factors

### 2.3.1. Definition and the Equation for an Integrating Factor

**Definition 2.3.1** If there is a function $\mu(x,y)$, continuously differentiable and nowhere zero on a region $D$, such that

$$
\mu(x,y)P(x,y)\,\mathrm{d}x+\mu(x,y)Q(x,y)\,\mathrm{d}y=0
$$
is exact, then $\mu$ is called an **integrating factor** of Eq. (2.1).

The condition $\mu\ne0$ ensures that multiplying by $\mu$ does not change the integral curves of the equation. In practice, the integrating factors one finds often vanish or are undefined on certain curves (for example $1/y^2$ on $y=0$), and these curves must be checked separately for solutions. In a rectangular region, by Theorem 2.1.2, $\mu$ is an integrating factor if and only if $(\mu P)_y=(\mu Q)_x$, that is,

$$
Q\frac{\partial\mu}{\partial x}-P\frac{\partial\mu}{\partial y}=\Big(\frac{\partial P}{\partial y}-\frac{\partial Q}{\partial x}\Big)\mu.\tag{2.6}
$$
This is a first-order linear partial differential equation for $\mu$. One can show (by the theory of first integrals in [2.4.14](/2.4.14)) that when $P$ and $Q$ are continuously differentiable and do not vanish simultaneously, integrating factors always exist locally. Solving (2.6), however, generally requires the characteristic curves of Eq. (2.1), which are the solutions of the original equation, so (2.6) usually cannot be used to find an integrating factor. The practical approach is to restrict the form of $\mu$ so that (2.6) reduces to an ordinary differential equation.

### 2.3.2. Integrating Factors Depending on One Variable

**Theorem 2.3.1** Let $P$ and $Q$ be continuously differentiable on a region $D$, with $Q\ne0$. Eq. (2.1) has an integrating factor depending only on $x$ if and only if

$$
G=\frac{1}{Q}\Big(\frac{\partial P}{\partial y}-\frac{\partial Q}{\partial x}\Big)\tag{2.7}
$$
depends only on $x$, that is, $G=G(x)$. In this case $\mu(x)=\mathrm{e}^{\int G(x)\,\mathrm{d}x}$ is an integrating factor.

**Proof** Necessity. If $\mu=\mu(x)$ is an integrating factor, then $\mu_y=0$ and (2.6) becomes $Q\mu'(x)=(P_y-Q_x)\mu$, that is,

$$
\frac{\mu'(x)}{\mu(x)}=\frac{1}{Q}\Big(\frac{\partial P}{\partial y}-\frac{\partial Q}{\partial x}\Big).
$$
The left-hand side depends only on $x$, hence so does the right-hand side.

Sufficiency. If $G=G(x)$, let $\mu=\mathrm{e}^{\int G\,\mathrm{d}x}$. Then $\mu'=G\mu$ and $Q\mu'-P\cdot0=QG\mu=(P_y-Q_x)\mu$, so (2.6) holds. $\square$

Symmetrically, when $P\ne0$, the equation has an integrating factor depending only on $y$ if and only if

$$
H=\frac{1}{P}\Big(\frac{\partial Q}{\partial x}-\frac{\partial P}{\partial y}\Big)
$$
depends only on $y$, in which case $\mu(y)=\mathrm{e}^{\int H(y)\,\mathrm{d}y}$ is an integrating factor.

**Example 2.3.1** Write the first-order linear equation $y'+p(x)y=q(x)$ as $\big(p(x)y-q(x)\big)\,\mathrm{d}x+\mathrm{d}y=0$. Then $P_y-Q_x=p(x)$ and $G=p(x)$ depends only on $x$, so $\mu=\mathrm{e}^{\int p(x)\,\mathrm{d}x}$ is an integrating factor. After multiplication by $\mu$ the equation becomes $\mathrm{d}\Big(y\mathrm{e}^{\int p\,\mathrm{d}x}\Big)=q\mathrm{e}^{\int p\,\mathrm{d}x}\,\mathrm{d}x$, and integrating gives the solution formula of [2.4.3](/2.4.3). Note that $1/\mu=\mathrm{e}^{-\int p\,\mathrm{d}x}$ is precisely a nonzero solution of the corresponding homogeneous equation.

**Example 2.3.2** The separable equation $X(x)Y_1(y)\,\mathrm{d}x+X_1(x)Y(y)\,\mathrm{d}y=0$ has the integrating factor $\dfrac{1}{X_1(x)Y_1(y)}$ (where $X_1Y_1\ne0$); after multiplication it becomes $\dfrac{X}{X_1}\,\mathrm{d}x+\dfrac{Y}{Y_1}\,\mathrm{d}y=0$, and each of the two terms is a total differential.

The same derivation applies to integrating factors of the form $\mu=\mu\big(\omega(x,y)\big)$, where $\omega$ is a given function such as $x+y$, $xy$ or $x^2+y^2$. Substituting into (2.6) gives

$$
\frac{\mu'(\omega)}{\mu(\omega)}=\frac{P_y-Q_x}{Q\omega_x-P\omega_y},
$$
so the equation has an integrating factor of this form if and only if the right-hand side is a function of $\omega$ alone. The choices $\omega=x$ and $\omega=y$ are the two cases of Theorem 2.3.1.

**Example 2.3.3** Solve $(x^2+y^2+x)\,\mathrm{d}x+xy\,\mathrm{d}y=0$. Here $P_y-Q_x=2y-y=y$ and $G=\dfrac{y}{xy}=\dfrac1x$, so $\mu=x$ is an integrating factor, and a general integral is $\dfrac{x^4}{4}+\dfrac{x^3}{3}+\dfrac{x^2y^2}{2}=C$ ([2.2.15 Example 15.4.3](/2.2.15#ex-15.4.3)).

### 2.3.3. The Set of All Integrating Factors

**Theorem 2.3.2** Let $\mu$ be an integrating factor of Eq. (2.1) with $\mu(P\,\mathrm{d}x+Q\,\mathrm{d}y)=\mathrm{d}\Phi$. Then for every continuously differentiable nowhere-zero function $g$, $\mu g(\Phi)$ is also an integrating factor of Eq. (2.1). Conversely, near any point where $\nabla\Phi\ne\boldsymbol{0}$, every integrating factor of Eq. (2.1) can be written in the form $\mu g(\Phi)$.

**Proof** Let $\tilde G$ be an antiderivative of $g$. Then

$$
\mu g(\Phi)(P\,\mathrm{d}x+Q\,\mathrm{d}y)=g(\Phi)\,\mathrm{d}\Phi=\mathrm{d}\big(\tilde G(\Phi)\big),
$$
so $\mu g(\Phi)$ is an integrating factor. Conversely, let $\mu_1$ be another integrating factor with $\mu_1(P\,\mathrm{d}x+Q\,\mathrm{d}y)=\mathrm{d}\Phi_1$. Then $\nabla\Phi_1=\dfrac{\mu_1}{\mu}\nabla\Phi$; the two gradients are parallel, and the Jacobian determinant $\dfrac{\partial(\Phi_1,\Phi)}{\partial(x,y)}\equiv0$. Near a point where $\nabla\Phi\ne\boldsymbol{0}$, assume without loss of generality that $\Phi_y\ne0$, and change variables by $(x,y)\mapsto(x,\Phi)$ (locally invertible by the **inverse function theorem**). Regarding $\Phi_1$ as a function of $x$ and $\Phi$, we get

$$
\frac{\partial\Phi_1}{\partial x}\Big|_{\Phi\ \text{fixed}}=\frac{\partial\Phi_1}{\partial x}-\frac{\partial\Phi_1}{\partial y}\cdot\frac{\Phi_x}{\Phi_y}=\frac{1}{\Phi_y}\cdot\frac{\partial(\Phi_1,\Phi)}{\partial(x,y)}=0,
$$
so locally $\Phi_1=F(\Phi)$. From $\mathrm{d}\Phi_1=F'(\Phi)\,\mathrm{d}\Phi$ we get $\mu_1=\mu F'(\Phi)$, and we may take $g=F'$. $\square$

**Corollary 2.3.1** If $\mu_1$ and $\mu_2$ are two integrating factors of Eq. (2.1) and $\mu_1/\mu_2$ is not constant, then $\dfrac{\mu_1}{\mu_2}=C$ is a general integral of Eq. (2.1).

**Proof** By Theorem 2.3.2, locally $\mu_1/\mu_2=g(\Phi)$. It is constant on each integral curve $\Phi=C$ and is not a constant function, so $\mu_1/\mu_2=C$ gives precisely the family of integral curves. $\square$

For example, both $\dfrac1{y^2}$ and $\dfrac1{xy}$ are integrating factors of $y\,\mathrm{d}x-x\,\mathrm{d}y=0$, and their ratio $\dfrac{x}{y}=C$ is exactly the family of integral curves (lines through the origin). Theorem 2.3.2 also justifies the grouping method below.

### 2.3.4. Finding Integrating Factors by Grouping

Suppose the left-hand side of Eq. (2.1) can be split into two groups,

$$
(P_1\,\mathrm{d}x+Q_1\,\mathrm{d}y)+(P_2\,\mathrm{d}x+Q_2\,\mathrm{d}y)=0,
$$
which have integrating factors $\mu_1$ and $\mu_2$ respectively: $\mu_1(P_1\,\mathrm{d}x+Q_1\,\mathrm{d}y)=\mathrm{d}\Phi_1$ and $\mu_2(P_2\,\mathrm{d}x+Q_2\,\mathrm{d}y)=\mathrm{d}\Phi_2$. By Theorem 2.3.2, every integrating factor of the first group has the form $\mu_1g_1(\Phi_1)$, and every integrating factor of the second group has the form $\mu_2g_2(\Phi_2)$. If $g_1$ and $g_2$ can be chosen so that

$$
\mu_1g_1(\Phi_1)=\mu_2g_2(\Phi_2)=\mu,
$$
then $\mu$ turns both groups into total differentials at once and is therefore an integrating factor of the whole equation. In practice $g_1$ and $g_2$ are usually taken to be power functions, and the exponents on the two sides are compared.

**Example 2.3.4** Solve $(x^3y-2y^2)\,\mathrm{d}x+x^4\,\mathrm{d}y=0$.

Group the terms as $(x^3y\,\mathrm{d}x+x^4\,\mathrm{d}y)-2y^2\,\mathrm{d}x=0$. The first group is $x^3(y\,\mathrm{d}x+x\,\mathrm{d}y)=x^3\,\mathrm{d}(xy)$, with integrating factor $\mu_1=\dfrac1{x^3}$ and $\Phi_1=xy$; the second group $-2y^2\,\mathrm{d}x$ has integrating factor $\mu_2=\dfrac1{y^2}$ and $\Phi_2=x$. We look for $g_1$ and $g_2$ with

$$
\frac{1}{x^3}g_1(xy)=\frac{1}{y^2}g_2(x).
$$
Taking $g_1(u)=u^{-2}$ makes the left-hand side $\dfrac{1}{x^5y^2}$, and taking $g_2(x)=x^{-5}$ makes the right-hand side $\dfrac{1}{x^5y^2}$ as well. Hence $\mu=\dfrac{1}{x^5y^2}$, and after multiplication the equation becomes

$$
\frac{\mathrm{d}(xy)}{(xy)^2}-\frac{2\,\mathrm{d}x}{x^5}=\mathrm{d}\Big(-\frac{1}{xy}+\frac{1}{2x^4}\Big)=0,
$$
with general integral $\dfrac{1}{2x^4}-\dfrac{1}{xy}=C$, that is, $y-2x^3=2Cx^4y$. The integrating factor is undefined on $x=0$ and $y=0$; checking shows that $x=0$ and $y=0$ are also solutions. The solution $y=0$ is not contained in the general integral (no value of $C$ produces it) and must be listed separately.

## Summary

| Topic | Result |
|---|---|
| Exact equation | $\mathrm{d}\Phi=P\,\mathrm{d}x+Q\,\mathrm{d}y$; general integral $\Phi=C$; integral curves are the level curves of $\Phi$ |
| Criterion | On a rectangle or simply connected domain: exact ⇔ $P_y=Q_x$; general integrals (2.4), (2.5); may fail on non-simply-connected regions (Example 2.1.1) |
| Equation for an integrating factor | $Q\mu_x-P\mu_y=(P_y-Q_x)\mu$ |
| $\mu=\mu(x)$ | ⇔ $(P_y-Q_x)/Q$ depends only on $x$; $\mu=\mathrm{e}^{\int G\,\mathrm{d}x}$ |
| $\mu=\mu(y)$ | ⇔ $(Q_x-P_y)/P$ depends only on $y$; $\mu=\mathrm{e}^{\int H\,\mathrm{d}y}$ |
| $\mu=\mu(\omega)$ | ⇔ $(P_y-Q_x)/(Q\omega_x-P\omega_y)$ is a function of $\omega$ alone |
| All integrating factors | $\mu g(\Phi)$; the ratio of two integrating factors $=C$ is a general integral |
| Grouping method | Make $\mu_1g_1(\Phi_1)=\mu_2g_2(\Phi_2)$ |
