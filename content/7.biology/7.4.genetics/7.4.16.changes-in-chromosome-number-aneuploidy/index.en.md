---
title: "Changes in Chromosome Number: Aneuploidy and Polyploidy"
description: Euploidy, aneuploidy and polyploidy with the notation x, n and 2n; nullisomy, monosomy and trisomy; the gametes of nondisjunction in meiosis I and II and the maternal age effect; human autosomal and sex-chromosome aneuploidies; mitotic nondisjunction, mosaics and gynandromorphs; trisomy rescue and uniparental disomy; dosage balance; segregation in trisomics and mapping with trisomics; the sterility of triploids; chromosome and chromatid segregation in autotetraploids with double reduction; allopolyploidy in wheat, Brassica and cotton; whole-genome duplication; and the uses of polyploidy and haploidy in breeding.
---

The previous chapter changed the structure of chromosomes; this one changes their number. An extra or missing chromosome changes the dose of hundreds of genes at once, and in animals such changes are almost always harmful: in humans, aneuploidy is the most common identified cause of miscarriage and of intellectual disability. Changes of whole chromosome sets, by contrast, are common and often successful in plants, and many crops are polyploid. Both kinds of change are produced by errors of chromosome segregation. The cellular mechanics of these errors, including the cohesion loss that underlies the maternal age effect, are in [7.3.21](/7.3.21#sec-21.7.5), and **nondisjunction** was defined in [7.4.6](/7.4.6), where Bridges used it to prove the **chromosome theory of inheritance**. Here we follow its genetic consequences: which gametes it produces, how they can be recognized from the alleles they carry, why some aneuploids survive, and how meiosis works in organisms with more than two sets. The genetic effects of extra chromosomes in plants make them tools for mapping, and whole-genome duplications are a major source of new genes ([7.4.14](/7.4.14)).

## 16.1. Terms

The chromosome complement of a species is described by two numbers. The basic number $x$ is the number of different chromosomes in one complete set (a monoploid set). The gametic number $n$ is the number of chromosomes in a gamete, so that a normal sporophyte or somatic cell has $2n$. In diploids $n = x$; in polyploids they differ. Bread wheat has $x = 7$ and six sets: $2n = 6x = 42$, $n = 21$. A chromosome set (a genome, in the sense of classical cytogenetics) contains one member of each of the $x$ different chromosomes, which differ in size, centromere position and gene content and together form a complete, coordinated whole: a gamete or cell that lacks any one of them is usually inviable or sterile. In the genus *Triticum*, einkorn ($2n = 2x = 14$), emmer ($2n = 4x = 28$) and bread wheat ($2n = 6x = 42$) form a polyploid series on the same basic number.

**Definition 16.1.1 (Euploidy and Aneuploidy)** A cell or organism is **euploid** if its chromosome number is an exact multiple of the basic number $x$ (monoploid $x$, diploid $2x$, triploid $3x$, tetraploid $4x$, ...), and **aneuploid** if it has gained or lost one or more individual chromosomes, so that its number is not a multiple of $x$ (aneuploidy, [7.3.21](/7.3.21#def-21.7.5)). Euploids with more than two sets are **polyploid**.

**Definition 16.1.2 (Nullisomy, Monosomy, Trisomy, Tetrasomy)** Relative to a diploid $2n$: a **nullisomic** ($2n - 2$) lacks both homologues of one chromosome, a **monosomic** ($2n - 1$) lacks one, a **trisomic** ($2n + 1$) has one extra, and a **tetrasomic** ($2n + 2$) has two extra copies of the same chromosome. A double monosomic ($2n - 1 - 1$) lacks one copy of each of two different chromosomes, and a double trisomic ($2n + 1 + 1$) has one extra copy of each of two different chromosomes. Aneuploids with fewer chromosomes than $2n$ are hypoploid, those with more hyperploid.

**Definition 16.1.3 (Monoploid, Autopolyploid, Allopolyploid)** A **monoploid** has a single chromosome set ($x$). (A haploid has the gametic number $n$ of its species; for a diploid species the two coincide, but a haploid of hexaploid wheat has $3x$.) An **autopolyploid** has more than two sets from the same species; an **allopolyploid** has sets from two or more different species, usually two complete diploid genomes in an allotetraploid (an amphidiploid).

| Condition | Chromosome complement | Example |
|---|---|---|
| monoploid | $x$ | male bees, ants and wasps; anther-culture plants of diploids; the gametophytes of plants |
| diploid | $2x$ | most animals and plants |
| triploid | $3x$ | cultivated banana (AAA, $3x = 33$), seedless watermelon |
| autotetraploid | $4x$ | potato ($4x = 48$), alfalfa, tetraploid ryegrass |
| allotetraploid | $2x_1 + 2x_2$ | durum wheat (AABB), *Brassica napus* (AACC), cotton (AADD) |
| allohexaploid | $2x_1 + 2x_2 + 2x_3$ | bread wheat (AABBDD) |
| monosomic | $2n - 1$ | 45,X (Turner syndrome) |
| trisomic | $2n + 1$ | 47,+21 (Down syndrome); the 12 primary trisomics of *Datura* |

## 16.2. Aneuploidy

### 16.2.1. Nondisjunction in Meiosis I and Meiosis II

Most aneuploid gametes arise by nondisjunction or by premature separation of sister chromatids. The two meiotic divisions give gametes of different content, and the difference can be read in the alleles that a trisomic child received from the parent in whom the error occurred.

![Nondisjunction of one chromosome pair with the two homologues of the parent distinguished by alleles near the centromere (A on the blue homologue, a on the pink one; no crossing over between the locus and the centromere). A: nondisjunction in meiosis I sends both homologues to one secondary cell, giving two disomic gametes that carry A and a (heterodisomy) and two nullisomic gametes (O). B: nondisjunction in meiosis II in one secondary cell gives one disomic gamete with two copies of the same homologue (A and A, isodisomy), one nullisomic gamete and two normal gametes. C: trisomy rescue. A trisomic zygote (A and a from the egg, b from the sperm) that loses one of the three copies at random becomes disomic again; with probability 1/3 the lost copy is the paternal one, and the zygote has two maternal copies and none from the father (uniparental disomy)](./plots/nondisjunction-gametes.py)

**Proposition 16.2.1 (Gametes from Nondisjunction)** For one pair of homologues and a locus tightly linked to the centromere, at which the parent is heterozygous $A/a$:

| Error | Gametes | Disomic gamete carries |
|---|---|---|
| none | $\frac12\,A$, $\frac12\,a$ | — |
| meiosis I nondisjunction | $\frac12\,Aa$, $\frac12\,\mathrm{O}$ | both parental homologues ($Aa$) |
| meiosis II nondisjunction (in one secondary cell) | $\frac14\,AA$ or $\frac14\,aa$, $\frac14\,\mathrm{O}$, $\frac12$ normal | two copies of one homologue |

For loci far from the centromere, crossing over in meiosis I mixes the two patterns: an MI error leaves distal loci homozygous where a crossover moved the alleles, and an MII error leaves distal loci heterozygous. Mapping the transition from heterozygosity to homozygosity along the chromosome of a trisomic child with many markers therefore locates both the error and the crossovers; this is how most human data on the origin of trisomies were obtained.

**Example 16.2.1** A child with Down syndrome has genotypes at a marker near the centromere of chromosome 21: mother $13/18$, father $15/16$, child $13/18/16$. The child carries both maternal alleles near the centromere, so the extra chromosome came from the mother by an error in meiosis I. If the child had been $13/13/16$, the error would have been in maternal meiosis II (or, less likely, in meiosis I followed by a crossover between the marker and the centromere; markers nearer the centromere decide). If the child had been $13/15/16$, the extra chromosome would have been paternal.

Such studies show that about $90\,\%$ of trisomy 21 is maternal, about three quarters of the maternal errors in meiosis I, and that the chromosomes 21 that missegregate often had no crossover or a crossover very close to the telomere or the centromere: crossover position is a risk factor, as [7.3.21](/7.3.21#sec-21.7.5) explains through the cohesion that holds bivalents together. Trisomy 18 is also mostly maternal, but with more MII errors; most 45,X results from loss of the paternal sex chromosome; and about half of 47,XXY is paternal, from failure of the X–Y crossover in **pseudoautosomal region** 1 ([7.4.6](/7.4.6)).

### 16.2.2. The Maternal Age Effect

The risk of trisomy rises steeply with the age of the mother and hardly at all with the age of the father.

![Risk of Down syndrome at birth by maternal age. A: the logistic model of Morris, Mutton and Alberman (2002), fitted to births in England and Wales, with the risk at 20, 30, 35, 40 and 45 years. B: the same on a logarithmic scale, with an approximate risk at conception obtained by assuming that about one in five trisomy 21 conceptions survives to term. The risk is roughly constant until the late twenties and then grows almost exponentially](./plots/maternal-age.py)

**Formula 16.2.1 (Maternal Age and Down Syndrome)** An empirical model of the risk of trisomy 21 at birth as a function of maternal age $t$ (in years) is

$$
p(t) = \frac{1}{1 + \exp\!\left(7.330 - \dfrac{4.211}{1 + \mathrm{e}^{-0.282(t - 37.23)}}\right)},
$$
which gives about 1 in 1 500 at $20$, 1 in 940 at $30$, 1 in 350 at $35$, 1 in 85 at $40$ and 1 in 35 at $45$.

The model is descriptive; the mechanism is the decay of cohesin in oocytes arrested for decades in prophase I, together with weak checkpoints and unstable acentrosomal spindles ([7.3.21](/7.3.21#sec-21.7.5)). Since about $80\,\%$ of trisomy 21 conceptions and nearly all other autosomal trisomies are lost in pregnancy, the risks at conception are several times higher; in women over 40 more than half of all eggs are aneuploid.

### 16.2.3. Aneuploidy in Humans

Of all recognized pregnancies, about $5\,\%$ are aneuploid, and aneuploidy accounts for about a third to half of first-trimester miscarriages, trisomy 16 being the single most common (it is never born alive). Only three autosomal trisomies are seen at birth, those of the gene-poor chromosomes 21, 18 and 13, and no autosomal monosomy.

| Karyotype | Name | Frequency at birth | Survival and main features |
|---|---|---|---|
| 47,+21 | Down syndrome | about 1 in 700 | intellectual disability, heart defects, leukemia risk; life expectancy now about 60 years |
| 47,+18 | Edwards syndrome | about 1 in 5 000 | severe malformations; most die within the first year |
| 47,+13 | Patau syndrome | about 1 in 10 000 | holoprosencephaly, cleft lip, polydactyly; most die within weeks |
| 45,X | Turner syndrome | about 1 in 2 500 females | short stature, ovarian failure; about $99\,\%$ of 45,X conceptions are lost |
| 47,XXY | Klinefelter syndrome | about 1 in 600 males | tall stature, small testes, infertility |
| 47,XXX | trisomy X | about 1 in 1 000 females | usually mild |
| 47,XYY | — | about 1 in 1 000 males | usually tall, otherwise mild |

Sex-chromosome aneuploidies are far better tolerated than autosomal ones because of **X-chromosome inactivation**: in any number of X chromosomes all but one are inactivated, as the number of **Barr bodies** shows ([7.3.17](/7.3.17#sec-17.1.3)), and the Y carries few genes. That 45,X and 47,XXY have phenotypes at all is due to genes that escape inactivation, especially those of the pseudoautosomal regions, which need two active copies; *SHOX* in PAR1 explains the short stature of Turner syndrome and the tall stature of XXY and XYY. Their infertility arises in the germline, where the inactive X is reactivated: oogonia and oocytes need two active X chromosomes, and XXY spermatogonia have one too many.

### 16.2.4. Mitotic Nondisjunction, Mosaics and Gynandromorphs

Nondisjunction or chromosome loss in a mitotic division after fertilization produces a mosaic (Definition 9.5.2) with cell lines of different karyotypes. The earlier the error, the larger the fraction of abnormal cells. About $2$–$4\,\%$ of people with Down syndrome are 46/47,+21 mosaics, usually with milder phenotypes, and many women with Turner syndrome are 45,X/46,XX mosaics. A mosaic confined to the placenta (confined placental mosaicism, in about $1$–$2\,\%$ of chorionic villus samples) can mislead prenatal diagnosis.

**Definition 16.2.1 (Gynandromorph)** A **gynandromorph** is an individual of a species with genetic sex determination that consists of male and female tissues, usually as a result of loss of a sex chromosome from one of the first nuclei of a female zygote, or of fertilization of two nuclei of a binucleate egg.

In *Drosophila*, loss of one X chromosome in the first mitotic division of an XX zygote gives a fly that is XX (female) in about half of its body and XO (male) in the other half, often split along the midline; because sex is determined cell autonomously by the number of X chromosomes ([7.4.6](/7.4.6)), the two halves show female and male structures and, if the zygote was heterozygous for X-linked markers, the XO half shows the recessive phenotypes of the remaining X. Sturtevant used the boundaries in many such flies to map the embryonic origins of adult structures: two structures that are usually of the same genotype must come from nearby cells of the blastoderm ("sturts", the first fate map).

### 16.2.5. Trisomy Rescue and Uniparental Disomy

A trisomic zygote can return to disomy by losing one of the three copies in an early mitosis. If the loss is random, the remaining two copies include one from each parent with probability $2/3$; with probability $1/3$ the lost copy is the one from the parent who contributed only one, and the cell now has two copies from the same parent.

**Definition 16.2.2 (Uniparental Disomy)** **Uniparental disomy** (UPD) is the presence in a diploid cell of two copies of a chromosome, or of part of one, from the same parent and none from the other. In **heterodisomy** the two copies are the two different homologues of that parent; in **isodisomy** they are two copies of the same homologue. UPD most often results from **trisomy rescue**, the loss of one chromosome from a trisomic zygote or embryo, and less often from monosomy rescue (duplication of the single chromosome of a monosomic, which always gives isodisomy), from gamete complementation, or (for segments) from mitotic recombination (Definition 9.5.1).

The type of UPD records the type of meiotic error: a meiosis I error followed by rescue gives heterodisomy near the centromere, a meiosis II error isodisomy, and crossovers make the pattern change along the chromosome (Proposition 16.2.1). UPD has two kinds of consequences:

1. Isodisomy makes every locus of the chromosome (or of the isodisomic segments) homozygous, so a child can have a recessive disease for which only one parent is a carrier. The first UPD was found this way (Spence and colleagues, 1988): a child with cystic fibrosis and short stature had two copies of one maternal chromosome 7 and no paternal 7, although only the mother carried a *CFTR* mutation.
2. For chromosomes with imprinted genes, UPD removes the contribution of one parent and doubles that of the other ([7.4.18](/7.4.18)): maternal UPD 15 causes Prader–Willi syndrome and paternal UPD 15 Angelman syndrome; maternal UPD 7 causes about a tenth of Silver–Russell syndrome; paternal UPD of 11p15 (usually segmental, by mitotic recombination) causes Beckwith–Wiedemann syndrome.

**Example 16.2.2** Prenatal diagnosis by chorionic villus sampling shows trisomy 15 confined to the placenta; amniocentesis shows a disomic fetus. If the trisomy arose by maternal meiotic nondisjunction (the usual case) and the fetus was rescued by random loss of one chromosome 15, the probability that the fetus has maternal UPD 15, and hence Prader–Willi syndrome, is $1/3$. In practice the fetus is tested directly for UPD with markers or by methylation analysis of 15q11.

### 16.2.6. Why Aneuploidy Is Harmful: Dosage Balance

Every gene on an extra chromosome is expressed at about $1.5$ times the normal level (measured for chromosome 21 in Down syndrome cells), and every gene on a missing one at about half. A doubling of all genes, as in a polyploid, keeps their ratios. The asymmetry suggests that ratios, not absolute amounts, matter.

**Definition 16.2.3 (Dosage Balance)** The **dosage balance** hypothesis states that the products of many genes act in stoichiometric complexes or interacting networks, so that changing the dose of some of them relative to the others (as in aneuploids or segmental duplications) is more harmful than changing the dose of all of them together (as in polyploids).

The hypothesis explains several observations: aneuploidy of larger chromosomes, with more genes, is more harmful; in *Datura stramonium*, Blakeslee's twelve primary trisomics (1920s), one for each chromosome, each have a characteristic capsule shape, so each chromosome carries dose-sensitive genes of its own; the genes for subunits of complexes, transcription factors and signaling proteins are those most often retained in duplicate after whole-genome duplications and least often retained after small duplications (16.6.3); and aneuploid yeast and mammalian cells show protein-folding stress and slow proliferation whatever the extra chromosome. Some genes on chromosome 21 contribute specific features of Down syndrome (for example *APP*, whose extra copy causes the early Alzheimer pathology, and *DYRK1A*), but much of the phenotype probably reflects the many small imbalances together.

## 16.3. Segregation in Trisomics

A trisomic forms a trivalent (or a bivalent and a univalent) in meiosis, and two of the three homologues go to one pole and one to the other. If all three are distinct and the orientation is random, each of the three pairs goes together with probability $1/3$.

**Formula 16.3.1 (Gametes of a Trisomic)** Under random 2 : 1 segregation of three homologues, with no crossing over between the locus and the centromere, half of the gametes are disomic ($n + 1$) and half monosomic ($n$). A trisomic of genotype $AAa$ produces

$$
\tfrac16\,AA : \tfrac26\,Aa : \tfrac26\,A : \tfrac16\,a,
$$
so $5/6$ of the gametes carry $A$; a trisomic $Aaa$ produces $\frac16\,aa : \frac26\,Aa : \frac26\,a : \frac16\,A$.

**Proof** The three pairs of homologues that can go together, $\{A_1A_2\}$, $\{A_1a\}$ and $\{A_2a\}$, each have probability $1/3$; each gives one disomic and one monosomic gamete with probability $1/2$ each: $AA$ and $a$ for the first, $Aa$ and $A$ for the other two. $\square$

In practice $n + 1$ gametes are transmitted less often than $n$ gametes, especially through pollen, where they compete poorly; the expected ratios must then be corrected for the transmission rate of the extra chromosome.

**Example 16.3.1** A trisomic $AAa$ plant is selfed. (a) If all gametes function equally, the recessive $aa$ offspring arise only from $a \times a$ (an $Aaa$ or $AAa$ zygote has the dominant phenotype), with probability $(1/6)^2 = 1/36$: dominant : recessive $= 35 : 1$. (b) If only monosomic ($n$) pollen functions, the pollen is $\frac23\,A : \frac13\,a$ and the eggs as above; $\mathbb{P}(aa) = \frac16 \cdot \frac13 = \frac1{18}$, a ratio of $17 : 1$.

Trisomics were the first method of assigning genes to chromosomes in plants with many chromosomes, before molecular markers.

**Algorithm 16.3.1 (Assigning a Gene to a Chromosome with Trisomics)**
1. Cross a recessive mutant $aa$ (as male) to each primary trisomic line $AAA$ of the species, one line per chromosome.
2. Select trisomic $\mathrm{F}_1$ plants (recognized by their phenotype or karyotype); they are $AAa$ for the chromosome carrying the gene and $Aa$ (plus an extra unrelated chromosome) otherwise.
3. Testcross the trisomic $\mathrm{F}_1$ (as female) to $aa$. For the line trisomic for the chromosome carrying the gene, the progeny are about $5$ dominant $: 1$ recessive (Formula 16.3.1; less if the gene is far from the centromere); for all other lines $1 : 1$.

## 16.4. Triploids

A triploid has three homologues of each chromosome. At meiosis they form trivalents (or a bivalent and a univalent), and each trivalent sends two members to one pole and one to the other, independently of the other trivalents.

**Formula 16.4.1 (Euploid Gametes of a Triploid)** If each of the $x$ trivalents of a triploid sends one or two homologues to a given pole with probability $1/2$ each, independently, the fraction of gametes with a complete euploid set ($x$ or $2x$ chromosomes) is

$$
\mathbb{P}(\text{euploid}) = 2\left(\tfrac12\right)^x = 2^{1 - x}.
$$

**Proof** A gamete has $x$ chromosomes only if every trivalent sends one copy to its pole (probability $(1/2)^x$) and $2x$ only if every trivalent sends two (probability $(1/2)^x$); all other gametes are aneuploid. $\square$

![Fertility of triploids. The fraction of gametes that receive a complete haploid or diploid set falls as 2(1/2)^x with the basic number x (line; circles: simulation of 100 000 meioses for each x); with x = 11 (banana, watermelon) it is about one in a thousand, so that triploids are effectively sterile](./plots/triploid-gametes.py)

With $x = 11$, as in banana and watermelon, only about 1 in 1 000 gametes is euploid; most of the aneuploid gametes and zygotes of plants with so many imbalances die. Triploids are therefore sterile, which is an advantage for fruit without seeds. Seedless watermelons are triploid seeds produced by crossing a tetraploid (made with colchicine, 16.7) as female with a diploid as male; the triploid plants are pollinated by diploid plants grown alongside, which stimulates fruit development without fertile seeds. Cultivated bananas are triploid clones propagated vegetatively. Triploidy in humans (69 chromosomes, from dispermy or a diploid gamete) occurs in about $1\,\%$ of conceptions and is almost always lost.

The same reasoning explains the sterility of monoploids and of haploid plants of diploid species. Their $x$ chromosomes have no partners and form univalents; if each univalent goes to either pole with probability $1/2$, a given meiotic product receives the complete set with probability $(1/2)^{x}$, about 1 in 1000 for maize ($x = 10$). The monoploid males of bees, ants and wasps are fertile because they avoid reduction: the first meiotic division of their spermatocytes is abortive, and all chromosomes pass together into the sperm. (The females that aphids produce by parthenogenesis in summer, by contrast, are diploid: their eggs form without meiotic reduction.)

## 16.5. Autotetraploids

### 16.5.1. Chromosome Segregation

A tetraploid has four homologues of each chromosome. They may pair as two bivalents or as a quadrivalent, in which partners exchange along the chromosome. In autotetraploids the main configurations at metaphase I are one quadrivalent (IV) or two bivalents (II + II), with a trivalent and a univalent (III + I) or a bivalent and two univalents (II + I + I) in a minority of cells; most segregate 2 : 2, but III + I and unpaired univalents can give 3 : 1 segregation and aneuploid gametes. If the four homologues go two to each pole at random, and no crossing over separates the locus from the centromere, a gamete receives a random pair of the four homologues: there are $\binom{4}{2} = 6$ equally likely pairs.

**Formula 16.5.1 (Gametes of an Autotetraploid under Chromosome Segregation)** For a locus close to the centromere, with random segregation of the four homologues two to each pole, the gametes ($2x$) of the five genotypes are:

| Genotype | Name | Gametes $AA : Aa : aa$ | Recessive on selfing | Testcross to $aaaa$ |
|---|---|---|---|---|
| $AAAA$ | quadruplex | $1 : 0 : 0$ | 0 | all dominant |
| $AAAa$ | triplex | $1 : 1 : 0$ | 0 | all dominant |
| $AAaa$ | duplex | $1 : 4 : 1$ | $1/36$ | $5 : 1$ |
| $Aaaa$ | simplex | $0 : 1 : 1$ | $1/4$ | $1 : 1$ |
| $aaaa$ | nulliplex | $0 : 0 : 1$ | 1 | all recessive |

So the $\mathrm{F}_2$ of $AAAA \times aaaa$, whose $\mathrm{F}_1$ is duplex, segregates $35$ dominant $: 1$ recessive instead of $3 : 1$. Recessive phenotypes are rare in autotetraploids, which explains why tetraploid crops hide recessive variation and respond slowly to selection against it.

### 16.5.2. Chromatid Segregation and Double Reduction

The ratios above assume that the two sister chromatids of a chromosome never end up in the same gamete. In a quadrivalent, a crossover between the locus and the centromere followed by a particular orientation can bring two sister copies of the same segment to one pole in meiosis I, and they can then pass to the same gamete in meiosis II.

**Definition 16.5.1 (Double Reduction)** **Double reduction** is the transmission to a gamete of a polyploid of two copies of a segment derived from the two sister chromatids of one chromosome. It requires a quadrivalent (or higher multivalent), a crossover between the locus and the centromere, and suitable segregation in both divisions; its frequency $\alpha$ for a locus increases with the distance from the centromere, from $0$ (random chromosome segregation) to a maximum of $1/7$ (random chromatid segregation, in which the gamete receives two of the eight chromatids at random).

**Formula 16.5.2 (Tetrasomic Gametes with Double Reduction)** With a double-reduction rate $\alpha$, a gamete receives two copies of one chromosome with probability $\alpha$ (each of the four with probability $\alpha/4$) and two different chromosomes with probability $1 - \alpha$. The gametes of a duplex $AAaa$ are

$$
AA : Aa : aa = \frac{1 + 2\alpha}{6} : \frac{4(1 - \alpha)}{6} : \frac{1 + 2\alpha}{6},
$$
and of a simplex $Aaaa$, $AA : Aa : aa = \dfrac{\alpha}{4} : \dfrac{1 - \alpha}{2} : \dfrac{2 + \alpha}{4}$. At $\alpha = 1/7$ the duplex gives $3 : 8 : 3$, and its selfed progeny contain a fraction $(3/14)^2 = 9/196$ of recessives, a ratio of about $20.8 : 1$.

**Proof** For the duplex, two different homologues give $AA$ with probability $1/6$, $Aa$ with $4/6$ and $aa$ with $1/6$; two sister copies give $AA$ or $aa$ with probability $1/2$ each. Hence $\mathbb{P}(AA) = (1 - \alpha)/6 + \alpha/2 = (1 + 2\alpha)/6$, and similarly for the others. For the simplex, two different homologues give $Aa$ with probability $3/6$ and $aa$ with $3/6$; sister copies give $AA$ with probability $1/4$ and $aa$ with $3/4$. Under random chromatid segregation a gamete receives one of the $\binom{8}{2} = 28$ pairs of chromatids, of which 4 are sister pairs: $\alpha = 4/28 = 1/7$. $\square$

![Autotetraploid segregation. A: four homologues (one chromatid each) paired as two bivalents or as a quadrivalent in which they exchange partners. B: gametes of a duplex AAaa as functions of the double-reduction rate α (Formula 16.5.2): from 1:4:1 at α = 0 (random chromosome segregation) to 3:8:3 at α = 1/7 (random chromatid segregation). C: fraction of recessive offspring on selfing a duplex (from 1/36 to 9/196) and a simplex (from 1/4 to 225/784); circles: simulations of 20 000 offspring](./plots/tetraploid-gametes.py)

Because double reduction makes the ratios depend on the distance from the centromere, it can be used to map loci relative to centromeres in autotetraploids, as tetrad analysis does in fungi ([7.4.9](/7.4.9)). Its rate is usually much below $1/7$, because quadrivalents form only in part of the meioses.

### 16.5.3. Fertility and Stabilization

Quadrivalents can segregate 3 : 1 instead of 2 : 2, and multivalents of several chromosomes make many new autotetraploids partially sterile. Established autotetraploid species and crops have evolved regular bivalent pairing (diploidization of meiosis), usually through genes that shorten the chromosome axes and limit crossovers, so that the four homologues pair two by two; in *Arabidopsis arenosa* the alleles that do this have been identified. Autopolyploids keep tetrasomic inheritance (any homologue can pair with any other), unlike allopolyploids.

## 16.6. Allopolyploids and Whole-Genome Duplication

### 16.6.1. Making Fertile Hybrids

A hybrid of two diploid species with sets $A$ and $B$ has one set of each. If the sets are too different to pair, the univalents segregate at random and the hybrid is sterile, like a triploid. Doubling the chromosome number gives each chromosome a partner and restores fertility.

**Example 16.6.1 (*Raphanobrassica*)** Georgi Karpechenko (1928) crossed radish (*Raphanus sativus*, $2n = 18$) with cabbage (*Brassica oleracea*, $2n = 18$). The hybrids had $9 + 9$ unpaired chromosomes and were almost sterile, but a few produced unreduced gametes, and these gave fertile allotetraploids with $2n = 36$ (18 from each parent), which formed 18 bivalents and bred true. Unfortunately the plants had the root of a cabbage and the leaves of a radish. *Raphanobrassica* was the first new species made in the laboratory: it was reproductively isolated from both parents, because its backcrosses were triploid.

**Example 16.6.2 (Genome Analysis by Chromosome Pairing)** Chromosome pairing in hybrids shows which chromosome sets two species share, a method developed by Hitoshi Kihara for wheat (1920s–1930s). Bread wheat (AABBDD, $2n = 42$) crossed with durum wheat (AABB, $2n = 28$) gives a pentaploid hybrid AABBD with $21 + 14 = 35$ chromosomes, which forms $14$ bivalents (the A and B chromosomes of both parents pair) and $7$ univalents (the D chromosomes). Bread wheat crossed with *Triticum timopheevii* (AAGG) gives AABDG, also with 35 chromosomes, but only the A chromosomes pair: $7\,\mathrm{II} + 21\,\mathrm{I}$, which shows that *T. timopheevii* shares only the A genome with bread wheat and that its second genome G differs from B. The univalents of both hybrids segregate at random, so their gametes are unbalanced and the hybrids are largely sterile (Formula 16.4.1 with the 7 or 21 univalents).

An allotetraploid has disomic inheritance: each chromosome pairs only with its homologue from the same parental species, so its genes segregate in $3 : 1$ ratios like those of a diploid, while the two homoeologous copies (one from each subgenome) can diverge in function.

### 16.6.2. Wheat, *Brassica* and Cotton

![Allopolyploid crops. A: bread wheat arose by two rounds of hybridization followed by genome doubling. Tetraploid wheat (AABB, emmer and durum) formed about half a million years ago from *Triticum urartu* (A genome) and a species related to *Aegilops speltoides* (B genome); hexaploid bread wheat (AABBDD) formed about 10 000 years ago, in cultivated fields, from tetraploid wheat and the wild goat grass *Aegilops tauschii* (D genome). B: the triangle of U (1935): the three diploid *Brassica* species with genomes A, B and C and the allotetraploids formed from each pair, *B. juncea* (AABB), *B. napus* (AACC, rapeseed) and *B. carinata* (BBCC), whose chromosome numbers are the sums of those of their parents](./plots/allopolyploid-origins.py)

Bread wheat pairs only true homologues thanks to the *Ph1* locus on chromosome 5B, which suppresses pairing between homoeologous chromosomes of the three subgenomes; without *Ph1*, multivalents form and fertility falls. Because each gene is present three times, bread wheat tolerates nullisomy, monosomy and the replacement of one chromosome by a homoeologue, and Ernest Sears's complete series of nullisomic–tetrasomic lines (1950s) assigned genes to chromosomes and showed which chromosomes of the three subgenomes compensate for each other. Cultivated upland cotton (*Gossypium hirsutum*, AADD, $2n = 52$) combines an Old World A genome with a New World D genome; its long spinnable fibers develop from the A genome's lineage but depend on both.

### 16.6.3. Whole-Genome Duplication in Evolution

**Definition 16.6.1 (Whole-Genome Duplication)** A **whole-genome duplication** (WGD) is the doubling of the complete genome of a lineage by autopolyploidy or allopolyploidy, recognized in the genomes of the descendants, after most duplicate genes have been lost, as pairs of paralogous chromosome blocks with the same gene order (ohnologs, the paralogs that arose by a WGD).

Polyploidy has been frequent in plants: about $15\,\%$ of speciation events in flowering plants and about a third in ferns are accompanied by an increase in ploidy, and all flowering plants descend from at least two ancient WGDs. *Arabidopsis thaliana*, with a small genome, carries traces of three. In animals WGD is rarer, perhaps because of chromosomal sex determination, but it occurred twice at the base of the vertebrates (the 2R hypothesis of Ohno, which explains the four *Hox* clusters of mammals), once more in teleost fishes and again in salmonids. The budding yeast *Saccharomyces cerevisiae* descends from a WGD about 100 million years ago; comparison with the related *Kluyveromyces waltii* (Kellis and colleagues, 2004) showed that each region of *K. waltii* corresponds to two regions of *S. cerevisiae*, which retained both copies of only about $12\,\%$ of the genes. The retained pairs are enriched in subunits of complexes and regulatory proteins, as predicted by dosage balance (Definition 16.2.3). The fates of duplicate genes (loss, neofunctionalization, subfunctionalization) are treated in [7.4.14](/7.4.14) and their evolution in [7.10](/7.10).

## 16.7. Uses in Breeding

- Chromosome doubling. Colchicine, an alkaloid of the autumn crocus that blocks microtubule assembly ([7.3.21](/7.3.21)), prevents spindle formation; the chromosomes replicate and separate but stay in one nucleus, which doubles its chromosome number. Applied to seedlings or buds, colchicine (or oryzalin) produces autotetraploids and fertile allopolyploids. Triticale, an allopolyploid of wheat and rye ($6x$ or $8x$), was made in this way and is grown as a fodder crop; hexaploid triticale (AABBRR) combines durum wheat with rye, octoploid triticale (AABBDDRR) bread wheat with rye.
- Haploids and doubled haploids. Culture of anthers or isolated microspores, crosses with haploid-inducer lines (in maize; in *Arabidopsis*, crosses with lines carrying a modified centromeric histone CENH3, whose chromosomes are eliminated from the zygote), or wide crosses (wheat × maize, where the maize chromosomes are lost) produce plants with one chromosome set. Doubling their chromosomes gives completely homozygous diploids in one generation, instead of the six or more generations of selfing otherwise needed, and recessive alleles are exposed immediately in the haploids.
- Polyploids are often larger in cells, flowers and fruits (the gigas effect): newly made autopolyploids have larger stomata and guard cells, fewer stomata per unit leaf area, thicker leaves and larger flowers, but they often grow and flower more slowly and are less fertile; guard-cell length and the number of chloroplasts per guard cell are used to screen seedlings for doubled chromosome number. Triploids give seedless fruit (16.4), and tetraploid forms of ryegrass, red clover and many ornamentals are grown for their size.
- Monosomic and nullisomic series and alien addition and substitution lines (with one chromosome pair from a related species) transfer resistance genes from wild relatives into crops.

## Summary

| Change | How it arises | Meiosis | Key ratio or probability |
|---|---|---|---|
| Trisomy ($2n + 1$) | nondisjunction, MI or MII (Proposition 16.2.1) | trivalent, 2 : 1 | $AAa$: $1\,AA : 2\,Aa : 2\,A : 1\,a$ (Formula 16.3.1); selfed $35 : 1$ or $17 : 1$ |
| Monosomy ($2n - 1$) | nondisjunction, chromosome loss | univalent | human autosomal monosomies lethal; 45,X mostly lost |
| UPD | trisomy rescue (probability $1/3$), monosomy rescue | — | isodisomy exposes recessives; imprinting disorders (Definition 16.2.2) |
| Triploid ($3x$) | unreduced gamete × normal gamete, $4x \times 2x$ | trivalents | euploid gametes $2(1/2)^x$ (Formula 16.4.1) |
| Autotetraploid ($4x$) | doubling (colchicine, unreduced gametes) | bivalents or quadrivalents | duplex $1 : 4 : 1$, selfed $35 : 1$; with double reduction $\alpha \le 1/7$: up to $3 : 8 : 3$, $20.8 : 1$ (Formulas 16.5.1, 16.5.2) |
| Allopolyploid | hybridization + doubling | bivalents (disomic inheritance) | ratios of diploids; *Raphanobrassica*, wheat, *Brassica*, cotton |

- Notation: $x$ basic number, $n$ gametic number; a chromosome set contains each of the $x$ chromosomes once; euploidy, aneuploidy (hypo- and hyperploidy, double monosomics and trisomics), polyploidy (Definitions 16.1.1–16.1.3).
- Monoploids: univalents, complete gametes $(1/2)^x$; male Hymenoptera fertile through an abortive meiosis I.
- Genome analysis (Example 16.6.2): AABBD $14\,\mathrm{II} + 7\,\mathrm{I}$; AABDG $7\,\mathrm{II} + 21\,\mathrm{I}$.
- Human aneuploidy: about $5\,\%$ of pregnancies, mostly maternal MI errors; Down syndrome risk rises from about 1 in 1 500 at 20 to 1 in 35 at 45 (Formula 16.2.1); sex-chromosome aneuploidies are tolerated because of X inactivation, with phenotypes from escape and PAR genes.
- Mitotic errors: mosaics, gynandromorphs (Definition 16.2.1), confined placental mosaicism; trisomy rescue and UPD (Definition 16.2.2).
- Dosage balance (Definition 16.2.3): ratios matter more than absolute dose; explains the harm of aneuploidy, the tolerance of polyploidy, and which duplicates are retained after WGD (Definition 16.6.1).
- Tools: mapping with trisomics (Algorithm 16.3.1), nullisomic–tetrasomic lines, doubled haploids, colchicine doubling.

## Questions

1. Bread wheat has $2n = 42$. Give $x$, $n$, and the chromosome numbers of a monosomic, a nullisomic, a double trisomic, a haploid and a monoploid plant.

   **Answer** $x = 7$, $n = 21$. Monosomic $2n - 1 = 41$; nullisomic $2n - 2 = 40$; double trisomic $2n + 1 + 1 = 44$; haploid $n = 21$ ($3x$); monoploid $x = 7$ (not viable as a plant, since it would contain only one of the three subgenomes).
2. A woman heterozygous $A/a$ at a locus tightly linked to the centromere of chromosome 21 has a child with free trisomy 21. Give the probability that the child carries both $A$ and $a$ from her if the error was (a) in meiosis I, (b) in meiosis II. (c) At a marker far from the centromere, why can the pattern be reversed?

   **Answer** (a) $1$: MI nondisjunction transmits both homologues. (b) $0$: MII nondisjunction transmits two copies of one homologue, $AA$ or $aa$. (c) A crossover between the marker and the centromere in meiosis I exchanges the distal parts of two non-sister chromatids; after an MI error the two transmitted chromatids (one from each homologue) can then carry the same distal allele, and after an MII error the two sister chromatids can carry different distal alleles. Distal markers therefore show reduction to homozygosity after MI errors and heterozygosity after MII errors in a fraction of cases that grows with the distance from the centromere.
3. Use Formula 16.2.1 to compute the risk of Down syndrome at birth for mothers aged 25 and 38, and the ratio of the two risks.

   **Answer** At 25: $\mathrm{e}^{-0.282(25 - 37.23)} = \mathrm{e}^{3.449} = 31.5$; $4.211/32.5 = 0.130$; $\mathrm{e}^{7.200} = 1340$; risk $\approx 1/1340$. At 38: $\mathrm{e}^{-0.217} = 0.805$; $4.211/1.805 = 2.333$; $\mathrm{e}^{4.997} = 148$; risk $\approx 1/149$. The ratio is about $9$.
4. A trisomic plant $Aaa$ is testcrossed (as female) to $aa$. What ratio of dominant to recessive progeny is expected if all eggs function equally? If the plant is used as male and only $n$ pollen functions?

   **Answer** Gametes $\frac16\,aa : \frac26\,Aa : \frac26\,a : \frac16\,A$; dominant ($Aa$ or $A$) $= 3/6$, so $1 : 1$ as female. As male with only $n$ pollen: $a$ and $A$ pollen in the ratio $2 : 1$, so $1$ dominant $: 2$ recessive.
5. A recessive mutation of tomato is crossed with each of the 12 primary trisomics; the trisomic $\mathrm{F}_1$ plants are testcrossed as females to the mutant. The progeny of the line trisomic for chromosome 7 show 412 dominant and 96 recessive plants; all other lines give about $1 : 1$. Is the gene on chromosome 7? Is the ratio consistent with $5 : 1$, and what might explain a deviation?

   **Answer** Yes: only chromosome 7 deviates from $1 : 1$. Expected under $5 : 1$ for $508$ plants: $423.3$ and $84.7$; $\chi^2 = (11.3)^2/423.3 + (11.3)^2/84.7 = 0.30 + 1.52 = 1.82$ with 1 degree of freedom, $p \approx 0.18$, consistent. A higher recessive fraction would be expected if the locus is far from the centromere (crossing over between it and the centromere moves toward chromatid segregation) or if the transmission of disomic eggs differs from that of monosomic ones.
6. What fraction of the gametes of a triploid with $x = 7$ are euploid? With $x = 11$? Why is the answer for a triploid human ($x = 23$) irrelevant to human genetics?

   **Answer** $2^{1 - 7} = 1/64 \approx 1.6\,\%$; $2^{1 - 11} = 1/1024 \approx 0.1\,\%$. Human triploids (69,XXX, XXY or XYY) almost never survive to birth and never reproduce; the question of their gametes does not arise.
7. An autotetraploid $AAAA$ is crossed with $aaaa$. (a) What are the phenotypic ratios in the $\mathrm{F}_2$ and in the testcross of $\mathrm{F}_1$ to $aaaa$, under random chromosome segregation? (b) Under random chromatid segregation?

   **Answer** $\mathrm{F}_1$ is $AAaa$. (a) Gametes $1\,AA : 4\,Aa : 1\,aa$: $\mathrm{F}_2$ recessive $(1/6)^2 = 1/36$, $35 : 1$; testcross $5 : 1$. (b) Gametes $3 : 8 : 3$: $\mathrm{F}_2$ recessive $(3/14)^2 = 9/196$, $187 : 9 \approx 20.8 : 1$; testcross $11 : 3$.
8. In an autotetraploid, a simplex $Aaaa$ plant is selfed and gives $1.0\,\%$ of $AAAA$ (homozygous dominant) offspring. Estimate the double-reduction rate $\alpha$ at the locus.

   **Answer** Under Formula 16.5.2 the simplex makes $AA$ gametes with frequency $\alpha/4$, and $AAAA$ offspring require two of them: $(\alpha/4)^2 = 0.01$, so $\alpha/4 = 0.1$ and $\alpha = 0.4$. This exceeds the maximum $1/7$, so the observation cannot be explained by double reduction alone: the plant is probably not simplex (it could be duplex, giving $AAAA$ at $(1/6)^2 \approx 2.8\,\%$ or more), or the counts include misclassified plants. The calculation shows how a measured ratio is checked against the bounds of a model.
9. A child with cystic fibrosis is homozygous for the *CFTR* mutation p.Phe508del. The mother is a carrier; the father carries no *CFTR* mutation, and paternity is confirmed. Markers along chromosome 7 are all maternal, and the child is homozygous at every one of them. Explain, and give the type of the meiotic error and of the rescue.

   **Answer** Maternal uniparental isodisomy 7: the child has two copies of one maternal chromosome 7 and no paternal one. Homozygosity along the whole chromosome (no crossovers transitions) indicates complete isodisomy, which most simply arises by monosomy rescue (a nullisomic sperm and a normal egg, followed by duplication of the maternal 7) or by a maternal meiosis II error followed by trisomy rescue with loss of the paternal chromosome (in which case markers distal to crossovers would be heterozygous). The child's short stature fits maternal UPD 7 (Silver–Russell spectrum).
10. Prenatal testing finds a fetus with a normal karyotype but placental cells trisomic for chromosome 15 of maternal origin. Assuming random loss of one chromosome in trisomy rescue, what is the risk of Prader–Willi syndrome? How would it change if the trisomy were of paternal origin?

    **Answer** $1/3$: the fetus has maternal UPD 15 with probability $1/3$ (if the paternal 15 was lost), which causes Prader–Willi syndrome. If the extra chromosome were paternal, the rescued fetus would have paternal UPD 15 with probability $1/3$, causing Angelman syndrome instead.
11. Why do 47,XXY men have a phenotype, if all X chromosomes but one are inactivated? Why are 45,X individuals short, and why are most 45,X conceptions lost?

    **Answer** Genes in the pseudoautosomal regions and about $15\,\%$ of other X-linked genes escape inactivation, so XXY cells have three active copies of the PAR genes and two of the escape genes; in the germline the extra X is active too, which disrupts spermatogenesis. 45,X cells have one copy of *SHOX* (in PAR1) instead of two, which reduces growth (haploinsufficiency); the loss of most 45,X conceptions is thought to reflect haploinsufficiency of such genes in the placenta and embryo, and the survivors are often mosaics with a normal cell line.
12. A breeder wants a seedless triploid watermelon. Describe the crosses, give the chromosome numbers ($x = 11$), and explain why the triploid plants must be grown with diploid plants.

    **Answer** Double the chromosomes of a diploid ($2n = 22$) with colchicine to make a tetraploid ($4x = 44$); cross the tetraploid as female with a diploid as male, giving triploid seeds ($3x = 33$; the reverse cross gives poor seed). The triploid plants produce almost no euploid gametes ($2^{-10}$, Formula 16.4.1), so their own pollen is nearly sterile; fruit set requires pollination, which stimulates fruit development, so diploid pollinizer plants are grown alongside. The fruits contain only small, empty seed coats.

13. Tomato has $2n = 24$. Give the chromosome numbers of a double monosomic, a tetrasomic, a double trisomic, a triploid and a monoploid. Which of them are euploid?

    **Answer** Double monosomic $2n - 1 - 1 = 22$; tetrasomic $2n + 2 = 26$; double trisomic $2n + 1 + 1 = 26$; triploid $3x = 36$; monoploid $x = 12$. The triploid and the monoploid are euploid; the other three are aneuploid (hypoploid and hyperploid). The tetrasomic and the double trisomic have the same number but different constitutions: two extra copies of one chromosome versus one extra copy of each of two.

14. Predict the chromosome pairing at metaphase I and the somatic chromosome numbers of the following hybrids, assuming that only chromosomes of the same genome pair: (a) bread wheat (AABBDD) × *Aegilops tauschii* (DD, $2n = 14$); (b) durum wheat (AABB) × rye (RR, $2n = 14$); (c) the plant obtained by doubling (b); (d) radish × cabbage ($2n = 18$ each).

    **Answer** (a) ABDD: $7 + 7 + 14 = 28$ chromosomes, $7\,\mathrm{II}$ (D with D) $+ 14\,\mathrm{I}$. (b) ABR: $21$ chromosomes, $21\,\mathrm{I}$, sterile. (c) AABBRR, hexaploid triticale: $42$ chromosomes, $21\,\mathrm{II}$, fertile. (d) $9 + 9 = 18$ univalents (Example 16.6.1); doubling gives *Raphanobrassica* with $18\,\mathrm{II}$.

15. A haploid plant of a diploid species with $x = 7$ is obtained by anther culture. (a) What fraction of its meiotic products receive a complete set of 7 chromosomes, if each univalent goes to either pole at random? (b) If eggs and pollen are formed independently in this way and fuse at random, what fraction of zygotes from selfing would be euploid diploids? (c) Why are doubled haploids, not haploids, used in breeding?

    **Answer** (a) $(1/2)^7 = 1/128 \approx 0.78\,\%$. (b) Both gametes must be complete: $(1/128)^2 = 6.1 \times 10^{-5}$, about 1 in 16 000 (in practice, since incomplete pollen mostly aborts, seed set is somewhat higher than this but still close to zero). (c) Doubling with colchicine gives a fertile, completely homozygous diploid in one step (Section 16.7); the haploid itself is nearly sterile.

16. In an autotetraploid, $70\,\%$ of cells form a quadrivalent and $30\,\%$ two bivalents for a given chromosome. Quadrivalents segregate 2 : 2 in $90\,\%$ of cases and 3 : 1 in $10\,\%$; bivalents always 2 : 2. What fraction of the gametes are aneuploid for this chromosome? If the species has $x = 12$ chromosomes behaving independently in this way, what fraction of gametes are euploid?

    **Answer** Only 3 : 1 segregations give aneuploid gametes, and both products of such a meiosis are aneuploid (3 copies or 1): $0.7 \times 0.1 = 0.07$. Euploid for all 12: $0.93^{12} = 0.42$. Multivalent pairing is the main reason for the reduced fertility of newly made autotetraploids (Section 16.5.3).
