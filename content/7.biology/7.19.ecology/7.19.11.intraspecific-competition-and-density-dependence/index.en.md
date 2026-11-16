---
title: Intraspecific Competition and Density Dependence
description: "Intraspecific competition: resource limitation, exploitation and interference, crowding versus density; density-dependent mortality, fecundity and growth; under-, exact and overcompensation measured by the slope of k against log density, contest and scramble; the Beverton–Holt, Hassell and Maynard Smith–Slatkin models; net recruitment curves and regulation; constant final yield and the Shinozaki–Kira reciprocal equation; the −3/2 self-thinning rule, its geometric derivation and the −4/3 alternative; asymmetric competition and size hierarchies; territoriality and the consequences of competition."
---

Individuals of the same species need the same resources, in the same places, at the same times. When those resources are insufficient for all, the individuals compete, and each suffers in proportion to how many others there are. This intraspecific competition is the most general source of density dependence, the mechanism that bends exponential growth into the logistic curve of the previous chapter (7.19.10). Here we look at density dependence directly: how it affects survival, fecundity and growth; how its strength and form are measured with the $k$ values of life tables (7.19.9); how models capture its full range, from under- to overcompensation, with consequences for stability that are explored in 7.19.12; and how plants, which cannot move away from their neighbors, express it in the rules of constant final yield and self-thinning. The chapter ends with the asymmetry of competition and its consequences for individuals and populations. Behavioral mechanisms of competition (territoriality, dominance hierarchies, the ideal free distribution) are treated in animal behavior ([7.18.26](/7.18.26)); here they appear through their effects on population dynamics. The regulation of natural populations by density-dependent and other factors, and the long debate about it, is the subject of 7.19.13, and competition between species of 7.19.22.

## 11.1. The Nature of Intraspecific Competition

**Definition 11.1.1 (Intraspecific Competition)** **Intraspecific competition** is an interaction between individuals of the same species brought about by a shared requirement for a resource in limited supply, which reduces the survival, growth or reproduction of at least some of the competing individuals.

Three features characterize it.

1. *The resource is limited.* Competition occurs only for resources whose supply is insufficient for the demand: food, water, light, nutrients, nest sites, space on a rock. Its ultimate effect on an individual is a smaller contribution to the next generation than it would make without competitors.
2. *The effect is density dependent.* The more competitors there are, the greater the effect on each.
3. *The effect is often asymmetric.* Competitors are not equal, and the effects on weak competitors are typically far greater than on strong ones (Section 11.4.3).

Competition can be indirect or direct. In exploitation, individuals interact only through the resource, each reducing what is available to the others: diatoms grown in a culture deplete silicate until the population stabilizes at a level where there is too little for further growth. In interference, individuals prevent others from using a resource directly: a barnacle settled on a patch of rock excludes others even if food is abundant; red deer stags fight for access to hinds. Many cases combine both. Adult cave beetles (*Neaphaenops tellkampfi*) in Kentucky feed only on cricket eggs dug out of the sand floor; at high beetle density their fecundity falls with the depletion of eggs (exploitation), but in experimental arenas with ample eggs, beetles at higher density also fought more, dug fewer and shallower holes and ate fewer eggs (interference; Griffith & Poulson 1993). The two modes recur in competition between species, where they are classified in more detail (7.19.22).

An individual does not experience the density of the population, but the number of competitors in its neighborhood. If 1000 insects are spread over 100 host plants, the density is 10 per plant, but if 10 plants carry 91 insects each and the other 90 carry one, a typical insect experiences far more crowding than 10. The mean density experienced by an individual, the *organism-weighted density* (Lewontin & Levins 1989), is $\sum_in_i^2/\sum_in_i$ over patches with $n_i$ individuals: here $(10 \times 91^2 + 90 \times 1^2)/1000 = 82.9$. For a population with mean $\bar n$ and variance $s^2$ per patch, it equals $\bar n + s^2/\bar n$, so aggregation (a variance-to-mean ratio above 1, 7.19.8) intensifies competition beyond what density suggests. Sessile and modular organisms experience their neighbors more locally still: branches of young firs facing a neighboring tree grew less than branches on the opposite side, which grew like those of isolated trees (Devine & Harrington 2011).

## 11.2. Density-Dependent Mortality, Fecundity and Growth

### 11.2.1. Density Dependence

**Definition 11.2.1 (Density Dependence)** A demographic rate (per capita birth, death, growth or emigration rate) is **density dependent** if it changes with population density, and *density independent* if it does not. In the narrow sense used for regulation, density dependence means that per capita mortality increases, or per capita birth rate decreases, with density, so that the per capita growth rate declines; the opposite relation at low density is *inverse density dependence*, the Allee effect of 7.19.10.

Each demographic rate shows density dependence when competition is intense.

