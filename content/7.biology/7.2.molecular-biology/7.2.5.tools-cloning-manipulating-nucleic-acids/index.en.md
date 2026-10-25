---
title: "Tools I: Cloning and Manipulating Nucleic Acids"
description: Restriction endonucleases and restriction–modification systems (nomenclature, site frequency, sticky and blunt ends, isoschizomers, Dam and Dcm methylation); type IIS enzymes and overhangs of arbitrary sequence; the chemistry of DNA ligase; cloning vectors (plasmids, blue–white screening, directional cloning, expression vectors, λ, cosmids, BACs, YACs); genomic and cDNA libraries, the Clarke–Carbon formula and hybridization stringency; the polymerase chain reaction (the bookkeeping of the first cycles, the primer-limited plateau, fidelity); DNA polymerase activities as a toolbox, nick translation, terminal transferase and overlap-based assembly.
---

Molecular biology became an experimental science of individual genes when, in the early 1970s, it acquired a few enzymes that cut, join and copy DNA at defined places. A restriction endonuclease cuts a genome at a chosen sequence, DNA ligase joins fragments to a small replicon, and a bacterium copies the recombinant molecule a billionfold, so that one gene out of a genome of $10^9$ bp can be obtained in pure form; since the 1980s the polymerase chain reaction achieves the same isolation in a test tube. This chapter explains the tools by their logic, what each enzyme does chemically, why each element of a vector is there, and how many molecules, clones or cycles a method needs, rather than as procedures. Almost every tool is borrowed from nature, restriction enzymes from bacterial immunity, polymerases from replication, vectors from plasmids and phages, a theme that returns with genome editing in [7.2.24](/7.2.24). The companion chapter [7.2.6](/7.2.6) applies these tools to measurement; the separation methods they rely on (gel **electrophoresis**, chromatography) are treated in [6.4.14](/6.4.14), and the chemistry of nucleotides and of the **phosphodiester bond** in [6.5.33](/6.5.33).

## 5.1. Restriction Endonucleases and Host Modification

### 5.1.1. Restriction and Modification

In the 1950s Luria, Bertani and Weigle noticed that a phage grown on one strain of *Escherichia coli* infected a second strain poorly, but that the rare survivors then grew well on the second strain: the host "restricted" foreign phage DNA and "modified" the DNA that escaped. Arber showed that restriction is cleavage of unmodified DNA by an endonuclease and modification is methylation of the same sequence; Smith purified the first sequence-specific enzyme (1970), and Nathans used such enzymes to map the SV40 genome (Nobel Prize 1978).

**Definition 5.1.1** An endonuclease that recognizes a specific short DNA sequence and cleaves both strands at or near it is called a **restriction endonuclease**. Together with a methyltransferase that methylates the same sequence and thereby blocks cleavage, it forms a **restriction–modification system**.

The system is a primitive immune system: the host's sites are methylated and protected, while an infecting genome is cut before it can replicate. Four types are distinguished.

| Type | Subunits and cofactors | Cleavage position | Example | Laboratory use |
|---|---|---|---|---|
| I | one multisubunit enzyme (restriction, modification, specificity), ATP | random, up to kilobases away, after translocation | EcoKI | none |
| II | separate endonuclease (usually a homodimer) and methylase, $\mathrm{Mg^{2+}}$ | in or next to the site, at a fixed position | EcoRI, HindIII, BamHI | the workhorses of cloning |
| III | two-subunit enzyme, ATP | 25–27 bp from the site | EcoP15I | rare |
| IV | cleaves *methylated* DNA | near the methylated site | McrBC, Mrr | absent from hosts used for methylated DNA |

More than 300 type II specificities are known. Names take the first letter of the genus and the first two of the species, a strain designation if needed, and a Roman numeral for the order of discovery: HindIII is the third enzyme of *Haemophilus influenzae* strain Rd.

### 5.1.2. Site Frequency

Most type II enzymes recognize palindromes of 4 to 8 bp, sequences reading the same 5′→3′ on both strands (GAATTC for EcoRI). The palindrome matches the two-fold symmetry of the homodimer, each subunit reading one half-site and cleaving one strand. Hydrolysis leaves a 5′-phosphate and a 3′-OH at every new end, the pair of groups that DNA ligase joins (Section 5.3).

**Formula 5.1.1 (Site frequency)** In a random sequence with equal base frequencies, a site of $n$ specified base pairs occurs on average once in
$$
4^n\ \mathrm{bp}: \qquad 256\ (n = 4), \quad 4096\ (n = 6), \quad 65\,536\ (n = 8). \tag{5.1}
$$

Four-cutters therefore give fragments of a few hundred base pairs, six-cutters a few kilobases, eight-cutters tens of kilobases. NotI ($\mathrm{GCGGCCGC}$) cuts mammalian DNA still more rarely than Eq. (5.1) predicts, about once per megabase, because its site contains two CpG dinucleotides, which are depleted several-fold in mammalian genomes by deamination of methylated cytosine ([7.2.15](/7.2.15)): real frequencies are set by dinucleotide statistics, not by base composition.

### 5.1.3. Sticky and Blunt Ends

