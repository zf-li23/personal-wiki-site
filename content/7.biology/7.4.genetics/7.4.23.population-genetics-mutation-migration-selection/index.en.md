---
title: "Population Genetics II: Mutation, Migration, Selection and Drift"
description: "The four forces that change allele frequencies and their formulas. Mutation pressure and its equilibrium; gene flow and the island model; fitness, selection coefficients and dominance, the general one-locus recursion and its special cases, times to change under selection, heterozygote advantage (sickle-cell hemoglobin and malaria), underdominance and frequency-dependent selection; mutation–selection balance, Haldane's estimates of mutation rates and genetic load; genetic drift in the Wright–Fisher model, loss of heterozygosity, fixation probabilities and times, effective population size, founder effects and bottlenecks; drift and selection together (Kimura); the neutral theory and the molecular clock; human genetic ancestry and lactase persistence."
---

The Hardy–Weinberg law ([7.4.22](/7.4.22)) holds only when nothing changes the **allele** frequencies. Real populations are finite, mutate, exchange migrants and leave unequal numbers of offspring, and each of these violations is a force that changes the **gene** pool: **mutation** creates new alleles, migration (gene flow) homogenizes populations, natural selection changes frequencies in a direction set by fitness, and genetic drift changes them at random. Evolution, in its population-genetic definition, is change in allele frequencies, and this chapter derives the classical one-locus theory of the four forces: the recursions that describe each, their equilibria and their time scales, and the cases in which two forces balance (mutation and selection, migration and drift, drift and selection). The theory was built in the 1920s and 1930s by R. A. Fisher, J. B. S. Haldane and Sewall Wright, and completed by Motoo Kimura's diffusion theory in the 1950s–1960s; it remains the quantitative core of evolutionary genetics.

