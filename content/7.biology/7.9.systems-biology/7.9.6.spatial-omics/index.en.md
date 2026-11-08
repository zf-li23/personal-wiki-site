---
title: Spatial Omics
description: "Measuring molecules where they are: the map of spatial omics by molecular layer and readout; imaging transcriptomics (smFISH, combinatorial and error-correcting barcodes, in situ sequencing and Xenium) and imaging proteomics (cyclic immunofluorescence, CODEX, CyCIF, mass-tag imaging) with spillover compensation; capture arrays and mass spectrometry imaging; scaling up to whole slides and three dimensions, with tiled computation, halos and stitching; cell segmentation by watershed and deep learning, and its evaluation; SpatialData and the scverse ecosystem; cell-type annotation; spatial statistics (Moran's I, spatially variable genes, Ripley's K, neighborhood enrichment); spatial domains, cellular neighborhoods and niches; deconvolution and optimal-transport mapping; image registration; and the prospects and limits of foundation models."
---

Single-cell sequencing ([7.9.5](/7.9.5)) measures thousands of genes in each of millions of cells, but it first dissociates the tissue, and with it discards where each cell was and which cells were its neighbors. Much of biology is written in that lost information: the layered structure of the cortex, the crypts of the intestine, the zonation of the liver lobule, the boundary between a tumor and the immune cells that attack or protect it. Spatial omics measures molecules in intact tissue sections, at resolutions from tens of micrometres down to single molecules, so that expression, cell types and their arrangement are observed together. This chapter describes why space matters (6.1), the map of technologies by molecular layer and readout (6.2), imaging-based transcriptomics (6.3) and proteomics (6.4), capture-based and mass spectrometry methods (6.5), the scaling of experiments to whole slides and three dimensions (6.6), the image analysis that turns pictures into cells (6.7), the data structures of the scverse ecosystem (6.8), cell-type annotation (6.9), spatial statistics (6.10), domains, neighborhoods and niches (6.11), deconvolution and mapping (6.12), registration and multimodal integration (6.13), and the prospects of large models (6.14).

The field is young and changes fast; the chapter concentrates on principles that outlast particular instruments: how a molecule is encoded and decoded, what limits resolution and sensitivity, and which statistical model each analysis rests on. It builds on the count models of [7.9.2](/7.9.2) and [7.7.20](/7.7.20), the single-cell methods of [7.9.5](/7.9.5), the graphs of [1.4](/1.4) and [network science](/1.4.7), optics and diffusion from [biophysics](/7.6) ([7.6.5](/7.6.5), [7.6.12](/7.6.12)), and deep learning ([4.7](/4.7)). Cell–cell communication without spatial information is treated in [7.9.7](/7.9.7), spatial metabolomics in more detail with mass spectrometry in [7.9.9](/7.9.9), and the tumor microenvironment in [7.9.13](/7.9.13).

## 6.1. Why Space

### 6.1.1. What Dissociation Loses

Three kinds of question need positions. The first is structure: which cell types form a tissue's functional units and how they are arranged, for example the alternating zones of hepatocytes from the portal to the central vein of a liver lobule, whose metabolic programs follow the oxygen gradient. The second is context: the same cell type behaves differently in different surroundings, as a T cell at the invasive margin of a tumor differs from one inside it, and the composition of a cell's neighborhood often predicts outcome better than the abundance of any cell type. The third is communication: secreted signals act over tens to hundreds of micrometres and contact-dependent signals only between touching cells, so a ligand and its receptor expressed in the same tissue signal only if the cells are close. During development, cells read their **positional information** from **morphogen** gradients ([7.5.11](/7.5.11)); spatial measurements of expression are how such gradients and their targets are mapped at genome scale.

Dissociation also distorts what it keeps. Enzymatic digestion takes time at $37\,^\circ\mathrm{C}$ and induces stress genes; fragile or large cells (neurons, adipocytes, some epithelia) are lost, so cell-type proportions in single-cell data are biased. Measurements in sections avoid these biases, at the price of new ones: a section is thin, cells are cut, and molecules must be assigned to cells by image analysis (6.6, 6.7).

### 6.1.2. Definitions

**Definition 6.1.1 (Spatial Omics)** **Spatial omics** is the measurement of many molecular species of one or several omics layers in an intact tissue section or volume, with each measurement assigned to a position in the tissue. **Spatial transcriptomics** measures RNA in this way, **spatial proteomics** proteins.

The output is a set of positions with features. Depending on the technology the positions are molecules (each detected transcript with its coordinates), pixels or capture spots on a regular grid, or segmented cells; the features are counts of transcripts, antibody intensities or mass spectra. In every case the data combine an expression matrix, as in single-cell analysis, with coordinates and, usually, an image of the tissue: the statistics of the matrix are those of earlier chapters, and the new methods concern the coordinates.

## 6.2. The Map of Spatial Omics

Technologies are distinguished by the molecular layer they measure and by how they read it out. In capture-based methods, molecules are released from the tissue onto a surface carrying spatially barcoded oligonucleotides and sequenced; the barcode records the position. In imaging methods, molecules are labeled in place with fluorescent probes and imaged under a microscope, over several rounds that build up a code for each molecule. In mass spectrometry methods, a laser or ion beam ablates or desorbs material pixel by pixel and the ions are analyzed by mass.

| Layer | Capture and sequencing | Imaging | Mass spectrometry |
|---|---|---|---|
| Genome | Slide-DNA-seq (copy number and clones) | DNA FISH, chromatin tracing | |
| Epigenome | spatial ATAC-seq, spatial CUT&Tag | imaging of chromatin marks | |
| Transcriptome | ST, Visium, Visium HD, Slide-seq, Stereo-seq | smFISH, MERFISH, seqFISH+, STARmap, Xenium, CosMx | |
| Proteome | barcoded antibodies on Visium (few targets) | multiplexed immunofluorescence, CODEX, CyCIF | IMC, MIBI |
| Metabolome | | | MALDI imaging, ToF-SIMS (scSpaMet) |

![The map of spatial omics. Representative technologies placed by the spatial resolution of their readout (horizontal, finer to the right) and the number of molecular species measured in one experiment (vertical, logarithmic); colour: omics layer; marker: readout. Values are approximate orders of magnitude for current versions; genome- and epigenome-wide methods are drawn at the top. Capture methods cover the transcriptome at coarser resolution, imaging methods reach subcellular resolution with targeted panels, and mass spectrometry measures metals or metabolites at cellular to multicellular resolution](./plots/omics_map.py)

The figure shows the main trade-off. Capture-based sequencing is untargeted: every polyadenylated transcript can be captured, so the whole transcriptome is measured, but the resolution is limited by the size of the capture features and by the diffusion of molecules to them. Imaging resolves single molecules at subcellular resolution but needs a probe for every target, so panels are selected in advance, with hundreds to a few thousand genes, or tens of proteins. Beyond resolution and plex, four further quantities decide what an experiment can answer: sensitivity (the fraction of molecules present that are detected), specificity (the fraction of detections that are correct), the area or volume measured, and the throughput in samples per week and cost per sample.

**Example 6.2.1 (How many cells share a spot?)** A Visium spot has a diameter of $55\,\mu\mathrm{m}$, an area $A = \pi (27.5\,\mu\mathrm{m})^2 = 2376\,\mu\mathrm{m}^2$, and the section is $T = 10\,\mu\mathrm{m}$ thick. A cell of diameter $d$ contributes to the spot if its center lies within a slab of thickness $T + d$, so with $n_V$ cells per unit volume the spot contains, on average, parts of $n_V (T + d) A$ cells. In the cerebral cortex ($n_V \approx 10^5\,\mathrm{mm^{-3}} = 10^{-4}\,\mu\mathrm{m}^{-3}$, $d \approx 12\,\mu\mathrm{m}$) this is $10^{-4} \cdot 22 \cdot 2376 = 5.2$ cell profiles; in a lymph node ($n_V \approx 10^6\,\mathrm{mm^{-3}}$, $d \approx 7\,\mu\mathrm{m}$) it is $40$. A spot is therefore a mixture of several to tens of cells, often of different types, which is why spot data are deconvolved (6.12).

## 6.3. Imaging-Based Transcriptomics

### 6.3.1. Single Molecules and the Diffraction Limit

Single-molecule **fluorescence in situ hybridization** (smFISH; Raj and colleagues, 2008) tiles an mRNA with about $30$–$50$ short DNA probes, each carrying a fluorophore. One probe is too dim to see, but tens of probes bound to the same molecule make a diffraction-limited spot that stands out from the background of unbound probes, so each mRNA is counted individually. The image of a point source is the **point spread function**, about $0.25\,\mu\mathrm{m}$ wide in the focal plane for visible light ([7.6.12](/7.6.12)). The center of an isolated spot can be localized much more precisely than this width, but two spots closer than about the width merge.

smFISH measures a few genes at a time, one per colour. Measuring hundreds of genes requires codes, and the diffraction limit sets how many molecules can be imaged at once.

**Example 6.3.1 (Optical crowding)** A mammalian cell contains of the order of $10^5$ mRNA molecules. In a section whose thickness is comparable to the cell, these project onto about $100\,\mu\mathrm{m}^2$, that is about $1000$ molecules per $\mu\mathrm{m}^2$. Spots can be separated reliably at densities of the order of $10$ per $\mu\mathrm{m}^2$. A panel of $500$ genes that accounts for $5\%$ of the mRNA gives $50$ molecules per $\mu\mathrm{m}^2$; if a coding scheme makes each molecule visible in only a quarter of the rounds, $12$ are visible in each image, at the limit. Panel size and the expression of the chosen genes therefore cannot be increased freely: highly expressed genes are excluded or measured separately, the tissue is physically expanded (expansion microscopy), or the codes are spread over more rounds.

### 6.3.2. Combinatorial and Error-Correcting Codes

In sequential barcoding (seqFISH; Lubeck and colleagues, 2014) each gene is assigned a sequence of colours, one per round: probes are hybridized, imaged and removed, and the colour of a spot in round $r$ is the $r$th letter of its code. With $F$ colours and $N$ rounds there are $F^N$ codes; four colours in eight rounds give $65\,536$. Any error in reading one round, however, turns a molecule into another gene.

MERFISH (multiplexed error-robust FISH; Chen and colleagues, 2015) uses binary codes designed to detect and correct errors. Each gene is assigned a binary word of $N$ bits. Encoding probes hybridize to the mRNA and carry readout sequences; in round $r$ a fluorescent readout probe complementary to the readout sequence of bit $r$ is added, so a molecule lights up in exactly the rounds whose bit is $1$. The words are chosen with the **Hamming distance**, the number of positions in which two words differ: if every two codewords differ in at least $4$ bits, a word with one error is closer to its true codeword than to any other and can be corrected, and a word with two errors is at distance at least $2$ from every codeword and can be discarded.

**Definition 6.3.1** A **MERFISH codebook** with parameters $(N, w, d)$ is a set of binary words of length $N$ with exactly $w$ ones (constant weight) and pairwise Hamming distance at least $d$. Decoding assigns an observed word to the codeword at distance $0$ or, when $d \ge 3$, to the unique codeword at distance $1$, and discards all other words.

