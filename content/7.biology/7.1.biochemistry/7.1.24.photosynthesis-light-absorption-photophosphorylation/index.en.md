---
title: "Photosynthesis I: Light Absorption and Photophosphorylation"
description: The overall reaction and history of photosynthesis and the chloroplast; photon energies, chlorophylls, accessory pigments, absorption and action spectra; light-harvesting complexes and exciton transfer to the reaction center; the type II and type I reaction centers of purple and green sulfur bacteria; the red drop, the two photosystems and the Z scheme; photosystem II, the cytochrome b6f complex, plastocyanin and photosystem I; lateral heterogeneity, state transitions and cyclic electron flow; water splitting by the Mn4CaO5 cluster and the Kok cycle; photophosphorylation, its stoichiometry, the universal ATP synthase and the comparison with oxidative phosphorylation; the pathway card of the light reactions.
---

Photosynthesis captures the energy of sunlight in chemical bonds and is, directly or indirectly, the source of nearly all biological energy and of the oxygen of the atmosphere. Its first stage, the subject of this chapter, converts light into the two products that drive **biosynthesis**: ATP and the reductant **NADPH**. Mechanistically it is **oxidative phosphorylation** ([7.1.23](/7.1.23)) run in reverse with the help of light. In mitochondria electrons fall from **NADH** to $\ce{O2}$; in chloroplasts they are lifted from water to $\mathrm{NADP^+}$, which is possible only because absorbed photons turn a weak reductant into a strong one at two reaction centers. Between the two, the electrons flow downhill through a quinone pool and a **cytochrome** complex homologous to **Complex III**, pump protons, and the proton gradient drives an **ATP synthase** of the same rotary design. The use of the ATP and NADPH to reduce $\ce{CO2}$ in the **Calvin cycle**, **photorespiration** and the C4 and CAM pathways follow in [7.1.25](/7.1.25); the physiology of photosynthesis in leaves and canopies (light-response curves, photoinhibition and photoprotection, gas exchange and the Farquhar model) is in [7.13](/7.13), which uses the thylakoid figure of this chapter. The physics of light absorption and photon energy is in [5.5.1](/5.5.1) and [6.4.9](/6.4.9), and resonance energy transfer in [6.4.10](/6.4.10#sec-10.3.4).

## 24.1. Overview

### 24.1.1. The Overall Reaction and Its History

**Definition 24.1.1 (Photosynthesis)** **Photosynthesis** is the synthesis of carbohydrate from $\ce{CO2}$ and an electron donor driven by light; in plants, algae and cyanobacteria the donor is water and $\ce{O2}$ is released:

$$
\ce{CO2} + \ce{H2O} \xrightarrow{\text{light}} (\ce{CH2O}) + \ce{O2}. \tag{24.1}
$$
It comprises the light-dependent reactions, which use light to make ATP and NADPH, and the carbon-assimilation reactions, which use them to reduce $\ce{CO2}$ to triose phosphates.

The equation was assembled over two centuries. Joseph Priestley found in the 1770s that a sprig of mint "restored" air in which a candle had burned out; Jan Ingenhousz showed in 1779 that this requires light and green parts; Jean Senebier and Nicolas-Théodore de Saussure showed that $\ce{CO2}$ is taken up and that the gain in dry mass exceeds the carbon fixed, the difference being water; Julius Robert Mayer recognized in 1842 that plants convert light into chemical energy. Theodor Engelmann (1882) measured the first action spectrum: when a filamentous alga was illuminated with a spectrum, aerobic bacteria gathered at the parts lit by red and blue light. Cornelis van Niel's comparison of photosynthetic bacteria (1930s) led to the general form of the reaction,

$$
2\,\ce{H2D} + \ce{CO2} \xrightarrow{\text{light}} (\ce{CH2O}) + \ce{H2O} + 2\,\ce{D}, \tag{24.2}
$$
in which $\ce{H2D}$ is water in oxygenic photosynthesis and $\ce{H2S}$, $\ce{H2}$ or an organic acid in bacteria, and implied that the $\ce{O2}$ of plants comes from water, not from $\ce{CO2}$; experiments with $\ce{H2^{18}O}$ (Samuel Ruben and Martin Kamen, 1941) confirmed it. Robert Hill showed in 1937 that illuminated chloroplasts evolve $\ce{O2}$ and reduce an artificial acceptor A (the Hill reaction, $2\,\ce{H2O} + 2\,\mathrm{A} \to 2\,\mathrm{AH_2} + \ce{O2}$) without any $\ce{CO2}$, which separated the light reactions from **carbon fixation**; Severo Ochoa and others identified $\ce{NADP+}$ as the natural acceptor, and Melvin Calvin's group traced the path of carbon in the 1950s ([7.1.25](/7.1.25)).

### 24.1.2. Chloroplasts

In **eukaryotes** both stages take place in chloroplasts, plastids a few micrometers long descended from an engulfed cyanobacterium (**endosymbiotic theory**, [7.1.1](/7.1.1)). Like mitochondria, they have an outer membrane permeable to small molecules and an inner membrane with specific **transporters**; the space it encloses, the stroma, corresponds to the mitochondrial matrix and contains the **enzymes** of **carbon assimilation**, the chloroplast **DNA** and **ribosomes**. Within the stroma lies a third membrane system, the thylakoids, flattened sacs that enclose a single continuous lumen; stacks of disc-shaped thylakoids (grana) are connected by unstacked stromal thylakoids (stroma lamellae). The thylakoid membrane carries the pigments, the two photosystems, the cytochrome $b_6f$ complex and ATP synthase. The topology matters for chemiosmosis: protons are pumped from the stroma (N side) into the lumen (P side), and the $\mathrm{F_1}$ part of ATP synthase faces the stroma, as it faces the matrix in mitochondria (24.5.3).

## 24.2. Light Absorption

### 24.2.1. Photons

A **photon** of wavelength $\lambda$ has energy $E = h\nu = hc/\lambda$ ([5.5.1](/5.5.1#sec-1.3.3)); per mole of photons (an einstein),

$$
E_{\mathrm{m}} = \frac{N_{\mathrm{A}}hc}{\lambda} = \frac{119\,627\,\mathrm{kJ\,mol^{-1}\,nm}}{\lambda}. \tag{24.3}
$$

**Example 24.2.1** Red light of 680 nm carries $119\,627/680 = 176\,\mathrm{kJ\,mol^{-1}}$ (1.82 eV per photon), 700 nm light $171\,\mathrm{kJ\,mol^{-1}}$, and violet light of 400 nm $299\,\mathrm{kJ\,mol^{-1}}$: a mole of red photons carries about three times the free energy needed to make a mole of ATP in a cell (about $50\,\mathrm{kJ\,mol^{-1}}$, [7.1.16](/7.1.16#sec-16.3.2)). Absorption is all or nothing: a photon is absorbed only if its energy matches an electronic transition of the absorbing molecule, the chromophore, which is raised to an excited state; the excited molecule returns to the ground state within nanoseconds by emitting **fluorescence** (at longer wavelength), by **internal conversion** to heat, by passing its excitation to a neighboring molecule, or by transferring an electron, the photochemical reaction that photosynthesis exploits.

### 24.2.2. Chlorophylls

**Definition 24.2.1 (Chlorophyll)** A **chlorophyll** is a green photosynthetic pigment in which a planar, cyclic tetrapyrrole related to protoporphyrin, with a fifth (cyclopentanone) ring and one reduced pyrrole ring (a chlorin), coordinates a $\ce{Mg^2+}$ ion and carries the 20-carbon isoprenoid alcohol phytol as an ester; chlorophyll a and chlorophyll b (which has a formyl group in place of a methyl on ring II) are the main pigments of plants, and bacteriochlorophylls those of anoxygenic photosynthetic bacteria.

The extended conjugated system absorbs strongly in two regions, the Soret band in the blue (around 430 nm for chlorophyll a) and the $\mathrm{Q_y}$ band in the red (around 662 nm in organic solvent, 670–680 nm in **proteins**), with molar absorption coefficients above $10^{5}\,\mathrm{M^{-1}\,cm^{-1}}$, among the highest of biological molecules ([6.4.9](/6.4.9)); the green between them is reflected, which is why plants are green. Plants contain about twice as much chlorophyll a as b; their absorption bands are shifted relative to each other and together cover more of the spectrum. Bacteriochlorophylls, with a second reduced ring, absorb further in the infrared (800–1000 nm), where light filtered through the plants and algae above them is still available. Chlorophyll is always bound to proteins, which fix the chromophores at defined distances and orientations and shift their absorption (the "red" forms of PSI absorb beyond 700 nm). The **heme** of hemoglobin and chlorophyll share their biosynthetic pathway up to protoporphyrin IX, where an iron or a magnesium chelatase decides the fate ([7.1.27](/7.1.27)).

### 24.2.3. Accessory Pigments and Action Spectra

**Definition 24.2.2 (Accessory Pigment)** **Accessory pigments** are light-absorbing molecules of photosynthetic membranes other than the chlorophylls a and b, chiefly carotenoids (carotenes and xanthophylls) and, in cyanobacteria and red algae, the phycobilins; they absorb at wavelengths poorly absorbed by chlorophyll and pass the energy to it, and the carotenoids also protect the photosynthetic apparatus from photooxidative damage.

The carotenoids of leaves, β-carotene (orange) and the xanthophyll lutein (yellow), absorb between 400 and 500 nm. They are **isoprenoids** ([7.1.12](/7.1.12#sec-12.5.4)) with eleven conjugated double bonds:

```smiles
CC1=C(C(C)(C)CCC1)/C=C/C(C)=C/C=C/C(C)=C/C=C/C=C(C)/C=C/C=C(C)/C=C/C2=C(C)CCCC2(C)C β-carotene
```

Their protective role is probably more important than light harvesting. When absorbed energy exceeds what the photosynthetic chain can use, excited chlorophyll can cross to its long-lived **triplet state** ([6.4.10](/6.4.10)), which transfers energy to $\ce{O2}$ and forms highly reactive singlet oxygen; carotenoids quench both triplet chlorophyll and singlet oxygen, dissipating the energy as heat. In strong light the lumenal acidification also converts the xanthophyll violaxanthin into zeaxanthin and protonates the protein PsbS, which switches the antenna into a quenching state (nonphotochemical quenching, treated as plant physiology in [7.13](/7.13)). Mutant plants without carotenoids bleach and die in light.

Cyanobacteria and red algae use phycobilins (phycocyanobilin, phycoerythrobilin), open-chain tetrapyrroles related to the bile pigments, covalently bound to phycobiliproteins; they absorb at 520–630 nm, filling the green gap of chlorophyll. They are assembled into phycobilisomes, huge antenna complexes on the stromal surface of the thylakoid membrane, whose complete structure (16.8 MDa, more than 2000 bilins, from the red alga *Griffithsia pacifica*) was determined by **cryo-EM** in 2017 by Sen-Fang Sui's group: energy flows from phycoerythrin at the rim through phycocyanin and allophycocyanin in the core to the chlorophyll of PSII.

The action spectrum of photosynthesis, the rate of $\ce{O2}$ evolution per incident photon as a function of wavelength, follows the combined absorption of chlorophylls and accessory pigments, showing that the energy absorbed by the accessory pigments is used.

![Light absorption by photosynthetic pigments. A: schematic absorption spectra of chlorophyll a (maxima near 430 and 662 nm), chlorophyll b (453 and 642 nm) and β-carotene (425, 450 and 478 nm), built from Gaussian bands at their absorption maxima in organic solvent and normalized, with a schematic action spectrum of a green alga (dashed): photosynthesis is driven by blue and red light, less by green, and falls sharply beyond 680 nm. The upper axis gives the energy of a mole of photons (Eq. (24.3)). B: a two-photosystem model of the red drop. PSII (with chlorophyll b–rich LHCII) absorbs to about 680 nm, PSI further into the far red; linear electron flow needs one photon in each photosystem per electron, so the quantum yield is 2 min(a₁, a₂)/(a₁ + a₂) and drops beyond 680 nm, where PSI absorbs almost all the light. Right: the Emerson enhancement in the same model; O₂ evolution with a 690-nm and a 650-nm beam together exceeds the sum of the rates with each beam alone](./plots/pigment-spectra.py)

### 24.2.4. Light-Harvesting Complexes and Exciton Transfer

A single chlorophyll in full sunlight absorbs only about ten photons per second, too few to keep a reaction center busy, whose photochemistry could run a hundred times faster. The pigments are therefore organized into photosystems: arrays of several hundred chlorophylls and carotenoids, most of which serve as an antenna for one reaction center. Robert Emerson and William Arnold found in 1932 that saturating flashes evolve one $\ce{O2}$ per about 2500 chlorophylls, the first evidence of this "photosynthetic unit" (with four electrons and two photons per electron, about 300 chlorophylls per reaction center).

**Definition 24.2.3 (Light-Harvesting Complex, Exciton Transfer and Reaction Center)** A **light-harvesting complex** (LHC, antenna complex) is a pigment–protein complex that absorbs light and transfers the excitation to a reaction center. The nonradiative transfer of electronic excitation from an excited molecule to a neighboring one, which becomes excited as the first returns to the ground state, is **exciton transfer**. A photochemical **reaction center** is the pigment–protein complex in which the excitation of a specialized pair of chlorophylls (the special pair) causes the transfer of an electron to a nearby acceptor, separating charge across the membrane.

The major antenna of plants, LHCII, is a trimer; each monomer has three transmembrane helices binding eight chlorophyll a, six chlorophyll b, two luteins (which brace the structure like a cross-strut), a neoxanthin and a violaxanthin (the first structure, of 1994, resolved seven and five chlorophylls). Excitation moves between chlorophylls a few nanometers apart by the dipole–dipole mechanism of **Förster resonance energy transfer** ([6.4.10](/6.4.10#sec-10.3.4)), whose rate $k_{\mathrm{T}} = \tau_{\mathrm{D}}^{-1}(R_0/r)^6$ is very high at these distances (between closely coupled chlorophylls the excitation is delocalized and moves even faster). Transfer is funneled: pigments farther from the reaction center tend to absorb at shorter wavelengths (higher energy), so that each step loses a little energy as heat and the excitation drifts toward the special pair, which absorbs at the longest wavelength (680 nm in PSII, 700 nm in PSI). In intact leaves chlorophyll fluorescence is weak, because the excitation is used before it can be emitted.

**Example 24.2.2** Isolated chlorophyll a in solution has a fluorescence lifetime of about 6 ns. In a photosystem the excitation reaches the reaction center and is trapped by charge separation within about 30 ps in PSI and about 200–300 ps in PSII (when the reaction centers are open). If trapping competes with all the processes that would otherwise end the excitation (rate $1/\tau_0$, with $\tau_0 \approx 6\,\mathrm{ns}$ in the antenna), the **quantum yield** of photochemistry is $\Phi = k_{\mathrm{trap}}/(k_{\mathrm{trap}} + 1/\tau_0) = \tau_0/(\tau_0 + \tau_{\mathrm{trap}})$: $6/6.03 = 0.995$ for PSI and $6/6.25 \approx 0.96$ for PSII. Nearly every absorbed photon drives an electron, which is why the measured maximal quantum yield of $\ce{O2}$ evolution, about one $\ce{O2}$ per 8–10 photons, is close to the theoretical one per 8 (24.3.3). When the reaction centers are closed (reduced $\mathrm{Q_A}$) trapping slows, and fluorescence rises; chlorophyll fluorescence is used in the field to measure photosynthetic efficiency (7.13).

## 24.3. Photochemical Reaction Centers

### 24.3.1. Charge Separation

In the reaction center, the excited special pair, a strong reductant, gives an electron within picoseconds to an acceptor a few angstroms away; the hole left on the special pair, a strong oxidant, is filled by an electron from a donor on the other side. The result is a charge-separated state across the membrane, stabilized against recombination by rapid further transfers that move the electron and the hole apart. Two kinds of reaction center, distinguished by their primary acceptors, evolved in bacteria.

- Type II (pheophytin–quinone) reaction centers, as in purple bacteria and in photosystem II, pass the electron from the special pair through a pheophytin (chlorophyll without $\ce{Mg^2+}$) to a tightly bound quinone $\mathrm{Q_A}$ and then to an exchangeable quinone $\mathrm{Q_B}$, which leaves as quinol after two turnovers.
- Type I (Fe–S) reaction centers, as in green sulfur bacteria, heliobacteria and photosystem I, pass the electron through a chlorophyll and a quinone to a chain of [4Fe–4S] clusters and then to the soluble **Fe–S protein** ferredoxin, a reductant strong enough to reduce $\ce{NAD+}$ or $\ce{NADP+}$.

In purple bacteria (*Rhodobacter*, *Rhodopseudomonas*), light excites P870 (the special pair of bacteriochlorophylls, named for its absorption maximum); the electron passes through bacteriopheophytin and $\mathrm{Q_A}$ to $\mathrm{Q_B}$, the quinol diffuses to the cytochrome $bc_1$ complex, homologous to mitochondrial Complex III, which pumps protons by a **Q cycle** and returns the electron through cytochrome $c_2$ to P870⁺. The flow is cyclic: it makes a proton gradient and ATP but no NAD(P)H, which purple bacteria make by reverse electron flow through a Complex I-like enzyme driven by the **proton-motive force**. In green sulfur bacteria (*Chlorobium*), P840* reduces ferredoxin, which reduces $\ce{NAD+}$ through ferredoxin:$\ce{NAD+}$ reductase (linear flow), and the electrons are replaced by the oxidation of $\ce{H2S}$ to sulfur; a cyclic path through menaquinone and a bc complex also pumps protons. The structure of the reaction center of *Rhodopseudomonas viridis*, the first of a membrane protein at atomic resolution, earned Johann Deisenhofer, Robert Huber and Hartmut Michel the Nobel Prize in Chemistry in 1988: two homologous **subunits**, L and M, form a pseudo-twofold symmetrical scaffold with two branches of **cofactors**, of which only one carries the electron.

![The two types of bacterial reaction center on a midpoint-potential axis (reducing at the top; approximate values). A: purple bacteria (type II). Light raises P870 to P870*, which reduces bacteriopheophytin (BPheo), then QA and QB; the quinol joins the ubiquinone pool and is oxidized by the cytochrome bc₁ complex, which pumps protons, and the electron returns through cytochrome c₂ to P870⁺: cyclic flow, ATP but no NADH. B: green sulfur bacteria (type I). P840* reduces a chlorophyll (A₀), a quinone (A₁) and the Fe–S clusters FX and FA/FB, then ferredoxin (Fd), which reduces NAD⁺ (linear flow); the electron lost by P840⁺ is replaced from H₂S through cytochrome c; a cyclic route through menaquinone (MK) and the bc complex (dashed) also pumps protons](./plots/bacterial-reaction-centers.py)

### 24.3.2. Two Photosystems in Tandem

Oxygenic photosynthesis uses both types, in series. The evidence came from quantum yields. Emerson found that the quantum yield of $\ce{O2}$ evolution, constant through most of the red, falls sharply beyond 680 nm, although chlorophyll still absorbs there (the red drop), and that far-red light becomes efficient again if light of shorter wavelength is given at the same time, the combined rate exceeding the sum of the separate rates (the Emerson enhancement effect, 1957). Absorbance changes ("bleaching") of a pigment absorbing at 700 nm, oxidized by far-red light and reduced by shorter-wavelength light, identified the reaction center of one photosystem. In 1960 Robin Hill and Fay Bendall proposed that two photosystems operate in series, linked by cytochromes.

**Definition 24.3.1 (Photosystem I, Photosystem II and the Z Scheme)** **Photosystem II** (PSII) is the type II reaction center of oxygenic organisms, with the special pair P680, which oxidizes water and reduces plastoquinone; **photosystem I** (PSI) is the type I reaction center, with the special pair P700, which oxidizes plastocyanin and reduces ferredoxin. In the **Z scheme**, the carriers of electron flow from water to $\ce{NADP+}$ are arranged by their midpoint potentials: two photochemical steps, one in each photosystem, lift each electron, and between them the electron flows downhill from PSII through plastoquinone, the cytochrome $b_6f$ complex and plastocyanin to PSI.

Overall,

$$
2\,\ce{H2O} + 2\,\ce{NADP+} + 8\,\text{photons} \to \ce{O2} + 2\,\ce{NADPH} + 2\,\ce{H+}, \tag{24.4}
$$
one photon per electron in each photosystem, four electrons per $\ce{O2}$. The span from $\ce{O2}/\ce{H2O}$ (+0.82 V) to $\ce{NADP+}/\mathrm{NADPH}$ (−0.32 V) is 1.14 V, $+440\,\mathrm{kJ}$ per $\ce{O2}$; one 680-nm photon (1.82 eV) could in principle lift an electron 1.82 V, but each photosystem must also make its charge separation irreversible, and the downhill segment between them is used to pump protons, so two photons per electron are needed. The red drop follows at once: PSII absorbs little beyond 680 nm, and far-red light drives PSI alone.

![The Z scheme. Carriers of linear electron flow on a midpoint-potential axis (reducing at the top). Light absorbed by PSII raises P680 to P680*, which reduces pheophytin (Pheo), the quinones QA and QB and the plastoquinone pool; P680⁺, the strongest biological oxidant (about +1.2 V), takes electrons from water through the Mn₄CaO₅ cluster and Tyr Z. Plastoquinol is oxidized by the cytochrome b₆f complex (Rieske Fe–S center, cytochrome f), which pumps protons in a Q cycle, and plastocyanin (PC) carries the electron to P700⁺. Light absorbed by PSI raises P700 to P700*, which reduces the chlorophyll A₀, the phylloquinone A₁, the Fe–S clusters FX, FA and FB, ferredoxin (Fd) and, through ferredoxin–NADP⁺ reductase (FNR), NADP⁺. Dashed: cyclic electron flow from ferredoxin back to the plastoquinone pool](./plots/z-scheme.py)

### 24.3.3. Photosystem II

PSII is a dimer; each monomer has about 20 subunits. Its core is the heterodimer of D1 and D2 (homologous to L and M of the purple-bacterial reaction center), which binds P680, two pheophytins, $\mathrm{Q_A}$ (on D2) and $\mathrm{Q_B}$ (on D1), and a nonheme iron between them; CP43 and CP47 bind the core antenna chlorophylls, and three extrinsic proteins on the lumenal side stabilize the $\ce{Mn4CaO5}$ cluster (24.4). Within picoseconds P680* gives an electron to pheophytin; within hundreds of picoseconds it reaches $\mathrm{Q_A}$; $\mathrm{Q_A^-}$ reduces $\mathrm{Q_B}$ to the semiquinone and, after a second turnover, to the quinol, which takes up two protons from the stroma and leaves its site:

$$
2\,\mathrm{PQ_B} + 4\,\ce{H+_{stroma}} + 4\,\text{photons} + 2\,\ce{H2O} \to 2\,\mathrm{PQ_BH_2} + \ce{O2} + 4\,\ce{H+_{lumen}}. \tag{24.5}
$$

**Definition 24.3.2 (Plastoquinone)** **Plastoquinone** (PQ) is the lipid-soluble benzoquinone with a nonaprenyl side chain that carries two electrons and two protons from PSII to the cytochrome $b_6f$ complex in the thylakoid membrane, the counterpart of ubiquinone in mitochondria.

Many herbicides, among them DCMU (diuron) and atrazine, bind in the $\mathrm{Q_B}$ pocket of D1 and block electron transfer from $\mathrm{Q_A}$; resistance arises from point **mutations** in D1 (Ser264 to Gly). The radical chemistry of water oxidation damages D1 continually, and the protein is replaced every half hour or so in bright light, which makes the repair cycle of PSII an important determinant of photoinhibition (7.13).

### 24.3.4. The Cytochrome b₆f Complex and Plastocyanin

**Definition 24.3.3 (Cytochrome b₆f Complex)** The **cytochrome b₆f complex** is the dimeric plastoquinol:plastocyanin oxidoreductase of the thylakoid membrane, homologous to mitochondrial Complex III; each monomer contains cytochrome $b_6$ with hemes $b_{\mathrm{L}}$ and $b_{\mathrm{H}}$, an extra heme $c_{\mathrm{n}}$ (heme x), the Rieske [2Fe–2S] protein, cytochrome f and a chlorophyll a and a β-carotene of uncertain function, and it couples electron transfer to proton translocation by a Q cycle.

As in Complex III ([7.1.23](/7.1.23#sec-23.1.6)), plastoquinol is oxidized at the lumenal site: one electron goes through the Rieske center and cytochrome f to plastocyanin, the other through the b hemes back to a plastoquinone at the stromal site. For each pair of electrons passed to plastocyanin, four protons are released into the lumen (two from each plastoquinol in the full Q cycle), so per $\ce{O2}$ (four electrons) up to eight protons enter the lumen at $b_6f$ and four from water oxidation: twelve in all. Because the lumen is thin, these protons change its pH strongly: in illuminated chloroplasts the stroma is near pH 8 and the lumen reaches pH 5–6.

**Definition 24.3.4 (Plastocyanin)** **Plastocyanin** (PC) is a small soluble blue copper protein of the thylakoid lumen ($\ce{Cu^2+}/\ce{Cu+}$, $E_{\mathrm{m}} \approx +0.37\,\mathrm{V}$) that carries single electrons from cytochrome f to P700⁺, the role of cytochrome c in mitochondria; many cyanobacteria and algae use cytochrome $c_6$ instead, especially when copper is scarce.

### 24.3.5. Photosystem I

PSI of plants is a monomer of the core complex (PsaA and PsaB, which bind P700, the electron acceptors and about 90 antenna chlorophylls), with about 12 smaller subunits and the LHCI belt; in cyanobacteria it is a trimer. P700* gives an electron to $\mathrm{A_0}$, a chlorophyll a (the counterpart of pheophytin in PSII), then to $\mathrm{A_1}$, a phylloquinone (**vitamin** $\mathrm{K_1}$), and through the [4Fe–4S] clusters $\mathrm{F_X}$, $\mathrm{F_A}$ and $\mathrm{F_B}$ to ferredoxin on the stromal side. P700⁺ is reduced by plastocyanin. Ferredoxin, a soluble [2Fe–2S] protein ($E_{\mathrm{m}} \approx -0.42\,\mathrm{V}$), reduces $\ce{NADP+}$ through the **flavoprotein** ferredoxin–$\ce{NADP+}$ reductase (FNR), which collects two electrons on its **FAD** from two ferredoxins and transfers them as a hydride:

$$
2\,\mathrm{Fd_{red}} + \ce{NADP+} + \ce{H+} \to 2\,\mathrm{Fd_{ox}} + \ce{NADPH}. \tag{24.6}
$$
Ferredoxin also supplies electrons to the **thioredoxin** system that switches on the Calvin cycle in light ([7.1.25](/7.1.25)), to nitrite and sulfite reductases, and to **fatty acid** **desaturases**: it is the hub of reductive **metabolism** in the chloroplast.

### 24.3.6. Lateral Heterogeneity and State Transitions

The two photosystems are not neighbors. PSII and LHCII are concentrated in the appressed membranes of the grana, PSI and ATP synthase in the unstacked stromal thylakoids and the margins of the grana, where they have access to the stroma (ADP, $\ce{NADP+}$), and the cytochrome $b_6f$ complex is distributed in both; plastoquinol and plastocyanin carry electrons between them. The separation keeps the excitation of PSII, whose special pair absorbs at higher energy, from spilling over to PSI. The distribution of the antenna between the photosystems is adjusted to the light. When PSII is excited faster than PSI (state 1, light rich in blue or red), plastoquinol accumulates and activates, through the $b_6f$ complex, a **protein kinase** (STN7) that phosphorylates a Thr **residue** of LHCII; phosphorylated LHCII leaves the grana and associates with PSI (state 2), and the transfer of excitation to PSI increases. When PSI is excited faster (far-red light), the pool becomes oxidized and a phosphatase reverses the change. State transitions are an example of signaling by the redox state of a metabolite pool, and are most pronounced in algae.

### 24.3.7. Cyclic Electron Flow

**Definition 24.3.5 (Cyclic Electron Flow)** In **cyclic electron flow**, electrons from ferredoxin reduced by PSI return to the plastoquinone pool (through the PGR5–PGRL1 pathway or the NDH complex, a relative of Complex I) and through the cytochrome $b_6f$ complex and plastocyanin back to P700, so that PSI and $b_6f$ pump protons and ATP is made without water oxidation or NADPH formation.

Cyclic flow balances the products of the light reactions with the needs of the cell. Linear flow produces 12 protons per two NADPH (Eq. (24.7) below), enough for about 2.6 ATP with a $c_{14}$ ring; the Calvin cycle needs 3 ATP per 2 NADPH, and other processes (protein synthesis, photorespiration, $\ce{CO2}$-concentrating mechanisms) need more. The extra ATP comes from cyclic flow, which is upregulated when the stroma is reduced and ATP is short; C4 plants, whose bundle-sheath chloroplasts need much ATP and little NADPH, rely on it heavily ([7.1.25](/7.1.25)).

![Linear electron flow and the proton circuit in the thylakoid membrane, stroma (N side) above and lumen (P side) below. PSII, with its LHCII antenna, oxidizes water at the oxygen-evolving complex on the lumenal side and reduces plastoquinone at the QB site with protons from the stroma; plastoquinol diffuses to the cytochrome b₆f complex, which oxidizes it at its lumenal site in a Q cycle and reduces plastocyanin (PC); PSI, with LHCI, passes the electrons through ferredoxin (Fd) to FNR, which reduces NADP⁺. Per O₂ evolved (four electrons): 4 H⁺ released by water oxidation and 8 H⁺ by plastoquinol oxidation into the lumen; protons are taken up from the stroma at the QB site, at the stromal site of b₆f and by FNR. Protons return through CF₀ of the chloroplast ATP synthase (c₁₄ ring: 14 H⁺ per 3 ATP), whose CF₁ head faces the stroma](./plots/thylakoid-complexes.py)

## 24.4. Water Splitting

### 24.4.1. The Oxygen-Evolving Complex

Water is a very poor electron donor ($E'^{\circ} = +0.82\,\mathrm{V}$), and four electrons must be removed from two water molecules to release one $\ce{O2}$ without liberating the dangerous partially oxidized intermediates (hydroxyl radical, peroxide). PSII solves both problems. P680⁺, with $E_{\mathrm{m}} \approx +1.2\,\mathrm{V}$, is the strongest oxidant known in biology; it is reduced within nanoseconds by a Tyr residue of D1 ($\mathrm{Tyr_Z}$, Tyr161), which loses an electron and a proton to become a neutral tyrosyl radical; $\mathrm{Tyr_Z^{\bullet}}$ in turn oxidizes a metal cluster that accumulates oxidizing equivalents one at a time.

**Definition 24.4.1 (Oxygen-Evolving Complex)** The **oxygen-evolving complex** (water-oxidizing complex) of PSII consists of the $\ce{Mn4CaO5}$ cluster on the lumenal side of D1, with its protein ligands, bound water molecules and chloride, and the extrinsic proteins that shield it; it stores four oxidizing equivalents produced by four successive photochemical turnovers and uses them to oxidize two water molecules to $\ce{O2}$ and four protons, which are released into the lumen.

The structure of the cluster was resolved at 1.9 Å in 2011 (Yasufumi Umena, Jian-Ren Shen, Nobuo Kamiya and colleagues): three Mn and one Ca, bridged by four oxygens, form a distorted cube, and the fourth Mn is attached outside, with another oxygen bridge, like the back of a chair. Four water molecules are bound, two to the outer Mn and two to Ca. The emergence of this catalyst in the ancestors of cyanobacteria, more than 2.5 billion years ago, gave life an unlimited electron donor and, as a waste product, the oxygen that accumulated in the atmosphere in the Great Oxidation Event about 2.4 billion years ago and made aerobic respiration, and complex life, possible.

### 24.4.2. The Kok Cycle

Pierre Joliot showed in 1969 that dark-adapted chloroplasts given a series of short saturating flashes evolve almost no $\ce{O2}$ on the first two flashes, a maximum on the third, and then oscillate with a period of four, damped after a few cycles. Bessel Kok explained the pattern in 1970.

**Definition 24.4.2 (Kok Cycle)** In the **Kok cycle** (S-state cycle) the oxygen-evolving complex passes through five oxidation states $\mathrm{S_0}$ to $\mathrm{S_4}$; each photochemical turnover of PSII advances it by one state ($\mathrm{S}_n \to \mathrm{S}_{n+1}$), and $\mathrm{S_4}$ decays spontaneously to $\mathrm{S_0}$ with release of $\ce{O2}$. In the dark the complex relaxes to $\mathrm{S_1}$ (about three quarters of the centers) and $\mathrm{S_0}$.

Because the dark-stable state is $\mathrm{S_1}$, the third flash produces $\mathrm{S_4}$ and $\ce{O2}$, and every fourth flash after it. Not every flash advances every center: some fail ("misses", probability α ≈ 0.1) and a few advance twice during one flash ("double hits", β), so the population dephases and the oscillation damps toward the average yield. Protons are released in the pattern 1, 0, 1, 2 for the transitions $\mathrm{S_0} \to \mathrm{S_1} \to \mathrm{S_2} \to \mathrm{S_3} \to \mathrm{S_0}$; the electron and proton removals alternate so that the cluster does not accumulate charge, which would raise the potential needed for each step. Serial femtosecond crystallography with X-ray free-electron lasers has caught the cluster in each S state; in $\mathrm{S_3}$ an additional oxygen (from a water) is bound to Mn1 next to O5, and the O–O bond is thought to form between them in the transient $\mathrm{S_4}$ state, but the exact mechanism is still being established.

![The Kok cycle. A: each photochemical turnover of PSII (wavy arrows) removes one electron from the Mn₄CaO₅ cluster through Tyr Z and advances it by one S state; O₂ is released in the fast S₄ → S₀ transition, and protons are released into the lumen in the pattern 1, 0, 1, 2. The dark-stable state is S₁. B: O₂ evolved per flash in a train of saturating flashes given to dark-adapted thylakoids (25% S₀, 75% S₁), simulated with the Kok model: on each flash a center advances one state with probability 1 − α − β, fails with probability α = 0.10 (miss) or advances two states with probability β = 0.04 (double hit); O₂ is released by centers passing from S₃ (or, by a double hit, from S₂) to S₀. Without misses and double hits (red dots) the yield would be zero except on flashes 3, 7, 11, … and 4, 8, 12, …; misses dephase the population and the oscillation of period four damps to the steady-state yield](./plots/kok-cycle.py)

The Kok model is a Markov chain with four states. With the population vector $\boldsymbol{s} = (s_0, s_1, s_2, s_3)^{\mathsf T}$, each flash multiplies it by a transition matrix $M$ whose columns contain $\alpha$ on the diagonal, $1 - \alpha - \beta$ one state ahead and $\beta$ two states ahead; the oxygen yield of flash $n$ is $Y_n = (1 - \alpha - \beta)s_3 + \beta(s_2 + s_3)$. $M$ has the eigenvalue 1 (the steady state, $s_k = 1/4$) and three others of modulus less than 1, which set the damping and the period; fitting $\alpha$ and $\beta$ to measured flash yields is a standard analysis in photosynthesis research, and the eigenvalue analysis is that of [2.1](/2.1) and [3.1](/3.1).

## 24.5. Photophosphorylation

### 24.5.1. A Proton Gradient Couples Electron Flow to ATP Synthesis

**Definition 24.5.1 (Photophosphorylation)** **Photophosphorylation** is the synthesis of ATP from ADP and $\mathrm{P_i}$ driven by light-induced electron flow, coupled through a transmembrane proton gradient generated by photosynthetic electron-transfer chains; it is noncyclic when coupled to linear electron flow from water to $\ce{NADP+}$ and cyclic when coupled to cyclic electron flow around PSI.

The chemiosmotic mechanism ([7.1.23](/7.1.23#sec-23.2.2)) was demonstrated with chloroplasts before it was accepted for mitochondria. In André Jagendorf's "acid bath" experiment (1966), thylakoids were equilibrated in the dark at pH 4, so that the lumen became acidic, and then transferred to a medium at pH 8 containing ADP and $\mathrm{P_i}$: they made a burst of ATP in the dark, driven by the imposed pH gradient alone. **Uncouplers** abolish photophosphorylation without stopping electron flow, as in mitochondria.

In illuminated thylakoids the proton-motive force is stored mainly as a pH difference: the thylakoid membrane is permeable to $\ce{Cl-}$ and $\ce{Mg^2+}$, whose movements collapse most of the membrane potential. Lehninger gives $\Delta\mathrm{pH} \approx 3$ (stroma 8, lumen 5) and $\Delta\tilde\mu_{\mathrm{H^+}} \approx 17\,\mathrm{kJ\,mol^{-1}}$ (Eq. (23.5) of [7.1.23](/7.1.23#sec-23.2.2)); measurements in intact leaves suggest that a lumen pH below about 5.8 would damage the oxygen-evolving complex and the plastocyanin site, and that in steady light a part of the proton-motive force is kept as $\Delta\varphi$, with the partition regulated by **ion channels**.

### 24.5.2. Stoichiometry

Twelve protons enter the lumen per $\ce{O2}$ (24.3.4). The chloroplast ATP synthase has a ring of 14 c subunits, so $14/3 \approx 4.7$ protons pass for each ATP (transport costs do not arise, because ATP is made in the stroma where it is used), giving $12/4.67 \approx 2.6$ ATP per $\ce{O2}$; Lehninger's summary equation rounds this to three:

$$
2\,\ce{H2O} + 8\,\text{photons} + 2\,\ce{NADP+} + {\sim}3\,\ce{ADP} + {\sim}3\,\mathrm{P_i} \to \ce{O2} + {\sim}3\,\ce{ATP} + 2\,\ce{NADPH}. \tag{24.7}
$$

**Example 24.5.1** The energy efficiency of the light reactions under ideal conditions: eight photons of 680 nm carry $8 \times 176 = 1408\,\mathrm{kJ}$. They produce two NADPH from two water molecules, $\Delta_{\mathrm{r}}G'^{\circ} = -zF\Delta E'^{\circ} = 4 \times 96.5 \times 1.14 = +440\,\mathrm{kJ}$, and about 2.6 ATP, each worth about $50\,\mathrm{kJ}$ in the cell, $130\,\mathrm{kJ}$. About $570/1408 \approx 40\%$ of the absorbed light energy is conserved. Relative to the whole solar spectrum, most of which is not absorbed or is absorbed at wavelengths shorter than needed (the excess energy of a blue photon is lost as heat in the antenna), and including carbon fixation and photorespiration, the maximal efficiency of converting sunlight to biomass is about 4.6% for C3 and 6% for C4 plants, and crops in the field achieve 1–2% (7.13).

### 24.5.3. A Universal Mechanism of ATP Synthesis

The chloroplast ATP synthase ($\mathrm{CF_oCF_1}$) is homologous to the mitochondrial and bacterial enzymes in subunit composition, structure and mechanism: ADP and $\mathrm{P_i}$ condense on the enzyme surface with $\Delta G'^{\circ} \approx 0$, protons flowing through $\mathrm{CF_o}$ turn the c ring and the γ subunit, and binding changes in the three β subunits release ATP ([7.1.23](/7.1.23#sec-23.3.3)). A disulfide bond in its γ subunit, reduced by thioredoxin in light, activates it, so that the enzyme does not hydrolyze ATP in the dark. The orientation of the synthase relative to the proton gradient is the same in all coupling membranes: $\mathrm{F_1}$ sits on the N side, protons flow from P to N, and ATP is made in the matrix of mitochondria, the stroma of chloroplasts and the cytosol of bacteria. Protons are pumped out of mitochondria and bacteria but into the thylakoid lumen; topologically, the lumen corresponds to the intermembrane space and the bacterial periplasm.

Cyanobacteria, which carry out both photosynthesis and respiration in their thylakoid membranes, share three components between the two processes: the cytochrome $b_6f$ complex, which oxidizes plastoquinol from PSII and also quinol from respiratory dehydrogenases; cytochrome $c_6$, which reduces both PSI and the respiratory **cytochrome oxidase**; and ATP synthase. The two photosystems of oxygenic photosynthesis appear to have combined the type II reaction center of a purple-bacterium-like ancestor with the type I center of a green-sulfur-bacterium-like one; chloroplasts arose from a cyanobacterium engulfed by a eukaryote about 1.5 billion years ago, and they keep a small **genome** (about 120 **genes** in plants, including those for D1 and the large subunit of **rubisco**) and their own ribosomes.

### 24.5.4. Oxidative Phosphorylation and Photophosphorylation Compared

| Feature | Oxidative phosphorylation | Photophosphorylation |
|---|---|---|
| Membrane | inner mitochondrial membrane (bacterial plasma membrane) | thylakoid membrane (cyanobacterial thylakoids) |
| Source of electrons | NADH, $\ce{FADH2}$ (fuel oxidation) | $\ce{H2O}$ (or $\ce{H2S}$, organic donors in bacteria) |
| Energy that drives electron flow | free energy of oxidation: $\Delta E'^{\circ} = +1.14\,\mathrm{V}$ | light: two photons per electron lift it against $\Delta E'^{\circ} = -1.14\,\mathrm{V}$ |
| Final electron acceptor | $\ce{O2}$ (reduced to $\ce{H2O}$) | $\ce{NADP+}$ (water oxidized to $\ce{O2}$) |
| Mobile carriers | **ubiquinone**, cytochrome c | plastoquinone, plastocyanin, ferredoxin |
| Proton-pumping quinol oxidase | Complex III ($bc_1$, Q cycle) | cytochrome $b_6f$ (Q cycle) |
| Direction of proton pumping | matrix → intermembrane space | stroma → lumen |
| Proton-motive force | mostly $\Delta\varphi$ (0.15–0.2 V), ΔpH ≈ 0.75 | mostly ΔpH (2–3), small $\Delta\varphi$ |
| ATP synthase | $\mathrm{F_oF_1}$, $c_8$ in animals, 3.7 H⁺/ATP with transport | $\mathrm{CF_oCF_1}$, $c_{14}$, 4.7 H⁺/ATP |
| Products | ATP (and $\ce{H2O}$) | ATP and NADPH (and $\ce{O2}$) |

## Summary

The pathway card of the light reactions ([7.1.16](/7.1.16#sec-16.1.3)):

| Field | Light reactions of oxygenic photosynthesis |
|---|---|
| Location | thylakoid membranes of chloroplasts (grana: PSII, LHCII; stroma lamellae: PSI, ATP synthase); cyanobacterial thylakoids |
| Net reaction | 2 $\ce{H2O}$ + 8 photons + 2 $\ce{NADP+}$ + ~3 ADP + ~3 $\mathrm{P_i}$ → $\ce{O2}$ + ~3 ATP + 2 NADPH (Eq. (24.7)) |
| Energy account | 1 photon per e⁻ per photosystem; 12 H⁺ per $\ce{O2}$; 14 H⁺ per 3 ATP (c₁₄); ≈ 2.6 ATP per 2 NADPH; ~40% of absorbed red light conserved (Example 24.5.1) |
| Committed and regulated steps | charge separation in PSII and PSI (quantum yield ≈ 1, Example 24.2.2); plastoquinol oxidation at $b_6f$ is the slowest step of linear flow |
| Activators | light; reduced thioredoxin (activates CF₁ and Calvin-cycle enzymes) |
| Inhibitors | DCMU, atrazine ($\mathrm{Q_B}$ site); paraquat diverts electrons from PSI to $\ce{O2}$; uncouplers |
| Covalent, hormonal and transcriptional control | LHCII phosphorylation (STN7) in state transitions; cyclic electron flow; nonphotochemical quenching (7.13); D1 repair cycle |
| Opposing pathway | respiration and oxidative phosphorylation, which reverse the overall reaction and share homologous components |
| **Coenzymes** (vitamins) | chlorophylls, carotenoids, plastoquinone, phylloquinone (vitamin $\mathrm{K_1}$), hemes, Fe–S, Cu (plastocyanin), Mn₄CaO₅, FAD (FNR) |
| Diseases and drugs | herbicides (triazines, ureas, paraquat); carotenoid-deficient mutants photobleach |

| Topic | Key points |
|---|---|
| Overview (Definition 24.1.1) | light reactions + carbon assimilation; 2H₂D + CO₂ → (CH₂O) + H₂O + 2D; O₂ from water (¹⁸O); Hill reaction |
| Pigments (Definitions 24.2.1, 24.2.2) | chlorophyll a and b (Mg chlorin, phytol; 430/662 nm), bacteriochlorophylls; carotenoids (light harvesting and photoprotection), phycobilins and phycobilisomes; action spectrum ≈ combined absorption |
| Antenna (Definition 24.2.3) | LHCII; Förster exciton transfer funneled to the special pair; Φ ≈ 0.96–0.99 (Example 24.2.2) |
| Reaction centers | type II (Pheo–quinone; purple bacteria, PSII) and type I (Fe–S; green sulfur bacteria, PSI); bacterial cyclic flow; 1988 Nobel Prize |
| Z scheme (Definition 24.3.1) | red drop and enhancement; PSII → PQ (Definition 24.3.2) → $b_6f$ (Definition 24.3.3, Q cycle) → PC (Definition 24.3.4) → PSI → Fd → FNR → NADPH; 8 photons per O₂ |
| Regulation | lateral heterogeneity; state transitions by LHCII phosphorylation; cyclic electron flow (Definition 24.3.5) to raise ATP/NADPH |
| Water splitting (Definitions 24.4.1, 24.4.2) | P680⁺ (+1.2 V) → Tyr Z → Mn₄CaO₅; S₀–S₄, period-four O₂ yield, dark-stable S₁; H⁺ pattern 1, 0, 1, 2 |
| Photophosphorylation (Definition 24.5.1) | Jagendorf acid bath; pmf mainly ΔpH; CF₀CF₁, c₁₄; same orientation as mitochondria (F₁ on N side) |

## Questions

1. Calculate the energy of a mole of photons at 450 nm and at 700 nm. Why does photosynthesis work as well with blue light, absorbed by chlorophyll and carotenoids, as with red light, although a blue photon carries more energy?

   **Answer** $119\,627/450 = 266\,\mathrm{kJ\,mol^{-1}}$ and $119\,627/700 = 171\,\mathrm{kJ\,mol^{-1}}$. An excited chlorophyll relaxes within femtoseconds to picoseconds from its higher excited state (Soret, $S_2$) to the lowest one ($S_1$, corresponding to red absorption) by internal conversion, and excitation from carotenoids is passed to the $S_1$ state of chlorophyll; only this lowest excited state drives photochemistry. Each photon, whatever its wavelength, delivers one excitation of about 1.8 eV to the reaction center; the excess energy of the blue photon is lost as heat. Photosynthesis therefore counts photons, not energy, and its quantum yield per absorbed photon is similar in the blue and the red (slightly lower in the blue because transfer from carotenoids is less than 100% efficient).

2. DCMU blocks electron transfer from $\mathrm{Q_A}$ to $\mathrm{Q_B}$. Predict its effects on $\ce{O2}$ evolution, on the redox state of P700, on chlorophyll fluorescence and on cyclic photophosphorylation.

   **Answer** Linear flow stops, so $\ce{O2}$ evolution stops (after one turnover). P700 becomes oxidized in the light, because PSI continues to send electrons to ferredoxin while no electrons arrive from PSII. Chlorophyll fluorescence rises to its maximum: with $\mathrm{Q_A}$ reduced the reaction centers of PSII are closed and the excitation cannot be used photochemically (Example 24.2.2). Cyclic electron flow around PSI, which does not involve PSII, continues and still makes ATP (it is often studied in the presence of DCMU with far-red light).

3. In Jagendorf's experiment, thylakoids equilibrated at pH 4 were transferred to pH 8. Estimate the maximal free energy per mole of protons available from this gradient at $25\,^\circ\mathrm{C}$ and the minimal number of protons needed per ATP if the **phosphorylation potential** in the medium is $+45\,\mathrm{kJ\,mol^{-1}}$. Why is the ATP yield limited?

   **Answer** $\Delta\tilde\mu_{\mathrm{H^+}} = 2.303RT\,\Delta\mathrm{pH} = 5.71 \times 4 = 22.8\,\mathrm{kJ\,mol^{-1}}$ (no membrane potential), so at least $45/22.8 = 2$ protons per ATP; the c₁₄ synthase uses 4.7, comfortably below the available free energy. The yield is limited by the number of protons stored in the lumen (and bound to buffering groups): the gradient decays as protons flow out, and no electron flow regenerates it in the dark.

4. Using the Z scheme, explain why two photosystems are needed in oxygenic photosynthesis, whereas purple bacteria manage with one.

   **Answer** Oxygenic photosynthesis must take electrons from water (+0.82 V), which requires an oxidant more positive than +1 V (P680⁺, +1.2 V), and deliver them to $\ce{NADP+}$ (−0.32 V), which requires a reductant more negative than about −0.4 V (reduced Fd, from P700*, about −1.3 V). The span from +1.2 to −1.3 V (2.5 V) exceeds the energy of a single red photon (1.8 eV), the more so because each charge separation must be stabilized by a few steps that lose energy. Two photons per electron in series solve the problem, and the downhill segment between them is used for proton pumping. Purple bacteria need neither: their donors (cytochrome $c_2$ in a cycle, or $\ce{H2S}$ and organic acids) are more reducing than water, and they do not make NAD(P)H directly; they run cyclic flow for ATP and make NADH by reverse electron flow at the expense of the proton-motive force.

5. A train of flashes is given to chloroplasts that had been preilluminated with one flash and then kept in the dark for 1 second. On which flash do you expect the first maximum of $\ce{O2}$ evolution? What if they had been kept in the dark for 10 minutes instead?

   **Answer** One preflash converts most $\mathrm{S_1}$ to $\mathrm{S_2}$ (and $\mathrm{S_0}$ to $\mathrm{S_1}$). After 1 second, too short for the decay of $\mathrm{S_2}$ (seconds to minutes) and $\mathrm{S_3}$, the population is mostly $\mathrm{S_2}$, so the maximum moves to the second flash of the new train (S₂ → S₃ → S₄). After 10 minutes in the dark, $\mathrm{S_2}$ and $\mathrm{S_3}$ have relaxed back to $\mathrm{S_1}$ (and $\mathrm{S_0}$ is slowly oxidized to $\mathrm{S_1}$ by $\mathrm{Tyr_D}$), and the maximum is again on the third flash. Such experiments established that $\mathrm{S_2}$ and $\mathrm{S_3}$ are unstable in the dark and $\mathrm{S_1}$ is stable.

6. (Open question) Some cyanobacteria grown in far-red light synthesize chlorophylls d and f, which absorb at 710–750 nm, and incorporate them into PSII. What does this imply for the energetics of water oxidation, and what experiments would test whether such PSII centers are less efficient or less protected?

   **Answer** Outline: a 740-nm photon carries 1.68 eV instead of 1.82 eV at 680 nm, about 0.14 eV less, yet the potential needed to oxidize water through P680⁺/Tyr Z is unchanged; the energy margin of the charge separation and of the stabilizing steps must therefore be smaller, which could increase charge recombination (and triplet formation, risking singlet oxygen) or slow the forward reactions. Tests: measure the quantum yield of $\ce{O2}$ evolution and the flash-oxygen pattern (misses, Kok model) in far-red-grown and white-light-grown cells; compare the rates of charge recombination by delayed fluorescence and thermoluminescence; determine the midpoint potentials of Pheo and $\mathrm{Q_A}$ and the location of the far-red chlorophyll (antenna or primary donor) by spectroscopy and cryo-EM; and measure photodamage (D1 turnover, singlet oxygen probes) under high light. Such organisms show that the "red limit" of oxygenic photosynthesis is not absolute, an issue relevant for engineering crops to use more of the solar spectrum.
