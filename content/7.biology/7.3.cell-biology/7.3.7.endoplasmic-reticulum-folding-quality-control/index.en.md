---
title: "The Endoplasmic Reticulum: Folding, Quality Control and Lipid Synthesis"
description: The endoplasmic reticulum as the cell's largest membrane system; rough and smooth ER and microsomes; N-linked glycosylation on a dolichol-linked precursor, disulfide formation and GPI anchors; the calnexin cycle, ER-associated degradation and diseases of quality control; the unfolded protein response (IRE1, PERK, ATF6) and a model of ER folding homeostasis; lipid synthesis, detoxification and the Ca²⁺ store of the smooth ER; the shaping of sheets and tubules by reticulons and atlastins, and ER contact sites.
---

The endoplasmic reticulum is the entry point of the secretory pathway and the largest membrane system of most eukaryotic cells. Almost every protein that will be secreted, inserted in the plasma membrane or delivered to the **Golgi apparatus**, **endosomes** or **lysosomes** enters it first ([7.3.6](/7.3.6) describes the targeting by the **signal sequence** and the **signal recognition particle**, [7.2.19](/7.2.19) the **SRP** cycle on the **ribosome**), and most membrane lipids are made in its membrane. The ER is therefore a factory that must keep three accounts in balance: it receives a flux of unfolded **polypeptides**, folds and modifies them, and releases only those that are correct; it makes lipids for itself and for other **organelles**; and it holds the cell's main reservoir of $\ce{Ca^2+}$. This chapter follows these tasks: the structure of the ER and the classical way of studying it (7.1), the modifications that new proteins receive in the lumen (7.2), how folded and misfolded proteins are told apart (7.3), how the ER measures its own load and adjusts its capacity, the unfolded protein response, with a small dynamical model (7.4), the functions of the smooth ER (7.5), and how the shape of the ER is built and connected to other organelles (7.6). Proteins that pass quality control leave in **COPII** vesicles, whose machinery is the subject of [7.3.8](/7.3.8); their glycans are completed in the Golgi apparatus ([7.3.9](/7.3.9)). The chemistry of glycans is in [7.1.10](/7.1.10), protein folding and **chaperones** in [7.1.6](/7.1.6), lipid biosynthesis in [7.1.26](/7.1.26).

## 7.1. Structure of the ER

### 7.1.1. Rough and Smooth ER

**Definition 7.1.1 (Endoplasmic Reticulum)** The **endoplasmic reticulum** (ER) is a continuous network of membrane tubules and flattened sacs (cisternae) that extends from the nuclear envelope through the cytoplasm. It encloses a single internal space, the ER lumen, which is continuous with the perinuclear space between the two nuclear membranes.

The ER was among the first structures revealed by electron microscopy of whole cells: Keith Porter, Albert Claude and Ernest Fullam (1945) saw a lacelike network in thin, spread cultured chick-embryo fibroblasts, and Porter named it the endoplasmic reticulum in the early 1950s because it was concentrated in the inner ("endoplasmic") region of the cytoplasm. The ER membrane is typically more than half of all membrane of an animal cell, and the lumen can take more than 10 % of the cell volume. Because the network reaches every region of the cytoplasm, almost no point of the cytosol is more than a micrometer away from ER membrane, and the ER is the natural hub for contacts with other organelles (7.6.2).

**Definition 7.1.2** The **rough endoplasmic reticulum** (rough ER) is the region of the ER whose cytosolic surface is studded with ribosomes synthesizing proteins that are translocated into or across its membrane; it is mostly organized as stacked sheets. The **smooth endoplasmic reticulum** (smooth ER) lacks bound ribosomes, is mostly tubular, and carries out lipid synthesis and metabolism, detoxification and $\ce{Ca^2+}$ storage. Small ribosome-free patches of the rough ER from which transport vesicles bud are called ER exit sites (transitional ER).

Ribosomes are not permanent parts of the rough ER. A ribosome is attached only while it translates an **mRNA** whose product has been targeted to the **Sec61 translocon**; after termination the subunits are released, and the same ribosome may next translate a cytosolic protein. A **polysome** on the rough ER is therefore a single mRNA held to the membrane by several nascent chains, each passing through its own translocon.

Which proteins are made on the rough ER follows from the sorting rules of [7.3.6](/7.3.6): secreted proteins (antibodies, **hormones**, digestive enzymes, matrix proteins); **integral membrane proteins** of the plasma membrane and of the ER, Golgi apparatus, endosomes and lysosomes; and soluble resident proteins of these compartments, including the lysosomal hydrolases, which must be kept apart from the cytosol. Proteins of the cytosol, nucleus, **mitochondria**, **plastids** and **peroxisomes** are completed on free ribosomes and, where they leave the cytosol, are imported posttranslationally. Many ER-made proteins are also glycosylated (7.2.1), but **glycosylation** is a consequence of entering the ER, not a reason for it.

The proportions of the two kinds of ER follow the specialization of the cell (MBoC 7e, Table 12–2):

| Cell type | Rough ER (% of membrane) | Smooth ER (% of membrane) | Dominant tasks |
|---|---|---|---|
| Pancreatic acinar cell | 60 | < 1 | secretes about its own mass of digestive enzymes per day |
| Hepatocyte | 35 | 16 | plasma proteins; **lipoproteins**, drug metabolism, glucose release |
| Plasma cell, pancreatic β cell | greatly expanded | little | antibodies; **insulin** |
| Leydig cell, adrenal cortex | little | abundant | **steroid hormones** |
| Skeletal and cardiac muscle | little | sarcoplasmic reticulum (Definition 7.5.1) | $\ce{Ca^2+}$ release and uptake |

Such numbers are a first example of how a cell sizes its organelles to the flux through them. Section 7.4 describes the feedback that does the sizing.

### 7.1.2. Microsomes

**Definition 7.1.3 (Microsome)** A **microsome** is a small closed vesicle, roughly 100–200 nm across, formed when cells are homogenized and pieces of ER (and of other membranes, mainly Golgi) break up and reseal. Rough microsomes carry ribosomes on their outer surface, which corresponds to the cytosolic face of the ER; smooth microsomes carry none.

Microsomes do not exist in living cells, but they keep the topology and much of the activity of the ER: their lumen corresponds to the ER lumen, and they continue to translocate, glycosylate and fold proteins. Because ribosomes contain much RNA and are dense, rough microsomes are denser than smooth ones and the two are separated by equilibrium centrifugation in a sucrose gradient (**cell fractionation**, [7.3.3](/7.3.3)). Rough microsomes were the key reagent of the **signal hypothesis**. Milstein and colleagues (1972) found that **immunoglobulin** light chains translated in a **cell-free system** without microsomes were longer than the secreted chains; Blobel and Dobberstein (1975) showed that adding rough microsomes during translation, but not after it, removed the extra N-terminal segment and made the chain resistant to added protease, that is, sequestered inside the microsomal lumen. The protease-protection assay is still the standard test of whether a protein has crossed a membrane ([7.3.6](/7.3.6)).

