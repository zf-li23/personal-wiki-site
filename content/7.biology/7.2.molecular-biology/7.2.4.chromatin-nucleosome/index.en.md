---
title: Chromatin and the Nucleosome
description: Histones and the nucleosome core particle (147 bp, 1.65 left-handed turns, the histone fold, linker histone H1); the evidence for the nucleosome (nuclease ladders, beads on a string, cross-linking, crystal structure); higher-order structure (the 30 nm fiber in vitro and its absence in vivo, Hi-C, loop extrusion and topologically associating domains, euchromatin and heterochromatin, the mitotic chromosome); nucleosome positioning and accessibility (nucleosome-free regions, DNase I hypersensitive sites, MNase-seq and ATAC-seq); histone variants and remodelers; quantitative models of compaction, unwrapping under force, site exposure and statistical positioning.
---

A human diploid nucleus holds about $2\,\mathrm{m}$ of DNA in a sphere $6\,\mu\mathrm{m}$ across, and every **base pair** of it must remain available for **replication**, repair and **transcription**. **Eukaryotes** solve this with a protein spool, the nucleosome, on which about $147$ bp of DNA is wrapped; strings of nucleosomes are folded further into loops, domains and, at mitosis, compact chromosomes. This chapter describes that hierarchy from the bottom up and the experiments that revealed each level, and it ends with the quantitative facts that make chromatin a regulatory system rather than mere packaging: how much the DNA is compacted, how much free energy holds it on the octamer, how a transcription factor can reach a wrapped site, and how nucleosomes become positioned without being placed one by one. The topology of the wrapped DNA (each nucleosome takes up about one negative supercoil) was treated in [7.2.3](/7.2.3); the covalent modifications of histones, the remodeling machines and epigenetic silencing, which act on the structures described here, are the subject of [7.2.15](/7.2.15). The methods used throughout (nuclease digestion, Southern blotting, chromatin immunoprecipitation, sequencing) are explained in [7.2.6](/7.2.6).

## 4.1. Histones and the Nucleosome Core Particle

### 4.1.1. Chromatin and Histones

**Definition 4.1.1** The complex of DNA with the proteins (and RNA) that package it in the eukaryotic nucleus is called **chromatin**. By mass it consists of DNA and histones in roughly equal amounts, plus a variable amount of nonhistone proteins and RNA.

**Definition 4.1.2** The small, strongly basic proteins that make up the protein spool of chromatin are called **histones**. All eukaryotes have five major classes: the four *core histones* H2A, H2B, H3, H4 and the linker histone H1.

| Histone | **Residues** (bovine) | $M_{\mathrm{r}}$ | Lys / % | Arg / % | Conservation |
|---|---|---|---|---|---|
| H1 | 223 | 21 130 | 29.5 | 11.3 | low; many tissue-specific subtypes |
| H2A | 129 | 13 960 | 10.9 | 19.3 | moderate; several variants |
| H2B | 125 | 13 774 | 16.0 | 16.4 | moderate |
| H3 | 135 | 15 273 | 19.6 | 13.3 | extreme |
| H4 | 102 | 11 236 | 10.8 | 13.7 | extreme: pea and cow differ at 2 of 102 residues |

The properties of histones follow from their job:

- They are basic: lysine plus arginine make up about a quarter of the residues, so the proteins carry a large positive charge at neutral pH that neutralizes about half of the phosphate charges of the DNA they bind. This is why histones are extracted from chromatin by acid and dissociate at high salt.
- H3 and H4 are among the most conserved proteins known: almost every residue contacts DNA or another histone, so almost every substitution is deleterious.
- The genes are multicopy. The replication-dependent histone genes are clustered and repeated (about 70 genes in humans), have no **introns**, and their mRNAs end in a stem–loop instead of a poly(A) tail; they are expressed in S phase, when the amount of chromatin must double (Example 4.6.2).
- Histones are heterogeneous for two reasons: different gene copies encode slightly different proteins (the variants of Section 4.5), and the proteins are covalently modified after translation (acetylation, methylation, phosphorylation, **ubiquitination**, [7.2.15](/7.2.15)).

Bacteria have no histones. Their chromosome forms a *nucleoid* compacted by **supercoiling** and by abundant nucleoid-associated proteins (HU, IHF, H-NS, Fis) that bend or bridge DNA but bind and dissociate within minutes and form no regular repeating particle. Many archaea, by contrast, have histones homologous to the eukaryotic histone fold; they assemble into continuous "hypernucleosome" superhelices, which suggests that the eukaryotic octamer evolved from such an ancestor.

### 4.1.2. The Core Particle

**Definition 4.1.3** The repeating unit of chromatin is the **nucleosome**: a **nucleosome core particle**, in which $147$ bp of DNA is wrapped in $1.65$ turns of a left-handed superhelix around a **histone octamer** of two copies each of H2A, H2B, H3 and H4, together with the **linker DNA** that joins it to the next core (from a few to about $80$ bp) and, in most cells, one molecule of the linker histone H1. The length of DNA per nucleosome (core plus linker) is the **nucleosome repeat length**; it is about $160$–$240$ bp depending on the species and cell type (about $165$ bp in yeast, about $190$ bp in most human cells).

The word "nucleosome" is often used loosely for the core particle alone; when the distinction matters, we say core particle for the $147$ bp unit.

![The nucleosome. A: the histone fold (three helices joined by two loops, with a disordered N-terminal tail) and the assembly path from H3–H4 and H2A–H2B dimers through the (H3–H4)₂ tetramer to the octamer. B: the core particle viewed down the superhelix axis: 147 bp in 1.65 left-handed turns around the octamer, with entry and exit DNA near the dyad where H1 binds. C: a nucleosome array with its base-pair bookkeeping; micrococcal nuclease cuts the linkers first](./plots/nucleosome-structure.py)

