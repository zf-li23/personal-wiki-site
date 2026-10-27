---
title: "Dissecting Cells: Culture, Fractionation and Perturbation"
description: "The experimental toolkit of cell biology beyond the light microscope: electron microscopy (TEM, SEM, sample preparation, negative staining, freeze-fracture, immunogold, cryo-electron tomography); cell culture, cell lines, organoids and hybridomas with HAT selection; cell fractionation by differential, velocity and isopycnic centrifugation with the pelleting time t = ln(r2/r1)/(omega^2 s); cell-free systems; radioactive tracers and the Jamieson–Palade pulse–chase as a compartment model; flow cytometry and FACS; protein–protein interaction methods with an SPR binding model; and perturbation of gene function by overexpression, RNAi, knockout, Cre–loxP and CRISPR."
---

Cell biology has a characteristic method in three steps: see a structure or a process, isolate the components that carry it out, and perturb them to find out which are necessary and how they work. The light microscope of [7.3.2](/7.3.2) covers most of the first step in living cells. This chapter collects the other methods on which the rest of the course relies: the electron microscope, which shows the fine structure of fixed cells and, in its cryogenic forms, the molecular architecture of cells close to their native state (3.1); cell culture, which provides uniform populations of cells to study (3.2); the fractionation of cells into organelles and the reconstitution of cellular processes in cell-free systems (3.3); radioactive tracers and pulse–chase experiments, which follow molecules through the cell in time (3.4); flow cytometry, which measures and sorts single cells by the thousands per second (3.5); methods for detecting interactions between proteins (3.6); and the genetic perturbation of cells and organisms (3.7). Many of the underlying techniques have been treated in earlier courses: protein purification, electrophoresis and mass spectrometry in [7.1.4](/7.1.4), chromatography and electrophoresis in [6.4.13](/6.4.13)–[6.4.14](/6.4.14), cloning, sequencing and genome editing in [7.2.5](/7.2.5), [7.2.6](/7.2.6) and [7.2.24](/7.2.24). They are linked rather than repeated here; the emphasis is on how each method is used to answer a question about cells.

## 3.1. Electron Microscopy

### 3.1.1. Why Electrons

The resolution of a microscope is limited by the wavelength of its radiation (Formula 2.1.1). Electrons accelerated through a potential difference $U$ have the **de Broglie wavelength** $\lambda = h/\sqrt{2m_{\mathrm{e}}eU(1 + eU/2m_{\mathrm{e}}c^2)}$, about $3.7\,\mathrm{pm}$ at $100\,\mathrm{kV}$, five orders of magnitude shorter than visible light. Electron lenses are magnetic and have large aberrations, so they are used at small apertures, but the instrumental resolution of a modern transmission microscope is still better than $0.1\,\mathrm{nm}$. For biological specimens the practical limit is set by the specimen: by the thickness of sections, by the size of the stain grains, and above all by radiation damage, since the electron dose that destroys an organic molecule is reached long before enough electrons have been collected to image it with high contrast. In stained sections the resolution is about $2\,\mathrm{nm}$; for purified macromolecules, averaging thousands of images of identical particles in cryo-electron microscopy reaches near-atomic resolution ([7.1.6](/7.1.6)). Because electrons are scattered by air, the column is kept at high vacuum, and specimens must be either dried and fixed or frozen.

**Definition 3.1.1** The microscope in which a beam of electrons transmitted through a thin specimen is focused by magnetic lenses into an image, the contrast arising from the scattering of electrons by atoms of the specimen (or by heavy-metal stains bound to it), is called the **transmission electron microscope** (TEM).

### 3.1.2. Preparing Specimens

Conventional preparation for TEM fixes, embeds, cuts and stains the specimen.

| Step | Typical reagents | Purpose |
|---|---|---|
| Fixation | Glutaraldehyde (cross-links proteins through amino groups), then osmium tetroxide (reacts with unsaturated lipids) | Immobilize structures; osmium also adds contrast to membranes |
| Dehydration and embedding | Graded ethanol or acetone, epoxy resin | Replace water, which would evaporate in the vacuum, with a hard plastic |
| Sectioning | Ultramicrotome with a diamond knife | Sections $50$–$100\,\mathrm{nm}$ thick, thin enough for electrons to pass |
| Staining | Uranyl acetate and lead citrate | Heavy atoms scatter electrons strongly and outline membranes, ribosomes and chromatin |

Chemical fixation is slow (seconds to minutes) compared with many cellular processes, and dehydration extracts lipids and shrinks structures. Rapid freezing avoids these artifacts: specimens frozen under high pressure or plunged into liquid ethane cool so fast that water solidifies as amorphous (vitreous) ice without crystals, and the cell is immobilized within milliseconds. The frozen specimen can then be fixed and embedded at low temperature (freeze substitution) or imaged directly in the frozen state (3.1.5).

### 3.1.3. Imaging Surfaces and Isolated Structures

Several methods produce contrast without sectioning.

**Definition 3.1.2** The method of embedding isolated particles (viruses, filaments, protein complexes) adsorbed on a carbon film in a thin layer of a heavy-metal salt such as uranyl acetate, so that they appear light against a dark background of stain that fills the spaces around and within them, is called **negative staining**.

In metal shadowing, a thin film of platinum is evaporated onto a dried specimen at a low angle, so that raised structures cast "shadows" and the surface relief is seen.

**Definition 3.1.3** The method in which a rapidly frozen specimen is fractured with a cold knife, so that the fracture plane tends to run through the hydrophobic interior of membranes and split them into their two leaflets, and the exposed surface is replicated by evaporating platinum and carbon onto it, is called **freeze-fracture electron microscopy**; when ice is first allowed to sublime from the fractured surface to expose true membrane surfaces, it is called freeze-etching.

The two faces produced by splitting a membrane are named after the compartment that faces them: the protoplasmic face (P face) is the inner face of the cytoplasmic leaflet, seen from the middle of the bilayer, and the exoplasmic face (E face) is the inner face of the leaflet facing the exterior or the lumen. The fracture faces of most membranes are studded with intramembrane particles $5$–$10\,\mathrm{nm}$ across, more numerous on the P face; they are integral membrane proteins and were key evidence for the fluid mosaic model ([7.3.4](/7.3.4)). Deep-etched replicas of quick-frozen cells (John Heuser) show the cytoskeleton, clathrin coats and synaptic vesicle fusion in three dimensions.

**Definition 3.1.4** The microscope that scans a finely focused electron beam over the surface of a specimen and forms an image from the secondary electrons emitted at each point, which depend on the local topography, is called the **scanning electron microscope** (SEM).

