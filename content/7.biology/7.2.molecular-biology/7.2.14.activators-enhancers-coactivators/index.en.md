---
title: Activators, Enhancers and Coactivators
description: The modular structure of eukaryotic activators (DNA-binding, activation and dimerization domains; acidic, glutamine-rich and proline-rich activation domains as intrinsically disordered regions); DNA-binding domains (zinc fingers, the GAL4 Zn2Cys6 cluster, nuclear-receptor zinc modules, homeodomains, bZIP and bHLH); dimerization and affinity; domain independence and the yeast two-hybrid assay; activation by recruitment and synergy; action at a distance (the catenane experiment, chromosome conformation capture, forced looping, the effective concentration of a looped enhancer); complex enhancers, architectural factors and the IFN-β enhanceosome; insulators and imprinting at H19/Igf2; Mediator, CBP/p300 and the p160 coactivators; regulation of activators by ligands, phosphorylation, ubiquitination, sumoylation and acetylation.
---

The **general transcription factors** of [7.2.13](/7.2.13) assemble at every **core promoter**, but on their own they give only a low, basal level of transcription. What turns a gene on in one cell type, at one stage of development or in response to one signal are the gene-specific **activators** that bind **enhancers** and proximal **promoter** elements ([7.2.12](/7.2.12)). This chapter asks how they work: how their DNA-binding **domains** read DNA sequence, why their domains can be exchanged between proteins, what they contact at the promoter, how they act from many kilobases away, how many of them cooperate on one enhancer, how insulators restrict their range, and how coactivators relay their signals. It closes with the regulation of the regulators, the point at which **signal transduction** ends. The bacterial counterparts, **activators** that recruit **RNA polymerase** by touching it, are in [7.2.11](/7.2.11); the chromatin-modifying coactivators are treated fully in [7.2.15](/7.2.15).

The human genome encodes about $1600$ sequence-specific DNA-binding transcription factors, about $8\%$ of its protein-coding genes. They are classified by their DNA-binding domains: about $750$ have $\mathrm{Cys_2His_2}$ zinc fingers, about $200$ homeodomains, about $110$ basic helix–loop–helix and about $55$ basic leucine-zipper domains, and $48$ are **nuclear receptors**.

## 14.1. The Modular Structure of Activators

Activators have at least two functional parts: a DNA-binding domain, which brings the protein to a specific sequence, and a transcription-activation domain, which does the activating. Many also have a dimerization domain, and some a ligand-binding or regulatory domain. Each part is a **domain** in the structural sense, an independently folded (or, for activation domains, independently functioning) region of the protein ([7.1.5](/7.1.5)).

**Definition 14.1.1** The part of a transcriptional activator that stimulates transcription by interacting with coactivators, the general transcription machinery or chromatin-modifying complexes, and that can do so when attached to a heterologous DNA-binding domain, is called an **activation domain** (transactivation domain).

Activation domains were classified by their amino acid composition:

| Class | Example | Composition |
|---|---|---|
| Acidic | yeast GAL4; herpesvirus VP16; yeast GCN4; p53 | the GAL4 activation domain has $11$ acidic **residues** among $49$ |
| Glutamine-rich | Sp1 | two domains of about $25\%$ glutamine ($39$ of $143$ residues in one) |
| Proline-rich | CTF/NF-I | $19$ prolines among $84$ residues |

Unlike DNA-binding domains, activation domains have no fixed structure. They are intrinsically disordered regions that fold, if at all, only when bound to a target, and they bind their targets through short hydrophobic **motifs** (tryptophan, phenylalanine, leucine) in "fuzzy" complexes with several alternative binding modes. High-throughput assays of thousands of random and mutated **peptides** (Staller, Cohen and colleagues, 2018–2022) showed that activity rises with both the number of aromatic and leucine residues and the number of acidic residues; the acidic residues keep the hydrophobic residues exposed and the domain disordered ("acidic exposure"). This explains why activation domains are hard to recognize by sequence alignment and why many unrelated sequences, even some from bacteria, activate transcription in yeast. Their disorder and multivalency also let activation domains form condensates with Mediator ([7.2.21](/7.2.21)).

## 14.2. DNA-Binding Domains

DNA-binding domains have well-defined structures, and X-ray and NMR structures of their complexes with DNA show how they read sequence. Almost all of them insert an α-helix, the recognition helix, into the **major groove**, where the edges of the **base pairs** present distinct patterns of hydrogen-bond donors, acceptors and methyl groups; **TBP** ([7.2.13](/7.2.13)) and HMG-box proteins, which bind the **minor groove** and bend the DNA, are the main exceptions. Most DNA-binding proteins bind as dimers or with several linked modules, for reasons explained in Section 14.2.5.

![A gallery of DNA-binding domains (schematic). A: three Cys₂His₂ zinc fingers of Zif268 following the major groove, each finger reading three base pairs with residues at positions −1, 3 and 6 of its helix. B: a homeodomain: three helices, helix 3 in the major groove and the N-terminal arm in the minor groove. C: a bZIP dimer (GCN4): a parallel coiled coil of leucine zippers whose basic regions grip the DNA like tongs. D: a bHLH dimer (MyoD, Max): two helices and a loop per monomer forming a four-helix bundle, basic regions in the major groove at an E box. E: the GAL4 dimer, with a Zn₂Cys₆ cluster in each recognition module and a coiled-coil dimerization helix. F: a nuclear receptor DNA-binding domain dimer, two Cys₄ zinc modules per monomer, on an inverted repeat](./plots/dna-binding-domains.py)

### 14.2.1. Zinc Fingers

**Definition 14.2.1** A DNA-binding module of about $30$ residues, consisting of a two-stranded antiparallel β-hairpin followed by an α-helix, in which a $\ce{Zn^2+}$ ion is coordinated by two cysteines of the hairpin and two histidines of the helix and the helix contacts about three base pairs in the major groove, is called a **zinc finger** ($\mathrm{Cys_2His_2}$ zinc finger).

Klug and colleagues (Miller, McLachlan and Klug, 1985) found that TFIIIA ([7.2.13](/7.2.13)) contains nine repeats of a $30$-residue sequence, each with two Cys and two His and enough zinc for one ion per repeat, and proposed that each repeat folds around its zinc into a finger-shaped domain. The NMR structure of a single finger of the *Xenopus* protein Xfin (1989) confirmed the fold. The finger shape itself confers no specificity: many proteins have identically shaped fingers that bind different sequences.

