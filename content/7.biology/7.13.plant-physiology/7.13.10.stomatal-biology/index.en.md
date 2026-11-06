---
title: Stomatal Biology
description: Stomatal number, distribution and opening mechanics; osmotic regulation in guard cells (K⁺ with Cl⁻, malate, sucrose) and a modern assessment of the classical hypotheses; the dual-beam experiment with red and blue light and the phototropin–H⁺-ATPase–14-3-3 signaling chain; CO₂, humidity and temperature; ABA closure of stomata through PYR/PYL–PP2C–SnRK2–SLAC1; the Brown–Escombe small-pore diffusion law and stomatal conductance; the Ball–Berry and Medlyn models and Cowan–Farquhar optimal stomatal behavior; stomatal development and density control.
source_hash: 839ebd118b09
---

Land plants face an unavoidable trade. A leaf must take up $\ce{CO2}$ for **photosynthesis**, which requires connecting the moist surfaces of its internal cells to the atmosphere, and any pathway that lets $\ce{CO2}$ in also lets water vapor out. The cuticle is almost impermeable to both water and $\ce{CO2}$; the **stomata** are adjustable gates through it. A pair of **guard cells** senses light, $\ce{CO2}$, humidity and hormonal signals and, by changing its own turgor, widens or narrows the pore within minutes, so that the leaf can continually renegotiate between "gaining carbon" and "losing less water." This chapter explains how the gate works: the mechanics of opening and closing (Section 10.2), the osmotic regulation that drives it (Section 10.3), control by light and other environmental factors (Sections 10.4–10.5), and the abscisic acid signal that closes the stomata (Section 10.6). It then describes the stoma quantitatively as a diffusion pathway (Section 10.7), introduces models of stomatal conductance and the theory of optimal stomatal behavior (Section 10.8), and ends with how stomata develop and how their density adjusts to the environment (Section 10.9). The morphology and types of stomatal complexes are described in [7.12.4](/7.12.4#sec-4.3.2); water potential and the general principles of **transpiration** are in [7.13.2](/7.13.2) and [7.13.3](/7.13.3); the limitation that stomata impose on leaf photosynthesis is discussed in [7.13.9](/7.13.9) together with mesophyll conductance and the Farquhar model.

## 10.1. Stomatal Number, Distribution and Opening Rhythm

The epidermis of a leaf carries tens to hundreds of stomata per square millimeter. Sun plants have more and smaller stomata, shade plants fewer and larger ones; yet the total area of the fully open pores is only about 1% of the leaf area:

| Plant type | Stomata / $\mathrm{mm^{-2}}$ | Pore length / $\mu\mathrm{m}$ | Pore width / $\mu\mathrm{m}$ | Pore area as fraction of leaf area |
|---|---|---|---|---|
| Sun plants | 100–200 | 10–20 | 4–5 | 0.8%–1.0% |
| Shade plants | 40–100 | 15–20 | 5–6 | 0.8%–1.2% |

The distribution of stomata over the two leaf surfaces depends on habitat and leaf orientation. Most herbaceous dicots have stomata mainly on the lower epidermis, and many woody plants only there; the erect leaves of grasses and other monocots have them on both sides; floating leaves (water lily) have them only on the upper surface exposed to air, and submerged leaves usually have none. Two quantities describe how many stomata a leaf has:

**Definition 10.1.1 (Stomatal Density and Stomatal Index)** The number of stomata per unit leaf area is the **stomatal density**, in $\mathrm{mm^{-2}}$. The number $S$ of stomata expressed as a percentage of the sum of the number $E$ of epidermal cells and $S$,

$$
\mathrm{SI} = \frac{S}{S + E} \times 100\%
$$
is the **stomatal index**.

As a leaf expands, its epidermal cells enlarge and the stomatal density falls, whereas the stomatal index is largely independent of cell size; it is therefore the preferred measure when comparing leaves that developed in different environments, as well as fossil leaves (Section 10.9).

Most plants open their stomata by day and close them at night; **CAM plants** do the opposite, opening at night to take up $\ce{CO2}$ and closing by day to reduce water loss ([7.13.8](/7.13.8)). Between these two extremes, stomatal aperture varies continuously with light intensity, $\ce{CO2}$, humidity and leaf water status, and it is also under circadian control: when a plant is moved to constant conditions, aperture still oscillates with a period of about 24 h.

## 10.2. The Mechanics of Opening and Closing

### 10.2.1. Guard Cells as Turgor-Operated Valves

In 1856 von Mohl proposed that changes in guard-cell turgor supply the mechanical force that alters pore size. The idea still holds: when guard cells take up water and their **turgor pressure** rises, the pore opens; when they lose water and turgor falls, it closes.

**Definition 10.2.1 (Stomatal Movement)** The deformation of guard cells caused by changes in turgor, which widens or narrows the stomatal pore, is **stomatal movement**. Movement produced by signals such as light, $\ce{CO2}$ or hormones that cause guard cells to actively accumulate or release solutes is active movement; movement produced solely when a change in leaf water status alters the water balance between guard cells and the surrounding epidermal cells is passive movement (hydropassive movement).

How turgor is converted into pore opening depends on the construction of the guard-cell wall. Mature guard cells have no **plasmodesmata** connecting them to neighboring cells, so solutes can enter and leave only across membranes, and osmotic regulation in guard cells depends entirely on transport proteins in the plasma membrane and the tonoplast (Section 10.3).

### 10.2.2. Uneven Wall Thickening and Microfibril Orientation

The orientation of **cellulose microfibrils** determines in which direction a cell expands. In an ordinary cylindrical cell, microfibrils are wound transversely around the long axis and the cell elongates as it takes up water. Guard cells are arranged differently:

- Kidney-shaped guard cells (most dicots, many monocots, ferns and gymnosperms): the ventral wall facing the pore and the upper and lower walls are thick, while the dorsal wall, away from the pore and adjoining the epidermal cells, is thin; microfibrils fan out radially from the pore. When the cell swells, the thin dorsal wall stretches more, and the radial microfibrils prevent the cell from widening and convert elongation into bending along an arc, so the two guard cells bow outward and the pore opens.
- Dumbbell-shaped guard cells (grasses and sedges): the wall of the middle part is very thick, the swollen bulbous ends have thin walls, and microfibrils are oriented radially. When the ends swell, they push the two thick-walled middle parts apart like two crossbars, and the pore opens. Dumbbell-shaped guard cells always flank a pair of subsidiary cells; during opening and closing, $\ce{K+}$ and water shuttle between guard cells and subsidiary cells, so the subsidiary cells serve both as a solute reservoir and as a space that yields when the guard cells swell. Grass stomata therefore open and close faster than those of most dicots.

![Opening and closing of kidney-shaped and dumbbell-shaped guard cells (schematic surface view). A, B: kidney-shaped guard cells (without subsidiary cells), open and closed; C, D: dumbbell-shaped guard cells of grasses with a pair of subsidiary cells, open and closed. Light lines indicate the radially arranged cellulose microfibrils; the darker ventral walls (A, B) and middle parts (C, D) are the thickened walls. On water uptake, the thin dorsal walls of kidney-shaped guard cells stretch and the cells bow outward; the ends of dumbbell-shaped guard cells swell and push the thick-walled middle parts apart](./plots/stoma-mechanics.py)

Guard-cell deformation does not depend on their own turgor alone. The turgor of the surrounding epidermal cells (or subsidiary cells) presses against the guard cells from outside and acts on the pore in the opposite sense; within a certain range this effect is stronger than the guard cells' own turgor (the "mechanical advantage" of the epidermis). Hence when a leaf suddenly loses water, epidermal turgor falls first and the pore briefly widens (the "wrong-way response"); only afterward do the guard cells lose water and the pore narrows. Recent mechanical measurements and finite-element simulations also show that the walls at the two ends (polar regions) of the guard cells are stiff and hold the two ends of the pair in place, so that swelling can be converted only into bending of the middle region.

Guard-cell turgor changes by a large amount: about 1 MPa or less when closed and 4–5 MPa when fully open, and within a certain range pore width increases roughly linearly with guard-cell turgor. This requires the solute potential of the guard cell to fall by about 2 MPa on opening; the next section explains where these solutes come from.

## 10.3. Osmotic Regulation in Guard Cells

### 10.3.1. From Solutes to the Pore

All the internal and external factors that regulate stomatal opening and closing act ultimately by changing the solute content of the guard cells. This is a stepwise chain:

```mermaid
flowchart LR
  A["Ions and organic solutes<br/>enter or leave the guard cell"] --> B["Solute potential Ψs falls or rises"]
  B --> C["Water potential Ψw falls or rises"]
  C --> D["Water enters or leaves"]
  D --> E["Turgor pressure Ψp rises or falls"]
  E --> F["Deformation of the unevenly walled guard cell"]
  F --> G["Pore widens or narrows"]
```

By the van 't Hoff relation, the solute potential is $\Psi_{\mathrm{s}} = -c\,RT$, where $c$ is the **osmolarity** ([7.13.2](/7.13.2)). The guard-cell solutes fall into three classes: $\ce{K+}$ with its counter-anions $\ce{Cl-}$ and malate, sucrose, and small amounts of other sugars.

### 10.3.2. K⁺ and Its Counter-Anions

When the stomata open, the $\ce{K+}$ concentration in guard cells rises several-fold: about 100 mM when closed and 400–800 mM when open, depending on species and conditions. A cation increment this large must be balanced by anions, which in most species are $\ce{Cl-}$ and malate ($\text{malate}^{2-}$) in varying proportions; the guard cells of some *Allium* species such as onion contain almost no starch, and $\ce{K+}$ is balanced entirely by $\ce{Cl-}$. Most of these ions are stored in the vacuole.

- $\ce{K+}$ enters passively through voltage-gated inward-rectifying $\ce{K+}$ channels (KAT1, KAT2 and others in *Arabidopsis*). The driving force comes from the hyperpolarization produced by proton pumping by the **plasma membrane H⁺-ATPase**: light-induced hyperpolarization can reach 64 mV, together with a transmembrane pH difference of 0.5–1 pH unit.
- $\ce{Cl-}$ is taken up from the apoplast by an $\ce{H+}$–$\ce{Cl-}$ **symporter**, using the chemical component of the proton gradient; on closing it leaves through anion channels.
- Malate is synthesized inside the guard cell: triose phosphates produced by starch hydrolysis pass through glycolysis to PEP, PEP carboxylase adds $\ce{HCO3-}$ to PEP to give oxaloacetate, and malate dehydrogenase reduces it to malate. These are the same first two steps as $\ce{CO2}$ fixation in the mesophyll cells of **C4 plants** ([7.13.8](/7.13.8)). The $\ce{H+}$ released on dissociation of malate is pumped out, and malate anions remain to balance $\ce{K+}$. Malate content falls when the stomata close, but whether it is respired in mitochondria, exported to the apoplast, or both is not yet clear.

**Example 10.3.1 (Change in Solute Potential Required for Opening)** Suppose guard-cell $\ce{K+}$ increases from 100 mM to 500 mM, and of the added 400 mM of positive charge 60% is balanced by $\ce{Cl-}$ and 40% by malate. Find the change in solute potential at 25 °C.

$\ce{Cl-}$ increases by 240 mM; malate carries two negative charges, so only 80 mM is needed to balance 160 mM of positive charge. The osmolarity increases by

$$
\Delta c = 400 + 240 + 80 = 720\ \mathrm{mM} = 720\ \mathrm{mol\,m^{-3}},
$$
so

$$
\Delta\Psi_{\mathrm{s}} = -\Delta c\,RT = -720 \times 8.314 \times 298.15\ \mathrm{Pa} \approx -1.8\ \mathrm{MPa}.
$$
If the water potential of the guard cell remains in equilibrium with that of the surrounding cells, turgor rises by about 1.8 MPa, the same order of magnitude as the 2–4 MPa turgor increment on opening. With $\ce{KCl}$ alone ($\Delta c = 800\ \mathrm{mM}$), $\Delta\Psi_{\mathrm{s}} \approx -2.0\ \mathrm{MPa}$: with malate as counter-ion, each anion "carries off" the charge of two $\ce{K+}$, so the same $\ce{K+}$ increment produces a slightly smaller osmotic effect.

**Example 10.3.2 (Is $\ce{K+}$ Uptake Passive?)** Suppose that during opening the guard-cell cytosolic $\ce{K+}$ is 300 mM and the apoplastic $\ce{K+}$ is 10 mM. By the **Nernst equation**, at 25 °C

$$
E_{\ce{K}} = \frac{RT}{F}\ln\frac{[\ce{K+}]_{\mathrm{o}}}{[\ce{K+}]_{\mathrm{i}}} = 25.7\ \mathrm{mV} \times \ln\frac{10}{300} \approx -87\ \mathrm{mV}.
$$
When the proton pump holds the plasma membrane potential near $-150\ \mathrm{mV}$, $V - E_{\ce{K}} \approx -63\ \mathrm{mV} < 0$, and the **electrochemical potential** gradient of $\ce{K+}$ points inward; $\ce{K+}$ enters down this gradient through channels and no $\ce{K+}$ pump is needed. Conversely, when the plasma membrane depolarizes to about $-40\ \mathrm{mV}$ on closing, $V - E_{\ce{K}} \approx +47\ \mathrm{mV}$, and $\ce{K+}$ leaves through outward-rectifying channels. Chinese textbooks often say that "$\ce{K+}$ is actively taken up by $\ce{H+}$–$\ce{K+}$ exchange"; strictly, $\ce{K+}$ uptake itself is passive, and the energy-consuming step is the proton pump.

### 10.3.3. Sucrose and the Two Osmotic Phases

Guard-cell chloroplasts contain large starch grains. In contrast to mesophyll cells, guard-cell starch decreases in the morning when the stomata open and increases in the evening when they close. Insoluble starch does not contribute to the solute potential, whereas its hydrolysis to soluble sugars lowers it, which was the basis of the earliest starch–sugar hypothesis. After the 1960s the role of $\ce{K+}$ was established, and sugars were for a time thought unimportant; but a study of the diurnal course of stomatal opening in intact leaves (Talbott and Zeiger, 1998, broad bean) showed that sucrose takes the leading role in the afternoon:

- in the morning, $\ce{K+}$ content rises in step with the opening of the pore;
- in the early afternoon, $\ce{K+}$ begins to decline while the pore is still widening, and sucrose accumulates slowly to become the main osmotic solute of the guard cell;
- in the evening, closure of the pore parallels the decline in sucrose content.

![Diurnal course of pore width, K⁺ and sucrose content in broad bean guard cells (schematic after the results of Talbott and Zeiger 1998; values are relative). Opening of the pore in the morning is driven mainly by accumulation of K⁺ and its counter-anions; in the afternoon K⁺ leaves and sucrose becomes the main osmotic solute; closing of the pore in the evening parallels the decline in sucrose content. The bands below indicate the two osmotic phases](./plots/diurnal-osmotica.py)

Sucrose in guard cells has three possible sources: (1) hydrolysis of starch in guard-cell chloroplasts; (2) photosynthetic carbon fixation in the guard-cell chloroplasts themselves; and (3) uptake by the guard cells of sucrose exported from the mesophyll into the apoplast. Which predominates depends on conditions. At ordinary $\ce{CO2}$ concentrations, when isolated epidermis is illuminated with red light the guard cells accumulate mainly sucrose produced by photosynthetic fixation, with almost no detectable $\ce{K+}$ uptake or starch degradation; in $\ce{CO2}$-free air, where photosynthetic fixation is blocked, red-light-induced opening is accompanied by $\ce{K+}$ accumulation. The significance of the two phases is not fully understood: $\ce{K+}$ may suit the rapid opening at sunrise, while the sucrose phase may coordinate the aperture of the epidermal stomata with the photosynthetic rate of the mesophyll.

Guard-cell starch is degraded rapidly early in opening. In *Arabidopsis* this degradation is triggered by blue light through phototropin and carried out by β-amylase BAM1 and α-amylase AMY3 (Horrer et al., 2016); the sugars produced supply carbon skeletons for malate synthesis and also act directly as osmotic solutes.

### 10.3.4. Several Hypotheses and Their Modern Assessment

Several hypotheses have been proposed historically for where the guard-cell solutes come from:

**Definition 10.3.1 (Osmotic-Regulation Hypotheses of Stomatal Movement)** The hypothesis that interconversion of starch and soluble sugars in guard cells (controlled by pH) changes the solute potential and thereby controls stomatal opening and closing is the **starch–sugar hypothesis**; the hypothesis that uptake and release of $\ce{K+}$ and its counter-anions by guard cells control opening and closing is the **potassium hypothesis** (also called the inorganic-ion uptake hypothesis); and the hypothesis that malate synthesized in light by PEP carboxylase in guard cells both supplies $\ce{H+}$ for exchange with $\ce{K+}$ and balances charge as the malate anion is the **malate hypothesis**.

| Hypothesis | Proposed | Main points | Modern assessment |
|---|---|---|---|
| Starch–sugar hypothesis | Lloyd, 1908 | Photosynthetic consumption of $\ce{CO2}$ raises guard-cell pH; starch phosphorylase converts starch to sugar, lowering the solute potential; reversed in the dark | The pH mechanism of starch phosphorylase does not hold; but starch degradation and sucrose accumulation do take part in osmotic regulation, and the afternoon sucrose phase brings it back in a new form |
| K⁺ hypothesis | Japanese workers in the 1940s; rediscovered in Europe and the United States in the 1960s | Light activates the plasma membrane H⁺-ATPase; hyperpolarization drives $\ce{K+}$ entry through channels, with $\ce{Cl-}$ taken up alongside | The main mechanism of morning opening, established at the molecular level (H⁺-ATPase, KAT1, GORK, SLAC1) |
| Malate hypothesis | 1970s | Starch → PEP → oxaloacetate → malate; malate balances $\ce{K+}$; $\ce{H+}$ exchanged for $\ce{K+}$ | Malate is indeed one of the counter-anions of $\ce{K+}$, and the two hypotheses together form the "K⁺–malate hypothesis"; exchange of malate-derived $\ce{H+}$ for $\ce{K+}$ is not the main driving force, which comes from the proton pump |
| Sucrose hypothesis | Talbott and Zeiger, 1990s | In the afternoon sucrose replaces $\ce{K+}$ as the main osmotic solute | Confirmed in intact leaves of broad bean, onion and others; its generality is still under study |
| Zeaxanthin hypothesis | Zeiger and colleagues, 1990s | Zeaxanthin in guard-cell chloroplasts is the blue-light receptor and starts the proton pump after isomerization | The main blue-light receptor has been identified as phototropin (Section 10.4.2); zeaxanthin may participate in the reversal of the blue-light response by green light, but its role is disputed |

The hypotheses are not mutually exclusive. The modern picture is that light, especially blue light, first activates the proton pump; uptake of $\ce{K+}$ and $\ce{Cl-}$ and synthesis of malate provide most of the solutes needed for opening in the morning, and sucrose sustains the aperture in the afternoon, in proportions that vary with species, light quality and $\ce{CO2}$ concentration.

## 10.4. Regulation of Stomata by Light

### 10.4.1. Two Light Responses: The Dual-Beam Experiment

Under temperate conditions, light is the main environmental signal causing stomata to open: in greenhouse-grown broad bean, the aperture of stomata on the lower epidermis follows the photosynthetically active radiation at the leaf surface almost hour by hour. Light acts by two routes: photosynthesis in the guard-cell chloroplasts, and a specific blue-light response. In addition, mesophyll photosynthesis lowers the intercellular $\ce{CO2}$ concentration $c_{\mathrm{i}}$, and a low $c_{\mathrm{i}}$ itself causes stomata to open (Section 10.5).

DCMU, an inhibitor of photosynthetic electron transport, only partially inhibits light-induced opening, which indicates a component independent of photosynthesis. Because blue light drives both photosynthesis and the specific blue-light response, blue light alone cannot separate the two, hence the dual-beam experiment: the guard cells are first illuminated with high-intensity red light to saturate their photosynthesis, so that more red light no longer opens the stomata further; a low-intensity blue light is then superimposed, and the pore opens further, clearly beyond the saturating red-light level. This increment cannot come from photosynthesis (already saturated by red light) and must come from a separate photoreceptor system. Use of isolated epidermis excluded any influence of mesophyll $\ce{CO2}$ (Schwartz and Zeiger, 1984, *Commelina*).

**Definition 10.4.1 (Blue-Light Response of Stomata)** Stomatal opening caused by low-intensity blue light against a saturating red-light background and independent of photosynthesis is the **blue-light response** of stomata.

The blue-light response has several characteristics. Its action spectrum has three peaks between 400 and 500 nm (near 420, 450 and 470 nm, a "three-finger" shape), the typical spectrum of blue-light responses and quite unlike the **action spectrum** of photosynthesis; isolated guard-cell protoplasts swell in blue light, showing that light is perceived in the guard cell itself; suspensions of guard-cell protoplasts acidify after a blue-light pulse, and this acidification is blocked by the uncoupler CCCP and by the H⁺-ATPase inhibitor vanadate. The response has a lag of about 25 s and continues at its maximal rate for several minutes after the blue light is turned off, indicating that the photoreceptor, once converted to its active state by blue light, returns only slowly to the inactive state. The fungal toxin fusicoccin directly activates the plasma membrane H⁺-ATPase and likewise causes proton extrusion and stomatal opening; excess fusicoccin holds the stomata irreversibly open and the plant wilts and dies, which is the cause of the wilt disease of almond and other plants.

![The dual-beam experiment (schematic, redrawn after the design of Schwartz and Zeiger 1984). A: in isolated epidermis under saturating red light the pore widens to a plateau (red line); when low-intensity blue light is added on the same red background (arrow), the pore opens further (blue line), the increment coming from a blue-light receptor system independent of photosynthesis. B: action spectrum for blue-light promotion of stomatal opening on a saturating red background (schematic), with three peaks near 420, 450 and 470 nm, the typical spectrum of a blue-light response](./plots/dual-beam.py)

### 10.4.2. Phototropin–H⁺-ATPase–14-3-3

Stomata of the *Arabidopsis phot1 phot2* double mutant do not open in low-intensity blue light, so the main photoreceptor mediating this response is **phototropin** (structure and photochemistry in [7.6.18](/7.6.18)). Blue-light-induced opening is the best-understood of the pathways mediated by phototropins:

1. Phototropin absorbs blue light and is activated by autophosphorylation.
2. Activated phototropin phosphorylates BLUS1 (BLUE LIGHT SIGNALING1), a membrane-bound protein kinase specific to guard cells; stomata of the *blus1* mutant do not respond to blue light, but phototropism and chloroplast movement are normal.
3. The signal converges on type 1 protein phosphatase PP1 (catalytic subunit PP1c with regulatory subunit PRSL1), and then passes through a protein kinase not yet identified.
4. This kinase phosphorylates serine and threonine residues in the C-terminal autoinhibitory domain of the plasma membrane H⁺-ATPase (mainly the penultimate Thr).
5. A 14-3-3 protein binds the phosphorylated C terminus and moves the autoinhibitory domain away from the catalytic site, lowering the $K_{\mathrm{m}}$ of the enzyme for ATP and raising $V_{\max}$; on dephosphorylation 14-3-3 dissociates and the enzyme returns to the inhibited state. Fusicoccin acts precisely by stabilizing the binding of 14-3-3 to the C terminus.
6. Proton extrusion hyperpolarizes the plasma membrane and drives $\ce{K+}$ entry through inward-rectifying channels; at the same time blue light inhibits S-type anion channels, reducing the loss of anions.
7. Solute accumulation lowers the water potential, water enters, and the pore opens.

When **abscisic acid** closes stomata in the light, one of its routes is precisely to antagonize this pathway: the signaling lipid **phosphatidic acid** induced by ABA inhibits PP1 and activates the S-type anion channels that are inhibited by blue light (Section 10.6).

The identity of the blue-light receptor was the subject of a controversy. Zeaxanthin is a component of the chloroplast **xanthophyll cycle**; its content in guard cells varies with light intensity during the day and with pore width, its absorption spectrum resembles the action spectrum of the blue-light response, and the *npq1* mutant, which lacks zeaxanthin, also lacks the specific blue-light response, so zeaxanthin was thought to be the guard-cell blue-light receptor (the zeaxanthin hypothesis), a view still often listed in Chinese textbooks. But the phenotype of *phot1 phot2* and the signaling components downstream of BLUS1 all show that phototropin is the main blue-light receptor. Zeaxanthin may take part in the reversal of the blue-light response by green light: a green-light pulse after a blue-light pulse cancels the blue-light-induced opening, and a further blue-light pulse restores it; *npq1* lacks this reversal while *phot1 phot2* shows it; the molecular mechanism remains unresolved. Cryptochromes and phytochrome B also promote stomatal opening, but to a lesser extent.

### 10.4.3. Red Light and Guard-Cell Photosynthesis

Guard-cell chloroplasts are rich in photosystem II, with a high rate of photosynthetic electron transport but a low rate of carbon fixation, and can acidify the thylakoid lumen even in weak light. Their contribution to stomatal opening includes supplying ATP to the proton pump (possibly also indirectly through chloroplast–mitochondrion shuttles) and producing sucrose by photosynthetic fixation (Section 10.3.3). However, the photosynthetic capacity of guard-cell chloroplasts is weak, and a large part of red-light-induced opening comes from the mesophyll: mesophyll photosynthesis lowers $c_{\mathrm{i}}$ and the guard cells respond to the low $c_{\mathrm{i}}$; the mesophyll may also transmit unidentified signals to the guard cells. Some plants show plasticity of the guard cell: in *Paphiopedilum* the guard-cell chloroplasts lack chlorophyll and the stomata open in blue light without a typical red-light response; in *Adiantum* the guard cells contain particularly many chloroplasts, lack a specific blue-light response, and open in red light, which is inhibited by DCMU.

## 10.5. CO₂, Humidity, Temperature and Other Factors

$\ce{CO2}$: a low $c_{\mathrm{i}}$ opens the stomata, and a high $c_{\mathrm{i}}$ closes them rapidly even in the light. Guard cells sense the intercellular, not the atmospheric, $\ce{CO2}$ concentration. In *Arabidopsis*, the guard-cell β-type carbonic anhydrases βCA1 and βCA4 convert $\ce{CO2}$ to $\ce{HCO3-}$, the protein kinase HT1 (HIGH LEAF TEMPERATURE1) is a negative regulator required for opening at low $\ce{CO2}$, and the high-$\ce{CO2}$ signal ultimately also activates the SLAC1 anion channel (Section 10.6), joining the ABA pathway. Stomatal conductance of most plants declines when atmospheric $\ce{CO2}$ rises, which is one reason for reduced plant transpiration under climate change.

Humidity: as the vapor pressure deficit (VPD) between leaf and air increases, stomata narrow. Part of this is hydropassive: stronger transpiration dehydrates the guard cells; part is active and involves ABA synthesis in the leaf. When the soil dries, falling leaf water potential also closes stomata through ABA (Section 10.6).

**Temperature**: within the favorable range, stomatal aperture generally increases with temperature, reaching a maximum near 30 °C; temperatures that are too high (above 35 °C) or too low (below 10 °C) inhibit opening. When water is ample, staying open at high temperature favors transpirational cooling.

Wind: a light breeze thins the boundary layer at the leaf surface and promotes transpiration; strong wind makes transpiration too fast, the guard cells lose water, and the stomata close.

Patchy stomata: stomata on a leaf do not always open and close in synchrony. After water stress or ABA treatment, a leaf often shows an alternation of regions of open and closed stomata, termed *patchy stomatal conductance*; the relative hydraulic independence of the small areas into which the vascular bundles divide the leaf may be one cause. Patchiness causes the intercellular $\ce{CO2}$ concentration inferred from gas exchange to be overestimated.

Antitranspirants: to reduce water loss during transplanting or drought, antitranspirants can be applied. By mode of action they fall into three classes: metabolic types that narrow stomata (such as ABA and its stable analogs), film-forming types that form a gas-permeable, water-impermeable film on the leaf, and reflective types that raise leaf reflectance to lower leaf temperature (such as kaolin). They reduce $\ce{CO2}$ entry along with transpiration and are suitable only for short-term use.

## 10.6. Closure of Stomata by Abscisic Acid

### 10.6.1. Water Deficit and ABA

When the soil dries, leaf water potential falls, the ABA content of the leaf rises rapidly, and stomatal resistance (the reciprocal of **stomatal conductance**) increases accordingly; after rewatering all three recover (maize, Beardsell and Cohen, 1975). The increase of ABA around the guard cells may come from several sources: accelerated synthesis in the leaf itself (vascular parenchyma cells and the guard cells themselves); release from intracellular storage sites or by hydrolysis of conjugated ABA-glucose ester; and delivery from the roots in the xylem. Signals from drying roots can close stomata before leaf water potential changes, and early work attributed this mainly to root-derived ABA; more recent work shows that synthesis in the leaf itself is often the main source, and that the roots may act more through hydraulic signals and other molecules. ABA synthesis and transport are described in [7.13.15](/7.13.15).

### 10.6.2. The Signaling Pathway

The physical basis of ABA-induced stomatal closure is the large loss of $\ce{K+}$ and anions from the guard cells, with a fall in turgor. The plasma membrane $\ce{K+}$ efflux channels are voltage-gated and open only when the plasma membrane depolarizes, so the key is first to depolarize the membrane. The ABA receptors and core signaling components (PYR/PYL/RCAR receptors, clade A PP2Cs, SnRK2s) are introduced in [7.1.15](/7.1.15#sec-15.5.6); here they are strung together in their order in guard cells:

1. ABA binds the intracellular PYR/PYL/RCAR receptors, and the receptor–ABA complex binds and inhibits clade A type 2C protein phosphatases (ABI1, ABI2 and others). In the absence of ABA, PP2Cs are the main negative regulators in this network.
2. Freed from PP2C inhibition, the protein kinase OST1 (OPEN STOMATA1, that is, SnRK2.6) is activated by autophosphorylation.
3. OST1 phosphorylates and activates the plasma membrane NADPH oxidases RBOHD and RBOHF, which produce **reactive oxygen species** ($\ce{O2^.-}$, $\ce{H2O2}$) in the apoplast and activate $\ce{Ca^2+}$-permeable channels in the plasma membrane. $\ce{Ca^2+}$ flows in and also triggers release of $\ce{Ca^2+}$ from the vacuole and endoplasmic reticulum; within about 3 min of adding ABA, cytosolic $\ce{Ca^2+}$ rises from about 0.1 µM to about 1 µM, and about 5 min later the pore begins to narrow (McAinsh et al., 1990).
4. $\ce{Ca^2+}$ activates calcium-dependent protein kinases (CPKs); OST1 and the CPKs both phosphorylate and activate plasma membrane anion channels: the slow (S-type) SLAC1 and its homologs, and the rapid (R-type) QUAC1. In the absence of ABA, PP2Cs directly dephosphorylate and thereby inactivate these channels.
5. Anions such as $\ce{Cl-}$ and malate flow out in large amounts down their electrochemical gradients and depolarize the plasma membrane; depolarization opens the outward-rectifying $\ce{K+}$ channel GORK, and $\ce{K+}$ flows out.
6. Most of the guard-cell $\ce{K+}$ and anions are in the vacuole; they are released to the cytosol through $\ce{Ca^2+}$-activated $\ce{K+}$ channels and anion transporters in the tonoplast and then leave the cell.
7. At the same time, elevated $\ce{Ca^2+}$ inhibits the inward $\ce{K+}$ channels, and ABA also inhibits the plasma membrane H⁺-ATPase and raises cytosolic pH from about 7.7 to about 7.9, an alkalinization that further promotes opening of the $\ce{K+}$ efflux channels. These inhibitory actions on opening prevent re-uptake of the ions.

Ion efflux raises the water potential, water flows out, turgor falls, and the stoma closes. During closure the plasma membrane area of the guard cell can decrease by as much as 50%, and the excess membrane is recovered by endocytosis as vesicles. ABA also induces nitric oxide production, which promotes closure in many experiments. In general the ABA pathway works by the logic of "inhibiting an inhibitor": the hormone inactivates a phosphatase and releases constitutively active kinases.

![Integration of opening and closing signals in the guard cell (SBGN activity flow diagram, simplified). Upper part: blue light acts through phototropin, BLUS1 and PP1 to phosphorylate the plasma membrane H⁺-ATPase, which binds 14-3-3; proton extrusion hyperpolarizes the membrane and drives K⁺ entry through the inward channel (KAT1), and the stoma opens. Lower part: ABA binds PYR/PYL receptors, inhibits PP2C and releases OST1 (SnRK2.6); OST1 activates the SLAC1 anion channel directly and, indirectly, through RBOH, reactive oxygen species, Ca²⁺ and CPK; anion efflux depolarizes the membrane, K⁺ leaves through GORK, and the stoma closes. Ca²⁺ inhibits KAT1 and ABA inhibits PP1 through phosphatidic acid (PA), connecting the two pathways; high CO₂ also feeds into activation of SLAC1. Open arrowheads indicate promotion, bars indicate inhibition, and dashed lines indicate indirect action](./plots/guard-cell-signaling.py)

### 10.6.3. A Single Integrated Valve

The signals from light, $\ce{CO2}$, humidity and ABA all converge on the same set of transport proteins: the plasma membrane H⁺-ATPase, inward and outward $\ce{K+}$ channels, S-type and R-type anion channels, and the tonoplast transport systems. Opening signals activate the pump and the inward channels and inhibit the anion channels; closing signals do the opposite. This convergence makes the guard cell a "multi-input hydraulic valve," able to integrate conflicting signals (for example, strong midday light and drought) into a single aperture.

## 10.7. Diffusion Through Small Pores

### 10.7.1. The Brown–Escombe Law

The movement of water vapor and $\ce{CO2}$ through stomata is diffusion. An apparent paradox is that the total area of fully open stomata is only about 1% of the leaf area, yet the transpiration rate of a leaf can reach half or more of the evaporation from a free water surface of the same area; that is, evaporation per unit pore area is tens of times faster than from a free water surface. Brown and Escombe (1900) studied this problem with perforated films: the amount of diffusion through an isolated pore is not proportional to the area of the pore but to its diameter (that is, its perimeter).

**Definition 10.7.1 (Small-Pore Diffusion Law)** When a gas diffuses through an isolated small circular hole in a thin partition, the diffusion rate is proportional to the diameter (perimeter) of the hole and not to its area, so the rate per unit area increases as the hole becomes smaller. This rule is the **small-pore diffusion law**, also called the edge effect.

Physically, diffusing molecules form a hemispherical concentration "shell" on each side of the pore, and molecules at the rim of the opening can diffuse sideways and have less chance of "colliding" and crowding each other, so the flux at the edge is larger than at the center; the smaller the pore, the greater the fraction occupied by the edge. Quantitatively, solving steady diffusion in the half-space outside the pore with **Fick's law** ([2.5.1](/2.5.1)), the resistance to diffusion from a disk of radius $r$ into a half-space is $1/(4Dr)$, and each side of the pore contributes one such "end resistance"; the resistance of a pore channel of depth $l$ is $l/(\pi r^2 D)$. Hence:

**Formula 10.7.1 (Diffusion Through a Single Pore)** For a concentration difference $\Delta c$, the diffusive flux through a circular pore of radius $r$ and depth $l$ is

$$
J = \frac{\pi r^2 D\,\Delta c}{l + \frac{\pi}{2} r}. \tag{10.1}
$$

When $l \gg r$, $J \approx \pi r^2 D\Delta c/l$, proportional to area (ordinary diffusion in a tube); when the pore is very shallow ($l \ll r$), $J \approx 2rD\Delta c$, proportional to diameter, which is the Brown–Escombe result. The depth of a stoma is of the same order as its pore diameter, so neither term can be neglected. Chinese textbooks often summarize the small-pore law as "the diffusion rate is proportional to the perimeter of the small pore," which holds only for an isolated shallow pore.

Brown and Escombe also found that when the pore spacing is less than about 10 pore diameters, the concentration shells of neighboring pores overlap and the flux through each pore decreases; with pores dense enough, the total diffusion through a multi-pore film approaches that through a free surface of the same area. Stomatal spacing on a leaf usually lies at the edge of this range, and together with the boundary-layer resistance at the leaf surface ([7.13.3](/7.13.3)) this means that leaf transpiration cannot exceed that from a free water surface, but can reach a considerable fraction of it with 1% pore area.

### 10.7.2. Stomatal Conductance

It is most convenient to write transpiration in the form "driving force × conductance":

**Definition 10.7.2 (Stomatal Conductance)** The ratio of the flux $E$ of water vapor diffusing through the stomata per unit leaf area to the difference $\Delta w$ in water vapor mole fraction between the inside of the leaf (the substomatal cavity) and the leaf surface,

$$
g_{\mathrm{s}} = \frac{E}{\Delta w}
$$
is the **stomatal conductance**, in $\mathrm{mol\,m^{-2}\,s^{-1}}$; its reciprocal $r_{\mathrm{s}} = 1/g_{\mathrm{s}}$ is the stomatal resistance. The diffusion coefficient of $\ce{CO2}$ is $1/1.6$ that of water vapor, so the stomatal conductance to $\ce{CO2}$ is $g_{\mathrm{c}} = g_{\mathrm{s}}/1.6$.

Older literature uses units of $\mathrm{mm\,s^{-1}}$ or $\mathrm{cm\,s^{-1}}$ (with the concentration difference rather than the mole-fraction difference as driving force); the conversion is $g[\mathrm{mol\,m^{-2}\,s^{-1}}] = g[\mathrm{m\,s^{-1}}] \cdot p/(RT)$, and at 25 °C and 101.3 kPa $p/(RT) \approx 40.9\ \mathrm{mol\,m^{-3}}$, that is, $1\ \mathrm{mm\,s^{-1}} \approx 0.041\ \mathrm{mol\,m^{-2}\,s^{-1}}$. A "stomatal resistance of $10\ \mathrm{s\,cm^{-1}}$," common in the literature, corresponds to $g_{\mathrm{s}} \approx 0.004\ \mathrm{mol\,m^{-2}\,s^{-1}}$, close to complete closure. Leaves of well-watered crops in the light generally have $g_{\mathrm{s}}$ of $0.2$–$0.8\ \mathrm{mol\,m^{-2}\,s^{-1}}$.

Multiplying Eq. (10.1) by the number of stomata per unit area $N$ and approximating the stomatal pore as a circular hole of area $a$ gives the maximum stomatal conductance determined by anatomy (Franks and Farquhar, 2001):

**Formula 10.7.2 (Anatomical Maximum Stomatal Conductance)**

$$
g_{\max} = \frac{D_{\mathrm{w}}}{v}\cdot\frac{N a}{l + \frac{\pi}{2}\sqrt{a/\pi}}, \tag{10.2}
$$
where $D_{\mathrm{w}}$ is the diffusion coefficient of water vapor in air (about $2.5\times10^{-5}\ \mathrm{m^2\,s^{-1}}$ at 25 °C), $v = RT/p$ is the molar volume of air (about $0.0245\ \mathrm{m^3\,mol^{-1}}$), and $l$ is the pore depth.

**Example 10.7.1** A sun leaf has stomatal density $N = 200\ \mathrm{mm^{-2}} = 2.0\times10^{8}\ \mathrm{m^{-2}}$, with elliptical pores 20 µm long and 5 µm wide and 8 µm deep. The pore area is $a = \frac{\pi}{4}\times 20\times 5\ \mu\mathrm{m^2} = 78.5\ \mu\mathrm{m^2}$, and the total pore area is $Na = 1.6\%$ of the leaf area; the equivalent radius is $\sqrt{a/\pi} = 5.0\ \mu\mathrm{m}$, and the denominator is $l + \frac{\pi}{2}\times 5.0 = 15.9\ \mu\mathrm{m}$. Substituting in Eq. (10.2):

$$
g_{\max} = \frac{2.49\times10^{-5}}{0.0245}\times\frac{2.0\times10^{8}\times 7.85\times10^{-11}}{1.59\times10^{-5}} \approx 1.0\ \mathrm{mol\,m^{-2}\,s^{-1}}.
$$
The actual working conductance is usually only 20%–50% of $g_{\max}$, since stomata are rarely fully open; $g_{\max}$ is used mainly to compare the gas-exchange potential of leaves of different species and different geological periods (fossils).

![Diffusion through small pores. A: diffusive flux through a single circular pore (8 µm deep) as a function of pore diameter (Eq. (10.1), driven by a 1 kPa water vapor pressure difference at 25 °C), compared with the flux extrapolated in proportion to area (tube diffusion with l ≫ r); flux through a small pore is proportional to diameter, and flux per unit area increases as the pore becomes smaller (right axis). B: anatomical maximum stomatal conductance (Eq. (10.2)) as a function of stomatal density and pore size; the dashed lines mark the leaf of Example 10.7.1](./plots/pore-diffusion.py)

## 10.8. Models of Stomatal Conductance and Optimal Stomatal Behavior

### 10.8.1. Empirical and Semi-Empirical Models

To build stomatal conductance into crop models and global land-surface models requires a formula for $g_{\mathrm{s}}$ that varies with the environment. Early models (Jarvis, 1976) wrote the influence of each factor, such as light, temperature, VPD and leaf water potential, as multiplicative functions. Ball, Woodrow and Berry (1987) found that under a wide range of conditions $g_{\mathrm{s}}$ is proportional to the net photosynthetic rate $A$, inversely proportional to the leaf-surface $\ce{CO2}$ concentration $c_{\mathrm{s}}$, and increases with the relative humidity $h_{\mathrm{s}}$ at the leaf surface:

**Formula 10.8.1 (Ball–Berry Model)**

$$
g_{\mathrm{s}} = g_0 + g_1\frac{A\,h_{\mathrm{s}}}{c_{\mathrm{s}}}. \tag{10.3}
$$

Here $g_0$ is the residual conductance at zero photosynthesis. The model embodies a key fact: the stoma is not a valve independent of photosynthesis, and its aperture varies in concert with carbon assimilation in the mesophyll, so that the intercellular $\ce{CO2}$ concentration $c_{\mathrm{i}}$ remains at a fairly stable fraction of the atmospheric concentration. Later models replaced the humidity term by VPD (Leuning, 1995), and Medlyn et al. (2011) derived from optimization theory (next subsection) a model of similar form whose parameters have clear meaning:

**Formula 10.8.2 (Medlyn Model)**

$$
g_{\mathrm{s}} = g_0 + 1.6\left(1 + \frac{g_1}{\sqrt{D}}\right)\frac{A}{c_{\mathrm{a}}}, \tag{10.4}
$$
where $D$ is the vapor pressure deficit at the leaf surface (kPa), $c_{\mathrm{a}}$ is the leaf-surface $\ce{CO2}$ concentration, and $g_1$ (in $\mathrm{kPa^{1/2}}$) reflects how "frugally" the plant uses water: the larger $g_1$, the more water may be lost per unit of carbon gained.

Combining Eq. (10.4) (with $g_0 = 0$) with Fick's law for $\ce{CO2}$, $A = \frac{g_{\mathrm{s}}}{1.6}(c_{\mathrm{a}} - c_{\mathrm{i}})$, and eliminating $g_{\mathrm{s}}$ and $A$ gives

$$
\frac{c_{\mathrm{i}}}{c_{\mathrm{a}}} = \frac{g_1}{g_1 + \sqrt{D}}. \tag{10.5}
$$

As $D$ increases, $c_{\mathrm{i}}/c_{\mathrm{a}}$ falls: the drier the air, the more "miserly" the stomata, and the more photosynthesis relies on lowering $c_{\mathrm{i}}$ to be maintained. In global data, $g_1$ is mostly around 4–5 $\mathrm{kPa^{1/2}}$ for C3 crops and herbs, about 3–4 for woody angiosperms, about 2–3 for gymnosperms, and about 1.5 for **C4 plants** (Lin et al., 2015). By Eq. (10.5), at $D = 1\ \mathrm{kPa}$ a C3 plant ($g_1 = 4$) has $c_{\mathrm{i}}/c_{\mathrm{a}} = 0.8$ and a C4 plant ($g_1 = 1.6$) has $0.62$, in the same direction as the typical values measured by carbon isotopes (about 0.7–0.8 for C3 and about 0.3–0.4 for C4); the lower $c_{\mathrm{i}}$ of C4 plants is one reason for their higher **water-use efficiency** ([7.13.8](/7.13.8)).

### 10.8.2. Cowan–Farquhar Optimization

Why do stomata behave this way? Cowan and Farquhar (1977) treated the stoma as an optimizer: for a fixed total amount of available water $\int E\,\mathrm{d}t$ over a period, maximize the carbon gain $\int A\,\mathrm{d}t$. Using the **method of Lagrange multipliers**, the objective functional $\int (A - \lambda E)\,\mathrm{d}t$ is made extremal with respect to $g_{\mathrm{s}}$ at each instant, giving the optimality condition:

**Theorem 10.8.1 (Cowan–Farquhar Optimality Condition)** If $A$ and $E$ are both smooth functions of $g_{\mathrm{s}}$ and the increase of $A$ with $g_{\mathrm{s}}$ gradually saturates, then the stomatal behavior that maximizes total carbon gain for a fixed amount of available water satisfies, at every instant,

$$
\frac{\partial E/\partial g_{\mathrm{s}}}{\partial A/\partial g_{\mathrm{s}}} = \lambda, \tag{10.6}
$$
where $\lambda$ is a time-independent constant (the marginal water cost of gaining one more unit of carbon).

**Proof** Divide the day into many short intervals, with conductance $g_k$ in interval $k$. Maximize $\sum_k A_k(g_k)\Delta t$ subject to the constraint $\sum_k E_k(g_k)\Delta t = W$. Form the Lagrangian $\mathcal{L} = \sum_k [A_k(g_k) - \lambda E_k(g_k)]\Delta t + \lambda W$ and set the partial derivative with respect to each $g_k$ to zero: $A_k'(g_k) = \lambda E_k'(g_k)$, that is, $E_k'/A_k' = \lambda$ is the same for all $k$. The saturation of $A$ ensures that this stationary point is a maximum. $\square$

Intuitively, if spending a unit of water at one moment buys more carbon than at another, it always pays to shift water from the latter to the former, until the "exchange rates" at all times are equal. This allows qualitative predictions: in the morning, when light is strong and VPD low, each unit of water buys much carbon and the stomata open wide; at midday, when VPD is high and the transpiration cost large, the stomata narrow (the photosynthetic "midday depression," [7.13.9](/7.13.9)). Substituting the Farquhar photosynthesis model into Eq. (10.6) and making approximations gives the Medlyn model, in which $g_1 \propto \sqrt{\Gamma^*\lambda}$ ($\Gamma^*$ is the $\ce{CO2}$ compensation point in the absence of dark respiration). When the soil dries $\lambda$ should decrease (water becomes more "expensive," and for the same carbon the plant will pay less water); strictly, more recent developments of optimization theory also include soil water depletion and the risk of xylem **cavitation** in the cost, which explains why stomata close earlier under drought than predicted with a fixed $\lambda$.

![Stomatal conductance models and optimization. A: g_s/A in the Medlyn model (Eq. (10.4)) as a function of leaf-surface vapor pressure deficit D, for a C3 plant (g₁ = 4 kPa^½) and a C4 plant (g₁ = 1.6 kPa^½); B: c_i/c_a as a function of D from Eq. (10.5); C: geometric meaning of the optimization: at one time of day both the photosynthetic rate A and the transpiration rate E increase with stomatal conductance, with A gradually saturating; at the optimal conductance the slope of the tangent to the A–E curve equals 1/λ, and the larger λ is (the "cheaper" the water), the farther to the right the optimum lies](./plots/medlyn-optimality.py)

## 10.9. Stomatal Development and Control of Density

### 10.9.1. The Stomatal Lineage and Peptide Signals

Stomata in the *Arabidopsis* leaf arise from a specialized lineage in the protoderm (morphology of the lineage in [7.12.4](/7.12.4#sec-4.3.2)): a protodermal cell becomes a meristemoid mother cell (MMC) and, by one **asymmetric cell division** (entry division), yields a smaller meristemoid and a larger stomatal lineage ground cell (SLGC); the meristemoid may undergo several further asymmetric amplifying divisions and then converts to a guard mother cell (GMC), which divides once symmetrically to form a pair of guard cells. The SLGC can differentiate into an ordinary pavement cell, or serve again as an MMC and undergo spacing divisions that produce secondary lineages. Because meristemoids and SLGCs can divide repeatedly, this "stomatal lineage" in fact generates most of the cells of the leaf epidermis.

The transitions among the three cell states are each driven by a bHLH transcription factor: SPEECHLESS (SPCH) initiates the entry and amplifying divisions, MUTE terminates the stem-cell behavior of the meristemoid and converts it to a GMC, and FAMA promotes the last division of the GMC and guard-cell differentiation; all of them form heterodimers with the bHLH-leucine zipper proteins SCREAM (SCRM) and SCRM2.

Cells outside the lineage control the number and spacing of stomata through secreted peptides. Of the EPIDERMAL PATTERNING FACTOR (EPF) family, EPF2 is secreted by MMCs and early meristemoids and EPF1 by GMCs; they are recognized by ERECTA-family receptor kinases (together with the receptor-like protein TMM) on neighboring cells and inhibit those cells from forming new meristemoids. The result is that two adjacent stomata are separated by at least one cell (the "one-cell-spacing rule"), which ensures that every stoma is surrounded by epidermal cells with which it can exchange $\ce{K+}$ and water, and reduces overlap of the diffusion shells of adjacent stomata (Section 10.7.1). EPF2–ERECTA mainly regulates stomatal number and density, and EPF1 mainly regulates spacing. STOMAGEN (EPFL9) of the same family is secreted by the underlying mesophyll, enters the epidermis, competes with EPF for the receptor, and promotes stomatal formation; the mesophyll thereby matches stomatal number to its own demand for $\ce{CO2}$. This is an example of **lateral inhibition** ([7.3.24](/7.3.24)) in the plant epidermis, except that the signal is a secreted peptide rather than a membrane-bound ligand.

### 10.9.2. Environmental Adjustment of Stomatal Density

The response of stomatal density to the environment has long-term adaptive significance:

- $\ce{CO2}$: in most plants, leaves that develop under high $\ce{CO2}$ have lower stomatal density and stomatal index. Comparison of herbarium specimens collected over more than two hundred years shows that the stomatal density of several temperate trees has fallen by about 40% since the Industrial Revolution (Woodward, 1987). Mutants of the *Arabidopsis HIC* (HIGH CARBON DIOXIDE) gene instead have more stomata under high $\ce{CO2}$, showing that this response is under genetic control. Because of this relationship, the stomatal index of fossil leaves is used as a proxy for reconstructing paleoatmospheric $\ce{CO2}$ concentration.
- Light: leaves that develop in strong light have higher stomatal density. The light and $\ce{CO2}$ conditions sensed by mature leaves can determine the stomatal density of new leaves through some systemic signal, even when the new leaves themselves are in different conditions.
- Water: drought often lowers the stomatal density of new leaves.

Lowering stomatal density is one route to improving crop water-use efficiency: overexpressing *EPF* genes in rice, barley and other crops markedly lowers stomatal density, reducing water loss under drought with little loss of yield, because under normal conditions the actual conductance is far below $g_{\max}$ (Section 10.7.2). Conversely, too low a stomatal density limits photosynthesis and transpirational cooling in strong light, so there is a favorable range that depends on the environment.

## Summary

The causal chain of stomatal opening and closing and the main players at each level:

| Level | Opening | Closing |
|---|---|---|
| Environmental signals | Light (especially blue), low $c_{\mathrm{i}}$, high humidity, moderate temperature | Darkness, high $c_{\mathrm{i}}$, high VPD, drought, ABA, strong wind |
| Photoreceptors / receptors | Phototropins phot1 and phot2 (main); cryptochromes, phytochrome B; photosynthesis in guard cells and mesophyll | PYR/PYL/RCAR (ABA); βCA1/4, HT1 ($\ce{CO2}$) |
| Signals | BLUS1 → PP1 → phosphorylation of the H⁺-ATPase C terminus + 14-3-3 | PP2C inhibited → OST1 (SnRK2.6); RBOH → ROS → $\ce{Ca^2+}$ → CPK; phosphatidic acid inhibits PP1 |
| Executors in the membrane | H⁺-ATPase activated (hyperpolarization); inward $\ce{K+}$ channel KAT1; $\ce{H+}$–$\ce{Cl-}$ symport; S-type anion channels inhibited | SLAC1 (S-type) and QUAC1 (R-type) anion channels open (depolarization); outward $\ce{K+}$ channel GORK; H⁺-ATPase and KAT1 inhibited |
| Solutes | $\ce{K+}$ 100 → 400–800 mM, $\ce{Cl-}$, malate; sucrose in the afternoon | $\ce{K+}$ and anions leave, sucrose decreases, starch is synthesized |
| Result | $\Psi_{\mathrm{s}}$ falls by about 2 MPa, turgor rises to 4–5 MPa | Turgor falls, plasma membrane area decreases (endocytosis) |

Kidney-shaped and dumbbell-shaped guard cells:

| | Kidney-shaped | Dumbbell-shaped |
|---|---|---|
| Distribution | Most dicots, many monocots, ferns, gymnosperms | Grasses, sedges |
| Wall thickening | Ventral and lateral walls thick, dorsal wall thin | Middle part thick, bulbous ends thin |
| Microfibrils | Radial about the pore | Radial across the cell |
| Mode of opening | Dorsal wall stretches, cell bows outward | Ends swell and push the middle parts apart |
| Subsidiary cells | Present or absent | Always a pair, serving as reservoirs of $\ce{K+}$ and water |
| Speed of movement | Slower | Faster |

Main equations:

| Equation | Content |
|---|---|
| $\Delta\Psi_{\mathrm{s}} = -\Delta c\,RT$ | Change in solute potential caused by solute accumulation (Example 10.3.1) |
| $E_{\ce{K}} = \frac{RT}{F}\ln\frac{[\ce{K+}]_{\mathrm{o}}}{[\ce{K+}]_{\mathrm{i}}}$ | Determines the direction of $\ce{K+}$ transport (Example 10.3.2) |
| Eq. (10.1) $J = \pi r^2 D\Delta c/(l + \frac{\pi}{2}r)$ | Diffusion through a single pore; for a shallow pore $J \approx 2rD\Delta c$ (small-pore diffusion law, Definition 10.7.1) |
| Eq. (10.2) $g_{\max} = \frac{D_{\mathrm{w}}}{v}\frac{Na}{l + \frac{\pi}{2}\sqrt{a/\pi}}$ | Anatomical maximum stomatal conductance (Example 10.7.1) |
| $g_{\mathrm{s}} = E/\Delta w$, $g_{\mathrm{c}} = g_{\mathrm{s}}/1.6$ | Stomatal conductance (Definition 10.7.2) |
| Eq. (10.3) $g_{\mathrm{s}} = g_0 + g_1 A h_{\mathrm{s}}/c_{\mathrm{s}}$ | Ball–Berry model |
| Eq. (10.4) $g_{\mathrm{s}} = g_0 + 1.6(1 + g_1/\sqrt{D})A/c_{\mathrm{a}}$ | Medlyn model |
| Eq. (10.5) $c_{\mathrm{i}}/c_{\mathrm{a}} = g_1/(g_1 + \sqrt{D})$ | Consequence of the Medlyn model |
| Eq. (10.6) $\partial E/\partial A = \lambda$ | Cowan–Farquhar optimality condition (Theorem 10.8.1) |

Stomatal development: MMC →(SPCH, asymmetric entry division) meristemoid →(MUTE) GMC →(FAMA, symmetric division) guard cells; EPF1 and EPF2 inhibit, via the ERECTA family and TMM, and mesophyll STOMAGEN promotes, stomatal formation; high $\ce{CO2}$ lowers stomatal density.

## Questions

1. The solute potential of a plant's guard cell when closed is $-1.5\ \mathrm{MPa}$. On opening it takes up 300 mM $\ce{K+}$ from the apoplast, 2/3 of whose charge is balanced by $\ce{Cl-}$ and the rest by newly synthesized malate; at the same time 50 mM sucrose accumulates from starch hydrolysis. If the water potential of the guard cell is always $-0.6\ \mathrm{MPa}$, find the turgor before and after opening (25 °C).

   **Answer** When closed, $\Psi_{\mathrm{p}} = \Psi_{\mathrm{w}} - \Psi_{\mathrm{s}} = -0.6 - (-1.5) = 0.9\ \mathrm{MPa}$. Solutes added on opening: $\ce{K+}$ 300 mM, $\ce{Cl-}$ 200 mM, malate 50 mM to balance 100 mM of positive charge, and sucrose 50 mM, for a total of $\Delta c = 600\ \mathrm{mM}$. $\Delta\Psi_{\mathrm{s}} = -600 \times 8.314 \times 298.15\ \mathrm{Pa} = -1.49\ \mathrm{MPa}$, so when open $\Psi_{\mathrm{s}} = -2.99\ \mathrm{MPa}$ and $\Psi_{\mathrm{p}} = -0.6 + 2.99 \approx 2.4\ \mathrm{MPa}$. (In reality, after water enters, the cell volume increases and the solutes are diluted, so the turgor increment is slightly smaller than this estimate.)

2. In a patch-clamp experiment the plasma membrane potential of an opening guard cell is measured as $-130\ \mathrm{mV}$ and cytosolic $\ce{K+}$ as 200 mM. (a) At what apoplastic $\ce{K+}$ concentration can $\ce{K+}$ still enter passively? (b) After ABA treatment the membrane potential becomes $-50\ \mathrm{mV}$; with apoplastic $\ce{K+}$ at 10 mM, in which direction does $\ce{K+}$ move, and through which class of channel?

   **Answer** (a) Passive entry requires $V < E_{\ce{K}}$, that is, $-130\ \mathrm{mV} < 25.7\ \mathrm{mV}\times\ln([\ce{K+}]_{\mathrm{o}}/200)$, giving $[\ce{K+}]_{\mathrm{o}} > 200\,\mathrm{e}^{-130/25.7}\ \mathrm{mM} = 200 \times 6.4\times10^{-3} \approx 1.3\ \mathrm{mM}$. As long as apoplastic $\ce{K+}$ exceeds about 1.3 mM, the inward channels can take up $\ce{K+}$ down the electrochemical gradient. (b) $E_{\ce{K}} = 25.7 \times \ln(10/200) = -77\ \mathrm{mV}$, and $V - E_{\ce{K}} = -50 - (-77) = +27\ \mathrm{mV} > 0$; the driving force is outward, and $\ce{K+}$ leaves through the depolarization-activated outward-rectifying $\ce{K+}$ channel (GORK).

3. Use Eq. (10.2) to compare the maximum stomatal conductance of two leaves: leaf X has a stomatal density of $100\ \mathrm{mm^{-2}}$ and a pore area of $150\ \mu\mathrm{m^2}$; leaf Y has a stomatal density of $300\ \mathrm{mm^{-2}}$ and a pore area of $50\ \mu\mathrm{m^2}$; both have a pore depth of 8 µm, and the total pore area is the same. Which has the larger $g_{\max}$? What does this show?

   **Answer** Both have $Na = 1.5\%$. For X the equivalent radius is $\sqrt{150/\pi} = 6.91\ \mu\mathrm{m}$ and the denominator is $8 + 1.571\times6.91 = 18.9\ \mu\mathrm{m}$; for Y the equivalent radius is $3.99\ \mu\mathrm{m}$ and the denominator is $8 + 6.27 = 14.3\ \mu\mathrm{m}$. $g_{\max} = (D_{\mathrm{w}}/v)\,Na/\text{denominator}$, with $D_{\mathrm{w}}/v = 1.02\times10^{-3}\ \mathrm{mol\,m^{-1}\,s^{-1}}$: for X, $1.02\times10^{-3}\times0.015/1.89\times10^{-5} \approx 0.81$, and for Y, $\approx 1.07\ \mathrm{mol\,m^{-2}\,s^{-1}}$. For the same total pore area, small and numerous stomata give the larger conductance, a direct consequence of the small-pore diffusion law; in the fossil record, during periods of falling atmospheric $\ce{CO2}$ land plants evolved small, dense stomata, obtaining higher conductance from a smaller total area.

4. According to the Medlyn model ($g_0 = 0$, $g_1 = 4\ \mathrm{kPa^{1/2}}$), a leaf at $c_{\mathrm{a}} = 420\ \mu\mathrm{mol\,mol^{-1}}$ and $D = 1\ \mathrm{kPa}$ has $A = 20\ \mu\mathrm{mol\,m^{-2}\,s^{-1}}$. (a) Find $g_{\mathrm{s}}$ and $c_{\mathrm{i}}$. (b) At midday $D$ rises to $2.25\ \mathrm{kPa}$; if $A$ is unchanged, what does $g_{\mathrm{s}}$ become? How does the transpiration rate ($E \approx g_{\mathrm{s}}D/p$, $p = 100\ \mathrm{kPa}$) change?

   **Answer** (a) $g_{\mathrm{s}} = 1.6\times(1 + 4/1)\times20/420 = 0.381\ \mathrm{mol\,m^{-2}\,s^{-1}}$; $c_{\mathrm{i}}/c_{\mathrm{a}} = 4/(4+1) = 0.8$, so $c_{\mathrm{i}} = 336\ \mu\mathrm{mol\,mol^{-1}}$. (b) $g_{\mathrm{s}} = 1.6\times(1 + 4/1.5)\times20/420 = 0.279\ \mathrm{mol\,m^{-2}\,s^{-1}}$, a decrease of 27%. $E$ changes from $0.381\times1/100 = 3.8$ to $0.279\times2.25/100 = 6.3\ \mathrm{mmol\,m^{-2}\,s^{-1}}$: the stomata have narrowed, but the driving force has increased more, so transpiration still rises by about 65%, and the water-use efficiency $A/E$ falls from 5.2 to $3.2\ \mathrm{mmol\,mol^{-1}}$. To maintain $A$ unchanged, $c_{\mathrm{i}}$ would actually fall to $0.73c_{\mathrm{a}}$, and the leaf must have enough photosynthetic capacity to use the lower $c_{\mathrm{i}}$.

5. You are studying the response of the stomata of a newly discovered plant to light. In isolated epidermis, blue light causes opening. Design experiments to answer in turn: (a) Does opening come from photosynthesis in the guard cells themselves or from a specific blue-light receptor? (b) If it is a specific blue-light response, how can you tell whether it depends on phototropin? (c) What would the behavior of the *Arabidopsis* homologous mutants *npq1* and *phot1 phot2* of this plant tell you?

   **Answer** (a) Use the dual-beam experiment: first saturate guard-cell photosynthesis with saturating red light and then superimpose low-intensity blue light; if the pore opens further, a blue-light response independent of photosynthesis exists. DCMU treatment can also be used: partial inhibition indicates a nonphotosynthetic component. If red light in place of blue light causes opening and this is inhibited by DCMU, guard-cell photosynthesis is at work. (b) Determine whether the action spectrum has the "three-finger" shape between 400 and 500 nm; test whether blue light causes acidification and swelling of guard-cell protoplasts and whether this is blocked by vanadate, and examine phosphorylation of the H⁺-ATPase C terminus and binding of 14-3-3; most directly, use genetic means (knockout or silencing of the phototropin genes) to see whether the blue-light response disappears. (c) *phot1 phot2* does not open in low-intensity blue light, showing that phototropin is the main blue-light receptor; *npq1* (lacking zeaxanthin) does not show the green-light reversal of the blue-light response while *phot1 phot2* does, showing that green-light reversal depends on zeaxanthin and not on phototropin. The two take part in different processes, and the phenotype of *npq1* cannot be used to prove that zeaxanthin is the main receptor for blue-light opening.
