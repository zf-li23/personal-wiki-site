---
title: "Tools II: Measurement and Sequencing"
description: Hybridization assays (Southern and Northern blots, FISH and single-molecule FISH); quantitative PCR (SYBR Green and hydrolysis probes, the quantification cycle and the standard curve, relative quantification, digital PCR); steady-state levels versus synthesis rates and run-on assays; mapping transcript ends (S1 nuclease protection, primer extension); protein–nucleic acid interactions (filter binding, gel shift, DNase I and chemical footprinting, cross-linking, ChIP and ChIP-seq); measuring translation (polysome and ribosome profiling); sequencing chemistries (Sanger, pyrosequencing, reversible-terminator sequencing by synthesis, SMRT, nanopore); libraries, template switching, target enrichment and coverage statistics.
---

Every conclusion of molecular biology rests on a measurement: how much of an RNA there is, where it starts, which protein sits on which DNA, how fast a gene is transcribed, which messages are being translated, and, underlying all of them, what the sequence is. This chapter explains the logic of the main measurements: what physical or enzymatic property each one exploits, what quantity it actually reports, and what it cannot distinguish. Most of them are built from the enzymes of [7.2.5](/7.2.5) (polymerases, nucleases, ligases) combined with two read-outs, separation by length in gel **electrophoresis** ([6.4.14](/6.4.14)) and, increasingly, counting sequenced molecules. The chapter is a reference for the rest of the course: the gel shift and footprinting experiments of bacterial and eukaryotic transcription ([7.2.10](/7.2.10)–[7.2.14](/7.2.14)), the nuclear run-on and nuclease-mapping experiments of RNA processing ([7.2.16](/7.2.16)–[7.2.18](/7.2.18)) and ribosome profiling ([7.2.20](/7.2.20)) all use the methods described here. How the resulting sequencing data are analysed (alignment, peak calling, quantification of expression) belongs to [7.8](/7.8).

## 6.1. Hybridization Assays

All hybridization assays rest on one property: a single-stranded nucleic acid pairs specifically with its complement, and the stability of the hybrid depends on its length, base composition and the number of mismatches, which the stringency of the conditions controls ([7.2.5](/7.2.5), [7.1.11](/7.1.11)). A labeled complementary molecule, the probe, therefore reports the presence and amount of one sequence in a complex mixture.

**Definition 6.1.1** The detection of specific DNA sequences in a mixture of fragments separated by gel electrophoresis, after denaturation and transfer of the fragments to a membrane, by hybridization with a labeled probe, is called a **Southern blot** (Southern, 1975). The same procedure applied to RNA separated in a denaturing gel is called a **Northern blot**.

A Southern blot answers questions about genome structure: how many copies of a gene there are, whether it has been rearranged or deleted, and where the restriction sites around it lie (restriction fragment length polymorphisms, the first genome-wide genetic markers). It also maps DNase I hypersensitive sites by indirect end-labeling ([7.2.4](/7.2.4)). The required sensitivity is set by simple arithmetic: a single-copy $1$ kb fragment in $10\,\mu\mathrm{g}$ of human DNA amounts to $10\,\mu\mathrm{g} \times 10^3/3.1 \times 10^9 \approx 3\,\mathrm{pg}$, which radioactive or chemiluminescent probes detect. A Northern blot reports the size of a transcript as well as its abundance, and so distinguishes alternatively processed forms that other assays merge; a constitutively expressed RNA on the same blot serves as a loading control. The analogous detection of proteins with antibodies after electrophoresis is the Western blot.

**Definition 6.1.2** Hybridization of fluorescently labeled probes to nucleic acids within fixed cells or chromosomes, observed by fluorescence microscopy, is called **fluorescence in situ hybridization** (FISH).

FISH maps genes to chromosomes, reveals chromosome territories and rearrangements, and localizes RNAs within cells. In *single-molecule FISH* (Raj et al., 2008) several dozen short oligonucleotide probes, each carrying one fluorophore, tile one mRNA; a single bound probe is invisible, but the dozens bound to one molecule produce a diffraction-limited spot, so individual mRNA molecules can be counted in each cell. Absolute counts per cell, rather than averages over a population, revealed the large cell-to-cell variation of gene expression and its origin in transcriptional bursts ([7.2.22](/7.2.22)).

Microarrays generalized hybridization to the whole transcriptome by placing tens of thousands of probes on a slide; they have largely been replaced by sequencing (Section 6.8), which counts molecules instead of measuring fluorescence of hybrids and so has a wider dynamic range and needs no prior knowledge of the sequences.

## 6.2. Quantitative PCR

### 6.2.1. The Quantification Cycle

The end point of PCR says almost nothing about the input, because all reactions converge on the same plateau ([7.2.5](/7.2.5)). What depends on the input is *when* the product appears: a sample with twice as much template reaches any given amount of product one cycle earlier. Monitoring the product in every cycle turns this into a measurement.