- *Mortality.* In the barnacle *Semibalanus balanoides* on a rocky shore in north Wales, the number of adults surviving two years after settlement increased with the number of settling recruits up to about 30 per cm², and declined at higher densities (Jenkins et al. 2008). The per capita mortality rate was constant at the lowest densities (density independent), then rose increasingly steeply. In the yellow star thistle *Centaurea solstitialis* in California, the number of surviving seedlings rose with seed density and then leveled off (Swope & Parker 2010).
- *Fecundity.* Seeds per plant of the dune annual *Vulpia fasciculata* were constant at low density and declined at higher density, though not enough to stop the total number of seeds from rising (Watkinson & Harper 1978). In the southern pine beetle (*Dendroctonus frontalis*), eggs per attack declined with attack density so that the total number of eggs laid per unit bark area was roughly constant.
- *Growth.* Monarch butterfly pupae (*Danaus plexippus*) reared at more than about two eggs per plant were smaller (Flockhart et al. 2012); smaller individuals usually survive and reproduce less, so that effects on growth precede those on survival and fecundity.

### 11.2.2. Under-, Exact and Overcompensation

The examples differ in how strongly the rates respond to density, and the difference can be expressed precisely. Let $B$ be the number of individuals before a density-dependent process acts ("before") and $A$ the number after it. For mortality, $B$ is the initial number and $A$ the number of survivors; for fecundity, $B$ is the number of offspring that would have been produced without competition and $A$ the number actually produced; for growth, $B$ and $A$ are potential and actual biomass. As in a life table (7.19.9), the killing power of the process is
$$
k = \lg B - \lg A = \lg\frac{B}{A}. \tag{11.1}
$$

**Definition 11.2.2 (Compensation)** Density dependence is *undercompensating* if $A$ increases with $B$, *exactly compensating* if $A$ is independent of $B$, and *overcompensating* if $A$ decreases as $B$ increases. Exact compensation, with a constant number of winners, is also called *contest competition*; the extreme of overcompensation, in which all competitors are so harmed that none survive, is called *scramble competition* (Nicholson 1954).

**Proposition 11.2.1 (Compensation and the Slope of $k$)** Let $b = \mathrm{d}k/\mathrm{d}\lg B$ be the slope of $k$ plotted against $\lg B$. Then $\mathrm{d}\lg A/\mathrm{d}\lg B = 1 - b$, so the density dependence is absent if $b = 0$, undercompensating if $0 < b < 1$, exactly compensating if $b = 1$ and overcompensating if $b > 1$; scramble corresponds to $b \to \infty$.

**Proof** From Eq. (11.1), $\lg A = \lg B - k$; differentiating with respect to $\lg B$ gives $\mathrm{d}\lg A/\mathrm{d}\lg B = 1 - b$. $A$ increases with $B$ iff this is positive ($b < 1$), is constant iff $b = 1$, and decreases iff $b > 1$. If $b = 0$, $k$ is constant, so the proportion surviving $A/B = 10^{-k}$ does not depend on density. $\square$

Plotting $k$ against $\lg B$ is therefore the standard diagnostic of density dependence (the same plot is used in key factor analysis, 7.19.9). Typically $k$ is constant at low density (no competition), then rises with a slope that increases with density. Data from many species fall along the continuum: seedling mortality of *Androsace septentrionalis* in Poland is undercompensating at intermediate and exactly compensating at high densities ($b \to 1$); early-instar mortality of the European corn borer (*Ostrinia nubilalis*) overcompensates throughout ($b > 1$); spore production of the fungus *Metschnikowia bicuspidata* in its host *Daphnia magna* shows a $b$ rising toward infinity, near-scramble (Begon & Townsend 2021, from the original studies).

![Forms of density dependence (Definition 11.2.2), computed with the mortality function A = B/(1 + (aB)^b), a = 0.01. A: survivors against initial density: proportional (b = 0, density independent), still rising (b = 0.5, undercompensation), leveling off at 1/a = 100 (b = 1, exact compensation or contest), and declining (b = 2, overcompensation; b = 5, close to scramble). B: k = lg B − lg A against lg B: constant at low density, then rising with a slope that approaches b (Proposition 11.2.1). C: the per capita mortality rate −ln(A/B) increases with density in all density-dependent cases](./plots/compensation.py)

## 11.3. Quantifying Intraspecific Competition

### 11.3.1. Models of Competition with Discrete Generations