**Example 14.2.1 (Zif268)** The crystal structure of the three fingers of the mouse activator Zif268 (also called Egr1; it is not TFIIIA, as sometimes labeled) bound to its site $\mathrm{GCGTGGGCG}$ (Pavletich and Pabo, 1991) shows how fingers read DNA. The three fingers are arranged in a C-shape that follows the major groove, all approaching the DNA from the same angle. In each finger the β-hairpin contacts the backbone and positions the helix, and amino acids at positions $-1$, $3$ and $6$ of the helix (numbered from its start) contact three successive bases, mostly on one strand (the G-rich one): finger 1 reads $\mathrm{GCG}$, finger 2 $\mathrm{TGG}$, finger 3 $\mathrm{GCG}$. Most contacts are with bases rather than with the backbone, and the construction is modular: fingers can be shuffled and redesigned to read new triplets, the basis of engineered zinc-finger nucleases ([7.2.24](/7.2.24)).

Two other zinc-containing modules are unrelated in structure:

- *The GAL4 binuclear cluster.* GAL4, the yeast activator of the galactose genes, binds its upstream activating sequence ($\mathrm{UAS_G}$, a $17$ bp site $\mathrm{CGG{-}N_{11}{-}CCG}$) as a dimer. Its DNA-binding motif lies in residues $1$–$40$: six cysteines coordinate two zinc ions in a $\mathrm{Zn_2Cys_6}$ cluster that holds a short recognition helix in the major groove at the $\mathrm{CGG}$ triplet. Residues $50$–$94$ form an α-helix that pairs with the helix of the other monomer in a parallel **coiled coil**, and the linker between the two sets the $11$ bp spacing of the half-sites (Marmorstein, Harrison and colleagues, 1992).
- *Nuclear receptor zinc modules.* **Nuclear receptors** for steroid and thyroid **hormones**, retinoic acid and **vitamin** D have a DNA-binding domain of two modules, each with a zinc ion coordinated by four cysteines. The first module carries the recognition helix that reads a six-base-pair half-site, the second mediates dimerization on DNA. Type I **receptors** (glucocorticoid, estrogen, progesterone, androgen receptors) bind as homodimers to inverted repeats, such as the glucocorticoid response element $\mathrm{AGAACAnnnTGTTCT}$; type II receptors (thyroid hormone, retinoic acid and vitamin D receptors) bind as heterodimers with RXR to direct repeats of $\mathrm{AGGTCA}$, and the spacing of the repeats decides which receptor binds: $3$ bp for the vitamin D receptor, $4$ for the thyroid hormone receptor, $5$ for the retinoic acid receptor (the "3-4-5 rule", Umesono, Evans and colleagues, 1991).

The two types of receptors differ in how the hormone acts (the signaling chemistry is in [7.1.15](/7.1.15)).

**Example 14.2.2 (Two ways a hormone turns a receptor on)** The glucocorticoid receptor, without hormone, is held in the cytoplasm in a complex with the **chaperone** Hsp90. The steroid diffuses across the plasma membrane and binds the receptor, which changes conformation, releases Hsp90, enters the nucleus, dimerizes and binds glucocorticoid response elements (**hormone response elements**), acting as an activator. The thyroid hormone receptor, by contrast, stays in the nucleus bound to its response elements whether or not hormone is present. Without hormone it binds **corepressors** (NCoR, SMRT) and represses the gene; hormone binding repositions the C-terminal helix of the ligand-binding domain, releases the corepressor and creates a groove that binds coactivators (Section 14.8), so the same protein on the same DNA becomes an activator. Receptors whose **ligands** are unknown are called orphan receptors.

### 14.2.2. Homeodomains

**Definition 14.2.2** A DNA-binding domain of about $60$ residues, folded into three α-helices of which the second and third form a helix–turn–helix with helix 3 lying in the major groove and an N-terminal arm in the adjacent minor groove, is called a **homeodomain**. The $180$ bp DNA sequence that encodes it is the *homeobox*.

Homeoboxes were discovered (McGinnis, Scott, Gehring and colleagues, 1984) in the homeotic genes of *Drosophila*, whose mutations transform one body segment into another: dominant *Antennapedia* mutations, for example, make legs grow on the head in place of antennae. The homeodomain resembles the **helix–turn–helix** of bacterial **repressors** such as the λ repressor ([7.2.11](/7.2.11)) but has the extra N-terminal arm. Homeodomains typically recognize an AT-rich site with a $\mathrm{TAAT}$ core and, alone, bind with modest specificity; homeodomain proteins achieve their specificity in vivo by binding with partners (Hox proteins with Exd/Pbx), the start of the combinatorial logic of development ([7.5](/7.5)).

### 14.2.3. bZIP Domains

**Definition 14.2.3** An α-helical dimerization motif in which leucines occur at every seventh position, so that two such helices form a parallel coiled coil, is called a **leucine zipper**. A *bZIP* domain combines a leucine zipper with an N-terminal basic region that binds DNA.

In the crystal structure of the bZIP domain of yeast GCN4 (an activator of amino acid **biosynthesis** genes, itself regulated at the level of translation, [7.2.20](/7.2.20)) bound to DNA (Ellenberger, Harrison and colleagues, 1992), the two leucine-zipper helices form a **coiled coil**, and each helix continues uninterrupted into its basic region, which enters the major groove of one half-site. The dimer grips the DNA like a pair of tongs. Leucines at the $d$ positions of the heptad repeat $(abcdefg)_n$, and hydrophobic residues at $a$, form the core of the coiled coil ([7.1.5](/7.1.5)); charged residues at $e$ and $g$ determine which helices can pair. Fos cannot form homodimers but forms a heterodimer with Jun, and the Fos–Jun heterodimer (AP-1) binds the sequence $\mathrm{TGA(C/G)TCA}$; C/EBP is another bZIP family.

### 14.2.4. bHLH Domains

**Definition 14.2.4** A dimerization and DNA-binding domain in which each monomer contributes two amphipathic α-helices separated by a loop, the four helices of the dimer forming a bundle, and a basic region at the N-terminus of the first helix binds the major groove, is called a **basic helix–loop–helix** (bHLH) domain.

bHLH proteins bind the E box, $\mathrm{CANNTG}$. MyoD, which with its partner E47 drives muscle differentiation, is the classic example; its structure on DNA (Ma, Pabo and colleagues, 1994) resembles the bZIP tongs, with the basic regions as continuations of the first helices. The oncoprotein c-Myc and its partner Max have *bHLH-ZIP* domains, a bHLH followed by a leucine zipper that adds dimerization specificity. Myc does not bind DNA as a homodimer; Myc–Max heterodimers activate genes with $\mathrm{CACGTG}$ E boxes, while Mad–Max heterodimers bind the same sites and repress them by recruiting a **histone** deacetylase complex ([7.2.15](/7.2.15)). Id proteins, which have an HLH but no basic region, dimerize with bHLH partners and inactivate them.