**Definition 4.1.4** The common structural domain of the four core histones, three α-helices (a short $\alpha 1$, a long $\alpha 2$ of about 28 residues and a short $\alpha 3$) connected by two loops $\mathrm{L1}$ and $\mathrm{L2}$, is called the **histone fold**.

Two histone folds pair head to tail in a "handshake", with the long $\alpha 2$ helices crossing, to form the H3–H4 and H2A–H2B heterodimers. Two H3–H4 dimers join through a four-helix bundle between the two H3 molecules to form the $(\mathrm{H3{-}H4})_2$ tetramer, and an H2A–H2B dimer docks on each side through a similar H2B–H4 bundle. The order of assembly is also the order of deposition in vivo: histone **chaperones** load an $(\mathrm{H3{-}H4})_2$ tetramer onto DNA first and then add the two H2A–H2B dimers; disassembly runs in reverse, H2A–H2B leaving first (at about $0.8$–$1\,\mathrm{M}$ NaCl in vitro, the tetramer only above about $1.2\,\mathrm{M}$).

The crystal structure of the core particle (Luger and Richmond, 1997, at $2.8$ Å; later to $1.9$ Å) shows the details of the spool:

- The octamer is a wedge-shaped disc about $11\,\mathrm{nm}$ across and $5.7\,\mathrm{nm}$ thick, with the DNA on the outside. The particle has a two-fold (dyad) axis through the central base pair.
- The DNA contacts the octamer at 14 sites, one per helical turn, wherever its **minor groove** faces the protein; at each site an arginine **side chain** inserts into the minor groove and the backbone phosphates are bound by helix dipoles and main-chain amides. The contacts are with the backbone, not the bases, so the octamer binds any sequence, although some sequences bend more easily than others (Section 4.4).
- The DNA is bent with a radius of about $4.2\,\mathrm{nm}$, much tighter than its persistence length of about $50\,\mathrm{nm}$; the bending energy is paid by the many electrostatic and hydrogen-bond contacts (Section 4.6).
- The eight N-terminal tails (and the C-terminal tail of H2A) are intrinsically disordered and make up about $28\%$ of the mass of the core histones. They leave the particle between the two gyres of DNA and through the minor-groove channels, so they are exposed to modifying enzymes. The H4 tail contacts an acidic patch on the H2A–H2B surface of the neighbouring nucleosome, an interaction that drives the folding of nucleosome arrays; acetylation of H4 K16 abolishes it.

### 4.1.3. The Linker Histone and the Topology of Wrapping

**Definition 4.1.5** Histone H1 and its relatives, which bind at the dyad of a nucleosome to the DNA entering and leaving the core, are called **linker histones**. A core particle together with H1 and about $20$ bp of linker DNA, $167$ bp in all (two full superhelical turns), is called a **chromatosome**.

H1 has a central globular "winged-helix" domain flanked by long basic tails. It is not part of the octamer (one H1 per repeat, against eight core histones): it is removed by $0.5\,\mathrm{M}$ salt or brief trypsin treatment, which leaves the core particles intact and turns condensed chromatin into the "beads on a string" of Example 4.2.2. H1 brings the entering and exiting DNA together into a stem, promotes the folding of nucleosome arrays, and exchanges rapidly in living nuclei (residence times of minutes). It represses transcription in vitro beyond the repression by core histones, and activators can counteract it ([7.2.15](/7.2.15)).

Wrapping has a topological consequence ([7.2.3](/7.2.3)). If a core is assembled on a relaxed closed-circular DNA, the left-handed wrap introduces negative **writhe**; since $\mathrm{Lk}$ cannot change without a strand break, an equal positive supercoil appears in the free DNA. A **topoisomerase** relaxes this compensating supercoil, and when the histones are later removed, the DNA is negatively supercoiled. Counting **topoisomers** after deproteinization of minichromosomes gives $\Delta\mathrm{Lk} \approx -1$ per nucleosome, although the DNA makes $1.65$ left-handed turns (the "**linking number** paradox"): the wrapped DNA is also slightly overtwisted (about $10.2$ bp per turn instead of $10.5$), which partly cancels the writhe. This is why eukaryotic DNA is negatively supercoiled although eukaryotes have no **DNA gyrase**.

## 4.2. The Discovery of the Nucleosome

In the early 1970s chromatin was imagined as DNA coated more or less uniformly with histones. Four independent lines of evidence, collected in under three years, replaced this picture with a repeating particle. The episode is a model of how molecular biology argues: each experiment alone is ambiguous, and their combination is decisive.

**Example 4.2.1 (The nuclease ladder)** Hewish and Burgoyne (1973) found that an endogenous nuclease in isolated rat liver nuclei cut the DNA into fragments that, after deproteinization and gel electrophoresis, formed a ladder of bands at multiples of about $200$ bp. Micrococcal nuclease (MNase) gives the same ladder (Noll, 1974). A ladder means that cleavage is restricted to regularly spaced sites: something protects the DNA between them in a repeating pattern.

**Example 4.2.2 (Beads on a string)** Electron micrographs of chromatin spread at low ionic strength (Olins and Olins, 1974; Woodcock, 1973) showed particles about $10\,\mathrm{nm}$ in diameter connected by thin filaments of DNA. Removing H1 makes the "beads on a string" appearance clearer, so the beads are not H1 complexes; brief MNase digestion releases mononucleosome beads that sediment as a single species.