For a population with discrete generations, competition can be written into the geometric growth model $N_{t+1} = \lambda N_t$ (7.19.10) by making the realized reproductive rate decline with density. The simplest choice makes the *reciprocal* of the generation increase rise linearly with density, from $1/\lambda$ at $N_t = 0$ to 1 at $N_t = K$:
$$
\frac{N_t}{N_{t+1}} = \frac{1}{\lambda} + \frac{1 - 1/\lambda}{K}N_t \quad\Longrightarrow\quad N_{t+1} = \frac{\lambda N_t}{1 + aN_t}, \qquad a = \frac{\lambda - 1}{K}. \tag{11.2}
$$
This is the *Beverton–Holt model* (Beverton & Holt 1957, for fish stocks). Its competition term is easily read in $k$ values: the potential number produced is $\lambda N_t$ and the actual number $\lambda N_t/(1 + aN_t)$, so $k = \lg(1 + aN_t)$, whose slope against $\lg N_t$ rises from 0 to 1. The Beverton–Holt model therefore describes exactly compensating competition at high density, and it always approaches $K$ monotonically (7.19.12). A parameter for the type of competition is added in two standard ways.

**Formula 11.3.1 (Models of Intraspecific Competition)** With $\lambda$ the per capita reproductive rate at low density, $a$ a measure of the susceptibility of individuals to crowding and $b$ the type of density dependence:

| Model | $N_{t+1}$ | $k$ | Slope of $k$ at high density |
|---|---|---|---|
| Beverton–Holt (1957) | $\lambda N_t/(1 + aN_t)$ | $\lg(1 + aN_t)$ | 1 |
| Hassell (1975) | $\lambda N_t/(1 + aN_t)^b$ | $b\lg(1 + aN_t)$ | $b$ |
| Maynard Smith–Slatkin (1973) | $\lambda N_t/[1 + (aN_t)^b]$ | $\lg[1 + (aN_t)^b]$ | $b$ |

The equilibria are $N^* = (\lambda^{1/b} - 1)/a$ (Hassell) and $N^* = (\lambda - 1)^{1/b}/a$ (Maynard Smith–Slatkin).

**Proof** For the Hassell model, $\mathrm{d}k/\mathrm{d}\lg N = b\,aN/(1 + aN) \to b$ as $N \to \infty$; for the Maynard Smith–Slatkin model, $\mathrm{d}k/\mathrm{d}\lg N = b\,(aN)^b/[1 + (aN)^b] \to b$. The equilibria solve $\lambda(1 + aN^*)^{-b} = 1$ and $\lambda/[1 + (aN^*)^b] = 1$. $\square$

The two-parameter view emphasized by Kuno (1991) is useful here: the dynamics are determined by properties of individuals (their reproductive rate $\lambda$, their susceptibility to crowding $a$ and the way that susceptibility rises with density, $b$), and the carrying capacity is an outcome of these properties, not a separate parameter. In particular, $a$ sets only the *level* of the equilibrium, while $\lambda$ and $b$ determine its *stability*: the more strongly density dependence overcompensates, and the higher $\lambda$, the more prone the population is to overshoot, oscillate and fluctuate chaotically. This is the subject of the next chapter. Fitted to life tables of insects, the Hassell and Maynard Smith–Slatkin models describe the observed density dependence well with values of $b$ from below 0.5 to above 3 (Bellows 1981).

### 11.3.2. Net Recruitment and Regulation

Competition can also be viewed through numbers rather than rates. With density-dependent per capita birth and death rates $b(N)$ and $d(N)$ in continuous time, the numbers born and dying per unit time are $b(N)N$ and $d(N)N$, and their difference is the *net recruitment*. It is small at low density (few parents), large at intermediate density, zero at $K$ and negative above: an n-shaped (domed) curve. For the logistic, it is the parabola $rN(1 - N/K)$ with its peak at $K/2$; for the Beverton–Holt model, the net recruitment per generation $F(N) - N = \lambda N/(1 + aN) - N$ peaks where $F'(N) = \lambda/(1 + aN)^2 = 1$, at $N = (\sqrt\lambda - 1)/a$, which lies below $K/2$ because $(\sqrt\lambda - 1)/(\lambda - 1) = 1/(\sqrt\lambda + 1) < 1/2$. Successive generations climb the curve in steps that are small at first, large around the peak, and small again near $K$: this is how density dependence produces sigmoidal growth.

**Proposition 11.3.1 (Regulation by Density-Dependent Birth and Death)** Let $\dot N = [b(N) - d(N)]N$ with continuously differentiable per capita rates, and let $K > 0$ satisfy $b(K) = d(K)$. Then $K$ is a locally stable equilibrium if $b'(K) < d'(K)$ and unstable if $b'(K) > d'(K)$. In particular, $K$ is stable when either rate is density dependent in the regulating direction ($b' < 0$ or $d' > 0$) and the other is density independent.

**Proof** Write $f(N) = [b(N) - d(N)]N$. Then $f'(K) = [b'(K) - d'(K)]K + [b(K) - d(K)] = [b'(K) - d'(K)]K$, which is negative iff $b'(K) < d'(K)$; by the linearization criterion for one-dimensional equations (7.19.10, Proposition 10.2.3) this gives local stability. $\square$

