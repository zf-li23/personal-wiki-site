---
title: The Nuclear Envelope and Nucleocytoplasmic Transport
description: The components of the nucleus; the nuclear envelope (inner and outer membranes, perinuclear space, targeting of inner-membrane proteins, LINC complexes); the nuclear lamina, lamin processing, laminopathies and progeria; the nuclear matrix as an operational concept; the nuclear pore complex (architecture, FG-repeat barrier, soft size limit of passive diffusion); nuclear localization and export signals, karyopherins and the Ran gradient, the thermodynamic limit of accumulation, RNA export and regulated access; breakdown and reassembly of the envelope and NPC assembly; nuclear size scaling and the origin of the nucleus.
---

The nucleus is the defining organelle of eukaryotes, and its boundary, the nuclear envelope, is what separates the two halves of gene expression: DNA replication, transcription and RNA processing inside, translation outside. That separation has a price. Every protein that works in the nucleus, from histones and polymerases to transcription regulators, is made in the cytosol and must be imported, and every RNA that works in the cytosol must be exported, at a rate of up to a thousand macromolecules per second through each pore. It also has a payoff: a cell can regulate gene expression simply by deciding which proteins and RNAs may cross, and when. This chapter treats the nucleus as a compartment. We describe its components (16.1), the double membrane of the envelope and its links to the cytoskeleton (16.2), the lamina that supports it and the diseases caused by its defects (16.3), the nuclear pore complex and its permeability barrier (16.4), and the receptor- and Ran-driven machinery of active transport, with a model that shows where its energy goes (16.5). We then follow the envelope through mitosis (16.6) and ask what sets the size of the nucleus and how it arose (16.7). The contents of the nucleus, chromatin, chromosomes and the nucleolus, are the subject of [7.3.17](/7.3.17); the molecular structure of chromatin is treated in [7.2.4](/7.2.4) and the regulation of transcription in [7.2.12](/7.2.12)–[7.2.15](/7.2.15). **Gated transport** through nuclear pores is one of the three modes of **protein sorting** introduced in [7.3.6](/7.3.6).

## 16.1. The Components of the Nucleus

A typical animal nucleus is a sphere or flattened ellipsoid $5$–$10\,\mu\mathrm{m}$ across, occupying about $6$–$10\%$ of the volume of the cell. Its parts are:

| Component | Structure | Main functions |
|---|---|---|
| Nuclear envelope | two lipid bilayers (inner and outer nuclear membranes) enclosing the perinuclear space, continuous with the ER | barrier between nucleoplasm and cytoplasm; anchoring of lamina and chromatin; link to the cytoskeleton |
| Nuclear pore complexes | about $3000$–$4000$ channels of $\sim 110$–$125\,\mathrm{MDa}$ each in a mammalian nucleus | all exchange between nucleus and cytoplasm |
| Nuclear lamina | meshwork of lamin filaments on the inner face of the envelope | mechanical support, anchoring of chromatin and pores, nuclear assembly |
| Chromatin | DNA with histones and other proteins, organized into chromosome territories | storage, replication, transcription of the genome ([7.3.17](/7.3.17)) |
| Nucleolus and nuclear bodies | membraneless **biomolecular condensates** | ribosome biogenesis; RNA processing ([7.3.17](/7.3.17)) |
| Nucleoplasm | the aqueous phase between these structures, continuous with the cytosol through the pores | site of transcription and RNA processing |

Two features distinguish the nucleus from the other membrane-enclosed **organelles**. First, its lumen, the nucleoplasm, is topologically equivalent to the cytosol: the pores are open holes, through which ions and small molecules pass freely. The nucleus is therefore a compartment for macromolecules only, and its composition differs from the cytosol's because of selective transport, not because of a membrane impermeable to solutes. Second, in most animal and plant cells it is dismantled at every mitosis and rebuilt in each daughter cell (16.6). Two questions raised by its appearance, why it is round and what sets its size, are taken up in 16.7.

## 16.2. The Nuclear Envelope

### 16.2.1. Two Membranes and a Perinuclear Space

**Definition 16.2.1 (Nuclear Envelope)** The **nuclear envelope** is the double membrane that encloses the nucleus. It consists of the **inner nuclear membrane** (INM), facing the nucleoplasm and lined by the lamina; the **outer nuclear membrane** (ONM), facing the cytoplasm and continuous with the membrane of the endoplasmic reticulum; and the **perinuclear space** between them, $20$–$50\,\mathrm{nm}$ wide and continuous with the ER lumen. The two membranes are joined at the **pore membrane**, the sharply curved membrane that lines each nuclear pore and holds a nuclear pore complex.

The envelope is thus a specialized domain of the **endoplasmic reticulum**, folded around the chromosomes. The ONM resembles **rough ER**: it carries ribosomes on its cytosolic face and makes proteins that enter the perinuclear space, and in many cells it is the site of ER functions such as calcium storage. The INM, although its lipids are continuous with the ONM through the pore membrane, has a distinct set of proteins: in mammals several dozen transmembrane proteins concentrated in the INM, among them the lamin B receptor (LBR), the LEM-domain proteins emerin, LAP2 and MAN1 (named after a shared domain that binds the chromatin protein BAF), and the SUN proteins of the LINC complex (16.2.3). These proteins bind the lamina and chromatin and give the INM its function as the chromatin-facing surface of the nucleus.

### 16.2.2. How Proteins Reach the Inner Nuclear Membrane

Proteins of the INM are inserted into the ER membrane by the same machinery as other membrane proteins ([7.3.6](/7.3.6)). How do they reach the INM, and why do they stay there? The main answer is the diffusion–retention model. A newly made INM protein diffuses laterally in the continuous membrane from the ER to the ONM, through the pore membrane, which it passes along peripheral channels of about $10\,\mathrm{nm}$ between the scaffold of the nuclear pore complex and the bilayer, and into the INM. There it binds lamins or chromatin and is immobilized; proteins that do not bind diffuse back. Two observations support the model. In **fluorescence recovery after photobleaching** experiments, LBR fused to **green fluorescent protein** is mobile in the ER but nearly immobile in the INM (Ellenberg and colleagues, 1997), and its retention depends on its lamin-binding domain. And a nucleoplasmic domain larger than about $60\,\mathrm{kDa}$ prevents a membrane protein from reaching the INM, because it cannot pass the peripheral channels. Some INM proteins of yeast (Heh1 and Heh2) carry a nuclear localization signal in a long linker, and use importins and Ran (16.5) to cross the pore while remaining in the membrane, a hybrid of diffusion and active transport.

**Example 16.2.1** Suppose that the free (unbound) form of an INM protein equilibrates by diffusion between the ER and the INM, so that its concentration in the membrane is the same everywhere, $c_{\mathrm{f}}$, and that in the INM it also binds lamina sites of concentration $B$ (per unit area, $B \gg c_{\mathrm{f}}$) with dissociation constant $K$ (in the same units). The bound concentration is $c_{\mathrm{f}}B/(K + c_{\mathrm{f}}) \approx c_{\mathrm{f}}B/K$, so the protein is enriched in the INM relative to the ER by the factor

$$
E = \frac{c_{\mathrm{f}} + c_{\mathrm{f}}B/K}{c_{\mathrm{f}}} = 1 + \frac{B}{K}.
$$
An enrichment of a hundredfold, typical of lamina-binding proteins, requires only $B/K \approx 100$: binding sites in excess of the dissociation constant by two orders of magnitude, with no energy input beyond that of synthesis. The INM proteome is a steady state of diffusion and binding, like the sorting of proteins in other continuous membranes.

### 16.2.3. LINC Complexes Connect the Nucleus to the Cytoskeleton

**Definition 16.2.2 (LINC Complex)** A **LINC complex** (linker of nucleoskeleton and cytoskeleton) is a protein bridge across the nuclear envelope formed by SUN proteins (Sad1–UNC-84 homology), trimers anchored in the INM whose SUN domains lie in the perinuclear space, and KASH proteins (Klarsicht–ANC-1–Syne homology; the nesprins in mammals), anchored in the ONM, whose short C-terminal KASH peptide reaches into the perinuclear space and is clamped between SUN domains. On the nucleoplasmic side, SUN proteins bind lamins and chromatin proteins; on the cytoplasmic side, nesprins bind actin filaments (the giant isoforms of nesprin-1 and -2), intermediate filaments through plectin (nesprin-3), or microtubule motors (nesprin-4, and adaptors for kinesin and dynein).

