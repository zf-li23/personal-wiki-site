---
title: Light Microscopy and Live-Cell Imaging
description: "How cells are seen alive: the diffraction limit, numerical aperture and sampling; contrast methods for unstained cells (phase contrast, DIC, dark field, polarization); fluorescence and immunofluorescence; optical sectioning by deconvolution, confocal, two-photon, light-sheet and TIRF microscopy; super-resolution (SIM, STED, single-molecule localization with precision s/sqrt(N), MINFLUX, expansion microscopy); fluorescent proteins, Ca2+ indicators and biosensors; and quantitative imaging: FRAP with fitted D and mobile fraction, FLIP, FRET by acceptor bleaching and FLIM, single-particle tracking and the mean squared displacement."
---

Most of what is known about the organization of living cells has been seen before it was understood. The light microscope is the instrument of cell biology because it is the only one that can watch living cells: it uses visible light, which passes through water and does little damage, and it works at the scale of cells and organelles. Its weaknesses are that most cellular components are transparent and colorless, so contrast must be created, and that diffraction limits its resolution to about $200\,\mathrm{nm}$, larger than most protein complexes. This chapter treats, in order, the limit of resolution (2.1), the optical methods that make unstained cells visible (2.2), fluorescence microscopy and the methods of optical sectioning (2.3), the super-resolution methods that circumvent the diffraction limit (2.4), the probes that label specific molecules and report the chemistry of the cell (2.5), and the quantitative methods that turn images into measurements of diffusion, binding and transport (2.6). The physics of diffraction is developed in optics ([5.4.2](/5.4.2)), the photophysics of fluorescence and the principles of confocal and super-resolution microscopy in analytical chemistry ([6.4.10](/6.4.10)); here the emphasis is on what each method shows about cells and how its output is interpreted. Electron microscopy, which resolves finer detail in dead and fixed cells, follows in [7.3.3](/7.3.3).

## 2.1. Resolution

### 2.1.1. The Diffraction Limit

A compound light microscope has three parts: an illumination system (light source, collector lens, field and aperture diaphragms, condenser), the imaging optics (objective and eyepiece, or a camera) and the mechanical stand with stage and focus drive. The objective forms a magnified, inverted real image of the specimen (in modern infinity-corrected microscopes with the help of a tube lens), and the eyepiece magnifies this intermediate image again into a virtual image seen by the eye; the total magnification is the product of the two. In Köhler illumination (August Köhler, 1893) the condenser is adjusted so that the specimen is lit evenly and the aperture of the illumination matches that of the objective.