**Definition 5.1.2** Ends with a short single-stranded extension, produced by cuts staggered about the centre of the site, are called **sticky ends**; the extension is a 5′ overhang (EcoRI) or a 3′ overhang (PstI). Ends produced by cuts directly opposite each other are called **blunt ends** (SmaI, EcoRV).

Two sticky ends with complementary overhangs can pair whatever enzyme made them. BamHI, BglII and Sau3AI all leave the overhang GATC, so their fragments can be joined; the hybrid junction is cut by neither BamHI nor BglII, which is a way of destroying a site deliberately. Blunt ends pair with any other blunt end, which is general but inefficient (Section 5.3).

![Cleavage geometry of type II restriction enzymes. Each row shows the recognition site (boxed) in its duplex, the cut through both strands (red) and the two products, with overhang bases coloured. EcoRI leaves 5′ overhangs, PstI 3′ overhangs and SmaI blunt ends; the type IIS enzyme BsaI cuts outside its asymmetric site, so its four-nucleotide overhang can have any sequence and the recognition site stays on the discarded fragment](./plots/restriction-ends.py)

**Definition 5.1.3** Enzymes from different sources that recognize the same sequence are called **isoschizomers**; isoschizomers that cleave that sequence at different positions are called **neoschizomers**.

SphI and BbuI are isoschizomers; SmaI ($\mathrm{CCC^\wedge GGG}$, blunt) and XmaI ($\mathrm{C^\wedge CCGGG}$, sticky) are neoschizomers. Isoschizomers often differ in their sensitivity to methylation, which turns them into probes of it: of the pair HpaII and MspI, which share the site CCGG, only MspI cuts when the internal cytosine is methylated, so comparing the two digests reveals methylation ([7.2.15](/7.2.15)).

### 5.1.4. Methylation in Cloning Hosts

Three methylases of laboratory *E. coli* strains matter for cloning.

| Methylase | Site (methylated base) | Cellular role | Consequence |
|---|---|---|---|
| Dam | $\mathrm{G\underline{A}TC}$ ($N^6$-methyladenine) | strand discrimination in mismatch repair, replication timing ([7.2.7](/7.2.7), [7.2.8](/7.2.8)) | blocks MboI and enzymes whose site overlaps GATC; DpnI cuts *only* the methylated site |
| Dcm | $\mathrm{C\underline{C}WGG}$ (5-methylcytosine) | unclear | blocks several enzymes with overlapping sites |
| EcoKI | type I system | restriction of foreign DNA | cloning hosts are restriction-deficient, so that unmethylated DNA survives |

DpnI shows how a methylation state becomes a tool. A plasmid grown in a $dam^+$ host is methylated whereas DNA newly made in vitro is not, so a DpnI digest removes the original template from a reaction and leaves only the newly synthesized molecules, the basis of plasmid-wide mutagenesis (Section 5.6.4).

## 5.2. Type IIS Enzymes and Overhangs of Arbitrary Sequence

A palindromic site fixes the overhang: every EcoRI end carries AATT. A second class of enzymes lets the experimenter choose it.

**Definition 5.2.1** Type II enzymes that recognize an asymmetric sequence and cleave at a fixed distance outside it are called **type IIS restriction enzymes**; the distances on the two strands are written after the site, as in BsaI $\mathrm{GGTCTC}(1/5)$ or FokI $\mathrm{GGATG}(9/13)$.

Because the overhang lies outside the recognition sequence, it may be any of $4^4 = 256$ four-base sequences, and a single enzyme can be made to produce ends compatible with EcoRI, BamHI or HindIII. Two consequences follow. The recognition site is not part of the product, so a joined product cannot be cut again; and a set of distinct, mutually incompatible overhangs fixes the order in which many fragments are joined. Assembly methods built on this idea join tens of fragments in a defined order in one reaction, because incorrectly rejoined starting molecules are cut again while the correct product, having lost its sites, accumulates. The same enzyme class contributed to genome editing: the cleavage domain of FokI, which is separate from its DNA-recognition domain, became the nuclease of zinc-finger nucleases and TALENs ([7.2.24](/7.2.24)).

## 5.3. DNA Ligase

**Definition 5.3.1** An enzyme that forms a phosphodiester bond between a 5′-phosphate and an adjacent 3′-OH at a nick in a double-stranded nucleic acid is called **DNA ligase**.

Forming the bond costs energy, taken from ATP (phage T4 and eukaryotic ligases) or $\mathrm{NAD^+}$ (the *E. coli* enzyme), in three steps whose logic is the activation of the phosphate as a leaving group:

1. AMP is transferred to an active-site lysine, giving a covalent enzyme–AMP intermediate.
2. The AMP is passed to the 5′-phosphate of the nick, giving an adenylated DNA (a phosphoanhydride).
3. The 3′-OH attacks that activated phosphate, forming the phosphodiester and releasing AMP.

Ligation is thus not the chemical reverse of cleavage: hydrolysis of a phosphodiester is downhill, and its synthesis must be coupled to the cleavage of phosphoanhydride bonds. T4 DNA ligase seals nicks, joins annealed cohesive ends (two nicks sealed while the short overhangs are transiently paired, which is why such reactions are run cold), and joins blunt ends, which must collide end to end and react one to two orders of magnitude less efficiently. It requires a 5′-phosphate and cannot fill a gap. Both limitations are useful: removing the phosphates of a cut vector with a phosphatase prevents it from closing on itself, while the insert, which keeps its phosphates, is still joined on one strand at each end and the remaining nicks are repaired in the host.

