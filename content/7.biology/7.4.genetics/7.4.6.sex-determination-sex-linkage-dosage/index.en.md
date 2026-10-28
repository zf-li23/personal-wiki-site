---
title: Sex Determination, Sex Linkage and Dosage Compensation
description: How organisms decide between male and female (XY, XO, ZW, haplodiploidy and complementary sex determination, temperature), sex determination in humans (SRY, the pseudoautosomal regions, sex chromosome aneuploidy, androgen insensitivity) and in Drosophila (X counting and the Sxl splicing cascade); X-linked, Y-linked and Z-linked inheritance, Morgan's crosses and Bridges' nondisjunction; sex-limited and sex-influenced traits; dosage compensation and the genetic consequences of X inactivation.
---

Sex is the most conspicuous phenotype of most animals and many plants, and it was the first trait to be tied to a particular chromosome. This chapter has three parts. The first asks how sex is determined: by sex chromosomes (with very different mechanisms behind the same XX/XY notation in humans and flies), by the number of chromosome sets, by a single multi-allelic locus, or by temperature. The second follows genes that happen to lie on sex chromosomes: their transmission differs between the sexes, and it was such a gene, Morgan's *white*, that together with Bridges' analysis of nondisjunction proved the chromosome theory of inheritance ([7.4.5](/7.4.5)). The third concerns the problem that sex chromosomes create, unequal gene dose in the two sexes, and the strategies that solve it. The molecular mechanism of **X-chromosome inactivation** is described in [7.3.17](/7.3.17#sec-17.1.3); here we study its genetic consequences, mosaicism and the variable phenotype of heterozygous women. The probabilities of X-linked risk in human families are computed with the Bayesian methods of [7.4.7](/7.4.7), and the development of the gonads and genitalia is treated in [7.5](/7.5).

## 6.1. Sex-Determining Systems

### 6.1.1. Sex Chromosomes

In 1891 Hermann Henking saw that in the spermatocytes of the firebug *Pyrrhocoris* one chromosome had no partner and went to only half of the sperm; he called it "X" for its unknown nature. In 1905 Nettie Stevens (in the mealworm *Tenebrio*) and Edmund Wilson (in true bugs) showed that females and males differ in a pair of chromosomes and that the sex of the zygote depends on which of two kinds of sperm fertilizes the egg.

**Definition 6.1.1 (Sex Chromosome)** A **sex chromosome** is a chromosome whose presence, absence or number differs between the sexes of a species and is associated with sex determination, such as the X and Y chromosomes of mammals and the Z and W chromosomes of birds. The sex with two different sex chromosomes (XY males, ZW females) is the heterogametic sex, because it produces two kinds of gametes in equal numbers; the sex with two copies of the same sex chromosome is the homogametic sex.

Because the heterogametic parent transmits each of its two sex chromosomes to half of its gametes and the homogametic parent always transmits the same one, an XX × XY or ZW × ZZ cross is a **testcross** for sex: it predicts the $1{:}1$ sex ratio of most species.

**Definition 6.1.2 (Sex Determination)** **Sex determination** is the mechanism that decides whether a zygote or embryo develops as a male or as a female (or as a hermaphrodite), either genetically (by sex chromosomes, by the number of chromosome sets, or by genes at a sex-determining locus) or environmentally (by temperature, social cues or other external conditions).

Sex determination is distinct from sex differentiation, the development of the gonads, genitalia and secondary sexual characters that follows the decision.

![Some sex-determining systems. In XX/XY systems the male is heterogametic: in mammals a gene on the Y (SRY) determines maleness, whereas in *Drosophila* the number of X chromosomes decides and the Y is needed only for male fertility. In XX/XO systems (grasshoppers; *Caenorhabditis elegans*, where XX individuals are self-fertilizing hermaphrodites) males lack the second X. In ZW/ZZ systems (birds, butterflies and moths) the female is heterogametic. In haplodiploid insects (bees, ants and wasps) females are diploid and males haploid, from unfertilized eggs. With temperature-dependent sex determination (many turtles, all crocodilians) the sex chromosomes are the same in both sexes and the incubation temperature of the egg decides](./plots/sex-determination-systems.py)

| System | Female | Male | Examples | What decides |
|---|---|---|---|---|
| XX/XY, Y-dominant | XX | XY | mammals | the *SRY* gene on the Y |
| XX/XY, X-counting | XX | XY | *Drosophila* | the dose of X-linked signal elements |
| XX/XO | XX (hermaphrodites in *C. elegans*) | XO | grasshoppers, *C. elegans* | the X : autosome ratio |
| ZW/ZZ | ZW | ZZ | birds, Lepidoptera, some fish and reptiles | Z dose (*DMRT1* in birds) |
| haplodiploidy | diploid | haploid | Hymenoptera, thrips, some mites | ploidy, through the *csd* locus in honey bees |
| environmental | depends | depends | turtles, crocodilians (temperature); *Bonellia* (larvae settling on a female become male); clownfish (social rank) | external cue |

Sex chromosomes have arisen many times from an ordinary pair of autosomes. Once a sex-determining gene appears on one homologue, selection favors suppression of recombination around it, and the non-recombining chromosome (Y or W) gradually loses most of its genes; the human Y retains only a few dozen protein-coding genes, against about 800–850 on the X. The process is described with its evolutionary genetics in [7.10](/7.10).

### 6.1.2. Haplodiploidy and Complementary Sex Determination

In honey bees (*Apis mellifera*) fertilized eggs become females (workers or queens, depending on larval diet) and unfertilized eggs become haploid males (drones). Johann Dzierzon inferred this in 1845, before chromosomes were known, from the observation that virgin queens produce only drones. Ploidy acts through a single locus: females are heterozygous at the *complementary sex determiner* (*csd*) gene, which encodes an SR-type protein; only a heteromeric complex of two different Csd proteins directs female splicing of *feminizer* (*fem*), whose product maintains its own female splicing by positive feedback and controls *doublesex*. Haploid males have one *csd* allele; diploid embryos homozygous at *csd* also develop as males, which are sterile and are eaten by the workers as larvae. Inbreeding therefore costs a colony part of its brood.

**Formula 6.1.1 (Diploid Males under Complementary Sex Determination)** Suppose a population has $k$ *csd* alleles of equal frequency $1/k$ and a queen is heterozygous for two of them. A drone carries one allele, which matches one of the queen's with probability $2/k$ under random mating; if it matches, half of the fertilized eggs are homozygous. The expected fraction of diploid males among the diploid offspring is

$$
\mathbb{P}(\text{diploid male}) = \frac{2}{k}\cdot\frac{1}{2} = \frac{1}{k},
$$
independently of the number of drones she mates with (multiple mating only reduces the variance between colonies). If a queen mates with a brother, his allele is one of their mother's two alleles: it equals the queen's maternal allele with probability $1/2$ and her paternal one with probability about $1/(2k)$, so the fraction of diploid males is about $\frac12\left(\frac12 + \frac{1}{2k}\right) \approx \frac14$.

**Example 6.1.1** Honey bee populations carry roughly 10–20 *csd* alleles each (more than 100 are known worldwide). With $k = 15$, about $1/15 \approx 7\,\%$ of diploid eggs become diploid males under random mating; a queen mated to her brother loses about $27\,\%$ of her diploid brood. The large number of *csd* alleles is itself a consequence of this cost: a rare allele rarely forms homozygotes, so its carriers have more daughters, and negative frequency-dependent selection maintains many alleles ([7.4.23](/7.4.23)).

![Two quantitative sex-determining systems. A: under complementary sex determination the expected fraction of diploid males among the diploid offspring of a honey bee queen is 1/k for k equally frequent csd alleles under random mating (line); simulations of 2000 colonies with one drone (circles) or fifteen drones (squares) agree with it, since multiple mating does not change the mean. A queen mated with her brother produces about one quarter diploid males whatever k (dashed). B: temperature-dependent sex determination modeled as a logistic reaction norm, P(male) = 1/(1 + exp(β(T − Tp))) with an illustrative pivotal temperature Tp = 29 °C and three slopes β; in many turtles cool incubation gives males and warm incubation females, and the transitional range of temperatures that gives both sexes is narrow](./plots/csd-and-temperature.py)

### 6.1.3. Environmental Sex Determination

In many turtles all eggs incubated below a pivotal temperature $T_{\mathrm{p}}$ hatch as males and all above it as females (in the red-eared slider *Trachemys scripta* $T_{\mathrm{p}} \approx 29\,^\circ\mathrm{C}$); in crocodilians intermediate temperatures give males and both extremes females. The sensitive period is the middle third of incubation. The curve is a **norm of reaction** of sex.

**Formula 6.1.2 (Logistic Model of Temperature-Dependent Sex Determination)** The fraction of males at constant incubation temperature $T$ is described by

$$
\mathbb{P}(\text{male} \mid T) = \frac{1}{1 + \mathrm{e}^{\beta (T - T_{\mathrm{p}})}},
$$
where $T_{\mathrm{p}}$ is the pivotal temperature (50 % of each sex) and $\beta > 0$ the steepness; the transitional range of temperatures that produces 10 % to 90 % males has width $2\ln 9/\beta \approx 4.4/\beta$.

In *T. scripta* the temperature signal is transduced by a calcium-dependent phosphorylation of a transcription factor that represses the histone demethylase gene *Kdm6b*, which in turn is needed to activate the male-determining gene *Dmrt1* at cool temperatures. Other environmental systems use social cues: the marine worm *Bonellia viridis* develops as a dwarf male if its larva settles on a female; clownfish (*Amphiprion*) are protandrous hermaphrodites in which the largest fish of a group becomes the female, and many wrasses are protogynous. In flowering plants most species are hermaphroditic or monoecious; about 6 % are dioecious, some with XY systems (*Silene latifolia*, with a large Y; papaya; asparagus). In maize, which is monoecious, two genes control where flowers of each sex form: a plant homozygous for *barren stalk* ($ba\,ba$) has no ears and is functionally male, and one homozygous for *tassel seed* ($ts\,ts$) converts the tassel into a female inflorescence; $ba\,ba\,ts\,ts$ plants are female, and the cross $ba\,ba\,ts\,ts$ (female) × $ba\,ba\,Ts\,ts$ (male) gives a $1{:}1$ ratio of males and females, an artificial XY system with $ts$ in the role of X.

## 6.2. Sex Determination in Humans

### 6.2.1. The Y Chromosome and *SRY*

Human sex chromosome aneuploids show that a Y chromosome makes a male, whatever the number of X chromosomes:

| Karyotype | Phenotype | Frequency (approximate) |
|---|---|---|
| 45,X (Turner syndrome) | female; short stature, gonadal dysgenesis, usually infertile | 1 in 2 500 female births (about 99 % of 45,X conceptions are lost) |
| 47,XXX | female; usually unremarkable, tall | 1 in 1 000 female births |
| 47,XXY (Klinefelter syndrome) | male; tall, small testes, infertile | 1 in 600 male births |
| 47,XYY (Jacobs syndrome) | male; tall, usually fertile | 1 in 1 000 male births |
| 45,Y (no X) | lethal | — |

The male-determining factor is the gene *SRY* (sex-determining region Y), identified in 1990 (Sinclair and colleagues) from sex-reversed patients: XX males carry a fragment of the Y, always including *SRY*, translocated to an X (usually by an aberrant crossover in the paternal meiosis), and many XY females carry a deletion or point mutation of *SRY*. In 1991 Koopman and colleagues showed sufficiency: XX mice transgenic for a $14\,\mathrm{kb}$ fragment containing *Sry* developed as males. SRY is an HMG-box transcription factor expressed briefly in the supporting cells of the bipotential gonad at about six weeks of human development; it activates *SOX9*, which maintains itself by feedback and specifies Sertoli cells, so that the gonad becomes a testis. The testis secretes anti-Müllerian hormone, which causes regression of the female internal ducts, and testosterone, which (after conversion to dihydrotestosterone by 5α-reductase) masculinizes the external genitalia. Without *SRY* the gonad becomes an ovary, and female development follows (its own genes, such as *WNT4*, *RSPO1* and *FOXL2*, actively maintain the ovary).

Mutations downstream of *SRY* dissociate chromosomal, gonadal and phenotypic sex. In *androgen insensitivity syndrome* an XY individual has testes and normal testosterone but a nonfunctional androgen receptor, encoded by the X-linked gene *AR*; in the complete form the external phenotype is female (with a short vagina and no uterus, because anti-Müllerian hormone still acts). Since a 46,XY individual with complete androgen insensitivity is infertile, the mutant allele is transmitted by heterozygous XX carriers, and half of the XY children of a carrier are affected: an X-linked recessive, sex-limited pattern. Autosomal recessive 5α-reductase deficiency gives a similar phenotype at birth that virilizes at puberty.

### 6.2.2. The Pseudoautosomal Regions

**Definition 6.2.1 (Pseudoautosomal Region)** A **pseudoautosomal region** is a segment of a sex chromosome that is homologous between the X and the Y (or Z and W), pairs and recombines between them in meiosis of the heterogametic sex, and therefore shows an inheritance pattern close to that of an autosome. Humans have PAR1, about $2.7\,\mathrm{Mb}$ at the tips of Xp and Yp, and PAR2, about $0.33\,\mathrm{Mb}$ at the tips of Xq and Yq; together they contain about 25–30 genes.

The X and Y pair in male meiosis only through the PARs, and a crossover in PAR1 is obligatory for their correct segregation. This single crossover in a short segment makes PAR1 the most highly recombining region of the male genome: its male genetic length is about $50\,\mathrm{cM}$ in $2.7\,\mathrm{Mb}$, roughly $18\,\mathrm{cM/Mb}$, against an average of about $1\,\mathrm{cM/Mb}$. The pseudoautosomal boundary separates PAR1 from the male-specific region of the Y (MSY), which never recombines with the X and contains *SRY*.

**Formula 6.2.1 (Recombination Between a Pseudoautosomal Locus and Sex)** Suppose that every male meiosis has exactly one crossover in PAR1, uniformly distributed over its length $L$. A locus at distance $d$ from the pseudoautosomal boundary is separated from the sex-determining region exactly when the crossover falls between them, with probability $d/L$; since a crossover involves two of the four chromatids, the probability that a sperm carries a recombinant chromosome is

$$
r(d) = \frac{d}{2L}, \qquad 0 \le d \le L.
$$
A locus at the boundary is completely sex-linked ($r = 0$), and a locus at the telomere is transmitted independently of sex ($r = 1/2$).

**Example 6.2.1** The gene *SHOX* (short stature homeobox), at about $0.6$–$0.65\,\mathrm{Mb}$ from the Xp/Yp telomere, lies about $2.1\,\mathrm{Mb}$ from the boundary, so Formula 6.2.1 predicts $r \approx 2.1/5.4 \approx 0.39$ between *SHOX* and sex in male meiosis: a father who is heterozygous for a *SHOX* deletion on his Y transmits it to about $61\,\%$ of his sons and $39\,\%$ of his daughters, rather than to all sons (Y-linked) or all daughters (X-linked). Loss of one *SHOX* copy (haploinsufficiency) contributes to the short stature of Turner syndrome.

![Quantitative consequences of sex linkage. A: if every male meiosis has one crossover in PAR1, uniformly placed, the recombination fraction between a pseudoautosomal locus and sex rises linearly from 0 at the pseudoautosomal boundary to one half at the telomere (Formula 6.2.1). B: in a population with Hardy–Weinberg proportions an X-linked recessive phenotype has frequency q in males and q² in females, and heterozygous carrier females (2pq) are about twice as common as affected males; for rare alleles such as those of hemophilia A almost all affected individuals are male, whereas for red-green color blindness affected women are not rare (Formula 6.4.2)](./plots/population-sex-linkage.py)

## 6.3. Sex Determination in *Drosophila* and *C. elegans*

### 6.3.1. Counting X Chromosomes

*Drosophila* has XX females and XY males, but the Y does not determine sex: XXY flies are fertile females and XO flies are males (sterile, because the Y carries male fertility genes). Bridges (1921) studied flies with different numbers of X chromosomes and sets of autosomes (A) and concluded that sex follows the ratio X : A, with $1.0$ and above female, $0.5$ male and intermediate ratios ($2X{:}3A$) intersexes. The modern picture is a count of X chromosomes rather than a true ratio. Several X-linked genes, the X signal elements (*sisterless-a*, *scute* (*sisterless-b*), *runt*, *unpaired*), encode transcription factors whose concentration in the early embryo is proportional to the number of X chromosomes; only the double dose of XX embryos activates the establishment promoter $P_{\mathrm{e}}$ of the gene *Sex-lethal* (*Sxl*). Autosomal "denominator" genes such as *deadpan* oppose them, which explains the intersexes of triploids, but in diploids the decision is a threshold in X dose.

### 6.3.2. A Cascade of Alternative Splicing

*Sxl* encodes an RNA-binding protein. Its later, maintenance promoter $P_{\mathrm{m}}$ is active in both sexes, and its transcript contains a male-specific exon with a stop codon. The early Sxl protein made from $P_{\mathrm{e}}$ in XX embryos binds this transcript and causes the exon to be skipped, so that more Sxl protein is made: a positive feedback loop that turns a transient signal into a permanent cell state, a bistable switch ([7.9](/7.9)). The decision then propagates through a chain of **alternative splicing** events:

1. Sxl blocks a splice site in the pre-mRNA of *tra* (named for the mutant phenotype, which transforms XX flies into males), so that female cells make functional Tra protein; in males the default splice includes a stop codon.
2. Tra, with the constitutive Tra2, promotes the female splicing of *doublesex* (*dsx*) and *fruitless* (*fru*) transcripts. DsxF and DsxM are transcription factors with a common DNA-binding domain and sex-specific C-termini that control somatic sexual differentiation in opposite directions; male Fru (FruM), made only in the absence of Tra, specifies the neurons of male courtship behavior.
3. Sxl also binds *msl-2* mRNA and represses its translation, so that females do not assemble the male-specific lethal (MSL) dosage compensation complex (Section 6.5).

![The sex-determination cascade of *Drosophila* in Systems Biology Graphical Notation (activity flow). In XX embryos the double dose of the X signal elements activates the early promoter Pe of Sex-lethal; Sxl then maintains its own productive splicing (loop), directs the female splicing of transformer, and Tra with Tra2 gives the female Doublesex protein DsxF and female somatic development; Sxl also represses translation of msl-2, so that the X chromosomes are not hyperactivated. In XY embryos the single dose of the signal elements is too weak, no Sxl is made, Sxl and tra transcripts are spliced to include stop codons, dsx is spliced by default to the male form DsxM, and MSL-2 assembles the complex that doubles transcription of the single X](./plots/sxl-cascade.py)

The phenotypes of loss-of-function mutations follow from the cascade and order its genes by **epistasis** ([7.4.4](/7.4.4)):

| Mutation | XY phenotype | XX phenotype | Interpretation |
|---|---|---|---|
| *Sxl* | male | dies (no Sxl, so MSL complex forms and both X chromosomes are hyperactivated) | top of the hierarchy, also controls dosage compensation |
| *tra* | male | male (sterile) | needed only for female soma |
| *dsx* (null) | intersex | intersex | both DsxF and DsxM lost |
| *fru* | male with abnormal courtship | normal female | male-specific behavior |

The cascade is cell autonomous: each cell reads its own X chromosomes. Loss of one X from one nucleus of an early XX embryo (for example a ring X chromosome that is lost in mitosis) makes the descendants of that nucleus XO and male, and the fly becomes a mosaic of male and female tissue, often divided along the midline: a gynandromorph. Gynandromorphs were used by Sturtevant to locate the origin of tissues and behaviors in the embryo (fate mapping, [7.4.20](/7.4.20)); in birds, rare gynandromorph chickens (ZW/ZZ chimeras) showed that avian somatic cells, too, have a cell-autonomous sexual identity, rather than being directed only by hormones.

### 6.3.3. *Caenorhabditis elegans*

*C. elegans* has XX hermaphrodites, which make both sperm and eggs and fertilize themselves, and XO males. The X : autosome ratio is read by the gene *xol-1* (XO lethal), which is active in XO embryos and switches on the male program; in XX embryos X-linked signal elements repress it, and *xol-1* mutant XO embryos die because they activate the hermaphrodite program, including dosage compensation. Males arise from hermaphrodites by X-chromosome nondisjunction, in about $0.1$–$0.2\,\%$ of self-progeny; mutants with an increased frequency (*him*, high incidence of males) identify genes of meiotic pairing and crossing over.

## 6.4. Sex Linkage

### 6.4.1. X-Linked Genes

**Definition 6.4.1 (Sex Linkage, X-Linked and Y-Linked Genes)** **Sex linkage** is the inheritance of a gene located on a sex chromosome, whose transmission therefore differs between the sexes. A gene is **X-linked** if it lies on the X chromosome outside the pseudoautosomal regions, and **Y-linked** (holandric) if it lies in the male-specific region of the Y; in ZW species genes on the Z are Z-linked.

**Definition 6.4.2 (Hemizygous)** A diploid individual is **hemizygous** for a gene of which it has only one copy, such as an XY male for X-linked genes or a ZW female for Z-linked genes (and any individual for a gene in a region deleted from one homologue). A hemizygote shows the phenotype of its single allele, whether that allele is **dominant** or **recessive**.

In 1910 Thomas Hunt Morgan found a white-eyed male among red-eyed *Drosophila melanogaster*. Crossed to red-eyed females (cross A), it gave an all red-eyed $\mathrm{F}_1$; the $\mathrm{F}_1$ intercross (cross B) gave $3$ red : $1$ white in the $\mathrm{F}_2$, as for a recessive allele, but all the white-eyed flies were males, and red-eyed females outnumbered red-eyed males $2{:}1$. Morgan then obtained white-eyed females by crossing $\mathrm{F}_2$ red-eyed females to white-eyed males (cross C) and crossed them to wild-type males (cross D), which gave only red-eyed daughters and white-eyed sons. All four results follow if the gene, now called *white* ($w$; wild-type allele $w^{+}$), lies on the X and the Y carries no allele of it, so that males are hemizygous. We write genotypes with the alleles as superscripts on the X: $X^{+}X^{w}$, $X^{w}Y$.

**Definition 6.4.3 (Criss-Cross Inheritance)** **Criss-cross inheritance** is the pattern of an X-linked (or Z-linked) recessive trait in a cross between a homozygous recessive female and a hemizygous dominant male (or, for Z-linkage, a recessive male and a dominant female), in which every son shows the mother's phenotype and every daughter the father's, because sons receive their only X from the mother and daughters receive the father's X.

![Morgan's reciprocal crosses with the X-linked white gene (Punnett squares: sperm across the top, eggs down the left). A: a red-eyed female (X+X+) crossed to a white-eyed male (XwY) gives red-eyed heterozygous daughters (X+Xw) and red-eyed sons (X+Y). B: the reciprocal cross of a white-eyed female (XwXw) to a red-eyed male (X+Y) gives red-eyed daughters and white-eyed sons: criss-cross inheritance. That reciprocal crosses give different results is the signature of sex linkage](./plots/morgan-crosses.py)

The difference between **reciprocal crosses** is the operational test of sex linkage; for an autosomal gene reciprocal crosses give the same result ([7.4.2](/7.4.2)).

**Algorithm 6.4.1 (Solving X-Linked Crosses)**

1. Write each genotype with the X chromosomes and their alleles ($X^{A}X^{a}$, $X^{a}Y$); in ZW species write $Z^{A}W$ and $Z^{a}Z^{a}$.
2. Daughters receive the father's X and one of the mother's two X chromosomes; sons receive the Y from the father and one of the mother's X chromosomes. Hence the phenotypes of the sons are a direct sample of the mother's gametes, and every daughter of a father with a dominant X-linked allele carries it.
3. Compute the offspring classes separately for each sex (each sex is half of the progeny), and state ratios within sexes.
4. To decide whether a gene is X-linked, compare reciprocal crosses and look for sex-specific ratios in the $\mathrm{F}_1$ and $\mathrm{F}_2$.

**Example 6.4.1** In cross B, $X^{+}X^{w} \times X^{+}Y$: daughters are $\frac12 X^{+}X^{+} + \frac12 X^{+}X^{w}$, all red; sons are $\frac12 X^{+}Y + \frac12 X^{w}Y$, half white. Overall, red females : red males : white males $= 2 : 1 : 1$, which is Morgan's result. In cross C, $X^{+}X^{w} \times X^{w}Y$: in both sexes half red, half white, a $1{:}1{:}1{:}1$ ratio of the four sex–phenotype classes, which looks like an autosomal testcross; only cross D distinguishes X-linkage clearly.

### 6.4.2. Nondisjunction Proves the Chromosome Theory

Morgan's results showed that *white* is transmitted like the X, but they could not show that it is physically part of the X. Calvin Bridges (1916) found the proof in exceptions. In crosses of white-eyed females with red-eyed males (cross D), about 1 in 2000 progeny was exceptional: white-eyed females and red-eyed males.

**Definition 6.4.4 (Nondisjunction)** **Nondisjunction** is the failure of homologous chromosomes (in meiosis I) or of sister chromatids (in meiosis II or mitosis) to separate to opposite poles, so that one daughter cell receives both and the other neither. Nondisjunction in a normal diploid is primary nondisjunction; the regular production of aneuploid gametes by an individual whose own chromosome set is aneuploid (such as an XXY female) is secondary nondisjunction.

Bridges proposed that the exceptional females came from XX eggs produced by nondisjunction in the mother, fertilized by Y-bearing sperm, and the exceptional males from eggs with no X (O eggs) fertilized by X-bearing sperm. The hypothesis made three predictions, all confirmed: the exceptional white-eyed females were XXY in the microscope; the exceptional red-eyed males were XO and sterile; and the XXY females themselves produced a few percent of exceptional offspring again (secondary nondisjunction), because the three sex chromosomes pair as X–X (with a free Y) in most meioses but as X–Y in some, with the unpaired X joining the paired one. A gene's transmission followed a chromosome's behavior even when the chromosome misbehaved: this was the first proof that a specific gene lies on a specific chromosome.

![Bridges' proof of the chromosome theory. A: nondisjunction of the X chromosomes in meiosis I of a white-eyed (XwXw) female produces eggs with two X chromosomes (n + 1) and eggs with none (O, n − 1); nondisjunction in meiosis II (not shown) gives XX, O and two normal eggs. B: the exceptional eggs fertilized by sperm of a red-eyed male. XwXwY zygotes are white-eyed females (they received both X chromosomes from the mother and the Y from the father), X+O zygotes are red-eyed sterile males (their only X came from the father), and XXX and OY zygotes usually die. C: in an XXY female the two X chromosomes usually pair and disjoin, giving X and XY eggs, but sometimes X pairs with Y and the unpaired X goes to the same pole as its homologue, giving XX and Y eggs: secondary nondisjunction](./plots/bridges-nondisjunction.py)

**Formula 6.4.1 (Exceptional Progeny from Secondary Nondisjunction)** Let an $X^{w}X^{w}Y$ female be crossed to an $X^{+}Y$ male, and let a fraction $s$ of her meioses segregate the two X chromosomes to the same pole (giving $XX$ and $Y$ eggs, $s/2$ each); the remaining meioses give $X$ and $XY$ eggs ($(1 - s)/2$ each). Of the zygotes, $XXX$ (from $XX$ eggs and $X^{+}$ sperm, $s/4$) and $YY$ ($s/4$) die. The exceptional progeny, $X^{w}X^{w}Y$ white-eyed females and $X^{+}Y$ red-eyed males, make up $s/4 + s/4 = s/2$ of the zygotes, so among the surviving progeny their fraction is

$$
e = \frac{s/2}{1 - s/2} = \frac{s}{2 - s}, \qquad s = \frac{2e}{1 + e}.
$$

**Example 6.4.2** If $4.3\,\%$ of the progeny of $X^{w}X^{w}Y$ females are exceptional, then $s = 2(0.043)/1.043 \approx 0.082$: about 8 % of meioses in such females segregate the X chromosomes together. Compare primary nondisjunction, which in normal XX females occurs in roughly one meiosis in a thousand.

The same mechanisms produce human sex chromosome aneuploidies. About half of 47,XXY Klinefelter cases arise by nondisjunction in the father (in meiosis I, where X and Y must recombine in the short PAR1 to segregate properly), and half in the mother; 45,X usually results from loss of the paternal sex chromosome. The cell biology of nondisjunction and its maternal age dependence are discussed in [7.3.21](/7.3.21#sec-21.7.5), and the genetics of aneuploid syndromes in [7.4.16](/7.4.16).

### 6.4.3. X-Linked Traits in Humans

E. B. Wilson (1911) assigned the first human gene to a chromosome when he noticed that red-green color blindness passes from affected men through their unaffected daughters to half of their grandsons. The pedigree patterns of X-linked inheritance, and their use for recognizing a mode of inheritance, are tabulated in [7.4.7](/7.4.7#sec-7.2). Briefly: an X-linked recessive trait affects mostly males, is never transmitted from father to son, and passes from an affected man to all his daughters (obligate carriers) and through them to half of their sons; an X-linked dominant trait affects about twice as many females as males, and an affected man transmits it to all his daughters and none of his sons.

| Trait | Gene | Mode | Frequency |
|---|---|---|---|
| red-green color blindness | *OPN1LW*, *OPN1MW* (red and green opsins) | X-linked recessive | about 8 % of men of European ancestry, 0.5 % of women |
| hemophilia A | *F8* (clotting factor VIII) | X-linked recessive | 1 in 5 000 male births |
| Duchenne muscular dystrophy | *DMD* (dystrophin) | X-linked recessive, lethal before reproduction | 1 in 3 500–5 000 male births |
| G6PD deficiency | *G6PD* | X-linked recessive | common where malaria was endemic |
| hypophosphatemic rickets | *PHEX* | X-linked dominant | 1 in 20 000 |
| Rett syndrome | *MECP2* | X-linked dominant, almost always de novo, usually lethal in hemizygous males | 1 in 10 000 girls |

Y-linked traits should pass from father to all sons. Apart from male determination and fertility (deletions of the azoospermia factor regions of the Y cause infertility, so they are transmitted only when fertility is restored by assisted reproduction), no Y-linked trait is established in humans; the much cited "hairy ears" of some Indian families, once given as the example, was not confirmed by later studies and is probably not Y-linked.

**Formula 6.4.2 (Population Frequencies of X-Linked Phenotypes)** If an X-linked allele has frequency $q$ in both sexes and genotypes are in Hardy–Weinberg proportions (derived in [7.4.22](/7.4.22); used here as given), then hemizygous males are affected with frequency $q$, homozygous females with frequency $q^2$, and heterozygous (carrier) females have frequency $2pq$ with $p = 1 - q$. The ratio of affected females to affected males equals $q$, and carrier females are $2p \approx 2$ times as common as affected males.

**Example 6.4.3** If 8 % of men are color blind, a single allele with $q = 0.08$ would make $q^2 = 0.64\,\%$ of women color blind. The observed figure is lower, about $0.4$–$0.5\,\%$, because the 8 % comprise two different loci: protan defects (red opsin, about 2 % of men) and deutan defects (green opsin, about 6 %). A woman heterozygous for one protan and one deutan allele has normal color vision, because each of her X chromosomes carries one functional opsin gene of each kind: the alleles complement ([7.4.4](/7.4.4)). The predicted frequency of affected women is $0.02^2 + 0.06^2 = 0.04\,\%$ $+ 0.36\,\% = 0.40\,\%$, in agreement with observation.

### 6.4.4. Z-Linkage

In birds and Lepidoptera the inheritance is mirrored: males (ZZ) can be heterozygous, females (ZW) are hemizygous. The dominant Z-linked allele *B* gives barred plumage in chickens. Crossing a barred hen ($Z^{B}W$) with a nonbarred rooster ($Z^{b}Z^{b}$) gives barred sons ($Z^{B}Z^{b}$) and nonbarred daughters ($Z^{b}W$), criss-cross inheritance that allows day-old chicks to be sorted by sex by the color of their down (an autosexing cross).

### 6.4.5. Sex-Limited and Sex-Influenced Traits

Not all differences in inheritance between the sexes come from sex chromosomes.

**Definition 6.4.5 (Sex-Limited and Sex-Influenced Traits)** A **sex-limited trait** is a trait expressed in only one sex, although the genes affecting it may be present and transmitted in both, usually because the trait depends on an anatomical structure or a hormonal environment of that sex. A **sex-influenced trait** is a trait expressed in both sexes but with a different dominance relation or penetrance in each, so that the same genotype has different phenotypes in males and females.

Examples of sex-limited traits are milk yield in cattle (bulls carry and transmit genes for it), and hen feathering in chickens: males of genotype $H\_$ have the short, rounded feathers of hens and $hh$ males the long, pointed feathers of cocks, whereas all females are hen-feathered whatever their genotype (the $H$ allele increases the conversion of androgens to estrogens in the skin). Complete androgen insensitivity is an X-linked sex-limited condition, expressed only in XY individuals. Horns in some sheep breeds are sex-influenced: crossing horned (Dorset) and hornless (Suffolk) breeds gives horned males and hornless females in the $\mathrm{F}_1$, and $3$ horned : $1$ hornless males but $1$ horned : $3$ hornless females in the $\mathrm{F}_2$, as expected if the horned allele is dominant in males and recessive in females. Male pattern baldness is often cited as an autosomal sex-influenced trait; in fact it is polygenic, with its largest single effect at the X-linked *AR* locus, so family patterns are only approximately Mendelian.

**Example 6.4.4** In a sheep population with frequency $p$ of the horned allele $H$ (dominant in males, recessive in females) and Hardy–Weinberg proportions, the fraction of horned males is $p^2 + 2pq$ and of horned females $p^2$. If 75 % of males are horned, $q^2 = 0.25$, so $q = 0.5$ and $p = 0.5$, and $p^2 = 25\,\%$ of females are horned.

## 6.5. Dosage Compensation

**Definition 6.5.1 (Dosage Compensation)** **Dosage compensation** is any mechanism that equalizes the expression of genes on the sex chromosomes between the sex with two copies of a sex chromosome and the sex with one, and that balances the expression of these genes against that of autosomal genes.

Sex chromosomes create a dosage problem in two directions: between the sexes (two X chromosomes against one) and, in the heterogametic sex, between the single X and the two sets of autosomes. Most genes tolerate a twofold change in dose poorly when many of them change at once (an entire chromosome), which is why autosomal monosomies are lethal ([7.4.16](/7.4.16)). Organisms have solved the problem in at least four ways:

| Organism | Strategy | Mechanism |
|---|---|---|
| mammals | inactivate all but one X in each female cell; the active X is upregulated in both sexes | *XIST* long noncoding RNA, Polycomb, DNA methylation ([7.3.17](/7.3.17#sec-17.1.3)) |
| *Drosophila* | double transcription of the single male X | MSL complex with the roX noncoding RNAs, acetylation of histone H4 at Lys16 |
| *C. elegans* | halve expression from each of the two X chromosomes of hermaphrodites | a condensin-like dosage compensation complex |
| birds, Lepidoptera | partial, gene-by-gene compensation; Z genes are expressed about 1.5 times higher in ZZ males | local regulation |

The diversity shows that dosage compensation evolved independently each time a pair of sex chromosomes arose.

### 6.5.1. Genetic Consequences of X Inactivation

Mary Lyon's hypothesis (1961), confirmed in every detail ([7.3.17](/7.3.17#sec-17.1.3)), has four consequences for genetics.

1. Counting. A cell keeps one X active and inactivates the rest, so the number of **Barr bodies** is $n_X - 1$: none in 45,X and normal 46,XY cells, one in 46,XX and 47,XXY, two in 47,XXX and 48,XXXY. The phenotypes of sex chromosome aneuploids are mild compared with autosomal aneuploidies for this reason; they are not absent, because genes in the pseudoautosomal regions and about 15 % of other X-linked genes escape inactivation and are expressed from every X. A 45,X individual thus has one dose of *SHOX* and of other escape genes instead of two, and 47,XXY three.
2. Mosaicism. Inactivation is random and clonally inherited, so a woman heterozygous for an X-linked gene is a mosaic of patches of cells expressing one allele or the other. Calico and tortoiseshell cats are heterozygous at the X-linked *Orange* locus; a male calico cat is almost always XXY (or a chimera), and is sterile. Women heterozygous for anhidrotic ectodermal dysplasia have patches of skin without sweat glands. A tumor that expresses only one allele of a heterozygous X-linked marker (such as one isoform of G6PD) must descend from a single cell: this was the first evidence of the clonal origin of cancers ([7.4.21](/7.4.21)).
3. Variable expression in carriers. Because the proportion of cells that silenced the normal allele varies by chance, heterozygous carriers of X-linked recessive diseases range from unaffected to (rarely) as severely affected as males.
4. Transmission is unaffected. The inactive X is reactivated in the female germline, so the alleles a woman transmits follow Mendel's rules, whichever X was inactive in her soma.

**Definition 6.5.2 (Manifesting Heterozygote)** A **manifesting heterozygote** (manifesting carrier) is a female heterozygous for an X-linked recessive allele who shows signs of the disease, usually because, by chance or by selection, the X chromosome carrying the normal allele is inactive in most cells of the affected tissue.

**Formula 6.5.1 (Probability of Manifestation)** Under the model of [Proposition 17.1.1](/7.3.17#prop-17.1.1), a tissue derived from $n$ precursor cells that inactivated independently has a fraction $F$ of cells with the normal allele active, where $nF \sim \mathrm{Bin}(n, 1/2)$. If the tissue fails when $F$ falls below a threshold $t$, the probability that a carrier manifests is

$$
\mathbb{P}(F < t) = \sum_{k < nt} \binom{n}{k} 2^{-n}.
$$
If mutant-expressing clones grow to only a fraction $1 - s$ of the size of normal clones, then $F = k/[k + (n - k)(1 - s)]$ for $k$ normal precursors, which raises $F$ and lowers the probability of manifestation.

**Example 6.5.1** For $t = 0.3$ the probability is $0.145$ for $n = 8$, $0.038$ for $n = 16$ and $0.010$ for $n = 32$; for $t = 0.2$ it is $0.035$, $0.011$ and $0.0003$. Clinical estimates that roughly 2–8 % of female carriers of Duchenne muscular dystrophy show muscle weakness are of the order expected for a few tens of precursors and a threshold near one third of normal dystrophin-expressing nuclei. Selection can act in either direction: in carriers of mutations that impair cell survival, such as in the genes for some immunodeficiencies, the cells expressing the mutant X are lost and inactivation in blood becomes completely skewed in favor of the normal allele, which is used as a carrier test.

![Chance alone makes some carriers manifest an X-linked recessive disease. A: probability that fewer than a fraction t of the cells of a tissue express the normal allele, when the tissue descends from n precursors that each inactivated one X at random (Formula 6.5.1), for thresholds t = 0.1, 0.2 and 0.3; the probability falls roughly exponentially with n, with a sawtooth caused by the discreteness of the number of precursors. B: the same when clones expressing the mutant allele grow less (to 70 % of the size of normal clones): selection against mutant cells protects carriers](./plots/manifesting-carriers.py)

## Summary

| System | Heterogametic sex | Decisive signal | Key genes |
|---|---|---|---|
| mammals XX/XY | male | presence of Y | *SRY* → *SOX9* → testis → hormones |
| *Drosophila* XX/XY | male | X dose | X signal elements → *Sxl* (feedback) → *tra* → *dsx*, *fru*; Sxl ⊣ *msl-2* |
| *C. elegans* XX/XO | male | X : A ratio | *xol-1* |
| birds ZW/ZZ | female | Z dose | *DMRT1* |
| honey bee | none (haplodiploid) | heterozygosity at *csd* | *csd* → *fem* → *dsx* |
| turtles | none | temperature | *Kdm6b* → *Dmrt1* |

- Definitions: sex chromosome, heterogametic and homogametic sex (Definition 6.1.1), sex determination (Definition 6.1.2), pseudoautosomal region (Definition 6.2.1), sex linkage, X- and Y-linkage (Definition 6.4.1), hemizygosity (Definition 6.4.2), criss-cross inheritance (Definition 6.4.3), nondisjunction (Definition 6.4.4), sex-limited and sex-influenced traits (Definition 6.4.5), dosage compensation (Definition 6.5.1), manifesting heterozygote (Definition 6.5.2).
- Formulas: diploid males under complementary sex determination $1/k$ (random mating), about $1/4$ (brother–sister) (Formula 6.1.1); logistic temperature reaction norm (Formula 6.1.2); recombination of a PAR1 locus with sex $r = d/(2L)$ (Formula 6.2.1); exceptional progeny from secondary nondisjunction $e = s/(2 - s)$ (Formula 6.4.1); X-linked recessive phenotypes $q$ in males, $q^2$ in females, carriers $2pq$ (Formula 6.4.2); probability of manifestation from random X inactivation (Formula 6.5.1).
- X-linked crosses (Algorithm 6.4.1): sons show the mother's alleles; daughters receive the father's X; reciprocal crosses differ. Morgan's *white* showed X-linkage; Bridges' exceptional XXY females and XO males proved the chromosome theory.
- Population genetics of sex linkage: female to male ratio of an X-linked recessive phenotype equals $q$; allelic heterogeneity (protan and deutan) lowers the frequency in women (Example 6.4.3).
- X inactivation: Barr bodies $= n_X - 1$; escape genes and PAR genes explain the phenotypes of sex chromosome aneuploidies; random and clonal choice makes heterozygous females mosaics; chance or selection skews it.

## Questions

1. A red-eyed female *Drosophila* crossed with a white-eyed male produces 50 red-eyed females, 49 white-eyed females, 51 red-eyed males and 50 white-eyed males. What were the parental genotypes? Which reciprocal cross would confirm X-linkage?

   **Answer** White-eyed daughters must have received $X^{w}$ from both parents, so the mother is $X^{+}X^{w}$ and the father $X^{w}Y$; the cross gives $1{:}1$ red : white in both sexes. This looks like an autosomal testcross. The confirming cross is white-eyed female ($X^{w}X^{w}$) × red-eyed male ($X^{+}Y$): with X-linkage all daughters are red-eyed and all sons white-eyed (criss-cross inheritance), whereas an autosomal gene would give all red-eyed progeny of both sexes.
2. A woman whose father has hemophilia A marries an unaffected man. What is the probability that (a) their first child is a hemophilic son, (b) their first son is hemophilic, (c) a daughter is a carrier?

   **Answer** The woman is an obligate carrier ($X^{\mathsf H}X^{h}$). (a) The child is a son with probability $1/2$ and a son receives $X^{h}$ with probability $1/2$: $1/4$. (b) Given a son: $1/2$. (c) A daughter receives $X^{h}$ from her mother with probability $1/2$ (and $X^{\mathsf H}$ from her father): $1/2$.
3. In a population, 1 in 10 000 male births has an X-linked recessive disease. Assuming Hardy–Weinberg proportions, what fraction of women are carriers, and what fraction affected? What is the ratio of carrier women to affected men?

   **Answer** $q = 10^{-4}$. Carriers $2pq \approx 2\times10^{-4}$, i.e. 1 in 5 000 women; affected women $q^2 = 10^{-8}$. Carrier women are about twice as frequent as affected men ($2p \approx 2$).
4. A barred rooster is crossed to a nonbarred hen; all $\mathrm{F}_1$ are barred. In the $\mathrm{F}_2$, all males are barred and half of the females are barred. Give the genotypes and explain why the reciprocal cross can be used to sex chicks.

   **Answer** Barring is Z-linked and dominant. P: $Z^{B}Z^{B}$ rooster × $Z^{b}W$ hen; $\mathrm{F}_1$: $Z^{B}Z^{b}$ males and $Z^{B}W$ females, all barred. $\mathrm{F}_2$: males $Z^{B}Z^{B}$ and $Z^{B}Z^{b}$ (all barred), females $Z^{B}W$ and $Z^{b}W$ (half barred). In the reciprocal cross, nonbarred rooster ($Z^{b}Z^{b}$) × barred hen ($Z^{B}W$), every son is $Z^{B}Z^{b}$ (barred) and every daughter $Z^{b}W$ (nonbarred), so the sex of each chick can be read from its phenotype.
5. Using Formula 6.2.1 with $L = 2.7\,\mathrm{Mb}$, at what distance from the pseudoautosomal boundary would a PAR1 locus show 10 % recombination with sex in male meiosis? Why are female recombination rates in PAR1 much lower than male ones?

   **Answer** $d = 2Lr = 2(2.7)(0.10) = 0.54\,\mathrm{Mb}$ from the boundary. In female meiosis the two X chromosomes pair along their whole length and PAR1 is only a small part of a long bivalent, which needs only one or a few crossovers anywhere; there is no obligatory crossover in PAR1, so its female genetic length (a few cM) is close to the genome average for $2.7\,\mathrm{Mb}$, whereas in males the obligatory X–Y crossover must fall within it.
6. A honey bee population has 12 *csd* alleles at equal frequencies. (a) What fraction of a randomly mated queen's diploid offspring are diploid males? (b) If a queen mates with 15 drones, does the expected fraction change? (c) In a population that has lost alleles through a bottleneck to $k = 4$, what fraction is expected?

   **Answer** (a) $1/12 \approx 8.3\,\%$. (b) No: each drone independently matches one of the queen's two alleles with probability $2/k$, so the expected fraction remains $1/k$; multiple mating only reduces the variation between colonies. (c) $1/4 = 25\,\%$, the same as brother–sister mating in a large population, a substantial loss of brood that makes small bee populations vulnerable.
7. In Bridges' experiments, white-eyed $X^{w}X^{w}Y$ females crossed to red-eyed males gave 4 % exceptional progeny among the survivors. Estimate the fraction of their meioses in which the two X chromosomes went to the same pole, and list the four kinds of eggs with their frequencies.

   **Answer** $s = 2e/(1 + e) = 0.08/1.04 \approx 0.077$. Eggs: $X^{w}X^{w}$ and $Y$ about $3.8\,\%$ each; $X^{w}$ and $X^{w}Y$ about $46.2\,\%$ each.
8. A man with red-green color blindness and a woman with normal vision whose father was color blind have a daughter with Turner syndrome (45,X) who is color blind. In which parent did the nondisjunction (or chromosome loss) occur? What if the daughter had normal vision?

   **Answer** The mother is a carrier ($X^{C}X^{c}$), the father $X^{c}Y$. A color-blind 45,X daughter has a single $X^{c}$, which could have come from either parent, so color vision does not decide; molecular markers would be needed. If she had normal vision, her single X must carry $C$, which only the mother has: the X is maternal, and the error (loss of the sex chromosome) occurred in the father's gamete or in an early mitosis, losing the paternal X or Y.
9. How many Barr bodies are present in the cells of individuals with the karyotypes 45,X; 46,XY; 47,XXY; 48,XXXY; 49,XXXXY? Why are their phenotypes nevertheless abnormal?

   **Answer** $n_X - 1$: 0, 0, 1, 2, 3. Genes in the pseudoautosomal regions and about 15 % of other X-linked genes escape inactivation, so each extra X adds a dose of these genes (and 45,X lacks one); in addition, inactivation takes some time in early development, during which all X chromosomes are active.
10. Using Formula 6.5.1, compute the probability that a DMD carrier has fewer than 30 % of muscle precursors expressing the normal allele if $n = 10$. How does the answer change if mutant precursors' clones grow to only 80 % of the size of normal clones?

    **Answer** With random inactivation, $F = k/10 < 0.3$ requires $k \le 2$: $\mathbb{P} = (1 + 10 + 45)/1024 = 56/1024 \approx 0.055$. With selection ($s = 0.2$), $F = k/[k + 0.8(10 - k)]$: $k = 2$ gives $2/(2 + 6.4) = 0.24$, $k = 3$ gives $3/(3 + 5.6) = 0.35$, so still $k \le 2$ and $\mathbb{P} \approx 0.055$. Selection of this strength does not change the answer for $n = 10$, because of the discreteness; it matters when $n$ is larger or the selection stronger.
11. In sheep, the allele $H$ for horns is dominant in males and recessive in females. A hornless ram is mated with a horned ewe. What are the phenotypes of their sons and daughters? In the $\mathrm{F}_2$ from intercrossing them?

    **Answer** The hornless ram must be $hh$ and the horned ewe $HH$. All $\mathrm{F}_1$ are $Hh$: sons horned, daughters hornless (a pattern that mimics criss-cross inheritance). $\mathrm{F}_2$: $\frac14 HH$, $\frac12 Hh$, $\frac14 hh$; males $3$ horned : $1$ hornless, females $1$ horned : $3$ hornless.
12. Explain why XX *Sxl* loss-of-function mutants die but XY *Sxl* mutants are normal males, whereas XX *tra* mutants are viable sterile males.

    **Answer** Sxl has two targets: it promotes female splicing of *tra* (sex) and represses translation of *msl-2* (dosage compensation). Without Sxl, XX animals assemble the MSL complex and hyperactivate both X chromosomes, a fourfold X dose relative to the autosomes, which is lethal. XY animals make no Sxl anyway, so the mutation has no effect. Tra acts only on sex: XX *tra* mutants still make Sxl, so their dosage compensation is female (no hyperactivation), but their soma follows the male default (*dsx* male splicing), giving pseudomales that are sterile because their germ cells are XX.
13. (Comprehensive) The maize genotypes $Ba\_\,Ts\_$ are monoecious, $ba\,ba\,Ts\_$ male, and $Ba\_\,ts\,ts$ and $ba\,ba\,ts\,ts$ female. (a) What ratio of sexes is produced by crossing a $ba\,ba\,ts\,ts$ female with a $ba\,ba\,Ts\,ts$ male? (b) What results from self-pollinating a monoecious $Ba\,ba\,Ts\,ts$ plant?

    **Answer** (a) All progeny are $ba\,ba$; half are $Ts\,ts$ (male) and half $ts\,ts$ (female): $1{:}1$, a stable system in which $ts$ plays the role of X and $Ts$ of Y. (b) With independent assortment, $\frac{9}{16}$ $Ba\_\,Ts\_$ monoecious, $\frac{3}{16}$ $ba\,ba\,Ts\_$ male, and $\frac{3}{16} + \frac{1}{16} = \frac{4}{16}$ female: $9{:}3{:}4$, a recessive-epistasis ratio ([7.4.4](/7.4.4)), because $ts\,ts$ masks the effect of $ba$.
