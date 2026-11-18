---
title: Island Biogeography and the Species–Area Relationship
description: "The species–area relationship S = cA^z: power and semilogarithmic forms, fitting, the values of z, and why richness grows with area (sampling, habitat diversity, area per se); the MacArthur–Wilson equilibrium theory derived for general and species-specific rates, turnover, the time to equilibrium, and the effects of area and isolation with target and rescue effects; tests by defaunation, area reduction, Krakatau, Surtsey and long-term censuses; disharmony and evolution on islands; habitat islands and metapopulations; SLOSS, nestedness, corridors and wildlife crossings."
---

Islands are natural replicates: they differ in area and isolation, and the number of species on them varies with both in regular ways. The **theory of island biogeography** of MacArthur and Wilson, introduced in [7.10.30](/7.10.30) with its simplest linear form, explains these regularities as a dynamic balance between the arrival of new species and the extinction of residents. This chapter develops the theory and its evidence in the depth that an ecology course needs. Section 34.1 treats the species–area relationship as a pattern and asks why richness should be a power of area. Section 34.2 derives the equilibrium theory in general form, including species that differ in their rates, the time needed to reach equilibrium and the effects of area and isolation. Section 34.3 reviews the experimental and natural tests, Section 34.4 the extension from oceanic islands to habitat islands and metapopulations, and Section 34.5 the consequences for conservation: the design of reserves and the connection of fragments. The theory built here is used again for fragmented landscapes in [7.19.49](/7.19.49) and for the loss of species in [7.19.51](/7.19.51); the evolutionary side of island biotas, speciation in place and adaptive radiation, is the subject of [7.10.30](/7.10.30).

## 34.1. The Species–Area Relationship

### 34.1.1. Islands and Area

Larger islands hold more species. The number of plant species on the Galápagos Islands increases from a handful on islets of a few hectares to several hundred on Isabela and Santa Cruz, and the bird species of the West Indies from a few on small cays to more than a hundred on Cuba and Hispaniola. The pattern, sometimes called the *island effect*, is one of the most consistent in ecology, and it is not restricted to islands in the sea. Lakes are islands of water in a sea of land, mountaintops islands of montane habitat above lowlands, caves islands of darkness, woodlots islands of forest in farmland, and even a single epiphytic bird's nest fern (*Asplenium goudeyi*) on Lord Howe Island is an island for the plants that grow in it; species richness increases with the size of all of them.

**Definition 34.1.1 (Species–Area Relationship)** The **species–area relationship** is the increase of the number of species $S$ with the area $A$ of an island or a sampled region. Its most common form is the power function of Arrhenius (1921),

$$
S = cA^{z}, \qquad \log S = \log c + z\log A, \tag{34.1}
$$
where $c$ is the number of species in a unit area and $z$ the slope on logarithmic axes. The semilogarithmic form of Gleason (1922), $S = a + b\log A$, fits some data better.

The power law is a straight line on log–log axes, so $z$ is usually estimated by linear regression of $\log S$ on $\log A$ ([3.3](/3.3)). Two cautions apply. First, the regression on logarithms estimates the median, not the mean, of $S$ at a given area, and its errors are assumed multiplicative; fitting $S = cA^z$ directly by nonlinear least squares weights the large islands more heavily and can give a different $z$. Second, the power and semilogarithmic forms, and saturating forms such as $S = S_{\max}A/(K + A)$, should be compared by a criterion such as AIC rather than chosen by eye; over the two or three orders of magnitude of area that most data sets span, several forms fit about equally well.

The meaning of $z$ is easy to remember: a tenfold increase of area multiplies $S$ by $10^z$, so with $z = 0.25$ a tenfold larger island holds $1.8$ times as many species and the number of species doubles for a 16-fold increase of area. Values of $z$ fall into recognizable groups (Table 1, after the compilation in Begon and Townsend 2021).

| Type of area | Examples ($z$) |
|---|---|
| Arbitrary areas within a mainland | Birds, Central Europe (0.09); flowering plants, England (0.10); birds, Nearctic (0.12); savanna vegetation, Brazil (0.14); land plants, Britain (0.16) |
| Oceanic islands | Birds, New Zealand islands (0.18); lizards, Californian islands (0.20); birds, West Indies (0.24); birds, East Indies (0.28); ants, Melanesia (0.30); land plants, Galápagos (0.31); beetles, West Indies (0.34); mammals, Scandinavian islands (0.35) |
| Habitat islands | Zooplankton in lakes, New York State (0.17); fish in lakes, New York State (0.24); birds in páramo, Andes (0.29); mammals on mountaintops, Great Basin (0.43); cave invertebrates, West Virginia (0.72) |

Two regularities stand out. Within a continuous mainland, where nested sample areas are compared, $z$ is low (about 0.1–0.2); for islands it is higher (about 0.2–0.35); and for isolated habitat islands it can be higher still. And island curves lie below mainland curves: an island holds fewer species than an equally large piece of mainland, most of all when it is small.

