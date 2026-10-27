---
title: Mitochondria and Chloroplasts as Organelles
description: Mitochondria and plastids as organelles rather than energy machines (the chemiosmotic mechanism is in 7.1.23–7.1.25); mitochondrial membranes, cristae, MICOS and ATP synthase dimers, numbers and functions; fusion, fission, transport and a graph model of the network with a percolation threshold; contacts with the ER and other organelles; biogenesis of a semiautonomous organelle, mitochondrial DNA, its genetic code, maternal inheritance and a sampling model of the heteroplasmy bottleneck; layered quality control; plastid types, interconversion, division, chloroplast genome and retrograde signaling; endosymbiotic origin, gene transfer to the nucleus, why organelles keep genomes, and secondary endosymbiosis.
---

Mitochondria and chloroplasts convert energy, and how they do it, by **chemiosmotic coupling** through the **respiratory chain**, photosynthetic electron transport and **ATP synthase**, was the subject of [7.1.23](/7.1.23)–[7.1.25](/7.1.25). This chapter treats them as **organelles**: how their membranes are built and shaped, how they grow, divide, fuse and move, how they exchange lipids and ions with the ER, how a cell maintains a second genome inside them and passes it to the next generation, how damaged organelles are recognized and removed, and how they arose from bacteria. These questions connect the energy machines to the rest of the cell. Mitochondrial dynamics determines where ATP is made in a neuron; contacts with the ER supply lipids and buffer $\ce{Ca^2+}$ signals; the mitochondrial genome, with its own **genetic code**, makes maternally inherited diseases possible; and mitochondria control **apoptosis** ([7.3.25](/7.3.25)). Protein import into both organelles, which depends on **sorting signals** and translocases, was described with the other routes of **protein sorting** in [7.3.6](/7.3.6); **mitophagy**, the final step of quality control, in [7.3.11](/7.3.11#sec-11.7.2). Three quantitative models recur: the percolation of the mitochondrial network as a function of the balance of fusion and fission, the random sampling of mitochondrial genomes through the germline bottleneck, and, from the previous chapter, the **PINK1** switch.

## 12.1. Energy Conversion in Brief

The two organelles share one design, which the table summarizes with links to the detailed treatment.

| Feature | Mitochondrion | Chloroplast |
|---|---|---|
| Energy source | oxidation of **NADH** and $\ce{FADH2}$ from fuels ([7.1.20](/7.1.20), [7.1.21](/7.1.21)) | light absorbed by **chlorophyll** ([7.1.24](/7.1.24#sec-24.2.2)) |
| Electron flow | NADH → Complexes I, III, IV → $\ce{O2}$ ([7.1.23](/7.1.23#sec-23.1.8)) | $\ce{H2O}$ → **photosystem II** → $b_6f$ → **photosystem I** → $\ce{NADP+}$ |
| Coupling membrane | inner membrane (cristae) | thylakoid membrane |
| Proton gradient | matrix (N) → intermembrane and crista space (P); mostly $\Delta\psi$ | stroma (N) → thylakoid lumen (P); mostly $\Delta\mathrm{pH}$ |
| **ATP synthase** | $\mathrm{F_1}$ in the matrix; **proton-motive force** ([7.1.23](/7.1.23#sec-23.2.2)) | $\mathrm{CF_1}$ in the stroma ([7.1.24](/7.1.24)) |
| Main products | ATP for the cell, $\ce{CO2}$, water | ATP and **NADPH** for **carbon fixation** ([7.1.25](/7.1.25)), $\ce{O2}$ |

Both are enclosed by two membranes, both have their own DNA and **ribosomes**, both import most of their proteins from the cytosol, and both arose from bacteria (12.8). The rest of the chapter starts from these shared features.

## 12.2. Mitochondrial Architecture

### 12.2.1. Membranes and Compartments

Mitochondria were seen in the light microscope long before their function was known. Richard Altmann (1890) described them as "bioblasts", granules he believed to be elementary organisms; Carl Benda (1898) named them mitochondria (from the Greek words for "thread" and "granule") after their appearance in spermatocytes; and Leonor Michaelis (1900) showed that they are stained in living cells by the redox dye Janus green B, which they keep in its oxidized, colored form, the first hint of their oxidative activity. After Hogeboom, Schneider and Palade (1948) isolated intact mitochondria by centrifugation in sucrose, Eugene Kennedy and Albert Lehninger (1949) showed that the isolated organelles carry out the **citric acid cycle**, **fatty acid** oxidation and **oxidative phosphorylation**, and Palade and Sjöstrand described the cristae by electron microscopy in the early 1950s. A typical mitochondrion is 0.5–1 µm wide and 1 to several micrometers long; under some conditions, for example in hepatocytes in alcoholic liver disease, giant mitochondria (megamitochondria) of up to about 10 µm form.

**Definition 12.2.1 (Mitochondrion and Its Compartments)** A **mitochondrion** is a double-membrane organelle of eukaryotic cells that carries out oxidative phosphorylation, the citric acid cycle and fatty acid oxidation, among other functions, and contains its own genome. Its **outer membrane** is permeable to molecules up to about 5 kDa through porins (VDAC); the narrow space between it and the inner membrane, continuous with the lumen of the cristae, is the **intermembrane space**, whose small-molecule composition resembles that of the cytosol; the **inner membrane**, impermeable to ions and most metabolites except through specific carriers, encloses the **mitochondrial matrix**, which contains the enzymes of the citric acid cycle and β oxidation, the mitochondrial DNA and the mitoribosomes.

The inner membrane is itself divided. The inner boundary membrane runs parallel to the outer membrane, 20–30 nm from it, and carries the import machinery (TOM–TIM contacts, [7.3.6](/7.3.6)). The cristae protrude into the matrix as lamellae or tubes about 20 nm wide, and their membranes carry the respiratory complexes and ATP synthase. The inner membrane is one of the most protein-rich membranes of the cell (about 75% protein by mass) and contains cardiolipin, a phospholipid with two phosphates and four acyl chains made only in mitochondria, which binds the respiratory complexes and supports curvature. The matrix is extremely crowded, with protein at more than $500\,\mathrm{mg\,mL^{-1}}$, close to the concentration in a protein crystal.

The four compartments were separated in the 1960s by swelling mitochondria osmotically and treating them with digitonin, which strips the cholesterol-containing outer membrane first, and each was identified by a **marker enzyme** (Schnaitman and Greenawalt, 1968):

| Compartment | Marker enzyme | Other characteristic components |
|---|---|---|
| Outer membrane | monoamine oxidase | porins (VDAC), TOM and **SAM complexes**, long-chain acyl-CoA synthetase, Mfn1/2, Drp1 receptors; lipid composition close to that of the ER, with some **cholesterol** |
| Intermembrane space | **adenylate kinase** | **cytochrome** c, creatine kinase (mitochondrial isoform), small TIM **chaperones**, Mia40 |
| Inner membrane | **cytochrome c oxidase** (also succinate dehydrogenase) | respiratory complexes, ATP synthase, ADP/ATP translocase and other carriers, TIM complexes, OXA1; about 15–20 % cardiolipin, almost no cholesterol, a composition resembling that of a bacterial plasma membrane |
| Matrix | malate dehydrogenase (also citrate synthase) | enzymes of the citric acid cycle, pyruvate dehydrogenase and **β oxidation**, mtDNA and mitoribosomes, dense granules of calcium phosphate |

**Definition 12.2.2 (Crista, Crista Junction and MICOS)** A **crista** is an invagination of the mitochondrial inner membrane into the matrix that enlarges its area and concentrates the respiratory chain and ATP synthase. Each crista is connected to the inner boundary membrane by a narrow tubular or slot-like **crista junction**, 12–40 nm wide, held by **MICOS** (mitochondrial contact site and cristae organizing system), a multi-subunit inner membrane complex built around Mic60 (mitofilin) and Mic10 that stabilizes the curvature of the junction and binds the SAM complex of the outer membrane.

![Architecture and dynamics of mitochondria (schematic, not to scale). A: section through a mitochondrion: the outer membrane; the intermembrane space; the inner boundary membrane, parallel to the outer membrane; lamellar cristae joined to the boundary membrane by narrow crista junctions held by MICOS (red dots); rows of ATP synthase dimers (pink heads in the matrix) at the curved rims of the cristae and respiratory complexes (teal) on their flat faces; the crista lumen; the matrix with nucleoids of mtDNA (blue loops) and mitoribosomes; TOM and TIM import complexes at a contact between the two membranes; and an ER tubule at a membrane contact site, where tethering complexes (ERMES in yeast) exchange lipids and Ca²⁺. B: fusion: outer membranes are tethered and fused by mitofusins (Mfn1/2), then the inner membranes by OPA1. C: fission: an ER tubule wraps the mitochondrion and preconstricts it, and Drp1, recruited by receptors of the outer membrane (Mff, MiD49/51), forms a ring that constricts it until it divides](./plots/mito-structure.py)

### 12.2.2. Shaping the Cristae

Cristae are not passive folds; three molecular systems give them their shape:

- ATP synthase dimers. Mitochondrial ATP synthase, unlike the bacterial and chloroplast enzymes, forms dimers in which the two membrane domains meet at an angle of about 86° (in mammals), and the dimers line up in rows along the rims of the cristae, bending the membrane. Yeast mutants lacking the dimer-specific subunits e and g have monomeric synthase and no proper cristae; their respiration falls by half and they grow slowly. **Cryo-electron tomography** shows the respiratory complexes on the flat faces on either side of the rows, so protons pumped into the narrow crista lumen reach the synthases at the rims quickly.
- MICOS at the junctions (Definition 12.2.2). Loss of Mic60 detaches the cristae from the boundary membrane, which then form concentric onion-like stacks.
- OPA1, the inner membrane fusion protein (12.3.1), whose **oligomers** also tighten the crista junctions. During **apoptosis** the junctions widen as OPA1 oligomers are disrupted, which releases cytochrome c stored in the crista lumen (about 85% of the total) into the intermembrane space and, after permeabilization of the outer membrane, into the cytosol ([7.1.23](/7.1.23#sec-23.5.3), [7.3.25](/7.3.25)).

Because the junctions are narrow, the crista lumen is partly separated from the rest of the intermembrane space, and individual cristae within one mitochondrion can have different membrane potentials. The area gained is large: in heart muscle the cristae have about 20 times the area of the plasma membrane, and the total area of inner mitochondrial membrane in a human body has been estimated at the size of a football field. Highly active tissues (heart, flight muscle of insects, brown fat) have densely packed lamellar cristae; steroid-producing cells have tubular cristae.

### 12.2.3. Number, Distribution and Functions

Mitochondria occupy up to a fifth of the cytoplasmic volume of a hepatocyte (about 1000–2000 per cell) and about a third of a cardiomyocyte's; a mature human oocyte contains some $10^5$ of them and a sperm about 50–75, wrapped around the base of the flagellum; mature red blood cells have none. Their position follows the demand for ATP and $\ce{Ca^2+}$ buffering: between the myofibrils of muscle, along axons and at synapses of neurons, beneath the basolateral membrane of kidney tubule cells, where the $\ce{Na+}/\ce{K+}$-ATPase consumes ATP. Mitochondria are often drawn as isolated beans, but in many cells they form a branched reticulum that is continuously remodeled (12.3).

ATP synthesis is only one of their jobs:

| Function | Mitochondrial contribution | Where treated |
|---|---|---|
| ATP synthesis | oxidative phosphorylation | [7.1.23](/7.1.23) |
| Biosynthetic precursors | citric acid cycle intermediates (citrate for lipids, oxaloacetate and α-ketoglutarate for amino acids), one-carbon units for nucleotides | [7.1.20](/7.1.20) |
| **Cofactors** | iron–sulfur clusters, the first and last steps of **heme** synthesis | [7.1.27](/7.1.27) |
| Nitrogen | two steps of the **urea cycle** (liver) | [7.1.22](/7.1.22) |
| Lipids | cardiolipin, phosphatidylethanolamine, phosphatidylglycerol; **steroid hormones** (side-chain cleavage by **cytochrome P-450** in the matrix) | 12.4, [7.1.26](/7.1.26) |
| Heat | **uncoupling protein 1** in brown fat | [7.1.23](/7.1.23#sec-23.5.1) |
| Signaling | $\ce{Ca^2+}$ uptake and release, **reactive oxygen species**, release of metabolites that modify **chromatin** (acetyl-CoA, α-ketoglutarate) | 12.4, [7.3.18](/7.3.18) |
| Cell death | cytochrome c and other proteins released in apoptosis | [7.3.25](/7.3.25) |
| Innate immunity | MAVS on the outer membrane signals viral RNA; released mtDNA activates cGAS–STING | 7.15 |

For cells that can make enough ATP by **glycolysis**, the synthesis of iron–sulfur clusters is probably the mitochondrial function they cannot do without: some anaerobic protists have lost oxidative phosphorylation and keep reduced mitochondria (hydrogenosomes, mitosomes) mainly for this purpose, and the one known eukaryote without any mitochondrion, the oxymonad *Monocercomonoides*, acquired a bacterial pathway for iron–sulfur clusters in the cytosol.

## 12.3. Mitochondrial Dynamics

### 12.3.1. Fusion

**Definition 12.3.1 (Mitochondrial Fusion, Mitofusin and OPA1)** **Mitochondrial fusion** is the merging of two mitochondria into one, in two coordinated steps that preserve the separation of the compartments: fusion of the outer membranes by the **mitofusins** Mfn1 and Mfn2, dynamin-related GTPases of the outer membrane that tether the two organelles by dimerizing in trans and fuse them when they hydrolyze GTP; and fusion of the inner membranes by **OPA1**, a dynamin-related GTPase of the inner membrane that acts with cardiolipin on the opposing membrane and requires the membrane potential.

The first fusion protein was found in flies. During *Drosophila* spermatogenesis, the mitochondria of each spermatid fuse into a giant two-part structure, the Nebenkern, which in cross-section looks like an onion; Hales and Fuller (1997) found that the gene mutated in male-sterile *fuzzy onions* (*fzo*) mutants, in which the Nebenkern does not form, encodes an outer membrane GTPase, the founding mitofusin. Mammalian OPA1 exists in long forms anchored in the inner membrane and short soluble forms made by two proteases: YME1L cleaves constitutively, while OMA1 is activated by stress and loss of membrane potential and converts all OPA1 to the short form, which stops inner membrane fusion. A damaged mitochondrion is thus prevented from fusing back into the network.

### 12.3.2. Fission

**Definition 12.3.2 (Mitochondrial Fission and Drp1)** **Mitochondrial fission** is the division of a mitochondrion, in which both membranes are constricted and cut together from the outside. Its central component is **Drp1** (dynamin-related protein 1; Dnm1 in yeast), a cytosolic GTPase that is recruited to the outer membrane by receptors (Mff, Fis1, MiD49 and MiD51), assembles into rings or spirals around the organelle and constricts it as it hydrolyzes GTP.

Fission sites are chosen by other organelles. Friedman, Voeltz and colleagues (2011) showed that most fission events in yeast and mammalian cells occur where an ER tubule crosses and wraps the mitochondrion: the ER, with **actin filaments** polymerized by the ER-bound **formin** INF2 and **myosin II**, preconstricts the tubule to a diameter of about 150 nm, below what a free mitochondrion has and close to the diameter of a Drp1 ring. Nucleoids that are replicating their mtDNA sit at such contacts, which links genome replication to division, so that both daughters receive DNA; and contacts with **lysosomes**, at which the lysosomal Rab7 hydrolyzes its GTP, also mark sites of fission. A second **dynamin** (dynamin 2) may complete scission, although this is debated. Inside the mitochondrion, the inner membrane must divide at the same place; how it does so in mammals is not fully known.

### 12.3.3. Transport and Positioning

Mitochondria move along **microtubules** on kinesin-1 (toward plus ends, out to axon terminals) and dynein (back toward the cell body) through an adaptor complex of the outer membrane GTPase Miro and the protein Milton (TRAK1/2 in mammals); in plants and yeast they move on actin. Miro has $\ce{Ca^2+}$-binding EF hands: where cytosolic $\ce{Ca^2+}$ is high, as at active synapses, $\ce{Ca^2+}$ binding detaches the motor and the mitochondrion stops (Wang and Schwarz, 2009), so mitochondria accumulate where ATP and $\ce{Ca^2+}$ buffering are needed. Anchoring proteins such as syntaphilin hold most axonal mitochondria still; in mature axons only about 20–30% are moving at any moment.

### 12.3.4. Why Fuse and Divide?

The continuous cycle of fusion and fission, each mitochondrion fusing every few minutes to an hour, serves several purposes:

1. Complementation. Fusion mixes matrix contents, including mtDNA and its products, so that a mitochondrion carrying a mutant genome can borrow proteins made from a wild-type genome. Cells lacking both mitofusins lose mtDNA and respiratory capacity, and in mice the muscle-specific loss of Mfn1 and Mfn2 depletes muscle mtDNA and leads to the accumulation of mtDNA mutations.
2. Distribution. Fission produces units small enough to be carried into axons and dendrites, and to be partitioned between daughter cells at mitosis, when Drp1 is activated by phosphorylation by Cdk1 (cyclin B).
3. Quality control. Fission often produces daughters with unequal membrane potentials; the depolarized daughter is less likely to fuse again (its OPA1 is cleaved) and is removed by mitophagy (Twig and colleagues, 2008). Fission thus segregates damage that fusion has diluted.
4. Metabolic adaptation. In starvation, mitochondria elongate (fission is inhibited by phosphorylation of Drp1 by **protein kinase A**), which increases the density of cristae and protects them from autophagy; in proliferating cells, especially cancer cells with high glycolysis, they tend to fragment.

Defects in the machinery cause neurological disease, because neurons depend on transport and quality control over long distances: mutations in *MFN2* cause Charcot–Marie–Tooth disease type 2A, an axonal neuropathy of the longest peripheral nerves; mutations in *OPA1* cause dominant optic atrophy, a degeneration of retinal ganglion cells and the optic nerve; and a dominant-negative mutation in *DNM1L* (Drp1) was found in a newborn with fatal encephalopathy, with elongated mitochondria and peroxisomes (Drp1 also divides peroxisomes).

### 12.3.5. A Network Model

The steady-state shape of the network can be understood as a balance between rates. Sukhorukov and colleagues (2012) described the chondriome of a yeast cell as a graph whose edges are mitochondrial tubules and whose nodes are free tips (degree 1), tip-to-tip fusion points (degree 2) and three-way junctions (degree 3), which form when a tip fuses with the side of a tubule.

**Formula 12.3.1 (Fusion–Fission Graph Model)** Let $X_1$, $X_2$, $X_3$ be the numbers of nodes of degree 1, 2 and 3. Tip-to-tip fusion and tip-to-side fusion and their reverse fissions,
$$
X_1 + X_1 \underset{b_1}{\overset{a_1}{\rightleftharpoons}} X_2, \qquad X_1 + X_2 \underset{b_2}{\overset{a_2}{\rightleftharpoons}} X_3, \tag{12.1}
$$
conserve the number of tubule ends $M = X_1 + 2X_2 + 3X_3$. At steady state (the **law of mass action**), with $x_k = X_k/M$ and the same ratio $\kappa = a_1 M/b_1 = a_2 M/b_2$ for both reactions,
$$
x_2 = \kappa x_1^2, \qquad x_3 = \kappa^2 x_1^3, \qquad x_1 + 2\kappa x_1^2 + 3\kappa^2 x_1^3 = 1. \tag{12.2}
$$
If the tubules are otherwise connected at random, the network contains a giant connected component when $\sum_k k(k-2)\,x_k > 0$ (the Molloy–Reed criterion for random graphs), that is, when
$$
3x_3 > x_1, \qquad \kappa > \kappa_{\mathrm{c}} = \frac{2}{\sqrt 3} + \frac{2}{3} \approx 1.82. \tag{12.3}
$$

The model reproduces the main observation: as the balance shifts toward fusion, the network does not grow gradually but undergoes a percolation transition, from many fragments to a single interconnected reticulum containing most of the mitochondrial mass (figure). Degree-2 nodes, which merely join tubules end to end, do not affect the threshold; only branching does. Near the threshold, small changes in fusion or fission rates change the structure greatly and cluster sizes fluctuate widely, which is what is seen in yeast and mammalian cells: networks in many cell types appear to operate close to the transition, where they can switch rapidly between connected and fragmented states, for example on starvation or stress. The model ignores space, motion and the cytoskeleton, and real networks are not random graphs; the point is the existence and position of a threshold, not the details.

![A graph model of the mitochondrial network (Formula 12.3.1, after Sukhorukov and colleagues). A: the three node types (free tips, end-to-end fusion points, three-way junctions, yellow) and the two fusion–fission reactions; κ is the ratio of fusion to fission. B: fraction of tubule ends at tips (x₁), at degree-2 nodes (2x₂) and at junctions (3x₃) as functions of κ (Eq. (12.2)). C: fraction of mitochondrial mass in the largest connected cluster: random-graph theory for networks with this degree distribution (line) and simulations of random networks with 4000 tubule ends (dots). The giant network appears at the threshold 3x₃ = x₁, κ ≈ 1.82 (dashed, Eq. (12.3))](./plots/mito-network.py)

## 12.4. Contacts with Other Organelles

Mitochondria are not connected to the endomembrane system by vesicle traffic, so they receive lipids and ions through membrane contact sites ([7.3.6](/7.3.6)), places where the outer membrane comes within 10–30 nm of another organelle and tethering proteins hold the membranes together without fusing them.

**Definition 12.4.1 (ERMES)** **ERMES** (ER–mitochondria encounter structure) is the tethering complex of yeast that links the ER membrane (Mmm1) to the mitochondrial outer membrane (Mdm10, Mdm34) through the cytosolic Mdm12; three of its subunits have SMP domains that form a hydrophobic channel through which glycerophospholipids pass between the two membranes.

Kornmann, Walter and colleagues (2009) found ERMES in a screen for mutants rescued by an artificial ER–mitochondria tether; mutants lacking it have altered mitochondrial phospholipids and lose mtDNA, and ERMES foci mark sites of mtDNA nucleoids and of fission. Animals lack ERMES but use other tethers and lipid transfer proteins at the same contacts (PDZD8, a relative of Mmm1; VPS13 proteins, long bridges for lipid flow; the VAPB–PTPIP51 pair; ORP5 and ORP8 for phosphatidylserine), and Mfn2 on the ER has been proposed as a tether, although this is debated.

The contacts serve four functions:

1. Phospholipid synthesis shared between organelles. Phosphatidylserine is made in the ER and its mitochondria-associated domains (first isolated by Jean Vance as a fraction of "mitochondria-associated membranes"), transferred to the mitochondrion and decarboxylated to phosphatidylethanolamine by phosphatidylserine decarboxylase in the inner membrane; much of this phosphatidylethanolamine returns to the ER, where in liver and yeast it is methylated to phosphatidylcholine ([7.1.26](/7.1.26#sec-26.4.3)). Cardiolipin is made in the inner membrane from phosphatidic acid, which crosses the intermembrane space bound to a transfer protein (PRELID1–TRIAP1). The two organelles thus run one pathway between them.
2. $\ce{Ca^2+}$ transfer. Inositol trisphosphate receptors of the ER, linked through the chaperone GRP75 to VDAC in the outer membrane, release $\ce{Ca^2+}$ into a narrow gap, where the local concentration reaches tens of micromolar, enough for the low-affinity mitochondrial calcium uniporter (MCU) of the inner membrane, driven by the membrane potential, to take it up. Matrix $\ce{Ca^2+}$ activates the dehydrogenases of the citric acid cycle, matching ATP production to the demand signaled by $\ce{Ca^2+}$; too much opens the permeability transition pore and kills the cell.
3. Fission and DNA replication (12.3.2).
4. Autophagy and apoptosis: contact sites contribute membrane to autophagosomes ([7.3.11](/7.3.11#sec-11.6.3)), and proteins of the Bcl-2 family act at them ([7.3.25](/7.3.25)).

Mitochondria also contact lipid droplets (which supply fatty acids for β oxidation in fasting), peroxisomes (with which they share β oxidation and the division machinery Drp1, Fis1 and Mff), lysosomes and the plasma membrane. The cell is thus a network of organelles joined by contacts, not a set of independent compartments.

## 12.5. Biogenesis and the Mitochondrial Genetic System

### 12.5.1. A Semiautonomous Organelle

**Definition 12.5.1 (Semiautonomous Organelle)** A **semiautonomous organelle** is an organelle that contains its own genome and machinery for its replication, transcription and translation, but depends on the nuclear genome for most of its proteins, which are made in the cytosol and imported; mitochondria and plastids are semiautonomous, and they arise only by growth and division of existing organelles, never de novo.

That the organelle makes some of its own proteins was shown with antibiotics. Mitochondrial ribosomes, like bacterial ones, are inhibited by chloramphenicol but not by cycloheximide, which blocks cytosolic ribosomes; cells labeled with radioactive amino acids in the presence of cycloheximide therefore label only the mitochondrially made polypeptides. In human cells these are 13: subunits 1–3 of cytochrome c oxidase, subunits 6 and 8 of the $\mathrm{F_o}$ part of ATP synthase, seven subunits of NADH dehydrogenase (ND1–ND6 and ND4L) and cytochrome b. A green plant cell thus runs three genetic systems, in the nucleus, the mitochondria and the plastids.

Human mitochondria contain about 1100–1500 different proteins (the MitoCarta inventory lists 1136), of which mtDNA encodes 13; the rest, including all proteins needed to replicate and express mtDNA and all mitoribosomal proteins, are nuclear-encoded and imported through TOM and TIM ([7.3.6](/7.3.6)). Most respiratory complexes are mosaics: Complex I has 7 mtDNA-encoded and 38 nuclear-encoded subunits ([7.1.23](/7.1.23#sec-23.5.4)). The two genetic systems must therefore be coordinated, and assembly factors make sure that the mtDNA-encoded core subunits, translated on mitoribosomes bound to the inner membrane (by the insertase OXA1), are joined by their nuclear partners; unassembled subunits are degraded by inner membrane proteases (12.6).

The amount of mitochondria is regulated as a whole. The transcriptional coactivator PGC-1α (discovered in brown fat as a **coactivator** induced by cold) activates the nuclear respiratory factors NRF1 and NRF2 and the estrogen-related receptor ERRα, which induce nuclear genes for respiratory subunits, import machinery and the mtDNA transcription factor TFAM; endurance exercise (through AMPK and $\ce{Ca^2+}$ signaling) and cold (through **protein kinase A**) increase the mitochondrial content of muscle and fat cells in this way. In cell division, the mitochondrial mass doubles and is partitioned between the daughters; in budding yeast the volume of the mitochondrial network scales with the volume of the cell.

### 12.5.2. Mitochondrial DNA

**Definition 12.5.2 (Mitochondrial DNA)** **Mitochondrial DNA** (mtDNA) is the genome of the mitochondrion, located in the matrix. In humans it is a circular double-stranded molecule of 16 569 bp, present in hundreds to thousands of copies per cell, that encodes 13 proteins of the oxidative phosphorylation system, 2 rRNAs and 22 tRNAs; it is packaged with the protein TFAM into nucleoids of about 100 nm, most containing a single genome.

The human genome is extremely compact. Its genes have no introns, they abut or overlap, and some lack complete stop codons, which are created by polyadenylation of the mRNA (U or UA plus poly(A) gives UAA). The only substantial noncoding region, the control region of about 1.1 kb, contains the promoters for transcription of each strand and an origin of replication, with a short third strand (7S DNA) forming a displacement loop. Each strand is transcribed into long polycistronic precursors by the single-subunit RNA polymerase POLRMT, related to the RNA polymerases of T-odd bacteriophages, with the factors TFAM and TFB2M; for this reason mitochondrial transcription is insensitive to rifampicin, which inhibits bacterial-type multisubunit RNA polymerases, so rifampicin sensitivity, sometimes listed among their bacterial features, is not a property of animal mitochondria. The tRNA genes are interspersed between the rRNA and protein genes, and excision of the tRNAs by RNase P and RNase Z releases the other RNAs ("tRNA punctuation"). Replication uses DNA polymerase γ and the helicase Twinkle, also of phage origin. The mitoribosome (55S in mammals, with 12S and 16S rRNAs and about 80 nuclear-encoded proteins) translates the 13 mRNAs at the inner membrane.

The mitochondrial **genetic code** differs from the standard code ([7.2.19](/7.2.19#sec-19.2.1)), and differs between lineages:

| Codon | Standard code | Vertebrate mitochondria | Invertebrate mitochondria (*Drosophila*) | Yeast mitochondria | Plant mitochondria |
|---|---|---|---|---|---|
| UGA | stop | Trp | Trp | Trp | stop |
| AUA | Ile | Met | Met | Met | Ile |
| CUN | Leu | Leu | Leu | Thr | Leu |
| AGA, AGG | Arg | not used as sense (see Remark 12.5.1) | Ser | Arg | Arg |

Mitochondrial tRNAs also read codons with relaxed rules: many recognize all four codons of a family with U in the wobble position, so 22 tRNAs suffice for all codons.

**Remark 12.5.1** AGA and AGG are often listed as stop codons of vertebrate mitochondria, but no release factor reads them. The two human genes that appear to end with them (*COX1* and *ND6*) are terminated by a −1 frameshift of the mitoribosome, which places a standard UAG stop codon in the A site (Temperley and colleagues, 2010). Plant mitochondria use the standard code but edit many of their transcripts by C-to-U conversion (**RNA editing**), so that the codons read differ from those in the DNA.

Why can the mitochondrial code change when the nuclear code is frozen? A change in the meaning of a codon alters every protein that uses it; with only 13 proteins encoded, a rare codon can drift to a new meaning without lethal consequences. The variant code also makes transfer of genes to the nucleus harder (12.8.3).

### 12.5.3. Maternal Inheritance and the Bottleneck

**Definition 12.5.3 (Maternal Inheritance)** **Maternal inheritance** is the transmission of organelle genomes (mtDNA, and plastid DNA in most flowering plants) to all offspring from the mother only, so that a trait encoded in the organelle is passed from an affected mother to all her children, but not from an affected father; it is a form of non-Mendelian (cytoplasmic) inheritance.

In mammals several mechanisms ensure it. The oocyte contains about $10^5$ copies of mtDNA and the sperm about a hundred, so paternal mtDNA would be diluted a thousandfold; in addition, mtDNA in the sperm is reduced during spermatogenesis, and the paternal mitochondria that enter the egg are ubiquitylated and eliminated, by autophagy in *C. elegans* ("allophagy") and by related mechanisms in mammals. In yeast, in contrast, both mating partners contribute mitochondria, and the mixed population sorts out within a few cell divisions by mitotic segregation.

Because a cell has many genomes, a **mutation** can coexist with the wild type (**heteroplasmy**, [7.1.23](/7.1.23#sec-23.5.4)), and the proportion can change between generations much faster than expected from the large number of copies in the oocyte.

**Definition 12.5.4 (Mitochondrial Bottleneck)** The **mitochondrial bottleneck** is the restriction of the number of mtDNA molecules that effectively contribute to the next generation during the development of the female germline, so that the heteroplasmy of the oocytes, and of the children, of one mother varies widely around hers.

Primordial germ cells contain only about 200 copies of mtDNA (Cree and colleagues, 2008), and the effective number of segregating units, estimated from the variance of heteroplasmy among siblings, is smaller still, of the order of tens; only a subpopulation of genomes may be replicated during oocyte maturation. The resulting variance can be calculated with the same sampling model that describes genetic drift in a population (7.10).

**Formula 12.5.1 (Binomial Sampling through the Bottleneck)** If each generation passes through $N$ effective segregating units sampled at random from a mother with mutant fraction $h_0$, and the oocyte is then amplified without further change, the heteroplasmy $h$ of a child has the **binomial distribution** $Nh \sim \mathrm{Bin}(N, h_0)$, with
$$
\mathbb{E}[h] = h_0, \qquad \operatorname{Var}(h) = \frac{h_0(1 - h_0)}{N}. \tag{12.4}
$$
After $t$ successive sampling steps of the same size,
$$
\operatorname{Var}(h_t) = h_0(1 - h_0)\left[1 - \left(1 - \frac{1}{N}\right)^t\right], \tag{12.5}
$$
which approaches $h_0(1 - h_0)$ as each lineage becomes fixed for one genotype (homoplasmy). The normalized variance $V = \operatorname{Var}(h)/[h_0(1 - h_0)]$ measures the size of the bottleneck: $N_{\mathrm{eff}} = 1/V$ for one step.

**Example 12.5.1 (Estimating the bottleneck and the risk)** Suppose the children of mothers with $h_0 = 0.5$ for a pathogenic mutation have heteroplasmies with a standard deviation of 0.10 (illustrative). Then $V = 0.01/0.25 = 0.04$ and $N_{\mathrm{eff}} \approx 25$. If disease appears above a threshold of 70% mutant genomes, the risk for a child of a mother with $h_0 = 0.3$ is $\mathbb{P}(\mathrm{Bin}(25, 0.3) \geq 18) \approx 2 \times 10^{-5}$, but for a mother with $h_0 = 0.5$ it is $\mathbb{P}(\mathrm{Bin}(25, 0.5) \geq 18) \approx 0.02$; with a bottleneck of 10 units the corresponding risks are 0.011 and 0.17. The risk depends steeply on both the mother's heteroplasmy and the size of the bottleneck, which is why genetic counseling for mtDNA diseases is difficult and why preimplantation diagnosis measures the heteroplasmy of the embryo directly.

![Segregation of mtDNA heteroplasmy through the germline bottleneck (Formula 12.5.1, neutral binomial sampling). A: heteroplasmy in ten maternal lineages over eight generations starting from 30% mutant mtDNA, with N = 10 (red) and N = 100 (blue) effective segregating units per generation: with the narrow bottleneck, lineages drift quickly, some to loss of the mutation and some above the threshold of 70% (dashed), within a few generations. B: distribution of heteroplasmy among the children of a mother with h₀ = 0.3 (dotted) for N = 10, 30 and 200, plotted as a density. C: probability that a child exceeds the 70% threshold as a function of N for mothers with h₀ = 0.2, 0.3 and 0.5 (logarithmic axes; the steps come from the discreteness of the binomial)](./plots/mtdna-bottleneck.py)

The neutral model is a baseline. Severe mutations are selected against in the female germline (purifying selection), so their transmitted heteroplasmy is lower than predicted, while some variants are favored within cells or tissues (selfish replication). Within a person, heteroplasmy also drifts among tissues during development and ageing, and deletions accumulate clonally in postmitotic cells such as neurons and muscle fibers, partly because shorter genomes may replicate faster. Mitochondrial replacement by nuclear transfer into an enucleated donor oocyte, which bypasses the bottleneck, is described in [7.1.23](/7.1.23#sec-23.5.4); the transmission genetics of organelle genes is treated in 7.4.

## 12.6. Quality Control

Mitochondria are particularly exposed to damage: the respiratory chain produces **reactive oxygen species** next to the mtDNA and the respiratory complexes, and import of about a thousand proteins and assembly of complexes from two genomes give many chances for error. The cell deals with damage at four levels, each acting on a larger scale and at a higher cost than the previous one:

| Level | Mechanism | Trigger |
|---|---|---|
| Molecules | **molecular chaperones** (mtHsp70, Hsp60–Hsp10) and ATP-dependent proteases: LONP1 and ClpXP in the matrix, the AAA proteases YME1L (facing the intermembrane space) and AFG3L2/paraplegin (facing the matrix) in the inner membrane; the ubiquitin–proteasome system extracts outer membrane proteins and clears clogged import channels | misfolded or unassembled proteins |
| Signaling to the nucleus | mitochondrial unfolded protein response: in *C. elegans* the transcription factor ATFS-1 is normally imported and degraded, but when import fails it goes to the nucleus and induces chaperones and proteases; in mammals the protease OMA1 cleaves DELE1, which activates the kinase HRI and the **integrated stress response** ([7.2.20](/7.2.20)) | stress that impairs import or folding |
| Parts of an organelle | mitochondria-derived vesicles carry oxidized proteins to lysosomes or peroxisomes; fission isolates damaged segments (12.3.4) | local oxidative damage |
| Whole organelles | mitophagy: PINK1–Parkin and receptor-mediated ([7.3.11](/7.3.11#sec-11.7.2)) | loss of membrane potential |
| Whole cell | apoptosis via cytochrome c release ([7.3.25](/7.3.25)) | irreparable damage, stress signals |

Two of these systems use the same sensor. Both PINK1 and ATFS-1 carry mitochondrial targeting sequences and are normally destroyed after import; when import fails, their survival outside the matrix becomes the signal. Because import requires the membrane potential, import efficiency is a direct readout of mitochondrial health, and the cell reads it from outside. Mutations in mitochondrial proteases cause neurodegeneration (paraplegin in hereditary spastic paraplegia), and loss of quality control at several levels is a feature of ageing (7.3.25).

## 12.7. Plastids

### 12.7.1. Plastid Types and Interconversion

**Definition 12.7.1 (Plastid and Chloroplast)** A **plastid** is a double-membrane organelle of plants and algae, descended from a cyanobacterium, that contains its own genome and develops into different forms according to cell type and conditions, all derived from the small undifferentiated **proplastids** of meristem cells. A **chloroplast** is the photosynthetic plastid, with an envelope of two membranes, the stroma (which contains the enzymes of carbon fixation, the plastid DNA and ribosomes) and the internal thylakoid membranes, stacked in grana, that carry the photosystems and ATP synthase ([7.1.24](/7.1.24#sec-24.1.2)).

A chloroplast of a leaf mesophyll cell is lens-shaped, typically 5–10 µm long and 2–4 µm thick, and a mesophyll cell holds from a few dozen to more than a hundred of them. It has three membranes (outer and inner envelope and thylakoid) enclosing three separate aqueous spaces (the intermembrane space of the envelope, the stroma and the thylakoid lumen), one more of each than a mitochondrion, because the thylakoids are not connected to the inner envelope in the mature organelle:

| Part | Properties |
|---|---|
| Outer envelope membrane | permeable to small solutes through porin-like channels (OEPs); TOC import complex |
| Inner envelope membrane | the permeability barrier; metabolite carriers such as the triose phosphate/phosphate translocator, which exports the products of carbon fixation in exchange for $\mathrm{P_i}$ ([7.1.25](/7.1.25)); TIC import complex |
| Stroma | Rubisco (about half of the soluble protein of a leaf) and the other enzymes of carbon assimilation; plastid DNA, 70S ribosomes; starch grains, plastoglobules (lipoprotein droplets) and the iron store phytoferritin |
| Thylakoid membrane | photosystems, cytochrome $b_6f$, ATP synthase; lipids mostly galactolipids (monogalactosyl- and digalactosyldiacylglycerol, about 75 %), with few phospholipids; stacked into grana (often 40–60 per chloroplast) joined by stroma lamellae |

**Definition 12.7.2 (Etioplast, Amyloplast and Chromoplast)** An **etioplast** is the plastid of seedlings grown in the dark, which contains a paracrystalline lattice of tubular membranes (the prolamellar body) rich in protochlorophyllide and its light-dependent reductase, and turns into a chloroplast within hours of illumination. An **amyloplast** is a nonpigmented plastid that stores starch, found in storage organs (potato tubers, cereal endosperm) and, in the columella cells of the root cap and the endodermis of shoots, serving as a gravity sensor (statolith). A **chromoplast** is a plastid that accumulates carotenoids in globules, fibrils or crystals and gives yellow, orange and red colors to fruits, petals and some roots.

Other plastids include elaioplasts, which store lipids (in the tapetum of anthers), the general class of nonpigmented leucoplasts, and gerontoplasts, chloroplasts of senescent leaves that dismantle their thylakoids and export nitrogen. The types interconvert. A tomato fruit turns red as its chloroplasts become chromoplasts: chlorophyll and thylakoids are broken down and the carotenoid lycopene accumulates as crystals; potato tubers exposed to light turn green as amyloplasts become chloroplasts; and some chromoplasts can revert to chloroplasts, as in citrus fruits that regreen. Etioplasts explain why seedlings germinating under soil are pale: the enzyme protochlorophyllide oxidoreductase of angiosperms needs light to reduce its substrate, so chlorophyll synthesis and thylakoid assembly wait for the seedling to reach the surface.

![Plastid types, their interconversions and plastid division (schematic, not to scale). A: all plastids develop from proplastids of meristems; in light they become chloroplasts, in the dark etioplasts, with a lattice-like prolamellar body, which turn into chloroplasts within hours of illumination; proplastids also become amyloplasts (starch granules; gravity sensing in root caps) and elaioplasts (lipid droplets). Chloroplasts become chromoplasts (carotenoid globules and crystals) when fruits ripen and gerontoplasts in senescent leaves; dashed arrows show reversals such as the greening of amyloplasts in light and the regreening of chromoplasts. B: division of a chloroplast: a ring of FtsZ proteins assembles on the stromal side of the inner envelope (green dots), and through proteins spanning the envelope (ARC6, PDV1/2) recruits the dynamin-related ARC5 (DRP5B) and the polyglucan outer plastid-dividing ring on the cytosolic side (red dots); together they constrict the organelle](./plots/plastids.py)

### 12.7.2. Plastid Division

Plastids divide like the bacteria they came from, but with help from the host. In a developing leaf, proplastids and young chloroplasts divide repeatedly as the cells expand, while mature chloroplasts in fully expanded leaves rarely divide. Inside, in the stroma, the tubulin-like GTPases FtsZ1 and FtsZ2, now encoded in the nucleus, assemble a ring at the division site, positioned by homologs of the bacterial Min system (MinD, MinE and the plant protein ARC3). The ring is linked through the inner envelope protein ARC6 and the outer envelope proteins PDV1 and PDV2 to the cytosolic dynamin-related protein ARC5 (DRP5B). Electron microscopy of the red alga *Cyanidioschyzon merolae*, which has a single chloroplast, revealed plastid-dividing (PD) rings on both sides of the envelope (Kuroiwa and colleagues); the outer PD ring is a bundle of polyglucan filaments made by a glycosyltransferase. Arabidopsis mutants defective in the machinery (*arc*, for accumulation and replication of chloroplasts) have mesophyll cells with a few giant chloroplasts instead of about a hundred normal ones, yet they photosynthesize nearly normally: what is regulated is the total chloroplast volume per cell, not the number of plastids. In some algae mitochondria also divide with FtsZ, but animals and fungi lost the bacterial system and use Drp1 only, from the outside (12.3.2).

### 12.7.3. The Chloroplast Genome

The chloroplast genomes of land plants are circular molecules of 120–160 kb, present in tens to hundreds of copies per plastid and thousands per leaf cell. Most have a quadripartite structure, a large and a small single-copy region separated by two inverted repeats that contain the rRNA genes. They carry about 100–130 genes, for the rRNAs and about 30 tRNAs, ribosomal proteins, subunits of a bacterial-type RNA polymerase, and core subunits of photosystems I and II, the cytochrome $b_6f$ complex, ATP synthase and NADH dehydrogenase-like complex, and the large subunit of Rubisco (*rbcL*); more than 95% of the 2000–3000 chloroplast proteins are nuclear-encoded. Plastid genes are transcribed by two polymerases: the plastid-encoded, bacterial-type PEP, which uses nuclear-encoded σ factors and transcribes mainly photosynthesis genes, and a nuclear-encoded, phage-type NEP, which transcribes housekeeping genes early in development. Transcripts are processed and edited (C to U at about 30–40 sites in angiosperms) by nuclear-encoded pentatricopeptide repeat proteins, an RNA-binding family with hundreds of members in plants.

Rubisco is the textbook example of coordination between genomes. Its large subunit is made in the chloroplast, its small subunit in the cytosol, imported and processed; the two assemble with the help of chaperonins and assembly factors into the $\mathrm{L_8S_8}$ holoenzyme ([7.1.25](/7.1.25#sec-25.1.2)), and when the small subunit is lacking, translation of the large subunit is repressed. Plastid inheritance is maternal in most angiosperms but biparental in some (*Pelargonium*, as Erwin Baur found in 1909) and paternal in most conifers; in plants with biparental inheritance, mixtures of normal and defective plastids sort out in development and produce variegated leaves with green and white sectors, the phenomenon in which Carl Correns and Baur first recognized non-Mendelian inheritance.

### 12.7.4. Retrograde Signaling

**Definition 12.7.3 (Retrograde Signaling)** **Retrograde signaling** is the communication from organelles (plastids or mitochondria) to the nucleus that adjusts the expression of nuclear genes for organelle proteins to the developmental and functional state of the organelle; the opposite flow, from the nucleus to the organelle, is anterograde control.

The classic experiment used norflurazon, an inhibitor of carotenoid synthesis that causes photobleaching of chloroplasts in light: in treated seedlings the nuclear genes for chloroplast proteins, such as those encoding the light-harvesting chlorophyll-binding proteins (*LHCB*), are shut off, so the nucleus must receive a signal of plastid damage. Joanne Chory's group isolated *Arabidopsis* mutants that keep expressing *LHCB* after such treatment, the *genomes uncoupled* (*gun*) mutants (Susek and colleagues, 1993). Several encode enzymes of tetrapyrrole synthesis (GUN4, GUN5, the H subunit of magnesium chelatase), which suggested that a chlorophyll precursor is the signal, but the precursor hypothesis has not been confirmed; GUN1, a plastid pentatricopeptide repeat protein, integrates several signals. Other plastid signals include singlet oxygen sensed through the EXECUTER proteins, the isoprenoid precursor MEcPP, which accumulates under stress, and the nucleotide PAP. Mitochondria signal by analogous routes: the RTG pathway in yeast, which induces genes of the citric acid cycle when respiration fails, and the mitochondrial unfolded protein response, AMPK and the integrated stress response in animals (12.6).

## 12.8. Origin and Evolution

### 12.8.1. The Evidence for Endosymbiosis

The **endosymbiotic theory** ([7.1.1](/7.1.1)), championed by Lynn Margulis in 1967 after earlier proposals by Mereschkowski and others, holds that mitochondria descend from an α-proteobacterium and plastids from a cyanobacterium, each engulfed by a host cell and reduced to an organelle. The evidence is now overwhelming:

- Phylogenies of rRNA and of proteins encoded by the organelle genomes place mitochondria next to the Alphaproteobacteria and plastids within the Cyanobacteria (close to the freshwater genus *Gloeomargarita*).
- The organelles have their own circular genomes, their own **ribosomes** of bacterial type (70S in chloroplasts; 55S, with shortened rRNAs, in mammalian mitochondria), sensitive to antibiotics such as chloramphenicol and tetracycline, and start translation with formylmethionine.
- The outer membranes contain β-barrel proteins (porins) inserted by machinery homologous to the bacterial Omp85/BamA system (SAM50 in mitochondria, TOC75 in chloroplasts), and the inner membranes resemble bacterial plasma membranes, with cardiolipin and bacterial-type respiratory chains and transporters.
- They multiply only by division; plastids divide with FtsZ.
- Intermediate stages exist: endosymbiotic bacteria of insects with tiny genomes, and the chromatophore of the amoeba *Paulinella* (12.8.4).

The host of the mitochondrial endosymbiont was itself an archaeon. Asgard archaea, first known from environmental genomes (Lokiarchaeota, 2015) and cultured in 2020 (*Prometheoarchaeum syntrophicum*, a slow-growing, tentacle-forming organism that lives with bacterial partners), are the closest prokaryotic relatives of eukaryotes and encode homologs of eukaryotic actin, small GTPases and ESCRT ([7.3.10](/7.3.10#sec-10.4.2)). Mitochondria were acquired once, more than 1.5 billion years ago and before the last eukaryotic common ancestor, which already had them; all eukaryotes known to lack mitochondria have lost them secondarily.

### 12.8.2. Gene Transfer to the Nucleus

The endosymbionts had thousands of genes; their descendants keep from 3 to about 100 (mitochondria) and about 100–250 (plastids). The others were lost because the host already had equivalents, or were transferred to the nucleus, acquired a targeting sequence and returned as imported proteins (endosymbiotic gene transfer); about 18% of the nuclear genes of *Arabidopsis* (some 4500) are of cyanobacterial origin. Transfer continues today: fragments of mitochondrial and plastid DNA enter the nucleus as NUMTs and NUPTs; in tobacco, plastid DNA reaches the nucleus of about one in 16 000 pollen grains in each generation (Huang, Ayliffe and Timmis, 2003); and new NUMTs arise in about one in $10^4$ human births. Most such insertions are nonfunctional, but they show that the rate-limiting step for a functional transfer is not the movement of DNA but its activation: the gene must acquire a nuclear promoter, a targeting sequence and, for mitochondria, the standard genetic code.

![Gene content of organelle genomes compared with free-living relatives (logarithmic scale; approximate values). Mitochondrial lineage: the alphaproteobacterium Rickettsia prowazekii, an intracellular parasite whose genome is already reduced (834 protein genes); the mitochondrial genomes of the protist Reclinomonas americana (97 genes, the most bacteria-like known), of Arabidopsis thaliana (57), of humans (37) and of the malaria parasite Plasmodium falciparum (3 protein genes plus fragmented rRNA genes); and the human mitochondrial proteome (about 1136 proteins), almost all encoded in the nucleus. Plastid lineage: the cyanobacterium Synechocystis (about 3200 protein genes); the chromatophore of Paulinella chromatophora, a plastid acquired about 100 million years ago (about 870 protein genes); a typical land-plant chloroplast genome (about 120 genes); and the estimated chloroplast proteome of Arabidopsis (about 3000 proteins)](./plots/organelle-genomes.py)

### 12.8.3. Why Keep a Genome?

Maintaining a separate genetic system is expensive: more than a hundred nuclear genes (polymerases, ribosomal proteins, aminoacyl-tRNA synthetases, processing enzymes) serve only to express 13 mitochondrial proteins in humans. Why has transfer not gone to completion? Three hypotheses are discussed, and they are not exclusive:

1. Hydrophobicity. The proteins kept are mostly very hydrophobic core subunits of the respiratory and photosynthetic complexes; made in the cytosol, they might be misdirected to the ER by the **signal recognition particle** or aggregate before import.
2. Colocation for redox regulation (CoRR; John Allen). An organelle that keeps the genes for the core subunits of its electron transport chains can adjust their synthesis directly to its own redox state, independently of other organelles in the same cell; this explains why the retained genes are so similar in independent lineages.
3. Barriers to transfer, such as the variant genetic code of mitochondria and the editing of plant organelle transcripts, which make a transferred gene nonfunctional.

Comparisons across eukaryotes show that the genes retained most often encode proteins at the center of their complexes, are hydrophobic and have a high GC content (Johnston and Williams, 2016), consistent with the first two hypotheses. The genome itself is a liability, as mtDNA diseases show; the costs and benefits of keeping it are still being weighed by evolution.

### 12.8.4. Primary, Secondary and Tertiary Endosymbiosis

All plastids of plants, green and red algae and glaucophytes (the Archaeplastida) descend from one primary endosymbiosis with a cyanobacterium; their plastids have two envelope membranes (and the glaucophyte plastids even keep a peptidoglycan wall between them). The amoeba *Paulinella chromatophora* acquired a cyanobacterium independently, about 100 million years ago; its "chromatophore" has lost two-thirds of its genes and imports some nuclear-encoded proteins, a second primary plastid caught at an early stage.

Many other algae obtained their plastids at second hand, by engulfing a eukaryotic alga:

| Endosymbiosis | Plastid source | Examples | Features |
|---|---|---|---|
| Primary | cyanobacterium | land plants, green and red algae, glaucophytes; *Paulinella* (independently) | two envelope membranes |
| Secondary (green) | green alga | euglenids, chlorarachniophytes | three or four membranes; chlorarachniophytes keep a vestigial nucleus of the alga (nucleomorph) |
| Secondary (red) | red alga | diatoms, brown algae, haptophytes, cryptophytes, dinoflagellates, apicomplexans | four membranes in most; cryptophytes keep a nucleomorph |
| Tertiary | alga with a secondary plastid | some dinoflagellates (*Karenia*, with a haptophyte plastid) | complex envelopes, replaced plastids |

The extra membranes record the history: the outer two of four come from the host's food vacuole and the engulfed alga's plasma membrane, and nuclear-encoded plastid proteins of these algae carry a signal peptide that takes them first into the ER, followed by a plastid transit peptide. Parasites of the phylum Apicomplexa, including *Plasmodium* and *Toxoplasma*, descend from photosynthetic algae and keep a nonphotosynthetic plastid, the apicoplast, which makes isoprenoids, fatty acids and heme; because it is of bacterial origin, it is a target for antibiotics and the herbicide-like drug fosmidomycin. The tree of eukaryotes is thus a web of endosymbioses, and the chloroplast of a diatom is, in effect, a cyanobacterium inside a red alga inside another eukaryote.

## Summary

| Topic | Key points |
|---|---|
| Energy conversion (12.1) | chemiosmosis, respiratory chain, photosystems, ATP synthase in [7.1.23](/7.1.23)–[7.1.25](/7.1.25); shared design: two membranes, own genome, imported proteins, bacterial origin |
| Architecture (Definitions 12.2.1, 12.2.2) | Altmann, Benda, Michaelis, Kennedy and Lehninger; marker enzymes: monoamine oxidase (outer), adenylate kinase (intermembrane space), cytochrome c oxidase (inner), malate dehydrogenase (matrix); outer membrane (VDAC), intermembrane space, inner boundary membrane, cristae, matrix; crista junctions and MICOS, ATP synthase dimer rows at rims, OPA1; cardiolipin; crista lumen stores cytochrome c |
| Number and roles (12.2.3) | up to 20–35% of cell volume; positioned at ATP demand; biosynthesis, Fe–S clusters, heme, urea cycle, lipids, heat, Ca²⁺, ROS, apoptosis, innate immunity |
| Dynamics (Definitions 12.3.1, 12.3.2) | fusion: Mfn1/2 (outer), OPA1 (inner; OMA1/YME1L processing); fission: Drp1 with Mff, Fis1, MiD49/51 at ER (INF2–actin) and lysosome contacts; transport: Miro–TRAK, Ca²⁺ arrest |
| Purposes and disease (12.3.4) | complementation, distribution, segregation of damage, metabolic adaptation; CMT2A (*MFN2*), dominant optic atrophy (*OPA1*), *DNM1L* encephalopathy |
| Network model (Formula 12.3.1) | tips, end-to-end nodes, junctions; $x_2 = \kappa x_1^2$, $x_3 = \kappa^2 x_1^3$; percolation at $3x_3 = x_1$, $\kappa_{\mathrm{c}} \approx 1.82$ |
| Contacts (Definition 12.4.1) | ERMES (yeast), PDZD8, VPS13, ORP5/8; PS → PE → PC shared pathway; IP₃R–GRP75–VDAC–MCU Ca²⁺ transfer; fission and nucleoid sites |
| Biogenesis (Definition 12.5.1) | semiautonomous; chloramphenicol-sensitive, cycloheximide-resistant mitochondrial translation; ≈ 1136 proteins, 13 from mtDNA; mosaic complexes; PGC-1α, NRF1/2, TFAM; growth and division only |
| mtDNA (Definition 12.5.2, Remark 12.5.1) | 16 569 bp, 13 + 2 + 22 genes, TFAM nucleoids; POLRMT, tRNA punctuation, POLγ, Twinkle; variant and lineage-specific codes (UGA Trp, AUA Met; AGA/AGG by frameshift) |
| Inheritance (Definitions 12.5.3, 12.5.4; Formula 12.5.1) | maternal; bottleneck of tens of units; $\operatorname{Var}(h) = h_0(1-h_0)/N$; disease risk steep in $h_0$ and $N$ (Example 12.5.1); purifying selection |
| Quality control (12.6) | chaperones and proteases → UPRmt (ATFS-1; OMA1–DELE1–HRI–ISR) → mitochondria-derived vesicles and fission → mitophagy → apoptosis; import efficiency as sensor |
| Plastids (Definitions 12.7.1, 12.7.2) | three membranes, three spaces; triose phosphate translocator; galactolipid thylakoids, grana; proplastid → chloroplast, etioplast, amyloplast, chromoplast, elaioplast, gerontoplast; interconversion |
| Plastid division and genome (12.7.2, 12.7.3) | FtsZ inside, ARC5/DRP5B and PD ring outside; 120–160 kb quadripartite genome, ≈ 100–130 genes; PEP and NEP; editing; Rubisco L₈S₈ coordination; maternal, biparental or paternal inheritance, variegation |
| Retrograde signaling (Definition 12.7.3) | norflurazon, *gun* mutants, GUN1; singlet oxygen, MEcPP, PAP; yeast RTG, UPRmt |
| Origin (12.8) | α-proteobacterium and cyanobacterium; Asgard archaeal host; endosymbiotic gene transfer (18% of *Arabidopsis* genes), NUMTs; hydrophobicity, CoRR, code barriers; primary, *Paulinella*, secondary and tertiary plastids, nucleomorphs, apicoplast |

## Questions

1. Cells are treated with an uncoupler that collapses the mitochondrial membrane potential. Predict, within an hour, what happens to (a) the import of a matrix protein, (b) OPA1 processing and mitochondrial morphology, (c) PINK1 and Parkin. Explain how these responses together direct damaged mitochondria to mitophagy.

   **Answer** (a) Import through TIM23 requires the potential, which pulls the positively charged presequence across the inner membrane; import of matrix proteins stops (outer membrane proteins inserted by TOM and SAM are less affected). (b) OMA1 is activated and converts long OPA1 to short forms; inner membrane fusion stops while Drp1-mediated fission continues, so the network fragments into small, round mitochondria. (c) PINK1 is no longer imported and degraded; it accumulates on the outer membrane, phosphorylates ubiquitin and Parkin, and Parkin coats the mitochondria with ubiquitin chains (Formula 11.7.1). Together: fragmentation produces units small enough to be engulfed, loss of OPA1 function and Parkin-dependent degradation of mitofusins prevent refusion with healthy mitochondria, and the ubiquitin coat recruits autophagy receptors, so the damaged pieces are removed by mitophagy.

2. In the graph model of Formula 12.3.1, suppose a drug halves the rate of tip-to-side fusion only, so that $a_2/b_2$ is half of $a_1/b_1$. Without calculating, how should the threshold change? Then generalize Eq. (12.2) to $\kappa_1 \neq \kappa_2$ and state the percolation condition.

   **Answer** Junctions form only by tip-to-side fusion, and only junctions (degree 3) favor percolation, so reducing $a_2$ raises the overall fusion/fission ratio needed for a connected network. With $\kappa_1 = a_1 M/b_1$ and $\kappa_2 = a_2 M/b_2$, mass action gives $x_2 = \kappa_1 x_1^2$ and $x_3 = \kappa_2 x_2 x_1 = \kappa_1\kappa_2 x_1^3$, with $x_1 + 2\kappa_1 x_1^2 + 3\kappa_1\kappa_2 x_1^3 = 1$. The Molloy–Reed condition $3x_3 > x_1$ becomes $3\kappa_1\kappa_2 x_1^2 > 1$, and at the threshold $x_1 = 1/\sqrt{3\kappa_1\kappa_2}$. Substituting into the constraint, $x_1 + 2\kappa_1 x_1^2 + 3\kappa_1\kappa_2 x_1^3 = 2x_1 + 2/(3\kappa_2) = 1$, so the threshold is
   $$
   \frac{2}{\sqrt{3\kappa_1\kappa_2}} + \frac{2}{3\kappa_2} = 1.
   $$
   For $\kappa_1 = \kappa_2$ this gives $\kappa_{\mathrm{c}} = 2/\sqrt 3 + 2/3$. Percolation requires $2/(3\kappa_2) < 1$, i.e. $\kappa_2 > 2/3$, whatever $\kappa_1$ is; halving $\kappa_2$ requires a larger $\kappa_1$, confirming that end-to-end fusion alone, however fast, cannot make the network percolate.

3. A woman carries a pathogenic mtDNA mutation at 40% heteroplasmy in her blood and is asymptomatic. Her brother is also a carrier. Explain (a) whether the brother can transmit the mutation, (b) why her children may be unaffected, mildly or severely affected, and (c) how the heteroplasmy measured in one tissue may differ from that in her oocytes and in her muscle.

   **Answer** (a) No: mtDNA is maternally inherited, and paternal mtDNA is eliminated after fertilization, so the brother's children do not inherit it (rare exceptions aside). (b) Through the germline bottleneck each oocyte samples a small effective number of genomes, so the children's heteroplasmy is distributed around 40% with variance $h_0(1-h_0)/N$; children above the biochemical threshold (often 60–90% depending on the mutation and tissue) are affected, and the severity increases with their level (Formula 12.5.1, Example 12.5.1). (c) Heteroplasmy drifts independently in different cell lineages during development and life (mitotic segregation); it often declines in blood, a rapidly dividing tissue in which cells with high mutant load are selected against, and may rise in postmitotic muscle and neurons. Blood therefore underestimates the risk, and her oocytes, each sampled through the bottleneck, vary widely.

4. Plastid gene expression in leaves is blocked by lincomycin, an inhibitor of plastid translation. Predict the effect on the expression of the nuclear gene *RBCS* and on the amount of the Rubisco large subunit, and explain the role of *gun1* mutants in this experiment.

   **Answer** Without plastid translation, the large subunit (plastid-encoded *rbcL*) is not made, and Rubisco cannot assemble; the small subunits made in the cytosol are imported but, unassembled, are degraded. Retrograde signals from the damaged plastids repress nuclear photosynthesis genes, including *RBCS* and *LHCB*, so their mRNAs fall. In *gun1* mutants the signal from blocked plastid translation is not transmitted, and *RBCS* and *LHCB* stay expressed despite lincomycin: the uncoupling of nuclear expression from plastid state identifies GUN1 as a component of the retrograde pathway.

5. Why do chloroplasts and mitochondria divide differently (FtsZ from the inside versus Drp1 from the outside), and what does this suggest about the history of each organelle?

   **Answer** Plastids retain the bacterial division apparatus: FtsZ, a tubulin-like GTPase assembled on the inner side of the membrane as in bacterial cytokinesis, positioned by Min proteins, now nuclear-encoded; the host added an outer machinery (ARC5/DRP5B, PD ring) to divide the outer envelope. Mitochondria of animals and fungi lost FtsZ and are divided entirely from outside by a dynamin of the host, recruited and positioned by host organelles (ER, lysosomes). Mitochondria of some algae still use FtsZ, which shows that the ancestral mitochondrion also divided bacterially. The difference reflects age and degree of integration: mitochondria were acquired earlier, and the host took over more of their biology, including division; plastids, acquired later, remain closer to their bacterial ancestors in genome, ribosomes and division.

6. (Open question) Using the hypotheses of 12.8.3, predict which genes you would expect to remain in the mitochondrial genome of a newly discovered protist that has kept many mitochondrial genes, and how you would test the CoRR hypothesis experimentally.

   **Answer** Outline: the genes most likely retained are those encoding hydrophobic core subunits of the respiratory complexes (cytochrome b, COX1–3, ND1–6) and the rRNAs and tRNAs needed to express them, followed by ribosomal proteins and, in genomes like that of *Reclinomonas*, subunits of a bacterial-type RNA polymerase and the SecY translocase; genes for soluble matrix enzymes are expected to have moved to the nucleus. Tests of CoRR: show that the expression of organelle-encoded subunits responds to the redox state of the organelle's own electron transport chain (for example, quinone pool reduction measured with inhibitors) independently of nuclear signals, and differently in different organelles of the same cell (e.g. in a heteroplasmic or chimeric cell, or with targeted inhibitors); express a recoded, nuclear version of a retained gene with a targeting sequence (allotopic expression) and ask whether it can replace the organelle copy and whether redox control is lost. Successful allotopic expression of hydrophobic subunits (e.g. ATP6) has been difficult, which supports the hydrophobicity hypothesis; loss of regulation without loss of function would support CoRR.