The constant weight keeps the number of "on" rounds, and so the brightness and the error probability, the same for all genes, and a small $w$ keeps the density of spots per round low (Example 6.3.1). The number of words is limited: of the $\binom{16}{4} = 1820$ words of length $16$ and weight $4$, at most $140$ have pairwise distance at least $4$. A code that reaches this bound is the set of $4$-element subsets $\{a, b, c, d\}$ of $\{0, \dots, 15\}$ whose binary representations satisfy $a \oplus b \oplus c \oplus d = 0$ (the planes of the affine space over $\mathbb{F}_2^4$); two such subsets share at most two elements, so their words differ in at least four bits.

**Example 6.3.2** Suppose a $1$ is misread as $0$ with probability $p_{10} = 0.10$ and a $0$ as $1$ with probability $p_{01} = 0.04$, independently in each round ("on" bits are typically lost more often than "off" bits are gained). A molecule is read exactly with probability $0.9^4 \cdot 0.96^{12} = 0.402$. With the $140$-word code of distance $4$, exact enumeration of all $2^{16}$ received words gives: exact reads $40.2\%$, single errors corrected $38.0\%$ (total correct $78.2\%$), discarded $19.7\%$, misidentified as another gene $2.1\%$. Using all $1820$ weight-$4$ words without error correction, only the $40.2\%$ exact reads are correct and $9.3\%$ of the molecules are assigned to a wrong gene. Error correction doubles the yield and cuts misidentification by a factor of four, at the price of encoding only $140$ instead of $1820$ genes. Blank codewords (valid words assigned to no gene) estimate the misidentification rate in each experiment.

:::

Later versions use longer codes for larger panels and combine MERFISH with expansion and tissue clearing (Moffitt and colleagues, 2016). seqFISH+ (Eng and colleagues, 2019) measured $10\,000$ genes by spreading the molecules over $60$ "pseudocolours" imaged in sequence, so that only a sixtieth of the molecules is visible in each image.

### 6.3.3. In Situ Sequencing and Xenium

In situ sequencing (Ke and colleagues, 2013) amplifies the target before reading it. A padlock probe is a linear oligonucleotide whose two ends hybridize next to each other on the target (on cDNA, or directly on RNA with suitable ligases) and contains a gene-specific barcode in its backbone. Ligation closes the circle only if both ends match, which gives specificity; rolling-circle amplification by a strand-displacing polymerase then copies the circle into a single-stranded product of hundreds of tandem repeats, a submicrometre ball of DNA that is bright enough to image with ordinary optics. The barcode is read in cycles, by sequencing by ligation or by hybridization of fluorescent probes, and the series of colours over cycles is decoded as in seqFISH, with codes that allow error detection.

Xenium (10x Genomics, 2022) is a commercial implementation of this principle: padlock probes against a panel of genes, rolling-circle amplification, and cycles of fluorescent probe hybridization and imaging on an instrument that handles the fluidics. Each decoded transcript is reported with its coordinates and a quality score, which summarizes how well the observed colour series matches the codeword; transcripts below a threshold are removed. Panels have grown from a few hundred genes to $5000$ (2024). Similar instruments based on cyclic hybridization of barcoded probes, such as CosMx, also measure thousands of genes. STARmap (Wang and colleagues, 2018) embeds the tissue in a hydrogel and sequences amplified probes in three dimensions, in thick sections.

All imaging methods produce molecules, not cells. Assigning molecules to cells requires segmentation (6.7), and errors in that step propagate into every downstream analysis.

### 6.3.4. Sensitivity and Specificity

Sensitivity depends on probe design, on how much RNA survives fixation and permeabilization (formalin-fixed paraffin-embedded tissue, the standard clinical format, has fragmented RNA), and on the decoding threshold. It is estimated by comparing counts with smFISH of the same genes or with single-cell data from the same tissue, after correcting for the fraction of each cell's volume in the section. Specificity is estimated from negative controls: probes against sequences absent from the genome, and unused codewords. Both are trade-offs set by thresholds: a lower quality threshold detects more molecules and more errors. Panel design selects genes that distinguish the cell types of interest, avoids genes so highly expressed that they crowd the images, and is often derived from a single-cell reference of the same tissue ([7.9.5](/7.9.5)).

## 6.4. Imaging-Based Proteomics

### 6.4.1. Multiplexed Immunofluorescence

Proteins are detected with antibodies. Conventional **immunofluorescence** images up to four or five targets at once, limited by the overlap of fluorophore spectra.

**Definition 6.4.1** **Multiplexed immunofluorescence** (mIF) is the imaging of more targets in one section than the number of spectrally separable channels, by spectral unmixing of overlapping fluorophores, by cyclic staining and removal of the signal, or by barcoded antibodies read in cycles.

Spectral methods (for example tyramide signal amplification with $6$–$9$ fluorophores and unmixing) image a whole slide in one pass and are used clinically. For tens of markers, cyclic methods trade time for plex.

### 6.4.2. Cyclic Methods: CODEX and CyCIF

CODEX (co-detection by indexing; Goltsev and colleagues, 2018), commercialized as PhenoCycler, labels all antibodies at once, each conjugated to a unique DNA oligonucleotide barcode. In each cycle, fluorescent oligonucleotides complementary to three barcodes are hybridized, the three channels are imaged together with a nuclear stain, and the reporters are stripped; the antibodies stay bound. A panel of $60$ markers therefore needs $20$ cycles, but only one staining step, which avoids the damage of repeated antibody incubations. A published protocol (Black and colleagues, 2021) describes antibody conjugation, panel validation, staining, imaging and processing (stitching, drift compensation, background subtraction, segmentation), and the validation of every antibody on control tissue that is necessary because a conjugated antibody can lose specificity.

CyCIF (cyclic immunofluorescence; Lin and colleagues, 2018) uses conventional fluorophore-labeled antibodies, three or four per cycle, and after imaging inactivates the fluorophores chemically (hydrogen peroxide and light in alkaline solution) before the next cycle. Any validated commercial antibody can be used, and $40$–$60$ markers are routine. In both methods the nuclear stain imaged in every cycle registers the cycles to each other, so that the channels of one cell align to within a fraction of a micrometre.

### 6.4.3. Mass-Tag Imaging

Imaging mass cytometry (IMC; Giesen and colleagues, 2014) and multiplexed ion beam imaging (MIBI; Angelo and colleagues, 2014) label antibodies with isotopically pure lanthanide metals instead of fluorophores. IMC ablates the tissue spot by spot with a pulsed ultraviolet laser at $1\,\mu\mathrm{m}$ resolution and carries the plume into an inductively coupled plasma and a time-of-flight mass spectrometer; MIBI sputters the surface with a focused primary ion beam and analyzes the secondary ions, reaching a few hundred nanometres. Because metal isotopes have narrow, well-separated mass peaks and tissue has no metal background in this mass range, about $40$ markers are measured in one acquisition without autofluorescence. The price is speed and destruction of the sample.

**Example 6.4.1** IMC at $1\,\mu\mathrm{m}$ pixels and $200$ laser shots per second acquires $1\,\mathrm{mm}^2 = 10^6$ pixels in $5000\,\mathrm{s} = 83\,\mathrm{min}$. A whole section of $1\,\mathrm{cm}^2$ would take $139\,\mathrm{h}$, so IMC is used on selected regions or tissue microarrays, while cyclic fluorescence images whole slides in hours to a day.

### 6.4.4. Panel Design and Spillover

A panel assigns each antibody to a channel (fluorophore or metal). Bright channels are reserved for weakly expressed targets, and markers that are co-expressed in the same cells are placed in channels with little crosstalk. The remaining crosstalk is corrected with a linear model.

**Formula 6.4.1 (Spillover Compensation)** Let $\boldsymbol{x} \ge \boldsymbol{0}$ be the true signals of the $m$ labels in a pixel or cell and $\boldsymbol{y}$ the measured intensities in the $m$ channels. With the spillover matrix $S$, whose entry $s_{ij}$ is the fraction of label $j$'s signal recorded in channel $i$ ($s_{ii} = 1$), measured on single-stained controls,
$$
\boldsymbol{y} = S\boldsymbol{x} + \boldsymbol{\varepsilon}, \qquad \hat{\boldsymbol{x}} = \arg\min_{\boldsymbol{x} \ge \boldsymbol{0}} \|\boldsymbol{y} - S\boldsymbol{x}\|^2. \tag{6.1}
$$

The non-negativity constraint (non-negative least squares) avoids negative intensities that simple inversion $S^{-1}\boldsymbol{y}$ produces in noisy pixels; in IMC the spillover comes from isotopic impurities and oxide formation ($M + 16$), and the matrix is estimated once per batch of conjugates (Chevrier and colleagues, 2018).

**Example 6.4.2** Three channels with spillover $s_{12} = 0.08$, $s_{21} = 0.15$, $s_{23} = 0.05$, $s_{31} = 0.02$, $s_{32} = 0.10$, and a cell that expresses only labels $2$ and $3$ ($\boldsymbol{x} = (0, 50, 200)$), give $\boldsymbol{y} = (4, 60, 205)$: the cell appears positive for marker $1$ at $4$ units and overestimates marker $2$ by $20\%$. With measurement noise $(+3, -2, +4)$, compensation by Eq. (6.1) returns $(3.2, 47.3, 204.2)$.

:::

A second kind of spillover is spatial. In a tissue, cells touch, and the membrane signal of one cell overlaps the segmented outline of its neighbor, so a tumor cell next to a T cell appears weakly CD3-positive. Corrections such as REDSEA (Bai and colleagues, 2021) estimate, from the signal along shared boundaries, how much of each neighbor's intensity leaks into a cell and subtract it; better segmentation of membranes (6.7) reduces the problem at its source.

## 6.5. Capture-Based and Mass Spectrometry Methods

### 6.5.1. Spatially Barcoded Arrays

The first array-based method (Ståhl and colleagues, 2016) placed a tissue section on a glass slide printed with spots of oligonucleotides, each containing a poly(dT) sequence to capture mRNA, a **unique molecular identifier** and a spatial barcode specific to the spot. After imaging the stained section, the tissue is permeabilized, mRNA diffuses down to the surface and is captured, cDNA is synthesized on the slide, and the library is sequenced; the spatial barcode of each read gives its spot. Visium, its commercial successor, has $4992$ spots of $55\,\mu\mathrm{m}$ diameter at $100\,\mu\mathrm{m}$ center-to-center distance in a $6.5 \times 6.5\,\mathrm{mm}$ area; a probe-based version hybridizes gene-specific probe pairs in the tissue and captures the probes instead of the mRNA, which works on fragmented RNA of fixed tissue.

Higher resolution requires smaller features. Slide-seq (Rodriques and colleagues, 2019; Stickels and colleagues, 2021) packs $10\,\mu\mathrm{m}$ beads randomly on a surface and decodes each bead's barcode by sequencing in situ before the experiment. Stereo-seq (Chen and colleagues, 2022) uses DNA nanoballs patterned at about $0.5\,\mu\mathrm{m}$ pitch on chips up to centimetres across, and Visium HD (2024) a continuous grid of $2 \times 2\,\mu\mathrm{m}$ squares. At this resolution a single square holds only a few molecules, and the data are analyzed after binning (for example into $8\,\mu\mathrm{m}$ squares) or after assigning squares to cells segmented in the image of the same section.

The resolution of capture methods is not just the feature size. Molecules travel laterally between their release and their capture.