In fractionation the microsomal fraction is followed by **marker enzymes**: glucose 6-phosphatase (7.5.2), the classical marker of the ER since de Duve's work on liver, and **NADPH**–**cytochrome P-450** reductase; the ribophorins, subunits of oligosaccharyltransferase (Definition 7.2.2), are found only in rough microsomes. The ER membrane is relatively rich in protein (roughly 60–70 % of its mass) and its lipids are mostly phosphatidylcholine and phosphatidylethanolamine, with little **sphingomyelin** and **cholesterol** (7.5.1); it is thinner and more loosely packed than the plasma membrane, a difference that the Golgi apparatus bridges step by step ([7.3.9](/7.3.9)).

## 7.2. Modification of New Proteins in the Lumen

A polypeptide emerges into the ER lumen as an unfolded chain, much as a cytosolic protein emerges from the ribosome. The lumen differs from the cytosol in three ways that shape everything that follows: it is oxidizing, so cysteines can form **disulfide bonds**; it holds a high concentration of resident chaperones and folding enzymes, kept in the ER by a C-terminal KDEL retrieval signal ([7.3.8](/7.3.8)); and it has its own glycosylation machinery, which tags proteins with sugars that later report on their folding state.

### 7.2.1. N-Linked Glycosylation

About half of the proteins that pass through the ER are **glycoproteins**, and their most common modification is the attachment of an **N-linked glycan** to an asparagine in the sequon Asn–X–Ser/Thr (X ≠ Pro; the structure of glycans is in [7.1.10](/7.1.10)). Unlike the sugars of **glycogen** or **glycolipids**, this glycan is not built on the protein: a 14-sugar precursor is assembled on a lipid carrier and transferred as a unit.

**Definition 7.2.1** **Dolichol** is a long polyisoprenoid alcohol (17–21 isoprene units in animals) embedded in the ER membrane. Dolichol phosphate serves as the membrane anchor on which the N-glycan precursor, $\mathrm{Glc_3Man_9GlcNAc_2}$, is assembled; the oligosaccharide is linked to it through a pyrophosphate bridge.

**Definition 7.2.2** **Oligosaccharyltransferase** (OST) is the multisubunit membrane enzyme of the ER, with its active site in the lumen, that transfers the preassembled $\mathrm{Glc_3Man_9GlcNAc_2}$ en bloc from dolichol pyrophosphate to the side-chain amide nitrogen of asparagine in an Asn–X–Ser/Thr sequon of a translocating or newly translocated polypeptide.

The precursor is built in two halves on the two faces of the membrane:

1. On the cytosolic face, sugars are added from nucleotide sugars: GlcNAc-1-phosphate from UDP-GlcNAc (the step blocked by the antibiotic tunicamycin), a second GlcNAc, and five mannoses from GDP-Man, giving $\mathrm{Man_5GlcNAc_2}$-PP-dolichol.
2. This lipid-linked intermediate is flipped to the lumenal face, a slow step assisted by membrane proteins whose mechanism is still debated.
3. In the lumen, four more mannoses and three glucoses are added from dolichol-phosphate-mannose and dolichol-phosphate-glucose, which are themselves made on the cytosolic face and flipped.

![The N-glycan precursor and its trimming in the ER, in the Symbol Nomenclature for Glycans (blue circle glucose, green circle mannose, blue square N-acetylglucosamine; reducing end on the right). A: Glc3Man9GlcNAc2 on dolichol pyrophosphate; the three glucoses extend the lower (A) arm of the core, the upper α1-6 mannose carries the B and C arms. Glucosidase I removes the outermost glucose and glucosidase II the next two; ER mannosidase I removes the terminal mannose of the B arm, and the slower EDEM mannosidases remove terminal mannoses that mark a protein for degradation. B: the trimming intermediates in order and the lectins that read them: Glc1Man9 binds calnexin and calreticulin; Man9 is released (and re-glucosylated by UGGT if still unfolded); Man8B is the typical glycan of a protein ready to leave; Man7, with the α1-6 mannose of the C arm exposed, is recognized by the ERAD lectins OS-9 and XTP3-B.](./plots/n-glycan-precursor.py)

The OST of mammals has two catalytic isoforms: STT3A sits next to the Sec61 translocon and glycosylates sequons cotranslationally, as soon as they are about 12–14 **residues** into the lumen, before the chain folds and buries them; STT3B glycosylates sites that STT3A skipped, after translocation. Not every sequon is used: a sequon that folds too fast or lies too close to the C-terminus can escape. Defects in the assembly or transfer of the precursor cause the congenital disorders of glycosylation, multisystem diseases of which PMM2-CDG (phosphomannomutase 2, needed to make mannose 1-phosphate) is the most common.

Two features distinguish glycosylation from the synthesis of nucleic acids and proteins. There is no template: the structure of a glycan is set by the set of glycosyltransferases and glycosidases a protein meets and by how accessible its glycan is to them, so one protein exists as a population of glycoforms. And the same precursor is put on almost all N-glycoproteins, so that the ER can use the glycan as a uniform, protein-independent tag of folding state (7.3.1). N-glycosylation was long described as absent from prokaryotes; in fact many archaea and some bacteria (for example *Campylobacter jejuni*, whose PglB is homologous to STT3) N-glycosylate proteins, although with different glycans and on the outer face of the plasma membrane.

### 7.2.2. Disulfide Bonds

Disulfide bonds form almost exclusively in the ER lumen (and in the bacterial periplasm and the mitochondrial **intermembrane space**), because the cytosol is strongly reducing: the ratio of reduced to oxidized glutathione is above 30 : 1 in the cytosol but only about 1 : 1 to 3 : 1 in the ER. Oxidation of cysteine pairs is catalyzed by **protein disulfide isomerase** (PDI) and its family members (about 20 in mammals), thioredoxin-fold oxidoreductases with CXXC **active sites** whose chemistry is described in [7.1.6](/7.1.6). An oxidized PDI passes its disulfide to a client protein and becomes reduced; the **flavoprotein** Ero1 reoxidizes PDI with $\ce{O2}$ as the final electron acceptor, producing $\ce{H2O2}$, which peroxiredoxin 4 uses to form further disulfides. A protein with many cysteines often forms wrong pairs first, and the same enzymes, acting as reductases, shuffle them until the native set is reached. Each disulfide therefore costs the cell a molecule of $\ce{H2O2}$ that must be detoxified, a hidden cost of high secretory output.

The lumen also contains peptidyl-prolyl *cis–trans* isomerases and the chaperones described in 7.3.1, and it is where multisubunit proteins are assembled: an antibody is released only as a complete $\mathrm{H_2L_2}$ tetramer, and a free heavy chain stays bound to BiP. Reducing agents such as dithiothreitol added to cells prevent disulfide formation and cause misfolded proteins to accumulate, which makes them, with tunicamycin and the SERCA inhibitor thapsigargin (7.5.3), the standard experimental inducers of ER stress.

### 7.2.3. GPI Anchors

