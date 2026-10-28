---
title: Bacterial and Phage Genetics
description: Bacteria and phages as genetic organisms; prototrophs, auxotrophs, selection and screening; horizontal gene transfer by transformation, conjugation and transduction used as tools for mapping; cotransformation; F, Hfr and F′, interrupted mating, time-of-entry maps, the circular chromosome and fine mapping by recombination; generalized transduction, cotransduction and Wu's formula, three-factor transductions, specialized and lateral transduction; phage crosses.
---

Bacteria are haploid, divide every 20 to 30 minutes and can be grown by the billion on a single plate, so a mutation that occurs once in $10^8$ cells can be found in an afternoon. They have no meiosis, but they exchange genes in three ways: by taking up free DNA (transformation), by transfer of DNA through cell contact (conjugation) and by phages that carry bacterial DNA from one cell to another (transduction). In each, a fragment of a donor's genome enters a recipient and is incorporated into its chromosome by **homologous recombination**, and the frequency with which two donor markers are inherited together measures the distance between them. This chapter treats these processes as tools of genetic analysis: how they were discovered, how they map genes, and how they distinguish dominant from recessive and cis from trans in partial diploids. The physiology of gene transfer, its role in bacterial evolution and ecology, and the biology of phages belong to microbiology ([7.11](/7.11)); the bacterial genome itself is described in [7.2.2](/7.2.2#sec-2.7.2), the molecular machinery of recombination in [7.2.9](/7.2.9), and the operons and phage λ, whose genetic dissection relied on the methods described here, in [7.2.11](/7.2.11). Phage crosses also prepare the fine-structure mapping of the *rII* gene in [7.4.13](/7.4.13).

## 10.1. Bacteria as Experimental Organisms

### 10.1.1. Genomes and Genotypes

The genome of *Escherichia coli* K-12 is a single circular chromosome of $4.64\,\mathrm{Mb}$ with about 4300 genes, densely packed (about $88\,\%$ coding), without introns and with little repeated DNA; many strains also carry **plasmids**, small circular DNA molecules that replicate independently and often carry genes for antibiotic resistance, toxins or the ability to transfer DNA. Genomes vary between strains: a core of about 1000 to 2000 genes is shared by all *E. coli*, and the pangenome of the species contains tens of thousands of genes found only in some strains ([7.2.2](/7.2.2)). Because bacteria are **haploid**, every mutation is expressed: there is no dominance to hide a recessive allele, except in the partial diploids of 10.4.6.

Bacterial genetic notation distinguishes genotype and phenotype. Genes have three-letter italic names with a capital letter for each gene of a cluster: *lacZ*, *lacY*, *trpA*. Alleles are written with superscripts, $lac^{+}$, $lacZ^{-}$, $str^{r}$ (streptomycin resistant) and $str^{s}$ (sensitive). Phenotypes are written in roman with a capital: Lac⁺ (can use lactose), Str$^{\mathrm{r}}$, Thr⁻ (requires threonine).

### 10.1.2. Prototrophs, Auxotrophs, Selection and Screens

**Definition 10.1.1 (Prototroph and Auxotroph)** A **prototroph** is a strain that can grow on minimal medium, which contains only inorganic salts, a carbon source and water; wild-type *E. coli* is prototrophic. An **auxotroph** is a mutant strain that grows only if the medium is supplemented with one or more specific nutrients (an amino acid, a nucleotide, a vitamin) that it can no longer synthesize; for example a $his^{-}$ auxotroph requires histidine.

Mutant classes used in bacterial genetics are auxotrophs, mutants unable to use a carbon source (Lac⁻, Gal⁻), mutants resistant to antibiotics or phages (Str$^{\mathrm{r}}$, Ton$^{\mathrm{r}}$, resistant to phage T1) and conditional mutants (temperature-sensitive alleles of essential genes). Two strategies find them.

**Definition 10.1.2 (Genetic Selection and Screen)** A **genetic selection** is an experimental condition under which only cells of the desired genotype can grow (or only cells of other genotypes die), so that rare mutants or recombinants are recovered from enormous populations: for example plating $10^{9}$ cells on streptomycin to recover Str$^{\mathrm{r}}$ mutants, or plating on minimal medium to recover prototrophic recombinants. A screen, in contrast, examines every colony for a phenotype, as when colonies on an indicator medium are inspected for colour, or replica-plated to find those that fail to grow on minimal medium.

Selections can examine $10^{8}$ to $10^{10}$ cells per plate, screens a few thousand; this difference of five orders of magnitude is what makes the experiments of this chapter possible, since the recombinants we count are often rare. Screens are usually needed to find auxotrophs (one cannot select for the inability to grow), and because spontaneous mutation rates are low ($10^{-6}$ to $10^{-8}$ per gene per generation, [7.4.12](/7.4.12)), mutagens or enrichment are used first. Penicillin enrichment is a selection against growth: penicillin kills only growing cells, so in minimal medium it kills prototrophs and spares auxotrophs. Genetic screens in eukaryotes are treated in [7.4.19](/7.4.19).

Counting relies on dilution: a culture with $N$ cells per millilitre plated after dilution $10^{-k}$ gives $N\,10^{-k}v$ colonies from a volume $v$, Poisson-distributed, so a plate with $c$ colonies estimates the titre with relative standard error $1/\sqrt c$.

## 10.2. Gene Transfer in Bacteria

### 10.2.1. Three Mechanisms

