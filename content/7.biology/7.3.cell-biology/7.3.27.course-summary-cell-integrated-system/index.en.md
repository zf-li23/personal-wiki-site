---
title: "Course Summary: The Cell as an Integrated System"
description: "The course assembled into one picture: the numbers and scales of the cell; the flow of membrane through its compartments as a set of steady-state balances; matter, energy and information; a comparison of every switch, oscillator and adaptive circuit of the course; how growth, division, polarity, adhesion, signaling, fate and death are coordinated; an index of the quantitative models, a timeline of the classic experiments and a table of diseases by compartment."
---

The preceding twenty-six chapters took the cell apart: its membranes and compartments, its cytoskeleton, its nucleus, its signaling, its cycle, and its life in a society of cells. This chapter puts it back together. It adds no new mechanism. Its purpose is to make explicit what the chapters showed one at a time: that a cell is a set of coupled steady states and decisions, and that the same few designs recur at every level. A compartment is a balance of inflow and outflow; a signaling pathway, a cell-cycle transition and a fate choice are built from the same switches and clocks; and the coordination of growth with division, of polarity with migration, and of proliferation with death is carried out by modules that read one another's outputs. The chapter collects the numbers of the course (27.1), follows the flow of membrane through the cell (27.2) and the three flows of matter, energy and information (27.3), compares all the switches, oscillators and adaptive circuits (27.4), describes how the parts coordinate (27.5), and ends with an index of the quantitative models, a timeline of the classic experiments and a table of diseases by compartment (27.6). The molecular foundations are in biochemistry ([7.1](/7.1)) and molecular biology ([7.2](/7.2)); the ideas collected here continue in genetics ([7.4](/7.4)), developmental biology ([7.5](/7.5)), biophysics ([7.6](/7.6)), systems biology ([7.9](/7.9)), animal physiology ([7.14](/7.14)) and immunology ([7.15](/7.15)).

## 27.1. Numbers and Scales

A cell biologist reasons with orders of magnitude. The table collects the numbers that recur in the course; the chapter in which each is derived or measured is given in the last column.

| Quantity | Typical value | Chapter |
|---|---|---|
| Volume: *E. coli*, budding yeast, HeLa cell, *Xenopus* oocyte | $1$, $40$, $3000\,\mathrm{fL}$, $1\,\mu\mathrm{L}$ | [7.3.1](/7.3.1) |
| Diffusion-limited radius for $\ce{O2}$ (Formula 1.3.1) | about $40\,\mu\mathrm{m}$ (*E. coli*), $300\,\mu\mathrm{m}$ (mammalian cell) | [7.3.1](/7.3.1) |
| One molecule per cell | $1\,\mathrm{nM}$ in *E. coli*; $1\,\mathrm{nM} \approx 1800$ molecules in a HeLa cell | [7.3.1](/7.3.1) |
| Proteins, ribosomes per cell | bacterium $3\times10^6$, $10^4$; human cell $10^9$–$10^{10}$, $10^6$–$10^7$ | [7.3.1](/7.3.1) |
| Lateral resolution of light (Formula 2.1.1) | about $230\,\mathrm{nm}$ (green, NA 1.4); SMLM $\sigma_{\mathrm{loc}} \approx s/\sqrt N$ | [7.3.2](/7.3.2) |
| Volume fractions of a hepatocyte | cytosol $54\,\%$, mitochondria $22\,\%$, ER $14\,\%$; plasma membrane $2\,\%$ of membrane area | [7.3.6](/7.3.6) |
| Ions in the cytosol | $\ce{K+}$ $140$, $\ce{Na+}$ $12$, $\ce{Cl-}$ $8\,\mathrm{mM}$; free $\ce{Ca^2+}$ about $10^{-4}\,\mathrm{mM}$; $V_{\mathrm{m}} \approx -70\,\mathrm{mV}$ | [7.3.5](/7.3.5) |
| Transport rates | channels $10^7$–$10^8$, carriers $1$–$10^3$, pumps about $100$ ions per second | [7.3.5](/7.3.5) |
| Charge for the resting potential (Example 5.6.1) | about $4\times10^6$ ions for a $1000\,\mu\mathrm{m^2}$ cell | [7.3.5](/7.3.5) |
| Vesicles, pits, caveolae | $50$–$150$, $100$–$200$, $50$–$80\,\mathrm{nm}$ | [7.3.8](/7.3.8), [7.3.10](/7.3.10) |
| Endocytosis | $1\,\%$ (fibroblast) to $3\,\%$ (macrophage) of the surface per minute | [7.3.10](/7.3.10) |
| Lumenal pH | Golgi $6.7 \to 6.0$, early endosome $6.0$–$6.5$, late endosome $5.0$–$6.0$, lysosome $4.5$–$5.0$ | [7.3.9](/7.3.9)–[7.3.11](/7.3.11) |
| Nuclear pores | $3000$–$4000$ per nucleus, $110$–$125\,\mathrm{MDa}$, up to $10^3$ macromolecules per second each | [7.3.16](/7.3.16) |
| Ribosome production (Example 17.8.1) | about $3500$ per minute in a HeLa cell | [7.3.17](/7.3.17) |
| Filaments: diameter, persistence length | actin $7\,\mathrm{nm}$, $17\,\mu\mathrm{m}$; microtubule $25\,\mathrm{nm}$, about $5\,\mathrm{mm}$; intermediate filament $10\,\mathrm{nm}$, about $1\,\mu\mathrm{m}$ | [7.3.13](/7.3.13)–[7.3.15](/7.3.15) |
| Motors | kinesin-1 $8.2\,\mathrm{nm}$ steps, $0.8\,\mu\mathrm{m\,s^{-1}}$, stall $6\,\mathrm{pN}$; myosin V $36\,\mathrm{nm}$ steps; duty ratio myosin II $0.04$, myosin V $0.7$ | [7.3.13](/7.3.13), [7.3.14](/7.3.14) |
| Signal range $\lambda = \sqrt{D/k}$ (Formula 18.2.1) | acetylcholine $0.2$, Dpp $20$, NO $60\,\mu\mathrm{m}$; $\ce{Ca^2+}$ nanodomain $0.1\,\mu\mathrm{m}$ | [7.3.18](/7.3.18) |
| Cells of the body | $3.7\times10^{13}$; $2\times10^{11}$ red cells made per day; at least $10^6$ cells die per second | [7.3.24](/7.3.24), [7.3.25](/7.3.25) |
| A tumor at detection | about $10^9$ cells, $2$–$8$ driver mutations | [7.3.26](/7.3.26) |

Three lessons run through these numbers. First, cells contain few copies of many molecules: a regulator at $1\,\mathrm{nM}$ is a handful of molecules in a bacterium, so compartments, scaffolds and condensates are as much quantitative devices that raise local concentrations as structural ones ([7.3.1](/7.3.1), [7.3.6](/7.3.6)). Second, the flows are large compared with the stocks: a fibroblast internalizes its surface in about two hours, a lysosome holds its pH only as long as V-type ATPases outpace a proton leak, and a HeLa cell must export several thousand ribosomal subunits per minute through its pores. Third, the energies and forces of cellular machines are a few to a few hundred $k_{\mathrm{B}}T$ and a few piconewtons, so thermal fluctuation is never negligible: cells rectify it (the **Brownian ratchet**, Definition 13.4.1) rather than overpower it.

![Scales of the cell, with the chapter of each value in parentheses. A: characteristic times on one logarithmic axis, from the capture of free Ca²⁺ by buffers (about 50 µs) through kinesin steps (10 ms), the turnover of actin in cells (half-life about 30 s), the formation of a coated vesicle (1 min), the Rab5 → Rab7 switch on an endosome (minutes), the rise of caspase-3 activity in an apoptotic cell (about 9 min) and transit through the Golgi (about 20 min), to mitosis (about 1 h), the NF-κB, Hes1 and p53 rhythms (about 100 min, 2 h and 5.5 h), the 24-h cell cycle and circadian clock, the takeover of an intestinal crypt by one stem-cell clone (about 42 days), the red-cell lifespan (120 days), the progression from adenoma to carcinoma (about 17 years) and the turnover of elastin (decades); the bands are the response times of signaling through channels, covalent modification and transcription. B: forces in piconewtons, from k_BT/δ for one actin subunit (1.6 pN) through talin unfolding (5 pN), the stall forces of kinesin-1 and of a polymerizing actin filament (6–7 pN) and the optimum of a catch bond (about 12 pN) to the electrophoretic pull of the mitochondrial membrane potential on a presequence (about 26 pN). C: energies in units of k_BT at 37 °C: pumping one proton into gastric juice (about 15), the zippering of one SNARE complex (about 65) and the bending energy of a spherical vesicle, 8πκ (about 500)](./plots/scales-time-force-energy.py)

