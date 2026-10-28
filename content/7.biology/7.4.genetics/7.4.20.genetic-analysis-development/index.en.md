---
title: The Genetic Analysis of Development
description: "How genetics dissects development. Mosaic and regulative determination; mutagenesis screens for zygotic and maternal-effect genes and the sorting of mutations into complementation groups; identifying the gene (positional cloning, transposon tagging, mapping by sequencing and its allele-frequency model); the sevenless system and modifier screens in a sensitized background; where a gene acts (expression patterns, genetic mosaics, cell autonomy) and when (temperature-sensitive periods); epistasis analysis and the rules for ordering switch and biosynthetic pathways; the Drosophila body plan as a genetic hierarchy of maternal-effect, gap, pair-rule, segment-polarity and homeotic genes; RNAi screens and organoids."
---

Development turns one cell into an organism with many kinds of cell in a reproducible arrangement. Its mechanisms are the subject of [7.5](/7.5); its **genes** were found, and the order in which they act was established, by the methods of this chapter. The programme is that of [7.4.1](/7.4.1), applied to a process rather than to a trait: mutate at random, screen for individuals whose development goes wrong in a defined way, sort the **mutations** into genes by **complementation**, identify the genes molecularly, and then ask of each gene where it acts, when it acts and where it lies in a pathway. The answers rest on tools assembled earlier: mutagenesis and **allele** classes ([7.4.12](/7.4.12)), **complementation groups** ([7.4.13](/7.4.13)), **mitotic recombination** and **genetic mosaics** ([7.4.9](/7.4.9)), **maternal effects** ([7.4.11](/7.4.11)), **epistasis** ([7.4.4](/7.4.4)), mapping ([7.4.8](/7.4.8), [7.4.14](/7.4.14)) and the transgenic and conditional methods of [7.4.19](/7.4.19). This chapter keeps to the genetic logic and to the classes of **mutant** **phenotype**; the morphogen gradients, the regulatory networks and the comparative developmental biology that explain the phenotypes belong to [7.5](/7.5).

## 20.1. Why Development Can Be Analyzed Genetically

Two facts make the genetic approach possible. First, the strategies of development are conserved: the same genes build eyes in flies and in vertebrates, as the discovery that the fly gene *eyeless*, the mouse *Pax6* and the human *ANIRIDIA* gene are one **gene family** showed, so a gene found in a fly screen usually has a counterpart with a related function in humans. Second, development is modular enough that single mutations disturb recognizable parts of it, which is why screens for visible defects work at all.

Species differ in how much of the pattern is fixed in the egg. If one cell of a two-cell *C. elegans* embryo is destroyed, the remaining cell produces only the structures it would have made in an intact embryo: determination is mosaic, each blastomere receiving its own set of molecular instructions. A mammalian embryo of two cells, by contrast, can lose one and still develop completely: determination is regulative, cells adjusting their fates to their surroundings. The genetic consequence is practical. In a mosaic embryo the lineage is invariant and every cell can be named, which makes it possible to see exactly which cell a mutation affects; in a regulative embryo, fates must be followed with markers and clones. Both strategies occur in all animals, in different tissues and at different stages.

## 20.2. Finding the Genes

### 20.2.1. Screens for Zygotic and Maternal-Effect Genes

