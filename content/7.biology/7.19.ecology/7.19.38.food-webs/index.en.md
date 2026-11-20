---
title: "Food Webs: Structure, Complexity and Stability"
description: "Food chains (grazing, detrital and parasitic) and food webs; basal, intermediate and top species, link density and connectance; fractional trophic levels from a linear system; the cascade and niche models of food-web structure; food-chain length and the energetic, productive-space, ecosystem-size, dynamic-stability and design hypotheses; resistance, resilience, persistence, variability and robustness; May's random community matrices, the circular law and the criterion σ√(SC) < 1; the elliptic law and the Allesina–Tang result for predator–prey, competitive and mutualistic structure; weak interactions, trophic loops and compartments; diversity and stability: mean–variance scaling, the portfolio effect, synchrony and the insurance hypothesis, Tilman's grasslands; secondary extinctions and robustness."
---

Every species of a community eats or is eaten by others, and the network of who eats whom, the food web, carries the energy and matter of the ecosystem ([7.19.42](/7.19.42)–[7.19.46](/7.19.46)) and transmits the effects of one species to others. The pairwise interactions of [7.19.24](/7.19.24)–[7.19.28](/7.19.28) are its links. This chapter describes food webs and asks what their structure implies for the persistence of communities. Section 38.1 defines food chains, food webs and trophic levels, and introduces quantitative descriptors and two structural models. Section 38.2 asks why food chains are short. Section 38.3 distinguishes the several meanings of stability. Section 38.4 develops May's theory of random community matrices, which overturned the belief that complex communities must be stable, and its refinement by Allesina and Tang; the mathematics is that of eigenvalues of large random matrices, built on the [community matrix](/7.19.22#sec-22.5.1) of [7.19.22](/7.19.22) and the **eigenvalues** of [2.1.6](/2.1.6). Section 38.5 explains why the same complexity that destabilizes populations can stabilize aggregate properties of communities, and Section 38.6 treats the robustness of webs to species loss. The indirect effects that propagate through food webs, trophic cascades and apparent competition, are the subject of [7.19.39](/7.19.39). The tools of network science used here (degree distributions, robustness to node removal) are developed in [1.4.7](/1.4.7) and, for molecular networks, [7.9.12](/7.9.12).

## 38.1. Food Chains, Food Webs and Trophic Levels

### 38.1.1. Food Chains

**Definition 38.1.1 (Food Chain)** A **food chain** is a sequence of species, each feeding on the preceding one, along which the energy and matter fixed by producers pass through a series of consumers: plant → herbivore → carnivore → top carnivore. Its *length* is the number of feeding links.

Ecosystems contain three kinds of food chains.

| Type | Begins with | Example |
|---|---|---|
| Grazing food chain | living plants eaten by herbivores | grass → grasshopper → frog → snake → hawk; phytoplankton → krill → baleen whale |
| Detrital food chain | dead organic matter (litter, carcasses, feces) and its decomposers | leaf litter → fungi and bacteria → springtails and mites → predatory mites → spiders |
| Parasitic food chain | a host and its parasites, which are smaller than their hosts | mammal → flea → bacterium carried by the flea (such as *Yersinia pestis*) → bacteriophage |

The two main channels are linked: most primary production of forests, grasslands and wetlands is not eaten alive but enters the detrital chain, and detritivores are eaten by the same predators that eat herbivores (Section 38.2 and [7.19.39](/7.19.39)). Odum described the two layers of an ecosystem as an upper "green belt" where autotrophic production dominates and a lower "brown belt" of soils and sediments where decomposition dominates; the detrital chain is treated in [7.19.44](/7.19.44). Food chains are abstractions. Many consumers change their diet with age, season and prey availability (a tadpole grazes algae, the adult frog eats insects), so a chain is often temporary, and the relationships of the abundant, central species of a community are the most constant.

### 38.1.2. Food Webs

**Definition 38.1.2 (Food Web)** A **food web** is the network of feeding relationships among the species (or groups of species) of a community: a directed graph whose nodes are species and whose links run from each resource to each of its consumers.

Food chains interlock into webs because most consumers eat several kinds of food and most species are eaten by several consumers. In the Southern Ocean, diatoms and other phytoplankton are eaten by Antarctic krill (*Euphausia superba*), copepods and salps; krill is eaten by baleen whales, crabeater seals, penguins, flying seabirds, squid and fishes; fishes and squid are eaten by leopard seals, Weddell seals, emperor penguins and toothed whales; and killer whales eat seals, penguins and other whales. A web of this kind is dominated by one species at the second level: krill links almost all consumers to the phytoplankton, and a decline of krill would propagate to almost every predator. The first food web drawn as a diagram, of Bear Island in the Arctic (Summerhayes and Elton 1923), already showed that even a community poor in species has complex feeding relations.

A food web with $S$ species and $L$ links is described by a few quantities.

- *Basal species* have no prey (producers, or detritus treated as a node); *top species* have no predators; *intermediate species* have both.
- *Link density* $L/S$ is the mean number of links per species; each link counts for one consumer and one resource, so the mean number of prey and the mean number of predators both equal $L/S$.
- *Omnivory*: feeding on more than one trophic level (Section 38.1.3).
- *Generality* and *vulnerability*: the number of prey and of predators of a species, whose distributions in real webs are skewed: a few species eat or are eaten by many.

**Definition 38.1.3 (Connectance)** The **connectance** of a food web is the fraction of possible feeding links that are realized, $C = L/S^2$ (directed connectance, counting all ordered pairs including cannibalism); some authors use $L/[S(S - 1)/2]$, the fraction of pairs of species that interact.

