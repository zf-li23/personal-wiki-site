---
title: Dissecting the Gene with Mutations
description: Using collections of mutations to define genes and their functions; complementation groups from a complementation matrix with a grouping algorithm and its exceptions (intragenic complementation, dominant negatives, nonallelic noncomplementation); the cistron and the cis–trans test; Benzer's fine-structure analysis of the rII region of phage T4, selective recombination, deletion mapping and mutational hotspots; base pairs per map unit across organisms; Beadle and Tatum's one gene, one enzyme and the ordering of pathways from growth tests; the period genes; unequal crossing over in the opsin genes of color vision.
---

The previous chapter treated **mutations** one at a time. Geneticists rarely have one mutation: a screen ([7.4.19](/7.4.19)) yields dozens or thousands of **mutants** with similar **phenotypes**, and the first questions are how many **genes** they represent, how the mutations are arranged within each gene, and what each gene does. This chapter shows how these questions were answered with nothing but crosses and growth tests, before DNA could be sequenced, and why the answers remain the logic of genetic analysis today. Three tools are combined. The **complementation test** ([7.4.4](/7.4.4)) sorts **recessive** mutations into functional units, genes; recombination between mutations in the same gene, measured with the powerful selection of phage genetics, shows that a gene is a linear sequence of many mutable sites; and the phenotypes of mutants blocked at different steps reveal the function of each gene in a pathway. The chapter ends with two examples from human and fly behavior and vision in which mutations exposed the molecular basis of a phenotype: the circadian clock and color vision. Sequence-level definitions of the gene and its parts are in [7.2.1](/7.2.1) and [7.2.2](/7.2.2); the use of these principles in the genetic analysis of development is taken up in 7.4.20.

## 13.1. Complementation Groups

### 13.1.1. From Pairwise Tests to Genes

When two recessive mutations with the same phenotype are combined in one **diploid** (or in a bacterial **merodiploid**, or a cell infected by two phages), the phenotype is **wild type** if they lie in different genes (each **genome** supplies the product the other lacks) and mutant if they lie in the same gene (neither genome has a functional copy). The mutations that fail to complement each other form a **complementation group**, and a **complementation group** corresponds to a gene ([7.4.4](/7.4.4)). With many mutations, the tests are arranged in a matrix, and the groups are read off by a simple procedure.

**Algorithm 13.1.1 (Complementation Groups from a Complementation Matrix)** Input: $n$ recessive mutations and the results of all pairwise **complementation tests**.

1. Confirm that each mutation is recessive to the wild type (in a **heterozygote** with the wild-type **allele**); a **dominant** mutation cannot be tested.
2. Form a graph with the mutations as vertices and an edge between every pair that fails to complement.
3. The complementation groups are the connected components of the graph, found by depth-first search or union–find in time proportional to the $n^2$ tests. Each component is a gene; the number of components is the number of genes represented.
4. Check that each component is a clique: every pair within a component should fail to complement. If $a$ fails with $b$ and $b$ with $c$, but $a$ complements $c$, the relation is not transitive, and one of the exceptions below must be considered before the groups are accepted.

Step 4 matters because failure to complement is an equivalence relation only in the simple model, where every mutation inactivates exactly one gene and does nothing else.

**Example 13.1.1 (Eye-Color Mutations of *Drosophila*)** Nine recessive X-linked mutations change eye color: *white*, *garnet*, *ruby*, *vermilion*, *cherry*, *coral*, *apricot*, *buff* and *carnation*. Females heterozygous for each pair are tested. *white* fails to complement *cherry*, *coral*, *apricot* and *buff*, and these four fail to complement one another; every other pair complements. The graph has five components: $\{white, cherry, coral, apricot, buff\}$ and the four singletons $\{garnet\}$, $\{ruby\}$, $\{vermilion\}$, $\{carnation\}$. The nine mutations therefore lie in five genes, and *cherry*, *coral*, *apricot* and *buff* are alleles of *white*, members of a **multiple alleles** series with different residual activities (the colors range from white through pale yellow to near-red); each component is a clique, so the grouping is consistent.

![Complementation groups from a complementation matrix (Algorithm 13.1.1, Example 13.1.1). A: results of the pairwise tests among nine recessive X-linked eye-color mutations of *Drosophila* in trans-heterozygous females; "+" (green) means wild-type eyes, complementation, and "−" (red) means mutant eyes, failure to complement; the diagonal is each mutation against itself. B: the same matrix with rows and columns reordered by the connected components of the "fails to complement" graph: a block of five mutually noncomplementing alleles of *white* and four single-member groups, five genes in all.](./plots/complementation-matrix.py)

### 13.1.2. Exceptions to the Simple Rule

Three situations break the correspondence between noncomplementation and allelism.

**Definition 13.1.1 (Intragenic Complementation)** **Intragenic complementation** is the restoration of function in a heterozygote for two mutant alleles of the same gene, usually because the gene product is a **multimer** and the two mutant **polypeptides**, defective in different domains, assemble into a partly functional complex.

Intragenic complementation is typically partial and occurs only between some pairs of alleles, so it makes the matrix nontransitive: two alleles $a$ and $c$ complement each other, while both fail to complement a third allele $b$ (for example a **null allele**). The classic cases are **enzymes** such as the β-galactosidase of *E. coli* (**α-complementation**, [7.2.5](/7.2.5), is the extreme form) and many yeast biosynthetic enzymes. Second, a **dominant negative allele** (Formula 12.3.1) fails to complement every allele of its own gene, and sometimes alleles of genes whose products bind to its product. Third, *nonallelic noncomplementation* (second-site noncomplementation) occurs when heterozygosity for recessive mutations in two different genes whose products interact reduces function below the threshold, as for mutations in α- and β-tubulin genes of yeast and *Drosophila*: the failure to complement then indicates a physical or functional interaction rather than allelism. Mutations are therefore assigned to a gene with more confidence when they also map to the same position by recombination (Section 13.2) and, today, when the mutations are found in the same coding sequence.

