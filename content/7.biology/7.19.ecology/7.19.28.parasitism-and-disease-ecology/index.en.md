---
title: Parasitism and Disease Ecology
description: "Parasites and pathogens as part of host population ecology: micro- and macroparasites, parasitoids, social and brood parasites; hosts as habitats and the negative binomial aggregation of worms; density- and frequency-dependent transmission, R0 and the threshold host density; the SIR model with host demography, its global stability, interepidemic period and seasonal forcing; vaccination thresholds and the shift in age at infection; the Anderson–May conditions for regulation of hosts by microparasites and by aggregated macroparasites; the evolution of virulence; and emerging diseases of wildlife."
---

Parasites, organisms that live on or in a host and take their resources from it, make up a large share of all species, and in many ecosystems their combined biomass rivals that of the top predators. For a long time ecologists treated them as a medical or veterinary matter. Since the work of Anderson and May around 1980 it has been clear that parasites are consumers like predators and parasitoids, with their own population dynamics, that they can regulate host populations, generate cycles and drive species to extinction, and that the theory of infectious disease is a branch of population ecology.

This chapter treats parasites from the host population's point of view. Section 28.1 classifies parasites and describes their distribution among hosts; Section 28.2 the transmission process and the basic reproduction number; Section 28.3 microparasite dynamics in a host population with births and deaths, including vaccination; Section 28.4 the question of whether parasites regulate their hosts; Section 28.5 the evolution of virulence; Section 28.6 disease in wild populations and conservation. The epidemic models of networks are in [1.4.7](/1.4.7#sec-7.8.2), which defines the **SIR model** and the **basic reproduction number**; the epidemiology of human infectious disease, outbreak investigation and surveillance are in [7.11.35](/7.11.35); vaccines and herd immunity in [7.11.28](/7.11.28#sec-28.8); the coevolution of hosts and parasites, including the virulence trade-off, in [7.10.17](/7.10.17#sec-17.2.4). The discrete-time dynamics of parasitoids are the subject of [7.19.27](/7.19.27).

## 28.1. Parasites and Their Hosts

### 28.1.1. Kinds of Parasites

The most useful classification for population dynamics is by what happens inside the host.

**Definition 28.1.1 (Microparasite and Macroparasite)** A **microparasite** multiplies directly within its host, usually inside cells: viruses, bacteria, many protists and fungi. Microparasites are small, have short generation times, and the infection of a host is usually short relative to the host's life and often followed by immunity; their dynamics are described by the numbers of susceptible, infected and recovered hosts. A **macroparasite** grows in or on its host but does not multiply there, or multiplies only slowly: parasitic helminths (flukes, tapeworms, nematodes), lice, fleas, ticks and parasitic plants. Each new adult macroparasite results from an infective stage acquired from outside, so the harm done to a host depends on its parasite burden, and dynamics must be described by the distribution of burdens.

The distinction is about dynamics, not taxonomy: a protist that forms long-lasting infections whose severity depends on dose is effectively a macroparasite. Other classifications cut across it.

- Location: ectoparasites (lice, ticks, mistletoe on its host tree) and endoparasites (intracellular or in body cavities and tissues).
- Transmission: direct, by contact, air, water or ingestion of infective stages; or indirect, through vectors (mosquitoes for malaria, ticks for Lyme disease, [7.17.40](/7.17.40)) or through intermediate hosts in complex life cycles. A digenean fluke, for example, passes from a snail to a fish to a bird; many such parasites manipulate the behavior of the intermediate host to reach the next host (**host manipulation**).
- Kill or not: parasitoids ([7.19.27](/7.19.27)) are parasites that necessarily kill their host, and are treated as natural enemies like predators. Many parasitic Hymenoptera and Diptera are parasitoids.
- Social parasites do not consume the host's tissue but exploit its behavior. Slave-making ants, such as *Polyergus* queens, which kill the queen of a *Formica* colony and are adopted by its workers, raid other colonies for brood that become workers of the parasite colony ([7.17.38](/7.17.38#sec-38.7)); **brood parasitism**, the laying of eggs in the nests of other species by cuckoos and cowbirds, is treated with its coevolution in [7.18.32](/7.18.32).

### 28.1.2. Hosts as Habitats

A host is a habitat for its parasites, with three peculiarities: it is patchy (each host is an island), it dies, and it fights back. Within a host, parasites face an immune response that can clear infection or limit parasite numbers, competition with other parasites for space and resources, and specialization to particular tissues (the many microhabitats of the human gut, or the gills, skin and intestine of a fish, each with its own fauna). Host specificity ranges from extreme, as in many lice, to very broad: the generalists, and especially parasites able to infect several host species, are the source of most emerging diseases, including the zoonoses of humans ([7.11.35](/7.11.35)).

Hosts respond to parasites by resistance, which reduces parasite numbers, and tolerance, which reduces the damage done by a given burden. Both have costs: lines of *Drosophila* selected for resistance to parasitoids, for example, are poorer larval competitors. The difference matters for the parasite: resistance reduces its fitness, tolerance does not, so tolerance does not select for counter-adaptations in the parasite.

### 28.1.3. Aggregation of Macroparasites