In compilations of well-resolved webs, connectance lies between about 0.03 and 0.3 and is roughly independent of the number of species, so that link density increases about in proportion to $S$ (Martinez 1992; Dunne et al. 2002). Early compilations had suggested a constant link density of about 2 ("link–species scaling"), but this turned out to be an artifact of the poor resolution of the early webs, in which species were lumped into large groups. All food-web statistics depend on taxonomic resolution, which is why well-resolved webs, such as those of Little Rock Lake (182 taxa), the Ythan estuary or Caribbean reefs, are the basis of modern analyses.

### 38.1.3. Trophic Levels

**Definition 38.1.4 (Trophic Level)** A **trophic level** is a position in the sequence of feeding steps from the producers: producers (autotrophs) form the first trophic level, herbivores (primary consumers) the second, carnivores that eat herbivores (secondary consumers) the third, and so on. In a food web the trophic level of a consumer is defined quantitatively as one plus the mean trophic level of its food, weighted by the fraction of its diet each food makes up.

The trophic level as a class ("all herbivores") is a concept of energy flow (Lindeman 1942): it groups organisms by the number of conversions their food has undergone since photosynthesis, and the transfer of energy between levels is the subject of [7.19.43](/7.19.43). The classes do not refer to species: a species belongs to as many levels as it has feeding links of different lengths to the producers, and omnivores are common. The quantitative definition assigns every species a single, generally fractional, value.

**Proposition 38.1.1 (Fractional Trophic Levels)** Let a web have $S$ species, let $q_{ij} \ge 0$ be the fraction of the diet of species $i$ provided by species $j$ ($\sum_j q_{ij} = 1$ for consumers, $q_{ij} = 0$ for all $j$ if $i$ is basal), and $Q = (q_{ij})$. The trophic levels $\boldsymbol{t} = (t_1, \dots, t_S)^{\mathsf T}$, defined by $t_i = 1 + \sum_j q_{ij}t_j$, are the unique solution of

$$
(I - Q)\,\boldsymbol{t} = \boldsymbol{1}, \tag{38.1}
$$
provided that every species is connected to some basal species by a chain of feeding links. Then $\boldsymbol{t} = (I + Q + Q^2 + \cdots)\boldsymbol{1}$, and $t_i - 1$ is the mean number of links in a chain from species $i$ down to the producers, when each step down is chosen with the diet fractions as probabilities.

**Proof** $Q$ is the transition matrix of a random walk that moves from a species to one of its foods with probabilities $q_{ij}$ and stops at a basal species (whose row is zero). If every species connects to a basal species, the walk stops with probability one, so $Q^k \to O$, the spectral radius of $Q$ is less than 1, and the Neumann series $\sum_k Q^k$ converges to $(I - Q)^{-1}$ ([2.1.11](/2.1.11)). Hence (38.1) has the unique solution $\boldsymbol{t} = \sum_k Q^k\boldsymbol{1}$. The $i$-th component of $Q^k\boldsymbol{1}$ is the probability that the walk from $i$ has not yet stopped after $k$ steps, and $\sum_{k\ge0}\mathbb{P}(\text{not stopped after }k) = \mathbb{E}[\text{number of steps}] + 1$. $\square$

**Example 38.1.1** In a small grassland web, grasshoppers eat only grass; a mouse eats grass (50 % of its diet) and grasshoppers (50 %); a snake eats only mice; a hawk eats mice (70 %) and snakes (30 %). The trophic levels follow in order:

| Species | Diet | Trophic level |
|---|---|---|
| Grass | — | $1$ |
| Grasshopper | grass | $1 + 1 = 2$ |
| Mouse | grass 0.5, grasshopper 0.5 | $1 + 0.5 \cdot 1 + 0.5 \cdot 2 = 2.5$ |
| Snake | mouse | $1 + 2.5 = 3.5$ |
| Hawk | mouse 0.7, snake 0.3 | $1 + 0.7 \cdot 2.5 + 0.3 \cdot 3.5 = 3.8$ |

Here the web has no loops, and the species can be solved one at a time; with loops (cannibalism, mutual predation of larvae) the linear system must be solved simultaneously. Without diet data, each prey is often given equal weight ("prey-averaged" trophic level). Trophic levels measured with stable nitrogen isotopes, in which $\delta^{15}\mathrm{N}$ rises by about 3.4 ‰ per trophic step, integrate diet over time and are the standard field method (Post 2002).

:::

### 38.1.4. Models of Food-Web Structure

Are the regularities of real webs (the proportions of basal, intermediate and top species, connectance, chain lengths, the frequency of omnivory) consequences of simple rules? Two stochastic models generate webs with prescribed $S$ and $C$.

- *The cascade model* (Cohen and Newman 1985): species are ranked $1, \dots, S$, and each species $i$ eats each lower-ranked species $j < i$ independently with probability $p = 2CS/(S - 1)$. The ranking forbids loops: there is a hierarchy in which every species eats only those below it. The model reproduces the proportions of basal, intermediate and top species of the early webs, but underestimates the frequency of species with similar diets and of omnivory.
- *The niche model* (Williams and Martinez 2000): each species $i$ receives a niche value $n_i$ uniform on $[0, 1]$ (think of body size), a feeding range of width $r_i = xn_i$ with $x$ drawn from a Beta$(1, \beta)$ distribution, $\beta = 1/(2C) - 1$ (so that $\mathbb{E}[x] = 2C$ and the expected connectance is $C$), and a range center $c_i$ uniform on $[r_i/2, n_i]$. Species $i$ eats all species whose niche values lie in $[c_i - r_i/2, c_i + r_i/2]$.

