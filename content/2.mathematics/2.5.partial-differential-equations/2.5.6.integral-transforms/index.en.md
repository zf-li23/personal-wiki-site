---
title: Fourier and Laplace Transforms
---

Separation of variables on a bounded interval produces a discrete set of eigenvalues and a **Fourier series**. On the whole line there are no boundary conditions to quantize the frequencies: every frequency $\xi\in\mathbb{R}$ is allowed, and the series becomes an integral. The Fourier transform decomposes a function into the plane waves $\mathrm{e}^{\mathrm{i}\xi x}$, which are eigenfunctions of differentiation: $\frac{\mathrm{d}}{\mathrm{d}x}\mathrm{e}^{\mathrm{i}\xi x}=\mathrm{i}\xi\,\mathrm{e}^{\mathrm{i}\xi x}$. Under the transform, differentiation becomes multiplication by $\mathrm{i}\xi$, a linear PDE with constant coefficients on $\mathbb{R}$ becomes an ordinary differential equation in the remaining variable, and the solution formula appears as a convolution. The Fourier transform is equally fundamental outside PDEs: in signal processing, optics, probability (the characteristic function of a distribution is a Fourier transform), quantum mechanics and numerical analysis.

This chapter develops the theory carefully, because the usual calculus course states the formulas without saying when they hold or why. We pass from Fourier series to the Fourier integral (§6.1), define the transform and prove its main properties, including the convolution theorem and the transform of the Gaussian, computed by shifting a contour in the complex plane (§6.2). We then prove the inversion formula and Plancherel's theorem and derive the uncertainty principle (§6.3), and use the transform to solve the heat equation, the wave equation and the Laplace equation on unbounded domains (§6.4). Finally, the Laplace transform, the one-sided version suited to initial value problems, is inverted by a contour integral evaluated with residues (§6.5). Complex analysis ([2.3](/2.3)) is used throughout; the heat kernel found here is studied in [2.5.7](/2.5.7), and the Poisson kernel of the half-plane reappears in [2.5.8](/2.5.8).

## 6.1. From Fourier Series to the Fourier Integral

