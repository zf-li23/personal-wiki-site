---
title: "Demography: Life Tables, Survivorship and Reproduction"
description: Primary and secondary population parameters; cohort and static life tables and their columns; fecundity schedules; survivorship curves and the hazard function; net reproductive rate, generation time and the Euler–Lotka equation with its dominant root and the approximation r ≈ ln R₀/T; k values and key factor analysis; age pyramids and the age structure of human populations.
---

A population changes in size only through four processes: individuals are born, die, arrive and leave. Demography is the bookkeeping of these processes, and its central instrument, the **life table**, records how the chances of dying and of reproducing change over an individual's life. From a life table and a schedule of fecundity follow the three numbers that summarize a population's potential: the number of offspring an individual leaves in its lifetime ($R_0$), the length of a generation ($T$), and the rate of increase per unit time ($r$), linked by the **Euler–Lotka equation**. This chapter builds these tools for populations of organisms in the field. It follows the previous chapter on counting individuals (7.19.8) and provides the parameters of the growth models that come next: exponential and logistic growth (7.19.10), density dependence (7.19.11, 7.19.12) and matrix models of structured populations (7.19.14). The statistical side of life tables (censoring, hazard estimation, Kaplan–Meier curves) is treated in [7.7.16](/7.7.16#sec-16.4), and their evolutionary use, fitness in age-structured populations, in [7.10.15](/7.10.15#sec-15.1.2); here the emphasis is on what the tables reveal about the ecology of a population.

## 9.1. Population Parameters

A **population** (7.19.8) has properties that no individual has: a density, a birth rate, an age structure. These group properties are mostly statistical quantities, and they are of two kinds.

**Definition 9.1.1 (Demography)** *Demography* is the quantitative study of the birth, death, migration, sex ratio and age structure of populations. Its parameters fall into three groups:

1. the **population density**, the most basic property of a population;
2. the **primary population parameters**, which change the number of individuals directly: *natality* (the production of new individuals), *mortality* (deaths), *immigration* (individuals entering from elsewhere) and *emigration* (individuals leaving);
3. the **secondary population parameters**, which are derived from the primary ones: sex ratio, age structure and rate of increase.

The primary parameters combine in the balance equation of a population over an interval $(t, t+1]$,
$$
N_{t+1} = N_t + B - D + I - E, \tag{9.1}
$$
with $B$ births, $D$ deaths, $I$ immigrants and $E$ emigrants. Dividing by population size turns counts into rates. A *crude* rate divides the count by the mean population size in the interval (births per 1000 individuals per year, the "‰" of human demography); an *instantaneous* per capita rate is the limit of this ratio as the interval shrinks. With instantaneous birth and death rates $b$ and $d$, a closed population ($I = E = 0$) changes as $\mathrm{d}N/\mathrm{d}t = (b - d)N$, and $r = b - d$ is its instantaneous rate of increase (7.19.10). Mortality is therefore best expressed as an instantaneous rate: deaths in an interval divided by the mean number at risk and by the length of the interval.

Among the secondary parameters, the **sex ratio** ([7.10.13](/7.10.13#def-13.3.1)) of most animal populations is close to $1:1$, as Fisher's argument predicts. The exceptions are informative. Populations of rotifers and aphids that reproduce by parthenogenesis consist mostly or entirely of females for much of the year; a colony of ants, bees or wasps consists overwhelmingly of females (the workers), with males produced only seasonally; the sex of the amphipod *Gammarus duebeni* is determined by day length during development, so the population sex ratio varies with season; and the rice-field eel *Monopterus albus* changes sex from female to male as it grows, so older age classes are mostly male. The ecology of sex and the sex ratio is the subject of 7.19.21. Age structure and the rate of increase occupy the rest of this chapter.

## 9.2. Life Tables

### 9.2.1. Cohort and Static Life Tables

A life table can be built in two ways, which differ in how individuals of different ages are sampled. Picture each individual as a line in a diagram with time on the horizontal axis and age on the vertical axis: it starts at age 0 when it is born and rises at unit slope until it dies.

**Definition 9.2.1 (Cohort and Static Life Tables)** A **cohort** is a group of individuals born within the same interval of time. A **cohort life table** (dynamic life table) follows one cohort from birth until the last member dies, recording the number alive at the start of each age class. A **static life table** (time-specific life table) is constructed from the ages of all individuals alive at one time, or from the ages at death of individuals found dead over a short period, treating the numbers in successive age classes as if they were the survivors of a single cohort.

A cohort table follows one diagonal band of the diagram; a static table takes one vertical slice through all bands at once. The static table therefore mixes cohorts born at different times, and it describes the survival of a single cohort only under an assumption that is rarely checked.

**Proposition 9.2.1 (When a Static Life Table Is Valid)** Suppose that age-specific survival $l_x$ has been the same for all cohorts and that the number of births has changed geometrically, $B_t = B_0\lambda^t$. Then the number of individuals of age $x$ in a census at time $t$ is
$$
n_x(t) = B_{t-x}\,l_x = B_t\,\lambda^{-x}l_x,
$$
so the static table recovers $l_x$ exactly only when $\lambda = 1$ (a stationary population). In a growing population it underestimates survival to older ages by the factor $\lambda^{-x}$; in a declining one it overestimates it.

**Proof** An individual of age $x$ at time $t$ was born at $t - x$ and has survived $x$ years, which happens with probability $l_x$. With $B_{t-x}$ births at that time, the expected number alive is $B_{t-x}l_x = B_t\lambda^{-x}l_x$. Dividing by $n_0(t) = B_t$ gives $n_x/n_0 = \lambda^{-x}l_x$, which equals $l_x$ for all $x$ only if $\lambda = 1$. $\square$

If $\lambda$ is known from another source, the static table can be corrected by multiplying $n_x/n_0$ by $\lambda^x$. Fluctuations in recruitment are harder to correct: a single good year produces a bulge that travels up the age distribution and appears in the static table as a period of low mortality followed by a period of high mortality. Such artifacts show up as *negative* deaths ($d_x < 0$), which is impossible in a real cohort. The classic static life table of red deer (*Cervus elaphus*) on the island of Rhum, reconstructed by Lowe (1969) from the ages of deer alive in 1957, has exactly this problem: more 7-year-olds than 6-year-olds and more 15-year-olds than 14-year-olds were counted. Lowe therefore smoothed the counts before computing mortality rates, which is the usual remedy. Static tables are nonetheless indispensable for long-lived organisms and for organisms whose cohorts cannot be followed. A spectacular example is a population of the small dinosaur *Psittacosaurus lujiatunensis* from the Lower Cretaceous Yixian Formation in Liaoning, apparently killed together by a volcanic mudflow about 125 million years ago (Erickson et al. 2009). Ages estimated from growth lines in the bones gave a static life table with high mortality in the first three years, low mortality during rapid growth, and rising mortality again at the size of sexual maturity.

### 9.2.2. The Columns of a Life Table

**Formula 9.2.1 (Life Table)** For age classes $x = 0, 1, 2, \dots$, a life table records

| Column | Meaning | Computation |
|---|---|---|
| $n_x$ | number alive at the start of age class $x$ | data |
| $l_x$ | proportion of the original cohort surviving to the start of $x$ | $l_x = n_x/n_0$ |
| $d_x$ | number dying during $x$ | $d_x = n_x - n_{x+1}$ |
| $q_x$ | age-specific mortality rate during $x$ | $q_x = d_x/n_x$ |
| $p_x$ | age-specific survival rate | $p_x = 1 - q_x = n_{x+1}/n_x$ |
| $L_x$ | mean number alive during $x$ | $L_x = (n_x + n_{x+1})/2$ |
| $T_x$ | total time lived beyond the start of $x$ by those alive at $x$ | $T_x = \sum_{y \geq x}L_y$ |
| $e_x$ | life expectancy at the start of $x$ | $e_x = T_x/n_x$ |
| $k_x$ | killing power during $x$ | $k_x = \lg n_x - \lg n_{x+1} = -\lg p_x$ |

Survival is a product of the stage survivals, $l_x = p_0p_1\cdots p_{x-1}$. The formula for $L_x$ assumes that deaths are spread evenly through the interval; the life expectancy $e_x$ is measured in units of the age interval, and $e_0$ is the mean length of life.

The columns differ in what they are good for (Begon & Townsend 2021). The $d_x$ values can be added (the proportion of a cohort dying in the first four years is $d_0 + d_1 + d_2 + d_3$ divided by $n_0$), but they do not measure the intensity of mortality, because more individuals die when more are present. The $q_x$ values measure intensity, but cannot be added. The $k_x$ values do both: they measure intensity, and because $\sum_{x<y}k_x = \lg n_0 - \lg n_y$ they add up to the killing power of any stretch of life. They are the basis of key factor analysis (Section 9.5) and of the analysis of competition (7.19.11).

**Example 9.2.1 (A Barnacle Cohort)** Connell (1970) followed a cohort of the barnacle *Balanus glandula* on the rocky shore of San Juan Island, Washington, from settlement on the rock. The cohort life table (numbers rescaled to 142 settlers, after Krebs) is

| Age $x$ (years) | $n_x$ | $l_x$ | $d_x$ | $q_x$ | $L_x$ | $T_x$ | $e_x$ |
|---|---|---|---|---|---|---|---|
| 0 | 142 | 1.000 | 80 | 0.563 | 102 | 224 | 1.58 |
| 1 | 62 | 0.437 | 28 | 0.452 | 48 | 122 | 1.97 |
| 2 | 34 | 0.239 | 14 | 0.412 | 27 | 74 | 2.18 |
| 3 | 20 | 0.141 | 4.5 | 0.225 | 17.75 | 47 | 2.35 |
| 4 | 15.5 | 0.109 | 4.5 | 0.290 | 13.25 | 29.25 | 1.89 |
| 5 | 11 | 0.077 | 4.5 | 0.409 | 8.75 | 16 | 1.45 |
| 6 | 6.5 | 0.046 | 4.5 | 0.692 | 4.25 | 7.25 | 1.12 |
| 7 | 2 | 0.014 | 0 | 0 | 2 | 3 | 1.50 |
| 8 | 2 | 0.014 | 2 | 1.000 | 1 | 1 | 0.50 |
| 9 | 0 | 0 | — | — | 0 | 0 | — |

The fractional numbers (15.5, 6.5) were interpolated from the survivorship curve. Mortality is heaviest in the first year after settlement and lowest at ages 3–4, so life expectancy *rises* from 1.58 years at settlement to 2.35 years at age 3: a barnacle that has survived the dangerous first years can expect to live longer than a newly settled one. Such a rise is typical whenever juvenile mortality is high.

:::

### 9.2.3. Fecundity Schedules

Life tables are usually compiled together with an age-specific *fecundity schedule*. Its columns are $F_x$, the total number of offspring (of the youngest stage recorded) produced by the cohort during age class $x$, and $m_x = F_x/n_x$, the mean number produced per surviving individual. In sexual species $m_x$ usually counts daughters per female. The product $l_xm_x$ is the number of offspring produced at age $x$ per individual of the original cohort, and its sum is the **net reproductive rate** ([7.10.15](/7.10.15#def-15.1.3)), which we take up in Section 9.4. A life table with fecundity columns is sometimes called a *comprehensive life table*.

**Example 9.2.2 (A Grasshopper with Discrete Generations)** Richards & Waloff (1954) followed a cohort of the field grasshopper *Chorthippus brunneus* in southern England through its annual life cycle. Here the "age classes" are developmental stages:

| Stage $x$ | $n_x$ | $l_x$ | $q_x$ | $\lg n_x$ | $k_x$ | $F_x$ | $m_x$ | $l_xm_x$ |
|---|---|---|---|---|---|---|---|---|
| Eggs (0) | 44 000 | 1.000 | 0.92 | 4.64 | 1.10 | — | — | — |
| Instar I (1) | 3513 | 0.080 | 0.28 | 3.55 | 0.14 | — | — | — |
| Instar II (2) | 2529 | 0.057 | 0.24 | 3.40 | 0.12 | — | — | — |
| Instar III (3) | 1922 | 0.044 | 0.24 | 3.28 | 0.12 | — | — | — |
| Instar IV (4) | 1461 | 0.033 | 0.11 | 3.16 | 0.05 | — | — | — |
| Adults (5) | 1300 | 0.030 | — | 3.11 | — | 22 617 | 17.4 | 0.51 |

Almost all of the mortality falls on the overwintering eggs ($k_0 = 1.10$ of a total $\lg 44000 - \lg 1300 = 1.53$). Since the species is annual, the net reproductive rate $R_0 = \sum l_xm_x = \sum F_x/n_0 = 22617/44000 = 0.51$ is also the factor by which the population changed from one generation to the next: in that year it halved.

:::

## 9.3. Survivorship Curves

**Definition 9.3.1 (Survivorship Curve)** The **survivorship curve** of a cohort is the graph of $\lg l_x$ (or $\lg n_x$) against age $x$.

The logarithmic scale is essential. A fall from 1000 to 500 individuals looks dramatic on a linear scale and a fall from 50 to 25 looks trivial, yet the individual risk is the same; on a log scale both are drops of $\lg 2$. In continuous age, the survivorship $l(x)$ is the **survival function** of age at death, and the slope of $\ln l(x)$ is minus the **hazard function** $\mu(x)$ ([3.5.4](/3.5.4)), the instantaneous risk of death at age $x$:
$$
l(x) = \exp\Bigl(-\int_0^x\mu(a)\,\mathrm{d}a\Bigr), \qquad \mu(x) = -\frac{\mathrm{d}\ln l(x)}{\mathrm{d}x}. \tag{9.2}
$$
A straight survivorship curve thus means a constant hazard, and the steepness of the curve at any age is the risk of dying at that age. In discrete age classes the slope of the $\lg l_x$ curve over one interval is $-k_x$.

Pearl (1928) and Deevey (1947) classified survivorship curves into three types:

- Type I (convex): mortality is low until late in life and then rises steeply; most individuals live close to the physiological maximum. Humans in developed countries, many large mammals, and animals kept in zoos and as pets.
- Type II (straight): a constant risk of death at all ages, so that a constant *proportion* dies in each interval. Some birds after fledging; seeds buried in a seed bank.
- Type III (concave): very high mortality early in life, followed by a low and nearly constant risk in the few that survive. Fishes and marine invertebrates that release many small eggs, most plants (seeds and seedlings), and parasites.

Most wild animals lie between types II and III; most plant populations are close to type III, which is probably the commonest pattern in nature. The three types are conveniently generated by the **Weibull distribution** ([3.1.4](/3.1.4#def-4.3.3)) of age at death, whose hazard $\mu(x) = (\beta/\eta)(x/\eta)^{\beta-1}$ increases with age for $\beta > 1$ (type I), is constant for $\beta = 1$ (type II), and decreases for $\beta < 1$ (type III). Human mortality after childhood follows the **Gompertz–Makeham law** ([7.5.37](/7.5.37#def-37.1.2)), $\mu(x) = A + B\mathrm{e}^{cx}$: a constant background risk plus an exponentially rising risk of senescence.

![Survivorship curves (Definition 9.3.1). A: the three idealized types on a logarithmic scale, with age scaled to the maximum life span, generated by Weibull hazards with shape β = 6 (type I), 1 (type II) and 0.25 (type III), each scaled so that one in a thousand reaches the maximum age. B: the corresponding hazards μ(x) (Eq. (9.2)): rising with age in type I, constant in type II, falling in type III. C: two real cohorts. Female yellow-bellied marmots (*Marmota flaviventris*) in Colorado (Schwartz et al. 1998) die at a nearly constant rate (type II) until about age 8, faster for three years, and then the last few survivors die; the barnacle *Balanus glandula* (Connell 1970), followed from the settling larvae, loses more than 99.99% in the first year (k₀ = 4.2) and then survives at a nearly constant rate (type III)](./plots/survivorship.py)

The types are generalizations; real curves often change shape between life stages, as the marmot and dinosaur examples show. A survey of 37 mammal species in zoos (Lynch et al. 2010) found that, scaled to maximum longevity, most survivorship curves were essentially type II with an admixture of type I (senescence) or type III (early mortality), and that the mixture was associated with taxonomic order: artiodactyls showed the least senescence and carnivores the most, which allows managers to predict the mortality schedule of species with few data.

**Example 9.3.1 (Survival of Adult Tiger Mosquitoes)** The Asian tiger mosquito *Aedes albopictus* is the principal vector of dengue in southern China. Li et al. (2014) reared cohorts of adults in field cages at urban, suburban and rural sites around Guangzhou in August–September and October–November and recorded their daily survival. Survival curves were plateau-shaped (close to type I over the short adult life), with almost no deaths in the first days and a later steep decline. Adults lived longer in the autumn trials than in late summer, and in the urban and suburban sites longer than in the rural one, where in late summer most adults died within two weeks; some suburban females lived about two months. The differences matter epidemiologically because a mosquito can transmit dengue virus only after an extrinsic incubation period of roughly 8–12 days: the proportion of females that survive beyond this age, read directly off the survivorship curve, scales the transmission potential of a mosquito population.

:::

## 9.4. Reproductive Rate, Generation Time and Rate of Increase

### 9.4.1. Net Reproductive Rate and Generation Time

The life table and the fecundity schedule together determine how fast a population could grow if they stayed constant. Two summary statistics come first.

**Formula 9.4.1 (Net Reproductive Rate and Cohort Generation Time)** For a cohort with survivorship $l_x$ and fecundity $m_x$, the **net reproductive rate** and the cohort generation time are
$$
R_0 = \sum_x l_xm_x = \frac{1}{n_0}\sum_xF_x, \qquad T_c = \frac{\sum_x x\,l_xm_x}{\sum_x l_xm_x}. \tag{9.3}
$$
$R_0$ is the mean number of offspring produced by a newborn over its whole life. $T_c$ is the mean age of the parents at the birth of their offspring, averaged over the lifetime of a cohort.

$R_0 > 1$ means that each generation is larger than the last, $R_0 = 1$ that it just replaces itself, and $R_0 < 1$ that it declines. For an annual species with discrete generations, $R_0$ is simply the factor of change per year (Example 9.2.2). For the marmots of Figure C above, $R_0 = 0.67$ and $T_c = 4.5$ years: every four and a half years the population fell to about two thirds of its size.

To compare species with different generation lengths we need a rate per unit time. If a population grows by a constant factor $R$ per unit time, $N_t = N_0R^t$, and if it grows by $R_0$ in one generation of length $T$, then $R_0 = R^{\mathsf T}$, so
$$
\ln R_0 = T\ln R = rT, \qquad r = \frac{\ln R_0}{T}, \tag{9.4}
$$
where $r = \ln R$ is the rate of increase per individual per unit time, the **intrinsic rate of increase** ([7.10.15](/7.10.15#def-15.1.4)) when $l_x$ and $m_x$ are those of an unrestricted population. The question is what $T$ means when generations overlap. Using $T_c$ gives the common approximation $r \approx \ln R_0/T_c$. The exact rate follows from the dynamics of births.

### 9.4.2. The Euler–Lotka Equation

Let $B(t)$ be the number of births in year $t$ in a population with constant schedules $l_x$, $m_x$. The mothers of these newborns are the survivors of earlier births, and those born $x$ years earlier contribute $B(t - x)l_xm_x$. Hence, once the founders have died out,
$$
B(t) = \sum_{x\geq1}B(t-x)\,l_xm_x, \tag{9.5}
$$
the discrete form of the **renewal equation** ([7.5.34](/7.5.34#def-34.3.1)). It is a linear recursion, and it has solutions of geometric form.

**Theorem 9.4.1 (Euler–Lotka Equation)** The renewal equation (9.5) has a solution $B(t) = B_0\mathrm{e}^{rt}$ if and only if $r$ satisfies the **Euler–Lotka equation**
$$
\sum_{x\geq1}\mathrm{e}^{-rx}l_xm_x = 1, \qquad\text{or in continuous age}\qquad \int_0^\infty\mathrm{e}^{-ra}l(a)m(a)\,\mathrm{d}a = 1. \tag{9.6}
$$
If $l_xm_x \geq 0$ and is positive for at least one $x$, then (a) the equation has exactly one real root $r$; (b) $r > 0$, $r = 0$ or $r < 0$ according as $R_0 > 1$, $R_0 = 1$ or $R_0 < 1$; (c) in continuous age, every complex root $z \neq r$ has $\operatorname{Re}z < r$.

**Proof** Substituting $B(t) = B_0\mathrm{e}^{rt}$ in Eq. (9.5) and dividing by $B_0\mathrm{e}^{rt}$ gives Eq. (9.6), and conversely. Write $\varphi(r) = \sum_x\mathrm{e}^{-rx}l_xm_x$.

(a) Each term $\mathrm{e}^{-rx}l_xm_x$ with $x \geq 1$ and $l_xm_x > 0$ decreases strictly in $r$, tends to $+\infty$ as $r \to -\infty$ and to 0 as $r \to +\infty$. So $\varphi$ is continuous and strictly decreasing from $+\infty$ to 0, and takes the value 1 exactly once.

(b) $\varphi(0) = \sum l_xm_x = R_0$. Because $\varphi$ is decreasing, its root lies to the right of 0 if $\varphi(0) > 1$ and to the left if $\varphi(0) < 1$.

(c) Let $z = u + \mathrm{i}v$ be a root. Then $1 = \bigl\lvert\int\mathrm{e}^{-za}l(a)m(a)\,\mathrm{d}a\bigr\rvert \leq \int\mathrm{e}^{-ua}l(a)m(a)\,\mathrm{d}a = \varphi(u)$, so $\varphi(u) \geq 1 = \varphi(r)$, and $u \leq r$ because $\varphi$ is decreasing. Equality $u = r$ requires equality in the triangle inequality, that is, $\mathrm{e}^{-\mathrm{i}va}$ constant on the set of ages where $l(a)m(a) > 0$; for a continuous maternity function this forces $v = 0$, so $z = r$. $\square$

The general solution of the renewal equation is a sum of terms $c_j\mathrm{e}^{z_jt}$ over all roots $z_j$ of Eq. (9.6). Part (c) says that the real root dominates: whatever the initial age distribution, births eventually grow at rate $r$, and the age distribution converges to a fixed shape in which the number of age $x$ is proportional to $\mathrm{e}^{-rx}l_x$ (compare Proposition 9.2.1). This convergence to a stable age distribution, and its rate, are analyzed with matrix models in 7.19.14. In discrete time with reproduction confined to ages that share a common divisor (for example, only even ages), complex roots of the same modulus can occur and the births oscillate forever; this is the exception noted in part (c).

The root $r$ is the true intrinsic rate of increase of the schedule, and $\lambda = \mathrm{e}^r$ is the factor of increase per unit time. With $r$ in hand, the generation time can be *defined* to make Eq. (9.4) exact, $T = \ln R_0/r$. This $T$ generally differs both from $T_c$ and from the mean age of mothers in the stable population, $\bar A = \sum x\,\mathrm{e}^{-rx}l_xm_x$; "generation time" has several definitions, which coincide only when $R_0 = 1$.

**Proposition 9.4.1 (Accuracy of $r \approx \ln R_0/T_c$)** Let $A$ be the age of the mother at the birth of a randomly chosen offspring of a cohort, with distribution $\mathbb{P}(A = x) = l_xm_x/R_0$, mean $T_c$ and variance $\sigma^2$. Then
$$
r = \frac{\ln R_0}{T_c} + \frac{\sigma^2(\ln R_0)^2}{2T_c^3} + O\bigl((\ln R_0)^3\bigr). \tag{9.7}
$$
The approximation $r \approx \ln R_0/T_c$ is exact if all offspring are produced at one age ($\sigma = 0$), and good when $R_0$ is close to 1 or the ages of reproduction vary little.

**Proof** The Euler–Lotka equation reads $R_0\,\mathbb{E}[\mathrm{e}^{-rA}] = 1$, so $\ln R_0 = -\ln\mathbb{E}[\mathrm{e}^{-rA}] = -K(-r)$, where $K(s) = \ln\mathbb{E}[\mathrm{e}^{sA}]$ is the cumulant generating function of $A$. Its expansion $K(s) = T_cs + \sigma^2s^2/2 + O(s^3)$ gives
$$
\ln R_0 = rT_c - \frac{\sigma^2r^2}{2} + O(r^3).
$$
Thus $r = \ln R_0/T_c + O(\ln R_0)$ to first order; substituting this back into the quadratic term yields Eq. (9.7). $\square$

Because $\sigma^2 > 0$ whenever reproduction is spread over several ages, the correction term is positive, and the first-order approximation lies below the true $r$ both in growing populations and in declining ones (where it gives too steep a decline).

**Example 9.4.1 (Barnacle and Marmot)** For the barnacle of Example 9.2.1, counted from the larvae ($n_0 = 10^6$; Connell 1970), the fecundity schedule gives

| Age $x$ | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|---|---|---|---|---|---|---|---|---|
| $l_x \times 10^6$ | 62 | 34 | 20 | 15.5 | 11 | 6.5 | 2 | 2 |
| $m_x$ | 4600 | 8700 | 11 600 | 12 700 | 12 700 | 12 700 | 12 700 | 12 700 |
| $l_xm_x$ | 0.285 | 0.296 | 0.232 | 0.197 | 0.140 | 0.083 | 0.025 | 0.025 |

so $R_0 = 1.283$, $T_c = 3.07$ years and $\ln R_0/T_c = 0.081$ per year. The Euler–Lotka root is $r = 0.0847$ per year ($\lambda = 1.088$), and the second-order formula (9.7) with $\sigma^2 = 3.10$ gives 0.0845. The generation time that makes Eq. (9.4) exact is $T = \ln R_0/r = 2.94$ years, shorter than $T_c$ because in a growing population young mothers are overrepresented. For the marmots, $R_0 = 0.671$ and $T_c = 4.50$ years give $\ln R_0/T_c = -0.089$, against the exact $r = -0.085$ per year ($\lambda = 0.918$).

:::

![The Euler–Lotka equation (Theorem 9.4.1). A: the function φ(r) = Σ e^(−rx) lₓmₓ decreases strictly; its value at r = 0 (squares) is R₀ and the root of φ(r) = 1 (dots) is the intrinsic rate of increase: r = +0.085 per year for the barnacle (R₀ = 1.28) and −0.085 per year for the marmots (R₀ = 0.67). B: when every fecundity of the barnacle schedule is multiplied by a constant, so that R₀ varies while the shape of lₓmₓ stays fixed, the approximation ln R₀/T_c (dashed) is accurate near R₀ = 1 and increasingly underestimates r as R₀ grows; adding the variance term of Eq. (9.7) (dotted) extends the range of accuracy](./plots/euler-lotka.py)

The equation is solved numerically. Since $\varphi$ is monotone, bracketing methods are safe; the root of the barnacle schedule is found in a line:

```python
import numpy as np
from scipy.optimize import brentq

x = np.arange(1, 9)
lm = np.array([0.285, 0.296, 0.232, 0.197, 0.140, 0.083, 0.025, 0.025])
r = brentq(lambda r: np.sum(np.exp(-r * x) * lm) - 1, -1, 1)   # 0.0847
```

The intrinsic rate of increase measured under ideal laboratory conditions (unlimited food, optimal temperature, no enemies) is the *maximum* intrinsic rate $r_m$, an attribute of the species; the rate realized in the field is lower and varies with conditions. Comparing $r$ estimated from life tables for the same species in different habitats or years is one of the most direct ways to judge where a species does well. The sensitivity of $r$ to each $l_x$ and $m_x$, which determines how selection acts on the life history ([7.10.15](/7.10.15#sec-15.1.4)) and which vital rates management should target, follows from implicit differentiation of Eq. (9.6) and is developed with the **Leslie matrix** in 7.19.14.

## 9.5. Key Factor Analysis

A single life table describes one cohort in one year. With a series of life tables for successive generations one can ask which stage of the life cycle is responsible for the year-to-year changes in abundance, and which stage, if any, regulates it.

For a species with discrete generations, divide the life cycle into stages with killing powers $k_1, \dots, k_m$, and let the total generation mortality be
$$
K = \sum_{i=1}^mk_i = \lg(\text{potential births}) - \lg(\text{adults}),
$$
where "potential births" is the maximum fecundity times the number of adults of the previous generation, so that a shortfall in fecundity is counted as a $k$ value as well.

**Definition 9.5.1 (Key Factor Analysis)** **Key factor analysis** (Morris 1959; Varley & Gradwell 1960) compares the $k$ values of the stages of a life cycle over a series of generations to identify the *key factor*, the stage whose mortality contributes most to the variation in total generation mortality $K$, and hence to the fluctuations in abundance.

The mean $k$ values show which stages kill most individuals on average. They do not show which stage *drives fluctuations*: a factor that kills 90% every year without fail (a constant $k$) contributes nothing to the variation of $K$. Varley and Gradwell's original method was graphical: plot $K$ and all $k_i$ against generation and see which $k_i$ moves most closely with $K$. Podoler & Rogers (1975) made it quantitative.

**Proposition 9.5.1 (Podoler–Rogers Regression)** Let $b_i = \operatorname{Cov}(k_i, K)/\operatorname{Var}(K)$ be the slope of the regression of $k_i$ on $K$ over the generations. Then $\sum_ib_i = 1$, and $b_i$ is the share of the variance of $K$ attributable to stage $i$, in the sense that $\operatorname{Var}(K) = \sum_i\operatorname{Cov}(k_i, K)$. The key factor is the stage with the largest $b_i$.

**Proof** By bilinearity of covariance, $\sum_i\operatorname{Cov}(k_i, K) = \operatorname{Cov}\bigl(\sum_ik_i, K\bigr) = \operatorname{Cov}(K, K) = \operatorname{Var}(K)$. Dividing by $\operatorname{Var}(K)$ gives $\sum_ib_i = 1$. $\square$

A regression coefficient can be negative. This happens when a stage compensates for the others: if early mortality is high, fewer individuals reach a density-dependent later stage, which then kills a smaller fraction, so that its $k$ varies inversely with $K$.

The second question, regulation, is answered by plotting each $k_i$ against $\lg N_i$, the logarithm of the number entering the stage. A positive slope means that the stage kills a larger fraction at higher density, that is, it acts in a density-dependent way and can regulate the population (the slope $b$ of such plots and its meaning are the subject of 7.19.11). Such regressions are vulnerable to a spurious correlation: an error in estimating $N_i$ appears with a positive sign in $\lg N_i$ and in $k_i = \lg N_i - \lg N_{i+1}$, and so produces a positive slope even without density dependence. Varley and Gradwell therefore also regressed $\lg N_i$ on $\lg N_{i+1}$ and accepted density dependence only when both regressions indicated it.

![Key factor analysis of a simulated insect with four stages (model in the script: k₁ is weather-driven mortality of eggs and young larvae, variable and density independent; k₂ is a nearly constant parasitism; k₃ is pupal predation with k₃ = 0.3(lg N − 1); k₄ is a small adult mortality). A: the Varley–Gradwell plot over 40 generations: total mortality K (shifted upward for clarity) moves with k₁. B: the regression coefficients of each kᵢ on K (Proposition 9.5.1) sum to 1; k₁ is the key factor (b = 1.00), while the density-dependent k₃ has a negative coefficient because it compensates for the losses of earlier stages. C: k₃ increases with the logarithm of the number of pupae (slope 0.30), so pupal predation is density dependent and regulates the population; k₁ is unrelated to the number of eggs](./plots/key-factor.py)

The classic study is Varley and Gradwell's analysis of the winter moth (*Operophtera brumata*) in Wytham Wood near Oxford, over 1950–1968. The key factor was "winter disappearance", the loss between the adult females' potential fecundity and the larvae established in spring, which depended mainly on how well the hatching of the eggs matched the bud burst of the oaks; the factor that regulated the population was pupal predation in the soil by shrews and beetles, which was density dependent. The key factor (which explains fluctuations) and the regulating factor (which keeps the population within bounds) are usually different stages, as in the simulation above. In three regions of the eastern United States, the key phase in wood frogs (*Rana sylvatica*) was consistently the larval period, because ponds dry out in dry years, whereas density dependence acted mainly in the adult phase (Berven 1995). In the dune annual *Androsace septentrionalis* in Poland, the seeds in the soil were the key phase, but density dependence acted on the seedlings (Symonides 1979).

Key factor analysis identifies phases, not causes: the "factor" attributed to a phase is a hypothesis to be tested by experiment. It also weights all phases equally, although a death before maturity affects population growth more than a death after most reproduction is done. Sibly & Smith (1998) therefore proposed $\lambda$-contribution analysis, which regresses the contribution of each phase to the yearly deviation of the population growth rate $\lambda$, weighted by the sensitivity of $\lambda$ to that phase (7.19.14). Applied to the red deer of Rhum, key factor analysis singles out fecundity in old age, which matters little for $\lambda$, while $\lambda$-contribution analysis identifies calf survival in the first year.

## 9.6. Age Structure

The age structure of a population is the proportion of individuals in each age class. It is usually drawn as an age pyramid.

**Definition 9.6.1 (Age Pyramid)** An **age pyramid** is a diagram of the age structure of a population made of horizontal bars stacked from the youngest age class at the bottom to the oldest at the top, the width of each bar showing the number or percentage of individuals in that class; for populations with two sexes, males are drawn to the left and females to the right.

Three basic shapes are distinguished:

| Shape | Age structure | Births and deaths | Population |
|---|---|---|---|
| Pyramid (broad base) | many young, few old | birth rate > death rate | expanding |
| Bell | similar numbers in young and middle classes, tapering at the top | birth rate ≈ death rate | stationary |
| Urn (narrow base) | few young, many middle-aged and old | birth rate < death rate | contracting |

The connection between shape and growth follows from the stable age distribution: in a population with constant schedules and rate of increase $r$, the proportion of age $x$ is proportional to $\mathrm{e}^{-rx}l_x$ (Theorem 9.4.1). A positive $r$ weights the young by the factor $\mathrm{e}^{-rx}$ and widens the base; a negative $r$ inflates the older classes. The converse inference, from shape to dynamics, is unreliable, because a real age structure records the population's history as well as its current vital rates. A past baby boom or a famine produces a bulge or a notch that moves up the pyramid for decades, and a recent fall in fertility narrows the base of a pyramid that is still growing because large cohorts born earlier are now of reproductive age (population momentum).

![Age pyramids of model human populations (script: a Siler-type mortality schedule with male senescent mortality 1.4 times that of females; 1.05 male births per female birth; model values, not data for any country). A–C: stable age distributions proportional to e^(−rx)l(x) for r = +0.025 per year (pyramid, 5% aged 65 or over), 0 (bell, 15%) and −0.012 (urn, 23%). D: a population that had the stable structure of A, after its total fertility rate fell within ten years from 4.2 to 1.1 children per woman: 45 years later the large cohorts born before the decline are aged 35–60, the base has contracted to the size of the small cohorts born since, and the proportion aged 65 or over has nearly tripled, although the population is far from any stable structure](./plots/age-pyramids.py)

Human populations show these processes on a large scale. China's age pyramid, compared over successive censuses, changed from a broad pyramid in the 1950s–1960s to a structure with a contracted base and a bulge in the middle-aged classes, the result of the rapid fall in fertility after the 1970s and the large cohorts born in the 1960s, much like panel D. By the conventional thresholds (the proportion aged 65 or over exceeding 7%, 14% and 20% for an "aging", "aged" and "super-aged" society), China passed 7% in 2000 and 14% in 2021, and the proportion was 14.9% in 2022, compared with a world average of about 9.8%. In 2023, 9.02 million births (a crude birth rate of 6.39‰) and 11.10 million deaths (7.87‰) gave a rate of natural increase of −1.48‰; in 2024, 9.54 million births (6.77‰) and 10.93 million deaths (7.76‰) gave −0.99‰. A negative natural increase with a narrow base means that the population will continue to decline and age for decades even if fertility recovers, because the cohorts that will become parents are already small. The ecological tools of this chapter, life tables, $R_0$ (for humans, the net reproduction rate counted in daughters) and the stable population, are the same ones demographers use.

## Summary

- Population size changes through births, deaths, immigration and emigration (Eq. (9.1), Definition 9.1.1); sex ratio, age structure and rate of increase are secondary parameters derived from them.
- A cohort life table follows one cohort; a static life table takes a census of all ages and is valid only for a stationary population with constant schedules (Proposition 9.2.1). Its columns (Formula 9.2.1) are linked by $l_x = n_x/n_0$, $q_x = d_x/n_x$, $e_x = T_x/n_x$ and $k_x = \lg n_x - \lg n_{x+1}$; $k$ values measure intensity and are additive.
- Survivorship curves plot $\lg l_x$ against age (Definition 9.3.1); their slope is minus the hazard (Eq. (9.2)). Types I, II and III correspond to rising, constant and falling risk of death; most natural populations lie between II and III.

| Quantity | Formula | Meaning |
|---|---|---|
| Net reproductive rate | $R_0 = \sum l_xm_x$ | offspring per newborn per lifetime |
| Cohort generation time | $T_c = \sum xl_xm_x/R_0$ | mean age of parents |
| Euler–Lotka equation | $\sum\mathrm{e}^{-rx}l_xm_x = 1$ | exact $r$ (unique real, dominant root) |
| Approximation | $r \approx \ln R_0/T_c + \sigma^2(\ln R_0)^2/(2T_c^3)$ | accurate near $R_0 = 1$ |
| Finite rate | $\lambda = \mathrm{e}^r$ | factor of increase per unit time |

- The Euler–Lotka equation follows from the renewal equation for births (Theorem 9.4.1); its real root dominates all others, so populations with constant schedules approach exponential growth and a stable age distribution proportional to $\mathrm{e}^{-rx}l_x$. The approximation $r \approx \ln R_0/T_c$ is exact for reproduction at a single age (Proposition 9.4.1, Example 9.4.1).
- Key factor analysis finds the stage whose mortality drives the fluctuations of total mortality; the regression coefficients of $k_i$ on $K$ sum to 1 (Proposition 9.5.1). Density dependence is tested by regressing $k_i$ on $\lg N_i$; the key factor and the regulating factor are usually different stages.
- Age pyramids are pyramid-, bell- or urn-shaped for expanding, stationary and contracting populations (Definition 9.6.1), but real age structures also record past fluctuations, as the aging of China's population shows.

## Questions

1. From the barnacle life table (Example 9.2.1), compute $k_x$ for each age and verify that $\sum_{x=0}^{2}k_x = \lg n_0 - \lg n_3$. Which age class has the highest killing power, and does it coincide with the largest $d_x$?

   **Answer** $k_x = \lg n_x - \lg n_{x+1}$: $k_0 = \lg142 - \lg62 = 0.360$, $k_1 = 0.261$, $k_2 = 0.230$, $k_3 = 0.111$, $k_4 = 0.149$, $k_5 = 0.228$, $k_6 = 0.513$, $k_7 = 0$. Then $k_0 + k_1 + k_2 = 0.851 = \lg142 - \lg20 = 2.152 - 1.301$. The largest $d_x$ is $d_0 = 80$, but the largest killing power is $k_6 = 0.513$ (in age class 6, 4.5 of 6.5 die): $d_x$ is large in the first year only because most individuals are still alive then, while the intensity of mortality is greatest in old age.

2. A static life table is compiled from a census of a population that is in fact growing at $\lambda = 1.1$ per year. By what factor does it misestimate survival to age 5? How could you correct it?

   **Answer** By Proposition 9.2.1, $n_5/n_0 = \lambda^{-5}l_5 = 0.621\,l_5$: survival to age 5 is underestimated by about 38%, because the five-year-olds come from a cohort that was smaller at birth. If $\lambda$ is known (from counts of the population over several years, or from the Euler–Lotka equation applied to the fecundity schedule, iterated together with the corrected $l_x$), multiply each $n_x/n_0$ by $\lambda^x$.

3. Show that if all reproduction occurs at a single age $\alpha$ with $l_\alpha m_\alpha = R_0$, the Euler–Lotka equation gives $r = \ln R_0/\alpha$ exactly. What does Proposition 9.4.1 imply for a species whose reproduction is spread over many ages?

   **Answer** The equation reduces to $\mathrm{e}^{-r\alpha}R_0 = 1$, so $r = \ln R_0/\alpha$; here $T_c = \alpha$ and $\sigma^2 = 0$. When reproduction is spread out ($\sigma^2 > 0$), the correction term $\sigma^2(\ln R_0)^2/(2T_c^3)$ is positive, so the true $r$ always exceeds $\ln R_0/T_c$: when $R_0 > 1$ the approximation underestimates growth (offspring produced early start compounding sooner), and when $R_0 < 1$ it exaggerates the decline. The error grows with $(\ln R_0)^2$, so it matters for fast-growing populations.

4. In the key factor simulation (figure in Section 9.5), why is the regression coefficient of the density-dependent pupal mortality $k_3$ on $K$ negative? Would removing the pupal predators make the population fluctuate more or less?

   **Answer** When $k_1$ is high, fewer pupae survive to be attacked, and because $k_3$ increases with the logarithm of pupal numbers, a smaller fraction is then killed. $k_3$ therefore varies opposite to $k_1$, and since $k_1$ dominates $K$, $k_3$ is negatively correlated with $K$: it compensates. Without the predators, the logarithm of abundance would perform a random walk driven by $k_1$ (each generation's change would be the deviation of $k_1$ from its mean, uncompensated), so the population would fluctuate far more and would not be regulated at all; the key factor explains fluctuations, the density-dependent factor limits them.

5. (Open) The adult survival of *Aedes albopictus* differs between urban and rural sites (Example 9.3.1). Outline how you would combine a survivorship curve with the extrinsic incubation period of dengue virus to compare the transmission potential of mosquito populations.

   **Answer** The number of infectious bites a mosquito delivers is roughly the biting rate times the expected number of days it is alive and infectious. If a female becomes infected on the day of her first blood meal at age $a_1$ and the virus needs $n$ days (the extrinsic incubation period) to reach the salivary glands, the expected infectious lifetime is $\sum_{x\geq a_1+n}l_x/l_{a_1}$, which can be read from the cohort life table: the area under the survivorship curve beyond age $a_1 + n$. With a constant daily survival $p$ this becomes $p^n/(-\ln p)$, the factor that appears in the Ross–Macdonald vectorial capacity (7.17.40). Because $p^n$ depends steeply on $p$ when $n$ is 8–12 days, a modest increase in adult survival in urban habitats can raise transmission potential several-fold; temperature also shortens $n$, so seasonal comparisons need both curves.
