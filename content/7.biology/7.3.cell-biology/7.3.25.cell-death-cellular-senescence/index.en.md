---
title: Cell Death and Cellular Senescence
description: Death as a cell fate; accidental, regulated and programmed cell death and the NCCD classification; the morphology and biochemical markers of apoptosis and its functions; the core machinery from the ced genes of C. elegans to initiator and executioner caspases; the extrinsic pathway (death receptors, DISC, FLIP) and the intrinsic pathway (Bcl-2 family, MOMP, apoptosome, XIAP and Smac), survival signals and a model of the caspase switch with its variable delay; the clearance of apoptotic cells; necroptosis, pyroptosis, ferroptosis and other forms of regulated necrosis; cellular senescence, the Hayflick limit and a stochastic model of telomere shortening, markers, inducers and the SASP, senescence as a barrier to cancer, and senescent cells in organismal aging.
---

A cell in a multicellular organism has four fates: it can divide, rest in G0, differentiate or die. The last is not a failure of the others but a decision taken by the same kind of molecular machinery: an adult human loses at least a million cells per second by a tidy, self-inflicted death and replaces them by division, and in development whole structures are carved out by cell death. This chapter treats death and its relative, cellular senescence, as the two ways in which a metazoan cell permanently removes itself from the proliferating population. We first classify the ways cells die (25.1), describe the features of apoptosis (25.2), its core machinery (25.3), the two pathways that activate it and their switch-like dynamics (25.4) and the removal of the corpses (25.5); then the forms of regulated necrosis that kill cells with inflammation (25.6); and finally senescence, the permanent arrest that counts divisions with telomeres and that links tumor suppression to aging (25.7). The molecular outline of apoptosis was introduced in [7.1.15](/7.1.15#sec-15.6.3) and the role of mitochondria in [7.1.23](/7.1.23#sec-23.5.3); the controls of proliferation whose failure triggers death or senescence (survival factors, the DNA damage response, p53) are in [7.3.22](/7.3.22); autophagy is in [7.3.11](/7.3.11); the consequences of escaping both death and senescence, cancer, are the subject of [7.3.26](/7.3.26).

## 25.1. Cell Fates and the Classification of Cell Death

### 25.1.1. Death as a Cell Fate

In a tissue that is neither growing nor shrinking, birth and death must balance. If cells divide at rate $b$ and die at rate $\delta$ per cell, the cell number obeys $\mathrm{d}N/\mathrm{d}t = (b - \delta)N$, so a constant size requires $b = \delta$ exactly; any persistent imbalance grows or shrinks the tissue exponentially. Tissues therefore regulate both rates. When part of a rat liver is removed, hepatocytes divide until the mass is restored; when a rat is given phenobarbital, which stimulates hepatocyte division, the liver enlarges, and when the drug is withdrawn apoptosis increases until the original cell number returns within about a week. In the intestinal epithelium, where cells are produced in the crypts and shed at the villus tips every 4–5 days, and in the blood, where about $10^{11}$ neutrophils die each day, death is a routine part of tissue homeostasis.

Cell death also occurs in unicellular organisms (bacterial toxin–antitoxin systems, abortive infection that kills a phage-infected cell and protects its clone) and in plants (the hypersensitive response to pathogens, the hollowing of xylem vessels, the senescence of leaves and petals; [7.13](/7.13)), but by mechanisms that differ from those of animals. Apoptosis, the main subject of this chapter, is found only in animals.

### 25.1.2. Accidental and Regulated Cell Death

Morphologists first classified cell death by appearance (Schweichel and Merker 1973): type I, apoptosis, with shrinkage, chromatin condensation and fragmentation into bodies taken up by phagocytes; type II, autophagic death, with extensive vacuolization of the cytoplasm; type III, necrosis, with swelling and rupture and no phagocytic clearance. The Nomenclature Committee on Cell Death (NCCD), whose 2018 recommendations were signed by more than 160 authors, replaced this by a classification based on molecular mechanisms, because cells that look alike can die by different mechanisms and vice versa.

**Definition 25.1.1 (Accidental, Regulated and Programmed Cell Death)** **Accidental cell death** is the instantaneous and catastrophic death of cells exposed to severe physical (high temperature, pressure, osmotic forces), chemical (extreme pH) or mechanical (shear) insults; it cannot be prevented or modulated by molecular interventions. **Regulated cell death** is cell death that relies on a dedicated molecular machinery and can therefore be delayed or accelerated by pharmacological or genetic interventions. **Programmed cell death** is regulated cell death that occurs without any exogenous perturbation, as a built-in effector of developmental programs or of physiological tissue turnover.

The other instances of regulated death are responses to stresses (DNA damage, ER stress, infection, loss of survival signals) that are too intense or too prolonged for adaptive responses to restore homeostasis. A cell is considered dead, by the NCCD's operational criteria, when its plasma membrane has been irreversibly permeabilized or the cell has fragmented completely; before this point of no return, some stressed cells that have begun to activate a death program can still recover.

**Definition 25.1.2 (Necrosis)** **Necrosis** is cell death with the morphology of swelling of the cell and its organelles (oncosis) followed by rupture of the plasma membrane and release of the cell contents, which provoke inflammation. It may be accidental, as after trauma or ischemia, or regulated, as in necroptosis and pyroptosis (25.6).

The contents released from necrotic cells, such as HMGB1, ATP, uric acid, DNA and heat shock proteins, act as *damage-associated molecular patterns* (DAMPs) on receptors of the innate immune system ([7.15](/7.15)). This, more than the manner of dying itself, is the physiological difference between apoptosis and necrosis: apoptosis removes cells silently, necrosis raises an alarm.

| NCCD mode of regulated death (2018) | Defining molecular event | Key mediators | Section |
|---|---|---|---|
| intrinsic apoptosis | MOMP, then caspases | Bax, Bak, cytochrome c, caspase-9, caspase-3 | 25.4.2 |
| extrinsic apoptosis | death receptor or dependence receptor signaling | Fas, TNFR1, caspase-8 | 25.4.1 |
| mitochondrial permeability transition–driven necrosis | opening of the permeability transition pore in the inner membrane | cyclophilin D | 25.6.4 |
| necroptosis | MLKL pores | RIPK1, RIPK3, MLKL | 25.6.1 |
| ferroptosis | iron-dependent lipid peroxidation | GPX4, ACSL4 | 25.6.3 |
| pyroptosis | gasdermin pores | caspase-1, -4, -5, -11, gasdermin D | 25.6.2 |
| parthanatos | PARP1 hyperactivation | PAR polymer, AIF, MIF | 25.6.4 |
| entotic cell death | engulfment of a living cell by a neighbor | Rho–ROCK, actomyosin | 25.6.4 |
| NETotic cell death | release of neutrophil extracellular traps | NADPH oxidase, PAD4 | 25.6.4 |
| lysosome-dependent cell death | lysosomal membrane permeabilization | cathepsins | 25.6.4 |
| autophagy-dependent cell death | requires the autophagy machinery | ATG proteins | 25.6.4 |
| immunogenic cell death | death that elicits adaptive immunity | calreticulin exposure, ATP, HMGB1 | 25.6.4 |

## 25.2. The Features of Apoptosis

### 25.2.1. Morphology

Kerr, Wyllie and Currie (1972) named **apoptosis**, from the Greek for the falling of leaves, after recognizing a common sequence of changes in dying cells of many tissues. The cell detaches from its neighbors and shrinks; its chromatin condenses into dense masses against the nuclear envelope (pyknosis) and the nucleus breaks into fragments (karyorrhexis); the cytoskeleton collapses and the cell surface forms blebs; finally a large cell breaks into membrane-enclosed fragments. Throughout, the plasma membrane remains intact and the organelles are largely preserved, so that nothing leaks.

**Definition 25.2.1 (Apoptotic Body)** An **apoptotic body** is a membrane-enclosed fragment of an apoptotic cell, 1–5 µm across, containing condensed cytoplasm, organelles and often nuclear fragments, which exposes phosphatidylserine and is engulfed by a phagocyte.

![Apoptosis and necrosis compared (schematic). Top, apoptosis: a normal cell shrinks while its chromatin condenses at the nuclear periphery; the cell surface blebs and the nucleus fragments; the cell breaks into membrane-enclosed apoptotic bodies that expose phosphatidylserine (small dots on the surface) as an "eat me" signal; a macrophage engulfs them and digests them in phagolysosomes, without inflammation. The plasma membrane stays intact throughout. Bottom, necrosis: the cell and its organelles, especially mitochondria, swell; the plasma membrane ruptures and the contents, including damage-associated molecular patterns, leak into the tissue; neutrophils and macrophages are recruited and cause inflammation](./plots/death-morphology.py)

### 25.2.2. Biochemical Markers

Because apoptotic cells are cleared within an hour or so, they are rare in tissue sections even where many cells die; quantitative work relies on markers, each of which detects one step of the program.

**Definition 25.2.2 (DNA Ladder, Annexin V Staining and TUNEL Assay)** A **DNA ladder** is the pattern of DNA fragments of about 180–200 bp and its multiples seen on agarose gel electrophoresis of DNA from apoptotic cells, produced when the caspase-activated DNase cuts the linker DNA between nucleosomes. **Annexin V** staining detects phosphatidylserine on the outer leaflet of the plasma membrane with fluorescently labeled annexin V, a protein that binds phosphatidylserine in the presence of $\ce{Ca^2+}$. The **TUNEL assay** (terminal deoxynucleotidyl transferase dUTP nick end labeling) labels the free $3'$-OH ends of fragmented DNA in situ, in single cells, by adding labeled dUTP with **terminal deoxynucleotidyl transferase**.

Annexin V is usually combined with a membrane-impermeant DNA dye such as propidium iodide and measured by **flow cytometry** ([7.3.3](/7.3.3)): living cells are negative for both; early apoptotic cells bind annexin V but exclude the dye, because their membrane is still intact; late apoptotic and necrotic cells are positive for both, because the membrane has failed (in culture, without phagocytes, apoptotic cells eventually lyse, which is called secondary necrosis). The ladder reflects the periodicity of nucleosomes, the cut sites being the accessible linkers ([7.2.4](/7.2.4)); necrotic DNA, digested at random, gives a smear.

| Marker | Step detected | Method |
|---|---|---|
| cytochrome c release, loss of mitochondrial membrane potential | MOMP | imaging of cytochrome c–GFP, dyes such as TMRM |
| caspase activity | caspase activation | fluorogenic peptide substrates (DEVD for caspase-3 and -7), antibodies to cleaved caspase-3 or cleaved PARP1 |
| phosphatidylserine exposure | caspase cleavage of the flippase and scramblase | annexin V with propidium iodide |
| DNA fragmentation | CAD activity | DNA ladder (populations), TUNEL (single cells), sub-G1 peak in flow cytometry |
| condensation, fragmentation | late morphology | microscopy, nuclear dyes |

### 25.2.3. Functions

- Sculpting. The digits of the mouse and human hand form as the cells between them die; in ducks, whose interdigital webs persist, less death occurs there. The tadpole tail is removed at metamorphosis in response to thyroid hormone, and in mammalian embryos the Müllerian ducts regress in males under the influence of anti-Müllerian hormone.
- Matching numbers. About half of the motor neurons and many other neurons made in the vertebrate embryo die soon after they reach their targets: they compete for limited amounts of neurotrophic factors made by the target, and those that obtain too little die (the neurotrophic hypothesis of Levi-Montalcini and Hamburger, who discovered NGF). The same competition for survival signals adjusts cell numbers in other tissues ([7.3.22](/7.3.22#sec-22.1.1)).
- Quality control. Developing T and B lymphocytes that fail to make a useful antigen receptor, or make a self-reactive one, die by apoptosis, as do most lymphocytes expanded in an immune response once the infection is cleared; cells with irreparable DNA damage, cells infected by viruses (killed by cytotoxic lymphocytes) and cells that lose contact with the extracellular matrix (anoikis) are also removed.
- Disease. Too much apoptosis contributes to the tissue loss after heart attack and stroke (in the penumbra around the necrotic core) and to neurodegeneration; too little contributes to autoimmunity and cancer (25.4.3; [7.3.26](/7.3.26)).

## 25.3. The Core Machinery

### 25.3.1. The Genetics of Cell Death in *C. elegans*

The nematode *Caenorhabditis elegans* develops by an invariant lineage, traced cell by cell by Sulston: of the 1090 somatic cells generated in the hermaphrodite, exactly 131 die, always the same ones, mostly neurons, soon after their birth. Horvitz and his colleagues screened for mutants in which these cells survived or died abnormally and assembled a genetic pathway (Nobel Prize 2002 to Brenner, Horvitz and Sulston):

$$
\text{EGL-1} \dashv \text{CED-9} \dashv \text{CED-4} \to \text{CED-3} \to \text{death}.
$$

In *ced-3* or *ced-4* loss-of-function mutants all 131 cells survive; in *ced-9* loss-of-function mutants many cells that should live die, and the embryo does not survive, unless *ced-3* or *ced-4* is also mutated (*ced-9* is epistatic upstream). EGL-1 is made in cells fated to die and releases CED-4 from CED-9. Cloning revealed a conserved pathway: CED-3 resembled the human interleukin-1β–converting enzyme (caspase-1), the founding member of the caspases; CED-9 resembled the human oncogene product Bcl-2 (and human Bcl-2 prevents death in worms); CED-4 resembled Apaf1; and EGL-1 is a BH3-only protein. A second set of genes (*ced-1*, *ced-2*, *ced-5*, *ced-6*, *ced-7*, *ced-10*, *ced-12*) is needed for the engulfment of the corpses by neighboring cells, in two parallel pathways that converge on the small GTPase CED-10, a Rac homolog that reorganizes actin for **phagocytosis** ([7.3.10](/7.3.10#sec-10.1.2)).

The mammalian pathway is more elaborate: mitochondria are interposed between the Bcl-2 family and Apaf1, and cytochrome c is required to activate Apaf1, which CED-4 does not need.

### 25.3.2. Caspases

**Caspases** cut their substrates after an aspartate, within a four-residue recognition motif (DEVD for caspase-3 and -7, IETD for caspase-8, LEHD for caspase-9), using a catalytic cysteine. They are made as inactive **zymogens** (procaspases) with an N-terminal prodomain, a large subunit (about 20 kDa) and a small subunit (about 10 kDa), and are activated in two different ways.

**Definition 25.3.1 (Initiator and Executioner Caspases)** **Initiator caspases** (caspase-8, -9, -10 and -2 in mammals) have long prodomains with protein interaction modules (death effector domains, DED, in caspase-8 and -10; caspase recruitment domains, CARD, in caspase-9 and -2); they exist as inactive monomers and are activated by dimerization when an adaptor complex brings several monomers together, after which they cleave themselves. **Executioner caspases** (caspase-3, -6 and -7) have short prodomains and exist as inactive dimers; they are activated by cleavage between the large and small subunits by an initiator caspase, and they cleave the hundreds of cellular proteins whose cleavage produces apoptosis.

A third group, the inflammatory caspases (caspase-1, -4 and -5 in humans, caspase-1 and -11 in mice), processes cytokines and gasdermin D in pyroptosis (25.6.2). (Caspase-14, sometimes listed among the executioners, is expressed in keratinocytes and acts in their terminal differentiation, not in apoptosis.)

The two modes of activation are the logic of the cascade. Activation of initiators by proximity converts an assembly event, the formation of an adaptor platform, into protease activity; activation of executioners by cleavage allows one active initiator to activate many executioners, so the cascade amplifies; and because cleavage is irreversible, so is the outcome. Executioner caspase-3 and -6 also cleave and activate further initiator and executioner molecules (caspase-8 and -9 by caspase-3, caspase-3 by caspase-6), a positive feedback that makes the cascade self-sustaining (25.4.6).

Among the substrates whose cleavage explains the features of 25.2:

| Substrate | Effect of cleavage |
|---|---|
| ICAD (inhibitor of CAD) | releases the caspase-activated DNase CAD, an **endonuclease** that enters the nucleus and cuts linker DNA (ladder) |
| **lamins** (by caspase-6) | disassembly of the **nuclear lamina** and nuclear fragmentation |
| ROCK1, PAK2, gelsolin | constitutive actomyosin contraction: blebbing |
| FAK, cadherins, catenins | detachment from matrix and neighbors |
| flippase ATP11C (inactivated), scramblase Xkr8 (activated) | phosphatidylserine exposure (25.5) |
| PARP1 and other repair enzymes | prevents futile repair and the depletion of NAD⁺ and ATP |
| Golgi and ER proteins, kinases (PKCδ, Raf1) | dismantling of organelles and survival signaling |

No single cleavage is necessary for death: blocking any one changes a feature of apoptosis but not the death of the cell.

## 25.4. Two Pathways to Caspase Activation

![The extrinsic and intrinsic pathways of apoptosis (SBGN activity flow; open arrows activate, bars inhibit). Extrinsic: death ligands such as FasL, TNF and TRAIL cluster their receptors, which recruit FADD and procaspase-8 into the DISC; FLIP inhibits caspase-8 activation in the DISC; active caspase-8 activates caspase-3 and -7 directly (type I cells) and cleaves Bid to tBid, which engages the mitochondria (type II cells). Intrinsic: DNA damage acting through p53, ER stress and the loss of survival signals activate BH3-only proteins; survival factors acting through PI3K and PKB inhibit them. BH3-only proteins inhibit the anti-apoptotic Bcl-2, Bcl-xL and Mcl-1 and activate Bax and Bak, which permeabilize the outer mitochondrial membrane (MOMP) and release cytochrome c and Smac/Omi. Cytochrome c builds the apoptosome, which activates caspase-9 and then caspase-3 and -7; Smac and Omi neutralize XIAP, which inhibits caspase-9 and caspase-3 and -7. Executioner caspases feed back on the initiators (dashed)](./plots/apoptosis-pathways.py)

### 25.4.1. The Extrinsic Pathway

**Definition 25.4.1 (Death Receptor and DISC)** A **death receptor** is a transmembrane receptor of the tumor necrosis factor receptor superfamily that carries a cytoplasmic death domain of about 80 residues and can trigger apoptosis when bound by its trimeric ligand: Fas (CD95, APO-1) binding Fas ligand, TNFR1 binding TNF, and TRAIL-R1 and -R2 (DR4 and DR5) binding TRAIL. The **death-inducing signaling complex** (DISC) is the assembly of clustered death receptors, the adaptor FADD (bound to the receptor through death domains) and procaspase-8 and -10 (bound to FADD through DEDs), in which the initiator caspases dimerize and are activated.

Fas ligand on cytotoxic T cells and natural killer cells kills infected or transformed target cells and removes activated lymphocytes at the end of an immune response; people with heterozygous dominant-negative mutations in the gene encoding Fas develop the autoimmune lymphoproliferative syndrome (ALPS), with enlarged lymph nodes and spleen and autoantibodies, and *lpr* and *gld* mice, which lack Fas and Fas ligand, have a similar disease. Structurally, at least two ligand trimers must cluster receptors to expose their death domains; FADD then nucleates filaments of caspase-8 through its DED, a mechanism that amplifies a small number of receptor complexes into many caspase dimers.

The *extrinsic pathway* of apoptosis (receptor → DISC → caspase-8 → executioner caspases) is restrained at several levels. FLIP (cellular FLICE-inhibitory protein) resembles caspase-8 but lacks the catalytic cysteine; incorporated into the DISC, it forms heterodimers with caspase-8 that cannot propagate the cascade, and its level sets the threshold of ligand needed to kill. TNFR1 shows that a death receptor need not kill at all: TNF binding normally builds a membrane-bound complex I (TRADD, RIPK1, TRAF2, cIAP1/2 and LUBAC), whose ubiquitin chains recruit IKK and activate **NF-κB** ([7.3.19](/7.3.19#sec-19.3.3)), which induces survival genes including FLIP. Only when NF-κB activation or the ubiquitination of RIPK1 fails does a cytoplasmic complex II with FADD and caspase-8 form and trigger apoptosis, or, if caspase-8 is inhibited, necroptosis (25.6.1).

Cells differ in how they relay the signal. In type I cells (such as lymphocytes) the DISC generates enough caspase-8 to activate caspase-3 directly. In type II cells (such as hepatocytes and many cancer cells) little caspase-8 is made, XIAP holds the executioners in check, and death requires amplification through the mitochondria: caspase-8 cleaves the BH3-only protein Bid, whose truncated form tBid activates Bax and Bak (25.4.3), and the resulting MOMP releases Smac to neutralize XIAP (25.4.4). Mice lacking Bid are resistant to Fas-induced liver failure.

### 25.4.2. The Intrinsic Pathway

Most apoptotic deaths in vertebrates, those caused by DNA damage, by loss of survival signals, by ER stress or during development, go through the mitochondria, by the *intrinsic pathway* (mitochondrial pathway) of apoptosis.

**Definition 25.4.2 (MOMP, Apaf1 and the Apoptosome)** **Mitochondrial outer membrane permeabilization** (MOMP) is the formation of openings in the outer mitochondrial membrane by oligomers of Bax and Bak that release the soluble proteins of the **intermembrane space**, including cytochrome c, Smac and Omi, into the cytosol. **Apaf1** (apoptotic protease-activating factor 1) is a cytosolic adaptor with an N-terminal CARD, a nucleotide-binding oligomerization domain and C-terminal WD40 repeats that bind cytochrome c. The **apoptosome** is the wheel-shaped heptamer of Apaf1 formed when cytochrome c binds Apaf1 and dATP (or ATP) is exchanged for its bound dADP; its central hub of seven CARDs recruits and activates caspase-9.

Cytochrome c, a carrier of the **respiratory chain** ([7.1.23](/7.1.23)), was identified as an apoptotic factor by Xiaodong Wang's group (1996), who fractionated a cell-free extract in which dATP activated caspase-3 and found that one of the required components was cytochrome c from the mitochondria; Apaf1 and caspase-9 were the other two. The protein thus has two unrelated jobs, electron transfer inside the mitochondrion and caspase activation outside it. About 85% of it is stored in the crista lumen, and its release requires both MOMP and the widening of the crista junctions ([7.3.12](/7.3.12#sec-12.2.2)).

Several features make MOMP the point of no return of the intrinsic pathway. MOMP is fast and complete: cytochrome c–GFP imaging (Goldstein et al. 2000) showed that within a single cell all mitochondria release their cytochrome c within about 5 minutes, whereas different cells in the same dish begin at widely different times, hours apart. MOMP is effectively irreversible: even if caspases are inhibited, a cell that has lost its cytochrome c from all mitochondria usually dies slowly from the bioenergetic failure (caspase-independent cell death), and the release of mitochondrial DNA through Bax/Bak macropores can activate cGAS–STING and inflammation. Only if a few mitochondria escape MOMP (minority MOMP, incomplete MOMP) can a cell recover, at the cost of DNA damage from the limited caspase activity, a possible source of mutations.

### 25.4.3. The Bcl-2 Family

**Definition 25.4.3 (Bcl-2 Family and BH3-Only Protein)** The **Bcl-2 family** is the family of proteins sharing one to four Bcl-2 homology (BH) domains that control MOMP. Its anti-apoptotic members (Bcl-2, Bcl-xL, Bcl-w, Mcl-1 and A1) have BH1–BH4 and inhibit MOMP; its pro-apoptotic effectors **Bax** and **Bak** (and the less understood Bok) have BH1–BH3 and form the openings in the outer membrane; and **BH3-only proteins** (Bim, Bid, Puma, Bad, Noxa, Bik, Bmf, Hrk) share only the BH3 domain and promote MOMP by binding the other members. BH3-only proteins that also bind and activate Bax and Bak directly (Bim, tBid, Puma) are called activators; those that only neutralize anti-apoptotic members (Bad, Noxa) are called sensitizers.

The BH1–BH3 domains of the multidomain proteins fold into a bundle of α-helices with a hydrophobic groove on its surface, into which the amphipathic BH3 helix of a partner binds. This one interaction explains the family. Bak resides in the outer membrane and Bax mostly in the cytosol; when activated, they change conformation, expose their own BH3 domain, insert into the outer membrane and form homodimers by inserting each BH3 into the groove of its partner, then larger oligomers and lipidic pores large enough for cytochrome c (and eventually macropores that let the inner membrane herniate). Anti-apoptotic proteins bind the exposed BH3 domain of activated Bax and Bak and so prevent their oligomerization, and they sequester the activator BH3-only proteins. Cells lacking both Bax and Bak do not undergo MOMP in response to any intrinsic stimulus (Wei et al. 2001), and every cell requires at least one anti-apoptotic member to survive.

![The Bcl-2 family. (A) Domain architecture: anti-apoptotic proteins have BH4, BH3, BH1 and BH2 domains and a C-terminal transmembrane anchor (TM); the effectors Bax and Bak have BH3, BH1, BH2 and TM; BH3-only proteins share only the BH3 helix, which binds the groove formed by BH1–BH3 of the others. (B) Selective binding of BH3 domains to the five anti-apoptotic proteins (qualitative; after Chen et al. 2005 and Certo et al. 2006): the activators Bim, Puma and tBid bind all of them, the sensitizer Bad binds Bcl-2, Bcl-xL and Bcl-w but not Mcl-1 or A1, and Noxa binds only Mcl-1 and A1. A cell protected by both Bcl-xL and Mcl-1 is killed by Bad and Noxa together but by neither alone](./plots/bcl2-family.py)

How exactly BH3-only proteins activate Bax and Bak was debated between a direct-activation model (activators bind and trigger Bax and Bak; anti-apoptotic proteins work by sequestering activators) and a displacement model (Bax and Bak are constitutively capable of activation; anti-apoptotic proteins hold them, and BH3-only proteins displace them). The current unified view accepts both modes, with anti-apoptotic proteins restraining both activators (mode 1) and activated effectors (mode 2). In any case MOMP is decided by a balance of competing binding equilibria, and the selectivity of the BH3 domains (panel B) means that the death of a particular cell depends on which anti-apoptotic proteins it relies on. This "BH3 profiling" with peptides predicts the response of tumor cells to chemotherapy.

Different stresses act through different BH3-only proteins, transcriptionally or post-translationally:

| Stimulus | BH3-only protein | Mechanism |
|---|---|---|
| DNA damage | Puma, Noxa | induced by p53 ([7.3.22](/7.3.22#sec-22.3.2)) |
| loss of growth factor signaling, cytokine withdrawal | Bim, Bad | FOXO induces Bim; PKB no longer phosphorylates Bad |
| ER stress | Bim, Puma, Noxa | CHOP (via PERK–ATF4) induces them ([7.3.7](/7.3.7)) |
| detachment from matrix (anoikis) | Bim, Bmf | released from the cytoskeleton, induced |
| death receptors | Bid | cleaved by caspase-8 to tBid |
| antigen-receptor negative selection of lymphocytes | Bim | induced |

Bcl-2 itself was the first oncogene found to act by preventing death rather than by promoting proliferation: it was cloned from the breakpoint of the t(14;18) translocation of follicular lymphoma, which places *BCL2* under the immunoglobulin heavy-chain enhancer, it promotes the survival of hematopoietic cells deprived of growth factors without making them divide (Vaux, Cory and Adams 1988), and transgenic mice overexpressing it accumulate long-lived B cells and develop lymphoma only after additional mutations (McDonnell et al. 1989). This discovery made evasion of apoptosis a hallmark of cancer ([7.3.26](/7.3.26)). Drugs that mimic BH3 domains bind the groove of anti-apoptotic proteins and release the effectors: venetoclax, specific for Bcl-2, is approved for chronic lymphocytic leukemia and acute myeloid leukemia, whose cells depend on Bcl-2; navitoclax inhibits Bcl-2, Bcl-xL and Bcl-w but causes thrombocytopenia, because platelets depend on Bcl-xL for their life span; and Mcl-1 inhibitors are in trials.

**Definition 25.4.4 (BH3 Mimetic)** A **BH3 mimetic** is a small molecule that binds the BH3-binding groove of anti-apoptotic Bcl-2 family proteins and so triggers MOMP in cells that depend on them for survival.

### 25.4.4. IAPs and Smac

**Definition 25.4.5 (IAP and Smac)** An **inhibitor of apoptosis protein** (IAP) is a protein with one to three baculovirus IAP repeat (BIR) domains; the mammalian XIAP binds and inhibits active caspase-9 (through BIR3) and caspase-3 and -7 (through BIR2 and its linker), and, as a RING ubiquitin ligase, ubiquitinates them. **Smac** (second mitochondria-derived activator of caspases, also called DIABLO) is an intermembrane-space protein that, after release by MOMP, binds the BIR domains of XIAP through its N-terminal Ala-Val-Pro-Ile (AVPI) motif and displaces the caspases; Omi (HtrA2), a serine protease, acts similarly and also cleaves IAPs.

IAPs were found in baculoviruses, which use them to keep infected insect cells alive until the virus has replicated. In mammals XIAP is the only member that inhibits caspases directly; cIAP1, cIAP2 and survivin act mainly through ubiquitination in TNF signaling and in mitosis. XIAP sets a threshold that the caspases must exceed, so that small, accidental activation of a few caspase molecules does not kill the cell. In *Drosophila* the balance is different: the fly IAP DIAP1 continuously restrains caspase activity, and cells die when the IAP antagonists Reaper, Hid and Grim, which share the IAP-binding motif of Smac, are expressed; the fly Apaf1 homolog Dark does not need cytochrome c. Small-molecule Smac mimetics, which cause the degradation of cIAPs and release XIAP-bound caspases, sensitize cancer cells to TNF and TRAIL and are in clinical trials.

### 25.4.5. Survival Signals

Most animal cells need signals from other cells to avoid apoptosis: Raff's proposal that death is the default fate of a cell deprived of **survival factors** ([7.3.22](/7.3.22#sec-22.1.1)) explains how tissues match cell numbers to the supply of signals. Survival signals act mainly on the Bcl-2 family ([7.3.18](/7.3.18#sec-18.6.3)):

1. **Phosphoinositide 3-kinase** and **protein kinase B** (Akt) phosphorylate Bad on Ser112 and Ser136, creating binding sites for 14-3-3 proteins that hold it away from Bcl-xL and Bcl-2; they phosphorylate FOXO transcription factors, which are exported from the nucleus and cannot induce Bim and Fas ligand; and they phosphorylate and activate Mdm2, which lowers p53.
2. The Ras–MAPK pathway phosphorylates Bim, targeting it for proteasomal degradation, and induces Mcl-1 and Bcl-xL; JAK–STAT signaling by cytokines such as IL-3 and erythropoietin induces Bcl-xL.
3. Adhesion to the extracellular matrix through **integrins** and focal adhesion kinase signals survival, so that epithelial cells that detach die by anoikis, a safeguard that metastatic cells must overcome ([7.3.26](/7.3.26)).

Some neurons use a different logic: their survival-factor receptors (such as the dependence receptors DCC and UNC5 for netrin, and p75NTR) actively promote apoptosis when unoccupied and stop doing so when bound. In either case survival depends on the presence of the factor.

### 25.4.6. A Switch with a Variable Delay

Apoptosis is all-or-none at the level of a single cell: cells are found alive or dying, rarely in between, and once caspase-3 begins to rise it reaches its maximum within minutes. Yet cells exposed to the same stimulus die at very different times. Live-cell imaging with FRET reporters of caspase-8 and caspase-3 activity (Albeck et al. 2008) showed that after TRAIL treatment the initiator caspase activity rises slowly and variably for hours, then MOMP occurs, and within about 15 minutes the executioners are fully active: a variable delay followed by a fast, invariant execution. This combination is the signature of a **bistable** switch with a threshold, built from positive feedback and a stoichiometric inhibitor. A minimal model with the topology of Eissing et al. (2004) captures it.

**Formula 25.4.1 (Minimal Caspase Switch)** Let $x$ and $y$ be the active fractions of the initiator caspase (caspase-8 or -9) and the executioner caspase-3, and $z$ the level of free XIAP relative to its resting value. With a stimulus of strength $u$,

$$
\begin{aligned}
\frac{\mathrm{d}x}{\mathrm{d}t} &= (u + a y)(1 - x) - d x, \\
\frac{\mathrm{d}y}{\mathrm{d}t} &= b x (1 - y) - (c z + d) y, \\
\frac{\mathrm{d}z}{\mathrm{d}t} &= p - (q + e y) z,
\end{aligned}
\tag{25.1}
$$
where $a$ is the feedback activation of initiators by executioners (through caspase-6 and direct cleavage), $b$ the activation of executioners by initiators, $c$ the inhibition of caspase-3 by XIAP, $d$ the inactivation of active caspases, $p$ and $q$ the synthesis and turnover of XIAP, and $e$ the degradation of XIAP that is caused by binding to active caspase-3.

Near the resting state ($x = y = 0$, $z = 1$), a small perturbation grows only if the loop gain $ab/[d(c + d)]$ exceeds 1; with $a = b = 1$, $c = 32$, $d = 0.1$ (per minute) the gain is about 0.3, so the resting state is stable and small amounts of active caspase are cleared, mainly because XIAP binds them. A large perturbation consumes XIAP (term $e y z$), which removes the brake, and the feedback then carries the system to a second stable state with high caspase activity. A constant stimulus $u$ moves the resting state towards the threshold; above a critical $u^*$ the resting state disappears in a saddle-node **bifurcation** ([2.4](/2.4)) and the system must switch. Just above $u^*$ the trajectory lingers near the place where the two states merged ("ghost" of the steady state), so the delay grows without bound as $u \to u^*$, whereas the final rise, driven by the feedback, takes the same few minutes whatever $u$. Because the high state persists when $u$ is removed, the switch is irreversible.

![Variable delay and all-or-none activation in the caspase switch, Eq. (25.1), with a = b = 1, c = 32, d = 0.1, p = q = 0.02 and e = 4 per minute. (A) Active caspase-3 after constant stimuli of increasing strength u: at u = 0.003 (below the threshold) the cell stays alive; above it, activity stays low for a delay that is longer the closer u is to the threshold, and then rises steeply to the same high level. (B) The delay to half-maximal activity diverges as the stimulus approaches the threshold u* (dashed line). (C) A population of 400 cells whose stimulus varies lognormally (median 0.008): each dot is a cell; the times at which cells activate their caspases are spread over hours, but in every cell the 10–90 % rise takes about 9 minutes; cells whose stimulus falls below the threshold survive](./plots/caspase-switch.py)

The model explains why fractional killing, the survival of part of a genetically identical population exposed to a drug, need not reflect genetic resistance: Spencer et al. (2009) showed that the timing and the probability of TRAIL-induced death in clonal cells are set by natural, non-genetic differences in the levels of pathway proteins at the time of treatment; sister cells, which inherit similar levels, die at similar times, and the correlation decays over a few generations as the protein levels drift ([7.2.22](/7.2.22)). The same logic, a switch with a threshold set by protein levels, makes the response of tumors to chemotherapy partly stochastic.

## 25.5. Clearing the Corpses

**Definition 25.5.1 (Efferocytosis)** **Efferocytosis** is the phagocytic engulfment and digestion of apoptotic cells by macrophages, dendritic cells or neighboring nonprofessional phagocytes (epithelial cells, fibroblasts), guided by signals displayed and released by the dying cell, and accompanied by an anti-inflammatory response of the phagocyte.

Clearance proceeds in steps, each with its own signals.

1. Find me. Apoptotic cells release nucleotides (ATP and UTP, through pannexin-1 channels opened by caspase cleavage), lysophosphatidylcholine, sphingosine 1-phosphate and the chemokine fractalkine (CX3CL1), which attract phagocytes.
2. Eat me. The main signal is phosphatidylserine on the outer leaflet. In healthy cells it is confined to the inner leaflet by the ATP-dependent **flippase** ATP11C (with CDC50A); during apoptosis caspases inactivate the flippase and activate the **scramblase** Xkr8 by cleavage, and both changes are needed for fast, irreversible exposure ([7.1.13](/7.1.13#sec-13.2.2); [7.3.4](/7.3.4)): without scrambling, phosphatidylserine would leak out only slowly; without flippase inactivation, it would be flipped back. Phagocytes recognize it directly (TIM-4, BAI1, stabilin-2) or through bridging proteins (MFG-E8 to integrin αvβ3; Gas6 and protein S to the TAM receptor tyrosine kinases Tyro3, Axl and MerTK); calreticulin and oxidized lipids add further signals.
3. Don't eat me. Healthy cells, including activated platelets and lymphocytes that transiently expose phosphatidylserine, display CD47, which binds SIRPα on macrophages and inhibits engulfment through the phosphatase SHP-1; dying cells lose these signals.
4. Digestion and resolution. The engulfed corpse is degraded in phagolysosomes ([7.3.11](/7.3.11)), sometimes by LC3-associated phagocytosis, and the phagocyte metabolizes the excess lipids and cholesterol (through LXR and PPAR nuclear receptors) and secretes TGF-β, IL-10 and prostaglandin E₂, which suppress inflammation.

Efferocytosis is so efficient that a macrophage in the thymus may engulf several apoptotic thymocytes in an hour, and apoptotic bodies are seen in tissue sections only for minutes. Its failure is pathological: mice lacking MerTK or MFG-E8 accumulate uncleared apoptotic cells that undergo secondary necrosis and develop lupus-like autoimmunity, and defective efferocytosis in atherosclerotic plaques enlarges their necrotic core. Cancer cells exploit the same system by overexpressing CD47, and antibodies that block CD47 are being tested to make tumor cells edible ([7.3.26](/7.3.26)).

## 25.6. Other Forms of Regulated Cell Death

Apoptosis is not the only regulated death. Several programs kill cells by rupturing their membranes, which releases DAMPs and cytokines and alerts the immune system; they are thought to have evolved largely as defenses against pathogens that block apoptosis.

![Three forms of regulated necrosis (SBGN activity flow; notched boxes are inhibitors). (A) Necroptosis: TNF bound to TNFR1 activates RIPK1; active caspase-8 cleaves RIPK1 and sends the cell into apoptosis, but when caspase-8 is inhibited RIPK1 and RIPK3 form a necrosome, RIPK3 phosphorylates MLKL and MLKL ruptures the plasma membrane; necrostatin-1 inhibits RIPK1. (B) Pyroptosis: microbial products and danger signals assemble an inflammasome such as NLRP3 with ASC, which activates caspase-1; cytosolic LPS activates caspase-11 (caspase-4 and -5 in humans). Both caspases cleave gasdermin D, whose N-terminal fragment forms pores; caspase-1 also matures IL-1β and IL-18, which leave through the pores, and the cell lyses. (C) Ferroptosis: iron and reactive oxygen species peroxidize phospholipids containing polyunsaturated fatty acids, which ACSL4 incorporates into membranes; GPX4, using glutathione made from cystine imported by system xc⁻, and FSP1 with ubiquinol (CoQH₂) remove the peroxides. Erastin blocks system xc⁻ and RSL3 inhibits GPX4](./plots/rcd-pathways.py)

### 25.6.1. Necroptosis

**Definition 25.6.1 (Necroptosis)** **Necroptosis** is regulated necrosis executed by the pseudokinase MLKL after its phosphorylation by RIPK3, which is activated by RHIM-domain proteins (RIPK1 downstream of death receptors, TRIF downstream of Toll-like receptors 3 and 4, ZBP1 sensing viral nucleic acids) when caspase-8 is inactive.

RIPK1 and RIPK3 interact through their RHIM motifs and polymerize into amyloid-like filaments (the necrosome), in which RIPK3 is activated and phosphorylates MLKL; phosphorylated MLKL oligomerizes, moves to the plasma membrane, binds phosphoinositides and disrupts it. Caspase-8 suppresses the pathway by cleaving RIPK1 (and CYLD): mice lacking caspase-8 or FADD die at mid-gestation, and the additional deletion of *Ripk3* or *Mlkl* rescues them, showing that a key embryonic role of caspase-8 is to prevent necroptosis. The logic is a backup: viruses such as cytomegalovirus and vaccinia encode caspase-8 inhibitors to block apoptosis, and the cell responds by dying a death that the inhibitors cannot stop and that alarms the immune system. Necroptosis contributes to ischemia–reperfusion injury and inflammatory diseases, and necrostatin-1, an allosteric RIPK1 inhibitor, protects in models.

### 25.6.2. Pyroptosis

**Definition 25.6.2 (Inflammasome, Gasdermin and Pyroptosis)** An **inflammasome** is a cytosolic multiprotein complex in which a sensor (NLRP1, NLRP3, NLRC4, AIM2 or pyrin), the adaptor ASC and procaspase-1 assemble on detection of microbial products or cellular damage, activating caspase-1 by proximity. **Gasdermins** are a family of pore-forming proteins (gasdermin A–E in humans) whose N-terminal domain is held inactive by the C-terminal domain until a protease cleaves the linker; the N-terminal fragment then binds acidic phospholipids of the inner leaflet and oligomerizes into pores 10–20 nm across. **Pyroptosis** is regulated necrosis caused by gasdermin pores, typically after cleavage of gasdermin D by inflammatory caspases.

The pathway was clarified in 2015, when Shao's and Dixit's groups identified gasdermin D as the substrate of caspase-1 and caspase-11 that is needed for pyroptosis. Two routes activate it: the canonical inflammasomes, which activate caspase-1, and the noncanonical route, in which caspase-11 (caspase-4 and -5 in humans) binds lipopolysaccharide from Gram-negative bacteria directly in the cytosol. Caspase-1 also cleaves the precursors of IL-1β and IL-18, which leave the cell through the gasdermin pores, and the influx of water through the pores causes swelling, followed by rupture that depends on the membrane protein NINJ1. Pyroptosis removes the replication niche of intracellular bacteria and releases cytokines that recruit neutrophils; excessive activation causes septic shock, and gain-of-function mutations in *NLRP3* cause autoinflammatory diseases. Other proteases cleave other gasdermins: caspase-3 cleaves gasdermin E, so that chemotherapy can turn apoptosis into pyroptosis in cells that express it, and granzyme A from cytotoxic lymphocytes cleaves gasdermin B.

### 25.6.3. Ferroptosis

**Definition 25.6.3 (Ferroptosis)** **Ferroptosis** is regulated cell death caused by the iron-dependent, uncontrolled peroxidation of membrane phospholipids that contain polyunsaturated fatty acids, which occurs when the glutathione peroxidase GPX4 and other lipid-radical defenses fail.

Dixon and Stockwell named it in 2012 after characterizing cell death induced by the small molecule erastin, which did not need caspases or RIPK1, was blocked by iron chelators and lipophilic antioxidants (ferrostatin-1) and was accompanied by lipid peroxidation. Its biochemistry is a race between lipid peroxidation, a chain reaction propagated by lipid radicals and started by iron (through Fenton chemistry and lipoxygenases), and its repair. GPX4, a selenoprotein, reduces phospholipid hydroperoxides to alcohols using glutathione, whose synthesis is limited by cysteine; most cells obtain cysteine as cystine through system xc⁻, an antiporter (SLC7A11 with SLC3A2) that exchanges it for glutamate. A second line of defense is FSP1, which regenerates ubiquinol (and vitamin K) in the plasma membrane as radical-trapping antioxidants. The substrate is supplied by ACSL4 and LPCAT3, which esterify arachidonic and adrenic acid into phosphatidylethanolamine; cells that lack ACSL4 are resistant. How peroxidation finally kills, probably by thinning and permeabilizing membranes, is still unclear.

Ferroptosis contributes to ischemic injury of kidney and liver and to neurodegeneration, and mice lacking GPX4 die as embryos. p53 represses *SLC7A11*, which may contribute to its tumor-suppressor function; conversely, some therapy-resistant cancer cells in a mesenchymal state depend strongly on GPX4 and can be killed by inhibiting it.

### 25.6.4. Other Modes and a Comparison

- Mitochondrial permeability transition–driven necrosis: $\ce{Ca^2+}$ overload and oxidative stress open a nonspecific pore in the inner mitochondrial membrane (requiring cyclophilin D, inhibited by cyclosporin A); the mitochondria depolarize and swell and ATP is lost. It contributes to ischemia–reperfusion injury of heart and brain. (Older models attributed apoptotic cytochrome c release to this pore; it is now associated with necrosis, and MOMP with apoptosis.)
- Parthanatos: excessive DNA damage hyperactivates PARP1 ([7.2.8](/7.2.8)), whose poly(ADP-ribose) polymer depletes NAD⁺ and induces the release of AIF from mitochondria, which with the nuclease MIF fragments chromatin into large pieces; it is important in excitotoxic neuronal death.
- NETotic death: activated neutrophils decondense their chromatin by citrullination of histones (PAD4) and expel it with antimicrobial proteins as neutrophil extracellular traps that capture bacteria.
- Entosis: a living cell, usually a detached epithelial cell, invades a neighbor and is killed in a lysosomal vacuole.
- Lysosome-dependent death: lysosomal membrane permeabilization releases cathepsins into the cytosol ([7.3.11](/7.3.11)).
- Autophagy-dependent death: death that requires the **autophagy** machinery, as in the destruction of the *Drosophila* salivary gland at metamorphosis or autosis ([7.3.11](/7.3.11#sec-11.7.4)); in most dying cells autophagy is an attempt to survive.
- Immunogenic cell death: any death that is accompanied by calreticulin exposure, ATP and HMGB1 release and type I interferon, and therefore primes adaptive immunity against antigens of the dead cell; some chemotherapies (anthracyclines, oxaliplatin) and radiotherapy induce it ([7.15](/7.15)).
- Cuproptosis (Tsvetkov et al. 2022), proposed more recently: copper binds lipoylated enzymes of the citric acid cycle, causing their aggregation and proteotoxic stress.

| | Apoptosis | Necroptosis | Pyroptosis | Ferroptosis | Accidental necrosis |
|---|---|---|---|---|---|
| morphology | shrinkage, condensation, blebbing, apoptotic bodies | swelling, rupture | swelling, pores, rupture | shrunken mitochondria with dense membranes, rupture | swelling, rupture |
| plasma membrane | intact until cleared | ruptured by MLKL | gasdermin pores | peroxidized | ruptured |
| key effector | caspase-3, -7 | MLKL | gasdermin D | lipid peroxides | — |
| triggered by | death receptors, DNA damage, loss of survival signals | TNF, TLR, viruses with caspase-8 blocked | inflammasomes, cytosolic LPS | loss of GPX4 or cystine, excess iron | trauma, extreme conditions |
| inflammation | none (efferocytosis) | strong | strong (IL-1β, IL-18) | moderate | strong |
| inhibitors | zVAD-fmk, Bcl-2 | necrostatin-1, RIPK3 inhibitors | caspase-1 inhibitors, disulfiram | ferrostatin-1, liproxstatin-1, deferoxamine | — |

The modes are not independent: caspase-8 decides between apoptosis and necroptosis, caspase-3 can cleave gasdermin E, and a cell can switch from one mode to another when one is blocked (the concept of PANoptosis describes complexes that engage several at once). This redundancy is part of the safety design of a multicellular organism: a cell that has become dangerous should die, by whatever route remains open.

## 25.7. Cellular Senescence

**Definition 25.7.1 (Cellular Senescence)** **Cellular senescence** is a stable and essentially irreversible arrest of proliferation in cells that remain metabolically active and viable, induced by telomere shortening and by various stresses, enforced by the p53–p21 and p16INK4a–Rb pathways, and accompanied by changes in morphology, chromatin and gene expression including the secretion of a characteristic set of factors (the SASP).

Senescence differs from **quiescence** (G0, [7.3.22](/7.3.22#sec-22.1.2)), which is reversed by mitogens, and from terminal differentiation, which is a specialized program; senescent cells do not re-enter the cycle when stimulated, and they often resist apoptosis.

### 25.7.1. The Hayflick Limit

Until the 1960s it was believed, following Carrel's claim to have kept chick fibroblasts dividing for decades, that cultured vertebrate cells were immortal. Hayflick and Moorhead (1961) showed that normal human fetal fibroblasts divide only about 50 times and then stop, although they remain alive for months. To exclude a culture artifact, they mixed male cells that had already divided many times with female cells that had divided few times; when the male cells, identified by their Y chromosome, stopped, the female cells in the same flask kept dividing. The limit was therefore intrinsic to the cells, not to the medium. Cells frozen at a given division resumed counting where they had stopped, and fusing enucleated old cells (cytoplasts) with young cells, or the reverse, showed that the "memory" resides in the nucleus (Wright and Hayflick 1975).

**Definition 25.7.2 (Hayflick Limit and Replicative Senescence)** The **Hayflick limit** is the finite number of times, typically 40–60 population doublings for human fetal fibroblasts, that a normal somatic cell population can divide in culture. **Replicative senescence** is the arrest reached at this limit, caused mainly by the shortening of telomeres.

The course slides summarize the classical observations: the proliferative lifespan of cultured fibroblasts falls with the age of the donor (about 40–60 doublings for embryonic cells, about 20 for cells from middle-aged and 2–4 for cells from old donors), and correlates with the lifespan of the species (Röhme 1981). Both correlations are weaker than these early results suggested. Large studies of healthy donors found little or no decline of replicative capacity with age and a large variation among individuals (Cristofalo et al. 1998), and comparisons across mammals show that body mass and the expression of telomerase predict the use of replicative senescence better than lifespan: small rodents have long telomeres and express telomerase, whereas large species repress telomerase in somatic cells and limit division with short telomeres (Gomes et al. 2011). Cells from patients with premature aging syndromes (Werner syndrome, caused by loss of the RecQ helicase WRN, and **Hutchinson–Gilford progeria syndrome**, [7.3.16](/7.3.16#sec-16.3.3)) do senesce after fewer divisions.

### 25.7.2. Telomeres Count Divisions

Olovnikov (1971) and Watson (1972) noted that conventional DNA polymerases cannot replicate the very ends of linear chromosomes (the end-replication problem, [7.2.7](/7.2.7#sec-7.6.3)), and Olovnikov proposed that the resulting shortening could count divisions. Harley, Futcher and Greider (1990) found that the telomeres of human fibroblasts shorten by about 50–100 bp per population doubling in culture, and that the telomeres of older donors are shorter. The decisive experiment was the expression of the catalytic subunit of **telomerase**, hTERT, in normal human fibroblasts and retinal epithelial cells (Bodnar et al. 1998): their **telomeres** were maintained, and they divided far beyond their Hayflick limit with a normal karyotype and without becoming cancerous.

Human telomeres are 10–15 kb at birth and shorten at each division by end processing (exonucleolytic resection that creates the $3'$ overhang) and incomplete lagging-strand synthesis, and faster under oxidative stress, which causes single-strand breaks in their G-rich repeats. Senescence is triggered not by the average length but by the few shortest telomeres: when a telomere becomes too short to bind enough shelterin, its end is recognized as a double-strand break and activates the ATM–Chk2–p53–p21 pathway of the DNA damage response ([7.3.22](/7.3.22#sec-22.3.2)), forming persistent telomere-associated DNA-damage foci (Hemann et al. 2001 showed in mice that the shortest telomere, not the average, determines viability).

**Example 25.7.1 (A Stochastic Model of Replicative Lifespan)** Give a cell 92 telomeres with initial lengths $L_j(0) \sim \mathcal{N}(L_0, \sigma_0^2)$, $\sigma_0 = 1.5\,\mathrm{kb}$, and let each telomere of each daughter lose a random amount $\Delta_j \ge 0$ with mean $80\,\mathrm{bp}$ and standard deviation $40\,\mathrm{bp}$ at every division:

$$
L_j(k + 1) = L_j(k) - \Delta_j(k), \qquad \text{senescence at } K = \min\{k : \min_j L_j(k) < L_{\mathrm{c}}\},
\tag{25.2}
$$
with a critical length $L_{\mathrm{c}} = 1.5\,\mathrm{kb}$. The shortest of 92 normally distributed lengths lies about $2.5\sigma_0$ below the mean, so $K \approx (L_0 - 2.5\sigma_0 - L_{\mathrm{c}})/\bar\Delta$: about 60 divisions for $L_0 = 10\,\mathrm{kb}$ and about 30 for $L_0 = 7.5\,\mathrm{kb}$. The spread of initial lengths, not only the loss per division, sets the limit: each lineage inherits a different shortest telomere, so sister lineages senesce after different numbers of divisions, as observed in clonal analyses of fibroblasts (Smith and Whitney 1980). In a culture the longest-lived lineages continue to double after the others have stopped, so the culture's cumulative number of doublings exceeds the median lifespan of single lineages, and the culture slows gradually rather than stopping at once. With telomerase ($\Delta_j = 0$ on average) there is no limit.

![Telomere shortening counts divisions, Eq. (25.2). (A) One lineage: the mean length of 92 telomeres (blue) and the shortest telomere (red) fall by about 80 bp per division; the cell senesces when the shortest telomere reaches the critical length (dashed line), long before the average is critical. (B) Replicative lifespans of 2000 lineages from a young donor (initial mean length 10 kb, median about 59 divisions) and an old donor (7.5 kb, median about 28). (C) Cumulative population doublings of cultures with one division per day: the young-donor and old-donor cultures slow and reach a plateau, the Hayflick limit, whereas cells expressing hTERT keep doubling](./plots/telomere-senescence.py)

Mice have telomeres of 20–50 kb and express telomerase in many somatic cells, so their cells in culture stop instead because of oxidative damage at atmospheric oxygen (they divide indefinitely at 3% $\ce{O2}$; Parrinello et al. 2003). Mice lacking the telomerase RNA (*Terc*) are normal in the first generation, but their telomeres shorten from generation to generation, and after four to six generations they are infertile and show defects of highly proliferative tissues (blood, intestine, skin) and premature aging (Blasco et al. 1997), a model of human telomere syndromes such as dyskeratosis congenita.

### 25.7.3. Markers of Senescent Cells

No single marker is specific; senescence is recognized by a combination.

| Feature | Description |
|---|---|
| arrest | no DNA synthesis (no EdU or BrdU incorporation, no Ki-67), not reversed by mitogens; high p21 and p16INK4a, hypophosphorylated Rb |
| morphology | large, flat cells (in culture often several times the normal area), often multinucleate; nuclear invaginations |
| lysosomes | enlarged lysosomal compartment with lipofuscin and dense bodies; senescence-associated β-galactosidase |
| chromatin | senescence-associated heterochromatin foci (SAHF): condensed, DAPI-dense foci with H3K9me3, HP1 and macroH2A that silence E2F target genes, assembled with HIRA, ASF1 and **PML bodies**; loss of lamin B1 |
| DNA damage | persistent damage foci (γH2AX, 53BP1), many at telomeres |
| organelles | reduced and abnormal ER, leaky, elongated mitochondria with more ROS |
| secretion | the SASP (25.7.5) |

**Definition 25.7.3 (Senescence-Associated β-Galactosidase)** **Senescence-associated β-galactosidase** (SA-β-gal) is lysosomal β-galactosidase activity detectable histochemically at pH 6.0 (rather than at its optimum of pH 4.0–4.5) in senescent cells, because of the large increase of their lysosomal mass (Dimri et al. 1995).

### 25.7.4. Inducers and Pathways

| Type | Trigger | Main pathway |
|---|---|---|
| replicative | critically short telomeres | DDR → p53 → p21 |
| oncogene-induced | activated Ras, BRAF, excess Myc or E2F; loss of PTEN ([7.3.22](/7.3.22#sec-22.5.3)) | ARF → p53; p16INK4a → Rb; replication stress → DDR |
| DNA damage–induced (including therapy-induced) | ionizing radiation, chemotherapy | DDR → p53 → p21 |
| stress-induced | oxidative stress (ROS, high $\ce{O2}$), culture shock, mitochondrial dysfunction | p38 MAPK, p16INK4a |
| developmental | specific embryonic structures (mesonephros, endolymphatic sac, apical ectodermal ridge) | p21, independent of DNA damage |
| paracrine | SASP of neighboring senescent cells | TGF-β, IL-1, ROS |

The two arms converge on the cell-cycle machinery: p21 inhibits Cdk2 and Cdk1, and p16INK4a inhibits Cdk4 and Cdk6, so that Rb stays hypophosphorylated and represses the targets of **E2F** ([7.3.22](/7.3.22#sec-22.2.2)). p53–p21 usually establishes the arrest and p16–Rb maintains it: senescent human fibroblasts with low p16 can resume division if p53 is inactivated, whereas cells with high p16 cannot, because Rb-dependent heterochromatin has silenced proliferation genes. This reinforcement by chromatin is what makes the state stable.

### 25.7.5. The Senescence-Associated Secretory Phenotype

**Definition 25.7.4 (SASP)** The **senescence-associated secretory phenotype** (SASP) is the secretion by senescent cells of a large set of proinflammatory cytokines (IL-6, IL-1α and IL-1β), chemokines (IL-8, MCP-1), growth factors (VEGF, HGF), proteases (matrix metalloproteinases) and other proteins (PAI-1), which act on neighboring cells and on the immune system.

The SASP is driven by NF-κB and C/EBPβ, activated by persistent DNA damage signaling, by p38 MAPK and **mTORC1**, by IL-1α acting as an autocrine amplifier, and by fragments of chromatin that leak into the cytoplasm of senescent cells and are sensed by cGAS–STING, a pathway that normally detects viral DNA. Its effects are double-edged. On the beneficial side, the SASP reinforces the arrest (autocrine IL-6 and IL-8), recruits natural killer cells, macrophages and T cells that clear the senescent cells (in mouse liver, senescent cells expressing oncogenic Ras are removed by CD4 T cells, Kang et al. 2011), promotes wound healing and limits fibrosis (senescent stellate cells in the injured liver), and participates in embryonic patterning (developmental senescence, Muñoz-Espín et al. and Storer et al. 2013). On the harmful side, chronic SASP from accumulating senescent cells causes local and systemic inflammation, induces senescence in neighbors (paracrine senescence), degrades tissue structure, and can stimulate the proliferation and invasion of nearby premalignant cells. Senescence thus resembles an acute damage response that is useful when transient and harmful when it persists.

### 25.7.6. Senescence as a Barrier to Cancer

Several observations show that senescence is a tumor-suppressor mechanism. It is triggered by potentially oncogenic events (activated oncogenes, as in **oncogene-induced senescence** of [7.3.22](/7.3.22#sec-22.5.3); DNA damage; eroded telomeres), and senescent cells are abundant in premalignant lesions (nevi, lung adenomas, prostate intraepithelial neoplasia) but rare in the cancers that arise from them (Collado et al. 2005). It is enforced by p53 and Rb, the two **tumor suppressor gene** products most frequently inactivated in cancer, and many **oncogenes** of DNA tumor viruses (SV40 large T, adenovirus E1A and E1B, papillomavirus E6 and E7) act by inactivating them. And mice whose cells do not senesce in response to damage, for example those lacking p53 or the *Cdkn2a* locus, die young of cancer.

In human cells two barriers must be overcome. Inactivating p53 and Rb lets cells bypass the first, senescence (M1), but they continue to lose telomeric DNA until they reach crisis (M2), where unprotected chromosome ends fuse, form dicentric chromosomes that break in mitosis (breakage–fusion–bridge cycles) and kill most cells. The rare survivors of crisis have stabilized their telomeres, usually by reactivating telomerase (in about 85–90% of human cancers) and otherwise by the recombination-based alternative lengthening of telomeres (ALT). Telomere erosion is thus both a barrier and, during crisis, a source of the genomic chaos characteristic of many carcinomas ([7.3.26](/7.3.26)).

### 25.7.7. Senescent Cells and Organismal Aging

Senescent cells accumulate with age in many tissues (skin, liver, adipose tissue, kidney) and at sites of age-related disease (atherosclerotic plaques, osteoarthritic joints, fibrotic lungs). Whether they cause aging was tested in mice.

- BubR1 hypomorphic mice. BubR1 is a component of the **spindle assembly checkpoint** ([7.3.21](/7.3.21#sec-21.3.3)); mice expressing about 10% of the normal amount (*BubR1*$^{\mathrm{H/H}}$) become aneuploid and age prematurely, with infertility, cataracts, loss of subcutaneous fat, arrhythmia, arterial stiffening, impaired wound healing, thin skin, kyphosis and sarcopenia, and their tissues accumulate p16INK4a-positive senescent cells.
- INK-ATTAC. Baker, van Deursen and colleagues (2011) put a drug-inducible suicide gene (FKBP fused to caspase-8, dimerized by the drug AP20187) under the *p16Ink4a* promoter, so that senescent cells could be killed at will. In BubR1 mice, lifelong clearance delayed cataracts, sarcopenia and fat loss, and late clearance slowed their progression (Science's runner-up breakthroughs of 2011). In normal mice, clearance from one year of age extended median lifespan by about a quarter and delayed age-related decline of kidney, heart and fat (Baker et al. 2016).
- Senolytics. Drugs that selectively kill senescent cells exploit their dependence on anti-apoptotic pathways that let them resist death: dasatinib with quercetin, navitoclax (a BH3 mimetic inhibiting Bcl-2 and Bcl-xL, 25.4.3), fisetin and others improved several age-related conditions in mice, and early human trials are under way. Senomorphic drugs instead suppress the SASP (rapamycin, JAK inhibitors).

**Definition 25.7.5 (Senolytic)** A **senolytic** is an agent that selectively kills senescent cells, usually by inhibiting the pro-survival pathways (Bcl-2 family proteins, PI3K–PKB, p53–FOXO4 interactions) on which senescent cells depend.

A simple model shows why senescent cells accumulate faster than linearly with age. Karin et al. (2019) measured, in mice, that senescent cells are produced at a rate that rises linearly with age, $\eta t$, and are removed by the immune system with saturating kinetics, $\beta X/(\kappa + X)$, where $X$ is the number of senescent cells:

$$
\frac{\mathrm{d}X}{\mathrm{d}t} = \eta t - \beta\frac{X}{\kappa + X} + \text{noise}.
\tag{25.3}
$$

When production approaches the maximal removal rate $\beta$, $X$ rises steeply and turns over more slowly, from days in young mice to weeks in old ones, as they observed; with a death threshold for $X$, the model gives a mortality that rises roughly exponentially with age, as in the Gompertz law of human mortality, with the large variation in lifespan between individuals coming from the noise.

Senescence is one of the twelve hallmarks of aging in the scheme of López-Otín and colleagues (2023), with genomic instability, telomere attrition, epigenetic alterations, loss of proteostasis, disabled macroautophagy, deregulated nutrient sensing (insulin/IGF-1, **mTORC1**, **AMP-activated protein kinase**, sirtuins), mitochondrial dysfunction, stem cell exhaustion, altered intercellular communication, chronic inflammation and dysbiosis. The older theories of aging answer two different questions:

| Theory | Claim | Status |
|---|---|---|
| mutation accumulation (Medawar 1952) | selection is weak against harmful effects that appear after reproduction, so they accumulate | evolutionary explanation of why aging exists |
| antagonistic pleiotropy (Williams 1957) | alleles that benefit the young but harm the old are favored | supported; senescence and the p53 response are examples |
| disposable soma (Kirkwood 1977) | organisms invest limited resources in reproduction rather than in perfect maintenance of the soma | supported by trade-offs |
| free radical and mitochondrial theory (Harman 1956, 1972) | **reactive oxygen species** from respiration damage macromolecules and cause aging | damage contributes, but antioxidants do not extend lifespan, and ROS are also signals |
| telomere theory | telomere shortening limits tissue renewal | explains replicative limits and telomere syndromes, but not aging in mice with long telomeres |
| programmed aging | aging is an adaptive program | not supported as a general explanation; conserved pathways (insulin/IGF-1, TOR) modulate lifespan without being "aging programs" |

The genetic studies of lifespan in model organisms, from *daf-2* (insulin/IGF-1 receptor) mutants of *C. elegans* that live twice as long (Kenyon et al. 1993) to dietary restriction and rapamycin in mice, show that the rate of aging is regulated by nutrient-sensing pathways that also control growth, autophagy ([7.3.11](/7.3.11#sec-11.7.4)) and senescence: the same signals that decide whether a cell grows decide how fast an organism ages.

## Summary

| Topic | Key points |
|---|---|
| Classification (Definitions 25.1.1, 25.1.2) | accidental vs regulated death; programmed death = physiological subset of regulated; NCCD 2018: 12 modes defined by mechanism; necrosis = swelling, rupture, DAMPs, inflammation |
| Apoptosis (Definitions 25.2.1, 25.2.2) | shrinkage, chromatin condensation, blebbing, apoptotic bodies, intact membrane; DNA ladder (≈ 180–200 bp), annexin V/PI, TUNEL, cleaved caspase-3; sculpting, matching neuron numbers, lymphocyte selection, damage removal |
| Core machinery (Definition 25.3.1) | *C. elegans*: EGL-1 ⊣ CED-9 ⊣ CED-4 → CED-3 = BH3-only ⊣ Bcl-2 ⊣ Apaf1 → caspase; 131 of 1090 cells; initiators (8, 9, 10, 2) activated by dimerization on platforms, executioners (3, 6, 7) by cleavage; substrates ICAD, lamins, ROCK1, ATP11C, Xkr8, PARP1 |
| Extrinsic pathway (Definition 25.4.1) | FasL, TNF, TRAIL → death domain → FADD → caspase-8 filaments (DISC); FLIP threshold; TNFR1 complex I (NF-κB, survival) vs II (death); type I vs type II cells, Bid → tBid; ALPS |
| Intrinsic pathway (Definition 25.4.2) | Bax/Bak oligomers → MOMP → cytochrome c + Apaf1 + dATP → apoptosome → caspase-9; fast, complete, variable onset; minority MOMP |
| Bcl-2 family (Definitions 25.4.3, 25.4.4) | anti-apoptotic (BH1–4), effectors Bax/Bak (BH1–3), BH3-only activators (Bim, tBid, Puma) and sensitizers (Bad, Noxa) with selective binding; BH3 into groove; t(14;18) *BCL2*; venetoclax, navitoclax |
| IAPs (Definition 25.4.5) | XIAP inhibits caspase-9, -3, -7; Smac (AVPI) and Omi released by MOMP; *Drosophila* Reaper/Hid/Grim vs DIAP1 |
| Survival signals (25.4.5) | PKB phosphorylates Bad (14-3-3), FOXO (no Bim, FasL), Mdm2; ERK degrades Bim, induces Mcl-1; anoikis; dependence receptors |
| Caspase switch (Formula 25.4.1, Eq. (25.1)) | positive feedback + XIAP; stable rest (loop gain < 1), threshold u*, saddle-node; delay diverges near u*, execution ≈ minutes; irreversible; non-genetic cell-to-cell variation → fractional killing |
| Clearance (Definition 25.5.1) | find me (ATP, LPC, CX3CL1), eat me (PS via ATP11C off + Xkr8 on; TIM-4, MFG-E8, Gas6–MerTK), don't eat me (CD47–SIRPα), anti-inflammatory resolution; defects → lupus-like disease |
| Regulated necrosis (Definitions 25.6.1–25.6.3) | necroptosis (RIPK1–RIPK3–MLKL when caspase-8 is off); pyroptosis (inflammasome → caspase-1/11 → gasdermin D pores, IL-1β); ferroptosis (Fe, PUFA-PE, GPX4–GSH–system xc⁻, FSP1); MPT necrosis, parthanatos, NETosis, entosis, lysosomal, autophagy-dependent, immunogenic death |
| Senescence (Definitions 25.7.1–25.7.4) | stable arrest; Hayflick limit ≈ 40–60 doublings, intrinsic and nuclear; telomeres (hTERT immortalizes); shortest telomere sets the limit (Eq. (25.2)); markers SA-β-gal, p16, SAHF, γH2AX foci; inducers (replicative, oncogene, damage, stress, developmental); p53–p21 initiates, p16–Rb maintains; SASP (NF-κB, C/EBPβ, cGAS–STING) |
| Cancer and aging (25.7.6, 25.7.7; Definition 25.7.5) | senescence barrier (M1) and crisis (M2), telomerase or ALT in cancers; BubR1 and INK-ATTAC mice; senolytics; Eq. (25.3): linear production, saturating removal → Gompertz-like mortality; theories and hallmarks of aging |

## Questions

1. Cells in culture are treated with a drug and analyzed by flow cytometry after staining with annexin V and propidium iodide. At 4 hours, 30% of the cells are annexin V–positive and propidium iodide–negative; at 24 hours, 60% are positive for both. Interpret the results. Why would the double-positive population be much smaller in a tissue?

   **Answer** Annexin V binds phosphatidylserine exposed on the outer leaflet; exclusion of propidium iodide shows that the membrane is still intact. At 4 hours 30% of the cells are therefore in early apoptosis. At 24 hours most dying cells have lost membrane integrity: in culture, without phagocytes, apoptotic cells undergo secondary necrosis, so double-positive cells at late times are mostly late apoptotic cells (a primary necrotic death would give double-positive cells without the earlier annexin-only stage). In a tissue, macrophages and neighboring cells engulf apoptotic cells within minutes to an hour of phosphatidylserine exposure (efferocytosis), before they lose membrane integrity.

2. In *C. elegans*, *ced-9* loss-of-function mutants die as embryos because many cells die ectopically, whereas *ced-9*; *ced-3* double mutants are viable with no cell deaths. What does this tell us about the order of action of the genes? Predict the phenotype of an *egl-1* loss-of-function mutant and of a *ced-9* gain-of-function mutant that cannot bind EGL-1.

   **Answer** CED-9 acts upstream of CED-3 and inhibits it (indirectly, by holding CED-4): without CED-9, CED-3 kills cells, and without CED-3 no cell can die whatever the state of CED-9, so *ced-3* is epistatic. EGL-1 inhibits CED-9 in cells fated to die; in an *egl-1* loss-of-function mutant CED-9 remains active and the 131 cells that normally die survive (the original *egl-1* gain-of-function alleles kill the HSN neurons and give an egg-laying defect, hence the name). A *ced-9* gain-of-function protein that cannot bind EGL-1 also prevents the deaths, as indeed found for the *ced-9(n1950)* allele, which is a substitution in the BH3-binding groove.

3. Using Formula 25.4.1, explain (a) why cells with more XIAP require a stronger stimulus to die and (b) why Smac mimetics shorten the delay and lower the threshold. (c) In type II cells, death receptor stimulation alone fails to kill cells that lack Bax and Bak, although caspase-8 is activated. Explain in terms of the model.

   **Answer** (a) XIAP enters through the term $c z y$: a higher resting level $z = p/q$ (larger $p$) increases the effective inactivation of active caspase-3, lowers the loop gain $ab/[d(cz + d)]$ and moves the saddle-node point to larger $u$, so a stronger stimulus is needed, and near-threshold delays at a given $u$ are longer. (b) Smac mimetics bind XIAP and reduce the free inhibitor, corresponding to a smaller $c z$ or a faster consumption $e$; the threshold falls and the delay, which depends on the distance from threshold, shortens. (c) In type II cells caspase-8 activity ($u$ in the model, acting on the executioners through $x$) is too low to overcome XIAP; the mitochondrial loop (tBid → Bax/Bak → MOMP) provides a second source of initiator activity (caspase-9) and releases Smac, which removes the brake. Without Bax and Bak this amplification and the release of Smac are absent, so the system stays in the resting state.

4. A tumor cell line depends on Mcl-1 and Bcl-xL for survival. Predict its response to (a) venetoclax, (b) navitoclax, (c) a peptide containing the BH3 domain of Noxa, (d) navitoclax combined with the Noxa peptide. Why do platelet counts fall in patients treated with navitoclax but not with venetoclax?

   **Answer** (a) Venetoclax inhibits only Bcl-2, which the cells do not rely on: little effect. (b) Navitoclax inhibits Bcl-2, Bcl-xL and Bcl-w but not Mcl-1; Mcl-1 can still restrain Bax/Bak and sequester activators, so killing is partial at best. (c) The Noxa BH3 domain neutralizes Mcl-1 (and A1) but not Bcl-xL, which remains protective: little effect. (d) Both protective proteins are neutralized and the cell undergoes MOMP and apoptosis: the combination kills, an example of the complementary selectivity shown in the Bcl-2 figure. Platelets are anucleate and their life span is limited by Bak and Bax activation that is restrained by Bcl-xL; inhibiting Bcl-xL with navitoclax shortens platelet life span, whereas venetoclax spares Bcl-xL.

5. Mice lacking caspase-8 die around embryonic day 10.5, but mice lacking both caspase-8 and RIPK3 are born and live, although they develop lymphadenopathy later. Explain both observations. Why might a host benefit from a death pathway that is suppressed by caspase-8?

   **Answer** Caspase-8 has, besides its role in extrinsic apoptosis, a constitutive role in cleaving RIPK1 and RIPK3 (as a caspase-8–FLIP heterodimer), which prevents necroptosis; without it, RIPK3-dependent necroptosis kills cells of the embryonic vasculature and yolk sac. Deleting RIPK3 removes this death, so the embryos survive. The later lymphadenopathy resembles ALPS, because Fas-induced apoptosis of lymphocytes, which requires caspase-8, is lost. Many viruses encode caspase-8 inhibitors to block apoptosis of the infected cell; the inhibition of caspase-8 then unleashes necroptosis, which kills the infected cell anyway and releases inflammatory signals, so the pathway acts as a backup that turns the viral countermeasure into a trigger.

6. In the model of Example 25.7.1, estimate the replicative lifespan if (a) the loss per division doubles because of oxidative stress, (b) the standard deviation of initial lengths doubles, (c) the cells express telomerase at a level that adds back 60 bp per division. Which is more effective at delaying senescence of a cell population, raising the average telomere length or eliminating the shortest telomeres, and why?

   **Answer** With $K \approx (L_0 - 2.5\sigma_0 - L_{\mathrm{c}})/\bar\Delta$ and $L_0 = 10$, $\sigma_0 = 1.5$, $L_{\mathrm{c}} = 1.5\,\mathrm{kb}$: the numerator is about $4.75\,\mathrm{kb}$, and $K \approx 59$ at $\bar\Delta = 80\,\mathrm{bp}$. (a) $\bar\Delta = 160\,\mathrm{bp}$: $K \approx 30$. (b) $\sigma_0 = 3\,\mathrm{kb}$: numerator $10 - 7.5 - 1.5 = 1\,\mathrm{kb}$, $K \approx 12$ (some cells would start below the limit). (c) Net loss $20\,\mathrm{bp}$: $K \approx 240$, effectively a fourfold extension (in reality telomerase preferentially elongates the shortest telomeres, so the extension would be larger). Because the shortest telomere triggers the DNA damage response, eliminating the short tail of the distribution matters more than the mean; a treatment that lengthens all telomeres equally helps by the same amount it adds to the minimum, whereas one that preferentially rescues the shortest gains up to $2.5\sigma_0/\bar\Delta \approx 47$ divisions.

7. Senescent cells resist apoptosis yet are killed by navitoclax. Reconcile these facts. Suggest why the SASP might help clear senescent cells in a young animal but promote disease in an old one, using Eq. (25.3).

   **Answer** Senescent cells express high levels of BH3-only proteins and p53 targets (they are "primed" for death) but survive because they up-regulate Bcl-xL, Bcl-2 and Bcl-w and other survival pathways; this dependence makes them resistant to many stresses but very sensitive to inhibition of the specific anti-apoptotic proteins, as in the BH3-profiling logic of 25.4.3. The SASP recruits immune cells (NK cells, macrophages, T cells) that remove senescent cells; in a young animal production $\eta t$ is small compared with the maximal removal rate $\beta$, so $X$ stays low and each senescent cell is short-lived, and the SASP is transient and useful (repair, tumor suppression). In an old animal production approaches saturation of removal, so $X$ rises steeply, turnover slows, and the persistent SASP from many cells causes chronic inflammation, paracrine senescence and tissue dysfunction; removal itself may also decline as the immune system ages, which lowers $\beta$ and accelerates the accumulation.