Natural populations do not have a single sharp $K$. Birth and death rates scatter around their trends because of weather, food and enemies, and they may balance over a range of densities rather than at one point; intraspecific competition then keeps the population within limits rather than at an equilibrium. Dome-shaped net recruitment curves have been documented for brown trout (*Salmo trutta*) in an English stream (Elliott 1994), for the wildebeest (*Connochaetes taurinus*) of the Serengeti, whose recruitment declined above about one million animals because of dry-season food shortage (Mduma et al. 1999), and, for modules, for leaf area in stands of subterranean clover. In Soay sheep (*Ovis aries*) on St Kilda, an integral projection model combining density-dependent growth, survival and fecundity predicts that the population growth rate $\ln R$ falls to zero at about 455 sheep, the estimated carrying capacity. The peak of the net recruitment curve is where a population is most productive, which is why harvesting theory aims to hold exploited populations at that density (7.19.53).

![Net recruitment and regulation (Section 11.3.2). A: linear density-dependent per capita birth rate b(N) = 0.9 − 0.004N and death rate d(N) = 0.1 + 0.004N cross at the carrying capacity K = 100; below K births exceed deaths and the population increases, above K it decreases (arrows; Proposition 11.3.1). B: the corresponding numbers: births b(N)N and deaths d(N)N per unit time, and net recruitment, a dome with its maximum at K/2. C: in the Beverton–Holt model (λ = 4, a = 0.03, K = 100) the population started at N₀ = 2 climbs the net recruitment curve F(N) − N in successive steps, largest near the peak at (√λ − 1)/a = 33; the inset shows the resulting S-shaped growth](./plots/net-recruitment.py)

## 11.4. Density Effects in Plants

Plants cannot escape crowding, and they respond to it with great plasticity. At low density a plant branches freely and produces many modules; at high density each plant is smaller, with fewer branches, leaves and seeds, and some die. Two empirical regularities summarize these responses.

### 11.4.1. The Law of Constant Final Yield

**Definition 11.4.1 (Law of Constant Final Yield)** The **law of constant final yield** states that, over a wide range of sowing densities and under the same conditions, the total biomass per unit area $Y = d\bar w$ of a plant stand at the end of growth is nearly independent of the density $d$: the mean mass per plant $\bar w$ decreases in inverse proportion to density, so that $\lg\bar w = \lg Y - \lg d$ has slope $-1$.

Carrots (*Daucus carota*) sown at a range of densities illustrate it (Li et al. 1996). At the first harvest, 29 days after sowing, yield per pot still increased with sowing density; after 62, 76 and 90 days it was the same over a wide range of densities, at a level that increased with the nutrient supply, showing that the constant yield is set by limiting resources. In *Vulpia fasciculata* (Watkinson 1984), $\lg\bar w$ was nearly independent of $\lg d$ early in the season and approached a slope of $-1$ by June. The constancy arises largely through modules: when perennial ryegrass (*Lolium perenne*) was sown over a 30-fold range of densities, the final densities of tillers varied far less than those of plants (Kays & Harper 1974). It holds for total biomass; the yield of seeds often declines at high density, because crowded plants allocate less to reproduction.

Shinozaki and Kira (1956) explained the law with a logistic model of stand growth, which also gives the shape of the yield–density relationship before the final harvest.

**Proposition 11.4.1 (Shinozaki–Kira Reciprocal Equation)** Suppose that the biomass per unit area $Y = d\bar w$ of a stand grows logistically, $\mathrm{d}Y/\mathrm{d}t = \lambda Y(1 - Y/\hat Y)$, with the same rate $\lambda$ and the same ceiling $\hat Y$ at every density, starting from $Y_0 = dw_0$. Then at every time the mean plant mass satisfies the *reciprocal yield–density equation*
$$
\frac{1}{\bar w} = A(t) + B(t)\,d, \qquad A(t) = \frac{\mathrm{e}^{-\lambda t}}{w_0}, \qquad B(t) = \frac{1 - \mathrm{e}^{-\lambda t}}{\hat Y}, \tag{11.3}
$$
and as $t \to \infty$, $\bar w \to \hat Y/d$: the final yield is constant.

**Proof** The logistic equation for $Y$ is linear in $1/Y$: with $z = 1/Y$, $\dot z = -\dot Y/Y^2 = -\lambda(z - 1/\hat Y)$, so $z = 1/\hat Y + (z_0 - 1/\hat Y)\mathrm{e}^{-\lambda t}$ with $z_0 = 1/(dw_0)$. Then $1/\bar w = d/Y = dz = d/\hat Y + (1/w_0 - d/\hat Y)\mathrm{e}^{-\lambda t}$, which is Eq. (11.3). As $t \to \infty$, $A \to 0$ and $B \to 1/\hat Y$, so $d\bar w \to \hat Y$. $\square$

