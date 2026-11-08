---
title: Proteomics and Metabolomics
description: "Measuring proteins and metabolites at scale: proteoforms and the dynamic range of the proteome; gels and liquid chromatography; what mass spectrometry contributes (ionization, analyzers, resolution, charge states); peptide identification by b/y ions, database search, probability scores, the target–decoy estimate of the false discovery rate, q-values and protein inference; label-free, SILAC and isobaric quantification, ratio compression, DDA and DIA, and missing values that are not missing at random; phosphoproteomics, site localization and kinase activity; affinity proteomics, single-cell and single-molecule methods; and metabolomics: targeted and untargeted LC-MS, GC-MS and NMR, feature tables, levels of annotation and isotope tracing with natural-abundance correction."
---

Transcriptomes tell us which genes a cell is prepared to use; proteins and metabolites are what it actually uses. Enzymes, receptors, transporters and structural proteins do the work of the cell, and their abundance, modification state, location and partners determine what that work is. Metabolites are the substrates, products and signals of this work, and the layer of molecular data closest to the phenotype. This chapter describes how both layers are measured at scale and how the measurements become numbers that can be analyzed statistically. Most of the technology is **mass spectrometry**, whose physics, ion sources, analyzers and basic peptide fragmentation are treated in [6.4.15](/6.4.15) and the separations in front of it in [6.4.14](/6.4.14); the classical methods of protein chemistry are in [7.1.4](/7.1.4). Here we take the instruments as given and concentrate on what is specific to proteomes and metabolomes: identification as a large-scale statistical inference, quantification and its biases, modifications and their localization, and the integration of the results with the other omics layers.

The chapter follows the path of a sample: why proteins must be measured directly (9.1), how they are separated (9.2) and ionized and weighed (9.3), how peptides are identified with a controlled error rate (9.4), how they are quantified (9.5), how modifications are found (9.6), what proteomics looks like at the scale of tissues, populations and single cells (9.7), and how the same instruments measure metabolites (9.8). The statistics used are those of [7.7](/7.7) and of the **false discovery rate** ([7.7.20](/7.7.20)); proteins whose interactions are measured by mass spectrometry are the subject of the next chapter, [7.9.10](/7.9.10), and imaging of proteins and metabolites in tissue sections is in [7.9.6](/7.9.6).

## 9.1. Why Measure Proteins