**Example 6.5.1** A molecule diffusing in two dimensions with **diffusion coefficient** $D$ for a time $t$ is displaced by $\sqrt{2Dt}$ in each direction ([7.6.5](/7.6.5)). For an effective $D = 0.1\,\mu\mathrm{m}^2\,\mathrm{s}^{-1}$ in permeabilized tissue and $t = 10\,\mathrm{min}$, the root-mean-square displacement along one axis is $\sqrt{2 \cdot 0.1 \cdot 600} = 11\,\mu\mathrm{m}$. With features of $2\,\mu\mathrm{m}$, the blur from diffusion, not the feature size, limits resolution: shorter permeabilization reduces the blur and the number of captured molecules together. Probe-based capture, in which short probes are transferred by a controlled device, and directional transfer reduce the spread.

:::

Sensitivity is lower than that of imaging, since only a fraction of the molecules reaches the surface and is reverse-transcribed, and the counts are sparse at high resolution. In exchange, capture methods are untargeted, so they discover genes not chosen in advance and measure isoforms and non-polyadenylated or non-coding RNA with suitable chemistry.

### 6.5.2. Mass Spectrometry Imaging

**Mass spectrometry imaging** (MSI) records a mass spectrum at each pixel. In MALDI imaging a matrix is sprayed over the section, a laser desorbs and ionizes molecules pixel by pixel at $5$–$50\,\mu\mathrm{m}$, and the spectra report metabolites, lipids, drugs, glycans or peptides without labels. The images contain thousands of $m/z$ features, of which only a fraction can be annotated to compounds by accurate mass, isotope pattern and, where possible, fragmentation; ionization efficiency depends on the local chemical environment (ion suppression), so intensities are relative ([7.9.9](/7.9.9)). Secondary-ion mass spectrometry reaches subcellular resolution: scSpaMet (Hu and colleagues, 2023) combined time-of-flight secondary-ion mass spectrometry for metabolites with IMC for proteins on the same sample, to relate metabolic states to cell types at single-cell resolution.

### 6.5.3. Spatial Genomics and Epigenomics

The same barcoding ideas apply to DNA. Slide-DNA-seq (Zhao and colleagues, 2022) captures fragments of genomic DNA on barcoded beads and reads copy-number profiles in space, which maps tumor clones in a section. DBiT-seq (Liu and colleagues, 2020) delivers barcodes through two perpendicular sets of microfluidic channels, so that every intersection, $10$–$50\,\mu\mathrm{m}$ across, receives a unique combination; with transposase-based chemistry this yields spatial ATAC-seq and spatial CUT&Tag (Deng and colleagues, 2022), genome-wide maps of accessibility and histone marks in tissue ([7.9.8](/7.9.8)).

## 6.6. Scaling Up

### 6.6.1. Five Dimensions of Scale

Spatial omics is growing along five dimensions at once: the cohort (from a few sections to hundreds of patients, needed for clinical associations), the resolution (from spots to subcellular molecules), the analyzable area (from millimetre regions to whole slides and to volumes), the gene or marker panel (from tens to thousands), and the dimensionality of the data per cell (several modalities on one cell). Each multiplies the size of the data and the cost of every step of analysis.

**Example 6.6.1** A whole-slide CODEX image of $1\,\mathrm{cm}^2$ at $0.5\,\mu\mathrm{m}$ per pixel has $(10^4/0.5)^2 = 4\times10^8$ pixels per channel; with $50$ channels at $16$ bits it occupies $4\times10^{10}$ bytes, $40\,\mathrm{GB}$, before any processing. A $30\,\mu\mathrm{m}$ thick section imaged in $30$ optical planes would occupy $1.2\,\mathrm{TB}$. Imaging transcriptomics of the same area adds hundreds of millions of decoded molecules, each with coordinates, gene and quality. Such data do not fit in the memory of a workstation, and every algorithm must be able to work on parts.

### 6.6.2. Three Dimensions

Most spatial data are from sections of $4$–$10\,\mu\mathrm{m}$, thinner than the cells they cut.

**Example 6.6.2 (Cut cells)** Model a cell as a sphere of diameter $d$ whose center falls uniformly in depth relative to a section of thickness $T$; a cell appears in the section if its center lies in a slab of width $T + d$. Integrating the volume of the spherical segment inside the section over this slab gives the following, for the cells that appear:

| $d$ / $\mu\mathrm{m}$ | $T$ / $\mu\mathrm{m}$ | mean fraction of the cell in the section | cells entirely inside |
|---|---|---|---|
| $10$ | $5$ | $0.33$ | $0$ |
| $10$ | $10$ | $0.50$ | $0$ |
| $10$ | $30$ | $0.75$ | $0.50$ |
| $12$ | $50$ | $0.81$ | $0.61$ |
| $6$ (nucleus) | $5$ | $0.46$ | $0$ |
| $6$ (nucleus) | $30$ | $0.83$ | $0.67$ |

In a $5\,\mu\mathrm{m}$ section no cell and no nucleus is complete, and an average cell is represented by a third of its volume; whether a cut cell is counted as positive for a marker located in one part of it depends on where it was cut.

:::

Three-dimensional measurements avoid this. Serial sections can be imaged and registered into a volume (6.13), with losses between sections and distortions from cutting. Thick sections imaged optically avoid both: three-dimensional CyCIF (Yapp and colleagues, 2025) imaged sections of $30$–$50\,\mu\mathrm{m}$ with a **confocal microscope** over $8$–$18$ cycles ($20$–$54$ markers) and showed, in line with the example, that nearly all cells in standard $5\,\mu\mathrm{m}$ sections are incomplete, which makes their phenotypes inaccurate; in thick sections intact cells, the contacts between them and their organelles can be resolved, revealing juxtacrine interactions between tumor and immune cells. Scale also grows sideways: placing sections of several organs or patients on one slide puts them into the same staining and imaging batch and makes them directly comparable.

### 6.6.3. Computing in Tiles

An image too large for memory is processed in tiles. Tiling is simple for pixel-wise operations, but segmentation and any analysis of neighborhoods need context: a cell crossing a tile boundary is cut into two fragments, each counted as a cell. The standard remedy, used in libraries for chunked array computing (such as `map_overlap` in dask) and in distributed versions of segmentation models, is to process each tile with a margin of surrounding pixels, the halo, and to reconcile the results.

**Algorithm 6.6.1 (Tiled Segmentation with Halos)** Input: an image, a tile side $L$, a halo $h$, a segmentation method.
1. Partition the image into tiles of side $L$. For each tile, form its window, the tile enlarged by $h$ on every side (clipped at the image border).
2. Segment every window independently, in parallel.
3. Discard every object that touches an edge of its window that is not an image border.
4. Map the remaining objects to global coordinates. For every pair of objects from overlapping windows, compute their intersection over union (6.7.6); if it is at least $0.5$, unite them in a **union–find** structure.
5. Output one object per set of the union–find structure (for example, the version from the window in whose core its centroid lies).

**Proposition 6.6.1** If every object has diameter less than $h$, each object lies entirely inside the window of the tile that contains any one of its points, so it survives step 3 in at least one window.

**Proof** Let $p$ be a point of the object in tile $Q$. Every point of the object is within distance $h$ of $p$, hence within the square of $Q$ enlarged by $h$, which is the window of $Q$ (or its clipping at the image border, where the object ends anyway). An object entirely inside a window does not touch its inner edges, unless it touches them exactly at distance $h$, which a strict inequality excludes. $\square$

The cost of the halo is the extra area processed, $(1 + 2h/L)^k - 1$ in $k$ dimensions: for tiles of $2048$ pixels and a halo of $64$ it is $12.9\%$ in two dimensions and $19.9\%$ in three; for smaller tiles of $1024$ with the same halo it is $26.6\%$ and $42.4\%$. Large tiles are cheaper but need more memory per worker, a choice that depends on whether the work runs on CPUs or on graphics processors, whose memory is smaller and faster.

![Segmenting a large image in tiles (synthetic image of 90 cells). A: 3 × 3 tiles of 120 px (solid lines); each is processed with a halo of 24 px (dashed: the window of the centre tile). B: without a halo, the 16 cells crossing tile boundaries are cut into fragments (red) and counted twice, giving 106 objects. C: with the halo, objects touching inner window edges are discarded and duplicates from overlapping windows are merged at IoU ≥ 0.5 with a union-find structure (Algorithm 6.6.1): exactly 90 objects. D: the extra pixels processed, (1 + 2h/L)^k − 1, in two and three dimensions; the dot marks the small tiles of this illustration](./plots/halo_stitch.py)

Storage follows the same logic. Chunked array formats (Zarr, and the OME-Zarr convention for bioimages) store an image as independently compressed chunks, often with a pyramid of downsampled copies for viewing, so that a program can read any region without loading the whole file and many workers can write in parallel. Out-of-core libraries (dask) build a graph of operations on chunks and execute it in parallel, on one machine or a cluster; graphics processors accelerate segmentation models and operations on large point clouds (nearest-neighbor search, graph construction). These engineering choices determine what analyses are practical at the scale of whole slides and cohorts.

## 6.7. Image Processing and Cell Segmentation

### 6.7.1. The Task

**Definition 6.7.1** **Cell segmentation** is the partition of an image (or volume) into regions that each correspond to one cell or one nucleus, and a background; the output is a label image in which each pixel carries the identifier of its cell or $0$.

Nuclei are easy to stain (DAPI, Hoechst) and are compact and separated by cytoplasm, so they are segmented first and most reliably. Cell boundaries require membrane stains (antibodies against membrane proteins such as E-cadherin, CD45, $\beta$-catenin or Na$^+$/K$^+$-ATPase, often pooled) or must be inferred. Once cells are segmented, the expression of each cell is the sum of the transcripts inside its region or the mean of each protein channel over it, together with morphological features (area, eccentricity).

### 6.7.2. The Watershed

Thresholding the nuclear stain separates nuclei from background, and connected components of the foreground give objects, but touching nuclei merge into one component. The classical remedy treats an image as a landscape.

**Algorithm 6.7.1 (Marker-Controlled Watershed)** Input: an elevation image $f$ (for example the negative distance to the background, or the gradient magnitude of the stain), a foreground mask and a set of markers, one connected group of pixels per object.
1. Give each marker its own label and put its pixels in a priority queue keyed by elevation.
2. Repeatedly remove the pixel of lowest elevation from the queue; give each of its unlabeled foreground neighbors the pixel's label and insert them into the queue.
3. Stop when the queue is empty. Pixels where regions from different markers meet form the watershed lines.

With a heap as priority queue the algorithm takes $O(n \log n)$ time for $n$ pixels. The *watershed algorithm* floods the landscape from the markers: each basin fills until it meets a neighboring basin, and the meeting lines separate the objects. For round nuclei, the Euclidean distance transform (the distance of each foreground pixel to the nearest background pixel) peaks at the centers and dips at the necks between touching nuclei, so its local maxima serve as markers and its negative as elevation. Too many markers split a nucleus (over-segmentation), too few merge two (under-segmentation); smoothing the distance transform and requiring a minimum peak height or separation control the balance.

![Marker-controlled watershed on a synthetic nuclear stain (40 nuclei, many touching). A: the image. B: threshold and connected components: touching nuclei merge into 20 objects, F1 = 0.47 at IoU ≥ 0.5. C: the smoothed distance transform of the foreground with its 39 local maxima as markers. D: watershed flooding from the markers: 39 objects, F1 = 0.99; one pair of nuclei with a wide neck shared a single marker and was merged](./plots/watershed.py)