| Family | Fold and recognition | Dimer | Examples |
|---|---|---|---|
| $\mathrm{Cys_2His_2}$ zinc finger | ββα finger, helix in major groove, $3$ bp per finger | no; tandem fingers | TFIIIA, Sp1, Zif268, CTCF, KRAB-zinc-finger proteins |
| $\mathrm{Zn_2Cys_6}$ cluster | short helix at $\mathrm{CGG}$ | coiled-coil homodimer | GAL4 and other fungal activators |
| Nuclear receptor | two $\mathrm{Cys_4}$ zinc modules | homo- or heterodimer | GR, ER (type I); TR, RAR, VDR with RXR (type II) |
| Homeodomain | three helices, helix 3 in major groove, arm in minor groove | often with partners | Antennapedia, Hox, Engrailed, Oct-1 (POU) |
| bZIP | basic region + leucine zipper | obligate dimer | GCN4, Fos–Jun (AP-1), CREB, C/EBP |
| bHLH (bHLH-ZIP) | basic region + four-helix bundle | obligate dimer | MyoD–E47, Myc–Max, Mad–Max |
| HMG box | L-shaped, minor groove, bends DNA | no | LEF-1/TCF, SRY, UBF |
| Others | winged helix, Rel homology, p53 core, T box | various | FOX, ETS, E2F, HSF; NF-κB, NFAT; p53 |

### 14.2.5. Dimerization and Affinity

Why are so many DNA-binding proteins dimers? A dimer contacts twice as much DNA as a monomer, and binding free energies add.

**Formula 14.2.1 (Affinity of a dimer)** Let a monomer bind a half-site with association constant $K_1 = \mathrm{e}^{-\Delta G_1/RT}/c^\circ$. If a dimer binds the two half-sites of a **palindrome**, the second half-site, once the first is bound, is present at a high effective concentration $c_{\mathrm{eff}}$ fixed by the geometry of the dimer, and
$$
K_2 = K_1^2\,c_{\mathrm{eff}}, \qquad \Delta G_2 = 2\,\Delta G_1 - RT\ln\frac{c_{\mathrm{eff}}}{c^\circ}. \tag{14.1}
$$
The binding free energy roughly doubles, so the association constant is roughly squared. A monomer with $K_1 = 10^6\,\mathrm{M^{-1}}$ ($K_D = 1\,\mu\mathrm{M}$) and a dimer with $c_{\mathrm{eff}} = 1\,\mathrm{mM}$ give $K_2 = 10^{12} \times 10^{-3} = 10^9\,\mathrm{M^{-1}}$, $K_D = 1\,\mathrm{nM}$.

The course slide states that "the affinity varies with the square of the free energy of binding"; the correct statement is the one above: affinity depends exponentially on the binding free energy, and dimerization approximately doubles the free energy, which squares the affinity. Specificity is squared too. If a monomer prefers its half-site over a random sequence by a factor $r$, a dimer prefers its full site by about $r^2$, which matters because a factor must find a few sites among about $10^9$ nonspecific positions in a mammalian genome (compare the **thermodynamic model** of [7.2.11](/7.2.11)). If the monomers bind separately and dimerize only on the DNA, the occupancy of the site depends on roughly the square of the monomer concentration: binding becomes cooperative, with a **Hill coefficient** approaching $2$ (figure, panel A). Heterodimers multiply the repertoire: $n$ monomers that pair freely could form $n(n + 1)/2$ different dimers with different sites and different activation domains, although the pairing rules of zippers and HLH bundles restrict this in practice.

![Binding energetics of activators (computed). A: occupancy of a palindromic site against protein concentration for a monomer (KD = 1 µM), a preformed dimer (Eq. (14.1), c_eff = 1 mM, KD = 1 nM) and monomers that dimerize only on DNA (cooperative, Hill coefficient near 2). B: synergy by recruitment, Eq. (14.2): activation against the number of bound activator sites for an interaction factor ω = 4 per activator at full and at half occupancy, compared with additive activation. C: cooperative assembly of a four-factor enhanceosome: probability that all four sites are filled against the concentration of each factor (in units of its dissociation constant) without and with cooperativity between neighbouring factors; the legend gives the Hill coefficient of the mean site occupancy](./plots/binding-energetics.py)

## 14.3. Independence of the Domains

**Example 14.3.1 (A chimeric activator)** Brent and Ptashne (1985) fused the DNA-binding domain of the bacterial repressor LexA, which has no activation domain and binds lexA **operators**, to the activation domain of GAL4. In yeast cells carrying a reporter gene with a lexA operator in place of the GAL4-binding site, the hybrid protein activated transcription; LexA alone did not, and GAL4 did not activate this reporter. The activation domain therefore works when brought to DNA by any DNA-binding domain, even a bacterial one, and the DNA-binding domain needs no particular partner. Domain-swap experiments with GCN4 and GAL4 (Hope and Struhl, 1986; Keegan, Gill and Ptashne, 1986) gave the same result.

The independence of the two domains became a tool.

The **yeast two-hybrid** assay, introduced as a tool for mapping signaling interactions in [7.1.15](/7.1.15), is a direct application: it detects the interaction of two proteins X and Y by fusing X to a DNA-binding domain (the "bait") and Y to an activation domain (the "prey"), so that a reporter gene with the corresponding **binding site** is transcribed only when X and Y bind each other and thereby bring the activation domain to the promoter.

Fields and Song (1989) tested the yeast proteins Snf1 and Snf4, known to interact, as fusions to the GAL4 DNA-binding domain and the GAL4 activation domain: the reporter ($\mathrm{GAL1}$–$lacZ$) was expressed only when both fusions were present. With a reporter that allows growth (*HIS3*) and a library of prey fusions, the assay screens a genome for the partners of a bait, and systematic screens of all pairs have mapped tens of thousands of binary interactions in yeast and human proteomes. Its limitations follow from its design: the interaction must occur in the nucleus, without the partners' normal modifications or compartments (membrane proteins need other versions, such as the split-ubiquitin assay); baits that activate on their own give false positives; and indirect interactions may be missed or mistaken. Variants detect DNA–protein (one-hybrid) and RNA–protein (three-hybrid) interactions, and the same modularity underlies the engineered transcription systems of genetics: GAL4–UAS expression in *Drosophila*, the tetracycline-controlled transactivator (TetR fused to VP16), and dCas9 fused to activation domains ([7.2.24](/7.2.24)).

