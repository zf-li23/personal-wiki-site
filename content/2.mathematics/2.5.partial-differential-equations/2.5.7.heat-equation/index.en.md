---
title: The Heat Equation
---

The **heat equation** $u_t=k\Delta u$, with the diffusivity $k>0$ ([2.5.1](/2.5.1)), governs every process in which a quantity spreads by random local motion: heat in a solid, a solute in a solvent, a population of moving organisms, the probability density of a Brownian particle. Its solutions behave very differently from those of the **wave equation** ([2.5.3](/2.5.3)). Heat spreads instantly to the whole space, but the amount arriving far away is tiny; rough initial data become smooth immediately; time has a direction, since the equation cannot in general be solved backward; and the solution is controlled by its values on the "parabolic boundary" through a maximum principle.

In [2.5.6](/2.5.6) the Fourier transform produced the heat kernel and the solution formula on the line. This chapter puts these on a rigorous footing in $\mathbb{R}^n$ (§7.1), proves the maximum principle and uses it, together with the energy method, to obtain uniqueness and stability on bounded domains (§7.2), solves problems on a half-line by reflection (§7.3) and nonhomogeneous problems by Duhamel's principle (§7.4), and finally explains diffusion probabilistically and introduces reaction-diffusion equations, the basic models of spatial patterns in biology (§7.5, continued in [Ecology](/7.19) and [Developmental Biology](/7.5)). Problems on bounded intervals by series were treated in [2.5.4](/2.5.4) and [2.5.5](/2.5.5).

## 7.1. The Heat Kernel

### 7.1.1. The Fundamental Solution

The heat kernel can also be found without the Fourier transform, from symmetry. If $u(x,t)$ solves $u_t=k u_{xx}$, so does $u(\lambda x,\lambda^2t)$ for every $\lambda>0$: space scales like the square root of time. Moreover the total heat $\int u\,\mathrm{d}x$ is conserved. A solution that describes a unit amount of heat released at the origin should therefore have the self-similar form $u=t^{-1/2}v(\eta)$, $\eta=x/\sqrt t$, which keeps $\int u\,\mathrm{d}x=\int v\,\mathrm{d}\eta$ constant. Substituting,

