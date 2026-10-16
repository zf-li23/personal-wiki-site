---
title: Antiderivatives and Indefinite Integrals
source_hash: a16a67bea75e
---

The basic problem of differential calculus is to find the derivative of a given function. This chapter treats the inverse problem: given a derivative $f$, find a function $F$ with $F' = f$. This is the problem of finding an antiderivative, or computing an indefinite integral, and it is the inverse of differentiation. Because the rules of differentiation can be applied mechanically, the derivative of every elementary function can be computed; finding antiderivatives, by contrast, has no general algorithm. There are only a few basic methods (substitution, integration by parts, and systematic treatments of rational functions, rational functions of sines and cosines, and a few classes of irrational functions), and each of them is some differentiation rule read backwards. A small change in the form of the integrand can turn an easy integral into a hard one, or even into one whose antiderivative cannot be expressed in elementary functions. This chapter relies on the differentiation formulas of [2.2.4](/2.2.4) and on the **mean value theorem** of [2.2.5](/2.2.5); in the next chapter ([2.2.7](/2.2.7)) the **fundamental theorem of calculus** reduces the evaluation of definite integrals to finding antiderivatives, and the solution of ordinary differential equations ([2.2.15](/2.2.15)) makes heavy use of the integration techniques developed here.

## 6.1. The Indefinite Integral and Its Properties

### 6.1.1. Antiderivatives

**Definition 6.1.1 (Antiderivative)** Let $f$ be defined on an interval $I$. If there is a function $F$ such that $F'(x) = f(x)$ on $I$, then $F$ is called an **antiderivative** of $f$ on $I$.

For example, on $(-\infty,+\infty)$, $\frac12x^2$ is an antiderivative of $x$, and $-\cos x$ is an antiderivative of $\sin x$. An antiderivative, if it exists, is not unique: if $F$ is one, so is $F+C$. Conversely, any two antiderivatives differ only by a constant:

**Theorem 6.1.1** If $F$ and $G$ are both antiderivatives of $f$ on an interval $I$, then $G(x) = F(x)+C$ for some constant $C$.

**Proof** $(G-F)' = f-f = 0$, so by Corollary 5.1.1, $G-F$ is constant on $I$. $\square$

The hypothesis that $I$ is an interval cannot be dropped: on $(-\infty,0)\cup(0,+\infty)$, both $\ln|x|$ and $\ln|x|+\operatorname{sgn}x$ are antiderivatives of $\frac1x$, but their difference is not constant.

### 6.1.2. The Indefinite Integral

**Definition 6.1.2 (Indefinite Integral)** The set of all antiderivatives of $f$ on an interval $I$, that is, of all functions $F$ with $\mathrm{d}F(x) = f(x)\,\mathrm{d}x$, is called the **indefinite integral** of $f$ on $I$ and is denoted by $\int f(x)\,\mathrm{d}x$. The function $f$ is called the integrand, and $f(x)\,\mathrm{d}x$ the integrand expression.

By Theorem 6.1.1, if $F$ is one antiderivative of $f$ on $I$, then

$$
\int f(x)\,\mathrm{d}x = F(x)+C,
$$

where $C$ is an arbitrary constant (the constant of integration). Indefinite integration is "antidifferentiation": from the differential $f(x)\,\mathrm{d}x = \mathrm{d}F(x)$ we recover all such $F$. The two operations are inverse to each other (up to a constant):

$$
\int\mathrm{d}F(x) = F(x)+C,\qquad\mathrm{d}\Bigl(\int f(x)\,\mathrm{d}x\Bigr) = f(x)\,\mathrm{d}x,\qquad\Bigl(\int f(x)\,\mathrm{d}x\Bigr)' = f(x).
$$

Geometrically, the graph of an antiderivative $y = F(x)$ is called an integral curve of $f$. The indefinite integral is a family of integral curves $y = F(x)+C$, each obtained from any other by a vertical translation; at a common abscissa $x_0$ the tangent lines of all these curves are parallel, with slope $f(x_0)$. Prescribing one point through which the curve passes (an initial condition) determines the constant $C$; this is the initial value problem for the simplest differential equation $y' = f(x)$.

![The family of integral curves y = x³/3 − x + C of f(x) = x² − 1 together with its slope field: the slope of each segment depends only on x, and at x = x₀ the tangent lines of all curves are parallel](./plots/integral-curves.py)

### 6.1.3. Table of Basic Integrals

Reading the table of derivatives in [2.2.4](/2.2.4) backwards gives the basic integration formulas:

| Integral | Result | Integral | Result |
|---|---|---|---|
| $\int0\,\mathrm{d}x$ | $C$ | $\int\mathrm{d}x$ | $x+C$ |
| $\int x^p\,\mathrm{d}x$ ($p\ne-1$) | $\frac{x^{p+1}}{p+1}+C$ | $\int\frac1x\,\mathrm{d}x$ | $\ln\lvert x\rvert+C$ |
| $\int a^x\,\mathrm{d}x$ ($a>0$, $a\ne1$) | $\frac{a^x}{\ln a}+C$ | $\int\mathrm{e}^x\,\mathrm{d}x$ | $\mathrm{e}^x+C$ |
| $\int\sin x\,\mathrm{d}x$ | $-\cos x+C$ | $\int\cos x\,\mathrm{d}x$ | $\sin x+C$ |
| $\int\sec^2x\,\mathrm{d}x$ | $\tan x+C$ | $\int\csc^2x\,\mathrm{d}x$ | $-\cot x+C$ |
| $\int\sec x\tan x\,\mathrm{d}x$ | $\sec x+C$ | $\int\csc x\cot x\,\mathrm{d}x$ | $-\csc x+C$ |
| $\int\frac{\mathrm{d}x}{\sqrt{1-x^2}}$ | $\arcsin x+C = -\arccos x+C_1$ | $\int\frac{\mathrm{d}x}{1+x^2}$ | $\arctan x+C = -\operatorname{arccot}x+C_1$ |

The last row shows that the same indefinite integral can be written in different forms, which differ only by a constant ($\arcsin x+\arccos x = \frac\pi2$). To check an integration, it suffices to differentiate the result.

### 6.1.4. Existence of Antiderivatives

**Theorem 6.1.2** If $f$ is continuous on an interval $I$, then $f$ has an antiderivative on $I$.

The proof requires the definite integral (an integral with variable upper limit); see [2.2.7](/2.2.7). Consequently, every **elementary function** has an antiderivative on each interval of its domain.

Continuity is sufficient, but not necessary, for the existence of an antiderivative. Let $F(x) = x^2\sin\frac1x$ ($x\ne0$) and $F(0) = 0$. By Example 4.1.6,

$$
F'(x) = f(x) = \begin{cases}2x\sin\frac1x-\cos\frac1x, & x\ne0,\\ 0, & x = 0,\end{cases}
$$

so $f$ has the antiderivative $F$ on $(-\infty,+\infty)$, although $f$ is discontinuous at $0$. On the other hand, by **Darboux's theorem** a derivative has no **discontinuity of the first kind**, so a function with a **jump discontinuity** or a **removable discontinuity** inside an interval has no antiderivative there. For example, the **sign function** $\operatorname{sgn}x$ has no antiderivative on $(-\infty,+\infty)$ (though it certainly has one on any interval not containing $0$).