![The modularity of activators. A: a chimera of the LexA DNA-binding domain and the GAL4 activation domain activates a reporter with a lexA operator, while the parental proteins do not (Example 14.3.1). B: the yeast two-hybrid assay: a bait fused to the GAL4 DNA-binding domain binds the UAS of a reporter; only when the prey, fused to an activation domain, binds the bait is the reporter (HIS3 or lacZ) transcribed](./plots/modularity.py)

## 14.4. Activation by Recruitment

### 14.4.1. Activators Contact the Transcription Machinery

In bacteria, the core polymerase cannot initiate at promoters, the holoenzyme gives basal transcription, and activators raise transcription at weak promoters by binding the polymerase and recruiting it ([7.2.11](/7.2.11)). Eukaryotic activators also recruit, but what they recruit is the preinitiation complex and the coactivators that help it form. Two models were proposed: activators stimulate the stepwise assembly of the PIC by contacting individual general factors (TFIID, TFIIB, TFIIA), or they recruit a preassembled holoenzyme containing Pol II, several general factors and Mediator ([7.2.13](/7.2.13)). Both mechanisms operate; in either, direct contacts between activators and the machinery are needed.

**Example 14.4.1 (VP16 binds TFIID)** Stringer, Ingles and Greenblatt (1990) fused the acidic activation domain of VP16 to protein A of *Staphylococcus aureus*, which binds IgG tightly, immobilized the fusion on an IgG column (**affinity chromatography**) and passed a HeLa nuclear extract through it. TFIID activity, measured by its ability to restore accurate run-off transcription to a TFIID-deficient system, was retained by the column and could be eluted; a mutant VP16 domain that cannot activate did not retain TFIID. Later work showed that VP16 contacts TBP, TAF9 and TFIIB, and the Med25 subunit of Mediator.

### 14.4.2. Recruitment Is Sufficient

If activation is recruitment, then any interaction that brings the machinery to a promoter should activate, whatever its chemical nature. This was tested by fusing a DNA-binding domain directly to a component of the machinery, with no activation domain at all. LexA fused to TBP activated transcription from a lexA operator in yeast (Chatterjee and Struhl, 1995; Klages and Strubin, 1995), and so did LexA fused to the Mediator subunit Gal11 (Barberis, Ptashne and colleagues, 1995); a point mutation in Gal11 that created an adventitious contact with the dimerization region of GAL4 turned that region into a potent activator. Ptashne and Gann summarized these results as "activation by recruitment": the activation domain is an adhesive surface whose only essential job is to raise the local concentration of the machinery at the promoter.

Recruitment explains why activators act synergistically: several activators bound near one promoter stimulate transcription much more than the sum of their separate effects (Carey, Ptashne and colleagues, 1990, with one to five GAL4 sites). In the thermodynamic picture of [7.2.11](/7.2.11), each bound activator that contacts the machinery adds its interaction free energy to that of the complex, so the factors multiply.

**Formula 14.4.1 (Synergy from recruitment)** Let a weak promoter have $n$ independent activator sites, each occupied with statistical weight $x = [\mathrm{A}]/K_D$, and let a bound activator stabilize the bound machinery by the factor $\omega = \mathrm{e}^{-\varepsilon/k_{\mathrm{B}}T}$ ($\varepsilon < 0$ the interaction energy). Summing the statistical weights of the activator sites with and without the machinery, the fold activation is
$$
F = \left(\frac{1 + \omega x}{1 + x}\right)^{n}, \tag{14.2}
$$
which tends to $\omega^n$ when all sites are occupied ($x \gg 1$). Two activators each worth $\omega = 4$ give $16$-fold, not $8$-fold, activation; four give $256$-fold. The multiplicative law holds as long as the promoter is weak; at strong promoters, activation saturates.

### 14.4.3. What Else Activators Recruit

Recruitment of the PIC is not the only target. Activators recruit histone acetyltransferases and chromatin-remodeling complexes, which make the promoter accessible ([7.2.15](/7.2.15)); P-TEFb, which releases paused polymerase ([7.2.13](/7.2.13)); and factors that increase the frequency of reinitiation from the scaffold left at the promoter after each round. Different activators emphasize different steps, which is one reason why two activators on one promoter can act synergistically even if each is weak.

## 14.5. Action at a Distance

### 14.5.1. Four Hypotheses and the Catenane Experiment

Enhancers stimulate promoters from kilobases away, in bacteria (the NtrC-dependent promoters) as well as eukaryotes. Four mechanisms were proposed (figure, panel A):

1. *Topology.* Binding of an activator changes the DNA structure (supercoiling, for example), and the change propagates along the DNA to the promoter.
2. *Sliding.* The activator binds the enhancer and then slides along the DNA to the promoter.
3. *Looping.* The activator stays at the enhancer and contacts the promoter-bound machinery by looping out the intervening DNA.
4. *Facilitated tracking.* The activator stays bound at the enhancer while another part of the complex tracks along the DNA, enlarging a loop until it reaches the promoter.

**Example 14.5.1 (Enhancer and promoter on separate rings)** Dunaway and Dröge (1989) placed the rRNA enhancer of *Xenopus laevis* and an rRNA minigene promoter on opposite sides of a plasmid that also contained the attachment sites attP and attB of phage λ. Recombination between the att sites by λ integrase in vitro ([7.2.9](/7.2.9)) split the plasmid into two interlocked rings, a catenane, with the enhancer on one ring and the promoter on the other. They injected the catenanes into frog oocyte nuclei together with a reference minigene (distinguishable by its length in **S1 mapping**) and measured transcription. The enhancer stimulated the promoter as well in the catenane as when both were on one circle, but not when the two rings were separate. The enhancer need not be on the same DNA molecule as the promoter, but it must be held close to it. Since there is no continuous DNA path from enhancer to promoter, topology changes, sliding and tracking are excluded, and protein–protein contact between the two sites, as in looping, is what matters.

![Action at a distance. A: the four hypotheses for how an enhancer-bound activator (orange) reaches the promoter (topology, sliding, looping, facilitated tracking). B: the catenane experiment: site-specific recombination between attP and attB divides a plasmid into two interlocked rings carrying the enhancer and the promoter (Example 14.5.1). C: the effective concentration of an enhancer at its promoter, Eq. (14.3), for naked DNA modeled as a Gaussian chain (Kuhn length 100 nm; dashed where DNA stiffness makes the model invalid) and, for comparison, a chromatin-like decay ∝ s⁻¹ as seen in Hi-C, with the range of transcription factor concentrations](./plots/action-at-distance.py)

### 14.5.2. Looping in Living Cells

