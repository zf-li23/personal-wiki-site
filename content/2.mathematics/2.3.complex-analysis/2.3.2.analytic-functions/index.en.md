---
title: Analytic Functions
description: Complex differentiability, the Cauchy–Riemann equations, analytic and entire functions, Wirtinger derivatives, harmonic conjugates and how to recover an analytic function from its real part, and the geometric meaning of the derivative.
---

The derivative of a complex function is defined by the same difference quotient as in one-variable calculus, but the increment $\Delta z$ now approaches $0$ from every direction in the plane. Requiring the same limit from all directions is a strong condition: written in terms of the real and imaginary parts $u,v$, it becomes the pair of Cauchy–Riemann equations, which tie $u$ and $v$ so tightly that each determines the other up to a constant, and both are harmonic functions. Functions that are complex differentiable on an open set are called analytic; they are the subject of the whole course. This chapter defines them, gives the practical tests for analyticity (the Cauchy–Riemann equations and the Wirtinger derivative $\partial f/\partial\bar z$), shows how to reconstruct an analytic function from its real part, and explains the geometric meaning of $f'(z)$ as a local rotation and scaling. The integral theory of [2.3.4](/2.3.4) will then show that analytic functions are infinitely differentiable, and [2.3.5](/2.3.5) that they are sums of power series. The elementary functions $\mathrm{e}^z$, $\log z$, $\sin z$ to which these tests are applied are introduced in [2.3.3](/2.3.3); here our examples use polynomials and rational functions.

## 2.1. The Complex Derivative

**Definition 2.1.1 (Complex Derivative)** Let $f$ be defined on a neighborhood of $z_0$. If the limit

$$
f'(z_0)=\lim_{\Delta z\to0}\frac{f(z_0+\Delta z)-f(z_0)}{\Delta z}
$$
exists (as a finite complex number), $f$ is said to be complex differentiable at $z_0$, and $f'(z_0)$ is called the **complex derivative** of $f$ at $z_0$; we also write $\frac{\mathrm{d}f}{\mathrm{d}z}(z_0)$.

Equivalently, $f$ is complex differentiable at $z_0$ with $f'(z_0)=A$ if and only if

$$
f(z_0+\Delta z)=f(z_0)+A\,\Delta z+o(|\Delta z|)\qquad(\Delta z\to0). \tag{2.1}
$$

The linear part $\Delta z\mapsto A\,\Delta z$ is multiplication by a complex number. This is the essential difference from real differentiability in $\mathbb{R}^2$, where the linear part may be any real $2\times2$ matrix (§2.2). As in the real case, Eq. (2.1) shows that complex differentiability implies continuity, and the usual rules hold with the same proofs:

$$
(f\pm g)'=f'\pm g',\quad (fg)'=f'g+fg',\quad \Big(\frac fg\Big)'=\frac{f'g-fg'}{g^2}\ (g\ne0),\quad \big(f(g(z))\big)'=f'(g(z))\,g'(z).
$$

If $f$ is complex differentiable and injective near $z_0$ with continuous inverse and $f'(z_0)\ne0$, then $(f^{-1})'(w_0)=1/f'(z_0)$ at $w_0=f(z_0)$.

**Example 2.1.1** From $(z+\Delta z)^n-z^n=nz^{n-1}\Delta z+O(|\Delta z|^2)$ we get $(z^n)'=nz^{n-1}$ for $n\ge1$, and by the quotient rule for all $n\in\mathbb{Z}$ ($z\ne0$ when $n<0$). Hence polynomials are complex differentiable everywhere, and a rational function $P/Q$ is complex differentiable wherever $Q\ne0$.

**Example 2.1.2** The function $f(z)=\bar z$ is continuous but complex differentiable nowhere. The difference quotient is $\frac{\overline{\Delta z}}{\Delta z}$; for real $\Delta z$ it equals $1$, for purely imaginary $\Delta z$ it equals $-1$, so the limit does not exist. The same argument shows that $\operatorname{Re}z$, $\operatorname{Im}z$ and $|z|$ are complex differentiable nowhere.

**Example 2.1.3** The function $f(z)=|z|^2=z\bar z$ is complex differentiable only at $0$. At $z_0$,

$$
\frac{|z_0+\Delta z|^2-|z_0|^2}{\Delta z}=\bar z_0+\overline{\Delta z}+z_0\frac{\overline{\Delta z}}{\Delta z}.
$$