The **proteome** is not a translation of the **transcriptome**. Across genes, mRNA levels explain roughly half of the variance of protein levels in steady state, because translation rates and protein lifetimes vary by orders of magnitude between genes ([7.9.4](/7.9.4#sec-4.4.4)); after a perturbation, protein levels lag behind mRNA by hours to days. In a deep comparison of $29$ healthy human tissues, RNA sequencing quantified $18\,072$ protein-coding genes and mass spectrometry $13\,640$ proteins; the ranges and the tissue specificity of the two layers differed markedly (Wang and colleagues, 2019). And many of the properties that matter for function are invisible in RNA: proteolytic processing, **post-translational modification**, the assembly into complexes and the location in the cell.

One gene gives many molecular forms of its product. Alternative splicing ([7.9.4](/7.9.4)), alternative start sites, signal-peptide removal and proteolytic maturation change the sequence; phosphorylation, acetylation, glycosylation, ubiquitination and hundreds of other modifications decorate it in combinations.

**Definition 9.1.1 (Proteoform)** A **proteoform** is one defined molecular form of a protein: a particular amino acid sequence, resulting from a particular allele, splice isoform and processing, carrying a particular combination of covalent modifications at particular sites (Smith and Kelleher, 2013).

A protein with five phosphorylation sites can exist in $2^5 = 32$ phosphorylation states alone; the number of proteoforms in a human cell is unknown but certainly much larger than the number of genes. Most proteomics measures peptides, not proteoforms (9.4), and so describes each protein by summary quantities: total abundance and the occupancy of individual sites.

The second difficulty is range. In a human cell the most abundant proteins (histones, ribosomal proteins, glycolytic enzymes, cytoskeleton) are present at $10^7$–$10^8$ copies and transcription factors at $10^3$–$10^4$, so that the copy numbers of expressed proteins span about seven orders of magnitude. In blood plasma, albumin is present at about $40\,\mathrm{g\,L^{-1}}$ and cytokines such as interleukin 6 at a few $\mathrm{ng\,L^{-1}}$, a range of more than ten orders of magnitude (Anderson and Anderson, 2002). Proteins cannot be amplified like nucleic acids, so every protein must be detected from the molecules that are in the sample, against the background of the abundant ones. The design of proteomic experiments is largely a strategy against this range: separation before detection, enrichment of subsets, depletion of abundant proteins, and targeted acquisition.

## 9.2. Separation

Separation spreads a complex mixture over a dimension of space or time, so that the detector sees fewer molecules at once.

**Two-dimensional gel electrophoresis** (O'Farrell, 1975) separates proteins by **isoelectric focusing** in the first dimension and by size in SDS gels in the second ([6.4.14](/6.4.14#sec-14.5.6), [7.1.4](/7.1.4)), resolving up to a few thousand spots on one gel. Difference gel electrophoresis (DIGE) labels two or three samples with different fluorescent dyes (Cy2, Cy3, Cy5) and runs them on the same gel, which removes the gel-to-gel variation that made comparisons between gels unreliable; the spots are then cut out, digested and identified by mass spectrometry. Gels resolve intact proteoforms, which is their remaining strength, but they lose membrane proteins (which are insoluble during focusing), very large, very small and very basic proteins, and low-abundance proteins; spots often contain several proteins, so that an intensity change can belong to any of them. For proteome-wide work, gels have been replaced by liquid chromatography of peptides.

**Reversed-phase chromatography** of peptides on C18 columns, with an acetonitrile gradient over one to two hours at nanoliter-per-minute flow ([6.4.14](/6.4.14#sec-14.3.3)), separates a tryptic digest by hydrophobicity and delivers the peptides directly into the ion source of the mass spectrometer (LC-MS/MS). The retention time is reproducible to within a fraction of a minute, so it becomes a coordinate of the measurement, used to align runs and, increasingly, predicted from the sequence by machine learning. Deeper coverage is obtained by fractionating the digest beforehand (for example by high-pH reversed-phase chromatography into $8$–$24$ fractions), at the cost of more instrument time per sample; ion mobility separation inside the instrument adds a further dimension within seconds.

## 9.3. Mass Spectrometry for Proteomics

### 9.3.1. Ions from Peptides

Two soft ionization methods made proteomics possible, recognized by the 2002 Nobel Prize in Chemistry to John Fenn and Koichi Tanaka. **Electrospray ionization** ([6.4.15](/6.4.15#sec-15.2.4)) produces multiply protonated ions $[\mathrm{M}+z\mathrm{H}]^{z+}$ from a liquid stream and therefore couples naturally to chromatography; tryptic peptides, with a basic C-terminal residue and a free N-terminus, mostly carry $z = 2$ or $3$. **Matrix-assisted laser desorption/ionization** ([6.4.15](/6.4.15#sec-15.2.6)) produces mostly singly charged ions from a dried spot; it is used for **peptide mass fingerprinting** of purified proteins, for microbial identification from whole-cell spectra in clinical laboratories, and for **mass spectrometry imaging** ([7.9.6](/7.9.6#sec-6.5.2)).

The mass analyzers used in proteomics are quadrupoles (as mass filters to select precursors), ion traps, **time-of-flight mass spectrometry** and the **Orbitrap**, usually combined in hybrid instruments for **tandem mass spectrometry**: a quadrupole selects a precursor, a collision cell fragments it, and an Orbitrap or time-of-flight analyzer records the fragments ([6.4.15](/6.4.15#sec-15.3)). What proteomics requires of them is resolution (to separate the isotope peaks of multiply charged ions and co-eluting peptides of nearly equal mass), mass accuracy of a few parts per million (to restrict the candidate peptides) and speed (tens of fragment spectra per second, to keep up with the peptides eluting from the column).

### 9.3.2. Charge States

An ion is measured at its mass-to-charge ratio, not its mass. For a molecule of neutral monoisotopic mass $M$ carrying $z$ protons,
$$
m/z = \frac{M + z\,m_{\mathrm{H}^+}}{z}, \qquad m_{\mathrm{H}^+} = 1.007\,276. \tag{9.1}
$$
The charge must therefore be determined before the mass can be known. Two patterns in the spectrum reveal it.

**Formula 9.3.1 (Charge from Isotope Spacing and from Adjacent Charge States)** (a) The **isotope peaks** of an ion are separated by $\Delta_{\mathrm{C}}/z$, where $\Delta_{\mathrm{C}} = 1.003\,355$ is the mass difference between $^{13}\mathrm{C}$ and $^{12}\mathrm{C}$; a spacing $\delta$ between neighboring isotope peaks gives
$$
z = \frac{\Delta_{\mathrm{C}}}{\delta}. \tag{9.2}
$$
(b) If two neighboring peaks of an electrospray envelope at $m_1 < m_2$ belong to the same molecule with charges $z$ and $z - 1$, then
$$
z = \frac{m_2 - m_{\mathrm{H}^+}}{m_2 - m_1}, \qquad M = z\,(m_1 - m_{\mathrm{H}^+}). \tag{9.3}
$$

Both follow from Eq. (9.1): (a) because adding one neutron's worth of mass, $\Delta_{\mathrm{C}}$, moves the peak by $\Delta_{\mathrm{C}}/z$; (b) by solving $z(m_1 - m_{\mathrm{H}^+}) = (z-1)(m_2 - m_{\mathrm{H}^+})$ for $z$.

**Example 9.3.1** (a) A peptide shows isotope peaks $0.502$ apart: $z = 1.003\,355/0.502 = 2.0$, a doubly charged ion; triply charged ions have spacings of $0.334$. Resolving such peaks at $m/z \approx 1000$ requires a resolving power well above $1000/0.33 \approx 3000$, and in practice tens of thousands. (b) A protein gives neighboring peaks at $m_1 = 1071.007$ and $m_2 = 1189.896$. Then $z = (1189.896 - 1.007)/(1189.896 - 1071.007) = 1188.889/118.889 = 10.00$, so the first peak is the $10+$ ion and $M = 10 \times (1071.007 - 1.007) = 10\,700.0$. Deconvolution software does the same for all peaks of an envelope at once ([6.4.15](/6.4.15#ex-15.2.1) works the case of myoglobin).

### 9.3.3. Acquisition

In data-dependent acquisition the instrument records a survey spectrum (MS1) of all ions eluting at a moment, selects the most intense precursors in turn for fragmentation (MS2) and excludes each selected precursor for some seconds; a modern instrument records several survey scans and tens of fragment spectra per second. Selection by intensity is stochastic near the detection limit, so a peptide fragmented in one run may be missed in the next, the main origin of missing values in label-free data (9.5.4). Data-independent acquisition, which fragments everything, is described in 9.5.3.

## 9.4. Peptide Identification

### 9.4.1. Digestion and Fragmentation

In bottom-up proteomics, proteins are reduced, alkylated (cysteines carry a carbamidomethyl group, $+57.021$) and digested with trypsin, which cleaves after lysine and arginine. A human proteome yields some $10^6$ distinct tryptic peptides of useful length ($7$–$30$ residues), of which a single run identifies tens of thousands. Collision-induced or higher-energy collisional dissociation breaks the peptide bonds and produces b ions, which contain the N-terminus, and y ions, which contain the C-terminus ([6.4.15](/6.4.15#eq-15.11)). For a peptide of residues with masses $m_1, \dots, m_n$,
$$
m(\mathrm{b}_i) = \sum_{k \le i} m_k + m_{\mathrm{H}^+}, \qquad m(\mathrm{y}_j) = \sum_{k > n - j} m_k + m(\ce{H2O}) + m_{\mathrm{H}^+}
$$
for singly charged fragments, and $m(\mathrm{b}_i) + m(\mathrm{y}_{n-i}) = M + 2m_{\mathrm{H}^+}$: each cleaved bond gives a complementary pair.

**Example 9.4.1** The tryptic peptide HLVDEPQNLIK has monoisotopic mass $M = 1304.709$ and is observed as $[\mathrm{M}+2\mathrm{H}]^{2+}$ at $m/z\ 653.362$. Its b ions run from $\mathrm{b}_1 = 138.066$ (His) to $\mathrm{b}_{10} = 1159.611$, its y ions from $\mathrm{y}_1 = 147.113$ (Lys) to $\mathrm{y}_{10} = 1168.657$; $\mathrm{b}_3 + \mathrm{y}_8 = 350.219 + 956.505 = 1306.723 = M + 2m_{\mathrm{H}^+}$. In the simulated spectrum of the figure the y series $\mathrm{y}_2$–$\mathrm{y}_7$ is complete: the differences $373.281 - 260.197 = 113.084$, $114.043$, $128.059$, $97.053$ and $129.043$ are the residue masses of Leu (or Ile), Asn, Gln, Pro and Glu, which reads the sequence …EPQNL… backwards from the C-terminus. Leucine and isoleucine have the same mass and cannot be distinguished this way.

![Fragment ions of the tryptic peptide HLVDEPQNLIK. A: each peptide bond, when broken, gives a b ion (blue; N-terminal fragment, numbered from the left) and a y ion (red; C-terminal fragment, numbered from the right), with their singly charged m/z. B: a simulated fragment spectrum with 14 of the 20 b and y ions (b1, b3–b6, b8, b10, y2–y7, y10) among 46 noise peaks; y ions are usually the stronger for tryptic peptides, whose C-terminal Lys or Arg holds the charge](./plots/by_ions.py)

### 9.4.2. Matching Spectra to Sequences

Spectra are interpreted by comparison with a database of the protein sequences predicted from the genome. The search engine digests every protein in silico, keeps the peptides whose mass agrees with the precursor within the tolerance (a few ppm), predicts their fragment ions, and scores how well each candidate explains the spectrum.

**Definition 9.4.1 (Peptide-Spectrum Match)** A **peptide-spectrum match** (PSM) is the assignment of a fragment spectrum to the candidate peptide sequence (with its modifications and charge) that best explains it, together with a score measuring the quality of the match.

Scores differ between search engines: the cross-correlation of observed and predicted spectra (SEQUEST; Eng, McCormack and Yates, 1994), probability-based scores (Mascot, Andromeda), hyperscores built from matched intensities (X!Tandem), and spectral similarity to libraries of observed or, increasingly, predicted spectra. The idea behind probability-based scores is the simplest.

**Formula 9.4.1 (Probability-Based Score)** Let a candidate peptide have $n$ predicted fragment ions, and let $p$ be the probability that a predicted ion matches a peak of the spectrum by chance (approximately the number of peaks times the width $2\varepsilon$ of the tolerance window, divided by the mass range). If $k$ of the $n$ ions match, the probability of at least $k$ chance matches is the binomial tail
$$
P = \sum_{j=k}^{n} \binom{n}{j} p^j (1-p)^{n-j}, \qquad \text{score} = -10 \log_{10} P. \tag{9.4}
$$

**Example 9.4.2** For HLVDEPQNLIK ($n = 20$ b and y ions) in a spectrum of $60$ peaks between $m/z$ $150$ and $1300$, a tolerance of $\pm 0.02$ gives $p = 60 \times 0.04/1150 = 0.0021$. Fourteen matches give $P = 1.1\times10^{-33}$ and a score of $329$; a random peptide of the same precursor mass would match on average $np = 0.04$ ions. With a low-resolution tolerance of $\pm 0.5$, $p = 0.052$, a random peptide matches about one ion and the same $14$ matches give $P = 3.2\times10^{-14}$ (score $135$). High fragment-mass accuracy is thus worth some $20$ orders of magnitude of evidence per spectrum.

:::

The P of Eq. (9.4) is a p-value for one candidate; but each spectrum is compared with thousands of candidates, the matches of different candidates are dependent, and the binomial model ignores the intensities and the correlations between ions. Scores are therefore treated as ranking statistics whose error rates are calibrated empirically, by the method of decoys.

### 9.4.3. The Target–Decoy Approach

**Definition 9.4.2 (Target–Decoy Approach)** In the **target–decoy approach** the spectra are searched against a database containing, besides the real (target) protein sequences, the same number of decoy sequences that cannot be present in the sample, usually the reversed or shuffled target sequences. Each spectrum keeps its best match, target or decoy. Since a spectrum without a correct candidate is equally likely to match its best random partner among targets or among decoys, the number of decoy matches above a score threshold estimates the number of incorrect target matches above it (Elias and Gygi, 2007).

**Formula 9.4.2 (FDR and q-Value from Decoys)** With $T(t)$ target and $D(t)$ decoy PSMs scoring at least $t$, the false discovery rate of the target PSMs accepted at threshold $t$ is estimated by
$$
\widehat{\mathrm{FDR}}(t) = \frac{D(t)}{T(t)} \tag{9.5}
$$
(or $(D(t) + 1)/T(t)$, a slightly conservative version). The q-value of a PSM with score $s$ is the smallest estimated FDR of any threshold that accepts it, $q(s) = \min_{t \le s} \widehat{\mathrm{FDR}}(t)$. Accepting all PSMs with $q \le 0.01$ controls the FDR at $1\%$.

The decoys must resemble the targets in everything except correctness: same length distribution, same amino acid composition, same number of tryptic peptides, same mass distribution. Reversal preserves these properties. The estimate assumes that an incorrect match is equally likely to be a target or a decoy, which holds for spectra from peptides absent from the database (unexpected modifications, nontryptic cleavages, chimeric spectra) and for spectra too poor to be identified.

**Example 9.4.3** In the simulation of the figure, $20\,000$ spectra are searched; $11\,944$ come from peptides in the database. Ranking all best matches by score, the q-value threshold of $0.01$ is reached at a score of $31.4$, accepting $6406$ target PSMs and $64$ decoys ($64/6406 = 1.0\%$). The true proportion of incorrect PSMs among the accepted targets, known only in the simulation, is $1.01\%$: the decoys estimate it accurately at every threshold (panel B). Only $6406$ of the $11\,312$ spectra whose best match is correct are accepted: the price of a $1\%$ error rate is that correct matches with low scores are lost.

![Target–decoy estimation of the false discovery rate (simulation of 20 000 spectra, 60% from peptides in the database; random best matches follow a Gumbel distribution, correct matches a normal distribution). A: scores of the accepted target matches, correct and incorrect, and of the decoy matches, whose distribution mirrors that of the incorrect targets. B: estimated FDR (decoys/targets above the threshold) and the true false discovery proportion. C: the number of target matches accepted as a function of the q-value threshold; dashed: 1%](./plots/target_decoy.py)

:::

Several refinements are standard. Percolator (Käll and colleagues, 2007) trains a classifier, a support vector machine, on many features of each PSM (score, mass error, charge, missed cleavages, retention-time agreement), using decoys as negatives and high-scoring targets as positives, which separates correct from incorrect matches better than any single score; the decoys used for training must then not be the ones used for FDR estimation, which is handled by cross-validation. The posterior error probability (PEP) of an individual PSM, the probability that this match is wrong, is estimated by fitting a **finite mixture model** of correct and incorrect score distributions with the **EM algorithm** (PeptideProphet; Keller and colleagues, 2002): the q-value is a property of a list, the PEP of a single match. FDR is controlled separately at the levels of PSMs, peptides and proteins, because errors accumulate differently: an incorrect protein is typically supported by a single incorrect PSM, whereas a correct protein collects many correct ones, so a $1\%$ PSM-level FDR can mean a much higher protein-level FDR in large data sets.

### 9.4.4. Protein Inference

Peptides are identified; proteins must be inferred from them. A peptide can be shared among several proteins (paralogs, splice isoforms), and a protein may be supported only by shared peptides.

**Algorithm 9.4.1 (Parsimonious Protein Inference)** Given the bipartite graph of identified peptides and the database proteins that contain them:

1. Group proteins with identical sets of identified peptides into one protein group (they cannot be distinguished).
2. Remove groups whose peptide set is a proper subset of another group's (subsumable groups).
3. Choose a smallest set of groups that explains every identified peptide: a set cover, solved greedily by repeatedly adding the group that explains most still-unexplained peptides.
4. Report the chosen groups, flagging those supported only by shared peptides.

Set cover is NP-hard in general, but the greedy algorithm is fast and nearly optimal on the small connected components of real peptide–protein graphs. Parsimony is Occam's razor, not a fact: a protein that explains no peptide uniquely may still be present. Probabilistic methods (ProteinProphet, Fido) instead estimate for each protein the probability of presence given the peptide probabilities.

**Example 9.4.4** Peptides $p_1, p_2$ occur only in protein A, $p_3$ in A and B, $p_4$ in B and C, and $p_5$ only in C. Protein A explains $\{p_1, p_2, p_3\}$, B explains $\{p_3, p_4\}$, C explains $\{p_4, p_5\}$. Greedy cover selects A (three peptides), then C ($p_4, p_5$); B explains nothing that A and C do not, and is not reported, although the data do not exclude it. If $p_5$ had not been identified, B and C would explain the same remaining peptide $p_4$ and would form an ambiguous pair.

### 9.4.5. Beyond the Database

Database search can only find what is in the database. Peptides from unannotated open reading frames, sequence variants, unexpected modifications or organisms without a reference require other strategies. Proteogenomics searches databases built from the sample's own genome and transcriptome (variants, splice junctions, translated noncoding RNAs found by **ribosome profiling**, [7.9.4](/7.9.4)), with stricter FDR control because the enlarged database contains more wrong candidates. Open searches allow any precursor mass shift and discover modifications from the distribution of mass differences. De novo sequencing reads the sequence from the ladders of fragment masses without a database, as in Example 9.4.1; deep learning models (such as Casanovo, trained on millions of identified spectra) now reach useful accuracy. Deep learning also predicts the fragment intensities and retention times of any peptide (Prosit; Gessulat and colleagues, 2019), which improves scoring and is the basis of library-free data-independent acquisition (9.5.3). Top-down proteomics measures intact proteins and is the only way to observe proteoforms directly, at a much lower throughput.

## 9.5. Quantification

Mass spectrometry is not quantitative across molecules: the signal of a peptide depends on its ionization efficiency, which differs by orders of magnitude between sequences. All quantitative proteomics therefore compares the same peptide across samples, or a peptide with an isotope-labeled copy of itself.

### 9.5.1. Label-Free Quantification

In label-free quantification each sample is run separately and the same peptide is compared across runs, either by the area of its MS1 elution peak (intensity-based quantification) or by the number of its fragment spectra (spectral counting, cruder and saturating at high abundance). Runs are aligned by retention time, signals are transferred between runs for peptides identified in only some of them ("match between runs", with its own FDR), intensities are normalized (by medians, or by assuming that most proteins do not change), and peptide intensities are combined into protein intensities, for example by the MaxLFQ algorithm (Cox and colleagues, 2014), which uses ratios between pairs of samples to be robust to peptides missing in some runs. Label-free designs allow any number of samples and are the standard for clinical cohorts, at the cost of run-to-run variation and missing values (9.5.4). Absolute amounts across proteins can be approximated by intensity-based absolute quantification (iBAQ), the summed intensity divided by the number of theoretically observable peptides, or by adding labeled peptides of known amount (**isotope dilution**, the AQUA method), as in targeted assays by **selected reaction monitoring**.

### 9.5.2. Stable-Isotope Labeling

Labels make samples distinguishable inside one run, so that they are compared under identical conditions of chromatography and ionization.

**Definition 9.5.1 (SILAC)** **SILAC** (stable isotope labeling by amino acids in cell culture; Ong and colleagues, 2002) is metabolic labeling in which cells are grown for several divisions in media containing light or heavy forms of essential amino acids, usually $^{13}\mathrm{C}_6{}^{15}\mathrm{N}_2$-lysine ($+8.014$) and $^{13}\mathrm{C}_6{}^{15}\mathrm{N}_4$-arginine ($+10.008$), until their proteins are fully labeled; the samples are mixed at the level of cells or lysates and each peptide appears as a light–heavy pair of MS1 peaks whose intensity ratio is the ratio of its abundance in the two samples.

Because trypsin cleaves after Lys and Arg, almost every tryptic peptide contains exactly one labeled residue, and the pair of a doubly charged peptide is separated by $8.014/2 = 4.007$ (Lys) or $10.008/2 = 5.004$ (Arg) in $m/z$. Mixing at the earliest step means that all later handling affects both samples equally, which makes SILAC the most precise labeling method. It is limited to cells that can be grown in defined media (and to animals fed labeled diets) and to two or three samples per run. Pulsed SILAC, in which the label is switched during the experiment, measures synthesis and degradation: the heavy fraction of a protein after time $t$ gives its turnover rate, the protein-level analogue of the RNA labeling of [7.9.4](/7.9.4#sec-4.5).

**Definition 9.5.2 (Isobaric Labeling)** In **isobaric labeling** the peptides of each sample are chemically labeled at their amino groups with one of a set of tags (TMT, tandem mass tags; iTRAQ) that have the same total mass but distribute their heavy isotopes differently between a reporter group and a balancer group; the labeled samples are pooled, the same peptide from all samples appears as one MS1 peak, and fragmentation releases reporter ions of distinct masses (in TMT around $m/z\ 126$–$135$) whose intensities give the relative abundances of the peptide in the samples.

Isobaric labeling multiplexes up to $18$ samples (TMTpro) in one run, which removes missing values within a set and saves instrument time; designs with more samples combine several sets through a common reference channel. Its systematic weakness is interference.

**Formula 9.5.1 (Ratio Compression)** Let the isolation window of a precursor contain, besides the target peptide, co-isolated ions that make up a fraction $\phi$ of the reporter signal and are present equally in two channels. If the true ratio of the target between the channels is $R$, the observed reporter ratio is
$$
R_{\mathrm{obs}} = \frac{(1-\phi)\dfrac{R}{1+R} + \dfrac{\phi}{2}}{(1-\phi)\dfrac{1}{1+R} + \dfrac{\phi}{2}}, \tag{9.6}
$$
which lies between $1$ and $R$: all ratios are compressed towards $1$.

**Example 9.5.1** A protein increases fourfold ($R = 4$, $\log_2 R = 2$). With $\phi = 0.1$ the observed ratio is $3.35$ ($\log_2 = 1.74$), with $\phi = 0.3$ it is $2.45$ ($\log_2 = 1.29$) and with $\phi = 0.5$ only $1.86$ ($\log_2 = 0.89$). In the simulation of the figure, with interference fractions drawn from $\mathrm{Beta}(2, 5)$, the median observed $\log_2$ ratio of fourfold-changed peptides is $1.34$ in MS2-based quantification; reducing interference to a mean of $0.05$, as MS3 methods do, raises it to $1.90$.

![Ratio compression in isobaric labeling. A: observed against true log2 ratio when a fraction φ of the reporter signal comes from co-isolated peptides that are 1:1 between the channels (Eq. (9.6)). B: simulated distributions of observed log2 ratios for unchanged peptides (left peak) and fourfold-changed peptides (right), with interference typical of MS2 quantification (orange, φ ~ Beta(2, 5)) and after MS3 with synchronous precursor selection (blue, φ ~ Beta(1, 20)); dashed: the true log2 ratio of 2](./plots/ratio_compression.py)

:::

Compression does not create false positives among unchanged proteins, but it shrinks effect sizes, reduces power and distorts comparisons with other data. It is reduced by narrow isolation windows, by isolating the precursor in a second stage before releasing the reporters (MS3 with synchronous precursor selection; Ting and colleagues, 2011; McAlister and colleagues, 2014), by ion mobility, and by computational corrections based on the measured purity of each isolation.

### 9.5.3. Data-Independent Acquisition

**Definition 9.5.3 (Data-Independent Acquisition)** In **data-independent acquisition** (DIA) the mass spectrometer fragments, cycle after cycle, all precursors within a series of predefined isolation windows covering the whole precursor range (for example $40$ windows of $15$–$25\,\mathrm{Th}$), independently of what is detected in the survey scan; the resulting multiplexed fragment spectra are deconvolved by extracting, for each peptide, the chromatograms of its expected fragment ions and testing whether they co-elute.

DIA, introduced at proteome scale as SWATH-MS (Gillet and colleagues, 2012), trades the clean spectra of data-dependent acquisition for completeness: every peptide is fragmented in every cycle of every run, so its quantity can be read in every sample, and missing values become much rarer. The spectra are chimeric by design, and identification requires either a spectral library from data-dependent runs or, now usually, libraries predicted by deep learning from the sequence database (DIA-NN; Demichev and colleagues, 2020); the FDR is still controlled by decoys, here decoy peptides whose fragment chromatograms are extracted in the same way. DIA has become the standard for large label-free cohorts.

### 9.5.4. Missing Values and Statistical Analysis

Missing values are the defining statistical problem of label-free proteomics. In a typical data-dependent data set, $20$–$50\,\%$ of the protein-by-sample matrix is empty, and the values are not missing at random: a peptide is missed mostly because its abundance is near the detection limit, or because the instrument chose other precursors.

The mechanism matters for analysis. If missing values were missing completely at random, the observed values would be an unbiased sample and could be analyzed as they are. If they are left-censored, the observed values of a low-abundance protein are its larger ones, and ignoring the missing values biases its mean upwards and its fold changes towards zero.

**Formula 9.5.2 (Left-Censored Normal Likelihood)** If the log intensities $x_1, \dots, x_n$ of a protein in a group are $\mathcal{N}(\mu, \sigma^2)$ and values below a detection limit $L$ are not observed, with $o$ observed values and $c$ missing ones, the log-likelihood of $\mu$ and $\sigma$ is
$$
\ell(\mu, \sigma) = \sum_{i \in \text{observed}} \log \frac{1}{\sigma}\varphi\!\left(\frac{x_i - \mu}{\sigma}\right) + c \log \Phi\!\left(\frac{L - \mu}{\sigma}\right), \tag{9.7}
$$
where $\varphi$ and $\Phi$ are the standard normal density and distribution function. The missing values count as evidence that the intensity was below $L$ (a Tobit model; the same likelihood of **censoring** is used in survival analysis, [7.7.16](/7.7.16), with the opposite tail).

**Example 9.5.2** In the simulation of the figure, intensities below $L = 20$ (log scale) are lost, plus $3\%$ of values at random, giving $12\%$ missing values in a sample. For proteins with a true fourfold decrease ($\log_2$ fold change $-2$) and control abundance between $20$ and $21.5$, the complete-case estimate averages $-1.17$, imputation by random draws from a normal distribution shifted $1.8$ standard deviations below the observed mean (a common default) $-0.94$, and the censored likelihood (with known $\sigma$) $-1.58$. For abundant proteins (above $24$) all three give about $-1.9$. Among all $600$ proteins, $31\%$ had no observed value in one group, so that only the imputation method returned a number for them, and that number is driven by the imputed distribution rather than by the data.

![Missing values in label-free proteomics are not missing at random (simulation). A: true log2 intensities of 3000 proteins in one sample and those observed when values below a detection limit of 20 are lost (plus 3% at random). B: estimates of a true log2 fold change of −2 between two groups of 4 samples, against abundance in the control group: complete-case means, down-shifted random imputation and the left-censored likelihood of Eq. (9.7); lines are running means over 60 proteins. Proteins with no observed value in a group have no complete-case or censored estimate](./plots/missing_values.py)

:::

The practical consequences are: report the missingness pattern; filter proteins that are quantified in too few samples per group; analyze present/absent patterns separately (a protein detected in all treated and no control samples is a qualitative finding, not a fold change); prefer acquisition schemes with few missing values (DIA, isobaric labeling); and when imputing, use methods that match the mechanism and propagate uncertainty, for example multiple imputation or censored likelihoods. After these steps the statistics are those of other omics: log transformation, normalization, linear models with moderated variances (limma, the empirical Bayes shrinkage of [7.7.20](/7.7.20)), and FDR control across proteins. Peptide-level models (MSstats; Choi and colleagues, 2014) fit each protein from its peptides with run and feature effects, which uses the information of each peptide and accounts for missing features.

## 9.6. Post-Translational Modifications

### 9.6.1. Enrichment

A modification changes the mass of a residue by a defined amount: phosphorylation $+79.966$, acetylation $+42.011$, methylation $+14.016$, and the GlyGly remnant left on a lysine by trypsin digestion of a **ubiquitin**-modified protein, $+114.043$. A search engine can therefore look for modified peptides by allowing these mass shifts as variable modifications. The difficulty is abundance: most sites are modified on a small fraction of the molecules, often transiently, and modified peptides are a small minority of a digest. Modification proteomics therefore begins with enrichment of the modified peptides.

| Modification | Enrichment | Notes |
|---|---|---|
| Phosphorylation (Ser, Thr, Tyr) | immobilized metal affinity chromatography (IMAC, $\ce{Fe^3+}$ or $\ce{Ti^4+}$), metal oxides ($\ce{TiO2}$); anti-phosphotyrosine antibodies | the phosphate binds the positively charged metal; pTyr is about $1\%$ of sites and needs antibodies |
| Ubiquitination (Lys) | antibodies against the K-ε-GG remnant | detects sites of ubiquitin and of NEDD8 and ISG15, which leave the same remnant |
| Acetylation (Lys) | anti-acetyllysine antibodies | **histone acetyltransferase** and **histone deacetylase** substrates far beyond histones |
| Glycosylation | lectins, hydrazide chemistry, hydrophilic interaction chromatography | glycans are heterogeneous; intact glycopeptides need special fragmentation |

Serial enrichment from one sample, for example antibodies against GlyGly and acetyllysine followed by IMAC on the flow-through, measures several modification types from the same material (Mertins and colleagues, 2013).

### 9.6.2. The Phosphoproteome

**Definition 9.6.1 (Phosphoproteome)** The **phosphoproteome** of a cell is the set of its phosphorylated proteins, with the positions of the phosphorylated residues and the fraction of each protein phosphorylated at each position (the site occupancy); phosphoproteomics measures it by enrichment of phosphopeptides and LC-MS/MS.

Single experiments identify tens of thousands of phosphosites; the total number of reported human sites exceeds $10^5$, and most have no known function or kinase. Changes of phosphopeptide intensity mix two effects, a change of occupancy and a change of the protein's abundance, and must be normalized to the protein level measured in the same samples.

A phosphopeptide with several Ser, Thr or Tyr residues must also be localized: the precursor mass says that a phosphate is present, only fragment ions between the candidate sites say where.

**Formula 9.6.1 (Site-Localization Score)** For two candidate sites, let $n$ be the number of site-determining fragment ions (those whose masses differ between the two placements), $k$ the number of them matched for the better placement, and $p$ the probability of a chance match per ion. The probability of at least $k$ chance matches is $P = \sum_{j \ge k}\binom{n}{j}p^j(1-p)^{n-j}$, and the localization score is
$$
\mathrm{Ascore} = -10 \log_{10} P \tag{9.8}
$$
(Beausoleil and colleagues, 2006); a score above $19$ ($P < 0.0125$) is conventionally taken as confident localization. Probabilistic variants (ptmRS, the localization probabilities of MaxQuant) give each site a posterior probability.

**Example 9.6.1** Two serines are four residues apart, so that four b ions (and their complementary y ions) distinguish the placements; three of the four b ions predicted for the first placement are found, none of the second's, and $p = 0.04$. Then $P = 4 \times 0.04^3 \times 0.96 + 0.04^4 = 2.5 \times 10^{-4}$ and $\mathrm{Ascore} = 36.0$: the phosphate is on the first serine. If the two serines were adjacent there would be a single site-determining pair of ions, and even a match would give only $P = p = 0.04$, $\mathrm{Ascore} = 14$, not enough to decide.

### 9.6.3. From Sites to Kinases and Signaling

Phosphoproteomes are read through the kinases that produce them. Each **protein kinase** prefers substrates with particular residues around the site (proline at $+1$ for CDKs and MAP kinases, basic residues at $-3$ for PKA and AKT); an atlas of the motif preferences of nearly all human serine/threonine kinases, measured on peptide libraries (Johnson and colleagues, 2023), and curated kinase–substrate relations (PhosphoSitePlus) assign sites to candidate kinases. Kinase activity is then inferred from the coordinated change of its substrates, exactly as transcription factor activity is inferred from its targets ([7.9.3](/7.9.3#sec-3.4)): kinase–substrate enrichment analysis (KSEA; Casado and colleagues, 2013) compares the mean log fold change of a kinase's known substrates with the distribution of all sites by a z score. Time courses of phosphorylation after a stimulus, measured by SILAC or isobaric labeling at seconds-to-minutes resolution, order the activation of kinases along a pathway and are the data for the signaling models of [7.9.14](/7.9.14) and [7.9.16](/7.9.16).

## 9.7. Scale, Affinity and Single Cells

### 9.7.1. Atlases and Proteogenomics

The Human Protein Atlas maps the expression and localization of human proteins with antibodies (immunohistochemistry on tissue microarrays, immunofluorescence in cell lines) and RNA sequencing; its tissue, subcellular and pathology sections link protein expression to organ, organelle and cancer survival (Uhlén and colleagues, 2015). The Human Proteome Project has found mass-spectrometric or other protein-level evidence for more than $90\%$ of the predicted protein-coding genes. The Clinical Proteomic Tumor Analysis Consortium (CPTAC) profiles tumors by genomics, transcriptomics, proteomics and phosphoproteomics on the same samples; in colon cancer, for example, phosphorylation of the retinoblastoma protein was associated with proliferation and reduced apoptosis, explaining why this tumor suppressor is elevated rather than lost in these tumors (Vasaikar and colleagues, 2019). Such data connect genomic alterations to the pathways that they actually activate ([7.9.13](/7.9.13)).

### 9.7.2. Affinity Proteomics

Antibodies and other binders measure predefined proteins with much higher sensitivity than mass spectrometry, which matters in plasma. Classical assays are the **ELISA** and the **Western blot**; arrays of antibodies or of purified proteins extend them to hundreds of targets, limited by the specificity of the binders and by the very different conditions under which proteins are stable. Two methods dominate large plasma studies. The proximity extension assay (Olink) uses pairs of antibodies carrying DNA oligonucleotides; only when both bind the same protein do the oligonucleotides hybridize and get extended into a DNA barcode, which is counted by PCR or sequencing, so that the readout of thousands of proteins is a sequencing count. SomaScan uses modified DNA aptamers (SOMAmers) selected to bind specific proteins, quantified on DNA arrays. Both reach femtomolar sensitivity and measure thousands of proteins in microliters of plasma; their weakness is that a binder may not measure the intended protein, or may be affected by a coding variant at its epitope, which creates false protein QTLs. Agreement between platforms varies widely across proteins.

### 9.7.3. Single Cells and Single Molecules

Protein measurements in single cells come in three kinds. Antibody-based cytometry counts tens of proteins per cell in millions of cells: flow cytometry with fluorophores, and mass cytometry (CyTOF) with antibodies tagged by lanthanide isotopes read by time-of-flight mass spectrometry, about $40$–$50$ markers without spectral overlap; the same tags read spatially are imaging mass cytometry ([7.9.6](/7.9.6#sec-6.4.3)). Antibodies carrying DNA barcodes are counted with the transcriptome by sequencing (CITE-seq, [7.9.5](/7.9.5#sec-5.7)). Mass spectrometry of single cells, finally, measures proteins without antibodies: SCoPE2 (Specht and colleagues, 2021) labels single cells with isobaric tags and adds a carrier channel of many cells that supplies ions for identification, quantifying about a thousand proteins per cell; label-free single-cell DIA on the most sensitive instruments reaches several thousand. The statistical problems are those of single-cell RNA data, small counts and many missing values, and those of isobaric labeling, interference and the carrier's influence on the measured ratios.

The ultimate goal, sequencing single protein molecules, is being approached from several directions: fluorescent recognizers of N-terminal amino acids observed while the protein is degraded residue by residue on a semiconductor chip (Reed and colleagues, 2022), fluorescent fingerprints of labeled residues, and nanopores that read the ionic current of peptides passing through them ([7.6.12](/7.6.12#sec-12.7)). None yet matches mass spectrometry in throughput or in the range of modifications it can read.

## 9.8. Metabolomics

### 9.8.1. The Metabolome

**Definition 9.8.1 (Metabolomics)** The **metabolome** of a sample is the complete set of its small molecules (typically below $1500\,\mathrm{Da}$): substrates, intermediates and products of **metabolism**, signaling molecules, and compounds from diet, microbes, drugs and the environment. **Metabolomics** is the comprehensive identification and quantification of the metabolome and of its changes in response to genotype, disease, perturbation or time.

The metabolome differs from the other omics layers in three ways. It is chemically diverse: amino acids, sugars, lipids, nucleotides and cofactors differ in polarity, charge and stability, so no single extraction, separation or ionization captures them all. It is not encoded in a sequence: there is no reference list from which to predict what to look for, and a large fraction of the signals in untargeted data cannot be identified. And it changes fast: the turnover of ATP and glycolytic intermediates is measured in seconds, so the sampling must stop metabolism instantly (quenching in cold solvent or liquid nitrogen) and handle all samples identically. In return, metabolites are measured in accessible fluids (blood, urine, saliva), are directly related to physiology, and are the targets of many clinical tests: newborn screening for **inborn errors of metabolism** by tandem mass spectrometry is metabolomics in routine use.

### 9.8.2. Platforms

| Platform | Separation and detection | Strengths | Limits |
|---|---|---|---|
| LC-MS | reversed-phase or hydrophilic interaction chromatography, ESI, high-resolution MS (Orbitrap, TOF) | broad coverage, high sensitivity (nM), the main untargeted platform | ion suppression; ionization efficiency differs between compounds; many unknowns |
| GC-MS | **gas chromatography** after chemical derivatization, electron ionization | reproducible fragmentation with large spectral libraries; volatile and central-carbon metabolites | derivatization; thermally labile compounds |
| NMR | **nuclear magnetic resonance**, usually $^1\mathrm{H}$, without separation | quantitative without standards, nondestructive, highly reproducible, identifies structures | sensitivity only to about $\mu\mathrm{M}$; overlapping peaks |
| Targeted MS | LC with triple quadrupole, selected reaction monitoring | absolute quantification of tens to hundreds of known compounds with labeled standards | only what is chosen beforehand |

Metabolomics can be targeted, measuring a predefined panel of compounds with authentic standards, or untargeted, recording all detectable signals and identifying them afterwards. Lipidomics is the branch devoted to lipids, whose thousands of molecular species are organized by class, chain length and saturation. Spatial metabolomics by mass spectrometry imaging is treated in [7.9.6](/7.9.6#sec-6.5.2).

### 9.8.3. From Spectra to a Feature Table

Untargeted LC-MS data are processed into a feature table, the metabolomic analogue of the count matrix. Software such as XCMS (Smith and colleagues, 2006), MZmine or MS-DIAL detects chromatographic peaks in each run as features defined by $m/z$ and retention time, aligns them across runs, fills in missing peaks by integrating the raw signal at the expected position, and groups features that are adducts ($[\mathrm{M}+\mathrm{H}]^+$, $[\mathrm{M}+\mathrm{Na}]^+$, $[\mathrm{M}+\mathrm{NH_4}]^+$), isotopes or in-source fragments of the same compound. One compound typically gives several features, and a data set of a few hundred compounds can have tens of thousands of features.

Quality control is built into the design: a pooled QC sample, a mixture of all samples, is injected repeatedly through the run order; features whose coefficient of variation in the QC exceeds about $20$–$30\,\%$ are removed, and drifts of the instrument signal along the run are corrected by fitting a smooth curve (for example LOESS) to the QC intensities of each feature. Samples are randomized in run order so that drift and batch are not confounded with groups. Normalization adjusts for differences in sample amount (total signal, probabilistic quotient normalization, or for urine the creatinine concentration), and log transformation stabilizes the variance. Statistical analysis is then univariate (t-tests or linear models with FDR control) and multivariate (principal component analysis and partial least squares discriminant analysis, the latter prone to overfitting and to be validated by cross-validation and permutation; [7.7.21](/7.7.21)).

### 9.8.4. Annotation

The hardest step is to say what a feature is. An accurate mass constrains the elemental formula; isotope patterns, fragment spectra and retention time constrain the structure; only comparison with an authentic standard under the same conditions identifies it.

**Example 9.8.1** A feature at $m/z\ 181.0710$ in positive mode, if it is $[\mathrm{M}+\mathrm{H}]^+$, has neutral mass $180.0637$. The formula $\ce{C6H12O6}$ has monoisotopic mass $180.0634$, so $[\mathrm{M}+\mathrm{H}]^+ = 181.0707$ and the error is $+1.9\,\mathrm{ppm}$, within the accuracy of an Orbitrap. But glucose, fructose, galactose, mannose and the other hexoses all have this formula, and they are distinguished only by retention time and fragmentation compared with standards; in positive ESI, sugars moreover prefer $[\mathrm{M}+\mathrm{Na}]^+$ ($m/z\ 203.0526$). A correct formula is far from an identification.

:::

The Metabolomics Standards Initiative defines levels of confidence (Sumner and colleagues, 2007): level 1, identified compounds, confirmed by comparison of at least two orthogonal properties (such as retention time and fragment spectrum) with an authentic standard in the same laboratory; level 2, putatively annotated compounds, by spectral similarity to a library; level 3, putatively characterized compound classes; level 4, unknown compounds, distinguishable only as features. Papers should report the level of each annotation. Spectral libraries (METLIN, MassBank, the GNPS libraries, NIST for GC-MS), in silico fragmentation (CSI:FingerID in SIRIUS) and molecular networking, which links features whose fragment spectra are similar into a network so that annotations propagate from known compounds to structurally related unknowns (Wang and colleagues, 2016), raise the fraction of annotated features, which nevertheless often remains below a third in untargeted studies.

### 9.8.5. Isotope Tracing and Fluxes

Concentrations do not reveal fluxes: a metabolite can be at the same level in two conditions while flowing through its pathway at very different rates. Isotope tracing measures pathway activity by feeding a labeled nutrient, such as $[\mathrm{U}\text{-}^{13}\mathrm{C}]$glucose or $[^{13}\mathrm{C}_5]$glutamine, and measuring how the label distributes over downstream metabolites.

**Definition 9.8.2 (Mass Isotopomer Distribution)** The **mass isotopomer distribution** (MID) of a metabolite with $n$ carbon atoms is the vector of fractions $(f_0, f_1, \dots, f_n)$ of its molecules that contain $0, 1, \dots, n$ heavy atoms of the tracer element ($^{13}\mathrm{C}$), measured as the relative intensities of its M+0, M+1, …, M+$n$ peaks.

The measured MID contains, besides the tracer, the natural heavy isotopes of all elements of the molecule (and of a derivatization group in GC-MS), which must be removed before interpretation.

**Formula 9.8.1 (Natural-Abundance Correction)** Let $\boldsymbol{f}$ be the true MID of tracer labeling and $\boldsymbol{m}$ the measured one. A molecule with $j$ tracer-labeled carbons has $n - j$ unlabeled carbons, each $^{13}\mathrm{C}$ with natural probability $p = 0.0107$, and its other atoms contribute their own natural isotope distribution $\boldsymbol{d}$ (for $\mathrm{H}$, $\mathrm{N}$, $\mathrm{O}$, $\mathrm{S}$, …). Its measured distribution is the column
$$
\boldsymbol{a}_j = \boldsymbol{\delta}_j * \mathrm{Bin}(n - j, p) * \boldsymbol{d}, \qquad \boldsymbol{m} = A\boldsymbol{f}, \quad A = [\boldsymbol{a}_0, \dots, \boldsymbol{a}_n], \tag{9.9}
$$
where $*$ is convolution and $\boldsymbol{\delta}_j$ a unit shift by $j$ mass units. The true MID is recovered by solving $A\boldsymbol{f} = \boldsymbol{m}$ with $\boldsymbol{f} \ge \boldsymbol{0}$, $\sum_j f_j = 1$ (non-negative **least squares**), as implemented in IsoCor or AccuCor.

**Example 9.8.2** For citrate, $\ce{C6H8O7}$, the unlabeled molecule measures as $92.1\%$ M+0, $6.3\%$ M+1 and $1.5\%$ M+2 (mostly $^{13}\mathrm{C}$ for M+1 and $^{18}\mathrm{O}$ for M+2). In the illustrative labeling experiment of the figure, the true MID $(0.35, 0.04, 0.33, 0.06, 0.14, 0.03, 0.05)$ is measured as $(0.322, 0.059, 0.318, 0.073, 0.142, 0.034, 0.053)$; the fractional enrichment $\sum_j j f_j/n$ appears as $32.7\%$ instead of $31.5\%$, and the M+1 and M+3 fractions, which carry information about pyruvate carboxylase and multiple turns of the cycle, are inflated by $48\,\%$ and $22\,\%$. Solving Eq. (9.9) recovers the true MID exactly from noise-free data.

![Mass isotopomer distributions of citrate and their correction for natural isotope abundance. A: unlabeled citrate is not pure M+0. B: an illustrative labeling experiment with [U-13C]glucose: true, measured and corrected MIDs, with the fractional enrichment FE; the measured distribution is the true one convolved with the natural isotopes of unlabeled carbons, hydrogens and oxygens (Eq. (9.9)). C: the correction matrix, column j being the measured distribution of a molecule with exactly j labeled carbons](./plots/isotopologues.py)

:::

The labeling patterns are interpreted by atom mapping: glucose-derived acetyl-CoA enters citrate as two labeled carbons (M+2), whereas pyruvate carboxylase, which makes oxaloacetate from pyruvate, contributes M+3, so the ratio of the two reports on the anaplerotic entry into the cycle. ${}^{13}\mathrm{C}$ metabolic flux analysis turns such data into fluxes: a model of the network with its atom transitions predicts the MIDs of all measured metabolites at isotopic steady state as a function of the fluxes, constrained by the **stoichiometric matrix** and mass balance, and the fluxes are estimated by weighted least squares, with confidence intervals by profile likelihood. It complements **flux balance analysis** ([7.6.34](/7.6.34)), which predicts **metabolic flux** from stoichiometry and an assumed objective without labeling data, and provides the measured fluxes that the control analysis of [7.1.17](/7.1.17) and the kinetic models of [7.9.14](/7.9.14) require.

### 9.8.6. Integration

Metabolomic changes are interpreted against pathway maps (KEGG, Reactome, the human metabolic reconstruction Recon) by over-representation or enrichment of pathways ([7.9.3](/7.9.3)), with the same caveats about background and annotation, and with an additional one: many metabolites belong to several pathways, and the pathway that changed is rarely identified by concentrations alone. Genetic studies of metabolite levels (metabolite QTLs) link enzymes and transporters to their substrates, the metabolic counterpart of eQTL mapping ([7.4.25](/7.4.25)). Combining transcript, protein and metabolite data in genome-scale models constrains which enzymes can carry flux and identifies the steps that control it; the network methods for this integration are those of [7.9.12](/7.9.12).

## Summary

| Step | Problem | Method | Key relation |
|---|---|---|---|
| Ionization and mass | charge unknown | isotope spacing, adjacent charge states | Formula 9.3.1, Eqs. (9.1)–(9.3) |
| Identification | which peptide made this spectrum | b/y ions, database search, PSM (Definition 9.4.1) | Formula 9.4.1, Eq. (9.4) |
| Error control | thousands of PSMs, unknown errors | target–decoy approach (Definition 9.4.2) | $\widehat{\mathrm{FDR}} = D/T$, q-values (Formula 9.4.2) |
| Protein inference | shared peptides | parsimony, protein groups | Algorithm 9.4.1 |
| Label-free quantification | run-to-run variation, missing values | MS1 intensities, MaxLFQ; censored models | Formula 9.5.2 |
| Labeled quantification | samples within one run | SILAC (Definition 9.5.1), isobaric tags (Definition 9.5.2) | ratio compression, Formula 9.5.1 |
| Completeness | stochastic precursor selection | DIA (Definition 9.5.3) | library or predicted spectra, decoys |
| Modifications | low occupancy, localization | enrichment; localization scores | Formula 9.6.1 |
| Metabolites | chemical diversity, unknowns | LC-MS, GC-MS, NMR; feature tables; MSI levels | Example 9.8.1 |
| Fluxes | concentrations ≠ fluxes | isotope tracing, MIDs (Definition 9.8.2) | Formula 9.8.1 |

- Protein levels are only partly predicted by mRNA, proteoforms (Definition 9.1.1) multiply each gene, and the proteome spans seven (cells) to ten (plasma) orders of magnitude; separation, enrichment and targeted acquisition are strategies against this range (9.1–9.2).
- Peptide identification is statistical inference at scale: probability scores rank candidates (Example 9.4.2), and decoys calibrate the error rate (Example 9.4.3: $6406$ PSMs at $1\%$ FDR, true FDP $1.01\%$); FDR must be controlled at the protein level separately, and protein inference is a set-cover problem (Example 9.4.4).
- Quantification compares the same peptide across samples: label-free designs scale to cohorts but have left-censored missing values (Example 9.5.2); SILAC is most precise; isobaric tags multiplex but compress ratios (Example 9.5.1: $\log_2$ ratio $2$ observed as $1.34$ in MS2); DIA reduces missingness.
- Phosphoproteomics requires enrichment, normalization to protein levels and site localization (Example 9.6.1); kinase activities are inferred from substrate sets as regulator activities are from target sets (9.6.3).
- Affinity methods (proximity extension, aptamers) reach the low end of the plasma range; single-cell and single-molecule methods extend proteomics to resolutions that RNA methods already reach (9.7).
- Metabolomics measures the layer nearest to phenotype; its main limits are chemical diversity and annotation (Example 9.8.1, MSI levels 1–4); isotope tracing with natural-abundance correction (Example 9.8.2) turns snapshots into pathway activities and fluxes (9.8.5).

## Questions

1. Why can protein levels not be predicted from mRNA levels, and what kinds of information does proteomics provide that RNA sequencing cannot, even in principle?

   **Answer** Protein level at steady state is the synthesis rate divided by the degradation rate; synthesis is mRNA level times translation rate, and both translation rates and protein half-lives vary by orders of magnitude between genes, so that mRNA explains only part of the variance across genes ([7.9.4](/7.9.4#sec-4.4.4)); after a perturbation, proteins also lag behind. In principle RNA cannot report post-translational modifications and their site occupancies, proteolytic processing, proteoforms (Definition 9.1.1), complex membership, subcellular location or secretion, all of which determine activity.

2. In an ESI spectrum, an envelope contains neighboring peaks at $m/z\ 893.4$ and $942.9$. Find the charges and the neutral mass of the molecule.

   **Answer** By Eq. (9.3) with $m_1 = 893.4$, $m_2 = 942.9$: $z = (942.9 - 1.007)/(942.9 - 893.4) = 941.89/49.5 = 19.03 \approx 19$, so $893.4$ is the $19+$ ion and $942.9$ the $18+$ ion. $M = 19 \times (893.4 - 1.007) = 16\,955$; from the other peak $18 \times 941.89 = 16\,954$, consistent to within the rounding of the $m/z$ values.

3. Compute the m/z of $\mathrm{b}_2$ and $\mathrm{y}_2$ for the peptide SAMPLER, and of its $[\mathrm{M}+2\mathrm{H}]^{2+}$ ion. (Residue masses: S $87.032$, A $71.037$, M $131.040$, P $97.053$, L $113.084$, E $129.043$, R $156.101$.)

   **Answer** $\mathrm{b}_2 = 87.032 + 71.037 + 1.007 = 159.076$. $\mathrm{y}_2 = 129.043 + 156.101 + 18.011 + 1.007 = 304.162$. The sum of residues is $784.390$, so $M = 784.390 + 18.011 = 802.401$ and $[\mathrm{M}+2\mathrm{H}]^{2+} = (802.401 + 2.015)/2 = 402.208$. (Cleavage N-terminal to proline is enhanced in practice, so the y ion containing PLER, $\mathrm{y}_4 = 514.299$, would be prominent.)

4. A search of $50\,000$ spectra against a concatenated target–decoy database gives, above a score threshold, $12\,400$ target and $93$ decoy PSMs. Estimate the FDR. Why would doubling the size of the target database (for example by adding all six-frame translations of the genome) usually reduce the number of PSMs accepted at $1\%$ FDR?

   **Answer** $\widehat{\mathrm{FDR}} = 93/12\,400 = 0.75\%$ (or $94/12\,400 = 0.76\%$ with the conservative $+1$). A larger database contains more wrong candidates per spectrum, so the best random match of each spectrum scores higher; the incorrect-match (and decoy) score distribution shifts to the right, more overlap with correct matches arises, and the threshold needed for $1\%$ FDR rises, losing correct low-scoring matches. Few of the added sequences are real, so the gain in true identifications rarely compensates. This is why proteogenomic searches use focused databases from the sample's own sequencing data.

5. Why does a $1\%$ PSM-level FDR not guarantee a $1\%$ protein-level FDR? Illustrate with a data set of $100\,000$ accepted PSMs from $5000$ true proteins.

   **Answer** At $1\%$ PSM-level FDR, about $1000$ accepted PSMs are wrong. Correct PSMs concentrate on true proteins ($99\,000$ PSMs over $5000$ proteins, about $20$ each), while wrong PSMs are scattered over the large database, so most of the $1000$ wrong PSMs hit different, absent proteins. Counting proteins with at least one PSM, there could be up to about $1000$ false proteins among $6000$, a protein-level FDR near $17\%$. Protein-level FDR must therefore be estimated separately, with decoy proteins and protein scores that reward multiple supporting peptides.

6. In a TMT experiment, the median observed $\log_2$ ratio of a set of proteins known (from a spike-in) to be changed tenfold is $1.9$. Estimate the average interference fraction, assuming the co-isolated ions are $1:1$. How could you check this assumption, and what would you do about it?

   **Answer** The true ratio is $10$, so solve Eq. (9.6) for $R_{\mathrm{obs}} = 2^{1.9} = 3.73$: $\big((1-\phi)\cdot\tfrac{10}{11} + \tfrac{\phi}{2}\big)\big/\big((1-\phi)\cdot\tfrac{1}{11} + \tfrac{\phi}{2}\big) = 3.73$. At $\phi = 0.30$ the left side is $0.786/0.214 = 3.68$, and solving numerically gives $\phi = 0.29$: on average about $29\%$ of the reporter signal comes from co-isolated ions. One checks the assumption with the precursor isolation purity recorded for each scan (ratios should be more compressed in impure scans) and with peptides from proteins known to be unchanged. Remedies: narrower isolation windows, MS3 with synchronous precursor selection, filtering PSMs with low purity, or modeling the compression as a function of purity.

7. A protein is detected in all four treated samples (log2 intensities $22.1$, $21.8$, $22.4$, $21.9$) and in none of four controls; the detection limit is about $20$. What can be concluded, and how should it be reported?

   **Answer** The protein is likely more abundant in treated samples, by at least $22.05 - 20 \approx 2$ log units on average if the controls are just below the limit, but the fold change is not estimable: it could be much larger. A test of presence/absence (for example Fisher's exact test on 4/4 against 0/4, $p = 0.029$ two-sided) or a censored likelihood ratio test (Formula 9.5.2) gives the evidence; the report should state "detected only in treated samples, lower bound on the fold change about 4", not a fold change computed from imputed values, which would reflect the imputation distribution.

8. A phosphopeptide has phosphorylatable residues at positions 3 and 9. Explain which fragment ions determine the site, and compute the Ascore if $5$ of $6$ site-determining ions are matched for one placement, with $p = 0.05$.

   **Answer** The b ions $\mathrm{b}_3$ to $\mathrm{b}_8$ (and the complementary y ions) contain residue 3 but not residue 9: they carry the extra $79.966$ only if the phosphate is on residue 3; their masses differ by $79.966$ between the two placements, so they are the site-determining ions. With $n = 6$, $k = 5$, $p = 0.05$: $P = 6 \times 0.05^5 \times 0.95 + 0.05^6 = 1.78\times10^{-6} + 1.6\times10^{-8} = 1.80\times10^{-6}$, $\mathrm{Ascore} = -10\log_{10}P = 57.4$, a confident localization to residue 3.

9. Design a phosphoproteomic experiment to determine which kinases are activated within the first $10$ minutes after stimulating cells with EGF, and the analysis you would perform.

   **Answer** Design: cells (SILAC-labeled, or label-free/TMT) starved, then stimulated with EGF for $0, 1, 2, 5, 10$ minutes, at least three biological replicates, quenched rapidly; lysis with phosphatase inhibitors, digestion, a portion analyzed for the proteome and the rest enriched by $\ce{Ti^4+}$-IMAC (plus anti-pTyr immunoprecipitation, since receptor tyrosine kinase signaling begins with pTyr), LC-MS/MS (TMT sets including all time points, or DIA). Analysis: target–decoy FDR at PSM and site level, localization probabilities (keep sites above $0.75$), normalization of site intensities to protein abundance, time-course models (for example limma with time as a factor, or spline fits) with FDR control; kinase activities by KSEA or motif-based enrichment over time, expecting EGFR autophosphorylation sites first, then ERK (MAPK) and AKT substrates; clustering of site trajectories; validation with kinase inhibitors (an MEK inhibitor should abolish the ERK substrate group).

10. In a ${}^{13}\mathrm{C}$-glucose tracing experiment, citrate in a cancer cell line shows a large M+3 fraction after natural-abundance correction. What pathway does this suggest, and which control experiment would distinguish it from multiple turns of the TCA cycle?

    **Answer** M+3 citrate arises when oxaloacetate made by pyruvate carboxylase from M+3 pyruvate condenses with unlabeled acetyl-CoA, so it suggests anaplerotic entry through pyruvate carboxylase. M+3 can also arise after several turns of the cycle from combinations of labeled fragments, and from natural abundance if not corrected (Example 9.8.2). Controls: measure the MID of aspartate or malate (M+3 oxaloacetate gives M+3 aspartate in the first turn, whereas cycling first gives M+2), use $[1\text{-}^{13}\mathrm{C}]$- or $[3,4\text{-}^{13}\mathrm{C}_2]$glucose tracers that label pyruvate carboxylase and pyruvate dehydrogenase products differently, measure at early time points before multiple turns, and knock down pyruvate carboxylase to see whether M+3 disappears.

11. Why does a feature table from untargeted LC-MS usually contain many more features than there are metabolites in the sample? How would you estimate the number of distinct compounds?

    **Answer** Each compound gives several features: adducts ($[\mathrm{M}+\mathrm{H}]^+$, $[\mathrm{M}+\mathrm{Na}]^+$, $[\mathrm{M}+\mathrm{K}]^+$, $[\mathrm{M}+\mathrm{NH_4}]^+$, dimers), isotope peaks, in-source fragments and multiply charged ions; there are also background and contaminant features (solvent, plastics) and noise peaks passing the detection threshold. Grouping features that co-elute (same retention time, correlated intensities across samples) and have mass differences of known adducts and isotopes (CAMERA, MS-DIAL) collapses them into compound groups; blanks remove background features, and pooled QC dilution series remove features that do not scale with sample amount. The number of compound groups after these steps estimates the number of compounds.

12. A clinical study measures $1500$ plasma proteins with an aptamer platform and finds that a coding variant of gene $X$ is strongly associated with the measured level of protein $X$. Give two explanations and an experiment to distinguish them.

    **Answer** (1) A true protein QTL: the variant changes the expression, secretion or stability of protein $X$. (2) An epitope effect: the variant changes the amino acid at the binder's site, so the aptamer binds the variant protein less (or more) strongly although the amount is the same. To distinguish them, measure protein $X$ by an orthogonal method that does not depend on the same binder: targeted mass spectrometry of peptides not containing the variant residue, or an antibody-based assay recognizing a different epitope; also check whether the association depends on the specific platform and whether the variant is near the binding region. Agreement between orthogonal methods supports a true protein QTL.
