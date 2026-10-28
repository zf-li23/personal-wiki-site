---
title: Biological Membranes and Transport
description: The lipid bilayer and the composition, asymmetry and proteins of biological membranes; hydropathy plots and lipid anchors; membrane fluidity, flip-flop, lateral diffusion (FRAP, Saffman–Delbrück), rafts, curvature and fusion; the thermodynamics of transport; transporters and channels; GLUT1 and the anion exchanger; P-, V- and F-type ATPases, ABC transporters and secondary active transport; ionophores, aquaporins and the K⁺ channel.
---

Every cell is bounded by a membrane, and in **eukaryotes** membranes also divide the interior into compartments with different compositions. A biological membrane is a lipid bilayer, a sheet two molecules thick held together by the **hydrophobic effect** ([7.1.2](/7.1.2#sec-2.1.3)), in which **proteins** are embedded or to which they are attached. The bilayer is a barrier to ions and polar molecules; the proteins make it selectively permeable, receive signals, and in mitochondria and chloroplasts convert energy. Following the thread of Part I, this chapter derives the properties of membranes from the chemistry of their components: the amphipathic membrane **lipids** of [7.1.12](/7.1.12#sec-12.4) determine the thickness, fluidity and asymmetry of the bilayer; the hydrophobicity of amino acid **side chains** ([7.1.3](/7.1.3)) determines how a protein spans it; and the thermodynamics of the **electrochemical potential** ([6.3.13](/6.3.13#sec-13.4.2)) determines which transport processes are spontaneous and how much energy the others need. Transporters behave like **enzymes** ([7.1.9](/7.1.9)), and the coupling of a downhill flow to an uphill one, described abstractly in [6.3.18](/6.3.18#sec-18.2.5), is made concrete here by pumps and cotransporters. Membrane **receptors** and gated channels as signal transducers follow in [7.1.14](/7.1.14) and [7.1.15](/7.1.15); vesicle traffic, endocytosis and cell junctions belong to cell biology ([7.3](/7.3)); the electrical behaviour of excitable membranes to [7.16](/7.16).

## 13.1. The Composition and Architecture of Membranes

### 13.1.1. The Lipid Bilayer

**Glycerophospholipids**, **sphingolipids** and **sterols** are almost insoluble in water. Mixed with water they form aggregates in which the hydrocarbon chains are shielded from the solvent and the polar head groups face it, which releases ordered water from the hydrocarbon surface and increases the entropy of the system. The shape of the molecule decides which aggregate forms. Free **fatty acids**, lysophospholipids and detergents such as SDS, whose head group is wider than the single chain, pack into **micelles** ([6.3.19](/6.3.19)); glycerophospholipids and sphingolipids, whose two chains are about as wide as the head group, pack side by side into a bilayer.

**Definition 13.1.1 (Lipid Bilayer)** A **lipid bilayer** is a sheet formed by two monolayers (leaflets) of amphipathic lipids, with their hydrocarbon chains in contact in the interior and their head groups facing the water on either side. A bilayer closed on itself, enclosing an aqueous compartment, is a lipid vesicle or **liposome**.

An open bilayer sheet exposes hydrocarbon at its edges, so it closes spontaneously into a vesicle, which has no edges at all; for the same reason a punctured membrane reseals. The hydrocarbon core is about as nonpolar as decane and about $3\,\mathrm{nm}$ thick, roughly two extended acyl chains; the head-group regions add about $1\,\mathrm{nm}$ on each side, and with the proteins that protrude from both faces a biological membrane is $5$ to $8\,\mathrm{nm}$ thick. Vesicles are also the likely form of the first compartments that separated a living system from its surroundings.

### 13.1.2. Each Membrane Has Characteristic Lipids and Proteins

The proportions of protein and lipid reflect what a membrane does. The myelin sheath of neurons, an electrical insulator, is mostly lipid; the plasma membranes of bacteria and the inner membranes of mitochondria and chloroplasts, sites of many enzyme-catalyzed processes, are mostly protein.

| Plasma membrane of | Protein | Phospholipid | Sterol | Sterol type | Other lipids |
|---|---|---|---|---|---|
| Human myelin sheath | 30 | 30 | 19 | **cholesterol** | galactolipids, **plasmalogens** |
| Mouse liver | 45 | 27 | 25 | cholesterol | — |
| Maize leaf | 47 | 26 | 7 | sitosterol | galactolipids |
| Yeast | 52 | 7 | 4 | ergosterol | triacylglycerols, steryl esters |
| *Paramecium* (ciliated protist) | 56 | 40 | 4 | stigmasterol | — |
| *E. coli* | 75 | 25 | 0 | — | — |

(Mass percent; Lehninger, earlier editions, Table 11-1.)

Within one cell the organelles differ just as much. In a rat hepatocyte the plasma membrane is rich in cholesterol and sphingolipids and contains no cardiolipin; the mitochondrial membranes contain almost no cholesterol or sphingolipid but most of the cell's phosphatidylglycerol and cardiolipin, which are made in mitochondria, and cardiolipin is required for the assembly of the respiratory complexes ([7.1.23](/7.1.23)). Most membrane lipids and proteins are made in the endoplasmic reticulum (ER) and reach their destination in two ways: in vesicles that bud from one compartment and fuse with the next (ER → Golgi apparatus → plasma membrane, endosomes and lysosomes, the endomembrane system of [7.3](/7.3)), and, faster, through lipid transfer proteins, soluble proteins with a hydrophobic pocket that carry single lipid molecules through the cytosol at contact sites between membranes.

### 13.1.3. Membranes Are Asymmetric

The two leaflets of the plasma membrane have different compositions. The choline-containing lipids phosphatidylcholine and **sphingomyelin** are mostly in the outer (exoplasmic) leaflet; phosphatidylserine, phosphatidylethanolamine and the phosphatidylinositols are almost exclusively in the inner (cytoplasmic) leaflet, where the negative charges of serine and the inositol phosphates bind the positively charged regions of peripheral proteins. **Glycolipids** and the oligosaccharides of **glycoproteins** are always on the outer face. Every transmembrane protein also has a fixed orientation: glycophorin, for example, always has its glycosylated **domain** outside the erythrocyte. The asymmetry of lipids is produced by enzymes that move them between leaflets (13.2.2), and its loss is a signal: phosphatidylserine exposed on the outer face marks a cell undergoing **apoptosis** for engulfment by macrophages ([7.1.15](/7.1.15)), and on activated platelets it provides the surface on which coagulation factors assemble ([7.1.9](/7.1.9#sec-9.5.5)).

### 13.1.4. Integral, Peripheral and Amphitropic Proteins

Membrane proteins are classified operationally, by what it takes to remove them from the membrane.

**Definition 13.1.2 (Classes of Membrane Proteins)** An **integral membrane protein** is held in the membrane by hydrophobic interactions between nonpolar parts of the protein and the hydrocarbon core of the bilayer, and can be released only by agents that disrupt these interactions (detergents, organic solvents). A **peripheral membrane protein** is bound by electrostatic interactions and hydrogen bonds to the head groups of lipids or to integral proteins, and is released by mild treatments (high salt, changes of pH, chelators). An **amphitropic protein** associates with the membrane reversibly, depending on a regulatory process (phosphorylation, ligand binding, attachment of a lipid), and is found both in the membrane and in the cytosol.

Integral proteins are further distinguished by how they cross the bilayer: monotopic proteins penetrate only one leaflet with a small hydrophobic surface (**prostaglandin H₂ synthase**, the target of aspirin), bitopic proteins cross once (glycophorin, **receptor tyrosine kinases**), and polytopic proteins cross several times (bacteriorhodopsin, transporters, **G protein–coupled receptors**).

![How proteins associate with the lipid bilayer. Integral proteins: a bitopic protein with one transmembrane helix and a glycosylated extracellular domain (glycophorin); a polytopic protein with seven transmembrane helices (bacteriorhodopsin, GPCRs); a β-barrel protein (porin); a monotopic protein in the inner leaflet only (prostaglandin H₂ synthase). A peripheral protein bound to head groups and to an integral protein. Lipid-anchored proteins: GPI-anchored on the outer face; N-myristoylated and S-palmitoylated, and prenylated (farnesylated, as Ras), on the inner face. Glycans (green) are always on the extracellular side](./plots/membrane-proteins.py)

Bacteriorhodopsin, a light-driven proton pump of the purple membrane of *Halobacterium salinarum*, was the first polytopic protein whose structure was seen: seven α helices of about 20 hydrophobic **residues** each cross the bilayer almost perpendicularly, joined by hydrophilic loops on the two faces, with the chromophore retinal buried among them. The same seven-helix arrangement recurs in the receptors of [7.1.14](/7.1.14). Crystal and **cryo-EM** structures of membrane proteins often contain bound lipids: some fill grooves between **subunits**, and a ring of lipids (the annulus) seals the protein into the bilayer.

### 13.1.5. Predicting Topology from Sequence: Hydropathy Plots

Determining the three-dimensional structure of a membrane protein is still much harder than determining its sequence, but the sequence alone usually identifies the membrane-spanning segments. A **polypeptide** in the bilayer has no water to hydrogen-bond with, so its backbone forms α helices or **β sheets** in which every NH and C=O is hydrogen-bonded internally; an **α helix** rises $0.15\,\mathrm{nm}$ per residue ([7.1.5](/7.1.5#sec-5.2.2)), so about 20 residues span the $3\,\mathrm{nm}$ core, and its side chains must be mostly nonpolar.

**Definition 13.1.3 (Hydropathy Plot)** A **hydropathy plot** is the average **hydropathy index** ([7.1.3](/7.1.3)) of the residues in a window of $w$ consecutive residues, plotted against the position of the central residue as the window slides along the sequence:

$$
\bar h(i) = \frac{1}{w}\sum_{j = i - (w-1)/2}^{i + (w-1)/2} h_j .
$$
With the Kyte–Doolittle scale and $w = 19$, a peak above about $1.6$ indicates a likely transmembrane helix.

Narrow windows (7 residues) reveal short features such as amphipathic helices and turns; wide windows (15–21 residues, about the length of a transmembrane helix) average out noise. The plot for glycophorin shows a single transmembrane helix; that for bacteriorhodopsin shows seven hydrophobic regions, although the last two are poorly resolved, because the seventh helix carries the lysine that binds retinal and other polar residues. Applied to whole **genomes**, such analyses predict that 20% to 30% of all proteins are integral membrane proteins. Two further regularities help to orient the helices. Tyr and Trp side chains cluster at the interface between the hydrocarbon core and the head groups, where their amphipathic rings interact with both, forming two aromatic belts; charged residues are found almost exclusively outside the core. And by the *positive-inside rule*, Lys and Arg in the loops between transmembrane segments are much more frequent on the cytoplasmic side. Modern predictors (and structure prediction, [7.1.6](/7.1.6)) combine these signals, but the sliding-window average remains their basis.

![Hydropathy plots with the Kyte–Doolittle scale and a window of 19 residues, computed from the UniProt sequences (precursor numbering); shaded bands are the transmembrane segments known from the structures. A: human glycophorin A has one transmembrane helix (residues 92–114 of the precursor; 73–95 of the mature protein); the hydrophobic N-terminal peak is the signal peptide, removed during synthesis. B: bacteriorhodopsin of *Halobacterium salinarum* has seven transmembrane helices, A–G; the peaks of F and G barely cross the threshold, showing the limits of the method](./plots/hydropathy-plot.py)

Not all integral proteins are helical. In the outer membranes of gram-negative bacteria, mitochondria and chloroplasts the common **motif** is the *β barrel*: a β sheet of 8 to 26 strands closed into a cylinder. Because the **β conformation** is more extended (about $0.33\,\mathrm{nm}$ per residue), 7 to 9 residues suffice to span the membrane, and since adjacent side chains point to opposite sides of a strand, only every second residue needs to be hydrophobic (facing the lipid), while the others can line a water-filled pore. Porins of this type let sugars, ions and amino acids cross the outer membrane of *E. coli*; FepA (iron uptake) has 22 strands, maltoporin 16. A hydropathy plot does not detect β barrels, whose strands are too short and alternate in polarity.

### 13.1.6. Covalently Attached Lipids Anchor Some Proteins

Some membrane proteins are held by one or more covalently attached lipids.

| Anchor | Attachment | Typical location | Reversible? |
|---|---|---|---|
| N-Myristoyl (14:0) | amide to an N-terminal Gly | cytoplasmic face (Src, Gα subunits) | no |
| S-Palmitoyl (16:0) | thioester to Cys | cytoplasmic face, often with a second anchor; enriched in rafts | yes |
| Farnesyl (C15) or geranylgeranyl (C20) | thioether to the Cys of a C-terminal CaaX box; the Cys is then methylated | cytoplasmic face (**Ras**, Gγ, Rab) | no |
| Glycosylphosphatidylinositol (GPI) | the C-terminal residue joined through phosphoethanolamine to an oligosaccharide on phosphatidylinositol | outer face only; enriched in rafts and, in epithelia, on the apical surface | cleavable by phospholipases |

A single hydrocarbon chain barely holds a protein in the bilayer, so many anchored proteins carry two lipids or add electrostatic attraction. MARCKS, a **substrate** of **protein kinase C**, has a myristoyl group and a cluster of Lys and Arg residues that bind the negative head groups of PIP₂; when the head groups are hydrolyzed or the basic cluster is phosphorylated, the protein leaves the membrane, so it is amphitropic. Because each anchor type prefers a particular leaflet and lipid environment, lipidation also targets a protein to a particular location.

## 13.2. Membrane Dynamics

### 13.2.1. Membrane Fluidity and Phase Behavior

Although the bilayer is stable, its individual lipids move constantly, and how much they move depends on temperature and composition. A bilayer of a single lipid species has a sharp transition at a **melting temperature** $T_{\mathrm{m}}$: below it the chains are extended and packed in a regular array, and both rotation about C–C bonds and lateral motion are strongly restricted (the gel or solid-ordered phase); above it the chains are disordered by rotation about their C–C bonds and the lipids diffuse rapidly in the plane (the liquid-disordered or fluid phase). The thickness and the barrier function are kept in both phases; only the freedom of motion changes. Long saturated chains raise $T_{\mathrm{m}}$; cis double bonds and short chains lower it ([7.1.12](/7.1.12#sec-12.2.2)). Cholesterol has a dual effect: its rigid ring system orders the chains of fluid lipids and thickens the bilayer, while it disrupts the packing of saturated chains that would otherwise be in the gel phase. Mixtures of cholesterol with sphingolipids or saturated phospholipids form a third state, the liquid-ordered phase, in which the chains are extended and ordered yet the lipids diffuse almost as fast as in a fluid bilayer.

Biological membranes are kept in the fluid range by adjusting their composition, a response called homeoviscous adaptation. *E. coli* grown at low temperature incorporates more unsaturated and shorter fatty acids into its phospholipids; in the leg of a reindeer, membranes near the cold hooves contain more unsaturated fatty acids than those near the warm body.

### 13.2.2. Transbilayer Movement Requires Catalysis

Lateral exchange of neighboring lipids takes microseconds, but the uncatalyzed movement of a phospholipid from one leaflet to the other, which requires its head group to cross the hydrocarbon core, takes hours to days. Cells need such movement, because glycerophospholipids are synthesized on the cytosolic leaflet of the ER, and they control it with three kinds of proteins.

**Definition 13.2.1 (Lipid Translocators)** A **flippase** moves phospholipids (mainly phosphatidylserine and phosphatidylethanolamine) from the outer to the cytoplasmic leaflet of the plasma membrane, using about one ATP per lipid; flippases are P-type ATPases (13.5.2). A **floppase** moves phospholipids and sterols from the cytoplasmic to the outer leaflet, also using ATP; floppases are ABC transporters (13.5.4). A **scramblase** moves any phospholipid in either direction, down its concentration gradient, without ATP; many scramblases are activated by $\ce{Ca^2+}$.

Asymmetric synthesis, the near absence of spontaneous flip-flop and the action of ATP-driven translocators together generate the asymmetry of 13.1.3; a burst of scramblase activity, triggered by a rise in cytosolic $\ce{Ca^2+}$ or by **caspases** during apoptosis, randomizes the leaflets in minutes and exposes phosphatidylserine.

### 13.2.3. Lateral Diffusion of Lipids and Proteins

Lipids and many proteins diffuse in the plane of the membrane by **Brownian motion** ([6.3.21](/6.3.21#sec-21.3.1)). In two dimensions the mean squared displacement grows as $\langle r^2\rangle = 4Dt$; with $D \approx 1\,\mu\mathrm{m^2\,s^{-1}}$ for a lipid, a molecule travels about $2\,\mu\mathrm{m}$ in one second and could cross a eukaryotic cell in a few minutes. The standard measurement is the following.

**Definition 13.2.2 (FRAP)** **Fluorescence recovery after photobleaching** (FRAP) measures lateral diffusion in a membrane whose lipids or proteins carry a fluorescent label: a small region is bleached with an intense laser pulse, and the recovery of fluorescence in that region, as unbleached molecules diffuse in and bleached ones diffuse out, is recorded with weak illumination.

**Formula 13.2.1 (FRAP Recovery)** For a uniformly bleached circular spot of radius $w$ in a membrane with diffusion coefficient $D$ and mobile fraction $M_{\mathrm{f}}$, the fraction of the fluorescence that has recovered at time $t$ after bleaching is

$$
F(t) = M_{\mathrm{f}}\,\mathrm{e}^{-2\tau_D/t}\left[I_0\!\left(\frac{2\tau_D}{t}\right) + I_1\!\left(\frac{2\tau_D}{t}\right)\right], \qquad \tau_D = \frac{w^2}{4D},
$$
where $I_0$ and $I_1$ are modified Bessel functions (Soumpasis, 1983). Half of the mobile fluorescence returns at $t = \tau_D$.

Fitting a recovery curve therefore gives two numbers: the half-time, hence $D$, and the plateau, hence the fraction of molecules free to move. Lipids typically have $D$ of 0.1–$1\,\mu\mathrm{m^2\,s^{-1}}$; membrane proteins in the plasma membrane are 10 to 100 times slower and often partly immobile, whereas the same proteins reconstituted in pure lipid bilayers diffuse at a few $\mu\mathrm{m^2\,s^{-1}}$. The theory of diffusion in a thin viscous sheet explains why size matters so little.

**Formula 13.2.2 (Saffman–Delbrück Relation)** A cylinder of radius $a$ spanning a membrane of thickness $h$ and viscosity $\mu_{\mathrm{m}}$, surrounded by water of viscosity $\mu$, has the lateral diffusion coefficient

$$
D = \frac{k_{\mathrm{B}}T}{4\pi\mu_{\mathrm{m}}h}\left[\ln\frac{\mu_{\mathrm{m}}h}{\mu a} - \gamma\right],
$$
where $\gamma \approx 0.577$ is Euler's constant; it holds for $a \ll \mu_{\mathrm{m}}h/\mu$ (a few hundred nanometres).

With $h = 4\,\mathrm{nm}$, $\mu_{\mathrm{m}} = 0.1\,\mathrm{Pa\,s}$ and $a = 2\,\mathrm{nm}$, $D \approx 4\,\mu\mathrm{m^2\,s^{-1}}$ at $37\,^\circ\mathrm{C}$, and a tenfold larger radius lowers $D$ by less than a factor of two, whereas the **Stokes–Einstein equation** for a sphere in water gives a tenfold decrease. The much slower and partial mobility of proteins in cells therefore reflects their interactions, not their size: crowding by other proteins, binding to the cytoskeleton, and confinement. Single-particle tracking at up to 40 000 frames per second shows that a lipid in the plasma membrane diffuses freely within a compartment some 30–250 nm across and only occasionally jumps into the next one (hop diffusion), as if fenced in. The fences are probably transmembrane proteins tethered to the cortical cytoskeleton; in erythrocytes, glycophorin and the anion exchanger (13.4.2) are linked through ankyrin to a network of spectrin filaments that also gives the cell its resistance to deformation.

![Lateral diffusion in membranes. A: FRAP recovery of a 5 µm² spot (radius 1.26 µm) from Formula 13.2.1: a lipid (D = 1 µm² s⁻¹) recovers within seconds; a protein with D = 0.05 µm² s⁻¹ recovers about twenty times more slowly, and to only 70% if 30% of the molecules are immobile. B: the Saffman–Delbrück relation (Formula 13.2.2; h = 4 nm, membrane viscosity 0.1 Pa s, 37 °C) depends only logarithmically on the radius of the diffusing protein, whereas the Stokes–Einstein coefficient of a sphere in water falls as 1/a](./plots/frap-recovery.py)

### 13.2.4. Rafts and Caveolae

Even within one leaflet the lipids are not uniformly mixed. Sphingolipids, whose long saturated chains pack well against the flat ring system of cholesterol, associate with it into small, ordered and slightly thicker domains of the outer leaflet.

**Definition 13.2.3 (Lipid Raft)** A **lipid raft** is a small (about 10–200 nm), dynamic domain of the plasma membrane enriched in sphingolipids and cholesterol, in a liquid-ordered state, in which particular proteins are concentrated: GPI-anchored proteins in the outer leaflet and proteins with two saturated acyl chains (doubly palmitoylated, or myristoylated and palmitoylated) in the inner leaflet.

Rafts were first recognized as membrane fractions that resist solubilization by cold nonionic detergents. That method can create domains as well as reveal them, and the size, lifetime and even the existence of rafts in unperturbed cells were long debated; the current view, from super-resolution microscopy and single-molecule tracking, is that they are nanoscale assemblies lasting milliseconds to seconds, which can coalesce into larger platforms when their components are cross-linked by **ligands** or **scaffold proteins**. Proteins with longer transmembrane helices (24–25 residues) partition into the thicker raft bilayer, and those with shorter ones (19–20) are excluded. By bringing receptors and their downstream partners together, rafts raise the probability of their collisions, and depleting membrane cholesterol disrupts some signaling pathways ([7.1.15](/7.1.15)).

Caveolae ("little caves") are flask-shaped invaginations, 50–100 nm across, of raft-like membrane coated on the inside by caveolin, an integral protein that inserts a hairpin into the inner leaflet and carries three palmitoyl groups, and by cavin proteins. **Oligomers** of caveolin bend the bilayer inward. Caveolae take part in signaling and endocytosis, and by flattening under tension they add surface area, protecting cells such as myocytes and endothelial cells from rupture under osmotic or mechanical stress.

### 13.2.5. Curvature, Fusion and Adhesion

Budding, fission and fusion of membranes underlie vesicle traffic, endocytosis and exocytosis, cell division, fertilization and the entry of enveloped viruses, and each begins by bending a bilayer. Curvature can come from lipids (cone-shaped cardiolipin, with four acyl chains and a small head group, concentrates at the strongly curved poles of *E. coli*), from intrinsically curved proteins that bind the surface (the crescent-shaped dimers of BAR domains, whose positively charged concave face binds PIP₂ and PIP₃), and from amphipathic helices that insert like wedges into one leaflet (some BAR proteins, the septins). Fusion of two bilayers must remove the water between them, merge first the two contacting leaflets (hemifusion) and then the other two, and happen only at the right place and time; fusion proteins see to all of this.

**Definition 13.2.4 (SNARE)** **SNAREs** are membrane proteins that drive membrane fusion: a v-SNARE in the vesicle membrane (synaptobrevin at a synapse) and t-SNAREs in the target membrane (syntaxin and SNAP25) zip together, from their membrane-distal ends towards the membranes, into a bundle of four α helices whose formation pulls the two bilayers into contact and fuses them.

At a synapse the zipping is held at an intermediate stage until a rise in $\ce{Ca^2+}$ triggers release of neurotransmitter ([7.1.14](/7.1.14)); after fusion the ATPase NSF disassembles the SNARE complex. Botulinum and tetanus toxins are proteases that cleave specific SNAREs, blocking neurotransmitter release; minute doses of botulinum toxin (Botox) are used to treat muscle spasms and, cosmetically, wrinkles.

Several families of integral proteins attach cells to one another and to the extracellular matrix.

**Definition 13.2.5 (Cell Adhesion Proteins)** **Integrins** are heterodimers of an α and a β subunit, each with one transmembrane helix, that bind proteins of the extracellular matrix (collagen, fibronectin, often at an Arg–Gly–Asp sequence) and carry signals across the membrane in both directions. Cadherins bind identical cadherins on a neighboring cell in a $\ce{Ca^2+}$-dependent homophilic interaction; selectins bind specific glycans on another cell in the presence of $\ce{Ca^2+}$.

Selectins on endothelial cells and leukocytes mediate the rolling of leukocytes along blood vessel walls at sites of inflammation ([7.1.10](/7.1.10)); integrin signaling is taken up in [7.1.15](/7.1.15), the junctions they form in [7.3](/7.3).

## 13.3. The Thermodynamics of Transport

### 13.3.1. Free Energy of Transport

Whether a solute moves spontaneously from one side of a membrane to the other depends on the difference of its electrochemical potential between the two sides. For an uncharged solute only the concentrations matter; for an ion the **membrane potential** ([6.3.13](/6.3.13#sec-13.9.1)) adds an electrical term. In biology the membrane potential is the potential inside relative to outside, $\Delta\varphi = \varphi_{\text{in}} - \varphi_{\text{out}}$; across most plasma membranes it is $-50$ to $-90\,\mathrm{mV}$.

**Formula 13.3.1 (Free Energy of Transport)** The Gibbs energy change for moving one mole of a solute of charge number $z$ from compartment 1 (concentration $c_1$, potential $\varphi_1$) to compartment 2 is

$$
\Delta G_{\mathrm{t}} = \tilde\mu_2 - \tilde\mu_1 = RT\ln\frac{c_2}{c_1} + zF(\varphi_2 - \varphi_1),
$$
with concentrations in place of activities. Transport is spontaneous if $\Delta G_{\mathrm{t}} < 0$, and the solute is at equilibrium across the membrane when $\Delta G_{\mathrm{t}} = 0$, that is, when the potential difference equals the Nernst potential $(RT/zF)\ln(c_1/c_2)$ of that ion ([6.3.13](/6.3.13#sec-13.9.2)).

There is no standard term: transport makes and breaks no bonds, so the "reaction" has $\Delta_{\mathrm{r}}G'^{\circ} = 0$. At $37\,^\circ\mathrm{C}$, $RT = 2.58\,\mathrm{kJ\,mol^{-1}}$, so each tenfold concentration ratio costs $RT\ln 10 = 5.9\,\mathrm{kJ\,mol^{-1}}$ ($5.7$ at $25\,^\circ\mathrm{C}$), and each $10\,\mathrm{mV}$ costs $0.96\,\mathrm{kJ\,mol^{-1}}$ per unit charge.

**Example 13.3.1** The cytosolic concentration of $\ce{Ca^2+}$ is about $0.1\,\mu\mathrm{M}$, the extracellular one about $1\,\mathrm{mM}$, and the membrane potential $-50\,\mathrm{mV}$ (Lehninger's value). Pumping $\ce{Ca^2+}$ out at $37\,^\circ\mathrm{C}$ costs

$$
\Delta G_{\mathrm{t}} = (2.58\,\mathrm{kJ\,mol^{-1}})\ln\frac{10^{-3}}{10^{-7}} + 2\,(96.5\,\mathrm{kJ\,V^{-1}\,mol^{-1}})(0.050\,\mathrm{V}) = 23.7 + 9.6 = 33\,\mathrm{kJ\,mol^{-1}},
$$
since the ion moves from $-50\,\mathrm{mV}$ to $0$ ($\varphi_2 - \varphi_1 = +0.050\,\mathrm{V}$). For $\ce{Na+}$ entering the cell from $145\,\mathrm{mM}$ outside to $12\,\mathrm{mM}$ inside, $\Delta G_{\mathrm{t}} = 2.58\ln(12/145) + 96.5\times(-0.050) = -6.4 - 4.8 = -11.2\,\mathrm{kJ\,mol^{-1}}$: both the concentration gradient and the field draw $\ce{Na+}$ in.

The Gibbs energy of ATP hydrolysis under cellular conditions is about $-50$ to $-60\,\mathrm{kJ\,mol^{-1}}$ ([7.1.16](/7.1.16)), enough to export one $\ce{Ca^2+}$ but not two against these gradients; the SERCA pump (13.5.2) indeed moves two $\ce{Ca^2+}$ per ATP into the ER, where the concentration is lower than outside the cell, and exchanges protons in the opposite direction. Most cells maintain tenfold or larger ion gradients across their membranes, and active transport is a major item in their energy budget.

![Free energy of transport at 37 °C (Formula 13.3.1). A: ΔG_t against the concentration ratio (destination/origin) across a membrane with a potential of −50 mV, for an uncharged solute and for cations moved inward (z = +1) or outward (z = +1, +2); the points are the two cases of Example 13.3.1, and the band is the free energy available from ATP hydrolysis in cells. B: the maximal accumulation ratio of glucose reached by a Na⁺–glucose symporter with perfect coupling (Formula 13.5.1), against the membrane potential, for one and two Na⁺ per glucose ([Na⁺] 145 mM outside, 12 mM inside); the values at −50 and −70 mV are marked](./plots/transport-energetics.py)

### 13.3.2. Why the Bilayer Is a Barrier

To cross the bilayer unaided a polar solute must shed its hydration shell, dissolve in the hydrocarbon core and diffuse about $3\,\mathrm{nm}$ through a medium in which it is poorly soluble. The energy spent in dehydration is recovered on the other side, but the intermediate state is high in Gibbs energy, like a **transition state**, and the **activation energy** of passage is very large. The permeability coefficient $P$ of a solute (flux per unit concentration difference, $J = P\,\Delta c$) is therefore roughly proportional to its partition coefficient between hydrocarbon and water. Gases and small nonpolar molecules ($\ce{O2}$, $\ce{CO2}$, $\ce{N2}$, steroids) cross readily; water, urea and glycerol, small and polar, cross slowly; glucose and amino acids very slowly; and ions practically not at all, with permeability coefficients about ten orders of magnitude below that of water (of the order of $10^{-12}\,\mathrm{cm\,s^{-1}}$ for $\ce{Na+}$ and $\ce{K+}$). At pH 7 tryptophan, a zwitterion, crosses a bilayer about a thousand times more slowly than indole, which has the same ring but no charged groups. Pure lipid bilayers are thus practically impermeable to ions and polar metabolites on the time scale of a cell's life, and every such solute needs a protein to cross.

### 13.3.3. Transporters and Channels

Membrane proteins speed transport in the way enzymes speed reactions: they lower the activation energy by providing an alternative path. A transport protein binds the dehydrated solute with several **weak interactions** whose **binding energy** compensates for the loss of the hydration shell, and offers a polar route through the bilayer.

**Definition 13.3.1 (Transporter and Ion Channel)** A **transporter** (carrier) is a membrane protein that binds its substrate with high stereospecificity and moves it across the membrane by a conformational cycle; its rate is saturable and well below the limit of free diffusion. An **ion channel** is a membrane protein that forms a water-filled transmembrane pore through which ions diffuse, when the channel is open, at rates approaching the diffusion limit; channels are selective for certain ions but not saturable under physiological conditions, and most are gated, opening and closing in response to a signal.

| Property | Transporter | Ion channel |
|---|---|---|
| Mechanism | alternating access: two gates, never open at the same time | one gate; when open, a continuous pore |
| Rate per protein | about $10^2$–$10^4\,\mathrm{s^{-1}}$ (Na⁺/K⁺-ATPase about $10^2$) | $10^7$–$10^8$ ions $\mathrm{s^{-1}}$ |
| Saturation | yes, $V = V_{\max}[\mathrm{S}]/(K_{\mathrm{t}} + [\mathrm{S}])$ | no (within physiological range) |
| Specificity | high, stereospecific | selective for an ion species or charge |
| Energy coupling | can be coupled to ATP or an ion gradient (active transport) | always downhill |
| Typical structure | one long polypeptide with 10–14 transmembrane helices | oligomers of several (often identical) subunits around a central pore |

Transporters are classified by the energy they use and by the number and direction of the solutes they carry.

**Definition 13.3.2 (Passive Transport, Uniport, Symport and Antiport)** **Passive transport** (facilitated diffusion) is transport by a protein down the electrochemical gradient of the solute, without input of energy; active transport moves a solute against its gradient by coupling to another process. A transporter that carries one solute is a **uniporter**; a **cotransporter** carries two solutes simultaneously, in the same direction (a **symporter**) or in opposite directions (an **antiporter**). Transport that moves net charge across the membrane is **electrogenic**; transport that moves none is electroneutral.

This classification is independent of the energetics: a symporter can be passive if both solutes move down their gradients, and it becomes the engine of **secondary active transport** ([6.3.18](/6.3.18#sec-18.2.5)) when one solute's downhill flow drives the other uphill.

![Classes of membrane transport proteins (cytosol below). Passive: a uniporter (GLUT1, glucose), an antiporter (AE1, Cl⁻ in and HCO₃⁻ out, electroneutral) and an ion channel (K⁺). Secondary active: a symporter (SGLT1) in which the entry of 2 Na⁺ down their gradient drives the uptake of glucose against its gradient. Primary active, driven by ATP: a P-type ATPase (Na⁺/K⁺-ATPase: 3 Na⁺ out, 2 K⁺ in, with A, P and N cytoplasmic domains), a rotary V-type ATPase that pumps H⁺ into vacuoles and lysosomes (the F-type ATP synthase has the same architecture) and an ABC transporter, with two transmembrane domains and two ATP-binding domains, exporting a drug](./plots/transporter-classes.py)

## 13.4. Passive Transport

### 13.4.1. The Glucose Transporter GLUT1

Erythrocytes depend entirely on **glycolysis** and take up glucose from the plasma, where its concentration is held at 4.5–5 mM, through the uniporter GLUT1, about 50 000 times faster than glucose could cross the bilayer alone. GLUT1 has 12 transmembrane helices; several of them are amphipathic, with their polar faces lining a hydrophilic path for glucose. Crystal structures of GLUT1 open to the cytosol and of its close relative GLUT3 open to the outside (Deng and colleagues, 2014 and 2015) confirm the mechanism.

**Definition 13.4.1 (Alternating Access)** In the **alternating-access mechanism**, a transporter has a substrate-binding site that is exposed to only one side of the membrane at a time; it alternates between an outward-facing conformation $\mathrm{T_1}$ and an inward-facing conformation $\mathrm{T_2}$, passing through an occluded state in which the bound substrate is accessible from neither side.

For GLUT1 the cycle is: glucose binds $\mathrm{T_1}$ outside; the complex converts to $\mathrm{glucose\cdot T_2}$; glucose is released inside; the empty transporter returns to $\mathrm{T_1}$. Every step is reversible, so GLUT1 can carry glucose in either direction; in the cell, glucose is phosphorylated by hexokinase as soon as it enters ([7.1.18](/7.1.18)), which keeps the internal concentration low and the net flux inward.

**Formula 13.4.1 (Kinetics of a Carrier)** The initial rate of uptake ($[\mathrm{S}]_{\text{in}} = 0$) follows the analogue of the **Michaelis–Menten equation** ([6.3.17](/6.3.17)),

$$
V_0 = \frac{V_{\max}[\mathrm{S}]_{\text{out}}}{K_{\mathrm{t}} + [\mathrm{S}]_{\text{out}}},
$$
where the transport constant $K_{\mathrm{t}}$ is the external concentration at half-maximal rate. For a symmetric carrier (substrate binding at equilibrium on both sides, the same rate constant for reorientation of the empty and the loaded carrier) the net influx in the presence of internal substrate is

$$
J = J_{\max}\frac{K_{\mathrm{t}}\left([\mathrm{S}]_{\text{out}} - [\mathrm{S}]_{\text{in}}\right)}{\left(K_{\mathrm{t}} + [\mathrm{S}]_{\text{out}}\right)\left(K_{\mathrm{t}} + [\mathrm{S}]_{\text{in}}\right)} .
$$

**Proof** Let the total carrier be $E_{\mathrm{t}}$, the reorientation rate constant $k$ for every form, and $K_{\mathrm{t}}$ the dissociation constant on both sides. At steady state as many carriers turn inward as outward, $k(\text{all outward forms}) = k(\text{all inward forms})$, so each set holds $E_{\mathrm{t}}/2$. The loaded fractions are $[\mathrm{S}]/(K_{\mathrm{t}} + [\mathrm{S}])$ on each side, and the net flux is $k$ times the difference of the loaded outward and inward carriers: $J = (kE_{\mathrm{t}}/2)\left[[\mathrm{S}]_{\text{out}}/(K_{\mathrm{t}} + [\mathrm{S}]_{\text{out}}) - [\mathrm{S}]_{\text{in}}/(K_{\mathrm{t}} + [\mathrm{S}]_{\text{in}})\right]$, which gives the formula with $J_{\max} = kE_{\mathrm{t}}/2$; with $[\mathrm{S}]_{\text{in}} = 0$ it reduces to the first equation. $\square$

The net flux vanishes when the concentrations are equal: a passive transporter only equilibrates its substrate, much faster than diffusion would, and cannot accumulate it. GLUT1 shows the three hallmarks of passive transport, a high rate down the gradient, saturability and stereospecificity: its $K_{\mathrm{t}}$ is about 6 mM for D-glucose, 20 mM for D-mannose and 30 mM for D-galactose, which differ from glucose only in the configuration of one carbon, and above 3000 mM for L-glucose. (Compilations give values from about 1.5 to 6 mM for D-glucose depending on the conditions; the table below lists 3 mM.) With $K_{\mathrm{t}}$ close to the blood glucose concentration, GLUT1 works near half saturation, so its rate follows the glucose supply.

![Kinetics of passive transport by GLUT1 (Formula 13.4.1). A: initial uptake rate against the external concentration of four hexoses, with the K_t values of GLUT1 (D-glucose 6 mM, D-mannose 20 mM, D-galactose 30 mM, L-glucose 3000 mM); the dashed line marks blood glucose. B: net influx of a symmetric carrier at [S]_out = 5 mM and K_t = 6 mM against the internal concentration: the flux falls to zero at equal concentrations and reverses beyond, saturating in both directions, whereas diffusion through the bilayer (drawn 1000-fold enlarged) is linear and far slower](./plots/transport-kinetics.py)

The human genome encodes 14 GLUT proteins (SLC2A1–14), with different tissue distributions and kinetics (Lehninger 8e, Table 11-1):

| Transporter | Main tissues | $K_{\mathrm{t}}$ for glucose / mM | Role |
|---|---|---|---|
| GLUT1 | erythrocytes, blood–brain barrier, placenta, most tissues at a low level | about 3 | basal uptake; defective in GLUT1 deficiency (De Vivo disease) |
| GLUT2 | liver, pancreatic β cells, intestine, kidney | about 17 | high $K_{\mathrm{t}}$: flux follows glucose concentration; glucose release from liver, glucose sensing by β cells |
| GLUT3 | neurons, testis | about 1.4 | basal uptake at low glucose; high turnover number |
| GLUT4 | skeletal and heart muscle, adipose tissue | about 5 | translocated to the plasma membrane in response to **insulin** |
| GLUT5 | intestine, testis, kidney | ($K_{\mathrm{M}}$ for fructose about 6) | fructose transport |

Children with GLUT1 deficiency, who cannot supply enough glucose across the blood–brain barrier, have seizures and developmental delay; a ketogenic diet, which provides **ketone bodies** as an alternative fuel for the brain ([7.1.21](/7.1.21)), is the standard treatment. GLUT4 is regulated by location rather than by its kinetics. Between meals about 90% of it is held in intracellular vesicles; insulin triggers, within minutes, the fusion of these vesicles with the plasma membrane and raises glucose uptake into muscle and fat fifteenfold or more ([7.1.15](/7.1.15)), and when insulin falls the transporters are retrieved by endocytosis. In **type 1 diabetes** the lack of insulin leaves GLUT4 inside, and blood glucose stays high after a meal ([7.1.29](/7.1.29)).

### 13.4.2. The Chloride–Bicarbonate Exchanger

A second passive transporter of the erythrocyte serves the transport of $\ce{CO2}$. In respiring tissues $\ce{CO2}$ enters the erythrocyte and is hydrated to $\ce{HCO3-}$ by carbonic anhydrase; the bicarbonate leaves the cell in exchange for $\ce{Cl-}$, travels in the plasma, which can carry far more $\ce{HCO3-}$ than dissolved $\ce{CO2}$, and in the lungs the exchange runs in reverse and $\ce{CO2}$ is exhaled (the chloride shift; the parallel transport of $\ce{CO2}$ bound to hemoglobin is described in [7.1.7](/7.1.7#sec-7.3.7), and the role of bicarbonate as the main blood buffer in [7.1.2](/7.1.2)). The exchanger, anion exchanger 1 (AE1, band 3), is a dimer with 14 transmembrane segments per subunit and raises the rate of $\ce{HCO3-}$ transport more than a millionfold. Its antiport is obligatory, one $\ce{Cl-}$ for each $\ce{HCO3-}$, and electroneutral, so it neither depends on nor changes the membrane potential.

## 13.5. Active Transport

### 13.5.1. Primary and Secondary Active Transport

**Active transport** accumulates a solute above its equilibrium distribution and must be coupled to an exergonic process ([6.3.18](/6.3.18#sec-18.2.5)). *E. coli*, for example, can grow in a medium containing $1\,\mu\mathrm{M}$ phosphate while keeping millimolar phosphate inside. In primary active transport the solute flux is coupled directly to a chemical reaction (ATP hydrolysis, or in other systems the absorption of light or an oxidation, [7.1.23](/7.1.23), [7.1.24](/7.1.24)); in secondary active transport it is coupled to the downhill flow of a second solute, usually $\ce{Na+}$ or $\ce{H+}$, whose gradient was built by primary active transport. Four families of ATP-driven pumps are known.

| Family | Mechanism | Substrates | Examples |
|---|---|---|---|
| P-type ATPases | phosphorylation of an Asp residue in each cycle; inhibited by vanadate | cations; lipids | Na⁺/K⁺-ATPase, SERCA and plasma membrane Ca²⁺ pumps, gastric H⁺/K⁺-ATPase, plant and fungal H⁺-ATPase, Cu²⁺ and Cd²⁺ pumps, flippases |
| V-type ATPases | rotary; ATP hydrolysis in V₁ turns a proton-conducting ring in V₀ | H⁺ | acidification of vacuoles, lysosomes, endosomes, Golgi, secretory vesicles |
| F-type ATPases | rotary, reversible; usually synthesize ATP | H⁺ (Na⁺ in some bacteria) | **ATP synthase** of mitochondria, chloroplasts and bacteria |
| ABC transporters | two nucleotide-binding domains drive alternating access | ions, sugars, amino acids, **peptides**, lipids, drugs | MDR1, CFTR (a channel), ABCA1, bacterial importers |

### 13.5.2. P-Type ATPases

**Definition 13.5.1 (P-Type ATPase)** A **P-type ATPase** is an active transporter, a single polypeptide (sometimes with accessory subunits) with 8 to 10 transmembrane helices and three cytoplasmic domains, that is reversibly phosphorylated on a conserved Asp residue in each transport cycle: the N (nucleotide-binding) domain transfers the γ-phosphoryl group of ATP to the Asp in the P (phosphorylation) domain, and the A (actuator) domain catalyzes the hydrolysis of the aspartyl phosphate. The two phosphorylation states favor two conformations, E1 and E2, whose ion-binding sites face opposite sides of the membrane with different affinities.

The ion-binding sites lie in the middle of the transmembrane region, 4–5 nm from the phosphorylated Asp, so phosphorylation acts at a distance, through the movements of the cytoplasmic domains: it is an allosteric switch of the kind seen in [7.1.9](/7.1.9#sec-9.5.3). Vanadate ($\ce{VO4^3-}$), which mimics the pentacoordinate phosphoryl group of the transition state, inhibits all P-type pumps. The human genome encodes about 36 of them.

The sarcoplasmic and endoplasmic reticulum $\ce{Ca^2+}$-ATPase (SERCA) and the plasma membrane $\ce{Ca^2+}$-ATPase together keep the cytosolic $\ce{Ca^2+}$ concentration below $10^{-7}\,\mathrm{M}$, which makes $\ce{Ca^2+}$ usable as a signal ([7.1.14](/7.1.14)). In the E1 state SERCA binds two $\ce{Ca^2+}$ from the cytosol with high affinity; phosphorylation by ATP (at Asp351) converts it to E2–P, whose sites face the lumen with low affinity, so the $\ce{Ca^2+}$ ions are released into the lumen; hydrolysis of the aspartyl phosphate returns the pump to E1.

**Definition 13.5.2 (Na⁺/K⁺-ATPase)** The **Na⁺/K⁺-ATPase** (sodium pump) of the plasma membrane of animal cells is a P-type ATPase that, for each ATP hydrolyzed, moves three $\ce{Na+}$ out of the cell and two $\ce{K+}$ in, both against their electrochemical gradients.

The pump follows the cycle proposed by Post and Albers: E1·ATP binds three $\ce{Na+}$ from the cytosol; phosphorylation occludes them; the change to E2–P opens the sites to the outside with low affinity for $\ce{Na+}$, which leaves, and high affinity for $\ce{K+}$; binding of two $\ce{K+}$ triggers dephosphorylation and occludes them; ATP binding converts E2 back to E1, and the $\ce{K+}$ ions are released inside. The turnover number is about $100\,\mathrm{s^{-1}}$. Because each cycle moves one net positive charge out, the pump is electrogenic, but it contributes only a few millivolts directly; its main contribution to the resting potential of $-50$ to $-70\,\mathrm{mV}$ is indirect, through the $\ce{K+}$ gradient it maintains and the $\ce{K+}$ channels that dominate the resting permeability ([6.3.13](/6.3.13#sec-13.9.2)). With the concentrations of 13.3.1 and $-70\,\mathrm{mV}$, one cycle stores about $44\,\mathrm{kJ\,mol^{-1}}$ in the two gradients, close to the Gibbs energy of ATP hydrolysis (the example in [6.3.18](/6.3.18#sec-18.2.5)). The pump consumes about a quarter of the energy of a resting human and much more in the kidney and brain; ouabain, which inhibits it specifically, lowers the oxygen consumption of kidney slices by about two-thirds.

![The Post–Albers cycle of the Na⁺/K⁺-ATPase, clockwise from lower left (outside up in each panel). E1·ATP, with its sites open to the cytosol and a high affinity for Na⁺, binds 3 Na⁺; transfer of the phosphoryl group of ATP to the Asp residue (P) occludes them; the conformational change to E2–P opens the sites to the outside with low Na⁺ and high K⁺ affinity, so 3 Na⁺ leave and 2 K⁺ bind; dephosphorylation occludes the K⁺ ions; ATP binding converts E2 back to E1 and releases 2 K⁺ into the cytosol](./plots/na-k-atpase-cycle.py)

Ouabain and digoxin, cardiac glycosides from plants, bind the pump from the outside. In cardiac myocytes, partial inhibition of the pump lets $[\ce{Na+}]_{\text{in}}$ rise; the $\ce{Na+}$–$\ce{Ca^2+}$ exchanger, which uses the $\ce{Na+}$ gradient to export $\ce{Ca^2+}$ (three $\ce{Na+}$ in for one $\ce{Ca^2+}$ out), then removes less $\ce{Ca^2+}$, more $\ce{Ca^2+}$ is stored in the sarcoplasmic reticulum, and each contraction is stronger. Digitalis preparations have been used against heart failure for more than two centuries. Other P-type pumps include the $\ce{H+}$/$\ce{K+}$-ATPase of the parietal cells of the stomach, which acidifies the gastric juice to pH 1–2 and is inhibited by the "proton pump inhibitors" such as omeprazole; the plasma membrane $\ce{H+}$-ATPase of plants and fungi, which sets their membrane potential (as negative as $-200\,\mathrm{mV}$) and drives their secondary transport; pumps that export toxic $\ce{Cu^2+}$ and $\ce{Cd^2+}$ (in humans, defective $\ce{Cu}$ pumps cause Menkes and Wilson diseases); and the flippases of 13.2.2.

### 13.5.3. V-Type and F-Type ATPases

V-type (vacuolar) ATPases acidify intracellular compartments: the vacuoles of plants and fungi to pH 3–6 (the cytosol is near 7.5), and lysosomes (pH 4.5–5), endosomes, the Golgi complex and secretory vesicles in animal cells; the acid lumen activates lysosomal hydrolases and releases ligands from receptors after endocytosis. A V-type ATPase consists of an integral domain $\mathrm{V_o}$, a ring of c subunits that conducts protons, and a peripheral domain $\mathrm{V_1}$ with three catalytic sites, joined by a central rotor and a peripheral stator. ATP hydrolysis in $\mathrm{V_1}$ rotates the rotor and the c ring, which carries protons across the membrane.

**Definition 13.5.3 (F-Type ATPase)** An **F-type ATPase** is a rotary proton pump of the same architecture, with a proton-conducting integral domain $\mathrm{F_o}$ and a peripheral domain $\mathrm{F_1}$ with three catalytic β subunits. It catalyzes the reaction in both directions: ATP hydrolysis drives protons uphill, and, more often, protons flowing down a sufficiently large electrochemical gradient drive ATP synthesis, when the enzyme is called ATP synthase.

The name records its discovery as coupling factors: $\mathrm{F_1}$ was the first factor isolated from mitochondria, and the subscript of $\mathrm{F_o}$ refers to its inhibition by oligomycin. The number of protons per ATP equals the number of c subunits in the ring divided by three, the number of catalytic sites, and so differs between organisms: 8/3 ≈ 2.7 in mammalian mitochondria, 10/3 in yeast and *E. coli*, 14/3 ≈ 4.7 in chloroplasts. The F-type enzyme of *E. coli* pumps protons out when the bacterium grows anaerobically, and archaea have a homologous A-type enzyme. ATP synthesis by this mechanism, the center of **oxidative phosphorylation** and **photophosphorylation**, is the subject of [7.1.23](/7.1.23) and [7.1.24](/7.1.24).

### 13.5.4. ABC Transporters

**Definition 13.5.4 (ABC Transporter)** An **ABC transporter** (ATP-binding cassette transporter) has two transmembrane domains, each usually with six helices, and two cytoplasmic nucleotide-binding domains (NBDs) of conserved sequence, in one polypeptide or in separate subunits. Binding of ATP brings the two NBDs together into a closed dimer, which switches the transmembrane domains between inward- and outward-facing conformations; hydrolysis of ATP separates them again.

The NBDs are a conserved motor that evolution has coupled to transmembrane domains of many different specificities, with a stoichiometry of one or two ATP per substrate molecule. Exporters, the only kind in eukaryotes, bind their substrate from the cytoplasm or the inner leaflet and release it outside; bacterial importers take up nutrients such as maltose or **vitamin** B₁₂ with the help of a binding protein in the periplasm and are probably the evolutionary ancestors of the eukaryotic exporters. The human genome contains 48 ABC transporter **genes**; yeast has about 30, *Drosophila* 56 and *E. coli* about 80, some 2% of its genome.

| Gene | Protein and role | Medical relevance |
|---|---|---|
| ABCA1 | exports cholesterol and phospholipids to **apolipoprotein** A-I (**reverse cholesterol transport**, [7.1.26](/7.1.26)) | Tangier disease |
| ABCA4 | recycles retinal in photoreceptors ([7.1.14](/7.1.14)) | Stargardt macular degeneration |
| ABCB1 | MDR1 (P-glycoprotein): broad specificity drug efflux at the blood–brain barrier and in the placenta | multidrug resistance of tumors |
| ABCB11 | bile salt export pump of hepatocytes | cholestasis |
| ABCC7 | CFTR, a Cl⁻ channel | cystic fibrosis |
| ABCC8 | sulfonylurea receptor, regulatory subunit of the **ATP-sensitive K⁺ channel** of β cells | target of sulfonylurea drugs in **type 2 diabetes** |
| ABCG2 | BCRP, exporter of anticancer drugs and **urate** | drug resistance, **gout** |

MDR1 in tumor cells pumps out drugs such as doxorubicin and vinblastine, and its overexpression is a frequent cause of failed chemotherapy in cancers of the liver, kidney and colon. Pathogens (*Pseudomonas aeruginosa*, *Staphylococcus aureus*, *Candida albicans*, *Plasmodium falciparum*) owe part of their drug resistance to similar transporters.

CFTR (cystic fibrosis transmembrane conductance regulator) is an ABC protein that has become an ion channel. It has the two transmembrane domains and two NBDs of the family and an extra regulatory (R) domain. Phosphorylation of the R domain by **protein kinase A** ([7.1.14](/7.1.14)) permits ATP to bind; when ATP is bound to both NBDs, the channel opens and $\ce{Cl-}$ flows down its electrochemical gradient, and hydrolysis of one ATP closes it. In cystic fibrosis, a recessive disease affecting about 1 in 3000 newborns of European descent, defective CFTR reduces $\ce{Cl-}$ and, with it, water secretion by the epithelia of the airways, intestine, pancreas and sweat glands; the airway mucus becomes thick and sticky, cannot be cleared by cilia, and harbors chronic bacterial infections that destroy the lungs. In about 90% of patients at least one allele carries the deletion of Phe508 (F508del), which causes misfolding and degradation of the protein in the ER ([7.1.6](/7.1.6)); other **mutations**, such as G551D, give a protein that reaches the membrane but opens poorly. Modern drugs act on the protein itself: potentiators (ivacaftor) increase the opening of mutant channels at the surface, and correctors (tezacaftor, elexacaftor) improve the folding of F508del. The triple combination, approved in 2019, restores enough function in most patients to transform the course of the disease; median predicted survival, about 10 years in 1960, now exceeds 50 years.

### 13.5.5. Secondary Active Transport

The $\ce{H+}$ gradient that respiration builds across the plasma membrane of *E. coli* drives the uptake of lactose by lactose permease (LacY), a symporter that carries one $\ce{H+}$ with each lactose ([7.2.11](/7.2.11) describes its gene, *lacY*). LacY belongs to the major facilitator superfamily, transporters with 12 transmembrane helices in two bundles of six that rock against each other around the substrate-binding site, an alternating-access mechanism driven by substrate binding and protonation. If respiration is blocked or the proton gradient is collapsed by an **uncoupler**, LacY still equilibrates lactose across the membrane but can no longer accumulate it; mutants with defective proton-binding residues behave the same way, showing that the protein couples the two fluxes and is not an ATP-driven pump.

In animal cells the main driving force is the $\ce{Na+}$ gradient established by the Na⁺/K⁺-ATPase. The epithelial cells of the small intestine take up glucose from the lumen with the $\ce{Na+}$–glucose symporter SGLT1 in their apical membrane, which carries two $\ce{Na+}$ with each glucose,

$$
2\,\ce{Na+_{out}} + \text{glucose}_{\text{out}} \longrightarrow 2\,\ce{Na+_{in}} + \text{glucose}_{\text{in}},
$$
and pass the glucose on to the blood through the uniporter GLUT2 in the basolateral membrane, where the Na⁺/K⁺-ATPase also pumps the $\ce{Na+}$ out again.

**Formula 13.5.1 (Maximal Accumulation by a Symporter)** If a symporter couples the movement of $n$ $\ce{Na+}$ to one uncharged solute S with perfect efficiency, the solute can be accumulated up to

$$
\ln\left(\frac{[\mathrm{S}]_{\text{in}}}{[\mathrm{S}]_{\text{out}}}\right)_{\max} = n\left[\ln\frac{[\ce{Na+}]_{\text{out}}}{[\ce{Na+}]_{\text{in}}} - \frac{F\Delta\varphi}{RT}\right], \qquad \Delta\varphi = \varphi_{\text{in}} - \varphi_{\text{out}},
$$
the condition that the total $\Delta G_{\mathrm{t}}$ of the coupled transport (Formula 13.3.1) is zero.

**Example 13.5.1** With $[\ce{Na+}]_{\text{out}} = 145\,\mathrm{mM}$, $[\ce{Na+}]_{\text{in}} = 12\,\mathrm{mM}$, $\Delta\varphi = -50\,\mathrm{mV}$ and $37\,^\circ\mathrm{C}$, each entering $\ce{Na+}$ releases $11.2\,\mathrm{kJ\,mol^{-1}}$ (Example 13.3.1), two release $22.4\,\mathrm{kJ\,mol^{-1}}$, and $\ln(\text{ratio}) = 22.4/2.58 = 8.7$: SGLT1 can concentrate glucose up to about 6000-fold. A membrane potential of $-70\,\mathrm{mV}$ raises the limit to about $3\times10^{4}$; a symporter with a single $\ce{Na+}$ would reach only about 80-fold at $-50\,\mathrm{mV}$. The coupling stoichiometry enters as an exponent, which is why transporters that must work against steep gradients couple more ions.

The kidney recovers glucose from the glomerular filtrate in the same way, mostly through SGLT2 in the proximal tubule. Its inhibitors, the gliflozins (dapagliflozin, empagliflozin), lower blood glucose in type 2 diabetes by letting glucose escape into the urine, and have proved to protect the heart and kidneys as well. The oral rehydration solution that has saved millions of lives in cholera contains glucose together with salt, because SGLT1 still works in the intestine of a cholera patient and its uptake of $\ce{Na+}$ and glucose draws water with it ([7.1.14](/7.1.14)).

### 13.5.6. Ionophores

Because ion gradients store the energy of active transport and of respiration, compounds that dissipate them are potent poisons, and those that act selectively on microorganisms are antibiotics.

**Definition 13.5.5 (Ionophore)** An **ionophore** is a small hydrophobic molecule that binds an ion and carries it across a lipid bilayer, or forms a channel through it, allowing the ion to move down its electrochemical gradient.

Valinomycin, a cyclic depsipeptide from *Streptomyces*, wraps a $\ce{K+}$ ion in six inward-facing carbonyl oxygens that replace its hydration shell, while its outward-facing side chains make the complex soluble in the bilayer; it is about $10^4$ times more selective for $\ce{K+}$ than for $\ce{Na+}$ (the basis of $\ce{K+}$-selective electrodes, [6.3.13](/6.3.13#sec-13.9.3)). Monensin exchanges $\ce{Na+}$ for $\ce{H+}$ and is used as an antiparasitic agent in animal feed; gramicidin A forms a channel by dimerizing end to end into a helix that spans the bilayer. Uncouplers of oxidative phosphorylation are protonophores ([7.1.23](/7.1.23)).

## 13.6. Channels

### 13.6.1. Aquaporins

**Definition 13.6.1 (Aquaporin)** **Aquaporins** (AQPs) are integral membrane proteins that form channels for the rapid passage of water, and in some members glycerol or other small neutral solutes, across membranes, while excluding ions, including $\ce{H3O+}$.

Water crosses a lipid bilayer slowly, but cells that must swell or shrink quickly, or move large volumes of water, have many aquaporins: an erythrocyte has about $2\times10^5$ copies of AQP1, which lets it adjust within milliseconds to the changing **osmolarity** of the renal medulla (**osmosis**, [7.1.2](/7.1.2#sec-2.1.6)). AQP1 conducts about $10^9$ water molecules per second per channel, compared with $4\times10^7\,\mathrm{s^{-1}}$ for catalase, among the fastest enzymes, and the activation energy of passage is below $15\,\mathrm{kJ\,mol^{-1}}$, so water moves in a continuous single file in the direction of the osmotic gradient. Each monomer of the tetramer forms its own pore from six transmembrane helices and two half-helices that dip into the membrane from opposite sides and meet in the middle at their conserved Asn–Pro–Ala (NPA) motifs. Two features exclude ions and protons: a narrow aromatic/arginine constriction near the outer end, about 0.28 nm wide, which admits a water molecule but not a hydrated ion; and the positive ends of the half-helix dipoles at the NPA motifs, which orient the central water molecule so that it cannot pass a proton along the hydrogen-bonded chain of waters (the Grotthuss mechanism would otherwise conduct protons as fast as water). Peter Agre, who discovered AQP1, shared the 2003 Nobel Prize in Chemistry with Roderick MacKinnon.

Mammals have 13 aquaporins (AQP0–AQP12), each with a characteristic location; AQP3, 7, 9 and 10, the aquaglyceroporins, also conduct glycerol. *Arabidopsis* has about 35 aquaporin genes. In the collecting duct of the kidney, the **hormone** vasopressin (antidiuretic hormone) acts through **cAMP** to insert AQP2 into the apical membrane, increasing water reabsorption ([7.14](/7.14)); mutations in AQP2 or in the vasopressin receptor cause nephrogenic **diabetes** insipidus, the excretion of large volumes of dilute urine.

### 13.6.2. The K⁺ Channel: Selectivity at the Speed of Diffusion

Ion channels, first studied in neurons and now known in all cells and many intracellular membranes, determine together with the pumps the permeability of a membrane to each ion and thus its potential. Their activity is measured electrically. In patch clamping (Neher and Sakmann, Nobel Prize 1991) a glass micropipette sealed onto a small patch of membrane records the current through one or a few channels while the voltage is held constant: single-channel currents are a few picoamperes and switch abruptly between zero and a fixed value as the channel opens and closes, often within a fraction of a millisecond.

The $\ce{K+}$ channel KcsA of the bacterium *Streptomyces lividans* (structure by MacKinnon and colleagues, 1998) is the prototype of all $\ce{K+}$ channels, including the **voltage-gated channels** of neurons. Four identical subunits, each with two transmembrane helices and a short pore helix, form an inverted cone around the pore. From the cytoplasmic side the pore is a wide, water-filled vestibule in which the ion keeps its hydration shell, stabilized by the negative ends of the four pore-helix dipoles pointing at it; about two-thirds of the way across it narrows into the selectivity filter, formed by the conserved signature sequence Thr–Val–Gly–Tyr–Gly.

**Definition 13.6.2 (Selectivity Filter)** The **selectivity filter** of an ion channel is the narrowest part of its pore, where the ion must shed its hydration shell and is coordinated instead by groups of the protein; in $\ce{K+}$ channels it is a series of four sites, each a cage of eight backbone carbonyl oxygens arranged to match the hydration shell of a $\ce{K+}$ ion.

$\ce{K+}$ (radius $0.133\,\mathrm{nm}$) fits the cages exactly, so the cost of dehydration is repaid by coordination. $\ce{Na+}$ (radius $0.095\,\mathrm{nm}$) is too small to touch all eight oxygens of a rigid cage at once and would pay the larger dehydration cost of a smaller ion without being repaid; the filter therefore passes $\ce{K+}$ about $10^4$ times better than $\ce{Na+}$. Two $\ce{K+}$ ions occupy the filter at a time, in sites 1 and 3 or 2 and 4; the two configurations have nearly the same energy, so the energy profile is flat rather than a series of deep wells, and the mutual repulsion of the ions keeps them moving. High selectivity and high throughput are thus achieved together. (Whether water molecules alternate with the ions in the filter or the ions move in direct contact is still debated.)

**Example 13.6.1** How close is $10^8$ ions per second to the diffusion limit? The rate at which ions diffusing with coefficient $D$ reach a hemispherical capture area of radius $a$ at the mouth of a pore is $2\pi Dac$. With $D = 2\times10^{-9}\,\mathrm{m^2\,s^{-1}}$ for $\ce{K+}$, $a = 0.5\,\mathrm{nm}$ and $c = 150\,\mathrm{mM} = 9.0\times10^{25}\,\mathrm{m^{-3}}$,

$$
2\pi Dac = 2\pi\,(2\times10^{-9})(5\times10^{-10})(9.0\times10^{25})\,\mathrm{s^{-1}} \approx 6\times10^{8}\,\mathrm{s^{-1}},
$$
the same order as the measured flux; equivalently, a single-channel current of $16\,\mathrm{pA}$ ($10^8$ elementary charges per second) is near the largest observed. Ion passage through the open channel is thus nearly a **diffusion-controlled reaction** ([6.3.17](/6.3.17#sec-17.1.3)), like catalysis by the most efficient enzymes ([7.1.9](/7.1.9)).

Like most channels, $\ce{K+}$ channels are gated: ligand-gated channels open when a molecule binds, voltage-gated channels when the membrane potential moves a charged domain of the protein. How channels are gated and how they make electrical signals is the subject of [7.1.14](/7.1.14), and how their currents produce the action potential of [7.16](/7.16).

## Summary

| Structural feature | Chemical or physical property | Biological function |
|---|---|---|
| Amphipathic lipids with two chains (Definition 13.1.1) | **hydrophobic effect**; cylindrical shape favors bilayers over micelles | self-sealing barrier, 3 nm core, 5–8 nm with proteins |
| Lipid composition per membrane and leaflet | PC and sphingomyelin outside, PS/PE/PI inside; translocators (Definition 13.2.1) | asymmetry; PS exposure signals apoptosis and coagulation |
| Integral, peripheral, amphitropic proteins (Definition 13.1.2) | hydrophobic transmembrane helices (~20 residues) or β barrels; electrostatic binding; lipid anchors | topology predictable by hydropathy plots (Definition 13.1.3), aromatic belts, positive-inside rule |
| Fluid bilayer | gel / liquid-disordered / liquid-ordered (cholesterol) states; homeoviscous adaptation | lateral diffusion $D \sim 1\,\mu\mathrm{m^2\,s^{-1}}$ (FRAP, Formula 13.2.1); weak size dependence (Formula 13.2.2); corrals |
| Sphingolipid–cholesterol domains (Definition 13.2.3) | liquid-ordered nanodomains; caveolin bends the membrane | rafts concentrate signaling proteins; caveolae buffer membrane tension |
| SNAREs (Definition 13.2.4), BAR domains | four-helix bundle zips membranes together | vesicle fusion, neurotransmitter release |
| Electrochemical potential | $\Delta G_{\mathrm{t}} = RT\ln(c_2/c_1) + zF\Delta\varphi$ (Formula 13.3.1) | direction and cost of every transport process |
| Transporters vs channels (Definition 13.3.1) | alternating access (Definition 13.4.1), saturable, $10^2$–$10^4\,\mathrm{s^{-1}}$; pores, $10^7$–$10^8\,\mathrm{s^{-1}}$ | uniport, symport, antiport (Definition 13.3.2) |
| GLUT1, AE1 | $V_0 = V_{\max}[\mathrm{S}]/(K_{\mathrm{t}} + [\mathrm{S}])$ (Formula 13.4.1), stereospecific; electroneutral exchange | glucose supply; insulin-regulated GLUT4; CO₂ transport |
| P-type ATPases (Definitions 13.5.1, 13.5.2) | Asp phosphorylation switches E1/E2 | Na⁺/K⁺ gradients (3 Na⁺ out, 2 K⁺ in), Ca²⁺ removal; ouabain, digoxin, omeprazole |
| V- and F-type ATPases (Definition 13.5.3) | rotary; F-type reversible | acidification of organelles; ATP synthesis |
| ABC transporters (Definition 13.5.4) | two NBDs as an ATP-driven motor | drug efflux (MDR1); CFTR as a Cl⁻ channel (cystic fibrosis) |
| Cotransporters | coupling of downhill Na⁺ or H⁺ flow (Formula 13.5.1) | intestinal glucose uptake (SGLT1), LacY; gliflozins |
| Ionophores (Definition 13.5.5), aquaporins (Definition 13.6.1), K⁺ channel (Definition 13.6.2) | carriers or pores; NPA and ar/R filters; carbonyl cages | gradient collapse (antibiotics); water flux 10⁹ s⁻¹; K⁺ selectivity 10⁴ at near-diffusion rate (Example 13.6.1) |

| Quantity | Value |
|---|---|
| Hydrocarbon core of the bilayer | about 3 nm |
| Residues per transmembrane **α helix** / **β strand** | about 20 / 7–9 |
| $D$ of lipids / of proteins in cells | 0.1–1 / 0.01–0.1 µm² s⁻¹ |
| $RT\ln10$ at 37 °C; $F\times10\,\mathrm{mV}$ | 5.9 kJ mol⁻¹; 0.96 kJ mol⁻¹ |
| Cytosolic / extracellular [Ca²⁺] | about 0.1 µM / 1–2 mM |
| Na⁺ in / out; K⁺ in / out (mammalian cell) | 12 / 145 mM; 140 / 4 mM |
| GLUT1 $K_{\mathrm{t}}$ (D-glucose) | 1.5–6 mM |
| Na⁺/K⁺-ATPase turnover; share of resting energy use | about 100 s⁻¹; about 25% |
| H⁺ per ATP of F-type ATPases | c-ring size / 3 (2.7 in mammalian mitochondria) |
| Maximal glucose accumulation by SGLT1 (−50 mV) | about 6000-fold |
| Water flux through AQP1; K⁺ flux through a K⁺ channel | about 10⁹ s⁻¹; about 10⁸ s⁻¹ |

## Questions

1. The cross-sectional area of a phosphatidylcholine molecule in a bilayer is about $0.7\,\mathrm{nm^2}$. *E. coli* is roughly a cylinder $1\,\mu\mathrm{m}$ in diameter and $2\,\mu\mathrm{m}$ long. About how many lipid molecules form its inner (plasma) membrane, ignoring proteins? If the cell makes 10 000 copies of the lactose transporter, each about 6 nm across, what fraction of the membrane do they occupy?

   **Answer** The area is $\pi dL + 2\pi(d/2)^2 = \pi(1)(2) + \pi/2 \approx 7.85\,\mu\mathrm{m^2} = 7.85\times10^6\,\mathrm{nm^2}$. A bilayer has two leaflets, so the number of lipids is $2\times7.85\times10^6/0.7 \approx 2.2\times10^7$. Each transporter covers about $\pi(3\,\mathrm{nm})^2 \approx 28\,\mathrm{nm^2}$; 10 000 copies cover $2.8\times10^5\,\mathrm{nm^2}$, about 3.6% of the surface. (In reality proteins occupy a large part of the area of a bacterial plasma membrane, which is about 75% protein by mass.)

2. An erythrocyte membrane protein X is released by concentrated salt. Proteases applied to intact cells do not cleave X, but proteases applied to broken membranes do. Where is X, and what kind of membrane protein is it?

   **Answer** Release by salt shows that X is held by electrostatic interactions: it is a peripheral protein. Its resistance to proteases outside intact cells and its sensitivity once the membrane is opened show that it is on the cytoplasmic face. (Spectrin and ankyrin of the erythrocyte cytoskeleton behave like this.)

3. Calculate the Gibbs energy needed to pump one mole of $\ce{H+}$ from blood plasma (pH 7.4) into the gastric juice (pH 1.5) at $37\,^\circ\mathrm{C}$, ignoring the membrane potential. How many protons could one ATP move if $\Delta G$ of ATP hydrolysis in the cell is $-58\,\mathrm{kJ\,mol^{-1}}$? The gastric $\ce{H+}$/$\ce{K+}$-ATPase in fact exchanges one $\ce{H+}$ for one $\ce{K+}$ per ATP at this gradient. Why is this compatible with thermodynamics?

   **Answer** $\Delta G_{\mathrm{t}} = RT\ln(10^{-1.5}/10^{-7.4}) = 2.58\times5.9\times\ln10 = 2.58\times13.6 = 35\,\mathrm{kJ\,mol^{-1}}$. One ATP ($58\,\mathrm{kJ}$) could in principle move at most $58/35 \approx 1.6$ protons, so one $\ce{H+}$ per ATP leaves a margin; the exchanged $\ce{K+}$ moves outward from the cell to the lumen and back through channels, so the overall process is electroneutral and only the $\ce{H+}$ gradient must be paid for. At the steepest gradient the pump approaches thermodynamic equilibrium and slows, which limits the gastric pH to about 1.

4. A cell takes up glucose ten times faster at 5 mM than at 0.2 mM, and uptake requires external $\ce{Na+}$. In another cell type, uptake requires no $\ce{Na+}$ and is unaffected by cyanide. Classify both transporters, and predict the effect of ouabain in each case.

   **Answer** The first is a $\ce{Na+}$–glucose symporter (secondary active transport): it is saturable ($K_{\mathrm{t}}$ of the order of millimolar, since a 25-fold increase in concentration gives only a tenfold increase in rate) and depends on the $\ce{Na+}$ gradient. Ouabain inhibits the Na⁺/K⁺-ATPase, so the $\ce{Na+}$ gradient runs down and glucose uptake against a gradient stops (slowly, as the gradient decays). The second is a passive uniporter (a GLUT); it needs no energy, and ouabain has no direct effect on it.

5. Valinomycin is added to a suspension of *Paramecium*, whose resting potential is $-50\,\mathrm{mV}$ and whose cytosol contains much more $\ce{K+}$ than the medium. Predict the effect on the membrane potential. Why does valinomycin kill bacteria?

   **Answer** Valinomycin makes the membrane highly permeable to $\ce{K+}$, so the potential moves towards the $\ce{K+}$ equilibrium (Nernst) potential, $(RT/F)\ln([\ce{K+}]_{\text{out}}/[\ce{K+}]_{\text{in}})$; with low external $\ce{K+}$ this is more negative than $-50\,\mathrm{mV}$, so the membrane hyperpolarizes. In bacteria valinomycin collapses the electrical part of the proton-motive force and, with it, secondary active transport and ATP synthesis that depend on it.

6. A symporter accumulates an uncharged solute 25-fold while the $\ce{Na+}$ concentration outside is only ten times that inside. Does this violate the second law? Give two explanations consistent with thermodynamics.

   **Answer** No. With one $\ce{Na+}$ per solute and no membrane potential the limit would be tenfold, but (1) the membrane potential, inside negative, adds $-F\Delta\varphi/RT$ to the driving force of each $\ce{Na+}$: at $-50\,\mathrm{mV}$ the limit for one $\ce{Na+}$ is $10\times\mathrm{e}^{1.87} \approx 65$-fold (Formula 13.5.1); and (2) the transporter may couple two or more $\ce{Na+}$ per solute, which squares the ratio (100-fold without any potential).

7. Why do $\ce{K+}$ channels conduct $\ce{K+}$ $10^4$ times better than $\ce{Na+}$, although $\ce{Na+}$ is the smaller ion? Why do water channels exclude protons, which move faster than any other ion through bulk water?

   **Answer** In the selectivity filter each ion must give up its hydration shell. The carbonyl cages are sized for $\ce{K+}$, so the energy of coordination by eight oxygens compensates the dehydration energy of $\ce{K+}$; $\ce{Na+}$, more strongly hydrated and too small to be coordinated by all the oxygens, would not be compensated and faces a high barrier (Definition 13.6.2). In aquaporins protons would move by hopping along the single file of water molecules (Grotthuss mechanism); the positive ends of the two half-helix dipoles at the NPA motifs orient the central water so that the hydrogen-bonded chain is broken, and the aromatic/arginine constriction repels cations, so water passes but $\ce{H+}$ does not, and the membrane's proton gradients are preserved.

8. (Open question) Using Formula 13.2.1, design a FRAP experiment to decide whether a receptor in the plasma membrane is held by the cytoskeleton. What would you vary, and what results would distinguish free diffusion, binding to immobile structures and confinement in corrals?

   **Answer** Outline: label the receptor (for example with a GFP fusion or a fluorescent Fab fragment), bleach spots of two or more radii, and fit $D$ and the mobile fraction $M_{\mathrm{f}}$. Free diffusion gives $M_{\mathrm{f}} \approx 1$ and $\tau_D \propto w^2$ with the same $D$ for all spots. Binding to immobile structures lowers $M_{\mathrm{f}}$ and, if binding is transient, adds a slow recovery phase whose rate is the dissociation rate constant and is independent of spot size. Confinement in corrals smaller than the spot makes the apparent $D$ depend on the spot size (low for large spots); single-particle tracking resolves the corrals directly. Repeating the experiment after disrupting actin (latrunculin) or depleting cholesterol (methyl-β-cyclodextrin) shows which structure is responsible.
