---
title: Sturm Theory and Boundary Value Problems
source_hash: f7d7d22e73a8
---

A second-order linear equation with variable coefficients $y''+a_1(x)y'+a_2(x)y=0$ generally cannot be solved, yet many properties of its solutions can still be read off directly from the equation. The protagonists of this chapter are the zeros of solutions: where they are, how dense they are, and how the zeros of two solutions are arranged. Sturm's idea is to compare the equation under study with an equation whose solutions are known (often one with constant coefficients): the equation with the larger coefficient oscillates faster and has denser zeros. This "qualitative theory without solving" serves two purposes. One is to decide whether solutions oscillate and to estimate the spacing of their zeros. The other is the study of boundary value problems, eigenvalue problems in which conditions are imposed at both ends of an interval and an unknown parameter $\lambda$ is sought at the same time. The latter leads to Sturm–Liouville theory: the eigenvalues are real, countable and tend to infinity, and the eigenfunctions are mutually orthogonal and can be used to expand functions; trigonometric series ([2.2.9](/2.2.9#sec-9.3)) are just a special case. The method of separation of variables for partial differential equations ([2.5](/2.5)) rests on exactly this theory.

This chapter uses the general theory of second-order linear equations ([2.4.9](/2.4.9), [2.2.16](/2.2.16#sec-16.1)): the **existence and uniqueness theorem**, the **Wronskian** and **Liouville's formula**. Throughout, the coefficients are assumed continuous on the interval in question, and a "nontrivial solution" means a solution that is not identically zero.

## 12.1. Normal Forms of Second-Order Linear Equations

### 12.1.1. Isolation of Zeros

**Lemma 12.1.1** Let $a_1,a_2\in C(I)$ and let $y(x)$ be a nontrivial solution on the interval $I$ of the equation

$$
y''+a_1(x)y'+a_2(x)y=0.\tag{12.1}
$$
Then the zeros of $y$ are isolated: they have no accumulation point in $I$. In particular, $y$ has only finitely many zeros on any bounded closed subinterval.

**Proof** Suppose, to the contrary, that there are zeros $x_k\to x^*\in I$ with $x_k\ne x^*$. By continuity $y(x^*)=\lim y(x_k)=0$. By the mean value theorem there is $\xi_k$ between $x_k$ and $x^*$ with

$$
y'(\xi_k)=\frac{y(x_k)-y(x^*)}{x_k-x^*}=0,
$$
and letting $k\to\infty$ gives $y'(x^*)=0$. Then $y$ and the zero solution satisfy the same initial conditions $y(x^*)=y'(x^*)=0$, so $y\equiv0$ by uniqueness, a contradiction. $\square$

The same argument shows that all zeros of a nontrivial solution are simple: $y(x_0)=0$ implies $y'(x_0)\ne0$, so a solution always changes sign at a zero.

### 12.1.2. Normal Form and Self-Adjoint Form

Eq. (12.1) has two commonly used equivalent forms, each of which eliminates one coefficient.

**Lemma 12.1.2** Let $a_1\in C^1(I)$, $a_2\in C(I)$ and $x_0\in I$. The substitution

$$
y=z\exp\Big(-\frac12\int_{x_0}^x a_1(t)\,\mathrm{d}t\Big)
$$
transforms Eq. (12.1) into the normal form without a first-derivative term,

$$
z''+Q(x)z=0,\qquad Q(x)=a_2(x)-\frac12a_1'(x)-\frac14a_1^2(x).\tag{12.2}
$$

This is verified by direct substitution. Since the factor in the substitution is always positive, $y$ and $z$ have exactly the same zeros, so for the study of zeros it suffices to consider the normal form (12.2).

**Definition 12.1.1 (Self-Adjoint Form)** Let $p\in C^1(I)$ with $p>0$, and $q\in C(I)$. An equation of the form

$$
\big(p(x)y'\big)'+q(x)y=0\tag{12.3}
$$
is called the **self-adjoint form** (or Sturm–Liouville form) of a second-order linear equation.

Multiplying Eq. (12.1) by $p(x)=\exp\big(\int_{x_0}^x a_1(t)\,\mathrm{d}t\big)$, we have $p'=a_1p$, so the left-hand side becomes $(py')'+a_2py$. Hence every equation (12.1) (with $a_1$ merely continuous) can be put into self-adjoint form, with $q=a_2p$. The meaning of "self-adjoint" is explained in §12.5: under suitable boundary conditions, the operator $y\mapsto-(py')'+qy$ is a **self-adjoint operator**.

For the self-adjoint form, Liouville's formula becomes a simple conservation law: if $u,v$ are both solutions of Eq. (12.3), then

$$
\frac{\mathrm{d}}{\mathrm{d}x}\Big[p(uv'-u'v)\Big]=u(pv')'-v(pu')'=u(-qv)-v(-qu)=0,
$$
that is, $p(x)W(x)$ is constant, where $W=uv'-u'v$.

## 12.2. Sturm Comparison Theorems

### 12.2.1. The Separation Theorem

**Theorem 12.2.1 (Sturm Separation Theorem)** Let $u,v$ be two linearly independent solutions of Eq. (12.1). Then $u$ and $v$ have no common zeros, and their zeros interlace: between any two consecutive zeros of $u$ there is exactly one zero of $v$, and vice versa.

**Proof** By Liouville's formula, $W(x)=u v'-u'v=W(x_0)\exp\big(-\int_{x_0}^x a_1\big)$ never vanishes; we may assume $W>0$. If $u,v$ had a common zero $x_1$, then $W(x_1)=0$, a contradiction.

Let $x_1<x_2$ be consecutive zeros of $u$, and assume $u>0$ on $(x_1,x_2)$. Since the zeros are simple, $u'(x_1)>0$ and $u'(x_2)<0$. At $x_1,x_2$ we have $W=-u'v$, so

$$
W(x_1)=-u'(x_1)v(x_1)>0,\qquad W(x_2)=-u'(x_2)v(x_2)>0,
$$
which gives $v(x_1)<0<v(x_2)$; by the intermediate value theorem $v$ has at least one zero in $(x_1,x_2)$. If $v$ had two zeros $\zeta<\eta$ in $(x_1,x_2)$, exchanging the roles of $u$ and $v$ would give a zero of $u$ in $(\zeta,\eta)$, contradicting the assumption that $x_1,x_2$ are consecutive. $\square$

For example, the zeros of the solutions $\sin x$ and $\cos x$ of $y''+y=0$ interlace. The separation theorem says that all nontrivial solutions of the same equation "oscillate equally fast": on any interval their numbers of zeros differ by at most 1.

### 12.2.2. The Comparison Theorem

Consider two equations in normal form,

$$
z''+Q(x)z=0,\tag{12.4}
$$

$$
y''+P(x)y=0,\tag{12.5}
$$
where $P,Q\in C[x_0,+\infty)$.

**Theorem 12.2.2 (Sturm Comparison Theorem)** Suppose $Q(x)\le P(x)$ for $x\ge x_0$. If $a<b$ are consecutive zeros of some nontrivial solution $z$ of Eq. (12.4), then every nontrivial solution $y$ of Eq. (12.5) has at least one zero in the closed interval $[a,b]$.

**Proof** Multiplying Eq. (12.4) by $y$ and Eq. (12.5) by $z$ and subtracting gives $yz''-y''z=(P-Q)yz$, that is,

$$
\frac{\mathrm{d}}{\mathrm{d}x}(yz'-y'z)=(P-Q)yz.
$$
Integrating from $a$ to $b$ and using $z(a)=z(b)=0$:

$$
y(b)z'(b)-y(a)z'(a)=\int_a^b\big[P(x)-Q(x)\big]y(x)z(x)\,\mathrm{d}x.\tag{12.6}
$$
We may assume $z>0$ on $(a,b)$, so $z'(a)>0$ and $z'(b)<0$. If $y>0$ on $[a,b]$, the left-hand side of Eq. (12.6) is negative while the right-hand side is nonnegative, a contradiction; the case $y<0$ on $[a,b]$ is the same. Hence $y$ has a zero in $[a,b]$. $\square$

**Corollary 12.2.1** If, in addition to the hypotheses of Theorem 12.2.2, $P\not\equiv Q$ on every subinterval of $[a,b]$, then $y$ has at least one zero in the open interval $(a,b)$.

**Proof** If $y$ has no zero in $(a,b)$, we may assume $y>0$ on $(a,b)$ and $y(a),y(b)\ge0$. Then the left-hand side of Eq. (12.6) is $\le0$, while the integrand on the right is $\ge0$ and positive somewhere ($P-Q\ge0$ is continuous and not identically zero), so the integral is $>0$, a contradiction. $\square$

**Corollary 12.2.2** If $0<m^2\le Q(x)\le M^2$ for $x\in(a,b)$, where $m,M$ are constants, then the distance $d$ between any two consecutive zeros in $(a,b)$ of a nontrivial solution of Eq. (12.4) satisfies

$$
\frac{\pi}{M}\le d\le\frac{\pi}{m}.
$$

**Proof** Compare with the constant-coefficient equations $u''+m^2u=0$ and $v''+M^2v=0$. Consecutive zeros of their solutions $\sin(mx+\theta_1)$ and $\sin(Mx+\theta_2)$ are $\pi/m$ and $\pi/M$ apart, and by choosing $\theta_1,\theta_2$ suitably the zeros can be placed anywhere. If $z$ had consecutive zeros $\alpha<\beta$ with $\beta-\alpha>\pi/m$, we could choose $u$ with two consecutive zeros in $(\alpha,\beta)$; by Theorem 12.2.2 (with $m^2\le Q$), $z$ would have a zero in the closed interval between these two zeros of $u$, contradicting the assumption that $\alpha,\beta$ are consecutive. The other inequality is proved in the same way (comparing with $v$, using $Q\le M^2$). $\square$

The comparison theorem means that "the larger $Q$, the faster the solutions oscillate." The left part of the figure below shows two linearly independent solutions of $y''+xy=0$: their zeros interlace and become denser as the coefficient $x$ grows (with spacing about $\pi/\sqrt x$). The right part compares $z''+z=0$ with $y''+(1+x/5)y=0$: the latter has the larger coefficient, and it has a zero between every two consecutive zeros of $\sin x$.

![Left: the zeros of two linearly independent solutions of y'' + x y = 0 interlace and become denser; right: a solution of y'' + (1 + x/5) y = 0 oscillates faster than sin x](./plots/sturm-zeros.py)

**Example 12.2.1** The normal form of the Bessel equation $x^2y''+xy'+(x^2-\nu^2)y=0$ ($x>0$, see [2.4.10](/2.4.10)) is (by Lemma 12.1.2 with $a_1=1/x$ and $y=z/\sqrt x$)

$$
z''+\Big(1+\frac{1-4\nu^2}{4x^2}\Big)z=0.
$$
By Corollary 12.2.2: for $|\nu|<\frac12$ we have $Q>1$, and consecutive zeros of a **Bessel function** are less than $\pi$ apart; for $|\nu|>\frac12$ we have $Q<1$, and they are more than $\pi$ apart; for $\nu=\frac12$, $z=\sin x$ and the spacing is exactly $\pi$. Moreover $Q\to1$ as $x\to+\infty$, so for every $\varepsilon>0$ we have $(1-\varepsilon)^2\le Q\le(1+\varepsilon)^2$ for $x$ large enough; hence, whatever the value of $\nu$, the spacing of consecutive zeros tends to $\pi$.

### 12.2.3. Comparison Theorem for the Self-Adjoint Form

The comparison theorem also holds for the self-adjoint form; now the equation with smaller $p$ and larger $q$ oscillates faster.

**Theorem 12.2.3 (Sturm–Picone Comparison Theorem)** Suppose $p_1\ge p_2>0$ and $q_2\ge q_1$ on $[a,b]$, with $p_i\in C^1$ and $q_i\in C$. If $a,b$ are consecutive zeros of some nontrivial solution $y$ of $(p_1y')'+q_1y=0$, then every nontrivial solution $z$ of $(p_2z')'+q_2z=0$ has at least one zero in $[a,b]$.

The proof follows the same idea as Theorem 12.2.2, with the integral identity (12.6) replaced by Picone's identity: where $z\ne0$,

$$
\frac{\mathrm{d}}{\mathrm{d}x}\Big[\frac{y}{z}\big(p_1y'z-p_2yz'\big)\Big]=(q_2-q_1)y^2+(p_1-p_2)y'^2+p_2\Big(y'-\frac{y}{z}z'\Big)^2.
$$
If $z$ had no zero on $[a,b]$, integrating from $a$ to $b$ would make the left-hand side zero and the right-hand side the integral of a nonnegative function, so every term would vanish identically. This implies that $z$ is a constant multiple of $y$, contradicting $z(a)\ne0$.

## 12.3. Oscillation and Nonoscillation

### 12.3.1. Oscillatory Equations

**Definition 12.3.1 (Oscillatory Solution)** Let $y$ be a nontrivial solution of Eq. (12.3) (or (12.4)) on $[x_0,+\infty)$. If $y$ has only finitely many zeros on $[x_0,+\infty)$, $y$ is called **nonoscillatory**; otherwise $y$ is called **oscillatory**, that is, there are infinitely many $x_k\in[x_0,+\infty)$ with $y(x_k)=0$. By the isolation of zeros (Lemma 12.1.1), necessarily $x_k\to+\infty$ in this case.

By the separation theorem, on any interval the numbers of zeros of two nontrivial solutions of the same equation differ by at most 1, so one solution oscillates if and only if all nontrivial solutions oscillate.

**Definition 12.3.2 (Oscillatory Equation)** If one (and hence every) nontrivial solution of Eq. (12.3) is oscillatory, the equation is called **oscillatory**; otherwise it is called **nonoscillatory**.

**Theorem 12.3.1** Consider the equations $(p_1y')'+q_1y=0$ and $(p_2y')'+q_2y=0$ for $x\ge x_0$, where $p_1\le p_2$ and $q_1\ge q_2$.

1. If the second equation is oscillatory, so is the first;
2. If the first equation is nonoscillatory, so is the second.

This is a direct consequence of Theorem 12.2.3: a nontrivial solution of the second equation has infinitely many pairs of consecutive zeros on $[x_0,+\infty)$, and between each pair there is a zero of a solution of the first equation. The two statements are contrapositives of each other.

### 12.3.2. The Riccati Inequality Criterion

On an interval where a nontrivial solution $y$ of Eq. (12.3) has no zeros, the function $r=py'/y$ satisfies the first-order equation

$$
r'+q(x)+\frac{r^2}{p(x)}=0,
$$
which is a **Riccati equation** (as can be verified by differentiation). Thus "the solution has no zeros" translates into "the Riccati equation has a global solution", and a solution of the corresponding inequality is already enough:

**Theorem 12.3.2** Eq. (12.3) ($x\ge x_0$) is nonoscillatory if and only if there exist $x_1\ge x_0$ and $r\in C^1[x_1,+\infty)$ such that for $x\ge x_1$

$$
r'+q(x)+\frac{r^2}{p(x)}\le0.\tag{12.7}
$$

**Proof** Necessity: if the equation is nonoscillatory, there is $x_1$ such that some nontrivial solution $y$ has no zeros on $[x_1,+\infty)$; taking $r=py'/y$, Eq. (12.7) holds with equality.

Sufficiency: let $s(x)=r'+q+r^2/p\le0$, so that $r$ satisfies $r'+(q-s)+r^2/p=0$. Let $z(x)=\exp\big(\int_{x_1}^x\frac{r(t)}{p(t)}\,\mathrm{d}t\big)>0$. Then $pz'=rz$ and

$$
(pz')'=r'z+rz'=\Big(r'+\frac{r^2}{p}\Big)z=(s-q)z,
$$
so $z$ is a solution without zeros of the equation $(pz')'+(q-s)z=0$, which is therefore nonoscillatory. Since $q-s\ge q$, part 2 of Theorem 12.3.1 shows that Eq. (12.3) is nonoscillatory. $\square$

**Example 12.3.1** If $q(x)\le0$ for $x\ge x_0$, then Eq. (12.3) is nonoscillatory: take $r\equiv0$, so that $r'+q+r^2/p=q\le0$. Alternatively, compare with $(py')'=0$, which has the solution $y\equiv1$ without zeros.

**Example 12.3.2** If $0<p(x)\le p_0$ and $q(x)\ge q_0>0$, then Eq. (12.3) is oscillatory, and consecutive zeros of any nontrivial solution are at most $\pi\sqrt{p_0/q_0}$ apart. Indeed, compare with $(p_0y')'+q_0y=0$, that is, $y''+\frac{q_0}{p_0}y=0$: the zeros of its solution $\sin\big(\sqrt{q_0/p_0}\,(x-x_0)\big)$ are $x_0+n\pi\sqrt{p_0/q_0}$, and by Theorem 12.2.3 the solutions of Eq. (12.3) have a zero between every two consecutive ones. In particular, if $p\equiv1$ and $q\ge M>0$, consecutive zeros are at most $\pi/\sqrt M$ apart, and if $q(x)\to+\infty$, the spacing of consecutive zeros tends to $0$.

**Example 12.3.3 (The Critical Constant $\frac14$)** The solutions of the **Cauchy–Euler equation** $y''+\dfrac{c}{x^2}y=0$ ($x\ge1$) are $x^m$ with $m(m-1)+c=0$. For $c\le\frac14$, $m$ is real, and every linear combination of the solutions $x^{m_1}$, $x^{m_2}$ (for $c=\frac14$, $\sqrt x$ and $\sqrt x\ln x$) has at most one zero on $x\ge1$, so the equation is nonoscillatory. For $c>\frac14$, $m=\frac12\pm\mathrm{i}\beta$, and the real solution $\sqrt x\cos(\beta\ln x)$ has infinitely many zeros, so the equation is oscillatory. Combined with the comparison theorem this gives Kneser's criterion: if $q(x)\le\frac{1}{4x^2}$ for all sufficiently large $x$, then $y''+q(x)y=0$ is nonoscillatory (this can also be checked directly by taking $r=\frac{1}{2x}$ in Eq. (12.7)); if $q(x)\ge\frac{c}{x^2}$ with $c>\frac14$, the equation is oscillatory. Thus whether an equation with $q\to0$ oscillates depends on how fast $q$ tends to zero.

### 12.3.3. The Prüfer Transformation

Another way to prove comparison theorems is to describe the motion in the phase plane $(y,y')$ in polar coordinates. For the equation $y''=f(x,y,y')$ set

$$
y=r\sin\theta,\qquad y'=r\cos\theta\qquad(r>0).
$$
From $y'=r'\sin\theta+r\theta'\cos\theta=r\cos\theta$ and $y''=r'\cos\theta-r\theta'\sin\theta=f$, multiplying the first by $\sin\theta$ and adding the second times $\cos\theta$, and multiplying the first by $\cos\theta$ and subtracting the second times $\sin\theta$, we obtain the equivalent system

$$
r'=\cos\theta\big[r\sin\theta+f(x,y,y')\big],\qquad\theta'=\cos^2\theta-\frac{\sin\theta\,f(x,y,y')}{r}.
$$
For the normal form $y''+Q(x)y=0$ we have $f=-Qy=-Qr\sin\theta$, and the angle equation does not involve $r$:

$$
\theta'=\cos^2\theta+Q(x)\sin^2\theta.\tag{12.8}
$$
This is the *Prüfer transformation*: it turns a second-order linear equation into a first-order equation for the angle $\theta$, together with an $r$ that can be found once $\theta$ is known. The zeros of $y$ are exactly the points where $\theta$ is an integer multiple of $\pi$; at these points $\theta'=1>0$, so $\theta$ can only cross $k\pi$ increasing. The question about zeros thus becomes the question of "how fast $\theta$ turns", and by Eq. (12.8), the larger $Q$, the faster $\theta$ turns: this is the geometric meaning of the comparison theorem. For the self-adjoint form (12.3) one sets $y=r\sin\theta$, $py'=r\cos\theta$ instead and obtains $\theta'=\frac{1}{p}\cos^2\theta+q\sin^2\theta$.

**Example 12.3.4** Let $0<m^2\le Q(x)\le M^2$. By Eq. (12.8), $\cos^2\theta+m^2\sin^2\theta\le\theta'\le\cos^2\theta+M^2\sin^2\theta$, so the "time" $T=\int_{\theta_0}^{\theta_0+2\pi}\frac{\mathrm{d}x}{\mathrm{d}\theta}\,\mathrm{d}\theta$ needed for $\theta$ to increase by $2\pi$ satisfies

$$
\frac{2\pi}{M}=\int_{\theta_0}^{\theta_0+2\pi}\frac{\mathrm{d}\theta}{\cos^2\theta+M^2\sin^2\theta}\le T\le\int_{\theta_0}^{\theta_0+2\pi}\frac{\mathrm{d}\theta}{\cos^2\theta+m^2\sin^2\theta}=\frac{2\pi}{m},
$$
where we used $\int_{\theta_0}^{\theta_0+2\pi}\frac{\mathrm{d}\theta}{A^2\cos^2\theta+B^2\sin^2\theta}=\frac{2\pi}{AB}$ ($A,B>0$). If $n<m\le M<n+1$ for some positive integer $n$, then $\frac{2\pi}{n+1}<T<\frac{2\pi}{n}$, so on an interval of length $2\pi$ the increment of $\theta$ lies strictly between $2n\pi$ and $2(n+1)\pi$. But if $y$ were a nontrivial $2\pi$-periodic solution, $(y,y')$ would return to its starting point and the increment of $\theta$ would have to be an integer multiple of $2\pi$. Hence in this case the equation $y''+Q(x)y=0$ has no nontrivial $2\pi$-periodic solution. This generalizes the fact that the constant-coefficient equation $y''+M^2y=0$ ($M\notin\mathbb{Z}$) has no $2\pi$-periodic solution (compare the periodic solutions of $y''+M^2y=f$ in [2.4.9](/2.4.9)).

## 12.4. Two-Point Boundary Value Problems

In an initial value problem, $y$ and $y'$ are prescribed at one point, and the solution always exists and is unique. More common in physics is to prescribe one condition at each end of an interval, as for a string fixed at both ends or a rod with given temperatures at both ends; this is a *two-point boundary value problem*. A boundary value problem may have no solution or more than one, depending on the parameters in the equation, and this is exactly where eigenvalue problems come from.

### 12.4.1. The Eigenvalue Problem for $y''+\lambda y=0$

**Definition 12.4.1 (Eigenvalue Problem)** Let $\lambda$ be a parameter. If the boundary value problem

$$
y''+\lambda y=0,\quad x\in[0,l],\qquad\text{with homogeneous boundary conditions}
$$
has a nontrivial solution for $\lambda=\lambda_0$, then $\lambda_0$ is called an **eigenvalue** of the problem, and a corresponding nontrivial solution is called an **eigenfunction** belonging to $\lambda_0$.

Common homogeneous boundary conditions are the *Dirichlet boundary condition* $y(0)=y(l)=0$ (prescribed endpoint values), the *Neumann boundary condition* $y'(0)=y'(l)=0$ (prescribed endpoint derivatives), and mixtures of the two.

**Example 12.4.1 (Dirichlet Problem)** Find the eigenvalues and eigenfunctions of $y''+\lambda y=0$, $y(0)=y(\pi)=0$.

**Solution** If $\lambda=-k^2<0$, the general solution is $y=c_1\mathrm{e}^{kx}+c_2\mathrm{e}^{-kx}$, and the boundary conditions give $c_1=c_2=0$. If $\lambda=0$, then $y=c_1x+c_2$, and again there is only the zero solution. If $\lambda=k^2>0$ ($k>0$), then $y=c_1\cos kx+c_2\sin kx$; $y(0)=0$ gives $c_1=0$, and $y(\pi)=c_2\sin k\pi=0$ with $c_2\ne0$ gives $k\in\mathbb{N}_+$. Hence the eigenvalues are $\lambda_n=n^2$ and the eigenfunctions are $\sin nx$, $n=1,2,\dots$ (negative integers $k$ give negative multiples of the same eigenfunctions, not new eigenvalues).

The same method gives the following table (on the interval $[0,l]$; for a general interval $[a,b]$ replace $x$ by $x-a$ and $l$ by $b-a$).

| Boundary conditions | Eigenvalues $\lambda_n$ | Eigenfunctions | Range of $n$ |
|---|---|---|---|
| $y(0)=y(l)=0$ | $\big(\frac{n\pi}{l}\big)^2$ | $\sin\frac{n\pi x}{l}$ | $1,2,\dots$ |
| $y'(0)=y'(l)=0$ | $\big(\frac{n\pi}{l}\big)^2$ | $\cos\frac{n\pi x}{l}$ | $0,1,2,\dots$ |
| $y(0)=0$, $y'(l)=0$ | $\big(\frac{(2n-1)\pi}{2l}\big)^2$ | $\sin\frac{(2n-1)\pi x}{2l}$ | $1,2,\dots$ |
| $y'(0)=0$, $y(l)=0$ | $\big(\frac{(2n-1)\pi}{2l}\big)^2$ | $\cos\frac{(2n-1)\pi x}{2l}$ | $1,2,\dots$ |
| $y(-l)=y(l)$, $y'(-l)=y'(l)$ | $\big(\frac{n\pi}{l}\big)^2$ | $1$; $\cos\frac{n\pi x}{l}$, $\sin\frac{n\pi x}{l}$ | $0$; $1,2,\dots$ |

The Neumann problem has the additional eigenvalue $0$ (with constant eigenfunctions); the last row is the periodic boundary condition, under which each positive eigenvalue has two linearly independent eigenfunctions. The eigenfunction systems of these five problems give, respectively, the **Fourier sine series**, the **Fourier cosine series**, trigonometric series with half-integer frequencies, and the full **Fourier series**: trigonometric expansions are precisely eigenfunction expansions for these eigenvalue problems. The patterns in the table (the eigenvalues are real, countable and increase to $+\infty$; the $n$th eigenfunction has exactly $n-1$ zeros inside the interval; eigenfunctions are mutually orthogonal) hold for general equations, as shown in §12.5.

### 12.4.2. Nonhomogeneous Boundary Value Problems

**Theorem 12.4.1** Let $a_1,a_2,f\in C[a,b]$, and suppose the homogeneous boundary value problem

$$
y''+a_1(x)y'+a_2(x)y=0,\qquad y(a)=y(b)=0\tag{12.9}
$$
has only the zero solution. Then the nonhomogeneous boundary value problem

$$
y''+a_1(x)y'+a_2(x)y=f(x),\qquad y(a)=y(b)=0\tag{12.10}
$$
has a unique solution.

**Proof** Let $\varphi,\psi$ be a fundamental set of solutions of the homogeneous equation. By variation of parameters ([2.4.9](/2.4.9)), the general solution of the nonhomogeneous equation is $y=C_1\varphi+C_2\psi+y^*$, where

$$
y^*(x)=\int_a^xK(x,t)f(t)\,\mathrm{d}t,\qquad K(x,t)=\frac{\varphi(t)\psi(x)-\varphi(x)\psi(t)}{\varphi(t)\psi'(t)-\varphi'(t)\psi(t)}.
$$
The boundary conditions give the linear system

$$
C_1\varphi(a)+C_2\psi(a)=-y^*(a),\qquad C_1\varphi(b)+C_2\psi(b)=-y^*(b),
$$
with determinant $\Delta=\varphi(a)\psi(b)-\varphi(b)\psi(a)$. If $\Delta=0$, there are $c_1,c_2$, not both zero, such that $y_0=c_1\varphi+c_2\psi$ satisfies $y_0(a)=y_0(b)=0$; since $\varphi,\psi$ are linearly independent, $y_0$ is a nontrivial solution of (12.9), contrary to the hypothesis. Hence $\Delta\ne0$, and $C_1,C_2$ are uniquely determined:

$$
C_1=\frac{y^*(b)\psi(a)-y^*(a)\psi(b)}{\Delta},\qquad C_2=\frac{y^*(a)\varphi(b)-y^*(b)\varphi(a)}{\Delta}.
$$
Uniqueness: the difference of two solutions solves (12.9) and must be zero. $\square$

Conversely, if the homogeneous problem has a nontrivial solution, the nonhomogeneous problem has either no solution or infinitely many (see the end of §12.4.3). This is completely analogous to the situation for $A\boldsymbol{x}=\boldsymbol{b}$ in linear algebra.

**Example 12.4.2** Let $M>0$ with $2M\notin\mathbb{Z}$. Solve $y''+M^2y=f(x)$, $y(0)=y(2\pi)=0$.

**Solution** Take $\varphi=\cos Mx$ and $\psi=\sin Mx$. Then $K(x,t)=\frac1M\sin M(x-t)$, $y^*(x)=\frac1M\int_0^x\sin M(x-t)f(t)\,\mathrm{d}t$ and $y^*(0)=0$. We have $\Delta=\sin2M\pi\ne0$: the condition $2M\notin\mathbb{Z}$ says precisely that $M^2$ is not one of the eigenvalues $k^2/4$ of the Dirichlet problem on $[0,2\pi]$ (see the table in §12.4.1), so the homogeneous problem has only the zero solution. Hence $C_1=0$,

$$
C_2=-\frac{y^*(2\pi)}{\sin2M\pi}=\frac{1}{M\sin2M\pi}\int_0^{2\pi}\sin M(t-2\pi)f(t)\,\mathrm{d}t,
$$
and the unique solution is

$$
y(x)=\frac1M\Big[\frac{\sin Mx}{\sin2M\pi}\int_0^{2\pi}\sin M(t-2\pi)f(t)\,\mathrm{d}t+\int_0^x\sin M(x-t)f(t)\,\mathrm{d}t\Big].
$$

### 12.4.3. Green's Functions

The solution in Theorem 12.4.1 can be written as an integral operator applied to $f$. The result is most symmetric for the self-adjoint form. Let

$$
Ly=-\big(p(x)y'\big)'+q(x)y,\qquad p\in C^1[a,b],\ p>0,\ q\in C[a,b].
$$

**Theorem 12.4.2** Suppose the homogeneous problem $Ly=0$, $y(a)=y(b)=0$ has only the zero solution. Take nontrivial solutions $u_1,u_2$ of $Lu=0$ with $u_1(a)=0$ and $u_2(b)=0$, and let $c=p\,(u_1u_2'-u_1'u_2)$, which is a constant (§12.1.2). Then $c\ne0$, and for every $f\in C[a,b]$ the unique solution of the problem $Ly=f$, $y(a)=y(b)=0$ is

$$
y(x)=\int_a^bG(x,t)f(t)\,\mathrm{d}t,\qquad G(x,t)=-\frac1c\begin{cases}u_1(t)u_2(x),&a\le t\le x,\\u_1(x)u_2(t),&x\le t\le b.\end{cases}\tag{12.11}
$$

**Proof** If $c=0$, then $u_1,u_2$ are linearly dependent, so $u_1$ satisfies the conditions at both ends and is a nontrivial solution of the homogeneous problem, a contradiction. Write $y=-\frac1c\big[u_2(x)\int_a^xu_1f\,\mathrm{d}t+u_1(x)\int_x^bu_2f\,\mathrm{d}t\big]$. On differentiation, the two terms $\pm u_1(x)u_2(x)f(x)$ coming from the variable limits cancel, giving $y'=-\frac1c\big[u_2'\int_a^xu_1f+u_1'\int_x^bu_2f\big]$; differentiating again,

$$
(py')'=-\frac1c\Big[(pu_2')'\int_a^xu_1f+(pu_1')'\int_x^bu_2f\Big]-\frac1c\,p\,(u_2'u_1-u_1'u_2)f=qy-f,
$$
that is, $Ly=f$. Moreover $y(a)=-\frac1cu_1(a)\int_a^bu_2f=0$, and similarly $y(b)=0$. $\square$

**Definition 12.4.2 (Green's Function)** The function $G(x,t)$ in Eq. (12.11) is called the **Green's function** of the boundary value problem $Ly=f$, $y(a)=y(b)=0$.

The Green's function has the following characteristic properties, which can also be used to find $G$ directly:

1. For fixed $t$, $G(\cdot,t)$ satisfies $LG=0$ for $x\ne t$ and satisfies the boundary conditions at both ends;
2. $G$ is continuous on $[a,b]^2$ and symmetric: $G(x,t)=G(t,x)$;
3. $\partial G/\partial x$ has a jump at $x=t$: $\dfrac{\partial G}{\partial x}(t^+,t)-\dfrac{\partial G}{\partial x}(t^-,t)=-\dfrac{1}{p(t)}$.

Physically, $G(x,t)$ is the response of the system at $x$ to a unit point force (or point heat source) applied at $t$, and the solution $y=\int G f$ views a distributed force as a superposition of infinitely many point forces; the symmetry $G(x,t)=G(t,x)$ is the reciprocity principle.

**Example 12.4.3** Find the Green's function of $-y''=f(x)$, $y(0)=y(1)=0$.

**Solution** Here $p=1$ and $q=0$. Take $u_1=x$ and $u_2=1-x$; then $c=x\cdot(-1)-1\cdot(1-x)=-1$, and

$$
G(x,t)=\begin{cases}t(1-x),&0\le t\le x,\\x(1-t),&x\le t\le1.\end{cases}
$$
For example, for $f\equiv1$, $y=\int_0^xt(1-x)\,\mathrm{d}t+\int_x^1x(1-t)\,\mathrm{d}t=\frac{x(1-x)}{2}$, and one checks directly that $-y''=1$. Here $G\ge0$: an upward force bends the string upward everywhere.

![The Green's function G(x, t) of -y'' = f, y(0) = y(1) = 0: piecewise linear graphs for several fixed values of t](./plots/green-function.py)

If the homogeneous problem has a nontrivial solution $\varphi$ (that is, $0$ is an eigenvalue), the Green's function does not exist. In this case, for self-adjoint operators we have the *Fredholm alternative*: $Ly=f$ with the boundary conditions is solvable if and only if $\int_a^bf\varphi\,\mathrm{d}x=0$, and when it is solvable the solutions differ by arbitrary multiples of $\varphi$. For example, $-y''=f$, $y'(0)=y'(1)=0$ ($\varphi=1$) is solvable if and only if $\int_0^1f\,\mathrm{d}x=0$: for a rod insulated at both ends, a steady-state temperature is possible only if the heat sources add up to zero.

## 12.5. Sturm–Liouville Problems

### 12.5.1. Regular Sturm–Liouville Problems

**Definition 12.5.1 (Sturm–Liouville Problem)** Let $p\in C^1[a,b]$ with $p>0$, let $q,w\in C[a,b]$ with $w>0$, let the real numbers $\alpha_1,\alpha_2$ be not both zero, and let $\beta_1,\beta_2$ be not both zero. The boundary value problem with parameter $\lambda$

$$
-\big(p(x)y'\big)'+q(x)y=\lambda w(x)y,\quad a<x<b,\tag{12.12}
$$

$$
\alpha_1y(a)-\alpha_2y'(a)=0,\qquad\beta_1y(b)+\beta_2y'(b)=0\tag{12.13}
$$
is called a **regular Sturm–Liouville problem**. A value of $\lambda$ for which it has a nontrivial solution is called an eigenvalue, a corresponding nontrivial solution is called an eigenfunction, and $w$ is called the weight function.

The conditions (12.13) are called separated boundary conditions: each involves only one endpoint. The case $\alpha_2=0$ is a Dirichlet condition, $\alpha_1=0$ is a Neumann condition, and when both are nonzero it is called a Robin condition (a boundary condition of the third kind). Example 12.4.1 is the special case $p=w=1$, $q=0$. If the interval is unbounded, or $p$ or $w$ vanishes at an endpoint, the problem is called singular; the Legendre and Bessel equations ([2.4.10](/2.4.10)) both lead to problems of this kind.

Let $Ly=-(py')'+qy$. For $u,v\in C^2[a,b]$ we have Lagrange's identity $vLu-uLv=\frac{\mathrm{d}}{\mathrm{d}x}\big[p(uv'-u'v)\big]$, and integration gives Green's formula

$$
\int_a^b(vLu-uLv)\,\mathrm{d}x=\Big[p\,(uv'-u'v)\Big]_a^b.\tag{12.14}
$$
If $u,v$ both satisfy (12.13), then at $x=a$ the nonzero vector $(\alpha_1,-\alpha_2)$ solves the homogeneous system with coefficient matrix $\begin{bmatrix}u(a)&u'(a)\\v(a)&v'(a)\end{bmatrix}$, so the determinant $uv'-u'v$ vanishes at $a$; the same holds at $b$. Hence the right-hand side of Eq. (12.14) vanishes:

$$
\int_a^b vLu\,\mathrm{d}x=\int_a^b uLv\,\mathrm{d}x.
$$
In terms of the inner product $\langle u,v\rangle=\int_a^b uv\,\mathrm{d}x$, this says $\langle Lu,v\rangle=\langle u,Lv\rangle$: $L$ is symmetric on the space of functions satisfying (12.13). This is the analogue of a real symmetric matrix (a **self-adjoint operator**) in finite dimensions, and the theorems below correspond one to one to the facts that "the eigenvalues of a real symmetric matrix are real and eigenvectors belonging to distinct eigenvalues are orthogonal".

### 12.5.2. Properties of Eigenvalues and Eigenfunctions

**Theorem 12.5.1** The regular Sturm–Liouville problem (12.12)–(12.13) has the following properties:

1. All eigenvalues are real, and the eigenfunctions can be taken to be real-valued;
2. Every eigenvalue is simple: eigenfunctions belonging to the same eigenvalue differ only by constant factors;
3. Eigenfunctions belonging to distinct eigenvalues are orthogonal with respect to the weight $w$: for $\lambda\ne\mu$, $\int_a^b\varphi_\lambda\varphi_\mu w\,\mathrm{d}x=0$.

**Proof** (1) Let $L\varphi=\lambda w\varphi$, where $\varphi$ may be complex-valued. Since $p,q,w$ and the coefficients of the boundary conditions are real, $\bar\varphi$ satisfies $L\bar\varphi=\bar\lambda w\bar\varphi$ and (12.13). Taking $u=\varphi$ and $v=\bar\varphi$ in Eq. (12.14):

$$
0=\int_a^b(\bar\varphi L\varphi-\varphi L\bar\varphi)\,\mathrm{d}x=(\lambda-\bar\lambda)\int_a^bw|\varphi|^2\,\mathrm{d}x,
$$
and since $\int w|\varphi|^2>0$, we get $\lambda=\bar\lambda$. Then the real and imaginary parts of $\varphi$ both satisfy the equation and the boundary conditions, and at least one of them is not identically zero; it is a real eigenfunction.

(2) If $\varphi,\psi$ belong to the same eigenvalue, then by the discussion above their Wronskian vanishes at $a$; since they are solutions of the same second-order linear equation, they are linearly dependent.

(3) Taking $u=\varphi_\lambda$ and $v=\varphi_\mu$ in Eq. (12.14) gives $(\lambda-\mu)\int_a^b\varphi_\lambda\varphi_\mu w\,\mathrm{d}x=0$. $\square$

**Theorem 12.5.2** The eigenvalues of a regular Sturm–Liouville problem form a strictly increasing sequence of real numbers tending to $+\infty$,

$$
\lambda_1<\lambda_2<\cdots<\lambda_n<\cdots\to+\infty,
$$
and an eigenfunction $\varphi_n$ belonging to $\lambda_n$ has exactly $n-1$ zeros in the open interval $(a,b)$.

The idea of the proof is the Prüfer transformation (§12.3.3). Setting $y=r\sin\theta$ and $py'=r\cos\theta$, the angle for Eq. (12.12) satisfies

$$
\theta'=\frac{1}{p}\cos^2\theta+(\lambda w-q)\sin^2\theta.
$$
The condition at the left endpoint fixes $\theta(a)=\alpha\in[0,\pi)$ (with $\alpha_1\sin\alpha=\frac{\alpha_2}{p(a)}\cos\alpha$), and the condition at the right endpoint requires $\theta(b)$ to equal a fixed angle $\beta\in(0,\pi]$ plus an integer multiple of $\pi$. Let $\theta(b;\lambda)$ be the value at $b$ of the solution with $\theta(a)=\alpha$. A comparison argument shows that it is continuous and strictly increasing in $\lambda$, tends to $0$ as $\lambda\to-\infty$, and tends to $+\infty$ as $\lambda\to+\infty$. Hence for each $n=1,2,\dots$ the equation $\theta(b;\lambda)=\beta+(n-1)\pi$ has exactly one solution $\lambda_n$; in $(a,b)$, $\theta$ crosses each of $\pi,2\pi,\dots,(n-1)\pi$ exactly once, and these crossings are the $n-1$ zeros of $\varphi_n$.

That the $n$th eigenfunction has exactly $n-1$ zeros generalizes the fact that $\sin nx$ has $n-1$ zeros in $(0,\pi)$: the larger the eigenvalue, the faster the eigenfunction oscillates. The right part of the figure below shows numerical results for a problem with variable coefficients, exhibiting the same pattern.

![Left: the first four eigenfunctions sin nx of y'' + λ y = 0, y(0) = y(π) = 0; right: the first four eigenfunctions (computed numerically) of -((1 + x) y')' = λ y, y(0) = y(1) = 0; the nth one has n - 1 interior zeros](./plots/sl-eigenfunctions.py)

The sign of the eigenvalues can often be determined from the Rayleigh quotient. Multiplying $L\varphi=\lambda w\varphi$ by $\varphi$ and integrating by parts gives

$$
\lambda\int_a^bw\varphi^2\,\mathrm{d}x=\int_a^b\big(p\varphi'^2+q\varphi^2\big)\,\mathrm{d}x-\Big[p\varphi\varphi'\Big]_a^b.
$$
If $q\ge0$, $\alpha_1\alpha_2\ge0$ and $\beta_1\beta_2\ge0$, then the boundary term $-[p\varphi\varphi']_a^b$ is $\ge0$ (for example, if $\alpha_2\ne0$, then $p(a)\varphi(a)\varphi'(a)=p(a)\frac{\alpha_1}{\alpha_2}\varphi(a)^2\ge0$), and therefore all eigenvalues satisfy $\lambda\ge0$. Dirichlet and Neumann conditions both meet this requirement.

### 12.5.3. Eigenfunction Expansions

Normalize the eigenfunctions so that $\int_a^b\varphi_n^2w\,\mathrm{d}x=1$. Then $\{\varphi_n\}$ is a normalized **orthogonal system of functions** with respect to the weight $w$. By analogy with Fourier series, for a function $f$ define

$$
c_n=\int_a^bf(x)\varphi_n(x)w(x)\,\mathrm{d}x,\qquad f\sim\sum_{n=1}^\infty c_n\varphi_n(x).\tag{12.15}
$$
This is called the *eigenfunction expansion* of $f$, and $c_n$ is the "coordinate" of $f$ along $\varphi_n$.

**Theorem 12.5.3 (Expansion Theorem)** Let $\{\varphi_n\}$ be the orthonormal system of eigenfunctions of the regular Sturm–Liouville problem (12.12)–(12.13).

1. If $f\in C^2[a,b]$ satisfies the boundary conditions (12.13), then the series (12.15) converges absolutely and uniformly to $f$ on $[a,b]$;
2. If $f$ is piecewise smooth on $[a,b]$, then the series converges at every point of $(a,b)$ to $\frac12\big[f(x^+)+f(x^-)\big]$, as in Dirichlet's theorem for Fourier series ([2.2.9](/2.2.9#thm-9.3.1));
3. If $\int_a^bf^2w\,\mathrm{d}x<+\infty$, then the series converges to $f$ in the mean square, and Parseval's identity $\int_a^bf^2w\,\mathrm{d}x=\sum_{n=1}^\infty c_n^2$ holds.

Part 3 expresses the completeness of the system of eigenfunctions: it is an "orthogonal basis" of the space of square-integrable functions. The proof regards the inverse of $L$ (the integral operator whose kernel is the Green's function, §12.4.3) as a compact symmetric operator and applies its spectral theorem; we do not go into it here. For the Dirichlet and Neumann problems on $[0,\pi]$, the theorem is the convergence theorem for Fourier sine and cosine series.

**Example 12.5.1 (The Legendre Equation)** The problem $\big((1-x^2)y'\big)'+\lambda y=0$, $-1<x<1$, is a singular Sturm–Liouville problem in which $p=1-x^2$ vanishes at both ends; the "boundary condition" is replaced by boundedness at $x=\pm1$. One can show that it has bounded solutions exactly for $\lambda=n(n+1)$ ($n=0,1,2,\dots$), with the **Legendre polynomials** $P_n(x)$ as eigenfunctions. Hence $\int_{-1}^1P_mP_n\,\mathrm{d}x=0$ ($m\ne n$), and functions on $[-1,1]$ can be expanded in Legendre polynomials.

**Example 12.5.2 (The Bessel Equation)** Separation of variables in polar coordinates on a disk of radius $R$ leads to $(xy')'+\big(\lambda x-\frac{\nu^2}{x}\big)y=0$, $0<x<R$, $y(R)=0$, with $y$ bounded at $0$. Here $p=w=x$ vanishes at $x=0$, so the problem is singular. Its eigenfunctions are $J_\nu(\sqrt{\lambda_k}\,x)$, where $\sqrt{\lambda_k}R$ is the $k$th positive zero of $J_\nu$; they are orthogonal with respect to the weight $x$, which gives the Fourier–Bessel expansion.

### 12.5.4. Connection with Separation of Variables

Take as an example heat conduction in a rod of length $l$ whose ends are held at temperature zero: $u_t=u_{xx}$, $u(0,t)=u(l,t)=0$, $u(x,0)=f(x)$. Setting $u=X(x)T(t)$ and substituting gives $\frac{T'}{T}=\frac{X''}{X}=-\lambda$, so $X$ satisfies the Dirichlet eigenvalue problem $X''+\lambda X=0$, $X(0)=X(l)=0$, with $\lambda_n=(n\pi/l)^2$ and $X_n=\sin\frac{n\pi x}{l}$, while $T_n=\mathrm{e}^{-\lambda_nt}$. Superposition gives

$$
u(x,t)=\sum_{n=1}^\infty c_n\mathrm{e}^{-(n\pi/l)^2t}\sin\frac{n\pi x}{l},
$$
and the initial condition requires $f=\sum c_n\sin\frac{n\pi x}{l}$, with $c_n$ determined by the eigenfunction expansion (12.15). For general domains, media with variable coefficients or other boundary conditions, one simply replaces $\sin\frac{n\pi x}{l}$ by the eigenfunctions of the corresponding Sturm–Liouville problem; Theorems 12.5.1–12.5.3 justify the method. See [2.5](/2.5) for details.

## Summary

| Result | Statement | Method |
|---|---|---|
| Isolated, simple zeros | Zeros of a nontrivial solution have no accumulation point, and $y'\ne0$ there | Uniqueness |
| Separation theorem | Zeros of two linearly independent solutions of the same equation interlace | The Wronskian does not change sign |
| Comparison theorem | If $Q\le P$, between consecutive zeros of $z''+Qz=0$ there is a zero of $y''+Py=0$ | Integral identity (12.6) / Picone's identity |
| Spacing of zeros | $m^2\le Q\le M^2$ ⟹ $\pi/M\le d\le\pi/m$ | Comparison with constant-coefficient equations |
| Nonoscillation criterion | Nonoscillatory ⟺ the Riccati inequality (12.7) has a global solution | $r=py'/y$ |
| Boundary value problems | Homogeneous problem has only the zero solution ⟹ nonhomogeneous problem uniquely solvable, with solution $=\int Gf$ | Variation of parameters, Green's function |
| Sturm–Liouville | Eigenvalues real, simple, $\lambda_n\uparrow+\infty$; $\varphi_n$ has $n-1$ zeros; eigenfunctions orthogonal with respect to $w$ and complete | Green's formula (12.14), Prüfer transformation |