The equation $1/\bar w = A + Bd$, or its equivalent $Y = d/(A + Bd)$, describes yield–density data of many crops well: yield rises almost linearly with density at low density (each plant grows as if alone, $\bar w \approx 1/A$) and saturates at $1/B$ at high density. The parameter $1/A$ is the mass of an isolated plant and $B$ measures the strength of crowding.

![Constant final yield (Proposition 11.4.1): stands grow logistically in biomass per unit area (λ = 0.12 per day, ceiling 1000 g m⁻², 1 g per seedling at sowing). A: log mean plant mass against log density on four days; the curves approach a line of slope −1 at high density, earliest at the highest densities, and the range of densities over which mass is reduced widens as plants grow (compare Definition 11.4.1). B: yield per unit area against density: increasing with density early in the season, constant at the ceiling over a widening range of densities later. C: the reciprocal equation 1/w = A + Bd is a straight line in density at every time, with intercept falling and slope rising toward 1/Ŷ](./plots/yield-density.py)

### 11.4.2. The −3/2 Self-Thinning Rule

The law of constant final yield compares stands sown at different densities at one time. Following a single crowded stand through time shows a different regularity: as the plants grow, some die, and density falls while mean mass rises.

**Definition 11.4.2 (Self-Thinning)** **Self-thinning** is the progressive decline in density of a crowded, growing population caused by density-dependent mortality, in which fewer, larger individuals survive. In many plant stands, the mean mass $\bar w$ and the density $d$ of a self-thinning population follow the relation
$$
\bar w = Cd^{-3/2}, \qquad \lg\bar w = \lg C - \tfrac32\lg d, \tag{11.4}
$$
the −3/2 self-thinning rule (Yoda et al. 1963); equivalently, the biomass per unit area is $Y = d\bar w = Cd^{-1/2}$.

(The rule is sometimes written $\bar w = Cd^{-a}$ with "$a = 2/3$"; the exponent is $3/2$, and $2/3$ is the exponent of the inverse relation $d \propto \bar w^{-2/3}$.)

Sown at five densities, stands of *Lolium perenne* first grew with little mortality, so that their trajectories on a plot of $\lg\bar w$ against $\lg d$ rose almost vertically; as they approached a common line, mortality increased and all stands then moved along it, the highest densities first (Lonsdale & Watkinson 1983). The line that a stand approaches and then follows is its *dynamic thinning line*. A slope steeper than $-1$ means that total biomass still increases during thinning; when it stops increasing, as in the same ryegrass grown at 83% shade, the thinning line has slope $-1$. Lines for different species, from mosses to redwoods, occupy a narrow band in the $(\lg d, \lg\bar w)$ plane with slopes near $-3/2$ (White 1980), but individual slopes vary considerably, and the idea of a universal rule has been abandoned (Weller 1987; Lonsdale 1990). Plots of $\lg\bar w$ against $\lg d$ also contain a statistical artifact, because $\bar w$ is usually computed as $Y/d$, so that $\bar w$ and $d$ are correlated by construction; fitting $\lg Y$ against $\lg d$ (expected slope $-1/2$) avoids it.

**Proposition 11.4.2 (Geometric Basis of the −3/2 Rule)** Suppose that in a closed canopy the ground area occupied per plant is $s = 1/d$, and that plants are geometrically similar, so that the occupied area scales as the square of a linear dimension $L$ and the mass as its cube, $s \propto L^2$, $\bar w \propto L^3$. Then $\bar w \propto d^{-3/2}$. More generally, if $s \propto D^\alpha$ and $\bar w \propto D^\beta$ for some measure of size $D$ (stem diameter), then $\bar w \propto d^{-\beta/\alpha}$.

**Proof** $L \propto s^{1/2} = d^{-1/2}$, so $\bar w \propto L^3 \propto d^{-3/2}$. In general $D \propto s^{1/\alpha} = d^{-1/\alpha}$ and $\bar w \propto D^\beta \propto d^{-\beta/\alpha}$. $\square$

The argument is the areal version of Begon & Townsend's derivation with a constant leaf area index: if the leaf area per unit ground area stays constant once the canopy has closed, the leaf area per plant scales as $1/d$; with leaf area $\propto D^2$ and mass $\propto D^3$ the slope is $-3/2$. Its generalization explains departures from $-3/2$ as departures from geometric similarity. Osawa & Allen (1993) measured the allometric exponents ([7.5.34](/7.5.34)) of individual trees: $\alpha = 2.08$, $\beta = 2.19$ in mountain beech (*Nothofagus solandri*) and $\alpha = 1.63$, $\beta = 2.41$ in red pine (*Pinus densiflora*), predicting thinning slopes of $-1.05$ and $-1.48$; the observed slopes were $-1.06$ and $-1.48$. Red pine follows the "rule", but for the "wrong" reason.

