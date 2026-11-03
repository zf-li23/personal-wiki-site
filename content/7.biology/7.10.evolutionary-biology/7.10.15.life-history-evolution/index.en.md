---
title: Life History Evolution
description: "How natural selection shapes survival and reproduction at each age: trade-offs and the cost of reproduction; fitness in age-structured populations (life tables, the Euler–Lotka equation, Leslie matrices, reproductive value and Hamilton's sensitivities); r- and K-selection; semelparity and Cole's paradox, age at maturity, clutch size and the Smith–Fretwell model, bet hedging and sex change; specialists and generalists, Levins's fitness sets and specialization without trade-offs."
---

Species differ enormously in how they live and reproduce. A Greenland shark (*Somniosus microcephalus*) lives at least 272 years, a bristlecone pine in California more than 5000, while some rotifers live fewer than 20 days. Oysters release millions of tiny eggs at a time; a kiwi (*Apteryx*) lays a single egg a quarter of its own weight. Some salmon (*Oncorhynchus*) and century plants (*Agave*) reproduce once and die; humans reproduce repeatedly; periodical cicadas feed underground for 13 or 17 years, emerge, reproduce and die within a month. These features, the ages at which reproduction begins and ends, the number and size of offspring and the probability of survival to each age, are the components of fitness itself, so their diversity poses a sharp question: if selection favors higher survival and fecundity, how can short lives and few offspring evolve?