The chapter takes what genetics needs: the formulas behind disease-allele frequencies, **mutation rates**, founder effects, the persistence of the sickle-cell allele and the logic of the neutral theory. Genealogical (coalescent) theory, molecular tests of selection ($d_N/d_S$, McDonald–Kreitman, Tajima's $D$), speciation, phylogenetics and the quantitative theory of phenotypic evolution belong to evolutionary biology (7.10); selection on **quantitative traits**, the **breeder's equation**, follows in [7.4.24](/7.4.24). The mathematics is that of difference equations and their continuous limits ([2.4](/2.4)), of the **binomial distribution** ([3.1.4](/3.1.4#sec-4.1.3)) and of **Markov chains** ([3.5.9](/3.5.9)). Notation: $p$ and $q = 1 - p$ are the frequencies of alleles $A$ and $a$; a prime ($p'$) denotes the next generation; $\Delta p = p' - p$.

## 23.1. Mutation

Let $A$ mutate to $a$ at rate $\mu$ per gene copy per generation (**forward mutation**) and $a$ to $A$ at rate $\nu$ (**reverse mutation**). In an infinite population

$$
p' = p(1 - \mu) + q\nu, \qquad \Delta p = -\mu p + \nu q. \tag{23.1}
$$

**Formula 23.1.1 (Mutation Equilibrium)** The frequency of $a$ approaches the equilibrium

$$
\hat q = \frac{\mu}{\mu + \nu}, \qquad q_t - \hat q = (q_0 - \hat q)(1 - \mu - \nu)^t \approx (q_0 - \hat q)\,\mathrm{e}^{-(\mu + \nu)t}. \tag{23.2}
$$

**Proof** Setting $\Delta p = 0$ in Eq. (23.1) gives $\mu\hat p = \nu\hat q$, hence $\hat q = \mu/(\mu + \nu)$. Subtracting the equilibrium from Eq. (23.1) written for $q$, $q' - \hat q = (1 - \mu - \nu)(q - \hat q)$, which iterates to Eq. (23.2). $\square$

**Example 23.1.1** With $\mu = 10^{-5}$ and $\nu = 10^{-6}$ (reverse mutations, which must restore a specific function, are usually rarer), $\hat q = 10^{-5}/(1.1 \times 10^{-5}) = 0.91$, and the half-life of a departure from equilibrium is $\ln 2/(\mu + \nu) = 63\,000$ generations, more than a million years in humans.

Mutation is thus a weak force for changing frequencies; its importance is that it is the only source of new alleles, the raw material on which the other forces act. Mutation rates and their measurement are treated in [7.4.12](/7.4.12); here a rate of $10^{-5}$–$10^{-6}$ per gene and $10^{-8}$ per nucleotide per generation (humans) is enough.

## 23.2. Migration

**Definition 23.2.1 (Gene Flow)** **Gene flow** is the transfer of alleles between populations by the movement of individuals or gametes (pollen, spores) followed by reproduction. Its simplest model is the island model of migration: in each generation a fraction $m$ of the breeding individuals of a population are immigrants from a source (a continent, or a large pool of populations) with constant **allele frequency** $P$.

**Formula 23.2.1 (Island Model)** With migration rate $m$ from a source with frequency $P$,

$$
p' = (1 - m)p + mP, \qquad p_t - P = (1 - m)^t(p_0 - P). \tag{23.3}
$$

**Example 23.2.1** An island population with $p_0 = 0.1$ receives $m = 0.01$ migrants per generation from a continent with $P = 0.5$. After 50 generations $p_{50} = 0.5 - 0.4 \cdot 0.99^{50} = 0.258$; half the initial difference is eliminated in $\ln 2/m \approx 69$ generations.

The same equation read once describes admixture: if a hybrid population derives a fraction $m$ of its genes from population 1 (frequency $p_1$) and $1 - m$ from population 2 ($p_2$), then $p_{\mathrm{h}} = mp_1 + (1 - m)p_2$, and $m = (p_{\mathrm{h}} - p_2)/(p_1 - p_2)$. Estimates from many loci (or, today, from the local ancestry of **chromosome** segments) give admixture proportions of human populations, such as the European, African and Native American fractions of the **genomes** of people in the Americas. Migration homogenizes: without other forces every population converges to the source frequency. It is opposed by local selection (a cline results) and by drift, which differentiates small populations; the balance between drift and migration is in §23.5.4.

## 23.3. Natural Selection

### 23.3.1. Fitness and the One-Locus Recursion

**Definition 23.3.1 (Fitness and Selection Coefficient)** The (Darwinian) **fitness** of a **genotype** is its average contribution of offspring to the next generation, combining survival to reproductive age, mating success and fertility; the absolute fitness $W_{ij}$ of genotype $A_iA_j$ is the mean number of offspring (more precisely, of zygotes of the next generation) per individual. The **relative fitness** $w_{ij} = W_{ij}/W_{\max}$ is fitness relative to a reference genotype, usually the fittest. The **selection coefficient** $s = 1 - w$ is the proportional reduction of fitness of a genotype relative to the reference; the dominance coefficient $h$ describes the fitness of the **heterozygote**, in the standard parameterization

$$
w_{AA} = 1, \qquad w_{Aa} = 1 - hs, \qquad w_{aa} = 1 - s
$$

($h = 0$: $a$ is recessive for fitness; $h = 1$: dominant; $h = 1/2$: additive, no dominance; $h < 0$: heterozygote advantage).

Only relative fitness matters for the change of frequencies, because the absolute values cancel in the recursion. In the life cycle of the model, zygotes are formed in Hardy–Weinberg proportions, genotypes survive and reproduce in proportion to their fitnesses, and the gametes of the survivors form the next zygotes.

**Theorem 23.3.1 (One Generation of Selection)** With genotype fitnesses $w_{11}, w_{12}, w_{22}$ for $AA$, $Aa$, $aa$ and zygotes in Hardy–Weinberg proportions,

$$
\bar w = p^2w_{11} + 2pqw_{12} + q^2w_{22}, \qquad p' = \frac{p^2w_{11} + pqw_{12}}{\bar w}, \tag{23.4}
$$

and the change is

$$
\Delta p = \frac{pq\,[\,p(w_{11} - w_{12}) + q(w_{12} - w_{22})\,]}{\bar w} = \frac{pq}{2\bar w}\,\frac{\mathrm{d}\bar w}{\mathrm{d}p}. \tag{23.5}
$$

**Proof** After selection the genotypes are in the ratio $p^2w_{11} : 2pqw_{12} : q^2w_{22}$; dividing by the total $\bar w$ (the mean fitness) gives frequencies, and the frequency of $A$ among the gametes of the survivors is the frequency of $AA$ plus half that of $Aa$, which is Eq. (23.4). Then $\Delta p = [p^2w_{11} + pqw_{12} - p\bar w]/\bar w$; substituting $\bar w$ and using $p - p^2 = pq$, the numerator is $p^2w_{11} + pqw_{12} - p^3w_{11} - 2p^2qw_{12} - pq^2w_{22} = pq[pw_{11} + (1 - 2p)w_{12} - qw_{22}]$, which equals $pq[p(w_{11} - w_{12}) + q(w_{12} - w_{22})]$. Differentiating $\bar w$ with $q = 1 - p$ gives $\mathrm{d}\bar w/\mathrm{d}p = 2[p(w_{11} - w_{12}) + q(w_{12} - w_{22})]$, hence the second form. $\square$

The second form of Eq. (23.5) is Wright's: selection moves the allele frequency uphill on the curve of mean fitness $\bar w(p)$, at a speed proportional to the genetic variability $pq$; mean fitness increases (Fisher's fundamental theorem in its simplest form) and stops changing only at an equilibrium where $\Delta p = 0$, namely at $p = 0$, $p = 1$, or where the bracket vanishes.

**Formula 23.3.1 (Change in Allele Frequency for the Main Cases)** With the parameterization of Definition 23.3.1, the change in the frequency $q$ of the disfavored allele $a$ is

| Selection | Fitnesses $AA : Aa : aa$ | $\Delta q$ | Rare $a$ ($q \to 0$) |
|---|---|---|---|
| against a recessive | $1 : 1 : 1 - s$ | $-\dfrac{spq^2}{1 - sq^2}$ | $\approx -sq^2$ |
| against a dominant | $1 : 1 - s : 1 - s$ | $-\dfrac{sp^2q}{1 - s(1 - p^2)}$ | $\approx -sq$ |
| additive | $1 : 1 - s/2 : 1 - s$ | $-\dfrac{\tfrac12 spq}{1 - sq}$ | $\approx -\tfrac12 sq$ |
| general $h$ | $1 : 1 - hs : 1 - s$ | $-\dfrac{spq[\,q + h(p - q)\,]}{\bar w}$ | $\approx -hsq$ |


The decisive feature is the power of $q$ in the last column. Selection acts on **phenotypes**, so a rare allele that is recessive for fitness is exposed only in **homozygotes**, which have frequency $q^2$: its change per generation is of second order in $q$, while that of an allele expressed in heterozygotes is of first order.

**Formula 23.3.2 (Time to Change Under Genic Selection)** If each $A$ allele multiplies fitness by $1 + s$ relative to $a$ (genic or multiplicative selection, which in **diploids** is close to additive for small $s$), the odds of $A$ grow geometrically, $p_t/q_t = (1 + s)^t\,p_0/q_0$, so

$$
t = \frac{1}{\ln(1 + s)}\,\ln\frac{p_tq_0}{p_0q_t} \approx \frac1s\ln\frac{p_tq_0}{p_0q_t}. \tag{23.6}
$$

**Example 23.3.1** An allele with $s = 0.01$ goes from $p = 0.01$ to $0.99$ in $\ln(0.99^2/0.01^2)/\ln 1.01 = 9.19/0.00995 = 924$ generations: selection of $1\,\%$, invisible in any field study, changes a population completely in about 25 000 years of human generations. The trajectory is the logistic curve $p_t = 1/(1 + \mathrm{e}^{-s(t - t_{1/2})})$, the solution of the continuous approximation $\mathrm{d}p/\mathrm{d}t = spq$ ([2.4](/2.4)).

**Formula 23.3.3 (Selection Against a Recessive Lethal)** If $aa$ has fitness $0$ and $AA$ and $Aa$ fitness $1$, then

$$
q' = \frac{q}{1 + q}, \qquad q_t = \frac{q_0}{1 + tq_0}, \qquad t = \frac{1}{q_t} - \frac{1}{q_0}. \tag{23.7}
$$

**Proof** With $s = 1$ in the first row of Formula 23.3.1, $q' = q - pq^2/(1 - q^2) = q - q^2/(1 + q) = q/(1 + q)$. Hence $1/q' = 1/q + 1$, so $1/q_t = 1/q_0 + t$. $\square$

**Example 23.3.2** Halving the frequency of a recessive **lethal allele** from $0.01$ to $0.005$ takes $200 - 100 = 100$ generations, about 2500 years; from $0.001$ to $0.0005$ it takes 1000 generations. This is why the program of the early twentieth-century eugenics movement, to rid a population of recessive conditions by preventing affected people from reproducing, could never have worked even on its own terms (apart from its ethical indefensibility): almost all copies of a rare recessive allele are in heterozygous **carriers** ([7.4.22](/7.4.22), Eq. (22.2)), which selection on affected homozygotes does not touch.

The three cases of dominance are compared in the figure. A favored dominant allele rises quickly while rare but stalls near fixation, because the last copies of the recessive allele hide in heterozygotes; a favored recessive allele takes a long time to start. In finite populations a new recessive beneficial mutation is therefore usually lost by drift before selection can see it, so adaptive substitutions are biased toward dominant mutations (Haldane's sieve).

![Deterministic selection at one locus. A: a favored allele with fitnesses 1 + s (AA), 1 + hs (Aa), 1 (aa), s = 0.05, from p = 0.01. A dominant favored allele (h = 1) spreads fast while rare and slowly near fixation; a recessive one (h = 0) is nearly invisible to selection while rare; the additive case (h = 1/2) is the symmetric logistic curve. B: decline of a deleterious recessive allele from q = 0.1 under complete selection (s = 1), which follows q_t = q_0/(1 + t q_0) exactly (Formula 23.3.3, dashed), and under s = 0.2; at low frequency, halving q takes about 1/(sq) generations](./plots/selection-trajectories.py)

### 23.3.2. Forms of Selection and Balanced Polymorphism

**Definition 23.3.2 (Forms of Selection)** **Natural selection** is the differential survival and reproduction of individuals because of differences in phenotype; when the phenotypic differences are heritable, it changes allele frequencies. With respect to a **locus**:

- **directional selection** moves an allele frequency consistently in one direction until fixation or loss: *positive selection* increases a new favorable allele, *purifying selection* removes deleterious mutations;
- **balancing selection** actively maintains two or more alleles at intermediate frequencies; its main forms are **heterozygote advantage** (overdominance), in which the heterozygote is fitter than both homozygotes, and negative **frequency-dependent selection**, in which the fitness of an allele or phenotype decreases as it becomes common;
- **underdominance** (heterozygote disadvantage) is the opposite case, in which the heterozygote is less fit than both homozygotes.

For quantitative traits one also distinguishes directional, stabilizing and disruptive selection, according to whether the extreme, the intermediate or both extreme phenotypes are favored ([7.4.24](/7.4.24)).

**Theorem 23.3.2 (Heterozygote Advantage)** Let the fitnesses be $w_{AA} = 1 - s_1$, $w_{Aa} = 1$, $w_{aa} = 1 - s_2$ with $s_1, s_2 > 0$. Then there is a unique interior equilibrium

$$
\hat p = \frac{s_2}{s_1 + s_2}, \qquad \hat q = \frac{s_1}{s_1 + s_2}, \tag{23.8}
$$

which is globally stable for $0 < p < 1$. The mean fitness at equilibrium is $\bar w = 1 - s_1s_2/(s_1 + s_2)$. With $s_1, s_2 < 0$ (underdominance) the same point is an unstable equilibrium, and the allele initially above it goes to fixation.

**Proof** By Eq. (23.5), $\Delta p = pq[p(-s_1) + q s_2]/\bar w$, which vanishes for $0 < p < 1$ only when $s_1p = s_2q$, that is $p = s_2/(s_1 + s_2)$. For $p < \hat p$ the bracket $s_2q - s_1p$ is positive, so $p$ increases; for $p > \hat p$ it decreases: the equilibrium attracts. With negative $s_i$ the signs reverse. The mean fitness is $1 - s_1\hat p^2 - s_2\hat q^2 = 1 - s_1s_2/(s_1 + s_2)$. $\square$

**Example 23.3.3 (Sickle-Cell Hemoglobin and Malaria)** In regions of Africa with intense transmission of *Plasmodium falciparum*, heterozygotes $AS$ for the hemoglobin allele $\mathrm{Hb}^S$ ([7.4.3](/7.4.3)) are partly protected against severe malaria, while $SS$ homozygotes have sickle cell disease. A survey of 12 387 adults in West Africa found 9365 $AA$, 2993 $AS$ and 29 $SS$, so $q_S = (2 \cdot 29 + 2993)/(2 \cdot 12\,387) = 0.123$. If the zygotes were in Hardy–Weinberg proportions at this frequency, the expected adult counts without selection would be $9524$, $2675$ and $188$. The ratios observed/expected, $0.983$, $1.119$ and $0.154$, divided by that of $AS$, estimate the relative viabilities $w_{AA} = 0.88$, $w_{AS} = 1$, $w_{SS} = 0.14$; so $s_1 = 0.12$ and $s_2 = 0.86$. Theorem 23.3.2 then predicts $\hat q = 0.12/(0.12 + 0.86) = 0.122$, in agreement with the observed frequency, as it must be if the population is at equilibrium. The selective advantage of $AS$ over $AA$ is $1/0.88 = 1.14$. (The estimate assumes that adults were sampled after all selection and that the frequency is at equilibrium; it is a classic calculation, not a precise measurement.) The geography confirms the explanation: $\mathrm{Hb}^S$ is frequent in humid lowlands with high malaria transmission and nearly absent at altitude, as around Nairobi, and other malaria-protective alleles (HbC, HbE, thalassemias, G6PD deficiency, the Duffy-null allele) show similar distributions. In malaria-free environments, such as among African Americans, the advantage disappears and the allele slowly declines.

The price of a balanced polymorphism is a segregational load: even at equilibrium a fraction $s_1s_2/(s_1 + s_2)$ of fitness is lost, because Mendelian segregation keeps producing the less fit homozygotes. For HbS this is $0.12 \cdot 0.86/0.98 = 0.105$, mostly malaria deaths of $AA$ children and sickle-cell disease of $SS$ children.

Underdominance cannot maintain polymorphism: the equilibrium is unstable, and a new allele (necessarily rare) is eliminated unless drift carries it past the threshold in a small population. **Chromosomal rearrangements** whose heterozygotes are semisterile ([7.4.15](/7.4.15)) and the maternal–fetal Rh incompatibility are examples; underdominance in hybrids contributes to reproductive isolation between species (7.10). Negative frequency dependence, by contrast, maintains many alleles: the self-incompatibility S alleles of plants ([7.4.22](/7.4.22)), the MHC alleles that confer resistance to pathogens that have adapted to common types, and the left- and right-mouthed morphs of scale-eating cichlid fishes, each of which does better when rare.

![Change in allele frequency per generation as a function of frequency, Eq. (23.5), with phase lines below (arrows: direction of change; filled dots: stable equilibria; open dots: unstable). A: directional additive selection (s = 0.05): the favored allele increases at every frequency, fastest at p = 1/2. B: heterozygote advantage with the sickle-cell fitnesses of Example 23.3.3 (AA 0.88, AS 1, SS 0.14): a stable equilibrium at q = 0.122 (only q < 0.3 is shown). C: heterozygote disadvantage (1, 0.8, 1): the equilibrium at 1/2 is unstable, and the allele that is initially more common is fixed](./plots/delta-q.py)

**Example 23.3.4 (Industrial Melanism in the Peppered Moth)** The melanic form *carbonaria* of the peppered moth *Biston betularia* was first recorded near Manchester in 1848; by 1895 about $98\,\%$ of the moths there were melanic, while rural populations remained mostly of the light form *typica*. The melanic phenotype is dominant, and the moth has one generation per year. If the frequency of melanics was about $1\,\%$ in 1848, the allele frequency was $p_0 = 1 - \sqrt{0.99} = 0.005$, and iterating Theorem 23.3.1 with fitnesses $1 : 1 : 1 - s$ (selection against the recessive *typica*) shows that the change in 47 generations requires $s \approx 0.25$: melanics were about $1/(1 - 0.25) = 1.34$ times as fit as light moths. Haldane (1924), with similar data, obtained a ratio of about 1.5; it was the first estimate of a selection coefficient in a natural population, and it showed that selection could be far stronger than Darwin had supposed. The agent is predation by birds, which find light moths more easily on trunks darkened by soot and stripped of lichens, as Kettlewell's release–recapture experiments of the 1950s and Majerus's experiment of 2001–2007 confirmed. After clean-air legislation in the 1950s, lichens returned and *carbonaria* declined across Britain to below $10\,\%$ in most places by about 2000, at a rate that implies selection of roughly $0.1$–$0.2$ per generation against the melanics. The *carbonaria* allele is an insertion of a transposable element into an **intron** of the gene *cortex* ([7.4.17](/7.4.17)), and the **haplotype** around it dates the mutation to about 1819. Two lessons of the general theory are visible in the figure: selection acts on phenotypes, so the light allele, recessive and hidden in heterozygotes, declined slowly once it was rare; and during the decline the melanic allele, now disfavored but dominant, is exposed in every carrier and falls quickly at first.

![Industrial melanism in the peppered moth as a one-locus model (Example 23.3.4). A: rise of the dominant melanic form *carbonaria* under selection s = 0.25 against the light recessive *typica*, the value that takes the melanic phenotype from 1 % (assumed for 1848) to 98 % (1895) in 47 annual generations near Manchester; the phenotype frequency (solid) runs well ahead of the allele frequency (dashed), and the last light moths disappear slowly because the light allele hides in heterozygotes. B: the decline after air pollution fell, from 90 % melanics, for selection coefficients of 0.1, 0.15 and 0.2 against the melanic phenotype; at s = 0.15 the melanic frequency falls below 10 % (dotted) in about 36 generations](./plots/peppered-moth.py)

## 23.4. Mutation–Selection Balance and Genetic Load

### 23.4.1. Equilibrium Frequencies

Purifying selection removes deleterious alleles that mutation keeps creating; at equilibrium the two rates are equal.

**Theorem 23.4.1 (Mutation–Selection Balance)** Let $A$ mutate to a deleterious allele $a$ at rate $\mu$, with fitnesses $1 : 1 - hs : 1 - s$, and $\mu \ll s$. The equilibrium frequency of $a$ is approximately

$$
\hat q \approx \sqrt{\frac{\mu}{s}} \quad (h = 0), \qquad \hat q \approx \frac{\mu}{hs} \quad (hs \gg \sqrt{\mu s}). \tag{23.9}
$$

For a dominant lethal ($hs = 1$), $\hat q = \mu$: every copy is new.

**Proof** At equilibrium the gain by mutation, about $\mu p \approx \mu$ per generation, equals the loss by selection, which for a rare allele is $sq^2$ if $h = 0$ and about $hsq$ otherwise (Formula 23.3.1). Solving $\mu = s\hat q^2$ and $\mu = hs\hat q$ gives the two cases; the second is the better approximation as soon as the term $hsq$ dominates $sq^2$, that is $h \gg q$. $\square$

**Example 23.4.1** With $\mu = 10^{-5}$, a recessive lethal has $\hat q = \sqrt{10^{-5}} = 0.0032$ and affects $q^2 = \mu = 10^{-5}$ of births. If the same allele reduces the fitness of heterozygotes by only $5\,\%$ ($h = 0.05$, $s = 1$), $\hat q \approx 10^{-5}/0.05 = 2 \times 10^{-4}$, sixteen times lower: even slight expression in heterozygotes is decisive, because heterozygotes are where nearly all copies are. This is the population-genetic basis for the observation that most deleterious mutations are partially recessive rather than fully recessive in their effects on fitness.

![Mutation–selection balance with μ = 10⁻⁵ (Theorem 23.4.1). A: equilibrium frequency of the deleterious allele against the selection coefficient against homozygotes: √(μ/s) for a completely recessive allele and about μ/(hs) when heterozygotes are affected (h = 0.01, 0.05, 0.5); dots: exact equilibria from the recursion. B: approach from q = 0 to the equilibrium of a recessive lethal (√μ = 0.0032, slow) and of a lethal with h = 0.05 (μ/hs = 0.0002, fast)](./plots/mutation-selection.py)

### 23.4.2. Estimating Mutation Rates from Disease Frequencies

Before DNA sequencing, Haldane (1935) used Theorem 23.4.1 backward to estimate human mutation rates: at equilibrium, the new mutations entering a population each generation replace the disease alleles lost by reduced reproduction.

**Formula 23.4.1 (Haldane's Indirect Method)** For an autosomal dominant disease with birth incidence $I$ (affected births per birth, $I \approx 2\hat q$) whose patients have relative fertility $f$,

$$
\mu \approx \tfrac12(1 - f)\,I. \tag{23.10}
$$

For an **X-linked** recessive disease of incidence $I_m$ in male births with relative fertility $f$ of affected males, $\mu \approx \tfrac13(1 - f)I_m$; if the disease is lethal before reproduction ($f = 0$), one third of all affected males carry a new mutation.

**Proof** Autosomal dominant: each affected person carries one disease allele, so $2\hat q \approx I$; selection removes a fraction $1 - f$ of these copies each generation, $(1 - f)I/2$ per gene copy, and mutation adds $\mu$ per gene copy. X-linked: of all X chromosomes, one third are in males; selection removes the fraction $1 - f$ of the disease alleles in males, $(1 - f)I_m$ per male X, which is $(1 - f)I_m/3$ per X chromosome in the population, and mutation adds $\mu$ per X chromosome. When $f = 0$, the loss of $I_m/3$ is balanced by new mutations at rate $\mu = I_m/3$, and since every affected boy's X came from his mother, in whom a new mutation arises with probability $\mu$, a fraction $\mu/I_m = 1/3$ of affected boys carry a new mutation. $\square$

**Example 23.4.2** A dominant condition with birth incidence $1/25\,000$ in which patients have $20\,\%$ of normal fertility gives $\mu \approx 0.8/(2 \cdot 25\,000) = 1.6 \times 10^{-5}$ per gene per generation. For Duchenne muscular dystrophy ($f \approx 0$, $I_m \approx 1/3500$ male births) the method gives $\mu \approx 1 \times 10^{-4}$, one of the highest known, explained by the 2.2 Mb size of the *DMD* gene; and the "one third of cases are new mutations" rule is used in **genetic counseling** of mothers of isolated cases ([7.4.7](/7.4.7)). Direct sequencing of parent–offspring trios has confirmed rates of this order and shown that most new **point mutations** arise in the father ([7.4.12](/7.4.12)).

### 23.4.3. Genetic Load

**Definition 23.4.1 (Genetic Load)** The **genetic load** of a population is the proportional reduction of its mean fitness below that of the fittest genotype, $L = (w_{\max} - \bar w)/w_{\max}$. The part due to recurrent deleterious mutation is the mutation load; the part due to the segregation of less fit homozygotes under heterozygote advantage is the segregational load (§23.3.2).

**Theorem 23.4.2 (Haldane–Muller Principle)** At mutation–selection balance, the mutation load at a locus is $L \approx \mu$ for a recessive deleterious allele and $L \approx 2\mu$ for a partially dominant one, independent of the selection coefficient.

**Proof** Recessive: $L = s\hat q^2 = s \cdot \mu/s = \mu$. Partially dominant: $L \approx 2\hat q\,hs = 2hs \cdot \mu/(hs) = 2\mu$ (each heterozygote carries one allele and loses $hs$). $\square$

The principle says that a mildly deleterious mutation costs a population as much as a lethal one: it is less harmful per carrier but persists longer and so affects more individuals. Summed over the genome, with $U$ new deleterious mutations per diploid genome per generation, mean fitness is reduced to about $\mathrm{e}^{-U}$; for humans $U$ is of order 1 or more, which is one of the arguments that most of the genome is not under strong selective constraint.

## 23.5. Genetic Drift

### 23.5.1. The Wright–Fisher Model

In a finite population, which allele a heterozygous parent transmits to a particular child, and which individuals happen to reproduce, are matters of chance; allele frequencies therefore fluctuate even without selection.

**Definition 23.5.1 (Genetic Drift and the Wright–Fisher Model)** **Genetic drift** is the random change of allele frequencies from generation to generation caused by the sampling of gametes in a finite population. Its standard model, the **Wright–Fisher model**, describes a population of $N$ diploid individuals ($2N$ gene copies) with non-overlapping generations: each generation is formed by drawing $2N$ gene copies at random, with replacement, from the **gene pool** of the previous one. The number of copies of $A$ in generation $t + 1$, given frequency $p_t$, is binomial:

$$
2Np_{t+1} \sim \mathrm{Bin}(2N, p_t). \tag{23.11}
$$

The sequence $p_t$ is a **Markov chain** on $\{0, \tfrac{1}{2N}, \dots, 1\}$ ([3.5.9](/3.5.9)) with absorbing states 0 (loss) and 1 (fixation). (The same model, with mitochondrial genomes in place of individuals, described heteroplasmic segregation in [7.4.11](/7.4.11).)

**Theorem 23.5.1 (Properties of Drift)** In the Wright–Fisher model without mutation or selection:

1. $\mathbb{E}[p_{t+1} \mid p_t] = p_t$ and $\operatorname{Var}(p_{t+1} \mid p_t) = p_tq_t/2N$;
2. the expected **heterozygosity** $H_t = \mathbb{E}[2p_tq_t]$ decays as $H_t = H_0(1 - \tfrac{1}{2N})^t \approx H_0\,\mathrm{e}^{-t/2N}$;
3. an allele with initial frequency $p_0$ is eventually fixed with probability $p_0$ and lost with probability $1 - p_0$; a new mutation ($p_0 = 1/2N$) is fixed with probability $1/2N$.

**Proof** (1) is the mean and **variance** of $\mathrm{Bin}(2N, p_t)$ divided by $2N$. (2) For two gene copies drawn from generation $t + 1$ (without replacement), the probability that they are copies of the same parental copy is $1/2N$, in which case they are identical by descent; otherwise they derive from two distinct parental copies, which are IBD with probability $F_t$. Hence $1 - F_{t+1} = (1 - \tfrac{1}{2N})(1 - F_t)$, the last row of Formula 22.4.2, and $H_t = H_0(1 - F_t)$. (3) By (1), $p_t$ is a martingale, so $\mathbb{E}[p_t] = p_0$ for all $t$; absorption is certain, so $\mathbb{E}[p_\infty] = 1 \cdot u + 0 \cdot (1 - u) = p_0$ gives the fixation probability $u = p_0$. $\square$

In words: drift has no direction, but it has a rate, $1/2N$ per generation, at which genetic variation is lost in every population and which differs between populations, so that isolated populations diverge. In the extreme, a population of $N = 1$ (a self-fertilizing heterozygote) is fixed for $A$ in the next generation with probability $(1/2)^2 = 1/4$, a population of $N = 2$ with probability $(1/2)^4 = 1/16$; in general, fixation in one generation has probability $p^{2N}$, negligible for any real population. Other consequences of the model, which follow from its diffusion approximation (Kimura 1955; the Kolmogorov forward equation, a partial differential equation of the type in [2.5](/2.5)):

- a new neutral mutation that is eventually fixed takes on average about $4N$ generations to do so; one that is lost disappears on average within about $2\ln(2N)$ generations;
- the time to fixation or loss starting from $p_0$ is $\bar t(p_0) \approx -4N[p_0\ln p_0 + q_0\ln q_0]$, about $2.8N$ generations for $p_0 = 1/2$.

![Genetic drift in the Wright–Fisher model (Definition 23.5.1). A–C: 20 replicate populations each of N = 10, 100 and 1000 diploids, all starting from p = 0.5 (orange: fixed; blue: lost; grey: still segregating after 200 generations). Small populations fix or lose the allele within tens of generations; large ones barely change. D: mean heterozygosity over 2000 replicate populations (dots) and the prediction H_t = H_0(1 − 1/2N)^t of Theorem 23.5.1 (lines)](./plots/drift.py)

### 23.5.2. Effective Population Size

Real populations differ from the Wright–Fisher ideal: the sexes are unequal in number, population size fluctuates, and some individuals leave many more offspring than others. Each of these increases drift.

**Definition 23.5.2 (Effective Population Size)** The **effective population size** $N_e$ of a population is the size of an ideal Wright–Fisher population that would lose heterozygosity (or show variance of allele-frequency change) at the same rate, so that $H_t = H_0(1 - 1/2N_e)^t$.

**Formula 23.5.1 (Effective Population Size)**

| Departure from the ideal | $N_e$ |
|---|---|
| $N_m$ breeding males, $N_f$ breeding females | $\dfrac{4N_mN_f}{N_m + N_f}$ |
| sizes $N_1, \dots, N_t$ over $t$ generations | harmonic mean $\left(\dfrac1t\sum_i \dfrac{1}{N_i}\right)^{-1}$ |
| variance $V_k$ of the number of gametes contributed per individual (mean 2), constant $N$ | $\dfrac{4N - 2}{V_k + 2}$ |

The first follows because each gene copy comes with probability $1/2$ from a father and $1/2$ from a mother, so two copies share a parental copy with probability $\tfrac14\cdot\tfrac{1}{2N_m} + \tfrac14\cdot\tfrac{1}{2N_f}$ times 2 (same sex) $= \tfrac18(1/N_m + 1/N_f) = 1/(2N_e)$; the second because the heterozygosity retained is $\prod(1 - 1/2N_i) \approx \exp(-\sum 1/2N_i)$; the third is Wright's, and gives $N_e = N$ for Poisson offspring numbers ($V_k = 2$) and up to $2N$ when every individual contributes exactly two gametes.

**Example 23.5.1** A herd of 10 breeding males and 100 females has $N_e = 4 \cdot 10 \cdot 100/110 = 36$, not 110; with 10 males and 40 females, $N_e = 32$. A population of 1000 that passes through a bottleneck of 10 individuals for one generation and recovers has, over four generations of sizes 1000, 10, 1000, 1000, $N_e = 4/(3/1000 + 1/10) = 39$: the harmonic mean is dominated by the smallest size.

Effective sizes are usually much smaller than census sizes. The human $N_e$ estimated from genetic diversity is about $10^4$ (§23.7), reflecting the small ancestral populations of the last several hundred thousand years rather than the present 8 billion; for domestic cattle breeds, where a few bulls sire most offspring by artificial insemination, $N_e$ is often below 100.

### 23.5.3. Founder Effects and Bottlenecks

**Definition 23.5.3 (Founder Effect and Population Bottleneck)** A **founder effect** is the change in allele frequencies, and the loss of variation, in a new population established by a small number of individuals from a larger one. A **population bottleneck** is a drastic temporary reduction of population size (by disease, climate or human action), after which the survivors are in effect the founders of the recovered population.

Both are episodes of intense drift. The founders carry only a sample of the alleles of the source population, and an allele that was rare there may by chance be common among them. Human populations derived from few founders and later isolated by geography or culture show characteristic disease spectra:

- the Old Order Amish of Lancaster County, Pennsylvania, founded by a few hundred immigrants in the eighteenth century, have a high frequency of Ellis–van Creveld syndrome (a recessive form of dwarfism with polydactyly), traced to a single founder couple;
- the Finnish population carries about 36 recessive diseases (the "Finnish disease heritage") that are rare elsewhere, while some diseases common elsewhere (such as **phenylketonuria** and cystic fibrosis) are rare in Finland;
- Ashkenazi Jewish, French Canadian (Saguenay–Lac-Saint-Jean), Afrikaner and many island populations show similar founder mutations, whose shared ancestral haplotypes ([7.4.22](/7.4.22), §22.3.2) make them easy to map and allow targeted carrier screening.

Bottlenecks reduce heterozygosity by the factor $(1 - 1/2N_b)$ per generation spent at size $N_b$, and they reduce the number of alleles even more, because rare alleles are lost first. Northern elephant seals, hunted to perhaps 20–30 individuals in the 1890s and now over 100 000, have very low genetic diversity; cheetahs show the signature of ancient bottlenecks.

### 23.5.4. Drift and Migration

Drift differentiates subpopulations and migration homogenizes them. In Wright's island model with $n$ subpopulations of size $N$ exchanging migrants at rate $m$, the equilibrium **fixation index** ([7.4.22](/7.4.22), Eq. (22.11)) is

$$
F_{\mathrm{ST}} \approx \frac{1}{1 + 4Nm}. \tag{23.12}
$$

The product $Nm$ is the number of migrants per generation, and Eq. (23.12) shows that it alone matters: about one migrant per generation ($Nm = 1$, $F_{\mathrm{ST}} = 0.2$) is enough to prevent subpopulations from becoming fixed for different neutral alleles, whatever their size. Conversely, the observed human $F_{\mathrm{ST}}$ of about $0.1$ corresponds to $Nm \approx 2$ if interpreted at equilibrium (it is better understood historically, as the result of expansion out of Africa with serial founder events).

## 23.6. Drift and Selection Together

Selection is deterministic in an infinite population, but every new mutation starts as a single copy, and at low copy number drift dominates even for favorable alleles.

**Theorem 23.6.1 (Kimura's Fixation Probability)** In a diploid population of size $N$ and effective size $N_e$, an allele with additive selection coefficient $s$ (fitnesses $1 + s$, $1 + s/2$, $1$ in Kimura's form; equivalently genic selection) and initial frequency $p$ is fixed with probability

$$
u(p) = \frac{1 - \mathrm{e}^{-4N_esp}}{1 - \mathrm{e}^{-4N_es}}. \tag{23.13}
$$

For a new mutation ($p = 1/2N$) with $N_e = N$: $u \approx 1/2N$ when $|4Ns| \ll 1$; $u \approx 2s$ when $4Ns \gg 1$ (Haldane 1927); and $u \approx 4|s|\mathrm{e}^{-4N|s|}$ for a deleterious allele with $4N|s| \gg 1$.

The formula is derived from the diffusion approximation of the Wright–Fisher model (Kimura 1962); we use it without proof. The limits follow by expansion: for small $4N_es$ both numerator and denominator are linear and $u \to p$; for a new mutation with $4Ns \gg 1$ the denominator is about 1 and the numerator $1 - \mathrm{e}^{-2s} \approx 2s$.

**Example 23.6.1** A new mutation with $s = 0.01$ in a population of $N = N_e = 1000$ ($4Ns = 40$) is fixed with probability $u = 0.0198 \approx 2s$: about 98 of every 100 such favorable mutations are lost by chance in the first few generations, while they are present in a handful of copies. Once an allele has reached a few times $1/(Ns)$ copies, its fate is effectively decided and it increases deterministically. A neutral mutation is fixed with probability $1/2000 = 0.0005$, so the favorable one is 40 times more likely to be fixed. A slightly deleterious mutation with $s = -0.001$ ($4Ns = -4$) is fixed with probability $3.7 \times 10^{-5}$, still 7.5 % of the neutral value.

The scaled selection coefficient $N_es$ is the measure that matters: selection is effective when $|N_es| \gg 1$ and the allele behaves as effectively neutral when $|4N_es| \lesssim 1$. The same mutation can thus be selected in a large population and drift freely in a small one, which is the basis of the nearly neutral theory (§23.7) and of the accumulation of mildly deleterious mutations in small populations.

![Fixation probability of a new mutation (p = 1/2N) relative to the neutral value, 2N u, against the scaled selection coefficient Ns. Lines: Kimura's formula, Eq. (23.13), for N = 100 and 1000, which nearly coincide in these scaled units; dots: 20 000 simulated Wright–Fisher populations of N = 100 for each s, with 95 % intervals; dashed: Haldane's approximation u = 2s. In the nearly neutral zone |4Ns| < 1 (shaded) drift dominates; favorable mutations with 4Ns ≫ 1 are fixed with probability only about 2s, and deleterious ones almost never](./plots/fixation.py)

## 23.7. The Neutral Theory and the Molecular Clock

When amino acid sequences of **proteins** from different species and protein polymorphisms within species became available in the 1960s, they revealed far more variation and a far more regular rate of change than selection-based theories had expected.

**Definition 23.7.1 (Neutral Theory and Molecular Clock)** The **neutral theory of molecular evolution** (Kimura 1968; King and Jukes 1969) holds that most evolutionary changes at the molecular level, and most polymorphisms within species, are caused by the random drift of selectively neutral or nearly neutral mutations, rather than by positive selection; selection acts mainly to remove deleterious mutations. The **molecular clock** is the approximate constancy of the rate of molecular evolution (substitutions per site per year) of a given gene across lineages, which allows divergence times to be estimated from sequence differences.

**Theorem 23.7.1 (Rate of Neutral Substitution)** If neutral mutations arise at rate $\mu$ per gene copy per generation, the rate of substitution (fixation of new mutations) in the population is

$$
k = 2N\mu \cdot \frac{1}{2N} = \mu, \tag{23.14}
$$

independent of the population size. Two lineages that separated $t$ generations ago differ at about $2\mu t$ sites per site (each lineage accumulates $\mu t$), ignoring ancestral polymorphism and multiple hits.

**Proof** Each generation $2N\mu$ new neutral mutations enter the population, and by Theorem 23.5.1(3) each is eventually fixed with probability $1/2N$; their product is the long-run number of fixations per generation. $\square$

This is the remarkable feature that explains the clock: population size cancels, so that the rate depends only on the neutral mutation rate, which in turn depends on functional constraint. Functionally unconstrained sequences (**pseudogenes**, synonymous sites, introns) evolve fastest, at close to the mutation rate; strongly constrained proteins (**histones**) evolve slowest, because most of their mutations are deleterious and are removed. The clock ticks per generation, not per year, and the rate also differs with the mutation rate of lineages, so it is only approximately constant; calibrating and testing it are topics of 7.10.

**Formula 23.7.1 (Neutral Diversity)** At equilibrium between mutation and drift, with $N_e$ the effective size and $\mu$ the neutral mutation rate,

$$
\theta = 4N_e\mu, \qquad H = \frac{\theta}{1 + \theta} \quad \text{(infinite-alleles model)}, \qquad \pi \approx \theta \quad \text{(per site)}, \tag{23.15}
$$

where $H$ is the expected heterozygosity of a locus at which every mutation creates a new allele and $\pi$ the expected number of differences per site between two sequences (for $\theta \ll 1$). The derivation, which follows the genealogy of two gene copies back to their common ancestor, belongs to coalescent theory (7.10).

**Example 23.7.1** Two human genomes differ at about 1 site in 1000 ($\pi \approx 0.001$), and the mutation rate is about $1.2 \times 10^{-8}$ per site per generation. Then $N_e \approx \pi/(4\mu) = 0.001/(4.8 \times 10^{-8}) \approx 21\,000$: humans are genetically a small species, less diverse than chimpanzees, whose populations were larger, and this "long-term" $N_e$ is the harmonic mean over the ancestral history of the species (§23.5.2).

Not all molecular evolution is neutral: adaptive substitutions are detected by an excess of amino acid–changing over silent changes, and selective sweeps by reduced diversity and long haplotypes. Ohta's nearly neutral theory (1973) refines the neutral theory: many mutations are slightly deleterious, with $|N_es|$ near 1, so whether they behave as neutral depends on $N_e$. The neutral theory remains the **null hypothesis** against which selection is tested (7.10).

New genes and new functions arise mainly by duplication of existing genes and genomes ([7.4.14](/7.4.14) for gene families and the fates of duplicates, [7.4.16](/7.4.16) for **polyploidy**), by **transposition** and retrotransposition ([7.4.17](/7.4.17)), and occasionally de novo from noncoding sequence. A duplicate copy is initially redundant, so its mutations are nearly neutral: it usually decays into a pseudogene, but may acquire a new function or split the functions of the ancestral gene with its partner.

## 23.8. Human Genetic Ancestry and Selection in Action

### 23.8.1. Genealogical and Genetic Ancestors

The frequencies of variants in present-day populations, and the haplotypes on which they lie, are molecular records of population history. Two notions of ancestry must be separated. Your genealogical ancestors are your parents, grandparents and so on: $2^t$ positions $t$ generations back, a number that exceeds the population size after about 30 generations, so that ancestors appear many times in a **pedigree** and everyone alive more than a few thousand years ago is either an ancestor of all present-day humans or of none. Your genetic ancestors are those from whom you actually inherited segments of DNA; because recombination cuts the genome into about 30–40 new pieces per generation, beyond about 10 generations most genealogical ancestors contribute no DNA at all.

**Definition 23.8.1 (Most Recent Common Ancestor)** The **most recent common ancestor** (MRCA) of a set of gene copies (a DNA segment in two or more individuals) is the most recent ancestral copy, in some past generation, from which all of them descend through unbroken lines of replication and transmission.

Each segment of the genome has its own MRCA and its own genealogy. The mitochondrial genome (inherited from mothers only, [7.4.11](/7.4.11)) and the non-recombining part of the Y chromosome (from fathers only) are each inherited as a single block, so their genealogies are single trees, and mutations accumulated along the branches reveal them: the longer the branch separating two people's copies, the more differences between them. The MRCA of human mtDNA ("mitochondrial Eve") lived about 150 000–200 000 years ago and that of the Y chromosome at a similar or somewhat earlier time; they were not contemporaries and not the only ancestors of their time, merely the ancestors at two loci, and other loci have MRCAs up to a few million years old. The deepest branches of most genealogies are in Africa, and the diversity of non-African populations is a subset of African diversity, the genetic signature of the expansion of modern humans out of Africa about 50 000–70 000 years ago, followed by serial founder effects that reduced heterozygosity with distance from Africa. Sequences of ancient DNA ([7.4.14](/7.4.14)) showed that non-Africans carry about $1$–$2\,\%$ of DNA from Neanderthals, and people of Oceania several percent from Denisovans, from interbreeding after the expansion.

### 23.8.2. Natural Selection in Human Populations

Darwin's theory rests on three principles that **population genetics** makes quantitative: variation (individuals differ), heredity (offspring resemble their parents more than unrelated individuals) and selection (some variants survive and reproduce better than others in a given environment). The sickle-cell polymorphism (Example 23.3.3) is a case of balancing selection; lactase persistence is the best-documented case of recent positive selection.

**Example 23.8.1 (Lactase Persistence)** In most mammals, and most humans, expression of lactase (*LCT*) declines after weaning. In some populations most adults continue to digest lactose. In Europeans this trait is caused by an allele $-13910\,\mathrm{T}$ in an **enhancer** within an intron of the neighboring gene *MCM6*, dominant at the phenotypic level; different alleles in the same enhancer arose independently in pastoralist populations of East Africa and the Middle East (convergent evolution). The European allele lies on a haplotype that extends over more than 1 Mb with little recombinational decay, which by the logic of §22.3.2 implies that it rose to high frequency within the last several thousand years; ancient DNA shows it was rare in Europe until about 3000–4000 years ago, long after the start of dairying. Selection coefficients of about $0.01$–$0.1$ have been estimated. A rough check with Formula 23.3.2: an allele with $s = 0.05$ starting as a single copy in a population of $N = 10^4$ ($p_0 = 5 \times 10^{-5}$) reaches $p = 0.75$ in $\ln[3 \cdot (1 - p_0)/p_0]/\ln 1.05 = 225$ generations, about 6000 years: strong selection, acting over a historically short time, is required.

## Summary

| Force | Recursion | Equilibrium / time scale |
|---|---|---|
| mutation $A \rightleftarrows a$ | $\Delta p = -\mu p + \nu q$, Eq. (23.1) | $\hat q = \mu/(\mu + \nu)$; time $\sim 1/(\mu + \nu)$ (Formula 23.1.1) |
| migration (island) | $p' = (1 - m)p + mP$ | $p \to P$; $(1 - m)^t$ (Formula 23.2.1); admixture $m = (p_{\mathrm{h}} - p_2)/(p_1 - p_2)$ |
| selection | $p' = (p^2w_{11} + pqw_{12})/\bar w$; $\Delta p = \tfrac{pq}{2\bar w}\,\mathrm{d}\bar w/\mathrm{d}p$ (Theorem 23.3.1) | rare recessive $\Delta q \approx -sq^2$, otherwise $\approx -hsq$ (Formula 23.3.1) |
| drift | $2Np' \sim \mathrm{Bin}(2N, p)$ (Definition 23.5.1) | $\operatorname{Var}(\Delta p) = pq/2N$; $H_t = H_0(1 - 1/2N)^t$; fixation $p_0$ (Theorem 23.5.1) |

- Times under selection: genic $t \approx \tfrac1s\ln(p_tq_0/p_0q_t)$ (Formula 23.3.2); recessive lethal $t = 1/q_t - 1/q_0$ (Formula 23.3.3), so selection against rare recessives is slow.
- Directional selection in nature: industrial melanism of *Biston betularia*, $s \approx 0.25$ against *typica* during the rise and $0.1$–$0.2$ against *carbonaria* during the decline (Example 23.3.4).
- Balancing selection: heterozygote advantage gives the stable $\hat q = s_1/(s_1 + s_2)$ (Theorem 23.3.2; HbS: $0.12/0.98 = 0.122$); underdominance an unstable equilibrium; negative frequency dependence maintains many alleles.
- Mutation–selection balance: $\hat q = \sqrt{\mu/s}$ (recessive), $\mu/(hs)$ (partially dominant) (Theorem 23.4.1); Haldane's $\mu = \tfrac12(1 - f)I$, one third of X-linked lethal cases are new mutations (Formula 23.4.1); load $\mu$ or $2\mu$, independent of $s$ (Theorem 23.4.2).
- Effective size: sex ratio $4N_mN_f/(N_m + N_f)$, harmonic mean of sizes, $(4N - 2)/(V_k + 2)$ (Formula 23.5.1); founder effects and bottlenecks; drift–migration $F_{\mathrm{ST}} \approx 1/(1 + 4Nm)$, Eq. (23.12).
- Drift with selection: $u(p) = (1 - \mathrm{e}^{-4N_esp})/(1 - \mathrm{e}^{-4N_es})$; a new favorable mutation fixes with $u \approx 2s$; $|4N_es| \lesssim 1$ is effectively neutral (Theorem 23.6.1).
- Neutral theory: substitution rate $k = \mu$, independent of $N$ (Theorem 23.7.1), hence the **molecular clock**; diversity $\theta = 4N_e\mu$ (Formula 23.7.1); human $N_e \approx 2 \times 10^4$.
- History: genealogical vs genetic ancestors, MRCA of each locus, out-of-Africa expansion and archaic admixture; lactase persistence as recent strong positive selection.

## Questions

1. A gene mutates from $A$ to $a$ at rate $\mu = 2 \times 10^{-6}$ and back at $\nu = 5 \times 10^{-7}$ per generation. (a) What is the equilibrium frequency of $a$? (b) Starting from $q = 0$, how many generations are needed to reach half of it?

   **Answer** (a) $\hat q = 2 \times 10^{-6}/2.5 \times 10^{-6} = 0.8$. (b) $q_t = \hat q[1 - (1 - \mu - \nu)^t]$; half is reached at $t = \ln 2/(\mu + \nu) = 0.693/2.5 \times 10^{-6} \approx 277\,000$ generations.

2. An island population has $q = 0.6$ for an allele whose frequency on the mainland is $0.2$; each generation $5\,\%$ of the island's breeders are mainland immigrants. What is $q$ after 10 and after 30 generations?

   **Answer** $q_t = 0.2 + 0.4 \cdot 0.95^t$: $t = 10$: $0.2 + 0.4 \cdot 0.599 = 0.440$; $t = 30$: $0.2 + 0.4 \cdot 0.215 = 0.286$.

3. A hybrid population has allele frequency $0.30$ at a marker whose frequencies in the two parental populations are $0.10$ and $0.90$. Estimate the admixture proportion. Why are many loci needed in practice?

   **Answer** $m = (0.30 - 0.10)/(0.90 - 0.10) = 0.25$ from the population with frequency $0.90$. Each locus gives a noisy estimate (sampling error, drift and selection since admixture change single-locus frequencies), and loci with small parental differences give unstable ratios; averaging over many loci with large differences, or using local ancestry along chromosomes, gives reliable estimates.

4. The fitnesses of $AA$, $Aa$ and $aa$ are $1$, $0.9$ and $0.6$, and $p = 0.4$. Compute $\bar w$, $p'$ and $\Delta p$.

   **Answer** $\bar w = 0.16 \cdot 1 + 0.48 \cdot 0.9 + 0.36 \cdot 0.6 = 0.16 + 0.432 + 0.216 = 0.808$. $p' = (0.16 + 0.24 \cdot 0.9)/0.808 = 0.376/0.808 = 0.4653$; $\Delta p = 0.0653$. Check with Eq. (23.5): $0.24[0.4 \cdot 0.1 + 0.6 \cdot 0.3]/0.808 = 0.24 \cdot 0.22/0.808 = 0.0653$.

5. A recessive lethal allele has frequency $0.02$. (a) How many generations of complete selection are needed to reduce it to $0.01$? To $0.001$? (b) If it is recessive with $s = 0.2$ instead, approximately what is $\Delta q$ at $q = 0.1$?

   **Answer** (a) $1/0.01 - 1/0.02 = 50$ generations; $1/0.001 - 1/0.02 = 950$. (b) $\Delta q = -spq^2/(1 - sq^2) = -0.2 \cdot 0.9 \cdot 0.01/(1 - 0.002) = -0.0018$.

6. An allele increases fitness multiplicatively by $s = 0.02$ per copy. How many generations does it take to go from $p = 0.001$ to $p = 0.5$, and from $0.5$ to $0.999$?

   **Answer** By Eq. (23.6) with $\ln 1.02 = 0.0198$: $\ln(0.5 \cdot 0.999/(0.001 \cdot 0.5))/0.0198 = \ln 999/0.0198 = 6.907/0.0198 = 349$ generations, and by symmetry the same 349 from $0.5$ to $0.999$.

7. In a malarial region the fitnesses of $AA$, $AS$ and $SS$ are estimated as $0.85$, $1$ and $0.2$. (a) What is the equilibrium frequency of $S$? (b) What is the segregational load? (c) If malaria is eradicated and $AA$ and $AS$ become equally fit, how many generations would it take for $q$ to fall to half of its equilibrium value, assuming $SS$ fitness $0.2$?

   **Answer** (a) $s_1 = 0.15$, $s_2 = 0.8$: $\hat q = 0.15/0.95 = 0.158$. (b) $L = s_1s_2/(s_1 + s_2) = 0.12/0.95 = 0.126$. (c) Selection against a recessive with $s = 0.8$: iterating $q' = q(1 - sq)/(1 - sq^2)$ from $0.158$ to $0.079$ takes 9 generations (the approximation $\Delta(1/q) \approx s$ for rare recessives gives $(1/0.079 - 1/0.158)/0.8 = 7.9$), a few centuries.

8. A recessive lethal disease occurs in 1 in 40 000 births in a large randomly mating population at mutation–selection equilibrium. (a) Estimate the mutation rate. (b) What carrier frequency is expected? (c) If heterozygotes had a $1\,\%$ fitness disadvantage, how would the equilibrium frequency compare?

   **Answer** (a) $q^2 = \mu$, so $\mu = 2.5 \times 10^{-5}$ and $q = 0.005$. (b) $2pq \approx 0.01$. (c) $\hat q \approx \mu/(hs) = 2.5 \times 10^{-5}/0.01 = 0.0025$, half as large; the affected frequency would fall to $6 \times 10^{-6}$.

9. An autosomal dominant disorder has a birth incidence of 1 in 25 000; affected individuals have on average $20\,\%$ of the number of children of their unaffected sibs. Estimate the mutation rate. What fraction of affected children are expected to have an unaffected parent?

   **Answer** $\mu = \tfrac12(1 - 0.2)/25\,000 = 1.6 \times 10^{-5}$. New mutations account for $2\mu$ of births in $I = 4 \times 10^{-5}$, that is $2\mu/I = 1 - f = 0.8$: about $80\,\%$ of cases are sporadic, with unaffected parents (assuming full **penetrance**).

10. In a Wright–Fisher population of $N = 50$, (a) what fraction of the initial heterozygosity remains after 100 generations? (b) What is the probability that a neutral allele now at frequency $0.2$ is eventually fixed? (c) What is the variance of the allele frequency in the next generation if $p = 0.2$?

    **Answer** (a) $(1 - 1/100)^{100} = 0.366$. (b) $0.2$. (c) $pq/2N = 0.16/100 = 0.0016$ (**standard deviation** $0.04$).

11. Compute the effective population size of (a) a captive population of 4 males and 36 females; (b) a population that over five generations had sizes 500, 50, 500, 500, 500; (c) a population of 100 in which the number of gametes contributed per individual has variance 6.

    **Answer** (a) $4 \cdot 4 \cdot 36/40 = 14.4$. (b) $5/(4/500 + 1/50) = 5/0.028 = 179$. (c) $(400 - 2)/(6 + 2) = 49.75$, half the census size.

12. A new mutation with $s = 0.002$ (additive) arises in a population with $N = N_e = 500$. Compute its fixation probability by Kimura's formula and compare with $1/2N$ and $2s$. Would it behave as effectively neutral if $N_e$ were 50?

    **Answer** $4N_es = 4$, $p = 0.001$: $u = (1 - \mathrm{e}^{-0.004})/(1 - \mathrm{e}^{-4}) = 0.003992/0.9817 = 0.00407$, about 4 times the neutral $0.001$ and close to $2s = 0.004$. With $N_e = 50$, $4N_es = 0.4 < 1$: drift dominates and its fixation probability (for $p = 1/100$) is $u = (1 - \mathrm{e}^{-0.004})/(1 - \mathrm{e}^{-0.4}) = 0.0121$, only $1.2$ times the neutral value $0.01$.

13. Why is the rate of neutral substitution independent of population size, whereas the rate of substitution of favorable mutations ($4Ns \gg 1$) is about $4N\mu_bs$, where $\mu_b$ is the rate of favorable mutations?

    **Answer** In both cases the rate is (number of new mutations per generation) × (fixation probability). For neutral mutations this is $2N\mu \cdot 1/2N = \mu$: a larger population produces more mutations but each has a proportionally smaller chance of fixation. For favorable mutations the fixation probability is about $2s$, independent of $N$, so the rate is $2N\mu_b \cdot 2s = 4N\mu_bs$ and grows with population size.

14. Two species differ at $2\,\%$ of the sites of a pseudogene that evolves at a neutral rate of $2.5 \times 10^{-9}$ substitutions per site per year in each lineage. Estimate their divergence time. Name two reasons why the estimate may be biased.

    **Answer** $d = 2\mu t$, $t = 0.02/(2 \cdot 2.5 \times 10^{-9}) = 4 \times 10^6$ years. Biases: (i) ancestral polymorphism: the gene copies diverged before the species split, so the time estimated is the gene divergence, older than the speciation; (ii) multiple substitutions at the same site (saturation) make $d$ underestimate the number of changes for large divergences; (iii) the rate per year differs between lineages with different generation times or mutation rates; (iv) calibration error.

15. (Open question.) A population of 5000 has a deleterious recessive allele at frequency $0.01$. It is split into 50 isolated populations of 100. Describe what happens to (a) the frequency of affected individuals in the short term, (b) the allele frequency in each subpopulation in the long term, (c) the mean fitness of the subpopulations.

    **Answer** (a) Initially, nothing changes; then drift raises homozygosity within subpopulations at rate $1/2N = 0.005$ per generation ($F_t \approx t/200$ at first), so affected individuals increase from $q^2 = 10^{-4}$ toward $q^2 + Fpq$, an increase of about $0.0005$ per $10\,\%$ of $F$ (inbreeding within small populations). (b) In each subpopulation $q$ drifts: by Theorem 23.5.1 the allele is eventually lost in most subpopulations and fixed in about $1\,\%$ of them if neutral; selection against homozygotes ($s$ relative to $1/2N$) makes loss more likely and purges the allele when it becomes common (purging). (c) Mean fitness falls at first (**inbreeding depression**), then may partly recover by purging; subpopulations in which the allele drifts to fixation suffer a permanent load, the main reason why conservation genetics tries to keep $N_e$ above a few hundred and to maintain some gene flow ($Nm \geq 1$).

16. In an industrial area, the frequency of melanic peppered moths (dominant) rose from $36\,\%$ to $51\,\%$ in one generation. Assuming Hardy–Weinberg proportions among zygotes and selection only against the light recessive phenotype, estimate the selection coefficient against *typica*.

    **Answer** Light moths: $q_0^2 = 0.64$, $q_0 = 0.8$; $q_1^2 = 0.49$, $q_1 = 0.7$. From Formula 23.3.1, $q_1 = q_0(1 - sq_0)/(1 - sq_0^2)$: $0.7(1 - 0.64s) = 0.8(1 - 0.8s)$, so $0.192s = 0.1$ and $s = 0.52$. Such a large value from a single generation is imprecise (sampling error of both frequencies, migration between areas), which is why rates are estimated over many years (Example 23.3.4).

17. With $s = 1/3$ against the light recessive phenotype, the melanic allele has frequency $0.1$. (a) What are the melanic phenotype frequencies in this and the next generation? (b) About how many generations does it take until $90\,\%$ of the moths are melanic? (c) Why would the same selection take much longer to remove the last few percent of light moths?

    **Answer** (a) Melanics $1 - 0.9^2 = 0.19$. Next generation: $q' = q(1 - sq)/(1 - sq^2) = 0.9 \cdot 0.7/0.73 = 0.863$, $p' = 0.137$; melanics $1 - 0.863^2 = 0.255$. (b) Iterating, 13 generations. (c) When $q$ is small, $\Delta q \approx -sq^2$ (Formula 23.3.1): the light allele survives mostly in melanic heterozygotes, which selection does not see, so its decline becomes very slow, as for the recessive lethal of Formula 23.3.3.