$$
u_t=-\frac{1}{2t^{3/2}}\big(v+\eta v'\big),\qquad u_{xx}=\frac{1}{t^{3/2}}v'',
$$
so $k v''+\frac12(\eta v)'=0$, that is, $k v'+\frac12\eta v=C$. For a solution decaying at infinity $C=0$, and $v=A\mathrm{e}^{-\eta^2/(4k)}$. Normalizing the total heat to 1 with the **Gaussian integral** gives $A=(4\pi k)^{-1/2}$, which is the heat kernel (6.8) of [2.5.6](/2.5.6). In $\mathbb{R}^n$ the Laplacian is a sum of second derivatives in separate variables, and the product of one-dimensional heat kernels in $x_1,\dots,x_n$ solves the heat equation.

**Definition 7.1.1 (Fundamental Solution of the Heat Equation)** The function

$$
\Phi(x,t)=\frac{1}{(4\pi k t)^{n/2}}\exp\Big(-\frac{\lvert x\rvert^2}{4k t}\Big),\qquad x\in\mathbb{R}^n,\ t>0,\tag{7.1}
$$
is called the **fundamental solution** of the heat equation, or the **heat kernel**.

**Theorem 7.1.1** The heat kernel has the following properties.

1. $\Phi\in C^\infty(\mathbb{R}^n\times(0,\infty))$ and $\Phi_t=k\Delta\Phi$;
2. $\Phi>0$ and $\displaystyle\int_{\mathbb{R}^n}\Phi(x,t)\,\mathrm{d}x=1$ for every $t>0$;
3. For every $\delta>0$, $\displaystyle\int_{\lvert x\rvert\ge\delta}\Phi(x,t)\,\mathrm{d}x\to0$ as $t\to0^+$;
4. (Semigroup property) $\Phi(\cdot,t)*\Phi(\cdot,s)=\Phi(\cdot,t+s)$ for $t,s>0$.

**Proof** 1: Since $\ln\Phi=-\frac n2\ln(4\pi k t)-\frac{\lvert x\rvert^2}{4k t}$,

$$
\Phi_t=\Phi\Big(\frac{\lvert x\rvert^2}{4k t^2}-\frac{n}{2t}\Big),\qquad\partial_i\Phi=-\frac{x_i}{2k t}\Phi,\qquad\partial_i^2\Phi=\Phi\Big(\frac{x_i^2}{4k^2t^2}-\frac1{2k t}\Big),
$$
and summing over $i$ gives $k\Delta\Phi=\Phi\big(\frac{\lvert x\rvert^2}{4k t^2}-\frac n{2t}\big)=\Phi_t$.

2 and 3: Substitute $x=\sqrt{4k t}\,z$. Then $\int_{\lvert x\rvert\ge\delta}\Phi\,\mathrm{d}x=\pi^{-n/2}\int_{\lvert z\rvert\ge\delta/\sqrt{4k t}}\mathrm{e}^{-\lvert z\rvert^2}\,\mathrm{d}z$. For $\delta=0$ this equals 1 by the Gaussian integral; for $\delta>0$ it is the tail of a convergent integral whose lower limit tends to infinity as $t\to0^+$.

4: By the $n$-dimensional version of (6.4) ([2.5.6](/2.5.6#sec-6.2.5)), $\hat\Phi(\xi,t)=\mathrm{e}^{-k\lvert\xi\rvert^2t}$. By the **convolution theorem** the transform of the left side is $\mathrm{e}^{-k\lvert\xi\rvert^2t}\mathrm{e}^{-k\lvert\xi\rvert^2s}=\hat\Phi(\xi,t+s)$, and both sides are continuous and absolutely integrable, so they coincide by uniqueness (Corollary 6.3.1). $\square$

Properties 2 and 3 say that $\Phi(\cdot,t)$ is an approximate identity as $t\to0^+$ (Lemma 6.3.1 with $\varepsilon=\sqrt t$): the initial datum of the fundamental solution is the **Dirac delta function**, a unit point source of heat. Property 4 says that diffusing for time $t$ and then for time $s$ is the same as diffusing for time $t+s$.

![Left: the heat kernel at four times; it keeps total mass 1 while its width grows like sqrt(t). Right: a rectangular initial temperature is smoothed instantly and spreads out](./plots/heat-kernel.py)

### 7.1.2. Solution of the Cauchy Problem

**Theorem 7.1.2** Let $\varphi$ be continuous and bounded on $\mathbb{R}^n$, and define

$$
u(x,t)=\int_{\mathbb{R}^n}\Phi(x-y,t)\,\varphi(y)\,\mathrm{d}y=\frac{1}{(4\pi k t)^{n/2}}\int_{\mathbb{R}^n}\mathrm{e}^{-\lvert x-y\rvert^2/(4k t)}\varphi(y)\,\mathrm{d}y,\qquad t>0.\tag{7.2}
$$
Then

1. $u\in C^\infty(\mathbb{R}^n\times(0,\infty))$ and $u_t=k\Delta u$ for $t>0$;
2. $u(x,t)\to\varphi(x_0)$ as $(x,t)\to(x_0,0^+)$, for every $x_0\in\mathbb{R}^n$;
3. $\inf\varphi\le u\le\sup\varphi$.

Hence $u$, extended by $u(x,0)=\varphi(x)$, is a solution of the Cauchy problem $u_t=k\Delta u$, $u(x,0)=\varphi(x)$, continuous on $\mathbb{R}^n\times[0,\infty)$.

**Proof** 1: Every partial derivative of $\Phi(x-y,t)$ with respect to $x$ and $t$ is $\Phi(x-y,t)$ times a polynomial in $x-y$ and $1/t$. For $\lvert x\rvert\le A$ and $t_0\le t\le T$ (with $0<t_0<T$) it is therefore bounded by $C(1+\lvert y\rvert^m)\mathrm{e}^{-(\lvert y\rvert-A)^2/(4k T)}$ for $\lvert y\rvert\ge A$, an integrable function of $y$; since $\varphi$ is bounded, the differentiated integrals converge uniformly on this set. Hence **differentiation under the integral sign** is allowed to all orders, and $u_t-k\Delta u=\int(\Phi_t-k\Delta\Phi)(x-y,t)\varphi(y)\,\mathrm{d}y=0$ by Theorem 7.1.1.

2: Let $\lvert\varphi\rvert\le M$ and $\varepsilon>0$, and choose $\delta>0$ with $\lvert\varphi(y)-\varphi(x_0)\rvert<\varepsilon$ for $\lvert y-x_0\rvert<\delta$. By part 2 of Theorem 7.1.1,

$$
\lvert u(x,t)-\varphi(x_0)\rvert\le\int_{\mathbb{R}^n}\Phi(x-y,t)\,\lvert\varphi(y)-\varphi(x_0)\rvert\,\mathrm{d}y.
$$
Let $\lvert x-x_0\rvert<\delta/2$. On $\lvert y-x_0\rvert<\delta$ the integrand is less than $\varepsilon\Phi$, which contributes at most $\varepsilon$. On $\lvert y-x_0\rvert\ge\delta$ we have $\lvert x-y\rvert\ge\delta/2$, so this part contributes at most $2M\int_{\lvert z\rvert\ge\delta/2}\Phi(z,t)\,\mathrm{d}z$, which is less than $\varepsilon$ for small $t$ by part 3 of Theorem 7.1.1.

3: $u(x,t)$ is an average of the values of $\varphi$ with the positive weight $\Phi(x-\cdot,t)$ of total mass 1. $\square$

Formula (7.2) is sometimes called the Poisson formula for the heat equation. Bounded solutions of the Cauchy problem are unique, so (7.2) is *the* bounded solution. Without a growth condition uniqueness fails: Tychonoff constructed a solution on $\mathbb{R}\times(0,\infty)$ that is not identically zero, tends to $0$ as $t\to0^+$, and grows faster than $\mathrm{e}^{ax^2}$ for every $a$. Uniqueness holds in the class $\lvert u(x,t)\rvert\le M\mathrm{e}^{a\lvert x\rvert^2}$ (stated without proof); physically unreasonable solutions are excluded by such a condition.

### 7.1.3. Qualitative Properties

Formula (7.2) displays the characteristic features of diffusion.

1. Infinite speed of propagation: if $\varphi\ge0$ and $\varphi\not\equiv0$, then $u(x,t)>0$ for all $x$ and all $t>0$, because $\Phi>0$ everywhere. Heat released in a small region is felt immediately at any distance, although in an amount of order $\mathrm{e}^{-\lvert x\rvert^2/(4k t)}$. The heat equation is an idealization that ignores the finite speed of the underlying molecular motion; on macroscopic scales the error is negligible.
2. Smoothing: the solution is infinitely differentiable for $t>0$ even if $\varphi$ is only bounded and continuous (or piecewise continuous). In Fourier terms, each frequency is multiplied by $\mathrm{e}^{-k\lvert\xi\rvert^2t}$, which kills high frequencies at once.
3. Decay: if $\varphi$ is absolutely integrable, then $\lvert u(x,t)\rvert\le\sup_y\Phi(y,t)\int\lvert\varphi\rvert=(4\pi k t)^{-n/2}\int\lvert\varphi\rvert$, while the total heat $\int u\,\mathrm{d}x=\int\varphi\,\mathrm{d}x$ is conserved: the heat spreads over a region of diameter of order $\sqrt{k t}$.
4. Irreversibility: the backward problem is ill-posed in the sense of Hadamard ([2.5.1](/2.5.1)). On the line, the function $u_n(x,t)=\frac1n\mathrm{e}^{k n^2(T-t)}\sin nx$ solves the heat equation and has the final value $u_n(x,T)=\frac1n\sin nx$, which tends to $0$ uniformly as $n\to\infty$, while its value at $t=0$ has amplitude $\frac1n\mathrm{e}^{k n^2T}\to\infty$. Arbitrarily small changes in the present temperature correspond to arbitrarily large changes in the past one: the information in fine details is destroyed by diffusion.

**Example 7.1.1** Let $n=1$ and $\varphi(x)=\mathrm{e}^{-x^2/(2\sigma^2)}$. Then $\hat\varphi=\sigma\sqrt{2\pi}\,\mathrm{e}^{-\sigma^2\xi^2/2}$ by (6.4), and $\hat u=\hat\varphi\,\mathrm{e}^{-k\xi^2t}=\sigma\sqrt{2\pi}\,\mathrm{e}^{-(\sigma^2+2k t)\xi^2/2}$. Inverting with (6.4) again,

$$
u(x,t)=\frac{\sigma}{\sqrt{\sigma^2+2k t}}\exp\Big(-\frac{x^2}{2(\sigma^2+2k t)}\Big).
$$
A Gaussian profile stays Gaussian; its variance grows linearly, $\sigma^2\mapsto\sigma^2+2k t$, and its height decreases so that the area is conserved. In probabilistic terms (§7.5), convolving with $\Phi(\cdot,t)$ adds an independent normal variable of variance $2k t$.

## 7.2. The Maximum Principle

### 7.2.1. The Weak Maximum Principle

On a bounded domain the temperature inside a body over a time interval cannot exceed the larger of the initial temperatures and the temperatures imposed on the boundary: heat flows from hot to cold and does not create new extremes.

Let $\Omega\subset\mathbb{R}^n$ be a bounded region and $T>0$. Write $Q_T=\Omega\times(0,T]$ for the space-time cylinder; its closure is $\bar Q_T=\bar\Omega\times[0,T]$.

**Definition 7.2.1 (Parabolic Boundary)** The set

$$
\Gamma_T=\big(\bar\Omega\times\{0\}\big)\cup\big(\partial\Omega\times[0,T]\big)
$$
is called the **parabolic boundary** of $Q_T$: the bottom and the lateral surface of the cylinder, without its top $\Omega\times\{T\}$.

These are exactly the parts of the boundary where data are prescribed for the heat equation (initial and boundary conditions); no condition is imposed at the final time.

**Theorem 7.2.1 (Weak Maximum Principle)** Let $u\in C(\bar Q_T)$ have continuous derivatives $u_t$, $u_{x_ix_j}$ in $Q_T$, and suppose $u_t-k\Delta u\le0$ in $Q_T$. Then

$$
\max_{\bar Q_T}u=\max_{\Gamma_T}u.
$$
Similarly, if $u_t-k\Delta u\ge0$, then $\min_{\bar Q_T}u=\min_{\Gamma_T}u$. In particular, solutions of the heat equation attain their maximum and minimum on the parabolic boundary.

**Proof** First suppose the strict inequality $v_t-k\Delta v<0$ holds in $Q_T$ for a function $v$ with the same regularity, and let $v$ attain its maximum over the compact set $\bar Q_T$ at $(x_0,t_0)$. If $(x_0,t_0)\notin\Gamma_T$, then $x_0\in\Omega$ and $0<t_0\le T$. Since $x\mapsto v(x,t_0)$ has an interior maximum at $x_0$, every $v_{x_ix_i}(x_0,t_0)\le0$, so $\Delta v(x_0,t_0)\le0$. Since $t\mapsto v(x_0,t)$ on $(0,t_0]$ is maximal at $t_0$, $v_t(x_0,t_0)\ge0$ (with equality if $t_0<T$, and as a one-sided derivative if $t_0=T$). Then $v_t-k\Delta v\ge0$ at $(x_0,t_0)$, a contradiction. Hence $\max_{\bar Q_T}v=\max_{\Gamma_T}v$.

In general, let $\varepsilon>0$ and $v=u+\varepsilon\lvert x\rvert^2$. Then $v_t-k\Delta v=u_t-k\Delta u-2nk\varepsilon<0$. With $R=\max_{x\in\bar\Omega}\lvert x\rvert$,

$$
\max_{\bar Q_T}u\le\max_{\bar Q_T}v=\max_{\Gamma_T}v\le\max_{\Gamma_T}u+\varepsilon R^2,
$$
and letting $\varepsilon\to0$ gives $\max_{\bar Q_T}u\le\max_{\Gamma_T}u$; the reverse inequality is trivial. The statement about the minimum follows by applying this to $-u$. $\square$

The strict-inequality trick is needed because at an interior maximum we only know $\Delta u\le0$ and $u_t\ge0$, which is consistent with $u_t=k\Delta u$ when both vanish. A stronger statement also holds (stated without proof): if $\Omega$ is connected and a solution attains its maximum over $\bar Q_T$ at a point $(x_0,t_0)$ with $x_0\in\Omega$, $0<t_0\le T$, then $u$ is constant on $\bar\Omega\times[0,t_0]$ (the strong maximum principle). The future cannot influence the past, so nothing is asserted for $t>t_0$.

### 7.2.2. Uniqueness, Stability and Comparison

Consider the initial-boundary value problem

$$
\begin{cases}
u_t-k\Delta u=f(x,t),&(x,t)\in Q_T,\\
u=g(x,t),&x\in\partial\Omega,\ 0\le t\le T,\\
u(x,0)=\varphi(x),&x\in\bar\Omega.
\end{cases}\tag{7.3}
$$

**Corollary 7.2.1 (Uniqueness and Stability)** Problem (7.3) has at most one solution $u\in C(\bar Q_T)$ with continuous $u_t$, $u_{x_ix_j}$ in $Q_T$. If $u_1,u_2$ are the solutions for the data $(f,g_1,\varphi_1)$ and $(f,g_2,\varphi_2)$, then

$$
\max_{\bar Q_T}\lvert u_1-u_2\rvert\le\max\Big\{\max_{\bar\Omega}\lvert\varphi_1-\varphi_2\rvert,\ \max_{\partial\Omega\times[0,T]}\lvert g_1-g_2\rvert\Big\}.
$$

**Proof** The difference $w=u_1-u_2$ satisfies $w_t-k\Delta w=0$, so by Theorem 7.2.1 both $w$ and $-w$ are bounded on $\bar Q_T$ by their maxima on $\Gamma_T$, where $w$ equals $\varphi_1-\varphi_2$ or $g_1-g_2$. This is the estimate; for equal data it gives $w\equiv0$. $\square$

Together with the existence of solutions (by series in [2.5.4](/2.5.4), or in general), this shows that the Dirichlet problem for the heat equation is well-posed: small errors in the initial and boundary temperatures produce small errors in the solution, uniformly in space and time. The same argument applied to $v-u$ gives a comparison principle.

**Corollary 7.2.2 (Comparison Principle)** If $u_t-k\Delta u\le v_t-k\Delta v$ in $Q_T$ and $u\le v$ on $\Gamma_T$, then $u\le v$ in $\bar Q_T$.

**Example 7.2.1** Let $u$ solve $u_t=u_{xx}$ on $(0,\pi)$, $u(0,t)=u(\pi,t)=0$, $u(x,0)=x(\pi-x)$. Estimate $u$ without solving.

**Solution** The function $v=A\mathrm{e}^{-t}\sin x$ solves the same equation and vanishes at $x=0,\pi$. The ratio $\frac{x(\pi-x)}{\sin x}$ decreases from $\pi$ (its limit at $x=0^+$) to $\frac{\pi^2}4$ at $x=\frac\pi2$ and is symmetric about $\frac\pi2$, so $\frac{\pi^2}4\sin x\le x(\pi-x)\le\pi\sin x$ on $[0,\pi]$. By Corollary 7.2.2,

$$
\frac{\pi^2}{4}\mathrm{e}^{-t}\sin x\le u(x,t)\le\pi\,\mathrm{e}^{-t}\sin x.
$$
The exact solution $u=\sum_{n\text{ odd}}\frac{8}{\pi n^3}\mathrm{e}^{-n^2t}\sin nx$ has leading coefficient $\frac8\pi\approx2.55$, which indeed lies between $\frac{\pi^2}4\approx2.47$ and $\pi\approx3.14$.

### 7.2.3. The Energy Method

For the Neumann problem the maximum principle does not directly control the boundary values, but an integral identity does. Let $u$ solve $u_t=k\Delta u$ in $\Omega\times(0,T]$ with either $u=0$ or $\frac{\partial u}{\partial\boldsymbol{n}}=0$ on $\partial\Omega$, and let

$$
E(t)=\int_\Omega u(x,t)^2\,\mathrm{d}x.
$$
Differentiating under the integral sign and applying **Green's first identity**,

$$
E'(t)=2\int_\Omega uu_t\,\mathrm{d}x=2k\int_\Omega u\,\Delta u\,\mathrm{d}x=2k\oint_{\partial\Omega}u\frac{\partial u}{\partial\boldsymbol{n}}\,\mathrm{d}S-2k\int_\Omega\lvert\nabla u\rvert^2\,\mathrm{d}x=-2k\int_\Omega\lvert\nabla u\rvert^2\,\mathrm{d}x\le0.
$$
Hence $E(t)\le E(0)$. Applied to the difference of two solutions with the same data, this proves uniqueness for the Dirichlet and the Neumann problem (and for Robin conditions $\frac{\partial u}{\partial\boldsymbol{n}}+\beta u=0$ with $\beta\ge0$), and stability in the mean-square sense. For the Dirichlet problem the decay can be quantified: the first Dirichlet eigenvalue $\lambda_1$ of $-\Delta$ ([2.5.5](/2.5.5#sec-5.1.2)) is the minimum of the quotient $\int\lvert\nabla w\rvert^2/\int w^2$ over functions vanishing on $\partial\Omega$ (stated without proof), so $E'\le-2k\lambda_1E$ and

$$
E(t)\le E(0)\,\mathrm{e}^{-2k\lambda_1t},
$$
in agreement with the slowest mode $\mathrm{e}^{-k\lambda_1t}$ of the series solution.

## 7.3. Problems on the Half-Line

### 7.3.1. The Method of Reflection

On the half-line $x>0$ with a condition at $x=0$, we extend the initial datum to the whole line so that the condition holds automatically, as for the wave equation ([2.5.3](/2.5.3)).

**Theorem 7.3.1** Let $\varphi$ be bounded and continuous on $[0,\infty)$ and $\Phi$ the one-dimensional heat kernel. For $t>0$ and $x\ge0$ let

$$
u_{\mathrm{D}}(x,t)=\int_0^\infty\big[\Phi(x-y,t)-\Phi(x+y,t)\big]\varphi(y)\,\mathrm{d}y,\qquad u_{\mathrm{N}}(x,t)=\int_0^\infty\big[\Phi(x-y,t)+\Phi(x+y,t)\big]\varphi(y)\,\mathrm{d}y.
$$
Then $u_{\mathrm{D}}$ and $u_{\mathrm{N}}$ solve $u_t=k u_{xx}$ for $x>0$, $t>0$, tend to $\varphi(x_0)$ as $(x,t)\to(x_0,0^+)$ for every $x_0>0$, and satisfy $u_{\mathrm{D}}(0,t)=0$ and $\partial_xu_{\mathrm{N}}(0,t)=0$ for $t>0$, respectively.

**Proof** Let $\varphi_{\mathrm{odd}}$ be the odd extension of $\varphi$ to $\mathbb{R}$ (with any value at $0$). Splitting $\int_{\mathbb{R}}$ at $0$ and substituting $y\mapsto-y$ on $(-\infty,0)$ shows $u_{\mathrm{D}}(x,t)=\int_{\mathbb{R}}\Phi(x-y,t)\varphi_{\mathrm{odd}}(y)\,\mathrm{d}y$. Theorem 7.1.2 (whose proof of parts 1 and 2 only uses boundedness of $\varphi$ and continuity at $x_0$) gives the equation and the initial condition. Since $\Phi$ is even in $x$, the substitution $y\mapsto-y$ shows that $u_{\mathrm{D}}(\cdot,t)$ is odd, hence vanishes at $x=0$. For $u_{\mathrm{N}}$ use the even extension; $u_{\mathrm{N}}(\cdot,t)$ is then even and smooth, so its derivative vanishes at $0$. $\square$

In other words, the solution on the half-line with $u(0,t)=0$ is the restriction of the solution on the line with odd data: an image source of opposite sign at $-y$ absorbs exactly the heat flowing through $x=0$. The same idea gives Green's functions of the Laplace equation by the method of images ([2.5.8](/2.5.8)).

**Example 7.3.1** A half-infinite rod at uniform temperature $1$ has its end held at $0$ from time $0$ on. With $\varphi\equiv1$,

$$
u(x,t)=\int_0^\infty\Phi(x-y,t)\,\mathrm{d}y-\int_0^\infty\Phi(x+y,t)\,\mathrm{d}y=\frac12\Big(1+\operatorname{erf}\frac{x}{2\sqrt{k t}}\Big)-\frac12\Big(1-\operatorname{erf}\frac{x}{2\sqrt{k t}}\Big)=\operatorname{erf}\Big(\frac{x}{2\sqrt{k t}}\Big),
$$
with the **error function** of [2.5.6](/2.5.6). This is complementary to Example 6.5.3: there the rod was cold and its end hot, and $T_0-T_0\operatorname{erfc}=T_0\operatorname{erf}$. The temperature gradient at the end is $u_x(0,t)=\frac1{\sqrt{\pi k t}}$. In 1862 Kelvin applied this formula to the cooling of the Earth: from the observed increase of temperature with depth near the surface, an initial temperature of a few thousand degrees and the conductivity of rock, he estimated that $t$ is of the order of $10^8$ years. The estimate is far too small, because it ignores heat produced by radioactivity (unknown at the time) and convection in the mantle.

![Reflection: the solution on x > 0 with u(0, t) = 0 and u(x, 0) = 1 is the restriction of the whole-line solution with odd initial data, u = erf(x / (2 sqrt(t)))](./plots/half-line-reflection.py)

### 7.3.2. Time-Dependent Boundary Data

If the boundary temperature varies, $u(0,t)=h(t)$ with $u(x,0)=0$, the Laplace transform gives the formula at the end of Example 6.5.3:

$$
u(x,t)=\int_0^th(\tau)\,K(x,t-\tau)\,\mathrm{d}\tau,\qquad K(x,t)=\frac{x}{2\sqrt{\pi k}\,t^{3/2}}\mathrm{e}^{-x^2/(4k t)}=-2k\,\partial_x\Phi(x,t).
$$
The kernel $K$ is the response to a short heat pulse at the end. Combined with Theorem 7.3.1 by superposition, this solves the half-line problem with arbitrary initial and boundary data. A periodic boundary temperature $h=\cos\omega t$ (the daily or annual cycle at the Earth's surface) produces, after transients have died out, the damped wave $\mathrm{e}^{-x\sqrt{\omega/2k}}\cos\big(\omega t-x\sqrt{\omega/2k}\big)$, as one checks by substitution: the annual temperature cycle penetrates about $\sqrt{365}\approx19$ times deeper than the daily one, and at the depth $\pi\sqrt{2k/\omega}$ (a few meters in soil) the annual cycle is reversed in phase, so that the ground there is coldest in summer and warmest in winter.

## 7.4. The Nonhomogeneous Equation and Duhamel's Principle

Consider the heat equation with a source on $\mathbb{R}^n$:

$$
u_t-k\Delta u=f(x,t),\quad t>0,\qquad u(x,0)=0.\tag{7.4}
$$
By **Duhamel's principle** ([2.5.3](/2.5.3)), we regard the source acting during $[s,s+\mathrm{d}s]$ as an initial temperature $f(\cdot,s)\,\mathrm{d}s$ given at time $s$. Let $w(x,t;s)$ solve the homogeneous equation for $t>s$ with $w(x,s;s)=f(x,s)$, that is, $w(\cdot,t;s)=\Phi(\cdot,t-s)*f(\cdot,s)$. Superposing,

$$
u(x,t)=\int_0^tw(x,t;s)\,\mathrm{d}s=\int_0^t\!\!\int_{\mathbb{R}^n}\Phi(x-y,t-s)f(y,s)\,\mathrm{d}y\,\mathrm{d}s.\tag{7.5}
$$

**Theorem 7.4.1** Let $f$ be bounded and continuous on $\mathbb{R}^n\times[0,\infty)$ with bounded continuous derivatives $f_t$, $f_{x_i}$, $f_{x_ix_j}$. Then (7.5) is a solution of (7.4), continuous on $\mathbb{R}^n\times[0,\infty)$ with $u(x,0)=0$. The solution of $u_t-k\Delta u=f$ with $u(x,0)=\varphi(x)$ is the sum of (7.2) and (7.5).

**Proof** (Sketch.) Formally, differentiating (7.5) with respect to the upper limit and under the integral sign,

$$
u_t=w(x,t;t)+\int_0^tw_t(x,t;s)\,\mathrm{d}s=f(x,t)+\int_0^tk\Delta w(x,t;s)\,\mathrm{d}s=f(x,t)+k\Delta u.
$$
The difficulty is that the second derivatives of $\Phi(x-y,t-s)$ are not integrable near $s=t$. The remedy is to substitute $y\mapsto x-y$ and $s\mapsto t-s$, writing $u=\int_0^t\int\Phi(y,s)f(x-y,t-s)\,\mathrm{d}y\,\mathrm{d}s$, so that all derivatives fall on $f$; the singular part near $s=0$ is then handled by integrating by parts in $y$ and using $\Phi_s=k\Delta\Phi$ (see Evans, §2.3). The bound $\lvert u\rvert\le t\sup\lvert f\rvert$, which follows from $\int\Phi=1$, gives continuity at $t=0$. $\square$

The structure is the same as the **variation of constants formula** for linear ODEs: the solution operator of the homogeneous problem, applied to the source at each earlier time and integrated. On a bounded interval the same principle, combined with the eigenfunction expansions of [2.5.4](/2.5.4), gives the series solution of nonhomogeneous problems.

**Example 7.4.1** Solve $u_t=k u_{xx}+\sin x$ on $\mathbb{R}$, $u(x,0)=0$.

**Solution** The homogeneous solution with initial value $\sin x$ at time $s$ is $w(x,t;s)=\mathrm{e}^{-k(t-s)}\sin x$ (since $\sin x$ is an eigenfunction of $\partial_x^2$). By (7.5),

$$
u(x,t)=\int_0^t\mathrm{e}^{-k(t-s)}\,\mathrm{d}s\,\sin x=\frac{1-\mathrm{e}^{-k t}}{k}\sin x.
$$
As $t\to\infty$, $u$ tends to the steady state $\frac1k\sin x$, the solution of $-k u''=\sin x$: the source and the diffusive loss come into balance on the time scale $1/k$.

## 7.5. Diffusion, Random Walks and Reaction-Diffusion Equations

### 7.5.1. The Probabilistic Meaning of the Heat Kernel

Let a particle on the line jump a distance $h$ to the left or to the right, with probability $\frac12$ each, every $\tau$ units of time, independently of its past. The probability $p(x,t)$ of finding it at the lattice point $x$ at time $t$ satisfies

$$
p(x,t+\tau)=\tfrac12p(x-h,t)+\tfrac12p(x+h,t).
$$
Expanding both sides by **Taylor's formula**, $\tau p_t+O(\tau^2)=\frac{h^2}2p_{xx}+O(h^4)$. Dividing by $\tau$ and letting $h,\tau\to0$ with $\frac{h^2}{2\tau}=k$ fixed gives $p_t=k p_{xx}$: the diffusion equation is the continuum limit of a random walk, and the diffusion coefficient is $k=h^2/(2\tau)$.

The same conclusion follows from the **central limit theorem**. After $n=t/\tau$ steps the position is a sum of $n$ independent steps $\pm h$ with mean $0$ and variance $h^2$, so it is approximately normal with variance $nh^2=2k t$. The density of $\mathcal{N}(0,2k t)$ is exactly $\Phi(x,t)$. In the limit the random walk becomes Brownian motion $B_t$ (with $k=\frac12$), and formula (7.2) acquires the meaning

$$
u(x,t)=\mathbb{E}\big[\varphi\big(x+\sqrt{2k}\,B_t\big)\big]:
$$
the temperature at $x$ is the average of the initial temperature at the random position reached by a Brownian particle started at $x$. In $\mathbb{R}^n$ the mean squared displacement is $\mathbb{E}\lvert X_t\rvert^2=2nk t$ (Einstein's relation), and the time to diffuse a distance $L$ is of order $L^2/k$.

![Left: sample paths of a random walk with step h = 0.1 every tau = 0.005 stay mostly within ±2 sqrt(2 k t). Right: histograms of 50000 walkers at three times agree with the heat kernel with k = h^2 / (2 tau) = 1](./plots/random-walk.py)

The quadratic scaling of diffusion time with distance has direct consequences in biology. A protein in the cytoplasm has a diffusion coefficient of order $10\,\mathrm{\mu m^2\,s^{-1}}$: it crosses a cell of size $10\,\mathrm{\mu m}$ in a few seconds, but would need months to travel $1\,\mathrm{cm}$. Diffusion suffices for transport inside cells and over short distances between them; larger organisms need circulation and active transport.

### 7.5.2. Reaction-Diffusion Equations

When the diffusing quantity is also produced or consumed locally, the heat equation acquires a nonlinear source term. An equation of the form

$$
u_t=D\Delta u+f(u),\tag{7.6}
$$
or a system of such equations $\boldsymbol{u}_t=D\Delta\boldsymbol{u}+\boldsymbol{f}(\boldsymbol{u})$ with a diagonal matrix $D$ of diffusion coefficients, is called a *reaction-diffusion equation*. The diffusion term spreads $u$ out, and the reaction term $f$ (birth and death, chemical reactions) acts at each point as in the corresponding ODE. Two phenomena have no counterpart in either part alone; they appear in [Ecology](/7.19) and [Developmental Biology](/7.5), respectively.

1. Invasion fronts: for the Fisher–KPP equation $u_t=Du_{xx}+ru(1-u)$, a population spreading into empty territory forms a *traveling wave solution* $u=U(x-ct)$ connecting $u=1$ behind the front to $u=0$ ahead of it. Near the leading edge $u$ is small and the equation is approximately $u_t=Du_{xx}+ru$; substituting $u=\mathrm{e}^{-\lambda(x-ct)}$ gives $c=D\lambda+\frac r\lambda\ge2\sqrt{rD}$ (by the AM–GM inequality). The front from localized initial data travels at the minimal speed $c^*=2\sqrt{rD}$ (stated without proof): the invasion speed is set by the growth rate and the diffusion coefficient together.
2. Diffusion-driven instability: for two species $u,v$ with $u_t=D_u\Delta u+f(u,v)$ and $v_t=D_v\Delta v+g(u,v)$, let $(u^*,v^*)$ be a homogeneous steady state that is stable for the ODE, so that the Jacobian matrix $J$ has $\operatorname{tr}J<0$ and $\det J>0$. A perturbation proportional to $\mathrm{e}^{\mathrm{i}qx+\sigma t}$ grows or decays according to the eigenvalues $\sigma$ of $J-q^2\operatorname{diag}(D_u,D_v)$. The trace remains negative, so instability occurs exactly when the determinant
$$
h(q^2)=D_uD_vq^4-\big(D_vf_u+D_ug_v\big)q^2+\det J
$$
becomes negative for some $q$. This requires $D_vf_u+D_ug_v>2\sqrt{D_uD_v\det J}$, which is possible, despite $f_u+g_v<0$, only if $f_u$ and $g_v$ have opposite signs and the diffusion coefficients are sufficiently different: a self-enhancing activator that diffuses slowly and an inhibitor that diffuses fast. A band of wave numbers $q$ then grows, and the nonlinear terms saturate the growth into stationary, spatially periodic patterns called *Turing patterns*. Turing proposed this mechanism in 1952 as a chemical basis of morphogenesis, and it is used to explain animal coat patterns, digit spacing and vegetation patterns.

That diffusion, which smooths everything when acting alone, can destabilize a uniform state is one of the most remarkable facts of applied mathematics.

## Summary

| Topic | Statement |
|---|---|
| Heat kernel | $\Phi=(4\pi k t)^{-n/2}\mathrm{e}^{-\lvert x\rvert^2/(4k t)}$; positive, mass 1, approximate identity as $t\to0^+$, $\Phi(t)*\Phi(s)=\Phi(t+s)$ |
| Cauchy problem | $u=\Phi(\cdot,t)*\varphi$ for bounded continuous $\varphi$; smooth for $t>0$; unique among bounded solutions |
| Qualitative behavior | Infinite speed of propagation, instant smoothing, decay like $t^{-n/2}$, backward problem ill-posed |
| Weak maximum principle | $u_t-k\Delta u\le0\Rightarrow\max_{\bar Q_T}u=\max_{\Gamma_T}u$; gives uniqueness, stability, comparison |
| Energy method | $\frac{\mathrm{d}}{\mathrm{d}t}\int u^2=-2k\int\lvert\nabla u\rvert^2$ for Dirichlet or Neumann conditions |
| Half-line | Odd extension for $u(0,t)=0$, even extension for $u_x(0,t)=0$; $\varphi\equiv1$ gives $\operatorname{erf}\frac{x}{2\sqrt{k t}}$ |
| Duhamel's principle | $u=\int_0^t\Phi(\cdot,t-s)*f(\cdot,s)\,\mathrm{d}s$ |
| Probability | $\Phi(\cdot,t)$ is the density of $\mathcal{N}(0,2k t)$; random walk with $k=h^2/(2\tau)$ |
| Reaction-diffusion | $u_t=D\Delta u+f(u)$: traveling fronts with speed $2\sqrt{rD}$; Turing instability for $D_v\gg D_u$ |
