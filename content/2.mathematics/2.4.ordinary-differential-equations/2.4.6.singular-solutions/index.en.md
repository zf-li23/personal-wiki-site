---
title: Singular Solutions and Envelopes
source_hash: c259fd8708ac
---

A first-order equation usually has a **general solution** containing one arbitrary constant, and it may also have special solutions that are not contained in the general solution. One class of such solutions has a striking geometric feature: at each of its points another solution is tangent to it, so uniqueness fails everywhere along it. Such solutions are called singular solutions. This chapter first completes the treatment of implicit first-order equations $F(x,y,y')=0$, which elementary integration has not yet covered (the differentiation method, the parametric method, Clairaut's equation). We then study singular solutions from two points of view: without knowing the general solution, we look for singular solutions through the $p$-discriminant; when the general solution is known, a singular solution is the envelope of the family of integral curves and is found from the $C$-discriminant. Finally we turn to geometric applications of envelopes: curves determined by properties of their tangent lines, the astroid, evolutes and involutes, and envelopes of families of surfaces.

By the Picard theorem of [2.4.4](/2.4.4), an explicit equation $y'=f(x,y)$ has no singular solutions in a region where $f$ satisfies a local Lipschitz condition. Singular solutions can occur only where the conditions for uniqueness fail; for an implicit equation, these are the places where $p$ cannot be solved smoothly from $F(x,y,p)=0$, that is, where $F_p=0$. This chapter uses the **implicit function theorem** from [2.2.10](/2.2.10). Throughout we write $p=y'=\dfrac{\mathrm{d}y}{\mathrm{d}x}$.

## 6.1. Implicit First-Order Equations

### 6.1.1. The Differentiation Method

Suppose that $F(x,y,p)=0$ can be solved for $y$:

$$
y=f(x,p), \tag{6.1}
$$
where $f$ is continuously differentiable. Differentiating both sides with respect to $x$ and using $y'=p$, we get

$$
p=f_x(x,p)+f_p(x,p)\frac{\mathrm{d}p}{\mathrm{d}x},\qquad\text{i.e.}\qquad\big(f_x(x,p)-p\big)\,\mathrm{d}x+f_p(x,p)\,\mathrm{d}p=0.
$$
This is an explicit first-order equation in $x$ and $p$. If its general solution is $p=u(x,C)$, then the general solution of Eq. (6.1) is $y=f(x,u(x,C))$; if it is more convenient to write the general solution as $x=v(p,C)$, we obtain the general solution in parametric form, with $p$ as the parameter:

$$
x=v(p,C),\qquad y=f\big(v(p,C),p\big).
$$
An equation $x=g(y,p)$ is treated in the same way, by differentiating with respect to $y$ and using $\dfrac{\mathrm{d}x}{\mathrm{d}y}=\dfrac1p$. If the differentiated equation contains a factor free of derivatives, the solutions given by that factor are often special solutions and must be checked separately.

**Example 6.1.1** Solve $y=p^2-xp+\dfrac{x^2}{2}$. Differentiating with respect to $x$ gives $p=2pp'-p-xp'+x$, which rearranges to