As $\Delta z\to0$ the first two terms tend to $\bar z_0$, while the last has a limit only if $z_0=0$, by Example 2.1.2. So $f'(0)=0$ and $f'(z_0)$ does not exist for $z_0\ne0$, although $u=x^2+y^2$ and $v=0$ are as smooth as possible.

## 2.2. The Cauchy–Riemann Equations

### 2.2.1. The Theorem

Let $f=u+\mathrm{i}v$ be complex differentiable at $z_0=x_0+\mathrm{i}y_0$. Letting $\Delta z=\Delta x$ be real in the difference quotient gives $f'(z_0)=u_x+\mathrm{i}v_x$, and letting $\Delta z=\mathrm{i}\Delta y$ be purely imaginary gives $f'(z_0)=\frac{u_y+\mathrm{i}v_y}{\mathrm{i}}=v_y-\mathrm{i}u_y$ (all partial derivatives at $(x_0,y_0)$). Comparing the two expressions yields a necessary condition, which together with real differentiability is also sufficient.

**Theorem 2.2.1 (Cauchy–Riemann Equations)** Let $f=u+\mathrm{i}v$ be defined on a neighborhood of $z_0=x_0+\mathrm{i}y_0$. Then $f$ is complex differentiable at $z_0$ if and only if

1. $u$ and $v$ are differentiable at $(x_0,y_0)$ as functions of two real variables (they have a **total differential** there), and
2. they satisfy the Cauchy–Riemann equations at $(x_0,y_0)$:

$$
\frac{\partial u}{\partial x}=\frac{\partial v}{\partial y},\qquad \frac{\partial u}{\partial y}=-\frac{\partial v}{\partial x}. \tag{2.2}
$$

In that case

$$
f'(z_0)=u_x+\mathrm{i}v_x=v_y-\mathrm{i}u_y=u_x-\mathrm{i}u_y=v_y+\mathrm{i}v_x. \tag{2.3}
$$

**Proof** Write $\Delta z=\Delta x+\mathrm{i}\Delta y$ and $f'(z_0)=a+\mathrm{i}b$.

Necessity. By Eq. (2.1), $\Delta f=(a+\mathrm{i}b)(\Delta x+\mathrm{i}\Delta y)+o(|\Delta z|)$. Taking real and imaginary parts,

$$
\Delta u=a\,\Delta x-b\,\Delta y+o(|\Delta z|),\qquad \Delta v=b\,\Delta x+a\,\Delta y+o(|\Delta z|).
$$

So $u$ and $v$ are differentiable at $(x_0,y_0)$ with $u_x=a$, $u_y=-b$, $v_x=b$, $v_y=a$, which gives Eq. (2.2) and Eq. (2.3).

Sufficiency. Let $a=u_x=v_y$ and $b=v_x=-u_y$ at $(x_0,y_0)$. Differentiability of $u$ and $v$ gives

$$
\Delta u+\mathrm{i}\Delta v=(u_x\Delta x+u_y\Delta y)+\mathrm{i}(v_x\Delta x+v_y\Delta y)+o(|\Delta z|)=(a+\mathrm{i}b)(\Delta x+\mathrm{i}\Delta y)+o(|\Delta z|),
$$

which is Eq. (2.1) with $A=a+\mathrm{i}b$. $\square$

Since continuous partial derivatives imply differentiability ([2.2.10](/2.2.10)), we obtain the test used in practice.

**Corollary 2.2.1** If $u$ and $v$ have continuous first-order **partial derivatives** on an open set $D$ and satisfy the Cauchy–Riemann equations there, then $f=u+\mathrm{i}v$ is complex differentiable at every point of $D$.

The Cauchy–Riemann equations without differentiability of $u,v$ do not suffice: $f(z)=\sqrt{|xy|}$ satisfies Eq. (2.2) at $0$ (all four partial derivatives vanish there) but is not complex differentiable at $0$, since along $z=t(1+\mathrm{i})$ the difference quotient is $\frac{|t|}{t(1+\mathrm{i})}$, which has no limit.

### 2.2.2. Matrix and Polar Forms

The Cauchy–Riemann equations say that the **Jacobian matrix** of the map $(x,y)\mapsto(u,v)$ has the form

$$
\begin{bmatrix}u_x&u_y\\v_x&v_y\end{bmatrix}=\begin{bmatrix}a&-b\\b&a\end{bmatrix},\qquad a+\mathrm{i}b=f'(z_0),
$$