**Definition 6.2.1** PCR in which the amount of product is measured by fluorescence after every cycle is called **quantitative PCR** (qPCR, real-time PCR). The fractional cycle number at which the fluorescence of a reaction crosses a threshold set within the exponential phase is called the **quantification cycle** $C_q$ (also threshold cycle $C_t$).

**Formula 6.2.1 (Standard curve)** If a reaction with $N_0$ initial template molecules amplifies with efficiency $E$, the threshold amount $N_{\mathrm{T}}$ is reached when $N_0(1 + E)^{C_q} = N_{\mathrm{T}}$, so
$$
C_q = \frac{\lg N_{\mathrm{T}} - \lg N_0}{\lg(1 + E)}, \qquad \frac{\mathrm{d}C_q}{\mathrm{d}\lg N_0} = -\frac{1}{\lg(1 + E)}. \tag{6.1}
$$
For perfect doubling ($E = 1$) the slope is $-1/\lg 2 = -3.32$: a tenfold difference in input shifts $C_q$ by $3.32$ cycles. Conversely, the efficiency is estimated from the slope $s$ of a dilution series as $E = 10^{-1/s} - 1$; acceptable assays have $E$ between about $0.9$ and $1.1$ (slopes between $-3.6$ and $-3.1$).

![Quantitative PCR. A: simulated amplification curves for tenfold dilutions of a template (10 to 10⁶ copies, three replicates each) with efficiency 0.95; the dashed line is the threshold that defines Cq. B: Cq against the logarithm of input copy number; the slope (−3.45) gives the efficiency E = 10^(−1/slope) − 1 = 0.95, close to the ideal slope −3.32](./plots/qpcr-standard-curve.py)

**Example 6.2.1** Three samples amplified with the same primers reach the threshold at cycles $22$, $24$ and $20$. Relative to the first, the second contained $2^{-2} = 1/4$ as much template and the third $2^{2} = 4$ times as much, assuming $E = 1$. The quantity measured is a ratio of initial amounts; an absolute number requires a standard curve made from known amounts of the same template.

### 6.2.2. Detection Chemistries

Two ways of making fluorescence report the product are standard. The dye *SYBR Green* binds double-stranded DNA and fluoresces far more strongly when bound; it detects every double-stranded product, including primer dimers and unintended products, so the specificity of the reaction is checked afterwards by a melting curve, in which a single product gives a single, sharp melting transition.

**Definition 6.2.2** An oligonucleotide that pairs with the target between the two primers and carries a fluorophore at its 5′ end and a quencher at its 3′ end, and whose fluorescence is released when the $5' \to 3'$ exonuclease of the polymerase degrades it during extension, is called a **hydrolysis probe** (TaqMan probe).

While the probe is intact, the quencher close to the fluorophore absorbs its excitation energy by **Förster resonance energy transfer** or contact **quenching** ([6.4.10](/6.4.10)); a polymerase that meets the paired probe while extending the primer cleaves it, separating the two dyes, and the fluorescence increases in proportion to the product made in that cycle. Because the signal requires pairing of a third oligonucleotide, the probe adds specificity, and probes with different dyes allow several targets to be measured in one reaction. The assay depends on a polymerase with $5' \to 3'$ exonuclease activity, the "Taq" of TaqMan.

### 6.2.3. Relative and Absolute Quantification

Gene expression is usually measured by reverse transcription followed by qPCR (RT-qPCR) and expressed relative to a reference gene whose expression is assumed constant. The comparative method takes the difference $\Delta C_q = C_q(\text{target}) - C_q(\text{reference})$ in each sample and the difference of these between a treated and a control sample; with $E = 1$ for both assays,
$$
\text{fold change} = 2^{-\Delta\Delta C_q}, \qquad \Delta\Delta C_q = \Delta C_q(\text{treated}) - \Delta C_q(\text{control}). \tag{6.2}
$$
Its assumptions are the weak points of the method: equal efficiencies (a $5\%$ difference in efficiency over $25$ cycles changes the ratio by more than $3$-fold), a truly constant reference, and equal efficiency of reverse transcription.

**Definition 6.2.3** PCR in which a sample is divided into thousands of small partitions, each amplified to its end point and scored as positive or negative, the number of template molecules being inferred from the fraction of negative partitions, is called **digital PCR**.

If molecules are distributed at random among partitions, the number per partition follows a **Poisson distribution** with mean $\lambda$, and the fraction of empty partitions is $\mathrm{e}^{-\lambda}$. Hence
$$
\lambda = -\ln(\text{fraction negative}),
$$
and the total count is $\lambda$ times the number of partitions. Digital PCR needs no standard curve and is insensitive to efficiency, because each partition is scored only as positive or negative; it is used for absolute quantification, rare mutations in cell-free DNA, and viral loads.

## 6.3. Steady-State Levels and Synthesis Rates

### 6.3.1. Concentration Is Not Rate

