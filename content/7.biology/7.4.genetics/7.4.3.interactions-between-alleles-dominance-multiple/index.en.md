---
title: "Interactions Between Alleles: Dominance, Multiple Alleles and Lethality"
description: Complete and incomplete dominance and codominance, and a dominance index; why dominance depends on the level of observation (sickle-cell hemoglobin); the metabolic explanation of recessiveness and haploinsufficiency; multiple alleles, allelic series and the ABO system; wild-type, mutant and polymorphic alleles; lethal alleles and the 2:1 ratio as a conditional probability; pleiotropy; penetrance, expressivity, modifier genes, conditional alleles, phenocopies and norms of reaction, with the corresponding risk calculations.
---

Mendel's seven **genes** each had two **alleles**, one completely **dominant**, and every **genotype** had one predictable **phenotype**. These were fortunate choices. Most genes have many alleles, **heterozygotes** are often intermediate or show both parental forms, some alleles kill their carriers, a single gene can affect many traits, and the same genotype can give different phenotypes in different individuals or environments. None of this contradicts the **law of segregation**: alleles still segregate 1:1 in gametes and combine at random. What changes is the mapping from genotype to phenotype, and with it the ratios observed. This chapter treats the interactions between the alleles of one gene, and the next (7.4.4) the interactions between genes.