A second explanation comes from metabolic scaling. If an individual's rate of resource use scales with mass as $u \propto \bar w^{3/4}$ (**Kleiber's law**, [7.14.30](/7.14.30)) and a stand at its limit uses the whole resource supply per unit area, $S = d_{\max}u$, then $d_{\max} \propto S\bar w^{-3/4}$, that is $\bar w \propto d^{-4/3}$ at constant supply (Enquist et al. 1998; the metabolic theory of ecology, 7.19.6). The predicted slope is $-4/3$ instead of $-3/2$, and the argument applies to sessile animals as well as plants. Thinning lines of experimental grasshopper cohorts ($-1.29$) and sea trout ($-1.35$) are close to $-4/3$, whereas house crickets (*Acheta domesticus*), whose metabolic exponent is about 0.9 rather than 3/4, thin along a slope of $-1.11$, the reciprocal of their exponent (Jonsson 2017). Mussels ($-1.4$), barnacles ($-1.6$) and tunicates ($-1.5$) on rocky shores, which pack bodies beneath a supply of food falling from above, follow lines near $-3/2$. Neither the areal nor the metabolic argument is universal; both make the slope a consequence of how individuals of different sizes use space and resources.

### 11.4.3. Asymmetric Competition and Size Hierarchies

Competition among plants is seldom equal. In stands of flax (*Linum usitatissimum*) sown at three densities and harvested at three ages, the weights of individual plants were distributed symmetrically when competition was weak, and became increasingly skewed, with many small plants and a few large ones, as density and plant size increased (Obeid et al. 1967). The same pattern appears in fish: in years of high density, cod (*Gadus morhua*) off the Norwegian coast were smaller on average and their length distribution more skewed (Lekve et al. 2002). The inequality of sizes in a population is measured by the Gini coefficient, borrowed from economics,
$$
G = \frac{\sum_i\sum_j\lvert w_i - w_j\rvert}{2n^2\bar w}, \tag{11.5}
$$
the mean absolute difference between two individuals divided by twice the mean: 0 when all are equal, approaching 1 when one individual has everything.

Why should competition produce inequality? In *size-symmetric* competition, each competitor obtains a share of contested resources in proportion to its size, or equal shares; in *size-asymmetric* competition, larger individuals obtain a disproportionate share. Competition for light is strongly asymmetric, because a taller plant shades a shorter one but not vice versa; competition for water and nutrients in the soil is more nearly symmetric, because even a small root system has access to the soil around it. When morning glory vines (*Ipomoea tricolor*) competed only by their roots (in a shared pot), their mean weight fell more than when they competed only by their shoots (intertwined on one stake); but shoot competition increased the inequality of sizes far more (Weiner 1986). A meta-analysis confirmed that root competition is generally more intense but shoot competition more asymmetric (Kiær et al. 2013).

The dynamics of inequality reflect two opposing processes. Asymmetric competition magnifies small initial differences: in experimental stands of the kelp *Laminaria digitata* at high density, small plants grew more slowly than large ones, the reverse of their growth in isolation, so the Gini coefficient of frond lengths increased as the plants grew; later, as the smallest plants died, it decreased again (Creed et al. 1998). Mortality of the smallest individuals truncates the size distribution, so self-thinning and inequality are linked.

![A zone-of-influence model of competing plants (model in the script): each plant occupies a circular zone whose area scales as mass^(2/3); overlapping areas are shared equally (size-symmetric) or almost entirely won by the larger plant (size-asymmetric, p = 8), and growth is proportional to the uncontested share. A: under asymmetric competition, stands sown at 400, 1600 and 6400 plants per unit area grow at first without mortality (vertical trajectories), then converge on a common self-thinning line; the fitted slope of the thinning phase is −1.31, between the −4/3 and −3/2 of Section 11.4.2. B: without mortality (suppressed plants persist at minimal size; solid), the Gini coefficient of plant mass rises much faster and higher under asymmetric competition; with mortality of suppressed plants (dashed) it rises only briefly and then falls, because the deaths remove the small end of the distribution. C: size distributions without mortality at t = 60: asymmetric competition produces a few large dominants and many suppressed plants (note the logarithmic scale), symmetric competition a more compact distribution](./plots/self-thinning-ibm.py)

Asymmetry also strengthens regulation, much as contest competition does. In a population of the perennial herb *Anemone hepatica* in a Swedish forest, followed plant by plant from 1943 to 1956 (Tamm 1956), 28 of the 30 plants that were large or intermediate in 1943 survived to 1956, while of the 112 plants that were small in 1943 or appeared as seedlings later, only 26 survived and none flowered. The established plants were winners year after year; the variable crop of seedlings were losers that grew little and usually died. The number of reproducing adults therefore stayed nearly constant while the number of seedlings fluctuated, the pattern also typical of tree populations, in which a few established adults have high survival and fecundity and the many seedlings and saplings almost none.

