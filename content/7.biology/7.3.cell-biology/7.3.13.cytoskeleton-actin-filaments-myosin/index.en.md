---
title: "The Cytoskeleton I: Actin Filaments and Myosin"
description: "The three filament systems and the logic of dynamic self-assembly; actin filaments: structure and polarity, nucleation, critical concentration, the two ends, ATP hydrolysis and treadmilling; drugs; actin-binding proteins (thymosin, profilin, formins, the Arp2/3 complex and its activators, capping, severing and cross-linking proteins); the cortex, lamellipodia, filopodia and stress fibers; how polymerization pushes (Listeria, the Brownian ratchet, buckling); the myosin superfamily, the cross-bridge cycle, muscle contraction in outline, non-muscle myosin II, myosin V, duty ratio and processivity."
---

A cell has to hold its shape, change it, move, divide, and place its organelles where they are needed, and it does all of this with three kinds of protein polymer that together form the cytoskeleton. The filaments are not girders: most of them are assembled and disassembled within seconds to minutes, from subunits that diffuse through the cytosol, and the cell decides where and when they grow by controlling a small number of nucleating, capping and severing proteins. Out of the same few principles (polar filaments, nucleotide hydrolysis, nucleation as a barrier, motors that walk on the filaments) the cell builds structures as different as the leading edge of a crawling cell, the microvilli of the gut, the contractile ring of cytokinesis and the sarcomere of muscle. This chapter introduces the three filament systems and then treats actin and its motor, myosin; microtubules and their motors and cilia follow in [7.3.14](/7.3.14), and intermediate filaments, the mechanics of the cytoskeleton, cell polarity and migration in [7.3.15](/7.3.15). The molecular basis of motor proteins was introduced with actin and myosin in muscle in [7.1.7](/7.1.7#sec-7.5); single-molecule mechanics and its statistical physics are treated in [7.6](/7.6), and the physiology of muscle in [7.14](/7.14). The signaling that controls the cytoskeleton is taken up again in [7.3.19](/7.3.19).

## 13.1. The Three Filament Systems

### 13.1.1. Actin Filaments, Microtubules and Intermediate Filaments

**Definition 13.1.1 (Cytoskeleton)** The **cytoskeleton** is the system of protein filaments in the cytoplasm of a eukaryotic cell, with their accessory proteins, that gives the cell its shape and mechanical strength, organizes its interior and produces movement. It has three main components: actin filaments (microfilaments), microtubules and intermediate filaments.

The three filaments differ in their subunits, their structure and therefore their behavior:

| | Actin filament | Microtubule | Intermediate filament |
|---|---|---|---|
| Subunit | actin, a globular $42\,\mathrm{kDa}$ ATPase | αβ-tubulin heterodimer, $2 \times 50\,\mathrm{kDa}$, a GTPase | elongated fibrous proteins (keratins, vimentin, neurofilament proteins, lamins) |
| Structure | two-stranded helix, about $7\,\mathrm{nm}$ across | hollow tube of 13 protofilaments, $25\,\mathrm{nm}$ | rope of staggered coiled coils, about $10\,\mathrm{nm}$ |
| Polarity | polar: plus (barbed) and minus (pointed) end | polar: plus and minus end | none |
| Nucleotide | ATP, hydrolyzed after assembly | GTP on β-tubulin, hydrolyzed after assembly | none |
| Motors | myosins | kinesins, dyneins | none |
| Typical structures | cortex, lamellipodia, filopodia, microvilli, stress fibers, contractile ring, sarcomere | radial array from the centrosome, mitotic spindle, axonemes of cilia, axonal tracks | cytoplasmic networks anchored at cell junctions, nuclear lamina |
| Main roles | shape of the cell surface, crawling, cytokinesis, contraction | positioning of organelles, long-range transport, chromosome segregation, ciliary beating | tensile strength |

![The cytoskeleton of a crawling fibroblast. A (schematic, top view): actin (red) forms the branched network of the lamellipodium at the leading edge (right), parallel bundles in filopodia, contractile stress fibers ending in focal adhesions (yellow) and a thin cortex under the whole plasma membrane; microtubules (blue) radiate from the centrosome, which lies between the nucleus and the leading edge, with their plus ends (dots) at the periphery; intermediate filaments (green) form a cage around the nucleus and extend towards the cell surface. B: the three filaments drawn at the same scale (100 nm segments): a two-stranded actin filament, a microtubule of αβ-tubulin dimers, and a ropelike intermediate filament](./plots/cytoskeleton-overview.py)

In a crawling fibroblast the three systems divide the work. Actin builds the protrusions at the front and the contractile bundles that pull the cell body forward; microtubules, growing from the centrosome placed in front of the nucleus, set the axis of the cell and carry membranes and messenger RNAs to the front; intermediate filaments resist stretching. In a polarized epithelial cell the same filaments build stable structures instead: actin cores of microvilli at the apical surface, a belt of actin and myosin at the adherens junctions, microtubules running from the apical to the basal surface with their minus ends at the top, and keratin filaments anchored at desmosomes and hemidesmosomes (cell junctions are treated in [7.3.23](/7.3.23)). At mitosis both kinds of cell take apart their interphase arrays within minutes and build a spindle and a contractile ring ([7.3.21](/7.3.21)).

### 13.1.2. Dynamic Self-Assembly

The filaments share a design. Each is a polymer of small subunits held together by many weak noncovalent bonds, and each subunit is a few nanometers in size and diffuses quickly, while the filaments it builds can span the cell. Three consequences follow.

1. Assembly is reversible and fast. No covalent bonds are made or broken, so a structure can be dismantled in one place and rebuilt elsewhere at little energetic cost, the way an ant trail moves when the food moves.
2. Multiple strands give thermal stability with dynamic ends. A single string of subunits would break wherever one bond failed. In a filament of several protofilaments a subunit in the middle is held by bonds to several neighbors, so the filament resists breakage, while a subunit at the end has fewer contacts and can be added or lost. Breaking a microtubule in two requires breaking bonds in all 13 protofilaments at once; removing a dimer from its end breaks bonds with at most three others.
3. Polarity and nucleotide hydrolysis make the filament an engine. Actin and tubulin subunits assemble head to tail, so that the two ends of a filament are structurally different, and both hydrolyze a bound nucleotide after they assemble. Hydrolysis drives the filaments out of equilibrium: it produces treadmilling and dynamic instability, and the free energy of polymerization can push a load. Intermediate filament subunits are symmetric and hydrolyze nothing: their filaments are nonpolar, strong ropes.

**Definition 13.1.2 (Motor Protein)** A **motor protein** is a protein that binds a polar track (a cytoskeletal filament or a nucleic acid) and converts the free energy of repeated cycles of nucleotide hydrolysis into directed movement along it. The cytoskeletal motors are the myosins (on actin, 13.5) and the kinesins and dyneins (on microtubules, [7.3.14](/7.3.14)).

Motors work in an environment dominated by viscosity. The Reynolds number $\operatorname{Re} = \rho v a/\eta$, the ratio of inertial to viscous forces, is about $10^{-5}$ for a $1\,\mu\mathrm{m}$ vesicle moving at $1\,\mu\mathrm{m\,s^{-1}}$ in water ($\rho = 10^3\,\mathrm{kg\,m^{-3}}$, $\eta = 10^{-3}\,\mathrm{Pa\,s}$), so that an object stops within a fraction of a nanometer once the force on it ceases. Nothing coasts in a cell: a motor that lets go of its track is immediately at the mercy of **Brownian motion**, and movement requires force at every instant. Conversely, thermal motion can itself be rectified into directed movement, as 13.4 shows.

### 13.1.3. Drugs That Act on the Cytoskeleton

Natural toxins that stabilize or destabilize filaments are among the most useful tools of cell biology, and some are drugs.

| Compound | Target | Effect | Source |
|---|---|---|---|
| Latrunculin | actin monomers (1 : 1) | depolymerizes (prevents assembly) | sponges |
| Cytochalasin B, D | actin plus ends | caps plus ends, depolymerizes | fungi |
| Phalloidin | sides of actin filaments | stabilizes; fluorescent phalloidin stains F-actin | *Amanita* mushrooms |
| Jasplakinolide | actin filaments | stabilizes, promotes nucleation | sponges |
| Taxol (paclitaxel) | β-tubulin in the lattice | stabilizes microtubules | Pacific yew |
| Colchicine, nocodazole | tubulin dimers | depolymerize (tubulin–drug complex poisons the ends) | autumn crocus; synthetic |
| Vinblastine, vincristine | tubulin dimers | depolymerize; suppress dynamics at low doses | Madagascar periwinkle |

(MBoC 7e, Table 16–1, extended.) That both stabilizers and destabilizers are toxic shows that the cell needs the exchange between subunits and filaments, not just the filaments. Microtubule drugs arrest cells in mitosis and are used against cancer ([7.3.14](/7.3.14#sec-14.4.3)).

## 13.2. Actin Filaments

### 13.2.1. Structure and Polarity

**Definition 13.2.1 (Actin Filament)** **Actin** is a $42\,\mathrm{kDa}$ protein of 375 residues that binds one ATP or ADP with $\mathrm{Mg^{2+}}$ in a deep cleft. Monomeric, globular actin is **G-actin**; its polymer, filamentous actin or **F-actin**, is the **actin filament**: a right-handed helix of subunits, all pointing the same way, which can be seen as two protofilaments winding around each other with a crossover every $36$–$37\,\mathrm{nm}$. Each subunit adds $2.75\,\mathrm{nm}$ to the length (about 370 subunits per micrometer).

Actin is one of the most abundant and most conserved eukaryotic proteins: actins from amoebae and humans are about $90\,\%$ identical, and actin accounts for $5$–$10\,\%$ of the protein of a typical non-muscle cell, up to $20\,\%$ in muscle. Vertebrates have three classes of isoforms: α-actins in muscle and β- and γ-actins in non-muscle cells. Its fold belongs to a family that includes hexokinase and Hsp70 and, in bacteria, MreB and ParM ([7.3.15](/7.3.15#sec-15.2)).

**Definition 13.2.2 (Plus End and Minus End)** Because its subunits point one way, a polar filament has two structurally different ends. The **plus end** is the end at which subunits add and dissociate faster; the **minus end** is the slower one. For actin they are also called the **barbed end** and the **pointed end**, after the arrowhead pattern seen in the electron microscope when filaments are decorated with myosin heads: the arrowheads point to the minus end.

The decoration experiment (Huxley, 1963; Ishikawa, Bischoff and Holtzer, 1969) became the standard way to determine filament orientation. Seeds decorated with myosin heads and then allowed to grow with pure actin elongate much faster at the barbed end, which is how the plus end was identified. The ATP-binding cleft of each subunit faces the minus end.

![Actin filament structure (schematic). Top: a filament from its minus (pointed) end on the left to its plus (barbed) end on the right, decorated with myosin heads (purple) that form arrowheads pointing to the minus end; the subunits are colored by their bound nucleotide: ATP (gold) near the growing plus end, ADP·Pi (pale gold) behind it and ADP (red) in the older part. Bottom: a daughter filament nucleated by the Arp2/3 complex (yellow) on the side of a mother filament at 70°](./plots/actin-filament-structure.py)

### 13.2.2. Nucleation and Elongation

Two actin monomers bind each other very weakly and a trimer only a little better; only from about three subunits on does an oligomer have enough contacts, along and across the strands, to grow faster than it falls apart.

**Definition 13.2.3 (Nucleation)** **Nucleation** is the formation of the smallest oligomer of a polymerizing protein (the nucleus; about three subunits for actin) that is more likely to grow than to dissociate. Because the intermediates are unstable, nucleation is slow and rate-limiting, and polymerization of pure subunits starts after a **lag phase**; adding preformed filament fragments (seeds) abolishes the lag.

Polymerization of purified actin is followed by the fluorescence of pyrene-labeled actin, which increases about twentyfold when the subunit enters a filament. The curve has three phases: lag (nucleation), growth (elongation of the nuclei), and a plateau at which assembly and disassembly balance.

**Formula 13.2.1 (Nucleation–Elongation Kinetics)** Let $c$ be the free monomer concentration, $F$ the concentration of filaments and $M$ the concentration of polymerized subunits. If nuclei of $n$ subunits form at rate $k_{\mathrm{n}}c^{n}$ and every filament end elongates at net rate $k_{\mathrm{on}}c - k_{\mathrm{off}}$,

$$
\frac{\mathrm{d}F}{\mathrm{d}t} = k_{\mathrm{n}}c^{n}, \qquad \frac{\mathrm{d}M}{\mathrm{d}t} = (k_{\mathrm{on}}c - k_{\mathrm{off}})F, \qquad c = c_{\mathrm{tot}} - M .
\tag{13.1}
$$
At early times $c \approx c_{\mathrm{tot}}$ and $M \approx \tfrac12 k_{\mathrm{on}}k_{\mathrm{n}}c_{\mathrm{tot}}^{n+1}t^2$, so the time to reach a given fraction of the final polymer scales as $t_{1/2} \propto c_{\mathrm{tot}}^{-n/2}$.

The scaling turns a kinetic curve into structural information: the slope of $\log t_{1/2}$ against $\log c_{\mathrm{tot}}$ estimates the size of the nucleus, which for actin is three to four subunits. In cells, spontaneous nucleation is negligible; the barrier is what lets the cell decide where filaments start, by placing nucleating proteins (13.3.2) at particular membranes.

![Nucleation–elongation kinetics of actin (Eq. (13.1), trimer nucleus, $k_{\mathrm{on}} = 12.9\,\mu\mathrm{M^{-1}\,s^{-1}}$ and $k_{\mathrm{off}} = 2.2\,\mathrm{s^{-1}}$ for both ends together). A: polymer as a fraction of its final value, as read from pyrene fluorescence, for 2, 4 and 8 µM actin without seeds: a lag that shortens steeply with concentration, then growth and a plateau that leaves the critical concentration free; with preformed seeds (dashed, 4 µM) the lag disappears. B: the half-time of polymerization against total actin on log–log axes has slope $-3/2$ for a trimer nucleus, $-n/2$ in general](./plots/actin-nucleation-kinetics.py)

### 13.2.3. The Critical Concentration

**Definition 13.2.4 (Critical Concentration)** For a filament end that adds subunits at rate $k_{\mathrm{on}}c$ and loses them at rate $k_{\mathrm{off}}$, the **critical concentration** $C_{\mathrm{c}} = k_{\mathrm{off}}/k_{\mathrm{on}}$ is the free subunit concentration at which the end neither grows nor shrinks. Above $C_{\mathrm{c}}$ it grows at net rate $J = k_{\mathrm{on}}(c - C_{\mathrm{c}})$; below, it shrinks. For a simple equilibrium polymer $C_{\mathrm{c}}$ equals the **dissociation constant** of a subunit from the end.

In a test tube, actin added above $C_{\mathrm{c}}$ polymerizes until the free monomer concentration has fallen to $C_{\mathrm{c}}$, about $0.1\,\mu\mathrm{M}$ for ATP-actin in physiological salt; everything above it ends up in filaments. Measured rate constants for Mg-ATP-actin (Pollard, 1986) are, at the plus end, $k_{\mathrm{on}} = 11.6\,\mu\mathrm{M^{-1}\,s^{-1}}$ and $k_{\mathrm{off}} = 1.4\,\mathrm{s^{-1}}$, and at the minus end $k_{\mathrm{on}} = 1.3\,\mu\mathrm{M^{-1}\,s^{-1}}$ and $k_{\mathrm{off}} = 0.8\,\mathrm{s^{-1}}$. The plus-end association constant is close to the diffusion limit for a protein of this size. At $10\,\mu\mathrm{M}$ ATP-actin a plus end grows by about $115$ subunits, or $0.3\,\mu\mathrm{m}$, per second.

**Proposition 13.2.1 (Equal Critical Concentrations Without Hydrolysis)** If the subunits at both ends are in the same nucleotide state, the critical concentrations of the two ends are equal, even though their rate constants differ.

**Proof** Adding a subunit to either end turns a filament of $n$ subunits into one of $n + 1$ subunits with the same bonds; the initial and final states, and hence the free energy change $\Delta G^\circ = -RT\ln(1/C_{\mathrm{c}})$, are the same at both ends. Since $C_{\mathrm{c}} = k_{\mathrm{off}}/k_{\mathrm{on}}$ is fixed by $\Delta G^\circ$, the ratio is the same at both ends: if the plus end grows ten times faster at a given $c$, it also shrinks ten times faster below $C_{\mathrm{c}}$. $\square$

The free energy of polymerization can do work. For $c > C_{\mathrm{c}}$, adding a subunit releases $\Delta G = -k_{\mathrm{B}}T\ln(c/C_{\mathrm{c}})$; a filament pointing its plus end at a membrane can therefore push it (13.4), provided the force does not exceed $(k_{\mathrm{B}}T/\delta)\ln(c/C_{\mathrm{c}})$, where $\delta$ is the length added per subunit.

### 13.2.4. ATP Hydrolysis and Treadmilling

Free actin hydrolyzes its ATP very slowly; in the filament the rate rises to about $0.3\,\mathrm{s^{-1}}$, and the phosphate is released much more slowly still (half-time several minutes). A filament therefore has an age structure: ATP-actin at a growing end, ADP·Pi-actin behind it, and ADP-actin in the old parts. ADP-actin binds its neighbors less tightly ($C_{\mathrm{c}}$ for ADP-actin is about $2\,\mu\mathrm{M}$), so old filament is less stable than new. Hydrolysis breaks the symmetry of Proposition 13.2.1, because the subunit that adds (ATP-actin) is not the subunit that leaves (often ADP-actin): the two ends can now have different critical concentrations, and the filament is no longer at equilibrium but in a steady state paid for with ATP.

**Definition 13.2.5 (Treadmilling)** **Treadmilling** is the steady state of a polar filament in which subunits add at the plus end and dissociate at the minus end at the same rate, so that the filament keeps its length while its subunits flow through it from the plus to the minus end. It occurs at free subunit concentrations between the critical concentrations of the two ends, $C_{\mathrm{c}}^{+} < c < C_{\mathrm{c}}^{-}$, which differ because of nucleotide hydrolysis.

**Formula 13.2.2 (Treadmilling Concentration and Flux)** With the plus end in the ATP state (rates $k_{\mathrm{on}}^{+}$, $k_{\mathrm{off}}^{+}$) and the minus end in the ADP state (rates $k_{\mathrm{on}}^{-}$, $k_{\mathrm{off}}^{-}$), the length of a filament is constant when $J^{+} + J^{-} = 0$, that is at

$$
c_{\mathrm{tm}} = \frac{k_{\mathrm{off}}^{+} + k_{\mathrm{off}}^{-}}{k_{\mathrm{on}}^{+} + k_{\mathrm{on}}^{-}}, \qquad
J_{\mathrm{tm}} = k_{\mathrm{on}}^{+}c_{\mathrm{tm}} - k_{\mathrm{off}}^{+} = k_{\mathrm{off}}^{-} - k_{\mathrm{on}}^{-}c_{\mathrm{tm}} .
\tag{13.2}
$$

With the measured constants ($k_{\mathrm{off}}^{-} = 0.27\,\mathrm{s^{-1}}$ for ADP-actin at the pointed end) this gives $c_{\mathrm{tm}} \approx 0.13\,\mu\mathrm{M}$ and a flux of only about $0.1$ subunit per second: a subunit spends about half an hour in a $1\,\mu\mathrm{m}$ filament of pure actin. In a non-muscle cell actin turns over in filaments with a half-life of about $30\,\mathrm{s}$, a hundred times faster, because accessory proteins accelerate both ends: profilin and formins feed the plus ends, cofilin dismantles the old ADP-actin, and capping proteins confine growth to a few ends. Treadmilling of the whole network, assembly at the front and disassembly behind it, is how lamellipodia advance (13.4.2); it can be seen directly by fluorescent speckle microscopy, in which sparse labeling makes individual subunits visible as speckles that stay put while the network flows past them.

![Critical concentrations and treadmilling (rate constants of Pollard, 1986; the pointed end carries ADP-actin). A: net elongation rate of the plus end, the minus end and the whole filament against free ATP-actin; between the two critical concentrations (shaded) the plus end grows while the minus end shrinks, and at $c_{\mathrm{tm}} \approx 0.13\,\mu\mathrm{M}$ the filament has constant mean length (Formula 13.2.2). B: a stochastic simulation of one filament at $c_{\mathrm{tm}}$ for an hour: both ends advance together by about 1 µm while the length fluctuates; marked subunits (black lines) stay where they joined until the minus end reaches them](./plots/actin-treadmilling.py)

## 13.3. Actin-Binding Proteins

A cell contains $50$–$200\,\mu\mathrm{M}$ unpolymerized actin, hundreds of times the critical concentration, yet only about half of its actin is in filaments, and new filaments appear only at particular places. More than a hundred actin-binding proteins make this possible. They fall into a few classes, each with a definite effect on the kinetics of 13.2.

![The main classes of actin-binding proteins (schematic; minus ends left, plus ends right; subunits colored by nucleotide as in 13.2). Top row: thymosin β4 sequesters ATP-actin; profilin binds monomers and delivers them to plus ends; a formin dimer rides on the plus end and feeds it with profilin–actin bound to its FH1 arms; the Arp2/3 complex, activated at the membrane by a nucleation-promoting factor (WASP or WAVE), nucleates a branch at 70°. Middle row: capping protein blocks the plus end; tropomyosin coats the filament and tropomodulin caps its minus end; cofilin binds old ADP-actin and severs it; gelsolin severs in response to Ca²⁺ and caps the new plus end. Bottom row: fimbrin, villin and fascin make tight parallel bundles; α-actinin makes loose antiparallel bundles with room for myosin II; filamin joins filaments at wide angles into a gel; ERM proteins and spectrin link filaments to the plasma membrane](./plots/actin-binding-proteins.py)

### 13.3.1. Monomer-Binding Proteins

**Definition 13.3.1 (Thymosin β4 and Profilin)** **Thymosin β4** is a small ($5\,\mathrm{kDa}$) protein that binds ATP-actin monomers 1 : 1 and prevents them from adding to either end of a filament: a buffer of unpolymerizable actin. **Profilin** is a $15\,\mathrm{kDa}$ protein that binds the face of an actin monomer that would contact the minus end, so that profilin–actin can add to plus ends but not to minus ends; it also catalyzes the exchange of ADP for ATP on the monomer, and binds polyproline sequences in formins and nucleation-promoting factors.

The two compete for the same monomers. In cells such as neutrophils and platelets, thymosin holds several hundred micromolar actin in reserve. When plus ends become available, profilin–actin adds to them, the free monomer concentration falls, and actin dissociates from thymosin to replace it: the reserve is released exactly where filaments grow. Profilin thus restricts growth to plus ends, recharges ADP-actin released by disassembly with ATP, and channels monomers to nucleators.

### 13.3.2. Nucleators: Formins and the Arp2/3 Complex

**Definition 13.3.2 (Formin)** A **formin** is a dimeric protein whose FH2 domains form a ring around the plus end of an actin filament and stay bound while it grows (processive capping), nucleating unbranched filaments; its FH1 domains, rich in proline, bind profilin–actin and deliver it to the end, so that formin-bound plus ends can elongate several times faster than free ones. Diaphanous-related formins are autoinhibited and are opened by Rho-GTP.

Formins build the long, straight filaments of filopodia, stress fibers, the actin cables of yeast and the contractile ring.

**Definition 13.3.3 (Arp2/3 Complex)** The **Arp2/3 complex** is a complex of seven proteins, two of them actin-related proteins (Arp2 and Arp3), that binds the side of an existing actin filament and, when activated, nucleates a daughter filament at an angle of about $70°$; it remains at the branch point, capping the minus end of the daughter. Its activators are **nucleation-promoting factors**: proteins whose C-terminal WCA region binds an actin monomer (W, WH2 domain) and the Arp2/3 complex (C and A, connector and acidic segments) and brings the two together.

The activators place nucleation under signaling control. *WASP* (Wiskott–Aldrich syndrome protein, in blood cells) and the ubiquitous N-WASP are autoinhibited and opened by **small G proteins** of the Rho family (Cdc42-GTP) together with PI(4,5)P₂ at the membrane; mutations in WASP cause the Wiskott–Aldrich syndrome, an immunodeficiency with small platelets, in which blood cells cannot form proper protrusions or immune synapses. WAVE, in a pentameric regulatory complex, is activated by Rac-GTP and builds lamellipodia; WASH acts on endosomes. Each step is a coincidence detector: an activator needs a GTPase and a lipid at the same membrane, and the Arp2/3 complex needs an activator, a monomer and a mother filament at the same place. Branched networks arise wherever these coincide, at the leading edge, around endocytic pits, at phagocytic cups ([7.3.10](/7.3.10)) and on endosomes.

| Nucleator | Product | Activated by | Structures |
|---|---|---|---|
| Arp2/3 complex + WASP, N-WASP | branched network | Cdc42-GTP, PI(4,5)P₂ | endocytic sites, podosomes, phagocytic cups |
| Arp2/3 complex + WAVE complex | branched network | Rac-GTP | lamellipodia |
| Formins (mDia and others) | long unbranched filaments | Rho-GTP (and Cdc42, Rac for some) | filopodia, stress fibers, contractile ring, yeast cables |
| Tandem-WH2 nucleators (Spire, cordon-bleu) | unbranched filaments | various | vesicle transport in oocytes, neurons |

### 13.3.3. Capping, Severing and Depolymerizing Proteins

**Definition 13.3.4 (Capping Protein)** **Capping protein** (CapZ in muscle) is a heterodimer that binds the plus end of an actin filament with subnanomolar affinity and blocks both addition and loss of subunits there. Tropomodulin caps the minus ends of tropomyosin-coated filaments.

Capping looks like a brake but works as a focusing device. A cell has thousands of plus ends; if all grew, the monomer pool would be spread thin. Capping all but the newest ends keeps the free monomer concentration high and directs polymerization to the few ends just nucleated at the membrane, where pushing is needed. Because only ends matter, one molecule per filament (one per several hundred subunits) suffices.

**Definition 13.3.5 (Cofilin)** **Cofilin** (actin-depolymerizing factor, ADF) is a small protein that binds cooperatively along ADP-actin filaments, twists them more tightly (the crossover shortens from $37$ to $27\,\mathrm{nm}$) and severs them at boundaries between bare and cofilin-decorated segments, creating new ends from which ADP-actin dissociates.

Because cofilin prefers ADP-actin, it dismantles old filaments and spares new ones: the nucleotide in the filament acts as a timer that marks subunits for removal. Cofilin is inactivated by phosphorylation on Ser3 by LIM kinase (downstream of Rho and ROCK, [7.3.15](/7.3.15)) and reactivated by the phosphatase slingshot. *Gelsolin* severs filaments when cytosolic $\ce{Ca^2+}$ rises into the micromolar range and then caps the new plus end; PI(4,5)P₂ removes it. Severing has two opposite effects, depending on the monomer concentration and the presence of capping proteins: it accelerates disassembly by creating ends, or it accelerates assembly by creating new plus ends to grow on.

### 13.3.4. Cross-Linking Proteins and the Architecture of Actin Arrays

**Definition 13.3.6 (Cell Cortex)** The **cell cortex** is the layer of actin filaments, myosin II and associated proteins, typically a few hundred nanometers thick, under the plasma membrane of an animal cell; tension in this layer sets the shape of the cell surface.

Cross-linkers have two actin-binding sites, on one chain or on a dimer, and the spacing and angle between the sites decide what is built:

| Cross-linker | Geometry | Spacing | Structures |
|---|---|---|---|
| Fimbrin (plastin), villin, espin | tight parallel bundle | about $14\,\mathrm{nm}$ (excludes myosin II) | microvilli, stereocilia |
| Fascin | tight parallel bundle | about $10\,\mathrm{nm}$ | filopodia |
| α-Actinin | loose bundle, often antiparallel | about $35$–$40\,\mathrm{nm}$ (admits myosin II) | stress fibers, Z discs, contractile ring |
| Filamin | V-shaped dimer joining filaments at wide angles | — | three-dimensional gel of the cortex and lamella |
| Spectrin | long flexible tetramer | — | membrane skeleton of erythrocytes and neurons ([7.3.4](/7.3.4)) |
| Dystrophin | links actin to the membrane glycoprotein complex | — | muscle cortex; absent in Duchenne muscular dystrophy |

Because fimbrin packs filaments too closely for α-actinin, and α-actinin too loosely for fimbrin, the two exclude each other and a bundle becomes either non-contractile or contractile. Membrane linkers, notably the ERM proteins (ezrin, radixin, moesin), bind PI(4,5)P₂ and the tails of membrane proteins and attach the cortex to the membrane when activated by phosphorylation; moesin stiffens the cortex as cells round up in mitosis.

Three protrusive and contractile structures recur in crawling cells:

**Definition 13.3.7 (Lamellipodium, Filopodium and Stress Fiber)** A **lamellipodium** is a thin (about $0.2\,\mu\mathrm{m}$), sheet-like protrusion at the leading edge of a crawling cell, filled with a branched network of actin filaments nucleated by the Arp2/3 complex, with their plus ends at the membrane. A **filopodium** is a finger-like protrusion, $0.1$–$0.3\,\mu\mathrm{m}$ wide and up to tens of micrometers long, with a core of 10–30 parallel actin filaments bundled by fascin and elongated at the tip by formins and Ena/VASP proteins. A **stress fiber** is a contractile bundle of antiparallel actin filaments, α-actinin and myosin II, often ending in focal adhesions, with a periodic, sarcomere-like arrangement.

Filopodia are sensors as much as protrusions: the growth cones of axons extend them to explore their surroundings, and their receptors detect guidance cues. Microvilli on the apical surface of intestinal epithelial cells are stable relatives of filopodia, each a bundle of about 20 filaments cross-linked by villin and fimbrin, plus ends at the tip, and anchored in a terminal web; their 20-fold increase of the membrane area serves absorption. The stereocilia of hair cells in the inner ear, hundreds of filaments in a tight bundle, last a lifetime and turn over only at their tips.

## 13.4. Force from Polymerization

### 13.4.1. Listeria and the Brownian Ratchet

The bacterium *Listeria monocytogenes*, a food-borne pathogen, escapes from the phagosome into the cytosol of the cells it infects and then moves through the cytoplasm at up to $15\,\mu\mathrm{m\,min^{-1}}$, propelled by a comet tail of actin filaments that forms behind it and spreads it to neighboring cells. Its surface protein ActA is a nucleation-promoting factor: it activates the host Arp2/3 complex at the rear of the bacterium. No motor protein is involved. Listeria motility was reconstituted from pure proteins (Loisel and colleagues, 1999): ATP-actin, the Arp2/3 complex, capping protein and cofilin are necessary and sufficient, with profilin, α-actinin and VASP increasing the speed. Polymerization itself must therefore generate the force.

**Definition 13.4.1 (Brownian Ratchet)** A **Brownian ratchet** is a mechanism that produces directed motion by rectifying thermal fluctuations: random motion in one direction is captured by an irreversible step (here, the addition of a subunit into a gap opened by a fluctuation), and motion back is blocked. The energy comes from the irreversible step, not from the fluctuations themselves.

The same principle drives protein translocation into mitochondria (Formula 6.5.1, with chaperone binding in place of subunit addition). For a filament pushing a membrane, the load must wait for a fluctuation that opens a gap of at least $\delta$ before a subunit can enter.

**Formula 13.4.1 (Polymerization Ratchet)** If the membrane (or bacterium) fluctuates fast compared with subunit addition, a filament tip pushing against a load $f$ advances at

$$
v = \delta\left(k_{\mathrm{on}}c\,\mathrm{e}^{-f\delta/k_{\mathrm{B}}T} - k_{\mathrm{off}}\right),
\tag{13.3}
$$
where $\mathrm{e}^{-f\delta/k_{\mathrm{B}}T}$ is the probability that the gap is open (Boltzmann factor of the work $f\delta$), $\delta = 2.7\,\mathrm{nm}$ for actin, and $k_{\mathrm{on}}$, $k_{\mathrm{off}}$ are the plus-end rate constants (Peskin, Odell and Oster, 1993). The velocity falls to zero at the *stall force*

$$
f_{\mathrm{s}} = \frac{k_{\mathrm{B}}T}{\delta}\ln\frac{c}{C_{\mathrm{c}}} ,
\tag{13.4}
$$
which is the free energy per subunit, $k_{\mathrm{B}}T\ln(c/C_{\mathrm{c}})$, divided by the distance it moves the load.

With $k_{\mathrm{B}}T = 4.1\,\mathrm{pN\,nm}$, $k_{\mathrm{B}}T/\delta \approx 1.5\,\mathrm{pN}$, and at $c = 10\,\mu\mathrm{M}$ ($c/C_{\mathrm{c}} \approx 80$) a single filament can in principle push with up to about $7\,\mathrm{pN}$. Measured stall forces of small bundles of growing filaments are of this order or lower, a few piconewtons per filament. A lamellipodium has a few hundred filaments per micrometer of edge, enough to push against membrane tension and the viscous resistance of the surroundings; how the work is shared among filaments, many of them lagging behind the membrane, is the subject of more detailed models ([7.6](/7.6)).

### 13.4.2. The Lamellipodium: Dendritic Nucleation and Treadmilling of a Network

The leading edge of a crawling cell such as a fish keratocyte or a fibroblast is a treadmilling network. The model of dendritic nucleation (Pollard and Borisy, 2003) combines the proteins of 13.3 into one cycle:

1. A signal activates Rac at the plasma membrane; Rac-GTP and PI(3,4,5)P₃ activate the WAVE complex.
2. WAVE activates the Arp2/3 complex on the side of existing filaments, near the membrane: new filaments branch at $70°$, so that most filaments point their plus ends towards the membrane at about $\pm 35°$.
3. The new plus ends, fed by profilin–actin, grow for a fraction of a second and push the membrane forward (Formula 13.4.1); then they are capped.
4. Behind the edge, the filaments age: ATP is hydrolyzed, phosphate released, and cofilin binds and severs the ADP-actin, assisted by coronin and Aip1.
5. Released ADP-actin binds profilin, exchanges ADP for ATP and diffuses back to the front.

The edge advances at the rate of polymerization minus the rate at which the network flows backward; the backward (retrograde) flow is driven by the membrane pushing on the network and by myosin II pulling it at the rear of the lamellipodium. When the network is attached to the substratum through adhesions, retrograde flow slows and protrusion speeds up, like a clutch engaging ([7.3.15](/7.3.15#sec-15.5)).

The geometry has a mechanical reason. A filament is a thin rod with flexural rigidity $\kappa = 7.3\times10^{-26}\,\mathrm{N\,m^2}$ (persistence length about $17\,\mu\mathrm{m}$; [7.3.15](/7.3.15#sec-15.3)), and a rod of free length $L$ pushed at its end buckles at the Euler force $F_{\mathrm{c}} = \pi^2\kappa/L^2$. A free filament longer than about $0.3\,\mu\mathrm{m}$ buckles before it can deliver its stall force. Short branches anchored in a cross-linked network, and parallel bundles in filopodia (whose rigidity scales with the number of filaments squared when they are tightly cross-linked), are the solutions the cell uses.

![How actin polymerization pushes. A: the dendritic network of a lamellipodium (schematic). WAVE (pink, activated by Rac-GTP) at the membrane activates the Arp2/3 complex (yellow dots) to nucleate branches; the plus ends that reach the membrane push it upward (protrusion), others are capped (pink caps); further back cofilin (orange) disassembles old filaments, and profilin–actin returns to the front, while the network flows backward relative to the edge. B: force–velocity relation of the polymerization ratchet (Formula 13.4.1) for three monomer concentrations, with the stall forces of Eq. (13.4) marked on the axis. C: the Euler buckling force of a single actin filament against its free length, compared with the stall force at 5 µM: filaments longer than about 0.3 µm buckle before they can push with full force](./plots/lamellipodium-ratchet.py)

Polymerization drives other movements as well: endocytic vesicles are pushed off the plasma membrane by short-lived Arp2/3 networks (especially in yeast, where turgor opposes invagination), the sperm of nematodes crawl with a polymer unrelated to actin (major sperm protein), and in podosomes and invadopodia of macrophages, osteoclasts and invasive cancer cells actin cores push into the matrix while proteases digest it.

## 13.5. Myosin

### 13.5.1. The Myosin Superfamily

**Definition 13.5.1 (Myosin)** A **myosin** is an actin-based motor protein whose heavy chain has a conserved N-terminal motor domain (head) with an ATP site and an actin-binding site, followed by a neck (lever arm) of one to six IQ motifs, each binding a light chain of the calmodulin family, and a tail that varies among classes and determines dimerization and cargo. Almost all myosins move towards the plus end of actin filaments.

Sequence comparisons divide the superfamily into some 35 classes; humans have about 40 myosin genes. The main ones in animal cells:

| Class | Heads | Function |
|---|---|---|
| Myosin I | one; tail binds membranes | links membranes to actin, microvilli, endocytosis |
| Myosin II | two; coiled-coil tail forms bipolar filaments | contraction: muscle, stress fibers, cortex, contractile ring |
| Myosin V | two; long lever arm (6 IQ) | processive transport of vesicles, organelles and mRNA on actin cables |
| Myosin VI | two; unique insert in the lever | moves towards the minus end; endocytosis, stereocilia |
| Myosin VII, XV | two | stereocilia; mutations cause hereditary deafness (Usher syndrome type 1B: myosin VIIa) |
| Myosin XI | two (plants) | cytoplasmic streaming, up to $60\,\mu\mathrm{m\,s^{-1}}$ in *Chara* |

**Definition 13.5.2 (Myosin II)** **Myosin II**, conventional myosin, is a hexamer of two heavy chains (about $2000$ residues each) and two pairs of light chains (essential and regulatory) bound to the necks. The heavy chains dimerize through a long α-helical **coiled coil** (the tail) and assemble tail to tail into bipolar filaments, with heads at both ends pointing away from a central bare zone: about 300 heads in the $1.6\,\mu\mathrm{m}$ thick filament of skeletal muscle, 15–30 in the short minifilaments of non-muscle cells.

A bipolar filament with heads walking towards the plus ends of two antiparallel sets of actin filaments pulls them towards each other. This simple arrangement contracts a sarcomere, a stress fiber, a contractile ring and the cortex alike.

### 13.5.2. The Cross-Bridge Cycle

Myosin was purified from muscle in the 19th century (Kühne) and shown to be an ATPase by Engelhardt and Ljubimova (1939); Szent-Györgyi found that threads of actomyosin contract when ATP is added. Kinetic studies of the actomyosin ATPase in solution (Lymn and Taylor, 1971) then revealed how hydrolysis is coupled to binding.

**Definition 13.5.3 (Cross-Bridge Cycle)** The **cross-bridge cycle** is the mechanochemical cycle of a myosin head on actin, in which each step of ATP binding, hydrolysis and product release changes the affinity of the head for actin and the position of its lever arm:

1. **Rigor**: without nucleotide, the head is bound tightly to actin with the lever in the post-stroke position;
2. **ATP binding** opens the actin-binding cleft and the head detaches within milliseconds;
3. **hydrolysis** on the detached head (ATP → ADP·Pi) re-cocks the lever (recovery stroke), and the head binds weakly to a new actin subunit further towards the plus end;
4. **phosphate release** strengthens binding and triggers the **power stroke**, in which the lever arm swings by about $60°$ and moves the filament by $5$–$10\,\mathrm{nm}$; **ADP release** returns the head to rigor.

One ATP is hydrolyzed per cycle. Without ATP heads stay in rigor: this is the cause of rigor mortis.

The amplification is structural. Small movements in the nucleotide pocket, about $0.1$–$0.5\,\mathrm{nm}$, rotate a converter domain at the base of the neck, and the $8.5\,\mathrm{nm}$ lever arm, stiffened by its light chains, turns this rotation into a movement of $5\,\mathrm{nm}$ or more at its end. The step size scales with lever length: myosin V, with a lever three times longer, takes $36\,\mathrm{nm}$ steps; shortening or lengthening the lever of myosin II by protein engineering changes the sliding velocity proportionally (Uyeda, Abramson and Spudich, 1996).

![The cross-bridge cycle of myosin II (schematic; actin plus end on the right, the thick filament above). 1, rigor: the nucleotide-free head is bound tightly, its lever in the post-stroke position. 2, ATP binds and the head detaches. 3, hydrolysis to ADP·Pi on the detached head re-cocks the lever (recovery stroke), and the head binds weakly to a subunit further towards the plus end. 4, phosphate release triggers the power stroke: the lever swings towards the plus end and the thick filament is pulled to the right relative to actin (compare the tail with the dashed mark, its position in state 1); ADP release returns the head to rigor](./plots/myosin-crossbridge-cycle.py)

Two kinds of experiment measure the cycle on single molecules. In the *in vitro motility assay* (Sheetz and Spudich, 1983; Kron and Spudich, 1986) myosin is attached to a glass surface and fluorescent actin filaments glide over it when ATP is added; the velocity, a few micrometers per second for skeletal myosin II, equals that of unloaded muscle. In the optical-trap assay a filament held between two trapped beads is lowered onto a single myosin; its displacements reveal individual power strokes of a few nanometers and forces of a few piconewtons (Finer, Simmons and Spudich, 1994). The physics of these instruments is treated in [7.6](/7.6).

### 13.5.3. Muscle Contraction in Outline

Skeletal muscle is the most ordered actin–myosin system. Its fibers contain myofibrils, chains of sarcomeres about $2.2\,\mu\mathrm{m}$ long, in which thin filaments of actin, anchored with their plus ends in the Z discs by α-actinin and capped by CapZ and tropomodulin, interdigitate with bipolar thick filaments of myosin II held in the center by the M line and connected to the Z discs by the giant elastic protein titin ([7.1.7](/7.1.7#sec-7.5)). The sliding filament model (A. F. Huxley and Niedergerke; H. E. Huxley and Hanson, 1954) states that the filaments keep their length while they slide past each other, so that the A band stays constant while the I band and H zone shorten; the dependence of active tension on sarcomere length (Gordon, Huxley and Julian, 1966) measures the overlap between thick and thin filaments and confirms it.

Contraction is switched on by $\ce{Ca^2+}$. An action potential spreads into the T tubules, voltage sensors there open $\ce{Ca^2+}$ release channels of the sarcoplasmic reticulum, and cytosolic $\ce{Ca^2+}$ rises about a hundredfold; $\ce{Ca^2+}$ binds troponin C, and the troponin complex shifts tropomyosin on the thin filament away from the myosin-binding sites. When $\ce{Ca^2+}$ is pumped back, tropomyosin blocks the sites again. Excitation–contraction coupling, the mechanics of the length–tension and force–velocity relations, and heart and smooth muscle belong to [7.14](/7.14).

### 13.5.4. Non-Muscle Myosin II

Smooth muscle and non-muscle cells regulate myosin itself rather than the thin filament. Phosphorylation of the regulatory light chain (Ser19) by myosin light-chain kinase, activated by $\ce{Ca^2+}$ and **calmodulin**, or by Rho kinase (ROCK), unfolds the inactive, folded myosin and lets it assemble into minifilaments and bind actin; myosin light-chain phosphatase reverses it, and ROCK also inhibits the phosphatase. Contraction is therefore controlled by both $\ce{Ca^2+}$ and the Rho pathway ([7.3.15](/7.3.15#sec-15.5)). Non-muscle myosin II contracts the cortex, generating the tension that rounds cells in mitosis and drives blebs; it tightens the circumferential belts of epithelial cells during tissue folding; it builds the contractile ring that divides cells ([7.3.21](/7.3.21)); and it retracts the rear of migrating cells.

### 13.5.5. Duty Ratio and Processivity

Myosin II and myosin V solve different problems. Myosin II works in ensembles: hundreds of heads on a filament must not get in each other's way, so each head should spend most of its cycle detached. Myosin V carries a vesicle alone: one of its two heads must always hold the track.

**Definition 13.5.4 (Duty Ratio)** The **duty ratio** $r$ of a motor is the fraction of its mechanochemical cycle that a head spends strongly bound to its track: $r = \tau_{\mathrm{on}}/(\tau_{\mathrm{on}} + \tau_{\mathrm{off}})$. A two-headed motor with a high duty ratio and coordinated heads is **processive**: it takes many steps before it lets go.

**Formula 13.5.1 (Ensembles of Low-Duty-Ratio Motors)** For $N$ independent heads with duty ratio $r$, the probability that at least one is bound is $1 - (1 - r)^N$. If each attached head moves the filament by its step $d$ during its attached time $\tau_{\mathrm{on}}$, the filament slides at

$$
v \approx \frac{d}{\tau_{\mathrm{on}}}\left[1 - (1 - r)^N\right],
\tag{13.5}
$$
which saturates at $d/\tau_{\mathrm{on}}$ once $N \gg 1/r$.

Skeletal myosin II has $r \approx 0.04$, $d \approx 5\,\mathrm{nm}$ and $\tau_{\mathrm{on}} \approx 1\,\mathrm{ms}$: about a hundred heads are needed for smooth sliding at $5\,\mu\mathrm{m\,s^{-1}}$, and filaments shorter than that, with fewer heads, slide intermittently, as observed (Uyeda, Kron and Spudich, 1990). The maximal speed is set by how fast a head detaches after its stroke (ADP release), not by how many heads pull: more heads add force, not speed, which is why a thick filament can carry high loads at the velocity of a single head. The low duty ratio has a price, high ATP consumption per unit of force held, which smooth muscle avoids by a latch state of slowly cycling dephosphorylated heads.

Myosin V has a duty ratio of about $0.7$, because ADP release from the bound head is slow. Its two heads alternate: the rear head detaches after ATP binds, swings forward by $72\,\mathrm{nm}$ past the bound head and lands $36\,\mathrm{nm}$ ahead of the center, the half-repeat of the actin helix, so the molecule walks straight along one face of the filament. That the movement is hand over hand, not inchworm, was shown by labeling one head with a single fluorophore and localizing it with nanometer precision: it moved in alternating steps of $72$ and $0\,\mathrm{nm}$ (Yildiz and colleagues, 2003). Strain between the heads keeps them out of phase: the front head, pulled backward, releases ADP more slowly than the rear one. A single myosin V moves about $1\,\mu\mathrm{m}$ (some 30 steps) before detaching, at $0.3$–$0.5\,\mu\mathrm{m\,s^{-1}}$, and stalls at about $3\,\mathrm{pN}$; its **processivity** matches its job of carrying melanosomes into the dendrites of melanocytes, secretory vesicles into the yeast bud, and mRNAs along actin cables.

![Duty ratio and processivity. A: probability that at least one of $N$ independent heads is bound, $1-(1-r)^N$, for skeletal muscle myosin II ($r \approx 0.04$), a non-muscle myosin II (0.2) and myosin V (0.7): a two-headed myosin V almost never lets go, while myosin II needs tens of heads. B: simulated sliding velocity of an actin filament moved by $N$ skeletal myosin heads ($d = 5$ nm, $\tau_{\mathrm{on}} = 1$ ms): the velocity rises with the number of heads and saturates at $d/\tau_{\mathrm{on}} = 5\,\mu\mathrm{m\,s^{-1}}$ (Formula 13.5.1, line). C: a simulated trace of myosin V at low ATP: its center moves in 36 nm steps, while a label on one head moves 72 nm on every second step, the signature of hand-over-hand walking](./plots/myosin-duty-ratio.py)

The two strategies recur among microtubule motors: kinesin-1, like myosin V, is a processive porter, while the axonemal dyneins, like muscle myosin, work in large arrays ([7.3.14](/7.3.14)).

## Summary

| Topic | Key points |
|---|---|
| Three systems (13.1, Definitions 13.1.1–13.1.2) | Actin (7 nm, ATP, polar), microtubules (25 nm, GTP, polar), intermediate filaments (10 nm, no nucleotide, nonpolar); noncovalent multi-stranded polymers: stable bodies, dynamic ends; motors: myosins on actin, kinesins and dyneins on microtubules; low Reynolds number ($\sim 10^{-5}$): no coasting; drugs: latrunculin, cytochalasin, phalloidin, taxol, colchicine, nocodazole, vinca alkaloids |
| Actin filament (13.2.1, Definitions 13.2.1–13.2.2) | 375-residue ATPase; two-stranded helix, $2.75\,\mathrm{nm}$ per subunit, crossover $37\,\mathrm{nm}$; barbed (plus) and pointed (minus) end, arrowheads of bound myosin point to the minus end |
| Kinetics (13.2.2–13.2.3, Definitions 13.2.3–13.2.4, Formula 13.2.1, Proposition 13.2.1) | Nucleation (trimer) is rate-limiting, lag phase, $t_{1/2} \propto c^{-n/2}$; $C_{\mathrm{c}} = k_{\mathrm{off}}/k_{\mathrm{on}} \approx 0.1\,\mu\mathrm{M}$; plus end $k_{\mathrm{on}} = 11.6\,\mu\mathrm{M^{-1}\,s^{-1}}$; without hydrolysis both ends have the same $C_{\mathrm{c}}$ |
| Treadmilling (13.2.4, Definition 13.2.5, Formula 13.2.2) | Hydrolysis in the filament, slow Pi release, ADP-actin less stable; $C_{\mathrm{c}}^{+} < c < C_{\mathrm{c}}^{-}$; $c_{\mathrm{tm}} \approx 0.13\,\mu\mathrm{M}$, flux $0.1\,\mathrm{s^{-1}}$ in vitro, 100-fold faster in cells |
| Binding proteins (13.3, Definitions 13.3.1–13.3.7) | Thymosin β4 buffers, profilin feeds plus ends; formins (processive, unbranched; Rho) and the Arp2/3 complex (branches at 70°; NPFs WASP/N-WASP with Cdc42 and PIP₂, WAVE with Rac); capping protein focuses growth; cofilin severs old ADP-actin (LIM kinase inhibits); gelsolin ($\ce{Ca^2+}$); fimbrin/fascin vs α-actinin bundles, filamin gels, ERM and spectrin membrane links; cortex, lamellipodium, filopodium, stress fiber, microvilli |
| Force from polymerization (13.4, Definition 13.4.1, Formula 13.4.1) | Listeria (ActA → Arp2/3; reconstituted from four proteins); ratchet $v = \delta(k_{\mathrm{on}}c\,\mathrm{e}^{-f\delta/k_{\mathrm{B}}T} - k_{\mathrm{off}})$, $f_{\mathrm{s}} = (k_{\mathrm{B}}T/\delta)\ln(c/C_{\mathrm{c}}) \approx 7\,\mathrm{pN}$; dendritic nucleation cycle; retrograde flow; buckling $F_{\mathrm{c}} = \pi^2\kappa/L^2$ limits pushing filaments to $\lesssim 0.3\,\mu\mathrm{m}$ |
| Myosin (13.5, Definitions 13.5.1–13.5.4, Formula 13.5.1) | Superfamily (I, II, V, VI minus-end, VII, XI); myosin II bipolar filaments; cross-bridge cycle: rigor → ATP release → hydrolysis, recovery → Pi release, power stroke → ADP release; lever arm amplifies; motility assay and optical trap; sarcomere and sliding filaments, troponin–tropomyosin (details in 7.14); non-muscle regulation by RLC phosphorylation (MLCK, ROCK); duty ratio: myosin II $0.04$ (ensembles, $v = d/\tau_{\mathrm{on}}$), myosin V $0.7$ (processive, 36 nm hand-over-hand steps) |

## Questions

1. A solution of $5\,\mu\mathrm{M}$ ATP-actin is induced to polymerize. (a) How much actin is in filaments at steady state? (b) The experiment is repeated with $1\,\mu\mathrm{M}$ cytochalasin D, which caps plus ends. What changes? (c) And with $5\,\mu\mathrm{M}$ latrunculin A?

   **Answer** (a) All but the critical concentration: about $4.9\,\mu\mathrm{M}$ (with $C_{\mathrm{c}} \approx 0.1\,\mu\mathrm{M}$ for the plus end). (b) With plus ends capped, only minus ends exchange subunits, and the free concentration rises to the minus-end critical concentration (about $0.6\,\mu\mathrm{M}$ for ATP-actin, higher if the ends carry ADP-actin), so somewhat less actin polymerizes, and it polymerizes much more slowly, because the minus end has a ninefold lower $k_{\mathrm{on}}$. (c) Latrunculin sequesters monomers 1 : 1; it binds tightly, so about $5\,\mu\mathrm{M}$ actin is removed from the pool, leaving almost nothing above the critical concentration: little or no polymer forms.

2. Using Formula 13.2.1, explain how a plot of the half-time of polymerization against actin concentration can reveal the size of the nucleus. Why is the method only approximate?

   **Answer** At early times $M \propto k_{\mathrm{n}}k_{\mathrm{on}}c^{n+1}t^2$, so the time to reach a fixed fraction of the final polymer (proportional to $c$) scales as $c^{-n/2}$; the slope of $\log t_{1/2}$ against $\log c$ is $-n/2$. It is approximate because the early-time expansion ignores monomer depletion and dissociation, because nucleation may proceed through several unstable intermediates with their own rate constants rather than a single step of order $n$, because filament fragmentation and annealing create or remove ends, and because pyrene fluorescence and real filament mass are not perfectly proportional. Fits of complete kinetic models are used in practice.

3. Why must the critical concentrations of the two ends be equal for a polymer that does not hydrolyze its nucleotide, and how does ATP hydrolysis allow them to differ? What would happen to treadmilling in a filament polymerized from actin bound to a nonhydrolyzable ATP analog?

   **Answer** The free energy of adding a subunit is the same at either end (Proposition 13.2.1), so $k_{\mathrm{off}}/k_{\mathrm{on}}$ is the same. With hydrolysis, the subunit that adds (ATP-actin) differs from the one that leaves (ADP-actin at an end where hydrolysis has caught up), so the ratio at each end compares different reactions, and the minus end, where addition is slow and hydrolysis catches up, has a higher $C_{\mathrm{c}}$. The steady state is maintained by a continuous input of free energy (ATP hydrolysis, nucleotide exchange on free monomers). With a nonhydrolyzable analog all subunits stay in the T state, the two critical concentrations become equal, and treadmilling disappears: at steady state both ends just fluctuate around zero net growth.

4. A single actin filament pushes against a membrane under a load of $2\,\mathrm{pN}$ at $c = 10\,\mu\mathrm{M}$ free ATP-actin. Using Formula 13.4.1, estimate its velocity and compare it with the unloaded velocity. How would profilin, which raises the effective $k_{\mathrm{on}}$, and capping protein, which reduces the number of growing ends, affect the speed of a whole lamellipodium?

   **Answer** $f\delta/k_{\mathrm{B}}T = 2 \times 2.7/4.1 = 1.32$, $\mathrm{e}^{-1.32} = 0.27$. Unloaded: $v_0 = 2.7\,\mathrm{nm} \times (116 - 1.4)\,\mathrm{s^{-1}} \approx 310\,\mathrm{nm\,s^{-1}}$. Loaded: $v = 2.7 \times (116 \times 0.27 - 1.4) \approx 81\,\mathrm{nm\,s^{-1}}$, about a quarter. Profilin and formins raise the rate of addition and hence both velocity and stall force (logarithmically). Capping reduces the number of ends competing for monomers; the remaining ends grow at higher free monomer concentration, and in the reconstituted Listeria system an optimal concentration of capping protein maximizes speed: too little and monomers are depleted by many ends, too much and too few ends push.

5. Skeletal muscle myosin II and myosin V differ in duty ratio. (a) Explain with Formula 13.5.1 why a short actin filament moves smoothly over a surface coated with myosin V but jerkily over a sparse coating of myosin II. (b) Why does increasing the number of myosin II heads not increase the unloaded sliding velocity? (c) Which kinetic step sets the duty ratio of each motor?

   **Answer** (a) With $r = 0.04$, a filament in contact with 5 heads has at least one bound only $1 - 0.96^5 \approx 18\,\%$ of the time and diffuses away or pauses in between; with $r = 0.7$ even one two-headed myosin V keeps the filament attached ($1 - 0.3^2 \approx 91\,\%$ for independent heads, and more with gating). (b) Once a head is always attached, the filament slides at the speed with which heads finish their strokes and detach, $d/\tau_{\mathrm{on}}$; additional heads cannot make the strokes faster and, if they detach late, they drag. (c) In myosin II, the rapid release of ADP after the power stroke followed by fast ATP binding keeps the attached time short; in myosin V, ADP release is slow (rate-limiting), so the head stays strongly bound most of the cycle.

6. (Open) Fluorescent speckle microscopy of a lamellipodium shows speckles moving backward at $2\,\mu\mathrm{m\,min^{-1}}$ while the leading edge advances at $4\,\mu\mathrm{m\,min^{-1}}$. (a) What is the rate of polymerization at the edge? (b) How do you expect the two rates to change if the cell is plated on a more adhesive substratum, or treated with a myosin II inhibitor? (c) Where in the lamellipodium would you expect speckles to appear and disappear?

   **Answer** (a) Edge velocity = polymerization rate − retrograde flow, so polymerization adds network at $6\,\mu\mathrm{m\,min^{-1}}$ relative to the substratum frame of the network, i.e. $4 + 2$. (b) Stronger adhesion engages the "clutch": the network is held against the substratum, retrograde flow slows, and more of the polymerization goes into protrusion (the edge speeds up, if polymerization is unchanged). Blocking myosin II reduces the pulling at the rear of the lamellipodium and slows retrograde flow, often with faster protrusion at first. (c) Speckles appear (assembly) mainly in a narrow band at the leading edge, where plus ends grow, and disappear (disassembly) over a broader zone further back, where cofilin acts on older ADP-actin; the mature network treadmills from front to back.