Looping was demonstrated in cells by a method that converts spatial proximity into DNA sequence.

**Definition 14.5.1** A method that detects the spatial proximity of two genomic loci by cross-linking chromatin with formaldehyde, cutting it with a restriction enzyme, ligating the cut ends under dilute conditions that favor joining of cross-linked fragments, and detecting the junctions between the loci by PCR (or, genome-wide, by sequencing, as in Hi-C) is called **chromosome conformation capture** (3C).

Dekker and colleagues introduced 3C in 2002. Applied to the β-globin locus, it showed that the locus control region, an enhancer some $40$–$60$ kb upstream, contacts the promoter of the globin gene active at each developmental stage, forming an "active chromatin hub" in erythroid cells only (Tolhuis, de Laat and colleagues, 2002). Contact does not prove causation, but forced looping does: in erythroid cells lacking the activator GATA1, the loop and β-globin transcription are lost; tethering the looping protein Ldb1 to the β-globin promoter with an engineered zinc-finger protein restored both the contact with the locus control region and transcription (Deng, Blobel and colleagues, 2012). Genome-wide maps show that most enhancer–promoter contacts lie within one **topologically associating domain**, whose loops are made by cohesin-driven **loop extrusion** ([7.2.4](/7.2.4)). Live imaging has added a caution: at some loci enhancer and promoter do not come within a few tens of nanometres during transcription, which suggests that large protein assemblies (hubs or condensates, [7.2.21](/7.2.21)) can bridge distances of a few hundred nanometres.

### 14.5.3. How Effective Is a Loop?

A looped enhancer acts by raising the local concentration of its bound activator at the promoter. For a flexible polymer this concentration can be estimated.

**Formula 14.5.1 (Effective concentration of a looped site)** For a Gaussian chain of contour length $L$ and Kuhn length $b$ (twice the persistence length), the probability density that one end lies at the other end is $\left(3/(2\pi L b)\right)^{3/2}$, so the effective concentration of one site at the other is
$$
j = \frac{1}{N_{\mathrm{A}}}\left(\frac{3}{2\pi L b}\right)^{3/2}. \tag{14.3}
$$
For naked DNA ($b \approx 100\,\mathrm{nm}$, $0.34\,\mathrm{nm}$ per bp) and a separation of $3\,\mathrm{kb}$ ($L \approx 1\,\mu\mathrm{m}$), $3/(2\pi L b) \approx 4.7 \times 10^{-6}\,\mathrm{nm^{-2}}$, $j \approx 1.0 \times 10^{-8}\,\mathrm{nm^{-3}}$, or about $17\,\mathrm{nM}$ (since $1\,\mathrm{nm^{-3}}$ corresponds to $1.66\,\mathrm{M}$).

An enhancer $3\,\mathrm{kb}$ away is thus present at the promoter at a concentration comparable with that of a typical transcription factor in the nucleus ($1$–$100\,\mathrm{nM}$), and the loop is effective; at $30\,\mathrm{kb}$ the Gaussian estimate falls to about $0.5\,\mathrm{nM}$, and at $1\,\mathrm{Mb}$ to about $3 \times 10^{-3}\,\mathrm{nM}$, too little to explain enhancer action. Below a few hundred base pairs Eq. (14.3) fails in the other direction, because DNA is stiff and bending it into a small loop costs energy; enhancers very close to the promoter rely on DNA-bending architectural proteins instead (Section 14.6). The contact probability measured by Hi-C in chromatin decays more slowly with genomic distance $s$, roughly as $s^{-1}$ rather than $s^{-3/2}$, and is enhanced within TADs: chromatin compaction and loop extrusion keep distant elements of a domain close, which is what allows enhancers to work over hundreds of kilobases.

## 14.6. Complex Enhancers and Enhanceosomes

### 14.6.1. Combinatorial Control

Most genes are controlled by many activator-binding sites, often grouped into several enhancers, each of which must interact with the preinitiation complex. The control region of the human metallothionein IIA gene, which protects cells against heavy metals, has binding sites for the glucocorticoid receptor (a hormone response), for the metal-activated factor MTF-1 (several metal response elements), for AP-1 and Sp1 and others near the TATA box. Different combinations of active factors in different cells give different levels of expression: the gene responds to several stimuli because its control region integrates several inputs.

**Example 14.6.1 (The *Endo16* control region computes)** The *Endo16* gene of the sea urchin *Strongylocentrotus purpuratus* is expressed first in the vegetal plate and then in the midgut of the embryo. Its $2.3\,\mathrm{kb}$ control region contains more than $30$ binding sites for about a dozen factors, organized into six modules, G, F, E, DC, B and A, defined by restriction sites (Yuh, Bolouri and Davidson, 1998). Modules F, E and DC repress expression in ectoderm and skeletogenic mesoderm, confining it spatially; module B drives the late midgut expression; module A, next to the basal promoter, drives early expression and integrates the others: it passes the repressive inputs to the promoter and multiplies the output of module B. Measuring reporter output for constructs with different module combinations, the authors described module A by a set of logic and arithmetic rules (switches, AND/OR, multiplication by a constant) that predicted the output of new combinations. A cis-regulatory region is in this sense a small computing device whose inputs are the concentrations of its activators and repressors.

### 14.6.2. Architectural Factors

**Definition 14.6.1** A transcription factor whose main function is to change the shape of a DNA control region, typically by bending it, so that other proteins bound there can interact with each other and with the transcription machinery, is called an **architectural transcription factor**.

The enhancer of the human T-cell receptor α-chain gene contains three factor sites within $112$ bp upstream of the start site. One of them binds LEF-1, which cannot activate the gene by itself. LEF-1 binds the minor groove through its HMG box (high-mobility-group domain, named for small nuclear proteins of high electrophoretic mobility) and bends the DNA by about $130°$ (Giese, Grosschedl and colleagues), bringing the factors on either side into contact. LEF-1 acquires an activation function when it binds β-catenin, the transcriptional effector of Wnt signaling (Section 14.9).

### 14.6.3. The IFN-β Enhanceosome

**Definition 14.6.2** A nucleoprotein complex in which a defined set of activators binds cooperatively to an enhancer in a fixed arrangement and functions as a single unit to stimulate transcription is called an **enhanceosome**.