Some proteins are cleaved, immediately after translocation, from a C-terminal hydrophobic segment that held them in the membrane, and are attached instead to a preassembled glycosylphosphatidylinositol (GPI) lipid by a transamidase in the ER. The protein then hangs from the lumenal leaflet by two **fatty acid** chains, which end up in the outer leaflet of the plasma membrane. GPI-anchored proteins are concentrated in **lipid rafts**, are sorted to the apical surface of many epithelia ([7.3.9](/7.3.9)) and can be released from the cell surface by a phospholipase. The signal for GPI addition and its topology are described with the other membrane-protein topologies in [7.3.6](/7.3.6).

### 7.2.4. Other Modifications

Several further modifications are made during or soon after translocation:

| Modification | Enzyme and site | Example |
|---|---|---|
| Removal of the **signal peptide** | signal peptidase complex, lumenal active site, cotranslational | almost all secretory proteins; preproinsulin → proinsulin ([7.3.9](/7.3.9)) |
| Hydroxylation of Pro and Lys | prolyl 4-hydroxylase (whose β subunit is PDI) and lysyl hydroxylase, in the lumen; need $\ce{Fe^2+}$, $\ce{O2}$, α-ketoglutarate and ascorbate | **collagen**: hydroxyproline stabilizes the triple helix, hydroxylysine carries **O-linked** Gal–Glc; scurvy from **vitamin** C deficiency ([7.3.23](/7.3.23)) |
| γ-Carboxylation of Glu | vitamin K-dependent carboxylase of the ER membrane | clotting factors II, VII, IX and X; inhibited indirectly by warfarin |
| Fatty acylation | palmitoyl transferases (DHHC family) on the cytosolic face of the ER and Golgi | palmitoylated cysteines of membrane proteins such as SNAP-25 ([7.3.8](/7.3.8)) |
| Assembly of oligomers | chaperones and folding enzymes of 7.3.1 | antibodies, collagen trimers, MHC class I |

None of these needs a template, and like N-glycosylation they mark proteins as having passed through the lumen; several (hydroxylation of collagen, disulfide formation) are also conditions for the protein to fold and leave.

## 7.3. Quality Control

Many newly made proteins fail to fold: estimates range from a few percent to more than half for large multidomain or multisubunit proteins. In classical pulse–chase experiments, most newly made subunits of the T-cell receptor and of the muscle acetylcholine receptor never assembled and were degraded within the ER system without reaching the cell surface; the degradation is by ERAD and the proteasome (7.3.2), not by lysosomes, as was once assumed. The ER keeps such proteins from leaving, gives them repeated chances to fold, and eventually destroys those that do not. This system must solve a problem of measurement: a folding intermediate and a terminally misfolded protein look alike at any instant, and only the time spent in the ER distinguishes them.

### 7.3.1. BiP and the Lectin Chaperones

Two classes of **molecular chaperones** work in the lumen. BiP (binding immunoglobulin protein, GRP78) is the ER member of the Hsp70 family of **heat shock proteins**. Like its cytosolic relatives ([7.1.6](/7.1.6)) it binds exposed hydrophobic segments in its ADP state and releases them on nucleotide exchange and ATP binding, cycling with lumenal J-domain cofactors; it holds nascent chains, prevents their aggregation, helps pull chains into the ER during posttranslational translocation ([7.3.6](/7.3.6)), and retains unassembled subunits. Calnexin (a type I membrane protein) and calreticulin (its soluble paralog) are $\ce{Ca^2+}$-dependent **lectins** that bind one particular glycan, $\mathrm{Glc_1Man_9GlcNAc_2}$, and bring the PDI-family oxidoreductase ERp57 to their clients.

**Definition 7.3.1 (Calnexin Cycle)** The **calnexin cycle** (calnexin/calreticulin cycle) is the cycle of glucose removal and re-addition that controls the binding of N-glycoproteins to the lectin chaperones calnexin and calreticulin. Glucosidases I and II trim the precursor to $\mathrm{Glc_1Man_9GlcNAc_2}$, which binds the lectins; glucosidase II then removes the last glucose and releases the protein. A protein that is still incompletely folded is reglucosylated by UDP-glucose:glycoprotein glucosyltransferase (UGGT) and binds again; a folded protein is not, and is free to leave the ER.

UGGT is the folding sensor of the cycle: it is itself a large protein that recognizes exposed hydrophobic patches near the glycan and adds a glucose only to glycoproteins that are not yet native. It thereby translates a conformational property, which differs from protein to protein, into a chemical mark on a uniform glycan, which a single set of lectins can read. Folded glycoproteins with $\mathrm{Man_8}$–$\mathrm{Man_9}$ glycans are then picked up by cargo receptors such as the mannose-binding lectin ERGIC-53 and packaged into COPII vesicles ([7.3.8](/7.3.8)).

![Glycoprotein quality control in the ER. In the lumen (top), the new glycoprotein is trimmed by glucosidases I and II to the monoglucosylated form, which binds calnexin or calreticulin together with the oxidoreductase ERp57. Glucosidase II removes the last glucose and releases the protein: a folded protein leaves the ER with cargo receptors in COPII vesicles; an unfolded one is reglucosylated by UGGT, the folding sensor, and rebinds. Slow mannose trimming by ER mannosidase I and the EDEMs acts as a timer: proteins whose glycans are trimmed to Man7–5 are recognized by OS-9 or XTP3-B and delivered to the Hrd1–Sel1L complex. In the cytosol (bottom) the retrotranslocated chain is ubiquitinated, pulled out of the membrane by the ATPase p97 (Cdc48 in yeast), deglycosylated by N-glycanase and degraded by the proteasome.](./plots/calnexin-cycle.py)

The cycle can be thought of as a race between two clocks. If a protein folds with rate constant $k_{\mathrm{f}}$ and the mannose timer marks it for degradation with rate constant $k_{\mathrm{m}}$ (both first-order, while the protein cycles on calnexin), the probability that it leaves folded is $k_{\mathrm{f}}/(k_{\mathrm{f}} + k_{\mathrm{m}})$ and its mean residence time is $1/(k_{\mathrm{f}} + k_{\mathrm{m}})$: a race of two **exponential distributions**. A mutation that slows folding tenfold therefore does not merely delay secretion; if $k_{\mathrm{f}}$ drops below $k_{\mathrm{m}}$, most molecules are destroyed. This is exactly what happens to the commonest mutant of the CFTR chloride channel (7.3.3).

### 7.3.2. ER-Associated Degradation

**Definition 7.3.2** **ER-associated degradation** (ERAD) is the pathway by which misfolded or unassembled proteins of the ER lumen and membrane are recognized, moved back across the ER membrane into the cytosol, polyubiquitinated and degraded by the proteasome. The movement of a protein from the ER lumen or membrane into the cytosol is called **retrotranslocation** (dislocation).

ERAD has four steps, each with its own machinery:

