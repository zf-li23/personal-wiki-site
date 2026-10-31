---
title: "Cryo-Electron Microscopy: Image Formation and Three-Dimensional Reconstruction"
description: The physics and computation of cryo-electron microscopy. Relativistic electron wavelength and the interaction constant; the transmission electron microscope and Abbe's theory of image formation; mass-thickness, diffraction and phase contrast; elastic and inelastic scattering, radiation damage, critical exposure and vitreous ice; the weak-phase-object approximation, defocus and spherical aberration, the contrast transfer function with amplitude contrast and envelopes, Thon rings, CTF estimation, phase flipping and Wiener filtering, phase plates; direct electron detectors, DQE, motion correction and dose weighting; the projection-slice theorem, the Radon transform, filtered back-projection and the Crowther criterion; single-particle analysis, Euler angles, cross-correlation, averaging and reference bias, 2D classification; maximum-likelihood and Bayesian refinement with the EM algorithm, 3D classification and continuous heterogeneity; Fourier shell correlation, the 0.143 criterion and the Rosenthal-Henderson plot; symmetry and helical reconstruction; cryo-electron tomography, the missing wedge and subtomogram averaging; 2D crystals and MicroED; scanning electron microscopy and volume EM; the resolution revolution.
---

Of the three methods that determine the structures of biological macromolecules at atomic resolution, electron cryo-microscopy is the youngest and the one that changed fastest. Until about 2012 it produced maps in which proteins appeared as blobs a nanometer or two across; since then it has produced atomic models of membrane proteins, of molecular machines of several megadaltons, of complexes that exist in many conformations at once, and, by tomography, of molecules inside cells. This chapter explains why it works and why it was hard. **Cryo-electron microscopy** was introduced in [7.1.6](/7.1.6#sec-6.6.3), and the electron microscope as an instrument of cell biology in [7.3.3](/7.3.3#sec-3.1); here we follow the electron from the gun through the specimen and the lenses to the detector, and then follow the images through the computer to a three-dimensional map.

The story has two halves. The first is image formation (14.1–14.5). Electrons are used because their wavelength is a few picometers (14.1), and a transmission microscope forms an image as a lens forms a Fourier transform and transforms back (14.2). A biological specimen is almost transparent to electrons and is destroyed by them: the contrast is weak, the usable exposure is small, and the specimen must be kept hydrated in vacuum as vitreous ice (14.3). The image of such a weak phase object is produced by the aberrations of the lens, and its relation to the object is described by the contrast transfer function, the central formula of the chapter (14.4). Detectors that count individual electrons and record movies made high-resolution imaging possible (14.5). The second half is reconstruction (14.6–14.12). The projection–slice theorem connects two-dimensional images to the three-dimensional Fourier transform of the object (14.6). Single-particle analysis must find the unknown orientation of every particle in an image whose signal-to-noise ratio is far below one (14.7); this is a statistical inference problem, solved by maximum likelihood and Bayesian methods (14.8). Resolution is measured by the Fourier shell correlation (14.9). Symmetric and helical particles (14.10), tomography of cells (14.11) and electron diffraction of crystals (14.12) are the other branches; the scanning electron microscope is mentioned briefly (14.13), and the chapter ends with the place of cryo-EM among structural methods (14.14).

The mathematics is that of Fourier optics. The **Fourier transform** and the **convolution theorem** come from [2.5.6](/2.5.6); diffraction as a Fourier transform from [5.4.2](/5.4.2) and from the scattering of [7.6.9](/7.6.9), where the amplitude scattered by a particle was shown to be the Fourier transform of its density; Bragg diffraction, the Ewald sphere and the phase problem of crystals are the subject of [7.6.10](/7.6.10). The statistics of 14.7–14.8 use the **maximum likelihood estimation**, **Bayesian inference** and **EM algorithm** of [3.2](/3.2) and [3.4](/3.4). The models obtained are refined and interpreted by the simulation methods of the next chapter ([7.6.15](/7.6.15)).

Throughout, the two-dimensional Fourier transform of an image $f(\boldsymbol{r})$ is written with the spatial frequency $\boldsymbol{k}$ (in reciprocal length, $\lvert\boldsymbol{k}\rvert = 1/d$ for a periodicity $d$):

$$
F(\boldsymbol{k}) = \mathscr{F}\{f\}(\boldsymbol{k}) = \int f(\boldsymbol{r})\,\mathrm{e}^{-2\pi\mathrm{i}\boldsymbol{k}\cdot\boldsymbol{r}}\,\mathrm{d}^2\boldsymbol{r}, \qquad f(\boldsymbol{r}) = \int F(\boldsymbol{k})\,\mathrm{e}^{2\pi\mathrm{i}\boldsymbol{k}\cdot\boldsymbol{r}}\,\mathrm{d}^2\boldsymbol{k}.
$$
This is the convention of image processing; it differs from that of [2.5.6](/2.5.6) only by the factor $2\pi$ in the exponent ($\xi = 2\pi k$), and from the crystallographic convention of [7.6.10](/7.6.10) by the sign of the exponent. Lengths are given in nanometers or, following the practice of the field, in ångström ($1\,\text{Å} = 0.1\,\mathrm{nm}$).

## 14.1. Why Electrons

### 14.1.1. Wavelength and Resolution

A microscope cannot resolve details much finer than the wavelength of its radiation: by the **Rayleigh criterion** ([5.4.2](/5.4.2)), two points are resolved if they are farther apart than $d = 0.61\lambda/\mathrm{NA}$, where the **numerical aperture** $\mathrm{NA} = n\sin\alpha$ is at most about $1.4$ ([7.3.2](/7.3.2)). With visible light ($\lambda \approx 500\,\mathrm{nm}$) the **limit of resolution** is about $200\,\mathrm{nm}$, a hundred times the size of a protein. Atomic detail needs radiation of wavelength $0.1\,\mathrm{nm}$ or shorter. X-rays have such wavelengths but cannot be focused by lenses with useful aperture (their refractive index differs from 1 by about $10^{-6}$), so X-ray structure determination records diffraction patterns and must recover the phases by other means ([7.6.10](/7.6.10)). Electrons have two properties that make them the radiation of choice for imaging: their wavelength is short, and, being charged, they are deflected by magnetic fields, so they can be focused into images.

### 14.1.2. The Relativistic Electron Wavelength

An electron accelerated from rest through a potential difference $U$ has kinetic energy $eU$. Its **de Broglie wavelength** $\lambda = h/p$ ([5.5.2](/5.5.2)) follows from the relativistic relation between energy and momentum: with $E = eU + m_0c^2$ and $E^2 = p^2c^2 + m_0^2c^4$, $p^2c^2 = (eU)^2 + 2eUm_0c^2$.

**Formula 14.1.1 (Electron Wavelength)** An electron of rest mass $m_0$ accelerated through the potential difference $U$ has the wavelength

$$
\lambda = \frac{h}{\sqrt{2m_0eU\left(1 + \dfrac{eU}{2m_0c^2}\right)}}. \tag{14.1}
$$
The factor in parentheses is the relativistic correction; with $m_0c^2 = 511\,\mathrm{keV}$ it is $1.29$ at $300\,\mathrm{kV}$.

**Example 14.1.1** At $U = 300\,\mathrm{kV}$, $eU/(2m_0c^2) = 300/1022 = 0.294$, and

$$
\lambda = \frac{6.626\times10^{-34}\,\mathrm{J\,s}}{\sqrt{2\cdot 9.109\times10^{-31}\,\mathrm{kg}\cdot 4.806\times10^{-14}\,\mathrm{J}\cdot 1.294}} = 1.97\times10^{-12}\,\mathrm{m} = 1.97\,\mathrm{pm}.
$$
The non-relativistic formula would give $2.24\,\mathrm{pm}$, $14\,\%$ too long. The electron moves at $\beta = v/c = 0.78$, and its Lorentz factor is $\gamma = 1 + eU/m_0c^2 = 1.59$.

| $U$ | $\lambda$ | $\beta$ | $\gamma$ | $\sigma$ (rad V⁻¹ nm⁻¹) |
|---|---|---|---|---|
| $80\,\mathrm{kV}$ | $4.18\,\mathrm{pm}$ | $0.50$ | $1.16$ | $0.0101$ |
| $120\,\mathrm{kV}$ | $3.35\,\mathrm{pm}$ | $0.59$ | $1.23$ | $0.0086$ |
| $200\,\mathrm{kV}$ | $2.51\,\mathrm{pm}$ | $0.70$ | $1.39$ | $0.0073$ |
| $300\,\mathrm{kV}$ | $1.97\,\mathrm{pm}$ | $0.78$ | $1.59$ | $0.0065$ |
| $1\,\mathrm{MV}$ | $0.87\,\mathrm{pm}$ | $0.94$ | $2.96$ | $0.0054$ |

The wavelength is a hundred times smaller than an atom, so diffraction does not limit the resolution of an electron microscope; its lenses, its specimen and its detector do. Most biological work uses $300\,\mathrm{kV}$; $200\,\mathrm{kV}$ instruments are common for screening and for thin specimens, and inexpensive $100\,\mathrm{kV}$ instruments have recently been shown to reach near-atomic resolution as well. Microscopes above about $1\,\mathrm{MV}$ (high-voltage microscopes) penetrate thicker specimens but are rare.

The last column of the table is the *interaction constant* $\sigma = 2\pi\gamma m_0e\lambda/h^2$, which converts the electrostatic potential of the specimen into a phase shift of the electron wave (14.4.1). It decreases with voltage: faster electrons are scattered less, which lets them pass through thicker ice but also gives less contrast per unit of potential.

![The electron as a wave. A: the de Broglie wavelength from Eq. (14.1) (solid) and its non-relativistic approximation (dashed) against accelerating voltage, with the voltages of biological microscopes marked; the dotted curve (right axis) is the speed v/c. B: the interaction constant σ, the phase shift produced by a projected potential of 1 V nm](./plots/wavelength.py)

### 14.1.3. Sources and Lenses

The electron gun determines the brightness and coherence of the beam. A heated tungsten filament (thermionic emission) is cheap but dim and has a large energy spread; a lanthanum hexaboride (LaB₆) crystal is ten times brighter; a field-emission gun (FEG), in which a sharp tungsten tip coated with zirconium oxide emits electrons under a strong electric field, is a thousand times brighter, with a small effective source and an energy spread of about $0.7\,\mathrm{eV}$ (less with cold field emission). Small source size means high **spatial coherence**, small energy spread high **temporal coherence** ([5.4.1](/5.4.1)); both are needed to transfer high spatial frequencies (14.4.4), and every high-resolution cryo-microscope has a FEG.

A magnetic lens is a coil with a soft-iron pole piece that produces a short, rotationally symmetric field. An electron passing off axis experiences the **Lorentz force** $-e\boldsymbol{v}\times\boldsymbol{B}$, which spirals it toward the axis: the field acts as a converging lens whose focal length is set by the coil current. Two properties distinguish magnetic lenses from glass. They can only converge, and by a theorem of Scherzer (1936) any static, rotationally symmetric, charge-free lens has positive spherical aberration and positive chromatic aberration, which cannot be cancelled by combining such lenses as glass lenses are combined. The aberrations of the objective lens are therefore not a defect of engineering but a law, and they are why the image must be interpreted through the contrast transfer function. (Multipole correctors, which break rotational symmetry, can cancel spherical aberration and are standard in materials science; biological cryo-EM rarely needs them, for reasons explained in 14.4.6.)

## 14.2. The Transmission Electron Microscope

### 14.2.1. The Optical Path

A **transmission electron microscope** (TEM, [7.3.3](/7.3.3)) has the same layout as a light microscope with Köhler illumination, turned upside down. From top to bottom:

| Part | Function |
|---|---|
| Electron gun and accelerator | emits electrons and accelerates them to $U$ ($80$–$300\,\mathrm{kV}$) |
| Condenser lenses (C1, C2, sometimes C3) and condenser aperture | C1 demagnifies the source; C2 (and C3) form a nearly parallel beam of chosen diameter; the aperture limits the beam divergence, improving coherence at the cost of brightness |
| Specimen stage | holds the specimen at about $-180\,^\circ\mathrm{C}$ (cryo-holder or autoloader cooled by liquid nitrogen), with cold traps (anticontaminators) around it; tilts to $\pm70^\circ$ |
| Objective lens | forms the first image and the diffraction pattern; its aberrations dominate the image |
| Objective aperture (back focal plane) | removes electrons scattered to high angle (amplitude contrast); a phase plate can sit here |
| Selected-area aperture (first image plane) | selects the area that contributes to a diffraction pattern |
| Intermediate and projector lenses | magnify the image or, refocused, the diffraction pattern onto the detector |
| Energy filter | removes inelastically scattered electrons (14.3.1) |
| Detector | fluorescent screen for viewing; film, scintillator camera or direct electron detector (14.5) |

The column is evacuated to about $10^{-5}\,\mathrm{Pa}$ (and far better near the gun), because electrons travel only millimeters in air. This is why biological specimens must be dried, stained, embedded or frozen.

### 14.2.2. Abbe's Theory of Image Formation

Ernst Abbe (1873) explained the light microscope by noting that a lens does two things at once. Let a coherent plane wave illuminate a thin object, leaving the *exit wave* $\psi(\boldsymbol{r})$ just below it. Each Fourier component $\Psi(\boldsymbol{k})\,\mathrm{e}^{2\pi\mathrm{i}\boldsymbol{k}\cdot\boldsymbol{r}}$ of $\psi$ is a plane wave leaving the object in the direction of angle $\theta \approx \lambda\lvert\boldsymbol{k}\rvert$ to the axis. An ideal lens focuses all rays that leave the object in the same direction to one point of its back focal plane, at distance $f\theta$ from the axis, whatever point of the object they came from. The amplitude in the back focal plane at position $\boldsymbol{u}$ is therefore the Fourier component of the exit wave at $\boldsymbol{k} = \boldsymbol{u}/(\lambda f)$: the back focal plane contains the **Fraunhofer diffraction** pattern of the object. The waves then travel on and interfere in the image plane, where rays from each object point meet again: the image is the inverse transform, magnified and inverted.

**Theorem 14.2.1 (Abbe's Theory of Image Formation)** For coherent illumination of a thin object by an ideal lens, the wave in the back focal plane is the Fourier transform of the exit wave,

$$
\Psi_{\mathrm{bfp}}(\boldsymbol{u}) \propto \Psi\!\left(\frac{\boldsymbol{u}}{\lambda f}\right), \qquad \Psi = \mathscr{F}\{\psi\},
$$
and the wave in the image plane is its inverse transform, $\psi_{\mathrm{img}}(\boldsymbol{r}) \propto \psi(\boldsymbol{r}/M)$ with magnification $M = -V/U$. A lens with aberrations, or any mask placed in the back focal plane, multiplies $\Psi(\boldsymbol{k})$ by a transfer function $T(\boldsymbol{k})$ before the second transform.

The last sentence is the key to everything that follows. An aperture of radius $a$ in the back focal plane passes only spatial frequencies $\lvert\boldsymbol{k}\rvert < a/(\lambda f)$; a phase plate shifts the phase of some frequencies; and the aberrations of a real lens multiply each frequency by a phase factor. By changing the strengths of the intermediate and projector lenses so that their object plane is the back focal plane rather than the image plane, the microscope displays the diffraction pattern instead of the image; this is how electron diffraction is recorded (14.12).

![The transmission electron microscope. A: the column of a cryo-TEM from the gun to the detector (schematic, not to scale), with the beam envelope (shaded) converging at the cross-overs. B: Abbe's theory: rays leaving three points of the object in the same direction (same colour) meet at a single point of the back focal plane, which therefore holds the Fourier transform Ψ(k) of the exit wave; rays from the same object point meet again in the image plane (here U = 3, f = 2, V = 6, M = −2)](./plots/tem-optics.py)

### 14.2.3. Three Kinds of Contrast

The detector records only intensity, $\lvert\psi_{\mathrm{img}}\rvert^2$. Where the image differs from the uniform intensity of the incident beam, the specimen has been "seen". Three mechanisms produce this contrast.

1. *Mass–thickness (amplitude) contrast*. Thick, dense or heavy-atom regions scatter more electrons to high angles. The objective aperture stops them, so these regions appear dark. The mechanism is incoherent (it needs no phase relation between waves) and dominates for thick specimens and for heavy-metal stains; it gives the classical images of sections and of **negative staining** ([7.3.3](/7.3.3)), at resolutions of $1$–$2\,\mathrm{nm}$.
2. *Diffraction contrast*. In a crystalline specimen, grains oriented to satisfy a Bragg condition send intensity into a diffracted beam; selecting the transmitted or a diffracted beam with the aperture makes such grains dark (bright-field image) or bright (dark-field image). This is the main contrast of materials science (dislocations, grain boundaries) and plays no role in biological imaging.
3. *Phase contrast*. A thin specimen changes the phase of the transmitted wave but hardly its amplitude. Interference between the unscattered beam and the scattered waves converts the phase changes into intensity, provided the lens or a phase plate shifts their relative phase. Phase contrast uses the unscattered beam and as many scattered beams as possible, and is the mechanism of all high-resolution imaging, including atomic images of crystals and all of biological cryo-EM.

In any real image the three coexist; which dominates depends on the specimen and the conditions. Materials science has developed further modes: scanning transmission imaging (STEM), in which a focused probe is scanned and transmitted electrons are collected by annular detectors, and *ptychography*, which records a full diffraction pattern at each probe position and computes the image; electron ptychography has reached a lateral resolution of about $20\,\mathrm{pm}$, limited by the thermal vibrations of the atoms. These are being adapted to biological specimens, but the workhorse remains phase-contrast imaging with parallel illumination.

## 14.3. Electrons and the Specimen

### 14.3.1. Elastic and Inelastic Scattering

An electron passing through matter interacts with the electrostatic potential of the nuclei and electrons. Two kinds of event matter.

- In **elastic scattering** the electron is deflected by the screened potential of a nucleus without losing energy. The scattered wave keeps a definite phase relation to the incident wave and carries the structural information. Elastic scattering cross sections grow roughly as $Z^{4/3}$, so heavy atoms scatter much more than light ones.
- In **inelastic scattering** the electron excites or ionizes the electrons of the specimen and loses energy: about $20$–$40\,\mathrm{eV}$ on average for plasmon and valence excitations, more for inner-shell ionization. The deflection is small, but the energy change spoils coherence, and the energy deposited breaks chemical bonds.

For the light elements of biological matter at $300\,\mathrm{kV}$, inelastic events are about three times as frequent as elastic ones. The **mean free path** for inelastic scattering in vitreous ice is about $300$–$400\,\mathrm{nm}$; ice thicker than this produces mostly inelastically scattered, blurred electrons. An *energy filter* (a magnetic prism that disperses electrons by energy and a slit that passes only those within about $20\,\mathrm{eV}$ of the original energy) removes them and improves contrast, especially for thick specimens and tomography. Multiple elastic scattering, which spoils the simple single-scattering picture of 14.4, is negligible in ice of $20$–$50\,\mathrm{nm}$ used for single particles but matters for thick crystals (14.12).

Compared with X-rays, electrons interact about $10^4$–$10^5$ times more strongly with matter per incident particle, which is why a few nanometers of protein produce measurable signal and why crystals far too small for X-ray diffraction diffract electrons (14.12). Per unit of useful (elastic) scattering, electrons also deposit about a thousand times less energy than X-rays of the wavelengths used in crystallography, because X-rays are mostly absorbed by the photoelectric effect (Henderson, 1995). This is the deep reason why imaging single molecules with electrons is possible at all.

### 14.3.2. Radiation Damage and the Critical Exposure

The specimen is destroyed by the beam. Each inelastic event deposits tens of electronvolts, more than enough to break covalent bonds and to create radicals that diffuse and react; hydrogen is released, and at high exposures bubbles of hydrogen gas appear in protein. Exposure is measured in electrons per unit area, usually $\mathrm{e^-}/\text{Å}^2$.

**Example 14.3.1** How large a radiation dose does a typical image impose? The stopping power of water for $300\,\mathrm{keV}$ electrons is about $2.4\,\mathrm{MeV\,cm^2\,g^{-1}}$. An exposure of $1\,\mathrm{e^-}/\text{Å}^2 = 10^{16}\,\mathrm{e^-\,cm^{-2}}$ deposits $2.4\times10^{16}\,\mathrm{MeV\,g^{-1}} = 3.8\times10^{3}\,\mathrm{J\,g^{-1}}$, an absorbed dose of $3.8\,\mathrm{MGy}$. A single-particle image of $40\,\mathrm{e^-}/\text{Å}^2$ thus delivers about $150\,\mathrm{MGy}$, some $10^7$ times the dose that kills a human and comparable to the doses that destroy protein crystals at synchrotrons in a fraction of a second.

Damage proceeds from fine to coarse: side chains, especially carboxylates of aspartate and glutamate and disulfide bonds, lose definition first, while secondary structure survives much longer. The decay of the signal with exposure has been measured as a function of spatial frequency.

**Formula 14.3.1 (Critical Exposure)** At $300\,\mathrm{kV}$ the amplitude of the image signal at spatial frequency $k$ decays with accumulated exposure $N$ as $\exp[-N/(2N_{\mathrm{e}}(k))]$, with the *critical exposure*

$$
N_{\mathrm{e}}(k) \approx 0.245\,k^{-1.665} + 2.81 \quad (\mathrm{e^-}/\text{Å}^2,\ k \text{ in } \text{Å}^{-1}) \tag{14.2}
$$
(Grant and Grigorieff, 2015). At $3\,\text{Å}$ ($k = 0.33\,\text{Å}^{-1}$), $N_{\mathrm{e}} = 4.3\,\mathrm{e^-}/\text{Å}^2$; at $10\,\text{Å}$, $14\,\mathrm{e^-}/\text{Å}^2$.

High-resolution information is therefore present only in the first few electrons per square ångström. If the whole exposure is summed with equal weight, the signal at frequency $k$ grows as $\int_0^N \mathrm{e}^{-n/2N_{\mathrm{e}}}\,\mathrm{d}n = 2N_{\mathrm{e}}(1 - \mathrm{e}^{-N/2N_{\mathrm{e}}})$ while the shot noise grows as $\sqrt{N}$, and the signal-to-noise ratio at that frequency is largest at $N \approx 2.5\,N_{\mathrm{e}}$. A total of $30$–$60\,\mathrm{e^-}/\text{Å}^2$ is a compromise between the high frequencies, which want little, and the low frequencies needed to see and align particles, which want much; exposure weighting of movie frames (14.5.2) removes most of the conflict. Cooling to liquid-nitrogen temperature does not prevent the primary bond breakage but slows the diffusion of radicals and fragments and so raises the tolerable exposure several-fold; this "cryo-protection" is the original reason for the "cryo" in cryo-EM.

![Radiation damage. A: the critical exposure of Eq. (14.2) against spatial frequency; high-resolution features fade after a few electrons per square ångström. B: the fraction of the signal amplitude remaining at four feature sizes as exposure accumulates. C: the signal-to-noise ratio at one frequency of an image summed without weighting, against exposure in units of the critical exposure; the optimum is near 2.5 Nₑ](./plots/dose.py)

### 14.3.3. Vitreous Ice

A biological specimen in the vacuum of the microscope dries and collapses unless it is fixed and stained or kept frozen. Ordinary (hexagonal) ice is useless: water expands by about $9\,\%$ on crystallizing, ice crystals pierce membranes and exclude solutes, and crystalline ice diffracts strongly. Water cooled fast enough (above about $10^5$–$10^6\,\mathrm{K\,s^{-1}}$) solidifies into an amorphous, glass-like solid, *vitreous ice*, whose molecules keep the disordered arrangement of the liquid. Jacques Dubochet and Alasdair McDowall (1981–1982) showed that a thin film of solution plunged into liquid ethane cooled by liquid nitrogen vitrifies: ethane has a high heat capacity and, unlike liquid nitrogen, does not form an insulating vapor layer (the Leidenfrost effect) around the warm specimen.

The standard procedure, *plunge freezing*, is:

1. A grid (a $3\,\mathrm{mm}$ copper or gold mesh covered by a holey carbon or gold film, holes $1$–$2\,\mu\mathrm{m}$) is made hydrophilic by glow discharge.
2. A drop of $2$–$4\,\mu\mathrm{L}$ of purified sample ($0.1$–$5\,\mathrm{mg\,mL^{-1}}$) is applied, and most of it is blotted away with filter paper, leaving films of $20$–$100\,\mathrm{nm}$ spanning the holes.
3. The grid is plunged into liquid ethane at about $-180\,^\circ\mathrm{C}$ and kept below $-140\,^\circ\mathrm{C}$ from then on, since vitreous ice converts to crystalline ice above that temperature.

The few hundred milliseconds between blotting and freezing are the weak point of the method. The thin film has an enormous surface: in that time a particle collides with the air–water interface thousands of times, and many proteins adsorb there, partially unfold or adopt a preferred orientation, which leaves directions of Fourier space unsampled (14.11.2). Remedies include detergents, continuous thin supports of graphene or graphene oxide that attract particles away from the interface, tilting the specimen during data collection, and devices that spray and freeze within milliseconds, which also allow time-resolved experiments. For cells and tissues thicker than a few micrometers, *high-pressure freezing* at $204.5\,\mathrm{MPa}$, where the freezing point of water is lowest and the formation of hexagonal ice is suppressed, vitrifies specimens up to about $200\,\mu\mathrm{m}$ thick; they must then be thinned for imaging (14.11.4).

Negative staining remains the quickest way to check a sample: protein adsorbed on a continuous carbon film is embedded in a dried layer of uranyl acetate or a tungstate, the stain outlines the particle (which appears light on dark), and images of high contrast are obtained in minutes. The price is a resolution of about $2\,\mathrm{nm}$, flattening and the risk of artefacts.

## 14.4. Phase Contrast and the Contrast Transfer Function

### 14.4.1. The Weak Phase Object

Inside matter the electron's kinetic energy is raised by the local electrostatic potential $V(\boldsymbol{r})$ (positive near nuclei), its wavelength is shortened, and its phase advances relative to a wave in vacuum. For a specimen thin enough that the electron travels in a straight line along $z$ (the *projection approximation*), the phase advance is proportional to the potential integrated along the path.

**Definition 14.4.1 (Weak-Phase-Object Approximation)** Let $\varphi(\boldsymbol{r}) = \int V(\boldsymbol{r}, z)\,\mathrm{d}z$ be the projected potential of a thin specimen at the point $\boldsymbol{r}$ of the image plane. The exit wave of a pure phase object is $\psi(\boldsymbol{r}) = \exp[\mathrm{i}\sigma\varphi(\boldsymbol{r})]$, with the interaction constant $\sigma$ of 14.1.2. If in addition $\sigma\varphi \ll 1$, the specimen is a weak phase object, and the exit wave can be linearized,

$$
\psi(\boldsymbol{r}) \approx 1 + \mathrm{i}\sigma\varphi(\boldsymbol{r}). \tag{14.3}
$$
This is the **weak-phase-object approximation**. A small amplitude loss (absorption, or electrons scattered outside the objective aperture) is included as $\psi \approx 1 + \mathrm{i}\sigma\varphi - \varepsilon\varphi$ with a small $\varepsilon$.

**Example 14.4.1** The mean inner potential of protein is about $7\,\mathrm{V}$ and that of vitreous ice about $4\,\mathrm{V}$, so a protein of thickness $5\,\mathrm{nm}$ in ice adds a projected potential of about $3\,\mathrm{V} \times 5\,\mathrm{nm} = 15\,\mathrm{V\,nm}$. At $300\,\mathrm{kV}$ ($\sigma = 0.0065\,\mathrm{rad\,V^{-1}\,nm^{-1}}$) the phase shift is $0.1\,\mathrm{rad}$. Proteins and nucleic acids in ice are weak phase objects; heavy-atom clusters and thick crystals are not.

The approximation makes image formation linear in $\varphi$, which is what allows the whole of 14.4–14.9 to be written in Fourier space. Its weakness is the projection approximation itself: a straight-line path is accurate only within the *depth of field* $D \approx d^2/(2\lambda)$ for resolution $d$, which at $300\,\mathrm{kV}$ and $d = 3\,\text{Å}$ is $9/(2\cdot0.0197)\,\text{Å} \approx 23\,\mathrm{nm}$. For particles larger than this, such as large viruses at high resolution, the curvature of the Ewald sphere ([7.6.10](/7.6.10)) must be taken into account in reconstruction.

### 14.4.2. Why a Phase Object Is Invisible, and How to See It

With an ideal lens the image wave is the exit wave, and the recorded intensity is $\lvert 1 + \mathrm{i}\sigma\varphi\rvert^2 = 1 + \sigma^2\varphi^2 \approx 1$: a pure phase object is invisible, to first order, in a perfectly focused image. The same is true of unstained cells in a light microscope. In the Fourier picture the exit wave is $\delta(\boldsymbol{k}) + \mathrm{i}\sigma\Phi(\boldsymbol{k})$, with $\Phi = \mathscr{F}\{\varphi\}$: the unscattered beam $\delta$ and the scattered waves are a quarter period out of phase, so they do not interfere constructively or destructively. If the scattered waves are multiplied by $\mathrm{i}$ (a phase shift of $\pi/2$) relative to the unscattered beam, the image wave becomes $1 - \sigma\varphi$ and the intensity $1 - 2\sigma\varphi$: now the image is proportional to the projected potential.

This is Zernike's principle of **phase-contrast microscopy** ([7.3.2](/7.3.2)), realized in light microscopy by a phase ring in the back focal plane. In the electron microscope a *phase plate* does the same. The most successful, the Volta phase plate (Danev and Baumeister, 2014), is a thin, heated carbon film in the back focal plane; the intense unscattered beam charges a small spot of it, and the resulting local potential shifts the phase of the unscattered beam relative to the scattered waves, building up to about $\pi/2$. Volta phase plates gave the first single-particle structures of proteins below $100\,\mathrm{kDa}$ and are used in tomography, but their phase shift drifts and they add some noise; laser phase plates, in which a standing light wave in the back focal plane shifts the phase of the unscattered beam, are under development. Without a phase plate, the microscope produces phase contrast in the same way as an imperfect lens does: by its aberrations.

### 14.4.3. Defocus and Spherical Aberration

A real objective lens does not bring all waves leaving a point to the same point of the image. Relative to an ideal lens, the wave diffracted to spatial frequency $\boldsymbol{k}$ (angle $\theta = \lambda k$) acquires an extra phase $\chi(k)$, the *wave aberration*. For a round lens two terms matter.

- *Defocus*. If the specimen lies at a distance $\Delta f$ from the plane that the lens images sharply onto the detector, the path of a ray at angle $\theta$ differs from that of the axial ray by $\Delta f(1 - \cos\theta) \approx \Delta f\theta^2/2$, a phase difference $2\pi/\lambda \cdot \Delta f\lambda^2k^2/2 = \pi\lambda\Delta f k^2$. The microscopist sets $\Delta f$ with the objective lens current; biological images are recorded in *underfocus* (lens slightly too strong), typically $\Delta f = 0.5$–$3\,\mu\mathrm{m}$.
- *Spherical aberration*. Rays far from the axis are focused more strongly than paraxial rays (Scherzer's theorem guarantees the sign), which adds a phase $-\frac{\pi}{2}C_{\mathrm{s}}\lambda^3k^4$, where the spherical aberration coefficient $C_{\mathrm{s}}$ is a length of a few millimeters for an objective lens ($2.7\,\mathrm{mm}$ in a common $300\,\mathrm{kV}$ design).

**Formula 14.4.1 (Wave Aberration)** With underfocus taken as positive, the phase shift imposed by the objective lens on the wave scattered to spatial frequency $k$ is

$$
\chi(k) = \pi\lambda\Delta f\,k^2 - \frac{\pi}{2}C_{\mathrm{s}}\lambda^3k^4. \tag{14.4}
$$
Astigmatism makes the defocus depend on the azimuth $\alpha$ of $\boldsymbol{k}$: $\Delta f(\alpha) = \bar{\Delta f} + \frac{1}{2}\Delta f_{\mathrm{a}}\cos 2(\alpha - \alpha_{\mathrm{a}})$, with a mean defocus, an astigmatic difference and an axis. Astigmatism is corrected with stigmators (weak quadrupole lenses) to a few tens of nanometers, and the residual is measured and corrected computationally.

**Remark 14.4.1 (Sign conventions)** The sign of $\Delta f$ is a convention. Many texts, including Chinese textbooks, write $\chi = \pi\lambda\Delta f k^2 + \frac{\pi}{2}C_{\mathrm{s}}\lambda^3k^4$ (both terms with the same sign); this is the same physics if underfocus is counted negative. Eq. (14.4), with underfocus positive, is the convention of the programs most used in single-particle analysis (CTFFIND, RELION, cryoSPARC). Whatever convention is used, the defocus term and the aberration term have opposite signs in underfocus, and for small $k$ the defocus term dominates.

### 14.4.4. The Contrast Transfer Function

Insert the aberration into Abbe's picture. The exit wave Eq. (14.3), including a small amplitude term, has the Fourier transform $\delta(\boldsymbol{k}) + (\mathrm{i}\sigma - \varepsilon)\Phi(\boldsymbol{k})$. The lens multiplies each scattered component by $\mathrm{e}^{\mathrm{i}\chi(k)}$ (the unscattered beam, at $k = 0$, is unchanged); in the sign convention of Eq. (14.4), this is the factor by which an underfocused lens advances the phase of a wave scattered at angle $\lambda k$. The image wave is

$$
\psi_{\mathrm{img}}(\boldsymbol{r}) = 1 + \mathscr{F}^{-1}\!\left\{(\mathrm{i}\sigma - \varepsilon)\Phi(\boldsymbol{k})\,\mathrm{e}^{\mathrm{i}\chi(k)}\right\}.
$$
Since $\varphi$ is real, $\Phi(-\boldsymbol{k}) = \Phi(\boldsymbol{k})^*$, and since $\chi$ depends only on $k = \lvert\boldsymbol{k}\rvert$, $\mathscr{F}^{-1}\{\Phi\cos\chi\}$ and $\mathscr{F}^{-1}\{\Phi\sin\chi\}$ are real functions. Expanding $(\mathrm{i}\sigma - \varepsilon)(\cos\chi + \mathrm{i}\sin\chi)$, the real part of the image wave's correction is $\mathscr{F}^{-1}\{(-\sigma\sin\chi - \varepsilon\cos\chi)\Phi\}$, and to first order in $\varphi$ the intensity is $\lvert\psi_{\mathrm{img}}\rvert^2 \approx 1 + 2\operatorname{Re}(\psi_{\mathrm{img}} - 1)$. Writing $\sigma = \sigma'\sqrt{1 - A^2}$ and $\varepsilon = \sigma' A$ with $\sigma' = \sqrt{\sigma^2 + \varepsilon^2}$:

**Theorem 14.4.1 (Image of a Weak Phase Object)** Under the weak-phase-object approximation, the Fourier transform of the recorded image intensity is

$$
\hat I(\boldsymbol{k}) = \delta(\boldsymbol{k}) + 2\sigma'\,\Phi(\boldsymbol{k})\,\mathrm{CTF}(\boldsymbol{k}), \qquad \mathrm{CTF}(\boldsymbol{k}) = -\left[\sqrt{1 - A^2}\,\sin\chi(\boldsymbol{k}) + A\cos\chi(\boldsymbol{k})\right], \tag{14.5}
$$
where $A$ is the fraction of amplitude contrast. In real space the image is $1 + 2\sigma'\,\varphi * \mathscr{F}^{-1}\{\mathrm{CTF}\}$: the projected potential convolved with the point-spread function of the microscope.

**Definition 14.4.2 (Contrast Transfer Function)** The function $\mathrm{CTF}(\boldsymbol{k})$ of Eq. (14.5), by which each Fourier component of the projected potential is multiplied in the image, is called the **contrast transfer function**. Equivalently, $\mathrm{CTF} = -\sin(\chi + \phi_A)$ with $\phi_A = \arctan\bigl(A/\sqrt{1 - A^2}\bigr)$; for proteins in vitreous ice, $A \approx 0.07$–$0.10$.

The CTF explains the appearance of every cryo-EM image:

- At $\Delta f = 0$ and small $k$, $\chi \approx 0$ and $\mathrm{CTF} \approx -A$: only the weak amplitude contrast is transferred, and the particles are nearly invisible.
- In underfocus, $\chi > 0$ grows as $k^2$ at low frequency, $\mathrm{CTF}$ becomes strongly negative over a band of low frequencies, and particles (positive $\varphi$) appear dark on a light background. Larger defocus makes this band narrower and the contrast of large features stronger.
- At higher frequency $\chi$ passes through multiples of $\pi$, and the CTF oscillates between $-1$ and $+1$ with zeros in between. Bands of frequencies are transferred with inverted contrast, and the information at the zeros is lost. The image is not a faithful picture of the object at any scale finer than the first zero.

For a defocus that is not small, the zeros occur where $\chi(k) + \phi_A = n\pi$, approximately at $k_n \approx \sqrt{n/(\lambda\Delta f)}$ (neglecting $C_{\mathrm{s}}$ and $A$). At $300\,\mathrm{kV}$ and $\Delta f = 1.5\,\mu\mathrm{m}$, the first zero lies at $1/k_1 = \sqrt{\lambda\Delta f} = \sqrt{1.97\,\mathrm{pm}\times1.5\,\mu\mathrm{m}} = 1.7\,\mathrm{nm}$, and the oscillations become ever faster: the $n$-th zero is at $1.7\,\mathrm{nm}/\sqrt{n}$.

The CTF is not the whole story. Partial coherence and other imperfections multiply it by *envelope functions* that damp high frequencies:

- Spatial coherence. Illumination is not perfectly parallel; with a Gaussian distribution of incidence angles of width $\alpha$ (typically $0.01$–$0.05\,\mathrm{mrad}$), different angles see different aberration phases, giving $E_{\mathrm{s}}(k) = \exp\bigl[-\pi^2\alpha^2(C_{\mathrm{s}}\lambda^2k^3 - \Delta f k)^2\bigr]$. Note that it worsens with defocus.
- Temporal coherence. The energy spread of the electrons and fluctuations of the high voltage and lens current make the focus fluctuate by a spread $\delta = C_{\mathrm{c}}\sqrt{(\sigma_E/E)^2 + (\sigma_U/U)^2 + 4(\sigma_I/I)^2}$ ($C_{\mathrm{c}}$ the chromatic aberration coefficient), giving $E_{\mathrm{t}}(k) = \exp\bigl[-\frac{1}{2}\pi^2\lambda^2\delta^2k^4\bigr]$.
- *Specimen and detector*. Drift, beam-induced motion, radiation damage and the detector's response are lumped into an empirical Gaussian $\exp(-Bk^2/4)$ with a "B-factor" $B$ (the same form as the temperature factor of crystallography, [7.6.10](/7.6.10)).

The total envelope sets the *information limit* of the microscope, the highest frequency transferred above noise. For a modern FEG instrument it lies beyond $1\,\text{Å}$; in practice the specimen terms dominate.

![The contrast transfer function at 300 kV (Cs = 2.7 mm, A = 0.07) in the convention of Eq. (14.4). A: CTF at 1.0 µm underfocus multiplied by the envelopes of spatial coherence (illumination semi-angle 0.02 mrad), temporal coherence (focal spread 4 nm) and a B-factor of 50 Å² (grey band: the total envelope); the oscillations transfer alternate bands with opposite sign. B: the undamped CTF at three defoci: larger defocus gives stronger low-frequency contrast and faster oscillations. C: the lowest frequencies: in focus only the amplitude contrast −A is transferred; an ideal phase plate (phase shift π/2) transfers the lowest frequencies at full strength](./plots/ctf.py)

![Phase contrast of a weak phase object, simulated: six copies of a toy complex in random orientations (field 600 Å), maximum phase shift 0.1 rad, 300 kV. In focus the particles are nearly invisible; in underfocus they appear dark with fringes whose extent grows with defocus; an ideal phase plate gives strong contrast close to the projected potential; the last panel is the 2 µm image with the shot noise of an exposure of 25 e⁻/Å², what a real micrograph looks like](./plots/defocus-images.py)

### 14.4.5. Thon Rings and CTF Estimation

The CTF can be read off the image itself. An amorphous specimen, such as the carbon support or the ice with its embedded particles, has a projected potential whose power spectrum is smooth and roughly isotropic. By Eq. (14.5), the power spectrum of its image is $\lvert\hat I(\boldsymbol{k})\rvert^2 \approx 4\sigma'^2\lvert\Phi(\boldsymbol{k})\rvert^2\,\mathrm{CTF}(\boldsymbol{k})^2E(k)^2 + N(k)$, where $N$ is the noise spectrum. The factor $\mathrm{CTF}^2$ imprints concentric rings on the spectrum, the *Thon rings* (Friedrich Thon, 1966), whose minima are the zeros of the CTF. Astigmatism makes them elliptical; drift smears them in one direction.

CTF estimation fits a model of the spectrum to the measured one: the background $N(k)$ is subtracted, and the defocus, astigmatism, and (with phase plates) the extra phase shift are found by maximizing the correlation of $\mathrm{CTF}^2$ with the background-subtracted spectrum (programs such as CTFFIND and Gctf). The highest frequency to which the fit remains good, the "CTF fit resolution", is a first indicator of micrograph quality. In single-particle refinement the defocus of each particle, which differs by its height in the ice, is refined further (14.7.1).

![Thon rings. A: the power spectrum (log scale) of a simulated image of an amorphous weak phase object at 1.5 µm underfocus with 0.1 µm of astigmatism; the rings, slightly elliptical, are the square of the CTF. B: rotational average of the spectrum of an image without astigmatism (background subtracted) and the model CTF² × envelope²; the zeros (dotted lines) mark the defocus. The first zero lies at 17.4 Å](./plots/thon.py)

### 14.4.6. Correcting for the CTF

Because the CTF changes sign, an uncorrected image mixes contrast-inverted and normal bands of frequencies; averaging uncorrected images taken at different defoci would cancel high-resolution information. Correction proceeds at two levels.

- *Phase flipping*: multiply each Fourier component by $\operatorname{sgn}\mathrm{CTF}(\boldsymbol{k})$. This restores the correct sign everywhere but leaves the amplitudes modulated.
- *Wiener filtering*: frequencies near the zeros carry no signal, and simply dividing by the CTF would amplify noise without limit. Given images $X_j$ of the same object with transfer functions $\mathrm{CTF}_j$, the least-squares estimate of the object's transform is

$$
\hat\Phi(\boldsymbol{k}) = \frac{\sum_j \mathrm{CTF}_j(\boldsymbol{k})X_j(\boldsymbol{k})}{\sum_j \mathrm{CTF}_j(\boldsymbol{k})^2 + 1/\mathrm{SNR}(\boldsymbol{k})},
$$
a *Wiener filter*: where the summed transfer is large the data are divided by it, where it is small the estimate is suppressed toward zero. Combining images taken at different defoci fills in each other's zeros. The same structure, with a statistically estimated SNR, appears in the reconstruction step of Bayesian refinement (Eq. (14.11)).

Why not record at the defocus of best transfer, as materials scientists do? At *Scherzer defocus* $\Delta f_{\mathrm{Sch}} = 1.2\sqrt{C_{\mathrm{s}}\lambda}$ ($88\,\mathrm{nm}$ at $300\,\mathrm{kV}$, $C_{\mathrm{s}} = 2.7\,\mathrm{mm}$), the CTF stays near $-1$ over a broad band out to the first zero at about $0.25\,\mathrm{nm}$, so atomic columns in a crystal appear directly. For biological specimens this fails at the other end: near focus the lowest frequencies are hardly transferred (the CTF is $-A$ at $k \to 0$), and particles cannot be seen, picked or aligned. Large defocus buys low-frequency contrast at the price of oscillations, which computation then removes. This is also why spherical-aberration correctors bring little to biological cryo-EM: high-resolution transfer is not the limiting factor, low-frequency contrast is.

## 14.5. Recording the Image

### 14.5.1. Detectors and the DQE

Until about 2012, images were recorded on photographic film, which detects electrons directly but must be developed and scanned, or with charge-coupled-device (CCD) cameras, in which a scintillator converts each electron into a flash of light that is relayed to the sensor. In the scintillator the light spreads, so the signal of one electron is blurred over several pixels and high frequencies are lost. The performance of a detector is measured by its *detective quantum efficiency*,

$$
\mathrm{DQE}(k) = \frac{\mathrm{SNR}_{\mathrm{out}}(k)^2}{\mathrm{SNR}_{\mathrm{in}}(k)^2},
$$
the fraction of the information carried by the incident electrons (whose SNR is set by Poisson statistics) that the detector preserves at spatial frequency $k$. A perfect counting detector has $\mathrm{DQE} = 1$; scintillator cameras had $\mathrm{DQE} \approx 0.1$ at half the Nyquist frequency, worse than film.

A *direct electron detector* is a thin CMOS sensor (monolithic active pixel sensor) in which the incident electron itself creates electron–hole pairs in a sensitive layer about $10\,\mu\mathrm{m}$ thick; the sensor is thinned from the back so that electrons pass through instead of scattering back and spreading their signal. Read out fast enough (hundreds to thousands of frames per second), each frame contains so few electrons that individual impacts are separated, and each can be located and counted as one event (*counting mode*), even to sub-pixel precision (super-resolution mode). Counting removes the variability of the deposited energy (Landau noise) and gives a DQE of $0.7$–$0.9$ at low frequency and $0.4$–$0.6$ near Nyquist. The price is a low dose rate per pixel, to avoid two electrons overlapping (coincidence loss).

Sampling sets a second limit. A detector with pixels of size $p$ (referred to the specimen) samples frequencies up to the Nyquist frequency $k_{\mathrm{N}} = 1/(2p)$; resolution $d$ requires $p \le d/2$, in practice $p \approx d/3$, so a $3\,\text{Å}$ structure is recorded at about $1\,\text{Å}$ per pixel. A $4096 \times 4096$ detector then covers a field of $0.4\,\mu\mathrm{m}$, containing a few hundred particles.

### 14.5.2. Movies, Motion Correction and Exposure Weighting

Fast detectors record each exposure as a *movie* of $20$–$60$ frames. This turned out to be at least as important as the higher DQE. When the beam strikes the specimen, the ice film moves and bends by several ångström, especially at the beginning of the exposure (*beam-induced motion*), and the stage drifts. In a single long exposure this motion blurs the image beyond repair; in a movie each frame can be aligned to the others before summation (*motion correction*). Global alignment by cross-correlation corrects drift; local, patch-based alignment and per-particle trajectories ("Bayesian polishing") correct the non-uniform motion of the ice.

Movies also allow *exposure weighting*. The first frames contain the best high-resolution signal (before damage), but suffer most from motion; the last frames are damaged at high resolution but still useful at low resolution. Each frame is filtered by a frequency-dependent weight proportional to $\exp[-N_j/(2N_{\mathrm{e}}(k))]$, where $N_j$ is the exposure accumulated before frame $j$ (Formula 14.3.1), and the weights are normalized at each frequency. The sum then has the best possible SNR at every frequency, and the total exposure can be large without penalty at high resolution.

### 14.5.3. Shot Noise and the Size Limit

Even a perfect detector records Poisson shot noise. At an exposure of $30\,\mathrm{e^-}/\text{Å}^2$ and $1\,\text{Å}$ pixels, each pixel receives on average $30$ electrons with a standard deviation of $\sqrt{30} \approx 5.5$, an $18\,\%$ fluctuation, while the contrast of a protein against ice is a few percent. A single particle image therefore has a signal-to-noise ratio (variance of signal over variance of noise) of order $0.01$–$0.1$; atomic detail is present but invisible. It becomes visible only by averaging many copies, which requires knowing how to align them (14.7).

Averaging gives a size limit. To align an image, the particle must contribute enough signal to determine its orientation and position; the smaller the particle, the less signal it contains. Henderson (1995) estimated from the physics of scattering and damage that particles as small as about $40\,\mathrm{kDa}$ could in principle be aligned to give $3\,\text{Å}$ maps from about $10^4$ images with a perfect microscope and detector. Practice has approached this: structures of proteins of $40$–$60\,\mathrm{kDa}$ have been determined, and smaller ones by attaching them to larger rigid scaffolds or antibody fragments. The common statement that cryo-EM needs particles above $100\,\mathrm{kDa}$ is outdated; below about $50\,\mathrm{kDa}$ it remains difficult.

## 14.6. The Projection–Slice Theorem

### 14.6.1. Images Are Projections

Under the weak-phase-object and projection approximations, a corrected cryo-EM image is a projection of the three-dimensional Coulomb potential $V(\boldsymbol{x})$ of the specimen along the beam. All information about depth is lost in a single image. To recover the third dimension one needs images of the same structure from many directions, either by tilting one specimen (tomography, 14.11) or by imaging many identical particles in different orientations (single-particle analysis, 14.7). The mathematical link is the following theorem, which also underlies medical computed tomography (CT). It was introduced into structural biology by David DeRosier and Aaron Klug (1968), who used it to compute the first three-dimensional reconstruction from electron micrographs, of the helical tail of bacteriophage T4.

**Definition 14.6.1 (Radon Transform)** For a function $f$ on $\mathbb{R}^2$, the *Radon transform* is the set of its line integrals,

$$
(\mathcal{R}f)(\theta, s) = p_\theta(s) = \int_{-\infty}^{\infty} f(s\boldsymbol{e}_\theta + t\boldsymbol{e}_\theta^{\perp})\,\mathrm{d}t,
$$
where $\boldsymbol{e}_\theta = (\cos\theta, \sin\theta)$ and $\boldsymbol{e}_\theta^{\perp} = (-\sin\theta, \cos\theta)$; $p_\theta$ is the projection of $f$ along $\boldsymbol{e}_\theta^{\perp}$. In three dimensions, the projection of $V$ along a unit vector $\boldsymbol{n}$ is the function on the plane perpendicular to $\boldsymbol{n}$ obtained by integrating along lines parallel to $\boldsymbol{n}$.

### 14.6.2. The Theorem

**Theorem 14.6.1 (Projection–Slice Theorem)** The Fourier transform of the projection of an object along a direction $\boldsymbol{n}$ equals the central section (the slice through the origin) of the Fourier transform of the object perpendicular to $\boldsymbol{n}$. In two dimensions,

$$
\hat p_\theta(k) = \hat f(k\boldsymbol{e}_\theta), \tag{14.6}
$$
and in three dimensions, with the beam along $z$, $\hat p(k_x, k_y) = \hat V(k_x, k_y, 0)$.

**Proof** Take the beam along $z$; any other direction is reduced to this one by a rotation, which rotates $V$ and $\hat V$ alike. The projection is $p(x, y) = \int V(x, y, z)\,\mathrm{d}z$. Its two-dimensional Fourier transform is

$$
\hat p(k_x, k_y) = \iint\left[\int V(x, y, z)\,\mathrm{d}z\right]\mathrm{e}^{-2\pi\mathrm{i}(k_xx + k_yy)}\,\mathrm{d}x\,\mathrm{d}y = \iiint V(x, y, z)\,\mathrm{e}^{-2\pi\mathrm{i}(k_xx + k_yy + 0\cdot z)}\,\mathrm{d}x\,\mathrm{d}y\,\mathrm{d}z = \hat V(k_x, k_y, 0). \qquad \square
$$

The theorem says that each image measures one plane through the origin of Fourier space, and the plane is perpendicular to the viewing direction. Images from many directions fill Fourier space plane by plane; once it is filled, an inverse transform gives the structure. Two practical questions follow: how many views are needed, and how to compute the inverse from planes that sample Fourier space unevenly.

![The projection–slice theorem and reconstruction from projections. A: a two-dimensional test object and the rays of one projection (θ = 30°). B: the projection, one line of the Radon transform. C: the one-dimensional Fourier transform of the projection (line) coincides with the values of the two-dimensional transform of the object along the central line in the same direction (dots). D–F: filtered back-projection from 8, 24 and 120 equally spaced views over 180°; with too few views, high frequencies are undersampled and streaks appear](./plots/projection-slice.py)

### 14.6.3. How Many Views, and How to Invert

The central sections all pass through the origin, so they crowd together at low frequency and spread apart at high frequency. For an object of diameter $D$, the Fourier transform varies smoothly over distances of $1/D$ (its transform is "band-limited" in the sense of the sampling theorem), so the sections need to be no farther apart than $1/D$ at the highest frequency $1/d$ to be reconstructed. This gives the *Crowther criterion* (Crowther, DeRosier and Klug, 1970): for evenly distributed views around an axis,

$$
N \approx \frac{\pi D}{d}. \tag{14.7}
$$
A ribosome ($D = 25\,\mathrm{nm}$) at $d = 0.3\,\mathrm{nm}$ requires about $260$ views about each axis, a few tens of thousands of evenly spread orientations in three dimensions. Single-particle data sets contain far more images than this, because each image is noisy and many must be averaged per orientation (14.5.3).

Inversion can be done in Fourier space or real space.

- *Direct Fourier inversion*: transform each image, insert its values into the three-dimensional Fourier grid at the positions of its central section (with interpolation and with weights that correct for the uneven density of samples), and transform back. This is the method of single-particle programs; with Wiener-filter weights it is the reconstruction step of Eq. (14.11).
- *Back-projection*: "smear" each projection back through space along the direction it was recorded, and sum. Unweighted back-projection overweights low frequencies, because all sections pass through the origin; the density of sections near $\boldsymbol{k}$ falls as $1/\lvert\boldsymbol{k}\rvert$ in two dimensions. Multiplying each projection's transform by the ramp $\lvert k\rvert$ before back-projection (*filtered* or *weighted back-projection*) compensates exactly for full, even sampling. Iterative algebraic methods (SIRT and its variants) instead adjust the map repeatedly until its reprojections match the images, which handles uneven sampling and missing data more gracefully and is common in tomography.

## 14.7. Single-Particle Analysis

### 14.7.1. The Method

**Definition 14.7.1 (Single-Particle Analysis)** **Single-particle analysis** (SPA) is the determination of the three-dimensional structure of a macromolecule from many images of separate, identical copies of it embedded in random orientations in a thin film (usually vitreous ice), by estimating the orientation and position of each copy in its image and combining the images by the projection–slice theorem.

The method rests on one assumption: all particles combined into one map have the same structure, to the precision of the target resolution. Heterogeneous samples are handled by classification (14.8.4), which divides the data into subsets that satisfy the assumption. A typical project proceeds as follows.

1. *Data collection*. Automated software visits thousands of holes in the grid and records one or more movies in each: $5\,000$–$50\,000$ movies per data set, millions of particles, a few terabytes, in one or two days of microscope time.
2. *Pre-processing*. Motion correction and exposure weighting of the movies (14.5.2); CTF estimation for each micrograph (14.4.5).
3. *Particle picking*. Particles are located by matching templates, by a blob detector or, now usually, by convolutional neural networks trained on a few hundred hand-picked examples (Topaz, crYOLO). Each particle is extracted in a box about twice its diameter.
4. *Two-dimensional classification*. Particles are aligned and clustered in two dimensions (14.7.4); classes of junk (ice contamination, aggregates, edges of holes) are discarded, and the averages show views of the molecule with secondary structure visible at high resolution.
5. *Initial model*. A first three-dimensional map is computed without prior knowledge: historically by random conical tilt (pairs of tilted and untilted images of the same field, Radermacher and Frank 1987) or common lines, now by stochastic gradient descent from random starting maps (cryoSPARC) or by Bayesian methods.
6. *Three-dimensional refinement and classification*. The orientations and positions of all particles are refined against the map, and the map against the particles, iteratively (14.8); 3D classification separates conformations.
7. *Polishing and CTF refinement*. Per-particle motion, per-particle defocus, beam tilt, higher-order aberrations and the Ewald-sphere curvature are refined.
8. *Post-processing and modeling*. Resolution is estimated (14.9), the map is sharpened, an atomic model is built (by hand in programs such as Coot, or automatically by neural networks such as ModelAngelo) and refined with stereochemical restraints, and model and map are validated against each other.

### 14.7.2. Orientation Parameters

Each particle image is described by five geometric parameters: three **Euler angles** ([5.1.5](/5.1.5)) $(\alpha, \beta, \gamma)$ for the rotation of the particle relative to the map, and two in-plane translations $(\Delta x, \Delta y)$. Cryo-EM programs use the $zyz$ convention: rotate by $\alpha$ about $z$, by $\beta$ about $y$, by $\gamma$ about $z$; the rotation matrix is $R = R_z(\gamma)R_y(\beta)R_z(\alpha)$, and $(\alpha, \beta)$ fix the viewing direction while $\gamma$ is the in-plane rotation. The rotations form the group $\operatorname{SO}(3)$; sampling it uniformly is not the same as sampling the Euler angles uniformly (the density in $\beta$ must be proportional to $\sin\beta$), and programs use special grids such as HEALPix on the sphere of directions. With a defocus per particle and a class label, a data set of $10^6$ particles has some $6\times10^6$ unknowns, more than the number of voxels in a $256^3$ map that they determine.

### 14.7.3. Comparing Images

Alignment requires a measure of similarity between an experimental image $x$ and a reference projection $y$, both written as vectors of $N_{\mathrm{p}}$ pixel values. The normalized **cross-correlation** coefficient is

$$
\rho(x, y) = \frac{\sum_i (x_i - \bar x)(y_i - \bar y)}{\sqrt{\sum_i (x_i - \bar x)^2\,\sum_i (y_i - \bar y)^2}},
$$
the cosine of the angle between the two mean-subtracted vectors in $\mathbb{R}^{N_{\mathrm{p}}}$. For normalized images (zero mean, unit length), the squared Euclidean distance is $\lVert x - y\rVert^2 = 2(1 - \rho)$, so maximizing correlation and minimizing distance are the same criterion, and clustering by distance (14.7.4) is clustering by similarity. The correlation of $x$ with all translates of $y$ at once is computed by the convolution theorem as $\mathscr{F}^{-1}\{X(\boldsymbol{k})Y(\boldsymbol{k})^*\}$ with two fast Fourier transforms; the position of its maximum gives the shift. In Fourier space, similarity is often expressed by the *phase residual*, the amplitude-weighted mean of the phase difference $\Delta\phi(\boldsymbol{k})$ between $X$ and $Y$ over a band of frequencies; its cosine is the band-limited correlation. The Fourier shell correlation of 14.9 is the same quantity computed between two maps shell by shell.

### 14.7.4. Averaging, Reference Bias and Two-Dimensional Classification

If $N$ images of the same view, each with signal $s$ and independent noise of variance $\sigma_{\mathrm{n}}^2$, are aligned and averaged, the signal stays the same and the noise variance falls to $\sigma_{\mathrm{n}}^2/N$: the SNR of the average is $N$ times that of one image. With $\mathrm{SNR} = 0.05$ per image, a few tens of images give an average in which the particle is clearly seen, and thousands one in which fine details emerge.

The weakness of averaging is alignment. If images are aligned to a reference, noise that happens to resemble the reference is aligned with it, and the average reproduces the reference even if the images contain no particle at all. This "Einstein from noise" experiment (named after a demonstration in which pure noise images aligned to a portrait of Einstein averaged to that portrait; Henderson, 2013) is a reminder that a beautiful average proves nothing about the data. Safeguards are references derived from the data themselves, starting from featureless models, the independent refinement of half data sets (14.9.2) and checks that features not present in the reference appear.

![Averaging and its pitfall. Top: a toy particle at a per-pixel SNR of 0.05 (one image and averages of 10, 100 and 1000 aligned copies) and the SNR of the average, which grows in proportion to N. Bottom: 2000 images of pure noise, each shifted to its position of maximal cross-correlation with the reference and averaged: the average reproduces the reference, and its correlation with it grows with the number of noise images ("Einstein from noise")](./plots/averaging.py)

*Two-dimensional classification* sorts the particle images into groups of similar appearance (the same view of the same conformation) and averages each group, without a three-dimensional model. The images are points in a space of dimension $N_{\mathrm{p}}$ ($10^4$ or more), and classification is a clustering problem. Early methods used **principal component analysis** (multivariate statistical analysis, Frank and van Heel, 1981) to reduce the dimension, followed by hierarchical clustering or **k-means clustering** ([3.4.11](/3.4.11)) in the reduced space; reduction matters, because most of the dimensions carry only noise. Reference-free alignment must be combined with classification, since each image must be rotated and shifted to its class average; modern programs do both together by maximum likelihood (14.8), assigning each image to all classes and orientations with probabilities.

![Two-dimensional classification of a heterogeneous data set. A: projections of a toy complex in two conformations. B: 1200 aligned noisy images (per-pixel SNR 0.03) projected on their first two principal components, coloured by the true state: the clouds overlap. C: averages of the two classes found by k-means clustering of the first ten principal-component coordinates, with the number of images and the purity of each class. D: the average of all images, a blurred mixture of both states](./plots/classification.py)

## 14.8. Maximum Likelihood and Bayesian Reconstruction

### 14.8.1. The Image-Formation Model

The algorithms of 14.7 alternate between two steps: find the best orientation of each image given the current map, then reconstruct the map from the images at their best orientations. This "projection matching" works when the images are good, but at low SNR the best orientation is often wrong, and errors reinforce the reference. The statistical view treats the orientations as unknown random quantities to be integrated over rather than estimated (Sigworth, 1998; Scheres and colleagues, 2005–2012).

Write the two-dimensional Fourier transform of the $i$-th particle image, pixel by pixel, as

$$
X_i(\boldsymbol{k}) = \mathrm{CTF}_i(\boldsymbol{k})\,(\boldsymbol{P}_{\phi}V)(\boldsymbol{k}) + N_i(\boldsymbol{k}), \tag{14.8}
$$
where $V$ is the three-dimensional Fourier transform of the map, $\boldsymbol{P}_\phi$ takes the central section at orientation and shift $\phi$ (by the projection–slice theorem), and $N_i$ is noise, assumed independent and Gaussian at each frequency with a variance $\sigma^2(k)$ that depends on spatial frequency (the noise is not white: it is coloured by the CTF of the ice and by the detector). The orientation $\phi_i$ is a **latent variable**: unobserved, but needed to explain the data.

The probability of observing image $X_i$ given the map and a particular orientation is a product of Gaussians over pixels:

$$
\mathbb{P}(X_i \mid \phi, V) \propto \prod_{\boldsymbol{k}} \exp\!\left(-\frac{\lvert X_i(\boldsymbol{k}) - \mathrm{CTF}_i(\boldsymbol{k})(\boldsymbol{P}_\phi V)(\boldsymbol{k})\rvert^2}{2\sigma^2(k)}\right). \tag{14.9}
$$
Its logarithm is, up to constants, a weighted squared distance between the image and the predicted projection; when the noise is white, maximizing it is the same as maximizing the cross-correlation (14.7.3).

### 14.8.2. Marginal Likelihood and the EM Algorithm

The **likelihood function** of the map is obtained by integrating over the unknown orientation of each image with a prior $\mathbb{P}(\phi)$ (usually uniform over $\operatorname{SO}(3)$ and Gaussian in the shifts):

$$
L(V) = \prod_i \int \mathbb{P}(X_i \mid \phi, V)\,\mathbb{P}(\phi)\,\mathrm{d}\phi. \tag{14.10}
$$
Maximizing $L$ directly is impossible, but the problem has the structure for which the **EM algorithm** ([3.4.11](/3.4.11)) was designed: if the latent variables were known, the maximization would be a linear least-squares problem.

**Algorithm 14.8.1 (Expectation–Maximization Refinement)** Starting from a map $V^{(0)}$, repeat until convergence:

1. *E-step*. For every image $i$ and every orientation $\phi$ on a grid, compute the posterior probability by **Bayes' theorem**,

$$
\Gamma_{i\phi} = \frac{\mathbb{P}(X_i \mid \phi, V^{(n)})\,\mathbb{P}(\phi)}{\sum_{\phi'}\mathbb{P}(X_i \mid \phi', V^{(n)})\,\mathbb{P}(\phi')}.
$$
2. *M-step*. Reconstruct the map in Fourier space, inserting every image at every orientation with weight $\Gamma_{i\phi}$:

$$
V^{(n+1)}(\boldsymbol{k}) = \frac{\sum_i\sum_\phi \Gamma_{i\phi}\,\boldsymbol{P}_\phi^{\mathsf T}\!\left[\mathrm{CTF}_iX_i/\sigma^2\right](\boldsymbol{k})}{\sum_i\sum_\phi \Gamma_{i\phi}\,\boldsymbol{P}_\phi^{\mathsf T}\!\left[\mathrm{CTF}_i^2/\sigma^2\right](\boldsymbol{k}) + 1/\tau^2(k)}, \tag{14.11}
$$
where $\boldsymbol{P}_\phi^{\mathsf T}$ inserts a two-dimensional section into the three-dimensional grid. Update the noise spectrum $\sigma^2(k)$ from the residuals and the signal spectrum $\tau^2(k)$ from the map.

Each EM iteration cannot decrease the likelihood (or, with the term $1/\tau^2$, the posterior), so the algorithm converges, though possibly to a local optimum; good initial models and coarse-to-fine sampling of orientations matter.

Three features distinguish this from projection matching. First, each image contributes to the map at all plausible orientations, weighted by their posterior probability, rather than at a single "best" one; at high SNR the posterior becomes concentrated on one orientation and the method reduces to projection matching. Second, the noise and signal spectra are estimated from the data rather than set by the user. Third, the term $1/\tau^2(k)$ in Eq. (14.11) comes from a Gaussian **prior distribution** on the map, $\mathbb{P}(V) \propto \prod_{\boldsymbol{k}}\exp[-\lvert V(\boldsymbol{k})\rvert^2/(2\tau^2(k))]$, which expresses the expectation that the map is smooth (its power falls at high frequency). Maximizing the posterior $\mathbb{P}(V \mid X) \propto L(V)\,\mathbb{P}(V)$ rather than the likelihood (a **maximum a posteriori estimate**, implemented in the program RELION, Scheres 2012) makes Eq. (14.11) a Wiener filter (14.4.6) whose strength at each frequency is set by the data: where the signal is weak, $1/\tau^2$ dominates and the map is suppressed toward zero. This **regularization** prevents **overfitting**, the growth of noise that a user-set filter could not control, and it was, together with direct detectors, the second ingredient of the "resolution revolution".

The cost is computational: $10^6$ images, $10^5$–$10^6$ orientations and shifts per image and thousands of pixels each. Programs restrict the E-step to orientations of non-negligible probability (adaptive or branch-and-bound searches), work at low resolution first and use graphics processors, so a refinement takes hours rather than months. cryoSPARC introduced stochastic gradient descent for *ab initio* reconstruction (each step uses a random subset of images), which escapes poor local optima.

### 14.8.3. Conformational Heterogeneity

Real samples contain mixtures: complexes with and without a subunit, enzymes in several states of a cycle, flexible domains. A single map averages them and blurs the variable parts.

- *Discrete 3D classification* generalizes the model to $K$ maps $V_1, \dots, V_K$: each image has a latent class label as well as an orientation, and the E-step computes posteriors over both. This is a **Gaussian mixture model** fitted by EM; it separates distinct states present in sufficient numbers, and is the standard tool for analyzing molecular machines (for example the different states of the **spliceosome** in the cycle of splicing, [7.2.16](/7.2.16), and of the ribosome during translocation).
- *Focused classification and masked refinement* restrict the comparison to a region of the map, so that a flexible domain can be classified or refined independently of the rest; multibody refinement treats a particle as several rigid bodies moving relative to each other.
- *Continuous heterogeneity* is described by low-dimensional manifolds of structures: the variance of the map can be decomposed into principal components (3D variability analysis), and neural networks of the variational-autoencoder type (cryoDRGN, Zhong and colleagues, 2021) learn a map-generating function of a few latent coordinates, from which a whole landscape of conformations, and in favorable cases their relative free energies from their populations, can be read.

Heterogeneity is a nuisance for a single static structure but an opportunity for biophysics: a cryo-EM data set is a sample of a molecular ensemble frozen within microseconds, and the populations of states reflect their Boltzmann weights at the temperature before freezing (with caveats about cooling during vitrification).

## 14.9. Resolution

### 14.9.1. What a Resolution Means

The resolution of a cryo-EM map is the finest spatial frequency at which its Fourier components are reliable. The features visible at each resolution are characteristic:

| Resolution | Visible features |
|---|---|
| $> 20\,\text{Å}$ | overall shape, envelope of domains |
| $10$–$20\,\text{Å}$ | domains and subunits |
| $6$–$10\,\text{Å}$ | rod-like $\alpha$ helices, RNA double helices |
| $4$–$5\,\text{Å}$ | $\beta$ strands separated; pitch of helices |
| $3$–$4\,\text{Å}$ | most side chains; backbone traceable, atomic model possible |
| $2$–$3\,\text{Å}$ | carbonyl oxygens, holes in aromatic rings, water molecules and ions |
| $< 1.5\,\text{Å}$ | individual atoms as separate peaks; some hydrogen atoms near $1.2\,\text{Å}$ |

In 2020 two groups obtained maps of apoferritin, a very stable octahedral protein, at $1.2\,\text{Å}$, the first cryo-EM maps at true atomic resolution (Nakane and colleagues; Yip and colleagues).

### 14.9.2. The Fourier Shell Correlation

There is no reference structure against which to judge a new map. Instead, the data are split at random into two halves, each refined independently from the start (the *gold-standard* procedure, Henderson and colleagues 2012, Scheres and Chen 2012), and the two half-maps are compared frequency by frequency.

**Definition 14.9.1 (Fourier Shell Correlation)** For two three-dimensional maps with Fourier transforms $F_1$ and $F_2$, the **Fourier shell correlation** at spatial frequency $k$ is the correlation coefficient of their Fourier components over the shell $S_k$ of frequencies with $\lvert\boldsymbol{k}\rvert \in [k, k + \Delta k)$:

$$
\mathrm{FSC}(k) = \frac{\operatorname{Re}\sum_{\boldsymbol{k} \in S_k}F_1(\boldsymbol{k})F_2(\boldsymbol{k})^*}{\sqrt{\sum_{\boldsymbol{k} \in S_k}\lvert F_1(\boldsymbol{k})\rvert^2\,\sum_{\boldsymbol{k} \in S_k}\lvert F_2(\boldsymbol{k})\rvert^2}}. \tag{14.12}
$$
Writing $F_j = A_j\mathrm{e}^{\mathrm{i}\phi_j}$, the numerator is $\sum A_1A_2\cos(\phi_1 - \phi_2)$: FSC is the amplitude-weighted mean cosine of the phase differences, $1$ when the maps agree, near $0$ when their phases are unrelated.

The FSC curve starts near 1 at low frequency and falls toward 0 as noise takes over. Independent refinement is essential: if both halves are aligned to the same reference, their noise is aligned to it as well (14.7.4), and the FSC overestimates the resolution. Masks that are too tight produce a similar artefact, which is detected by randomizing the phases beyond a certain frequency and recomputing the FSC (Chen and colleagues, 2013).

### 14.9.3. The 0.143 Criterion

To turn the curve into a number, one needs a threshold. Its justification comes from the relation between FSC and the signal-to-noise ratio.

**Theorem 14.9.1 (FSC and Signal-to-Noise Ratio)** Let two half-maps be $F_j = S + N_j$ ($j = 1, 2$) with a common signal $S$ and independent noise $N_j$ of equal power, and let $\mathrm{SNR}(k)$ be the ratio of signal power to noise power in a half-map at frequency $k$. In the limit of many Fourier components per shell,

$$
\mathrm{FSC}(k) = \frac{\mathrm{SNR}(k)}{1 + \mathrm{SNR}(k)}. \tag{14.13}
$$
The full map $(F_1 + F_2)/2$ has twice the half-map SNR, and its correlation with the noise-free structure $S$ is

$$
C_{\mathrm{ref}}(k) = \sqrt{\frac{2\,\mathrm{FSC}(k)}{1 + \mathrm{FSC}(k)}}. \tag{14.14}
$$

**Proof** Over a shell, $\sum F_1F_2^* \approx \sum\lvert S\rvert^2$ because the cross terms average to zero, and $\sum\lvert F_j\rvert^2 \approx \sum\lvert S\rvert^2 + \sum\lvert N_j\rvert^2$. With $\mathrm{SNR} = \sum\lvert S\rvert^2/\sum\lvert N\rvert^2$, $\mathrm{FSC} = \mathrm{SNR}/(1 + \mathrm{SNR})$. The full map has signal $S$ and noise $(N_1 + N_2)/2$ of half the power, so its SNR is $2\,\mathrm{SNR}$, and its correlation with $S$ is $\sqrt{2\,\mathrm{SNR}/(1 + 2\,\mathrm{SNR})}$. Substituting $\mathrm{SNR} = \mathrm{FSC}/(1 - \mathrm{FSC})$ gives $2\,\mathrm{SNR}/(1 + 2\,\mathrm{SNR}) = 2\,\mathrm{FSC}/(1 + \mathrm{FSC})$. $\square$

In crystallography, data are conventionally regarded as useful down to the frequency where the figure of merit, the expected cosine of the phase error, is about $0.5$. Applying the same standard to the full cryo-EM map, $C_{\mathrm{ref}} = 0.5$, Eq. (14.14) gives $2\,\mathrm{FSC}/(1 + \mathrm{FSC}) = 1/4$, so $\mathrm{FSC} = 1/7 = 0.143$ (Rosenthal and Henderson, 2003). This is the origin of the *0.143 criterion*, now the standard for gold-standard half-maps. The older 0.5 criterion corresponds to a half-map SNR of 1 and is more conservative; other criteria (such as the half-bit criterion of van Heel and Schatz) take the number of Fourier components per shell into account. Any threshold is a convention: frequencies beyond it still contain some signal, and frequencies below it may be degraded in parts of the map. A single number cannot describe a map whose quality varies from a rigid core to flexible loops; *local resolution* estimates (computed in a sliding window) and directional FSCs, which reveal anisotropy from preferred orientations, complement it.

![Fourier shell correlation. A: the FSC of two simulated half-maps with a common signal decaying as exp(−Bk²/2) (B = 100 Å²) and independent noise (line) follows SNR/(1 + SNR) (dashed); the 0.5 and 0.143 thresholds give 2.89 Å and 2.53 Å. The grey curve is the correlation of the full map with the true structure, Eq. (14.14), which is 0.5 where FSC = 0.143. B: Rosenthal–Henderson plot: if each particle contributes signal decaying as exp(−Bk²/2), the number of particles needed for resolution d grows as exp(B/2d²); ln N is linear in 1/d² with slope B/2](./plots/fsc.py)

### 14.9.4. B-Factors, Sharpening and the Number of Particles

All the envelopes of 14.4.4, the errors of alignment and the residual motion damp the high frequencies of the reconstruction roughly as $\exp(-Bk^2/4)$, with an overall B-factor $B$ of typically $50$–$150\,\text{Å}^2$. The map is therefore *sharpened* by multiplying its transform by $\exp(+B_{\mathrm{sharp}}k^2/4)$ up to the FSC resolution and low-pass filtered beyond it, which restores the contrast of side chains; oversharpening amplifies noise.

The same B-factor determines how many particles a target resolution costs. If each particle contributes a signal whose power decays as $\exp(-Bk^2/2)$ and the half-map SNR is proportional to the number $N$ of particles, the 0.143 criterion is met at $k = 1/d$ when $N\,\mathrm{e}^{-B/(2d^2)}$ reaches a constant, so

$$
\ln N = \frac{B}{2d^2} + \mathrm{const}. \tag{14.15}
$$
Plotting $\ln N$ against $1/d^2$ (the *Rosenthal–Henderson plot*), from refinements with subsets of the data, gives a straight line whose slope is $B/2$, a single number that measures the quality of the whole experiment.

**Example 14.9.1** With $B = 100\,\text{Å}^2$, improving the resolution from $4\,\text{Å}$ to $3\,\text{Å}$ multiplies the required number of particles by $\exp[50(1/9 - 1/16)] = \mathrm{e}^{2.43} \approx 11$; going on to $2.5\,\text{Å}$ costs another factor $\exp[50(1/6.25 - 1/9)] \approx 11$. Halving $B$ to $50\,\text{Å}^2$ (better specimens, detectors or motion correction) makes each of these steps cost a factor $3.3$. This exponential cost is why progress in cryo-EM has come from reducing $B$, not merely from collecting more data.

## 14.10. Symmetric and Helical Particles

Many complexes are symmetric: dimers ($C_2$), rings ($C_n$), dihedral assemblies ($D_n$), the octahedral ferritin ($O$, $24$ subunits) and icosahedral virus capsids ($I$, $60$ asymmetric units). Their symmetry is a **point group** ([7.6.7](/7.6.7)), and it can be imposed during refinement: each particle image is equivalent to as many images as the order of the group, so an icosahedral virus needs sixty times fewer particles than an asymmetric particle of the same size. Icosahedral viruses were the first objects reconstructed to near-atomic resolution by single-particle methods (about $3.8\,\text{Å}$ for a reovirus capsid in 2008, before direct detectors), because of this sixty-fold gain and their large size. Imposing a symmetry that is broken in reality (a single unique vertex, a bound ligand on one subunit) blurs the asymmetric features; *symmetry expansion* followed by focused classification recovers them.

Helical assemblies (**actin filaments**, **microtubules**, flagella, amyloid fibrils, tobacco mosaic virus) have **helical symmetry** ([7.6.7](/7.6.7#sec-7.4)): a subunit repeats after a rise $\Delta z$ and a twist $\Delta\phi$. A single image of a straight filament already contains many views of the subunit at different angles about the filament axis.

**Definition 14.10.1 (Helical Reconstruction)** **Helical reconstruction** is the determination of the three-dimensional structure of a helical assembly from images of segments of filaments by exploiting its helical symmetry: in Fourier–Bessel reconstruction, from the layer lines of the Fourier transform of an image, each layer line being a sum of Bessel functions of order fixed by the helical selection rule (DeRosier and Klug, 1968; the diffraction theory is that of fiber diffraction, [7.6.10](/7.6.10)); in iterative helical real-space reconstruction (Egelman, 2000), by treating overlapping segments as single particles and imposing the helical rise and twist on the map at each cycle.

The rise and twist must be determined first, from the layer lines in the power spectrum of the filament images, and the solution is not always unique: different helical lattices can produce the same layer-line positions, and an incorrect choice can still give a plausible-looking map at moderate resolution. Agreement of the map with independent knowledge (secondary structure with the correct hand, a sensible atomic model) is the test. Amyloid fibrils of tau, $\alpha$-synuclein and amyloid-$\beta$ from patients' brains, solved by helical reconstruction since 2017, showed that each disease is associated with its own fibril structure.

## 14.11. Cryo-Electron Tomography and Subtomogram Averaging

### 14.11.1. Tilt Series

Single-particle analysis requires many identical copies, purified. Cells are not made of identical copies arranged in random orientations: each region is unique. **Cryo-electron tomography** ([7.3.3](/7.3.3#sec-3.1.5)) therefore images one specimen from many directions by tilting it in the microscope, typically from $-60^\circ$ to $+60^\circ$ in steps of $2$–$3^\circ$, recording $40$–$60$ images with known tilt angles. The total exposure the specimen can tolerate ($100$–$150\,\mathrm{e^-}/\text{Å}^2$) must be divided among all of them, so each image has a few $\mathrm{e^-}/\text{Å}^2$ and very low SNR. The order of acquisition matters: in the *dose-symmetric* scheme (Hagen and colleagues, 2017) the tilts alternate on either side of zero ($0, +3, -3, +6, -6, \dots$), so that the low-tilt images, which carry the best high-resolution information, are recorded first, before damage.

The images are aligned to each other, by gold beads ($5$–$10\,\mathrm{nm}$) added as fiducial markers or by tracking features of the specimen itself, CTF-corrected (with a defocus gradient across the tilted specimen) and combined by weighted back-projection or by iterative methods (14.6.3) into a *tomogram*, a three-dimensional image of the volume. The tilted slab becomes thicker in projection, as $t/\cos\theta$: a $200\,\mathrm{nm}$ slab is $400\,\mathrm{nm}$ thick at $60^\circ$, beyond the inelastic mean free path, which is why higher tilts are rarely useful and energy filters are standard in tomography.

### 14.11.2. The Missing Wedge

**Definition 14.11.1 (Missing Wedge)** If a specimen is tilted about one axis only up to $\pm\theta_{\max}$ with $\theta_{\max} < 90^\circ$, the central sections recorded leave unmeasured a wedge-shaped region of Fourier space of half-angle $90^\circ - \theta_{\max}$ around the direction of the beam at zero tilt: the **missing wedge**. In single-particle analysis, a strongly preferred orientation of particles leaves a similar missing cone.

The specimen holder and the growing thickness prevent tilts much beyond $60$–$70^\circ$, so about a third of Fourier space is missing for $\pm60^\circ$. The consequences are visible in real space: objects are elongated along the beam direction, by a factor of about $1.55$ for $\theta_{\max} = 60^\circ$; membranes and other structures parallel to the specimen plane (perpendicular to the beam) fade, because their Fourier transforms are concentrated along $k_z$; and ripple artefacts appear above and below dense objects. Dual-axis tilting reduces the missing wedge to a missing pyramid. The resolution of a tomogram along the tilt directions is limited, by the Crowther criterion Eq. (14.7), to $d \approx \pi D/N$: for a $D = 200\,\mathrm{nm}$ slab and $N = 61$ images, about $10\,\mathrm{nm}$. In practice tomograms of cells show membranes, cytoskeletal filaments and large complexes such as ribosomes at a resolution of a few nanometers.

![The missing wedge of tomography, in a two-dimensional section (x horizontal, z along the beam). A: Fourier-space coverage of a tilt series from −60° to +60° in 3° steps; the wedges around kz are not measured. B: a model specimen with horizontal membranes, a vertical membrane and dense particles. C: reconstruction from a full tilt range. D: reconstruction from ±60°: particles are elongated along z, the horizontal membranes vanish while the vertical one survives, and streaks appear](./plots/missing-wedge.py)

### 14.11.3. Specimen Preparation for Cells

Electrons penetrate only a few hundred nanometers of ice, but most cells are micrometers thick. Thin regions (the periphery of cultured cells, small bacteria, isolated organelles, viruses) can be imaged directly after plunge freezing. Thicker specimens are thinned by *focused-ion-beam (FIB) milling* in a scanning electron microscope with a second, ion column: a beam of gallium (or, increasingly, xenon or argon) ions at a grazing angle of $10$–$20^\circ$ ablates material above and below a chosen region, leaving a lamella $100$–$200\,\mathrm{nm}$ thick. For tissues and multicellular organisms vitrified by high-pressure freezing, a block is lifted out with a micromanipulator (cryo-lift-out) before milling. Finding a rare target inside a cell requires correlative light and electron microscopy (CLEM): fluorescence images of the frozen specimen locate the labeled structure, and the coordinates guide milling and tilt-series acquisition.

### 14.11.4. Subtomogram Averaging

A tomogram of a cell contains many copies of abundant complexes (ribosomes, proteasomes, nuclear pores, viral spikes), each at the poor resolution of the tomogram and each distorted by the missing wedge. Cutting out small subvolumes around each copy, aligning them in three dimensions and averaging, as in single-particle analysis, increases the SNR. Because the copies lie in different orientations, their missing wedges point in different directions relative to the molecule, and the average fills them in: the alignment must compare only the measured parts of Fourier space, by weighting each subtomogram with its own wedge. This is *subtomogram averaging*. Its modern form refines the alignment against the original tilt-series images rather than the reconstructed tomogram (multiparticle refinement), with per-particle defocus and deformation of the specimen.

Subtomogram averaging has determined structures of ribosomes in bacterial cells at about $3.5\,\text{Å}$, revealing the drugs bound to them and their translational states, the structures of the nuclear pore complex in situ (which is dilated in cells compared with isolated nuclei), coat proteins on viruses and membranes, and the arrangement of motor proteins in cilia. The frontier is identifying molecules that do not have characteristic shapes: template matching with a high-resolution model, made possible by accurate predicted structures (7.6.15), can locate complexes in crowded tomograms.

## 14.12. Electron Crystallography and MicroED

Before single-particle methods matured, high-resolution structures from electron microscopes came from crystals. Kenneth Taylor and Robert Glaeser (1974) showed that frozen-hydrated protein crystals diffract electrons to about $3\,\text{Å}$; Richard Henderson and Nigel Unwin (1975) obtained a three-dimensional map of bacteriorhodopsin in two-dimensional crystals of the purple membrane, showing seven transmembrane helices; and in 1990 Henderson's group built the first atomic model of a membrane protein from electron images. Two-dimensional crystals give both images (which carry the phases) and diffraction patterns (which give accurate amplitudes); the structure of **aquaporin**-0 at $1.9\,\text{Å}$ from two-dimensional crystals (Gonen and colleagues, 2005) showed lipids around the protein.

*Microcrystal electron diffraction* uses three-dimensional crystals far too small for X-ray diffraction.

**Definition 14.12.1 (Microcrystal Electron Diffraction)** **Microcrystal electron diffraction** (MicroED) is the determination of crystal structures from electron diffraction patterns of three-dimensional crystals of submicrometer size, recorded in the diffraction mode of a cryo-electron microscope while the crystal is rotated continuously, and processed with the methods of X-ray crystallography.

MicroED works because electrons interact so strongly with matter. The scattering factor of an atom for electrons is related to that for X-rays $f_{\mathrm{X}}(s)$ by the Mott–Bethe formula,

$$
f_{\mathrm{e}}(s) = \frac{m_0\mathrm{e}^2}{8\pi^2\varepsilon_0h^2}\,\frac{Z - f_{\mathrm{X}}(s)}{s^2}, \qquad s = \frac{\sin\theta}{\lambda},
$$
because electrons are scattered by the electrostatic potential of the nucleus screened by the electrons, while X-rays are scattered by the electrons alone. Electron scattering amplitudes are about $10^3$ times larger than those of X-rays in the useful range of $s$, so a crystal $0.1$–$0.5\,\mu\mathrm{m}$ thick gives measurable diffraction. Since 2013 (Shi, Nannenga, Iadanza and Gonen), MicroED has solved structures of proteins, of amyloid-forming peptides whose microcrystals never grow large, and above all of small molecules and drugs from powders in minutes. Two features differ from X-ray crystallography: the maps show the electrostatic potential, so the charge states of atoms and the positions of hydrogens are visible, and thick crystals scatter electrons more than once (dynamical diffraction), which distorts the intensities and must be minimized by thin crystals (often milled with a FIB) or modeled. The theory of diffraction by crystals, Bragg's law and the phase problem are developed in [7.6.10](/7.6.10).

## 14.13. Scanning Electron Microscopy

The **scanning electron microscope** ([7.3.3](/7.3.3)) focuses the beam to a probe of a few nanometers and scans it over the specimen surface; a single-pixel detector records, for each probe position, the electrons emitted from the surface, building the image point by point. *Secondary electrons*, ejected from the outermost few nanometers by inelastic collisions and having energies below $50\,\mathrm{eV}$, report the topography (surfaces facing the detector and edges appear bright). *Backscattered electrons*, primary electrons scattered elastically through large angles, have energies close to the beam energy and come from depths of up to hundreds of nanometers; their yield rises with atomic number, so they show the distribution of heavy-metal stains. The resolution of secondary-electron images of biological specimens is about $5$–$10\,\mathrm{nm}$. Specimens are dried by critical-point drying and coated with metal, or examined frozen.

The scanning microscope has become a tool for three-dimensional imaging of whole cells and tissues (*volume electron microscopy*). In serial block-face SEM, an ultramicrotome inside the microscope cuts the face of a resin-embedded, heavy-metal-stained block, and the freshly exposed face is imaged after each cut; in FIB-SEM, the ion beam removes layers a few nanometers thick; in array tomography, ribbons of serial sections are collected on tape or wafers and imaged later. Voxel sizes of $5$–$10\,\mathrm{nm}$ in the plane and $10$–$30\,\mathrm{nm}$ in depth over cubic millimeters have made possible the reconstruction of complete neuronal wiring diagrams (connectomes) of the larval and adult *Drosophila* brain and of a cubic millimeter of mouse cortex.

## 14.14. Cryo-EM among the Structural Methods

The development of cryo-EM spans the whole history of electron microscopy. Ernst Ruska built the first transmission electron microscope in 1931–1933 and soon found that biological specimens were burned by the beam. Negative staining and thin sectioning made electron microscopy the instrument of cell biology from the 1950s. DeRosier and Klug (1968) reconstructed a three-dimensional structure from images; Henderson and Unwin (1975) showed that unstained, low-dose images of crystals contain high-resolution information; Dubochet (1982) made vitrification practical; and Joachim Frank developed, from the 1970s, the theory and software (SPIDER) for single-particle analysis. Jacques Dubochet, Joachim Frank and Richard Henderson shared the Nobel Prize in Chemistry in 2017.

For two decades, single-particle maps rarely exceeded about $10\,\text{Å}$ except for symmetric viruses. Around 2012–2013 three advances converged: direct electron detectors with counting and movies (14.5), motion correction, and Bayesian refinement with automatically estimated filters (14.8). The structure of the **ion channel** TRPV1, the capsaicin and heat receptor, at $3.4\,\text{Å}$ without crystals (Liao, Cao, Julius and Cheng, 2013) was a landmark of this "resolution revolution". Within a few years, cryo-EM determined structures that crystallography had failed to obtain for decades: the spliceosome in many states of its cycle, the γ-secretase complex, respiratory supercomplexes, the nuclear pore complex, and the spike glycoprotein of SARS-CoV-2 within weeks of the virus's discovery in 2020. Since about 2020 more new structures of large complexes enter the **Protein Data Bank** from cryo-EM than from X-ray crystallography.

| | X-ray crystallography | NMR | Single-particle cryo-EM | Cryo-ET |
|---|---|---|---|---|
| Specimen | crystals | concentrated labeled solution | purified complex in ice, $\sim 0.1$–$1\,\mathrm{mg\,mL^{-1}}$, a few µL | cells, lamellae, organelles |
| Size | no upper limit; small proteins easiest | best below $\sim 50\,\mathrm{kDa}$ | best above $\sim 100\,\mathrm{kDa}$; possible near $40\,\mathrm{kDa}$ | complexes of $\gtrsim 300\,\mathrm{kDa}$ for averaging |
| Resolution | often $1$–$2\,\text{Å}$ | ensemble from restraints | typically $2.5$–$4\,\text{Å}$; $1.2\,\text{Å}$ at best | $1$–$3\,\mathrm{nm}$; $3$–$10\,\text{Å}$ by averaging |
| Heterogeneity | averaged in the crystal | dynamics measured | separated by classification | in situ, molecule by molecule |
| Main obstacle | crystallization | size, assignment | small, flexible or interface-sensitive particles | thickness, missing wedge, SNR |

The methods are complementary. Crystallography remains the method of choice for high-throughput structures of small proteins with ligands (drug discovery); NMR measures dynamics in solution ([7.6.13](/7.6.13)); SAXS ([7.6.9](/7.6.9)) tests models in solution; cryo-EM handles large, flexible and heterogeneous assemblies; tomography places them in the cell. Structure prediction ([7.6.15](/7.6.15)) now supplies accurate models of most single chains, and cryo-EM maps of moderate resolution are increasingly interpreted by fitting predicted models, while prediction programs in turn learned from the structures that experiments produced. Machine learning has entered every step of the cryo-EM pipeline as well: particle picking, denoising of images and tomograms, filling in the missing wedge, modeling of continuous heterogeneity and automatic model building. The physical principles of this chapter, the CTF, the projection–slice theorem, the statistics of noisy images and the limits set by radiation damage, determine what all these methods can achieve.

## Summary

| Topic | Key relation or fact | Reference |
|---|---|---|
| Electron wavelength | $\lambda = h/\sqrt{2m_0eU(1 + eU/2m_0c^2)}$; $1.97\,\mathrm{pm}$ at $300\,\mathrm{kV}$ | Formula 14.1.1, Example 14.1.1 |
| Lenses | magnetic, converging only; positive $C_{\mathrm{s}}$ and $C_{\mathrm{c}}$ (Scherzer) | 14.1.3 |
| Abbe | back focal plane = Fourier transform of exit wave; image = inverse transform; masks and aberrations multiply in Fourier space | Theorem 14.2.1 |
| Contrast | mass–thickness (stain, sections), diffraction (crystals), phase (all high-resolution imaging) | 14.2.3 |
| Specimen | inelastic events 3× elastic; $1\,\mathrm{e^-}/\text{Å}^2 \approx 4\,\mathrm{MGy}$; critical exposure $4\,\mathrm{e^-}/\text{Å}^2$ at $3\,\text{Å}$; vitreous ice by plunging into ethane | Formula 14.3.1, Example 14.3.1, 14.3.3 |
| Weak phase object | $\psi \approx 1 + \mathrm{i}\sigma\varphi$; $\sigma\varphi \approx 0.1\,\mathrm{rad}$ for protein in ice; invisible in focus | Definition 14.4.1, Example 14.4.1 |
| Aberration | $\chi = \pi\lambda\Delta f k^2 - \frac{\pi}{2}C_{\mathrm{s}}\lambda^3k^4$ (underfocus positive) | Formula 14.4.1, Remark 14.4.1 |
| CTF | $\hat I = \delta + 2\sigma'\Phi\,\mathrm{CTF}$, $\mathrm{CTF} = -[\sqrt{1 - A^2}\sin\chi + A\cos\chi]$; envelopes $E_{\mathrm{s}}, E_{\mathrm{t}}, \mathrm{e}^{-Bk^2/4}$; Thon rings; phase flipping and Wiener filter; phase plates | Theorem 14.4.1, Definition 14.4.2, 14.4.5–14.4.6 |
| Detection | DQE; counting direct detectors; movies, motion correction, exposure weighting; SNR per particle $0.01$–$0.1$ | 14.5 |
| Projection–slice | FT of a projection = central section of the 3D FT; Crowther $N \approx \pi D/d$; filtered back-projection | Theorem 14.6.1, Eq. (14.7) |
| Single particles | 5 parameters per image ($zyz$ Euler angles, shifts); cross-correlation; SNR ∝ N; reference bias; 2D classification by PCA and k-means | Definition 14.7.1, 14.7.2–14.7.4 |
| Bayesian refinement | marginal likelihood over orientations; EM with posterior weights; MAP reconstruction as a data-driven Wiener filter; mixtures for heterogeneity | Eqs. (14.8)–(14.11), Algorithm 14.8.1 |
| Resolution | FSC; $\mathrm{FSC} = \mathrm{SNR}/(1 + \mathrm{SNR})$; 0.143 from $C_{\mathrm{ref}} = 0.5$; $\ln N = B/2d^2 + \mathrm{const}$ | Definition 14.9.1, Theorem 14.9.1, Eq. (14.15) |
| Symmetry | point-group symmetry multiplies data; helical reconstruction by Fourier–Bessel or real-space methods | Definition 14.10.1 |
| Tomography | tilt series $\pm60^\circ$; missing wedge, elongation $\approx 1.55$; FIB milling; subtomogram averaging | Definition 14.11.1, 14.11.3–14.11.4 |
| MicroED | strong electron scattering (Mott–Bethe), submicrometer crystals, potential maps | Definition 14.12.1 |
| SEM | secondary and backscattered electrons; volume EM and connectomics | 14.13 |

## Questions

1. Calculate the wavelength of electrons accelerated through $200\,\mathrm{kV}$ with and without the relativistic correction, and the speed of the electrons.

   **Answer** $eU = 200\,\mathrm{keV}$, $eU/(2m_0c^2) = 200/1022 = 0.196$. Non-relativistic: $\lambda = h/\sqrt{2m_0eU} = 6.626\times10^{-34}/\sqrt{2\cdot9.109\times10^{-31}\cdot3.204\times10^{-14}} = 2.74\,\mathrm{pm}$. Relativistic: divide by $\sqrt{1.196} = 1.094$: $\lambda = 2.51\,\mathrm{pm}$. $\gamma = 1 + 200/511 = 1.391$, $\beta = \sqrt{1 - 1/\gamma^2} = 0.695$, $v = 2.08\times10^8\,\mathrm{m\,s^{-1}}$.

2. Why is a perfectly focused image of an unstained protein in ice almost featureless, and which two ways are used to obtain contrast? Why does increasing the defocus make particles easier to see but not improve the final resolution?

   **Answer** The protein shifts the phase of the electron wave by about $0.1\,\mathrm{rad}$ but hardly changes its amplitude; with an ideal lens the intensity is $\lvert 1 + \mathrm{i}\sigma\varphi\rvert^2 \approx 1$, because the scattered waves are in quadrature with the unscattered beam (only the small amplitude contrast $A$ remains). Contrast is obtained by shifting the relative phase of the scattered waves by about $\pi/2$, either with a phase plate in the back focal plane (Zernike's principle) or with the wave aberration of the lens, by defocusing. Defocus makes $\chi$ grow faster at low $k$, so the CTF reaches $-1$ at lower frequencies, enhancing the large-scale features used to see and align particles. It does not add high-resolution information: the CTF oscillates faster (more zeros), the spatial-coherence envelope $E_{\mathrm{s}}$ falls faster with defocus, and the signal is delocalized over a larger area (edge of the box). High-resolution information is recovered only by CTF correction and averaging; moderate defocus ($0.5$–$2\,\mu\mathrm{m}$) is a compromise.

3. A micrograph recorded at $300\,\mathrm{kV}$ shows Thon rings whose first minimum (zero of the CTF) lies at $1/(20\,\text{Å})$. Estimate the defocus, neglecting spherical aberration and amplitude contrast. At what spatial frequency is the fourth zero?

   **Answer** The first zero satisfies $\pi\lambda\Delta f k_1^2 = \pi$, so $\Delta f = 1/(\lambda k_1^2) = (20\,\text{Å})^2/0.0197\,\text{Å} = 2.03\times10^4\,\text{Å} = 2.0\,\mu\mathrm{m}$. Zeros at $k_n = \sqrt{n}\,k_1$ (while $C_{\mathrm{s}}$ is negligible): $k_4 = 2k_1 = 1/(10\,\text{Å})$. With amplitude contrast $A = 0.07$ the zeros shift slightly to lower $k$ (the condition becomes $\chi = n\pi - \phi_A$ with $\phi_A = 0.07\,\mathrm{rad}$), and spherical aberration matters only at higher frequencies: at $k = 0.1\,\text{Å}^{-1}$ its phase is $\frac{\pi}{2}C_{\mathrm{s}}\lambda^3k^4 = 1.57\cdot2.7\times10^7\cdot7.6\times10^{-6}\cdot10^{-4} = 0.03\,\mathrm{rad}$, negligible.

4. Prove that the Fourier shell correlation of two independent half-maps equals $\mathrm{SNR}/(1 + \mathrm{SNR})$, and derive the 0.143 threshold. Why must the two half-maps be refined independently?

   **Answer** See Theorem 14.9.1: with $F_j = S + N_j$ and independent noise, the numerator averages to the signal power and each factor of the denominator to signal plus noise power. The full map has twice the SNR; its correlation with the truth is $\sqrt{2\,\mathrm{FSC}/(1 + \mathrm{FSC})}$; setting this to $0.5$ (the crystallographic convention for useful phases) gives $\mathrm{FSC} = 1/7 = 0.143$. If the halves share a reference or orientations determined against a common map, their noise is correlated by alignment (as in the Einstein-from-noise experiment), the cross terms in the numerator no longer vanish, and the FSC overestimates the resolution; it can even rise to high values for pure noise.

5. A refinement gives the following resolutions for subsets of a data set: $20\,000$ particles, $4.0\,\text{Å}$; $80\,000$ particles, $3.3\,\text{Å}$. Estimate the B-factor of the experiment and the number of particles needed for $2.8\,\text{Å}$.

   **Answer** From Eq. (14.15), $\ln(N_2/N_1) = \frac{B}{2}(1/d_2^2 - 1/d_1^2)$: $\ln 4 = 1.386 = \frac{B}{2}(0.0918 - 0.0625) = 0.01466\,B$, so $B \approx 95\,\text{Å}^2$. For $2.8\,\text{Å}$ ($1/d^2 = 0.1276$): $\ln(N/80\,000) = 47.3\cdot(0.1276 - 0.0918) = 1.69$, $N \approx 80\,000\cdot5.4 \approx 4.3\times10^5$ particles, assuming that nothing else (heterogeneity, alignment accuracy) limits the resolution.

6. Using the projection–slice theorem, explain why a cryo-ET reconstruction from a tilt series of $\pm60^\circ$ elongates spherical particles along the beam direction and makes horizontal membranes disappear, but leaves vertical membranes visible. What fraction of Fourier space is missing?

   **Answer** Each image is a central section of the Fourier transform perpendicular to its viewing direction; tilting about $y$ from $-60^\circ$ to $+60^\circ$ fills all sections whose normals lie within $60^\circ$ of $z$, leaving unmeasured the wedge of frequencies within $30^\circ$ of the $k_z$ axis. A missing range of $60^\circ$ out of $180^\circ$ is one third of Fourier space. A sphere's transform is isotropic, so losing its high-$k_z$ components lowers the resolution along $z$ and stretches it in that direction (by about 1.55). A horizontal membrane (a thin sheet perpendicular to $z$) has a transform concentrated along the $k_z$ axis, entirely inside the wedge, so it vanishes; a vertical membrane has its transform along an axis in the $k_x$–$k_y$ plane, fully measured, so it is reconstructed. Averaging many subtomograms in different orientations fills the wedge.

7. Henderson estimated a lower size limit for single-particle cryo-EM. Explain qualitatively why smaller particles are harder, and why attaching a small protein to a large rigid scaffold or a Fab fragment helps. Why does a phase plate help?

   **Answer** Orientation and position must be determined from each image separately, and the information available for alignment is the total low-to-medium-resolution signal in the particle, which scales with its mass (number of atoms) while the noise is set by the exposure, limited by radiation damage. Below about $40\,\mathrm{kDa}$ the signal is too weak to determine orientations accurately even in principle; errors in orientation blur the average. A rigid scaffold adds mass and distinctive features that can be aligned, and the small protein rides along in a known orientation. A phase plate increases low-frequency contrast (CTF $\approx -1$ at low $k$ instead of $-A$), so the signal used for alignment is larger at the same exposure.

8. Describe the E-step and M-step of maximum-likelihood refinement, and explain why the method is more robust than assigning each particle to its best orientation. What role does the prior on the map play?

   **Answer** E-step: for each image, compute the likelihood of the image given the current map for every orientation and shift on a grid (Gaussian noise model with a frequency-dependent variance, CTF included), and normalize with the prior over orientations to obtain posterior probabilities $\Gamma_{i\phi}$. M-step: reconstruct the map by inserting each CTF-weighted image at every orientation with its posterior weight, dividing by the summed CTF² weights plus $1/\tau^2$, and re-estimate the noise and signal spectra. At low SNR, the "best" orientation is often wrong; hard assignment then imposes errors and the reference's noise on the map (reference bias), while posterior weighting spreads an uncertain image over its plausible orientations, so that its contribution is blurred rather than misplaced, and converges to the hard assignment when the data are good. The Gaussian prior on the map's Fourier components turns the M-step into a Wiener filter with a data-derived strength, suppressing frequencies where the signal is weak and preventing overfitting of noise without arbitrary user-chosen filters.

9. (Design) A membrane transporter of $90\,\mathrm{kDa}$ in detergent gives two-dimensional class averages showing only side views, and the 3D map is stretched in one direction. Diagnose the problem and propose three remedies.

   **Answer** The particles adopt a preferred orientation, probably by adsorbing to the air–water interface with the detergent micelle or a hydrophobic face; views from other directions are missing, leaving a missing cone in Fourier space (Definition 14.11.1), which stretches the map along the unsampled direction and makes the directional FSC anisotropic. Remedies: (a) collect data with the stage tilted ($30$–$40^\circ$), which converts a single view into a cone of views (CTF varies across the tilted image and must be estimated locally); (b) change the interface: add a small amount of a different detergent or fluorinated surfactant, use graphene oxide or other continuous supports, or freeze faster (spray devices) to reduce the time spent at the interface; (c) change the particle: reconstitute into nanodiscs, or bind a Fab fragment or a nanobody that both alters the surface properties and adds mass for alignment.

10. Estimate the absorbed dose in gray of a single-particle exposure of $50\,\mathrm{e^-}/\text{Å}^2$ at $300\,\mathrm{kV}$, using a stopping power of $2.4\,\mathrm{MeV\,cm^2\,g^{-1}}$, and the number of $3\,\text{Å}$ critical exposures it contains. Why can the structure nevertheless be determined at $3\,\text{Å}$?

    **Answer** $50\,\mathrm{e^-}/\text{Å}^2 = 5\times10^{17}\,\mathrm{e^-\,cm^{-2}}$; energy per mass $= 5\times10^{17}\cdot2.4\,\mathrm{MeV\,g^{-1}} = 1.2\times10^{18}\,\mathrm{MeV\,g^{-1}} = 1.9\times10^5\,\mathrm{J\,g^{-1}} = 1.9\times10^8\,\mathrm{Gy}$ ($190\,\mathrm{MGy}$). With $N_{\mathrm{e}}(3\,\text{Å}) = 4.3\,\mathrm{e^-}/\text{Å}^2$, the exposure contains about $12$ critical exposures; the $3\,\text{Å}$ amplitude has fallen to $\mathrm{e}^{-50/8.6} = 0.3\,\%$ by the end. The structure is determined because the movie records the exposure in frames: the first frames, before damage, carry the high-resolution signal, and exposure weighting uses each frame only at the frequencies at which it is still undamaged, while the later frames contribute low-frequency signal for alignment.

11. Why is helical reconstruction subject to an ambiguity that does not arise for point-group symmetric particles, and how is the correct solution recognized?

    **Answer** The helical parameters (rise and twist) are inferred from the positions of layer lines in the power spectrum of images, which are sampled at the spacings permitted by the helical lattice; several lattices (with different numbers of starts and different twists) can produce layer lines at nearly the same positions within the resolution of the data, and imposing a wrong symmetry can still converge to a self-consistent map at moderate resolution. A point group, by contrast, is a finite set of exact rotations fixed by the subunit count, and the correct group is usually evident from 2D averages. The correct helical solution is recognized by testing several candidate symmetries and checking which gives a map with features expected at that resolution: separated $\beta$ strands with the correct spacing, right-handed $\alpha$ helices, side chains that fit the sequence, and a model with good stereochemistry.

12. MicroED maps show the electrostatic potential rather than the electron density. Give one consequence for the interpretation of a map and one complication that does not arise in X-ray crystallography.

    **Answer** Consequence: the potential depends on the charge of an atom (the screening of the nucleus by its electrons), so charged groups look different from neutral ones: carboxylates (negative) appear weaker and can even vanish, and positively charged groups stronger, which reveals protonation states, and hydrogen atoms, whose contribution to the potential is relatively larger than their single electron's contribution to X-ray scattering, are more visible. Complication: because electrons interact so strongly with matter, they are scattered more than once in crystals thicker than about $100$–$200\,\mathrm{nm}$ (dynamical diffraction); the measured intensities are then not proportional to the squared structure factors, which reduces the accuracy of the model unless crystals are thinned (by FIB milling) or dynamical scattering is modeled.
