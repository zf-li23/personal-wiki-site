---
title: "The Cell by the Numbers: Census, Sizes and Timescales"
description: "Quantitative reasoning about cells before any model is built. E. coli as a standard ruler and stopwatch; the molecular census (proteins, ribosomes, lipids, water, ions) by estimate and by measurement, and counting molecules from the binomial noise of partitioning at division; concentrations as copy numbers, spacings and encounter times; sizes from yeast, organelles and viruses to multicellular organisms; the hierarchy of time scales, the material budget of a cell cycle and the speeds of the machines of the central dogma; procedural time (synthesis, lifetimes, clocks), relative time (checkpoints, assembly order, viral life cycles, development) and manipulated time (enzymes, motors, channels, multifork replication, dormancy); model organisms from a physical point of view."
---

Before a cell can be modeled it has to be measured: how big it is, how many molecules of each kind it contains, how fast its processes run. These numbers are not decoration. They decide whether a concentration or a count is the right variable, whether a reaction is limited by diffusion, whether a machine is fast enough for the task the cell needs done, and whether equilibrium ideas apply at all, which depends on the separation of time scales. This chapter assembles them, following the plan of the first part of *Physical Biology of the Cell*: the bacterium *Escherichia coli* serves as the standard ruler for sizes and molecular counts (20.1–20.3) and as the standard stopwatch for times (20.4), and the times of life are then read in three ways, as the duration of a procedure (20.5), as the order of events (20.6) and as a quantity that cells actively shorten or stretch (20.7). The chapter ends with the model organisms on which these numbers were measured (20.8). The orders of magnitude of lengths, times and energies were surveyed in [7.6.1](/7.6.1); the cell biology behind the numbers is in [7.3](/7.3), especially the scale of cells and copy numbers in [7.3.1](/7.3.1#sec-1.3), and the tables of molecular-biology numbers in [7.2.1](/7.2.1#sec-1.5). Here the emphasis is on the reasoning: each number is derived from a few others by a **Fermi estimate** ([7.6.1](/7.6.1#sec-1.5.2)) and then compared with measurement.

## 20.1. *E. coli* as a Standard Ruler

### 20.1.1. Size, Volume and Mass

An *E. coli* cell grown at $37\,^\circ\mathrm{C}$ in a minimal medium with glucose is a rod about $2\,\mu\mathrm{m}$ long and $0.8$–$1\,\mu\mathrm{m}$ wide. For estimates we use the round numbers

$$
V_{\mathrm{E.\,coli}} \approx 1\,\mu\mathrm{m}^3 = 1\,\mathrm{fL}, \qquad A_{\mathrm{E.\,coli}} \approx 6\,\mu\mathrm{m}^2, \qquad m \approx 1\,\mathrm{pg}, \tag{20.1}
$$
with a dry mass of about 30 % of the total, half of it protein. The area follows from idealizing the cell as a spherocylinder (Question 1). Cell size is not fixed: it depends on the growth condition, and faster-growing cells are larger. Schaechter, Maaløe and Kjeldgaard showed in 1958 that across nutrient conditions the average mass of *Salmonella* grows exponentially with the growth rate, one of the first quantitative regularities of bacterial physiology; its modern form, together with the allocation of the proteome between ribosomes and other proteins, is the subject of [7.6.39](/7.6.39), and the control of size in single cells is in [7.3.22](/7.3.22). Single-cell measurements of buoyant mass with a resonating hollow cantilever (Godin and colleagues, 2010) confirmed that the growth rate of an individual cell increases with its mass, as exponential growth requires. Throughout this chapter the reference condition is glucose minimal medium, with a doubling time of about $50\,\mathrm{min}$ (20.4).

### 20.1.2. Taking the Census

The number of proteins, about $3\times10^6$, was estimated from the dry mass in [Example 1.5.1](/7.6.1#sec-1.5.2). The same reasoning, with one additional fact for each class of molecule, gives the rest of the inventory.

**Example 20.1.1 (The census by estimate)** (a) *Ribosomes.* About 20 % of the protein mass is ribosomal protein, and a ribosome of $2.5\,\mathrm{MDa}$ is one third protein ($0.83\,\mathrm{MDa}$) and two thirds rRNA. Hence

$$
N_{\mathrm{rib}} \approx \frac{0.2\times0.15\,\mathrm{pg}}{0.83\times10^6\,\mathrm{Da}\times1.66\times10^{-24}\,\mathrm{g\,Da^{-1}}} \approx 2\times10^4,
$$
which occupy $2\times10^4\times\frac{\pi}{6}(20\,\mathrm{nm})^3 \approx 10^8\,\mathrm{nm}^3$, about 10 % of the cell volume. (b) *Lipids.* The inner and outer membranes are two bilayers, so lipids cover the area four times; if half of the area is protein and a lipid occupies $0.5\,\mathrm{nm}^2$,

$$
N_{\mathrm{lip}} \approx \frac{4\times0.5\times6\times10^6\,\mathrm{nm}^2}{0.5\,\mathrm{nm}^2} \approx 2.4\times10^7 .
$$
(c) *Water.* 70 % of $1\,\mathrm{pg}$ is $0.7\,\mathrm{pg}$, or $0.7\times10^{-12}/18\times6.0\times10^{23} \approx 2.3\times10^{10}$ molecules. (d) *Ions.* At about $0.3\,\mathrm{M}$ total small ions (mostly $\ce{K+}$ and its counterions), $0.3\times6\times10^{23}\times10^{-15} \approx 2\times10^8$. (e) *Carbon.* About half of the dry mass is carbon: $0.15\,\mathrm{pg}/(12\,\mathrm{g\,mol^{-1}})\times N_{\mathrm{A}} \approx 10^{10}$ atoms, the material that must be taken up to make a new cell.

The measured census agrees with these estimates to within a factor of two.

| Substance | % of dry mass | Molecules per cell | Estimate |
|---|---|---|---|
| Protein | 55 | $2.4\times10^6$ | $3\times10^6$ ([Example 1.5.1](/7.6.1#sec-1.5.2)) |
| rRNA (23S, 16S, 5S) | 16.5 | $1.9\times10^4$ of each | $2\times10^4$ ribosomes |
| tRNA | 2.9 | $2\times10^5$ | |
| mRNA | 0.8 | $1.4\times10^3$ | |
| Phospholipid | 9.1 | $2.2\times10^7$ | $2.4\times10^7$ |
| Lipopolysaccharide | 3.4 | $1.2\times10^6$ | |
| DNA | 3.1 | 2.1 genome equivalents | |
| Peptidoglycan | 2.5 | 1 sacculus | |
| Glycogen | 2.5 | $4.4\times10^3$ granules | |
| Small molecules and ions | 3.9 | water $2.3\times10^{10}$, ions $\sim 2\times10^8$ | as estimated |

The table is for *E. coli* B/r doubling every 40 minutes (Neidhardt, 1990). The census immediately reveals the physical character of the cytoplasm: with $3\times10^6$ proteins of $5\,\mathrm{nm}$ and $2\times10^4$ ribosomes of $20$–$25\,\mathrm{nm}$ in $1\,\mathrm{fL}$, macromolecules occupy 20–30 % of the volume, and their mean spacing (20.2) is comparable to their size. This **macromolecular crowding** changes chemical equilibria and slows diffusion ([7.6.23](/7.6.23)).

![A molecular census of one *E. coli* cell (B/r, 40 min doubling time): numbers of molecules per cell on a logarithmic axis, from the compilation of Neidhardt (1990), with water and inorganic ions estimated from the wet mass. Open diamonds: the estimates of Example 20.1.1 and Example 1.5.1 of 7.6.1. Ten orders of magnitude separate water from the single peptidoglycan sacculus; proteins and lipids number in the millions, ribosomes in the tens of thousands, mRNAs in the thousands, and the genome is present in about two copies](./plots/ecoli-census.py)

### 20.1.3. How the Census Is Measured

The classical census came from biochemistry: cells were broken open, and the mass of each class of molecule was determined after separation. For proteins, **two-dimensional gel electrophoresis** (O'Farrell, 1975) separates the proteome by isoelectric point in one direction and by size, after binding of the detergent SDS, in the other; the intensity of each stained spot measures abundance, and the identity of a spot is determined by **mass spectrometry**. Three modern methods count proteins gene by gene:

| Method | What is counted | Range and limitations |
|---|---|---|
| Quantitative mass spectrometry | peptides from the whole proteome, calibrated with labeled standards | thousands of proteins at once; abundances of rare proteins less accurate |
| Fluorescent-protein fusion libraries with single-molecule calibration (Taniguchi and colleagues, 2010) | protein and mRNA copy numbers in single cells | about 1000 *E. coli* genes; reveals cell-to-cell variation; fusions may perturb |
| Ribosome profiling (Li and colleagues, 2014) | rates of synthesis of every protein from the density of ribosomes on its mRNA | near-complete; synthesis rate equals abundance only when degradation is negligible |

The methods agree on the overall shape of the distribution but can differ for individual proteins by factors of two to ten, from differences in growth condition and from systematic errors of each method. The single-cell measurements showed that copy numbers range over six orders of magnitude, from less than one molecule per cell on average (many transcription factors) to $10^5$ (ribosomal proteins, elongation factor Tu), and that most mRNAs are present at less than one copy per cell, with large variation from cell to cell ([7.2.22](/7.2.22)).

### 20.1.4. Counting Molecules by Their Partition Noise

Small numbers fluctuate, and the fluctuations themselves can be used to count. At division, molecules that are free in the cytoplasm go to one daughter or the other at random. If each of $N$ molecules goes to daughter 1 with probability $p = 1/2$, the number $n_1$ it receives follows the **binomial distribution** with mean $N/2$ and variance $N/4$, so the relative spread is $1/\sqrt{N}$ (Eq. (1.4) of [7.6.1](/7.6.1#sec-1.5.2)).

**Proposition 20.1.1 (Fluorescence Calibration by Partitioning)** Let each molecule contribute a fluorescence $\alpha$, so that the daughters have intensities $I_1 = \alpha n_1$ and $I_2 = \alpha(N - n_1)$. Under binomial partitioning with $p = 1/2$,

$$
\langle(I_1 - I_2)^2\rangle = \alpha\,(I_1 + I_2). \tag{20.2}
$$
A plot of the squared intensity difference against the total intensity of the mother is therefore a straight line whose slope is the fluorescence of a single molecule.

**Proof** $I_1 - I_2 = \alpha(2n_1 - N)$, and $\langle(2n_1 - N)^2\rangle = 4\operatorname{Var}(n_1) = 4\cdot N/4 = N$. Hence $\langle(I_1 - I_2)^2\rangle = \alpha^2N = \alpha(\alpha N) = \alpha(I_1 + I_2)$. $\square$

The method (Rosenfeld and colleagues, 2005) converts arbitrary fluorescence units into molecule counts without isolating single molecules, and it has been used to count transcription factors, mRNAs and organelles. It also tests the assumption: partitioning that is more even than binomial reveals active segregation, as for plasmids with partitioning systems or for the carboxysomes of cyanobacteria, which are positioned along the cell; partitioning that is less even reveals aggregation or attachment to one pole. The calibration matters for models: whether a regulator present at "low levels" means 5 or 500 molecules decides whether its noise matters ([7.6.32](/7.6.32)).

![Counting molecules by the noise of their partition at division. A: distribution of the fraction of molecules received by one daughter for 10, 100 and 1000 molecules (20,000 simulated divisions), with the normal approximations of standard deviation 1/(2√N): partitioning is noisy for tens of molecules and nearly exact for thousands. B: a simulated calibration experiment with 400 mother cells of 20–2000 molecules, each molecule giving 50 fluorescence units: the squared difference of the daughters' intensities scatters widely about a line of slope α (Proposition 20.1.1, logarithmic axes), and averaging recovers the brightness of a single molecule](./plots/partitioning.py)

## 20.2. Concentrations, Spacings and Encounters

### 20.2.1. Concentration as a Copy Number

In a test tube, concentration is the natural variable; in a cell it is a small integer divided by a small volume.

**Definition 20.2.1 (Copy Number)** The **copy number** of a molecular species is the number of its molecules in one cell (or one compartment). In a volume $V$, a concentration $c$ corresponds to $N = cVN_{\mathrm{A}}$ copies.

In *E. coli* one copy corresponds to $1/(N_{\mathrm{A}}\times1\,\mathrm{fL}) \approx 1.7\,\mathrm{nM}$ (Eq. (1.3) of [7.6.1](/7.6.1#sec-1.5.2)); "about $2\,\mathrm{nM}$ per molecule" is the rule of thumb, so $1\,\mu\mathrm{M}$ is about 600 copies and $1\,\mathrm{mM}$ about $6\times10^5$. The same concentration means $40$ times more copies in a yeast cell and $3000$ times more in a HeLa cell ([7.3.1](/7.3.1#sec-1.3.3)). A transcription factor with a dissociation constant of $1\,\mathrm{nM}$ for its site is, in *E. coli*, half-bound when there is about one free copy in the cell: this is why the in vitro language of dissociation constants and the in vivo language of copy numbers must be translated into each other through the cell volume, and why the thermodynamic models of gene regulation are written in copy numbers ([7.2.11](/7.2.11)).

### 20.2.2. Mean Spacing

**Formula 20.2.1 (Mean Spacing)** Molecules at number density $n = cN_{\mathrm{A}}$, imagined on a cubic lattice, are separated by

$$
d = n^{-1/3} \approx 1.18\,\mathrm{nm}\times\left(\frac{c}{1\,\mathrm{M}}\right)^{-1/3}. \tag{20.3}
$$

At $1\,\mathrm{nM}$, $d \approx 1.2\,\mu\mathrm{m}$, the size of the cell (one molecule per *E. coli*); at $1\,\mu\mathrm{M}$, $120\,\mathrm{nm}$; at the total protein concentration of the cytoplasm, about $5\,\mathrm{mM}$ ($3\times10^6$ proteins per $\mathrm{fL}$), $d \approx 7\,\mathrm{nm}$, barely more than the $5\,\mathrm{nm}$ diameter of a protein. A typical protein in the cytoplasm thus has its nearest neighbor within one or two nanometers of its surface.

### 20.2.3. Encounter Times

A third reading of concentration is the time it takes a molecule to find a partner. The naive estimate, the time to diffuse over the mean spacing, $d^2/6D$, is too short, because a random walker that has traveled a distance $d$ has not explored the volume $d^3$; it must find a target of radius $a$ in that volume. The correct rate is the diffusion-limited rate constant $k = 4\pi Da$ (Smoluchowski, [7.6.5](/7.6.5#sec-5.2)), and the mean time for a given molecule to meet one of the partners present at concentration $c$ is

$$
\tau_{\mathrm{enc}} = \frac{1}{4\pi Dac}. \tag{20.4}
$$
For a protein in cytoplasm ($D \approx 10\,\mu\mathrm{m^2\,s^{-1}}$, a tenth of its value in water because of crowding) and $a = 5\,\mathrm{nm}$, $k \approx 4\times10^8\,\mathrm{M^{-1}\,s^{-1}}$: at $1\,\mathrm{nM}$ (one copy per cell) an encounter takes about $3\,\mathrm{s}$, at $1\,\mu\mathrm{M}$ about $3\,\mathrm{ms}$. A transcription factor present at ten copies thus finds its target site within seconds in a bacterium only if it does not have to search the whole genome base by base; how facilitated diffusion along DNA solves this problem is the subject of [7.6.17](/7.6.17).

![Three readings of a concentration. Bottom axis: molar concentration; top axis: the same concentration as copies per *E. coli* cell. A: mean spacing d = c^(−1/3) (Formula 20.2.1) against the sizes of a protein and a ribosome; at the total protein concentration of the cytoplasm (about 5 mM) the spacing is about 7 nm. B: time for a molecule to meet a partner, from the diffusion-limited encounter rate 4πDa (Eq. (20.4), D = 10 µm²/s, a = 5 nm) and from the naive diffusion time over the mean spacing; one copy per cell means seconds, a micromolar partner milliseconds](./plots/concentration-scales.py)

## 20.3. Sizes from Cells to Organisms

### 20.3.1. Yeast and Human Cells

**Example 20.3.1 (Sizing up yeast)** A diploid budding yeast cell is roughly a sphere of diameter $5\,\mu\mathrm{m}$, $V \approx 65\,\mu\mathrm{m}^3$ (60 *E. coli*) and $A \approx 80\,\mu\mathrm{m}^2$; haploids are about $40\,\mu\mathrm{m}^3$. If the cytoplasm is as full as that of *E. coli*, it contains about $60\times3\times10^6 \approx 2\times10^8$ proteins. Its single plasma membrane holds $2\times0.5\times8\times10^7\,\mathrm{nm}^2/0.5\,\mathrm{nm}^2 \approx 2\times10^8$ lipids. The nucleus, $2\,\mu\mathrm{m}$ across ($4\,\mu\mathrm{m}^3$), holds the 12 Mb haploid genome wrapped into about $12\times10^6/200 = 6\times10^4$ nucleosomes (measured: about $8\times10^4$, at a repeat of 165 bp); at $1\,\mathrm{nm}^3$ per base pair the DNA fills only $3\times10^{-3}$ of the nuclear volume.

The protein estimate is too high by a factor of three to four: a unified analysis of many yeast proteome studies (Ho, Baryshnikova and Brown, 2018) gives about $4\times10^7$–$6\times10^7$ protein molecules per haploid cell, with a median copy number of a few thousand and a range from tens to about a million, because vacuole and cell wall occupy much of the volume. Estimates of this kind are valuable exactly when they fail: the factor of four points to what the simple picture leaves out. A human cell in culture (HeLa, about $3000\,\mu\mathrm{m}^3$) has $10^9$–$10^{10}$ proteins and a few million ribosomes ([7.2.1](/7.2.1#sec-1.5)).

### 20.3.2. Organelles

Organelles are measured with the same geometry. Mitochondria of yeast grown on glucose form a few tubes of radius $r \approx 100\,\mathrm{nm}$ and total length $12\,\mu\mathrm{m}$: a volume $\pi r^2\ell \approx 0.4\,\mu\mathrm{m}^3$, about 1 % of the cell, and an outer-membrane area $2\pi r\ell \approx 8\,\mu\mathrm{m}^2$, 10 % of the plasma membrane; on nonfermentable carbon sources the network grows severalfold ([7.3.12](/7.3.12)).

**Example 20.3.2 (The membrane area of the endoplasmic reticulum)** In a secretory cell such as a pancreatic acinar cell, the rough ER forms stacked sheets around the nucleus. Model them as concentric spherical cisternae spaced $d$ apart between the nuclear radius $R_{\mathrm{n}}$ and an outer radius $R_{\mathrm{out}}$. The volume they span is $\sum_iA_id = \frac{4\pi}{3}(R_{\mathrm{out}}^3 - R_{\mathrm{n}}^3)$, and each cisterna has two membranes, so the total ER membrane area is

$$
A_{\mathrm{ER}} = 2\sum_iA_i = \frac{8\pi}{3d}\left(R_{\mathrm{out}}^3 - R_{\mathrm{n}}^3\right).
$$
With $R_{\mathrm{n}} = 5\,\mu\mathrm{m}$, $R_{\mathrm{out}} = 10\,\mu\mathrm{m}$ and $d = 50\,\mathrm{nm}$, $A_{\mathrm{ER}} \approx 1.5\times10^5\,\mu\mathrm{m}^2$, fifteen times the plasma membrane ($\sim 10^4\,\mu\mathrm{m}^2$). Electron-microscopic stereology of liver cells gives the same order: the ER and the inner mitochondrial membrane together exceed the plasma membrane twenty- to fiftyfold ([7.3.7](/7.3.7)). The cell's chemistry happens mainly on internal surfaces.

### 20.3.3. Assemblies and Viruses

Macromolecular assemblies span $10$–$100\,\mathrm{nm}$: the ribosome ($2.5\,\mathrm{MDa}$, $20$–$25\,\mathrm{nm}$), the proteasome and chaperonins ($15$–$20\,\mathrm{nm}$), the nuclear pore complex (about $100\,\mathrm{nm}$ across, $50$–$100\,\mathrm{MDa}$ in vertebrates). Their structures are increasingly known at atomic resolution ([7.6.10](/7.6.10), [7.6.14](/7.6.14)), and their symmetric architectures, including the icosahedral capsids of viruses described by the triangulation number, are treated in [7.6.7](/7.6.7).

**Example 20.3.3 (Sizing up HIV)** The immature HIV-1 virion is a sphere of diameter about $130\,\mathrm{nm}$, whose outer $5\,\mathrm{nm}$ is the lipid envelope. Inside, the Gag polyproteins form a shell of radius about $60\,\mathrm{nm}$, each occupying a disc of radius about $2\,\mathrm{nm}$ on it:

$$
N_{\mathrm{Gag}} \approx \frac{4\pi(60\,\mathrm{nm})^2}{\pi(2\,\mathrm{nm})^2} \approx 3600, \qquad M \approx 3600\times55\,\mathrm{kDa} \approx 200\,\mathrm{MDa}.
$$
Cryo-electron tomography counts about 2500 Gag molecules, because the immature lattice is incomplete (it covers about two thirds of the sphere). The envelope holds about $2\times4\pi(65\,\mathrm{nm})^2/0.5\,\mathrm{nm}^2 \approx 2\times10^5$ lipids, close to the $3\times10^5$ measured by mass spectrometry, with a composition (rich in cholesterol and sphingomyelin) unlike that of the average host membrane. The dynamics of HIV infection was the worked model of [7.6.1](/7.6.1#sec-1.6.5).

### 20.3.4. Multicellular Structures

Cells cooperate in colonies, biofilms, aggregates and organisms, and the same estimates apply.

- The fruiting body of *Dictyostelium discoideum*. When starved, tens of thousands to millions of amoebae aggregate into a slug and then into a stalk carrying a ball of spores. A squashed ball about $200\,\mu\mathrm{m}$ across, treated as a hemisphere filled with spores of diameter $4\,\mu\mathrm{m}$, holds about $\frac{2}{3}\pi(100\,\mu\mathrm{m})^3/\frac{4}{3}\pi(2\,\mu\mathrm{m})^3 \approx 6\times10^4$ spores. A factor of two in the cell diameter changes the answer by a factor of eight: estimates of numbers from sizes amplify errors by the cube.
- Stripes in the *Drosophila* embryo. The embryo is a spherocylinder of radius $R \approx 100\,\mu\mathrm{m}$ and cylindrical length $L \approx 500\,\mu\mathrm{m}$, with about 6000 nuclei at its surface after 13 nuclear divisions. Their areal density is $\sigma = N/(4\pi R^2 + 2\pi RL) \approx 0.01\,\mu\mathrm{m}^{-2}$, and a stripe of gene expression $20\,\mu\mathrm{m}$ wide around the circumference contains $\sigma\cdot2\pi R\cdot20\,\mu\mathrm{m} \approx 125$ nuclei. A pair-rule stripe is a decision made by about a hundred nuclei, each reading a gradient whose relative precision must therefore be about 10 % ([7.5.11](/7.5.11), [7.6.35](/7.6.35)).
- *Caenorhabditis elegans*. The adult hermaphrodite is a cylinder about $1\,\mathrm{mm}$ long and $0.1\,\mathrm{mm}$ wide, $V \approx 8\times10^6\,\mu\mathrm{m}^3$, with 959 somatic nuclei (many cells are syncytial or very large): about $10^4\,\mu\mathrm{m}^3$ per nucleus, a characteristic eukaryotic cell volume of $10^3$–$10^4\,\mu\mathrm{m}^3$.
- The human body. A 70 kg adult contains about $3\times10^{13}$ human cells, about 85 % of them red blood cells by number, and about $4\times10^{13}$ bacteria, mostly in the colon (Sender, Fuchs and Milo, 2016). The often-quoted ratio of ten bacteria per human cell is an overestimate: the ratio is about one.

## 20.4. Stopwatches: The Hierarchy of Time Scales

### 20.4.1. How Biological Times Are Measured

Biological processes run from femtoseconds to billions of years ([7.6.1](/7.6.1#sec-1.3.2)). Four classes of experiment measure them on every scale:

| Strategy | Principle | Examples |
|---|---|---|
| Direct observation | follow an object over time | time-lapse microscopy of division, single-molecule trajectories of motors |
| Pulse labeling | mark a cohort and follow it | radioactive or isotope pulse–chase of proteins and mRNAs; the slow axonal transport of labeled proteins |
| Perturbation and relaxation | change a condition rapidly and watch the return to steady state | stopped flow, temperature jump, photoactivation, optogenetic switches |
| Fluctuation analysis | infer rates from spontaneous fluctuations at steady state | fluorescence correlation spectroscopy ([7.6.12](/7.6.12)), single-channel recordings, noise in gene expression ([7.6.32](/7.6.32)) |

The fourth strategy rests on the fact that, near equilibrium, spontaneous fluctuations decay with the same rates as small imposed perturbations (the fluctuation–dissipation theorem, [7.6.5](/7.6.5)).

### 20.4.2. The Evolutionary Stopwatch

The longest biological times are read from fossils and from sequences. The fossil record and isotopic dating fix a few anchor points: the first evidence of life about 3.5–3.8 billion years ago, eukaryotes by about 1.6–1.8 billion years ago, animals about 600 million years ago. Between anchors, the **molecular clock** converts the number of sequence differences between species into time, assuming a roughly constant rate of substitution calibrated by fossils. The clock is imperfect: rates differ between genes (constrained genes change slowly), lineages and generation times, and selection can accelerate or slow it, so divergence times are estimated with relaxed-clock models that allow the rate to vary ([7.10](/7.10)). The universal tree of ribosomal RNA sequences is the largest-scale application ([7.3.1](/7.3.1#sec-1.4.2)).

### 20.4.3. The Standard Stopwatch

**Definition 20.4.1 (Doubling Time)** The **doubling time** $\tau$ of a population of cells in steady exponential growth, $N(t) = N_0\mathrm{e}^{\lambda t}$, is the time in which the number of cells (or the total mass) doubles: $\tau = \ln 2/\lambda$, where $\lambda$ is the growth rate. For a population whose cells divide in synchrony, it equals the time between divisions of a single cell (the generation time).

The doubling time of *E. coli* is our standard stopwatch: about $20\,\mathrm{min}$ in rich medium at $37\,^\circ\mathrm{C}$, $40$–$50\,\mathrm{min}$ in glucose minimal medium, hours on poor carbon sources. We take $\tau = 3000\,\mathrm{s}$. Times vary with conditions far more than sizes: a tenfold change of doubling time changes the cell volume only two- to threefold. Exponential growth cannot continue: one cell doubling every 20 minutes would weigh as much as the Earth in two days. In a batch culture growth slows as nutrients are depleted, which the **logistic growth** equation $\mathrm{d}N/\mathrm{d}t = \lambda N(1 - N/K)$ describes phenomenologically, with carrying capacity $K$; a 5 mL culture reaches about $5\times10^9$ cells in a night.

**Example 20.4.1 (The material budget of a cell cycle)** To make a new cell in $\tau = 3000\,\mathrm{s}$, *E. coli* must, on average, take up and polymerize

| Material | Amount per cell | Rate |
|---|---|---|
| Carbon (as glucose, 6 C each) | $10^{10}$ atoms | $3\times10^6\,\mathrm{s^{-1}}$ ($5\times10^5$ glucose $\mathrm{s^{-1}}$) |
| DNA | $4.6\times10^6\,\mathrm{bp}$ | $1.5\times10^3\,\mathrm{bp\,s^{-1}}$ |
| Amino acids into protein | $2.4\times10^6\times300$ | $2.4\times10^5\,\mathrm{s^{-1}}$ |
| Phospholipids | $2.2\times10^7$ | $7\times10^3\,\mathrm{s^{-1}}$ |
| Water | $2.3\times10^{10}$ | $8\times10^6\,\mathrm{s^{-1}}$, about $1$ molecule $\mathrm{nm^{-2}\,s^{-1}}$ of membrane |

The glucose estimate counts only the carbon built into the cell; at least as much again is respired to make ATP. These are averages over a cycle; each rate must be delivered by molecular machines with finite speeds, which is the subject of the next section.

![The material budget of one *E. coli* cell cycle (τ = 3000 s). A: average rates needed to double the content of the cell (Example 20.4.1). B: the number of machines working at their measured speeds needed to sustain these rates (bars) against the number present (diamonds): two replication forks at 1000 bp/s copy the genome in time, about 600 RNA polymerases at 60 nt/s make the stable RNA (of the roughly 1000 engaged in transcription), and 16,000 ribosomes at 15 amino acids per second make the protein, close to the 19,000 counted](./plots/cell-cycle-budget.py)

## 20.5. Procedural Time

A process takes as long as its procedure: a polymer of $N$ units made by a machine adding units at rate $v$ takes $N/v$. Times of this kind, which PBoC calls procedural, change with temperature and nutrients because the rates of the underlying enzymatic steps do.

### 20.5.1. The Machines of the Central Dogma

The three polymerizations of the **central dogma** run at very different speeds.

**Example 20.5.1 (Timing the machines)** (a) *Replication.* The 4.6 Mb chromosome is copied by two replisomes moving in opposite directions from the **origin of replication**; at about $1000\,\mathrm{bp\,s^{-1}}$ each, replication takes $4.6\times10^6/2000 \approx 2300\,\mathrm{s} \approx 40\,\mathrm{min}$, the measured C period ([7.2.7](/7.2.7)). (b) *Transcription.* A typical mRNA of $1000\,\mathrm{nt}$ (a 300-residue protein) at $40$–$80\,\mathrm{nt\,s^{-1}}$ takes $15$–$25\,\mathrm{s}$. (c) *Translation.* The required $2.4\times10^5$ amino acids per second, divided among $2\times10^4$ ribosomes, give $12\,\mathrm{aa\,s^{-1}}$ per ribosome, close to the measured $12$–$20\,\mathrm{aa\,s^{-1}}$ (higher in fast growth); a 300-residue protein takes about $20\,\mathrm{s}$.

Translation is slower per monomer than transcription, but each mRNA is translated by many ribosomes at once, spaced about 100 nucleotides apart in a **polysome**, and in bacteria translation begins on the nascent mRNA while it is still being transcribed. The net rate of a process is the speed of one machine times the number of machines, and the second factor is under regulation: growing faster requires more ribosomes rather than faster ones ([7.6.39](/7.6.39)).

### 20.5.2. Lifetimes and Dilution

The steady-state amount of a molecule is set by the balance between its synthesis and its removal.

**Proposition 20.5.1 (Degradation and Dilution)** In a cell growing exponentially at rate $\lambda = \ln 2/\tau$, a molecule synthesized at rate $\beta$ per cell volume and degraded with rate constant $\gamma$ has concentration obeying $\mathrm{d}c/\mathrm{d}t = \beta - (\gamma + \lambda)c$, so that

$$
c^* = \frac{\beta}{\gamma + \lambda}, \qquad \text{response time } t_{1/2} = \frac{\ln 2}{\gamma + \lambda}. \tag{20.5}
$$

**Proof** With $c = n/V$ and $\mathrm{d}V/\mathrm{d}t = \lambda V$, $\mathrm{d}c/\mathrm{d}t = (\mathrm{d}n/\mathrm{d}t)/V - \lambda c$, and $\mathrm{d}n/\mathrm{d}t = \beta V - \gamma n$. The linear equation relaxes to $c^*$ with rate $\gamma + \lambda$. $\square$

Bacterial mRNAs are unstable: in *E. coli* their half-lives are mostly between 2 and 8 minutes, median about 5 minutes (Bernstein and colleagues, 2002), so that $\gamma \gg \lambda$ and mRNA levels follow transcription within minutes. Most bacterial proteins are stable on the scale of a cell cycle, $\gamma \ll \lambda$, so they are removed mainly by dilution and their levels respond with the doubling time; proteins that must change fast (regulators such as σ³² or LexA-controlled proteins) are actively degraded. In yeast, early measurements after blocking translation with cycloheximide suggested a median protein half-life of about 40 minutes, but labeling without inhibitors gave a median of several hours, so that in growing yeast, as in bacteria, dilution dominates for most proteins; in slowly dividing or nondividing mammalian cells, degradation sets the lifetimes, typically tens of hours. Eq. (20.5) is the reason a cell that wants a fast response uses unstable molecules, at the cost of continuous synthesis.

### 20.5.3. Clocks

Some procedures are repeated to make a clock. After fertilization, the *Xenopus laevis* egg ($1.2\,\mathrm{mm}$) divides without growing, the first cycle after about 90 minutes and the following eleven every 25–30 minutes at room temperature, until about 4000 cells form; the cycle is driven by the accumulation of cyclin to a threshold that activates the cyclin-dependent kinase Cdk1, which in turn activates the degradation of cyclin (half-life about 90 seconds in mitosis) and resets the clock ([7.3.20](/7.3.20)). The period is the sum of procedural times (synthesis to threshold, activation, degradation) and so varies with temperature. Circadian clocks must not: their period stays near 24 hours over a wide range of temperatures (temperature compensation, $Q_{10} \approx 1$). The smallest known circadian clock is that of the cyanobacterium *Synechococcus elongatus*: three proteins, KaiA, KaiB and KaiC, with ATP sustain a 24-hour cycle of KaiC phosphorylation in a test tube without transcription or degradation (Nakajima and colleagues, 2005), its slow, temperature-insensitive pace set by the ATPase of KaiC, which hydrolyzes only about 15 ATP per subunit per day. The dynamical theory of such oscillators, and the energetic cost of their precision, are taken up in [7.6.33](/7.6.33) and [7.6.38](/7.6.38).

## 20.6. Relative Time

Many processes care less about how long something takes than about what comes first: "socks before shoes". This relative time is enforced by dependencies between steps.

### 20.6.1. Checkpoints

In the eukaryotic **cell cycle** ([7.3.20](/7.3.20)), checkpoints make later events wait for earlier ones: mitosis waits for complete replication and repair of DNA, anaphase for the attachment of every kinetochore to the spindle. The order is fixed; the durations change from cell to cell and condition to condition. In the bacterium *Caulobacter crescentus*, whose cells can be synchronized, microarray measurements every 15 minutes over its 150-minute cycle found about one fifth of the genes expressed at a particular phase, in clusters that switch on in the order in which their products are needed: replication, chromosome segregation, flagellum and pili, division (Laub and colleagues, 2000).

### 20.6.2. Just-in-Time Assembly

The bacterial flagellum is built from the inside out: the basal body in the membrane, then the hook, then the filament, pushed through the hollow structure and added at its tip ([7.6.28](/7.6.28)). Measurements of promoter activity with fluorescent reporters in *E. coli* (Kalir and colleagues, 2001) showed that the flagellar operons are switched on in the same order as the structure is assembled, with delays of several minutes between successive operons. The mechanism is quantitative. A master regulator (FlhDC, then σ²⁸) accumulates, and each operon has a different threshold:

**Proposition 20.6.1 (Order from Thresholds)** If an activator accumulates as $X(t) = X_\infty(1 - \mathrm{e}^{-t/T})$ and gene $i$ switches on when $X$ crosses its activation threshold $K_i < X_\infty$, gene $i$ starts at

$$
t_i = -T\ln\left(1 - \frac{K_i}{X_\infty}\right), \tag{20.6}
$$
so that genes are activated in the order of their thresholds, and the delays between them are set by the time constant $T$ of the activator.

**Proof** Solve $X(t_i) = K_i$ for $t_i$; $t_i$ increases with $K_i$. $\square$

Thresholds spread evenly between $0.1X_\infty$ and $0.9X_\infty$ give delays that increase from about $0.1T$ to $0.5T$ per step; a time constant of tens of minutes, set by dilution of the stable activator (Proposition 20.5.1), yields the observed spacing. A single rising signal, read by promoters of different affinity, thus encodes a sequence, a principle also used in sporulation and in the temporal ordering of metabolic enzymes ([7.9](/7.9)).

### 20.6.3. Viral Life Cycles

A lytic phage infection is a strict sequence (adsorb, inject, transcribe early genes, replicate, transcribe late genes, assemble capsids, package DNA, lyse) completed in about 20–60 minutes, after which about 100 progeny emerge from each cell; the packaging step alone, a motor working against tens of piconewtons, takes a few minutes ([7.6.21](/7.6.21#sec-21.7.2)). HIV has a generation time of about one to two days in infected people, which, with the size of the infected population, makes its evolution of drug resistance fast ([7.6.1](/7.6.1#sec-1.6.5)).

### 20.6.4. Development

Development combines both kinds of time. In the early *Drosophila* embryo, nuclei divide synchronously every 8–10 minutes without cell membranes (a syncytium), because only DNA replication and mitosis are needed. With perfect synchrony,

$$
N(t) = 2^{t/\tau_{\mathrm{cc}}}, \tag{20.7}
$$
so after about 100 minutes ten divisions give about 1000 nuclei; the later cycles 10–13 lengthen, and after cycle 13 the roughly 6000 surface nuclei are cellularized and gastrulation begins ([7.5](/7.5)). The relative order of developmental stages is conserved between related species even when their absolute durations differ severalfold, which is why embryos are compared by stage rather than by hours.

## 20.7. Manipulated Time

Cells do not accept the time scales set by chemistry and diffusion; they speed some processes up by many orders of magnitude and slow others to a halt.

### 20.7.1. Enzymes

A reaction with an activation barrier $\Delta G^\ddagger$ proceeds at a rate proportional to $\mathrm{e}^{-\Delta G^\ddagger/k_{\mathrm{B}}T}$ ([7.6.3](/7.6.3)); an enzyme lowers the barrier, usually by binding the transition state more tightly than the substrate, without changing the equilibrium. The enhancements are enormous (Radzicka and Wolfenden, 1995): the decarboxylation of orotidine monophosphate has a half-life of 78 million years in water and of 20 milliseconds on its enzyme, a factor of $10^{17}$, corresponding to a barrier reduced by about $40\,k_{\mathrm{B}}T$; triose phosphate isomerase accelerates its reaction $10^9$-fold, to the limit set by diffusion of the substrate to the active site. **Enzyme catalysis** turns chemistry that would take geological time into chemistry on the millisecond scale of cellular life ([7.1.8](/7.1.8)).

### 20.7.2. Beating Diffusion

Diffusion is fast over short distances and slow over long ones, because the time grows as the square of the distance ([7.6.5](/7.6.5)). A protein with $D \approx 100\,\mu\mathrm{m^2\,s^{-1}}$ in water crosses *E. coli* ($1\,\mu\mathrm{m}$) in about $10\,\mathrm{ms}$; acetylcholine ($D \approx 400\,\mu\mathrm{m^2\,s^{-1}}$) crosses a $20\,\mathrm{nm}$ synaptic cleft in about a microsecond. But the same protein would need $x^2/2D \approx (0.1\,\mathrm{m})^2/(2\times10^{-10}\,\mathrm{m^2\,s^{-1}}) = 5\times10^7\,\mathrm{s}$, more than a year, to diffuse along a $10\,\mathrm{cm}$ squid giant axon, and centuries along the metre-long axons of human motor neurons. **Kinesin**, walking along microtubules at about $1\,\mu\mathrm{m\,s^{-1}}$, carries vesicles the same $10\,\mathrm{cm}$ in a day. The crossover between the two modes occurs at $x^* = 2D/v$: about $20\,\mu\mathrm{m}$ for a protein in cytoplasm ($D \approx 10\,\mu\mathrm{m^2\,s^{-1}}$) against a motor at $1\,\mu\mathrm{m\,s^{-1}}$, the size of a eukaryotic cell. This is why bacteria rely on diffusion and large eukaryotic cells on motors. Classical pulse-labeling experiments in neurons distinguished fast **axonal transport** of vesicles (about $200$–$400\,\mathrm{mm}$ per day, the speed of kinesin) from slow transport of cytoskeletal and cytosolic proteins ($0.2$–$8\,\mathrm{mm}$ per day), now understood as rare, fast motor-driven movements separated by long pauses: the average speed is that of the motor times its duty ratio ([7.6.27](/7.6.27)).

![How cells beat the intrinsic time scales. A: time to move a distance x by diffusion (t = x²/2D) for a small molecule, a protein in cytoplasm and a vesicle, and by directed transport at the speeds of fast and slow axonal transport, with characteristic distances marked; diffusion wins below the crossover x* = 2D/v (about 20 µm for a protein against a motor at 1 µm/s) and becomes hopeless over the length of an axon. B: half-lives of six reactions in water without enzyme (open) and on their enzymes (filled), with the rate enhancements, from 10⁶ (chorismate mutase) to 10¹⁷ (OMP decarboxylase)](./plots/manipulated-time.py)

### 20.7.3. Channels and Pumps

Membranes are nearly impermeable to ions, and proteins open controlled paths through them.

**Example 20.7.1 (How many ions through one channel?)** Model an open channel as a water-filled pore of diameter $0.5\,\mathrm{nm}$ (cross-section $A \approx 0.2\,\mathrm{nm}^2$) and length $\ell = 5\,\mathrm{nm}$, through which ions diffuse with $D \approx 2\times10^3\,\mu\mathrm{m^2\,s^{-1}} = 2\times10^9\,\mathrm{nm^2\,s^{-1}}$ down a concentration difference of $100\,\mathrm{mM} = 0.06\,\mathrm{nm^{-3}}$. By Fick's law the flux is

$$
J \approx D\frac{\Delta c}{\ell} = 2\times10^9\times\frac{0.06}{5}\,\mathrm{nm^{-2}\,s^{-1}} \approx 2.4\times10^7\,\mathrm{nm^{-2}\,s^{-1}}, \qquad JA \approx 5\times10^6\,\mathrm{ions\,s^{-1}}.
$$
Measured single-channel currents of a few picoamperes correspond to $10^6$–$10^8$ ions per second (1 pA is $6\times10^6$ monovalent ions per second), so the free-diffusion estimate is of the right order; the membrane potential adds a drift term ([7.6.30](/7.6.30)). Pumps, which must couple each transport event to ATP hydrolysis, are slower by four orders of magnitude, about 100 ions per second for the $\ce{Na+}$/$\ce{K+}$-ATPase.

### 20.7.4. Beating the Replication Limit

Replication of the *E. coli* chromosome takes 40 minutes (Example 20.5.1), yet the bacterium divides every 20 minutes in rich medium. It does so by starting new rounds of replication before the previous ones have finished: a fast-growing cell carries chromosomes with replication forks of two or three generations, so that each newborn cell inherits a chromosome already partly copied for its daughters and granddaughters (multifork replication, whose gene-dosage consequences are quantified by the Cooper–Helmstetter model in [7.2.7](/7.2.7)). Eukaryotes face a different limit: their forks are slower (about $1$–$3\,\mathrm{kb\,min^{-1}}$, $20$–$50\,\mathrm{bp\,s^{-1}}$) and their genomes larger. With fork speed $v$ and S phase of duration $T$, each origin can serve at most $2vT$ of DNA, so a genome of size $G$ needs at least $G/(2vT)$ origins. The *Xenopus* embryo replicates its $3\times10^9\,\mathrm{bp}$ genome in an S phase of about 20 minutes: with $v \approx 20\,\mathrm{bp\,s^{-1}}$ this requires at least $3\times10^9/(2\times20\times1200) \approx 6\times10^4$ active origins, and in fact origins fire every $5$–$15\,\mathrm{kb}$, more than $2\times10^5$ of them. In somatic cells, with fewer origins and S phases of 6–8 hours, the same genome takes much longer.

### 20.7.5. Suspended Animation

Organisms also stretch time. The *Xenopus* oocyte grows for months in the ovary and then, after fertilization, divides into a swimming tadpole of the same mass in about two days, separating growth from division. Bacterial endospores, fungal spores, plant seeds, the dauer larvae of nematodes and the desiccated tun state of tardigrades suspend metabolism for months to centuries; *Bacillus* spores remain viable for decades to centuries, and a few reports claim far longer survival. Dormancy is time manipulated to wait for better conditions.

## 20.8. Model Organisms from a Physical Point of View

The numbers of this chapter were measured on a handful of **model organisms** ([7.3.1](/7.3.1#sec-1.7.1)). The physicist's reasons for choosing them differ somewhat from the biologist's: each made a class of phenomena accessible to quantitative experiments that could be compared with simple models.

| Model | What made it quantitative | Physics it supports in this course |
|---|---|---|
| Hemoglobin | abundant, crystallizable, oxygen binding measurable to high precision | cooperativity, the MWC model ([7.6.4](/7.6.4)); first protein structures with myoglobin ([7.6.10](/7.6.10)); the first molecular disease, sickle-cell anemia |
| Bacteriophages (T4, λ, φ29, T7) | simple life cycles, huge numbers, genetics in a day | the gene as DNA (Hershey–Chase), the λ switch ([7.2.11](/7.2.11)); DNA packaging and single-molecule motors ([7.6.21](/7.6.21), [7.6.28](/7.6.28)) |
| *E. coli* | defined media, fast growth, precise genetics | the lac operon as the "hydrogen atom" of gene regulation ([7.2.11](/7.2.11)); chemotaxis ([7.6.35](/7.6.35)); growth laws ([7.6.39](/7.6.39)) |
| *Saccharomyces cerevisiae* | eukaryotic genetics with complete deletion and fusion libraries | cell-cycle control, polarity (Cdc42), membrane traffic; the first eukaryotic proteome census |
| *Drosophila melanogaster* | genetics of development, optically accessible embryo | morphogen gradients and their precision ([7.5.11](/7.5.11)) |
| *C. elegans*, zebrafish, mouse | invariant lineage; transparent embryos; mammalian genetics | development and physiology of whole animals |
| Exotica | an exaggerated feature or a unique molecule | the squid giant axon for the action potential ([7.6.30](/7.6.30)); green fluorescent protein from *Aequorea victoria*; the thermostable DNA polymerase of *Thermus aquaticus* for **PCR**; neurotoxins as affinity labels for channels and receptors |

![Model organisms by the numbers: haploid genome size against generation time, both on logarithmic axes. From phage λ (48.5 kb, about 50 min from infection to lysis) and *E. coli* (4.6 Mb, 20–50 min) to humans (3.1 Gb, about 25 years), genomes span five orders of magnitude and generation times seven; generation time is set by body plan and life history rather than by the time to copy the genome](./plots/model-organisms.py)

## Summary

| Quantity | *E. coli* (glucose minimal medium) | Reasoning |
|---|---|---|
| Size | $1\,\mathrm{fL}$, $6\,\mu\mathrm{m}^2$, $1\,\mathrm{pg}$ (30 % dry, half protein) | Eq. (20.1) |
| Census | $3\times10^6$ proteins, $2\times10^4$ ribosomes, $2\times10^7$ lipids, $2\times10^{10}$ water, $10^{10}$ C atoms | Example 20.1.1, Example 1.5.1 |
| Counting | binomial partition noise: $\langle(I_1 - I_2)^2\rangle = \alpha(I_1 + I_2)$ | Proposition 20.1.1 |
| Concentration | 1 copy $\approx 2\,\mathrm{nM}$; spacing $d = c^{-1/3}$, $7\,\mathrm{nm}$ for all protein; encounter $1/(4\pi Dac)$, seconds at 1 nM | Definition 20.2.1, Formula 20.2.1, Eq. (20.4) |
| Time | $\tau \approx 3000\,\mathrm{s}$; budget $1.5\times10^3\,\mathrm{bp}$, $2.4\times10^5$ aa, $7\times10^3$ lipids per second | Definition 20.4.1, Example 20.4.1 |
| Machines | replisome $1000\,\mathrm{bp\,s^{-1}}$, RNAP $40$–$80\,\mathrm{nt\,s^{-1}}$, ribosome $12$–$20\,\mathrm{aa\,s^{-1}}$ | Example 20.5.1 |
| Lifetimes | mRNA $\sim 5\,\mathrm{min}$; most proteins removed by dilution, $t_{1/2} = \ln2/(\gamma + \lambda)$ | Proposition 20.5.1 |

Three views of biological time: procedural time is the duration of a procedure ($N/v$, clocks built from procedures, temperature-compensated circadian clocks such as KaiABC); relative time is the order of events (checkpoints, threshold-ordered gene expression, Proposition 20.6.1, viral life cycles, development by stage); manipulated time is what cells do to escape intrinsic limits (enzymes up to $10^{17}$, motors beyond the crossover $2D/v$, channels at $10^6$–$10^8$ ions per second, multifork replication and many origins, dormancy). Estimates amplify errors (a factor two in a radius is eight in a count), and their failures, such as the yeast proteome estimate, are informative.

## Questions

1. Model *E. coli* as a cylinder of diameter $1\,\mu\mathrm{m}$ with hemispherical caps and total length $2\,\mu\mathrm{m}$. Compute its volume and surface area and compare with Eq. (20.1).

   **Answer** Cylinder length $\ell = 1\,\mu\mathrm{m}$, radius $r = 0.5\,\mu\mathrm{m}$. $V = \pi r^2\ell + \frac43\pi r^3 = 0.785 + 0.524 = 1.31\,\mu\mathrm{m}^3$; $A = 2\pi r\ell + 4\pi r^2 = 3.14 + 3.14 = 6.3\,\mu\mathrm{m}^2$. With the more typical width of $0.8\,\mu\mathrm{m}$ and length $2\,\mu\mathrm{m}$, $V = 0.88\,\mu\mathrm{m}^3$ and $A = 5.0\,\mu\mathrm{m}^2$. Both are consistent with $1\,\mathrm{fL}$ and $6\,\mu\mathrm{m}^2$ at the precision of a Fermi estimate.

2. Estimate the fraction of the *E. coli* cytoplasm occupied by proteins and ribosomes. Use a protein of $30\,\mathrm{kDa}$ with partial specific volume $0.73\,\mathrm{mL\,g^{-1}}$.

   **Answer** Protein mass $0.15\,\mathrm{pg}$ occupies $0.15\times10^{-12}\,\mathrm{g}\times0.73\,\mathrm{cm^3\,g^{-1}} = 1.1\times10^{-13}\,\mathrm{cm}^3 = 0.11\,\mu\mathrm{m}^3$ (this includes ribosomal protein). rRNA ($2\times10^4\times1.7\,\mathrm{MDa} = 5.6\times10^{-14}\,\mathrm{g}$ at about $0.55\,\mathrm{mL\,g^{-1}}$) adds $0.03\,\mu\mathrm{m}^3$. Dry macromolecules thus fill about 15 % of the volume; with hydration water (about $0.3\,\mathrm{g}$ per gram) and the excluded volume of their shapes the effective occupied fraction is 20–30 %, the regime of macromolecular crowding.

3. A transcription factor in *E. coli* has 10 copies per cell and binds its operator with $K_{\mathrm{d}} = 0.1\,\mathrm{nM}$ in vitro. Ignoring nonspecific binding, what is the probability that the operator is occupied? Why is ignoring nonspecific DNA wrong?

   **Answer** Ten copies in $1\,\mathrm{fL}$ is about $17\,\mathrm{nM}$; the occupancy is $c/(c + K_{\mathrm{d}}) = 17/17.1 \approx 0.99$. But most of the protein is bound to the $4.6\times10^6$ nonspecific sites of the genome, which reduces the free concentration and makes the relevant comparison a competition between one specific and millions of weak sites, as in the thermodynamic model of [7.2.11](/7.2.11); the occupancy then depends on the difference of specific and nonspecific binding energies rather than on the in vitro $K_{\mathrm{d}}$.

4. Prove Proposition 20.1.1 for a general partition probability $p \ne 1/2$ and show how a bias would appear in the data.

   **Answer** $I_1 - I_2 = \alpha(2n_1 - N)$, with $\langle 2n_1 - N\rangle = N(2p - 1)$ and $\operatorname{Var}(2n_1 - N) = 4Np(1 - p)$. Hence $\langle(I_1 - I_2)^2\rangle = \alpha^2[4Np(1-p) + N^2(2p-1)^2] = 4p(1-p)\,\alpha I_{\mathrm{tot}} + (2p-1)^2I_{\mathrm{tot}}^2$. A bias adds a quadratic term, so the plot curves upward at large intensities; the linear coefficient is reduced by $4p(1-p)$. Unequal daughter sizes produce exactly such a bias, which is why the analysis is restricted to divisions with nearly equal daughters or corrected for their size ratio.

5. Using Eq. (20.4), estimate how long it takes a single copy of a protein in *E. coli* to meet a single copy of its partner. How does this compare with the cell cycle? What does it imply for signaling with one or two molecules?

   **Answer** Each is at $1.7\,\mathrm{nM}$; $k = 4\pi Da \approx 3.8\times10^8\,\mathrm{M^{-1}\,s^{-1}}$ (with $a = 5\,\mathrm{nm}$ and $D = 10\,\mu\mathrm{m^2\,s^{-1}}$, the sum of the two diffusion coefficients would double it), so $\tau = 1/(kc) \approx 1.5\,\mathrm{s}$. This is short compared with the cell cycle (3000 s), so even single-copy partners meet hundreds of times per generation, but the time of each encounter is exponentially distributed: responses that depend on one or two molecules are noisy in timing, a theme of [7.6.32](/7.6.32) and [7.6.35](/7.6.35).

6. *E. coli* doubles in 20 minutes although its replication takes 40 minutes and division follows termination by about 20 minutes (the D period). How many replication forks are active in a newborn cell? (Hint: initiation must occur $C + D = 60$ minutes before the division it is for.)

   **Answer** Initiation for a given division occurs $C + D = 60\,\mathrm{min} = 3\tau$ before it. For a cell born at $t = 0$ and dividing at $\tau$, its own division was initiated at $-2\tau$ (in its grandmother), the division of its daughters at $-\tau$ and that of its granddaughters at $0$, at its birth. The round started at $-2\tau$ terminates at $C$ later, at $t = 0$: the newborn holds two complete sister chromosomes. Each carries the round started at $-\tau$, half finished (2 forks per chromosome, 4 in all), and at birth the 4 origins fire again (8 new forks). Just after birth there are therefore 2 termini, 8 origins and 12 forks; averaged over the cycle the origin-to-terminus ratio is $2^{C/\tau} = 4$, as measured.

7. A gene encoding a stable protein ($\gamma \approx 0$) is switched on in cells doubling every 50 minutes. How long until the protein reaches half its final concentration? How would you make the response five times faster without changing the final level?

   **Answer** By Proposition 20.5.1, $t_{1/2} = \ln 2/\lambda = \tau = 50\,\mathrm{min}$. To respond five times faster, add active degradation with $\gamma = 4\lambda$, so that $\gamma + \lambda = 5\lambda$ ($t_{1/2} = 10\,\mathrm{min}$), and increase the synthesis rate $\beta$ fivefold to keep $c^* = \beta/(\gamma + \lambda)$. Speed costs synthesis: four of every five proteins made are destroyed.

8. In Proposition 20.6.1, show that with thresholds $K_i = iX_\infty/(n + 1)$ ($i = 1, \dots, n$) the delays between successive genes increase along the sequence, and compute the times for $n = 4$ in units of $T$.

   **Answer** $t_i = -T\ln(1 - i/(n+1))$. For $n = 4$: $t_1 = 0.22T$, $t_2 = 0.51T$, $t_3 = 0.92T$, $t_4 = 1.61T$; delays $0.29T$, $0.41T$, $0.69T$, increasing because the activator approaches its plateau ever more slowly. Evenly spaced delays require thresholds that crowd towards $X_\infty$, or an activator that accumulates linearly, as a stable protein does at the start of its synthesis.

9. Estimate the diffusion time of a mitochondrion-sized vesicle ($D \approx 0.01\,\mu\mathrm{m^2\,s^{-1}}$ in cytoplasm) along a $1\,\mathrm{m}$ human motor axon, and the transport time by kinesin at $1\,\mu\mathrm{m\,s^{-1}}$. What happens to neurons when axonal transport fails?

   **Answer** Diffusion: $x^2/2D = 10^{12}\,\mu\mathrm{m}^2/(0.02\,\mu\mathrm{m^2\,s^{-1}}) = 5\times10^{13}\,\mathrm{s}$, more than a million years. Kinesin: $10^6\,\mathrm{s} \approx 12$ days. Without motors the distal axon and synapses cannot be supplied with organelles and membrane proteins; defects in kinesins, dynein and their adaptors cause hereditary neuropathies and motor neuron diseases that affect first the longest axons, consistent with transport time growing with length.

10. (Design) Propose an experiment to test whether a bacterial organelle (for example, a storage granule) is partitioned randomly at division, and the analysis that would distinguish random, even and one-sided partitioning.

    **Answer** Label the granules fluorescently, follow lineages by time-lapse microscopy, and count granules (or intensity) in the mother just before and in both daughters just after division, for hundreds of divisions. Compare the variance of $n_1 - n_2$ at given $N$ with the binomial prediction $N$ (Proposition 20.1.1 with $\alpha = 1$): random partitioning gives $\langle(n_1 - n_2)^2\rangle = N$; active, even segregation gives much less (near 0 or 1 for odd $N$); attachment to the old pole or aggregation gives more, up to $N^2$ when all go to one side. Controls: free fluorescent protein in the same cells (binomial by construction), correction for unequal daughter sizes, and a mutant lacking a candidate positioning system.
