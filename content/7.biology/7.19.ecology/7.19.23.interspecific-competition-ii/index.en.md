---
title: "Interspecific Competition II: Niches, Resources and Coexistence"
description: "The niche of Grinnell, Elton and Hutchinson; fundamental and realized niches (Connell's barnacles), spatial and temporal niche partitioning; resource utilization curves, niche overlap and limiting similarity derived from Gaussian overlap; the competitive exclusion principle and character displacement; consumer–resource models: MacArthur's derivation of Lotka–Volterra competition, the chemostat and the R* rule, Tilman's two-resource theory with zero net growth isoclines, supply points and consumption vectors; the paradox of the plankton; modern coexistence theory: invasion growth rates, stabilizing and equalizing mechanisms, relative nonlinearity and the storage effect; priority effects, heterogeneity and pre-emption."
---

The Lotka–Volterra model of [7.19.22](/7.19.22) shows that competitors coexist when each limits itself more than it limits the other, but it says nothing about why that should be so. Its competition coefficients are black boxes. This chapter opens them. Ecologists have answered the question "how do competitors coexist?" in three increasingly mechanistic ways: by describing the niches of species and how much they overlap (Sections 23.1–23.3), by modeling the resources for which species compete (Section 23.4), and by asking, in modern coexistence theory, what makes each species able to increase when rare (Section 23.5). Section 23.6 considers coexistence that depends on history, space and disturbance rather than on niche differences. The evolutionary consequences of competition (character displacement) are treated in [7.10.17](/7.10.17) and recalled in Section 23.3; competition as a force structuring whole communities, and the null models used to detect it, in [7.19.33](/7.19.33); neutral coexistence of equivalent species in [7.19.37](/7.19.37).

## 23.1. The Niche

### 23.1.1. Three Concepts

The word niche has been used in three related senses. Grinnell (1917), studying the California thrasher, used it for the habitat and conditions in which a species lives: its "address", determined by its requirements and tolerances. Elton (1927) used it for the role of a species in its community, above all its place in the food web, "what it is doing and not merely what it looks like": its "profession". Hutchinson (1957) combined and formalized the two. Each condition that affects an organism (temperature, humidity, pH) and each resource that it uses (food size, nest sites) can be treated as an axis, and along each axis there is a range within which the species can persist. Considering $n$ such axes together defines a region of the $n$-dimensional space of environmental variables, the *n-dimensional hypervolume*, inside which the population can grow. This is the **ecological niche** of a species as defined in [7.10.15](/7.10.15): the set of conditions under which it can persist and the resources it uses. With two conditions, temperature and humidity, the niche is an area; with a third axis it is a volume; with more axes it can no longer be drawn but can still be analyzed.

The niche is a property of a species, not a place: a habitat contains niches only in the sense that it provides the conditions and resources that some species require. Niche width describes the extent of the region along the axes: specialists have narrow niches and generalists broad ones ([7.10.15](/7.10.15)).

### 23.1.2. Fundamental and Realized Niches

Hutchinson distinguished the niche that a species could occupy from the one it does occupy.

**Definition 23.1.1 (Fundamental and Realized Niche)** The **fundamental niche** of a species is the set of conditions and resources under which it can maintain a population in the absence of other species that might be harmful to it, above all competitors and predators. Its **realized niche** is the part of the fundamental niche in which it maintains a population in the presence of specified other species.

Competitors and predators shrink the realized niche within the fundamental niche; mutualists can extend it, as mycorrhizal fungi extend the range of soils in which orchids and many trees can grow ([7.19.29](/7.19.29)). Begon describes the same distinction in the Tilman diagrams of Section 23.4: the zero net growth isocline of a species bounds its fundamental niche in resource space, and competition decides which part of it is realized.