Macroparasites are almost always aggregated among their hosts: most hosts carry few parasites and a few hosts carry most of them. The variance of the burden exceeds the mean, and the frequency distribution is well described by the **negative binomial distribution** with mean $\bar m$ and clumping parameter $k$,

$$
\mathbb{P}(\text{burden} = i) = \frac{\Gamma(k + i)}{i!\,\Gamma(k)}\Bigl(\frac{k}{k + \bar m}\Bigr)^k\Bigl(\frac{\bar m}{k + \bar m}\Bigr)^i, \qquad \operatorname{Var} = \bar m + \frac{\bar m^2}{k}, \tag{28.1}
$$
with variance tending to the Poisson variance $\bar m$ as $k \to \infty$. A survey of 269 host–parasite combinations by Shaw and Dobson (1995) found $k < 1$ in the great majority, and a value around 0.3–0.5 is typical of helminths. With $k = 0.5$ and a mean of 10 worms, about 22 % of hosts are uninfected, and the most infected 20 % of hosts carry two thirds of all worms (Figure 1). The same "20/80" pattern applies to the transmission of many infections (Woolhouse and colleagues 1997), and it is the basis of control programs that target the most heavily infected people.

Aggregation arises because hosts differ in exposure (behavior, diet, location) and in susceptibility (genotype, nutrition, immune history), and because infective stages are clumped in space. The parameter $k$ is estimated by the method of moments, $\hat k = \bar m^2/(s^2 - \bar m)$, or better by maximum likelihood with a negative binomial regression (the statistical model is in [3.3](/3.3)). Its dynamical consequence, a strong density-dependent effect of parasite-induced host mortality on the parasite population, is derived in Section 28.4.2.

![Aggregation of macroparasites. A: the distribution of worm burdens in a host population with mean burden 10, for random infection (Poisson) and for the negative binomial distribution, Eq. (28.1), with k = 0.5, typical of helminths: 22 % of hosts carry no worms, and a long tail of hosts carries dozens. B: the cumulative fraction of all worms carried by the most heavily infected hosts, with hosts ranked by burden, for the Poisson distribution and for k = 2, 0.5 and 0.2 (dashed diagonal: all hosts equal). The dotted lines mark the 20/80 pattern: the most infected fifth of the hosts carries about two thirds of the worms when k = 0.5 and about 85 % when k = 0.2](./plots/negbin-burden.py)

## 28.2. Transmission

### 28.2.1. Density- and Frequency-Dependent Transmission

The rate at which susceptible hosts $S$ become infected by infectious hosts $I$ depends on how contacts scale with host density.

**Definition 28.2.1 (Density- and Frequency-Dependent Transmission)** Transmission is **density-dependent transmission** if the rate of new infections is $\beta SI$, as when hosts meet at random and the contact rate per host increases in proportion to host density $N$ (mass action). It is **frequency-dependent transmission** if the rate is $\beta' SI/N$, as when the number of contacts per host is fixed by behavior and independent of density, so that what matters is the fraction $I/N$ of contacts that are infectious.

Sexually transmitted infections, infections spread within family groups or colonies, and vector-borne infections whose vectors bite a fixed number of times are approximately frequency dependent; infections spread by air or by free-living stages in a shared environment are approximately density dependent. Neither form is exact. Begon and colleagues (1998, 1999) measured the transmission of cowpox virus in field populations of bank voles and wood mice and found that the transmission rate increased with density, but less than proportionally: between the two ideal forms.

### 28.2.2. The Basic Reproduction Number and the Threshold Host Density