**Definition 10.2.1 (Horizontal Gene Transfer)** **Horizontal gene transfer** (lateral gene transfer) is the transmission of genetic material between organisms other than from parent to offspring, as opposed to vertical transmission by cell division or sexual reproduction. In bacteria it occurs by transformation, conjugation and transduction.

In all three, DNA moves one way, from a donor to a recipient. The three differ in how the DNA travels (Table), and therefore in how much of it can travel together, which sets the scale on which each maps genes.

| | Transformation | Conjugation | Transduction |
|---|---|---|---|
| Vehicle | free DNA taken up from the medium | a conjugative plasmid; cell contact | a phage particle |
| Sensitive to DNase? | yes | no | no |
| Requires contact between cells? | no | yes | no |
| Length transferred | usually $< 20$–$50\,\mathrm{kb}$ | up to the whole chromosome ($100\,\mathrm{min}$) | one phage head, about $1$–$2\,\%$ of the chromosome |
| Mapping by | cotransformation frequency | time of entry; recombination frequency | cotransduction frequency |

### 10.2.2. Merozygotes and Recombination

A transferred chromosomal fragment, the exogenote, is linear and cannot replicate on its own; it survives only if it replaces the homologous segment of the recipient's chromosome, the endogenote. Replacing an internal segment of a circular chromosome requires an even number of crossovers (two, or four), one on each side of the incorporated region (Figure in 10.4.5); a single crossover would open the circle into a non-viable linear molecule. The cell temporarily diploid for the transferred region is a merozygote (partial zygote). The requirement of two flanking crossovers is the key to all bacterial fine mapping: two markers on one fragment are inherited together unless one of the crossovers falls between them.

## 10.3. Transformation

### 10.3.1. Natural and Artificial Transformation

**Transformation** was discovered by Griffith (1928) in pneumococci and identified by Avery, MacLeod and McCarty (1944) as the uptake of DNA, the experiment that showed genes are made of DNA. Some species are naturally competent, able to take up DNA from their surroundings in a regulated physiological state: *Streptococcus pneumoniae* and *Bacillus subtilis* (Gram-positive) take up any DNA, while *Haemophilus influenzae* and *Neisseria* (Gram-negative) prefer DNA carrying short species-specific uptake sequences. A double-stranded fragment binds to the cell surface, one strand is degraded and the other enters as single-stranded DNA, which is coated by RecA and recombines with the homologous region of the chromosome, forming a heteroduplex; after replication one daughter carries the donor allele. *E. coli* is not naturally competent, but it can be transformed artificially, by treatment with $\ce{Ca^2+}$ in the cold followed by a heat shock or by electroporation, the basis of cloning ([7.2.5](/7.2.5)).

### 10.3.2. Cotransformation and Mapping

**Definition 10.3.1 (Cotransformation)** **Cotransformation** is the simultaneous transformation of a recipient by two or more donor markers carried on the same DNA fragment. Its frequency, the fraction of transformants for one marker that also received the other, decreases with the distance between the markers and is zero when they are farther apart than the length of the fragments taken up.

Two markers can also be acquired together on two separate fragments, and the two cases are distinguished by the dependence on DNA concentration. At low concentration each fragment is taken up with probability proportional to the concentration $c$, so

**Formula 10.3.1 (Double Transformation by Linked and Unlinked Markers)** At DNA concentrations below saturation, the frequency of transformants for one marker is proportional to $c$; the frequency of double transformants is proportional to $c$ if the markers are linked (one fragment), and to $c^2$ if they are unlinked (two independent fragments), when it is approximately the product of the two single frequencies.

**Example 10.3.1** DNA from a $trp^{+}\,his^{+}$ strain of *B. subtilis* transforms a $trp^{-}\,his^{-}$ recipient. Among $10^{8}$ recipients there are $5600$ $trp^{+}$ transformants (4000 $trp^{+}\,his^{-}$ and 1600 $trp^{+}\,his^{+}$) and $4600$ $his^{+}$ transformants (3000 $his^{+}\,trp^{-}$ and 1600 double). Independent uptake would give about $5600 \times 4600/10^{8} \approx 0.26$ doubles; 1600 are observed, so the markers are cotransformed on one fragment. The cotransformation frequency of $his$ with selected $trp$ is $1600/5600 = 0.29$. Diluting the DNA tenfold would lower singles and doubles tenfold each, confirming linkage.

Transformation maps genes within a few tens of kilobases, the size of the fragments. It is also how many bacteria acquire new genes in nature: in *Neisseria gonorrhoeae*, penicillin resistance arose by transformation with fragments of *penA* (encoding a penicillin-binding protein) from commensal *Neisseria* species, producing mosaic genes whose products bind penicillin poorly. The ecology of such transfer is treated in [7.11](/7.11).

## 10.4. Conjugation

### 10.4.1. Discovery

In 1946 Joshua Lederberg and Edward Tatum mixed two auxotrophic strains of *E. coli* K-12, one requiring methionine and biotin ($met^{-}\,bio^{-}$) and the other threonine, leucine and thiamine ($thr^{-}\,leu^{-}\,thi^{-}$), and plated them on minimal medium. Neither strain grows alone (reversion of two or three mutations at once is vanishingly rare), but the mixture gave prototrophic colonies at a frequency of about $10^{-7}$. Bernard Davis (1950) excluded cross-feeding or transformation by separating the two strains with a filter in a U-shaped tube through which medium was pumped back and forth: no prototrophs formed. Cell contact was required.

**Definition 10.4.1 (Conjugation)** **Conjugation** is the one-way transfer of DNA from a donor bacterium to a recipient through direct contact, initiated by a conjugative plasmid (or integrated conjugative element) in the donor.

