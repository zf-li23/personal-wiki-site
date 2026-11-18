---
title: "Trophic Control: Cascades, Apparent Competition and Regime Shifts"
description: "Indirect effects in food webs. Trophic cascades in three- and four-level systems (sea otters, kelp and salt-marsh crabs, intertidal birds, Costa Rican ant-plants, Atlantic cod, dingoes and mesopredators, lakes); top-down and bottom-up control, 'why is the world green?' and the exploitation ecosystems hypothesis, with the Lotka–Volterra food chain solved for any number of levels and proved globally stable; apparent competition, the reduction to Lotka–Volterra competition and the P* rule, intraguild predation; alternative stable states and regime shifts in lakes, reefs and drylands, the Scheffer lake model, fold bifurcations and hysteresis, critical slowing down derived from the Ornstein–Uhlenbeck process, early warning signals and biomanipulation."
---

A species affects not only the species it eats and the species that eat it. Through them it affects their other prey, predators and competitors, and the effects spread through the food web ([7.19.38](/7.19.38)) as indirect interactions. In a survey of more than 100 predator-removal experiments, about one in three that gave significant results showed effects that were indirect and often unexpected (Sih et al. 1985). This chapter treats the three most important classes of indirect effects. Section 39.1 describes trophic cascades, in which predators indirectly benefit plants by suppressing herbivores. Section 39.2 asks whether communities are controlled from the top or from the bottom of the food chain and derives the equilibrium structure of food chains along productivity gradients. Section 39.3 treats apparent competition between prey that share a predator, and intraguild predation. Section 39.4 turns to the most dramatic consequence of feedbacks in food webs, alternative stable states and the abrupt regime shifts between them, and derives the early warning signals that may precede such shifts. The mathematics, phase-plane analysis, Lyapunov functions and bifurcations, is developed in [2.4.11](/2.4.11) and was applied to predator–prey systems in [7.19.25](/7.19.25)–[7.19.26](/7.19.26); here it is applied to whole food chains.

## 39.1. Trophic Cascades

### 39.1.1. Definition

**Definition 39.1.1 (Trophic Cascade)** A **trophic cascade** is the propagation of the effects of a consumer down a food chain across more than one trophic level: a predator that reduces the abundance (or changes the behavior) of its prey thereby increases the abundance of the prey's own resources, typically plants or phytoplankton.