Specimens for SEM are fixed, dried (by critical-point drying, which avoids the surface tension of an evaporating liquid) and coated with a thin film of metal. The SEM resolves $1$–$10\,\mathrm{nm}$ and has a great depth of field, so that it gives vivid images of cell surfaces: microvilli of lymphocytes and macrophages, the stereocilia of hair cells in the inner ear, the cytoplasmic face of nuclear pores. In volume electron microscopy, a block of embedded tissue is imaged by SEM, its surface removed by an ultramicrotome inside the microscope or by a focused ion beam, and imaged again; thousands of such cycles reconstruct cells and whole circuits of neurons in three dimensions with nanometre resolution (connectomics).

Scanning probe microscopes use no lenses. The **scanning tunneling microscope** ([5.5](/5.5)) images conducting surfaces with atomic resolution and is little used for cells. The atomic force microscope scans a sharp tip on a flexible cantilever over a surface and records the deflection caused by interatomic forces; it images membranes, protein arrays and living cells in aqueous solution with nanometre resolution and, used as a force probe, measures the strength of single bonds between a ligand and its receptor.

### 3.1.4. Locating Molecules in the Electron Microscope

Specific molecules can be located in thin sections in two ways. In enzyme cytochemistry the activity of an enzyme deposits an electron-dense product where the enzyme is: in the Golgi apparatus, osmium impregnation stains the *cis* cisternae, NADPase activity the medial cisternae, nucleoside diphosphatase the *trans* cisternae and acid phosphatase the *trans* Golgi network, a direct demonstration that the stack is biochemically polarized ([7.3.9](/7.3.9)).

**Definition 3.1.5** The localization of a molecule in electron micrographs with antibodies (usually a primary antibody and a secondary antibody or protein A) coupled to colloidal gold particles of defined diameter ($5$–$20\,\mathrm{nm}$), which are electron dense and appear as black dots, is called **immunogold labeling**.

Gold particles of two sizes locate two proteins in the same section. Antibodies penetrate only the surface of resin sections, so the method is done on thin sections of mildly fixed, frozen tissue (the Tokuyasu method) or of specimens embedded in hydrophilic resins. In correlative light and electron microscopy (CLEM), a fluorescent signal seen in the light microscope, often a rare event in a living cell, is found again in the electron micrograph of the same cell.

### 3.1.5. Cryo-Electron Tomography

**Cryo-electron microscopy** ([7.1.6](/7.1.6)) images specimens in vitreous ice, unstained and close to their native state. For purified complexes, single-particle analysis averages images of many identical particles in random orientations. Cells are not identical, and require tomography.

**Definition 3.1.6** The method in which a vitrified specimen is imaged in the electron microscope at a series of tilt angles (typically from $-60^\circ$ to $+60^\circ$ in steps of $2$–$3^\circ$) and the images are combined computationally into a three-dimensional reconstruction is called **cryo-electron tomography** (cryo-ET).

Electrons penetrate ice only a few hundred nanometres thick, so thicker cells are first thinned with a focused ion beam into lamellae $100$–$200\,\mathrm{nm}$ thick. Averaging repeated objects in the tomogram (subtomogram averaging) yields their structure in situ at resolutions approaching those of purified complexes; ribosomes on the ER, the nuclear pore complex in its native membrane, the arrangement of ATP synthase dimers along the cristae ([7.3.12](/7.3.12)) and the attachment of microtubules to kinetochores have been seen in this way. Cryo-ET bridges structural biology and cell biology: it shows molecules in their cellular context.

| Method | Specimen | Resolution | Shows |
|---|---|---|---|
| TEM of stained sections | Fixed, embedded, sectioned | About $2\,\mathrm{nm}$ | Ultrastructure of organelles |
| Negative staining, shadowing | Isolated particles | $1$–$2\,\mathrm{nm}$ | Shape of filaments, viruses, complexes |
| Freeze-fracture, deep-etch | Rapidly frozen, replicated | $2$–$5\,\mathrm{nm}$ | Interior of membranes, cytoskeletal networks |
| Immunogold | Sections, Tokuyasu cryosections | $10$–$20\,\mathrm{nm}$ (label size) | Location of a specific protein |
| SEM, volume EM | Dried and coated; or resin blocks | $1$–$10\,\mathrm{nm}$ | Surfaces; 3D reconstruction of tissue |
| Cryo-ET | Vitrified cells or lamellae | $2$–$4\,\mathrm{nm}$ (better with averaging) | Molecular architecture in situ |

## 3.2. Cell Culture

### 3.2.1. Primary Cultures and Cell Lines

The cells of a tissue differ in type, state and position, which makes it hard to attribute a measurement to any one of them. Cultures provide large, homogeneous populations under controlled conditions. Tissues are dissociated with proteases such as trypsin and with chelators of $\ce{Ca^2+}$ (EDTA), which loosen the junctions between cells ([7.3.23](/7.3.23)).

**Definition 3.2.1** A culture of cells taken directly from an organism is called a **primary culture**. A population of cells that can be propagated in culture indefinitely, having escaped the normal limit on the number of divisions, is called a **cell line**.

Most vertebrate cells cannot grow suspended in medium: they must attach to a surface (anchorage dependence), they stop dividing when they cover the dish in a monolayer (contact inhibition, [7.3.22](/7.3.22)), and normal human fibroblasts divide only $40$–$60$ times before they stop permanently (the Hayflick limit, replicative senescence, [7.3.25](/7.3.25)), largely because their telomeres shorten. Cells become immortal when they express **telomerase** and lose the checkpoints that respond to short telomeres, which happens spontaneously in rodent cells, after expression of viral oncogenes (SV40 large T antigen, papillomavirus E6 and E7) or of the catalytic subunit of telomerase, and in cancer cells. Transformation by an oncogene goes further: NIH 3T3 mouse fibroblasts transformed by the *v-src* oncogene lose contact inhibition and anchorage dependence and pile up into dense foci ([7.3.26](/7.3.26)).

The first human cell line, HeLa, was derived in 1951 at the Johns Hopkins Hospital by George Gey from a cervical carcinoma of Henrietta Lacks, who was not asked for consent. HeLa cells carry integrated human papillomavirus 18 DNA and a highly abnormal karyotype, and they grow so vigorously that they contaminated and replaced many other cell lines in the decades that followed; authenticating cell lines by their pattern of short tandem repeats (**microsatellite** genotyping) and testing for contaminating mycoplasmas are now routine. The genome of HeLa cells was published in 2013, after which the US National Institutes of Health agreed with the Lacks family on the terms of access to the data.

### 3.2.2. Media and Three-Dimensional Culture

