---
title: "Bacterial Genetics: Genomes, Mobile Elements and Horizontal Gene Transfer"
description: "The prokaryotic genome: circular and linear chromosomes, size and gene density, operons and gene dosage during replication, core and accessory genome, minimal genomes. Plasmids: types, replication and copy-number control, incompatibility, partition and toxin-antitoxin systems, the cost of carriage. Mobile elements: insertion sequences, transposons, transposon mutagenesis and Tn-seq, integrons and gene cassettes, genomic islands and integrative conjugative elements. Mutation in bacterial populations, mutagens and the Ames test. The biology of transformation, transduction and conjugation, gene transfer in archaea, and the barriers that limit horizontal gene transfer."
---

A bacterium is haploid, divides every twenty minutes to a few hours, and lives in populations of billions. Under these conditions evolution is a laboratory phenomenon: a culture produces every possible point mutation of every gene many times over in a single overnight growth, and genes also arrive ready-made from other cells, sometimes from other phyla. This chapter describes the genetic material on which these processes act — the chromosome, its plasmids and its mobile elements — and the three routes by which DNA moves between cells. It is the genetic background to antimicrobial resistance ([7.11.15](/7.11.15)), to the diversity of bacterial lineages ([7.11.16](/7.11.16)) and to the way pathogens acquire their weapons ([7.11.33](/7.11.33)).