Whether the two ends of one molecule join (circularization) or ends of different molecules join is a question of concentration. The effective concentration of one end of a molecule in the neighbourhood of its other end is fixed by the length and stiffness of the DNA and does not depend on how much DNA is present, whereas intermolecular joining is proportional to the concentration of partner ends. Dilute reactions therefore favour circles, concentrated ones long concatemers.

## 5.4. Vectors

**Definition 5.4.1** A DNA molecule that replicates autonomously in a host cell and can carry inserted foreign DNA is called a **cloning vector**. Every vector has an origin of replication, a selectable marker and one or more cloning sites.

A foreign fragment has no origin that functions in the host; the vector supplies one, and with it the means to make billions of identical copies, which is what cloning means.

### 5.4.1. Plasmids

**Definition 5.4.2** A small circular double-stranded DNA that replicates in a bacterium independently of the chromosome is called a **plasmid**.

Cloning plasmids are reduced to three elements, each for a reason. The *origin* of the widely used pUC series derives from a ColE1-family plasmid whose copy number is controlled by an antisense RNA; mutations that weaken that control raise the copy number to several hundred per cell, so that plasmid DNA is abundant. The *selectable marker*, typically a β-lactamase gene, lets only plasmid-bearing cells grow on the corresponding antibiotic. The *cloning site* is a synthetic cluster of unique sites.

**Definition 5.4.3** A short synthetic region containing many unique restriction sites in a row is called a **multiple cloning site** (MCS, polylinker).

**Definition 5.4.4** The uptake of free DNA by a cell, resulting in a heritable change, is called **transformation**.

*E. coli* is not naturally competent; treatments that make it permeable yield transformants from a small fraction of the cells, and those that take up DNA usually take up a single molecule because DNA is limiting. Each colony is therefore a clone descended from one recombinant molecule, which is what makes cloning a method of separating molecules: a mixture of ligation products becomes a set of colonies, each containing one of them. Plasmid DNA is recovered by alkaline lysis, which exploits topology: on neutralization the small covalently closed plasmid strands, which remain interlinked, snap back into duplexes, whereas the long broken chromosomal DNA does not and is removed with the precipitate.

### 5.4.2. Recognizing Recombinants

A ligation yields both vector that has closed without an insert and recombinant vector, and both confer resistance. Colour distinguishes them.

**Definition 5.4.5** The restoration of β-galactosidase activity by two separately inactive fragments of the enzyme, the α peptide encoded by the vector and the remaining fragment encoded by a deletion allele in the host, is called **α-complementation**. The screen in which recombinant colonies are recognized by loss of this activity on plates with a chromogenic substrate is called **blue–white screening**.

The MCS lies in frame inside the α-peptide coding sequence, so an insert interrupts it. On plates containing the antibiotic, an inducer and the chromogenic substrate, cells without plasmid do not grow, cells with empty vector form blue colonies, and cells with an insert form white ones. The screen has known failure modes, a short in-frame insert that leaves the peptide partly active, or a rearranged vector that is white without an insert, so white colonies are confirmed by amplification or digestion.

![The pUC19 vector and blue–white screening. A: map of pUC19 (2686 bp) with its high-copy origin, the ampicillin-resistance gene bla and the multiple cloning site inside lacZα under the lac promoter. B: on plates with ampicillin, X-gal and IPTG in a lacZΔM15 host, cells without plasmid die, cells with religated vector give blue colonies, and cells whose insert interrupts lacZα give white colonies](./plots/puc-cloning.py)

**Definition 5.4.6** Cloning in which the vector is cut with two enzymes leaving incompatible ends and the insert carries the matching ends, so that it can enter in only one orientation, is called **directional cloning**.

Its two advantages are that the orientation of the insert relative to vector elements such as a promoter is known, and that the vector cannot close on itself, which removes most of the empty-vector background.

### 5.4.3. Expression Vectors

**Definition 5.4.7** A vector that supplies, next to the cloning site, a promoter, a ribosome-binding site and the other signals needed to transcribe and translate the insert in the host is called an **expression vector**.

The common bacterial design places the gene behind a promoter recognized only by the RNA polymerase of phage T7, whose gene sits in the host under an inducible promoter; the gene is therefore silent until induction and then transcribed very strongly. Short affinity tags fused to either end, a run of histidines or a small soluble protein, allow purification in one step by **affinity chromatography** ([6.4.14](/6.4.14)), with a protease site between tag and protein so that the tag can be removed. Proteins that require eukaryotic folding, disulfide bonds or glycosylation are made in yeast, insect or mammalian cells from vectors with the appropriate promoters and polyadenylation signals; *shuttle vectors* carry origins and markers for two hosts at once.

### 5.4.4. Phage and Artificial-Chromosome Vectors

Plasmids carry inserts up to about 10 kb efficiently; genomic libraries (Section 5.5) need more.