The niche model adds two features: diets are contiguous intervals on one niche axis (Figure 1B), so that species with similar niche values share predators and prey, and a consumer can eat species with slightly larger niche values than its own, permitting loops and cannibalism. Fed only $S$ and $C$, it predicts a dozen properties of the best-resolved webs, the fractions of top, intermediate and basal species, the variability of generality and vulnerability, the mean chain length, the frequency of omnivory and cannibalism, better than the cascade model. That webs are almost "interval" (diets can be ordered along a single dimension) is one of the strongest regularities of food-web structure, and it has an evident biological basis in body size: predators eat prey within a range of sizes related to their own (Cohen et al. 2003).

![A food web generated by the niche model, with 30 species and target connectance 0.12 (realized L = 113 links, C = L/S² = 0.126). A: species placed by niche value and prey-averaged trophic level, from Eq. (38.1); lines join prey to consumer; basal species (green) and intermediate species (blue); in this realization every consumer is itself eaten by another, because species with high niche values eat each other. B: the feeding matrix with consumers as rows and resources as columns, both ordered by niche value; each diet is an interval of the niche axis](./plots/niche-model-web.py)

## 38.2. Food-Chain Length

Almost all food webs have between two and five trophic levels, most three or four; the mean chain length of an exposed rocky shore web in Washington State (Briand 1983) is about 2.3 links, of most lake webs between 3 and 4.5. Why so few? Five hypotheses have been proposed.

1. *Energetics* (Elton 1927; Lindeman 1942). Only about a tenth of the energy of one level reaches the next ([7.19.43](/7.19.43)), so a viable population of a fifth-level predator needs a very large production at the base. Food chains should be longer where productivity per unit area is higher.
2. *Productive space* (Schoener 1989). The relevant quantity is total productivity, productivity per unit area times the area of the ecosystem, because a top predator needs a minimum total supply, not a minimum density.
3. *Ecosystem size.* Larger ecosystems hold more species and more habitats, allow top predators to persist as larger populations and include refuges; Post, Pace and Hairston (2000) found that in 25 lakes of northeastern North America food-chain length, measured by $\delta^{15}\mathrm{N}$ of the top predators, increased with lake volume and not with productivity.
4. *Dynamic stability* (Pimm and Lawton 1977). In Lotka–Volterra models, longer chains return more slowly to equilibrium after a perturbation: they are less resilient (Section 38.3), and would be eliminated in frequently disturbed environments. Later models with more realistic functional responses did not always confirm this.
5. *Design constraints and foraging.* Predators are usually larger than their prey, and body size increases up the chain; a predator able to catch and kill an eagle would have to be both fast and very large. An adaptive forager should, moreover, prefer abundant, poorly defended prey low in the chain: in models where consumers switch to the most profitable prey, chains are shorter and do not lengthen with productivity (Kondoh and Ninomiya 2009).

Experiments with very simple systems support the energetic hypothesis at very low productivity: in artificial water-filled tree holes, a hundredfold reduction of leaf-litter input removed the top predator, a chironomid midge (Jenkins et al. 1992). In natural systems, a meta-analysis of comparisons among similar habitats found that chain length increases with ecosystem size and, less consistently, with productivity, and is unrelated to disturbance, as expected under the productive-space and ecosystem-size hypotheses (Takimoto and Post 2013). On Bahamian islands, food-chain length increased with island area, and storms replaced the top predator (a lizard) by another (an orb spider) without shortening the chain (Takimoto et al. 2008). Including parasites, which are usually omitted, lengthens chains and changes their structure ([7.19.28](/7.19.28)).

## 38.3. Concepts of Stability

"Stability" has many meanings, and the answer to "are complex communities more stable?" depends on which is meant. Disturbances themselves are of two kinds: a *pulse*, a single event that displaces the community (a fire, a flood), and a *press*, a sustained change of conditions (eutrophication, warming).

**Definition 38.3.1 (Resistance and Resilience)** The **resistance** of a community or ecosystem is its ability to remain unchanged when disturbed, measured inversely by the size of the displacement that a given disturbance causes. Its **resilience** is the speed with which it returns to its former state after being displaced; near a stable equilibrium it is measured by the asymptotic return rate, the magnitude of the real part of the dominant eigenvalue of the Jacobian, $-\max_k\operatorname{Re}\lambda_k$, whose inverse is the *return time*.

Other properties are distinguished from these:

| Property | Meaning | Typical measure |
|---|---|---|
| Local stability | return after small perturbations | all eigenvalues of the Jacobian with $\operatorname{Re}\lambda < 0$ |
| Global stability | return after perturbations of any size | Lyapunov function; size of the basin of attraction |
| Persistence | how long a system lasts before it changes (e.g. loses a species) | time to first extinction, fraction of species surviving |
| Variability (inverse of constancy) | magnitude of fluctuations through time | coefficient of variation of abundance or biomass |
| Robustness | resistance of a web to secondary extinctions after species loss | fraction of species that must be removed to lose half (Section 38.6) |

Holling (1973) used "resilience" differently, for the size of the disturbance a system can absorb before shifting to another stable state, and that *ecological resilience* is the concept relevant to regime shifts ([7.19.39](/7.19.39)); the definition above is Pimm's (1984) *engineering resilience*. The two can be opposed: a system may return quickly from small disturbances and yet lie close to a threshold.

Resistance and resilience are often inversely related (Odum). A redwood forest resists fire with thick bark and tall crowns but, once burned, takes centuries to recover; chaparral burns easily but regrows from resprouting shrubs and seeds within a few years. Ecosystems in benign, constant environments tend to be resistant, those in variable environments resilient. Models of nutrient and energy flow show that resilience increases with the flux of energy per unit of standing biomass (DeAngelis 1980): systems dominated by small, fast-turnover organisms recover fast. O'Neill (1976) compared the response of models of a pond, a tundra and a forest to the same perturbation: the pond, whose phytoplankton turn over in days and whose heterotroph biomass exceeds that of autotrophs (ratio about 5.4), recovered fastest; the tundra, with very little heterotroph biomass relative to plants (ratio about 0.004) and slow plant growth, slowest.