Let $f$ be a function on $\mathbb{R}$ that decays at infinity. On $[-l,l]$ it has the complex Fourier series ([2.2.9](/2.2.9#sec-9.3.3))

$$
f(x)=\sum_{n=-\infty}^{\infty}c_n\mathrm{e}^{\mathrm{i}\xi_nx},\qquad c_n=\frac1{2l}\int_{-l}^lf(y)\mathrm{e}^{-\mathrm{i}\xi_ny}\,\mathrm{d}y,\qquad\xi_n=\frac{n\pi}{l}.
$$
The admissible frequencies $\xi_n$ are spaced $\Delta\xi=\pi/l$ apart. Writing $F_l(\xi)=\int_{-l}^lf(y)\mathrm{e}^{-\mathrm{i}\xi y}\,\mathrm{d}y$, we have $c_n=F_l(\xi_n)/(2l)=F_l(\xi_n)\Delta\xi/(2\pi)$, so

$$
f(x)=\frac1{2\pi}\sum_{n=-\infty}^\infty F_l(\xi_n)\,\mathrm{e}^{\mathrm{i}\xi_nx}\,\Delta\xi.
$$
As $l\to\infty$, the frequencies fill the whole line, $F_l(\xi)$ tends to $\hat f(\xi)=\int_{\mathbb{R}}f(y)\mathrm{e}^{-\mathrm{i}\xi y}\,\mathrm{d}y$, and the sum looks like a Riemann sum for an integral:

$$
f(x)=\frac1{2\pi}\int_{-\infty}^{\infty}\hat f(\xi)\,\mathrm{e}^{\mathrm{i}\xi x}\,\mathrm{d}\xi.\tag{6.1}
$$
This representation of $f$ as a continuous superposition of plane waves is the *Fourier integral*. The argument is only heuristic (the Riemann sum runs over an unbounded range, and $F_l$ changes with $l$), and the rest of the chapter establishes when (6.1) is actually true. The coefficients of a periodic function form a discrete spectrum; for a function on the whole line, $\hat f(\xi)\,\mathrm{d}\xi/(2\pi)$ is the amplitude of the frequencies in $[\xi,\xi+\mathrm{d}\xi]$, a continuous spectrum.

![For exp(-|x|) restricted to [-l, l], the scaled Fourier coefficients 2l c_n sit at the frequencies n pi / l; as l grows they fill in the curve of the Fourier transform 2 / (1 + xi^2)](./plots/series-to-integral.py)

## 6.2. The Fourier Transform

### 6.2.1. Definition and Basic Examples

We say that $f\colon\mathbb{R}\to\mathbb{C}$ is absolutely integrable if it is integrable on every bounded interval and $\int_{\mathbb{R}}\lvert f\rvert\,\mathrm{d}x<\infty$ (an absolutely convergent **improper integral**).

**Definition 6.2.1 (Fourier Transform)** Let $f$ be absolutely integrable on $\mathbb{R}$. The function

$$
\hat f(\xi)=\mathscr{F}\{f\}(\xi)=\int_{-\infty}^{\infty}f(x)\,\mathrm{e}^{-\mathrm{i}\xi x}\,\mathrm{d}x,\qquad\xi\in\mathbb{R},\tag{6.2}
$$
is called the **Fourier transform** of $f$. For an absolutely integrable $g$ on $\mathbb{R}$, the function

$$
\mathscr{F}^{-1}\{g\}(x)=\frac1{2\pi}\int_{-\infty}^\infty g(\xi)\,\mathrm{e}^{\mathrm{i}\xi x}\,\mathrm{d}\xi\tag{6.3}
$$
is called the **inverse Fourier transform** of $g$.

The variable $\xi$ is the angular frequency (or wave number) if $x$ is time (or position). Other books place the factors differently: some use $\frac1{\sqrt{2\pi}}$ in both directions, and signal processing often writes $\int f(x)\mathrm{e}^{-2\pi\mathrm{i}\nu x}\,\mathrm{d}x$ with the ordinary frequency $\nu=\xi/(2\pi)$, which removes all factors $2\pi$. The theory is the same; only the constants in the formulas below change, and one must check the convention before using a table.

**Theorem 6.2.1** If $f$ is absolutely integrable, then $\hat f$ is bounded, with $\lvert\hat f(\xi)\rvert\le\int_{\mathbb{R}}\lvert f\rvert\,\mathrm{d}x$, uniformly continuous on $\mathbb{R}$, and $\hat f(\xi)\to0$ as $\xi\to\pm\infty$ (the *Riemann–Lebesgue lemma*).

**Proof** The bound follows from $\lvert f(x)\mathrm{e}^{-\mathrm{i}\xi x}\rvert=\lvert f(x)\rvert$. For continuity, $\lvert\hat f(\xi+h)-\hat f(\xi)\rvert\le\int\lvert f(x)\rvert\,\lvert\mathrm{e}^{-\mathrm{i}hx}-1\rvert\,\mathrm{d}x$. Given $\varepsilon>0$, choose $A$ with $\int_{\lvert x\rvert>A}\lvert f\rvert<\varepsilon$; on $\lvert x\rvert\le A$ we have $\lvert\mathrm{e}^{-\mathrm{i}hx}-1\rvert\le\lvert h\rvert A$. Hence the difference is at most $\lvert h\rvert A\int\lvert f\rvert+2\varepsilon$, independently of $\xi$.

For the Riemann–Lebesgue lemma, first let $f=\boldsymbol{1}_{[a,b]}$ be the indicator of an interval. Then $\hat f(\xi)=\frac{\mathrm{e}^{-\mathrm{i}a\xi}-\mathrm{e}^{-\mathrm{i}b\xi}}{\mathrm{i}\xi}$, which tends to $0$, and so does the transform of every step function (a finite linear combination of indicators). A general absolutely integrable $f$ can be approximated by a step function $s$ with $\int\lvert f-s\rvert<\varepsilon$ (cut off the tails, then approximate by Riemann sums), and $\lvert\hat f(\xi)\rvert\le\lvert\hat s(\xi)\rvert+\varepsilon<2\varepsilon$ for large $\lvert\xi\rvert$. $\square$

The decay $\hat f(\xi)\to0$ says that a function cannot contain an appreciable amount of arbitrarily high frequencies. The finer statements below show that the rate of decay of $\hat f$ measures the smoothness of $f$.

**Example 6.2.1 (Rectangular Pulse)** For $a>0$, $f=\boldsymbol{1}_{[-a,a]}$ has the transform

$$
\hat f(\xi)=\int_{-a}^a\mathrm{e}^{-\mathrm{i}\xi x}\,\mathrm{d}x=\frac{2\sin a\xi}{\xi}\qquad(\hat f(0)=2a).
$$
The transform is not absolutely integrable, since $\lvert\sin a\xi/\xi\rvert$ decays only like $1/\lvert\xi\rvert$. This is the price of the jumps of $f$.

**Example 6.2.2 (Exponentials)** For $a>0$,

$$
\mathscr{F}\{\mathrm{e}^{-a\lvert x\rvert}\}(\xi)=\int_{-\infty}^\infty\mathrm{e}^{-a\lvert x\rvert}\mathrm{e}^{-\mathrm{i}\xi x}\,\mathrm{d}x=\frac{1}{a+\mathrm{i}\xi}+\frac{1}{a-\mathrm{i}\xi}=\frac{2a}{a^2+\xi^2},
$$
because $\int_0^\infty\mathrm{e}^{-(a+\mathrm{i}\xi)x}\,\mathrm{d}x=\frac1{a+\mathrm{i}\xi}$. The first term alone shows that the one-sided exponential $H(x)\mathrm{e}^{-ax}$ has the transform $\frac1{a+\mathrm{i}\xi}$, where $H$ is the Heaviside step function ($H(x)=1$ for $x>0$ and $0$ for $x<0$). The function $\mathrm{e}^{-a\lvert x\rvert}$ is continuous but has a corner at $0$, and its transform decays like $1/\xi^2$.

### 6.2.2. The Gaussian

The most important transform pair is that of the Gaussian. We compute it with complex integration: the idea is to complete the square and then shift the line of integration back to the real axis.

**Theorem 6.2.2 (Fourier Transform of the Gaussian)** For $a>0$,

$$
\mathscr{F}\{\mathrm{e}^{-ax^2}\}(\xi)=\sqrt{\frac\pi a}\,\mathrm{e}^{-\xi^2/(4a)}.\tag{6.4}
$$
In particular, $\mathscr{F}\{\mathrm{e}^{-x^2/2}\}=\sqrt{2\pi}\,\mathrm{e}^{-\xi^2/2}$: up to a constant factor, the standard Gaussian is its own Fourier transform.

**Proof** Completing the square, $-ax^2-\mathrm{i}\xi x=-a(x+\mathrm{i}b)^2-\frac{\xi^2}{4a}$ with $b=\frac{\xi}{2a}$, so

$$
\hat f(\xi)=\mathrm{e}^{-\xi^2/(4a)}\int_{-\infty}^\infty\mathrm{e}^{-a(x+\mathrm{i}b)^2}\,\mathrm{d}x.
$$
The last integral is the integral of the entire function $h(z)=\mathrm{e}^{-az^2}$ along the horizontal line $\operatorname{Im}z=b$. Let $\gamma_R$ be the boundary of the rectangle with vertices $-R$, $R$, $R+\mathrm{i}b$, $-R+\mathrm{i}b$. By **Cauchy's integral theorem** ([2.3.4](/2.3.4)), $\oint_{\gamma_R}h(z)\,\mathrm{d}z=0$. On the vertical side $z=R+\mathrm{i}y$ ($y$ between $0$ and $b$) we have $\lvert h(z)\rvert=\mathrm{e}^{-a(R^2-y^2)}\le\mathrm{e}^{-aR^2+ab^2}$, so the integral over this side is at most $\lvert b\rvert\mathrm{e}^{ab^2}\mathrm{e}^{-aR^2}\to0$ as $R\to\infty$, and likewise for the side at $-R$. Hence

$$
\int_{-\infty}^\infty\mathrm{e}^{-a(x+\mathrm{i}b)^2}\,\mathrm{d}x=\int_{-\infty}^\infty\mathrm{e}^{-ax^2}\,\mathrm{d}x=\sqrt{\frac\pi a}
$$
by the **Gaussian integral**. $\square$

A second proof avoids complex analysis. The function $f=\mathrm{e}^{-ax^2}$ satisfies $f'=-2axf$. By the derivative and multiplication rules of Theorem 6.2.3 below, $\mathrm{i}\xi\hat f=-2a\cdot\mathrm{i}\hat f'$, that is, $\hat f'=-\frac{\xi}{2a}\hat f$, so $\hat f=\hat f(0)\mathrm{e}^{-\xi^2/(4a)}$ with $\hat f(0)=\int\mathrm{e}^{-ax^2}\,\mathrm{d}x=\sqrt{\pi/a}$.

Formula (6.4) displays a reciprocity that will recur: a narrow Gaussian (large $a$, width about $1/\sqrt a$) has a wide transform (width about $\sqrt a$), and conversely.

![Three transform pairs: the rectangular pulse and 2 sin(xi)/xi, the two-sided exponential and the Lorentzian 2/(1 + xi^2), and Gaussians of three widths s, whose transforms have width 1/s](./plots/fourier-pairs.py)

### 6.2.3. Properties

**Theorem 6.2.3** Let $f$ be absolutely integrable and let $a,b\in\mathbb{R}$, $b\ne0$.

1. (Linearity) $\mathscr{F}\{\alpha f+\beta g\}=\alpha\hat f+\beta\hat g$;
2. (Translation) $\mathscr{F}\{f(x-a)\}=\mathrm{e}^{-\mathrm{i}a\xi}\hat f(\xi)$;
3. (Modulation) $\mathscr{F}\{\mathrm{e}^{\mathrm{i}ax}f(x)\}=\hat f(\xi-a)$;
4. (Scaling) $\mathscr{F}\{f(bx)\}=\frac1{\lvert b\rvert}\hat f\big(\frac\xi b\big)$;
5. (Conjugation) $\mathscr{F}\{\bar f\}(\xi)=\overline{\hat f(-\xi)}$; hence if $f$ is real, $\hat f(-\xi)=\overline{\hat f(\xi)}$, and if $f$ is real and even, $\hat f$ is real and even;
6. (Differentiation) if $f$ is continuous and piecewise $C^1$ and $f'$ is absolutely integrable, then $\mathscr{F}\{f'\}=\mathrm{i}\xi\hat f$; more generally $\mathscr{F}\{f^{(k)}\}=(\mathrm{i}\xi)^k\hat f$ under the corresponding hypotheses;
7. (Multiplication by $x$) if $xf(x)$ is absolutely integrable, then $\hat f\in C^1$ and $\mathscr{F}\{xf(x)\}=\mathrm{i}\hat f'(\xi)$.

**Proof** Properties 1–5 follow from the substitutions $x\mapsto x+a$ and $x\mapsto x/b$ in (6.2) (for $b<0$ the substitution reverses the limits, which produces $\lvert b\rvert$).

6: Since $f(x)=f(0)+\int_0^xf'$ and $f'$ is absolutely integrable, $f(x)$ has limits as $x\to\pm\infty$; these limits must be $0$ because $f$ is absolutely integrable. Integrating by parts on $[-R,R]$,

$$
\int_{-R}^Rf'(x)\mathrm{e}^{-\mathrm{i}\xi x}\,\mathrm{d}x=\Big[f(x)\mathrm{e}^{-\mathrm{i}\xi x}\Big]_{-R}^R+\mathrm{i}\xi\int_{-R}^Rf(x)\mathrm{e}^{-\mathrm{i}\xi x}\,\mathrm{d}x,
$$
and letting $R\to\infty$ gives $\mathscr{F}\{f'\}=\mathrm{i}\xi\hat f$.

7: The derivative of the integrand with respect to $\xi$ is $-\mathrm{i}xf(x)\mathrm{e}^{-\mathrm{i}\xi x}$, which is bounded by the integrable function $\lvert xf(x)\rvert$ independently of $\xi$. Hence the differentiated integral converges uniformly (Weierstrass M-test), and **differentiation under the integral sign** is justified: $\hat f'(\xi)=\int(-\mathrm{i}x)f(x)\mathrm{e}^{-\mathrm{i}\xi x}\,\mathrm{d}x=-\mathrm{i}\,\mathscr{F}\{xf\}$. $\square$

Properties 6 and 7 are the heart of the matter and are dual to each other:

- Smoothness of $f$ gives decay of $\hat f$: if $f,f',\dots,f^{(k)}$ are absolutely integrable, then $(\mathrm{i}\xi)^k\hat f$ is bounded and tends to $0$ (Theorem 6.2.1), so $\hat f(\xi)=o(\lvert\xi\rvert^{-k})$.
- Decay of $f$ gives smoothness of $\hat f$: if $x^kf$ is absolutely integrable, then $\hat f\in C^k$.

The Gaussian is both infinitely smooth and rapidly decaying, and so is its transform. The rectangular pulse has jumps, and its transform decays only like $1/\xi$; the function $\mathrm{e}^{-a\lvert x\rvert}$ has a corner, and its transform decays like $1/\xi^2$, but it decays exponentially, so its transform $\frac{2a}{a^2+\xi^2}$ is infinitely differentiable.

### 6.2.4. Convolution

**Definition 6.2.2 (Convolution)** Let $f,g$ be absolutely integrable, and let one of them be bounded. The function

$$
(f*g)(x)=\int_{-\infty}^\infty f(x-y)g(y)\,\mathrm{d}y
$$
is called the **convolution** of $f$ and $g$.

The substitution $y\mapsto x-y$ shows $f*g=g*f$; convolution is also associative and bilinear, and $\int\lvert f*g\rvert\le\int\lvert f\rvert\int\lvert g\rvert$. If $g\ge0$ and $\int g=1$, then $(f*g)(x)$ is a weighted average of the values of $f$ near $x$, a smoothed version of $f$: for example, $f*\frac1{2h}\boldsymbol{1}_{[-h,h]}$ is the moving average $\frac1{2h}\int_{x-h}^{x+h}f$. Convolution describes every linear, translation-invariant system: if a system responds to a unit impulse at $y$ with $g(x-y)$, then by superposition its response to the input $f$ is $f*g$.

**Theorem 6.2.4 (Convolution Theorem)** Under the hypotheses of Definition 6.2.2,

$$
\mathscr{F}\{f*g\}=\hat f\,\hat g.\tag{6.5}
$$

**Proof** Since $\int\!\!\int\lvert f(x-y)\rvert\,\lvert g(y)\rvert\,\mathrm{d}x\,\mathrm{d}y=\int\lvert f\rvert\cdot\int\lvert g\rvert<\infty$, the double integral below converges absolutely, and the order of integration may be interchanged (Fubini's theorem). Writing $\mathrm{e}^{-\mathrm{i}\xi x}=\mathrm{e}^{-\mathrm{i}\xi(x-y)}\mathrm{e}^{-\mathrm{i}\xi y}$,

$$
\mathscr{F}\{f*g\}(\xi)=\int_{-\infty}^\infty g(y)\mathrm{e}^{-\mathrm{i}\xi y}\Big(\int_{-\infty}^\infty f(x-y)\mathrm{e}^{-\mathrm{i}\xi(x-y)}\,\mathrm{d}x\Big)\mathrm{d}y=\hat f(\xi)\int_{-\infty}^\infty g(y)\mathrm{e}^{-\mathrm{i}\xi y}\,\mathrm{d}y=\hat f(\xi)\hat g(\xi).\ \square
$$

The theorem is the reason convolutions appear in solution formulas: if the transformed problem is solved by multiplying the transformed data by some function $\hat K(\xi)$, then the solution is the convolution of the data with $K$. Dually, under suitable hypotheses (for instance when the inversion formula of §6.3 applies to $f$ and $g$), $\mathscr{F}\{fg\}=\frac1{2\pi}\hat f*\hat g$.

**Example 6.2.3** Let $p=\boldsymbol{1}_{[-1,1]}$. Then $(p*p)(x)$ is the length of $[-1,1]\cap[x-1,x+1]$, the triangle function $\max(2-\lvert x\rvert,0)$. By Theorem 6.2.4 and Example 6.2.1,

$$
\mathscr{F}\{\max(2-\lvert x\rvert,0)\}=\Big(\frac{2\sin\xi}{\xi}\Big)^2=\frac{4\sin^2\xi}{\xi^2},
$$
which can be checked by direct integration. The triangle is continuous with corners, and its transform decays like $1/\xi^2$.

### 6.2.5. Several Variables

For an absolutely integrable $f$ on $\mathbb{R}^n$ we define $\hat f(\xi)=\int_{\mathbb{R}^n}f(x)\,\mathrm{e}^{-\mathrm{i}\xi\cdot x}\,\mathrm{d}x$ and $\mathscr{F}^{-1}\{g\}(x)=(2\pi)^{-n}\int_{\mathbb{R}^n}g(\xi)\mathrm{e}^{\mathrm{i}\xi\cdot x}\,\mathrm{d}\xi$. All the results of this chapter carry over with the obvious changes: $\partial/\partial x_j$ becomes multiplication by $\mathrm{i}\xi_j$, so the Laplacian becomes multiplication by $-\lvert\xi\rvert^2$; the convolution theorem holds with $\int_{\mathbb{R}^n}$; and since $\mathrm{e}^{-a\lvert x\rvert^2}=\prod_j\mathrm{e}^{-ax_j^2}$, formula (6.4) gives

$$
\mathscr{F}\{\mathrm{e}^{-a\lvert x\rvert^2}\}(\xi)=\Big(\frac\pi a\Big)^{n/2}\mathrm{e}^{-\lvert\xi\rvert^2/(4a)}.
$$

## 6.3. Inversion and Plancherel's Theorem

### 6.3.1. Approximate Identities and the Delta Function

The proof of the inversion formula rests on a simple but far-reaching idea: convolving with a narrow kernel of total mass 1 almost reproduces the function.

**Lemma 6.3.1 (Approximate Identity)** Let $K$ be absolutely integrable with $\int_{\mathbb{R}}K\,\mathrm{d}x=1$, and set $K_\varepsilon(x)=\frac1\varepsilon K\big(\frac x\varepsilon\big)$ for $\varepsilon>0$. If $f$ is bounded on $\mathbb{R}$ and continuous at $x$, then $(K_\varepsilon*f)(x)\to f(x)$ as $\varepsilon\to0^+$. If $f$ is bounded and uniformly continuous, the convergence is uniform in $x$.

**Proof** Since $\int K_\varepsilon=1$, substituting $y=\varepsilon z$,

$$
(K_\varepsilon*f)(x)-f(x)=\int_{-\infty}^\infty K_\varepsilon(y)\big(f(x-y)-f(x)\big)\,\mathrm{d}y=\int_{-\infty}^\infty K(z)\big(f(x-\varepsilon z)-f(x)\big)\,\mathrm{d}z.
$$
Let $\lvert f\rvert\le M$ and $\eta>0$. Choose $A$ with $\int_{\lvert z\rvert>A}\lvert K\rvert<\eta$, then $\varepsilon_0$ such that $\lvert f(x-w)-f(x)\rvert<\eta$ for $\lvert w\rvert<\varepsilon_0A$. For $\varepsilon<\varepsilon_0$ the integral over $\lvert z\rvert\le A$ is at most $\eta\int\lvert K\rvert$ and the integral over $\lvert z\rvert>A$ is at most $2M\eta$. If $f$ is uniformly continuous, $\varepsilon_0$ does not depend on $x$. $\square$

As $\varepsilon\to0^+$, the kernels $K_\varepsilon$ concentrate all their mass at the origin. Physicists describe the limit as the *Dirac delta function* $\delta$: a "function" that vanishes for $x\ne0$ and satisfies

$$
\int_{-\infty}^\infty\delta(x)\varphi(x)\,\mathrm{d}x=\varphi(0)\qquad\text{for every continuous }\varphi.
$$
No genuine function has this property; $\delta$ is a generalized function (a distribution), and the statement $K_\varepsilon\to\delta$ means precisely that $\int K_\varepsilon\varphi\to\varphi(0)$, which is Lemma 6.3.1 at $x=0$. With this language, $\delta*f=f$, the impulse response of a system is its response to $\delta$, and

$$
\mathscr{F}\{\delta\}=1,\qquad\mathscr{F}\{1\}=2\pi\delta,\qquad\mathscr{F}\{\mathrm{e}^{\mathrm{i}ax}\}=2\pi\delta(\xi-a).
$$
The first formula is consistent with $\hat K_\varepsilon(\xi)=\hat K(\varepsilon\xi)\to\hat K(0)=1$; the last says that a pure oscillation has its entire spectrum at one frequency. We use $\delta$ only as a convenient shorthand for such limits.

### 6.3.2. The Inversion Theorem

**Theorem 6.3.1 (Fourier Inversion Theorem)** Let $f$ be absolutely integrable on $\mathbb{R}$.

1. If $f$ is continuous and $\hat f$ is absolutely integrable, then for every $x\in\mathbb{R}$
$$
f(x)=\frac1{2\pi}\int_{-\infty}^\infty\hat f(\xi)\,\mathrm{e}^{\mathrm{i}\xi x}\,\mathrm{d}\xi,\qquad\text{that is,}\quad\mathscr{F}^{-1}\{\mathscr{F}\{f\}\}=f.
$$
2. If $f$ is piecewise smooth on every bounded interval, then for every $x$
$$
\lim_{R\to\infty}\frac1{2\pi}\int_{-R}^R\hat f(\xi)\,\mathrm{e}^{\mathrm{i}\xi x}\,\mathrm{d}\xi=\frac{f(x^+)+f(x^-)}2.
$$

**Proof** We prove 1. The idea is to insert a Gaussian factor $\mathrm{e}^{-\varepsilon\xi^2}$ that makes all integrals absolutely convergent, and then let $\varepsilon\to0^+$. Let

$$
I_\varepsilon(x)=\frac1{2\pi}\int_{-\infty}^\infty\hat f(\xi)\,\mathrm{e}^{-\varepsilon\xi^2}\mathrm{e}^{\mathrm{i}\xi x}\,\mathrm{d}\xi.
$$
Substituting the definition of $\hat f$, the double integral converges absolutely because $\int\!\!\int\lvert f(y)\rvert\mathrm{e}^{-\varepsilon\xi^2}\,\mathrm{d}y\,\mathrm{d}\xi<\infty$, so we may interchange the order:

$$
I_\varepsilon(x)=\int_{-\infty}^\infty f(y)\Big(\frac1{2\pi}\int_{-\infty}^\infty\mathrm{e}^{-\varepsilon\xi^2}\mathrm{e}^{\mathrm{i}\xi(x-y)}\,\mathrm{d}\xi\Big)\mathrm{d}y=\int_{-\infty}^\infty f(y)\,g_\varepsilon(x-y)\,\mathrm{d}y,
$$
where, by (6.4) with $a=\varepsilon$ (the sign of $\xi$ in the exponent is irrelevant because the Gaussian is even),

$$
g_\varepsilon(z)=\frac1{2\pi}\sqrt{\frac\pi\varepsilon}\,\mathrm{e}^{-z^2/(4\varepsilon)}=\frac{1}{\sqrt{4\pi\varepsilon}}\mathrm{e}^{-z^2/(4\varepsilon)}.
$$
This is $K_{\sqrt\varepsilon}$ for the Gaussian $K(z)=\frac1{\sqrt{4\pi}}\mathrm{e}^{-z^2/4}$, which has total integral 1. A continuous absolutely integrable function need not be bounded, so we split $f=f\boldsymbol{1}_{[x-1,x+1]}+f\boldsymbol{1}_{\mathbb{R}\setminus[x-1,x+1]}$. The first part is bounded and Lemma 6.3.1 applies to it, while the contribution of the second part is at most $\sup_{\lvert z\rvert\ge1}g_\varepsilon(z)\int\lvert f\rvert\to0$. Hence $I_\varepsilon(x)\to f(x)$.

On the other hand, $\lvert\hat f(\xi)(\mathrm{e}^{-\varepsilon\xi^2}-1)\rvert\le\lvert\hat f(\xi)\rvert$, which is integrable, and the integrand tends to $0$ for each $\xi$. Given $\eta>0$, choose $A$ with $\int_{\lvert\xi\rvert>A}\lvert\hat f\rvert<\eta$; on $\lvert\xi\rvert\le A$, $1-\mathrm{e}^{-\varepsilon\xi^2}\le\varepsilon A^2$. Thus $\big\lvert I_\varepsilon(x)-\frac1{2\pi}\int\hat f\mathrm{e}^{\mathrm{i}\xi x}\big\rvert\le\frac1{2\pi}\big(\varepsilon A^2\int\lvert\hat f\rvert+\eta\big)$, which is small for small $\varepsilon$. Comparing the two limits proves 1.

The proof of 2 is parallel to that of **Dirichlet's convergence theorem** for Fourier series ([2.2.9](/2.2.9#thm-9.3.1)): the truncated integral equals $\int f(x-y)\frac{\sin Ry}{\pi y}\,\mathrm{d}y$, and the kernel $\frac{\sin Ry}{\pi y}$ plays the role of the Dirichlet kernel; we omit the details. $\square$

The kernel $g_\varepsilon$ that appeared in the proof is, with $\varepsilon=k t$, the solution of the heat equation found in §6.4.1: the proof smooths $f$ by letting heat diffuse for a short time.

**Corollary 6.3.1 (Uniqueness)** If $f,g$ are continuous and absolutely integrable and $\hat f=\hat g$, then $f=g$.

**Proof** Apply part 1 of Theorem 6.3.1 to $f-g$, whose transform $0$ is absolutely integrable. $\square$

Uniqueness is what makes tables of transforms useful: once we recognize a transform, we know the function. The inversion formula also yields the duality $\mathscr{F}\{\hat f\}(x)=2\pi f(-x)$ (replace $x$ by $-x$ in part 1), which doubles every table.

**Example 6.3.1** By Example 6.2.2 and duality, $\mathscr{F}\big\{\frac{2a}{a^2+x^2}\big\}=2\pi\mathrm{e}^{-a\lvert\xi\rvert}$, that is,

$$
\mathscr{F}\Big\{\frac{a}{\pi(a^2+x^2)}\Big\}(\xi)=\mathrm{e}^{-a\lvert\xi\rvert}.\tag{6.6}
$$
Written out with $\xi$ and $x$ interchanged, the inversion formula for $\mathrm{e}^{-a\lvert x\rvert}$ says $\int_{-\infty}^\infty\frac{\cos\xi x}{a^2+\xi^2}\,\mathrm{d}\xi=\frac\pi a\mathrm{e}^{-a\lvert x\rvert}$, an integral that is usually evaluated with residues and **Jordan's lemma** ([2.3.7](/2.3.7)). The two methods are two views of the same fact.

**Example 6.3.2** Part 2 of Theorem 6.3.1 applied to the rectangular pulse of Example 6.2.1 with $a=1$ at $x=0$ gives $\frac1{2\pi}\lim_{R\to\infty}\int_{-R}^R\frac{2\sin\xi}{\xi}\,\mathrm{d}\xi=1$, that is, the **Dirichlet integral** $\int_0^\infty\frac{\sin\xi}{\xi}\,\mathrm{d}\xi=\frac\pi2$. At the jump $x=1$ the inverse transform gives the average value $\frac12$.

### 6.3.3. Plancherel's Theorem

**Theorem 6.3.2 (Plancherel's Theorem)** Let $f,g$ be absolutely integrable and square integrable on $\mathbb{R}$, and suppose the inversion formula of Theorem 6.3.1 (part 1) holds for $f$. Then

$$
\int_{-\infty}^\infty f(x)\overline{g(x)}\,\mathrm{d}x=\frac1{2\pi}\int_{-\infty}^\infty\hat f(\xi)\overline{\hat g(\xi)}\,\mathrm{d}\xi,\qquad\int_{-\infty}^\infty\lvert f\rvert^2\,\mathrm{d}x=\frac1{2\pi}\int_{-\infty}^\infty\lvert\hat f\rvert^2\,\mathrm{d}\xi.\tag{6.7}
$$

**Proof** Substitute the inversion formula for $f$ and interchange the order of integration (the double integral converges absolutely because $\hat f$ and $g$ are absolutely integrable):

$$
\int f\bar g\,\mathrm{d}x=\int\Big(\frac1{2\pi}\int\hat f(\xi)\mathrm{e}^{\mathrm{i}\xi x}\,\mathrm{d}\xi\Big)\overline{g(x)}\,\mathrm{d}x=\frac1{2\pi}\int\hat f(\xi)\,\overline{\int g(x)\mathrm{e}^{-\mathrm{i}\xi x}\,\mathrm{d}x}\,\mathrm{d}\xi=\frac1{2\pi}\int\hat f\,\overline{\hat g}\,\mathrm{d}\xi.
$$
Taking $g=f$ gives the second formula. $\square$

The second formula in (6.7) is the continuous analogue of Parseval's identity for Fourier series: the energy of a signal equals the total energy of its frequency components, and $\lvert\hat f(\xi)\rvert^2/(2\pi)$ is the energy spectral density. The hypotheses can be removed entirely: for every square-integrable $f$, the truncated transforms $\int_{-R}^Rf(x)\mathrm{e}^{-\mathrm{i}\xi x}\,\mathrm{d}x$ converge in the mean-square sense to a function $\hat f$ satisfying (6.7), and the Fourier transform becomes a bijection of the space $L^2(\mathbb{R})$ of square-integrable functions onto itself that preserves the inner product up to the factor $2\pi$ (stated without proof). This is the natural setting of the Fourier transform in quantum mechanics.

**Example 6.3.3** For $f=\boldsymbol{1}_{[-a,a]}$, $\int\lvert f\rvert^2=2a$, and (6.7) gives $\frac1{2\pi}\int\frac{4\sin^2a\xi}{\xi^2}\,\mathrm{d}\xi=2a$, that is, $\int_{-\infty}^\infty\frac{\sin^2a\xi}{\xi^2}\,\mathrm{d}\xi=\pi a$. (Here $f$ is discontinuous and Theorem 6.3.2 as stated does not apply, but the $L^2$ version does.)

### 6.3.4. The Uncertainty Principle

The reciprocity between the widths of $f$ and $\hat f$, visible in (6.4), holds for every function.

**Theorem 6.3.3 (Uncertainty Principle)** Let $f\in C^1(\mathbb{R})$ be such that $f$, $xf$ and $f'$ are square integrable, $f$ and $f'$ are absolutely integrable, and $x\lvert f(x)\rvert^2\to0$ as $x\to\pm\infty$. Then

$$
\Big(\int_{-\infty}^\infty x^2\lvert f(x)\rvert^2\,\mathrm{d}x\Big)\Big(\int_{-\infty}^\infty\xi^2\lvert\hat f(\xi)\rvert^2\,\mathrm{d}\xi\Big)\ge\frac\pi2\Big(\int_{-\infty}^\infty\lvert f(x)\rvert^2\,\mathrm{d}x\Big)^2,
$$
with equality if and only if $f(x)=C\mathrm{e}^{-ax^2}$ for some $a>0$.

**Proof** Integrating by parts and using $(\lvert f\rvert^2)'=f'\bar f+f\bar f'=2\operatorname{Re}\big(f\bar f'\big)$,

$$
\int_{-\infty}^\infty\lvert f\rvert^2\,\mathrm{d}x=\Big[x\lvert f\rvert^2\Big]_{-\infty}^\infty-\int_{-\infty}^\infty x\big(\lvert f\rvert^2\big)'\,\mathrm{d}x=-2\operatorname{Re}\int_{-\infty}^\infty xf(x)\overline{f'(x)}\,\mathrm{d}x.
$$
By the **Cauchy–Schwarz inequality**, $\big(\int\lvert f\rvert^2\big)^2\le4\int x^2\lvert f\rvert^2\int\lvert f'\rvert^2$. By Theorem 6.2.3 (part 6) and Plancherel's theorem applied to $f'$ (whose transform is $\mathrm{i}\xi\hat f$), $\int\lvert f'\rvert^2=\frac1{2\pi}\int\xi^2\lvert\hat f\rvert^2$, which gives the inequality. Equality in Cauchy–Schwarz requires $f'=-2axf$ for a constant $a$, which must be real and positive for the real part to attain the bound and for $f$ to be square integrable; hence $f=C\mathrm{e}^{-ax^2}$. Conversely, Gaussians give equality by direct computation. $\square$

Define the spreads of $f$ and $\hat f$ about the origin by $\sigma_x^2=\int x^2\lvert f\rvert^2/\int\lvert f\rvert^2$ and $\sigma_\xi^2=\int\xi^2\lvert\hat f\rvert^2/\int\lvert\hat f\rvert^2$. Since $\int\lvert\hat f\rvert^2=2\pi\int\lvert f\rvert^2$, the theorem says

$$
\sigma_x\,\sigma_\xi\ge\frac12.
$$
(Applying the theorem to $\mathrm{e}^{-\mathrm{i}\xi_0x}f(x+x_0)$ gives the same bound for the spreads about any centers $x_0$, $\xi_0$.) A signal cannot be sharply localized both in time and in frequency: a short pulse contains a broad band of frequencies, and a pure tone must last a long time. In quantum mechanics, the wave function of a particle in the momentum variable $p=\hbar\xi$ is the Fourier transform of its wave function in position, and the inequality becomes Heisenberg's $\sigma_x\sigma_p\ge\hbar/2$.

## 6.4. Solving PDEs with the Fourier Transform

**Algorithm 6.4.1 (Fourier Transform Method)** For a linear PDE with constant coefficients in which $x$ ranges over $\mathbb{R}$ (or $\mathbb{R}^n$):

1. Transform in $x$: $u(x,t)\mapsto\hat u(\xi,t)$. Derivatives $\partial_x^k$ become multiplication by $(\mathrm{i}\xi)^k$, and the PDE becomes an ODE in $t$ (or in the other variable) with the parameter $\xi$;
2. Transform the data and solve the ODE, using boundedness where needed to discard growing solutions;
3. Invert, recognizing products as convolutions (Theorem 6.2.4) and using tables, duality and the translation rule.

The computation is formal: it assumes that $u$ has a Fourier transform and that differentiation in $t$ commutes with the transform. The resulting formula is then verified directly, which is how we proceed in [2.5.7](/2.5.7) for the heat equation.

### 6.4.1. The Heat Equation on the Line

Consider the **heat equation** on an infinite rod:

$$
u_t=k u_{xx},\quad x\in\mathbb{R},\ t>0;\qquad u(x,0)=\varphi(x).
$$
Transforming in $x$ gives $\hat u_t=-k\xi^2\hat u$ with $\hat u(\xi,0)=\hat\varphi(\xi)$, so $\hat u(\xi,t)=\hat\varphi(\xi)\,\mathrm{e}^{-k\xi^2t}$. Each frequency decays at the rate $k\xi^2$: high frequencies (fine details) are damped fastest. By (6.4) with $a=\frac1{4k t}$, $\mathrm{e}^{-k\xi^2t}$ is the transform of

$$
\Phi(x,t)=\frac{1}{\sqrt{4\pi k t}}\,\mathrm{e}^{-x^2/(4k t)},\qquad t>0,\tag{6.8}
$$
and by the convolution theorem

$$
u(x,t)=(\Phi(\cdot,t)*\varphi)(x)=\frac1{\sqrt{4\pi k t}}\int_{-\infty}^\infty\mathrm{e}^{-(x-y)^2/(4k t)}\varphi(y)\,\mathrm{d}y.\tag{6.9}
$$
The function $\Phi$ is called the *heat kernel*. It is the temperature produced by a unit amount of heat released at the origin at time $0$ (initial datum $\delta$), and (6.9) superposes such point sources with strengths $\varphi(y)\,\mathrm{d}y$. In [2.5.7](/2.5.7) we verify that (6.9) solves the problem for every bounded continuous $\varphi$, even when $\varphi$ has no Fourier transform.

**Example 6.4.1** Let $\varphi=\boldsymbol{1}_{[-1,1]}$: a segment of the rod is initially at temperature 1 and the rest at 0. By (6.9) and the substitution $s=(y-x)/\sqrt{4k t}$,

$$
u(x,t)=\frac1{\sqrt\pi}\int_{(-1-x)/\sqrt{4k t}}^{(1-x)/\sqrt{4k t}}\mathrm{e}^{-s^2}\,\mathrm{d}s=\frac12\Big[\operatorname{erf}\Big(\frac{1-x}{\sqrt{4k t}}\Big)+\operatorname{erf}\Big(\frac{1+x}{\sqrt{4k t}}\Big)\Big],
$$
where

$$
\operatorname{erf}(x)=\frac2{\sqrt\pi}\int_0^x\mathrm{e}^{-s^2}\,\mathrm{d}s,\qquad\operatorname{erfc}(x)=1-\operatorname{erf}(x)=\frac2{\sqrt\pi}\int_x^\infty\mathrm{e}^{-s^2}\,\mathrm{d}s
$$
are the *error function* and the complementary error function. The function $\operatorname{erf}$ is odd, increases from $-1$ to $1$, and $\operatorname{erf}(x)\approx\frac{2x}{\sqrt\pi}$ near $0$. The jumps of $\varphi$ are smoothed instantly, and the solution is positive everywhere for $t>0$.

### 6.4.2. The Wave Equation on the Line

For the **wave equation** $u_{tt}=c^2u_{xx}$ on $\mathbb{R}$ with $u(x,0)=\varphi(x)$ and $u_t(x,0)=\psi(x)$, transforming gives $\hat u_{tt}=-c^2\xi^2\hat u$, so

$$
\hat u(\xi,t)=\hat\varphi(\xi)\cos(c\xi t)+\hat\psi(\xi)\frac{\sin(c\xi t)}{c\xi}.
$$
Now $\cos(c\xi t)\hat\varphi=\frac12\big(\mathrm{e}^{\mathrm{i}c\xi t}+\mathrm{e}^{-\mathrm{i}c\xi t}\big)\hat\varphi$, which by the translation rule is the transform of $\frac12\big(\varphi(x+ct)+\varphi(x-ct)\big)$. By Example 6.2.1 with $a=ct$, $\frac{\sin(c\xi t)}{c\xi}$ is the transform of $\frac1{2c}\boldsymbol{1}_{[-ct,ct]}$, and its product with $\hat\psi$ is the transform of the convolution $\frac1{2c}\int_{x-ct}^{x+ct}\psi(y)\,\mathrm{d}y$. Therefore

$$
u(x,t)=\frac{\varphi(x+ct)+\varphi(x-ct)}2+\frac1{2c}\int_{x-ct}^{x+ct}\psi(y)\,\mathrm{d}y,
$$
which is **d'Alembert's formula** ([2.5.3](/2.5.3)). Comparing the two equations in the frequency domain explains their different behavior: for the heat equation the factor $\mathrm{e}^{-k\xi^2t}$ damps every frequency, while for the wave equation the factors $\mathrm{e}^{\pm\mathrm{i}c\xi t}$ have modulus 1, so no frequency is damped and singularities of the data propagate without being smoothed.

### 6.4.3. The Laplace Equation in the Upper Half-Plane

Find a bounded **harmonic function** in the upper half-plane with prescribed boundary values:

$$
u_{xx}+u_{yy}=0,\quad x\in\mathbb{R},\ y>0;\qquad u(x,0)=f(x),\qquad u\text{ bounded}.
$$
Transforming in $x$ gives $\hat u_{yy}=\xi^2\hat u$, so $\hat u=A(\xi)\mathrm{e}^{-\lvert\xi\rvert y}+B(\xi)\mathrm{e}^{\lvert\xi\rvert y}$. The second term grows exponentially in $y$ and is excluded by boundedness, and $A=\hat f$:

$$
\hat u(\xi,y)=\hat f(\xi)\,\mathrm{e}^{-\lvert\xi\rvert y}.
$$
By (6.6) with $a=y$, $\mathrm{e}^{-\lvert\xi\rvert y}$ is the transform of $P_y(x)=\frac{y}{\pi(x^2+y^2)}$, and the convolution theorem gives

$$
u(x,y)=(P_y*f)(x)=\frac y\pi\int_{-\infty}^\infty\frac{f(s)}{(x-s)^2+y^2}\,\mathrm{d}s.\tag{6.10}
$$
The function $P_y$ is the Poisson kernel of the half-plane; it is positive, has integral 1, and $P_y=K_y$ for $K(x)=\frac1{\pi(1+x^2)}$, so by Lemma 6.3.1 $u(x,y)\to f(x)$ as $y\to0^+$ at every point of continuity of a bounded $f$. In [2.5.8](/2.5.8) the same formula is obtained from a Green's function, and for the disk from a conformal map.

**Example 6.4.2** Let $f=\boldsymbol{1}_{[-1,1]}$. Then

$$
u(x,y)=\frac1\pi\int_{-1}^1\frac{y\,\mathrm{d}s}{(s-x)^2+y^2}=\frac1\pi\Big[\arctan\frac{1-x}y+\arctan\frac{1+x}y\Big]=\frac{\alpha(x,y)}\pi,
$$
where $\alpha$ is the angle under which the segment $[-1,1]$ is seen from the point $(x,y)$. By the inscribed angle theorem the level curves $\alpha=\text{const}$ are circular arcs through $\pm1$. This angle is the argument of $\frac{z-1}{z+1}$, the imaginary part of an analytic function, which explains why it is harmonic ([2.5.8](/2.5.8)).

![Left: the Poisson kernel of the half-plane for several heights y, an approximate identity as y → 0. Right: the bounded harmonic function with boundary values 1 on (-1, 1) and 0 elsewhere; its level curves are circular arcs through ±1](./plots/half-plane-poisson.py)

## 6.5. The Laplace Transform

The Fourier transform requires $f$ to be (absolutely) integrable on the whole line. Functions such as $\mathrm{e}^{t}$ or $\sin t$ on $t\ge0$, typical of initial value problems, are not; multiplying them by a damping factor $\mathrm{e}^{-\sigma t}$ and restricting to $t\ge0$ repairs this. The result is the Laplace transform, which handles growing functions and builds the initial conditions into the transform.

### 6.5.1. Definition and Properties

We say that $f\colon[0,\infty)\to\mathbb{C}$ is of exponential order $\sigma_0$ if it is piecewise continuous and $\lvert f(t)\rvert\le M\mathrm{e}^{\sigma_0t}$ for some constant $M$ and all $t\ge0$.

**Definition 6.5.1 (Laplace Transform)** Let $f$ be of exponential order $\sigma_0$. The function

$$
F(s)=\mathscr{L}\{f\}(s)=\int_0^\infty f(t)\,\mathrm{e}^{-st}\,\mathrm{d}t,\qquad\operatorname{Re}s>\sigma_0,\tag{6.11}
$$
of the complex variable $s$ is called the **Laplace transform** of $f$.

For $s=\sigma+\mathrm{i}\omega$ with $\sigma>\sigma_0$, $F(\sigma+\mathrm{i}\omega)$ is the Fourier transform (in $\omega$) of $H(t)f(t)\mathrm{e}^{-\sigma t}$: the Laplace transform is a Fourier transform of a damped, one-sided function, viewed as a function of the complex frequency $s$.

**Theorem 6.5.1** If $f$ is of exponential order $\sigma_0$, then the integral (6.11) converges absolutely for $\operatorname{Re}s>\sigma_0$, $F$ is an **analytic function** in this half-plane with $F'(s)=-\mathscr{L}\{tf(t)\}(s)$, and $F(s)\to0$ as $\operatorname{Re}s\to+\infty$.

**Proof** For $\operatorname{Re}s=\sigma>\sigma_0$, $\lvert f(t)\mathrm{e}^{-st}\rvert\le M\mathrm{e}^{-(\sigma-\sigma_0)t}$, which is integrable, and $\lvert F(s)\rvert\le\frac{M}{\sigma-\sigma_0}\to0$. On every half-plane $\operatorname{Re}s\ge\sigma_1>\sigma_0$ the integrand and its $s$-derivative $-tf(t)\mathrm{e}^{-st}$ are dominated by $M\mathrm{e}^{-(\sigma_1-\sigma_0)t}$ and $Mt\mathrm{e}^{-(\sigma_1-\sigma_0)t}$, so the integrals converge uniformly and may be differentiated under the integral sign with respect to $s$; the complex derivative exists and equals $-\mathscr{L}\{tf\}$. $\square$

**Theorem 6.5.2** Let $f,g$ be of exponential order, and write $F=\mathscr{L}\{f\}$, $G=\mathscr{L}\{g\}$.

1. (Derivatives) If $f$ is continuous and $f'$ is of exponential order, then $\mathscr{L}\{f'\}=sF(s)-f(0)$; consequently $\mathscr{L}\{f''\}=s^2F(s)-sf(0)-f'(0)$;
2. (Integration) $\mathscr{L}\big\{\int_0^tf(\tau)\,\mathrm{d}\tau\big\}=\frac{F(s)}s$;
3. (Shift in $s$) $\mathscr{L}\{\mathrm{e}^{at}f(t)\}=F(s-a)$;
4. (Delay) for $a>0$, $\mathscr{L}\{H(t-a)f(t-a)\}=\mathrm{e}^{-as}F(s)$;
5. (Convolution) with $(f*g)(t)=\int_0^tf(t-\tau)g(\tau)\,\mathrm{d}\tau$, $\mathscr{L}\{f*g\}=F(s)G(s)$.

**Proof** 1: Integration by parts gives $\int_0^Rf'\mathrm{e}^{-st}\,\mathrm{d}t=f(R)\mathrm{e}^{-sR}-f(0)+s\int_0^Rf\mathrm{e}^{-st}\,\mathrm{d}t$, and $f(R)\mathrm{e}^{-sR}\to0$ for $\operatorname{Re}s$ large. 2 follows from 1 applied to $\int_0^tf$. 3 and 4 are substitutions. 5 is the convolution theorem (Theorem 6.2.4) for the functions $H(t)f(t)\mathrm{e}^{-\sigma t}$ and $H(t)g(t)\mathrm{e}^{-\sigma t}$, whose convolution on $\mathbb{R}$ is $H(t)(f*g)(t)\mathrm{e}^{-\sigma t}$. $\square$

Property 1 is the reason for using the Laplace transform: a linear ODE with constant coefficients and its initial conditions become a single algebraic equation for $F$. The convolution in 5 is the one-sided convolution; it agrees with Definition 6.2.2 for functions vanishing on $t<0$.

| $f(t)$, $t>0$ | $F(s)$ | Region |
|---|---|---|
| $1$ | $\dfrac1s$ | $\operatorname{Re}s>0$ |
| $t^n$ ($n\in\mathbb{N}$) | $\dfrac{n!}{s^{n+1}}$ | $\operatorname{Re}s>0$ |
| $t^\alpha$ ($\alpha>-1$) | $\dfrac{\Gamma(\alpha+1)}{s^{\alpha+1}}$ | $\operatorname{Re}s>0$ |
| $\mathrm{e}^{at}$ | $\dfrac1{s-a}$ | $\operatorname{Re}s>\operatorname{Re}a$ |
| $\cos\omega t$, $\sin\omega t$ | $\dfrac{s}{s^2+\omega^2}$, $\dfrac{\omega}{s^2+\omega^2}$ | $\operatorname{Re}s>0$ |
| $\operatorname{erfc}\dfrac{a}{2\sqrt t}$ ($a>0$) | $\dfrac{\mathrm{e}^{-a\sqrt s}}{s}$ | $\operatorname{Re}s>0$ |
| $\dfrac{a}{2\sqrt\pi\,t^{3/2}}\mathrm{e}^{-a^2/(4t)}$ ($a>0$) | $\mathrm{e}^{-a\sqrt s}$ | $\operatorname{Re}s>0$ |

The entry for $t^\alpha$ is the integral defining the **gamma function** after the substitution $st=u$ (for complex $s$, by analytic continuation from real $s$); in the last two rows $\sqrt s$ is the principal branch. The function $t^\alpha$ with $-1<\alpha<0$ is not piecewise continuous at $0$, but (6.11) still converges.

### 6.5.2. Inversion: The Bromwich Integral

**Theorem 6.5.3 (Bromwich Inversion Formula)** Let $f$ be of exponential order $\sigma_0$ and piecewise smooth on every bounded interval, and let $\gamma>\sigma_0$. Then for $t>0$

$$
\frac{f(t^+)+f(t^-)}2=\frac1{2\pi\mathrm{i}}\lim_{R\to\infty}\int_{\gamma-\mathrm{i}R}^{\gamma+\mathrm{i}R}F(s)\,\mathrm{e}^{st}\,\mathrm{d}s,\tag{6.12}
$$
where the integral is taken along the vertical line $\operatorname{Re}s=\gamma$. For $t<0$ the right-hand side equals $0$.

**Proof** The function $g(t)=H(t)f(t)\mathrm{e}^{-\gamma t}$ is absolutely integrable on $\mathbb{R}$ and piecewise smooth, and $\hat g(\omega)=\int_0^\infty f(t)\mathrm{e}^{-(\gamma+\mathrm{i}\omega)t}\,\mathrm{d}t=F(\gamma+\mathrm{i}\omega)$. Part 2 of Theorem 6.3.1 gives

$$
\frac{g(t^+)+g(t^-)}2=\frac1{2\pi}\lim_{R\to\infty}\int_{-R}^RF(\gamma+\mathrm{i}\omega)\,\mathrm{e}^{\mathrm{i}\omega t}\,\mathrm{d}\omega.
$$
Multiply by $\mathrm{e}^{\gamma t}$ and substitute $s=\gamma+\mathrm{i}\omega$, $\mathrm{d}s=\mathrm{i}\,\mathrm{d}\omega$. $\square$

The integral in (6.12) is called the *Bromwich integral*, and the line $\operatorname{Re}s=\gamma$ the Bromwich contour. Its value does not depend on $\gamma>\sigma_0$: by **Cauchy's integral theorem**, two such lines can be joined by horizontal segments whose contribution vanishes. In practice the integral is evaluated with the **residue theorem** by closing the contour to the left, where the factor $\mathrm{e}^{st}$ is small for $t>0$.

**Theorem 6.5.4 (Inversion by Residues)** Suppose $F=\mathscr{L}\{f\}$ extends to a function analytic in $\mathbb{C}$ except for finitely many isolated singularities $s_1,\dots,s_N$, and $\max_{\lvert s\rvert=R}\lvert F(s)\rvert\to0$ as $R\to\infty$. Then for $t>0$ at points of continuity of $f$

$$
f(t)=\sum_{k=1}^N\operatorname{Res}\big(F(s)\mathrm{e}^{st},s_k\big).
$$

**Proof** (Sketch.) Choose $\gamma$ to the right of all $s_k$ and close the segment from $\gamma-\mathrm{i}R$ to $\gamma+\mathrm{i}R$ by the arc $C_R$ of the circle $\lvert s-\gamma\rvert=R$ lying in $\operatorname{Re}s<\gamma$. For large $R$ the closed contour encloses all singularities, and the residue theorem gives $\frac1{2\pi\mathrm{i}}\big(\int_{\text{segment}}+\int_{C_R}\big)F\mathrm{e}^{st}\,\mathrm{d}s=\sum_k\operatorname{Res}(F\mathrm{e}^{st},s_k)$. On $C_R$, $\lvert\mathrm{e}^{st}\rvert=\mathrm{e}^{t\operatorname{Re}s}$, and Jordan's lemma ([2.3.7](/2.3.7)), rotated by a quarter turn, shows $\int_{C_R}F\mathrm{e}^{st}\,\mathrm{d}s\to0$ for $t>0$. Letting $R\to\infty$ and using (6.12) proves the claim. $\square$

For a rational function $F=P/Q$ with $\deg P<\deg Q$ the hypotheses hold. If all poles are simple, $\operatorname{Res}(F\mathrm{e}^{st},s_k)=\frac{P(s_k)}{Q'(s_k)}\mathrm{e}^{s_kt}$ and $f(t)=\sum_k\frac{P(s_k)}{Q'(s_k)}\mathrm{e}^{s_kt}$, which is the same as inverting the **partial fraction decomposition** of $F$ term by term. Each pole $s_k$ contributes a mode $\mathrm{e}^{s_kt}$: poles in the left half-plane give decaying modes, poles on the imaginary axis oscillations, and poles of order $m$ produce factors $t^{m-1}$.

**Example 6.5.1** Invert $F(s)=\dfrac1{s(s+1)^2}$.

**Solution** The pole $s=0$ is simple, with residue $\frac{\mathrm{e}^{st}}{(s+1)^2}\big|_{s=0}=1$. The pole $s=-1$ is double, with residue $\frac{\mathrm{d}}{\mathrm{d}s}\frac{\mathrm{e}^{st}}{s}\big|_{s=-1}=\big(\frac{t}{s}-\frac1{s^2}\big)\mathrm{e}^{st}\big|_{s=-1}=-(t+1)\mathrm{e}^{-t}$. Hence $f(t)=1-(1+t)\mathrm{e}^{-t}$.

### 6.5.3. Applications

**Example 6.5.2 (Resonance)** Solve the **initial value problem** $y''+y=\sin t$, $y(0)=y'(0)=0$.

**Solution** By Theorem 6.5.2, $(s^2+1)Y(s)=\frac{1}{s^2+1}$, so $Y=\frac1{(s^2+1)^2}$, with double poles at $\pm\mathrm{i}$. At $s=\mathrm{i}$,

$$
\operatorname{Res}\Big(\frac{\mathrm{e}^{st}}{(s-\mathrm{i})^2(s+\mathrm{i})^2},\mathrm{i}\Big)=\frac{\mathrm{d}}{\mathrm{d}s}\frac{\mathrm{e}^{st}}{(s+\mathrm{i})^2}\Big|_{s=\mathrm{i}}=\frac{t\mathrm{e}^{\mathrm{i}t}}{(2\mathrm{i})^2}-\frac{2\mathrm{e}^{\mathrm{i}t}}{(2\mathrm{i})^3}=-\frac{t\mathrm{e}^{\mathrm{i}t}}4-\frac{\mathrm{i}\,\mathrm{e}^{\mathrm{i}t}}{4},
$$
and the residue at $-\mathrm{i}$ is its complex conjugate (because $Y$ is real on the real axis). Adding,

$$
y(t)=2\operatorname{Re}\Big(-\frac{t\mathrm{e}^{\mathrm{i}t}}4-\frac{\mathrm{i}\,\mathrm{e}^{\mathrm{i}t}}{4}\Big)=\frac{\sin t-t\cos t}2.
$$
The forcing frequency equals the natural frequency, the double poles produce the factor $t$, and the amplitude grows linearly: resonance.

**Example 6.5.3 (A Semi-Infinite Rod with a Heated End)** A rod $x>0$, initially at temperature $0$, has its end held at the constant temperature $T_0$ from time $0$ on:

$$
u_t=k u_{xx}\ (x>0,\ t>0),\qquad u(x,0)=0,\qquad u(0,t)=T_0,\qquad u\text{ bounded}.
$$

**Solution** Transform in $t$, writing $U(x,s)=\mathscr{L}\{u(x,\cdot)\}(s)$. By Theorem 6.5.2 and $u(x,0)=0$, $sU=k U_{xx}$, so $U=A(s)\mathrm{e}^{-x\sqrt{s/k}}+B(s)\mathrm{e}^{x\sqrt{s/k}}$ with the principal branch of the square root ($\operatorname{Re}\sqrt s>0$). Boundedness in $x$ forces $B=0$, and $U(0,s)=T_0/s$ gives

$$
U(x,s)=T_0\frac{\mathrm{e}^{-x\sqrt{s/k}}}{s}.
$$
By the table with $a=x/\sqrt k$,

$$
u(x,t)=T_0\operatorname{erfc}\Big(\frac{x}{2\sqrt{k t}}\Big).
$$
One checks directly that this function satisfies the equation and the conditions. Here $F$ has a branch point at $s=0$, so Theorem 6.5.4 does not apply; the inversion in the table is obtained by deforming the Bromwich contour into a contour that wraps around the branch cut along the negative real axis. The heat penetrates to a depth of order $\sqrt{k t}$, so doubling the depth takes four times as long. If the end temperature is a function $h(t)$ instead of $T_0$, then $U=\mathscr{L}\{h\}\cdot\mathrm{e}^{-x\sqrt{s/k}}$, and the convolution rule together with the last row of the table gives

$$
u(x,t)=\int_0^th(\tau)\,\frac{x}{2\sqrt{\pi k}\,(t-\tau)^{3/2}}\,\mathrm{e}^{-x^2/(4k(t-\tau))}\,\mathrm{d}\tau.
$$

## Summary

| | Fourier transform | Laplace transform |
|---|---|---|
| Definition | $\hat f(\xi)=\int_{\mathbb{R}}f(x)\mathrm{e}^{-\mathrm{i}\xi x}\,\mathrm{d}x$ | $F(s)=\int_0^\infty f(t)\mathrm{e}^{-st}\,\mathrm{d}t$ |
| Functions | Absolutely (or square) integrable on $\mathbb{R}$ | Exponential order on $[0,\infty)$ |
| Inversion | $f=\frac1{2\pi}\int_{\mathbb{R}}\hat f(\xi)\mathrm{e}^{\mathrm{i}\xi x}\,\mathrm{d}\xi$ | $f=\frac1{2\pi\mathrm{i}}\int_{\gamma-\mathrm{i}\infty}^{\gamma+\mathrm{i}\infty}F(s)\mathrm{e}^{st}\,\mathrm{d}s$, by residues |
| Derivative | $f'\mapsto\mathrm{i}\xi\hat f$ | $f'\mapsto sF-f(0)$ |
| Convolution | $\int_{\mathbb{R}}f(x-y)g(y)\,\mathrm{d}y\mapsto\hat f\hat g$ | $\int_0^tf(t-\tau)g(\tau)\,\mathrm{d}\tau\mapsto FG$ |
| Typical use | Spatial variable on $\mathbb{R}$: heat, wave and Laplace equations | Time variable with initial data: ODEs, semi-infinite problems |

Key pairs: $\mathrm{e}^{-ax^2}\mapsto\sqrt{\pi/a}\,\mathrm{e}^{-\xi^2/(4a)}$; $\mathrm{e}^{-a\lvert x\rvert}\mapsto\frac{2a}{a^2+\xi^2}$; $\boldsymbol{1}_{[-a,a]}\mapsto\frac{2\sin a\xi}{\xi}$; $\frac{a}{\pi(a^2+x^2)}\mapsto\mathrm{e}^{-a\lvert\xi\rvert}$. Key facts: smoothness of $f$ $\leftrightarrow$ decay of $\hat f$; Plancherel $\int\lvert f\rvert^2=\frac1{2\pi}\int\lvert\hat f\rvert^2$; uncertainty $\sigma_x\sigma_\xi\ge\frac12$.