## 27.2. Membrane Flow Through the Cell

### 27.2.1. The Map

Every nuclear-encoded protein starts on a cytosolic ribosome, and every membrane-enclosed compartment is reached by one of the three modes of **protein sorting** (Definition 6.3.1): gated transport through **nuclear pore complexes**, transmembrane transport by translocators into the ER, mitochondria, plastids and peroxisomes, and vesicular transport among the compartments of the **endomembrane system** (Definition 6.1.2). The figure assembles the routes of chapters 7.3.6–7.3.11 into one map, with the rates that the chapters give.

![Membrane and protein flow in an animal cell. Translocation from the cytosol (orange): import into and export from the nucleus through nuclear pores, posttranslational import into mitochondria and peroxisomes, cotranslational entry into the ER through the SRP and the Sec61 translocon, and the formation of autophagosomes. Secretory flow (yellow): ER → Golgi in COPII vesicles, through the Golgi stack in about 20 min (pH falling from 6.7 to 6.0), from the trans Golgi network to the plasma membrane by constitutive secretion, to secretory granules (pH 5.0–5.5) released by Ca²⁺-triggered exocytosis within milliseconds, and to endosomes with the mannose 6-phosphate receptors. Endocytic flow (pink): uptake of 1–3 % of the surface per minute, about 2500 clathrin-coated vesicles per minute in a fibroblast, into early endosomes (pH 6.0–6.5, Rab5, PI(3)P), which convert to late endosomes (pH 5.0–6.0, Rab7, ESCRT) by Rab conversion after about 10 min and fuse with lysosomes (pH 4.5–5.0, the platform of mTORC1); phagosomes, macropinosomes and autophagosomes also end in lysosomes. Recycling and retrieval (blue, dashed): COPI vesicles and the KDEL receptor return escaped ER proteins, retromer returns receptors to the TGN, and recycling endosomes return membrane to the surface (an LDL receptor makes a round trip about every 10 min)](./plots/membrane-flow.py)

Read as a whole, the map has a simple structure. Proteins make one decision in the cytosol, ER or not ER (6.3.2), and those that enter the ER then flow outward in bulk, by default to the plasma membrane, unless a signal sends them elsewhere or retrieves them. The inward flow from the surface mirrors the outward one, and both are dominated by return traffic: most of the membrane that leaves a compartment comes back. Lysosomes are the common sink for four streams (**endocytosis**, **phagocytosis**, macropinocytosis and **autophagy**) and at the same time the place where the cell reads its nutrient state through **mTORC1** ([7.3.11](/7.3.11), [7.3.18](/7.3.18)).

### 27.2.2. Compartments Are Steady States

The most general lesson of the membrane chapters is that a compartment is not a container but a steady state of opposing fluxes, $\mathrm{d}A/\mathrm{d}t = J_{\mathrm{in}} - J_{\mathrm{out}}$ (Eq. (8.4)). The same balance, an input against a first-order loss, appears at every level of the course, and in every case it fixes two things: the steady level, input divided by the removal rate constant, and the time to reach it, about the reciprocal of that rate constant (the response time of [7.3.18](/7.3.18)).

| Balance | Input | Loss | Steady state | Chapter |
|---|---|---|---|---|
| Ions and volume (**pump–leak model**, Definition 5.2.1) | $\ce{Na+}$/$\ce{K+}$ pump | leaks down electrochemical gradients | ion contents, $V_{\mathrm{m}}$, volume | [7.3.5](/7.3.5) |
| Organelle pH (Formula 11.1.1) | V-type ATPase | proton leak, counter-ions | lumenal pH set by pump/leak ratio | [7.3.11](/7.3.11) |
| Labeled cargo (Formula 3.4.1, Eq. (9.1)) | pulse into compartment 1 | exit at $k_i$ | order of peaks, residence times $1/k_i$ | [7.3.3](/7.3.3), [7.3.9](/7.3.9) |
| Membrane area (Eq. (8.4)) | delivery by vesicles | budding of vesicles | constant compartment size | [7.3.8](/7.3.8) |
| Surface receptors (Formula 10.5.1) | synthesis $V_{\mathrm{s}}$, recycling $k_{\mathrm{r}}$ | internalization $k_{\mathrm{e}}$, degradation $k_{\mathrm{h}}$ | $f_{\mathrm{s}} = 1/(1 + k_{\mathrm{e}}/(k_{\mathrm{r}} + k_{\mathrm{h}}))$ | [7.3.10](/7.3.10) |
| Autophagosomes (Formula 11.6.1) | formation $k_{\mathrm{f}}$ | fusion $k_{\mathrm{fus}}$ | $A^* = k_{\mathrm{f}}/k_{\mathrm{fus}}$: a level does not reveal the flux | [7.3.11](/7.3.11) |
| Organelle size (Proposition 6.2.1) | assembly from a cytoplasmic pool | disassembly | $S^* = (\rho - c^*)V$, size scales with cell volume | [7.3.6](/7.3.6) |
| Unfolded ER proteins (Eq. (7.1)) | secretory load | folding by chaperones, ERAD | homeostasis up to the induced capacity | [7.3.7](/7.3.7) |
| Nuclear cargo (Proposition 16.5.1) | importins, Ran-GTP gradient | export, leak | accumulation at most $G_{\mathrm{n}}/G_{\mathrm{c}}$ | [7.3.16](/7.3.16) |
| β-Catenin (Formula 19.3.1) | synthesis $\nu$ | destruction complex | $B^* = \nu/(k_{\mathrm{b}} + k_{\mathrm{dc}}D)$: slow on, fast off | [7.3.19](/7.3.19) |

Two consequences follow. A steady level can be changed either by the input or by the loss, and the cell uses both: the **limiting-pool model** sets organelle size through the input, while ligand-induced internalization of EGF receptors (Example 10.5.1) and Wnt inhibition of the destruction complex act on the loss. And because the response time is set by the loss, a system whose loss is slowed responds slowly: β-catenin rises over hours after Wnt but falls within an hour when Wnt is removed (Question 5).

**Example 27.2.1 (The Membrane Budget of a Fibroblast)** A cultured fibroblast with about $3000\,\mu\mathrm{m^2}$ of plasma membrane that internalizes $1\,\%$ of it per minute ([7.3.10](/7.3.10)) removes $30\,\mu\mathrm{m^2\,min^{-1}}$, which, at $\pi d^2 \approx 0.020\,\mu\mathrm{m^2}$ per vesicle of $80\,\mathrm{nm}$ membrane diameter, is about $1500$ vesicles per minute, roughly $25$ per second (the estimate of 8.5.2; Example 10.1.1 counts about $2500$ clathrin-coated vesicles per minute). By Eq. (8.4), a constant surface requires that recycling and exocytosis return the same $30\,\mu\mathrm{m^2\,min^{-1}}$. If the cell also doubles its surface in a $24\,\mathrm{h}$ cycle, the net addition is $3000/1440 \approx 2.1\,\mu\mathrm{m^2\,min^{-1}}$, about $7\,\%$ of the recycling flux: almost all the membrane traffic at the surface is exchange, and only a small excess of delivery over removal makes the cell grow. The same budget explains why blocking endocytosis enlarges the surface within minutes, and why blocking ER exit makes the Golgi shrink while its membrane continues to leave (8.5.2).

### 27.2.3. Identity Under Flow

If membrane flows continuously, how does a compartment keep its identity? The chapters gave four answers that work together.

