---
title: Derivatives and Differentials
source_hash: e3e5fdb5b68b
---

With this chapter we enter differential calculus. The derivative describes the rate of change of a function at a point: geometrically it is the slope of the tangent line to a curve, physically it is instantaneous velocity. The differential describes the linear principal part of the increment of a function, that is, "replacing the curve locally by a straight line." The chapter first defines the derivative through the **limit of a function** and discusses one-sided derivatives and the relation between differentiability and **continuous functions**. It then establishes the arithmetic rules, the chain rule and the rule for inverse functions, and computes the derivatives of all **basic elementary functions**, so that every **elementary function** can be differentiated mechanically. Next come logarithmic differentiation, derivatives of functions given parametrically or implicitly, higher-order derivatives and the Leibniz rule, and finally the differential and its invariance of form. The next chapter ([2.2.5](/2.2.5)) uses derivatives to study monotonicity, extrema, convexity and Taylor expansions; [2.2.6](/2.2.6) goes in the opposite direction and recovers functions from their derivatives; partial derivatives and total differentials of functions of several variables are treated in [2.2.10](/2.2.10).

## 4.1. The Concept of the Derivative

### 4.1.1. Derivatives

Motivating example 1 (instantaneous velocity): a particle moves along the $x$-axis, and its position at time $t$ is $x(t)$. Its displacement from $t_0$ to $t_0 + \Delta t$ is $x(t_0+\Delta t) - x(t_0)$, and its average velocity is $\frac{x(t_0+\Delta t)-x(t_0)}{\Delta t}$. The smaller $\Delta t$ is, the closer the average velocity is to the instantaneous velocity at time $t_0$; if the limit

$$
\lim_{\Delta t\to 0}\frac{x(t_0+\Delta t)-x(t_0)}{\Delta t}
$$

exists, it is the instantaneous velocity of the particle at time $t_0$.

Motivating example 2 (tangent lines): let the curve $L$ be the graph of $y = f(x)$ and let $M(x_0, y_0)$ be a point on $L$. Take a point $Q(x_0+\Delta x, y_0+\Delta y)$ on $L$ near $M$; the secant line $MQ$ has slope $\frac{\Delta y}{\Delta x}$. As $\Delta x \to 0$, the point $Q$ moves along the curve toward $M$; if the secant line $MQ$ approaches a limiting position $MT$, the line $MT$ is called the tangent line to $L$ at $M$, and its slope is

$$
\lim_{\Delta x\to 0}\frac{\Delta y}{\Delta x} = \lim_{\Delta x\to 0}\frac{f(x_0+\Delta x)-f(x_0)}{\Delta x}.
$$

![As Δx decreases, the slope of the secant line MQ tends to the slope f′(x₀) of the tangent line.](./plots/secant-to-tangent.py)

Both examples lead to the same kind of limit: the limit of the ratio of the increment of the function to the increment of the independent variable, as the latter tends to zero. Throughout, the function is assumed to be defined on some **neighborhood** of $x_0$.

**Definition 4.1.1 (Derivative)** Let $y = f(x)$ be defined at and near $x_0$. If the limit

$$
\lim_{\Delta x\to 0}\frac{\Delta y}{\Delta x}=\lim_{\Delta x\to 0}\frac{f(x_0+\Delta x)-f(x_0)}{\Delta x}
$$
exists, then $f$ is said to be **differentiable** at the point $x_0$, and the limit is called the **derivative** of $f$ at $x_0$, denoted $f'(x_0)$, $\frac{\mathrm{d}f}{\mathrm{d}x}\big|_{x=x_0}$ or $\frac{\mathrm{d}f(x_0)}{\mathrm{d}x}$; otherwise $f$ is said to be not differentiable at $x_0$.

Setting $x = x_0 + \Delta x$ gives an equivalent form of the derivative:

$$
f'(x_0) = \lim_{x\to x_0}\frac{f(x)-f(x_0)}{x-x_0}.
$$

If $f$ is differentiable at every point of an interval $I$ (at endpoints, one-sided derivatives are meant; see below), then $f$ is said to be differentiable on $I$, and $x \mapsto f'(x)$ is a function on $I$, called the derivative (or derived function) of $f$. If moreover $f'$ is continuous on $I$, then $f$ is said to be continuously differentiable on $I$, written $f \in C^1(I)$.

If the limit above is $+\infty$ or $-\infty$ (or $\infty$), then $f$ is not differentiable at $x_0$, but for convenience we still write $f'(x_0) = \infty$; in this case the tangent line is vertical.

Geometric meaning of the derivative: if $f$ is differentiable at $x_0$, then $f'(x_0)$ is the slope of the tangent line to the curve $y = f(x)$ at $M(x_0, y_0)$.

**Definition 4.1.2** Let the curve $L\colon y=f(x)$ pass through the point $M(x_0,y_0)$. If $f'(x_0)$ exists, the line $y - y_0 = f'(x_0)(x - x_0)$ is called the **tangent line** to $L$ at $M$; if $f'(x_0) = \infty$, the tangent line is $x = x_0$. The line through $M$ perpendicular to the tangent line is called the **normal line** to $L$ at $M$:

$$
y - y_0 = -\frac{1}{f'(x_0)}(x - x_0)\ \ (f'(x_0)\ne 0),\qquad y = y_0\ \ (f'(x_0)=\infty),\qquad x = x_0\ \ (f'(x_0)=0).
$$

**Example 4.1.1** Let $f'(x_0) = A$. Find (1) $\lim\limits_{h\to 0}\frac{f(x_0+3h)-f(x_0)}{h}$; (2) $\lim\limits_{h\to 0}\frac{f(x_0+2h)-f(x_0-h)}{h}$.

**Solution** The key is to rewrite the numerator as a difference quotient with "matching increments." (1) $\lim\limits_{h\to0} 3\cdot\frac{f(x_0+3h)-f(x_0)}{3h} = 3A$. (2) Subtract and add $f(x_0)$ in the numerator:

$$
\lim_{h\to0}\frac{f(x_0+2h)-f(x_0)}{h} - \lim_{h\to0}\frac{f(x_0-h)-f(x_0)}{h} = 2\lim_{h\to0}\frac{f(x_0+2h)-f(x_0)}{2h} + \lim_{h\to0}\frac{f(x_0-h)-f(x_0)}{-h} = 2A + A = 3A.
$$

Note that (2) uses the existence of $f'(x_0)$; the mere existence of the limit of the symmetric difference quotient $\frac{f(x_0+h)-f(x_0-h)}{2h}$ does not imply differentiability (consider $|x|$ at $0$).

