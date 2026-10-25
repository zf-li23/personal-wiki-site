---
title: The Foundations of Biochemistry
description: Course map and the two threads of biochemistry (chemical properties → structure → function; energy balance + feedback control); cellular, chemical, physical, genetic and evolutionary foundations of life.
---

*Biochemistry* is the chemistry of life: it describes in molecular terms the structures, mechanisms and chemical processes shared by all organisms, and it supplies the organizing principles that underlie life in all its diverse forms. Following Lehninger, the subject has three parts: the structural chemistry of the components of living matter and the relation between chemical structure and biological function (Part I, *structure and catalysis*); the chemical reactions of living organisms and their energetics (Part II, *bioenergetics and metabolism*); and the chemistry of the storage and transmission of biological information (Part III, *information pathways*). This course covers Parts I and II; Part III, from genes and chromosomes to protein synthesis, is the subject of [Molecular Biology](/7.2).

The course is long and much of its detail must be remembered, but neither part is a list. Each has one thread that organizes the detail:

| | Part I: structural biochemistry (7.1.2–7.1.15) | Part II: metabolic biochemistry (7.1.16–7.1.29) |
|---|---|---|
| Thread | chemical properties → structure → biological function | energy balance + feedback control |
| Question asked of every molecule or pathway | Which weak interactions and which reactive groups does it have, what shape do they impose, and what does the shape allow it to do? | Where does it run, what is the net reaction and its ATP/NAD(P)H balance, which step is committed and far from equilibrium, who activates and who inhibits it, and how is the opposing pathway switched off? |
| Example | the imidazole of His has $\mathrm{p}K_{\mathrm{a}} \approx 6$ (7.1.3), so it can both donate and accept a proton at pH 7 and becomes the catalytic base of serine proteases (7.1.8) | phosphofructokinase-1 is inhibited by ATP and citrate and activated by AMP (7.1.18), so glycolysis runs when the cell's energy charge falls |
| Summary format | table "structural feature → chemical property → function" | "pathway card": location, net reaction, energy account, regulated steps, activators, inhibitors, hormones, coenzymes, diseases |

This first chapter lays the foundations on which both threads rest: what a cell is and why it is small (1.1), which chemistry living matter is built from (1.2), how organisms use energy without ever reaching equilibrium (1.3), and how genetic information and evolution explain why all organisms share the same molecules (1.4). Most of the chemistry and physics needed here has been developed in the chemistry courses ([6.1](/6.1), [6.3](/6.3), [6.5](/6.5)); this chapter only collects what biochemistry takes from them. The orders of magnitude of molecular biology (sizes, copy numbers, rates, energies in units of $k_{\mathrm{B}}T$) are tabulated in [7.2.1](/7.2.1).

![Course map. The structural hierarchy of the cell runs from monomeric units (amino acids, nucleotides, sugars, fatty acids, together with water) through macromolecules (proteins, nucleic acids, polysaccharides) and supramolecular complexes (ribosomes, membranes with their proteins) to cells and organelles. Under each level are the chapters of this course that deal with it. Part I (7.1.2–7.1.15) follows the thread from chemical properties to structure to function; Part II (7.1.16–7.1.29) treats metabolism in terms of energy balance and feedback control](./plots/course-map.py)

## 1.1. Cellular Foundations

### 1.1.1. Cells Are the Structural and Functional Units of Life

Living matter is distinguished from inanimate matter by a set of properties that no single molecule possesses but every cell does: a high degree of chemical complexity and microscopic organization; systems for extracting, transforming and using energy from the environment to build and maintain structures and do work; defined functions for each component and regulated, dynamic interactions among them; mechanisms for sensing and responding to changes in the surroundings; and a capacity for precise self-replication combined with enough variation for evolution.

All cells, from the smallest bacterium to a neuron, share three features. A *plasma membrane* of lipid and protein separates the cell from its surroundings; it is a barrier to the free passage of ions and polar molecules, and its transport proteins and receptors control what enters and what signals are received (7.1.13). The *cytoplasm* is the aqueous interior, a concentrated solution of enzymes, metabolites, RNA and ribosomes in which most of metabolism takes place; the *cytosol* is the soluble part of it. A *nucleoid* (in bacteria and archaea) or a *nucleus* (in eukaryotes) holds the genome as DNA complexed with proteins.

**Definition 1.1.1** Organisms whose cells have no nuclear envelope, so that the DNA lies in a nucleoid in direct contact with the cytoplasm, are called **prokaryotes**; they comprise the domains Bacteria and Archaea. Organisms whose cells have a nucleus bounded by a double membrane, and in general other membrane-bounded organelles, are called **eukaryotes**.