Blots, qPCR and RNA sequencing measure how much of an RNA is present, not how fast it is made. If an RNA is synthesized at rate $k_{\mathrm{s}}$ and degraded with first-order rate constant $k_{\mathrm{d}}$, its amount $m$ obeys the **ordinary differential equation**
$$
\frac{\mathrm{d}m}{\mathrm{d}t} = k_{\mathrm{s}} - k_{\mathrm{d}}m, \qquad \bar m = \frac{k_{\mathrm{s}}}{k_{\mathrm{d}}}, \tag{6.3}
$$
so two genes with the same steady-state level may differ tenfold in transcription if their RNAs differ tenfold in stability, and a change in level after a stimulus may come from either term. After a step change in $k_{\mathrm{s}}$ the level approaches its new value with time constant $1/k_{\mathrm{d}}$ ([7.2.18](/7.2.18)). To measure transcription itself one must label or capture the RNA that is being made.

### 6.3.2. Run-On Assays

**Definition 6.3.1** The measurement of transcription in which nuclei are isolated, the RNA polymerases already engaged on the genes are allowed to extend their nascent RNAs in vitro with labeled or tagged nucleotides, and the labeled RNA from each gene is quantified, is called a **nuclear run-on assay**.

The logic is that isolated nuclei do not initiate new transcripts but polymerases already elongating continue for a short distance; the label therefore enters only RNA from genes that were being transcribed at the moment of isolation, in proportion to the number of polymerases on each gene, that is, to the transcription rate at that moment. Classically the labeled RNA was hybridized to gene probes fixed on a membrane; this is how the transcription of immediate-early genes was shown to rise within minutes of a stimulus. Sequencing versions report polymerase positions across the genome: GRO-seq incorporates a brominated nucleotide and purifies the tagged RNA with an antibody, and PRO-seq uses nucleotides that allow extension by a single base, mapping the active site of each polymerase at single-nucleotide resolution; these maps revealed widespread promoter-proximal pausing of RNA polymerase II ([7.2.13](/7.2.13)). Nascent RNA can also be read without run-on, by immunoprecipitating the polymerase and sequencing the 3′ ends of the RNA it carries. In living cells, a short pulse of a modified nucleoside such as 4-thiouridine labels newly made RNA; at steady state the labeled fraction after a pulse of length $t$ is $1 - \mathrm{e}^{-k_{\mathrm{d}}t}$, so a single labeling experiment estimates synthesis and degradation rates together.

A different way to measure promoter activity is a *reporter gene*: the control region is fused to a coding sequence whose product is easy to measure (β-galactosidase, luciferase, which produces light by **bioluminescence**, or a fluorescent protein). The amount of reporter product then reflects the activity of the promoter, which is how the elements of promoters and enhancers were dissected by mutation ([7.2.12](/7.2.12), [7.2.14](/7.2.14)).

## 6.4. Mapping the Ends of Transcripts

### 6.4.1. Nuclease Protection

**Definition 6.4.1** The determination of the position of the 5′ or 3′ end of a transcript by hybridizing it to a labeled single-stranded DNA probe that spans the end, digesting all single-stranded nucleic acid with S1 nuclease and measuring the length of the labeled probe fragment that the RNA protects, is called **S1 mapping** (Berk and Sharp, 1977).

S1 nuclease, from the mold *Aspergillus oryzae*, degrades single-stranded DNA and RNA and also cuts double-stranded DNA at nicks, gaps and loops, but spares duplexes. The probe is labeled at the end that lies inside the transcribed region. The RNA protects the probe from its own 5′ end to the label; everything beyond is single-stranded and digested. The length of the surviving labeled fragment, read against a size ladder (ideally a sequencing ladder of the same DNA), is therefore the distance from the label to the start of the transcript, and the amount of the fragment is proportional to the amount of that RNA. Several start sites give several bands; a transcript that starts upstream of the probe protects the whole probe. The 3′ end is mapped the same way with a probe labeled at its other end. The RNase protection assay is the same design with an RNA probe and RNases, and is more sensitive.

![S1 nuclease mapping of a transcription start site. A: a single-stranded probe spanning the start site and labeled at its end inside the gene is hybridized to the RNA; S1 nuclease removes everything single-stranded, and the labeled fragment that survives is as long as the distance from the label to the 5′ end of the RNA. B: on a denaturing gel the band moves with the start site (three hypothetical sites A–C); a transcript that starts upstream of the probe protects the full-length probe](./plots/nuclease-mapping.py)

### 6.4.2. Primer Extension and Run-Off Transcription

**Definition 6.4.2** The mapping of the 5′ end of an RNA by annealing a labeled oligonucleotide some tens to a hundred nucleotides downstream of the presumed start and extending it with reverse transcriptase to the end of the template, the length of the product giving the position of the 5′ end, is called **primer extension**.

Primer extension is simpler than S1 mapping and gives the same information, but reverse transcriptase can stop prematurely at stable secondary structures or modified nucleotides, producing extra bands; this weakness was later turned into a method, since chemical modification of RNA followed by detection of stops or misincorporations maps RNA structure. For transcription in vitro, *run-off transcription* serves the same purpose: a template is cut at a known site downstream of the promoter, and polymerase starting at the promoter runs off the end, giving a transcript whose length locates the start site and whose amount measures the strength of the promoter ([7.2.12](/7.2.12)). Genome-wide, 5′ ends are mapped by capturing capped RNA ends and sequencing them, 3′ ends by sequencing from the poly(A) tail.