*Phage λ vectors.* The central third of the 48.5 kb λ genome is dispensable for lytic growth; replacement vectors remove it and keep the two arms with the replication and packaging genes. Packaging into phage heads in vitro accepts only DNA between cohesive-end (cos) sites that is 78–105% of the wild-type length, so the length window itself selects for molecules with an insert of roughly 9–23 kb: arms alone are too short to be packaged. Packaged phage enter cells far more efficiently than plasmids, and each clone appears as a plaque, a clear zone in a bacterial lawn.

**Definition 5.4.8** A plasmid carrying the λ cos sites, which can be packaged into λ heads but then replicates as a plasmid, is called a **cosmid**.

Since a cosmid retains almost no λ genes, nearly the whole packaging capacity is available for an insert of about 35–45 kb. Cosmids and their single-copy successors (fosmids) were central to genome mapping in the 1980s and are now largely historical.

**Definition 5.4.9** A vector based on the single-copy F plasmid of *E. coli*, which maintains inserts of about 100–300 kb stably, is called a **bacterial artificial chromosome** (BAC). A vector carrying the elements of a yeast chromosome, a centromere, an autonomously replicating sequence and two telomeres, which is maintained in yeast as a linear chromosome with inserts up to about 1–2 Mb, is called a **yeast artificial chromosome** (YAC).

YACs take the largest inserts, but many early YAC clones were chimeric or rearranged and the insert is hard to separate from the host chromosomes. BACs, held at one or two copies per cell by the F partitioning system, are much more stable, and the public human genome project sequenced the genome clone by clone from some twenty thousand overlapping BACs.

| Vector | Host | Insert | Copies per cell | Status |
|---|---|---|---|---|
| plasmid | *E. coli* | up to about 10 kb | hundreds | standard |
| λ replacement | *E. coli* (plaques) | 9–23 kb | — | now rare |
| cosmid, fosmid | *E. coli* | 35–45 kb | many / one | historical |
| BAC | *E. coli* | 100–300 kb | 1–2 | genome projects, large transgenes |
| YAC | *S. cerevisiae* | 0.2–2 Mb | 1 | historical (chimerism) |

## 5.5. Libraries and Clone Identification

### 5.5.1. Genomic Libraries

**Definition 5.5.1** A collection of clones whose inserts together contain every sequence of a genome is called a **genomic library**.

So that inserts overlap randomly instead of ending at fixed positions, the DNA is cut only partially with a frequently cutting enzyme, or sheared, and fragments of suitable length are selected. How many clones are needed follows from probability alone.

**Formula 5.5.1 (Clarke–Carbon)** If inserts of length $I$ are drawn at random from a genome of length $G$, so that a given sequence lies in a given clone with probability $f = I/G$, the number of clones for which that sequence is present with probability $P$ is
$$
N = \frac{\ln(1 - P)}{\ln(1 - f)} \approx \frac{G}{I}\,\ln\frac{1}{1 - P}. \tag{5.2}
$$

**Proof** The sequence is absent from one clone with probability $1 - f$ and, the clones being independent, from all $N$ with probability $(1 - f)^N$. Setting $1 - (1 - f)^N = P$ and solving gives Eq. (5.2); for $f \ll 1$, $\ln(1 - f) \approx -f$. $\square$

The approximate form shows the structure of the answer: the library needs $G/I$ genome equivalents multiplied by $\ln[1/(1-P)]$, which is $4.6$ for $P = 0.99$, so about five genome equivalents give $99\%$ confidence. This is the same **Poisson distribution** argument that fixes sequencing coverage ([7.2.6](/7.2.6)).

**Example 5.5.1** For the human genome ($G = 3.1 \times 10^9$ bp) and $P = 0.99$: inserts of $20$ kb give $f = 6.5 \times 10^{-6}$ and $N \approx 7.1 \times 10^5$ clones, whereas inserts of $150$ kb give $N \approx 9.5 \times 10^4$. For *E. coli* ($4.6$ Mb) with $40$ kb inserts, $N \approx 530$. Large-insert vectors were needed for mammalian genomes simply to keep the number of clones manageable.

![Clones needed for a complete genomic library (P = 0.99) against insert size for four genomes, from the Clarke–Carbon formula; the shaded bands are the insert ranges of plasmid, λ, cosmid/fosmid, BAC and YAC vectors. For the human genome, about 7.1×10⁵ λ clones or 9.5×10⁴ BACs](./plots/library-size.py)

### 5.5.2. cDNA Libraries

**Definition 5.5.2** DNA synthesized from an RNA template by reverse transcription is called **complementary DNA** (cDNA); a collection of clones of cDNAs from the mRNA of a cell or tissue is called a **cDNA library**.

A cDNA library differs from a genomic library in three useful ways: it contains only the genes expressed in the source tissue; it represents them in proportion to the abundance of their mRNAs, so that a few hundred abundant species dominate while some ten thousand rare ones are present at a few copies each; and its clones have no introns, so the coding sequence can be read directly and expressed in bacteria. Rare messages can be enriched by normalization, that is, by reannealing and removing the abundant species. The enzymology is treated in Section 5.7.1.

### 5.5.3. Finding a Clone: Hybridization and Stringency