**Example 4.2.3 (Cross-linking and stoichiometry)** Kornberg and Thomas (1974) found that histones extracted under mild conditions are not monomers: H3 and H4 form an $(\mathrm{H3{-}H4})_2$ tetramer, and H2A and H2B form dimers. Cross-linking chromatin with dimethyl suberimidate (Thomas and Kornberg, 1975) gave covalent products up to, but not beyond, octamers. Stoichiometry then fixes the size of the repeat. An octamer has a mass of about $2 \times (14.0 + 13.8 + 15.3 + 11.2) \approx 109\,\mathrm{kDa}$, and with one H1 the histone mass per repeat is about $130\,\mathrm{kDa}$. Equal masses of DNA and histone therefore mean about $130\,\mathrm{kDa}/(650\,\mathrm{Da\ per\ bp}) \approx 200$ bp of DNA per octamer, the spacing of the nuclease ladder.

**Example 4.2.4 (The core particle)** Prolonged MNase digestion does not end with a 200 bp unit: the linker is trimmed further until a stable particle containing the octamer and about $146$–$147$ bp of DNA remains, with a transient pause at about $167$ bp while H1 is still bound. Neutron scattering, which can distinguish protein from DNA by contrast matching in $\mathrm{H_2O}$/$\mathrm{D_2O}$ mixtures, showed that the DNA lies outside the protein. Crystal structures at $7$ Å (Richmond, Klug and colleagues, 1984) and $2.8$ Å (Luger et al., 1997) confirmed the 1.65-turn left-handed superhelix.

Kornberg's 1974 proposal described the whole repeat: about 200 bp of DNA, an octamer of the four core histones and one H1. Van Holde and colleagues emphasized the roughly 140 bp nuclease-resistant core containing only the octamer, with H1 associated with the linker. Both were right about different objects, and the vocabulary of Definition 4.1.3 (nucleosome, core particle, linker, chromatosome) records the resolution of the debate.

## 4.3. Higher-Order Structure

### 4.3.1. The 10 nm Fiber and the 30 nm Fiber

A string of nucleosomes with the linkers drawn out is the *10 nm fiber*. Wrapping alone shortens the DNA about six- to sevenfold: one repeat of $200$ bp ($68\,\mathrm{nm}$ of **B-DNA**) occupies about $11\,\mathrm{nm}$ of a compact array. The overall compaction of a mitotic chromosome is about $10^4$-fold (Example 4.6.1), so further folding is needed.

When the salt concentration is raised to physiological values or $\mathrm{Mg^{2+}}$ is added, nucleosome arrays in vitro condense into fibers about $30\,\mathrm{nm}$ in diameter, a further five- to sixfold compaction. Two models were long debated:

| | One-start solenoid | Two-start zigzag |
|---|---|---|
| Arrangement | consecutive nucleosomes are neighbours along one helical path, about six per turn; linkers bent | nucleosomes alternate between two stacks; linkers straight and crossing the fiber axis |
| Proposed by | Finch and Klug (1976) | Woodcock; Williams |
| Support | EM of long-repeat arrays with H1, interdigitated solenoid (Robinson et al. 2006) | crystal structure of a tetranucleosome (Schalch et al. 2005), **cryo-EM** of 12-nucleosome arrays (Song et al. 2014) |

The geometry depends on the repeat length and on H1: short repeats (about $167$ bp) favour the two-start zigzag, long repeats with H1 (about $197$ bp) a more compact interdigitated solenoid, and single-molecule force spectroscopy of reconstituted fibers detected both behaviours. It was therefore proposed that inactive chromatin, with long repeats, forms solenoids and active chromatin zigzags.

In living cells, however, a regular 30 nm fiber is generally not found. Cryo-electron microscopy of vitrified sections of mitotic chromosomes (Eltsov et al., 2008), small-angle X-ray scattering of nuclei, and electron tomography of chromatin stained in situ (ChromEMT, Ou et al., 2017) show instead a disordered chain of nucleosomes, with local diameters from about $5$ to $24\,\mathrm{nm}$, packed at different densities in different regions. Regular 30 nm fibers are seen only in a few specialized nuclei with long repeats and little transcription (chicken erythrocytes, some sperm). The older textbook statement that "30 nm fibers account for most of the chromatin of an interphase nucleus" is therefore no longer accepted; the in vitro fiber remains useful as a demonstration of which nucleosome–nucleosome contacts are possible (the H4 tail–acidic patch contact of Section 4.1.2).

### 4.3.2. Loops, Domains and Compartments

Above the level of the nucleosome chain, interphase chromatin is organized by loops and domains, which were discovered not by microscopy but by sequencing-based proximity maps. In chromosome conformation capture and its genome-wide version, Hi-C (Lieberman-Aiden et al., 2009), chromatin is cross-linked with formaldehyde, digested, and the cut ends that lie close together in space are ligated to each other; sequencing the junctions gives a matrix of contact frequencies between all pairs of loci. Three features appear:

1. Compartments: at the scale of megabases, the genome segregates into an A compartment (gene rich, transcribed, early replicating, nuclear interior) and a B compartment (gene poor, silent, late replicating, often at the nuclear lamina or around nucleoli). Loci of the same type contact each other preferentially, even across long distances. On the scale of whole chromosomes, each interphase chromosome occupies its own *chromosome territory*, with little intermingling.
2. Domains: along the diagonal of the contact map, blocks of enriched contacts are separated by sharp boundaries.
3. Loops: point-like peaks of contact join two loci, typically $0.1$–$1$ Mb apart.