## 6.5. Protein–Nucleic Acid Interactions

### 6.5.1. Binding Assays

The oldest binding assay uses a property of nitrocellulose: proteins stick to it, double-stranded DNA alone passes through, and DNA bound to a protein is retained with it. Filtering mixtures of labeled DNA and protein therefore measures the amount of complex. Kinetics follow from the same assay: if a preformed complex with labeled DNA is challenged with an excess of unlabeled DNA, every complex that dissociates is replaced by an unlabeled one, so the retained label decays as $\mathrm{e}^{-k_{\mathrm{off}}t}$ and gives the dissociation rate constant. This is how σ factor was shown to make RNA polymerase bind promoters tightly ([7.2.10](/7.2.10)) and how the lac repressor was characterized ([7.2.11](/7.2.11)).

**Definition 6.5.1** The detection of a protein–DNA complex by the slower migration of a short labeled DNA bound to protein than of the free DNA during electrophoresis in a nondenaturing gel is called an **electrophoretic mobility shift assay** (EMSA, gel shift assay).

The complex survives electrophoresis because the gel matrix keeps dissociated partners close together, so they rebind before they separate. A gel shift shows more than binding. Complexes of different composition migrate differently, so stepwise assembly can be followed band by band, as for the preinitiation complex ([7.2.13](/7.2.13)); an antibody against one protein further retards the complex containing it (a supershift), identifying the protein; and competition with unlabeled DNAs of different sequence measures specificity. When the DNA concentration is far below the dissociation constant $K_D$, the fraction of DNA bound is $\theta = [\mathrm{P}]/([\mathrm{P}] + K_D)$, so $K_D$ is the protein concentration that shifts half of the DNA.

### 6.5.2. Footprinting

**Definition 6.5.2** The identification of the DNA sequence covered by a bound protein through the protection of that sequence from cleavage by DNase I, seen as a gap in the ladder of cleavage products of an end-labeled DNA, is called **DNase I footprinting** (Galas and Schmitz, 1978).

The DNA is labeled at one end of one strand, the protein is bound, and the complex is treated with so little DNase I that each molecule is cut on average less than once. The products are denatured and separated on a high-resolution gel; each band corresponds to a cut at one position, measured from the label. Where the protein covers the DNA no cuts occur, and the ladder has a gap, the footprint; positions where the protein bends the DNA are often cut more readily (hypersensitive bands).

Why so little enzyme? Only the cut nearest to the label is seen, because the fragment beyond it is unlabeled. If the number of cuts per molecule is Poisson distributed with mean $\lambda$, and each bond is cut with the same small probability, the probability that the labeled fragment ends at position $i$ is approximately geometric, decreasing as $\mathrm{e}^{-\lambda i/L}$ along a fragment of length $L$. Under single-hit conditions ($\lambda \lesssim 1$) the ladder is nearly uniform and the whole fragment is read; with heavy digestion almost all labeled fragments are short and the distal part of the ladder, including any footprint there, disappears.

![DNase I footprinting and gel shift, simulated. A: cleavage ladders of an end-labeled fragment without and with a protein covering positions 50–70; the protected positions leave a gap. B: band intensity along the ladder for an average of 0.5 and 5 cuts per molecule (solid: naked DNA; dashed: with protein); heavy digestion confines the signal to short fragments and loses the distal footprint. C: fraction of DNA shifted against protein concentration for KD = 10 nM; half of the DNA is shifted at [P] = KD](./plots/footprinting.py)

Chemical reagents give finer footprints. Dimethyl sulfate methylates guanine N7 in the major groove (and adenine N3 in the minor groove), and a bound protein that contacts these atoms protects or enhances their methylation; hydroxyl radicals cut the backbone almost without sequence preference and show the protected surface at single-nucleotide resolution; potassium permanganate oxidizes thymines only when they are unpaired, and so detects the melted DNA of an open promoter complex ([7.2.10](/7.2.10)). In interference experiments the DNA is modified first and the molecules that can still bind are selected, revealing which bases are essential for binding.

### 6.5.3. Cross-Linking and Chromatin Immunoprecipitation

Cross-linking fixes contacts covalently: ultraviolet light joins proteins to nucleic acid bases they touch, and photoreactive nucleotides placed at defined positions report which part of a protein or RNA lies next to them, as in the experiments that measured the RNA–DNA hybrid inside RNA polymerase ([7.2.10](/7.2.10)). Formaldehyde cross-links reversibly and works in living cells, which is the basis of the most widely used in vivo assay.

**Definition 6.5.3** The identification of the DNA sequences bound by a protein in living cells, by cross-linking proteins to DNA with formaldehyde, fragmenting the chromatin, precipitating the protein of interest with a specific antibody, reversing the cross-links and analyzing the co-precipitated DNA, is called **chromatin immunoprecipitation** (ChIP). When the precipitated DNA is analyzed by high-throughput sequencing, the method is called **ChIP-seq**.