A library helps only if one clone can be found among $10^5$–$10^6$. Classically this is done by hybridization: colonies or plaques are transferred to a membrane, their DNA is denatured and fixed, and a labeled single-stranded probe complementary to part of the wanted sequence is allowed to pair with it, so that positive clones appear as spots. The probe may be a related gene from another species, or a mixture of oligonucleotides deduced from a protein sequence, degenerate wherever the genetic code is ([7.2.19](/7.2.19)). Base pairing, melting and renaturation are treated in [7.1.11](/7.1.11); for screening, the variable that matters is how many mismatches a hybrid may contain and survive.

**Definition 5.5.3** The degree to which the conditions of hybridization and washing (temperature, salt concentration, denaturant) allow only perfectly matched duplexes to persist is called **stringency**.

High temperature, low salt (less screening of the repulsion between the backbones) and organic denaturants all destabilize duplexes and raise stringency. For long hybrids an empirical expression (Meinkoth and Wahl, 1984) gives

**Formula 5.5.2 (Melting temperature of long hybrids)**
$$
T_{\mathrm{m}}/{}^\circ\mathrm{C} = 81.5 + 16.6\lg\!\left([\ce{Na+}]/\mathrm{M}\right) + 0.41\,(\%\mathrm{GC}) - 0.63\,(\%\ \text{formamide}) - \frac{500}{L/\mathrm{bp}}, \tag{5.3}
$$
and every $1\%$ of mismatched pairs lowers $T_{\mathrm{m}}$ by about $1$–$1.5\,^\circ\mathrm{C}$.

**Example 5.5.2** A homologue with $80\%$ identity to the probe forms hybrids melting some $20$–$30\,^\circ\mathrm{C}$ below the perfect hybrid. Finding it therefore requires washing at lower temperature or higher salt than for the perfect match: lowering stringency tolerates mismatches at the price of more false positives, and this trade-off, not the labeling chemistry, is what determines whether a cross-species screen succeeds.

The alternative to hybridization is amplification. By the late 1980s a short unique sequence (a *sequence-tagged site*) could be detected by PCR in pools of clones, and Olson, Hood, Cantor and Botstein (1989) proposed building physical maps of the human genome from such sites; screening pooled clones needs about $\log_2 N$ rounds of pooling instead of $N$ separate tests.

## 5.6. The Polymerase Chain Reaction

### 5.6.1. Principle

**Definition 5.6.1** The amplification of a DNA segment defined by two oligonucleotide **primers**, which pair with opposite strands at its two ends with their 3′ ends facing each other, through repeated cycles of denaturation, primer annealing and extension by a thermostable DNA polymerase, is called the **polymerase chain reaction** (PCR).

Kary Mullis conceived PCR in 1983 (Nobel Prize in Chemistry 1993); it became practical with the DNA polymerase of *Thermus aquaticus*, which survives the denaturation step so that enzyme need not be replenished. A cycle separates the strands at about $95\,^\circ\mathrm{C}$, lets the primers (present in large excess, so that they find their sites before the long template strands can find each other) pair a few degrees below their melting temperature, and extends them at about $72\,^\circ\mathrm{C}$. Primers of some twenty nucleotides are chosen so that their melting temperatures match and their 3′ ends pair neither with each other nor within themselves, since only a 3′ end is extended. The 5′ end, by contrast, need not match at all: a 5′ tail carrying a restriction site, a promoter or a mutation is copied into the product, which is the basis of most uses of PCR in construction (Section 5.6.4).

### 5.6.2. The Bookkeeping of the First Cycles

A newly made strand starts at a primer but runs on to the end of its template, so products bounded by both primers appear only in the third cycle.

**Proposition 5.6.1** Starting from one duplex template, and assuming every strand is copied in every cycle, after $n \ge 1$ cycles there are $2^n$ duplexes, of which $2^n - 2n$ have exactly the target length (both ends defined by primers).

**Proof** Classify the strands as original (2 of them), *long* (made on an original template: they begin at a primer and continue to the end of the template) and *short* (bounded by both primers). Each strand templates one new strand per cycle. An original template yields a long strand; a long or short template yields a short strand, because synthesis stops at the 5′ end of the template, which for those strands is a primer. Hence after $n$ cycles there are $2$ original strands, $2n$ long strands and $2^{n+1}$ strands in all. A duplex has target length only if both strands are short, and counting gives $2^{n+1}/2 - 1 - (n-1) - 1 \cdot 1 = 2^n - 2n$. $\square$

The sequence $2^n - 2n$ is $0, 0, 2, 8, 22, 52, \dots$: nothing of target length after two cycles, two molecules of eight after three, and after thirty cycles $2^{30} - 60 \approx 10^9$, which is essentially all of the product, because the long products grow only linearly.

![PCR bookkeeping. A: the strands present after cycles 1–3, obtained by copying every strand from the primer that pairs with it; duplexes of target length (orange on both strands) first appear after cycle 3, and their number after n cycles is 2ⁿ − 2n. B: amplification from 10³, 2²⁰ and 10⁹ starting duplexes in a primer-limited model with 6×10¹² primer molecules; all three reactions level off near 10¹² duplexes, as the sudden-stop estimate (dashed) suggests](./plots/pcr-bookkeeping.py)

### 5.6.3. Efficiency and the Plateau

With efficiency $E$ (the fraction of templates copied per cycle, ideally $1$) the number of molecules is $N_n = N_0(1 + E)^n$. Exponential growth does not continue: every reaction levels off at roughly the same number of molecules, whatever the input, and the budget of primers explains the order of magnitude.