The basic reproduction number $R_0$ is the expected number of secondary infections caused by one infectious host in an otherwise fully susceptible population ([1.4.7](/1.4.7#sec-7.8.2)). For an infection with transmission rate $\beta$ in a host population of size $N$, from which infected hosts are lost by recovery (rate $\gamma$), natural death (rate $\mu$) and death caused by infection (the **virulence** $\alpha$, [7.10.17](/7.10.17#sec-17.2.4)), the expected infectious period is $1/(\alpha + \mu + \gamma)$, and

$$
R_0 = \frac{\beta N}{\alpha + \mu + \gamma} \quad\text{(density dependent)}, \qquad R_0 = \frac{\beta'}{\alpha + \mu + \gamma} \quad\text{(frequency dependent)}. \tag{28.2}
$$
An infection can invade if and only if $R_0 > 1$. With density-dependent transmission this defines a threshold.

**Definition 28.2.2 (Threshold Host Density)** The **threshold host density** of a density-dependently transmitted infection is $N_{\mathrm{T}} = (\alpha + \mu + \gamma)/\beta$, the host density at which $R_0 = 1$; the infection cannot invade or persist in a host population below it.

Two consequences shape disease ecology. First, density-dependent infections can be controlled by reducing host density, as culling is meant to do for rabies in foxes or bovine tuberculosis in badgers, though such culling often fails because it increases host movement and contact. Second, infections with frequency-dependent transmission have no threshold: they can persist in small populations and drive their hosts to extinction (Section 28.6). In finite populations a further threshold arises from chance. An infection with lifelong immunity, like measles, needs a continuous supply of new susceptibles through births; in a small population the chains of transmission die out in the troughs between epidemics. Bartlett (1957) estimated this *critical community size* for measles at roughly 250,000–500,000 people, and Black (1966) confirmed it with the records of island populations: below this size, measles disappeared between epidemics and returned only by reintroduction. Such acute, immunizing infections of humans could not have persisted before agricultural societies created large populations.

## 28.3. Microparasites in Host Populations

### 28.3.1. The SIR Model with Births and Deaths

In a closed epidemic (no births or deaths) the SIR model of [1.4.7](/1.4.7) predicts a single outbreak that ends when the susceptible fraction has fallen below $1/R_0$, leaving a fraction $s_\infty$ of susceptibles that solves the Kermack–McKendrick final size equation $s_\infty = \mathrm{e}^{-R_0(1 - s_\infty)}$ (derived there, and discussed for human epidemics in [7.11.35](/7.11.35#sec-35.3.2)). Over longer times births bring in new susceptibles, and the infection can become endemic. Let a host population of constant size have per capita birth and death rates $\mu$ (life expectancy $1/\mu$), with all newborns susceptible, and let $s$, $i$, $r$ be the fractions susceptible, infectious and recovered (immune for life). With frequency-dependent transmission, or density-dependent transmission at constant $N$ absorbed into $\beta$,

$$
\frac{\mathrm{d}s}{\mathrm{d}t} = \mu - \beta si - \mu s, \qquad \frac{\mathrm{d}i}{\mathrm{d}t} = \beta si - (\gamma + \mu)i, \qquad r = 1 - s - i, \tag{28.3}
$$
with $R_0 = \beta/(\gamma + \mu)$.

**Proposition 28.3.1 (Endemic Equilibrium)** For Eq. (28.3):

1. If $R_0 \le 1$, every solution tends to the disease-free state $(s, i) = (1, 0)$.
2. If $R_0 > 1$, the endemic equilibrium
   $$
   s^* = \frac{1}{R_0}, \qquad i^* = \frac{\mu}{\gamma + \mu}\Bigl(1 - \frac{1}{R_0}\Bigr) = \frac{\mu(R_0 - 1)}{\beta}
   $$
   is globally asymptotically stable for all initial conditions with $i(0) > 0$, and the approach is by damped oscillations when $\mu$ is small compared with $\gamma$.

**Proof** At the equilibrium with $i^* > 0$, $\beta s^* = \gamma + \mu$, so $s^* = 1/R_0$, and $\mu = \beta s^*i^* + \mu s^*$ gives $i^*$. For $R_0 > 1$ consider

$$
V(s, i) = s - s^* - s^*\ln\frac{s}{s^*} + i - i^* - i^*\ln\frac{i}{i^*},
$$
which is positive except at the equilibrium and tends to infinity at the boundary of the region $s, i > 0$. Using $\mu = \beta s^*i^* + \mu s^*$, the $s$-equation reads $\dot s = -\beta(si - s^*i^*) - \mu(s - s^*)$, and $si - s^*i^* = s(i - i^*) + i^*(s - s^*)$. Then

$$
\dot V = \frac{s - s^*}{s}\dot s + \frac{i - i^*}{i}\dot i = -\beta(s - s^*)(i - i^*) - (\beta i^* + \mu)\frac{(s - s^*)^2}{s} + (i - i^*)\beta(s - s^*) = -(\beta i^* + \mu)\frac{(s - s^*)^2}{s} \le 0,
$$
where we used $\dot i = i\beta(s - s^*)$. The set $\dot V = 0$ is the line $s = s^*$, on which $\dot s = \mu - \beta s^*i - \mu s^* = \beta s^*(i^* - i)$, nonzero unless $i = i^*$; by LaSalle's principle every solution converges to the equilibrium. For $R_0 \le 1$, $\dot i = i(\beta s - \gamma - \mu) \le i(\gamma + \mu)(R_0 s - 1) \le 0$ once $s \le 1$ (which holds eventually, since $\dot s < 0$ when $s > 1$), and a similar argument with $V = i$ shows $i \to 0$ and then $s \to 1$. At the endemic equilibrium

$$
J = \begin{bmatrix} -\beta i^* - \mu & -\beta s^* \\ \beta i^* & 0\end{bmatrix} = \begin{bmatrix} -\mu R_0 & -(\gamma + \mu) \\ \mu(R_0 - 1) & 0\end{bmatrix},
$$
with $\operatorname{tr}J = -\mu R_0$ and $\det J = \mu(R_0 - 1)(\gamma + \mu)$. If $\mu \ll \gamma$, then $(\operatorname{tr}J)^2 \ll 4\det J$ and the eigenvalues are complex, $-\frac12\mu R_0 \pm \mathrm{i}\omega$ with $\omega \approx \sqrt{\mu(R_0 - 1)(\gamma + \mu)}$. $\square$

The frequency of the damped oscillations has a memorable interpretation. In the endemic state the force of infection, the rate at which a susceptible becomes infected, is $\beta i^* = \mu(R_0 - 1)$, so the mean age at infection is $A = 1/[\mu(R_0 - 1)]$, and the infectious period is $D = 1/(\gamma + \mu)$. Then

$$
T \approx \frac{2\pi}{\omega} = 2\pi\sqrt{AD}, \qquad R_0 \approx 1 + \frac{L}{A}, \tag{28.4}
$$
where $L = 1/\mu$ is the life expectancy. The second formula estimates $R_0$ from serological data on the age at infection. For measles before vaccination in industrialized countries, $A \approx 4$–$5$ years and $L \approx 70$ years give $R_0 \approx 15$, and with $D \approx 2$ weeks the first gives $T \approx 2$–$2.5$ years, close to the observed interepidemic periods of measles in England and Wales before 1968. Epidemics recur because they exhaust the susceptibles, which then take years to be replenished by births.

In the model the oscillations are damped (Figure 2B), but in real populations they persist, because transmission varies seasonally: for childhood infections it rises when schools are in session. With seasonal forcing, $\beta(t) = \beta_0(1 + \varepsilon\cos 2\pi t)$, the SIR model produces annual, biennial or irregular epidemics, depending on $R_0$, the birth rate and $\varepsilon$; Earn and colleagues (2000) showed that the changes of measles dynamics in British and American cities, from annual to biennial to irregular, followed changes in the birth rate (the baby boom, then vaccination, which acts like a reduced birth rate of susceptibles) as predicted by the forced model.

![The SIR model. A: a closed epidemic with R₀ = 3 and an infectious period of one week: the infectious fraction peaks when s falls to 1/R₀ (dotted), and the epidemic ends with a fraction s∞ = 0.06 still susceptible (dashed), the root of the final size equation. B: with host births and deaths (life expectancy 50 years) and measles-like parameters (R₀ = 15, infectious period 2 weeks), Eq. (28.3): incidence (log scale) shows recurrent epidemics, damped toward the endemic equilibrium (Proposition 28.3.1), with a period approaching 2π√(AD) ≈ 2.3 years, Eq. (28.4). C: the same model with seasonal transmission, β(t) = β₀(1 + 0.25 cos 2πt): after a transient the epidemics become sustained and biennial, with large and small epidemics alternating, as measles did in many cities before vaccination](./plots/sir-demography.py)

### 28.3.2. Vaccination and Herd Immunity

Vaccinating a fraction $p$ of newborns removes them from the susceptible class. In Eq. (28.3) this replaces the inflow $\mu$ by $\mu(1 - p)$, which is equivalent to replacing $R_0$ by $R_0(1 - p)$ in the invasion condition.

**Proposition 28.3.2 (Critical Vaccination Coverage)** With a fraction $p$ of newborns immunized for life by a fully effective vaccine, the infection is eliminated if and only if

$$
p > p_{\mathrm{c}} = 1 - \frac{1}{R_0}.
$$

**Proof** With inflow $\mu(1 - p)$, the disease-free state has $s = 1 - p$, and a rare infection grows if and only if $\beta(1 - p) > \gamma + \mu$, that is $R_0(1 - p) > 1$. The rest of Proposition 28.3.1 applies with $R_0$ replaced by $R_0(1 - p)$. $\square$

This is **herd immunity**: the unvaccinated are protected because chains of transmission cannot be sustained. The thresholds vary greatly among infections (Figure 3A), from about 40 % for seasonal influenza to more than 90 % for measles and pertussis, which explains why measles returns quickly when coverage drops below 90–95 %, and why smallpox ($R_0 \approx 5$) was the first infection to be eradicated. A vaccine that is only partially effective, with efficacy $e$, requires coverage $p_{\mathrm{c}}/e$, which may exceed 1.

Vaccination below the threshold still reduces the total number of infections, but it has a side effect. It lowers the force of infection, so the remaining infections occur at older ages: the mean age at infection rises as $1/[\mu(R_0(1 - p) - 1)]$. For most infections this is harmless, but for rubella, whose danger is to the fetus when a woman is infected in early pregnancy (congenital rubella syndrome), the number of infections in women of childbearing age falls much more slowly than the total and can even rise at low coverage (Figure 3B). Anderson and May (1983) warned that low coverage could increase congenital rubella; Greece, where coverage of infants remained low in the 1980s, had a congenital rubella epidemic in 1993 after the mean age at infection had shifted into the reproductive years (Panagiotopoulos and colleagues 1999). Programs must therefore either reach high coverage quickly or, as the United Kingdom did from 1970 to 1988, vaccinate girls before puberty only, leaving the circulation among children, and thereby natural immunity, intact.

![Vaccination. A: the critical coverage for elimination, p_c = 1 − 1/R₀ (Proposition 28.3.2), with commonly cited ranges of R₀ for several infections marked on the curve; the shaded region is coverage sufficient for elimination. B: incomplete vaccination of newborns against rubella (R₀ = 7, rectangular survival to 70 years). The force of infection falls with coverage p, so the mean age at infection rises (blue, left axis). Relative to no vaccination (right axis), total infections fall in proportion to the coverage gap (dashed), but infections at ages 15–45, which carry the risk of congenital rubella syndrome, fall much more slowly and even rise slightly at low coverage (red)](./plots/vaccination.py)

## 28.4. Parasites and Host Population Regulation

### 28.4.1. Microparasites

Can a pathogen regulate a growing host population, as predators can ([7.19.13](/7.19.13#sec-13.2))? Anderson and May (1979, 1981) analyzed a family of models. In the simplest, the host population $N = S + I$ grows with per capita birth rate $b$ (all newborns susceptible, infected hosts breeding as well) and death rate $d$, so that $r = b - d > 0$ in the absence of disease; infected hosts suffer the extra mortality $\alpha$ and recover at rate $\gamma$ to the susceptible class; transmission is density dependent:

$$
\frac{\mathrm{d}S}{\mathrm{d}t} = bN - dS - \beta SI + \gamma I, \qquad \frac{\mathrm{d}I}{\mathrm{d}t} = \beta SI - (\alpha + d + \gamma)I, \qquad \frac{\mathrm{d}N}{\mathrm{d}t} = rN - \alpha I. \tag{28.5}
$$

**Proposition 28.4.1 (Regulation by a Microparasite)** Eq. (28.5) has an equilibrium with $N^* > 0$ if and only if $\alpha > r$; it is then

$$
N^* = \frac{\alpha}{\alpha - r}N_{\mathrm{T}}, \qquad \frac{I^*}{N^*} = \frac{r}{\alpha}, \qquad N_{\mathrm{T}} = \frac{\alpha + d + \gamma}{\beta}.
$$
If $\alpha < r$, the pathogen cannot regulate the host, which grows indefinitely (asymptotically at the rate $r - \alpha$, with almost all hosts infected).

**Proof** At an equilibrium with $I^* > 0$, the $I$-equation gives $S^* = N_{\mathrm{T}}$, and $\dot N = 0$ gives $I^* = rN^*/\alpha$. Then $N^* = S^* + I^* = N_{\mathrm{T}} + rN^*/\alpha$, so $N^*(1 - r/\alpha) = N_{\mathrm{T}}$, which has a positive solution if and only if $\alpha > r$. If $\alpha < r$, then $\dot N = rN - \alpha I \ge (r - \alpha)N > 0$, so $N$ grows at least exponentially; as $N \to \infty$ the prevalence $I/N$ tends to 1, because transmission $\beta SI$ grows faster than the losses, and $\dot N \approx (r - \alpha)N$. $\square$

The result is intuitive: even if every host is infected, the population still grows if the extra mortality caused by the infection is less than the host's intrinsic rate of increase. Regulation thus requires a pathogen that is virulent relative to the host's growth rate, and a host density above the threshold $N_{\mathrm{T}}$. Two further features follow from the formula (Figure 4A, B). The regulated host density is lowest at intermediate virulence: a mild pathogen ($\alpha$ just above $r$) kills too little, a very virulent one kills its hosts so fast that it raises $N_{\mathrm{T}}$. And the prevalence at equilibrium, $r/\alpha$, is low for virulent pathogens, so a regulating pathogen can be inconspicuous in field samples. Models with immunity, latent periods and free-living infective stages show that pathogens can also generate host cycles; Anderson and May (1980) applied such a model to the baculoviruses of forest Lepidoptera, whose long-lived virus particles in the environment provide the delay.

### 28.4.2. Macroparasites

For macroparasites the variables are the host population $H$ and the total number of parasites $P$, or the mean burden $m = P/H$. Let parasites reduce host survival in proportion to their number, with the extra host mortality $\alpha i$ for a host with $i$ worms, and let adult parasites produce infective stages at rate $\lambda$, of which a fraction $H/(H_0 + H)$ reaches a host; adult parasites die at rate $\mu$, die with their host when it dies naturally (rate $b$, assuming host births balance natural deaths except for the growth rate $r$) or from the infection. The loss of parasites through parasite-induced host mortality is $\alpha\sum_i i^2p_i H$, and for the negative binomial distribution, Eq. (28.1), $\sum_i i^2p_i = m + m^2(k + 1)/k$. Anderson and May (1978) obtained

$$
\frac{\mathrm{d}H}{\mathrm{d}t} = (r - \alpha m)H, \qquad \frac{\mathrm{d}m}{\mathrm{d}t} = m\Bigl[\frac{\lambda H}{H_0 + H} - (\mu + b + \alpha)\Bigr] - \frac{\alpha}{k}m^2. \tag{28.6}
$$
The last term, derived from the variance of the burden, is a density-dependent loss of parasites: because most parasites are in heavily infected hosts, the hosts that die from infection take disproportionately many parasites with them.

**Proposition 28.4.2 (Regulation by an Aggregated Macroparasite)** Eq. (28.6) has an equilibrium with $H^*, m^* > 0$ if and only if $\lambda > \mu + b + \alpha + r/k$; then

$$
m^* = \frac{r}{\alpha}, \qquad H^* = H_0\,\frac{\mu + b + \alpha + r/k}{\lambda - (\mu + b + \alpha + r/k)},
$$
and the equilibrium is locally asymptotically stable for every finite $k$. As $k \to \infty$ (random distribution of parasites) the stabilizing effect vanishes.

**Proof** $\dot H = 0$ with $H > 0$ gives $m^* = r/\alpha$; substituting into $\dot m = 0$ gives $\lambda H^*/(H_0 + H^*) = \mu + b + \alpha + r/k$, solvable with $H^* > 0$ exactly under the stated condition. With $g(H) = \lambda H/(H_0 + H)$, the Jacobian at the equilibrium is

$$
J = \begin{bmatrix} 0 & -\alpha H^* \\ m^*g'(H^*) & g(H^*) - (\mu + b + \alpha) - 2\alpha m^*/k \end{bmatrix} = \begin{bmatrix} 0 & -\alpha H^* \\ m^*g'(H^*) & -r/k \end{bmatrix},
$$
since $g(H^*) - (\mu + b + \alpha) = r/k = \alpha m^*/k$. Thus $\operatorname{tr}J = -r/k < 0$ and $\det J = \alpha H^*m^*g'(H^*) > 0$: the equilibrium is a sink. As $k \to \infty$ the trace tends to zero and the linearization becomes a center, the neutral case of the Lotka–Volterra model. $\square$

Aggregation of parasites thus plays the role that aggregation of parasitoid attacks plays in [7.19.27](/7.19.27#sec-27.3): it is the main stabilizing factor of the interaction (Figure 4C). A parasite that reduces host fecundity rather than survival does not remove parasites with their hosts, and parasites with arrested larval stages respond to host density with a delay; both effects are destabilizing. Dobson and Hudson (1992) built them into a model of the red grouse and its nematode *Trichostrongylus tenuis*, and the model produced cycles when the parasite's effect on fecundity was large relative to the stabilizing effect of aggregation; anthelmintic treatment of grouse reduced the amplitude of the population crashes (Hudson, Dobson and Newborn 1998), although, as discussed in [7.19.13](/7.19.13#sec-13.4.4), territorial behavior also contributes to the cycles.

![Regulation of hosts by parasites. A: the microparasite model, Eq. (28.5), with host birth rate b = 1 and death rate d = 0.5 (r = 0.5), transmission β = 0.01 and recovery γ = 0.5; host numbers (log scale) for virulence α = 0.3 < r (unregulated: the host grows exponentially although almost every host is infected) and α = 1 and 2 > r (regulated at N* = N_T α/(α − r) = 400, dotted, after damped oscillations; Proposition 28.4.1). B: the regulated host density N* and the equilibrium prevalence r/α against virulence: no regulation for α ≤ r, strongest suppression at intermediate virulence, and low prevalence when the pathogen is very virulent. C: the macroparasite model, Eq. (28.6), with r = 0.5, α = 0.1, λ = 10, H₀ = 10 and μ + b = 2: with aggregated worms (k = 0.5, k = 5) host numbers converge to a stable equilibrium (Proposition 28.4.2); with a random distribution of worms (k → ∞) the equilibrium is neutral and the populations oscillate indefinitely](./plots/anderson-may.py)

### 28.4.3. Evidence from Wild Populations

Demonstrating regulation by parasites requires experiments that remove parasites, and these are rare. The evidence from natural "experiments" and from treatment studies includes:

- Rinderpest, a morbillivirus of cattle and wild ungulates, entered Africa in the 1880s and killed most of the buffalo, wildebeest and cattle of East Africa. After vaccination of cattle around the Serengeti in the early 1960s eliminated it from the wild ungulates, the migratory wildebeest population increased from about 250,000 to about 1.3 million by the late 1970s, with cascading effects on grasses, fire and predators. Rinderpest was declared eradicated worldwide in 2011.
- Soay sheep on St Kilda, an unmanaged island population, crash every few years in late winter from a combination of malnutrition and nematode infection; sheep treated with anthelmintics survived the crashes better (Gulland 1992).
- Svalbard reindeer: removing nematodes with anthelmintics increased the fecundity of females, and the parasites contributed to the population's fluctuations (Albon and colleagues 2002).
- Wolves on Isle Royale declined from 50 to 14 in 1980–1982, coinciding with the arrival of canine parvovirus, introduced by dogs.

## 28.5. The Evolution of Virulence

### 28.5.1. The Trade-off Hypothesis

Virulence, the harm a parasite does to its host, is not a fixed property of the parasite: it evolves, together with host resistance. The older view that parasites evolve toward harmlessness, because a dead host is useless to them, is wrong in general. In the model of Eq. (28.2), a parasite strain's fitness is its $R_0 = \beta(\alpha)N/(\alpha + \mu + \gamma)$, and if faster within-host replication increases both transmission and virulence, $R_0$ is maximized at an intermediate virulence ([Theorem 17.2.1](/7.10.17#thm-17.2.1) of 7.10.17). The trade-off hypothesis predicts higher virulence when hosts die quickly from other causes, when transmission opportunities are plentiful, and when several strains compete within a host, and lower virulence when transmission is vertical.

The myxoma virus and the European rabbit in Australia remain the classic test. Fenner classified virus strains into five grades by the case fatality in laboratory rabbits, from grade I (more than 99 %, death within about two weeks) to grade V (less than 50 %). The strain released in 1950 was grade I. Within a few years, strains of intermediate virulence (grade III, 70–95 %) dominated in the field, because rabbits infected with them survived longer and were available to mosquito vectors for longer, while the rabbits evolved genetic resistance. Later the virus evolved greater virulence again in Australia, in part by suppressing the immune response of the now more resistant rabbits (Kerr and colleagues 2017): virulence is a moving target in a coevolutionary arms race (**coevolution**, [7.10.17](/7.10.17)).

### 28.5.2. Is a Highly Lethal Pathogen "Unsuccessful"?

Ebola virus disease kills, on average, about half of the people it infects, and the West African epidemic of 2013–2016 caused more than 28,000 cases and 11,000 deaths. It is sometimes said that such a virus is "unsuccessful" because it kills its hosts. Two ecological points correct this. First, high case fatality need not reduce transmission much: Ebola is transmitted mostly late in the illness and from the bodies of the dead, through care and burial practices, so death does not end the infectious period. Second, humans are not the virus's normal host. The reservoir is probably among fruit bats, in which the virus causes little disease, and human infections are spillovers into a dead-end or short-chain host. Virulence in a spillover host is not shaped by selection in that host; it is a by-product of adaptation elsewhere, and the trade-off theory, which concerns selection in the host in which the parasite circulates, does not apply. The same holds for many zoonoses (avian influenza H5N1 in humans, rabies).

### 28.5.3. Phylodynamics

Many RNA viruses evolve on the same time scale as their epidemics, so their genetic sequences record their population dynamics. Grenfell and colleagues (2004) called the joint study of epidemiological and evolutionary dynamics *phylodynamics*. Human influenza A (H3N2) shows its signature most clearly: its phylogeny has a single trunk with short side branches, a "ladder", because herd immunity against current strains favors new antigenic variants (**antigenic drift**), each of which sweeps through the population and is replaced within a few years; antigenic cartography shows the virus moving through clusters that are replaced every three years or so (Smith and colleagues 2004). The variants of SARS-CoV-2 that replaced each other worldwide from 2020 (Alpha, Delta, Omicron and its descendants) show the same population genetics of successive selective sweeps, with Omicron emerging as a highly divergent lineage, probably from long-term evolution in a chronically infected person. The genetics and immunology are treated in [7.11.35](/7.11.35) and [7.15](/7.15); for population ecology the lesson is that host immunity is a resource that the virus depletes, and that selection by herd immunity shapes both the virus's phylogeny and the timing of epidemics.

## 28.6. Disease in Wild Populations and Conservation

Theory says that a pathogen with density-dependent transmission and no other hosts cannot drive its host to extinction: as host density falls below $N_{\mathrm{T}}$, the pathogen disappears first. Extinction by disease therefore requires frequency-dependent transmission, a reservoir in other host species or in the environment, or a host population already small for other reasons. Several emerging diseases of wildlife have exactly these properties.

- Chytridiomycosis. The chytrid fungus *Batrachochytrium dendrobatidis* (Bd), a **chytrid** spread around the world from East Asia, probably through the trade in amphibians, infects the skin of frogs, disrupts electrolyte balance and kills by cardiac arrest. Its zoospores persist in water and it infects many tolerant reservoir species, so it does not disappear when susceptible species decline. A global assessment attributed declines in at least 501 amphibian species, including about 90 presumed extinctions, to the disease (Scheele and colleagues 2019), the greatest loss of biodiversity attributed to any pathogen; the related *B. salamandrivorans* has since devastated fire salamanders in the Netherlands and Belgium.
- White-nose syndrome. The fungus *Pseudogymnoascus destructans*, introduced from Europe, was first recorded in a cave in New York in 2006. It grows on hibernating bats, causing them to arouse repeatedly and exhaust their fat reserves; because bats hibernate in dense clusters, transmission is effectively independent of the total population size. Populations of the little brown bat, the northern long-eared bat and the tricolored bat in eastern North America declined by more than 90 %.
- Devil facial tumor disease. Tasmanian devils are threatened by a transmissible cancer, a clonal cell line passed between animals by bites during social interactions. First seen in 1996, it has reduced the devil population by about 80 %. Because biting occurs during mating and feeding regardless of density, transmission is frequency dependent, and models predicted extinction; however, devil populations have persisted at low densities, and genomic studies show rapid evolution of resistance in the devils (Epstein and colleagues 2016). A second, independent transmissible tumor was discovered in 2014.

Two broader ideas connect disease and community ecology. The **dilution effect** hypothesis holds that diverse host communities reduce disease risk when the additional species are poor hosts for the pathogen or its vector, as has been argued for Lyme disease, where white-footed mice are highly competent reservoirs and many other hosts of the tick vector are not; whether diversity generally reduces disease is debated, because the outcome depends on which species are lost first. And parasites are part of food webs: they reshape the trophic links of their hosts through **host manipulation** and are themselves prey ([7.19.38](/7.19.38)). Diseases of wildlife and the management of zoonotic spillover are part of conservation biology ([7.19.52](/7.19.52)).

## Summary

- Microparasites multiply in the host and are modeled by host classes (S, I, R); macroparasites do not multiply in the host and are modeled by burden distributions (Definition 28.1.1). Parasitoids, social parasites and brood parasites are related consumers. Hosts are patchy, mortal and reactive habitats; resistance and tolerance are distinct defenses.
- Macroparasites are aggregated among hosts, negative binomial with $k < 1$ typical (Eq. (28.1)): most hosts carry few parasites, a few carry most.
- Transmission is density dependent ($\beta SI$) or frequency dependent ($\beta'SI/N$) (Definition 28.2.1); $R_0 = \beta N/(\alpha + \mu + \gamma)$ for density-dependent infections, which have a threshold host density $N_{\mathrm{T}}$ (Definition 28.2.2); frequency-dependent ones do not. Immunizing infections also need a critical community size (measles: 250,000–500,000).
- SIR with demography (Proposition 28.3.1): endemic equilibrium $s^* = 1/R_0$, globally stable (Lyapunov function), approached by damped oscillations with period $2\pi\sqrt{AD}$; $R_0 \approx 1 + L/A$. Seasonal forcing sustains annual, biennial or irregular epidemics.
- Elimination requires vaccination coverage $p > 1 - 1/R_0$ (Proposition 28.3.2); incomplete coverage raises the age at infection, which for rubella can sustain congenital rubella.
- Microparasites regulate hosts only if virulence exceeds the host's growth rate, $\alpha > r$, with $N^* = \alpha N_{\mathrm{T}}/(\alpha - r)$ and prevalence $r/\alpha$ (Proposition 28.4.1). Aggregated macroparasites regulate hosts stably for finite $k$ (Proposition 28.4.2). Field evidence: rinderpest and wildebeest, Soay sheep, Svalbard reindeer, red grouse.
- Virulence evolves toward an intermediate optimum under a transmission–virulence trade-off (myxoma and rabbits); virulence in spillover hosts (Ebola in humans) is not adaptive. Phylodynamics links viral phylogenies to herd immunity.
- Disease can drive hosts extinct when transmission is frequency dependent or reservoirs exist: chytridiomycosis, white-nose syndrome, devil facial tumor disease.

## Questions

1. Measles in a population with life expectancy 60 years has a mean age at infection of 5 years and an infectious period of 10 days. Estimate $R_0$, the critical vaccination coverage, and the interepidemic period.

   **Answer** $R_0 \approx 1 + L/A = 1 + 60/5 = 13$; $p_{\mathrm{c}} = 1 - 1/13 \approx 0.92$. With $A = 5$ years and $D = 10/365 \approx 0.027$ years, $T \approx 2\pi\sqrt{AD} = 2\pi\sqrt{0.137} \approx 2.3$ years. In practice seasonal forcing locks the epidemics into a biennial pattern.
2. Explain why a pathogen with density-dependent transmission cannot by itself drive its only host to extinction, while one with frequency-dependent transmission can.

   **Answer** With density-dependent transmission, $R_0 = \beta N/(\alpha + \mu + \gamma)$ falls with host density, and below $N_{\mathrm{T}}$ each infected host infects fewer than one other, so the pathogen dies out while hosts remain, and the host can recover. With frequency-dependent transmission $R_0 = \beta'/(\alpha + \mu + \gamma)$ does not depend on $N$; if it exceeds 1, the infection persists at a positive prevalence however few hosts remain, and if its virulence exceeds the host's growth rate it can push the host to zero (in deterministic models asymptotically, in finite populations to actual extinction).
3. In the model (28.5), with $b = 1$, $d = 0.5$, $\beta = 0.01$ and $\gamma = 0.5$, what virulence minimizes the equilibrium host density, and what is that density?

   **Answer** $N^*(\alpha) = \frac{\alpha(\alpha + d + \gamma)}{\beta(\alpha - r)}$ with $r = 0.5$ and $d + \gamma = 1$: $N^* = 100\,\alpha(\alpha + 1)/(\alpha - 0.5)$. Setting the derivative of $\ln N^* = \ln\alpha + \ln(\alpha + 1) - \ln(\alpha - 0.5)$ to zero gives $1/\alpha + 1/(\alpha + 1) = 1/(\alpha - 0.5)$, so $(2\alpha + 1)(\alpha - 0.5) = \alpha(\alpha + 1)$, that is $\alpha^2 - \alpha - 0.5 = 0$ and $\alpha = (1 + \sqrt3)/2 \approx 1.37$. Then $N^* = 100 \times 1.37 \times 2.37/0.87 \approx 373$, the minimum in Figure 4B.
4. Why does the aggregation of macroparasites stabilize their interaction with the host, and why does a parasite that reduces host fecundity rather than survival tend to destabilize it?

   **Answer** When parasites are aggregated, the hosts that die from infection are the heavily infected ones, so each death removes many parasites: parasite mortality rises more than proportionally with the mean burden ($\alpha(k + 1)m^2/k$ per host), a density-dependent loss that damps the interaction (Proposition 28.4.2, $\operatorname{tr}J = -r/k$). A parasite that reduces fecundity reduces host recruitment without killing the hosts and their parasites, so this density-dependent removal of parasites is absent, and the reduction in recruitment acts on the next generation, a delayed effect; delayed regulation without compensating direct density dependence produces oscillations, as in the grouse–nematode system.
5. (Open problem) A new fungal disease appears in a bat species that hibernates in a few large colonies. Which data would you need to decide whether the disease threatens the species with extinction, and what management options does the theory suggest?

   **Answer** The key questions are whether transmission depends on density or on frequency (measure infection rates in colonies of different sizes; in dense hibernation clusters transmission may be nearly independent of the total population), whether the pathogen persists in the environment or in other species (sample cave sediments and co-occurring species), the virulence and how it depends on temperature and humidity, and whether some individuals or populations survive (heritable resistance or tolerance). If transmission is frequency dependent or environmental reservoirs exist, the theory predicts no threshold and possible extinction; culling would not help and could harm. Options: reduce environmental loads (decontamination, protocols for cavers), manipulate microclimate to slow fungal growth, protect uninfected colonies from introduction, treat bats (probiotics, antifungals) during hibernation, and support populations with evolving resistance; monitoring by repeated counts and genomic analysis tracks the outcome.
