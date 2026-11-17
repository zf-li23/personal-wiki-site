---
title: "Predator–Prey Dynamics II: Limit Cycles, Enrichment and Natural Cycles"
description: "The Rosenzweig–MacArthur model: humped prey isocline, the graphical stability criterion, the Hopf bifurcation and stable limit cycles; the paradox of enrichment and its experimental tests; refuges and type III responses; predator-mediated coexistence of competing prey with invasion criteria; chaos in three-species food chains (Hastings–Powell); predator–prey cycles in nature: lynx and hare with a fitted model, voles and lemmings, and spatial persistence in Huffaker's mites."
---

The Lotka–Volterra model of [7.19.25](/7.19.25) has neutral cycles that the smallest change destroys: prey self-limitation damps them, and saturation of the predator's feeding rate makes them grow. Combining both effects gives the model that has become the standard description of a predator and its prey, the Rosenzweig–MacArthur model, and with it the central qualitative result of predator–prey theory: an equilibrium that is stable when the prey's environment is poor loses its stability, through a **Hopf bifurcation**, when the environment is enriched, and is replaced by a stable limit cycle whose amplitude is independent of the initial conditions.

Section 26.1 develops the model and its graphical stability criterion; Section 26.2 the paradox of enrichment and what experiments have made of it; Section 26.3 shows how a predator can allow competing prey to coexist; Section 26.4 adds a third trophic level and finds chaos; Section 26.5 confronts the theory with the most famous cycles in nature. The mathematics of limit cycles, the Poincaré–Bendixson theorem and the Hopf bifurcation is in [2.4.11](/2.4.11); the population cycles of grouse, hares and voles were introduced, with their field experiments, in [7.19.13](/7.19.13#sec-13.4.4), and host–parasitoid cycles are in [7.19.27](/7.19.27).

## 26.1. The Rosenzweig–MacArthur Model

### 26.1.1. The Model and Its Scaling

**Definition 26.1.1 (Rosenzweig–MacArthur Model)** The **Rosenzweig–MacArthur model** (Rosenzweig and MacArthur 1963) describes logistic prey consumed by a predator with a type II functional response:

$$
\frac{\mathrm{d}N}{\mathrm{d}t} = rN\Bigl(1 - \frac{N}{K}\Bigr) - \frac{aNP}{1 + ahN}, \qquad \frac{\mathrm{d}P}{\mathrm{d}t} = \frac{caNP}{1 + ahN} - mP, \tag{26.1}
$$
with prey growth rate $r$, carrying capacity $K$, attack rate $a$, handling time $h$, conversion efficiency $c$ and predator death rate $m$.

It is the general consumer–resource model, Eq. (25.7) of [7.19.25](/7.19.25), with $g(N) = r(1 - N/K)$ and the disc equation $f(N) = aN/(1 + ahN)$. Measuring prey in units of the half-saturation density $1/(ah)$ and time in units of $1/r$,

$$
x = ahN, \qquad y = \frac{a}{r}P, \qquad \tau = rt,
$$
gives

$$
\frac{\mathrm{d}x}{\mathrm{d}\tau} = x\Bigl(1 - \frac{x}{\kappa}\Bigr) - \frac{xy}{1 + x}, \qquad \frac{\mathrm{d}y}{\mathrm{d}\tau} = y\Bigl(\frac{\gamma x}{1 + x} - \delta\Bigr), \tag{26.2}
$$
with three parameters, each with a clear meaning:

| Parameter | Definition | Meaning |
|---|---|---|
| $\kappa = ahK$ | prey carrying capacity / half-saturation density | enrichment of the prey's environment |
| $\gamma = c/(hr)$ | maximal predator production rate / prey growth rate | the predator's potential for numerical response |
| $\delta = m/r$ | predator death rate / prey growth rate | the predator's cost of living |

### 26.1.2. Isoclines and Equilibria

The predator isocline is again vertical: $\gamma x/(1 + x) = \delta$ gives

$$
x^* = \frac{\delta}{\gamma - \delta}, \qquad\text{or}\qquad N^* = \frac{m}{a(c - mh)}, \tag{26.3}
$$
which exists only if $\gamma > \delta$, that is, if the predator's maximal rate of reproduction $c/h$, reached when it eats as fast as it can handle prey, exceeds its death rate. The prey isocline is the parabola

$$
y = (1 + x)\Bigl(1 - \frac{x}{\kappa}\Bigr), \tag{26.4}
$$
which starts at $y = 1$, ends at $x = \kappa$ and, for $\kappa > 1$, has a hump at $x = (\kappa - 1)/2$. The hump has a biological reason. At high prey density the prey isocline falls because of the prey's self-limitation, as in [7.19.25](/7.19.25#sec-25.3). At low prey density it rises because the predators are saturated: the per capita risk of prey, $y/(1 + x)$ for given $y$, decreases as prey become more common, so more predators are needed to stop prey growth. Saturation makes predation inversely density dependent, which is destabilizing.

The equilibria are $(0, 0)$, a saddle; $(\kappa, 0)$, the prey alone at carrying capacity, with eigenvalues $-1$ and $\gamma\kappa/(1 + \kappa) - \delta$, so that predators can invade if and only if $x^* < \kappa$; and, when $x^* < \kappa$, the coexistence equilibrium $(x^*, y^*)$ with $y^* = (1 + x^*)(1 - x^*/\kappa)$.

### 26.1.3. The Graphical Stability Criterion

Rosenzweig and MacArthur (1963) discovered that the stability of the coexistence equilibrium can be read off the phase plane. The criterion holds for a whole class of models.

**Theorem 26.1.1 (Graphical Stability Criterion)** Consider

$$
\frac{\mathrm{d}N}{\mathrm{d}t} = F(N, P), \qquad \frac{\mathrm{d}P}{\mathrm{d}t} = P\,G(N),
$$
with $F, G$ continuously differentiable, $\partial F/\partial P < 0$ (predators reduce prey growth) and $G' > 0$ (predator growth increases with prey density and does not depend on predator density). Let $(N^*, P^*)$ with $P^* > 0$ be an equilibrium, and let the prey isocline near it be the graph $P = \varphi(N)$ of the solution of $F(N, \varphi(N)) = 0$. Then $\det J > 0$ at the equilibrium, and the equilibrium is asymptotically stable if $\varphi'(N^*) < 0$ (the predator isocline crosses the descending part of the prey isocline) and unstable if $\varphi'(N^*) > 0$ (it crosses the ascending part).

**Proof** Since $G(N^*) = 0$, the Jacobian at the equilibrium is

$$
J = \begin{bmatrix} F_N & F_P \\ P^*G'(N^*) & 0 \end{bmatrix},
$$
so $\det J = -F_PP^*G'(N^*) > 0$ and $\operatorname{tr}J = F_N$. Differentiating $F(N, \varphi(N)) = 0$ gives $F_N + F_P\varphi' = 0$, so $F_N = -F_P\varphi'$ has the sign of $\varphi'$, because $-F_P > 0$. With $\det J > 0$ the equilibrium is a sink if $\operatorname{tr}J < 0$ and a source if $\operatorname{tr}J > 0$ ([Theorem 11.5.2](/2.4.11#thm-11.5.2) of 2.4.11 and Lyapunov's first method). $\square$

The criterion explains the results of [7.19.25](/7.19.25) at a glance: in the Lotka–Volterra model the prey isocline is horizontal ($\varphi' = 0$, neutral); with logistic prey it falls everywhere (always stable); with interference the predator isocline is no longer vertical and the theorem does not apply directly, but tilting the predator isocline adds a negative term to the trace.

For the Rosenzweig–MacArthur model, $\varphi'(x^*) < 0$ means that $x^*$ lies to the right of the hump:

**Proposition 26.1.1 (Stability and Hopf Bifurcation)** For Eq. (26.2) with $\gamma > \delta$ and $x^* < \kappa$:

1. The coexistence equilibrium is a stable focus or node if $\kappa < \kappa_{\mathrm{H}} = 1 + 2x^*$ and unstable if $\kappa > \kappa_{\mathrm{H}}$.
2. At $\kappa = \kappa_{\mathrm{H}}$ a pair of complex conjugate eigenvalues crosses the imaginary axis with positive speed: a Hopf bifurcation.
3. For $\kappa > \kappa_{\mathrm{H}}$ every solution with $x(0), y(0) > 0$ not starting at the equilibrium approaches a periodic orbit; the orbit is in fact unique (Cheng 1981), so it is a globally attracting stable limit cycle.

**Proof** 1. At the equilibrium, with $y^*/(1 + x^*)^2 = (1 - x^*/\kappa)/(1 + x^*)$,

$$
J_{11} = x^*\Bigl(-\frac{1}{\kappa} + \frac{y^*}{(1 + x^*)^2}\Bigr) = \frac{x^*(\kappa - 1 - 2x^*)}{\kappa(1 + x^*)}, \quad J_{12} = -\frac{x^*}{1 + x^*}, \quad J_{21} = \frac{\gamma y^*}{(1 + x^*)^2}, \quad J_{22} = 0.
$$
So $\det J = -J_{12}J_{21} > 0$ and $\operatorname{tr}J = J_{11}$, which is negative if and only if $\kappa < 1 + 2x^*$, as Theorem 26.1.1 predicts: the hump of (26.4) is at $(\kappa - 1)/2$.

2. Near $\kappa_{\mathrm{H}}$ the eigenvalues are $\frac12\operatorname{tr}J \pm \mathrm{i}\sqrt{\det J - \frac14(\operatorname{tr}J)^2}$, complex because $\operatorname{tr}J \approx 0$ and $\det J > 0$. Their real part $\frac12 J_{11}$ vanishes at $\kappa_{\mathrm{H}}$, and since $x^*$ does not depend on $\kappa$,

$$
\frac{\mathrm{d}J_{11}}{\mathrm{d}\kappa}\Big|_{\kappa_{\mathrm{H}}} = \frac{x^*}{\kappa_{\mathrm{H}}(1 + x^*)} > 0.
$$

3. Solutions are bounded: let $W = x + y/\gamma$; then $\dot W = x(1 - x/\kappa) - (\delta/\gamma)y$, so $\dot W + \delta W = (1 + \delta)x - x^2/\kappa \le \kappa(1 + \delta)^2/4$, and $W$ eventually stays below $\kappa(1 + \delta)^2/(4\delta) + 1$. The positive quadrant is invariant, and in it the only equilibrium is the unstable focus or node $(x^*, y^*)$, which repels nearby orbits. The boundary equilibria cannot belong to the $\omega$-limit set of an interior orbit: $(0, 0)$ and $(\kappa, 0)$ are saddles whose stable manifolds lie on the axes, and a standard argument (the Butler–McGehee lemma) shows that an $\omega$-limit set containing such a saddle would contain an entire orbit of its unstable manifold, which leaves every bounded neighbourhood of the axes along the interior. By the Poincaré–Bendixson theorem ([Theorem 11.6.1](/2.4.11#thm-11.6.1) of 2.4.11), the $\omega$-limit set of every interior orbit other than the equilibrium is a periodic orbit. Uniqueness, which needs a separate argument, was proved by Cheng (1981), and was extended to a large class of predator–prey models by Kuang and Freedman (1988). $\square$

The bifurcation is supercritical: the limit cycle is born with zero amplitude at $\kappa_{\mathrm{H}}$ and grows as $\kappa$ increases (Figure 1, Figure 2A). In original units the condition for stability reads

$$
K < K_{\mathrm{H}} = \frac{1}{ah} + 2N^*. \tag{26.5}
$$
A stable equilibrium requires that the prey's carrying capacity be not much larger than what the predator needs to break even: inefficient predators (large $N^*$) and saturating at high density (small $ah$) favour stability; efficient predators on productive prey oscillate.

The contrast with [7.19.25](/7.19.25) is essential. A limit cycle is isolated and attracting: its amplitude and period are properties of the parameters, not of the history, and a disturbance is followed by a return to the same cycle. Regular oscillations of constant amplitude in real populations are therefore consistent with limit cycles, not with Lotka–Volterra cycles.

![The Rosenzweig–MacArthur model, Eq. (26.2), with γ = 2 and δ = 1, so that the predator isocline (red, dashed) is x* = 1 and the Hopf point κ_H = 1 + 2x* = 3; the prey isocline is blue (dashed) with its hump marked ▲. A: κ = 2.5: the predator isocline crosses the descending limb of the prey isocline and trajectories spiral into a stable focus (filled circle; Theorem 26.1.1). B: κ = 5: the crossing is on the ascending limb; the equilibrium (open circle) is an unstable focus, and trajectories from inside and outside converge to the same stable limit cycle (Proposition 26.1.1). C: with a sigmoid (type III) response x²/(1 + x²), γ = 3 and δ = 0.6 (x* = 0.5), the prey isocline rises steeply toward low prey density, because rare prey are hardly attacked; the predator isocline crosses it on a descending part and the equilibrium is stable even at κ = 8](./plots/rm-phase-portraits.py)

### 26.1.4. Type III Responses, Refuges and Multiple States

Anything that makes predation density dependent at low prey density bends the prey isocline upward near the vertical axis and can stabilize the interaction (Figure 1C).

- A type III functional response ([7.19.25](/7.19.25#sec-25.4.3)) does so if the predator can persist at the low prey density where its response is accelerating, which requires an efficient predator. A specialist that ignores rare prey cannot usually maintain itself on them; the strongest stabilization comes from generalists that switch among prey and whose numbers are set by other food, so that their isocline is horizontal rather than vertical. Generalist predators are more common in southern than in northern Fennoscandia, and voles there do not cycle ([7.19.13](/7.19.13#sec-13.4.4)).
- A refuge that protects a fixed number $N_{\mathrm{r}}$ of prey (predation acts only on $N - N_{\mathrm{r}}$) makes the prey isocline rise without limit near $N_{\mathrm{r}}$, and stabilizes for the same reason. A refuge that protects a fixed proportion of prey merely rescales the attack rate and has a much weaker effect.
- When the prey isocline has a valley and a hump, as with type III predation at high carrying capacity, the predator isocline of a generalist can cross it three times, giving a low equilibrium held by predators, a high equilibrium held by food, and an unstable one between them. The spruce budworm model of [7.19.13](/7.19.13#sec-13.2.5) is this situation with the predators held constant: outbreaks occur when growth of the forest removes the low equilibrium, and the system shows hysteresis, the subject of regime shifts in [7.19.39](/7.19.39).

## 26.2. The Paradox of Enrichment

### 26.2.1. Rosenzweig's Paradox

Proposition 26.1.1 has a disturbing consequence, which Rosenzweig (1971) called a paradox.

**Definition 26.2.1 (Paradox of Enrichment)** The **paradox of enrichment** is the prediction of prey-dependent predator–prey models with saturating functional responses that increasing the carrying capacity of the prey (by fertilization, nutrient input or protection) destabilizes the interaction: the equilibrium gives way to a limit cycle whose amplitude grows and whose minima approach zero, so that enrichment can lead to the extinction of the predator, the prey or both.

The mechanism has three parts, all visible in Figure 2. First, the equilibrium prey density $x^*$ does not change with $\kappa$: it is set by the predator, Eq. (26.3), so all extra production goes into predators, whose equilibrium $y^* = (1 + x^*)(1 - x^*/\kappa)$ rises. Second, as $\kappa$ passes $\kappa_{\mathrm{H}} = 1 + 2x^*$ the hump of the prey isocline moves to the right of the predator isocline and the equilibrium becomes unstable. Third, on the limit cycle the minima of both species fall roughly exponentially with $\kappa$ (Figure 2B): at $\kappa = 10$ in the figure, both species spend part of each cycle at densities four orders of magnitude below their means. In a finite population, such troughs end in extinction through **demographic stochasticity** ([7.19.15](/7.19.15)).

![The paradox of enrichment in the Rosenzweig–MacArthur model (γ = 2, δ = 1; x* = 1, κ_H = 3). A: bifurcation diagram against the prey carrying capacity κ: the equilibrium prey density stays at x* = 1, the equilibrium predator density rises, both are stable (solid) below the Hopf point and unstable (dashed) above it; the shaded band shows the range of prey densities on the limit cycle. B: the minimum densities of prey and predator on the cycle (log scale) fall roughly exponentially with κ. C: time series at κ = 2.5 (damped oscillations, dotted) and κ = 8 (sharp peaks and long troughs near zero, solid)](./plots/enrichment.py)

### 26.2.2. Experimental Tests

The paradox has been tested in laboratory systems, with mixed but instructive results.

- Protists. Gause (1934) found that the ciliate *Didinium nasutum* ate all the *Paramecium caudatum* in a simple culture and then starved; with a sediment refuge for the prey, *Paramecium* survived after the predator died out, and only regular immigration of both produced repeated oscillations. Luckinbill (1973) made *Didinium* and *Paramecium aurelia* persist for many cycles by thickening the medium with methyl cellulose, which reduces the attack rate, and by halving the food for *Paramecium*, which reduces its carrying capacity: both manipulations move the system toward the stable side of Eq. (26.5).
- Rotifers and algae in chemostats. Fussmann and colleagues (2000) grew the rotifer *Brachionus calyciflorus* on the green alga *Chlorella vulgaris* in chemostats, where the dilution rate acts as a mortality imposed on both species and the nitrogen concentration of the inflow as enrichment. As the dilution rate was varied the system showed stable coexistence, cycles and extinction of the predator, in the order and at the parameter values predicted by a parameterized consumer–resource model: the experiment crossed a Hopf bifurcation in a living system. Yoshida and colleagues (2003) then found that when the algae were genetically variable, cycles became longer and predator and prey oscillated almost in antiphase, because a defended but competitively inferior algal clone increased when rotifers were abundant and declined when they were rare. Rapid evolution of prey defence changes the shape of the cycles and is itself a stabilizing factor.

In the field the paradox is rarely seen. Fertilized lakes become more productive, but they do not regularly develop violent predator–prey cycles, and when they do, other mechanisms are often responsible. Several features of real systems, each in effect bending the prey isocline or tilting the predator isocline, counteract the destabilization: inedible or defended prey, whose share grows with enrichment (large or colonial algae that zooplankton cannot eat); prey refuges; predator interference and ratio dependence ([7.19.25](/7.19.25#sec-25.5)), under which prey equilibria rise with enrichment and stability need not decline; declining food quality at high productivity (algae grown under high light and low phosphorus are poor food for *Daphnia*, a stoichiometric constraint, [7.19.6](/7.19.6)); and spatial structure. The paradox is thus best read as a statement of a tendency, which real food webs have many ways to resist, and as an explanation of why the theory needs those mechanisms.

## 26.3. Predator-Mediated Coexistence

### 26.3.1. Two Competing Prey and One Predator

A predator can do more than regulate its prey: by feeding preferentially on a superior competitor, it can prevent that competitor from excluding inferior ones. Combining the Lotka–Volterra competition model ([7.19.22](/7.19.22)) with Lotka–Volterra predation, and scaling as in [7.19.22](/7.19.22) and [7.19.25](/7.19.25), gives

$$
\begin{aligned}
\frac{\mathrm{d}u_1}{\mathrm{d}\tau} &= u_1(1 - u_1 - a u_2 - v),\\
\frac{\mathrm{d}u_2}{\mathrm{d}\tau} &= \rho u_2(1 - u_2 - b u_1 - \kappa v),\\
\frac{\mathrm{d}v}{\mathrm{d}\tau} &= v(-d + e_1u_1 + e_2u_2),
\end{aligned} \tag{26.6}
$$
where $u_1, u_2$ are the two prey relative to their carrying capacities, $a$ and $b$ the scaled competition coefficients, $v$ the predator scaled by its effect on prey 1, $\kappa$ the predator's relative attack on prey 2 (per unit of its density, relative to prey 1), $e_1, e_2$ the predator's gain from each prey and $d$ its death rate. Without the predator, $a < 1 < b$ means that prey 1 excludes prey 2 ([7.19.22](/7.19.22)).

**Proposition 26.3.1 (Invasion Conditions)** Suppose $a < 1 < b$, $0 < \kappa < 1$ and $d < e_1$.

1. The predator persists with prey 1 alone at $(u_1, v) = (d/e_1,\ 1 - d/e_1)$, and prey 2 can invade this system if and only if
   $$
   d < e_1\frac{1 - \kappa}{b - \kappa}.
   $$
2. If $d < e_2$, the predator persists with prey 2 alone at $(u_2, v) = (d/e_2,\ (1 - d/e_2)/\kappa)$, and prey 1 can invade this system if and only if
   $$
   d > e_2\frac{1 - \kappa}{1 - a\kappa};
   $$
   if $d \ge e_2$, the predator cannot persist on prey 2, and prey 1 invades prey 2 alone because $a < 1$.

When both invasions are possible, no species is lost: the three species coexist.

**Proof** In the subsystem of prey 1 and the predator, $\dot v = 0$ requires $u_1 = d/e_1 < 1$ and $\dot u_1 = 0$ then gives $v = 1 - d/e_1 > 0$; this is the logistic-prey predator model of Proposition 25.3.1 of [7.19.25](/7.19.25), whose equilibrium is globally stable. A rare prey 2 has per capita growth rate $\rho(1 - bu_1 - \kappa v)$ there, which is positive if and only if $1 - bd/e_1 - \kappa(1 - d/e_1) > 0$, that is $(d/e_1)(b - \kappa) < 1 - \kappa$; since $b > \kappa$ this is condition 1. In the same way, in the subsystem of prey 2 and the predator the equilibrium is $u_2 = d/e_2$, $v = (1 - d/e_2)/\kappa$, and rare prey 1 grows at the rate $1 - au_2 - v = 1 - ad/e_2 - (1 - d/e_2)/\kappa$. Multiplying by $\kappa > 0$, this is positive if and only if $(d/e_2)(1 - a\kappa) > 1 - \kappa$, condition 2 (note $1 - a\kappa > 0$). Mutual invasibility means that each boundary state with one prey missing is unstable to the return of that prey; together with the boundedness of solutions it implies, for this system, that the three species persist (a result of permanence theory, which we use without proof). $\square$

Coexistence therefore requires an intermediate predator mortality (Figure 3). If the predator is very efficient (small $d$), it holds prey 1 so low that prey 1 cannot recover in the presence of the predator supported by prey 2, and prey 1 is lost: the predator has turned the competitive hierarchy upside down. If the predator is inefficient (large $d$), it does not reduce prey 1 enough, and prey 1 excludes prey 2 as in the absence of predators. In between, the predator suppresses its preferred prey just enough. The preference matters: the smaller $\kappa$, the wider the window.

![Predator-mediated coexistence, Eq. (26.6), with a = 0.5, b = 1.5 (prey 1 excludes prey 2 without the predator), ρ = 1, e₁ = 1 and e₂ = 0.2. A: time series for a relative attack κ = 0.3 on prey 2 and three predator death rates: d = 0.1, the efficient predator eliminates its preferred prey 1 and persists with prey 2; d = 0.35, all three species coexist; d = 0.8, the predator persists on prey 1, which excludes prey 2. B: long-term outcomes in the (d, κ) plane from simulations on a coarse grid (green: prey 2 and predator; yellow: all three; blue: prey 1 and predator; grey: prey 1 alone), with the invasion boundaries of Proposition 26.3.1: prey 2 can invade the prey 1–predator system to the left of the solid curve, prey 1 can invade the prey 2–predator system to the right of the dashed curve, and the predator cannot live on prey 1 for d > e₁ (dotted)](./plots/predator-mediated-coexistence.py)

### 26.3.2. In the Field

The classic demonstrations are Paine's removal of the starfish *Pisaster ochraceus* from rocky shores in Washington, after which mussels monopolized the space and the number of species fell, and Lubchenco's experiments with the periwinkle *Littorina littorea*, which prefers the competitively dominant green alga *Ulva* (formerly *Enteromorpha*) and maximizes algal diversity in tide pools at intermediate snail densities. These are treated as community processes, with the concept of a **keystone species**, in [7.19.33](/7.19.33). The reverse effect, in which two prey that share a predator harm each other by increasing its numbers, is **apparent competition** ([7.19.39](/7.19.39)); in Eq. (26.6) it is the interaction between prey 2 and prey 1 that passes through $v$.

## 26.4. Chaos in Food Chains

Two-species autonomous models in continuous time cannot be chaotic: by the Poincaré–Bendixson theorem their bounded trajectories approach equilibria or periodic orbits. Three species suffice. Hastings and Powell (1991) linked two Rosenzweig–MacArthur interactions into a food chain of a resource $x$ (logistic), a consumer $y$ and a top predator $z$, both consumers with type II responses:

$$
\begin{aligned}
\dot x &= x(1 - x) - \frac{a_1xy}{1 + b_1x},\\
\dot y &= \frac{a_1xy}{1 + b_1x} - \frac{a_2yz}{1 + b_2y} - d_1y,\\
\dot z &= \frac{a_2yz}{1 + b_2y} - d_2z.
\end{aligned} \tag{26.7}
$$
With $a_1 = 5$, $a_2 = 0.1$, $b_2 = 2$, $d_1 = 0.4$ and $d_2 = 0.01$, the lower pair oscillates fast and the top predator, which lives long ($d_2$ small), modulates these oscillations slowly. For $b_1$ near 3 the **attractor** has the shape of a teacup (Figure 4A): the fast consumer–resource cycle is stretched and folded by the slow changes of the top predator, so that the time series is irregular (Figure 4B), nearby trajectories diverge, and the largest **Lyapunov exponent** is positive. As $b_1$ increases the limit cycle undergoes period doubling and the dynamics become **chaos**, interrupted by periodic windows, the same sequence as in the discrete logistic map ([7.19.12](/7.19.12)).

![Chaos in the Hastings–Powell food chain, Eq. (26.7), with a₁ = 5, a₂ = 0.1, b₂ = 2, d₁ = 0.4 and d₂ = 0.01. A: the "teacup" attractor for b₁ = 3, after discarding a transient: a fast resource–consumer oscillation is stretched and folded by the slow dynamics of the top predator z (vertical axis). B: the top predator z and ten times the consumer y over 1000 time units: irregular, non-repeating fluctuations. C: bifurcation diagram: the local maxima of z on the attractor against b₁ (70 values). A single branch indicates a limit cycle; branches split near b₁ ≈ 2.65 and become clouds of points (chaos) from about 2.8, with periodic windows](./plots/hastings-powell.py)

Whether chaos is common in nature is a separate question ([7.19.12](/7.19.12#sec-12.4) discusses the evidence for single species). It has been demonstrated in two experimental food webs: Becks and colleagues (2005) found chaotic dynamics in a chemostat with a ciliate predator and two bacterial prey at intermediate dilution rates, and Benincà and colleagues (2008) followed a plankton community from the Baltic Sea in a laboratory mesocosm for more than eight years, with constant external conditions, and found that its species fluctuated irregularly, with positive Lyapunov exponents. Chaotic food webs can persist; what chaos limits is prediction, which beyond a horizon of a few weeks in the mesocosm was no better than guessing the mean.

## 26.5. Predator–Prey Cycles in Nature

### 26.5.1. The Lynx and the Hare

The roughly ten-year cycle of the Canada lynx (*Lynx canadensis*) and the snowshoe hare (*Lepus americanus*) is the best-known population cycle. The longest record is the number of pelts traded to the Hudson's Bay Company, which goes back to the early nineteenth century; the short series for 1900–1920 in Figure 5 is reproduced in many textbooks. Fitting the Lotka–Volterra model (25.1) to it by least squares on the log scale gives $r = 0.54$ per year for hares, $m = 0.80$ per year for lynx, a small-amplitude period $2\pi/\sqrt{rm} \approx 9.6$ years, and equilibria $N^* \approx 34$ and $P^* \approx 20$ thousand pelts, close to the means of the data (34.1 and 20.2), as Theorem 25.1.1 of [7.19.25](/7.19.25) requires of a cycle. The fit is visually good, and it shows the expected quarter-cycle lag.

A good fit is not a demonstration of mechanism, and the lynx–hare cycle is a cautionary example.

- The data are pelts, not populations. Trapping effort varied with fur prices and with the number of trappers, and the series for different regions were combined.
- In other parts of the longer record the loops in the phase plane run clockwise for some years, as if the hares ate the lynx (Gilpin 1973), which no model of this kind can produce.
- Hares cycle in regions without lynx, and the lynx is only one of several predators (coyotes, great horned owls, goshawks) that kill hares. Time-series analysis of the record suggests that the hare series has a more complex structure, reflecting both its food and its predators, whereas the lynx series is mainly driven by the hare (Stenseth and colleagues 1997).
- Field experiments at Kluane Lake in the Yukon ([7.19.13](/7.19.13#sec-13.4.4)) found that adding food tripled hare density, excluding mammalian predators roughly doubled it, and doing both increased it about elevenfold (Krebs and colleagues 1995). Predation is the immediate cause of most hare deaths, but the delay in the hare's recovery comes from predator-induced stress transmitted to offspring.

The hare cycle is thus the product of a three-level system, vegetation–hare–predators, in which the lynx is a follower more than a driver. What the simple models contribute is not a fit but a framework: which delays and nonlinearities are required for cycles, and which experiments can tell the candidate mechanisms apart.

![The snowshoe hare and the Canada lynx, 1900–1920: pelts (thousands) from the Hudson's Bay Company fur returns, as compiled by MacLulich (1937) and Elton and Nicholson (1942) and widely reproduced. A: the data and the Lotka–Volterra model (25.1) fitted by least squares on the log scale (Nelder–Mead; r = 0.54 and m = 0.80 per year, period about 9.6 years). B: the data in the phase plane, labelled every five years; in these two decades the loops run anticlockwise, as the model requires; dashed: the fitted model orbit](./plots/lynx-hare.py)

### 26.5.2. Voles, Lemmings and Specialist Predators

The 3–5-year cycles of voles and lemmings ([7.19.13](/7.19.13#sec-13.4.4)) are the other main testing ground. In Fennoscandia the specialist predation model of Hanski, Turchin and colleagues is a Rosenzweig–MacArthur-type system: voles with logistic growth and a seasonal environment, weasels with a type II functional response and a numerical response delayed by their breeding cycle, and generalist predators with a type III response whose density is fixed by alternative prey. Increasing the density of generalists, as one goes south, damps and finally removes the cycles, as Section 26.1.4 predicts for a horizontal predator isocline. For collared lemmings in northeast Greenland, Gilg, Hanski and Sittler (2003) parameterized a model with one specialist (the stoat) and three generalists (arctic fox, snowy owl and long-tailed skua) from field data and reproduced the observed four-year cycle; for Norwegian lemmings, Turchin and colleagues (2000) argued that the cycles are instead generated by the interaction with their food plants, with mosses recovering slowly from grazing. Different systems with the same period may have different drivers: in a predator–prey cycle the predator lags the prey by about a quarter cycle, in a plant–herbivore cycle the plants do.

### 26.5.3. Spatial Structure: Huffaker's Mites

The models of this chapter describe well-mixed populations. In nature predator and prey occupy patches, and local overexploitation can be compensated by recolonization. Huffaker (1958) tested this with the six-spotted mite *Eotetranychus sexmaculatus*, which feeds on oranges, and the predatory mite *Typhlodromus occidentalis*. On a few oranges close together, predators found all prey, ate them, and starved: the system collapsed within one cycle. On a large array of oranges, mostly covered so that only small areas could be fed on, separated by petroleum-jelly barriers that slowed the walking predators, and with wooden posts from which the prey could disperse on silk threads in an air current, the system persisted through three successive oscillations: prey colonized empty oranges before predators found them, predators overexploited local prey and died out locally, and the cycle restarted elsewhere. Later experiments with protists in networks of connected bottles (Holyoak and Lawler 1996) gave the same result: persistence increased with the number of patches and with restricted dispersal.

The interaction persists as a **metapopulation** ([7.19.16](/7.19.16)): local populations are unstable, but asynchrony among patches and recolonization keep the regional system going. The spatial version of this idea, with waves and spirals of abundance, is developed for host–parasitoid systems in [7.19.27](/7.19.27#sec-27.4) and for reaction–diffusion models in [7.19.30](/7.19.30).

## Summary

- Rosenzweig–MacArthur model (Definition 26.1.1): logistic prey and a type II predator; three dimensionless parameters $\kappa = ahK$ (enrichment), $\gamma = c/(hr)$, $\delta = m/r$. The predator isocline is vertical at $x^* = \delta/(\gamma - \delta)$; the prey isocline is humped, because predator saturation makes predation inversely density dependent at low prey density.
- Graphical criterion (Theorem 26.1.1): with prey-dependent predator growth, the coexistence equilibrium is stable if the predator isocline crosses the descending part of the prey isocline and unstable if it crosses the ascending part.
- Hopf bifurcation (Proposition 26.1.1): stability is lost at $\kappa_{\mathrm{H}} = 1 + 2x^*$ ($K_{\mathrm{H}} = 1/(ah) + 2N^*$), and a unique, globally attracting limit cycle appears, whose amplitude is fixed by the parameters, unlike the neutral Lotka–Volterra cycles.
- Type III responses, fixed-number refuges and generalist predators bend or tilt the isoclines and stabilize; they can also create alternative equilibria and hysteresis.
- Paradox of enrichment (Definition 26.2.1): enrichment leaves $x^*$ unchanged, raises predators, destabilizes the equilibrium and deepens the troughs of the cycle exponentially. Laboratory tests (*Didinium*–*Paramecium*, rotifer–alga chemostats) support the Hopf transition; in the field, inedible prey, refuges, interference, poor food quality and space counteract it.
- Predator-mediated coexistence (Proposition 26.3.1): a predator that prefers the superior competitor allows the inferior one to persist for intermediate predator mortality, $e_2(1 - \kappa)/(1 - a\kappa) < d < e_1(1 - \kappa)/(b - \kappa)$.
- Three-species food chains can be chaotic (Hastings–Powell teacup attractor); chaos has been demonstrated in a chemostat food web and a plankton mesocosm.
- Natural cycles: the lynx–hare pelt series is fitted well by the Lotka–Volterra model, but pelts, clockwise loops, hare cycles without lynx and the Kluane experiments show a three-level system; vole cycles are explained by specialist predators damped by generalists; Huffaker's mites persisted only in a patchy universe, as a metapopulation.

## Questions

1. In the Rosenzweig–MacArthur model with $a = 0.02$, $h = 0.5$, $c = 0.4$ and $m = 0.2$ (time in days, densities per square metre), find the equilibrium prey density, and the carrying capacity above which the equilibrium is unstable. A manager fertilizes a pasture and doubles $K$ from 100 to 200. What happens to the predator–prey system?

   **Answer** $N^* = m/[a(c - mh)] = 0.2/[0.02 \times (0.4 - 0.1)] = 33.3$. The half-saturation density is $1/(ah) = 100$, so $K_{\mathrm{H}} = 100 + 2 \times 33.3 = 166.7$ (Eq. (26.5)). At $K = 100$ the equilibrium is stable, with $P^*$ given by the prey isocline, $P^* = (r/a)(1 + ahN^*)(1 - N^*/K)$. At $K = 200 > K_{\mathrm{H}}$ it is unstable and the populations cycle; the prey equilibrium is unchanged at 33.3, and prey are no more abundant on average, while the predators are more numerous and both species reach low densities in the troughs: the paradox of enrichment.
2. Show directly from Eq. (26.2), without Theorem 26.1.1, that the slope of the prey isocline at $x^*$ is negative exactly when $\kappa < 1 + 2x^*$.

   **Answer** The prey isocline is $\varphi(x) = (1 + x)(1 - x/\kappa) = 1 + x(1 - 1/\kappa) - x^2/\kappa$, with $\varphi'(x) = 1 - 1/\kappa - 2x/\kappa = (\kappa - 1 - 2x)/\kappa$. Thus $\varphi'(x^*) < 0$ if and only if $\kappa < 1 + 2x^*$, which matches the sign of $J_{11}$ in the proof of Proposition 26.1.1: $J_{11} = x^*\varphi'(x^*)/(1 + x^*)$.
3. Explain why a prey refuge that protects a constant number of prey is stabilizing, whereas one that protects a constant proportion of prey is not.

   **Answer** With a constant-number refuge, predation acts only on $N - N_{\mathrm{r}}$, so the per capita risk of the whole prey population, $f(N - N_{\mathrm{r}})P/N$, goes to zero as $N$ falls toward $N_{\mathrm{r}}$: predation becomes strongly density dependent at low density, and the prey isocline rises steeply near $N_{\mathrm{r}}$, so that the predator isocline crosses it on a descending part. With a constant-proportion refuge, a fraction $q$ of prey is always protected, and predation becomes $f((1 - q)N)P$: this is equivalent to a smaller attack rate, which shifts the isoclines but does not change their shapes, so the stability criterion is affected only through the change in $N^*$.
4. In the Hastings–Powell model, why is the top predator's death rate $d_2$ chosen much smaller than $d_1$, and what would you expect if $z$ were removed?

   **Answer** A small $d_2$ makes the top predator a slow variable: the resource–consumer pair oscillates quickly while $z$ changes slowly and alters the parameters of that oscillation; the interplay between the fast cycle and the slow modulation is what stretches and folds trajectories into the teacup attractor. Without $z$ the system is the Rosenzweig–MacArthur model for $x$ and $y$, which is planar and therefore cannot be chaotic: with these parameters ($a_1 = 5$, $b_1 = 3$, $d_1 = 0.4$) it has an unstable equilibrium and a stable limit cycle.
5. (Open problem) Design a field experiment to decide whether a population cycle of a small mammal is driven by predators or by food.

   **Answer** The key is to manipulate each factor separately and in combination, over the whole cycle, on replicated areas large enough to contain many home ranges: (1) predator exclusion (fences, removal of specialists), (2) food supplementation or fertilization, (3) both, (4) controls; densities, survival and reproduction are monitored by mark–recapture ([7.19.8](/7.19.8)). If predators drive the cycle, exclusion should prevent the decline and keep density high; food alone should raise density without preventing the decline. Phase relations add evidence: predators should lag the prey by about a quarter cycle; if the food plants lag, food is implicated. The Kluane hare experiment (food ×3, predator exclusion ×2, both ×11) is the model; its limitation, that the combination of treatments could not be fully factorial for all measurements, shows the logistical difficulty.