Note also that "having an antiderivative" and "having an elementary antiderivative" are different things. The functions $\mathrm{e}^{-x^2}$, $\frac{\sin x}{x}$, $\frac1{\ln x}$ and $\sqrt{1-k^2\sin^2x}$ ($0<k<1$) are all continuous and hence have antiderivatives, but one can prove (a theorem of Liouville) that none of these antiderivatives is elementary: they "cannot be integrated in closed form". These functions are very important in probability (the normal distribution), signal processing and elliptic integrals, and can only be studied through definite integrals, series or numerical methods.

### 6.1.5. Linearity of the Indefinite Integral

**Theorem 6.1.3** If $f$ and $g$ both have antiderivatives on an interval $I$ and $k, l$ are constants, then

$$
\int\bigl(kf(x)+lg(x)\bigr)\,\mathrm{d}x = k\int f(x)\,\mathrm{d}x+l\int g(x)\,\mathrm{d}x,
$$
where $k, l$ are not both zero (both sides contain arbitrary constants, and the equation is understood as an equality of two families of functions).

**Proof** Differentiating the right-hand side and using the linearity of differentiation gives $kf+lg$. $\square$

Using linearity to split the integrand into a sum of functions from the table of basic integrals is the most direct method of integration.

**Example 6.1.1** Evaluate: (1) $\int(x^2+2^x)\,\mathrm{d}x$; (2) $\int\frac{x^4}{1+x^2}\,\mathrm{d}x$; (3) $\int\frac{\mathrm{d}x}{a^2-x^2}$ ($a>0$); (4) $\int\frac{\cos2x}{\sin x-\cos x}\,\mathrm{d}x$; (5) $\int f(x)\,\mathrm{d}x$, where $f(x) = 2x$ for $x\le1$ and $f(x) = 2x^2$ for $x>1$.

Solution. (1) $\frac13x^3+\frac{2^x}{\ln2}+C$.

(2) 
$$
\int\frac{x^4-1+1}{1+x^2}\,\mathrm{d}x = \int\Bigl(x^2-1+\frac1{1+x^2}\Bigr)\,\mathrm{d}x = \frac13x^3-x+\arctan x+C.
$$

(3) 
$$
\int\frac1{2a}\Bigl(\frac1{a+x}+\frac1{a-x}\Bigr)\,\mathrm{d}x = \frac1{2a}\bigl(\ln\lvert a+x\rvert-\ln\lvert a-x\rvert\bigr)+C = \frac1{2a}\ln\Bigl\lvert\frac{a+x}{a-x}\Bigr\rvert+C.
$$

(4) Since $\cos2x = (\cos x-\sin x)(\cos x+\sin x)$, the integral equals $-\int(\sin x+\cos x)\,\mathrm{d}x = \cos x-\sin x+C$.

(5) Find antiderivatives piece by piece: $x^2+C$ for $x<1$ and $\frac23x^3+C_1$ for $x>1$. An antiderivative is differentiable, hence continuous at $x = 1$, so $1+C = \frac23+C_1$, that is, $C_1 = C+\frac13$. Therefore

$$
\int f(x)\,\mathrm{d}x = \begin{cases}x^2, & x\le1,\\ \frac23x^3+\frac13, & x>1\end{cases}\ +\ C.
$$

(One should also check that this function is differentiable at $x = 1$ with derivative $f(1) = 2$: both one-sided derivatives equal $2$.)

## 6.2. Integration by Substitution

### 6.2.1. The First Substitution Rule

Reading the chain rule $\bigl(F(\varphi(x))\bigr)' = F'(\varphi(x))\varphi'(x)$ backwards gives the first substitution rule.

**Theorem 6.2.1 (First Substitution Rule)** If $\int f(u)\,\mathrm{d}u = F(u)+C$ and $\varphi$ is differentiable, then

$$
\int f(\varphi(x))\varphi'(x)\,\mathrm{d}x = \int f(\varphi(x))\,\mathrm{d}\varphi(x) \overset{u = \varphi(x)}{=} \int f(u)\,\mathrm{d}u = F(\varphi(x))+C.
$$

**Proof** By the chain rule, $\bigl(F(\varphi(x))\bigr)' = f(\varphi(x))\varphi'(x)$. $\square$

By the **invariance of the first differential**, $\varphi'(x)\,\mathrm{d}x = \mathrm{d}\varphi(x)$, so applying the first substitution rule amounts to rewriting the integrand expression in the form $f(\varphi(x))\,\mathrm{d}\varphi(x)$, that is, to recognizing a differential $\mathrm{d}\varphi(x)$ inside it. Given $\int g(x)\,\mathrm{d}x$, the key step is not the substitution itself but recognizing a factorization $g = f(\varphi(x))\varphi'(x)$. There are two ways to look for one:

1. The integrand $g = g_1g_2$ contains a fairly complicated composite factor $f(\varphi(x))$. Try $u = \varphi(x)$ and see whether the remaining factor is exactly $\varphi'(x)$ (up to a constant multiple). Examples: $\frac{\cos(\ln x)}{x}$, $\cos^3x\sin x$, $\frac{\sin(\arctan x)}{1+x^2}$, $a^{\cos x}\sin x$.
2. The integrand contains a factor $g_2$ that is the derivative of some $\varphi$; then check whether the rest can be written as a function of $\varphi$. For example,

$$
\frac{\cos x}{\sin x} = \frac{(\sin x)'}{\sin x},\qquad\frac1{\sin x} = \frac{\sin x}{1-\cos^2x} = -\frac{(\cos x)'}{1-\cos^2x},\qquad\frac1{x\ln x} = \frac{(\ln x)'}{\ln x},\qquad\frac1{x\ln x\ln\ln x} = \frac{(\ln\ln x)'}{\ln\ln x}.
$$

Frequently used differentials: $\mathrm{d}x = \frac1a\mathrm{d}(ax+b)$, $x\,\mathrm{d}x = \frac12\mathrm{d}(x^2)$, $\frac{\mathrm{d}x}{x} = \mathrm{d}\ln x$, $\frac{\mathrm{d}x}{\sqrt x} = 2\,\mathrm{d}\sqrt x$, $\cos x\,\mathrm{d}x = \mathrm{d}\sin x$, $\sec^2x\,\mathrm{d}x = \mathrm{d}\tan x$, $\frac{\mathrm{d}x}{1+x^2} = \mathrm{d}\arctan x$, $\mathrm{e}^x\,\mathrm{d}x = \mathrm{d}\,\mathrm{e}^x$.

**Example 6.2.1** Evaluate the following integrals.

(1) $\int x\sin x^2\,\mathrm{d}x\overset{u = x^2}{=}\frac12\int\sin u\,\mathrm{d}u = -\frac12\cos x^2+C$.

(2) $\int\frac{\cos(\ln x)}{x}\,\mathrm{d}x = \int\cos(\ln x)\,\mathrm{d}\ln x = \sin(\ln x)+C$.