In the figure, connected components recover only $14$ of the $40$ nuclei at an intersection over union of at least $0.5$ (precision $0.70$, recall $0.35$, **F1 score** $0.47$), while the watershed recovers $39$ (precision $1.00$, recall $0.975$, F1 $0.99$). Real images are harder: nuclei are irregular, stained unevenly and overlap in projection, and cytoplasm is not round, so classical pipelines need careful tuning for each tissue.

### 6.7.3. Deep Learning Models

Learned models replaced hand-tuned pipelines because they generalize across tissues and stains given enough annotated examples. They differ in what the network predicts and how objects are recovered from the prediction.

- Cellpose (Stringer and colleagues, 2021). For each training mask, a diffusion process from the cell's center ([7.6.5](/7.6.5)) defines a smooth vector field of flows pointing to the center. A U-Net ([4.7.3](/4.7.3)) predicts the horizontal and vertical flows and the probability that a pixel is inside a cell; at inference, pixels follow the predicted flows until they converge, and pixels that converge to the same sink form one cell. The flow representation handles irregular and elongated shapes that defeat distance-based methods. Later versions added human-in-the-loop retraining (Cellpose 2.0, 2022) and image restoration (Cellpose3, 2025).
- StarDist (Schmidt and colleagues, 2018). Each pixel predicts the distances to the object boundary along $32$ fixed directions, describing a star-convex polygon, and a probability of being near an object center; the polygons of high-probability pixels are pruned by non-maximum suppression. It is fast and accurate for nuclei, which are nearly star-convex, but not for irregular cells.
- Mesmer (Greenwald and colleagues, 2022). Trained on TissueNet, more than one million manually annotated nuclei and cells in multiplexed tissue images from several platforms, it takes a nuclear and a membrane channel and predicts transforms of the masks that a watershed turns into cells and nuclei.

General foundation models for segmentation (the Segment Anything family and its microscopy adaptations) can be prompted with points or boxes and fine-tuned with few examples; they are useful for annotation and for unusual objects, though specialized models remain more accurate for dense cells in tissue.

### 6.7.4. From Nuclei to Cells

Without a reliable membrane signal, cells are approximated by expanding each nucleus by a fixed distance (a few micrometres) until it meets its neighbors, which is a **Voronoi diagram** of the nuclei truncated at the expansion distance. The approximation fails for cells far from round (fibroblasts, neurons, macrophages) and in dense tissue, where it assigns the cytoplasm of one cell to another. When a membrane channel is available, a watershed on the membrane signal seeded by the nuclei follows actual boundaries.

Imaging transcriptomics offers a third source of information, the transcripts themselves: molecules of one cell tend to share a cell type. Baysor (Petukhov and colleagues, 2022) models molecules as points generated by cells, each with a spatial distribution and a composition over genes, with a Markov random field prior that favors neighboring molecules belonging to the same cell, and estimates the assignments iteratively, in the manner of an **EM algorithm**. Combining the nuclear image, a membrane stain and transcript composition is the current practice for subcellular platforms.

### 6.7.5. Three Dimensions

Volumes are segmented in three ways. Native three-dimensional models (3D StarDist, 3D U-Nets) need three-dimensional training annotations, which are laborious. Cellpose applies its two-dimensional network to the $xy$, $xz$ and $yz$ planes and averages the flows into a three-dimensional field, which requires roughly isotropic voxels. Alternatively, each plane is segmented in two dimensions and the masks are linked between consecutive planes, by thresholding their overlap (intersection over union) or, as in CellStitch (Liu and colleagues, 2023), by an optimal transport between the masks of neighboring planes (6.12.2), which tolerates the splitting and merging of masks along $z$. The same choices apply to serial sections, with registration first.

### 6.7.6. Evaluation

**Definition 6.7.2** The **intersection over union** (IoU) of two regions $A$ and $B$ is $\lvert A \cap B\rvert / \lvert A \cup B\rvert$, the Jaccard index of their pixel sets.

A predicted object matches a true object when their IoU exceeds a threshold $\tau$, usually $0.5$; at this threshold the matching is unique, since a region can overlap more than half of the union with at most one other region. With $\mathrm{TP}$ matched pairs, $\mathrm{FP}$ unmatched predictions and $\mathrm{FN}$ unmatched true objects, precision is $\mathrm{TP}/(\mathrm{TP} + \mathrm{FP})$, recall $\mathrm{TP}/(\mathrm{TP} + \mathrm{FN})$ and F1 their harmonic mean; segmentation benchmarks also report $\mathrm{TP}/(\mathrm{TP} + \mathrm{FP} + \mathrm{FN})$ averaged over $\tau$ from $0.5$ to $0.95$. Pixel-level metrics are misleading for segmentation, since merging two cells changes few pixels but loses a cell. The errors have characteristic types: over-segmentation (one cell split, an FN and two FPs) and under-segmentation (two cells merged, two FNs and one FP), and missed and spurious objects. Evaluation must use images from the tissue and platform at hand: a model accurate on one tissue can fail on another.

### 6.7.7. Human in the Loop, and Why Errors Matter

Because annotation is expensive and models must be adapted to each tissue, a three-step practice has become common: run a pretrained model zero-shot; correct its errors on a few representative regions in an interactive viewer; fine-tune the model on the corrections and apply it to the whole data set, repeating if necessary. Cellpose 2.0 showed that a small number of corrected images can adapt a generalist model to a new image type.

Segmentation errors do not remain local. Transcripts or protein signal of one cell assigned to its neighbor create cells that appear to co-express markers of two types, inflate apparent cell–cell interactions, and create artificial "intermediate" states.

**Example 6.7.1** A T cell with $10$ transcripts of *CD3E* lies between two tumor cells. If segmentation assigns $10\%$ of the T cell's transcripts to each tumor neighbor, the number of *CD3E* transcripts in each tumor cell is approximately $\mathrm{Poisson}$ with mean $1$, and $1 - \mathrm{e}^{-1} = 63\%$ of such tumor cells show at least one *CD3E* transcript. A rule "at least one *CD3E* molecule" for calling T cells would misclassify many tumor cells at the margin, exactly where T-cell infiltration is studied. Calls should use several markers, thresholds that account for contamination, and estimates of spillover such as those of 6.4.4.

## 6.8. Data Structures and the scverse Ecosystem

A spatial experiment produces several kinds of data that must stay aligned: images (multichannel, often multiscale), label images from segmentation, points (decoded transcripts), shapes (spot circles, cell polygons) and tables (the expression matrix with annotations). SpatialData (Marconato and colleagues, 2025) represents all of them in one object, stored on disk in OME-Zarr so that large elements are read lazily, chunk by chunk.

| Element | Content | Example |
|---|---|---|
| images | multichannel rasters, multiscale | morphology image, CODEX channels, H&E |
| labels | integer rasters of segmented objects | nucleus and cell masks |
| points | coordinates with attributes | decoded transcripts with gene and quality |
| shapes | circles and polygons | Visium spots, cell boundaries |
| tables | AnnData annotating any of these | counts per cell or spot, cell types |

Each element carries transformations (scaling, translation, affine maps) to one or more named coordinate systems, so that an image, its masks, the transcripts and an H&E image of the same section registered to it (6.13) can be queried together in physical units. Tables are AnnData objects ([7.9.1](/7.9.1)), the same structure as in single-cell analysis ([7.9.5](/7.9.5)): `X` holds the matrix, `obs` the cell annotations, `var` the genes, `obsm["spatial"]` the coordinates, and `obsp` the spatial graphs. MuData groups several AnnData tables of different modalities measured on the same cells. Scanpy provides the single-cell methods that apply unchanged to spatial tables (normalization, principal components, Leiden clustering), squidpy (Palla and colleagues, 2022) the spatial graphs and statistics (6.10), and napari an interactive viewer in which images, masks and points can be inspected and annotated, which is the interface for human-in-the-loop correction (6.7.7).

```python
import spatialdata as sd
import spatialdata_io
import scanpy as sc
import squidpy as sq

# read a Xenium run: morphology images, nucleus and cell labels, transcripts, boundaries, table
sdata = spatialdata_io.xenium("xenium_output/")
sdata.write("sample.zarr")                      # OME-Zarr; later sessions use sd.read_zarr
sdata = sd.read_zarr("sample.zarr")

# a region of interest in physical coordinates (micrometres), with the matching table rows
crop = sd.bounding_box_query(sdata, axes=("x", "y"), min_coordinate=[2000, 2000],
                             max_coordinate=[4000, 4000], target_coordinate_system="global")

adata = sdata.tables["table"]                   # cells x genes, coordinates in obsm["spatial"]
sc.pp.filter_cells(adata, min_counts=20)
sc.pp.normalize_total(adata)
sc.pp.log1p(adata)
sc.pp.pca(adata)
sc.pp.neighbors(adata)                          # expression graph
sc.tl.leiden(adata, key_added="cluster")

sq.gr.spatial_neighbors(adata, coord_type="generic", delaunay=True)   # spatial graph
sq.gr.nhood_enrichment(adata, cluster_key="cluster", n_perms=1000)    # 6.10.5
sq.gr.spatial_autocorr(adata, mode="moran", n_perms=999)              # 6.10.2
sq.gr.ripley(adata, cluster_key="cluster", mode="L")                  # 6.10.4
print(adata.uns["moranI"].head())
```

The expression graph and the spatial graph are distinct objects in the same table: the first connects cells with similar expression, the second cells that are close in the tissue, and most spatial methods combine the two.

## 6.9. Cell-Type Annotation

Annotation assigns a cell type or state to each segmented cell. Protein and transcript panels pose different problems.

For protein panels, the classical approach mimics **flow cytometry**: manual gating on scatter plots of marker intensities (CD45$^+$, then CD3$^+$, then CD8$^+$), applied hierarchically. Gating encodes expert knowledge but is slow and subjective, and image intensities are much noisier than cytometry: they depend on segmentation, spillover from neighbors (6.4.4) and staining variation across the slide. Unsupervised clustering of arcsinh-transformed or normalized intensities (**k-means clustering**, Leiden on a **k-nearest neighbors** graph) followed by manual labeling of clusters is fast, but clusters of tens of markers often mix types that differ in one marker. Supervised classifiers trained on labeled cells can use the image itself rather than per-cell means: CellSighter (Amitay and colleagues, 2023) is a **convolutional neural network** that classifies each cell from image crops of all channels around it, so that it can distinguish a true membrane signal from spillover of a neighbor; Nimbus (2025) predicts for each cell and marker whether the cell is positive, a calibrated building block for any rule-based or learned classifier. Graph-based methods use neighbors as context (STELLAR transfers labels between data sets with a graph neural network on the spatial graph). The current direction combines these with human-in-the-loop active learning: CellTune (Bussi and colleagues, 2026) iterates between classifier predictions and targeted expert corrections of the cells on which the model is least certain, reaching high precision with limited annotation.

For transcript panels, the usual route is reference mapping: a single-cell atlas of the same tissue provides labeled profiles, and each spatial cell is assigned by a classifier trained on the reference genes shared with the panel or by joint embedding of reference and query ([7.9.5](/7.9.5)). Two cautions apply. The panel contains only a few hundred to a few thousand genes, chosen to separate known types, so fine states not represented in the panel cannot be found. And a classifier always returns some label: cells with too few transcripts, cut cells (6.6.2) and segmentation errors (Example 6.7.1) need explicit "unassigned" or low-confidence categories.

Benchmarks of annotation methods for imaging data agree on a few points: supervised methods with good training labels beat clustering on rare and similar types; no method is best on all tissues and platforms; accuracy is limited more by segmentation and marker quality than by the classifier; and claims should be checked against held-out expert annotation of the same tissue, not only against the reference used for training.

