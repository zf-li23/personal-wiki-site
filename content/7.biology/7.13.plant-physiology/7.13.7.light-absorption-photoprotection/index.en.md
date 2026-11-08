---
title: Light Absorption, Energy Conversion and Photoprotection
description: Chloroplasts and photosynthetic pigments; pigment extraction, separation and spectrophotometric quantification; photosynthetically active radiation, absorption and action spectra, fluorescence and phosphorescence; the photosynthetic unit and quantum requirement, with an eigenvalue analysis of the Kok flash-oxygen oscillation; red drop and the Emerson enhancement effect, the division of labor of the two photosystems and the ATP/NADPH balance; electron-transport inhibitors and herbicides; chlorophyll fluorescence and the saturating-pulse method (Fv/Fm, ΦPSII, NPQ, ETR) and energy partitioning; the xanthophyll cycle, PsbS, state transitions, photoinhibition and the kinetics of D1 repair; chlorophyll synthesis, degradation and leaf color.
source_hash: b57772e1a6d2
---

The first step of photosynthesis turns light into usable excitation energy. Every later step can be limited by too little light, or damaged by too much. The molecular mechanism of the light reactions (charge separation in the reaction centers, the Z scheme, water splitting and photophosphorylation) is covered in [7.1.24](/7.1.24); the physics of pigments, excitation transfer and electron-transfer theory is in [7.6.18](/7.6.18); the microscopic structure of the chloroplast is in [7.12.3](/7.12.3). This chapter looks at the same machinery from the viewpoint of plant physiology: which pigments a leaf contains and how they are measured; what fraction of the absorbed photons is really used for photochemistry, and how this fraction can be read nondestructively from leaf fluorescence; how a leaf converts surplus energy into heat when light exceeds demand, and how it repairs damaged photosystem II; and how chlorophyll is synthesized and degraded, with the resulting changes in leaf color. The next chapter ([7.13.8](/7.13.8)) shows how ATP and NADPH are used to fix $\ce{CO2}$ in C3, C4 and CAM plants, and Chapter 9 ([7.13.9](/7.13.9)) places these processes in the leaf and the canopy and discusses the response of photosynthetic rate to light, $\ce{CO2}$ and temperature.

## 7.1. Chloroplasts and Photosynthetic Pigments

### 7.1.1. The Chloroplast: Site of Photosynthesis