LINC complexes transmit force in both directions. They position and move the nucleus: nuclei are anchored at the periphery of muscle fibers and move along microtubules in migrating neurons, and in fibroblasts that orient towards a wound, actin cables coupled to nesprins drag the nucleus rearward ("transmembrane actin-associated nuclear lines"). They couple the centrosome to the nucleus. They transmit mechanical stress from the cell surface to the lamina and chromatin, which is one route of mechanotransduction. In meiotic prophase, SUN–KASH complexes attach telomeres to cytoplasmic dynein, whose movements along microtubules shuffle the chromosomes and help homologues to pair ([7.3.21](/7.3.21)). The SUN–KASH bridge also spans the perinuclear space at a fixed length and so contributes to the even spacing of the two membranes: in some cell types depletion of SUN proteins lets the perinuclear space dilate locally.

![The nuclear envelope in section (schematic; perinuclear space and pores enlarged relative to the membranes). A: the outer nuclear membrane (ONM), with ribosomes on its cytosolic face, is continuous with the ER, and the perinuclear space with the ER lumen; the inner nuclear membrane (INM) is lined by the lamina, to which peripheral heterochromatin is attached. Inner and outer membranes join at the pore membrane of each nuclear pore complex. A LINC complex crosses the envelope: a SUN protein in the INM binds the KASH peptide of a nesprin in the ONM, whose spectrin-repeat rod reaches an actin filament. B: a nuclear pore complex in side view, with its cytoplasmic filaments, cytoplasmic ring, inner ring lining the pore membrane, nuclear ring and nuclear basket; the central channel is filled with the disordered FG-repeat domains of the channel nucleoporins. C: face view, showing the eightfold symmetry of the scaffold around the central channel](./plots/nuclear-envelope.py)

## 16.3. The Nuclear Lamina

### 16.3.1. Lamins

**Definition 16.3.1 (Nuclear Lamina)** The **nuclear lamina** is a meshwork of protein filaments, $10$–$30\,\mathrm{nm}$ thick, on the nucleoplasmic face of the inner nuclear membrane, attached to INM proteins, nuclear pore complexes and chromatin. Its main components are **lamins**, the type V intermediate filament proteins, which are the only intermediate filaments of the nucleus and the evolutionarily oldest members of the family. Vertebrates have A-type lamins (lamin A and lamin C, made from one gene, *LMNA*, by alternative splicing; expressed mainly in differentiated cells) and B-type lamins (lamins B1 and B2, from *LMNB1* and *LMNB2*; expressed in all cells).

Lamins share the domain organization of cytoplasmic intermediate filament proteins ([7.3.15](/7.3.15)): a short head, a central α-helical rod domain that forms a parallel **coiled coil** with a partner, and a tail, which in lamins carries a nuclear localization signal, a globular immunoglobulin-like fold, and (except in lamin C) a C-terminal CaaX motif (Cys, two aliphatic residues, any residue). Dimers associate head to tail into polymers, which associate laterally. **Cryo-electron tomography** of mammalian nuclei shows the assembled lamina as a meshwork of filaments only $3.5\,\mathrm{nm}$ thick, much thinner than the $10\,\mathrm{nm}$ filaments of the cytoplasm, in which A- and B-type lamins form separate but interacting networks (Turgay and colleagues, 2017).

The CaaX motif is the substrate of a sequence of modifications that anchor lamins to the membrane. A farnesyltransferase attaches a farnesyl group, a 15-carbon **isoprenoid**, to the cysteine by a thioether bond; a protease removes the three terminal residues; and a methyltransferase esterifies the new C-terminal carboxyl group. B-type lamins keep this hydrophobic, methylated tail permanently and therefore stay attached to membranes even when the lamina disassembles at mitosis. Lamin A is made as prelamin A, which after farnesylation is cleaved a second time, 15 residues upstream, by the zinc metalloprotease ZMPSTE24; mature lamin A is thus not farnesylated and is more soluble, and lamin C, which lacks the CaaX motif, is never modified.

### 16.3.2. What the Lamina Does

| Function | Evidence |
|---|---|
| Mechanical support of the nucleus | nuclei lacking A-type lamins are soft, deform easily and rupture when cells squeeze through narrow constrictions; the amount of lamin A scales with the stiffness of tissues (low in brain, high in bone and muscle) |
| Anchoring of pores and INM proteins | without B-type lamins, pores cluster; emerin and other INM proteins mislocalize to the ER when lamin A is absent |
| Anchoring of heterochromatin | lamina-associated domains of chromatin ([7.3.17](/7.3.17)); in cells lacking both lamin A/C and LBR, heterochromatin moves to the nuclear center |
| Nuclear assembly and growth | lamin depletion in *Xenopus* egg extracts gives small, fragile nuclei that fail to replicate DNA |
| Gene regulation and signaling | lamins and LEM-domain proteins bind transcription factors (such as the retinoblastoma protein and SREBP1) and sequester them at the periphery |
| DNA replication and repair | lamin defects impair replication fork progression and repair of double-strand breaks |

Ruptures of the envelope in migrating cells (for instance tumor cells moving through dense tissue) are transient: chromatin herniates through the gap, nuclear and cytoplasmic proteins mix for minutes, and the hole is sealed by the **ESCRT** machinery, the same membrane-scission system that forms intraluminal vesicles in **endosomes** ([7.3.10](/7.3.10)) and closes the envelope after mitosis (16.6.3). Repeated rupture causes DNA damage, linking nuclear mechanics to genome stability.

### 16.3.3. Laminopathies and Progeria

**Definition 16.3.2 (Laminopathy)** A **laminopathy** (nuclear envelopathy) is an inherited disease caused by mutations in genes for lamins, the enzymes that process them, or proteins of the nuclear envelope that interact with them.

More than 500 mutations in *LMNA* alone are known, with strikingly tissue-specific consequences:

| Disease | Gene | Affected tissues |
|---|---|---|
| Emery–Dreifuss muscular dystrophy | *EMD* (emerin; X-linked); *LMNA* (autosomal) | skeletal muscle, joint contractures, cardiac conduction |
| Dilated cardiomyopathy with conduction defects | *LMNA* | heart |
| Familial partial lipodystrophy (Dunnigan type) | *LMNA* (often Arg482) | loss of subcutaneous fat, insulin resistance, diabetes |
| Charcot–Marie–Tooth disease type 2B1 | *LMNA* | peripheral nerves |
| Hutchinson–Gilford progeria syndrome | *LMNA* (G608G) | premature aging (below) |
| Restrictive dermopathy; mandibuloacral dysplasia type B | *ZMPSTE24* | skin, bone; lethal at birth when the protease is absent |
| Pelger–Huët anomaly (heterozygous); Greenberg skeletal dysplasia (homozygous) | *LBR* | neutrophil nuclear shape; lethal skeletal dysplasia |
| Adult-onset autosomal dominant leukodystrophy | *LMNB1* (duplication) | central nervous system myelin |

**Definition 16.3.3 (Hutchinson–Gilford Progeria Syndrome)** **Hutchinson–Gilford progeria syndrome** (HGPS) is a rare dominant disease of premature aging caused, in most cases, by a de novo point mutation in exon 11 of *LMNA* (c.1824C>T, a silent change of Gly608) that activates a cryptic 5′ splice site; the resulting mRNA lacks 150 nucleotides, and the protein, **progerin**, lacks 50 amino acids including the ZMPSTE24 cleavage site, so that it remains permanently farnesylated and anchored to the inner nuclear membrane.

Children with HGPS appear healthy at birth but stop growing in the first years and develop alopecia, loss of subcutaneous fat, joint stiffness and, decisively, accelerated atherosclerosis; they die at a mean age of about 14.5 years from heart attack or stroke. At the cellular level progerin acts as a dominant negative: nuclei become lobulated and blebbed, peripheral heterochromatin is lost, DNA damage accumulates, and cells enter senescence early ([7.3.25](/7.3.25)). Both the mutation (identified in 2003 by two groups) and the mechanism, a lamin that cannot be released from its lipid anchor, suggested a treatment: the farnesyltransferase inhibitor lonafarnib, approved in 2020, reduces nuclear blebbing in cells and extends the mean survival of patients by about two and a half years. Mice lacking ZMPSTE24, which accumulate unprocessed prelamin A, age prematurely in the same way. Progerin is also made at low levels, by use of the same cryptic splice site, in cells of healthy old people, and cells of elderly donors show some of the same nuclear defects (Scaffidi and Misteli, 2006), although whether progerin contributes to normal aging remains uncertain.

![Lamin structure and processing. A: domain organization of the lamins (schematic, approximately to scale in residues): head, α-helical rod with its coiled-coil segments, nuclear localization signal (NLS), immunoglobulin-like fold (Ig) and C-terminal CaaX motif. Lamin C, an alternatively spliced product of LMNA, ends before the CaaX motif. B: processing of prelamin A: farnesylation of the CaaX cysteine, removal of -aaX, carboxymethylation, and cleavage by ZMPSTE24 that removes the farnesylated C-terminal 15 residues, releasing mature lamin A. B-type lamins stop after carboxymethylation and stay farnesylated. C: in progerin, the mutation G608G activates a cryptic splice site that deletes 50 residues of exon 11 including the ZMPSTE24 site; the protein remains farnesylated and methylated](./plots/lamin-processing.py)

