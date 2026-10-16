---
title: Separation of Variables
---

On a bounded interval, d'Alembert's formula has to be combined with infinitely many reflections ([2.5.3](/2.5.3#sec-3.2.3)), and for the heat and Laplace equations there is no such formula at all. The method of *separation of variables*, due to Daniel Bernoulli and Fourier, works instead for all three classical equations on simple bounded regions. We look for solutions of the special form $u=X(x)T(t)$; the equation then splits into ordinary differential equations, the boundary conditions turn the equation for $X$ into an **eigenvalue problem** ([2.4.12](/2.4.12#sec-12.4.1)), and the general solution is obtained by superposing the resulting product solutions. The initial (or boundary) data are matched by expanding them in **eigenfunctions**, which for the simplest boundary conditions is exactly a **Fourier series** ([2.2.9](/2.2.9#sec-9.3)). The physical content is a decomposition into modes: a vibrating string is a superposition of standing waves with discrete natural frequencies, and a cooling rod is a superposition of temperature profiles that decay at different exponential rates. We treat the vibrating string, the heat equation in a rod with various boundary conditions, the general method and its justification by Sturm–Liouville theory ([2.4.12](/2.4.12#sec-12.5)), nonhomogeneous equations and boundary conditions, and the Laplace equation in a rectangle and a disk, where summing the series gives Poisson's integral formula. The same method in cylindrical and spherical coordinates, which leads to Bessel functions and Legendre polynomials, is the subject of [2.5.5](/2.5.5); on unbounded regions the series become Fourier integrals ([2.5.6](/2.5.6)).

## 4.1. The Vibrating String with Fixed Ends

### 4.1.1. Separation of Variables

Consider a string of length $l$ fixed at both ends:

$$
\begin{cases}u_{tt}=c^2u_{xx},&0<x<l,\ t>0,\\u(0,t)=u(l,t)=0,&t\ge0,\\u(x,0)=\varphi(x),\quad u_t(x,0)=\psi(x),&0\le x\le l.\end{cases}\tag{4.1}
$$
The equation and the boundary conditions are linear and homogeneous, so by the **superposition principle** sums of solutions are solutions; the initial conditions will be imposed at the end. We look for nonzero solutions of the form $u(x,t)=X(x)T(t)$. Substituting into the equation gives $XT''=c^2X''T$, that is,

$$
\frac{T''(t)}{c^2T(t)}=\frac{X''(x)}{X(x)}.
$$
The left side depends only on $t$, the right side only on $x$; so both equal a constant, which we write as $-\lambda$. The boundary conditions $X(0)T(t)=X(l)T(t)=0$ for all $t$ (with $T\not\equiv0$) give $X(0)=X(l)=0$. Thus

$$
X''+\lambda X=0,\quad X(0)=X(l)=0;\qquad T''+\lambda c^2T=0.\tag{4.2}
$$
The problem for $X$ is the Dirichlet eigenvalue problem of [Example 12.4.1](/2.4.12#sec-12.4.1): it has nontrivial solutions only for

$$
\lambda_n=\Big(\frac{n\pi}{l}\Big)^2,\qquad X_n(x)=\sin\frac{n\pi x}{l},\qquad n=1,2,\dots
$$
For $\lambda=\lambda_n$ the equation for $T$ gives $T_n(t)=A_n\cos\frac{n\pi ct}{l}+B_n\sin\frac{n\pi ct}{l}$. Superposing all the product solutions,

$$
u(x,t)=\sum_{n=1}^\infty\Big(A_n\cos\frac{n\pi ct}{l}+B_n\sin\frac{n\pi ct}{l}\Big)\sin\frac{n\pi x}{l}.\tag{4.3}
$$
Setting $t=0$ in the series and in its derivative with respect to $t$, the initial conditions require

$$
\varphi(x)=\sum_{n=1}^\infty A_n\sin\frac{n\pi x}{l},\qquad\psi(x)=\sum_{n=1}^\infty\frac{n\pi c}{l}B_n\sin\frac{n\pi x}{l},
$$
which are **Fourier sine series** on $[0,l]$ ([2.2.9](/2.2.9#sec-9.3.2)). By orthogonality,

$$
A_n=\frac2l\int_0^l\varphi(x)\sin\frac{n\pi x}{l}\,\mathrm{d}x,\qquad B_n=\frac{2}{n\pi c}\int_0^l\psi(x)\sin\frac{n\pi x}{l}\,\mathrm{d}x.\tag{4.4}
$$

### 4.1.2. Convergence of the Series

So far the computation is formal: we must check that the series (4.3) with coefficients (4.4) converges, can be differentiated twice term by term, and attains the initial values. This depends on how fast the coefficients decay, hence on the smoothness of the data.

**Theorem 4.1.1** Let $\varphi\in C^3[0,l]$ and $\psi\in C^2[0,l]$ satisfy the compatibility conditions

$$
\varphi(0)=\varphi(l)=\varphi''(0)=\varphi''(l)=0,\qquad\psi(0)=\psi(l)=0.\tag{4.5}
$$
Then the series (4.3), with coefficients (4.4), converges together with its partial derivatives of order at most $2$ uniformly on $[0,l]\times[0,+\infty)$, and its sum is the unique $C^2$ solution of problem (4.1).

**Proof** Integrating by parts three times in the formula for $A_n$, the boundary terms vanish by (4.5), and we get

$$
A_n=-\Big(\frac{l}{n\pi}\Big)^3a_n,\qquad a_n=\frac2l\int_0^l\varphi'''(x)\cos\frac{n\pi x}{l}\,\mathrm{d}x.
$$
The $a_n$ are coefficients of $\varphi'''$ with respect to the orthogonal system $\cos\frac{n\pi x}{l}$, so by orthogonality

$$
0\le\int_0^l\Big(\varphi'''-\sum_{n=1}^Na_n\cos\frac{n\pi x}{l}\Big)^2\mathrm{d}x=\int_0^l(\varphi''')^2\,\mathrm{d}x-\frac l2\sum_{n=1}^Na_n^2,
$$
which gives Bessel's inequality $\sum a_n^2\le\frac2l\int_0^l(\varphi''')^2\,\mathrm{d}x<+\infty$. By the **Cauchy–Schwarz inequality**,

$$
\sum_{n=1}^\infty n^2\lvert A_n\rvert=\Big(\frac l\pi\Big)^3\sum_{n=1}^\infty\frac{\lvert a_n\rvert}{n}\le\Big(\frac l\pi\Big)^3\Big(\sum a_n^2\Big)^{1/2}\Big(\sum\frac1{n^2}\Big)^{1/2}<+\infty.
$$
In the same way, two integrations by parts give $B_n=-\frac{l^3}{c\,(n\pi)^3}b_n$ with $b_n$ the sine coefficients of $\psi''$, and $\sum n^2\lvert B_n\rvert<+\infty$. Each term of the series (4.3) and of its first and second partial derivatives is bounded by a constant times $n^2(\lvert A_n\rvert+\lvert B_n\rvert)$, so by the **Weierstrass M-test** all these series converge uniformly. By [Theorem 1.1.1](/2.5.1#thm-1.1.1) the sum is a $C^2$ solution, and the boundary and initial conditions hold by construction (the sine series of $\varphi$ and $\psi$ converge to them by **Dirichlet's convergence theorem**). Uniqueness was proved by the energy method ([Theorem 3.4.2](/2.5.3#thm-3.4.2)). $\square$

The conditions (4.5) are natural: $\varphi(0)=\psi(0)=0$ say that the data respect the fixed ends, and $\varphi''(0)=0$ follows from $u_{tt}(0,t)=0$, as for the semi-infinite string ([2.5.3](/2.5.3#thm-3.2.1)). For data that do not satisfy them, such as the plucked string, the series still converges and defines a generalized solution. Indeed, by the product formula $\sin\alpha\cos\beta=\frac12[\sin(\alpha+\beta)+\sin(\alpha-\beta)]$, the series (4.3) can be rewritten as d'Alembert's formula applied to the odd $2l$-periodic extensions of $\varphi$ and $\psi$ ([2.5.3](/2.5.3#sec-3.2.3)): the two methods give the same solution.

### 4.1.3. Standing Waves and Natural Frequencies

Each term of the series (4.3) can be written as

$$
u_n(x,t)=C_n\sin\frac{n\pi x}{l}\cos\big(\omega_nt-\theta_n\big),\qquad\omega_n=\frac{n\pi c}{l},\quad C_n=\sqrt{A_n^2+B_n^2}.
$$
It is a *standing wave*: every point of the string oscillates in phase with the same frequency, with an amplitude $C_n\lvert\sin\frac{n\pi x}{l}\rvert$ that depends on the position. The points $x=\frac{jl}{n}$ ($j=1,\dots,n-1$) where the amplitude vanishes are the nodes, and the points of maximal amplitude are the antinodes. The solutions $u_n$ are the normal modes of the string, and $\omega_n$ are its *natural frequencies*. In terms of the tension and density, the frequencies are

$$
f_n=\frac{\omega_n}{2\pi}=\frac{n}{2l}\sqrt{\frac T\rho},\qquad n=1,2,\dots
$$
The lowest one, $f_1$, is the fundamental frequency, and the others are its integer multiples, the harmonics. This is why a string produces a definite musical pitch, and why a shorter, tighter or lighter string sounds higher. The energy of the string ([2.5.3](/2.5.3#sec-3.4.1)) is the sum of the energies of the modes, $E=\frac{l}{4}\sum_n\omega_n^2C_n^2$, since the cross terms vanish by orthogonality.

**Example 4.1.1 (The Plucked String)** A string is pulled aside at the point $x=b$ to height $h$ and released from rest: $\psi=0$, and $\varphi(x)=\frac{hx}{b}$ for $0\le x\le b$, $\varphi(x)=\frac{h(l-x)}{l-b}$ for $b\le x\le l$. Then $B_n=0$ and

$$
A_n=\frac2l\int_0^l\varphi(x)\sin\frac{n\pi x}{l}\,\mathrm{d}x=\frac{2hl^2}{\pi^2n^2b(l-b)}\sin\frac{n\pi b}{l},
$$
so

$$
u(x,t)=\frac{2hl^2}{\pi^2b(l-b)}\sum_{n=1}^\infty\frac{1}{n^2}\sin\frac{n\pi b}{l}\sin\frac{n\pi x}{l}\cos\frac{n\pi ct}{l}.
$$
The amplitudes decay like $1/n^2$, reflecting the corner of the initial shape. The modes with a node at the plucking point are missing: plucked at the middle, $b=l/2$, the string sounds no even harmonics. Guitarists use this to change the timbre by plucking nearer to or farther from the bridge.

![Left: the first four normal modes sin(nπx/l) cos(ω_n t) of a string with fixed ends, at several instants. Right: the plucked string (b = l/4) at several times, computed from the series; the corners travel along the string as predicted by d'Alembert's formula](./plots/string-modes.py)

## 4.2. Heat Conduction in a Finite Rod

### 4.2.1. Ends at Zero Temperature

For a rod of length $l$ with both ends kept at temperature $0$,

$$
\begin{cases}u_t=ku_{xx},&0<x<l,\ t>0,\\u(0,t)=u(l,t)=0,&t>0,\\u(x,0)=\varphi(x),&0\le x\le l.\end{cases}\tag{4.6}
$$
Substituting $u=X(x)T(t)$ gives $\frac{T'}{kT}=\frac{X''}{X}=-\lambda$, the same eigenvalue problem for $X$ as before, and $T'+k\lambda T=0$, so $T_n=\mathrm{e}^{-k\lambda_nt}$. Hence (as already sketched in [2.4.12](/2.4.12#sec-12.5.4))

$$
u(x,t)=\sum_{n=1}^\infty C_n\,\mathrm{e}^{-k(n\pi/l)^2t}\sin\frac{n\pi x}{l},\qquad C_n=\frac2l\int_0^l\varphi(x)\sin\frac{n\pi x}{l}\,\mathrm{d}x.\tag{4.7}
$$
The exponential factors make this series far better behaved than the series for the wave equation.

**Theorem 4.2.1** Let $\varphi$ be bounded and integrable on $[0,l]$.

1. For $t>0$ the series (4.7) converges, together with all its partial derivatives, uniformly on $[0,l]\times[t_0,+\infty)$ for every $t_0>0$. Its sum $u$ is infinitely differentiable for $t>0$, satisfies the heat equation and the boundary conditions, and $\lvert u(x,t)\rvert\le M\mathrm{e}^{-k\pi^2t/l^2}\sum_{n}\mathrm{e}^{-k(n^2-1)\pi^2t/l^2}$ with $M=\frac2l\int_0^l\lvert\varphi\rvert\,\mathrm{d}x$, so $u\to0$ exponentially as $t\to+\infty$.
2. If moreover $\varphi$ is continuous and piecewise $C^1$ with $\varphi(0)=\varphi(l)=0$, then $u$ is continuous on $[0,l]\times[0,+\infty)$ and $u(x,0)=\varphi(x)$.

**Proof** (1) $\lvert C_n\rvert\le M$. For $t\ge t_0$, a partial derivative $\partial_t^j\partial_x^m$ of the $n$th term is bounded by $M\big(k\frac{n^2\pi^2}{l^2}\big)^j\big(\frac{n\pi}{l}\big)^m\mathrm{e}^{-kn^2\pi^2t_0/l^2}$, and these bounds form a convergent series because the exponential decays faster than any power of $n$ grows. The Weierstrass M-test and termwise differentiation ([2.2.9](/2.2.9#thm-9.1.6)) give the smoothness, and each term satisfies the equation and the boundary conditions. The bound on $\lvert u\rvert$ follows from $\lvert C_n\rvert\le M$.

(2) Integrating by parts, $C_n=\frac{l}{n\pi}c_n'$, where $c_n'$ are the cosine coefficients of $\varphi'$; as in the proof of Theorem 4.1.1, $\sum\lvert C_n\rvert<+\infty$. Since every term of (4.7) is bounded by $\lvert C_n\rvert$ for $t\ge0$, the series converges uniformly on $[0,l]\times[0,+\infty)$, its sum is continuous, and at $t=0$ it is the sine series of $\varphi$, which converges to $\varphi$ by Dirichlet's convergence theorem. $\square$

Part 1 is the *smoothing effect* of the heat equation: whatever the initial temperature, even a discontinuous one, the temperature is infinitely differentiable at every positive time. The reason is visible in the formula: the $n$th mode decays at the rate $kn^2\pi^2/l^2$, so fine details (large $n$) disappear almost instantly. For large $t$ only the first mode survives:

$$
u(x,t)\approx C_1\,\mathrm{e}^{-k\pi^2t/l^2}\sin\frac{\pi x}{l},
$$
and the temperature profile approaches the shape of a sine arch, decaying on the time scale $l^2/(k\pi^2)$. Doubling the length of the rod makes it cool four times more slowly. This is the reverse side of the ill-posedness of the backward heat equation ([2.5.1](/2.5.1#sec-1.4)). In contrast with the wave equation, the time dependence is not oscillatory and the process is irreversible.

**Example 4.2.1** A rod at uniform temperature $u_0$ has its ends plunged into ice water at $t=0$: $\varphi\equiv u_0$. Then $C_n=\frac{2u_0}{n\pi}(1-(-1)^n)$, which is $\frac{4u_0}{n\pi}$ for odd $n$ and $0$ for even $n$, and

$$
u(x,t)=\frac{4u_0}{\pi}\sum_{m=0}^\infty\frac{1}{2m+1}\,\mathrm{e}^{-k(2m+1)^2\pi^2t/l^2}\sin\frac{(2m+1)\pi x}{l}.
$$
The data are incompatible with the boundary condition ($\varphi(0)=u_0\ne0$), so part 2 of Theorem 4.2.1 does not apply, and the solution is discontinuous at the corners $(0,0)$ and $(l,0)$; but by part 1 it is smooth for $t>0$, and one can show that $u(x,t)\to u_0$ as $t\to0^+$ for each $0<x<l$.

![Cooling of a rod with initial temperature 1 and ends held at 0 (k = l = 1). The profile is smooth at every t > 0 and quickly approaches the first mode, whose amplitude decays like exp(-π² t) (dashed: first mode only)](./plots/heat-rod-cooling.py)

### 4.2.2. Other Boundary Conditions

Other boundary conditions lead to other eigenvalue problems for $X$, and hence to other expansions; the table of [2.4.12](/2.4.12#sec-12.4.1) lists the most common ones. The choice of series is dictated by the boundary conditions, not by the initial data.

| Boundary conditions | Eigenfunctions $X_n$ | Expansion of the data |
|---|---|---|
| $u(0)=u(l)=0$ (both ends at temperature $0$) | $\sin\frac{n\pi x}{l}$, $n\ge1$ | Fourier sine series |
| $u_x(0)=u_x(l)=0$ (both ends insulated) | $1$, $\cos\frac{n\pi x}{l}$, $n\ge1$ | Fourier cosine series |
| $u(0)=0$, $u_x(l)=0$ | $\sin\frac{(2n-1)\pi x}{2l}$, $n\ge1$ | odd half-integer sine series |
| periodic, $u(-l)=u(l)$, $u_x(-l)=u_x(l)$ (a ring) | $1$, $\cos\frac{n\pi x}{l}$, $\sin\frac{n\pi x}{l}$ | full Fourier series |
| $u(0)=0$, $u_x(l)+hu(l)=0$ (Robin) | $\sin\mu_nx$, $\tan\mu_nl=-\mu_n/h$ | expansion in nonharmonic sines |

**Example 4.2.2 (Insulated Ends)** Solve $u_t=ku_{xx}$, $u_x(0,t)=u_x(l,t)=0$, $u(x,0)=x$.

**Solution** The eigenvalues are $\lambda_n=(n\pi/l)^2$, $n=0,1,2,\dots$, with eigenfunctions $\cos\frac{n\pi x}{l}$, and the solution is $u=\frac{a_0}{2}+\sum_{n\ge1}a_n\mathrm{e}^{-k(n\pi/l)^2t}\cos\frac{n\pi x}{l}$ with the cosine coefficients of $x$ ([Example 9.3.5](/2.2.9#sec-9.3.2) with $\pi$ replaced by $l$): $\frac{a_0}{2}=\frac l2$ and $a_n=\frac{2l((-1)^n-1)}{n^2\pi^2}$. So

$$
u(x,t)=\frac l2-\frac{4l}{\pi^2}\sum_{m=0}^\infty\frac{1}{(2m+1)^2}\,\mathrm{e}^{-k(2m+1)^2\pi^2t/l^2}\cos\frac{(2m+1)\pi x}{l}.
$$
As $t\to+\infty$ the temperature tends to the constant $\frac l2$, the average of the initial temperature. This is conservation of energy: for an insulated rod, $\frac{\mathrm{d}}{\mathrm{d}t}\int_0^lu\,\mathrm{d}x=k\big[u_x\big]_0^l=0$. The zero eigenvalue, absent for Dirichlet conditions, carries exactly this conserved quantity.

**Example 4.2.3 (Heat Exchange at One End)** Let the end $x=0$ be kept at temperature $0$ and let the end $x=l$ exchange heat with surroundings at temperature $0$ according to Newton's law of cooling: $u_x(l,t)+hu(l,t)=0$, $h>0$ (a **Robin boundary condition**). Find the eigenvalues and eigenfunctions.

**Solution** The problem $X''+\lambda X=0$, $X(0)=0$, $X'(l)+hX(l)=0$ is a regular **Sturm–Liouville problem**, so its eigenvalues are real, simple and increase to $+\infty$ ([Theorem 12.5.2](/2.4.12#thm-12.5.2)); by the Rayleigh quotient argument of [2.4.12](/2.4.12#sec-12.5.2) they are nonnegative, and $\lambda=0$ is not an eigenvalue ($X=x$ gives $X'(l)+hX(l)=1+hl\ne0$). For $\lambda=\mu^2>0$, $X=\sin\mu x$, and the second condition gives

$$
\mu\cos\mu l+h\sin\mu l=0,\qquad\text{that is,}\qquad\tan\mu l=-\frac{\mu}{h}.
$$
Graphically, the line $-\mu/h$ meets each branch of $\tan\mu l$ once, so there is exactly one root $\mu_n$ with $(n-\frac12)\pi<\mu_nl<n\pi$, and $\mu_nl-(n-\frac12)\pi\to0$ as $n\to\infty$. For $l=h=1$, numerically, $\mu_1\approx2.0288$, $\mu_2\approx4.9132$, $\mu_3\approx7.9787$. The eigenfunctions $\sin\mu_nx$ are not harmonics of a common frequency, but they are orthogonal on $[0,l]$ by [Theorem 12.5.1](/2.4.12#thm-12.5.1), with $\int_0^l\sin^2\mu_nx\,\mathrm{d}x=\frac l2-\frac{\sin2\mu_nl}{4\mu_n}$, and the solution is $u=\sum c_n\mathrm{e}^{-k\mu_n^2t}\sin\mu_nx$ with $c_n=\int_0^l\varphi\sin\mu_nx\,\mathrm{d}x\big/\int_0^l\sin^2\mu_nx\,\mathrm{d}x$.

## 4.3. The General Method

The examples follow one pattern, which applies whenever the region, the equation and the boundary conditions are compatible with a product structure.

1. Make the boundary conditions homogeneous (§4.4.2).
2. Substitute a product $u=X(x)T(t)$ into the homogeneous equation and separate the variables, with a separation constant $-\lambda$.
3. Solve the eigenvalue problem for $X$ given by the separated equation and the homogeneous boundary conditions: eigenvalues $\lambda_n$ and eigenfunctions $X_n$.
4. Solve the equation for $T$ for each $\lambda_n$.
5. Superpose: $u=\sum_nT_n(t)X_n(x)$.
6. Determine the remaining constants from the initial conditions by the **eigenfunction expansion** of the data.
7. Check the convergence of the series (or interpret the solution as a generalized solution).

Steps 3 and 6 are justified by Sturm–Liouville theory. Consider heat conduction in a nonhomogeneous rod, where the density, specific heat and conductivity depend on $x$. The derivation of [2.5.1](/2.5.1#sec-1.2.2) gives

$$
w(x)u_t=\big(p(x)u_x\big)_x-q(x)u,\qquad0<x<l,
$$
with $w=c_{\mathrm{p}}\rho>0$, $p=\kappa>0$, and $q\ge0$ describing heat loss through the lateral surface. With separated boundary conditions at the two ends, separation of variables gives $T'=-\lambda T$ and the regular Sturm–Liouville problem

$$
-(pX')'+qX=\lambda wX,\qquad\alpha_1X(0)-\alpha_2X'(0)=0,\quad\beta_1X(l)+\beta_2X'(l)=0.
$$
By [Theorems 12.5.1–12.5.3](/2.4.12#sec-12.5.2), its eigenvalues are real and increase to $+\infty$, the eigenfunctions $X_n$ are orthogonal with respect to the weight $w$, and every reasonable initial temperature can be expanded in them. The solution is

$$
u(x,t)=\sum_{n=1}^\infty c_n\mathrm{e}^{-\lambda_nt}X_n(x),\qquad c_n=\frac{\int_0^l\varphi X_nw\,\mathrm{d}x}{\int_0^lX_n^2w\,\mathrm{d}x}.
$$
The vibrating string with variable density works the same way, with $T''=-\lambda T$. Separation of variables thus generalizes the diagonalization of a symmetric matrix: the operator $-(pX')'+qX$ with boundary conditions is "diagonal" in the basis of its eigenfunctions, and in this basis the partial differential equation becomes an uncoupled system of ordinary differential equations, one for each mode.

The method requires that the region be a coordinate rectangle in some coordinate system (an interval, a rectangle, a disk or annulus in polar coordinates, a ball in spherical coordinates) and that the boundary conditions be of the same kind on each side. For other regions, Green's functions ([2.5.8](/2.5.8)) or numerical methods take over.

## 4.4. Nonhomogeneous Problems

### 4.4.1. Eigenfunction Expansion

Consider a rod with internal heat sources:

$$
u_t=ku_{xx}+f(x,t),\qquad u(0,t)=u(l,t)=0,\qquad u(x,0)=\varphi(x).\tag{4.8}
$$
Product solutions are no longer available, but the eigenfunctions of the homogeneous problem still form a basis. Expand the unknown solution at each time in the eigenfunctions,

$$
u(x,t)=\sum_{n=1}^\infty T_n(t)\sin\frac{n\pi x}{l},\qquad T_n(t)=\frac2l\int_0^lu(x,t)\sin\frac{n\pi x}{l}\,\mathrm{d}x,
$$
and let $f_n(t)$ and $\varphi_n$ be the sine coefficients of $f(\cdot,t)$ and $\varphi$. Differentiating $T_n$ under the integral sign, using the equation, and integrating by parts twice (the boundary terms vanish because $u=0$ and $\sin\frac{n\pi x}{l}=0$ at the ends),

$$
T_n'=\frac2l\int_0^l\big(ku_{xx}+f\big)\sin\frac{n\pi x}{l}\,\mathrm{d}x=-k\lambda_nT_n+f_n(t),\qquad T_n(0)=\varphi_n,
$$
with $\lambda_n=(n\pi/l)^2$. Each mode satisfies a first-order linear ordinary differential equation, solved by variation of constants:

$$
T_n(t)=\varphi_n\mathrm{e}^{-k\lambda_nt}+\int_0^t\mathrm{e}^{-k\lambda_n(t-s)}f_n(s)\,\mathrm{d}s.\tag{4.9}
$$
The integral is Duhamel's principle again ([2.5.3](/2.5.3#thm-3.3.1)), now mode by mode. For the string $u_{tt}=c^2u_{xx}+f$ with fixed ends, the same computation gives $T_n''+\omega_n^2T_n=f_n(t)$ with $\omega_n=\frac{n\pi c}{l}$, and

$$
T_n(t)=A_n\cos\omega_nt+B_n\sin\omega_nt+\frac{1}{\omega_n}\int_0^t\sin\omega_n(t-s)\,f_n(s)\,\mathrm{d}s,\tag{4.10}
$$
with $A_n,B_n$ from (4.4).

**Example 4.4.1 (Resonance)** A string with fixed ends, initially at rest in equilibrium, is driven by the force $f=F_0\sin\frac{\pi x}{l}\sin\omega t$. Only the first mode is excited: $f_1=F_0\sin\omega t$, $f_n=0$ for $n\ge2$, and $T_n\equiv0$ for $n\ge2$. If $\omega\ne\omega_1=\frac{\pi c}{l}$, Eq. (4.10) gives

$$
T_1(t)=\frac{F_0}{\omega_1^2-\omega^2}\Big(\sin\omega t-\frac{\omega}{\omega_1}\sin\omega_1t\Big),
$$
which stays bounded. Letting $\omega\to\omega_1$,

$$
T_1(t)=\frac{F_0}{2\omega_1^2}\big(\sin\omega_1t-\omega_1t\cos\omega_1t\big),
$$
whose amplitude grows linearly in $t$: **resonance**. A string, a bridge or a building responds strongly to forcing at one of its natural frequencies $\omega_n$, provided the force has a nonzero component $f_n$ in the corresponding mode; forcing at a frequency that is not a natural frequency produces a bounded response.

### 4.4.2. Nonhomogeneous Boundary Conditions

If the ends of the rod are held at prescribed temperatures, $u(0,t)=g_1(t)$ and $u(l,t)=g_2(t)$, the eigenfunction method cannot be applied directly, because the sum of two solutions does not satisfy the boundary conditions. We first subtract any function satisfying them, for instance the linear interpolation

$$
W(x,t)=g_1(t)+\frac xl\big(g_2(t)-g_1(t)\big).
$$
Then $v=u-W$ satisfies homogeneous boundary conditions and the nonhomogeneous equation

$$
v_t=kv_{xx}+f-W_t,\qquad v(x,0)=\varphi(x)-W(x,0),
$$
which is of the form (4.8). For the wave equation the new source is $f-W_{tt}$. When the boundary values and the source do not depend on time, it is better to subtract the steady state $U(x)$, the solution of $kU''+f=0$ with the boundary values; then $v=u-U$ solves a homogeneous problem.

**Example 4.4.2** Solve $u_t=ku_{xx}$, $u(0,t)=0$, $u(l,t)=u_1$, $u(x,0)=0$ (a cold rod whose right end is suddenly heated to $u_1$).

**Solution** The steady state is $U=\frac{u_1x}{l}$, and $v=u-U$ solves problem (4.6) with $\varphi=-\frac{u_1x}{l}$, whose sine coefficients are $C_n=\frac2l\int_0^l\big(-\frac{u_1x}{l}\big)\sin\frac{n\pi x}{l}\,\mathrm{d}x=\frac{2u_1(-1)^n}{n\pi}$. Hence

$$
u(x,t)=\frac{u_1x}{l}+\frac{2u_1}{\pi}\sum_{n=1}^\infty\frac{(-1)^n}{n}\,\mathrm{e}^{-k(n\pi/l)^2t}\sin\frac{n\pi x}{l}.
$$
The temperature approaches the linear steady state; the deviation decays like $\mathrm{e}^{-k\pi^2t/l^2}$.

## 4.5. The Laplace Equation in a Rectangle and a Disk

### 4.5.1. A Rectangle

Consider the steady temperature in a rectangular plate $0<x<a$, $0<y<b$, with three sides at temperature $0$ and the fourth at a prescribed temperature:

$$
\Delta u=0\ \ \text{in }(0,a)\times(0,b),\qquad u(0,y)=u(a,y)=0,\quad u(x,0)=0,\quad u(x,b)=f(x).\tag{4.11}
$$
Substituting $u=X(x)Y(y)$ gives $\frac{X''}{X}=-\frac{Y''}{Y}=-\lambda$. The homogeneous conditions on the vertical sides give the eigenvalue problem $X''+\lambda X=0$, $X(0)=X(a)=0$, with $X_n=\sin\frac{n\pi x}{a}$ and $\lambda_n=(n\pi/a)^2$. The equation $Y''=\lambda_nY$ with $Y(0)=0$ gives $Y_n=\sinh\frac{n\pi y}{a}$: in the Laplace equation the second variable produces hyperbolic functions instead of exponentials or oscillations. Superposing,

$$
u(x,y)=\sum_{n=1}^\infty c_n\sinh\frac{n\pi y}{a}\sin\frac{n\pi x}{a},\qquad c_n\sinh\frac{n\pi b}{a}=\frac2a\int_0^af(x)\sin\frac{n\pi x}{a}\,\mathrm{d}x.\tag{4.12}
$$
For example, $f(x)=\sin\frac{\pi x}{a}$ gives the single term $u=\frac{\sinh(\pi y/a)}{\sinh(\pi b/a)}\sin\frac{\pi x}{a}$. Since $\frac{\sinh(n\pi y/a)}{\sinh(n\pi b/a)}\le\mathrm{e}^{-n\pi(b-y)/a}$ for $0\le y\le b$, the series converges extremely fast inside the rectangle, and its sum is infinitely differentiable there, for any bounded integrable $f$: harmonic functions are smooth in the interior. A Dirichlet problem with nonzero data on all four sides is the sum of four problems of the form (4.11), each with data on one side; this is the superposition principle applied to the boundary data. By the uniqueness theorem for the Dirichlet problem ([2.2.14](/2.2.14#thm-14.5.3)), the solution obtained in this way is the only one.

### 4.5.2. A Disk

For the Dirichlet problem in the disk $r<a$, we use **polar coordinates**, in which ([2.2.14](/2.2.14#sec-14.6))

$$
\Delta u=u_{rr}+\frac1ru_r+\frac{1}{r^2}u_{\theta\theta}.
$$
Substituting $u=R(r)\Theta(\theta)$ and multiplying by $\frac{r^2}{R\Theta}$ gives

$$
\frac{r^2R''+rR'}{R}=-\frac{\Theta''}{\Theta}=\lambda.
$$
The "boundary condition" for $\Theta$ is that $u$ be a single-valued function in the plane, so $\Theta$ must be $2\pi$-periodic: the periodic eigenvalue problem $\Theta''+\lambda\Theta=0$ has the eigenvalues $\lambda=n^2$ ($n=0,1,2,\dots$) with eigenfunctions $1$ and $\cos n\theta$, $\sin n\theta$. The equation for $R$ is $r^2R''+rR'-n^2R=0$, an Euler equation whose solutions are $r^n$ and $r^{-n}$ for $n\ge1$, and $1$ and $\ln r$ for $n=0$. The second condition hidden in the problem is that $u$ be bounded at the center of the disk, which excludes $r^{-n}$ and $\ln r$. So

$$
u(r,\theta)=\frac{a_0}{2}+\sum_{n=1}^\infty r^n\big(a_n\cos n\theta+b_n\sin n\theta\big).\tag{4.13}
$$
The boundary condition $u(a,\theta)=f(\theta)$ is a Fourier series for $f$ on $[0,2\pi]$, so $a^na_n$ and $a^nb_n$ are the Fourier coefficients of $f$:

$$
a_n=\frac{1}{\pi a^n}\int_0^{2\pi}f(\varphi)\cos n\varphi\,\mathrm{d}\varphi,\qquad b_n=\frac{1}{\pi a^n}\int_0^{2\pi}f(\varphi)\sin n\varphi\,\mathrm{d}\varphi.
$$
In terms of the complex variable $z=x+\mathrm{i}y=r\mathrm{e}^{\mathrm{i}\theta}$, the functions $r^n\cos n\theta$ and $r^n\sin n\theta$ are $\operatorname{Re}z^n$ and $\operatorname{Im}z^n$: Eq. (4.13) is the real part of a power series in $z$, in keeping with the relation between harmonic and analytic functions ([2.3](/2.3)). For the exterior of the disk, $r>a$, one keeps $r^{-n}$ instead of $r^n$ (boundedness at infinity), and for an annulus all four kinds of solutions are needed.

The series (4.13) can be summed in closed form.

**Theorem 4.5.1 (Poisson Integral Formula)** Let $f$ be continuous and $2\pi$-periodic. For $0\le r<a$, the sum of the series (4.13) is

$$
u(r,\theta)=\frac{1}{2\pi}\int_0^{2\pi}\frac{a^2-r^2}{a^2-2ar\cos(\theta-\varphi)+r^2}\,f(\varphi)\,\mathrm{d}\varphi.\tag{4.14}
$$
The function $u$ is harmonic in the disk and extends continuously to the closed disk with $u=f$ on the boundary circle.

**Proof** (Of the formula.) Substituting the coefficients into Eq. (4.13), with $\rho=r/a<1$,

$$
u(r,\theta)=\frac1{2\pi}\int_0^{2\pi}f(\varphi)\Big[1+2\sum_{n=1}^\infty\rho^n\cos n(\theta-\varphi)\Big]\mathrm{d}\varphi;
$$
the interchange of summation and integration is allowed because the series converges uniformly in $\varphi$ (its terms are bounded by $2\rho^n$). By **Euler's formula**, with $\alpha=\theta-\varphi$, the bracket is the real part of a geometric series:

$$
1+2\sum_{n=1}^\infty\rho^n\cos n\alpha=\operatorname{Re}\Big(1+2\sum_{n=1}^\infty\big(\rho\mathrm{e}^{\mathrm{i}\alpha}\big)^n\Big)=\operatorname{Re}\frac{1+\rho\mathrm{e}^{\mathrm{i}\alpha}}{1-\rho\mathrm{e}^{\mathrm{i}\alpha}}=\frac{1-\rho^2}{1-2\rho\cos\alpha+\rho^2},
$$
where the last step multiplies the numerator and denominator by $1-\rho\mathrm{e}^{-\mathrm{i}\alpha}$. Multiplying the numerator and denominator by $a^2$ gives Eq. (4.14). The proof that $u\to f$ at the boundary is given in [2.5.8](/2.5.8), where the formula is derived again from the Green's function of the disk. $\square$

The kernel in Eq. (4.14) is positive, has integral $1$ (take $f\equiv1$, for which $u\equiv1$), and concentrates at $\varphi=\theta$ as $r\to a$; so $u(r,\theta)$ is a weighted average of the boundary values, with most of the weight on the nearby part of the boundary. At the center, $r=0$, all weights are equal:

$$
u(0)=\frac{1}{2\pi}\int_0^{2\pi}f(\varphi)\,\mathrm{d}\varphi,
$$
the mean value property of harmonic functions: the value at the center of a disk is the average over its boundary. From it follows the maximum principle, the subject of [2.5.8](/2.5.8).

**Example 4.5.1** The upper half of the boundary of the disk $r<a$ is kept at temperature $1$, the lower half at $0$: $f(\theta)=1$ for $0<\theta<\pi$ and $0$ for $\pi<\theta<2\pi$. Find the steady temperature.

**Solution** The Fourier coefficients of $f$ are $\frac{a_0}{2}=\frac12$, $a^na_n=0$, and $a^nb_n=\frac1\pi\int_0^\pi\sin n\varphi\,\mathrm{d}\varphi=\frac{1-(-1)^n}{n\pi}$, which is $\frac{2}{n\pi}$ for odd $n$. So

$$
u(r,\theta)=\frac12+\frac2\pi\sum_{m=0}^\infty\frac{1}{2m+1}\Big(\frac ra\Big)^{2m+1}\sin(2m+1)\theta=\frac12+\frac1\pi\arctan\frac{2ar\sin\theta}{a^2-r^2},
$$
where the series was summed using $\sum_{m\ge0}\frac{\rho^{2m+1}\sin(2m+1)\theta}{2m+1}=\frac12\arctan\frac{2\rho\sin\theta}{1-\rho^2}$ (the imaginary part of $\frac12\log\frac{1+\rho\mathrm{e}^{\mathrm{i}\theta}}{1-\rho\mathrm{e}^{\mathrm{i}\theta}}$). The isotherms $u=\text{const}$ are arcs of circles through the two points $(\pm a,0)$ where the boundary temperature jumps; the temperature along the horizontal diameter is $\frac12$.

![Steady temperature in a disk whose upper boundary half is held at 1 and lower half at 0: the isotherms are circular arcs through the points (±a, 0) where the boundary data jump](./plots/disk-dirichlet.py)

## 4.6. Convergence and Regularity

The convergence of the series produced by separation of variables reflects the qualitative behavior of the three types of equations ([2.5.1](/2.5.1#sec-1.5.3)).

- Smoothness of a function corresponds to fast decay of its Fourier coefficients: if the periodic extension is $C^k$, integrating by parts $k$ times shows that the coefficients are $o(n^{-k})$; a jump gives coefficients of order $1/n$ and the **Gibbs phenomenon** near the jump. The periodic extension is the relevant object, so the compatibility of the data with the boundary conditions matters as much as their smoothness inside the interval.
- For the heat equation, the factors $\mathrm{e}^{-k\lambda_nt}$ overwhelm any growth of $n$, so the solution is infinitely differentiable at every $t>0$, whatever the initial data (Theorem 4.2.1). The initial values are attained in the sense of mean-square convergence for square-integrable data, and pointwise at points where the data are continuous and piecewise smooth.
- For the wave equation, the factors $\cos\omega_nt$, $\sin\omega_nt$ do not decay, so the solution is exactly as smooth as the data, and twice differentiable data are not quite enough for a classical solution (Theorem 4.1.1 needs $\varphi\in C^3$ with compatibility conditions). Singularities persist and travel, in agreement with [2.5.3](/2.5.3#sec-3.1.3).
- For the Laplace equation, the factors $(r/a)^n$ or $\frac{\sinh(n\pi y/a)}{\sinh(n\pi b/a)}$ decay geometrically in the interior, so the solution is infinitely differentiable (indeed real analytic) inside the region for any integrable boundary data.

## Summary

| Problem | Eigenfunctions | Time / second-variable factor | Solution |
|---|---|---|---|
| String, fixed ends | $\sin\frac{n\pi x}{l}$ | $\cos\omega_nt$, $\sin\omega_nt$, $\omega_n=\frac{n\pi c}{l}$ | standing waves, Eq. (4.3) |
| Rod, ends at $0$ | $\sin\frac{n\pi x}{l}$ | $\mathrm{e}^{-k(n\pi/l)^2t}$ | Eq. (4.7); smoothing, exponential decay |
| Rod, insulated ends | $1$, $\cos\frac{n\pi x}{l}$ | $\mathrm{e}^{-k(n\pi/l)^2t}$ | tends to the average of the data |
| Robin end | $\sin\mu_nx$, $\tan\mu_nl=-\mu_n/h$ | $\mathrm{e}^{-k\mu_n^2t}$ | Sturm–Liouville expansion |
| Rectangle, Laplace | $\sin\frac{n\pi x}{a}$ | $\sinh\frac{n\pi y}{a}$ | Eq. (4.12) |
| Disk, Laplace | $1$, $\cos n\theta$, $\sin n\theta$ | $r^n$ | Eq. (4.13), Poisson integral formula (4.14) |

- Separation of variables turns a linear homogeneous problem on a product region into an eigenvalue problem in one variable and ordinary differential equations in the other; the data are matched by eigenfunction expansions, justified by Sturm–Liouville theory.
- Nonhomogeneous equations are solved mode by mode (Duhamel's principle for each $T_n$); nonhomogeneous boundary conditions are first removed by subtracting a function that satisfies them, preferably the steady state.
- Forcing at a natural frequency produces resonance; the zero eigenvalue of the Neumann problem carries the conserved total heat.