Photosynthesis in higher plants takes place mainly in the **chloroplasts** of mesophyll cells. A palisade cell contains a few dozen chloroplasts, and there are about $5\times10^{5}$ of them per square millimeter of leaf area. The chloroplast is surrounded by a double envelope and contains the stroma and the thylakoids. Thylakoids are flattened membrane sacs whose membranes carry the photosynthetic pigments and the electron-transport complexes (hence the name photosynthetic membrane); the **Calvin cycle** runs in the stroma. The thylakoid membrane has two kinds of region: grana thylakoids, which are tightly appressed and stacked into grana, and stroma thylakoids, which run between grana and are not stacked. Stacking has two consequences. First, it partitions membrane proteins laterally: **photosystem II** and its light-harvesting complex LHCII are concentrated in the stacked regions, whereas **photosystem I** and ATP synthase lie only in the unstacked regions and at the margins of grana that the stroma can reach ([7.1.24](/7.1.24#sec-24.3.6)); this separation keeps excitation in the higher-energy-absorbing PSII from "spilling over" into PSI. Second, the degree of stacking is adjustable: shade leaves have large grana with many layers, and stacking is relaxed in strong light.

The chloroplast has its own circular genome (about 120–160 kb in angiosperms, encoding about 100 genes), but more than 95% of chloroplast proteins are encoded in the nucleus, synthesized in the cytoplasm and imported through the TOC/TIC translocon complexes of the envelope. Many complexes are assembled from products of both genomes: the large subunit of **Rubisco** is encoded by the plastid gene *rbcL* and the small subunit by the nuclear gene *RBCS*, and eight large and eight small subunits make up the holoenzyme; the D1 protein of the PSII reaction center is encoded by the plastid gene *psbA*. In most angiosperms plastids are transmitted only through the mother, so traits determined by chloroplast genes (such as the herbicide-resistance mutation in Section 7.3.4 below) show **maternal inheritance**.

### 7.1.2. Photosynthetic Pigments

**Definition 7.1.1 (Photosynthetic Pigment)** Pigments on the thylakoid membrane that absorb and transfer light energy or carry out photochemical reactions are called **photosynthetic pigments**. Higher plants have two classes of them: chlorophylls (chlorophyll a and chlorophyll b) and carotenoids (carotenes and xanthophylls). Cyanobacteria and red algae also have phycobilins covalently bound to proteins.

By function, most chlorophyll a, all chlorophyll b and all carotenoids are antenna (light-harvesting) pigments, which only absorb and transfer light energy; a few chlorophyll a molecules in a special protein environment form the special pair of the reaction center (P680, P700) and convert excitation energy into charge separation. The structure of **chlorophyll** (the tetrapyrrole ring, the central $\ce{Mg^2+}$, the long phytol tail) and the photoprotective role of **accessory pigments** were defined in [7.1.24](/7.1.24#sec-24.2.2); only their physiological properties are listed here:

| Pigment | Formula | Color | Absorption peaks in organic solvent | Solubility | Function |
|---|---|---|---|---|---|
| Chlorophyll a | $\ce{C55H72O5N4Mg}$ | blue-green | about 430, 662 nm | soluble in ethanol, acetone, ether | antenna; the only pigment of the special pair |
| Chlorophyll b | $\ce{C55H70O6N4Mg}$ | yellow-green | about 453, 642 nm | same, slightly more polar | antenna (mainly in LHCII) |
| β-Carotene | $\ce{C40H56}$ | orange-yellow | about 425, 450, 478 nm | only in organic solvents, least polar | quencher in the reaction-center complexes; antenna |
| Xanthophylls (lutein, violaxanthin, zeaxanthin, neoxanthin) | $\ce{C40H56O2}$ to $\ce{C40H56O4}$ | yellow | about 420–480 nm (three peaks) | only in organic solvents | antenna; quench triplet chlorophyll; xanthophyll cycle (Section 7.5.2) |
| Phycobilins (phycoerythrobilin, phycocyanobilin) | open-chain tetrapyrroles | red, blue | 520–630 nm | covalently bound to **phycobiliproteins**, water-soluble | antennae of cyanobacteria and red algae (**phycobilisomes**) |

The chlorophyll molecule is amphipathic: the porphyrin head is polar and can bind proteins, whereas the phytol tail is a long hydrocarbon chain buried in the membrane lipids. Chlorophyll is insoluble in water and must therefore be extracted with organic solvents; its binding to protein is not covalent and is easily disrupted during extraction, whereas phycobilins are linked to protein by thioether bonds and can be separated only by boiling in strong acid. In acid, chlorophyll loses $\ce{Mg^2+}$ and turns into brown pheophytin; replacing Mg with copper or zinc gives stable green copper chlorophyll, which is the principle of "green retention" in processing green vegetables and preserving specimens.

In a normal leaf the chlorophyll-to-carotenoid ratio is about 3:1, the chlorophyll a-to-b ratio about 3:1, and the lutein-to-carotene ratio about 2:1. The chlorophyll a/b ratio varies with the light environment: shade leaves have more LHCII and a lower a/b (about 2.2–2.6); the chloroplasts in the bundle sheath of C4 plants lack LHCII, and the a/b of such leaves is often slightly higher than in C3 plants.

### 7.1.3. Extraction, Separation and Quantification of Pigments

Extraction exploits the lipid solubility of the pigments: leaves are ground in 80% acetone or 95% ethanol (a little $\ce{CaCO3}$ is added to neutralize organic acids released from the vacuole and prevent pheophytinization, and quartz sand aids grinding) and filtered to give the extract. Separation exploits differences in polarity and adsorption: the extract is spotted on filter paper or a silica thin layer and developed with a solvent of very low polarity such as petroleum ether–acetone (or with a little benzene). Carotene, the least polar, travels farthest with the solvent front, followed by xanthophyll and chlorophyll a, and chlorophyll b, the most polar, moves least; from top to bottom there are thus four bands: orange-yellow, yellow, blue-green and yellow-green.

Quantification relies on the additivity of the **Lambert–Beer law**: the absorbance of a mixed solution at a given wavelength is the sum of the absorbances of the components. Measuring absorbance at two wavelengths near the red peaks of chlorophylls a and b gives two linear equations whose solution yields both concentrations. The commonly used coefficients are those of Lichtenthaler (1987) for 80% acetone (concentrations in $\mathrm{\mu g\,mL^{-1}}$):

$$
\begin{aligned}
c_{\mathrm{a}} &= 12.25\,A_{663.2} - 2.79\,A_{646.8},\\
c_{\mathrm{b}} &= 21.50\,A_{646.8} - 5.10\,A_{663.2},\\
c_{\mathrm{x+c}} &= \frac{1000\,A_{470} - 1.82\,c_{\mathrm{a}} - 85.02\,c_{\mathrm{b}}}{198},
\end{aligned}
\tag{7.1}
$$
where $c_{\mathrm{x+c}}$ is the total concentration of carotenoids (xanthophylls and carotenes). Absorption peak positions and absorption coefficients differ among solvents, so the coefficients for the solvent actually used must be applied. The Arnon (1949) equations ($A_{663}$ and $A_{645}$), common in Chinese textbooks, rest on less accurate absorption coefficients and underestimate the chlorophyll a/b ratio (Porra et al., 1989); today the equations above or Porra's coefficients are generally used instead.

**Example 7.1.1** A 0.10 g sample of fresh leaf is extracted in 80% acetone and made up to 10 mL; the measured absorbances (1 cm path) are $A_{663.2} = 0.60$, $A_{646.8} = 0.25$ and $A_{470} = 0.70$. By Eq. (7.1), $c_{\mathrm{a}} = 12.25 \times 0.60 - 2.79 \times 0.25 = 6.65\,\mathrm{\mu g\,mL^{-1}}$, $c_{\mathrm{b}} = 21.50 \times 0.25 - 5.10 \times 0.60 = 2.32\,\mathrm{\mu g\,mL^{-1}}$ and $c_{\mathrm{x+c}} = (700 - 12.1 - 197.2)/198 = 2.48\,\mathrm{\mu g\,mL^{-1}}$. Total chlorophyll is $8.97\,\mathrm{\mu g\,mL^{-1}} \times 10\,\mathrm{mL}/0.10\,\mathrm{g} = 0.90\,\mathrm{mg\,g^{-1}}$ (fresh weight), the a/b ratio is 2.87, and the chlorophyll-to-carotenoid ratio is 3.6, all within the range of normal leaves.

## 7.2. Light Absorption and Excited States

### 7.2.1. Photosynthetically Active Radiation

One mole of **photons** of wavelength $\lambda$ carries energy $E_{\mathrm{m}} = N_{\mathrm{A}}hc/\lambda$ ([7.1.24](/7.1.24#eq-24.3)): $176\,\mathrm{kJ\,mol^{-1}}$ for red light of 680 nm and $266\,\mathrm{kJ\,mol^{-1}}$ for blue light of 450 nm. The light that photosynthesis can use lies between 400 and 700 nm and is called *photosynthetically active radiation* (PAR); it makes up about 45%–50% of the solar radiant energy reaching the ground ([7.6.18](/7.6.18#sec-18.1.1)). Photosynthesis is a photochemical reaction in which one photon drives one excitation regardless of its energy, so plant physiology measures light in photons rather than energy: the *photosynthetic photon flux density* (PPFD) is the amount of substance of 400–700 nm photons passing through unit area per unit time, in $\mathrm{\mu mol\,m^{-2}\,s^{-1}}$. Full sunlight at clear-sky noon is about $2000\,\mathrm{\mu mol\,m^{-2}\,s^{-1}}$, an overcast day about 200–500, a closed forest floor often less than 20, and indoor lighting about 10.

**Example 7.2.1** For the solar spectrum, the conversion factor between PAR energy flux and photon flux is about $4.57\,\mathrm{\mu mol\,J^{-1}}$ (McCree, 1972). Full sunlight at $2000\,\mathrm{\mu mol\,m^{-2}\,s^{-1}}$ thus corresponds to a PAR energy flux of $2000/4.57 = 438\,\mathrm{W\,m^{-2}}$; taking PAR as 45% of total radiation, total radiation is about $970\,\mathrm{W\,m^{-2}}$, in agreement with the empirical value of $1000\,\mathrm{W\,m^{-2}}$ for clear-sky noon at sea level. For artificial sources the factor depends on the spectrum (about $5.5\,\mathrm{\mu mol\,J^{-1}}$ for red LEDs, because long-wavelength photons carry less energy), so plant lighting should be evaluated by PPFD rather than illuminance (lx, weighted by the sensitivity of the human eye, with green light weighted most).

### 7.2.2. Absorption Spectra and Action Spectra

The absorption spectrum of a pigment says which wavelengths it absorbs; whether absorbed light is then used for photosynthesis is answered by a different spectrum.

**Definition 7.2.1 (Action Spectrum)** The **action spectrum** of a photobiological process is the efficiency of the process (reaction rate per incident photon or per absorbed photon) as a function of wavelength. The action spectrum of photosynthesis is usually the quantum yield of $\ce{O2}$ evolution or $\ce{CO2}$ uptake plotted against wavelength.

Comparing an action spectrum with the absorption spectra of candidate pigments is the classical method of identifying a photoreceptor: if the action spectrum matches the absorption spectrum of a pigment, that pigment is the photoreceptor of the process. In 1882 Theodor Engelmann obtained the first action spectrum of photosynthesis by observing aerobic bacteria gathering at the parts of a filamentous green alga illuminated by red and blue light; photoreceptors such as **phytochrome** and **phototropin** were later found in the same way ([7.6.18](/7.6.18#sec-18.5.3), [7.13.16](/7.13.16)).

The absorption spectra of pigments in a leaf differ from those in solution (Figure 1). In proteins the red peak of chlorophyll a shifts from 662 nm to 670–680 nm and the absorption band broadens; multiple scattering inside the leaf lengthens the light path (the "detour effect"), so that 70%–80% of green light, which is weakly absorbed in solution, is absorbed in the leaf; conversely, because pigments are concentrated in chloroplasts rather than uniformly distributed, part of the light passes between chloroplasts (the "sieve effect"). A whole leaf therefore absorbs about 85% of PAR, with only a shallow trough near 550 nm. The action spectrum differs from the absorption spectrum mainly in two ways: the quantum yield is lower in the blue than in the red, because part of the blue light is absorbed by pigments that do not transfer energy (anthocyanins, flavonoids) and by carotenoids, whose energy transfer is less efficient (about 90% for carotenoid to chlorophyll a, close to 100% for chlorophyll b); and beyond 700 nm the leaf still absorbs a little while the action spectrum drops steeply, which is the red drop discussed below.

![Absorption spectra of photosynthetic pigments and the action spectrum of a leaf. A: schematic absorption spectra in organic solvent of chlorophyll a (430, 662 nm), chlorophyll b (453, 642 nm), β-carotene (425, 450, 478 nm) and lutein (422, 445, 474 nm), built from Gaussian bands at the absorption maxima and normalized individually. B: absorptance of a whole leaf (solid line), the action spectrum of $\ce{CO2}$ uptake per incident photon (approximating the mean curve for crop leaves measured by McCree in 1972) and their ratio, the quantum yield per absorbed photon (dashed line); the shaded band is photosynthetically active radiation at 400–700 nm. The leaf absorbs most green light, the quantum yield is highest in the red and lower in the blue, and it drops steeply beyond 700 nm. The curves are schematic, not measured data](./plots/spectra.py)

### 7.2.3. Fates of the Excited State: Fluorescence and Phosphorescence

After chlorophyll absorbs a photon, one electron is promoted to an excited singlet state. On absorbing blue light it reaches the second excited singlet state $\mathrm{S}_2$, which loses the excess energy as heat by internal conversion within about $10^{-13}\,\mathrm{s}$ and falls to the first excited singlet state $\mathrm{S}_1$; on absorbing red light it reaches $\mathrm{S}_1$ directly. The lifetime of $\mathrm{S}_1$ is of the order of nanoseconds, during which the excitation energy has several possible fates ([7.6.18](/7.6.18#sec-18.1.3)):

1. Emission of a photon as **fluorescence**, returning to the ground state. A chlorophyll solution is green in transmitted light and emits dark red fluorescence in reflected light; the fluorescence is slightly longer in wavelength than the red light absorbed (two peaks at about 685 nm and 740 nm in leaves) because part of the energy has already been lost before emission.
2. Radiationless return to the ground state as heat (internal conversion).
3. Intersystem crossing to the **triplet state**. The triplet state is long-lived (microseconds to milliseconds), and the light it emits on returning to the ground state is **phosphorescence**; triplet chlorophyll can also pass its energy to $\ce{O2}$ to form highly destructive singlet oxygen, one of the roots of damage in strong light (Section 7.5.1).
4. Transfer of the excitation energy to neighboring pigment molecules, finally reaching the reaction center to drive the photochemical reaction.

These pathways compete, and the **quantum yield** of each is the share of its rate constant in the total rate constant (**Formula 7.4.1**). In solution, isolated chlorophyll has no pathway 4 and the fluorescence yield is about 30%; in the leaf the reaction center captures the excitation within tens to hundreds of picoseconds, the quantum yield of photochemistry is as high as 0.85 or more, and fluorescence accounts for only a few percent of absorbed photons.

**Example 7.2.2** Because of the $\mathrm{S}_2 \to \mathrm{S}_1$ internal conversion, a blue photon and a red photon act identically in photosynthesis. Of the energy of a 450 nm photon, $(266 - 176)/266 = 34\%$ becomes heat in the very first step. Per unit energy, therefore, red light is used more efficiently than blue; per photon, the two have similar quantum yields. This is also why plant lighting is based on red light with a little blue added (blue light serves photomorphogenesis and stomatal opening, not as the energy source of photosynthesis).

## 7.3. The Photosynthetic Unit and the Two Photosystems

### 7.3.1. The Photosynthetic Unit

In 1932 Robert Emerson and William Arnold illuminated *Chlorella* with a series of very short (about $10\,\mu\mathrm{s}$) saturating flashes and measured the $\ce{O2}$ evolved per flash. When the flash was strong enough, the oxygen yield per flash no longer increased with flash intensity; at that point only one $\ce{O2}$ molecule was evolved per 2500 chlorophyll molecules. If every chlorophyll molecule could carry out photochemistry independently, a saturating flash should give an oxygen yield comparable to the number of chlorophylls; the actual yield was three orders of magnitude lower, showing that chlorophylls work in groups serving a small number of reaction centers.

**Definition 7.3.1 (Photosynthetic Unit)** The structural unit, consisting of one reaction center and the antenna pigments that collect light for it, required to complete one photochemical reaction under a saturating flash is called the **photosynthetic unit**. Evolving one $\ce{O2}$ requires 4 electrons, and each electron requires one photochemical reaction in each of the two photosystems, so 2500 chlorophylls correspond to about 8 photochemical reactions and each reaction center has about 300 chlorophylls (in fact the antenna sizes of PSII and PSI differ and vary with the light environment, at about 200–400).

The significance of the antenna lies in matching rates: in full sunlight a single chlorophyll absorbs only about 10 photons per second, whereas a reaction center can turn over 100–500 times per second ([7.6.18](/7.6.18#sec-18.3.1)). The antenna concentrates the photons absorbed by several hundred pigments on one reaction center so that the costly reaction-center protein is fully used. The cost of the antenna appears in strong light: a large antenna, advantageous in weak light, collects far more photons in full sunlight than the reaction center can handle, and the excess excitation must be dissipated (Section 7.5).

### 7.3.2. Quantum Requirement

**Definition 7.3.2 (Quantum Requirement)** The number of photons that must be absorbed per $\ce{O2}$ molecule evolved (or per $\ce{CO2}$ molecule fixed) in photosynthesis is called the **quantum requirement**; it is the reciprocal of the **quantum yield**:

$$
\text{quantum requirement} = \frac{\text{photons absorbed}}{\ce{O2}\ \text{evolved}} = \frac{1}{\Phi_{\ce{O2}}}. \tag{7.2}
$$

The Z scheme ([7.1.24](/7.1.24#sec-24.3.2)) gives the theoretical lower limit: moving 4 electrons from 2 water molecules to 2 $\mathrm{NADP^+}$ requires one photon in PSII and one in PSI for each electron, 8 photons in all, and the quantum yield has an upper limit of $1/8 = 0.125$. In the 1940s Otto Warburg insisted that the quantum requirement was only 3–4, and argued for years against the 8–10 measured by Emerson; later accurate measurements supported the latter. Björkman and Demmig (1987) measured the maximum quantum yield of leaves of 37 C3 species under low-$\ce{CO2}$, photosynthesis-limiting conditions: the mean was 0.106 $\ce{O2}$ per photon absorbed, a quantum requirement of about 9.4, with almost no difference among the species measured.

The roughly one photon above 8 is used mainly to balance the ratio of ATP to NADPH:

**Example 7.3.1** For each electron passed along linear electron flow, 3 $\ce{H+}$ are transferred into the thylakoid lumen (1 released by water splitting and 2 through the Q cycle of the $b_6f$ complex). The c-ring of chloroplast ATP synthase has 14 subunits; one turn transports 14 $\ce{H+}$ and synthesizes 3 ATP, so each ATP requires $14/3 = 4.67$ $\ce{H+}$. Reducing 2 NADPH requires 4 electrons and transfers 12 $\ce{H+}$, producing $12/4.67 = 2.57$ ATP. The Calvin cycle needs 3 ATP and 2 NADPH per $\ce{CO2}$ fixed ([7.1.25](/7.1.25#eq-25.3)), so 0.43 ATP is missing, equivalent to 2 $\ce{H+}$. **Cyclic electron flow** transfers 2 $\ce{H+}$ per electron, so about 1 cyclic electron is needed per 4 linear electrons: PSI turns over 5 times and PSII 4 times, giving a photon requirement of 9 per $\ce{CO2}$, in agreement with the measured 9–10. The statement common in Chinese textbooks that "noncyclic electron transport produces 3 ATP and assimilating 3 $\ce{CO2}$ requires 10 ATP" uses an old value that assumes 4 $\ce{H+}$ per ATP and also miscounts the requirement of the Calvin cycle (which is 9 ATP and 6 NADPH). Photorespiration, nitrate assimilation and the C4 cycle increase the ATP demand further ([7.13.8](/7.13.8)).

:::

The flash experiments of Emerson and Arnold also revealed the four-step accumulation in the PSII oxygen-evolving complex (the **Kok cycle**, [7.1.24](/7.1.24#sec-24.4.2)): in dark-adapted chloroplasts oxygen evolution is greatest at the third flash and then oscillates with a period of 4 while gradually damping. Section 7.1.24 wrote the Kok model as a Markov chain; here we see how its parameters are read from the oscillation.

**Example 7.3.2** Let each flash leave a center in place with probability $\alpha$ (a miss), advance it two steps with probability $\beta$ (a double hit) and advance it one step with probability $1-\alpha-\beta$. Take $\alpha = 0.10$ and $\beta = 0.04$; the eigenvalues of the transition matrix $M$ are $1$, $0.06 \pm 0.86\mathrm{i}$ and $-0.72$. The complex pair of modulus $0.862$ determines the oscillation: the argument $86.0^\circ$ corresponds to a period of $360/86.0 = 4.19$ flashes (misses make the period slightly longer than 4), the amplitude is multiplied by $0.862$ per flash, and over one period it decays by $0.862^{4.19} = 0.54$. Starting from 25% $\mathrm{S}_0$ and 75% $\mathrm{S}_1$, the relative oxygen yields of successive flashes are 0, 0.05, 0.53, 0.30, 0.10, 0.11, 0.36, 0.31, …, and by the 12th flash they are close to the steady-state value of 0.25. In practice the measured flash-yield sequence is fitted by least squares for $\alpha$, $\beta$ and the initial state; conversely, the decay rate and period, two observables, also determine $\alpha$ and $\beta$ directly.

### 7.3.3. Red Drop and the Emerson Enhancement Effect

**Definition 7.3.3 (Red Drop)** Under far-red light of wavelength greater than about 680 nm, the quantum yield of photosynthesis falls steeply even though chlorophyll still absorbs this light. This phenomenon is called the **red drop** (Emerson and Lewis, 1943).

**Definition 7.3.4 (Emerson Enhancement Effect)** When light of shorter wavelength (for example 650 nm) is supplied in addition to far-red light (for example 700 nm), the photosynthetic rate exceeds the sum of the rates under the two lights separately. This phenomenon is called the **Emerson enhancement effect** (Emerson, 1957).

For example, the oxygen evolution rate is 20 under far-red light alone and 100 under red light alone, but can reach 160 under both together, an enhancement ratio of $160/120 = 1.33$. These two phenomena show that photosynthesis is carried out by two photochemical reactions in series: one (PSI) can use far-red light and the other (PSII) cannot; under far-red light alone PSII becomes the bottleneck, and adding red light balances the excitation of the two photosystems (Figure 2). This inference, together with the opposite redox changes of cytochrome under the two lights, led to the Z scheme of Hill and Bendall (1960).

![Red drop and the Emerson enhancement effect in a two-photosystem model. Linear electron flow needs one photon absorbed in each of PSII and PSI per electron, so the light-limited quantum yield is proportional to 2 min(f₁, f₂), where f₁ and f₂ = 1 − f₁ are the fractions of absorbed photons allocated to PSI and PSII. A: excitation partitioning in the model: at short wavelengths f₁ = 0.42 in state 1 (slightly more to PSII), and beyond 700 nm almost only PSI absorbs (solid line); in state 2 part of LHCII moves to PSI and f₁ increases by 0.08, bringing the two photosystems close to balance (dashed line). B: relative quantum yield; the steep drop beyond 680 nm is the red drop, and a state transition can improve only the band where PSII still absorbs. C: a 700 nm beam (photon flux 1) supplemented with 650 nm light of different fluxes; the oxygen evolution rate under simultaneous illumination (solid line) is higher than the sum for the two beams separately (dashed line), the shaded area being the enhancement. Parameters are schematic values](./plots/red-drop.py)

The division of labor of the two photosystems:

| | Photosystem II | Photosystem I |
|---|---|---|
| Reaction-center pigment | P680 | P700 |
| Main location | stacked regions of grana | stroma thylakoids and grana margins |
| Absorption | up to about 680 nm (LHCII rich in chlorophyll b) | extends beyond 700 nm |
| Photochemical reaction | oxidizes water, releasing $\ce{O2}$ and $\ce{H+}$; reduces plastoquinone | oxidizes plastocyanin; reduces $\mathrm{NADP^+}$ via ferredoxin |
| Produces | a strong oxidant ($\mathrm{P680^+}$, about +1.2 V) | a strong reductant (about −1.0 V) |
| Sensitivity to strong light | D1 protein easily damaged, constantly repaired | generally stable; easily damaged by reactive oxygen species at low temperature, with very slow recovery |

Besides linear electron flow, PSI electrons can return to plastoquinone (**cyclic electron flow**, producing only ATP) or be given to $\ce{O2}$ to form superoxide anion, which is then reduced to water by **superoxide dismutase** and ascorbate peroxidase (the Mehler reaction, or water–water cycle; called pseudocyclic electron transport in Chinese textbooks). Neither produces NADPH. Both increase in strong light, at low temperature, or when stomatal closure leaves too little $\mathrm{NADP^+}$, supplementing ATP and maintaining acidification of the thylakoid lumen to start photoprotection (Section 7.5.2).

### 7.3.4. Electron-Transport Inhibitors and Herbicides

Many herbicides act on photosynthetic electron transport or on pigment synthesis. Their sites of action are individual steps of the electron-transport chain, and in research they are also tools for dissecting its parts:

| Agent (class) | Site of action | Consequence |
|---|---|---|
| Diuron (DCMU, substituted ureas), atrazine (triazines) | compete with plastoquinone for the $\mathrm{Q_B}$ binding site on the D1 protein | PSII cannot pass electrons to plastoquinone; the excitation cannot be used, fluorescence rises, and triplet chlorophyll and singlet oxygen increase |
| Paraquat, diquat (bipyridyliums) | accept electrons from the iron–sulfur centers on the acceptor side of PSI and pass them to $\ce{O2}$ | continuous production of superoxide anion and other **reactive oxygen species**, lipid peroxidation of membranes, leaves wilt within hours in light |
| DBMIB (experimental reagent) | plastoquinol oxidation site of the cytochrome $b_6f$ complex | blocks electron flow between PSII and PSI |
| Norflurazon (phytoene desaturase inhibitor), mesotrione (HPPD inhibitor) | carotenoid synthesis (mesotrione also blocks synthesis of plastoquinone and tocopherol) | new leaves lack carotenoids and are bleached white in light |
| Acifluorfen and others (protoporphyrinogen oxidase inhibitors) | chlorophyll and heme synthesis (Section 7.6.1) | protoporphyrinogen leaks into the cytoplasm and is oxidized to protoporphyrin IX, a photosensitizer that produces singlet oxygen |

Wide use of triazine herbicides has selected resistant weeds: in many weeds such as *Amaranthus* and *Chenopodium*, resistance comes from a point mutation in the chloroplast *psbA* gene that changes serine at position 264 of the D1 protein to glycine, so that the herbicide no longer binds. The same mutation slows electron transfer from $\mathrm{Q_A}$ to $\mathrm{Q_B}$, so that resistant plants photosynthesize less and compete less well in the absence of the herbicide; being encoded in the chloroplast genome, it is inherited maternally.

## 7.4. Chlorophyll Fluorescence

### 7.4.1. Competition among Fluorescence, Photochemistry and Heat Dissipation

Chlorophyll fluorescence comes almost entirely from the PSII antenna; at room temperature PSI fluorescence is weak. An excited chlorophyll in the PSII antenna has three fates: fluorescence (rate constant $k_{\mathrm{F}}$), heat dissipation ($k_{\mathrm{D}}$, plus the regulated nonphotochemical quenching $k_{\mathrm{N}}$) and photochemistry in open reaction centers ($k_{\mathrm{P}}$). A reaction center is "open" when its primary quinone acceptor $\mathrm{Q_A}$ is oxidized and able to accept an electron; once $\mathrm{Q_A}$ is reduced the center is "closed" and cannot carry out photochemistry again until $\mathrm{Q_A^-}$ has passed its electron to $\mathrm{Q_B}$. Let $q$ be the fraction of open centers; the fluorescence yield is

$$
\Phi_{\mathrm{F}} = \frac{k_{\mathrm{F}}}{k_{\mathrm{F}} + k_{\mathrm{D}} + k_{\mathrm{N}} + q\,k_{\mathrm{P}}}. \tag{7.3}
$$

Photochemistry and heat dissipation both "quench" fluorescence and are called photochemical quenching and nonphotochemical **quenching**, respectively. Fluorescence is thus an internal probe: it competes with photochemistry for the same excited state, so measuring fluorescence lets us infer how much excitation photochemistry has used. In 1931 Hans Kautsky observed that when a dark-adapted leaf is suddenly illuminated, fluorescence rises quickly to a peak and then falls to a steady state within a few minutes (the Kautsky effect); the latter corresponds to the gradual start-up of carbon assimilation and the reopening of reaction centers.

**Formula 7.4.1 (Maximum Photochemical Efficiency of PSII)** In a dark-adapted leaf $k_{\mathrm{N}} = 0$. With all centers open ($q = 1$) the minimum fluorescence is $F_0 \propto k_{\mathrm{F}}/(k_{\mathrm{F}} + k_{\mathrm{D}} + k_{\mathrm{P}})$; when a saturating flash temporarily closes all centers ($q = 0$) the maximum fluorescence is $F_{\mathrm{m}} \propto k_{\mathrm{F}}/(k_{\mathrm{F}} + k_{\mathrm{D}})$. The ratio of the variable fluorescence $F_{\mathrm{v}} = F_{\mathrm{m}} - F_0$ to $F_{\mathrm{m}}$ is

$$
\frac{F_{\mathrm{v}}}{F_{\mathrm{m}}} = 1 - \frac{F_0}{F_{\mathrm{m}}} = \frac{k_{\mathrm{P}}}{k_{\mathrm{F}} + k_{\mathrm{D}} + k_{\mathrm{P}}}, \tag{7.4}
$$
exactly the fraction of the excitation absorbed by open PSII centers that is used for photochemistry, that is, the maximum quantum yield of PSII photochemistry.

$F_{\mathrm{v}}/F_{\mathrm{m}}$ requires neither $k_{\mathrm{F}}$ nor the absolute intensity of the measuring light, only the ratio of two fluorescence levels, so it can be measured in the field in a few seconds with a portable instrument. Healthy C3 and C4 leaves are almost all near 0.83 (Björkman and Demmig, 1987, consistent with the maximum quantum yield of 0.106 for the same set of leaves); a value below 0.8 indicates damage to PSII from photoinhibition, low temperature, drought, nutrient deficiency or disease, and it is the index most used in stress physiology ([7.13.27](/7.13.27)).

### 7.4.2. The Saturating-Pulse Method

A pulse-amplitude-modulated (PAM) fluorometer illuminates the leaf with three kinds of light: a very weak modulated measuring light (of fixed frequency, too weak to close reaction centers; the instrument detects only fluorescence at that frequency and so is unaffected by ambient light), an actinic light that drives photosynthesis, and a saturating pulse lasting less than a second that closes all centers. Under actinic light fluorescence is at a steady state $F_{\mathrm{s}}$; a saturating pulse then gives the maximum fluorescence in the light, $F_{\mathrm{m}}'$. If $F_{\mathrm{m}}' < F_{\mathrm{m}}$, the actinic light has induced additional heat dissipation, which persists during the pulse.

**Definition 7.4.1 (Nonphotochemical Quenching)** Lowering of chlorophyll fluorescence by processes other than photochemistry (mainly regulated heat dissipation in the antenna) is called **nonphotochemical quenching** (NPQ). Its magnitude is often expressed as

$$
\mathrm{NPQ} = \frac{F_{\mathrm{m}} - F_{\mathrm{m}}'}{F_{\mathrm{m}}'} \tag{7.5}
$$
(Bilger and Björkman, 1990); by Eq. (7.3) it equals $k_{\mathrm{N}}/(k_{\mathrm{F}} + k_{\mathrm{D}})$, the ratio of the rate constant of regulated heat dissipation to that of basal dissipation in the dark-adapted state.

In the light, the actual photochemical quantum yield of PSII (the fraction of photons absorbed by PSII that is used for photochemistry) is given by Genty et al. (1989):

$$
\Phi_{\mathrm{PSII}} = \frac{F_{\mathrm{m}}' - F_{\mathrm{s}}}{F_{\mathrm{m}}'}, \tag{7.6}
$$
the product of the fraction of open centers and the efficiency of open centers. Multiplying by the absorbed photon flux gives an estimate of the linear electron transport rate:

$$
\mathrm{ETR} = \Phi_{\mathrm{PSII}} \times \mathrm{PPFD} \times 0.5 \times \alpha, \tag{7.7}
$$
where $\alpha$ is the absorptance of the leaf (about 0.84) and 0.5 assumes that absorbed photons are divided equally between the two photosystems.

![Chlorophyll fluorescence by the saturating-pulse method, simulated with a kinetic model. The fluorescence yield is $F = k_{\mathrm{F}}/(k_{\mathrm{F}} + k_{\mathrm{D}} + k_{\mathrm{N}} + q k_{\mathrm{P}})$ with $k_{\mathrm{F}} = 1$, $k_{\mathrm{D}} = 4$ and $k_{\mathrm{P}} = 24.4$ (giving $F_{\mathrm{v}}/F_{\mathrm{m}} = 0.83$), with $F_{\mathrm{m}}$ set to 1. A: a dark-adapted leaf is first given the measuring light to obtain $F_0$, and a saturating pulse (vertical line) gives $F_{\mathrm{m}}$; at 60 s an actinic light of 1000 µmol m⁻² s⁻¹ is switched on (shaded), most reaction centers first close and fluorescence rises to the Kautsky peak, then falls to the steady state $F_{\mathrm{s}}$ as carbon assimilation starts; a pulse every 30 s gives $F_{\mathrm{m}}'$, which declines as nonphotochemical quenching builds up; after the light is switched off at 360 s the centers quickly reopen, nonphotochemical quenching relaxes gradually, dominated by a fast component (time constant 60 s), so that $F_{\mathrm{m}}'$ recovers, and a slow component (900 s) keeps it from recovering completely even after 6 min. B: $\Phi_{\mathrm{PSII}}$ and NPQ calculated from each pulse by Eqs. (7.6) and (7.5). Parameters are schematic values](./plots/pam.py)

**Example 7.4.1** A dark-adapted leaf gives $F_0 = 0.17$ and $F_{\mathrm{m}} = 1.00$ (relative units), so $F_{\mathrm{v}}/F_{\mathrm{m}} = 0.83$. At $1000\,\mathrm{\mu mol\,m^{-2}\,s^{-1}}$ the measurements are $F_{\mathrm{s}} = 0.22$ and $F_{\mathrm{m}}' = 0.41$. Then $\Phi_{\mathrm{PSII}} = (0.41 - 0.22)/0.41 = 0.46$, $\mathrm{NPQ} = (1.00 - 0.41)/0.41 = 1.44$, and $\mathrm{ETR} = 0.46 \times 1000 \times 0.5 \times 0.84 = 195\,\mathrm{\mu mol\,\mathrm{e}^-\,m^{-2}\,s^{-1}}$. If used only to fix $\ce{CO2}$, with 4 electrons per $\ce{CO2}$, this supports a gross assimilation of about $49\,\mathrm{\mu mol\,m^{-2}\,s^{-1}}$; the measured gross assimilation is usually only one half to two thirds of this, the difference going mainly to photorespiration (each oxygenation also consumes 4 electrons) and to nitrate reduction and the Mehler reaction. Measuring ETR and gas exchange together allows estimation of the rate of photorespiration and of mesophyll conductance ([7.13.9](/7.13.9)).

### 7.4.3. Partitioning of Light Energy

From $\Phi_{\mathrm{PSII}}$ and NPQ the energy absorbed by PSII can be divided into three parts (Kramer et al., 2004; the expressions below are the simplified form of Hendrickson et al., 2004): photochemistry $\Phi_{\mathrm{PSII}}$, regulated heat dissipation $\Phi_{\mathrm{NPQ}}$, and other, unregulated losses $\Phi_{\mathrm{NO}}$ (fluorescence and basal heat dissipation). From the definitions of the fluorescence parameters,

$$
\Phi_{\mathrm{NO}} = \frac{F_{\mathrm{s}}}{F_{\mathrm{m}}} = \frac{1 - \Phi_{\mathrm{PSII}}}{1 + \mathrm{NPQ}},\qquad
\Phi_{\mathrm{NPQ}} = \frac{F_{\mathrm{s}}}{F_{\mathrm{m}}'} - \frac{F_{\mathrm{s}}}{F_{\mathrm{m}}} = \frac{(1 - \Phi_{\mathrm{PSII}})\,\mathrm{NPQ}}{1 + \mathrm{NPQ}}, \tag{7.8}
$$
and the three sum to 1. In weak light almost all absorbed light is used for photochemistry; as light intensity increases photochemistry saturates, the surplus is borne mainly by $\Phi_{\mathrm{NPQ}}$, and $\Phi_{\mathrm{NO}}$ stays essentially unchanged (Figure 4). If $\Phi_{\mathrm{NO}}$ rises markedly, regulated dissipation is insufficient, excited states accumulate in the reaction centers and antenna, and the formation of triplet chlorophyll and singlet oxygen increases, a precursor of photodamage. In full sunlight, even a sun leaf with high photosynthetic capacity dissipates more than half of the light it absorbs as heat.

![Partitioning of the light energy absorbed by PSII as a function of light intensity (decomposition of Kramer et al., 2004). Model: linear electron transport $J$ saturates with absorbed light as a nonrectangular hyperbola ($J_{\max} = 200\,\mathrm{\mu mol\,m^{-2}\,s^{-1}}$, curvature 0.7), $\Phi_{\mathrm{PSII}} = J/(0.5 \times 0.84 \times I)$; NPQ increases with light as a Hill function (maximum 2.5, half-saturation 500 µmol m⁻² s⁻¹, Hill coefficient 2); $\Phi_{\mathrm{NPQ}}$ and $\Phi_{\mathrm{NO}}$ are calculated from Eq. (7.8). A: the proportion of the three parts; B: the same partitioning converted into photon flux reaching PSII. Above about 500 µmol m⁻² s⁻¹ nearly all additional light becomes heat. Parameters are schematic values for a sun leaf](./plots/partition.py)

## 7.5. Photoprotection and Photoinhibition

### 7.5.1. Multilayered Photoprotection

Leaves often absorb more light than photosynthesis can use: light above the light-saturation point, and light when low temperature or drought slows carbon assimilation, is excess light energy. Excess excitation increases triplet chlorophyll and singlet oxygen, and excess electrons on the acceptor side of PSI generate superoxide anion and hydrogen peroxide; these **reactive oxygen species** oxidize membrane lipids, proteins and pigments. The defense of plants is multilayered:

| Layer | Mechanism | Time scale |
|---|---|---|
| Reducing absorption | leaf movement (leaf parallel to incident light), reflection by trichomes and wax, chloroplast avoidance movement (mediated by **phototropin**, moving to the lateral walls of the cell in strong light), smaller antenna | minutes to days |
| Dissipating excitation | nonphotochemical quenching: heat dissipation driven by $\Delta\mathrm{pH}$, PsbS and zeaxanthin (Section 7.5.2); state transitions (Section 7.5.3) | seconds to minutes |
| Consuming electrons | photorespiration ([7.13.8](/7.13.8)), cyclic electron flow, Mehler reaction | seconds |
| Scavenging reactive oxygen species | carotenoids quench triplet chlorophyll and singlet oxygen; superoxide dismutase, ascorbate peroxidase, glutathione; tocopherol | continuous |
| Repair | degradation and resynthesis of the D1 protein (Section 7.5.4) | minutes to hours |

### 7.5.2. The Xanthophyll Cycle and PsbS

Rapid nonphotochemical quenching (energy-dependent quenching, qE) builds up within tens of seconds of an increase in light and relaxes within tens of seconds of a decrease. Its trigger is acidification of the thylakoid lumen: when linear electron flow exceeds consumption by ATP synthase, the lumen pH falls from about 7 to 5.5–6. Acidification of the lumen does two things at once: it protonates the PsbS protein in the PSII antenna and it activates the xanthophyll cycle.

**Definition 7.5.1 (Xanthophyll Cycle)** The cycle of reversible interconversion among violaxanthin, antheraxanthin and zeaxanthin on the thylakoid membrane according to light intensity is called the **xanthophyll cycle**. In strong light violaxanthin de-epoxidase, located in the thylakoid lumen (pH optimum about 5.2, with ascorbate as reductant), removes in turn the epoxy groups on the two rings of violaxanthin, forming zeaxanthin through antheraxanthin; in weak light and in the dark zeaxanthin epoxidase, located on the stromal side (requiring NADPH and $\ce{O2}$), epoxidizes zeaxanthin back to violaxanthin.

Zeaxanthin together with protonated PsbS causes LHCII to change conformation and aggregate, entering a state in which excitation energy is rapidly converted to heat; the exact quenching mechanism (energy transfer or charge transfer between chlorophyll and carotenoid) is still debated. The extent of conversion of the xanthophyll pool is expressed by the de-epoxidation state $\mathrm{DEPS} = (Z + 0.5A)/(V + A + Z)$, which can reach 0.6–0.8 in sun leaves at noon; shade leaves have a smaller xanthophyll pool. In *Arabidopsis*, the *npq1* mutant lacking violaxanthin de-epoxidase and the *npq4* mutant lacking PsbS have greatly reduced qE and are more easily damaged in strong and fluctuating light (Niyogi et al., 1998; Li et al., 2000).

Nonphotochemical quenching has a cost: when light intensity drops suddenly (for example when a cloud covers the sun or shade is cast by the swaying of upper leaves) NPQ takes several minutes to relax, and during this time the leaf is still dissipating light it could have used. Kromdijk et al. (2016) simultaneously overexpressed violaxanthin de-epoxidase, PsbS and zeaxanthin epoxidase in tobacco, which sped up NPQ relaxation and raised field biomass by about 15%; the same design raised seed yield of some soybean lines (De Souza et al., 2022). This is a successful example of "improving radiation-use efficiency" ([7.13.9](/7.13.9)).

### 7.5.3. State Transitions

PSII and PSI differ in absorption spectrum, and the spectrum of natural light changes with time: light beneath a canopy is rich in far-red and favors PSI, whereas direct blue and red light favor PSII. If the excitation of the two photosystems is unbalanced, linear electron flow is limited by the one receiving less excitation.

**Definition 7.5.2 (State Transition)** The regulation that redistributes excitation energy by moving part of the antenna between PSII and PSI through reversible phosphorylation of LHCII is called a **state transition**. When PSII is overexcited the plastoquinone pool is reduced, and plastoquinol bound to the cytochrome $b_6f$ complex activates the **protein kinase** STN7, which phosphorylates LHCII; the phosphorylated LHCII leaves the stacked region and binds to PSI (state 2). When PSI is overexcited the plastoquinone pool is oxidized, the kinase is inactivated, and the phosphatase TAP38 dephosphorylates LHCII, which returns to PSII (state 1).

The molecular details of state transitions are in [7.1.24](/7.1.24#sec-24.3.6). In higher plants only a small fraction of LHCII moves; the process acts mainly in weak light and under changes of spectrum, and contributes little in strong light; in the unicellular green alga *Chlamydomonas* the amplitude is much larger. It differs from the xanthophyll cycle in that the xanthophyll cycle converts excess energy to heat, whereas a state transition transfers energy from one photosystem to the other and so raises the quantum yield in weak light (the dashed line in Figure 2B).

### 7.5.4. Photoinhibition and Repair of the D1 Protein

**Definition 7.5.3 (Photoinhibition)** The decline in the efficiency of photosynthesis (quantum yield and maximum photosynthetic rate) when light energy exceeds what the photosynthetic apparatus can use and dissipate is called **photoinhibition**; its main site is PSII, and it appears as a decrease in $F_{\mathrm{v}}/F_{\mathrm{m}}$.

There are two kinds of photoinhibition. Dynamic photoinhibition occurs under moderate excess light: the quantum yield falls while the maximum photosynthetic rate does not, as a result of increased nonphotochemical quenching, and recovery is quick once light intensity falls, so that it is in effect a protection. Chronic photoinhibition occurs under stronger or more prolonged excess light: the D1 protein of the PSII reaction center is oxidatively damaged, and recovery takes hours. D1 is the fastest-turning-over protein in the thylakoid membrane: damaged PSII moves to the unstacked region and partly disassembles, the damaged D1 is degraded by proteases such as FtsH, chloroplast ribosomes synthesize new D1 from *psbA* mRNA and insert it cotranslationally into the membrane, and PSII reassembles and returns to the stacked region. Most other subunits can be reused.

The rate of photodamage is proportional to light intensity and occurs even in weak light; the extent of photoinhibition depends on the balance of damage and repair. Let $x$ be the fraction of functional PSII:

$$
\frac{\mathrm{d}x}{\mathrm{d}t} = -k_{\mathrm{d}}\,I\,x + k_{\mathrm{r}}\,(1 - x), \tag{7.9}
$$
where $k_{\mathrm{d}}I$ is the first-order damage rate constant (proportional to photon flux $I$) and $k_{\mathrm{r}}$ is the repair rate constant.

**Formula 7.5.1 (Steady State of Photoinhibition)** At constant light intensity, Eq. (7.9) approaches the steady state with time constant $1/(k_{\mathrm{d}}I + k_{\mathrm{r}})$:

$$
x^* = \frac{k_{\mathrm{r}}}{k_{\mathrm{r}} + k_{\mathrm{d}}\,I}. \tag{7.10}
$$

This model explains two classical observations. When chloroplast protein synthesis is inhibited with lincomycin or chloramphenicol ($k_{\mathrm{r}} = 0$), even moderate light intensity makes $F_{\mathrm{v}}/F_{\mathrm{m}}$ fall continuously, and the rate of decline gives $k_{\mathrm{d}}$ directly; over the range measured, $k_{\mathrm{d}}I$ is indeed proportional to light intensity (Tyystjärvi and Aro, 1996). Repair is an enzymatic process dependent on protein synthesis with a large temperature coefficient, whereas photodamage itself is almost independent of temperature, so the same light causes much more severe photoinhibition at low temperature. This is why photoinhibition is especially severe on clear days in early spring, at high elevation and in winter evergreens, and it is part of low-temperature stress ([7.13.27](/7.13.27)).

![Two-state damage–repair model of photoinhibition. The fraction of functional PSII, $x$, obeys Eq. (7.9) and $F_{\mathrm{v}}/F_{\mathrm{m}}$ is taken as $0.83x$; $k_{\mathrm{d}} = 10^{-7}\,\mathrm{m^2\,\mu mol^{-1}}$ (damage half-time 58 min at 2000 µmol m⁻² s⁻¹), and $k_{\mathrm{r}} = 3\times10^{-4}\,\mathrm{s^{-1}}$ at 25 °C (half-time 39 min) and $6\times10^{-5}\,\mathrm{s^{-1}}$ at 8 °C. A: 3 h of strong light (shaded) followed by 3 h of weak light: with normal repair $F_{\mathrm{v}}/F_{\mathrm{m}}$ falls to a steady state of 0.50 in about 1 h and recovers essentially in 2 h of weak light; low temperature slows repair, giving a deeper decline and slower recovery; when repair is blocked with lincomycin the decline is continuous and there is no recovery. B: steady-state $F_{\mathrm{v}}/F_{\mathrm{m}}$ against light intensity for the two repair rates, Eq. (7.10). Parameters are schematic values](./plots/photoinhibition.py)

**Example 7.5.1** With the parameters of Figure 5, at 25 °C and $2000\,\mathrm{\mu mol\,m^{-2}\,s^{-1}}$, $k_{\mathrm{d}}I = 2\times10^{-4}\,\mathrm{s^{-1}}$, $x^* = 3/(3 + 2) = 0.60$ and $F_{\mathrm{v}}/F_{\mathrm{m}} = 0.50$; the time constant for reaching steady state is $1/(5\times10^{-4}\,\mathrm{s^{-1}}) = 33\,\mathrm{min}$. At 8 °C, $x^* = 0.6/(0.6 + 2) = 0.23$ and $F_{\mathrm{v}}/F_{\mathrm{m}} = 0.19$. To keep the steady-state $F_{\mathrm{v}}/F_{\mathrm{m}}$ at 0.50 at low temperature, light intensity must be lowered to $k_{\mathrm{r}}(1 - x^*)/(k_{\mathrm{d}}x^*) = 6\times10^{-5} \times 0.4/(10^{-7} \times 0.6) = 400\,\mathrm{\mu mol\,m^{-2}\,s^{-1}}$, only one fifth of the original.

:::

PSI is generally not susceptible to photoinhibition, but in chilling-sensitive plants (cucumber, rice) reactive oxygen species on the acceptor side of PSI destroy its iron–sulfur centers in weak light at 0–10 °C; PSI has no rapid repair cycle comparable to that of D1, and recovery takes days, so the damage is often more serious than photoinhibition of PSII. If photoinhibition lasts too long, chlorophyll is oxidatively degraded and the leaf becomes chlorotic and bleached, which is called photooxidation or photobleaching.

## 7.6. Chlorophyll Synthesis, Degradation and Leaf Color

### 7.6.1. Biosynthesis of Chlorophyll

Chlorophyll shares a tetrapyrrole synthesis pathway with **heme**, and all of it takes place in plastids:

1. Synthesis of 5-aminolevulinic acid (ALA). Plants and most bacteria start from glutamate (the C5 pathway): glutamate is first attached to $\mathrm{tRNA^{Glu}}$, reduced to glutamate-1-semialdehyde by glutamyl-tRNA reductase, and then transaminated to ALA. Animals and fungi instead condense glycine with succinyl-CoA (the Shemin pathway). Glutamyl-tRNA reductase is the rate-limiting step of the whole pathway and is feedback-inhibited by heme and, in the dark, by the FLU protein.
2. Formation of the tetrapyrrole ring. Two ALA condense into the monopyrrole porphobilinogen (PBG); four PBG polymerize and cyclize into uroporphyrinogen III, which is converted by decarboxylation and oxidation to protoporphyrin IX. One chlorophyll molecule requires 8 ALA.
3. Branching. Protoporphyrin IX is the watershed between chlorophyll and heme: ferrochelatase inserts $\ce{Fe^2+}$ to give heme, whereas magnesium chelatase (consuming ATP) inserts $\ce{Mg^2+}$ and sends the molecule into the chlorophyll branch. Mg-protoporphyrin is methylated and forms the fifth ring (by a cyclase that requires Fe) to give protochlorophyllide.
4. Light-requiring reduction. Protochlorophyllide oxidoreductase (POR) reduces one double bond of ring D with NADPH to give chlorophyllide a. Angiosperms have only the light-dependent POR: in the dark protochlorophyllide, POR and NADPH form a ternary complex stored in the prolamellar bodies of **etioplasts**, which is converted within milliseconds on exposure to light. Gymnosperms, mosses, ferns and algae also have a light-independent protochlorophyllide reductase, so the cotyledons of pine are green even in the dark.
5. Esterification and formation of chlorophyll b. Chlorophyll synthase attaches phytol (as phytyl diphosphate) to the propionate side chain of ring IV to give chlorophyll a; chlorophyllide a oxygenase oxidizes the methyl group on ring II of chlorophyll (chlorophyllide) a to a formyl group, giving chlorophyll b.

Free chlorophyll and the synthetic intermediates are all photosensitizers: they absorb light but have no protein to give the energy somewhere to go, and the excited state passes its energy to $\ce{O2}$ to form singlet oxygen. The pathway is therefore tightly controlled, and newly synthesized chlorophyll is immediately bound to light-harvesting proteins. The *Arabidopsis flu* mutant cannot suppress ALA synthesis in the dark, and the protochlorophyllide that accumulates produces singlet oxygen after transfer to light, bleaching and killing the seedlings (Meskauskiene et al., 2001); the PPO-inhibitor herbicides (Section 7.3.4) exploit the same point. The greening of etiolated seedlings on exposure to light is simultaneously controlled by expression of nuclear genes regulated by **phytochrome** and is part of **photomorphogenesis** ([7.13.16](/7.13.16)).

Conditions that affect chlorophyll synthesis:

| Factor | Effect |
|---|---|
| Light | POR of angiosperms requires light; seedlings grown in the dark are etiolated. Light also regulates expression of the synthetic genes through photoreceptors |
| Temperature | enzymatic reactions with an optimum of about 20–30 °C; new leaves turn yellow at low temperature, as seen in wheat seedlings in early spring and in autumn leaves |
| Mineral elements | N and Mg are constituents of chlorophyll; Fe (cyclase, ferredoxin, regulation of glutamyl-tRNA reductase), Mn, Cu and Zn are cofactors of some enzymes in the pathway or affect chloroplast development; deficiency causes chlorosis ([7.13.4](/7.13.4)) |
| Water and oxygen | drought suppresses synthesis and accelerates degradation; without oxygen ALA and the steps after it cannot proceed |

### 7.6.2. Degradation of Chlorophyll

In leaf senescence and fruit ripening chlorophyll is degraded in an orderly way to colorless products, by the PAO (pheophorbide a oxygenase) pathway (Hörtensteiner and Kräutler, 2011):

1. Chlorophyll b is reduced to chlorophyll a (chlorophyll b reductase); only the a form can enter the following steps;
2. the STAY-GREEN (SGR) protein acts as a magnesium dechelatase to remove $\ce{Mg^2+}$, giving pheophytin a (Shimoda et al., 2016);
3. pheophytinase (PPH) hydrolyzes off the phytol to give pheophorbide a, which still retains the intact macrocycle and is green;
4. PAO opens the macrocycle to give red chlorophyll catabolite, which is reduced to primary fluorescent catabolites;
5. the latter are exported from the plastid and isomerized in the vacuole into the colorless, nonfluorescent final products.

The purpose of degradation is not to "remove the green" but to dismantle photosensitive chlorophyll safely while recovering the large amount of nitrogen in chlorophyll-binding proteins and moving it to seeds and new organs ([7.13.24](/7.13.24)). Older textbooks (including some in English) write the removal of phytol by chlorophyllase as the first step; genetic evidence shows that in senescing leaves the main route is first removal of magnesium and then removal of phytol by PPH, while chlorophyllase has a different function. The discovery of SGR also solved an old puzzle: the recessive "green" cotyledon trait ($i$) in Mendel's pea crosses is a mutation in the *SGR* gene, and green seeds cannot degrade chlorophyll at maturity (Armstead et al., 2007; Sato et al., 2007). Stay-green mutations that keep leaves green during senescence are of two kinds: in one chlorophyll is not degraded although photosynthesis has already stopped (such as *sgr*, "cosmetic stay-green"), and in the other the whole senescence process is delayed and the photosynthetic period prolonged ("functional stay-green", associated with drought tolerance and higher yield in crops such as sorghum).

### 7.6.3. Leaf Color and Its Changes

The color of a leaf is the combined result of absorption by the various pigments. In a normal leaf chlorophyll is about three times carotenoid, and the green masks the yellow. Several changes of leaf color:

| Phenomenon | Cause |
|---|---|
| Autumn leaves turn yellow | chlorophyll is degraded in senescence and the more stable carotenoids are revealed (carotenoids are also degraded, but much more slowly) |
| Autumn leaves turn red | not the revealing of existing pigments: senescing leaves newly synthesize anthocyanins in the vacuole, promoted by low temperature, strong light and sugar accumulation; anthocyanins are thought to screen strong light and protect leaves that are recovering nutrients from photoinhibition |
| Etiolation | growth in the dark; angiosperms cannot synthesize chlorophyll and plastids remain at the etioplast stage |
| Chlorosis | deficiency of N or Mg (constituents, remobilizable, so old leaves yellow first) or of Fe, Mn, Cu or Zn (not readily remobilized, so new leaves yellow first; Fe deficiency often gives interveinal chlorosis) |
| Albinism and variegation | mutations in plastid or nuclear genes, or virus infection, prevent some cells from forming normal chloroplasts |
| Photobleaching | prolonged photoinhibition and photooxidation, with chlorophyll destroyed by reactive oxygen species (Section 7.5.4) |

Leaf color can therefore be used diagnostically: in the field a chlorophyll meter (SPAD) measures leaf transmittance at 650 nm and 940 nm to estimate quickly the chlorophyll content and nitrogen nutrition status, guiding topdressing.

## Summary

| Topic | Key points | Quantities |
|---|---|---|
| Photosynthetic pigments (Definition 7.1.1) | chlorophyll a (special pair and antenna), chlorophyll b, carotenoids (antenna and photoprotection), phycobilins | chlorophyll:carotenoid ≈ 3:1, a:b ≈ 3:1, lutein:carotene ≈ 2:1 |
| Extraction and separation | extraction with organic solvents; chromatography from top to bottom: carotene, xanthophyll, chlorophyll a, chlorophyll b | two-wavelength quantification, Eq. (7.1) |
| Measuring light | PAR 400–700 nm, in photons (PPFD) | full sunlight about $2000\,\mathrm{\mu mol\,m^{-2}\,s^{-1}}$; $4.57\,\mathrm{\mu mol\,J^{-1}}$ |
| Action spectrum (Definition 7.2.1) | identifies photoreceptors; leaf absorbs about 85% of PAR; quantum yield highest in red | 34% of the energy of a blue photon is lost in internal conversion |
| Fates of the excited state | fluorescence, heat, triplet state (→ singlet oxygen), energy transfer and photochemistry compete | $\Phi_i = k_i/\sum k$ |
| Photosynthetic unit (Definition 7.3.1) | antenna collects photons for few reaction centers | 2500 Chl per $\ce{O2}$; about 300 Chl per reaction center |
| Quantum requirement (Definition 7.3.2) | two photosystems in series | theoretical 8, measured about 9.4 (quantum yield 0.106); the c14 ring gives ATP/NADPH = 1.29 for linear flow, needing about 1/4 cyclic electrons |
| Red drop and enhancement (Definitions 7.3.3, 7.3.4) | PSI uses far-red, PSII cannot; balanced when both lights are given | quantum yield ∝ $2\min(f_1, f_2)$ |
| Herbicides | DCMU, triazines: $\mathrm{Q_B}$ site; paraquat: reactive oxygen species at the PSI acceptor side; pigment-synthesis inhibitors: bleaching | triazine resistance: D1 Ser264Gly, maternal inheritance |
| Chlorophyll fluorescence | competes with photochemistry for PSII excitation; nondestructive measurement | $F_{\mathrm{v}}/F_{\mathrm{m}} \approx 0.83$; $\Phi_{\mathrm{PSII}}$, NPQ, ETR, Eqs. (7.4)–(7.7) |
| Nonphotochemical quenching (Definition 7.4.1) and xanthophyll cycle (Definition 7.5.1) | $\Delta\mathrm{pH}$ → PsbS protonation + violaxanthin → zeaxanthin; heat dissipation | over half of absorbed light becomes heat in full sunlight; faster relaxation raises yield |
| State transition (Definition 7.5.2) | LHCII phosphorylation (STN7), antenna moves between the two photosystems | acts in weak light and under spectral change |
| Photoinhibition (Definition 7.5.3) | balance of D1 damage and repair; low temperature inhibits repair | Eq. (7.9), steady state $x^* = k_{\mathrm{r}}/(k_{\mathrm{r}} + k_{\mathrm{d}}I)$ |
| Chlorophyll synthesis and degradation | glutamate → ALA → protoporphyrin IX (branch with heme) → light-requiring POR → chlorophyll a → b; degradation: b→a, SGR dechelation, PPH, PAO | 8 ALA per chlorophyll; Mendel's green cotyledons = *sgr* |
| Leaf color | yellow: chlorophyll degradation; red: newly synthesized anthocyanin; chlorosis: N, Mg (old leaves) or Fe etc. (new leaves) | SPAD estimates chlorophyll |

Main equations:

- Photon energy $E_{\mathrm{m}} = N_{\mathrm{A}}hc/\lambda$; quantum requirement $= 1/\Phi_{\ce{O2}}$, Eq. (7.2).
- Fluorescence yield $\Phi_{\mathrm{F}} = k_{\mathrm{F}}/(k_{\mathrm{F}} + k_{\mathrm{D}} + k_{\mathrm{N}} + q k_{\mathrm{P}})$, Eq. (7.3); $F_{\mathrm{v}}/F_{\mathrm{m}} = (F_{\mathrm{m}} - F_0)/F_{\mathrm{m}}$, Eq. (7.4).
- $\mathrm{NPQ} = (F_{\mathrm{m}} - F_{\mathrm{m}}')/F_{\mathrm{m}}'$, $\Phi_{\mathrm{PSII}} = (F_{\mathrm{m}}' - F_{\mathrm{s}})/F_{\mathrm{m}}'$, $\mathrm{ETR} = \Phi_{\mathrm{PSII}} \times \mathrm{PPFD} \times 0.5 \times \alpha$, Eqs. (7.5)–(7.7); energy partitioning $\Phi_{\mathrm{PSII}} + \Phi_{\mathrm{NPQ}} + \Phi_{\mathrm{NO}} = 1$, Eq. (7.8).
- Photoinhibition $\mathrm{d}x/\mathrm{d}t = -k_{\mathrm{d}}Ix + k_{\mathrm{r}}(1 - x)$, Eqs. (7.9), (7.10).

## Questions

1. The 80% acetone extract of a leaf (1.0 g fresh leaf made up to 25 mL) gives $A_{663.2} = 0.82$ and $A_{646.8} = 0.40$. Find the contents of chlorophylls a and b ($\mathrm{mg\,g^{-1}}$) and the a/b ratio. If this leaf comes from the forest understory, what does the difference in a/b ratio from the leaf of Example 7.1.1 indicate?

   **Answer** By Eq. (7.1), $c_{\mathrm{a}} = 12.25 \times 0.82 - 2.79 \times 0.40 = 10.05 - 1.12 = 8.93\,\mathrm{\mu g\,mL^{-1}}$ and $c_{\mathrm{b}} = 21.50 \times 0.40 - 5.10 \times 0.82 = 8.60 - 4.18 = 4.42\,\mathrm{\mu g\,mL^{-1}}$. Multiplying by 25 mL and dividing by 1.0 g gives $0.22\,\mathrm{mg\,g^{-1}}$ for chlorophyll a and $0.11\,\mathrm{mg\,g^{-1}}$ for b, and an a/b ratio of 2.0, clearly lower than 2.87 in Example 7.1.1. A shade leaf of the understory invests more nitrogen in LHCII, which is rich in chlorophyll b, enlarging the antenna to absorb more weak light, while it has relatively less PSII and PSI reaction centers, electron-transport chain and Rubisco; this is consistent with its lower light-saturation point ([7.13.9](/7.13.9)).

2. *Chlorella* illuminated with 700 nm far-red light evolves oxygen at a rate of 20; with 650 nm red light, 100; with both together, 160. Calculate the enhancement ratio. Why does the enhancement appear only when far-red light and light of shorter wavelength are given simultaneously (or in very short succession)? How does this experiment support the hypothesis of two photosystems in series?

   **Answer** The enhancement ratio is $160/(20 + 100) = 1.33$. Far-red light is absorbed mainly by PSI; under far-red alone PSI excitation is in excess and PSII in deficit, and linear electron flow is limited by PSII. Light of 650 nm is absorbed by both photosystems, slightly more by PSII, and when it is added the excitation of the two photosystems is balanced, the previously surplus PSI excitation is also used, and the combined rate exceeds the sum of the two. If the two photochemical reactions each evolved $\ce{O2}$ independently, the rates should simply add and there would be no enhancement; the existence of enhancement shows that the two lights drive two steps of the same chain, which must cooperate. When the two beams are given more than a few seconds apart, the enhancement disappears, showing that the two reactions are connected by intermediates of limited lifetime (the plastoquinone pool and so on).

3. A leaf at 1500 µmol m⁻² s⁻¹ gives $F_{\mathrm{s}} = 0.20$ and $F_{\mathrm{m}}' = 0.32$; after dark adaptation $F_{\mathrm{m}} = 1.00$ and $F_0 = 0.17$. Calculate $\Phi_{\mathrm{PSII}}$, NPQ, ETR ($\alpha = 0.84$), $\Phi_{\mathrm{NPQ}}$ and $\Phi_{\mathrm{NO}}$. If the same leaf measured early next morning gives $F_{\mathrm{v}}/F_{\mathrm{m}} = 0.70$, what does this indicate?

   **Answer** $\Phi_{\mathrm{PSII}} = (0.32 - 0.20)/0.32 = 0.375$; $\mathrm{NPQ} = (1.00 - 0.32)/0.32 = 2.13$; $\mathrm{ETR} = 0.375 \times 1500 \times 0.5 \times 0.84 = 236\,\mathrm{\mu mol\,m^{-2}\,s^{-1}}$. By Eq. (7.8), $\Phi_{\mathrm{NO}} = 0.20/1.00 = 0.20$ and $\Phi_{\mathrm{NPQ}} = 0.20/0.32 - 0.20 = 0.425$, and the three sum to 1. 42.5% of the absorbed light is dissipated as regulated heat. An $F_{\mathrm{v}}/F_{\mathrm{m}}$ of only 0.70 early next morning (normally about 0.83) shows that about $1 - 0.70/0.83 = 16\%$ of PSII has not recovered overnight: this is chronic photoinhibition (D1 damage not yet fully repaired) or persistent, slowly relaxing quenching associated with retained zeaxanthin, often seen after strong light combined with low temperature or drought.

4. By Eq. (7.9), at 25 °C with $k_{\mathrm{r}} = 3\times10^{-4}\,\mathrm{s^{-1}}$, light is suddenly lowered from 2000 to 50 µmol m⁻² s⁻¹. Find the time for $x$ to recover from 0.60 to 0.95. If lincomycin is sprayed, how long does it take $x$ to fall to 0.5 at 2000 µmol m⁻² s⁻¹?

   **Answer** At 50 µmol m⁻² s⁻¹, $k_{\mathrm{d}}I = 5\times10^{-6}\,\mathrm{s^{-1}}$, $k = k_{\mathrm{d}}I + k_{\mathrm{r}} = 3.05\times10^{-4}\,\mathrm{s^{-1}}$, and the steady state is $x^* = 3/3.05 = 0.984$. From $x(t) = x^* + (x_0 - x^*)\mathrm{e}^{-kt}$, $0.95 = 0.984 - 0.384\,\mathrm{e}^{-kt}$, $\mathrm{e}^{-kt} = 0.0876$, and $t = \ln(11.4)/k = 2.43/3.05\times10^{-4} = 8.0\times10^{3}\,\mathrm{s} \approx 2.2\,\mathrm{h}$. With repair blocked, $x = \mathrm{e}^{-k_{\mathrm{d}}It}$ and $t = \ln 2/(2\times10^{-4}\,\mathrm{s^{-1}}) = 3.5\times10^{3}\,\mathrm{s} \approx 58\,\mathrm{min}$. The presence of repair makes the steady state in strong light stop at 0.6 rather than tend to zero.

5. Explain the following: (a) fluorescence of a leaf treated with DCMU increases markedly in light; (b) paraquat kills plants only in light; (c) bean sprouts (etiolated seedlings) turn green a few hours after being put in light, whereas pine seedlings are green even in the dark; (d) in autumn ginkgo leaves turn yellow and maple leaves turn red.

   **Answer** (a) DCMU occupies the $\mathrm{Q_B}$ site, $\mathrm{Q_A^-}$ cannot pass its electron on, the reaction centers close ($q \to 0$), and by Eq. (7.3) the fluorescence yield rises to near $F_{\mathrm{m}}$. (b) Paraquat accepts electrons from the acceptor side of PSI and passes them to $\ce{O2}$, generating reactive oxygen species; in the dark there is no photosynthetic electron flow, no electrons for it to intercept, and so no reactive oxygen species. (c) Angiosperms have only the light-dependent protochlorophyllide oxidoreductase; in the dark protochlorophyllide accumulates as a ternary complex and is reduced immediately on exposure to light, chlorophyll synthesis resumes, and phytochrome at the same time promotes expression of chloroplast genes and the formation of thylakoids; gymnosperms such as pine also have a light-independent reductase and can synthesize chlorophyll in the dark. (d) Both degrade chlorophyll in autumn; in ginkgo leaves what is revealed is the existing carotenoids, whereas maple leaves in addition synthesize large amounts of anthocyanin anew in the vacuole and appear red.