The classical experiments that discovered **transformation**, **conjugation** and **transduction**, and the use of these processes to map genes by interrupted mating and cotransduction, are described in [7.4.10](/7.4.10); the kinds of mutations, the **fluctuation test** and the measurement of **mutation rates** in [7.4.12](/7.4.12); the molecular mechanisms of **homologous recombination** and transposition in [7.2.9](/7.2.9#sec-9.8); **DNA lesions** and their repair in [7.2.8](/7.2.8). None of that is repeated here. The subject of this chapter is the microbiological one: what these elements are, how they are organized and controlled, how often they move in nature, and what they do to the organisms that carry them.

## 13.1. The Prokaryotic Genome

### 13.1.1. Chromosomes

Most bacteria and archaea carry their genes on a single circular chromosome, replicated bidirectionally from one origin ([7.11.8](/7.11.8#sec-8.1.2)) and compacted as a **nucleoid**. The rule has instructive exceptions. *Borrelia burgdorferi*, the agent of Lyme disease, has a linear chromosome of $0.91\,\mathrm{Mb}$ together with twelve linear and nine circular plasmids; *Streptomyces coelicolor* has a linear chromosome of $8.7\,\mathrm{Mb}$. A linear replicon faces the end-replication problem that telomeres solve in eukaryotes ([7.2.7](/7.2.7#sec-7.6)); bacteria solve it differently, with covalently closed hairpin ends resolved by a telomere resolvase (*Borrelia*) or with terminal proteins bound to the $5'$ ends that prime the last stretch of synthesis (*Streptomyces*). *Vibrio cholerae* has two circular chromosomes, one of $2.96\,\mathrm{Mb}$ carrying most essential genes and one of $1.07\,\mathrm{Mb}$ whose replication system is plasmid-like; such secondary replicons, common in the *Pseudomonadota* (formerly Proteobacteria), appear to be domesticated **plasmids** that captured essential genes. Their replication is timed so that both chromosomes finish together.

### 13.1.2. Size, Gene Number and Density

**Property 13.1.1 (Genomes of Bacteria and Archaea Are Small and Dense)** Prokaryotic **genome sizes** span about $0.11$ to $16\,\mathrm{Mb}$. Across this whole range the number of protein-coding genes is proportional to the length of the genome, close to one gene per kilobase, because coding sequence occupies $85$–$90\,\%$ of the DNA: there are few introns, little repetitive DNA and short intergenic regions.

![Genome size and gene content of Bacteria and Archaea. A: protein-coding genes (ORFs) against genome size for representative sequenced genomes, on logarithmic axes; circles are bacteria, triangles archaea, and the color gives the way of life. The dashed line is the pooled gene density of these genomes, 0.89 genes per kilobase: gene number is proportional to genome size over more than two orders of magnitude. The smallest genomes belong to insect endosymbionts (*N. deltocephalinicola*, 112 kb, 137 genes; *B. aphidicola*), then to parasites (*M. genitalium*, *R. prowazekii*, and the archaeon *N. equitans*); free-living soil bacteria have the largest (*S. coelicolor*, *S. cellulosum*, 14.8 Mb). B: the functional categories of the genes of three genomes of decreasing size. Metabolism dominates large genomes, while the share of genes devoted to translation rises from 4 % in *E. coli* to 22 % in *M. genitalium*: a cell can give up biosynthesis and regulation but not its ribosomes. Data from Madigan et al. (2019).](./plots/genome-size.py)

The extremes are informative. Genomes below about $1\,\mathrm{Mb}$ belong to organisms that live inside other cells and have lost what their host provides: the sap-feeding insect endosymbiont *Nasuia deltocephalinicola* has $112\,\mathrm{kb}$ and 137 genes, less than the largest viral genomes. Genome reduction of this kind is a one-way street driven by drift in tiny, clonal, bottlenecked populations ([7.10.18](/7.10.18#sec-18.8.3)), and is treated with the symbioses in [7.11.31](/7.11.31). At the other end, the myxobacterium *Sorangium cellulosum* ($14.8\,\mathrm{Mb}$, 11 559 genes) has more genes than baker's yeast; large genomes belong to soil and freshwater bacteria with versatile metabolism and complex development, and they spend a disproportionate share of their genes on transcriptional regulation and signal transduction, because the main cost of a versatile life is deciding what to do.

The free-living minimum is about $1.3\,\mathrm{Mb}$ and 1300 genes. A laboratory minimum is lower: JCVI-syn3.0, whose chemically synthesized genome of $531\,\mathrm{kb}$ with 473 genes supports growth in a rich medium, with about a third of its genes still of unknown function ([7.3.1](/7.3.1#sec-1.3.4)). Systematic inactivation of genes one by one in *E. coli* and *B. subtilis* likewise finds only $300$–$400$ genes strictly essential in the laboratory — a reminder that "essential" is a statement about a condition, not about a gene.

### 13.1.3. Organization: Operons, Coupling and Gene Dosage

Genes for one pathway are often adjacent and transcribed from a single promoter into a polycistronic mRNA, an **operon** ([7.2.11](/7.2.11)); in *E. coli*, however, many transcription units contain a single gene, so the operon is a conspicuous arrangement rather than the usual one. Because there is no nucleus, ribosomes load onto an mRNA while RNA polymerase is still making it; this coupling of transcription and translation makes expression fast and also makes translation part of transcriptional control, as in **attenuation** ([7.2.10](/7.2.10#sec-10.7.3)).

A consequence of the way bacteria replicate is less obvious. During rapid growth, replication forks are always present and several rounds overlap ([7.11.8](/7.11.8#sec-8.1.2)), so genes near the origin are present in more copies than genes near the terminus — up to four- to eightfold in the fastest growth. Gene position is therefore a quantitative regulatory device: ribosomal RNA operons sit near the origin in fast-growing species and are thereby amplified exactly when they are needed. Transient imbalances also carry information. In *B. subtilis* the sporulation genes *spo0F* and *kinA* lie at opposite ends of the replication arc, so each round of replication produces a pulse of imbalance between them; the sporulation phosphorelay converts the pulse into a once-per-cycle pulse of the master regulator Spo0A~P, at which the cell decides whether to sporulate ([7.11.12](/7.11.12)).

### 13.1.4. Core Genome, Accessory Genome and Islands

Two strains of one bacterial species may differ by a quarter of their genes. The *E. coli* **pangenome** ([Definition 14.2.2](/7.4.14#def-14.2.2)) consists of a **core genome** of a few thousand genes present in every strain and a much larger **accessory genome** present in some; the harmless laboratory strain K-12 ($4.64\,\mathrm{Mb}$) and the enterohemorrhagic strain O157:H7 ($5.59\,\mathrm{Mb}$) share about 4000 genes, while O157:H7 carries more than a thousand that K-12 lacks. The evolutionary meaning of open pangenomes is discussed in [7.10.27](/7.10.27#sec-27.6.3); what matters here is how the accessory genes are arranged.

**Definition 13.1.1 (Genomic Island)** A **genomic island** is a cluster of genes, typically $10$–$200\,\mathrm{kb}$, that is present in some strains of a species and absent from others, inserted at a defined chromosomal site. Islands are recognized by their restricted distribution, by a base composition and codon usage unlike that of the rest of the chromosome, and by their structure: many are flanked by direct repeats, insert into a tRNA gene (which is regenerated on insertion) and carry an integrase gene, the signature of acquisition by site-specific recombination.

**Definition 13.1.2 (Pathogenicity Island)** A **pathogenicity island** is a genomic island carrying genes for virulence, such as adhesins, toxins, secretion systems or iron-uptake systems. Examples are the LEE island of enteropathogenic *E. coli*, which encodes a type III secretion system, SPI-1 and SPI-2 of *Salmonella enterica*, and the *cag* island of *Helicobacter pylori*.

Islands are not confined to pathogens: there are islands for the degradation of aromatic compounds, for symbiosis with legumes and for magnetosome formation ([7.11.17](/7.11.17)). The base composition of an island approaches that of its host genome over time (amelioration), so compositional signals detect only recent acquisitions, and an island that has lost its integrase or its ends is a permanent part of the chromosome. The accessory genome thus grades continuously into the core.

## 13.2. Plasmids

### 13.2.1. What Plasmids Are and What They Carry

**Definition 13.2.1 (Plasmid)** A **plasmid** is a replicon, usually a circular double-stranded DNA molecule, that replicates independently of the chromosome and is not required for growth under all conditions. Plasmids range from about $1\,\mathrm{kb}$ to more than $1\,\mathrm{Mb}$ and are present in one to several hundred copies per cell. A plasmid able to integrate reversibly into the chromosome is an **episome**; the **F plasmid** is the classic example ([Definition 10.4.2](/7.4.10#def-10.4.2)).

Plasmid genes are dispensable in the sense that a cured cell grows, but they often decide where a cell can live. The recurring types are:

| Type | Example | What it provides |
|---|---|---|
| Fertility | F of *E. coli* ($99\,\mathrm{kb}$) | conjugative transfer; mobilization of the chromosome from Hfr donors |
| Resistance (**R plasmid**) | R100, R1 | resistance to several antibiotics and to heavy metals, usually conjugative |
| Bacteriocinogenic | ColE1 | colicins that kill related strains, plus immunity to one's own |
| Virulence | pXO1/pXO2 of *Bacillus anthracis*, the pYV plasmids of *Yersinia* | toxins, capsule, secretion systems |
| Degradative | TOL (pWW0) of *Pseudomonas putida* | enzymes for toluene, camphor, naphthalene, herbicides |
| Tumor-inducing | **Ti plasmid** of *Agrobacterium tumefaciens* | transfer of T-DNA into plant cells; the basis of plant transformation |

**Definition 13.2.2 (R Plasmid)** An **R plasmid** (resistance plasmid) is a plasmid carrying genes for resistance to antimicrobial drugs, usually several at once and frequently together with resistance to heavy metals and disinfectants. Plasmid R100, for example, carries resistance to sulfonamides, streptomycin, spectinomycin, chloramphenicol and tetracycline, and to mercury, and transfers itself by conjugation.

R plasmids explain the speed at which resistance spreads. Their resistance genes sit in mobile elements nested inside one another, so that a single conjugation event moves resistance to several unrelated drugs into a new host, and selection by any one of the drugs maintains the whole set.

![Anatomy of a conjugative R plasmid (schematic, in the style of the IncF resistance plasmids R1 and R100; the positions are illustrative). The backbone (blue) carries the functions of the plasmid itself: the origin of vegetative replication oriV with the copy-number control genes, a partition system par, a toxin-antitoxin module (green), and the tra region encoding the sex pilus, the type IV secretion system and the relaxase, with the origin of transfer oriT. The accessory genes (pink) sit in mobile elements (yellow): a composite transposon Tn10 whose tetracycline-resistance gene lies between two copies of IS10; a Tn3-family transposon carrying bla, a β-lactamase; and a Tn21-like transposon that carries mercury resistance and a class 1 integron, whose integrase intI1 (green) has captured the cassette aadA (streptomycin and spectinomycin resistance) upstream of sul1 (sulfonamide resistance).](./plots/r-plasmid.py)

### 13.2.2. Replication Control and Incompatibility

Every plasmid controls its own copy number: an inhibitor made from the plasmid, usually a small antisense RNA (RNA I of the ColE1 family) or an iteron-binding Rep protein, accumulates in proportion to the number of copies and shuts initiation down. The control is negative feedback on a number, so the copy number is a property of the plasmid, not of the host: ColE1 derivatives used as cloning vectors sit at 15–20 copies and their high-copy mutants at several hundred, while the F plasmid and most large conjugative plasmids keep one or two copies per chromosome, because replicating $100\,\mathrm{kb}$ many times over would be expensive.

**Definition 13.2.3 (Plasmid Incompatibility)** Two plasmids are **incompatible** if they cannot be stably maintained together in one lineage without selection for both: one or the other is lost from the descendants. Incompatibility arises when two plasmids share a replication control circuit or a partition system, so that the control system counts them as one population and the random choice of which copy to replicate and which to segregate leads to the loss of one type. Plasmids are grouped into incompatibility (Inc) groups on this criterion; it is a classification by replication machinery, and relatives of the F plasmid (IncF), of RP4 (IncP) and of RSF1010 (IncQ) each form one.

Host range is another property of the replication system. Narrow-host-range plasmids (ColE1, F) replicate only in enteric bacteria because they depend on host proteins; broad-host-range plasmids such as RP4 (IncP) and RSF1010 (IncQ) encode most of their own replication functions and are maintained in almost any Gram-negative bacterium, which makes them the vehicles of resistance spread across genera and the standard vectors for genetic work in non-model organisms.

### 13.2.3. Staying in the Population

A plasmid is lost unless it is both inherited and selected. Three devices work against loss.

- Active partition. Low-copy plasmids cannot rely on diffusion: if two copies segregate at random, one daughter in two would be plasmid-free after a few divisions. They carry active partition systems in which a centromere-like site (*parC*) is bound by an adaptor (ParR) and pushed apart by a cytoskeletal filament: in the ParMRC system of plasmid R1, actin-like ParM polymerizes between the two plasmid copies and drives them to opposite poles, while other systems use the ParA ATPase that also segregates chromosomes ([7.11.8](/7.11.8#sec-8.1.2)). Multimer resolution systems (*cer*/XerCD) additionally convert dimers back to monomers, which otherwise behave as one segregating unit.
- Postsegregational killing of cells that lose the plasmid.

  **Definition 13.2.4 (Toxin–Antitoxin System)** A **toxin–antitoxin system** is a pair of genes encoding a stable toxin and an unstable antitoxin that neutralizes it. While the module is present, the antitoxin is made continuously and the cell is unharmed; in a cell that has lost the module, the antitoxin is degraded within minutes while the toxin persists, so the cell dies or stops growing. Examples are *ccdAB* on the F plasmid (the toxin poisons DNA gyrase) and *hok/sok* on R1 (an antisense RNA antitoxin; the toxin damages the membrane).

  Toxin–antitoxin systems are addiction modules: they do not help the plasmid replicate, they eliminate the competitors produced by its failures. Chromosomal copies of the same modules are common and have been implicated in the dormancy of persister cells ([7.11.15](/7.11.15)) and in abortive infection by phages ([7.11.23](/7.11.23)).
- Infectious transfer. A conjugative plasmid need not be free of cost if it spreads horizontally faster than it is lost, like an infectious disease of the bacterial population.

**Formula 13.2.1 (Invasion of a Conjugative Plasmid)** Consider plasmid-free cells $F$ and plasmid-bearing cells $P$ growing in a chemostat at dilution rate $D$ on a resource $R$ with the Monod growth rate $\psi(R)$ ([7.6.39](/7.6.39)). Let the plasmid impose a relative cost $c$, let a fraction $\lambda$ of divisions of plasmid-bearing cells produce a plasmid-free segregant, and let conjugation follow mass action with rate constant $\gamma$:

$$
\begin{aligned}
\frac{\mathrm{d}F}{\mathrm{d}t} &= \psi(R)F + \lambda(1-c)\psi(R)P - \gamma FP - DF, \\
\frac{\mathrm{d}P}{\mathrm{d}t} &= (1-\lambda)(1-c)\psi(R)P + \gamma FP - DP.
\end{aligned}
$$
A rare plasmid invades a resident population at its steady state $F^{*}$ (where $\psi(R) = D$) when $\mathrm{d}P/\mathrm{d}t > 0$ for small $P$, that is when

$$
\gamma F^{*} > D\bigl[1 - (1-c)(1-\lambda)\bigr] \approx D(c + \lambda). \tag{13.1}
$$
Transfer must therefore be fast enough to pay for both the cost of carriage and the rate of segregational loss; since $F^{*}$ is the density of susceptible cells, a plasmid that cannot invade a sparse population may invade a dense one such as a biofilm or a gut.

![Population biology of a conjugative plasmid in a chemostat, from the model of Formula 13.2.1 (μmax = 1 h⁻¹, K = 1 μg mL⁻¹, feed 100 μg mL⁻¹, D = 0.2 h⁻¹, λ = 10⁻³; parameters illustrative). A: a thousand plasmid-bearing cells per milliliter are added to a resident population at steady state, with a cost of carriage of 5 %. Without conjugation the plasmid-bearing cells are diluted out; with a transfer rate below the threshold of Eq. (13.1) they still decline; above it the plasmid spreads through the population in a few hundred hours like an infection and then persists, with a minority of plasmid-free segregants (dashed) maintained by segregation. B: the plasmid-bearing fraction at the end of a long run, over transfer rate constants and costs; the dashed curve is the invasion threshold of Eq. (13.1). Costly plasmids persist only if they transfer fast.](./plots/plasmid-maintenance.py)

The model explains two observations: that plasmids carrying useless genes are nonetheless common in nature, and that resistance plasmids are lost slowly, if at all, when antibiotic use stops. The cost of carriage is itself evolvable — compensatory mutations in the host or the plasmid often reduce it to zero within a few hundred generations, after which there is no selection against the plasmid at all ([7.11.15](/7.11.15)).

## 13.3. Mobile Elements

### 13.3.1. Insertion Sequences and Transposons

The mobile elements of bacteria are variations on one theme: a segment of DNA bounded by inverted repeats, encoding a transposase that recognizes those repeats and moves what lies between them. The chemistry (transesterification by a DDE transposase, the target-site duplication, cut-and-paste and replicative pathways, the cointegrate and its resolution) is described in [7.2.9](/7.2.9#sec-9.8) and is not repeated; what distinguishes the bacterial elements is their content and their traffic between replicons.

**Definition 13.3.1 (Insertion Sequence and Composite Transposon)** An **insertion sequence** (IS element) is the simplest bacterial transposable element: $0.7$–$2.5\,\mathrm{kb}$ of DNA carrying only a transposase gene between terminal inverted repeats of $10$–$50\,\mathrm{bp}$. A **composite transposon** is a segment of DNA, usually carrying resistance or metabolic genes, flanked by two copies of an IS element whose transposase moves the whole structure by acting on the outer ends. A unit (non-composite) transposon such as Tn3 carries its own transposase and resolvase together with its cargo between $38\,\mathrm{bp}$ inverted repeats and moves replicatively.

Several thousand distinct IS elements have been cataloged, in bacteria, archaea, plasmids and phages; a single strain of *E. coli* carries a few dozen copies of half a dozen families. Their best-known cargo is drug resistance — Tn5 ($5.7\,\mathrm{kb}$, kanamycin, streptomycin and bleomycin resistance between IS50L and IS50R), Tn10 (tetracycline, between IS10 copies), Tn3 (ampicillin, through the β-lactamase *bla*) — but the elements matter at least as much for what they do to the genome as for what they carry:

- They inactivate genes by inserting into them, and turn genes on by bringing promoters.
- Recombination between two copies of the same element produces deletions, inversions and duplications, and joins replicons: it is recombination between IS copies on the F plasmid and on the chromosome that creates **Hfr strains** ([Definition 10.4.3](/7.4.10#def-10.4.3)).
- Their abundance reflects the recent history of a lineage. *Bordetella bronchiseptica*, a broad-host-range respiratory pathogen, has $5.3\,\mathrm{Mb}$ and no known IS elements; the human-restricted *B. pertussis* has a smaller genome, $4.1\,\mathrm{Mb}$, and more than 260 IS copies, which mediated the rearrangements and deletions by which it lost genes while specializing on one host.

Phage Mu takes the theme to its limit: its entire genome is a transposon, and it replicates by transposing a hundred times in each infection ([7.11.23](/7.11.23)).

### 13.3.2. Transposon Mutagenesis and Tn-seq

**Definition 13.3.2 (Transposon Mutagenesis)** **Transposon mutagenesis** is the generation of a library of insertion mutants by introducing a transposon, usually on a suicide vector (a plasmid that cannot replicate in the recipient), and selecting for the resistance marker carried by the transposon, so that survivors are almost all cells in which the transposon has jumped into the genome. Because prokaryotic genomes are dense, most insertions fall in genes, and the disrupted gene is read off directly from the sequence flanking the insertion.

Transposon mutagenesis with Tn5 and Tn10 was the workhorse of bacterial genetics for two decades: a library of a few thousand mutants screened for a phenotype (for example, the loss of biofilm formation by *Pseudomonas aeruginosa*, which identified the flagellar hook protein FlgK) identifies the genes needed for it. High-throughput sequencing turned the screen into a measurement.

**Definition 13.3.3 (Transposon Sequencing)** In **transposon sequencing** (Tn-seq, and the related TraDIS and INSeq), a saturated library of hundreds of thousands of insertion mutants is grown as a pool under a condition of interest, and the insertion sites are counted by sequencing the junctions between the transposon and the genome before and after growth. The change in the number of reads at the insertions within a gene measures the contribution of that gene to fitness in the condition: genes with no insertions recovered are essential, genes depleted during growth contribute to fitness, and genes enriched are costly under that condition.

If the abundance of a mutant grows as $2^{wt}$ with relative fitness $w$ while the pool as a whole grows as $2^{t}$ over $t$ generations, the mutant's share of the pool changes by the factor $2^{(w-1)t}$. Read counts depend on sequencing depth, so they are first normalized to read frequencies $f$ (the reads at the insertions in a gene divided by all reads of the sample), and the per-gene fitness is $w = 1 + t^{-1}\log_2(f_{\mathrm{final}}/f_{\mathrm{initial}})$; a library grown for 10–20 generations resolves fitness differences of a few percent across every gene at once.

![Transposon sequencing (simulated data). A: read counts at the insertion sites of a saturated mariner-transposon library in a 30 kb stretch of genome with ten genes, after 15 generations of growth as a pool. Insertions are spread over the whole segment, but mutants are missing in the two essential genes and strongly depleted in the two genes whose disruption carries a fitness cost; insertions in the last tenth of a gene often leave the product functional and are excluded from the analysis. B: fitness estimated from the ratio of final to initial reads per gene, against the value used in the simulation. One experiment thus gives a quantitative fitness value for every gene, and repeating it in a new condition (an antibiotic, a host, a carbon source) gives the genes that matter in that condition.](./plots/tn-seq.py)

### 13.3.3. Integrons and Gene Cassettes

A transposon moves a fixed cargo. Integrons are platforms that collect new cargo.

**Definition 13.3.4 (Integron and Gene Cassette)** An **integron** is a genetic element consisting of a gene for a site-specific recombinase (the integrase, *intI*), a recombination site *attI* and a promoter Pc, which together capture and express **gene cassettes**. A **gene cassette** is a mobile unit consisting of a single open reading frame, usually without a promoter, and a recombination site *attC*; it exists either free as a covalently closed circle or integrated at *attI* in the array of an integron. Integrase-catalyzed recombination between *attI* and *attC* inserts a cassette at the front of the array, where the promoter Pc transcribes it most strongly; the same reaction in reverse excises cassettes and reshuffles the array.

![Integrons capture and express gene cassettes (a class 1 integron, drawn with SBOL Visual glyphs). 1: the platform — the integrase gene intI, the promoter Pc, the site attI — followed by an array of promoterless cassettes, each a coding sequence with its own attC site, ending in the 3′ conserved segment of class 1 integrons (qacEΔ1 and sul1). 2: a free, circular cassette carrying dfrA (trimethoprim resistance) is inserted at attI by the integrase, which recombines attI with the cassette's attC site. Transcription of intI is repressed by LexA, so the SOS response induced by DNA-damaging antibiotics switches cassette capture on. 3: the newly captured cassette lies closest to Pc and is expressed most strongly (bars); expression of the cassettes behind it falls along the array.](./plots/integron.py)

Integrons are not themselves mobile: they move by sitting in transposons and on plasmids. The class 1 integrons responsible for much of the multidrug resistance of Gram-negative clinical isolates are carried on Tn21-like transposons and end in a conserved segment with *qacE*Δ1 (quaternary ammonium disinfectants) and *sul1* (sulfonamides); more than 130 different resistance cassettes are known in this one class. Two features make the system efficient. The cassettes have no promoters of their own, so capture and expression are one event; and *intI* is part of the LexA regulon, so the **SOS response** provoked by DNA damage — including the damage caused by quinolones and by β-lactams — turns on the very machinery that assembles resistance arrays. Chromosomal "superintegrons" with hundreds of cassettes, as in *Vibrio cholerae*, show that the system is far older than antibiotic therapy and is in origin a general device for storing accessory functions.

### 13.3.4. Integrative Conjugative Elements

**Definition 13.3.5 (Integrative and Conjugative Element)** An **integrative and conjugative element** (ICE, formerly conjugative transposon) is a mobile element that resides integrated in the chromosome and is replicated with it, but can excise as a circle, transfer itself to a new cell by conjugation using a type IV secretion system that it encodes, and integrate into the recipient's chromosome by site-specific recombination. It combines the stability of a chromosomal island with the mobility of a conjugative plasmid.

Tn916 of *Enterococcus faecalis* ($18\,\mathrm{kb}$, tetracycline resistance) transfers to a wide range of Gram-positive recipients; the SXT element of *Vibrio cholerae* ($100\,\mathrm{kb}$) carries resistance to sulfamethoxazole, trimethoprim, chloramphenicol and streptomycin and spread through epidemic cholera strains in the 1990s. ICEs also carry the genes for nitrogen fixation and symbiosis in some rhizobia, so that a non-symbiotic soil bacterium can be converted into a nodule former by a single transfer. With plasmids, prophages, IS elements, transposons and integrons, they make up what is called the mobilome, the mobile fraction of a genome; the categories grade into one another, and most genomic islands are decayed members of it.

## 13.4. Mutation in Bacterial Populations

### 13.4.1. Mutants and How They Are Found

A **mutant** differs from the **wild type** in genotype; it need not differ in phenotype. The practical division is between mutations that can be selected and mutations that must be screened ([Definition 10.1.2](/7.4.10#def-10.1.2)): plating $10^{9}$ cells on streptomycin recovers the one resistant mutant among them, while a pigmentless or auxotrophic mutant must be found by looking at colonies, by **replica plating** or, now, by sequencing. The five-order-of-magnitude difference in throughput is why bacterial genetics is built around selections.

| Class | Change | How it is detected |
|---|---|---|
| **Auxotroph** | loss of an enzyme of a biosynthetic pathway | no growth on minimal medium lacking the nutrient; replica plating |
| Resistant | altered target, detoxification, reduced uptake | growth on an inhibitory concentration of the drug or on a phage lawn |
| Conditional lethal | an essential protein inactivated under restrictive conditions (**temperature-sensitive alleles**; nonsense mutations suppressible in one host) | growth at $30\,^\circ\mathrm{C}$ but not at $42\,^\circ\mathrm{C}$; the only route to essential genes in a haploid |
| Carbon-source | loss of a catabolic enzyme or transporter | color on an indicator medium (MacConkey, EMB) |
| Morphological and colonial | capsule, pigment, flagella, LPS O-antigen | colony appearance: rough instead of smooth, unpigmented, compact instead of spreading |

Alongside these, *phase variation* — the reversible, programmed switching of surface structures by inversion of a promoter, slipped-strand mispairing of repeats or epigenetic methylation — generates heritable variation without mutation, and is treated with immune evasion in [7.11.34](/7.11.34).

### 13.4.2. Rates, Reversion and Suppression

Replication errors in bacteria occur at about $10^{-6}$ to $10^{-7}$ per kilobase per round of replication after proofreading and mismatch repair, so a typical gene of $1\,\mathrm{kb}$ mutates at $10^{-6}$ to $10^{-7}$ per generation and a whole genome at a few times $10^{-3}$ per generation. The second figure is the one that matters in practice: a culture of $10^{9}$ cells per milliliter contains, in every milliliter and every generation, several million new mutations, so that within a few generations every possible point mutation of every gene has arisen. Selection in a bacterial population is therefore rarely limited by the supply of mutations, and resistance to a new drug appears in the clinic within a few years of its introduction.

A point mutation can be reversed. A *same-site revertant* restores activity by a second change at the site of the first, a *true revertant* restores the original sequence, and a **suppressor mutation** restores function from elsewhere: by a second frameshift that restores the reading frame, by a compensating change in an interacting protein, or — the classic case — by a change in the anticodon of a tRNA that makes it read a nonsense codon. Such a suppressor tRNA is viable only because most cells have several tRNAs for a codon, and it is itself a tool: a nonsense mutant grown on a suppressor host behaves as wild type and on a normal host as a null, which makes it a conditional allele for essential genes. Because deletions and insertions do not revert, the reversion frequency of a mutant is evidence about its molecular nature.

### 13.4.3. Mutagens and the Ames Test

Mutagens raise the mutation rate by orders of magnitude, each with a characteristic spectrum, which is why they were the tools with which the genetic code and the nature of mutation were worked out ([7.4.12](/7.4.12#sec-12.7.1), [7.2.8](/7.2.8#sec-8.1.2)).

| Mutagen | Action | Mutations produced |
|---|---|---|
| 5-Bromouracil, 2-aminopurine (**base analogs**) | incorporated in place of T or A; mispair in their rare tautomers | transitions, mostly $\mathrm{A{\cdot}T} \to \mathrm{G{\cdot}C}$ |
| Nitrous acid | deaminates C to U and A to hypoxanthine | transitions in both directions |
| Alkylating agents (EMS, *N*-methyl-*N*′-nitro-*N*-nitrosoguanidine) | alkylate G; $O^{6}$-alkylguanine pairs with T; act on nonreplicating DNA too | $\mathrm{G{\cdot}C} \to \mathrm{A{\cdot}T}$; very high yields |
| Acridines, ethidium bromide (**intercalating agents**) | insert between base pairs and distort the helix | $\pm 1$ frameshifts |
| Ultraviolet radiation ($254\,\mathrm{nm}$) | pyrimidine dimers; bypass by error-prone polymerases | $\mathrm{C} \to \mathrm{T}$ and $\mathrm{CC} \to \mathrm{TT}$ at dipyrimidines |
| Ionizing radiation | hydroxyl radicals; strand breaks | deletions and rearrangements |

The sensitivity of bacterial selections turns mutagenesis into an assay for chemical hazard.

**Definition 13.4.1 (Ames Test)** The **Ames test** measures the mutagenicity of a chemical as the rate at which it reverts a histidine auxotroph of *Salmonella enterica* serovar Typhimurium to prototrophy: the compound is applied to a plate of medium lacking histidine seeded with the tester strain, and revertant colonies are counted against the spontaneous background. The tester strains are sensitized by mutations that remove nucleotide-excision repair (*uvrB*) and part of the lipopolysaccharide (so that chemicals enter), and by a plasmid carrying error-prone repair functions; because many carcinogens become reactive only after metabolism, the chemical is first incubated with a mammalian liver extract (the S9 fraction). Different tester strains carry base-substitution or frameshift alleles, so the test also reports which kind of lesion the compound causes.

In its first validation about $90\,\%$ of the animal carcinogens tested were mutagenic (later, broader surveys found lower agreement, because some carcinogens act without damaging DNA); the test costs a few days instead of two years, and it remains the first screen applied to new chemicals and drugs ([7.2.8](/7.2.8#sec-8.7.1)).

### 13.4.4. Mutation Rate under Stress

The mutation rate is itself a variable. Three observations qualify the picture of a constant, uniform rate.

- The **SOS response** induced by DNA damage includes the error-prone polymerases IV (*dinB*) and V (*umuDC*), which fill gaps and bypass lesions without a template to read, and raise the mutation rate by one to two orders of magnitude for as long as the damage lasts ([7.2.8](/7.2.8#sec-8.6.2)). Since quinolones, β-lactams and UV all induce it, treatment can transiently increase the rate at which resistance arises.
- About $1\,\%$ of natural isolates of *E. coli* and *Salmonella* are mutators, with rates $10$ to $100$ times higher than normal, usually through loss of **mismatch repair**. A mutator allele has no effect of its own, but it hitchhikes with the beneficial mutations it produces, so mutators are enriched in populations adapting to a new environment, and are found more often among pathogens and in long-term infections, such as *Pseudomonas aeruginosa* in cystic fibrosis.
- Starving, nondividing populations continue to acquire mutations (stress-induced mutagenesis), through error-prone polymerases and recombination-dependent replication in a hypermutable subpopulation. The phenomenon is real and the mechanisms are known; the claim that the mutations produced are directed toward usefulness is not supported — the randomness of mutation with respect to its usefulness is established by the fluctuation test ([7.4.12](/7.4.12#sec-12.4)) and has survived every subsequent test.

## 13.5. Transformation

**Definition 13.5.1 (Natural Transformation)** **Natural transformation** is the uptake of free DNA from the environment by a cell in a genetically programmed physiological state, **competence**, and its inheritance, either by recombination into the chromosome or by establishment as a replicon. It is distinguished from artificial transformation, in which the envelope is made permeable by treatment with $\ce{Ca^2+}$ and a heat shock or by electroporation.

Natural competence has been found in some eighty species across most bacterial phyla and in archaea. In some it is a brief, population-wide state: *Streptococcus pneumoniae* becomes competent in early exponential phase, for a few minutes, in all cells at once, in response to a secreted competence-stimulating peptide. In others it is a minority state: about $10$–$20\,\%$ of a *B. subtilis* population becomes competent in stationary phase and remains so for hours, a bistable decision made by the ComK circuit ([7.11.12](/7.11.12)). In *Vibrio cholerae* the inputs are ecological: competence genes are induced by chitin (the material of the crustacean exoskeletons the bacterium colonizes), by quorum sensing at high cell density, and by the absence of glucose. The same cells use a type VI secretion system to kill neighbors and then take up the DNA released from the corpses — predation and gene acquisition in one behavior (Borgeaud and colleagues 2015).

The uptake machinery is built from the components of type IV pili and type II secretion systems, and is essentially the same in Gram-positive and Gram-negative bacteria apart from the extra membrane that the latter must cross.

![DNA uptake in natural transformation (schematic; protein names after *Bacillus subtilis* and *Streptococcus pneumoniae* on the left, *Neisseria* and *Vibrio* on the right). A, Gram-positive: a competence pseudopilus (ComGC) reaches through the thick peptidoglycan and brings bound double-stranded DNA to the membrane receptor ComEA; a nuclease (EndA) degrades one strand, whose nucleotides are released, while the other is threaded through the ComEC channel by the ATPase ComFA. B, Gram-negative: a type IV pilus extends through the PilQ secretin of the outer membrane, binds DNA and is retracted by the PilT ATPase, pulling the double strand into the periplasm, where successive ComEA molecules bind it and ratchet it inward; a single strand then crosses the inner membrane through ComEC. In both, the incoming strand is coated by DprA and loaded with RecA, which finds the homologous sequence in the chromosome and catalyzes strand exchange; after one round of replication, one daughter carries the donor allele.](./plots/transformation-machinery.py)

Three features of the process set what transformation can do.

- Only single strands enter, and only short pieces. A chromosome shears into fragments of about $10\,\mathrm{kb}$ on lysis; a competent *S. pneumoniae* cell binds some ten of them and takes up single strands of around $8\,\mathrm{kb}$. Two markers are therefore inherited together only if they lie within this distance ([Definition 10.3.1](/7.4.10#def-10.3.1)), and a plasmid is a poor substrate, because a single strand cannot replicate.
- Uptake can be selective. *Haemophilus influenzae* takes up DNA efficiently only if it contains a specific $9\,\mathrm{bp}$ uptake signal sequence, present in more than 1400 copies in its own genome; *Neisseria* species have an analogous DNA uptake sequence. Such species therefore sample mainly the DNA of their own kind, which makes transformation a mechanism of recombination within a species rather than of acquisition from outside.
- What the DNA is for. Because competence is regulated and costly, it is presumably adaptive, but for what is debated: as a source of templates for the repair of damaged chromosomes, as a source of new alleles (recombination within the species), or simply as food — DNA is rich in carbon, nitrogen and phosphorus, and in many species most of the DNA taken up is degraded. The three are not exclusive, and the balance differs between species.

## 13.6. Transduction

Transduction is gene transfer in a phage coat: a mistake of phage assembly from the phage's point of view, and the most abundant form of gene transfer in the sea from ours. With some $10^{31}$ phage particles on Earth and roughly ten phages per bacterial cell, even a rare packaging error becomes a large flux of DNA. The two classical mechanisms and their use for mapping are described in [7.4.10](/7.4.10#sec-10.5): in **generalized transduction** a headful of host DNA is packaged in place of the phage genome, so any gene can be transferred, at about one particle in $10^{3}$ and one transductant per $10^{6}$ to $10^{8}$ recipients per gene; in **specialized transduction** a prophage excises imprecisely and carries the genes next to its attachment site. Lateral transduction, in which an induced prophage replicates in place and packages hundreds of kilobases of adjacent chromosome, transfers host genes far more efficiently than either.

For microbiology three consequences matter.

- Transduction moves virulence and resistance genes in nature. Shiga toxin genes of *E. coli* O157:H7, the cholera toxin genes of *V. cholerae* (on the filamentous phage CTXφ), the diphtheria toxin gene of *Corynebacterium diphtheriae* and the pathogenicity islands of *Staphylococcus aureus* all travel in phages; the *S. aureus* islands even hijack the phage, excising and packaging themselves into particles too small to hold the phage genome.
- Lysogeny changes the host. A prophage brings its own genes into the lysogen: immunity against the same phage, and often other traits, which is the phenomenon of **lysogenic conversion** ([7.11.23](/7.11.23)). Many bacteria isolated from nature are lysogens, and prophages make up a substantial fraction of the accessory genome.
- Some cells have domesticated the mechanism.

  **Definition 13.6.1 (Gene Transfer Agent)** A **gene transfer agent** (GTA) is a phage-like particle encoded by the genome of a cell, produced under the control of the cell's own regulatory systems, that packages a random, small fragment of the host genome and delivers it to other cells. GTAs are not viruses: they cannot package enough DNA to encode themselves and they form no plaques. The best-studied, RcGTA of *Rhodobacter capsulatus*, is produced by a subpopulation in stationary phase and carries about $4.5\,\mathrm{kb}$ of host DNA; GTAs are widespread in the *Alphaproteobacteria*, in marine bacteria and in some methanogenic archaea.

## 13.7. Conjugation

Conjugation is transfer through contact, encoded by the transferred element itself. It moves the largest pieces of DNA, it is the main route by which resistance spreads between clinical isolates, and it is the only one of the three mechanisms in which the donor plays an active part.

![The molecular steps of conjugation by an F-like plasmid between two Gram-negative cells. 1: the sex pilus of the donor binds a receptor on the recipient and retracts by depolymerization, pulling the cells together. 2: in the mating pair, a type IV secretion system spans both envelopes; the relaxosome, whose main component is the relaxase TraI, nicks one strand of the plasmid at oriT and the relaxase stays covalently bound to the 5′ end, which a coupling protein hands to the secretion system. 3: the relaxase leads the single strand into the recipient while the donor replaces it by rolling-circle replication from the 3′ end at the nick; the recipient synthesizes the complementary strand. 4: the relaxase rejoins the ends of the transferred strand, both cells hold a complete double-stranded plasmid, and the former recipient is now itself a donor.](./plots/conjugation-steps.py)

Transfer of the $100\,\mathrm{kb}$ F plasmid takes about five minutes, and nearly every cell that forms a mating pair acquires it, so a few donors convert a dense population within hours. The *tra* region that pays for this comprises more than thirty genes, most of them devoted to the pilus and the secretion channel; the F pilus is also the receptor of the RNA and filamentous phages that specifically infect donor cells, one of several costs of being a donor. Surface exclusion prevents a donor from receiving a second copy of the same plasmid.

Four variations extend the reach of the mechanism.

- Chromosome mobilization. When F integrates at one of the IS elements it shares with the chromosome, the cell becomes an **Hfr strain** and transfer initiated at *oriT* runs on into chromosomal DNA; the mating pair usually breaks before the $100\,\mathrm{min}$ needed for the whole chromosome, so the recipient receives a linear fragment and stays F⁻. Imprecise excision gives **F′ plasmids**. These are the basis of genetic mapping ([7.4.10](/7.4.10#sec-10.4)) and, in nature, a route by which chromosomal genes move between strains.
- Mobilizable elements. A plasmid too small to encode a secretion system needs only an *oriT* and a relaxase of its own: it is then mobilized by a conjugative plasmid in the same cell, which lends it the channel. Mobilizable plasmids such as RSF1010 and the ColE1 family outnumber self-transmissible ones, and genomic islands and ICEs are mobilized in the same way.
- Conjugation in Gram-positive bacteria. The machinery is homologous (a relaxase, a coupling protein, a type IV secretion system), but there is no pilus: cells adhere directly. In *Enterococcus faecalis*, recipients secrete short peptide pheromones; a donor carrying the matching plasmid responds by making an aggregation substance that binds it to the recipient, so that transfer is induced by the presence of a partner. Enterococcal conjugative plasmids also carry vancomycin resistance (*vanA* in transposon Tn1546), which has been transferred from them to *Staphylococcus aureus* in patients.
- Transfer across the boundaries of life. Conjugative systems are promiscuous: IncP plasmids transfer between almost all Gram-negative bacteria and to Gram-positive recipients, and the laboratory has demonstrated transfer from *E. coli* to yeast and to cultured mammalian cells. Nature's example is *Agrobacterium tumefaciens*, which uses a type IV secretion system to inject part of its **Ti plasmid**, the T-DNA, into a plant cell, where it integrates into the nuclear genome and directs the plant to make a tumor and to feed the bacterium — the mechanism that became the standard method of plant transformation.

## 13.8. Gene Transfer in Archaea

Archaea exchange DNA as freely as bacteria, as their genomes show, but their mechanisms are only partly the same, and laboratory systems are less developed, partly because most model archaea are extremophiles and because few antibiotics act on them, so selectable markers are scarce (novobiocin and mevinolin for halophiles, puromycin and neomycin for methanogens).

Natural transformation occurs in the methanogen *Methanococcus voltae* and in the hyperthermophiles *Thermococcus kodakarensis* and *Pyrococcus furiosus*. Transduction is known for only one archaeal virus. Conjugative plasmids occur in *Sulfolobus*, but they use systems with little resemblance to the bacterial *tra* machinery. Two archaeal routes have no bacterial counterpart:

- Cell fusion. *Haloferax volcanii* forms cytoplasmic bridges between mated cells through which chromosomal DNA passes in both directions, producing cells with mixed genomes that later segregate recombinants — the nearest prokaryotic analog of sex, since the exchange is reciprocal.
- Damage-induced aggregation. UV irradiation and other DNA-damaging treatments induce *Sulfolobus* cells to make Ups pili, which make them aggregate with cells of the same species (recognized by the glycosylation pattern of the S-layer) and exchange DNA; recombination then repairs the damaged chromosomes. Here gene exchange is visibly a repair mechanism. *Thermococcus* species release membrane vesicles that carry DNA, including plasmids, from cell to cell.

## 13.9. The Limits of Horizontal Transfer

Transfer is frequent, but most transferred DNA leaves no trace. Four barriers act in succession, and they decide what a genome looks like.

1. Physical and ecological barriers. Donor and recipient must share a habitat, and the vehicle must fit: free DNA is degraded by nucleases within minutes in most environments, a phage has a narrow host range, conjugation needs contact, which is why transfer rates in biofilms and in the gut are orders of magnitude higher than in planktonic culture.
2. Immunity against foreign DNA. **Restriction–modification systems** cleave incoming DNA that lacks the host's methylation pattern; CRISPR–Cas systems destroy sequences recorded in previous encounters, and are present in roughly $40\,\%$ of bacterial and $85\,\%$ of archaeal genomes ([7.11.23](/7.11.23)). Both reduce transfer by orders of magnitude but neither is absolute: a fraction of incoming molecules is methylated before it is cut, and phages and plasmids carry anti-restriction and anti-CRISPR proteins.
3. Recombination requires homology. A transferred fragment that is not a replicon survives only if it recombines, and **homologous recombination** by RecA needs a long stretch of near-identity. **Mismatch repair** rejects recombination between diverged sequences: in *mutS* or *mutL* mutants, recombination between *E. coli* and *Salmonella*, whose genomes differ by about $20\,\%$, rises a thousandfold. The frequency of recombination falls roughly exponentially with sequence divergence, so homologous exchange is mainly a within-species process, and it is through illegitimate or site-specific routes — transposition, integration at *att* sites, integron capture — that genes cross between distant lineages.
4. Selection. An acquired gene must earn its keep. Genes whose products act alone and are useful in a condition the recipient meets — resistance, toxins, transporters, peripheral metabolism — are retained; genes of the information-processing machinery, whose products must work with many partners, are almost never transferred successfully (the complexity hypothesis, [7.10.27](/7.10.27#sec-27.6.2)). Everything else is deleted, and prokaryotic genomes delete quickly.

The net result is the pattern described in [7.10.27](/7.10.27): a vertically inherited core of information-processing genes, around which an accessory genome of mobile elements, islands and plasmids circulates rapidly between lineages that share a habitat. For microbiology the practical consequences are the ones to keep in view: a bacterial species is a population with a shared gene pool rather than a fixed gene set; the resistance gene found today in a clinical isolate existed yesterday in a soil organism; and a genome sequence describes a strain at a moment, not a species.

## Summary

| Topic | Key points |
|---|---|
| Chromosomes | Usually one circle; exceptions are linear (*Borrelia*, *Streptomyces*, with hairpin or protein-primed ends) and multipartite (*Vibrio cholerae*, a secondary chromosome of plasmid ancestry) |
| Genome size | $0.11$–$16\,\mathrm{Mb}$, about one gene per kb, $85$–$90\,\%$ coding (Property 13.1.1); the smallest belong to endosymbionts, the largest to soil bacteria; $300$–$400$ genes are essential in the laboratory, 473 in JCVI-syn3.0 |
| Organization | Operons and coupled transcription–translation; gene dosage during multifork replication makes map position quantitative (*spo0F*/*kinA*) |
| Accessory genome | **Genomic islands** (Definition 13.1.1) and **pathogenicity islands** (Definition 13.1.2): foreign base composition, tRNA insertion sites, integrase; the **core genome** and the **accessory genome** make up the **pangenome** |
| Plasmids | Definition 13.2.1; F, **R plasmid** (Definition 13.2.2), Col, virulence, degradative, **Ti plasmid**; copy number set by antisense RNA or Rep–iteron feedback; incompatibility = shared replication or partition control (Definition 13.2.3); host range |
| Plasmid maintenance | Partition (ParMRC), **toxin–antitoxin systems** as addiction modules (Definition 13.2.4), and infectious transfer; a costly plasmid persists only if $\gamma F^{*} > D(c + \lambda)$ (Formula 13.2.1, Eq. (13.1)) |
| Mobile elements | **Insertion sequences** and **composite transposons** (Definition 13.3.1); they inactivate genes, rearrange genomes (Hfr formation, the *Bordetella* contrast) and carry resistance |
| Transposon genetics | **Transposon mutagenesis** (Definition 13.3.2) and transposon sequencing (Definition 13.3.3), which measures the fitness contribution of every gene at once |
| Integrons | **Integron** and **gene cassette** (Definition 13.3.4): promoterless cassettes captured at *attI* and expressed from Pc; class 1 integrons in multidrug resistance; *intI* under SOS control |
| ICEs | **Integrative and conjugative elements** (Definition 13.3.5): chromosomal residence plus self-transfer (Tn916, SXT, symbiosis islands); with plasmids and prophages they form the mobilome |
| Mutation | Mutant classes and selection versus screening; $10^{-6}$–$10^{-7}$ per gene, a few $10^{-3}$ per genome per generation; reversion and suppressor tRNAs; mutagens and the **Ames test** (Definition 13.4.1); SOS mutagenesis, mutators, stress-induced mutagenesis — but mutation is still random with respect to usefulness |
| Transformation | **Natural transformation** (Definition 13.5.1): pilus-like uptake machinery, one strand degraded, the other RecA-loaded; fragments of about $8\,\mathrm{kb}$; uptake sequences restrict it to relatives; repair, recombination and nutrition as explanations |
| Transduction | Generalized, specialized and lateral; the largest flux of DNA in the sea; toxins and islands move in phages; **gene transfer agents** are domesticated particles (Definition 13.6.1) |
| Conjugation | Pilus, type IV secretion system, relaxase at *oriT*, rolling-circle transfer; Hfr and F′; mobilizable plasmids; pheromone-induced transfer in *Enterococcus*; T-DNA transfer by *Agrobacterium* |
| Archaea | Transformation and conjugation with distinct machinery; *Haloferax* cell fusion (bidirectional) and UV-induced Ups pili of *Sulfolobus* |
| Barriers | Ecology, restriction–modification and CRISPR, the homology requirement enforced by mismatch repair, and selection; information-processing genes are rarely transferred |

## Questions

1. A conjugative plasmid imposes a $3\,\%$ cost of carriage and is lost by segregation in $1$ in $10^{3}$ divisions. In a chemostat at $D = 0.2\,\mathrm{h^{-1}}$ with $10^{9}$ plasmid-free cells per milliliter, what conjugation rate constant does it need in order to invade? What changes in a biofilm?

   **Answer** By Eq. (13.1), invasion needs $\gamma F^{*} > D(c + \lambda) = 0.2 \times (0.03 + 0.001) = 6.2 \times 10^{-3}\,\mathrm{h^{-1}}$, so $\gamma > 6.2 \times 10^{-12}\,\mathrm{mL\,h^{-1}}$. In a biofilm the local density of recipients and the duration of contact are both much higher, which raises the effective $\gamma F^{*}$ by orders of magnitude; the same plasmid invades there although it cannot in dilute culture.

2. Two plasmids carry resistance to different antibiotics and belong to the same Inc group. A strain is selected with both drugs and grows. Explain, and predict what happens after a few hundred generations without either drug.

   **Answer** Incompatible plasmids share replication or partition control, so no lineage keeps both: selection with both drugs does not prevent loss, it kills the cells that have lost one, so the population consists of cells that are continually segregating and being selected. Without the drugs, each cell rapidly becomes a stable carrier of one plasmid or the other (or of neither, if there is no addiction module); the population splits into two subpopulations rather than retaining both plasmids.

3. A saturated Tn-seq library of a pathogen is grown in rich medium and, in parallel, in a mouse. A gene has abundant insertions and no change in read counts in the medium, but is strongly depleted in the mouse. What does this mean, and what distinguishes such a gene from one with no insertions in either condition?

   **Answer** The gene is dispensable for growth in the medium but contributes to fitness in the host — a candidate virulence or in-host metabolism gene (for example one supplying a nutrient the host restricts). A gene with no insertions anywhere is essential under all conditions tested, so it cannot be scored for a condition-specific role; essentiality is read from the absence of insertions in the initial library, condition-specific fitness from the change in abundance during growth.

4. Why does an integron express a newly captured cassette most strongly, and why is it advantageous that the integrase is part of the LexA regulon?

   **Answer** Cassettes have no promoters; they are transcribed from Pc at the front of the array, and transcription weakens with distance, so the cassette just inserted at *attI* is closest to the promoter and best expressed. Because *intI* is repressed by LexA, capture and reshuffling are switched on by the SOS response, which is triggered by DNA damage — including by quinolones and β-lactams. The cell therefore rearranges its resistance array precisely when it is under the kind of attack that such genes counter.

5. *Haemophilus influenzae* takes up only DNA containing its uptake signal sequence, while *Acinetobacter baylyi* takes up any DNA. What are the consequences for each species, and what does the contrast suggest about what transformation is for?

   **Answer** *H. influenzae* samples mainly DNA of its own species, so transformation serves recombination within the species (new allele combinations and the repair of damaged chromosomes) and brings almost no foreign genes; *A. baylyi* can acquire genes from any organism in its habitat, including resistance genes, but risks taking up DNA that is useless or harmful. The contrast suggests that transformation has no single function: where uptake is selective it looks like a recombination and repair system, where it is indiscriminate the DNA may also serve as nutrition and as an occasional source of new functions.

6. A newly isolated *Klebsiella* strain is resistant to five unrelated antibiotics, and the resistance transfers to *E. coli* in a mating experiment at high frequency. Sequencing shows all five genes within $25\,\mathrm{kb}$ of one another. Explain the arrangement and why it is so common.

   **Answer** The genes are almost certainly nested mobile elements on a conjugative plasmid: cassettes in an integron, the integron in a transposon, the transposon in the plasmid. The nesting arises because each level can capture the one below it, and selection preserves the result: whenever any of the five drugs is used, the whole assembly is selected, so unrelated resistances accumulate on one replicon. Transfer at high frequency identifies the carrier as a self-transmissible plasmid rather than a chromosomal island.
