---
title: Detecting Selection in Genomes
description: "The neutral theory as null hypothesis for detecting selection in DNA sequences: synonymous and nonsynonymous substitutions, the dN/dS ratio and its counting estimate, selective constraint and codon usage bias; neutrality tests from polymorphism: Tajima's D, Fu and Li's D, Fay and Wu's H, confounding by demography; tests combining polymorphism and divergence: the HKA test, the McDonald–Kreitman test and the proportion of adaptive substitutions α; linked selection: hard and soft sweeps, background selection, diversity and recombination, balancing selection and trans-species polymorphism; genome scans and local adaptation; measuring selection directly and from allele-frequency time series; selection on noncoding DNA and the extent of selection in genomes."
---

Selection leaves traces in genomes, and drift and mutation leave traces too. The neutral theory ([7.10.6](/7.10.6#sec-6.6)) makes precise predictions for sequences evolving under mutation and drift alone, and coalescent theory ([7.10.7](/7.10.7)) turns them into probability distributions for polymorphism within species and divergence between them. Every test of selection compares data with these predictions. The tests differ in what they compare: kinds of sites that differ in their likely fitness effects (synonymous and nonsynonymous), the frequency spectrum of polymorphism, polymorphism and divergence together, or patterns along the chromosome produced by selection at linked sites. They also differ in what they detect: purifying selection, recurrent positive selection over millions of years, a single recent sweep, or balancing selection.

This chapter presents the theory of these tests. Its foundations are Theorem 7.3.3 (the neutral site frequency spectrum) and Formula 5.4.2 (the footprint of a selective sweep); the computation of $F_{\mathrm{ST}}$ and haplotype statistics on real data is in [7.8.13](/7.8.13#sec-13.6), and the likelihood analysis of codon substitution models for detecting adaptive protein evolution along particular lineages and sites is in [7.10.23](/7.10.23).

## 8.1. Divergence: Synonymous and Nonsynonymous Change

### 8.1.1. Synonymous and Nonsynonymous Substitutions

The redundancy of the genetic code provides a natural internal control. Changes at the third position of many codons do not alter the amino acid (CCU, CCC, CCA and CCG all encode proline), while changes at first and second positions usually do.

**Definition 8.1.1 (Synonymous and Nonsynonymous Substitutions)** A **synonymous substitution** is a nucleotide substitution in a protein-coding sequence that does not change the encoded amino acid; a **nonsynonymous substitution** (replacement substitution) changes it. The synonymous and nonsynonymous distances $d_{\mathrm{S}}$ and $d_{\mathrm{N}}$ are the numbers of synonymous substitutions per synonymous site and of nonsynonymous substitutions per nonsynonymous site between two sequences.

Counting methods (Nei and Gojobori 1986) estimate them in three steps. First, sites are counted: each codon has three sites, and a site is counted as a fraction $f$ synonymous if a fraction $f$ of the three possible changes at it is synonymous; for CCU, the third position is fully synonymous and the first two are fully nonsynonymous, giving 1 synonymous and 2 nonsynonymous sites. Summing over the sequence (averaged over the two sequences) gives $S$ and $N$ sites. Second, the observed differences are classified as synonymous ($S_d$) or nonsynonymous ($N_d$), averaging over the possible paths when a codon differs at more than one position. Third, the proportions $p_{\mathrm{S}} = S_d/S$ and $p_{\mathrm{N}} = N_d/N$ are corrected for multiple substitutions, for example with the Jukes–Cantor formula $d = -\frac34\ln(1 - \frac43p)$ ([7.8.6](/7.8.6#sec-6.2)). These approximations ignore transition–transversion bias and codon frequencies; the likelihood codon models of [7.10.23](/7.10.23) avoid them.

**Definition 8.1.2 (dN/dS Ratio)** The **dN/dS ratio** $\omega = d_{\mathrm{N}}/d_{\mathrm{S}}$ measures selection on the protein relative to the synonymous benchmark:

| $\omega$ | interpretation |
|---|---|
| $\omega < 1$ | most nonsynonymous mutations are deleterious and removed by purifying selection |
| $\omega \approx 1$ | nonsynonymous changes evolve as if neutral |
| $\omega > 1$ | nonsynonymous changes have been fixed faster than neutral ones, evidence of positive selection |

Because synonymous and nonsynonymous sites are interleaved in the same gene, the ratio is insensitive to variation in mutation rate among genes and lineages, and it needs only one sequence from each of two species. Most genes are dominated by purifying selection: in a comparison of 15 350 genes between humans and mice, almost all have $\omega$ well below 1. The genes with $\omega > 1$ belong to a few functional classes, above all host–pathogen interactions and reproduction, where arms races keep the optimum moving ([7.10.17](/7.10.17)). The breast-cancer gene *BRCA1* has $\omega > 1$ on the human and chimpanzee branches of the great-ape phylogeny, perhaps through a role in defense against viruses. Sperm lysin of abalones, which dissolves the egg envelope species-specifically, has been compared among 25 species: its codons fall into a rapidly evolving class with $\omega \approx 3.1$, concentrated on the exposed surface of the protein, an intermediate class with $\omega \approx 0.9$ and a slow class with $\omega \approx 0.09$.

The ratio is a conservative test. Averaged over a whole gene and over the whole time since divergence, it is below 1 whenever most sites are constrained, even if a few have been under strong positive selection; this is why methods that let $\omega$ vary among sites and lineages ([7.10.23](/7.10.23)) detect far more cases. Rates can also be accelerated episodically: lysozyme acquired a digestive function in the stomachs of ruminants and of leaf-eating colobine monkeys, and evolved by bursts of amino acid substitution in both lineages, several identical in the two.

**Definition 8.1.3 (Selective Constraint)** The *selective constraint* on a sequence is the fraction of its mutations that are removed by purifying selection, measured as the reduction of its rate of evolution (or of its diversity) relative to a neutral standard: $1 - \omega$ for a protein against synonymous sites, or one minus the ratio of substitution rates for noncoding sequence against a putatively neutral reference.

Constraint explains the hierarchy of rates of the neutral theory ([7.10.6](/7.10.6#sec-6.6)) and applies equally to polymorphism: in the glycoprotein gene of vesicular stomatitis virus, synonymous diversity is about 20 times nonsynonymous diversity.

### 8.1.2. Codon Usage Bias

Synonymous sites are not entirely free of selection. In *E. coli*, yeast, *Caenorhabditis elegans* and *Drosophila*, highly expressed genes use some codons much more often than their synonyms, and the preferred codons correspond to the most abundant tRNAs; within genes, the bias is strongest at functionally important sites, suggesting selection for translational accuracy as well as speed. This **codon usage bias** is the classic case of selection with $N_{\mathrm{e}}s$ of order one ([7.10.6](/7.10.6#sec-6.5)). If a site mutates from a preferred to an unpreferred codon at rate $u$ and back at rate $v$, and the preferred codon has selective advantage $s$, then in the regime of weak mutation the population spends time in the two states in the ratio

$$
\frac{\mathbb{P}(\text{preferred})}{\mathbb{P}(\text{unpreferred})} = \frac vu\,\mathrm{e}^{4N_{\mathrm{e}}s}, \tag{8.1}
$$

because transitions in the two directions occur at rates $2Nu\cdot u(-s)$ and $2Nv\cdot u(s)$, and Kimura's formula gives $u(s)/u(-s) = \mathrm{e}^{4N_{\mathrm{e}}s}$ (the stationary distribution of Formula 6.3.1; compare [Theorem 41.3.1](/7.6.41#thm-41.3.1)). Codon usage thus measures the product $N_{\mathrm{e}}s$: it is pronounced in species with very large effective sizes and weak in mammals, where synonymous codon choice is dominated by mutation bias and by regional base composition. An MK-like comparison (§8.2.3) of preferred and unpreferred changes within and between species of *Drosophila* confirms that this weak selection is real.

## 8.2. Neutrality Tests from Polymorphism and Divergence

**Definition 8.2.1 (Neutrality Test)** A **neutrality test** is a statistical test of the null hypothesis that the observed variation within and between species was produced by mutation and drift alone, under a specified neutral model (usually a single randomly mating population of constant size at mutation–drift equilibrium, with the infinite-sites model).

The null hypothesis is composite. Rejection means that some assumption fails, which may be neutrality, but also constant size, random mating or the mutation model. The tests below differ in how they separate these possibilities.

### 8.2.1. Tests Based on the Site Frequency Spectrum

Under the neutral null model every estimator of $\theta$ built from the site frequency spectrum has expectation $\theta$ (Theorem 7.3.3), so differences between estimators that weight frequency classes differently measure departures of the spectrum from $\theta/i$.

**Definition 8.2.2 (Tajima's D)** **Tajima's D** (Tajima 1989) is the standardized difference between the mean number of pairwise differences and Watterson's estimator for a sample of $n$ sequences with $S$ segregating sites,

$$
D = \frac{\hat\theta_\pi - S/a_1}{\sqrt{e_1S + e_2S(S - 1)}}, \tag{8.2}
$$

with $a_1 = \sum_{i=1}^{n-1}1/i$, $a_2 = \sum_{i=1}^{n-1}1/i^2$, $b_1 = \frac{n + 1}{3(n - 1)}$, $b_2 = \frac{2(n^2 + n + 3)}{9n(n - 1)}$, $c_1 = b_1 - 1/a_1$, $c_2 = b_2 - \frac{n + 2}{a_1n} + \frac{a_2}{a_1^2}$, $e_1 = c_1/a_1$ and $e_2 = c_2/(a_1^2 + a_2)$. The denominator estimates the standard deviation of the numerator under neutrality.

The numerator has mean zero under the null model because $\mathbb{E}[\hat\theta_\pi] = \mathbb{E}[S]/a_1 = \theta$ (Theorem 7.3.2 and Definition 7.3.3). Since $\hat\theta_\pi$ weights intermediate-frequency variants and $S/a_1$ counts all variants equally, the sign of $D$ reads the shape of the spectrum:

- $D < 0$: an excess of rare variants, as after a selective sweep (new mutations on a star-like genealogy), during population expansion, or with slightly deleterious variants kept rare by purifying selection;
- $D > 0$: an excess of intermediate-frequency variants, as under balancing selection (deep genealogy with two allelic classes), after a population decline, or when a sample pools differentiated subpopulations.

$D$ is roughly but not exactly standard normal; its null distribution is usually obtained by coalescent simulation (Algorithm 7.4.1), conditioning on $S$ or on $\theta$.

**Example 8.2.1** Ten sequences have $S = 16$ segregating sites and a mean of $\hat\theta_\pi = 3.2$ pairwise differences. Then $a_1 = 2.829$, $S/a_1 = 5.66$, and Eq. (8.2) gives $D = (3.2 - 5.66)/1.22 = -2.01$: there are too many singletons and low-frequency variants for neutral equilibrium. For $n = 10$ this value lies in the lower tail of the null distribution, significant at about the $5\,\%$ level; whether it reflects selection or demography cannot be decided from this locus alone.

Other statistics weight the spectrum differently. Fu and Li's $D$ compares the number of mutations on external branches of the genealogy (singletons, $\eta_{\mathrm{e}}$) with the total, on the argument that slightly deleterious mutations are young and sit on external branches. Fay and Wu's $H = \hat\theta_\pi - \hat\theta_H$, with $\hat\theta_H = \sum_ii^2\xi_i/\binom{n}{2}$, compares intermediate with high-frequency derived alleles; it needs an outgroup to identify the derived state. A significantly negative $H$, an excess of derived alleles at high frequency, is a distinctive signature of hitchhiking: neutral alleles that happened to lie on the chromosome carrying a beneficial mutation are carried to high frequency with it, while recombination near the end of a sweep keeps a few lineages with the ancestral allele.

Before DNA sequencing, electrophoretic data allowed a related test based on the Ewens sampling formula (§7.3.3 of [7.10.7](/7.10.7#sec-7.3)). In a sample of 21 genes of xanthine dehydrogenase of *Drosophila persimilis*, ten alleles were found, one in 12 copies and nine in single copies, the most extreme configuration possible: under the neutral infinite-alleles model its probability is only $0.00012$.

### 8.2.2. Demography as a Confounder

Population history changes the spectrum in the same direction as selection. Exponential growth and the recovery from a bottleneck produce star-like genealogies and negative $D$; a decline or population structure produces positive $D$ ([7.10.7](/7.10.7#sec-7.5)). Human mitochondrial DNA has an excess of rare variants, which has been attributed to population expansion after the dispersal out of Africa but could equally reflect the spread of an advantageous mitochondrial variant, since the whole mitochondrial genome is a single locus. The way out is that demography affects the whole genome while selection acts on particular regions. Tests are therefore applied as genome-wide comparisons: a locus is a candidate when it is extreme relative to the distribution over the genome, or relative to simulations under a demographic model fitted to genome-wide data. Comparisons of classes of sites within the same genomic region help too: in human populations, nonsynonymous variants are rarer than synonymous ones, and radical amino acid changes rarer than conservative ones; since all classes share the same history, their differences must reflect selection.

![Tajima's D under different histories (coalescent simulations, Algorithm 7.4.1 with Eq. (7.10); n = 20 sequences, θ = 10 per locus, 5000 loci per history). Constant size: D is centered near 0 (its null distribution, slightly skewed). Exponential growth (rate 10 per 2N₀ generations backward): D is shifted strongly negative at every locus, as it would be after a sweep at one locus. A recent decline (the population ten times larger before 0.1 time units ago): D is shifted positive, as under balancing selection. Because demography shifts the whole genomic distribution while selection affects particular loci, candidates for selection are loci in the tails of the genome-wide distribution](./plots/tajima.py)

### 8.2.3. Combining Polymorphism and Divergence

Under neutrality, polymorphism within species and divergence between them are two phases of the same process ([7.10.6](/7.10.6#sec-6.6)), and both are proportional to the neutral mutation rate: polymorphism is about $4N_{\mathrm{e}}\mu$ (Theorem 7.3.1), divergence $2\mu t$.

**Definition 8.2.3 (HKA Test)** The **Hudson–Kreitman–Aguadé test** (HKA test; Hudson, Kreitman and Aguadé 1987) tests whether the ratio of polymorphism to divergence is the same at several unlinked loci, as the neutral theory predicts whatever their mutation rates. With $L$ loci, segregating sites $S_i^A$ and $S_i^B$ in two species and divergence $D_i$ between them, the expectations under the neutral model are fitted with $L + 2$ parameters ($\theta_i$ for each locus, the ratio of the population sizes and the divergence time), and the goodness of fit of the $3L$ observations is compared with a $\chi^2$ distribution with $2L - 2$ degrees of freedom.

A locus with too much polymorphism for its divergence suggests balancing selection; one with too little suggests a recent sweep or background selection.

**Definition 8.2.4 (McDonald–Kreitman Test)** The **McDonald–Kreitman test** (MK test; McDonald and Kreitman 1991) compares, within one gene, the ratio of nonsynonymous to synonymous changes among fixed differences between species ($D_{\mathrm{N}}$, $D_{\mathrm{S}}$) and among polymorphisms within species ($P_{\mathrm{N}}$, $P_{\mathrm{S}}$). Under neutrality, with synonymous changes neutral, $D_{\mathrm{N}}/D_{\mathrm{S}} = P_{\mathrm{N}}/P_{\mathrm{S}}$ in expectation; independence in the $2 \times 2$ **contingency table** is tested with **Fisher's exact test** or a $G$ test. The neutrality index is $\mathrm{NI} = (P_{\mathrm{N}}/P_{\mathrm{S}})/(D_{\mathrm{N}}/D_{\mathrm{S}})$, and the proportion of nonsynonymous substitutions fixed by positive selection is estimated as

$$
\alpha = 1 - \frac{D_{\mathrm{S}}P_{\mathrm{N}}}{D_{\mathrm{N}}P_{\mathrm{S}}} = 1 - \mathrm{NI}. \tag{8.3}
$$

The logic is that strongly deleterious nonsynonymous mutations contribute neither to polymorphism nor to divergence, neutral ones contribute equally to both, and advantageous ones are fixed quickly and contribute to divergence almost only. An excess of nonsynonymous divergence is therefore positive selection; an excess of nonsynonymous polymorphism indicates slightly deleterious variants, which segregate but are rarely fixed.

**Example 8.2.2 (*Adh* in *Drosophila*)** McDonald and Kreitman sequenced the alcohol dehydrogenase gene *Adh* in *D. melanogaster*, *D. simulans* and *D. yakuba*:

| | fixed | polymorphic |
|---|---|---|
| nonsynonymous | $D_{\mathrm{N}} = 7$ | $P_{\mathrm{N}} = 2$ |
| synonymous | $D_{\mathrm{S}} = 17$ | $P_{\mathrm{S}} = 42$ |

The ratio of nonsynonymous to synonymous changes is $7/17 = 0.41$ among fixed differences and $2/42 = 0.05$ among polymorphisms; a $G$ test gives $P < 0.006$, and Fisher's exact test $P = 0.007$. If both kinds of change were neutral, $D_{\mathrm{S}}P_{\mathrm{N}}/P_{\mathrm{S}} = 17 \cdot 2/42 = 0.81$ nonsynonymous fixed differences would be expected; the excess $7 - 0.81 = 6.2$, or $\alpha = 1 - 0.116 = 0.88$, is attributed to positive selection.

Applied across many genes, the MK framework estimates the fraction of adaptive substitutions genome-wide. Estimates are high in species with large populations: about $45\,\%$ of amino acid differences between *D. simulans* and *D. yakuba*, which with about 13 600 genes and 44 differences per gene implies some 270 000 adaptive substitutions in about 6 million years of divergence ([7.10.5](/7.10.5#sec-5.8)), and about half in enteric bacteria. Estimates for primates are lower and vary between studies and methods, from about $35\,\%$ to $15\,\%$ or less; one study of 3377 human–chimpanzee orthologs found significant positive selection in about $9\,\%$ of genes, often transcription factors and hormone receptors, and purifying or balancing selection in others. The estimates must be corrected for two biases. Slightly deleterious nonsynonymous polymorphisms inflate $P_{\mathrm{N}}$ and bias $\alpha$ downward, which is usually handled by excluding low-frequency polymorphisms or by modeling the distribution of fitness effects from the frequency spectrum (Poisson random field models, Sawyer and Hartl 1992). Conversely, a population that was smaller in the past fixed slightly deleterious substitutions that are now removed, which inflates $D_{\mathrm{N}}$ and mimics adaptation. The excess of nonsynonymous polymorphism in mammalian mitochondrial genes is an example of the first effect.

![The McDonald–Kreitman test. A: the Adh data of McDonald and Kreitman (1991), from Yang (2014), Table 11.1 and Barton et al. (2007), Box 19.1: proportions of nonsynonymous changes among fixed differences (7 of 24) and among polymorphisms (2 of 44), with the expected number of nonsynonymous fixed differences under neutrality (0.81 of 24, dashed). B: expected outcome of the test under a nearly neutral model, computed from diffusion theory: synonymous sites neutral; nonsynonymous mutations 70 % strongly deleterious, 20 % weakly deleterious (4N_e s = −5) and 10 % neutral, with adaptive substitutions making up a true α = 0.3 of nonsynonymous divergence. The estimate α̂ = 1 − NI using all polymorphisms with derived frequency above a cutoff c is strongly biased downward by the weakly deleterious polymorphisms, which are mostly rare; excluding low-frequency polymorphisms reduces but does not remove the bias](./plots/mk.py)

## 8.3. Selection at Linked Sites

### 8.3.1. Hard and Soft Sweeps

A beneficial mutation that sweeps to fixation removes variation around it, over a region of size about $s/\ln(2N)$ in recombination units (Formula 5.4.2 of [7.10.5](/7.10.5#sec-5.4.2)). Seen from the genealogy, it causes a burst of coalescence at the time of the sweep at linked sites ([7.10.7](/7.10.7#sec-7.8)).

**Definition 8.3.1 (Hard and Soft Sweeps)** A **hard sweep** is a selective sweep in which a single copy of the beneficial allele, on a single haplotype, rises to fixation. A **soft sweep** is a selective sweep in which several copies of the beneficial allele on different haplotypes rise together, because selection acts on standing genetic variation or because the beneficial mutation arose recurrently during the sweep.

Recurrent mutation produces soft sweeps when the population-scaled rate of the beneficial mutation, $\theta_{\mathrm{b}} = 4N_{\mathrm{e}}\mu_{\mathrm{b}}$, is not small compared with one, so they are expected in large populations (insecticide resistance in *Drosophila*, drug resistance in HIV and malaria parasites, [7.10.34](/7.10.34)). Standing variation produces them when the allele has recombined onto several backgrounds before it became beneficial.

The signatures of a hard sweep, in order of how long they persist:

1. haplotype structure: carriers of the selected allele share an extended haplotype, a signal that decays after fixation within a small fraction of $N_{\mathrm{e}}$ generations; it is measured by **extended haplotype homozygosity** and the **integrated haplotype score** ([Definition 13.6.1](/7.8.13#def-13.6.1), [Formula 13.6.2](/7.8.13#fml-13.6.2)), which are most powerful while the sweep is incomplete;
2. the frequency spectrum: around the selected site, an excess of high-frequency derived alleles (negative Fay and Wu's $H$) during and just after the sweep, then an excess of rare variants (negative Tajima's $D$) as new mutations accumulate on the star-like genealogy;
3. reduced diversity: a valley of $\pi$ around the selected site, which recovers as new mutations arise, over about $N_{\mathrm{e}}$ generations.

The Duffy blood group gives a clear human case. The *FY\*O* allele, fixed in sub-Saharan Africa and rare in Europe and Asia, differs from the ancestral allele by a single noncoding base that prevents expression of the Duffy chemokine receptor on red blood cells; homozygotes are resistant to the malaria parasite *Plasmodium vivax*, which needs the receptor to invade. As expected of an allele established by a single mutation, variation in West Africans is markedly reduced over about 20 kb around it. Lactase persistence in Europeans ([Example 23.8.1](/7.4.23#ex-23.8.1)) is a hard sweep within Europe, while the independent persistence alleles of pastoral populations of East Africa and the Middle East make the adaptation, at the level of the species, a soft sweep from recurrent mutation.

In a soft sweep the selected allele is on several haplotypes, each of which hitchhikes, so diversity is reduced much less, the frequency spectrum is less distorted, and several distinct extended haplotypes carry the allele: the signature is harder to detect and needs haplotype-based statistics designed for it.

![Hard and soft sweeps (forward Wright–Fisher simulations with recombination; 2N = 2000 haplotypes, s = 0.05, recombination 10⁻⁸ per bp per generation, neutral sites initially at linkage equilibrium, mean of 30 completed sweeps). The diversity at neutral sites after fixation, relative to an unlinked site, against distance from the selected site. Hard sweep: the beneficial allele starts on one haplotype (solid line: Eq. (5.8)). Soft sweeps: selection starts on 20 or 100 copies already present on different haplotypes, as for selection on standing variation; the valley becomes much shallower as the number of founding haplotypes grows (the simulated hard sweep lies somewhat below Eq. (5.8), because sweeps that succeed start faster than the deterministic trajectory)](./plots/sweeps.py)

### 8.3.2. Background Selection

Purifying selection also affects linked neutral variation. A chromosome that carries a deleterious mutation is destined to be removed; the neutral variants on it are removed with it.

**Definition 8.3.2 (Background Selection)** **Background selection** is the reduction of neutral genetic diversity at sites linked to loci under purifying selection, caused by the removal of chromosomes carrying deleterious mutations. Together with selective sweeps it forms **linked selection**, the effects of selection on variation at linked neutral sites.

**Formula 8.3.1 (Background Selection)** Without recombination, if deleterious mutations arise on a chromosome at rate $u$ per generation and each reduces the fitness of its heterozygous carrier by $hs$ multiplicatively, the effective size of a linked neutral site is reduced to

$$
N_{\mathrm{e}} = BN, \qquad B = \mathrm{e}^{-u/(hs)}. \tag{8.4}
$$

With recombination, for a neutral site at recombination fraction $r_j$ from selected sites $j$ with mutation rates $u_j$,

$$
B \approx \exp\Bigl(-\sum_j\frac{u_jhs}{(hs + r_j)^2}\Bigr) \tag{8.5}
$$

(Hudson and Kaplan 1995; Nordborg, Charlesworth and Charlesworth 1996), which reduces to Eq. (8.4) when all $r_j = 0$.

**Proof** (of Eq. (8.4)) Without recombination, the number of deleterious mutations on a chromosome at mutation–selection balance is Poisson with mean $u/(hs)$: each generation adds $u$ new ones on average, and each is removed at rate $hs$, so the mean $m$ satisfies $m = m(1 - hs) + u$, and the Poisson form is preserved by Poisson mutation and multiplicative selection (Haigh 1978). The fraction of chromosomes free of deleterious mutations is $\mathrm{e}^{-u/(hs)}$. In the long run, all chromosomes descend from this least-loaded class, because every other chromosome carries mutations that will be removed; so the genealogy of a linked neutral site is that of a population of size $BN$. $\square$

The effect is strongest where recombination is rare and genes are dense. In *D. melanogaster*, synonymous diversity is greatly reduced near centromeres and telomeres and on the tiny fourth chromosome, where crossing over is rare, and correlates positively with the local recombination rate, while divergence from *D. simulans* does not; so the correlation is not caused by recombination being mutagenic, but by linked selection, and models of background selection with plausible mutation rates fit much of the pattern. Sweeps and background selection make similar predictions for diversity and their relative contributions are still debated. In self-fertilizing species, effective recombination is low because individuals are homozygous, and linked selection is correspondingly strong: in wild tomatoes, self-compatible species are much less diverse than self-incompatible ones. Linked selection is one explanation of **Lewontin's paradox** ([Definition 6.4.1](/7.10.6#def-6.4.1)): because selection is more efficient in large populations, it removes more diversity there.

![Background selection along a chromosome (Eq. (8.5)). A: recombination rate along a hypothetical chromosome of 30 Mb (cM per Mb), low near the centromere at 15 Mb and near the telomeres. B: the predicted reduction B of neutral diversity along the chromosome, for deleterious mutations with heterozygous effect hs = 0.02 at rate u = 2 × 10⁻⁹ per bp per generation (solid) or twice that (dashed), integrated over all linked sites with the map distance as recombination fraction. Diversity is lowest where recombination is low, the pattern seen on *Drosophila* chromosomes; divergence, which does not depend on N_e, would be uniform](./plots/background.py)

### 8.3.3. Balancing Selection at Linked Sites

Balancing selection has the opposite effect. When alleles are maintained for a long time, the sequences associated with each allele accumulate neutral differences, and linked diversity is increased in a narrow region around the selected site; the frequency spectrum has an excess of intermediate frequencies (positive Tajima's $D$), and polymorphism is high relative to divergence (HKA). At the self-incompatibility loci of plants ([7.10.5](/7.10.5#sec-5.5.2)), alleles persist longer than species: in Solanaceae, alleles of different genera can be more similar than alleles of the same species. In the cabbage and turnip, *Brassica oleracea* and *B. rapa*, different alleles of the pollen protein SP11 and the stigma receptor kinase SRK within one species share less than $50\,\%$ amino acid identity, yet four pairs of alleles from the two species, which have been separated for 2–3 million years, are remarkably similar. The major histocompatibility complex of vertebrates shows the same trans-species polymorphism. The region of elevated diversity is narrow, because even a low rate of recombination between the selected site and a neutral site homogenizes the allelic classes over long times. Balanced polymorphisms that are young or fluctuate in frequency, such as many inversion polymorphisms of *Drosophila*, instead show reduced diversity, because each arrangement arose recently from a single chromosome.

## 8.4. Genome Scans and Local Adaptation

**Definition 8.4.1 (Genome Scan)** A **genome scan** is a search for regions under selection by computing a statistic (diversity, a frequency-spectrum or haplotype statistic, differentiation between populations) in windows or at individual variants across the genome, and identifying the outliers relative to the genome-wide distribution or to a neutral demographic model.

**Definition 8.4.2 (Local Adaptation)** **Local adaptation** is the higher fitness of genotypes in the environment of their own population than in that of other populations, produced by divergent selection among populations; in reciprocal transplant experiments, local genotypes outperform foreign ones in each environment.

Divergent selection raises differentiation at the selected loci above the level that drift and migration produce for the rest of the genome, so outliers of $F_{\mathrm{ST}}$ are candidates for local adaptation (Lewontin and Krakauer 1973); the estimator of $F_{\mathrm{ST}}$ from samples, which must allow for sampling error, is [Formula 13.6.1](/7.8.13#fml-13.6.1). The Tibetan Plateau provides a striking example. Many Tibetans live above $4000\,\mathrm{m}$, where the partial pressure of oxygen is less than two thirds of its sea-level value. Comparing about 20 000 genes between Tibetans and Han Chinese, allele frequencies were strongly correlated at almost all SNPs, but two SNPs in *EPAS1*, a hypoxia-inducible transcription factor gene expressed in lung and placenta and involved in the regulation of red blood cell production, had alleles at about $90\,\%$ in Tibetans and $10\,\%$ in Han; the allele is also rare in Europeans, so the change happened in the Tibetan lineage. The original study estimated the split of the two populations at about 2750 years ago, which would imply very strong selection, although human presence on the plateau is much older; the haplotype carrying the allele was later found to have been introduced from Denisovans ([7.4.14](/7.4.14#sec-14.6)). The population branch statistic used in such studies combines pairwise $F_{\mathrm{ST}}$ among three populations to locate the change on one branch.

Scans share two difficulties. Demography (bottlenecks, expansions, admixture, structure with isolation by distance) produces long tails of the null distribution, so outliers are only candidates; and the statistics are correlated along the genome and between methods. A candidate becomes credible when several independent signals agree, when it is extreme relative to simulations under a fitted demographic model, and when a functional variant and a selective agent can be identified ([7.8.13](/7.8.13#sec-13.6.2)).

![An F_ST genome scan (simulated). Allele frequencies of 5000 SNPs in two populations derived from a common ancestral frequency under the Balding–Nichols model with F_ST = 0.05 (frequencies drawn from beta distributions around the ancestral frequency), samples of 100 chromosomes per population, and Hudson's estimator of F_ST per SNP (the estimator of 7.8.13); five loci under divergent selection have ancestral-to-population divergence equivalent to F_ST = 0.5, and the neighboring SNPs within 5 positions share part of the signal. A: F_ST along the "genome"; dashed: the 99.9th percentile of the neutral SNPs. B: the distribution of F_ST for neutral SNPs and the selected regions; the neutral tail is long, so single-SNP outliers are only candidates](./plots/fst-scan.py)

## 8.5. Measuring Selection Directly and Through Time

Indirect tests detect the cumulative effects of selection; direct measurement estimates selection coefficients. It is difficult for two reasons: fitness differences of a few percent require large samples, and a fitness difference between genotypes must be attributed to the variant itself rather than to linked variants.

In microorganisms, two strains competing in a common culture change their frequency ratio as $\mathrm{e}^{st}$ when their growth rates differ by $s$, so $s$ is the slope of the log ratio against time. A yeast mutant whose ratio to the wild type declined from $1.27$ to $0.69$ over 150 generations has $s = \ln(0.69/1.27)/150 = -0.004$; such experiments resolve differences down to about $0.5\,\%$ per generation. Genome-wide deletion collections of yeast measured this way show that only about $19\,\%$ of genes are essential for growth on rich medium, and that a minority of viable deletions grow detectably slower, although more sensitive competition assays reveal small fitness effects for most. In multicellular organisms selection coefficients are rarely measured to better than a few percent. Convincing cases connect the fitness effect to the function of the gene: the *Adh* alleles of *D. melanogaster*, where the $F$ allele with higher enzyme activity increases in laboratory populations given ethanol and becomes more frequent with latitude on several continents, while closely linked variants show no cline.

Allele frequencies measured repeatedly through time give a more direct handle. The change of frequency between samples is a combination of selection and drift, and both are captured by the Wright–Fisher Markov chain of [7.10.6](/7.10.6#sec-6.2): the likelihood of a series of sample frequencies is computed by a hidden Markov model in which the hidden state is the population frequency, the transition is the Wright–Fisher step with selection, and the emission is binomial sampling. Maximizing over $s$ (and $N_{\mathrm{e}}$) estimates selection from time series of experimental evolution, of the peppered moth ([Example 23.3.4](/7.4.23#ex-23.3.4)), of viruses during epidemics and, with ancient DNA, of human populations over the last ten thousand years, where samples have shown directly that the lactase persistence allele rose in frequency only in the last few thousand years ([Example 23.8.1](/7.4.23#ex-23.8.1)).

![Estimating selection from a time series. A: one simulated Wright–Fisher population of N = 100 diploids with s = 0.05 per copy (true frequency, line), sampled every 10 generations with 40 chromosomes per sample (dots, with binomial 95 % intervals). B: the log likelihood of the samples as a function of s, computed by the forward algorithm of a hidden Markov model whose hidden states are the 201 possible numbers of copies, with Wright–Fisher transitions including selection and binomial sampling emissions; the maximum-likelihood estimate (dotted) and the approximate 95 % interval (log likelihood within 1.92 of the maximum, shaded) contain the true value (solid)](./plots/timeseries.py)

## 8.6. Selection on Noncoding DNA and the Extent of Selection

Most of the genomes of animals and plants is noncoding, and much of their functional evolution, especially in gene regulation, is thought to be in noncoding sequence. Detecting selection there is harder than in coding regions: there is no natural internal benchmark like synonymous sites, insertions and deletions make alignment difficult, and the function of a sequence is usually unknown. The main approach is comparative. Sequence conserved across distantly related species, evolving more slowly than a neutral reference such as ancestral transposable elements, is under purifying selection (**phylogenetic footprinting**, [7.8.8](/7.8.8#sec-8.6.1)); comparisons of many mammalian genomes suggest that roughly 5–10 % of the human genome is under such constraint, most of it noncoding. Conversely, conserved elements that evolved unusually fast in one lineage, such as the human accelerated regions, are candidates for lineage-specific adaptation. Within RNA molecules, selection for base pairing leaves compensatory changes: when one base of a paired stem changes, the change of its partner restores pairing, and the two changes are correlated across species, the basis of comparative RNA structure prediction (covariation, [7.8.5](/7.8.5)).

How much of the genome is affected by selection? Several lines of evidence now converge:

- purifying selection constrains a minority of the human genome directly, but the fraction is larger in species with compact genomes, such as *Drosophila*;
- in species with large populations, a large fraction of amino acid substitutions is adaptive (§8.2.3), and linked selection reduces diversity over much of the genome (§8.3.2);
- in humans and other species with small $N_{\mathrm{e}}$, a smaller fraction of substitutions is adaptive, many slightly deleterious mutations segregate and some are fixed ([7.10.6](/7.10.6#sec-6.5)), and clear hard sweeps are relatively few;
- the load arguments of Haldane ([7.10.5](/7.10.5#sec-5.8)) do not forbid these levels of selection, because selection on many loci at once can act like truncation selection.

The neutral theory thus survives as the null model and as a good description of most noncoding DNA, while selection, direct and linked, shapes a substantial part of molecular variation, more so in species with large populations.

## Summary

| Approach | Statistic | Detects | Confounded by |
|---|---|---|---|
| divergence | $\omega = d_{\mathrm{N}}/d_{\mathrm{S}}$ (Definition 8.1.2); selective constraint (Definition 8.1.3) | recurrent positive selection ($\omega > 1$), purifying selection | averaging over sites and time (conservative) |
| codon usage | preferred : unpreferred $= (v/u)\mathrm{e}^{4N_{\mathrm{e}}s}$ (Eq. (8.1)) | weak selection on synonymous sites | mutation bias, base composition |
| frequency spectrum | Tajima's $D$ (Eq. (8.2)), Fu and Li's $D$, Fay and Wu's $H$ | sweeps ($D < 0$, $H < 0$), balancing selection ($D > 0$) | demography, structure |
| polymorphism vs divergence | HKA (Definition 8.2.3); MK, $\alpha = 1 - \mathrm{NI}$ (Definition 8.2.4, Eq. (8.3)) | positive selection, balancing selection, sweeps | slightly deleterious variants, past changes of $N_{\mathrm{e}}$ |
| linked selection | diversity valleys, haplotypes; $B = \mathrm{e}^{-u/hs}$ and Eq. (8.5) | hard and soft sweeps (Definition 8.3.1), background selection (Definition 8.3.2) | low recombination, demography |
| genome scans | $F_{\mathrm{ST}}$ outliers, EHH, iHS (Definition 8.4.1) | local adaptation (Definition 8.4.2), recent sweeps | demographic tails |
| direct and temporal | competition slopes, Wright–Fisher HMM likelihood | the selection coefficient itself | linked variants, environmental fluctuation |

## Questions

1. A gene has $\omega = 0.15$ between two species. Can it have experienced positive selection? What data would reveal it?

   **Answer** Yes. A whole-gene ratio averages over all codons and the whole divergence time; strong purifying selection on most codons can hide a few codons, or a short episode on one lineage, with $\omega > 1$. Sequences from several species analyzed with codon models in which $\omega$ varies among sites or among branches ([7.10.23](/7.10.23)), or polymorphism data for an MK test, which compares nonsynonymous and synonymous changes within and between species, can reveal it.

2. Compute Tajima's $D$ for $n = 10$ sequences with $S = 16$ and $\hat\theta_\pi = 8.0$. Which processes could explain the result?

   **Answer** With $a_1 = 2.829$, $S/a_1 = 5.66$. For $n = 10$ the constants of Eq. (8.2) are $a_2 = 1.540$, $b_1 = 0.407$, $b_2 = 0.279$, $c_1 = 0.0539$, $c_2 = 0.0472$, so $e_1 = 0.0191$ and $e_2 = 0.00495$; the denominator is $\sqrt{0.0191 \cdot 16 + 0.00495 \cdot 240} = \sqrt{0.305 + 1.188} = 1.22$ and $D = (8.0 - 5.66)/1.22 = 1.92$. A positive $D$ indicates an excess of intermediate-frequency variants: balancing selection, a population decline, or a sample drawn from structured subpopulations. A value of $1.92$ is near the upper tail but not clearly significant for one locus.

3. In an MK table, $D_{\mathrm{N}} = 20$, $D_{\mathrm{S}} = 40$, $P_{\mathrm{N}} = 30$, $P_{\mathrm{S}} = 50$. Compute NI and $\alpha$ and interpret them. Why might $\alpha$ be underestimated?

   **Answer** $\mathrm{NI} = (30/50)/(20/40) = 1.2$ and $\alpha = -0.2$. There is an excess of nonsynonymous polymorphism, not of divergence: many nonsynonymous variants are slightly deleterious, segregating but rarely fixed. Because these inflate $P_{\mathrm{N}}$, they mask any adaptive divergence; excluding low-frequency polymorphisms or modeling the distribution of fitness effects would give a higher (possibly positive) estimate of $\alpha$.

4. Why does a hard sweep produce negative Fay and Wu's $H$, and why does this signal fade faster than the reduction of diversity?

   **Answer** Neutral alleles on the chromosome on which the beneficial mutation arose are carried to high frequency; lineages that recombine away near the end of the sweep keep the alternative alleles, at low frequency, so at linked sites derived alleles are in excess at high frequency. After fixation, drift soon removes these few remaining low-frequency lineages, after which the sites are monomorphic and no longer contribute to $H$; the diversity valley, by contrast, is refilled only by new mutations, which takes of the order of $N_{\mathrm{e}}$ generations or more.

5. Using Eq. (8.4), what fraction of neutral diversity is left in a nonrecombining region in which deleterious mutations arise at $u = 0.1$ per chromosome per generation with $hs = 0.02$? What changes if the region recombines?

   **Answer** $B = \mathrm{e}^{-0.1/0.02} = \mathrm{e}^{-5} = 0.0067$: less than $1\,\%$ of the neutral diversity expected from $N$ remains, as on the nonrecombining Y chromosome or in asexual genomes. With recombination, each selected site contributes $u_jhs/(hs + r_j)^2$ instead of $u_j/(hs)$ (Eq. (8.5)), so sites farther than about $hs$ in recombination fraction contribute little, and $B$ is much closer to 1.