**Definition 4.3.1** A genomic region, typically $0.1$–$1$ Mb long, whose loci contact one another more often than they contact loci outside it, with sharp boundaries in Hi-C maps, is called a **topologically associating domain** (TAD).

Most loop anchors and many TAD boundaries are **binding sites** of the zinc-finger protein CTCF, and the two CTCF motifs at the anchors of a loop point toward each other (a "convergent" orientation) in more than $90\%$ of loops (Rao et al., 2014). The orientation rule cannot be explained by diffusion and random collision, which do not distinguish the two directions along the fiber. It is explained by an active process:

**Definition 4.3.2** The process in which a ring-shaped SMC complex (cohesin in interphase, condensin in mitosis) binds chromatin and, using ATP, reels DNA into a progressively growing loop until it is stopped, for cohesin typically by CTCF bound in the orientation that faces the loop, is called **loop extrusion**.

The SMC (structural maintenance of chromosomes) proteins are long antiparallel **coiled coils** with an ATPase head at one end and a hinge at the other; cohesin (SMC1–SMC3 with a kleisin) also holds sister chromatids together after **replication**, and condensin (SMC2–SMC4) compacts mitotic chromosomes. Evidence for loop extrusion:

- Purified yeast condensin and human cohesin extrude DNA loops in single-molecule experiments, at about $0.5$–$2$ kb per second (Ganji et al., 2018; Davidson et al., 2019; Kim et al., 2019). At $1\,\mathrm{kb\,s^{-1}}$ a $200$ kb loop forms in a few minutes, well within the residence time of cohesin on chromatin (about 20 minutes).
- Acute degradation of cohesin erases loops and TADs within hours, while compartments persist or even sharpen (Rao et al., 2017): domains and compartments are made by different mechanisms.
- Inverting a CTCF motif by genome editing abolishes the loop it anchored or creates a new one in the predicted direction (de Wit et al., 2015; Guo et al., 2015).

TADs matter because enhancers act mostly within them ([7.2.14](/7.2.14)). Deletions or inversions that remove a TAD boundary let an enhancer reach a gene in the neighbouring domain; in human families such rearrangements at the *EPHA4* locus misexpress neighbouring genes in the developing limb and cause malformations (Lupiáñez et al., 2015).

**Definition 4.3.3** Chromatin that is relatively decondensed during interphase, stains lightly and contains most of the transcribed genes is called **euchromatin**; chromatin that remains condensed throughout interphase, stains darkly and is largely transcriptionally silent is called **heterochromatin**.

The distinction goes back to cytology (Heitz, 1928). *Constitutive heterochromatin* (pericentromeric satellite repeats, **telomeres**) is heterochromatic in all cells and is marked by H3 K9 trimethylation bound by HP1; *facultative heterochromatin* is condensed only in some cells or at some times, the inactive X chromosome of female mammals being the classic case (H3 K27 trimethylation, the long **noncoding RNA** Xist). Heterochromatin corresponds broadly to the B compartment. How the marks are written, read and spread is the subject of [7.2.15](/7.2.15).

### 4.3.3. The Mitotic Chromosome

At mitosis, chromatin is compacted a further tenfold into the familiar rod-shaped chromatids. When histones are extracted from metaphase chromosomes, the DNA spreads out as a halo of loops anchored to a proteinaceous "scaffold" rich in topoisomerase II and condensin (Paulson and Laemmli, 1977). This *radial loop model*, with loops of a few tens of kilobases (about $20$–$100$ kb), has been refined by Hi-C of synchronized cells (Gibcus et al., 2018): condensin II first forms large loops (about $400$ kb) arranged around a helical central axis, and condensin I then nests smaller loops (about $80$ kb) within them. The "scaffold" is thus the line of condensin complexes at the loop bases, not a preexisting structure. The negative supercoiling of loops observed after histone removal, and its relaxation by nicking, is the topological signature of the nucleosomes that had occupied them ([7.2.3](/7.2.3)).

## 4.4. Nucleosome Positioning and Accessibility

**Definition 4.4.1** The nonrandom placement of nucleosomes on DNA is called **nucleosome positioning**. It has two components: *translational* positioning (which stretch of DNA a core covers) and *rotational* positioning (which face of the double helix points toward the octamer).

Positioning matters because a factor whose site lies inside a core particle binds poorly (Section 4.6), while a site in a linker or in a nucleosome-free region is freely accessible. Its main determinants are:

1. *DNA sequence.* Wrapping compresses the minor groove where it faces the octamer and widens it where it faces outward. AA, TT and TA dinucleotides favour a narrow minor groove, GC dinucleotides a wide one; sequences in which these dinucleotides alternate with a period of about $10$ bp, offset by half a turn, bend easily and are preferred (the basis of the "Widom 601" sequence used in reconstitutions). Long poly(dA:dT) tracts are stiff and disfavour nucleosomes; they are enriched in yeast promoters.
2. *Barriers.* DNA-binding proteins and other bound complexes exclude nucleosomes from their sites and, by excluded volume, order the nucleosomes next to them (statistical positioning, Example 4.6.4).
3. *ATP-dependent remodelers* slide, space and evict nucleosomes (Section 4.5, [7.2.15](/7.2.15)).

Genome-wide maps show a stereotyped promoter architecture: a nucleosome-depleted region of about $150$ bp just upstream of the transcription start site, flanked by a strongly positioned "$-1$" and "$+1$" nucleosome, with a regular array of decreasingly well positioned nucleosomes downstream in the gene body. Many core promoter elements and activator sites lie in the depleted region.

