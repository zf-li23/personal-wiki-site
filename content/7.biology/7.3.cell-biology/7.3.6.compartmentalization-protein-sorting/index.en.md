---
title: Compartmentalization and Protein Sorting
description: The compartments of a eukaryotic cell (volumes and membrane areas, the cytosol, the endomembrane system and its topology, membraneless compartments); how organelle size scales with cell size (the limiting-pool model); the three modes of protein sorting and the sorting signals; translocation into the ER (signal hypothesis, Sec61, co- and posttranslational import, start- and stop-transfer sequences, membrane protein topology, tail-anchored proteins and GET, GPI anchors); import into mitochondria (TOM, TIM23, TIM22, SAM, MIA, Oxa1; membrane potential and the import motor; the translocation ratchet) and chloroplasts (TOC, TIC, four thylakoid pathways); peroxisomes (functions, PTS1 and PTS2, peroxins, biogenesis, Zellweger syndrome); unconventional secretion and lipid transport at membrane contact sites.
---

A bacterium is, to a first approximation, one compartment: a cytoplasm bounded by a plasma membrane. A eukaryotic cell is a city of compartments, each with its own membrane, its own set of proteins and lipids, and its own chemistry, from the oxidizing, calcium-rich lumen of the **endoplasmic reticulum** to the acid interior of the **lysosome**. The previous two chapters described the membranes that make such compartments possible ([7.3.4](/7.3.4)) and the transport that keeps their contents different ([7.3.5](/7.3.5)). This chapter asks how a cell organizes itself into compartments and keeps each one supplied with the right proteins, a problem of logistics on a large scale: a human cell makes some $10^4$ different proteins, almost all of them on cytosolic **ribosomes**, and must deliver each to one of a dozen destinations. We first survey the compartments (6.1) and how their sizes are matched to the size of the cell (6.2). The rest of the chapter follows proteins to their destinations: the three modes of transport and the signals that direct them (6.3), translocation into the ER (6.4), import into **mitochondria** (6.5), **chloroplasts** (6.6) and peroxisomes (6.7), and finally the exceptions, proteins secreted without passing the ER and lipids that move without vesicles (6.8). The targeting of **ribosomes** to the ER by the **signal recognition particle** is treated in [7.2.19](/7.2.19#sec-19.9.2) and is only summarized here; import into the nucleus is the subject of [7.3.16](/7.3.16), and the further sorting of proteins by vesicles from the ER onward fills [7.3.7](/7.3.7)–[7.3.11](/7.3.11). The **organelle** biology of mitochondria and chloroplasts (dynamics, genomes, origin) follows in [7.3.12](/7.3.12).

## 6.1. The Compartments of a Eukaryotic Cell

### 6.1.1. Membrane-Enclosed Organelles

**Definition 6.1.1 (Membrane-Enclosed Organelle)** A **membrane-enclosed organelle** is a compartment of a eukaryotic cell bounded by one or two lipid bilayers, with a characteristic composition of proteins and lipids in its membrane and its lumen, which carries out a defined set of functions. The division of the cell into such compartments, each separated from the cytosol by a selectively permeable membrane, is **compartmentalization**.

Compartmentalization does three things that a single compartment cannot. It keeps incompatible reactions apart (**fatty acid** synthesis in the cytosol, their oxidation in mitochondria; proteins folded in the cytosol, others digested in lysosomes). It provides environments that differ from the cytosol (low pH, oxidizing conditions, high $\ce{Ca^2+}$) and concentrates enzymes and **substrates** in small volumes. And it multiplies the membrane area available for membrane-bound processes such as **oxidative phosphorylation** and lipid synthesis.

| Compartment | Share of cell volume in a hepatocyte | Main functions |
|---|---|---|
| Cytosol | $54\,\%$ | protein synthesis and degradation, most intermediary metabolism |
| Mitochondria | $22\,\%$ | oxidative phosphorylation, **citric acid cycle**, **β oxidation**, Fe–S clusters, **apoptosis** signals |
| **Rough ER** | $9\,\%$ | synthesis of secretory and membrane proteins |
| **Smooth ER** | $5\,\%$ | lipid synthesis, detoxification, $\ce{Ca^2+}$ store |
| **Golgi apparatus** | $1\,\%$ | **glycosylation**, sorting of proteins and lipids |
| Nucleus | $6\,\%$ | genome, DNA and RNA synthesis, ribosome assembly |
| Peroxisomes | $1\,\%$ | oxidations producing $\ce{H2O2}$, very-long-chain fatty acid oxidation, ether lipids |
| Lysosomes | $1\,\%$ | degradation |
| **Endosomes** | $1\,\%$ | sorting of endocytosed material |

(MBoC 7e, Table 12–1.) Membranes enclose nearly half the volume of a hepatocyte, and the plasma membrane is a minor part of the cell's membrane: in a hepatocyte of about $5000\,\mu\mathrm{m^3}$, with some $110\,000\,\mu\mathrm{m^2}$ of membrane, the plasma membrane accounts for $2\,\%$, the rough and smooth ER for about half and the mitochondrial inner membrane for a third; in a pancreatic acinar cell, specialized for secretion, the rough ER alone makes up $60\,\%$ of the membrane. The relative sizes of the compartments thus reflect what a cell does.

Organelles can also be grouped by their boundaries, which reflects their origins:

| Boundary | Organelles | Note |
|---|---|---|
| Two membranes | Nucleus (the **nuclear envelope**), mitochondria, **plastids** | The nuclear envelope is a flattened sac of ER, so its two membranes enclose one lumen; the two membranes of mitochondria and plastids enclose two separate spaces and descend from the envelope of a bacterium (6.1.3) |
| One membrane | ER, Golgi apparatus, endosomes, lysosomes, plant and fungal **vacuoles**, secretory vesicles, peroxisomes (and glyoxysomes) | All but peroxisomes belong to the endomembrane system |
| No membrane | Ribosomes, **centrosomes** and **centrioles**, the **cytoskeleton**, the **nucleolus** and other **condensates** (6.1.4), **proteasomes** | Macromolecular assemblies or condensates in the cytosol or nucleoplasm |

### 6.1.2. The Cytosol

The cytoplasm is everything inside the plasma membrane except the nucleus; the cytosol is its fluid part, outside the membrane-enclosed organelles (both terms are defined in [7.1.1](/7.1.1)). The cytosol is not a dilute solution: it contains about $200$–$300\,\mathrm{g\,L^{-1}}$ of protein, so that **macromolecular crowding** raises the effective concentrations and association constants of **macromolecules**, slows their diffusion (GFP diffuses about four times more slowly in the cytoplasm than in water), and favors compact states. It is crossed by the filaments of the cytoskeleton ([7.3.13](/7.3.13)–[7.3.15](/7.3.15)), which organize it, and is the site of protein synthesis, of most folding by cytosolic **chaperones**, and of degradation by the **ubiquitin–proteasome system** ([7.2.20](/7.2.20)). Some textbooks call the cytosol together with the cytoskeleton that pervades it the cytoplasmic matrix (cytomatrix), stressing that it is a structured gel rather than a solution. Its functions are many.

| Function | Examples |
|---|---|
| Metabolism | **Glycolysis**, the **pentose phosphate pathway**, **gluconeogenesis** (most steps), **glycogen** synthesis and breakdown, fatty acid synthesis, synthesis of nucleotides and many amino acids ([7.1.18](/7.1.18)–[7.1.28](/7.1.28)) |
| Protein synthesis and quality control | Translation on free ribosomes; folding by chaperones; modification (phosphorylation, acetylation, **ubiquitination**); selective degradation by the proteasome; the **N-end rule** ([7.2.20](/7.2.20)) |
| Ionic and chemical environment | Kept at pH about 7.2, low $\ce{Na+}$ and $\ce{Ca^2+}$, high $\ce{K+}$ ([7.3.5](/7.3.5)), and reducing (high glutathione) |
| Supply of the organelles | Substrates, ATP and **cofactors** for organelle metabolism; all nuclear-encoded organelle proteins (6.3) |
| Signaling and control of gene expression | **Second messengers**, kinase cascades, the cytoplasmic retention and release of transcription factors ([7.3.18](/7.3.18)); **cytoplasmic determinants** of cell fate ([7.3.24](/7.3.24)) |
| Organization and transport | Anchoring of organelles and **mRNAs** on the cytoskeleton; motor-driven transport ([7.3.13](/7.3.13)–[7.3.15](/7.3.15)) |

### 6.1.3. The Endomembrane System and Its Topology

**Definition 6.1.2 (Endomembrane System)** The **endomembrane system** comprises the organelles that exchange membrane and lumenal content with one another and with the plasma membrane by vesicle traffic, or are continuous with one another: the endoplasmic reticulum and nuclear envelope, the Golgi apparatus, endosomes, lysosomes, transport and secretory vesicles, and the plasma membrane itself.

Mitochondria and plastids are not part of it: they arose by endosymbiosis (**endosymbiotic theory**, [7.1.1](/7.1.1)), have their own genomes, grow by importing proteins from the cytosol and divide, and exchange no vesicles with other organelles. Peroxisomes occupy an intermediate position: they import most of their proteins from the cytosol but can arise from the ER (6.7.3).

The organelles of the endomembrane system are topologically related. The lumen of each compartment is equivalent to the outside of the cell: a vesicle that buds from one membrane and fuses with another carries its lumenal content from lumen to lumen, and the cytosolic face of its membrane always faces the cytosol. This explains why glycans, added in the ER and Golgi lumens, are found on the outside of the plasma membrane ([7.3.4](/7.3.4#sec-4.6.1)), and why secretion and **endocytosis** are mirror images. The nuclear envelope, a double membrane whose **perinuclear space** is continuous with the ER lumen, fits the same picture, and suggests how the system arose: by invagination of the plasma membrane of an ancestral cell around its chromosomes and into its cytoplasm. Because the cytosol and the nucleoplasm are connected through nuclear pores, they are topologically one space, whereas the **mitochondrial matrix** and the chloroplast stroma are separate spaces, derived from the cytoplasm of the bacterial ancestors.

### 6.1.4. Membraneless Compartments

Cells also concentrate molecules without membranes, in **biomolecular condensates** formed by **liquid–liquid phase separation** of proteins and RNAs held together by **multivalency** and **intrinsically disordered regions** ([7.2.21](/7.2.21)): the nucleolus, Cajal bodies and nuclear speckles in the nucleus; **stress granules**, P-bodies and germ granules in the cytoplasm. Their physics is treated in [7.2.21](/7.2.21); for the cell biologist two points matter. First, condensates are functional compartments that cooperate with membrane organelles. At presynaptic terminals, the reserve pool of synaptic vesicles is held together by a condensate of synapsin and other proteins, which keeps hundreds of vesicles clustered yet mobile and releases them when synapsin is phosphorylated; in the postsynaptic density, scaffold proteins form condensates that concentrate receptors and signaling enzymes. In cyanobacteria and some chemoautotrophs, Rubisco is condensed with a linker protein and enclosed by a protein shell in carboxysomes, which concentrate $\ce{CO2}$ for carbon fixation. Second, condensates change their material state over time, from liquid to gel to solid, and the cell disposes of them by selective autophagy ([7.3.11](/7.3.11)). In *Caenorhabditis elegans* embryos the P granules left in somatic cells are converted by the adaptor proteins SEPA-1 and EPG-2 into gel-like assemblies that are degraded by autophagy; in mammalian cells the chaperonin subunit CCT2 acts as a receptor that targets solid protein aggregates, but not liquid condensates, to autophagosomes. Aggregates that escape such clearance accumulate in neurodegenerative diseases.

## 6.2. How Big Should an Organelle Be?

The sizes of organelles scale with the size of the cell. In budding yeast the total volume of the mitochondrial network is proportional to cell volume; in the early embryos of *C. elegans* and *Xenopus*, whose cells halve their volume at each cleavage division, the centrosomes, mitotic spindles and nuclei become smaller in proportion. In extracts of *Xenopus* eggs confined in droplets of different sizes, spindles assembled in small droplets are smaller, and spindle length scales with droplet volume until it reaches a maximum. These observations suggest that size is set, at least in part, not by a ruler inside each organelle but by the amount of material the cell provides.

**Definition 6.2.1 (Limiting-Pool Model)** In the **limiting-pool model** of organelle size, an organelle assembles from a cytoplasmic pool of subunits whose total amount is proportional to cell volume; it grows as long as the free subunit concentration exceeds a critical value set by the balance of assembly and disassembly, so that growth depletes the pool until assembly and disassembly balance, and the steady-state size is determined by the amount of subunit available, not by an intrinsic property of the organelle.

**Proposition 6.2.1** Let the total amount of subunit be $N = \rho V$ in a cell of volume $V$, let the organelle of size $S$ (in subunits) gain subunits at the rate $k_{\mathrm{on}}c$, where $c = (N - S)/V$ is the free concentration, and lose them at the constant rate $k_{\mathrm{off}}$. Then $S$ approaches

$$
S^* = N - c^*V = (\rho - c^*)V, \qquad c^* = \frac{k_{\mathrm{off}}}{k_{\mathrm{on}}},
$$
exponentially with time constant $V/k_{\mathrm{on}}$, provided $\rho > c^*$; if $\rho \le c^*$ no organelle forms.

**Proof** The size obeys $\mathrm{d}S/\mathrm{d}t = k_{\mathrm{on}}(N - S)/V - k_{\mathrm{off}}$, a linear equation with fixed point $S^* = N - (k_{\mathrm{off}}/k_{\mathrm{on}})V$ and relaxation rate $k_{\mathrm{on}}/V$; the solution from $S(0) = 0$ is $S(t) = S^*(1 - \mathrm{e}^{-k_{\mathrm{on}}t/V})$. Substituting $N = \rho V$ gives the result. $\square$

The model makes testable predictions: organelle size is proportional to cell volume when expression per volume is constant; it falls when the subunit is depleted (lower $\rho$) and rises when it is overexpressed; and the free subunit concentration at steady state is the same in cells of every size. Centrosomes in *C. elegans* embryos behave this way: their size is limited by the amount of the scaffold protein SPD-2 per cell, and when one of the two centrosomes is removed, the other grows larger.

![The limiting-pool model of organelle size (Proposition 6.2.1, arbitrary units, ρ = 1, c* = 0.4). A: an organelle grows from its subunit pool until the free concentration has fallen to c*; in cells of volume 1, 2 and 4 the final sizes (dotted lines) are proportional to volume, and larger cells take longer to reach them. B: steady-state size against cell volume: a straight line through the origin for the limiting-pool model, with scatter when expression varies between cells by 8 % (points); lowering the expression per volume (ρ = 0.7, dashed) lowers the slope. An organelle whose size is fixed by an intrinsic ruler would have the same size in all cells (gray)](./plots/limiting-pool.py)

Not every organelle is sized by a pool. When two organelles compete for one pool by the same autocatalytic growth, the model leaves their relative sizes undetermined, and cells use additional feedback to make them equal. Other mechanisms of size control are a balance between length-dependent assembly and length-independent disassembly (the length of the flagella of *Chlamydomonas*, set by the rate at which intraflagellar transport delivers subunits to the tip, [7.3.14](/7.3.14)), and growth limited by an import rate (the nucleus, whose volume tracks cell volume at a constant nuclear-to-cytoplasmic ratio, [7.3.16](/7.3.16)). The question of how the parts of a cell are matched to the whole recurs in [7.3.22](/7.3.22) for cell size itself.

## 6.3. The Logic of Protein Sorting

### 6.3.1. Three Modes of Transport

**Definition 6.3.1 (Protein Sorting)** **Protein sorting** (protein targeting) is the delivery of each protein, after or during its synthesis, to the compartment in which it functions, directed by information in its own sequence. Proteins move between compartments in three ways:

- by **gated transport** between topologically equivalent spaces, the cytosol and the nucleus, through nuclear pore complexes that let folded proteins and large complexes pass selectively and let small molecules diffuse;
- by **transmembrane transport** across a membrane from the cytosol into a topologically distinct space (ER lumen, mitochondria, plastids, peroxisomes), through a protein translocator, usually in an unfolded state;
- by **vesicular transport** between topologically equivalent compartments of the endomembrane system, in membrane-enclosed carriers that bud from one compartment and fuse with the next.

The road map that follows from this is simple. Every nuclear-encoded protein starts on cytosolic ribosomes. Proteins without a sorting signal stay in the cytosol. A protein that enters the ER can then reach the Golgi apparatus, the plasma membrane, endosomes and lysosomes, or the cell exterior, by vesicles, without crossing another membrane; a protein that is to reach the mitochondria, plastids or peroxisomes must be imported directly from the cytosol. The first decision, ER or not, is therefore the most important one, and it is made in the first seconds of synthesis.

![The road map of protein sorting. All nuclear-encoded proteins are made on ribosomes in the cytosol. Gated transport (purple, dashed) through nuclear pores connects the cytosol with the nucleus; transmembrane transport by translocators (red) takes proteins from the cytosol into the ER, mitochondria, plastids and peroxisomes; vesicular transport (blue) connects the compartments of the secretory and endocytic pathways (inside the dashed frame), whose lumens are topologically equivalent to the outside of the cell](./plots/sorting-road-map.py)

### 6.3.2. Sorting Signals

**Definition 6.3.2 (Sorting Signal)** A **sorting signal** is a feature of a protein that directs it to a particular compartment: a stretch of contiguous amino acids (a signal sequence, often 15–60 residues, at the N- or C-terminus or internal), or a signal patch formed in the folded protein by residues distant in the sequence, or a modification such as a particular glycan. Signals are read by sorting receptors that deliver the protein to a translocator or a vesicle coat; signals that are removed after use are cleaved by signal peptidases.

| Destination | Signal | Example of the signal | Read by |
|---|---|---|---|
| ER lumen (import) | N-terminal **signal sequence**: positive n-region, hydrophobic core of 7–15 residues, polar c-region with cleavage site | $^+$H₃N-Met-Met-Ser-Phe-Val-Ser-Leu-Leu-Leu-Val-Gly-Ile-Leu-Phe-Trp-Ala-Thr-Glu-Ala-Glu-Gln-Leu-Thr-Lys-Cys-Glu-Val-Phe-Gln- | SRP, Sec61 |
| Return to ER | C-terminal Lys-Asp-Glu-Leu (KDEL) | -Lys-Asp-Glu-Leu-COO⁻ | KDEL receptor ([7.3.8](/7.3.8)) |
| Mitochondrial matrix | N-terminal amphipathic helix with Arg and Lys, cleaved | $^+$H₃N-Met-Leu-Ser-Leu-Arg-Gln-Ser-Ile-Arg-Phe-Phe-Lys-Pro-Ala-Thr-Arg-Thr-Leu-Cys-Ser-Ser-Arg-Tyr-Leu-Leu- | Tom20, Tom22, TIM23 |
| Plastid stroma | N-terminal transit peptide, rich in Ser and Thr, cleaved | $^+$H₃N-Met-Val-Ala-Met-Ala-Met-Ala-Ser-Leu-Gln-Ser-Ser-Met-Ser-Ser-Leu-Ser-Leu-Ser-Ser-Asn-Ser-Phe-Leu-Gly-Gln-Pro-Leu-Ser-Pro-Ile-Thr-Leu-Ser-Pro-Phe-Leu-Gln-Gly- | TOC, TIC |
| Peroxisome | C-terminal PTS1 or N-terminal PTS2 | -Ser-Lys-Leu-COO⁻ | Pex5, Pex7 |
| Nucleus | internal basic NLS | -Pro-Pro-Lys-Lys-Lys-Arg-Lys-Val- | importins ([7.3.16](/7.3.16)) |
| Nuclear export | leucine-rich NES | -Met-Glu-Glu-Leu-Ser-Gln-Ala-Leu-Ala-Ser-Ser-Phe- | exportins |
| Lysosome | mannose 6-phosphate on N-linked glycans, added after recognition of a signal patch | — | M6P receptors ([7.3.11](/7.3.11)) |

(Sequences from MBoC 7e, Figure 12–13; signals for vesicle coats, such as the tyrosine and dileucine motifs of endocytosed receptors, appear in [7.3.8](/7.3.8) and [7.3.10](/7.3.10).) Two properties of sorting signals are general. They are recognized by their physical character, hydrophobicity, charge and amphipathic shape, rather than by an exact sequence: signal sequences from different proteins share almost no identical residues, and a large fraction of random peptides can function as mitochondrial presequences. And they are transferable: fused to a cytosolic protein, a signal sequence takes it to the corresponding organelle, which is the standard test that a sequence is a signal and also the basis of the fluorescent organelle markers used in live-cell imaging ([7.3.2](/7.3.2)).

## 6.4. Translocation into the Endoplasmic Reticulum

### 6.4.1. The Signal Hypothesis

In 1972 César Milstein and colleagues found that the light chain of immunoglobulin translated in a cell-free system was about 20 residues longer at its N-terminus than the light chain secreted by myeloma cells, and that adding ER membranes (microsomes) to the translation produced the mature size. Günter Blobel and David Sabatini (1971) had already proposed, and Blobel and Bernhard Dobberstein (1975) demonstrated, the explanation.

**Definition 6.4.1 (Signal Hypothesis)** The **signal hypothesis** states that a protein destined for secretion carries at its N-terminus a signal sequence that, as it emerges from the ribosome, directs the ribosome to the ER membrane and the growing chain into the ER lumen, where the signal is removed; in its generalized form (Blobel, 1980), every protein contains in its sequence the information that specifies its location in the cell.

The machinery is described in [7.2.19](/7.2.19#sec-19.9.2): the signal recognition particle, a ribonucleoprotein of the $300$-nucleotide 7SL RNA and six polypeptides (SRP54 binds the signal sequence and is a GTPase; SRP9 and SRP14 cause the pause in elongation), binds the signal sequence as it emerges from the ribosome and slows elongation, docks on the SRP receptor in the ER membrane, and hands the ribosome to the translocator; GTP hydrolysis by both GTPases releases SRP for another round. Ribosomes making proteins for the ER are thus attached to the ER membrane only while they make such a protein; the "membrane-bound" and "free" ribosomes are the same population, and a single mRNA is translated by a **polysome** of ER-bound ribosomes. Blobel received the 1999 Nobel Prize in Physiology or Medicine.

### 6.4.2. The Sec61 Translocon

**Definition 6.4.2 (Sec61 Translocon)** The **Sec61 translocon** is the protein-conducting channel of the ER membrane, a heterotrimer of Sec61α (ten transmembrane helices arranged as a clamshell around an hourglass-shaped pore), Sec61β and Sec61γ, homologous to SecYEG of bacteria and archaea. A ring of hydrophobic residues at the constriction and a short plug helix seal the pore in the resting state; a lateral gate between transmembrane helices 2 and 7 of Sec61α opens towards the lipid bilayer and lets hydrophobic segments of the chain leave the channel sideways into the membrane.

The signal sequence opens the channel by binding at the lateral gate as a helix, which displaces the plug; the chain then passes as a loop, its N-terminus remaining in the channel and its downstream part threading into the lumen. The lumen and the cytosol are not connected for small molecules during translocation, because the ribosome seals the channel on one side, the hydrophobic pore ring fits tightly around the chain, and BiP binds the channel on the lumenal side when it is idle. Signal peptidase, associated with the translocon, cleaves the signal on the lumenal side, and oligosaccharyltransferase, another neighbor, adds N-linked glycans as the chain emerges ([7.3.7](/7.3.7)).

### 6.4.3. Co- and Posttranslational Translocation

**Definition 6.4.3 (Co- and Posttranslational Translocation)** In **cotranslational translocation** the polypeptide passes through the translocon while it is still being synthesized by a ribosome bound to the channel, and the elongating ribosome itself provides the directionality. In **posttranslational translocation** a completed polypeptide, released from the ribosome and kept unfolded by cytosolic chaperones, is imported through the translocon; in eukaryotes this requires the Sec62–Sec63 complex and the lumenal chaperone BiP, whose ATP-dependent binding to the emerging chain prevents it from sliding back.

In mammals, most secretory and membrane proteins enter cotranslationally, but short secretory proteins (under about 160 residues, which are released from the ribosome almost as soon as their signal emerges) and tail-anchored proteins (6.4.5) are imported after translation. Yeast imports many proteins posttranslationally, and bacteria export most proteins posttranslationally through SecYEG, with the cytosolic ATPase SecA pushing the chain through in steps.

How can a chaperone that only binds pull a chain? BiP does not pull. The chain diffuses back and forth in the channel by thermal motion; whenever enough of it has emerged on the lumenal side, a molecule of BiP in its ATP state binds, and hydrolysis of ATP locks it on. The bound BiP is too large to fit through the channel, so the chain can no longer move back past that point, while it remains free to move forward. Thermal motion is rectified into directed translocation: this is a Brownian ratchet, and the same mechanism operates in mitochondrial import (6.5.3).

### 6.4.4. Signals Determine the Topology of Membrane Proteins

The same machinery inserts integral membrane proteins into the ER membrane, and the arrangement of hydrophobic segments in the sequence determines how each protein will span the membrane. Two kinds of signal combine.

**Definition 6.4.4 (Start- and Stop-Transfer Sequences)** A **start-transfer sequence** is a hydrophobic segment that opens the translocon and initiates translocation of the following part of the chain into the ER lumen: a cleaved N-terminal signal sequence, or an internal, uncleaved signal-anchor sequence that remains in the membrane as a transmembrane helix. A **stop-transfer sequence** is a hydrophobic segment that enters the translocon after translocation has started, stops it, and leaves the channel laterally into the bilayer as a transmembrane helix, so that the rest of the chain remains in the cytosol.

| Type | Signals | Orientation | Examples |
|---|---|---|---|
| Soluble lumenal or secreted | cleaved N-terminal signal sequence | entire chain in the lumen | albumin, insulin, antibodies, BiP |
| Single-pass type I | cleaved signal sequence + stop-transfer sequence | N-terminus in the lumen (outside), C-terminus in the cytosol | LDL receptor, insulin receptor, glycophorin |
| Single-pass type II | internal signal anchor, positive charges on its N-terminal side | N-terminus in the cytosol, C-terminus in the lumen | transferrin receptor, Golgi glycosyltransferases |
| Single-pass type III | internal signal anchor, positive charges on its C-terminal side | N-terminus in the lumen, C-terminus in the cytosol | cytochrome P-450 of the ER |
| Tail-anchored | single C-terminal transmembrane segment | N-terminus in the cytosol | Sec61β, cytochrome b₅, SNAREs, Bcl-2 family (on mitochondria) |
| Multipass | alternating start- and stop-transfer sequences (internal signal anchors) | set by the first segment | GPCRs, transporters, channels |
| GPI-anchored | cleaved signal sequence + C-terminal GPI signal | entire protein in the lumen, attached to the lumenal leaflet | alkaline phosphatase, CD59, prion protein |

The orientation of a signal-anchor sequence is decided mainly by the distribution of charged residues around it: the side with more positive charge stays in the cytosol, the positive-inside rule seen in the **hydropathy plots** of [7.1.13](/7.1.13#sec-13.1.5) (and an N-terminal domain that folds quickly in the cytosol also cannot be translocated). In a multipass protein, the first signal anchor sets the orientation and the following segments alternate as stop- and start-transfer sequences, so that the topology of the whole protein can usually be predicted from its sequence. The real process is more flexible: segments can reorient after insertion, and multipass proteins with weakly hydrophobic segments are inserted with the help of further complexes associated with Sec61 (the EMC and the "multipass translocon"), which shield polar residues until the helices pack against each other.

![Topologies of membrane proteins made at the ER (lumen, topologically equivalent to the exterior, at the top). From left to right: a soluble secretory protein, released entirely into the lumen after its signal sequence is cleaved; a type I protein, held in the membrane by a stop-transfer sequence; type II and type III proteins, held by an internal signal-anchor sequence (pink) whose orientation is set by the positive charges (+) flanking it; a tail-anchored protein, with one C-terminal transmembrane segment inserted after translation; a multipass protein, with alternating start- and stop-transfer segments; a GPI-anchored protein, whose C-terminal segment has been replaced by a glycosylphosphatidylinositol anchor in the lumenal leaflet](./plots/membrane-protein-topology.py)

**Example 6.4.1** A protein of 420 residues has hydrophobic segments (each about 20 residues) at positions 30–50, 95–115, 160–180 and 300–320, and no cleavable signal; the loop between residues 1 and 30 contains five Lys and Arg, the loop 51–94 none, the loop 116–159 four, and the loop 181–299 one. Predict its topology. The first hydrophobic segment acts as a signal anchor; the positive N-terminal flank stays in the cytosol, so residues 51–94 are in the lumen. The second segment acts as a stop-transfer sequence, so loop 116–159 (positive, as the rule requires) is cytosolic; the third segment is a start-transfer, so 181–299 is lumenal (one positive residue, consistent); the fourth is a stop-transfer and the C-terminus (321–420) is cytosolic. The protein has four transmembrane helices with both termini in the cytosol; its N-glycosylation sites (Asn-X-Ser/Thr) should lie in loops 51–94 and 181–299, which is one way to test the prediction experimentally (glycosylation reporters, protease protection, [7.3.4](/7.3.4#ex-4.3.1)).

### 6.4.5. Tail-Anchored Proteins and the GET Pathway

**Definition 6.4.5 (Tail-Anchored Protein)** A **tail-anchored protein** is an integral membrane protein with a single transmembrane segment within about 30 residues of its C-terminus and its functional domain in the cytosol; because the transmembrane segment emerges from the ribosome only after translation has terminated, it cannot be recognized by SRP and is targeted and inserted posttranslationally.

About $2$–$5\,\%$ of membrane proteins, several hundred in human cells, are tail-anchored. Those with a strongly hydrophobic tail are captured, as they leave the ribosome, by a pretargeting complex (SGTA and the Bag6 complex in mammals, Sgt2 and Get4–Get5 in yeast) and handed to the ATPase Get3 (TRC40 in mammals), whose hydrophobic groove shields the transmembrane helix in the cytosol. Get3 docks on its receptor Get1–Get2 (WRB–CAML) in the ER membrane, which also acts as the insertase; ATP hydrolysis releases Get3 for a new cycle, a scheme parallel to the SRP cycle with ATP in place of GTP. Tail-anchored proteins with less hydrophobic tails are inserted by the ER membrane protein complex (EMC). Mitochondrial tail-anchored proteins, such as many Bcl-2 family members and Tom5, insert into the outer mitochondrial membrane instead, whose low ergosterol or cholesterol content and specific insertases favor them; the mistargeted ones are extracted by the AAA ATPase Msp1 (ATAD1).

### 6.4.6. GPI Anchors

**Definition 6.4.6 (GPI Anchor)** A **GPI anchor** (glycosylphosphatidylinositol anchor) is a glycolipid, preassembled in the ER membrane (phosphatidylinositol, glucosamine, three mannoses and phosphoethanolamine), that a transamidase attaches to the new C-terminus of a protein after cleaving off a C-terminal hydrophobic signal of 15–20 residues; the protein is then held in the lumenal leaflet of the ER membrane, and later on the outer surface of the plasma membrane, by the anchor's lipid chains alone.

About 150 human proteins are GPI-anchored, including enzymes (alkaline phosphatase), receptors (folate receptor, CD14), adhesion molecules and the complement inhibitors CD55 and CD59. GPI-anchored proteins are concentrated in **lipid rafts** and sorted to the apical surface of many epithelial cells ([7.3.4](/7.3.4#sec-4.6.2)), and they can be released from the cell surface by phospholipases. In paroxysmal nocturnal hemoglobinuria, a hematopoietic stem cell acquires a somatic mutation in *PIGA*, which encodes an enzyme of the first step of GPI synthesis; its descendant red cells lack all GPI-anchored proteins, including CD55 and CD59, and are lysed by complement, an illustration of how a single anchor serves an entire class of proteins.

Proteins that fail to fold in the ER are returned to the cytosol for degradation through a channel formed by the ubiquitin ligase Hrd1 (retrotranslocation), the subject of [7.3.7](/7.3.7).

## 6.5. Protein Import into Mitochondria

### 6.5.1. Presequences and Four Import Routes

A mitochondrion contains about 1000 (yeast) to 1500 (human) different proteins, of which only 8 (yeast) or 13 (human) are encoded by the mitochondrial genome ([7.3.12](/7.3.12)); the rest are made on cytosolic ribosomes and imported into four subcompartments: the outer membrane, the intermembrane space, the inner membrane and the matrix.

**Definition 6.5.1 (Presequence)** A **presequence** (mitochondrial targeting sequence) is an N-terminal sequence of about 15–50 residues that targets a protein to the mitochondrial matrix; it forms an amphipathic **α helix** with positively charged residues (Arg, Lys) on one face and hydrophobic residues on the other, lacks acidic residues, and is cleaved after import by the matrix processing peptidase (MPP).

About two-thirds of mitochondrial proteins have presequences; the others carry internal signals that direct them to the outer or inner membrane or the intermembrane space. All pass through one entry gate in the outer membrane, and then diverge.

**Definition 6.5.2 (Mitochondrial Protein Translocases)** The **TOM complex** (translocase of the outer membrane) is the general entry gate, formed by the **β barrel** Tom40, with the receptors Tom20 (for presequences) and Tom70 (for hydrophobic inner-membrane carriers) and the central receptor Tom22. The **TIM23 complex** (translocase of the inner membrane) imports presequence proteins into the matrix or releases them laterally into the inner membrane, driven by the membrane potential and by the matrix import motor (PAM). The TIM22 complex inserts the multipass carrier proteins of the inner membrane. The **SAM complex** (sorting and assembly machinery, with the β-barrel protein Sam50) inserts β-barrel proteins into the outer membrane from the intermembrane space.

The four main routes, with the less common ones, are summarized in the table and the figure.

| Route | Cargo | Machinery after TOM | Energy |
|---|---|---|---|
| Presequence pathway | matrix proteins (most enzymes of the citric acid cycle, F₁ subunits); inner membrane proteins with presequence + stop-transfer | TIM23 (channel formed mainly by Tim17, with Tim23, Tim50 and Mgr2); import motor: matrix Hsp70 (mtHsp70), Tim44, J-protein Pam18; MPP | $\Delta\psi$ for the presequence; ATP in the matrix for the motor |
| Carrier pathway | multipass inner membrane carriers (ADP/ATP carrier, phosphate carrier) with internal signals | small Tim9–Tim10 chaperones in the intermembrane space; TIM22 | $\Delta\psi$ |
| β-barrel pathway | outer membrane β barrels (Tom40, porin/VDAC) | small TIMs; SAM (Sam50, homologous to bacterial BamA) | none known |
| Disulfide relay (MIA) | small intermembrane space proteins with twin Cys motifs | Mia40 forms a transient disulfide with the incoming protein and oxidizes it; Erv1 reoxidizes Mia40 and passes electrons to cytochrome c | oxidative folding traps the protein |
| Insertion from the matrix | mtDNA-encoded inner membrane proteins; some imported ones (conservative sorting) | Oxa1 (homologous to bacterial YidC) | — |
| Outer membrane α-helical | signal-anchored and multipass outer membrane proteins | MIM complex | — |

![Protein import into mitochondria (schematic). All imported proteins enter through the TOM complex (Tom40 channel, Tom20 and Tom22 receptors). Presequence pathway (left): the positively charged presequence is pulled through TIM23 by the membrane potential Δψ across the inner membrane (positive outside), the chain is drawn into the matrix by the import motor mtHsp70, and the presequence is cleaved by MPP. Carrier pathway: carriers are escorted across the intermembrane space by the small Tim9–Tim10 chaperones and inserted by TIM22. β-barrel pathway: outer membrane β barrels return from the intermembrane space to the SAM complex. Disulfide relay: small cysteine-rich proteins are oxidized by Mia40 (reoxidized by Erv1) and thereby trapped in the intermembrane space. Oxa1 inserts proteins into the inner membrane from the matrix](./plots/mitochondrial-import.py)

Recent cryo-EM structures of the TIM23 complex (2023, including work from Long Li's group) settled a long-standing question: the protein-conducting path is formed mainly by Tim17, whose concave, negatively charged face, with Mgr2 and parts of Tim23, lines a channel through which the presequence passes; Tim17 alone can act as a translocase and insertase. The older model, in which Tim23 formed the channel, rested largely on electrophysiology of reconstituted proteins.

### 6.5.2. What Drives Import

Import across the two membranes needs three inputs of energy. ATP in the cytosol is used by cytosolic Hsp70 chaperones to keep precursors unfolded and import-competent. The membrane potential across the inner membrane, $150$–$180\,\mathrm{mV}$ negative inside, one component of the **proton-motive force** ([7.1.23](/7.1.23)), pulls the positively charged presequence through TIM23 electrophoretically; uncouplers, which collapse it, block import, and this requirement is the reason mitochondria need a working **respiratory chain** or a reversed **ATP synthase** to grow. ATP in the matrix is used by mtHsp70, which binds the chain as it emerges and drives it in; many imported proteins are then folded in the matrix by the chaperonin Hsp60–Hsp10, the mitochondrial counterpart of bacterial GroEL–GroES ([7.1.6](/7.1.6)), whereas some first exposed on the matrix side are sorted back into the inner membrane by Oxa1.

**Example 6.5.1** How strong is the electrophoretic pull? A presequence with $z = 4$ net positive charges in an inner membrane of thickness $d \approx 4\,\mathrm{nm}$ with $\Delta\psi = 160\,\mathrm{mV}$ feels a force $F = ze\Delta\psi/d = 4 \times 1.6\times10^{-19}\,\mathrm{C} \times 0.16\,\mathrm{V}/(4\times10^{-9}\,\mathrm{m}) \approx 26\,\mathrm{pN}$, and gains an energy $ze\Delta\psi = 0.64\,\mathrm{eV} \approx 24\,k_{\mathrm{B}}T$. That is enough to pull the presequence across the membrane and partly unfold a weakly folded domain that follows, but not a stable one; and the force acts only on the charges in the membrane, so it cannot import the rest of the chain. The motor does that.

Classical experiments established that the chain crosses both membranes at once, unfolded, at sites where the two membranes are close. A fusion of a presequence to mouse **dihydrofolate reductase** (DHFR) is imported normally; in the presence of methotrexate, which binds DHFR and stabilizes its fold, import stops with the presequence in the matrix (where it is cleaved by MPP) and the DHFR domain outside the outer membrane. Such stalled intermediates span TOM and TIM23 simultaneously: imports through the two membranes are coupled.

### 6.5.3. The Import Motor as a Brownian Ratchet

How mtHsp70 drives the chain has been debated in terms of two limiting models. In the power-stroke model, mtHsp70 bound to Tim44 at the channel exit binds the chain and pulls it inward by a conformational change. In the ratchet model, mtHsp70 binds whichever segment has diffused into the matrix and prevents it from sliding back, exactly as BiP does at the ER (6.4.3). The ratchet model has a simple quantitative form.

**Formula 6.5.1 (Translocation Ratchet)** Let a chain diffuse in a channel with coefficient $D$, and let a ratcheting molecule bind each time a further length $\delta$ has emerged, fast and irreversibly (a perfect ratchet). The mean velocity of translocation against an opposing force $f$ is (Simon, Peskin and Oster, 1992)

$$
v = \frac{2D}{\delta}\cdot\frac{\omega^2/2}{\mathrm{e}^{\omega} - 1 - \omega}, \qquad \omega = \frac{f\delta}{k_{\mathrm{B}}T},
$$
which tends to $v = 2D/\delta$ at zero load and falls roughly exponentially at large load.

The zero-load result can be understood from the time to diffuse a distance $\delta$ next to a reflecting wall, $\delta^2/(2D)$. The ratchet requires no force-producing step: its energy comes from the binding and ATP hydrolysis of the chaperone, which make the bound state irreversible, and its stall force depends on that free energy. Ratchets of this kind, with filament polymerization in place of chaperone binding, also explain how actin pushes the membrane forward ([7.3.13](/7.3.13)). For mitochondrial import the evidence suggests that both mechanisms contribute: ratcheting suffices for loosely folded proteins, whereas tightly folded domains outside the outer membrane need active pulling to be unfolded. Import is often limited not by translocation but by the rate at which domains outside unfold spontaneously, which is why destabilizing mutations speed import.

![The translocation ratchet (units δ = D = k_B T = 1). A: a chain diffusing in a channel, with (green) and without (gray) a ratchet that blocks backward motion past each newly bound site; rectified diffusion advances at the mean velocity 2D/δ (dashed), while free diffusion goes nowhere on average. B: velocity against the opposing load fδ/k_B T from 200 simulated chains (points) agrees with Formula 6.5.1 (line)](./plots/translocation-ratchet.py)

## 6.6. Protein Import into Chloroplasts

Chloroplasts contain about 3000 proteins, of which fewer than 100 are encoded by the plastid genome. Nuclear-encoded stromal proteins carry an N-terminal transit peptide, 30–100 residues long, rich in hydroxylated residues and with few acidic ones, which is recognized at the outer envelope and removed by the stromal processing peptidase.

**Definition 6.6.1 (TOC and TIC Complexes)** The **TOC complex** (translocon at the outer envelope membrane of chloroplasts) contains the β-barrel channel Toc75 (an Omp85 family member, like Sam50) and the GTPase receptors Toc159 and Toc34, which recognize transit peptides. The **TIC complex** (translocon at the inner envelope membrane) is a large complex of about 1 MDa whose channel is formed by Tic20, Tic214 (encoded in the chloroplast genome) and other subunits; an ATP-driven motor in the stroma, including the AAA protein complex Ycf2–FtsHi and the chaperones Hsp93 and Hsp70, pulls the chain into the stroma.

Import into chloroplasts differs from mitochondrial import in its energy source: there is no membrane potential across the envelope, and import is driven by GTP at the TOC receptors and ATP in the stroma. Proteins of the thylakoid membrane and lumen carry, behind the transit peptide, a second signal that becomes exposed after cleavage in the stroma (a bipartite signal) and directs them across or into the thylakoid membrane by one of four routes, three of them inherited from the cyanobacterial ancestor. Plastocyanin, a copper protein of the thylakoid lumen, is the classic example: its precursor carries an N-terminal transit peptide, removed in the stroma after import through TOC and TIC, followed by a thylakoid signal resembling a bacterial signal sequence, which directs it through the cpSec translocon into the lumen, where it is cleaved by the thylakoid processing peptidase. Each signal is read by the machinery of one membrane, and the order of the signals in the sequence reproduces the order of the membranes the protein must cross.

| Pathway | Cargo | Machinery | Energy | Bacterial counterpart |
|---|---|---|---|---|
| cpSec | unfolded lumenal proteins (plastocyanin, PsbO) | SecA, SecY–SecE | ATP | Sec |
| cpTat | folded lumenal proteins, often with bound cofactors; signal with a twin-arginine (RR) motif | Tha4, Hcf106, cpTatC | thylakoid $\Delta\mathrm{pH}$ | Tat |
| cpSRP | light-harvesting chlorophyll-binding proteins (LHCP) of the membrane | cpSRP43–cpSRP54, cpFtsY, the insertase Alb3 | GTP | SRP, YidC |
| Spontaneous | some single-pass membrane proteins | none | — | — |

The thylakoid lumen is a fourth space within a single organelle, and the Tat pathway is remarkable in transporting fully folded proteins across a membrane without dissipating its proton gradient. The organelle biology of plastids (types and interconversion, division, signaling to the nucleus) is described in [7.3.12](/7.3.12).

## 6.7. Peroxisomes

### 6.7.1. What Peroxisomes Do

Peroxisomes and the related glyoxysomes of plant seeds were first described in electron micrographs of liver and kidney (Johannes Rhodin, 1954) as microbodies, small vesicles with a granular matrix, often containing a crystalline core of urate oxidase; de Duve's fractionation then defined them by their enzymes ([7.3.3](/7.3.3)).

**Definition 6.7.1 (Peroxisome)** A **peroxisome** is a small organelle (usually $0.1$–$1\,\mu\mathrm{m}$), bounded by a single membrane and lacking a genome, that contains oxidases which use $\ce{O2}$ to oxidize organic substrates and produce hydrogen peroxide, and catalase, which decomposes or uses the $\ce{H2O2}$; it imports its matrix proteins from the cytosol in a folded state.

The name comes from the hydrogen peroxide. Peroxisomal oxidases (urate oxidase in most mammals other than humans, D-amino acid oxidase, acyl-CoA oxidase) transfer hydrogen atoms from their substrates to $\ce{O2}$:

$$
\ce{RH2 + O2 -> R + H2O2}, \qquad \ce{2H2O2 ->[catalase] 2H2O + O2} \quad\text{or}\quad \ce{H2O2 + R'H2 ->[catalase] R' + 2H2O}.
$$
Catalase uses the $\ce{H2O2}$ to oxidize phenols, formic acid, formaldehyde and ethanol; in liver and kidney about a quarter of ingested ethanol is oxidized in this way. Peroxisomes have five main metabolic functions:

| Function | Details | Links |
|---|---|---|
| **β oxidation** of very-long-chain fatty acids | chains longer than C₂₂ are shortened in peroxisomes (first step by acyl-CoA oxidase, producing $\ce{H2O2}$ instead of $\ce{FADH2}$), then finished in mitochondria; in yeast and plants all fatty acid oxidation is peroxisomal | [7.1.21](/7.1.21) |
| Ether lipid synthesis | the first steps of **plasmalogen** synthesis; plasmalogens make up about $80\,\%$ of the phospholipid of myelin | [7.1.12](/7.1.12) |
| Bile acids and other lipids | side-chain shortening of cholesterol in bile acid synthesis; degradation of phytanic acid (α oxidation) | [7.1.26](/7.1.26) |
| Plant glyoxysomes | in germinating oilseeds, β oxidation and the **glyoxylate cycle** convert stored fat into succinate and sugar | [7.1.25](/7.1.25) |
| Plant leaf peroxisomes | glycolate oxidase in **photorespiration**, with chloroplasts and mitochondria | [7.1.25](/7.1.25) |

Trypanosomes even carry out glycolysis in peroxisome-related glycosomes. The content of peroxisomes changes with the needs of the cell: yeast grown on methanol or oleic acid fills with large peroxisomes containing the enzymes that metabolize them.

### 6.7.2. Import of Folded Proteins

**Definition 6.7.2 (Peroxin and PTS)** **Peroxins** (Pex proteins, encoded by *PEX* genes) are the more than 30 proteins required for the biogenesis of peroxisomes and the import of their proteins. Most peroxisomal matrix proteins carry the peroxisomal targeting signal **PTS1**, a C-terminal tripeptide Ser-Lys-Leu (SKL) or a conservative variant, recognized by the cytosolic receptor Pex5; a minority carry **PTS2**, an N-terminal nonapeptide recognized by Pex7 together with a coreceptor.

The receptor binds its cargo in the cytosol, docks on the membrane proteins Pex13 and Pex14, and becomes part of a transient import pore through which the cargo enters. Unlike the translocators of the ER and mitochondria, this machinery imports folded, cofactor-bound and even oligomeric proteins: gold particles $9\,\mathrm{nm}$ in diameter coated with a PTS1 peptide are imported into peroxisomes. Energy is spent not on cargo translocation but on recycling the receptor: Pex5 is monoubiquitinated on a conserved cysteine by the RING ubiquitin ligases Pex2–Pex10–Pex12, which together also form a channel for its retrotranslocation, and pulled back into the cytosol by the AAA ATPases Pex1 and Pex6, anchored on the membrane by Pex15 (Pex26 in mammals). In this "export-driven import" model, removal of the receptor from the membrane releases the cargo inside. Peroxisomal membrane proteins use a different route, the cytosolic receptor Pex19 and the membrane docking protein Pex3.

### 6.7.3. Biogenesis and Disease

Peroxisomes multiply in two ways. Existing peroxisomes grow by importing proteins and lipids and divide: Pex11 elongates them, and the dynamin-related GTPase Drp1 and its adaptors, shared with mitochondria, cut them ([7.3.12](/7.3.12)). They can also form anew from the ER: yeast mutants lacking *PEX3* have no peroxisomes, and on reintroduction of the gene, Pex3 first appears in the ER and then in vesicles that mature into peroxisomes. In wild-type cells both routes operate, and the relative contributions differ between organisms.

Defects of peroxisome biogenesis cause the Zellweger spectrum disorders, the most severe of which is *Zellweger syndrome*, a lethal recessive disease of newborns caused by mutations in any of a dozen *PEX* genes (most often *PEX1*). The patients' cells contain empty peroxisomal membranes ("ghosts") while the matrix enzymes, unable to enter, remain in the cytosol and are degraded; very-long-chain fatty acids accumulate in the blood (the diagnostic test), plasmalogens are deficient, and the brain, liver and kidneys are severely abnormal, with death usually in the first year. Other diseases affect a single peroxisomal protein: X-linked adrenoleukodystrophy, caused by mutations in the **ABC transporter** ABCD1 that imports very-long-chain acyl-CoA into peroxisomes, destroys myelin in the brain and the function of the adrenal cortex.

## 6.8. Exceptions to the Rules: Unconventional Secretion and Nonvesicular Lipid Traffic

### 6.8.1. Secretion without a Signal Sequence

It was long a dogma that secreted proteins must carry a signal sequence and pass through the ER and Golgi apparatus. A number of proteins, however, leave cells although they have none.

**Definition 6.8.1 (Unconventional Protein Secretion)** **Unconventional protein secretion** is the release of proteins from cells by routes other than the conventional pathway from the ER through the Golgi apparatus to the plasma membrane: either the secretion of cytosolic proteins without a signal sequence ("leaderless" proteins) or the delivery of transmembrane proteins to the plasma membrane that bypasses the Golgi apparatus.

Four routes are distinguished.

| Type | Route | Examples |
|---|---|---|
| I: direct translocation across the plasma membrane | the protein binds PI(4,5)P₂ in the inner leaflet, oligomerizes and forms a lipidic pore through which it passes; heparan sulfate proteoglycans capture it outside; or it leaves through protein pores | FGF2 (Walter Nickel); interleukin-1β through gasdermin D pores in activated macrophages (gasdermin D was identified as the executor of pyroptosis by Feng Shao's group, [7.3.25](/7.3.25)) |
| II: ABC transporter | an **ABC transporter** of the plasma membrane exports a peptide | yeast a-factor (Ste6) |
| III: vesicle intermediates | the protein enters an intracellular membrane carrier and reaches the surface by fusion | IL-1β and other leaderless cargo through the TMED10 channel into the ER–Golgi intermediate compartment (the THU pathway, Min Zhang's group, 2020); secretory autophagy; yeast Acb1 |
| IV: Golgi bypass | transmembrane proteins travel from the ER to the plasma membrane without passing the Golgi apparatus | CFTR under ER stress |

In the THU pathway (TMED10-channeled unconventional protein secretion), the cargo is unfolded by HSP90A and translocated into the lumen of the ER–Golgi intermediate compartment through a channel formed by oligomers of the transmembrane protein TMED10, which recognizes a short motif in the cargo; the cargo then follows vesicles to the cell surface. The pathway thus resembles transmembrane transport into the ER, but through a different channel and into a later compartment. Unconventional secretion is particularly important for inflammatory signals, galectins and growth factors released under stress, and its routes are still being mapped.

### 6.8.2. Lipids Move at Membrane Contact Sites

Most membrane lipids are made in the ER, yet their concentrations differ greatly between organelles: cholesterol makes up about $5\,\%$ of the lipid of the ER but $30$–$40\,\%$ of that of the plasma membrane; PS and PI(4)P are enriched in the plasma membrane and the Golgi, cardiolipin in mitochondria. Vesicle traffic cannot account for this, because vesicles carry the composition of their donor and do not reach mitochondria at all; and blocking vesicle traffic slows lipid delivery to the plasma membrane much less than protein delivery. Most lipids move instead without vesicles, carried by lipid transfer proteins at sites where two membranes come very close.

**Definition 6.8.2 (Membrane Contact Site)** A **membrane contact site** is a region where the membranes of two organelles, or of an organelle and the plasma membrane, are held within about $10$–$30\,\mathrm{nm}$ of each other by tethering proteins, without fusing, and exchange lipids, ions or signals; contact sites are characterized by specific tethers and resident proteins.

The ER makes contacts with almost every other membrane.

| Contact | Tethers and transfer proteins | What moves |
|---|---|---|
| ER–plasma membrane | extended synaptotagmins (E-Syts, SMP domains), ORP5 and ORP8, STIM1–Orai1 | glycerolipids; PS from the ER exchanged for PI(4)P from the plasma membrane; $\ce{Ca^2+}$ refilling of the ER (store-operated entry, [7.3.7](/7.3.7)) |
| ER–Golgi (trans-Golgi) | OSBP, CERT, with VAP in the ER | cholesterol exchanged for PI(4)P (OSBP); **ceramide** for sphingomyelin synthesis (CERT) |
| ER–mitochondria | ERMES in yeast (with the SMP-domain proteins Mdm12, Mdm34, Mmm1), PDZD8 and others in mammals | PS to mitochondria (converted to PE), $\ce{Ca^2+}$; sites of mitochondrial division ([7.3.12](/7.3.12)) |
| ER–lipid droplets, ER–endosomes, ER–autophagosomes | seipin; VAP–ORP1L; ATG2 | triacylglycerol and sterol esters; cholesterol; bulk phospholipid for autophagosome growth |

Two modes of transfer have been identified. Shuttle-like proteins with a hydrophobic cavity (OSBP-related proteins, the SMP domains, the START domain of CERT) extract one lipid molecule at a time, carry it across the gap and deposit it. Rod-shaped bridge-like proteins (VPS13 and ATG2) span the gap with a continuous hydrophobic groove along which many lipids slide, a bulk flow that supports the rapid growth of membranes such as autophagosomes.

How can transfer proteins, which only catalyze exchange, create a gradient? OSBP exchanges cholesterol for PI(4)P: it carries cholesterol from the ER to the trans-Golgi and PI(4)P back. PI(4)P is made in the Golgi by a PI 4-kinase, using ATP, and destroyed in the ER by the phosphatase Sac1, so its gradient is kept steep; downhill transport of PI(4)P drives uphill transport of cholesterol, a countertransport analogous to secondary active transport across a membrane ([7.3.5](/7.3.5#sec-5.1.2)), except that the "carrier" moves between two membranes. Phosphoinositide metabolism thus pays for the lipid identity of organelles, and contact sites are as much a part of the cell's logistics as vesicles and translocators.

## Summary

| Topic | Key points |
|---|---|
| Compartments (6.1, Definitions 6.1.1–6.1.2) | Hepatocyte volumes: cytosol $54\,\%$, mitochondria $22\,\%$, ER $14\,\%$; plasma membrane only $2\,\%$ of membrane area; organelles with two, one or no membranes; crowded cytosol (cytoplasmic matrix) with its metabolic, synthetic, ionic, supply, signaling and organizing functions; endomembrane system with lumens topologically equivalent to the exterior; mitochondria and plastids separate; condensates as membraneless compartments (synaptic vesicle clusters, carboxysomes), cleared by autophagy when solid (SEPA-1/EPG-2, CCT2) |
| Size (6.2, Definition 6.2.1, Proposition 6.2.1) | Organelle size scales with cell volume; limiting pool: $S^* = (\rho - c^*)V$, $c^* = k_{\mathrm{off}}/k_{\mathrm{on}}$; centrosomes and spindles in embryos; other mechanisms: balance-point length control, import-limited growth |
| Sorting (6.3, Definitions 6.3.1–6.3.2) | Gated, transmembrane and vesicular transport; the ER decision is made first; signal sequences and patches read by physical character; table of signals; transferable signals |
| ER (6.4, Definitions 6.4.1–6.4.6, Example 6.4.1) | Signal hypothesis (Milstein 1972, Blobel); Sec61αβγ with plug, pore ring and lateral gate; co- vs posttranslational (Sec62/63, BiP ratchet; SecA in bacteria); start- and stop-transfer sequences; type I, II, III, tail-anchored, multipass, GPI-anchored; positive-inside rule; GET (Get3/TRC40, Get1/2) and EMC; GPI transamidase; PNH |
| Mitochondria (6.5, Definitions 6.5.1–6.5.2, Example 6.5.1, Formula 6.5.1) | Presequence: amphipathic, positive, cleaved by MPP; TOM → TIM23 (Tim17 channel) + PAM; TIM22 carriers; SAM β barrels; MIA disulfide relay; Oxa1; energy: cytosolic ATP, $\Delta\psi$ (about $26\,\mathrm{pN}$ on four charges), matrix ATP; DHFR–methotrexate intermediates; ratchet $v = 2D/\delta$ at zero load |
| Chloroplasts (6.6, Definition 6.6.1) | Transit peptide; TOC (Toc75, Toc159, Toc34) and TIC (Tic20, Tic214; Ycf2–FtsHi motor); GTP and ATP, no $\Delta\psi$; bipartite signals; thylakoid cpSec, cpTat (folded, $\Delta\mathrm{pH}$), cpSRP, spontaneous |
| Peroxisomes (6.7, Definitions 6.7.1–6.7.2) | Microbodies of early EM; oxidases and catalase; VLCFA β oxidation, plasmalogens, bile acids, glyoxysomes, photorespiration; PTS1 (SKL, Pex5) and PTS2 (Pex7); folded cargo, export-driven import (ubiquitination, Pex1/Pex6); growth and division or de novo from the ER (Pex3, Pex19); Zellweger syndrome, X-ALD |
| Exceptions (6.8, Definitions 6.8.1–6.8.2) | Unconventional secretion types I–IV (FGF2, IL-1β via gasdermin D or the TMED10 THU pathway, Ste6, CFTR bypass); contact sites at $10$–$30\,\mathrm{nm}$; shuttle and bridge transfer proteins; OSBP countertransport of cholesterol and PI(4)P driven by PI4K and Sac1 |

## Questions

1. A cytosolic protein is fused to (a) an N-terminal ER signal sequence, (b) an N-terminal mitochondrial presequence, (c) a C-terminal SKL, (d) an N-terminal ER signal sequence and a C-terminal KDEL, (e) an ER signal sequence followed by a mitochondrial presequence. Where does each fusion go?

   **Answer** (a) Into the ER lumen and, lacking other signals, by the default pathway through the Golgi apparatus to secretion. (b) Into the mitochondrial matrix, where the presequence is cleaved, provided the protein can be unfolded for import. (c) Into the peroxisomal matrix, even if folded. (d) Into the ER, and retained there by retrieval from the Golgi via the KDEL receptor. (e) Into the ER: the signal sequence is recognized cotranslationally by SRP as soon as it emerges, before the presequence is complete, and the ER decision is taken first; once in the lumen, the protein cannot reach the mitochondrial import machinery.

2. Using Proposition 6.2.1, predict what happens to the size of an organelle (a) after a cell divides symmetrically, (b) in a cell that doubles the expression of the subunit, (c) when there are two such organelles in one cell competing for the pool. Which experiments in embryos test (a) and (c)?

   **Answer** (a) Each daughter receives half the volume and, with constant concentration, half the subunits, so each organelle re-equilibrates at half the size ($S^*$ proportional to $V$): organelles shrink at each cleavage division, as centrosomes and spindles do in early embryos. (b) $\rho$ doubles; $S^* = (2\rho - c^*)V$ more than doubles if $c^*$ is a sizable fraction of $\rho$. (c) Both draw on the same free concentration; the steady state fixes the total $S_1 + S_2 = (\rho - c^*)V$ but not how it is divided, so additional mechanisms (for example size-dependent growth rates) are needed to make them equal. Removing one of two centrosomes in a *C. elegans* embryo and observing that the remaining one grows larger, or varying the volume of droplets of egg extract and measuring spindle length, test the limiting-pool predictions.

3. A type II membrane protein has 8 Arg and Lys in the 20 residues preceding its single hydrophobic segment and 1 in the 20 residues after it. A mutant replaces the N-terminal basic residues with Glu and Asp and adds 6 Lys after the segment. Predict the topology of each, and explain how you would test the prediction with a glycosylation reporter.

   **Answer** Wild type: by the positive-inside rule the N-terminal flank stays in the cytosol, giving a type II orientation (N in, C in the lumen). The mutant reverses the charge difference: the positive C-terminal flank stays in the cytosol and the N-terminus is translocated, giving type III (N in the lumen, C in the cytosol). Test: place an Asn-X-Thr site at the N-terminus and another at the C-terminus (each in a short reporter extension) and measure glycosylation by the shift in gel mobility or by sensitivity to endoglycosidase H: only the end in the lumen is glycosylated. Protease protection of microsomes (only cytosolic parts are digested) gives an independent check.

4. Estimate the velocity of a perfect translocation ratchet with $\delta = 0.35\,\mathrm{nm}$ (one residue of an extended chain) and an effective diffusion coefficient of the chain in the channel of $D = 10^{-13}\,\mathrm{m^2\,s^{-1}}$. How many residues per second is that? Measured import rates of unfolded precursors are of the order of tens to hundreds of residues per second. What do you conclude? At what load does the ratchet slow down to one tenth of its free velocity?

   **Answer** $v = 2D/\delta = 2\times10^{-13}/(3.5\times10^{-10})\,\mathrm{m\,s^{-1}} \approx 5.7\times10^{-4}\,\mathrm{m\,s^{-1}}$, about $1.6\times10^6$ residues per second, if the chaperone binds instantly after each residue. Even if $D$ were a hundred times smaller, diffusion would not limit import; the observed rates are set by other steps, the binding rate of the chaperone (which needs several residues to bind), the unfolding of domains outside, and friction in the channel. The velocity falls to $0.1 \times 2D/\delta$ when $(\omega^2/2)/(\mathrm{e}^\omega - 1 - \omega) = 0.1$, at $\omega \approx 4.5$ (figure in 6.5.3), so at $f \approx 4.5\,k_{\mathrm{B}}T/\delta = 4.5 \times 4.3\,\mathrm{pN\,nm}/0.35\,\mathrm{nm} \approx 55\,\mathrm{pN}$; a folded domain requiring a larger unfolding force will hold up a pure ratchet.

5. Cells from a patient with suspected Zellweger syndrome are stained with antibodies against catalase and against the peroxisomal membrane protein PMP70. (a) What pattern do you expect in normal cells and in the patient's cells? (b) How could you find which *PEX* gene is defective, using cell fusion? (c) Why does the patient lack plasmalogens but have normal levels of most mitochondrial enzymes?

   **Answer** (a) In normal cells both antibodies give the same punctate pattern of peroxisomes. In the patient's cells PMP70 still marks punctate membrane ghosts (membrane protein import uses Pex19 and Pex3, often intact), but catalase is diffuse in the cytosol because matrix import (Pex5, docking, recycling) has failed. (b) By complementation: fuse the patient's cells with cells of known complementation groups (or transfect individual *PEX* cDNAs); restoration of punctate catalase in the hybrid or transfected cells identifies the gene that is mutated (cells with mutations in the same gene do not complement). (c) The first steps of plasmalogen synthesis are catalyzed by peroxisomal matrix enzymes, which are mislocalized and degraded; mitochondria import their proteins by entirely separate machinery (TOM, TIM), which is unaffected, although secondary defects can arise from accumulated lipids.

6. (Open) Using the OSBP cycle as a model, explain how a lipid transfer protein that only exchanges two lipids can maintain a cholesterol gradient between the ER and the Golgi, what provides the energy, and what would happen to the gradient if Sac1 were inhibited.

   **Answer** OSBP binds either cholesterol or PI(4)P in the same pocket and exchanges them: it extracts cholesterol from the ER and PI(4)P from the Golgi, and delivers each to the other membrane. If PI(4)P is kept high in the Golgi (made by a PI 4-kinase using ATP) and near zero in the ER (hydrolyzed by Sac1), PI(4)P flows down its gradient from Golgi to ER, and each round carries one cholesterol from ER to Golgi, even against the cholesterol gradient: the free energy comes from ATP spent on PI(4)P synthesis and released by its hydrolysis. This is countertransport, like an antiporter driven by an ion gradient. If Sac1 is inhibited, PI(4)P accumulates in the ER, the PI(4)P gradient collapses, the exchange reverses or becomes equal in both directions, and cholesterol is no longer concentrated in the Golgi and plasma membrane; in cells, Sac1 depletion indeed disturbs sterol distribution and Golgi function.