**Example 5.6.1 (Why amplification saturates near $10^{12}$ molecules)** A reaction starting from $2^{20} \approx 10^6$ templates saturates after about $21$ cycles; assuming perfect doubling and a sudden stop, it has made $2^{20} \times 2^{21} = 2^{41} \approx 2 \times 10^{12}$ molecules. A reaction contains of the order of $10^{-11}\,\mathrm{mol}$ of each primer, that is some $6 \times 10^{12}$ molecules, and each product duplex consumes one molecule of each. The plateau therefore reflects the primer supply, not the nucleotides, of which there are a thousandfold more than needed.

Saturation in fact begins earlier, because the product competes with the primers: as the product strands approach the primer concentration they increasingly pair with each other during cooling instead of with a primer, and the polymerase becomes limiting relative to the number of templates. A model in which the fraction of duplexes copied per cycle is $E_0 p/(p + N)$, with $p$ the remaining primer, already reproduces the common plateau (figure). The practical consequence is developed in [7.2.6](/7.2.6): the final amount of product says almost nothing about the starting amount, so quantification must use the cycle at which product first becomes detectable.

### 5.6.4. Fidelity and Uses

Taq polymerase has no $3' \to 5'$ proofreading exonuclease (Section 5.7) and misincorporates at about $10^{-5}$ per base per duplication; proofreading archaeal enzymes err at about $10^{-6}$ or less. If each duplication introduces errors at rate $\varepsilon$ per base, then after $d$ effective duplications a product of length $L$ carries on average $\lambda = \varepsilon L d$ errors and a fraction $\mathrm{e}^{-\lambda}$ of the molecules are error-free.

**Example 5.6.2** For a $1$ kb product after $30$ duplications, $\varepsilon = 2 \times 10^{-5}$ gives $\lambda = 0.6$ and only about $55\%$ correct molecules, whereas $\varepsilon = 1 \times 10^{-6}$ gives $\lambda = 0.03$ and $97\%$. Products destined to be cloned and expressed are therefore made with proofreading enzymes and the clones are sequenced; for simple detection, fidelity is irrelevant.

PCR is now the first step of most manipulations: adding restriction or type IIS sites and assembly overlaps through 5′ tails; introducing a point mutation by amplifying the whole plasmid with primers that carry it and removing the methylated template with DpnI (Section 5.1.4); testing colonies for inserts; amplifying cDNA to detect and quantify transcripts ([7.2.6](/7.2.6)); and detecting pathogens or genotypes, where exponential amplification gives single-molecule sensitivity and carry-over of earlier products is the main hazard.

## 5.7. Polymerase Activities as a Toolbox

The organizing idea of molecular technology is that a DNA polymerase is more than a copying machine. Besides $5' \to 3'$ synthesis on a primed template, the various enzymes offer a $3' \to 5'$ exonuclease (proofreading), a $5' \to 3'$ exonuclease (removal of the strand ahead), extension of RNA primers, initiation at a nick, displacement of a downstream strand, use of RNA as template, or addition of nucleotides with no template at all. What all of them require, a template, a free 3′-OH and synthesis only $5' \to 3'$, is the set of constraints every method must respect. The enzymes and their roles in the cell belong to [7.2.7](/7.2.7).

| Enzyme | Template | $3' \to 5'$ exo | $5' \to 3'$ exo | Special property | Use as a tool |
|---|---|---|---|---|---|
| *E. coli* DNA polymerase I | DNA | yes | yes | starts at a nick | nick translation, second-strand cDNA |
| Klenow fragment | DNA | yes (exo⁻ mutants: no) | no | — | filling 5′ overhangs, 3′ end labeling |
| T4 DNA polymerase | DNA | strong | no | — | blunting ends from either overhang |
| Taq polymerase | DNA | no | yes | thermostable; adds a 3′ A | PCR; cleaves probes during extension ([7.2.6](/7.2.6)) |
| Pfu and engineered enzymes | DNA | yes | no | thermostable, high fidelity | PCR for cloning |
| φ29 polymerase | DNA | yes | no | strong strand displacement, high processivity | rolling-circle and whole-genome amplification |
| Reverse transcriptase | RNA or DNA | no | no | associated RNase H; adds untemplated nucleotides at the 5′ end of a capped template | cDNA synthesis, template switching ([7.2.6](/7.2.6)) |
| Terminal transferase | none | no | no | adds nucleotides to any 3′ end | homopolymer tails, end labeling |

The table answers the questions a cloner asks. Can reverse transcriptase use DNA as a template? Yes, and in retroviruses it makes the second strand itself. Can a DNA polymerase extend an RNA primer? Yes, as it does on every Okazaki fragment ([7.2.7](/7.2.7)). Can it start at a nick? Only an enzyme that removes or displaces the strand ahead of it.

### 5.7.1. Making cDNA

Reverse transcriptase needs a primer, and most eukaryotic mRNAs provide a binding site in their poly(A) tail ([7.2.17](/7.2.17)), so an oligo(dT) primer starts the first strand at the 3′ end of the message. The classical second-strand method combines three activities: RNase H, which cleaves RNA only within an RNA–DNA hybrid, nicks the template; the remaining RNA pieces prime DNA polymerase I, which extends them while removing the RNA ahead of it; and ligase seals the nicks. The product is given ends for cloning either with adapters or with complementary homopolymer tails added by terminal transferase, the remaining nicks being repaired in the host. Current methods instead add defined adapters to both ends during reverse transcription by template switching ([7.2.6](/7.2.6)).

