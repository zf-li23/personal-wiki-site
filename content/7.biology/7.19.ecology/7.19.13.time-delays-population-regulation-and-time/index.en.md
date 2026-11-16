---
title: Time Delays, Population Regulation and Time-Series Analysis
description: "Delayed density dependence and the delayed logistic equation (linearization, the thresholds rT = 1/e and π/2, Hopf bifurcation), discrete delays and Nicholson's blowflies; theories of population regulation and limitation; patterns of fluctuation in natural populations; autoregressive analysis of time series, Royama's diagram, population cycles and the pitfalls of testing for density dependence."
---

The logistic equation of [7.19.10](/7.19.10) assumes that a population responds instantly to its own density: the per capita growth rate at time $t$ depends on $N(t)$. Real feedbacks act with a delay. Food plants regrow over a season, eggs laid now become adults weeks later, and a predator population built up on abundant prey keeps eating after the prey has declined. This chapter asks what such delays do to population dynamics and how ecologists find out, from data, whether and how a population is regulated. Section 13.1 analyzes the delayed logistic equation completely (linearization, characteristic equation, the thresholds $rT = 1/\mathrm{e}$ and $rT = \pi/2$, and the **Hopf bifurcation** to a **limit cycle**) and its discrete-time and laboratory counterparts, extending the discrete models of [7.19.12](/7.19.12). Section 13.2 reviews the long debate on what regulates populations, Section 13.3 the patterns of fluctuation seen in nature, and Section 13.4 the statistical analysis of population time series, which connects these ideas to the population cycles of voles, hares and grouse. Predator–prey oscillations themselves are developed in [7.19.25](/7.19.25) and [7.19.26](/7.19.26), and the sudden shifts between alternative states in [7.19.39](/7.19.39).

## 13.1. Time Delays in Density Dependence

### 13.1.1. Why Delays Arise

**Density dependence** ([7.19.11](/7.19.11)) acts through resources, natural enemies or behavior, and each of these takes time to respond. Three sources of delay are common:

- Development time: recruitment to the adult stage at time $t$ reflects the conditions experienced by juveniles, born at $t - \tau$ when adults were at their density then.
- Resource recovery: grazed vegetation, depleted prey or nutrients take time to recover, so the food available now depends on consumer density in the past.
- Responses of natural enemies: specialist predators and parasitoids increase only after their prey have increased, and their impact persists after the prey declines.

**Definition 13.1.1 (Delayed Density Dependence)** *Delayed density dependence* is density dependence in which the per capita birth, death or growth rate at time $t$ depends on population density at an earlier time $t - T$ (or on densities over an interval of the past), rather than only on the current density. Density dependence acting on current density is called *direct density dependence*.

Delays have a characteristic signature: a population overshoots its equilibrium, because the brake is applied late, and then undershoots, because the brake is released late. Whether these oscillations die out or persist depends on how long the delay is relative to the speed of the response, which is what the following model makes precise.

### 13.1.2. The Delayed Logistic Equation

**Definition 13.1.2 (Delayed Logistic Equation)** The *delayed logistic equation* (Hutchinson 1948) is

$$
\frac{\mathrm{d}N}{\mathrm{d}t} = rN(t)\left(1 - \frac{N(t - T)}{K}\right),
\tag{13.1}
$$
where $r > 0$ is the **intrinsic rate of increase**, $K > 0$ the **carrying capacity** and $T > 0$ the delay with which density depresses the per capita growth rate. A solution requires an initial function $N(t) = \phi(t) > 0$ on $[-T, 0]$, not just an initial value: Eq. (13.1) is a delay differential equation, whose state at time $t$ is the whole history segment $\{N(s) : t - T \le s \le t\}$.

Two rescalings remove two parameters. With $u = N/K$ and time measured in units of $1/r$ (so $s = rt$), Eq. (13.1) becomes $\mathrm{d}u/\mathrm{d}s = u(s)\bigl(1 - u(s - a)\bigr)$ with the single dimensionless parameter $a = rT$: the delay measured in units of the natural response time $1/r$. Everything about the qualitative behavior must depend on $rT$ alone.

Positivity is preserved, since $\mathrm{d}\ln N/\mathrm{d}t = r(1 - N(t - T)/K)$ is bounded on bounded intervals; and $N^* = K$ is the only positive equilibrium. To study its stability, write $N(t) = K\bigl(1 + x(t)\bigr)$. Then $\dot x = -r\bigl(1 + x(t)\bigr)x(t - T)$, and dropping the quadratic term gives the linearized equation

$$
\dot x(t) = -r\,x(t - T).
\tag{13.2}
$$
Trying $x = \mathrm{e}^{\lambda t}$ gives the characteristic equation $\lambda = -r\mathrm{e}^{-\lambda T}$, or, with $z = \lambda T$ and $a = rT$,