### 34.1.2. Why Richness Increases with Area

Three explanations, not mutually exclusive, have been proposed.

1. *Sampling.* A larger area contains more individuals and therefore, by chance alone, more species, because rare species are more likely to be included.
2. *Habitat diversity.* A larger area contains more kinds of habitat, each with its own species.
3. *Area per se.* Larger islands support larger populations, which go extinct less often, and are larger targets for colonists. This is the explanation of the equilibrium theory (Section 34.2).

The first can be made exact. Suppose that the individuals of a community are scattered independently over a region and that a plot covers a fraction $a$ of it (the *random placement* model of Coleman 1981).

**Proposition 34.1.1 (Random Placement)** If the $n_i$ individuals of species $i$ are placed independently and uniformly in a region, a plot covering a fraction $a$ of the region contains

$$
\mathbb{E}[S(a)] = \sum_{i}\left[1 - (1 - a)^{n_i}\right], \qquad \operatorname{Var}[S(a)] = \sum_i (1 - a)^{n_i}\left[1 - (1 - a)^{n_i}\right] \tag{34.2}
$$
species. The curve is increasing and concave in $a$, and its local slope on logarithmic axes, $z(a) = \mathrm{d}\ln\mathbb{E}[S]/\mathrm{d}\ln a$, decreases from 1 for very small plots to 0 as $a \to 1$.

**Proof** Species $i$ is absent from the plot if and only if none of its $n_i$ individuals falls in it, which has probability $(1 - a)^{n_i}$. $S(a)$ is the sum of the indicators $\boldsymbol{1}_{\{i \text{ present}\}}$, which are independent across species, so its mean and variance are the sums of the Bernoulli means and variances. Each term $1 - (1 - a)^{n_i}$ is increasing and concave in $a$. For small $a$, $1 - (1 - a)^{n_i} \approx n_ia$, so $\mathbb{E}[S] \approx a\sum_i n_i$ and $z \to 1$; as $a \to 1$, $\mathbb{E}[S]$ approaches the total number of species with zero derivative, so $z \to 0$. $\square$

Sampling alone thus produces a curve that looks like a power law over a few orders of magnitude, with local slopes of 0.2–0.5 at intermediate scales for a lognormal distribution of abundances (Figure 1A). Preston (1962) showed that for his "canonical" lognormal distribution of abundances the slope is close to $z \approx 0.26$ over a wide range, one reason why values near 0.25 are so common. The random placement model is the appropriate null model for nested samples within a mainland, and departures from it, usually because individuals of a species are aggregated, give steeper curves. For islands, sampling and habitat diversity are not enough: isolated islands hold fewer species than samples of the same area on the mainland, and the deficit must be explained by dynamics.

![Species–area relationships. A: passive sampling (Proposition 34.1.1) from a mainland community of 400 species with lognormal abundances: expected richness of a plot against the fraction of the region it covers (log–log axes) and its local slope z (dashed, right axis), which falls from 1 to 0 and lies between about 0.2 and 0.5 over the middle range. B: two simulated archipelagos under the equilibrium theory with area- and distance-dependent rates, S* = P/(1 + (e/i)A^(−x)e^(d/d₀)) with P = 200, x = 0.5: 30 islands each at 10 km (near) and 300 km (far) from the mainland, counts scattered around S*, with fitted power laws: the far islands hold fewer species and have a steeper fitted slope. C: the local slope of the model, z = x(1 − S*/P) (Proposition 34.2.4), for three distances: isolation steepens the species–area curve, and every curve flattens on large islands that approach saturation](./plots/species-area.py)

## 34.2. The Equilibrium Theory

### 34.2.1. Immigration, Extinction and Equilibrium

MacArthur and Wilson (1963, 1967) considered an island near a mainland pool of $P$ species. Let $S$ be the number of species on the island. The *immigration rate* $I(S)$ is the rate at which species not yet present arrive and establish; it is highest for an empty island, where every arrival is new, and falls to zero when all $P$ species are present. The *extinction rate* $E(S)$ is the rate at which resident species are lost; it is zero for an empty island and increases with $S$, because there are more species to lose and, with more competitors, each has a smaller population. Then

$$
\frac{\mathrm{d}S}{\mathrm{d}t} = I(S) - E(S). \tag{34.3}
$$

**Proposition 34.2.1 (The Equilibrium Number of Species)** Let $I$ and $E$ be continuous on $[0, P]$, with $I$ strictly decreasing, $E$ strictly increasing, $I(0) > 0$, $E(0) = 0$ and $I(P) = 0$. Then Eq. (34.3) has a unique equilibrium $S^* \in (0, P)$, it is globally asymptotically stable on $[0, P]$, and at equilibrium species continue to arrive and to go extinct at the common rate $\hat T = I(S^*) = E(S^*)$, the *turnover rate*.