**Example 4.4.1 (The SV40 control region is nucleosome-free)** The DNA of simian virus 40 (5.2 kb) exists in infected cells as a minichromosome of about 20 nucleosomes. Electron micrographs of minichromosomes showed a nucleosome-free gap of about $400$ bp in a fraction of them, and restriction enzymes with sites in the late control region (the origin of replication, the 72 bp enhancer repeats and the GC boxes) cut minichromosomes there readily, while sites elsewhere were protected. The regulatory region of an active gene is therefore exposed, and this exposure can be measured by nuclease accessibility.

**Definition 4.4.2** A short region of chromatin, typically $100$–$300$ bp, that is cut by DNase I at concentrations 10–100 times lower than those needed to digest bulk chromatin is called a **DNase I hypersensitive site**.

Hypersensitive sites mark active or poised regulatory DNA: promoters, enhancers, insulators and locus control regions. They are tissue specific (the sites upstream of the β-globin genes are present in erythroid cells and absent in others) and often appear before the gene is transcribed. Part of the hypersensitivity is due to the absence of a nucleosome; the rest to the distortion of DNA by bound factors. Hypersensitive sites are mapped by *indirect end-labeling*: nuclei are treated lightly with DNase I, the purified DNA is cut with a restriction enzyme, and a Southern blot ([7.2.6](/7.2.6)) is probed with a short fragment abutting one restriction site; each hypersensitive site produces a band whose length gives its distance from that site.

Three sequencing assays now map nucleosomes and accessibility genome-wide; their interpretation is complementary:

| Assay | Principle | What the reads report |
|---|---|---|
| MNase-seq | MNase digests linkers; the protected 147 bp fragments are sequenced | positions (dyads) and occupancy of nucleosomes |
| DNase-seq | ends of DNase I cuts in lightly digested nuclei are sequenced | hypersensitive sites; footprints of bound factors within them |
| ATAC-seq | Tn5 transposase loaded with sequencing adapters inserts into accessible DNA ("tagmentation") | accessible regions; fragment lengths reveal nucleosome-free (below 100 bp), mono- (about 200 bp) and dinucleosomal (about 400 bp) fragments |

ATAC-seq (Assay for Transposase-Accessible Chromatin with sequencing, Buenrostro et al., 2013) has become the standard because the transposase cuts and adds adapters in one step, so a library can be made from a few thousand cells, or a single cell. It turns a property of chromatin structure, accessibility, into a quantity that can be compared between cell types; the analysis of such data belongs to [7.8](/7.8).

## 4.5. Histone Variants and Chromatin Remodeling: An Overview

The canonical histones are made in S phase and deposited behind the replication fork. Variant histones, encoded by separate, usually single-copy genes with introns and polyadenylated mRNAs, are made throughout the cell cycle and placed at particular loci by dedicated chaperones:

| Variant | Replaces | Location and role | Deposited by |
|---|---|---|---|
| H3.3 | H3.1/H3.2 (differs at 4–5 residues) | transcribed genes, enhancers; replication-independent replacement; telomeres and pericentromeres | HIRA (genes); DAXX–ATRX (repeats) |
| CENP-A | H3 | **centromeres**; marks the site of kinetochore assembly epigenetically, independent of sequence | HJURP |
| H2A.Z | H2A | the $-1$ and $+1$ nucleosomes flanking promoters; poises genes for activation | SWR1 (yeast), SRCAP, p400 |
| H2A.X | H2A | throughout; phosphorylated at Ser139 ($\gamma$H2A.X) over megabases around a double-strand break, recruiting repair factors ([7.2.8](/7.2.8)) | general |
| macroH2A | H2A | inactive X chromosome; repression | — |

Deposition is the work of histone chaperones, acidic proteins that shield the positive charge of histones and hand them to DNA: CAF-1 binds the replication sliding clamp PCNA and deposits new H3–H4 behind the fork, ASF1 passes H3–H4 dimers to CAF-1 or HIRA, and FACT disassembles and reassembles nucleosomes in front of and behind elongating RNA polymerase II. Parental H3–H4 tetramers are recycled at the fork and distributed between the two daughter duplexes, so each daughter inherits about half of the old, modified histones, a point central to the inheritance of chromatin states ([7.2.15](/7.2.15)).

Nucleosomes are not static. ATP-dependent chromatin remodelers, all with an ATPase of the SF2 helicase superfamily that translocates on nucleosomal DNA about two helical turns from the dyad, slide nucleosomes along DNA, evict them, or exchange histone dimers. There are four families: SWI/SNF (eviction and sliding, recruited by activators), ISWI and CHD (spacing of regular arrays, establishing the repeat length) and INO80/SWR1 (exchange of H2A.Z). Their mechanisms and their place in gene activation are treated in [7.2.15](/7.2.15).

## 4.6. A Quantitative View of Chromatin

**Example 4.6.1 (The compaction cascade)** Human chromosome 22 contains about $48 \times 10^6$ bp (the round number used in the course; the current assembly gives about $51$ Mbp). As B-DNA ($0.34\,\mathrm{nm}$ per bp) its contour length is
$$
48 \times 10^6 \times 0.34\,\mathrm{nm} \approx 1.63\,\mathrm{cm},
$$
whereas the metaphase chromatid is about $2\,\mu\mathrm{m}$ long, a compaction of about $8000$-fold. The diploid genome, $6.2 \times 10^9$ bp, is $2.1\,\mathrm{m}$ of DNA. Treating B-DNA as a cylinder of radius $1\,\mathrm{nm}$, its volume is
$$
6.2 \times 10^9 \times \pi (1\,\mathrm{nm})^2 \times 0.34\,\mathrm{nm} \approx 6.6\,\mu\mathrm{m}^3,
$$
about $6\%$ of a nucleus $6\,\mu\mathrm{m}$ in diameter ($113\,\mu\mathrm{m}^3$). Packing is thus not a problem of space but of order: the DNA must be folded so that it does not tangle, can be segregated at mitosis, and keeps the right regions accessible.