### 10.4.2. The F Plasmid

**Definition 10.4.2 (F Plasmid)** The **F plasmid** (fertility factor, F factor) of *E. coli* is a conjugative plasmid of about $100\,\mathrm{kb}$ that carries the *tra* genes for a sex pilus and for DNA transfer and an origin of transfer, *oriT*. Cells carrying it are donors, F⁺; cells without it are recipients, F⁻.

The F pilus contacts an F⁻ cell and retracts to bring the cells together. A relaxase (TraI) nicks one strand at *oriT* and remains attached to its $5'$ end, which is led through the type IV secretion channel into the recipient, while replication in the donor (rolling circle) replaces the transferred strand. The recipient synthesizes the complementary strand and circularizes the plasmid. In an F⁺ × F⁻ cross, therefore, the recipient becomes F⁺ and the donor remains F⁺; F spreads through a population, and F⁺ cells rarely transfer chromosomal genes (frequency about $10^{-7}$).

![Conjugation. (A) F+ × F−: the donor (blue chromosome, small yellow F plasmid) contacts the recipient (pink chromosome) through the F pilus and transfers one strand of F, starting at oriT; both strands are completed by synthesis, so both cells end up F+, and chromosomal genes are rarely transferred. (B) Hfr × F−: F (yellow segment) is integrated in the donor chromosome; transfer starts inside F and continues into the chromosome, so donor genes enter in a fixed order from the origin; the pair usually breaks long before the rest of F would enter, the linear donor fragment is incorporated by two crossovers, and the recipient remains F−.](./plots/conjugation.py)

### 10.4.3. Hfr Strains and Interrupted Mating

In a small fraction of F⁺ cells, about $10^{-5}$, F integrates into the chromosome by homologous recombination between an insertion sequence (a short transposable element, [7.4.17](/7.4.17)) on F and a copy of the same element on the chromosome.

**Definition 10.4.3 (Hfr Strain and Episome)** An **Hfr strain** (high frequency of recombination) is a donor in which the F plasmid is integrated into the chromosome. Its transfer begins at *oriT* within the integrated F and continues into the adjacent chromosomal DNA, so that it transfers chromosomal markers at high frequency, always in the same order, starting from a fixed origin. A plasmid that can exist either autonomously or integrated into the chromosome, like F, is an **episome**.

Transfer from an Hfr is linear and starts with part of F; the rest of F would enter last, after the whole chromosome. Since the mating pair usually breaks before then (transfer of the entire chromosome takes about $100\,\mathrm{min}$ at $37\,^\circ\mathrm{C}$), recipients of an Hfr cross almost always remain F⁻.

**Definition 10.4.4 (Interrupted Mating)** In an **interrupted mating** experiment (Wollman and Jacob, 1955–1957), an Hfr strain and an F⁻ strain differing at several markers are mixed, samples are taken at intervals and agitated violently (in a kitchen blender) to separate the mating pairs, and the recipients are plated on a medium that selects recombinants for one marker and kills the donors; the unselected donor markers in these recombinants are then scored.

In the classic experiment, HfrH ($thr^{+}\,leu^{+}\,azi^{r}\,ton^{r}\,lac^{+}\,gal^{+}\,str^{s}$) was mated with an F⁻ strain $thr^{-}\,leu^{-}\,azi^{s}\,ton^{s}\,lac^{-}\,gal^{-}\,str^{r}$; recombinants were selected on medium without threonine and leucine containing streptomycin (which selects $thr^{+}\,leu^{+}$, the first markers transferred, and kills the Str$^{\mathrm{s}}$ donor). The donor's $azi^{r}$ allele first appeared among the recombinants at about $9\,\mathrm{min}$, $ton^{r}$ at about $11\,\mathrm{min}$, $lac^{+}$ at about $18\,\mathrm{min}$ and $gal^{+}$ at about $25\,\mathrm{min}$. Each marker's frequency then rose and reached a plateau, lower for markers that enter later. The entry times give the gene order and the distances in minutes.

![Interrupted mating. (A) A model of the HfrH × F⁻ cross: frequency of recombinants carrying each unselected donor marker (among *thr*⁺ *leu*⁺ *str*ʳ recombinants) against the time at which mating was interrupted. Each marker appears at its entry time, rises over a few minutes because pairs begin mating at different times, and reaches a plateau that is lower for later markers because mating pairs break at a constant rate. (B) Entry time against the order of the markers along the chromosome: the slope is the transfer speed, about 1 minute per minute of map (about 46 kb per minute). Model curves with illustrative parameters (pair breakage rate 0.06 per minute).](./plots/interrupted-mating.py)

**Formula 10.4.1 (Time of Entry and Transfer Gradient)** If transfer proceeds at a constant speed from the origin, and each mating pair breaks at a constant rate $\lambda$ per minute, a donor marker at a distance $x$ (in minutes) from the origin enters at time $t_x = t_0 + x$, and the fraction of matings in which it is transferred at all is $\mathrm{e}^{-\lambda x}$. The final (plateau) frequency of recombinants carrying the marker therefore declines exponentially with its position, a transfer gradient: for markers $x_1$ and $x_2$, the ratio of plateaus is $\mathrm{e}^{-\lambda(x_2 - x_1)}$.

The minute is the unit of the *E. coli* map: the whole chromosome is $100\,\mathrm{min}$, so $1\,\mathrm{min} \approx 46\,\mathrm{kb}$, and the origin of the map (0 min) is at *thr*. The gradient is itself a mapping tool, since the plateau frequencies give order and rough distance even without a time course: with $\lambda = 0.06\,\mathrm{min}^{-1}$ a marker $20\,\mathrm{min}$ beyond the selected one is inherited by $\mathrm{e}^{-1.2} = 30\,\%$ of recombinants, and only about $0.2\,\%$ of pairs transfer the entire chromosome.