The first question about any developmental process is which genes are required for it. The answer comes from a screen ([7.4.19](/7.4.19#sec-19.5)) whose design follows the genetics of the process: whether the gene product is made by the embryo itself or deposited in the egg by the mother.

**Definition 20.2.1 (Zygotic and Maternal-Effect Genes)** A **zygotic gene** is one whose product acts in the embryo and is transcribed from the embryo's own **genome**, so that the phenotype follows the embryo's **genotype**. A **maternal-effect gene** is one whose product is made during **oogenesis** and deposited in the egg, so that the phenotype of the embryo follows the genotype of its mother and not its own ([7.4.11](/7.4.11#def-11.6.1)).

In *Drosophila* the distinction is sharp, because the zygotic nuclei transcribe very little during the thirteen rapid syncytial divisions that follow fertilization: everything that happens before cellularization depends on maternal products. A screen for maternal-effect mutations therefore looks one generation further than a screen for zygotic mutations: the mutation must be made homozygous in females, and it is their embryos, of any genotype, that are examined. Homozygous females are usually sterile in the sense that their eggs develop abnormally and die, which is itself the screening criterion.

**Algorithm 20.2.1 (A Screen for Recessive Maternal-Effect Mutations)**

1. Mutagenize males and establish balanced lines, each carrying one mutagenized **chromosome** over a balancer, as in Algorithm 19.5.1 of [7.4.19](/7.4.19#alg-19.5.1).
2. From each line obtain homozygous females ($*/*$), one quarter of the offspring of the sibling intercross; lines in which **homozygotes** die carry a zygotic lethal and are set aside for the zygotic screen.
3. Cross the homozygous females to wild-type males, so that every embryo carries a wild-type allele from its father. Any defect in these embryos cannot be due to their own genotype and must come from the mother: it is a maternal effect.
4. Examine the embryos (cuticle preparations, in situ markers). Identify the classes of defect, for example loss of anterior structures or of abdominal segments.
5. Confirm by the **reciprocal cross**: heterozygous mothers mated to homozygous fathers give embryos of the same genotypes but normal development.
6. Sort the mutations into complementation groups by crossing the lines in pairs ([7.4.13](/7.4.13#sec-13.1.1)); estimate from the numbers of alleles per group whether the screen is saturated (Formula 19.5.1 of [7.4.19](/7.4.19#fml-19.5.1)).

Nüsslein-Volhard and Wieschaus applied the zygotic version of this programme to the pattern of the larval cuticle, which records the segments of the embryo in a form that can be scored quickly in large numbers, and recovered about 120 genes; the maternal version identified some 30 more that establish the axes. Together they defined the classes of gene described in 20.6.

![A screen for recessive maternal-effect mutations. Each line carries a mutagenized chromosome (asterisk) over a balancer; the intercross of siblings yields homozygous females among the survivors, and these are mated to wild-type males. Their embryos all carry a wild-type allele from the father, so a defect in them must come from the products the mother deposited in the egg: the phenotype follows the mother's genotype, not the embryo's. The reciprocal cross, heterozygous mothers by homozygous fathers, gives the same embryonic genotypes and normal embryos, which confirms the maternal effect](./plots/maternal-effect-screen.py)

### 20.2.2. From Mutation to Gene

A mutation identifies a gene only when the gene is known molecularly. Three routes lead there.

- **Positional cloning** ([7.4.14](/7.4.14)): map the mutation by recombination and deficiencies to a small interval, list the genes in it, and test the candidates by sequencing them in several independent alleles and by **transgene** rescue (Algorithm 19.3.1 of [7.4.19](/7.4.19#alg-19.3.1)).
- **Transposon** tagging ([7.4.17](/7.4.17)): if the mutation was caused by a transposon insertion, the flanking DNA is recovered by inverse PCR or by sequencing, and the identification is immediate. Reversion of the phenotype when the element is mobilized out again (precise excision) confirms it.
- Mapping by sequencing: cross the mutant to a polymorphic strain, select mutant individuals in the F2, pool their DNA and sequence it. Away from the mutation the two parental genotypes are equally represented; near the mutation almost all chromosomes come from the mutant parent, because only recombinants separate the marker from the causative site.

**Formula 20.2.1 (Allele Frequency in a Mutant Pool)** Let a recessive mutation be selected in the F2 of a cross between the mutant strain and a polymorphic strain, and let $r(d)$ be the **recombination frequency** between the mutation and a marker at genetic distance $d$ (a **mapping function**, [7.4.8](/7.4.8#sec-8.4)). In a pool of $n$ mutant F2 individuals, the expected frequency of the allele contributed by the mutant parent at that marker is

$$
f(d) = 1 - r(d),
\tag{20.1}
$$

which equals 1 at the mutation itself and falls to $1/2$ for unlinked markers. With $n$ individuals and read depth large, the **standard error** of the estimate at one marker is about $\sqrt{f(1-f)/(2n)}$, so the peak is located to within a few **centimorgans** with a pool of 50 and to a fraction of a centimorgan with several hundred.

Because the frequency is a smooth function of position, the profile over a chromosome has a single maximum at the gene, and the candidate variants are those near the maximum that are predicted to change a **protein**. The same statistics underlie bulked segregant analysis in plants and QTL mapping in populations ([7.4.25](/7.4.25)).

![Mapping by sequencing (simulation). Mutant F2 individuals from a cross to a polymorphic strain are pooled and sequenced; at each marker the plot shows the fraction of reads carrying the allele of the mutant parent. Away from the mutation the two parental alleles are equally frequent (0.5), and near it the mutant parent's allele approaches fixation, following Eq. (20.1) with the Haldane mapping function. Points: simulated pools of 20 and of 200 mutant individuals, sequenced to 300-fold depth, so that the scatter reflects mainly the number of individuals pooled; line: the expectation. The width of the peak and the scatter of the points set how precisely the gene can be located](./plots/mapping-by-sequencing.py)

## 20.3. Screens That Find What the First Screen Missed

A screen for a specific morphological defect misses two kinds of gene. A **pleiotropic** gene needed for viability kills the animal before the structure forms, so its mutants never appear in the screen. Redundant genes compensate for one another, so that loss of either alone gives no phenotype ([7.4.4](/7.4.4#sec-4.3.3)). Both are recovered by a screen in a sensitized background.

**Definition 20.3.1 (Modifier Screen and Sensitized Background)** A **sensitized background** is a genotype in which a process is impaired but not abolished, typically by a hypomorphic allele, so that its outcome depends on the amount of other components. A **modifier screen** is a screen in such a background for mutations that make the phenotype more severe (**enhancer mutations**, dominant **enhancers**) or less severe (**suppressor mutations**, dominant suppressors), usually scored in **heterozygotes** in the F1.

The classic example is the recruitment of the R7 photoreceptor in the compound eye of *Drosophila*. Each of the about 800 ommatidia contains eight photoreceptors that are recruited in a fixed order, R7 last; a fly without R7 cells sees no ultraviolet light but is otherwise normal, and the cell can be seen in sections or by a simple optical test. A screen for flies lacking R7 but keeping the other photoreceptors recovered mutations in only two complementation groups, *sevenless* (*sev*), which encodes a **receptor tyrosine kinase** on the R7 precursor, and *bride of sevenless* (*boss*), which encodes its **ligand** on the neighboring R8 cell. The rest of the pathway was invisible to that screen because its components are used everywhere and their loss is lethal.

To find them, a hypomorphic *sev* allele was used, whose protein has reduced activity, so that R7 is recruited in only some ommatidia. In this background, halving the dose of a gene whose product helps Sevenless signal makes all ommatidia lack R7 (a dominant enhancer), and halving the dose of a gene whose product opposes the pathway restores R7 in all of them (a dominant suppressor). Heterozygous mutations in *Ras1* and in *Sos*, which encodes the exchange factor that loads Ras with GTP, behave as dominant enhancers; mutations in the gene for the Ras **GTPase-activating protein** behave as dominant suppressors. None of these heterozygotes has any eye phenotype in a wild-type background: the sensitized genotype is what makes them visible. A complementary design uses a mild gain of function instead: a transgene expressing a constitutively active Ras protein, with an amino-acid substitution at position 12, under the *sev* regulatory region, which makes all five competent precursor cells become R7 cells, and whose phenotype is likewise sensitive to the dose of other pathway components.

![Modifier screens in a sensitized background, with the Sevenless pathway as an activity-flow diagram. The Boss ligand on R8 activates the Sevenless receptor tyrosine kinase on the R7 precursor; the signal passes through Drk and Sos to Ras, which is turned off by a GTPase-activating protein, and on through the kinase cascade to transcription factors that give the R7 fate. In a background with a hypomorphic sev allele the pathway works in only some ommatidia. Halving the dose of a positive component (green) disables it completely: a dominant enhancer. Halving the dose of a negative component (red) restores recruitment in every ommatidium: a dominant suppressor. In a wild-type background these heterozygotes have no phenotype](./plots/sevenless-modifiers.py)

Two further strategies extend the reach of screens. **RNA interference** ([7.2.18](/7.2.18#sec-18.5)) makes it possible to reduce the activity of a chosen gene, or of every gene in turn: in *C. elegans*, feeding worms bacteria that express double-stranded RNA knocks down a gene in the whole animal, and libraries covering nearly all genes have been screened for defects in embryogenesis and other processes, with the advantage that the gene is known from the start and the disadvantage that knockdown is partial and can hit related sequences. Transgenic **hairpin** constructs under GAL4 control ([7.4.19](/7.4.19#def-19.2.1)) restrict the knockdown to chosen cells, which gets around the lethality that blocked the original screen. Finally, human **organoids** ([7.3.24](/7.3.24)) allow screens in human tissue: stem-cell-derived three-dimensional cultures that reproduce much of the architecture of a human organ can be mutated or edited, and developmental phenotypes, such as the reduced size of cerebral **organoids** from patients with microcephaly mutations, scored directly.

## 20.4. Where and When a Gene Acts

### 20.4.1. Expression Patterns

The first description of a cloned developmental gene is where and when it is transcribed and where its protein goes: in situ **hybridization** with labeled complementary sequences for the mRNA, RNA sequencing of dissected or single cells for quantitative measurements, antibodies and fluorescent-protein fusions for the protein ([7.4.19](/7.4.19#sec-19.3)). An expression pattern is suggestive but not decisive: genes are often expressed where they are not needed, and a protein can act on cells other than the one that makes it.

### 20.4.2. Mosaic Analysis and Cell Autonomy

The decisive experiment asks whether the gene must be present in the cell that shows the phenotype.

**Definition 20.4.1 (Cell Autonomy)** A gene acts **cell-autonomously** if its product is required in the cell that shows the mutant phenotype, so that in a mosaic a mutant cell is abnormal whatever its neighbours are. It acts non-autonomously if the mutant phenotype of a cell can be rescued by wild-type neighbours, or if wild-type cells are made abnormal by mutant neighbours, which shows that the product acts between cells.

Mosaics are made as in [7.4.9](/7.4.9#sec-9.5.3): by **mitotic recombination**, induced at a chosen time with a **site-specific recombinase** (FLP acting on FRT sites) in an animal heterozygous for the mutation and for a marker, which produces clones homozygous for the mutation and marked. In the eye, the marker is *white*: clones homozygous for a *white* mutation have unpigmented facets, and the genotype of every photoreceptor can be read under the microscope.

The result for the R7 system is a model of the method. In mosaic eyes in which the marked cells were homozygous for both *white* and *sev*, every ommatidium that contained an R7 cell had a pigmented, that is genetically wild-type, R7, even when all the other photoreceptors of the same ommatidium were mutant: *sev* is needed in the R7 precursor itself and nowhere else, so it acts cell-autonomously, as a **receptor** should. For *boss* the result is the opposite: *boss* is required in R8, not in R7, and a mutant R7 precursor develops normally beside a wild-type R8. The conclusion, that Boss is a ligand presented on one cell to a receptor on another, was drawn from the mosaics before the molecules were characterized.

### 20.4.3. Temperature-Sensitive Periods

A gene needed at several times can be analyzed with a **conditional allele** ([7.4.3](/7.4.3#sec-3.5.3)).

**Definition 20.4.2 (Temperature-Sensitive Period)** The **temperature-sensitive period** of a temperature-sensitive mutation is the interval during development in which the restrictive temperature produces the mutant phenotype; shifting to the restrictive temperature before it or back to the permissive temperature after it leaves the phenotype normal.

Two complementary shifts define it: a shift-up at successive times (the last time at which a shift to the restrictive temperature still gives the mutant phenotype) and a shift-down (the first time at which the animal has already escaped). For a temperature-sensitive *sev* allele the period extends over many hours before the R7 cell differentiates, which means that the receptor must be activated continuously, not once, for the precursor to adopt the R7 fate. The method assumes that the protein is inactivated and reactivated quickly on shifting, which has to be checked, and that the shift itself has no other effect, which is controlled with wild-type animals.

## 20.5. Ordering a Pathway

Once several genes are known to affect one process, the next question is their order of action. Two kinds of evidence answer it.

Expression gives the first kind of evidence. If loss or overactivity of gene $a$ changes the expression of gene $b$, and not the converse, $a$ acts upstream of $b$ in the regulation of $b$. In the R7 system, mutations in *prospero*, which encodes a **transcription** factor, do not change the expression of *sevenless* or of Ras, while activation of the Sevenless pathway changes the expression of *prospero*: the pathway acts upstream of *prospero*.

Double mutants give the general method is epistasis analysis, which applies the concept of [7.4.4](/7.4.4#sec-4.2.1) to ordering rather than to ratios.

**Definition 20.5.1 (Epistasis Analysis)** **Epistasis analysis** is the ordering of genes in a pathway by the phenotype of the double mutant: if two mutations in genes of the same pathway give different phenotypes, and the double mutant resembles one of them, that mutation is epistatic, and its gene is assigned a position in the pathway according to the rules below.

The rules differ for the two kinds of pathway, and confusing them is the commonest error.

**Algorithm 20.5.1 (Epistasis Analysis)**

1. Establish that the two genes act in the same process (similar or related phenotypes, genetic interaction) and that their single-mutant phenotypes differ, so that the double mutant can resemble one of them.
2. Decide what kind of pathway it is. In a *switch* (regulatory) pathway, a signal travels along a chain of regulators, each turning the next on or off; in a *biosynthetic* pathway, each **enzyme** converts one substance into the next.
3. For a switch pathway, combine a **loss-of-function mutation** in one gene with a **gain-of-function mutation** in the other. The double mutant takes the phenotype of the *downstream* gene: activating a component downstream of a block restores the output, and removing a component downstream of an activated one leaves the output off.
4. For a biosynthetic pathway with two loss-of-function mutations, the double mutant shows the phenotype of the *upstream* block, because the intermediate that the downstream enzyme would accumulate is never made.
5. For two loss-of-function mutations in a switch pathway with the same direction of effect, no order can be inferred; use the combinations of step 3, a conditional allele or expression evidence instead.
6. Check the assumptions: the alleles must be null or fully constitutive (a **hypomorph** gives intermediate phenotypes that can masquerade as epistasis), and the genes must lie in one linear pathway, since a branch or a feedback loop can give a double-mutant phenotype that fits no simple order.

**Example 20.5.1** In the R7 system, flies with a null *sev* mutation have no R7 cells, and flies carrying the activated Ras transgene have too many. (a) The double mutant, a *sev* null carrying the activated Ras transgene, has too many R7 cells: Ras acts downstream of Sevenless, because the activated Ras no longer needs the receptor. (b) Conversely, loss of Ras function in a background with an activated receptor leaves no R7 cells: the same order, read from the other direction. (c) A *boss* null with activated Ras also has supernumerary R7 cells, which places both ligand and receptor above Ras.

![The informative double-mutant combinations in epistasis analysis. Above, a switch (regulatory) pathway in which A acts on B and B on the output: combining a loss of A with a gain of B leaves the output on, and a gain of A with a loss of B leaves it off, so in both cases B is epistatic and therefore downstream; two losses, or two gains, give the same phenotype as either single mutant and reveal no order. Below, the contrasting rule for a biosynthetic pathway: with two loss-of-function mutations the upstream block determines the phenotype, because the intermediate on which the downstream enzyme acts is never made](./plots/epistasis-analysis.py)

## 20.6. The Body Plan of *Drosophila* as a Genetic Hierarchy

The screens of 20.2 found the genes that build the segmented body of the fly, and the methods of 20.4 and 20.5 arranged them in a hierarchy of four tiers, from the products the mother supplies to the genes that name each segment. The present section gives the genetic result: the classes of gene, the classes of mutant phenotype that define them and the logic by which the order was established. The mechanisms (how a concentration gradient is read, how stripes are made by combinations of transcription factors, how the regulatory regions are organized, and how the system compares with that of other animals) are the subject of [7.5](/7.5).

The embryo in which these genes act is a syncytium: the zygotic nucleus divides thirteen times without cell division, the nuclei migrate to the surface at the ninth division to form the syncytial blastoderm, and membranes grow between them in the fourteenth **interphase** to make the cellular blastoderm. Until then, transcription factors diffuse between nuclei, which is why maternal products laid down as gradients in the egg can position zygotic gene expression directly.

**Definition 20.6.1 (The Four Classes of Segmentation Gene)** In the hierarchy that gives the *Drosophila* larva its segments:

- a **maternal-effect gene** of the axis systems is transcribed in the mother and deposited in the egg, and sets up the anterior–posterior or dorsal–ventral coordinates of the embryo; mutant mothers produce embryos lacking whole regions, for example all head and thoracic structures (*bicoid*) or all abdominal segments (*nanos*);
- a **gap gene** is a zygotic gene expressed in a broad domain of the blastoderm, and mutants lack a contiguous block of several segments, a gap in the pattern at the position where the gene is expressed;
- a **pair-rule gene** is a zygotic gene expressed in seven stripes, and mutants lack part of every alternate segment, so that the larva has half the normal number of segmental units;
- a **segment-polarity gene** is a zygotic gene expressed in fourteen stripes, one per segment, and mutants have the correct number of segments but a defect in the same part of each, often with that part replaced by a mirror image of the remaining part.

**Definition 20.6.2 (Homeotic Genes and Homeotic Transformation)** A **homeotic gene** is a gene that assigns identity to a region of the body, so that its loss or ectopic expression converts one body part into another, a **homeotic transformation**; the homeotic genes of the *Antennapedia* and *bithorax* complexes of *Drosophila*, and their counterparts in other animals, are the *Hox* genes, which contain the **homeobox**, a sequence of about 180 bp encoding the DNA-binding **homeodomain**.

The classes were defined by phenotype before any of the genes was cloned, and the order of the tiers was established genetically: maternal mutants alter the expression of gap genes but not the reverse; gap mutants alter the stripes of the pair-rule genes; pair-rule mutants alter the stripes of the segment-polarity genes; and homeotic genes change identity without changing the number of segments, so they must act after the segments exist. Mutations in the homeotic genes are among the oldest in genetics: *Antennapedia* alleles that convert antennae into legs, and *bithorax* alleles that convert the third thoracic segment into a copy of the second, giving a four-winged fly. The order of the genes along the chromosome parallels the order of the body regions in which they are expressed, a colinearity that holds for the *Hox* clusters of vertebrates as well; in mice and humans the clusters are quadruplicated, and their mutations likewise transform body regions.

![The hierarchy of segmentation genes and the mutant phenotypes that define each tier (schematic; positions along the embryo in fractions of egg length, anterior to the left). Left column: the expression of a representative gene of each tier in the blastoderm, from the maternal gradients through the broad domains of the gap genes and the seven pair-rule stripes to the fourteen stripes of the segment-polarity genes. Right column: the corresponding class of mutant larval pattern, drawn as the surviving segmental units — a whole region missing for a maternal-effect mutant, a contiguous block for a gap mutant, alternate units for a pair-rule mutant, and all units present but each defective for a segment-polarity mutant. Below, a homeotic mutation leaves the number of units unchanged and alters the identity of one of them](./plots/segmentation-hierarchy.py)

## Summary

| Topic | Key points |
|---|---|
| Why it works (20.1) | conserved strategies (*eyeless*/*Pax6*); mosaic vs regulative determination and what each allows |
| Screens (Definition 20.2.1, Algorithm 20.2.1) | zygotic vs maternal-effect: the maternal screen scores the embryos of homozygous mothers crossed to wild-type males; reciprocal cross as control; complementation groups; saturation ([7.4.19](/7.4.19#fml-19.5.1)) |
| Identifying genes (Formula 20.2.1, Eq. (20.1)) | positional cloning, **transposon tagging** with excision reversion, mapping by sequencing: **allele frequency** $1 - r(d)$ peaks at the gene |
| Modifier screens (Definition 20.3.1) | sensitized background (hypomorphic *sev*, or activated Ras in the eye); dominant enhancers (*Ras1*, *Sos*) and suppressors (Ras GAP) that are silent in a wild-type background; RNAi libraries; organoids |
| Where and when (Definitions 20.4.1, 20.4.2) | expression patterns are suggestive only; FLP/FRT mosaics: *sev* autonomous in R7, *boss* required in R8; temperature-shift experiments give the temperature-sensitive period (Sevenless needed for hours) |
| Ordering (Definition 20.5.1, Algorithm 20.5.1, Example 20.5.1) | switch pathway: loss + gain, the downstream gene is epistatic; biosynthetic pathway: two losses, the upstream block wins; needs null and constitutive alleles and a linear pathway |
| Body plan (Definitions 20.6.1, 20.6.2) | syncytial blastoderm; maternal-effect → gap → pair-rule → segment-polarity → homeotic; phenotype classes: region, block, alternate, every-segment, identity; colinearity of *Hox* clusters; mechanisms in [7.5](/7.5) |

## Questions

1. A recessive mutation gives embryos that die with no abdominal segments. How do you decide whether it is a zygotic or a maternal-effect mutation, using crosses only?

   **Answer** Cross homozygous females to wild-type males and heterozygous females to homozygous males. If the defect depends on the mother's genotype (all embryos of homozygous mothers die, although they carry a wild-type paternal allele, while embryos of heterozygous mothers are normal even when homozygous mutant themselves), the gene is maternal-effect. If instead a quarter of the embryos from an intercross of heterozygotes are affected, irrespective of which parent is homozygous, the gene is zygotic.

2. In a maternal-effect screen, 3 500 lines are examined and 18 complementation groups are found, 9 with one allele, 5 with two, 4 with three or more. (a) Estimate $\lambda$ and the number of genes still to be found. (b) How many lines would be needed to reach $\lambda = 3$?

   **Answer** (a) $\hat\lambda = 2n_2/n_1 = 10/9 = 1.11$; $\hat n_0 = n_1^2/(2n_2) = 81/10 = 8$ genes (Eq. (19.2) of [7.4.19](/7.4.19#fml-19.5.1)). (b) $\lambda \propto N$, so $N = 3\,500 \times 3/1.11 \approx 9\,500$ lines.

3. Mapping by sequencing: at a marker 8 cM from the mutation, what fraction of the reads in a pool of mutant F2 individuals is expected to carry the allele of the mutant parent, (a) using the recombination frequency directly, (b) at 25 cM, and (c) what is the expected fraction at an unlinked marker?

   **Answer** With the Haldane function $r = (1 - \mathrm{e}^{-2d})/2$: (a) $d = 0.08$, $r = 0.074$, $f = 0.926$. (b) $d = 0.25$, $r = 0.197$, $f = 0.803$. (c) $r = 0.5$, $f = 0.5$: the two parental alleles are equally frequent.

4. Why does a screen for flies that lack the R7 photoreceptor recover mutations in only two genes, although the pathway has at least six components? Name the two reasons and the screen design that overcomes each.

   **Answer** Components used in many tissues are essential, so their mutants die before the eye is scored (**pleiotropy**), and genes with redundant partners give no phenotype when mutated alone. A modifier screen in a sensitized background recovers the first, since heterozygotes are viable and their half dose shifts the sensitized phenotype; clonal screens with FLP/FRT recover the second kind of lethal gene by making homozygous mutant clones in a viable animal, and combinations (double knockdowns) reveal redundancy.

5. In a *sev* hypomorphic background, a heterozygous mutation makes all ommatidia lack R7. (a) Is it an enhancer or a suppressor, and does its gene promote or oppose the pathway? (b) Why does the same heterozygote look normal in a wild-type background? (c) What phenotype would you expect for this heterozygote in a background carrying the activated Ras transgene, if the gene acts upstream of Ras?

   **Answer** (a) A dominant enhancer; its product helps the pathway (reducing it by half pushes the weakened pathway below the threshold). (b) With a full-strength receptor the pathway has enough reserve that half the dose of one positive component still exceeds the threshold. (c) No change: activated Ras does not need the upstream components, so reducing one of them has no effect on the supernumerary R7 phenotype. This is itself a way of ordering genes.

6. In a mosaic eye, marked cells are homozygous for *boss* and *white*, and unmarked cells carry a wild-type allele of each. Predict which ommatidia lack R7 if Boss is a ligand on R8, and state what you would have concluded if R7 had been missing whenever the R7 cell itself was marked.

   **Answer** Ommatidia lack R7 when the R8 cell is marked (mutant), whatever the genotype of the R7 precursor: *boss* acts non-autonomously, in the signaling cell. Had the loss of R7 followed the genotype of the R7 precursor, *boss* would act cell-autonomously in R7, as a receptor or an intracellular component does.

7. A **temperature-sensitive allele** gives the mutant phenotype when embryos are kept at the restrictive temperature from 0 to 10 h but not from 12 h onwards, and a shift back to the permissive temperature at 6 h rescues them. (a) What is the temperature-sensitive period? (b) What must be true of the protein for the conclusion to hold? (c) Why is a wild-type control at both temperatures necessary?

   **Answer** (a) Roughly 6–10 h: the phenotype requires the restrictive temperature during that window (a shift back at 6 h still rescues, so nothing before 6 h is sufficient; shifts up after 12 h are too late). (b) The protein must lose and regain activity quickly on shifting, so that the interval of inactivation corresponds to the interval of the shift. (c) Temperature itself changes developmental rate and can produce phenocopies, so the timing must be calibrated and the phenotype shown to be specific to the mutant.

8. Two genes act in a switch pathway. A loss-of-function mutation in gene 1 gives phenotype X (output off); a gain-of-function mutation in gene 2 gives phenotype Y (output on). The double mutant shows Y. (a) Which gene is downstream? (b) What would the double mutant show if gene 2 were upstream? (c) Why is a double mutant of two loss-of-function alleles uninformative here?

   **Answer** (a) Gene 2: an activated downstream component bypasses the block upstream of it. (b) Phenotype X: an activated upstream component cannot signal through a missing downstream one. (c) Both single mutants turn the output off, so the double mutant also has the output off, which is consistent with any order.

9. In a biosynthetic pathway, mutants of gene A accumulate substance 1 and mutants of gene B accumulate substance 2. The double mutant accumulates substance 1. (a) Which gene acts earlier? (b) State the general rule and contrast it with the rule for switch pathways. (c) How can feeding experiments confirm the order?

   **Answer** (a) Gene A: its block is upstream, so substance 2 is never made. (b) In a biosynthetic pathway two loss-of-function mutations combine and the upstream block determines the phenotype; in a switch pathway the informative combination is loss plus gain and the downstream gene is epistatic. (c) Supplying the intermediates in turn: a mutant grows (or develops) when fed any intermediate downstream of its block but not one upstream of it, which orders the steps ([7.4.13](/7.4.13#sec-13.4.1)).

10. Assign each mutant phenotype to a class of segmentation gene: (a) embryos from homozygous mothers lack all abdominal segments; (b) embryos lack segments T1 to A4 as a block; (c) embryos have seven instead of fourteen denticle bands; (d) every segment has its posterior part replaced by a mirror image of its anterior part; (e) the third thoracic segment resembles the second.

    **Answer** (a) Maternal-effect (axis) gene; (b) gap gene; (c) pair-rule gene; (d) segment-polarity gene; (e) homeotic gene (a homeotic transformation, with the number of segments unchanged).

11. Why must a maternal-effect gene be identified by the phenotype of embryos from homozygous mothers rather than by the phenotype of the mothers themselves, and what does it mean for the recurrence of a phenotype in a pedigree-like scheme?

    **Answer** The gene acts during oogenesis, so the mother is normal apart from producing defective eggs; the phenotype appears one generation later than the genotype. In crosses, therefore, the affected class is defined by the mother's genotype and not by its own, and the apparent ratios are shifted by one generation: an intercross of heterozygotes gives a quarter of homozygous daughters, and all of their embryos, rather than a quarter of the embryos, are affected.

12. The *Hox* genes of flies and mice lie in clusters whose gene order matches the order of the body regions they specify. (a) What experiment shows that a mouse *Hox* gene can function in the fly pathway? (b) Why does colinearity not follow from the genetic analysis alone, and what does it predict about the consequences of a deletion within the cluster?

    **Answer** (a) Expressing the mouse gene in the fly, from a transgene under a fly **promoter**, produces transformations like those of the corresponding fly gene, which shows that the proteins are functionally interchangeable. (b) Genetics establishes which gene specifies which region, but the arrangement on the chromosome is a separate, molecular observation; it predicts that a deletion removing adjacent genes transforms a contiguous block of body regions, which is what the deletions of the *bithorax* complex do.