**Definition 5.7.1** The movement of a nick along a duplex in the $5' \to 3'$ direction by a polymerase that removes nucleotides ahead of the nick with its $5' \to 3'$ exonuclease while adding nucleotides behind it is called **nick translation**.

Nick translation was the standard way to make labeled hybridization probes: random nicks are introduced and the polymerase replaces the DNA downstream of each with nucleotides among which one is labeled. Priming denatured DNA with random hexamers and the Klenow fragment gives higher specific activity. Two further labeling tools follow from the same logic: polynucleotide kinase transfers the terminal phosphate of ATP to a 5′-OH, labeling 5′ ends, and the Klenow fragment labels 3′ ends by filling in 5′ overhangs. Molecules labeled at one end are the basis of footprinting and nuclease mapping ([7.2.6](/7.2.6)).

**Definition 5.7.2** The template-independent DNA polymerase that adds deoxynucleotides to the 3′-OH of DNA is called **terminal deoxynucleotidyl transferase** (TdT).

TdT is the only DNA polymerase that needs no template. Its natural role is in developing lymphocytes, where it inserts random nucleotides at the junctions made by V(D)J recombination and so enlarges the repertoire of antigen receptors ([7.2.9](/7.2.9)); as a tool it adds homopolymer tails, labels 3′ ends, and attaches adapters to single-stranded molecules.

### 5.7.2. Assembly by Overlap

Restriction cloning is limited by the sites that happen to be available. A third strategy uses only designed sequence overlaps.

**Definition 5.7.3** The isothermal, single-reaction joining of DNA fragments that share terminal overlaps of $20$–$40$ bp by the combined action of a $5' \to 3'$ exonuclease, a DNA polymerase and a DNA ligase is called **Gibson assembly** (Gibson et al., 2009).

The exonuclease recesses the 5′ ends, exposing 3′ single-stranded ends; the complementary overlaps of neighbouring fragments pair; the polymerase fills the remaining gaps; and the ligase seals the nicks.

![Joining two fragments that share a terminal overlap (yellow). 1: the two duplexes, each strand drawn with its 3′ end as an arrowhead. 2: the exonuclease recesses the 5′ ends, exposing complementary 3′ single-stranded ends. 3: the overlaps pair, leaving a gap on each strand. 4: the polymerase fills the gaps (teal) and the ligase seals the nicks, giving a junction without a scar](./plots/gibson-assembly.py)

Because the overlaps are designed, the junction has no scar and need contain no restriction site, and because the three enzymes work at one temperature, several fragments join in one reaction. The overlaps themselves are usually added by PCR as 5′ tails, which is why this method and the type IIS methods of Section 5.2 have displaced restriction cloning for constructing plasmids: the joints are specified by sequence design rather than by the sites a molecule happens to contain. Synthetic biology extends the same principle to whole genomes, assembled hierarchically from chemically synthesized oligonucleotides.

## Summary

| Tool | Chemistry | What it is for |
|---|---|---|
| Restriction endonuclease (Definition 5.1.1) | cleaves a palindrome, leaving 5′-P and 3′-OH; type II needs only $\mathrm{Mg^{2+}}$ | cutting at defined sites; frequency $4^n$ bp (Eq. 5.1), modified by dinucleotide bias |
| Sticky and blunt ends (Definition 5.1.2) | staggered or opposed cuts | compatibility between enzymes with the same overhang; blunt joining is general but inefficient |
| Methylation (Dam, Dcm; Definition 5.1.3) | $N^6$-methyladenine, 5-methylcytosine | blocks or permits specific enzymes; DpnI removes a methylated template; isoschizomer pairs probe methylation |
| Type IIS enzymes (Definition 5.2.1) | cut outside an asymmetric site | overhangs of any sequence; scarless, ordered multi-fragment assembly; FokI nuclease domain → editing ([7.2.24](/7.2.24)) |
| DNA ligase (Definition 5.3.1) | AMP transferred to lysine, then to 5′-P, then attacked by 3′-OH | joining nicks; needs 5′-P; dilution favours circles |
| Vectors (Definitions 5.4.1–5.4.9) | origin + marker + cloning site | plasmid ≤10 kb, λ 9–23 kb, cosmid 35–45 kb, BAC 100–300 kb, YAC up to 2 Mb; λ packaging length window selects inserts |
| Screening (Definitions 5.4.5, 5.4.6) | α-complementation; incompatible ends | blue–white screen for inserts; directional cloning fixes orientation and suppresses empty vector |
| Libraries (Definitions 5.5.1, 5.5.2) | partial digestion or shearing; reverse transcription | Clarke–Carbon $N = \ln(1-P)/\ln(1-f)$ (Eq. 5.2): about five genome equivalents for $P = 0.99$ (Example 5.5.1); cDNA has no introns and reflects abundance |
| Hybridization stringency (Definition 5.5.3) | $T_{\mathrm{m}}$ from Eq. (5.3); $1\%$ mismatch ≈ $1$–$1.5\,^\circ\mathrm{C}$ | trade-off between cross-species detection and false positives |
| PCR (Definition 5.6.1) | thermostable polymerase, primer excess | target-length product from cycle 3, $2^n - 2n$ molecules (Proposition 5.6.1); plateau set by primers near $10^{12}$ (Example 5.6.1); fidelity $\mathrm{e}^{-\varepsilon L d}$ (Example 5.6.2); 5′ tails add sites and mutations |
| Polymerase activities (Section 5.7) | $3'\to5'$ and $5'\to3'$ exonucleases, nick initiation, strand displacement, RNA templates, no template | nick translation (Definition 5.7.1), end labeling, cDNA synthesis, TdT tailing (Definition 5.7.2) |
| Overlap assembly (Definition 5.7.3) | exonuclease + polymerase + ligase at one temperature | scarless joining of several fragments designed by sequence |