## 11.5. Consequences of Intraspecific Competition

### 11.5.1. Territoriality

A **territory** is an area defended by an individual or group against intruders ([7.18.26](/7.18.26)). Territoriality is a contest: individuals that hold territories breed, and those that do not, the floaters, often make no contribution to the next generation. Since the number of territories is limited, territoriality keeps the number of breeders comparatively constant and regulates the population, like other forms of asymmetric competition. The number of territories, and especially of productive ones, may still vary with resources: in tawny owls (*Strix aluco*) in Finland, the proportion of territories in which the owners bred successfully increased with vole abundance (Karell et al. 2009), and lion (*Panthera leo*) territories in Zimbabwe were smaller where prey biomass was higher (Loveridge et al. 2015). Floaters are not always losers: in black kites (*Milvus migrans*) in Doñana, floaters were mainly young birds of normal size and condition, deferring rather than forgoing reproduction. Wynne-Edwards (1962) argued that territoriality evolved because it prevents populations from overexploiting their resources; this group-selection explanation was rejected because a behavior that benefits the population at the expense of the individual cannot spread by **natural selection** ([7.4.23](/7.4.23)). Territoriality persists because it benefits the individuals that defend territories, and its regulating effect on the population is a consequence, not its cause. The management of territorial species therefore depends on the availability of territories: bearded vultures (*Gypaetus barbatus*) reintroduced to the Alps first ranged where ibex carcasses were abundant, but settled to breed where limestone cliffs offered nest sites (Hirzel et al. 2004).

### 11.5.2. Dispersal