The archetype is the enhancer of the human interferon-β gene, which responds to virus infection (Thanos and Maniatis, 1995). Within about $55$ bp, from $-102$ to $-47$, it binds eight polypeptides: the heterodimer ATF-2–c-Jun, two copies each of the interferon regulatory factors IRF-3 and IRF-7, and the NF-κB heterodimer p50–RelA. Each factor is activated by a different signaling pathway triggered by the virus, and the enhancer works only when all are bound: it is an AND gate for virus infection. The architectural protein HMGA1 (HMG I(Y)), which binds the minor groove at several places in the enhancer, is required for the cooperative assembly. The original enhanceosome concept assumed that HMGA1 bends the DNA and remains part of the complex; the crystal structure of the assembled factors on the DNA (Panne, Maniatis and Harrison, 2007) showed instead an essentially straight DNA covered almost continuously by the factors, with few protein–protein contacts and no HMGA1. Cooperativity arises largely through the DNA itself, whose shape is adjusted by each bound factor to favor its neighbours, and HMGA1 acts as a transient chaperone of assembly. Once formed, the enhanceosome recruits coactivators and chromatin modifiers in a defined order ([7.2.15](/7.2.15)).

Cooperative assembly turns a set of graded inputs into an almost all-or-none output (figure above, panel C): if each neighbouring pair of factors stabilizes the other by a factor of $50$, the mean occupancy of the four sites of a model enhancer rises with a **Hill coefficient** of about $2.7$ instead of $1$, and the fully assembled state appears over a much narrower and lower range of factor concentrations than with independent binding. Few enhancers are as rigid as the IFN-β enhanceosome. Most developmental enhancers tolerate rearrangement of their sites, as if the factors acted independently on a "billboard"; these two models are ends of a continuum, and the degree of cooperativity of an enhancer can be measured by how sensitive its output is to changes in the spacing and order of its sites.

## 14.7. Insulators

**Definition 14.7.1** A DNA element that protects a gene from inappropriate regulatory influences of its genomic neighborhood, either by blocking the activation of a promoter by an enhancer when it lies between them (enhancer-blocking activity), or by stopping the spread of condensed, repressive chromatin into the gene (barrier activity), is called an **insulator**.

The two activities are separable. At the chicken β-globin locus, the hypersensitive site HS4 at the $5'$ boundary of the locus has both: its enhancer-blocking activity requires a binding site for the zinc-finger protein CTCF, and its barrier activity depends on other sites (bound by USF1 and VEZF1) that recruit histone-modifying enzymes and keep the adjacent nucleosomes acetylated (Felsenfeld and colleagues). In *Drosophila*, insulators were found flanking heat-shock genes (the scs and scs′ elements) and in the *gypsy* retrotransposon, whose insulator protein Su(Hw) blocks enhancers in genes where *gypsy* has inserted.

Two models were proposed for enhancer blocking. In a tracking model, an insulator blocks a signal that moves along the DNA from the enhancer. In a looping (domain) model, insulators bind proteins that interact with each other, so that a pair of insulators forms a loop that isolates the enhancer from promoters outside it. A telling observation favored looping: two copies of the *gypsy* insulator placed between an enhancer and a promoter do not block, but cancel each other (Cai and Shen, 2001; Muravyova, Georgiev and colleagues, 2001), presumably because they pair with each other and loop out the DNA between them, leaving enhancer and promoter in the same domain. A tracking signal would be blocked twice as well. The current view combines this with loop extrusion: vertebrate enhancer-blocking insulators are mostly CTCF sites, and they block when they stop cohesin and so form the boundaries of loops and TADs, in the orientation-dependent way described in [7.2.4](/7.2.4).

**Example 14.7.1 (An insulator controlled by DNA methylation)** The mouse *Igf2* and *H19* genes lie about $90$ kb apart and share enhancers downstream of *H19*. Between *Igf2* and *H19* lies an imprinting control region with several CTCF sites. On the maternal chromosome the region is unmethylated, CTCF binds and blocks the enhancers from *Igf2*, and the enhancers activate *H19*. On the paternal chromosome the region is methylated at CpG during spermatogenesis, CTCF cannot bind, the enhancers reach *Igf2*, and *H19* is silenced by the spreading methylation (Bell and Felsenfeld, 2000; Hark, Tilghman and colleagues, 2000). Each gene is thus expressed from one parental allele only, according to the methylation state of an insulator. DNA methylation is treated in [7.2.15](/7.2.15); defects of this control region cause human growth disorders (Beckwith–Wiedemann and Silver–Russell syndromes).

## 14.8. Coactivators

**Definition 14.8.1** A protein or protein complex that is recruited by DNA-bound activators, without binding DNA in a sequence-specific way itself, and that is required for their stimulation of transcription, either by contacting the general transcription machinery or by modifying or remodeling chromatin, is called a **coactivator**. Proteins with the converse role for repressors are corepressors.

### 14.8.1. Mediator

Overexpressing a strong activator inhibits transcription of genes driven by other activators, a phenomenon called squelching, as if the activators competed for a common limiting factor. Kelleher, Flanagan and Kornberg (1990) reproduced this interference in a yeast in vitro system: adding more GAL4-VP16 inhibited activation by another activator. The limiting factor was named mediator, since it appeared to mediate the effects of activators.

**Example 14.8.1 (Mediator in a G-less cassette assay)** To measure activated transcription in a yeast extract without background, Kornberg and colleagues used a template with GAL4 sites upstream of the *CYC1* core promoter and, downstream, a "G-less cassette", a stretch of a few hundred base pairs whose nontemplate strand contains no G. Transcription with ATP, CTP and UTP but no GTP yields a transcript that ends at the first G after the cassette; RNase T1, which cuts after G, removes any longer or nonspecific products. With purified general factors and Pol II, adding the mediator fraction greatly stimulated transcription in the presence of the activator GAL4-VP16 but had no effect on basal transcription without the activator (Kim, Björklund, Kornberg and colleagues, 1994). Mediator is thus a coactivator, not a general factor of basal transcription.

**Definition 14.8.2** The large multisubunit coactivator complex that binds activation domains through its tail module and RNA polymerase II through its head and middle modules, relays activator signals to the preinitiation complex and is required for transcription of nearly all Pol II genes is called **Mediator**.

Mediator has about $25$ subunits in yeast and $30$ in humans (about $1.4$ and $2\,\mathrm{MDa}$), named MED1 to MED31 in a unified nomenclature that replaced a dozen earlier names of human Mediator-like complexes (TRAP, DRIP, ARC, SMCC). Its tail subunits are the targets of activators: the acidic activation domain of GCN4 binds Med15 (Gal11), nuclear receptors bind MED1 through LXXLL motifs, and VP16 binds MED25. Its head and middle bind the polymerase and the unphosphorylated CTD, stabilize the PIC and stimulate the CTD kinase of TFIIH; Ser5 phosphorylation then helps release Pol II from Mediator into elongation. A dissociable kinase module (CDK8, cyclin C, MED12, MED13) can block Mediator's binding to Pol II and phosphorylates activators, often with repressive effects. Inactivating an essential Mediator subunit in yeast reduces transcription of nearly all genes (Holstege, Young and colleagues, 1998), and the discovery of Mediator was, with the structure of Pol II, part of the work recognized by the 2006 Nobel Prize in Chemistry to Roger Kornberg.