**Example 4.1.2** Let $f(x) = \frac{1-\cos x}{x}$ ($x \ne 0$) and $f(0) = 0$. Find $f'(0)$.

**Solution** $f'(0) = \lim\limits_{x\to0}\frac{f(x)-f(0)}{x-0} = \lim\limits_{x\to0}\frac{1-\cos x}{x^2} = \frac12$ (by the **equivalent infinitesimals** $1-\cos x \sim \frac{x^2}{2}$).

**Definition 4.1.3 (One-Sided Derivatives)** Let $f$ be defined at $x_0$ and on some interval to its left (right). If the limit

$$
f'_-(x_0) = \lim_{\Delta x\to 0^-}\frac{f(x_0+\Delta x)-f(x_0)}{\Delta x}\qquad\Bigl(f'_+(x_0) = \lim_{\Delta x\to 0^+}\frac{f(x_0+\Delta x)-f(x_0)}{\Delta x}\Bigr)
$$
exists, it is called the **left derivative** (**right derivative**) of $f$ at $x_0$.

The relation between **one-sided limits** and limits immediately gives:

**Theorem 4.1.1** $f$ is differentiable at $x_0$ $\iff$ the left and right derivatives of $f$ at $x_0$ both exist and are equal.

**Example 4.1.3** For $y = |x|$ at $0$: $\lim\limits_{x\to0^-}\frac{|x|}{x} = -1$ and $\lim\limits_{x\to0^+}\frac{|x|}{x} = 1$; the left and right derivatives exist but differ, so $|x|$ is not differentiable at $0$. The graph has a "corner" at $0$, called a corner point. For $y=\sqrt{|x|}$, the left and right derivatives at $0$ are $-\infty$ and $+\infty$, respectively, and the graph forms a cusp there.

**Theorem 4.1.2 (Differentiability Implies Continuity)** If $f$ is differentiable at $x_0$, then $f$ is continuous at $x_0$.

**Proof** From $\lim\limits_{\Delta x\to0}\frac{\Delta y}{\Delta x} = f'(x_0)$ we get $\lim\limits_{\Delta x\to0}\frac{\Delta y - f'(x_0)\Delta x}{\Delta x} = 0$, that is,

$$
\Delta y = f'(x_0)\Delta x + o(\Delta x)\qquad(\Delta x\to0). \tag{4.1}
$$

Hence $\Delta y \to 0$ as $\Delta x \to 0$, and $f$ is continuous at $x_0$. $\square$

The converse fails: $|x|$ is continuous but not differentiable at $0$ (Example 4.1.3). There even exist functions that are continuous everywhere and differentiable nowhere (Weierstrass's construction $\sum_n a^n\cos(b^n\pi x)$), so continuity is far weaker than differentiability. In Section 4.5, Eq. (4.1) will become the definition of the differential.

### 4.1.2. Examples of Differentiation

**Example 4.1.4 (Derivatives of Some Basic Elementary Functions)** Prove: (1) $c' = 0$ ($c$ a constant); (2) $(\sin x)' = \cos x$; (3) $(\cos x)' = -\sin x$; (4) $(a^x)' = a^x\ln a$, in particular $(\mathrm{e}^x)' = \mathrm{e}^x$; (5) $(\log_a x)' = \frac{1}{x\ln a}$, in particular $(\ln x)' = \frac1x$.

**Proof** (1) is obvious. (2) By the sum-to-product formula,

$$
(\sin x)' = \lim_{\Delta x\to0}\frac{2\cos\bigl(x+\frac{\Delta x}{2}\bigr)\sin\frac{\Delta x}{2}}{\Delta x} = \lim_{\Delta x\to0}\cos\Bigl(x+\frac{\Delta x}{2}\Bigr)\cdot\frac{\sin(\Delta x/2)}{\Delta x/2} = \cos x,
$$

where we used the continuity of $\cos$ and $\lim\limits_{t\to0}\frac{\sin t}{t} = 1$. (3) is similar. (4) Since $a^{\Delta x} - 1 \sim \Delta x\ln a$,

$$
(a^x)' = \lim_{\Delta x\to0}\frac{a^x(a^{\Delta x}-1)}{\Delta x} = a^x\ln a.
$$

(5) Since $\ln(1+u)\sim u$,

$$
(\log_a x)' = \lim_{\Delta x\to0}\frac{\log_a\bigl(1+\frac{\Delta x}{x}\bigr)}{\Delta x} = \lim_{\Delta x\to0}\frac{\ln\bigl(1+\frac{\Delta x}{x}\bigr)}{\Delta x\,\ln a} = \frac{1}{x\ln a}. \qquad\square
$$

**Example 4.1.5** Find the equations of the tangent lines to the curve $y = \sqrt[3]{x}$ at the points corresponding to $x = 1$ and $x = 0$.

**Solution** At $x = 1$, $y'(1) = \lim\limits_{\Delta x\to0}\frac{(1+\Delta x)^{1/3}-1}{\Delta x} = \frac13$ (since $(1+u)^{1/3}-1\sim\frac u3$), and the tangent line is $y - 1 = \frac13(x-1)$. At $x = 0$, $\lim\limits_{\Delta x\to0}\frac{(\Delta x)^{1/3}}{\Delta x} = +\infty$; thus $\sqrt[3]{x}$ is not differentiable at $0$, but the tangent line exists: it is the vertical line $x = 0$.

**Example 4.1.6** Let $f(x) = x^2\sin\frac1x$ ($x\ne0$) and $f(0)=0$. Then $f'(0) = \lim\limits_{x\to0}x\sin\frac1x = 0$, and for $x\ne0$, $f'(x) = 2x\sin\frac1x - \cos\frac1x$, which has no limit as $x\to0$. Thus $f$ is differentiable everywhere on $\mathbb{R}$, but its derivative is discontinuous at $0$ (a **discontinuity of the second kind**): the derivative of a differentiable function need not be continuous, and $C^1$ is a stronger condition than differentiability.

![Left: x² sin(1/x) lies between ±x², and its tangent line at 0 is y = 0. Right: its derivative oscillates infinitely often between −1 and 1 near 0 and has no limit at 0.](./plots/x2-sin-inverse-x.py)

## 4.2. Rules of Differentiation

### 4.2.1. Arithmetic Rules for Derivatives

**Theorem 4.2.1** Let $f$ and $g$ be differentiable at the point $x$. Then

1. $(cf)' = cf'$ ($c$ a constant) and $(f+g)' = f'+g'$;
2. $(fg)' = f'g + fg'$, and more generally $(f_1f_2\cdots f_n)' = f_1'f_2\cdots f_n + f_1f_2'\cdots f_n + \cdots + f_1f_2\cdots f_n'$;
3. If $g(x)\ne0$, then $\bigl(\frac1g\bigr)' = -\frac{g'}{g^2}$ and $\bigl(\frac fg\bigr)' = \frac{f'g-fg'}{g^2}$.

