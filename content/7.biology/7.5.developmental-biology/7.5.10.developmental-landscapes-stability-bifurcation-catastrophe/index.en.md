---
title: "Developmental Landscapes: Stability, Bifurcation and Catastrophe Theory"
description: "A qualitative mathematics of development: gradient dynamics and the Waddington landscape, writing a general flow in gradient form and its limits, Morse functions and the splitting lemma, unfoldings, codimension and universal unfoldings, the fold, cusp, swallowtail, butterfly and umbilic catastrophes, Mather's finite determinacy and Thom's seven elementary catastrophes, the Maxwell and perfect-delay conventions, symmetry, catastrophe models of blastulation and gastrulation, Boolean, Hill-function and piecewise-linear networks, and an assessment of catastrophe theory and of modern geometric models of cell fate."
---

Developmental biology describes its objects qualitatively: a group of cells becomes two groups, a sheet buckles, a boundary appears, a cell chooses one of two fates. These events are reproducible from embryo to embryo although no two embryos are quantitatively identical, which suggests that what is conserved is a qualitative, topological structure, stable under small changes of conditions. This chapter develops the mathematics of such structures for the simplest class of dynamics, those in which the state of a cell or a tissue region minimizes an energy or follows its gradient. The image is the **Waddington landscape** of [7.3.24](/7.3.24#def-24.7.4): valleys are stable states, ridges barriers, branch points decisions. Catastrophe theory answers a precise question about such landscapes: when a landscape depends on a few control parameters (position, time, the concentration of a signal), in how many essentially different ways can its minima appear, disappear and exchange? The answer for up to four parameters is Thom's list of seven elementary catastrophes. We derive it, discuss which minimum a real system occupies, look at Percus and Childress's catastrophe models of blastulation and **gastrulation**, and then turn to coarser descriptions (Boolean networks) and intermediate ones (Hill-function and piecewise-linear networks). The last section assesses the rise, fall and recent return of the geometric approach. The chapter uses stability theory and bifurcations from [2.4.11](/2.4.11) and the Taylor formula and extrema of [2.2.11](/2.2.11); the cusp already appeared in the **blastocoel** model of 7.5.5 and reappears in the clock-and-wavefront model of somitogenesis (7.5.23).

## 10.1. Why a Topological Description

The exact sciences usually seek a law that turns exact initial data into an exact future. For development this format is too strong: there are intrinsic fluctuations, the parameters are never known exactly, and the information that distinguishes one organism or one developmental path from another is qualitative. A stochastic description does not remove the difficulty, because it still does not supply the qualitative information. What is needed is a description stable against small, smooth perturbations of both input and output.

Let the internal variables that specify the state at a point of space-time be $\boldsymbol{q} = (q_\alpha)$: the concentrations of a few key molecules, or the densities of cell types. Treating space-time as continuous (by smoothing over cells, or by assuming that each cell's state is determined by a smooth underlying field), a complete description is the set of functions $\boldsymbol{q}(\boldsymbol{r}, t)$. An alternative is to describe interfaces: the surfaces $q_\alpha(\boldsymbol{r}, t) = Q_\alpha$, where $Q_\alpha$ might separate the presence and the absence of an $\alpha$-type cell, give the boundaries between groups of cells. Either way, such functions are naturally categorized by their remarkable events: their singularities that persist under small, smooth changes. How small and how smooth must be decided, and the mathematics depends on the decision; below, perturbations are bounded and infinitely differentiable.

**Definition 10.1.1 (Catastrophe Theory)** **Catastrophe theory** (René Thom, 1972; developed by Christopher Zeeman, Vladimir Arnold and others) is the part of singularity theory that classifies, up to smooth changes of coordinates, the generic ways in which the critical points of a smooth family of functions $E(\boldsymbol{q}; \boldsymbol{u})$ change their number and type as the control parameters $\boldsymbol{u}$ vary. A *catastrophe* is a point of control space at which such a change occurs, where a smoothly varying minimum may disappear or two minima exchange, producing a discontinuous jump in the state.

## 10.2. Gradient Dynamics and the Waddington Landscape

Whatever the short- and long-range interactions between cells, their net effect on a given cell (or a given point) can be summarized as a milieu in which the state is determined. In the quasi-static picture the state is not an explicit function of the milieu but minimizes an energy function $E(\boldsymbol{q}; \boldsymbol{r}, t)$ at each point; in the blastocoel model of 7.5.5 the relevant function was in fact $-E$, maximized, which shows that stationary points of every type deserve study. The mechanism enters only locally; behaviour in the large remains descriptive. This matches much of classical embryology, which speaks of "morphogenetic gradients", coordinate functions varying slowly in space that supply **positional information** (three of them suffice to label a position in three dimensions) and whose slow variation nevertheless induces singularities: abrupt boundaries between states.

The simplest dynamics behind quasi-statics is a gradient flow with friction,

$$
\dot q_\alpha = -\kappa\frac{\partial E}{\partial q_\alpha}(\boldsymbol{q}; \boldsymbol{u}),
\tag{10.1}
$$
along which $\dot E = -\kappa\lvert\nabla_{\boldsymbol{q}}E\rvert^2 \le 0$: $E$ is a **Lyapunov function** ([2.4.11](/2.4.11#sec-11.4)), trajectories run downhill and settle in minima. Overdamped mechanical systems are of this form with a friction matrix (Rayleigh's principle, 7.5.8, Example 8.6.1). Near a minimum $\boldsymbol{q}^0$, $\dot q_\alpha \approx -\kappa\sum_\beta(\partial^2E/\partial q_\alpha\partial q_\beta)(q_\beta - q_\beta^0)$, so the Hessian matrix of $E$ sets the relaxation rates. When a control parameter changes slowly with developmental time or position, the state tracks a moving minimum, and the qualitative events of development are the points where minima are born, die or split. This is Waddington's picture made precise (Figure 1); for noisy systems the potential can be generalized to the quasi-potential $U = -\ln P_{\mathrm{ss}}$ of 7.3.24.

![A developmental landscape: the potential E(x; u) = x⁴/4 − ux²/2 + vx over cell state x and developmental time t, with u = t − 1 and a small bias v = 0.04 (each time section shifted to minimum zero). A single valley (one state) splits at t = 1 into two valleys (two fates), a pitchfork, the symmetric section of the cusp catastrophe. The dark line follows a cell that tracks the nearest minimum (gradient flow); a small push just after the branch point sends it into the left valley](./plots/landscape.py)

Two extensions are worth noting. The connections between cells that establish the milieu can be included by minimizing a functional $E[\boldsymbol{q}(\boldsymbol{r}, t)]$ at each $t$, or, including non-quasi-static dynamics, over all space-time fields, an extension of the Euler–Lagrange (Hamilton) principle; but then the control space is one-dimensional ($t$) or empty, and the classification below does not apply directly. And internal parameters such as the adhesion constant $J$ and the Lagrange multiplier $\lambda$ of the blastocoel model enter naturally as controls, representing changes of species or experiment or arising from conservation laws, so the dimension of control space is not fixed in advance. We therefore consider simply a parametrized family of local variational problems, $\mathrm{d}E(\boldsymbol{q}; \boldsymbol{u}) = 0$, where $\boldsymbol{u}$ may but need not be space-time, and all functions are smooth ($C^\infty$) on a finite domain.

## 10.3. Writing a General Flow in Gradient Form

Minimizing an energy, $\dot q_\alpha = -\gamma_\alpha\,\partial E/\partial q_\alpha$, is a special case of the general flow

$$
\dot q_\alpha = X_\alpha(\boldsymbol{q}, t),
\tag{10.2}
$$
whose steady states are the zeros of $\boldsymbol{X}$. The intelligent general approach classifies singularities of vector fields and their unfoldings, which is a much harder theory (bifurcation theory, [2.4.11](/2.4.11#sec-11.6)). Percus and Childress describe a construction that makes the general case resemble the gradient case.

Write the equations of motion as the **Euler–Lagrange equation** ([2.4.13](/2.4.13)) of $\delta\int L\,\mathrm{d}t = 0$ with a Lagrangian linear in the velocities, $L = \sum_\alpha\dot q_\alpha U_\alpha(\boldsymbol{q}) - U(\boldsymbol{q})$. Since $\partial L/\partial q_\alpha = \sum_\beta\dot q_\beta\,\partial U_\beta/\partial q_\alpha - \partial U/\partial q_\alpha$ and $\frac{\mathrm{d}}{\mathrm{d}t}\partial L/\partial\dot q_\alpha = \sum_\beta\dot q_\beta\,\partial U_\alpha/\partial q_\beta$,

$$
\sum_\beta\Gamma_{\alpha\beta}\dot q_\beta = \frac{\partial U}{\partial q_\alpha}, \qquad \Gamma_{\alpha\beta} = \frac{\partial U_\beta}{\partial q_\alpha} - \frac{\partial U_\alpha}{\partial q_\beta},
\tag{10.3}
$$
so, if $\Gamma$ is invertible, $\dot q_\alpha = \sum_\beta(\Gamma^{-1})_{\alpha\beta}\,\partial U/\partial q_\beta$, a "force" $\nabla U$ balanced by a "drag" $\Gamma$. To reproduce a given flow (10.2) one needs $\partial U/\partial q_\alpha = \sum_\beta\Gamma_{\alpha\beta}X_\beta$, which holds if the $U_\alpha$ solve the linear first-order system $\sum_\beta X_\beta\,\partial U_\alpha/\partial q_\beta = -\sum_\beta U_\beta\,\partial X_\beta/\partial q_\alpha$ and $U = \sum_\beta X_\beta U_\beta$ (direct substitution). Then the steady states are the critical points $\nabla U = \boldsymbol{0}$, as desired.

**Proposition 10.3.1 (The Construction Is Conservative)** The matrix $\Gamma$ of Eq. (10.3) is antisymmetric. Consequently $U$ is a **first integral** of the flow, $\mathrm{d}U/\mathrm{d}t = 0$; $\Gamma$ is singular when the number of variables is odd; and the construction cannot represent motion towards an asymptotically stable steady state.

**Proof** Antisymmetry is evident from the definition. Along solutions, $\dot U = \sum_\alpha\dot q_\alpha\,\partial U/\partial q_\alpha = \sum_{\alpha\beta}\dot q_\alpha\Gamma_{\alpha\beta}\dot q_\beta = 0$. An antisymmetric matrix of odd order has $\det\Gamma = \det\Gamma^{\mathsf T} = (-1)^n\det\Gamma$, hence $\det\Gamma = 0$. Near an asymptotically stable steady state, every trajectory converges to it, so a continuous first integral must be constant on a neighbourhood; then $\nabla U = \boldsymbol{0}$ there and Eq. (10.3) gives no information. $\square$

**Example 10.3.1** For the harmonic oscillator $\dot x = y$, $\dot y = -x$, take $U_1 = y/2$, $U_2 = -x/2$. Then $U = X_1U_1 + X_2U_2 = (x^2 + y^2)/2$, $\Gamma_{12} = \partial U_2/\partial x - \partial U_1/\partial y = -1$, and $\Gamma\dot{\boldsymbol{q}} = (-\dot y, \dot x) = (x, y) = \nabla U$: the construction recovers the phase-space Lagrangian $L = \frac12(y\dot x - x\dot y) - U$, with $U$ the conserved energy.

So the "drag matrix" of this construction is not a friction: the representation is Hamiltonian-like and describes the steady states correctly but not their stability or the minimization that catastrophe theory assumes. Much, as Percus and Childress note, is hidden in the domain of existence of the $U_\alpha$ and the invertibility of $\Gamma$. The rigorous results go in another direction. Near a hyperbolic equilibrium every flow is topologically equivalent to its linearization (Hartman–Grobman), and every flow on a compact space is "gradient-like" away from its recurrent set: it has a complete Lyapunov function that decreases strictly along all trajectories that are not recurrent (Conley's theorem). Dynamics without cycles, such as the Morse–Smale systems used in modern fate models (10.13), therefore do admit landscape descriptions, but oscillators (7.5.23) and the closed orbits of conservative systems do not.

## 10.4. Morse Functions and the Splitting Lemma

Fix the controls and look at $E$ near a point where its gradient vanishes, a *critical* (singular) point $\bar{\boldsymbol{q}}$. By Taylor's formula,

$$
E(\boldsymbol{q}) = E(\bar{\boldsymbol{q}}) + \frac12\sum_{\alpha\beta}\frac{\partial^2E}{\partial q_\alpha\partial q_\beta}(\bar{\boldsymbol{q}})(q_\alpha - \bar q_\alpha)(q_\beta - \bar q_\beta) + \cdots
$$
The **Hessian matrix** $H$ of second derivatives is real symmetric, so an orthogonal change of variables $q_\alpha = \bar q_\alpha + \sum_\beta\Omega_{\alpha\beta}\xi_\beta$ diagonalizes it, and a rescaling $\xi_\alpha \to k_\alpha\xi_\alpha$ makes the eigenvalues $\lambda_\alpha \in \{0, +1, -1\}$: $E = \bar E + \frac12\sum_\alpha\lambda_\alpha\xi_\alpha^2 + \cdots$.

**Definition 10.4.1 (Morse Function)** A critical point is *nondegenerate* if $\det H \ne 0$ (no $\lambda_\alpha = 0$). A smooth function all of whose critical points are nondegenerate is a **Morse function**. The *index* of a nondegenerate critical point is the number of negative eigenvalues of $H$ (0 for a minimum).

**Theorem 10.4.1 (Morse Lemma and Genericity)** (i) Near a nondegenerate critical point there are coordinates in which $E = \bar E + \sum_\alpha\pm\xi_\alpha^2$ exactly. (ii) Morse functions are dense: arbitrarily close to any smooth function (in all derivatives simultaneously) there is a Morse function. (iii) Only nondegenerate critical points are stable, that is, persist with the same index under all small perturbations.

For example, the degenerate critical point of $E = x^3$ at $0$ splits under the perturbation $x^3 - 3\varepsilon^2x$ into a maximum at $x = -\varepsilon$ and a minimum at $x = \varepsilon$. So a single function is generically featureless (only its indices matter, and for minima not even those); the interesting events occur in *families*, which pass through degenerate critical points at isolated parameter values. A family of functions changes qualitatively only where it contains a degenerate critical point, and the structure of the family near such a point determines its larger structure. One therefore studies the *germ* of a function at a point (the class of functions that coincide with it in some neighbourhood); functions and germs are not distinguished below.

**Theorem 10.4.2 (Splitting Lemma)** Let $E$ have a critical point at $\boldsymbol{0} \in \mathbb{R}^n$ at which the Hessian has rank $n - l$. Then there are coordinates $(\xi'_1, \dots, \xi'_l, \xi''_1, \dots, \xi''_{n-l})$ in which

$$
E = \phi(\xi'_1, \dots, \xi'_l) + \sum_{\alpha=1}^{n-l}\lambda_\alpha(\xi''_\alpha)^2, \qquad \lambda_\alpha = \pm1,
$$
where $\phi$ has vanishing gradient and Hessian at $\boldsymbol{0}$: a constant plus terms of third and higher order.

Near a degenerate point only the $l$ "essential" variables (the corank) matter; the others contribute a nondegenerate quadratic form that does not change the qualitative behaviour. Biologically this is a strong statement: however many genes participate in a decision, only as many combinations as the corank behave non-trivially at the moment of decision (compare the reduction to a centre manifold in bifurcation theory).

## 10.5. Unfoldings, Codimension and Universal Unfoldings

**Definition 10.5.1 (Unfolding)** An **unfolding** of a germ $\phi(\boldsymbol{\xi})$, $\boldsymbol{\xi} \in \mathbb{R}^k$, is a family $\phi(\boldsymbol{\xi}; \boldsymbol{u})$, $\boldsymbol{u} \in \mathbb{R}^m$, with $\phi(\boldsymbol{\xi}; \boldsymbol{0}) = \phi(\boldsymbol{\xi})$. Two unfoldings $\phi_1(\boldsymbol{\xi}; \boldsymbol{u})$ and $\phi_2(\boldsymbol{\xi}; \boldsymbol{v})$ are *equivalent* if there are smooth changes of control variables $\boldsymbol{v} = \boldsymbol{g}(\boldsymbol{u})$ and of internal variables $\boldsymbol{\xi} \to \boldsymbol{f}_{\boldsymbol{u}}(\boldsymbol{\xi})$ (depending on $\boldsymbol{u}$), and a function $K(\boldsymbol{u})$, such that

$$
\phi_1(\boldsymbol{\xi}; \boldsymbol{u}) = \phi_2\bigl(\boldsymbol{f}_{\boldsymbol{u}}(\boldsymbol{\xi}); \boldsymbol{g}(\boldsymbol{u})\bigr) + K(\boldsymbol{u}), \qquad \boldsymbol{f}_{\boldsymbol{0}}(\boldsymbol{\xi}) = \boldsymbol{\xi}, \quad \boldsymbol{g}(\boldsymbol{0}) = \boldsymbol{0}.
\tag{10.4}
$$
An unfolding is *stable* if every nearby unfolding of the same germ is equivalent to it.

For example, $\phi = x^4 - ux^2$, whose two minima are always equally deep, is not stable: it is not equivalent to $x^4 - u(x^2 + \varepsilon x)$, whose minima are unequal. Stability is not a severe restriction: every unfolding can be approximated arbitrarily closely by a locally stable one, and every unfolding is obtained from a stable one by a transformation of the form (10.4) (though not necessarily an invertible one).

How is a stable unfolding determined by the degenerate germ? To first order in $\boldsymbol{u}$, $\phi(\boldsymbol{\xi}; \boldsymbol{u}) = \phi(\boldsymbol{\xi}) + \sum_\beta u_\beta b_\beta(\boldsymbol{\xi})$. A nearby unfolding has the form $\phi(\boldsymbol{\xi}) + \sum_\beta u_\beta\bigl[b_\beta(\boldsymbol{\xi}) + f_\beta(\boldsymbol{\xi})\bigr]$ with arbitrary small $f_\beta$ (with $f_\beta(\boldsymbol{0}) = 0$, up to equivalence). The infinitesimal transformations $\xi_\alpha \to \xi_\alpha + \sum_\beta a_{\alpha\beta}(\boldsymbol{\xi})u_\beta$ and $u_\alpha \to u_\alpha + \sum_\beta\lambda_{\alpha\beta}u_\beta$ change $\phi$ by $\sum_{\alpha\beta}u_\beta\bigl[a_{\alpha\beta}\,\partial\phi/\partial\xi_\alpha + \lambda_{\alpha\beta}b_\alpha\bigr]$. Equivalence requires that, for each $\beta$, the equation

$$
f(\boldsymbol{\xi}) = \sum_\alpha a_\alpha(\boldsymbol{\xi})\frac{\partial\phi}{\partial\xi_\alpha} + \sum_\alpha\lambda_\alpha b_\alpha(\boldsymbol{\xi})
$$
be solvable for arbitrary $f$ vanishing at $\boldsymbol{0}$. In other words:

**Theorem 10.5.1 (Infinitesimal Stability)** The unfolding $\phi + \sum_\alpha u_\alpha b_\alpha$ is stable (for $\boldsymbol{u}$ in a neighbourhood of $\boldsymbol{0}$) if and only if

$$
\operatorname{lin}\{b_\alpha\} + \operatorname{id}\Bigl\{\frac{\partial\phi}{\partial\xi_\alpha}\Bigr\} = C^\infty(\boldsymbol{\xi})_0,
$$
where $C^\infty(\boldsymbol{\xi})_0$ is the space of smooth germs vanishing at $\boldsymbol{0}$, $\operatorname{id}\{\partial\phi/\partial\xi_\alpha\}$ the **ideal** of all functions $\sum_\alpha a_\alpha(\boldsymbol{\xi})\,\partial\phi/\partial\xi_\alpha$ (the Jacobian ideal), and $\operatorname{lin}$ the linear span.

That the infinitesimal condition suffices for finite $\boldsymbol{u}$ is shown by iteration: differentiating a candidate equivalence $\phi_1(\boldsymbol{\xi}; \boldsymbol{u}) = \phi(\boldsymbol{f}(\boldsymbol{\xi}, \boldsymbol{u})) + \sum_\alpha g_\alpha(\boldsymbol{u})b_\alpha(\boldsymbol{f}) + K(\boldsymbol{u})$ with respect to $u_\beta$ gives, at $\boldsymbol{u} = \boldsymbol{0}$, equations for $\partial\boldsymbol{f}/\partial\boldsymbol{u}$, $\partial\boldsymbol{g}/\partial\boldsymbol{u}$ and $\partial K/\partial\boldsymbol{u}$ that are solvable by the theorem, with $\partial g_\alpha/\partial u_\beta \approx \delta_{\alpha\beta}$ (so $\boldsymbol{g}$ and $\boldsymbol{f}$ are invertible); for $\boldsymbol{u} \ne \boldsymbol{0}$ the remaining terms are treated as perturbations and the solution is continued. The region of validity may shrink to zero for an infinite system of equations, so a finite codimension (below) is required.

**Definition 10.5.2 (Codimension and Universal Unfolding)** The **codimension** of a germ $\phi$ is the dimension of the quotient space $C^\infty(\boldsymbol{\xi})_0/\operatorname{id}\{\partial\phi/\partial\xi_\alpha\}$, i.e. of what remains of the function space after multiples of the partial derivatives are removed. It is also the smallest number of control parameters of a stable unfolding; a stable unfolding with exactly this number of parameters is a **universal unfolding**, obtained by taking for the $b_\alpha$ a basis of a complement of the Jacobian ideal.

**Example 10.5.1** One variable, $\phi = x^m$, degenerate for $m \ge 3$. The ideal $\operatorname{id}\{mx^{m-1}\}$ consists of all $x^{m-1}\psi(x)$; a complement among functions vanishing at $0$ is $\operatorname{lin}\{x, x^2, \dots, x^{m-2}\}$. Hence the universal unfolding is $x^m + \sum_{j=1}^{m-2}u_jx^j$ and $\operatorname{codim}x^m = m - 2$.

**Example 10.5.2** Two variables, $\phi = x^4 + y^4$: the ideal $\operatorname{id}\{x^3, y^3\}$ contains every monomial $x^iy^j$ with $i \ge 3$ or $j \ge 3$, so the complement is spanned by the $x^iy^j$ with $i, j \le 2$, $i + j \ne 0$: $x, y, x^2, xy, y^2, x^2y, xy^2, x^2y^2$; $\operatorname{codim} = 8$. Simplicity of the germ does not guarantee a simple unfolding: for $\phi = x^2y$, $\operatorname{id}\{2xy, x^2\}$ contains all monomials divisible by $xy$ or $x^2$, leaving $x$ and all powers $y, y^2, y^3, \dots$; the codimension is infinite. Three variables, $\phi = x^3 + y^3 + z^3$ (the lowest-order germ with corank 3, since all second-order terms are absent): the complement is spanned by $x^iy^jz^k$ with $i, j, k \le 1$, not all zero; $\operatorname{codim} = 7$.

**Proposition 10.5.2 (Few Essential Variables)** A germ of corank $n$ (starting at third order in $n$ variables) has $\operatorname{codim}\phi \ge \binom{n+1}{2}$. Hence germs with codimension at most 4, the case relevant when the controls are space and time, have corank $n \le 2$.

**Proof** Consider the polynomials of degree 1 and 2: there are $n + \binom{n+1}{2}$ monomials. The partial derivatives of $\phi$ start at degree 2, so modulo higher-order terms the Jacobian ideal contains at most the $n$ quadratic parts of the $\partial\phi/\partial\xi_\alpha$ in this range. The complement therefore has dimension at least $n + \binom{n+1}{2} - n = \binom{n+1}{2}$. For $n = 3$ this is 6 > 4. $\square$

## 10.6. Singular, Degenerate and Catastrophe Sets; the Cuspoids

The qualitative character of an unfolded singularity changes whenever a degenerate critical point recurs. For an unfolding $E(\boldsymbol{q}; \boldsymbol{u})$ define

- the *singular set* $\Sigma = \{(\boldsymbol{q}, \boldsymbol{u}) : \partial E/\partial q_\alpha = 0 \text{ for all } \alpha\}$, the equilibrium manifold;
- the *degenerate set* $\Delta = \{(\boldsymbol{q}, \boldsymbol{u}) \in \Sigma : \det(\partial^2E/\partial q_\alpha\partial q_\beta) = 0\}$;
- the *catastrophe set* (bifurcation set) $D = \{\boldsymbol{u} : (\boldsymbol{q}, \boldsymbol{u}) \in \Delta \text{ for some } \boldsymbol{q}\}$, the projection of $\Delta$ onto control space: the set of controls at which local nondegeneracy fails.

For one essential variable these sets are computed directly (Figure 2).

**Definition 10.6.1 (Fold, Cusp, Swallowtail and Butterfly Catastrophes)** The *cuspoid* catastrophes are the universal unfoldings of $x^m$, written with convenient coefficients: the **fold catastrophe** $x^3 + 3ux$ ($m = 3$), the **cusp catastrophe** $x^4 + 6ux^2 + 4vx$ ($m = 4$), the **swallowtail catastrophe** $x^5 + 10ux^3 + 10vx^2 + 5wx$ ($m = 5$) and the **butterfly catastrophe** $x^6 + 15tx^4 + 20ux^3 + 15vx^2 + 5wx$ ($m = 6$); in general $x^m + \sum_{p=1}^{m-2}\binom{m}{p}u_px^p$.

For the fold, $\phi = x^3 + 3ux$: $\Sigma$ is $x^2 + u = 0$, i.e. $\{(x, -x^2)\}$; $\Delta$ is $x = u = 0$; $D = \{0\}$. Two critical points (a minimum and a maximum) exist for $u < 0$, none for $u > 0$.

For the cusp, $\phi = x^4 + 6ux^2 + 4vx$: $\Sigma$ is $x^3 + 3ux + v = 0$, i.e. $\{(x, u, -x^3 - 3ux)\}$; adding $x^2 + u = 0$ gives $\Delta = \{(x, -x^2, 2x^3)\}$ and the catastrophe set $\{(-x^2, 2x^3)\}$, that is

$$
v^2 + 4u^3 = 0.
\tag{10.5}
$$
There are three critical points (two minima and a maximum) for $v^2 + 4u^3 < 0$ and one outside. Over the control plane the equilibrium surface is pleated (Figure 3): along the fold lines the middle unstable sheet meets the stable ones, and their projection is the cusp curve.

For the swallowtail, $\phi = x^5 + 10ux^3 + 10vx^2 + 5wx$: $\Sigma$ is $x^4 + 6ux^2 + 4vx + w = 0$; the degenerate set adds $x^3 + 3ux + v = 0$, so $D$ is parametrized by $(u, x) \mapsto (u, v, w) = (u, -x^3 - 3ux, 3x^4 + 6ux^2)$. Non-parametrically, $D$ is where the quartic $x^4 + 6ux^2 + 4vx + w$ has a double root, the zero set of its **discriminant** (computed as the resultant of the quartic and its derivative by Sylvester's elimination):

$$
27v^4 + 54u^3v^2 - 54uv^2w - 81u^4w + 18u^2w^2 - w^3 = 0.
$$
In the section $u < 0$ the curve has two cusps and a self-intersection, the "swallowtail" (Figure 4A); within its tail the quartic has four real roots (two minima), outside two.

For general $m$, the singular set is $x^{m-1} + \sum_p\binom{m-1}{p-1}u_px^{p-1} = 0$ and the degenerate set adds its derivative; the catastrophe set is the zero set of the discriminant $\prod_{i<j}(\alpha_i - \alpha_j)^2$ of the roots $\alpha_1, \dots, \alpha_{m-1}$ of the singular set, which vanishes when two roots coincide. Each pair of complex roots changes the sign of the discriminant; higher coincidences give lower catastrophes inside higher ones (the cusp $w = 0$ inside the swallowtail).

![The fold and the cusp. A: the fold family x³ + 3ux: a minimum and a maximum exist for u < 0, merge at u = 0 and vanish for u > 0. B: the cusp family x⁴ + 6ux² + 4vx at u = −0.5: two minima for |v| < 2(−u)^(3/2) ≈ 0.71, one minimum outside. C: equilibria of the cusp at u = −0.5 against v (solid stable, dashed unstable): the S-shaped curve folds back at v = ±0.71; arrows mark the jumps of perfect delay, the dotted line the Maxwell switch at v = 0. D: the catastrophe set v² + 4u³ = 0 in the control plane: three critical points inside, one outside; dotted, the Maxwell set v = 0, u < 0](./plots/fold-cusp.py)

![The equilibrium surface of the cusp catastrophe, x³ + 3ux + v = 0, over the control plane (u, v). Light: the stable sheets (minima); dark: the unstable middle sheet (maxima); black: the fold lines x² = −u, v = 2x³, whose projection onto the floor is the cusp v² + 4u³ = 0 (red). A path at fixed u = −0.6 with increasing v (red) stays on the upper sheet until the fold and then jumps to the lower sheet (dashed): hysteresis](./plots/cusp-surface.py)

## 10.7. Finite Determinacy and the Seven Elementary Catastrophes

To classify catastrophes one must classify germs up to equivalence: $\phi_1 \approx \phi_2$ if $\phi_1(\boldsymbol{\xi}) = \phi_2(\boldsymbol{f}(\boldsymbol{\xi})) + K$ for a smooth invertible $\boldsymbol{f}$ and a constant $K$. Since $\partial\phi_1/\partial\xi_\alpha = \sum_\beta(\partial f_\beta/\partial\xi_\alpha)\,\partial\phi_2/\partial f_\beta$, equivalent germs have Jacobian ideals related by the coordinate change, and hence equivalent unfoldings. A germ is *$k$-determined* if every germ with the same Taylor series through order $k$ is equivalent to it.

**Theorem 10.7.1 (Mather)** A germ is finitely determined if and only if it has finite codimension; if the codimension is $r$, it is $k$-determined for some $k \le r + 2$. Moreover, if $M^k$, the set of germs whose Taylor series start at order $k$, is contained in $M\cdot\operatorname{id}\{\partial\phi/\partial\xi_\alpha\} = \operatorname{id}\{\xi_\beta\,\partial\phi/\partial\xi_\alpha\}$, then $\phi$ is $k$-determined.

**Example 10.7.1** For $\phi = x^3 + xy^2$, $\operatorname{id}\{\xi_\beta\,\partial\phi/\partial\xi_\alpha\}$ is generated by $x(3x^2 + y^2)$, $y(3x^2 + y^2)$, $x(2xy)$, $y(2xy)$, which span all cubic monomials $x^3, x^2y, xy^2, y^3$; so it contains $M^3$ and $\phi$ is 3-determined: no higher-order terms can change its type.

In one variable the theorem is transparent. Write $\phi = x^m + h(x)$ with $h$ starting at order $m + 1$. If $\phi_1 = x^m + \ell(x)$ is another such germ, try $\phi(x(1 + p(x))) = \phi_1(x)$: this is $mp + \binom m2p^2 + \cdots = x^{-m}\bigl[\ell(x) - h(x + xp(x))\bigr]$, which can be solved for $p$ near $0$ by the implicit function theorem. So $x^m$ is $m$-determined and equivalent to any series starting at $x^m$ (and indeed $\operatorname{id}\{x\,\partial\phi/\partial x\} = \operatorname{id}\{x^m\} = M^m$). With Mather's theorem the classification for codimension at most 4 is finite: only germs in one or two essential variables (Proposition 10.5.2), and only Taylor terms of degree 3 to 6.

One variable gives $x^3, x^4, x^5, x^6$ (codimension 1 to 4). Two variables: there must be cubic terms, since a germ starting at order 4 would leave $x, y, x^2, xy, y^2, x^3, x^2y, xy^2, y^3$ to be spanned by only two derivative directions, codimension $\ge 7$. The dominant terms can be found with the Newton polygon (plotting the exponents $(p, q)$ of the monomials present and keeping those on the lower-left boundary); here they lie on the line $p + q = 3$. A binary cubic factors into three linear factors with at least one real root, giving four cases:

1. three distinct real roots: after a linear change, $x(x - y)(x + y) = x^3 - xy^2$;
2. a double and a simple real root: $x^2y$;
3. a triple root: $x^3$;
4. one real and two complex roots: $x(x + \mathrm{i}y)(x - \mathrm{i}y) = x^3 + xy^2$.

Cases 1 and 4 have codimension 3 and are 3-determined: the ideal $\operatorname{id}\{3x^2 \mp y^2, \pm2xy\}$ contains, through $xy$, all $x^py^q$ with $p, q > 0$, and with $x(3x^2 \mp y^2)$, $y(3x^2 \mp y^2)$ all monomials of degree $\ge 3$; the complement is spanned by $x$, $y$ and $x^2 + y^2$. Cases 2 and 3 have infinite codimension and must be completed by higher terms. For $x^3 + \phi_4$ the complement has dimension at least $2 + 3 + 4 - 4 = 5$, outside our range. For $x^2y + \phi_k$, $k \ge 4$, a coordinate shift removes every degree-$k$ term except $y^k$, leaving $x^2y + ay^k$ with complement $\operatorname{lin}\{x, y, y^2, \dots, y^{k-1}\}$; codimension 4 requires $k = 4$: $x^2y + y^4$.

**Definition 10.7.1 (Umbilic Catastrophes)** The *umbilic catastrophes* are the universal unfoldings of the corank-2 germs: the **hyperbolic umbilic** and the **elliptic umbilic**,

$$
\phi = \tfrac13\alpha x^3 + xy^2 + u(y^2 - \alpha x^2) + vx + wy, \qquad \alpha = +1 \text{ (hyperbolic)}, \ \alpha = -1 \text{ (elliptic)},
$$
of codimension 3, and the **parabolic umbilic** $\phi = x^2y + \frac14y^4 + tx^2 + uy^2 - vx - wy$, of codimension 4.

For the hyperbolic and elliptic umbilics, the singular set is $\alpha x^2 + y^2 - 2\alpha ux + v = 0$, $2y(x + u) + w = 0$; the Hessian $\begin{pmatrix}2\alpha(x - u) & 2y\\ 2y & 2(x + u)\end{pmatrix}$ has rank 0 only at $x = y = u = 0$, and rank 1 on $y^2 - \alpha x^2 = -\alpha u^2$. The catastrophe set, parametrized by $x$ at fixed $u$, is

$$
v = -\alpha x^2 - y^2 + 2\alpha ux, \qquad w = -2y(x + u), \qquad y^2 = \alpha(x^2 - u^2),
$$
a cone over the $(v, w)$ sections, which scale as $v, w \propto u^2$ (Figure 4B, C). A stable minimum requires a positive definite Hessian, $x + u > 0$ and $\alpha x^2 - y^2 > \alpha u^2$. The elliptic section is a curvilinear triangle with three cusps; the hyperbolic one a cusp facing a fold line. For the parabolic umbilic, the singular set gives $v = 2x(y + t)$, $w = x^2 + y^3 + 2uy$, the degenerate set $(y + t)(3y^2 + 2u) = 2x^2$, and the sections in $(v, w)$ change their connectivity at special values of $u/t^2$ (namely $0$, $-3/8$, $-3/2$ and $1/2$), with $u \propto t^2$, $v \propto t^{5/2}$, $w \propto t^3$.

**Theorem 10.7.2 (Thom's Classification)** A generic family of smooth functions depending on at most four control parameters has, at each point, a germ equivalent (up to the addition of a nondegenerate quadratic form in the remaining variables) to a Morse germ or to one of the seven elementary catastrophes:

| Catastrophe | Germ | Codimension | Corank |
|---|---|---|---|
| fold | $x^3$ | 1 | 1 |
| cusp | $x^4$ | 2 | 1 |
| swallowtail | $x^5$ | 3 | 1 |
| butterfly | $x^6$ | 4 | 1 |
| hyperbolic umbilic | $x^3 + y^3 \sim x^3 + xy^2$ | 3 | 2 |
| elliptic umbilic | $x^3 - 3xy^2 \sim x^3 - xy^2$ | 3 | 2 |
| parabolic umbilic | $x^2y + y^4$ | 4 | 2 |

For five controls there are four more (eleven in all); from codimension 6 on, continuous families (moduli) appear and the classification is no longer a finite list. (The labels "hyperbolic" and "elliptic" follow the cubic's roots: one real root for the hyperbolic umbilic, three for the elliptic one.)

What is the biological relevance? A developmental sequence that is regularly observed is by definition unaffected by small internal and external perturbations. If the relevant differentiability conditions hold, it therefore corresponds to a stable unfolding in space-time, and for at most four control dimensions there are only finitely many possibilities. For a single organism higher codimensions are neither needed nor allowed; for comparisons between species or phyla, where more parameters vary, higher codimensions become unavoidable, and with them both the infinity of types and "strange" unfoldings not close to stable ones.

![Sections of catastrophe sets. A: swallowtail, section u = −1 in the (v, w) plane: two cusps and a self-intersection; inside the tail the potential has two minima. B: hyperbolic umbilic (α = 1), section u = 1: a cusp facing a fold line. C: elliptic umbilic (α = −1), section u = 1: a curvilinear triangle with three cusps. D: the bilaterally symmetric unfolding of Eq. (10.7) with α = 1, β = 0.2 and γ = 0.05 (solid) or 0.2 (dashed): four-cusped figures in the (u, v) plane, symmetric under v → −v](./plots/control-sections.py)

## 10.8. Constraints and the Choice of Control Space

The theory assumes that internal variables range freely over an open set. This is not true of concentrations (which are positive) or of the variable $R^2$ in the blastocoel model of 7.5.5, which must be nonnegative. There, $E \propto (R^2)^2 - (\gamma V/J)R^2$ can be transformed to have no control parameter at all (codimension 0) as long as $\gamma V/J > 0$; but if $\gamma V/J < 0$ the minimum leaves the admissible range $R^2 \ge 0$, an event that unconstrained theory does not see. Allowing inequality constraints enlarges the classification substantially (boundary singularities), and the number of inequivalent stable unfoldings becomes infinite for codimension above 3. The point matters whenever a true constraint (such as $\sigma \le 1$ for an occupation fraction) is replaced in a model by a merely high energy barrier. A similar warning applies to control space: space and time cannot reasonably be mixed in forming equivalence classes, since a smooth change of coordinates that mixes them has no physical meaning; the classification must respect the distinction (and there are real asymmetries between space and time, below).

## 10.9. Which Minimum? Maxwell and Perfect-Delay Conventions

The quasi-static picture says that the state sits in a minimum, but there may be several. Two extreme rules are possible.

**Definition 10.9.1 (Maxwell Convention)** Under the **Maxwell convention** the system always occupies the global minimum of $E$ (the Gibbs criterion of thermodynamic equilibrium, appropriate if large fluctuations let the system sample all configurations of lower energy before it equilibrates). Jumps then occur on the *Maxwell set*, the control values at which two minima are equally deep, in addition to the primary catastrophes where a minimum disappears.

**Definition 10.9.2 (Perfect-Delay Convention)** Under the **perfect-delay convention** the system stays in its current local minimum, following it as the controls change, until that minimum ceases to exist at the catastrophe set; only then does it jump to another minimum.

Since only minima matter, the overall sign of $\phi$ is now significant and unfoldings that can reach $-\infty$ are excluded: among the cuspoids only the cusp and the butterfly qualify. For the cusp, by the symmetry $x \to -x$, $v \to -v$, the Maxwell set is evidently $v = 0$, $u < 0$. For the butterfly $x^6 + 15tx^4 + 20ux^3 + 15vx^2 + 5wx$ one must solve $\bigl(\phi(x) - \phi(y)\bigr)/(x - y) = 0$, $\phi'(x) = \phi'(y) = 0$ for two equal minima; the line $u = w = 0$ belongs to the Maxwell set, but only as the intersection of several surfaces.

Perfect delay produces **hysteresis** (Figure 2C, Figure 3): the jump up and the jump down occur at different control values, and the state depends on history, a form of memory like that of bistable signalling switches ([7.3.18](/7.3.18)). Thom considered perfect delay much closer to biological reality than the Maxwell rule; the truth must lie in between and depends on the time scales. If the controls change slowly compared with the time needed to cross the barrier between minima, the system can find the deeper minimum (Maxwell); if they change quickly, or the barrier is high compared with fluctuations, it stays where it is (delay). Figure 5 shows the transition in a simulation of noisy gradient dynamics: as noise increases, the switching point moves from the fold towards the Maxwell point. (A finite sweep rate also delays the deterministic jump slightly beyond the fold.)

![Which minimum does the system occupy? Overdamped noisy dynamics in the cusp potential at u = −0.5, dx = −φ′(x)dt + √(2D) dW, with the control v swept slowly up and down. A: state against control for noise D = 0 (perfect delay: jumps only where the occupied minimum disappears, near the folds v = ±0.71), D = 0.1 and D = 0.3 (the hysteresis loop narrows). B: mean value of v at which the state switches on the upward sweep, against noise: it moves from the perfect-delay value towards the Maxwell value v = 0, where the two minima are equally deep](./plots/delay-maxwell.py)

The simplest dynamical model with an asymmetry between space and time is the relaxation-time model: if $\boldsymbol{\xi}^0(\boldsymbol{r}, t)$ is the minimizing state at $(\boldsymbol{r}, t)$, the actual state follows it with time constant $\tau$,

$$
\frac{\partial\boldsymbol{\xi}}{\partial t} = \frac1\tau\bigl(\boldsymbol{\xi}^0(\boldsymbol{r}, t) - \boldsymbol{\xi}(\boldsymbol{r}, t)\bigr),
$$
homing in exponentially, $\boldsymbol{\xi} = \boldsymbol{\xi}^0 + \Delta\,\mathrm{e}^{-t/\tau}$, if $\boldsymbol{\xi}^0$ is fixed, and lagging behind if it moves. With several attractors $\boldsymbol{\xi}^\lambda$ the most direct representation is $\partial_t\boldsymbol{\xi} = \tau^{-1}\sum_\lambda w_\lambda(\boldsymbol{\xi}^\lambda - \boldsymbol{\xi})$ with weights $w_\lambda$. The weights need not be mysterious: the gradient dynamics (10.1) reduces near a minimum to $\dot\xi_\alpha = -\kappa\sum_\beta(\partial^2E/\partial\xi_\alpha\partial\xi_\beta)(\xi_\beta - \xi^0_\beta)$, a relaxation model with the Hessian as rate matrix, and away from minima it automatically weighs the competing attractors, though not in the linear form above.

## 10.10. Symmetry-Constrained Unfoldings

A compendium of local analyses says nothing about the relations between singularities at different places, and some of these relations are easy to add: those due to symmetry. A **blastula** is basically a sphere, so its intrinsic description should be radially symmetric and stability of an unfolding should be required only under radially symmetric perturbations; a **gastrula** has an underlying bilateral symmetry. If an unfolding is invariant under a group $G = \{g\}$ acting on control space, then $\phi(\boldsymbol{\xi}; g\boldsymbol{u})$ can be returned to $\phi(\boldsymbol{\xi}; \boldsymbol{u})$ by an outwardly invisible change of internal coordinates: $\phi(\hat g\boldsymbol{\xi}; g\boldsymbol{u}) = \phi(\boldsymbol{\xi}; \boldsymbol{u})$, where $\hat G = \{\hat g\}$ is a representation of $G$ on internal space induced by the symmetry. It restricts the possible unfoldings.

**Example 10.10.1** The germ $x^4 + y^4$ unfolds universally to $x^4 + y^4 + \operatorname{lin}\{x, y, x^2, xy, y^2, x^2y, xy^2, x^2y^2\}$ (Example 10.5.2). Suppose bilateral symmetry requires invariance under $v \to -v$, where $v$ is the coefficient of $y$. Since $v \to -v$ must be compensated by $y \to -y$, the remaining terms must be even in $y$. If one further allows equivalence under continuous rather than smooth transformations (a step that weakens the theory and is not justified here), the $x^2y^2$ term can also be dropped, and Percus and Childress arrive at

$$
\phi = \alpha\bigl(x^4 - 6x^2y^2 + y^4\bigr) + \beta\bigl(3xy^2 - x^3\bigr) + \gamma\bigl(x^2 + y^2\bigr) + ux + vy.
\tag{10.7}
$$

## 10.11. Catastrophe Models of Early Development

How can one infer mechanism from qualitative observations? An observed boundary between two regimes admits two extreme interpretations: a primary catastrophe, where a minimum simply disappears, or a secondary one, where the system jumps to a new lower minimum (the Maxwell set), or something in between. Percus and Childress illustrate the reasoning on examples of increasing codimension. These are descriptive models; they are included as examples of method, not as established mechanisms.

**Example 10.11.1 (Late Blastulation as a Fold)** Model late blastulation as the passage of a wave of cell formation (non-cell → cell) through a locally homogeneous milieu, with the single control $x - ct$. The fold

$$
E(V; x, t) = V^3 + 3aV(ct - x)
$$
has the minimizing state $V^0 = \bigl(a(x - ct)\bigr)^{1/2}$ behind the front ($x > ct$) and no minimum ahead of it, as required by perfect delay if $V$ measures cell occupation. Can this local behaviour be produced by a global energy with space-independent adhesion, $\mathcal{E} = \int\bigl[\frac J2V'^2 + \mathcal{V}(V)\bigr]\mathrm{d}x$? Its minimizer satisfies $JV'' = \mathcal{V}'(V)$. For the structure to be set only by boundary conditions, $\mathcal{V}$ must not depend on $x - ct$; substituting $V^0$, $V^{0\prime\prime} = -\frac{a^2}{4}\bigl(a(x - ct)\bigr)^{-3/2} = -a^2/(4V^3)$, so

$$
\mathcal{V}'(V) = -\frac{a^2J}{4V^3}, \qquad \mathcal{V}(V) = \frac{a^2J}{8V^2}.
$$
An energy that favours the non-cell → cell transition in this special way reproduces the local behaviour. Inserting a monotonic relation $V = f(\nu)$ to an effective cell density $\nu$ and comparing with the "thermal" and adhesive energies of the blastocoel model of 7.5.5, both symmetric about $\nu = \frac12$, shows that an antisymmetric component is needed: a cell-number conservation energy $\lambda\bigl(\int\nu\,\mathrm{d}x - N\bigr)$ with $\lambda < 0$. The control $x - ct$ must enter at the outer boundary, say through $V(ct + d) = V_M$, together with the conservation condition $\int_{ct}^{ct+d}V\,\mathrm{d}x = 2V_M^3/(3a)$, which indeed reproduces $V^0$ (since $\int_0^d(as)^{1/2}\,\mathrm{d}s = \frac23a^{1/2}d^{3/2}$ and $V_M = (ad)^{1/2}$).

**Example 10.11.2 (The Spherical Blastula as a Cusp)** Taking $r$ and $t$ as controls (no symmetry problem, but the restricted range $r \ge 0$), the fold must be generalized to a cusp and perfect delay perhaps to a Maxwell rule: the cubic of Example 10.11.1 is raised to a quartic that reduces to it in the old region. Raising the degree is easy with the **Lagrange interpolation polynomial**: if $\phi_{N-1}$ takes values $a_i$ at $N$ points $x_i$, appending a new zero at $x_0$ gives $\phi_N(x) = \sum_ia_i\frac{x - x_0}{x_i - x_0}\prod_{j\ne i}\frac{x - x_j}{x_i - x_j}$, which for large $-x_0$ is approximately $\phi_{N-1}(x)(x - x_0)/(-x_0)$. What model produces this? The observed radial structure of the blastula wall is approximated by $\partial V/\partial r = aV(1 - V)$, slow variation near $V = 0$ and $V = 1$. If the energy density is a surface term plus a bulk term and the polynomial is to be quartic, one is virtually driven to the surface term $\frac J2\lvert\nabla V\rvert^2$, and along the profile $\frac J2\lvert\nabla V\rvert^2 = \frac{Ja^2}{2}V^2(1 - V)^2$, a double well with two minima or one depending on $a$ and the bulk term. But the system is not homogeneous, and $a$, at first closely tied to time, becomes an internal variable determined by minimizing

$$
\mathcal{E} = 4\pi\int_0^{R(t)}\Bigl[\frac{J(t)}{2}a^2V^2(1 - V)^2 + \mathcal{V}(V)\Bigr]r^2\,\mathrm{d}r
$$
over $a$ and the integration constant $K$ of the profile: from $a\,\mathrm{d}r = \mathrm{d}V/\bigl(V(1 - V)\bigr)$, $ar + \ln K = \ln\frac{V}{1 - V}$, so

$$
V(r) = \frac{K\mathrm{e}^{ar}}{1 + K\mathrm{e}^{ar}},
$$
the logistic profile. Converting an initially spatially or temporally controlled parameter into a neutral internal variable sets the stage for a new control variable; this is the hierarchical step of the catastrophe description.

**Example 10.11.3 (Gastrulation as a Hyperbolic Umbilic)** The non-mammalian blastula is essentially a thin sheet of cells, a sphere with distorted thickness scale. A characteristic **invagination** occurs in the vegetal half, emanating from a region of newly differentiated cells. Descriptively, the abrupt spread over the surface of a point of activation, needing the two controls $r$ and $t$, is most directly represented by the penetration of a stable minimum in a hyperbolic umbilic,

$$
\tfrac13x^3 + xy^2 + u(y^2 - x^2) + vx + wy.
$$
If this is believed, two internal variables are required: for example the densities of two cell types produced earlier by another process, or the balance of two biochemicals. It is a prediction of the description, not derived from it, that the mechanism has two essential variables; how amphibian gastrulation is actually driven (**bottle cells**, **involution**, **convergent extension**) is the subject of 7.5.9.

**Example 10.11.4 (Fivefold Symmetry)** The early bilateral symmetry of the gastrula is often followed by a more or less vague fivefold pattern (head and four limbs of a vertebrate, the arms of a starfish). Percus and Childress suggest that the bilateral unfolding (10.7) yields a catastrophe of this form in the $(u, v)$ plane at small $\gamma$, requiring only two internal variables. A direct computation of its bifurcation set (Figure 4D) gives curvilinear figures with four cusps for the parameter values shown (and three or six in other ranges) but no fivefold pattern, so the suggestion should be regarded as speculative. Pentaradial symmetry of echinoderms is in any case a derived trait of an adult body plan with a well-studied genetic basis, not a property of the early gastrula.

## 10.12. Dynamics at Different Resolutions

Gradient-flow dynamics $\dot x_i = -\partial E/\partial x_i(\boldsymbol{x}, \boldsymbol{a})$ can contain much detail through the complexity of $E$, but phenomenology is usually qualitative before it is quantitative. Catastrophe theory is one qualitative format; another concentrates on logical form.

### 10.12.1. Low Resolution: Boolean Dynamics

Let $x_i = 0$ mean "off" and $x_i = 1$ "on", time be an integer, and study the transition sequence of the Boolean vector $\boldsymbol{x}$: a **Boolean network** ([1.3.4](/1.3.4)). Even the predator–prey equations of Lotka and Volterra, $\dot a = a(h - h_0)$, $\dot h = h(a_0 - a)$ ($a$ predators, $h$ prey), which conserve $K = h + a - h_0\ln h - a_0\ln a$ and have an unstable steady state $(0, 0)$, a neutrally stable one $(a_0, h_0)$ and a family of closed orbits, have a slim roster of behaviours. A minimal discrete version sets $a = 0$ if small, $1$ if large, takes $(a_0, h_0) = (\frac12, \frac12)$ as the reference and lets each variable follow the sign of its derivative: $a(t + 1) = 1$ if $\dot a > 0$, $0$ if $\dot a < 0$. Since $\dot a = 0$ and $\dot h = 0$ are marginal at the Boolean values, replace the equations by

$$
\dot a = (a + \varepsilon)\bigl(h - \tfrac12\bigr), \qquad \dot h = (h + \varepsilon)\bigl(\tfrac12 - a\bigr).
$$
The four states then map as $00 \to 01 \to 11 \to 10 \to 00$: the logical equations $a' = h$, $h' = \bar a$ (with a prime for the next state and a bar for negation), a single 4-cycle, the Boolean counterpart of the closed orbits (Figure 7A). The only conserved quantity is the trivial $a(1 - a) + h(1 - h)$. The $\varepsilon$-modification is not unique: with $\dot h = (h - \varepsilon)(\frac12 - a)$ instead, one gets $a' = h$, $h' = a\oplus h$ (exclusive or: $h' = a\bar h + \bar ah$), in which $00$ is a fixed point and the other three states form a 3-cycle, with the nontrivial conserved quantity $\bar a\bar h$. The fixed point $00$ is recognizably unstable because it disappears under a change of $\varepsilon$.

Discretizing space as well turns partial differential equations into cellular automata. For pure diffusion on a unit grid, $\dot a_n \propto a_{n+1} - 2a_n + a_{n-1}$, with the rule that $a_n$ is unchanged when $\dot a_n = 0$, the eight-entry table of $a'_n$ against $(a_{n-1}, a_n, a_{n+1})$ is the Boolean function

$$
a'_n = a_{n-1}a_na_{n+1} + \bar a_n\bigl(1 - \bar a_{n-1}\bar a_{n+1}\bigr),
$$
under which a block such as $0001111000$ evolves into $0010110100$, $0101001010$, $1010110101$: diffusion appears as a front moving one site per step with decreasing coarse-grained density (Figure 7B). Total content is not conserved and must be renormalized; a grey scale ($a = 0, 1, 2$) would capture more but contradicts the philosophy of the representation. Lindenmayer-type automata, used to model growth patterns, give more complex dynamics: in a formal model of a shoot apex, an apical growth region at one end keeps its form while leaving a changing pattern behind, generated by a next-state table such as "new state = state xor left neighbour" (Figure 7C), which produces the self-similar pattern of Pascal's triangle modulo 2; even for such simple rules, closed formulas for the state of a given cell at a given time are generally unknown.

![Low-resolution dynamics. A: Boolean versions of the Lotka–Volterra predator–prey system (a predator, h prey): with one ε-modification, a′ = h, h′ = not a, a single 4-cycle; with another, a′ = h, h′ = a xor h, a fixed point 00 (green) and a 3-cycle. B: diffusion as a cellular automaton, a′_n = a_{n−1}a_n a_{n+1} + not(a_n)(a_{n−1} or a_{n+1}), from a block of four occupied sites (time runs downwards): a front spreading one site per step with falling coarse-grained density. C: a Lindenmayer-type growing automaton, each new row the previous one with every cell replaced by (cell xor left neighbour) and a cell added at the right: the Sierpinski pattern of Pascal's triangle mod 2](./plots/boolean-automata.py)

### 10.12.2. Intermediate Resolution: Hill Functions and Piecewise-Linear Networks

The construction can be reversed: start from a logical structure that captures the phenomenology, then convert it into continuous dynamics that can be analysed quantitatively. Consider three species in which $a$ inhibits $b$, $b$ activates $c$ and $c$ inhibits $a$. Its symbolic dynamics, $a' = \bar c$, $b' = \bar a$, $c' = b$, has two steady states, $011$ and $100$, and two 3-cycles (Figure 6A). To make it continuous, replace the jumps $0 \mapsto 1$ and $1 \mapsto 0$ by sigmoidal Hill functions (the **Hill equation** of cooperative binding, [7.1](/7.1)),

$$
F^+_\lambda(x) = \frac{x^n}{\theta_\lambda^n + x^n}, \qquad F^-_\lambda(x) = \frac{\theta_\lambda^n}{\theta_\lambda^n + x^n},
$$
and add first-order decay, so that a species is driven towards 0 when not stimulated and towards its maximum when stimulated:

$$
\dot a = kF^-_a(c) - \alpha a, \qquad \dot b = k'F^-_b(a) - \beta b, \qquad \dot c = k''F^+_c(b) - \gamma c.
$$
In general a logical product or sum translates into a product or sum of Hill functions: $a' = a\cdot\bar b + c$ becomes $\dot a = kF^+(a)F^-(b) + k'F^+(c) - \alpha a$. Much more complex immunological and gene regulatory networks have been analysed in this way.

Comparing the two resolutions is instructive (Figure 6B). The continuous system has exactly two stable steady states, near $(1, 0, 0)$ and $(0, 1, 1)$: the loop contains two inhibitions and one activation, an even number of negative links, so it is a positive feedback loop, which can produce **bistability** but not oscillation (René Thomas's rule: a negative loop is necessary for sustained oscillation, a positive loop for multistability). The two 3-cycles of the Boolean map are artefacts of updating all genes simultaneously; with asynchronous updating (one gene at a time) they disappear. Choosing the update scheme is part of the modelling.

![A three-gene positive feedback loop at two resolutions (a ⊣ b → c ⊣ a). A: synchronous Boolean dynamics a′ = not c, b′ = not a, c′ = b on the eight states: two fixed points, 011 and 100 (green), and two 3-cycles. B: the Hill-function version (n = 4, threshold 0.5, unit decay rates) from twelve random initial states: time courses of a, and trajectories in the (a, c) plane; every trajectory ends in one of two stable steady states near the Boolean fixed points, and nothing corresponds to the Boolean 3-cycles](./plots/boolean-hill.py)

Continuous dynamics need not use continuous functions. In the piecewise-linear networks of Leon Glass and Kauffman, probably the simplest extension of state-transition dynamics, the amplitudes $x_i$ (relative concentrations, measured from their thresholds) have Boolean shadows $\tilde x_i = 0$ for $x_i < 0$ and $1$ for $x_i \ge 0$, and

$$
\frac{\mathrm{d}x_i}{\mathrm{d}t} = \Lambda_i(\tilde{\boldsymbol{x}}) - x_i,
$$
with $\Lambda_i$ a nonzero constant in each orthant, multilinear in the $\tilde x_j$ (since $\tilde x_j^2 = \tilde x_j$) and, for convenience, with sign independent of $\tilde x_i$ itself. Within an orthant the solution is explicit, $x_i(t) = \lambda_i + (c_i - \lambda_i)\mathrm{e}^{-t}$ with $x_i(0) = c_i$ and $\lambda_i = \Lambda_i(\tilde{\boldsymbol{c}})$: the trajectory heads straight for a focal point that lies in another orthant and changes direction when some $x_j$ crosses zero. The dynamics is thus a sequence of passages between orthant boundaries, and a cyclic sequence can be studied through its successive returns to one boundary (a Poincaré return map), which is how stable limit cycles and chaos have been found in such networks.

## 10.13. Assessment: Rise, Fall and Return

After Thom's *Structural Stability and Morphogenesis* (1972) there was intense interest in applying catastrophe theory across the biological and social sciences. In much of this work the models were poorly conceived, the formulations speculative and the conclusions unwarranted; critical surveys (Sussmann and Zahler 1978, among others) showed this in detail, and the theory came to be seen in some circles as irrelevant and overblown. This judgement concerned the applications, not the mathematics: as a technique for classifying robust geometric structure catastrophe theory has well-established uses, for example in the classification of the caustics of optics and of the asymptotics of oscillatory integrals. In development the applications in this chapter are minimal, and Percus and Childress included the material in the hope that the control parameters might one day be given biological meaning.

One application did leave a lasting mark: the **clock-and-wavefront model** of **somite** formation (Cooke and Zeeman 1976) was proposed in this framework, with the cusp catastrophe describing the abrupt transition of cells as a wavefront passes, and its components (a **segmentation clock** and a posterior-to-anterior wavefront) were later identified molecularly (7.5.23). And the geometric approach has returned in a sharper form. Corson and Siggia (2012) showed that the vulval cell fates of *C. elegans*, and their responses to combinations of signals and mutations, can be fitted by a landscape with three attractors and a small number of parameters, from which **epistasis** relations follow geometrically; later work classified the generic decision geometries of gradient-like (Morse–Smale) systems with few attractors and fitted such landscapes to the differentiation of mouse embryonic **stem cells** (Sáez et al. 2022). The common idea is the one of this chapter: if a decision is robust, it is described by a structurally stable family, and there are few such families. What has changed is that the landscape is now inferred quantitatively from data and tied to known signalling pathways, and that its limits are explicit: oscillators and other recurrent dynamics (Proposition 10.3.1) need different tools, and noise and the rate of change of signals decide where between delay and Maxwell a system switches.

## Summary

| Topic | Key results |
|---|---|
| Programme (10.1–10.2) | qualitative, stable description; catastrophe theory (Definition 10.1.1); quasi-static minimization, gradient flow (Eq. (10.1)) with $E$ a Lyapunov function; Waddington landscape |
| General flows (10.3) | Lagrangian $L = \sum\dot q_\alpha U_\alpha - U$ gives $\Gamma\dot{\boldsymbol{q}} = \nabla U$ (Eq. (10.3)), but $\Gamma$ is antisymmetric and $U$ conserved (Proposition 10.3.1, Example 10.3.1); gradient-like flows (Conley) |
| Morse theory (10.4) | Morse function (Definition 10.4.1): generic, stable (Theorem 10.4.1); splitting lemma: only the corank matters (Theorem 10.4.2) |
| Unfoldings (10.5) | unfolding, equivalence, stability (Definition 10.5.1, Eq. (10.4)); tangent condition $\operatorname{lin}\{b_\alpha\} + \operatorname{id}\{\partial\phi\} = C^\infty_0$ (Theorem 10.5.1); codimension, universal unfolding (Definition 10.5.2); $x^m$: codim $m - 2$; $x^4 + y^4$: 8; $x^2y$: ∞; $x^3 + y^3 + z^3$: 7 (Examples 10.5.1–10.5.2); codim $\ge \binom{n+1}{2}$ (Proposition 10.5.2) |
| Catastrophe sets (10.6) | singular, degenerate, catastrophe sets; fold, cusp $v^2 + 4u^3 = 0$ (Eq. (10.5)), swallowtail (discriminant), butterfly (Definition 10.6.1) |
| Classification (10.7) | Mather: finite determinacy ⇔ finite codimension, $k \le r + 2$ (Theorem 10.7.1, Example 10.7.1); binary cubics and Newton polygon; umbilics (Definition 10.7.1); Thom's seven (Theorem 10.7.2) |
| Constraints (10.8) | inequality constraints enlarge the classification; do not mix space and time |
| Conventions (10.9) | Maxwell (Definition 10.9.1; cusp: $v = 0$) vs perfect delay (Definition 10.9.2): **hysteresis**; noise and sweep rate interpolate; relaxation-time model |
| Symmetry (10.10) | induced representation; bilateral unfolding (Example 10.10.1, Eq. (10.7)) |
| Applications (10.11) | blastulation fold, $\mathcal{V} = a^2J/8V^2$ (Example 10.11.1); spherical blastula cusp, logistic wall profile (Example 10.11.2); gastrulation as hyperbolic umbilic, two essential variables (Example 10.11.3); fivefold symmetry not supported (Example 10.11.4) |
| Resolutions (10.12) | Boolean Lotka–Volterra (4-cycle; xor variant); diffusion automaton; Lindenmayer automata; Boolean → Hill functions; positive loop bistable, synchronous cycles artefacts; Glass piecewise-linear networks, Poincaré returns |
| Assessment (10.13) | overuse and criticism in the 1970s; lasting value as classification; clock-and-wavefront; modern geometric fate models (Corson–Siggia) |

## Questions

1. Show that the cusp $\phi = x^4 + 6ux^2 + 4vx$ has three critical points exactly when $v^2 + 4u^3 < 0$, and compute the control values at which the minimum near $x = 1$ disappears when $u = -1$ and $v$ increases from $0$.

   **Answer** Critical points solve $x^3 + 3ux + v = 0$. A cubic $x^3 + px + q$ has three real roots iff its discriminant $-4p^3 - 27q^2 > 0$; with $p = 3u$, $q = v$: $-108u^3 - 27v^2 > 0$, i.e. $v^2 + 4u^3 < 0$. At $u = -1$ the fold points are where $3x^2 + 3u = 0$, $x = \pm1$, with $v = -x^3 - 3ux = -x^3 + 3x$: at $x = 1$, $v = 2$. On the critical curve $v = 3x - x^3$, the right minimum ($x > 1$) moves towards $x = 1$ as $v$ increases from 0 and merges with the maximum at $x = 1$, $v = 2 = 2(-u)^{3/2}$, where it disappears; under perfect delay the state then jumps to the left minimum $x = -2$ (the other root of $x^3 - 3x + 2 = (x - 1)^2(x + 2)$).

2. Compute the codimension and a universal unfolding of $\phi = x^5$, and verify that the swallowtail catastrophe set contains a cusp-shaped curve in the plane $w = 0$.

   **Answer** $\operatorname{id}\{5x^4\}$ contains $x^4, x^5, \dots$; the complement is $\operatorname{lin}\{x, x^2, x^3\}$: codimension 3, universal unfolding $x^5 + u_3x^3 + u_2x^2 + u_1x$ (equivalently $x^5 + 10ux^3 + 10vx^2 + 5wx$). In the parametrization $(v, w) = (-x^3 - 3ux, 3x^4 + 6ux^2)$, $w = 0$ at $x = 0$ (any $u$, $v = 0$) and at $x^2 = -2u$ ($u < 0$), where $v = -x^3 - 3ux = -x(x^2 + 3u) = -xu$, so $v^2 = x^2u^2 = -2u^3$: the curve $v^2 + 2u^3 = 0$ in the plane $w = 0$, a cusp (the remark of 10.6 that lower catastrophes appear inside higher ones, here with rescaled coefficients).

3. For the germ $\phi = x^3 + y^3$, find the Jacobian ideal, its codimension and a universal unfolding, and show that it is equivalent to $x^3 + xy^2$ (one real root of the cubic form).

   **Answer** $\operatorname{id}\{3x^2, 3y^2\}$ contains every monomial divisible by $x^2$ or $y^2$; the complement among functions vanishing at $0$ is $\operatorname{lin}\{x, y, xy\}$, codimension 3, universal unfolding $x^3 + y^3 + wxy - ux - vy$ (the standard hyperbolic umbilic). $x^3 + y^3 = (x + y)(x^2 - xy + y^2)$ has one real linear factor and an irreducible quadratic factor, the same root type as $x(x^2 + y^2) = x^3 + xy^2$. Binary cubic forms with the same root type are related by a real linear change of variables (a real projective transformation can move the real root and the complex pair of roots of $P_3(x/y)$ to $0$ and $\pm\mathrm{i}$, as in the classification of 10.7), so the germs are equivalent, both 3-determined by Example 10.7.1.

4. Prove that the Maxwell set of the cusp is $v = 0$, $u < 0$.

   **Answer** Two minima exist only for $u < 0$ and $v^2 < -4u^3$. Under $x \to -x$, $\phi(x; u, v) = \phi(-x; u, -v)$, so at $v = 0$ the potential is even and the two minima $\pm\sqrt{-3u}$ are equally deep. For $v > 0$, the term $4vx$ lowers the left minimum ($x < 0$) relative to the right one, and for $v < 0$ the reverse; since $\partial\phi/\partial v = 4x$ at fixed $x$, by the envelope theorem $\mathrm{d}(\phi_{\mathrm{right}} - \phi_{\mathrm{left}})/\mathrm{d}v = 4(x_{\mathrm{right}} - x_{\mathrm{left}}) > 0$, so the difference changes sign only at $v = 0$.

5. In Example 10.11.1, check that $V^0 = (a(x - ct))^{1/2}$ minimizes the fold energy, and that it satisfies $JV'' = \mathcal{V}'(V)$ with $\mathcal{V} = a^2J/(8V^2)$. What does a negative $\mathcal{V}'$ mean physically?

   **Answer** $\partial E/\partial V = 3V^2 + 3a(ct - x) = 0$ gives $V^2 = a(x - ct)$; $\partial^2E/\partial V^2 = 6V > 0$ for the positive root, a minimum. Differentiating, $V' = a/(2V)$, $V'' = -aV'/(2V^2) = -a^2/(4V^3)$, and $\mathcal{V}'(V) = -2a^2J/(8V^3) = -a^2J/(4V^3) = JV''$. Negative $\mathcal{V}'$ means the bulk energy decreases as $V$ (cell occupation) increases: the medium favours conversion of non-cells into cells, the drive of the front, while the gradient term $\frac J2V'^2$ resists sharp profiles.

6. For the three-gene loop $a \dashv b \to c \dashv a$, list the states reached under asynchronous updating (one randomly chosen gene updated per step) from $000$, and explain why the synchronous 3-cycles disappear.

   **Answer** From $000$: updating $a$ gives $a = \bar c = 1$ → $100$ (a fixed point: $a = \bar c = 1$, $b = \bar a = 0$, $c = b = 0$, no gene changes); updating $b$ gives $b = \bar a = 1$ → $010$; updating $c$ leaves $c = b = 0$. From $010$: $a \to 1$ (→ $110$), $c \to 1$ (→ $011$, fixed point), $b$ stays. From $110$: $b \to \bar a = 0$ (→ $100$) or $c \to 1$ (→ $111$), and so on. Every asynchronous path eventually ends in $100$ or $011$; the synchronous 3-cycles require all genes to flip simultaneously in a coordinated way, which a single-gene update never does, so they are not attractors of the asynchronous dynamics. This agrees with the continuous Hill model (Figure 6B), which has only the two steady states.

7. Show that in the Hill-function model with equal thresholds $\theta$ and large $n$, the steady states approach the Boolean fixed points, and use the Jacobian to explain why the symmetric steady state is unstable.

   **Answer** As $n \to \infty$, $F^\pm$ become step functions at $\theta$; with unit production and decay, steady states have $a = F^-(c)$, $b = F^-(a)$, $c = F^+(b)$, so each variable is 0 or 1 away from the threshold: $(1, 0, 0)$ and $(0, 1, 1)$ are consistent (e.g. $c = 0 < \theta$ gives $a = 1$, $a = 1 > \theta$ gives $b = 0$, $b = 0$ gives $c = 0$). There is also a steady state with all variables at intermediate values near $\theta$. Linearizing there, the Jacobian is $J = -I + G$, where $G$ has entries $F^{-\prime}(c) < 0$ (in row $a$), $F^{-\prime}(a) < 0$ (row $b$), $F^{+\prime}(b) > 0$ (row $c$) arranged in a cycle. The eigenvalues of $G$ are the cube roots of the loop gain $g = F^{-\prime}F^{-\prime}F^{+\prime} > 0$ (positive loop); one of them is the real positive root $g^{1/3}$, so $J$ has the eigenvalue $g^{1/3} - 1 > 0$ when the loop gain exceeds 1, which holds for steep Hill functions: the intermediate state is a saddle and the system is bistable.

8. (Open question) Design an experiment that would distinguish between perfect delay and the Maxwell convention in a cell-fate switch driven by a signal, for example a **morphogen** concentration controlling a binary fate.

   **Answer** Vary the signal slowly up and then down in the same cells (in culture, with an inducible or optogenetic input) and record the fate marker in single cells over time. Under perfect delay, switching thresholds differ between the up and down sweeps (hysteresis), are sharp and independent of sweep rate (if slow); under Maxwell behaviour, both sweeps switch at the same threshold. Intermediate behaviour shows itself through sweep-rate dependence (slower sweeps narrow the loop) and through cell-to-cell variability of switching points (noise-driven barrier crossing, Figure 5). Additional tests: hold the signal at a value inside the hysteresis range and ask whether cells prepared in opposite states stay there (memory) or converge; perturb transiently (a pulse) to measure the barrier.

9. Explain why a gradient-flow (landscape) description cannot capture the segmentation clock, and what geometric object replaces the minimum.

   **Answer** Along a gradient flow $E$ decreases strictly except at equilibria, so no trajectory can return to its starting point: periodic orbits are impossible (Proposition 10.3.1 shows that even the Lagrangian construction produces only a conserved, not a decreasing, $U$). The segmentation clock is a sustained oscillation, a stable **limit cycle** ([2.4.11](/2.4.11#sec-11.6)), which is an attractor of a non-gradient flow; its onset is a Hopf bifurcation rather than a catastrophe of a potential. A landscape picture can describe the slow variable (the state of cells relative to the wavefront) but not the clock itself.

10. Using the Boolean diffusion rule, compute two further steps of the evolution of $0001111000$ beyond those given in the text (taking the sites outside the row to be 0), and comment on what is and is not diffusion-like about the result.

    **Answer** Starting from $1010110101$ (step 3) with zero boundaries: a site with value 0 becomes 1 if a neighbour is 1; a site with value 1 stays 1 only if both neighbours are 1. Step 4: position 1 (1, neighbours 0 and 0) → 0; position 2 (0, neighbours 1, 1) → 1; position 3 (1; 0, 0) → 0; position 4 (0; 1, 1) → 1; position 5 (1; 0, 1) → 0; position 6 (1; 1, 0) → 0; position 7 (0; 1, 1) → 1; position 8 (1; 0, 0) → 0; position 9 (0; 1, 1) → 1; position 10 (1; 0, 0) → 0: $0101001010$. Step 5 then gives $1010110101$ again: on a bounded row the pattern oscillates with period 2 (on an infinite line the front keeps spreading, Figure 7B). Diffusion-like: spreading at a finite rate and dilution of the coarse-grained density. Not diffusion-like: no conservation of content, period-2 oscillation instead of relaxation to a uniform state, and no dependence on a diffusion coefficient.