## 6.10. Spatial Statistics

### 6.10.1. Spatial Graphs

Spatial statistics begin with a definition of neighbors. Three constructions are standard: the $k$ nearest neighbors of each cell (here a cell is the unit, and $k$ is typically $6$–$15$); all cells within a radius $r$; and the Delaunay triangulation, whose edges join cells whose Voronoi regions share a boundary, a natural approximation of physical contact. For grid data (spots), neighbors are the adjacent spots (six on the hexagonal Visium grid). The resulting graph ([1.4.1](/1.4.1)) is stored as a sparse **adjacency matrix** $W$ with entries $w_{ij}$, binary or weighted by distance, and sometimes row-normalized so that the weights of each cell sum to $1$.

### 6.10.2. Spatial Autocorrelation: Moran's I

A gene is spatially structured if its expression in neighboring cells is more similar than in random pairs.

**Definition 6.10.1 (Moran's I)** For values $x_1, \dots, x_n$ at $n$ locations with mean $\bar x$ and spatial weights $w_{ij}$ ($w_{ii} = 0$), with $S_0 = \sum_{i,j} w_{ij}$,
$$
I = \frac{n}{S_0}\,\frac{\sum_{i,j} w_{ij}(x_i - \bar x)(x_j - \bar x)}{\sum_i (x_i - \bar x)^2}, \qquad C = \frac{(n - 1)\sum_{i,j} w_{ij}(x_i - x_j)^2}{2 S_0 \sum_i (x_i - \bar x)^2}. \tag{6.2}
$$
Here **Moran's I** is a spatially weighted correlation of the values with themselves; **Geary's C** compares squared differences of neighbors with the overall variance.

$I > 0$ means that neighbors are similar (positive autocorrelation), $I < 0$ that they alternate, as in a checkerboard; $C < 1$ means positive autocorrelation, $C > 1$ negative. Moran's I is more sensitive to global structure, Geary's C to local differences.

**Proposition 6.10.1** Under the randomization hypothesis, that the observed values are assigned to the locations by a random permutation, $\mathbb{E}[I] = -1/(n - 1)$.

**Proof** Write $z_i = x_i - \bar x$, so $\sum_i z_i = 0$. Under a random permutation, for $i \neq j$ the pair $(z_{\pi(i)}, z_{\pi(j)})$ is a random ordered pair of distinct values, so $\mathbb{E}[z_{\pi(i)}z_{\pi(j)}] = \frac{1}{n(n-1)}\sum_{k \ne l} z_k z_l = \frac{(\sum_k z_k)^2 - \sum_k z_k^2}{n(n-1)} = -\frac{\sum_k z_k^2}{n(n-1)}$. The denominator of $I$ does not change under permutation, so $\mathbb{E}[I] = \frac{n}{S_0} \cdot S_0 \cdot \left(-\frac{1}{n(n-1)}\right) = -\frac{1}{n-1}$. $\square$

The null distribution can be approximated by a normal distribution with a variance computed from the weights, or obtained by permuting the values over the locations, which is exact for any weights and any distribution of the values: the p-value is $(1 + \#\{I^{(b)} \ge I\})/(B + 1)$ for $B$ permutations.

**Example 6.10.1** Five cells in a row, with values $1, 2, 3, 4, 5$ and binary weights between adjacent cells ($S_0 = 8$, each of the four adjacent pairs counted twice). The deviations are $-2, -1, 0, 1, 2$ with $\sum z_i^2 = 10$, and $\sum w_{ij} z_i z_j = 2\,(2 + 0 + 0 + 2) = 8$, so $I = \frac{5}{8} \cdot \frac{8}{10} = 0.5$. The squared differences of neighbors are all $1$, so $C = \frac{4 \cdot 8}{2 \cdot 8 \cdot 10} = 0.2$. Of the $120$ permutations of the values, $8$ give $I \ge 0.5$ (the monotone arrangements and a few near-monotone ones), so the exact one-sided p-value is $8/120 = 0.067$; their mean is exactly $-0.25 = -1/(n - 1)$. With so few cells even a perfect gradient is not significant.

![Spatial autocorrelation and clustering on synthetic data. A: a smooth field on a 30 × 30 grid (Gaussian-filtered noise), Moran's I = 0.85 with rook weights. B: the same values shuffled, I = −0.034. C: the permutation null of 999 random relabelings (identical for A and B, which have the same values), centred at −1/(n − 1) = −0.0011 with standard deviation 0.023: A lies far outside it (p = 0.001, the smallest attainable), B inside (p = 0.93). D: Ripley's L(r) − r for 300 points: complete spatial randomness stays within the range of 99 simulations (shaded), the clustered Thomas process lies far above it at short distances](./plots/morans_i.py)

In the figure, the smooth field has $I = 0.847$. The permutation null has standard deviation $0.0228$, close to the normal-theory value $0.0239$ for this grid, so $I$ lies about $37$ standard deviations above its expectation. With thousands of cells, almost every gene with any spatial structure is significant, and the value of $I$, not the p-value, ranks genes by the strength of their pattern.

### 6.10.3. Spatially Variable Genes

**Definition 6.10.2** A **spatially variable gene** is a gene whose expression depends on position in the tissue beyond what is explained by noise, so that the covariance of its expression between locations decreases with their distance.

Moran's I on normalized expression is the simplest test. Model-based methods make the dependence explicit. SpatialDE (Svensson, Teichmann and Stegle, 2018) models the normalized expression $\boldsymbol{y}$ of a gene at $n$ locations $\boldsymbol{s}_1, \dots, \boldsymbol{s}_n$ as a Gaussian process,
$$
\boldsymbol{y} \sim \mathcal{N}\big(\mu\boldsymbol{1},\ \sigma_s^2 K + \delta I_n\big), \qquad K_{ij} = \exp\!\left(-\frac{\|\boldsymbol{s}_i - \boldsymbol{s}_j\|^2}{2\ell^2}\right), \tag{6.3}
$$
where the **Gaussian kernel** $K$ with length scale $\ell$ describes spatially smooth variation of variance $\sigma_s^2$ and $\delta$ independent noise. The model is compared with the null model $\sigma_s^2 = 0$ by a likelihood ratio test; the fraction of variance $\sigma_s^2/(\sigma_s^2 + \delta)$ that is spatial and the length scale $\ell$ that maximizes the likelihood describe the pattern. Exact Gaussian-process likelihoods cost $O(n^3)$, too much for $10^5$ cells; SPARK (Sun, Zhu and Zhou, 2020) models counts directly with Poisson or negative binomial likelihoods and combines several kernels, SPARK-X (Zhu, Sun and Zhou, 2021) replaces the likelihood by a nonparametric test of the covariance between expression and transformed coordinates computable in $O(n)$, and nearest-neighbor Gaussian processes (nnSVG) approximate the likelihood with sparse neighborhoods.

Two confounders must be kept in mind. A gene expressed specifically in one cell type is spatially variable wherever that type is clustered, so a list of spatially variable genes largely recapitulates the cell-type map; the interesting question is often variation within a type, which requires conditioning on cell type. And technical factors, such as tissue thickness, RNA quality or capture efficiency that vary across a section, create smooth spatial patterns in all genes at once.

### 6.10.4. Point Patterns: Ripley's K

The positions of cells of one type form a point pattern. The reference is complete spatial randomness (CSR), a homogeneous Poisson process, in which the number of points in a region is Poisson-distributed with mean proportional to its area and counts in disjoint regions are independent.

**Definition 6.10.3** For $n$ points in a region of area $\lvert A\rvert$ with pairwise distances $d_{ij}$, **Ripley's K function** is estimated by
$$
\hat K(r) = \frac{\lvert A\rvert}{n(n-1)}\sum_{i \neq j} \boldsymbol{1}\{d_{ij} < r\}\, e_{ij}, \tag{6.4}
$$
with edge-correction weights $e_{ij}$; under CSR, $K(r) = \pi r^2$. The variance-stabilized form $L(r) = \sqrt{K(r)/\pi}$ equals $r$ under CSR.

$\lambda K(r)$, with $\lambda = n/\lvert A\rvert$ the intensity, is the expected number of further points within distance $r$ of a typical point. $L(r) - r > 0$ indicates clustering at scale $r$, $L(r) - r < 0$ regularity (inhibition, as between cells that cannot overlap at distances smaller than their diameter). Significance is assessed with envelopes from simulated CSR patterns with the same number of points. In the figure (panel D), $300$ points of a clustered Thomas process have $L(0.05) - 0.05 = 0.052$, while $99$ CSR simulations range from $-0.003$ to $0.003$. Cross-type versions ($K_{ab}$, counting points of type $b$ around points of type $a$) measure attraction or avoidance between types. Since tissues are not homogeneous, an inhomogeneous reference (with a varying overall cell density) is often more appropriate than CSR.

### 6.10.5. Neighborhood Enrichment

For annotated cells, a simpler question is whether types $a$ and $b$ are neighbors in the spatial graph more often than expected. The statistic is the number of edges between cells of types $a$ and $b$; its null distribution is obtained by permuting the type labels over the cells, keeping the graph fixed, and the result is a z-score $(N_{ab} - \bar N_{ab})/s_{ab}$ for each pair, or a permutation p-value.

**Example 6.10.2** Four hundred cells placed at random in a square are labeled $A$ on the left and $B$ on the right, with a blurred boundary (the label depends on the horizontal coordinate plus noise of standard deviation $0.1$). In the graph of $6$ nearest neighbors, $271$ of the $2400$ directed edges join different types; under $1000$ label permutations the mean is $1193$ with standard deviation $33$, a z-score of $-27.9$: strong segregation.

:::

The permutation of labels preserves the abundance of each type but not their spatial heterogeneity, so the z-scores grow with the number of cells and reflect any large-scale structure; they rank pairs within one sample better than they compare samples. Co-occurrence scores as a function of distance, and comparisons of the neighbor compositions of individual cells (6.11), give a more detailed picture.

## 6.11. Spatial Domains, Neighborhoods and Niches

### 6.11.1. Cellular Neighborhoods

The arrangement of cells can be summarized by their surroundings.

**Definition 6.11.1** The neighborhood composition of a cell is the vector of the proportions of each cell type among its $k$ nearest neighbors (or within a radius). A **cellular neighborhood** is a cluster of cells with similar neighborhood compositions; the label assigned to each cell by the clustering describes the kind of tissue region in which it sits.

In CODEX images of colorectal cancer, Schürch and colleagues (2020) computed the cell-type composition of windows of the $10$ nearest neighbors of each cell and grouped them by **k-means clustering** into nine conserved neighborhoods, such as follicles, bulk tumor, immune-infiltrated stroma and a granulocyte-enriched neighborhood; in a high-risk group of patients, PD-1$^+$ CD4$^+$ T cells correlated with survival only when they were located in the granulocyte-enriched neighborhood. Neighborhood analysis turns cell positions into a small number of interpretable regions that can be compared across patients.

### 6.11.2. Spatial Domains and the Potts Prior

For spot data or for expression without cell types, regions are found directly from expression.

**Definition 6.11.2** A **spatial domain** is a contiguous region of a tissue whose locations share an expression profile distinct from that of neighboring regions, such as a cortical layer or a tumor region.

Clustering spots by expression alone ignores that neighbors usually belong to the same domain, and yields noisy, fragmented domains. BayesSpace (Zhao and colleagues, 2021) adds a prior. Let $z_i \in \{1, \dots, q\}$ be the domain of spot $i$ and $\boldsymbol{y}_i$ its expression summarized by principal components. The model is
$$
\boldsymbol{y}_i \mid z_i = k \sim \mathcal{N}(\boldsymbol{\mu}_k, \Lambda^{-1}), \qquad p(z_1, \dots, z_n) \propto \exp\Big(\gamma \sum_{i \sim j} \boldsymbol{1}\{z_i = z_j\}\Big), \tag{6.5}
$$
where the sum is over neighboring spots and $\gamma > 0$ sets the strength of smoothing. The prior is a Potts model on the spatial graph, the same family of distributions as the Ising model of statistical physics (two states) and the Potts models of protein families ([7.6.15](/7.6.15)). The parameters and labels are sampled by a **Gibbs sampler**: the full conditional of one label is
$$
p(z_i = k \mid \boldsymbol{y}_i, z_{-i}) \propto \mathcal{N}(\boldsymbol{y}_i; \boldsymbol{\mu}_k, \Lambda^{-1}) \exp\big(\gamma\, m_{ik}\big), \tag{6.6}
$$
where $m_{ik}$ is the number of neighbors of $i$ in domain $k$.

**Example 6.11.1** A spot on the hexagonal grid has $4$ neighbors in domain $A$ and $2$ in domain $B$, and its expression favors $B$: the likelihood ratio is $p(\boldsymbol{y}_i \mid B)/p(\boldsymbol{y}_i \mid A) = \mathrm{e}^4 = 55$. Without smoothing ($\gamma = 0$), $\mathbb{P}(z_i = A) = 1/(1 + \mathrm{e}^4) = 0.018$. With $\gamma = 1$ the prior ratio is $\mathrm{e}^{1 \cdot (4 - 2)}$ and $\mathbb{P}(z_i = A) = 0.12$; with $\gamma = 3$ it is $\mathrm{e}^6 = 403$ and $\mathbb{P}(z_i = A) = 0.88$. The smoothing parameter decides whether an expression outlier inside a domain is kept or absorbed; too large a $\gamma$ erases thin structures such as a narrow layer.

:::

BayesSpace also refines resolution by dividing each spot into subspots that share the spot's data but have their own labels. Graph neural network methods learn embeddings of each location from its expression and that of its neighbors on the spatial graph (SpaGCN, STAGATE, GraphST) and cluster the embeddings; simpler methods augment each cell's expression with the mean expression of its neighbors before clustering (Banksy, CellCharter) and are competitive in benchmarks. Since the number of domains and the degree of smoothing are choices, domain maps should be shown at several settings and checked against anatomy.

### 6.11.3. Niches and Spatially Constrained Communication

**Definition 6.11.3** A **cellular niche** is the local microenvironment of a cell, the cells, extracellular matrix and signals within interaction range, considered as a determinant of the cell's state.

The concept, older in stem-cell biology, is made measurable by spatial data: a niche is characterized by the neighborhood composition and the expression of neighbors, and niche effects are estimated by relating a cell's state to its surroundings, for example by regressing a cell's expression on the composition of its neighborhood with cell type as a covariate. Ligand–receptor analysis ([7.9.7](/7.9.7)) gains a constraint: in dissociated data any ligand-expressing type might signal to any receptor-expressing type, whereas in space only pairs within the signal's range are candidates. Spatial versions restrict the permutation tests of co-expression to neighboring cells (squidpy), or model the distribution of each ligand over its possible receivers as an optimal transport limited by distance (COMMOT; Cang and colleagues, 2023). Such analyses remain inferences from co-localization and co-expression: they propose interactions to be tested by perturbation.

In tumors, these methods describe the tumor microenvironment ([7.9.13](/7.9.13)): whether T cells are excluded at the margin or infiltrate the tumor, the location of tertiary lymphoid structures, and the niches in which macrophages adopt immunosuppressive states. Spatial features of this kind are being evaluated as biomarkers of response to immunotherapy, for which the density of cells alone is often a weaker predictor than their arrangement.

## 6.12. Deconvolution and Mapping

### 6.12.1. The Mixture Model of a Spot

When each measurement mixes several cells (Example 6.2.1), the composition of each spot is estimated from a single-cell reference.

**Definition 6.12.1** **Cell-type deconvolution** estimates, for each spot, the proportions $\pi_{s1}, \dots, \pi_{sK}$ of $K$ reference cell types whose mixture best explains the spot's counts, given reference profiles $\mu_{gk}$ (the expected fraction of type $k$'s transcripts that come from gene $g$).

In the basic Poisson model, the count of gene $g$ in spot $s$ with $N_s$ molecules is
$$
y_{sg} \sim \mathrm{Poi}\Big(N_s \sum_{k} \pi_{sk}\,\mu_{gk}\Big), \qquad \sum_k \pi_{sk} = 1,\ \pi_{sk} \ge 0. \tag{6.7}
$$

**Algorithm 6.12.1 (EM for Mixture Weights)** For one spot, start with $\pi_k = 1/K$ and repeat until convergence:
1. E-step: for each gene, the expected fraction of its counts that comes from type $k$ is $r_{gk} = \pi_k\mu_{gk}/\sum_j \pi_j\mu_{gj}$.
2. M-step: $\pi_k \leftarrow \sum_g y_g r_{gk} / \sum_g y_g$.

Each iteration costs $O(GK)$ and increases the likelihood, as for any **EM algorithm**; it is the same algorithm as the assignment of reads to isoforms in pseudoalignment ([7.9.2](/7.9.2)), with cell types in the place of transcripts.

![Deconvolution of capture spots by a Poisson mixture (simulation). A: reference profiles of four cell types over 60 genes, 15 markers each. B: true and estimated proportions of 300 spots with 1000 UMIs each (Algorithm 6.12.1); mean absolute error 0.011. C: the error against the number of UMIs per spot: without a platform effect it falls roughly as one over the square root of depth (0.038 at 100 UMIs, 0.003 at 20000); with an uncorrected gene-specific platform effect (log-normal, sd 0.5) it levels off near 0.031](./plots/deconv.py)

The simulation in the figure shows the two sources of error. Sampling error decreases with depth. Systematic error does not: the reference comes from a different technology, whose capture efficiency differs from gene to gene, and a model that ignores this assigns the wrong proportions however deep the spot is sequenced. RCTD (Cable and colleagues, 2022) therefore includes gene-specific platform effects and spot-specific overdispersion (a log-normal term inside the Poisson), estimated across all spots, and allows a spot to contain only one or two types where the data support it; cell2location (Kleshchevnikov and colleagues, 2022) is a Bayesian negative binomial model with hierarchical priors on the number of cells per spot and on technical effects, fitted by variational inference. Benchmarks find these model-based methods among the most accurate. All deconvolution is limited by the reference: a cell type missing from it is explained as a mixture of the types present.

### 6.12.2. Optimal Transport and Mapping

Mapping methods go the other way and place each cell of a single-cell reference at locations in the tissue. Many of them use optimal transport, which also appears in segmentation (6.7.5), registration (6.13) and communication (6.11.3).

**Definition 6.12.2 (Optimal Transport)** Given distributions $\boldsymbol{a} \in \mathbb{R}^m$ and $\boldsymbol{b} \in \mathbb{R}^n$ (non-negative, each summing to $1$) and a cost matrix $C$, the **optimal transport** problem is
$$
\min_{P \ge 0} \sum_{i,j} C_{ij}P_{ij} \quad \text{subject to} \quad P\boldsymbol{1} = \boldsymbol{a},\ P^{\mathsf T}\boldsymbol{1} = \boldsymbol{b}; \tag{6.8}
$$
the plan $P$ says how much of the mass at source $i$ goes to target $j$. Adding the entropy term $\varepsilon\sum_{ij}P_{ij}(\log P_{ij} - 1)$ gives entropic optimal transport, whose solution is $P = \operatorname{diag}(\boldsymbol{u})\,\mathrm{e}^{-C/\varepsilon}\operatorname{diag}(\boldsymbol{v})$, with $\boldsymbol{u}, \boldsymbol{v}$ found by the Sinkhorn iteration $\boldsymbol{v} \leftarrow \boldsymbol{b}/(K^{\mathsf T}\boldsymbol{u})$, $\boldsymbol{u} \leftarrow \boldsymbol{a}/(K\boldsymbol{v})$, $K = \mathrm{e}^{-C/\varepsilon}$ (elementwise operations).

Problem (6.8) is a linear program; its constraints say that every source sends out exactly its mass and every target receives exactly its mass.

**Example 6.12.1** Three sources with masses $\boldsymbol{a} = (0.5, 0.3, 0.2)$ and three targets with $\boldsymbol{b} = (0.2, 0.3, 0.5)$ lie on a line at positions $1, 2, 3$, with squared distances as costs. The optimal plan sends $0.2$ from source $1$ to target $1$ and $0.3$ to target $2$, all of source $2$ to target $3$ and all of source $3$ to target $3$, at cost $0.3 \cdot 1 + 0.3 \cdot 1 = 0.6$. Entropic transport with $\varepsilon = 1$ spreads the mass (for example $0.09$ from source $1$ to the distant target $3$) at cost $0.81$; with $\varepsilon = 0.1$ it returns the exact plan. The entropic term trades exactness for smoothness and for an algorithm of simple matrix operations that runs on graphics processors.

:::

Tangram (Biancalani and colleagues, 2021) learns a mapping matrix $M$ (cells × spots, each row a probability distribution over spots) that maximizes the cosine similarity between the predicted spatial expression $M^{\mathsf T}X$ and the measured one, gene by gene and spot by spot, with optional constraints on cell densities, so it is an optimal-transport-like assignment with a learned cost. novoSpaRc (Nitzan and colleagues, 2019) reconstructs positions even without spatial expression data, from the assumption that cells close in space have similar expression: it finds a transport plan between cells and locations that makes the expression distances between cells agree with the physical distances between their assigned locations, a Gromov–Wasserstein problem (6.13.2). Mapping a whole-transcriptome reference onto a targeted spatial panel predicts the expression of unmeasured genes in space; such predictions inherit every error of the mapping and should be validated on held-out measured genes.

## 6.13. Registration and Multimodal Integration

### 6.13.1. Registration

**Definition 6.13.1** **Image registration** is the estimation of a transformation $T$ that maps coordinates of a moving image onto those of a fixed image of the same specimen, so that corresponding structures coincide.

Registration is needed between cycles of a cyclic assay, between modalities measured on the same section (for example an imaging assay and an H&E stain performed afterwards on the same slide), and between serial sections. Transformations are rigid (rotation and translation), similarity (plus a uniform scale), affine (any linear map plus translation, which absorbs anisotropic shrinkage and shear) or non-rigid (deformation fields, for tissue that folds, tears or stretches). With matched landmarks, such as the centroids of the same nuclei found in the nuclear channels of both images, the rigid and affine fits have closed forms.

**Theorem 6.13.1 (Kabsch)** Let $\boldsymbol{x}_1, \dots, \boldsymbol{x}_n$ and $\boldsymbol{y}_1, \dots, \boldsymbol{y}_n$ be matched points in $\mathbb{R}^k$ with centroids $\bar{\boldsymbol{x}}, \bar{\boldsymbol{y}}$, and let $H = \sum_i (\boldsymbol{x}_i - \bar{\boldsymbol{x}})(\boldsymbol{y}_i - \bar{\boldsymbol{y}})^{\mathsf T}$ have the **singular value decomposition** $H = U\Sigma V^{\mathsf T}$. The rotation $R$ and translation $\boldsymbol{t}$ minimizing $\sum_i \|R\boldsymbol{x}_i + \boldsymbol{t} - \boldsymbol{y}_i\|^2$ are
$$
R = V \operatorname{diag}(1, \dots, 1, \det(VU^{\mathsf T}))\, U^{\mathsf T}, \qquad \boldsymbol{t} = \bar{\boldsymbol{y}} - R\bar{\boldsymbol{x}}. \tag{6.9}
$$

**Proof** For fixed $R$, the optimal $\boldsymbol{t}$ makes the residuals sum to zero, which gives the second formula and reduces the problem to centered points. Then $\sum_i \|R\boldsymbol{x}_i' - \boldsymbol{y}_i'\|^2 = \sum_i (\|\boldsymbol{x}_i'\|^2 + \|\boldsymbol{y}_i'\|^2) - 2\operatorname{tr}(RH)$, so $R$ must maximize $\operatorname{tr}(RH) = \operatorname{tr}(\Sigma\, V^{\mathsf T}RU)$. The matrix $Z = V^{\mathsf T}RU$ is orthogonal, so its diagonal entries are at most $1$ and $\operatorname{tr}(\Sigma Z) \le \sum_l \sigma_l$, with equality at $Z = I$, that is $R = VU^{\mathsf T}$. If $\det(VU^{\mathsf T}) = -1$ this is a reflection; among rotations the maximum of $\operatorname{tr}(\Sigma Z)$ is attained by $Z = \operatorname{diag}(1, \dots, 1, -1)$, changing the sign of the smallest singular value. $\square$

The same algorithm superimposes protein structures ([7.8.17](/7.8.17)). The affine fit is ordinary **least squares**: with $\tilde{\boldsymbol{x}}_i = (\boldsymbol{x}_i^{\mathsf T}, 1)^{\mathsf T}$, the map $\boldsymbol{y} \approx A\boldsymbol{x} + \boldsymbol{t}$ has $[A\ \boldsymbol{t}]$ solving the normal equations of the regression of each coordinate of $\boldsymbol{y}_i$ on $\tilde{\boldsymbol{x}}_i$, and needs at least three non-collinear landmarks in two dimensions.

![Landmark registration using matched nucleus centroids. The moving image (orange) is the fixed one (blue) rotated by 8°, scaled by 1.03 and 0.98 along its axes, sheared and translated, with centroid noise of 0.8 µm. A: before registration. B: best rigid fit by the Kabsch algorithm; residuals magnified 10×: systematic, because a rotation cannot absorb anisotropic shrinkage (RMS 3.6 µm). C: least-squares affine fit; residuals are noise (RMS 1.13 µm). D: error at 200 held-out nuclei against the number of landmarks used: the rigid error stays near 3.4 µm, the affine error falls towards that of the true transform (dashed) as landmarks are added](./plots/registration.py)

**Example 6.13.1** In the figure, $60$ matched nuclei give a rigid fit with root-mean-square residual $3.6\,\mu\mathrm{m}$ and a recovered rotation of $-7.4^\circ$ (the inverse of the applied $8^\circ$, biased by the shear), and an affine fit with residual $1.13\,\mu\mathrm{m}$, whose matrix agrees with the inverse of the applied map to within $0.002$ in every entry. On $200$ held-out nuclei the affine error is $2.3\,\mu\mathrm{m}$ with $3$ landmarks, $1.4\,\mu\mathrm{m}$ with $6$ and $1.07\,\mu\mathrm{m}$ with $60$, against $1.05\,\mu\mathrm{m}$ for the true transform. For transcripts that are localized to within a micrometre, the choice between rigid and affine matters: a $3.6\,\mu\mathrm{m}$ error moves molecules between neighboring cells.

:::

In practice correspondences are not known. They are found by matching features (nucleus positions and shapes, or image descriptors) with robust estimation that tolerates wrong matches (RANSAC: fit to random minimal subsets, keep the fit with most inliers), by iterating between nearest-neighbor matching and refitting (the iterative closest point algorithm), or by maximizing an intensity similarity such as mutual information over the transformation parameters. A coarse affine registration is then refined by a non-rigid deformation where the tissue requires it, with smoothness penalties that prevent the deformation from inventing structure; for whole-slide images, tools such as VALIS chain these steps. The quality of a registration is reported as the residual distance between held-out landmarks.

### 6.13.2. Aligning Sections Without Landmarks

Serial sections, or sections measured with different technologies, do not share individual cells. PASTE (Zeira and colleagues, 2022) aligns spots of two adjacent sections with a fused Gromov–Wasserstein optimal transport: the plan $P$ between the spots of section $1$ and section $2$ minimizes
$$
(1 - \alpha)\sum_{i,j} M_{ij}P_{ij} + \alpha \sum_{i,j,k,l}\big(D_{ik} - D'_{jl}\big)^2 P_{ij}P_{kl}, \tag{6.10}
$$
where $M_{ij}$ is the expression dissimilarity of spots $i$ and $j$, and $D$, $D'$ are the physical distances within each section; the second term prefers plans that preserve distances, so that neighboring spots map to neighboring spots, without requiring the two coordinate systems to be aligned in advance. The plan then gives a rigid transformation by a weighted Kabsch fit, and a stack of sections aligned pairwise forms a three-dimensional reconstruction. Successors handle partial overlap (PASTE2) and time series, and general frameworks such as moscot provide optimal transport for spatial and temporal alignment at scale. Diffeomorphic methods (STalign) register cell positions or images to each other and to anatomical atlases.

### 6.13.3. Integrating Modalities

Multi-omics integration in space (reviewed by Tran and colleagues, 2025) can be grouped into three forms. In the first, several modalities are measured on the same section, in one assay (RNA and protein panels on one instrument) or sequentially, with the nuclear stain or the tissue morphology providing landmarks for registration; after registration and segmentation, each cell carries several feature sets, stored as a multimodal table, and the modalities can be compared cell by cell. In the second, modalities come from adjacent sections, and integration proceeds through registration and shared structure, at the level of regions rather than cells. In the third, modalities are linked only through a common embedding learned from paired training data, as when expression is predicted from H&E morphology (6.14). Each step removes some certainty: same-cell integration is limited by registration and segmentation errors, adjacent-section integration by the fact that the cells differ, and embedding-based integration by how well the training data represent the new sample.

## 6.14. AI and Large Models: Prospects

Deep learning already performs the image-level tasks of spatial omics: segmentation (6.7), cell classification (6.9) and decoding of molecular signals. The question for the coming years is whether large models trained on many tissues will do more: integrate scales, translate between modalities, and predict the effects of perturbations. The tasks and the model families proposed for them can be summarized as follows.

| Task | Model family | Current state |
|---|---|---|
| Cross-scale integration: molecules, cells, niches, tissue, patient | **foundation model** pretrained on many tissues | single-cell, spatial and pathology foundation models learn transferable representations; gains over simple baselines vary by task |
| Cross-modal generation: predict expression or protein from H&E, or one panel from another | universal embedding spaces, contrastive and generative models | expression of well-defined, abundant genes can be predicted from morphology; benchmarks (such as HEST-1k) show modest correlations for most genes |
| From two to three dimensions; interpolation between sections | video generation models, which learn the continuity of consecutive frames | prospective; current reconstructions use registration and interpolation of aligned sections (6.13.2) |
| Perturbation prediction: how a tissue responds to a drug or a mutation | world models, which simulate the dynamics of a system under actions | prospective; for single cells, deep-learning predictors of perturbation effects do not yet outperform simple linear baselines (Ahlmann-Eltze, Huber and Anders, 2025) |

The table separates what exists from what is proposed. Foundation models are pretrained by **self-supervised learning** (masking genes or image patches and predicting them), usually with **vision Transformer** or Transformer architectures ([4.7.6](/4.7.6), [4.7.7](/4.7.7)), and then adapted to tasks. Their promise is that a representation learned from millions of cells in thousands of tissues captures regularities that no single study can. Their limits are equally clear: spatial data sets are still far fewer than images or text, technologies and panels differ, so models must handle different gene sets, and evaluations often compare against weak baselines. The history of single-cell foundation models, whose zero-shot embeddings and perturbation predictions were often matched by principal components or linear models, argues for benchmarks with strong simple baselines before biological conclusions are drawn from model outputs.

The software that supports analysis is changing along three lines. The first is computation: parallel and out-of-core execution, graphics processors and memory-efficient formats, without which whole-slide and three-dimensional data cannot be analyzed (6.6.3). The second is integration: shared data structures and ecosystems (scverse, SpatialData) that let methods be combined, and registration that places different modalities and sections in one coordinate system (6.13). The third is interaction: human-in-the-loop correction of segmentation and annotation (6.7.7, 6.9), and agents built on large language models that plan and execute analysis steps with these tools. The last is the least mature; it accelerates routine work, but the choices that determine biological conclusions, which cells to trust, which null model to use, what counts as a niche, still require understanding of the methods described in this chapter.

## Summary

- Spatial omics (Definition 6.1.1) measures molecules in place, recovering the structure, context and communication lost by dissociation (6.1). Technologies differ by layer and readout: capture and sequencing are untargeted but coarser, imaging is targeted and subcellular, mass spectrometry measures metals or metabolites (6.2); a $55\,\mu\mathrm{m}$ spot holds parts of $5$ to $40$ cells (Example 6.2.1).
- Imaging transcriptomics counts single molecules (smFISH), limited by the point spread function and optical crowding (Example 6.3.1). Codes multiplex: sequential colour codes ($F^N$), and MERFISH codebooks with Hamming distance $4$ (Definition 6.3.1) that correct single errors; with $p_{10} = 0.1$, $p_{01} = 0.04$ the yield rises from $40\%$ to $78\%$ and misidentification falls from $9.3\%$ to $2.1\%$ (Example 6.3.2). Xenium and in situ sequencing amplify padlock probes by rolling circles and decode them in cycles (6.3.3).
- Imaging proteomics multiplexes antibodies by cycles of DNA-barcoded reporters (CODEX) or fluorophore inactivation (CyCIF), or by metal tags read by mass spectrometry (IMC, MIBI; $83\,\mathrm{min}$ per $\mathrm{mm}^2$, Example 6.4.1). Channel spillover is removed by non-negative least squares, Formula 6.4.1; lateral spillover between touching cells needs separate correction (6.4.4).
- Capture arrays (Visium, Slide-seq, Stereo-seq, Visium HD) are limited by feature size and by diffusion of molecules before capture ($\sqrt{2Dt} \approx 11\,\mu\mathrm{m}$, Example 6.5.1); mass spectrometry imaging maps metabolites; barcoding extends to DNA and chromatin (6.5).
- Scale grows in cohort, resolution, area, panel and dimension (6.6.1). Thin sections cut every cell (Example 6.6.2), which three-dimensional imaging of thick sections avoids. Large images are processed in tiles with halos larger than the largest object and stitched by IoU with union–find (Algorithm 6.6.1, Proposition 6.6.1), with chunked storage and parallel computation (6.6.3).
- Cell segmentation (Definition 6.7.1) uses the watershed (Algorithm 6.7.1; F1 from $0.47$ to $0.99$ on touching nuclei) and learned models (Cellpose flows, StarDist polygons, Mesmer); nuclei are expanded or combined with membrane and transcript information; three-dimensional segmentation is native, multi-plane or stitched; errors are measured by IoU-matched F1 (Definition 6.7.2) and propagate into false co-expression (Example 6.7.1) (6.7).
- SpatialData stores images, labels, points, shapes and AnnData tables with coordinate transformations in OME-Zarr; squidpy and scanpy provide the analyses (6.8). Annotation combines gating, clustering, image-based classifiers and active learning for proteins, and reference mapping for transcript panels (6.9).
- Spatial statistics: graphs of neighbors (6.10.1); Moran's I and Geary's C, Eq. (6.2), with $\mathbb{E}[I] = -1/(n-1)$ under randomization (Proposition 6.10.1, Example 6.10.1); spatially variable genes by Gaussian processes, Eq. (6.3), and scalable tests (Definition 6.10.2); Ripley's K and L, Eq. (6.4); neighborhood enrichment by label permutation (Example 6.10.2).
- Cellular neighborhoods cluster neighbor compositions (Definition 6.11.1); spatial domains (Definition 6.11.2) are smoothed by a Potts prior sampled by Gibbs sampling, Eqs. (6.5)–(6.6), whose strength $\gamma$ decides the fate of outliers (Example 6.11.1); niches (Definition 6.11.3) constrain ligand–receptor inference to cells within range.
- Deconvolution (Definition 6.12.1) fits Poisson mixtures, Eq. (6.7), by EM (Algorithm 6.12.1); platform effects cause bias that depth does not remove. Optimal transport (Definition 6.12.2, Eq. (6.8)) underlies mapping (Tangram, novoSpaRc), section alignment and communication models (6.12).
- Registration (Definition 6.13.1) fits rigid maps by the Kabsch algorithm (Theorem 6.13.1) and affine maps by least squares (Example 6.13.1: $3.6$ against $1.13\,\mu\mathrm{m}$); sections without shared cells are aligned by fused Gromov–Wasserstein transport, Eq. (6.10). Integration is same-cell, same-region or embedding-based (6.13.3).
- Foundation, embedding, video and world models are proposed for cross-scale integration, cross-modal generation, three-dimensional interpolation and perturbation prediction; current evidence calls for strong baselines. Tools move toward parallel computation, integrated ecosystems with registration, and human-in-the-loop and agent-assisted analysis (6.14).

## Questions

1. Explain why a MERFISH code with minimum Hamming distance $4$ can correct one error and detect two, but a code with distance $3$ can only correct one error without detecting double errors. Why are constant-weight codes preferred?

   **Answer** Balls of radius $1$ around codewords at distance $\ge 3$ are disjoint, so a word with one error has a unique nearest codeword; at distance $4$, a word with two errors is at distance $\ge 2$ from all codewords, and could be equidistant from two, so it is recognized as uncorrectable and discarded. At distance $3$, a word with two errors from codeword $c$ can be at distance $1$ from another codeword $c'$ and is silently "corrected" to the wrong gene. Constant weight equalizes the number of "on" rounds, so all genes have the same brightness and the same error probabilities (errors $1 \to 0$ and $0 \to 1$ differ), and a small weight limits the density of visible spots per round.

2. Using the error model of Example 6.3.2, compute the probability that a molecule is read exactly for a code of length $16$ and weight $6$ instead of $4$. What does this suggest about the choice of weight?

   **Answer** $0.9^6 \cdot 0.96^{10} = 0.531 \cdot 0.665 = 0.353$, lower than $0.402$ for weight $4$, because "on" bits are lost more often than "off" bits are gained. More ones also mean more spots per round. Higher weights allow more codewords (there are many more weight-$6$ words), but at a cost in exact reads and crowding; low weights with long words are the usual compromise.

3. A tissue has $2\times10^5$ cells per $\mathrm{mm}^3$ of diameter $10\,\mu\mathrm{m}$. How many cell profiles does a Visium spot contain on average in a $10\,\mu\mathrm{m}$ section, and how many in a $2 \times 2\,\mu\mathrm{m}$ Visium HD square? What follows for analysis?

   **Answer** With $n_V = 2\times10^{-4}\,\mu\mathrm{m}^{-3}$ and $T + d = 20\,\mu\mathrm{m}$, a spot of $2376\,\mu\mathrm{m}^2$ contains $2\times10^{-4} \cdot 20 \cdot 2376 = 9.5$ profiles. A $4\,\mu\mathrm{m}^2$ square contains on average $2\times10^{-4} \cdot 20 \cdot 4 = 0.016$ cell centers within the slab, i.e. it almost always lies inside one cell (or between cells), but it holds only a few molecules. Spots are deconvolved (6.12); HD squares are aggregated, by binning or, better, by assigning squares to cells segmented in the image.

4. In Example 6.4.2, why would inverting $S$ without the non-negativity constraint be a problem for a cell that expresses none of the three markers?

   **Answer** For $\boldsymbol{x} = \boldsymbol{0}$ the measurement is pure noise, $\boldsymbol{y} = \boldsymbol{\varepsilon}$, and $S^{-1}\boldsymbol{\varepsilon}$ has negative components about half of the time, which are physically impossible and distort means, thresholds and clustering (for example, negative values after an arcsine-type transformation). NNLS sets these components to zero; it still leaves positive noise, which is why thresholds must be set from negative controls.

5. Prove that with a halo $h$ smaller than the largest object diameter, Algorithm 6.6.1 can lose an object, and give the smallest halo that is safe for cells of diameter $25\,\mu\mathrm{m}$ imaged at $0.5\,\mu\mathrm{m}$ per pixel. What is the extra cost in two and three dimensions with tiles of $2048$ pixels?

   **Answer** Take an object of diameter $d > h$ that crosses a tile corner so that it extends more than $h$ beyond the boundary of each of the four tiles it touches; then every window cuts it, it touches an inner edge in every window, and step 3 discards all its versions. A safe halo is $h > d$, that is more than $25\,\mu\mathrm{m} = 50$ pixels (Proposition 6.6.1). Taking the limit $h = 50$ with $L = 2048$: $(1 + 100/2048)^2 - 1 = 10.0\%$ in two dimensions and $(1.0488)^3 - 1 = 15.4\%$ in three.

6. In Example 6.10.1, list the arrangements of $1, \dots, 5$ in a row with $I \ge 0.5$ and verify that there are $8$.

   **Answer** Here $I = \frac{5}{8}\cdot\frac{2\sum_{\text{adjacent}} z_i z_j}{10}$, so $I \ge 0.5$ means $\sum_{\text{adjacent}} z_i z_j \ge 4$ for the deviations $-2, -1, 0, 1, 2$. The value $4$ is the maximum and is reached when $0$ is in the middle, the two negative deviations on one side and the two positive on the other, in either internal order: $(1, 2, 3, 4, 5)$, $(2, 1, 3, 4, 5)$, $(1, 2, 3, 5, 4)$, $(2, 1, 3, 5, 4)$ and their four reverses. For example $(2, 1, 3, 5, 4)$ has deviations $(-1, -2, 0, 2, 1)$ and products $2 + 0 + 0 + 2 = 4$, because swapping the two values on one side does not change the product within the pair. These $8$ arrangements all have $I = 0.5$ exactly, so $p = 8/120 = 0.067$.

7. A gene has Moran's I of $0.30$ in a section with $50\,000$ cells, with p-value below $10^{-100}$. A second gene has $I = 0.05$ and p-value $10^{-30}$. Which is more interesting, and what additional analysis would you do before calling either a spatially variable gene of biological interest?

   **Answer** Both p-values are meaningless as measures of importance: with $50\,000$ cells, tiny autocorrelations are significant (the null standard deviation is of order $1/\sqrt{n}$). $I = 0.30$ is a much stronger pattern than $0.05$. Before interpreting, check whether the pattern follows cell-type composition (compute $I$ within each type, or of residuals after regressing on type), whether it follows technical gradients shared by many genes (total counts per cell, tissue quality), and whether it is reproducible in another section; then describe the pattern (domain, gradient, scale $\ell$).

8. In the BayesSpace model, Eq. (6.6), a spot has $3$ neighbors in each of two domains. How does $\gamma$ affect its label, and why is this an argument for not setting $\gamma$ too high?

   **Answer** With $m_{iA} = m_{iB} = 3$, the prior factors $\mathrm{e}^{3\gamma}$ cancel, and the label is decided by the likelihood alone, whatever $\gamma$. At boundaries the prior is neutral; inside a domain, a large $\gamma$ forces every spot to the majority label of its neighbors even when its expression clearly differs, which erases small or thin structures (a narrow layer, a small lesion). $\gamma$ should be chosen by checking domains against known anatomy or by stability across values, not maximized.

9. Show that in Algorithm 6.12.1 the M-step update keeps the proportions non-negative and summing to $1$, and explain why a cell type absent from the reference is a problem that more sequencing does not solve.

   **Answer** $r_{gk} \ge 0$ and $\sum_k r_{gk} = 1$ for every gene, so $\sum_k \pi_k^{\text{new}} = \sum_g y_g \sum_k r_{gk}/\sum_g y_g = 1$ and every $\pi_k^{\text{new}} \ge 0$. A missing type has no column $\mu_{\cdot k}$; the model must explain its transcripts as a mixture of the available profiles, choosing the combination closest in Poisson likelihood. This is a bias of the model, not sampling noise: more UMIs make the wrong answer more precise. A residual analysis (genes systematically underpredicted in some spots) can reveal the missing type.

10. Why does the rigid fit in Example 6.13.1 recover a rotation of $-7.4^\circ$ rather than $-8^\circ$? Design a check that would detect, from held-out landmarks, that a rigid model is inadequate.

    **Answer** The applied map is a rotation composed with anisotropic scaling and shear; its best rigid approximation absorbs part of the shear as rotation, so the fitted angle is biased. Fit both models on part of the landmarks and compute the errors at held-out landmarks: if the rigid error ($3.4\,\mu\mathrm{m}$) is well above the affine error ($1.07\,\mu\mathrm{m}$) and the rigid residuals show a systematic pattern (growing with distance from the center, aligned with an axis), the rigid model is inadequate; the affine error approaching the localization noise indicates that a non-rigid model is unnecessary.

11. (Design) You want to know whether CD8$^+$ T cells are excluded from tumor nests in a cohort of $100$ patients. Choose a technology, describe the analysis from images to a patient-level statistic, and name three sources of error you would control.

    **Answer** A whole-slide cyclic protein assay (CyCIF or CODEX, $\sim 30$ markers including pan-cytokeratin, CD8, CD3, CD45 and a membrane cocktail) gives cellular resolution over whole sections at cohort scale; IMC would cover only small regions. Analysis: register cycles; segment nuclei and cells with a model fine-tuned on corrected examples (6.7.7); compensate spillover (6.4.4); classify cells with a supervised or active-learning classifier; define tumor nests as regions of cytokeratin-positive cells (for example a domain or a smoothed density); compute per patient the ratio of CD8$^+$ densities inside and outside nests, or a cross-type $K$ or neighbor-enrichment statistic, with a confidence interval by spatial block bootstrap; relate it to outcome by a regression with clinical covariates ([7.7](/7.7)). Errors: segmentation and lateral spillover creating false CD8$^+$ tumor cells (Example 6.7.1); batch effects across slides and staining runs (include controls on each slide, normalize per batch); and sampling, since a single section may not represent the tumor (several regions or sections per patient, blinded definition of nests).