| Mechanism | What it does | Examples | Chapter |
|---|---|---|---|
| Selection at budding | **coat proteins** concentrate cargo and exclude residents | COPII (Sar1), COPI (Arf1), clathrin with AP complexes | [7.3.8](/7.3.8) |
| Retrieval | receptors return escaped proteins | KDEL receptor (binds at Golgi pH, releases at ER pH), retromer | [7.3.8](/7.3.8), [7.3.10](/7.3.10) |
| Molecular address | the **phosphoinositide code** and **Rab proteins** mark each membrane | PI(4)P Golgi, PI(4,5)P₂ plasma membrane, PI(3)P and Rab5 early endosome, PI(3,5)P₂ and Rab7 late endosome | [7.3.8](/7.3.8), [7.3.10](/7.3.10) |
| Matching at fusion | tethers, SM proteins and **SNAREs** pair the right membranes | specificity as the product of coat, Rab, tether, SM and SNARE layers | [7.3.8](/7.3.8) |

When a compartment changes identity, it does so by a switch: **Rab conversion** (Definition 8.3.4) turns an early endosome into a late one abruptly, by the positive feedback of Rab5 on itself and the delayed inhibition of Rab5 by Rab7 (Eq. (8.3)); and **endosome maturation** (Definition 10.3.2), like the progression of Golgi cisternae in the **cisternal maturation model** (Definition 9.3.2), converts membrane in place instead of moving cargo between fixed stations. Identity is therefore a dynamic property maintained by the same molecular switches that the rest of this chapter compares (27.4).

## 27.3. Matter, Energy and Information

The plan of the course ([7.3.1](/7.3.1)) distinguished flows of matter, force and information, and the decisions built on them. Seen from the end, the flows meet at a small number of molecules.

### 27.3.1. Matter: Diffusion, Motors and Flow

Small molecules and proteins move by diffusion, which is fast over short distances and slow over long ones: the time to diffuse a distance $L$ grows as $L^2/2D$, the time to be carried by a motor as $L/v$ ([7.3.14](/7.3.14)). The crossover is at micrometers to tens of micrometers, which is why diffusion suffices inside a bacterium but not along an axon, why organelles are positioned by **kinesins**, **dyneins** and myosin V, and why the size of a cell supplied only by diffusion is limited (Formula 1.3.1). Diffusion in cells is also hindered: proteins in the plasma membrane move 10–100 times more slowly than in a free bilayer because of the cortical fences of the picket-fence model (Formula 4.5.1), and macromolecules cross the nuclear envelope only by the FG-repeat mesh (Proposition 16.4.1). Bulk flows complete the picture: membrane flow through the endomembrane system (27.2), cortical flow in the polarizing *C. elegans* zygote ([7.3.15](/7.3.15)) and cytoplasmic flows in large cells.

### 27.3.2. Energy: What the Cell Pays For

Every steady state of the previous section costs free energy. The chapters identified three currencies and their uses.

| Currency | Paid for | Chapter |
|---|---|---|
| ATP hydrolysis | ion pumps (**Na⁺/K⁺-ATPase**, SERCA, V-ATPase), myosins, kinesins and dyneins, chaperones (BiP, Hsp70 in mitochondrial import), unfolding and extraction (NSF, p97, Vps4), actin polymerization and treadmilling | [7.3.5](/7.3.5)–[7.3.14](/7.3.14) |
| GTP hydrolysis | timers that make switches one-way: Sar1, Arf1, **Rab proteins**, Ran, SRP, dynamin, tubulin (the GTP cap of **dynamic instability**), Rho family GTPases, heterotrimeric G proteins | [7.3.6](/7.3.6)–[7.3.8](/7.3.8), [7.3.14](/7.3.14), [7.3.16](/7.3.16), [7.3.19](/7.3.19) |
| Ion gradients and membrane potential | secondary active transport (SGLT1), mitochondrial protein import ($\Delta\psi$), thylakoid Tat transport ($\Delta\mathrm{pH}$), the bacterial flagellar motor, electrical signaling | [7.3.5](/7.3.5), [7.3.6](/7.3.6), [7.3.14](/7.3.14) |

The distinction between ATP and GTP is functional. ATP is spent mostly to do work, against a gradient or a load; GTP is spent mostly to measure time and to make a cycle irreversible. A GTPase switch is turned on by a GEF at a defined place and off by hydrolysis after a delay, so a Rab marks a membrane only where its GEF sits, Ran-GTP is high only in the nucleus because RCC1 is on chromatin, and a microtubule grows only while its GTP cap lasts. Polymers convert chemical potential directly into force: a filament pushing against a load stalls at $f_{\mathrm{s}} = (k_{\mathrm{B}}T/\delta)\ln(c/C_{\mathrm{c}})$ (Eq. (13.4)), a few piconewtons, the same order as the stall force of a motor (figure in 27.1). The **proton-motive force** and the chemiosmotic machinery that charge the ATP pool are treated in [7.1.23](/7.1.23).

### 27.3.3. Information: Signals in Space and Time

Information enters the cell as signals and leaves as decisions. Between them, the course found three layers.

- Speed: Responses that open channels take milliseconds, those that modify existing proteins seconds to minutes, those that require transcription hours (18.3.2). The response time of each layer is set by the removal rate of its output, $\ln 2/k$.
- Space: A secreted signal reaches a distance $\lambda = \sqrt{D/k}$ (Formula 18.2.1); inside the cell, $\ce{Ca^2+}$ acts in nanodomains of about $0.1\,\mu\mathrm{m}$ while IP₃ spreads over the cell, the Ran-GTP gradient marks the nucleus, phosphoinositides mark membranes, and scaffolds and condensates hold pathways together (18.5).
- Logic: Pathways converge on shared proteins that compute AND, OR and opposition (**signal integration**, Definition 18.6.1): mTORC1 is active only when amino acids (through Rag) and growth factors (through Rheb) are both present on the lysosome. Signals reach the nucleus by regulated shuttling, so that a nuclear transcription regulator reports the current activity of its receptor (Smad), oscillates (NF-κB), or reads the mechanics of the cell (**YAP**) ([7.3.16](/7.3.16), [7.3.19](/7.3.19)).

The three flows meet at a few hubs. mTORC1 on the lysosome reads matter (amino acids), energy (through **AMP-activated protein kinase**) and information (growth factors) and decides between growth and recycling ([7.3.11](/7.3.11), [7.3.18](/7.3.18)); the Na⁺/K⁺ pump consumes energy to maintain the gradients that carry matter and the potential that carries electrical information ([7.3.5](/7.3.5)); and the Rho family GTPases translate receptor signals into the forces of the cytoskeleton ([7.3.19](/7.3.19)).

## 27.4. Switches, Oscillators and Timers

### 27.4.1. A Comparison

The decisions of a cell are made by a small number of circuit designs, which the course met in very different molecular contexts. The table lists every switch, oscillator and adaptive circuit for which a chapter gave a model.

