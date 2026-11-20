---
title: "Interspecific Competition I: The Lotka–Volterra Model"
description: "Interactions between species and their signs; exploitation, interference and apparent competition; examples from protists, flour beetles, salmonids, birds and grazing geese; the Lotka–Volterra competition model derived from the logistic equation, its competition coefficients and nondimensional form; zero net growth isoclines and the four outcomes; equilibria, Jacobians, eigenvalues and global dynamics (Dulac criterion, a Lyapunov function); mutual invasibility; n-species competition, the community matrix and Goh's theorem; measuring competition and the limits of the model."
---

No population lives alone. The individuals of a population eat, are eaten by, compete with and depend on individuals of other species, and the interactions between species connect the population ecology of [7.19.8](/7.19.8)–[7.19.21](/7.19.21) to the community ecology of [7.19.31](/7.19.31) and later chapters. This chapter and the next treat competition between species. Here we classify interactions between species (Section 22.1), survey what competition between species looks like in experiments and in the field (Section 22.2), and then analyze the simplest model of it, the Lotka–Volterra competition model, completely: its construction from the logistic equation (Section 22.3), its isoclines and equilibria, their stability and the global behavior of all trajectories (Section 22.4), and its extension to many species (Section 22.5). Section 22.6 asks how competition coefficients are measured and what the model leaves out. The next chapter ([7.19.23](/7.19.23)) opens the black box of the competition coefficients: niches, resource utilization, consumer–resource models and modern coexistence theory. The mathematics used here, phase planes, linearization and Lyapunov functions, is developed in [2.4.11](/2.4.11); the logistic equation, on which everything is built, in [7.19.10](/7.19.10).

## 22.1. Interactions between Species

### 22.1.1. The Signs of Interactions

An interaction between two species can be classified by its effect on each partner: positive ($+$), if the presence of the other species increases the survival, growth or fecundity of individuals; negative ($-$), if it decreases them; or neutral ($0$). This gives the classical table (Odum; Burkholder 1952):

| Interaction | Species A | Species B | Nature | Chapter |
|---|---|---|---|---|
| Neutralism | $0$ | $0$ | neither affects the other | |
| Competition | $-$ | $-$ | each inhibits the other, through a shared resource or directly | 7.19.22–23 |
| Amensalism | $-$ | $0$ | A is inhibited, B unaffected (e.g. a tree shading a herb) | 7.19.29 |
| Predation, herbivory, parasitism | $+$ | $-$ | A (the consumer) feeds on B | 7.19.24–28 |
| Commensalism | $+$ | $0$ | A benefits, B unaffected | 7.19.29 |
| Mutualism | $+$ | $+$ | both benefit | 7.19.29 |

The table classifies net effects, which may change with conditions: a plant that protects a seedling from drought (facilitation) may compete with it for light later ([7.19.29](/7.19.29)). Ecologists study two consequences of interactions. Their *codynamics* are the effects of the species on each other's abundance and distribution, the subject of this and the following chapters. Their **coevolution** ([7.10.17](/7.10.17)) is the reciprocal evolutionary change of interacting species, each adapting to the other. The two are linked, because evolution can change the parameters of the dynamics (character displacement, [7.19.23](/7.19.23)), and because the dynamics decide which species are there to evolve.

### 22.1.2. Interspecific Competition

**Definition 22.1.1 (Interspecific Competition)** **Interspecific competition** is an interaction between individuals of different species in which the survival, growth or fecundity of individuals of at least one species is reduced as a result of the exploitation of a shared limiting resource, or of interference, by individuals of the other.

The definition parallels that of **intraspecific competition** ([7.19.11](/7.19.11)) and distinguishes the same two mechanisms. In *exploitation competition* individuals interact only through the resource: each depletes what is available to the other, and the effect is indirect. Two phytoplankton species growing on the phosphate of a lake, two seed-eating birds feeding on the same seeds, and plants drawing water from the same soil compete by exploitation. In *interference competition* individuals act directly on each other: they fight, displace one another from foraging or nesting sites, overgrow each other (barnacles and bryozoans on rock), or release toxins. Chemical interference among plants is **allelopathy** ([7.13.26](/7.13.26), [7.19.21](/7.19.21)). The seaweed *Galaxaura filamentosa* on Fijian reefs produces terpenes that damage the coral *Porites cylindrica*, and produces more of them after contact with live coral; the cost is that it then makes fewer anti-herbivore compounds and is eaten more by surgeonfish (Rasher and Hay 2014).

A third interaction has the same sign pattern without any shared resource. Two prey species attacked by a common predator harm each other indirectly: an increase of one prey supports more predators, which then eat more of the other. Holt (1977) called this **apparent competition**; it is treated in [7.19.39](/7.19.39), where it is shown that, for the prey, it is indistinguishable in sign from exploitation competition. The distinction matters in practice. When the removal of sagebrush (*Artemisia*) in Arizona improved the growth of 22 herb species, the result was attributed to competition for water, but the shrubs also sheltered the deer, rodents and insects that grazed the herbs, so the effect may equally have been apparent competition (Connell 1990).

Several general features recur in the examples below.

- *Asymmetry.* Competition between species is usually one-sided: one species is strongly affected and the other little or not at all. In reviews of field experiments, the effect of competition was asymmetric in most pairs studied (Connell 1983; Schoener 1983).
- *Interaction between resources.* Competition for one resource affects competition for another. A plant shaded by a neighbor grows fewer roots and takes up less water and nutrients, which reduces its leaf growth further. In mixtures of maize and pea, root competition reduced pea biomass to 57 % of that grown alone, shoot competition to 90 %, and both together to 53 %, close to the product $0.57 \times 0.90 = 0.51$ (Semere and Froud-Williams 2001).
- *Ecological and evolutionary effects.* Competition can exclude a species from a habitat or reduce its abundance (ecological effects), and it can select for divergence of the competitors (evolutionary effects). Coexisting species that differ in resource use may differ because competition in the past drove them apart, because competition eliminated the species that did not differ, or simply because they evolved independently; Connell (1980) warned against invoking the "ghost of competition past" without evidence. The ecological effects can be tested by experiment, the evolutionary ones only by comparison and, rarely, by selection experiments ([7.19.23](/7.19.23)).

### 22.1.3. Examples

