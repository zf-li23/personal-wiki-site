---
title: Dispersal and Metapopulations
description: "Patterns, modes and causes of dispersal and migration, dispersal kernels and long-distance dispersal, density-dependent emigration and the demographic role of dispersal; metapopulations: concept and conditions, the Levins model analyzed completely, mainland–island and rescue-effect models, habitat destruction and the extinction debt, the incidence function model and metapopulation capacity, source–sink dynamics, and coexistence through the competition–colonization trade-off."
---

All organisms are where they are because they, or their ancestors, moved there. Movement links the local processes of birth and death studied in [7.19.9](/7.19.9)–[7.19.15](/7.19.15) to the spatial structure of the environment, and in a patchy world it can matter as much as births and deaths for the size and persistence of a population. This chapter first describes the patterns, modes and causes of **dispersal** and migration and their demographic consequences (Section 16.1). It then develops the theory of metapopulations, populations of local populations linked by dispersal: the concept (Section 16.2), the Levins model and its extensions (Section 16.3), the effects of habitat destruction (Section 16.4), spatially realistic models and source–sink dynamics (Section 16.5), and coexistence of competitors through a trade-off between competitive and colonizing ability (Section 16.6). The genetics of dispersal (gene flow, isolation by distance) is treated in [7.10.10](/7.10.10), the behavior of dispersal and migration in [7.18.20](/7.18.20) and [7.18.26](/7.18.26), and dispersal in continuous space (diffusion, invasion waves) in [7.19.17](/7.19.17); landscape structure and corridors return in [7.19.48](/7.19.48)–[7.19.49](/7.19.49).

## 16.1. Dispersal and Migration

### 16.1.1. Kinds of Movement