**Proof** $h(S) = I(S) - E(S)$ is continuous and strictly decreasing, with $h(0) = I(0) > 0$ and $h(P) = -E(P) < 0$, so by the intermediate value theorem it has exactly one zero $S^*$ in $(0, P)$. For $S < S^*$, $\dot S = h(S) > 0$ and for $S > S^*$, $\dot S < 0$: every solution in $[0, P]$ moves monotonically toward $S^*$ (a one-dimensional phase line, [2.4.11](/2.4.11)). At $S^*$, $I(S^*) = E(S^*)$ by definition, and this common value is positive because $E$ is strictly increasing from $E(0) = 0$. $\square$

The linear case $I(S) = I_0(1 - S/P)$, $E(S) = E_0S/P$ of Eq. (30.1) in [7.10.30](/7.10.30) gives $S^* = PI_0/(I_0 + E_0)$ and $\hat T = I_0E_0/(I_0 + E_0)$. The theory makes four predictions: the number of species on an island approaches a characteristic value; it does so with a continual turnover of species; large islands hold more species than small ones; and remote islands hold fewer species than near ones. Only the second is unique to the equilibrium theory: constancy of numbers and the effect of area also follow from habitat diversity, and the effect of remoteness from limited dispersal alone. Turnover is therefore the critical test.

### 34.2.2. Species That Differ

The curves drawn by MacArthur and Wilson were concave rather than straight: the immigration rate falls steeply at first and the extinction rate rises more than in proportion to $S$. The reason is that species differ. Good dispersers arrive first, so the species that remain to arrive are the poor dispersers; species with small populations or specialized requirements go extinct first. The simplest model with this property treats each species separately.

