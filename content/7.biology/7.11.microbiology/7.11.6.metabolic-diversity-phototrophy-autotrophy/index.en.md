---
title: "Metabolic Diversity I: Phototrophy, Autotrophy and Nitrogen Fixation"
description: How bacteria and archaea harvest light with chlorophyll-based and rhodopsin-based systems, the two types of reaction center, the six pathways of CO₂ fixation and the microbiology of nitrogen fixation.
---

The previous chapter treated the energy metabolism that microorganisms share with animals: the oxidation of organic compounds by fermentation and respiration. This chapter and the next turn to the metabolisms that are found only, or mainly, in bacteria and archaea, and that make them the engines of the biogeochemical cycles. Here we follow the energy of light and the assimilation of the two gases that every cell needs in reduced form, $\ce{CO2}$ and $\ce{N2}$. The biochemistry of oxygenic photosynthesis, the Calvin cycle and nitrogenase has been worked out in [7.1.24](/7.1.24), [7.1.25](/7.1.25) and [7.1.27](/7.1.27), and the physics of light harvesting and electron transfer in [7.6.18](/7.6.18); we link to them and concentrate on what is distinctively microbial: the variety of pigments and reaction centers, photosynthesis without oxygen, light-driven proton pumps, five autotrophic pathways that plants do not have, and the ecology of the organisms that fix nitrogen. The evolutionary history of these inventions, in particular the rise of oxygen, is told in [7.10.27](/7.10.27#sec-27.5.3). The next chapter, [7.11.7](/7.11.7), treats the chemical counterparts: energy from inorganic electron donors, respiration with acceptors other than oxygen, and methane.

## 6.1. Phototrophy

### 6.1.1. Two Ways to Use Light

A **phototroph** converts the energy of light into chemical energy. Two unrelated molecular solutions exist. In chlorophyll-based phototrophy, light excites a chlorophyll in a reaction center, the excited pigment gives away an electron, and the electron passes through a membrane-bound transport chain that builds up a **proton-motive force**; the same chain can also supply electrons for biosynthesis. In rhodopsin-based phototrophy, light isomerizes a retinal bound to a membrane protein, which pumps one proton per photon; there is no electron transfer at all (6.4).

Chlorophyll-based **photosynthesis** has two forms, distinguished by the electron donor.

**Definition 6.1.1 (Anoxygenic and Oxygenic Photosynthesis)** In **oxygenic photosynthesis** (cyanobacteria and the chloroplasts of algae and plants) water is the electron donor and $\ce{O2}$ is released; two reaction centers act in series. In **anoxygenic photosynthesis** (all other phototrophic bacteria) the electron donor is a reduced compound other than water, such as $\ce{H2S}$, $\ce{S^0}$, thiosulfate, $\ce{H2}$, $\ce{Fe^2+}$ or an organic compound, no $\ce{O2}$ is formed, and a single type of reaction center is used.

Cornelis van Niel, studying purple and green sulfur bacteria in the 1930s, recognized that the two forms are variants of one reaction and that the $\ce{O2}$ of plants must therefore come from water rather than from $\ce{CO2}$:

**Formula 6.1.1 (van Niel's Equation)** For an electron donor $\ce{H2A}$,

$$
\ce{CO2 + 2 H2A ->[light] (CH2O) + H2O + 2 A},
$$
with $\ce{H2A} = \ce{H2O}$ (so that $2\,\ce{A} = \ce{O2}$) in oxygenic and, for example, $\ce{H2A} = \ce{H2S}$ ($\ce{A} = \ce{S}$) in anoxygenic photosynthesis.

Chlorophyll-based phototrophy is known from seven bacterial phyla with cultured representatives (and from an eighth, Eremiobacterota, known so far only from metagenomes) and from no archaea. Throughout this course phyla are named with the current names ending in *-ota*; the older names are given at first mention.

| Group | Phylum | Reaction center | Main pigments | Typical electron donors | CO₂ fixation |
|---|---|---|---|---|---|
| Cyanobacteria | Cyanobacteriota | type I + type II (PSI, PSII) | chlorophyll *a* (*b*, *d*, *f* in some), phycobilins | $\ce{H2O}$ (some also $\ce{H2S}$) | Calvin cycle |
| Purple sulfur bacteria | Pseudomonadota (formerly Proteobacteria), Gammaproteobacteria | type II | bacteriochlorophyll *a* or *b* | $\ce{H2S}$, $\ce{S^0}$ (S⁰ stored inside the cell) | Calvin cycle |
| Purple nonsulfur bacteria | Pseudomonadota (Alpha-, Betaproteobacteria) | type II | bacteriochlorophyll *a* or *b* | organic compounds, $\ce{H2}$, low $\ce{H2S}$, $\ce{Fe^2+}$ | Calvin cycle (usually photoheterotrophs) |
| Green sulfur bacteria | Chlorobiota (formerly Chlorobi) | type I | bacteriochlorophyll *c*, *d* or *e* in chlorosomes | $\ce{H2S}$, $\ce{S^0}$ (S⁰ outside the cell), $\ce{H2}$, $\ce{Fe^2+}$ | reverse citric acid cycle |
| Green nonsulfur bacteria (filamentous anoxygenic phototrophs) | Chloroflexota (formerly Chloroflexi) | type II | bacteriochlorophyll *a*; *c* in chlorosomes | organic compounds, $\ce{H2}$, $\ce{H2S}$ | 3-hydroxypropionate bicycle |
| Heliobacteria | Bacillota (formerly Firmicutes) | type I | bacteriochlorophyll *g* | organic compounds (photoheterotrophs) | none |
| *Chloracidobacterium* | Acidobacteriota | type I | bacteriochlorophyll *a*, *c* | organic compounds | none |
| *Gemmatimonas phototrophica* | Gemmatimonadota | type II | bacteriochlorophyll *a* | organic compounds | none |

The distribution makes two points. First, anoxygenic phototrophs are phylogenetically scattered; the photosynthesis genes of the purple bacteria and of *Gemmatimonas* sit in a compact gene cluster that has evidently moved between phyla by **horizontal gene transfer**. Second, many phototrophs do not fix $\ce{CO2}$ with light but live as **photoheterotrophs**, using light for ATP and organic compounds for carbon.

### 6.1.2. Chlorophylls and Bacteriochlorophylls

All chlorophylls are magnesium tetrapyrroles related to heme ([7.1.24](/7.1.24#sec-24.2.2)), with a fifth (cyclopentanone) ring and a long hydrophobic alcohol that anchors them in membranes or in protein. Small changes in the substituents and in the saturation of the ring shift the absorption bands substantially.

**Definition 6.1.2 (Bacteriochlorophyll)** A **bacteriochlorophyll** (Bchl) is a chlorophyll of anoxygenic phototrophs. Bacteriochlorophylls *a*, *b* and *g* are bacteriochlorins (two of the four pyrrole rings are reduced), whose long-wavelength (Qy) band lies in the near infrared, 790–1040 nm in vivo; bacteriochlorophylls *c*, *d* and *e* are chlorins like chlorophyll *a* and absorb at 705–755 nm.

In living cells the absorption maxima are set as much by the protein environment and by pigment–pigment coupling as by the molecule itself: bacteriochlorophyll *a* dissolved in methanol absorbs at about 770 nm, but in the light-harvesting complexes of purple bacteria it absorbs at 800–890 nm, depending on the complex.

![In vivo absorption maxima of the photosynthetic pigments (schematic; band shapes and heights are illustrative, peak positions after Madigan et al. 2019). Chlorophyll *a* absorbs blue and red light and transmits green. The phycobiliproteins of cyanobacteria fill the green-to-orange gap (phycoerythrin 550 nm, phycocyanin 620 nm, allophycocyanin 650 nm) and the carotenoids the blue-green (450–550 nm). The bacteriochlorophylls of anoxygenic phototrophs absorb mostly beyond 700 nm: *a* at 805 and 870 nm in purple bacteria, *b* at 1020–1040 nm, *g* of heliobacteria at 788 nm, and the chlorosome pigments *c*, *d* and *e* of green sulfur bacteria at 705–755 nm, with blue (Soret) bands as well.](./plots/pigment-spectra.py)

### 6.1.3. Carotenoids, Phycobiliproteins and Phycobilisomes

Two further classes of **accessory pigments** widen the absorbed spectrum and protect the cell.

*Carotenoids* are long conjugated isoprenoids (40 carbons) embedded in the photosynthetic membranes of all phototrophs. They absorb at 400–550 nm, give purple bacteria their red, purple, brown or orange colours (a carotenoid-less mutant of *Rhodospirillum rubrum* is blue-green, the colour of bacteriochlorophyll *a* itself), and pass part of their excitation to the bacteriochlorophylls. Their main function, however, is photoprotection: they quench triplet bacteriochlorophyll and singlet oxygen ($\ce{^1O2}$), which would otherwise destroy the reaction centers in bright light. The particle-in-a-box picture of why a conjugated chain of this length absorbs blue light is developed in [7.6.18](/7.6.18#sec-18.2.1).

**Definition 6.1.3 (Phycobiliprotein)** A **phycobiliprotein** is a water-soluble protein of cyanobacteria, red algae and glaucophytes carrying covalently bound open-chain tetrapyrroles (bilins). The three main kinds are phycoerythrin (red, absorption maximum near 550 nm), phycocyanin (blue, near 620 nm) and allophycocyanin (near 650 nm).

**Definition 6.1.4 (Phycobilisome)** A **phycobilisome** is the light-harvesting antenna of cyanobacteria and red algae: a large complex of phycobiliproteins and linker proteins attached to the stromal (cytoplasmic) face of the thylakoid membrane, with a core of allophycocyanin next to the membrane and rods of phycocyanin and, outermost, phycoerythrin.

The arrangement is an energy funnel: excitation absorbed at shorter wavelength in the rods flows downhill, phycoerythrin → phycocyanin → allophycocyanin → chlorophyll *a* of photosystem II, with an overall efficiency above 90 percent. Because the phycobiliproteins absorb in the green and orange, where chlorophyll *a* does not, they let cyanobacteria grow in deep or turbid water where green light dominates.

### 6.1.4. Antennas, Membranes and Chlorosomes

Most of the pigment of a phototroph is not in the reaction center but in **light-harvesting complexes** that funnel excitation to it ([7.1.24](/7.1.24#sec-24.2.4)). Purple bacteria typically make two kinds: LH1 surrounds each reaction center as a ring of about 16 subunits, and peripheral LH2 rings (absorbing at 800 and 850 nm) transfer energy to LH1 (875 nm), which passes it to the special pair (870 nm), each step slightly downhill in energy. Under low light purple bacteria make more LH2 and more membrane. Their photosynthetic membranes are invaginations of the cytoplasmic membrane, either vesicles (chromatophores) or flat stacks (lamellae); cyanobacteria have separate thylakoid membranes, often in concentric layers under the cell membrane but without the grana of chloroplasts.

Green sulfur bacteria, green nonsulfur bacteria and *Chloracidobacterium* have a quite different antenna.

**Definition 6.1.5 (Chlorosome)** A **chlorosome** is an oblong antenna body appressed to the inner face of the cytoplasmic membrane of green sulfur bacteria, some green nonsulfur bacteria and *Chloracidobacterium*. It is bounded by a lipid monolayer and contains up to about 250 000 molecules of bacteriochlorophyll *c*, *d* or *e*, which are not bound to protein but self-assemble into tubular or lamellar aggregates; excitation reaches the reaction centers through a baseplate of bacteriochlorophyll *a*-protein and, in green sulfur bacteria, the FMO protein.

Because no protein is needed to hold each pigment, a chlorosome packs an enormous antenna per reaction center (thousands of bacteriochlorophylls, against a few tens in purple bacteria). Green sulfur bacteria can therefore grow at the lowest light intensities known for any phototroph: one strain was isolated from a deep-sea hydrothermal vent, where the only light is the faint geothermal glow, and they form the deepest phototrophic layers in stratified lakes.

### 6.1.5. Light Niches

Pigment diversity is the reason why several kinds of phototroph can share one habitat. In a stratified lake the upper, oxic water is occupied by cyanobacteria and algae; anoxygenic phototrophs need both light and reduced sulfur, which diffuses up from sulfate-reducing sediments, and so live below the oxycline in a layer only decimetres thick: purple sulfur bacteria above, green sulfur bacteria below. In microbial mats the same sequence is compressed into a few millimetres. What each layer receives depends on what the layers above have taken and, in water, on the absorption of water itself (Figure below).

![The light left for each layer (Beer–Lambert model with a flat surface spectrum; pigment absorption as in the previous figure). A: stratified lake. Water absorbs strongly beyond 700 nm (absorption coefficient about 2 m⁻¹ at 750–800 nm), and a cyanobacterial layer in the top 3 m removes the blue and red; below a few metres only blue-green light (450–570 nm) is left, so the purple and green sulfur bacteria of the hypolimnion depend on carotenoids and on the blue bands of their bacteriochlorophylls (the brown, bacteriochlorophyll *e*-containing green sulfur bacteria are typical of the deepest layers). B: microbial mat. Over millimetres water absorption is negligible: the cyanobacteria at the surface absorb the visible light, and the near infrared that passes through is absorbed by bacteriochlorophyll *a* of purple bacteria (800–900 nm) and bacteriochlorophyll *c* of green bacteria (about 750 nm) below them.](./plots/light-niches.py)

## 6.2. Anoxygenic Photosynthesis

### 6.2.1. Two Types of Reaction Center

All photochemical **reaction centers** share an architecture: a dimer of membrane proteins binds a special pair of (bacterio)chlorophylls near the periplasmic or lumenal side and two branches of electron carriers that cross the membrane ([7.6.18](/7.6.18#sec-18.4.1)). They differ in the terminal acceptors.

**Definition 6.2.1 (Type I and Type II Reaction Centers)** In a **type II reaction center** (quinone type) the electron from the special pair passes via bacteriopheophytin or pheophytin to two quinones, $\mathrm{Q_A}$ and $\mathrm{Q_B}$; $\mathrm{Q_B}$ takes up two electrons and two protons and leaves as quinol. In a **type I reaction center** (iron–sulfur type) the electron passes via chlorophyll and a quinone to iron–sulfur clusters ($\mathrm{F_X}$, $\mathrm{F_A}$, $\mathrm{F_B}$) and then to soluble ferredoxin. Photosystem II and the reaction centers of purple bacteria, Chloroflexota and *Gemmatimonas* are type II; photosystem I and the reaction centers of green sulfur bacteria, heliobacteria and *Chloracidobacterium* are type I.

The two types differ in what they can do. A type II center yields a quinol, whose $E'^{\circ}$ near 0 V is too positive to reduce $\ce{NAD+}$ ($-0.32\,\mathrm{V}$); a type I center reduces ferredoxin ($E'^{\circ} \approx -0.42\,\mathrm{V}$), which reduces $\ce{NAD(P)+}$ directly. Type II reaction centers are made of two different subunits (L and M in purple bacteria, D1 and D2 in PSII); the type I centers of green sulfur bacteria and heliobacteria are homodimers, which is thought to be the ancestral state.

### 6.2.2. Purple Bacteria: Cyclic Electron Flow

The reaction center of the purple bacterium *Blastochloris viridis* (formerly *Rhodopseudomonas viridis*) was the first membrane protein whose structure was determined at atomic resolution (Deisenhofer, Huber and Michel, 1985; Nobel Prize 1988); that of *Rhodobacter sphaeroides* followed soon after. It consists of the L and M subunits, which bind the cofactors, the H subunit on the cytoplasmic side and, in some species, a bound tetraheme cytochrome on the periplasmic side. The cofactors are a special pair of bacteriochlorophyll *a* (P870, named after its absorption maximum), two accessory bacteriochlorophylls, two bacteriopheophytins (bacteriochlorophyll without $\ce{Mg^2+}$), the quinones $\mathrm{Q_A}$ and $\mathrm{Q_B}$, a non-heme iron and a carotenoid; only one of the two branches carries electrons.

The sequence of events, with the time scales that make it efficient, is analysed in [7.6.18](/7.6.18#sec-18.4.1): excited P870 ($E'^{\circ}$ about $-1.0\,\mathrm{V}$ against about $+0.45\,\mathrm{V}$ in the ground state) reduces bacteriopheophytin within about 3 ps, which reduces $\mathrm{Q_A}$ within about 200 ps; $\mathrm{Q_A}$ reduces $\mathrm{Q_B}$ in microseconds. After two photons, $\mathrm{Q_BH_2}$ leaves the reaction center and joins the quinone pool. The quinol is oxidized by the cytochrome $bc_1$ complex, the same complex as in respiration, which by the **Q cycle** releases protons into the periplasm; cytochrome $c_2$, a small periplasmic carrier, returns the electron to $\ce{P870+}$.

Electrons thus travel in a closed loop: this is **cyclic electron flow**, and the ATP made by ATP synthase from the resulting proton-motive force is cyclic **photophosphorylation**. No electron donor is consumed, so a purple bacterium can make ATP from light alone; what it cannot do in this way is make NADH.

![Electron flow in the two kinds of anoxygenic phototroph on a scale of standard reduction potential (approximate values after Madigan et al. 2019). Left: in purple bacteria light converts P870 (about +0.45 V) into the strong donor P870* (about −1.0 V); electrons pass through bacteriochlorophyll (Bchl), bacteriopheophytin (Bph) and the quinones to the quinone pool (about 0 V), and back through cytochrome *bc*₁ and cytochrome *c*₂ (cyclic flow, which pumps protons). The quinone pool is more positive than NAD⁺/NADH (−0.32 V), so NADH is made by reverse electron transport at the expense of the proton-motive force; electrons from H₂S enter at the quinone pool. Right: in green sulfur bacteria the excited P840 (about −1.2 V) reduces chlorophyll *a* and iron–sulfur clusters that are more negative than ferredoxin (Fd, −0.42 V); ferredoxin reduces NAD⁺ and drives CO₂ fixation directly. Electrons from sulfide enter through menaquinone (MQ) and cytochrome *c*. Heliobacteria (P798, bacteriochlorophyll *g*) resemble the right panel.](./plots/anoxygenic-electron-flow.py)

### 6.2.3. Reverse Electron Transport

To grow autotrophically, a purple bacterium must reduce $\ce{NAD+}$, and the electrons that its reaction center delivers to the quinone pool are not reducing enough.

**Definition 6.2.2 (Reverse Electron Transport)** **Reverse electron transport** (reverse electron flow) is the energy-requiring transfer of electrons from a carrier of higher reduction potential to one of lower potential, against the direction of spontaneous flow, driven by the proton-motive force. Typically, quinol reduces $\ce{NAD+}$ through Complex I (NADH:quinone oxidoreductase) running backwards, with protons flowing into the cell.

**Example 6.2.1** How many protons does it cost to make one NADH from quinol? Take $E'^{\circ}(\mathrm{Q/QH_2}) \approx 0\,\mathrm{V}$ and $E'^{\circ}(\ce{NAD+}/\mathrm{NADH}) = -0.32\,\mathrm{V}$. Moving two electrons uphill by $0.32\,\mathrm{V}$ needs $\Delta_{\mathrm{r}}G'^{\circ} = zF\Delta E'^{\circ} = 2 \times 96.5 \times 0.32 \approx 62\,\mathrm{kJ\,mol^{-1}}$. A proton entering the cell across a proton-motive force of $\Delta p = 0.18\,\mathrm{V}$ releases $F\Delta p \approx 17\,\mathrm{kJ\,mol^{-1}}$, so at least four protons are needed per NADH; Complex I in reverse indeed translocates four. The same mechanism serves every chemolithotroph whose electron donor is more positive than $\ce{NAD+}$ ([7.11.7](/7.11.7)), and there the cost is much greater.

:::

Reducing power comes from external donors. In purple sulfur bacteria (*Chromatium*, *Allochromatium*, *Thiocapsa*, *Thiospirillum*), $\ce{H2S}$ is oxidized to elemental sulfur, which is stored as globules inside the cell (in the periplasm, in fact), and then to sulfate when sulfide runs out. The electrons enter at the cytochrome or quinone level and reach $\ce{NAD+}$ by reverse electron transport; $\ce{CO2}$ is fixed by the **Calvin cycle**. Purple nonsulfur bacteria (*Rhodospirillum*, *Rhodobacter*, *Rhodopseudomonas*) are the most metabolically versatile organisms known: in light and without oxygen they grow as photoheterotrophs on organic acids, alcohols, sugars or even aromatic compounds; with $\ce{H2}$ or low levels of sulfide they grow photoautotrophically; and in darkness most respire aerobically, $\ce{O2}$ repressing the synthesis of the photosynthetic apparatus. Nearly all of them fix nitrogen, and their light-driven, ATP-consuming nitrogenase makes them prolific $\ce{H2}$ producers (6.6.2).

### 6.2.4. Green Sulfur Bacteria and Heliobacteria

The green sulfur bacteria (*Chlorobium*, *Chlorobaculum*, *Prosthecochloris*) are a small, phylogenetically compact group of strictly anaerobic, nonmotile, obligate photoautotrophs. Their type I reaction center (P840) reduces iron–sulfur clusters at about $-0.55\,\mathrm{V}$ and then ferredoxin, so reducing power is made by light directly, without reverse electron transport; reduced ferredoxin is also the electron donor of two carboxylases of their **reverse citric acid cycle** (6.5.2). Electrons from sulfide (via sulfide:quinone oxidoreductase), thiosulfate or $\ce{H2}$ enter through menaquinone and cytochromes; sulfur is deposited outside the cells. Whether green sulfur bacteria also run cyclic electron flow is still debated; the evidence favours mainly noncyclic flow. With chlorosomes and high sulfide tolerance they occupy the deepest, most sulfidic and dimmest phototrophic layers. Some live as the epibionts of a motile, nonphototrophic central bacterium in two-membered consortia ("*Chlorochromatium aggregatum*"), in which the central cell swims towards light and sulfide carrying its phototrophic partners.

The heliobacteria (*Heliobacterium*, *Heliobacillus*) are the only phototrophic gram-positive bacteria. They are strictly anaerobic photoheterotrophs with the simplest known photosynthetic apparatus: a homodimeric type I reaction center (P798) containing bacteriochlorophyll *g*, no intracellular membranes and no light-harvesting antenna proteins. They form **endospores** with dipicolinic acid, like their *Bacillus* and *Clostridium* relatives, and fix nitrogen actively; they are common in rice paddy soils.

### 6.2.5. Filamentous Anoxygenic Phototrophs and Aerobic Phototrophs

*Chloroflexus aurantiacus*, the best-studied green nonsulfur bacterium, is a filamentous, gliding thermophile that forms orange layers under the cyanobacteria in hot-spring mats. Its photosynthetic apparatus is a hybrid: chlorosomes like a green sulfur bacterium but a type II reaction center like a purple bacterium, and therefore cyclic electron flow and reverse electron transport. It grows best photoheterotrophically, can grow photoautotrophically with $\ce{H2}$ or $\ce{H2S}$ using the **3-hydroxypropionate bicycle** (6.5.3), and respires aerobically in the dark. The mosaic of components is one of the strongest arguments that the photosynthetic genes have been exchanged between phyla.

Not all anoxygenic phototrophs are anaerobes.

**Definition 6.2.3 (Aerobic Anoxygenic Phototroph)** **Aerobic anoxygenic phototrophs** are obligately aerobic heterotrophic bacteria (mainly Alphaproteobacteria such as *Roseobacter* and *Erythrobacter*) that contain bacteriochlorophyll *a* and a type II reaction center and use light only as a supplementary energy source; they do not fix $\ce{CO2}$ and make their pigments in the dark.

They are abundant in the surface ocean (a few to about 10 percent of bacterioplankton cells, more in coastal waters), and together with the rhodopsin phototrophs (6.4) they show that much of the "heterotrophic" bacterioplankton supplements its energy budget with light.

### 6.2.6. Electron Donors and Photoferrotrophy

The electron donors of anoxygenic phototrophs range from sulfide ($\ce{S^0}/\ce{HS-}$, $-0.27\,\mathrm{V}$) and $\ce{H2}$ ($-0.41\,\mathrm{V}$) to ferrous iron, nitrite and even arsenite. Oxidation of $\ce{Fe^2+}$ in the light, photoferrotrophy, was discovered in purple and green bacteria in 1993 (Widdel and colleagues):

$$
\ce{4 Fe^2+ + CO2 + 11 H2O ->[light] (CH2O) + 4 Fe(OH)3 + 8 H+}.
$$
At neutral pH the $\ce{Fe(OH)3}/\ce{Fe^2+}$ couple is only slightly positive, so the electrons can enter the cytochrome chain. Photoferrotrophs are a candidate for the deposition of the banded iron formations of the Archean ocean before free oxygen existed.

Conversely, some cyanobacteria fall back on anoxygenic photosynthesis: *Oscillatoria limnetica*, from a sulfide-rich salt pond, switches off photosystem II in the presence of sulfide and oxidizes $\ce{H2S}$ to $\ce{S^0}$ with photosystem I alone, depositing sulfur outside its filaments.

### 6.2.7. The Evolution of the Reaction Centers

The two types of reaction center share a conserved core of five transmembrane helices around the cofactors and are certainly homologous, though their sequences have diverged beyond recognition and only the structures reveal the relationship. Oxygenic photosynthesis was the innovation of the cyanobacterial lineage, which (a) combined a type I and a type II center in one organism and linked them in series, and (b) evolved a type II center (PSII) oxidizing enough (about $+1.2\,\mathrm{V}$) to split water with the $\ce{Mn4CaO5}$ cluster ([7.1.24](/7.1.24#sec-24.4.1)). How the two types came to be in one cell is debated: either a single ancestral lineage had both and other phototrophs lost one (selective loss), or the genes were brought together by horizontal transfer (fusion). Anoxygenic photosynthesis is generally thought to be older; the geological record of the oxygenation of the Earth that followed is discussed in [7.10.27](/7.10.27#sec-27.5.3) (**Great Oxidation Event**).

## 6.3. Oxygenic Photosynthesis in Cyanobacteria

### 6.3.1. What Is Special about Cyanobacteria

The light reactions of **cyanobacteria** are those of chloroplasts, which descend from them: **photosystem II**, the **cytochrome b6f complex** and **photosystem I** in series (the **Z scheme**), linear and cyclic electron flow, and about 12 protons translocated per $\ce{O2}$ released ([7.1.24](/7.1.24#sec-24.3.2)). The microbial differences are in the membrane and the antenna:

- The thylakoids lie free in the cytoplasm and, unusually, carry both the photosynthetic and the respiratory electron transport chains, which share the plastoquinone pool and the cytochrome $b_6f$ complex; in the dark cyanobacteria respire glycogen through the same membrane.
- The main antenna is the phycobilisome, which is on the outside of the thylakoid and can move between the two photosystems (state transitions).
- Some lineages use other chlorophylls. *Prochlorococcus*, the smallest (about 0.6 µm) and most abundant photosynthetic organism in the oligotrophic ocean, has no phycobilisomes but divinyl chlorophylls *a* and *b*; *Acaryochloris marina* uses chlorophyll *d*, absorbing at about 710 nm, as its main pigment; and several cyanobacteria grown in far-red light synthesize chlorophylls *d* and *f* (discovered in 2010, absorbing up to about 740 nm) and modified photosystems, extending oxygenic photosynthesis beyond the 700 nm once thought to be its limit.

Together with *Synechococcus*, *Prochlorococcus* accounts for a large share of marine primary production; cyanobacteria as a whole are thought to contribute about a quarter of global net primary production, and the nitrogen fixers among them are the main source of new nitrogen in the tropical ocean (6.6.1).

### 6.3.2. Chromatic Acclimation

Cyanobacteria sense the colour of the light and adjust their antenna accordingly.

**Definition 6.3.1 (Chromatic Acclimation)** **Chromatic acclimation** (historically, complementary chromatic adaptation) is the change in the pigment composition of the phycobilisomes of a cyanobacterium with the spectrum of the available light: in green light the cells make phycoerythrin (red), in red light phycocyanin (blue-green), so that the antenna absorbs the light that is present.

In *Fremyella diplosiphon* (also known as *Tolypothrix* sp. PCC 7601), the classical model, the switch is controlled by RcaE, a phytochrome-like photoreceptor that is also a sensor kinase, through a two-component system that regulates the transcription of the phycoerythrin and phycocyanin operons. Cells grown in green light are red, cells grown in red light blue-green; the change takes about one generation. Other forms of acclimation exchange the bilins of existing phycocyanin rods (blue–green acclimation in marine *Synechococcus*) or replace the whole set of photosystem subunits in far-red light (6.3.1).

## 6.4. Rhodopsin Phototrophy

A second, completely independent form of phototrophy uses retinal proteins. Microbial rhodopsins (type 1 rhodopsins, unrelated in sequence to the visual rhodopsin of animals) are seven-helix membrane proteins with all-*trans*-retinal bound to a lysine as a protonated Schiff base; light isomerizes the retinal to 13-*cis*, and the protein returns to the dark state in a photocycle of a few milliseconds that moves one ion across the membrane ([7.6.18](/7.6.18#sec-18.5.1)).

The first to be found was **bacteriorhodopsin**, which forms the crystalline purple membrane of the haloarchaeon *Halobacterium salinarum* (Oesterhelt and Stoeckenius, 1971). It is an outward proton pump and allows these aerobic heterotrophs to make ATP in the light when $\ce{O2}$, which is poorly soluble in saturated brine, runs short. The same archaea have halorhodopsin, an inward chloride pump, and sensory rhodopsins that steer phototaxis.

**Definition 6.4.1 (Proteorhodopsin)** **Proteorhodopsin** is a light-driven outward proton pump of the bacteriorhodopsin family found in marine and freshwater bacteria (first, in 2000, in the genome of an uncultured marine gammaproteobacterium of the SAR86 clade); variants tuned to green light (about 525 nm) occur in surface waters and to blue light (about 490 nm) in deeper waters.

Metagenomic surveys later showed that genes for proteorhodopsin and its relatives occur in a large fraction of the bacteria and archaea of the sunlit ocean, including the SAR11 clade (*Pelagibacter*), Bacteroidota and marine archaea; the photosystem needs only the opsin gene and a few genes for retinal synthesis, so it spreads readily by horizontal transfer. In culture, light stimulates the growth of some proteorhodopsin-containing flavobacteria (*Dokdonia*) under carbon limitation, and in others it improves survival during starvation. Rhodopsin phototrophy and chlorophyll-based phototrophy compare as follows:

| | Chlorophyll-based | Rhodopsin-based |
|---|---|---|
| Pigment | (bacterio)chlorophylls, carotenoids | retinal |
| Primary event | charge separation, electron transfer | isomerization, ion pumping |
| Product | proton-motive force and reducing power | proton-motive force only |
| Protein cost | many proteins, cofactors, membranes | one protein (about 27 kDa) |
| Autotrophy with light | possible | not possible; cells are photoheterotrophs |

## 6.5. Autotrophy: The Six Pathways of CO₂ Fixation

An **autotroph** must reduce $\ce{CO2}$ to the level of cell material, which costs both ATP and electrons. Plants know a single solution, the Calvin cycle, but bacteria and archaea have at least six; the variety reflects the different redox environments in which autotrophy evolved and the oxygen sensitivity of the enzymes involved. A brief survey is given in [7.10.27](/7.10.27#sec-27.5.2); here we compare the pathways.

### 6.5.1. The Calvin Cycle and Carboxysomes

The **Calvin cycle** (reductive pentose phosphate cycle) is described in [7.1.25](/7.1.25#sec-25.1): **rubisco** carboxylates ribulose 1,5-bisphosphate, the 3-phosphoglycerate is reduced to triose phosphate, and phosphoribulokinase regenerates the acceptor, at a cost of 3 ATP and 2 NAD(P)H per $\ce{CO2}$ (18 ATP and 12 NAD(P)H per hexose). It is used by cyanobacteria, purple bacteria, most aerobic chemolithotrophs and a few archaea. Microbial rubiscos come in several forms: form I ($\mathrm{L_8S_8}$) of plants, cyanobacteria and many proteobacteria; form II (a dimer of large subunits only) of some purple bacteria and dinoflagellates, with a low specificity for $\ce{CO2}$ over $\ce{O2}$ ([7.1.25](/7.1.25#sec-25.3.2)); and form III of archaea, which functions in a nucleotide salvage pathway rather than in autotrophy.

Because rubisco is slow and does not discriminate well against $\ce{O2}$, many Calvin-cycle bacteria concentrate $\ce{CO2}$ around it. The **carboxysome**, a polyhedral protein shell about 100–150 nm across ([7.11.3](/7.11.3)), packages rubisco with carbonic anhydrase: bicarbonate accumulated by membrane transporters diffuses in, is converted to $\ce{CO2}$ inside, and the $\ce{CO2}$ is fixed before it can leak out. Cyanobacteria (with α- and β-carboxysomes) and many chemolithotrophs (*Halothiobacillus*, nitrifiers) have them; the pyrenoids of algae are the eukaryotic analogue ([7.1.25](/7.1.25#sec-25.4.3)).

### 6.5.2. The Reverse Citric Acid Cycle

**Definition 6.5.1 (Reverse Citric Acid Cycle)** The **reverse citric acid cycle** (reductive tricarboxylic acid cycle, rTCA) is a pathway of autotrophic $\ce{CO2}$ fixation that runs the citric acid cycle in the reductive direction: starting from oxaloacetate, two carboxylations driven by reduced ferredoxin (2-oxoglutarate:ferredoxin oxidoreductase, succinyl-CoA → 2-oxoglutarate; and, outside the cycle, pyruvate:ferredoxin oxidoreductase, acetyl-CoA → pyruvate) and one by NAD(P)H (isocitrate dehydrogenase) fix $\ce{CO2}$, fumarate reductase replaces succinate dehydrogenase, and ATP-citrate lyase cleaves citrate into acetyl-CoA and oxaloacetate.

One turn converts oxaloacetate plus two $\ce{CO2}$ into two oxaloacetate equivalents (citrate → acetyl-CoA + oxaloacetate), and acetyl-CoA plus a third $\ce{CO2}$ gives pyruvate. The cycle was discovered in the green sulfur bacterium *Chlorobium limicola* (Evans, Buchanan and Arnon, 1966) and also operates in Aquificota (*Hydrogenobacter*, *Aquifex*), in many Campylobacterota (formerly Epsilonproteobacteria, such as the deep-sea vent symbionts and *Sulfurimonas*) and in some Nitrospirota and Thermoproteota. Its 2-oxoacid:ferredoxin oxidoreductases are $\ce{O2}$-sensitive, so it is found in anaerobes and microaerophiles.

### 6.5.3. The 3-Hydroxypropionate Bicycle

**Definition 6.5.2 (3-Hydroxypropionate Bicycle)** The **3-hydroxypropionate bicycle** of *Chloroflexus* fixes bicarbonate with two biotin-dependent carboxylases, acetyl-CoA carboxylase and propionyl-CoA carboxylase. In the first cycle acetyl-CoA is carboxylated to malonyl-CoA, reduced via 3-hydroxypropionate to propionyl-CoA, carboxylated to methylmalonyl-CoA and converted via succinyl-CoA and malyl-CoA back to acetyl-CoA, releasing glyoxylate; the second cycle combines glyoxylate with propionyl-CoA and yields pyruvate, regenerating acetyl-CoA.

All its enzymes are $\ce{O2}$-tolerant and the carboxylases use bicarbonate, which is abundant at the alkaline pH of the hot springs where *Chloroflexus* lives; the price is a high ATP cost (Figure below). The bicycle is so far known only from the Chloroflexaceae.

### 6.5.4. Two Archaeal Cycles

Two further cycles were found in autotrophic archaea (Berg, Fuchs and colleagues, 2007–2008). Both start by carboxylating a C2 or C3 compound and pass through 4-hydroxybutyryl-CoA, whose dehydration by 4-hydroxybutyryl-CoA dehydratase is the characteristic radical step, before splitting into two acetyl-CoA.

- The 3-hydroxypropionate/4-hydroxybutyrate (3HP/4HB) cycle fixes two bicarbonate with acetyl-CoA/propionyl-CoA carboxylase. It operates in the aerobic, acidophilic Sulfolobales (*Metallosphaera*, *Sulfolobus*) and in the ammonia-oxidizing archaea of the Nitrososphaerota (formerly Thaumarchaeota), where a variant is the most energy-efficient aerobic autotrophic pathway known; because ammonia-oxidizing archaea are among the most abundant cells in the ocean, this cycle fixes a substantial amount of carbon in the dark ocean.
- The dicarboxylate/4-hydroxybutyrate (DC/4HB) cycle combines a ferredoxin-dependent pyruvate synthase and PEP carboxylase with the 4-hydroxybutyrate part; it occurs in anaerobic Desulfurococcales (*Ignicoccus hospitalis*) and Thermoproteales (*Thermoproteus*).

### 6.5.5. The Wood–Ljungdahl Pathway

**Definition 6.5.3 (Wood–Ljungdahl Pathway)** The **Wood–Ljungdahl pathway** (reductive acetyl-CoA pathway) is a linear pathway in which one $\ce{CO2}$ is reduced to a methyl group on a pterin (tetrahydrofolate in bacteria, tetrahydromethanopterin in archaea) and transferred to a corrinoid iron–sulfur protein, a second $\ce{CO2}$ is reduced to enzyme-bound CO by CO dehydrogenase, and the bifunctional CO dehydrogenase/acetyl-CoA synthase (a nickel enzyme) joins methyl, CO and coenzyme A into acetyl-CoA.

It is the only autotrophic pathway that is not a cycle, the cheapest (about 1 ATP per pyruvate), and the only one that can also serve energy conservation: acetogens use it as their respiratory chain, reducing $\ce{CO2}$ to acetate with $\ce{H2}$, and acetoclastic methanogens and some sulfate reducers run it backwards to oxidize acetate. Its enzymes contain many metal clusters and are extremely $\ce{O2}$-sensitive, so it occurs only in strict anaerobes: acetogens, methanogens, anammox bacteria and autotrophic sulfate reducers. Its chemistry resembles that of hydrothermal-vent minerals, and it is a leading candidate for the first autotrophic pathway ([7.10.27](/7.10.27#sec-27.2.5)). Its role in energy metabolism is the subject of [7.11.7](/7.11.7#sec-7.4.1).

### 6.5.6. Comparing the Pathways

![Simplified schemes of three microbial autotrophic pathways. A: reverse citric acid cycle of green sulfur bacteria; two ferredoxin-dependent carboxylations (succinyl-CoA → 2-oxoglutarate and acetyl-CoA → pyruvate, the latter by pyruvate:ferredoxin oxidoreductase, PFOR) and isocitrate dehydrogenase fix CO₂, and ATP-citrate lyase splits citrate into oxaloacetate and acetyl-CoA. B: the first cycle of the 3-hydroxypropionate bicycle of *Chloroflexus*: two biotin-dependent carboxylases fix bicarbonate, and malyl-CoA is cleaved into acetyl-CoA and glyoxylate, which the second cycle (not drawn) converts with propionyl-CoA into pyruvate. C: the Wood–Ljungdahl pathway: a methyl branch on tetrahydrofolate (THF) and a carbonyl branch on CO dehydrogenase meet at CO dehydrogenase/acetyl-CoA synthase (CODH/ACS). [2H] stands for two electrons from NAD(P)H, reduced ferredoxin (Fd) or H₂.](./plots/autotrophic-pathways.py)

| Pathway | Carboxylating enzymes | Primary product | ATP per pyruvate | O₂ tolerance | Distribution |
|---|---|---|---|---|---|
| Calvin cycle | rubisco | 3-phosphoglycerate | 7 | tolerant (oxygenase side reaction) | cyanobacteria, plants, purple bacteria, most chemolithotrophs |
| Reverse citric acid cycle | 2-oxoglutarate and pyruvate:Fd oxidoreductases, isocitrate dehydrogenase, PEP carboxylase | acetyl-CoA | 2 | sensitive | green sulfur bacteria, Aquificota, Campylobacterota |
| Wood–Ljungdahl | CO dehydrogenase/acetyl-CoA synthase, formate dehydrogenase | acetyl-CoA | ≈ 1 | very sensitive | acetogens, methanogens, anammox bacteria, sulfate reducers |
| 3-Hydroxypropionate bicycle | acetyl-CoA and propionyl-CoA carboxylases | glyoxylate, pyruvate | 7 | tolerant | *Chloroflexus* |
| 3HP/4HB cycle | acetyl-CoA/propionyl-CoA carboxylase | acetyl-CoA | 9 (6 in the AOA variant) | tolerant | Sulfolobales, ammonia-oxidizing archaea |
| DC/4HB cycle | pyruvate:Fd oxidoreductase, PEP carboxylase | acetyl-CoA | 5 | sensitive | Desulfurococcales, Thermoproteales |

![The ATP cost of making one pyruvate from CO₂ in the six classical pathways (ATP equivalents, values after Berg 2011; an ATP hydrolysed to AMP counts as two, electrons are not counted). The cheap pathways (reverse citric acid cycle, Wood–Ljungdahl pathway, dicarboxylate/4-hydroxybutyrate cycle) depend on oxygen-sensitive ferredoxin-dependent or metal-cluster enzymes and occur in anaerobes and microaerophiles; aerobic autotrophs pay more for oxygen-tolerant enzymes.](./plots/co2-fixation-costs.py)

The pattern in the table is a trade-off: low-potential reductants (reduced ferredoxin) and metal-cluster enzymes make carboxylation cheap but cannot survive oxygen, so aerobes use the expensive but robust Calvin cycle or the 3HP/4HB cycle. The total cost of autotrophy also includes the electrons; for a chemolithotroph oxidizing a weak electron donor, generating NAD(P)H by reverse electron transport can cost more than the ATP itself ([7.11.7](/7.11.7#sec-7.1.3)).

**Remark 6.5.1** The list is not closed. Since 2018 two further routes have been demonstrated: a reversed oxidative citric acid cycle in which citrate synthase itself runs backwards (in *Thermosulfidibacter takaii* and *Desulfurella acetivorans*), and a reductive glycine pathway, in which $\ce{CO2}$ is reduced via formate and glycine cleavage run in reverse to serine and pyruvate (in *Desulfovibrio desulfuricans*); the second is also being engineered into *Escherichia coli* for synthetic autotrophy.

## 6.6. Nitrogen Fixation

### 6.6.1. Who Fixes Nitrogen

**Nitrogen fixation**, the reduction of $\ce{N2}$ to ammonia by **nitrogenase**, is the only biological entry of new nitrogen into the biosphere apart from lightning and the Haber–Bosch process. The enzyme, its FeMo cofactor and its stoichiometry are described in [7.1.27](/7.1.27#sec-27.1.2); here we consider the organisms.

**Definition 6.6.1 (Diazotroph)** A **diazotroph** is an organism that can grow with $\ce{N2}$ as its sole nitrogen source by fixing it with nitrogenase. All known diazotrophs are bacteria or archaea; eukaryotes fix nitrogen only through prokaryotic symbionts.

Diazotrophs are scattered over many bacterial phyla and the methanogenic archaea, and the phylogeny of *nifH*, the gene of the Fe protein, disagrees with that of 16S rRNA, a sign of repeated horizontal transfer; *nifH* sequences from environmental DNA are the standard marker for the diversity of nitrogen fixers. Ecologically they fall into three groups:

| Lifestyle | Examples | Notes |
|---|---|---|
| Free-living anaerobes | *Clostridium pasteurianum*, *Desulfovibrio*, green sulfur bacteria, heliobacteria, *Methanosarcina*, *Methanococcus* | the ancestral situation; no oxygen problem |
| Free-living facultative or microaerobic | *Klebsiella pneumoniae*, purple nonsulfur bacteria | fix only in the absence of $\ce{O2}$ or at low $\ce{O2}$ |
| Free-living aerobes | *Azotobacter*, *Beijerinckia*, cyanobacteria (*Anabaena*, *Nostoc*, *Trichodesmium*, *Crocosphaera*) | need active protection of nitrogenase |
| Associative | *Azospirillum*, *Gluconacetobacter diazotrophicus*, *Herbaspirillum* on and in grass roots and sugar cane | live on root exudates, supply part of their N to the plant |
| Symbiotic | **rhizobia** in legume **root nodules**; *Frankia* (Actinomycetota) in alder and other actinorhizal plants; cyanobacteria in lichens, cycads, *Azolla* and diatoms | the host provides carbon and $\ce{O2}$ control ([7.11.31](/7.11.31)) |

In the ocean, nitrogen fixation is dominated by cyanobacteria: the filamentous *Trichodesmium*, which forms visible surface tufts, the unicellular *Crocosphaera*, and UCYN-A, an endosymbiont of a haptophyte alga. UCYN-A has lost photosystem II and the Calvin cycle and receives carbon from its host; in 2024 it was shown to divide in step with the host cell and to import host proteins, and it has been described as a nitrogen-fixing organelle (a "nitroplast").

### 6.6.2. The Cost of Fixation and the Hydrogen By-product

By [Eq. (27.1)](/7.1.27#eq-27.1), the molybdenum nitrogenase consumes 16 ATP and 8 electrons per $\ce{N2}$ and inevitably releases one $\ce{H2}$: at least a quarter of the electrons are "wasted" on protons, more when $\ce{N2}$ is limiting. Many diazotrophs recover part of this loss with an uptake hydrogenase that reoxidizes the $\ce{H2}$ and feeds the electrons into respiration (*Bradyrhizobium* strains with this enzyme give higher soybean yields); purple nonsulfur bacteria, which lack it under some conditions, are used to produce $\ce{H2}$ photobiologically.

When molybdenum is scarce, *Azotobacter vinelandii*, many cyanobacteria, *Rhodopseudomonas palustris* and methanogens switch to alternative nitrogenases encoded by separate gene sets (*vnf*, *anf*), with vanadium or only iron in place of molybdenum. They are slower and less efficient: the vanadium enzyme releases about three $\ce{H2}$ per $\ce{N2}$, and the iron-only enzyme more. Because of the energy cost, fixation is tightly regulated: *nif* genes are repressed by ammonium and $\ce{O2}$, and in some bacteria the Fe protein is switched off within minutes by ADP-ribosylation when ammonium appears (the regulation through the PII proteins is treated in [7.11.11](/7.11.11)).

### 6.6.3. Protecting Nitrogenase from Oxygen

Nitrogenase is irreversibly destroyed by $\ce{O2}$, yet many diazotrophs are aerobes, and cyanobacteria produce $\ce{O2}$ themselves. Their solutions separate fixation from oxygen in time, in space or by chemistry.

- Temporal separation: unicellular cyanobacteria such as *Cyanothece* and *Crocosphaera* photosynthesize by day and fix nitrogen at night, under the control of the circadian clock, using the glycogen stored in daylight.
- Spatial separation: filamentous Nostocales (*Anabaena*, *Nostoc*) differentiate **heterocysts** at regular intervals along the filament ([Definition 36.6.1](/7.6.36#def-36.6.1), where the patterning is modelled; development in [7.11.12](/7.11.12)). Heterocysts lack photosystem II, build an extra envelope of glycolipid and polysaccharide that slows $\ce{O2}$ entry, raise their respiration, and exchange fixed nitrogen (glutamine) for sugar with their neighbours. *Trichodesmium*, which has no heterocysts, fixes nitrogen by day in groups of cells within the filament.
- Respiratory protection: *Azotobacter* respires faster than almost any other organism, partly uncoupled, so that $\ce{O2}$ is consumed at the membrane before it reaches nitrogenase; the respiration rate rises with $\ce{O2}$ tension. A thick capsule slows diffusion.
- Conformational protection: on a sudden $\ce{O2}$ shock, the FeSII (Shethna) protein of *Azotobacter* binds the two nitrogenase proteins into an inactive but $\ce{O2}$-resistant complex, which dissociates and resumes fixation when $\ce{O2}$ falls again.
- Symbiotic $\ce{O2}$ control: in legume nodules a diffusion barrier in the nodule cortex and **leghemoglobin** in the infected plant cells keep free $\ce{O2}$ in the nanomolar range while supplying the bacteroids' high-affinity terminal oxidase ([7.11.31](/7.11.31)).

![Three ways to keep oxygen away from nitrogenase. A: in a filament of *Anabaena*, vegetative cells evolve O₂ and fix CO₂; the heterocyst has a thick glycolipid and polysaccharide envelope, no photosystem II and only photosystem I for ATP, respires the O₂ that leaks in, imports sugar (sucrose) and exports glutamine. B: *Azotobacter* protects nitrogenase by respiring O₂ at the cell membrane as fast as it enters (respiratory protection), slows diffusion with a capsule, and on an O₂ shock binds nitrogenase to the FeSII protein (conformational protection). C: in a legume root nodule the bacteroids live in symbiosomes inside infected plant cells, where leghemoglobin buffers free O₂ at nanomolar concentrations; the plant supplies dicarboxylic acids and receives ammonia.](./plots/nitrogenase-protection.py)

### 6.6.4. Measuring Nitrogen Fixation

Nitrogenase also reduces other triple-bonded substrates, among them acetylene, which it reduces with two electrons to ethylene and no further.

**Definition 6.6.2 (Acetylene Reduction Assay)** The **acetylene reduction assay** measures nitrogenase activity by incubating a culture, soil, root or water sample under acetylene ($\ce{C2H2}$, typically 10 percent of the gas phase) and measuring the ethylene ($\ce{C2H4}$) formed by gas chromatography.

The assay is cheap, sensitive and fast, and was decisive for field studies of nitrogen fixation from the late 1960s. It measures electron flux through nitrogenase rather than $\ce{N2}$ fixed: acetylene competes with $\ce{N2}$ and suppresses $\ce{H2}$ evolution, so conversion to $\ce{N2}$ needs a factor that is calibrated against $^{15}\mathrm{N}_2$ incorporation, the definitive method.

**Example 6.6.1** A root sample forms 120 nmol of ethylene per hour. Each ethylene corresponds to 2 electrons. Fixing one $\ce{N2}$ consumes 8 electrons (6 for $\ce{N2}$, 2 for the obligatory $\ce{H2}$), so the theoretical conversion factor is $8/2 = 4$ mol $\ce{C2H4}$ per mol $\ce{N2}$, and the sample fixes about $120/4 = 30\,\mathrm{nmol}$ $\ce{N2}$ per hour, that is, 60 nmol N or about 0.84 µg N per hour. With the older factor of 3 (ignoring the $\ce{H2}$) the estimate would be 40 nmol $\ce{N2}$; measured factors in the field range more widely, which is why $^{15}\mathrm{N}_2$ calibration is needed.

## Summary

- Light is used by two unrelated systems: chlorophyll-based reaction centers, which transfer electrons and can provide both a proton-motive force and reducing power, and retinal-based rhodopsins, which only pump ions (bacteriorhodopsin, proteorhodopsin; 6.4).
- In oxygenic photosynthesis (cyanobacteria) water is the electron donor and two reaction centers act in series; in anoxygenic photosynthesis (purple, green sulfur, green nonsulfur, heliobacteria and others) a single reaction center uses sulfide, $\ce{H2}$, $\ce{Fe^2+}$ or organic donors (Definition 6.1.1, Formula 6.1.1).
- Pigments: chlorophyll *a*, the bacteriochlorophylls with near-infrared bands (Definition 6.1.2), carotenoids (photoprotection) and phycobiliproteins in phycobilisomes (Definitions 6.1.3, 6.1.4); chlorosomes (Definition 6.1.5) allow green bacteria to grow in very dim light. Different absorption spectra let phototrophs stratify in lakes and mats.
- Type II reaction centers deliver electrons to quinones and need reverse electron transport (Definition 6.2.2, Example 6.2.1) to make NADH; type I centers reduce ferredoxin directly (Definition 6.2.1).

| Group | Reaction center | NAD(P)H from | CO₂ fixation |
|---|---|---|---|
| Purple bacteria | type II | reverse electron transport | Calvin cycle |
| Green sulfur bacteria | type I | ferredoxin | reverse citric acid cycle |
| *Chloroflexus* | type II | reverse electron transport | 3-hydroxypropionate bicycle |
| Heliobacteria | type I | ferredoxin | none (photoheterotrophs) |
| Cyanobacteria | type I + II | PSI → ferredoxin | Calvin cycle |

- Six classical autotrophic pathways (Definitions 6.5.1–6.5.3): the oxygen-tolerant Calvin cycle, 3-hydroxypropionate bicycle and 3HP/4HB cycle cost 7–9 ATP per pyruvate; the oxygen-sensitive reverse citric acid cycle, DC/4HB cycle and Wood–Ljungdahl pathway cost 1–5 ATP. Carboxysomes concentrate $\ce{CO2}$ around rubisco.
- Nitrogen fixation is confined to bacteria and archaea (diazotrophs, Definition 6.6.1), free-living, associative or symbiotic; it costs 16 ATP and releases $\ce{H2}$, alternative V and Fe nitrogenases serve when Mo is scarce, and aerobes protect nitrogenase by temporal separation, heterocysts, respiratory and conformational protection or leghemoglobin. The acetylene reduction assay (Definition 6.6.2, Example 6.6.1) measures its activity.

## Questions

1. Why can a purple sulfur bacterium make ATP in the light without consuming any electron donor, but not grow without one?

   **Answer** Cyclic electron flow returns every electron from the quinone pool through cytochrome $bc_1$ and cytochrome $c_2$ to P870, pumping protons on the way, so photophosphorylation needs no net donor. Growth also needs NAD(P)H for $\ce{CO2}$ fixation and biosynthesis; electrons for it must come from an external donor such as $\ce{H2S}$ and be raised to the potential of $\ce{NAD+}$ by reverse electron transport.

2. Green sulfur bacteria are found below purple sulfur bacteria in stratified lakes. Give two physiological reasons.

   **Answer** Their chlorosomes hold thousands of antenna bacteriochlorophylls per reaction center, so they can grow at lower light intensities than any other phototroph; and they tolerate higher sulfide concentrations, which increase with depth. In addition, the brown species absorb the blue-green light that remains at depth with bacteriochlorophyll *e* and isorenieratene.

3. A chemolithotroph lives in an environment with plenty of $\ce{H2}$ but traces of $\ce{O2}$. Which pathway of $\ce{CO2}$ fixation would you expect, and why not the cheapest one in a fully aerobic organism?

   **Answer** With $\ce{H2}$ (a low-potential donor that reduces ferredoxin) and only microaerobic conditions, the reverse citric acid cycle is likely (as in *Hydrogenobacter* or *Aquifex*), costing about 2 ATP per pyruvate. A fully aerobic organism cannot rely on the 2-oxoacid:ferredoxin oxidoreductases or on the metal clusters of the Wood–Ljungdahl pathway, which are destroyed by $\ce{O2}$, so it uses the Calvin cycle or the 3HP/4HB cycle at 7–9 ATP per pyruvate.

4. Proteorhodopsin is found in a large fraction of marine bacteria, whereas bacteriochlorophyll-based photosystems are much rarer. Suggest why, and state what proteorhodopsin cannot do for a cell.

   **Answer** A rhodopsin system needs one small protein, retinal synthesis and no other cofactors or membranes, and can spread by horizontal transfer of a few genes; it costs little and pays off whenever light is available. But it only pumps protons: it provides no reducing power, so cells using it cannot fix $\ce{CO2}$ with light and remain heterotrophs that use light to supplement their energy budget.

5. An *Anabaena* culture is transferred from a medium with ammonium to one without combined nitrogen. Describe what happens and how you would verify that the culture fixes $\ce{N2}$.

   **Answer** Nitrogen starvation triggers the differentiation of about 5–10 percent of the cells into heterocysts at regular intervals; they lose photosystem II, build the thick glycolipid and polysaccharide envelope, express nitrogenase, and exchange glutamine for sugar with vegetative cells. Fixation is shown by the acetylene reduction assay (ethylene production under $\ce{C2H2}$) and, definitively, by the incorporation of $^{15}\mathrm{N}_2$ into cell material.