(3) $\int\tan x\,\mathrm{d}x = -\int\frac{\mathrm{d}\cos x}{\cos x} = -\ln\lvert\cos x\rvert+C$; similarly $\int\cot x\,\mathrm{d}x = \ln\lvert\sin x\rvert+C$.

(4) $\int\frac{\mathrm{d}x}{a^2+x^2} = \frac1a\int\frac{\mathrm{d}(x/a)}{1+(x/a)^2} = \frac1a\arctan\frac xa+C$.

(5) $\int\frac{\mathrm{d}x}{\sqrt{a^2-x^2}} = \int\frac{\mathrm{d}(x/a)}{\sqrt{1-(x/a)^2}} = \arcsin\frac xa+C$ ($a>0$).

(6) 
$$
\int\sec x\,\mathrm{d}x = \int\frac{\cos x\,\mathrm{d}x}{\cos^2x} = \int\frac{\mathrm{d}\sin x}{1-\sin^2x} = \frac12\ln\Bigl\lvert\frac{1+\sin x}{1-\sin x}\Bigr\rvert+C = \ln\Bigl\lvert\frac{1+\sin x}{\cos x}\Bigr\rvert+C = \ln\lvert\sec x+\tan x\rvert+C,
$$

where the third step uses Example 6.1.1 (3) and the fourth multiplies numerator and denominator by $1+\sin x$. Similarly, $\int\csc x\,\mathrm{d}x = \ln\lvert\csc x-\cot x\rvert+C$.

(7) On the domain $(0,1)$, $\int\frac{\mathrm{d}x}{\sqrt{x(1-x)}} = 2\int\frac{\mathrm{d}\sqrt x}{\sqrt{1-(\sqrt x)^2}} = 2\arcsin\sqrt x+C$.

(8) $\int\frac{(x-1)\,\mathrm{d}x}{\sqrt{2-2x+x^2}}\overset{u = x-1}{=}\int\frac{u\,\mathrm{d}u}{\sqrt{1+u^2}} = \frac12\int\frac{\mathrm{d}(1+u^2)}{\sqrt{1+u^2}} = \sqrt{2-2x+x^2}+C$.

(9) Put $u = x^2$, then split the numerator into a multiple of the derivative of the denominator plus a constant:

$$
\int\frac{x^3\,\mathrm{d}x}{x^4-2x^2+2} = \frac12\int\frac{u\,\mathrm{d}u}{u^2-2u+2} = \frac14\int\frac{\mathrm{d}(u^2-2u+2)}{u^2-2u+2}+\frac12\int\frac{\mathrm{d}(u-1)}{(u-1)^2+1} = \frac14\ln(x^4-2x^2+2)+\frac12\arctan(x^2-1)+C.
$$

**Example 6.2.2** Suppose $f'(\cos x+2) = \sin^2x+\tan^2x$. Find $f(x)$.

Solution. Let $u = \cos x+2$. Then $\cos x = u-2$ and $\sin^2x+\tan^2x = 1-\cos^2x+\frac1{\cos^2x}-1 = -(u-2)^2+\frac1{(u-2)^2}$. Hence $f'(x) = -(x-2)^2+\frac{1}{(x-2)^2}$, and

$$
f(x) = -\frac13(x-2)^3-\frac1{x-2}+C.
$$

### 6.2.2. The Second Substitution Rule

The first substitution rule simplifies $f(\varphi(x))\varphi'(x)$ to $f(u)$. Sometimes we need the opposite direction: the integrand $f(x)$ itself is hard to integrate, but after substituting $x = \varphi(t)$ the function $f(\varphi(t))\varphi'(t)$ becomes easy. The typical use is to eliminate a radical.

**Theorem 6.2.2 (Second Substitution Rule)** Let $f$ be continuous, and let $x = \varphi(t)$ have a continuous derivative with $\varphi'(t)\ne0$ (so that it has an inverse $t = \varphi^{-1}(x)$). If

$$
\int f(\varphi(t))\varphi'(t)\,\mathrm{d}t = G(t)+C,
$$
then $\int f(x)\,\mathrm{d}x = G\bigl(\varphi^{-1}(x)\bigr)+C$.

**Proof** By the chain rule and the rule for differentiating inverse functions,