1. Recognition. Lumenal misfolded glycoproteins are marked by mannose trimming: ER mannosidase I and the EDEM proteins slowly remove α1-2 mannoses, and the lectins OS-9 and XTP3-B bind glycans in which the α1-6 mannose of the C arm has been exposed (figure of 7.2.1). BiP and PDI-family reductases keep the substrate unfolded and break its disulfides so that it can be threaded through a narrow channel.
2. Retrotranslocation. The main mammalian channel is formed by the multispanning E3 ubiquitin ligase Hrd1 in a complex with Sel1L and the Derlin proteins (Hrd1 alone forms a channel in cryo-EM structures of the yeast complex). Misfolded membrane proteins and proteins with cytosolic lesions use related ligase complexes (in yeast, Hrd1 and Doa10 handle ERAD-L, ERAD-M and ERAD-C substrates).
3. Ubiquitination and extraction. The ligase attaches a polyubiquitin chain as the chain emerges into the cytosol, and the hexameric AAA ATPase p97 (VCP; Cdc48 in yeast) with its cofactors Ufd1 and Npl4 pulls the protein out using ATP hydrolysis.
4. Degradation. The cytosolic N-glycanase NGLY1 removes the glycan and the proteasome degrades the chain (the **ubiquitin–proteasome system**, [7.2.20](/7.2.20)).

ERAD also degrades correctly folded proteins on demand. HMG-CoA reductase, the rate-limiting enzyme of cholesterol synthesis, is ubiquitinated and degraded through Insig-dependent ERAD when sterols accumulate ([7.1.26](/7.1.26)); and the cytomegalovirus proteins US2 and US11 hijack the pathway to destroy newly made MHC class I molecules, hiding infected cells from cytotoxic T cells. Retrotranslocation is also the route by which some toxins (cholera toxin, ricin) reach the cytosol after travelling backwards through the secretory pathway.

### 7.3.3. Diseases of Quality Control

Quality control can fail in both directions: proteins that ought to be destroyed accumulate, or proteins that would work are destroyed.

| Disease | Protein and mutation | What goes wrong | Consequence |
|---|---|---|---|
| Cystic fibrosis | CFTR, deletion of Phe508 (ΔF508) in nucleotide-binding domain 1 | folding of the multidomain protein is slow; nearly all molecules are retained and degraded by ERAD (wild-type CFTR also matures inefficiently, roughly a third of molecules) | loss of the apical $\ce{Cl-}$ channel in lung, pancreas and gut; the mutant protein works partly if it reaches the surface |
| α1-antitrypsin deficiency | α1-antitrypsin, Glu342Lys (Z allele) | the serpin polymerizes in the ER of hepatocytes | liver damage from retained polymers (gain of toxic function); emphysema because too little inhibitor reaches the lung to restrain neutrophil elastase (loss of function) |
| Familial hypercholesterolemia, class 2 alleles | LDL receptor | the receptor is retained in the ER | fewer receptors on the cell surface ([7.3.10](/7.3.10)) |
| NGLY1 deficiency | N-glycanase | deglycosylation of ERAD substrates fails | neurodevelopmental disorder |

Cystic fibrosis illustrates both the race of 7.3.1 and the logic of therapy. ΔF508-CFTR reaches the surface when cells are grown at 27 °C, where folding is faster relative to the timer; small-molecule correctors (tezacaftor, elexacaftor) that bind and stabilize the mutant protein have the same effect, and combined with a potentiator (ivacaftor) that increases the open probability of the channels that reach the surface they restore enough function to change the course of the disease (approved in 2019). Cystic fibrosis is often presented as a defect of membrane trafficking; strictly the transport machinery is intact, and it is the quality control of the ER that holds the protein back.

## 7.4. The Unfolded Protein Response

The load on the ER varies over a wide range: a B cell that becomes a plasma cell increases antibody synthesis by orders of magnitude, and a pancreatic β cell raises proinsulin synthesis several-fold within an hour of a meal. Cells match folding capacity to this load by a signaling system that reports on the lumen and acts on the nucleus and on translation.

### 7.4.1. Three Sensors

**Definition 7.4.1 (Unfolded Protein Response)** The **unfolded protein response** (UPR) is the set of signaling pathways by which the accumulation of unfolded proteins in the ER lumen (ER stress) is sensed by the ER transmembrane proteins IRE1, PERK and ATF6 and transmitted to the cytosol and nucleus, where it reduces the entry of new proteins into the ER and increases the transcription of genes for ER chaperones, folding enzymes, ERAD components, lipid synthesis and the expansion of the ER.

How do the sensors read the lumen? In unstressed cells BiP binds the lumenal domains of all three and keeps them inactive; unfolded proteins compete for BiP and titrate it away. In addition, the lumenal domain of IRE1 binds unfolded polypeptides directly, which promotes its oligomerization. Both mechanisms make the sensors respond to the ratio of unfolded clients to free chaperone, which is the quantity the cell needs to control.

**Definition 7.4.2 (IRE1)** **IRE1** (inositol-requiring enzyme 1) is a type I ER transmembrane protein whose cytosolic part has a protein kinase domain and an endoribonuclease domain. In response to ER stress it oligomerizes and trans-autophosphorylates, which activates the ribonuclease; the ribonuclease excises a short intron from a specific cytosolic mRNA (*XBP1* in metazoans, *HAC1* in yeast), and the ligated mRNA encodes an active transcription factor.

IRE1 is the only branch present in all eukaryotes, and it was discovered in yeast. Cox, Shamu and Walter (1993) and Mori and colleagues (1993) independently identified Ire1 in screens for mutants unable to induce BiP (Kar2) under stress; Cox and Walter (1996) found that the target *HAC1* mRNA is spliced in the cytoplasm, removing a 252-nucleotide intron that blocks its translation, without the spliceosome, and the tRNA ligase joins the two exons. In mammals IRE1α cuts *XBP1* mRNA at two stem-loops, removing 26 nucleotides; the ligase RtcB rejoins the ends, the reading frame shifts, and the product XBP1s is a basic leucine zipper transcription factor that induces chaperones, ERAD components and lipid synthesis. Splicing in the cytosol is a fast switch: the unspliced mRNA is already present and bound to the ER membrane, and its conversion needs no new transcription. Strongly activated IRE1 also degrades other ER-associated mRNAs (regulated IRE1-dependent decay, RIDD), which further reduces the influx of new proteins. Kazutoshi Mori and Peter Walter received the 2014 Lasker Award for the discovery of the UPR.

**Definition 7.4.3 (PERK)** **PERK** (PKR-like ER kinase) is a type I ER transmembrane kinase that, activated by ER stress, phosphorylates the α subunit of translation initiation factor eIF2 at Ser51. This reduces translation initiation throughout the cell, and so the influx of new proteins into the ER, while it increases the translation of the transcription factor ATF4.

PERK is one of the four eIF2α kinases of the **integrated stress response** ([7.2.20](/7.2.20), where the mechanism by which phosphorylated eIF2 sequesters eIF2B and the uORF-based selective translation of *ATF4* are worked out). ATF4 induces genes for amino-acid import and synthesis and antioxidant defense, the proapoptotic transcription factor CHOP, and GADD34, the regulatory subunit that targets protein phosphatase 1 to eIF2α. GADD34 closes a negative feedback loop: translation resumes after a delay, whether or not the stress has been resolved.