## 38.4. Complexity and Stability

### 38.4.1. From Elton to May

Until about 1970 the conventional view, expressed by MacArthur (1955) and Elton (1958), was that more complex communities are more stable: a consumer with many prey can switch when one declines, a web with many paths can reroute energy, and simple communities such as crops, islands and the Arctic tundra seem prone to outbreaks and invasions. May (1972, 1973) tested the claim with a model and found the opposite.

Consider a community of $S$ species at an equilibrium and its community matrix ([7.19.22](/7.19.22)), the Jacobian $A = (a_{ij})$ of the population dynamics at the equilibrium, where $a_{ij}$ is the effect of a small change in species $j$ on the growth of species $i$. May assumed that each species regulates itself, $a_{ii} = -d$ (with time scaled so that $d = 1$), and that the off-diagonal entries are random: with probability $C$ (the connectance) $a_{ij}$ is drawn from a distribution with mean 0 and standard deviation $\sigma$ (the interaction strength), and otherwise $a_{ij} = 0$. Then $A = -dI + M$, where $M$ has independent entries with mean 0 and variance $C\sigma^2$, and the equilibrium is locally stable if and only if all eigenvalues of $M$ have real part less than $d$.

### 38.4.2. The Circular Law and May's Criterion

**Theorem 38.4.1 (Circular Law)** Let $X_S$ be an $S \times S$ matrix whose entries are independent, identically distributed random variables with mean 0 and variance 1. As $S \to \infty$, the eigenvalues of $X_S/\sqrt S$ become uniformly distributed on the unit disk $\{\lvert z\rvert \le 1\}$ of the complex plane (Girko 1984; Bai 1997; Tao and Vu 2010). If the entries also have a finite fourth moment, the largest modulus of an eigenvalue of $X_S/\sqrt S$ converges to 1 almost surely (Geman 1986; Bai and Yin 1986).

The theorem is deep, and its proof (by "hermitization", relating the eigenvalue distribution to the singular values of $X_S - zI$) is beyond our scope. A heuristic makes the radius plausible: for any fixed unit vector $\boldsymbol{u}$, $\mathbb{E}\lVert X_S\boldsymbol{u}\rVert^2 = \sum_{i}\sum_j u_j^2\operatorname{Var}(x_{ij}) = S$, so $X_S/\sqrt S$ stretches a typical vector by a factor 1, and eigenvectors are typical vectors.