### 16.3.4. The Nuclear Matrix: An Operational Definition

**Definition 16.3.4 (Nuclear Matrix)** The **nuclear matrix** (nucleoskeleton) is the insoluble residue that remains when nuclei are treated with nonionic detergent, digested with nucleases and extracted with high salt (typically $2\,\mathrm{M}\ \ce{NaCl}$): a fibrogranular network of protein and RNA attached to the remnants of the lamina, nucleoli and pores (Berezney and Coffey, 1974). It is defined by the procedure, as the material that is left after everything that can be extracted has been removed.

Analysis of such residues identified topoisomerase II, matrins, scaffold attachment factor A (SAF-A, also called hnRNP U), lamins, and many enzymes of DNA and RNA metabolism, transcription factors and **nuclear receptors**. Replicating DNA and nascent RNA were found attached to the residue, and AT-rich DNA sequences that bind it (scaffold or matrix attachment regions, S/MARs) were mapped near the bases of chromatin loops. The matrix was therefore proposed as a nuclear counterpart of the cytoskeleton: a scaffold for chromatin loops, a solid support for replication and transcription, and a framework for RNA processing and viral assembly.

The concept remains controversial, and the evidence for a continuous filament network is weak. The structures obtained depend on the extraction conditions, and high salt can precipitate proteins and RNA into artifactual aggregates. No network of filaments other than the lamina has been seen in intact nuclei by **cryo-electron tomography**, and live-cell experiments show that most "matrix" proteins exchange rapidly. Many of the properties attributed to the matrix are now explained by other structures: loops are anchored by cohesin and CTCF (**loop extrusion**, [7.2.4](/7.2.4#sec-4.3.2)); replication and transcription occur in clustered factories and **biomolecular condensates** ([7.2.21](/7.2.21)); and SAF-A binds both chromatin and nuclear RNA and may organize chromatin through an RNA "mesh". The similar residue of mitotic chromosomes, the chromosome scaffold rich in topoisomerase II and condensin (Paulson and Laemmli, 1977), corresponds to the axis of condensin complexes at the bases of nested loops ([7.2.4](/7.2.4#sec-4.3.3)). The nucleus is highly organized, but by chromatin, RNA and condensates rather than by a matrix analogous to the cytoskeleton.

## 16.4. The Nuclear Pore Complex

### 16.4.1. Architecture

**Definition 16.4.1 (Nuclear Pore Complex)** A **nuclear pore complex** (NPC) is the large protein assembly that occupies each pore of the nuclear envelope and mediates all exchange between nucleus and cytoplasm. It is built of about 30 different proteins, the **nucleoporins** (Nups), each present in multiples of eight copies, $500$–$1000$ molecules in total ($\sim 60\,\mathrm{MDa}$ in yeast, $\sim 110$–$125\,\mathrm{MDa}$ in vertebrates). The NPC has eightfold rotational symmetry around the transport axis and is nearly symmetric across the plane of the envelope: a scaffold of an inner ring and two outer rings (cytoplasmic and nuclear) surrounds a central channel, with cytoplasmic filaments on one face and a nuclear basket on the other.

The nucleoporins fall into a few structural classes:

| Class | Examples (vertebrate) | Location and role |
|---|---|---|
| Transmembrane | POM121, NDC1, GP210 | anchor the NPC in the pore membrane |
| Scaffold: outer rings | Y complex (Nup107–Nup160 complex, with SEH1 and SEC13), in two concentric rings of eight on each face | cytoplasmic and nuclear rings |
| Scaffold: inner ring | Nup93 complex (Nup205, Nup188, Nup155, Nup35) | lines the pore membrane; binds the channel Nups |
| Channel (FG) nucleoporins | Nup62–Nup58–Nup54 complex, Nup98 | disordered FG-repeat domains fill the channel |
| Cytoplasmic filaments | Nup358 (RanBP2), Nup214, Nup88 | docking of transport complexes; RanGAP binding; mRNA remodeling |
| Nuclear basket | TPR, Nup153, Nup50 | docking of import and export complexes; mRNA quality control |

The scaffold Nups are built from β-propellers and α-solenoids, the same folds as the **clathrin** and **COPII** coats of **transport vesicles** ([7.3.8](/7.3.8)), and SEC13 is a subunit of both the Y complex and the COPII coat. This shared "protocoatomer" architecture suggests that pores and coats descend from an ancestral membrane-bending module of the early endomembrane system (16.7.2). Structures of the human NPC that combine **cryo-electron tomography** of nuclear envelopes in cells with structure predictions of the nucleoporins now account for most of the scaffold at near-atomic detail (2022). They also showed that the pore is dynamic: the diameter of the central channel is about $40$–$60\,\mathrm{nm}$ in intact cells and constricts when cells are depleted of energy or exposed to hyperosmotic stress, because the scaffold rings respond to the tension of the nuclear envelope.

The classical images of NPCs came from thin sections, **negative staining** of isolated envelopes and **freeze-fracture electron microscopy**, which showed the octagonal outline and the "fish-trap" of filaments and basket; in living cells, an NPC component fused to GFP (POM121–GFP, for example) labels the envelope as a fine punctate rim. A mammalian nucleus has about $3000$–$4000$ NPCs, at a density of about $10$–$20$ per $\mu\mathrm{m}^2$ of envelope, but the number varies widely: a few hundred in small glial nuclei, nearly $2 \times 10^4$ in large Purkinje neurons, and some $5 \times 10^7$ in the giant nucleus (germinal vesicle) of a *Xenopus* oocyte. NPCs are assembled both at the end of mitosis and during interphase (16.6.3), and their number grows with the surface of the nucleus and with its transcriptional activity. In nondividing neurons the scaffold nucleoporins are among the longest-lived proteins of the body, persisting for years, and their slow deterioration with age has been linked to leakiness of the barrier.

### 16.4.2. The Permeability Barrier

The central channel is not empty. It is filled with the intrinsically disordered domains of the FG nucleoporins.

**Definition 16.4.2 (FG Repeat)** An **FG repeat** is a short motif containing phenylalanine and glycine (FG, FxFG or GLFG), repeated tens of times, separated by hydrophilic spacers, in the intrinsically disordered regions of about a third of the nucleoporins (the FG nucleoporins). A single NPC contains several thousand FG motifs anchored to the scaffold and filling the central channel, where their weak hydrophobic interactions form the permeability barrier.

The FG domains are **intrinsically disordered regions** of the kind that drive condensate formation ([7.2.21](/7.2.21)). How they form a selective barrier is debated, but several models converge on a common principle. In the selective-phase (hydrogel) model, FG domains interact with each other to form a sieve-like gel or condensed phase: purified FG domains form hydrogels, and condensates, that exclude inert proteins of the size of mCherry but are entered more than a thousand times faster by transport receptors, which bind FG motifs (Frey and Görlich, 2006; Schmidt and Görlich, 2016). In the polymer-brush ("virtual gate") model, FG domains form an entropic brush that repels large inert molecules. In both, a molecule enters the channel if its interactions with FG motifs pay for the disruption of FG–FG contacts, which only transport receptors and their complexes do; and in both the barrier is soft, a gradual exclusion rather than a hole of fixed size.

Small molecules and ions pass the NPC essentially unhindered. For larger molecules, the rate of passive diffusion falls steeply but continuously with size. The older statement that the pore is an aqueous channel about $9\,\mathrm{nm}$ in diameter that admits globular proteins below $40$–$60\,\mathrm{kDa}$ and excludes larger ones describes a sieve that does not exist: systematic measurements in yeast (Timney and colleagues, 2016) and mammalian cells show no sharp cutoff, and proteins of more than $100\,\mathrm{kDa}$ still leak slowly. The $60\,\mathrm{kDa}$ "limit" is the size at which passive equilibration becomes slow compared with the lifetime of a protein or the duration of interphase. A simple physical model reproduces this soft behavior.

**Proposition 16.4.1 (Passive Equilibration Through a Mesh)** Consider $n$ pores, each a channel of cross-section $A$ and length $L$ filled with a random network of fibers of radius $r_{\mathrm{f}}$ occupying the volume fraction $\varphi$. A globular protein of radius $a$ partitions into the network with the Ogston coefficient

$$
K(a) = \exp\!\left[-\varphi\left(1 + \frac{a}{r_{\mathrm{f}}}\right)^2\right]
\tag{16.1}
$$
and diffuses in it with diffusion coefficient $D(a)$. If the cytoplasmic concentration $c_{\mathrm{c}}$ is held constant, the nuclear concentration approaches it as $c_{\mathrm{n}}(t) = c_{\mathrm{c}}(1 - \mathrm{e}^{-t/\tau})$, with

$$
\tau(a) = \frac{L\,V_{\mathrm{n}}}{n\,A\,D(a)\,K(a)},
\tag{16.2}
$$
where $V_{\mathrm{n}}$ is the nuclear volume.

**Proof** In each channel the flux is diffusive (**Fick's law**) with the concentrations just inside the two ends equal to $Kc_{\mathrm{c}}$ and $Kc_{\mathrm{n}}$, so the total flux into the nucleus is $J = nAD K(c_{\mathrm{c}} - c_{\mathrm{n}})/L$. Then $V_{\mathrm{n}}\,\mathrm{d}c_{\mathrm{n}}/\mathrm{d}t = J$ is a linear equation with relaxation time (16.2) and fixed point $c_{\mathrm{n}} = c_{\mathrm{c}}$. $\square$

With $D \propto 1/a$ (the **Stokes–Einstein equation**) and the radius of a globular protein of mass $M$ approximately $a \approx 0.066\,M^{1/3}\,\mathrm{nm}$ ($M$ in daltons), $\ln\tau$ grows as $\varphi(1 + a/r_{\mathrm{f}})^2$, roughly as $M^{2/3}$: each increment of size multiplies the equilibration time by a factor, without a threshold. By contrast, a rigid cylindrical pore of radius $R$ excludes molecules with $a \ge R$ completely, and permeability falls to zero at a sharp cutoff. Binding to FG repeats changes the picture qualitatively: if a receptor gains free energy $\varepsilon$ per FG contact for $m$ contacts, its partition coefficient is multiplied by $\mathrm{e}^{m\varepsilon/k_{\mathrm{B}}T}$, so that a complex of $150\,\mathrm{kDa}$ or more enters the channel more readily than a small inert protein. Selectivity is therefore a property of partitioning, not of size alone.

![Passive diffusion through the NPC is limited by a soft barrier. A: relative permeability per pore (normalized to a 1-kDa molecule) as a function of the molecular mass of a globular protein, for a rigid aqueous channel of 9 nm diameter (hindered diffusion, Renkin equation) and for a channel filled with an FG mesh (Ogston partition, Eq. (16.1), volume fraction 0.1, fiber radius 0.5 nm). The two models agree for small proteins, but the rigid channel has a sharp cutoff where the protein radius equals the pore radius (about 300 kDa), whereas the mesh gives a steep, continuous decline with no size at which permeability vanishes; the dotted line marks the classical 60-kDa "limit". B: kinetics of nuclear accumulation of inert proteins of 10, 27 (GFP), 60 and 110 kDa injected into the cytoplasm, from Eq. (16.2) with the mesh model, calibrated so that a GFP-sized protein equilibrates with a time constant of about two minutes. The dashed curve shows a 110-kDa cargo bound to a transport receptor whose FG binding raises its partition coefficient a thousandfold](./plots/passive-diffusion.py)

## 16.5. Active Transport Through the Pore

### 16.5.1. Nuclear Localization and Export Signals

Experiments in the early 1980s established that nuclear import is signal-mediated. Nucleoplasmin, an abundant pentameric protein of *Xenopus* oocyte nuclei, reaccumulated in the nucleus when injected into the cytoplasm; its protease-resistant core did not, but its tails did, and a single tail was enough to bring the pentamer in (Dingwall, Laskey and colleagues, 1982). Gold particles coated with nucleoplasmin and injected into the cytoplasm were seen by electron microscopy to gather at the cytoplasmic filaments and pass through the center of the pores (Feldherr and colleagues, 1984), with particles up to about $26\,\mathrm{nm}$ in diameter transported, later extended to $39\,\mathrm{nm}$ (Panté and Kann, 2002). In 1984 Kalderon, Smith and colleagues identified the signal of the SV40 large T antigen, Pro-Lys-Lys-Lys-Arg-Lys-Val: a single Lys-to-Thr substitution in it kept the protein in the cytoplasm, and the peptide fused to cytosolic proteins brought them into the nucleus.

**Definition 16.5.1 (Nuclear Localization and Export Signals)** A **nuclear localization signal** (NLS) is a sorting signal that directs a protein into the nucleus by binding a nuclear import receptor. The classical NLS is either a single cluster of basic residues (monopartite, such as the SV40 T antigen signal PKKKRKV) or two clusters separated by a spacer of about 10 residues (bipartite, such as the nucleoplasmin signal KRPAATKKAGQAKKKK); other NLSs include the PY-NLS (an extended signal ending in Pro-Tyr, recognized by transportin). A **nuclear export signal** (NES) directs a protein out of the nucleus by binding an export receptor; the classical NES is a short leucine-rich motif with regularly spaced hydrophobic residues, first found in the HIV Rev protein and the protein kinase A inhibitor PKI, and recognized by exportin 1 (CRM1).

Nuclear localization signals differ from most other **sorting signals** in that they are not removed after transport: they can be anywhere in the sequence, usually in exposed loops, and remain functional, so a nuclear protein can be imported again each time the nucleus reassembles after mitosis. A complex needs only one subunit with an NLS. Transport through the pore also differs from translocation into the ER, mitochondria or plastids ([7.3.6](/7.3.6)): the channel is constitutively open and large, so proteins cross folded and complexes cross assembled, in both directions at once.

### 16.5.2. Karyopherins

**Definition 16.5.2 (Karyopherin)** The **karyopherins** are the family of nuclear transport receptors (in humans about 20; β-karyopherins) that bind both their cargoes and FG repeats and shuttle between nucleus and cytoplasm. Each is a superhelix of 19–20 HEAT repeats, an α-solenoid that wraps around its cargo and binds Ran-GTP. Karyopherins that carry cargo into the nucleus are **importins**, and those that carry cargo out are **exportins**; a few (exportin 4, importin 13) work in both directions.

| Receptor | Direction | Cargo (signal) |
|---|---|---|
| Importin β1 with the adaptor importin α | import | proteins with a classical NLS |
| Importin β1 directly | import | some ribosomal proteins, snurportin-bound snRNPs, HIV Rev |
| Transportin 1 (importin β2) | import | PY-NLS proteins (hnRNP A1, FUS) |
| Importin 7, importin 5 | import | histones, ribosomal proteins |
| Exportin 1 (CRM1) | export | leucine-rich NES proteins; pre-ribosomal subunits; snRNAs with adaptors |
| CAS (exportin 2) | export | importin α (recycling) |
| Exportin-t | export | tRNA |
| Exportin 5 | export | pre-miRNA ([7.2.18](/7.2.18)) |
| NTF2 (not a karyopherin) | import | Ran-GDP |

Importin α is an adaptor rather than a karyopherin: its armadillo-repeat domain binds the classical NLS, and its N-terminal IBB domain (importin β-binding) binds importin β. When importin α is free, the IBB domain folds back into its own NLS-binding groove, an autoinhibition that prevents empty importin α from competing for importin β. The FG-binding pockets on the convex surface of the karyopherins let them partition into the FG phase of the channel and move through it by repeated binding and release; the pore lets receptors diffuse quickly but gives the diffusion no direction.

### 16.5.3. The Ran Gradient Gives Direction

**Definition 16.5.3 (Ran)** **Ran** is a small GTPase of the Ras superfamily that controls nucleocytoplasmic transport (and the assembly of the mitotic spindle and of the nuclear envelope). Its guanine nucleotide-exchange factor, RCC1, is bound to chromatin (it binds nucleosomes) and is therefore nuclear; its GTPase-activating protein, RanGAP1, aided by the Ran-binding proteins RanBP1 and RanBP2, is cytoplasmic, attached in vertebrates to the cytoplasmic filaments of the NPC. As a result Ran is mostly in its GTP-bound form (Ran-GTP) in the nucleus and in its GDP-bound form (Ran-GDP) in the cytoplasm.

Like every **small G protein** ([7.1.15](/7.1.15)), Ran is switched on by a **guanine nucleotide-exchange factor** and off by a **GTPase-activating protein**; what is special is that the two regulators are in different compartments. The asymmetric localization of GEF and GAP, not of Ran itself, creates the gradient. Its existence was visualized directly with fluorescent sensors that change **Förster resonance energy transfer** when bound by Ran-GTP (Kalab, Weis and Heald, 2002), and its magnitude is estimated at several hundredfold or more. Karyopherins read the gradient by the way Ran-GTP affects their cargo binding:

- Importins bind cargo in the cytoplasm, where Ran-GTP is absent. In the nucleus, Ran-GTP binds importin β and releases the cargo (and importin α with it); the importin β–Ran-GTP complex returns to the cytoplasm, where RanGAP triggers GTP hydrolysis and Ran-GDP dissociates, freeing importin β for another cycle. Importin α is returned by the exportin CAS together with Ran-GTP.
- Exportins bind cargo only together with Ran-GTP, so the ternary complex exportin–Ran-GTP–cargo forms in the nucleus. In the cytoplasm, GTP hydrolysis dissolves it and releases the cargo.
- Ran-GDP is brought back into the nucleus by its own carrier, NTF2, and RCC1 exchanges its GDP for GTP.

Each cycle of import or export thus moves one molecule of Ran-GTP from nucleus to cytoplasm, where its GTP is hydrolyzed: the energy for transport comes from GTP, consumed by Ran, and not from ATP. (Active transport of mRNA, which uses ATP, is the exception, 16.5.5.) Directionality comes entirely from the compartment-specific release of cargo, and the demonstration is that it can be inverted: in permeabilized cells (the digitonin-permeabilized cell assay, in which the plasma membrane is opened and the nuclei are supplied with recombinant factors), an inverted Ran gradient, with Ran-GTP added outside and Ran-GAP inside, drove import cargo out of the nucleus (Nachury and Weis, 1999).

![The Ran cycle and the transport cycles of importins and exportins (cytoplasm above, nucleus below). Import (left): importin β, bound to cargo through the adaptor importin α and its NLS, crosses the NPC; in the nucleus Ran-GTP (T) binds importin β and releases importin α and cargo, and the importin β–Ran-GTP complex returns. Export (right): an exportin binds an NES cargo together with Ran-GTP in the nucleus; the ternary complex crosses the pore. In the cytoplasm RanGAP, helped by RanBP1 and RanBP2 on the cytoplasmic filaments, makes Ran hydrolyze its GTP, releasing the receptors and the export cargo; Ran-GDP (D) returns with NTF2, and RCC1 on chromatin exchanges GDP for GTP. Importin α is re-exported by CAS with Ran-GTP (not shown). Each cycle consumes one GTP](./plots/ran-cycle.py)

The Ran system is a pump that converts the free energy of GTP hydrolysis into a concentration gradient of cargo. How steep a gradient can it make? A minimal model gives a clean answer.

**Proposition 16.5.1 (The Ran Gradient Limits Accumulation)** Let cargo $C$, importin $I$ and Ran-GTP $G$ occupy the nucleus (n) and cytoplasm (c). In each compartment, importin binds cargo or Ran-GTP, but not both, with association constants $K_1$ and $K_2$ (fast equilibria: $[IC] = K_1[I][C]$, $[IG] = K_2[I][G]$). Importin and its complexes cross the pore with equal permeability, free cargo crosses passively with permeability $k_{\mathrm{p}}$, and the Ran-GTP concentrations $G_{\mathrm{n}}$ and $G_{\mathrm{c}}$ are held fixed by RCC1 and RanGAP. If $k_{\mathrm{p}} = 0$, the steady-state accumulation ratio of free cargo is

$$
\frac{C_{\mathrm{n}}}{C_{\mathrm{c}}} = \frac{1 + K_2G_{\mathrm{n}}}{1 + K_2G_{\mathrm{c}}} \le \frac{G_{\mathrm{n}}}{G_{\mathrm{c}}},
\tag{16.3}
$$
with equality approached when $K_2G_{\mathrm{c}} \gg 1$. Passive leakage ($k_{\mathrm{p}} > 0$) lowers the ratio further.

**Proof** At steady state the net flux of cargo through the pore vanishes. With $k_{\mathrm{p}} = 0$, cargo crosses only as $IC$, so $[IC]_{\mathrm{c}} = [IC]_{\mathrm{n}}$, that is $I_{\mathrm{c}}C_{\mathrm{c}} = I_{\mathrm{n}}C_{\mathrm{n}}$. The net flux of importin, carried by $I$, $IC$ and $IG$, also vanishes: $I_{\mathrm{c}} + [IC]_{\mathrm{c}} + [IG]_{\mathrm{c}} = I_{\mathrm{n}} + [IC]_{\mathrm{n}} + [IG]_{\mathrm{n}}$. Using $[IC]_{\mathrm{c}} = [IC]_{\mathrm{n}}$ and $[IG] = K_2IG$, this gives $I_{\mathrm{c}}(1 + K_2G_{\mathrm{c}}) = I_{\mathrm{n}}(1 + K_2G_{\mathrm{n}})$. Hence $C_{\mathrm{n}}/C_{\mathrm{c}} = I_{\mathrm{c}}/I_{\mathrm{n}} = (1 + K_2G_{\mathrm{n}})/(1 + K_2G_{\mathrm{c}})$. Since $G_{\mathrm{n}} > G_{\mathrm{c}}$, the function $x \mapsto (1 + K_2G_{\mathrm{n}}x)/(1 + K_2G_{\mathrm{c}}x)$ increases with $x$ towards $G_{\mathrm{n}}/G_{\mathrm{c}}$, which bounds it. A passive return flux $k_{\mathrm{p}}(C_{\mathrm{n}} - C_{\mathrm{c}}) > 0$ must be balanced by a net inward flux of $IC$, which requires $[IC]_{\mathrm{c}} > [IC]_{\mathrm{n}}$ and lowers the ratio. $\square$

The result has a thermodynamic reading. The free energy stored in the cargo gradient, $RT\ln(C_{\mathrm{n}}/C_{\mathrm{c}})$, cannot exceed that of the Ran-GTP gradient, $RT\ln(G_{\mathrm{n}}/G_{\mathrm{c}})$, because each cargo is carried in exchange for one Ran-GTP moved down its gradient. The Ran gradient is in turn maintained by GTP hydrolysis, whose free energy in the cell, about $-50\,\mathrm{kJ\,mol^{-1}}$, could in principle sustain a ratio of $\mathrm{e}^{50/2.6} \approx 10^8$; the actual limit is set by the much smaller Ran gradient, which depends on how completely RanGAP and RCC1 separate the two forms. A thousandfold Ran gradient corresponds to $RT\ln 1000 \approx 18\,\mathrm{kJ\,mol^{-1}}$ at $37\,^\circ\mathrm{C}$. This is a general design: a single gradient, made once by a dedicated enzyme pair, powers dozens of receptors, just as the $\ce{Na+}$ gradient made by the $\mathrm{Na^+/K^+}$ pump powers many symporters ([7.3.5](/7.3.5)).

![A model of Ran-driven import (Proposition 16.5.1; nuclear volume one fifth of the cytoplasmic volume; K₂G_n = 100, transport and binding in arbitrary units). A: time course of the ratio of free cargo concentrations, nucleus to cytoplasm, after the Ran gradient is switched on, for Ran-GTP gradients G_n/G_c of 10, 100 and 1000. B: steady-state accumulation ratio against the Ran gradient, without passive leakage (solid, the curve of Eq. (16.3)) and with passive leakage of the free cargo at two rates (dashed); the gray diagonal is the thermodynamic limit C_n/C_c = G_n/G_c. Dotted lines in A and the solid line in B are Eq. (16.3); points in B are steady states of the simulation](./plots/ran-accumulation.py)

### 16.5.4. Export of RNA

All RNAs that work in the cytoplasm are made in the nucleus and must be exported, each class by its own route and only after its processing is complete:

| RNA | Export receptor | Remarks |
|---|---|---|
| tRNA | exportin-t, with Ran-GTP | binds only mature tRNAs with correct 5′ and 3′ ends |
| pre-miRNA | exportin 5, with Ran-GTP | recognizes the 2-nt 3′ overhang left by Drosha ([7.2.18](/7.2.18)) |
| snRNA (U1, U2, U4, U5) | CRM1 with the adaptor PHAX and the cap-binding complex | assembled into snRNPs in the cytoplasm and reimported with snurportin and importin β |
| Pre-ribosomal subunits | CRM1 (via the adaptor NMD3 for the 60S subunit) and other receptors | the 5S rRNA travels as part of the pre-60S particle ([7.3.17](/7.3.17)) |
| mRNA | NXF1–NXT1 (TAP–p15; Mex67–Mtr2 in yeast) | Ran-independent; driven by an ATP-dependent helicase |

The export of mRNA is coupled to its synthesis and processing ([7.2.17](/7.2.17)). The TREX complex, recruited to the nascent transcript during capping, splicing (near the **exon junction complex**) and 3′-end formation, loads the export receptor NXF1–NXT1, a heterodimer that binds FG repeats but not Ran. The mRNA crosses the pore as a large ribonucleoprotein particle, 5′ end first; this was seen directly by electron microscopy of the giant Balbiani-ring mRNPs of insect salivary glands, which uncoil as they pass the pore ([7.3.17](/7.3.17)). On the cytoplasmic face, the DEAD-box helicase DDX19 (Dbp5), activated by Gle1 and inositol hexakisphosphate on the cytoplasmic filaments, uses ATP to strip NXF1 and other proteins from the mRNA, which can then no longer re-enter the pore; ATP hydrolysis makes the process unidirectional. Unspliced or incompletely processed transcripts are retained at the nuclear basket and degraded by the nuclear exosome, a quality control that keeps intron-containing RNAs, and many products of pervasive transcription, from reaching the ribosomes.

### 16.5.5. Transport Without Importins, and Regulated Access

Not all transport uses karyopherins. β-Catenin, the transcriptional coactivator of the Wnt pathway, has no classical NLS. In assays with isolated nuclei it bound the nuclear envelope and entered the nucleus without cytosol (the source of importins) and without Ran, but required ATP, and cytosol competed with this direct entry (Fagotto and colleagues, 1998). It crosses the pore by binding FG nucleoporins directly through its armadillo repeats, behaving as its own transport receptor; it can also leave the nucleus independently of CRM1. Several other signaling proteins, among them ERK2, Smad2 and Smad3, and unphosphorylated STAT1, can cross the pore in the same receptor-independent way, in addition to receptor-mediated routes.

Because transport is selective, a cell can regulate a protein by controlling its access to the transport machinery. For a protein that shuttles, with import and export rate constants $k_{\mathrm{in}}$ and $k_{\mathrm{out}}$ (per unit concentration), the steady state satisfies $k_{\mathrm{in}}C_{\mathrm{c}} = k_{\mathrm{out}}C_{\mathrm{n}}$, so its distribution is $C_{\mathrm{n}}/C_{\mathrm{c}} = k_{\mathrm{in}}/k_{\mathrm{out}}$; changing either rate moves the protein. The common mechanisms are:

| Mechanism | Example | Signal |
|---|---|---|
| Cytoplasmic retention by an inhibitor that masks the NLS | NF-κB, held by IκB ([7.3.19](/7.3.19)) | phosphorylation and degradation of IκB |
| Phosphorylation that unmasks or masks a signal | NFAT: dephosphorylation by the $\ce{Ca^2+}$-dependent phosphatase calcineurin exposes its NLS, rephosphorylation exposes its NES; yeast Pho4: phosphorylation by Pho80–Pho85 promotes export and blocks import | $\ce{Ca^2+}$; phosphate supply |
| Release from a chaperone or membrane anchor | glucocorticoid receptor, released from Hsp90 by hormone; SREBP, cleaved from the ER–Golgi membrane when sterols are low ([7.1.26](/7.1.26)) | ligand; sterols |
| Regulated export | p53 exported after ubiquitination by Mdm2 ([7.3.22](/7.3.22)); cyclin B1–Cdk1 accumulates in the nucleus at prophase when phosphorylation inhibits its export ([7.3.20](/7.3.20)) | DNA damage; mitotic entry |
| Changes in the pore | stretching of the nucleus by force on the cell dilates NPCs and increases import of the mechanosensitive coactivator YAP (Elosegui-Artola and colleagues, 2017) | substrate stiffness |

The NFAT case shows that nucleocytoplasmic transport can decode signals in time: NFAT accumulates in the nucleus only during sustained or frequent $\ce{Ca^2+}$ signals, because its export after each spike is slower than its import, so that the nuclear fraction integrates the signal ([7.3.18](/7.3.18)).

## 16.6. Breakdown and Reassembly of the Nuclear Envelope

### 16.6.1. Open and Closed Mitosis

**Definition 16.6.1 (Open and Closed Mitosis)** In **open mitosis** (animals, plants and many protists) the nuclear envelope breaks down at the end of prophase, so that spindle microtubules formed in the cytoplasm can capture the chromosomes, and it reassembles around each set of daughter chromosomes at telophase. In **closed mitosis** (budding and fission yeast, many other fungi and protists) the envelope stays intact, the spindle forms inside the nucleus from spindle pole bodies embedded in the envelope, and the nucleus divides by constriction. Intermediate, **semi-open** forms are common: in *Aspergillus nidulans* the NPCs partly disassemble so that the barrier opens without loss of the membranes, and in early *Drosophila* embryos the envelope is breached only near the spindle poles.

Closed mitosis requires the nucleus to elongate as the spindle lengthens, and thus extra envelope membrane; open mitosis gives the spindle access to the whole cytoplasm and its tubulin and motors. The diversity of solutions, even among closely related species (*Schizosaccharomyces japonicus*, unlike its relative *S. pombe*, breaks its envelope at anaphase), shows that the choice is not fixed by the rest of the cell's design.

### 16.6.2. Disassembly

Nuclear envelope breakdown is a regulated, stepwise process triggered at the onset of mitosis by the mitotic **cyclin-dependent kinase** Cdk1–cyclin B ([7.3.20](/7.3.20)) together with other kinases (PLK1, NIMA-related kinases, and protein kinase C for B-type lamins).

1. Permeabilization. Cdk1 and PLK1 phosphorylate nucleoporins, beginning with Nup98, and the NPCs disassemble into subcomplexes; the barrier is lost before the membranes are removed.
2. Lamina disassembly. Phosphorylation of lamins at sites flanking the rod domain (Ser22 and Ser392 in lamin A) depolymerizes the lamina; mutating these sites prevents disassembly. Lamin A and C disperse into the cytoplasm as soluble dimers, while farnesylated B-type lamins stay attached to membranes.
3. Release of the membranes. Phosphorylation of INM proteins (LBR, emerin, LAP2) breaks their links to chromatin; dynein, recruited to the ONM, pulls on the envelope along spindle microtubules and tears it near the poles. In mammalian cells the membranes and INM proteins are absorbed into the mitotic ER network, as seen by imaging GFP-tagged INM proteins (Ellenberg and colleagues, 1997), rather than dispersed as separate vesicles; vesiculation is seen in *Xenopus* egg extracts.
4. Chromosome condensation, which begins earlier in prophase, completes the release of chromatin.

RCC1 stays bound to the mitotic chromosomes, so they remain surrounded by a cloud of Ran-GTP, which releases spindle assembly factors from importins near chromatin and helps build the spindle around the chromosomes ([7.3.21](/7.3.21)). The same signal will later mark where the envelope must reassemble.

### 16.6.3. Reassembly and the Assembly of Nuclear Pores

At anaphase the destruction of cyclin B by the anaphase-promoting complex inactivates Cdk1, and phosphatases (PP1 and PP2A–B55) dephosphorylate the envelope proteins. Reassembly then follows the chromosomes:

1. The DNA cross-bridging protein BAF (barrier-to-autointegration factor) binds the separating chromosomes, gathers them into a single compact mass, and binds the LEM-domain proteins of ER membranes, which spread over the chromatin surface.
2. Postmitotic NPC assembly starts on chromatin: the Nup ELYS binds chromatin and recruits the Y complex, transmembrane Nups and membranes are added, and Ran-GTP near the chromosomes releases nucleoporins from importin β, which otherwise holds them inactive.
3. The remaining holes in the new envelope, many of them where spindle microtubules still pass, are sealed by ESCRT-III, recruited by its INM adaptor LEM2 and CHMP7, with the microtubule-severing enzyme spastin.
4. Once the envelope is sealed and pores are present, Ran-dependent import restores the nuclear proteome; imported lamins assemble the lamina, and the nucleus expands.

During interphase, as the nucleus grows, new NPCs are inserted into the intact envelope by a different route. Correlative light and electron microscopy of human cells showed that interphase pores form from the inside out: an evagination of the INM, seeded by nucleoporins such as Nup153 and POM121 on the nuclear side, grows and fuses with the ONM (Otsuka and colleagues, 2016). Postmitotic assembly takes minutes, interphase assembly about an hour. The number of pores is thus not fixed: it is set by the rates of these two assembly modes, which increase with the growth of the nuclear surface and with Cdk activity in interphase.

## 16.7. Nuclear Size and the Origin of the Nucleus

### 16.7.1. The Nuclear-to-Cytoplasmic Ratio

Nuclei come in a vast range of sizes, from about $1\,\mu\mathrm{m}$ in yeast to $400\,\mu\mathrm{m}$ in amphibian oocytes, but in growing cells of one type the ratio of nuclear to cell volume is remarkably constant. This was noted by Richard Hertwig in 1903 as the *Kernplasmarelation*.

**Definition 16.7.1 (Nuclear-to-Cytoplasmic Ratio)** The **nuclear-to-cytoplasmic ratio** (N/C ratio, karyoplasmic ratio) is the ratio of the volume of the nucleus to the volume of the cytoplasm (or of the whole cell, as specified). **Nuclear size scaling** is the proportionality of nuclear volume to cell volume as cells grow, or among cells of different sizes.

In fission yeast the nuclear volume is about $8\%$ of the cell volume over a 16-fold range of cell sizes, including mutants that divide at abnormal sizes (Neumann and Nurse, 2007); budding yeast behaves similarly. Strikingly, DNA content matters little: diploid and haploid cells of the same volume have similar nuclei. What, then, sets nuclear size? Two classes of mechanism are supported by experiments.

The first is the supply of nuclear structural proteins by import. In egg extracts of the two frogs *Xenopus laevis* and the smaller *Xenopus tropicalis*, sperm chromatin assembles nuclei whose size reflects the species of the extract, not of the chromatin. The difference was traced to two transport factors (Levy and Heald, 2010): *X. laevis* extract contains more importin α, which imports the lamin B3 needed for nuclear growth, and less NTF2, which in excess narrows the pores and reduces import of large cargoes. Adding importin α to *tropicalis* extract enlarged its nuclei, and adding NTF2 to *laevis* extract made them smaller. In the dividing *laevis* embryo, the amount of importin α available decreases (it is partly sequestered on membranes by palmitoylation), and nuclei shrink with the cells. Nuclear growth is limited by import capacity.

The second is osmotic balance, which explains why the ratio is constant.

**Proposition 16.7.1 (Osmotic Model of Nuclear Size)** Suppose that the nuclear envelope, which is permeable to water, ions and small metabolites, is not under tension (it has excess area, as its wrinkles show), so that the osmotic pressures of nucleus and cytoplasm are equal; and that the osmotic pressure in each compartment is due to $N_{\mathrm{n}}$ and $N_{\mathrm{c}}$ macromolecules (with their counterions) that cannot cross the pores, distributed in the volumes $V_{\mathrm{n}} - b_{\mathrm{n}}$ and $V_{\mathrm{c}} - b_{\mathrm{c}}$, where $b$ is the volume occupied by dry mass. Then

$$
V_{\mathrm{n}} = b_{\mathrm{n}} + \frac{N_{\mathrm{n}}}{N_{\mathrm{c}}}\,(V_{\mathrm{c}} - b_{\mathrm{c}}),
\tag{16.4}
$$
so that if a cell grows with constant composition, the nuclear volume is proportional to the cytoplasmic volume, with a slope set by the ratio of macromolecules confined to each compartment.

**Proof** In the dilute (van 't Hoff) limit the colloid osmotic pressures are $\Pi_{\mathrm{n}} = N_{\mathrm{n}}k_{\mathrm{B}}T/(V_{\mathrm{n}} - b_{\mathrm{n}})$ and $\Pi_{\mathrm{c}} = N_{\mathrm{c}}k_{\mathrm{B}}T/(V_{\mathrm{c}} - b_{\mathrm{c}})$; small solutes equilibrate across the pores and contribute equally to both. A tension-free envelope transmits no pressure difference, so $\Pi_{\mathrm{n}} = \Pi_{\mathrm{c}}$, which rearranges to (16.4). If $N_{\mathrm{n}}$, $N_{\mathrm{c}}$, $b_{\mathrm{n}}$ and $b_{\mathrm{c}}$ all grow in proportion to cell volume, $V_{\mathrm{n}}/V_{\mathrm{c}}$ is constant. $\square$

The model, developed for fission yeast by Lemière, Chang and colleagues (2022), predicts the results of perturbations: when nuclear export is blocked with leptomycin B, an inhibitor of CRM1, proteins accumulate in the nucleus, $N_{\mathrm{n}}/N_{\mathrm{c}}$ rises and the nucleus swells; hyperosmotic shock shrinks nucleus and cell in proportion. The counterions of the charged macromolecules, held by a **Donnan equilibrium**, contribute substantially to $N$, and the RNA of the nucleus and the dense proteome of the cytoplasm are the main osmotic agents of their compartments. The two classes of mechanism are complementary: transport sets how many macromolecules each compartment holds, and osmotic balance converts that number into a volume. The lamina, the supply of membrane from the ER and the state of chromatin then shape the nucleus within these limits; a round nucleus is simply the shape of a slack envelope inflated by its contents, and nuclei become irregular when the lamina is defective (16.3.3).

The N/C ratio is also a biological signal. In the early *Xenopus* embryo, cleavage divisions halve the cytoplasm at each cycle while the number of nuclei doubles, and the embryo switches from rapid synchronous cycles to slower cycles with zygotic transcription (the mid-blastula transition) when the ratio of DNA to cytoplasm reaches a threshold; embryos made partly haploid or polyspermic switch one cycle later or earlier (Newport and Kirschner, 1982), a titration of maternal factors by DNA ([7.5](/7.5)). In pathology, enlarged and irregular nuclei, a high N/C ratio, are among the oldest criteria used to recognize and grade cancer ([7.3.26](/7.3.26)).

![Two models of nuclear size (arbitrary units). A: the osmotic model (Proposition 16.7.1): nuclear volume against cell volume for a growing cell with constant composition (solid line, slope set by N_n/N_c; points, individual cells with 10% variation in composition), after blocking nuclear export so that more macromolecules are held in the nucleus (dashed), and after an increase in the cytoplasmic macromolecule content (dotted); dry-mass volumes are neglected, so the lines pass through the origin. B: import-limited nuclear growth in Xenopus egg extracts: the import flux of lamin is proportional to the number of pores, hence to nuclear surface, and rises with the concentration of importin α (Michaelis–Menten) and falls with the concentration of NTF2, so that the nuclear radius grows linearly and the cross-sectional area quadratically in time; nuclei in X. laevis extract (more importin α, less NTF2) grow faster than in X. tropicalis extract; adding importin α to tropicalis extract or NTF2 to laevis extract moves each towards the other](./plots/nuclear-size.py)

### 16.7.2. The Origin of the Nucleus

The **last eukaryotic common ancestor** already had a complete nucleus: its descendants in all eukaryotic supergroups share nuclear pore complexes with homologous scaffold Nups and FG repeats, the Ran system, karyopherins and, in most lineages, lamins (plants lack lamins but have analogous coiled-coil proteins, the CRWN proteins). The nucleus therefore arose in the transition from an archaeal ancestor (related to the Asgard archaea) to the first eukaryotes ([7.3.1](/7.3.1)), and no intermediate forms survive. The membranes of some planctomycete bacteria, once described as nucleus-like, turned out to be invaginations of the plasma membrane continuous with the periplasm.

Two kinds of argument constrain how it happened. The first is structural. The envelope is part of the ER, and its pores are built of coat-like proteins related to those of vesicles, so the nucleus most likely arose from the **endomembrane system** rather than by engulfment of one cell by another. In the classical outside-in scenario, invaginations of the plasma membrane of an ancestral cell enclosed its chromosome and fused into a double-membraned envelope, whose lumen is topologically equivalent to the outside of the cell. In the inside-out scenario (Baum and Baum, 2014), an archaeal cell extended protrusions, the spaces between the protrusions became the ER, and the original cell body became the nucleus; the protrusions, which surrounded the mitochondrial endosymbionts, became the cytoplasm. The second argument is functional. Group II **self-splicing introns** from the α-proteobacterial ancestor of **mitochondria** are thought to have invaded the host genome and evolved into spliceosomal introns ([7.2.16](/7.2.16)); because splicing is slow and translation fast, ribosomes would have translated unspliced transcripts into faulty proteins. Separating transcription and splicing from translation by a barrier with gates for finished mRNAs would have solved the problem (Martin and Koonin, 2006). On this view, the nucleus is the price of introns and the condition for the complex gene regulation that followed.

## Summary

| Topic | Key points |
|---|---|
| Components (16.1) | envelope, NPCs, lamina, chromatin, nucleolus and nuclear bodies, nucleoplasm; the nucleoplasm is continuous with the cytosol for small molecules |
| Envelope (16.2, Definitions 16.2.1–16.2.2) | INM and ONM joined at the pore membrane; ONM and perinuclear space continuous with ER; INM proteins reach the INM by diffusion and are retained by binding (enrichment $1 + B/K$, Example 16.2.1); LINC complexes (SUN–KASH) transmit force between cytoskeleton and lamina |
| Lamina (16.3, Definitions 16.3.1–16.3.3) | A-type (lamin A/C, *LMNA*) and B-type lamins, type V intermediate filaments; CaaX farnesylation, ZMPSTE24 cleavage of prelamin A; mechanics, anchoring of pores and chromatin; laminopathies; progerin in HGPS stays farnesylated, lonafarnib |
| Nuclear matrix (Definition 16.3.4) | an operational residue after extraction; no continuous network in situ; its functions explained by chromatin loops, condensates and RNA |
| NPC (16.4, Definitions 16.4.1–16.4.2) | ~30 Nups in eightfold symmetry, $\sim 110$–$125\,\mathrm{MDa}$, $3000$–$4000$ per mammalian nucleus; coat-like scaffold; FG-repeat barrier; passive permeability falls continuously with size (Ogston mesh, Proposition 16.4.1), no sharp $60\,\mathrm{kDa}$ cutoff |
| Signals and receptors (Definitions 16.5.1–16.5.2) | NLS (monopartite, bipartite, PY), NES (leucine-rich, CRM1); karyopherins (importins, exportins) of HEAT repeats; importin α adaptor with IBB autoinhibition |
| Ran (Definition 16.5.3, Proposition 16.5.1) | RCC1 on chromatin, RanGAP in cytoplasm: Ran-GTP nuclear; importins release cargo on Ran-GTP binding, exportins bind cargo with Ran-GTP; one GTP per cycle; accumulation ratio $\le G_{\mathrm{n}}/G_{\mathrm{c}}$; inverted gradient reverses transport |
| RNA export (16.5.4) | tRNA, pre-miRNA, snRNA, ribosomal subunits by exportins and Ran; mRNA by NXF1–NXT1, coupled to processing, made unidirectional by the ATPase DDX19 |
| Regulated access (16.5.5) | receptor-independent transport (β-catenin); masking and unmasking of signals (NF-κB, NFAT, Pho4, glucocorticoid receptor, SREBP, p53); force-dependent pore dilation (YAP); distribution $C_{\mathrm{n}}/C_{\mathrm{c}} = k_{\mathrm{in}}/k_{\mathrm{out}}$ |
| Mitosis (16.6, Definition 16.6.1) | open, closed and semi-open mitosis; Cdk1 and other kinases disassemble NPCs, lamina and INM–chromatin links, dynein tears the envelope; reassembly with BAF, ELYS-seeded NPCs, Ran-GTP, ESCRT-III sealing; interphase NPC assembly inside out |
| Size and origin (16.7, Definition 16.7.1, Proposition 16.7.1) | constant N/C ratio; import capacity (importin α, NTF2) and osmotic balance of confined macromolecules set nuclear volume; N/C ratio times the mid-blastula transition; nucleus present in LECA, derived from the endomembrane system, possibly selected to separate splicing from translation |

## Questions

1. Why can a protein of $20\,\mathrm{kDa}$ that has no nuclear localization signal still be found mainly in the nucleus, and how would you test which explanation applies?

   **Answer** Small proteins equilibrate passively through the pores within minutes, so without further interactions they would be distributed evenly (per accessible volume). Nuclear enrichment of such a protein requires either a binding partner that holds it in the nucleus (retention by chromatin, the nucleolus or a nuclear protein), or piggyback import as part of a complex with a protein that has an NLS, or a nonclassical signal recognized by another karyopherin. Tests: measure its mobility by FRAP or FLIP (bound proteins exchange slowly; **fluorescence loss in photobleaching** of the cytoplasm drains a freely diffusing nuclear pool through the pores); enlarge it by fusion to several GFPs (retention survives, passive entry slows down, so a retained protein is still nuclear only if it is imported); delete candidate binding domains; and deplete candidate receptors or partners.

2. In a permeabilized-cell assay, nuclei are incubated with a fluorescent NLS cargo, importin α, importin β, Ran-GDP, NTF2 and GTP. Predict the effect of each change: (a) replacing GTP by the nonhydrolyzable analogue GTPγS; (b) omitting NTF2; (c) adding an excess of importin β lacking its Ran-binding site; (d) adding Ran-GTP and RanGAP to the incubation medium while blocking RanGAP inside the nucleus.

   **Answer** (a) Ran-GTPγS cannot be hydrolyzed in the cytoplasm, so importin β–Ran complexes that return to the cytoplasm are not dissociated; free importin β is depleted and import stops after one round (the first cargoes may still enter). (b) Without NTF2, Ran-GDP that leaves the nucleus is not returned, nuclear Ran-GTP is depleted, cargo release in the nucleus fails and import stalls after a few cycles. (c) Mutant importin β binds importin α–cargo and enters the nucleus but cannot be loaded with Ran-GTP, so it does not release cargo; it competes with wild-type importin β and inhibits import, and cargo that enters remains bound to the receptor. (d) This inverts the gradient (high Ran-GTP outside, low inside): importins would bind cargo inside and release it outside, so cargo is exported, as Nachury and Weis (1999) observed. Directionality comes from where Ran-GTP is, not from the pore.

3. Using Proposition 16.5.1, estimate the maximal nuclear accumulation of an NLS protein if the Ran-GTP concentration is $5\,\mu\mathrm{M}$ in the nucleus and $10\,\mathrm{nM}$ in the cytoplasm, and $K_2 = 10^{8}\,\mathrm{M^{-1}}$ (dissociation constant $10\,\mathrm{nM}$). How much free energy does the cargo gradient store at $37\,^\circ\mathrm{C}$?

   **Answer** $K_2G_{\mathrm{n}} = 10^8 \times 5 \times 10^{-6} = 500$ and $K_2G_{\mathrm{c}} = 10^8 \times 10^{-8} = 1$. Then $C_{\mathrm{n}}/C_{\mathrm{c}} = 501/2 \approx 250$, half of the Ran gradient $G_{\mathrm{n}}/G_{\mathrm{c}} = 500$, because at this cytoplasmic Ran-GTP concentration half of the cytoplasmic importin is not occupied by Ran. The stored free energy is $RT\ln 250 = 8.314 \times 310 \times 5.52\,\mathrm{J\,mol^{-1}} \approx 14\,\mathrm{kJ\,mol^{-1}}$, much less than the free energy of GTP hydrolysis (about $50\,\mathrm{kJ\,mol^{-1}}$). Passive leakage of the cargo would lower the ratio further.

4. A child with HGPS carries one normal and one mutant *LMNA* allele. Explain why the disease is dominant, and why a farnesyltransferase inhibitor might help but could not be expected to cure it.

   **Answer** The mutant allele produces progerin, which cannot be cleaved by ZMPSTE24 and stays farnesylated and membrane-anchored; it incorporates into the lamina together with normal lamins and disrupts it (a dominant-negative, gain-of-function effect), so one normal allele does not prevent the phenotype. A farnesyltransferase inhibitor prevents farnesylation of progerin (and of prelamin A and other CaaX proteins), so progerin is less tightly bound to the membrane and nuclear blebbing is reduced. But progerin still lacks 50 residues and is still made; in the presence of the inhibitor some prelamin A is alternatively prenylated by geranylgeranyltransferase; and other farnesylated proteins are affected. Accordingly lonafarnib extends survival by a few years but does not stop the disease. Approaches that remove progerin itself (antisense oligonucleotides that block the cryptic splice site, base editing of the mutation in mice) address the cause.

5. Fission yeast cells grow from $60$ to $120\,\mu\mathrm{m}^3$ in one cycle, and their nuclei occupy $8\%$ of cell volume. (a) According to Proposition 16.7.1, what happens to nuclear volume if a drug blocks the export of a set of proteins and $N_{\mathrm{n}}/N_{\mathrm{c}}$ doubles? (b) Why does the model predict that the DNA content has only a small effect on nuclear volume?

   **Answer** (a) Neglecting the dry-mass volumes, $V_{\mathrm{n}}/V_{\mathrm{c}} = N_{\mathrm{n}}/N_{\mathrm{c}}$; initially $V_{\mathrm{n}}/V_{\mathrm{c}} = 0.08/0.92 \approx 0.087$. Doubling $N_{\mathrm{n}}/N_{\mathrm{c}}$ doubles this ratio to about $0.17$, so at a cell volume of $100\,\mu\mathrm{m}^3$ the nucleus grows from about $8$ to about $15\,\mu\mathrm{m}^3$ (the total volume being set by the cell's osmotic balance with the medium), as observed qualitatively when export is blocked with leptomycin B. (b) DNA contributes few osmotically active particles: the genome is a few chromosome-sized polymers, and its counterions are largely shared with the histones. The osmotic pressure of the nucleus is dominated by the much larger number of proteins and RNAs (and their counterions); doubling the DNA changes $N_{\mathrm{n}}$ little and changes $b_{\mathrm{n}}$ by the small dry volume of chromatin.

6. (Open question) The nuclear envelope breaks down in human cells but not in yeast. List the problems that each strategy must solve and the evidence that envelope breakdown is not simply a consequence of chromosome condensation.

   **Answer** Open mitosis must disassemble and rebuild pores, lamina and membranes every cycle, exclude cytoplasmic components (ribosomes) from the new nucleus and sort nuclear proteins back by import, and recapture all chromosomes in one envelope (micronuclei form when lagging chromosomes are enclosed separately, with DNA damage as a consequence). Closed mitosis must insert spindle pole bodies into the envelope, supply extra membrane as the nucleus elongates, and divide the envelope without mixing compartments. Breakdown is an active, kinase-driven process: it requires Cdk1 and PLK1 phosphorylation of Nups and lamins (nonphosphorylatable lamin mutants keep the lamina), it is assisted by dynein pulling on the envelope, and in the semi-open mitosis of *Aspergillus* or *S. japonicus* chromosomes condense without full breakdown; conversely, breakdown and permeabilization begin before condensation is complete.