Dispersal, defined in [Definition 10.2.1](/7.10.10#def-10.2.1) of 7.10.10 as movement from the place of birth to the place of reproduction, is in a broader ecological sense any movement of individuals away from others: of seeds away from the parent and from one another, of voles from one grassland to another, of birds among islands in search of habitat. It is usually divided into natal dispersal (from birthplace to first breeding site) and breeding dispersal (between successive breeding sites) ([7.18.26](/7.18.26)). **Migration** ([7.18.20](/7.18.20)) is the directed movement of individuals, often of whole populations, between regions used at different times, usually in a regular seasonal cycle. Every movement has three phases, each with its own causes and its own demographic consequence: leaving (emigration), transfer, and settlement (immigration).

Migrations can be classified by what they achieve, although most combine several functions:

- tracking a resource that moves: shore crabs following the tide; monarch butterflies (*Danaus plexippus*), which overwinter in Mexico and recolonize North America over four generations as their milkweed host plants grow; desert locusts (*Schistocerca gregaria*), whose swarms fly downwind toward areas where rain is likely;
- moving between distinct habitats: planktonic algae that sink at night to take up nutrients and rise by day to photosynthesize, amphibians that breed in water and live on land, giant pandas in the Qinling Mountains that feed on the bamboo *Fargesia spathacea* at 1900–3000 m in summer and on *Bashania fargesii* at 1000–2100 m from October to May (Loucks et al. 2003), so that reserves must include both elevation belts;
- one-way life-cycle migrations: Pacific salmon and European eels (*Anguilla anguilla*), which grow in one habitat and return to breed and die in another;
- seasonal escape and breeding: most migratory birds, and baleen whales that feed in polar waters in summer and breed in the tropics in winter.

Migrations evolved in environments with predictable seasonal cycles are triggered by proximate cues (day length) and preceded by physiological preparation; plague migrations of locusts are tactical responses to crowding in unpredictable environments.

### 16.1.2. Modes of Dispersal

Dispersal ranges from passive to active. Most seeds fall close to the parent: the density of seeds deposited by a plant, its *seed rain*, typically rises to a peak near the parent and falls steeply with distance, forming a seed shadow on the ground. The destination is determined by the position of the parent and by the distance distribution, but the microhabitat where a seed lands is left largely to chance. The small fraction that travels much farther is hard to measure ("most lost keys are found under streetlights") but important: seed-trap studies in New Zealand forests found that models with an input of long-distance dispersers fitted the data much better, the tail of the seed shadow extending ten times farther than the main peak (Canham et al. 2014). Wind-dispersed spiders and insects show the continuum between the extremes: young spiders actively climb to a high point and release silk threads (ballooning), and are then carried passively; even winged insects such as the midges (*Culicoides*) that carry bluetongue virus are effectively dispersed by the wind, and atmospheric dispersion models predicted the spread of bluetongue across northern Europe from 2006.

Animals that carry seeds make dispersal directed. Seeds of the mahaleb cherry *Prunus mahaleb* in Spain, assigned to their parent trees by genotyping, were deposited by small birds mostly near the parent and under shrubs, where seedlings establish best, whereas mammals and medium-sized birds (mistle thrushes, carrion crows) carried seeds much farther, into open habitats or pine forest, and accounted for most of the long-distance dispersal (Jordano et al. 2007). Modular organisms also disperse by clonal growth ([7.19.8](/7.19.8)): "guerrilla" growth forms with long connections between widely spaced ramets, such as many stoloniferous herbs and lianas, explore and invade new ground, whereas "phalanx" forms with short connections hold their ground and expand slowly. Many invasive aquatic weeds (water hyacinth, *Salvinia*, *Elodea*) spread mainly by fragments.

### 16.1.3. Dispersal Kernels

**Definition 16.1.1 (Dispersal Kernel)** A **dispersal kernel** is the probability density $k(\boldsymbol{x})$ of the displacement $\boldsymbol{x}$ between the origin of a propagule or individual (its parent or natal site) and the place where it settles. In two dimensions it is often described by the distribution of the distance $r = \lvert\boldsymbol{x}\rvert$, with density $g(r) = 2\pi r\,k(r)$ for an isotropic kernel.

Common kernels differ above all in their tails. A Gaussian kernel, the result of a random walk of fixed duration ([7.19.17](/7.19.17)), has tails that decay as $\mathrm{e}^{-r^2/(2\sigma^2)}$; the exponential (Laplace) kernel decays as $\mathrm{e}^{-r/a}$; *fat-tailed* kernels decay more slowly than any exponential, for example as a power of $r$ (the "2Dt" kernel $k(r) \propto (1 + r^2/u)^{-(p+1)}$ of Clark et al. 1999, or the Pareto family). Kernels with the same mean distance can differ by many orders of magnitude in the fraction of propagules that travel ten mean distances (Figure 1). The tail determines the speed of spread: populations with exponentially bounded kernels spread at a constant asymptotic speed, whereas fat-tailed kernels produce accelerating spread and patchy, leapfrogging advance fronts, as in the post-glacial spread of trees (Reid's paradox, Clark 1998) and many invasions (Neubert and Caswell 2000; [7.19.17](/7.19.17)). Kurtosis (the excess of both very short and very long moves over a Gaussian of the same variance) is a common summary of fat tails.

![Dispersal kernels with the same mean distance. A: distance densities of a Gaussian (half-normal), an exponential and a fat-tailed (Lomax) kernel, on a log scale: similar near the source, very different far away. B: probability of moving farther than r: beyond ten mean distances it is about 10^-15, 5×10^-5 and 6×10^-3. C: 2000 propagules dispersed from one parent with each kernel; only the fat-tailed kernel produces occasional distant colonists](./plots/dispersal-kernels.py)

### 16.1.4. Why Disperse? Density-Dependent and Variable Dispersal

The evolutionary forces acting on dispersal are discussed in [7.18.26](/7.18.26); they include escaping crowding and competition, avoiding competition with kin (the Hamilton–May model shows that some dispersal is favored even when it is costly and all sites are equal; [Theorem 26.6.1](/7.18.26#thm-26.6.1) of 7.18.26), avoiding inbreeding (balanced against outbreeding depression: in larkspur, *Delphinium nelsonii*, progeny from crosses with pollen from 1 m or 30 m both had lower fitness than from intermediate distances; Waser and Price 1994), and colonizing new habitat in a variable environment. Their demographic consequences are that dispersal is often density dependent, condition dependent and variable among individuals.

- Density-dependent emigration: spiders (*Erigone atra*) in a wind tunnel climbed launching points and adopted the "tiptoe" take-off posture more often at higher density, and spider mites (*Tetranychus urticae*) dispersed farther from denser and more related groups (De Meester and Bonte 2010; Bitume et al. 2013). Locally, density-dependent emigration regulates a population just as density-dependent mortality does ([7.19.11](/7.19.11)); globally the two differ, because emigrants may contribute to other populations.
- Dispersal polymorphism: many insects produce winged and wingless morphs, the pea aphid *Acyrthosiphon pisum* more winged morphs in the presence of predators; some plants produce two kinds of seed. The annual *Emex spinosa* produces dispersive aerial fruits and non-dispersing underground fruits, investing relatively more in aerial fruits at low density and high nutrient levels, a "good-year" dispersal strategy (Sadeh et al. 2009).
- Sex- and age-biased dispersal: in most birds females disperse farther, in most mammals males, a pattern related to mating systems and parental care (Greenwood 1980; [7.18.26](/7.18.26)).

### 16.1.5. The Demographic Significance of Dispersal

Dispersal is hard to measure and often ignored, but where it has been measured it is large. In a long-term study of great tits (*Parus major*) near Oxford, 57 % of breeding birds were immigrants (Greenwood et al. 1978). The sea rocket *Cakile edentula*, an annual of sand dunes in Nova Scotia, maintained itself only on the seaward beach, where seed production exceeded mortality; in the middle and landward zones of the dunes deaths always exceeded local births, yet the plant persisted there for years because most seeds produced on the beach were blown landward (Keddy 1981, 1982). The distribution of the plant was set by dispersal from a source into habitats where it could not replace itself, an example of source–sink dynamics (Section 16.5.3).

Dispersal habitat is therefore part of the habitat a species needs. Siberian flying squirrels (*Pteromys volans*) in Finland, which declined with intensive forestry, breed in mixed spruce–deciduous forest of a few hectares but move through a much larger area of pine and young forest; landscapes occupied by squirrels had three times more breeding habitat within 1 km than random landscapes, and also 23 % more dispersal habitat, which was better connected (Reunanen et al. 2000). For the violet copper butterfly *Lycaena helle* in Germany, patches with the larval food plant were more likely to be occupied if they were larger and less isolated (Bauerfeind et al. 2009): abundance was limited not by habitat but by the difficulty of reaching it. These observations lead directly to metapopulation theory.

## 16.2. Metapopulations

### 16.2.1. The Concept

Andrewartha and Birch (1954) had already emphasized that suitable habitat may be empty simply because individuals have failed to reach it. Levins (1969, 1970), working on the control of agricultural pests, formalized the idea for a species living in many patches, each of which is occupied or empty, and introduced the term metapopulation, "a population of populations".

**Definition 16.2.1 (Metapopulation)** A **metapopulation** is a set of local populations of a species, each occupying a discrete patch of habitat, that are linked by dispersal and whose dynamics are dominated by the extinction of local populations and the colonization of empty patches. A *local population* is a group of conspecific individuals in a patch that interact with each other with high probability; the *metapopulation dynamics* are the changes over time in the fraction (or number) of patches occupied.

Hanski (1999) listed four conditions for a classic metapopulation: (1) the habitat consists of discrete patches that can support local breeding populations; (2) even the largest local population has a substantial risk of extinction; (3) patches are not too isolated to be recolonized; (4) local dynamics are sufficiently asynchronous that simultaneous extinction of all local populations is unlikely. The size of a metapopulation is measured by the fraction of patches occupied, not by the number of individuals, and its most fundamental property is that it can persist in a balance between extinction and colonization even though none of its local populations is stable. In a metapopulation of the solitary bee *Andrena hattorfiana* in southern Sweden, surveyed from 2003 to 2006 in patches of its pollen plant *Knautia arvensis*, only 16 % of local populations persisted through the four years, yet the metapopulation as a whole was stable (Franzén and Nilsson 2010).

Real spatially structured populations form a continuum (Harrison and Taylor 1997).

| Type | Structure | Example |
|---|---|---|
| Classic (Levins) metapopulation | many similar patches, all prone to extinction | Glanville fritillary networks on the Åland Islands |
| Mainland–island metapopulation | one or a few large persistent populations and many small, ephemeral ones | silver-studded blue (*Plebejus argus*) in the Dulas Valley, North Wales |
| Patchy population | dispersal so frequent that patches form a single demographic unit | many mobile birds and insects |
| Non-equilibrium metapopulation | extinctions not balanced by colonizations, often after habitat loss | declining remnants in fragmented landscapes |
| Source–sink system | populations with births exceeding deaths support others where deaths exceed births | *Cakile edentula*; many birds in suboptimal habitat |

In North Wales the silver-studded blue occupied nearly all habitable patches within 1 km of existing populations; the empty patches were small and isolated, and some were shown to be habitable by successful introductions (Thomas and Harrison 1992). Between 1983 and 1990 small local populations went extinct and new ones appeared, much more so in heathland at South Stack Cliffs, where most populations were small, than in the limestone habitat of the Dulas Valley, where several large populations persisted. Plants with seed banks pose a special difficulty: an apparent recolonization may be the germination of buried seeds rather than dispersal, so true plant metapopulations are hard to demonstrate. The treacle mustard *Erysimum cheiranthoides* on the stony banks of the River Meuse in Belgium, whose sites are scoured by winter floods, is one example in which genetic assignment showed recolonization of empty sites by seeds carried by the river (Honnay et al. 2009).

The concept has shaped landscape planning. Beijing's master plan for 2016–2035 organizes the city's green space as a mountain ecological barrier, three rings of parks (including the first and second green isolation belts around the urban core), five river corridors and nine green wedges that link the mountains with the plain: a network of habitat patches and connecting corridors whose function for wildlife can be analyzed with the models of this chapter.

## 16.3. The Levins Model

### 16.3.1. Analysis

**Definition 16.3.1 (Levins Model)** The **Levins model** describes the fraction $p(t)$ of a large number of identical habitat patches that are occupied:

$$
\frac{\mathrm{d}p}{\mathrm{d}t} = cp(1 - p) - ep,
\tag{16.1}
$$
where $e$ is the rate at which local populations go extinct and $c$ the colonization rate: each occupied patch sends out colonists that establish in empty patches at rate $c$ per empty patch, so colonization is proportional both to the fraction of sources, $p$, and to the fraction of empty targets, $1 - p$.

The assumptions are strong: infinitely many patches, all equal in size and quality and equally accessible from each other (a spatially implicit model, in which space enters only through the existence of patches); extinction independent of the number of occupied patches; local dynamics so fast that a patch is simply occupied or empty.

**Theorem 16.3.1 (Dynamics of the Levins Model)** Let $p(0) \in (0, 1]$.

1. If $e/c \ge 1$, $p(t) \to 0$: the metapopulation goes extinct.
2. If $e/c < 1$, $p(t) \to p^* = 1 - e/c$, which is globally stable on $(0, 1]$; the extinct state $p = 0$ is unstable.
3. Eq. (16.1) is the logistic equation $\mathrm{d}p/\mathrm{d}t = rp(1 - p/K)$ with $r = c - e$ and $K = 1 - e/c$, so that for $c \ne e$

$$
p(t) = \frac{p^*}{1 + \bigl(p^*/p(0) - 1\bigr)\mathrm{e}^{-(c - e)t}} .
$$

**Proof** Rewrite $cp(1 - p) - ep = (c - e)p - cp^2 = (c - e)p\bigl(1 - \frac{c}{c - e}p\bigr)$, which is logistic with $r = c - e$ and $K = (c - e)/c = 1 - e/c$; the solution is that of the logistic equation ([7.19.10](/7.19.10), [2.2.15](/2.2.15)). For stability, $f(p) = (c - e)p - cp^2$ has $f'(0) = c - e$ and $f'(p^*) = c - e - 2cp^* = -(c - e)$. If $c > e$, the origin is unstable and $p^*$ stable, and since $f > 0$ on $(0, p^*)$ and $f < 0$ on $(p^*, 1]$, every solution with $p(0) > 0$ converges monotonically to $p^*$. If $c \le e$, $f(p) = (c - e)p - cp^2 < 0$ for all $p > 0$, so $p$ decreases to 0. $\square$

The condition for persistence, $c > e$, is the metapopulation analog of $R_0 > 1$: the ratio $c/e$ is the expected number of new local populations founded by one local population during its lifetime $1/e$ when almost all patches are empty. The equilibrium fraction of empty patches, $1 - p^* = e/c$, depends only on the ratio of extinction to colonization: a metapopulation always leaves a fraction $e/c$ of suitable habitat empty, a point that matters when habitat is destroyed (Section 16.4). Figure 2A shows the phase line for several values of $e/c$, and Figure 2B the approach to equilibrium together with a stochastic version with 50 patches.

With a finite number $n$ of patches the model becomes a stochastic patch occupancy model: a birth–death process for the number of occupied patches with "birth" rate $c k(n - k)/n$ and "death" rate $ek$. Extinction of the whole metapopulation is then certain, but by Theorem 15.1.2 of [7.19.15](/7.19.15#thm-15.1.2) the mean time to extinction grows exponentially with $n$; networks of a few tens of patches with $e/c$ close to 1 are at considerable risk.

![The Levins model. A: rate of change dp/dt against the fraction of patches occupied for four values of e/c; the stable equilibrium p* = 1 - e/c (points) exists only for e/c < 1. B: deterministic approach to p* = 0.5 from low and high occupancy (green) and one realization of a stochastic model with 50 patches (red), which fluctuates around p*. C: equilibrium occupancy p* = 1 - D - e/c when a fraction D of the patches is destroyed (solid) and the fraction of patches that are suitable but empty (dashed), which stays at e/c until the metapopulation collapses at D = 1 - e/c](./plots/levins-dynamics.py)

### 16.3.2. Mainland–Island Models and the Rescue Effect

Two extensions change the conclusions qualitatively. If colonists come from a permanent mainland population at rate $m$ per empty patch, independent of $p$ (the *propagule rain* model), then $\mathrm{d}p/\mathrm{d}t = m(1 - p) - ep$ with the globally stable equilibrium $p^* = m/(m + e)$: the island populations can never all disappear, and the model is the single-species version of the MacArthur–Wilson **theory of island biogeography** ([7.19.34](/7.19.34)).

**Definition 16.3.2 (Rescue Effect)** The **rescue effect** (Brown and Kodric-Brown 1977) is the reduction in the extinction rate of local populations by immigration, which increases population size, supplements reproduction or restores genetic variation; in metapopulation models it makes the extinction rate decrease with the fraction of occupied patches.

If immigration rescues local populations in proportion to the fraction of occupied patches, so that the extinction rate is $e(1 - p)$, then $\mathrm{d}p/\mathrm{d}t = (c - e)p(1 - p)$ (Hanski 1982 with internal colonization): the only stable states are $p = 1$ if $c > e$ and $p = 0$ if $c < e$. More realistic versions, in which extinction decreases gradually with $p$ because more occupied patches mean more migrants and larger local populations, have an intermediate unstable threshold of $p$ with two stable equilibria, one with high and one with low (or zero) occupancy (Hanski and Gyllenberg 1993). Different metapopulations of the same species should then occupy either a high or a low fraction of their patches, and this bimodal distribution has been found among the networks of the Glanville fritillary (Hanski et al. 1995). Positive feedback between occupancy and local persistence is a form of Allee effect at the metapopulation level ([7.19.15](/7.19.15)).

## 16.4. Habitat Destruction and the Extinction Debt

Let a fraction $D$ of the patches be destroyed permanently. Colonists landing in destroyed patches are lost, so

$$
\frac{\mathrm{d}p}{\mathrm{d}t} = cp(1 - D - p) - ep,
\tag{16.2}
$$
where $p$ is still the fraction of all original patches that are occupied.

**Theorem 16.4.1 (Persistence Under Habitat Destruction)** The metapopulation (16.2) persists if and only if $D < 1 - e/c$, and then tends to $p^* = 1 - D - e/c$. The fraction of patches that are suitable but empty at equilibrium is $e/c$, independent of $D$; the metapopulation goes extinct when the fraction destroyed equals the fraction occupied before destruction.

**Proof** Equation (16.2) is Eq. (16.1) with $c$ replaced by $c' = c(1 - D)$ applied to $p' = p/(1 - D)$, the fraction of the remaining patches that is occupied: $\mathrm{d}p'/\mathrm{d}t = c'p'(1 - p') - ep'$. By Theorem 16.3.1 it persists iff $e/c' < 1$, i.e. $D < 1 - e/c$, with $p'^* = 1 - e/(c(1 - D))$ and $p^* = (1 - D)p'^* = 1 - D - e/c$. The suitable but empty fraction is $1 - D - p^* = e/c$. Before destruction $p_0^* = 1 - e/c$, so the extinction threshold is $D = p_0^*$. $\square$

The result (Lande 1987, Nee and May 1992) has a sobering corollary. Habitat that is suitable but empty is not "spare": the empty fraction $e/c$ is required for the metapopulation to persist, and a species can be driven extinct by the destruction of habitat that it did not occupy at the time. Persistence requires that the fraction of habitat remaining exceeds $e/c$, which may be close to 1 for poor colonizers. Figure 2C shows the linear decline of occupancy with $D$.

**Definition 16.4.1 (Extinction Debt)** The **extinction debt** is the number (or fraction) of species in a community, or of populations in a region, that are destined to go extinct because of past habitat loss or fragmentation, but have not yet done so because extinction takes time (Tilman et al. 1994).

Tilman, May, Lehman and Nowak (1994) extended Eq. (16.2) to many competing species ranked by competitive ability, each displaced from a site by any better competitor that arrives (Section 16.6). Coexistence of many species in such a community requires that better competitors be poorer colonizers. Habitat destruction therefore eliminates first the best competitors, which are poor colonizers, even if they are abundant; and their decline after the destruction can take very long, because their population dynamics are slow near the extinction threshold. In the example of Figure 3, destroying 25 % of the sites dooms the dominant species, which was the most abundant, but it takes five centuries to fall below 1 % of its former abundance, while inferior competitors increase. The extinctions predicted for a given amount of habitat loss are thus "owed" for many generations, during which the debt might still be repaid by habitat restoration.

The evidence for extinction debts comes from comparisons between present species richness and present and past habitat. In Estonian dry calcareous grasslands, specialist plant richness was explained by the area and connectivity of grasslands 70 years earlier rather than by present area (Helm, Hanski and Pärtel 2006); many similar cases, in which the richness of plants or butterflies in fragmented habitats is better predicted by past than by present habitat, are reviewed by Kuussaari et al. (2009). The application of species–area relationships to predicting extinctions from habitat loss, and its biases, is discussed in [7.19.51](/7.19.51).

![Habitat destruction in a ten-species competition–colonization hierarchy (Tilman et al. 1994; mortality 0.05 per year, geometric initial abundances). A: abundances after 25 % of the sites are destroyed. The best competitor (species 1, red), although the most abundant, declines slowly to extinction, taking about 500 years to fall below 1 % of its initial abundance, while poorer competitors such as species 2 increase. B: number of species eventually lost (line) and time until species 1 falls below 1 % (points), against the fraction destroyed: the closer the destruction to the threshold, the longer the delay](./plots/extinction-debt.py)

## 16.5. Spatially Realistic Metapopulations

### 16.5.1. The Incidence Function Model

Real patches differ in size and isolation, and these differences have predictable effects: small patches support small populations that go extinct more often, and isolated patches receive fewer colonists. Hanski's (1994) incidence function model captures this with patch-specific probabilities per year:

$$
E_i = \min\left(1, \frac{e}{A_i^{x}}\right), \qquad C_i = \frac{S_i^2}{S_i^2 + y^2}, \qquad S_i = \sum_{j\ne i}p_j\,\mathrm{e}^{-\alpha d_{ij}}A_j^{b},
\tag{16.3}
$$
where $A_i$ is the area of patch $i$, $x$ describes how extinction risk declines with area, $S_i$ is the *connectivity* of patch $i$ (the contributions of occupied patches $j$, $p_j = 1$, weighted by their area and declining with distance $d_{ij}$ at a rate $\alpha$ set by the dispersal ability of the species), and $y$ describes how colonization saturates with connectivity. If patch $i$ is treated as a two-state Markov chain with constant $E_i$ and $C_i$, its long-run probability of being occupied, the *incidence*, is

$$
J_i = \frac{C_i}{C_i + E_i - C_iE_i} .
$$
Fitted to snapshot data on occupancy, areas and positions, the model estimates its parameters from the dependence of incidence on area and connectivity and can then be simulated to predict the dynamics of the network, for instance after the loss of particular patches. Figure 4 shows a simulated network.

![A simulated metapopulation in the incidence function model (60 patches in a 10 km × 10 km landscape, illustrative parameters). A: the patch network, with circle size increasing with patch area and fill showing the fraction of 400 years in which each patch was occupied. B: incidence against patch area for patches of low, middle and high connectivity (points), with the equilibrium incidence J = C/(C + E - CE) for three fixed connectivities (lines). Large, well-connected patches are almost always occupied, small isolated ones rarely](./plots/incidence-function.py)

The Glanville fritillary (*Melitaea cinxia*) on the Åland Islands, southwestern Finland, is the model system of metapopulation biology. The butterfly lives in dry meadows with its larval host plants *Plantago lanceolata* and *Veronica spicata*; about 4000–4500 meadow patches, with a median area of only 0.06 ha, have been surveyed every autumn since 1993 for the conspicuous winter nests of the larvae. Local populations turn over rapidly, and the patches fall into about 125 semi-independent networks, grouped by the typical lifetime dispersal of 2–3 km. The probability that a meadow is occupied increases with its area and connectivity as the incidence function model predicts, and the model fitted to one part of the region predicted occupancy elsewhere.

### 16.5.2. Metapopulation Capacity

Hanski and Ovaskainen (2000) asked when a spatially realistic network can support a species at all. In continuous time, let patch $i$ be colonized at rate $C_i = c\sum_{j\ne i}\mathrm{e}^{-\alpha d_{ij}}A_jp_j$ and its population go extinct at rate $E_i = e/A_i$, so that the probability $p_i$ that patch $i$ is occupied obeys $\mathrm{d}p_i/\mathrm{d}t = C_i(1 - p_i) - E_ip_i$.

**Proposition 16.5.1 (Metapopulation Capacity)** Let $M$ be the symmetric matrix with $m_{ij} = A_iA_j\mathrm{e}^{-\alpha d_{ij}}$ for $i \ne j$ and $m_{ii} = 0$, and let $\lambda_M$ (the *metapopulation capacity* of the network) be its leading eigenvalue. Then the state with all patches empty is unstable, so that the metapopulation can invade and persist, if and only if

$$
\lambda_M > \delta = \frac ec .
$$

**Proof** Near $\boldsymbol{p} = \boldsymbol{0}$, $\mathrm{d}\boldsymbol{p}/\mathrm{d}t \approx J\boldsymbol{p}$ with $J = cW - e\Lambda$, where $W_{ij} = \mathrm{e}^{-\alpha d_{ij}}A_j$ ($i \ne j$), $W_{ii} = 0$ and $\Lambda = \operatorname{diag}(1/A_1, \dots, 1/A_n)$. Since $W = \Lambda M$, $J = \Lambda(cM - eI)$. The matrix $\Lambda^{-1/2}J\Lambda^{1/2} = \Lambda^{1/2}(cM - eI)\Lambda^{1/2}$ is similar to $J$, so it has the same eigenvalues, and it is symmetric and congruent to $cM - eI$. By Sylvester's law of inertia, congruent symmetric matrices have the same numbers of positive, zero and negative eigenvalues. Hence $J$ has a positive eigenvalue if and only if $cM - eI$ does, that is, if and only if $c\lambda_M > e$. (By the Perron–Frobenius theorem, $\lambda_M$ is the largest eigenvalue in modulus and has a positive eigenvector when the network is connected.) $\square$

The proposition separates the properties of the species ($\delta = e/c$, the extinction threshold) from those of the landscape ($\lambda_M$, which increases with the areas of patches and their proximity on the scale of the species' dispersal, $1/\alpha$). The leading eigenvector weights each patch by its contribution to persistence, which ranks patches for protection. Hanski and Ovaskainen also showed that a suitably weighted equilibrium occupancy is approximately $p_\lambda^* = 1 - \delta/\lambda_M$, the spatially realistic analog of $p^* = 1 - e/c$. For the Glanville fritillary networks, the estimated threshold $\delta = 5.47$ separated viable from non-viable networks: of 92 networks with $\lambda_M < \delta$, 79 were extinct in at least five of 22 years, compared with only 5 of the 33 networks above the threshold, and networks below the threshold persisted mainly when they were close to other networks, a metapopulation of metapopulations (Hanski et al. 2017). The capacity can also reveal threats that area alone hides: for four bird species of the Central American highlands, reassessed habitat was 15–30 % of the previously assumed area, but the metapopulation capacity was only 1–6 % of the previous value because the remaining forest was fragmented (Schnell et al. 2013). For giant pandas in the Minshan Mountains, climate projections to 2100 predict a 16 % loss of habitat but a 35 % decline in the metapopulation capacity of protected areas (Shen et al. 2015).

Metapopulation dynamics also interact with evolution. In the Glanville fritillary, butterflies carrying the C allele at a site in the phosphoglucose isomerase gene *Pgi* have a higher flight metabolic rate and disperse farther; they are more frequent in newly founded local populations and in networks with high turnover and small patches, and the frequency of this allele explained as much of the variation in metapopulation size as the metapopulation capacity (Hanski et al. 2017).

### 16.5.3. Sources and Sinks

**Definition 16.5.1 (Source–Sink Dynamics)** In **source–sink dynamics** (Pulliam 1988), a species occupies habitats of different quality: in *source* habitats local births exceed deaths and there is a net export of emigrants; in *sink* habitats local deaths exceed births, and the local population persists only because of immigration from sources.

A simple model shows how large sinks can be. Let the source contain $\hat N_1$ breeding sites (territories), all occupied, and let each breeder produce enough surviving offspring and survive itself so that, without limitation, the population would grow by the factor $\lambda_1 > 1$ a year. Each year the surplus $(\lambda_1 - 1)\hat N_1$ cannot settle in the source and moves to the sink, where the population changes by the factor $\lambda_2 < 1$: $N_2(t + 1) = \lambda_2N_2(t) + (\lambda_1 - 1)\hat N_1$. The sink population tends to

$$
N_2^* = \frac{(\lambda_1 - 1)\hat N_1}{1 - \lambda_2} .
$$
With $\lambda_1 = 1.2$, $\lambda_2 = 0.9$ and $\hat N_1 = 100$, $N_2^* = 200$: two-thirds of the individuals live where the population cannot replace itself. Consequences: habitat quality cannot be judged from density; destroying a source can eliminate apparently thriving sink populations; and protecting the sink alone achieves nothing. Sinks can still be valuable, as reservoirs that buffer sources against catastrophes. When animals prefer sink habitat because their habitat cues have been decoupled from quality, the sink becomes an **ecological trap** ([7.18.26](/7.18.26)). Conservation planning for the northern wheatear in the Netherlands, where one population depended on immigrants from a neighboring one, followed this logic: the source was protected to sustain the sink (Van Oosten et al. 2015).

Two applications show how the theory guides management. For the critically endangered Mount Lofty Ranges southern emu-wren (*Stipiturus malachurus intermedius*), a poor flier occupying six swamp patches in South Australia, a stochastic patch occupancy model showed that the best action depends on which patches are occupied: connecting a large occupied patch by corridors to its neighbors when only it is occupied, enlarging a patch when only the two smallest are occupied; sequences of actions reduced the 30-year extinction risk by 50–80 % (Westphal et al. 2003). For range shifts under climate change, analogies with electrical circuits identify the patches through which most colonists "flow" and the bottlenecks where adding habitat helps most (Hodgson et al. 2016).

## 16.6. Competition and Colonization

Can a competitively inferior species persist with a superior one? In a homogeneous habitat, competitive exclusion ([7.19.22](/7.19.22)) predicts not. In a patchy habitat with local extinctions, an inferior competitor can survive as a *fugitive species* (Hutchinson 1951): it colonizes empty patches quickly and is displaced later by the superior competitor, but reaches new patches before it.

Let species 1 be the superior competitor, unaffected by species 2 and obeying the Levins model, and let species 2 colonize only empty patches and be displaced from its patches whenever species 1 colonizes them (Levins and Culver 1971, Hastings 1980, Tilman 1994):

$$
\frac{\mathrm{d}p_1}{\mathrm{d}t} = c_1p_1(1 - p_1) - e_1p_1, \qquad
\frac{\mathrm{d}p_2}{\mathrm{d}t} = c_2p_2(1 - p_1 - p_2) - e_2p_2 - c_1p_1p_2 .
\tag{16.4}
$$

**Theorem 16.6.1 (Coexistence Through the Competition–Colonization Trade-off)** Suppose $c_1 > e_1$, so that species 1 persists at $p_1^* = 1 - e_1/c_1$. Then species 2 can invade and the two species coexist, at the globally stable equilibrium

$$
p_2^* = 1 - p_1^* - \frac{e_2 + c_1p_1^*}{c_2},
$$
if and only if $p_2^* > 0$, that is

$$
c_2 > \frac{c_1(c_1 + e_2 - e_1)}{e_1} .
\tag{16.5}
$$
With equal extinction rates $e_1 = e_2 = e$, the condition is $c_2 > c_1^2/e = c_1 \cdot (c_1/e)$: the inferior competitor must be a better colonizer by at least the factor $c_1/e > 1$.

**Proof** Species 1 follows Theorem 16.3.1 independently of species 2. On the line $p_1 = p_1^*$, the second equation is $\mathrm{d}p_2/\mathrm{d}t = p_2\bigl[c_2(1 - p_1^* - p_2) - e_2 - c_1p_1^*\bigr]$, a logistic equation for $p_2$ whose positive equilibrium is the stated $p_2^*$; it exists and is globally attracting for $p_2(0) > 0$ exactly when the per capita growth rate of species 2 at $p_2 = 0$, $c_2(1 - p_1^*) - e_2 - c_1p_1^*$, is positive, which is the invasion condition. With $1 - p_1^* = e_1/c_1$ and $c_1p_1^* = c_1 - e_1$, the condition reads $c_2e_1/c_1 > e_2 + c_1 - e_1$, which is (16.5). Since $p_1(t) \to p_1^*$ for every positive initial value, solutions of the full system converge to $(p_1^*, p_2^*)$ (the system is triangular, and the theory of asymptotically autonomous equations applies). $\square$

The condition expresses a *competition–colonization trade-off*: the competitively superior species must be the poorer colonizer, and by a sufficient margin. With equal extinction rates, coexistence also requires $c_1^2/c_2 < e < c_1$: extinction (disturbance) must be frequent enough to keep opening patches for the fugitive, but not so frequent that the superior competitor cannot persist. This is one mechanism behind the **intermediate disturbance hypothesis** ([7.19.33](/7.19.33)). Figure 5 shows the regions of the parameter plane and an example: the fugitive spreads first, reaches 80 % of the patches and is then pushed back to 25 % as the superior competitor spreads.

![The competition–colonization trade-off (Eq. 16.4, equal extinction rates). A: outcomes in the plane of e/c1 and c2/c1: species 1 persists if e < c1; species 2 coexists with it if c2/c1 > c1/e (above the curve), and persists alone if species 1 cannot (right of e = c1, above the dashed line c2 = e). B: an example with c1 = 0.2, c2 = 0.8 and e = 0.1 per year (point in A): the fugitive species spreads first and is then partly displaced; the two species settle at 50 % and 25 % of the patches](./plots/competition-colonization.py)

Tilman (1994) extended the model to $n$ species ranked by competitive ability: species $i$ is displaced by all species $j < i$, and any number of species can coexist if colonization rates increase down the hierarchy fast enough; this is the model used for the extinction debt in Section 16.4. Plants show such trade-offs: in the grasslands of Cedar Creek, Minnesota, species that are strong competitors for nitrogen allocate much biomass to roots and produce few seeds, whereas good colonizers produce many small seeds. The theory has limitations. It assumes strict competitive hierarchies and instantaneous displacement; when superior competitors cannot displace established inferior ones, or colonists compete for the same empty sites (preemption), coexistence becomes much harder (Yu and Wilson 2001), and very similar species cannot coexist by this mechanism ("limiting similarity" in colonization rates). Nevertheless, competition–colonization trade-offs are an important explanation of diversity in disturbed and patchy habitats and of the order of species during succession ([7.19.36](/7.19.36)).

## Summary

- Dispersal (movement away from others; natal and breeding) and migration (directed, often seasonal, movement between regions) have three phases: emigration, transfer, immigration. Migrations track resources, connect distinct habitats or serve breeding, as in the elevational migration of Qinling pandas.
- Seed rain and seed shadows decline steeply with distance, but rare long-distance dispersal matters for colonization. Dispersal kernels (Definition 16.1.1) with the same mean can differ enormously in their tails; fat tails accelerate spread.
- Dispersal is often density dependent, polymorphic and sex biased; it can supply most of a population (great tits), sustain populations in habitats where they cannot replace themselves (*Cakile*), and limit abundance through isolation (violet copper); dispersal habitat is part of a species' habitat (flying squirrels).
- A metapopulation (Definition 16.2.1) persists by a balance of local extinction and colonization. Types range from classic to mainland–island, patchy, non-equilibrium and source–sink systems.
- The Levins model (Definition 16.3.1, Theorem 16.3.1): $\mathrm{d}p/\mathrm{d}t = cp(1 - p) - ep$ is logistic with $r = c - e$, $K = 1 - e/c$; persistence iff $c > e$; the empty fraction at equilibrium is $e/c$. A mainland gives $p^* = m/(m + e)$; the rescue effect (Definition 16.3.2) can create alternative stable states.
- Habitat destruction: $p^* = 1 - D - e/c$, extinction when $D$ equals the original occupancy (Theorem 16.4.1). Extinctions occur with long delays, the extinction debt (Definition 16.4.1), and in competitive hierarchies the best competitors are lost first.
- Spatially realistic models: the incidence function model (16.3) and metapopulation capacity, persistence iff $\lambda_M > e/c$ (Proposition 16.5.1), applied to the Glanville fritillary (threshold 5.47), Central American birds and pandas. Source–sink dynamics (Definition 16.5.1): $N_2^* = (\lambda_1 - 1)\hat N_1/(1 - \lambda_2)$, sinks may hold most individuals.
- Competition–colonization trade-off (Theorem 16.6.1): an inferior competitor coexists if $c_2 > c_1(c_1 + e_2 - e_1)/e_1$, which with equal extinction rates requires $c_1^2/c_2 < e < c_1$, linking fugitive coexistence to intermediate disturbance.

## Questions

1. For the Levins model with $c = 0.4$ and $e = 0.1$ per year, find the equilibrium occupancy and the time needed for $p$ to rise from $0.05$ to $0.5$. How much habitat can be destroyed before the metapopulation goes extinct?

   **Answer** $p^* = 1 - 0.1/0.4 = 0.75$ and $r = c - e = 0.3$ per year. From the logistic solution, $t = \frac1r\ln\frac{p(t)(p^* - p_0)}{p_0(p^* - p(t))} = \frac1{0.3}\ln\frac{0.5 \times 0.70}{0.05 \times 0.25} = \frac{\ln 28}{0.3} \approx 11$ years. By Theorem 16.4.1 the metapopulation persists while $D < 1 - e/c = 0.75$: up to three quarters of the patches can be destroyed, but at $D = 0.7$ only 5 % of all patches would be occupied, and with a finite number of patches the stochastic risk of extinction would already be high.

2. Derive the equilibrium of the propagule rain model $\mathrm{d}p/\mathrm{d}t = m(1 - p) - ep$ and of the model with both internal colonization and a mainland, $\mathrm{d}p/\mathrm{d}t = (m + cp)(1 - p) - ep$. Can the second model have $p^* = 0$?

   **Answer** Propagule rain: $p^* = m/(m + e)$, globally stable (linear equation). With both sources, $f(p) = (m + cp)(1 - p) - ep$ is a downward parabola with $f(0) = m > 0$ and $f(1) = -e < 0$, so it has exactly one root in $(0, 1)$, $p^* = \bigl[(c - m - e) + \sqrt{(c - m - e)^2 + 4cm}\bigr]/(2c)$, which is globally stable on $[0, 1]$. Since $f(0) = m > 0$, $p = 0$ is never an equilibrium: any immigration from a mainland prevents regional extinction, which is why mainland–island systems are more robust than classic metapopulations.

3. Show that in the source–sink model the sink can contain more individuals than the source, and find the condition. Why might a census of densities mislead a manager?

   **Answer** $N_2^* > \hat N_1$ iff $(\lambda_1 - 1)/(1 - \lambda_2) > 1$, i.e. $\lambda_1 + \lambda_2 > 2$: the surplus production of the source exceeds the deficit of the sink. Then most individuals live in habitat where they cannot replace themselves, and a census would rank the sink as the better habitat (more individuals), whereas demographic data (births and deaths per individual, $\lambda$ by habitat) would reveal the opposite. Protecting the sink and allowing the source to be destroyed would cause both populations to collapse.

4. For the competition–colonization model with $e_1 = e_2 = 0.1$ and $c_1 = 0.3$, what colonization rate must the inferior competitor have to coexist? If disturbance increases $e$ to $0.25$ for both species, what happens?

   **Answer** With equal extinction rates the condition is $c_2 > c_1^2/e = 0.09/0.1 = 0.9$, three times $c_1$. With $e = 0.25$: species 1 still persists ($e < c_1$), with $p_1^* = 1 - 0.25/0.3 = 0.17$, and the condition becomes $c_2 > 0.09/0.25 = 0.36$, so an inferior competitor with $c_2 = 0.9$ now coexists easily, with $p_2^* = 1 - 0.17 - (0.25 + 0.3 \times 0.17)/0.9 = 0.50$. If $e$ rose above $0.3$, species 1 would disappear. More disturbance favors the fugitive and, up to a point, coexistence.

5. Use Proposition 16.5.1 to explain why two networks with the same total habitat area can differ in their capacity to support a species, and which kind of network is better for a poor disperser.

   **Answer** The capacity $\lambda_M$ is the leading eigenvalue of the matrix with entries $A_iA_j\mathrm{e}^{-\alpha d_{ij}}$; it increases with the products of areas of pairs of patches and with their proximity relative to the dispersal scale $1/\alpha$. Concentrating the same area in a few large patches close together gives large entries and a high $\lambda_M$; spreading it over many small, distant patches gives small entries. For a poor disperser (large $\alpha$), all entries for distant pairs are near zero, so the capacity depends mainly on the size of individual clusters of nearby large patches; compact, well-connected networks (or corridors that reduce effective distance) are best. For a good disperser, many small patches spread widely may still give enough capacity and spread the risk of catastrophes. This is the metapopulation version of the SLOSS debate ([7.19.34](/7.19.34)).

6. (Open question) Discuss whether the Glanville fritillary on the Åland Islands is a good model for the conservation of large mammals such as the Amur tiger or giant panda.

   **Answer** Key points: the butterfly fits the classic metapopulation concept well (many small patches, frequent local extinction and recolonization, short generation time, a well-defined habitat that can be mapped), which made it possible to test the theory quantitatively. Large mammals have few, large local populations, long generation times and rare dispersal events; local extinctions are rarely observed, and the relevant dynamics are those of small populations (demographic and genetic stochasticity, [7.19.15](/7.19.15)) connected by occasional migrants. The general lessons transfer: persistence depends on the area and connectivity of habitat, not on area alone (metapopulation capacity of panda reserves), empty suitable habitat is needed, and extinction debts may hide future losses after fragmentation. But the parameters cannot be estimated from occupancy turnover, and connectivity must be analyzed with movement data and landscape resistance ([7.19.49](/7.19.49)) rather than with simple distance kernels.