A lens images a point source not as a point but as a diffraction pattern, the **Airy disk** surrounded by faint rings, whose width is set by the wavelength and by the cone of light the lens collects ([5.4.2](/5.4.2#sec-2.4.1)). Two points closer than about the width of this pattern merge into one.

**Definition 2.1.1** The smallest distance at which two point objects can still be distinguished as separate in the image is called the **limit of resolution** of the microscope.

**Definition 2.1.2** For an objective that accepts light within a half-angle $\theta$ from a specimen immersed in a medium of refractive index $n$, the quantity $\mathrm{NA} = n\sin\theta$ is called its **numerical aperture**.

Since $\sin\theta < 1$, a dry objective has $\mathrm{NA} < 1$ (in practice at most $0.95$); immersion in water ($n = 1.33$), glycerol ($n = 1.47$) or oil ($n = 1.515$, matching the glass of the coverslip and front lens, originally cedarwood oil) raises it to about $1.2$, $1.35$ and $1.4$–$1.49$ respectively. Media of still higher index, such as α-bromonaphthalene ($n = 1.66$) with special high-index coverslips, push the NA to about $1.6$, the practical maximum.

**Formula 2.1.1 (Resolution of the Light Microscope)** By the **Rayleigh criterion** ([5.4.2](/5.4.2#sec-2.4.2)), the lateral limit of resolution for light of wavelength $\lambda$ is

$$
d_{xy} = \frac{0.61\lambda}{\mathrm{NA}}; \tag{2.1}
$$
Abbe's criterion, derived for periodic objects, gives $\lambda/(2\,\mathrm{NA})$. Along the optical axis the resolution is about $d_z \approx 2n\lambda/\mathrm{NA}^2$, two to three times worse.

**Example 2.1.1** For green emission ($\lambda = 520\,\mathrm{nm}$) and an oil objective with $\mathrm{NA} = 1.4$, $d_{xy} = 0.61\times520/1.4 \approx 230\,\mathrm{nm}$ and $d_z \approx 2\times1.515\times520/1.96 \approx 800\,\mathrm{nm}$. A mitochondrion ($0.5\,\mu\mathrm{m}$ wide) is resolved; the two membranes of its envelope ($20\,\mathrm{nm}$ apart), a $25\,\mathrm{nm}$ microtubule and a $100\,\mathrm{nm}$ vesicle are not.

![Diffraction and resolution. A: the image profile of two point sources (solid) as the sum of two Airy patterns (dotted), for separations of 1.0, 0.75 and 0.5 times the Rayleigh distance d = 0.61λ/NA (about 230 nm for λ = 520 nm, NA = 1.4); at d the summed profile still shows a dip of about a quarter, at half of d it shows a single peak. B: lateral and axial resolution against numerical aperture for green light, with the apertures of typical dry, water-immersion and oil-immersion objectives](./plots/resolution.py)

Resolution must not be confused with detection. An isolated object much smaller than $d_{xy}$ that emits light, such as a single microtubule labeled with a fluorescent dye or a single fluorescent molecule, is readily seen, but it appears as a blur at least $200\,\mathrm{nm}$ wide; what cannot be done is to separate two such objects close together. Super-resolution methods (2.4) exploit exactly this difference.

### 2.1.2. Magnification, Sampling and the Photon Budget

Magnification only spreads the image over a larger area; beyond about $500$–$1000$ times the NA it adds no detail ("empty magnification"). The same limit follows from the eye: to be seen, a detail of $0.2\,\mu\mathrm{m}$ must be enlarged to the $0.1$–$0.2\,\mathrm{mm}$ that the eye resolves at reading distance, so the largest useful magnification of a light microscope is about $1000$–$1500\times$. For a digital camera the relevant quantity is the pixel size referred to the specimen. By the Nyquist–Shannon sampling theorem a detail of size $d$ is recorded faithfully only if the pixel is at most about $d/2$ to $d/2.3$: a camera with $6.5\,\mu\mathrm{m}$ pixels behind a $100\times$ objective samples the specimen at $65\,\mathrm{nm}$, sufficient for $230\,\mathrm{nm}$ resolution, whereas behind a $20\times$ objective ($325\,\mathrm{nm}$ pixels) it would discard the resolution of the lens.

In live-cell imaging the limiting resource is usually light. An image is made of photons, and the number $N$ collected per pixel has Poisson noise $\sqrt{N}$, so the signal-to-noise ratio is at most $\sqrt{N}$. More light gives better images but bleaches the fluorophores and damages the cell, mainly by generating **reactive oxygen species**. Every experiment trades spatial resolution, temporal resolution, signal-to-noise ratio and the duration of observation against each other within a fixed "photon budget"; the methods of 2.3 differ largely in how economically they spend it.

## 2.2. Contrast in Unstained Cells

### 2.2.1. Bright Field and Staining

In *bright-field microscopy* the specimen is illuminated from below and seen by the light it transmits. A living cell absorbs almost no visible light and appears nearly invisible. Classical cytology therefore fixed tissue (with formaldehyde or glutaraldehyde, which cross-link proteins), cut it into sections a few micrometres thick and stained it with dyes that bind selectively to classes of molecules: hematoxylin (with a metal mordant) colors nucleic-acid-rich nuclei blue and eosin colors proteins pink, the Feulgen reaction stains DNA quantitatively, the periodic acid–Schiff (PAS) reaction stains polysaccharides. Fixation kills the cell and can create artifacts, so the methods below, which generate contrast optically, were essential for the study of living cells.

Staining reactions that are chemically specific enough to show where a class of molecules or an enzyme activity lies in a cell are the methods of *cytochemistry* (histochemistry in tissues). Fixation is chosen to preserve the target: physical fixation (air-drying of blood smears, freeze-drying) or chemical fixation, by precipitating agents (methanol, ethanol, acetone) or cross-linking ones (formaldehyde, glutaraldehyde, osmium tetroxide); polysaccharides are best kept by alcohol fixation, enzyme activities by brief fixation in cold buffered formaldehyde or acetone, which leaves them active.

| Reaction | Principle | Shows |
|---|---|---|
| Feulgen reaction (1924) | Mild acid hydrolysis removes purines from DNA and exposes aldehydes on deoxyribose; Schiff's reagent (decolorized basic fuchsin) turns magenta where it reacts with aldehydes | DNA, quantitatively (Feulgen cytophotometry of nuclear DNA content) |
| Periodic acid–Schiff (PAS) | Periodic acid oxidizes vicinal hydroxyl groups of sugars to aldehydes, which react with Schiff's reagent | Glycogen, glycoproteins, mucins, basement membranes |
| Metal precipitation (Gomori, 1939) | The enzyme releases phosphate from a substrate; the phosphate is trapped as an insoluble lead or calcium salt, converted to black lead or cobalt sulfide | Acid phosphatase (lysosomes), alkaline phosphatase (brush borders); the lead product is also visible in the electron microscope |
| Peroxidase reaction | Peroxidase oxidizes a colorless chromogen with $\ce{H2O2}$ into a colored precipitate (historically benzidine, now diaminobenzidine, which is less carcinogenic and gives an electron-dense product) | Peroxidases of blood cells; horseradish peroxidase used as a label (2.3.1) |
| Sudan dyes (Sudan III, IV, black B), Oil Red O | Lipid-soluble dyes dissolve preferentially in lipid droplets | Neutral fat and lipid droplets in frozen sections |
| Methyl green–pyronin | Methyl green binds DNA, pyronin RNA | DNA green in the nucleus, RNA red in the nucleolus and the cytoplasm of protein-secreting cells |
| Ninhydrin, Millon's reaction | Reaction with free amino groups; with tyrosine | Proteins |
| Vital stains: Janus green B, neutral red | Taken up by living cells; Janus green B is kept oxidized (blue-green) by the respiratory chain, neutral red accumulates in acidic compartments | Mitochondria; lysosomes and vacuoles |

### 2.2.2. Phase Contrast, DIC and Dark Field

Light passing through a cell is slowed by its higher refractive index ($n \approx 1.36$–$1.40$, against $1.33$ for water) and emerges with a phase lag $\Delta\varphi = 2\pi(n_{\mathrm{c}} - n_{\mathrm{m}})t/\lambda$ that depends on the thickness $t$ and the refractive-index difference: for a $5\,\mu\mathrm{m}$ cell with $\Delta n = 0.03$ in green light, $\Delta\varphi \approx 1.8\,\mathrm{rad}$. The eye and the camera detect intensity, not phase, so this information is lost in bright field.

**Definition 2.2.1** The method that converts the phase shifts of light passing through a transparent specimen into differences of brightness, by shifting the phase of the undiffracted light by a quarter wavelength relative to the light diffracted by the specimen so that the two interfere, is called **phase-contrast microscopy** (Frits Zernike, 1934; Nobel Prize in Physics 1953).

Two components make it work: an annular diaphragm in front of the condenser, which illuminates the specimen with a hollow cone of light, and a phase plate in the back focal plane of the objective, a ring coated with a thin layer (of magnesium fluoride, for example) that advances or retards the undiffracted light passing through it by a quarter wavelength and dims it, while the diffracted light passes beside the ring. Phase contrast shows the outline of cells, the nucleus and nucleolus and larger organelles with high contrast, and it is the standard way of inspecting cultured cells. Its images have bright halos around edges and do not permit optical sectioning.

**Definition 2.2.2** The method that splits polarized light into two orthogonally polarized beams laterally displaced (sheared) by less than the resolution limit, passes them through neighboring points of the specimen and recombines them so that they interfere, making the image brightness proportional to the gradient of optical path length, is called **differential interference contrast microscopy** (DIC, Nomarski optics).

DIC images look like a relief illuminated from one side, have no halos and, because they use the full aperture of the objective, a shallow depth of field that gives a degree of optical sectioning; DIC is used to follow organelle movement, mitosis and cell motility in time-lapse recordings. In *dark-field microscopy* the specimen is illuminated obliquely, by a condenser whose central part is blocked, so that only light scattered by the specimen enters the objective; bright objects appear on a black background, and objects below the resolution limit that scatter strongly (bacterial flagella, single microtubules, colloidal particles down to a few nanometres) become visible as points of light, although their shape is not resolved. In *polarized-light microscopy* the specimen, on a rotating stage, is placed between crossed polarizers (the polarizer below the condenser and the analyzer above the objective) and only birefringent structures, whose refractive index depends on the direction of polarization (**polarization**, [5.4.3](/5.4.3)), are bright; ordered arrays of filaments such as the mitotic spindle, the A bands of muscle and cellulose microfibrils are birefringent, and Shinya Inoué used this method in the 1950s to show that spindle fibers exist in living cells and are in dynamic equilibrium with a pool of subunits.

| Method | Contrast from | Best for | Limitations |
|---|---|---|---|
| Bright field | Absorption | Stained, fixed sections | Living cells nearly invisible |
| Phase contrast | Phase shift (optical path) | Routine inspection of cultured cells | Halos; no sectioning |
| DIC | Gradient of optical path | Time-lapse of organelles, mitosis, motility | Needs non-birefringent dishes |
| Dark field | Scattering | Objects below the resolution limit | Little structural detail |
| Polarized light | Birefringence | Spindles, muscle, cell walls | Only ordered structures |

Cultured cells grow on the bottom of a dish under a layer of medium, too far from an objective placed above them. In the *inverted microscope* the positions are reversed: the illumination and condenser are above the stage and the objectives below it, looking up through the bottom of the dish. Inverted microscopes, usually equipped for phase contrast, DIC and fluorescence and fitted with stage incubators that keep the cells at $37\,^\circ\mathrm{C}$ and $5\,\%$ $\ce{CO2}$, are the standard instruments for live-cell imaging, microinjection and micromanipulation ([7.3.3](/7.3.3)). Modern research microscopes combine all the contrast modes of this section and the fluorescence methods of the next in one motorized, computer-controlled stand.

## 2.3. Fluorescence Microscopy

### 2.3.1. Epifluorescence and Immunofluorescence

The methods of 2.2 show where there is matter but not what it is. **Fluorescence** ([6.4.10](/6.4.10#sec-10.1)) provides chemical specificity: a fluorophore absorbs light of one wavelength and emits at a longer one, and filters separate the weak emission from the much stronger excitation, so that labeled molecules shine against a dark background.

**Definition 2.3.1** The method that images the distribution of fluorescent molecules in a specimen, by exciting them with light of a short wavelength and forming the image only from their longer-wavelength emission, is called **fluorescence microscopy**.

In the usual epifluorescence arrangement the objective both delivers the excitation and collects the emission, which a dichroic mirror separates ([6.4.10](/6.4.10#sec-10.4.1)). Using fluorophores with separated spectra, three to five different molecules can be imaged in the same cell. Some probes label structures directly: DAPI and Hoechst stain DNA, phalloidin (a mushroom toxin) coupled to a dye binds actin filaments, potential-sensitive dyes accumulate in active mitochondria. Antibodies label any protein against which they can be raised.

**Definition 2.3.2** The localization of a specific molecule in fixed cells or tissue with an **antibody** that binds it and carries a fluorescent label, either directly (direct immunofluorescence) or through a labeled secondary antibody that binds the first (indirect immunofluorescence), is called **immunofluorescence**.

Cells are first fixed and their membranes permeabilized with a detergent so that antibodies can enter. The indirect method amplifies the signal, because several secondary antibodies bind each primary antibody, and one labeled secondary antibody (for example anti-rabbit immunoglobulin) serves for all primary antibodies raised in one species. Instead of a fluorophore the secondary antibody can carry an enzyme such as horseradish peroxidase or alkaline phosphatase, which deposits a colored precipitate for bright-field microscopy, or colloidal gold particles for electron microscopy ([7.3.3](/7.3.3)). The specificity of the result is only as good as that of the antibody, which must be validated, for example by the loss of staining in cells lacking the protein.

Nucleic acids are located in the same way by hybridization. In in situ hybridization a labeled single-stranded DNA or RNA probe is applied to fixed cells or chromosomes whose own nucleic acids have been made accessible (and, for DNA, denatured), and it pairs with the complementary sequence where it lies. The first probes were radioactive and detected by autoradiography ([7.3.3](/7.3.3)); **fluorescence in situ hybridization** (FISH) with fluorescent or hapten-labeled probes now maps genes on chromosomes, counts chromosomes in single cells, shows the position of chromosome territories in the nucleus ([7.3.17](/7.3.17)) and, with many short probes against one mRNA, counts single mRNA molecules in each cell (smFISH). smFISH and the hybridization methods for extracted nucleic acids (**Southern blot** and **Northern blot**) are treated in [7.2.6](/7.2.6).

### 2.3.2. Optical Sectioning

In a widefield microscope every plane of a thick specimen fluoresces, and the out-of-focus light blurs the image of the plane in focus. Five methods remove or avoid this light.

1. Deconvolution. The image is the object convolved with the three-dimensional point spread function of the microscope, which can be measured with fluorescent beads. A stack of widefield images at different focal planes is computationally deconvolved, which reassigns out-of-focus light to its source. The method is economical with light but requires accurate knowledge of the point spread function.
2. Confocal microscopy. The **confocal microscope** ([6.4.10](/6.4.10#def-10.4.1)) illuminates one point at a time with a focused laser beam and places a pinhole in front of the detector at a plane conjugate to the focus, so that light from above and below the focal plane is blocked. Scanning yields an optical section about $0.5$–$0.8\,\mu\mathrm{m}$ thick, and a stack of sections a three-dimensional reconstruction. The gain is mainly in contrast and in the axial direction; lateral resolution improves only modestly, by at most about $\sqrt{2}$ with a nearly closed pinhole, at a great cost in signal. Spinning-disk confocal microscopes scan thousands of pinholes in parallel and image living cells faster and with less bleaching.
3. Two-photon excitation. In *two-photon microscopy* a fluorophore can be excited by the simultaneous absorption of two near-infrared photons of twice the wavelength (Winfried Denk, James Strickler and Watt Webb, 1990). The probability of two-photon absorption is proportional to the square of the light intensity, which is high enough only at the focus of a pulsed laser; excitation, and therefore bleaching, is confined to the focal volume without a pinhole, and infrared light scatters less in tissue, so that neurons can be imaged up to about $1\,\mathrm{mm}$ deep in the living brain.
4. Light sheets. Both the confocal and the two-photon microscope excite molecules above and below the focal plane on the way to it (or, in two-photon, at least scan the whole volume), so a three-dimensional recording exposes each plane many times.

   **Definition 2.3.3** The method that illuminates the specimen from the side with a thin sheet of light, a few micrometres thick, coinciding with the focal plane of a detection objective placed at right angles, so that only the plane being imaged is excited, is called **light-sheet microscopy**.

   Light-sheet microscopes (selective plane illumination, Huisken and Stelzer, 2004; the lattice light sheet of Eric Betzig's laboratory, 2014) record whole embryos for days with little photodamage and image single cells at subsecond intervals in three dimensions.
5. Total internal reflection. When light in glass strikes the interface with the aqueous medium at an angle larger than the critical angle, it is totally reflected, but an evanescent field penetrates a short distance into the medium, with intensity decaying as $I(z) = I_0\mathrm{e}^{-z/\delta}$ and

   $$
   \delta = \frac{\lambda}{4\pi\sqrt{n_1^2\sin^2\theta - n_2^2}}, \tag{2.2}
   $$
   typically $70$–$200\,\mathrm{nm}$ ($n_1$: glass, $n_2$: medium, $\theta$: angle of incidence).

   **Definition 2.3.4** The method that excites fluorophores only within the evanescent field, about $100\,\mathrm{nm}$ deep, at the interface between the coverslip and a cell, so that events at the basal plasma membrane are seen without background from the rest of the cell, is called **total internal reflection fluorescence microscopy** (TIRF microscopy).

   TIRF microscopy shows single exocytic events, clathrin-coated pits forming and disappearing at the plasma membrane ([7.3.10](/7.3.10)), and single molecules moving on reconstituted membranes or filaments.

![Four geometries of fluorescence microscopy. A: widefield epifluorescence excites the whole depth of the specimen (shaded), and the camera collects light from all planes. B: in a confocal microscope the focused laser excites a double cone; light from the focus (solid) passes the pinhole, light from above and below (dashed) is blocked. C: in a light-sheet microscope a thin sheet entering from the side excites only the observed plane. D: in TIRF the totally reflected beam creates an evanescent field about 100 nm deep that excites only the basal surface of the cell](./plots/optical-sectioning.py)

## 2.4. Super-Resolution Fluorescence Microscopy

### 2.4.1. The Principle and the Methods

The diffraction limit applies to molecules that emit at the same time. **Super-resolution fluorescence microscopy** ([6.4.10](/6.4.10#def-10.4.2)) circumvents it by switching fluorophores between an emitting and a dark state, so that neighbors within one diffraction-limited spot emit at different times or are confined to a region smaller than the spot. The photophysics of the switching and the derivation of the STED resolution are given in 6.4.10; the methods differ in the resolution they reach, their speed and the demands they place on the sample.

| Method | Principle | Lateral resolution | Speed and use |
|---|---|---|---|
| Structured illumination (SIM) | Striped illumination shifts fine detail into the passband; computational reconstruction | About $100\,\mathrm{nm}$ (twofold gain) | Fast, ordinary fluorophores; live cells in three dimensions |
| STED | A ring-shaped depletion beam confines emission to a subdiffraction spot, which is scanned | $20$–$50\,\mathrm{nm}$ | Seconds per image; intense light |
| Single-molecule localization (PALM, STORM) | Sparse subsets of switchable fluorophores are localized one by one | $10$–$30\,\mathrm{nm}$ | Minutes per image; mostly fixed cells |
| MINFLUX | Localization with a patterned beam whose intensity minimum is scanned around the molecule | $1$–$3\,\mathrm{nm}$ | Very few photons per localization; small fields |
| Expansion microscopy | The specimen is embedded in a swellable hydrogel and physically expanded about 4.5-fold (up to about 20-fold iteratively) | $60$–$70\,\mathrm{nm}$ with a confocal microscope; better with iteration | Fixed samples; ordinary microscopes |

Super-resolution images have resolved, for example, the eightfold symmetry of the nuclear pore complex, the periodic rings of actin and spectrin spaced $190\,\mathrm{nm}$ apart under the axonal membrane, and contacts between the ER exit sites and the ER–Golgi intermediate compartment ([7.3.8](/7.3.8)). Two limits remain that are not optical. The label is displaced from its target, by $10$–$20\,\mathrm{nm}$ for a primary plus secondary antibody, which is comparable to the resolution; and a structure is resolved only if it is labeled densely enough. By the sampling theorem, resolving a detail of size $d$ requires labels spaced at most $d/2$, a density of at least $(2/d)^2$ per unit area in two dimensions: for $d = 20\,\mathrm{nm}$, about $10^4$ labels per $\mu\mathrm{m}^2$.

### 2.4.2. Single-Molecule Localization

**Definition 2.4.1** The super-resolution methods that record many images in each of which only a sparse, random subset of photoswitchable fluorophores is in the emitting state, determine the position of each emitting molecule from the center of its diffraction-limited image, and assemble the positions of all molecules into an image, are called **single-molecule localization microscopy** (SMLM; photoactivated localization microscopy, PALM, with fluorescent proteins; stochastic optical reconstruction microscopy, STORM, with dyes).

**Formula 2.4.1 (Localization Precision)** A single fluorophore whose image is a Gaussian of standard deviation $s$ (about $100\,\mathrm{nm}$), from which $N$ photons are collected, can be localized with standard deviation

$$
\sigma_{\mathrm{loc}} \approx \frac{s}{\sqrt{N}}, \tag{2.3}
$$
the **standard error** of the mean position of $N$ photons. Pixelation and background add terms: $\sigma_{\mathrm{loc}}^2 = (s^2 + a^2/12)/N + 8\pi s^4b^2/(a^2N^2)$ for pixel size $a$ and background $b$ photons per pixel (Thompson, Larson and Webb, 2002).

With $N = 1000$ photons, $\sigma_{\mathrm{loc}} \approx 3\,\mathrm{nm}$; in practice drift, background and the label offset limit the resolution to $10$–$30\,\mathrm{nm}$. The method was developed independently in 2006 by Eric Betzig and Harald Hess (PALM), Xiaowei Zhuang (STORM) and Samuel Hess (fPALM); Betzig, Stefan Hell (STED) and William Moerner (single-molecule detection) shared the Nobel Prize in Chemistry 2014.

![Single-molecule localization, simulated. Ground truth: fluorophores on two parallel filaments 80 nm apart and on a ring of radius 60 nm. A: the widefield image, each emitter blurred by a point spread function of standard deviation 100 nm; the two filaments merge into one band and the ring into a spot. B: the image rebuilt from 20 localizations per fluorophore, each with precision s/√N for a random photon number N (mean about 1700); both filaments and the ring are resolved. C: intensity profiles across the filaments; only the localization image separates the two peaks at ±40 nm](./plots/smlm.py)

## 2.5. Probes for Living Cells

### 2.5.1. Fluorescent Proteins

The **green fluorescent protein** of the jellyfish *Aequorea victoria* forms its chromophore autocatalytically from three of its own residues, so that the gene alone suffices to make a cell fluorescent; its structure, chromophore chemistry and color variants are treated in [6.4.10](/6.4.10#sec-10.5) and its use in signaling research in [7.1.15](/7.1.15#sec-15.7.1). Since Martin Chalfie expressed GFP in *E. coli* and *C. elegans* in 1994, fluorescent proteins have become the basic tool of live-cell imaging, used in four ways.

| Use | Construct | Shows |
|---|---|---|
| Fusion tag | Fluorescent protein fused in frame to the protein of interest | Location and movement of that protein (in the slides of the course: spliceosomal components moving in the nucleus, receptors at the cell surface) |
| Reporter gene | Fluorescent protein coding sequence under a promoter of interest | When and in which cells the promoter is active |
| Photoactivatable or photoconvertible protein | PA-GFP (dark to green), Dendra2 or mEos (green to red) | Fate of a pulse-labeled population: optical pulse–chase |
| Sensor | Fluorescent protein whose emission depends on a ligand or on FRET | Concentrations and enzyme activities (2.5.2, 2.5.3) |

A fusion is a new protein. A tag of $27\,\mathrm{kDa}$ can disturb folding, targeting signals at the end to which it is fused (an N-terminal signal sequence, a C-terminal ER retention signal), interactions and function, and overexpression from a strong promoter can mislocalize a protein that is normally scarce. The fusion should therefore be shown to complement a loss-of-function mutant, and ideally be expressed from the endogenous locus by genome editing ([7.2.24](/7.2.24)). Fluorescent proteins mature (fold and form the chromophore, which needs $\ce{O2}$) over minutes to an hour, which sets a lower bound on the time resolution of reporter assays. Self-labeling tags (HaloTag, SNAP-tag) react covalently with cell-permeable synthetic dyes that are brighter and more photostable than fluorescent proteins.

### 2.5.2. Calcium Indicators

$\ce{Ca^2+}$ is the most widely imaged second messenger: free cytosolic $\ce{Ca^2+}$ is about $100\,\mathrm{nM}$ at rest and rises transiently to $0.5$–$2\,\mu\mathrm{M}$ on stimulation, whereas the lumen of the ER contains several hundred micromolar ([7.3.7](/7.3.7), [7.3.18](/7.3.18)). Three generations of indicators have been used.

- Aequorin, the photoprotein of the same jellyfish, emits blue light when it binds $\ce{Ca^2+}$ (Osamu Shimomura, 1962), without excitation light and hence without background or bleaching. Its light output rises steeply with $[\ce{Ca^2+}]$ (it has three binding sites), but each molecule flashes only once and the signal is weak, so it is used mainly in populations of cells.
- Synthetic dyes based on the chelator BAPTA (Roger Tsien), of which fura-2 is ratiometric (its excitation spectrum shifts on binding $\ce{Ca^2+}$, and the ratio of the emissions excited at $340$ and $380\,\mathrm{nm}$ gives $[\ce{Ca^2+}]$ independently of the dye concentration through the Grynkiewicz equation, [6.4.10](/6.4.10#sec-10.4.4)) and Fluo-4 increases in brightness about a hundredfold.
- Genetically encoded indicators, which can be targeted to cell types and organelles.

**Definition 2.5.1** A protein sensor of $\ce{Ca^2+}$ encoded by a gene, which changes its fluorescence when it binds $\ce{Ca^2+}$, is called a **genetically encoded calcium indicator** (GECI). In the GCaMP family a circularly permuted GFP is fused to calmodulin and the calmodulin-binding M13 peptide of myosin light-chain kinase; $\ce{Ca^2+}$-bound calmodulin wraps around the peptide and changes the protonation of the chromophore, increasing its fluorescence many times. The cameleons (2.5.3) report $\ce{Ca^2+}$ by FRET.

Each indicator responds over a limited range. For binding of $\ce{Ca^2+}$ with dissociation constant $K_{\mathrm{d}}$ and Hill coefficient $n$, the fraction of indicator bound is

$$
f = \frac{[\ce{Ca^2+}]^n}{K_{\mathrm{d}}^n + [\ce{Ca^2+}]^n}, \tag{2.4}
$$
which changes appreciably only between about $0.1K_{\mathrm{d}}$ and $10K_{\mathrm{d}}$ for $n = 1$. An indicator must be chosen whose $K_{\mathrm{d}}$ lies in the range to be measured: a high-affinity dye for cytosolic transients, a low-affinity one for the ER lumen.

![Fraction of indicator bound against free [Ca²⁺] (Eq. 2.4) for representative indicators with approximate in vitro constants: fura-2 and Fluo-4 (K_d 0.2–0.4 µM, n = 1), GCaMP6s and GCaMP6f (cooperative, n ≈ 2–3), the low-affinity dye Mag-Fluo-4 (22 µM) and the ER-targeted sensor G-CEPIA1er (670 µM). Shaded: resting cytosol, cytosolic transients and the ER lumen. A probe reports changes only where its curve is steep; cooperativity sharpens the response but makes the signal a nonlinear function of concentration](./plots/calcium-indicators.py)

Every indicator is also a $\ce{Ca^2+}$ buffer. Cytosol binds about 99% of the $\ce{Ca^2+}$ that enters it to endogenous buffers; adding tens of micromolar of a high-affinity dye adds substantially to this buffering, slowing and blunting the transient it is meant to measure. The indicator concentration must therefore be kept low, and kinetic measurements should be checked at different indicator loadings.

### 2.5.3. Biosensors and Optogenetics

**Förster resonance energy transfer** ([6.4.10](/6.4.10#sec-10.3.4)) between two fluorescent proteins in one molecule converts a conformational change into a change in the ratio of acceptor to donor emission; such biosensors report cAMP, $\ce{Ca^2+}$ (the cameleons, Miyawaki and Tsien, 1997), the activity of protein kinases (AKAR for PKA) and the activation of small GTPases in single living cells with subcellular resolution. Their design is described in [7.1.15](/7.1.15#sec-15.7.2); their main lesson for cell biology is spatial: the same messenger can be high in one part of the cell and low in another ([7.3.18](/7.3.18)).

Light can also be used to act on cells rather than to observe them. Microbial opsins such as channelrhodopsin-2, a light-gated cation channel, depolarize neurons that express them within milliseconds of illumination (Boyden, Deisseroth and colleagues, 2005); this is *optogenetics*. Light-induced dimerizers (the plant photoreceptor CRY2 with its partner CIB1, or the engineered iLID system) recruit a protein to a membrane or to an organelle wherever light is shone, which activates a signaling protein in one part of a cell or moves organelles at will. Such perturbations are reversible within seconds and confined to a chosen region, unlike genetic perturbations ([7.3.3](/7.3.3)).

## 2.6. Quantitative Live-Cell Imaging

### 2.6.1. FRAP

In **fluorescence recovery after photobleaching** (FRAP, [7.1.13](/7.1.13#def-13.2.2)) a region is bleached with an intense laser pulse and the return of fluorescence is followed. For a uniformly bleached circle of radius $w$ in a two-dimensional membrane, the recovery of the mobile molecules follows the Soumpasis function with characteristic time $\tau_D = w^2/4D$ ([Formula 13.2.1](/7.1.13#fml-13.2.1)); half of the mobile fluorescence returns at $t \approx \tau_D$. Writing $F_{\mathrm{pre}} = 1$ for the prebleach intensity and $F_0$ for the intensity just after bleaching, the measured curve is

$$
F(t) = F_0 + M(1 - F_0)\,\mathrm{e}^{-2\tau_D/t}\left[I_0\!\left(\frac{2\tau_D}{t}\right) + I_1\!\left(\frac{2\tau_D}{t}\right)\right], \tag{2.5}
$$
and a least-squares fit returns $D$ and the mobile fraction $M = (F_\infty - F_0)/(1 - F_0)$.

**Example 2.6.1** In a FRAP experiment on a membrane protein with a bleach spot of radius $1\,\mu\mathrm{m}$, half recovery is reached at $2.5\,\mathrm{s}$ and the fluorescence recovers to $60\%$ of its prebleach value from $15\%$ just after bleaching. Then $D \approx w^2/(4t_{1/2}) = 1/(4\times2.5) = 0.1\,\mu\mathrm{m^2\,s^{-1}}$ and $M = (0.60 - 0.15)/(1 - 0.15) \approx 0.53$: about half of the molecules are immobile on the time scale of the experiment, bound to the cytoskeleton or to large complexes.

Equation (2.5) assumes free diffusion of a single species, a bleach that is instantaneous compared with recovery, and a reservoir that is large compared with the spot. When recovery is limited by binding rather than diffusion, its rate reflects the dissociation rate constant of the bound molecules, not $D$ (for example for transcription factors exchanging on chromatin); the two regimes are distinguished by varying the spot size, since only diffusion-limited recovery depends on $w$.

### 2.6.2. FLIP and Photoactivation

**Definition 2.6.1** The method in which one region of a cell is bleached repeatedly while the loss of fluorescence elsewhere is recorded, so that all regions whose molecules exchange with the bleached region lose fluorescence and unconnected regions do not, is called **fluorescence loss in photobleaching** (FLIP).

FLIP asks a question of connectivity: whether the lumen of the ER is continuous throughout the cell (it is), whether a protein shuttles between nucleus and cytoplasm, whether two mitochondria share their matrix. Photoactivation and photoconversion (2.5.1) ask the complementary question of where molecules from one region go.

![FRAP and FLIP, simulated. A: recovery curves for a bleach spot of radius 1 µm for a fast, mostly mobile protein (D = 1 µm² s⁻¹, M = 0.9) and a slow protein with a large immobile fraction (D = 0.1 µm² s⁻¹, M = 0.6), with 2% noise; least-squares fits of Eq. (2.5) recover both parameters. The rate of recovery gives D; the plateau separates mobile and immobile molecules. B: FLIP in a two-compartment model: a spot holding 10% of a connected volume is bleached every 2 s (90% loss per pulse) and exchanges with the rest at 0.2 s⁻¹; the connected region loses its fluorescence step by step, while a region that does not exchange keeps it](./plots/frap-flip.py)

### 2.6.3. FRET in Cells

The FRET efficiency $E$ between a donor and an acceptor ([Eq. (10.5) of 6.4.10](/6.4.10#eq-10.5)) can be measured in cells in two ways that do not depend on the concentrations of the two labels. In acceptor photobleaching, the acceptor is destroyed and the donor emission rises from $F_{\mathrm{DA}}$ to $F_{\mathrm{D}}$, so $E = 1 - F_{\mathrm{DA}}/F_{\mathrm{D}}$. In fluorescence lifetime imaging (FLIM), the **fluorescence lifetime** of the donor is measured in each pixel; transfer shortens it, $E = 1 - \tau_{\mathrm{DA}}/\tau_{\mathrm{D}}$, and the lifetime is independent of the amount of donor. A positive FRET signal shows that two proteins are within about $10\,\mathrm{nm}$, which is consistent with, but does not prove, direct binding; the absence of FRET does not exclude binding if the fluorophores are far apart or badly oriented within the complex.

### 2.6.4. Single-Particle Tracking

Individual molecules, vesicles or viruses labeled with bright fluorophores or quantum dots can be localized frame by frame with the precision of Formula 2.4.1 and joined into trajectories. The way a trajectory spreads over time distinguishes modes of motion.

**Definition 2.6.2** For a particle at position $\boldsymbol{r}(t)$, the average $\mathrm{MSD}(\tau) = \langle \lvert \boldsymbol{r}(t + \tau) - \boldsymbol{r}(t)\rvert^2\rangle$ over all times $t$ (and over particles) is called the **mean squared displacement** for lag time $\tau$.

In $d$ dimensions, free diffusion gives $\mathrm{MSD} = 2dD\tau$ (the **Brownian motion** of [6.3.21](/6.3.21#sec-21.3.1)), directed transport at speed $v$ with diffusion gives $2dD\tau + v^2\tau^2$, and diffusion confined to a region of size $L$ gives an MSD that levels off at a value of order $L^2$. Anomalous diffusion, $\mathrm{MSD} \propto \tau^\alpha$ with $\alpha < 1$, arises in crowded or obstructed media. Localization error adds a constant $2d\sigma_{\mathrm{loc}}^2$. Single-particle tracking showed that membrane proteins hop between compartments of $30$–$250\,\mathrm{nm}$ bounded by the cortical cytoskeleton ([7.3.4](/7.3.4)) and that motor-driven cargoes alternate between runs and pauses ([7.3.14](/7.3.14)).

![Single-particle tracking, simulated with a frame interval of 50 ms and a localization error of 20 nm. A: trajectories of 10 s for free diffusion (D = 0.1 µm² s⁻¹), diffusion confined to a 0.4 µm corral, and directed motion at 0.5 µm s⁻¹. B: their mean squared displacement against lag time on logarithmic axes, with the theoretical curves (dashed): slope 1 for diffusion, a plateau of L²/3 for confinement, slope approaching 2 for transport. For a single trajectory the estimate becomes noisy at lags beyond about a tenth of its length, where few independent displacements are averaged](./plots/single-particle-tracking.py)

A related method, fluorescence correlation spectroscopy (FCS), records the fluctuations of fluorescence from a confocal volume of about $0.2\,\mathrm{fL}$ as molecules diffuse in and out. The autocorrelation of the signal decays with the diffusion time through the volume, which gives $D$, and its amplitude is $1/\langle N\rangle$, which gives the absolute number of molecules in the volume and hence the concentration in living cells.

## Summary

| Topic | Key points |
|---|---|
| Resolution (Definitions 2.1.1–2.1.2) | Objective forms an inverted real image, eyepiece a virtual one; immersion media (water 1.33, glycerol 1.47, oil 1.515) raise NA to about 1.4–1.6; $d_{xy} = 0.61\lambda/\mathrm{NA}$, $d_z \approx 2n\lambda/\mathrm{NA}^2$ (Formula 2.1.1): about $230$ and $800\,\mathrm{nm}$ for green light at NA 1.4 (Example 2.1.1); detection is not resolution; Nyquist sampling; photon budget and phototoxicity |
| Stains and cytochemistry | Fixation by precipitation or cross-linking; Feulgen (DNA), PAS (polysaccharides), Gomori metal precipitation (phosphatases), peroxidase with DAB, Sudan dyes (lipids), methyl green–pyronin (DNA, RNA), vital stains (Janus green B, neutral red) |
| Contrast without stains | Phase contrast (Definition 2.2.1) converts optical path into brightness; DIC (Definition 2.2.2) shows its gradient with shallow depth of field; dark field shows sub-resolution scatterers; polarized light shows birefringent order (spindle); inverted microscopes for cultured cells |
| Fluorescence (Definitions 2.3.1–2.3.2) | Chemical specificity; direct and indirect immunofluorescence on fixed, permeabilized cells; antibody validation; in situ hybridization and FISH for DNA and RNA |
| Optical sectioning | Deconvolution; confocal pinhole; two-photon excitation ∝ $I^2$ confined to the focus; light sheet (Definition 2.3.3) excites only the imaged plane; TIRF (Definition 2.3.4) excites about $100\,\mathrm{nm}$ at the coverslip (Eq. 2.2) |
| Super-resolution | SIM ($100\,\mathrm{nm}$), STED ($20$–$50\,\mathrm{nm}$), SMLM (Definition 2.4.1; $\sigma_{\mathrm{loc}} \approx s/\sqrt{N}$, Formula 2.4.1), MINFLUX, expansion; limits from label size and density |
| Probes | Fluorescent proteins as tags, reporters, photoactivatable labels and sensors (tags can perturb; maturation time); aequorin, fura-2, Fluo-4, GECIs (Definition 2.5.1); choose $K_{\mathrm{d}}$ to match the range (Eq. 2.4); indicators buffer $\ce{Ca^2+}$; FRET biosensors; optogenetics |
| Quantitative imaging | FRAP: $\tau_D = w^2/4D$, mobile fraction from the plateau (Eq. 2.5, Example 2.6.1); FLIP (Definition 2.6.1) tests connectivity; FRET by acceptor bleaching or FLIM; MSD (Definition 2.6.2) separates diffusion, confinement and transport; FCS gives $D$ and absolute concentration |

## Questions

1. A cell biologist wants to resolve two kinetochores $300\,\mathrm{nm}$ apart, labeled with a red dye emitting at $650\,\mathrm{nm}$. Can she do so with a $60\times$ water-immersion objective of NA 1.2? With a $40\times$ dry objective of NA 0.75? What camera pixel size (in the camera plane) is needed with the first objective?

   **Answer** By Eq. (2.1), $d_{xy} = 0.61\times650/1.2 \approx 330\,\mathrm{nm}$ for the water objective and $0.61\times650/0.75 \approx 530\,\mathrm{nm}$ for the dry one; the kinetochores are not resolved with either, though with NA 1.2 they are close to the limit. A shorter-wavelength dye (green, $520\,\mathrm{nm}$: $d \approx 260\,\mathrm{nm}$) and an oil objective of NA 1.4 ($d \approx 230\,\mathrm{nm}$) would resolve them. To sample $330\,\mathrm{nm}$ by Nyquist the specimen pixel must be at most about $150\,\mathrm{nm}$, that is $60\times150\,\mathrm{nm} = 9\,\mu\mathrm{m}$ on the camera; a camera with $6.5\,\mu\mathrm{m}$ pixels suffices.

2. Why does a confocal microscope reduce photobleaching of the imaged plane less than a light-sheet microscope when a three-dimensional stack is recorded?

   **Answer** In a confocal microscope the excitation beam passes through the whole depth of the specimen in the double cone above and below the focus; the pinhole rejects the emission from these regions but they are still excited and bleached. Recording a stack of $n$ planes therefore exposes every plane about $n$ times. In a light-sheet microscope only the plane being imaged is illuminated, so each plane is exposed once per stack. This is why light-sheet microscopy can follow whole embryos for days.

3. In a STORM experiment a dye yields on average $3000$ photons per switching cycle, and the point spread function has $s = 110\,\mathrm{nm}$. What is the localization precision? Why is the resolution of the final image usually two to three times worse than this number?

   **Answer** $\sigma_{\mathrm{loc}} \approx 110/\sqrt{3000} \approx 2\,\mathrm{nm}$ by Formula 2.4.1 (background and pixelation raise it to perhaps $3$–$5\,\mathrm{nm}$). The resolution of the image is worse because the full width at half maximum of the localization distribution is about $2.35\sigma_{\mathrm{loc}}$; stage drift during the minutes of acquisition adds error; the label sits $10$–$20\,\mathrm{nm}$ from its target when antibodies are used; and the structure must be labeled densely enough to satisfy the sampling theorem (2.4.1).

4. A GFP-tagged nuclear protein is studied by FRAP with bleach spots of radius $0.5$ and $1\,\mu\mathrm{m}$. In both cases half recovery occurs after about $8\,\mathrm{s}$. What can be concluded? What would you expect for free GFP?

   **Answer** For diffusion-limited recovery $t_{1/2} \approx \tau_D = w^2/4D$ would increase fourfold when $w$ doubles. A recovery time independent of spot size means that recovery is limited by binding: the protein spends most of its time bound to chromatin and exchanges with a dissociation rate $k_{\mathrm{off}} \approx \ln 2/t_{1/2} \approx 0.09\,\mathrm{s^{-1}}$ (a residence time of about $11\,\mathrm{s}$). Free GFP, with $D \approx 25\,\mu\mathrm{m^2\,s^{-1}}$, would recover in $\tau_D = 1/(4\times25) = 0.01\,\mathrm{s}$ for a $1\,\mu\mathrm{m}$ spot, faster than most bleach pulses, so it would appear never to have been bleached.

5. Vesicles in a neuronal process are tracked at $20$ frames per second. One vesicle has an MSD of $0.02\,\mu\mathrm{m}^2$ at $\tau = 0.1\,\mathrm{s}$ and $0.8\,\mu\mathrm{m}^2$ at $\tau = 1\,\mathrm{s}$. Is it diffusing or being transported? Estimate its speed, treating the motion as one-dimensional along the process.

   **Answer** Between $\tau = 0.1$ and $1\,\mathrm{s}$ the MSD increases fortyfold for a tenfold increase in $\tau$, an exponent of $\log 40 \approx 1.6$, between diffusion (1) and pure transport (2); transport dominates at long times. Fitting $\mathrm{MSD} = 2D\tau + v^2\tau^2$ to both points: $0.02 = 0.2D + 0.01v^2$ and $0.8 = 2D + v^2$. Subtracting ten times the first equation from the second gives $0.6 = 0.9v^2$, so $v \approx 0.8\,\mu\mathrm{m\,s^{-1}}$ and $D \approx 0.07\,\mu\mathrm{m^2\,s^{-1}}$, a speed typical of kinesin-driven transport ([7.3.14](/7.3.14)).