### 10.4.4. The Circular Chromosome

Different Hfr strains, derived from independent integrations of F at different insertion sequences, transfer the chromosome from different origins and in either direction. Each gives a linear order of markers, and the orders are all segments of one circle (Figure). This was the first evidence (Jacob and Wollman, 1958) that the *E. coli* chromosome is circular, long before it was seen by autoradiography (Cairns, 1963).

**Algorithm 10.4.1 (Inferring a Circular Map From Several Hfr Strains)**

1. For each Hfr strain, write the markers in the order of entry, with the entry times.
2. Align the lists by shared markers; reverse a list if its markers appear in the opposite order (that Hfr transfers in the opposite direction).
3. Join the lists where they overlap. If the joined list closes on itself (the last markers of one list are the first of another), the map is circular.
4. Place each Hfr origin between its first marker and the marker that precedes it on the circle, with an arrow in the direction of transfer; convert entry times into distances by subtracting.

**Example 10.4.1** Four Hfr strains transfer (in order of entry): Hfr1 *a b c d*; Hfr2 *e f g a*; Hfr3 *d c b a g*; Hfr4 *c d e f*. Hfr1 and Hfr3 transfer the same markers in opposite directions. Joining Hfr4 *c d e f* with Hfr2 *e f g a* gives *c d e f g a*, and with Hfr1 *a b c*, *c d e f g a b c*: the list closes on itself, so the map is the circle *a b c d e f g* (back to *a*). Hfr1's origin lies between *g* and *a* (transfer *a* → *b*), Hfr2's between *d* and *e*, Hfr4's between *b* and *c*, all in the same direction, and Hfr3's between *e* and *d*, transferring in the opposite direction.

![The circular *E. coli* map with the origins of several Hfr strains. The chromosome is drawn with its standard coordinates in minutes (0 at *thr*, 100 in all) and selected markers outside the circle. Each yellow dot is the integration site of F in one Hfr strain, and the arrow beside it shows the direction in which that strain transfers the chromosome: the markers it transfers first are those just ahead of its arrow. Positions approximate.](./plots/hfr-map.py)

### 10.4.5. Fine Mapping by Recombination

Time of entry is accurate to about a minute. Closer markers are mapped by the frequency of recombination within the transferred fragment. Choose as the selected marker one that enters after the markers to be mapped, so that every selected recombinant also received the others; the unselected markers are then inherited unless a crossover falls between them and the selected marker.

**Example 10.4.2** An interrupted-mating experiment has shown the order *met*, *arg*, *leu*, with *met* entering first and *leu* last, all within a few minutes. In an Hfr $met^{+}\,arg^{+}\,leu^{+}\,str^{s}$ × F⁻ $met^{-}\,arg^{-}\,leu^{-}\,str^{r}$ cross, $leu^{+}$ $str^{r}$ recombinants are selected after the pairs have had time to transfer all three markers, and 1000 recombinants are scored:

| Class | Number | Crossovers needed (besides one to the right of *leu*) |
|---|---|---|
| $met^{+}\,arg^{+}\,leu^{+}$ | 628 | one to the left of *met* |
| $met^{-}\,arg^{+}\,leu^{+}$ | 210 | one between *met* and *arg* |
| $met^{-}\,arg^{-}\,leu^{+}$ | 160 | one between *arg* and *leu* |
| $met^{+}\,arg^{-}\,leu^{+}$ | 2 | three (four in all) |

Since the left crossover falls in each region in proportion to its length (when the regions are short), the *met*–*arg* region is about $210/1000 = 21\,\%$ and the *arg*–*leu* region $16\,\%$ of the recombinants' crossover positions; the rare class that needs four crossovers confirms the order (*arg* between *met* and *leu*). Such frequencies are converted into minutes by calibration with markers of known position.

![Fine mapping after conjugation. The donor fragment (blue, entering from the Hfr, *met*⁺ *arg*⁺ *leu*⁺) pairs with the recipient chromosome (pink, *met*⁻ *arg*⁻ *leu*⁻). Selection for *leu*⁺ requires one crossover to the right of *leu*; the position of the second (left) crossover decides which unselected donor markers are inherited: left of *met* (all three), between *met* and *arg* (*arg*⁺ *leu*⁺), or between *arg* and *leu* (*leu*⁺ only). Getting *met*⁺ without *arg*⁺ requires four crossovers and is rare. The counts are those of Example 10.4.2.](./plots/conjugation-fine-mapping.py)

### 10.4.6. F′ Plasmids and Partial Diploids

Excision of F from an Hfr chromosome is occasionally imprecise and takes adjacent chromosomal genes with it, producing an F′ plasmid.

**Definition 10.4.5 (F′ Plasmid and Merodiploid)** An **F′ plasmid** (F-prime) is an F plasmid that carries a segment of the bacterial chromosome. A cell that carries an F′ plasmid and the chromosome is a **merodiploid** (partial diploid) for the chromosomal segment, written for example F′ $lac^{+}/lac^{-}$ (plasmid genotype first).