$$
(2p-x)(p'-1)=0.
$$
From $p'=1$ we get $p=x+C$, and substituting back gives the general solution $y=\dfrac{x^2}{2}+Cx+C^2$. From $2p-x=0$ we get $p=\dfrac x2$, and substituting back gives $y=\dfrac{x^2}{4}$; one checks that it satisfies the equation, so it is a solution not contained in the general solution. Example 6.3.2 will show that it is a singular solution.

An equation of the form $y=x\varphi(p)+\psi(p)$ is called a Lagrange equation (or d'Alembert equation). The differentiation method turns it into $\big(p-\varphi(p)\big)\dfrac{\mathrm{d}x}{\mathrm{d}p}-x\varphi'(p)=\psi'(p)$, a first-order linear equation for $x$ as a function of $p$. The special case $\varphi(p)=p$ is Clairaut's equation, treated below.

### 6.1.2. The Parametric Method

Suppose the equation does not contain $x$ explicitly: $F(y,p)=0$. If this curve in the $(y,p)$-plane has a parametrization $y=g(t)$, $p=h(t)$, then from $\mathrm{d}y=p\,\mathrm{d}x$,

$$
\mathrm{d}x=\frac{\mathrm{d}y}{p}=\frac{g'(t)}{h(t)}\,\mathrm{d}t,
$$
and integration gives the general solution with parameter $t$:

$$
x=\int\frac{g'(t)}{h(t)}\,\mathrm{d}t+C,\qquad y=g(t).
$$
A parameter value with $h(t_0)=0$ gives the constant solution $y=g(t_0)$, which must be checked separately. An equation $F(x,p)=0$ not containing $y$ is handled in the same way, now integrating $\mathrm{d}y=p\,\mathrm{d}x$ to find $y$. For a general equation $F(x,y,p)=0$, if the surface it defines can be parametrized as $x=x(u,v)$, $y=y(u,v)$, $p=p(u,v)$, then $\mathrm{d}y=p\,\mathrm{d}x$ becomes a first-order equation relating $u$ and $v$.

**Example 6.1.2** Solve $(y')^2+y^2=1$. Put $y=\sin\theta$, $p=\cos\theta$. Then $\cos\theta\,\mathrm{d}\theta=\mathrm{d}y=p\,\mathrm{d}x=\cos\theta\,\mathrm{d}x$. Where $\cos\theta\ne0$ we have $\mathrm{d}\theta=\mathrm{d}x$, so $\theta=x+C$, and the general solution is $y=\sin(x+C)$. The condition $\cos\theta=0$ gives $y=\pm1$; these are also solutions, but they are not contained in the general solution.

### 6.1.3. Clairaut's Equation

**Definition 6.1.1** An equation of the form

$$
y=xp+f(p) \tag{6.2}
$$
where $f$ is twice continuously differentiable, is called a **Clairaut equation**.

By the differentiation method, $p=p+xp'+f'(p)p'$, that is, $\big(x+f'(p)\big)p'=0$.

- From $p'=0$ we get $p=C$ and the general solution $y=Cx+f(C)$: a family of straight lines.
- From $x+f'(p)=0$ we get the curve with parameter $p$

$$
x=-f'(p),\qquad y=f(p)-pf'(p). \tag{6.3}
$$
When $f''(p)\ne0$, the relation $x=-f'(p)$ can be inverted to give $p=p(x)$, and $\dfrac{\mathrm{d}y}{\mathrm{d}x}=\dfrac{\mathrm{d}y/\mathrm{d}p}{\mathrm{d}x/\mathrm{d}p}=\dfrac{-pf''(p)}{-f''(p)}=p$, so the curve (6.3) is a solution of Eq. (6.2). It is not a straight line (its slope $p$ varies from point to point), so it is not contained in the general solution.

**Example 6.1.3** The general solution of the Clairaut equation $y=xp-\dfrac{p^2}{4}$ is the family of lines $y=Cx-\dfrac{C^2}{4}$; by (6.3), $x=\dfrac p2$, $y=\dfrac{p^2}{4}$, which is the parabola $y=x^2$. The line $y=Cx-\frac{C^2}{4}$ is exactly the tangent line to the parabola $y=x^2$ at the point $\big(\frac C2,\frac{C^2}{4}\big)$: every line of the general solution is tangent to this special solution.

![The general solution of the Clairaut equation y = x p - p^2/4 (the family of lines y = C x - C^2/4) and the special solution y = x^2: every line is tangent to the parabola, which is the envelope of the family of lines and a singular solution of the equation](./plots/clairaut-envelope.py)

## 6.2. Singular Solutions

**Definition 6.2.1** Let $\Gamma\colon y=\varphi(x)$ ($x\in J$) be a solution of the first-order equation $F(x,y,y')=0$. If for every point $Q$ of $\Gamma$, every neighborhood of $Q$ contains a solution of the equation that is different from $\Gamma$ and tangent to $\Gamma$ at $Q$, then $\Gamma$ is called a **singular solution** of the equation.

A singular solution destroys uniqueness at every point: there are at least two solutions through $Q$ with the same slope. In Example 6.1.2 the line $y=1$ is a singular solution: through any of its points $(x_1,1)$, the solution $y=\sin(x-x_1+\frac\pi2)$ takes the value $1$ with slope $0$ there, so it is tangent to $y=1$ without coinciding with it. The same holds for $y=-1$.

**Definition 6.2.2** Let $F(x,y,p)$ be differentiable with respect to $p$. The system

$$
F(x,y,p)=0,\qquad F_p(x,y,p)=0 \tag{6.4}
$$
is called the **p-discriminant** of the equation $F(x,y,y')=0$; the curve defined by the equation $\Delta(x,y)=0$ obtained by eliminating $p$ from it is called the $p$-discriminant curve.

**Theorem 6.2.1 (Necessary Condition for Singular Solutions)** Let $F(x,y,p)$ be continuous in a region $D\subset\mathbb{R}^3$ with continuous partial derivatives $F_y,F_p$. If $y=\varphi(x)$ ($x\in J$) is a singular solution of the equation $F(x,y,y')=0$ with $(x,\varphi(x),\varphi'(x))\in D$, then it satisfies the $p$-discriminant:

$$
F(x,\varphi(x),\varphi'(x))=0,\qquad F_p(x,\varphi(x),\varphi'(x))=0,\qquad x\in J.
$$

**Proof** The first equation holds because $\varphi$ is a solution. Suppose the second fails at some point $x_1$: $F_p(x_1,y_1,p_1)\ne0$, where $y_1=\varphi(x_1)$ and $p_1=\varphi'(x_1)$. By the implicit function theorem, in some neighborhood $U$ of $(x_1,y_1,p_1)$ the equation $F(x,y,p)=0$ is equivalent to $p=f(x,y)$, where $f$ is continuous and $f_y=-F_y/F_p$ is continuous, so $f$ satisfies a local Lipschitz condition near $(x_1,y_1)$. Any solution $\psi$ tangent to $\Gamma$ at $Q=(x_1,y_1)$ satisfies $\psi(x_1)=y_1$ and $\psi'(x_1)=p_1$; by continuity of $\psi'$, we have $(x,\psi,\psi')\in U$ for $x$ close to $x_1$, hence $\psi'=f(x,\psi)$, and the same holds for $\varphi$. By the uniqueness part of the Picard theorem, $\psi$ coincides with $\varphi$ near $x_1$, contradicting the definition of a singular solution. $\square$

Thus, to find singular solutions, we first determine the $p$-discriminant curve and then check each of its branches: is it a solution, and is it a singular one? A branch of the $p$-discriminant curve may fail to be a solution at all, or it may be a solution without being singular (Example 6.2.1). The next theorem gives a sufficient condition that does not require the general solution.

**Theorem 6.2.2 (Sufficient Condition for Singular Solutions)** Let $F(x,y,p)$ be twice continuously differentiable in $D$, and suppose the function $y=\psi(x)$ ($x\in J$) obtained by eliminating $p$ from the $p$-discriminant (6.4) is a solution of the equation $F(x,y,y')=0$ with

$$
F_y(x,\psi(x),\psi'(x))\ne0,\qquad F_{pp}(x,\psi(x),\psi'(x))\ne0,\qquad x\in J.
$$
Then $y=\psi(x)$ is a singular solution of the equation.

Sketch of proof: near a point of $\Gamma$ we may assume $F_y>0$ and $F_{pp}>0$. For fixed $x$, the function $p\mapsto F(x,\psi(x),p)$ has a nondegenerate minimum value $0$ at $p=\psi'(x)$ (since $F=F_p=0$ and $F_{pp}>0$). For $y$ slightly below $\psi(x)$, the condition $F_y>0$ makes this minimum negative, so the equation $F=0$ has two roots $p_-(x,y)<p_+(x,y)$ near $\psi'(x)$; there $F_p\ne0$, so by the implicit function theorem they depend smoothly on $(x,y)$, and both tend to $\psi'(x)$ as $y\to\psi(x)$. For $y$ slightly above $\psi(x)$ there are no real roots. Thus below $\Gamma$ there are two direction fields $y'=p_\pm(x,y)$ whose directions on $\Gamma$ coincide with the tangent direction of $\Gamma$. This is the same situation as for $y'=\pm\sqrt{\lvert y\rvert}$ near $y=0$ (Example 4.3.1), and one can show that through each point of $\Gamma$ there are integral curves of these fields tangent to $\Gamma$. The condition $F_y\ne0$ guarantees this structure of "two roots on one side, none on the other"; when $F_y=0$ the conclusion may fail (Example 6.2.1(3)).

**Example 6.2.1** (1) $(y')^2+y^2=1$: $F_p=2p=0$, and substitution gives $y=\pm1$. These are solutions, with $F_y=2y=\pm2\ne0$ and $F_{pp}=2\ne0$, so by Theorem 6.2.2 they are singular solutions, in agreement with the direct verification above.

(2) $(y')^2=y$: the $p$-discriminant gives $y=0$, which is a solution with $F_y=-1\ne0$ and $F_{pp}=2\ne0$, hence a singular solution. The general solution $y=\dfrac{(x-C)^2}{4}$ is a family of parabolas tangent to the $x$-axis.

(3) $(y')^2=y^2$: the $p$-discriminant gives $y=0$, which is a solution, but $F_y=-2y=0$, so Theorem 6.2.2 does not apply. In fact the equation is $y'=\pm y$, with solutions $y=C\mathrm{e}^{\pm x}$; it satisfies a local Lipschitz condition, the only solution through a point of the $x$-axis is $y=0$, and therefore $y=0$ is not a singular solution.

(4) $(y')^2=x$: the $p$-discriminant gives $x=0$, a vertical line, which is not a solution of the form $y=\varphi(x)$; the equation has no singular solution.

## 6.3. Envelopes of Families of Curves

### 6.3.1. Envelopes and the C-Discriminant

**Definition 6.3.1** Consider a one-parameter family of curves

$$
K(C)\colon V(x,y,C)=0 \tag{6.5}
$$
with $V$ continuously differentiable. A continuously differentiable plane curve $\Gamma$ is called an **envelope** of the family (6.5) if for every point $q$ of $\Gamma$ there is a curve $K(C^*)$ of the family that passes through $q$, is tangent to $\Gamma$ at $q$, and differs from $\Gamma$ in every neighborhood of $q$.

For example, the line $y=1$ is an envelope of the family of parabolas $y=(x-C)^2+1$, and the parabola $y=x^2$ is an envelope of the family of lines $y=Cx-\frac{C^2}{4}$ (Example 6.1.3).

**Definition 6.3.2** The system

$$
V(x,y,C)=0,\qquad V_C(x,y,C)=0 \tag{6.6}
$$
is called the **C-discriminant** of the family (6.5); the curve defined by the equation $\Omega(x,y)=0$ obtained by eliminating $C$ from it is called the $C$-discriminant curve.

**Theorem 6.3.1 (Necessary Condition for Envelopes)** Let $\Gamma$ be an envelope of the family (6.5) that can be written as $x=\varphi(C)$, $y=\psi(C)$ with $\varphi,\psi$ continuously differentiable, where $(\varphi(C),\psi(C))$ is the point of tangency of $\Gamma$ and $K(C)$. Then $\Gamma$ satisfies the $C$-discriminant (6.6).

**Proof** The point of tangency lies on $K(C)$, so $V(\varphi(C),\psi(C),C)\equiv0$. Differentiating with respect to $C$ gives

$$
V_x\varphi'(C)+V_y\psi'(C)+V_C=0.
$$
If $(V_x,V_y)\ne(0,0)$ at the point of tangency, it is a normal vector of $K(C)$ there, while $(\varphi',\psi')$ is a tangent vector of $\Gamma$; since the two curves are tangent, $V_x\varphi'+V_y\psi'=0$, and therefore $V_C=0$. If $(V_x,V_y)=(0,0)$, the equation above gives $V_C=0$ directly. $\square$

The proof also shows what else may enter the $C$-discriminant curve: points where $V_x=V_y=0$ are singular points (nodes, cusps) of the curves $K(C)$, and the locus of these singular points satisfies the $C$-discriminant without necessarily being an envelope. To exclude them we need a nondegeneracy condition.

**Theorem 6.3.2 (Sufficient Condition for Envelopes)** Suppose the $C$-discriminant (6.6) determines a continuously differentiable curve $\Lambda\colon x=\varphi(C)$, $y=\psi(C)$ ($C\in J$), no arc of which is contained in a single curve of the family, and that the nondegeneracy conditions

$$
\big(\varphi'(C),\psi'(C)\big)\ne(0,0),\qquad\big(V_x,V_y\big)\ne(0,0)
$$
hold, where $V_x,V_y$ are evaluated at $(\varphi(C),\psi(C),C)$. Then $\Lambda$ is an envelope of the family (6.5).

**Proof** Since $V(\varphi(C),\psi(C),C)\equiv0$, the point $(\varphi(C),\psi(C))$ lies on $K(C)$. Differentiating with respect to $C$ and using $V_C=0$ gives $V_x\varphi'+V_y\psi'=0$. By the nondegeneracy conditions, $\Lambda$ is a regular curve at this point with tangent vector $(\varphi',\psi')\ne\boldsymbol{0}$, and $K(C)$ is also regular there with normal vector $(V_x,V_y)\ne\boldsymbol{0}$. The tangent vector of $\Lambda$ is orthogonal to the normal vector of $K(C)$, so the two curves are tangent at this point. Moreover, by hypothesis, $K(C)$ differs from $\Lambda$ in every neighborhood of the point. $\square$

### 6.3.2. Envelopes and Singular Solutions

**Theorem 6.3.3** Suppose the equation $F(x,y,y')=0$ has a general integral $U(x,y,C)=0$ and the family of integral curves has an envelope $\Gamma\colon y=\varphi(x)$ ($x\in J$). Then $\Gamma$ is a singular solution of the equation.

**Proof** For any point $q=(x_1,\varphi(x_1))$ of $\Gamma$ there is an integral curve $y=y_C(x)$ tangent to $\Gamma$ at $q$, so $y_C(x_1)=\varphi(x_1)$ and $y_C'(x_1)=\varphi'(x_1)$. Since $y_C$ is a solution, $F(x_1,y_C(x_1),y_C'(x_1))=0$, that is, $F(x_1,\varphi(x_1),\varphi'(x_1))=0$. As $x_1$ is arbitrary, $\varphi$ is a solution; and since at every point there is a solution different from $\Gamma$ tangent to it, it is a singular solution. $\square$

There are thus two ways to find singular solutions: without the general solution, use the $p$-discriminant (Theorems 6.2.1 and 6.2.2); with a general integral, find its $C$-discriminant curve and use the nondegeneracy conditions to pick out the envelope (Theorems 6.3.2 and 6.3.3). Both discriminant curves may contain branches that are not singular solutions: the $p$-discriminant curve may contain the locus of cusps of the integral curves, and the $C$-discriminant curve may contain the locus of their nodes.

**Example 6.3.1** Find the singular solutions of $(y-1)^2(y')^2=\dfrac49y$. The equation is $(y-1)y'=\pm\dfrac23\sqrt y$ ($y\ge0$). For $y>0$, separating variables gives $\Big(\sqrt y-\dfrac1{\sqrt y}\Big)\mathrm{d}y=\pm\dfrac23\,\mathrm{d}x$; integrating, $\dfrac23y^{1/2}(y-3)=\pm\dfrac23(x-C)$, and squaring gives the general integral

$$
V(x,y,C)=y(y-3)^2-(x-C)^2=0.
$$
In the $C$-discriminant, $V_C=2(x-C)=0$, and substitution gives $y(y-3)^2=0$, i.e. the two branches $\Lambda_1\colon x=C,\ y=0$ and $\Lambda_2\colon x=C,\ y=3$.

- $\Lambda_1$: $(\varphi',\psi')=(1,0)$; $V_x=-2(x-C)=0$ and $V_y=(y-3)(3y-3)=9\ne0$. The branch is nondegenerate, hence an envelope, and $y=0$ is a singular solution (directly: it satisfies the equation).
- $\Lambda_2$: $V_x=0$ and $V_y=0$, so the branch is degenerate. Indeed $y=3$ does not satisfy the equation (the left-hand side is $0$, the right-hand side $\frac43$); the two branches of the integral curve $x-C=\pm(y-3)\sqrt y$ cross at $(C,3)$, forming a node, and $y=3$ is the locus of nodes, not an envelope.

Check with the $p$-discriminant: $F_p=2(y-1)^2p=0$ gives $p=0$ (and then $y=0$) or $y=1$ (then $F=-\frac49\ne0$, rejected), so again only $y=0$ remains.

![The family of integral curves (x - C)^2 = y (y - 3)^2 of (y - 1)^2 (y')^2 = 4y/9: each curve is tangent to the x-axis (the envelope y = 0 is a singular solution) and crosses itself at y = 3, forming a node (the locus of nodes y = 3 is not a solution)](./plots/envelope-node-locus.py)

**Example 6.3.2** For the general solution $y=\dfrac{x^2}{2}+Cx+C^2$ of Example 6.1.1, the $C$-discriminant gives $V_C=x+2C=0$, so $C=-\dfrac x2$, and substitution gives $y=\dfrac{x^2}{4}$. The nondegeneracy conditions hold ($V_y=-1$, $\varphi'(C)=-2$), so $y=\dfrac{x^2}4$ is an envelope and hence a singular solution.

**Example 6.3.3 (A Solution Not Contained in the General Solution Need Not Be Singular)** Dividing the equation $y\,\mathrm{d}x-x\,\mathrm{d}y=0$ by $y^2$ gives $\mathrm{d}\big(\frac xy\big)=0$, with general solution $x=Cy$, the family of lines through the origin (other than the $x$-axis). The line $y=0$ is also a solution and cannot be obtained from the general solution for any $C$. But it is not singular: no line of the general solution passes through a point $(x_1,0)$ with $x_1\ne0$, so the only solution through that point is $y=0$. The family $x=Cy$ also has no envelope (the $C$-discriminant $V_C=-y=0$ together with $x=Cy$ gives only the origin). Similarly, the solution $x=0$ of $x\,\mathrm{d}y-y\,\mathrm{d}x=0$ is not in the general solution $y=Cx$, and it is not singular either.

### 6.3.3. Singular Solutions of Clairaut's Equation

**Proposition 6.3.1** If $f''\ne0$, the special solution (6.3) of the Clairaut equation (6.2) is an envelope of the family of lines $y=Cx+f(C)$ forming the general solution, and is therefore a singular solution.

**Proof** Take $V=Cx+f(C)-y$. Then $V_C=x+f'(C)=0$ gives $x=-f'(C)$, $y=f(C)-Cf'(C)$, which is (6.3). Since $\varphi'(C)=-f''(C)\ne0$ and $V_y=-1\ne0$, the nondegeneracy conditions hold; the slope $C$ of (6.3) varies from point to point, so no arc of it lies on a single line. The claim follows from Theorems 6.3.2 and 6.3.3. $\square$

Clairaut's equation therefore provides a way to "construct an equation with a prescribed singular solution": the set of all tangent lines of a convex curve satisfies a Clairaut equation, and the curve itself is its singular solution.

**Example 6.3.4** Construct an equation having $y=\sin x$ ($0<x<\pi$) as a singular solution. On $(0,\pi)$ we have $y''<0$ for $y=\sin x$. The tangent line at the point $x$ has slope $t=\cos x$ and intercept $\sin x-x\cos x$. Since $x=\arccos t$ and $\sin x=\sqrt{1-t^2}$, the family of tangent lines is $y=tx+f(t)$ with

$$
f(t)=\sqrt{1-t^2}-t\arccos t,\qquad f'(t)=-\arccos t,\qquad f''(t)=\frac{1}{\sqrt{1-t^2}}\ne0.
$$
Hence $y=xy'+\sqrt{1-(y')^2}-y'\arccos y'$ is a Clairaut equation with general solution $y=Cx+\sqrt{1-C^2}-C\arccos C$; by (6.3), $x=-f'(p)=\arccos p$ and $y=\sin x$, which is a singular solution by Proposition 6.3.1.

## 6.4. Geometric Applications

Many geometric problems ask for a curve whose tangent lines satisfy some condition. Often the tangent lines themselves automatically satisfy the condition, so such problems lead to Clairaut equations: the general solution consists of the straight lines satisfying the condition, and the curve actually sought is the singular solution. Let the tangent line to a curve $y=y(x)$ at the point $(x,y)$ be $Y-y=p(X-x)$; it meets the $x$-axis and the $y$-axis at $\big(x-\frac yp,0\big)$ and $(0,y-xp)$ respectively.

### 6.4.1. Tangent Lines Cutting Off a Triangle of Constant Area

**Example 6.4.1** Find the curves whose tangent line at each point forms, together with the two coordinate axes, a triangle of constant area $S$. Consider first the first quadrant, where both intercepts are positive:

$$
\Big(x-\frac yp\Big)(y-xp)=2S,\qquad\text{i.e.}\qquad(y-xp)^2=-2Sp,
$$
so $y=xp\pm\sqrt{-2Sp}$ ($p<0$), a Clairaut equation. The general solution $y=Cx\pm\sqrt{-2SC}$ ($C<0$) consists of the lines whose intercepts have product $2S$. Taking the plus sign, (6.3) gives

$$
x=-f'(C)=\frac{S}{\sqrt{-2SC}},\qquad y=Cx+\sqrt{-2SC}=\frac{\sqrt{-2SC}}{2},
$$
and eliminating $C$ yields $xy=\dfrac S2$. So the required curves are the hyperbola $xy=\dfrac S2$ (in the first and third quadrants) and, similarly, $xy=-\dfrac S2$ (in the second and fourth quadrants). Check: the tangent line to the hyperbola $xy=k$ at $(x,y)$ has intercepts $2x$ and $2y$, and the area is $2xy=2k=S$.

### 6.4.2. Tangent Segments of Constant Length: the Astroid

**Example 6.4.2** Find the curves for which the segment of each tangent line between the two coordinate axes has constant length $a$. From the distance between the two intercepts,

$$
a^2=\Big(x-\frac yp\Big)^2+(y-xp)^2=\frac{1+p^2}{p^2}(y-xp)^2,
$$
so $y=xp\pm\dfrac{ap}{\sqrt{1+p^2}}$, a Clairaut equation with general solution $y=Cx\pm\dfrac{aC}{\sqrt{1+C^2}}$. Taking $f(C)=\dfrac{aC}{\sqrt{1+C^2}}$, so that $f'(C)=a(1+C^2)^{-3/2}$, (6.3) gives

$$
x=-a(1+C^2)^{-3/2},\qquad y=Cx+f(C)=aC^3(1+C^2)^{-3/2}.
$$
Then $x^{2/3}=a^{2/3}(1+C^2)^{-1}$ and $y^{2/3}=a^{2/3}C^2(1+C^2)^{-1}$, and adding,

$$
x^{2/3}+y^{2/3}=a^{2/3};
$$
the minus sign gives another part of the same curve. This curve is the *astroid*, with parametric equations $x=a\cos^3\theta$, $y=a\sin^3\theta$ ($0\le\theta\le2\pi$). It is the path of a point on a circle of radius $a/4$ rolling inside a circle of radius $a$ (the hypocycloid with four cusps); it is symmetric about both coordinate axes and the origin, has total length $6a$, and encloses area $\dfrac{3\pi a^2}{8}$. Physically, the envelope of all positions of a ladder of length $a$ sliding down a wall is an astroid.

![A segment of length a slides with its endpoints on the two coordinate axes; the envelope of all its positions (a family of lines) is the astroid x^{2/3} + y^{2/3} = a^{2/3}](./plots/astroid-envelope.py)

### 6.4.3. Evolutes and Involutes

**Definition 6.4.1** If the normal line to a curve $C$ at each point is a tangent line of a curve $\Gamma$, then $\Gamma$ is called the **evolute** of $C$, and $C$ is called an **involute** of $\Gamma$. When $\Gamma$ is a circle, $C$ is called an involute of the circle.

By definition, the evolute is the envelope of the family of **normal lines**.

**Theorem 6.4.1** The evolute $\Gamma$ of a curve $C\colon y=f(x)$ ($f''\ne0$) is the locus of its centers of curvature:

$$
X=x-\frac{y'(1+y'^2)}{y''},\qquad Y=y+\frac{1+y'^2}{y''}, \tag{6.7}
$$
where $y'=f'(x)$, $y''=f''(x)$, and $x$ is the parameter. If $C$ is given parametrically by $x=x(t)$, $y=y(t)$, then

$$
X=x-\frac{y'(x'^2+y'^2)}{x'y''-x''y'},\qquad Y=y+\frac{x'(x'^2+y'^2)}{x'y''-x''y'},
$$
where the derivatives are taken with respect to $t$.

**Proof** The family of normal lines of $C$ at the points $(x,f(x))$ is $V(X,Y,x)=(X-x)+f'(x)\big(Y-f(x)\big)=0$, with $x$ as parameter. In the $C$-discriminant,

$$
V_x=-1+f''(x)\big(Y-f(x)\big)-f'(x)^2=0,
$$
which gives $Y=f+\dfrac{1+f'^2}{f''}$; substituting into $V=0$ gives $X$, which is (6.7). These are exactly the coordinates of the center of **curvature** (which lies on the normal line, on the concave side, at a distance equal to the **radius of curvature** $\dfrac{(1+y'^2)^{3/2}}{\lvert y''\rvert}$). We have $V_X=1\ne0$, and $(X'(x),Y'(x))=(0,0)$ only at stationary points of the curvature (the vertices of the curve), where the evolute has cusps; elsewhere the nondegeneracy conditions hold. The parametric form is handled in the same way. $\square$

Conversely, finding the involutes of a given $\Gamma$ is a differential equation problem: the centers of curvature of $C$ must lie on $\Gamma$. Geometrically, an involute is traced by the end of a taut string unwound from $\Gamma$. Parametrize $\Gamma$ by arc length $s$ and let $\boldsymbol{T}(s)$ be its unit tangent vector. Then

$$
\boldsymbol{r}_C(s)=\boldsymbol{r}_\Gamma(s)+(k-s)\boldsymbol{T}(s),
$$
where $k$ is a constant (the total length of the string). Since $\boldsymbol{r}_C'(s)=(k-s)\boldsymbol{T}'(s)$ and $\boldsymbol{T}'\perp\boldsymbol{T}$, the tangent line of $C$ at each point is perpendicular to $\boldsymbol{T}$, that is, the tangent line of $\Gamma$ is the normal line of $C$. The involutes form a family (depending on $k$) of mutually "parallel" curves.

**Example 6.4.3** Parametrize the circle $x^2+y^2=R^2$ by arc length $t$: $\boldsymbol{r}_\Gamma=\big(R\cos\frac tR,R\sin\frac tR\big)$, $\boldsymbol{T}=\big(-\sin\frac tR,\cos\frac tR\big)$. The involutes are

$$
x=R\cos\frac tR-(t_0-t)\sin\frac tR,\qquad y=R\sin\frac tR+(t_0-t)\cos\frac tR,
$$
with $t_0$ a constant. The involute of a circle is the tooth profile of involute gears.

**Example 6.4.4** For the cycloid $x=a(t-\sin t)$, $y=a(1-\cos t)$ ($0\le t\le2\pi$), the arc length is $s=4a\big(1-\cos\frac t2\big)$ and the unit tangent vector is $\boldsymbol{T}=\big(\sin\frac t2,\cos\frac t2\big)$. Substituting into the formula above and writing $c=k-4a$, the involutes are

$$
x=a(t+\sin t)+c\sin\frac t2,\qquad y=a(3+\cos t)+c\cos\frac t2,
$$
with $c$ a constant. For $c=0$, putting $t=\tau+\pi$ gives $x=a(\tau-\sin\tau)+\pi a$, $y=a(1-\cos\tau)+2a$: one involute of a cycloid is a congruent cycloid. Equivalently, the evolute of a cycloid is a congruent cycloid; this is the basis of Huygens' design of the isochronous pendulum.

## 6.5. Envelopes of One-Parameter Families of Surfaces

The notion of envelope extends to families of surfaces in space, where it plays an important role in the theory of first-order partial differential equations ([2.4.14](/2.4.14), [2.5](/2.5)).

**Definition 6.5.1** Consider a one-parameter family of surfaces

$$
\{S_\alpha\}\colon F(x,y,z,\alpha)=0 \tag{6.8}
$$
where $F$ has continuous first-order partial derivatives with respect to all variables and the parameter $\alpha$. A surface $S$ is called an **envelope** of the family (6.8) if every point of $S$ lies on some surface $S_\alpha$ of the family, with $S$ and $S_\alpha$ having the same tangent plane at that point, and conversely every surface $S_\alpha$ of the family has the same tangent plane as $S$ at some point $P_\alpha$ of $S$.

As in Theorem 6.3.1, an envelope satisfies the system

$$
F(x,y,z,\alpha)=0,\qquad F_\alpha(x,y,z,\alpha)=0; \tag{6.9}
$$
the surface $\varphi(x,y,z)=0$ obtained by eliminating $\alpha$ is called the discriminant surface, and the envelope is contained in it. For fixed $\alpha$, the system (6.9) defines a curve on $S_\alpha$ along which $S_\alpha$ touches the envelope, called a characteristic curve; as $\alpha$ varies, the characteristic curves sweep out the envelope.

**Example 6.5.1** Find the envelope of the family of planes $x\cos\alpha+y\sin\alpha-z\sin\alpha=1$. From

$$
x\cos\alpha+(y-z)\sin\alpha=1,\qquad-x\sin\alpha+(y-z)\cos\alpha=0,
$$
squaring and adding to eliminate $\alpha$ gives $x^2+(y-z)^2=1$, a cylinder whose generators have direction $(0,1,1)$. Each plane touches it along one generator.

**Example 6.5.2** Find the envelope of the family of planes $\alpha^2x+2\alpha y+2z=2\alpha$. From $F_\alpha=2\alpha x+2y-2=0$ we get $\alpha=\dfrac{1-y}{x}$, and substituting into $\alpha^2x+2\alpha(y-1)+2z=0$ gives

$$
2xz-(y-1)^2=0,
$$
which is homogeneous of degree two in $(x,y-1,z)$: a cone with vertex $(0,1,0)$.