$$
\frac{\mathrm{d}}{\mathrm{d}x}G\bigl(\varphi^{-1}(x)\bigr) = G'(t)\frac{\mathrm{d}t}{\mathrm{d}x} = f(\varphi(t))\varphi'(t)\cdot\frac1{\varphi'(t)} = f(\varphi(t)) = f(x). \qquad\square
$$

The two substitution rules go in opposite directions:

$$
\int f(\varphi(x))\varphi'(x)\,\mathrm{d}x\overset{u = \varphi(x)}{=}\int f(u)\,\mathrm{d}u,\qquad\int f(x)\,\mathrm{d}x\overset{x = \varphi(t)}{=}\int f(\varphi(t))\varphi'(t)\,\mathrm{d}t.
$$

In the second rule the substitution must be invertible, because at the end we substitute back $t = \varphi^{-1}(x)$. Common substitutions for integrands containing radicals:

| Integrand contains | Substitution | Range |
|---|---|---|
| $\sqrt{x+1}$ or, generally, $\sqrt[n]{ax+b}$ | $ax+b = t^n$ | $t\ge0$ ($n$ even) |
| $\sqrt{a^2-x^2}$ | $x = a\sin t$ | $t\in\bigl(-\frac\pi2,\frac\pi2\bigr)$ |
| $\sqrt{a^2+x^2}$ | $x = a\tan t$ | $t\in\bigl(-\frac\pi2,\frac\pi2\bigr)$ |
| $\sqrt{x^2-a^2}$ | $x = a\sec t$ | $t\in\bigl(0,\frac\pi2\bigr)$ for $x>a$ |

After a trigonometric substitution, one can draw a right triangle to read off the relations between $\sin t$, $\cos t$, $\tan t$ and $x$ when substituting back.

**Example 6.2.3** Evaluate: (1) $\int\frac{\mathrm{d}x}{1+\sqrt{x+1}}$; (2) $\int\sqrt{a^2-x^2}\,\mathrm{d}x$; (3) $\int\frac{\mathrm{d}x}{\sqrt{x^2-a^2}}$; (4) $\int\frac{\mathrm{d}x}{\sqrt{x^2+a^2}}$; (5) $\int\frac{\mathrm{d}x}{x^2\sqrt{1+x^2}}$. (Here $a>0$.)

Solution. (1) Let $x+1 = t^2$, $t\ge0$, $\mathrm{d}x = 2t\,\mathrm{d}t$:

$$
\int\frac{2t\,\mathrm{d}t}{1+t} = 2\int\Bigl(1-\frac1{1+t}\Bigr)\mathrm{d}t = 2t-2\ln(1+t)+C = 2\sqrt{x+1}-2\ln\bigl(1+\sqrt{x+1}\bigr)+C.
$$

(2) Let $x = a\sin t$, $t\in\bigl[-\frac\pi2,\frac\pi2\bigr]$. Then $\sqrt{a^2-x^2} = a\cos t$ and $\mathrm{d}x = a\cos t\,\mathrm{d}t$:

$$
\int a^2\cos^2t\,\mathrm{d}t = \frac{a^2}2\int(1+\cos2t)\,\mathrm{d}t = \frac{a^2}2(t+\sin t\cos t)+C = \frac12\Bigl(a^2\arcsin\frac xa+x\sqrt{a^2-x^2}\Bigr)+C,
$$

where we substituted back using $\sin t = \frac xa$ and $\cos t = \frac1a\sqrt{a^2-x^2}$.

(3) For $x>a$, let $x = a\sec t$, $t\in\bigl(0,\frac\pi2\bigr)$, so $\sqrt{x^2-a^2} = a\tan t$ and $\mathrm{d}x = a\sec t\tan t\,\mathrm{d}t$:

$$
\int\sec t\,\mathrm{d}t = \ln\lvert\sec t+\tan t\rvert+C = \ln\Bigl\lvert\frac xa+\frac{\sqrt{x^2-a^2}}a\Bigr\rvert+C = \ln\bigl\lvert x+\sqrt{x^2-a^2}\bigr\rvert+C_1,
$$

where $C_1 = C-\ln a$. For $x<-a$, the substitution $x = -u$ reduces to the case $u>a$, and the result has the same form (alternatively, take $t\in\bigl(\pi,\frac{3\pi}2\bigr)$).

(4) Let $x = a\tan t$, $t\in\bigl(-\frac\pi2,\frac\pi2\bigr)$, so $\sqrt{x^2+a^2} = a\sec t$:

$$
\int\frac{a\sec^2t\,\mathrm{d}t}{a\sec t} = \ln\lvert\sec t+\tan t\rvert+C = \ln\bigl(x+\sqrt{x^2+a^2}\bigr)+C_1.
$$

(5) Method 1 (second substitution rule): let $x = \tan t$. Then

$$
\int\frac{\sec^2t\,\mathrm{d}t}{\tan^2t\sec t} = \int\frac{\cos t}{\sin^2t}\,\mathrm{d}t = -\frac1{\sin t}+C = -\frac{\sqrt{1+x^2}}{x}+C.
$$

Method 2 (reciprocal substitution): for $x>0$, let $x = \frac1u$ ($u>0$), so $\mathrm{d}x = -\frac{\mathrm{d}u}{u^2}$ and $x^2\sqrt{1+x^2} = \frac{\sqrt{u^2+1}}{u^3}$. The integral becomes $-\int\frac{u\,\mathrm{d}u}{\sqrt{u^2+1}} = -\sqrt{1+u^2}+C = -\frac{\sqrt{x^2+1}}{x}+C$; the case $x<0$ is similar. The reciprocal substitution is often effective when the denominator has a high power of $x$.

## 6.3. Integration by Parts

Integrating both sides of the product rule $(uv)' = u'v+uv'$ gives integration by parts.

**Theorem 6.3.1 (Integration by Parts)** If $u, v$ are differentiable and $u'v$ has an antiderivative, then

$$
\int u\,\mathrm{d}v = uv-\int v\,\mathrm{d}u,\qquad\text{i.e.}\qquad\int uv'\,\mathrm{d}x = uv-\int u'v\,\mathrm{d}x.
$$

**Proof** $\mathrm{d}(uv) = v\,\mathrm{d}u+u\,\mathrm{d}v$, so $u\,\mathrm{d}v = \mathrm{d}(uv)-v\,\mathrm{d}u$; integrate both sides. $\square$

Integration by parts converts $\int u\,\mathrm{d}v$ into $\int v\,\mathrm{d}u$; whenever the latter is easy, so is the former.

**Example 6.3.1** $\int x\sin3x\,\mathrm{d}x = \int x\,\mathrm{d}\Bigl(-\frac13\cos3x\Bigr) = -\frac13x\cos3x+\frac13\int\cos3x\,\mathrm{d}x = -\frac19(3x\cos3x-\sin3x)+C$.

How should we choose $u$ and $v'$ when integrating $\int f_1(x)f_2(x)\,\mathrm{d}x$ by parts? The principle is that $v'$ should be easy to integrate and $u$ should become simpler when differentiated.

1. If the product contains one of $\mathrm{e}^{ax}$, $\sin ax$ ($\cos ax$), $x^m$, it is usually chosen as $v'$, in the order of preference $\mathrm{e}^{ax}$, $\sin ax$ ($\cos ax$), $x^m$;
2. If the product contains one of $\arcsin x$, $\arccos x$, $\arctan x$, $\operatorname{arccot}x$, $\ln x$, it is usually chosen as $u$, and the remaining factor serves as $v'$ (with $v' = 1$ if there is only one factor).

**Example 6.3.2** Evaluate the following integrals.

(1) $\int x^2\ln x\,\mathrm{d}x = \int\ln x\,\mathrm{d}\frac{x^3}3 = \frac{x^3}3\ln x-\int\frac{x^3}3\cdot\frac1x\,\mathrm{d}x = \frac13x^3\ln x-\frac19x^3+C$.

(2) Integrate by parts twice, lowering the degree of the polynomial by one each time:

$$
\int x^2\mathrm{e}^{2x}\,\mathrm{d}x = \frac12x^2\mathrm{e}^{2x}-\int x\mathrm{e}^{2x}\,\mathrm{d}x = \frac12x^2\mathrm{e}^{2x}-\frac12x\mathrm{e}^{2x}+\frac12\int\mathrm{e}^{2x}\,\mathrm{d}x = \Bigl(\frac12x^2-\frac12x+\frac14\Bigr)\mathrm{e}^{2x}+C.
$$

(3) $\int\arctan x\,\mathrm{d}x = x\arctan x-\int\frac{x\,\mathrm{d}x}{1+x^2} = x\arctan x-\frac12\ln(1+x^2)+C$; similarly $\int\ln x\,\mathrm{d}x = x\ln x-x+C$.

(4) 
$$
\int\frac{\ln x}{(1+x)^2}\,\mathrm{d}x = -\int\ln x\,\mathrm{d}\frac1{1+x} = -\frac{\ln x}{1+x}+\int\Bigl(\frac1x-\frac1{1+x}\Bigr)\mathrm{d}x = -\frac{\ln x}{1+x}+\ln\frac{x}{1+x}+C = \frac{x\ln x}{1+x}-\ln(1+x)+C.
$$

(5) A recurring integral:

$$
\int\sqrt{a^2+x^2}\,\mathrm{d}x = x\sqrt{a^2+x^2}-\int\frac{x^2\,\mathrm{d}x}{\sqrt{a^2+x^2}} = x\sqrt{a^2+x^2}-\int\sqrt{a^2+x^2}\,\mathrm{d}x+a^2\int\frac{\mathrm{d}x}{\sqrt{a^2+x^2}}.
$$

The integral we want reappears on the right. Moving it to the left and using Example 6.2.3 (4),

$$
\int\sqrt{a^2+x^2}\,\mathrm{d}x = \frac12\Bigl(x\sqrt{a^2+x^2}+a^2\ln\bigl(x+\sqrt{a^2+x^2}\bigr)\Bigr)+C.
$$