**Example 23.1.1 (Connell's Barnacles)** On rocky shores in Scotland, adults of the barnacle *Chthamalus stellatus* occupy a band high in the intertidal zone, and *Semibalanus balanoides* (then *Balanus balanoides*) a broad band below it, although *Chthamalus* larvae settle in both zones. Connell (1961) removed *Semibalanus* from rocks in the lower zone: *Chthamalus* then survived there well. Where *Semibalanus* was present, it smothered, undercut or crushed the *Chthamalus*, especially in the first months after settlement. *Semibalanus*, on the other hand, was confined below by desiccation in the upper zone, where it died even when *Chthamalus* was absent. The fundamental niche of *Chthamalus* thus extends over both zones, but its realized niche is the upper zone, set by interference competition; the realized niche of *Semibalanus* coincides with its fundamental niche, set by physical conditions. This pattern, in which the upper limit of a species on a gradient of stress is set by physical factors and the lower limit by biological interactions, recurs on shores, in mountains and along salinity gradients.

**Example 23.1.2 (Two Bedstraws)** Tansley (1917) grew the bedstraws *Galium saxatile*, which grows on acid peaty soils, and *G. sylvestre* (= *G. pumilum*), which grows on calcareous soils, on both soil types. Alone, each established and grew on either soil. Together, *G. saxatile* overgrew *G. sylvestre* on acid soil and *G. sylvestre* overgrew *G. saxatile* on calcareous soil. Each species' realized niche is the soil on which it is competitively superior, a much smaller region than its fundamental niche.

:::

### 23.1.3. Partitioning Space and Time

Coexisting species with similar requirements often divide the environment along one or more axes.

- *Space.* MacArthur (1958) found that five species of warblers (*Setophaga*) breeding in the spruce forests of Maine, all insectivores of similar size, fed in different parts of the same trees: the Cape May warbler at the top and outer tips, the Blackburnian and black-throated green warblers in the upper and middle crown, the bay-breasted warbler in the dense middle interior, and the yellow-rumped (myrtle) warbler mainly low and on the ground, with further differences in foraging movements and nesting time. Four *Sylvia* warblers on Corsica and Sardinia separate by the height of the shrubs they use and by the plants on which they forage (Martin and Thibault 1996).
- *Time.* Diurnal raptors (Accipitriformes, Falconiformes) and nocturnal owls (Strigiformes) both hunt small rodents, but at different times of day; sympatric species of desert annuals germinate after rains of different seasons.
- *Resources.* Sympatric species may differ in the size or kind of food, as the large carnivores of the Tibetan Plateau do in part ([7.19.22](/7.19.22), Example 22.1.6).
- *Conditions.* Two species may use the same resources but differ in the conditions under which each is the better competitor, as the charr of Hokkaido do with temperature ([7.19.22](/7.19.22), Example 22.1.3).

Such differences are consistent with niche partitioning that permits coexistence, but they are not proof of it: they might have arisen for reasons unconnected with competition, and only experiments can show whether the species now compete (Section 23.3).

## 23.2. Resource Utilization, Niche Overlap and Limiting Similarity

### 23.2.1. Resource Utilization Curves

Along a single, continuous resource axis, such as the size of food items, the use of the resource by a species can be described by a *resource utilization curve* $u(x)$: the rate at which the species consumes items of size $x$. Such curves are often roughly bell-shaped, highest at a preferred size and tailing off on either side, and can be summarized by the position $\mu$ of the peak and the standard deviation $w$ (the niche width along this axis). For two species with peaks a distance $d$ apart, $d > w$ means little overlap and weak competition, $d < w$ much overlap and strong competition.

**Definition 23.2.1 (Niche Overlap)** The **niche overlap** of species $i$ with species $j$ is a measure of the extent to which they use the same resources. For utilization functions $u_i, u_j$ on a resource axis, MacArthur and Levins (1967) defined

$$
\alpha_{ij} = \frac{\int u_i(x)u_j(x)\,\mathrm{d}x}{\int u_i(x)^2\,\mathrm{d}x},
\tag{23.1}
$$
the probability that an item consumed by species $j$ would also have been consumed by species $i$, relative to the probability that it would have been consumed by another member of species $i$. For discrete resource categories with proportions $p_k$, $q_k$ in the two diets, Pianka's symmetric index $O = \sum_k p_kq_k \big/ \sqrt{\sum_k p_k^2 \sum_k q_k^2}$ is widely used.

MacArthur and Levins interpreted (23.1) as the Lotka–Volterra competition coefficient: if competition is purely exploitative and each item consumed by $j$ is denied to $i$, the inhibition of $i$ by one individual of $j$ relative to one individual of $i$ is the ratio of overlaps. Section 23.4.1 derives this from resource dynamics.

**Proposition 23.2.1 (Overlap of Gaussian Utilization Curves)** If $u_i(x) = \exp\!\big(-(x - \mu_i)^2/2w^2\big)$ and $u_j$ is the same curve centered at $\mu_j$, with $d = \lvert\mu_i - \mu_j\rvert$, then

$$
\alpha_{ij} = \alpha_{ji} = \exp\!\left(-\frac{d^2}{4w^2}\right).
$$

**Proof** Let $m = (\mu_i + \mu_j)/2$. Completing the square, $(x - \mu_i)^2 + (x - \mu_j)^2 = 2(x - m)^2 + d^2/2$. Hence

$$
\int u_iu_j\,\mathrm{d}x = \mathrm{e}^{-d^2/4w^2}\int \mathrm{e}^{-(x - m)^2/w^2}\,\mathrm{d}x = \sqrt{\pi}\,w\,\mathrm{e}^{-d^2/4w^2},
$$
and $\int u_i^2\,\mathrm{d}x = \sqrt{\pi}\,w$ is the case $d = 0$. $\square$

The competition coefficient is close to 1 for $d/w \ll 1$, equal to $\mathrm{e}^{-1/4} = 0.78$ at $d = w$ and $\mathrm{e}^{-1} = 0.37$ at $d = 2w$ (Figure 1B).

### 23.2.2. Limiting Similarity

Since the Lotka–Volterra model allows coexistence whenever $\alpha_{12}$ and $\alpha_{21}$ are less than 1 and the carrying capacities are suitably balanced, any niche difference at all would seem to permit coexistence. The question "must competitors differ in order to coexist?" is therefore badly put. The better question is: *how much* must they differ?

**Definition 23.2.2 (Limiting Similarity)** The **limiting similarity** of competing species is the minimum difference in their resource use (for example the separation $d/w$ of their utilization curves) compatible with their stable coexistence in a given model and environment.

MacArthur and Levins (1967) and May and MacArthur (1972) considered three species on a resource axis with Gaussian utilization curves of equal width, peaks $d$ apart, and asked when a middle species (carrying capacity $K_2$) can persist between two outer species (carrying capacities $K_1 = K_3$).

**Proposition 23.2.2 (Three Species on a Resource Axis)** With $\alpha = \mathrm{e}^{-d^2/4w^2}$ between adjacent species and $\alpha^4$ between the outer two, the Lotka–Volterra model has an equilibrium with all three species present if and only if

$$
\frac{2\alpha}{1 + \alpha^4} < \frac{K_2}{K_1} < \frac{1}{\alpha},
\tag{23.2}
$$
and this equilibrium is then globally stable.

**Proof** The outer species are $2d$ apart, so their coefficient is $\mathrm{e}^{-4d^2/4w^2} = \alpha^4$. By symmetry the equilibrium has $N_1 = N_3$, and $A\boldsymbol{N} = \boldsymbol{K}$ reduces to

$$
(1 + \alpha^4)N_1 + \alpha N_2 = K_1,\qquad 2\alpha N_1 + N_2 = K_2.
$$
Substituting $N_2 = K_2 - 2\alpha N_1$ into the first equation gives $N_1(1 + \alpha^4 - 2\alpha^2) = K_1 - \alpha K_2$, that is

$$
N_1 = \frac{K_1 - \alpha K_2}{(1 - \alpha^2)^2},\qquad N_2 = K_2 - \frac{2\alpha(K_1 - \alpha K_2)}{(1 - \alpha^2)^2}.
$$
$N_1 > 0$ if and only if $K_2/K_1 < 1/\alpha$. $N_2 > 0$ if and only if $K_2\big[(1 - \alpha^2)^2 + 2\alpha^2\big] > 2\alpha K_1$, and $(1 - \alpha^2)^2 + 2\alpha^2 = 1 + \alpha^4$. The competition matrix $A_{ij} = \exp\!\big(-(\mu_i - \mu_j)^2/4w^2\big)$ is the Gram matrix of the functions $u_i$ in $L^2$ (up to a constant factor), hence symmetric positive definite for distinct peaks, and a feasible equilibrium is globally stable by Goh's theorem ([7.19.22](/7.19.22), Theorem 22.5.1). $\square$

Figure 1C shows the range (23.2). For $d/w = 2$ the middle species persists for $0.72 < K_2/K_1 < 2.72$; for $d/w = 1$ only for $1.14 < K_2/K_1 < 1.28$; for $d/w = 0.5$ for $1.056 < K_2/K_1 < 1.065$. Coexistence remains possible however similar the species are, but the environment must suit them more and more exactly equally. May and MacArthur argued that in a fluctuating environment, where the carrying capacities vary, this fine balance cannot be maintained, and coexistence requires roughly $d/w \gtrsim 1$.

The result has been influential but is not general. Abrams (1975, 1983) showed that with other shapes of utilization curves, several resource dimensions, or resources with their own dynamics, the limit to similarity changes, often to much smaller values, and that there is no universal value of $d/w$. What survives is the qualitative lesson: the more similar the competitors, the narrower the conditions for coexistence. Coexistence depends jointly on how much the niches overlap and how similar the competitors are in overall competitive ability, a distinction made precise in Section 23.5. Carmel et al. (2017) showed in a consumer–resource model that the *rate* of competitive exclusion is greatest when overlap is high and abilities differ, and falls to zero both when overlap is zero and when the species are competitively equivalent: complete overlap with equal abilities gives the neutral case ([7.19.37](/7.19.37)).

![Resource utilization curves, overlap and limiting similarity. A: Gaussian utilization curves of three species along a resource axis, with peaks d = 0.8w apart (upper: much overlap) and d = 2w apart (lower: little overlap). B: the competition coefficient between adjacent species, α = exp(−d²/4w²) (Proposition 23.2.1), and between the outer species, α⁴. C: the range of the ratio K2/K1 of carrying capacities for which a middle species coexists with two outer ones (shaded, Eq. (23.2), logarithmic scale): it narrows sharply as d/w falls below about 1](./plots/resource-utilization-overlap.py)

## 23.3. Competitive Exclusion and Its Evolutionary Consequences

### 23.3.1. The Competitive Exclusion Principle

The **competitive exclusion principle** ([7.10.17](/7.10.17)), also called Gause's principle after the experiments of [7.19.22](/7.19.22) (Example 22.1.1), states that species that are too similar in their use of limiting resources cannot coexist indefinitely in a stable environment: complete competitors cannot coexist (Hardin 1960). Begon and Townsend state it in two parts. If two competing species coexist in a stable environment, they do so as a result of niche differentiation. If there is no such differentiation, or the habitat precludes it, one species will exclude the other. Extended to many species, $n$ competing species require at least $n$ distinct limiting factors (Section 23.4.2).

The principle is logically compelling but hard to test in nature. If two species coexist, a niche difference can almost always be found; if one is absent, its absence may have other causes. The principle is therefore best treated not as an empirical law but as a framework that directs attention to the differences that allow coexistence, and to the circumstances (non-equilibrium dynamics, fluctuations, space) in which it does not apply (Sections 23.4.4–23.6).

The strongest field evidence comes from *competitive release*: the expansion of the realized niche when a competitor is absent, also called **ecological release** ([7.10.17](/7.10.17)). Ocelots (*Leopardus pardalis*, 8–18 kg) living with pumas and jaguars take mostly small prey; in two sites in Panama without jaguars, more than 60 % of their prey items weighed over 1 kg, whereas at sites with jaguars throughout Central and South America the proportion was never more than 50 % and often less than 10 % (Moreno et al. 2006). Removal experiments, such as Connell's (Example 23.1.1), are more decisive. Reviews of such experiments found evidence of competition in most of the species studied, more often in plants and sessile animals than in mobile ones, and more often among large than small herbivores (Connell 1983; Schoener 1983; Gurevitch et al. 1992).

### 23.3.2. Character Displacement and Related Processes

If competition reduces the fitness of the individuals that overlap most with another species, selection favors those that differ: competitors evolve apart. **Character displacement** ([7.10.17](/7.10.17)) is the resulting divergence of a trait in sympatry, where two species occur together, relative to allopatry, where each occurs alone.

- *Galápagos finches.* On islands where the small ground finch (*Geospiza fuliginosa*) and the medium ground finch (*G. fortis*) occur together, their beaks differ clearly in depth; on Daphne Major, without *G. fuliginosa*, *G. fortis* has a beak of intermediate size, and on Los Hermanos, without *G. fortis*, *G. fuliginosa* has a larger beak than in sympatry (Lack 1947). The process was observed directly on Daphne Major: the large ground finch (*G. magnirostris*) colonized the island in 1982, and during the drought of 2003–2005, when large seeds were exhausted by both species, *G. fortis* with large beaks died disproportionately and the mean beak size of *G. fortis* fell sharply in one generation (Grant and Grant 2006).
- *Mongooses.* Where the small Indian mongoose (*Urva auropunctata*, formerly *Herpestes javanicus*) lives with two larger congeners in western India, its canine teeth are smaller than in the east, where it occurs alone; on islands to which it was introduced without its competitors, its canines increased within 100–200 generations (Simberloff et al. 2000).
- *Sticklebacks.* Brook sticklebacks (*Culaea inconstans*) living with ninespine sticklebacks have shorter gill rakers and longer jaws than in lakes where they occur alone, and in enclosures with ninespine sticklebacks the sympatric form grew better than the allopatric one, as expected if the shift reduces competition (Gray and Robinson 2002).
- *Experimental evolution.* In unshaken culture vessels, the bacterium *Pseudomonas fluorescens* diversifies within days into three types that use the broth ("smooth"), the surface ("wrinkly spreader") and the bottom ("fuzzy spreader"), each able to invade the others when rare; in shaken vessels, where the spatial niches disappear, the diversity does not arise (Rainey and Travisano 1998).

Natural comparisons must be interpreted cautiously, because sympatric and allopatric populations differ in more than the presence of the competitor: the mud snails *Hydrobia ulvae* and *H. ventrosa* differ in size where they co-occur, but they co-occur in sheltered habitats where size differs for other reasons (Saloniemi 1993).

Displacement can involve signals as well as resources and can have further evolutionary consequences. In *cascade reinforcement*, selection against hybridization with a second species in sympatry changes mating signals or preferences in one population, which as a side effect becomes reproductively isolated from conspecific populations living without the second species. Females of the spadefoot toad *Spea multiplicata* living with *S. bombifrons* prefer males whose calls differ from those of *S. bombifrons*, and as a result they discriminate against males of their own species from allopatric populations (Pfennig and Ryan 2006); speciation in one pair of species can thus trigger divergence within one of them ([7.10.12](/7.10.12)). In *convergent character displacement* sympatric species become more similar: the songs of the Peruvian and yellow-breasted warbling antbirds (*Hypocnemis peruviana*, *H. subflava*), which defend territories against each other, are more alike in sympatry, which may facilitate mutual recognition and interspecific territoriality (Tobias and Seddon 2009).

## 23.4. Consumer–Resource Models

The Lotka–Volterra model describes the net effect of one competitor on another. Consumer–resource models describe its mechanism: competitors affect each other through the resources they consume, whose dynamics are modeled explicitly.

### 23.4.1. Lotka–Volterra Competition from Resource Dynamics

MacArthur (1970, 1972) showed that Lotka–Volterra competition is what a consumer–resource system looks like when the resources equilibrate quickly.

**Proposition 23.4.1 (MacArthur's Consumer–Resource Model)** Let $n$ consumers $N_i$ feed on $m$ biotic resources $R_k$, each growing logistically in the absence of consumers:

$$
\frac{\mathrm{d}N_i}{\mathrm{d}t} = N_i\Big(b_i\sum_k v_kc_{ik}R_k - \mu_i\Big),\qquad
\frac{\mathrm{d}R_k}{\mathrm{d}t} = R_k\Big(s_k\Big(1 - \frac{R_k}{L_k}\Big) - \sum_i c_{ik}N_i\Big),
$$
where $c_{ik}$ is the per capita consumption rate of resource $k$ by consumer $i$, $v_k$ the value (e.g. energy) of a unit of resource $k$, $b_i$ the conversion efficiency, $\mu_i$ the death rate, and $s_k$, $L_k$ the intrinsic rate of increase and carrying capacity of resource $k$. If the resources equilibrate fast relative to the consumers and stay positive, the consumers obey the Lotka–Volterra model

$$
\frac{\mathrm{d}N_i}{\mathrm{d}t} = N_i\Big(\gamma_i - \sum_j a_{ij}N_j\Big),\qquad
\gamma_i = b_i\sum_k v_kc_{ik}L_k - \mu_i,\qquad a_{ij} = b_i\sum_k \frac{v_kL_k}{s_k}c_{ik}c_{jk}.
$$

**Proof** Setting $\mathrm{d}R_k/\mathrm{d}t = 0$ with $R_k > 0$ gives the quasi-steady state $R_k = L_k\big(1 - \sum_i c_{ik}N_i/s_k\big)$. Substituting into the consumer equation,

$$
b_i\sum_k v_kc_{ik}R_k - \mu_i = b_i\sum_k v_kc_{ik}L_k - \mu_i - \sum_j\Big(b_i\sum_k \frac{v_kc_{ik}L_kc_{jk}}{s_k}\Big)N_j. \qquad\square
$$

The interaction matrix has the form $a_{ij} = b_iG_{ij}$ with $G = CVC^{\mathsf T}$, where $C = (c_{ik})$ and $V = \operatorname{diag}(v_kL_k/s_k)$. Three consequences follow.

1. *The competition coefficients have a mechanism.* $a_{ij}$ is proportional to the overlap $\sum_k c_{ik}c_{jk}(v_kL_k/s_k)$ of the consumption vectors of $i$ and $j$, weighted by the value and the slowness of renewal of each resource; the coefficient $\alpha_{ij} = a_{ij}/a_{ii} = G_{ij}/G_{ii}$ is the discrete version of the overlap (23.1).
2. *Global stability.* With $W = \operatorname{diag}(1/b_i)$, $WA = G$ is symmetric and positive semidefinite, and positive definite when the consumption vectors are linearly independent. By Goh's theorem ([7.19.22](/7.19.22), Theorem 22.5.1), any feasible equilibrium is globally stable. MacArthur also showed that the dynamics minimize a quadratic function measuring the unused resource production, a rare case in ecology of a model governed by an optimization principle.
3. *The limit to diversity.* If $n > m$ and the consumption vectors span at most $m$ dimensions, $G$ is singular; generically no feasible equilibrium with all $n$ species exists, and at most $m$ consumers coexist at equilibrium on $m$ resources.

The derivation also shows the limits of the Lotka–Volterra description: the coefficients are constant only if the resources respond linearly and quickly, and the consumers have linear (type I) functional responses ([7.19.25](/7.19.25)).

### 23.4.2. One Abiotic Resource: The Chemostat and the R* Rule

Tilman (1977, 1982) developed a mechanistic theory of competition for abiotic resources, such as the nutrients of phytoplankton and plants, whose supply is not produced by the resource itself but delivered from outside. The laboratory **chemostat** ([7.6.39](/7.6.39), [7.11.8](/7.11.8)) realizes it exactly: medium with resource concentration $S$ flows in at dilution rate $D$, and medium with organisms and unused resource flows out at the same rate. For $n$ species with Monod growth ([7.11.8](/7.11.8)) on one resource $R$,

$$
\frac{\mathrm{d}R}{\mathrm{d}t} = D(S - R) - \sum_{i=1}^n \frac{\mu_i(R)N_i}{Y_i},\qquad
\frac{\mathrm{d}N_i}{\mathrm{d}t} = N_i\big(\mu_i(R) - D\big),\qquad
\mu_i(R) = \frac{\mu_{\max,i}R}{k_i + R},
\tag{23.3}
$$
where $Y_i$ is the yield (individuals produced per unit resource). In natural systems $D$ is replaced by the loss rate $m_i$ (mortality, sinking, grazing), which may differ among species.

**Definition 23.4.1 (R\* and the R\* Rule)** The **break-even concentration** ([7.11.4](/7.11.4)) $R_i^*$ of species $i$ is the resource level at which its per capita growth balances its losses, $\mu_i(R_i^*) = D$; for Monod growth

$$
R_i^* = \frac{Dk_i}{\mu_{\max,i} - D}\qquad(\mu_{\max,i} > D).
$$
The **R\* rule** states that, when several species compete for a single limiting resource at equilibrium, the species with the lowest $R^*$ excludes all others.

**Theorem 23.4.1 (Competitive Exclusion in the Chemostat)** Suppose $R_1^* < R_2^* \le \dots \le R_n^*$ and $R_1^* < S$. Then every solution of (23.3) with $N_1(0) > 0$ converges to $R = R_1^*$, $N_1 = Y_1(S - R_1^*)$, $N_i = 0$ for $i \ge 2$.

**Proof** (sketch; Hsu, Hubbell and Waltman 1977) Let $\Sigma = R + \sum_i N_i/Y_i$ be the total amount of resource, free and bound in organisms. Adding the equations gives $\dot\Sigma = D(S - \Sigma)$, so $\Sigma(t) \to S$ exponentially. On the limiting set $\Sigma = S$, write $R = S - \sum_i N_i/Y_i$. For $i \ge 2$, $\mathrm{d}\ln N_i/\mathrm{d}t = \mu_i(R) - D$ is negative whenever $R < R_i^*$ and $\mathrm{d}\ln N_1/\mathrm{d}t$ positive whenever $R > R_1^*$; one shows that $R(t)$ cannot remain above $R_1^*$ (species 1 would grow without bound, contradicting $\Sigma \to S$) and eventually stays below $R_2^*$, after which all other species decline exponentially. The reduced system for $N_1$ alone has the globally stable equilibrium $R = R_1^*$. A Lyapunov function of the form $\int_{R_1^*}^R (\mu_1(s) - D)/\mu_1(s)\,\mathrm{d}s + \sum_i c_i(\dots)$ makes the argument rigorous for general monotone uptake functions (Armstrong and McGehee 1980; Wolkowicz and Lu 1992). $\square$

The species that wins is not necessarily the one that grows fastest when resources are plentiful (Figure 2). A low $R^*$ results from a high maximal growth rate, a low half-saturation constant (efficient uptake at low concentrations) and a low loss rate, and these traits trade off: a plant that invests in roots to take up nitrogen at low concentrations invests less in leaves and grows more slowly.

The rule has strong experimental support. Five freshwater phytoplankton species, each grown alone in chemostats, drew phosphate down to steady concentrations in the order *Synechocystis* (0.030 µmol L⁻¹) < *Chlorella* (0.059) < *Monoraphidium* (0.117) < *Selenastrum* (0.160) < *Monodus* (0.182); in every pairwise competition the species with the lower $R^*$ won (Passarge et al. 2006). In a review of competition experiments with bacteria, phytoplankton and zooplankton, the $R^*$ rule predicted the winner in nearly all cases (Wilson et al. 2007). Among five prairie grasses grown on nitrogen-poor soils at Cedar Creek, Minnesota, *Schizachyrium scoparium* and *Andropogon gerardi*, which drew soil nitrate and ammonium down to the lowest levels, displaced *Agrostis scabra* whatever the initial proportions; the better nitrogen competitors had higher root allocation, lower growth rates and lower reproductive allocation, and dominate late in old-field succession (Tilman and Wedin 1991), a trade-off taken up in [7.19.36](/7.19.36). An invading gecko (*Hemidactylus frenatus*) that depletes insects to lower levels than the native *Lepidodactylus lugubris* has replaced it in urban habitats across the Pacific (Petren and Case 1996).

![Competition for a single resource in a chemostat (simulated parameters). A: per capita growth rates of two species with Monod kinetics against the resource concentration; each species can persist only where its growth exceeds the dilution rate D (horizontal line), and its break-even concentration R* is where its curve crosses D (R*₁ = 0.67, R*₂ = 1.0). Species 2 grows faster at high concentrations. B: dynamics from equal small inocula with the resource at the supply concentration S = 10: species 2 increases first, but the resource is drawn down to R*₁ (dashed), at which species 2 cannot replace its losses and is washed out](./plots/chemostat-rstar.py)

### 23.4.3. Two Resources: Tilman's Graphical Theory

With two resources, $R_1$ and $R_2$, the state of the resources is a point in a plane, and the growth of a consumer depends on both. The **zero net growth isocline** ([7.19.22](/7.19.22), Definition 22.3.3) of a consumer is now the curve in the resource plane on which its per capita growth balances its losses ([7.19.6](/7.19.6)); the resource combinations outside it, in which the population can grow, are its fundamental niche along these two axes. For essential resources (Liebig's law, growth $\mu_i = \mu_{\max,i}\min_k R_k/(k_{ik} + R_k)$) the isocline is a right angle with its corner at $(R_{i1}^*, R_{i2}^*)$, the break-even concentrations for each resource alone; for substitutable resources it is a line or curve from one axis to the other.

The resource dynamics have two parts (Figure 3A).

- *Supply.* Without consumers the resources move toward the *supply point* $\boldsymbol{S} = (S_1, S_2)$ along the *supply vector* $D(\boldsymbol{S} - \boldsymbol{R})$, which points from the current state to $\boldsymbol{S}$.
- *Consumption.* Each consumer removes resources at a rate $\mu_i(\boldsymbol{R})N_i\boldsymbol{c}_i$, where the *consumption vector* $\boldsymbol{c}_i = (c_{i1}, c_{i2})$ gives the amounts of the two resources used per unit of growth; its direction is fixed by the species' stoichiometry ([7.19.6](/7.19.6)).

A single consumer equilibrates on its isocline (so that its population is constant) at the point where its consumption vector exactly opposes the supply vector (so that the resources are constant): the resources are drawn down from $\boldsymbol{S}$ along the direction $-\boldsymbol{c}_i$ until they reach the isocline. The equilibrium point is the two-resource analogue of $R^*$.

For two consumers A and B, superimposing the isoclines gives two cases. If the isocline of A lies entirely inside that of B (A has the lower $R^*$ for both resources), A excludes B wherever both can persist, as with one resource. If the isoclines cross, say A has the lower break-even concentration for resource 1 ($R_{A1}^* < R_{B1}^*$) and B for resource 2 ($R_{B2}^* < R_{A2}^*$), the crossing point $\boldsymbol{R}^{**} = (R_{B1}^*, R_{A2}^*)$ is a candidate coexistence equilibrium: there A is limited by resource 2 and B by resource 1.

**Theorem 23.4.2 (Coexistence on Two Essential Resources)** Suppose the isoclines of A and B cross at $\boldsymbol{R}^{**}$ as above. Then the two species can each invade the other's equilibrium, and therefore coexist, if and only if the supply point lies in the cone

$$
\boldsymbol{S} = \boldsymbol{R}^{**} + s\,\boldsymbol{c}_A + t\,\boldsymbol{c}_B,\qquad s, t > 0,
$$
and each species consumes relatively more of the resource that limits it at $\boldsymbol{R}^{**}$, that is

$$
\frac{c_{A2}}{c_{A1}} > \frac{c_{B2}}{c_{B1}}.
\tag{23.4}
$$
If the inequality (23.4) is reversed, supply points in the cone give bistability: neither species can invade the other, and the first to establish wins.

**Proof** Consider B alone. It draws the resources down from $\boldsymbol{S}$ along the straight line $\boldsymbol{S} - t\boldsymbol{c}_B$, $t \ge 0$, until it reaches its isocline. If $\boldsymbol{S}$ lies above the ray $\boldsymbol{R}^{**} + t\boldsymbol{c}_B$, this line is parallel to the ray and above it, so it meets the vertical arm $R_1 = R_{B1}^*$ of B's isocline at a point with $R_2 > R_{A2}^*$. There $R_1 = R_{B1}^* > R_{A1}^*$ and $R_2 > R_{A2}^*$: the resources lie outside A's isocline, so A, when rare, grows. If instead $\boldsymbol{S}$ lies below that ray, B's equilibrium lies on its vertical arm below $R_{A2}^*$ or on its horizontal arm, inside A's isocline, and A cannot invade. Symmetrically, A alone draws the resources down along $-\boldsymbol{c}_A$ and leaves them outside B's isocline (so that B can invade) if and only if $\boldsymbol{S}$ lies below (to the right of) the ray $\boldsymbol{R}^{**} + t\boldsymbol{c}_A$. Both invasions succeed if and only if $\boldsymbol{S}$ lies above the $\boldsymbol{c}_B$ ray and below the $\boldsymbol{c}_A$ ray. These two conditions define a nonempty region beyond $\boldsymbol{R}^{**}$, namely the cone $\boldsymbol{R}^{**} + s\boldsymbol{c}_A + t\boldsymbol{c}_B$, exactly when the $\boldsymbol{c}_A$ ray is steeper than the $\boldsymbol{c}_B$ ray, which is (23.4). If (23.4) is reversed, supply points in the cone lie below the $\boldsymbol{c}_B$ ray and above the $\boldsymbol{c}_A$ ray, and neither species can invade the other. Local stability of the four-dimensional coexistence equilibrium under (23.4) is shown by linearization (León and Tumpson 1975; Tilman 1980). $\square$

The condition has a biological reading that parallels the Lotka–Volterra condition: at the coexistence point each species is limited by a different resource and consumes more of the resource that limits it. It therefore limits itself more than it limits its competitor. The other regions of Figure 3B follow from the same reasoning: with supply points below both isoclines neither species persists (region 1); between the isoclines only one can (regions 2 and 6); and outside the cone the resource that is relatively scarce in the supply decides: where resource 1 is scarce (region 3) the better competitor for resource 1, A, wins; where resource 2 is scarce (region 5), B wins. The outcome of competition depends on the *ratio* of the supplied resources, the basis of Tilman's resource-ratio hypothesis of succession and of plant diversity along gradients ([7.19.36](/7.19.36)).

The theory has been confirmed in several systems. The diatoms *Asterionella formosa* and *Cyclotella meneghiniana* compete for phosphate and silicate; *Asterionella* has the lower $R^*$ for phosphate and *Cyclotella* for silicate. In cultures with low silicate supply *Cyclotella* won, with low phosphate supply *Asterionella* won, and at intermediate Si:P ratios they coexisted, as predicted (Tilman 1977). The rotifers *Brachionus rubens* and *B. calyciflorus* compete for two algae, *Monoraphidium minutum* (on which *B. rubens* grows better) and *Chlamydomonas sphaeroides* (on which *B. calyciflorus* does better); the algae are substitutable, so the isoclines are straight lines, which cross. The predicted outcomes at different supply ratios and two dilution rates were confirmed in 11 of 12 experiments (Rothhaupt 1988). In an 11-year experiment with prairie grasses competing for nitrogen and light, pairs in which one species had both the lower $N^*$ and the lower $L^*$ showed exclusion, and the two pairs with opposite rankings coexisted (Dybzinski and Tilman 2007). In three Yellowstone lakes the diversity of phytoplankton rose with the number of resources (N, P, Si, light) at limiting levels (Interlandi and Kilham 2001).

![Tilman's theory of competition for two essential resources (simulated parameters, Liebig growth). A: the zero net growth isocline (ZNGI) of a single consumer is a right angle; from the supply point S the resources are drawn down along the consumption vector to the equilibrium on the isocline (square). B: two consumers whose isoclines cross at (3, 3); dashed rays from the crossing along the consumption vectors bound the region where both can invade each other. Regions: 1, neither species persists; 2, only A; 3, A excludes B (resource 1 relatively scarce); 4, stable coexistence (each species consumes relatively more of the resource that limits it); 5, B excludes A; 6, only B. Thin lines: simulated resource trajectories from supply points in regions 2, 3, 4 and 5 (dots), ending at the squares (blue: only A survives; orange: only B; black: both). C: the two populations for the supply point (9, 7) in region 4 converge to coexistence](./plots/two-resource-zngi.py)

### 23.4.4. The Paradox of the Plankton

If $n$ species can coexist at equilibrium on at most $n$ limiting resources, how can dozens of phytoplankton species coexist in a small, well-mixed body of water that offers only a handful of limiting resources, nitrogen, phosphorus, silicon, iron, light and carbon? Hutchinson (1961) called this the *paradox of the plankton*. Its resolution illuminates the assumptions behind the exclusion principle, which requires (i) a constant environment, (ii) equilibrium, (iii) spatial homogeneity, and (iv) competition only for the counted resources. Each assumption can fail:

- *Fluctuating environment.* Seasons, mixing events and weather change the conditions faster than exclusion proceeds, so that the identity of the best competitor changes before any species is lost (Hutchinson's own explanation; Section 23.5.3).
- *Endogenous oscillations and chaos.* Even in a constant environment, competition for three or more essential resources can produce oscillations and chaos, in which many more species than resources persist: Huisman and Weissing (1999) found nine species coexisting on three resources in a standard model. Two consumers on one resource can coexist if one of them, with a saturating functional response, generates oscillations that leave the resource above the other's $R^*$ on average (Armstrong and McGehee 1980; Section 23.5.2).
- *Heterogeneity, predators and pathogens.* Spatial structure, selective grazing by zooplankton and species-specific viruses add limiting factors and make rare species grow faster than common ones.

Diatoms in laboratory cultures provide a direct test of fluctuations: at constant 18 °C *Cyclotella pseudostelligera* excluded *Fragilaria crotonensis*, at constant 24 °C the reverse happened, and when the temperature alternated between 18 and 24 °C every 12 hours the two coexisted, both in a fitted consumer–resource model and in the experiment (Descamps-Julien and Gonzalez 2005).

## 23.5. Modern Coexistence Theory

### 23.5.1. The Invasion Criterion

Chesson (2000) organized coexistence theory around one question: can each species increase when it is rare and the others are at their typical (equilibrium or fluctuating) state? If so, no species can be lost through competition, because any species that becomes rare tends to recover. The *invasion growth rate* $\bar r_i$, the long-term average per capita growth rate of species $i$ when rare, is the central quantity; the eigenvalue $\rho(1 - b)$ of [7.19.22](/7.19.22) (Theorem 22.4.1) is its simplest case. Two species coexist robustly ("stably" in the stochastic sense) if both invasion growth rates are positive.

Mechanisms that allow coexistence act by making species limit themselves more than they limit others, so that a species gains an advantage when rare. Chesson distinguished two kinds of difference between species.

**Definition 23.5.1 (Stabilizing and Equalizing Mechanisms)** A **stabilizing mechanism** is a difference between species that concentrates intraspecific relative to interspecific competition (a *niche difference*), giving each species an advantage when rare. An **equalizing mechanism** reduces the difference in average competitive ability between species (their *fitness difference*), without itself favoring a species when rare. Coexistence requires that niche differences outweigh fitness differences.

For two species in Lotka–Volterra form the decomposition is exact.

**Theorem 23.5.1 (Niche and Fitness Differences in Lotka–Volterra Competition)** For $\mathrm{d}N_i/\mathrm{d}t = r_iN_i(1 - a_{ii}N_i - a_{ij}N_j)$, $i \ne j \in \{1, 2\}$, with all $a > 0$, define the *niche overlap* and the *fitness ratio*

$$
\rho = \sqrt{\frac{a_{12}a_{21}}{a_{11}a_{22}}},\qquad \frac{\kappa_1}{\kappa_2} = \sqrt{\frac{a_{22}a_{21}}{a_{11}a_{12}}}.
$$
The two species coexist stably if and only if

$$
\rho < \frac{\kappa_1}{\kappa_2} < \frac{1}{\rho}.
\tag{23.5}
$$
If $\rho < 1$ and $\kappa_1/\kappa_2 > 1/\rho$, species 1 excludes species 2; if $\kappa_1/\kappa_2 < \rho$, species 2 excludes species 1; if $\rho > 1$, the system is bistable or one species wins.

**Proof** Species 2 alone settles at $N_2 = 1/a_{22}$, and the invasion growth rate of species 1 is $r_1(1 - a_{12}/a_{22})$, positive if and only if $a_{12} < a_{22}$. Similarly species 2 invades species 1 if and only if $a_{21} < a_{11}$. Now

$$
\rho < \frac{\kappa_1}{\kappa_2} \iff \frac{a_{12}a_{21}}{a_{11}a_{22}} < \frac{a_{22}a_{21}}{a_{11}a_{12}} \iff a_{12}^2 < a_{22}^2,\qquad
\frac{\kappa_1}{\kappa_2} < \frac{1}{\rho} \iff \frac{a_{22}a_{21}}{a_{11}a_{12}} < \frac{a_{11}a_{22}}{a_{12}a_{21}} \iff a_{21}^2 < a_{11}^2.
$$
So (23.5) is mutual invasibility, which by [7.19.22](/7.19.22) (Theorem 22.4.3, with $a = a_{12}/a_{22}$ and $b = a_{21}/a_{11}$ in its notation) is stable coexistence. The other cases follow from the same table. $\square$

Here $1 - \rho$ is the niche difference: $\rho = 1$ when each species' effect on the other equals its effect on itself, $\rho = 0$ when the species do not interact. The fitness ratio measures how much better one species is when niche differences are ignored. The coexistence region of (23.5) widens as $\rho$ decreases (Figure 4A): a large fitness difference needs a large niche difference to be offset. Stabilizing mechanisms move a pair of species to the right in this diagram, equalizing mechanisms toward the line $\kappa_1 = \kappa_2$. Equalizing alone can never produce coexistence; it only reduces the niche difference required. Species that are equal in fitness and have no niche difference ($\rho = 1$, $\kappa_1 = \kappa_2$) are neutral ([7.19.37](/7.19.37)).

Field experiments have begun to measure the two quantities. In annual plants of a Californian serpentine grassland, sown at different densities to estimate competition coefficients, niche differences were large enough to stabilize most pairs, but fitness differences were often larger, so that only a few pairs were predicted to coexist; removing the stabilizing effect in simulations reduced diversity sharply (Levine and HilleRisLambers 2009; Godoy et al. 2014). Phylogenetically close species tended to have smaller niche differences, but not necessarily smaller fitness differences.

### 23.5.2. Fluctuation-Independent and Fluctuation-Dependent Mechanisms

Stabilizing mechanisms are of two kinds.

- *Fluctuation-independent mechanisms* operate at equilibrium: resource partitioning (Section 23.4), differences in the predators or pathogens that limit each species (frequency-dependent predation, the Janzen–Connell effect, [7.19.37](/7.19.37)), and spatial partitioning of habitats.
- *Fluctuation-dependent mechanisms* require variation in time or space. Chesson identified two.
  - *Relative nonlinearity* of competition: species differ in how nonlinearly their growth depends on a limiting factor, such as a resource, and that factor fluctuates. A species with a saturating response (type II) does relatively better when the resource fluctuates less, one with a more linear response when it fluctuates more; if each species, when common, generates the fluctuations that favor the other, both can invade. This is the mechanism of Armstrong and McGehee (1980): a consumer with a saturating functional response oscillates with its resource, and the time-averaged resource level $\bar R$ exceeds the $R^*$ of a second consumer with a linear response, which can therefore invade although its $R^*$ is higher than the first's.
  - The *storage effect*, the subject of the next section.

### 23.5.3. The Storage Effect

**Definition 23.5.2 (Storage Effect)** The **storage effect** is a coexistence mechanism in a temporally (or spatially) variable environment that operates when (i) species respond differently to the environment (each has good and bad times), (ii) the environment and competition covary, so that a species is most limited by competition when conditions favor it, and (iii) population growth is buffered, so that a species loses relatively little in bad times, for example through long-lived adults, seed banks or resting eggs that "store" the gains of good years.

The lottery model of Chesson and Warner (1981) shows the mechanism in its simplest form. Imagine two species of reef fish or forest trees that occupy all of a large number of sites, one adult per site. Each year a fraction $\delta$ of adults dies, and the vacant sites are filled by juveniles in proportion to the recruitment $B_i(t)N_i$ of each species, where $N_i$ is the fraction of sites held by species $i$ and $B_i(t)$ its per capita fecundity in year $t$:

$$
N_i(t+1) = (1 - \delta)N_i(t) + \delta\,\frac{B_i(t)N_i(t)}{B_1(t)N_1(t) + B_2(t)N_2(t)}.
\tag{23.6}
$$
When species 1 is rare and species 2 holds almost all sites, $N_1(t+1)/N_1(t) \approx 1 - \delta + \delta B_1(t)/B_2(t)$, so the invasion growth rate is

$$
\bar r_1 = \mathbb{E}\Big[\ln\big(1 - \delta + \delta\,X\big)\Big],\qquad X = \frac{B_1}{B_2}.
$$

**Proposition 23.5.1 (Storage Effect in the Lottery Model)** Let $\ln B_1 - \ln B_2 = Z$ have mean $\Delta\mu$ and variance $\sigma_Z^2$. If $\delta = 1$ (no adult survival), $\bar r_1 = \Delta\mu$: the species with the larger mean log fecundity wins, whatever the variability. If $0 < \delta < 1$, $\bar r_1 > \ln\big(1 - \delta + \delta\,\mathrm{e}^{\Delta\mu}\big)$ whenever $\sigma_Z > 0$, and $\bar r_1$ increases with the variability of $Z$; for sufficiently large variability both species have positive invasion growth rates and coexist, even if one has a lower mean fecundity.

**Proof** For $\delta = 1$, $\ln X = Z$, so $\bar r_1 = \mathbb{E}Z = \Delta\mu$, and by symmetry $\bar r_2 = -\Delta\mu$: one invasion rate is negative. For $0 < \delta < 1$ let $g(z) = \ln(1 - \delta + \delta\mathrm{e}^z)$. Then

$$
g''(z) = \frac{\delta(1 - \delta)\,\mathrm{e}^z}{(1 - \delta + \delta\mathrm{e}^z)^2} > 0,
$$
so $g$ is strictly convex and Jensen's inequality gives $\bar r_1 = \mathbb{E}\,g(Z) > g(\mathbb{E}Z)$ for nondegenerate $Z$. For normal $Z$, increasing $\sigma_Z$ with the mean fixed is a mean-preserving spread, which increases $\mathbb{E}\,g(Z)$ for convex $g$. As $\sigma_Z \to \infty$, $g(z) \ge \ln\delta + z$ for $z > 0$ and $g(z) \ge \ln(1 - \delta)$ for all $z$, so $\mathbb{E}\,g(Z) \ge \ln(1 - \delta) + \mathbb{E}\big[(\ln\delta - \ln(1 - \delta) + Z)^+\big] \to \infty$; the same holds for $\bar r_2$, so both become positive. $\square$

The convexity has a biological meaning. Because adults survive, a rare species cannot lose more than the fraction $\delta$ in a bad year, but it can gain greatly in a good year for it, when its competitor recruits poorly and many sites are won by its juveniles. The common species does not enjoy this asymmetry, because its good years are also years of intense intraspecific competition for the vacant sites: environment and competition covary. Figure 4B–D shows the model with independent lognormal fecundities. With long-lived adults ($\delta = 0.1$) both species persist indefinitely, although species 1 has the lower mean fecundity; with an annual life cycle ($\delta = 1$) species 1 is lost within a century.

Storage effects have been documented in desert annual plants, whose seed banks buffer bad years and whose germination responds differently to the timing of rains (Angert et al. 2009); in *Daphnia* species whose diapausing eggs persist in lake sediments (Cáceres 1997); in two saltbushes of the Chihuahuan Desert, *Atriplex acanthocarpa*, which increases fast in wet years and declines fast in dry ones, and the longer-lived *A. canescens*, which changes little (Verhulst et al. 2008); and in tropical trees and coral reef fishes, the systems for which the lottery model was designed. Environmental variation can also make communities easier to invade but less affected by invasion, because it allows invaders and residents to coexist (Melbourne et al. 2007).

![Modern coexistence theory. A: two Lotka–Volterra competitors coexist if their fitness ratio lies between the niche overlap ρ and its reciprocal (Theorem 23.5.1, shaded); stabilizing mechanisms increase the niche difference 1 − ρ, equalizing mechanisms bring the fitness ratio toward 1. B–C: the lottery model (Eq. (23.6)) with independent lognormal fecundities (σ = 1.2; species 1 has a 10 % lower mean log fecundity). B: with long-lived adults (a fraction δ = 0.1 dying each year) the species fluctuate but both persist. C: with an annual life cycle (δ = 1) the species with the higher mean fecundity excludes the other. D: the long-run growth rate of species 1 when rare as a function of the environmental variability σ for four adult death rates: with δ < 1 it becomes positive when fluctuations are large enough (the storage effect); with δ = 1 it stays equal to the mean disadvantage](./plots/coexistence-theory.py)

## 23.6. History, Space and Disturbance

Coexistence also depends on processes that the models above omit.

- *Priority effects.* When competitors arrive at different times, the first may win even if it is the weaker competitor in a simultaneous start. In experiments with the reef fishes *Thalassoma hardwicke* and *T. quinquevittatum* at Moorea, *T. quinquevittatum* won when both arrived together, but a 5- or 12-day head start reversed the outcome in favor of the resident *T. hardwicke* (Geange and Stier 2009). Fukami (2015) distinguished *niche preemption*, in which the early species uses up resources or space, from *niche modification*, in which it changes the habitat qualitatively, facilitating or inhibiting later species ([7.19.36](/7.19.36)). The bistable case of the Lotka–Volterra model ([7.19.22](/7.19.22)) is the simplest model of a priority effect. If space is preempted by different species in different patches, the landscape as a whole can hold both.
- *Competition and colonization.* In patchy, disturbed environments a poor competitor that is a better colonizer can coexist with a superior competitor by reaching vacant patches first (the **competition–colonization trade-off**, [7.19.16](/7.19.16), Theorem 16.6.1). Four species of ants on whistling-thorn acacias in Kenya form a strict competitive hierarchy for occupying trees (*Crematogaster sjostedti* > *C. mimosae* > *C. nigriceps* > *Tetraponera penzigi*), but their ability to colonize trees vacated by fire, elephants or drought by foundress queens is exactly the reverse, and all four coexist within any 100 m² (Palmer et al. 2000; Stanton et al. 2002).
- *Aggregation.* If the superior competitor is clumped among patches independently of the inferior one, it competes mostly with itself and leaves patches where the inferior species escapes competition (Atkinson and Shorrocks 1981). In experiments with four marine invertebrates settling on panels in Queensland, the dominant ascidian grew less, and two inferior competitors fared better, when each species was aggregated than when individuals were randomly mixed (Hart and Marshall 2009); sowing wild plants of field margins in intraspecific clumps similarly increased the survival of the weakest competitors (Wassmuth et al. 2009).
- *Disturbance and predation.* Disturbance that kills individuals regardless of species, or predators that prefer the commonest prey, keep the dominant competitor below the density at which it would exclude the others, a theme developed in the intermediate disturbance hypothesis and keystone predation ([7.19.33](/7.19.33)).

In each case heterogeneity, in space, time or among individuals, has a stabilizing effect, because it again makes intraspecific competition stronger relative to interspecific competition. The common thread of the chapter is that this inequality, however it arises, is what coexistence requires.

## Summary

- The niche (Grinnell's habitat, Elton's role, Hutchinson's $n$-dimensional hypervolume; **ecological niche** of 7.10.15) describes the conditions and resources a species needs. The **fundamental niche** is reduced by competitors and predators to the **realized niche** (Definition 23.1.1; Connell's barnacles, Example 23.1.1; Tansley's bedstraws, Example 23.1.2). Species partition space, time, resources and conditions.
- Resource utilization curves define niche overlap (Definition 23.2.1); for Gaussian curves $\alpha = \mathrm{e}^{-d^2/4w^2}$ (Proposition 23.2.1). Three species coexist for $2\alpha/(1 + \alpha^4) < K_2/K_1 < 1/\alpha$ (Proposition 23.2.2): **limiting similarity** (Definition 23.2.2) is a narrowing of conditions, roughly $d/w \gtrsim 1$, not a universal threshold.
- The **competitive exclusion principle**, ecological release (ocelots) and **character displacement** (finches, mongooses, sticklebacks, *Pseudomonas*) link competition to niche differences; cascade reinforcement and convergent displacement extend the idea to signals.
- MacArthur's consumer–resource model gives Lotka–Volterra competition with $a_{ij}$ proportional to the overlap of consumption, a symmetric structure and global stability (Proposition 23.4.1).
- In the chemostat the species with the lowest break-even concentration $R^*$ excludes the others (Definition 23.4.1, Theorem 23.4.1; phytoplankton, grasses, geckos). With two resources, crossing isoclines, a supply point in the cone of the consumption vectors and each species consuming more of the resource that limits it give coexistence (Theorem 23.4.2; diatoms, rotifers, prairie grasses).
- The paradox of the plankton is resolved by fluctuations, endogenous oscillations and chaos, heterogeneity and natural enemies.
- Coexistence requires positive invasion growth rates. In Lotka–Volterra form, $\rho < \kappa_1/\kappa_2 < 1/\rho$ (Theorem 23.5.1): stabilizing (niche) differences must exceed fitness differences, which equalizing mechanisms reduce (Definition 23.5.1). Fluctuation-dependent mechanisms are relative nonlinearity and the storage effect (Definition 23.5.2), which in the lottery model follows from the convexity of buffered growth (Proposition 23.5.1).
- Priority effects, competition–colonization trade-offs, aggregation and disturbance allow coexistence without classical niche partitioning; all work by strengthening intraspecific relative to interspecific competition.

## Questions

1. Two species have Gaussian utilization curves of width $w = 2$ mm (prey length) with peaks at 10 mm and 13 mm. Compute their competition coefficient. If a third species with its peak at 16 mm joins them, with the outer species having equal carrying capacities $K$, for what range of carrying capacities of the middle species can all three coexist?

   **Answer** $d/w = 1.5$, so $\alpha = \exp(-2.25/4) = \mathrm{e}^{-0.5625} = 0.570$, and $\alpha^4 = \mathrm{e}^{-2.25} = 0.105$. By (23.2), $2\alpha/(1 + \alpha^4) = 1.140/1.105 = 1.03$ and $1/\alpha = 1.75$: the middle species coexists with the other two if $1.03K < K_2 < 1.75K$. It needs a slightly higher carrying capacity than the outer species because it competes on both sides.

2. Species A and B compete for one resource in a chemostat with $D = 0.2$ per day. A has $\mu_{\max} = 0.8$ per day and $k = 4$ µmol L⁻¹; B has $\mu_{\max} = 0.5$ per day and $k = 1$ µmol L⁻¹. Which species wins? Is there a dilution rate at which the outcome is reversed?

   **Answer** $R_A^* = 0.2 \cdot 4/(0.8 - 0.2) = 1.33$ and $R_B^* = 0.2 \cdot 1/(0.5 - 0.2) = 0.67$ µmol L⁻¹, so B wins. In general $R^* = Dk/(\mu_{\max} - D)$; the two are equal when $4/(0.8 - D) = 1/(0.5 - D)$, that is $2 - 4D = 0.8 - D$, $D = 0.4$. For $D > 0.4$ (but $D < 0.5$), A has the lower $R^*$ and wins: at high loss rates the fast-growing species is favored, at low loss rates the efficient one. For $D \ge 0.5$ B cannot persist at all.

3. Explain, using Tilman's graphical model, why adding nitrogen fertilizer to a nitrogen-limited grassland often reduces plant species diversity.

   **Answer** On nitrogen-poor soils most species are limited by nitrogen, and coexistence of several species requires that they be limited by different resources at their crossing isoclines (for example nitrogen and light). Fertilization moves the supply point to high nitrogen relative to light: the supply ratio moves out of the coexistence cones toward the region in which light becomes relatively scarce for all species, and the species with the lowest light requirement $L^*$ (usually tall, fast-growing species that shade the others) excludes the rest. In addition, fertilization reduces the number of distinct limiting resources, which reduces the number of species that can coexist. Long-term fertilization experiments at Rothamsted (Park Grass) and Cedar Creek show exactly this loss of diversity.

4. For the Lotka–Volterra competitors with $a_{11} = 1.0$, $a_{22} = 0.8$, $a_{12} = 0.6$, $a_{21} = 0.7$, compute the niche overlap and fitness ratio and decide whether they coexist. Which single coefficient change would be equalizing, and which stabilizing?

   **Answer** $\rho = \sqrt{0.6 \cdot 0.7/(1.0 \cdot 0.8)} = \sqrt{0.525} = 0.725$; $\kappa_1/\kappa_2 = \sqrt{0.8 \cdot 0.7/(1.0 \cdot 0.6)} = \sqrt{0.933} = 0.966$. Since $0.725 < 0.966 < 1/0.725 = 1.38$, they coexist (check: $a_{12} = 0.6 < a_{22} = 0.8$ and $a_{21} = 0.7 < a_{11} = 1.0$). Reducing both interspecific coefficients in proportion, e.g. $a_{12}$ and $a_{21}$ by the same factor, reduces $\rho$ and leaves the fitness ratio unchanged: a purely stabilizing change. Multiplying the row of species 1, $a_{11}$ and $a_{12}$, by a common factor $c$ (species 1 becoming uniformly more or less sensitive to competition) leaves $\rho$ unchanged and multiplies $\kappa_1/\kappa_2$ by $1/c$: a purely equalizing (or unequalizing) change.

5. In the lottery model, why does the storage effect disappear if the fecundities of the two species are perfectly positively correlated, $B_1(t) = cB_2(t)$?

   **Answer** Then $X = B_1/B_2 = c$ is constant, the invasion growth rate is $\ln(1 - \delta + \delta c)$, positive only if $c > 1$, and the reciprocal rate for species 2 is $\ln(1 - \delta + \delta/c)$, positive only if $c < 1$: exactly one species can invade. The storage effect requires species-specific responses to the environment (condition (i) of Definition 23.5.2): each species must have years that are good for it and bad for its competitor. Correlated responses remove the covariance between environment and competition that the mechanism exploits.

6. (Open question) Design a field experiment to test whether two coexisting species of annual plants coexist by a stabilizing mechanism, and describe what results would support neutral coexistence instead.

   **Answer** Sow each species at a range of densities alone and in mixture with a range of densities of the other (a response-surface design), measure seed production per individual, and fit a model of per capita fecundity as a function of the densities of both species (e.g. annual plant models of the Beverton–Holt type). From the fitted intra- and interspecific competition coefficients and the germination and seed survival rates, compute the niche overlap and fitness ratio and the predicted invasion growth rate of each species when rare. A direct test: sow each species at low frequency into established stands of the other and measure its per capita population growth; if both increase when rare and their per capita growth declines with their own frequency (negative frequency dependence), a stabilizing mechanism operates. Neutral coexistence would be indicated by equal per capita growth rates of both species at all relative frequencies (no frequency dependence), with fluctuations in relative abundance consistent with drift. Replicating the experiment across years would show whether fluctuation-dependent mechanisms (storage through the seed bank) contribute.