**Proposition 38.4.1 (May's Stability Criterion)** For May's random community matrix $A = -dI + M$, with connectance $C$ and interaction strength $\sigma$, as $S \to \infty$ the eigenvalues of $A$ fill the disk of radius $\sigma\sqrt{SC}$ centered at $-d$, and the equilibrium is stable with probability tending to 1 if

$$
\sigma\sqrt{SC} < d \tag{38.2}
$$
and unstable with probability tending to 1 if $\sigma\sqrt{SC} > d$.

**Proof** The entries of $M$ are independent with mean 0 and variance $C\sigma^2$ (a value from the interaction distribution with probability $C$, zero otherwise), so $M = \sigma\sqrt C\,X_S$ with $X_S$ as in Theorem 38.4.1 (the zero diagonal does not change the limit), and $M = \sigma\sqrt{SC}\,(X_S/\sqrt S)$. By the theorem the eigenvalues of $M$ fill the disk of radius $\sigma\sqrt{SC}$, and the largest real part of an eigenvalue of $M$, which lies between $-\sigma\sqrt{SC}$ and the largest modulus, converges to $\sigma\sqrt{SC}$ because the disk is filled uniformly up to its edge. The eigenvalues of $A = -dI + M$ are those of $M$ shifted by $-d$, so the largest real part of an eigenvalue of $A$ tends to $\sigma\sqrt{SC} - d$, which is negative under (38.2) and positive in the opposite case. $\square$

May's result is that, in a random community, each of the three components of complexity, the number of species $S$, the connectance $C$ and the interaction strength $\sigma$, decreases the probability of stability, and that the transition becomes abrupt for large $S$ (Figure 2B): a large random community is almost surely stable just below the threshold and almost surely unstable just above it. It follows that if real communities are large and stable, their connectance and interaction strengths must satisfy $\sigma^2SC < d^2$: complexity has to be "paid for" by weaker or fewer interactions per species, and the near-constancy of $C$ with $S$ suggests that $\sigma$ declines with richness. Note that $\sigma$ is the root-mean-square strength of the non-zero interactions (their standard deviation, the mean being zero), not their average magnitude.

May's conclusion did not show that complex communities are unstable; it showed that complexity does not by itself confer stability, and that stable complex communities must have special, non-random structure. Much of food-web theory since 1972 has been a search for that structure.

![May's complexity–stability criterion. A: eigenvalues of one random community matrix A = −I + M with S = 250 species, connectance C = 0.2 and σ√(SC) = 0.8: they fill a disk of radius σ√(SC) centered at −1 (red), entirely in the left half-plane, so the equilibrium is stable (circular law, Theorem 38.4.1). B: fraction of random matrices (C = 0.3) that are stable against the complexity σ√(SC), for S = 10, 40 and 150 species: the transition sharpens around σ√(SC) = 1 (dashed) as S increases (Proposition 38.4.1)](./plots/may-stability.py)

### 38.4.3. Interaction Types and the Elliptic Law

Real interactions are not independent in sign. A predator benefits from its prey ($a_{ij} > 0$) while harming it ($a_{ji} < 0$); competitors harm each other; mutualists benefit each other. These constraints correlate the pairs $(a_{ij}, a_{ji})$, and the circular law generalizes.

**Theorem 38.4.2 (Elliptic Law)** Let the pairs $(x_{ij}, x_{ji})$, $i < j$, of an $S \times S$ matrix $X_S$ be independent and identically distributed, with means 0, variances 1 and correlation $\rho = \mathbb{E}[x_{ij}x_{ji}]$. As $S \to \infty$ the eigenvalues of $X_S/\sqrt S$ become uniformly distributed in the ellipse with horizontal semi-axis $1 + \rho$ and vertical semi-axis $1 - \rho$ (Sommers et al. 1988; Nguyen and O'Rourke 2015).

For $\rho = 0$ this is the circular law; for $\rho = 1$ (symmetric matrices) the ellipse degenerates to the segment $[-2, 2]$ of the real axis, Wigner's semicircle law; for $\rho = -1$ (antisymmetric matrices) to the segment $[-2\mathrm{i}, 2\mathrm{i}]$ of the imaginary axis.

**Proposition 38.4.2 (Allesina–Tang Criteria)** Let each pair of species interact with probability $C$, with interaction magnitudes $\lvert X\rvert$ for $X \sim \mathcal{N}(0, \sigma^2)$ drawn independently for the two entries, and self-regulation $-d$. Then, as $S \to \infty$, the equilibrium is stable if

| Interaction structure | Signs of $(a_{ij}, a_{ji})$ | Correlation $\rho$ | Stability condition |
|---|---|---|---|
| Random (May) | independent | $0$ | $\sigma\sqrt{SC} < d$ |
| Predator–prey | $(+, -)$ or $(-, +)$ | $-2/\pi$ | $\sigma\sqrt{SC}\,(1 - 2/\pi) < d$ |
| Competition and mutualism mixed | $(-, -)$ or $(+, +)$ | $+2/\pi$ | $\sigma\sqrt{SC}\,(1 + 2/\pi) < d$ |

so that predator–prey communities tolerate $1/(1 - 2/\pi) \approx 2.75$ times the complexity of random ones, and mixtures of competition and mutualism tolerate only $1/(1 + 2/\pi) \approx 0.61$ times as much (Allesina and Tang 2012).

**Proof** In each case the sign of a pair is chosen with probability $1/2$ for each orientation, so the entries have mean 0. Their variance is $C\,\mathbb{E}[X^2] = C\sigma^2$. For predator–prey pairs $\mathbb{E}[a_{ij}a_{ji}] = -C\,\mathbb{E}\lvert X\rvert\,\mathbb{E}\lvert Y\rvert = -C\sigma^2\cdot 2/\pi$, because $\mathbb{E}\lvert X\rvert = \sigma\sqrt{2/\pi}$ for a normal variable; the correlation is therefore $\rho = -2/\pi$. For same-sign pairs the product is positive and $\rho = +2/\pi$; for independent entries $\rho = 0$. Writing $M = \sigma\sqrt{SC}\,X_S/\sqrt S$ with $X_S$ satisfying Theorem 38.4.2, the eigenvalues of $M$ fill an ellipse whose rightmost point is $\sigma\sqrt{SC}(1 + \rho)$, and stability of $A = -dI + M$ requires this to be less than $d$. $\square$

The intuition is that a predator–prey pair is an oscillator: its $2 \times 2$ block has eigenvalues $\pm\mathrm{i}\sqrt{\lvert a_{ij}a_{ji}\rvert}$, moving eigenvalues along the imaginary axis without pushing them to the right, whereas pairs of the same sign are positive or negative feedback loops that spread the eigenvalues along the real axis (Figure 3). Several qualifications apply. Communities of competitors only, or of mutualists only, have entries with non-zero mean; the mean adds a single outlying eigenvalue near $(S - 1)C\,\mathbb{E}[a_{ij}]$, which is strongly negative (stabilizing) for competition and strongly positive (destabilizing) for mutualism, so that large mutualistic communities need strong self-regulation or saturating benefits ([7.19.29](/7.19.29)). Real webs also have hierarchical, body-size-structured predator–prey links, and the community matrix is not independent of the equilibrium abundances, which must be positive (*feasible*); random matrices say nothing about feasibility, which becomes improbable at large $S$ unless interactions are weak (Dougoud et al. 2018).

![Interaction types and stability (Allesina and Tang 2012). Eigenvalues of random interaction matrices with S = 400 species, connectance C = 0.25 and σ√(SC) = 1, without self-regulation, and the ellipses of the elliptic law (red; horizontal semi-axis 1 + ρ, vertical 1 − ρ, Theorem 38.4.2). A: independent random entries (ρ = 0): the circle of May's model. B: predator–prey pairs (ρ = −2/π): the cloud is compressed horizontally, so a self-regulation d = 0.36 suffices for stability. C: pairs of the same sign, competition and mutualism mixed (ρ = +2/π): the cloud is stretched horizontally and requires d = 1.64](./plots/allesina-tang.py)

### 38.4.4. What Stabilizes Real Webs

Empirical food webs are more stable than random matrices with the same $S$, $C$ and interaction strengths, and several features account for this.

- *Many weak interactions.* Interaction strengths in real webs are highly skewed: most links are weak and a few strong (Paine 1992; Wootton 1997). In models, weak links between strongly interacting pairs dampen oscillations, because a weak link to an alternative prey or a competing consumer draws energy away from a potentially unstable pair (McCann, Hastings and Huxel 1998). Reducing $\sigma$ for most links is exactly what (38.2) requires.
- *Organization of trophic loops.* Neutel, Heesterbeek and de Ruiter (2002) analyzed soil food webs whose interaction strengths had been calculated from measured biomass and energy flows. Each closed loop of interactions has a *loop weight*, the geometric mean of the magnitudes of its interaction strengths. Because biomass declines up the web and the per capita effect of predators on prey is much larger than that of prey on predators, long loops in real webs contain weak links and have low weights; in randomized webs with the same interaction strengths, long loops are heavy, and stability is much lower. The maximum loop weight predicted stability.
- *Compartments.* Webs divided into subwebs with strong interactions within and weak interactions between them are more persistent, because perturbations are contained (May 1972; Stouffer and Bascompte 2011). Real webs are more compartmentalized than random ones, mainly because species in different habitats or of different body sizes rarely interact.
- *Allometry and adaptive behavior.* Predator–prey body-mass ratios of 10–100 make the interactions of large predators slow and weak relative to their prey, which stabilizes large model webs (Brose, Williams and Martinez 2006); adaptive diet choice, switching to abundant prey, redistributes predation and stabilizes webs that would otherwise lose species (Kondoh 2003).

## 38.5. Diversity and Stability

### 38.5.1. Populations and Aggregates

May's analysis concerns the stability of the abundances of individual species. Ecosystem services depend instead on aggregate properties: total biomass, primary production, yield. These can be stabilized by diversity even when populations are not, by a purely statistical mechanism.

**Proposition 38.5.1 (Statistical Averaging)** Let a community of $S$ species have total abundance $T = \sum_i N_i$ with mean $m$, shared equally ($\mathbb{E}[N_i] = m/S$), and let the variance of each species obey the mean–variance scaling $\operatorname{Var}(N_i) = c\,\mathbb{E}[N_i]^z$ (Taylor's power law; typically $1 \le z \le 2$). If the species fluctuate independently,

$$
\mathrm{CV}_{\mathrm{pop}} = \sqrt c\left(\frac mS\right)^{z/2 - 1} \propto S^{1 - z/2}, \qquad
\mathrm{CV}_{\mathrm{com}} = \sqrt c\,m^{z/2 - 1}S^{(1 - z)/2} \propto S^{(1 - z)/2}. \tag{38.3}
$$
If instead all pairs of species have the same correlation $\rho$ (with equal variances),

$$
\frac{\mathrm{CV}_{\mathrm{com}}}{\mathrm{CV}_{\mathrm{pop}}} = \sqrt{\rho + \frac{1 - \rho}{S}}. \tag{38.4}
$$

**Proof** The coefficient of variation of one species is $\sqrt{c(m/S)^z}/(m/S) = \sqrt c\,(m/S)^{z/2 - 1}$. For independent species $\operatorname{Var}(T) = S\cdot c(m/S)^z$, so $\mathrm{CV}_{\mathrm{com}} = \sqrt{Sc(m/S)^z}/m = \sqrt c\,m^{z/2 - 1}S^{(1 - z)/2}$. With pairwise correlation $\rho$ and common variance $v$, $\operatorname{Var}(T) = Sv + S(S - 1)\rho v$, and dividing $\mathrm{CV}_{\mathrm{com}}^2 = \operatorname{Var}(T)/m^2$ by $\mathrm{CV}_{\mathrm{pop}}^2 = v/(m/S)^2$ gives $(1 + (S - 1)\rho)/S = \rho + (1 - \rho)/S$. $\square$

For $1 < z < 2$, the variability of the community total falls with richness while the variability of each population rises (Figure 4A): diversity stabilizes the aggregate and destabilizes its parts, and both statements can be true of the same community (Tilman 1999; Doak et al. 1998).

**Definition 38.5.1 (Portfolio Effect and Insurance Hypothesis)** The *portfolio effect* is the reduction in the variability of an aggregate property (total biomass, production, yield) of a community, relative to the variability of its components, that results from summing components that fluctuate less than perfectly synchronously, in analogy with a diversified financial portfolio. The *insurance hypothesis* (Yachi and Loreau 1999) holds that biodiversity insures ecosystem functioning against environmental fluctuations, because species respond differently to the environment, so that some maintain function when others fail, and that this effect increases the mean and decreases the variance of ecosystem properties.

The portfolio effect depends on synchrony (Figure 4B, Eq. 38.4). With positively correlated species, as when all plants respond in the same way to a drought, averaging is limited: $\mathrm{CV}_{\mathrm{com}}/\mathrm{CV}_{\mathrm{pop}} \to \sqrt\rho$ as $S \to \infty$. Negative covariance, *compensatory dynamics* in which one species increases when its competitor decreases, strengthens it. Competition therefore contributes, because competitors tend to fluctuate in opposite directions, as do differences in response to the environment, the core of the insurance hypothesis; complementarity and selection effects on mean productivity, which add to these effects, are treated in [7.19.50](/7.19.50). Loreau and de Mazancourt (2008) measured synchrony by $\varphi = \operatorname{Var}(T)/(\sum_i \sigma_i)^2$, which is 1 for perfectly synchronous and $1/S$ for independent species of equal variance.

![Diversity and the variability of populations and communities. A: coefficient of variation of the community total (solid) and of single populations (dashed) against the number of equally abundant, independently fluctuating species, for mean–variance scaling exponents z = 1.0, 1.5 and 2.0 (Eq. 38.3): for 1 < z < 2 community variability declines and population variability increases with richness; z = 1 leaves community variability unchanged, z = 2 population variability. B: the ratio of community to population variability for species with pairwise correlation ρ (Eq. 38.4): positive correlation (synchrony) limits the portfolio effect, and negative covariance (ρ = −0.03, possible for up to 1 + 1/0.03 ≈ 34 species) strengthens it](./plots/diversity-stability.py)

### 38.5.2. Evidence

The clearest tests come from grasslands at Cedar Creek, Minnesota. In 207 plots of natural grassland, the year-to-year variability of total plant biomass over 11 years was lower in plots with more species, and plots with more species lost less biomass and recovered faster after the severe drought of 1987–1988 (Tilman and Downing 1994; Tilman 1996). The variability of the populations of the 39 most common species, in contrast, tended to increase slightly with richness, but the effect was weak and inconsistent. In the Cedar Creek biodiversity experiment, plots sown with 1–16 species showed over a decade that the temporal stability of total biomass (mean/standard deviation) increased with richness and that of single species decreased (Tilman, Reich and Knops 2006). Across eight European grassland experiments with 1–32 species, richness stabilized community biomass through both overyielding (higher mean production) and asynchrony among species, while destabilizing populations (Hector et al. 2010).

The portfolio effect is also economically important. The sockeye salmon (*Oncorhynchus nerka*) of Bristol Bay, Alaska, spawn in hundreds of streams and lakes whose populations fluctuate asynchronously; the variability of the total catch is less than half of what it would be if the fishery depended on a single population, and fishery closures would be about ten times as frequent (Schindler et al. 2010). In multitrophic communities the relation between richness and population variability can differ: in microcosms of algae, bacteria, protozoa and rotifers, population variability did not increase with richness, and in microcosms assembled from tropical rock pools it decreased (Steiner et al. 2005; Vogt et al. 2006). There is no single relation between complexity and stability: it depends on the level (population or aggregate), the kind of stability and the structure of the interactions.

## 38.6. Robustness and Secondary Extinctions

The loss of a species can cause the loss of others: consumers that depend on it, parasites that need it as a host, plants that need it as a pollinator. These *secondary extinctions* are the most direct way in which food-web structure determines the consequences of species loss.

Dunne, Williams and Martinez (2002) simulated the sequential removal of species from 16 real food webs. A consumer went extinct when it had lost all its prey; basal species could be lost only by removal. Robustness was measured as the fraction of species that had to be removed for half of all species to be lost (primary plus secondary extinctions), $R_{50}$; its maximum value is 0.5 (no secondary extinctions).

- Removing the most connected species first caused much faster collapse than random removal. Removing the most connected species but protecting basal species produced collapse no faster than random removal, because the most damaging removals are those of producers on which many consumers depend.
- Robustness increased with connectance: in webs where consumers have many prey, the loss of one rarely leaves a consumer without food.
- There were exceptions: the removal of a poorly connected basal species could cause a cascade of extinctions if its single consumer was the main prey of many predators, a reminder that the identity of the lost species matters, which is the idea of the **keystone species** ([7.19.33](/7.19.33)).

Simulations with niche-model webs reproduce these results (Figure 5). Including parasites reduces robustness slightly, mainly because many parasites need several host species to complete their life cycles ([7.19.28](/7.19.28)). The vulnerability of food webs to the loss of their most connected species parallels the "robust yet fragile" behavior of networks with skewed degree distributions, which tolerate random failures but break up when hubs are attacked ([1.4.7](/1.4.7#sec-7.8.1); [7.9.12](/7.9.12#sec-12.1.3)). Mutualistic networks of plants and pollinators differ from food webs in structure: they are nested (**nestedness**, [7.19.29](/7.19.29)), which makes them robust to random species loss but sensitive to the loss of the generalist core, whereas food webs tend to be compartmentalized (Thébault and Fontaine 2010).

![Secondary extinctions and robustness of niche-model food webs with 50 species. After each primary removal, consumers left without prey go extinct, repeatedly. A: fraction of species remaining against fraction removed, mean of 40 webs with connectance 0.10, for removal of the most connected species first (red), random removal (blue) and removal of the most connected species while sparing basal species (green); the dotted diagonal is the line of no secondary extinctions, the dashed line the 50 % level that defines robustness R50. B: robustness R50 against connectance for the three removal orders: robustness increases with connectance, most markedly when the most connected species are removed first](./plots/secondary-extinctions.py)

## Summary

| Topic | Key results |
|---|---|
| Food chains | **Food chain** (Definition 38.1.1); grazing, detrital and parasitic chains; chains are temporary abstractions within webs |
| Food webs | **Food web** (Definition 38.1.2); basal, intermediate and top species; link density $L/S$; connectance $C = L/S^2$ (Definition 38.1.3), 0.03–0.3 and roughly independent of $S$ |
| Trophic levels | **Trophic level** (Definition 38.1.4); fractional levels from $(I - Q)\boldsymbol{t} = \boldsymbol{1}$ (Proposition 38.1.1, Example 38.1.1); $\delta^{15}\mathrm{N}$ +3.4 ‰ per step |
| Structure | cascade model (hierarchy, no loops); niche model (interval diets on one axis, predicts many properties from $S$ and $C$) |
| Chain length | 2–5 levels; energetics, productive space, ecosystem size (best supported with productivity), dynamic stability, design constraints and adaptive foraging |
| Stability | resistance and **resilience** (Definition 38.3.1), local/global stability, persistence, variability, robustness; resistance and resilience often traded off; resilience rises with energy flux per biomass |
| Complexity | circular law (Theorem 38.4.1); May's criterion $\sigma\sqrt{SC} < d$ (Proposition 38.4.1); elliptic law (Theorem 38.4.2); predator–prey structure tolerates 2.75 times the complexity, competition–mutualism mixtures 0.61 times (Proposition 38.4.2); weak links, light long loops, compartments and allometry stabilize real webs |
| Diversity–stability | community CV $\propto S^{(1 - z)/2}$ falls, population CV $\propto S^{1 - z/2}$ rises (Proposition 38.5.1); portfolio effect and insurance hypothesis (Definition 38.5.1) depend on asynchrony; Cedar Creek, European grasslands, Bristol Bay salmon |
| Robustness | secondary extinctions fastest when the most connected (especially basal) species are lost; robustness increases with connectance |

## Questions

1. In Example 38.1.1, the hawk changes its diet to 40 % mice, 40 % snakes and 20 % grasshoppers. Compute its new trophic level. Then suppose the snake also eats grasshoppers (30 % of its diet) and recompute the levels of snake and hawk.

   **Answer** With the original levels (grasshopper 2, mouse 2.5, snake 3.5): hawk $= 1 + 0.4\cdot2.5 + 0.4\cdot3.5 + 0.2\cdot2 = 1 + 1 + 1.4 + 0.4 = 3.8$, unchanged by coincidence. If the snake eats 70 % mice and 30 % grasshoppers, its level is $1 + 0.7\cdot2.5 + 0.3\cdot2 = 3.35$, and the hawk's becomes $1 + 0.4\cdot2.5 + 0.4\cdot3.35 + 0.2\cdot2 = 3.74$.

2. A community has $S = 100$ species with connectance $C = 0.1$ and self-regulation $d = 1$. By May's criterion, what is the maximal root-mean-square interaction strength compatible with stability if interactions are random? If they are all predator–prey pairs? If $S$ doubles with $C$ unchanged, by what factor must interaction strengths fall?

   **Answer** Random: $\sigma < d/\sqrt{SC} = 1/\sqrt{10} = 0.32$. Predator–prey: $\sigma < 1/[\sqrt{10}(1 - 2/\pi)] = 0.316/0.363 = 0.87$. Doubling $S$ multiplies $\sqrt{SC}$ by $\sqrt2$, so $\sigma$ must fall by the factor $1/\sqrt2 \approx 0.71$.

3. Show that a $2 \times 2$ block $\begin{bmatrix} 0 & a \\ -b & 0 \end{bmatrix}$ with $a, b > 0$ (a predator–prey pair without self-regulation) has purely imaginary eigenvalues, and that $\begin{bmatrix} 0 & a \\ b & 0\end{bmatrix}$ (mutualism) has one positive real eigenvalue. Relate this to Proposition 38.4.2.

   **Answer** The characteristic polynomials are $\lambda^2 + ab$ and $\lambda^2 - ab$, with roots $\pm\mathrm{i}\sqrt{ab}$ and $\pm\sqrt{ab}$. A predator–prey pair rotates perturbations (neutral oscillation, as in the Lotka–Volterra predator–prey model of [7.19.25](/7.19.25)), contributing imaginary parts but no positive real part, so the eigenvalue cloud of a predator–prey community extends mainly along the imaginary axis and the rightmost eigenvalue is small ($1 + \rho$ with $\rho < 0$). A pair of the same sign (mutualism, or competition, whose block $\begin{bmatrix} 0 & -a\\ -b & 0\end{bmatrix}$ also has eigenvalues $\pm\sqrt{ab}$) is a positive feedback loop with a real positive eigenvalue, which spreads the cloud along the real axis and requires more self-regulation.

4. Ten species of equal mean biomass fluctuate independently, each with a coefficient of variation of 0.4. What is the coefficient of variation of total biomass? What if the pairwise correlation is 0.5?

   **Answer** With equal means and variances and independence, $\mathrm{CV}_{\mathrm{com}} = \mathrm{CV}_{\mathrm{pop}}/\sqrt S = 0.4/\sqrt{10} = 0.126$. With $\rho = 0.5$, by (38.4), $\mathrm{CV}_{\mathrm{com}} = 0.4\sqrt{0.5 + 0.5/10} = 0.4\sqrt{0.55} = 0.30$: synchrony removes most of the benefit of diversity.

5. Why might a food web be robust to random species loss but fragile to the loss of particular species? Which kinds of species are most likely to be "particular" in this sense?

   **Answer** When species are lost at random, most losses are of species with few links, whose disappearance leaves no consumer without food, especially when connectance is high and consumers have alternative prey. When the most connected species are lost, many consumers lose a large part of their diet at once, and secondary extinctions spread. The species whose loss is most damaging are (1) basal species or abundant intermediate species on which many consumers depend (such as krill in the Southern Ocean), (2) keystone predators whose loss releases competitive dominants, causing extinctions of other species through competition, an effect not captured by simple topological simulations ([7.19.33](/7.19.33)), and (3) mutualists such as the generalist pollinators at the core of nested networks.

6. (Open question) Design a study to test whether food-chain length in a set of lakes is limited by productivity, by ecosystem size or by disturbance.

   **Answer** Choose 20–30 lakes spanning independent gradients of total phosphorus (productivity), volume (size) and disturbance (e.g. frequency of drying or winter fish kills), avoiding correlation among the three. Measure food-chain length as the trophic position of the top predator from $\delta^{15}\mathrm{N}$, corrected for the baseline with long-lived primary consumers (snails, mussels), $\mathrm{TP} = \lambda + (\delta^{15}\mathrm{N}_{\mathrm{top}} - \delta^{15}\mathrm{N}_{\mathrm{base}})/3.4$. Fit a regression of chain length on the three variables (and their products, since productive space is productivity times size), and compare models by AIC. The productive-space hypothesis predicts an interaction or a product term, the ecosystem-size hypothesis a size effect independent of productivity, the dynamic-stability hypothesis a negative effect of disturbance. Complement with experiments in mesocosms (fertilization, predator addition) and consider the mechanisms by which size acts: more prey species, habitat heterogeneity, larger populations of top predators.