Similarly, $\int\sqrt{x^2-a^2}\,\mathrm{d}x = \frac12\bigl(x\sqrt{x^2-a^2}-a^2\ln\lvert x+\sqrt{x^2-a^2}\rvert\bigr)+C$, and the same method applied to $\int\sqrt{a^2-x^2}\,\mathrm{d}x$ reproduces Example 6.2.3 (2).

(6) A reduction formula: let $I_n = \int\cos^nx\,\mathrm{d}x$. Then

$$
I_n = \int\cos^{n-1}x\,\mathrm{d}\sin x = \cos^{n-1}x\sin x+(n-1)\int\cos^{n-2}x\sin^2x\,\mathrm{d}x = \cos^{n-1}x\sin x+(n-1)(I_{n-2}-I_n),
$$

so

$$
I_n = \frac1n\cos^{n-1}x\sin x+\frac{n-1}nI_{n-2},\qquad n\ge2.
$$

Starting from $I_0 = x+C$ and $I_1 = \sin x+C$, we can compute every $I_n$. There is an analogous reduction formula for $\int\sin^nx\,\mathrm{d}x$.

(7), (8) Let $ab\ne0$. Integrating by parts twice,

$$
\int\mathrm{e}^{ax}\cos bx\,\mathrm{d}x = \frac{\mathrm{e}^{ax}}{a}\cos bx+\frac ba\int\mathrm{e}^{ax}\sin bx\,\mathrm{d}x,\qquad\int\mathrm{e}^{ax}\sin bx\,\mathrm{d}x = \frac{\mathrm{e}^{ax}}{a}\sin bx-\frac ba\int\mathrm{e}^{ax}\cos bx\,\mathrm{d}x,
$$

and solving this pair of equations gives

$$
\int\mathrm{e}^{ax}\cos bx\,\mathrm{d}x = \frac{\mathrm{e}^{ax}(a\cos bx+b\sin bx)}{a^2+b^2}+C,\qquad\int\mathrm{e}^{ax}\sin bx\,\mathrm{d}x = \frac{\mathrm{e}^{ax}(a\sin bx-b\cos bx)}{a^2+b^2}+C.
$$