![Compaction of chromosome 22. A: contour length at successive levels of packing (log scale), with the fold compaction relative to B-DNA; the 30 nm fiber is drawn hollow because it is an in vitro structure. B: the diploid genome as B-DNA occupies only about 6% of the nuclear volume](./plots/compaction-cascade.py)

**Example 4.6.2 (How many nucleosomes?)** With a repeat of about $200$ bp, a diploid human cell contains
$$
\frac{6.2 \times 10^9\ \mathrm{bp}}{200\ \mathrm{bp}} \approx 3 \times 10^7
$$
nucleosomes. Their histone mass, $3.1 \times 10^7 \times 109\,\mathrm{kDa}/N_{\mathrm{A}} \approx 5.6\,\mathrm{pg}$, matches the DNA mass, $6.2 \times 10^9 \times 650\,\mathrm{Da}/N_{\mathrm{A}} \approx 6.7\,\mathrm{pg}$, as Example 4.2.3 requires. In an S phase of about $8$ hours the cell must make the core histones for half of these octamers (the other half are recycled), about $1.2 \times 10^8$ histone molecules, or some $4000$ per second. This demand explains the many copies of the replication-dependent histone genes, their coupling to DNA synthesis, and their short, unspliced, rapidly processed mRNAs.

How tightly is DNA held on the octamer? Single-molecule force spectroscopy answers this directly. A single nucleosome tethered between a surface and a bead in an optical trap is pulled with force $F$; when the outer part of the wrapped DNA comes off, the tether lengthens by $\Delta z$. Treat the nucleosome as a two-state system, closed and open, with free-energy difference $\Delta G = G_{\mathrm{open}} - G_{\mathrm{closed}} > 0$ at zero force. The force does work $F\Delta z$ on opening, so the free-energy difference becomes $\Delta G - F\Delta z$, and the **Boltzmann distribution** gives the following.

**Formula 4.6.1 (Two-state opening under force)**
$$
P_{\mathrm{open}}(F) = \frac{1}{1 + \exp\!\left[(\Delta G - F\Delta z)/k_{\mathrm{B}}T\right]}, \qquad F_{1/2} = \frac{\Delta G}{\Delta z}. \tag{4.1}
$$

The midpoint $F_{1/2}$ gives the ratio of $\Delta G$ to $\Delta z$, and the steepness of the transition gives $\Delta z$ itself: the slope at the midpoint is $\Delta z/(4k_{\mathrm{B}}T)$, so the transition is $4k_{\mathrm{B}}T/\Delta z$ wide in force. Fitting Eq. (4.1) to $P_{\mathrm{open}}(F)$ therefore yields both parameters and hence $\Delta G = F_{1/2}\Delta z$.

**Example 4.6.3 (Unwrapping energy)** In the experiment analysed in the course (after Mihardja et al., 2006), the transition is centred at $F_{1/2} \approx 3\,\mathrm{pN}$ with $\Delta z \approx 40\,\mathrm{nm}$. Then
$$
\Delta G \approx 3\,\mathrm{pN} \times 40\,\mathrm{nm} = 120\,\mathrm{pN\,nm} \approx 30\,k_{\mathrm{B}}T,
$$
using $k_{\mathrm{B}}T \approx 4.1\,\mathrm{pN\,nm}$ at room temperature. The transition width $4k_{\mathrm{B}}T/\Delta z \approx 0.4\,\mathrm{pN}$ is narrow, so the force must be resolved finely around $F_{1/2}$ to fit $\Delta z$; with a realistic number of observations the fitted $\Delta z$ and hence $\Delta G$ are uncertain by tens of percent (figure, panel A).

![Two-state models of nucleosome opening. A: fraction of time a nucleosome is open against pulling force; simulated optical-trap data (dots, true ΔG = 30 kBT, Δz = 40 nm) fitted with Eq. (4.1); the fit returns F1/2 ≈ 3.1 pN and Δz ≈ 34 nm, i.e. ΔG ≈ 25 kBT, illustrating the uncertainty of Δz. B: site exposure: occupancy of a factor site with KD = 1 nM on naked DNA and inside a nucleosome where the site is exposed with equilibrium constant Kconf = 10⁻² (near the entry) or 10⁻⁴ (near the dyad)](./plots/nucleosome-unwrapping.py)

**Remark 4.6.1** Thirty $k_{\mathrm{B}}T$ for unwrapping most of the DNA corresponds to roughly $2$–$3\,k_{\mathrm{B}}T$ per $10$ bp contact. It is the *net* free energy: the adsorption energy of the contacts is much larger, but most of it is spent on bending the DNA to a $4\,\mathrm{nm}$ radius. Finer experiments show that unwrapping proceeds in stages: the outer turn comes off reversibly at a few piconewtons, the inner turn abruptly at higher forces, and the detailed values depend on the sequence and the salt concentration. A force of a few piconewtons is within the range generated by RNA polymerase and remodelers, which is why these motors can displace nucleosomes.

