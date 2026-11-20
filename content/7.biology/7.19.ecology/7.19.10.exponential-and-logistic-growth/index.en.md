---
title: Exponential and Logistic Growth
description: "Density-independent growth: geometric growth, exponential growth, λ = e^r, doubling time, human population growth and the demographic transition; the logistic equation derived from density-dependent birth and death, its solution, phases, phase-line stability and a Lyapunov function; θ-logistic and Gompertz models; strong and weak Allee effects, bistability and the saddle-node collapse; fitting growth curves by nonlinear and linearized least squares; numerical solution; significance and limits of the logistic model."
---

The simplest question about a population is how its size changes with time when nothing but its own size matters. Two answers frame all of population ecology. If every individual has the same chances of reproducing and dying regardless of how many others there are, the population grows (or declines) exponentially. If those chances worsen as the population becomes crowded, growth slows and the population approaches a ceiling set by its environment, the carrying capacity; the logistic equation is the simplest model of this. This chapter develops both models and their generalizations, analyzes their equilibria and stability with the phase line, shows how strong positive density dependence at low numbers (the Allee effect) creates thresholds and sudden collapses, and fits growth curves to data. It uses the demographic quantities of the previous chapter (7.19.9): the finite and intrinsic rates of increase come from life tables. Density dependence itself, its forms and its measurement are the subject of 7.19.11; populations with discrete generations, whose dynamics can be far more complex than the smooth curves here, are the subject of 7.19.12; and delayed responses to density follow in 7.19.13. The mathematics of first-order equations is in [2.2.15](/2.2.15) and that of stability in [2.4.11](/2.4.11); we do not repeat it, but the ecological analysis is given in full.

## 10.1. Density-Independent Growth

### 10.1.1. Geometric Growth

Many annual plants and insects breed once a year and die, so that generations do not overlap. If each individual of generation $t$ leaves on average $\lambda$ individuals in generation $t + 1$, independently of the size of the population, and there is no migration,

$$
N_{t+1} = \lambda N_t, \qquad N_t = N_0\lambda^t. \tag{10.1}
$$

**Definition 10.1.1 (Finite Rate of Increase)** The **finite rate of increase** $\lambda = N_{t+1}/N_t$ is the factor by which a population multiplies in one unit of time (for discrete generations, one generation, when $\lambda$ equals the net reproductive rate $R_0$ of 7.19.9). Growth according to Eq. (10.1) with constant $\lambda$ is called **geometric growth**.

The value of $\lambda$ classifies the fate of the population:

| $\lambda$ | Population |
|---|---|
| $\lambda > 1$ | increases |
| $\lambda = 1$ | constant |
| $0 < \lambda < 1$ | declines toward extinction |
| $\lambda = 0$ | no reproduction: extinct in the next generation |

Taking logarithms, $\lg N_t = \lg N_0 + t\lg\lambda$: on a logarithmic scale geometric growth is a straight line with slope $\lg\lambda$, which is how $\lambda$ is estimated from a series of annual counts.

### 10.1.2. Exponential Growth

When generations overlap and births and deaths occur continuously (humans, many mammals, bacteria), the change of population size is described by instantaneous rates. If $b$ and $d$ are the per capita birth and death rates per unit time, independent of density,

$$
\frac{\mathrm{d}N}{\mathrm{d}t} = (b - d)N = rN, \qquad N(t) = N_0\mathrm{e}^{rt}. \tag{10.2}
$$

**Definition 10.1.2 (Exponential Growth)** **Exponential growth** is growth at a constant per capita rate $r = b - d$, according to Eq. (10.2); $r$ is the instantaneous rate of increase. Plotted against time, $N$ rises along a J-shaped curve, and $\ln N$ along a straight line of slope $r$.

The two descriptions are the same process seen at different time resolutions.

**Proposition 10.1.1 (Discrete and Continuous Rates)** A population growing exponentially at rate $r$ multiplies by $\lambda = \mathrm{e}^r$ per unit time; conversely, geometric growth with finite rate $\lambda > 0$ agrees at integer times with exponential growth at $r = \ln\lambda$. Over an interval of length $\Delta t$ the factor of increase is $\mathrm{e}^{r\Delta t}$, so instantaneous rates add over time while finite rates multiply. The doubling time is
$$
t_{\mathrm{d}} = \frac{\ln 2}{r} \approx \frac{0.693}{r}. \tag{10.3}
$$

**Proof** From Eq. (10.2), $N(t+1)/N(t) = \mathrm{e}^{r(t+1)}/\mathrm{e}^{rt} = \mathrm{e}^r$, which is constant; this is Eq. (10.1) with $\lambda = \mathrm{e}^r$. Conversely, $N_0\lambda^t = N_0\mathrm{e}^{t\ln\lambda}$. For an interval $\Delta t$, $N(t + \Delta t)/N(t) = \mathrm{e}^{r\Delta t}$, and two successive intervals give $\mathrm{e}^{r\Delta t_1}\mathrm{e}^{r\Delta t_2} = \mathrm{e}^{r(\Delta t_1 + \Delta t_2)}$. Setting $\mathrm{e}^{rt_{\mathrm{d}}} = 2$ gives Eq. (10.3). $\square$

Thus $r > 0$, $r = 0$ and $r < 0$ correspond to $\lambda > 1$, $\lambda = 1$ and $\lambda < 1$. The two rates are nearly equal when small: $\lambda = \mathrm{e}^r \approx 1 + r$, so a population growing at $r = 0.02$ per year increases by about 2% per year and doubles in about 35 years (the "rule of 70"). The **doubling time** ([7.6.20](/7.6.20)) is the familiar measure for cells in culture; for a population it is meaningful only while growth is exponential.