**Definition 7.4.4 (ATF6)** **ATF6** is a type II ER transmembrane protein whose cytosolic N-terminal domain is a basic leucine zipper transcription factor. Under ER stress it is released from BiP, transported to the Golgi apparatus in COPII vesicles and cleaved there by site-1 and site-2 proteases; the released N-terminal fragment, ATF6(N), enters the nucleus and induces genes for ER chaperones (BiP, GRP94), *XBP1* and ERAD components.

The two-step cleavage of ATF6 by the Golgi proteases S1P and S2P is the same as that of the **SREBP** proteins that control cholesterol synthesis ([7.1.26](/7.1.26)): a transcription factor stored in the ER membrane is activated by changing compartment, so its activation depends on vesicle traffic. The three branches differ in speed and in what they change (figure): PERK acts within minutes and on translation; IRE1 within tens of minutes, through splicing; ATF6 needs transport and proteolysis. Their relative weights differ between cell types: IRE1–XBP1 is required for the expansion of the ER in plasma cells, and PERK is essential in β cells: loss of PERK causes Wolcott–Rallison syndrome, with diabetes in infancy as the β cells die.

![The three branches of the unfolded protein response (SBGN activity flow: open arrows activate, bars inhibit, dashed arrows act indirectly). In the ER lumen, unfolded proteins titrate BiP away from the three sensors and bind IRE1 directly. IRE1 splices XBP1 mRNA and degrades other mRNAs (RIDD); PERK phosphorylates eIF2α, which lowers global translation, and so the load on the ER, and raises translation of ATF4; ATF6 moves to the Golgi in COPII vesicles and is cleaved by S1P and S2P. In the nucleus XBP1s, ATF6(N) and ATF4 induce the adaptive program (chaperones, ERAD, lipid synthesis, expansion of the ER); ATF4 induces CHOP, which promotes apoptosis under prolonged stress, and GADD34, which with protein phosphatase 1 dephosphorylates eIF2α (negative feedback).](./plots/upr-branches.py)

### 7.4.2. Adaptation or Death

The UPR first tries to restore homeostasis. When it succeeds, the sensors return to their inactive state as free BiP recovers. When stress persists (an unfoldable mutant protein, a β cell under chronic high glucose demand), the same pathways switch the cell to apoptosis: CHOP induces proapoptotic Bcl-2 family members and Ero1α (whose $\ce{H2O2}$ adds oxidative stress); strongly oligomerized IRE1 activates the kinase JNK; and the balance of the branches changes with time, because IRE1 signaling declines during prolonged stress while PERK–CHOP signaling persists. In a multicellular organism, removing a cell that cannot fold its proteins is often less harmful than letting it secrete misfolded products. Chronic ER stress contributes to the loss of β cells in type 2 diabetes, to neurodegenerative diseases with ER protein aggregates, and to liver disease in α1-antitrypsin deficiency; conversely, cancer cells and highly secretory cells depend on the adaptive arms, which makes IRE1 and PERK drug targets.

### 7.4.3. A Model of ER Folding Homeostasis

The logic of adaptation and of its limit can be made explicit with a two-variable model. Let $U$ be the amount of unfolded protein in the lumen and $C$ the amount of free chaperone capacity (BiP and its partners), in arbitrary units, with time in hours. Unfolded clients enter at rate $s$ (the secretory load), are folded and exported at a rate proportional to the encounter of client and chaperone, and are degraded by ERAD at a first-order rate; the chaperone is made at a basal rate and, through the UPR, at a rate that increases with $U$ as a Hill function:

$$
\begin{aligned}
\frac{\mathrm{d}U}{\mathrm{d}t} &= s\,T(U) - k_{\mathrm{f}} C U - k_{\mathrm{d}} U,\\
\frac{\mathrm{d}C}{\mathrm{d}t} &= c_0 + \beta\,\frac{U^n}{K^n + U^n} - \gamma C.
\end{aligned}
\tag{7.1}
$$

| Symbol | Meaning | Value in the figure |
|---|---|---|
| $s$ | rate at which new client proteins enter the ER (translation of secretory proteins) | 1–60 |
| $k_{\mathrm{f}}$ | chaperone-assisted folding and export, per unit chaperone | 0.5 |
| $k_{\mathrm{d}}$ | ERAD rate constant | 0.05 |
| $c_0$ | basal chaperone synthesis | 1 |
| $\beta$, $K$, $n$ | maximal UPR-induced synthesis (IRE1–XBP1 and ATF6 transcription), half-saturating load, cooperativity | 8, 1, 2 |
| $\gamma$ | chaperone turnover (dilution and degradation), $\ln 2/\gamma \approx 1.4\,\mathrm{h}$ | 0.5 |
| $T(U)$ | PERK attenuation of translation: $T = 1/(1 + (U/K_{\mathrm{P}})^2)$ with PERK, $T = 1$ without | $K_{\mathrm{P}} = 3$ |

At steady state $U^* = s\,T(U^*)/(k_{\mathrm{f}}C^* + k_{\mathrm{d}})$. Without the UPR ($\beta = 0$) the chaperone is fixed at $c_0/\gamma$ and $U^*$ rises in proportion to the load. With the UPR the chaperone rises with $U$, so $U^*$ grows much more slowly than $s$: this is integral-like adaptation by a negative feedback loop, the same design that keeps **sterol regulatory element-binding protein** signaling matched to cholesterol. But the induced capacity saturates at $C_{\max} = (c_0 + \beta)/\gamma$; once the chaperone is maximal, $U^* \approx s/(k_{\mathrm{f}}C_{\max})$ rises in proportion to the load again, with a slope reduced by the factor $C_{\max}\gamma/c_0$. PERK flattens the curve further by throttling the input. If we take, as an assumption of the model, that persistent $U$ above a threshold commits the cell to apoptosis (7.4.2), the model reproduces the three regimes seen in cells: small loads are absorbed with little change; larger loads trigger a transient overshoot of $U$, followed by adaptation within a few chaperone lifetimes; loads beyond the induced capacity cannot be adapted to and lead to death. The time scale of the overshoot is set by $1/\gamma$, the time needed to make new chaperone, which is why the fast, translational PERK arm is valuable even though it does not add capacity.

![The ER folding homeostasis model, Eq. (7.1). A: unfolded protein U and chaperone C after the load is raised at t = 5 h from 1 to 5, 20 or 45 (with UPR and PERK): U overshoots and returns towards a new steady state within a few hours as the UPR induces chaperone; the largest step briefly crosses the assumed apoptosis threshold (dashed). B: steady-state U against load: without UPR U rises in proportion to the load and soon crosses the threshold; the transcriptional UPR (IRE1 and ATF6) keeps U low until the induced chaperone saturates, after which U rises linearly again; PERK attenuation of translation extends the range further.](./plots/upr-model.py)

