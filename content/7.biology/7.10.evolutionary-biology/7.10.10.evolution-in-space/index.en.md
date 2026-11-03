---
title: Evolution in Space
description: "Geographic variation and its causes. Clines, mosaics and common-garden tests; gene flow, dispersal and their direct and indirect measurement (migration rate, dispersal variance, F_ST); island, stepping-stone and isolation-by-distance models; Q_ST versus F_ST; migration–selection balance, gene swamping and the critical migration rate; clines in step environments and their width; tension zones; the Fisher–KPP wave of advance of favourable alleles; drift, gene flow and local adaptation; the evolution of dispersal (disturbance, kin competition, inbreeding avoidance, spatial sorting); and the evolution of species' ranges."
---

Almost every species varies geographically. White clover (*Trifolium repens*) protects itself against herbivores with cyanide, released from its leaves when the cells are damaged, yet in cold climates the genes needed to make cyanide have been deleted from most plants; one hypothesis is that freezing ruptures the cells and poisons cyanogenic plants, so that cyanide production is beneficial in warm regions and harmful in cold ones. Geographic patterns like this are the product of selection that varies in space, of **genetic drift** in local populations, and of gene flow, which mixes them. This chapter treats the interplay of these forces. It builds on the island model and $F_{\mathrm{ST}}$ of population genetics ([7.4.22](/7.4.22), [7.4.23](/7.4.23)), whose estimation from genomic data is described in [7.8.13](/7.8.13); the diffusion of genes through space is the heat equation of [2.5.7](/2.5.7), and the spread of favourable alleles is a traveling wave of the Fisher–KPP equation. The interaction of gene flow and divergence is also the central problem of speciation ([7.10.11](/7.10.11), [7.10.12](/7.10.12)), and the large-scale distribution of species is the subject of biogeography ([7.10.30](/7.10.30)).

## 10.1. Patterns in Space

**Definition 10.1.1 (Cline)** A **cline** is a gradual change in space of an allele frequency or of the mean of a trait.

The cyanide polymorphism of white clover forms a cline: the frequency of plants with the deletion of the gene *CYP79D15* rises towards colder climates, following January temperatures. Some clines extend over thousands of kilometres. Moose (*Alces alces*) are much heavier in northern than in southern Sweden; such latitudinal clines of body size are so common in birds and mammals that they have a name, Bergmann's rule, explained by the lower surface-to-volume ratio of large bodies, which lose heat less quickly in cold climates. Other clines are very short. The grass *Agrostis capillaris* growing on an abandoned copper mine in Wales, an area of about $100\,\mathrm{m} \times 300\,\mathrm{m}$ with soil lethal to most plants, has evolved copper tolerance, and tolerance declines over a few dozen metres along transects into the surrounding pasture. These are examples of **local adaptation** ([7.10.8](/7.10.8)). Where the environment is a patchwork rather than a gradient, local adaptation produces a mosaic instead of a smooth cline.

Geographic variation in phenotype need not be genetic. A classic study of yarrow (*Achillea millefolium*) by Clausen, Keck and Hiesey sampled seeds along a transect from the Californian coast to the high Sierra Nevada, where plants are much shorter than at low elevation, and grew them in a common garden near sea level. Plants from high-elevation seed remained shorter, but the differences were smaller than in nature: both genetic divergence and **phenotypic plasticity** ([7.10.9](/7.10.9)) contribute. Short plants can flower before the early winter at high elevation, whereas tall plants attract more pollinators at low elevation, so the genetic part is probably adaptive.

Clines need not be adaptive at all. Where populations that diverged in isolation meet again, as many species did when they expanded from glacial refugia after the last glaciation, which ended about $11\,700$ years ago, the mixing of their genes produces clines at all loci that differ between them, in the same place. In the eelpout *Zoarces viviparus*, found in both the North Sea and the Baltic, several enzyme loci show parallel clines through the straits that connect the two seas; such concordance of many clines is evidence of a historical contact rather than of selection at each locus. Geographic variation within a species is traditionally described by naming subspecies: geographically defined populations that differ consistently in some traits but interbreed where they meet. A species divided into several subspecies is called polytypic.

## 10.2. Gene Flow and Dispersal

