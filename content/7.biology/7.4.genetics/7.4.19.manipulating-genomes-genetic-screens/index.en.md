---
title: Manipulating Genomes and Genetic Screens
description: "Genome manipulation as a genetic method. Transgenic organisms (pronuclear injection, extrachromosomal arrays, P-element and phiC31 transformation, Agrobacterium T-DNA) and the segregation of transgenes; binary expression systems (GAL4/UAS, enhancer traps, Tet-On/Off); transgene rescue and other uses; gene targeting in embryonic stem cells, chimeras and breeding schemes, conditional alleles, knock-ins, CRISPR founders and saturation genome editing; the design of forward genetic screens (mutagens, F1, F3 and maternal-effect screens, balancer chromosomes) and the Poisson theory of saturation; pooled screens in cells; transmission ratio distortion in natural selfish elements; somatic gene therapy."
---

The previous chapters used mutations that nature or a mutagen provided and asked what they reveal. Since the 1980s geneticists have also been able to do the reverse: to put a chosen DNA sequence into the genome of a model organism, to replace an endogenous gene with an allele designed in the laboratory, and to switch a gene off in chosen cells at a chosen time. These methods made **reverse genetics** ([7.4.1](/7.4.1)) routine, and they also transformed **forward genetics**: the screens that find genes by their mutant phenotypes now rest on engineered chromosomes, transgenic reporters and sequencing. The molecular tools themselves (cloning, **CRISPR–Cas9**, base and prime editing, guide-RNA libraries) belong to [7.2.5](/7.2.5) and [7.2.24](/7.2.24), and the knockout and **conditional knockout** of the mouse were defined with the methods of cell biology in [7.3.3](/7.3.3#sec-3.7.3). This chapter treats them as a geneticist uses them: which strains to build, which crosses to set up and in what proportions the wanted genotypes appear, and how large a screen must be to find most of the genes for a process. The screens of [7.4.20](/7.4.20) and the mouse models and variant assays of [7.4.21](/7.4.21) apply what is collected here.

## 19.1. Transgenic Organisms

**Definition 19.1.1 (Transgene and Transgenic Organism)** A **transgene** is a DNA sequence introduced experimentally into the genome of an organism, from the same or another species, in a form that is replicated and transmitted to daughter cells and, if it is present in the germ line, to the offspring. An organism carrying a transgene in its germ line is a **transgenic organism**.

The method of introduction differs between organisms, and with it the genetic properties of the result: whether the transgene integrates at random or at a chosen site, in one copy or many, and whether the first generation is mosaic.

### 19.1.1. Mice: Pronuclear Injection

A fertilized mouse egg has two haploid pronuclei for several hours before they fuse. Linear DNA injected into the larger (male) pronucleus integrates, in a fraction of the eggs, at a random chromosomal site, usually as a tandem head-to-tail array of a few to a hundred copies (Gordon and Ruddle 1980; the growth-hormone mice of Palmiter and Brinster 1982). The injected eggs are transferred to pseudopregnant females and the pups tested by PCR of tail DNA. Three genetic consequences follow.

1. Each founder carries a different insertion. Expression depends on copy number and on the integration site (a **position effect**, [7.2.15](/7.2.15#sec-15.6.1)), and the insertion may disrupt a host gene (insertional mutagenesis). Conclusions must therefore hold for several independent lines.
2. Founders are often mosaic, because integration may follow the first replication; a founder may transmit the transgene to fewer than half of its offspring.
3. Thereafter the transgene segregates as a single dominant marker at its insertion site: a hemizygous transgenic mouse crossed to wild type transmits it to half of the offspring, and two hemizygotes give $1/4$ homozygous, $1/2$ hemizygous and $1/4$ nontransgenic offspring.

**Example 19.1.1** A founder male mated to wild-type females gives 6 transgenic pups out of 40. (a) A nonmosaic founder would be expected to give 20; the probability of 6 or fewer under $\mathrm{Bin}(40, 1/2)$ is about $4 \times 10^{-6}$, so he is a germline mosaic. (b) If a fraction $f$ of his germ cells carry the transgene, $f/2 = 6/40$ and $f = 0.3$. (c) His transgenic offspring are nonmosaic hemizygotes and transmit the transgene to half of their own offspring.

### 19.1.2. Nematodes, Flies and Plants

In *C. elegans*, DNA injected into the syncytial gonad forms large extrachromosomal arrays, concatemers of hundreds of plasmid copies, transmitted to some offspring and lost at random in mitosis; lines are followed with a co-injected visible marker and are mosaic. Arrays can be integrated by irradiation, and single-copy insertions at defined sites are made with transposase-mediated integration or CRISPR.

In *Drosophila*, Rubin and Spradling (1982) used the P element, a **DNA transposon** ([7.2.9](/7.2.9#sec-9.8)), as a vector: the transgene and a visible marker (originally *rosy*$^{+}$, now a mini-*white* gene that colors the eyes of a *white* host) are placed between the P-element ends, and transposase is supplied from a separate helper plasmid that cannot itself move. Because the helper is not inherited, the insertions in the offspring are stable. Insertion at a chosen site uses the bacteriophage φC31 integrase, which recombines an *attB* site on the plasmid with an *attP* landing site previously placed in the genome, so that constructs to be compared share one position and one position effect.

In plants the vector is the Ti (tumor-inducing) plasmid of *Agrobacterium tumefaciens*, a soil bacterium that transfers a segment of the plasmid, the T-DNA, into the plant nuclear genome. DNA placed between the two 25-bp border repeats is transferred by the virulence (*vir*) proteins; in the binary vectors used today the borders and the transgene lie on a small plasmid and the *vir* genes on a separate, disarmed Ti plasmid. Tissue pieces are infected and plants regenerated on selective medium, or, in *Arabidopsis*, flowering plants are dipped in a bacterial suspension and about 0.1–1 % of the seeds are transformed, each hemizygous for one or a few independent insertions.

**Formula 19.1.1 (Segregation of Independent Transgene Insertions)** If a transformed plant carries $n$ unlinked dominant selectable insertions and is self-fertilized, the fraction of progeny carrying none is $(1/4)^n$, so that resistant and sensitive seedlings appear in the ratio $3:1$ for one insertion, $15:1$ for two and $63:1$ for three. Among the resistant progeny of a single insertion, $1/3$ are homozygous, recognized because all of their own progeny are resistant.

**Example 19.1.2** A transformed plant gives 290 resistant and 22 sensitive progeny. For one insertion the expectations are 234 and 78, $\chi^2 = 13.4 + 40.2 = 53.6$ with 1 degree of freedom: rejected. For two unlinked insertions, 292.5 and 19.5, $\chi^2 = 0.02 + 0.32 = 0.34$: accepted. The plant carries two insertions, which are separated by backcrossing (the **goodness-of-fit test** of [7.4.2](/7.4.2)).

## 19.2. Controlling Where and When a Transgene Acts

A transgene expressed everywhere and always is rarely informative and often lethal. Binary systems separate the control of expression from the gene to be expressed, so that one collection of driver strains can be combined by a cross with any responder.

**Definition 19.2.1 (GAL4/UAS System)** The **GAL4/UAS system** is a two-component expression system in which one transgene (the driver) expresses the yeast transcriptional activator Gal4 under a chosen enhancer, and a second transgene (the responder) carries the gene of interest downstream of Gal4-binding upstream activating sequences (UAS); the responder is expressed only in cells of offspring that carry both transgenes and make Gal4 (Brand and Perrimon 1993).

Gal4 controls the galactose genes of yeast ([7.2.14](/7.2.14)) and has no targets in the genomes of flies, fish or plants, so it activates the UAS transgene alone. Thousands of driver lines with defined patterns exist in *Drosophila*. Many came from enhancer trapping, in which a transposon carrying *GAL4* behind a weak promoter is mobilized at random so that each insertion reports the activity of nearby **enhancers** ([7.4.17](/7.4.17)); others carry cloned enhancer fragments. Crossing a driver to a responder expresses a reporter (*UAS-GFP*) to see the pattern, a cDNA to test the effect of expression in the wrong place, or a hairpin RNA that knocks the gene down by **RNA interference** in those cells only.

Control in time is added by a further component: a temperature-sensitive allele of the Gal4 inhibitor Gal80 blocks Gal4 at 18 °C and releases it at 29 °C, so that expression begins when the flies are shifted. In mammals the analogous systems are the tetracycline-controlled transactivators (Tet-Off, in which the activator binds its operator unless doxycycline is present, and Tet-On, the reverse) and the tamoxifen-dependent recombinase CreERT2 ([7.3.3](/7.3.3#def-3.7.2)).

**Example 19.2.1** A driver on chromosome 2 kept over a balancer, $GAL4/CyO$, is crossed to a responder on chromosome 3, $UAS/TM3$. Each transgene is transmitted with probability $1/2$ independently, so $1/4$ of the offspring are $GAL4/+;\ UAS/+$ and are recognized because they are neither Curly (*CyO*) nor Stubble (*TM3*). If both stocks were homozygous for their transgene, every offspring would carry both, which is why driver and responder stocks are made homozygous where possible.

![Binary expression with GAL4/UAS, drawn in SBOL Visual symbols. The driver transgene (top) places the yeast activator gene GAL4 under a tissue-specific enhancer (E) and a minimal promoter; the responder (bottom) places the gene of interest, here GFP, behind UAS sites bound by Gal4. Neither transgene does anything on its own: the responder has no activator, and Gal4 has no target in the fly genome. In offspring of a cross between the two lines, Gal4 made where the enhancer is active binds the UAS and switches on the responder in those cells only. The temperature-sensitive inhibitor Gal80 (dashed) blocks Gal4 at low temperature and so adds control in time](./plots/gal4-uas.py)

## 19.3. What Transgenes Are Used For

A mutation mapped by recombination, or a deletion that removes several genes, leaves open which gene is responsible. The decisive test is transgene rescue: a transgene carrying the wild-type copy of one candidate, with its own regulatory sequences, is crossed into the mutant, and if the mutant phenotype disappears that gene is the one. Rescue is a **complementation test** ([7.4.4](/7.4.4#sec-4.4.2)) between a mutation and a cloned gene.

**Algorithm 19.3.1 (Identifying a Gene by Transgene Rescue)**

1. Map the mutation to a small interval (recombination, deletions, sequencing; [7.4.14](/7.4.14)) and list the candidate genes.
2. Make transgenic lines, each carrying a genomic fragment with one candidate gene and its regulatory regions; in flies, insert them all at the same landing site.
3. Cross each line into the homozygous mutant background, or into a mutation over a deletion, and score the phenotype.
4. The gene whose transgene restores the wild-type phenotype is identified. As a control, the same fragment with a frameshift or premature stop codon in that gene should not rescue.
5. Independently, inactivate the candidate in a wild-type background (a second allele, RNAi or editing) and confirm that it reproduces the phenotype.

Transgenes are also the standard reporters of gene expression: a regulatory region fused to GFP, luciferase or β-galactosidase shows where and when a gene is transcribed, and a fusion of the coding region with a fluorescent protein shows where the protein goes. Transgenic animals and plants produce human proteins (antithrombin from goat milk, the first drug approved from a transgenic animal, 2009) and model human disease. Transgenic crops are grown on about 200 million hectares: maize and cotton expressing insecticidal Cry proteins of *Bacillus thuringiensis*, several crops made tolerant to glyphosate by a bacterial EPSP synthase insensitive to the herbicide, and Golden Rice, which makes β-carotene in the endosperm. Their genetic risks are questions of population genetics: resistance alleles in pests spread under selection ([7.4.23](/7.4.23)), which refuges of non-transgenic plants slow by keeping those alleles rare and mostly heterozygous, and transgenes can move into wild relatives wherever the crop hybridizes with them.

## 19.4. Targeted Mutagenesis

### 19.4.1. Gene Targeting in Embryonic Stem Cells

A transgene inserted at random adds a gene; removing or changing an endogenous gene requires **homologous recombination** between the chromosome and an introduced DNA.

**Definition 19.4.1 (Gene Targeting and Positive–Negative Selection)** **Gene targeting** is the modification of a chosen endogenous gene by homologous recombination with an introduced DNA molecule that carries the desired change between sequences homologous to the gene. **Positive–negative selection** is the enrichment of targeted cells by a positive marker placed within the homology, so that cells which integrated the vector survive, and a negative marker outside it, so that cells in which the entire vector integrated at a random site are killed.

In mouse **embryonic stem cells** (Capecchi, Evans and Smithies, Nobel Prize 2007) homologous integration is a hundred to a thousand times rarer than random integration. A knockout vector replaces an essential exon with a neomycin-resistance gene (selected with G418) and carries the herpes simplex thymidine kinase gene beyond one homology arm; homologous recombination exchanges the arms and loses the thymidine kinase gene, whereas random integration usually keeps it, and ganciclovir, which the enzyme converts into a toxic nucleotide, kills those cells. Surviving colonies are screened by PCR or Southern blotting across the junctions ([7.3.3](/7.3.3#sec-3.7.3)).

Targeted cells, heterozygous for the knockout, are injected into blastocysts of a strain with a different coat color, and the mice that develop are chimeras.

**Definition 19.4.2 (Chimera)** A **chimera** is an organism composed of cells derived from two or more zygotes, or from a zygote and cultured cells, as distinct from a **genetic mosaic**, whose genetically different cells arise by mutation or recombination within one zygote ([7.4.9](/7.4.9#sec-9.5.3)).

Cells from an agouti strain injected into a black host give chimeras with a patchwork coat, and the agouti fraction indicates how much the injected cells contributed. If they colonized the germ line, the chimera's offspring with a black mate include agouti pups, which came from gametes derived from the targeted cells.

**Formula 19.4.1 (Breeding a Knockout)** Let a chimera transmit gametes derived from the targeted cells with probability $g$, those cells being heterozygous $+/-$. Mated to wild type, the offspring are host-derived $+/+$ with probability $1-g$, and agouti $+/+$ or agouti $+/-$ with probability $g/2$ each. Heterozygotes are then intercrossed and give $+/+$, $+/-$ and $-/-$ in the ratio $1:2:1$; if the knockout is lethal before weaning, the survivors are $+/+$ and $+/-$ in the ratio $1:2$, as for any **lethal allele** ([7.4.3](/7.4.3#sec-3.4.1)).

**Example 19.4.1** (a) A chimera with $g = 0.6$ sires a litter of 8: the expected number of heterozygous pups is $8 \times 0.3 = 2.4$, and the probability of none is $0.7^8 = 0.058$. (b) An intercross of heterozygotes gives 52 weaned pups: 18 $+/+$, 34 $+/-$ and no $-/-$, although 13 were expected. The probability of seeing no homozygote among 52 survivors if they were viable is $0.75^{52} \approx 3 \times 10^{-7}$, so the knockout is lethal; the observed $18:34$ fits the $1:2$ expected among survivors ($\chi^2 = 0.04$). Embryos are then genotyped at successive stages to find when the homozygotes die.

Many knockouts die as embryos and many others have no phenotype because a paralog compensates. Both problems are met by **conditional knockouts** ([7.3.3](/7.3.3#def-3.7.2)), in which an essential exon is flanked by *loxP* sites and **site-specific recombination** ([7.2.9](/7.2.9#sec-9.6)) by Cre removes it only where Cre is made. The floxed allele is itself normal, so the method is entirely a matter of crosses.

**Formula 19.4.2 (Breeding a Conditional Knockout)** Let $fl$ denote the floxed allele and $Cre$ a hemizygous transgene unlinked to it. The cross $fl/fl \times Cre$ gives offspring that are all $fl/+$, half of them carrying $Cre$. Crossing $fl/+;\ Cre$ back to $fl/fl$ gives four classes of equal frequency $1/4$: $fl/fl;\ Cre$ (the conditional knockout), $fl/fl$ (floxed control without Cre), $fl/+;\ Cre$ (control for the effects of Cre itself and of heterozygosity) and $fl/+$. Thereafter $fl/fl;\ Cre \times fl/fl$ gives half experimental and half control animals in every litter.

The method has genetic pitfalls of its own. A driver that is leaky in the germ line deletes the floxed exon in the gametes and transmits a null allele to all offspring, which is why $Cre$ is usually passed through the sex in which the driver is silent in germ cells. Deletion is often incomplete, so the tissue is a mosaic; its extent is measured with a Cre reporter, a floxed stop cassette in front of a fluorescent protein. Cre itself can be toxic when strongly expressed, which the $fl/+;\ Cre$ controls reveal.

### 19.4.2. Knock-Ins

**Definition 19.4.3 (Knock-In)** A **knock-in** is an allele made by gene targeting in which a sequence is inserted or substituted at a chosen endogenous locus, so that it is expressed under that gene's own regulation: a point mutation, a tag or reporter fused in frame, or a replacement of the gene by its human counterpart.

Knock-ins model disease mutations exactly (a knock-in mouse expresses human sickle hemoglobin), place reporters under endogenous control, avoiding the copy-number and position artifacts of random transgenes, and humanize genes whose products are targets of drugs. Genetically a knock-in allele behaves like any allele: heterozygotes show dominance relations, homozygotes recessive phenotypes, and compound heterozygotes with a null allele the effect of a single dose.

### 19.4.3. Editing as a Genetic Tool

With **CRISPR–Cas9** ([7.2.24](/7.2.24#sec-24.4)) targeting no longer needs cultured stem cells. Cas9 protein and a **single guide RNA** injected into a zygote cut the target; repair by **nonhomologous end joining** gives small insertions and deletions, many of them frameshifts, and a co-injected template gives precise changes by homology-directed repair in a smaller fraction of cases. Three genetic consequences follow.

1. Founders are mosaic, because cutting and repair occur after the first replication and differ between the two homologs; a founder may carry three or four alleles at the locus.
2. Each allele must be separated in the next generation: founders are crossed to wild type and the offspring genotyped by sequencing, so that each line carries one defined allele.
3. Off-target changes at similar sequences ([7.2.24](/7.2.24#sec-24.8)) are usually unlinked to the target and are removed by backcrossing, exactly as background mutations from chemical mutagenesis are.

The same tools turn the genome into an instrument for measuring the effect of variants. In saturation genome editing (Findlay and colleagues 2018), nearly all possible single-nucleotide variants in 13 exons of *BRCA1*, about 4 000 of them, were introduced into the endogenous gene of a haploid human cell line in which *BRCA1* is essential, and the change in the frequency of each variant during growth measured its effect on function. Most variants of uncertain significance seen in patients ([7.4.21](/7.4.21)) could thereby be classified, and prime-editing screens now do the same for regulatory DNA. This is reverse genetics at the scale of a forward screen.

## 19.5. Forward Genetic Screens

### 19.5.1. Screens and Selections

**Definition 19.5.1 (Genetic Screen)** A **genetic screen** is the examination of many individuals, after mutagenesis or another source of variation, in order to identify those with a defined phenotype; a **forward genetic screen** starts from the phenotype and proceeds to the gene. A screen differs from a **genetic selection** ([7.4.10](/7.4.10#def-10.1.2)), in which the conditions allow only the wanted genotypes to survive or grow, so that individuals need not be examined.

A selection finds one mutant among $10^9$ bacteria; a screen of a multicellular organism examines each individual and reaches perhaps $10^3$–$10^5$ genomes. The design of a screen is therefore arithmetic: how many genomes must be examined, in how many generations, with how much work per genome.

### 19.5.2. Mutagens

| Mutagen | Lesions | Organisms | Rate per gene per gamete |
|---|---|---|---|
| ethyl methanesulfonate (EMS) | G·C → A·T **transitions** via $O^6$-ethylguanine | *Drosophila*, *C. elegans*, *Arabidopsis* | about $10^{-3}$ (flies), $5 \times 10^{-4}$ (worms) |
| *N*-ethyl-*N*-nitrosourea (ENU) | mainly A·T substitutions | mouse, zebrafish | about $1$–$2 \times 10^{-3}$ per locus in spermatogonia |
| X-rays and γ-rays | double-strand breaks: deletions, rearrangements | flies, plants | lower, but the alleles are usually null |
| **transposons**, retroviruses | insertions | flies, zebrafish, cultured cells | $10^{-4}$–$10^{-2}$ per gene, strongly biased by insertion preference |
| T-DNA | insertions | *Arabidopsis*, rice | indexed collections covering most genes |

Chemical mutagens give point mutations, including the hypomorphic and temperature-sensitive alleles that reveal the later functions of essential genes ([7.4.12](/7.4.12#sec-12.3.1)); insertional mutagens give fewer alleles per genome but tag the gene with known sequence, so that it can be found from the flanking DNA ([7.4.17](/7.4.17)). The rates are per gene: an average fly gene is mutated by a standard EMS dose in about one sperm in a thousand, and each mutagenized genome carries a recessive lethal on roughly half of its major chromosome arms.

### 19.5.3. Screen Designs

The generation in which a phenotype can be seen depends on whether the mutation is dominant or recessive, and on whether it acts in the zygote or in the mother.

| Screen | Mutation | Generation scored | Example |
|---|---|---|---|
| F1 (dominant) | dominant, or recessive in a sensitized background | F1 of the mutagenized parent | dominant modifiers ([7.4.20](/7.4.20)), suppressors of variegation ([7.4.18](/7.4.18)) |
| F2 (selfing or haploid) | recessive | F2 of a self-fertilizing F1 | *C. elegans*, *Arabidopsis*; haploid yeast scored at once |
| F3 | recessive, zygotic | F3 from an intercross of heterozygous F2 siblings | *Drosophila*, zebrafish, mouse |
| maternal effect | recessive, acting in the mother | embryos of homozygous females | axis determination in *Drosophila* ([7.4.20](/7.4.20)) |
| clonal | recessive, lethal when ubiquitous | homozygous clones in heterozygous animals | FLP/FRT clones in the fly eye ([7.4.9](/7.4.9#sec-9.5.3)) |

In *Drosophila*, recessive screens rely on balancer chromosomes ([7.4.15](/7.4.15)): chromosomes carrying multiple inversions, which prevent the recovery of crossover products with their homolog, a dominant visible marker and a recessive lethal. A mutagenized chromosome kept opposite a balancer cannot recombine with it, so the mutagenized genome is preserved intact, and the stock maintains itself because balancer homozygotes die.

**Algorithm 19.5.1 (An F3 Screen for Recessive Mutations on a *Drosophila* Autosome)**

1. Feed males a mutagen and cross them to females carrying a balancer of chromosome 2 (*CyO*, Curly wings).
2. In the F1, each male carries one mutagenized chromosome, written $*$, over *CyO*, and each male represents a different mutagenized genome. Cross single $*/CyO$ males to balancer females, one vial per male.
3. In the F2, collect the $*/CyO$ sons and daughters of each vial, all carrying the same mutagenized chromosome, and intercross them.
4. In the F3 the zygotes are $*/*$, $*/CyO$ and $CyO/CyO$ in the ratio $1:2:1$; the balancer homozygotes die, so a third of the survivors are straight-winged $*/*$ homozygotes. Score them, or their embryos, for the phenotype of interest. If no straight-winged flies appear, the chromosome carries a recessive lethal.
5. Keep each interesting line as the balanced stock $*/CyO$, which breeds true.

![An F3 screen for recessive mutations on chromosome 2 of *Drosophila*. Mutagenized males (asterisk: a mutagenized chromosome 2) are crossed to balancer females; each F1 male carries a different mutagenized chromosome over the balancer CyO (Curly wings) and founds a separate line; F2 siblings of one line, all */CyO, are intercrossed; in the F3 the homozygotes */* are a quarter of the zygotes and a third of the survivors, since CyO/CyO dies, and are scored for the phenotype. The balancer prevents crossing over, so the mutagenized chromosome passes through the scheme unchanged](./plots/f3-screen.py)

### 19.5.4. Saturation

How many genomes must be screened to find all the genes for a process? If genes are hit independently at a low rate, the number of alleles recovered for one gene is binomial with a small success probability and hence nearly Poisson distributed ([3.1.4](/3.1.4)).

**Formula 19.5.1 (Saturation of a Screen)** Let a screen examine $N$ mutagenized genomes and let each of $G$ genes that can mutate to the phenotype be hit with probability $\mu$ per genome. The number of alleles recovered per gene is approximately $\mathrm{Poi}(\lambda)$ with $\lambda = N\mu$, so

$$
\mathbb{P}(\text{a gene is missed}) = \mathrm{e}^{-\lambda}, \qquad
\mathbb{E}[\text{genes found}] = G\,(1 - \mathrm{e}^{-\lambda}), \qquad
\mathbb{E}[\text{alleles per gene found}] = \frac{\lambda}{1 - \mathrm{e}^{-\lambda}}.
\tag{19.1}
$$

Conversely, if $n_k$ genes were found with exactly $k$ alleles, then $\mathbb{E}[n_k] = G\mathrm{e}^{-\lambda}\lambda^k/k!$, so that

$$
\hat\lambda = \frac{2 n_2}{n_1}, \qquad \hat n_0 = \frac{n_1^2}{2 n_2}
\tag{19.2}
$$

estimate the hit rate and the number of genes not yet found.

**Proof** The counts follow from the Poisson probabilities summed over the $G$ genes: $\mathbb{E}[n_1] = G\mathrm{e}^{-\lambda}\lambda$ and $\mathbb{E}[n_2] = G\mathrm{e}^{-\lambda}\lambda^2/2$, whose ratio is $\lambda/2$, and $\mathbb{E}[n_0] = G\mathrm{e}^{-\lambda} = \mathbb{E}[n_1]^2/(2\mathbb{E}[n_2])$. The mean number of alleles conditional on at least one is $\lambda/(1-\mathrm{e}^{-\lambda})$. $\square$

Equation (19.2) is the estimator Chao introduced in ecology for the number of species not yet observed. A screen is called saturated when most genes have been hit several times, $\lambda \gtrsim 3$, so that fewer than 5 % are missed. The model assumes equal mutability, which is never exact: genes differ in size, sequence and hotspots ([7.4.13](/7.4.13#sec-13.2.4)), and some cannot give the phenotype at all because their loss kills the embryo earlier or because a paralog is redundant. If the rates vary as a gamma distribution with mean $\lambda$ and shape $k$, the counts are negative binomial and the probability of missing a gene is $(1 + \lambda/k)^{-k}$, which falls far more slowly than $\mathrm{e}^{-\lambda}$: the last genes of a pathway are always the hardest, and Eq. (19.2) is a lower bound on what remains.

**Example 19.5.1** (a) With $\mu = 10^{-3}$ per gene per genome, screening $N = 3\,000$ genomes gives $\lambda = 3$, so 95 % of the genes are expected to be found, with on average $3/(1-\mathrm{e}^{-3}) = 3.16$ alleles each; 99 % requires $\lambda = \ln 100 = 4.6$, that is $N = 4\,600$. (b) A screen yields 40 genes with one allele and 25 with two. Then $\hat\lambda = 2 \times 25/40 = 1.25$ and $\hat n_0 = 40^2/50 = 32$: about 32 genes are still missing, and the fraction missed, $\mathrm{e}^{-1.25} = 0.29$, shows that the screen is far from saturated.

The Heidelberg screens of Christiane Nüsslein-Volhard and Eric Wieschaus (1980, Nobel Prize 1995) examined some 27 000 lines for zygotic mutations that disturb the larval cuticle pattern of *Drosophila* and found about 120 loci, most with several alleles, which argued that nearly all such genes had been found ([7.4.20](/7.4.20)). Zebrafish screens of the 1990s and ENU screens in the mouse followed the same arithmetic.

![The arithmetic of saturation. A: expected fraction of genes found, 1 − exp(−λ), against λ = Nμ, the mean number of alleles recovered per gene (N genomes screened, μ hits per gene per genome); dashed curves allow the mutability to vary between genes (gamma distributed with shape k = 1 or 3), for which the last genes are found far more slowly. B: a simulated screen of 120 genes with λ = 1.5: bars, the number of genes found with 1, 2, 3 … alleles; points, the Poisson expectation; the estimate of the number of genes missed from Eq. (19.2) is compared with the true number](./plots/saturation.py)

### 19.5.5. Pooled Screens in Cultured Cells

In cultured cells every gene can be targeted at once, with a library of guide RNAs or short hairpin RNAs delivered by lentiviral vectors ([7.2.24](/7.2.24#sec-24.7)). The genetics of such a **pooled screen** is sampling.

**Formula 19.5.2 (One Perturbation per Cell)** If vectors integrate at a multiplicity of infection $m$, the number per cell is approximately $\mathrm{Poi}(m)$. The fraction of cells infected is $1 - \mathrm{e}^{-m}$, and among infected cells the fraction carrying more than one vector is

$$
1 - \frac{m\,\mathrm{e}^{-m}}{1 - \mathrm{e}^{-m}}.
\tag{19.3}
$$

At $m = 0.3$, about 26 % of the cells are infected and 14 % of those carry more than one vector, so that each phenotype can be attributed to one perturbation. To keep every member of the library represented, the number of infected cells is several hundred times the library size: a library of $8 \times 10^4$ guides at 500-fold coverage needs $4 \times 10^7$ infected cells, about $1.5 \times 10^8$ cells at infection. Abundances are counted by sequencing before and after selection, compared against the overdispersed variation of read counts (a negative binomial model) and combined across the guides for each gene, methods treated with genomics in [7.8](/7.8).

**Example 19.5.2** A screen uses a library of 20 000 guides at $m = 0.25$ and requires 300 cells per guide. (a) Infected cells needed: $6 \times 10^6$. (b) Cells to infect: $6 \times 10^6/(1 - \mathrm{e}^{-0.25}) = 2.7 \times 10^7$. (c) Among infected cells, the fraction with two or more guides is $1 - 0.25\mathrm{e}^{-0.25}/(1 - \mathrm{e}^{-0.25}) = 0.12$.

## 19.6. Biased Transmission

Every scheme in this chapter assumes Mendelian segregation: a heterozygote transmits each allele to half of its offspring, and the frequencies in a population change only through selection, drift, mutation and migration ([7.4.22](/7.4.22), [7.4.23](/7.4.23)). Some natural elements break this assumption. Meiotic drivers and other selfish genetic elements ([7.4.17](/7.4.17)) are transmitted by heterozygotes to more than half of the offspring, and they can spread in a population although they reduce the fitness of their carriers.

**Formula 19.6.1 (Transmission Ratio Distortion)** Let a locus carry alleles $A$ and $B$, with $B$ at frequency $q$, and let heterozygotes transmit $B$ with probability $t > 1/2$ instead of $1/2$. With zygote fitnesses $w_{AA} = 1$, $w_{AB} = 1 - hs$ and $w_{BB} = 1 - s$, random mating gives

$$
q' = \frac{q^2 (1 - s) + 2 t\, q (1 - q)(1 - hs)}{\bar w},
\qquad \bar w = 1 - s q^2 - 2 h s\, q(1 - q).
\tag{19.4}
$$

**Proof** After selection, the three genotypes contribute $q^2(1-s)$, $2q(1-q)(1-hs)$ and $(1-q)^2$ to the gamete pool, with total $\bar w$. Homozygotes $BB$ give only $B$ gametes and heterozygotes a fraction $t$ of them, which gives the numerator. $\square$

Two consequences follow, and both are checked by the simulations of the figure. A rare distorter increases in frequency when $2t(1 - hs) > 1$, so that a strong enough transmission advantage overcomes a substantial fitness cost in heterozygotes; and when the homozygote is much less fit than the heterozygote, the two forces balance at a stable polymorphism, with $q$ settling below one. The classical example is the *t* haplotype of the mouse ([7.4.17](/7.4.17)): heterozygous males transmit it to more than 90 % of their offspring, homozygotes are sterile or die, and the haplotype persists at frequencies of 10–25 % in wild populations, which is roughly what Eq. (19.4) predicts for these values.

![Transmission ratio distortion compared with Mendelian inheritance, from Eq. (19.4). A: frequency of an allele that heterozygotes transmit with probability $t$ and that costs $s = 0.2$ of fitness in homozygotes but nothing in heterozygotes, starting from $q = 0.02$: a Mendelian allele ($t = 0.5$) with such a cost declines, whereas a transmission advantage carries the allele to fixation, the faster the larger $t$. B: the frequency reached after many generations as a function of the cost $s$, now with a cost $0.2s$ in heterozygotes as well: up to a critical cost the allele is fixed, and beyond it the two forces balance at a stable polymorphism, as for the *t* haplotype of the mouse](./plots/transmission-distortion.py)

Engineered gene drives use the same arithmetic. A CRISPR homing drive is a cassette encoding Cas9 and a guide RNA that targets the wild-type allele at the cassette's own insertion site: in the germline of a heterozygote it cuts the homologous chromosome, and repair by homologous recombination copies the cassette into the break, so that with homing efficiency $e$ the heterozygote transmits the drive with $t = (1 + e)/2$ (the homing genes of [7.4.17](/7.4.17)). In *Anopheles stephensi* a drive carrying anti-malaria effector genes was transmitted to more than 99 % of the offspring of heterozygotes (Gantz et al., 2015), and a drive disrupting the female-specific exon of *doublesex* eliminated caged populations of *Anopheles gambiae* within 7 to 11 generations (Kyrou et al., 2018). The main obstacle is resistance: when the cut is repaired by nonhomologous end joining instead, the target site is mutated, no longer cut, and a resistant allele that keeps the gene's function is favoured by selection; drives that target conserved sites or several sites at once delay it.

## 19.7. Gene Therapy

The same methods applied to human somatic cells are gene therapy: a functional gene is added, or a mutation corrected, in the cells of a patient, without any change to the germ line. Two strategies are in use. In the ex vivo strategy, the patient's hematopoietic stem cells or T lymphocytes are removed, modified in culture with a lentiviral vector or by editing, and returned; this is how adenosine deaminase deficiency, β-thalassemia and sickle cell disease are treated, and how the engineered T cells of cancer immunotherapy are made ([7.3.26](/7.3.26#sec-26.6.4), [7.15](/7.15)). In the in vivo strategy, a vector is given to the patient directly, usually an adeno-associated virus, which does not integrate and so persists mainly in cells that do not divide: this is the basis of the approved treatments for a form of inherited retinal dystrophy (2017) and for spinal muscular atrophy (2019). The first approved therapy based on editing, for sickle cell disease and β-thalassemia (2023), disrupts a regulatory element in patients' own stem cells so that fetal hemoglobin is expressed again, a deliberate use of the natural modifier that makes some carriers of sickle cell disease mildly affected ([7.4.3](/7.4.3)).

Genetically, somatic therapy changes the phenotype of one person and nothing in the next generation: the mutant allele still segregates in the family exactly as before, and the risks computed in [7.4.7](/7.4.7) are unchanged. Editing of human embryos or germ cells, which would change the alleles transmitted, is prohibited in most jurisdictions and is subject to an international moratorium; the 2018 case in which embryos were edited and children born was condemned internationally and led to a criminal conviction.

## Summary

| Topic | Key points |
|---|---|
| Transgenes (Definition 19.1.1) | mouse pronuclear injection: random multicopy insertions, mosaic founders, dominant marker thereafter; worm arrays; P element and φC31 landing sites; *Agrobacterium* T-DNA |
| Segregation (Formula 19.1.1) | $3:1$, $15:1$, $63:1$ for 1, 2, 3 unlinked insertions; $1/3$ of resistant progeny homozygous; test by $\chi^2$ |
| Binary systems (Definition 19.2.1) | GAL4/UAS: driver × responder, enhancer traps; Gal80 and Tet systems add time; independent transgenes combine in $1/4$ of offspring |
| Uses (Algorithm 19.3.1) | transgene rescue identifies the gene; reporters; protein production; transgenic crops and the population genetics of resistance and escape |
| Targeting (Definitions 19.4.1–19.4.3) | homologous recombination with positive–negative selection; chimeras and germline transmission; floxed alleles, Cre crosses and their controls; knock-ins |
| Breeding (Formulas 19.4.1, 19.4.2) | chimera × wild type: $g/2$ heterozygotes; intercross $1:2:1$, survivors $1:2$ if lethal; conditional cross gives $1/4$ experimental + three controls |
| Editing (19.4.3) | mosaic founders with several alleles, separation in F1, off-targets removed by backcrossing; saturation genome editing classifies thousands of variants |
| Screens (Definition 19.5.1, Algorithm 19.5.1) | screen vs selection; EMS, ENU, radiation, insertions; F1, F2, F3, maternal-effect and clonal designs; balancers keep mutagenized chromosomes intact |
| Saturation (Formulas 19.5.1, 19.5.2, Eqs. (19.1)–(19.3)) | $\mathrm{e}^{-\lambda}$ missed, $\lambda \gtrsim 3$ for saturation; $\hat\lambda = 2n_2/n_1$, $\hat n_0 = n_1^2/2n_2$; unequal mutability slows the tail; pooled screens: low MOI, several hundred cells per perturbation |
| Biased transmission (Formula 19.6.1, Eq. (19.4)) | $t > 1/2$ spreads an allele against selection if $2t(1-hs) > 1$; stable polymorphism when homozygotes are unfit (the *t* haplotype of the mouse) |
| Gene therapy (19.7) | ex vivo (stem cells, T cells) and in vivo (AAV) somatic therapy; the first editing therapy (2023) restores fetal hemoglobin; somatic therapy does not change transmission; germline editing prohibited |

## Questions

1. A transgenic founder mouse transmits the transgene to 7 of 32 offspring. (a) Test whether this is consistent with a nonmosaic hemizygous founder. (b) Estimate the fraction of its germ cells that carry the transgene. (c) What do you expect in the next generation?

   **Answer** (a) Expected 16 under $\mathrm{Bin}(32, 1/2)$; $\chi^2 = (7-16)^2/16 + (25-16)^2/16 = 5.06 + 5.06 = 10.1$ with 1 df, $p \approx 0.0015$: not consistent, the founder is a germline mosaic. (b) $f/2 = 7/32$, $f = 0.44$. (c) Its transgenic offspring are nonmosaic hemizygotes and transmit the transgene to half of their offspring.

2. A self-fertilized transformed plant gives 112 resistant and 44 sensitive progeny. (a) How many insertions does it carry? (b) How would you obtain a line homozygous for one insertion? (c) Why are independent insertion lines compared before a conclusion is drawn?

   **Answer** (a) One: the expectation for one insertion is $117:39$, $\chi^2 = 0.21 + 0.64 = 0.85$ (1 df, accepted); two insertions would predict $146:10$, which is excluded. (b) Grow resistant progeny individually, self them and keep the lines all of whose progeny are resistant: those parents were homozygous ($1/3$ of the resistant progeny). (c) Expression and phenotype depend on the integration site and copy number (position effects, insertional mutagenesis), which differ between lines but not between individuals of a line.

3. A $GAL4$ driver on chromosome 2 over *CyO* is crossed to a homozygous $UAS$-$RNAi$ line on chromosome 3. (a) What fraction of the offspring express the hairpin RNA in the driver's pattern? (b) Which offspring serve as controls? (c) Why is a UAS line alone usually normal?

   **Answer** (a) All offspring carry one $UAS$ transgene, and half carry $GAL4$ (the other half carry *CyO*): half of the offspring, the non-Curly ones, express it. (b) Their Curly siblings, which carry the same $UAS$ transgene without the driver; a cross of the driver to a control UAS line gives the complementary control. (c) Without Gal4 the UAS promoter is nearly silent, and the fly genome has no Gal4-like activator for it.

4. You have mapped a mutation to an interval containing four genes. Design the experiment that identifies the gene, with its controls, and state what result would be unconvincing.

   **Answer** Make four transgenic lines, each with one candidate gene and its regulatory sequences, preferably at a common landing site; cross each into the homozygous mutant (or mutant over deficiency) and score the phenotype (Algorithm 19.3.1). The gene whose transgene rescues is identified. Controls: the same fragment with a nonsense or frameshift mutation must not rescue, and an independent loss-of-function allele of the candidate must reproduce the phenotype. Rescue by a transgene strongly overexpressing the gene is unconvincing, since overexpression of a related gene can bypass the defect.

5. In a targeting experiment, $10^7$ electroporated cells give 400 G418-resistant colonies, of which 2 are correctly targeted; with ganciclovir added, 30 colonies grow, of which 2 are targeted. (a) What is the enrichment by negative selection? (b) Why does negative selection not change the number of targeted colonies? (c) Why must junctions be checked by PCR or blotting rather than by resistance alone?

   **Answer** (a) The targeted fraction rises from $2/400 = 0.5\,\%$ to $2/30 = 6.7\,\%$, a 13-fold enrichment. (b) Targeted cells lose the thymidine kinase gene, which lies outside the homology, so ganciclovir does not kill them; it kills only the random integrants that retain it. (c) Resistance shows that the positive marker is present somewhere; only a junction assay shows that it is at the intended locus with the intended structure.

6. Heterozygous knockout mice are intercrossed and give 25 $+/+$, 51 $+/-$ and 8 $-/-$ weaned pups. (a) Test against the $1:2:1$ expectation. (b) What is the most likely explanation? (c) How would you find when the missing animals die?

   **Answer** (a) With $n = 84$ the expectations are 21, 42, 21; $\chi^2 = 0.76 + 1.93 + 8.05 = 10.7$ with 2 df, $p = 0.005$: rejected, with a deficit of homozygotes. (b) Partial penetrance of lethality: about $8/21 = 38\,\%$ of homozygotes survive to weaning, the rest die earlier (perhaps modified by genetic background). (c) Genotype litters at successive stages (late gestation, birth, before weaning) and find the stage at which the homozygotes fall below a quarter; examine embryos at that stage.

7. A conditional allele is bred as $fl/+;\ Cre \times fl/fl$. (a) List the four offspring classes and their frequencies. (b) Why is $Cre$ usually transmitted by the father in many schemes? (c) Deletion in the target tissue is 70 % complete; what does that imply for the interpretation of a weak phenotype?

   **Answer** (a) $fl/fl;\ Cre$, $fl/fl$, $fl/+;\ Cre$ and $fl/+$, each $1/4$. (b) Many drivers are leaky in the female germ line, where Cre protein or transcript in the oocyte deletes the floxed allele in all offspring, converting the conditional allele into a null; transmitting $Cre$ through the sex in which the driver is silent in germ cells avoids this. (c) 30 % of the cells still carry the intact gene and can compensate, so a weak phenotype may underestimate the gene's role; deletion must be quantified with a reporter, and the result compared with a complete null where one is viable.

8. (Saturation) A screen of 5 000 mutagenized genomes finds 60 genes: 30 with one allele, 16 with two, 9 with three, 5 with four or more. (a) Estimate $\lambda$ from $n_1$ and $n_2$. (b) Estimate the number of genes still to be found. (c) How many genomes would have to be screened in total for $\lambda = 3$?

   **Answer** (a) $\hat\lambda = 2 \times 16/30 = 1.07$. (b) $\hat n_0 = 30^2/(2 \times 16) = 28$ genes. (c) $\lambda$ is proportional to $N$, so $N = 5\,000 \times 3/1.07 = 1.4 \times 10^4$ genomes.

9. In the same screen the mean number of alleles per gene found is $60$ genes carrying $30 + 32 + 27 + 5 \times 4 \approx 109$ alleles, that is 1.8 per gene. (a) Compare with the zero-truncated Poisson mean for $\hat\lambda = 1.07$. (b) What does a discrepancy suggest?

   **Answer** (a) $\lambda/(1-\mathrm{e}^{-\lambda}) = 1.07/0.657 = 1.63$, less than the observed 1.8. (b) The alleles are distributed more unevenly than the Poisson distribution allows: genes differ in mutability (size, hotspots, the number of codons whose mutation gives the phenotype), so some accumulate many alleles while others are missed; the estimate $\hat n_0$ is then a lower bound.

10. A pooled screen uses a library of 100 000 guides. (a) At 400 cells per guide, how many infected cells are needed? (b) At a multiplicity of infection of 0.3, how many cells must be infected to obtain them? (c) What fraction of the infected cells carries more than one guide, and why does it matter?

    **Answer** (a) $4 \times 10^7$ infected cells. (b) $4 \times 10^7/(1 - \mathrm{e}^{-0.3}) = 1.5 \times 10^8$ cells. (c) $1 - 0.3\mathrm{e}^{-0.3}/(1-\mathrm{e}^{-0.3}) = 0.14$; such cells carry two perturbations, so their phenotype cannot be assigned to one gene and they add noise (and spurious interactions) to the counts.

11. An allele is transmitted by heterozygotes to 80 % of the offspring and costs 30 % of fitness in homozygotes but nothing in heterozygotes. (a) Does it spread when rare? (b) Using Eq. (19.4), compute the frequency after one generation starting from $q = 0.05$. (c) What is its fate, and what would change if heterozygotes also paid a cost of 40 % ($h s = 0.4$)?

    **Answer** (a) Yes: $2t(1-hs) = 1.6 > 1$. (b) With $s = 0.3$, $h = 0$: numerator $= 0.05^2 \times 0.7 + 2 \times 0.8 \times 0.05 \times 0.95 = 0.00175 + 0.076 = 0.0778$; $\bar w = 1 - 0.3 \times 0.0025 = 0.99925$; $q' = 0.0778$, an increase from 0.05. (c) It goes to fixation (every subsequent generation increases while $q < 1$, since the transmission advantage exceeds the cost at every frequency here). With $hs = 0.4$, $2t(1-hs) = 0.96 < 1$ and the allele cannot increase when rare, so it is lost.

12. Why does somatic gene therapy of a recessive disease not change the recurrence risk in the family, and what would have to be true for a therapy to change it?

    **Answer** The treated person's germ cells are unchanged, so each parent still transmits the mutant allele with probability $1/2$ and each future child is at the same risk; a treated patient still transmits one mutant allele to every child. Only a change in the alleles present in the germ line (germline editing, or selection among embryos by preimplantation genetic diagnosis, [7.4.14](/7.4.14)) alters transmission, and germline editing is prohibited in most jurisdictions.