Because the net binding per contact is only a few $k_{\mathrm{B}}T$, wrapped DNA is not permanently hidden: it unwraps transiently from the ends. Polach and Widom (1995) measured the equilibrium constant $K_{\mathrm{conf}}$ for spontaneous exposure of a restriction site inside a nucleosome: about $10^{-2}$ to $10^{-3}$ for sites near the entry, falling to $10^{-4}$–$10^{-5}$ near the dyad. Fluorescence measurements show that the ends of the DNA stay wrapped for about $250\,\mathrm{ms}$ and unwrap for $10$–$50\,\mathrm{ms}$ (Li et al., 2005). If a factor can bind its site only in the exposed state, with **dissociation constant** $K_D$ for naked DNA, the fraction of sites bound at factor concentration $[\mathrm{TF}]$ is
$$
\theta = \frac{K_{\mathrm{conf}}[\mathrm{TF}]/K_D}{1 + K_{\mathrm{conf}} + K_{\mathrm{conf}}[\mathrm{TF}]/K_D}
= \frac{[\mathrm{TF}]}{[\mathrm{TF}] + K_D^{\mathrm{app}}}, \qquad K_D^{\mathrm{app}} = K_D\,\frac{1 + K_{\mathrm{conf}}}{K_{\mathrm{conf}}} \approx \frac{K_D}{K_{\mathrm{conf}}}.
$$
A nucleosome thus raises the apparent dissociation constant by $1/K_{\mathrm{conf}}$, $10^2$- to $10^5$-fold depending on the position of the site, without making it unreachable. It also couples factors: once one factor holds the DNA unwrapped, a second factor binding further in pays a smaller unwrapping cost, so two factors whose sites lie in the same nucleosome bind cooperatively without touching each other (nucleosome-mediated **cooperativity**). This is one physical basis of the combinatorial control of enhancers ([7.2.14](/7.2.14), [7.2.22](/7.2.22)).

Finally, positioning does not require every nucleosome to be placed by sequence or by a remodeler. Kornberg and Stryer (1988) pointed out that a barrier is enough.

**Example 4.6.4 (Statistical positioning)** Model nucleosomes as hard rods of $w = 147$ bp on a one-base-pair lattice, with no sequence preference, at a density fixed by a fugacity $z$, and let a bound factor block the left end. The grand **partition function** $Z(i)$ of a segment of $i$ base pairs satisfies
$$
Z(i) = Z(i-1) + z\,Z(i - w), \qquad Z(i) = 1 \ (0 \le i < w),
$$
since the last base pair is either free or the end of a nucleosome. The probability that a nucleosome occupies positions $s+1, \dots, s+w$ of a segment of length $L$ is then $z\,Z(s)\,Z(L - s - w)/Z(L)$, computed for all $s$ by one forward and one backward recursion (**dynamic programming**, linear in $L$). The result (figure) is a nucleosome firmly placed against the barrier, the "$+1$ nucleosome", followed by peaks spaced by the repeat length whose order decays over a few nucleosomes, more slowly when the packing is denser. Excluded volume alone, the same physics that gives the oscillating density of a liquid near a wall, generates the phased arrays seen downstream of promoters; remodelers of the ISWI and CHD families then sharpen the arrays and set the spacing.

![Statistical positioning computed with the hard-rod lattice model. Density of nucleosome dyads against distance from a barrier for two packing densities (mean linker about 39 bp and 23 bp), blurred by 15 bp as in nucleosome maps: the first nucleosome is positioned by the barrier, and the phasing of the following ones decays with distance, faster at lower density](./plots/statistical-positioning.py)

## Summary

| Level | Size | Key facts |
|---|---|---|
| Histones | 102–223 residues | five classes; Lys + Arg ≈ 1/4 of residues; H3, H4 extremely conserved; multicopy replication-dependent genes (Definition 4.1.2) |
| Core particle | 147 bp, 1.65 left-handed turns, 11 nm × 5.7 nm | octamer $(\mathrm{H3{-}H4})_2 + 2(\mathrm{H2A{-}H2B})$; histone fold handshake (Definition 4.1.4); 14 minor-groove contacts; disordered tails 28% of mass; $\Delta\mathrm{Lk} \approx -1$ per nucleosome |
| Nucleosome, chromatosome | repeat 160–240 bp; 167 bp with H1 | H1 at the dyad, not in the octamer, removed by 0.5 M salt (Definitions 4.1.3, 4.1.5) |
| Evidence | — | nuclease ladder, beads on a string, cross-linking to octamers, mass balance (200 bp per octamer), core particle and crystal structure (Examples 4.2.1–4.2.4) |
| 10 nm and 30 nm fibers | 6–7× and about 40× | 30 nm fiber forms in vitro (solenoid or zigzag); in vivo chromatin is a disordered 5–24 nm chain |
| Loops, TADs, compartments | 0.1–1 Mb; Mb | Hi-C; convergent CTCF sites; cohesin loop extrusion at about 1 kb/s (Definitions 4.3.1, 4.3.2); A/B compartments; euchromatin and heterochromatin (Definition 4.3.3) |
| Mitotic chromosome | about $10^4$× | nested condensin loops around a helical axis (replacing the scaffold–radial loop picture) |
| Positioning and access | NDR about 150 bp; ±1 nucleosomes | sequence, barriers, remodelers (Definition 4.4.1); DNase I hypersensitive sites (Definition 4.4.2); MNase-seq, DNase-seq, ATAC-seq |
| Variants and remodelers | — | H3.3, CENP-A, H2A.Z, H2A.X, macroH2A; chaperones CAF-1, HIRA, ASF1, FACT; SWI/SNF, ISWI, CHD, INO80 |
| Quantities | — | chr22: 1.63 cm → 2 µm (8000×); $3 \times 10^7$ nucleosomes per cell; DNA fills 6% of the nucleus; $P_{\mathrm{open}}$ from Eq. (4.1), $\Delta G = F_{1/2}\Delta z \approx 30\,k_{\mathrm{B}}T$; $K_D^{\mathrm{app}} \approx K_D/K_{\mathrm{conf}}$; statistical positioning (Example 4.6.4) |