### 14.8.2. CBP/p300 and the p160 Coactivators

Cyclic AMP activates bacterial operons by binding CAP directly ([7.2.11](/7.2.11)); in eukaryotes it acts through a signal-transduction pathway.

**Example 14.8.2 (The CREB pathway)** Genes induced by cAMP have a cAMP response element (CRE, $\mathrm{TGACGTCA}$), bound by the bZIP protein CREB even before stimulation. When a hormone raises cAMP, the catalytic subunit of PKA, the cAMP-dependent **protein kinase**, enters the nucleus and phosphorylates CREB at Ser133. Phosphorylated CREB binds the KIX domain of CBP (CREB-binding protein, Chrivia, Goodman and colleagues, 1993), and CBP, which binds components of the basal machinery and is itself a histone acetyltransferase, recruits the machinery to the promoter and acetylates the surrounding chromatin. Unphosphorylated CREB is bound to the CRE but cannot activate.

CBP and its homolog p300 are coactivators for many activators besides CREB: nuclear receptors, AP-1, NF-κB, p53, STATs. For nuclear receptors, the link is a family of p160 steroid receptor coactivators (SRC-1, SRC-2, SRC-3), whose LXXLL motifs bind the groove created on the ligand-binding domain when hormone binds (Example 14.2.2); SRC in turn binds CBP/p300 and the arginine methyltransferase CARM1. Because CBP/p300 is present in limiting amounts and shared, activators compete for it, and one pathway can inhibit another. CARM1 makes this competition directional: it methylates an arginine in the KIX domain of CBP that is required for binding CREB, so that hormone-activated nuclear receptors, by recruiting CARM1, divert CBP away from CREB-dependent genes (Xu, Evans and colleagues, 2001).

## 14.9. Regulation of the Regulators

Responses to the environment usually require changes in gene expression, so signal-transduction pathways usually end with the activation or inactivation of transcription factors (the upstream chemistry is in [7.1.14](/7.1.14) and [7.1.15](/7.1.15)). The mechanisms fall into a few classes:

| Mechanism | Example | Effect |
|---|---|---|
| Ligand binding | glucocorticoid receptor; thyroid hormone receptor | nuclear entry and DNA binding; switch from repressor to activator (Example 14.2.2) |
| Phosphorylation | CREB (PKA, Ser133); STATs (JAK, tyrosine); SMADs (TGF-β receptor kinase); Elk-1 (MAP kinase) | coactivator binding; dimerization and nuclear entry; DNA binding |
| Release from an inhibitor | NF-κB, held in the cytoplasm by IκB | phosphorylation of IκB marks it for degradation; NF-κB enters the nucleus |
| Ubiquitination | polyubiquitination (Lys48 chains) of strong activators such as Myc, Gcn4; monoubiquitination | degradation by the proteasome; in some cases stimulation of activity |
| Sumoylation | LEF-1; Sp3; many others | relocation to nuclear bodies, recruitment of corepressors; usually repression |
| Acetylation, methylation | p53 (acetylated by p300 and PCAF); CBP (methylated by CARM1) | DNA binding, stability, partner choice |

**Ubiquitin** is a $76$-residue protein attached to lysines of target proteins by a cascade of activating (E1), conjugating (E2) and ligating (E3) enzymes; chains linked through Lys48 target proteins to the proteasome ([7.2.20](/7.2.20)). Several studies found that the sequences that make activation domains strong overlap with the signals that make them unstable, so that potent activators are rapidly destroyed. This lets a cell shut off strongly activated genes quickly, and it means that each activator molecule acts for a limited time. Monoubiquitination, by contrast, can stimulate some activators. SUMO, a ubiquitin-related protein of about $100$ residues attached by an analogous cascade, has quite different effects: sumoylated LEF-1, for example, is moved to nuclear bodies, where it is kept stable but inactive.

Two pathways show the general principle that a signal ends at a DNA-binding factor. In Wnt signaling, the activator β-catenin is continuously degraded in the absence of the signal; Wnt blocks its degradation, and β-catenin enters the nucleus and binds LEF-1/TCF, converting it from a repressor into an activator; sumoylation of LEF-1 blocks this. In the canonical TGF-β pathway (with its relatives activin, Nodal and BMP, which pattern the early embryo), receptor serine/threonine kinases phosphorylate receptor-regulated SMADs, which bind SMAD4, enter the nucleus and, with DNA-binding partners, activate target genes. Because each step of a kinase cascade can modify many molecules of the next, signals are amplified on their way to the nucleus.

## Summary