**Example 22.1.1 (Gause's *Paramecium* Experiments)** Gause (1934, 1935) grew ciliates on bacteria in test tubes, replenishing the medium regularly. Grown alone, *Paramecium aurelia* and *P. caudatum* both increased logistically to stable densities. Grown together on the same bacteria, *P. aurelia*, the faster-growing species that made better use of the limited food, increased while *P. caudatum* declined to extinction within about 16 days. Neither species produced substances harmful to the other: the exclusion was by exploitation. When *P. caudatum* was grown with *P. bursaria*, both persisted, at densities lower than when alone: *P. caudatum* fed mainly on bacteria suspended in the medium, *P. bursaria*, which contains symbiotic algae, mainly on yeast cells at the bottom of the tube. These experiments gave the mathematical models of the 1920s their "experimental teeth" and led to the **competitive exclusion principle** ([7.10.17](/7.10.17), [7.19.23](/7.19.23)).

**Example 22.1.2 (Park's Flour Beetles)** Park (1954, 1962) reared the flour beetles *Tribolium confusum* and *T. castaneum* together in containers of flour under six combinations of temperature and humidity. One species always went extinct, and which one depended on climate, but at intermediate climates the outcome was a matter of probability (percentage of replicates won by each species):

| Climate | *T. confusum* | *T. castaneum* |
|---|---|---|
| Hot–moist | 0 | 100 |
| Temperate–moist | 14 | 86 |
| Cold–moist | 71 | 29 |
| Hot–dry | 90 | 10 |
| Temperate–dry | 87 | 13 |
| Cold–dry | 100 | 0 |

Besides eating the flour, the beetles eat each other's eggs and pupae, and each species ate more individuals of the other species than of its own. Section 22.4 shows that this mutual antagonism produces an outcome that depends on the initial densities, and Figure 3B shows that demographic chance then makes the outcome probabilistic.

**Example 22.1.3 (Competition along Gradients)** The Dolly Varden charr (*Salvelinus malma*) and the white-spotted charr (*S. leucomaenis*) live in the streams of Hokkaido, the Dolly Varden farther upstream where the water is colder, with a zone of overlap at intermediate altitudes. In laboratory streams at 12 °C, white-spotted charr were more aggressive, displaced Dolly Varden from favorable foraging positions and grew faster; at 6 °C the two species were more evenly matched, but white-spotted charr survived poorly in cold water even alone (Taniguchi and Nakano 2000). The lower boundary of the Dolly Varden is therefore set by temperature-dependent interference competition, the upper boundary of the white-spotted charr by temperature alone. On a broad scale the two species coexist in the same streams; on a fine scale each is largely confined to its own zone.

**Example 22.1.4 (Invasion by a Superior Competitor)** Cheatgrass (*Bromus tectorum*), introduced from Eurasia to the intermountain grasslands of western North America in the late nineteenth century, germinates in autumn and extends its roots through the winter. By the time the summer drought begins, its roots have depleted the water of the upper soil, and seedlings of the native bluebunch wheatgrass (*Pseudoroegneria spicata*, formerly *Agropyron spicatum*), whose roots grow later, die in large numbers. Cheatgrass has replaced native perennial grasses over large areas, helped by the frequent fires that its dry litter promotes (Harris 1967; Mack 1981).

**Example 22.1.5 (Field Evidence from Birds)** Removal experiments show competition most directly. Orange-crowned warblers (*Leiothlypis celata*) and Virginia's warblers (*L. virginiae*) have overlapping territories in Arizona. On plots from which one species had been removed, the remaining species fledged 78–129 % more young per nest, mainly because it gained access to preferred nest sites and lost fewer nestlings to predators (Martin and Martin 2001). On Daphne Major in the Galápagos, the diets of the medium ground finch (*Geospiza fortis*) and the cactus finch (*G. scandens*) overlapped broadly in wet seasons when seeds were abundant and diverged as food became scarce in dry seasons, especially during the drought of 1977, when the species fell back on the foods each handled best (Boag and Grant 1984). Swan geese (*Anser cygnoides*) and bean geese (*A. fabalis*) winter at Poyang Lake, China, where the swan goose depends on the tubers of submerged plants (*Vallisneria*). As the submerged vegetation declined, swan geese foraged increasingly in the meadows used by bean geese. In mixed flocks swan geese pecked faster but spent markedly less of their time feeding (about 58 % against 80 % over the winter in single-species flocks), whereas bean geese spent slightly more (Wang et al. 2023): degradation of one habitat had created competition in another.

**Example 22.1.6 (Diet Overlap of Sympatric Carnivores)** DNA metabarcoding of scats of up to eight sympatric carnivores at three sites in the Sanjiangyuan region of the Qinghai–Tibet Plateau (snow leopard, leopard, wolf, brown bear, free-ranging dogs, Tibetan fox, red fox and Pallas's cat) showed broad overlap in the prey eaten, dominated by blue sheep, marmots, pikas and livestock, but significant differences in diet composition among species at all sites; species identity explained 14–62 % of the variation in diet (Lu et al. 2023). Diet overlap shows the potential for exploitation competition; whether it is realized depends on whether the shared prey are limiting, which only removal or comparative studies can show.

:::

Competition is not restricted to close relatives. Removing the sea urchin *Diadema antillarum* from experimental reefs in the US Virgin Islands increased the seaweed on which it feeds and, within two months, the numbers of parrotfish and surgeonfish that share this food (Hay and Taylor 1985). Insects colonizing experimental ponds reduced the growth of tadpoles of the Pine Barrens tree frog (*Hyla andersonii*) more than tadpoles of Fowler's toad did (Morin et al. 1988). Closely related species are more similar and so, other things equal, more likely to compete, but other things are often not equal.

## 22.2. Measuring Competition

Experiments on competition are of three kinds. *Field manipulations* remove or add one species and compare the response of the other with control plots; they test competition under natural conditions but are practical mainly for sessile or territorial organisms. *Long-term laboratory experiments* (protists, phytoplankton, flour beetles, *Drosophila*) put the species together and wait for the outcome; they reveal the dynamics but may lack the niche dimensions that allow coexistence in nature. For plants and other long-lived organisms, *single-generation experiments* compare yields:

- in *substitutive* (replacement series) designs the total density is fixed and the proportions of the two species vary (de Wit 1960). The *relative yield* of a species is its yield in the mixture divided by its yield in monoculture at the same total density, and the *relative yield total* (RYT) is the sum of the two. An RYT of 1 means that each species can only replace the other; an RYT above 1 means that the species use resources partly differently, so that the mixture yields more than either monoculture. The grass *Panicum maximum* and the legume *Glycine javanica* had RYT ≈ 1 without inoculation with nitrogen-fixing root-nodule bacteria and RYT > 1 with it, when the legume had access to atmospheric nitrogen (de Wit et al. 1966);
- in *additive* designs one species (often a crop) is sown at a fixed density and the density of the other (a weed) varies; total density and proportion change together;
- in *response-surface* designs both densities vary independently, and a competition model is fitted to the whole surface. This is the only single-generation design from which competition coefficients can be estimated without strong assumptions.

The quantities estimated by these designs are competition coefficients, the subject of the model that follows.

## 22.3. The Lotka–Volterra Competition Model

### 22.3.1. Construction

The model of Volterra (1926) and Lotka (1932) extends the logistic equation ([7.19.10](/7.19.10)) to two species. In the logistic equation for species 1,

$$
\frac{\mathrm{d}N_1}{\mathrm{d}t} = r_1N_1\,\frac{K_1 - N_1}{K_1},
$$

the term $N_1$ in the numerator represents the inhibition of species 1 by its own members: each individual uses a share $1/K_1$ of the capacity of the environment. Suppose that one individual of species 2 inhibits species 1 as much as $\alpha_{12}$ individuals of species 1 do. If 10 individuals of species 2 have, between them, the effect of a single individual of species 1, then $\alpha_{12} = 0.1$. The total inhibition of species 1 is then that of $N_1 + \alpha_{12}N_2$ individuals of species 1, and the logistic term becomes $(K_1 - N_1 - \alpha_{12}N_2)/K_1$.

**Definition 22.3.1 (Competition Coefficient)** In a model of competing populations, the **competition coefficient** $\alpha_{ij}$ is the per capita effect of species $j$ on the growth rate of species $i$, measured in units of the per capita effect of species $i$ on itself. $\alpha_{ij} < 1$ means that an individual of species $j$ inhibits species $i$ less than an individual of species $i$ does; $\alpha_{ij} > 1$ means that it inhibits more.

Chinese textbooks write $\alpha$ for $\alpha_{12}$ and $\beta$ for $\alpha_{21}$; the double-index notation extends to many species. With it the model is the **Lotka–Volterra model** of competition:

**Definition 22.3.2 (Lotka–Volterra Competition Model)** The Lotka–Volterra competition model for two species of densities $N_1(t), N_2(t) \ge 0$ is

$$
\frac{\mathrm{d}N_1}{\mathrm{d}t} = r_1N_1\,\frac{K_1 - N_1 - \alpha_{12}N_2}{K_1},\qquad
\frac{\mathrm{d}N_2}{\mathrm{d}t} = r_2N_2\,\frac{K_2 - N_2 - \alpha_{21}N_1}{K_2},
\tag{22.1}
$$
where $r_i > 0$ is the intrinsic rate of increase and $K_i > 0$ the carrying capacity of species $i$ when alone, and $\alpha_{12}, \alpha_{21} \ge 0$ are the competition coefficients.

The model inherits all the assumptions of the logistic equation ([7.19.10](/7.19.10)): no age structure or time lags, a constant environment, per capita growth rates that decline linearly with density, and in addition interspecific effects that are linear in the density of the competitor and independent of the density of the species affected. It says nothing about the mechanism of competition, whether exploitation or interference, and it contains no resources. These are its weaknesses (Section 22.6), but they are also what make it a general caricature of any competition, whose analysis clarifies what the possible outcomes are and which combinations of parameters decide between them.

An equivalent form, often used in modern work, writes per capita effects directly: $\dot N_i = r_iN_i(1 - a_{ii}N_i - a_{ij}N_j)$ with $a_{ii} = 1/K_i$ and $a_{ij} = \alpha_{ij}/K_i$. The quantity $1/K_i$ measures the intensity of intraspecific competition in species $i$ (a small carrying capacity means that each individual inhibits its own species strongly), and $\alpha_{ij}/K_i$ the intensity of the interspecific competition that species $j$ exerts on species $i$. The outcome of competition depends, as we shall see, on how these intensities compare.

### 22.3.2. Nondimensional Form

Measuring each density in units of its own carrying capacity and time in units of $1/r_1$,

$$
x = \frac{N_1}{K_1},\quad y = \frac{N_2}{K_2},\quad \tau = r_1t,\qquad
a = \alpha_{12}\frac{K_2}{K_1},\quad b = \alpha_{21}\frac{K_1}{K_2},\quad \rho = \frac{r_2}{r_1},
$$

turns (22.1) into

$$
\frac{\mathrm{d}x}{\mathrm{d}\tau} = x(1 - x - ay),\qquad \frac{\mathrm{d}y}{\mathrm{d}\tau} = \rho\,y(1 - y - bx).
\tag{22.2}
$$

Six parameters have become three, and the outcome of competition will depend only on $a$ and $b$: $\rho$ changes how fast trajectories move, not where they go. The parameter $a$ is the inhibition of species 1 by species 2 when species 2 is at its carrying capacity, relative to the inhibition of species 1 by itself at its own carrying capacity; $a < 1$ means that a population of species 2 at $K_2$ is not enough to stop species 1 from growing when rare. Equivalently, $a < 1$ if and only if $K_2 < K_1/\alpha_{12}$.

### 22.3.3. Zero Net Growth Isoclines

The behavior of (22.1) can be read from a diagram of $N_2$ against $N_1$ (Figure 1), in which every point is a possible pair of densities.

**Definition 22.3.3 (Zero Net Growth Isocline)** For a model of interacting populations, the **zero net growth isocline** (ZNGI, zero isocline; the nullcline of [7.6.33](/7.6.33)) of species $i$ is the set of states, other than $N_i = 0$, at which the per capita growth rate of species $i$ is zero. It separates the states at which species $i$ increases from those at which it decreases.

For species 1, $\dot N_1 = 0$ with $N_1 > 0$ when $N_1 + \alpha_{12}N_2 = K_1$, a straight line with intercepts $N_1 = K_1$ on the $N_1$ axis (species 1 alone at its carrying capacity) and $N_2 = K_1/\alpha_{12}$ on the $N_2$ axis (the density of species 2 that just stops species 1 from growing when it is rare). Below and to the left of the line, competition is weak and $N_1$ increases (horizontal arrows pointing right); above and to the right, $N_1$ decreases. The isocline of species 2, $N_2 + \alpha_{21}N_1 = K_2$, has intercepts $K_2$ on the $N_2$ axis and $K_2/\alpha_{21}$ on the $N_1$ axis; below it $N_2$ increases (arrows pointing up). The arrows are vectors with both components, and their sum at each point gives the direction in which the pair of densities moves. In the nondimensional variables (22.2) the isoclines are $x + ay = 1$ and $bx + y = 1$.

The two lines can be arranged in four ways relative to each other, determined by the order of their intercepts on each axis, and each arrangement gives a different outcome (Figure 1).

![The four outcomes of Lotka–Volterra competition, with K1 = K2 = 100, r1 = 1 and r2 = 0.8. Blue: zero net growth isocline of species 1; orange: of species 2; gray: direction field; black: trajectories from several initial densities; filled points: stable equilibria; open points: unstable equilibria. A: the isocline of species 1 lies outside that of species 2 (K1 > K2/α21, K2 < K1/α12), and species 1 excludes species 2 from every start. B: the reverse, species 2 wins. C: the isoclines cross with K1 > K2/α21 and K2 > K1/α12; the crossing point is a saddle, and its stable manifold (dashed) divides the plane into the basins of attraction of the two exclusion equilibria. D: the isoclines cross with K1 < K2/α21 and K2 < K1/α12, and all trajectories approach the stable coexistence equilibrium](./plots/lv-competition-outcomes.py)

## 22.4. Equilibria, Stability and the Four Outcomes

### 22.4.1. Equilibria and Their Local Stability

We work with (22.2). Its **equilibrium points** in the closed positive quadrant are the origin $E_0 = (0, 0)$, the two single-species equilibria $E_1 = (1, 0)$ and $E_2 = (0, 1)$, and, when $ab \ne 1$, the intersection of the two isoclines,

$$
E^* = (x^*, y^*) = \left(\frac{1 - a}{1 - ab},\ \frac{1 - b}{1 - ab}\right),
\tag{22.3}
$$
which lies in the open quadrant if and only if $a < 1, b < 1$ or $a > 1, b > 1$. In the original units, $N_1^* = (K_1 - \alpha_{12}K_2)/(1 - \alpha_{12}\alpha_{21})$ and $N_2^* = (K_2 - \alpha_{21}K_1)/(1 - \alpha_{12}\alpha_{21})$.

The **Jacobian matrix** of (22.2) is

$$
J(x, y) = \begin{bmatrix} 1 - 2x - ay & -ax \\ -\rho by & \rho(1 - 2y - bx) \end{bmatrix}.
$$

**Theorem 22.4.1 (Local Stability of the Equilibria)** For the system (22.2) with $a, b, \rho > 0$:

1. $E_0$ is an unstable node, with eigenvalues $1$ and $\rho$.
2. $E_1$ has eigenvalues $-1$ and $\rho(1 - b)$: it is a stable node if $b > 1$ and a saddle if $b < 1$.
3. $E_2$ has eigenvalues $-\rho$ and $1 - a$: it is a stable node if $a > 1$ and a saddle if $a < 1$.
4. If $a < 1$ and $b < 1$, $E^*$ is a stable node. If $a > 1$ and $b > 1$, $E^*$ is a saddle.

**Proof** At $E_0$, $J = \operatorname{diag}(1, \rho)$. At $E_1$,

$$
J(1, 0) = \begin{bmatrix} -1 & -a \\ 0 & \rho(1 - b) \end{bmatrix},
$$
an upper triangular matrix whose eigenvalues are its diagonal entries; $E_2$ is analogous. At $E^*$, using $1 - x^* - ay^* = 0$ and $1 - y^* - bx^* = 0$, the Jacobian simplifies to

$$
J^* = \begin{bmatrix} -x^* & -ax^* \\ -\rho by^* & -\rho y^* \end{bmatrix},\qquad
\operatorname{tr} J^* = -x^* - \rho y^*,\qquad \det J^* = \rho x^*y^*(1 - ab).
$$

When $E^*$ is interior, $x^*, y^* > 0$, so the trace is negative. If $a, b < 1$ then $ab < 1$ and the determinant is positive: both eigenvalues have negative real parts (the trace–determinant criterion, [2.4.11](/2.4.11)). Moreover the discriminant $(\operatorname{tr} J^*)^2 - 4\det J^* = (x^* - \rho y^*)^2 + 4\rho abx^*y^* > 0$, so the eigenvalues are real and $E^*$ is a node, not a focus. If $a, b > 1$, then $ab > 1$, the determinant is negative and $E^*$ is a saddle. $\square$

The eigenvalue $\rho(1 - b)$ at $E_1$ has a direct biological meaning. It is the per capita growth rate of species 2 when it is rare and species 1 is at its carrying capacity: $\dot y/y = \rho(1 - y - bx) \to \rho(1 - b)$ as $y \to 0$ at $x = 1$. It is the *invasion growth rate* of species 2 into a resident population of species 1. Similarly $1 - a$ is the invasion growth rate of species 1 into species 2. The local stability of the single-species equilibria is therefore a statement about invasion: species 1 cannot be invaded by species 2 if and only if $b > 1$.

### 22.4.2. Global Dynamics

Local stability does not say where trajectories that start far from an equilibrium end up. For (22.2) the global answer is simple, because the system can have no oscillations.

**Theorem 22.4.2 (Global Dynamics of Lotka–Volterra Competition)** Every solution of (22.2) with $x(0) > 0$, $y(0) > 0$ remains positive and bounded and converges to an equilibrium. There are no periodic orbits in the open positive quadrant.

**Proof** The axes are invariant (if $x = 0$ then $\dot x = 0$), so positive solutions stay positive. Since $\dot x \le x(1 - x)$, $x(\tau)$ is bounded by the solution of the logistic equation and eventually stays below $1 + \varepsilon$ for any $\varepsilon > 0$; likewise $y$. Solutions are therefore defined for all $\tau \ge 0$ and enter the compact box $[0, 1 + \varepsilon]^2$.

To exclude periodic orbits we use the *Dulac criterion*, a generalization of Bendixson's criterion ([2.4.11](/2.4.11)): if there is a continuously differentiable function $B(x, y)$ on a simply connected region such that the divergence of $(BF, BG)$, where $(F, G)$ is the vector field, has constant sign and is not identically zero, the region contains no closed orbit. With $B = 1/(xy)$ on the open quadrant,

$$
\frac{\partial}{\partial x}\left(\frac{1 - x - ay}{y}\right) + \frac{\partial}{\partial y}\left(\frac{\rho(1 - y - bx)}{x}\right) = -\frac{1}{y} - \frac{\rho}{x} < 0.
$$

Hence there is no periodic orbit, nor any cycle of equilibria and connecting orbits enclosing a region of the open quadrant (the same divergence argument applies to any such closed curve). By the Poincaré–Bendixson theorem the $\omega$-limit set of a bounded positive trajectory, which is nonempty, compact and invariant, then consists of equilibria, and since the equilibria are finitely many and isolated (for $ab \ne 1$) and the $\omega$-limit set is connected, it is a single equilibrium. $\square$

The theorem, together with Theorem 22.4.1, determines all outcomes. A trajectory can converge only to a stable equilibrium, or to a saddle along its stable manifold (a set of measure zero of initial conditions), and never to the unstable node $E_0$ from positive initial densities.

**Theorem 22.4.3 (The Four Outcomes)** For positive initial densities, the solutions of (22.1) behave as follows.

| Case | Condition (scaled) | Condition (original) | Outcome |
|---|---|---|---|
| 1 | $a < 1$, $b > 1$ | $K_2 < K_1/\alpha_{12}$, $K_1 > K_2/\alpha_{21}$ | species 1 excludes species 2: $(N_1, N_2) \to (K_1, 0)$ |
| 2 | $a > 1$, $b < 1$ | $K_2 > K_1/\alpha_{12}$, $K_1 < K_2/\alpha_{21}$ | species 2 excludes species 1: $(N_1, N_2) \to (0, K_2)$ |
| 3 | $a > 1$, $b > 1$ | $K_2 > K_1/\alpha_{12}$, $K_1 > K_2/\alpha_{21}$ | bistability: convergence to $(K_1, 0)$ or $(0, K_2)$, depending on which side of the stable manifold of the saddle $E^*$ the initial point lies |
| 4 | $a < 1$, $b < 1$ | $K_2 < K_1/\alpha_{12}$, $K_1 < K_2/\alpha_{21}$ | stable coexistence: $(N_1, N_2) \to (N_1^*, N_2^*)$ |

**Proof** In case 1 there is no interior equilibrium; $E_1$ is a stable node, $E_2$ a saddle whose stable manifold is the $y$ axis, and $E_0$ is repelling. By Theorem 22.4.2 every positive trajectory converges to an equilibrium, and the only one it can reach is $E_1$. Case 2 is symmetric. In case 3, $E_1$ and $E_2$ are stable nodes and $E^*$ a saddle; the two branches of its stable manifold run from $E^*$ to $E_0$ and to infinity (backward in time) and divide the quadrant into two open regions, each the basin of attraction of one of $E_1$, $E_2$. In case 4, $E_1$ and $E_2$ are saddles whose stable manifolds are the axes, and the only remaining attractor is $E^*$. $\square$

Figure 2A shows the four outcomes in the plane of $a$ and $b$, and Figure 3A the corresponding time courses. The degenerate cases $a = 1$ or $b = 1$ (isoclines touching on an axis) and $a = b = 1$ (isoclines coinciding, a line of neutrally stable equilibria) separate them.

![Outcomes of competition in the plane of the scaled competition coefficients a = α12K2/K1 and b = α21K1/K2. A: the lines a = 1 and b = 1 divide the plane into the four outcomes; species 1 can invade species 2 if a < 1, species 2 can invade species 1 if b < 1, so coexistence is mutual invasibility and bistability is mutual non-invasibility. The interior equilibrium exists in the coexistence and bistable quadrants and moves to infinity on the curve ab = 1 (dashed). Points: the four cases of Figure 1. B: equilibrium densities for K1 = K2 = 100 and α12 = 0.5 as the per capita effect α21 of species 1 on species 2 increases: N2* falls and N1* rises until, at α21 = 1, the coexistence equilibrium reaches the axis and species 2 is excluded (a transcritical bifurcation)](./plots/lv-parameter-plane.py)

### 22.4.3. Interpretation

The four outcomes have a clear biological reading if the conditions are written as comparisons of intra- and interspecific competition. In case 4, $\alpha_{21}/K_2 < 1/K_1$ and $\alpha_{12}/K_1 < 1/K_2$: the effect of each species on the other is weaker than its effect on itself. Each species limits its own growth before it can depress its competitor to extinction, and both persist. In case 1, species 1 inhibits species 2 more than species 2 inhibits itself ($\alpha_{21}/K_2 > 1/K_1$) while species 2 inhibits species 1 less than species 1 inhibits itself: species 1 is the strong interspecific competitor and wins wherever the two start. In case 3 both species inhibit the other more than themselves. This happens when each species attacks, poisons or eats the other more than its own kind, as in Park's flour beetles (Example 22.1.2): whichever species is initially more abundant inflicts more damage than it receives and drives the other out. The rule "the species that inhibits more strongly, relative to its self-limitation, wins" is the essence of the competitive exclusion principle in the language of the model:

- *stable coexistence requires that intraspecific competition be stronger than interspecific competition for both species.*

Three consequences are worth stating.

1. *Coexistence requires $\alpha_{12}\alpha_{21} < 1$, but this is not sufficient.* Case 4 requires $a < 1$ and $b < 1$, hence $ab = \alpha_{12}\alpha_{21} < 1$; the converse fails (case 1 can have $ab < 1$). The carrying capacities must also be balanced: $\alpha_{21} < K_2/K_1 < 1/\alpha_{12}$. The more similar the species ($\alpha_{12}, \alpha_{21}$ close to 1), the narrower the range of $K_2/K_1$ that allows coexistence. This is the starting point of the theory of limiting similarity ([7.19.23](/7.19.23)).
2. *Coexistence is mutual invasibility.* Species 2 can invade species 1 if and only if $b < 1$, and vice versa; stable coexistence (case 4) is the case in which each species can increase when rare in the presence of the other at its carrying capacity. This invasion criterion generalizes far beyond the Lotka–Volterra model and is the foundation of modern coexistence theory ([7.19.23](/7.19.23)).
3. *Priority effects.* In case 3 the outcome depends on history: whichever species arrives first or is initially more abundant wins. With demographic stochasticity ([7.19.15](/7.19.15)) the deterministic threshold becomes a probability (Figure 3B), which is exactly the pattern of Park's beetles at intermediate climates. Changing climate moves the parameters across the boundaries of Figure 2A, from "*T. castaneum* always wins" through "either may win" to "*T. confusum* always wins".

The model also predicts how competitors share the environment at equilibrium. In case 4 the total density $N_1^* + N_2^*$ exceeds the larger of $K_1$, $K_2$ when the coefficients are small (Figure 2B): species that compete weakly with each other use the environment more fully together than either does alone, the population counterpart of a relative yield total above 1.

![Time courses of competition and the effect of chance. A: densities against time (r1 = 1, r2 = 0.8, K1 = K2 = 100, both species starting at 5) for stable coexistence (α12 = 0.5, α21 = 0.6; solid lines) and for exclusion of species 2 (α12 = 0.6, α21 = 1.4; dashed lines); the losing species first increases while both are rare and is then driven out as species 1 approaches K1. B: the bistable case (α12 = 1.5, α21 = 1.3) as a stochastic birth–death process with K1 = K2 = 60 individuals, 60 individuals initially, 400 runs per point. The deterministic model has a sharp threshold at the stable manifold of the saddle (dashed step, about 62 % species 1); with demographic noise the probability that species 1 wins rises gradually with its initial share](./plots/lv-bistability.py)

**Example 22.4.1** For $K_1 = 200$, $K_2 = 150$, $\alpha_{12} = 0.6$ and $\alpha_{21} = 0.8$: $K_1/\alpha_{12} = 333 > K_2 = 150$, so species 1 can invade, and $K_2/\alpha_{21} = 187.5 < K_1 = 200$, so species 2 cannot. Species 1 excludes species 2 (case 1, $a = 0.45$, $b = 1.07$). If the environment changes so that $K_1$ falls to 150, then $K_2/\alpha_{21} = 187.5 > 150$ and both species can invade: they coexist at $N_1^* = (150 - 0.6 \cdot 150)/(1 - 0.48) = 115.4$ and $N_2^* = (150 - 0.8 \cdot 150)/0.52 = 57.7$. A reduction of the carrying capacity of the superior competitor allows the inferior one to persist.

:::

### 22.4.4. A Lyapunov Function

The convergence in case 4 can also be proved without Poincaré–Bendixson, by a Lyapunov function that generalizes to many species.

**Proposition 22.4.1 (Lyapunov Function for Two Competitors)** If $a < 1$ and $b < 1$, the function

$$
V(x, y) = \left(x - x^* - x^*\ln\frac{x}{x^*}\right) + \frac{a}{\rho b}\left(y - y^* - y^*\ln\frac{y}{y^*}\right)
$$
is a strict **Lyapunov function** ([2.4.11](/2.4.11)) for (22.2) on the open positive quadrant: $V \ge 0$ with equality only at $E^*$, $V \to \infty$ at the axes and at infinity, and $\dot V < 0$ except at $E^*$. Hence $E^*$ attracts every positive solution.

**Proof** Each bracket is nonnegative and vanishes only at the equilibrium value, because $u - 1 - \ln u \ge 0$ with equality only at $u = 1$. Write $u = x - x^*$, $v = y - y^*$ and $c = a/(\rho b)$. Using $1 - x - ay = -(u + av)$ and $1 - y - bx = -(v + bu)$,

$$
\dot V = \frac{x - x^*}{x}\,\dot x + c\,\frac{y - y^*}{y}\,\dot y = -u(u + av) - c\rho v(v + bu) = -\left(u^2 + 2auv + \frac{a}{b}v^2\right).
$$

The quadratic form is positive definite if and only if $a/b > a^2$, that is $ab < 1$, which holds in case 4. $\square$

The choice of the weight $c$ makes the cross terms symmetric; the same idea, applied to $n$ species, gives the theorem of Section 22.5.2.

## 22.5. Competition among Many Species

### 22.5.1. The n-Species Model and the Community Matrix

For $n$ competing species the model is

$$
\frac{\mathrm{d}N_i}{\mathrm{d}t} = \frac{r_iN_i}{K_i}\left(K_i - \sum_{j=1}^n \alpha_{ij}N_j\right),\qquad \alpha_{ii} = 1,\quad i = 1, \dots, n,
\tag{22.4}
$$
with the *competition matrix* $A = (\alpha_{ij})$. An interior equilibrium $\boldsymbol{N}^*$, if it exists, solves the linear system $A\boldsymbol{N}^* = \boldsymbol{K}$; it is *feasible* if all its components are positive. The Jacobian matrix at a feasible equilibrium,

$$
C_{ij} = \frac{\partial \dot N_i}{\partial N_j}\bigg|_{\boldsymbol{N}^*} = -\frac{r_iN_i^*}{K_i}\,\alpha_{ij},
\qquad C = -DA,\quad D = \operatorname{diag}\!\left(\frac{r_iN_i^*}{K_i}\right),
$$
is called the *community matrix* (Levins 1968; May 1973): its entries are the effects of a small change in the density of species $j$ on the growth of species $i$ near equilibrium, and the equilibrium is locally stable if all its **eigenvalues** ([2.1.6](/2.1.6)) have negative real parts. The community matrix returns in the theory of food webs, where May's random-matrix argument relates its size and connectance to stability ([7.19.38](/7.19.38)).

Two new phenomena appear with three or more species. First, a species may be excluded although each pairwise interaction would allow coexistence (*diffuse competition*), because the sum of many weak effects exceeds its self-limitation. Second, competition can be non-transitive. If species 1 outcompetes 2, 2 outcompetes 3, and 3 outcompetes 1, as in a game of rock–paper–scissors, no species can win. May and Leonard (1975) showed that for

$$
A = \begin{bmatrix} 1 & \alpha & \beta \\ \beta & 1 & \alpha \\ \alpha & \beta & 1 \end{bmatrix},\qquad 0 < \alpha < 1 < \beta,
$$
the interior equilibrium is unstable if $\alpha + \beta > 2$, and trajectories approach a *heteroclinic cycle* connecting the three single-species equilibria: each species in turn rises to near its carrying capacity while the others become very rare, and the periods of dominance grow longer and longer (Figure 4B). Real populations, which are discrete, would lose a species during one of the long periods of rarity. Non-transitive competition is known in sessile marine invertebrates competing for space on coral reefs (Jackson and Buss 1975), in three strains of *Escherichia coli* that produce, resist or are sensitive to the toxin colicin, which coexist when interactions are local (Kerr et al. 2002), and in the mating strategies of side-blotched lizards ([7.18.28](/7.18.28)).

### 22.5.2. A Global Stability Theorem

**Theorem 22.5.1 (Goh's Theorem)** Suppose that (22.4) has a feasible equilibrium $\boldsymbol{N}^*$ and that there is a positive diagonal matrix $W$ such that $WA + A^{\mathsf T}W$ is positive definite. Then $\boldsymbol{N}^*$ is globally stable: every solution with all $N_i(0) > 0$ converges to it.

**Proof** Let $w_i > 0$ be the diagonal entries of $W$ and

$$
V(\boldsymbol{N}) = \sum_{i=1}^n \frac{w_iK_i}{r_i}\left(N_i - N_i^* - N_i^*\ln\frac{N_i}{N_i^*}\right).
$$
As in Proposition 22.4.1, $V \ge 0$ with equality only at $\boldsymbol{N}^*$, and $V \to \infty$ at the boundary of the positive orthant and at infinity. With $\boldsymbol{u} = \boldsymbol{N} - \boldsymbol{N}^*$ and $K_i - \sum_j \alpha_{ij}N_j = -\sum_j \alpha_{ij}u_j$,

$$
\dot V = \sum_i \frac{w_iK_i}{r_i}\,\frac{u_i}{N_i}\,\dot N_i = -\sum_{i,j} w_iu_i\alpha_{ij}u_j = -\tfrac12\,\boldsymbol{u}^{\mathsf T}(WA + A^{\mathsf T}W)\boldsymbol{u} < 0
$$
for $\boldsymbol{u} \ne \boldsymbol{0}$. By Lyapunov's theorem ([2.4.11](/2.4.11)) $\boldsymbol{N}^*$ attracts every positive solution. $\square$

For two species, $W = \operatorname{diag}(1, a/b)$ in scaled units gives Proposition 22.4.1. The most important special case is a symmetric, **positive definite matrix** $A$, for which $W = I$ works. Symmetric competition matrices arise when competition is purely exploitative and the competition coefficients are derived from overlapping resource use ([7.19.23](/7.19.23)): then any feasible equilibrium is globally stable, and the question of coexistence reduces to the question of feasibility. Figure 4A shows six species with Gaussian resource-utilization curves, whose competition matrix is positive definite: with peaks two standard deviations apart the equilibrium is feasible and all six coexist, but with the same carrying capacities and peaks 1.2 standard deviations apart the equilibrium is not feasible and two species are excluded. How similar species can be and still coexist is the problem of limiting similarity, taken up in [7.19.23](/7.19.23).

The number of coexisting species is also limited by the number of limiting factors. If the per capita growth rates depend on the densities only through $m$ quantities (resources, predators), at most $m$ species can coexist at a stable equilibrium; this extension of the exclusion principle (Levin 1970; Armstrong and McGehee 1980) is derived for consumer–resource models in [7.19.23](/7.19.23), together with the ways in which non-equilibrium dynamics escape it.

![Lotka–Volterra competition among more than two species. A: six species with Gaussian resource-utilization curves of equal width w whose peaks are d = 2w apart, so that αij = exp(−(i − j)²d²/4w²), with carrying capacities 100, 90, 110, 95, 105 and 100 and r = 1: the competition matrix is symmetric and positive definite and the feasible equilibrium is globally stable, so all six species converge to it from unequal starts. B: three species with non-transitive competition (α = 0.8, β = 1.3, May and Leonard 1975), on a logarithmic scale: the interior equilibrium is unstable, each species in turn dominates and almost disappears, and the periods of dominance lengthen without limit](./plots/lv-n-species.py)

## 22.6. Lessons and Limitations

The Lotka–Volterra model makes the competitive exclusion principle precise: two species can coexist stably only if each limits itself more than it limits the other. It yields the full range of qualitative outcomes found in experiments, predictable exclusion, exclusion that depends on initial densities, and stable coexistence, and it ties them to biologically meaningful circumstances. But it is a phenomenological model, and its parameters are not easily measured or interpreted.

- *What the coefficients mean.* The model contains no resources and no niches. The competition coefficients summarize the net per capita effects of one species on another near the observed densities, whatever their mechanism; they may reflect niche differences, but they need not. Deriving them from resource dynamics ([7.19.23](/7.19.23)) shows that they are constant only under restrictive assumptions.
- *Estimation.* Competition coefficients have been estimated from the equilibrium densities of species grown alone and together (solving the isocline equations), from response-surface experiments and from time series. Equilibrium-based estimates are unreliable, because a single equilibrium point cannot determine two coefficients without assuming the carrying capacities are the same in mixture, and the values depend on which densities are used. Coefficients estimated in one environment rarely predict the outcome in another (Park's beetles).
- *Linearity.* In *Drosophila* cultures the isoclines are curved: per capita growth rates decline non-linearly with density (Ayala, Gilpin and Ehrenfeld 1973), as in the θ-logistic model of [7.19.10](/7.19.10). With curved isoclines two species can intersect more than once, giving multiple coexistence equilibria, and coexistence can occur in parameter regions where the linear model predicts exclusion.
- *Missing biology.* The model ignores age and size structure (competition is often among juveniles, or asymmetric in favor of larger individuals), time lags, spatial structure, temporal fluctuations and other species. Each can change the outcome: spatial heterogeneity, aggregation and colonization–competition trade-offs allow coexistence of species that would exclude each other in a uniform environment ([7.19.16](/7.19.16), [7.19.23](/7.19.23), [7.19.30](/7.19.30)), and fluctuations can create coexistence through the storage effect ([7.19.23](/7.19.23)).

Within these limits the model remains the reference point of the theory: other models of competition are judged by whether they reduce to it near equilibrium, and the invasion criterion that it suggests carries over to models of any complexity.

## Summary

- Interactions between species are classified by their signs (Section 22.1.1). **Interspecific competition** (Definition 22.1.1) reduces the performance of at least one species through exploitation of a shared resource or through interference (including allelopathy); **apparent competition** through a shared predator has the same signs. Competition is often asymmetric; its ecological effects can be tested by experiment, its evolutionary effects only indirectly.
- Gause's ciliates, Park's flour beetles, charr along a temperature gradient, cheatgrass, warblers, Galápagos finches and Poyang Lake geese (Examples 22.1.1–22.1.6) show exclusion, coexistence with niche differences and outcomes that depend on conditions. Substitutive, additive and response-surface designs measure competition between plants (Section 22.2).
- The Lotka–Volterra model (Definition 22.3.2, Eq. (22.1)) replaces $N_i$ in the logistic term by $N_i + \alpha_{ij}N_j$; the **competition coefficient** (Definition 22.3.1) measures interspecific relative to intraspecific inhibition. In scaled form (22.2) the outcome depends only on $a = \alpha_{12}K_2/K_1$ and $b = \alpha_{21}K_1/K_2$.
- The **zero net growth isoclines** (Definition 22.3.3) are straight lines; their four arrangements give four outcomes (Theorem 22.4.3): species 1 wins ($a < 1 < b$), species 2 wins ($b < 1 < a$), bistability with a saddle and a separatrix ($a, b > 1$), stable coexistence ($a, b < 1$).

  | Equilibrium | Eigenvalues | Stable when |
  |---|---|---|
  | $(0, 0)$ | $1$, $\rho$ | never |
  | $(1, 0)$ | $-1$, $\rho(1 - b)$ | $b > 1$ |
  | $(0, 1)$ | $-\rho$, $1 - a$ | $a > 1$ |
  | $E^*$, Eq. (22.3) | $\operatorname{tr} < 0$, $\det = \rho x^*y^*(1 - ab)$ | $a, b < 1$ (node) |

- There are no periodic orbits (Dulac criterion), and every trajectory converges to an equilibrium (Theorem 22.4.2); a Lyapunov function proves global stability of coexistence (Proposition 22.4.1). Coexistence requires intraspecific competition to exceed interspecific competition for both species, equivalently mutual invasibility; $\alpha_{12}\alpha_{21} < 1$ is necessary but not sufficient.
- With $n$ species, the community matrix $C = -DA$ decides local stability; if $WA + A^{\mathsf T}W$ is positive definite for some positive diagonal $W$, a feasible equilibrium is globally stable (Theorem 22.5.1). Non-transitive competition produces heteroclinic cycles (May–Leonard).
- The model is phenomenological: its coefficients are hard to estimate and lack mechanism, its isoclines may be curved, and it ignores structure, space and fluctuations (Section 22.6).

## Questions

1. Two species have $K_1 = 500$, $K_2 = 400$, $\alpha_{12} = 0.5$ and $\alpha_{21} = 1.5$. Which species wins? How large would $K_2$ have to be for the outcome to change, and to what?

   **Answer** $K_1/\alpha_{12} = 1000 > K_2 = 400$, so species 1 can invade species 2 ($a = 0.4 < 1$). $K_2/\alpha_{21} = 267 < K_1 = 500$, so species 2 cannot invade species 1 ($b = 1.875 > 1$). Species 1 excludes species 2. The outcome changes when $b$ falls below 1, that is when $K_2 > \alpha_{21}K_1 = 750$; as long as $K_2 < K_1/\alpha_{12} = 1000$ the two species then coexist. For $K_2 > 1000$, species 2 excludes species 1.

2. Show that in the scaled model (22.2) the eigenvalue $\rho(1 - b)$ at $(1, 0)$ equals the per capita growth rate of a rare population of species 2 in a population of species 1 at carrying capacity, and explain why this makes the stability of single-species equilibria a statement about invasion.

   **Answer** The per capita growth rate of species 2 is $\dot y/y = \rho(1 - y - bx)$. With $x = 1$ and $y \to 0$ it tends to $\rho(1 - b)$, which is the second eigenvalue at $E_1$ (the eigenvector of the first eigenvalue, $-1$, lies along the $x$ axis, where species 1 simply returns to its carrying capacity). A perturbation that adds a few individuals of species 2 grows if and only if this rate is positive; so $E_1$ is unstable exactly when species 2 can invade. Stable coexistence (both single-species equilibria unstable and no bistability) is therefore mutual invasibility.

3. For $a = b = 1$ the isoclines of (22.2) coincide. Describe the dynamics. What biological situation does this represent, and why is it structurally unstable?

   **Answer** The isoclines are the same line $x + y = 1$, and every point on it is an equilibrium. Off the line both species increase (below) or decrease (above) at rates proportional to the distance from it, so trajectories move to the line and stop; the point reached depends on the initial densities and on $\rho$, and a perturbation along the line is not corrected (neutral stability). This is the case of ecologically identical species, each individual inhibiting both species equally (and $K_1 = K_2$ in suitable units). Any small difference in the parameters makes $a \ne 1$ or $b \ne 1$ and produces exclusion or coexistence; in a stochastic model the species drift until one is lost, the ecological analogue of neutral genetic drift (the neutral theory of [7.19.37](/7.19.37)).

4. Prove that if $\alpha_{12}\alpha_{21} > 1$ the two species cannot coexist stably, whatever their carrying capacities.

   **Answer** If $E^*$ exists in the open quadrant, $1 - ab = 1 - \alpha_{12}\alpha_{21} < 0$, so $\det J^* = \rho x^*y^*(1 - ab) < 0$ and $E^*$ is a saddle. Otherwise there is no interior equilibrium at all. By Theorem 22.4.2, positive solutions converge to an equilibrium, which can then only be $(1, 0)$ or $(0, 1)$ (or, exceptionally, the saddle along its stable manifold). Either way one species is excluded.

5. In a replacement-series experiment, the relative yield total of two grasses is 1.0 at all proportions. In another pair it is 1.3. What do these results suggest about the competition coefficients, and why would a single total density be insufficient to predict the long-term outcome?

   **Answer** An RYT of 1 means that each species can only replace the other: yield is shared, as when the species use the same resources in the same way ($\alpha_{12} \approx \alpha_{21} \approx 1$ in suitable units). An RYT above 1 means that the species exploit resources partly differently, so that interspecific competition is weaker than intraspecific competition ($\alpha_{ij} < 1$), which favors coexistence. However, one total density tells us nothing about how yields change as total density changes over generations, and it confounds the two coefficients; predicting the outcome requires the response of each species to both densities (a response surface) or a multi-generation experiment.

6. (Open question) The Lotka–Volterra model assumes that the per capita effect of species $j$ on species $i$ is constant. Suggest two biological mechanisms that would make $\alpha_{ij}$ depend on the densities, and describe how the isoclines would change.

   **Answer** (1) Saturating resource use: when the resource is abundant, consumers are limited by handling time, and an additional competitor reduces the resource less than linearly, so the effect per competitor declines at low density of the focal species or at high resource supply; isoclines become curved (concave or convex) and can intersect twice, producing two interior equilibria (one stable, one saddle) or coexistence outside the linear prediction. (2) Interference that increases with encounter rate: aggression or intraguild predation may grow faster than linearly with density, steepening the isoclines at high density and favoring bistability. Other mechanisms include habitat partitioning at high density (refuges for the weaker competitor), which bends its isocline outward and allows coexistence, and size structure, where the effect depends on the size distribution, which itself changes with density.
