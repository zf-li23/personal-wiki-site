---
title: The Evolution of Genes and Genomes
description: "How new genes arise (duplication by unequal crossing over, slippage, retrotransposition and whole-genome duplication; exon shuffling and domains; de novo genes; horizontal transfer), the fates of duplicates (loss, dosage, neofunctionalization, subfunctionalization and the DDC model, concerted evolution), the death of genes, drift and selection in coding sequences, the evolution of gene expression, the origin of introns, chromosome evolution by fusion, fission and inversion, and the evolution of genome size: transposable elements, genome reduction in endosymbionts and streamlined bacteria, and the role of drift."
---

Comparing genomes reveals a startling disconnect between the complexity of organisms and the DNA that underlies them. The human genome has about $3.2 \times 10^9$ base pairs and about 20 000 protein-coding genes; the nematode *Caenorhabditis elegans*, whose adult body has about a thousand cells, has about as many genes, bread wheat about five times as many, and pines several times as much DNA. The **C-value paradox** ([7.2.2](/7.2.2#sec-2.1.2)) is only one of the puzzles. Genomes are not refined machines: they are the outcome of mutation, selection, **genetic drift** and conflicts between genetic elements, and many of their features are better explained by population genetics than by adaptation.

The molecular machinery behind these changes is treated elsewhere: gene families, the fates of duplicates and de novo genes in [7.4.14](/7.4.14#sec-14.4), whole-genome duplication in [7.4.16](/7.4.16#sec-16.6.3), rearrangements in [7.4.15](/7.4.15), transposition in [7.2.9](/7.2.9) and [7.4.17](/7.4.17), splicing and the origin of the spliceosome in [7.2.16](/7.2.16#sec-16.8.2). This chapter asks the evolutionary questions: how often each kind of change happens, what decides whether it spreads, and what the answers tell us about the forces that shape genomes. It uses the population genetics of [7.10.5](/7.10.5) and [7.10.6](/7.10.6) and the measures of selection on sequences of [7.10.8](/7.10.8). Changes of gene regulation that build new phenotypes are the subject of [7.10.19](/7.10.19); the statistical models of codon evolution are in [7.10.23](/7.10.23); the genomes of prokaryotes and of organelles return in [7.10.27](/7.10.27) and [7.10.28](/7.10.28).

## 18.1. The Birth of a Gene

### 18.1.1. Gene Duplication

The lens of the vertebrate eye is made largely of transparent proteins, the crystallins. Many proteins happen to be nearly transparent, and the crystallins of different vertebrate groups derive from proteins with quite different original functions: α-crystallin from a small heat-shock protein, δ-crystallin from argininosuccinate lyase, ε-crystallin from lactate dehydrogenase, τ-crystallin from α-enolase. Some of them are encoded by a duplicate of the ancestral gene; others are the very same gene product doing two jobs at once (*gene sharing*): in ducks, lactate dehydrogenase B also serves as ε-crystallin, and residues conserved in the lactate dehydrogenases of other vertebrates have changed in this dual-function protein. Novelty at the molecular level, like novelty in general, arises by descent with modification of what already exists.

**Definition 18.1.1 (Gene Duplication)** A **gene duplication** is a mutation that produces an additional copy of a gene, or of a segment containing genes, in the genome. The copies descended from one duplication are **paralogs** ([7.1.4](/7.1.4#def-4.4.1)).

Duplication is the most common way that new genes arise in eukaryotes. Its mechanisms differ in what they copy and where the copy goes:

| Mechanism | What is copied | Where the copy lies | Features of the copy |
|---|---|---|---|
| **Unequal crossing over** | a segment, one or several genes | in tandem with the parental copy | keeps introns and nearby regulatory elements |
| Replication slippage | a short segment | in tandem | mostly repeats and exons |
| Retrotransposition of an mRNA | the spliced transcript | anywhere, often on another chromosome | no introns, no promoter, poly(A) tract: usually a **processed pseudogene** ([7.2.2](/7.2.2#sec-2.2.5)) |
| Segmental duplication (non-allelic **homologous recombination**) | kilobases to megabases | nearby or on other chromosomes | whole genes with their regulation |
| **Whole-genome duplication** ([Definition 16.6.1](/7.4.16#def-16.6.1)) | every gene | everywhere at once | stoichiometry of all products preserved |

A new duplicate first exists as a polymorphism in the number of copies, a copy number variant. At the human *AMY1* locus, which encodes salivary amylase, individuals carry from two to more than a dozen diploid copies, and people with more copies have more amylase in their saliva. Populations with starch-rich diets (Japanese, European Americans, the Hadza) carry on average 6.7 copies, populations with low-starch diets (the Biaka and Mbuti hunter-gatherers of central Africa) 5.4: a duplication whose frequency has apparently responded to diet.

Over evolutionary time, duplication is pervasive. In the recent evolution of humans about 1 % of the genes have been duplicated per million years, and some 1400 duplicates have been fixed in humans or chimpanzees since the two lineages separated about 7 million years ago; more of the base pairs that differ between the two species differ because of duplications and deletions than because of single-nucleotide substitutions. A duplication can be an adaptation in itself. The douc langur (*Pygathrix nemaeus*) eats leaves, which are fermented by bacteria in its foregut, and it gains nutrition by digesting the bacteria with a ribonuclease. Its *RNASE1B* gene arose by duplication of *RNASE1* about 4 Myr ago; since then the duplicate has accumulated nine nonsynonymous and three synonymous substitutions and the parental copy none, and the changes adapt the enzyme to the acidic conditions of the gut. The ratio of the two kinds of change, $d_{\mathrm{N}}/d_{\mathrm{S}} \approx 4$ (**dN/dS ratio**, Definition 8.1.2), is the signature of **positive selection**.

### 18.1.2. New Genes from Parts

Duplication can also copy parts of genes. Proteins are built of **domains**, compact units that fold and often function independently, and many proteins consist of repeated domains: the α subunit of the vertebrate voltage-gated sodium channel has four homologous domains, each with six membrane-spanning segments, which arose by two rounds of internal duplication of a gene that encoded a single domain, like the tetrameric sodium channels of bacteria.

**Definition 18.1.2 (Exon Shuffling)** **Exon shuffling** is the creation of new genes by the combination of exons, usually encoding protein domains, from different genes, through recombination within introns, by retrotransposition of one gene into another, or by duplication of exons.

The *jingwei* gene of *Drosophila teissieri* and *D. yakuba* shows how quickly such a chimera can arise. About 2 Myr ago an mRNA of the alcohol dehydrogenase gene *Adh* was reverse-transcribed and inserted into the third intron of a duplicate of the gene *yellow-emperor* (*Ymp*). The new gene consists of the first three exons of *Ymp* fused to an intronless copy of *Adh*, whose stop codon ended the reading frame; the downstream *Ymp* exons then degenerated. *jingwei* is expressed, and its sequence shows rapid evolution by positive selection.

![The birth of a chimeric gene by retrotransposition: *jingwei* in *Drosophila* (after Futuyma and Kirkpatrick 2017, Fig. 14.8). A: a duplicate of the *Ymp* gene (green exons) and an *Adh* mRNA, which is reverse-transcribed and inserted into intron 3 of the *Ymp* duplicate. B: in the new gene *jingwei*, the first three *Ymp* exons are spliced to the intronless *Adh* sequence (purple), whose stop codon (red bar) ends the reading frame; the *Ymp* exons downstream, no longer translated, degenerate.](./plots/jingwei.py)

Long introns make recombination between exons of different genes more likely, and in animals many proteins of the extracellular matrix, blood clotting and cell signaling are mosaics of domains (fibronectin repeats, EGF-like domains, kringles) whose exon boundaries coincide with the domain boundaries. But in many proteins the domains are not congruent with exons, and the shuffling of domains also occurs in prokaryotes, which have no spliceosomal introns; recombination and fusion of coding sequences are the more general mechanism. Families of proteins that share one catalytic domain combined with different targeting or regulatory domains, such as the RecA-like ATPases that act in recombination and DNA repair, are the result.

### 18.1.3. Genes from Noncoding DNA and from Other Species

The chance that a random sequence encodes a useful protein seems vanishingly small, yet comparative genomics of yeasts, flies and primates has found genes that arose from noncoding DNA, the **de novo genes** ([Definition 14.4.3](/7.4.14#def-14.4.3)). In *Drosophila* many of them are expressed in the testis, consistent with other evidence that **sexual selection** on males drives rapid molecular change. A random reading frame is more likely to be long in GC-rich DNA, because the three stop codons TAA, TAG and TGA are AT-rich.

Genes can also come from other species, by **horizontal gene transfer**. In prokaryotes this is the main route by which new genes are acquired, including those for antibiotic resistance ([7.10.27](/7.10.27)). In eukaryotes the largest transfers were from the endosymbionts that became mitochondria and plastids, whose genes moved to the nucleus ([7.10.28](/7.10.28)), but transfers from bacteria and fungi have also opened ecological opportunities: the plant-parasitic nematodes invade roots with cellulases, pectate lyases and other enzymes that degrade plant cell walls, genes they acquired from bacteria and fungi. A gene acquired by transfer can replace a native gene of the same function but unrelated sequence (*nonhomologous gene displacement*), which diversifies the enzymes that different lineages use in the same pathway.

## 18.2. The Fates of Duplicate Genes

### 18.2.1. Fixation and Loss

A new duplicate is a single mutant copy in a population. Like any new mutation, it is most likely to be lost by drift within a few generations; a neutral duplicate is fixed with probability $1/(2N)$ and a beneficial one with probability about $2s$ (Theorem 6.3.1). Even when fixed, a redundant copy is not protected by selection: a mutation that disables either copy costs nothing as long as the other works, so most fixed duplicates degenerate into pseudogenes or are deleted, and in humans their half-life is a few million years. The duplicates that persist are those that acquire a reason to be kept.

| Fate | What happens | Example |
|---|---|---|
| Nonfunctionalization | one copy is silenced by a null mutation and decays into a pseudogene, or is deleted | the commonest outcome |
| Dosage | both copies keep the same function because more product is favored | histone and rRNA genes; amplified esterase genes of insecticide-resistant insects |
| Dosage balance | copies of genes whose products act in complexes are kept together after whole-genome duplication | retained pairs in yeast ([Definition 16.2.3](/7.4.16#def-16.2.3)) |
| **Neofunctionalization** | one copy acquires a new function, the other keeps the old | crystallins; *RNASE1B*; sodium channels of electric fish |
| **Subfunctionalization** | the ancestral functions are divided between the copies | zebrafish *engrailed-1* duplicates; fetal hemoglobin |

![Fates of a duplicated gene with two regulatory modules (enhancers for tissues 1 and 2, blue and orange) and a coding region. After the duplication both copies are redundant. Nonfunctionalization: a null mutation (red cross) silences one copy, which becomes a pseudogene. Neofunctionalization: one copy keeps both ancestral functions, the other gains a new expression domain or protein function (green star). Subfunctionalization (DDC model, Definition 18.2.1): complementary losses of a module in each copy leave both copies necessary, each carrying one ancestral function.](./plots/duplicate-fates.py)

Neofunctionalization is the fate that creates novelty, but it requires a mutation that confers a new function to occur before a null mutation silences the copy. The electric organs of fishes evolved independently in the South American knifefishes and the African elephant-nosed fishes. All teleost fishes carry two copies of a muscle sodium channel gene, a legacy of the teleost whole-genome duplication; in most teleosts both are expressed in muscle, but in these two families expression of one copy, *Scn4aa*, has been lost from muscle and moved to the electric organ, where the channel evolved rapidly in sequence.

### 18.2.2. Subfunctionalization and the DDC Model

Most genes do several things: they are expressed in several tissues or stages under separate enhancers, or their protein has several activities. Force, Lynch and colleagues (1999) pointed out that such genes can be preserved after duplication without any new function, simply by degenerative mutations.

**Definition 18.2.1 (DDC Model)** In the **duplication–degeneration–complementation model** (DDC model), the two copies of a duplicated gene with several independently mutable subfunctions each lose, by degenerative mutations fixed by drift, different subfunctions, until every subfunction is carried by only one copy; both copies are then preserved by **purifying selection**, together performing the function of the ancestral gene.

The model makes a quantitative prediction. Consider a gene with $z$ regulatory subfunctions, each lost by mutation at rate $u_{\mathrm{r}}$ per copy, and a coding region destroyed by null mutations at rate $u_{\mathrm{c}}$ per copy. A degenerative mutation can be fixed (by drift, as a **neutral mutation**) only if every subfunction is still carried by the other copy; otherwise it is eliminated by selection. The pair ends either with one copy dead (nonfunctionalization) or with each copy carrying a subfunction that the other lacks (subfunctionalization).

**Formula 18.2.1 (Probability of Subfunctionalization)** Let $r = u_{\mathrm{r}}/u_{\mathrm{c}}$, and suppose that permissible degenerative mutations are fixed one at a time. For $z = 1$ subfunctionalization is impossible; for $z = 2$ its probability is

$$
P_{\mathrm{sub}} = \frac{2r}{1 + 2r}\cdot\frac{r}{1 + 2r} = \frac{2r^2}{(1 + 2r)^2}.
$$

**Proof** Initially both copies carry subfunctions 1 and 2, and every degenerative mutation is permissible: the total rate is $2u_{\mathrm{c}} + 4u_{\mathrm{r}}$. A null mutation, with probability $2u_{\mathrm{c}}/(2u_{\mathrm{c}} + 4u_{\mathrm{r}}) = 1/(1 + 2r)$, ends in nonfunctionalization; otherwise, with probability $2r/(1 + 2r)$, one copy (say A) loses a subfunction (say 1). Now copy B is the only carrier of subfunction 1 and cannot lose it, nor be silenced. The permissible events are a null mutation in A (rate $u_{\mathrm{c}}$) or loss of subfunction 2 by A (rate $u_{\mathrm{r}}$), both leaving A without function, and loss of subfunction 2 by B (rate $u_{\mathrm{r}}$), which leaves A with 2 and B with 1 only. The last has probability $u_{\mathrm{r}}/(u_{\mathrm{c}} + 2u_{\mathrm{r}}) = r/(1 + 2r)$. Multiplying the two stages gives the formula. $\square$

With equal rates ($r = 1$), $P_{\mathrm{sub}} = 2/9 \approx 0.22$. Because each additional subfunction adds both a target for complementary loss and a way of keeping both copies, the probability rises with $z$ and with $r$: genes with many independently mutable enhancers, and regulatory regions that are larger mutational targets than coding sequences, favor preservation by subfunctionalization. The model explains why many more duplicates are retained than the rarity of new functions would suggest, and why retained duplicates commonly divide the expression domains of the ancestral gene, as the two zebrafish *engrailed-1* genes do for the single mouse gene ([7.4.14](/7.4.14#sec-14.4.2)). Subfunctionalization also sets the stage for later specialization: once each copy serves only one function, each can be improved for it without compromising the other. The mammalian fetal β-like globins, expressed only before birth and with a higher oxygen affinity than adult hemoglobin, which lets the fetus take oxygen from its mother's blood in the placenta, are an example of such a division of labor ([Example 14.4.1](/7.4.14#sec-14.4.2)).

![Probability that a duplicated gene is preserved by subfunctionalization in the DDC model (Formula 18.2.1), against the ratio r of the rate of loss of one regulatory subfunction to the rate of null mutations in the coding region, for genes with z = 1 to 5 independent subfunctions. Points: Monte Carlo simulation of the sequence of permissible degenerative mutations (4000 duplicates per point); the curve for z = 2 is the exact formula. With one subfunction a duplicate is always lost; with several, and with regulatory regions that mutate often, preservation by complementary degeneration becomes likely.](./plots/ddc-probability.py)

### 18.2.3. Gene Families and Concerted Evolution

Repeated duplication builds **gene families** ([Definition 14.4.1](/7.4.14#def-14.4.1)): the globins, with duplications separated by hundreds of millions of years ([7.4.14](/7.4.14#sec-14.4.2)); the *Hox* clusters, multiplied by whole-genome duplications ([7.5.15](/7.5.15)); the olfactory receptors; and recently expanded families such as the *spiggin* genes of sticklebacks, which encode the glue with which males build their nests and descend from a single gene for a mucus protein. Comparisons of mammalian genomes show that families expand and contract continually, each lineage gaining and losing hundreds of genes, so that a family's size reflects a birth–death process of duplications and losses on which selection acts.

When copies lie in tandem, misalignment between paralogs leads to unequal crossing over and **gene conversion** between them, and a mutation in one copy can spread to the others.

**Definition 18.2.2 (Concerted Evolution)** **Concerted evolution** is the evolution of the members of a gene family as a unit: through gene conversion and unequal crossing over between copies, the copies within a species remain similar to one another while diverging, as a set, from the copies in other species.

The hundreds of tandem copies of the ribosomal RNA genes are the classic case: within a species they are nearly identical, between related species they differ consistently. Concerted evolution keeps many copies of a gene whose product is needed in large amounts homogeneous, but it also opposes divergence: a duplicate can acquire a new function only after it escapes conversion, for example by moving to another chromosome or diverging enough that the copies no longer pair.

## 18.3. The Death of a Gene

A duplicate is often dead on arrival: it may lack part of the gene or the regulatory elements needed to express it, and a retrocopy lacks its promoter. A gene that has lost its function, whether a new duplicate or an old gene, becomes a **pseudogene**, and the human genome contains almost as many pseudogenes as functional genes. Because a pseudogene is free of selection, its sequence evolves at the rate of neutral mutation, faster than the functional gene from which it came, a "natural controlled experiment" that shows that most mutations in functional genes are eliminated by purifying selection ([7.10.6](/7.10.6#sec-6.6)).

Deletions remove genes as well, sometimes to advantage. The chemokine receptor CCR5 on white blood cells is used by HIV to enter the cell; the allele *CCR5-Δ32*, a 32-bp deletion that shifts the reading frame so that the truncated receptor does not reach the cell surface, makes homozygotes highly resistant to infection. The allele is common in northern Europe, long predates the HIV epidemic, and has been proposed to have risen by selection for resistance to earlier diseases, though the evidence for past selection on it is debated. Deletion of the parental copy after a duplication moves a gene to a new place in the genome (gene trafficking); in *Drosophila*, retrotransposed copies have moved disproportionately from the X chromosome to the autosomes. Losses of genes contribute as much as gains to the differences between the gene contents of related species.

## 18.4. The Evolution of Protein-Coding Sequences

### 18.4.1. Drift and Functional Constraint

Within protein-coding genes, the first and second positions of codons, where most changes alter the amino acid, evolve slowly; third positions and introns evolve much faster. If most changes were adaptive, the opposite would be expected. The pattern makes sense if most substitutions are neutral or nearly neutral and fixed by drift, while most amino acid changes are harmful: between 70 % and 97 % of nonsynonymous mutations, depending on the organism, are strongly deleterious and removed by purifying selection. This is the core of Kimura's **neutral theory of molecular evolution** ([7.10.6](/7.10.6#sec-6.6)).

Proteins differ in how much of their sequence is constrained by function (**selective constraint**, Definition 8.1.3). Histone H4, which packages DNA in all eukaryotes, differs by only two of about 100 amino acids between pea and human; the fibrinopeptides, which are cut from fibrinogen during blood clotting and whose sequence matters little, evolve hundreds to a thousand times faster; most proteins, such as the globins and cytochrome *c*, lie in between, and pseudogenes evolve at the mutation rate. A constant rate for each protein, set by its constraint, is the basis of the **molecular clock** ([7.10.24](/7.10.24)).

### 18.4.2. Positive Selection and Population Size

Positive selection reverses the usual pattern: when a protein adapts to a new role, nonsynonymous substitutions can outnumber synonymous ones, as in *RNASE1B*. How much of protein evolution is adaptive is estimated by extensions of the **McDonald–Kreitman test** (Definition 8.2.4), and the answer depends on the organism: about half of the amino acid differences between species of *Drosophila*, of mice (*Mus*) and of enteric bacteria (*E. coli* and *Salmonella enterica*) were fixed by positive selection, but less than 15 % in recent human evolution.

The difference reflects **effective population size**. *Drosophila melanogaster* has an effective size in the millions, humans about $10^4$ over much of their history. A mutation that lowers fitness by $s = 10^{-5}$ is efficiently removed in the fly ($4N_{\mathrm{e}}s \gg 1$) but behaves almost as a neutral mutation in humans ($4N_{\mathrm{e}}s \approx 0.4$), so in small populations many slightly deleterious substitutions are fixed and inflate the nonadaptive share of divergence (the **nearly neutral theory**, Definition 6.5.1); in large populations, moreover, more beneficial mutations arise each generation. Selection on synonymous sites, which produces **codon usage bias** in highly expressed genes, is likewise effective only in species with large populations such as free-living microbes and *Drosophila*, and is weak or absent in vertebrates ([7.10.8](/7.10.8#sec-8.1.2)).

![Population size sets the fate of weakly selected mutations. Rate of substitution relative to the neutral rate, k/μ = 4Nₑs/(1 − e^(−4Nₑs)) (from the fixation probability of Theorem 6.3.1, with N = Nₑ), for mutations with selection coefficients s = −10⁻⁴, −10⁻⁵, −10⁻⁶ (harmful) and +10⁻⁵ (beneficial), against the effective population size. Shaded bands mark the typical effective sizes of large vertebrates (about 10⁴–10⁵), of many invertebrates and plants (about 10⁵–10⁷) and of free-living bacteria (10⁸ and above). A slightly deleterious insertion or amino acid change with s = −10⁻⁵ is fixed almost as often as a neutral one when Nₑ is 10⁴, and practically never when Nₑ is 10⁶.](./plots/ne-and-fate.py)

## 18.5. The Evolution of Gene Expression

A gene can also adapt through changes in how often, when and where it is transcribed, how its transcript is spliced and processed, and how its protein is deployed. Mutations in the binding sites of transcription factors near the gene act in *cis*, only on the copy of the gene on the same chromosome; mutations in the genes for the factors themselves act in *trans*, on every target of the factor. The distinction, and why adaptive changes of morphology are often *cis*-regulatory, is the subject of [7.10.19](/7.10.19).

Adaptation often combines changes of structure and expression. In East Africa the mosquito *Aedes aegypti*, the vector of the dengue, yellow fever, Zika and chikungunya viruses, occurs as a domestic form that bites humans and a forest form that feeds on other animals. An odorant receptor, Or4, expressed on the antennae, has evolved in two ways in the domestic form: its alleles detect sulcatone, a compound characteristic of human body odor, and it is expressed at about twice the level. Genome scans of three-spined sticklebacks (*Gasterosteus aculeatus*), which have repeatedly colonized fresh water from the sea, find many regions consistently diverged between freshwater and marine populations; only about 17 % of them involve changes to coding sequences, while the rest lie in regions that are probably or certainly regulatory, and genes near them are enriched among those expressed differently in the two habitats.

Other levels of expression evolve too. About a third of alternative splicing events differ between human and mouse orthologs, so that **alternative splicing** diverges faster than the coding sequences themselves. In bacteria and archaea, genes transcribed together in **operons** are gained and lost as units of regulation, and operons are also found in viruses and a few eukaryotes. Short noncoding regions that are nearly identical between distantly related species, the ultraconserved elements, are among the most strongly constrained sequences in vertebrate genomes; many of them are thought to be regulatory elements.

## 18.6. Gene Structure and the Origin of Introns

Most genes of eukaryotes, but few genes of prokaryotes, are interrupted by spliceosomal introns, which make up about a quarter of the human genome. Where did they come from?

**Definition 18.6.1 (Introns-Early Hypothesis)** The **introns-early hypothesis** (the exon theory of genes, Gilbert 1978) holds that introns were present in the earliest genes, that the first genes were assembled from short exons encoding protein modules, and that the introns were later lost from the compact genomes of prokaryotes. The alternative, the *introns-late* view, holds that spliceosomal introns arose in the lineage leading to eukaryotes and spread within eukaryotic genomes.

The evidence favors introns-late. Spliceosomal introns are absent from all bacteria and archaea; intron positions in ancient genes shared by all domains rarely coincide with boundaries of structural modules, as the exon theory predicted; and introns are gained and lost relatively often, the loss commonly by recombination with a reverse-transcribed, spliced mRNA. The chemistry and structure of the spliceosome point to its origin from self-splicing group II introns, which are found in bacteria and in organelles derived from them ([7.2.16](/7.2.16#sec-16.8.2)): mobile group II introns from the bacterial ancestor of mitochondria probably invaded the nuclear genome of early eukaryotes, broke into the catalytic snRNAs and many intron copies, and multiplied. Comparisons of intron positions across eukaryotes indicate that the last eukaryotic common ancestor already had many introns, and that some lineages, such as budding yeast, have lost most of them since ([7.10.28](/7.10.28)).

Why were introns tolerated? One answer is nonadaptive: each intron is a small mutational liability, because mutations in its splice signals disable the gene, and such slightly deleterious features accumulate by drift in lineages with small effective populations (Lynch). Once present, introns made alternative splicing and exon shuffling possible, so a feature that may have arisen as genomic parasitism became a source of regulatory and protein diversity. The *Dscam* gene of *Drosophila*, whose 95 alternatively spliced exons could produce more than 38 000 protein isoforms, shows the extreme. Genes also overlap, so that one stretch of DNA encodes two proteins in different reading frames; this is common in viruses and bacteria and rare in eukaryotes.

## 18.7. Chromosome Evolution

### 18.7.1. Fissions, Fusions and Meiotic Drive

The number and structure of the chromosomes, the **karyotype**, differ among species. The commonest change of number is a fusion of two chromosomes, as at a **Robertsonian translocation**, or a fission. Humans have 23 pairs and the other great apes 24 because two ancestral chromosomes fused in our lineage to form human chromosome 2 ([7.4.15](/7.4.15#sec-15.6)); whether the fusion spread by selection or by drift is unknown.

The house mouse (*Mus musculus*) shows how chromosome number can evolve fast without benefiting the organism. Its populations have from 11 to 20 chromosome pairs, changes of number having occurred hundreds of times faster than in most mammals. In female meiosis one haploid set enters the egg and the other the polar body, which dies. In a female heterozygous for a fusion, the fused chromosome and its two unfused homologues compete for the egg, and which wins depends on which attaches more strongly to the spindle on the egg side, a property of the meiotic machinery that itself varies between populations. This **meiotic drive** favors fusions in some populations and fissions in others, and almost every possible pair of autosomes has fused in some population. Across 1170 species of mammals, karyotypes tend to have either most chromosomes fused or most unfused, rather than the intermediate mixtures expected if fusions occurred independently: the shifts appear to play out across mammals as well. The number of chromosomes, among the most basic features of a genome, can thus be the outcome of conflict between genetic elements at different **levels of selection** rather than an adaptation of the organism.

### 18.7.2. Inversions

An **inversion** carries the same genes as the uninverted chromosome in a different order ([7.4.15](/7.4.15#sec-15.4)); the third chromosome of *Drosophila pseudoobscura*, studied by Dobzhansky, is famously polymorphic for them, and the chromosomes of *Drosophila* species differ by many fixed inversions. Several mechanisms can make an inversion spread:

- its breakpoints can disrupt or alter the expression of a gene, occasionally beneficially;
- it can benefit from meiotic drive;
- because recombination is suppressed in heterozygotes, it can hold together a favorable combination of alleles at several loci, or capture alleles locally adapted to one environment (cf. [7.10.10](/7.10.10));
- it can drift to fixation even if it is underdominant (**underdominance**), when it crosses a frequency of $1/2$ by chance in a small population, and the resulting reduced fertility of hybrids can contribute to speciation ([7.10.12](/7.10.12)).

The ruff (*Calidris pugnax*), a sandpiper, has three kinds of males with different mating strategies: territorial "independents", nonterritorial "satellites" and female-mimicking "faeders". Satellites and faeders are heterozygous for a 4.5-Mb inversion, absent from independents, that contains genes affecting plumage and sex hormones; the satellite and faeder versions of the inversion carry different alleles. Suppressed recombination keeps each strategy's combination of alleles together, a **supergene**.

## 18.8. The Evolution of Genome Size and Content

### 18.8.1. Genomes Large and Small

**Definition 18.8.1 (Genome Size)** The **genome size** of an organism is the total amount of DNA in one copy of its genome (its haploid nuclear genome in eukaryotes, the **C value** of [Definition 2.1.1](/7.2.2#def-2.1.1)), measured in base pairs or picograms.

The smallest known genome, that of porcine circovirus type 1, has 1759 bp and three genes; one of the smallest bacterial genomes, that of the leafhopper symbiont *Nasuia deltocephalinicola*, about 112 kb and 137 protein-coding genes. Among eukaryotes genome size spans more than five orders of magnitude, and even within *D. melanogaster* it varies by up to 30 %. Plotting the amount of protein-coding sequence against genome size reveals the pattern behind the C-value paradox: in viruses and prokaryotes almost the whole genome codes for proteins, so the two grow together; in plants and animals most of the genome is noncoding, and its amount varies enormously among species with similar numbers of genes ([7.2.2](/7.2.2#sec-2.1)). Less than 2 % of the human genome codes for proteins; about half consists of transposable elements and their remains.

![The composition of the human genome (data from Futuyma and Kirkpatrick 2017, Fig. 14.14). Protein-coding exons are 2 % of the genome and introns 26 %. Transposable elements together make up almost half (blue): LINEs 20 %, SINEs (mainly Alu) 13 %, LTR retrotransposons 8 % and DNA transposons 3 %. The rest consists of segmental duplications (5 %), simple sequence repeats (3 %), heterochromatin (8 %) and other unique sequence (12 %).](./plots/human-genome-composition.py)

### 18.8.2. Transposable Elements as Genetic Parasites

**Transposons** reproduce within the genome: a sequence that copies itself more prolifically than others comes to make up more of the genome, whether or not it benefits the host (**selfish genetic elements**, [7.4.17](/7.4.17#sec-17.6)). The commonest element in the human genome, Alu, a SINE of about 300 bp, has more than a million copies that make up more than 10 % of the genome. Alu is a parasite of parasites: it encodes no reverse transcriptase and uses the enzyme made by **LINEs**. Retrotransposons that copy through RNA resemble retroviruses, and one hypothesis is that transposable elements are modified viruses that evolved to reproduce without leaving the cell.

Transposable elements spread through genomes as evolutionary epidemics: among *Drosophila* species they make up from 3 % to 25 % of the genome. Because copies diverge after insertion, the divergence among copies of a family dates its activity, like a molecular clock: in humans, Alu insertion peaked about 45 Myr ago, and the overall rate of transposition is now far lower than in the past, because host genomes have evolved ways to silence most elements ([7.2.15](/7.2.15)). The phylogenetic distribution dates the origin of Alu: it is found only in primates, and so arose about 65 Myr ago, near the base of the primate radiation. The equilibrium between the spread of copies and selection against them is modeled in [Formula 17.6.1](/7.4.17#fml-17.6.1).

Insertions disrupt genes, and recombination between copies at different sites causes rearrangements; elements therefore accumulate in regions of low recombination, where these harms are smaller and selection against them is less efficient: in *Arabidopsis thaliana* the density of transposable elements is about 20 times higher near the centromeres than near the telomeres. Occasionally an insertion is beneficial: the melanic form of the peppered moth (*Biston betularia*), the classic example of evolution observed in action, is caused by a transposon inserted in the gene *cortex*.

### 18.8.3. Routes to the Smallest and Largest Genomes

Small genomes arise in different ways in different organisms.

- Viruses are in a race to replicate, rely on their hosts for most functions and carry little or no noncoding DNA.
- *Buchnera aphidicola*, a symbiont that has lived inside aphids for more than 160 Myr, transmitted from mother to offspring, has about 600 kb and about 500 genes. Its host supplies many metabolites, so many genes are dispensable; its populations are small and pass through a bottleneck in every generation, so drift is strong; and deletions are more frequent than duplications in bacteria. Slightly harmful deletions are fixed by drift, and the genome shrinks by a ratchet towards the minimum needed to survive.
- *Pelagibacter ubique*, perhaps the most abundant organism on Earth (about $10^{28}$ cells), has a genome of about 1.3 Mb with no pseudogenes, no transposons and almost no intergenic DNA. With so large a population, drift is weak, and its streamlining appears to be an adaptation to nutrient-poor seawater, reducing the nitrogen and phosphorus needed for DNA and allowing a smaller cell.

Large genomes also arise in several ways. Gene number grows by whole-genome duplication: bread wheat, an allohexaploid formed by two rounds of hybridization and polyploidy (the second in cultivated fields, about 10 000 years ago), has about 100 000 genes, about four times as many as its diploid ancestors; if it follows other polyploid plants, many duplicates will eventually be lost and the genome will shrink again, as it has repeatedly in the crucifers (Brassicaceae). Noncoding DNA grows by the proliferation of transposable elements. And drift sets how much excess DNA selection can remove. Each extra stretch of DNA is a small mutational liability, a target for mutations that disrupt the genes it is attached to, but its cost is tiny; in animals and plants, with effective sizes of $10^4$ to $10^6$, such costs are smaller than $1/N_{\mathrm{e}}$ and invisible to selection, while in bacteria, with $N_{\mathrm{e}} \gtrsim 10^8$, they are not (the mutational hazard view of Lynch and Conery 2003, a form of the **drift-barrier hypothesis**, Definition 6.5.2, and [7.2.2](/7.2.2#sec-2.8)).

Is the noncoding 98 % of the human genome therefore junk? Comparative genomics finds that only a modest fraction of it, of the order of a tenth of the genome, shows evidence of purifying selection; much of the rest consists of decayed transposons and duplicates whose sequence does not matter. But some sequences derived from transposons have become regulatory elements, and the bulk of the DNA affects nuclear and cell size, so that the eukaryotic genome may be unable to shed it easily. Whatever its origin, abundant noncoding DNA opened new possibilities for the evolution of gene regulation, on which the evolution of complex multicellular organisms has drawn.

## Summary

| Process | Main mechanism | What decides its fate | Examples |
|---|---|---|---|
| New genes | **gene duplication** (Definition 18.1.1), WGD, **exon shuffling** (Definition 18.1.2), de novo origin, horizontal transfer | drift and selection on a single new copy | crystallins, *AMY1*, *RNASE1B*, *jingwei* |
| Fates of duplicates | loss, dosage, neofunctionalization, subfunctionalization | which mutation comes first; number of subfunctions (**DDC model**, Definition 18.2.1, Formula 18.2.1) | electric-fish *Scn4aa*, fetal globin |
| Gene families | repeated duplication; **concerted evolution** (Definition 18.2.2) by gene conversion | birth–death of copies; homogenization | globins, *Hox*, rRNA genes |
| Death of genes | pseudogenes, deletions | relaxed selection; occasionally positive selection for loss | *CCR5-Δ32* |
| Coding sequences | mostly drift under constraint; sometimes positive selection | constraint (histone vs fibrinopeptides); $N_{\mathrm{e}}$ ($\approx 50\,\%$ adaptive in flies, $< 15\,\%$ in humans) | $d_{\mathrm{N}}/d_{\mathrm{S}}$ |
| Expression | *cis*- and *trans*-regulatory change, splicing | as for coding changes | *Aedes* Or4, sticklebacks |
| Introns | spliceosomal introns from group II introns in early eukaryotes (**introns-early hypothesis**, Definition 18.6.1, rejected) | drift in small populations, later co-option | *Dscam* |
| Chromosomes | fusion, fission, inversion | meiotic drive, suppressed recombination, drift of underdominant variants | human chromosome 2, house mouse, ruff |
| **Genome size** (Definition 18.8.1) | transposable elements, WGD, deletion | strength of drift relative to tiny costs; deletion bias | *Buchnera*, *Pelagibacter*, wheat |

- Genomes are shaped as much by nonadaptive processes (mutation bias, drift, meiotic drive, selfish elements) as by natural selection; the balance between them depends on the effective population size.
- New functions arise mostly by tinkering with old genes: duplication, recombination of parts and the co-option of existing products.

## Questions

1. Why are duplicates produced by retrotransposition usually dead on arrival, while duplicates produced by unequal crossing over are more often functional?

   **Answer** A retrocopy is made from a processed mRNA: it lacks introns and, above all, the promoter and enhancers of the parental gene, so it is expressed only if it happens to land near a suitable promoter; it also carries a poly(A) tract and is often truncated by incomplete reverse transcription. A tandem duplicate made by unequal crossing over copies the gene together with its flanking regulatory region, so it is expressed like the parent from the start.

2. In the DDC model with $z = 2$ subfunctions, compute the probability of subfunctionalization when regulatory losses are three times as frequent as null mutations of the coding region, and explain why it is smaller than $1$ even when $r \to \infty$.

   **Answer** With $r = 3$, $P_{\mathrm{sub}} = 2\cdot 9/49 = 18/49 \approx 0.37$. As $r \to \infty$ null mutations are negligible, but after copy A has lost subfunction 1, copy A can still lose subfunction 2 (which also silences it) at the same rate as copy B loses subfunction 2; these are equally likely, so $P_{\mathrm{sub}} \to 1/2$.

3. A pair of paralogs in a fish shows $d_{\mathrm{N}}/d_{\mathrm{S}} = 0.1$ for one copy and $1.8$ for the other since the duplication. What data are needed to infer that the second copy evolved under positive selection, and what alternative explanation must be excluded?

   **Answer** The substitutions must be assigned to each copy since the duplication, which requires an outgroup gene from a species that diverged before the duplication (to polarize the changes) and enough synonymous changes on each branch for a reliable ratio; a likelihood test of a branch model ([7.10.23](/7.10.23)) compares $\omega > 1$ on that branch with $\omega = 1$. The alternative is relaxed constraint: a copy that is becoming a pseudogene evolves with $\omega \to 1$, not above it, so $\omega$ significantly greater than 1, and an intact reading frame and expression, distinguish adaptation from decay.

4. Alu elements are present at many sites in humans but not chimpanzees, and at others in chimpanzees but not humans. Give two hypotheses and a way to distinguish them at a given site.

   **Answer** (a) The insertion occurred in one lineage after the split; (b) the insertion is older, was polymorphic in the common ancestor and was lost or never fixed in the other lineage (incomplete lineage sorting), or was precisely deleted. A new insertion is flanked by target-site duplications and has a sequence close to the young Alu subfamilies active in that lineage, while the empty site in the other species shows no trace; an old polymorphic insertion belongs to an older subfamily and may be present in gorillas or other outgroups.

5. Why are genome sizes of free-living bacteria small and narrowly distributed, while those of animals and plants vary over orders of magnitude?

   **Answer** Bacteria have very large effective populations, so even the tiny fitness costs of extra DNA (replication cost, mutational hazard) exceed $1/N_{\mathrm{e}}$ and are removed by selection, helped by a mutational bias towards deletions; noncoding DNA is purged and gene number tracks genome size. In animals and plants, $N_{\mathrm{e}}$ is small, so insertions of transposable elements and other slightly deleterious DNA drift to fixation, and lineages differ in transposon activity, deletion rates and polyploidy; genome size then varies widely and independently of gene number.