| Circuit | Molecules | Design | Behavior | Time scale | Model |
|---|---|---|---|---|---|
| Positive feedback module | Mos–MEK–MAPK in *Xenopus* oocytes; CaMKII | self-activation with cooperativity | **bistability**, **hysteresis**, all-or-none in single cells | hours | Formula 18.4.1 |
| Rab cut-out switch | Rab5, Rabex-5–Rabaptin-5, Mon1–Ccz1, Rab7, Rab5 GAP | positive feedback + delayed inhibition of the upstream module | abrupt, one-way handover of identity | minutes | Eq. (8.3) |
| PINK1–Parkin | PINK1, phospho-ubiquitin, Parkin | import as sensor + feed-forward amplification | switch-like marking of depolarized mitochondria | minutes to hours | Formula 11.7.1 |
| Unfolded protein response | IRE1, PERK, ATF6, BiP | negative feedback through induced chaperone | homeostasis up to a capacity, then death | minutes to hours | Eq. (7.1) |
| Cdc42 polarization | Cdc42, Bem1–Cdc24, GDI | positive feedback + mass conservation, $D_a \ll D_b$ | one polarity site, threshold, memory | minutes | Formula 15.4.1 |
| Rac–Rho antagonism | Rac, Rho and their GEFs and GAPs | mutual inhibition (toggle) | exclusive front and rear | minutes | Formula 19.1.1 |
| Local excitation, global inhibition | receptors, PI3K, PTEN | incoherent feed-forward in space | **adaptation** to uniform signals, gradient sensing | seconds | Formula 15.5.1 |
| Adaptive circuits | desensitization; bacterial chemotaxis | incoherent feed-forward loop; integral feedback | perfect adaptation, fold-change detection | seconds to minutes | Formula 18.4.2 |
| Ca²⁺ oscillations | IP₃ receptor, SERCA, ER store | fast positive feedback (CICR) + slow depletion | **calcium oscillation**, frequency coding | seconds to minutes | Formula 18.4.3 |
| β-Catenin turnover | destruction complex, Wnt | regulated loss | slow on, fast off | hours | Formula 19.3.1 |
| NF-κB oscillator | NF-κB, IκBα, IKK | delayed negative feedback | nuclear pulses, period about 100 min | hours | Formula 19.3.2 |
| **Cell-cycle oscillator** | cyclin B–Cdk1, Wee1, Cdc25, APC/C–Cdc20 | positive feedback switch + delayed negative feedback | relaxation **limit cycle**, hysteresis | about an hour (embryo; model 65 min) to a day | Eqs. (20.1), (20.2) |
| Once-per-cycle replication | ORC, Cdc6, Cdt1, MCM, Cdk | two mutually exclusive windows | each origin fires once | one cycle | Proposition 20.4.1 |
| **Restriction point** | cyclin D–Cdk4/6, Rb, E2F, cyclin E–Cdk2 | positive feedback through E2F | bistable commitment, hysteresis in serum | hours | Eq. (22.1) |
| **Spindle assembly checkpoint** | Mad2, MCC, APC/C–Cdc20, securin | catalytic amplification + disassembly | one kinetochore holds anaphase; delay of about 20 min | minutes | Eq. (21.2) |
| p53 pulses | ATM, p53, Mdm2, Wip1 | delayed negative feedback | digital pulses about 5.5 h apart, dose sets their number | hours to days | Eq. (22.2) |
| Caspase switch | caspase-8/9, caspase-3, XIAP | positive feedback + titration of an inhibitor | variable delay, then complete activation | hours, then minutes | Formula 25.4.1 |
| **Lateral inhibition** | Delta, Notch | intercellular negative feedback | salt-and-pepper pattern if $f'\lvert g'\rvert > 2$ | hours | Eqs. (24.1), (24.2) |
| **Cell memory** | MyoD and other master regulators | transcriptional self-activation | bistable, heritable state | divisions | Eq. (24.3) |
| Hes1 oscillator | Hes1 mRNA and protein | delayed negative self-repression | period about 2 h, **Hopf bifurcation** above a critical delay | hours | Eq. (24.4) |
| Fate toggle | GATA1, PU.1 | mutual inhibition + self-activation | two valleys of the **Waddington landscape** | days | Eq. (24.6) |
| Dynamic instability | GTP-tubulin cap | stochastic switching of a polymer end | catastrophes, rescues, exponential lengths | seconds to minutes | Formula 14.2.1 |

![Six circuits of the course, each simulated with the equations and parameters of its own chapter. A: positive feedback with cooperativity, Eq. (18.2) (K = 0.5, n = 4, f = 0.8): the steady activity has two stable branches (solid) separated by an unstable one (dashed); a rising stimulus switches the system on at the upper fold (arrow up), a falling one switches it off only at the lower fold (arrow down): bistability and hysteresis. B: the Rab5 → Rab7 cut-out switch, Eq. (8.3): Rab5 rises by positive feedback, Rab7 is activated with a delay and then switches Rab5 off abruptly. C: the caspase switch, Eq. (25.1): stronger stimuli u shorten the delay from hours to less than an hour, but every activation is equally steep, and a stimulus below the threshold (dotted) never activates. D: the cyclin B–Cdk1 oscillator, Eq. (20.1): cyclin accumulates slowly, Cdk1 switches on abruptly and is switched off by APC/C-dependent destruction of cyclin, with a period of about 65 min. E: Hes1 delayed negative feedback, Eq. (24.4) with a delay of 18.7 min: protein and mRNA oscillate with a period of about 2 h. F: an incoherent feed-forward loop, Eq. (18.3): each step of the stimulus gives a transient response that returns exactly to the same level, perfect adaptation](./plots/switch-gallery.py)

### 27.4.2. Common Designs

The table reduces to five designs, each with a characteristic behavior, which [7.3.18](/7.3.18) introduced in the abstract and the later chapters found in the cell.

1. Positive feedback with nonlinearity gives switches and memory. Cooperativity, multisite phosphorylation, zero-order kinetics or titration of an inhibitor provide the **ultrasensitivity** (Definition 18.4.1) without which a feedback loop cannot be bistable. Bistability makes a transition all-or-none and, through hysteresis, irreversible: once Cdk1 is on, or E2F, or caspase-3, a fall of the input does not switch it off. The cell cycle uses this to make its transitions one-way, so that events cannot run backwards (20.6.3); apoptosis uses it to make death complete.
2. Negative feedback with delay gives oscillations. A loop in which an output represses its own production oscillates if the delay is long enough compared with the lifetimes of its components and the repression steep enough (NF-κB, p53, Hes1, the circadian clock, the cell-cycle oscillator). Without delay, the same loop gives homeostasis, as in the UPR.
3. Opposing branches that differ in speed give adaptation. An incoherent feed-forward loop or an integral feedback returns the output to its set point for any constant input and reports only changes (Formula 18.4.2); the LEGI model applies the same idea in space, so that a cell senses the relative gradient of an attractant rather than its level (Formula 15.5.1).
4. Mutual inhibition gives exclusive states. Rac against Rho separates front from rear, GATA1 against PU.1 separates two blood lineages, Delta–Notch between neighbors separates a precursor from its neighbors, and the PAR proteins separate the anterior from the posterior cortex.
5. Switch plus timer. The most reliable transitions combine a fast positive loop that commits with a delayed negative loop that resets. Rab5 activates itself and then, through Rab7, switches itself off; Cdk1 activates itself and then, through APC/C, destroys its cyclin; the SAC holds anaphase until the last kinetochore attaches and then releases it within minutes. GTP hydrolysis is the molecular timer of the small switches, proteolysis that of the large ones.

These designs connect cell biology to the mathematics of dynamical systems: fold bifurcations and hysteresis, the **phase plane** of the Cdk1 switch (Eq. (20.2)), limit cycles and the Hopf bifurcation of delayed feedback ([2.4](/2.4)), and to the systematic treatment of network motifs in [7.9](/7.9). A recurring observation of the course is that population measurements can hide single-cell switches: a population of oocytes responds gradually to progesterone although each oocyte is all-or-none (Example 18.4.1), the average p53 response looks like a damped oscillation although each cell pulses with constant amplitude (7.3.22), and the variable delay of the caspase switch produces fractional killing in a genetically uniform population (7.3.25).

## 27.5. How the Parts Coordinate

A cell has to keep many processes in step: it must grow before it divides, duplicate each organelle before it splits, polarize before it moves, and stop dividing or die when the body requires. The table collects the coordination problems that the course solved and the modules that solve them; the figure draws the same modules as one network.

