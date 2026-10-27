---
title: Membrane Transport, Cell Volume and Membrane Potential
description: Membrane transport seen from the whole cell. Bilayer permeability, simple and carrier-mediated diffusion; the Na⁺/K⁺ pump and the pump–leak model (ouabain makes cells swell and depolarize); osmosis, the Boyle–van 't Hoff relation, osmotic fragility, turgor, contractile vacuoles and regulatory volume decrease and increase; P-, V- and ABC-type pumps in cells; transepithelial transport in enterocytes and gastric parietal cells; the resting potential from the Nernst and Goldman–Hodgkin–Katz equations, the charge it takes, and the action potential in outline; mechanosensitive channels, Piezo and two-state gating by tension.
---

The molecules that move solutes across membranes, **transporters**, **ion channels** and ATP-driven pumps, are described in [7.1.13](/7.1.13), and the thermodynamics of transport against an **electrochemical potential** in [6.3.13](/6.3.13) and [6.3.18](/6.3.18). This chapter asks what these molecules do together for a cell. Three cellular properties emerge from their combined activity and from nothing else: the cell's ion composition, which is far from that of its surroundings (5.1); its volume, which a cell with impermeant macromolecules inside could not keep without continuous pumping (5.2, 5.3); and its membrane potential (5.6). The same proteins, arranged asymmetrically in the two membrane domains of an epithelial cell, move salt, sugar and acid across whole tissues (5.5), and channels that open when the membrane is stretched let cells feel force (5.7). The thread through the chapter is the pump–leak model, a set of equations in which a single pump and three leaks produce all three properties at once; it is the first systems model of this course, and it shows how a steady state that looks like equilibrium is in fact maintained by a continuous flow of energy. The membrane domains used here are those of [7.3.4](/7.3.4#sec-4.6.3); the electrical signaling of neurons is the subject of [7.16](/7.16), and the physiology of the kidney and intestine of [7.14](/7.14).

## 5.1. Principles Seen from the Cell

### 5.1.1. A Cell Is Not at Equilibrium with Its Surroundings

The cytosol of a mammalian cell differs from the extracellular fluid in almost every ion.

| Ion | Cytosol / mM | Extracellular / mM | Nernst potential at $37\,^\circ\mathrm{C}$ (inside relative to outside) |
|---|---|---|---|
| $\ce{Na+}$ | $5$–$15$ | $145$ | $+60$ to $+90\,\mathrm{mV}$ |
| $\ce{K+}$ | $140$ | $5$ | $-89\,\mathrm{mV}$ |
| $\ce{Mg^2+}$ (free) | $0.5$ | $1$–$2$ | — |
| $\ce{Ca^2+}$ (free) | $10^{-4}$ | $1$–$2$ | about $+125\,\mathrm{mV}$ |
| $\ce{H+}$ | $7\times10^{-5}$ (pH 7.2) | $4\times10^{-5}$ (pH 7.4) | $-12\,\mathrm{mV}$ |
| $\ce{Cl-}$ | $5$–$15$ | $110$ | $-53$ to $-82\,\mathrm{mV}$ |