**Gene flow** ([Definition 23.2.1 in 7.4.23](/7.4.23#def-23.2.1)) has two effects: it makes populations more similar, opposing divergence by selection or drift, and it introduces into a population alleles that arose elsewhere, playing a role like mutation. Natural selection can make populations either more or less similar; gene flow can only make them more similar.

**Definition 10.2.1 (Dispersal)** **Dispersal** is the movement of individuals, or of their gametes (pollen) and propagules (seeds, spores, larvae), from their place of birth to the place where they reproduce. It causes gene flow when the dispersers reproduce.

Many organisms disperse passively: pine pollen and fungal spores travel many kilometres on the wind, seeds with plumes are carried by wind and seeds with hooks by animals, spiderlings "balloon" on threads of silk to great heights and distances, and the planktonic larvae of sedentary marine animals are carried hundreds of kilometres by currents. Others disperse actively, sometimes dramatically: at high density, desert locusts (*Schistocerca gregaria*) change in behaviour and morphology into a gregarious form that flies long distances in swarms. Evolutionary biologists often use "migration" as a synonym of gene flow, a different meaning from the seasonal migration of behavioural ecology. Salmon migrate to the sea and back, but almost all return to breed in the stream where they were born, so there is very little gene flow between streams.

### 10.2.1. Measuring Gene Flow

In a population divided into discrete patches, gene flow is measured by the *migration rate* $m$, the fraction of the individuals of a population (or of its genes) that arrived from elsewhere in the last generation; the island model gives the resulting change in allele frequency, $\Delta p = m(p_{\mathrm{m}} - p)$ ([7.4.23](/7.4.23#fml-23.2.1)). In a continuous habitat there are no distinct populations, and gene flow is measured by the *dispersal variance* $\sigma^2$, the variance of the distance between the birthplaces of parent and offspring along one axis. Over $t$ generations, the displacements of a gene add up like the steps of a random walk, so its position becomes normally distributed with variance $\sigma^2t$: genes spread as a substance diffuses, with diffusion coefficient $D = \sigma^2/2$ in the notation of the heat equation ([2.5.7](/2.5.7#sec-7.1.1)).

**Example 10.2.1** Young Texas spiny lizards (*Sceloporus olivaceus*) were marked where they hatched and found again after they had established breeding territories; the distribution of distances has $\sigma^2 = 9800\,\mathrm{m^2}$, so $\sigma \approx 99\,\mathrm{m}$ per generation. Dobzhansky and Wright released $14\,026$ *Drosophila pseudoobscura* with an eye-colour marker in the Sierra Nevada of California and recaptured them in traps; assuming a mean adult life of $4.5$ days, they estimated $\sigma^2 = 21\,000\,\mathrm{m^2}$ per generation ($\sigma = 145\,\mathrm{m}$). The flightless alpine grasshopper *Podisma pedestris* has $\sigma^2 = 400\,\mathrm{m^2}$ per generation; a gene then moves about $20\sqrt{100} = 200\,\mathrm{m}$ in 100 generations and only about $2\,\mathrm{km}$ in $10\,000$. Diffusion is slow, because a random walk is as likely to go back as forward.

Direct methods of this kind, following marked individuals or assigning seeds and offspring to parents by genotyping (parentage analysis), give snapshots of dispersal over a short period. They have limitations: movements depend on conditions (in the flies, strongly on temperature); marking may change behaviour; rare long-distance movements, which contribute most to the variance, are easily missed; and dispersers that fail to reproduce contribute nothing to gene flow. Indirect methods infer gene flow from the genetic differences between populations. Mixing populations with different allele frequencies produces an excess of homozygotes (the **Wahlund effect**, [7.4.22](/7.4.22)) and **linkage disequilibrium**: in the United States, bald men more often have light than dark skin, simply because the population mixes ancestries from northern Europe, where alleles for both traits are common, and from Africa, where they are rare. The most widely used indirect approach is based on $F_{\mathrm{ST}}$ (§10.3).

## 10.3. Population Structure and Genetic Divergence

The **fixation index** $F_{\mathrm{ST}}$ ([7.4.22](/7.4.22)) measures the fraction of the genetic variance in a set of populations that is due to differences between them,

$$
F_{\mathrm{ST}} = \frac{\operatorname{Var}(p)}{\bar p(1 - \bar p)}, \tag{10.1}
$$
where $\operatorname{Var}(p)$ is the variance of the allele frequency among populations and $\bar p$ its mean. It is $0$ when the populations have identical frequencies and $1$ when each is fixed for a different allele; for two populations with frequencies $0.2$ and $0.8$, $F_{\mathrm{ST}} = 0.09/0.25 = 0.36$. Across the autosomes of East Asians, Europeans and Yoruba from Nigeria, $F_{\mathrm{ST}} \approx 0.12$: only $12\,\%$ of human genetic variation is between these populations, and $88\,\%$ is found within a typical population, so the conspicuous phenotypic differences among human populations are not representative of the genome. Populations of the northern dusky salamander (*Desmognathus fuscus*) living near New York City have $F_{\mathrm{ST}}$ more than four times larger than human populations across the whole planet, a reminder that a level of genetic differentiation alone cannot decide which populations belong to one species.

### 10.3.1. The Island Model

In Wright's island model, $n$ demes of effective size $N_e$ exchange migrants at rate $m$ through a common migrant pool. Drift increases the variance among demes and gene flow decreases it, and they balance at

$$
F_{\mathrm{ST}} \approx \frac{1}{1 + 4N_em\left(\dfrac{n}{n - 1}\right)^2}, \tag{10.2}
$$
which is $1/(1 + 4N_em)$ for many demes ([Eq. (23.12) in 7.4.23](/7.4.23#eq-23.12)) and $1/(1 + 16N_em)$ for two populations exchanging a fraction $m$ with each other. The decisive quantity is $N_em$, the number of migrants per generation, not the migration rate: one migrant per generation keeps neutral divergence small ($F_{\mathrm{ST}} \leq 0.2$) whatever the size of the demes. The same result follows from the **structured coalescent** ([7.10.7](/7.10.7)): two genes from one deme coalesce on average after $T_0 = 2nN_e$ generations, whatever the migration rate, whereas genes from different demes must first come together in one deme, which takes another $(n - 1)/(2m)$ generations; $F_{\mathrm{ST}} = (\bar T - T_0)/\bar T$, with $\bar T$ the mean coalescence time of two genes drawn at random from the whole population.

Eq. (10.2) suggests estimating gene flow from $F_{\mathrm{ST}}$ measured at neutral loci, as was done for the rock pocket mouse in §10.5. Indirect estimates average over many generations and count only migrants that actually contribute genes, but they rest on strong assumptions: an island model at equilibrium between drift and migration, with symmetric migration and constant deme sizes. A pattern of differentiation produced by history (colonization, range expansion) or by selection cannot be converted into a migration rate.

| Mode of transmission | Number of studies | Mean $F_{\mathrm{ST}}$ |
|---|---|---|
| Plants: maternally inherited organelle genes (seed only) | 29 | 0.46 |
| Plants: nuclear genes (pollen and seed) | 294 | 0.32 |
| Animals: mitochondrial genes | 150 | 0.45 |
| Animals: nuclear genes | 781 | 0.20 |

*Data from Barton et al. (2007), Table 16.2, after Morjan and Rieseberg (2004).* Organelle genes are more differentiated than nuclear genes, both because they move only with seeds (in plants) and because their effective population size is smaller (a quarter of that of autosomal genes, with one copy transmitted by one sex), which increases drift.

Population subdivision also changes the drift of the population as a whole. In the island model with symmetric migration, the effective size of the whole population is $nN_e/(1 - F_{\mathrm{ST}})$, larger than the sum of the deme sizes, because variation is stored as differences between demes. Frequent extinction and recolonization of demes has the opposite effect: alleles in expanding demes spread and those in demes that go extinct are lost, and when demes are nearly fixed the effective size of the whole population approaches the number of demes rather than the number of individuals. In HIV infections the virus lives in small clusters of lymphoid cells in the spleen; $F_{\mathrm{ST}}$ between clusters a few millimetres apart reached $0.59$ in one patient, and rapid extinction and recolonization of clusters help explain why viral diversity is much lower than expected from the huge numbers of virus particles.

### 10.3.2. Stepping Stones and Isolation by Distance

**Definition 10.3.1 (Stepping-Stone Model and Isolation by Distance)** In the **stepping-stone model** demes are arranged in a line or a lattice and exchange migrants only with their neighbours. In this model, and in continuous populations with limited dispersal, genetic differentiation between populations increases with the distance between them; this pattern is called **isolation by distance**.

Wright measured the scale of isolation by distance in a continuous two-dimensional population by the *neighbourhood size* $N_{\mathrm{b}} = 4\pi D_{\mathrm{e}}\sigma^2$, the number of breeding individuals in a circle of radius $2\sigma$ around an individual, where $D_{\mathrm{e}}$ is the effective density: with $N_{\mathrm{b}}$ below a few tens, local differentiation by drift is marked. A convenient way to analyse isolation by distance is Rousset's (1997) regression of pairwise $F_{\mathrm{ST}}/(1 - F_{\mathrm{ST}})$ on distance $r$ between samples. At distances that are not too large,

$$
\frac{F_{\mathrm{ST}}}{1 - F_{\mathrm{ST}}} \approx a + \frac{r}{4D_{\mathrm{e}}\sigma^2} \quad \text{(one dimension)}, \qquad \frac{F_{\mathrm{ST}}}{1 - F_{\mathrm{ST}}} \approx a + \frac{\ln r}{4\pi D_{\mathrm{e}}\sigma^2} \quad \text{(two dimensions)}, \tag{10.3}
$$
so the slope estimates the product $D_{\mathrm{e}}\sigma^2$, the neighbourhood size, without the assumptions of the island model. Combined with a direct estimate of $\sigma^2$, it gives the effective density; combined with a census density, it gives $\sigma^2$.

![Population structure at drift–migration equilibrium. A: the island model, F_ST against the number of migrants per generation N_e m, for many demes and for two demes (Eq. (10.2)); about one migrant per generation keeps neutral differentiation low whatever the deme size. B: isolation by distance in a one-dimensional stepping-stone model (60 demes of 50 diploids in a ring, migration 0.1 per generation to the neighbouring demes, mutation rate 10⁻⁴), computed exactly from the recursion for identity by descent. Pairwise F_ST/(1 − F_ST) rises linearly with distance with the slope 1/(4Dσ²) = 0.05 of Eq. (10.3) (dashed) and levels off at distances where mutation, rather than migration, limits the identity of genes](./plots/isolation-by-distance.py)

Human populations show isolation by distance: $F_{\mathrm{ST}}$, estimated from 783 loci, increases with the distance between pairs of populations measured along the routes by which humans spread. But this pattern reflects history rather than equilibrium. Populations on opposite sides of the globe are more similar than current gene flow could explain; the gradient reflects the colonization of the world by modern humans, with a loss of diversity in each step of a series of founder events ([7.10.33](/7.10.33)). A history of frequent extinction and recolonization similarly makes a species more homogeneous over large areas than present dispersal would suggest.

## 10.4. Divergence of Quantitative Traits: $Q_{\mathrm{ST}}$ and $F_{\mathrm{ST}}$

Neutral loci show the divergence expected from drift and gene flow alone. A quantitative trait has an analogous measure, defined from the variance of population means $V_{\mathrm{B}}$ and the mean additive genetic variance within populations $V_{A,\mathrm{W}}$ (estimated in a common environment):

$$
Q_{\mathrm{ST}} = \frac{V_{\mathrm{B}}}{V_{\mathrm{B}} + 2V_{A,\mathrm{W}}}. \tag{10.4}
$$
For a neutral additive trait, the population means drift exactly as allele frequencies do, and $Q_{\mathrm{ST}} = F_{\mathrm{ST}}$ in expectation. A trait with $Q_{\mathrm{ST}} > F_{\mathrm{ST}}$ has diverged more than drift can explain, which suggests divergent selection and local adaptation; $Q_{\mathrm{ST}} < F_{\mathrm{ST}}$ suggests stabilizing selection for the same optimum everywhere.

**Example 10.4.1** A trait with additive genetic variance $V_{A,\mathrm{W}} = 200$ within each population is measured in populations whose neutral $F_{\mathrm{ST}}$ is $0.02$. Under neutrality the expected variance among population means is $V_{\mathrm{B}} = 2V_{A,\mathrm{W}}F_{\mathrm{ST}}/(1 - F_{\mathrm{ST}}) = 8.2$, a standard deviation of $2.9$ trait units among population means. A much larger observed variance indicates divergent selection.

The comparison has pitfalls: $Q_{\mathrm{ST}}$ is estimated with large error from few populations, non-additive variance and maternal effects bias it, and the neutral expectation assumes that the trait and the marker loci have the same history. The same logic applies at the level of single loci. **Genome scans** ([7.10.8](/7.10.8)) search for loci whose $F_{\mathrm{ST}}$ is much higher than the genomic background. Marine three-spined sticklebacks (*Gasterosteus aculeatus*) have independently colonized thousands of freshwater lakes and streams around the Northern Hemisphere; in comparisons of three freshwater–marine pairs, the same genomic regions show peaks of differentiation, among them the region on chromosome 4 containing *Eda*, which controls the reduction of lateral armour plates in fresh water. In humans, *EPAS1*, involved in Tibetan adaptation to high elevation, was found by scanning for regions of high divergence.

## 10.5. Gene Flow and Selection

When selection favours different alleles in different places, it tends to fix whatever is best locally, and gene flow tends to make allele frequencies equal everywhere. Geographic patterns are compromises between the two.

### 10.5.1. Migration–Selection Balance

**Definition 10.5.1 (Migration–Selection Balance)** **Migration–selection balance** is an equilibrium in which the change in allele frequency caused by selection in a population is balanced by the change caused by gene flow from populations in which other alleles prevail.

**Formula 10.5.1 (Island Adapting Against Gene Flow)** Let an island receive a fraction $m$ of its genes per generation from a continent fixed for $A_1$, while on the island the genotypes $A_1A_1$, $A_1A_2$, $A_2A_2$ have fitnesses $1$, $1 + s$, $1 + 2s$. If $m \ll s$, the equilibrium frequency of $A_2$ on the island is

$$
p_2 \approx 1 - \frac{m}{s}, \tag{10.5}
$$
and the locally favoured allele cannot be maintained if $m$ exceeds about $s$.

**Proof** Near fixation of $A_2$, let $q$ be the frequency of $A_1$. Selection reduces $q$ by about $sq(1 - q) \approx sq$ per generation, and migration increases it by $m(1 - q) \approx m$. Equating gives $q \approx m/s$. When $A_2$ is rare, selection increases its frequency by a factor of about $1 + s$ and migration decreases it by $1 - m$, so $A_2$ can increase only if $s > m$ approximately. $\square$

**Definition 10.5.2 (Gene Swamping)** **Gene swamping** is the loss, or prevention, of local adaptation because gene flow from populations in which other alleles are favoured overwhelms local selection.

These results can be used to estimate selection in nature. The rock pocket mouse (*Chaetodipus intermedius*) of the deserts of the southwestern United States is usually light-coloured, matching granite and sand, but a dark form is common on dark lava flows, where it is camouflaged against owls; the dark colour is due to an allele at *Mc1r*. From the allele frequencies and a migration rate estimated indirectly from neutral markers, selection favouring the melanic allele on the lava was estimated at up to $s = 0.4$, extremely strong selection. Conversely, the mosquito *Culex pipiens* has evolved insecticide resistance in many places, but on Corsica resistance has not evolved although resistance alleles are present at low frequency: the treated patches are small, and mosquitoes moving in from untreated surroundings swamp the resistance alleles.

![Migration–selection balance. A: equilibrium frequency of an allele A₂ favoured on an island (s = 0.05) that receives migrants from a continent fixed for A₁, against the ratio m/s. With additive fitnesses the frequency falls almost linearly (dashed: the approximation 1 − m/s) and A₂ is lost when m ≈ s; when A₂ is dominant it persists at higher migration rates; when it is recessive it is lost abruptly at m ≈ 0.48s, because rare recessive alleles are hidden from selection in heterozygotes. B: gene swamping in continuous space. A patch of width L (in units of the characteristic length l = √(σ²/2s)) in which A₂ has advantage s lies in a habitat where it has disadvantage s; numerical steady states show the frequency of A₂, labelled with its maximum. Patches narrower than (π/2)l lose the allele completely](./plots/migration-selection.py)

### 10.5.2. Clines in a Step Environment

In continuous space, selection and gene flow interact through the dispersal variance. Let $A_2$ have a relative fitness advantage $s$ to the east of a boundary at $x = 0$ and the same disadvantage to the west. Without gene flow each allele would be fixed on its side; with gene flow a cline forms, described by the reaction–diffusion equation

$$
\frac{\partial p}{\partial t} = \frac{\sigma^2}{2}\frac{\partial^2p}{\partial x^2} + s(x)\,p(1 - p), \qquad s(x) = s\operatorname{sgn}(x), \tag{10.6}
$$
a heat equation with a source term ([2.5.7](/2.5.7#sec-7.5.2)). Measuring distance in units of the characteristic length $l = \sqrt{\sigma^2/(2s)}$ removes both parameters, so the shape of the cline is fixed and only its scale depends on dispersal and selection.

**Formula 10.5.2 (Cline Width)** The steady-state cline of Eq. (10.6) changes from $p = 0.1$ to $p = 0.9$ over a distance

$$
w_{\mathrm{c}} \approx 2.5\sqrt{\sigma^2/s}. \tag{10.7}
$$

The constant follows from the numerical solution (Figure, panel A). Cline width is proportional to $\sigma/\sqrt{s}$: strong selection and short dispersal give sharp clines. The relation can be inverted to estimate selection from a measured cline width and dispersal. Along the Mediterranean coast of southern France, a belt about $20\,\mathrm{km}$ wide is sprayed with organophosphate insecticides, and resistance alleles of *Culex pipiens* at two loci, *Ace1* (altered acetylcholinesterase, the target of the insecticide) and *Est1* (overproduced detoxifying esterases), form clines that sharpen each summer and broaden each winter. Fitting a model of this kind to genotype frequencies along transects gave dispersal of $\sigma^2 = 6.6\,\mathrm{km^2}$ per generation in summer and $14.6\,\mathrm{km^2}$ in autumn, and selection coefficients of $0.33$ (*Ace1*) and $0.19$ (*Est1*) in favour of resistance in the treated zone and $0.11$ and $0.05$ against it outside. The same model predicts that resistance could not become established if the treated zone were only about half as wide, because gene flow would swamp it.

The characteristic length also sets the spatial resolution of adaptation: an allele favoured only in a patch much smaller than $l$ cannot be maintained there, and in the model of Eq. (10.6) the critical patch width is $(\pi/2)l$. In the copper-mine grass, gene flow from the pasture keeps the mine population from becoming fixed for tolerance, and gene flow from the mine keeps tolerance alleles in the nearby pasture; the transect running downwind from the mine has a much broader cline than the upwind one, because pollen from tolerant plants is carried far downwind. Seeds collected on the mine are less tolerant than adults growing there, and seeds collected off the mine more tolerant than adults there: each generation, selection sharpens the cline that gene flow has broadened. Quantitative traits under stabilizing selection with an optimum that changes in space form clines in the same way; the shape of a cline says little about whether the environment changes abruptly or gradually.

### 10.5.3. Tension Zones

Selection can maintain a cline even where it acts the same way everywhere.

**Definition 10.5.3 (Tension Zone)** A **tension zone** is a cline maintained by a balance between gene flow and selection against hybrids or heterozygotes (**underdominance**, [7.4.23](/7.4.23#def-23.3.2)), or more generally against rare forms, in an environment that need not change across the cline.

On each side of a tension zone the rarer type is found mostly in heterozygotes and is selected against, so each side is held at its own fixed state; gene flow broadens the zone, selection sharpens it. In the alpine grasshopper *Podisma pedestris*, populations in the southern Maritime Alps differ by a fusion between the X chromosome and an autosome. Where they meet, the frequency of the fusion changes in a cline about $800\,\mathrm{m}$ wide that runs for more than $100\,\mathrm{km}$ through a wide variety of habitats and across the whole altitudinal range of the species, strong evidence that it is maintained by uniform selection against chromosomal heterozygotes rather than by environmental differences. The two races met after the last glaciation, roughly $10\,000$ generations ago (the species has one generation a year); had they simply mixed, the cline would by now be $\sqrt{2\pi\sigma^2t} = \sqrt{2\pi \cdot 400 \cdot 10\,000} \approx 5\,\mathrm{km}$ wide.

**Formula 10.5.3 (Width of a Tension Zone)** With heterozygote fitness $1 - s^*$ relative to both homozygotes, the steady-state tension zone has width (inverse of the maximum slope)

$$
w = \sqrt{8\sigma^2/s^*}. \tag{10.8}
$$

**Proof** For weak selection the frequency changes by $s^*pq(2p - 1)$ per generation, so the cline satisfies $\frac{\sigma^2}{2}p'' + 2s^*p(1 - p)(p - \tfrac12) = 0$. This is the bistable reaction–diffusion equation of [7.6.36](/7.6.36#sec-36.5.2) with $k = 2s^*$, threshold $a = \frac12$ and diffusion coefficient $D = \sigma^2/2$, whose front is $p = [1 + \exp(-x\sqrt{k/2D})]^{-1}$ and is stationary because $a = \frac12$. Its maximum slope is $\frac14\sqrt{k/2D} = \frac14\sqrt{2s^*/\sigma^2}$, whose inverse is Eq. (10.8). $\square$

For *Podisma*, $w = 800\,\mathrm{m}$ and $\sigma^2 = 400\,\mathrm{m^2}$ give $s^* = 8 \cdot 400/800^2 = 0.005$: selection of only half a percent against heterozygotes maintains the zone. If the two homozygotes differ in fitness, the threshold differs from $\frac12$ and the zone moves towards the less fit type at the speed given in [7.6.36](/7.6.36#thm-36.5.1); tension zones also move towards regions of low population density and tend to be trapped at density troughs and natural barriers, which is why many of them lie along rivers and mountain ridges. Tension zones also arise between races of Müllerian mimics: the warningly coloured butterflies *Heliconius erato* and *H. melpomene* converge on the same pattern in each area, and their ranges are divided into a mosaic of races separated by narrow clines, maintained by predation on rare, unfamiliar patterns. Many tension zones are hybrid zones between divergent populations ([7.10.12](/7.10.12)).

![Clines maintained by selection against gene flow (numerical steady states). A: a step environment, in which A₂ has relative fitness advantage s east of x = 0 and disadvantage s west of it, for four values of σ²/s; the width from p = 0.1 to p = 0.9 is 2.50√(σ²/s) in each case. B: a tension zone maintained by selection s* against heterozygotes in a uniform environment, in units of σ/√s*; the numerical cline agrees with the exact front of the bistable equation (dots), whose width is √(8σ²/s*). Dashed: a neutral cline of the same width formed by the mixing of two populations; unlike the tension zone it keeps widening, as √(2πσ²t)](./plots/clines.py)

### 10.5.4. The Spread of Favourable Alleles

A new allele that is favoured everywhere first increases locally; once established in a region it spreads outwards as a wave. If $s(x) = s$ everywhere, Eq. (10.6) becomes the **Fisher–KPP equation**, introduced by Fisher (1937) for exactly this problem.

**Formula 10.5.4 (Speed of the Wave of Advance)** A favourable allele with advantage $s$ spreading by diffusion with dispersal variance $\sigma^2$ advances at the speed

$$
v = \sqrt{2s\sigma^2}. \tag{10.9}
$$

**Proof** The minimal wave speed of $u_t = Du_{xx} + ru(1 - u)$ is $c^* = 2\sqrt{rD}$ ([2.5.7](/2.5.7#sec-7.5.2)); with $D = \sigma^2/2$ and $r = s$ this is Eq. (10.9). $\square$

An allele with $s = 0.005$ thus advances $\sqrt{0.01} = 0.1$ dispersal distances per generation, taking ten generations to cross one dispersal distance and $10\,000$ generations to cross a thousand. The same equation describes the spread of a species into empty habitat. Five muskrats (*Ondatra zibethicus*) escaped from a fur farm near Prague in 1905, and the species spread across Europe in a front advancing about $14\,\mathrm{km}$ per year. In a laboratory analogue, short RNA molecules replicated by Q$\beta$ replicase in a capillary tube spread as fronts whose speed, about $2.3\,\mu\mathrm{m\,s^{-1}}$, matched Fisher's prediction from the measured rate of diffusion of the replicating complex ($7.6 \times 10^{-11}\,\mathrm{m^2\,s^{-1}}$, the variance of distance moved per unit time, which plays the role of $\sigma^2$) and its exponential growth rate ($0.038\,\mathrm{s^{-1}}$): $\sqrt{2 \cdot 0.038 \cdot 7.6 \times 10^{-11}} = 2.4\,\mu\mathrm{m\,s^{-1}}$; a sudden increase of speed marked the replacement of the sequence by a faster-replicating variant.

Many spreads are much faster than local diffusion allows. After the last glaciation, tree species expanded their ranges by more than $100\,\mathrm{m}$ per year, although most seeds fall within $30\,\mathrm{m}$ and trees take decades to mature; cheatgrass (*Bromus tectorum*) spread through the rangelands of the western United States in erratic jumps along the railways. Rare long-distance dispersal founds colonies ahead of the front, which grow and merge, so that the advance is patchy and tends to accelerate. Subdivision of a species into demes slows the spread of a favourable allele but, with symmetric gene flow, does not change its probability of fixation, which remains about $2s$.

![The spread of a favourable allele. A: numerical solution of the Fisher–KPP equation with s = 0.05 and σ = 1 (distance in dispersal SDs) from a local introduction, profiles every 100 generations: a front of constant shape moves outwards in both directions. B: position of the front (p = 0.5) for s = 0.02, 0.05 and 0.1; after a transient the speed approaches √(2sσ²) (dashed). C: spread in an integro-difference model with logistic growth and a Gaussian dispersal kernel (blue) or a kernel of the same variance near the parent but with rare long jumps (red): long-distance dispersal founds colonies ahead of the front and the spread is many times faster](./plots/fisher-wave.py)

## 10.6. Gene Flow, Drift and Local Adaptation

Drift, too, can build up differences between populations, and its power to do so is also limited by gene flow. In the land snail *Cepaea nemoralis*, shell colour and banding correlate with vegetation and climate on a fine scale, which suggests selection, whereas allozyme frequencies vary over large regions separated by relatively sharp clines that reflect the historical origins of eastern, central and western populations. Local adaptation requires that selection be strong relative to both forces: $s$ must exceed $m$ (or the dispersal scale must be small relative to the patch), and $N_es$ must be much larger than one, or drift will fix alleles irrespective of their effects. Gene flow also has positive effects on adaptation: it brings new favourable alleles from elsewhere, and in small isolated populations, in which drift has fixed deleterious mutations, immigrants produce fitter offspring than residents. This immigrant advantage amplifies the genetic effect of migration and can rescue small populations from **inbreeding depression** ([7.4.24](/7.4.24)), the basis of genetic rescue in conservation ([7.10.34](/7.10.34)).

## 10.7. The Evolution of Dispersal

Dispersal itself is a trait under selection, and its benefits and costs vary.

- *Disturbance and changing habitats.* When the environment changes in time and space, dispersal is favoured if individuals that move have higher fitness on average than those that stay. When local populations are periodically destroyed, a genotype that never disperses has no descendants in the long run. Dandelions live in temporary open patches created by disturbance and eventually overgrown; their seeds carry a parachute (pappus) that reaches new patches. In an experiment with the nematode *Caenorhabditis elegans* in dishes with two food patches, worms were transferred each time from only one randomly chosen patch, simulating extinction of the other; within five generations a high-dispersal genotype became much more common, despite its lower fecundity, whereas in control treatments without extinction it became rarer.
- *Kin competition.* If a plant drops all its seeds in its own patch, which can support only one plant, many may germinate but only one inherits the patch; seeds that leave compete with fewer relatives. Dispersal is therefore favoured by **kin selection** ([7.10.16](/7.10.16)) even when it is costly.
- *Inbreeding avoidance.* Mating between relatives produces offspring with inbreeding depression; organisms that cannot recognize relatives reduce this risk by dispersing far from their birthplace.
- *Costs.* Passive dispersers may land in hostile habitat, and active dispersers must cross bad habitat. Salamanders inhabiting isolated springs in the hot, dry southwestern United States have lost the terrestrial stage of their life cycle, which once allowed dispersal between springs; the Barton Springs salamander (*Eurycea sosorum*) now lives only in the aquifer feeding a group of springs in Austin, Texas, a range of a few square kilometres, where a single catastrophe could exterminate it. Dispersal is also energetically expensive: in Roesel's bush-cricket (*Metrioptera roeselii*) and many other crickets, a long-winged morph that can fly has lower fecundity than a short-winged morph, probably because of the cost of flight muscles.

**Formula 10.7.1 (Dispersal Under Kin Competition)** In a habitat of sites each occupied by one adult, in which offspring compete for vacant sites and a dispersing offspring survives with probability $p$, the evolutionarily stable fraction of offspring that disperse is (Hamilton and May 1977)

$$
v^* = \frac{1}{2 - p}. \tag{10.10}
$$

Even when dispersal is almost certainly fatal ($p \to 0$), half of the offspring should disperse, because an offspring that stays competes with its siblings for the parent's site, whereas each one that leaves and survives competes only with strangers.

Dispersal also changes the composition of populations without any selection. The Glanville fritillary (*Melitaea cinxia*) lives in meadows surrounded by forest; a newly formed meadow is colonized by strong fliers, and flight ability, which is heritable, is high in a new population for several generations and then declines, because the strongest fliers leave. In a range expansion, the best dispersers arrive at the front first and mate with each other, so that dispersal ability increases at the front by spatial sorting. Cane toads (*Rhinella marina*), introduced to Australia from South America in 1935, have been expanding their range ever since: the toads at the invasion front have longer legs, which make them faster dispersers, and the front has accelerated over the decades. Paleontologists have found that marine snails with planktonic larvae had larger geographic ranges and longer durations in the fossil record than those without ([7.10.31](/7.10.31)).

![The evolution of dispersal. A: the evolutionarily stable dispersal fraction under kin competition (Formula 10.7.1) against the survival of dispersers: at least half of the offspring should disperse however costly dispersal is. B: spatial sorting in an individual-based simulation of a range expansion, in which offspring inherit the dispersal distance of their parent with small mutations: the mean dispersal distance at the expanding front (red) rises well above that in the core of the range (blue), without any selective advantage of dispersal](./plots/dispersal-evolution.py)

## 10.8. The Evolution of Species' Ranges

Humans occupy almost the entire land surface; the Barton Springs salamander occupies a few square kilometres. Some ranges are limited by obvious barriers, the edges of continents for marine species and of oceans for terrestrial ones. But many range limits have no barrier, and they pose one of the most puzzling questions of evolutionary biology: why do populations at the edge not adapt to the conditions just beyond it, so that the range expands? Several explanations have been proposed.

- *Lack of genetic variation.* Two species of rainforest *Drosophila* have no detectable genetic variation for desiccation tolerance, which may prevent them from expanding into drier habitats ([7.10.9](/7.10.9), Definition 9.6.3 of evolutionary constraint).
- *Gene swamping.* Gene flow from the centre of the range, where populations are dense and adapted to central conditions, may prevent populations at the edge from adapting to more extreme conditions. Kirkpatrick and Barton (1997) formalized this for a quantitative trait whose optimum changes along an environmental gradient: asymmetric gene flow from dense central populations pulls marginal populations away from their optimum, lowering their fitness and density, which makes them still more dominated by immigrants; when the gradient is steep relative to the dispersal distance and the strength of selection, adaptation fails and the range stops expanding. The model also shows the opposite possibility: gene flow increases the genetic variance of marginal populations and can thereby help them adapt. Consistent with swamping, cold resistance of the fly *Drosophila birchii* in Australian rainforest is lower at the top of a steep mountain slope than at the same altitude on a shallow slope, where high-altitude populations are farther from warm-adapted lowland populations and receive less gene flow from them.
- *Biotic interactions.* A range may end where a species meets a superior competitor, a predator or a pathogen ([7.10.17](/7.10.17)).

Climate change is a large, uncontrolled experiment on ranges. Species living along a gradient can respond by shifting their ranges or by adapting. Reviews of species with historical records find that many, perhaps more than half, have shifted in the direction expected from warming: in the Northern Hemisphere, northern limits have moved north and upwards while southern limits retreat. These are geographic, not evolutionary, changes; there is little evidence that most species have evolved broader or more extreme climatic tolerance. Species that cannot disperse fast enough, meet barriers or run out of habitat at mountain tops and coasts shrink in range; range expansion by adaptation at the trailing edge is rarely observed. As for evolutionary rescue ([7.10.9](/7.10.9)), the hope that adaptation will save most species from rapid climate change appears dim.

## Summary

| Process | Key quantity | Result | Reference |
|---|---|---|---|
| Dispersal | $m$ (patches), $\sigma^2$ (continuous) | Genes diffuse with variance $\sigma^2t$; neutral clines widen as $\sqrt{2\pi\sigma^2t}$ | Definition 10.2.1, Example 10.2.1 |
| Drift–migration balance | $N_em$ | $F_{\mathrm{ST}} \approx 1/(1 + 4N_em)$; one migrant per generation prevents strong divergence | Eq. (10.2) |
| Isolation by distance | $D_{\mathrm{e}}\sigma^2$ | $F_{\mathrm{ST}}/(1 - F_{\mathrm{ST}})$ linear in $r$ (1D) or $\ln r$ (2D) | Definition 10.3.1, Eq. (10.3) |
| Trait divergence | $Q_{\mathrm{ST}}$ vs $F_{\mathrm{ST}}$ | $Q_{\mathrm{ST}} > F_{\mathrm{ST}}$: divergent selection | Eq. (10.4) |
| Migration–selection | $m/s$ | $p \approx 1 - m/s$; swamping when $m \gtrsim s$ | Formula 10.5.1, Definition 10.5.2 |
| Cline in a step environment | $l = \sqrt{\sigma^2/2s}$ | Width $2.5\sqrt{\sigma^2/s}$; patches smaller than about $l$ cannot be adapted to | Formula 10.5.2 |
| Tension zone | $s^*$ against heterozygotes | Width $\sqrt{8\sigma^2/s^*}$; zones move to density troughs | Definition 10.5.3, Formula 10.5.3 |
| Favourable allele | $s$, $\sigma^2$ | Wave of advance at $\sqrt{2s\sigma^2}$ | Formula 10.5.4 |
| Dispersal evolution | disturbance, kin competition, inbreeding, costs | ESS dispersal $1/(2 - p)$ with kin competition; spatial sorting at range edges | Formula 10.7.1 |
| Range limits | gradient steepness vs dispersal | Lack of variation, gene swamping, biotic interactions | §10.8 |

## Questions

1. A population with allele frequency $0.4$ receives $10\,\%$ of its individuals each generation from a population with frequency $0.6$. Compute the frequency in the next two generations and in the long run.

   **Answer** $p_1 = 0.4 + 0.1(0.6 - 0.4) = 0.42$ and $p_2 = 0.42 + 0.1(0.18) = 0.438$. The change is smaller in the second generation ($0.018$ against $0.020$) because the difference from the source has decreased by the factor $0.9$. In the long run the frequency approaches $0.6$.

2. Two populations exchanging migrants only with each other have $F_{\mathrm{ST}} = 0.25$ at neutral loci. Estimate $N_em$ under the two-population model and under the model of many demes. Why is the distinction important?

   **Answer** Two populations: $1/(1 + 16N_em) = 0.25$ gives $N_em = 3/16 = 0.19$. Many demes: $1/(1 + 4N_em) = 0.25$ gives $N_em = 0.75$. The estimate of gene flow depends by a factor of four on assumptions about the structure that usually cannot be checked; in addition both assume equilibrium, which history can violate. Indirect estimates should therefore be treated as orders of magnitude.

3. In a step environment, a cline in an allele conferring resistance has width $w_{\mathrm{c}} = 5\,\mathrm{km}$ (from $10\,\%$ to $90\,\%$), and dispersal is $\sigma^2 = 1\,\mathrm{km^2}$ per generation. Estimate $s$. What is the smallest treated area in which resistance can be maintained?

   **Answer** From Eq. (10.7), $s = (2.5\sigma/w_{\mathrm{c}})^2 = (2.5/5)^2 = 0.25$. The characteristic length is $l = \sqrt{\sigma^2/2s} = \sqrt{2} = 1.41\,\mathrm{km}$, and in the model of Eq. (10.6) a treated strip narrower than $(\pi/2)l \approx 2.2\,\mathrm{km}$ cannot maintain the allele if it is equally disfavoured outside.

4. Show that Fisher's speed $\sqrt{2s\sigma^2}$ means that the time for an allele to spread across a range of length $L$ scales as $L/\sqrt{s}$, whereas the time to increase from a single copy to high frequency in a well-mixed population scales as $\ln(N)/s$. Which process limits the rate of adaptation of a widespread species with limited dispersal?

   **Answer** Crossing a distance $L$ at speed $\sqrt{2s}\,\sigma$ takes $L/(\sigma\sqrt{2s})$ generations. In a well-mixed population an allele goes from $1/(2N)$ to $1/2$ in about $\ln(2N)/s$ generations ([7.4.23](/7.4.23#fml-23.3.2)). For a species whose range is many thousands of dispersal distances, $L/\sigma \gg \ln(2N)/\sqrt{s}$, so spatial spread is the rate-limiting step, and favourable mutations may arise independently in different places before one has spread everywhere (producing soft sweeps or mosaics of different adaptive alleles, as in human malaria resistance).

5. According to Formula 10.7.1, at least half of the offspring disperse even if dispersal is almost always fatal. Explain the result intuitively, and state what would change if several adults shared a site or if dispersal were towards sites occupied by relatives.

   **Answer** An offspring that stays competes with its siblings for one site; from the parent's point of view, the extra offspring that stay after the first add almost nothing, because only one can win, whereas each dispersing offspring has a small but independent chance of winning a site elsewhere. With several adults per site, the siblings staying at home make up a smaller fraction of competitors, kin competition is weaker and the stable dispersal rate is lower; if dispersers also landed among relatives, the benefit of leaving would be reduced in the same way.