### 13.1.3. The Cistron and the Cis–Trans Test

**Definition 13.1.2 (Cis–Trans Test and Cistron)** The **cis–trans test** compares the phenotype of a double heterozygote for two recessive mutations in the *trans* configuration ($a_1\,{+}/{+}\,a_2$, one mutation on each homolog) with that in the *cis* configuration ($a_1\,a_2/{+}\,{+}$, both on the same homolog). If the cis heterozygote is wild type (both mutations recessive and not interacting) but the trans heterozygote is mutant, the two mutations lie in the same functional unit, called a **cistron**; if both are wild type, they lie in different cistrons.

The **cis configuration** is the control that makes the trans result interpretable: it shows that the mutations are recessive when a wild-type copy of the whole unit is present. Benzer (1957) introduced the term cistron for the unit so defined; in practice it is a synonym of gene in the functional sense, a stretch of DNA encoding one polypeptide or functional RNA. In bacteria the test is done in merodiploids made with **F′ plasmids** ([7.4.10](/7.4.10)); cis–trans tests of regulatory mutations of the *lac* **operon** distinguished cis-acting sites from trans-acting **proteins** ([7.2.11](/7.2.11)), a distinction that the complementation test of coding mutations alone cannot make.

The logic of the regulatory tests can be written as two questions about each mutation $x$ in a merodiploid. Is $x$ dominant or recessive to the wild type? And does it act only on the genes of its own DNA molecule (cis) or on both molecules (trans)? The second question is answered by placing a recessive structural mutation, $Z^{-}$, either on the same molecule as $x$ or on the other one, so that the enzyme reports which copy is expressed.

**Example 13.1.2 (Classifying Constitutive Mutations of the *lac* Operon)** Three independent mutants $c_1$, $c_2$, $c_3$ make β-galactosidase without **inducer**. Each is tested in two merodiploids (**chromosome** / F′), and the β-galactosidase is measured without and with the inducer IPTG:

| Merodiploid | $c_1$ | $c_2$ | $c_3$ |
|---|---|---|---|
| (i) $x\,Z^{+}$ / F′ $I^{+}O^{+}Z^{-}$ | inducible | constitutive | constitutive |
| (ii) $x\,Z^{-}$ / F′ $I^{+}O^{+}Z^{+}$ | inducible | inducible | constitutive |

Test (i) shows that $c_1$ is recessive: a wild-type copy restores regulation of the enzyme made from the chromosome, so the wild-type product acts in trans, and $c_1$ is an $I^{-}$ allele of the **repressor** gene. $c_2$ is dominant in (i) but has no effect on the $Z^{+}$ copy of the other molecule in (ii): it acts only in cis and is an operator-constitutive mutation $O^{c}$. $c_3$ is dominant and acts in trans on the other molecule's genes: a dominant negative repressor allele $I^{-\mathrm{d}}$, which poisons the tetramers that contain wild-type **subunits** (Formula 12.3.1). Noninducible mutants are classified in the same way: a super-repressor $I^{\mathrm{s}}$ is dominant and acts in trans, and a **promoter** mutation $P^{-}$ prevents expression only of the genes in cis. The full set of **genotypes**, with the molecular interpretation, is in [7.2.11](/7.2.11#sec-11.2.1).

### 13.1.4. The Gene in Molecular Terms

The functional definition of the gene by the cis–trans test, the unit that makes one product, survived the molecular analysis of genes, but several refinements were needed. Jacob and Monod distinguished *structural genes*, which encode the enzymes and other proteins or RNAs whose function is measured, from *regulatory genes*, such as *lacI*, whose products control the expression of other genes; the distinction is one of role, since a regulatory gene is itself a transcribed, complementable unit, unlike a cis-acting site such as an **operator**.