## Questions

1. Histone H4 of peas and cows differs at only 2 of 102 positions, whereas H1 varies considerably between species. Explain this difference in terms of structure.

   **Answer** Almost every residue of H4 lies in the histone fold or in the tail and contacts DNA, H3 (in the four-helix bundle and the handshake), H2B or the neighbouring nucleosome; a substitution almost anywhere disturbs one of these interactions in every nucleosome of the genome, and is selected against. H1 binds the outside of the nucleosome at the dyad through a single globular domain; its long basic tails act mainly through their overall positive charge, which tolerates substitutions, and the protein is in any case less essential (several H1 subtypes are partly redundant).
2. Chromatin is digested briefly with micrococcal nuclease, deproteinized and run on an agarose gel. Describe the result, and the result of digestion to completion. What does each tell you?

   **Answer** Brief digestion gives a ladder of DNA bands at multiples of the repeat length (about 200, 400, 600 bp …): cuts are confined to the linkers, so the DNA between them is protected by a regularly repeating particle, and the spacing gives the repeat length. Extensive digestion trims the linkers away and leaves a single band of about 147 bp (with a transient 167 bp intermediate while H1 is bound): this is the DNA protected by the octamer, the core particle.
3. A relaxed circular plasmid is assembled into chromatin with 20 nucleosomes in the presence of topoisomerase I, and the histones are then removed. What is the linking number difference of the plasmid? What would it be if no topoisomerase had been present?

   **Answer** Each nucleosome constrains about one negative supercoil; the topoisomerase relaxes the compensating positive supercoils in the free DNA, so after the histones are removed the plasmid has $\Delta\mathrm{Lk} \approx -20$ and is negatively supercoiled. Without topoisomerase no strand can pass, $\mathrm{Lk}$ is unchanged and $\Delta\mathrm{Lk} = 0$: the negative writhe in the nucleosomes is exactly compensated by positive supercoiling of the free DNA, which in turn resists assembly (topoisomerases are required for efficient assembly in vitro).
4. In Hi-C maps, why is the convergent orientation of CTCF sites at loop anchors strong evidence for loop extrusion rather than for random collisions of the two sites?

   **Answer** If two CTCF-bound sites met by diffusion and stuck together, the orientation of the motifs, which only defines a direction along the DNA, could not influence which pairs meet: all four orientation combinations would be equally common. A complex that translocates along the fiber, enlarging a loop until it meets a CTCF molecule facing it, detects direction, and predicts that the stopping sites at the two ends of a loop face each other; inverting one motif should then abolish the loop, as observed.
5. A transcription factor binds its site on naked DNA with $K_D = 1\,\mathrm{nM}$ and is present at $10\,\mathrm{nM}$. What fraction of its sites is bound on naked DNA, at a site near the nucleosome entry ($K_{\mathrm{conf}} = 10^{-2}$) and at a site near the dyad ($K_{\mathrm{conf}} = 10^{-4}$)? What does the factor need in order to bind the dyad site?

   **Answer** Naked DNA: $\theta = 10/(10 + 1) \approx 0.91$. Entry site: $K_D^{\mathrm{app}} \approx 1\,\mathrm{nM}/10^{-2} = 100\,\mathrm{nM}$, $\theta = 10/110 \approx 0.09$. Dyad site: $K_D^{\mathrm{app}} \approx 10\,\mu\mathrm{M}$, $\theta \approx 10^{-3}$. To bind near the dyad the factor needs either a much higher concentration, help from another factor that keeps the DNA unwrapped (cooperativity through the nucleosome), or a remodeler that slides or evicts the nucleosome; "pioneer" factors that bind nucleosomal DNA directly are an exception.
6. In a nucleosome-pulling experiment the transition is centred at $3\,\mathrm{pN}$ and its 10%–90% width is $0.9\,\mathrm{pN}$. Estimate $\Delta z$ and $\Delta G$ from Eq. (4.1).

   **Answer** From Eq. (4.1), $P = 0.1$ and $P = 0.9$ occur at $(F - F_{1/2})\Delta z/k_{\mathrm{B}}T = \mp\ln 9$, so the width is $2\ln 9\,k_{\mathrm{B}}T/\Delta z = 4.39\,k_{\mathrm{B}}T/\Delta z$. With a width of $0.9\,\mathrm{pN}$ and $k_{\mathrm{B}}T = 4.1\,\mathrm{pN\,nm}$, $\Delta z \approx 4.39 \times 4.1/0.9 \approx 20\,\mathrm{nm}$, and $\Delta G = F_{1/2}\Delta z \approx 60\,\mathrm{pN\,nm} \approx 15\,k_{\mathrm{B}}T$.
7. Explain why the hard-rod model of Example 4.6.4 produces a regular array next to a barrier but a uniform average density far from it, and why the phasing persists further at higher nucleosome density.

   **Answer** Next to the barrier the first nucleosome can only lie in a narrow range of positions (it cannot overlap the barrier, and the free gap before it costs entropy only if it is large), so its position is well defined; each following nucleosome must lie at least 147 bp beyond the previous one, so the positions are defined relative to the first, but the uncertainty of the linker lengths accumulates like a random walk and the peaks broaden and merge after a few nucleosomes. Far away, translational invariance gives a uniform density. At higher density the linkers are shorter and less variable (the rods are nearly jammed), so the accumulated uncertainty grows more slowly and the oscillation decays over more nucleosomes.