The answer lies in **trade-offs** (7.10.3): resources spent on one function are unavailable for another, so selection optimizes a compromise, and the best compromise depends on the ecology of each species. This chapter develops the demographic theory of fitness in age-structured populations, using the **life table** of survival analysis ([7.7.16](/7.7.16#sec-16.4)), the **Euler–Lotka equation** ([7.5.34](/7.5.34#sec-34.3)) and the Perron–Frobenius theory of nonnegative matrices ([Theorem 7.6.1](/1.4.7#thm-7.6.1)), and then applies it to the classic problems of life history evolution. The evolution of aging, which follows from the same theory, is developed in [7.5.37](/7.5.37#sec-37.2); here we derive only the decline in the force of selection with age on which it rests. The chapter ends with a broader component of a species' life history, its ecological niche: why some species are specialists and others generalists. Many examples come from evolutionary ecology; the population ecology itself belongs to 7.19.

## 15.1. Life History Traits as Components of Fitness

### 15.1.1. Allocation and Trade-offs

**Definition 15.1.1 (Life History)** The **life history** of an organism is its schedule of survival and reproduction: the ages at first and last reproduction, the fecundity at each age, the size and number of offspring, and the survival to each age. *Life history traits* are the traits that determine these rates.

An organism acquires a limited amount of energy and nutrients from its environment and allocates it among self-maintenance (hence survival), growth and reproduction. Growth is ultimately an investment in future survival and reproduction.

**Definition 15.1.2 (Reproductive Effort and Cost of Reproduction)** **Reproductive effort** is the fraction of an organism's resources, in a given period, that is allocated to reproduction. The **cost of reproduction** is the decrease in future survival, growth or fecundity caused by present reproduction.

The cost of reproduction is the most important trade-off of life history theory, but it is not always easy to see. If genotypes differ in how they *allocate* a fixed amount of resources between reproduction and survival, the genetic correlation between the two is negative; if they differ in how much they *acquire*, individuals that obtain more resources both survive and reproduce better, and the correlation is positive (van Noordwijk and de Jong 1986). The observed correlation depends on the relative amounts of variation in acquisition and allocation. In the seed beetle *Callosobruchus maculatus*, whose females can lay eggs without feeding, families showed a positive genetic correlation between fecundity and survival when the females were fed (variation in acquisition dominated) but a negative correlation, a cost of reproduction, when they were deprived of food.

![Acquisition and allocation (the Y model of van Noordwijk and de Jong). Each of 300 simulated individuals acquires resources A (lognormal) and allocates a fraction x to reproduction (logit-normal), so that reproduction is Ax and survival investment A(1 − x). A: when individuals vary much more in acquisition than in allocation, reproduction and survival are positively correlated across individuals, although each faces a trade-off. B: when they vary mainly in allocation, the trade-off appears as a negative correlation](./plots/acquisition-allocation.py)

Experiments that manipulate reproduction directly avoid this difficulty. Female brown anoles (*Anolis sagrei*) whose ovaries were surgically removed grew more and survived better over two years than sham-operated females, although this species lays only one egg per clutch (Cox and Calsbeek). Sterilized female *Drosophila* live longer; blue tits (*Cyanistes caeruleus*) given extra eggs to rear are more likely to die over the following winter and produce fewer fledglings the next year; and in the Soay sheep of St Kilda, castrated males, which do not compete in the rut, live as long as females, while intact males mostly die in their first winter.

### 15.1.2. Fitness in Age-Structured Populations

Fitness in a population with overlapping generations must combine survival and fecundity at all ages. Let $l_x$ be the probability that a newborn survives to age $x$ ($l_0 = 1$) and $m_x$ the mean number of offspring produced at age $x$ (counting, in a sexual population, half of the offspring to each parent or only daughters of females).

**Definition 15.1.3 (Net Reproductive Rate)** The *net reproductive rate* (lifetime reproductive success) is
$$
R_0 = \sum_x l_x m_x,
$$
the expected number of offspring produced by a newborn over its lifetime. A population with $R_0 > 1$ grows, one with $R_0 < 1$ declines.

**Example 15.1.1 (An Asexual Lizard)** A lizard reproduces at ages 2 and 3 and never lives to age 4, with the following life table:

| Age $x$ | $l_x$ | $m_x$ | $l_xm_x$ |
|---|---|---|---|
| 0 | 1 | 0 | 0 |
| 1 | 0.75 | 0 | 0 |
| 2 | 0.5 | 1 | 0.5 |
| 3 | 0.25 | 2 | 0.5 |

Then $R_0 = 1$: each female exactly replaces herself. A mutation that raises fecundity at age 2 from 1 to 1.2 raises $l_2m_2$ to 0.6 and $R_0$ to 1.1; the same increase at age 3 raises $l_3m_3$ to 0.55 and $R_0$ only to 1.05, because fewer individuals survive to age 3. A mutation that raises survival from age 3 to age 4 has no effect on fitness at all, because there is no reproduction after age 3.

$R_0$ is a good measure of fitness only when the population is roughly stationary. In a growing population the timing of reproduction matters: offspring produced early start reproducing earlier themselves. Two lizards both have $R_0 = 2$; one produces two offspring at age 1 and dies, the other produces two at age 2. After two years the first has four descendants and the second two. The right measure is the growth rate of a genotype's descendants.

**Definition 15.1.4 (Intrinsic Rate of Increase)** The **intrinsic rate of increase** $r$ of a population (or genotype) with stable age structure is the per capita rate of increase per unit time, $r = \ln\lambda$, where the finite rate of increase $\lambda$ is the unique positive root of the discrete Euler–Lotka equation
$$
\sum_{x \geq 1} \lambda^{-x} l_x m_x = 1 . \tag{15.1}
$$
When $\lambda$ is close to 1, $r \approx (\ln R_0)/T$, where $T$ is the generation time (the mean age of the mothers of newborns).

The left side of Eq. (15.1) decreases strictly from $+\infty$ to 0 as $\lambda$ increases from 0, so the positive root is unique; it exceeds 1 exactly when $R_0 > 1$. For the two lizards, $2\lambda^{-1} = 1$ gives $\lambda = 2$, and $2\lambda^{-2} = 1$ gives $\lambda = \sqrt 2 \approx 1.41$: early reproduction wins. In a growing population, selection favors early reproduction. Weedy plants that colonize disturbed habitats, where populations grow fast and then disperse before they are replaced, mature early: common ragweed (*Ambrosia artemisiifolia*) flowers four to five months after germinating, while some oaks do not reproduce for decades.

### 15.1.3. The Leslie Matrix and Reproductive Value

The same demography can be written as a linear map. Census a population just after breeding, with $n_x(t)$ individuals of age $x$, $x = 0, 1, \dots, \omega$. Individuals of age $x$ survive to age $x + 1$ with probability $p_x = l_{x+1}/l_x$, and those that do produce $m_{x+1}$ newborns at the next census.

**Definition 15.1.5 (Leslie Matrix)** The *Leslie matrix* of a life history is the nonnegative matrix
$$
L = \begin{bmatrix}
F_0 & F_1 & \cdots & F_{\omega - 1} & F_\omega \\
p_0 & 0 & \cdots & 0 & 0 \\
0 & p_1 & \cdots & 0 & 0 \\
\vdots & & \ddots & & \vdots \\
0 & 0 & \cdots & p_{\omega - 1} & 0
\end{bmatrix}, \qquad F_x = p_x m_{x+1},
$$
with $\boldsymbol{n}(t + 1) = L\boldsymbol{n}(t)$ for the vector $\boldsymbol{n}(t)$ of numbers by age.

**Theorem 15.1.1 (Growth Rate, Stable Age Distribution and Reproductive Value)** Let $L$ be a Leslie matrix with all $p_x > 0$ whose fecundities are positive at two ages with greatest common divisor 1. Then (a) the dominant **eigenvalue** of $L$ is the positive root $\lambda$ of Eq. (15.1), and every population with some individuals of reproductive age eventually grows as $\boldsymbol{n}(t) \approx c\lambda^t\boldsymbol{w}$; (b) the right eigenvector $\boldsymbol{w}$ is the stable age distribution, $w_x \propto \lambda^{-x}l_x$; (c) the left eigenvector $\boldsymbol{v}$ gives the reproductive value of each age class,
$$
v_x \propto \frac{\lambda^x}{l_x}\sum_{y > x}\lambda^{-y}l_y m_y ;
$$
(d) the sensitivity of $\lambda$ to an entry $L_{ij}$ is $\partial\lambda/\partial L_{ij} = v_i w_j/\langle\boldsymbol{v}, \boldsymbol{w}\rangle$.

**Proof** (a), (b) Suppose $L\boldsymbol{w} = \lambda\boldsymbol{w}$. The subdiagonal rows give $w_{x+1} = p_xw_x/\lambda$, so $w_x = w_0\lambda^{-x}l_x$. The first row then gives $\lambda w_0 = \sum_x p_xm_{x+1}w_0\lambda^{-x}l_x = w_0\sum_x\lambda^{-x}l_{x+1}m_{x+1}$, which is Eq. (15.1) after shifting the index. Under the stated conditions $L$ is irreducible and primitive, so by the Perron–Frobenius theorem this positive eigenvalue is simple and strictly larger in modulus than all others, which gives the asymptotic growth. (c) Similarly $\boldsymbol{v}^{\mathsf T}L = \lambda\boldsymbol{v}^{\mathsf T}$ gives $\lambda v_x = F_xv_0 + p_xv_{x+1}$; solving from the oldest age downward yields the stated sum. (d) Differentiating $L\boldsymbol{w} = \lambda\boldsymbol{w}$ and multiplying on the left by $\boldsymbol{v}^{\mathsf T}$ gives $\boldsymbol{v}^{\mathsf T}(\mathrm{d}L)\boldsymbol{w} = \mathrm{d}\lambda\,\langle\boldsymbol{v}, \boldsymbol{w}\rangle$. $\square$

**Definition 15.1.6 (Reproductive Value)** The **reproductive value** $v_x$ of an individual of age $x$ (Fisher 1930) is its expected contribution to the future growth of the population, relative to that of a newborn: the offspring it can still expect to produce after the present census, discounted by the growth rate $\lambda$ and divided by its probability $l_x$ of having survived to age $x$. Fisher's original definition, for an individual about to breed at age $x$, also counts the reproduction at age $x$ itself.

For the lizard of Example 15.1.1 ($\lambda = 1$, census just after breeding), $v_0 = 1$, $v_1 = (0.5 + 0.5)/0.75 = 1.33$, $v_2 = 0.5/0.5 = 1$ and $v_3 = 0$; counted just before breeding, as in Fisher's definition, the values are $1$, $1.33$, $2$ and $2$. Reproductive value usually rises until the age of first reproduction, because survival through the juvenile period is no longer in question, and then falls as the remaining reproduction is used up. Natural selection on behaviors that risk survival should weigh them by reproductive value: an old individual with little reproductive value left can afford risks that a young adult cannot.

### 15.1.4. The Force of Selection Declines with Age

The sensitivities of Theorem 15.1.1 measure the strength of selection on survival and fecundity at each age, since a mutation that changes a vital rate changes the growth rate of its carriers by the sensitivity times the size of the change.

**Theorem 15.1.2 (Hamilton's Forces of Selection)** Let $T = \sum_x x\lambda^{-x}l_xm_x$ be the generation time. The sensitivities of $\lambda$ to fecundity at age $x$ and to the logarithm of survival from age $a$ to $a + 1$ are
$$
\frac{\partial\lambda}{\partial m_x} = \frac{\lambda\,\lambda^{-x}l_x}{T}, \qquad \frac{\partial\lambda}{\partial\ln p_a} = \frac{\lambda}{T}\sum_{x > a}\lambda^{-x}l_xm_x .
$$
The first decreases with age as $\lambda^{-x}l_x$; the second is constant up to the age of first reproduction and then declines, reaching zero at the last age of reproduction.

**Proof** Write $\Phi(\lambda, \boldsymbol{m}, \boldsymbol{p}) = \sum_x\lambda^{-x}l_xm_x - 1 = 0$ and differentiate implicitly: $\partial\lambda/\partial\theta = -(\partial\Phi/\partial\theta)/(\partial\Phi/\partial\lambda)$, with $\partial\Phi/\partial\lambda = -\sum_x x\lambda^{-x-1}l_xm_x = -T/\lambda$. For $\theta = m_x$, $\partial\Phi/\partial m_x = \lambda^{-x}l_x$. For $\theta = \ln p_a$, since $l_x = \prod_{y < x}p_y$, every $l_x$ with $x > a$ is multiplied by the same factor, so $\partial\Phi/\partial\ln p_a = \sum_{x > a}\lambda^{-x}l_xm_x$. Before the first age of reproduction this sum is the whole of $\sum_x\lambda^{-x}l_xm_x = 1$. $\square$

This is the discrete form of the selection shadow of [Formula 37.2.1](/7.5.37#fml-37.2.1). In the lizard example ($\lambda = 1$, $T = 2 \cdot 0.5 + 3 \cdot 0.5 = 2.5$), $\partial\lambda/\partial m_2 = 0.5/2.5 = 0.2$ and $\partial\lambda/\partial m_3 = 0.25/2.5 = 0.1$, which reproduces the twofold difference of Example 15.1.1. Because selection on late-acting effects is weak, deleterious mutations that act late accumulate (**mutation accumulation**, Medawar) and alleles that improve early performance at a late cost are favored (**antagonistic pleiotropy**, Williams); both lead to the evolution of **aging** ([Definition 37.2.1](/7.5.37#def-37.2.1)). The genetic variance in reproductive success of *Drosophila melanogaster* increases with age, as mutation accumulation predicts, and inbreeding depression in several birds and mammals is greater at later ages. *Drosophila* populations selected for late reproduction evolved higher late fecundity and longer life but lower early fecundity, as antagonistic pleiotropy predicts. Many biologists consider antagonistic pleiotropy the more important factor, but both contribute, and both involve many genes, so that no single cause of senescence is expected.

![Hamilton's forces of selection (Theorem 15.1.2) for a hypothetical life history in which individuals mature at age 2, produce 1.5 offspring per year and survive each year with probability 0.4 as juveniles and 0.7 (black) or 0.9 (colored) as adults. A: sensitivity of the growth rate λ to the logarithm of survival at each age: constant before maturity, then declining. B: sensitivity of λ to fecundity at each age, proportional to λ^(−x)l_x. With higher adult survival, selection remains strong to older ages](./plots/leslie-sensitivity.py)

## 15.2. Population Growth and Density

The vital rates in a life table depend on the environment, including the density of the population itself. As resources are depleted, predators attracted and diseases spread, the per capita growth rate falls: in the simplest model of **logistic growth** ([2.2.15](/2.2.15)) it declines linearly from its maximum $r_m$ at low density to zero at the carrying capacity $K$,
$$
\frac{\mathrm{d}N}{\mathrm{d}t} = r_mN\left(1 - \frac{N}{K}\right).
$$
Which genotype has the highest fitness then depends on the density at which the population usually lives (MacArthur 1962).

**Definition 15.2.1 (r-Selection and K-Selection)** **r-selection** is selection in populations that are usually far below carrying capacity, as in colonizing species or after frequent disturbance, which favors a high maximum rate of increase $r_m$: early reproduction and high fecundity. **K-selection** is selection in populations that are usually near carrying capacity, which favors the ability to persist and reproduce under crowding, raising $K$, often at the cost of a lower $r_m$.

At low density the genotype with the higher $r_m$ increases faster; near equilibrium, a genotype that can keep a positive growth rate at a density at which the other cannot, that is, one with a higher $K$, replaces it. Experimental populations of *Drosophila serrata* maintained on a constant supply of food evolved steadily higher population densities, a sign of adaptation to crowding. In the streams of Trinidad, guppies (*Poecilia reticulata*) living with the predatory cichlid *Crenicichla* suffer high mortality and live at low density, while those above waterfalls, where predators are absent, live at high density and compete for food (Reznick and colleagues). Reared in a common environment, guppies from high-predation sites mature earlier and produce more offspring, as expected under r-selection, and the growth rate of populations from low-predation sites is less depressed by high density. Guppies transplanted into predator-free streams rapidly evolved the low-predation life history.

![Density-dependent selection (Definition 15.2.1). Two clones grow logistically with competition for the same resources, dN_i/dt = r_i N_i [1 − (N_A + N_B)/K_i]: clone A has r = 1, K = 100, clone B has r = 0.5, K = 150; both start with one individual. A: numbers of the two clones; A increases faster at first, but once the population approaches 100 only B can still grow, and A is excluded. B: the frequency of clone B dips while the population is growing and then rises to fixation](./plots/r-K-selection.py)

The r/K scheme organized much early work but has largely been replaced by demographic theory based on age-specific mortality (Section 15.1.4), because density acts on particular ages and vital rates, and the scheme's predictions do not follow from density dependence alone. Its lasting legacy is the observation that life histories covary: across species, traits fall along a *fast–slow continuum*, from early maturation, short life and many small offspring to late maturation, long life and few large offspring.

## 15.3. Diverse Life Histories

### 15.3.1. Reproducing Once or Repeatedly

**Definition 15.3.1 (Semelparity and Iteroparity)** In **semelparity** an organism reproduces once in its life and then dies (annual plants, Pacific salmon, agaves, bamboos); in **iteroparity** it reproduces repeatedly (most perennial plants and vertebrates).

Cole (1954) noticed that iteroparity seems to give surprisingly little advantage.

**Theorem 15.3.1 (Cole's Paradox and Its Resolution)** Consider an annual (semelparous) genotype that produces $B_a$ offspring and dies, and a perennial (iteroparous) genotype that produces $B_p$ offspring each year. Let offspring survive to reproduce with probability $c$ and perennial adults survive each year with probability $p$. Then the finite rates of increase are
$$
\lambda_a = cB_a, \qquad \lambda_p = cB_p + p,
$$
and semelparity is favored if and only if $B_a > B_p + p/c$. If $c = p = 1$, as in Cole's original argument, an annual that produced just one more offspring than a perennial would grow as fast: $B_a = B_p + 1$.

**Proof** Census just before breeding. For the annual, each breeder is replaced by its $cB_a$ surviving offspring. For the perennial, each breeder leaves $cB_p$ surviving offspring and itself survives with probability $p$, so $N_{t+1} = (cB_p + p)N_t$. $\square$

The resolution (Charnov and Schaffer 1973) is that juvenile and adult survival differ. When juvenile survival $c$ is low and adult survival $p$ high, a surviving adult is worth many seeds, $p/c$ is large, and iteroparity is strongly favored; this is the usual situation in trees and long-lived vertebrates. Semelparity is favored when adults have little chance of reproducing again, or when the number of offspring increases so steeply with the effort that all-out reproduction pays: when fecundity rises exponentially with body size and survival increases with size, delaying reproduction and then reproducing massively can maximize fitness. The terrestrial bromeliad *Puya dasylirioides* produces exponentially more fruits as its rosette grows; agaves, bamboos and the cabbage palm *Corypha utan* reproduce once after many years, producing enormous numbers of seeds, and then die. The semelparous Amazonian tree *Tachigali vasquezii* grows unusually fast, by making low-density wood, which reduces its risk of dying before it reproduces. Coho salmon (*Oncorhynchus kisutch*) migrate from the sea up rivers to spawn, shut down their immune defenses and other functions, and die after spawning: the hazardous migration makes a second reproduction unlikely. Iteroparity is also favored in fluctuating environments, where spreading reproduction over several seasons reduces the variance of lifetime success, a form of **bet hedging** ([Definition 17.1.2](/7.9.17#def-17.1.2)): selection in a variable environment maximizes the **geometric mean** of fitness across years, which is reduced by variance. As expected, reproductive effort per episode is lower in iteroparous species: inflorescences make up a smaller fraction of plant mass in perennial than in annual grasses.

### 15.3.2. Age at Maturity

Delaying reproduction has a cost, the risk of dying before reproducing and a longer generation time, and benefits when fecundity increases with age or size, as in plants and fishes that grow throughout life, or when experience improves parental care. Theory predicts delayed maturity where adult survival is high relative to juvenile survival, and among species of snakes and lizards, those with lower adult mortality mature later (Shine and Charnov 1992). The guppies of Section 15.2 show the experimental side: higher adult mortality from predators favored earlier maturity.

### 15.3.3. Number and Size of Offspring

All else equal, higher fecundity means higher fitness. Lack (1947) proposed that the clutch size of birds evolves to the number of eggs that yields the greatest number of surviving offspring: parents cannot feed large broods adequately, so the survival of each nestling falls with brood size. Later work added the costs of large broods to the parents' own survival and future reproduction, which favor clutches somewhat smaller than Lack's prediction. In a long-term study of great tits (*Parus major*) in the Netherlands, in which brood sizes were manipulated by moving hatchlings among nests, enlarged broods had lower survival in the nest and after fledging, and the parents were less likely to lay a second clutch; the clutch size estimated to maximize fitness was 8.9 eggs, close to the observed mean of 9.2.

At a given reproductive effort there is a trade-off between the number and the size of offspring.

**Theorem 15.3.2 (Smith–Fretwell Optimal Offspring Size)** Let a parent have an amount $R$ of resources for reproduction and let an offspring that receives an amount $s$ survive to reproduce with probability $f(s)$, an increasing function with $f(s) = 0$ below some minimum size. If the parent makes $R/s$ offspring of size $s$, its fitness is $W(s) = (R/s)f(s)$, and the optimal offspring size $s^*$ satisfies
$$
f'(s^*) = \frac{f(s^*)}{s^*},
$$
so that the line from the origin to the point $(s^*, f(s^*))$ is tangent to the curve $f$. The optimum does not depend on $R$: parents with more resources should make more offspring, not larger ones (Smith and Fretwell 1974).

**Proof** $\ln W = \ln R - \ln s + \ln f(s)$, so $\mathrm{d}\ln W/\mathrm{d}s = -1/s + f'(s)/f(s) = 0$ gives the condition; $R$ does not appear. Geometrically, $f(s)/s$ is the slope of the line from the origin to $(s, f(s))$, which is maximal where the line touches the curve. $\square$

Large offspring are favored where starting life at a large size greatly increases survival. Among tropical trees, species whose seedlings establish in deep shade have larger seeds than those that germinate in light gaps, and trees and vines, which mostly establish in closed forest, have larger seeds on average than herbs and grasses of open habitats. At the extremes, orchid seeds are microscopic and can grow only in association with a mycorrhizal fungus, while a coconut can weigh 20 kg. Among birds and mammals, the largest offspring relative to adult size occur in species with a single offspring at a time, such as kiwis, albatrosses, elephants and humans.

![Two classic life history models. A: Cole's paradox resolved (Theorem 15.3.1): the extra offspring an annual must produce to match a perennial, B_a − B_p = p/c, as a function of adult survival p, for juvenile survival c = 1 (Cole's case), 0.5 and 0.1; when juvenile survival is low, iteroparity is strongly favored. B: the Smith–Fretwell model (Theorem 15.3.2) with a sigmoid offspring fitness f(s): parental fitness (R/s)f(s) is maximal where the line from the origin is tangent to f, at s* (dashed)](./plots/cole-smith-fretwell.py)

### 15.3.4. Life Histories and Mating Strategies

Males too pay costs of reproduction, and the different relations between size and reproductive success in the two sexes explain sex change. In the *size-advantage model* (Ghiselin 1969), sequential hermaphroditism is favored in organisms that grow throughout life when reproductive success increases with size faster in one sex than in the other: an individual should first function as the sex whose success depends less on size and change sex when it is large. In the bluehead wrasse (*Thalassoma bifasciatum*), large terminal-phase males defend territories and mate with many females, so male success rises steeply with size, and individuals start as females and become males (*protogyny*). In the slipper shell *Crepidula fornicata*, egg production rises steeply with size, small individuals are males, and the largest male in a stack becomes female when the female at its base dies (*protandry*); many cucurbits produce male flowers when small and female flowers when large, since pollen is much cheaper than seeds. Across sex-changing animals, sex change usually occurs at about 70 percent of maximum size, as the theory predicts.

## 15.4. Specialists and Generalists

### 15.4.1. Niche Width

A broader notion of life history includes how an organism uses its environment: its habitats, foods and tolerances.

**Definition 15.4.1 (Ecological Niche)** The **ecological niche** of a species is the set of environmental conditions under which it can persist and the resources it uses; Hutchinson (1957) formalized it as a region (hypervolume) in the space of environmental variables in which the population growth rate is positive. *Niche width* is the extent of this region: specialists have narrow niches and generalists broad ones.

The caterpillar of the juniper geometer (*Patalene olyzonaria*) feeds only on juniper, while that of the fall cankerworm (*Alsophila pometaria*), in the same family, feeds on oaks, maples, cherries and many other trees; some marine crabs are restricted to full-strength seawater while related species also live in brackish estuaries. The range of conditions tolerated often matches the variability of the environment. Temperate-zone species of *Drosophila*, frogs and other ectotherms have broader thermal tolerances than tropical species, but mostly because they tolerate lower temperatures; the critical thermal maximum varies little with latitude, which suggests that it is close to an evolutionary limit and that tropical species already living near it are especially vulnerable to warming.

### 15.4.2. Why Specialize?

Since environments vary, one might expect broad tolerance always to be favored. Several factors favor specialization. Plasticity, which often underlies broad tolerance, has costs: of producing the alternative phenotype, of maintaining the capacity to do so, and of errors when cues are unreliable. Interactions with other species can favor the use of resources that competitors do not use (7.10.17) or of "enemy-free space": herbivorous insects often suffer less predation and parasitism on some host plants than on others. But the most strongly supported hypothesis is that of trade-offs: "a jack of all trades is master of none".

**Theorem 15.4.1 (Levins's Fitness Set)** Let a phenotype $x$ have fitness $W_1(x)$ in environment 1 and $W_2(x)$ in environment 2, and let the population experience the environments in proportions $q$ and $1 - q$ within each generation, so that fitness is $W(x) = qW_1(x) + (1 - q)W_2(x)$. The *fitness set* is the curve $\{(W_1(x), W_2(x))\}$ of attainable combinations. The optimal phenotype is the point of the fitness set touched by the highest line $qW_1 + (1 - q)W_2 = \text{const}$. If the fitness set is convex (the trade-off is weak: intermediate phenotypes do reasonably well in both environments), the optimum is an intermediate generalist; if it is concave (the trade-off is strong), the optimum lies at an end of the set, a specialist on the more common or more profitable environment (Levins 1968).

**Proof** Maximizing a linear function over a curve: the maximum is at the point where a level line is tangent to the curve, provided the curve bulges outward (a convex set); if the curve bends inward (concave), any tangent point is a minimum along the curve, and the maximum is at an endpoint. $\square$

Trade-offs of this kind have been demonstrated in many organisms. Flowerpiercers (*Diglossa*) are tropical birds whose hooked bills hold tubular flowers while they pierce them to steal nectar; when the hook was clipped experimentally, the birds took nectar less efficiently but ate berries, the main food of related species with less hooked bills, more efficiently. The copepod *Eurytemora affinis*, which has invaded the North American Great Lakes from saline waters, shows strong negative genetic correlations between survival in fresh and in saline water. Elizabeth Bernays proposed that host specialization in herbivorous insects reflects a limit on neural processing; an aphid that is a host specialist in the eastern United States but a generalist in the West found its host among non-hosts and began feeding faster in its specialist populations.

![Levins's fitness set (Theorem 15.4.1). Each curve shows the attainable combinations of fitness in two environments as a phenotype x varies from a specialist on environment 2 (x = 0) to a specialist on environment 1 (x = 1), with W₁ = 1 − (1 − x)^k and W₂ = 1 − x^k. Dashed lines are contours of mean fitness 0.6W₁ + 0.4W₂ (environment 1 is more common); the dot marks the optimum. A: weak trade-off (k = 2, convex set): an intermediate generalist is optimal. B: strong trade-off (k = 0.5, concave set): the specialist on the common environment is optimal](./plots/fitness-set.py)

### 15.4.3. Specialization Without Trade-offs

Many studies, however, find no evidence of trade-offs: the growth and survival of genotypes of herbivorous insects reared on two or more plants are seldom negatively correlated. Specialization can evolve anyway. When a population occupies a common and a rare environment and mates at random, the strength of selection on an allele that improves fitness in one environment is proportional to the fraction of the population that experiences it. Adaptation to the common environment therefore proceeds faster than adaptation to the rare one, and once the population is better adapted to the common environment, alleles for preferring it are favored too. As the population becomes confined to the majority environment, mutations that disable adaptations to the minority environment become nearly neutral and may accumulate by drift (mutational decay). Experimental evolution confirms both routes: populations of *Escherichia coli* propagated for 20 000 generations on glucose lost the ability to grow on several other substrates, apparently mainly by antagonistic pleiotropy, while in *Pseudomonas fluorescens* the unused swimming motility was lost at a rate that depended on food supply, by drift when resources were plentiful and by selection, which saves the cost of motility, when they were limiting. Bacterial populations kept in variable environments, by contrast, evolve broader niches, either as generalist genotypes or as mixtures of specialists.

Niche evolution is often slow on longer time scales: related species tend to retain similar niches, a pattern called **phylogenetic niche conservatism** (7.10.26), which affects how species respond to climate change and how communities are assembled (7.10.17).

## Summary

- **Life history** traits are the components of fitness; their evolution is governed by trade-offs, especially the **cost of reproduction** (Definitions 15.1.1, 15.1.2). Variation in acquisition can mask allocation trade-offs, which experiments reveal (ovariectomized anoles, brood manipulation, castrated Soay rams).
- Fitness in age-structured populations: $R_0 = \sum l_xm_x$ (Definition 15.1.3); the growth rate $\lambda = \mathrm{e}^r$ solves $\sum\lambda^{-x}l_xm_x = 1$, Eq. (15.1), and is the dominant eigenvalue of the Leslie matrix (Theorem 15.1.1), whose eigenvectors are the stable age distribution and **reproductive value** (Definition 15.1.6). In growing populations early reproduction is favored.
- Hamilton's forces of selection (Theorem 15.1.2): $\partial\lambda/\partial m_x \propto \lambda^{-x}l_x$; sensitivity to survival is constant before maturity and declines afterwards. This underlies **mutation accumulation**, **antagonistic pleiotropy** and the evolution of **aging** ([7.5.37](/7.5.37)).
- Density: **r-selection** favors high $r_m$, **K-selection** high $K$ (Definition 15.2.1); guppies of high- and low-predation streams; the fast–slow continuum.
- **Semelparity** versus **iteroparity**: Cole's paradox, resolved by $B_a > B_p + p/c$ (Theorem 15.3.1); bet hedging in variable environments.
- Offspring: Lack's clutch size (great tits: 8.9 optimal vs 9.2 observed); Smith–Fretwell $f'(s^*) = f(s^*)/s^*$, independent of parental resources (Theorem 15.3.2); the size-advantage model of sex change.
- Niche width (Definition 15.4.1): specialization is favored by costs of plasticity, biotic interactions and trade-offs; with a linear adaptive function, convex fitness sets favor generalists and concave ones specialists (Theorem 15.4.1). Specialization also evolves without trade-offs, through asymmetric selection and mutational decay.

## Questions

1. Using Eq. (15.1), find the finite rate of increase $\lambda$ of a population with $l_1m_1 = 0.5$, $l_2m_2 = 0.6$ and no reproduction at other ages. By how much does $\lambda$ change if $m_1$ is increased by 10 percent?

   **Answer** Solve $0.5\lambda^{-1} + 0.6\lambda^{-2} = 1$, that is $\lambda^2 - 0.5\lambda - 0.6 = 0$, so $\lambda = (0.5 + \sqrt{0.25 + 2.4})/2 = (0.5 + 1.628)/2 = 1.064$. With $l_1m_1 = 0.55$: $\lambda = (0.55 + \sqrt{0.3025 + 2.4})/2 = (0.55 + 1.644)/2 = 1.097$, an increase of about 0.033. (Theorem 15.1.2 gives $T = 0.5/1.064 + 2 \cdot 0.6/1.064^2 = 0.470 + 1.060 = 1.530$ and $\Delta\lambda \approx \lambda\cdot\lambda^{-1}\cdot 0.05/T = 0.05/1.53 = 0.033$.)

2. Explain why, in the lizard of Example 15.1.1, a mutation that increases survival from age 3 to age 4 is selectively neutral, and what changes if the lizards cared for their grandchildren.

   **Answer** No reproduction occurs after age 3, so the survival of a lizard beyond 3 does not change $\sum\lambda^{-x}l_xm_x$; its sensitivity in Theorem 15.1.2 is zero. If old lizards increased the survival of their offspring's offspring, survival after age 3 would contribute to the fitness of their genes through relatives (indirect fitness, 7.10.16), and selection would favor it; this is the basis of the grandmother hypothesis for human menopause and of post-reproductive life in orcas.

3. In the Smith–Fretwell model, let $f(s) = 1 - \mathrm{e}^{-(s - s_0)}$ for $s > s_0$ (and 0 otherwise), with $s_0 = 1$. Find the optimal offspring size.

   **Answer** The condition $f'(s) = f(s)/s$ gives $s\mathrm{e}^{-(s - 1)} = 1 - \mathrm{e}^{-(s - 1)}$, that is $\mathrm{e}^{s - 1} = s + 1$. Numerically, $s = 2.146$ ($\mathrm{e}^{1.146} = 3.146$). The optimal size is a little more than twice the minimum viable size and does not depend on how much the parent has to invest.

4. Why does the r/K concept predict that colonizing weeds mature early and produce many small seeds, and why is the concept now considered insufficient?

   **Answer** Weeds live in disturbed patches where populations grow far below carrying capacity, so genotypes with the highest maximum rate of increase (early reproduction, high fecundity, short generation time) are favored, while competitive ability at high density matters little. The concept is insufficient because density-dependent selection alone does not determine which vital rates change: the predictions depend on which ages and processes density affects. Age-specific mortality theory (Hamilton's sensitivities, Cole and Charnov–Schaffer) gives more precise predictions; for example, high adult mortality favors early maturity, whatever the density.

5. (Open question) Fisheries often remove the largest individuals. Using the theory of this chapter, predict how harvested fish populations should evolve, and outline what data would test the prediction.

   **Answer** Key points: size-selective harvest raises adult mortality, especially of large, old individuals, which lowers the reproductive value of late life and the benefit of delaying reproduction. Theory (Section 15.3.2, Theorem 15.1.2) predicts evolution toward earlier maturation at smaller size, higher reproductive effort when young and slower growth; in protandrous species (which change from male to female) sex change at smaller size. Tests: long time series of age and size at maturity (probabilistic maturation reaction norms that separate genetic change from plastic responses to density and food), common-garden experiments with fish from harvested and unharvested stocks, and selection experiments in which the largest or smallest fish are removed each generation. Consequences include lower yields and slower recovery after fishing stops.