ChIP measures enrichment: the amount of a given DNA in the precipitate relative to the input chromatin, quantified for a few sites by qPCR or genome-wide by sequencing, where binding sites appear as peaks of reads. The same design maps histone modifications and variants ([7.2.4](/7.2.4), [7.2.15](/7.2.15)). Its limitations are the quality of the antibody, the fact that cross-linking captures indirect as well as direct contacts, and the resolution set by fragment size. Newer methods tether a nuclease or transposase to the antibody in permeabilized cells, so that only DNA near the bound protein is released, which gives lower background from far fewer cells. For RNA-binding proteins, the analogous method cross-links with ultraviolet light, immunoprecipitates the protein, and sequences the bound RNA fragments.

## 6.6. Measuring Translation

The amount of an mRNA does not tell how much protein is made from it, because translation is regulated ([7.2.20](/7.2.20)). Two methods measure translation directly by locating ribosomes.

In *polysome profiling*, cell extract is centrifuged through a sucrose gradient, and ribosomal subunits, single ribosomes and polysomes (mRNAs carrying several ribosomes) separate by their sedimentation (**sedimentation coefficient**: 40S, 60S, 80S and larger); absorbance at $260\,\mathrm{nm}$ along the gradient gives a profile, and the distribution of a given mRNA among the fractions, measured by qPCR or sequencing, shows how many ribosomes it carries. A message whose translation is induced shifts from light to heavy fractions.

**Definition 6.6.1** The genome-wide measurement of translation in which ribosomes are arrested on mRNA, unprotected mRNA is digested with a nuclease, and the mRNA fragments of about $30$ nt protected by each ribosome are sequenced, is called **ribosome profiling** (Ingolia et al., 2009).

Each footprint marks the position of one ribosome, so the density of footprints on a coding sequence, divided by the abundance of the mRNA measured in parallel, gives its *translation efficiency*. Because ribosomes move in steps of three nucleotides, the footprint ends show a three-nucleotide periodicity that reveals the reading frame; this identified translated upstream open reading frames and short ORFs in RNAs thought to be noncoding. Drugs that stop ribosomes only at the start codon map initiation sites, and pile-ups of footprints show where ribosomes pause. Translation-arresting drugs can distort the distribution, an artifact to be controlled.

## 6.7. Sequencing Chemistry

### 6.7.1. Chain Termination

**Definition 6.7.1** The sequencing method in which a DNA polymerase copies a template from a primer in the presence of the four dNTPs and small amounts of chain-terminating 2′,3′-dideoxynucleoside triphosphates (ddNTPs), producing a set of fragments ending at every position, whose lengths and terminal bases give the sequence, is called **Sanger sequencing** (dideoxy chain-termination sequencing; Sanger et al., 1977).

A ddNTP lacks the 3′-OH needed for the next phosphodiester bond, so its incorporation ends the chain. The read-out by capillary electrophoresis with four dyes, one per ddNTP, is described in [6.4.14](/6.4.14). The ratio of ddNTP to dNTP sets the probability $q$ of termination at each position, so fragment lengths follow a **geometric distribution** with mean about $1/q$: too much terminator gives only short fragments, too little gives too few molecules ending at any one position. Engineered polymerases that incorporate ddNTPs and dNTPs with similar efficiency give even peak heights. Sanger reads are up to about $1000$ nt with an error rate near $10^{-4}$ per base; the method sequenced the first human genome and remains the standard for checking clones and mutations. The chemical cleavage method of Maxam and Gilbert, developed at the same time, is historical.

### 6.7.2. Sequencing by Synthesis

Electrophoresis reads one sample per capillary. The next generation of methods removed electrophoresis altogether: millions of template molecules are amplified in place on a surface, and the sequence is read by detecting, cycle by cycle, which nucleotide the polymerase adds to each.

**Definition 6.7.2** Sequencing in which the identity of each nucleotide incorporated by a polymerase into a growing strand is detected during synthesis, rather than by separating products by length, is called **sequencing by synthesis**.

**Definition 6.7.3** The method of sequencing by synthesis in which the four nucleotides are supplied one at a time and incorporation is detected by the pyrophosphate released, which ATP sulfurylase converts to ATP and firefly luciferase converts to light, is called **pyrosequencing** (Ronaghi et al., 1998).

The light emitted is proportional to the number of nucleotides incorporated in one flow, so a run of identical bases (a homopolymer) must be counted from the intensity of one flash; for long runs this is imprecise, and insertion–deletion errors in homopolymers are the characteristic weakness of pyrosequencing (and of semiconductor sequencing, which detects the released proton instead of light).

**Definition 6.7.4** A nucleotide with a removable blocking group on its 3′-OH, which a polymerase can incorporate but not extend until the block is removed, is called a **reversible terminator**.