The value of $r$ attained when resources are unlimited and conditions optimal is the maximum **intrinsic rate of increase** $r_m$ ([7.10.15](/7.10.15#def-15.1.4)), computed from the life table with the Euler–Lotka equation of 7.19.9. It is a species attribute that varies over many orders of magnitude and scales roughly as the $-1/4$ power of body mass (7.19.6): bacteria can double in less than an hour, a vole population several times a year, while the maximal growth rate of a population of elephants is a few percent per year. Even the slowest growth is explosive if it continues. Darwin calculated in *The Origin of Species* that a single pair of elephants, the slowest breeders among animals, would leave nearly 19 million descendants after about 750 years if all survived: exponential growth must eventually stop.

Exponential growth is observed when a population is far below the limits of its resources: after colonizing a new area, or recovering after a catastrophe or after protection. The Eurasian collared dove (*Streptopelia decaocto*) spread from the Balkans across Europe in the twentieth century, reaching Britain in the 1950s, and the British population grew nearly exponentially for its first decade; protected populations of large whales, elephant seals and white-tailed eagles have shown the same phase.

### 10.1.3. Human Population Growth and the Demographic Transition

The world human population took the whole of prehistory and history to reach one billion, around 1804 (United Nations estimates). It reached two billion in 1927, three in 1960, four in 1974, five in 1987, six in 1999, seven in 2011 and eight in November 2022. Between 1804 and 1927 the mean growth rate was 0.56% per year; between 1960 and 1974 it was 2.1% per year, a doubling time of 33 years. Before about 1970 human growth was faster than exponential (the growth rate itself was increasing); since then the rate has fallen, to below 1% per year in the 2020s.

**Definition 10.1.3 (Demographic Transition)** The **demographic transition** is the historical change of a human population from high birth and death rates to low birth and death rates, in which the death rate falls first and the birth rate later. Four stages are distinguished: (1) high birth and death rates, slow growth; (2) falling death rate with high birth rate, rapid growth; (3) falling birth rate, slowing growth; (4) low birth and death rates, slow or negative growth.

Population growth during the transition is the integral of the gap between the two curves: the longer the lag between the fall in mortality (from improved nutrition, sanitation and medicine) and the fall in fertility, the more the population multiplies before stabilizing. European countries passed through the transition over the eighteenth to twentieth centuries; many countries of Asia and Latin America did so within a few decades after 1950, and the growth of the world population since 1950 is largely the result of stage 2 and 3 populations in these regions. Countries that have completed the transition with fertility below replacement, as China has since the 1990s, enter a stage of decline that the original four-stage scheme did not foresee, with the aging age structure discussed in 7.19.9.

![Human population growth. A: the years in which the world population reached 1 to 8 billion (United Nations Population Division estimates), on a logarithmic scale (dots), and the mean exponential growth rate between successive milestones (step curve, right axis), which peaked at 2.1% per year between 1960 and 1974 and has since fallen. B: a model of the demographic transition (illustrative parameters): the death rate falls first (centered on year 60), the birth rate 60 years later; the population (dashed, right axis) grows more than fivefold while the gap (shaded) is open, and levels off when the two rates meet again (stages 1–4 of Definition 10.1.3)](./plots/human-population.py)

## 10.2. The Logistic Equation

### 10.2.1. Derivation

No population grows exponentially for long: as numbers rise, resources per individual decline, waste accumulates, disease and predation increase, and birth rates fall or death rates rise. The simplest model of this assumes that the per capita growth rate declines *linearly* with density, from its maximum $r$ at low density to zero at a density $K$.

**Definition 10.2.1 (Carrying Capacity)** The **carrying capacity** $K$ of an environment for a population is the population size at which the per capita birth and death rates are equal, so that the population neither increases nor decreases; it is the largest population that the resources of the environment can maintain indefinitely.

**Formula 10.2.1 (Logistic Equation)** The logistic equation (Verhulst 1838; Pearl & Reed 1920) is
$$
\frac{\mathrm{d}N}{\mathrm{d}t} = rN\left(1 - \frac{N}{K}\right), \qquad \frac{1}{N}\frac{\mathrm{d}N}{\mathrm{d}t} = r\left(1 - \frac{N}{K}\right), \tag{10.4}
$$
where $r$ is the intrinsic rate of increase at low density and $K$ the carrying capacity.

The factor $1 - N/K$ is the "unused opportunity for growth": if each individual uses $1/K$ of the available resources (or space), $N$ individuals use $N/K$ and leave $1 - N/K$. Each added individual reduces the per capita growth rate by $r/K$; this inhibition by crowding is sometimes called environmental resistance. The same equation follows from density-dependent birth and death rates.

**Proposition 10.2.1 (Logistic Growth from Linear Vital Rates)** If the per capita birth rate declines and the death rate increases linearly with density, $b(N) = b_0 - \beta N$ and $d(N) = d_0 + \delta N$ with $b_0 > d_0$ and $\beta + \delta > 0$, then $N$ obeys the logistic equation (10.4) with
$$
r = b_0 - d_0, \qquad K = \frac{b_0 - d_0}{\beta + \delta},
$$
and $K$ is the density at which the birth-rate and death-rate lines cross.

**Proof** $\mathrm{d}N/\mathrm{d}t = [b(N) - d(N)]N = [(b_0 - d_0) - (\beta + \delta)N]N = rN(1 - N/K)$ with the stated $r$ and $K$. The lines cross where $b(N) = d(N)$, that is at $N = (b_0 - d_0)/(\beta + \delta) = K$. $\square$

The proposition makes a point that the notation hides: $K$ is not a property of the environment alone but the outcome of how strongly crowding affects the birth and death of individuals. The same environment has different carrying capacities for individuals that suffer more or less from crowding (Kuno 1991). Density dependence may act only on births ($\delta = 0$), only on deaths ($\beta = 0$) or on both; the logistic equation cannot tell them apart.

### 10.2.2. Solution and the Phases of the S-Shaped Curve

The logistic equation is separable; its solution ([2.2.15](/2.2.15#ex-15.2.4)) is
$$
N(t) = \frac{K}{1 + \mathrm{e}^{a - rt}}, \qquad a = \ln\frac{K - N_0}{N_0}, \tag{10.5}
$$
where the constant $a$ fixes the position of the curve relative to the origin. For $0 < N_0 < K$ the curve is S-shaped (sigmoid): it rises almost exponentially at first, then ever more slowly toward $K$. For $N_0 > K$ ($a$ is then the logarithm of a negative number, and the formula is read with $\mathrm{e}^a = (K - N_0)/N_0 < 0$) the population declines monotonically to $K$.

**Proposition 10.2.2 (Shape of the Logistic Curve)** Let $0 < N_0 < K$. Then (a) $N(t)$ increases monotonically to $K$; (b) the growth rate $\mathrm{d}N/\mathrm{d}t$ is greatest, equal to $rK/4$, when $N = K/2$, at time $t^* = a/r$, which is the inflection point of the curve; (c) the curve is point-symmetric about the inflection point; (d) the acceleration $\mathrm{d}^2N/\mathrm{d}t^2$ is greatest at $N = K(3 - \sqrt3)/6 \approx 0.211K$ and most negative at $N = K(3 + \sqrt3)/6 \approx 0.789K$.

**Proof** (a) $\mathrm{d}N/\mathrm{d}t = rN(1 - N/K) > 0$ for $0 < N < K$, and by uniqueness of solutions $N$ cannot reach the equilibrium $K$ in finite time, so it increases to a limit, which must be an equilibrium: $K$. (b) $f(N) = rN - rN^2/K$ has $f'(N) = r - 2rN/K = 0$ at $N = K/2$, where $f = rK/4$. Differentiating along the solution, $\ddot N = f'(N)\dot N = r(1 - 2N/K)\dot N$, which changes sign at $N = K/2$: the inflection point. Setting $N = K/2$ in Eq. (10.5) gives $\mathrm{e}^{a - rt^*} = 1$, $t^* = a/r$. (c) With $s = t - t^*$, Eq. (10.5) reads $N = K/(1 + \mathrm{e}^{-rs})$, and $N(-s) = K\mathrm{e}^{-rs}/(1 + \mathrm{e}^{-rs}) = K - N(s)$. (d) $\dddot N = \frac{\mathrm{d}}{\mathrm{d}t}[f'(N)f(N)] = [f''(N)f(N) + f'(N)^2]f(N)$, and $f(N) > 0$, so the extremes of $\ddot N$ satisfy $f''f + f'^2 = 0$. With $u = N/K$: $-2u(1 - u) + (1 - 2u)^2 = 6u^2 - 6u + 1 = 0$, so $u = (3 \mp \sqrt3)/6$. $\square$

These points give a quantitative basis for the five conventional phases of the S-shaped curve:

1. Lag phase (initial phase): numbers are small and increase slowly in absolute terms, although the per capita rate is near its maximum.
2. Acceleration phase: the increase speeds up; it ends where the acceleration is greatest, near $0.21K$.
3. Inflection: at $K/2$ the population grows fastest, by $rK/4$ per unit time.
4. Deceleration phase: above $K/2$ the increase slows; deceleration is greatest near $0.79K$.
5. Saturation phase: the population approaches $K$ and stays there.

That the yield $\mathrm{d}N/\mathrm{d}t$ is largest at $K/2$ is the basis of the theory of maximum sustainable yield in fisheries and forestry (7.19.53): a population kept at half its carrying capacity replaces losses fastest.

### 10.2.3. Equilibria and Stability

The logistic equation is a one-dimensional autonomous equation $\dot N = f(N)$, whose long-term behavior can be read from the graph of $f$: where $f > 0$ the population increases, where $f < 0$ it decreases, and the zeros of $f$ are the **equilibrium points** ([2.4.11](/2.4.11)).

**Proposition 10.2.3 (Stability of the Logistic Equilibria)** The logistic equation has the equilibria $N = 0$ and $N = K$. $N = 0$ is unstable and $N = K$ is asymptotically stable; every solution with $N_0 > 0$ converges to $K$. Near $K$, deviations decay as $\mathrm{e}^{-rt}$, so the characteristic return time is $T_R = 1/r$.

**Proof** Linearization: $f'(N) = r(1 - 2N/K)$, so $f'(0) = r > 0$ (unstable) and $f'(K) = -r < 0$ (stable). For $n = N - K$ small, $\dot n = f'(K)n = -rn$, $n(t) = n_0\mathrm{e}^{-rt}$. Global convergence follows from the signs of $f$: $f > 0$ on $(0, K)$ and $f < 0$ on $(K, \infty)$, so every positive solution moves monotonically toward $K$. A **Lyapunov function** ([2.4.11](/2.4.11#sec-11.4)) gives the same result in a form that generalizes to the many-species models of later chapters:
$$
V(N) = N - K - K\ln\frac{N}{K}, \qquad \dot V = \Bigl(1 - \frac{K}{N}\Bigr)\dot N = \frac{N - K}{N}\,rN\,\frac{K - N}{K} = -\frac{r}{K}(N - K)^2 \leq 0.
$$
$V$ is positive for $N \neq K$, zero at $K$, and tends to infinity as $N \to 0$ or $N \to \infty$; it decreases strictly along every solution except at $K$. $\square$

The return time $T_R = 1/r$, the *natural response time* of a population, measures how quickly it recovers from a disturbance: species with high $r$ return quickly, species with low $r$ slowly. (Its relation to the resilience of communities is taken up in 7.19.38.)

The logistic equation has no parameters that matter for its shape. With $x = N/K$ and $\tau = rt$ it becomes $\mathrm{d}x/\mathrm{d}\tau = x(1 - x)$: all logistic curves are one curve, rescaled in time by $1/r$ and in size by $K$. Such nondimensionalization is the first step in the analysis of every model in this course, because it reveals which combinations of parameters actually determine the dynamics.

![The logistic equation (Formula 10.2.1), r = 1, K = 100. A: the growth rate dN/dt (solid) is a parabola with maximum rK/4 at K/2; the per capita growth rate (dashed, right axis) declines linearly from r to 0 at K. The arrows show that N increases below K and decreases above it: 0 is an unstable and K a stable equilibrium (Proposition 10.2.3). B: solutions from N₀ = 2, 20, 60 and 150 all approach K; the curve from N₀ = 2 is divided into the five phases of Proposition 10.2.2, bounded where the acceleration is greatest (0.21K), at the inflection (K/2), where deceleration is greatest (0.79K), and at 0.99K](./plots/logistic-phase.py)

Real populations growing toward $K$ often overshoot it and oscillate before settling, because density affects births and deaths only after a delay (the time for food to be depleted, for embryos to develop, for predators to respond). Such overshoots are outside the logistic model; they are analyzed with the delayed logistic equation in 7.19.13.

## 10.3. Generalizations

### 10.3.1. The θ-Logistic and Gompertz Models

The linear decline of the per capita growth rate with density is an assumption of convenience. Data seldom support it exactly: in many large mammals the per capita growth rate stays high until the population is close to $K$ and then falls sharply (Fowler 1981), while in many insects and fish it falls steeply at low density and levels off.

**Definition 10.3.1 (θ-Logistic Model)** The **θ-logistic model** (Gilpin & Ayala 1973) is
$$
\frac{\mathrm{d}N}{\mathrm{d}t} = rN\left[1 - \left(\frac{N}{K}\right)^\theta\right], \qquad \theta > 0. \tag{10.6}
$$
The per capita growth rate $r[1 - (N/K)^\theta]$ is concave in $N$ for $\theta > 1$ (density dependence concentrated near $K$), linear for $\theta = 1$ (the logistic) and convex for $\theta < 1$ (density dependence concentrated at low density).

**Proposition 10.3.1 (Properties of the θ-Logistic Model)** For $0 < N_0 < K$:

(a) the solution is
$$
N(t) = K\Bigl[1 + \Bigl(\Bigl(\frac{K}{N_0}\Bigr)^\theta - 1\Bigr)\mathrm{e}^{-r\theta t}\Bigr]^{-1/\theta}; \tag{10.7}
$$
(b) the growth rate is greatest at the inflection point $N^* = K(1 + \theta)^{-1/\theta}$, which lies above $K/2$ for $\theta > 1$ and below it for $\theta < 1$;
(c) the equilibrium $K$ is stable with return rate $\theta r$;
(d) as $\theta \to 0$ with $r\theta = c$ held fixed, the model converges to the Gompertz equation $\mathrm{d}N/\mathrm{d}t = cN\ln(K/N)$, whose solution is $N(t) = K\exp[\ln(N_0/K)\,\mathrm{e}^{-ct}]$ and whose inflection point is $K/\mathrm{e} \approx 0.37K$.

**Proof** (a) Let $u = (N/K)^{-\theta}$. Then $\dot u = -\theta u\dot N/N = -\theta ur(1 - 1/u) = -r\theta(u - 1)$, so $u - 1 = (u_0 - 1)\mathrm{e}^{-r\theta t}$ with $u_0 = (K/N_0)^\theta$, and $N = Ku^{-1/\theta}$. (b) $f(N) = rN - rK^{-\theta}N^{1+\theta}$ has $f'(N) = r - r(1 + \theta)(N/K)^\theta = 0$ at $(N/K)^\theta = 1/(1 + \theta)$. Since $(1 + \theta)^{1/\theta}$ decreases from $\mathrm{e}$ to 1 as $\theta$ increases from 0 to $\infty$ and equals 2 at $\theta = 1$, $N^* > K/2$ iff $\theta > 1$. (c) $f'(K) = r - r(1 + \theta) = -r\theta$. (d) $[1 - (N/K)^\theta]/\theta = [1 - \mathrm{e}^{\theta\ln(N/K)}]/\theta \to -\ln(N/K) = \ln(K/N)$ as $\theta \to 0$, so $r[1 - (N/K)^\theta] = c[1 - (N/K)^\theta]/\theta \to c\ln(K/N)$. For the Gompertz equation, $y = \ln(N/K)$ satisfies $\dot y = -cy$, so $y = y_0\mathrm{e}^{-ct}$. Its inflection is where $\frac{\mathrm{d}}{\mathrm{d}N}[cN\ln(K/N)] = c[\ln(K/N) - 1] = 0$, at $N = K/\mathrm{e}$; equivalently, it is the limit of $(1 + \theta)^{-1/\theta} \to \mathrm{e}^{-1}$. $\square$

The parameter $\theta$ is therefore a *shape* parameter: it moves the density of maximal growth and the sharpness of regulation without changing $r$ or $K$. Fitted to long time series of 3269 populations of mammals, birds, fish and insects, the θ-logistic gave $\theta < 1$ for most of them (Sibly et al. 2005): populations usually spend much of their time above the density of maximal growth, where per capita growth is low and changes little with density. The estimate is controversial, because $\theta$, $r$ and $K$ are strongly correlated in fits to noisy data, and because measurement error biases $\theta$ downward. The Gompertz curve, with its inflection at $K/\mathrm{e}$ and asymmetric shape, is widely used for the growth of tumors and of organisms (for plant growth curves see [7.13.17](/7.13.17#sec-17.6.2)); the **Gompertz–Makeham law** of mortality (7.19.9) uses the same exponential form for a different quantity, the hazard of death.

The same family of curves (Eq. (10.7), also called the Richards curve) is used in fisheries as the Pella–Tomlinson surplus production model, where $\theta$ determines at what fraction of $K$ the maximum sustainable yield is obtained (7.19.53).

![The θ-logistic model (Definition 10.3.1), r = 1, K = 1. A: the per capita growth rate 1 − (N/K)^θ is convex for θ = 0.3, linear for θ = 1 (the logistic) and concave for θ = 4; the Gompertz model (dashed, r = 0.25) is the limit θ → 0 and has a per capita rate proportional to ln(K/N), unbounded at low density. B: the growth rate dN/dt, with its maximum (dots) at N* = K(1 + θ)^(−1/θ): 0.18K, 0.5K and 0.67K, and K/e for the Gompertz curve (Proposition 10.3.1). C: the growth curves from N₀ = 0.02K (Eq. (10.7)); larger θ makes the approach to K more abrupt and faster (return rate θr)](./plots/theta-logistic.py)

### 10.3.2. Allee Effects

In all models so far the per capita growth rate is greatest when the population is smallest. In many species the opposite holds at low density: individuals do worse when there are few of them. Allee (1931) demonstrated it in aggregations of animals, and it has many mechanisms: failure to find mates (in the gypsy moth *Lymantria dispar*, mating success falls steeply at low density, which slows the advance of its invasion front), pollen limitation in sparse plant populations, loss of cooperative hunting or breeding (African wild dogs, *Lycaon pictus*, need packs large enough to hunt and to guard pups), reduced vigilance against predators, failure to satiate predators, and inbreeding.

**Definition 10.3.2 (Allee Effect)** An **Allee effect** is a positive relationship between a component of individual fitness and population size or density at low density. A *demographic* Allee effect is one in which the per capita population growth rate increases with density at low density. It is *strong* if the per capita growth rate is negative below a threshold density (the Allee threshold) and *weak* if it remains positive.

A component Allee effect (fewer matings, say) need not produce a demographic one, if it is outweighed by reduced competition; it is the demographic effect that changes the dynamics. A convenient model contains both strong and weak effects:
$$
\frac{\mathrm{d}N}{\mathrm{d}t} = rN\left(1 - \frac{N}{K}\right)\frac{N - A}{K}, \qquad -K < A < K, \tag{10.8}
$$
with per capita growth rate $g(N) = (r/K^2)(K - N)(N - A)$. At $N = 0$, $g(0) = -rA/K$, which is negative for $A > 0$ (strong effect, threshold $A$) and positive for $A < 0$ (weak effect); $g'(0) = (r/K)(1 + A/K) > 0$, so per capita growth increases with density at low density in both cases. With $x = N/K$, $\tau = rt$, $a = A/K$, Eq. (10.8) becomes $\mathrm{d}x/\mathrm{d}\tau = x(1 - x)(x - a)$.

**Proposition 10.3.2 (Bistability under a Strong Allee Effect)** For $0 < a < 1$, the equation $\dot x = x(1 - x)(x - a)$ has equilibria $0$, $a$ and $1$; $0$ and $1$ are asymptotically stable and $a$ is unstable. Solutions with $x_0 < a$ decline to extinction and solutions with $x_0 > a$ grow to the carrying capacity.

**Proof** Let $f(x) = x(1 - x)(x - a)$. Then $f'(0) = -a < 0$, $f'(a) = a(1 - a) > 0$ and $f'(1) = -(1 - a) < 0$. The signs of $f$ are negative on $(0, a)$, positive on $(a, 1)$ and negative on $(1, \infty)$, so solutions move monotonically away from $a$ and toward $0$ or $1$. $\square$

The population is **bistable** ([7.3.18](/7.3.18#def-18.4.2)): two stable states, separated by the threshold, each with its own **basin of attraction** ([7.6.33](/7.6.33#def-33.2.1)). This has direct consequences for conservation and for invasions. A population reduced below its Allee threshold goes extinct by itself, even if the cause of its decline is removed; reintroductions and biological control releases fail unless the number released exceeds the threshold; and invading populations that arrive in small numbers often fail, which is one reason for the time lags of invasions (7.19.51). Together with demographic stochasticity, which is strongest exactly at low numbers, Allee effects make small populations much more vulnerable than deterministic models suggest (7.19.15).

The most dramatic consequence appears when the environment deteriorates gradually. Add to Eq. (10.8) a density-independent per capita mortality $m$ (from harvesting, habitat degradation or a pathogen), measured in units of $r$: $\dot x = x[g(x) - m]$ with $g(x) = (1 - x)(x - a)$. Equilibria other than 0 satisfy $g(x) = m$, a quadratic with roots
$$
x_\pm = \frac{(1 + a) \pm\sqrt{(1 - a)^2 - 4m}}{2}. \tag{10.9}
$$

**Proposition 10.3.3 (Saddle-Node Collapse)** In the strong case ($0 < a < 1$), the stable equilibrium $x_+$ and the unstable threshold $x_-$ approach each other as $m$ increases and annihilate at
$$
m_c = \frac{(1 - a)^2}{4}, \qquad x_c = \frac{1 + a}{2},
$$
in a **saddle-node bifurcation** ([7.6.33](/7.6.33)). For $m > m_c$, extinction is the only outcome. Reducing $m$ again below $m_c$ does not restore the population unless it is raised above $x_-$. In the logistic case ($\dot x = x(1 - x - m)$) the equilibrium $1 - m$ instead declines continuously to 0 at $m = 1$.

**Proof** The roots (10.9) are real and distinct for $m < m_c$ and coincide at $m = m_c$; for $m > m_c$ there are no positive equilibria other than 0, and since $g(x) - m \leq g_{\max} - m < 0$ with $g_{\max} = g(x_c) = m_c$, $\dot x < 0$ for all $x > 0$. Stability: $\frac{\mathrm{d}}{\mathrm{d}x}\{x[g(x) - m]\} = xg'(x)$ at an equilibrium with $g(x) = m$, and $g'(x) = 1 + a - 2x$ is negative at $x_+ > x_c$ and positive at $x_- < x_c$. The equilibrium 0 has eigenvalue $g(0) - m = -a - m < 0$, so it is stable for every $m$. For the logistic, the only positive equilibrium is $1 - m$, which tends to 0 continuously as $m \to 1$, where it merges with 0 (a transcritical bifurcation). $\square$

The difference is qualitative. Without an Allee effect, a population under increasing pressure declines in proportion, and a decline gives warning. With a strong Allee effect, the population stays at a substantial size until the pressure reaches $m_c$ and then crashes to extinction from a density of $(1 + a)/2$, more than half its carrying capacity; and the collapse shows **hysteresis** ([7.3.18](/7.3.18#def-18.4.3)): the conditions that preceded the collapse are not sufficient for recovery. A weak Allee effect produces a smaller window of the same behavior: 0 becomes stable at $m = -a$ (a transcritical bifurcation), but the positive equilibrium persists up to $m_c = (1 - a)^2/4 > -a$, so between the two there is bistability, and the final collapse is again abrupt. The collapse of the Atlantic cod off Newfoundland around 1992, and its failure to recover for decades after fishing was stopped, has been interpreted in these terms (other explanations, including changes in the community, also contribute). Sudden shifts between alternative states in whole ecosystems are taken up in 7.19.39.

![Allee effects (Definition 10.3.2), in dimensionless form dx/dτ = x(1 − x)(x − a). A: per capita growth rate for the logistic (1 − x), a weak Allee effect (a = −0.5: positive at zero density but increasing with density) and a strong Allee effect (a = 0.25: negative below the threshold x = a). B: solutions with a strong Allee effect: populations starting above the threshold (red) grow to the carrying capacity, those starting below it (gray) go extinct (Proposition 10.3.2). C: equilibria against an added per capita mortality m (solid stable, dashed unstable). The logistic equilibrium declines linearly to 0 at m = 1. With a strong Allee effect the stable equilibrium and the threshold meet at m = 0.14 in a saddle-node bifurcation, and the population collapses from x = 0.63 to extinction (arrow); the weak case collapses from x = 0.25 at m = 0.56, after the zero state has become stable at m = 0.5 (Proposition 10.3.3). x = 0 is stable for all m in the strong case](./plots/allee.py)

## 10.4. Fitting Growth Curves

Fitting the logistic curve to data estimates $r$ and $K$ and tests whether the model describes the population at all. The classic data set is the growth of yeast (*Saccharomyces cerevisiae*) in a culture measured by Carlson (1913), which Pearl (1927) used to illustrate the logistic curve and Gause (1934) reproduced in *The Struggle for Existence*:

| $t$ (h) | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
|---|---|---|---|---|---|---|---|---|---|---|
| $N$ | 9.6 | 18.3 | 29.0 | 47.2 | 71.1 | 119.1 | 174.6 | 257.3 | 350.7 | 441.0 |

| $t$ (h) | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 |
|---|---|---|---|---|---|---|---|---|---|
| $N$ | 513.3 | 559.7 | 594.8 | 629.4 | 640.8 | 651.1 | 655.9 | 659.6 | 661.8 |

($N$ is the amount of yeast in arbitrary units.) Gause's own experiments with *Paramecium*, which established the basis for his work on competition (7.19.22), gave similar sigmoid curves.

The direct approach, nonlinear least squares, minimizes the sum of squared deviations between the data and the solution (10.5) over the parameters $(K, r, N_0)$,
$$
S(K, r, N_0) = \sum_i\bigl[N_i - N(t_i; K, r, N_0)\bigr]^2.
$$
Because $N(t)$ is nonlinear in the parameters, this is solved iteratively, for example by the Gauss–Newton method, whose application to exactly this model is worked through in [3.5.5](/3.5.5#sec-5.1.5.2); in Python, `scipy.optimize.curve_fit` does it ([4.4.4](/4.4.4#sec-4.2.3)). For the yeast data it gives $K = 663.0 \pm 1.7$, $r = 0.547 \pm 0.006$ per hour and $N_0 = 9.1 \pm 0.4$ (standard errors from the asymptotic covariance matrix). Note what $r$ means: a per capita rate of $0.547\,\mathrm{h}^{-1}$ at low density corresponds to a factor $\mathrm{e}^{0.547} = 1.73$ per hour, a doubling time of $\ln2/0.547 = 1.27$ hours, not an increase of "55% per hour".

Before computers, the logistic curve was fitted by linearization, transforming it to a straight line. Rearranging Eq. (10.5),
$$
\ln\frac{K - N}{N} = a - rt, \tag{10.10}
$$
so that if $K$ is known, regressing $\ln[(K - N)/N]$ on $t$ gives $r$ (minus the slope) and $a$ (the intercept), and $N_0 = K/(1 + \mathrm{e}^a)$. When the population has not clearly leveled off, $K$ can be estimated from three equally spaced observations.

**Proposition 10.4.1 (Three-Point Estimate of $K$)** If $N_0$, $N_1$, $N_2$ are values of a logistic curve at times $t_0$, $t_0 + \Delta t$, $t_0 + 2\Delta t$, then
$$
K = \frac{N_1^2(N_0 + N_2) - 2N_0N_1N_2}{N_1^2 - N_0N_2}, \qquad r = \frac{1}{\Delta t}\ln\frac{N_1(K - N_0)}{N_0(K - N_1)}.
$$

**Proof** By Eq. (10.10), $y_i = (K - N_i)/N_i$ satisfy $y_1 = y_0\mathrm{e}^{-r\Delta t}$ and $y_2 = y_0\mathrm{e}^{-2r\Delta t}$, so $y_1^2 = y_0y_2$. Writing $y_i = K/N_i - 1$:
$$
\Bigl(\frac{K}{N_1} - 1\Bigr)^2 = \Bigl(\frac{K}{N_0} - 1\Bigr)\Bigl(\frac{K}{N_2} - 1\Bigr).
$$
Multiplying by $N_0N_1^2N_2$, expanding, and canceling the term $N_0N_1^2N_2$ on both sides gives $K^2N_0N_2 - 2KN_0N_1N_2 = K^2N_1^2 - KN_1^2(N_0 + N_2)$; dividing by $K \neq 0$ and solving the linear equation for $K$ gives the formula. Then $\mathrm{e}^{-r\Delta t} = y_1/y_0$ gives $r$. $\square$

With $t = 0, 9, 18$ h, the three-point formula gives $K = 664.3$, and the regression of Eq. (10.10) on all points then gives $r = 0.539$ per hour and $N_0 = 9.8$. The sum of squared residuals is 232, against 194 for the nonlinear fit. The difference is small here because the data are very regular, but it illustrates a general point: the transformation changes the error structure. An error of a few units in $N$ near $K$ becomes an enormous error in $\ln[(K - N)/N]$, while the same error at intermediate $N$ is shrunk, so ordinary least squares on the transformed scale gives the wrong points the most weight (see [3.3.5](/3.3.5) on assumptions of regression). Linearization is useful for starting values; estimates should come from the model on its natural scale, with an error model that fits the data (multiplicative errors, common for counts, call for least squares on $\ln N$, or for maximum likelihood with a suitable distribution).

A third method estimates the per capita growth rate directly from successive counts, $\ln(N_{t+1}/N_t)$, and regresses it on the density; for the logistic, the regression line has intercept $r$ and slope $-r/K$. For the yeast data it gives $r = 0.539$ per hour and $K = 663$. It is the most transparent check of the model's central assumption, the linear decline of per capita growth with density (Formula 10.2.1); curvature in this plot suggests a θ-logistic.

The most important practical lesson concerns the information in the data. Fitted to the first 6 hours only, before the inflection, the nonlinear model gives $K = 657$ with a 95% confidence interval of $\pm 490$; with 8 hours, $K = 789 \pm 109$; with 10 hours, just past the inflection, $K = 683 \pm 25$. Before the inflection point, data on a growing population contain almost no information about its carrying capacity, because the early part of every sigmoid curve looks exponential. Predictions of the eventual size of a growing population (of an invader, an epidemic, or a human population) from its early growth are correspondingly uncertain.

![Fitting the logistic curve to Carlson's (1913) yeast data. A: the nonlinear least squares fit (solid; K = 663, r = 0.547 per hour) and the linearized fit (dashed; K = 664 from the three-point formula with t = 0, 9, 18 h, then regression of ln((K − N)/N) on t) are almost indistinguishable. B: residuals of both fits; the nonlinear fit has the smaller sum of squares (194 against 232), and both show the same systematic waves around 4–7 h and 9–13 h. C: per capita growth over each hour, ln(Nₜ₊₁/Nₜ), against the geometric mean density: nearly linear, with intercept r = 0.539 per hour and K = 663, supporting the logistic form. D: nonlinear fits to the first 6, 8 and 10 hours only: before the inflection (about 7 h) the carrying capacity is almost undetermined](./plots/yeast-fit.py)

## 10.5. Numerical Solution

The logistic, θ-logistic and Gompertz equations have closed-form solutions; most models in this course do not, and are solved numerically. The simplest scheme, the **Euler method** ([7.9.14](/7.9.14)), advances by a step $h$: $N_{k+1} = N_k + hf(N_k)$. For the logistic equation this is
$$
N_{k+1} = N_k\Bigl[1 + hr\Bigl(1 - \frac{N_k}{K}\Bigr)\Bigr],
$$
which is exactly the discrete logistic model of a population with discrete generations (7.19.12) with growth parameter $hr$. For $hr < 1$ it approaches $K$ monotonically like the true solution; for $1 < hr < 2$ it overshoots and oscillates; for $hr > 2$ it oscillates permanently and for $hr > 2.57$ it is chaotic, although the differential equation itself always approaches $K$ smoothly. Two lessons follow. Numerical artifacts can mimic real dynamics, so step sizes must be small compared with the time scale $1/r$; and a difference equation is not a discretized differential equation but a different model, appropriate when reproduction really is synchronized.

In practice one uses adaptive higher-order methods (**Runge–Kutta methods**, [7.9.14](/7.9.14)), as implemented in `scipy.integrate.solve_ivp` ([4.4.4](/4.4.4#sec-4.3.2)), which control the local error automatically:

```python
import numpy as np
from scipy.integrate import solve_ivp

def allee(t, x, a=0.25, m=0.1):
    return x * (1 - x) * (x - a) - m * x

sol = solve_ivp(allee, (0, 60), [0.5], t_eval=np.linspace(0, 60, 301), rtol=1e-8)
# sol.y[0] approaches x+ = 0.5 [(1 + a) + sqrt((1 - a)^2 - 4m)] = 0.77
```

## 10.6. Significance and Limitations of the Logistic Model

The logistic equation is the most influential model in population ecology, and also the most criticized. Its significance:

1. It is the building block of models of interacting species: the Lotka–Volterra competition equations add interspecific terms to it (7.19.22), and predator–prey models use it for prey growth (7.19.25, 7.19.26).
2. It underlies the theory of harvesting, in which the surplus production $rN(1 - N/K)$ is the sustainable yield and its maximum $rK/4$ at $K/2$ the maximum sustainable yield (7.19.53).
3. Its two parameters became the axes of life-history theory: $r$ measures the capacity for increase and $K$ the ability to persist under crowding, the basis of **r-selection** and **K-selection** ([7.10.15](/7.10.15#def-15.2.1)). $K$, like $r$, changes with the environment.
4. It provides the return time $1/r$ and the idea that a population is regulated around an equilibrium.

Its assumptions are restrictive, and each failure leads to a later chapter:

| Assumption | Consequence when violated | Chapter |
|---|---|---|
| Per capita growth declines linearly with density | θ-logistic, Allee effects | 10.3 |
| Density acts instantaneously | overshoot, damped and sustained oscillations | 7.19.13 |
| Continuous breeding | cycles and chaos in discrete generations | 7.19.12 |
| All individuals equivalent | age and stage structure | 7.19.14 |
| Deterministic, constant environment | stochastic extinction, fluctuating $K$ | 7.19.15 |
| Closed, spatially homogeneous population | dispersal, metapopulations, spatial spread | 7.19.16, 7.19.17 |
| Single species | competition, predation, parasitism | 7.19.22–7.19.28 |

The logistic also represents a particular kind of density dependence. The number of individuals produced by a population changes with density in a strictly exactly compensating way: crowding never reduces the total output below what is needed to keep the population at $K$. The many forms of under- and overcompensating density dependence found in nature, and their consequences, are the subject of the next two chapters. Laboratory populations of yeast, protists and flour beetles often fit the logistic well; populations of sheep introduced to Tasmania (Davidson 1938) and of reindeer introduced to St Matthew Island (Klein 1968) overshot their carrying capacity and then declined, the reindeer catastrophically, after they had overgrazed the lichens that supported them, so that the carrying capacity itself fell.

## Summary

- Without density dependence, populations grow geometrically ($N_{t+1} = \lambda N_t$) with discrete generations and exponentially ($\mathrm{d}N/\mathrm{d}t = rN$) with overlapping ones; $\lambda = \mathrm{e}^r$ and the doubling time is $\ln 2/r$ (Definitions 10.1.1, 10.1.2, Proposition 10.1.1). Human growth peaked at 2.1% per year in 1960–1974; the demographic transition (Definition 10.1.3) explains its course.
- The logistic equation $\mathrm{d}N/\mathrm{d}t = rN(1 - N/K)$ assumes a linear decline of per capita growth; it follows from linear density dependence of birth and death, with $K$ where they cross (Proposition 10.2.1). Its solution is the S-shaped curve $K/(1 + \mathrm{e}^{a - rt})$ with inflection at $K/2$, maximum rate $rK/4$, and five phases bounded at $0.21K$, $0.5K$, $0.79K$ (Proposition 10.2.2).
- $0$ is unstable and $K$ globally stable, with return time $1/r$ (Proposition 10.2.3); the Lyapunov function $N - K - K\ln(N/K)$ proves it.

| Model | Per capita growth | Inflection | Stability of $K$ |
|---|---|---|---|
| Logistic | $r(1 - N/K)$ | $K/2$ | rate $r$ |
| θ-logistic | $r[1 - (N/K)^\theta]$ | $K(1 + \theta)^{-1/\theta}$ | rate $\theta r$ |
| Gompertz | $c\ln(K/N)$ | $K/\mathrm{e}$ | rate $c$ |
| Strong Allee | $r(1 - N/K)(N - A)/K$, $A > 0$ | — | bistable with $0$, threshold $A$ |

- Allee effects (Definition 10.3.2) make per capita growth increase with density at low density; a strong Allee effect creates a threshold and bistability (Proposition 10.3.2). Under increasing mortality the stable state disappears in a saddle-node bifurcation at $m_c = (1 - a)^2/4$, so the population collapses abruptly and shows hysteresis (Proposition 10.3.3).
- Growth curves should be fitted by nonlinear least squares on the natural scale; linearizations (three-point formula, Proposition 10.4.1) distort the error structure, and data before the inflection hardly constrain $K$.
- Euler's method applied to the logistic equation is the discrete logistic model, which can oscillate and become chaotic: numerical steps must be small compared with $1/r$.

## Questions

1. A population of an annual weed has $\lambda = 1.5$. What is its intrinsic rate of increase per year, and how long does it take to increase tenfold? A bacterial culture doubles every 30 minutes; what is $r$ per hour?

   **Answer** $r = \ln 1.5 = 0.405$ per year. A tenfold increase needs $\lambda^t = 10$, $t = \ln 10/\ln 1.5 = 5.7$ years. For the bacteria, $r = \ln 2/0.5\,\mathrm{h} = 1.39$ per hour ($\lambda = 4$ per hour).

2. Show that in the logistic model the time for a population to grow from $0.1K$ to $0.9K$ is $(2\ln 9)/r \approx 4.4/r$, independently of $K$. What does this mean for comparing species?

   **Answer** From Eq. (10.10), $t = [a - \ln((K - N)/N)]/r$. At $N = 0.1K$, $\ln((K - N)/N) = \ln 9$; at $0.9K$ it is $-\ln 9$. The difference is $2\ln 9/r = 4.39/r$. The time scale of logistic growth is set by $r$ alone; $K$ only scales the size. A species with ten times the intrinsic rate fills its environment ten times faster, whatever its carrying capacity.

3. Derive the logistic equation for a consumer whose resource is renewed rapidly. Suppose the resource $R$ is supplied at a constant rate $S$ and consumed at rate $cRN$, and the consumers reproduce at per capita rate $eR$ and die at rate $d$. Assume that the resource equilibrates quickly. When does the result resemble the logistic equation?

   **Answer** With resource dynamics $\dot R = S - wR - cRN$ (including a loss rate $w$ of the resource itself) equilibrating fast, $R = S/(w + cN)$, so $\dot N/N = eS/(w + cN) - d$. This decreases with $N$ but is convex, not linear: per capita growth $eS/w - d$ at $N = 0$ and zero at $N^* = (eS - dw)/(cd)$, the carrying capacity. Expanding for small $cN/w$ gives approximately $\dot N/N \approx (eS/w - d) - (eSc/w^2)N$, linear in $N$: the logistic is a good approximation when consumers deplete the resource only modestly. The general form shows that $K$ depends on the supply rate $S$, the efficiency $e$, the consumption rate $c$ and the mortality $d$, all properties of the interaction rather than of the environment alone; it corresponds to a θ-logistic with $\theta < 1$.

4. In the strong Allee model with mortality (Proposition 10.3.3), take $a = 0.25$. Find the population size just before the collapse and explain why a monitoring program that tracks only population size gives little warning.

   **Answer** At $m_c = (1 - 0.25)^2/4 = 0.1406$ the stable equilibrium is $x_c = (1 + a)/2 = 0.625$, so the population is still at 62.5% of its carrying capacity when it collapses; at $m = 0$ it is at 100%. Population size declines only by about a third over the whole range of stress and then drops to zero; there is no gradual approach to zero that would warn of extinction. What does change is the stability of the equilibrium: the eigenvalue $x_+g'(x_+)$ approaches 0 at $m_c$, so the population recovers ever more slowly from perturbations (critical slowing down, 7.19.39). Monitoring recovery rates or the variance and autocorrelation of fluctuations can therefore warn of the collapse when abundance does not.

5. Fit the per capita growth rates $\ln(N_{t+1}/N_t)$ of the yeast data against density by a straight line (figure in Section 10.4, panel C). How would you use the same plot to decide between the logistic and the θ-logistic, and what problem arises if the counts have measurement error?

   **Answer** Under the logistic the points lie on a straight line; under a θ-logistic with $\theta > 1$ they curve downward (concave), with $\theta < 1$ upward (convex). One can fit $\ln(N_{t+1}/N_t) = r[1 - (N_t/K)^\theta]$ by nonlinear least squares and test $\theta = 1$, or compare the two models by AIC. Measurement error in $N_t$ appears in both axes: an overestimated $N_t$ makes $\ln(N_{t+1}/N_t)$ too small and the density too large, so errors produce a spurious negative relation (apparent density dependence) and bias the estimated shape, typically toward $\theta < 1$. State-space models, which separate observation error from process noise, are used to avoid this.