| Topic | Key facts |
|---|---|
| Modular activators | DNA-binding domain + activation domain (Definition 14.1.1) + often dimerization domain; acidic, Gln-rich, Pro-rich activation domains are intrinsically disordered, active through exposed hydrophobic residues |
| Zinc fingers (Definition 14.2.1) | TFIIIA (9 fingers), Zif268 (3 fingers, 3 bp each, helix positions −1, 3, 6; Example 14.2.1); GAL4 $\mathrm{Zn_2Cys_6}$; nuclear receptors with two $\mathrm{Cys_4}$ modules, 3-4-5 rule, type I (GR) and type II (TR) receptors (Example 14.2.2) |
| Homeodomain (Definition 14.2.2) | 60 residues, helix 3 in major groove, N-terminal arm in minor groove; homeotic genes |
| bZIP and bHLH (Definitions 14.2.3, 14.2.4) | leucine zipper coiled coil (GCN4, Fos–Jun); bHLH four-helix bundle on E boxes (MyoD, Myc–Max, Mad–Max) |
| Dimerization | $K_2 = K_1^2 c_{\mathrm{eff}}$, Eq. (14.1): free energy doubles, affinity and specificity are squared; dimerization on DNA gives cooperativity |
| Domain independence | LexA–GAL4 chimera (Example 14.3.1); yeast two-hybrid assay |
| Recruitment | VP16 binds TFIID (Example 14.4.1); fusions of DNA-binding domains to TBP or Gal11 activate; synergy $F = [(1 + \omega x)/(1 + x)]^n \to \omega^n$, Eq. (14.2) |
| Action at a distance | topology, sliding, looping, tracking; catenane experiment (Example 14.5.1); 3C (Definition 14.5.1), β-globin LCR, forced looping by Ldb1; effective concentration $j \propto (Lb)^{-3/2}$, Eq. (14.3): about $17\,\mathrm{nM}$ at $3\,\mathrm{kb}$ |
| Complex enhancers | metallothionein; *Endo16* modules as logic (Example 14.6.1); architectural factors such as LEF-1 (Definition 14.6.1); IFN-β enhanceosome (Definition 14.6.2), eight polypeptides on 55 bp of straight DNA |
| Insulators (Definition 14.7.1) | enhancer blocking (CTCF) and barrier activities; two insulators cancel (looping); *H19*/*Igf2* imprinting controlled by CTCF and methylation (Example 14.7.1) |
| Coactivators (Definition 14.8.1) | Mediator (Definition 14.8.2; squelching, G-less cassette, Example 14.8.1); CBP/p300 (CREB–KIX, Example 14.8.2); p160/SRC and CARM1 |
| Regulation of activators | ligands, phosphorylation, release from inhibitors, ubiquitination (Lys48, degradation), SUMO, acetylation; Wnt/β-catenin–LEF-1, TGF-β/SMAD |

## Questions

1. A protein binds a half-site with $K_D = 10\,\mu\mathrm{M}$ and prefers it over random DNA by a factor of $30$. Estimate the $K_D$ and the specificity ratio of a dimer that binds the full palindromic site with $c_{\mathrm{eff}} = 1\,\mathrm{mM}$. Why might the dimer still bind nonspecific DNA more often than its specific site in a mammalian nucleus?

   **Answer** $K_1 = 10^5\,\mathrm{M^{-1}}$, so $K_2 = K_1^2 c_{\mathrm{eff}} = 10^{10} \times 10^{-3} = 10^7\,\mathrm{M^{-1}}$, $K_D = 100\,\mathrm{nM}$. The specificity ratio is about $30^2 = 900$. A genome has about $10^9$ nonspecific positions; even if each is $900$ times weaker, their total weight, $10^9/900 \approx 10^6$, far exceeds that of one specific site, so most molecules are bound nonspecifically and the occupancy of the specific site depends on the number of protein molecules relative to the nonspecific competitor (the thermodynamic model of [7.2.11](/7.2.11)). Additional contacts (more modules, partners, nucleosome-mediated cooperativity) are needed for high occupancy of a unique site.
2. Design a two-hybrid experiment to test whether proteins X and Y interact, with the controls needed to interpret a positive result.

   **Answer** Express X fused to the GAL4 DNA-binding domain (bait) and Y fused to the GAL4 activation domain (prey) in a yeast strain with *HIS3* and *lacZ* reporters driven by GAL4 sites; select on medium lacking histidine and test for blue colonies on X-gal. Controls: bait alone with empty prey vector (to exclude self-activation by X), prey with an unrelated bait (to exclude a "sticky" prey), and a known interacting pair as a positive control. Confirmation by an independent method (coimmunoprecipitation or in vitro binding) is needed, and swapping X and Y between bait and prey tests the robustness of the interaction.
3. Using Eq. (14.2), compare the fold activation by three activator sites, each with $\omega = 3$, at an activator concentration equal to $K_D$ and at ten times $K_D$. What does the result say about the dose response of a gene with many weak sites?

   **Answer** At $x = 1$: $F = [(1 + 3)/2]^3 = 2^3 = 8$. At $x = 10$: $F = (31/11)^3 \approx 22$, approaching the maximum $\omega^3 = 27$. The response rises steeply with activator concentration because each additional occupied site multiplies the activation; with many sites the dose response is sigmoidal and switch-like, a source of sensitivity to small changes in activator levels.
4. In the catenane experiment, what result would have been expected if the enhancer acted by sliding of an activator along the DNA? What experiment would test facilitated tracking in a single DNA molecule?

   **Answer** A sliding activator cannot pass from one ring to the other, since the rings are interlocked but not covalently joined, so the catenane should have behaved like two separate plasmids: no stimulation. The observed stimulation excludes sliding. Facilitated tracking predicts that a protein obstacle bound tightly between enhancer and promoter (for example, a lac repressor bound to an operator, or a DNA–protein cross-link) should block the enhancer on a linear molecule, while it should have no effect if the enhancer acts by looping.
5. Using Eq. (14.3), at what separation along naked DNA does the effective concentration of an enhancer at its promoter fall to $1\,\mathrm{nM}$? Why do enhancers nonetheless work at $100\,\mathrm{kb}$?

   **Answer** $j \propto L^{-3/2}$ and $j = 17\,\mathrm{nM}$ at $3\,\mathrm{kb}$, so $j = 1\,\mathrm{nM}$ at $L = 3\,\mathrm{kb} \times 17^{2/3} \approx 3 \times 6.6 \approx 20\,\mathrm{kb}$. At $100\,\mathrm{kb}$ the Gaussian estimate is about $0.1\,\mathrm{nM}$. In chromatin, compaction makes the chain shorter and contact probabilities decay more slowly (about $s^{-1}$), loop extrusion actively brings elements of a TAD together, and multivalent protein assemblies at enhancers and promoters can capture each other at larger distances; together these raise the effective concentration far above the naked-DNA estimate.
6. A reporter gene is flanked on one side by an enhancer. A CTCF site placed between them blocks activation. Predict the effect of (a) a second CTCF site next to the first, in the same orientation; (b) a second CTCF site upstream of the enhancer, in the opposite orientation; (c) methylating the CpGs of the CTCF site.

   **Answer** (a) Two insulators between enhancer and promoter can cancel each other if they pair (as for *gypsy*); with CTCF sites, the outcome depends on orientation, and two sites in tandem usually block at least as well, because a loop-extruding cohesin is stopped at the first site it meets facing it. (b) A convergent pair of CTCF sites flanking the enhancer would create a loop containing the enhancer alone, isolating it from the promoter: blocking would be reinforced. (c) Methylation of CpGs in its site prevents CTCF binding, as at the paternal *H19*/*Igf2* imprinting control region, so blocking would be lost and the enhancer would activate the reporter.
7. Why is a mediator-dependent increase of activated but not basal transcription, as in Example 14.8.1, evidence that Mediator is a coactivator? What would one expect if Mediator were a general transcription factor?

   **Answer** A general transcription factor is required for initiation at every promoter whether or not an activator is present, so removing it would abolish basal transcription and adding it back would restore basal and activated transcription in proportion. Mediator had no effect on the basal level but greatly increased the activator-dependent level, so its function is to transmit the effect of the activator: the definition of a coactivator. (In vivo, Mediator is needed at nearly all genes because nearly all genes depend on activators.)
