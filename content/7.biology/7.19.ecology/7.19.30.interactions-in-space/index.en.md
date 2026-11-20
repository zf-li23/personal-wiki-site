---
title: "Interactions in Space: Spatial Competition, Pattern Formation and Turing Instability"
description: "Interacting species in continuous space. Lotka–Volterra competition with diffusion: a Lyapunov functional shows that diffusion does not change the outcome in a uniform environment; competitive invasion waves; in heterogeneous environments the slower disperser wins under symmetric competition (Dockery et al.), proved through the principal eigenvalue, weak competition can still exclude, and the evolution of slow and ideal free dispersal. Advection up resource gradients and advection-mediated coexistence. Turing instability: linear analysis, dispersion relation, the four conditions, critical diffusion ratio and wave number, discrete modes in a bounded habitat; the Schnakenberg system; why Lotka–Volterra and Rosenzweig–MacArthur predators cannot make Turing patterns and a predator–prey model that can. Self-organized ecosystem patterns: the Klausmeier model of banded vegetation analyzed completely, mussel beds, fairy circles, patterns as early warnings and as escape from tipping. Lattice models: the contact process, mean-field and pair approximations, and the importance of being discrete."
---

Earlier chapters followed one species through space: dispersal and metapopulations ([7.19.16](/7.19.16)), and spread, invasion and critical patch size in **reaction-diffusion equation** models ([7.19.17](/7.19.17)). This chapter adds a second species. Movement can change the outcome of an interaction in three ways. It can do nothing, if the environment is uniform and the interaction stable; it can change who wins, if the environment varies in space and the species move at different rates; and it can create spatial structure out of nothing, when diffusion destabilizes a uniform equilibrium, as Turing (1952) showed for morphogenesis. Section 30.1 treats competition with diffusion, Section 30.2 directed movement up resource gradients, Section 30.3 the Turing mechanism in ecological form, Section 30.4 the self-organized patterns of real ecosystems, above all banded vegetation in drylands, and Section 30.5 individual-based lattice models. The mathematics of the heat equation and of the linear Turing condition is in [2.5.7](/2.5.7#sec-7.5.2), and the developmental theory of self-organized patterns, with the Gierer–Meinhardt model and the nonlinear steady states, in [7.5.12](/7.5.12); here we derive what the ecological applications need and emphasize what is different in ecology: the sign structure of species interactions, the heterogeneity of the environment and the directed flow of water.

## 30.1. Competition in Space

### 30.1.1. A Uniform Environment

Let two competitors with densities $u(x, t)$ and $v(x, t)$ diffuse in a bounded habitat $\Omega \subset \mathbb{R}^n$ with an impermeable boundary (**Neumann boundary condition**, zero flux):

$$
u_t = d_1\Delta u + u(a_1 - b_1u - c_1v),\qquad v_t = d_2\Delta v + v(a_2 - b_2u - c_2v),\qquad \frac{\partial u}{\partial\boldsymbol{n}} = \frac{\partial v}{\partial\boldsymbol{n}} = 0\ \text{on}\ \partial\Omega .
\tag{30.1}
$$
Here $a_i$ are intrinsic growth rates, $b_1, c_2$ the intraspecific and $c_1, b_2$ the interspecific competition coefficients, as in the Lotka–Volterra competition model of [7.19.22](/7.19.22) written without the carrying capacities. Weak competition, the case of stable coexistence in the well-mixed model, corresponds to

$$
\frac{b_1}{b_2} > \frac{a_1}{a_2} > \frac{c_1}{c_2},
$$
under which the ordinary differential equations have a positive equilibrium $(u^*, v^*)$ that attracts all positive solutions. Does diffusion change this?

**Theorem 30.1.1 (Diffusion Does Not Destroy Coexistence)** Under weak competition every solution of (30.1) with nonnegative initial data that are not identically zero in either species converges to the constant state $(u^*, v^*)$, for all diffusion rates $d_1, d_2 > 0$.

**Proof** We sketch the key estimate. Let $\gamma_1 = b_2$, $\gamma_2 = c_1$ (positive weights) and

$$
V(u, v) = \gamma_1\Bigl(u - u^* - u^*\ln\frac{u}{u^*}\Bigr) + \gamma_2\Bigl(v - v^* - v^*\ln\frac{v}{v^*}\Bigr),
$$
the **Lyapunov function** of the ordinary differential equations (Proposition 22.4.1 of [7.19.22](/7.19.22)). With $f = a_1 - b_1u - c_1v = -b_1(u - u^*) - c_1(v - v^*)$ and similarly $g$, its derivative along the reaction terms is

$$
\gamma_1(u - u^*)f + \gamma_2(v - v^*)g = -\bigl[\gamma_1b_1(u - u^*)^2 + (\gamma_1c_1 + \gamma_2b_2)(u - u^*)(v - v^*) + \gamma_2c_2(v - v^*)^2\bigr],
$$
a negative definite quadratic form when $(\gamma_1c_1 + \gamma_2b_2)^2 < 4\gamma_1\gamma_2b_1c_2$; with the chosen weights this is $4b_2^2c_1^2 < 4b_2c_1b_1c_2$, that is $b_2c_1 < b_1c_2$, which follows from the weak competition inequalities. Now consider the functional $E(t) = \int_\Omega V(u, v)\,\mathrm{d}x$. Since $V_u = \gamma_1(1 - u^*/u)$,

$$
\frac{\mathrm{d}E}{\mathrm{d}t} = \int_\Omega \bigl(V_u\,d_1\Delta u + V_v\,d_2\Delta v\bigr)\,\mathrm{d}x + \int_\Omega \bigl(V_u\,uf + V_v\,vg\bigr)\,\mathrm{d}x .
$$
Integrating by parts with the zero-flux boundary condition, the first integral equals $-\int_\Omega \bigl(d_1V_{uu}\lvert\nabla u\rvert^2 + d_2V_{vv}\lvert\nabla v\rvert^2\bigr)\,\mathrm{d}x$ with $V_{uu} = \gamma_1u^*/u^2 > 0$, so it is never positive; the second is negative unless $u \equiv u^*$, $v \equiv v^*$. Thus $E$ decreases strictly along nonconstant or non-equilibrium solutions, and a LaSalle-type argument (using the compactness of trajectories of parabolic equations) shows convergence to $(u^*, v^*)$. $\square$

Diffusion enters $\mathrm{d}E/\mathrm{d}t$ only through a term that is never positive: it smooths, and a stable well-mixed equilibrium stays stable. The proof uses only that $V$ is a sum of convex functions of each variable, and it applies to many systems with such a Lyapunov function. When competition is strong (bistable), the outcome also does not depend on diffusion in a convex habitat: Kishimoto and Weinberger (1985) proved that nonconstant steady states of (30.1) are then unstable, so that one species eventually occupies the whole habitat. In a nonconvex habitat, such as two chambers joined by a narrow channel (a "dumbbell"), the two competitors can each hold one chamber in a stable nonconstant steady state (Matano and Mimura 1983): the shape of the habitat alone can produce spatial segregation.

### 30.1.2. Competitive Invasion Waves

In a large habitat the outcome is reached through traveling fronts. If species $u$ is introduced at one end of a habitat occupied by $v$ at its carrying capacity $v^* = a_2/c_2$, its leading edge, where $u$ is rare, grows at the rate $a_1 - c_1v^*$, and by the argument for the Fisher–KPP equation ([7.19.17](/7.19.17), **traveling wave solution** of [2.5.7](/2.5.7)) one expects it to spread at

$$
c = 2\sqrt{d_1\bigl(a_1 - c_1v^*\bigr)}
$$
if this rate is positive. This "linear determinacy" holds under conditions that the nonlinear terms do not accelerate the front (Lewis, Li and Weinberger 2002). The replacement of the native red squirrel (*Sciurus vulgaris*) in Britain by the eastern gray squirrel (*S. carolinensis*), introduced from North America from 1876, was modeled in this way: a diffusion–competition model with parameters estimated from demography and dispersal reproduced the observed spread of the gray squirrel and the retreat of the red (Okubo et al. 1989), and the speed of the front was set by the growth rate of the invader at low density in the presence of the resident. Under strong competition the front connects the two single-species states, $(u^*, 0)$ behind and $(0, v^*)$ ahead, and its speed may have either sign: the species whose front advances wins in space even where the well-mixed model is bistable, so that the winner of a bistable competition in space is decided by the dynamics of the front, not by initial abundance.

### 30.1.3. A Heterogeneous Environment: the Slower Disperser Wins

Suppose now that resources vary in space, with a local growth rate $m(x)$, and that the two species differ only in their diffusion rates:

$$
u_t = d\Delta u + u(m - u - bv),\qquad v_t = D\Delta v + v(m - cu - v),
\tag{30.2}
$$
with zero-flux boundaries. Alone, a species with diffusion rate $d$ persists if $m$ is positive somewhere (for small $d$) or on average, and then approaches a unique positive steady state $\theta_d$, solving $d\Delta\theta + \theta(m - \theta) = 0$. Slow dispersers match the resource ($\theta_d \approx m$ where $m > 0$, an **ideal free distribution**, [7.18](/7.18)), fast dispersers are nearly uniform ($\theta_d \to$ the mean of $m$), and the total biomass $\int_\Omega\theta_d$ exceeds the total resource $\int_\Omega m$ for every $d$, with a maximum at intermediate $d$ ([7.19.17](/7.19.17)).

Whether a rare competitor can invade a resident at its steady state is decided by linearization. For $v$ rare and $u = \theta_d$, $v_t = D\Delta v + (m - c\theta_d)v$, a linear equation whose solutions grow or decay like $\mathrm{e}^{\lambda_1t}$, where $\lambda_1(D, h)$ is the principal eigenvalue of

$$
D\Delta\varphi + h(x)\varphi = \lambda\varphi\ \text{in}\ \Omega,\qquad \frac{\partial\varphi}{\partial\boldsymbol{n}} = 0,\qquad h = m - c\theta_d,
$$
with a positive eigenfunction. It has the variational characterization (a **Rayleigh quotient**)

$$
\lambda_1(D, h) = \max_{\varphi \ne 0}\frac{\int_\Omega\bigl(h\varphi^2 - D\lvert\nabla\varphi\rvert^2\bigr)\,\mathrm{d}x}{\int_\Omega\varphi^2\,\mathrm{d}x}.
$$

**Lemma 30.1.1** If $h$ is not constant, $\lambda_1(D, h)$ is strictly decreasing in $D$.

**Proof** Let $D_1 < D_2$ and let $\varphi_2$ be the maximizer for $D_2$. It is not constant, since a constant positive eigenfunction would force $h \equiv \lambda$. Hence $\int\lvert\nabla\varphi_2\rvert^2 > 0$ and

$$
\lambda_1(D_2, h) = \frac{\int\bigl(h\varphi_2^2 - D_2\lvert\nabla\varphi_2\rvert^2\bigr)}{\int\varphi_2^2} < \frac{\int\bigl(h\varphi_2^2 - D_1\lvert\nabla\varphi_2\rvert^2\bigr)}{\int\varphi_2^2} \le \lambda_1(D_1, h). \qquad\square
$$

**Theorem 30.1.2 (Dockery, Hutson, Mischaikow and Pernarowski 1998)** In (30.2) with $b = c = 1$ and nonconstant $m$: if $d < D$, the state $(\theta_d, 0)$ is stable and $(0, \theta_D)$ is unstable, and in fact $(\theta_d, 0)$ attracts all solutions with $u(\cdot, 0) \not\equiv 0$; if $d > D$ the roles are reversed. The slower disperser wins.

**Proof** (of the invasion part) The resident's steady state satisfies $d\Delta\theta_d + (m - \theta_d)\theta_d = 0$, so $\theta_d > 0$ is the principal eigenfunction of $d\Delta + (m - \theta_d)$ with eigenvalue $0$: $\lambda_1(d, m - \theta_d) = 0$. The function $m - \theta_d$ is not constant, for if $m - \theta_d \equiv k$ then $d\Delta\theta_d + k\theta_d = 0$ with $\theta_d > 0$ and zero flux forces $k = 0$ and $\theta_d$ constant, hence $m$ constant. By Lemma 30.1.1, the invasion rate of $v$, $\lambda_1(D, m - \theta_d)$, is negative for $D > d$ and positive for $D < d$ (Figure 1B). A slower invader therefore increases when rare and a faster one cannot. The global statement uses the theory of monotone (competitive) systems: with neither species able to persist alongside the other, solutions converge to the stable semitrivial state. $\square$

The reason is that a slow disperser tracks the resource: it accumulates where $m$ is high and avoids losing individuals to poor places, whereas a fast disperser constantly sends individuals into places where they die. Diffusion that is "blind" to the environment is costly in a heterogeneous but constant world. When competition is weak everywhere ($b, c < 1$), coexistence is common, but even then a species can be excluded: a resident with intermediate dispersal reaches a total biomass larger than the total resource, and a competitor that disperses much faster sees a habitat depleted below its average quality; if $c$ exceeds $c^* = \inf_d \int_\Omega m / \int_\Omega\theta_d < 1$, there are dispersal rates for which the faster species cannot invade and is excluded (Lou 2006). Figure 1C maps the outcomes for $b = c = 0.95$.

![Two competitors that differ only in dispersal, on (0, 1) with resource m(x) = 1 + 0.9 sin(2 pi x) and zero-flux ends. A: single-species steady states: the slow disperser (d = 0.001) matches the resource, the fast one (d = 10) is nearly uniform. B: symmetric competition (b = c = 1): the invasion rate lambda_1 of a rare competitor with diffusion rate D into a resident with d = 0.05 is zero at D = d and positive only for slower invaders (Theorem 30.1.2). C: weak competition (b = c = 0.95), outcome predicted by the two invasion rates over a grid of dispersal rates: coexistence for most pairs, but a species is excluded when its competitor has an intermediate dispersal rate (0.01 to 0.3, near the maximum of total biomass) and it disperses considerably faster](./plots/competition-dispersal.py)

Theorem 30.1.2 is an evolutionary statement as well. Read with $u$ and $v$ as a resident genotype and a mutant that differ only in dispersal rate, it says that a mutant with a slightly lower rate always invades: in a spatially heterogeneous but temporally constant environment, selection favors ever slower random dispersal (Hastings 1983), a special case of the "reduction principle" of population genetics. Dispersal is favored by the factors left out of this model: temporal variation, kin competition and inbreeding avoidance ([7.10.10](/7.10.10#sec-10.7)). Dispersal that is not blind, but conditioned on local fitness, escapes the cost: a strategy that produces an ideal free distribution, with fitness equal everywhere, is evolutionarily stable against all others (Cantrell, Cosner and Lou 2010), linking the reaction–diffusion theory to the behavioral theory of habitat choice ([7.18](/7.18)).

## 30.2. Advection and Competition

Many organisms do not diffuse blindly but move up gradients of resource quality, by taxis or by choosing where to settle. Belgacem and Cosner (1995) represented this by an advection term:

$$
u_t = \nabla\cdot\bigl(d\nabla u - \alpha u\nabla m\bigr) + u(m - u),\qquad \bigl(d\nabla u - \alpha u\nabla m\bigr)\cdot\boldsymbol{n} = 0\ \text{on}\ \partial\Omega,
$$
where the flux has a random part $-d\nabla u$ and a directed part $\alpha u\nabla m$, with advection rate $\alpha \ge 0$, and the boundary condition says that no individual crosses the boundary. Advection concentrates the population at the maxima of $m$; in convex habitats it improves persistence, whereas in some nonconvex habitats strong advection can drive individuals into a boundary region of poor quality and hinder it. The effects of a drift that is not chosen by the organism, a river current, on persistence are treated in [7.19.17](/7.19.17).

Cantrell, Cosner and Lou (2006, 2007) let an advecting species $u$ compete with a species $v$ that has the same diffusion rate but moves randomly:

$$
u_t = \nabla\cdot\bigl(d\nabla u - \alpha u\nabla m\bigr) + u(m - u - v),\qquad v_t = d\Delta v + v(m - u - v).
\tag{30.3}
$$
For small $\alpha$, the advecting species wins: a little movement toward better places is beneficial, and $(\theta_{u}, 0)$ is globally stable. For large $\alpha$ the result is unexpected: both semitrivial states are unstable and the species coexist. Strong advection crowds $u$ into a small neighborhood of the maximum of $m$ (in the limit, a spike), leaving most of the habitat underexploited, and $v$, the random disperser, can invade there. Too much habitat selection is no longer an advantage, because the selecting species crowds itself (Figure 2). The general lesson matches that of Section 30.1.3: the best movement strategy is one that matches the distribution of the population to the distribution of resources, which neither pure diffusion nor strong advection achieves.

![Advection toward better habitat (Eq. 30.3) with equal diffusion d = 0.1 and resource m(x) = 1 + 0.9 sin(pi x) on (0, 1), state at t = 1500 from u = v = 0.5. A: weak advection (alpha = 0.05): the advecting species u (blue) excludes the random disperser v (red). B: strong advection (alpha = 2): u is concentrated near the resource peak and v occupies the rest: coexistence. C: mean densities against alpha: v is excluded up to alpha of about 0.07 and coexists for larger alpha, while u declines](./plots/advection-coexistence.py)

## 30.3. Turing Instability

### 30.3.1. Diffusion-Driven Instability

Two interacting species move at different rates. Can their movement make a stable uniform state unstable? Turing (1952) showed that it can.

**Definition 30.3.1 (Diffusion-Driven Instability)** A homogeneous steady state of a system of reaction–diffusion equations undergoes *diffusion-driven instability* (Turing instability) if it is stable to spatially uniform perturbations in the absence of diffusion but unstable to some spatially nonuniform perturbation when diffusion is present. The stationary spatial patterns that grow from it are **Turing patterns** ([2.5.7](/2.5.7)).

Consider two species with densities $u$ and $v$ on an interval $[0, L]$ (or a rectangle) with zero-flux boundaries,

$$
u_t = f(u, v) + d_u\Delta u,\qquad v_t = g(u, v) + d_v\Delta v,
\tag{30.4}
$$
and a uniform steady state $(u^*, v^*)$ with $f = g = 0$. Write $J = \begin{bmatrix} f_u & f_v \\ g_u & g_v \end{bmatrix}$ for the Jacobian matrix at it and $D = \operatorname{diag}(d_u, d_v)$. For a small perturbation $\boldsymbol{w} = (u - u^*, v - v^*)$, the linearized system is $\boldsymbol{w}_t = J\boldsymbol{w} + D\Delta\boldsymbol{w}$. The eigenfunctions of $\Delta$ with zero-flux boundaries on $[0, L]$ are $\cos(kx)$ with $k = p\pi/L$, $p = 0, 1, 2, \dots$, and $\Delta\cos kx = -k^2\cos kx$. Substituting $\boldsymbol{w} = \boldsymbol{c}\,\mathrm{e}^{\sigma t}\cos kx$ gives $\sigma\boldsymbol{c} = (J - k^2D)\boldsymbol{c}$: the growth rate $\sigma(k^2)$ of mode $k$ is an eigenvalue of

$$
A(k^2) = J - k^2D = \begin{bmatrix} f_u - d_uk^2 & f_v \\ g_u & g_v - d_vk^2 \end{bmatrix}.
$$
The function $k^2 \mapsto \operatorname{Re}\sigma(k^2)$ is the **dispersion relation**. The general solution is a superposition of such modes, and the uniform state is unstable if and only if some admissible mode has $\operatorname{Re}\sigma > 0$.

**Theorem 30.3.1 (Conditions for Turing Instability)** The state $(u^*, v^*)$ is stable without diffusion and unstable, with diffusion, to modes with $k^2$ in some interval $(k_-^2, k_+^2)$ if and only if

$$
\text{(i)}\ f_u + g_v < 0,\qquad \text{(ii)}\ f_ug_v - f_vg_u > 0,\qquad \text{(iii)}\ d_vf_u + d_ug_v > 0,\qquad \text{(iv)}\ (d_vf_u + d_ug_v)^2 > 4d_ud_v(f_ug_v - f_vg_u).
$$
The unstable band is $k_\pm^2 = \bigl[(d_vf_u + d_ug_v) \pm \sqrt{(d_vf_u + d_ug_v)^2 - 4d_ud_v\det J}\bigr]/(2d_ud_v)$.

**Proof** Conditions (i) and (ii) are the trace–determinant conditions for stability of $J$, the case $k = 0$. For $k > 0$, $\operatorname{tr}A(k^2) = f_u + g_v - (d_u + d_v)k^2 < \operatorname{tr}J < 0$, so the two eigenvalues cannot both have positive real part, and complex eigenvalues have negative real part. Instability therefore requires a real positive eigenvalue, which occurs exactly when $\det A(k^2) < 0$:

$$
h(k^2) = \det A(k^2) = d_ud_vk^4 - (d_vf_u + d_ug_v)k^2 + \det J .
$$
This quadratic in $k^2$ is positive at $k^2 = 0$ by (ii), and it becomes negative for some $k^2 > 0$ if and only if its minimum, attained at

$$
k_{\mathrm{m}}^2 = \frac{d_vf_u + d_ug_v}{2d_ud_v},
$$
lies at positive $k^2$ (condition (iii)) and is negative: $h_{\min} = \det J - (d_vf_u + d_ug_v)^2/(4d_ud_v) < 0$, which is (iv). The band is the interval between the roots of $h$. $\square$

The conditions have a transparent structure. By (i), $f_u + g_v < 0$, and by (iii), $d_vf_u + d_ug_v > 0$; both can hold only if $f_u$ and $g_v$ have opposite signs and $d_u \ne d_v$. If $f_u > 0$ (species $u$ enhances its own growth near equilibrium, the "activator") then $g_v < 0$ (the "inhibitor" limits itself), and (iii) requires $d_v/d_u > -g_v/f_u > 1$: the inhibitor must spread faster than the activator. Condition (ii) with $f_ug_v < 0$ requires $f_vg_u < 0$, so the cross-effects have opposite signs. Two sign patterns are possible:

| Pattern | Signs of $J$ | Meaning | Example |
|---|---|---|---|
| activator–inhibitor | $\begin{bmatrix} + & - \\ + & - \end{bmatrix}$ | $u$ promotes $v$, $v$ inhibits $u$; high $u$ and high $v$ coincide | prey and predator; Gierer–Meinhardt ([7.5.12](/7.5.12)) |
| substrate depletion | $\begin{bmatrix} + & + \\ - & - \end{bmatrix}$ | $u$ consumes $v$, $v$ promotes $u$; high $u$ where $v$ is low | Schnakenberg, plants and water (Section 30.4) |

Setting $d_u = 1$ and $\delta = d_v$, condition (iv) at equality gives the *critical diffusion ratio*, the larger root of

$$
f_u^2\delta^2 + 2(2f_vg_u - f_ug_v)\delta + g_v^2 = 0,
\tag{30.5}
$$
and at $\delta = \delta_c$ the first unstable mode has $k_{\mathrm{c}}^2 = \sqrt{\det J/\delta_c}$, the double root of $h$. The pattern that first appears thus has a wavelength $2\pi/k_{\mathrm{c}}$ fixed by kinetics and diffusion, not by the size of the habitat. Two consequences matter in bounded habitats. Only discrete wave numbers $k = p\pi/L$ are available, so a habitat shorter than about half a wavelength cannot form a pattern at all; and as the habitat grows, the number of pattern elements increases in steps, each time a new mode enters the unstable band. In two dimensions the modes are $\cos(p\pi x/L_1)\cos(q\pi y/L_2)$ with $k^2 = (p\pi/L_1)^2 + (q\pi/L_2)^2$, and the nonlinear terms decide whether spots, stripes or labyrinths form: weakly nonlinear analysis shows that hexagonal spots are favored when the quadratic terms of the kinetics are asymmetric, stripes otherwise ([7.5.12](/7.5.12#sec-12.6)).

### 30.3.2. The Schnakenberg System

The simplest kinetics that produce Turing patterns are those of Schnakenberg (1979), a reduced model of the autocatalytic reaction $2U + V \to 3U$ with supply and removal, in dimensionless form

$$
f(u, v) = a - u + u^2v,\qquad g(u, v) = b - u^2v,\qquad a, b > 0 .
$$
The uniform state is $u^* = a + b$, $v^* = b/(a + b)^2$, and

$$
J = \begin{bmatrix} \dfrac{b - a}{a + b} & (a + b)^2 \\ -\dfrac{2b}{a + b} & -(a + b)^2 \end{bmatrix},\qquad \det J = (a + b)^2 > 0,\qquad \operatorname{tr}J = \frac{b - a}{a + b} - (a + b)^2 .
$$
The activator is $u$, self-enhancing when $b > a$; $v$ is a substrate consumed by $u$, of the substrate-depletion type. For $a = 0.1$, $b = 0.9$: $u^* = 1$, $f_u = 0.8$, $f_v = 1$, $g_u = -1.8$, $g_v = -1$, $\operatorname{tr}J = -0.2$, $\det J = 1$. Equation (30.5) becomes $0.64\delta^2 - 5.6\delta + 1 = 0$, so $\delta_c = 8.57$ and $k_{\mathrm{c}}^2 = 1/\sqrt{8.57} = 0.34$. With $\delta = 20$ the band of unstable modes is wide, the fastest mode has $k^2 = 0.24$, a wavelength of about 13, and a two-dimensional simulation from noise produces a hexagonal array of activator spots of that spacing (Figure 3). The parameter region where conditions (i)–(iv) hold, the *Turing space*, lies next to the region where the uniform state oscillates (Hopf, $\operatorname{tr}J > 0$).

![Turing instability in the Schnakenberg system. A: dispersion relation (largest real part of the eigenvalues of J − k² diag(1, d)) for a = 0.1, b = 0.9: stable for d = 5, marginal at d = d_c = 8.57 with k_c² = 0.34, a band of growing modes for d = 20. B: Turing space in the (a, b) plane for d = 20 (shaded): stable without diffusion, unstable with it; inside the dashed curve (tr J = 0) the uniform state is unstable even without diffusion. C: activator u after t = 200 on a periodic square of side 64 from the uniform state with 1 % noise: spots with a spacing close to the wavelength of the fastest mode, 12.9](./plots/turing-schnakenberg.py)

### 30.3.3. Predators and Prey

The classical ecological reading of the activator–inhibitor pattern is prey and predator: prey ($u$) feeds predators ($g_u > 0$), predators reduce prey ($f_v < 0$), and if predators spread faster than prey, a local excess of prey grows because the predators it attracts quickly disperse to surrounding areas, where they suppress prey. Segel and Jackson (1972) proposed this as the first ecological Turing mechanism, and Levin and Segel (1976) applied it to the patchiness of plankton. Which predator–prey models actually satisfy the conditions?

- In the Lotka–Volterra predation model with logistic prey, $f = ru(1 - u/K) - auv$, $g = eauv - \mu v$, the predator equation gives $g_v = eau^* - \mu = 0$ at equilibrium, and the prey equation $f_u = -ru^*/K < 0$. Then $f_ug_v = 0$, condition (iii) reads $d_vf_u > 0$ and fails: no Turing patterns for any diffusion rates. (The claim that this model forms patterns when $d_v \gg d_u$ is a common error.)
- In the Rosenzweig–MacArthur model ([7.19.26](/7.19.26)), prey self-enhancement $f_u > 0$ occurs on the rising side of the hump of the prey isocline, but again $g_v = 0$, so $\operatorname{tr}J = f_u > 0$: the uniform state is already unstable (the paradox of enrichment, a **Hopf bifurcation**), and condition (i) fails. Where it is stable, $f_u < 0$ and (iii) fails.
- Turing patterns therefore require both a self-enhancing prey near equilibrium and a self-limiting predator ($g_v < 0$): predator interference, territoriality or density-dependent mortality.

A minimal model with these ingredients, in dimensionless units, is

$$
u_t = u(1 - u) - \frac{uv}{u + a} + \Delta u,\qquad v_t = v\Bigl(\frac{u}{u + a} - b - cv\Bigr) + d\Delta v,
\tag{30.6}
$$
with a type II functional response ([7.19.25](/7.19.25)) and a quadratic predator death term $cv^2$. With $a = 0.2$, $c = 1.2$ and $b = 0.0716$ chosen so that the equilibrium is $u^* = 0.15$, $v^* = (1 - u^*)(u^* + a) = 0.2975$, on the rising side of the prey isocline (whose hump is at $u = (1 - a)/2 = 0.4$):

$$
f_u = 1 - 2u^* - \frac{av^*}{(u^* + a)^2} = 0.214,\quad f_v = -\frac{u^*}{u^* + a} = -0.429,\quad g_u = \frac{av^*}{(u^* + a)^2} = 0.486,\quad g_v = -cv^* = -0.357,
$$
so $\operatorname{tr}J = -0.143$ and $\det J = 0.132$: the well-mixed system is stable (a damped focus). Equation (30.5) gives $\delta_c = 14.6$. With predators diffusing 40 times faster than prey, the fastest mode has a wavelength of about 25, and simulations develop irregular patches and labyrinths of high prey density, over which the fast-moving predators are almost uniform but slightly concentrated (Figure 4). The required ratio of diffusion rates is large; in real systems it is approached when predators are much more mobile than their prey (insects on plants, fish on zooplankton). Cross-diffusion, movement of one species in response to the gradient of another (predators toward prey, prey away from predators), and nonlocal interactions relax the condition and are common extensions.

![Turing patterns in the predator–prey model (Eq. 30.6) with a = 0.2, c = 1.2 and uniform state u* = 0.15, v* = 0.2975. A: dispersion relation: stable for d = 5, marginal at d_c = 14.6, unstable band for d = 40 (fastest wavelength 25). B: prey density after t = 400 on a periodic square of side 128 from the uniform state with 2 % noise (d = 40): patches and labyrinths of high prey density. C: prey (blue) and predator (red) along the dotted transect in B; dotted lines are the uniform state: sharp prey patches, a nearly uniform predator](./plots/predator-prey-turing.py)

## 30.4. Self-Organized Patterns in Ecosystems

### 30.4.1. Scale-Dependent Feedback

Regular spatial patterns are found in many ecosystems: bands, spots, labyrinths and gaps of vegetation in drylands on every continent (*tiger bush* in Niger, the banded mulga of Australia, spotted grasslands in Sudan), regularly spaced ridges of mussels on intertidal flats, ribbed and string patterns in boreal peatlands, regularly spaced termite mounds and the bare "fairy circles" of the Namib. Their common explanation is a *scale-dependent feedback*: a positive feedback at short range (plants improve infiltration of water under their own canopy, mussels shelter each other from waves) combined with a negative feedback at longer range (plants deplete water from their surroundings, mussels deplete algae in the water flowing over neighbors), which is the activator–inhibitor or substrate-depletion structure of Section 30.3 (Rietkerk and van de Koppel 2008).

### 30.4.2. The Klausmeier Model of Banded Vegetation

On gentle slopes in semi-arid regions, vegetation often forms bands that run along the contours, separated by bare soil, with wavelengths of tens to hundreds of meters. Rain that falls on bare, crusted soil runs off downhill and infiltrates under the next band. Klausmeier (1999) captured this in a model of water $W$ and plant biomass $N$ on a slope, with $X$ the distance uphill:

$$
W_T = A - LW - RWN^2 + VW_X,\qquad N_T = RJWN^2 - MN + D\Delta N .
\tag{30.7}
$$
Water arrives as rainfall at rate $A$, is lost by evaporation at rate $LW$, is taken up by plants at rate $RWN^2$ and flows downhill with speed $V$; the factor $N^2$ expresses that uptake per plant increases with plant density because infiltration improves under vegetation. Plants grow in proportion to uptake with yield $J$, die at rate $M$ and spread by dispersal at rate $D$. With $w = J\sqrt{R/L}\,W$, $n = \sqrt{R/L}\,N$, $t = LT$ and $x = \sqrt{L/D}\,X$ the model becomes

$$
w_t = a - w - wn^2 + \nu w_x,\qquad n_t = wn^2 - mn + \Delta n,
\tag{30.8}
$$
with three dimensionless parameters: rainfall $a = AJ\sqrt{R}/L^{3/2}$, plant mortality $m = M/L$ and flow speed $\nu = V/\sqrt{LD}$. Klausmeier estimated $m = 0.45$ and $\nu = 182.5$ for grasses.

Uniform equilibria. Bare soil, $(w, n) = (a, 0)$, has Jacobian $\operatorname{diag}(-1, -m)$ and is always stable: a small amount of vegetation cannot grow, because uptake $wn^2$ is quadratic. Vegetated states satisfy $wn = m$ and $a - w - mn = 0$, so $mn^2 - an + m = 0$:

$$
n_\pm = \frac{a \pm \sqrt{a^2 - 4m^2}}{2m},\qquad w_\pm = \frac{m}{n_\pm},
$$
which exist if $a \ge 2m$, the minimum rainfall for vegetation. Since $n_+n_- = 1$, $n_+ > 1 > n_-$. At a vegetated state, using $wn = m$,

$$
J = \begin{bmatrix} -1 - n^2 & -2m \\ n^2 & m \end{bmatrix},\qquad \det J = m(n^2 - 1),\qquad \operatorname{tr}J = m - 1 - n^2 .
$$
The lower state $n_-$ has $\det J < 0$: a saddle, the threshold between bare soil and vegetation. The upper state has $\det J > 0$ and, for $m < 1 + n_+^2$ (always for the grass parameters), $\operatorname{tr}J < 0$: it is stable to uniform perturbations. Between $a = 2m$ and larger rainfall the system is bistable, with bare soil and vegetation as alternative stable states and a **saddle-node bifurcation** at $a = 2m$: a gradual decline of rainfall eventually causes an abrupt collapse to desert, a **regime shift** ([7.19.39](/7.19.39)).

Spatial instability on flat ground. Without the slope ($\nu = 0$) but with water diffusing at rate $d$ (add $d\Delta w$ to the water equation), the plant is the activator ($f_n = 2wn - m = m > 0$) and water the depleted substrate ($g_w = -1 - n^2 < 0$, $f_w = n^2 > 0$, $g_n = -2m < 0$), the substrate-depletion pattern. With the plant as $u$ ($d_u = 1$) and water as $v$ ($d_v = d$), conditions (iii) and (iv) of Theorem 30.3.1 become

$$
dm > 1 + n^2,\qquad (dm - 1 - n^2)^2 > 4dm(n^2 - 1):
$$
water must spread much faster than plants, which is true for overland flow and soil water against seed dispersal. Simulations of this model and its refinements (with separate surface and soil water, Rietkerk et al. 2002; von Hardenberg et al. 2001) produce a sequence of patterns as rainfall decreases: uniform vegetation, gaps, labyrinths, spots, bare soil.

Instability on a slope. With the advection term, a perturbation $\mathrm{e}^{\sigma t + \mathrm{i}kx}$ of the upper state satisfies $\sigma\boldsymbol{c} = M(k)\boldsymbol{c}$ with

$$
M(k) = \begin{bmatrix} -1 - n^2 + \mathrm{i}\nu k & -2m \\ n^2 & m - k^2 \end{bmatrix},
$$
whose eigenvalues are complex, so that growing modes travel. Here no difference of diffusion rates is needed: the directed flow of water plays the role of the fast inhibitor. For large $\nu$ the band of unstable wave numbers widens and extends to rainfall far above $2m$; for the grass parameters the uniform vegetation is unstable to bands for $2m < a < 3.3$ (Figure 5A). The bands that grow travel uphill, because water arrives at the uphill edge of each band, where plants grow, while plants at the downhill edge, in the band's water shadow, die back (Figure 5B, C). Uphill migration of vegetation bands has been documented in several regions, typically at rates of the order of decimeters to a meter per year, although bands are stationary in others.

![The Klausmeier model of banded vegetation (Eq. 30.8) with m = 0.45 and nu = 182.5. A: uniform states against rainfall a: bare soil (always stable), the saddle n− and the vegetated state n+, which exist for a ≥ 2m = 0.9; shaded, the range of rainfall in which uniform vegetation is unstable to bands, from the dispersion relation. B: space–time plot of plant biomass for a = 1.2 on a periodic slope of length 200, t = 300 to 400: four bands migrating steadily uphill (to the right). C: plant biomass (green) and water (blue) at t = 400: water accumulates as it flows downhill over bare soil and is taken up at the uphill edge of the next band](./plots/klausmeier-bands.py)

The model has two lessons beyond banded vegetation. First, patterned states persist at rainfall too low for uniform vegetation: concentrating water into bands keeps plants alive where a uniform cover would not survive, so pattern formation extends the range of persistence. Second, the transition from pattern to desert is itself abrupt, and the sequence of patterns along a rainfall gradient may announce it.

### 30.4.3. Other Self-Organized Patterns

- Mussel beds. On soft sediments of the Wadden Sea, young mussel beds (*Mytilus edulis*) form regularly spaced bands perpendicular to the tidal current. Mussels in clumps are protected from dislodgement by waves (short-range facilitation) but compete for the algae carried by the water, which are depleted downstream (long-range competition). Experiments that cleared mussels showed that patterned beds grew faster and were more resistant to disturbance than uniform ones of the same mean density, an emergent property of self-organization (van de Koppel et al. 2008).
- Fairy circles. The Namib fairy circles, bare disks of 2–12 m diameter surrounded by grass, arranged in a strikingly regular pattern, have been attributed both to sand termites (*Psammotermes allocerus*) and to scale-dependent competition for water among grasses. Similar circles found in Western Australia in 2016, without termites as an obvious cause, supported self-organization (Getzin et al. 2016); a model combining termite competition between colonies (which sets the large-scale regularity) with vegetation self-organization (smaller-scale patterns) reconciles the two explanations (Tarnita et al. 2017).
- Ribbed peatlands, tidal marshes and seagrass meadows show patterns explained by the same principle, with nutrients or sediment as the inhibitor.

### 30.4.4. Patterns as Warnings, and as an Escape from Tipping

Because pattern type changes systematically with stress, spatial patterns have been proposed as indicators of approaching collapse. In the models of Rietkerk et al. (2004), vegetation passes from labyrinths to spots before turning to desert, and spots are therefore a warning sign. In Mediterranean drylands, Kéfi et al. (2007) found that the sizes of vegetation patches follow a power law where grazing is light, and that the distribution loses its power-law tail as grazing increases, before desertification, an indicator that does not require a time series. These indicators are complemented by those of critical slowing down in time ([7.19.39](/7.19.39)). A more recent synthesis cautions that pattern formation does not always signal an imminent tipping point: in spatially extended systems, patterns can allow ecosystems to adjust gradually through a series of patterned states, evading a single catastrophic shift (Rietkerk et al. 2021). Whether a real dryland is close to collapse depends on which of these behaviors its feedbacks produce.

## 30.5. Individual-Based and Lattice Models

Reaction–diffusion equations treat densities as continuous and interactions as occurring between average densities at the same point. Individuals are discrete, interact locally and disperse over finite distances, and these facts can change the results qualitatively. The simplest spatially explicit model is the *contact process*: each site of a lattice is occupied (by an individual, or by a local population) or empty; occupied sites become empty at rate 1 and colonize each of their $z$ nearest neighbors at rate $\lambda/z$.

If neighbors were drawn at random from the whole lattice (global dispersal), the fraction $p$ of occupied sites would follow

$$
\frac{\mathrm{d}p}{\mathrm{d}t} = \lambda p(1 - p) - p,
$$
the **Levins model** of [7.19.16](/7.19.16), with persistence for $\lambda > 1$ and equilibrium $p^* = 1 - 1/\lambda$: the **mean-field approximation**. With local dispersal, occupied sites cluster: offspring land next to their parents, often on sites that are already occupied, and the effective colonization rate is reduced. The pair approximation, which follows the densities of pairs of neighboring sites and closes the equations by assuming that triplets are determined by pairs (Matsuda et al. 1992), gives

$$
p^* = \frac{(z - 1)\lambda - z}{(z - 1)\lambda - 1},
$$
with threshold $\lambda_c = z/(z - 1)$, $4/3$ for the square lattice. The exact threshold, known from simulation, is $\lambda_c \approx 1.65$: local dispersal raises the colonization rate needed for persistence by 65 % relative to the mean-field model (Figure 6). The same local crowding lowers equilibrium densities and slows the spread of populations relative to the predictions of mean-field models.

![The contact process on a 100 × 100 lattice (death rate 1, colonization of each of the 4 neighbors at rate lambda/4; discrete time steps of 0.1). A, B: occupied sites (green) at lambda = 1.9 and 3: clustering is evident near the threshold. C: equilibrium occupancy against lambda: the mean-field (Levins) model (threshold 1), the pair approximation (threshold 4/3) and simulation (points, threshold between 1.5 and 1.6, close to the critical value 1.65 of the continuous-time process)](./plots/contact-process.py)

Discreteness and local interactions also change the outcome of interactions between species. Durrett and Levin (1994) compared mean-field, reaction–diffusion and lattice versions of several competition models and found that they can predict different outcomes: in particular, spatial segregation in a lattice can allow coexistence that the mean-field model excludes, and the reverse. A striking experiment involved three strains of *Escherichia coli*: a colicin producer, a colicin-sensitive strain and a resistant strain, which beat each other in a cycle like rock–paper–scissors. On agar plates, where interactions are local, the three coexisted in shifting patches; in shaken flasks, where interactions are global, the resistant strain eliminated the others (Kerr et al. 2002). Spatially explicit individual-based models, which track every individual with its position, are now standard in ecology, from forest gap models ([7.19.33](/7.19.33)) to the spread of epidemics, and the approximations of this section (mean field, pair approximation, reaction–diffusion limits) are the tools that connect their behavior to analytical theory.

## Summary

| Topic | Results |
|---|---|
| Competition, uniform habitat | Weak competition: the constant equilibrium is globally stable for all diffusion rates (Theorem 30.1.1, Lyapunov functional); strong competition in convex habitats: no stable nonconstant states (Kishimoto–Weinberger); dumbbell habitats allow segregation |
| Invasion waves | Invader front speed $2\sqrt{d_1(a_1 - c_1v^*)}$ (linear determinacy); gray and red squirrels |
| Heterogeneous habitat | $\lambda_1(D, h)$ decreases in $D$ (Lemma 30.1.1); with $b = c = 1$ the slower disperser wins (Theorem 30.1.2); weak competition can still exclude (Lou 2006); selection for slow random dispersal (Hastings 1983) and for ideal free dispersal |
| Advection | Weak advection up resource gradients wins; strong advection crowds the advecting species and allows coexistence (Eq. 30.3) |
| Turing instability | Definition 30.3.1; conditions (i)–(iv) and unstable band (Theorem 30.3.1); critical ratio (30.5), $k_{\mathrm{c}}^2 = \sqrt{\det J/\delta_c}$; activator–inhibitor and substrate-depletion types; discrete modes in bounded habitats |
| Examples | Schnakenberg: $\delta_c = 8.57$ for $a = 0.1$, $b = 0.9$; LV and Rosenzweig–MacArthur predation cannot form Turing patterns; a self-enhancing prey and self-limiting predator can (Eq. 30.6, $\delta_c = 14.6$) |
| Klausmeier model | Bare soil always stable; vegetation for $a \ge 2m$, $n_\pm = (a \pm \sqrt{a^2 - 4m^2})/(2m)$, lower state a saddle; Turing condition on flat ground; uphill-migrating bands on slopes; patterns extend persistence |
| Ecosystem patterns | Scale-dependent feedback; mussel beds, fairy circles; patch-size power laws as warnings; patterns can also evade tipping |
| Lattice models | Contact process: mean field $p^* = 1 - 1/\lambda$, pair approximation threshold $z/(z - 1)$, exact $\approx 1.65$; local interactions change outcomes (Durrett–Levin; *E. coli* rock–paper–scissors) |

## Questions

1. Why does the Lyapunov functional argument of Theorem 30.1.1 fail for a predator–prey system with a stable equilibrium, and what does this suggest about the possibility of diffusion-driven instability in competition systems?

   **Answer** The argument needs a Lyapunov function that is a sum of convex functions of each species and decreases under the reaction terms for any relative weights compatible with the diffusion term. For two competitors with weak competition such a function exists, and diffusion can only make $\mathrm{d}E/\mathrm{d}t$ more negative, so no Turing instability is possible. For predators and prey the Volterra-type function decreases only marginally (or not at all) under the reaction terms in the classical model, and in models with a self-enhancing prey ($f_u > 0$) no function of this form decreases, so diffusion can destabilize. More generally, a two-species competition system has the sign pattern $\begin{bmatrix} - & - \\ - & - \end{bmatrix}$ near a stable coexistence equilibrium; since $f_u$ and $g_v$ are both negative, condition (iii) of Theorem 30.3.1 can never hold.
2. Verify the critical diffusion ratio $\delta_c = 8.57$ of the Schnakenberg system for $a = 0.1$, $b = 0.9$ and compute $k_{\mathrm{c}}$ and the corresponding wavelength. On an interval with zero-flux ends, what is the shortest length that allows a pattern at $\delta$ just above $\delta_c$?

   **Answer** $f_u = 0.8$, $f_v = 1$, $g_u = -1.8$, $g_v = -1$, $\det J = 1$. Eq. (30.5): $0.64\delta^2 + 2(2\cdot1\cdot(-1.8) - 0.8\cdot(-1))\delta + 1 = 0.64\delta^2 - 5.6\delta + 1 = 0$, roots $0.18$ and $8.57$; the root satisfying (iii) ($0.8\delta - 1 > 0$) is $8.57$. Then $k_{\mathrm{c}}^2 = \sqrt{1/8.57} = 0.342$, $k_{\mathrm{c}} = 0.585$, wavelength $2\pi/k_{\mathrm{c}} = 10.7$. The admissible modes are $k = p\pi/L$; the first nonuniform mode $p = 1$ equals $k_{\mathrm{c}}$ for $L = \pi/0.585 = 5.4$, half a wavelength: a shorter interval cannot form a pattern near threshold.
3. Show that in the Klausmeier model (30.8) the product of the two vegetated equilibria is $n_+n_- = 1$, and use it to prove that the lower state is always a saddle.

   **Answer** $n_\pm$ are the roots of $mn^2 - an + m = 0$, whose product is $m/m = 1$. Since $n_+ > n_-$ and their product is 1, $n_- < 1 < n_+$. At a vegetated state $\det J = m(n^2 - 1)$, which is negative for $n = n_- < 1$: the eigenvalues are real with opposite signs, a saddle.
4. In Theorem 30.1.2 the slower disperser wins in any heterogeneous habitat. Why do real organisms disperse at all? Name three features of real environments that favor faster dispersal, and say how each would enter the model.

   **Answer** (1) Temporal variation in $m(x, t)$: a population that does not move cannot track a changing resource, and in fluctuating environments intermediate or high dispersal rates can be favored; $m$ becomes time-dependent. (2) Local extinction (disturbance, catastrophes): it requires recolonization, as in metapopulation models; add random extinction events. (3) Kin competition and inbreeding: a disperser escapes competition with relatives ([Formula 10.7.1](/7.10.10#fml-10.7.1) of 7.10.10); this requires genetic structure absent from (30.2). In addition, conditional (non-random) dispersal toward better habitat is not costly in the way that blind diffusion is.
5. (Open) Design a field study to test whether banded vegetation on a dry hillslope is self-organized by the mechanism of the Klausmeier model rather than imposed by underlying soil heterogeneity.

   **Answer** Points to cover: map the bands repeatedly (historical aerial photographs, satellite images) to test the predicted uphill migration and the relation between band spacing and slope or rainfall across sites (the model predicts wavelength decreasing with rainfall and band orientation along contours); measure infiltration, runoff and soil moisture under bands and in interbands to quantify the feedback; check whether soil properties under interbands differ before or after vegetation loss (soil crusts are a consequence as well as a cause, so use deep soil properties unaffected by plants); perform experiments, clearing or creating vegetation patches or diverting runoff, and test whether the pattern regenerates at the same spacing (self-organization) or follows the soil template; fit the model to the measured parameters and compare predicted and observed wavelengths.