The explanations are often molecular, and they draw on earlier courses: the kinetics of pathways and **metabolic control analysis** ([7.1.17](/7.1.17#sec-17.4)) explain why most loss-of-function alleles are **recessive**; hemoglobin S ([7.1.7](/7.1.7)) shows that dominance depends on the level at which a phenotype is observed; glycosyltransferases build the ABO **antigens** ([7.3.9](/7.3.9)). The calculations are the conditional probabilities of 7.4.2: lethality and incomplete penetrance both change ratios by removing or hiding part of the expected progeny.

## 3.1. Dominance Relations

### 3.1.1. Complete Dominance, Incomplete Dominance and Codominance

**Definition 3.1.1 (Dominance Relations)** Let a **locus** have **alleles** $A_1$ and $A_2$. With respect to a given **phenotype**:

- $A_1$ shows **complete dominance** over $A_2$ if the **heterozygote** $A_1A_2$ has the same phenotype as the **homozygote** $A_1A_1$;
- the alleles show **incomplete dominance** (partial **dominance**, semidominance) if the heterozygote's phenotype is intermediate between those of the two homozygotes;
- the alleles show **codominance** if the heterozygote shows the phenotypes of both homozygotes at once, because both allelic products are present and each is detected.

For a measurable phenotype the three cases can be placed on one scale.

**Formula 3.1.1 (Dominance Index)** If the mean phenotypes of $A_1A_1$, $A_1A_2$ and $A_2A_2$ are $z_{11}$, $z_{12}$ and $z_{22}$ with $z_{11} \ne z_{22}$, the dominance index of $A_1$ is

$$
h = \frac{z_{12} - z_{22}}{z_{11} - z_{22}} .
$$

$h = 1$: $A_1$ is completely dominant; $h = 0$: $A_1$ is completely **recessive**; $0 < h < 1$: incomplete dominance ($h = 1/2$: the heterozygote is exactly intermediate, the additive case); $h > 1$ or $h < 0$: overdominance or underdominance (the heterozygote lies outside the range of the homozygotes, 7.4.23). Quantitative genetics uses the equivalent ratio $d/a = 2h - 1$ (7.4.24).

Codominance does not fit on this scale: it is a statement that both allelic products are distinguishable in the heterozygote, not that its value is intermediate.

**Example 3.1.1 (Incomplete dominance)** In snapdragons (*Antirrhinum majus*), **true-breeding** red and white lines give pink $\mathrm{F}_1$ plants. The red allele $A$ makes an **enzyme** of anthocyanin synthesis, the white allele none; the heterozygote makes about half as much pigment, and with this pathway the flower color is proportional to the amount. Because each **genotype** has its own phenotype, the $\mathrm{F}_2$ phenotypic ratio equals the genotypic ratio 1:2:1. An $\mathrm{F}_2$ of 112 red, 229 pink and 105 white ($n = 446$; expected $111.5$, $223$, $111.5$) gives $\chi^2 = 0.002 + 0.161 + 0.379 = 0.54$ with two degrees of freedom ($p = 0.76$). Incomplete dominance is convenient for analysis: every genotype can be read from the phenotype, and no **testcross** is needed.

**Example 3.1.2 (Codominance)** The human MN blood group is determined by two alleles, $L^M$ and $L^N$, of the **gene** for glycophorin A, a red-cell surface **glycoprotein**; the two allelic **proteins** differ at two amino acids near their N terminus. Antibodies distinguish them: $L^ML^M$ people are type M, $L^NL^N$ type N, and heterozygotes have both proteins on their cells and are type MN. Molecular markers are almost always codominant: in a gel, the two alleles of an enzyme (allozymes, which differ in charge and therefore in electrophoretic mobility), of a **microsatellite** or of a single-nucleotide polymorphism appear as separate bands or signals, and the heterozygote shows both. This is why they are so useful for mapping (7.4.14).

**Example 3.1.3 (Mosaic dominance)** The Asian lady beetle *Harmonia axyridis* has many elytral color forms, from black with two or four red spots to red with up to nineteen black spots, determined by a series of alleles at one locus. C. C. Tan (Tan Jiazhen) showed in 1946 that in heterozygotes each region of the elytron is black if it is black in either homozygote: the heterozygote's pattern is the superposition of the two parental patterns, each allele being dominant in the areas where it produces melanin. He called this *mosaic dominance*; the $\mathrm{F}_2$ of two forms is $1 : 2 : 1$, the heterozygote being a third, recognizable pattern. The locus is the transcription-factor gene *pannier*, and the alleles differ in its regulatory region, which determines where on the elytron it is expressed and melanin is made (Ando and colleagues, 2018). Mosaic dominance is codominance in space: both alleles act, each in its own part of the body.

| Relation | $\mathrm{F}_1$ phenotype | $\mathrm{F}_2$ phenotypic ratio | Example |
|---|---|---|---|
| complete dominance | that of one parent | 3:1 | Mendel's pea traits |
| incomplete dominance | intermediate | 1:2:1 | snapdragon flower color |
| codominance | both parental products detectable | 1:2:1 | MN blood group, $I^AI^B$ |
| mosaic dominance | each parental pattern in different parts | 1:2:1 | elytral patterns of *Harmonia axyridis* |

### 3.1.2. Dominance Depends on the Level of Observation

Dominance is a relation between two alleles with respect to a particular phenotype, and one pair of alleles can be dominant, recessive, incompletely dominant and codominant at once, depending on which phenotype is observed. The classic example is **sickle cell anemia** ([7.1.7](/7.1.7)). The allele $Hb\beta^{S}$ of the β-globin gene *HBB* has one base change that replaces glutamate 6 by valine; deoxygenated hemoglobin S polymerizes into fibers that distort red cells into sickle shapes.

| Mosaic dominance (Example 3.1.3) | heterozygote shows each parental pattern in different body regions (*Harmonia axyridis*, *pannier*); $\mathrm{F}_2$ 1:2:1 | |
| Level of observation | $Hb\beta^{A}/Hb\beta^{A}$ | $Hb\beta^{A}/Hb\beta^{S}$ | $Hb\beta^{S}/Hb\beta^{S}$ | Relation of $Hb\beta^{S}$ to $Hb\beta^{A}$ |
|---|---|---|---|---|
| β-globin polypeptides (electrophoresis) | A only | A and S | S only | codominant |
| Red-cell shape at sea level | normal | normal | sickled | recessive |
| Red-cell shape at low oxygen (high altitude, exertion) | normal | some cells sickle | severe sickling | incompletely dominant |
| Anemia | none | none (at sea level) | severe | recessive |
| Resistance to *Plasmodium falciparum* malaria | susceptible | resistant | resistant (but ill) | dominant |

![Dominance of the sickle-cell allele at different levels of observation. Columns: the three genotypes of the β-globin gene. Rows, from the molecule to the organism: hemoglobin polypeptides (both A and S are present in heterozygotes, codominance); red cells under normal and low oxygen (sickling in the homozygote only, or partly in the heterozygote at low oxygen); anemia (recessive); and resistance to *P. falciparum* malaria, which heterozygotes share with homozygotes (dominant). The same pair of alleles is codominant, recessive, incompletely dominant or dominant depending on the phenotype considered](./plots/sickle-cell-levels.py)

The malaria row explains why a lethal recessive allele is common in parts of Africa, the Mediterranean and South Asia: heterozygotes are protected (parasites grow poorly in their red cells, and infected cells sickle and are removed), so the heterozygote has the highest fitness, and the allele is maintained by balancing selection (7.4.23).

Dominance can also depend on the internal environment of the organism. In a **sex-influenced trait** the same heterozygote has different phenotypes in the two sexes: the allele for horns in some sheep breeds is dominant in rams and recessive in ewes, because the hormonal environment changes its expression ([7.4.6](/7.4.6#sec-6.4.5)). Dominance that changes with sex, age or external conditions is sometimes called conditional dominance.

## 3.2. Why Most Loss-of-Function Alleles Are Recessive

### 3.2.1. The Metabolic Explanation

Most mutant **alleles** that destroy the function of an **enzyme** are **recessive**: Mendel's $r$, $i$, $a$ and $le$ (7.4.2), albinism, **phenylketonuria**, cystic fibrosis. **Heterozygotes** have half the amount of active enzyme, so half the enzyme must usually be nearly as good as all of it. Kacser and Burns (1981) showed that this follows from the kinetics of pathways and does not need a special evolutionary explanation, as R. A. Fisher had proposed.

**Formula 3.2.1 (Flux Through a Pathway)** In the simplest model of a linear pathway $X_0 \to S_1 \to \cdots \to X_n$, in which each enzyme works far from saturation, the steps behave like resistances in series: with $E_i$ the amount of enzyme $i$ and $k_i$ its effective first-order rate constant, the steady-state flux is

$$
J = \frac{D}{\displaystyle\sum_{i=1}^{n} \frac{1}{k_i E_i}},
$$

where the driving term $D$ is fixed by the concentrations of the source $X_0$ and the sink $X_n$ and by the equilibrium constants of the steps. Viewed as a function of the amount $E$ of one enzyme, with the resistance $R$ of all the other steps fixed, $J = D/(1/(kE) + R)$, which has the form

$$
J(E) = J_{\max}\,\frac{E}{E + K_E}, \qquad J_{\max} = \frac{D}{R}, \quad K_E = \frac{1}{kR},
$$

where $J_{\max}$ is the flux with that enzyme in excess. The **flux control coefficient** of the enzyme is

$$
C^J_E = \frac{\partial \ln J}{\partial \ln E} = \frac{K_E}{E + K_E}.
$$

The hyperbolic form is the key. If the **wild-type** amount $E = 1$ is large compared with $K_E$, the flux is already close to $J_{\max}$, and halving the enzyme lowers it little. The **flux control coefficient** of a single enzyme is then small, and it has to be: by the summation theorem ([7.1.17](/7.1.17#sec-17.4.2)) the control coefficients of all the enzymes of a pathway sum to one, so in a pathway of many enzymes most of them have small coefficients.

**Example 3.2.1** Take $K_E = 0.05$ for an enzyme whose wild-type **homozygous** amount is $E = 1$. Then

$$
\frac{J(0.5)}{J(1)} = \frac{0.5/(0.5 + 0.05)}{1/(1 + 0.05)} = \frac{0.909}{0.952} = 0.955,
$$

so the heterozygote has 95.5 % of the wild-type flux, and if the **phenotype** depends on the flux (the amount of pigment, of a product) it is indistinguishable from the wild type: the null allele is recessive. The flux control coefficient at the wild-type amount is $C = 0.05/1.05 = 0.048$. For the heterozygote to retain only 90 % of the flux, $0.5(1 + K_E)/(0.5 + K_E) = 0.9$, which gives $K_E = 0.125$ and $C = 0.11$. An enzyme with a large control coefficient, $K_E = 1$ ($C = 0.5$), gives $J(0.5)/J(1) = 0.67$: the heterozygote is intermediate.

![Why loss of function is usually recessive. Flux through a pathway as a function of the amount of one enzyme (relative to the wild-type homozygote, E = 1), J(E) = Jmax E/(E + K_E), for an enzyme with little control of the flux (K_E = 0.05, upper curve) and one with much control (K_E = 1, lower curve). Circles mark the homozygous wild type (E = 1), the heterozygote for a null allele (E = 0.5) and the homozygous mutant (E = 0). With low control the heterozygote has almost full flux and the null allele is recessive; with high control the heterozygote is intermediate (incomplete dominance, or haploinsufficiency if the phenotype has a threshold)](./plots/flux-dominance.py)

### 3.2.2. Haploinsufficiency

**Definition 3.2.1 (Haploinsufficiency)** A **gene** shows **haploinsufficiency** if one functional copy is not enough for the wild-type phenotype, so that a loss-of-function allele is **dominant** (or incompletely dominant) in the heterozygote.

Haploinsufficient genes are the exceptions that the metabolic argument predicts: products whose amount matters directly rather than through a saturating flux. They include **transcription** factors whose targets respond to their concentration (*PAX6*: heterozygotes have aniridia, a reduced iris; *TBX5*: heart and upper-limb defects of Holt–Oram syndrome), structural **proteins** and components of complexes that must be made in a fixed ratio (**elastin**, *ELN*, in supravalvular aortic stenosis; ribosomal proteins in Diamond–Blackfan anemia), and signaling components set near a threshold. Large-scale analyses suggest that a few thousand human genes are intolerant of heterozygous loss of function. Dominant alleles of other kinds, gain-of-function and dominant-negative **mutations**, are treated with the classification of mutations in 7.4.12.

## 3.3. Multiple Alleles

### 3.3.1. Allelic Series

**Definition 3.3.1 (Multiple Alleles)** A **gene** with more than two **alleles** in a population has **multiple alleles**. Each **diploid** individual carries at most two of them. When the alleles can be arranged so that each is **dominant** over those after it, they form an **allelic series** (dominance series), written with $>$.

**Formula 3.3.1 (Number of Genotypes)** A **locus** with $k$ alleles in a diploid has $k$ **homozygous** and $\binom{k}{2} = k(k-1)/2$ **heterozygous** **genotypes**, in total

$$
\frac{k(k+1)}{2}.
$$

If the alleles form a complete dominance series, there are only $k$ **phenotypes**; with codominance between some pairs there are more.

**Example 3.3.1 (Coat color in rabbits)** The *C* gene, which encodes tyrosinase, the first **enzyme** of melanin synthesis, has four alleles in domestic rabbits: $c^{+}$ (full color), $c^{ch}$ (chinchilla: gray hairs, less pheomelanin), $c^{h}$ (Himalayan: white body with dark extremities) and $c$ (albino). Their dominance relations are $c^{+} > c^{ch} > c^{h} > c$, but the series is not entirely clean: $c^{ch}$ is only partially dominant over $c^{h}$ and $c$ (the heterozygotes are lighter than $c^{ch}c^{ch}$). With 4 alleles there are $4 \times 5/2 = 10$ genotypes. The Himalayan allele encodes a temperature-sensitive tyrosinase (3.5.3). The order of the series reflects the amount of enzyme activity: an allele with more activity is dominant over one with less, as Formula 3.2.1 predicts.

### 3.3.2. The ABO Blood Groups

The ABO system shows multiple alleles, codominance and complete dominance in one gene, and it has a clear biochemical explanation. The **antigens** are carbohydrates on red-cell **glycoproteins** and **glycolipids**, built by glycosyltransferases in the **Golgi apparatus** ([7.3.9](/7.3.9)).

1. A fucosyltransferase encoded by *FUT1* (the *H* gene) adds fucose to a precursor chain, making the H antigen.
2. The *ABO* gene encodes a glycosyltransferase that adds one more sugar to the H antigen. The allele $I^{A}$ encodes an enzyme that adds N-acetylgalactosamine (giving the A antigen); $I^{B}$ encodes an enzyme that differs from it at four amino acids, of which two determine its specificity for galactose (giving the B antigen); and $i$ (also called $O$) has a single-base deletion near the start of the coding region that shifts the **reading frame**, so no active enzyme is made and the H antigen remains unmodified.

![Biosynthesis of the ABO antigens. The FUT1 fucosyltransferase (H gene) adds fucose to the precursor chain to form the H antigen; the glycosyltransferase encoded by the I^A allele of ABO adds N-acetylgalactosamine to form the A antigen, and the I^B enzyme adds galactose to form the B antigen; the i (O) allele makes no active enzyme, so H remains. I^A I^B heterozygotes make both A and B antigens (codominance); I^A i and I^B i make one (complete dominance over i). People homozygous for loss of FUT1 (hh) make no H antigen and therefore neither A nor B, whatever their ABO genotype: the Bombay phenotype (7.4.4)](./plots/abo-pathway.py)

| Genotype | Antigens on red cells | Blood type | Antibodies in plasma |
|---|---|---|---|
| $I^AI^A$, $I^Ai$ | A | A | anti-B |
| $I^BI^B$, $I^Bi$ | B | B | anti-A |
| $I^AI^B$ | A and B | AB | none |
| $ii$ | H only | O | anti-A and anti-B |

$I^A$ and $I^B$ are codominant with each other and both are completely dominant over $i$: the three alleles give $3 \times 4/2 = 6$ genotypes and 4 phenotypes. People have antibodies against the A or B antigens they lack (formed early in life in response to similar carbohydrates on gut bacteria), so transfused cells carrying a foreign antigen are agglutinated and destroyed. Type O cells (no A, no B) can be given to anyone in emergencies; type AB recipients can accept cells of any ABO type.

**Example 3.3.2** (a) Parents of types A and B, both heterozygous ($I^Ai \times I^Bi$), have children of types AB, A, B and O with probability $1/4$ each. (b) A type O mother has a type AB child. The child received $i$ from the mother, so it cannot be AB: either the mother is not $ii$ (a Bombay phenotype that only looks like O, 7.4.4), or the child has been switched, or a rare cis-AB allele is present. (c) A type A mother ($I^A\_$) and a type B child: the father must carry $I^B$, so a type A or O man is excluded as the father, while any B or AB man is not excluded. Blood groups can exclude paternity but cannot prove it; DNA markers with many alleles are used today (7.4.14, 7.4.22).

The *ABO* gene lies on the long arm of **chromosome** 9 (9q34). The possible blood types of children for every combination of parental types follow from the genotypes each parental type can have:

| Parents | Possible children | Impossible children |
|---|---|---|
| A × A, A × O | A, O | B, AB |
| B × B, B × O | B, O | A, AB |
| A × B | A, B, AB, O | — |
| A × AB, B × AB, AB × AB | A, B, AB | O |
| AB × O | A, B | AB, O |
| O × O | O | A, B, AB |

Two rules summarize the table: a type AB parent never has a type O child, and a type O parent never has a type AB child (apart from the Bombay phenotype and the rare cis-AB allele).

**Example 3.3.3 (Rh incompatibility)** The Rh blood group is controlled by two closely linked genes on chromosome 1, *RHD* and *RHCE*; their tight linkage is why the system was once described as a series of many alleles. The clinically important antigen is RhD: people with at least one functional *RHD* gene are RhD positive, and most RhD-negative people ($dd$; about 15 % of Europeans, fewer than 1 % of East Asians) are homozygous for a deletion of the whole *RHD* gene. Unlike anti-A and anti-B, anti-D antibodies are not present naturally; they are formed only after exposure to RhD-positive red cells. An RhD-negative mother carrying an RhD-positive fetus is usually immunized at delivery, when fetal cells enter her circulation; in a later RhD-positive pregnancy her IgG anti-D crosses the placenta and destroys fetal red cells, causing hemolytic disease of the fetus and newborn (anemia, jaundice, in severe cases fetal death). Since 1968 the disease has been largely prevented by giving the mother anti-D **immunoglobulin** after delivery, which removes the fetal cells before she can respond. If the $d$ allele has frequency $q = 0.4$ and couples form at random, $q^2 = 16\,\%$ of mothers are $dd$, and the fetus of such a mother is RhD positive if the father transmits $D$, with probability $p = 0.6$ (Hardy–Weinberg proportions, [7.4.22](/7.4.22)): about $0.16 \times 0.6 \approx 10\,\%$ of pregnancies are RhD incompatible. Maternal anti-A or anti-B antibodies against an ABO-incompatible fetus destroy fetal cells that enter the mother and partly protect her from sensitization. Because the heterozygous fetuses of $dd$ mothers are the ones at risk, the incompatibility is a form of selection against heterozygotes (7.4.23).

### 3.3.3. Wild-Type, Mutant and Polymorphic Alleles

How common an allele is in a population is measured by its frequency.

**Formula 3.3.2 (Allele Frequency)** In a sample of $N$ diploid individuals, a locus has $2N$ copies; if allele $A_i$ is present in $n_i$ of them (counting homozygotes twice),

$$
p_i = \frac{n_i}{2N}, \qquad \sum_i p_i = 1 .
$$

**Definition 3.3.2 (Genetic Polymorphism)** A locus is polymorphic, or shows **genetic polymorphism**, in a population if it has two or more alleles each with a frequency above some threshold, usually 1 %; a locus at which a single allele has a frequency of 99 % or more is **monomorphic**. The common alleles of a polymorphic locus are common variants; for a monomorphic locus the common allele is the **wild type** and the rare ones are mutant alleles.

In wild mice the agouti allele $A$ of the *agouti* gene has a frequency above 99 %: black mutants ($a$) are rare, in part because they are seen more easily by predators, and *agouti* is monomorphic. The ABO gene is polymorphic in every human population (the $i$ allele has a frequency of about 0.6–0.7 in most). The distinction is relative to a population and can change: a mutant allele that is favored by selection increases in frequency and may become the new common allele (7.4.23). More than 400 mutant alleles of *HBB* are known, most of them rare; the human leukocyte antigen (HLA) genes have thousands of alleles each and are the most polymorphic genes of the human **genome**, which is the reason organ donors and recipients must be matched carefully ([7.15](/7.15)).

### 3.3.4. Self-Incompatibility Alleles

Many flowering plants cannot fertilize themselves although their pollen and ovules are functional. In *self-incompatibility*, the pistil recognizes and rejects pollen that carries the same allele as itself at the S locus, which has dozens of alleles in natural populations. In the gametophytic system of tobacco (*Nicotiana*), petunia and other Solanaceae, studied genetically by East and Mangelsdorf (1925), the style makes an S-RNase and the pollen a set of F-box **proteins** (SLFs), all encoded at the S locus; a pollen tube whose own (**haploid**) S allele matches either allele of the style is arrested in the style, and its RNA is degraded. The alleles show no dominance with respect to each other, because the pollen phenotype is that of its own haploid genotype.

**Example 3.3.4 (Crosses under gametophytic self-incompatibility)** (a) $S_1S_2$ selfed, or crossed with any $S_1S_2$ plant: all pollen is rejected, no seed. (b) $S_1S_2$ (seed parent) × $S_2S_3$ (pollen parent): $S_2$ pollen is rejected, only $S_3$ pollen grows, and the progeny are $S_1S_3 : S_2S_3 = 1 : 1$. The **reciprocal cross** $S_2S_3 \times S_1S_2$ uses only $S_1$ pollen and gives $S_1S_2 : S_1S_3$: reciprocal crosses differ, although no sex chromosome or cytoplasm is involved. (c) $S_1S_2 \times S_3S_4$: fully compatible, $S_1S_3 : S_1S_4 : S_2S_3 : S_2S_4 = 1:1:1:1$. Homozygotes $S_iS_i$ never arise, every plant is heterozygous, and a population with $k$ alleles has $\binom{k}{2}$ genotypes. A rare allele is compatible with nearly every plant, which is why selection keeps many alleles at similar frequencies ([7.4.22](/7.4.22)). In the sporophytic system of the cabbage family (*Brassica*), by contrast, the pollen's behavior is determined by the diploid genotype of the plant that produced it, and dominance between S alleles occurs.

## 3.4. Lethal Alleles and Pleiotropy

### 3.4.1. The 2:1 Ratio

In 1905 Lucien Cuénot found that yellow mice never bred true. Yellow × yellow crosses gave about 2 yellow : 1 non-yellow (agouti) instead of 3:1, and every yellow mouse, crossed with a non-yellow one, gave 1:1: all yellow mice were **heterozygous**. W. E. Castle and C. C. Little (1910) found that about a quarter of the embryos of yellow × yellow crosses died in the uterus. The yellow **allele** $A^{y}$ of the *agouti* **gene** is **dominant** over $A$ for coat color but **recessive** for lethality: $A^{y}A^{y}$ embryos die soon after implantation.

**Definition 3.4.1 (Lethal Allele)** A **lethal allele** is an allele that causes the death of the organism (before reproductive age, usually before birth) in some **genotype**. It is a recessive lethal if only **homozygotes** (or hemizygotes) die, and a dominant lethal if one copy kills. A conditional lethal kills only under certain conditions, the restrictive conditions, and is viable under permissive conditions (3.5.3).

**Remark 3.4.1 (Degrees of Lethality)** **Mutations** differ continuously in how much they reduce viability, and in the classification used for *Drosophila* **chromosomes** extracted from natural populations (Dobzhansky and colleagues), the viability of a homozygote relative to the **wild type**, $v$ in Formula 3.4.1 below, defines the classes: lethal ($v$ near 0, conventionally below 10 %), semilethal ($v$ between about 10 % and 50 %; that is, 50–90 % of the carriers die), subvital ($v$ reduced but above 50 %), and quasinormal. The thresholds are conventions, and other textbooks draw them differently. A dominant lethal that acts before reproduction disappears in the generation in which it arises; one that acts late, after reproduction has begun, is transmitted (see the examples below).

Lethality changes ratios because the dead progeny are not counted. The observed ratio is a conditional distribution given survival.

**Formula 3.4.1 (Ratios with Reduced Viability)** If progeny class $j$ has prior probability $q_j$ (from the Mendelian calculation) and viability (probability of surviving to be scored) $v_j$, then among the scored progeny

$$
\mathbb{P}(j \mid \text{scored}) = \frac{q_j v_j}{\sum_i q_i v_i} .
$$

For $Aa \times Aa$ with $AA$ of viability $v$ and the other genotypes fully viable, the fraction of the dominant **phenotype** among survivors is

$$
f = \frac{\tfrac14 v + \tfrac12}{\tfrac14 v + \tfrac34}, \qquad\text{so}\qquad v = \frac{3f - 2}{1 - f}.
$$

$v = 1$ gives $f = 3/4$ (the 3:1 ratio) and $v = 0$ gives $f = 2/3$ (2:1).

![A recessive lethal with a dominant visible effect: yellow mice (A^y A) crossed together. Of the four equally likely combinations of gametes, the A^y A^y embryo (crossed out) dies after implantation; among the survivors, A^y A (yellow) and A A (agouti) are in the ratio 2:1](./plots/lethal-punnett.py)

**Example 3.4.1** (a) Yellow × yellow mice give 230 yellow and 100 agouti progeny. Then $f = 230/330 = 0.697$ and $v = (2.091 - 2)/0.303 = 0.30$: these data would suggest that 30 % of $A^yA^y$ embryos survive. A χ² test against 2:1 (expected 220 : 110) gives $\chi^2 = 0.45 + 0.91 = 1.36$, $p = 0.24$, so the data are also consistent with complete lethality; the estimate of $v$ is imprecise. (b) A dihybrid $A^yA\,Bb \times A^yA\,Bb$, with $B$ (black) dominant over $b$ (brown) at an independent **locus**, gives $(2:1) \times (3:1) = 6:3:2:1$ (yellow black : yellow brown : agouti black : agouti brown), 12 parts instead of 16. A total number of parts that is not a power of 4 is the signature of lethality ([7.4.4](/7.4.4#sec-4.8)).

The molecular basis of $A^y$ was found in the 1990s: it is a deletion of about 170 kb that fuses the coding region of *agouti* to the **promoter** of the neighboring gene *Raly*, which is expressed everywhere. Agouti **protein**, which normally acts only in the hair follicle (where it switches melanocytes to yellow pheomelanin, [7.4.4](/7.4.4#sec-4.7)), is made in every tissue: the mice are yellow, and also obese and diabetic, because agouti blocks melanocortin **receptors** in the brain that regulate appetite. The deletion also destroys *Raly*, and the loss of both copies of *Raly* is lethal. The dominant visible phenotype and the recessive lethality are therefore effects on two different genes of one mutation.

Other examples: Manx cats are heterozygous for a dominant allele that shortens or removes the tail and is lethal in homozygotes; the Creeper allele of chickens (short legs) and many dominant visible mutations of *Drosophila* (*Curly*, *Stubby*, *Plum*) are recessive lethals. Recessive lethals cannot be kept as homozygous stocks; in *Drosophila* they are kept balanced over chromosomes carrying another lethal and inversions that suppress recombination (balancer chromosomes, 7.4.15). Dominant lethals that kill before reproduction are eliminated in the generation in which they arise, unless, like Huntington disease (late onset, 7.4.7), they act after reproduction has begun. The stage at which a lethal allele kills shows when the gene is first needed, a tool of developmental genetics (7.4.20).

### 3.4.2. Pleiotropy

**Definition 3.4.2 (Pleiotropy)** **Pleiotropy** is the effect of one gene (or one allele) on several distinct, apparently unrelated phenotypic traits.

Pleiotropy usually reflects one gene product that acts in several tissues or at several times, or one primary defect with many downstream consequences. $A^{y}$ affects coat color, body weight and viability. The sickle-cell allele causes anemia, pain crises from blocked capillaries, damage to spleen, kidneys and brain, and resistance to malaria, all from the polymerization of one protein. **Phenylketonuria** (loss of phenylalanine hydroxylase) causes intellectual disability, seizures and light pigmentation (phenylalanine inhibits melanin synthesis). Cystic fibrosis (CFTR, a chloride channel in epithelia) affects lungs, pancreas, sweat glands and male fertility. Because a new allele usually affects several traits at once, pleiotropy constrains evolution: a mutation that improves one trait may harm another.

Mendel himself noticed pleiotropy: purple flowers, gray-brown seed coats and a purple spot in the leaf axils always went together in his crosses, as if they were one unit. All three are anthocyanin pigmentations controlled by the **bHLH** factor encoded by his gene $A$ ([7.4.2](/7.4.2#sec-2.6)). The frizzle allele $F$ of chickens (a mutation in a feather **keratin** gene, *KRT75*) is incompletely dominant: $FF$ birds have brittle, strongly curled feathers that break off, $Ff$ birds mildly curled ones. Through the loss of insulation it raises heat loss and metabolic rate, enlarges the heart and other organs, and lowers fertility, a cascade of secondary effects from one primary defect (Landauer and Dunn, 1930). The converse relation, many genes affecting one trait, is the rule rather than the exception: dozens of maize genes are each required for normal chlorophyll, and the purple color of the maize aleurone needs dominant alleles at more than half a dozen loci, a property analyzed in the next chapter (genetic heterogeneity and complementation, [7.4.4](/7.4.4#sec-4.4)).

## 3.5. One Genotype, Several Phenotypes

### 3.5.1. Penetrance and Expressivity

**Definition 3.5.1 (Penetrance and Expressivity)** The **penetrance** of a **genotype** for a **phenotype** is the proportion of individuals with that genotype who show the phenotype; it is complete if it is 100 % and incomplete otherwise. The **expressivity** is the degree or intensity with which the phenotype is expressed among those who show it; it is variable if it differs between individuals and unvarying otherwise.

Polydactyly in humans (extra fingers or toes, often **dominant**) shows both: some carriers have normal hands (incomplete penetrance), and among affected carriers the extra digits may be on one hand, both hands or hands and feet, fully formed or rudimentary (variable expressivity). Waardenburg syndrome (dominant, mostly **mutations** in *PAX3* or *MITF*) is similar: carriers can have any combination of a white forelock, irises of different colors, widely spaced eyes and deafness. The protruding lower jaw of the Habsburg dynasty, recorded in portraits over two centuries, is a historical example of variable expressivity; it was long cited as a dominant trait with incomplete penetrance, but its degree correlates with the high inbreeding coefficients of the later Habsburgs (Vilas and colleagues, 2019), which suggests a contribution of **recessive** **alleles** (7.4.7).

Penetrance enters risk calculations as a factor.

**Formula 3.5.1 (Risk with Incomplete Penetrance)** If a genotype $G$ has penetrance $\pi$ for a disease and the disease occurs only in that genotype,

$$
\mathbb{P}(\text{affected}) = \mathbb{P}(G)\,\pi, \qquad
\mathbb{P}(G \mid \text{unaffected}) = \frac{\mathbb{P}(G)(1 - \pi)}{1 - \mathbb{P}(G)\,\pi}.
$$

The second expression is **Bayes' theorem**: an unaffected relative may still carry the allele.

**Example 3.5.1** A dominant disease has penetrance $\pi = 0.8$. (a) A child of an affected **heterozygote** and a non-carrier is a carrier with probability $1/2$ and affected with probability $0.5 \times 0.8 = 0.4$. (b) If that child is unaffected, the probability that the child is nevertheless a carrier is $\dfrac{0.5 \times 0.2}{1 - 0.4} = \dfrac{0.1}{0.6} = \dfrac16$. (c) The probability that a child of this unaffected person (with a non-carrier partner) is affected is $\tfrac16 \cdot \tfrac12 \cdot 0.8 = \tfrac1{15} \approx 0.067$. In a pedigree the disease can therefore skip a generation (7.4.7).

### 3.5.2. Modifier Genes and Chance

**Definition 3.5.2 (Modifier Gene)** A **modifier gene** is a **gene** whose alleles alter the phenotype produced by the alleles of another gene (the major gene) without, by themselves, producing a comparable phenotype. The set of unidentified modifiers that influence the action of a known gene is called the genetic background.

Modifiers explain why the same mutation can have different effects in different inbred strains: the dominant *Brachyury* (*T*) mutation of mice shortens the tail by different amounts on different genetic backgrounds, although each strain is **homozygous** at nearly all **loci** and is raised in the same conditions. The severity of cystic fibrosis lung disease and of sickle-cell anemia (strongly reduced by alleles that keep fetal hemoglobin expressed into adulthood) depends on modifier loci identified by association studies (7.4.25). The distinction between major genes and modifiers is one of degree: complex traits are influenced by many genes of every effect size (7.4.24).

Chance at the level of cells can also make penetrance incomplete. A person who inherits one mutant allele of the **tumor** suppressor *RB1* develops retinoblastoma only if a second, somatic mutation inactivates the remaining allele in a developing retinal cell (the **two-hit hypothesis**, [7.3.26](/7.3.26)).

**Formula 3.5.2 (Penetrance from Random Somatic Events)** If the number of independent second hits in the target tissue of a carrier is Poisson distributed with mean $m$, the penetrance is

$$
\pi = 1 - \mathrm{e}^{-m},
$$

and the mean number of tumors among affected carriers is $m/(1 - \mathrm{e}^{-m})$.

Knudson (1971) estimated $m \approx 3$ tumors per carrier from the distribution of tumor numbers in hereditary cases, which predicts $\pi = 1 - \mathrm{e}^{-3} = 0.95$: about 5 % of carriers remain unaffected, and most affected carriers have tumors in both eyes. A dominant pattern of inheritance arises from a mutation that is recessive at the level of the cell.

### 3.5.3. Environment, Conditional Alleles and Phenocopies

The phenotype of a genotype often depends on the environment. Siamese cats and Himalayan rabbits are homozygous for temperature-sensitive alleles of tyrosinase: the **enzyme** is inactivated at the temperature of the body core and active only at the lower temperature of the skin of the extremities, so pigment forms in the cooler ears, nose, paws and tail. A shaved patch of a Himalayan rabbit kept cold grows back dark.

**Definition 3.5.3 (Conditional Allele)** A **conditional allele** produces a mutant phenotype only under restrictive conditions and a (near) **wild-type** phenotype under permissive conditions. The most common are **temperature-sensitive alleles**, which usually encode **proteins** that fold or function correctly at a low (permissive) temperature and not at a high (restrictive) one.

The $shibir\mathrm{e}^{ts1}$ allele of *Drosophila* encodes a temperature-sensitive **dynamin**, the GTPase that pinches off endocytic vesicles ([7.3.10](/7.3.10)). At room temperature the flies are normal; shifted above about 29 °C they are paralyzed within minutes, because synaptic vesicles cannot be recycled, and they recover when cooled; held at high temperature for hours they die. Conditional alleles make it possible to study genes whose loss is lethal (the **cell-division-cycle genes** of yeast were found as temperature-sensitive mutants), and to switch a gene off at a chosen time (7.4.20).

The environment can also rescue a mutant phenotype: children with **phenylketonuria** who receive a low-phenylalanine diet from birth develop normally, so the disease phenotype is conditional on diet. Conversely, the environment can imitate a mutant phenotype.

**Definition 3.5.4 (Phenocopy)** A **phenocopy** is a phenotype produced by environmental factors that resembles the phenotype produced by a mutation, in an individual that does not carry the mutation.

The drug thalidomide, taken in early pregnancy, caused limb reductions (phocomelia) that resemble the rare inherited forms; heat shocks given to *Drosophila* pupae at specific times produce flies that resemble particular mutants. Phenocopies are a pitfall in pedigrees, where an environmentally caused case can be mistaken for a carrier.

### 3.5.4. Norms of Reaction

**Definition 3.5.5 (Norm of Reaction)** The **norm of reaction** (reaction norm) of a genotype is the function that gives its phenotype over a range of environments. Two genotypes show **genotype–environment interaction** (G×E) when their norms of reaction are not parallel, so that the difference between them depends on the environment.

![Norms of reaction (schematic, not data). The phenotype of three genotypes plotted against an environmental variable such as rearing temperature. Left: no genotype–environment interaction; the curves are parallel, and the difference between genotypes is the same in every environment. Right: genotype–environment interaction; the curves cross, so that which genotype has the larger phenotype depends on the environment, and the effect of the genotype cannot be stated without specifying the environment](./plots/reaction-norms.py)

Norms of reaction show why "genetic" and "environmental" are not alternatives. Every phenotype is produced by a genotype in an environment; when the norms are parallel, the effects can be separated additively, and when they cross, a statement such as "genotype 1 is larger" is true only in some environments. A single plant can display two points of its norm of reaction at once: in the water crowfoot *Ranunculus aquatilis*, leaves that develop under water are divided into fine threadlike segments, and leaves that develop in air on the same shoot are broad and lobed, although every cell has the same genotype. In *Drosophila*, the number of facets in the eyes of *Bar* mutants decreases with rearing temperature, and the slope differs between *Bar* alleles. In molecular terms, G×E arises when the environment changes gene regulation: **DNA methylation**, **chromatin** accessibility, transcription-factor binding and **splicing** all respond to the environment, and genetic variants that alter these steps can make the response genotype dependent. The quantitative treatment, with variance components for genotype, environment and their interaction, is in 7.4.24.

## Summary

| Concept | Key statement | Calculation |
|---|---|---|
| Dominance relations (Definition 3.1.1) | **complete dominance**, **incomplete dominance** (heterozygote intermediate, $\mathrm{F}_2$ 1:2:1), **codominance** (both products seen; MN, molecular markers) | dominance index $h = (z_{12} - z_{22})/(z_{11} - z_{22})$ (Formula 3.1.1) |
| Level of observation | $Hb\beta^S$ is codominant (proteins), recessive (anemia), incompletely dominant (sickling at low $\mathrm{O_2}$), dominant (malaria resistance) | |
| Recessiveness of null alleles | flux $J(E) = J_{\max}E/(E + K_E)$ saturates; control coefficients sum to one (Formula 3.2.1) | $K_E = 0.05$: heterozygote has 95.5 % flux (Example 3.2.1) |
| **Haploinsufficiency** (Definition 3.2.1) | dosage-sensitive genes: transcription factors, structural proteins, complexes | |
| **Multiple alleles** (Definition 3.3.1) | allelic series $c^+ > c^{ch} > c^h > c$; ABO: $I^A = I^B > i$ | $k(k+1)/2$ genotypes (Formula 3.3.1) |
| ABO crosses, Rh (Example 3.3.3) | AB parent: no O child; O parent: no AB child; RhD-negative mother × RhD-positive fetus: hemolytic disease, prevented by anti-D | $q^2p$ of pregnancies incompatible |
| Self-incompatibility (Example 3.3.4) | gametophytic: pollen with an S allele of the style is rejected; reciprocal crosses differ; no $S_iS_i$ | $S_1S_2 \times S_2S_3 \to S_1S_3 : S_2S_3$ |
| Polymorphism (Definition 3.3.2) | **genetic polymorphism**: ≥ 2 alleles above 1 %; monomorphic otherwise | $p_i = n_i/2N$ (Formula 3.3.2) |
| **Lethal allele** (Definition 3.4.1) | $A^y$: dominant for color, recessive lethal; 2:1 | $\mathbb{P}(j \mid \text{scored}) = q_jv_j/\sum q_iv_i$; $v = (3f-2)/(1-f)$ (Formula 3.4.1); $6:3:2:1$ |
| **Pleiotropy** (Definition 3.4.2) | one gene, several traits ($A^y$, sickle cell, PKU, CF, frizzle, Mendel's $A$) | viability classes: lethal, semilethal, subvital (Remark 3.4.1) |
| **Penetrance**, **expressivity** (Definition 3.5.1) | incomplete penetrance, variable expressivity | $\mathbb{P}(\text{affected}) = \mathbb{P}(G)\pi$; $\mathbb{P}(G \mid \text{unaffected})$ by Bayes (Formula 3.5.1); $\pi = 1 - \mathrm{e}^{-m}$ (Formula 3.5.2) |
| **Modifier gene** (Definition 3.5.2), conditional alleles (Definition 3.5.3), **phenocopy** (Definition 3.5.4), **norm of reaction** (Definition 3.5.5) | genetic background; permissive and restrictive conditions; G×E | |

## Questions

1. Snapdragons with red and white flowers give pink $\mathrm{F}_1$. (a) What progeny **phenotypes** and proportions result from pink × pink, pink × white and red × pink? (b) Why does incomplete **dominance** make a **testcross** unnecessary?

   **Answer** (a) Pink × pink ($Aa \times Aa$): $\tfrac14$ red, $\tfrac12$ pink, $\tfrac14$ white. Pink × white ($Aa \times aa$): $\tfrac12$ pink, $\tfrac12$ white. Red × pink ($AA \times Aa$): $\tfrac12$ red, $\tfrac12$ pink. (b) Each **genotype** has its own phenotype, so the genotype is read directly from the phenotype.
2. In a plant, the **homozygotes** $A_1A_1$ and $A_2A_2$ reach mean heights of 80 cm and 40 cm, and $A_1A_2$ reaches 70 cm. Compute the dominance index of $A_1$, and the ratio $d/a$. Classify the dominance relation.

   **Answer** $h = (70 - 40)/(80 - 40) = 0.75$; $d/a = 2h - 1 = 0.5$. $A_1$ is incompletely dominant (the **heterozygote** is closer to $A_1A_1$ than to the midpoint 60 cm).
3. Explain why the sickle-cell **allele** can be called codominant, **recessive** and dominant, and why this is not a contradiction.

   **Answer** Dominance describes the relation between two alleles with respect to a specific phenotype. In the heterozygote both A and S **polypeptides** are present (codominant for the **protein** phenotype); the heterozygote does not have anemia at normal oxygen (recessive for anemia); and it is resistant to *P. falciparum* malaria like the S homozygote (dominant for resistance). The alleles are the same; the phenotypes differ, so the relations differ.
4. Using $J(E) = J_{\max}E/(E + K_E)$ with $E = 1$ for the **wild-type** homozygote, (a) find the heterozygote's relative flux $J(0.5)/J(1)$ for $K_E = 0.02$, 0.2 and 2; (b) for which $K_E$ is the heterozygote exactly halfway, in flux, between the two homozygotes?

   **Answer** (a) $J(0.5)/J(1) = 0.5(1 + K_E)/(0.5 + K_E)$: $K_E = 0.02$: $0.51/0.52 = 0.981$; $0.2$: $0.6/0.7 = 0.857$; $2$: $1.5/2.5 = 0.6$. (b) Halfway means $J(0.5)/J(1) = 0.5$ (the null homozygote has $J = 0$), so $0.5(1 + K_E) = 0.5(0.5 + K_E)$, which has no solution: the hyperbola always gives the heterozygote more than half the flux; the ratio approaches 0.5 only as $K_E \to \infty$ (the **enzyme** has all the control, $C \to 1$, and the flux is proportional to $E$).
5. How many genotypes and phenotypes are possible (a) at a **locus** with five alleles forming a complete dominance series, (b) at the ABO locus, (c) at a locus with four codominant alleles?

   **Answer** (a) $5 \times 6/2 = 15$ genotypes, 5 phenotypes. (b) 6 genotypes, 4 phenotypes (A, B, AB, O). (c) 10 genotypes, all distinguishable: 10 phenotypes.
6. A man of blood type AB and a woman of type B, whose father was type O, have children. Give the probabilities of each blood type among their children. What is the probability that their first three children are all type B?

   **Answer** The woman is $I^Bi$ (she received $i$ from her type O father). $I^AI^B \times I^Bi$: $I^AI^B$ (AB) $\tfrac14$, $I^Ai$ (A) $\tfrac14$, $I^BI^B$ (B) $\tfrac14$, $I^Bi$ (B) $\tfrac14$. So AB $\tfrac14$, A $\tfrac14$, B $\tfrac12$, O 0. Three type B children: $(1/2)^3 = 1/8$.
7. In a population sample of 500 people, there are 180 $L^ML^M$, 240 $L^ML^N$ and 80 $L^NL^N$. Compute the allele frequencies. Is the locus polymorphic?

   **Answer** $p(L^M) = (2 \times 180 + 240)/1000 = 0.6$, $p(L^N) = (240 + 2 \times 80)/1000 = 0.4$. Both alleles exceed 1 %, so the locus is polymorphic.
8. Two mice heterozygous for a recessive lethal allele that also causes a dominant short tail ($T/+$, short tail; $T/T$ dies) are crossed. (a) What is the expected ratio among live progeny? (b) Of 120 live progeny, 76 are short-tailed. Test the 2:1 hypothesis. (c) Estimate the viability of $T/T$ from Formula 3.4.1, using $f = 76/120$.

   **Answer** (a) 2 short : 1 normal. (b) Expected 80 : 40; $\chi^2 = 16/80 + 16/40 = 0.2 + 0.4 = 0.6$ (1 df, $p = 0.44$): consistent with 2:1. (c) $f = 0.633$, $v = (3f - 2)/(1 - f) = (1.9 - 2)/0.367 = -0.27$; a negative estimate means fewer short-tailed progeny than even complete lethality predicts, which is sampling error around $v = 0$ (the estimate is truncated at 0).
9. A dihybrid $A^yA\,Cc \times A^yA\,Cc$ (yellow mice, $A^yA^y$ lethal; $cc$ albino, epistatic to agouti color) is made. Find the phenotypic ratio among live progeny.

   **Answer** At the agouti locus the survivors are $\tfrac23 A^yA$ (yellow) and $\tfrac13 AA$ (agouti); at the *C* locus $\tfrac34 C\_$ and $\tfrac14 cc$ (albino, whatever the agouti genotype). Yellow: $\tfrac23 \cdot \tfrac34 = \tfrac12$; agouti: $\tfrac13 \cdot \tfrac34 = \tfrac14$; albino: $\tfrac14$. The ratio is $2:1:1$ (out of 12 survivors per 16 zygotes: 6 yellow, 3 agouti, 3 albino).
10. A dominant disease has penetrance 0.7. A woman's father is affected (heterozygous); her mother is not a carrier. (a) What is the probability that the woman is affected? (b) She is unaffected. What is the probability that she carries the allele? (c) What is the probability that her first child (with a non-carrier) will be affected?

    **Answer** (a) $0.5 \times 0.7 = 0.35$. (b) $\dfrac{0.5 \times 0.3}{0.5 \times 0.3 + 0.5} = \dfrac{0.15}{0.65} = 0.231$. (c) $0.231 \times 0.5 \times 0.7 = 0.081$.
11. In hereditary retinoblastoma, suppose the number of **tumors** per carrier is Poisson with mean $m$. (a) What value of $m$ gives a penetrance of 90 %? (b) With $m = 3$, what fraction of affected carriers has exactly one tumor?

    **Answer** (a) $1 - \mathrm{e}^{-m} = 0.9 \Rightarrow m = \ln 10 = 2.30$. (b) $\mathbb{P}(1)/\mathbb{P}(\ge 1) = 3\mathrm{e}^{-3}/(1 - \mathrm{e}^{-3}) = 0.149/0.950 = 0.157$.
12. A temperature-sensitive mutant of yeast grows at 25 °C but not at 37 °C. Describe an experiment using the temperature shift to find the stage of the **cell cycle** at which the **gene** product is required.

    **Answer** Grow an asynchronous culture at the permissive temperature (25 °C) and shift it to the restrictive temperature (37 °C). Cells that have already passed the step that needs the protein complete the cycle and arrest at the next occurrence of that step; cells before it arrest immediately at it. After a few hours all cells arrest with a uniform morphology (for example, large-budded cells with an undivided nucleus), which shows the stage at which the gene acts; this is how Hartwell identified the *cdc* genes ([7.3.20](/7.3.20)). Shifting synchronized cells at different times (or shifting back to 25 °C) gives the execution point, the last moment at which the product is required.
13. Distinguish a phenocopy from incomplete penetrance, and explain why both can mislead the analysis of a pedigree.

    **Answer** Incomplete penetrance: an individual carries the disease genotype but does not show the phenotype; a phenocopy: an individual shows the phenotype without carrying the genotype, because of an environmental cause. In a pedigree, incomplete penetrance makes a dominant disease skip generations, so it can be misread as recessive, or makes a carrier be classified as a non-carrier; a phenocopy adds an affected person who does not transmit the allele, which can suggest a new **mutation**, a wrong mode of inheritance or a false linkage in mapping studies.
14. In *Harmonia axyridis*, a **true-breeding** form with black elytral margins is crossed with a true-breeding form with black central spots. (a) Describe the $\mathrm{F}_1$. (b) Among 80 $\mathrm{F}_2$ beetles there are 18 with margins only, 44 with margins and spots and 18 with spots only. Test the single-locus hypothesis. (c) What is expected from the **backcross** of the $\mathrm{F}_1$ to the margin form?

    **Answer** (a) Under mosaic dominance the $\mathrm{F}_1$ has both the black margins and the black spots. (b) Expected $1:2:1 = 20 : 40 : 20$; $\chi^2 = 4/20 + 16/40 + 4/20 = 0.8$ with two degrees of freedom ($p = 0.67$): consistent. (c) $1$ margins and spots : $1$ margins only.
15. (a) A type A man whose mother is type O and a type AB woman have children. Give the probabilities of each blood type. (b) A type B man and a type A woman have a type O child. What is the probability that their next child is type AB, and that their next two children are both type O?

    **Answer** (a) The man is $I^Ai$. $I^Ai \times I^AI^B$: $I^AI^A$, $I^AI^B$, $I^Ai$, $I^Bi$ with $\tfrac14$ each, so A $\tfrac12$, AB $\tfrac14$, B $\tfrac14$, O $0$. (b) The O child shows that both parents are heterozygous, $I^Bi \times I^Ai$. Next child AB: $\tfrac14$. Two O children: $(1/4)^2 = \tfrac1{16}$.
16. In a population, the frequency of the RhD-negative allele $d$ is $0.4$ and genotypes are in Hardy–Weinberg proportions. An RhD-negative woman has an RhD-positive partner of unknown genotype. (a) What is the probability that the partner is $DD$? (b) What is the probability that their first child is RhD positive? (c) The first child is RhD negative. What is the probability that the second child is RhD positive?

    **Answer** (a) $\mathbb{P}(DD \mid D\_) = p^2/(p^2 + 2pq) = 0.36/0.84 = 0.429$; $\mathbb{P}(Dd \mid D\_) = 0.571$. (b) $0.429 \times 1 + 0.571 \times \tfrac12 = 0.714$. (c) An RhD-negative child shows that the partner is $Dd$, so the probability is $\tfrac12$ (a **conditional probability**, as in [7.4.2](/7.4.2#sec-2.4.4)).
17. In a gametophytically self-incompatible plant, give the progeny genotypes and proportions of (a) $S_1S_2$ (seed parent) × $S_1S_3$ (pollen parent) and of the **reciprocal cross**; (b) an $S_1S_2$ plant pollinated with an equal mixture of pollen from $S_1S_3$ and $S_3S_4$ plants. In (b), what fraction of the seeds is sired by the $S_3S_4$ plant?

    **Answer** (a) Only $S_3$ pollen grows on the $S_1S_2$ style: $S_1S_3 : S_2S_3 = 1:1$. Reciprocal ($S_1S_3$ style, $S_1S_2$ pollen): only $S_2$ pollen grows: $S_1S_2 : S_2S_3 = 1:1$. (b) Functional pollen: from $S_1S_3$ only the $S_3$ half ($\tfrac14$ of all pollen); from $S_3S_4$ all of it ($\tfrac14$ $S_3$, $\tfrac14$ $S_4$). Among functional pollen $S_3 : S_4 = 2 : 1$, so the seeds are $S_1S_3$ $\tfrac13$, $S_2S_3$ $\tfrac13$, $S_1S_4$ $\tfrac16$, $S_2S_4$ $\tfrac16$; the $S_3S_4$ plant sires $\tfrac{1/2}{3/4} = \tfrac23$ of them (assuming equal competitive ability of compatible pollen).
18. Two *Drosophila* heterozygous for a recessive visible mutation are crossed, and 300 wild-type and 40 mutant flies emerge. (a) Estimate the relative viability $v$ of the mutant homozygote. (b) Classify the mutation by Remark 3.4.1.

    **Answer** (a) The expected survivors are $\tfrac34 : \tfrac14 v$, so $v = 3 \times 40/300 = 0.40$ (Formula 3.4.1 with the viability on the recessive class). (b) $v$ is between 10 % and 50 %: semilethal.