The dominant short-read method combines reversible terminators with clonal amplification. Fragments with adapters at both ends are captured on a flow cell and copied in place into clusters of about a thousand identical molecules. In each cycle all four nucleotides, each with a different (or, in two-color chemistry, a combination of) fluorescent labels and a 3′ block, are supplied together; the polymerase adds exactly one to every strand, the flow cell is imaged to read the color of each cluster, and the dye and block are then chemically removed. Because exactly one base is added per cycle, homopolymers pose no difficulty and the typical errors are substitutions. Reads are limited to a few hundred bases by *phasing*: in each cycle a small fraction $p$ of the strands in a cluster fails to extend (or extends twice), and the fraction still in step after $n$ cycles is about $(1 - p)^n$, so the signal of the correct base declines and that of neighbouring bases grows. With $p = 0.5\%$, only $0.995^{150} \approx 47\%$ of the strands are in phase after $150$ cycles. Reading both ends of each fragment (paired-end sequencing) doubles the information and constrains how reads are placed on a genome; short index sequences in the adapters allow many samples to be pooled in one run.

The accuracy of each base call is reported on a logarithmic scale:

**Definition 6.7.5** The quantity $Q = -10\lg p_{\mathrm{err}}$, where $p_{\mathrm{err}}$ is the estimated probability that a base call is wrong, is called the **Phred quality score**: $Q = 20$ means an error probability of $1\%$, $Q = 30$ one of $0.1\%$.

### 6.7.3. Single-Molecule Sequencing

Clonal amplification averages over many copies but limits read length and loses modifications of the original DNA. Single-molecule methods observe one polymerase or one strand.

**Definition 6.7.6** The sequencing method in which a single polymerase fixed at the bottom of a nanometre-scale well (a zero-mode waveguide) incorporates nucleotides carrying distinct fluorophores on their terminal phosphate, each incorporation being seen in real time as a pulse of fluorescence, is called **single-molecule real-time sequencing** (SMRT).

The well, about $100\,\mathrm{nm}$ across, is smaller than the wavelength of the light, so only a volume of about $10^{-21}\,\mathrm{L}$ (a zeptolitre) at its bottom is illuminated. At a nucleotide concentration of $1\,\mu\mathrm{M}$ this volume contains on average $10^{-6} \times 6 \times 10^{23} \times 10^{-21} \approx 6 \times 10^{-4}$ free nucleotides, so the background is negligible and the nucleotide held in the active site for milliseconds stands out. The dye leaves with the pyrophosphate, so the product is natural DNA and reads of tens of kilobases are possible. Individual reads have a high rate (around $10\%$) of random insertion and deletion errors, but because the errors are random, reading a circularized molecule many times and taking the consensus gives accuracies above $99.9\%$. The kinetics of the polymerase also slow down at modified bases, so methylation is detected directly from the timing of pulses.

In **nanopore sequencing** a motor protein ratchets a single strand through a protein pore in a membrane while the ionic current through the pore is measured; the current depends on the several nucleotides inside the pore at any moment, and the sequence is decoded from the series of current levels ([6.4.6](/6.4.6)). Reads can exceed a megabase, RNA can be read directly, and modified bases change the current.

| Method | Principle | Read length | Typical error | Main use |
|---|---|---|---|---|
| Sanger | chain termination, electrophoresis | up to about 1 kb | about $10^{-4}$ | checking clones and variants |
| Pyrosequencing | light from released pyrophosphate | 0.1–0.8 kb | indels in homopolymers | historical; targeted assays |
| Reversible terminator SBS | one blocked labeled base per cycle on clusters | 50–300 nt (paired) | substitutions, about $10^{-3}$ | genomes, RNA, ChIP and accessibility assays |
| SMRT | real-time single polymerase in a zero-mode waveguide | 10–25 kb | random indels; consensus above 99.9% | assembly, isoforms, methylation |
| Nanopore | ionic current through a pore | 10 kb to above 1 Mb | systematic errors, improving | assembly, direct RNA, field use |

## 6.8. Libraries for Sequencing

### 6.8.1. Making a Library

A sequencing library is a collection of fragments carrying adapters at both ends that the sequencer recognizes. DNA is fragmented, its ends are repaired and joined to adapters (or, as in ATAC-seq, fragmented and joined in one step by a transposase, [7.2.4](/7.2.4)), and the library is amplified with primers that add the index sequences. For RNA, the poly(A) RNA is selected or ribosomal RNA removed, and the RNA is fragmented and copied into cDNA; marking the second strand allows the strand of origin to be recorded. Because amplification copies some molecules more than others, a random sequence of about $10$ nt (a *unique molecular identifier*) is often attached to each original molecule before amplification; reads that share an identifier are copies of one molecule, so molecules rather than reads can be counted. With $10$ random nucleotides there are $4^{10} \approx 10^6$ identifiers, enough that two molecules of the same RNA in one cell rarely share one.

**Definition 6.8.1** The addition of an adapter sequence to the 3′ end of a first-strand cDNA by a reverse transcriptase that, on reaching the 5′ end of the RNA, adds a few untemplated cytidines and then continues copying an oligonucleotide that pairs with them, is called **template switching**.