**Proof** 2. Subtract and add $f(x)g(x+\Delta x)$ in the numerator:

$$
(fg)' = \lim_{\Delta x\to0}\Bigl[\frac{f(x+\Delta x)-f(x)}{\Delta x}\,g(x+\Delta x) + f(x)\,\frac{g(x+\Delta x)-g(x)}{\Delta x}\Bigr] = f'g+fg',
$$

where $g(x+\Delta x)\to g(x)$ because differentiability implies continuity (Theorem 4.1.2).

3. For the reciprocal,
$$
\Bigl(\frac1g\Bigr)' = \lim_{\Delta x\to0}\frac{1}{\Delta x}\Bigl(\frac{1}{g(x+\Delta x)}-\frac1{g(x)}\Bigr) = \lim_{\Delta x\to0}\Bigl(-\frac{g(x+\Delta x)-g(x)}{\Delta x}\Bigr)\frac{1}{g(x+\Delta x)g(x)} = -\frac{g'}{g^2}.
$$

Then 2 gives $\bigl(\frac fg\bigr)' = f'\cdot\frac1g + f\cdot\bigl(-\frac{g'}{g^2}\bigr) = \frac{f'g-fg'}{g^2}$. $\square$

Part 1 says that differentiation is a linear operation: the differentiable functions form a **vector space**, and differentiation is a **linear map** on it.

**Example 4.2.1** By the quotient rule,

$$
(\tan x)' = \frac{\cos^2x+\sin^2x}{\cos^2x} = \sec^2x,\quad (\cot x)' = -\csc^2x,\quad (\sec x)' = \frac{\sin x}{\cos^2x} = \sec x\tan x,\quad (\csc x)' = -\csc x\cot x.
$$

### 4.2.2. Differentiation of Composite Functions

**Theorem 4.2.2 (Chain Rule)** Let $u = u(x)$ be differentiable at $x_0$ and $y = y(u)$ differentiable at $u_0 = u(x_0)$. Then the **composite function** $y = y(u(x))$ is differentiable at $x_0$, and

$$
(y\circ u)'(x_0) = y'(u_0)\,u'(x_0),\qquad\text{that is,}\quad \frac{\mathrm{d}y}{\mathrm{d}x}\Big|_{x=x_0} = \frac{\mathrm{d}y}{\mathrm{d}u}\Big|_{u=u_0}\cdot\frac{\mathrm{d}u}{\mathrm{d}x}\Big|_{x=x_0}.
$$

**Proof** Since $y$ is differentiable at $u_0$, the function $\alpha(\Delta u) = \frac{y(u_0+\Delta u)-y(u_0)}{\Delta u} - y'(u_0)$ ($\Delta u\ne0$), $\alpha(0) = 0$, is continuous at $0$, and for every $\Delta u$ (including $\Delta u = 0$)

$$
\Delta y = y(u_0+\Delta u)-y(u_0) = \bigl(y'(u_0)+\alpha(\Delta u)\bigr)\Delta u.
$$

Give $x$ an increment $\Delta x\ne0$ and let $\Delta u = u(x_0+\Delta x)-u(x_0)$. Then $\frac{\Delta y}{\Delta x} = \bigl(y'(u_0)+\alpha(\Delta u)\bigr)\frac{\Delta u}{\Delta x}$. As $\Delta x\to0$, the continuity of $u$ gives $\Delta u\to0$, so $\alpha(\Delta u)\to0$, while $\frac{\Delta u}{\Delta x}\to u'(x_0)$; hence $\frac{\Delta y}{\Delta x}\to y'(u_0)u'(x_0)$. $\square$

(One could instead write $\Delta y = y'(u_0)\Delta u + o(\Delta u)$ and divide by $\Delta x$, but then one must check that $o(\Delta u)/\Delta x \to 0$ still holds when $\Delta u$ may vanish; the function $\alpha$ is introduced precisely to deal with this.)

The chain rule can be remembered as $y\to u\to x$: differentiate layer by layer along the chain of composition and multiply.

**Example 4.2.2** Find the derivatives: (1) $y = x^\alpha$ ($x>0$, $\alpha\in\mathbb{R}$); (2) $y = \cos(5x^2+2x+3)$; (3) $y = \bigl(\frac{x+1}{x-1}\bigr)^{3/2}$; (4) $y = \ln\bigl(x+\sqrt{x^2+a^2}\bigr)$.

**Solution** (1) $y = \mathrm{e}^{\alpha\ln x}$, so $y' = \mathrm{e}^{\alpha\ln x}\cdot\frac{\alpha}{x} = \alpha x^{\alpha-1}$.

(2) Let $u = 5x^2+2x+3$; then $y' = -\sin u\cdot(10x+2) = -(10x+2)\sin(5x^2+2x+3)$.

(3) Let $u = \frac{x+1}{x-1}$; then $y' = \frac32u^{1/2}\cdot\frac{-2}{(x-1)^2} = -\frac{3(x+1)^{1/2}}{(x-1)^{5/2}}$.

(4) We have
$$
y' = \frac{1}{x+\sqrt{x^2+a^2}}\Bigl(1+\frac{x}{\sqrt{x^2+a^2}}\Bigr) = \frac{1}{\sqrt{x^2+a^2}}.
$$

**Example 4.2.3** Prove that $(\ln|x|)' = \frac1x$ ($x\ne0$).

**Proof** For $x>0$ this is $(\ln x)' = \frac1x$. For $x<0$, $(\ln|x|)' = (\ln(-x))' = \frac{-1}{-x} = \frac1x$. $\square$

### 4.2.3. Differentiation of Inverse Functions

**Theorem 4.2.3** Let $y = f(x)$ be strictly monotonic and continuous on $[a,b]$, let $x_0\in(a,b)$, and suppose $f'(x_0)$ exists and is nonzero. Then the **inverse function** $x = f^{-1}(y)$ is differentiable at $y_0 = f(x_0)$, and

$$
(f^{-1})'(y_0) = \frac{1}{f'(x_0)},\qquad\text{that is,}\quad\frac{\mathrm{d}x}{\mathrm{d}y} = 1\Big/\frac{\mathrm{d}y}{\mathrm{d}x}.
$$

**Proof** The inverse of a strictly monotonic continuous function is also strictly monotonic and continuous, so $y\to y_0 \iff x = f^{-1}(y)\to x_0$, and $y\ne y_0\iff x\ne x_0$. Hence

$$
\lim_{y\to y_0}\frac{f^{-1}(y)-f^{-1}(y_0)}{y-y_0} = \lim_{x\to x_0}\frac{x-x_0}{f(x)-f(x_0)} = \frac1{f'(x_0)}. \qquad\square
$$

Geometrically, $y=f(x)$ and $x = f^{-1}(y)$ describe the same curve, and the slopes of the tangent line measured relative to the $x$-axis and to the $y$-axis are reciprocals of each other. If the inverse function is also written with $x$ as the independent variable, $y = f^{-1}(x)$, then $(f^{-1})'(x) = \frac{1}{f'(y)}$ with $y = f^{-1}(x)$.

**Example 4.2.4 (Derivatives of the Inverse Trigonometric Functions)** The functions $y = \arcsin x$ ($-1<x<1$) and $x = \sin y$ ($-\frac\pi2<y<\frac\pi2$) are inverse to each other, and $\cos y>0$, so

$$
(\arcsin x)' = \frac{1}{\cos y} = \frac{1}{\sqrt{1-\sin^2y}} = \frac{1}{\sqrt{1-x^2}}.
$$

Similarly, $(\arccos x)' = -\frac{1}{\sin y} = -\frac{1}{\sqrt{1-x^2}}$ ($0<y<\pi$); since $y=\arctan x$ and $x = \tan y$ are inverse to each other, $(\arctan x)' = \cos^2y = \frac{1}{1+\tan^2y} = \frac1{1+x^2}$; and from $\arctan x+\operatorname{arccot}x = \frac\pi2$ we get $(\operatorname{arccot}x)' = -\frac{1}{1+x^2}$.

**Example 4.2.5** Let $y = \arctan\frac{\sin x}{\mathrm{e}^x-1}$. Find $y'$.

**Solution** Let $u = \frac{\sin x}{\mathrm{e}^x-1}$. Then

$$
y' = \frac{1}{1+u^2}\cdot\frac{\cos x\,(\mathrm{e}^x-1)-\mathrm{e}^x\sin x}{(\mathrm{e}^x-1)^2} = \frac{(\cos x-\sin x)\mathrm{e}^x-\cos x}{(\mathrm{e}^x-1)^2+\sin^2x}.
$$

**Example 4.2.6** Let $y = \arcsin(\arctan x)+\log_a\arccos x$. Then

$$
y' = \frac{1}{\sqrt{1-\arctan^2x}}\cdot\frac1{1+x^2}+\frac{1}{\arccos x\,\ln a}\cdot\Bigl(-\frac{1}{\sqrt{1-x^2}}\Bigr).
$$

We have now found the derivatives of all six classes of basic elementary functions. By the arithmetic rules and the chain rule, every elementary function can be differentiated by formula on the intervals of its domain (except at isolated points), and its derivative is again an elementary function.

| Function | Derivative | Function | Derivative |
|---|---|---|---|
| $c$ | $0$ | $x^\alpha$ ($x>0$, $\alpha\in\mathbb{R}$) | $\alpha x^{\alpha-1}$ |
| $a^x$ ($a>0$) | $a^x\ln a$ | $\mathrm{e}^x$ | $\mathrm{e}^x$ |
| $\log_a x$ | $\frac{1}{x\ln a}$ | $\ln\lvert x\rvert$ | $\frac1x$ |
| $\sin x$ | $\cos x$ | $\cos x$ | $-\sin x$ |
| $\tan x$ | $\sec^2x$ | $\cot x$ | $-\csc^2x$ |
| $\sec x$ | $\sec x\tan x$ | $\csc x$ | $-\csc x\cot x$ |
| $\arcsin x$ | $\frac{1}{\sqrt{1-x^2}}$ | $\arccos x$ | $-\frac{1}{\sqrt{1-x^2}}$ |
| $\arctan x$ | $\frac{1}{1+x^2}$ | $\operatorname{arccot} x$ | $-\frac{1}{1+x^2}$ |
| $\sinh x$ | $\cosh x$ | $\cosh x$ | $\sinh x$ |
| $\ln\bigl(x+\sqrt{x^2+a^2}\bigr)$ | $\frac{1}{\sqrt{x^2+a^2}}$ | $\ln\lvert x+\sqrt{x^2-a^2}\rvert$ | $\frac{1}{\sqrt{x^2-a^2}}$ |

The two functions in the last row appear frequently in indefinite integrals ([2.2.6](/2.2.6)); the derivatives of the **hyperbolic functions** follow directly from $\sinh x = \frac{\mathrm{e}^x-\mathrm{e}^{-x}}2$ and $\cosh x = \frac{\mathrm{e}^x+\mathrm{e}^{-x}}2$.

## 4.3. Special Techniques of Differentiation

### 4.3.1. Logarithmic Differentiation

For functions involving many products, quotients and powers, or for functions of the form $u(x)^{v(x)}$ ($u>0$), it is often simpler to take logarithms first and then differentiate; this is called *logarithmic differentiation*. For $y = u(x)^{v(x)}$,

$$
\ln y = v\ln u\ \Longrightarrow\ \frac{y'}{y} = v'\ln u+v\frac{u'}{u}\ \Longrightarrow\ y' = u^{v}\Bigl(v'\ln u+\frac{vu'}{u}\Bigr).
$$

One may also write $y = \mathrm{e}^{v\ln u}$ directly and apply the chain rule, with the same result.

**Example 4.3.1** Find the derivatives: (1) $y = x^{\sin x}$; (2) $y = (x^2+1)^{\tan x}$; (3) $y = (\arccos x)^{\arctan x}$.

**Solution** (1) $y' = \bigl(\mathrm{e}^{\sin x\ln x}\bigr)' = x^{\sin x}\bigl(\cos x\ln x+\frac{\sin x}{x}\bigr)$.

(2) $y' = (x^2+1)^{\tan x}\Bigl[\sec^2x\,\ln(x^2+1)+\frac{2x\tan x}{x^2+1}\Bigr]$.

(3) We have
$$
y' = (\arccos x)^{\arctan x}\Bigl[\frac{\ln\arccos x}{1+x^2}-\frac{\arctan x}{\arccos x\,\sqrt{1-x^2}}\Bigr].
$$

For a product of several factors $y = f_1f_2\cdots f_n$, we have $\frac{y'}{y} = (\ln|y|)' = \frac{f_1'}{f_1}+\cdots+\frac{f_n'}{f_n}$ (wherever no factor vanishes), which is just another way of writing the product rule.

**Example 4.3.2** Let $y = \frac{\mathrm{e}^{-x+1}}{\sqrt[3]{2x-1}\,(4x^2+1)}$ ($x\ne\frac12$). Find $y'$.

**Solution** $\ln|y| = (-x+1)-\frac13\ln|2x-1|-\ln(4x^2+1)$; differentiating both sides,

$$
\frac{y'}{y} = -1-\frac{2}{3(2x-1)}-\frac{8x}{4x^2+1},\qquad y' = -\frac{\mathrm{e}^{-x+1}}{\sqrt[3]{2x-1}\,(4x^2+1)}\Bigl(1+\frac{2}{3(2x-1)}+\frac{8x}{4x^2+1}\Bigr).
$$

### 4.3.2. Derivatives of Functions Defined by Parametric Equations

Let $y$ be a function of $x$ determined by the parametric equations $x = \varphi(t)$, $y = \psi(t)$. If $\varphi$ and $\psi$ are differentiable and $\varphi'(t)\ne0$ (so that $x=\varphi(t)$ locally has a differentiable inverse $t = \varphi^{-1}(x)$ and $y = \psi(\varphi^{-1}(x))$), then the chain rule and the rule for inverse functions give

$$
\frac{\mathrm{d}y}{\mathrm{d}x} = \frac{\mathrm{d}y}{\mathrm{d}t}\cdot\frac{\mathrm{d}t}{\mathrm{d}x} = \frac{\psi'(t)}{\varphi'(t)}.
$$

Whenever we differentiate parametric equations from now on, we tacitly assume $\frac{\mathrm{d}x}{\mathrm{d}t}\ne0$; at points where $\varphi'(t)=0$ and $\psi'(t)\ne0$, the tangent line is vertical.

**Example 4.3.3** Find the equation of the tangent line at an arbitrary point of the ellipse $x = a\cos\theta$, $y = b\sin\theta$ ($0\le\theta<2\pi$).

**Solution** For $\theta\ne0,\pi$, $\frac{\mathrm{d}y}{\mathrm{d}x} = \frac{b\cos\theta}{-a\sin\theta} = -\frac ba\cot\theta$, and the tangent line is $y - b\sin\theta = -\frac ba\cot\theta\,(x-a\cos\theta)$, which simplifies to $\frac{x\cos\theta}{a}+\frac{y\sin\theta}{b} = 1$. For $\theta = 0,\pi$, $\frac{\mathrm{d}y}{\mathrm{d}x} = \infty$ and the tangent lines are $x = a$ and $x = -a$, respectively, which also agree with this equation.

### 4.3.3. Implicit Differentiation

A function of the form $y = f(x)$ is called explicit. If the relation between $x$ and $y$ is given by an equation $F(x,y) = 0$, then $y = y(x)$ is called the **implicit function** determined by the equation. The existence and differentiability of implicit functions require multivariable differential calculus (the **implicit function theorem**, [2.2.10](/2.2.10)); here we assume that the implicit function exists and is differentiable, and discuss only how to differentiate it: differentiate both sides of the equation with respect to $x$, regarding $y$ as a function of $x$ (applying the chain rule to the terms containing $y$), and then solve for $y'$. This is called *implicit differentiation*.

**Example 4.3.4** Let $y = y(x)$ be determined by the equation $\mathrm{e}^{xy}+\sin(x+y) = 0$. Find $\frac{\mathrm{d}y}{\mathrm{d}x}$.

**Solution** Differentiating both sides with respect to $x$ gives $\mathrm{e}^{xy}(y+xy')+\cos(x+y)(1+y') = 0$, so

$$
y' = -\frac{y\,\mathrm{e}^{xy}+\cos(x+y)}{x\,\mathrm{e}^{xy}+\cos(x+y)}.
$$

**Example 4.3.5** For the curve $L\colon y^3+y^2 = 2x^2$, find the equation of the tangent line to $L$ at the point $(1,1)$.

**Solution** Differentiating both sides with respect to $x$ gives $3y^2y'+2yy' = 4x$, so $y' = \frac{4x}{3y^2+2y}$. At $(1,1)$, $y' = \frac45$, and the tangent line is $y - 1 = \frac45(x-1)$.

## 4.4. Higher-Order Derivatives

**Definition 4.4.1 (Higher-Order Derivatives)** Let $f$ be differentiable on an interval $I$. If the derivative $f'$ is itself differentiable on $I$, then $(f')'$ is called the **second derivative** of $f$, denoted $f''(x)$ or $\frac{\mathrm{d}^2f}{\mathrm{d}x^2}$. Proceeding in the same way, we define the third derivative $f'''$ and the $n$-th derivative $f^{(n)}(x) = \frac{\mathrm{d}^nf}{\mathrm{d}x^n}$, with the convention $f^{(0)} = f$. Derivatives of order two and higher are collectively called **higher-order derivatives**.

Notation: $f\in C^n(I)$ means that $f$ has a continuous $n$-th derivative on $I$, and $f$ is then said to be $n$ times continuously differentiable on $I$; $f\in C^\infty(I)$ means that $f$ has derivatives of all orders, and $f$ is then said to be smooth. In physics, the second derivative of position with respect to time is acceleration.

**Example 4.4.1** Let $f(x) = x^4\cos\frac1x$ ($x\ne0$) and $f(0) = 0$. Find $f''(0)$.

**Solution** $f'(0) = \lim\limits_{x\to0}x^3\cos\frac1x = 0$, and for $x\ne0$, $f'(x) = 4x^3\cos\frac1x+x^2\sin\frac1x$. Hence

$$
f''(0) = \lim_{x\to0}\frac{f'(x)-f'(0)}{x} = \lim_{x\to0}\Bigl(4x^2\cos\frac1x+x\sin\frac1x\Bigr) = 0.
$$

At a breakpoint of a piecewise function, higher-order derivatives must be computed order by order from the definition; one may not differentiate the piecewise expressions and then take limits.

**Example 4.4.2** For $y = \sin x$: $y' = \cos x = \sin\bigl(x+\frac\pi2\bigr)$, $y'' = \sin(x+\pi)$, and so on; by induction,

$$
(\sin x)^{(n)} = \sin\Bigl(x+\frac{n\pi}{2}\Bigr),\qquad (\cos x)^{(n)} = \cos\Bigl(x+\frac{n\pi}{2}\Bigr),\qquad n\in\mathbb{N}.
$$

**Example 4.4.3** For $y = \ln x$: $y' = \frac1x$, $y'' = -\frac1{x^2}$, $y''' = \frac{2}{x^3}$, $y^{(4)} = -\frac{2\cdot3}{x^4}$, and so on;

$$
(\ln x)^{(n)} = (-1)^{n-1}\frac{(n-1)!}{x^n},\qquad \bigl(\ln(ax+b)\bigr)^{(n)} = (-1)^{n-1}\frac{(n-1)!\,a^n}{(ax+b)^n},\qquad \Bigl(\frac1{ax+b}\Bigr)^{(n)} = (-1)^n\frac{n!\,a^n}{(ax+b)^{n+1}}.
$$

The third formula follows from $\frac1{ax+b} = \frac1a\bigl(\ln(ax+b)\bigr)'$.

**Theorem 4.4.1** Let $f$ and $g$ have $n$-th derivatives and let $a, b$ be constants. Then $(af+bg)^{(n)} = af^{(n)}+bg^{(n)}$.

**Theorem 4.4.2 (General Leibniz Rule)** Let $f$ and $g$ have $n$-th derivatives. Then

$$
(fg)^{(n)} = \sum_{k=0}^{n}\binom nk f^{(k)}g^{(n-k)}.
$$

**Proof** By induction on $n$. For $n = 1$ this is the product rule. Suppose it holds for $n = m$; differentiating both sides,

$$
(fg)^{(m+1)} = \sum_{k=0}^m\binom mk\bigl(f^{(k+1)}g^{(m-k)}+f^{(k)}g^{(m-k+1)}\bigr) = \sum_{k=0}^{m+1}\Bigl[\binom m{k-1}+\binom mk\Bigr]f^{(k)}g^{(m+1-k)},
$$

with the convention $\binom m{-1} = \binom m{m+1} = 0$. Since $\binom m{k-1}+\binom mk = \binom{m+1}k$, the formula holds for $n = m+1$. $\square$

The formula has exactly the same form as the binomial theorem $(a+b)^n = \sum\binom nka^kb^{n-k}$. It is most useful when one factor is a polynomial of low degree, since then only the first few terms of the sum are nonzero.

**Example 4.4.4** Let $y = \frac{x^2-2}{x^2-x-2}$. Find $y^{(n)}$.

**Solution** First perform polynomial division and then the **partial fraction decomposition** (see Theorem 6.4.1):

$$
y = 1+\frac{x}{(x-2)(x+1)} = 1+\frac23\cdot\frac{1}{x-2}+\frac13\cdot\frac1{x+1}.
$$

By Example 4.4.3,

$$
y^{(n)} = (-1)^n n!\Bigl[\frac{2}{3(x-2)^{n+1}}+\frac{1}{3(x+1)^{n+1}}\Bigr],\qquad n\ge1.
$$

**Example 4.4.5** Let $y = x^2\sin x$. Find $y^{(20)}$.

**Solution** Since $(x^2)^{(k)} = 0$ for $k\ge3$, the Leibniz rule and Example 4.4.2 give

$$
y^{(20)} = x^2\sin(x+10\pi)+\binom{20}{1}2x\sin\Bigl(x+\frac{19\pi}2\Bigr)+\binom{20}22\sin(x+9\pi) = x^2\sin x-40x\cos x-380\sin x.
$$

**Example 4.4.6** Let $y = \frac{\ln x}{x}$. Find $y^{(n)}$.

**Solution** Apply the Leibniz rule with $f = \ln x$ and $g = \frac1x$:

$$
y^{(n)} = \ln x\cdot\Bigl(\frac1x\Bigr)^{(n)}+\sum_{k=1}^n\binom nk(\ln x)^{(k)}\Bigl(\frac1x\Bigr)^{(n-k)} = \frac{(-1)^nn!}{x^{n+1}}\ln x+\sum_{k=1}^n\binom nk\frac{(-1)^{k-1}(k-1)!}{x^k}\cdot\frac{(-1)^{n-k}(n-k)!}{x^{n-k+1}}.
$$

Since $\binom nk(k-1)!(n-k)! = \frac{n!}{k}$, the last sum equals $\frac{(-1)^{n-1}n!}{x^{n+1}}\sum_{k=1}^n\frac1k$, so

$$
\Bigl(\frac{\ln x}{x}\Bigr)^{(n)} = \frac{(-1)^nn!}{x^{n+1}}\Bigl(\ln x-\sum_{k=1}^n\frac1k\Bigr).
$$

Second derivatives of parametric equations. Let $x = \varphi(t)$ and $y = \psi(t)$ be twice differentiable with $\varphi'\ne0$. The derivative $\frac{\mathrm{d}y}{\mathrm{d}x} = \frac{\psi'(t)}{\varphi'(t)}$ is still a function of $t$, so differentiating it with respect to $x$ requires multiplying by $\frac{\mathrm{d}t}{\mathrm{d}x} = \frac1{\varphi'(t)}$:

$$
\frac{\mathrm{d}^2y}{\mathrm{d}x^2} = \frac{\mathrm{d}}{\mathrm{d}t}\Bigl(\frac{\psi'}{\varphi'}\Bigr)\cdot\frac{1}{\varphi'} = \frac{\varphi'\psi''-\psi'\varphi''}{\varphi'^3}.
$$

**Example 4.4.7** Let $x = a\cos^3t$, $y = a\sin^3t$ (the astroid). Find $\frac{\mathrm{d}y}{\mathrm{d}x}$ and $\frac{\mathrm{d}^2y}{\mathrm{d}x^2}$.

**Solution** $\frac{\mathrm{d}y}{\mathrm{d}x} = \frac{3a\sin^2t\cos t}{-3a\cos^2t\sin t} = -\tan t$, and

$$
\frac{\mathrm{d}^2y}{\mathrm{d}x^2} = \frac{\mathrm{d}(-\tan t)}{\mathrm{d}t}\cdot\frac{\mathrm{d}t}{\mathrm{d}x} = -\sec^2t\cdot\frac{1}{-3a\cos^2t\sin t} = \frac{1}{3a\cos^4t\sin t}.
$$

**Example 4.4.8** Let $y = y(x)$ be determined by the equation $\mathrm{e}^y-xy = 0$. Find $\frac{\mathrm{d}^2y}{\mathrm{d}x^2}$.

**Solution** Differentiating both sides with respect to $x$ gives $\mathrm{e}^yy'-y-xy' = 0$, so $y' = \frac{y}{\mathrm{e}^y-x}$. Differentiating again (the $y$ in $y'$ is still a function of $x$),

$$
y'' = \frac{y'(\mathrm{e}^y-x)-y(\mathrm{e}^yy'-1)}{(\mathrm{e}^y-x)^2} = \frac{2y(\mathrm{e}^y-x)-y^2\mathrm{e}^y}{(\mathrm{e}^y-x)^3},
$$

where in the last step we substituted $y' = \frac{y}{\mathrm{e}^y-x}$.

Second derivatives of inverse functions. Let $y = f(x)$ be twice differentiable with $f'\ne0$, and let $x = g(y)$ be its inverse function. Differentiating the identity $f(g(y)) = y$ twice gives $f'(g(y))g'(y) = 1$ and $f''(g(y))g'(y)^2+f'(g(y))g''(y) = 0$, so

$$
g'(y) = \frac{1}{f'(x)},\qquad g''(y) = -\frac{f''(x)}{f'(x)^3},\qquad x = g(y).
$$

**Example 4.4.9** Let $y = \mathrm{e}^x+x+1$ and let $x = g(y)$ be its inverse function. Find $g'(2)$ and $g''(2)$.

**Solution** For $y = 2$ we have $x = 0$. Then $g'(y) = \frac{1}{\mathrm{e}^x+1}$, so $g'(2) = \frac12$; and $g''(y) = -\frac{\mathrm{e}^x}{(\mathrm{e}^x+1)^3}$, so $g''(2) = -\frac18$.

## 4.5. Differentials

### 4.5.1. The Concept of the Differential

Given a function $y = f(x)$, an increment $\Delta x$ of the independent variable at $x_0$ causes an increment $\Delta y = f(x_0+\Delta x)-f(x_0)$ of the function. In general the relation between $\Delta y$ and $\Delta x$ is complicated; the simplest relation is a linear one, or an approximately linear one.

**Definition 4.5.1 (Differential)** If there is a constant $a$, independent of $\Delta x$, such that as $\Delta x\to0$

$$
\Delta y = f(x_0+\Delta x)-f(x_0) = a\,\Delta x+o(\Delta x),
$$
then $f$ is said to be differentiable at $x_0$ in the sense of differentials, and the linear principal part $a\,\Delta x$ is called the **differential** of $f$ at $x_0$, denoted $\mathrm{d}f(x_0) = a\,\Delta x$.

**Theorem 4.5.1** $f$ has a differential at $x_0$ $\iff$ $f$ is differentiable at $x_0$, and then $\mathrm{d}f(x_0) = f'(x_0)\Delta x$.

**Proof** If $f$ has a differential at $x_0$, so that $\Delta y = a\Delta x+o(\Delta x)$, then $\frac{\Delta y}{\Delta x} = a+\frac{o(\Delta x)}{\Delta x}\to a$, that is, $f'(x_0) = a$. Conversely, if $f$ is differentiable at $x_0$, then by Eq. (4.1) $\Delta y = f'(x_0)\Delta x+o(\Delta x)$, so $f$ has a differential and $\mathrm{d}f(x_0) = f'(x_0)\Delta x$. $\square$

For the independent variable itself, $y = x$, we have $\mathrm{d}x = 1\cdot\Delta x$: the differential of the independent variable is its increment. The differential is therefore usually written $\mathrm{d}y = f'(x)\,\mathrm{d}x$, and the derivative is the quotient of two differentials, $f'(x) = \frac{\mathrm{d}y}{\mathrm{d}x}$; for this reason the derivative is also called a differential quotient. By convention, $\Delta x$ denotes a concrete small number (such as $0.01$), while $\mathrm{d}x$ is used for the formal linear principal part.

For functions of one variable, having a derivative and having a differential are equivalent, but the two are different concepts: the differential concerns whether the increments $\Delta y$ and $\Delta x$ are approximately linearly related, while the derivative concerns the limit of their ratio. For functions of several variables the two are no longer equivalent ([2.2.10](/2.2.10)), and the differential is the "right" concept.

**Example 4.5.1** $\mathrm{d}\cos x = -\sin x\,\mathrm{d}x$, $\mathrm{d}\ln x = \frac{\mathrm{d}x}{x}$ and $\mathrm{d}a^x = a^x\ln a\,\mathrm{d}x$.

Geometric interpretation of the differential. Let the curve $y = f(x)$ be differentiable at $x_0$. When the independent variable has an increment $\Delta x$, $\Delta y$ is the increment of the ordinate along the curve, whereas $\mathrm{d}y = f'(x_0)\Delta x$ is exactly the increment of the ordinate along the tangent line $y = y_0+f'(x_0)(x-x_0)$; their difference is an infinitesimal of higher order than $\Delta x$. Replacing the increment by the differential means replacing the curve by its tangent line near $x_0$ (local linearization).

![Δy is the increment of the ordinate along the curve, dy = f'(x₀)Δx is the increment along the tangent line, and the two differ by o(Δx).](./plots/differential-vs-increment.py)

### 4.5.2. Approximation by Differentials

From $\Delta y = f'(x_0)\Delta x+o(\Delta x)$, when $|x-x_0|$ is small,

$$
f(x)\approx f(x_0)+f'(x_0)(x-x_0).
$$

**Example 4.5.2** Use differentials to approximate $\sqrt{1.02}$.

**Solution** Take $f(x) = \sqrt x$ and $x_0 = 1$; then $f'(x) = \frac{1}{2\sqrt x}$ and $\sqrt{1.02}\approx1+\frac12\times0.02 = 1.01$ (the exact value is $1.00995\cdots$).

In choosing $x_0$ we must balance two requirements: $x_0$ should be close enough to $x$, and $f(x_0)$ and $f'(x_0)$ should be easy to compute. This approximation has two shortcomings: (1) a suitable $x_0$ is not always easy to find; (2) the accuracy is limited, and no error estimate is given. Improving it with higher-order derivatives leads to Taylor's formula in the next chapter ([2.2.5](/2.2.5)).

### 4.5.3. Rules for Differentials

From $\mathrm{d}f = f'\,\mathrm{d}x$ and the rules for derivatives we immediately obtain the arithmetic rules for differentials: if $u$ and $v$ are differentiable and $c$ is a constant, then

$$
\mathrm{d}(cu) = c\,\mathrm{d}u,\quad \mathrm{d}(u\pm v) = \mathrm{d}u\pm\mathrm{d}v,\quad \mathrm{d}(uv) = v\,\mathrm{d}u+u\,\mathrm{d}v,\quad \mathrm{d}\Bigl(\frac uv\Bigr) = \frac{v\,\mathrm{d}u-u\,\mathrm{d}v}{v^2}\ (v\ne0).
$$

For example, $\mathrm{d}(uv) = (uv)'\,\mathrm{d}x = (u'v+uv')\,\mathrm{d}x = v\,\mathrm{d}u+u\,\mathrm{d}v$.

Differentials of composite functions. If $y = y(u)$ and $u = u(x)$ are both differentiable, then $\mathrm{d}y = \frac{\mathrm{d}y}{\mathrm{d}x}\mathrm{d}x = \frac{\mathrm{d}y}{\mathrm{d}u}\frac{\mathrm{d}u}{\mathrm{d}x}\mathrm{d}x = \frac{\mathrm{d}y}{\mathrm{d}u}\mathrm{d}u$. In other words, whether $u$ is the independent variable or an intermediate variable,

$$
\mathrm{d}y = y'(u)\,\mathrm{d}u.
$$

This is called the *invariance of the first differential*. It allows us to treat an intermediate variable as if it were the independent variable when computing differentials, for example $\mathrm{d}\,\mathrm{e}^{\sin x} = \mathrm{e}^{\sin x}\,\mathrm{d}\sin x = \mathrm{e}^{\sin x}\cos x\,\mathrm{d}x$; it also underlies the method of "absorbing a factor into the differential" (the first substitution method) in [2.2.6](/2.2.6). For an implicit function, we can also take differentials of both sides of the equation directly: from $y^3+y^2 = 2x^2$ we get $(3y^2+2y)\,\mathrm{d}y = 4x\,\mathrm{d}x$, in agreement with Example 4.3.5. Higher-order differentials do not have this invariance: $\mathrm{d}^2y = y''\,\mathrm{d}x^2$ when $x$ is the independent variable, but an extra term $y'\,\mathrm{d}^2x$ appears when $x$ is an intermediate variable.

**Example 4.5.3** Let $f$ be differentiable at $x_0$, and let the sequences $\{x_n\}$ and $\{y_n\}$ satisfy $x_n<x_0<y_n$, $x_n\to x_0$ and $y_n\to x_0$. Find $\lim\limits_{n\to\infty}\frac{f(y_n)-f(x_n)}{y_n-x_n}$.

**Solution** By differentiability, $f(y_n) = f(x_0)+f'(x_0)(y_n-x_0)+o(y_n-x_0)$ and $f(x_n) = f(x_0)+f'(x_0)(x_n-x_0)+o(x_n-x_0)$; subtracting,

$$
\frac{f(y_n)-f(x_n)}{y_n-x_n} = f'(x_0)+\frac{o(y_n-x_0)}{y_n-x_0}\cdot\frac{y_n-x_0}{y_n-x_n}-\frac{o(x_n-x_0)}{x_n-x_0}\cdot\frac{x_n-x_0}{y_n-x_n}.
$$

Since $0<\frac{y_n-x_0}{y_n-x_n}<1$ and $0<\frac{x_0-x_n}{y_n-x_n}<1$ are bounded, the last two terms tend to $0$, and the limit is $f'(x_0)$. The condition $x_n<x_0<y_n$ cannot be dropped: for example, $f = x^2\sin\frac1x$ (Example 4.1.6) is differentiable at $0$, but if $x_n$ and $y_n$ are taken on the same side of $0$, the slopes of the secant lines need not tend to $f'(0) = 0$.

## Summary

| Concept or rule | Content |
|---|---|
| Derivative | $f'(x_0) = \lim\limits_{\Delta x\to0}\frac{f(x_0+\Delta x)-f(x_0)}{\Delta x}$; differentiable $\iff$ $f'_-(x_0) = f'_+(x_0)$ |
| Tangent and normal lines | $y-y_0 = f'(x_0)(x-x_0)$; $y-y_0 = -\frac{1}{f'(x_0)}(x-x_0)$ |
| Differential, derivative, continuity | Has a differential $\iff$ differentiable $\implies$ continuous, but not conversely ($\lvert x\rvert$); differentiability does not guarantee a continuous derivative ($x^2\sin\frac1x$) |
| Arithmetic rules | $(fg)' = f'g+fg'$, $\bigl(\frac fg\bigr)' = \frac{f'g-fg'}{g^2}$ |
| Chain rule | $\frac{\mathrm{d}y}{\mathrm{d}x} = \frac{\mathrm{d}y}{\mathrm{d}u}\cdot\frac{\mathrm{d}u}{\mathrm{d}x}$ |
| Inverse functions | $\frac{\mathrm{d}x}{\mathrm{d}y} = 1\big/\frac{\mathrm{d}y}{\mathrm{d}x}$, $g'' = -\frac{f''}{f'^3}$ |
| Logarithmic differentiation | $(u^v)' = u^v\bigl(v'\ln u+\frac{vu'}{u}\bigr)$ |
| Parametric equations | $\frac{\mathrm{d}y}{\mathrm{d}x} = \frac{\psi'}{\varphi'}$, $\frac{\mathrm{d}^2y}{\mathrm{d}x^2} = \frac{\varphi'\psi''-\psi'\varphi''}{\varphi'^3}$ |
| Implicit functions | Differentiate both sides of the equation with respect to $x$, regarding $y$ as a function of $x$, and solve for $y'$ |
| Higher-order derivatives | $(\sin x)^{(n)} = \sin\bigl(x+\frac{n\pi}2\bigr)$, $\bigl(\frac1{ax+b}\bigr)^{(n)} = \frac{(-1)^nn!\,a^n}{(ax+b)^{n+1}}$, $(fg)^{(n)} = \sum\binom nkf^{(k)}g^{(n-k)}$ |
| Differentials | $\mathrm{d}y = f'(x)\,\mathrm{d}x$, $\Delta y = \mathrm{d}y+o(\Delta x)$; invariance of the first differential: $\mathrm{d}y = y'(u)\,\mathrm{d}u$ |
| Approximation | $f(x)\approx f(x_0)+f'(x_0)(x-x_0)$ |