The model omits much: chaperone sequestration by clients, the delay of transcription and translation, the separate roles of the branches, and the timer of ERAD. Its use is to make clear which parameters set the capacity of a secretory cell ($\beta/\gamma$, $k_{\mathrm{f}}$) and why the response has a limit, not to predict numbers.

## 7.5. The Smooth ER

### 7.5.1. Membrane Lipid Synthesis

Nearly all the phospholipids and cholesterol of the cell's membranes are made in the ER; the exceptions are some lipids of mitochondria and plastids (cardiolipin, made in the inner mitochondrial membrane) and sphingomyelin and glycosphingolipids, whose synthesis starts with ceramide in the ER and is completed in the Golgi apparatus ([7.3.9](/7.3.9)). The enzymes of phospholipid synthesis ([7.1.26](/7.1.26)) are integral ER membrane proteins whose active sites face the cytosol, where their water-soluble substrates (acyl-CoA, glycerol 3-phosphate, CDP-choline) are found. Two fatty acyl chains are joined to glycerol 3-phosphate to make phosphatidic acid, and head groups are added to give phosphatidylcholine, phosphatidylethanolamine and phosphatidylserine. All new lipid is therefore inserted into the cytosolic leaflet.

A bilayer that grew only on one side would bend and eventually tear. In the ER, **scramblases** move phospholipids between the leaflets in both directions without energy input and without strong head-group selectivity, so the two leaflets grow together; TMEM16K and the pair VMP1–TMEM41B have been identified as ER scramblases (scrambling is sometimes attributed to ABC transporters, but these are ATP-driven floppases, and the ER scramblases are distinct proteins). ER membranes are therefore nearly symmetric. Asymmetry is created later, in the Golgi and plasma membrane, by ATP-driven **flippases** that concentrate phosphatidylserine and phosphatidylethanolamine in the cytosolic leaflet ([7.3.4](/7.3.4)).

![Two functions of the ER membrane. A: phospholipid synthesis. Acyltransferases and the other enzymes of the pathway act at the cytosolic face, so new phospholipids (yellow heads) first appear in the cytosolic leaflet; an ER scramblase moves lipids between the leaflets in both directions without using energy, so the bilayer grows symmetrically. B: the ER as a calcium store. SERCA, a P-type ATPase with its A, P and N domains in the cytosol, pumps two Ca2+ ions into the lumen for each ATP hydrolyzed; low-affinity, high-capacity binding proteins (calreticulin; calsequestrin in the sarcoplasmic reticulum) buffer the lumenal calcium; IP3 receptors, opened by IP3 and Ca2+, and ryanodine receptors release it into the cytosol.](./plots/smooth-er.py)

The ER makes cholesterol but keeps very little of it: cholesterol is about 5 % of ER lipids but 30–40 % of those of the plasma membrane. Newly made lipids leave the ER by two routes. Vesicles carry them along the secretory pathway, but most lipid traffic is non-vesicular, through lipid-transfer proteins at membrane contact sites (7.6.2), and the low cholesterol of the ER is what allows its SCAP–SREBP sensor to detect small changes ([7.1.26](/7.1.26)). Neutral lipids (triacylglycerols, cholesterol esters) are made by ER enzymes and accumulate between the two leaflets until a lipid droplet buds into the cytosol, a process organized by the protein seipin.

### 7.5.2. Detoxification, Steroids and Glucose Release

The smooth ER of hepatocytes contains the **cytochrome P-450** monooxygenases and their reductase, which hydroxylate drugs, toxins and endogenous lipophilic compounds; the hydroxyl groups are then conjugated (glucuronidation by ER UDP-glucuronosyltransferases, sulfation) so that the products are water-soluble and excreted. Exposure to drugs such as phenobarbital induces these enzymes and expands the smooth ER of hepatocytes several-fold within days; the extra membrane is removed by autophagy ([7.3.11](/7.3.11)) when the drug is withdrawn. In steroid-secreting cells of the adrenal cortex, testis and ovary, the smooth ER and mitochondria carry the hydroxylases that convert **cholesterol** into steroid hormones.

The last step of gluconeogenesis and glycogen breakdown in liver and kidney is also an ER function. Glucose 6-phosphate is carried into the lumen by a transporter (SLC37A4) and hydrolyzed by glucose 6-phosphatase, whose active site faces the lumen; the free glucose returns to the cytosol and leaves the cell. Deficiency of the phosphatase or of the transporter causes von Gierke disease, the type I **glycogen storage disease**, with severe fasting hypoglycemia.

### 7.5.3. The Calcium Store

The ER lumen contains free $\ce{Ca^2+}$ at about 0.1–0.8 mM, against about 0.1 µM in the resting cytosol, and its total calcium is several times higher because of buffering proteins.

| Component | Function | Notes |
|---|---|---|
| SERCA (sarco/endoplasmic reticulum $\ce{Ca^2+}$-ATPase) | pumps $\ce{Ca^2+}$ into the lumen | a **P-type ATPase**: two $\ce{Ca^2+}$ per ATP, countertransport of $\ce{H+}$; inhibited by thapsigargin; in the heart regulated by phospholamban |
| IP₃ receptor | release channel opened by **inositol 1,4,5-trisphosphate** and cytosolic $\ce{Ca^2+}$ | tetramer; the main release route of non-excitable cells ([7.1.14](/7.1.14)) |
| Ryanodine receptor | release channel of muscle and neurons | the largest known ion channel (a tetramer of about 2.2 MDa) |
| Calreticulin, calsequestrin, BiP | lumenal buffers | low affinity, high capacity |
| STIM1 and Orai1 | store-operated $\ce{Ca^2+}$ entry | STIM1 senses lumenal $\ce{Ca^2+}$ with an EF hand; on depletion it moves to ER–plasma membrane contacts and opens Orai1 channels; loss of Orai1 causes severe combined immunodeficiency |

**Definition 7.5.1 (Sarcoplasmic Reticulum)** The **sarcoplasmic reticulum** is the specialized smooth ER of muscle cells, which surrounds each myofibril and stores and releases the $\ce{Ca^2+}$ that controls contraction. Its terminal cisternae lie next to the transverse tubules of the plasma membrane, where ryanodine receptors in the sarcoplasmic reticulum release $\ce{Ca^2+}$ in response to depolarization.

In skeletal muscle, voltage-sensing dihydropyridine receptors in the T tubule are mechanically coupled to ryanodine receptors (RyR1); in heart muscle, $\ce{Ca^2+}$ entering through these channels opens RyR2 ($\ce{Ca^2+}$-induced $\ce{Ca^2+}$ release). Relaxation is driven by SERCA, which in fast skeletal muscle is the most abundant membrane protein of the sarcoplasmic reticulum. Muscle contraction itself belongs to [7.3.13](/7.3.13) and animal physiology.

The calcium store couples the two halves of this chapter. Lumenal $\ce{Ca^2+}$ is needed by calnexin, calreticulin and other folding factors, so depleting the store with thapsigargin causes misfolding and triggers the UPR; conversely, sustained release of ER $\ce{Ca^2+}$ into mitochondria at contact sites is one of the routes to apoptosis under ER stress.