Let species $i$ of the pool colonize the island, when absent, at rate $\lambda_i$, and go extinct, when present, at rate $\mu_i$, independently of the other species. Its presence is a two-state continuous-time Markov chain with stationary probability $p_i = \lambda_i/(\lambda_i + \mu_i)$ of being present (the continuous-time analogue of the two-state chain in [Example 9.3.2](/3.5.9#ex-9.3.2) of 3.5.9).

**Proposition 34.2.2 (Independent Species)** With independent two-state species, the number of species at stationarity has mean and variance

$$
\mathbb{E}[S^*] = \sum_{i=1}^{P}\frac{\lambda_i}{\lambda_i + \mu_i},\qquad \operatorname{Var}(S^*) = \sum_{i=1}^{P}p_i(1 - p_i) < \mathbb{E}[S^*], \tag{34.4}
$$
the expected turnover rate is $\hat T = \sum_i \lambda_i\mu_i/(\lambda_i + \mu_i)$, and an island emptied at $t = 0$ accumulates species as

$$
\mathbb{E}[S(t)] = \sum_i p_i\left(1 - \mathrm{e}^{-(\lambda_i + \mu_i)t}\right).
$$

**Proof** For one species, the probability $q_i(t)$ of presence satisfies $\dot q_i = \lambda_i(1 - q_i) - \mu_iq_i$, whose solution from $q_i(0) = 0$ is $q_i(t) = p_i(1 - \mathrm{e}^{-(\lambda_i + \mu_i)t})$, tending to $p_i$. $S$ is a sum of independent Bernoulli variables (a Poisson binomial variable), so its mean and variance are the sums of $p_i$ and $p_i(1 - p_i)$; the variance is smaller than the mean because $1 - p_i < 1$. At stationarity species $i$ immigrates at the rate $\lambda_i(1 - p_i) = \lambda_i\mu_i/(\lambda_i + \mu_i)$, and the total immigration rate equals the total extinction rate $\sum_i\mu_ip_i$, which is the same sum. $\square$

The variance result is a testable prediction: if species occupy islands independently, the number of species on replicate islands should vary less than a Poisson variable with the same mean. Plotting the total immigration rate $I(t) = \sum_i\lambda_i(1 - q_i(t))$ and the total extinction rate $E(t) = \sum_i\mu_iq_i(t)$ against $\mathbb{E}[S(t)]$ along the trajectory recovers the curved rate functions of MacArthur and Wilson (Figure 2A). An analysis of breeding birds on 13 small British islands found that immigration rates decreased and extinction rates increased with the number of residents, with significant curvature on several islands (Manne et al. 1998).

![The equilibrium theory with species that differ (Proposition 34.2.2): a pool of 100 species with lognormally distributed colonization and extinction rates, on a near island and a far island (colonization rates four times lower). A: immigration (solid) and extinction (dotted) rates against the number of species present, during recolonization of an empty island: both curves bend upward, because the best colonists arrive first and the poorest persisters go extinct first; dots: the equilibria S* (about 32 and 14 species). B: recolonization after defaunation: expected numbers (smooth lines) and one stochastic realization of each island (steps); vertical lines: the time t₀.₉ at which 90 % of the equilibrium number is reached, longer for the far island. C: equilibrium on the near island over 200 years: the number of species fluctuates around S* while about 15 species immigrate and as many go extinct per decade (bars)](./plots/mw-heterogeneous.py)

### 34.2.3. The Time to Equilibrium

How fast is equilibrium approached? In the linear model $\dot S = I_0 - (I_0 + E_0)S/P$, so $S(t) = S^*(1 - \mathrm{e}^{-kt})$ with $k = (I_0 + E_0)/P$, and the fraction $1 - \mathrm{e}^{-kt}$ of the equilibrium is reached at a time independent of the starting point.

**Proposition 34.2.3 (Time to 90 % of Equilibrium)** In the linear model, an island starting empty reaches 90 % of $S^*$ at

$$
t_{0.9} = \frac{\ln 10}{k} = 2.30\,\frac{S^*}{\hat T}\left(1 - \frac{S^*}{P}\right) \approx 2.30\,\frac{S^*}{\hat T}\quad\text{if } S^* \ll P, \tag{34.5}
$$
where $\hat T$ is the turnover rate at equilibrium.

**Proof** $1 - \mathrm{e}^{-kt} = 0.9$ gives $t = \ln 10/k$. With $S^* = PI_0/(I_0 + E_0)$ and $\hat T = E_0S^*/P = I_0E_0/(I_0 + E_0)$, we have $S^*/\hat T = P/E_0$ and $1 - S^*/P = E_0/(I_0 + E_0)$; their product is $P/(I_0 + E_0) = 1/k$. $\square$

MacArthur and Wilson derived the approximate form: the time to equilibrium is about twice the number of species at equilibrium divided by the number of species replaced per unit time. The formula gives a check on turnover estimates. Simberloff and Wilson's mangrove islands (Section 34.3.1) returned to their former richness of 20–40 arthropod species within about a year; with $S^* \approx 30$ and $t_{0.9} \approx 1$ year, Eq. (34.5) implies a turnover of the order of 50 or more species per year, far higher than the 1.5 extinctions and immigrations per year estimated from annual censuses. Most turnover is invisible to occasional censuses: species that arrive and die out between two surveys are never recorded, so estimated turnover rates are lower bounds, and much of the real turnover is due to transient, rare species.

### 34.2.4. Area, Isolation, and the Target and Rescue Effects

MacArthur and Wilson proposed that isolation acts mainly on immigration and area mainly on extinction: remote islands receive fewer propagules, and small islands have smaller populations, which go extinct more often (**demographic stochasticity**, [7.19.15](/7.19.15)). Two refinements cross these effects.

**Definition 34.2.1 (Target Effect)** The **target effect** is the increase of the immigration rate with island area, because a larger island intercepts more dispersing propagules (Gilpin and Diamond 1976).

The converse, the reduction of extinction on near islands because immigrants reinforce declining populations, is the **rescue effect** of Brown and Kodric-Brown (1977), defined for metapopulations in [7.19.16](/7.19.16). With both effects, area and isolation each act on both rates, and near, large islands are favored doubly.

The shape of the resulting species–area curve can be derived. Suppose that immigration falls exponentially with distance, $I_0 = i\,\mathrm{e}^{-d/d_0}$, and that the per-species extinction rate falls as a power of area, $E_0 = eA^{-x}$, because mean time to extinction increases with population size ([7.19.15](/7.19.15)). In the linear model

$$
S^*(A, d) = \frac{P}{1 + (e/i)\,A^{-x}\,\mathrm{e}^{d/d_0}}. \tag{34.6}
$$

**Proposition 34.2.4 (Slope of the Equilibrium Species–Area Curve)** Under Eq. (34.6), the local slope of the species–area curve on logarithmic axes is

$$
z = \frac{\partial\ln S^*}{\partial\ln A} = x\left(1 - \frac{S^*}{P}\right).
$$
It decreases with area, is larger for more remote islands at a given area, and tends to $x$ for islands far from saturation ($S^* \ll P$).

**Proof** Write $u = (e/i)A^{-x}\mathrm{e}^{d/d_0}$, so $\ln S^* = \ln P - \ln(1 + u)$ and $\partial u/\partial\ln A = -xu$. Then $\partial\ln S^*/\partial\ln A = xu/(1 + u)$, and $u/(1 + u) = 1 - 1/(1 + u) = 1 - S^*/P$. $S^*$ increases with $A$ and decreases with $d$, which gives the monotonicity. $\square$

The proposition explains two features of Table 1. Island curves are steeper than mainland curves because islands are further from saturation; and isolated archipelagos and habitat islands, which receive few immigrants, have the steepest curves (Figure 1B–C). It also shows that a power law is only an approximation: an equilibrium species–area curve is curved on logarithmic axes. The extreme case is a set of islands that receive no immigrants at all. The mountaintops of the Great Basin of western North America were connected by forest during the last glaciation and have been isolated since; their small mammals cannot cross the intervening desert, so the mountains are losing species without replacement, a process called *faunal relaxation* (Brown 1971), and their species–area slope ($z = 0.43$) reflects extinction alone. In contrast, montane mammals of the American Southwest, where immigration from the Rocky Mountains and the Mogollon Rim is still possible, show a strong negative effect of distance from these sources, indicating that dispersal across the lowlands continues (Lomolino, Brown and Davis 1989).

The effect of isolation depends on the organism. Bird species richness is lower on the remote Azores than on the Channel Islands of the same area near the coast of France, but the richness of ferns, whose light spores are carried by wind, is similar in the two archipelagos (Williamson 1981). Islands within 800 km of New Guinea hold more bird species than islands of the same area more than 3200 km away (MacArthur and Wilson 1963).

## 34.3. Tests of the Theory

### 34.3.1. Defaunation and Area Reduction

Simberloff and Wilson (1969) carried out the most famous experiment in biogeography. They chose small islands of red mangrove (*Rhizophora mangle*) in the Florida Keys, 11–18 m in diameter and 2–1188 m from the nearest large stand of mangrove, censused their arthropods (20–40 insect species and 2–10 spider species per island), covered six of them with tents and fumigated them with methyl bromide, killing all arthropods. Within about 200 days, all islands except the most distant had returned to roughly their former number of species, and the nearest island recovered fastest; the composition, however, was substantially different, and species continued to appear and disappear. Both the return to a characteristic number and the turnover were predicted by the theory.

Simberloff (1976) then reduced the area of eight mangrove islands, 262–1263 m² in area, by cutting away sections with a power saw, leaving the habitat otherwise unchanged; a control island was left intact. Arthropod richness fell on all reduced islands and rose slightly on the control. The island Mud 2, reduced once from 942 to 327 m², fell from 79 to 62 species and then stayed nearly constant, while islands reduced twice lost species after each reduction. Because habitat diversity was not changed, the experiment demonstrated an effect of area per se.

### 34.3.2. New Islands and Long-Term Censuses

The volcano of Krakatau, between Java and Sumatra, exploded in 1883 and buried its remnants under hot ash, sterilizing them. Recolonization from Java and Sumatra, 40 km away, has been followed since: within a few decades the island held about 30 species of resident land birds, a number that then changed little while the list of species continued to change, together with hundreds of plant species. Recolonization was confounded by succession: as the vegetation developed from grassland to forest, the birds of open country were replaced by forest birds, so the "equilibrium" was itself shifting. The volcanic island of Surtsey, which emerged south of Iceland in 1963, was reached within six months by bacteria, fungi, seabirds, a fly and seeds of beach plants; its first vascular plant was found in 1965, and the number of species present has risen ever since, with many temporary extinctions, so that the number present is always lower than the cumulative number that have colonized (Magnússon et al. 2014). Both cases show that islands may be far from equilibrium for a long time.

When the level of Lake Hjälmaren in Sweden was lowered by 1.3 m in 1882–1886, many new islands appeared. Their plants were surveyed repeatedly for a century (Rydin and Borgegård 1988). Of about 700 plant species around the lake, individual islands (65 to more than 25 000 m²) held 0–127; area explained 44–85 % of the variation in richness, isolation only 4–10 % in the early surveys and none later. Small and medium islands still gained more species than they lost, but on large islands immigration and extinction had come into balance between 1928 and 1985, about 30 species being lost and 30 gained on each large island.

Bird censuses test turnover directly. Diamond (1969) compared the birds of the nine California Channel Islands in 1968 with surveys from 1917: the number of species on each island had changed little, but on most islands several species had disappeared and been replaced. In a small oak wood in southern England (Eastern Wood), 44 species bred between 1949 and 1975, 27–36 in any year; immigration decreased significantly with the number of species present, and the lines crossed at about 32 species with about three immigrations and three extinctions per year (Beven 1976). On Skokholm, an island off Wales, 69 years of bird records show that year-to-year turnover is dominated by the rarest species (one or two breeding pairs), whereas common species contribute to turnover only over intervals of a decade or more (McCollin 2017). Williamson (1989) had called the equilibrium theory "true but trivial" because turnover seemed to involve only rare, ecologically unimportant species; the long-term data show that the judgment depends on the time scale.

### 34.3.3. Area or Habitat Diversity?

Several studies have partitioned the variation in richness among islands statistically into components due to area alone, to habitat diversity alone, to their correlated variation, and unexplained. On the Lesser Antilles, habitat diversity was far more important than area for reptiles and amphibians, area was more important for bats, and both mattered for birds and butterflies (Ricklefs and Lovette 1999). For beetles of the Canary Islands, richness followed the number of plant species, a measure of resource diversity, much more closely than island area, especially for herbivores (Becker 1992). The two mechanisms are complementary, and their balance depends on the group: species that need particular habitats or food plants respond to habitat diversity, species limited by population size respond to area.

### 34.3.4. Which Species? Disharmony, Incidence and Evolution

The equilibrium theory predicts the number of species but treats them as interchangeable. Island biotas are *disharmonic*: their composition differs from that of the mainland, because good dispersers (ferns, birds, bats, small insects) are overrepresented on remote islands, because species that need large areas or depend on other species (large predators, specialist parasites and mutualists) are underrepresented, and because the environments of islands filter colonists. Galápagos plants, for example, are predicted better by the similarity of their climatic niche to the conditions of the islands than by their dispersal mode (Carvajal-Endara et al. 2017). Diamond (1975) described the islands occupied by each bird species of the Bismarck Archipelago by *incidence functions*, the proportion of islands in each class of richness or area that the species occupies; "supertramps" occurred only on small, species-poor islands (good colonists, poor competitors), "high-S" species only on large, rich islands.

On remote islands and for poor dispersers, speciation in place adds species faster than immigration (the third term of the balance discussed in [7.10.30](/7.10.30)); the proportion of **endemic species** on Norfolk Island is highest in the groups with the poorest dispersal (Holloway 1977). The *general dynamic model* of oceanic island biogeography (Whittaker et al. 2008) adds the geological life cycle of volcanic islands: they emerge, grow, then erode and subside, and the rate of speciation peaks at an intermediate island age, when niche space is large and still unfilled by immigrants. Reconstructions for 14 endemic radiations of the Hawaiian Islands, including silverswords, lobeliads, honeycreepers and picture-winged *Drosophila*, show species accumulation that first accelerated and then declined on the older islands (Lim and Marshall 2017).

## 34.4. Islands, Metapopulations and Landscapes

Habitat fragments in a human-modified landscape are islands, and the theory has been used to predict the consequences of **habitat fragmentation**. Two differences from oceanic islands matter. The "sea" between fragments, the landscape matrix, is not uninhabitable: some species live in it, and others cross it more or less easily ([7.19.48](/7.19.48)). And fragments are usually recent, so their biotas are not at equilibrium: a newly isolated fragment holds more species than it can support and loses the excess over decades, an **extinction debt** ([7.19.16](/7.19.16)). Eq. (34.5) gives an order of magnitude for the relaxation time: for a fragment of tropical forest that held 100 bird species and loses one species every few years, the time to lose most of the excess is decades to a century.

At the scale of single species, a set of fragments connected by dispersal is a **metapopulation** ([7.19.16](/7.19.16)), and the equilibrium theory is its community-level counterpart: the Levins model describes the fraction of patches occupied by one species, the island model the fraction of species occupying one patch. Proposition 34.2.2 makes the link explicit, since each species on an island is a two-state chain with colonization and extinction rates, just as each patch is in a metapopulation. Landscape features that increase dispersal, such as green corridors around cities, increase both. The green belt around the central districts of Beijing, for example, can be treated as a network of woodland islands in a matrix of built-up land, whose value for wildlife depends on the size and connection of its patches.

Land-bridge islands created by reservoirs are natural experiments in fragmentation. The Thousand Island Lake (Qiandao Lake) in Zhejiang Province, created by a dam in 1959, contains more than a thousand islands that were hilltops of a continuous forest; they have been studied for birds, lizards, small mammals and plants and show strong effects of island area on richness. In the Zhoushan Archipelago off Zhejiang, analyses of breeding birds found that land use on the islands (urban and agricultural land) altered the island biogeographic pattern of bird community assembly expected from area and isolation alone: human land use acts as a further factor besides area and isolation.

## 34.5. Conservation: Reserve Design and Connectivity

### 34.5.1. SLOSS

Nature reserves are islands in a sea of unprotected land. Diamond (1975) derived from island biogeography a set of rules for reserve design: a large reserve is better than a small one; one large reserve is better than several small ones of the same total area; reserves close to one another are better than distant ones; reserves should be grouped compactly rather than in a line; reserves connected by corridors are better than unconnected ones; round reserves are better than elongated ones. The second rule provoked the *SLOSS* debate (single large or several small; Simberloff and Abele 1976).

The species–area relationship by itself does not decide the question. If the small reserves contain the same subset of species, as in a homogeneous region, the single large reserve, which contains more of the regional pool, is better. If the region is heterogeneous, so that different small reserves contain different species (high **beta diversity**), several small reserves may together contain more species. The structure of the biota matters, and it can be analyzed by its **nestedness** (Definition 29.5.1 of [7.19.29](/7.19.29)): a set of sites is perfectly nested if the species of each poorer site are a subset of those of each richer site (Patterson and Atmar 1986).

**Proposition 34.5.1 (Nested Biotas Favor a Single Large Reserve)** If the biotas of a set of sites are perfectly nested and richness increases with area, the union of the species of any collection of sites equals the species list of its richest member. In particular, a single site of area at least as large as that of every site in the collection protects at least as many species as the whole collection.

**Proof** In a perfectly nested set, the species lists are totally ordered by inclusion, so the union of any subcollection is the largest list in it. If richness increases with area and nesting follows richness, a site larger than every member of the collection has a list that contains the list of the richest member, hence the union. $\square$

Real biotas are rarely perfectly nested, and the outcome depends on the area that species need. In the model of Figure 3, species have ranges along a region and require a minimum stretch of habitat within a single reserve; splitting a fixed total area into more pieces samples more of the region but shortens each piece. When requirements are small, several small reserves protect three times as many species as one large reserve; when typical requirements approach the size of a small reserve, the single large reserve wins.

![SLOSS in a model community: 300 species with ranges of lognormal length along a region of length 1; a species is protected if one reserve contains a stretch of its range at least as long as its area requirement. Total reserve length 0.1, divided into k equal, evenly spaced pieces. A: protected species against k for three levels of the median area requirement (mean of 200 communities, bands: central 90 %): with no area requirement, more and smaller reserves always protect more species; with moderate requirements richness peaks at intermediate k; with large requirements a single or few large reserves are best. B: single large (k = 1) and several small (k = 8) reserves against the median area requirement: the two curves cross where requirements approach the length of one small reserve (dashed). C: 60 of the ranges of one community and the two configurations](./plots/sloss.py)

Empirically, collections of small islands and small reserves usually contain more species than one large area of the same total size: mammals and birds in East African parks, mammals and lizards in Australian reserves and large mammals in national parks of the USA (Quinn and Harrison 1988), plants of spruce mires in Finland (Virolainen et al. 1998). But these counts include species of open and edge habitats that thrive in small fragments, whereas the species of greatest conservation concern, large-bodied, wide-ranging or interior species, often need large areas: species richness is not the only criterion. The practical consensus is that the question is posed too narrowly. Habitat quality, total area and connectivity all matter (Hodgson et al. 2009), large reserves are irreplaceable for area-demanding species, and small reserves add complementary species and safeguard against catastrophes that might destroy a single reserve. The persistence of particular species is assessed by **population viability analysis** ([7.19.15](/7.19.15)). For the Amur tiger in northeastern China, for example, such models compared disease control (canine distemper), habitat connection between the large population in Russia and the small one in China, and habitat expansion, and found that connection and expansion were needed for the small population to persist with its genetic diversity (Wang et al. 2023).

### 34.5.2. Corridors and Wildlife Crossings

A **corridor** in the sense of landscape ecology ([7.19.48](/7.19.48)) is a strip of habitat that connects otherwise isolated patches. Corridors increase immigration among fragments, raising equilibrium richness (Section 34.2.4) and reducing extinction through the rescue effect; they also allow movements that animals need over their life cycle and range shifts under climate change. Potential costs, the spread of fire, disease or invasive species along corridors and the correlation of catastrophes among connected fragments, are real but generally judged smaller than the benefits. Corridors need not be continuous strips; stepping stones and a permeable landscape matrix serve the same function for many species.

Roads are among the strongest barriers. Wildlife crossings, overpasses (green bridges), underpasses, culverts adapted with ledges and canopy bridges for arboreal animals, restore movement across them. In the Qinling Mountains of Shaanxi, part of National Road 108 was moved into a tunnel and the old road through the forest was closed and restored; giant panda signs were subsequently found throughout the core of the restored corridor, which reconnected panda populations on the two sides of the road. Connectivity analyses guide where such measures are placed: species distribution models of habitat suitability and least-cost paths have been used to identify corridors for Asian elephants in Yunnan, for the North China leopard (*Panthera pardus japonensis*) among core habitat patches in the mountains of northern China (Wang et al. 2024), and for spotted seals (*Phoca largha*) in the Bohai and Yellow Seas, whose migration corridors are interrupted by shipping lanes and aquaculture areas. The methods, resistance surfaces, least-cost paths, circuit theory and species distribution models, are developed in [7.19.49](/7.19.49).

## Summary

| Topic | Key results | Section |
|---|---|---|
| Species–area pattern | $S = cA^z$ (Eq. (34.1)); $z \approx 0.1$–0.2 for mainland samples, 0.2–0.35 for islands, up to 0.4–0.7 for isolated habitat islands; fit by regression on logarithms, compare forms by AIC | 34.1.1 |
| Explanations | Sampling: random placement gives $\mathbb{E}[S] = \sum[1 - (1 - a)^{n_i}]$, slope falling from 1 to 0 (Proposition 34.1.1); habitat diversity; area per se | 34.1.2 |
| Equilibrium theory | Unique, globally stable $S^*$ with turnover $\hat T = I(S^*) = E(S^*)$ (Proposition 34.2.1); independent species: $\mathbb{E}[S^*] = \sum\lambda_i/(\lambda_i + \mu_i)$, variance below the mean, concave rate curves (Proposition 34.2.2) | 34.2.1–34.2.2 |
| Time scale | $t_{0.9} = 2.30\,(S^*/\hat T)(1 - S^*/P)$ (Proposition 34.2.3); census-based turnover underestimates true turnover | 34.2.3 |
| Area and isolation | Target effect (Definition 34.2.1) and rescue effect; $z = x(1 - S^*/P)$: isolation steepens the curve (Proposition 34.2.4); faunal relaxation on isolated mountaintops | 34.2.4 |
| Tests | Mangrove defaunation and area reduction; Krakatau, Surtsey, Lake Hjälmaren; turnover in Channel Islands, Eastern Wood, Skokholm; area vs habitat diversity; disharmony, incidence functions, speciation and the general dynamic model | 34.3 |
| Conservation | Fragments as islands with extinction debt; nested biotas favor SL (Proposition 34.5.1); SS often richer, but area-demanding species need large reserves; corridors and wildlife crossings (G108 tunnel, leopard, elephant and seal corridors) | 34.4–34.5 |

## Questions

1. A forest that held 400 species of beetles is reduced to 10 % of its original area. Using $S = cA^z$ with $z = 0.25$, how many species are expected to persist eventually? Why is the loss not immediate, and why might the actual loss be larger or smaller than this estimate?

   **Answer** $S_{\mathrm{new}}/S_{\mathrm{old}} = 0.1^{0.25} = 0.56$, so about 225 species persist and about 175 are eventually lost. The loss takes time: populations in the remaining fragment decline to their new carrying capacity and go extinct one by one (an extinction debt, with a relaxation time of the order of $S^*/\hat T$, Eq. (34.5)). The estimate may be too high if the remnant is fragmented, isolated or degraded by edge effects, if endemic species with small ranges lived mainly in the cleared part, or if the mainland $z$ underestimates the effect of isolation (an isolated fragment behaves as an island with a larger $z$). It may be too low if many species can live in the modified matrix or if the remaining area holds most of the habitat types.

2. In the linear model with $P = 100$, $I_0 = 5$ and $E_0 = 20$ species per year, compute $S^*$, the turnover rate and $t_{0.9}$. How do they change if the island is moved closer to the mainland so that $I_0 = 20$?

   **Answer** $S^* = 100\cdot5/25 = 20$, $\hat T = I_0E_0/(I_0 + E_0) = 100/25 = 4$ species per year, $k = 25/100 = 0.25$ per year, $t_{0.9} = 2.30/0.25 = 9.2$ years (check: $2.30\cdot(20/4)(1 - 0.2) = 9.2$). With $I_0 = 20$: $S^* = 100\cdot20/40 = 50$, $\hat T = 400/40 = 10$ per year, $k = 0.4$, $t_{0.9} = 5.8$ years. The near island holds more species, has a higher turnover and approaches equilibrium faster.

3. Why is the variance of the number of species on replicate islands predicted to be smaller than the mean in Proposition 34.2.2? What would a variance larger than the mean suggest?

   **Answer** $S$ is a sum of independent Bernoulli variables with variances $p_i(1 - p_i) < p_i$, so its variance is less than its mean; species that are almost always present ($p_i \approx 1$) contribute almost nothing to the variance. A variance larger than the mean indicates positive covariance among species, for example because islands differ in habitat or area (so that all species are more likely on some islands than on others), because species facilitate one another (a specialist can only colonize after its host), or because catastrophes remove many species at once. Negative covariance, for example from competition, would reduce the variance further.

4. Show that in the linear model the slope $z$ of the equilibrium species–area curve cannot exceed the exponent $x$ in $E_0 \propto A^{-x}$. What does a very high observed $z$ (such as 0.72 for cave invertebrates) suggest?

   **Answer** By Proposition 34.2.4, $z = x(1 - S^*/P) < x$ since $S^* > 0$. If immigration also increases with area (the target effect, $I_0 \propto A^{y}$), the same calculation gives $z = (x + y)(1 - S^*/P)$, so a steep slope requires strong effects of area on both rates and islands far from saturation. A $z$ of 0.72 suggests very isolated habitat islands in which small caves are far from saturated, very strong area dependence of extinction or colonization, or a habitat-diversity effect (large caves contain more microhabitats). It may also reflect sampling: small caves are surveyed less completely.

5. A conservation agency can buy either one forest block of 1000 ha or five blocks of 200 ha spread over a mountain range. What information would you need to advise it?

   **Answer** (1) Whether the biota is nested: survey existing fragments and compute a nestedness index; if poor sites hold subsets of rich ones, the large block is better (Proposition 34.5.1). (2) Beta diversity along the range: if the five blocks span different elevations, soils or climates, they will hold complementary species. (3) The area requirements of the target species: home ranges and minimum viable populations of large or interior species (population viability analysis), and their sensitivity to edges. (4) The matrix and connectivity: whether animals can move among the five blocks, which allows rescue effects, or whether corridors can be added. (5) Risks: a single block may be destroyed by one fire or epidemic. (6) Costs of management, edges and enforcement. Often the best answer is a combination: a large core with smaller satellite reserves connected by corridors.