| Problem | Parts coupled | Mechanism | Model | Chapter |
|---|---|---|---|---|
| Grow before dividing | mTORC1, ribosomes, cyclins | **cell growth** (Definition 22.4.1) feeds the size control of division | sizer, **adder**, timer: $V_{\mathrm{d}} = aV_{\mathrm{b}} + b$ (Eq. (22.3)) | [7.3.22](/7.3.22) |
| Scale organelles with the cell | organelles, cytoplasm | assembly from a limiting pool; osmotic balance of the nucleus | Proposition 6.2.1, Proposition 16.7.1 | [7.3.6](/7.3.6), [7.3.16](/7.3.16) |
| Copy the genome exactly once | origins, Cdks | licensing at low Cdk, firing at high Cdk | Proposition 20.4.1 | [7.3.20](/7.3.20) |
| Separate chromosomes only when all are attached | kinetochores, APC/C | spindle assembly checkpoint | Eq. (21.2) | [7.3.21](/7.3.21) |
| Divide organelles between daughters | mitochondria, Golgi, ER, centrosomes | fusion–fission networks, fragmentation and partition, once-per-cycle duplication | Formula 12.3.1 | [7.3.12](/7.3.12), [7.3.21](/7.3.21) |
| Polarize and move | Cdc42, Rac, Rho, PAR proteins, actin, microtubules | positive feedback, mutual inhibition, the molecular clutch | Formulas 15.4.1, 15.5.1, 19.1.1 | [7.3.15](/7.3.15), [7.3.19](/7.3.19) |
| Read the mechanics of the tissue | **integrins**, talin, **focal adhesions**, YAP, LINC | force reinforces adhesion; stiffness controls YAP | catch bond, Eqs. (23.5), (23.6) | [7.3.16](/7.3.16), [7.3.23](/7.3.23) |
| Stop dividing when crowded | **cadherins**, Hippo, YAP | **contact inhibition** (Definition 22.5.1) | — | [7.3.19](/7.3.19), [7.3.22](/7.3.22) |
| Choose different fates in a sheet | Delta, Notch, Hes | lateral inhibition; asymmetric division | Eqs. (24.1), (24.2) | [7.3.21](/7.3.21), [7.3.24](/7.3.24) |
| Respond to damage | ATM/ATR, p53, p21, Bcl-2 family | arrest, **cellular senescence** or **apoptosis** according to damage | Eq. (22.2), Formula 25.4.1 | [7.3.22](/7.3.22), [7.3.25](/7.3.25) |
| Keep tissue size | stem cells, niche, death | **self-renewal**, transit amplification, **neutral drift** | Eq. (24.5) | [7.3.24](/7.3.24) |

![How one animal cell coordinates its decisions, in the activity-flow notation of SBGN (open arrowheads: activation; bar: inhibition; dashed: slower or indirect). Inputs on the left: amino acids and energy, growth factors acting through receptor tyrosine kinases, the matrix and its stiffness sensed by integrins, contact with neighbours through cadherins, Delta on neighbouring cells, and DNA damage. Integrating switches in the middle: mTORC1 on the lysosome, active only when amino acids and growth-factor signals through Ras–ERK and PI3K–PKB coincide (an AND gate); the Rho family GTPases; the Hippo kinases, which inhibit YAP/TAZ; Notch and its target Hes1; p53 activated by ATM and ATR; the Rb–E2F switch driven by cyclin D; and the Bcl-2 family and caspases. Outcomes on the right: growth, which feeds the size control of division; division through the restriction point and YAP; shape and migration; fate choice by lateral inhibition; arrest and senescence through p21; and apoptosis through Puma and Noxa](./plots/coordination-map.py)

### 27.5.1. Growth, Division and Size

A proliferating cell must double every component in each cycle, and the components are made at rates that depend on its size. The control is distributed. Growth is set by nutrients and growth factors through mTORC1 and ribosome biogenesis: a HeLa cell makes about $3500$ ribosomes per minute (Example 17.8.1), and its growth rate is proportional to the fraction of its proteome in ribosomes (7.3.22). Division is gated by the restriction point, a bistable switch whose input (cyclin D) is itself a product of mitogen signaling and growth (7.3.19). Size is kept in a narrow range because division depends on size: in an adder, a deviation in birth size is halved in each generation (Proposition 22.4.1). Organelles follow cell size without a separate controller, because they assemble from cytoplasmic pools that scale with volume (Proposition 6.2.1) and because the nucleus is held at a constant **nuclear-to-cytoplasmic ratio** by import and osmotic balance (Proposition 16.7.1). The diffusion limit of Formula 1.3.1 sets the outer bound on all of this. Growth and division can also be uncoupled, as in oocytes, neurons and cleavage-stage embryos, which shows that the coupling is a regulated property, not a physical necessity.

### 27.5.2. Duplicating and Inheriting the Parts

Chromosomes are duplicated by a once-per-cycle licensing system (Proposition 20.4.1) and separated by a mechanical apparatus with an error-correction loop and a checkpoint ([7.3.21](/7.3.21)). Centrosomes duplicate once per cycle under Plk4 (7.3.14). The other organelles cannot be made de novo, except peroxisomes, and are inherited by growth and division of pre-existing ones: mitochondria form a network whose connectivity is a balance of **mitochondrial fusion** and **mitochondrial fission** (Formula 12.3.1) and are partitioned in large numbers, so that random segregation gives nearly equal shares; the Golgi and ER fragment or partition at mitosis and reassemble in the daughters; the nuclear envelope breaks down and reassembles around the chromosomes (7.3.16). Where inheritance is random and copy numbers are small, cell-to-cell variation is the result: heteroplasmy drifts through the **mitochondrial bottleneck** (Formula 12.5.1), extrachromosomal DNA segregates binomially and lets tumors adapt quickly (Proposition 17.9.1), and the inactive X is chosen at random and inherited clonally (Proposition 17.1.1).

### 27.5.3. The Mechanical Loop: Cytoskeleton, Adhesion and Signaling

The cytoskeleton, adhesions and signaling form a closed loop. Receptors activate Rho family GTPases through their GEFs; Cdc42, Rac and Rho build filopodia, lamellipodia and contractile stress fibers (Definitions 13.3.7, 19.1.1); actomyosin pulls on integrins and cadherins; and the force feeds back on the adhesions themselves, which strengthen under load because talin unfolds at about $5\,\mathrm{pN}$ and recruits vinculin, and because many adhesion bonds are **catch bonds** (Definition 23.4.4). The same force is read by **mechanotransduction** (Definition 23.4.3): stiffness and spreading keep YAP in the nucleus, force on the nucleus through LINC complexes dilates nuclear pores, and Piezo channels open with membrane tension (Formula 5.7.1). The loop explains several observations that otherwise look unrelated: why cells on soft substrates or in crowded epithelia stop dividing (YAP inactivation and **contact inhibition**), why there is an optimal stiffness for migration (the molecular clutch, 15.5.3), why fibronectin fibrils assemble only under cell tension (7.3.23), and why mitogens and adhesion are both required for proliferation (anchorage dependence, 19.2.3).

Polarity is the spatial version of the same logic. A positive feedback with a limited, rapidly diffusing pool picks one site (Formula 15.4.1), mutual inhibition separates two domains (PAR proteins, Rac and Rho), and the polarized cytoskeleton then delivers membrane and determinants to one side. Migration, asymmetric division and epithelial organization are three uses of one polarization machinery ([7.3.15](/7.3.15), [7.3.21](/7.3.21), [7.3.23](/7.3.23)).

### 27.5.4. The Cell in Its Society, and Its Failure

In an animal, every decision of a cell is conditional on others. Survival requires signals from other cells, and without them apoptosis is the default (18.1, 7.3.25); division requires mitogens and anchorage; differentiation is induced, laterally inhibited or inherited from asymmetric divisions ([7.3.24](/7.3.24)); stem cells are maintained by their niche and compete neutrally for it (Eq. (24.5)). Cancer is the breakdown of this society, and the **hallmarks of cancer** (Definition 26.5.2) can be read as a list of the controls of this course that a tumor must defeat.

| Hallmark | Normal control | Chapter |
|---|---|---|
| Sustaining proliferative signaling | mitogens, RTK–Ras–ERK, PI3K–PKB–mTORC1 | [7.3.19](/7.3.19), [7.3.22](/7.3.22) |
| Evading growth suppressors | Rb–E2F switch, contact inhibition, Hippo–YAP | [7.3.19](/7.3.19), [7.3.22](/7.3.22) |
| Resisting cell death | Bcl-2 family, caspase switch, p53 | [7.3.25](/7.3.25) |
| Enabling replicative immortality | telomere shortening, **Hayflick limit** | [7.3.25](/7.3.25) |
| Inducing angiogenesis, activating invasion and metastasis | junctions, basal lamina, matrix metalloproteinases, **epithelial–mesenchymal transition** | [7.3.23](/7.3.23), [7.3.26](/7.3.26) |
| Reprogramming energy metabolism | mTORC1, HIF, Myc; the **Warburg effect** ([7.1.18](/7.1.18)) | [7.3.11](/7.3.11), [7.3.26](/7.3.26) |
| Genome instability (enabling) | DNA damage checkpoints, the SAC, once-per-cycle replication | [7.3.20](/7.3.20)–[7.3.22](/7.3.22) |
| Tumor-promoting inflammation (enabling) | the SASP of senescent cells | [7.3.25](/7.3.25) |
| Avoiding immune destruction | recognition by T cells, immune checkpoints | [7.3.26](/7.3.26), [7.15](/7.15) |