## Questions

1. A $3$ Mb bacterial genome with $60\%$ GC is digested with an enzyme recognizing a 6 bp site consisting only of G and C. How many fragments are expected, and how does this compare with the prediction of Eq. (5.1)?

   **Answer** With $p_{\mathrm{G}} = p_{\mathrm{C}} = 0.3$, the probability of a specified GC-only hexamer is $0.3^6 = 7.29 \times 10^{-4}$, that is one site per $1372$ bp, so about $2200$ fragments; Eq. (5.1) with equal base frequencies predicts one site per $4096$ bp, about $730$ fragments. In a GC-rich genome a GC-rich site is about three times more frequent than the naive estimate, which is why site frequency must be computed from the actual base (and dinucleotide) composition.
2. Why does a ligation of blunt ends require much more DNA and enzyme than a ligation of complementary sticky ends?

   **Answer** With sticky ends the four-base overhangs pair, holding the two ends together long enough and in the right geometry for the ligase to seal two nicks; the effective local concentration of the ends is thereby enormous. Blunt ends have nothing to hold them together, so the ligase must capture two ends that meet by chance in the correct alignment, and the rate is proportional to the product of end concentrations, hence the need for high concentrations and crowding agents.
3. A vector is cut with a single enzyme and ligated to an insert with the same ends. Most of the colonies contain vector without insert. Name two ways to reduce this background and explain each.

   **Answer** Dephosphorylate the vector: without 5′-phosphates the vector cannot be closed by ligase on either strand, whereas the insert supplies the phosphates needed to join it at each end, the remaining nicks being repaired in the host. Or use directional cloning with two enzymes leaving incompatible ends, so that the two ends of the vector cannot pair with each other, which also fixes the orientation of the insert.
4. A gene is cloned from mammalian genomic DNA into a bacterial expression vector, and no protein is made even though the insert is correct. Give the most likely reason and the standard remedy.

   **Answer** The genomic clone contains introns, which bacteria cannot splice, so the reading frame is interrupted; even without introns, eukaryotic signals are not read correctly. The remedy is to clone the cDNA, made by reverse transcription of the mRNA, behind the vector's own promoter and ribosome-binding site.
5. How many clones with $35$ kb inserts are needed for a $99.9\%$ chance that a given sequence of the *Drosophila* genome ($1.4 \times 10^8$ bp) is represented?

   **Answer** $f = 3.5 \times 10^4/1.4 \times 10^8 = 2.5 \times 10^{-4}$, and $N = \ln(0.001)/\ln(1 - 2.5 \times 10^{-4}) \approx 6.9/2.5 \times 10^{-4} \approx 2.8 \times 10^4$ clones, that is about seven genome equivalents.
6. Two reactions are amplified for $35$ cycles, one starting from $10^2$ and one from $10^6$ molecules, and both give the same amount of product on a gel. What can be concluded about the starting amounts, and what measurement would distinguish them?

   **Answer** Nothing: both reactions have reached the plateau set by the primer supply and the competition of product strands, which erases the initial difference. The reactions must be compared while they are still exponential, by monitoring the product in every cycle and recording the cycle at which it first exceeds a threshold, which differs by $\log_2(10^4) \approx 13$ cycles between the two ([7.2.6](/7.2.6)).
7. Explain why the first product molecules of exactly the target length appear only in the third cycle, and why the long products become irrelevant.

   **Answer** A strand made on an original template begins at a primer but runs past the other primer site to the end of the template, so one of its ends is undefined; only when such a long strand is itself copied does synthesis stop at a 5′ end that is a primer, giving a strand bounded at both ends, and a duplex of two such strands first exists after the third cycle. The long strands are made only on the two original templates, so their number grows by two per cycle (linearly), while target-length molecules double, and after thirty cycles they are a fraction of about $60/2^{30} \approx 6 \times 10^{-8}$ of the product.
8. You must join four DNA fragments in a defined order, and each fragment contains internal sites for the common six-cutters. Which assembly strategy would you choose, and why?

   **Answer** Either overlap-based assembly (Definition 5.7.3), since it needs no restriction sites at all, only $20$–$40$ bp overlaps added by PCR as 5′ tails, or type IIS assembly with an enzyme whose site is absent from the fragments, using four distinct four-base overhangs to fix the order. Both leave no scar; the choice depends on whether an enzyme free of internal sites exists (type IIS) or not (overlap assembly).