Template switching gives cDNA with known sequences at both ends in a single reaction and, because it occurs mainly when the enzyme reaches the capped 5′ end of the RNA, it enriches full-length copies. It made it possible to sequence the transcriptomes of single cells, where every step that loses molecules must be avoided, and it is used together with cell-specific barcodes in droplet-based single-cell methods.

### 6.8.2. Target Enrichment

Sequencing a whole genome is unnecessary when only part of it matters. In *amplicon* enrichment the targets are amplified by many PCR reactions; in *hybrid capture*, biotinylated DNA or RNA probes complementary to the targets pair with library fragments in solution, and the hybrids are recovered with streptavidin beads. The exome, the roughly $1$–$2\%$ of the human genome that is protein-coding, is the most common target: capturing it reduces the sequencing needed per sample fifty-fold or more, at the cost of uneven coverage and missed regions. Hybrid capture tolerates mismatches, which also makes it suitable for degraded or ancient DNA.

## 6.9. From Reads to Data

A sequencing experiment ends with reads, and the first design question is how many are needed.

**Definition 6.9.1** If $N$ reads of length $\ell$ are placed on a genome of length $G$, the average number of reads covering a base,
$$
c = \frac{N\ell}{G}, \tag{6.4}
$$
is called the **sequencing coverage** (depth).

If the reads are placed at random, the number covering a particular base is approximately Poisson distributed with mean $c$ (Lander and Waterman, 1988). The fraction of bases not covered at all is $\mathrm{e}^{-c}$: $37\%$ at $1\times$, $0.7\%$ at $5\times$. The fraction uncovered is not what sets the usual $30\times$ target for human genomes, however. A heterozygous site is called reliably only if each allele is seen several times, and given the total, the number of reads from each allele follows a **binomial distribution**; the probability of seeing each allele at least three times reaches about $10^{-4}$ only near $30\times$ (figure, panel B). Real coverage is also more variable than the Poisson model because of biases in fragmentation, amplification and capture. A $30\times$ human genome with $150$ nt reads requires $3.1 \times 10^9 \times 30/150 \approx 6 \times 10^8$ reads.

![Coverage statistics of shotgun sequencing. A: Poisson distribution of the number of reads covering a base at coverage 1×, 5× and 30×, with the fraction of bases left uncovered. B: fraction of the genome not covered, e^(−c), and the probability of missing a heterozygous site when at least three reads of each allele are required; the second falls to about 10⁻⁴ only near 30×](./plots/sequencing-coverage.py)

What follows, aligning reads to a reference or assembling them, calling peaks of ChIP-seq and accessibility data, quantifying expression and testing for differences, and calling variants, is the subject of [7.8](/7.8). The logic of each experiment, however, is fixed before any analysis: a sequencing read is only as informative as the molecular step that selected the fragment it came from.

## Summary

| Question | Method | What is measured | Key point |
|---|---|---|---|
| Is a sequence present; how many copies; what size? | Southern and Northern blots (Definition 6.1.1) | hybridization to fragments separated by length | stringency sets specificity; Northern gives transcript size |
| Where is it in the cell; how many molecules per cell? | FISH, single-molecule FISH (Definition 6.1.2) | fluorescent probes in situ | single-molecule counts reveal cell-to-cell variation |
| How much RNA or DNA? | qPCR (Definition 6.2.1), probes (Definition 6.2.2), digital PCR (Definition 6.2.3) | cycle at threshold; fraction of negative partitions | $C_q$ slope $-1/\lg(1+E)$, $-3.32$ at $E = 1$ (Eq. 6.1); $2^{-\Delta\Delta C_q}$ (Eq. 6.2); $\lambda = -\ln(\text{fraction negative})$ |
| How fast is it made? | run-on (Definition 6.3.1), metabolic labeling, reporter genes | label entering nascent RNA | level $\bar m = k_{\mathrm{s}}/k_{\mathrm{d}}$ conflates synthesis and decay (Eq. 6.3) |
| Where does the transcript start and end? | S1 mapping (Definition 6.4.1), primer extension (Definition 6.4.2), run-off | length of a protected or extended labeled fragment | read against a sequencing ladder |
| Which protein binds where, how tightly? | filter binding, gel shift (Definition 6.5.1), footprinting (Definition 6.5.2) | retained or retarded DNA; gap in a cleavage ladder | single-hit conditions; $K_D$ at half-shift; chemical footprints give base contacts |
| Where does it bind in living cells? | ChIP, ChIP-seq (Definition 6.5.3) | enrichment of cross-linked DNA | antibody quality and indirect contacts limit it |
| What is being translated? | polysome profiling, ribosome profiling (Definition 6.6.1) | ribosome-protected fragments | translation efficiency; three-nucleotide periodicity reveals frames |
| What is the sequence? | Sanger (Definition 6.7.1), pyrosequencing (Definition 6.7.3), reversible terminators (Definitions 6.7.2, 6.7.4), SMRT (Definition 6.7.6), nanopore | termination, released pyrophosphate, one blocked base per cycle, real-time single molecules, ionic current | phasing $(1-p)^n$ limits short reads; $Q = -10\lg p_{\mathrm{err}}$ (Definition 6.7.5); consensus overcomes random single-molecule errors |
| How to prepare and focus the experiment? | libraries, UMIs, template switching (Definition 6.8.1), target capture | adapters, molecular identifiers, full-length cDNA | coverage $c = N\ell/G$ (Definition 6.9.1), uncovered fraction $\mathrm{e}^{-c}$ |