$$
z\,\mathrm{e}^{z} = -a .
\tag{13.3}
$$
Unlike the characteristic polynomial of an ordinary differential equation ([2.4.11](/2.4.11#sec-11.2)), Eq. (13.3) is transcendental and has infinitely many roots; its solutions are $z = W_k(-a)$, the branches of the Lambert $W$ function. As for ordinary equations, the equilibrium is asymptotically stable if all roots have negative real part and unstable if one has positive real part (the principle of linearized stability holds for delay equations under the same smoothness conditions).

**Theorem 13.1.1 (Stability of the Delayed Logistic Equation)** Let $a = rT > 0$. Then:

1. If $0 < a \le 1/\mathrm{e}$, the dominant root of Eq. (13.3) is real and negative: perturbations of $N^* = K$ decay without oscillation (after transients).
2. If $1/\mathrm{e} < a < \pi/2$, Eq. (13.3) has no real roots, all roots have negative real part, and the dominant pair is complex: perturbations decay as damped oscillations.
3. At $a = \pi/2$ the pair $z = \pm\mathrm{i}\pi/2$ crosses the imaginary axis transversally from left to right; for $a > \pi/2$ the equilibrium is unstable. The oscillation at the threshold has angular frequency $\omega = \pi/(2T)$, that is, period $4T$.

**Proof** Write $g(z) = z\mathrm{e}^z$.

*Real roots.* For real $z$, $g'(z) = (1 + z)\mathrm{e}^z$, so $g$ decreases on $(-\infty, -1]$ from $0$ to $g(-1) = -1/\mathrm{e}$ and increases on $[-1, \infty)$. Hence $g(z) = -a$ has two negative real roots $z_2 < -1 < z_1 < 0$ if $a < 1/\mathrm{e}$, a double root $z = -1$ if $a = 1/\mathrm{e}$, and none if $a > 1/\mathrm{e}$.

*Crossings of the imaginary axis.* A root $z = \mathrm{i}y$ ($y > 0$, the conjugate case being symmetric) satisfies $\mathrm{i}y(\cos y + \mathrm{i}\sin y) = -a$, that is $y\cos y = 0$ and $y\sin y = a$. So $y = \pi/2 + k\pi$ with $\sin y > 0$, which gives $y = \pi/2, 5\pi/2, \dots$ and $a = \pi/2, 5\pi/2, \dots$. Since roots depend continuously on $a$, and as $a \to 0^+$ every root either tends to $0$ along $z \approx -a$ (the real root $z_1$) or has real part tending to $-\infty$ (because $\lvert z\rvert\mathrm{e}^{\operatorname{Re}z} = a$ forces $\mathrm{e}^{\operatorname{Re}z} \to 0$ when $\lvert z\rvert$ stays bounded away from $0$), all roots lie in the left half-plane for small $a$ and stay there until $a = \pi/2$. This proves the stability claims in 1 and 2.

*Transversality.* Differentiating $z\mathrm{e}^z = -a$ gives $(1 + z)\mathrm{e}^z\,\mathrm{d}z = -\mathrm{d}a$; using $\mathrm{e}^{z} = -a/z$,

$$
\frac{\mathrm{d}z}{\mathrm{d}a} = \frac{z}{a(1 + z)} .
$$
At $z = \mathrm{i}\pi/2$, $z/(1 + z) = (\pi^2/4 + \mathrm{i}\pi/2)/(1 + \pi^2/4)$ has positive real part, so the pair moves into the right half-plane as $a$ increases through $\pi/2$; this proves 3.

*Which root dominates for $a < 1/\mathrm{e}$.* A complex root $z = u + \mathrm{i}v$ ($v > 0$) satisfies, from the imaginary and real parts of $z\mathrm{e}^z = -a$, $u = -v\cot v$ and $a = \mathrm{e}^{u}v/\sin v$, so $\sin v > 0$ and $v \in (2k\pi, (2k + 1)\pi)$. For $k \ge 1$, $a \ge \mathrm{e}^{u}v > 2\pi\mathrm{e}^{u}$, so $u < \ln(a/2\pi) < -1 < z_1$. For $k = 0$, $a = \varphi(v) = v\,\mathrm{e}^{-v\cot v}/\sin v$, and

$$
\frac{\mathrm{d}\ln\varphi}{\mathrm{d}v} = \frac1v + \frac{v}{\sin^2v} - 2\cot v \ge \frac{2}{\sin v} - 2\cot v > 0
$$
(by the inequality of arithmetic and geometric means), so $\varphi$ increases from its limit $1/\mathrm{e}$ at $v \to 0^+$: there is no root on this branch when $a \le 1/\mathrm{e}$. Hence for $a < 1/\mathrm{e}$ every complex root has real part below $-1$, and the real root $z_1 \in (-1, 0)$ dominates. $\square$

The theorem explains why oscillation needs a delay that is long compared with the response time $1/r$. Figure 1 shows the four regimes: smooth logistic approach for $rT = 0.3$, overshoot and damped oscillation for $rT = 1$ and $1.5$, and a stable limit cycle for $rT = 2$. Figure 2 follows the roots and the long-run behavior across the bifurcation.

![Solutions of the delayed logistic equation (13.1) with N(t) = 0.1K on the initial interval, for four values of rT. A: monotone approach to K (rT < 1/e). B, C: damped oscillations, slower to decay as rT approaches π/2. D: a stable limit cycle (rT = 2 > π/2), with deep troughs and a period of about 4.4T](./plots/delayed-logistic.py)

Beyond the threshold the equation has a stable limit cycle born in a supercritical Hopf bifurcation (the general theory is in [2.4.11](/2.4.11#sec-11.6.4); for delay equations it is due to Wright 1955 and later work). Its amplitude grows rapidly with $rT$: the minimum falls to about $0.01K$ at $rT = 2.2$, so that a real population would risk extinction in the troughs (Chapter [7.19.15](/7.19.15)), and the period, $4T$ at the threshold, lengthens with $rT$ (Figure 2C). Two biological conclusions follow. First, stability is lost not by a long delay as such but by a long delay combined with a fast response: halving $r$ (slower breeders) is as stabilizing as halving $T$. Second, the period of a delay-driven cycle is roughly four delays. Applied to Nicholson's blowflies (Section 13.1.4), whose cycles last about 38 days, this suggests a delay of about 9 days, and the large amplitude of their cycles requires $rT$ well above $\pi/2$ (May 1973).

![The delayed logistic equation across the Hopf bifurcation. A: roots z = λT of z e^z = -rT for five values of rT (the seven branches k = -3, …, 3 of the Lambert W function); the dominant roots move right and cross the imaginary axis at ±iπ/2 when rT = π/2. B: long-run maximum and minimum of N/K in simulations: a stable equilibrium up to rT = π/2, then a limit cycle whose amplitude grows quickly and whose troughs approach zero. C: period in units of T, from the dominant complex root (damped region, curve) and from the simulated cycles (points); it equals 4T at the threshold](./plots/hutchinson-bifurcation.py)

### 13.1.3. Delays in Discrete Time

Populations with discrete generations can also respond to density with a delay, for instance when the food available in one breeding season depends on grazing in the previous one. Begon's example is cattle on a pasture whose spring growth is set by last year's grazing.

**Proposition 13.1.2 (Delayed Discrete Logistic Model)** Let $N_{t+1} = N_t\bigl[1 + r(1 - N_{t-1}/K)\bigr]$ with $r > 0$. The equilibrium $N^* = K$ is approached monotonically if $0 < r < 1/4$, through damped oscillations if $1/4 < r < 1$, and is unstable for $r > 1$, where the population oscillates persistently.

**Proof** Put $N_t = K(1 + x_t)$; to first order $x_{t+1} = x_t - rx_{t-1}$, whose characteristic equation is $z^2 - z + r = 0$. For $r < 1/4$ the roots $\tfrac12(1 \pm \sqrt{1 - 4r})$ are real and lie in $(0, 1)$. For $r > 1/4$ they are complex conjugates with $\lvert z\rvert^2 = z\bar z = r$, so they lie inside the unit circle exactly when $r < 1$. $\square$

At $r = 1$ the complex pair leaves the unit circle with argument $\theta = \arccos(1/2) = \pi/3$, so the oscillation that appears (in a Neimark–Sacker bifurcation, the discrete analog of the Hopf bifurcation) has a period of about $2\pi/\theta = 6$ generations, and it is quasi-periodic rather than periodic: the population moves around an invariant closed curve in the $(N_{t-1}, N_t)$ plane. The same reasoning applied to the delayed Beverton–Holt model $N_{t+1} = RN_t/(1 + aN_{t-1})$, with $a = (R - 1)/K$, gives $x_{t+1} = x_t - c\,x_{t-1}$ with $c = (R - 1)/R$. Since $0 < c < 1$ for every $R > 1$, this model can show damped oscillations (when $R > 4/3$) but never loses stability. Without the delay the Beverton–Holt model approaches equilibrium monotonically for every $R$ ([7.19.12](/7.19.12)); the delay alone has created the oscillations. The thresholds quoted in some textbooks for this class of models ($0.25$ and $1$) are the values of the coefficient of the delayed term.

![The delayed discrete logistic model. A: trajectories for r = 0.2 (monotone), 0.6 (damped oscillations) and 1.05 (persistent quasi-periodic oscillations with a period near 6 generations). B: modulus of the dominant root of z^2 - z + r = 0: real roots below r = 1/4, a complex pair of modulus √r above, leaving the unit circle at r = 1. The delayed Beverton–Holt model has the same characteristic equation with c = (R - 1)/R, which always lies in the shaded interval, so it can oscillate but is always stable](./plots/discrete-delay.py)

### 13.1.4. Nicholson's Blowflies

The classic laboratory demonstration of delay-driven cycles is A. J. Nicholson's work (1954, 1957) on the sheep blowfly *Lucilia cuprina*. When adults were given a limited daily ration of protein (needed for egg production) while larvae had ample food, the adult population cycled with a period of about 35–40 days, collapsing almost to zero and then rising to several thousand. Adults crowded at high density laid few eggs; when the adults then died, few new adults emerged two weeks later, the survivors had plenty of protein and laid many eggs, and so on. The delay is the development time from egg to adult, about 15 days at the culture temperature.

The Hutchinson equation reproduces the period but not the shape of these cycles. Gurney, Blythe and Nisbet (1980) proposed a model that separates recruitment from death:

$$
\frac{\mathrm{d}A}{\mathrm{d}t} = P\,A(t - \tau)\,\mathrm{e}^{-A(t - \tau)/A_0} - \delta A(t),
\tag{13.4}
$$
where $A$ is the number of adults, $\tau$ the development time, $P$ the maximum per capita rate of egg production (times survival to adulthood), $A_0$ the adult density at which recruitment is greatest, and $\delta$ the adult death rate. The recruitment term is a delayed Ricker function ([7.19.12](/7.19.12)): it is hump-shaped, so recruitment overcompensates, and crowding of adults reduces the recruitment a development time later. The positive equilibrium is $A^* = A_0\ln(P/\delta)$, which exists when $P > \delta$. Linearizing as before, with $A = A^*(1 + x)$,

$$
\dot x(t) = -\delta x(t) + \delta\bigl(1 - \ln(P/\delta)\bigr)x(t - \tau),
$$
whose characteristic equation $\lambda + \delta = \delta(1 - \ln(P/\delta))\mathrm{e}^{-\lambda\tau}$ shows that stability depends on the two dimensionless groups $P/\delta$ (how strongly recruitment overcompensates) and $\delta\tau$ (how many adult lifetimes fit into one delay). For values of the magnitude estimated from Nicholson's cultures ($\tau \approx 15$ d, $P \approx 8\,\mathrm{d}^{-1}$, $\delta \approx 0.18\,\mathrm{d}^{-1}$) the equilibrium is unstable and the model settles on a cycle of about $2.7\tau \approx 40$ days, close to the observed period (Figure 4). The deep troughs follow from overcompensation, not from the delay alone: high adult numbers $\tau$ days earlier mean low recruitment now.

![The Gurney–Blythe–Nisbet model (13.4) of Nicholson's blowflies with τ = 15 d, P = 8 per day, δ = 0.175 per day and A0 = 600. A: the adult population settles on a cycle with a period of about 40 days (2.7 development times), with a shoulder on the rising limb and a long trough. B: the cycle in delay coordinates, adults now against adults τ days earlier](./plots/blowfly-model.py)

## 13.2. Population Regulation

### 13.2.1. Regulation, Limitation and Determination

No natural population grows without bound, and few decline steadily to extinction; most fluctuate within limits. Whether these limits reflect stabilizing forces within the population or merely the irregular action of the environment was the central controversy of population ecology in the middle of the twentieth century. Nicholson (1933, 1954), working on blowflies and parasitoids, argued that density-dependent biotic interactions (competition, predation, parasitism) hold populations in balance with their environment, while density-independent factors such as weather may strongly affect density but cannot by themselves keep it within bounds. Andrewartha and Birch (1954), working on insect pests in Australia, saw populations as passing through repeated setbacks and recoveries: thrips on roses in South Australia, for example, increased each spring and were cut back each summer by drought before they reached the limits of their food supply, and the timing and severity of the weather explained most of the variation in their numbers. They also rejected the division of the environment into density-dependent and density-independent "factors".

Much of the dispute dissolves once two questions are separated.

**Definition 13.2.1 (Population Regulation)** *Population regulation* is the tendency of a population to decrease when it is above a particular level and to increase when it is below it; it can only arise from density-dependent processes acting on birth, death or movement. *Population limitation* refers to the processes that set the level (the equilibrium density or the average density) around which a population fluctuates; the level and the actual abundance at any time are *determined* by all processes affecting the population, density dependent or not.

Figure 6A shows the distinction. The birth rate declines with density and so regulates the population at every site; the death rate is density independent but differs between three sites because of physical conditions. Each site has a stable equilibrium, but the equilibrium densities differ because of the density-independent factor. Nicholson's school was concerned with regulation, Andrewartha and Birch's with determination, and both are valid. Regulation need not act all the time: density dependence may operate only intermittently (when food runs short in a dense year), and it may draw the population toward a target that itself moves, for example with the seasons. It is unlikely that any natural population is ever at equilibrium.

### 13.2.2. Extrinsic Theories

The classical theories are often grouped by whether they emphasize factors outside or inside the population.

- The climatic school (Bodenheimer 1928, Uvarov 1931, Andrewartha and Birch 1954), mostly entomologists, held that population size is limited mainly by the short periods during which weather is favorable for increase: insect populations rarely have enough time to reach the limits of their resources, so food competition seldom occurs.
- The biotic school (Howard and Fiske 1911, Nicholson 1933, Smith 1935, who coined the term "density-dependent factor") held that predation, parasitism, competition and disease, which intensify with density, determine the equilibrium level. A variant, the nutrient-recovery hypothesis, places the decisive delay in the recovery of food quality after heavy grazing.
- The compromise school (Milne 1957 and others) held that density-independent factors predominate when the population is at intermediate densities, and density-dependent intraspecific competition comes into play only at the extremes of very high density (and, in some versions, density-independent factors dominate in unfavorable habitats, biotic factors in favorable ones).

### 13.2.3. Self-Regulation Theories

The intrinsic theories hold that changes in the individuals themselves, triggered by density, regulate abundance.

- Behavioral regulation (Wynne-Edwards 1962). Social hierarchy and territoriality convey information about population size relative to resources. As density rises, favorable sites are all occupied by **territory** holders, and subordinate individuals are relegated to poor habitat, where they have low survival and breeding success, or emigrate. The demographic part of this argument is well supported: territoriality can produce strong density dependence, since the number of breeders is capped by the number of territories ([7.18.26](/7.18.26)). Wynne-Edwards's further claim, that animals restrain their reproduction for the good of the group, requires group selection and was rejected by Williams (1966) and Maynard Smith (1964): individuals that "cheat" by reproducing maximally would spread.
- Endocrine regulation (Christian 1950s). In crowded mammals, social stress increases the secretion of adrenocorticotropic hormone and glucocorticoids and reduces gonadotropins and growth hormone, lowering reproduction and resistance to disease. It was proposed to explain cycles in small mammals. Stress hormones are indeed elevated and depress fecundity in peak and declining populations, but in snowshoe hares the stress is caused mainly by predation risk rather than by crowding (Section 13.4.4).
- Genetic regulation (Chitty 1960, 1967). Two kinds of genotype differ in their behavior and reproduction: aggressive, less fecund types that do well at high density and docile, fecund types that do well at low density. Selection favors the fecund type while the population increases and the aggressive type at the peak, which reduces recruitment and so causes the decline; the population changes in quality as well as in number, with a lag of a generation. The "Chitty effect", that individuals are larger in the increase and peak phases of a vole cycle, is real, but no consistent heritable polymorphism of this kind has been found.

These intrinsic mechanisms are now seen as part of the explanation of how density dependence operates, not as alternatives to extrinsic factors: what appears intrinsic, such as stress, is often induced by extrinsic causes such as predators.

### 13.2.4. Where Density Dependence Acts

A comparison of many life tables (Sinclair 1989) suggests that the stage at which density-dependent mortality or reduced fecundity occurs, and its main causes, differ predictably between groups:

| Group | Stage where density dependence acts | Main causes |
|---|---|---|
| Insects | early larval stages; fecundity of adults | competition for food, predation and parasitism (in social insects also social interactions) |
| Fish | early juvenile (larval and fry) stages | food and predation |
| Birds | late juveniles, after fledging; recruitment to the breeding population | food, competition for territories |
| Small mammals | late juveniles, at independence from the mother | space and social behavior (dispersal, territoriality) |
| Large mammals | early juveniles; fecundity of females | food |

**Key factor analysis** ([7.19.9](/7.19.9)) is the classical method for locating such stages in a series of life tables, and λ-contribution analysis weights each stage by the sensitivity of the growth rate ([7.19.14](/7.19.14)).

### 13.2.5. Multiple Equilibria

A population may be regulated at different levels by different processes. The classic example is the spruce budworm *Choristoneura fumiferana* in the boreal forests of eastern Canada, which persists for decades at low densities and then erupts and defoliates whole forests. Ludwig, Jones and Holling (1978) modeled the budworm density $B$ as

$$
\frac{\mathrm{d}B}{\mathrm{d}t} = r_BB\left(1 - \frac{B}{K_B}\right) - \beta\frac{B^2}{\alpha^2 + B^2},
$$
logistic growth on foliage minus predation by birds with a saturating sigmoid (type III) **functional response** ([7.19.25](/7.19.25)). With $u = B/\alpha$, $\tau = \beta t/\alpha$, $r = r_B\alpha/\beta$ and $q = K_B/\alpha$, the equilibria $u > 0$ satisfy $r(1 - u/q) = u/(1 + u^2)$: a straight line (per capita growth) meets a hump-shaped curve (per capita predation). For small $q$ (young forest) there is one low equilibrium, held by predators; for large $q$ (mature forest with much foliage) only an outbreak equilibrium held by food; for intermediate $q$, three equilibria, two stable and one unstable between them (Figure 6B). As the forest matures and $q$ grows, the endemic equilibrium disappears in a saddle-node bifurcation and the population jumps to the outbreak state; it returns only after the foliage has been destroyed. A similar pattern appears in the Serengeti, where migratory wildebeest (about 1.3 million) are regulated by food, while resident populations of the same species are held at much lower densities by predators (Fryxell, Greever and Sinclair 1988): migration lets the migrants escape predator regulation. Alternative stable states and their consequences are treated in [7.19.39](/7.19.39).

![A: regulation and determination. The per capita birth rate falls with density; the death rate is density independent but differs between three sites. Each site has a stable equilibrium (N1*, N2*, N3*): density dependence regulates all three, the density-independent factor determines the level. B: the spruce budworm model in dimensionless form. Lines: per capita growth r(1 - u/q) for r = 0.55 and three values of q; curve: per capita predation u/(1 + u^2). Filled points are stable equilibria, open points unstable. For q = 9 an endemic and an outbreak equilibrium coexist](./plots/regulation-determination.py)

## 13.3. Patterns of Fluctuation in Natural Populations

Long-term counts show a range of patterns, which can be classified as follows; a given population may show different patterns in different places or periods.

- Seasonal fluctuations: species with several generations a year or with seasonal breeding change in abundance with the seasons, driven by seasonal conditions and by their own life cycle. Phytoplankton in temperate lakes peaks in spring, when light increases and nutrients mixed up in winter are still available, and often again in autumn; many insects, such as cotton mirid bugs in northern China, have one or two peaks a year whose timing depends on rainfall.
- Irregular fluctuations: many insect pests, such as pine caterpillars (*Dendrolimus*) and the East Asian migratory locust (*Locusta migratoria manilensis*), vary irregularly from year to year, largely in response to weather: locust outbreaks in the river valleys of eastern China historically followed droughts that exposed lake and river beds as breeding grounds.
- Cyclic fluctuations: a few populations fluctuate with a regular period: lemmings and voles in the Arctic and boreal zone with periods of 3–5 years, snowshoe hares and their predators in the boreal forest of North America with about 10 years, red grouse in Britain with 4–8 years, and the larch budmoth in the Alps with 8–9 years. The fur returns of the Hudson's Bay Company show the hare and lynx cycle since the early nineteenth century; hares also cycle where lynx are absent, so the lynx cannot be the sole cause.
- Outbreaks: species with high reproductive rates and irregular or cyclic dynamics occasionally erupt to very high densities when conditions are favorable or natural enemies are scarce: locusts, rodents, defoliating insects and algal blooms (red tides). Introduced species often erupt after a lag, as the floating fern *Salvinia molesta* did on Lake Kariba after the dam was closed in 1959 (invasions are treated in [7.19.51](/7.19.51)).
- Relative constancy: some populations remain at nearly the same level for long periods: many large ungulates and carnivores, some dragonflies and social insects with strong internal regulation. Constancy reflects strong direct density dependence, long life and buffering by stored reserves or age structure.
- Decline and extinction: populations decline when conditions deteriorate or human impacts increase; more than 99 % of the species that have ever existed are extinct. The stochastic processes that make small populations vulnerable are the subject of [7.19.15](/7.19.15).

Which pattern a population shows depends on the balance between direct and delayed density dependence, the strength of density-independent variation and the speed of the population's response, as Sections 13.1 and 13.4 make precise.

## 13.4. Detecting Density Dependence in Time Series

### 13.4.1. Autoregressive Models

Long series of counts are the most widely available data on abundance, and a large body of work has tried to infer the structure of density dependence from them (Royama 1992, Turchin 2003). Let $X_t = \ln N_t$ and $r_t = X_t - X_{t-1}$, the realized per capita growth rate on the log scale.

**Definition 13.4.1 (Autoregressive Model of Population Dynamics)** In the linear autoregressive model of order $d$ the growth rate depends linearly on past log abundances:

$$
r_t = \beta_0 + \beta_1X_{t-1} + \beta_2X_{t-2} + \cdots + \beta_dX_{t-d} + u_t,
\tag{13.5}
$$
where $u_t$ are independent density-independent perturbations with mean 0 and variance $\sigma^2$. The coefficient $\beta_1$ measures direct density dependence and $\beta_2, \dots, \beta_d$ delayed density dependence at lags $2, \dots, d$; regulation is reflected in negative $\beta$'s, and $\beta_0$ sets the mean level but not the dynamics. Equivalently, $X_t = \beta_0 + (1 + \beta_1)X_{t-1} + \beta_2X_{t-2} + \cdots + \beta_dX_{t-d} + u_t$, an autoregressive process for $X_t$. The number of lags $d$ is the *order* (or dimension) of the dynamics.

For $d = 1$ this is the stochastic Gompertz model: $X_t - X^* = (1 + \beta_1)(X_{t-1} - X^*) + u_t$, which is regulated (stationary) when $-2 < \beta_1 < 0$ and approaches equilibrium with alternating overshoots when $\beta_1 < -1$. Order 2 is the simplest model that produces cycles, and it fits many cyclic populations.

**Proposition 13.4.1 (Royama's Diagram)** The order-2 model $X_t = \beta_0 + (1 + \beta_1)X_{t-1} + \beta_2X_{t-2} + u_t$ is stationary (regulated) if and only if

$$
\beta_2 > -1, \qquad \beta_1 + \beta_2 < 0, \qquad \beta_2 - \beta_1 < 2 ,
$$
a triangle in the $(\beta_1, \beta_2)$ plane. Within it, the dynamics are cyclic (the autocorrelation function oscillates) when $\beta_2 < -\tfrac14(1 + \beta_1)^2$, with period

$$
T_{\mathrm{c}} = \frac{2\pi}{\theta}, \qquad \cos\theta = \frac{1 + \beta_1}{2\sqrt{-\beta_2}} .
$$

**Proof** The deterministic part has characteristic equation $z^2 - a_1z - a_2 = 0$ with $a_1 = 1 + \beta_1$, $a_2 = \beta_2$, and the process is stationary if and only if both roots lie inside the unit circle. If the roots $z_1, z_2$ are complex, $\lvert z_1\rvert^2 = z_1z_2 = -a_2$, so the condition is $a_2 > -1$. If they are real, both lie in $(-1, 1)$ if and only if $p(z) = z^2 - a_1z - a_2$ is positive at $z = \pm1$ and the product $-a_2$ of the roots is below 1: $p(1) = 1 - a_1 - a_2 > 0$, $p(-1) = 1 + a_1 - a_2 > 0$ and $a_2 > -1$. These three inequalities also hold in the complex case with $a_2 > -1$ (then $p > 0$ on the whole real line), so they characterize stationarity; in terms of $\beta$ they read as stated. The roots are complex when the discriminant $a_1^2 + 4a_2 < 0$; then $z_{1,2} = \sqrt{-a_2}\,\mathrm{e}^{\pm\mathrm{i}\theta}$ with $2\sqrt{-a_2}\cos\theta = z_1 + z_2 = a_1$, and the autocorrelation function is a damped cosine with angular frequency $\theta$ per time step. $\square$

The diagram (Figure 7A) carries a simple biological message. Populations without delayed density dependence ($\beta_2 \ge 0$) do not cycle. Negative $\beta_2$ produces cycles, and their period increases as delayed density dependence becomes stronger (more negative $\beta_2$) and, especially, as direct density dependence becomes weaker ($\beta_1$ closer to 0). With $\beta_1 = -1$ (strong direct density dependence) the period is 4 steps; with $\beta_1 = -0.2$ and $\beta_2 = -0.6$ it is about 6.

![Order-2 autoregressive dynamics of log abundance. A: Royama's diagram. Inside the triangle the process is stationary; below the parabola β2 = -(1 + β1)^2/4 it cycles, with periods shown by the contours (in time steps). B: simulated series for the two marked points (process noise SD 0.3): strong direct density dependence gives a period of 4 years, weak direct density dependence a period of about 6 years. C: autocorrelation (bars) and partial autocorrelation (points) of the second series, with approximate 95 % limits ±2/√n; the oscillating ACF reveals the cycle, and the PACF is negligible beyond lag 2](./plots/ar2-royama.py)

### 13.4.2. Correlation Functions and the Order of the Dynamics

The analysis of a series usually proceeds in three steps.

1. The *autocorrelation function* (ACF), the correlation between $X_t$ and $X_{t-k}$ as a function of the lag $k$, reveals periodicity: a peak at lag $k$ and a trough near $k/2$ indicate a cycle of period $k$. For the larch budmoth *Zeiraphera diniana* in the Engadine valley of Switzerland the ACF peaks at lag 9, a "nine-year cycle".
2. The *partial autocorrelation function* (PACF), the correlation between $X_t$ and $X_{t-k}$ after removing the linear effect of the intermediate lags, indicates the order: for an autoregressive process of order $d$ the PACF vanishes beyond lag $d$. For the budmoth it is large and negative at lag 2 and negligible beyond.
3. The *partial rate correlation function* (PRCF, Berryman and Turchin 2001) correlates the growth rate $r_t$, not $X_t$, with $X_{t-k}$. At lag 1 the PACF of $X_t$ is positive in almost any series, simply because successive values are similar; the PRCF at lag 1 instead estimates direct density dependence ($\beta_1$), which is the quantity of interest. For the budmoth it shows both direct and delayed density dependence.

Applied to 19 series of voles and lemmings from Fennoscandia, the analysis selected order 2 in nearly every case (Bjørnstad, Falck and Stenseth 1995). Delayed density dependence ($\beta_2$) was strong everywhere and did not vary with latitude, but direct density dependence ($\beta_1$) weakened toward the north; by Proposition 13.4.1 this predicts the observed lengthening of the cycles from about 3 years in southern Finland to about 5 years in northern Fennoscandia. For the hare–lynx system, Stenseth et al. (1997) found the best model for the hare series to have three lags (hares, their food and their predators) and the lynx series two (lynx and hares), in agreement with the structure of the boreal food web. The number of lags is thus a clue to the number of interacting components that drive a population, although the statistical structure does not by itself identify the biological mechanism.

The approach extends naturally to covariates. For two kangaroo rats in the Chihuahuan Desert, Lima et al. (2008) fitted models with direct density dependence plus summer and winter rainfall and the abundance of a competitor, estimated them on data up to 1992 and tested them on later years; the model with both summer rainfall and interspecific competition predicted best. Combining density dependence with weather in a single regression makes the old dichotomy between density-dependent and density-independent factors explicit and testable.

### 13.4.3. Statistical Pitfalls

Regressing $r_t$ on $X_{t-1}$ and testing whether the slope is negative is the simplest test for density dependence, but it is treacherous.

- Bias under the null hypothesis: even for a random walk ($\beta_1 = 0$, no regulation), the least squares slope estimated from a short series is biased downward, because $X_{t-1}$ and the subsequent growth rate are not independent when the level is estimated from the same data; ordinary $t$-tests therefore reject the null hypothesis too often. Tests designed for this situation use the distribution of the slope under a random walk: Bulmer (1975), the randomization test of Pollard, Lakhani and Rothery (1987) and the parametric bootstrap likelihood-ratio test of Dennis and Taper (1994). The problem is the same as testing for a unit root in econometrics.
- Sampling error: abundance is estimated, not counted exactly. If $Y_t = X_t + \varepsilon_t$ with independent errors, an overestimate of $X_t$ produces both a high value of the predictor and a low subsequent growth rate, so the observed slope is negative even when there is no density dependence at all (Figure 8). State-space models that separate process noise from observation error are the remedy (Freckleton et al. 2006).
- Short series and low power: most series are a few decades long; density dependence that is real but weak, or that acts only at high density, is easily missed, and the order of the dynamics is often underestimated.
- Correlation is not mechanism: a negative slope shows that growth rate falls with density, not why. Delayed density dependence may come from predators, food or maternal effects, and the same statistical structure is consistent with several mechanisms. Field experiments (adding food, removing predators) are needed to identify causes.
- Moving targets: if the carrying capacity changes over time (a trend in habitat, seasonal forcing), a regression on density alone confounds regulation with environmental change.

![Testing for density dependence by regressing r_t = ln(N_t+1/N_t) on ln N_t (simulated 30-year series). A: a regulated population (Gompertz model, β1 = -0.3) gives a negative slope. B: an unregulated random walk observed with sampling error (SD 0.3 on the log scale) gives an even steeper negative slope. C: slopes estimated from 2000 replicate series: the random walk without error is already biased below zero, sampling error makes the bias severe, and the regulated population cannot be distinguished from the unregulated one observed with error](./plots/density-dependence-tests.py)

### 13.4.4. Population Cycles

Regular cycles have attracted ecologists since Elton (1924), partly because cyclic populations span a wide range of densities and therefore give good power to detect density-dependent effects. The analyses above agree that cycles require a combination of direct and delayed density dependence; what supplies the delay differs between systems and remains debated.

- Red grouse (*Lagopus lagopus scoticus*) in Britain. One hypothesis emphasizes the parasitic nematode *Trichostrongylus tenuis*, which reduces breeding success; treating grouse with anthelmintics reduced the amplitude of the crashes (Hudson, Dobson and Newborn 1998) but did not abolish cycles everywhere. The other emphasizes territorial behavior: in experiments, testosterone implants that increased the aggressiveness of established males reduced the recruitment of young males in that year and the next, a delayed density-dependent effect (Mougeot et al. 2003), possibly mediated by the breakdown of clusters of related males as density rises. Parasites and aggressiveness interact, and both probably contribute.
- Snowshoe hares (*Lepus americanus*) in the boreal forest. Most hares die from predation, and field experiments at Kluane Lake, Yukon, showed that excluding mammalian predators had a larger effect on hare survival than adding food, with the largest effect when both were combined. Fecundity remains low for two or more years after the peak, even when predators have declined and food is plentiful. The delay is supplied by stress: predator exposure raises the glucocorticoid levels of pregnant hares, which reduces litter size, and the effect passes to their daughters, a maternal effect that prolongs the low phase (Sheriff, Krebs and Boonstra 2009). The lynx follows the hares with a lag of about a year.
- Voles and lemmings: in Fennoscandia the specialist predation hypothesis (Hanski, Turchin and others) holds that weasels, which reproduce under the snow and respond to vole density with a delay, supply the delayed density dependence, while generalist predators (foxes, raptors), more abundant in the south, add direct density dependence that damps the cycles. Parameterized with field data, the model reproduces the increase in period and amplitude with latitude and the absence of cycles in the south. Elsewhere it fails: field voles in Kielder Forest, northern England, cycle although generalist predation should prevent it, and reducing weasels by about 60 % did not stop the cycles (Graham and Lambin 2002). For lemmings, overgrazing of slowly regrowing mosses may supply the delay, and for grass-eating voles the induction of silica defenses in grasses has been proposed.

The general lesson is that the process that makes a population cycle need not be the process that sets the amplitude of the cycle, and that intrinsic changes (stress, behavior, body size) usually explain how the population responds while extrinsic factors (predators, food) explain why. Predator–prey models of cycles are developed in [7.19.25](/7.19.25) and [7.19.26](/7.19.26), and host–parasitoid models in [7.19.27](/7.19.27).

## Summary

- Density dependence often acts with a delay (development time, resource recovery, responses of natural enemies); delayed density dependence causes overshoot and undershoot (Definition 13.1.1).
- The delayed logistic equation (13.1) depends only on $rT$. Linearization gives the characteristic equation $z\mathrm{e}^z = -rT$, Eq. (13.3), and Theorem 13.1.1:

  | $rT$ | Dominant roots | Dynamics near $K$ |
  |---|---|---|
  | $(0, 1/\mathrm{e}]$ | real, negative | monotone approach |
  | $(1/\mathrm{e}, \pi/2)$ | complex, $\operatorname{Re} < 0$ | damped oscillations |
  | $\pi/2$ | $\pm\mathrm{i}\pi/2$ | Hopf bifurcation, period $4T$ |
  | $> \pi/2$ | $\operatorname{Re} > 0$ | stable limit cycle, deep troughs |

- In discrete time, $N_{t+1} = N_t[1 + r(1 - N_{t-1}/K)]$ is monotone for $r < 1/4$, damped for $1/4 < r < 1$ and oscillates persistently for $r > 1$ (Proposition 13.1.2); the delayed Beverton–Holt model oscillates but never loses stability. Nicholson's blowflies cycle with a period of about 2.7 development times; the Gurney–Blythe–Nisbet model (13.4) combines the delay with overcompensating recruitment.
- Regulation (density-dependent return toward a level) differs from limitation and determination (what sets the level and the actual abundance) (Definition 13.2.1). The classical theories (climatic, biotic, compromise; behavioral, endocrine, genetic self-regulation) emphasize different parts of the same process. Where density dependence acts differs predictably between taxa, and populations may have several equilibria (spruce budworm, migratory and resident wildebeest).
- Natural populations show seasonal, irregular and cyclic fluctuations, outbreaks, relative constancy, decline and extinction.
- Autoregressive models of log abundance (Definition 13.4.1) quantify direct ($\beta_1$) and delayed ($\beta_2$) density dependence; Royama's diagram (Proposition 13.4.1) shows that cycles need $\beta_2 < -\frac14(1 + \beta_1)^2$ and lengthen as direct density dependence weakens, which explains the latitudinal gradient in vole cycles. ACF, PACF and PRCF reveal period and order.
- Regression tests for density dependence are biased in short series and by sampling error; randomization, bootstrap and state-space methods, and above all field experiments, are needed.
- Cycles of grouse, hares and voles require direct and delayed density dependence, supplied by different mechanisms (parasites and territorial behavior, predation-induced stress with maternal effects, specialist predators or food).

## Questions

1. Show that the period of the oscillation of the delayed logistic equation at the Hopf threshold is $4T$, and explain intuitively why a delay $T$ produces a cycle of about four delays.

   **Answer** At $rT = \pi/2$ the dominant roots are $\lambda = \pm\mathrm{i}\pi/(2T)$ (Theorem 13.1.1), so the solution of the linearized equation is $\cos(\pi t/(2T) + \phi)$, with period $2\pi/(\pi/(2T)) = 4T$. Intuitively, the growth rate $\dot x(t) = -rx(t - T)$ is proportional to the deviation a delay earlier. In a sinusoidal oscillation the growth rate is a quarter period ahead of the deviation; so the deviation $T$ earlier must equal the negative of the deviation a quarter period ahead, which happens when $T$ is a quarter of the period.

2. A population of a small mammal with $r = 1.2\,\mathrm{yr}^{-1}$ is limited by a food plant that recovers from grazing with a delay of about 1 year. Use the delayed logistic equation to predict its dynamics. How would the prediction change for a large herbivore with $r = 0.2\,\mathrm{yr}^{-1}$ and the same delay?

   **Answer** For the small mammal $rT = 1.2$, between $1/\mathrm{e}$ and $\pi/2$: damped oscillations about $K$, with a period of $2\pi/\operatorname{Im}z$ delays; numerically the dominant root of $z\mathrm{e}^z = -1.2$ is $z \approx -0.19 \pm 1.44\mathrm{i}$, giving a period of $2\pi/1.44 \approx 4.4$ years and a decay of the amplitude by a factor $\mathrm{e}^{-0.19} \approx 0.83$ per year. Environmental noise would keep exciting these oscillations, so the population would show irregular quasi-cycles. For the large herbivore $rT = 0.2 < 1/\mathrm{e}$: monotone approach, no oscillations. Slow responders are stabilized by their slowness even with the same delay.

3. Prove that for the delayed Beverton–Holt model $N_{t+1} = RN_t/(1 + aN_{t-1})$ the equilibrium is locally stable for every $R > 1$, and find when the approach is oscillatory.

   **Answer** The equilibrium satisfies $1 + aN^* = R$. With $N_t = N^*(1 + x_t)$, $1 + aN^*(1 + x_{t-1}) = R(1 + c\,x_{t-1})$ where $c = aN^*/R = (R - 1)/R$, so $x_{t+1} \approx x_t - c\,x_{t-1}$. The characteristic equation $z^2 - z + c = 0$ has real roots in $(0, 1)$ if $c < 1/4$, that is $R < 4/3$ (monotone approach), and complex roots of modulus $\sqrt c < 1$ if $R > 4/3$ (damped oscillations). Since $c < 1$ for all $R$, the equilibrium is always stable.

4. A 40-year series of log counts of a vole population gives the estimates $\hat\beta_1 = -0.3$ and $\hat\beta_2 = -0.7$ in model (13.5) with $d = 2$. Is the population cyclic, and with what period? A second population further south gives $\hat\beta_1 = -1.1$, $\hat\beta_2 = -0.7$. Interpret the difference.

   **Answer** First population: $a_1 = 0.7$, $a_2 = -0.7$; the triangle conditions hold ($\beta_2 > -1$, $\beta_1 + \beta_2 = -1 < 0$, $\beta_2 - \beta_1 = -0.4 < 2$), and $a_1^2 + 4a_2 = 0.49 - 2.8 < 0$, so it cycles, with $\cos\theta = 0.7/(2\sqrt{0.7}) = 0.418$, $\theta = 1.140$ and a period of $2\pi/1.140 \approx 5.5$ years. Second population: $a_1 = -0.1$, $\cos\theta = -0.1/(2\sqrt{0.7}) = -0.060$, $\theta = 1.631$, a period of about 3.9 years. Delayed density dependence is the same, but the southern population has much stronger direct density dependence, which shortens the cycle: the pattern found in Fennoscandian voles and attributed to generalist predators.

5. Why might a regression of $\ln(N_{t+1}/N_t)$ on $\ln N_t$ from annual counts suggest density dependence where there is none? Describe two ways to guard against this conclusion.

   **Answer** Two reasons: in short series the least squares slope is biased below zero even for a random walk, and sampling error in the counts induces a negative correlation between the predictor and the subsequent growth rate (an overestimate inflates $\ln N_t$ and deflates $\ln(N_{t+1}/N_t)$). Guards: compare the observed slope with its distribution under a random walk (randomization test of Pollard et al., parametric bootstrap of Dennis and Taper); fit state-space models with separate process and observation error, using independent estimates of sampling variance; and, best, test the mechanism by experiment, for example by manipulating density or resources.

6. (Open question) Andrewartha and Birch argued that the thrips on roses in their garden were never regulated. Design an analysis or experiment that could distinguish "no regulation" from "regulation that acts only occasionally".

   **Answer** Key points: regulation that acts occasionally shows up as density dependence that appears only at high density or in particular seasons, so a single linear regression over all years may miss it. One could fit models in which the growth rate depends on density and weather with an interaction (density dependence switched on when food or space becomes limiting), and test these against a model with weather alone. Experimentally, one could add thrips to some roses and remove them from others at the start of the season and follow per capita survival and reproduction: regulation predicts that the treatments converge; pure density independence predicts that differences persist. Long-term boundedness itself is evidence that some density dependence must act at least sometimes, since a random walk would eventually wander to extinction or explosion.