which is exactly the real matrix representing multiplication by the complex number $a+\mathrm{i}b$ ([Proposition 9.1.1](/2.1.9#prop-9.1.1)). A real-differentiable map is complex differentiable precisely when its linear approximation is a rotation followed by a scaling. In particular the **Jacobian determinant** is $u_xv_y-u_yv_x=a^2+b^2=|f'(z_0)|^2\ge0$, so analytic maps preserve orientation.

In polar coordinates $z=r\mathrm{e}^{\mathrm{i}\theta}$ ($r>0$), the chain rule $u_r=u_x\cos\theta+u_y\sin\theta$, $u_\theta=-u_xr\sin\theta+u_yr\cos\theta$ (and similarly for $v$) turns Eq. (2.2) into

$$
\frac{\partial u}{\partial r}=\frac1r\frac{\partial v}{\partial\theta},\qquad \frac{\partial v}{\partial r}=-\frac1r\frac{\partial u}{\partial\theta},\qquad f'(z)=\mathrm{e}^{-\mathrm{i}\theta}\Big(\frac{\partial u}{\partial r}+\mathrm{i}\frac{\partial v}{\partial r}\Big). \tag{2.4}
$$

The last formula holds because differentiating along the ray, $\frac{\partial f}{\partial r}=f'(z)\frac{\partial z}{\partial r}=f'(z)\mathrm{e}^{\mathrm{i}\theta}$. The polar form is convenient for functions defined through modulus and argument, such as $\log z$ and $z^\alpha$ in [2.3.3](/2.3.3).

**Example 2.2.1** Where is $f(z)=x^2+\mathrm{i}y^2$ complex differentiable? Here $u_x=2x$, $v_y=2y$, $u_y=0$, $v_x=0$, all continuous. The second equation always holds and the first holds exactly when $x=y$. So $f$ is complex differentiable exactly on the line $y=x$, with $f'(x+\mathrm{i}x)=u_x+\mathrm{i}v_x=2x$.

**Example 2.2.2** For $f(z)=z^3$, $u=x^3-3xy^2$ and $v=3x^2y-y^3$, and indeed $u_x=3x^2-3y^2=v_y$ and $u_y=-6xy=-v_x$; Eq. (2.3) gives $f'(z)=u_x+\mathrm{i}v_x=3(x^2-y^2)+6xy\,\mathrm{i}=3z^2$. For $f(z)=\frac1z$ in polar form, $u=\frac{\cos\theta}{r}$ and $v=-\frac{\sin\theta}{r}$; then $u_r=-\frac{\cos\theta}{r^2}=\frac1rv_\theta$, $v_r=\frac{\sin\theta}{r^2}=-\frac1ru_\theta$, and $f'(z)=\mathrm{e}^{-\mathrm{i}\theta}\cdot\frac{-\cos\theta+\mathrm{i}\sin\theta}{r^2}=-\frac{\mathrm{e}^{-2\mathrm{i}\theta}}{r^2}=-\frac1{z^2}$.

## 2.3. Analytic Functions

Complex differentiability at a single point, or along a line as in Example 2.2.1, carries little information. The useful notion asks for differentiability on an open set.

**Definition 2.3.1 (Analytic Function)** A function $f$ is analytic at $z_0$ if it is complex differentiable at every point of some neighborhood of $z_0$. It is analytic on an open set $D$ if it is analytic at every point of $D$, i.e. complex differentiable at every point of $D$; it is then called an **analytic function** (or **holomorphic function**) on $D$. A function analytic on all of $\mathbb{C}$ is called an **entire function**. A function is said to be analytic on a closed set $E$ if it is analytic on some open set containing $E$.

**Definition 2.3.2 (Singular Point)** If $f$ is not analytic at $z_0$, but every neighborhood of $z_0$ contains points at which $f$ is analytic, then $z_0$ is called a **singular point** (or singularity) of $f$.

For example, polynomials are entire; a rational function $P/Q$ in lowest terms is analytic on $\mathbb{C}$ except at the zeros of $Q$, which are its singular points; $\frac1z$ is analytic on $\mathbb{C}\setminus\{0\}$ with singular point $0$. The functions $x^2+\mathrm{i}y^2$ (Example 2.2.1) and $|z|^2$ (Example 2.1.3) are analytic nowhere, even though they are complex differentiable at some points, and they have no singular points in this sense. Singular points around which $f$ is analytic in a whole punctured disc are called isolated; their classification into removable singularities, poles and essential singularities is the subject of [2.3.6](/2.3.6).

**Theorem 2.3.1** Sums, differences, products and compositions of analytic functions are analytic, and so is a quotient $f/g$ wherever $g\ne0$.

This follows at once from the differentiation rules in §2.1. Two consequences of the Cauchy–Riemann equations show how rigid analytic functions are.

**Theorem 2.3.2** Let $f=u+\mathrm{i}v$ be analytic on a **region** $D$. If $f'\equiv0$ on $D$, then $f$ is constant on $D$.

**Proof** By Eq. (2.3), $u_x=u_y=v_x=v_y=0$ on $D$. By the **mean value theorem** applied along segments parallel to the axes, $u$ and $v$ are constant on every disc contained in $D$, hence locally constant. A locally constant function on a connected open set is constant: the set where $u=u(z_0)$ is open and so is its complement in $D$, and $D$ cannot be split into two disjoint nonempty open sets. $\square$

**Corollary 2.3.1** Let $f=u+\mathrm{i}v$ be analytic on a region $D$. Each of the following implies that $f$ is constant on $D$:

1. $u$ is constant (or $v$ is constant);
2. $|f|$ is constant;
3. $\bar f$ is also analytic on $D$.

**Proof** 1. If $u$ is constant, $u_x=u_y=0$, so $f'=u_x-\mathrm{i}u_y=0$ and Theorem 2.3.2 applies; the case of $v$ is the same with $f'=v_y+\mathrm{i}v_x$.

2. If $u^2+v^2=c$, then $c=0$ gives $f\equiv0$. Otherwise, differentiating, $uu_x+vv_x=0$ and $uu_y+vv_y=0$; substituting $v_x=-u_y$ and $v_y=u_x$ gives the linear system $uu_x-vu_y=0$, $vu_x+uu_y=0$, whose determinant is $u^2+v^2=c\ne0$. Hence $u_x=u_y=0$ and $f$ is constant by 1.

3. Then $f+\bar f=2u$ is analytic and real-valued, so its imaginary part is constant, and by 1 it is constant; thus $u$ is constant and so is $f$. $\square$

## 2.4. Wirtinger Derivatives

### 2.4.1. Definition and the Analyticity Test

A function $f(x,y)$ of the real variables $x,y$ can be regarded as a function of $z$ and $\bar z$ through $x=\frac{z+\bar z}{2}$ and $y=\frac{z-\bar z}{2\mathrm{i}}$. Pretending that $z$ and $\bar z$ are independent variables and applying the chain rule formally, $\frac{\partial}{\partial z}=\frac{\partial x}{\partial z}\frac{\partial}{\partial x}+\frac{\partial y}{\partial z}\frac{\partial}{\partial y}=\frac12\frac{\partial}{\partial x}+\frac1{2\mathrm{i}}\frac{\partial}{\partial y}$, and similarly for $\bar z$. We take the result as a definition.

**Definition 2.4.1 (Wirtinger Derivatives)** For a function $f=u+\mathrm{i}v$ whose real and imaginary parts have first-order partial derivatives, the **Wirtinger derivatives** are

$$
\frac{\partial f}{\partial z}=\frac12\Big(\frac{\partial f}{\partial x}-\mathrm{i}\frac{\partial f}{\partial y}\Big),\qquad \frac{\partial f}{\partial\bar z}=\frac12\Big(\frac{\partial f}{\partial x}+\mathrm{i}\frac{\partial f}{\partial y}\Big),
$$

where $\frac{\partial f}{\partial x}=u_x+\mathrm{i}v_x$ and $\frac{\partial f}{\partial y}=u_y+\mathrm{i}v_y$. We also write $f_z$ and $f_{\bar z}$.

Expanding,

$$
\frac{\partial f}{\partial\bar z}=\frac12\big[(u_x-v_y)+\mathrm{i}(v_x+u_y)\big],\qquad \frac{\partial f}{\partial z}=\frac12\big[(u_x+v_y)+\mathrm{i}(v_x-u_y)\big]. \tag{2.5}
$$

So $\frac{\partial f}{\partial\bar z}=0$ is the pair of Cauchy–Riemann equations written as one complex equation, and when it holds, $\frac{\partial f}{\partial z}=u_x+\mathrm{i}v_x=f'$. Theorem 2.2.1 thus becomes:

**Theorem 2.4.1** Let $u,v$ be differentiable at $z_0$. Then $f=u+\mathrm{i}v$ is complex differentiable at $z_0$ if and only if $\dfrac{\partial f}{\partial\bar z}(z_0)=0$, and then $f'(z_0)=\dfrac{\partial f}{\partial z}(z_0)$. A function with continuous first-order partial derivatives on an open set $D$ is analytic on $D$ if and only if $\dfrac{\partial f}{\partial\bar z}\equiv0$ on $D$.

The slogan is that analytic functions are the functions that depend on $z$ alone and not on $\bar z$. In real terms the total differential is

$$
\mathrm{d}f=f_x\,\mathrm{d}x+f_y\,\mathrm{d}y=\frac{\partial f}{\partial z}\,\mathrm{d}z+\frac{\partial f}{\partial\bar z}\,\mathrm{d}\bar z,
$$

as one checks by substituting $\mathrm{d}x=\frac{\mathrm{d}z+\mathrm{d}\bar z}{2}$ and $\mathrm{d}y=\frac{\mathrm{d}z-\mathrm{d}\bar z}{2\mathrm{i}}$. The derivative $f'$ is the coefficient of $\mathrm{d}z$; the coefficient of $\mathrm{d}\bar z$ measures the failure of analyticity.

### 2.4.2. Computing with Wirtinger Derivatives

The operators $\partial/\partial z$ and $\partial/\partial\bar z$ are linear combinations of $\partial/\partial x$ and $\partial/\partial y$, so they are linear and satisfy the product and quotient rules. Moreover

$$
\frac{\partial z}{\partial z}=1,\quad \frac{\partial\bar z}{\partial z}=0,\quad \frac{\partial z}{\partial\bar z}=0,\quad \frac{\partial\bar z}{\partial\bar z}=1,\qquad \overline{\Big(\frac{\partial f}{\partial z}\Big)}=\frac{\partial\bar f}{\partial\bar z}, \tag{2.6}
$$

and for an analytic function $g$ the chain rule takes the form

$$
\frac{\partial}{\partial z}g(h)=g'(h)\frac{\partial h}{\partial z},\qquad \frac{\partial}{\partial\bar z}g(h)=g'(h)\frac{\partial h}{\partial\bar z},
$$

where $h$ is any function with continuous partial derivatives. (Both follow from $\mathrm{d}\,g(h)=g'(h)\,\mathrm{d}h$ and the expression for $\mathrm{d}h$ above.) In practice, then: write $f$ as an expression in $z$ and $\bar z$, using $|z|^2=z\bar z$, $\operatorname{Re}z=\frac{z+\bar z}2$ and $\operatorname{Im}z=\frac{z-\bar z}{2\mathrm{i}}$, and differentiate as if $z$ and $\bar z$ were independent variables. Finally, the **Laplace operator** factors as

$$
\Delta=\frac{\partial^2}{\partial x^2}+\frac{\partial^2}{\partial y^2}=4\frac{\partial^2}{\partial z\,\partial\bar z}, \tag{2.7}
$$

since $\big(\partial_x-\mathrm{i}\partial_y\big)\big(\partial_x+\mathrm{i}\partial_y\big)=\partial_x^2+\partial_y^2$ for functions with continuous second-order partial derivatives.

**Example 2.4.1** Let $f(z)=z^2+3z\bar z^2$. Then $\frac{\partial f}{\partial\bar z}=6z\bar z=6|z|^2$, which vanishes only at $z=0$. So $f$ is complex differentiable only at $0$, with $f'(0)=\frac{\partial f}{\partial z}(0)=(2z+3\bar z^2)\big|_{z=0}=0$, and $f$ is analytic nowhere. For $f=x^2+\mathrm{i}y^2$ of Example 2.2.1, Eq. (2.5) gives $\frac{\partial f}{\partial\bar z}=\frac12(2x+\mathrm{i}\cdot\mathrm{i}\,2y)=x-y$, recovering the line $y=x$.

**Example 2.4.2** Let $f(z)=\sin(z)\,\mathrm{e}^{|z|^2}$, with the entire function $\sin z$ of [2.3.3](/2.3.3) (its derivative is $\cos z$ and $\sin(\mathrm{i}t)=\mathrm{i}\sinh t$). Compute $\frac{\partial f}{\partial\bar z}$ and $\frac{\partial f}{\partial z}$ at $z=\mathrm{i}\pi$. Writing $\mathrm{e}^{|z|^2}=\mathrm{e}^{z\bar z}$, the product and chain rules give

$$
\frac{\partial f}{\partial\bar z}=\sin z\cdot z\,\mathrm{e}^{z\bar z},\qquad \frac{\partial f}{\partial z}=\cos z\cdot\mathrm{e}^{z\bar z}+\sin z\cdot\bar z\,\mathrm{e}^{z\bar z}.
$$

At $z=\mathrm{i}\pi$ we have $z\bar z=\pi^2$, $\sin(\mathrm{i}\pi)=\mathrm{i}\sinh\pi$ and $\cos(\mathrm{i}\pi)=\cosh\pi$, so

$$
\frac{\partial f}{\partial\bar z}(\mathrm{i}\pi)=\mathrm{i}\sinh\pi\cdot\mathrm{i}\pi\,\mathrm{e}^{\pi^2}=-\pi\sinh\pi\,\mathrm{e}^{\pi^2},\qquad \frac{\partial f}{\partial z}(\mathrm{i}\pi)=\big(\cosh\pi+\pi\sinh\pi\big)\mathrm{e}^{\pi^2}.
$$

The computation in terms of $x,y$ and Eq. (2.5) would be considerably longer.

## 2.5. Harmonic Functions and Harmonic Conjugates

### 2.5.1. Real and Imaginary Parts Are Harmonic

**Theorem 2.5.1** If $f=u+\mathrm{i}v$ is analytic on an open set $D$, then $u$ and $v$ are **harmonic functions** on $D$: $\Delta u=\Delta v=0$.

**Proof** We use the fact, proved in [2.3.4](/2.3.4) (Theorem 4.4.2), that the derivative of an analytic function is again analytic; in particular $u$ and $v$ have continuous partial derivatives of all orders. Differentiating $u_x=v_y$ with respect to $x$ and $u_y=-v_x$ with respect to $y$ and adding gives $u_{xx}+u_{yy}=v_{yx}-v_{xy}=0$, by equality of mixed partial derivatives. Similarly $\Delta v=-u_{yx}+u_{xy}=0$. In the notation of Eq. (2.7): $\Delta f=4\frac{\partial}{\partial z}\frac{\partial f}{\partial\bar z}=0$, and taking real and imaginary parts gives the claim. $\square$

Harmonic functions describe steady-state temperatures, electrostatic potentials in charge-free regions, and velocity potentials of ideal fluid flow ([2.2.14](/2.2.14)); the theorem makes analytic functions a source of explicit solutions of the Laplace equation, used systematically with conformal mappings in [2.3.8](/2.3.8) and [2.5.8](/2.5.8).

**Definition 2.5.1 (Harmonic Conjugate)** Let $u$ be harmonic on an open set $D$. A harmonic function $v$ on $D$ such that $u+\mathrm{i}v$ is analytic on $D$ is called a **harmonic conjugate** of $u$.

The relation is not symmetric: if $v$ is a harmonic conjugate of $u$, then $-u$ (not $u$) is a harmonic conjugate of $v$, because $v-\mathrm{i}u=-\mathrm{i}(u+\mathrm{i}v)$ is analytic. By Corollary 2.3.1, a harmonic conjugate on a region is unique up to an additive real constant.

### 2.5.2. Existence on Simply Connected Regions

**Theorem 2.5.2** Let $u$ be harmonic on a simply connected region $D$ and $z_0=(x_0,y_0)\in D$. Then

$$
v(x,y)=\int_{(x_0,y_0)}^{(x,y)}-u_y\,\mathrm{d}x+u_x\,\mathrm{d}y+C \tag{2.8}
$$

is well defined (independent of the path in $D$), and for every real constant $C$ it is a harmonic conjugate of $u$; every harmonic conjugate is of this form.

**Proof** The Cauchy–Riemann equations ask for $v_x=-u_y$ and $v_y=u_x$, i.e. that $-u_y\,\mathrm{d}x+u_x\,\mathrm{d}y$ be the total differential of $v$. The integrability condition $\frac{\partial(-u_y)}{\partial y}=\frac{\partial u_x}{\partial x}$ is exactly $\Delta u=0$. On a simply connected region, a **line integral of a vector field** with continuously differentiable components satisfying this condition is independent of the path, and it defines a potential function with the prescribed partial derivatives (by **Green's theorem**, [2.2.13](/2.2.13)). So $v$ is well defined with $v_x=-u_y$, $v_y=u_x$; these are continuous, so $u+\mathrm{i}v$ is analytic by Corollary 2.2.1, and $v$ is harmonic by Theorem 2.5.1. Uniqueness up to constants was noted above. $\square$

Simple connectivity cannot be dropped. The function $u=\ln|z|=\frac12\ln(x^2+y^2)$ is harmonic on $\mathbb{C}\setminus\{0\}$, and Eq. (2.8) produces $v=\arg z$, which changes by $2\pi$ around the origin: $u$ has harmonic conjugates on every simply connected subregion (such as the slit plane, where $v=\operatorname{Arg}z$) but none on the whole punctured plane. This is the origin of the multivalued logarithm $\ln|z|+\mathrm{i}\arg z$ in [2.3.3](/2.3.3).

### 2.5.3. Finding an Analytic Function from Its Real Part

A standard problem: given a harmonic $u$ (or $v$), find the analytic $f$ with $\operatorname{Re}f=u$, possibly with a normalization such as a prescribed value $f(z_0)$. Three methods are common.

1. Partial integration. From $v_y=u_x$, integrate in $y$: $v=\int u_x\,\mathrm{d}y+\varphi(x)$; then determine $\varphi$ from $v_x=-u_y$. (This is Eq. (2.8) along a path made of segments parallel to the axes.)
2. Line integral, Eq. (2.8), along any convenient path.
3. Through the derivative. By Eq. (2.3), $f'(z)=u_x-\mathrm{i}u_y$ (or $f'=v_y+\mathrm{i}v_x$ when $v$ is given). If $u$ is built from polynomials and elementary functions, put $x=z$, $y=0$ in the right-hand side: $f'(z)=u_x(z,0)-\mathrm{i}u_y(z,0)$. Then integrate in $z$. The substitution is justified because both sides are analytic and agree on the real axis, and two analytic functions that agree on a segment agree on the whole region (the identity theorem, [2.3.5](/2.3.5)).

**Example 2.5.1** Find $a\in\mathbb{R}$ such that $u=x^3+axy^2+x^2-y^2$ is harmonic, and find the analytic $f$ with $\operatorname{Re}f=u$ and $f(0)=0$.

Since $\Delta u=6x+2ax+2-2=(6+2a)x$, we need $a=-3$. By method 1, $u_x=3x^2-3y^2+2x$, so $v=\int(3x^2-3y^2+2x)\,\mathrm{d}y=3x^2y-y^3+2xy+\varphi(x)$. Then $v_x=6xy+2y+\varphi'(x)$ must equal $-u_y=6xy+2y$, so $\varphi$ is a constant $c$. Hence

$$
f=u+\mathrm{i}v=(x^3-3xy^2+x^2-y^2)+\mathrm{i}(3x^2y-y^3+2xy)+\mathrm{i}c=z^3+z^2+\mathrm{i}c,
$$

and $f(0)=0$ forces $c=0$, so $f(z)=z^3+z^2$.

**Example 2.5.2** Find the analytic $f$ on $\mathbb{C}\setminus\{0\}$ with $\operatorname{Im}f=v=2xy-\dfrac{y}{x^2+y^2}$ and $f(1)=3$.

By method 3 with $f'=v_y+\mathrm{i}v_x$: we compute $v_y=2x-\frac{x^2-y^2}{(x^2+y^2)^2}$ and $v_x=2y+\frac{2xy}{(x^2+y^2)^2}$, so $v_y(z,0)=2z-\frac1{z^2}$ and $v_x(z,0)=0$. Thus $f'(z)=2z-\frac1{z^2}$ and $f(z)=z^2+\frac1z+c$ with $c$ real (since $\operatorname{Im}f$ is prescribed). From $f(1)=2+c=3$ we get $f(z)=z^2+\frac1z+1$. Check: $\operatorname{Im}z^2=2xy$ and $\operatorname{Im}\frac1z=-\frac{y}{x^2+y^2}$.

Problems in which $u$ contains exponentials or trigonometric functions are solved the same way once $\mathrm{e}^z$ and $\sin z$ are available; see Example 3.1.2 in [2.3.3](/2.3.3).

## 2.6. Geometric Meaning of the Derivative

Let $f$ be analytic at $z_0$ with $f'(z_0)=\rho\,\mathrm{e}^{\mathrm{i}\alpha}\ne0$, and let $\gamma$ be a smooth curve with $\gamma(t_0)=z_0$. The image curve $\Gamma=f\circ\gamma$ satisfies, by the chain rule,

$$
\Gamma'(t_0)=f'(z_0)\,\gamma'(t_0).
$$

So the tangent direction of $\Gamma$ at $f(z_0)$ is that of $\gamma$ rotated by $\alpha=\operatorname{Arg}f'(z_0)$, and short lengths near $z_0$ are multiplied by approximately $\rho=|f'(z_0)|$, the same factor in every direction. Two consequences:

- the rotation angle and the scale factor do not depend on the curve, so the angle between any two curves through $z_0$ (the angle between their tangents) is preserved in size and orientation;
- infinitesimally small circles go to infinitesimally small circles, and areas are scaled by the Jacobian determinant $|f'(z_0)|^2$.

A map with these properties is called conformal at $z_0$; conformal mappings are studied in [2.3.8](/2.3.8). Where $f'(z_0)=0$ the picture changes: if $f(z)-f(z_0)$ behaves like $c(z-z_0)^k$ with $k\ge2$, angles at $z_0$ are multiplied by $k$.

![The map w = z^2 applied to a grid in the first quadrant. The vertical lines x = c and horizontal lines y = c become two families of parabolas that still cross at right angles, and a small square becomes a small curvilinear square; at z = 0, where the derivative vanishes, the right angle between the positive axes is doubled into a straight angle.](./plots/square-map.py)

**Example 2.6.1** For $w=z^2$, the vertical line $x=c$ is mapped to $u=c^2-y^2$, $v=2cy$, i.e. the parabola $u=c^2-\frac{v^2}{4c^2}$, opening to the left; the horizontal line $y=c$ goes to $u=x^2-c^2$, $v=2cx$, i.e. $u=\frac{v^2}{4c^2}-c^2$, opening to the right. At an intersection point $z_0=c_1+\mathrm{i}c_2\ne0$ the two lines are orthogonal and $f'(z_0)=2z_0\ne0$, so the two parabolas are orthogonal as well. At $z_0=0$, $f'(0)=0$ and the angle $\frac\pi2$ between the positive real and imaginary axes becomes the angle $\pi$ between the positive and negative real axes.

The same computation, read backwards, explains a classical fact about level curves.

**Theorem 2.6.1** Let $f=u+\mathrm{i}v$ be analytic with $f'(z_0)\ne0$. Then the level curves $u=u(z_0)$ and $v=v(z_0)$ intersect orthogonally at $z_0$.

**Proof** The gradients are $\nabla u=(u_x,u_y)$ and $\nabla v=(v_x,v_y)=(-u_y,u_x)$ by the Cauchy–Riemann equations, so $\nabla u\cdot\nabla v=0$. Both are nonzero since $|\nabla u|=|\nabla v|=|f'(z_0)|$, and they are normal to the respective **level curves**. $\square$

![Level curves of u = Re(1/z) (circles tangent to the imaginary axis at 0) and v = Im(1/z) (circles tangent to the real axis at 0). Every blue circle meets every red circle at right angles; all of them pass through the singular point z = 0.](./plots/level-curves.py)

In two-dimensional ideal flow, if $u$ is the velocity potential then the level curves of its harmonic conjugate $v$ are the streamlines; Theorem 2.6.1 says that streamlines cross equipotential lines at right angles. The function $f=u+\mathrm{i}v$ is the complex potential of the flow ([2.3.8](/2.3.8)).

## Summary

| Notion | Test or formula |
|---|---|
| complex differentiable at $z_0$ | $u,v$ differentiable and $u_x=v_y$, $u_y=-v_x$; equivalently $\partial f/\partial\bar z=0$ |
| derivative | $f'=u_x+\mathrm{i}v_x=v_y-\mathrm{i}u_y=\partial f/\partial z$; polar: $f'=\mathrm{e}^{-\mathrm{i}\theta}(u_r+\mathrm{i}v_r)$ |
| analytic on $D$ | complex differentiable at every point of the open set $D$ |
| rigidity | on a region: $f'=0$, or $\operatorname{Re}f$, or $\lvert f\rvert$ constant, or $\bar f$ analytic $\Rightarrow$ $f$ constant |
| harmonicity | $\operatorname{Re}f$, $\operatorname{Im}f$ harmonic; $\Delta=4\,\partial^2/\partial z\,\partial\bar z$ |
| reconstruction | $f'(z)=u_x(z,0)-\mathrm{i}u_y(z,0)$, or Eq. (2.8); unique up to an imaginary constant |
| geometry | $f'(z_0)\ne0$: rotation by $\operatorname{Arg}f'(z_0)$, scaling by $\lvert f'(z_0)\rvert$, angles preserved |