| Finding | Consequence for the gene concept | Details |
|---|---|---|
| Operons transcribed as **polycistronic mRNA** in bacteria | one **transcription** unit can contain several cistrons; eukaryotic **mRNAs** are mostly monocistronic | [7.2.11](/7.2.11) |
| Split genes: **exons** and **introns** | a gene is not a continuous stretch of coding DNA; **alternative splicing** makes several products from one gene | [7.2.2](/7.2.2#sec-2.4), [7.2.16](/7.2.16) |
| Overlapping and nested genes | one DNA sequence can belong to two genes, read in different frames or on opposite strands | [7.2.2](/7.2.2#sec-2.5) |
| Genes for RNAs | the product can be an rRNA, **tRNA** or regulatory RNA, not a polypeptide | [7.2.2](/7.2.2#sec-2.6) |
| **Pseudogenes** | gene-like sequences without function | [7.2.2](/7.2.2#sec-2.2.5) |
| **Transposable elements** ("jumping genes") | the position of a sequence in the genome can change | [7.4.17](/7.4.17) |
| Cis-regulatory elements, often far from the coding sequence | mutations that affect a gene can lie outside its transcribed region | [7.2.14](/7.2.14) |

A current working definition is that a gene is a region of DNA that is transcribed into a functional product, together with the sequences that regulate its expression; mutations within it that destroy the product fall into one complementation group.

## 13.2. Benzer's Fine Structure of the rII Region

### 13.2.1. A System of Extreme Resolution

Recombination between two mutations in the same gene should be very rare, because they are very close: it was not known in 1950 whether a gene could be divided by recombination at all, or whether it behaved like a bead on a string. Seymour Benzer (1955–1961) found an experimental system in which a **recombination frequency** of $10^{-6}$ could be measured. He used *rII* mutants of bacteriophage T4. Wild-type T4 forms small, fuzzy plaques on *E. coli* strain B and grows on strain K(λ), a K-12 strain lysogenic for phage λ (**lysogeny**, [7.2.11](/7.2.11)). An *rII* mutant forms large, sharp-edged plaques on B (rapid lysis) but cannot grow at all on K(λ). This difference gives both a screen (large plaques on B identify new mutants) and a selection (only $rII^{+}$ phage form plaques on K(λ)).

The complementation test is done by coinfection: K(λ) cells infected simultaneously with two *rII* mutants lyse and release phage if the mutations complement, but not if they do not. Benzer's mutations fell into two complementation groups, the cistrons *rIIA* and *rIIB*, and all *rIIA* mutations mapped on one side of the region and all *rIIB* mutations on the other.

### 13.2.2. Measuring Recombination within a Gene

To cross two mutants of the same cistron, Benzer coinfected strain B, on which both grow, with an excess of both, and plated the progeny on B (all phage form plaques) and on K(λ) (only $rII^{+}$ recombinants form plaques). Each $rII^{+}$ recombinant has a reciprocal double mutant, which cannot be distinguished from the parents.

**Formula 13.2.1 (Recombination Frequency in a Phage Cross)** If a lysate from a cross of two *rII* mutants contains $K$ plaque-forming units per milliliter on *E. coli* K(λ) and $B$ per milliliter on *E. coli* B (both corrected for their dilutions),

$$
\mathrm{RF} = \frac{2K}{B},
$$
in **map units** when multiplied by 100. The factor 2 counts the undetected reciprocal double-mutant recombinants. The measurement is valid only if $K$ greatly exceeds the **reversion** frequency of each parent alone, determined in single-mutant control infections.

Because a single plate of K(λ) can be seeded with $10^{8}$ or more phage and every $rII^{+}$ recombinant gives a plaque, recombination frequencies down to the reversion background (about $10^{-6}$ to $10^{-8}$ for most **point mutations**) could be detected. The smallest nonzero recombination frequency between two *rII* mutations was about $0.02$ map units ($2 \times 10^{-4}$). With a T4 **genetic map** of about 1500 map units over $169\,\mathrm{kb}$ (the figures Benzer used), 1 map unit corresponds to about $110\,\mathrm{bp}$, so $0.02$ map units is about $2\,\mathrm{bp}$: recombination can occur between mutations at adjacent or nearly adjacent **base pairs**. Benzer concluded that a gene consists of many mutable sites arranged in a linear order, separable by recombination, the structure later identified with a sequence of base pairs.

### 13.2.3. Deletion Mapping

Mapping several thousand mutations by **two-point crosses** would have required millions of crosses. Benzer used mutants that do not revert, which turned out to be deletions removing parts of the region.

**Definition 13.2.1 (Deletion Mapping)** **Deletion mapping** locates a point mutation by crossing it with a set of deletion mutants whose deleted segments overlap in a known way: wild-type recombinants can arise only if the point mutation lies outside the deleted segment, so the pattern of crosses that give and do not give wild-type recombinants assigns the mutation to the interval defined by the deletion end points.

**Algorithm 13.2.1 (Assigning a Mutation to a Deletion Interval)** 1. Order a set of overlapping deletions by their end points, which divides the region into intervals; each interval is characterized by the set of deletions that cover it. 2. Cross the new point mutation with each deletion and score the presence (+) or absence (−) of wild-type recombinants. 3. The mutation lies in the interval covered by exactly the deletions that gave −. 4. Repeat with a second set of smaller deletions within that interval, and finally map by two-point crosses only against the mutations in the same small interval. With $k$ well-chosen deletions, $2^k$ intervals can in principle be distinguished, so a thousand mutations are located with tens of crosses each rather than a thousand.

A deletion can also be mapped with respect to another deletion: two overlapping deletions give no wild-type recombinants. Deletion mapping is a general method: in *Drosophila*, collections of chromosomal deficiencies that tile the genome are used in the same way to map new recessive mutations (a mutation uncovered by a deficiency shows its mutant phenotype over the deficiency, a pseudodominance treated in 7.4.15).

![Deletion mapping of a point mutation (Definition 13.2.1, Algorithm 13.2.1; schematic). The rII region, comprising the cistrons *rIIA* and *rIIB*, is divided into seven intervals by the end points of seven overlapping deletions Df1–Df7 (pink: deleted segment; black: retained DNA). A point mutant crossed with each deletion gives wild-type recombinants (+) only if the deletion does not cover the mutation. Here Df1–Df5 give no wild-type progeny and Df6 and Df7 do, which places the mutation (yellow) in interval 4 of *rIIA*; it is then mapped finely by two-point crosses against the other mutations in interval 4 only.](./plots/deletion-mapping.py)

### 13.2.4. Mutational Hotspots

Benzer mapped 1612 spontaneous *rII* mutations and many induced ones. They were not evenly distributed. Most sites were hit once or a few times, but a few sites were hit hundreds of times; one site in *rIIB* accounted for more than 500 of the spontaneous mutations.

**Definition 13.2.2 (Mutational Hotspot)** A **mutational hotspot** is a site in the genome at which mutations arise at a much higher rate than at most other sites, recognized as a site with many more independent occurrences than expected if all sites mutated at the same rate.

If all $S$ mutable sites had the same rate, the numbers of independent mutations per site after $n$ mutations would follow a **Poisson distribution** with mean $n/S$, and the number of sites with $k$ hits would be $S\,\mathrm{e}^{-\lambda}\lambda^k/k!$. The observed distribution has both an excess of sites with many hits (hotspots) and an excess of sites with few or none (coldspots): the rates vary over orders of magnitude. The Poisson calculation also gives a lower bound on the number of sites not yet hit.

**Formula 13.2.2 (Unseen Mutable Sites)** If $n_1$ sites have been hit once and $n_2$ twice, and the low-rate sites are treated as one Poisson class with mean $\lambda$, then $n_2/n_1 = \lambda/2$, and the number of sites of that class not yet hit is

$$
\hat n_0 = n_1\,\mathrm{e}^{-\lambda}/(\lambda\,\mathrm{e}^{-\lambda}) = \frac{n_1}{\hat\lambda} = \frac{n_1^2}{2n_2}.
$$
Because rates vary within the class, this is an underestimate (the **estimator** $n_1^2/(2n_2)$ is Chao's lower bound for the number of unseen species, the same problem in ecology).

Benzer concluded from the distribution that many sites of the *rII* region had not yet been hit, and that a saturating map would need far more mutations. Hotspots differ for different **mutagens**, which have their own chemical specificities (Section 12.7 of [7.4.12](/7.4.12)); many spontaneous hotspots were later found to be 5-methylcytosines, which deaminate to thymine (and T4 hotspots at runs of identical bases, which favor slippage).

![Mutational hotspots, simulated after the pattern of Benzer's rII data (Definition 13.2.2). A: 1600 independent spontaneous mutations distributed over 400 mutable sites whose rates vary (gamma distributed), with two hotspots about 100 times as mutable as a typical site. B: number of sites with k = 0, 1, 2, … mutations (bars) compared with the Poisson distribution expected if all sites had the same rate (points, mean 4): the data have far more sites with no or one mutation and a long tail of sites with many, and the two hotspots lie far beyond the axis.](./plots/hotspots.py)

## 13.3. Map Units and Base Pairs

The relation between genetic and physical distance differs enormously among organisms, because the number of **crossovers** per **meiosis** (or per phage cross) is roughly constant per chromosome arm, whereas genome sizes differ by orders of magnitude.

| Organism | Genome size | Total genetic map | Approximate base pairs per map unit (cM) |
|---|---|---|---|
| Phage T4 | $169\,\mathrm{kb}$ | about 1500 map units (estimates vary) | $100$–$200\,\mathrm{bp}$ |
| *Saccharomyces cerevisiae* | $12\,\mathrm{Mb}$ | about $4200\,\mathrm{cM}$ | about $3\,\mathrm{kb}$ |
| *Caenorhabditis elegans* | $100\,\mathrm{Mb}$ | about $300\,\mathrm{cM}$ | about $330\,\mathrm{kb}$ |
| *Drosophila melanogaster* (female meiosis) | about $140\,\mathrm{Mb}$ (**euchromatin** about $120\,\mathrm{Mb}$) | about $280\,\mathrm{cM}$ | about $500\,\mathrm{kb}$ |
| Human (sex-averaged) | $3.1\,\mathrm{Gb}$ | about $3500\,\mathrm{cM}$ | about $0.9\,\mathrm{Mb}$ ("1 cM ≈ 1 Mb") |

**Example 13.3.1** Two point mutations $2\,\mathrm{kb}$ apart within a gene are expected to recombine with a frequency of about $2/0.9 \times 10^{-3}\,\mathrm{cM}$, that is $2 \times 10^{-5}$, in humans: one recombinant per $50\,000$ meioses, impossible to observe in families. In yeast the same distance is about $0.7\,\mathrm{cM}$, one recombinant **tetrad** spore in about 150, and in T4 about 18 map units. This is why intragenic recombination was studied in phage, bacteria and fungi, and why the fine structure of human genes is studied by sequencing rather than recombination. Recombination within a gene in fungi also produces **gene conversion** (non-reciprocal transfer between alleles, [7.4.9](/7.4.9)), so very close mutations do not always behave like points on a line.

Averages hide variation within genomes: recombination is concentrated in hotspots of 1–2 kb (in mammals defined by PRDM9 binding **motifs**), so the local ratio varies by orders of magnitude ([7.4.8](/7.4.8)).

## 13.4. Mutations Reveal Gene Function

### 13.4.1. One Gene, One Enzyme

George Beadle and Edward Tatum (1941) irradiated *Neurospora crassa* and screened for mutants that could not grow on minimal medium (salts, sugar and **biotin**) but could grow on medium supplemented with amino acids and **vitamins**: nutritional mutants (**auxotrophs**, [7.4.10](/7.4.10)). Each mutant could be rescued by a single nutrient. Among the arginine-requiring mutants, recombination placed the mutations in four regions and complementation tests sorted them into four complementation groups, the genes *ARG-E*, *ARG-F*, *ARG-G* and *ARG-H*. The mutants differed in which intermediates of arginine synthesis could replace arginine.

| Mutant class | Minimal | + ornithine | + citrulline | + argininosuccinate | + arginine |
|---|---|---|---|---|---|
| wild type | + | + | + | + | + |
| *ARG-E* | − | + | + | + | + |
| *ARG-F* | − | − | + | + | + |
| *ARG-G* | − | − | − | + | + |
| *ARG-H* | − | − | − | − | + |

**Definition 13.4.1 (One Gene, One Enzyme Hypothesis)** The **one gene, one enzyme hypothesis** (Beadle and Tatum 1941) states that each gene specifies one enzyme, so that a mutation in a gene blocks a single step of a biochemical pathway. It was generalized to one gene, one polypeptide, and now to the statement that each gene specifies one or more functional products, polypeptides or RNAs.

**Algorithm 13.4.1 (Ordering a Pathway from Growth Tests)** Given auxotrophic mutants, each blocked in one step, and a set of intermediates:

1. For each mutant, list the compounds that support its growth. A compound supports growth if and only if it lies downstream of the mutant's block.
2. Order the compounds by the number of mutants they rescue: the end product rescues all, and a compound earlier in the pathway rescues fewer mutants. Order the mutants by the number of compounds that rescue them: the mutant rescued by the most compounds is blocked earliest.
3. Check with accumulation: a mutant accumulates the intermediate immediately before its block, and a double mutant accumulates the intermediate before the earlier block (the earlier block is **epistatic**, [7.4.4](/7.4.4)).
4. If two mutants are rescued by the same set of compounds, their order is not resolved by growth tests; use accumulation, double mutants or enzyme assays.

For the table, ornithine rescues three mutant classes, citrulline two and argininosuccinate one, so the order is (precursor) → ornithine → citrulline → argininosuccinate → arginine, with *ARG-E* blocked before ornithine (in the conversion of *N*-acetylornithine), *ARG-F* between ornithine and citrulline, *ARG-G* between citrulline and argininosuccinate and *ARG-H* in the last step. The four genes encode acetylornithine deacetylase, ornithine transcarbamylase, argininosuccinate synthetase and argininosuccinate lyase; the last three are the enzymes of the **urea cycle** in mammals ([7.1.22](/7.1.22)).

![One gene, one enzyme in the arginine pathway of *Neurospora* (Definition 13.4.1, Algorithm 13.4.1). Top: the pathway from N-acetylornithine through ornithine, citrulline and argininosuccinate to arginine, each step catalyzed by the enzyme encoded by one of four genes, *ARG-E*, *ARG-F*, *ARG-G* and *ARG-H*. Bottom: growth (+) or no growth (−) of the wild type and the four classes of mutants on minimal medium alone or with one supplement. Each mutant grows on every compound downstream of its block, so the number of compounds that rescue a mutant decreases along the pathway and orders the steps.](./plots/arginine-pathway.py)

The hypothesis has well-known limits: many proteins are not enzymes; one enzyme may consist of several polypeptides encoded by different genes (so several complementation groups give one enzyme), or one polypeptide may carry several activities (so one gene controls several steps); a gene may give several products by alternative **splicing** ([7.2.16](/7.2.16)); and many genes encode functional RNAs. The idea that mutations block identifiable steps in a process, and that the order of steps can be deduced from the phenotypes of single and double mutants, has outlived its original form: it is the basis of epistasis analysis of signaling and developmental pathways (7.4.20).

### 13.4.2. From Behavior to Genes: the period Mutants

The same logic works for phenotypes far from **metabolism**. Ronald Konopka and Seymour Benzer (1971) mutagenized *Drosophila* males with EMS and screened the X chromosomes of their progeny for altered daily rhythms of eclosion (emergence of adults from pupae) and locomotor activity. They found three mutants: one arrhythmic, one with a short period of about 19 hours and one with a long period of about 28 hours, compared with about 24 hours in the wild type. The three mutations failed to complement each other and mapped by recombination with visible **X-linked** markers to the same position (band 3B1–2 of the polytene X chromosome). They were therefore alleles of one gene, *period*: $per^{0}$, $per^{S}$ and $per^{L}$. An **allelic series** that can shorten, lengthen or abolish the rhythm suggested that the gene product is part of the clock mechanism rather than an output; the gene was cloned in 1984, and the negative feedback of PER and TIM proteins on their own transcription was shown by Jeffrey Hall, Michael Rosbash and Michael Young (Nobel Prize 2017). The transcriptional feedback loop and its dynamics are a subject of systems biology (7.9).

## 13.5. A Synthesis: Mutations in the Genes for Vision

Human vision depends on four light-sensitive pigments, each an opsin protein with the chromophore 11-*cis*-retinal: **rhodopsin** in the rods, for dim light, and three cone opsins, for short (S, "blue"), middle (M, "green") and long (L, "red") wavelengths. Mutations in their genes illustrate almost every concept of this and the previous chapters.

- The **rhodopsin** gene *RHO* lies on chromosome 3. More than 100 **missense mutations** cause **autosomal** dominant retinitis pigmentosa, a progressive degeneration of rods; the commonest in North America, P23H, causes misfolding of rhodopsin, which accumulates in the ER and is toxic to the rod (a dominant **gain of function** by misfolding, Section 12.3 of [7.4.12](/7.4.12)). Other alleles are recessive nulls or cause stationary night blindness by constitutive activity (**hypermorphs**).
- The S opsin gene lies on chromosome 7; mutations cause rare autosomal dominant tritan defects.
- The L and M opsin genes lie in a tandem array at Xq28: one L gene followed by one or more M genes. The genes are about $96\,\%$ identical in sequence (they arose by a duplication in the ancestor of Old World primates, which gave them trichromatic vision), and the whole repeat units of about $39\,\mathrm{kb}$ are similar enough to pair out of register in female meiosis.

Jeremy Nathans and colleagues (1986) found that most red–green color vision defects are caused by **unequal crossing over** between misaligned arrays. A crossover between genes produces one X with no M gene (deuteranopia, inability to distinguish red from green because the M pigment is missing) and a reciprocal X with an extra M gene (normal vision). A crossover within misaligned L and M genes produces hybrid genes, part L and part M; their pigments have intermediate spectral sensitivities, determined mainly by a few amino-acid differences encoded in exons 3 and 5, and cause anomalous trichromacy (deuteranomaly or protanomaly) or, when the hybrid is the only gene expressed, dichromacy. Because only the first two genes of the array are expressed (under a **locus** control region upstream), extra M genes are usually silent. Red–green defects affect about $8\,\%$ of men of European descent and about $0.5\,\%$ of women, the pattern of an **X-linked** recessive trait: with allele frequency $q = 0.08$ in males, the expected frequency among females is $q^2 = 0.0064$ ([7.4.6](/7.4.6)). Unequal crossing over as a mechanism of duplication and deletion is treated in 7.4.15.

![Unequal crossing over in the X-linked opsin gene array (schematic). Top: a normal array on Xq28 with one long-wavelength (L, red) and one middle-wavelength (M, green) opsin gene. (1) Two arrays pair out of register, with the M gene of one opposite the L gene of the other, and a crossover occurs between genes (yellow cross): one product has lost its M gene (deuteranopia) and the other has gained an extra M gene (normal vision). (2) A crossover within the misaligned L and M genes produces hybrid genes: an X carrying only an L/M hybrid (5′ part from L, 3′ part from M), whose pigment has a shifted sensitivity (dichromacy), and an X carrying an L, an M/L hybrid and an M gene.](./plots/opsin-unequal.py)

## Summary

| Topic | Key results |
|---|---|
| Complementation groups (Algorithm 13.1.1, Example 13.1.1) | noncomplementation graph → connected components = genes; check cliques; *white* example: 9 mutations, 5 genes |
| Exceptions (Definition 13.1.1) | intragenic complementation (multimers, partial, nontransitive); dominant negatives; nonallelic noncomplementation (interacting products) |
| Cistron (Definition 13.1.2) | cis heterozygote is the control; trans mutant → same cistron; F′ merodiploids; cis-acting sites vs trans-acting products |
| Regulatory mutations (Example 13.1.2) | dominance test plus a $Z^{-}$ reporter in cis or trans: $I^{-}$ recessive, trans; $O^{c}$ dominant, cis only; $I^{-\mathrm{d}}$ and $I^{\mathrm{s}}$ dominant, trans; $P^{-}$ cis |
| The gene in molecular terms (13.1.4) | structural vs regulatory genes; polycistronic units, split, overlapping and nested genes, RNA genes, **pseudogenes**, transposons, distant cis-regulatory elements |
| rII system (13.2.1, Formula 13.2.1) | screen (large plaques on B) and selection (growth on K(λ)); $\mathrm{RF} = 2K/B$; detection to about $10^{-6}$; smallest RF 0.02 map units ≈ 2 bp; a gene is a linear array of mutable sites |
| Deletion mapping (Definition 13.2.1, Algorithm 13.2.1) | no wild-type recombinants if the deletion covers the mutation; $k$ deletions → up to $2^k$ intervals |
| Hotspots (Definition 13.2.2, Formula 13.2.2) | non-Poisson counts per site; unseen sites $\ge n_1^2/(2n_2)$; 5-methylcytosine and mutagen-specific hotspots |
| bp per map unit (13.3, Example 13.3.1) | T4 about 100–200 bp, yeast about 3 kb, *Drosophila* about 500 kb, human about 0.9 Mb per cM; intragenic recombination observable only in microbes |
| Gene function (Definition 13.4.1, Algorithm 13.4.1) | Beadle–Tatum arginine mutants: the more compounds rescue, the earlier the block; accumulation and double mutants confirm; one gene, one polypeptide and its limits |
| Behavior (13.4.2) | *period*: $per^{0}$, $per^{S}$ (19 h), $per^{L}$ (28 h), one complementation group, one locus; clock component |
| Vision (13.5) | *RHO* dominant misfolding alleles; L/M array on Xq28; unequal crossing over → deletion of M, hybrid genes; 8% of men, $q^2$ in women |

## Questions

1. Seven recessive mutants with the same phenotype are tested in all pairs. The pairs that fail to complement are (1, 3), (1, 6), (2, 5), (3, 6) and (4, 7); all others complement. How many genes are represented, and which mutations are alleles?

   **Answer** The noncomplementation graph has components $\{1, 3, 6\}$, $\{2, 5\}$ and $\{4, 7\}$; each is a clique (1–3, 1–6, 3–6 all fail), so there are three genes (Algorithm 13.1.1).

2. In a set of mutations, $a$ fails to complement $b$, $b$ fails to complement $c$, but $a$ complements $c$. Give two explanations, and an experiment to decide between them.

   **Answer** (i) Intragenic complementation: $a$, $b$ and $c$ are alleles of one gene encoding a multimer; $a$ and $c$ are defective in different domains and their polypeptides form a partly active complex, while $b$ (for example a null or a mutation affecting both functions) complements neither (Definition 13.1.1). (ii) $b$ is a dominant negative or a deletion that removes or poisons two adjacent genes, one containing $a$ and the other $c$, or $b$ causes nonallelic noncomplementation with one of them. Map $a$, $b$ and $c$ by recombination (or sequence them): if all lie in one transcription unit, (i) is likely; if $a$ and $c$ map to different genes and $b$ is a deletion spanning both, (ii). Testing $b$ over the wild type shows whether $b$ itself is dominant.

3. A lysate from a cross of two *rIIA* mutants is diluted $10^{-6}$ and $0.1\,\mathrm{mL}$ is plated on *E. coli* B, giving 230 plaques; diluted $10^{-2}$, $0.1\,\mathrm{mL}$ on K(λ) gives 460 plaques. Single-mutant controls give no plaques on K(λ) at the same dilution. (a) Compute the recombination frequency and the distance in map units. (b) Using $113\,\mathrm{bp}$ per map unit, estimate the distance in base pairs.

   **Answer** (a) $B = 230 \times 10^{6} \times 10 = 2.3 \times 10^{9}$ per mL; $K = 460 \times 10^{2} \times 10 = 4.6 \times 10^{5}$ per mL. $\mathrm{RF} = 2K/B = 4 \times 10^{-4}$, or $0.04$ map units (Formula 13.2.1). (b) $0.04 \times 113 \approx 4.5\,\mathrm{bp}$, so the mutations are a few base pairs apart.

4. Using the seven deletions of the deletion-mapping figure, a new point mutation gives wild-type recombinants with Df5, Df6 and Df7 but not with Df1–Df4. In which interval does it lie? Which patterns would place it in intervals 1 and 7?

   **Answer** Df1 to Df4 cover it, Df5 (intervals 1–4) does not, so it lies beyond the end of Df5 but within Df4 and not within Df6 (intervals 6–7): interval 5. Interval 1: covered only by Df1 and Df5 (− with Df1, Df5; + with Df2, Df3, Df4, Df6, Df7). Interval 7: covered by Df1, Df2, Df3, Df4, Df6 and Df7 (+ only with Df5) (Algorithm 13.2.1).

5. In a collection of independent spontaneous mutations of a gene, 120 sites were hit once and 40 sites twice. Estimate the number of mutable sites of the same low-rate class not yet hit. Why is this a lower bound?

   **Answer** $\hat\lambda = 2n_2/n_1 = 0.67$, $\hat n_0 = n_1^2/(2n_2) = 14\,400/80 = 180$ (Formula 13.2.2). It is a lower bound because rates vary among sites even within the "low-rate" class; sites with very low rates are underrepresented among those hit once or twice, so more of them remain unseen than a single Poisson class predicts.

6. Four auxotrophs require compound P for growth. Mutant 1 grows only on P; mutant 2 grows on Z or P; mutant 3 grows on X, Z or P; mutant 4 grows on Y, X, Z or P. (a) Give the order of the intermediates and the position of each block. (b) Which intermediate accumulates in mutant 2, and which in the double mutant 2 3? (c) Which mutant is epistatic in the double mutant 1 4?

   **Answer** (a) Y → X → Z → P, with mutant 4 blocked before Y, mutant 3 between Y and X, mutant 2 between X and Z and mutant 1 between Z and P (Algorithm 13.4.1). (b) Mutant 2 accumulates X; the double mutant 2 3 is blocked earlier at the step of mutant 3 and accumulates Y. (c) The double mutant 1 4 is blocked both before Y and between Z and P. It grows only on P (the requirement of mutant 1), but it accumulates the precursor of Y, the accumulation phenotype of mutant 4: for accumulation, the earlier block (mutant 4) is epistatic.

7. In the arginine pathway, a new mutant grows on citrulline and arginine but not on ornithine. A second new mutant grows only on arginine. Which known genes might they be in, and how would you check?

   **Answer** The first behaves like *ARG-F* (block between ornithine and citrulline); the second like *ARG-H* or *ARG-G*, unless it grows on argininosuccinate (then *ARG-H*: it should grow on argininosuccinate if the block is the last step; if it does not, *ARG-G*). Confirm by complementation tests with tester strains of *ARG-E* to *ARG-H* (in **heterokaryons**), by recombination mapping, by accumulation (the first should accumulate ornithine) and by enzyme assays.

8. Two mutations are $2\,\mathrm{kb}$ apart within a gene. Estimate their recombination frequency in human, *Drosophila*, yeast and T4, and the number of meioses (or progeny) needed to see one recombinant in each.

   **Answer** Human (about $0.9\,\mathrm{Mb/cM}$): $2.2 \times 10^{-3}\,\mathrm{cM}$, RF $\approx 2 \times 10^{-5}$, about $45\,000$ meioses. *Drosophila* (about $500\,\mathrm{kb/cM}$): $0.004\,\mathrm{cM}$, RF $4 \times 10^{-5}$, about $25\,000$ progeny. Yeast (about $3\,\mathrm{kb/cM}$): $0.7\,\mathrm{cM}$, RF $7 \times 10^{-3}$, about 150 spores. T4 ($113\,\mathrm{bp}$ per map unit): about 18 map units, RF $0.18$: recombinants among every few progeny. (Example 13.3.1.)

9. A woman with normal color vision has a deuteranopic father. (a) What is the probability that her son is deuteranopic? (b) If the frequency of red–green defects among men in her population is $8\,\%$, what fraction of women are expected to be affected, and what fraction carriers?

   **Answer** (a) She received her father's X and is a carrier (assuming her mother's X is normal); each son has probability $1/2$ of receiving it: $1/2$. (b) With $q = 0.08$: affected women $q^2 = 0.0064$; carriers $2q(1 - q) = 0.147$ (Hardy–Weinberg proportions, treated in 7.4.22). The observed female frequency (about $0.4$–$0.5\,\%$) is close to $q^2$; some heterozygotes for different defects (one protan, one deutan X) are not affected, because each X supplies the pigment the other lacks, a complementation between X chromosomes.

10. In a cis–trans test in *E. coli* F′ merodiploids, two recessive *lacZ* mutations $z_1$ and $z_2$ give a Lac⁺ phenotype in the cis configuration ($z_1 z_2/{+}{+}$) and a Lac⁻ phenotype in trans ($z_1{+}/{+}z_2$). A third mutation, $o^{c}$, gives constitutive expression in cis with a wild-type *lacZ* but not in trans. Interpret both results.

    **Answer** $z_1$ and $z_2$ are in the same cistron: in trans neither copy makes a functional β-galactosidase, while in cis the wild-type copy supplies it (Definition 13.1.2). $o^{c}$ is a cis-acting site mutation (an operator that no longer binds repressor): it affects only the genes on its own DNA molecule, so it is constitutive only for the *lacZ* in cis; a site has no diffusible product and cannot be complemented or act in trans ([7.2.11](/7.2.11)).

11. Konopka and Benzer's $per^{S}$, $per^{L}$ and $per^{0}$ mutations failed to complement each other. Why was this result informative, given that $per^{S}$ and $per^{L}$ are partly dominant? What additional evidence established that they are alleles?

    **Answer** Because the mutants were semidominant, complementation is not a clean test: a trans heterozygote $per^{S}/per^{L}$ could show an intermediate rhythm even if the mutations were in different genes. The decisive evidence was mapping: all three mapped to the same position on the X chromosome by recombination with visible markers, and none recombined with the others in the numbers of progeny examined; heterozygotes with a deficiency of the region ($per^{0}/\mathrm{Df}$ arrhythmic like $per^{0}$, $per^{S}/\mathrm{Df}$ short) confirmed that $per^{0}$ behaves as a null and that the alleles form an allelic series of one gene.

12. (Open question) Benzer's experiments are often summarized as showing that "the gene" is divisible into three different units: the unit of function (cistron), of recombination (recon) and of mutation (muton). How do these map onto the molecular gene, and which parts of the classical definition break down for eukaryotic genes?

    **Answer** Outline: the muton and the recon are a single base pair (mutations can change one pair; recombination can separate adjacent pairs, except where gene conversion and **mismatch repair** blur close sites). The cistron is the stretch of DNA encoding one polypeptide, defined by complementation. In **eukaryotes** the coding sequence is interrupted by introns, so the cistron is not a continuous DNA segment of the protein's length; alternative splicing and alternative promoters make one locus encode several polypeptides, and mutations in different exons may complement if they affect different isoforms; regulatory elements can lie far away and be shared by several genes; and overlapping and antisense transcription units exist. The functional (product-based) definition of the gene in [7.2.1](/7.2.1) replaces the classical one, but complementation remains the operational test of whether two mutations affect the same function.

13. Four mutants of the *lac* operon of *E. coli* are tested in merodiploids, and β-galactosidase and permease are measured without and with inducer. (a) $m_1$ makes no enzyme under any condition, and neither do $m_1/$F′ $I^{+}O^{+}Z^{+}Y^{+}$ cells. (b) $m_2$ makes inducible permease but no β-galactosidase; $m_2/$F′ $I^{+}O^{+}Z^{+}Y^{-}$ makes both, inducibly. (c) $m_3$ makes neither product; $m_3/$F′ $I^{+}O^{+}Z^{-}Y^{+}$ makes inducible permease but no β-galactosidase, and $m_3/$F′ $I^{+}O^{+}Z^{+}Y^{-}$ makes inducible β-galactosidase but no permease; $m_3$ maps between *lacI* and the operator. (d) $m_4$ makes both products without inducer, and $m_4/$F′ $I^{+}O^{+}Z^{+}Y^{+}$ is inducible. Classify each mutation.

    **Answer** (a) Noninducible and dominant in trans, silencing the F′ copy too: a super-repressor $I^{\mathrm{s}}$, whose repressor cannot bind inducer but binds both operators. (b) Only β-galactosidase is missing, regulation is normal, and the F′ $Z^{+}$ complements it: a recessive *lacZ* structural mutation. (c) Whatever the F′ carries, the genes on the chromosome are never expressed, while the F′ genes are expressed normally: $m_3$ acts only in cis and blocks expression of both genes **linked** to it, and its position outside *lacZ* excludes a polar mutation in *lacZ*: a promoter mutation $P^{-}$. (d) Constitutive and recessive: an $I^{-}$ allele of the repressor gene (Example 13.1.2).

14. Classify each of the following as a structural gene, a regulatory gene or a cis-acting site, and say whether a recessive **loss-of-function mutation** in it can be complemented in trans in a merodiploid: (a) *lacY*; (b) *lacI*; (c) the *lac* operator; (d) the gene for CAP (*crp*).

    **Answer** (a) Structural gene (permease); complemented in trans. (b) Regulatory gene (repressor); its $I^{-}$ alleles are complemented in trans by $I^{+}$. (c) Cis-acting site: it is not transcribed into a product, so $O^{c}$ is not complemented; it affects only the genes on its own molecule. (d) Regulatory gene (the activator CAP, encoded elsewhere in the genome); a *crp* null mutation, which lowers expression of all catabolite-sensitive operons, is complemented in trans by a wild-type *crp* copy (Section 13.1.4).