Because the controls are layered, one failure is not enough: the incidence of cancer rises with a high power of age (Formula 26.2.1), and tumors evolve by mutation and selection among their cells (Definition 26.2.2). In most cancers at least one component of each of three central pathways is altered (26.4.3): the mitogenic RTK–Ras–PI3K pathway and Rb and p53, the two hubs of the coordination network above.

## 27.6. Models, Experiments and Diseases

### 27.6.1. An Index of the Quantitative Models

Every chapter turned at least one mechanism into equations. The index lists them in the order of the course; each has a simulation or a data figure in its chapter.

| Chapter | Model | What it predicts or measures |
|---|---|---|
| [7.3.1](/7.3.1) | diffusion-limited radius, Formula 1.3.1 | the largest cell supplied by diffusion |
| [7.3.2](/7.3.2) | resolution, Formula 2.1.1; localization precision, Formula 2.4.1; FRAP, Eq. (2.5); MSD, Definition 2.6.2 | what can be seen; diffusion coefficients and mobile fractions in living cells |
| [7.3.3](/7.3.3) | pelleting time, Formula 3.3.1; pulse–chase compartments, Formula 3.4.1; SPR kinetics, Eq. (3.3) | fractionation conditions; pathway order and residence times; binding constants |
| [7.3.4](/7.3.4) | hop diffusion, Formula 4.5.1; Helfrich energy, Formula 4.7.1, Proposition 4.7.1 | slow diffusion in plasma membranes; $8\pi\kappa$ for any sphere, tether radius and force |
| [7.3.5](/7.3.5) | pump–leak model, Definition 5.2.1; Boyle–van 't Hoff, Formula 5.3.1; GHK, Formula 5.6.1; gating by tension, Formula 5.7.1 | ion contents, volume and its collapse without the pump; osmotic swelling; resting potential; mechanosensitive opening |
| [7.3.6](/7.3.6) | limiting pool, Proposition 6.2.1; translocation ratchet, Formula 6.5.1 | organelle size proportional to cell volume; import speed $2D/\delta$ |
| [7.3.7](/7.3.7) | ER folding homeostasis, Eq. (7.1) | adaptation by the UPR up to a capacity |
| [7.3.8](/7.3.8) | budding energy, Eqs. (8.1), (8.2); Rab cut-out switch, Eq. (8.3); membrane balance, Eq. (8.4) | vesicle size from coat curvature; abrupt Rab conversion; compartment size as a steady state |
| [7.3.9](/7.3.9) | Golgi exit times, Eq. (9.1); two-pool secretion, Eq. (9.2) | vesicular transport versus maturation from the lag; biphasic insulin release |
| [7.3.10](/7.3.10) | iterative geometric sorting, Formula 10.3.1; receptor traffic, Formula 10.5.1 | membrane recycled, content retained; surface fraction and down-regulation of receptors |
| [7.3.11](/7.3.11) | organelle pH, Formula 11.1.1; autophagic flux, Formula 11.6.1; PINK1–Parkin, Formula 11.7.1 | the need for counter-ions; flux from accumulation after block; switch-like mitophagy |
| [7.3.12](/7.3.12) | fusion–fission network, Formula 12.3.1; bottleneck, Formula 12.5.1 | percolation of the network at $\kappa_{\mathrm{c}} \approx 1.82$; heteroplasmy variance $h_0(1 - h_0)/N$ |
| [7.3.13](/7.3.13) | nucleation–elongation, Formula 13.2.1; treadmilling, Formula 13.2.2; polymerization ratchet, Formula 13.4.1; motor ensembles, Formula 13.5.1 | lag phase; treadmilling concentration; stall force of a filament; sliding by low-duty-ratio motors |
| [7.3.14](/7.3.14) | Dogterom–Leibler, Formula 14.2.1; kinesin two-step model, Formula 14.5.1; motor teams, Formula 14.5.2 | microtubule length distribution; force–velocity relation; run length of cargo |
| [7.3.15](/7.3.15) | worm-like chain, Formula 15.3.1; wave pinning, Formula 15.4.1; LEGI, Formula 15.5.1 | filament flexibility; a single polarity site; gradient sensing with adaptation |
| [7.3.16](/7.3.16) | passive equilibration, Proposition 16.4.1; Ran gradient, Proposition 16.5.1; nuclear size, Proposition 16.7.1 | soft size exclusion of pores; limit of accumulation; constant N/C ratio |
| [7.3.17](/7.3.17) | X-inactivation skewing, Proposition 17.1.1; ecDNA segregation, Proposition 17.9.1; ribosome budget, Example 17.8.1 | manifesting heterozygotes; rapid copy-number variation; demand on rRNA genes and pores |
| [7.3.18](/7.3.18) | signal range, Formula 18.2.1; positive feedback, Formula 18.4.1; adaptive circuits, Formula 18.4.2; Ca²⁺ oscillations, Formula 18.4.3 | reach of local signals; bistability and hysteresis; perfect adaptation; frequency coding |
| [7.3.19](/7.3.19) | Rac–Rho toggle, Formula 19.1.1; β-catenin turnover, Formula 19.3.1; NF-κB oscillator, Formula 19.3.2 | front–rear exclusion; kinetics of Wnt responses; nuclear pulses |
| [7.3.20](/7.3.20) | Cdk1 oscillator and hysteresis, Eqs. (20.1), (20.2); once-per-cycle replication, Proposition 20.4.1 | autonomous embryonic cycles; thresholds for entry and exit; no re-replication |
| [7.3.21](/7.3.21) | search and capture, Eq. (21.1), Proposition 21.2.1; spindle checkpoint, Eq. (21.2) | optimal catastrophe frequency; anaphase delay after the last attachment |
| [7.3.22](/7.3.22) | Rb–E2F switch, Eq. (22.1); p53 pulses, Eq. (22.2); size control, Eq. (22.3), Proposition 22.4.1 | restriction point with hysteresis; digital pulses; correction of size deviations |
| [7.3.23](/7.3.23) | Donnan swelling, Eq. (23.1); elastin, Eq. (23.2); cellular Potts model, Algorithm 23.3.1; slip and catch bonds, Eqs. (23.4)–(23.6); gap-junction coupling, Eqs. (23.7), (23.8); Lockhart growth, Eq. (23.9) | cartilage pressure; rubber elasticity; cell sorting; force-strengthened adhesion; spread of signals through coupled cells; plant cell expansion |
| [7.3.24](/7.3.24) | lateral inhibition, Eqs. (24.1), (24.2); cell memory, Eq. (24.3); Hes1, Eq. (24.4); neutral drift, Eq. (24.5); fate toggle, Eq. (24.6) | patterning; heritable states; period of the clock; clonal takeover of a crypt; Waddington valleys |
| [7.3.25](/7.3.25) | caspase switch, Formula 25.4.1; telomere lifespan, Eq. (25.2); senescent-cell accumulation, Eq. (25.3) | variable delay and fractional killing; Hayflick limit from the shortest telomere; accelerating accumulation with age |
| [7.3.26](/7.3.26) | Knudson, Eq. (26.1); Armitage–Doll, Formula 26.2.1; preexisting resistance, Eq. (26.3) | slopes of hereditary and sporadic incidence; incidence $\propto t^{k-1}$; the case for combination therapy |

### 27.6.2. Classic Experiments