Emigration rates often increase with density, so that competition drives individuals away from crowded places. Density-dependent **dispersal** ([7.10.10](/7.10.10#def-10.2.1)) relieves competition locally, spreads the population into unoccupied habitat, and links local populations in metapopulations (7.19.16).

### 11.5.3. Individuals and Evolution

For individuals, competition reduces growth, survival and reproduction, and its burden falls mainly on the weaker competitors. It also determines the selective environment: in populations that live near carrying capacity, natural selection favors traits that improve performance under crowding, the basis of **K-selection** ([7.10.15](/7.10.15#def-15.2.1)), and competitive ability, the size of seeds and the timing of germination and emergence evolve accordingly. Intraspecific competition is often said to "benefit the population" by eliminating weaker individuals; the accurate statement is that it is a cause of selection among individuals, with consequences for the population (regulation, a more resource-efficient phenotype), not an adaptation of the population.

### 11.5.4. Regulation

Above all, intraspecific competition is a density-dependent process that can regulate population size around a carrying capacity (Proposition 11.3.1). Whether it does so smoothly or with oscillations depends on how strongly it compensates: exact compensation (contest, $b = 1$) gives the tightest regulation, overcompensation (scramble) can produce cycles and chaos (7.19.12), and delays in its action produce oscillations even in continuous time (7.19.13).

## Summary

- Intraspecific competition is an interaction through a limiting shared resource (Definition 11.1.1), by exploitation, interference or both; it is density dependent and often asymmetric. Individuals experience the crowding of their neighborhood, which in aggregated populations exceeds the mean density ($\bar n + s^2/\bar n$).
- Density dependence (Definition 11.2.1) affects mortality, fecundity and growth. Its form is measured by the slope $b$ of $k = \lg(B/A)$ against $\lg B$ (Proposition 11.2.1):

| $b$ | Survivors $A$ as $B$ increases | Type |
|---|---|---|
| 0 | proportional to $B$ | density independent |
| $0 < b < 1$ | increase | undercompensating |
| 1 | constant | exact compensation (contest) |
| $b > 1$ | decrease | overcompensating |
| $\to\infty$ | fall to zero | scramble |

- Discrete-generation models (Formula 11.3.1): Beverton–Holt $\lambda N/(1 + aN)$ (exact compensation), Hassell $\lambda N/(1 + aN)^b$ and Maynard Smith–Slatkin $\lambda N/[1 + (aN)^b]$, whose $k$ slopes approach $b$; $a$ sets the equilibrium level, $\lambda$ and $b$ its stability.
- Net recruitment is dome-shaped; $K$ is stable where $b'(K) < d'(K)$ (Proposition 11.3.1).
- Plants obey the law of constant final yield (Definition 11.4.1), explained by logistic growth of stand biomass, which gives the reciprocal equation $1/\bar w = A + Bd$ (Proposition 11.4.1), and the self-thinning relation $\bar w = Cd^{-3/2}$ (Definition 11.4.2), derived from geometric similarity (Proposition 11.4.2); allometric departures change the slope, and metabolic scaling predicts $-4/3$.
- Asymmetric competition, especially for light, magnifies size differences (Gini coefficient, Eq. (11.5)); mortality of the smallest reduces inequality again. Asymmetry and territoriality make the number of successful breeders nearly constant and so strengthen regulation; these consequences follow from selection on individuals, not from benefits to the population.

## Questions

1. In an experiment, groups of $B = 10, 30, 100, 300, 1000$ larvae of a beetle were reared with a fixed amount of food, and the numbers of adults were $A = 9, 24, 50, 60, 35$. Compute $k$, plot it against $\lg B$, and classify the density dependence over the range.

   **Answer** $k = \lg(B/A)$: $0.046$, $0.097$, $0.301$, $0.699$, $1.456$ at $\lg B = 1, 1.48, 2, 2.48, 3$. The slopes between successive points are $0.11$, $0.39$, $0.83$, $1.45$. So mortality is nearly density independent at the lowest densities, undercompensating up to about 100 larvae (slope below 1), close to exact compensation around 100–300 (and $A$ nearly levels off between 100 and 300), and overcompensating at the highest density, where adding larvae reduces the number of adults ($A$ falls from 60 to 35, slope 1.45 > 1).

2. Show that the Beverton–Holt model $N_{t+1} = \lambda N_t/(1 + aN_t)$ can be solved exactly by the substitution $u_t = 1/N_t$. What does the solution say about the approach to $K$?

   **Answer** $u_{t+1} = (1 + aN_t)/(\lambda N_t) = u_t/\lambda + a/\lambda$, a linear recursion with fixed point $u^* = a/(\lambda - 1) = 1/K$. Thus $u_t - 1/K = (u_0 - 1/K)\lambda^{-t}$ and $N_t = K/[1 + (K/N_0 - 1)\lambda^{-t}]$: the discrete analog of the logistic curve (7.19.10), approaching $K$ monotonically and geometrically at rate $1/\lambda$, from below or above, for every $\lambda > 1$. No oscillations are possible, because the model is exactly compensating.

3. A forester records stands of a pine at densities of 10 000, 4000 and 1000 trees per hectare with mean stem masses of 2, 8 and 60 kg. Do these stands lie on a $-3/2$ thinning line? What is wrong with fitting $\lg\bar w$ against $\lg d$, and what would you fit instead?

   **Answer** The slopes between successive points are $(\lg8 - \lg2)/(\lg4000 - \lg10000) = 0.602/(-0.398) = -1.51$ and $(\lg60 - \lg8)/(\lg1000 - \lg4000) = 0.875/(-0.602) = -1.45$, close to $-3/2$. But $\bar w$ was presumably computed as stand biomass divided by density, so errors in counting trees enter both axes and create a spurious negative correlation. Better to fit $\lg Y$ against $\lg d$, where $Y = d\bar w$ is the biomass per hectare: $Y = 20\,000$, $32\,000$ and $60\,000\,\mathrm{kg\,ha^{-1}}$, with slopes $-0.51$ and $-0.45$, close to the expected $-1/2$. Also, these are different stands at one time, so they define a boundary line rather than a dynamic thinning line, unless they are stages of the same stand.

4. Using Proposition 11.4.2, predict the thinning slope for a species whose crown area scales as $D^{1.8}$ and whose mass scales as $D^{2.6}$. Why might the slope also depend on whether competition is size-asymmetric?

   **Answer** $\bar w \propto d^{-\beta/\alpha} = d^{-2.6/1.8} = d^{-1.44}$. The geometric argument treats all survivors as equal plants sharing the ground evenly. Under size-asymmetric competition the plants that die are the smallest, which hold little ground and little mass: their death lowers density without freeing much space, so density can fall faster than the canopy share of the survivors grows, and the mean mass rises partly because small plants are removed rather than because survivors grow. Under symmetric competition many plants are suppressed together and mortality begins later and more abruptly. The observed slope therefore reflects the mode of competition as well as allometry; in the zone-of-influence simulation (Section 11.4.3) it is −1.31 rather than the geometric −3/2.

5. (Open) Territorial behavior limits the number of breeding pairs of a bird to the number of territories, and floaters wait for vacancies. Predict how the breeding population and the total population respond to (a) a winter that kills half of all individuals, (b) a reduction in the number of territories by habitat loss.

   **Answer** (a) If floaters outnumber the deaths among territory holders, vacancies are refilled and the breeding population is almost unchanged; only the floater pool shrinks. Losses are buffered (compensated), so even large density-independent mortality may not change the number of breeders; this is the classic removal experiment result in red grouse and great tits, where removed territory owners were rapidly replaced. If the winter kills more than the floaters can replace, the breeding population falls. (b) Habitat loss reduces the ceiling directly: the breeding population falls in proportion to the territories lost, and the floater pool grows at first and then shrinks as recruitment declines. The total population is therefore regulated by the number of territories, so management must protect territories (breeding habitat), not only reduce mortality.