(MBoC 7e, Table 11–1.) Each compartment is electrically neutral: the excess of cations inside is balanced not by $\ce{Cl-}$ but by fixed anions, the negatively charged proteins, nucleic acids and metabolites that cannot leave the cell. The **Nernst equation** ([6.3.13](/6.3.13#sec-13.9.2)) gives the potential at which each ion would be in equilibrium across the membrane; the spread of these potentials from $-89$ to $+125\,\mathrm{mV}$ shows that a single membrane potential cannot put all ions in equilibrium at once. The cell maintains its composition by pumping.

### 5.1.2. The Bilayer as a Barrier and the Two Classes of Transport Proteins

A protein-free **lipid bilayer** is permeable to small nonpolar molecules ($\ce{O2}$, $\ce{CO2}$, steroid hormones), moderately to small uncharged polar ones (water, ethanol, urea, glycerol), poorly to sugars and amino acids, and practically impermeable to ions: the permeability coefficient of $\ce{Na+}$ is about $10^9$ times smaller than that of water ([7.1.13](/7.1.13#sec-13.3.2) explains why). Almost every solute a cell needs therefore crosses its membranes through proteins.

![Why cells need transport proteins. A: permeability coefficients of a protein-free phospholipid bilayer (order-of-magnitude values from synthetic bilayers), spanning twelve orders of magnitude from O₂ and CO₂ to Na⁺. B: the initial rate of uptake rises linearly with the external concentration for simple diffusion through the bilayer, but saturates for transport by a carrier (Michaelis–Menten form, Kₜ = 1.5 mM as for glucose and GLUT1); at physiological glucose concentrations the carrier is far faster](./plots/permeability-kinetics.py)

The two classes of transport proteins differ in mechanism and rate ([7.1.13](/7.1.13#def-13.3.1)): transporters (carriers) bind their solute and change conformation, moving $1$ to $10^3$ molecules per second and saturating like enzymes, with a $K_{\mathrm{t}}$ analogous to $K_{\mathrm{M}}$ (the **Michaelis–Menten equation**, [7.1.13](/7.1.13#fml-13.4.1)); channels form pores and conduct up to $10^7$–$10^8$ ions per second when open, without saturating at physiological concentrations, and are gated by voltage, ligands or mechanical force. Only transporters can carry out **active transport**; channels allow only **passive transport**. Active transport is driven in three ways: by ATP hydrolysis in pumps (primary active transport), by the downhill flow of another solute through **cotransporters** (**secondary active transport**), and, in some bacteria and archaea, by light.

## 5.2. The Na⁺/K⁺ Pump and the Pump–Leak Model

### 5.2.1. Four Jobs of One Pump

The **Na⁺/K⁺-ATPase** ([7.1.13](/7.1.13#def-13.5.2)) moves three $\ce{Na+}$ out and two $\ce{K+}$ in for each ATP, against both gradients. Present in the plasma membrane of virtually every animal cell, it uses a quarter to a third of the ATP of a resting cell, and half or more in neurons and in kidney tubules. At the level of the cell it has four jobs, all consequences of the same flux:

1. it maintains the $\ce{Na+}$ and $\ce{K+}$ gradients;
2. through the $\ce{K+}$ gradient and the $\ce{K+}$ leak channels, it is the ultimate source of the resting membrane potential (5.6), to which its own electrogenic current adds only a few millivolts;
3. the $\ce{Na+}$ gradient it builds drives secondary active transport: uptake of glucose and amino acids, export of $\ce{Ca^2+}$ by $\ce{Na+}$–$\ce{Ca^2+}$ exchange, regulation of pH by $\ce{Na+}$–$\ce{H+}$ exchange;
4. it keeps the cell's volume constant, the job that is least obvious and that the following model makes clear.

### 5.2.2. The Pump–Leak Model

A cell contains impermeant macromolecules and metabolites, mostly anions, at a concentration of order $100\,\mathrm{mM}$. If the membrane were permeable to $\ce{Na+}$, $\ce{K+}$ and $\ce{Cl-}$ and nothing else happened, these ions would distribute in a **Donnan equilibrium** ([6.3.21](/6.3.21#def-21.9.5)): the impermeant anions inside attract extra cations and repel $\ce{Cl-}$, but the total concentration of particles inside always exceeds that outside, so water enters by **osmosis** ([7.1.2](/7.1.2#sec-2.1.6)). In a cell without a wall, nothing stops the water, and the cell swells until it bursts. Daniel Tosteson and Joseph Hoffman (1960) explained, for red blood cells, how cells escape this fate.

**Definition 5.2.1 (Pump–Leak Model)** In the **pump–leak model**, the ion content and volume of an animal cell are a steady state, not an equilibrium: each ion leaks passively across the plasma membrane down its electrochemical gradient, the Na⁺/K⁺ pump moves $\ce{Na+}$ and $\ce{K+}$ back at the same rate, and water moves until the osmolarity inside equals that outside. Because $\ce{Na+}$ that leaks in is pumped out as fast as it enters, $\ce{Na+}$ behaves as if it were impermeant, and the extracellular $\ce{Na+}$ balances osmotically the impermeant anions inside.

The model is a set of ordinary differential equations. For the amounts $n_j$ of $\ce{Na+}$, $\ce{K+}$ and $\ce{Cl-}$ in a cell of volume $V$ and membrane area $A$,

$$
\frac{\mathrm{d}n_{\mathrm{Na}}}{\mathrm{d}t} = -\Phi_{\mathrm{Na}} - 3J_{\mathrm{p}}, \qquad
\frac{\mathrm{d}n_{\mathrm{K}}}{\mathrm{d}t} = -\Phi_{\mathrm{K}} + 2J_{\mathrm{p}}, \qquad
\frac{\mathrm{d}n_{\mathrm{Cl}}}{\mathrm{d}t} = -\Phi_{\mathrm{Cl}}, \qquad
\frac{\mathrm{d}V}{\mathrm{d}t} = L_{\mathrm{p}}ART\left(\frac{n_{\mathrm{Na}} + n_{\mathrm{K}} + n_{\mathrm{Cl}} + n_X}{V} - c_{\mathrm{o}}\right),
$$
where $\Phi_j$ is the outward leak of ion $j$, given by the Goldman–Hodgkin–Katz flux equation for its permeability $P_j$ and the membrane potential $V_{\mathrm{m}}$ (5.6.2); $J_{\mathrm{p}}$ is the pump rate in cycles per second, which rises steeply with cytosolic $\ce{Na+}$ (three sites); $n_X$ is the amount of impermeant solute; $c_{\mathrm{o}}$ is the external osmolarity; and $L_{\mathrm{p}}$ is the hydraulic conductivity of the membrane. The membrane potential is found at each instant from the condition that the net current is zero, $F(\Phi_{\mathrm{Na}} + \Phi_{\mathrm{K}} - \Phi_{\mathrm{Cl}} + J_{\mathrm{p}}) = 0$: because the membrane capacitance is tiny (Example 5.6.1), charge cannot accumulate. With realistic parameters the model reaches a steady state of $11\,\mathrm{mM}$ $\ce{Na+}$, $141\,\mathrm{mM}$ $\ce{K+}$, $8\,\mathrm{mM}$ $\ce{Cl-}$ and $V_{\mathrm{m}} = -71\,\mathrm{mV}$, close to measured values.

![The pump–leak model of an animal cell (leaks with P_Na : P_K : P_Cl = 0.05 : 1 : 0.4, pump with three Na⁺ sites, impermeant anions of mean charge −1.1; external Na⁺ 145, K⁺ 5, Cl⁻ 110 mM). A: at t = 10 min the pump is blocked with ouabain. Na⁺ leaks in and K⁺ out, at first in nearly equal amounts, so the volume hardly changes; the gradients run down within about two hours. B: as K⁺ leaves, the membrane depolarizes (dashed; the small immediate jump is the loss of the pump's own electrogenic current), Cl⁻ is no longer held out by the negative potential and enters, and water follows: the cell swells steadily towards a Donnan equilibrium that, in a cell without a wall, it would never reach before bursting](./plots/pump-leak-model.py)

The simulation reproduces three classical observations. Ouabain makes animal cells, and slices of kidney or brain, swell; the swelling is slow, because it requires the run-down of the $\ce{K+}$ gradient; and it is accompanied by depolarization and $\ce{Cl-}$ uptake. The same sequence happens in ischemia, when ATP runs out: cytotoxic edema of brain cells after a stroke is the pump–leak model with the pump switched off.

**Example 5.2.1** How many pumps does a cell need? In the simulation, the steady-state pump rate is $J_{\mathrm{p}} = 3.4\times10^{-17}\,\mathrm{mol\,s^{-1}}$, about $2\times10^7$ cycles per second. At a turnover of about $100\,\mathrm{s^{-1}}$ this requires some $2\times10^5$ pumps, within the measured range of $10^5$–$10^7$ per cell (red cells have only a few hundred, neurons millions). Each cycle uses one ATP, so this model cell spends $2\times10^7$ ATP per second on its ion balance. Cultured mammalian cells consume of order $10^9$ ATP per second in total, so the model cell, with its small area and tight membrane, would use only a few percent; the much larger share in real tissues (a quarter of the resting energy of the body) reflects larger membrane areas and leak permeabilities, and in neurons the extra $\ce{Na+}$ entry during electrical activity. The cost of the pump is set by the leaks it has to balance.

## 5.3. Osmosis and Cell Volume

### 5.3.1. Cells as Osmometers

Water crosses all biological membranes, slowly through the bilayer and quickly through **aquaporins** ([7.1.13](/7.1.13#sec-13.6.1)), so a cell placed in a solution of different **osmolarity** gains or loses water within seconds to minutes until the osmolarities inside and outside are equal (the **osmotic pressure** of a dilute solution, $\varPi = cRT$, is treated in [6.3.5](/6.3.5)). Solutions are hypotonic, isotonic or hypertonic according to whether a cell swells, keeps its volume or shrinks in them; tonicity depends on the effective, impermeant solutes only, so a solution of urea that is isosmotic with plasma is hypotonic to cells, which take up urea and water and swell.

**Formula 5.3.1 (Boyle–van 't Hoff Relation)** A cell that behaves as an ideal osmometer, containing a fixed amount of impermeant solute and an osmotically inactive volume $b$ (solids and bound water, as a fraction of the normal volume $V_0$), has in a medium of osmolarity $\varPi$ the equilibrium volume

$$
\frac{V}{V_0} = b + (1 - b)\frac{\varPi_0}{\varPi},
$$
where $\varPi_0$ is the normal (isotonic) osmolarity, about $290\,\mathrm{mOsm\,L^{-1}}$ in mammals.

Human red cells obey the relation over a wide range, with $b \approx 0.4$ (hemoglobin and its bound water). A red cell can swell without stretching its membrane only until it becomes a sphere ([7.3.4](/7.3.4#sec-4.6.4)): with $40\,\%$ excess area, that happens at about $1.7\,V_0$, which by Formula 5.3.1 corresponds to $\varPi/\varPi_0 \approx 0.46$, about $0.42\,\%$ NaCl. Below this concentration red cells burst and release their hemoglobin (hemolysis), the empty membranes being the ghosts of [7.3.4](/7.3.4#ex-4.3.1).

![Cell volume and osmolarity. A: model of the osmotic fragility test. Erythrocytes follow the Boyle–van 't Hoff relation (b = 0.4) and lyse when their volume reaches that of a sphere of the same area: about 1.7 V₀ for normal biconcave cells, but only about 1.25 V₀ for the spherocytes of hereditary spherocytosis, which therefore lyse in much less dilute saline (about 0.6 % instead of 0.4 % NaCl; 6 % cell-to-cell variation in critical volume). B: regulatory volume decrease. A cell moved from 290 to 200 mOsm L⁻¹ first swells as an osmometer; volume-activated K⁺ and Cl⁻ channels then release KCl, and water follows, so the volume returns towards normal within minutes. With the channels blocked (dashed) the cell stays at its Boyle–van 't Hoff volume](./plots/osmotic-volume.py)

### 5.3.2. Three Strategies: Pump, Wall, Expel

Cells have solved the osmotic problem of 5.2.2 in three ways. Animal cells pump ions and make $\ce{Na+}$ effectively impermeant, as described by the pump–leak model. Plants, fungi and most bacteria let the internal osmolarity exceed the external one and resist the resulting inflow of water with a rigid wall.

**Definition 5.3.1 (Turgor Pressure)** **Turgor pressure** is the hydrostatic pressure inside a walled cell, exerted on the cell wall, that balances the difference in osmotic pressure between the cytoplasm (or vacuole) and the surroundings, so that the chemical potential of water is equal inside and outside.

Turgor is typically $0.3$–$1\,\mathrm{MPa}$ in plant cells, several atmospheres; it keeps nonwoody tissues rigid, and its loss is wilting. Plants maintain the high internal osmolarity by accumulating ions and organic solutes in the vacuole, using a plasma membrane $\ce{H+}$-ATPase that sets their membrane potential at $-120$ to $-200\,\mathrm{mV}$ and drives the uptake of $\ce{K+}$ and other solutes; the controlled expansion of cells against their walls by turgor is how plant cells grow ([7.3.23](/7.3.23), [7.13](/7.13)). Freshwater protists such as *Paramecium*, which have no wall and live in strongly hypotonic water, collect the water that enters into contractile vacuoles and expel it to the outside every few seconds.

### 5.3.3. Regulation of Cell Volume

Animal cells do not behave as perfect osmometers for long. Within minutes after an osmotic shock they move solutes to restore their volume.

**Definition 5.3.2 (Regulatory Volume Decrease and Increase)** **Regulatory volume decrease** (RVD) is the return of a swollen cell towards its normal volume by the release of $\ce{K+}$, $\ce{Cl-}$ and organic osmolytes, followed by water; **regulatory volume increase** (RVI) is the return of a shrunken cell towards its normal volume by the uptake of $\ce{Na+}$, $\ce{K+}$ and $\ce{Cl-}$, followed by water.

In RVD, swelling opens volume-regulated anion channels (formed by LRRC8 proteins), which release $\ce{Cl-}$ and organic osmolytes such as taurine, and $\ce{K+}$ channels, so that KCl leaves. In RVI, the $\ce{Na+}$–$\ce{K+}$–$2\ce{Cl-}$ cotransporter NKCC1 and parallel $\ce{Na+}$–$\ce{H+}$ and $\ce{Cl-}$–$\ce{HCO3-}$ exchangers take up NaCl, and the pump then exchanges the $\ce{Na+}$ for $\ce{K+}$. Cells exposed to chronic hypertonicity, such as those of the renal medulla, accumulate compatible organic osmolytes (sorbitol, betaine, *myo*-inositol, taurine) that raise internal osmolarity without disturbing proteins as high ion concentrations would. How cells sense their volume is still not fully understood; candidates include macromolecular crowding, ionic strength and membrane tension (5.7).

## 5.4. Other Pumps in the Life of a Cell

The four families of ATP-driven pumps are described in [7.1.13](/7.1.13#sec-13.5.1). Their cellular roles:

| Pump | Where | What it does for the cell |
|---|---|---|
| Plasma membrane $\ce{Ca^2+}$-ATPase (PMCA), SERCA (P-type) | plasma membrane; ER and sarcoplasmic reticulum | keep cytosolic $\ce{Ca^2+}$ near $10^{-7}\,\mathrm{M}$, $10^4$ times below the outside, so that opening $\ce{Ca^2+}$ channels makes a signal ([7.1.14](/7.1.14#sec-14.3.2)); SERCA refills the ER store ([7.3.7](/7.3.7)) and relaxes muscle |
| $\ce{H+}$-ATPase (P-type) | plasma membrane of plants and fungi | sets the membrane potential and the $\ce{H+}$ gradient that drives nutrient uptake, the plant counterpart of the Na⁺/K⁺ pump |
| $\ce{H+}$/$\ce{K+}$-ATPase (P-type) | apical membrane of gastric parietal cells | secretes $\ce{HCl}$ up to $0.16\,\mathrm{M}$ (5.5.3) |
| V-type $\ce{H+}$-ATPase | lysosomes, endosomes, Golgi, secretory and synaptic vesicles, plant vacuoles; plasma membrane of osteoclasts and kidney intercalated cells | acidifies organelles (lysosomal pH 4.5–5, [7.3.11](/7.3.11)); the pH gradient drives neurotransmitter loading into synaptic vesicles; osteoclasts dissolve bone mineral |
| **ABC transporters** | plasma membrane, ER (TAP), peroxisomes | export drugs and lipids; MDR1 overexpression in more than $40\,\%$ of human cancers confers multidrug resistance ([7.3.26](/7.3.26)); TAP pumps peptides into the ER for antigen presentation ([7.15](/7.15)); yeast Ste6 exports the a-factor pheromone |
| F-type ATP synthase | inner mitochondrial, thylakoid and bacterial membranes | usually runs backward to make ATP ([7.1.23](/7.1.23)) |

## 5.5. Transepithelial Transport

### 5.5.1. Two Membrane Domains Make Transport Vectorial

**Definition 5.5.1 (Transepithelial Transport)** **Transepithelial transport** is the net movement of a solute across an epithelium from one side to the other, achieved by placing different transport proteins in the apical and basolateral membrane domains of each cell (transcellular route) and, for some solutes, by diffusion between the cells through the tight junctions (paracellular route).

Three conditions are necessary: the epithelial cells must be polarized, with distinct apical and basolateral sets of transporters; the tight junctions must seal the spaces between cells, so that what one membrane moves the other cannot let leak back; and they must also keep the two sets of membrane proteins from mixing ([7.3.4](/7.3.4#sec-4.6.3)). Water usually follows salt, through aquaporins or between the cells, so epithelia also move water.

### 5.5.2. Glucose Absorption in the Small Intestine

The enterocytes of the small intestine absorb glucose from the lumen even when its concentration there is lower than in the blood. The apical membrane, folded into microvilli, carries the symporter SGLT1, which couples the entry of one glucose to that of two $\ce{Na+}$ ions down their steep electrochemical gradient; this can concentrate glucose in the cell several thousandfold ([7.1.13](/7.1.13#fml-13.5.1) and [7.1.13](/7.1.13#ex-13.5.1)). The basolateral membrane carries the uniporter GLUT2, through which glucose leaves the cell down its concentration gradient into the interstitial fluid and blood, and the Na⁺/K⁺ pump, which returns the $\ce{Na+}$ to the blood and keeps the cytosolic $\ce{Na+}$ low. The overall process is the transport of glucose and $\ce{Na+}$ from lumen to blood, paid for by the ATP of the basolateral pump. Water follows the absorbed solute, which is why oral rehydration solution, glucose plus salt, can replace the fluid lost in cholera.

![Transepithelial transport. A: an enterocyte of the small intestine. Apical SGLT1, in the microvillus membrane, takes up 2 Na⁺ with each glucose; basolateral GLUT2 releases glucose into the blood; the basolateral Na⁺/K⁺ pump keeps cytosolic Na⁺ low and K⁺ leaves through basolateral K⁺ channels. B: a gastric parietal cell. Carbonic anhydrase makes H⁺ and HCO₃⁻; the apical H⁺/K⁺-ATPase pumps H⁺ into the lumen in exchange for K⁺, which returns to the lumen through apical K⁺ channels, and Cl⁻ follows through apical Cl⁻ channels, so HCl is secreted; HCO₃⁻ leaves across the basolateral membrane in exchange for Cl⁻ (the anion exchanger AE2). In both cells tight junctions seal the lateral spaces and separate the apical and basolateral membrane domains](./plots/transepithelial-transport.py)

### 5.5.3. Acid Secretion by Parietal Cells

Parietal cells of the gastric glands secrete hydrochloric acid at up to $0.16\,\mathrm{M}$ (pH about 0.8) into the stomach, a $\ce{H+}$ gradient of more than a millionfold across their apical membrane. Inside the cell, carbonic anhydrase converts $\ce{CO2}$ and water into $\ce{H+}$ and $\ce{HCO3-}$. The $\ce{H+}$/$\ce{K+}$-ATPase, a P-type pump, exchanges cytosolic $\ce{H+}$ for luminal $\ce{K+}$; $\ce{K+}$ recycles to the lumen through apical $\ce{K+}$ channels, and $\ce{Cl-}$ leaves through apical $\ce{Cl-}$ channels, so the net secretion is HCl. The $\ce{HCO3-}$ leaves on the basolateral side in exchange for $\ce{Cl-}$, which supplies the $\ce{Cl-}$ for secretion and makes the venous blood leaving the stomach alkaline after a meal (the "alkaline tide"). At rest the pumps are stored in the membranes of cytoplasmic tubulovesicles; histamine, acetylcholine and gastrin trigger their fusion with the apical membrane, which increases its area several-fold. The proton-pump inhibitors (omeprazole and its relatives) block the enzyme covalently and are among the most prescribed drugs.

**Example 5.5.1** What does it cost to pump one $\ce{H+}$ from the cytosol (pH 7.2) into gastric juice (pH 0.8)? The pump is electroneutral, so only the concentration terms count ([7.1.13](/7.1.13#fml-13.3.1)): $\Delta G = RT\ln 10 \times (7.2 - 0.8) = 5.94\,\mathrm{kJ\,mol^{-1}} \times 6.4 = 38\,\mathrm{kJ\,mol^{-1}}$ at $37\,^\circ\mathrm{C}$. Moving $\ce{K+}$ in from a lumen containing about $10\,\mathrm{mM}$ to a cytosol with $140\,\mathrm{mM}$ adds $RT\ln 14 \approx 7\,\mathrm{kJ\,mol^{-1}}$, so each $\ce{H+}/\ce{K+}$ exchange costs about $45\,\mathrm{kJ\,mol^{-1}}$. The free energy of ATP hydrolysis in cells is about $-50$ to $-60\,\mathrm{kJ\,mol^{-1}}$, so one ATP can drive at most one exchange at the lowest gastric pH; the pump indeed moves two $\ce{H+}$ per ATP when the lumen is less acidic and approaches one per ATP at maximal acidity. The limit of gastric acidity is thermodynamic.

## 5.6. The Membrane Potential

### 5.6.1. The Resting Potential

**Definition 5.6.1 (Resting Membrane Potential)** The **resting membrane potential** is the steady **membrane potential** $V_{\mathrm{m}} = \varphi_{\mathrm{in}} - \varphi_{\mathrm{out}}$ of a cell that is not being stimulated; it lies between $-20$ and $-120\,\mathrm{mV}$ in animal cells, depending on the cell type, and is a steady state in which the net current carried by all ions, including the current of electrogenic pumps, is zero.

The resting potential arises mainly from the $\ce{K+}$ gradient and the dominance of $\ce{K+}$ among the leak conductances of the resting membrane, provided by $\ce{K+}$ leak channels (two-pore-domain K2P and inward-rectifier channels). Consider first a membrane permeable to $\ce{K+}$ alone. $\ce{K+}$ ions diffuse out down their concentration gradient, leaving behind uncompensated negative charge, until the potential they create stops further net efflux: this is the $\ce{K+}$ equilibrium potential of the Nernst equation, $E_{\mathrm{K}} = (RT/F)\ln([\ce{K+}]_{\mathrm{o}}/[\ce{K+}]_{\mathrm{i}}) = -89\,\mathrm{mV}$ for the concentrations of 5.1.1. Real membranes are also somewhat permeable to $\ce{Na+}$ and $\ce{Cl-}$, and the potential is pulled away from $E_{\mathrm{K}}$ towards $E_{\mathrm{Na}}$ and $E_{\mathrm{Cl}}$, each in proportion to its permeability.

**Example 5.6.1** How much charge does it take to make the membrane potential? The membrane is a capacitor of about $1\,\mu\mathrm{F\,cm^{-2}}$. Charging a cell with $A = 1000\,\mu\mathrm{m^2} = 10^{-5}\,\mathrm{cm^2}$ to $-70\,\mathrm{mV}$ requires $Q = CAV = 10^{-6} \times 10^{-5} \times 0.07\,\mathrm{C} = 7\times10^{-13}\,\mathrm{C}$, or $4.4\times10^6$ monovalent ions. A cell of $2\,\mathrm{pL}$ with $140\,\mathrm{mM}$ $\ce{K+}$ contains $1.7\times10^{11}$ $\ce{K+}$ ions, forty thousand times more. Setting up or abolishing the membrane potential therefore leaves all concentrations practically unchanged and takes milliseconds; the cell is electroneutral everywhere except within about a **Debye length** ($\sim 1\,\mathrm{nm}$) of the membrane. This is why the pump–leak model can determine $V_{\mathrm{m}}$ by setting the net current to zero.

### 5.6.2. The Goldman–Hodgkin–Katz Equation

When several ions permeate, the membrane potential is a steady state, not an equilibrium ([6.3.13](/6.3.13#sec-13.9.2)), and depends on the relative permeabilities. The standard description assumes that each ion crosses the membrane independently by electrodiffusion (the Nernst–Planck equation) in a constant electric field.

**Formula 5.6.1 (Goldman–Hodgkin–Katz Equation)** If ion $j$ of valence $z_j$ crosses a membrane with permeability $P_j$, its outward flux per unit area at membrane potential $V_{\mathrm{m}}$ is, with $u_j = z_jFV_{\mathrm{m}}/RT$,

$$
\phi_j = P_j\,u_j\,\frac{c_{j,\mathrm{i}} - c_{j,\mathrm{o}}\mathrm{e}^{-u_j}}{1 - \mathrm{e}^{-u_j}}.
$$
For a membrane permeable to $\ce{K+}$, $\ce{Na+}$ and $\ce{Cl-}$, the potential at which the net current is zero is

$$
V_{\mathrm{m}} = \frac{RT}{F}\ln\frac{P_{\mathrm{K}}[\ce{K+}]_{\mathrm{o}} + P_{\mathrm{Na}}[\ce{Na+}]_{\mathrm{o}} + P_{\mathrm{Cl}}[\ce{Cl-}]_{\mathrm{i}}}{P_{\mathrm{K}}[\ce{K+}]_{\mathrm{i}} + P_{\mathrm{Na}}[\ce{Na+}]_{\mathrm{i}} + P_{\mathrm{Cl}}[\ce{Cl-}]_{\mathrm{o}}}.
$$
The flux equation gives zero flux at the Nernst potential of the ion; the voltage equation reduces to the Nernst equation when one permeability dominates.

**Proof** In the constant-field approximation the potential falls linearly across the membrane, and the Nernst–Planck flux $\phi = -D(\mathrm{d}c/\mathrm{d}x + c\,\mathrm{d}(zF\psi/RT)/\mathrm{d}x)$ is constant across it in the steady state. Multiplying by the integrating factor $\mathrm{e}^{zF\psi/RT}$ and integrating across a membrane of thickness $d$, with partition coefficient $\beta$ between water and membrane and $P = \beta D/d$, gives the flux equation. For monovalent ions the factors $u_j$ and $1 - \mathrm{e}^{-u}$ are the same for $\ce{K+}$ and $\ce{Na+}$; for $\ce{Cl-}$ ($z = -1$) the roles of inside and outside exchange. Setting the electric current $F(\phi_{\mathrm{K}} + \phi_{\mathrm{Na}} - \phi_{\mathrm{Cl}}) = 0$, the common factor cancels and the linear equation for $\mathrm{e}^{-u}$ (with $u = FV_{\mathrm{m}}/RT$) gives the voltage equation. $\square$

**Example 5.6.2** With the concentrations of 5.1.1 ($[\ce{Na+}]_{\mathrm{i}} = 12$, $[\ce{K+}]_{\mathrm{i}} = 140$, $[\ce{Cl-}]_{\mathrm{i}} = 8$; outside $145$, $5$, $110\,\mathrm{mM}$) and $P_{\mathrm{K}} : P_{\mathrm{Na}} : P_{\mathrm{Cl}} = 1 : 0.05 : 0.4$, the numerator is $5 + 7.25 + 3.2 = 15.45$ and the denominator $140 + 0.6 + 44 = 184.6$, so $V_{\mathrm{m}} = 26.7\,\mathrm{mV} \times \ln(0.0837) = -66\,\mathrm{mV}$, $23\,\mathrm{mV}$ positive of $E_{\mathrm{K}}$. The electrogenic pump, which moves $3\,\ce{Na+}$ out for $2\,\ce{K+}$ in, can be included by multiplying the $\ce{K+}$ terms by $r = 3/2$ (the Mullins–Noda form, valid when the pump balances the passive fluxes of $\ce{Na+}$ and $\ce{K+}$), which gives $-71\,\mathrm{mV}$: the pump's direct contribution is about $5\,\mathrm{mV}$.

![The membrane potential from the Goldman–Hodgkin–Katz equation (37 °C; inside Na⁺ 12, K⁺ 140, Cl⁻ 8 mM). A: as the external K⁺ concentration is raised (with Na⁺ + K⁺ = 150 mM), V_m follows the Nernst potential E_K at high [K⁺]ₒ but deviates from it at low [K⁺]ₒ, where the small Na⁺ permeability (P_Na : P_K = 0.05) becomes important; the dotted curve includes the electrogenic pump (r = 3/2). Measured resting potentials show exactly this shape, the classical evidence that the resting potential is mainly a K⁺ diffusion potential. B: V_m against P_Na/P_K: a rise in Na⁺ permeability by a factor of several hundred, as when voltage-gated Na⁺ channels open, carries the potential from near E_K to near E_Na, the peak of the action potential](./plots/ghk-potential.py)

The equation explains the main facts about membrane potentials. Raising external $\ce{K+}$ depolarizes cells, which is why hyperkalemia is dangerous to the heart and why concentrated KCl stops it. Changes in relative permeability change the potential quickly, without any change in concentrations: opening $\ce{Na+}$ or $\ce{Ca^2+}$ channels depolarizes, opening $\ce{K+}$ or (in mature neurons, where $E_{\mathrm{Cl}}$ is near or below the resting potential) $\ce{Cl-}$ channels hyperpolarizes or clamps the potential. These changes are the language of electrical signaling.

### 5.6.3. The Action Potential in Outline

In excitable cells (neurons, muscle, some endocrine cells) a depolarization beyond a threshold opens **voltage-gated channels** for $\ce{Na+}$, and the inflow of $\ce{Na+}$ depolarizes the membrane further, a positive feedback that drives $V_{\mathrm{m}}$ towards $E_{\mathrm{Na}}$ within about a millisecond. Inactivation of the $\ce{Na+}$ channels and the delayed opening of voltage-gated $\ce{K+}$ channels then return it to rest. The channels are described in [7.1.14](/7.1.14#sec-14.5.2); the quantitative model of Hodgkin and Huxley, propagation along axons and synaptic transmission are the subject of [7.16](/7.16) and [7.6](/7.6). For the cell biology of this chapter, two facts suffice. An action potential moves a negligible amount of charge (Example 5.6.1), so a neuron can fire thousands of times without its pumps before its gradients run down noticeably; and the pumps, by restoring the gradients over minutes, pay the energy bill afterwards, which makes signaling a major part of the energy budget of the brain.

## 5.7. Mechanosensitive Channels

### 5.7.1. Channels Gated by Membrane Tension

Cells are subject to forces: osmotic swelling, shear from flowing fluid, stretch of tissues, touch and sound. Some channels convert these forces directly into ion currents.

**Definition 5.7.1 (Mechanosensitive Channel)** A **mechanosensitive channel** is an ion channel whose opening probability is controlled by mechanical force, either by tension in the lipid bilayer itself ("force from lipids") or by force transmitted through tethers to the cytoskeleton or the extracellular matrix ("force from tethers").

In bacteria, mechanosensitive channels are osmotic safety valves. When an *E. coli* cell is moved into fresh water and swells, rising membrane tension opens first the channel of small conductance, MscS (a heptamer with a pore about $1.3\,\mathrm{nm}$ wide), and at higher tension the channel of large conductance, MscL (a pentamer whose pore opens to about $3\,\mathrm{nm}$). The cell loses ions, amino acids and sugars, more than $95\,\%$ of its small molecules, but keeps its macromolecules and survives a shock that would otherwise burst it. MscL opens at about $10\,\mathrm{mN\,m^{-1}}$, just below the tension at which the bilayer would rupture.

In animals, the main mechanically activated channels are Piezo1 and Piezo2, discovered by Ardem Patapoutian and colleagues in 2010 by silencing, one by one, candidate genes in a cell line that responded to poking with a current (Nobel Prize in Physiology or Medicine 2021, shared with David Julius for the heat- and capsaicin-sensitive channel TRPV1). A Piezo channel is a homotrimer of a very large protein (about 2500 residues) with 38 transmembrane helices per subunit; the cryo-EM structures (including those of Bailong Xiao's group) show three curved blades of transmembrane helix bundles arranged like a propeller around a central pore. The blades bend the surrounding membrane into a dome that bulges into the cytoplasm; tension in the membrane flattens the dome, the projected area of the channel increases, and the pore opens to cations, mainly $\ce{Ca^2+}$ and $\ce{Na+}$.

| Channel | Where | Function |
|---|---|---|
| Piezo2 | Merkel cells and sensory neurons of the skin, proprioceptors in muscle spindles, sensory endings in the lung and bladder | light touch, proprioception (people lacking Piezo2 have severe deficits of touch and body position), sensing of lung inflation and bladder filling |
| Piezo1 | endothelium, red blood cells, kidney, bone, many epithelia | shear stress sensing and vascular development (knockout mice die at mid-gestation); baroreception (with Piezo2); control of red cell volume |
| MscS, MscL | bacterial plasma membrane | osmotic safety valves |
| TREK/TRAAK K2P channels | neurons | tension-gated $\ce{K+}$ leak channels |

Gain-of-function mutations of *PIEZO1* cause hereditary xerocytosis: the channel lets in too much $\ce{Ca^2+}$, which opens $\ce{Ca^2+}$-activated $\ce{K+}$ channels (Gardos channels), so red cells lose KCl and water and become dehydrated, an example of the pump–leak balance shifted by one leak.

### 5.7.2. A Two-State Model of Gating by Tension

The simplest model treats the channel as having two states, closed and open, whose free energies differ by $\Delta G_0$ in a tension-free membrane, and whose areas in the plane of the membrane differ by $\Delta A$. A membrane tension $\tau$ (force per unit length) does work $\tau\Delta A$ on the channel when it opens.

**Formula 5.7.1 (Two-State Gating by Tension)** For a mechanosensitive channel with in-plane area change $\Delta A$ on opening, the open probability at membrane tension $\tau$ is the Boltzmann function

$$
P_{\mathrm{o}} = \frac{1}{1 + \exp\!\left[-\dfrac{(\tau - \tau_{1/2})\,\Delta A}{k_{\mathrm{B}}T}\right]}, \qquad \tau_{1/2} = \frac{\Delta G_0}{\Delta A},
$$
the mechanical analog of the voltage dependence of a voltage-gated channel, with $\Delta A$ in the role of the gating charge.

The model makes $\Delta A$ measurable from the steepness of the gating curve: the tension needed to raise $P_{\mathrm{o}}$ from $0.12$ to $0.88$, about $4k_{\mathrm{B}}T/\Delta A$, is small when the area change is large. For MscL, $\Delta A \approx 20\,\mathrm{nm^2}$ ($k_{\mathrm{B}}T = 4.3\,\mathrm{pN\,nm} = 4.3\,\mathrm{mN\,m^{-1}\,nm^2}$ at $37\,^\circ\mathrm{C}$), so the channel goes from mostly closed to mostly open over less than $1\,\mathrm{mN\,m^{-1}}$, consistent with the large structural change seen in its open and closed structures. Piezo1 is half-activated at about $1$–$3\,\mathrm{mN\,m^{-1}}$ in cell membranes, which lets it respond to the much smaller tensions of normal physiology. Because tension in a curved membrane depends on pressure and radius by the law of Laplace (the **Laplace pressure**, [6.3.19](/6.3.19)), a pressure step applied to a membrane patch in a pipette is the standard way to measure these curves by **patch clamp**.

![Gating of mechanosensitive channels by membrane tension. A: a Piezo channel in side view (schematic). In the closed state the three curved blades bend the membrane into a dome that bulges into the cytoplasm; tension flattens the dome, increasing the in-plane area of the channel, and the central pore opens to cations. B: open probability against tension from the two-state model (Formula 5.7.1, 37 °C) for MscS (τ½ = 5.5 mN m⁻¹, ΔA = 8 nm²) and MscL (10 mN m⁻¹, 20 nm²), the safety valves of bacteria, and for Piezo1 (τ½ = 1.4 mN m⁻¹; ΔA = 6 nm² is an illustrative value giving a graded response over the physiological range). Tensions at which bilayers usually rupture are shaded](./plots/piezo-gating.py)

## Summary

| Topic | Key points |
|---|---|
| Composition (5.1) | Cytosol low in $\ce{Na+}$, $\ce{Cl-}$, $\ce{Ca^2+}$ ($10^{-4}\,\mathrm{mM}$), high in $\ce{K+}$; neutrality from fixed anions; Nernst potentials from $-89$ ($\ce{K+}$) to $+125\,\mathrm{mV}$ ($\ce{Ca^2+}$); bilayer permeability spans 12 orders of magnitude; carriers saturate, channels conduct $10^7$–$10^8\,\mathrm{s^{-1}}$ |
| Pump–leak model (5.2, Definition 5.2.1, Example 5.2.1) | $3\ce{Na+}$ out, $2\ce{K+}$ in per ATP; four jobs: gradients, resting potential, secondary transport, volume; ODEs for ions and volume with GHK leaks and $V_{\mathrm{m}}$ from zero net current; ouabain or ischemia → $\ce{Na+}$ in, $\ce{K+}$ out, depolarization, $\ce{Cl-}$ entry, swelling; about $2\times10^5$ pumps, $20\,\%$ of ATP turnover |
| Volume (5.3, Formula 5.3.1, Definitions 5.3.1–5.3.2) | Boyle–van 't Hoff $V/V_0 = b + (1-b)\varPi_0/\varPi$; red cells lyse near $0.42\,\%$ NaCl, spherocytes earlier; tonicity counts only impermeant solutes; strategies: pump (animals), wall and turgor $0.3$–$1\,\mathrm{MPa}$ (plants, bacteria), contractile vacuoles (protists); RVD (LRRC8 anion channels, K⁺ channels, taurine) and RVI (NKCC1, NHE + AE); compatible osmolytes |
| Other pumps (5.4) | PMCA and SERCA keep $\ce{Ca^2+}$ low; plant $\ce{H+}$-ATPase; gastric $\ce{H+}$/$\ce{K+}$-ATPase; V-ATPase acidifies organelles; ABC: MDR1, TAP |
| Epithelia (5.5, Definition 5.5.1, Example 5.5.1) | Polarized transporters + tight junctions; enterocyte: apical SGLT1, basolateral GLUT2 and pump; parietal cell: carbonic anhydrase, apical $\ce{H+}$/$\ce{K+}$-ATPase with $\ce{K+}$ and $\ce{Cl-}$ channels, basolateral $\ce{Cl-}$/$\ce{HCO3-}$ exchange; $38\,\mathrm{kJ\,mol^{-1}}$ per $\ce{H+}$ at pH 0.8 |
| Membrane potential (5.6, Definition 5.6.1, Formula 5.6.1, Examples 5.6.1–5.6.2) | Mainly a $\ce{K+}$ diffusion potential; $4\times10^6$ ions charge a cell to $-70\,\mathrm{mV}$; GHK voltage equation, $-66\,\mathrm{mV}$ for $P_{\mathrm{K}} : P_{\mathrm{Na}} : P_{\mathrm{Cl}} = 1 : 0.05 : 0.4$, pump adds about $5\,\mathrm{mV}$; action potential as a transient switch of relative permeability |
| Mechanosensation (5.7, Definition 5.7.1, Formula 5.7.1) | MscS and MscL as osmotic valves; Piezo1/2 (2010, Nobel 2021): trimeric propeller, dome flattening; touch, proprioception, baroreception, red cell volume, xerocytosis; $P_{\mathrm{o}}$ is a Boltzmann function of $\tau\Delta A$ |

## Questions

1. In the pump–leak model, why does the cell volume barely change during the first half hour after ouabain, although the $\ce{Na+}$ and $\ce{K+}$ gradients are already collapsing? What makes it swell later?

   **Answer** At first $\ce{Na+}$ enters and $\ce{K+}$ leaves at nearly equal rates, because the membrane potential, still near $E_{\mathrm{K}}$, makes the net current zero mainly by balancing $\ce{Na+}$ influx against $\ce{K+}$ efflux; the exchange is roughly one for one and does not change the number of osmotically active particles inside. As the $\ce{K+}$ gradient runs down, the membrane depolarizes; the negative potential no longer keeps $\ce{Cl-}$ out, so $\ce{Cl-}$ enters together with a cation, which adds particles to the cell, and water follows. The swelling therefore lags behind the ion exchange and follows the depolarization (figure in 5.2.2). It continues towards a Donnan state in which the impermeant anions inside always make the internal osmolarity exceed the external one.

2. A cell is suspended in isotonic ($290\,\mathrm{mOsm\,L^{-1}}$) solutions of (a) NaCl, (b) urea, (c) glycerol mixed half and half with NaCl. Predict the volume changes, given that urea and glycerol cross the membrane but not instantly, and that the cell does not regulate its volume.

   **Answer** (a) No change: NaCl is effectively impermeant (the pump excludes $\ce{Na+}$), so the solution is isotonic. (b) Urea enters down its concentration gradient; as it accumulates, the internal osmolarity rises and water follows, until urea is equal on both sides and the cell has taken up water as if it were in pure water: it swells without limit and lyses. Isosmotic urea is hypotonic. (c) Half the osmolarity ($145\,\mathrm{mOsm\,L^{-1}}$) is NaCl; after glycerol equilibrates, only the NaCl counts, and the cell swells to its Boyle–van 't Hoff volume at $\varPi_0/\varPi = 2$: $V/V_0 = b + 2(1-b)$, which for $b = 0.4$ is $1.6$; a red cell (lysis at about $1.7\,V_0$) would just survive, a spherocyte would not. Glycerol enters more slowly than urea, so the swelling is slower.

3. Using the GHK equation with the parameters of Example 5.6.2, calculate $V_{\mathrm{m}}$ when $[\ce{K+}]_{\mathrm{o}}$ is raised from $5$ to $10\,\mathrm{mM}$ (with $[\ce{Na+}]_{\mathrm{o}}$ lowered to $140\,\mathrm{mM}$). Compare with the change of $E_{\mathrm{K}}$, and explain why the heart is sensitive to serum $\ce{K+}$.

   **Answer** Numerator: $10 + 0.05 \times 140 + 0.4 \times 8 = 10 + 7 + 3.2 = 20.2$; denominator unchanged at $184.6$; $V_{\mathrm{m}} = 26.7 \times \ln(0.1094) = -59\,\mathrm{mV}$, a depolarization of $7\,\mathrm{mV}$. $E_{\mathrm{K}}$ changes from $-89$ to $-70\,\mathrm{mV}$, by $18.5\,\mathrm{mV}$ (a factor of 2 in $[\ce{K+}]_{\mathrm{o}}$ gives $26.7\ln 2$), so the membrane follows $E_{\mathrm{K}}$ only partly at these concentrations. In the heart, a depolarization of several millivolts inactivates part of the voltage-gated $\ce{Na+}$ channels and changes conduction and repolarization, causing arrhythmias; in addition, $\ce{K+}$ permeability itself depends on external $\ce{K+}$ in cardiac inward rectifiers, which makes the real effect larger.

4. A Piezo1 channel has $P_{\mathrm{o}} = 0.1$ at a membrane tension of $1.0\,\mathrm{mN\,m^{-1}}$ and $P_{\mathrm{o}} = 0.5$ at $2.0\,\mathrm{mN\,m^{-1}}$. Estimate $\Delta A$ and $\Delta G_0$ from the two-state model. What tension gives $P_{\mathrm{o}} = 0.9$?

   **Answer** From Formula 5.7.1, $\ln[P_{\mathrm{o}}/(1-P_{\mathrm{o}})] = (\tau - \tau_{1/2})\Delta A/k_{\mathrm{B}}T$. With $\tau_{1/2} = 2.0\,\mathrm{mN\,m^{-1}}$ and $\ln(0.1/0.9) = -2.20$ at $\tau = 1.0$: $\Delta A = 2.20\,k_{\mathrm{B}}T/(1.0\,\mathrm{mN\,m^{-1}}) = 2.20 \times 4.3\,\mathrm{nm^2} \approx 9.4\,\mathrm{nm^2}$. Then $\Delta G_0 = \tau_{1/2}\Delta A = 2.0 \times 9.4/4.3\,k_{\mathrm{B}}T \approx 4.4\,k_{\mathrm{B}}T$ ($11\,\mathrm{kJ\,mol^{-1}}$). By symmetry $P_{\mathrm{o}} = 0.9$ at $\tau = 3.0\,\mathrm{mN\,m^{-1}}$.

5. (Open) Hereditary xerocytosis (gain of function of Piezo1) and hereditary spherocytosis both reduce the deformability of red cells, but by opposite changes in the ratio of area to volume. Explain, and predict the result of an osmotic fragility test for each.

   **Answer** In spherocytosis the cell loses membrane area (vesiculation, [7.3.4](/7.3.4#ex-4.6.1)) at constant volume, so its area-to-volume ratio falls; it is nearly spherical, cannot deform, and lyses at a small swelling: osmotic fragility is increased (lysis at higher NaCl). In xerocytosis excess $\ce{Ca^2+}$ entry activates Gardos $\ce{K+}$ channels; the cell loses KCl and water, so its volume falls at constant area and its area-to-volume ratio rises; it becomes dehydrated, with concentrated, viscous hemoglobin that makes it stiff. Such cells must take up more water before they become spherical, so they resist hypotonic lysis: osmotic fragility is decreased (lysis at lower NaCl). Both illustrate that red cell function depends on the balance of membrane area, volume and internal viscosity, set by the skeleton and the pump–leak balance.