Two distinctions are useful. In a *density-mediated* cascade the predator acts by killing prey; in a *trait-mediated* cascade it acts by changing prey behavior, for example by making herbivores avoid risky places or feed less, the **non-consumptive effects** of predation ([7.19.24](/7.19.24#sec-24.4.4)). And a *species-level* cascade changes the abundance of particular plant species, whereas a *community-level* cascade changes the biomass or production of the whole plant community (Polis et al. 2000). Community-level cascades are most likely where habitats are discrete and homogeneous, where producers grow fast relative to their consumers, and where the producers are uniformly edible: the pelagic zone of lakes, streams and rocky shores. In forests and grasslands, with their slow-growing, often unpalatable plants, cascades usually act at the species level.

### 39.1.2. Three-Level Cascades

**Example 39.1.1 (Sea Otters, Urchins and Kelp)** Sea otters (*Enhydra lutris*) were hunted almost to extinction for their fur in the eighteenth and nineteenth centuries. In the Aleutian Islands, islands where otters had recovered had few sea urchins and dense kelp forests, whereas islands without otters had abundant urchins and "urchin barrens" with little kelp (Estes and Palmisano 1974). The otter is a **keystone species** ([7.19.33](/7.19.33)): the kelp forest it maintains is habitat for fishes and invertebrates, including abalones on which fisheries depend, so that otters increase abalone densities in spite of eating them (Raimondi et al. 2015). In the 1990s, killer whales (*Orcinus orca*), apparently deprived of their usual prey of seals and sea lions, began to eat otters in the western Aleutians; otter numbers fell by an order of magnitude, urchins increased and kelp declined, adding a fourth level to the cascade (Estes et al. 1998).

:::

A recent example shows a cascade that reaches the physical environment. In the Elkhorn Slough estuary in California, sea otters that recolonized from the 1980s onward eat large numbers of shore crabs (*Pachygrapsus crassipes*), which burrow into creek banks and eat the roots of salt-marsh plants. As otter numbers rose, crab densities fell, marsh vegetation on the banks recovered, and the rate of lateral erosion of the creek banks declined markedly, both in comparisons of creeks with many and few otters and in experiments that excluded otters (Hughes et al. 2024). The recovery of a top predator thus slowed the loss of the marsh itself.

On the rocky shores of Washington State, Wootton (1992) excluded gulls and oystercatchers from areas of 10 m² with cages. The birds reduced the biomass of limpets and thereby increased the cover of algae, a cascade; but their effects on the three limpet species differed in sign, because the birds also removed goose barnacles, the cryptic background of one light-colored limpet, and freed space for mussels, the background of a dark one. Even a "simple" cascade is embedded in a web of indirect effects through habitat and competition.

### 39.1.3. Four Levels and Longer Chains

With four levels, a cascade predicts an alternation: an increase of the top carnivore decreases the primary carnivores, increases the herbivores and decreases the plants. In lowland rain forest in Costa Rica, beetles of the genus *Tarsobaenus* prey on *Pheidole* ants that live in the ant-plant *Piper cenocladum* and remove its herbivores. Where beetles were abundant, ants were scarce, herbivory was heavy and plants had less leaf area; at sites with few beetles, the reverse (Letourneau and Dyer 1998). On small Bahamian islands with lizards (top predators), orb-weaving spiders (primary carnivores) and herbivorous insects on sea-grape shrubs, removing the lizards increased spiders and reduced gall-forming midges that only the spiders eat, as a four-level chain predicts; but lizards also eat many plant-sucking homopterans directly, and through that link the system behaved as three levels (Spiller and Schoener 1990). Omnivory, which links nonadjacent levels, blurs the alternation.

In rare cases a cascade spreads through five levels. Off Nova Scotia, the collapse of Atlantic cod (*Gadus morhua*) and other large demersal fishes by overfishing in the early 1990s was followed by increases of their prey, small pelagic fishes and benthic crustaceans (snow crab, northern shrimp), decreases of the large zooplankton those eat, increases of phytoplankton, and a decline of the nitrate that phytoplankton consume (Frank et al. 2005).

A special case is *mesopredator release*: when an apex predator declines, the smaller predators it suppresses increase and their own prey decline. In the Strzelecki Desert of Australia, a fence more than 5000 km long excludes dingoes (*Canis lupus dingo*) from sheep country. Where dingoes were present, red foxes and feral cats were scarcer and the endangered dusky hopping mouse (*Notomys fuscus*) more abundant than across the fence (Letnic et al. 2009): the dingo, often treated as a pest, protects small native mammals from introduced mesopredators.

### 39.1.4. Cascades in Lakes

The cascade is clearest in lakes, where Carpenter, Kitchell and Hodgson (1985) formulated it as a theory of lake productivity: piscivorous fish eat planktivorous fish, which eat large zooplankton (above all *Daphnia*), which graze phytoplankton. Planktivorous fish select the largest zooplankton (the size-efficiency hypothesis of Brooks and Dodson 1965), so in lakes without piscivores the zooplankton is dominated by small species that graze inefficiently, and phytoplankton is abundant; adding piscivores reduces planktivores, allows large *Daphnia* to increase and clears the water. In whole-lake experiments in Wisconsin, piscivorous largemouth bass (*Micropterus salmoides*) were added to Tuesday Lake and planktivorous minnows removed, while the adjacent Paul Lake served as reference; zooplankton shifted to large *Daphnia* and chlorophyll and primary production fell (Carpenter and Kitchell 1993). The effect of nutrients and of the food web on phytoplankton are of similar magnitude: "bottom-up" phosphorus sets the potential productivity of a lake and "top-down" fish determine how much of it appears as algae ([7.19.42](/7.19.42)). This is the basis of biomanipulation (Section 39.4.5).

## 39.2. Top-Down and Bottom-Up Control

### 39.2.1. Two Kinds of Control

**Definition 39.2.1 (Top-Down and Bottom-Up Control)** A trophic level is under **top-down control** when its abundance is determined mainly by its consumers, and under **bottom-up control** when it is determined mainly by its resources. A food web is called top-down (consumer-controlled) when control by consumers propagates down the chain as a trophic cascade, and bottom-up (resource-controlled, or *donor-controlled*) when the abundance of every level is set by the supply from the level below, which its consumers do not reduce.

In a trophic cascade the two kinds alternate: in a three-level system predators are controlled bottom-up by their prey, herbivores top-down by predators, and plants bottom-up by their resources, having been released from herbivores. Donor control is inevitable where consumers cannot affect the supply of their food: detritivores do not affect the rate at which litter falls, nor nectar feeders the production of nectar, nor most rare phytophagous insects the abundance of their host plants. Both kinds of control operate in every ecosystem, and the question is their relative strength. A meta-analysis of 121 manipulations of predators in terrestrial, freshwater and marine systems found that removing predators consistently increased herbivores and, less strongly, decreased plants; fertilization increased plants but these increases were not transmitted to herbivores (Borer et al. 2006). Top-down effects seem to propagate through food chains more readily than bottom-up effects. Top-down control tends to be strong in systems with strong cascades and in mature, complex systems with many tight consumer–resource links; bottom-up control in systems dominated by detritivores and in simple, unproductive systems such as the Arctic, where the abundance of lichens and mosses limits reindeer.

### 39.2.2. Why Is the World Green?

Hairston, Smith and Slobodkin (1960; "HSS") asked why herbivores do not eat most of the plant biomass that surrounds them, and answered that herbivores are generally limited by predators rather than by food: the world is green because of a community-level trophic cascade. Murdoch (1966) objected that much of the green is inedible, protected by toughness, spines and toxic secondary compounds ([7.19.24](/7.19.24#sec-24.3)), so that herbivores may compete for the scarce palatable fraction and the world could be green under bottom-up control ("the world is prickly and tastes bad", in Polis's later phrase). The two answers are not exclusive, and they predict different responses to experiments: under HSS, removing predators should lead to defoliation; under Murdoch's view, it should have little effect on plant biomass. The meta-analyses above, and the dramatic effects of removing predators in systems such as islands of Lago Guri in Venezuela, where herbivores multiplied and seedlings almost disappeared on predator-free islands created by a reservoir (Terborgh et al. 2001), show that top-down control is common, though rarely complete.

### 39.2.3. The Exploitation Ecosystems Hypothesis

Oksanen, Fretwell, Arruda and Niemelä (1981) linked HSS to productivity. In unproductive environments a plant population cannot support enough herbivores to sustain predators; in more productive ones it can. They predicted which levels should increase with productivity from a model of a food chain, which we now analyze for any number of levels.

Let $X_1$ be plant biomass with logistic growth (rate $r$, carrying capacity $K$, a measure of productivity), and $X_2, \dots, X_n$ the consumer levels, each eating only the level below with a linear functional response:

$$
\begin{aligned}
\frac{\mathrm{d}X_1}{\mathrm{d}t} &= X_1\left[r\left(1 - \frac{X_1}{K}\right) - a_1X_2\right],\\
\frac{\mathrm{d}X_i}{\mathrm{d}t} &= X_i\left[e_{i-1}a_{i-1}X_{i-1} - m_i - a_iX_{i+1}\right],\qquad i = 2, \dots, n,\quad X_{n+1} = 0,
\end{aligned} \tag{39.1}
$$
where $a_i$ is the attack rate of level $i + 1$ on level $i$, $e_i$ the efficiency with which consumed biomass of level $i$ is converted into biomass of level $i + 1$, and $m_i$ the mortality of level $i$. This is the Lotka–Volterra food chain; for $n = 2$ it is the predator–prey model with logistic prey of [7.19.25](/7.19.25).

**Proposition 39.2.1 (Equilibria of the Food Chain)** Suppose (39.1) has an equilibrium $\boldsymbol{X}^*$ with all $n$ levels positive. Then

1. the levels $n - 1, n - 3, n - 5, \dots$ are independent of $K$: $X_{n-1}^* = m_n/(e_{n-1}a_{n-1})$ and $X_{i-1}^* = (m_i + a_iX_{i+1}^*)/(e_{i-1}a_{i-1})$;
2. the top level $n$ and the levels $n - 2, n - 4, \dots$ increase linearly with $K$;
3. adding a level $n + 1$ (possible once $e_na_nX_n^* > m_{n+1}$) fixes the former top level and makes the levels below it that were constant increase with $K$, and vice versa.

In particular, plant biomass increases with productivity when the chain has an odd number of levels and is constant when it has an even number.

**Proof** At the equilibrium the bracket of each equation vanishes. The equation for level $n$ gives $e_{n-1}a_{n-1}X_{n-1}^* = m_n$, a constant. The equation for level $i$ ($2 \le i \le n - 1$) gives $X_{i-1}^* = (m_i + a_iX_{i+1}^*)/(e_{i-1}a_{i-1})$, which expresses $X_{i-1}^*$ through $X_{i+1}^*$; starting from $X_{n-1}^*$, all levels $n - 3, n - 5, \dots$ are constants. If $n$ is odd this reaches $X_2^*$; the plant equation then gives $X_1^* = K(1 - a_1X_2^*/r)$, linear in $K$, and the level equations, read upward, $X_{i+1}^* = (e_{i-1}a_{i-1}X_{i-1}^* - m_i)/a_i$ give $X_3^*, X_5^*, \dots, X_n^*$, each linear in its predecessor and hence in $K$, with positive slope. If $n$ is even the recursion reaches $X_1^*$ as a constant, the plant equation gives $X_2^* = r(1 - X_1^*/K)/a_1$, an increasing function of $K$, and the upward recursion gives the increasing levels $X_4^*, \dots, X_n^*$. Part 3 follows by applying parts 1 and 2 to the chains of $n$ and $n + 1$ levels; the condition for invasion is that the per capita growth rate $e_na_nX_n^* - m_{n+1}$ of a rare level $n + 1$ be positive. $\square$

**Theorem 39.2.1 (Global Stability of the Food Chain)** If the equilibrium $\boldsymbol{X}^*$ of (39.1) with all levels positive exists, it attracts every solution with $X_i(0) > 0$ for all $i$.

**Proof** Write $u_i = X_i - X_i^*$. Using the equilibrium conditions, the per capita growth rates are $-(r/K)u_1 - a_1u_2$ for plants and $e_{i-1}a_{i-1}u_{i-1} - a_iu_{i+1}$ for level $i \ge 2$. Let

$$
V(\boldsymbol{X}) = \sum_{i=1}^n w_i\left(X_i - X_i^* - X_i^*\ln\frac{X_i}{X_i^*}\right), \qquad w_1 = 1,\quad w_{i+1} = \frac{w_i}{e_i},
$$
which is positive except at $\boldsymbol{X}^*$ and tends to infinity at the boundary of the positive orthant and at infinity. Then $\dot V = \sum_i w_iu_i\,\dot X_i/X_i$, in which the term $-w_ia_iu_iu_{i+1}$ from level $i$ cancels the term $w_{i+1}e_ia_iu_{i+1}u_i$ from level $i + 1$, by the choice of the weights. What remains is $\dot V = -(r/K)u_1^2 \le 0$. On the set $\dot V = 0$, $X_1 = X_1^*$ for all time, so $\dot X_1 = 0$ and the plant equation gives $X_2 = X_2^*$; then $\dot X_2 = 0$ gives $X_3 = X_3^*$, and so on. The only invariant subset is $\{\boldsymbol{X}^*\}$, and LaSalle's invariance principle ([2.4.11](/2.4.11)) gives the result. $\square$

The model therefore predicts biomass "staircases" along a productivity gradient (Figure 1A). At very low productivity only plants exist and increase with $K$. Beyond the first threshold herbivores invade, plant biomass is held constant and herbivores increase. Beyond the second, carnivores invade, herbivores are held constant and plants and carnivores increase; and so on. Adding a top predator to a chain at equilibrium causes a trophic cascade with alternating signs (Figure 1B). Oksanen and colleagues applied the prediction to the Fennoscandian tundra, where on the least productive fell tops plants are limited only by the environment, on more productive tundra lemmings and voles hold vegetation down, and in still more productive habitats predators (mustelids, foxes, birds of prey) limit the rodents. Experiments in which herbivores or predators were excluded along productivity gradients have broadly supported the prediction (Oksanen and Oksanen 2000), though with many exceptions.

![Equilibria of the Lotka–Volterra food chain, Eq. (39.1), with r = 1, all attack rates 1, efficiencies 0.5 and mortalities 0.1. A: equilibrium biomass of plants, herbivores, carnivores and top carnivores against the carrying capacity K of plants, a measure of productivity (logarithmic axis). New levels enter at K = 0.2, 0.25 and 0.75 (dotted lines). In each segment the top level and the levels two, four, … below it increase with K, while the others are fixed (Proposition 39.2.1): plants increase in chains with one or three levels and are held constant in chains with two or four. B: at K = 2, a three-level chain at equilibrium is invaded by a top carnivore: carnivores fall, herbivores rise and plants fall, and the chain settles at the new globally stable equilibrium (Theorem 39.2.1)](./plots/oksanen-food-chain.py)

The staircase is a consequence of prey-dependent functional responses. If consumption depends on the ratio of prey to predators (*ratio-dependent* responses, Arditi and Ginzburg 1989), all levels increase in proportion to productivity, and this is closer to what is seen across lakes, where the biomass of phytoplankton, zooplankton and fish all increase with phosphorus, though less than proportionally (Ginzburg and Akçakaya 1992; Mazumder 1994). The theory is also complicated by the detrital channel. Polis and Strong (1996) pointed out that predators are fed by both herbivores and detritivores; predators subsidized by the detrital chain can suppress herbivores more than the herbivory chain alone could support (the *apparent trophic cascade*), and in 23 marine food webs the share of predator diets derived from detritus increased with primary production (Ward et al. 2015).

## 39.3. Apparent Competition and Intraguild Predation

### 39.3.1. Apparent Competition

Two prey species that share a predator affect each other negatively without sharing any resource: an increase of one prey supports more predators, which then eat more of the other.

**Definition 39.3.1 (Apparent Competition)** **Apparent competition** (Holt 1977) is a reciprocal negative indirect interaction between two prey (or host) species mediated by a shared predator (or parasite): each prey, by increasing the abundance or the activity of the predator, increases the mortality of the other. Its sign pattern is the same as that of exploitation competition; prey can escape it by differing in the way they are found or attacked, "competition for *enemy-free space*" (Jeffries and Lawton 1984).

Field evidence:

- *Subtidal gastropods and bivalves.* On reefs at Santa Catalina Island, California, lobsters, octopuses and whelks prefer sessile bivalves (mainly *Chama arcana*) but also eat mobile gastropods. Adding bivalves to cobble areas attracted predators and increased the mortality and reduced the density of the gastropods, although the two groups compete for no resource (Schmitt 1987).
- *An invasive grass and an endangered lupine.* In the coastal dunes of northern California, European beachgrass (*Ammophila arenaria*) shelters deer mice (*Peromyscus maniculatus*), which eat seeds of the endangered lupine *Lupinus tidestromii*. Seed predation was higher the closer a lupine grew to beachgrass, and at one site it changed the projected growth rate of the lupine population from above to below replacement (Dangremond, Pardini and Knight 2010).
- *Disease-mediated apparent competition.* The introduced grey squirrel (*Sciurus carolinensis*) carries squirrelpox virus, which causes little disease in greys but kills red squirrels (*S. vulgaris*). Models fitted to the spread of greys in Britain showed that the virus made the replacement of reds by greys many times faster than resource competition alone would (Tompkins, White and Boots 2003); shared parasites are a common route of apparent competition ([7.19.28](/7.19.28)).
- *Insect communities.* In a tropical forest community of leaf-mining insects, removing one leaf-miner species reduced the attack by shared parasitoids on the others in the following generations (Morris, Lewis and Godfray 2004), a direct experimental demonstration in a natural host–parasitoid web ([7.19.27](/7.19.27)).

### 39.3.2. A Model

Let two prey $N_1, N_2$ with logistic growth be eaten by a predator $P$ with linear functional responses, and let the predator have a self-limiting term $qP$ (interference or limitation by other factors):

$$
\begin{aligned}
\frac{\mathrm{d}N_i}{\mathrm{d}t} &= N_i\left[r_i\left(1 - \frac{N_i}{K_i}\right) - a_iP\right], \qquad i = 1, 2,\\
\frac{\mathrm{d}P}{\mathrm{d}t} &= P\left[e_1a_1N_1 + e_2a_2N_2 - m - qP\right].
\end{aligned} \tag{39.2}
$$

**Proposition 39.3.1 (Apparent Competition as Lotka–Volterra Competition)** If the predator equilibrates fast relative to its prey and is present ($e_1a_1N_1 + e_2a_2N_2 > m$), the prey dynamics of (39.2) reduce to the Lotka–Volterra competition equations

$$
\frac{\mathrm{d}N_i}{\mathrm{d}t} = N_i\left(\rho_i - \beta_{i1}N_1 - \beta_{i2}N_2\right),\qquad
\rho_i = r_i + \frac{a_im}{q},\quad \beta_{ii} = \frac{r_i}{K_i} + \frac{e_ia_i^2}{q},\quad \beta_{ij} = \frac{a_ie_ja_j}{q}\ (j \ne i). \tag{39.3}
$$
The interspecific coefficients are positive although the prey share no resource; they are proportional to the vulnerability $a_i$ of the affected prey and to the value $e_ja_j$ of the other prey to the predator.

**Proof** Setting $\dot P = 0$ with $P > 0$ gives $P = (e_1a_1N_1 + e_2a_2N_2 - m)/q$. Substituting into the prey equations, $r_i(1 - N_i/K_i) - a_iP = r_i + a_im/q - (r_i/K_i + a_ie_ia_i/q)N_i - (a_ie_ja_j/q)N_j$. $\square$

All results of [7.19.22](/7.19.22) for Lotka–Volterra competition apply: depending on the parameters, one prey excludes the other, the outcome depends on the initial densities, or the prey coexist (when each limits itself more than the other, $\beta_{12}\beta_{21} < \beta_{11}\beta_{22}$). Figure 2 shows a case in which a less vulnerable, faster-growing prey 1 excludes prey 2: introduced into a system of prey 2 and predator, it raises the predator density until prey 2 can no longer persist. A limiting case gives a simple rule. If the prey are not self-limited ($K_i \to \infty$) and the predator is not either ($q \to 0$), each prey $i$ alone supports a predator density $P_i^* = r_i/a_i$, and a rare prey $j$ can invade only if its growth rate exceeds the mortality inflicted by that predator, $r_j > a_jP_i^*$, that is, if $P_j^* > P_i^*$. The prey that tolerates the higher predator density excludes the other: the *P\* rule* (Holt, Grover and Tilman 1994), the analogue for shared predators of the $R^*$ rule for shared resources ([7.19.23](/7.19.23)). When a predator lives mainly on an abundant, tolerant prey, it can drive a rarer, more vulnerable prey extinct while itself remaining abundant; this is the mechanism by which introduced prey (rabbits in Australia supporting cats and foxes, feral pigs on the Channel Islands of California supporting golden eagles that ate island foxes) endanger native species.

![Apparent competition between two prey that share a predator, Eq. (39.2), with r₁ = 1, a₁ = 0.5 (prey 1 is less vulnerable), r₂ = 0.5, a₂ = 1, K₁ = K₂ = 1, e₁ = e₂ = 1, m = 0.1 and q = 0.5. A: the zero-growth isoclines of the reduced Lotka–Volterra system (39.3), for prey 1 (green) and prey 2 (orange), and trajectories of the full three-species model projected on the prey plane (grey; dots mark the starts). The isocline of prey 1 lies above that of prey 2 everywhere, and all trajectories approach prey 1 alone (large dot). B: prey 2 and the predator are at equilibrium when prey 1 is introduced at low density at t = 50; the predator increases on the additional food and prey 2 is driven extinct, although the prey compete for nothing](./plots/apparent-competition.py)

### 39.3.3. Intraguild Predation

**Definition 39.3.2 (Intraguild Predation)** *Intraguild predation* is the killing and eating of species that use the same, often limiting, resources: the intraguild predator both competes with and eats the intraguild prey (Polis, Myers and Holt 1989).

It is widespread: lions kill cheetahs and hyenas, larger spiders eat smaller ones that hunt the same insects, and larval dragonflies eat the damselfly larvae with which they share prey. The simplest model is a module of three species, a resource, an intraguild prey that eats only the resource and an intraguild predator that eats both. Holt and Polis (1997) showed for Lotka–Volterra versions that the three species can coexist only if the intraguild prey is the better competitor for the shared resource (it must persist at a lower resource level, the $R^*$ rule) and only at intermediate productivity: at low productivity the intraguild predator cannot persist on the resource left by its prey, at high productivity it becomes so abundant that it excludes the intraguild prey by predation. Alternative stable states, in which either the predator or the prey wins depending on initial conditions, are also possible. Real systems often violate the coexistence conditions and still persist, through refuges, size structure (adults of one species eat juveniles of the other and vice versa) and omnivory with alternative foods.

## 39.4. Alternative Stable States and Regime Shifts

### 39.4.1. Definitions and Evidence

Some ecosystems do not respond gradually to gradual changes of conditions. A shallow lake that has been clear for decades while nutrients accumulated may become turbid within a year or two; a coral reef that has survived storms for centuries may be overgrown by algae after one more hurricane.

**Definition 39.4.1 (Alternative Stable States and Regime Shifts)** An ecosystem has **alternative stable states** when, under the same external conditions, it can persist in two or more distinct, self-maintaining states, each with its own basin of attraction. A **regime shift** is a large, persistent and relatively abrupt change of an ecosystem from one state (regime) to another, caused by a small change of conditions that crosses a threshold (a tipping point) or by a disturbance that pushes the system across the boundary of a basin of attraction.

Alternative stable states arise from positive feedbacks that make each state self-reinforcing; they are the ecosystem-level form of **bistability** ([7.3.18](/7.3.18)), and the history dependence they cause is **hysteresis**. Examples include:

| System | State 1 | State 2 | Feedbacks maintaining the states |
|---|---|---|---|
| Shallow lakes | clear water, submerged plants | turbid water, phytoplankton | plants stabilize sediment, take up nutrients, shelter zooplankton; phytoplankton shade out plants, benthivorous fish stir up sediment |
| Coral reefs | hard corals | fleshy macroalgae | herbivorous fishes and urchins keep algae down and coral recruits free; algae overgrow and poison recruits, reducing coral cover |
| Kelp forests | kelp forest | urchin barren | predators and drift kelp keep urchins sheltered and fed; in barrens, starving urchins graze all new kelp |
| Drylands | vegetation | bare soil | plants increase infiltration and soil moisture around themselves ([7.19.30](/7.19.30#sec-30.4)) |
| Boreal forest | budworm at low density | outbreak | birds hold budworm at low density until foliage grows too large ([7.19.13](/7.19.13#sec-13.2.5)) |
| Permafrost soils | frozen, inert carbon | thawed, decomposing | thawing releases $\ce{CO2}$ and $\ce{CH4}$, which warm the climate further |

On Caribbean reefs, overfishing of herbivorous fishes left the sea urchin *Diadema antillarum* as the main grazer; when a disease killed almost all *Diadema* in 1983, macroalgae overgrew the reefs of Jamaica within a few years and coral cover fell from more than 50 % to below 5 %, without recovering when the immediate causes eased (Hughes 1994). Scheffer and Carpenter (2003) listed the kinds of evidence for alternative states: sudden jumps in time series, bimodal frequency distributions of a state variable among similar sites, divergent outcomes of experiments started from different initial states, shifts triggered by experimental disturbances, and hysteresis in response to a variable changed slowly up and then down. None is conclusive alone, because a sudden change can also be a steep but continuous response to a rapid change of conditions.

### 39.4.2. The Scheffer Lake Model

Scheffer et al. (2001) captured the shallow-lake case in a minimal model of two variables, turbidity $E$ and the cover of submerged vegetation $V$ (scaled to its maximum):

$$
\frac{\mathrm{d}E}{\mathrm{d}t} = r_EE\left(1 - E\,\frac{h_V + V}{E_0h_V}\right), \qquad
\frac{\mathrm{d}V}{\mathrm{d}t} = r_VV\left(1 - V\,\frac{h_E^p + E^p}{h_E^p}\right). \tag{39.4}
$$
Without vegetation turbidity approaches $E_0$, a quantity that increases with the nutrient loading of the lake; vegetation reduces the equilibrium turbidity to $E_0h_V/(h_V + V)$, by half when $V = h_V$. Vegetation grows logistically to a cover that declines steeply, like a Hill function with exponent $p$, once turbidity exceeds the critical value $h_E$ at which too little light reaches the bottom. Phytoplankton, the main source of turbidity, responds in days, vegetation over a season, so we set $E$ to its quasi-equilibrium and study

$$
\frac{\mathrm{d}V}{\mathrm{d}t} = f(V; E_0) = r_VV\left[1 - g(V; E_0)\right], \qquad g(V; E_0) = V\left(1 + \left(\frac{E_0h_V}{h_E(h_V + V)}\right)^p\right). \tag{39.5}
$$

**Proposition 39.4.1 (Equilibria of the Lake Model)** The positive equilibria of (39.5) are the solutions of $g(V; E_0) = 1$; along them

$$
E_0(V) = h_E\left(\frac{1 - V}{V}\right)^{1/p}\frac{h_V + V}{h_V}, \qquad E^*(V) = h_E\left(\frac{1 - V}{V}\right)^{1/p}, \tag{39.6}
$$
and an equilibrium is stable if and only if $\mathrm{d}E_0/\mathrm{d}V < 0$ there. With $h_V = 0.2$, $h_E = 2$ and $p = 4$, $E_0(V)$ has a local minimum $E_0 = 5.15$ at $V = 0.074$ and a local maximum $E_0 = 7.29$ at $V = 0.676$: for $5.15 < E_0 < 7.29$ there are two stable equilibria, a clear, vegetated one ($V > 0.676$) and a turbid one ($V < 0.074$), separated by an unstable one.

**Proof** At a positive equilibrium the bracket in (39.5) vanishes. Solving $g = 1$ for $(E_0h_V/(h_E(h_V + V)))^p = (1 - V)/V$ gives (39.6), and $E^* = E_0h_V/(h_V + V)$. The eigenvalue of the one-dimensional system at an equilibrium is $\partial f/\partial V = r_V[1 - g] - r_VV\,\partial g/\partial V = -r_VV\,\partial g/\partial V$, so the equilibrium is stable if and only if $\partial g/\partial V > 0$. Differentiating the identity $g(V; E_0(V)) = 1$ gives $\partial g/\partial V + (\partial g/\partial E_0)\,\mathrm{d}E_0/\mathrm{d}V = 0$, and $\partial g/\partial E_0 > 0$, so $\partial g/\partial V > 0$ if and only if $\mathrm{d}E_0/\mathrm{d}V < 0$. The extrema of $E_0(V)$ were found numerically. $\square$

The curve of equilibria is folded (Figure 3A). Imagine nutrient loading rising slowly in a clear lake. Turbidity increases only slightly, because vegetation keeps the water clear, until $E_0$ reaches 7.29; there the clear equilibrium disappears, vegetation collapses and turbidity jumps to the turbid branch. Reducing nutrients back to the level of the collapse does not restore the clear state: the lake stays turbid until $E_0$ falls below 5.15, where the turbid state disappears. Between the two thresholds the state of the lake depends on its history. The potential $U(V) = -\int f\,\mathrm{d}V$ visualizes the stability landscape (Figure 3B): between the folds it has two valleys separated by a hill whose height measures the disturbance needed to switch states, Holling's ecological resilience. As conditions approach a fold the valley of the threatened state becomes shallower and disappears.

![Alternative stable states in the Scheffer lake model, Eqs. (39.4)–(39.6), with h_V = 0.2, h_E = 2 and p = 4. A: equilibrium turbidity against E₀, the turbidity the lake would have without plants, which increases with nutrient loading. The clear, vegetated branch and the turbid branch (solid) are stable and joined by an unstable branch (dashed) between the folds at E₀ = 5.15 and 7.29. Arrows: as nutrients rise, the lake stays clear until vegetation collapses at the upper fold (red); as they fall, it stays turbid until the lower fold (green): hysteresis. B: potentials U(V) for E₀ = 4 (one valley, clear), 6.2 (two valleys: bistable) and 8.5 (one valley, turbid)](./plots/scheffer-lake.py)

### 39.4.3. Folds and Hysteresis in General

The thresholds of the lake model are **saddle-node bifurcations** ([7.6.33](/7.6.33)), also called fold bifurcations, the generic way in which equilibria appear and disappear as a parameter changes. Near a fold every one-dimensional system looks the same.

**Proposition 39.4.2 (Behavior Near a Fold)** Let $\dot x = f(x; c)$, and let $(x_c, c_c)$ be a fold: $f = 0$ and $f_x = 0$ there, with $f_{xx} \ne 0$ and $f_c \ne 0$. Then near $(x_c, c_c)$, on the side where equilibria exist, there are two equilibria

$$
x^* - x_c \approx \pm\sqrt{\frac{-2f_c\,(c - c_c)}{f_{xx}}}, \qquad \lambda = f_x(x^*; c) \approx \pm\sqrt{-2f_cf_{xx}\,(c - c_c)},
$$
one stable and one unstable, and the eigenvalue of the stable one tends to zero like the square root of the distance $\lvert c - c_c\rvert$ to the fold.

**Proof** Expand $f$ to the lowest non-vanishing orders: $f(x; c) \approx f_c(c - c_c) + \frac12f_{xx}(x - x_c)^2$ (the term in $(x - x_c)$ vanishes because $f_x = 0$ at the fold; mixed terms are of higher order on the scale $x - x_c \sim \lvert c - c_c\rvert^{1/2}$). Setting this to zero gives the equilibria, which are real when $f_c(c - c_c)/f_{xx} < 0$. The eigenvalue is $f_x(x^*; c) \approx f_{xx}(x^* - x_c)$, which gives the stated expression; the root with $f_{xx}(x^* - x_c) < 0$ is stable. $\square$

The rescaled normal form is $\dot y = \mu - y^2$. A system with two folds, such as the lake, has a hysteresis loop whose width is the distance between them. Its existence requires a positive feedback strong enough to bend the equilibrium curve back on itself; in the lake model, steepness of the vegetation response ($p$ large) and a strong effect of vegetation on turbidity ($h_V$ small) widen the loop, while weak feedback ($p$ small) makes the response continuous, if steep.

### 39.4.4. Critical Slowing Down and Early Warning Signals

The approach to a fold changes the dynamics of the system before anything visible happens to its mean state, and this offers a possibility of anticipating regime shifts.

**Definition 39.4.2 (Critical Slowing Down)** **Critical slowing down** is the decrease in the rate at which a system recovers from small perturbations as it approaches a bifurcation at which its equilibrium loses stability: the dominant eigenvalue of the equilibrium tends to zero and the return time to infinity.

**Proposition 39.4.3 (Statistical Signatures of Slowing Down)** Let a system fluctuate around a stable equilibrium with eigenvalue $\lambda < 0$, driven by weak white noise of intensity $\sigma$, so that the deviation $y$ obeys the linearized equation $\mathrm{d}y = \lambda y\,\mathrm{d}t + \sigma\,\mathrm{d}W$. Then at stationarity

$$
\operatorname{Var}(y) = \frac{\sigma^2}{2\lvert\lambda\rvert}, \qquad \operatorname{Corr}(y_t, y_{t+\Delta}) = \mathrm{e}^{\lambda\Delta}, \tag{39.7}
$$
so that as the system approaches a fold, where $\lambda \to 0^-$ like $\lvert c - c_c\rvert^{1/2}$, the variance increases like $\lvert c - c_c\rvert^{-1/2}$ and the autocorrelation at any fixed lag tends to 1.

**Proof** The equation is the **Ornstein–Uhlenbeck process** ([7.6.5](/7.6.5)). Its solution $y_t = y_0\mathrm{e}^{\lambda t} + \sigma\int_0^t\mathrm{e}^{\lambda(t - s)}\,\mathrm{d}W_s$ has, by the Itô isometry, a variance whose part independent of $y_0$ is $\sigma^2\int_0^t\mathrm{e}^{2\lambda(t - s)}\,\mathrm{d}s \to \sigma^2/(2\lvert\lambda\rvert)$ as $t \to \infty$, while the term in $y_0$ decays. For the covariance, $y_{t+\Delta} = \mathrm{e}^{\lambda\Delta}y_t + (\text{noise after } t)$, independent of $y_t$, so $\operatorname{Cov}(y_t, y_{t+\Delta}) = \mathrm{e}^{\lambda\Delta}\operatorname{Var}(y_t)$. The behavior near the fold follows from Proposition 39.4.2. In discrete sampling with interval $\Delta$, $y$ is an autoregressive process of order 1 with coefficient $\mathrm{e}^{\lambda\Delta}$. $\square$

In practice the indicators are computed in moving windows of a time series after removing the slow trend: rising variance and rising lag-1 autocorrelation (often tested by Kendall's rank correlation with time) are taken as warnings; skewness and flickering between states are additional signs. Figure 4 shows them in a simulation of the lake model with slowly rising nutrients: the variance and autocorrelation of vegetation cover rise long before the collapse, while the mean declines only gently.

![Critical slowing down before a regime shift in the lake model (39.5) with additive noise (σ = 0.012) and E₀ increasing linearly from 4 to 7.6 over 6000 time units. A: vegetation cover (green) and the clear-state equilibrium (dashed); the collapse occurs shortly after the fold at E₀ = 7.29 (dotted line). B: variance and C: lag-1 autocorrelation of the detrended series in moving windows of 500 time units, computed up to the collapse: both rise well before it. D: the eigenvalue of the clear equilibrium as a function of E₀; it approaches zero at the fold like the square root of the distance, the cause of the rising variance and autocorrelation (Propositions 39.4.2 and 39.4.3)](./plots/critical-slowing-down.py)

The best test in a natural system was a whole-lake experiment. Carpenter et al. (2011) gradually added piscivorous largemouth bass to Peter Lake in Wisconsin, which was expected to push the food web from dominance by planktivorous fish to dominance by piscivores, while the neighboring Paul Lake served as a reference. Variance, autocorrelation and other indicators of chlorophyll and zooplankton rose in Peter Lake more than a year before the food-web transition was complete, and not in Paul Lake. In laboratory populations of yeast with an Allee effect ([7.19.10](/7.19.10)), which collapse at a fold when dilution is increased, recovery after perturbation slowed and the variance and autocorrelation of population size increased before the collapse (Dai et al. 2012).

The limitations are serious. Indicators require long, frequently sampled time series, often unavailable for ecosystems. Not every regime shift is a fold: a large disturbance can push a system across the boundary of a basin without any approach to a bifurcation, and shifts driven by noise or by rapid changes of conditions give no warning. Rising variance can also have other causes, such as increasing environmental variability, and some bifurcations (in cyclic systems, or with noise that is multiplicative) give different signatures. Early warning indicators are best regarded as one source of evidence, together with knowledge of the feedbacks that could create alternative states.

### 39.4.5. Restoration and Management

Hysteresis has a practical consequence: once a system has shifted, restoring the conditions under which it collapsed is not enough. A lake that became turbid at a certain phosphorus loading must be brought well below that loading, or the turbid state must be broken by an intervention that moves the system into the other basin of attraction. *Biomanipulation* does this: planktivorous and benthivorous fish (bream, roach, carp) are removed and piscivores (pike, perch) stocked, so that large zooplankton increase, the water clears, and submerged plants can establish and then maintain the clear state themselves. In the small Dutch lake Zwemlust, draining the lake to remove its fish in 1987 and restocking with pike and rudd produced clear water and dense vegetation within a year (van Donk et al. 1990); in many Danish and Dutch lakes biomanipulation succeeded where phosphorus loading had also been reduced, and failed or lasted only a few years where it had not (Jeppesen et al. 2012). The general lesson for management is to identify the slow variables (phosphorus in sediments, herbivore stocks, soil cover) that erode resilience before a shift and to maintain them away from thresholds, rather than to rely on the apparent stability of a system that still looks the same.

## Summary

- **Trophic cascade** (Definition 39.1.1): predators indirectly increase plants by suppressing herbivores; density- or trait-mediated, species- or community-level. Examples: sea otters, urchins and kelp, and otters, crabs and marsh erosion; birds and limpets; four-level chains in Costa Rica and the Bahamas; cod off Nova Scotia (to nitrate); dingoes and mesopredators; piscivores, planktivores, *Daphnia* and phytoplankton in lakes.
- Top-down and bottom-up control (Definition 39.2.1) alternate in cascades; top-down effects propagate more readily (meta-analysis). HSS: the world is green because predators control herbivores; Murdoch: because much plant matter is inedible.
- The Lotka–Volterra food chain (39.1): the levels below the top at odd distances are fixed, the top and the levels at even distances increase with productivity (Proposition 39.2.1); the interior equilibrium is globally stable (Theorem 39.2.1, Lyapunov function with weights $w_{i+1} = w_i/e_i$). Exploitation ecosystems hypothesis: biomass staircases; ratio dependence and detritus modify them.
- **Apparent competition** (Definition 39.3.1) through shared predators reduces to Lotka–Volterra competition with $\beta_{ij} = a_ie_ja_j/q$ (Proposition 39.3.1); P\* rule; examples from reefs, dunes, squirrels and leaf miners. Intraguild predation (Definition 39.3.2): coexistence requires a superior competitor as intraguild prey and intermediate productivity.
- **Alternative stable states** and **regime shifts** (Definition 39.4.1) arise from positive feedbacks: lakes, reefs, kelp, drylands, budworm, permafrost. Scheffer lake model: folded equilibrium curve, stable where $\mathrm{d}E_0/\mathrm{d}V < 0$, bistable for $5.15 < E_0 < 7.29$ (Proposition 39.4.1); hysteresis.
- Near a fold $\lvert\lambda\rvert \propto \lvert c - c_c\rvert^{1/2}$ (Proposition 39.4.2). Critical slowing down (Definition 39.4.2): variance $\sigma^2/(2\lvert\lambda\rvert)$ and lag-$\Delta$ autocorrelation $\mathrm{e}^{\lambda\Delta}$ increase before the shift (Proposition 39.4.3); evidence from Peter Lake and yeast; many shifts give no warning.
- Restoration must overcome hysteresis: biomanipulation with nutrient reduction; management of slow variables that set resilience.

## Questions

1. In the four-level chain of Figure 1 ($r = a_i = 1$, $e_i = 0.5$, $m_i = 0.1$), compute the equilibrium of all four levels at $K = 2$ and check the values reached in Figure 1B.

   **Answer** With four levels, $X_3^* = m_4/(e_3a_3) = 0.2$; then $X_1^* = (m_2 + a_2X_3^*)/(e_1a_1) = (0.1 + 0.2)/0.5 = 0.6$; the plant equation gives $X_2^* = r(1 - X_1^*/K)/a_1 = 1 - 0.3 = 0.7$; and $X_4^* = (e_2a_2X_2^* - m_3)/a_3 = 0.35 - 0.1 = 0.25$. Before the invasion (three levels), $X_2^* = 0.2$, $X_1^* = K(1 - 0.2) = 1.6$, $X_3^* = 0.5\cdot1.6 - 0.1 = 0.7$. The invasion therefore lowers plants from 1.6 to 0.6, raises herbivores from 0.2 to 0.7 and lowers carnivores from 0.7 to 0.2, as in the figure.

2. Show that in (39.1) with $n = 2$ the Lyapunov function of Theorem 39.2.1 reduces to the one used for the predator–prey model with logistic prey, and explain why the proof fails if the plants grow exponentially ($K = \infty$).

   **Answer** For $n = 2$, $V = (X_1 - X_1^* - X_1^*\ln(X_1/X_1^*)) + (1/e_1)(X_2 - X_2^* - X_2^*\ln(X_2/X_2^*))$, the standard function for the Lotka–Volterra predator–prey system with logistic prey ([7.19.25](/7.19.25)). Its derivative is $-(r/K)u_1^2$. With $K = \infty$, $\dot V = 0$ identically: $V$ is a first integral, and the orbits are the closed neutral cycles of the classical Lotka–Volterra model, so there is no convergence; self-limitation of the plants is what makes the chain globally stable.

3. In the model (39.2), suppose $q = 0$ and both prey have very large carrying capacities. Prey 1 has $r_1 = 0.8$, $a_1 = 0.4$; prey 2 has $r_2 = 0.5$, $a_2 = 0.2$. Which prey wins, and why? What would change if the predator also had a refuge-dependent attack rate on prey 2?

   **Answer** $P_1^* = r_1/a_1 = 2$ and $P_2^* = r_2/a_2 = 2.5$. Prey 2 tolerates the higher predator density, so it excludes prey 1 by the P\* rule: with prey 2 present the predator settles at 2.5, at which prey 1 has growth rate $0.8 - 0.4\cdot2.5 = -0.2 < 0$. Although prey 1 grows faster, it is too vulnerable. A refuge that lowers the attack rate on prey 2 further would increase $P_2^*$ and strengthen its advantage; a refuge for prey 1 (lowering $a_1$ below $0.32$) would reverse the outcome, since then $P_1^* > 2.5$. Coexistence requires some self-limitation of the prey or of the predator, or differences in how the prey are found (enemy-free space).

4. Using Proposition 39.4.3, by what factor does the stationary variance of a system increase when the distance to a fold is reduced by a factor of 100? Why might variance nevertheless fail as an early warning in a real ecosystem?

   **Answer** $\lvert\lambda\rvert \propto \lvert c - c_c\rvert^{1/2}$ decreases by a factor of 10, so the variance $\sigma^2/(2\lvert\lambda\rvert)$ increases by a factor of 10 (and the return time by 10). It may fail because (1) the noise intensity $\sigma$ may change at the same time, (2) the linear approximation breaks down close to the fold, where a large fluctuation can cause an early transition (noise-induced tipping), (3) the shift may not be a fold at all, (4) observation error and short or sparse time series make trends in variance undetectable, and (5) the slow change of conditions may be too fast for the system to equilibrate, so that the indicators lag.

5. A shallow lake became turbid after decades of agricultural runoff. Phosphorus inputs have since been halved, but the lake remains turbid. Explain with the lake model, and propose a restoration strategy.

   **Answer** The lake is in the bistable range: the reduced loading corresponds to an $E_0$ below the upper fold (where the collapse happened) but above the lower fold, so the turbid state is still stable (hysteresis, Figure 3A). In addition, phosphorus stored in the sediments is released and keeps the effective loading high for years. Strategy: reduce inputs further, ideally below the lower threshold; reduce internal loading (sediment removal or phosphorus binding); and push the system into the clear basin by biomanipulation, removing planktivorous and benthivorous fish and stocking piscivores, possibly with temporary protection or planting of submerged vegetation. Monitor water clarity, zooplankton size and vegetation; expect relapse if loading stays near the threshold.

6. (Open question) The return of wolves to Yellowstone National Park in 1995 has been described as initiating a trophic cascade from wolves to elk to aspen and willow. What evidence would be needed to establish such a cascade, and what alternative explanations should be considered?

   **Answer** Evidence: time series of wolf and elk abundance and of browsing intensity and plant recruitment, before and after reintroduction, with spatially replicated comparisons; experimental exclosures showing that browsing limits the plants; tests of whether reduced browsing is due to fewer elk (density-mediated) or changed elk behavior in risky places (trait-mediated), for example by comparing browsing in places of high and low predation risk at equal elk density. Alternatives: elk declines also caused by human hunting outside the park, increasing bear and cougar predation, and drought; plant recovery caused by changes in climate and stream hydrology, by beaver activity, or by regression to the mean in heavily browsed stands; sampling bias towards tall, visible plants. Several studies found weaker and more local effects than first reported, so the cascade is plausible but its strength is debated.