## 7.6. The Shape of the ER and Its Contacts

### 7.6.1. Sheets and Tubules

The ER is one continuous membrane with two main shapes. Sheets are pairs of flat membranes separated by a lumen of about 50 nm, the spacing maintained by the coiled-coil protein Climp-63; they carry most of the ribosomes and are concentrated near the nucleus, where in secretory cells they are stacked and connected by helicoidal ramps (Terasaki ramps). Tubules, 30–100 nm in diameter, form a polygonal network in the periphery; super-resolution imaging shows that some peripheral regions that look like sheets in conventional light microscopy are dense tubular matrices. The network is dynamic: tubules are pulled out along microtubules, by motors or by attachment to growing plus ends, and fuse with other tubules at three-way junctions.

**Definition 7.6.1 (Reticulon)** **Reticulons** are integral ER membrane proteins with two hydrophobic hairpin segments that occupy more space in the cytosolic leaflet than in the lumenal one; acting as wedges and oligomerizing into arcs, they induce and stabilize the high membrane curvature of ER tubules and of the edges of ER sheets. Together with the structurally similar REEP/DP1/Yop1 proteins they are necessary for the formation of ER tubules.

Voeltz, Rapoport and colleagues (2006) showed that yeast lacking reticulons and Yop1 lose their peripheral tubules, while purified reticulons in liposomes are sufficient to form tubules. The energy they must supply follows from membrane elasticity ([7.3.4](/7.3.4)): a cylinder of radius $r$ and length $L$ has bending energy $\frac{\kappa}{2}\left(\frac{1}{r}\right)^2 \cdot 2\pi r L = \pi\kappa L/r$, so with $\kappa \approx 20\,k_{\mathrm{B}}T$ and $r = 25\,\mathrm{nm}$ a tubule costs about $2.5\,k_{\mathrm{B}}T$ per nanometer, or $2500\,k_{\mathrm{B}}T$ per micrometer, which must be paid by the insertion of wedge-shaped proteins along its whole length. Sheets confine this cost to their edges, which is why reticulons are also found at sheet rims, and the ratio of reticulons to sheet-forming proteins such as Climp-63 sets the ratio of tubules to sheets.

The fusion of tubules is catalyzed by atlastins, dynamin-related GTPases of the ER membrane: atlastins on two membranes dimerize through their GTPase domains in the GTP-bound state, and the conformational change on hydrolysis pulls the membranes together and fuses them (in yeast the functional homolog is Sey1p, in plants RHD3). Without atlastin the network breaks into long unbranched tubules. Mutations in atlastin-1, the reticulon-like REEP1 and the microtubule-severing enzyme spastin together account for about half of the dominantly inherited hereditary spastic paraplegias, degenerations of the longest motor axons, which depend on a continuous ER over a meter of axon.

![The shape of the ER. A: top view of the ER in a spread animal cell: sheets with small fenestrations around the nucleus, continuous with the nuclear envelope, and a peripheral network of tubules joined at three-way junctions. B: a sheet in cross-section: two flat membranes held about 50 nm apart by lumenal spacers such as Climp-63, with highly curved rims stabilized by reticulons (wedges). C: a tubule in cross-section: reticulons and REEPs insert wedge-shaped hairpins into the cytosolic leaflet. D: atlastin dimerizes in trans between a tubule tip and another tubule and fuses them on GTP hydrolysis into a three-way junction.](./plots/er-shape.py)

The two shapes suit different tasks. Per unit of lumen volume, a tubule of radius $r$ has membrane area $2/r$ and a sheet of lumen thickness $d$ has area $2/d$; for $r = 25\,\mathrm{nm}$ and $d = 50\,\mathrm{nm}$ the tubule has twice the area per volume. Sheets provide flat membrane for polysomes and a large lumen for folding, and they expand in secretory cells; tubules provide much membrane for little volume, which suits lipid synthesis, detoxification and the many contacts with other organelles, and they dominate in hepatocytes and steroid-producing cells. ER exit sites, where COPII vesicles form, are marked by the scaffold Sec16 at a few hundred stable sites in a mammalian cell ([7.3.8](/7.3.8)).

### 7.6.2. Contacts with Other Organelles

At membrane contact sites the ER comes within 10–30 nm of another membrane without fusing with it ([7.3.6](/7.3.6)). These contacts are where most lipid exchange and much $\ce{Ca^2+}$ signaling take place:

- ER–plasma membrane: STIM1–Orai1 for store-operated $\ce{Ca^2+}$ entry; extended synaptotagmins transfer glycerolipids; the lipid-transfer protein OSBP and its relatives exchange sterol against phosphatidylinositol 4-phosphate (PI4P).
- ER–Golgi: CERT carries ceramide to the trans Golgi for sphingomyelin synthesis; OSBP moves cholesterol from the ER to the Golgi and returns PI4P, which the ER phosphatase Sac1 hydrolyzes, so that the PI4P gradient powers sterol transport against its concentration gradient.
- ER–mitochondria: phosphatidylserine is transferred and converted into phosphatidylethanolamine in mitochondria; IP₃ receptors pass $\ce{Ca^2+}$ to the mitochondrial uniporter; ER tubules mark the sites where mitochondria divide ([7.3.12](/7.3.12)), and in yeast the ERMES complex tethers the two organelles.
- ER–endosomes and lysosomes: contacts position endosomes, transfer cholesterol out of late endosomes, and mark sites of endosome fission ([7.3.10](/7.3.10)).

Bridge-like proteins of the VPS13 and ATG2 family form long hydrophobic grooves along which lipids slide between membranes in bulk; ATG2 supplies the lipid for the growth of autophagosomes ([7.3.11](/7.3.11)). Through these contacts the ER coordinates the lipid composition of the whole cell without moving most lipids through the secretory pathway at all.

## Summary

- The ER (Definition 7.1.1) is a single continuous membrane with one lumen. Rough ER (Definition 7.1.2) with bound ribosomes makes secretory and membrane proteins; smooth ER makes lipids, detoxifies, releases glucose and stores $\ce{Ca^2+}$; their proportions match the specialization of the cell. Microsomes (Definition 7.1.3) keep its topology and activities and made the signal hypothesis testable.
- Lumenal modifications: the N-glycan precursor $\mathrm{Glc_3Man_9GlcNAc_2}$ is built on dolichol (Definition 7.2.1) on both faces of the membrane and transferred en bloc by oligosaccharyltransferase (Definition 7.2.2) to Asn–X–Ser/Thr; PDI and Ero1 form and shuffle disulfides in the oxidizing lumen; GPI anchors replace C-terminal membrane anchors; signal peptide removal, prolyl and lysyl hydroxylation, γ-carboxylation and palmitoylation complete the set. Glucose 6-phosphatase marks the ER in fractionation, ribophorins the rough ER.
- Quality control: BiP binds hydrophobic segments; in the calnexin cycle (Definition 7.3.1) glucose trimming and UGGT reglucosylation translate folding state into a glycan mark; mannose trimming is the timer that sends terminally misfolded proteins to ERAD (Definition 7.3.2): recognition, retrotranslocation through Hrd1, ubiquitination, extraction by p97, proteasomal degradation. Folding success is a race, $k_{\mathrm{f}}/(k_{\mathrm{f}} + k_{\mathrm{m}})$; ΔF508-CFTR and α1-antitrypsin Z show the two failure modes.
- The UPR (Definition 7.4.1) senses the ratio of unfolded clients to free BiP:

  | Sensor | Output | Speed | Main effect |
  |---|---|---|---|
  | IRE1 (Definition 7.4.2) | cytosolic splicing of *XBP1* / *HAC1*; RIDD | minutes to tens of minutes | transcription of chaperones, ERAD, lipid synthesis |
  | PERK (Definition 7.4.3) | eIF2α phosphorylation; ATF4, CHOP, GADD34 | minutes | less translation; stress genes; apoptosis if prolonged |
  | ATF6 (Definition 7.4.4) | transport to the Golgi, S1P/S2P cleavage | tens of minutes | chaperones, *XBP1* |