## Questions

1. Two RNAs give equal bands on a Northern blot. After transcription is blocked, one disappears with a half-life of $10$ min and the other with $5$ h. Compare their synthesis rates.

   **Answer** Equal steady-state levels mean $k_{\mathrm{s}}/k_{\mathrm{d}}$ is the same (Eq. 6.3), so $k_{\mathrm{s}} \propto k_{\mathrm{d}} = \ln 2/t_{1/2}$. The short-lived RNA is made $300/10 = 30$ times faster. A run-on assay would show a thirtyfold stronger signal for it.
2. A dilution series in qPCR gives a slope of $-3.6$. What is the efficiency, and by what factor does it change the apparent fold difference between two samples that differ by $5$ cycles if one wrongly assumes $E = 1$?

   **Answer** $E = 10^{1/3.6} - 1 \approx 0.90$. The true ratio is $1.90^5 \approx 24.8$, while assuming doubling gives $2^5 = 32$; the assumption overestimates the difference by about $30\%$.
3. In a digital PCR experiment with $20\,000$ partitions, $12\,000$ are negative. How many template molecules were loaded?

   **Answer** The fraction negative is $0.6$, so $\lambda = -\ln 0.6 \approx 0.51$ molecules per partition, and the total is $0.51 \times 20\,000 \approx 1.0 \times 10^4$ molecules. Counting positive partitions alone ($8000$) would underestimate the number, because some positive partitions contain more than one molecule.
4. In an S1 mapping experiment the probe is labeled $250$ nt downstream of a candidate start site, inside the gene. RNA from liver protects a $250$ nt fragment, RNA from brain protects fragments of $250$ and $180$ nt. Interpret the result.

   **Answer** Liver transcripts start at the candidate site, $250$ nt upstream of the label. Brain uses the same start and a second one $180$ nt upstream of the label, that is, $70$ nt downstream of the first: the gene has a second, brain-specific start site (or promoter). The relative intensities of the bands give the relative use of the two sites.
5. Why must DNase I footprinting be done under conditions where each DNA molecule is cut on average less than once?

   **Answer** Only the fragment carrying the label is seen, and it ends at the cut nearest to the label. With many cuts per molecule nearly every labeled fragment is short, so positions far from the label, including a footprint there, are never represented; the ladder is uniform enough to read only when most molecules are cut at most once, so that each labeled fragment reports a single random cut.
6. A gel shift with a nuclear extract gives a retarded band. How would you show that the band contains a specific protein, and that its binding is sequence-specific?

   **Answer** Add an antibody against the protein: if the band is further retarded (supershifted) or abolished, the protein is in the complex. Add excess unlabeled competitor DNA: the same sequence should compete the band away at low excess, whereas an unrelated or mutated sequence should compete poorly; this distinguishes specific from nonspecific binding.
7. In reversible-terminator sequencing the fraction of strands that fail to extend is $0.3\%$ per cycle and the fraction that extend twice is $0.1\%$. Roughly what fraction of a cluster is still in phase after $250$ cycles, and why does this limit read length?

   **Answer** About $(1 - 0.004)^{250} \approx \mathrm{e}^{-1} \approx 0.37$. The out-of-phase strands emit the colors of neighbouring positions, so the correct signal is diluted and contaminated; as the in-phase fraction falls, base-call quality falls, which sets a practical limit of a few hundred cycles.
8. Why can random errors of single-molecule reads be removed by consensus, while systematic errors cannot?

   **Answer** Random errors occur at different positions in different passes of the same molecule, so the correct base is the majority at each position, and the probability that most of $n$ passes err at the same position falls rapidly with $n$ (binomially). A systematic error, such as a consistently miscalled homopolymer length or sequence context, recurs in every pass and every molecule, so averaging reinforces it; it must be corrected by better chemistry or by a model of the error.
9. How many $2 \times 150$ nt read pairs are needed to sequence a $3.1$ Gb genome to $30\times$, and what fraction of the genome would remain uncovered under the Poisson model?

   **Answer** Each pair gives $300$ nt, so $N = 30 \times 3.1 \times 10^9/300 \approx 3.1 \times 10^8$ pairs. The uncovered fraction is $\mathrm{e}^{-30} \approx 10^{-13}$, about $0.3$ bases of the genome; in practice regions that are hard to fragment, amplify or map remain uncovered, which is why real coverage is less uniform than the Poisson model.