F′ plasmids transfer efficiently by conjugation, so any recipient can be made diploid for the region they carry. Partial diploids are the bacterial equivalent of heterozygotes: they test dominance (is $lacI^{-}$ recessive to $lacI^{+}$?) and allow the **complementation test** of two mutations, which shows whether they are in the same gene or in different genes, and the cis–trans test of regulatory elements. Jacob and Monod's analysis of the *lac* **operon** with merodiploids, which distinguished trans-acting repressor mutations ($lacI$) from cis-acting operator mutations ($lacO^{c}$), is described in [7.2.11](/7.2.11#sec-11.2.1). For mutations of the *trp* operon, for example, F′ $trpA^{-}\,trpB^{+}/trpA^{+}\,trpB^{-}$ is Trp⁺ (the mutations complement: different genes), while F′ $trpA1/trpA2$ with two mutations in the same gene is Trp⁻.

## 10.5. Transduction

### 10.5.1. Phages and Their Life Cycles

Bacteriophages, viruses that infect bacteria, are the vehicles of transduction. A virulent phage, such as T4 or T7, follows only the lytic cycle: it injects its DNA, takes over the cell, replicates, packages its genome into new particles and lyses the cell, releasing tens to hundreds of progeny within half an hour. On a lawn of bacteria, each infected cell starts a cycle of infection that spreads radially and forms a clear area, a plaque; counting plaques gives the titre of a phage suspension just as colonies count bacteria. A **temperate phage**, such as λ or P1, can instead enter **lysogeny**: λ integrates into the chromosome as a **prophage** at a specific site by **site-specific recombination**, P1 persists as a plasmid, and the cell, a lysogen, can be induced later to enter the lytic cycle ([7.2.11](/7.2.11#sec-11.5)).

**Definition 10.5.1 (Transduction)** **Transduction** is the transfer of bacterial genes from one cell to another by a phage particle. In **generalized transduction**, a transducing particle carries a random segment of the donor chromosome instead of phage DNA, so any gene can be transferred; in **specialized transduction**, the particle carries phage DNA joined to the bacterial genes adjacent to the prophage site, so only those genes are transferred.

Transduction was discovered by Zinder and Lederberg (1952) with phage P22 of *Salmonella*, in a U-tube experiment like Davis's in which, unlike conjugation, the agent passed through the filter but was not destroyed by DNase.

### 10.5.2. Generalized Transduction

Phages such as P1 (*E. coli*) and P22 (*Salmonella*) package DNA by the headful: packaging starts at a recognition site and continues until the head is full, about $100\,\mathrm{kb}$ for P1 (a little more than its genome of $94\,\mathrm{kb}$, about $2\,\mathrm{min}$ of the *E. coli* map, $2.2\,\%$ of the chromosome) and $44\,\mathrm{kb}$ for P22. During lytic growth the phage degrades the host chromosome, and occasionally a fragment of host DNA is packaged instead of phage DNA, in roughly 1 of $10^{3}$ particles for P1. A lysate grown on a donor strain is used to infect a recipient at low multiplicity; the transducing particle injects the donor DNA, which, like the exogenote of conjugation, must be incorporated by two crossovers. Transductants are selected for one donor marker.

**Definition 10.5.2 (Cotransduction)** **Cotransduction** is the transfer of two or more donor markers by a single transducing particle; the cotransduction frequency of an unselected marker is the fraction of transductants for a selected marker that also inherit it.

Two markers can be cotransduced only if they lie within one headful, so cotransduction is the finest of the conjugation-free mapping tools, accurate within $2\,\mathrm{min}$ of the *E. coli* map. Wu derived the expected relationship between cotransduction and distance.

**Formula 10.5.1 (Wu's Formula)** If transducing fragments of length $L$ (in minutes) start at random positions, if the recombination needed for incorporation is equally likely anywhere in the fragment, and if both markers must be on one fragment, the cotransduction frequency of two markers $d$ minutes apart is

$$
C = \Bigl(1 - \frac{d}{L}\Bigr)^3, \qquad d = L\bigl(1 - C^{1/3}\bigr).
$$

The cube combines two requirements: that the fragment carrying the selected marker also carries the other, and that the two crossovers that incorporate the selected marker both fall outside the interval between the markers. The formula fits P1 data for $L \approx 2\,\mathrm{min}$, although real fragments are not uniformly distributed and recombination is not uniform along them.

**Example 10.5.1** P1 grown on a $cysC^{+}\,lysA^{+}$ donor transduces a $cysC^{-}\,lysA^{-}$ recipient; of 300 $cysC^{+}$ transductants, 126 are also $lysA^{+}$, a cotransduction frequency of $0.42$. With $L = 2\,\mathrm{min}$, $d = 2(1 - 0.42^{1/3}) = 2(1 - 0.749) = 0.50\,\mathrm{min}$, about $23\,\mathrm{kb}$. Markers that are never cotransduced are more than $2\,\mathrm{min}$ apart and are mapped by conjugation.

![Cotransduction frequency and distance. (A) Wu's formula C = (1 - d/L)^3 for transducing fragments of L = 2 minutes (P1) and L = 1 minute (a phage with a smaller head), with points from a simulated experiment (random fragment positions and random crossover positions, 300 transductants per pair). (B) The inverse relation used to convert a measured cotransduction frequency into a distance in minutes (L = 2 min); the dashed line marks Example 10.5.1.](./plots/cotransduction.py)

### 10.5.3. Three-Factor Transduction

As in a three-point cross, the order of three closely linked markers is read from the rarest class, the one that requires the most crossovers.

**Algorithm 10.5.1 (Order From a Three-Factor Transduction)** Transduce a recipient $a^{-}\,b^{-}\,c^{-}$ with a lysate grown on $a^{+}\,b^{+}\,c^{+}$, select $a^{+}$ and score $b$ and $c$.

1. Compute the cotransduction frequencies of $b$ and of $c$ with $a$; the marker with the higher frequency is closer to $a$.
2. For each possible order, list the crossovers each class requires: with order $a$–$b$–$c$, the class $a^{+}\,b^{-}\,c^{+}$ needs four crossovers, while every other class needs two.
3. The order in which the rarest class requires four crossovers is the correct one.

**Example 10.5.2** Of 300 $a^{+}$ transductants, 50 are $a^{+}\,b^{+}\,c^{+}$, 75 $a^{+}\,b^{+}\,c^{-}$, 1 $a^{+}\,b^{-}\,c^{+}$ and 174 $a^{+}\,b^{-}\,c^{-}$. Cotransduction with $a$: $b$ $125/300 = 0.42$, $c$ $51/300 = 0.17$. The rare class $a^{+}\,b^{-}\,c^{+}$ needs four crossovers only if $b$ lies between $a$ and $c$, so the order is $a$–$b$–$c$; if $c$ were in the middle, $a^{+}\,b^{+}\,c^{-}$ (75) would have been the rarest.

### 10.5.4. Specialized and Lateral Transduction

Specialized transduction was discovered with λ (Morse, Lederberg and Lederberg, 1956). λ integrates between the *gal* and *bio* genes. When a lysogen is induced, the prophage is normally excised precisely by site-specific recombination, but in about $10^{-5}$ to $10^{-6}$ of cells it is excised aberrantly, carrying a piece of adjacent bacterial DNA (*gal* on one side or *bio* on the other) and leaving behind phage genes that do not fit in the head. The resulting particles, λ*dgal* (defective, carrying *gal*) or λ*bio*, transfer only these neighbouring genes. A lysate made by inducing a lysogen transduces *gal* at about $10^{-6}$ per particle (low-frequency transduction); a transductant that is a double lysogen for wild-type λ and λ*dgal* releases a lysate in which about half the particles are transducing (high-frequency transduction). The recipient can become a partial diploid for *gal*, as with F′.

Lateral transduction, found in *Staphylococcus aureus* (Chen and colleagues, 2018), combines features of both. Some prophages, when induced, do not excise early but replicate bidirectionally in situ and start headful packaging from their *pac* site while still integrated; packaging then runs on into the adjacent chromosome for several headfuls, transferring hundreds of kilobases of host DNA at frequencies a thousand times higher than generalized transduction. Gene transfer agents, phage-like particles encoded in the host genome that package random host DNA (in *Rhodobacter* and other alphaproteobacteria), and DNA carried in membrane vesicles are further routes of horizontal transfer ([7.11](/7.11)).

![Generalized and specialized transduction. (A) Generalized transduction: during lytic growth of a phage such as P1 in the donor (blue chromosome), a random headful of host DNA is occasionally packaged instead of phage DNA (orange); the transducing particle injects it into a recipient (pink chromosome), where two crossovers replace the homologous segment, here making the recipient *a*⁺. (B) Specialized transduction: an integrated λ prophage between *gal* and *bio* is excised aberrantly with the adjacent *gal* gene, giving λ*dgal*, which transfers only *gal*; the recipient becomes a *gal*⁺ transductant, often a partial diploid when the phage integrates.](./plots/transduction.py)

## 10.6. Phage Genetics

Phages have their own genetics. Mutations of phage T4 change plaque morphology (*r*, rapid lysis, large sharp-edged plaques), host range (*h*, ability to grow on a resistant host) or make growth conditional (temperature-sensitive mutants; amber mutants, which grow only on a host carrying a suppressor tRNA). Hershey and Rotman (1949) crossed phages by infecting bacteria simultaneously with two mutants (a mixed infection at high multiplicity) and scoring the progeny plaques.

**Example 10.6.1** Cells are infected with T4 $h\,r^{+}$ and $h^{+}\,r$; of 1000 progeny plaques plated on a mixed indicator lawn, 430 are $h\,r^{+}$, 412 $h^{+}\,r$, 82 $h^{+}\,r^{+}$ and 76 $h\,r$. The recombination frequency is $(82 + 76)/1000 = 15.8\,\%$. Phage maps built this way are additive over short distances and, for T4, circular, although the genome in each particle is linear; this paradox is explained by headful packaging of terminally redundant, circularly permuted genomes.

Phage recombination differs from meiotic recombination: phage DNA molecules recombine repeatedly during several rounds of replication in the cell, as in a random-mating population, so the recombination frequency of unlinked phage markers does not reach $50\,\%$ in one cross, and close double exchanges are in excess (negative interference, [7.4.8](/7.4.8#sec-8.4.3)). The enormous numbers of progeny (a cross can produce $10^{9}$ phages) allow recombination frequencies as low as $10^{-6}$ to be measured with selective hosts, the resolution that Benzer used to map mutations within the *rII* gene down to single base pairs ([7.4.13](/7.4.13)).

## 10.7. Comparing the Tools

| Method | Measured quantity | Resolution | Range |
|---|---|---|---|
| Interrupted mating (Hfr) | time of entry (min) | about $1\,\mathrm{min}$ | whole chromosome, in segments |
| Conjugation, recombination | fraction of recombinants inheriting unselected markers | $0.1\,\mathrm{min}$ | within about $10\,\mathrm{min}$ of the selected marker |
| Generalized transduction (P1) | cotransduction frequency | $< 0.1\,\mathrm{min}$ | within $2\,\mathrm{min}$ |
| Transformation | cotransformation frequency | a few kb | within tens of kb |
| Phage crosses | recombination frequency among progeny | single base pairs (with selection) | one phage genome |

Today a bacterial mutation is usually located by sequencing the whole genome of the mutant ([7.2.6](/7.2.6)), but these tools remain essential to genetics for a different reason: they move defined alleles between strains. P1 transduction is the standard way to transfer a mutation linked to a selectable marker into a new genetic background, conjugation moves plasmids and libraries, and transformation and recombineering ([7.4.19](/7.4.19)) put engineered DNA into chromosomes.

## Summary

- Bacteria are haploid; prototrophs (Definition 10.1.1) grow on minimal medium, auxotrophs need supplements. Selections (Definition 10.1.2) recover rare genotypes from $10^{8}$–$10^{10}$ cells; screens inspect each colony.
- Horizontal gene transfer (Definition 10.2.1) by transformation, conjugation or transduction; the linear exogenote is incorporated by an even number of crossovers (10.2.2), which underlies all mapping.
- Transformation: uptake of free DNA (DNase-sensitive); cotransformation (Definition 10.3.1); double transformation $\propto c$ if linked, $\propto c^{2}$ if unlinked (Formula 10.3.1; Example 10.3.1).
- Conjugation (Definition 10.4.1): F plasmid (Definition 10.4.2), F⁺ × F⁻ gives F⁺ recipients; Hfr (Definition 10.4.3) transfers the chromosome linearly from a fixed origin; interrupted mating (Definition 10.4.4) gives a map in minutes (100 min $\approx 4.64\,\mathrm{Mb}$); transfer gradient $\mathrm{e}^{-\lambda x}$ (Formula 10.4.1); several Hfr orders reveal a circle (Algorithm 10.4.1, Example 10.4.1); fine mapping by the position of the second crossover (Example 10.4.2); F′ and merodiploids for dominance, complementation and cis–trans tests (Definition 10.4.5).
- Transduction (Definition 10.5.1): generalized (headful, P1 about $2\,\mathrm{min}$), cotransduction (Definition 10.5.2) and Wu's formula $C = (1 - d/L)^3$ (Formula 10.5.1; Example 10.5.1); the order of three markers from the class requiring four crossovers (Algorithm 10.5.1, Example 10.5.2); specialized transduction by aberrant excision of λ (λ*dgal*); lateral transduction by in-situ packaging.
- Phage crosses by mixed infection (Example 10.6.1): many rounds of recombination, negative interference, very high resolution (10.6).
- Resolution of the tools (10.7): time of entry about $1\,\mathrm{min}$; cotransduction within $2\,\mathrm{min}$; transformation and phage crosses at the kilobase-to-base-pair scale.

## Questions

1. Why is a selection more powerful than a screen for finding rare recombinants? Give a selection for $thr^{+}$ recombinants of an Hfr $thr^{+}\,str^{s}$ × F⁻ $thr^{-}\,str^{r}$ cross.

   **Answer** A selection lets only the desired cells grow, so $10^{8}$ or more cells can be examined on one plate, while a screen requires inspecting each colony (a few thousand per plate). Plate the mating mixture on minimal medium with streptomycin: $thr^{-}$ recipients cannot grow without threonine, and the $str^{s}$ donors are killed, so only $thr^{+}\,str^{r}$ recombinants form colonies.

2. In the Lederberg–Tatum experiment, prototrophs appeared at $10^{-7}$. The reversion frequency of each single mutation is about $10^{-7}$ per cell. Why can reversion be excluded?

   **Answer** Each strain carries two or three auxotrophic mutations; a prototroph would require two or three independent reversions in one cell, with probability of order $(10^{-7})^2 = 10^{-14}$ or less, far below $10^{-7}$. Indeed neither strain alone gave prototrophs.

3. *B. subtilis* DNA from a $pur^{+}\,met^{+}$ donor is used at two concentrations. At $1\,\mu\mathrm{g\,mL^{-1}}$ the frequencies per recipient are $pur^{+}$ $10^{-3}$, $met^{+}$ $8 \times 10^{-4}$, $pur^{+}\,met^{+}$ $8 \times 10^{-7}$; at $0.1\,\mu\mathrm{g\,mL^{-1}}$ they are $10^{-4}$, $8 \times 10^{-5}$ and $8 \times 10^{-9}$. Are the markers linked?

   **Answer** At $1\,\mu\mathrm{g\,mL^{-1}}$ the double frequency equals the product of the singles ($10^{-3} \times 8 \times 10^{-4} = 8 \times 10^{-7}$), and it falls 100-fold (as $c^2$) when the DNA is diluted tenfold, while the singles fall tenfold. The doubles arise from two independent fragments: the markers are not cotransformed (not within one fragment).

4. An HfrH × F⁻ interrupted mating gives the following times of first appearance of donor markers: *azi* 9 min, *ton* 11 min, *lac* 18 min, *gal* 25 min. Draw the map and give the distances in kilobases.

   **Answer** Order (from the origin) *azi*–*ton*–*lac*–*gal*, with intervals 2, 7 and 7 min. With $1\,\mathrm{min} \approx 46\,\mathrm{kb}$: about 93, 325 and 325 kb.

5. In the cross of Question 4, the plateau frequency of $azi^{r}$ among selected recombinants is 90 % and that of $gal^{+}$ 30 %. Estimate the pair breakage rate $\lambda$ and the fraction of matings that transfer the whole chromosome.

   **Answer** $\mathrm{e}^{-\lambda(25 - 9)} = 30/90$, so $\lambda = \ln 3/16 = 0.069\,\mathrm{min}^{-1}$. Whole chromosome (100 min): $\mathrm{e}^{-6.9} = 1.0 \times 10^{-3}$.

6. Five Hfr strains transfer markers in these orders: Hfr1 *q r s t*; Hfr2 *v u t s*; Hfr3 *p w v u*; Hfr4 *r q p w*; Hfr5 *t u v w*. Draw the map, and mark each origin and direction.

   **Answer** Joining overlaps: Hfr5 *t u v w*, Hfr3 reversed *u v w p*, Hfr4 reversed *w p q r*, Hfr1 *q r s t*: *t u v w p q r s t*, a circle *p q r s t u v w*. Origins (before the first marker, in the transfer direction): Hfr1 between *p* and *q*, clockwise (*q* → *r*); Hfr5 between *s* and *t*, clockwise; Hfr2 between *w* and *v*, anticlockwise (*v* → *u*); Hfr3 between *q* and *p*, anticlockwise; Hfr4 between *s* and *r*, anticlockwise.

7. Why do recipients in an Hfr × F⁻ cross almost never become Hfr or F⁺, whereas recipients in F⁺ × F⁻ crosses always become F⁺?

   **Answer** In an Hfr, transfer starts within the integrated F at *oriT*, and the rest of F comes last, after the entire chromosome (100 min); mating pairs almost always break before that (Question 5: about 1 in 1000 transfer everything). An autonomous F plasmid of 100 kb is transferred completely in about 2 min.

8. In a fine-mapping cross like Example 10.4.2 with the order *pro*–*his*–*trp* (*trp* entering last and selected), 1000 $trp^{+}$ recombinants contain 700 $pro^{+}\,his^{+}$, 180 $pro^{-}\,his^{+}$, 118 $pro^{-}\,his^{-}$ and 2 $pro^{+}\,his^{-}$. Which region is longer, and how does the rare class confirm the order?

   **Answer** The second crossover falls between *pro* and *his* in 180 and between *his* and *trp* in 118 of the 1000: the *pro*–*his* region is about $1.5$ times longer. The rare class $pro^{+}\,his^{-}$ needs four crossovers (one each side of *his*, plus the flanking two) only if *his* is between *pro* and *trp*.

9. An F′ $lacZ^{-}\,lacY^{+}/lacZ^{+}\,lacY^{-}$ merodiploid can use lactose; an F′ $lacZ1/lacZ2$ merodiploid cannot. Interpret.

   **Answer** In the first, each copy supplies the product the other lacks (β-galactosidase from the chromosome, permease from the plasmid): the mutations complement, so they are in different genes. In the second, both copies lack functional β-galactosidase: $lacZ1$ and $lacZ2$ fail to complement and are alleles of one gene.

10. A P1 lysate on a $thr^{+}\,leu^{+}$ donor transduces a $thr^{-}\,leu^{-}$ recipient; selecting $leu^{+}$, 3 % of transductants are also $thr^{+}$. Estimate the distance with Wu's formula ($L = 2\,\mathrm{min}$). How reliable is the estimate?

    **Answer** $d = 2(1 - 0.03^{1/3}) = 2(1 - 0.311) = 1.38\,\mathrm{min}$. Near the limit of a headful the formula is sensitive to $L$ and to the nonrandom positions of packaging and recombination, and the low frequency has a large relative sampling error, so the estimate is only rough; conjugation data would be used to confirm it.

11. What cotransduction frequencies does Wu's formula predict for markers 0.25, 1.0 and 1.5 min apart with P1?

    **Answer** $(1 - 0.125)^3 = 0.670$, $(1 - 0.5)^3 = 0.125$, $(1 - 0.75)^3 = 0.0156$.

12. In a three-factor transduction with $x^{+}$ selected, the transductants are: $x^{+}\,y^{+}\,z^{+}$ 30, $x^{+}\,y^{-}\,z^{+}$ 90, $x^{+}\,y^{+}\,z^{-}$ 2, $x^{+}\,y^{-}\,z^{-}$ 178. Determine the cotransduction frequencies and the order.

    **Answer** $y$: $32/300 = 0.107$; $z$: $120/300 = 0.40$. The rarest class $x^{+}\,y^{+}\,z^{-}$ requires four crossovers if $z$ is between $x$ and $y$: order $x$–$z$–$y$, consistent with $z$ being cotransduced more often than $y$.

13. Why can specialized transduction by λ transfer only *gal* and *bio*, and why is a lysate from a double lysogen (λ/λ*dgal*) much more efficient than one from a normal lysogen?

    **Answer** λ integrates at one site, between *gal* and *bio*; aberrant excision can only take genes adjacent to the prophage, and the particle has room only for a limited amount of DNA. In a normal lysogen aberrant excision occurs in about $10^{-5}$–$10^{-6}$ of cells, so transducing particles are rare. In a double lysogen both prophages are excised and replicated, the wild-type λ providing the functions missing from λ*dgal*, so about half the progeny are λ*dgal*.

14. In a T4 cross $a\,b^{+} \times a^{+}\,b$, 50 of 1200 progeny are recombinant. In a cross $b\,c^{+} \times b^{+}\,c$, 90 of 1500 are recombinant, and in $a\,c^{+} \times a^{+}\,c$, 140 of 1400. Give the map.

    **Answer** $r_{ab} = 4.2\,\%$, $r_{bc} = 6.0\,\%$, $r_{ac} = 10.0\,\%$. Since $4.2 + 6.0 \approx 10.0$, the order is $a$–$b$–$c$ with distances 4.2 and 6.0 map units.