The term "prokaryote" describes a cell plan, not a natural group: Archaea are more closely related to eukaryotes than to Bacteria (1.4.4).

### 1.1.2. Cell Size Is Limited by Diffusion

Most cells are microscopic: bacteria are typically 1–2 µm long, animal and plant cells 5–100 µm across. The lower limit is set by the minimum number of molecules needed for a self-replicating system (the smallest cells, mycoplasmas about 0.3 µm across, encode fewer than 500 proteins). The upper limit is set by diffusion. Every metabolite and every O₂ molecule moves through the cytoplasm by **Brownian motion** ([6.3.21](/6.3.21#sec-21.3)); in three dimensions the mean squared displacement after time $t$ is $\langle r^2\rangle = 6Dt$, so the time to diffuse a distance $x$ is of the order

$$
t \approx \frac{x^2}{6D},
$$
where $D$ is the diffusion coefficient. The time grows with the square of the distance, so doubling the size of a cell quadruples the time needed for a molecule to cross it, while the ratio of surface (through which nutrients enter) to volume (which consumes them) falls as $1/x$.

**Example 1.1.1** Small molecules in water have $D \approx 10^{-9}\,\mathrm{m^2\,s^{-1}}$ (O₂: $2.1 \times 10^{-9}$, glucose: $6.7 \times 10^{-10}\,\mathrm{m^2\,s^{-1}}$ at $25\,^\circ\mathrm{C}$). Across a bacterium ($x = 1\,\mu\mathrm{m}$) O₂ needs $t \approx (10^{-6})^2/(6 \times 2.1 \times 10^{-9})\,\mathrm{s} \approx 0.1\,\mathrm{ms}$; across a $20\,\mu\mathrm{m}$ animal cell about $30\,\mathrm{ms}$; over $1\,\mathrm{mm}$ about $80\,\mathrm{s}$; over $1\,\mathrm{cm}$ more than two hours. Proteins diffuse ten times more slowly in water ($D \approx 10^{-10}\,\mathrm{m^2\,s^{-1}}$ for myoglobin) and another three to ten times more slowly in the crowded cytoplasm (green fluorescent protein: $\approx 25\,\mu\mathrm{m^2\,s^{-1}}$ in mammalian cytoplasm, $\approx 8\,\mu\mathrm{m^2\,s^{-1}}$ in *E. coli*). Diffusion therefore supplies a cell within milliseconds to seconds, but cannot supply a tissue more than a fraction of a millimetre thick: larger organisms need circulation, and large cells need internal transport along the cytoskeleton (7.3).

![Mean time to diffuse a distance x in three dimensions, t = x²/(6D), for O₂, glucose and myoglobin in water and for green fluorescent protein in the cytoplasm of a mammalian cell. Bacteria (about 1 µm) are crossed in well under a millisecond by small molecules; eukaryotic cells (10–100 µm) in milliseconds to seconds; a distance of 1 cm takes hours even for O₂](./plots/diffusion-time.py)

### 1.1.3. Three Domains of Life and the Ways of Obtaining Energy and Carbon

Comparison of ribosomal RNA sequences (Woese, 1977) divides all cellular life into three domains: Bacteria, Archaea and Eukarya. The older division into six kingdoms (Bacteria, Archaea, Protista, Fungi, Plantae, Animalia), still found in many textbooks, mixes levels: Bacteria and Archaea are domains, Fungi, Plantae and Animalia are lineages within Eukarya, and "Protista" is not a natural group but a collection of all eukaryotes that are not fungi, plants or animals. Phylogenies are treated in [Evolutionary Biology](/7.10).

Biochemically more useful than taxonomy is the classification by the source of energy and of carbon (Lehninger's "all organisms require energy and carbon").

**Definition 1.1.2** Organisms that trap and use sunlight as their energy source are **phototrophs**; organisms that obtain energy by oxidizing chemical fuels are **chemotrophs**. Organisms that make all their biomolecules from $\ce{CO2}$ are **autotrophs**; organisms that require organic nutrients made by other organisms as their carbon source are **heterotrophs**. Chemotrophs that oxidize inorganic fuels ($\ce{H2}$, $\ce{H2S}$, $\ce{S}$, $\ce{NH4+}$, $\ce{F\mathrm{e}^2+}$) are lithotrophs; those that oxidize organic fuels are organotrophs.

![Classification of organisms by energy source (light or chemical fuels) and carbon source. Phototrophs are autotrophic (plants, algae, cyanobacteria, purple and green sulfur bacteria) or heterotrophic (purple non-sulfur bacteria, heliobacteria); chemotrophs are lithotrophs (hydrogen-, sulfur-, ammonia- and iron-oxidizing bacteria and many archaea, most of them autotrophic) or organotrophs (animals, fungi, most protists and most bacteria)](./plots/trophic-modes.py)

The two axes are independent: purple non-sulfur bacteria capture light but take their carbon from organic acids, whereas nitrifying bacteria fix $\ce{CO2}$ with energy from the oxidation of ammonia. Ultimately, almost all biological energy comes from sunlight, captured by photosynthesis (7.1.24) and passed on as reduced organic compounds and $\ce{O2}$ to the chemotrophs, which return $\ce{CO2}$ and $\ce{H2O}$ (7.1.16).

### 1.1.4. Bacterial and Eukaryotic Cells

*Escherichia coli*, the best-studied organism, shows the bacterial plan:

| Structure | Composition | Function |
|---|---|---|
| Cell envelope: outer membrane (Gram-negative only), peptidoglycan wall, plasma membrane | lipid + protein; peptidoglycan; lipid + protein | protection; mechanical support against osmotic pressure; permeability barrier, transport, energy transduction |
| Nucleoid | DNA + protein | genetic information (one circular chromosome of 4.6 Mbp; plasmids) |
| Ribosomes | RNA + protein | protein synthesis |
| Pili | protein | adhesion, conjugation |
| Flagella | protein | motility |
| Cytoplasm | aqueous solution | site of metabolism |

Eukaryotic cells are typically $10^3$–$10^4$ times larger in volume, and they solve the problems of size by compartmentation. The nucleus protects the DNA and separates transcription from translation, with traffic through nuclear pores; mitochondria (in nearly all eukaryotes) and chloroplasts (in plants and algae) carry out energy transduction; the endoplasmic reticulum and Golgi apparatus synthesize, modify and sort membrane and secreted proteins; lysosomes (vacuoles in plants) degrade unneeded molecules; peroxisomes oxidize fatty acids and destroy $\ce{H2O2}$. Separating energy-yielding from energy-consuming reactions in different compartments lets the cell maintain different conditions side by side. Plant cells additionally have a cellulose wall, plasmodesmata, a large central vacuole and glyoxysomes (specialized peroxisomes of germinating seeds, 7.1.25); animal cells have lysosomes and no wall. Some differentiated cells lose their nucleus altogether (mammalian erythrocytes).

The cytoplasm is organized by the *cytoskeleton*, three kinds of protein filaments: actin filaments (about 7 nm), microtubules (about 25 nm) and intermediate filaments (about 10 nm). They give the cell its shape, separate the chromosomes at division, organize the organelles, provide tracks for transport by motor proteins and produce cell movement. Organelles and the cytoskeleton are treated in [Cell Biology](/7.3).

### 1.1.5. Supramolecular Structures and the Crowded Cell

The molecular organization of a cell is hierarchical: small monomeric units are joined covalently into macromolecules, macromolecules assemble noncovalently into supramolecular complexes, and these build organelles and cells (course map above). The noncovalent level is the one that makes biological structure both stable and dynamic: ribosomes, chromatin, membranes and the cytoskeleton are held together by many weak interactions (7.1.2), so they can assemble spontaneously, change shape and come apart.

Biochemists study molecules mostly in vitro, purified in dilute solution, because only there can one molecular species be isolated and measured. Inside the cell conditions are very different: the cytoplasm of *E. coli* contains about 300–400 g of macromolecules per litre, occupying 20–30 % of the volume. Such *macromolecular crowding* lowers diffusion coefficients, raises the effective concentrations (activities) of large molecules and favours association and compact folding. Results obtained in vitro must therefore be checked in vivo; methods for doing so (fluorescent reporters, cryo-electron tomography, single-molecule tracking) recur throughout the biology courses.

## 1.2. Chemical Foundations

### 1.2.1. Elements and Functional Groups

Of the more than 90 naturally occurring elements, about 30 are essential to animals. Four, H, O, C and N, make up more than 99 % of the mass of most cells; they are the lightest elements that form one, two, four and three covalent bonds, respectively, and they form strong bonds. Carbon is central: it forms single bonds with H and with up to four other carbon atoms, and double and triple bonds, so it can build linear, branched and cyclic skeletons of unlimited variety. Single bonds allow free rotation; double bonds are rigid and planar, which fixes the geometry of molecules such as fatty acids (7.1.12). P and S (as phosphate esters, thioesters and thiols) and the ions $\ce{Na+}$, $\ce{K+}$, $\ce{Mg^2+}$, $\ce{Ca^2+}$ and $\ce{Cl-}$ are the other bulk elements; trace elements such as Fe, Cu, Zn, Mn, Co, Mo, Se and I are mostly bound in proteins as catalytic or structural cofactors (7.1.3, 7.1.8).

The chemistry of a biomolecule is that of its functional groups. Most biomolecules carry several:

| Group | Structure | Examples |
|---|---|---|
| hydroxyl | $\ce{R-OH}$ | alcohols, sugars, Ser, Thr |
| carbonyl | $\ce{R-CHO}$ (aldehyde), $\ce{R2C=O}$ (ketone) | open-chain sugars, pyruvate |
| carboxyl | $\ce{R-COOH}$ ($\ce{R-COO-}$ at pH 7) | amino acids, fatty acids |
| amino | $\ce{R-NH2}$ ($\ce{R-NH3+}$ at pH 7) | amino acids, amino sugars |
| amido | $\ce{R-CO-NH-R'}$ | peptide bond, Asn, Gln |
| guanidinium, imidazole | | Arg, His |
| sulfhydryl (thiol), disulfide | $\ce{R-SH}$, $\ce{R-S-S-R'}$ | Cys, cystine, coenzyme A |
| thioester | $\ce{R-CO-S-R'}$ | acetyl-CoA |
| ester, ether | $\ce{R-CO-O-R'}$, $\ce{R-O-R'}$ | triacylglycerols, plasmalogens |
| phosphoryl, phosphoanhydride | $\ce{R-O-PO3^2-}$; two phosphoryl groups sharing an O atom | sugar phosphates; ATP |

Acetyl-coenzyme A alone contains amino, hydroxyl, amido, phosphoanhydride, phosphate ester and thioester groups; its chemistry is the subject of much of Part II.

### 1.2.2. A Universal Set of Small Molecules and Their Polymers

Dissolved in the cytosol is a collection of perhaps a few thousand small molecules ($M_{\mathrm{r}}$ about 100–500): amino acids, nucleotides, sugars and their phosphorylated derivatives, mono-, di- and tricarboxylic acids, cofactors. The same compounds, made and degraded by the same central pathways, occur in essentially all cells; this *metabolome* is one of the clearest signs of the common origin of life.

**Definition 1.2.1** Polymers with molecular masses above about 5000 built from small monomeric units are called **macromolecules**; shorter polymers are called oligomers. Assemblies of macromolecules held together by noncovalent interactions, such as ribosomes, chromatin, membranes and multienzyme complexes, are called **supramolecular complexes**.

| Macromolecule | Monomer | Linkage (formed by condensation, broken by hydrolysis) | Typical size | Fraction of *E. coli* cell mass |
|---|---|---|---|---|
| proteins | 20 amino acids | peptide bond (7.1.3) | $10^2$–$10^4$ residues | 15 % |
| nucleic acids | 4 ribo- or deoxyribonucleotides | 3′,5′-phosphodiester bond (7.1.11) | $10^2$ (tRNA) to $10^8$ (chromosomal DNA) nucleotides | DNA 1 %, RNA 6 % |
| polysaccharides | monosaccharides | glycosidic bond (7.1.10) | up to $10^5$ residues, linear or branched | 3 % |
| lipids (not polymers) | fatty acids, glycerol, sphingosine, isoprene | ester and amide bonds | $M_{\mathrm{r}} < 2000$, assemble into membranes | 2 % |

The remainder of the cell mass is water (70 %), small organic molecules (about 2 %) and inorganic ions (about 1 %). Proteins and nucleic acids are *informational macromolecules*: their monomer sequence is not repetitive but specified, and it determines their three-dimensional structure and function. Polysaccharides and lipids serve as energy stores, structural elements and, as parts of glycoconjugates and membranes, recognition signals.

**Remark 1.2.1** The *relative molecular mass* $M_{\mathrm{r}}$ (molecular weight) is the mass of a molecule relative to $1/12$ of the mass of an atom of $^{12}\mathrm{C}$; it is a pure number. The *molecular mass* $m$ of the same molecule is expressed in daltons, $1\,\mathrm{Da} = 1\,\mathrm{u} = 1.660\,54 \times 10^{-27}\,\mathrm{kg}$. A protein therefore "has $M_{\mathrm{r}} = 50\,000$" or "has a mass of 50 kDa", never "$M_{\mathrm{r}} = 50\,000$ Da"; for the mass of a whole cell or organelle one uses grams (an *E. coli* cell: about 1 pg).

### 1.2.3. Three-Dimensional Structure: Configuration and Conformation

The function of a biomolecule depends on its three-dimensional structure. Organic chemistry ([6.5.4](/6.5.4), [6.5.5](/6.5.5)) distinguishes two kinds of spatial arrangement. A **configuration** is a fixed arrangement of atoms that can be changed only by breaking covalent bonds: the cis and trans isomers about a double bond (maleate and fumarate; 11-cis- and all-trans-retinal, whose interconversion by light is the primary event of vision, 7.1.14), and the two **enantiomers** of a molecule with a chiral centre. A **conformation** is an arrangement that can be changed by rotation about single bonds without breaking any bond, such as the staggered and eclipsed conformations of ethane or the folded and unfolded states of a protein (7.1.6).

**Stereoisomers** of a chiral compound have identical physical properties in an achiral environment, but cells are not achiral: enzymes and receptors are built of L-amino acids, so their binding sites are themselves chiral, and they distinguish stereoisomers as a hand distinguishes a right from a left glove. Biological systems therefore almost always make and use only one stereoisomer, and stereoisomers usually differ in their biological effects. Two classic examples: (*R*)-carvone smells of spearmint and (*S*)-carvone of caraway, because they bind to different olfactory receptors; and the sweetener aspartame, L-aspartyl-L-phenylalanine methyl ester (1), tastes sweet, whereas its diastereomer L-aspartyl-D-phenylalanine methyl ester (2) is bitter.

```smiles
N[C@@H](CC(=O)O)C(=O)N[C@@H](Cc1ccccc1)C(=O)OC 1
N[C@@H](CC(=O)O)C(=O)N[C@H](Cc1ccccc1)C(=O)OC 2
```

Interactions between biomolecules are thus stereospecific: a macromolecule has a binding pocket into which only a molecule of complementary shape, charge distribution and hydrogen-bonding pattern fits well. This complementarity, achieved with many weak interactions, is the molecular basis of enzyme specificity (7.1.8), of antibody–antigen recognition and ligand binding (7.1.7) and of signal reception (7.1.14).

## 1.3. Physical Foundations

### 1.3.1. Living Organisms Exist in a Dynamic Steady State

A living cell is an **open system** ([6.3.18](/6.3.18#sec-18.4)): it exchanges matter and energy with its surroundings and is never at equilibrium with them. Its composition nevertheless stays remarkably constant.

**Definition 1.3.1 (Dynamic steady state)** The state of a living system in which the concentrations of its components remain essentially constant although each component is continually synthesized and degraded, the rates of formation and removal being equal, is called the **dynamic steady state**.

The blood glucose concentration of a healthy person stays near 5 mM although glucose is constantly taken up by tissues and released by the liver; the ATP pool of a human body is only some tens of grams, yet the body hydrolyses and resynthesizes roughly its own mass of ATP every day. A steady state far from equilibrium can be maintained only by a continuous flow of energy: as soon as the flow stops, the system relaxes to equilibrium, which for a cell means death. The thermodynamics of such states (entropy production, dissipative structures) is treated in [6.3.18](/6.3.18).

### 1.3.2. Energy Coupling

Organisms take energy from the environment as light or chemical fuel and convert it into the forms they need: chemical energy of bonds and concentration gradients, electrical energy of membrane potentials, mechanical work of muscles and flagella, heat. In every conversion some energy is degraded to heat, and the entropy of the system plus surroundings increases; the order of a living cell is paid for by a larger increase in the entropy of its surroundings.

Whether a reaction can occur is decided by the change in **Gibbs free energy**, $\Delta G = \Delta H - T\Delta S$ ([6.1.6](/6.1.6#sec-6.4.7)): reactions with $\Delta G < 0$ are *exergonic* and can proceed spontaneously, those with $\Delta G > 0$ are *endergonic*. The standard reaction Gibbs energy is related to the **equilibrium constant** by $\Delta_{\mathrm{r}}G^\circ = -RT\ln K$ ([6.3.7](/6.3.7#sec-7.2)); biochemists use a standard state at pH 7, written $\Delta_{\mathrm{r}}G'^{\circ}$ and $K'$ (7.1.16). The synthesis of macromolecules, the formation of concentration gradients and mechanical work are all endergonic. They are made to proceed by **coupled reactions** ([6.3.7](/6.3.7#sec-7.6.2)) in which an endergonic process shares an intermediate with a more strongly exergonic one, so that the overall $\Delta G$ is negative. The phosphorylation of glucose is a typical example:

$$
\begin{aligned}
&\text{glucose} + \mathrm{P_i} \to \text{glucose 6-phosphate} + \ce{H2O} && \Delta_{\mathrm{r}}G'^{\circ} = +13.8\,\mathrm{kJ\,mol^{-1}} \\
&\ce{ATP + H2O -> ADP} + \mathrm{P_i} && \Delta_{\mathrm{r}}G'^{\circ} = -30.5\,\mathrm{kJ\,mol^{-1}} \\
&\text{glucose} + \ce{ATP} \to \text{glucose 6-phosphate} + \ce{ADP} && \Delta_{\mathrm{r}}G'^{\circ} = -16.7\,\mathrm{kJ\,mol^{-1}}
\end{aligned}
$$

Because standard Gibbs energies add, the coupled reaction has an equilibrium constant $K'$ that is the product of the two, about $10^{-2.4} \times 10^{5.3} \approx 10^{2.9}$ at $25\,^\circ\mathrm{C}$. The coupling is not a matter of bookkeeping: hexokinase transfers the phosphoryl group directly from ATP to glucose, so that no free phosphate is ever formed. ATP, together with the reduced electron carriers NADH and NADPH, is the universal energy currency: these molecules are regenerated by catabolism, using energy from sunlight or fuels, and are kept at concentrations far above their equilibrium values, so that their consumption can drive biosynthesis, transport and movement (7.1.16).

### 1.3.3. Enzymes and the Organization of Metabolism

A favourable $\Delta G$ says nothing about the rate. Most biological reactions have high activation barriers: the peptide bonds of a protein are thermodynamically unstable in water, yet their uncatalysed hydrolysis takes centuries. A cell cannot speed up reactions by heating (macromolecules would denature) or by raising concentrations (too costly), so it uses the two strategies that all organisms share: coupling to exergonic reactions (1.3.2) and **catalysis**.

Enzymes are biological catalysts, nearly all proteins (some are RNAs). By binding the **transition state** more tightly than the substrate, they lower the Gibbs energy of activation $\Delta^{\ddagger}G$ ([6.3.16](/6.3.16)); since the rate constant is proportional to $\mathrm{e}^{-\Delta^{\ddagger}G/RT}$, every $5.7\,\mathrm{kJ\,mol^{-1}}$ ($RT\ln 10$ at $25\,^\circ\mathrm{C}$) of lowering raises the rate tenfold, and rate enhancements of $10^{10}$–$10^{17}$ are common (7.1.8). An enzyme changes the rate, not the equilibrium: $\Delta_{\mathrm{r}}G'^{\circ}$ and $K'$ are properties of the reactants and products alone. Enzymes offer three things ordinary catalysts do not: large accelerations under mild conditions, high specificity for substrate and reaction, and the possibility of regulation.

**Definition 1.3.2 (Metabolism)** The entire set of enzyme-catalysed transformations of organic compounds in a living organism is called its **metabolism**.

Metabolic reactions are organized in pathways, series of consecutive reactions in which the product of one enzyme is the substrate of the next; breakdown pathways that release energy and synthetic pathways that consume it run side by side (Part II). Signal transduction pathways, built from the same kinds of proteins, transmit information instead of matter (7.1.14). Because the cell has only a limited supply of each metabolite, pathways must be regulated. The simplest and most common control is negative feedback: the end product of a pathway inhibits the enzyme that catalyses its first committed step, so that the pathway slows down as soon as the product accumulates (7.1.9, 7.1.17).

## 1.4. Genetic and Evolutionary Foundations

### 1.4.1. The Flow of Genetic Information

The near-perfect fidelity with which organisms reproduce rests on DNA. Its linear sequence of four nucleotides, copied by complementary base pairing, specifies the sequence of every RNA and, through the genetic code, of every protein; the protein sequence in turn determines how the chain folds into a three-dimensional structure and therefore what the protein does (7.1.5–7.1.6). This flow of information, DNA → RNA → protein, is the **central dogma** of molecular biology: DNA stores the information, RNA transmits it, and proteins express it as function. Replication, transcription and translation are the subject of [Molecular Biology](/7.2).

### 1.4.2. Mutation, Selection and Gene Duplication

DNA is copied with an error rate of about one in $10^9$–$10^{10}$ nucleotides per replication, and it is damaged chemically (7.1.11); the surviving errors are mutations. Most are neutral or harmful; those that give an advantage in a given environment are more likely to be passed on. This is natural selection, the mechanism of evolution proposed by Darwin and Wallace, now understood in molecular terms ([Evolutionary Biology](/7.10)). New enzymatic activities typically arise by gene duplication followed by divergence: one copy keeps the old function while the other accumulates mutations and may acquire a related activity. Families of proteins with similar sequences and related functions, such as the serine proteases or the dehydrogenases, are the result (homologs, 7.1.4).

### 1.4.3. Chemical Evolution and the RNA World

Life on Earth arose about 3.5–4 billion years ago, within a few hundred million years after the oceans formed. Miller and Urey (1953) showed that amino acids form readily from a reducing gas mixture subjected to electric discharges, and later experiments produced nucleobases, sugars and lipids under plausible prebiotic conditions. The key step was the appearance of a molecule able to catalyse its own replication. Proteins are good catalysts but cannot be copied; DNA is a good template but a poor catalyst. RNA can be both: it carries sequence information and, as ribozymes, catalyses reactions, including peptide-bond formation in the ribosome. According to the *RNA world hypothesis*, early life was based on self-replicating RNA; proteins later took over most catalysis, and DNA, more stable chemically, took over information storage. The central role of ribonucleotide-derived cofactors (ATP, NAD, FAD, coenzyme A) throughout metabolism is often read as a relic of this world.

### 1.4.4. Endosymbiosis and the Origin of Eukaryotes

The first cells were anaerobic chemotrophs. Around 2.7–2.4 billion years ago, oxygenic photosynthesis by cyanobacteria began to fill the atmosphere with $\ce{O2}$, which created both a toxic hazard and a far richer energy source: complete oxidation of glucose with $\ce{O2}$ yields more than ten times as much ATP as fermentation (7.1.18, 7.1.23).

Eukaryotes arose about 2 billion years ago. According to the *endosymbiotic theory*, mitochondria descend from an aerobic α-proteobacterium engulfed by a host cell, and chloroplasts from a cyanobacterium taken up later by an early eukaryote of the plant lineage. The evidence is strong: both organelles have two membranes, their own circular DNA, ribosomes of the bacterial type and a division mechanism derived from bacterial cell division, and their genes are most closely related to those of these bacterial groups. Genome analyses of the last decade have also identified the host: the closest known relatives of eukaryotes are the Asgard archaea. On this view the tree of life has two primary domains, Bacteria and Archaea, and eukaryotes arose from within the Archaea by the merger of an archaeal host with a bacterial endosymbiont; this replaces the original picture of three equally old domains.

### 1.4.5. Genomics

Since 1995 the complete genome sequences of tens of thousands of organisms have been determined, among them *E. coli* (4.6 Mbp, about 4300 protein-coding genes), budding yeast (12 Mbp, about 6000 genes) and humans (3.1 Gbp, about 20 000 protein-coding genes, less than 2 % of the DNA). Comparison of genomes reveals the universal core of biochemistry, the genes shared by all cells for replication, transcription, translation and central metabolism, and the lineage-specific innovations of each group. Genomics, together with the large-scale study of the proteins (proteomics, 7.1.4) and metabolites of a cell, is the starting point of [Bioinformatics](/7.8) and [Systems Biology](/7.9).

## Summary

| Foundation | Key facts | Where it returns |
|---|---|---|
| Cellular | cells: plasma membrane, cytoplasm, nucleoid or nucleus; prokaryotes vs eukaryotes (Definition 1.1.1); size limited by diffusion, $t \approx x^2/(6D)$ (Example 1.1.1); phototrophs/chemotrophs, autotrophs/heterotrophs (Definition 1.1.2); compartmentation and crowding | 7.1.13, 7.1.23–7.1.25, 7.3 |
| Chemical | H, O, C, N (> 99 % of mass); functional groups; monomers → macromolecules → supramolecular complexes (Definition 1.2.1); $M_{\mathrm{r}}$ vs Da (Remark 1.2.1); configuration vs conformation; stereospecific binding | 7.1.2–7.1.12 |
| Physical | open system in a dynamic steady state (Definition 1.3.1); $\Delta G$, $\Delta_{\mathrm{r}}G'^{\circ} = -RT\ln K'$, coupling through ATP; enzymes lower $\Delta^{\ddagger}G$ (×10 per $5.7\,\mathrm{kJ\,mol^{-1}}$) but not $K'$; metabolism (Definition 1.3.2) organized in pathways with feedback control | 7.1.8–7.1.9, 7.1.16–7.1.17 |
| Genetic and evolutionary | DNA → RNA → protein; sequence → structure → function; mutation and selection, gene duplication; RNA world; endosymbiotic origin of mitochondria and chloroplasts, archaeal host of eukaryotes | 7.1.4, 7.1.11, 7.2, 7.10 |

The two threads of the course: Part I asks of each class of biomolecule which chemical properties it has, what structure they impose and what function the structure makes possible; Part II asks of each pathway how its energy is balanced and how feedback and hormones control its flux.

## Questions

1. A spherical eukaryotic cell grows from 10 µm to 100 µm in diameter while its metabolic rate per unit volume stays constant. By what factors do (a) the surface-to-volume ratio and (b) the time for O₂ to diffuse from the membrane to the centre change? Why do large cells such as amphibian eggs or neurons nevertheless exist?

   **Answer** (a) The surface-to-volume ratio of a sphere is $3/r$, so it falls tenfold. (b) The diffusion time grows as $r^2$, a hundredfold: with $D = 2 \times 10^{-9}\,\mathrm{m^2\,s^{-1}}$ and $t \approx r^2/(6D)$, from about $2\,\mathrm{ms}$ to about $0.2\,\mathrm{s}$. Large cells survive by having a low metabolic rate per volume (egg yolk is mostly stored material), by active transport along the cytoskeleton (axonal transport in neurons), or by an elongated shape that keeps every point close to the membrane.

2. Classify (a) a cyanobacterium, (b) *Nitrosomonas*, which oxidizes $\ce{NH4+}$ to $\ce{NO2-}$ and fixes $\ce{CO2}$, (c) a human hepatocyte, and (d) a purple non-sulfur bacterium growing in light on succinate.

   **Answer** (a) Photoautotroph. (b) Chemolithoautotroph: energy from an inorganic fuel, carbon from $\ce{CO2}$. (c) Chemo-organoheterotroph: energy and carbon both from organic compounds. (d) Photoheterotroph: energy from light, carbon from an organic acid.

3. Hexokinase couples glucose phosphorylation ($\Delta_{\mathrm{r}}G'^{\circ} = +13.8\,\mathrm{kJ\,mol^{-1}}$) to ATP hydrolysis ($-30.5\,\mathrm{kJ\,mol^{-1}}$). Calculate $K'$ for the uncoupled phosphorylation with $\mathrm{P_i}$ and for the coupled reaction at $25\,^\circ\mathrm{C}$. If $[\mathrm{P_i}] = 5\,\mathrm{mM}$, what ratio [glucose 6-phosphate]/[glucose] could the uncoupled reaction reach at equilibrium?

   **Answer** $K' = \mathrm{e}^{-\Delta_{\mathrm{r}}G'^{\circ}/RT}$ with $RT = 2.479\,\mathrm{kJ\,mol^{-1}}$: uncoupled $K' = \mathrm{e}^{-5.57} = 3.8 \times 10^{-3}\,\mathrm{M^{-1}}$; coupled $K' = \mathrm{e}^{6.74} = 8.4 \times 10^{2}$. Uncoupled, $[\text{G6P}]/[\text{Glc}] = K'[\mathrm{P_i}] = 3.8 \times 10^{-3} \times 5 \times 10^{-3} \approx 2 \times 10^{-5}$: essentially no product. Coupled to ATP the ratio at equilibrium is $K'[\mathrm{ATP}]/[\mathrm{ADP}]$, of the order of $10^3$–$10^4$ in a cell.

4. An enzyme accelerates a reaction $10^{12}$-fold at $25\,^\circ\mathrm{C}$. By how much does it lower $\Delta^{\ddagger}G$? Does it change the equilibrium constant of the reaction, and why not?

   **Answer** $\Delta\Delta^{\ddagger}G = RT\ln 10^{12} = 12 \times 5.71 = 68.5\,\mathrm{kJ\,mol^{-1}}$. It does not change $K'$: the enzyme lowers the barrier for the forward and reverse reactions by the same amount (it is not consumed and does not change the Gibbs energies of reactants and products), so both rate constants increase by the same factor and their ratio, $K'$, is unchanged.

5. List three lines of evidence that mitochondria derive from bacteria. Why do mitochondria nevertheless depend on the nucleus?

   **Answer** Mitochondria have two membranes (the inner one of bacterial origin, with cardiolipin), their own circular genome, 70S-type ribosomes sensitive to some antibacterial antibiotics, and their genes and proteins are most similar to those of α-proteobacteria; they divide by fission. Most of the genes of the endosymbiont were lost or transferred to the nucleus during evolution: human mtDNA encodes only 13 proteins, so the more than 1000 other mitochondrial proteins are made in the cytosol from nuclear genes and imported.