Cell biology advanced by a method in three steps, see, isolate and perturb ([7.3.3](/7.3.3)), and its classic experiments illustrate each step. Electron microscopy and fractionation (Claude, de Duve, Palade) identified the organelles and their functions; de Duve's latent acid phosphatase revealed the **lysosome** before it was seen (7.3.11). Palade's **pulse–chase experiment** traced secretory proteins from the ER through the Golgi to granules (Definition 3.4.2, 9.6.1); Blobel and Dobberstein reconstituted translocation into microsomes and established the **signal hypothesis** (Definition 6.4.1); Schekman's **sec mutants** ordered the secretory pathway genetically, and Rothman's cell-free system found the fusion machinery (9.6). Frye and Edidin showed that membrane proteins diffuse (7.3.4); Brown and Goldstein dissected **receptor-mediated endocytosis** with the LDL receptor (7.3.10); Ohsumi found the *ATG* genes (7.3.11). Cell fusion (Rao and Johnson), *cdc* mutants (Hartwell, Nurse), cyclin (Hunt) and MPF assembled the cell-cycle control system (7.3.20); Mitchison and Kirschner discovered dynamic instability and Vale and colleagues kinesin (7.3.14). Hayflick found the finite lifespan of normal cells, Gurdon reprogrammed a nucleus by **somatic cell nuclear transfer** and Takahashi and Yamanaka by four transcription factors (7.3.24–7.3.25); Knudson's statistics and the discovery that *v-src* came from *c-src* founded the genetics of cancer (7.3.26). A more recent group of experiments measured dynamics in single cells, Rab conversion on one endosome, p53 and NF-κB pulses, the hysteresis of Cdk1 and of E2F, and turned the qualitative switches of the textbooks into measured ones.