Harry Eagle defined in 1955 the nutrients that cultured mammalian cells need: glucose, amino acids (including those essential to the whole organism), vitamins, salts and a bicarbonate buffer equilibrated with $5\%$ $\ce{CO2}$. Cells also need protein factors that stimulate division and survival, originally supplied as serum (fetal bovine serum, typically $10\%$); the discovery of the growth factors in serum (platelet-derived growth factor, epidermal growth factor) and their replacement by defined, serum-free media came from this need ([7.3.22](/7.3.22)).

Cells grown on rigid plastic in two dimensions differ from cells in tissues in shape, polarity, adhesion and gene expression; fibroblasts in a three-dimensional collagen gel form different adhesions and migrate differently from those on a dish. Three-dimensional cultures include spheroids, cells in matrices such as collagen or the basement-membrane extract Matrigel, and organoids: stem cells of the intestine (Toshiro Sato and Hans Clevers, 2009, from single Lgr5-positive cells), stomach, liver, brain or other organs that self-organize into structures resembling the organ, with its cell types and much of its architecture ([7.3.24](/7.3.24)). Plant cells are cultured as undifferentiated callus or as protoplasts, from which whole plants can be regenerated, a demonstration of totipotency (1.2.1 of [7.3.1](/7.3.1#sec-1.2.1)).

### 3.2.3. Cell Fusion and Hybridomas

Two cells can be fused with an inactivated Sendai virus, polyethylene glycol or an electric pulse into a heterokaryon, a cell with two nuclei in one cytoplasm. Heterokaryons showed that membrane proteins diffuse laterally (the Frye–Edidin experiment, [7.3.4](/7.3.4)) and that the cytoplasm of a mitotic cell induces chromosome condensation in an interphase nucleus ([7.3.20](/7.3.20)). Their most important application is the production of antibodies.

Each B lymphocyte makes antibodies of a single specificity, but it does not divide in culture. Georges Köhler and César Milstein fused antibody-producing B cells from the spleen of an immunized mouse with myeloma cells, a cancerous line of plasma cells that grows indefinitely (1975; Nobel Prize in Physiology or Medicine 1984, with Niels Jerne).

**Definition 3.2.2** A hybrid cell line obtained by fusing an antibody-producing B lymphocyte with a myeloma cell, which grows indefinitely and secretes the antibody of the B cell, is called a **hybridoma**.

Hybrids are selected in HAT medium, which contains hypoxanthine, aminopterin and thymidine. Aminopterin inhibits dihydrofolate reductase and so blocks the de novo synthesis of purine nucleotides and of thymidylate ([7.1.28](/7.1.28)); cells can then survive only by the **salvage pathway**, converting hypoxanthine to IMP with hypoxanthine–guanine phosphoribosyltransferase (HGPRT) and thymidine to TMP with thymidine kinase. The myeloma line lacks HGPRT, so unfused myeloma cells die in HAT medium; unfused B cells die because they do not proliferate in culture; only hybrids, which have the enzyme from the B cell and immortality from the myeloma cell, grow. Each surviving clone is screened (for example by **ELISA**) for the antibody wanted and expanded. The product is a **monoclonal antibody** ([7.1.7](/7.1.7)): a homogeneous reagent of one specificity for one **epitope**, available in unlimited amounts, which has become the standard probe of cell biology and, as humanized and fully human antibodies, a major class of drugs.

## 3.3. Cell Fractionation

### 3.3.1. Homogenization and Differential Centrifugation

**Definition 3.3.1** The separation of the components of broken cells (nuclei, membrane-enclosed organelles, vesicles, macromolecules) into fractions enriched in each, so that their composition and activities can be studied, is called **cell fractionation**.

Cells or tissues are broken gently, by a tight-fitting pestle in a glass tube (Potter–Elvehjem or Dounce homogenizer), by forcing through a narrow orifice, by ultrasound or by osmotic swelling, in an isotonic buffered medium (typically $0.25\,\mathrm{M}$ sucrose) that keeps organelles intact. The endoplasmic reticulum and the plasma membrane break into small sealed vesicles; vesicles derived from the ER are called microsomes ([7.3.7](/7.3.7)). The homogenate is then fractionated by **differential centrifugation** ([7.1.4](/7.1.4#def-4.1.1)), a series of spins at increasing speed and duration.

**Formula 3.3.1 (Pelleting Time)** A particle with **sedimentation coefficient** $s = v/(\omega^2r)$ ([6.3.21](/6.3.21#def-21.3.5)) moves outward as $\mathrm{d}r/\mathrm{d}t = s\omega^2r$, so in a rotor spinning at angular velocity $\omega$ it travels from the top of the liquid at radius $r_1$ to the bottom of the tube at $r_2$ in

$$
t = \frac{\ln(r_2/r_1)}{\omega^2s}. \tag{3.1}
$$
A spin of duration $t$ at relative centrifugal force $\mathrm{RCF} = \omega^2r_2/g$ therefore pellets every particle with $s > s_{\min} = \ln(r_2/r_1)/(\omega^2t)$, and particles with smaller $s$ are pelleted only in proportion to the fraction of the tube they cross.

**Example 3.3.1** In a rotor with $r_1 = 4\,\mathrm{cm}$ and $r_2 = 8\,\mathrm{cm}$, a spin at $1000\,g$ for $10\,\mathrm{min}$ has $\omega^2 = 1000\times9.81/0.08 = 1.2\times10^5\,\mathrm{s^{-2}}$ and pellets particles with $s > \ln 2/(1.2\times10^5\times600) \approx 9\times10^{-9}\,\mathrm{s} \approx 10^5\,\mathrm{S}$: nuclei and unbroken cells. The standard sequence of $20{,}000\,g$ for $20\,\mathrm{min}$, $80{,}000\,g$ for $1\,\mathrm{h}$ and $150{,}000\,g$ for $3\,\mathrm{h}$ pellets particles above about $2400$, $200$ and $35\,\mathrm{S}$: mitochondria, lysosomes and peroxisomes; microsomes and small vesicles; ribosomes and viruses. Soluble proteins ($2$–$20\,\mathrm{S}$) remain in the final supernatant, the cytosolic fraction.

![Differential centrifugation as a sieve on the sedimentation coefficient. Bars: order-of-magnitude ranges of s for the components of a liver homogenate. Dashed lines: the smallest s pelleted completely, s_min = ln(r₂/r₁)/(ω²t), by each of four standard steps in a rotor with r₁ = 4 cm and r₂ = 8 cm. A component is collected in the first step whose line lies below its range; the overlap of ranges (large microsomes with mitochondria, small mitochondria with lysosomes) is why each pellet is only enriched, not pure](./plots/differential-centrifugation.py)

### 3.3.2. Velocity and Equilibrium Gradients

Differential centrifugation separates only components whose sedimentation coefficients differ greatly. Finer separations use gradients, which also stabilize the sedimenting bands against convection.

**Definition 3.3.2** The separation of particles by the rate at which they move through a shallow density gradient (typically $5$–$20\%$ sucrose), less dense than any of them, after being layered in a thin band on top, so that they separate according to their sedimentation coefficient (size and shape) and the run is stopped before they reach the bottom, is called **velocity sedimentation**.

**Definition 3.3.3** The separation of particles in a steep density gradient (of sucrose, cesium chloride, iodixanol or Percoll), in which each particle moves until it reaches the depth where the density of the medium equals its own buoyant density and then stops, independently of its size, is called **equilibrium density-gradient centrifugation** (isopycnic centrifugation).

The two are complementary: velocity sedimentation separates particles of the same density by size (ribosomal subunits, polysomes of different sizes, [7.2.19](/7.2.19)), and isopycnic centrifugation separates particles of similar size by composition. Rough microsomes are denser than smooth ones because of their ribosomes, and DNA molecules differing only in their content of $^{15}\mathrm{N}$ were separated in CsCl gradients in the Meselson–Stahl experiment ([7.2.7](/7.2.7)).

![Velocity and equilibrium sedimentation, simulated as the positions of bands in a tube (v = sω²x with s proportional to the density difference between particle and medium). A: in a shallow gradient much less dense than the particles, three particles of the same density but different s move at constant relative rates, and the run is stopped (dotted line) while they are separated. B: in a steep gradient each particle stops where the medium matches its buoyant density (ER microsomes, mitochondria, lysosomes and peroxisomes, with illustrative densities); small (dashed) and large (solid) particles of the same density arrive at different times but at the same place](./plots/gradient-sedimentation.py)

Christian de Duve's discovery of lysosomes (1955) shows how fractionation was used before organelles could be identified by sight. Following the distribution of enzyme activities among fractions, he found that acid phosphatase sedimented with a group of particles slightly lighter than mitochondria and that its activity was latent: it rose when the particles were disrupted by detergent or freezing and thawing, showing that the enzyme was enclosed by a membrane. Several acid hydrolases followed the same distribution and defined the lysosome before it was seen in the electron microscope; peroxisomes were defined in the same way by catalase and urate oxidase ([7.3.6](/7.3.6), [7.3.11](/7.3.11)). Today organelles are also purified by immunoisolation, with antibodies against a surface protein coupled to magnetic beads, and the protein composition of every fraction of a gradient is measured by quantitative **mass spectrometry**, which assigns thousands of proteins to organelles by the similarity of their profiles (organelle proteomics).

### 3.3.3. Cell-Free Systems

**Definition 3.3.4** A preparation of cell components (an extract, isolated membranes, purified proteins) that carries out a cellular process outside the cell, under conditions the experimenter controls, is called a **cell-free system**.

Cell-free systems allow components to be added, removed, inhibited and purified one at a time until the process is reconstituted from defined parts, which proves that those parts are sufficient for it. Much of this course rests on such experiments:

| Process | Cell-free system | What it revealed | Chapter |
|---|---|---|---|
| Translation | Reticulocyte lysate or wheat germ extract programmed with mRNA | Genetic code, signal sequences | [7.2.19](/7.2.19) |
| Protein translocation into the ER | Translation in the presence of rough microsomes (Günter Blobel) | Cotranslational import, signal peptidase | [7.3.6](/7.3.6) |
| Vesicle transport within the Golgi | Two populations of Golgi membranes, cytosol and ATP (James Rothman) | NSF, SNAP, SNAREs; Nobel Prize 2013 with Randy Schekman and Thomas Südhof | [7.3.8](/7.3.8) |
| Nuclear import | Digitonin-permeabilized cells plus cytosol | Importins, Ran | [7.3.16](/7.3.16) |
| Cell cycle | *Xenopus* egg extracts | Cyclin synthesis and degradation drive the cycle | [7.3.20](/7.3.20) |
| Autophagosome biogenesis | Membranes and cytosol that lipidate LC3 in vitro | Membrane source of the phagophore | [7.3.11](/7.3.11) |

The last example is a cell-free LC3 lipidation assay, in which the conversion of LC3-I to the faster-migrating, lipid-conjugated LC3-II on membranes was used to identify the ER–Golgi intermediate compartment as a source of the autophagosome membrane (Ge, Melville, Zhang and Schekman, 2013).

## 3.4. Tracers and Pulse–Chase Experiments

### 3.4.1. Radioactive and Stable Isotopes

A molecule labeled with an **isotope** behaves chemically like the unlabeled one but can be detected at very low amounts. The radioactive isotopes most used in cell biology are $\beta$ emitters.

| Isotope | **Half-life** | Typical use |
|---|---|---|
| $^3\mathrm{H}$ | $12.3$ years | [³H]thymidine for DNA synthesis, [³H]leucine for protein synthesis; weak emission gives sharp autoradiographs |
| $^{14}\mathrm{C}$ | $5730$ years | Metabolic pathways (Calvin cycle, [7.1.25](/7.1.25)) |
| $^{35}\mathrm{S}$ | $87$ days | [³⁵S]methionine and cysteine for newly made proteins |
| $^{32}\mathrm{P}$ | $14.3$ days | Nucleic acids; [γ-³²P]ATP to label the phosphate transferred by kinases, [α-³²P]ATP to label nucleic acids made from it |
| $^{125}\mathrm{I}$ | $59$ days | Iodination of surface proteins and ligands (γ emitter) |

Radioactivity is measured by scintillation counting or imaged on film or phosphor screens.

**Definition 3.4.1** The detection of the position of a radioactive substance in a specimen (a cell, a section, a gel) by the exposure of a photographic emulsion or phosphor screen placed against it is called **autoradiography**.

In electron-microscope autoradiography a section is coated with a thin emulsion, and each decay produces a silver grain near the labeled molecule, which can be counted over each organelle. Radioactive methods are increasingly replaced by fluorescent labels and by stable isotopes detected by mass spectrometry: in SILAC (stable isotope labeling by amino acids in cell culture), cells grown with $^{13}\mathrm{C}$- or $^{15}\mathrm{N}$-labeled arginine and lysine make proteins whose peptides are heavier, so that protein abundances, synthesis and turnover in two conditions can be compared in one mass spectrum.

### 3.4.2. Pulse–Chase

**Definition 3.4.2** The experiment in which cells are exposed to a labeled precursor for a short time (the pulse), then transferred to an excess of the unlabeled precursor (the chase), and samples taken at intervals show where the labeled molecules made during the pulse are and what has become of them, is called a **pulse–chase experiment**.

The pulse labels a cohort of molecules made at the same time, and the chase follows the cohort as it moves: it is the temporal equivalent of a fluorescent label on a single structure. James Jamieson and George Palade (1967) incubated slices of guinea-pig pancreas with [³H]leucine for three minutes and followed the newly made digestive enzymes by EM autoradiography. At the end of the pulse the silver grains lay over the rough ER; after a few minutes of chase they moved to the Golgi region; after about 40 minutes most lay over condensing vacuoles, and after two hours over zymogen granules near the apical plasma membrane, from which the enzymes are secreted. This established the secretory pathway, ER → Golgi → secretory granules → exocytosis, that is the subject of [7.3.7](/7.3.7)–[7.3.9](/7.3.9), and Palade's share of the 1974 Nobel Prize.

**Formula 3.4.1 (Compartment Model of a Pulse–Chase)** If labeled molecules leave each compartment $i$ of a linear pathway with first-order rate constant $k_i$, their amounts $A_i$ obey

$$
\frac{\mathrm{d}A_1}{\mathrm{d}t} = p(t) - k_1A_1, \qquad \frac{\mathrm{d}A_i}{\mathrm{d}t} = k_{i-1}A_{i-1} - k_iA_i \quad (i \ge 2), \tag{3.2}
$$
where $p(t)$ is the rate of labeling during the pulse and zero during the chase. The mean residence time in compartment $i$ is $1/k_i$, and for a short pulse the mean time to reach compartment $n$ is $\sum_{i<n}1/k_i$.

![A compartment model of the Jamieson–Palade experiment (Eq. 3.2) with a 3 min pulse and illustrative exit rates of 0.12, 0.10, 0.03 and 0.004 min⁻¹ for the rough ER, Golgi, condensing vacuoles and zymogen granules. The fractions of label in each compartment rise and fall in sequence; points mark the classic sampling times of 3, 7, 37 and 117 min, at which the label lies mainly over the rough ER, between ER and Golgi, over condensing vacuoles and over zymogen granules. The order of the peaks shows the order of the compartments; their widths reflect the residence times](./plots/pulse-chase.py)

The model makes explicit what a pulse–chase can and cannot show. The order of the peaks gives the order of the compartments (a precursor–product relationship: the label in a product rises only as it falls in its precursor), and the decay of each curve gives its residence time; the broadening of the later peaks reflects the accumulated randomness of first-order exit. A rapid, transient compartment between two others is seen only if samples are taken more often than its residence time. The same design, with [³⁵S]methionine, immunoprecipitation of one protein and SDS-PAGE, follows the maturation of a single protein: the acquisition of resistance of its N-linked glycans to endoglycosidase H marks arrival in the medial Golgi ([7.3.9](/7.3.9)), the appearance of a cleaved form marks proteolytic processing, and the disappearance of the protein measures its **half-life**.

## 3.5. Flow Cytometry and Cell Sorting

**Definition 3.5.1** The method that passes cells in suspension one by one through one or more focused laser beams, at rates of thousands of cells per second, and measures for each cell the scattered light and the fluorescence in several wavelength bands, is called **flow cytometry**.

Hydrodynamic focusing by a sheath fluid aligns the cells in a stream narrower than a cell. Forward scatter is roughly proportional to the size of the cell, side scatter to its internal granularity, and each fluorescence channel reports a dye or a fluorescent antibody against a surface protein. Because each measurement is made on a single cell, flow cytometry reveals subpopulations that average measurements hide; the many CD ("cluster of differentiation") surface antigens of blood cells are defined this way ([7.15](/7.15)).

**Definition 3.5.2** A flow cytometer that, in addition, breaks the stream into droplets each containing at most one cell, charges each droplet according to the measured properties of its cell, and deflects it electrostatically into a collection tube, so that living cells with chosen properties are isolated, is called a **fluorescence-activated cell sorter** (FACS; Leonard Herzenberg and colleagues, 1972).

A frequent application is the analysis of the cell cycle. A dye that binds DNA stoichiometrically (propidium iodide or DAPI after fixation and RNase treatment, or the cell-permeable Hoechst 33342) makes the fluorescence of each cell proportional to its DNA content: cells in G1 have the diploid amount (2C), cells in G2 and mitosis twice as much (4C), and S-phase cells intermediate amounts ([7.3.20](/7.3.20)). A short pulse of the thymidine analog BrdU or EdU, detected with a fluorescent antibody or by click chemistry, identifies the cells that were replicating DNA during the pulse.

![Cell-cycle analysis by flow cytometry, simulated for 20,000 cells with a 4% coefficient of variation of the DNA signal. A: an asynchronous culture with 55% of cells in G1 (2C peak), 30% in S (between) and 15% in G2/M (4C peak). B: after a mitotic block with nocodazole, cells accumulate with 4C DNA. Shaded areas show the contribution of each phase; the measured histogram is their sum](./plots/flow-dna-content.py)

The fraction of cells in each phase of an exponentially growing culture is related to the duration of the phase, though not simply proportional to it: young cells outnumber old ones in a growing population (by a factor of 2 between birth and division), so phases early in the cycle are overrepresented relative to their duration. Mass cytometry replaces fluorophores with antibodies carrying heavy-metal isotopes detected by mass spectrometry, which removes the spectral overlap that limits fluorescence to about 20 channels and measures 40 or more proteins per cell.

## 3.6. Proteins and Their Interactions

### 3.6.1. Purification and Analysis

The methods for purifying and analyzing proteins are described in [7.1.4](/7.1.4) and [6.4.13](/6.4.13)–[6.4.15](/6.4.15); the table summarizes how cell biologists use them.

| Method | Separates or detects by | Typical use in cell biology |
|---|---|---|
| **Size-exclusion chromatography** | Size | Native size of complexes |
| **Ion-exchange chromatography** | Charge | Purification steps |
| **Affinity chromatography** | Specific binding (antibody, ligand, tag such as His₆ or GST) | One-step purification of a tagged protein and its partners |
| **SDS-PAGE** | Mass of the denatured polypeptide | Analysis of every fraction and immunoprecipitate |
| **Isoelectric focusing**, **two-dimensional gel electrophoresis** | Isoelectric point, then mass | Separation of modified forms (phosphorylation shifts the pI) |
| **Western blot** | Antibody after electrophoresis | Amount, size and modification of one protein |
| **Mass spectrometry** | Mass of peptides | Identification of proteins in a band, complex or organelle; modifications; quantification |

### 3.6.2. Detecting Protein–Protein Interactions

Most proteins work in complexes, and the question "what does it bind?" is asked of almost every new protein. The methods differ in whether they detect binding in vitro or in cells, direct or indirect, stable or transient.

**Definition 3.6.1** The method in which a protein fused to glutathione S-transferase (GST) and bound to glutathione-coated beads is incubated with a cell extract or a purified protein, so that partners that bind it are retained on the beads and detected after washing, is called a **GST pulldown**.

**Definition 3.6.2** The method in which an antibody against one protein (or against an epitope tag fused to it) is used to precipitate it from a cell lysate, together with any proteins bound to it, which are then detected by Western blot or mass spectrometry, is called **co-immunoprecipitation**.

A GST pulldown with two purified proteins tests direct binding, but in vitro; co-immunoprecipitation detects complexes that existed in the cell, but cannot distinguish direct from indirect binding and loses complexes that dissociate during lysis. Chemical cross-linking before lysis captures transient complexes, and cross-linking mass spectrometry identifies the cross-linked residues and hence the contacts. Proximity labeling fuses the protein of interest to an enzyme (a promiscuous biotin ligase in BioID and TurboID, an engineered peroxidase in APEX) that biotinylates all proteins within about $10\,\mathrm{nm}$ in the living cell; the biotinylated proteins are purified with streptavidin and identified by mass spectrometry, giving a map of neighbors, including weak and transient ones.

The **yeast two-hybrid system** ([7.1.15](/7.1.15)) detects binding in the nucleus of yeast by the reconstitution of a transcription factor from a DNA-binding domain fused to the "bait" and an activation domain fused to the "prey"; it screens libraries of millions of preys but gives false positives and misses membrane and modified proteins. **Förster resonance energy transfer** between labeled partners and bimolecular fluorescence complementation detect proximity in living cells ([7.3.2](/7.3.2)). Genetic interactions are a different kind of evidence: a mutation in one gene that suppresses the phenotype of a mutation in another (for example by restoring a disrupted binding interface) suggests that their products interact.

**Definition 3.6.3** The method in which a library of peptides or protein fragments is displayed on the surface of filamentous bacteriophages, each phage carrying the gene for the sequence it displays, and phages that bind an immobilized target are selected, amplified in bacteria and reselected in several rounds, is called **phage display** (George Smith, 1985; Nobel Prize in Chemistry 2018 with Gregory Winter and Frances Arnold).

Phage display finds the binding motifs of a protein domain and is used to evolve high-affinity antibodies without immunization.

### 3.6.3. Measuring Binding: Surface Plasmon Resonance

The methods above show that two proteins bind but not how strongly or how fast. **Surface plasmon resonance** ([6.4.9](/6.4.9)) detects the change in refractive index at a gold sensor surface as an analyte in solution binds a partner immobilized on it, in real time and without labels; the signal, in resonance units (RU), is proportional to the mass bound. For a 1:1 interaction with the analyte in excess, binding follows the relaxation to equilibrium of [Formula 22.1.1 in 7.2.22](/7.2.22#fml-22.1.1):

$$
R(t) = R_{\mathrm{eq}}\left(1 - \mathrm{e}^{-k_{\mathrm{obs}}t}\right), \qquad R_{\mathrm{eq}} = \frac{R_{\max}C}{C + K_{\mathrm{D}}}, \qquad k_{\mathrm{obs}} = k_{\mathrm{on}}C + k_{\mathrm{off}}, \tag{3.3}
$$
and after the analyte is replaced by buffer the complex dissociates as $R(t) = R(0)\mathrm{e}^{-k_{\mathrm{off}}t}$. Fitting the curves at several analyte concentrations $C$ gives $k_{\mathrm{on}}$, $k_{\mathrm{off}}$ and $K_{\mathrm{D}} = k_{\mathrm{off}}/k_{\mathrm{on}}$, which can be checked against the equilibrium isotherm of $R_{\mathrm{eq}}$.

![A simulated SPR experiment for a 1:1 interaction with k_on = 10⁵ M⁻¹ s⁻¹ and k_off = 10⁻³ s⁻¹ (K_D = 10 nM), R_max = 100 RU. A: sensorgrams for analyte at 3–300 nM injected for 120 s, then replaced by buffer; association approaches its plateau faster at higher concentration (k_obs = k_on C + k_off), and dissociation proceeds at the same rate k_off from every curve. B: the equilibrium response against concentration, a binding hyperbola half-saturated at K_D](./plots/spr-sensorgram.py)

## 3.7. Perturbing Gene Function

### 3.7.1. Getting Molecules into Cells

The plasma membrane excludes macromolecules, so DNA, RNA, proteins or antibodies must be introduced by microinjection with a glass needle, by electroporation (an electric pulse opens transient pores), by lipofection (cationic lipids that fuse with the membrane), by bombardment with DNA-coated gold particles (biolistics, used for plant cells) or by viral vectors (lentiviruses integrate into the genome and infect nondividing cells). Introducing DNA into eukaryotic cells is called transfection; integration of the DNA gives a stable line, and expression without integration is transient.

### 3.7.2. Gain of Function: Mutation and Overexpression

Site-directed mutagenesis by **polymerase chain reaction** ([7.2.5](/7.2.5)) changes chosen residues of a protein: a catalytic residue (to make an inactive enzyme), a phosphorylation site (to an alanine that cannot be phosphorylated, or to an aspartate or glutamate that mimics the phosphate), a targeting signal. An inactive mutant that still binds its partners can act as a dominant negative, blocking the endogenous protein, as the GDP-locked mutants of small GTPases do. Expressing a gene at a higher level, or where it is not normally expressed, tests whether it is sufficient for a process. Messenger RNA for Wnt-1 injected into the ventral side of an early *Xenopus* embryo induces a second body axis (McMahon and Moon, 1989), showing that Wnt signaling can specify the dorsal organizer ([7.3.19](/7.3.19)); overexpression of the zebrafish protein Dapper2, which promotes the lysosomal degradation of the Nodal receptors, causes cyclopia (fused eyes), the phenotype of loss of Nodal signaling (Zhang and colleagues, 2004).

### 3.7.3. Loss of Function: Knockdown and Knockout

Loss of function shows whether a gene is necessary. Knockdown reduces the amount of a gene product without changing the gene: **RNA interference** ([7.2.18](/7.2.18)) with transfected **small interfering RNA** acts for a few days, and short hairpin RNA expressed from an integrated vector acts stably; morpholino oligonucleotides block translation or splicing in zebrafish and *Xenopus* embryos. Knockdown is fast but often incomplete and has off-target effects, so a phenotype is credible only if it is reproduced by independent reagents and rescued by a resistant version of the gene.

Knockout destroys the gene. In mice, gene targeting by **homologous recombination** in embryonic stem cells was developed by Mario Capecchi, Martin Evans and Oliver Smithies (Nobel Prize in Physiology or Medicine 2007): a targeting vector carries a selectable marker (neomycin resistance) flanked by sequences homologous to the gene, and a gene for herpes simplex thymidine kinase outside the homology; cells with random insertions keep the thymidine kinase gene and are killed by ganciclovir, whereas cells with homologous recombination lose it (positive–negative selection). Targeted ES cells injected into a blastocyst contribute to a chimeric mouse, whose offspring inherit the allele if the ES cells colonized the germ line.

**Definition 3.7.1** A mouse in which both copies of a gene have been inactivated by gene targeting or genome editing is called a **knockout mouse**.

Many knockouts die as embryos, which shows that the gene is essential but hides its later functions; others have no phenotype because related genes compensate. Both problems are addressed by deleting the gene only in some cells or at some time.

**Definition 3.7.2** A loss-of-function allele that is inactivated only in chosen cell types or at a chosen time, usually by flanking an essential exon with *loxP* sites ("floxing") and expressing the **site-specific recombinase** Cre ([7.2.9](/7.2.9)) from a tissue-specific promoter, or as the tamoxifen-dependent fusion CreERT2, is called a **conditional knockout**; the method is the Cre–*loxP* system.

![A conditional knockout with the Cre–loxP system, in SBOL Visual symbols. Top: a floxed allele, in which exon 2 is flanked by two loxP sites (triangles) in the same orientation placed in introns, so that the gene is expressed normally. Middle: a transgene expressing Cre recombinase from the hepatocyte-specific albumin promoter. Bottom: in offspring carrying both, Cre excises the DNA between the loxP sites in hepatocytes, leaving one loxP site and an allele without exon 2; the excised circle is lost. Other tissues keep the intact gene](./plots/cre-lox.py)

**CRISPR–Cas9** ([7.2.24](/7.2.24)) has made knockouts possible in almost any cell line or organism within weeks: a guide RNA directs Cas9 to cut the gene, and repair by error-prone end joining introduces small insertions and deletions that shift the reading frame. Templated repair inserts point mutations or tags at the endogenous locus (knock-in), so that a fluorescently tagged protein is expressed at its natural level (2.5.1 of [7.3.2](/7.3.2#sec-2.5.1)). Libraries of guide RNAs against every gene make genome-wide **pooled screens** possible ([7.2.24](/7.2.24#sec-24.7)), in which the cells that survive or sort with a phenotype reveal the genes needed for it. In animals, knocking out *FGF5*, which limits the hair-growth phase, produces long hair, as in naturally occurring "angora" mutations of mice, cats and dogs; CRISPR knockouts of *FGF5* in goats and sheep have been made to increase wool yield. Plants are transformed with *Agrobacterium* Ti plasmids that transfer DNA into the plant genome.

Acute methods act faster than any genetic deletion. Degron tags fused to the endogenous protein (the auxin-inducible degron, the dTAG system) target it for proteasomal degradation within minutes to an hour after a small molecule is added, and chemical inhibitors and optogenetic tools ([7.3.2](/7.3.2#sec-2.5.3)) act within seconds. Fast perturbations reveal direct effects before the cell adapts.

| Perturbation | Level | Speed | Reversible | Main caveats |
|---|---|---|---|---|
| Inhibitor, drug | Protein activity | Seconds to minutes | Often | Specificity |
| Optogenetic tool | Protein activity or location | Seconds | Yes | Requires engineering, light delivery |
| Degron | Protein amount | Minutes to hours | Yes | Tag may alter function |
| RNAi, morpholino | mRNA | Days | Yes (transient) | Incomplete, off-target |
| CRISPR or targeted knockout | Gene | Weeks (cell lines) to months (mice) | No | Compensation, lethality |
| Conditional knockout | Gene, chosen cells and time | Days after Cre activity | No | Leaky or mosaic Cre |
| Overexpression, dominant negative | Protein amount or activity | Hours to days | Variable | Nonphysiological levels |

### 3.7.4. Reading Out the Effect

After a perturbation the cell is observed with the methods of [7.3.2](/7.3.2) and of this chapter, and its state is measured at genome scale. RNA sequencing measures the **transcriptome** of a population or of single cells ([7.2.6](/7.2.6#sec-6.9)), and clustering of expression profiles across treatments groups genes that respond together; mass spectrometry measures the **proteome** and its modifications. Single-cell RNA sequencing of whole tissues, in projects such as the Human Cell Atlas, classifies cells by their expression profiles and has found cell types that were invisible to morphology. Each of these readouts answers one part of the systems question of [7.3.1](/7.3.1#sec-1.7.2): which parts change together when one part is perturbed. Interpreting them follows the logic of necessity and sufficiency of [7.2.1](/7.2.1#sec-1.3.1): loss of function shows what is required, gain of function what is enough, and reconstitution (3.3.3) what is sufficient in the absence of the rest of the cell.

## Summary

| Topic | Key points |
|---|---|
| Electron microscopy (Definitions 3.1.1–3.1.6) | Electron wavelength picometres, but specimen-limited resolution (about $2\,\mathrm{nm}$ in sections); fixation (glutaraldehyde, $\ce{OsO4}$), resin sections, heavy-metal stains; rapid freezing; negative staining; freeze-fracture splits membranes into P and E faces with intramembrane particles; enzyme cytochemistry shows the polarity of the Golgi; immunogold; SEM for surfaces and volume EM; cryo-ET with FIB milling and subtomogram averaging |
| Cell culture (Definitions 3.2.1–3.2.2) | Primary cultures vs immortal cell lines (telomerase, loss of checkpoints, viral oncogenes); anchorage dependence, contact inhibition, Hayflick limit; HeLa (1951) and cell-line authentication; Eagle's medium and serum growth factors; 3D culture and organoids; heterokaryons; hybridomas selected in HAT medium (salvage pathway, HGPRT-deficient myeloma) give monoclonal antibodies |
| Fractionation (Definitions 3.3.1–3.3.4) | Homogenization in isotonic sucrose; differential centrifugation pellets $s > \ln(r_2/r_1)/(\omega^2t)$ (Formula 3.3.1, Example 3.3.1); velocity sedimentation by size, isopycnic centrifugation by density; de Duve's latency and marker enzymes; immunoisolation and organelle proteomics; cell-free systems prove sufficiency |
| Tracers (Definitions 3.4.1–3.4.2) | ³H, ¹⁴C, ³⁵S, ³²P, ¹²⁵I; autoradiography; SILAC; Jamieson–Palade pulse–chase defined the secretory pathway; compartment model (Formula 3.4.1): peak order gives pathway order, $1/k_i$ residence times |
| Flow cytometry (Definitions 3.5.1–3.5.2) | Scatter and fluorescence of single cells at thousands per second; FACS sorts living cells; DNA content histograms (2C, S, 4C); BrdU/EdU; mass cytometry |
| Interactions (Definitions 3.6.1–3.6.3) | GST pulldown (direct, in vitro), co-IP (in cells, possibly indirect), cross-linking, proximity labeling, yeast two-hybrid, FRET, phage display, genetic suppression; SPR gives $k_{\mathrm{on}}$, $k_{\mathrm{off}}$, $K_{\mathrm{D}}$ (Eq. 3.3) |
| Perturbation (Definitions 3.7.1–3.7.2) | Delivery methods; site-directed mutants and dominant negatives; overexpression tests sufficiency (Wnt second axis, Dapper2); RNAi and morpholinos; knockout by homologous recombination in ES cells; Cre–*loxP* conditional knockouts; CRISPR knockouts, knock-ins, pooled screens; degrons and optogenetics for acute loss; transcriptome and proteome readouts |

## Questions

1. A homogenate is centrifuged at $15{,}000\,g$ for $10\,\mathrm{min}$ in a rotor with $r_1 = 5\,\mathrm{cm}$ and $r_2 = 9\,\mathrm{cm}$. Which particles are pelleted completely? A colleague's protocol uses $10{,}000\,g$ for $15\,\mathrm{min}$ in the same rotor. Is it equivalent?

   **Answer** $\omega^2 = 15{,}000\times9.81/0.09 = 1.64\times10^6\,\mathrm{s^{-2}}$, and $s_{\min} = \ln(9/5)/(1.64\times10^6\times600) = 0.588/9.8\times10^8 = 6.0\times10^{-10}\,\mathrm{s} = 6000\,\mathrm{S}$ by Formula 3.3.1: mitochondria and most lysosomes and peroxisomes, with large microsomes partly. Since $s_{\min} \propto 1/(\omega^2t) \propto 1/(\mathrm{RCF}\times t)$, the product $g\times t$ determines the cut: $15{,}000\times10 = 150{,}000$ and $10{,}000\times15 = 150{,}000\,g\cdot\mathrm{min}$, so the protocols are equivalent (neglecting acceleration and deceleration).

2. Lysosomes and mitochondria from liver overlap in differential centrifugation. Which kind of gradient would you use to separate them, and why? How did de Duve show, without such a gradient, that acid phosphatase is enclosed in a membrane-bounded particle?

   **Answer** Their sedimentation coefficients overlap, so velocity separation is poor; their buoyant densities differ, so an isopycnic gradient (Definition 3.3.3, for example of Nycodenz or Percoll, sometimes after loading lysosomes with the detergent Triton WR-1339 to make them lighter) separates them. De Duve found that the measured activity of acid phosphatase in a fraction rose several-fold after treatments that break membranes (detergent, freezing and thawing, hypotonic media): the enzyme was latent because its substrate could not reach it across an intact membrane.

3. In a pulse–chase experiment like that of Jamieson and Palade, the label over the Golgi region peaks at $10\,\mathrm{min}$ and the label over condensing vacuoles at $30\,\mathrm{min}$. A drug is found that abolishes the Golgi peak but leaves the time of arrival in condensing vacuoles unchanged. What would you conclude? What alternative explanation should be tested?

   **Answer** If the Golgi were a required intermediate compartment, removing its peak without delaying arrival downstream would be unexpected; one conclusion is that the drug accelerates exit from the Golgi so much that its residence time ($1/k_{\mathrm{Golgi}}$ in Formula 3.4.1) falls below the sampling interval, so that the transient Golgi peak is missed. The alternative, that the drug opens a bypass from ER to condensing vacuoles, must be tested by sampling more frequently and by testing for Golgi-specific modifications of the secreted proteins (such as complex glycans or endoglycosidase H resistance), which a bypass would not produce.

4. Hybridomas are made from a myeloma line that lacks HGPRT. Why is this deficiency needed, and what would happen to unfused myeloma cells and to unfused B cells in HAT medium? Could a myeloma deficient in thymidine kinase be used instead?

   **Answer** Aminopterin in HAT medium blocks de novo synthesis of purines and thymidylate, so cells must use the salvage pathway, which needs HGPRT (for hypoxanthine) and thymidine kinase (for thymidine). Unfused HGPRT-deficient myeloma cells cannot salvage hypoxanthine and die; unfused B cells have HGPRT but do not proliferate in culture and die within days; hybrids get HGPRT from the B cell and immortality from the myeloma and survive. A thymidine-kinase-deficient myeloma would work on the same principle, since it cannot use the thymidine supplied and could not make thymidylate de novo; both kinds of deficient lines have been used.

5. An SPR experiment shows that a protein binds an immobilized partner with an association rate that is linear in concentration: $k_{\mathrm{obs}} = 0.012\,\mathrm{s^{-1}}$ at $100\,\mathrm{nM}$ and $0.032\,\mathrm{s^{-1}}$ at $300\,\mathrm{nM}$. Find $k_{\mathrm{on}}$, $k_{\mathrm{off}}$ and $K_{\mathrm{D}}$. What is the mean lifetime of the complex?

   **Answer** From $k_{\mathrm{obs}} = k_{\mathrm{on}}C + k_{\mathrm{off}}$ (Eq. 3.3): $k_{\mathrm{on}} = (0.032 - 0.012)/(200\times10^{-9}\,\mathrm{M}) = 1.0\times10^5\,\mathrm{M^{-1}\,s^{-1}}$ and $k_{\mathrm{off}} = 0.012 - 10^5\times10^{-7} = 0.002\,\mathrm{s^{-1}}$. $K_{\mathrm{D}} = k_{\mathrm{off}}/k_{\mathrm{on}} = 2\times10^{-8}\,\mathrm{M} = 20\,\mathrm{nM}$. The mean lifetime is $1/k_{\mathrm{off}} = 500\,\mathrm{s}$, about 8 minutes; the dissociation phase should be followed for at least that long to measure $k_{\mathrm{off}}$ reliably.

6. You want to know whether a protein required for early embryonic development also functions in adult liver. Design a genetic experiment in the mouse, and name two controls.

   **Answer** A conventional knockout is embryonic lethal, so make a conditional allele: flank an essential exon with *loxP* sites (Definition 3.7.2) and cross the floxed mice with mice expressing Cre from the albumin promoter (hepatocytes), or with an inducible CreERT2 line and inject tamoxifen in adults to avoid developmental effects. Controls: floxed mice without Cre (the floxed allele alone should be normal) and Cre-expressing mice without the floxed allele (Cre itself can be toxic or the transgene can disrupt a gene); deletion should be confirmed in the target tissue by PCR or Western blot, since Cre activity may be mosaic.