With complex numbers this takes one step: $\int\mathrm{e}^{(a+\mathrm{i}b)x}\,\mathrm{d}x = \frac{\mathrm{e}^{(a+\mathrm{i}b)x}}{a+\mathrm{i}b}+C$; take the real and imaginary parts (**Euler's formula**).

(9) First integrate by parts, then substitute for the radical:

$$
\int\frac{x\mathrm{e}^x}{\sqrt{\mathrm{e}^x-3}}\,\mathrm{d}x = 2\int x\,\mathrm{d}\sqrt{\mathrm{e}^x-3} = 2x\sqrt{\mathrm{e}^x-3}-2\int\sqrt{\mathrm{e}^x-3}\,\mathrm{d}x.
$$

Let $t = \sqrt{\mathrm{e}^x-3}$, so $x = \ln(t^2+3)$ and $\mathrm{d}x = \frac{2t\,\mathrm{d}t}{t^2+3}$:

$$
\int\sqrt{\mathrm{e}^x-3}\,\mathrm{d}x = \int\frac{2t^2}{t^2+3}\,\mathrm{d}t = 2t-2\sqrt3\arctan\frac t{\sqrt3}+C.
$$

Hence the integral equals $2x\sqrt{\mathrm{e}^x-3}-4\sqrt{\mathrm{e}^x-3}+4\sqrt3\arctan\sqrt{\frac{\mathrm{e}^x-3}{3}}+C$.

(10) 
$$
\int\sec^3x\,\mathrm{d}x = \int\sec x\,\mathrm{d}\tan x = \sec x\tan x-\int\sec x\tan^2x\,\mathrm{d}x = \sec x\tan x-\int\sec^3x\,\mathrm{d}x+\int\sec x\,\mathrm{d}x,
$$

so $\int\sec^3x\,\mathrm{d}x = \frac12\bigl(\sec x\tan x+\ln\lvert\sec x+\tan x\rvert\bigr)+C$.

**Example 6.3.3** Let $I_k = \int\frac{\mathrm{d}x}{(x^2+a^2)^k}$ ($a>0$, $k\ge1$). Find a reduction formula.

Solution. Take $u = \frac1{(x^2+a^2)^k}$ and $v = x$:

$$
I_k = \frac{x}{(x^2+a^2)^k}+2k\int\frac{x^2\,\mathrm{d}x}{(x^2+a^2)^{k+1}} = \frac{x}{(x^2+a^2)^k}+2k\int\frac{(x^2+a^2)-a^2}{(x^2+a^2)^{k+1}}\,\mathrm{d}x = \frac{x}{(x^2+a^2)^k}+2kI_k-2ka^2I_{k+1}.
$$

Therefore

$$
I_{k+1} = \frac{2k-1}{2ka^2}I_k+\frac{x}{2ka^2(x^2+a^2)^k},\qquad I_1 = \frac1a\arctan\frac xa+C.
$$

This reduction formula is needed in Section 6.4 for integrating rational functions.

It is also common to substitute first and then integrate by parts:

**Example 6.3.4** (1) $\int\frac{\ln^2x\cos(\ln x)}{x}\,\mathrm{d}x\overset{u = \ln x}{=}\int u^2\cos u\,\mathrm{d}u = u^2\sin u+2u\cos u-2\sin u+C$, that is, $(\ln^2x-2)\sin\ln x+2\ln x\cos\ln x+C$.

(2) $\int\frac{\arctan x\,\mathrm{e}^{\arctan x}}{1+x^2}\,\mathrm{d}x\overset{u = \arctan x}{=}\int u\mathrm{e}^u\,\mathrm{d}u = (u-1)\mathrm{e}^u+C = (\arctan x-1)\mathrm{e}^{\arctan x}+C$.

## 6.4. Integration of Rational Functions

### 6.4.1. Rational Functions

**Definition 6.4.1** A function of the form $\frac{P_m(x)}{Q_n(x)}$, where $P_m$ and $Q_n$ are polynomials with real coefficients of degrees $m$ and $n$, is called a **rational function**. It is called a **proper rational function** if $m<n$, and an **improper rational function** if $m\ge n$.

By **division with remainder** of polynomials, $P_m = q\,Q_n+r$ with $\deg r<n$, so an improper rational function is always the sum of a polynomial and a proper rational function: $\frac{P_m}{Q_n} = q+\frac{r}{Q_n}$. Polynomials are easy to integrate, so the problem reduces to integrating proper rational functions.

**Example 6.4.1** Dividing $f(x) = x^4+4x^3+2x^2+4x+1$ by $g(x) = x^2+x+1$ gives the quotient $q(x) = x^2+3x-2$ and remainder $r(x) = 3x+3$, so $\frac{f}{g} = x^2+3x-2+\frac{3x+3}{x^2+x+1}$. Likewise, $\frac{2x^4+1}{x^2+1} = 2x^2-2+\frac{3}{x^2+1}$.

**Definition 6.4.2** The following four types of proper rational functions are called **partial fractions** ($a\ne0$, $k\ge2$ an integer, $q^2-4pr<0$):

$$
\text{(1)}\ \frac{A}{ax+b};\qquad\text{(2)}\ \frac{A}{(ax+b)^k};\qquad\text{(3)}\ \frac{Bx+D}{px^2+qx+r};\qquad\text{(4)}\ \frac{Bx+D}{(px^2+qx+r)^k}.
$$

The condition $q^2-4pr<0$ means that $px^2+qx+r$ has no real roots, that is, it is an **irreducible polynomial** over the real numbers. By the fundamental theorem of algebra, a real polynomial factors over the reals into a product of linear factors and irreducible quadratic factors ([2.1.9](/2.1.9)), and from this one can prove:

**Theorem 6.4.1 (Partial Fraction Decomposition)** A proper rational function $\frac{P_m(x)}{Q_n(x)}$ can be written uniquely as a sum of partial fractions. Factor $Q_n$ into powers of linear factors and irreducible quadratic factors; the decomposition then follows these rules:

1. Each simple linear factor $ax+b$ of $Q_n$ contributes one term $\frac{A}{ax+b}$;
2. A linear factor of multiplicity $k$, $(ax+b)^k$, contributes $k$ terms $\frac{A_1}{ax+b}+\frac{A_2}{(ax+b)^2}+\cdots+\frac{A_k}{(ax+b)^k}$;
3. Each simple quadratic factor $px^2+qx+r$ contributes one term $\frac{Bx+D}{px^2+qx+r}$;
4. A quadratic factor of multiplicity $k$, $(px^2+qx+r)^k$, contributes $k$ terms $\frac{B_1x+D_1}{px^2+qx+r}+\cdots+\frac{B_kx+D_k}{(px^2+qx+r)^k}$.

The number of undetermined coefficients is exactly $n$. To find them, one can clear denominators and compare the coefficients of the numerators (the method of undetermined coefficients), or substitute suitable values of $x$ (for instance, the roots of $Q_n$).

**Example 6.4.2** Decompose the following proper rational functions into partial fractions: (1) $\frac{x-2}{x^3-2x^2+x}$; (2) $\frac{3x^2+2}{x^2(x^2+1)}$.

Solution. (1) $x^3-2x^2+x = x(x-1)^2$. Write $\frac{x-2}{x(x-1)^2} = \frac Ax+\frac{B}{x-1}+\frac{C}{(x-1)^2}$; clearing denominators gives $x-2 = A(x-1)^2+Bx(x-1)+Cx$. Setting $x = 0$ gives $A = -2$; setting $x = 1$ gives $C = -1$; comparing the coefficients of $x^2$ gives $A+B = 0$, so $B = 2$. Therefore

$$
\frac{x-2}{x^3-2x^2+x} = -\frac2x+\frac2{x-1}-\frac1{(x-1)^2}.
$$

(2) Write $\frac{3x^2+2}{x^2(x^2+1)} = \frac Ax+\frac B{x^2}+\frac{Cx+D}{x^2+1}$. Comparing coefficients gives $A = 0$, $B = 2$, $C = 0$, $D = 1$, that is, $\frac{3x^2+2}{x^2(x^2+1)} = \frac2{x^2}+\frac1{x^2+1}$.

All four types of partial fractions can be integrated:

$$
\begin{aligned}
&\text{(1)}\ \int\frac{A}{ax+b}\,\mathrm{d}x = \frac Aa\ln\lvert ax+b\rvert+C;\qquad\text{(2)}\ \int\frac{A}{(ax+b)^k}\,\mathrm{d}x = -\frac{A}{a(k-1)}(ax+b)^{-k+1}+C;\\
&\text{(3)}\ \int\frac{Bx+D}{px^2+qx+r}\,\mathrm{d}x = \frac B{2p}\int\frac{2px+q}{px^2+qx+r}\,\mathrm{d}x+\frac{2pD-Bq}{2p}\int\frac{\mathrm{d}x}{px^2+qx+r}\\
&\qquad = \frac{B}{2p}\ln\lvert px^2+qx+r\rvert+\frac{2pD-Bq}{p\sqrt{4pr-q^2}}\arctan\frac{2px+q}{\sqrt{4pr-q^2}}+C.
\end{aligned}
$$

For (3), split the numerator into a multiple of the derivative of the denominator plus a constant; the first part is handled by $\int\frac{\mathrm{d}u}{u}$, and the second, after completing the square, by $\int\frac{\mathrm{d}x}{(x+\alpha)^2+\beta^2} = \frac1\beta\arctan\frac{x+\alpha}\beta+C$. Type (4) is split in the same way:

$$
\int\frac{Bx+D}{(px^2+qx+r)^k}\,\mathrm{d}x = -\frac{B}{2p(k-1)}(px^2+qx+r)^{-k+1}+\frac{2pD-Bq}{2p^{k+1}}\int\frac{\mathrm{d}x}{\bigl[\bigl(x+\frac q{2p}\bigr)^2+\frac{4pr-q^2}{4p^2}\bigr]^k},
$$

and after the substitution $u = x+\frac{q}{2p}$ the last integral is the $I_k$ of Example 6.3.3, which is computed with the reduction formula.

**Algorithm 6.4.1 (Integration of Rational Functions)**

1. If $\frac{P_m}{Q_n}$ is an improper rational function, use division with remainder to write it as a polynomial plus a proper rational function;
2. Factor the denominator $Q_n$ into powers of linear factors and irreducible quadratic factors;
3. Write down the partial fraction decomposition according to Theorem 6.4.1 and find the coefficients by the method of undetermined coefficients;
4. Integrate the polynomial and each partial fraction separately (formulas (1)–(4) and the reduction formula of Example 6.3.3), and add the results.

This yields an important conclusion: the antiderivative of a rational function is always an elementary function, built from rational functions, logarithms and arctangents. The difficulty lies in step 2: the factorization of a polynomial of high degree generally cannot be found exactly. In practice, one should first look for a way, such as a substitution, to avoid the partial fraction decomposition altogether.

**Example 6.4.3** Evaluate the following integrals.

(1) $\int\frac{x+5}{(x+1)^2}\,\mathrm{d}x = \int\Bigl(\frac{1}{x+1}+\frac{4}{(x+1)^2}\Bigr)\mathrm{d}x = \ln\lvert x+1\rvert-\frac{4}{x+1}+C$.

(2) $\int\frac{x+1}{x^2-4x+3}\,\mathrm{d}x = \int\Bigl(\frac2{x-3}-\frac1{x-1}\Bigr)\mathrm{d}x = 2\ln\lvert x-3\rvert-\ln\lvert x-1\rvert+C$.

(3) There is no need to decompose over $x(x^{10}+1)^2$. Let $u = x^{10}$, so that $\frac{\mathrm{d}x}x = \frac{\mathrm{d}u}{10u}$:

$$
\int\frac{\mathrm{d}x}{x(x^{10}+1)^2} = \frac1{10}\int\frac{\mathrm{d}u}{u(u+1)^2} = \frac1{10}\int\Bigl(\frac1u-\frac1{u+1}-\frac1{(u+1)^2}\Bigr)\mathrm{d}u = \frac1{10}\Bigl(\ln\frac{x^{10}}{x^{10}+1}+\frac1{x^{10}+1}\Bigr)+C.
$$

(4) $\int\frac{x\,\mathrm{d}x}{x^2+4x+5} = \frac12\int\frac{(2x+4)\,\mathrm{d}x}{x^2+4x+5}-2\int\frac{\mathrm{d}x}{(x+2)^2+1} = \frac12\ln(x^2+4x+5)-2\arctan(x+2)+C$.

(5) $\int\frac{2x+5}{x^2+2x+3}\,\mathrm{d}x = \int\frac{(2x+2)\,\mathrm{d}x}{x^2+2x+3}+3\int\frac{\mathrm{d}x}{(x+1)^2+2} = \ln(x^2+2x+3)+\frac3{\sqrt2}\arctan\frac{x+1}{\sqrt2}+C$.

### 6.4.2. Rational Functions of Sine and Cosine

An expression obtained from $\sin x$, $\cos x$ and constants by finitely many arithmetic operations is called a rational function of sine and cosine and is written $R(\sin x,\cos x)$, where $R(u,v)$ is a rational function of $u$ and $v$. One should first see whether trigonometric identities simplify it.

**Example 6.4.4** Evaluate: (1) $\int\sin mx\sin nx\,\mathrm{d}x$; (2) $\int\frac{\mathrm{d}x}{1+\sin x+\cos x}$; (3) $\int\frac{\mathrm{d}x}{a\cos x+b\sin x}$ ($a^2+b^2\ne0$).

Solution. (1) Use the product-to-sum formula. For $m\ne\pm n$,

$$
\int\sin mx\sin nx\,\mathrm{d}x = \frac12\int\bigl[\cos(m-n)x-\cos(m+n)x\bigr]\mathrm{d}x = \frac{\sin(m-n)x}{2(m-n)}-\frac{\sin(m+n)x}{2(m+n)}+C.
$$

(Over $[-\pi,\pi]$ this integral vanishes; this is the source of the orthogonality of the trigonometric system in [2.2.9](/2.2.9).)

(2) Use the half-angle formulas:

$$
\int\frac{\mathrm{d}x}{2\sin\frac x2\cos\frac x2+2\cos^2\frac x2} = \int\frac{\frac12\sec^2\frac x2\,\mathrm{d}x}{\tan\frac x2+1} = \int\frac{\mathrm{d}\bigl(\tan\frac x2+1\bigr)}{\tan\frac x2+1} = \ln\Bigl\lvert1+\tan\frac x2\Bigr\rvert+C.
$$

(3) Introduce an auxiliary angle: $a\cos x+b\sin x = \sqrt{a^2+b^2}\sin(x+\varphi)$, where $\sin\varphi = \frac{a}{\sqrt{a^2+b^2}}$ and $\cos\varphi = \frac{b}{\sqrt{a^2+b^2}}$. By the formula following Example 6.2.1 (6),

$$
\int\frac{\mathrm{d}x}{a\cos x+b\sin x} = \frac1{\sqrt{a^2+b^2}}\int\csc(x+\varphi)\,\mathrm{d}x = \frac{1}{\sqrt{a^2+b^2}}\ln\bigl\lvert\csc(x+\varphi)-\cot(x+\varphi)\bigr\rvert+C.
$$

When no shortcut is available, the substitution $t = \tan\frac x2$ always turns a rational function of sine and cosine into a rational function; this is the *Weierstrass substitution* (also called the tangent half-angle substitution). On $(-\pi,\pi)$ we have $x = 2\arctan t$, and

$$
\sin x = \frac{2t}{1+t^2},\qquad\cos x = \frac{1-t^2}{1+t^2},\qquad\mathrm{d}x = \frac{2\,\mathrm{d}t}{1+t^2},
$$

so that

$$
\int R(\sin x,\cos x)\,\mathrm{d}x = \int R\Bigl(\frac{2t}{1+t^2},\frac{1-t^2}{1+t^2}\Bigr)\frac{2}{1+t^2}\,\mathrm{d}t.
$$

The right-hand side is the integral of a rational function, which Algorithm 6.4.1 can handle. The Weierstrass substitution always works, but the resulting rational function often has high degree, so it should be a last resort.

**Example 6.4.5** Evaluate $\int\frac{\mathrm{d}x}{3+5\cos x}$.

Solution. Let $t = \tan\frac x2$. Then

$$
\int\frac{\mathrm{d}x}{3+5\cos x} = \int\frac{1}{3+5\frac{1-t^2}{1+t^2}}\cdot\frac{2\,\mathrm{d}t}{1+t^2} = \int\frac{\mathrm{d}t}{4-t^2} = \frac14\ln\Bigl\lvert\frac{2+t}{2-t}\Bigr\rvert+C = \frac14\ln\Bigl\lvert\frac{2+\tan\frac x2}{2-\tan\frac x2}\Bigr\rvert+C.
$$

This result holds on every interval containing neither the points $(2k+1)\pi$ nor the zeros of $3+5\cos x$. In general, an antiderivative of a **periodic function** is the sum of a periodic function and a linear function (for example, $\int(1+\cos x)\,\mathrm{d}x = x+\sin x$), so an antiderivative expressed through $\tan\frac x2$ must be pieced together at the points $x = (2k+1)\pi$ to obtain an antiderivative that is continuous on the whole real line.

## 6.5. Integration of Irrational Functions

Below, $R(u,v)$ denotes a rational function of $u$ and $v$. For the following three classes of irrational functions, a suitable substitution removes the radical and reduces the problem to the integral of a rational function or of a rational function of sine and cosine (the second substitution rule).

I. $\int R\bigl(x,\sqrt[n]{ax+b}\bigr)\,\mathrm{d}x$ ($a\ne0$): let $ax+b = t^n$ (with $t\ge0$ if $n$ is even). Then

$$
x = \frac{t^n-b}{a},\qquad\mathrm{d}x = \frac{nt^{n-1}}{a}\,\mathrm{d}t,\qquad\int R\bigl(x,\sqrt[n]{ax+b}\bigr)\,\mathrm{d}x = \int R\Bigl(\frac{t^n-b}a,t\Bigr)\frac{nt^{n-1}}{a}\,\mathrm{d}t.
$$

If the integrand contains both $\sqrt[m]{ax+b}$ and $\sqrt[n]{ax+b}$, take the least common multiple of $m$ and $n$ as the index of the root.

II. $\int R\Bigl(x,\sqrt[n]{\frac{ax+b}{cx+d}}\Bigr)\,\mathrm{d}x$ ($ad-bc\ne0$): let $\frac{ax+b}{cx+d} = t^n$ (with $t\ge0$ if $n$ is even). Then

$$
x = \frac{dt^n-b}{a-ct^n},\qquad\mathrm{d}x = \frac{n(ad-bc)t^{n-1}}{(a-ct^n)^2}\,\mathrm{d}t.
$$

(If $ad-bc = 0$, then $\frac{ax+b}{cx+d}$ is constant and the root can simply be taken outside.)

III. $\int R\bigl(x,\sqrt{ax^2+bx+c}\bigr)\,\mathrm{d}x$ ($a\ne0$): complete the square, $ax^2+bx+c = a\bigl(x+\frac b{2a}\bigr)^2+\frac{4ac-b^2}{4a}$; after taking out a constant factor, the integral falls into one of the following three cases, and a trigonometric substitution turns it into a rational function of sine and cosine:

1. $\int R\bigl(x,\sqrt{(x+p)^2-q^2}\bigr)\,\mathrm{d}x$: let $x+p = q\sec t$;
2. $\int R\bigl(x,\sqrt{(x+p)^2+q^2}\bigr)\,\mathrm{d}x$: let $x+p = q\tan t$;
3. $\int R\bigl(x,\sqrt{q^2-(x+p)^2}\bigr)\,\mathrm{d}x$: let $x+p = q\sin t$.

**Example 6.5.1** Evaluate $\int\frac{\mathrm{d}x}{\sqrt x+\sqrt[3]x}$.

Solution. The least common multiple of $2$ and $3$ is $6$. Let $x = t^6$ ($t>0$), $\mathrm{d}x = 6t^5\,\mathrm{d}t$:

$$
\int\frac{6t^5\,\mathrm{d}t}{t^3+t^2} = 6\int\frac{t^3}{t+1}\,\mathrm{d}t = 6\int\Bigl(t^2-t+1-\frac1{t+1}\Bigr)\mathrm{d}t = 2\sqrt x-3\sqrt[3]x+6\sqrt[6]x-6\ln\bigl(1+\sqrt[6]x\bigr)+C.
$$

**Example 6.5.2** Evaluate $\int\frac1x\sqrt{\frac{1+x}{x}}\,\mathrm{d}x$ ($x>0$).

Solution. Let $t = \sqrt{\frac{1+x}{x}}$ ($t>1$), so $x = \frac{1}{t^2-1}$ and $\mathrm{d}x = -\frac{2t\,\mathrm{d}t}{(t^2-1)^2}$:

$$
\int(t^2-1)\,t\cdot\frac{-2t}{(t^2-1)^2}\,\mathrm{d}t = -2\int\frac{t^2}{t^2-1}\,\mathrm{d}t = -2\int\Bigl(1+\frac{1}{t^2-1}\Bigr)\mathrm{d}t = -2t-\ln\frac{t-1}{t+1}+C,
$$

where $t = \sqrt{\frac{1+x}x}$.

**Example 6.5.3** Evaluate $\int\sqrt{3+2x-x^2}\,\mathrm{d}x$.

Solution. Since $3+2x-x^2 = 4-(x-1)^2$, this is case 3. Let $x-1 = 2\sin t$, $t\in\bigl[-\frac\pi2,\frac\pi2\bigr]$; exactly as in Example 6.2.3 (2) we obtain

$$
\int\sqrt{4-(x-1)^2}\,\mathrm{d}x = \frac{x-1}{2}\sqrt{3+2x-x^2}+2\arcsin\frac{x-1}{2}+C.
$$

## Summary

Each method of indefinite integration is a differentiation rule read backwards:

| Method | Formula | Corresponding differentiation rule | When to use |
|---|---|---|---|
| Linearity | $\int(kf+lg) = k\int f+l\int g$ | Linearity of differentiation | Splitting into basic integrals |
| First substitution | $\int f(\varphi(x))\varphi'(x)\,\mathrm{d}x = \int f(u)\,\mathrm{d}u$ | Chain rule | Recognizing $\mathrm{d}\varphi(x)$ in the integrand |
| Second substitution | $\int f(x)\,\mathrm{d}x = \int f(\varphi(t))\varphi'(t)\,\mathrm{d}t$ | Chain rule, derivative of the inverse | Removing radicals: trigonometric, root and reciprocal substitutions |
| Integration by parts | $\int u\,\mathrm{d}v = uv-\int v\,\mathrm{d}u$ | Product rule | Polynomials times exponentials or trigonometric functions; inverse trigonometric functions and logarithms; recurring integrals and reduction formulas |
| Rational functions | Division with remainder + partial fractions | — | Always integrable (when the denominator can be factored) |
| Rational functions of $\sin x$, $\cos x$ | $t = \tan\frac x2$ | — | Reduces to a rational function |
| Irrational functions | $t = \sqrt[n]{ax+b}$, $t = \sqrt[n]{\frac{ax+b}{cx+d}}$, trigonometric substitution | — | Reduces to a rational function or a rational function of sine and cosine |

In addition to the basic integrals of Section 6.1.3, the following results are frequently used ($a>0$):

| Integral | Result |
|---|---|
| $\int\tan x\,\mathrm{d}x$, $\int\cot x\,\mathrm{d}x$ | $-\ln\lvert\cos x\rvert+C$, $\ln\lvert\sin x\rvert+C$ |
| $\int\sec x\,\mathrm{d}x$, $\int\csc x\,\mathrm{d}x$ | $\ln\lvert\sec x+\tan x\rvert+C$, $\ln\lvert\csc x-\cot x\rvert+C$ |
| $\int\frac{\mathrm{d}x}{a^2+x^2}$ | $\frac1a\arctan\frac xa+C$ |
| $\int\frac{\mathrm{d}x}{a^2-x^2}$ | $\frac1{2a}\ln\bigl\lvert\frac{a+x}{a-x}\bigr\rvert+C$ |
| $\int\frac{\mathrm{d}x}{\sqrt{a^2-x^2}}$ | $\arcsin\frac xa+C$ |
| $\int\frac{\mathrm{d}x}{\sqrt{x^2\pm a^2}}$ | $\ln\bigl\lvert x+\sqrt{x^2\pm a^2}\bigr\rvert+C$ |
| $\int\sqrt{a^2-x^2}\,\mathrm{d}x$ | $\frac12\bigl(x\sqrt{a^2-x^2}+a^2\arcsin\frac xa\bigr)+C$ |
| $\int\sqrt{x^2\pm a^2}\,\mathrm{d}x$ | $\frac12\bigl(x\sqrt{x^2\pm a^2}\pm a^2\ln\lvert x+\sqrt{x^2\pm a^2}\rvert\bigr)+C$ |
| $\int\mathrm{e}^{ax}\cos bx\,\mathrm{d}x$ | $\frac{\mathrm{e}^{ax}(a\cos bx+b\sin bx)}{a^2+b^2}+C$ |
| $\int\mathrm{e}^{ax}\sin bx\,\mathrm{d}x$ | $\frac{\mathrm{e}^{ax}(a\sin bx-b\cos bx)}{a^2+b^2}+C$ |
| $\int\cos^nx\,\mathrm{d}x$ | $I_n = \frac1n\cos^{n-1}x\sin x+\frac{n-1}nI_{n-2}$ |
| $\int\frac{\mathrm{d}x}{(x^2+a^2)^{k}}$ | $I_{k+1} = \frac{2k-1}{2ka^2}I_k+\frac{x}{2ka^2(x^2+a^2)^k}$ |