![A timeline of the discoveries described in the course, in five lanes (methods, membranes and traffic, cytoskeleton, cell cycle, the cell in its society), with the chapter of each in parentheses; diamonds mark work recognized by a Nobel Prize. The axis is compressed tenfold before 1950. From Hooke's cells (1665), the cell theory (1838–1855) and the Golgi apparatus (1898) through the bilayer (1925), fractionation, the lysosome and electron microscopy (1950s–1974), the unit membrane, the fluid mosaic model, the signal hypothesis, sec mutants and the LDL receptor (1959–1985), sliding microtubules, dynamic instability and kinesin (1971–1985), cell fusion, cdc mutants and cyclin (1970–1989), the Hayflick limit, nuclear transfer, differential adhesion, the two-hit hypothesis and v-src (1961–1976), to the molecular dynamics of the 2000s (Cdk1 hysteresis, p53 pulses, Rb–E2F bistability, Rab conversion), Piezo channels (2010), iPS cells (2006), super-resolution microscopy (Nobel 2014) and immune checkpoint blockade (Nobel 2018)](./plots/discovery-timeline.py)

### 27.6.3. Diseases by Compartment

Because the course followed the cell compartment by compartment, its diseases can be arranged the same way. Most are rare monogenic disorders, and each is informative because it shows what a single part does for the whole.

| Compartment or system | Disease | Defect | Chapter |
|---|---|---|---|
| Plasma membrane and its skeleton | hereditary spherocytosis; xerocytosis | ankyrin, band 3, spectrin; gain of function of Piezo1 | [7.3.4](/7.3.4), [7.3.5](/7.3.5) |
| ER and its quality control | cystic fibrosis (ΔF508-CFTR); α1-antitrypsin deficiency (Z) | misfolded protein degraded by ERAD; polymerized protein retained | [7.3.7](/7.3.7) |
| Membrane anchors, peroxisomes | paroxysmal nocturnal hemoglobinuria; Zellweger syndrome, X-ALD | GPI anchor synthesis; peroxin genes, a peroxisomal ABC transporter | [7.3.6](/7.3.6) |
| Vesicle traffic | disorders of Sec23A, Sar1B, Rab27A | paralog-specific coat and Rab defects | [7.3.8](/7.3.8) |
| Endocytosis | familial hypercholesterolemia | five classes of LDL receptor mutations | [7.3.10](/7.3.10) |
| Lysosomes | I-cell disease; Tay–Sachs, Gaucher, Pompe and more than 70 **lysosomal storage diseases** | mannose 6-phosphate tag; single hydrolases | [7.3.11](/7.3.11) |
| Autophagy and mitophagy | Parkinson's disease (PINK1, Parkin); Crohn's disease (*ATG16L1*) | mitochondrial quality control; xenophagy and inflammation | [7.3.11](/7.3.11) |
| Mitochondria | CMT2A, dominant optic atrophy; mtDNA diseases | MFN2, OPA1; heteroplasmy above a threshold | [7.3.12](/7.3.12) |
| Cytoskeleton and cilia | epidermolysis bullosa simplex; hereditary spastic paraplegia; **ciliopathies** (primary ciliary dyskinesia, ADPKD, Bardet–Biedl) | keratin 5/14; spastin; motile and primary cilia | [7.3.14](/7.3.14), [7.3.15](/7.3.15) |
| Nuclear envelope | **laminopathies**, Hutchinson–Gilford progeria | *LMNA*, persistent farnesylation of progerin | [7.3.16](/7.3.16) |
| Chromosomes | **aneuploidy** and the maternal age effect | loss of cohesion in aging oocytes | [7.3.21](/7.3.21) |
| Junctions and matrix | pemphigus, arrhythmogenic cardiomyopathy; osteogenesis imperfecta, Ehlers–Danlos, Marfan, Alport syndromes; leukocyte adhesion deficiencies | desmosomes; collagens, fibrillin, basal lamina; integrins and selectin ligands | [7.3.23](/7.3.23) |
| Signaling | Gorlin syndrome, basal cell carcinoma; T-ALL; colorectal cancer | Patched (Hedgehog); Notch; APC (Wnt) | [7.3.19](/7.3.19) |
| Death and clearance | autoimmune lymphoproliferative syndrome; lupus-like disease | Fas pathway; defective efferocytosis | [7.3.25](/7.3.25) |
| The cell society | cancer | accumulated defects in the controls of 27.5.4 | [7.3.26](/7.3.26) |

The table also shows a pattern that recurs in medicine: tissues are affected where a component is used most or has the fewest backups. Keratin 5/14 defects blister the basal epidermis, which bears the largest shear; MFN2 and OPA1 defects damage long peripheral axons and the retinal ganglion cells of the optic nerve, which depend most on mitochondrial transport and fusion; storage diseases damage the neurons that cannot dilute their lysosomal load by dividing.

## Summary

- Numbers (27.1): cells contain few copies of many molecules, their flows are large compared with their stocks, and their forces (a few pN) and energies (a few to a few hundred $k_{\mathrm{B}}T$) are close to the thermal scale; times range from microseconds (Ca²⁺ buffering) to decades.
- Membrane flow (27.2): one decision in the cytosol, then bulk flow outward with signal-mediated diversion and retrieval, and an inward endocytic flow of 1–3 % of the surface per minute; every compartment is a steady state, $\mathrm{d}A/\mathrm{d}t = J_{\mathrm{in}} - J_{\mathrm{out}}$ (Eq. (8.4)), and the same input-against-loss balance governs ions (Definition 5.2.1), organelle pH (Formula 11.1.1), receptors (Formula 10.5.1), autophagy (Formula 11.6.1) and organelle size (Proposition 6.2.1); identity is kept by coats, retrieval, Rab and phosphoinositide addresses and SNARE matching, and changed by switches such as Rab conversion (Eq. (8.3)).
- Matter, energy, information (27.3): diffusion versus motors ($L^2/2D$ versus $L/v$); ATP pays for work, GTP for timing; signals act in milliseconds, minutes or hours, over $\lambda = \sqrt{D/k}$ (Formula 18.2.1), and are integrated at hubs such as mTORC1.
- Circuits (27.4): five designs explain all the switches and clocks of the course, positive feedback (bistability, memory: Formula 18.4.1, Eqs. (20.2), (22.1), Formula 25.4.1), delayed negative feedback (oscillations: Formula 19.3.2, Eqs. (20.1), (22.2), (24.4)), adaptation (Formulas 15.5.1, 18.4.2), mutual inhibition (Formula 19.1.1, Eqs. (24.1), (24.6)) and switch plus timer (Eqs. (8.3), (20.1), (21.2)).
- Coordination (27.5): growth, division and size are coupled through mTORC1, the restriction point and an adder (Eq. (22.3), Proposition 22.4.1); organelles scale and are inherited by pools, networks and partition; cytoskeleton, adhesion and signaling form a mechanical loop read by YAP; the cell's society decides survival, division and fate, and cancer is the defeat of its controls.
- Models, experiments, diseases (27.6): an index of the more than 70 equations and formulas of the course, the classic experiments from Hooke to single-cell dynamics, and a table of diseases arranged by compartment.

## Questions

1. Rab5 → Rab7 conversion (Eq. (8.3)), the exit from mitosis (Eq. (20.1)) and the spindle assembly checkpoint (Eq. (21.2)) each combine a positive and a negative loop. What does each loop contribute, and what would happen if either were removed?

   **Answer** The positive loop makes the transition all-or-none and fast once it starts: Rab5 recruits its own GEF, Cdk1 activates Cdc25 and inhibits Wee1, and the mitotic checkpoint complex catalyzes its own formation. The negative loop, acting with a delay, resets the system or hands it over to the next state: Rab7 recruits the Rab5 GAP, Cdk1 activates APC/C–Cdc20, which destroys cyclin B, and once the last kinetochore is attached the MCC is disassembled and APC/C destroys securin. Without the positive loop the transitions would be graded and slow, so that endosomes would carry mixtures of Rab5 and Rab7 (the dotted curves of the Rab figure in 7.3.8) and Cdk1 activity would rise gradually with cyclin, so that events could be triggered at intermediate levels and out of order. Without the delayed negative loop the switch would stay on: endosomes would keep Rab5, cells would arrest in mitosis (as extracts do with a cyclin that lacks its destruction signal, 20.2.5), or anaphase would never start. The combination gives a transition that is both decisive and self-terminating.

2. An unoccupied EGF receptor is internalized with $k_{\mathrm{e}} \approx 0.03\,\mathrm{min^{-1}}$, and about three quarters of the receptors are on the surface (Example 10.5.1). Use Formula 10.5.1 to estimate the surface fraction if ligand binding raises $k_{\mathrm{e}}$ tenfold while recycling and degradation are unchanged. Why is the real effect of EGF larger?

   **Answer** From $f_{\mathrm{s}} = 1/(1 + k_{\mathrm{e}}/(k_{\mathrm{r}} + k_{\mathrm{h}})) = 3/4$ we get $k_{\mathrm{e}}/(k_{\mathrm{r}} + k_{\mathrm{h}}) = 1/3$, so $k_{\mathrm{r}} + k_{\mathrm{h}} \approx 0.09\,\mathrm{min^{-1}}$. With $k_{\mathrm{e}} = 0.3\,\mathrm{min^{-1}}$ the ratio is $3.3$ and $f_{\mathrm{s}} = 1/4.3 \approx 0.23$: most receptors are now inside, within the time scale $1/(k_{\mathrm{e}} + k_{\mathrm{r}} + k_{\mathrm{h}}) \approx 3\,\mathrm{min}$. The real effect is larger because occupied receptors are also ubiquitylated by Cbl and sorted by ESCRT into intralumenal vesicles of multivesicular bodies, which lowers recycling and raises degradation: the total number of receptors falls over an hour, not only their distribution (**receptor down-regulation**, Definition 10.5.2). Signaling is shaped by traffic: the surface number sets sensitivity, and internalization both terminates and relocates signaling.

3. A cell that follows an adder is born $30\,\%$ larger than the average. How many generations does it take for its birth size to be within $5\,\%$ of the average, and how would a sizer and a timer behave?

   **Answer** By Proposition 22.4.1 a deviation is multiplied by $a/2$ per generation; for an adder $a = 1$, so the deviation goes $30 \to 15 \to 7.5 \to 3.75\,\%$: three generations. A sizer ($a = 0$) corrects the deviation in one generation, because it divides at a fixed size whatever its birth size. A timer ($a = 2$) does not correct it at all: with exponential growth for a fixed time the deviation is passed on unchanged, and with noise in the growth rate or the division time sizes perform a random walk and the distribution broadens without limit. This is why pure timers are not found in proliferating cells, and why most bacteria and budding yeast daughters, which behave as adders, keep narrow size distributions with a simple mechanism such as the accumulation of an activator to a fixed number.

4. Normal epithelial cells divide on a stiff matrix when sparse but stop when crowded, and stop on a soft matrix even when sparse. Trace the modules of 27.5 that produce this behavior, and explain which changes allow cancer cells to escape it.

   **Answer** On a stiff matrix, integrins cluster into focal adhesions that are reinforced by force (talin unfolding, catch bonds); Rho-driven actomyosin tension and spreading keep the Hippo kinases LATS1/2 inactive, so YAP/TAZ enter the nucleus and, with TEAD, activate proliferation genes; integrin signaling also cooperates with growth factor receptors in activating ERK and PI3K–PKB, which drive cyclin D and the Rb–E2F switch (anchorage dependence). On a soft matrix the adhesions do not mature, tension is low, and YAP is excluded from the nucleus. When cells become crowded, cadherin junctions and apical polarity complexes activate the **Hippo pathway**, so YAP is phosphorylated and kept in the cytoplasm: **contact inhibition**. Cancer cells escape at several points: mutations that activate Ras or PI3K make the mitogenic pathway independent of adhesion; loss of Rb (or of p16, or amplification of cyclin D) removes the restriction-point gate; loss of E-cadherin in the **epithelial–mesenchymal transition** removes contact signals; and amplification or activation of YAP/TAZ bypasses the Hippo pathway. The result is the anchorage-independent growth and loss of contact inhibition used to recognize transformed cells (Definition 26.5.1).

5. β-Catenin has a half-life of about $30\,\mathrm{min}$ (Formula 19.3.1). Suppose Wnt reduces the activity of the destruction complex so that the total degradation rate constant falls ninefold. Estimate the time for β-catenin to reach half of its new steady level, and the time for it to fall back by half when Wnt is removed. What general principle does this illustrate?

   **Answer** Before Wnt, $k = \ln 2/30 \approx 0.023\,\mathrm{min^{-1}}$. With Wnt, $k' = k/9 \approx 0.0026\,\mathrm{min^{-1}}$, and the steady level rises ninefold. The approach to the new level is governed by the new removal rate: $B(t) = B^*_{\mathrm{new}} - (B^*_{\mathrm{new}} - B^*_{\mathrm{old}})\mathrm{e}^{-k't}$, so the half-time of the rise is about $\ln 2/k' \approx 270\,\mathrm{min} \approx 4.5\,\mathrm{h}$ (a little less to reach half of the final level itself, because the start is not zero). When Wnt is removed, the destruction complex is fully active again and the excess decays with $k$, half in about $30\,\mathrm{min}$. The principle is that of 27.2.2 and 18.3.2: the response time of a steady state is set by its loss, so a signal that acts by slowing degradation switches on slowly and off quickly. The same reasoning explains why receptor numbers change slowly when degradation is slowed and why short-lived regulators (p53, Hes1, IκBα) are the components of fast oscillators.

6. Why can the same cell population respond to a death ligand with a death time that varies over hours from cell to cell, while in each cell the executioner caspases switch on within minutes? What does this imply for interpreting a dose–response curve measured on a population?

   **Answer** In the caspase switch (Formula 25.4.1) the stimulus drives initiator activity slowly until the positive feedback through caspase-3 overcomes the titration by XIAP; near the threshold the system lingers close to a saddle-node, so the delay depends steeply on the stimulus and on the levels of the proteins in each cell, which vary nongenetically. Once the threshold is passed, the feedback completes activation in a few minutes regardless of how long the delay was (figure in 27.4, panel C). In a population, the fraction of dead cells therefore rises gradually with dose and time even though every cell switches abruptly: the graded population curve reflects the distribution of thresholds and delays, not graded caspase activity in single cells. Cells whose stimulus falls below their threshold survive, which is one source of fractional killing by chemotherapy and of nongenetic drug tolerance (7.3.25, 7.3.26). The same caution applies to the Xenopus oocyte switch (Example 18.4.1) and to p53 pulses (7.3.22).