- The model of Eq. (7.1) shows adaptation by negative feedback up to the induced capacity $C_{\max} = (c_0 + \beta)/\gamma$, after which unfolded protein rises with load and the cell dies.
- Smooth ER: lipids are made in the cytosolic leaflet and equilibrated by scramblases; cholesterol is made but not kept; cytochrome P-450 detoxification; glucose 6-phosphatase; the $\ce{Ca^2+}$ store with SERCA, IP₃ and ryanodine receptors and store-operated entry; the sarcoplasmic reticulum (Definition 7.5.1) of muscle.
- Shape: Climp-63 spaces sheets, reticulons (Definition 7.6.1) bend tubules (about $\pi\kappa/r$ per unit length), atlastins fuse them into three-way junctions; contact sites with the plasma membrane, Golgi, mitochondria and endosomes carry most lipid exchange.

## Questions

1. Cells are treated with tunicamycin. Which step is blocked, what happens to a secretory glycoprotein such as transferrin, and which signaling pathways are activated within an hour?

   **Answer** Tunicamycin inhibits GlcNAc-1-phosphate transferase, the first step of precursor assembly on dolichol phosphate, so no N-glycans are transferred. Glycoproteins are made without glycans; many cannot enter the calnexin cycle and fold poorly, are retained by BiP and are degraded by ERAD, so secretion of transferrin falls. The accumulation of unfolded proteins titrates BiP and activates all three UPR sensors: PERK (eIF2α phosphorylation within minutes, fall in global translation), IRE1 (*XBP1* splicing) and ATF6 (cleavage in the Golgi), leading to the induction of BiP and other ER chaperones.

2. Why is the glycan, rather than the polypeptide itself, used as the mark of folding state in the ER? What would be lost if every protein had its own sensor?

   **Answer** Nearly all N-glycoproteins receive the same precursor, so one set of enzymes (glucosidase II, UGGT, mannosidases) and lectins (calnexin, calreticulin, OS-9) can monitor thousands of different proteins. UGGT converts the protein-specific property "not yet folded" into a uniform chemical mark (a terminal glucose), and mannose trimming converts time spent in the ER into another uniform mark. A dedicated sensor for each client would be impossible to evolve for every new secreted protein; a generic glycan code makes quality control independent of the protein sequence, apart from the requirement for a sequon.

3. In the race of 7.3.1, wild-type CFTR has $k_{\mathrm{f}} \approx 0.5\,k_{\mathrm{m}}$ and ΔF508-CFTR $k_{\mathrm{f}} \approx 0.01\,k_{\mathrm{m}}$. What fractions mature? By how much must a corrector speed folding of the mutant to reach half of the wild-type amount at the surface?

   **Answer** Wild type: $0.5/(0.5 + 1) = 1/3$. ΔF508: $0.01/1.01 \approx 1\%$. Half of the wild-type value is $1/6$, so $k_{\mathrm{f}}/(k_{\mathrm{f}} + k_{\mathrm{m}}) = 1/6$ gives $k_{\mathrm{f}} = 0.2\,k_{\mathrm{m}}$, a twentyfold increase in the folding rate (or an equivalent combination of faster folding and a slower timer). Because the dependence is hyperbolic, moderate stabilization yields large gains when folding is far below the timer, which is why correctors combined with a potentiator are effective.

4. In the model of Eq. (7.1) without UPR and without PERK ($\beta = 0$, $T = 1$), find $U^*$ as a function of $s$. With the UPR at full induction, by what factor is $U^*$ reduced for large $s$, using the values in the table?

   **Answer** Without UPR, $C^* = c_0/\gamma = 2$ and $U^* = s/(k_{\mathrm{f}} c_0/\gamma + k_{\mathrm{d}}) = s/1.05$. At full induction $C^* = C_{\max} = (c_0 + \beta)/\gamma = 18$, so $U^* \approx s/(0.5 \cdot 18 + 0.05) = s/9.05$: about 8.6 times lower. The UPR shifts the load at which the apoptosis threshold is reached about ninefold but does not remove the threshold.

5. The IRE1 branch splices an mRNA in the cytosol rather than activating a transcription factor directly. What are the advantages of this design?

   **Answer** The unspliced *XBP1* (*HAC1*) mRNA is already present, and much of it is held at the ER membrane near IRE1, so active transcription factor can be made within minutes without new transcription; splicing is all-or-none for each molecule and is amplified by translation (each spliced mRNA gives many proteins); in yeast the intron also blocks translation of the unspliced mRNA, so leakiness is low. The ribonuclease can additionally degrade other ER-bound mRNAs (RIDD), reducing the load. The design couples a local membrane signal to a strong, fast transcriptional output.

6. Thapsigargin and dithiothreitol both cause ER stress. Explain why each does, and why the response to thapsigargin also involves the plasma membrane.

   **Answer** Dithiothreitol reduces disulfides and keeps the lumen from oxidizing them, so proteins that need disulfides cannot fold. Thapsigargin inhibits SERCA; $\ce{Ca^2+}$ leaks out of the ER and is not pumped back, and the $\ce{Ca^2+}$-dependent chaperones (calnexin, calreticulin) and other folding factors lose activity, so proteins misfold. Store depletion is sensed by STIM1, which moves to ER–plasma membrane junctions and opens Orai1 channels, so extracellular $\ce{Ca^2+}$ enters the cytosol (store-operated entry).

7. Hepatocytes of an animal given phenobarbital for a week have a much larger smooth ER. Why does the cell expand this compartment rather than raising enzyme concentration in the existing membrane, and what happens after the drug is withdrawn?

   **Answer** Cytochrome P-450 enzymes and their reductase are integral membrane proteins with lipophilic substrates that partition into the bilayer; their capacity is limited by membrane area, so the cell induces both the enzymes and lipid synthesis and expands the tubular smooth ER, which offers the most membrane area per volume. After withdrawal the extra membrane is no longer needed and is removed by selective autophagy of the ER (ER-phagy), and enzyme levels return to normal.
