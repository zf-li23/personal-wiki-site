---
title: "Working with Proteins: Purification, Analysis, and Sequencing"
description: How proteins are purified by exploiting differences in solubility, size, charge and binding affinity; assays, specific activity and the purification table; SDS-PAGE, isoelectric focusing and two-dimensional electrophoresis; determining primary structure by Edman degradation, specific cleavage and mass spectrometry; consensus sequences, homologs, orthologs and paralogs, and protein sequences as a record of evolution.
---

To understand a protein, one must first isolate it from the thousands of other proteins in a cell, and then determine what it is made of and in what order. Every technique for doing so exploits a chemical or physical property that distinguishes one protein from another: its solubility, its size, its net charge at a given pH (7.1.3), its affinity for a particular ligand, its mass. This chapter is therefore an application of the previous one: the properties of amino acid side chains become handles for separation and analysis. It covers separation and purification (4.1), electrophoresis (4.2), the determination of primary structure (4.3), and what amino acid sequences reveal about structure, function and evolution (4.4).

The analytical principles are treated in the chemistry courses: **chromatography** and its theory (resolution, plate height) in [6.4.13](/6.4.13), liquid chromatography and electrophoresis of biomolecules in [6.4.14](/6.4.14), **mass spectrometry** and proteomics in [6.4.15](/6.4.15), the chemistry of Edman degradation and of solid-phase peptide synthesis in [6.5.33](/6.5.33). Here we ask which property of a protein each method uses, and how the methods are combined.

## 4.1. Separating and Purifying Proteins

### 4.1.1. The Strategy: From Crude Extract to Pure Protein

A pure preparation is essential before a protein's properties and activities can be determined. The source is a tissue or a microbial culture, and the first step is to break open the cells (by homogenization, sonication, detergents or osmotic shock), releasing their contents into a solution called a *crude extract*. If the protein is inside an organelle, the organelles are first separated by centrifugation in isotonic sucrose, so that they do not burst (7.1.2).

**Definition 4.1.1** The separation of the components of a cell homogenate by successive centrifugations at increasing speed, each step sedimenting the larger and denser particles that remain in the supernatant of the previous step, is called **differential centrifugation**.

| Centrifugation | Pellet contains |
|---|---|
| $1000\,g$, 10 min | unbroken cells, nuclei, cytoskeleton |
| $20\,000\,g$, 20 min | mitochondria, lysosomes, peroxisomes, chloroplasts |
| $80\,000\,g$, 1 h | microsomes (fragments of plasma membrane and endoplasmic reticulum) |
| $150\,000\,g$, 3 h | ribosomes, large macromolecular complexes |

The final supernatant is the soluble cytosol. Fractions can be resolved further by **ultracentrifugation** through a density gradient ([6.3.21](/6.3.21#sec-21.3.4)), in which particles band at their own buoyant density (isopycnic centrifugation) or separate by sedimentation rate.

Today the source of a protein is usually not its native tissue but a cell engineered to overproduce it from a cloned gene, often with a short peptide *tag* added to one end for affinity purification ([7.2](/7.2)). The principles of purification are the same in both cases.

### 4.1.2. Which Property to Exploit

| Property | Method | Principle |
|---|---|---|
| solubility | salting out, isoelectric precipitation | solubility depends on ionic strength and on net charge |
| size | dialysis, ultrafiltration | small molecules pass a membrane, proteins do not |
| | size-exclusion chromatography | large molecules are excluded from the pores of the beads and elute first |
| | SDS-PAGE (analytical) | migration of SDS–protein complexes through a gel sieve depends on chain length |
| charge | ion-exchange chromatography | binding to a charged matrix depends on the sign and magnitude of the net charge |
| | isoelectric focusing (analytical) | migration in a pH gradient stops at the pI |
| binding affinity | affinity chromatography | specific binding to an immobilized ligand |
| hydrophobicity | hydrophobic-interaction and reversed-phase chromatography | binding of exposed nonpolar patches to a nonpolar matrix |

A good purification combines methods that rely on different properties, because two proteins that are similar in one property are unlikely to be similar in all of them.

### 4.1.3. Salting Out and Dialysis

The solubility of a protein depends on its interactions with water and with other proteins. At low ionic strength, adding salt increases solubility (*salting in*): the ions screen the attractive electrostatic interactions between protein molecules. At high salt concentrations the salt competes with the protein for water, and the protein aggregates and precipitates.

**Definition 4.1.2** The selective precipitation of proteins from solution by high concentrations of a salt is called **salting out**.

Different proteins precipitate at different salt concentrations, so a protein can be enriched by collecting the precipitate formed between two concentrations (for example between 40 % and 60 % saturation). Ammonium sulfate is the salt of choice: it is very soluble (saturated at about 4 M), it stabilizes rather than denatures most proteins, the precipitate redissolves readily, and it is cheap. The salt is then removed, or the buffer exchanged, by **dialysis** ([6.3.21](/6.3.21#sec-21.2.2)): the protein solution is placed in a bag of semipermeable membrane in a large volume of buffer, and small molecules equilibrate across the membrane while proteins are retained. Proteins are also least soluble at their isoelectric point, where there is no net charge to repel neighbouring molecules (isoelectric precipitation).

### 4.1.4. Column Chromatography

In column chromatography a solution of proteins (the mobile phase) flows through a column packed with a porous solid material (the stationary phase); proteins that interact more strongly with the stationary phase are retarded more and emerge, are *eluted*, later. Longer columns and smaller particles improve the separation but slow the flow and dilute the protein ([6.4.13](/6.4.13)). Three kinds of matrix dominate protein work.

**Ion-exchange chromatography** separates proteins by the sign and magnitude of their net charge at the pH of the buffer ([6.4.14](/6.4.14#sec-14.2)). A cation exchanger carries negatively charged groups, such as carboxymethyl (CM, $\ce{-CH2COO-}$) or sulfonate (S) groups, and binds positively charged proteins; an anion exchanger carries positively charged groups, such as diethylaminoethyl (DEAE, $\ce{-CH2CH2NH(C2H5)2+}$) or quaternary ammonium (Q) groups, and binds negatively charged proteins. The rule follows from the net charge $Z(\mathrm{pH})$ computed in 7.1.3: above its pI a protein is negative and binds an anion exchanger, below its pI it is positive and binds a cation exchanger. Bound proteins are eluted with a gradient of increasing salt concentration (the salt ions compete for the charged groups), or by changing the pH; those with the smallest net charge come off first.

![Choosing an ion exchanger. Net charge computed from the numbers of ionizable groups and typical pKa values for hen lysozyme (pI about 10.9; measured 11.3) and for a hypothetical acidic protein (pI about 4.3). At pH 7.5 lysozyme carries a charge of about +8 and binds a cation exchanger (CM or S), whereas the acidic protein carries about −16 and binds an anion exchanger (DEAE or Q); a mixture of the two is separated in one step](./plots/ion-exchange-charge.py)

**Size-exclusion chromatography** (gel filtration) uses beads with pores of a defined size. Large proteins cannot enter the pores and pass through the column quickly, in the volume between the beads; small proteins enter the pores and take a longer path. Proteins therefore elute in order of decreasing size, and for globular proteins the elution volume is approximately linear in $\lg M$ over the working range of the gel, so a column calibrated with standards gives the molecular mass of a native protein or complex ([6.4.14](/6.4.14#sec-14.2)).

**Affinity chromatography** uses a ligand covalently attached to the beads that binds the protein of interest specifically: a substrate analogue for an enzyme, an antibody for its antigen, a hormone for its receptor. All other proteins wash through, and the bound protein is eluted with a solution of free ligand or by conditions that weaken binding. Engineered tags make the method general: a run of six His residues (His₆ tag) binds to $\ce{Ni^2+}$ immobilized on nitrilotriacetic acid beads and is eluted with imidazole, which competes for the metal; glutathione S-transferase fusions bind glutathione beads. A single affinity step can purify a protein a thousandfold.

Each of these separations can be run as **high-performance liquid chromatography** (HPLC), with small, uniform, pressure-resistant particles and high-pressure pumps, which gives faster and better-resolved separations.

### 4.1.5. Assays and Specific Activity

To follow a protein through a purification, one needs an assay: a specific measurement of its presence or activity in each fraction. For an enzyme the assay measures the rate of the reaction it catalyses under defined conditions. Lactate dehydrogenase, for example, oxidizes lactate with $\ce{NAD+}$; the product NADH absorbs at 340 nm ($\varepsilon_{340} = 6220\,\mathrm{L\,mol^{-1}\,cm^{-1}}$) and $\ce{NAD+}$ does not, so the rate of increase in $A_{340}$ measures the enzyme's activity (**Beer–Lambert law**). The more specific the assay, the more effective the purification. For proteins without catalytic activity the assay may detect binding, an immunological reaction (7.1.7) or a tag.

**Definition 4.1.3** The amount of an enzyme that catalyses the transformation of $1\,\mu\mathrm{mol}$ of substrate per minute under defined conditions (temperature, pH, substrate concentration) is one *unit* (U) of activity; the SI unit is the katal, $1\,\mathrm{kat} = 1\,\mathrm{mol\,s^{-1}} = 6 \times 10^{7}\,\mathrm{U}$. The activity of a solution is the total number of units it contains. The number of units per milligram of total protein is the **specific activity**.

Specific activity is a measure of purity: it rises as contaminating proteins are removed and is constant once the protein is pure. A purification is summarized in a purification table.

**Example 4.1.1** A hypothetical purification of an enzyme from 1 kg of tissue:

| Step | Total protein / mg | Activity / U | Specific activity / (U mg⁻¹) | Yield / % | Purification / fold |
|---|---|---|---|---|---|
| 1. crude extract | 12 000 | 240 000 | 20 | 100 | 1 |
| 2. ammonium sulfate, 40–60 % | 3 600 | 216 000 | 60 | 90 | 3 |
| 3. anion exchange (DEAE) | 480 | 168 000 | 350 | 70 | 17.5 |
| 4. size exclusion | 120 | 132 000 | 1 100 | 55 | 55 |
| 5. affinity | 4.0 | 96 000 | 24 000 | 40 | 1 200 |

The yield (activity remaining relative to the crude extract) falls at every step, because some protein is always lost; the purification factor (specific activity relative to the crude extract) rises. Two conclusions follow. The enzyme made up about 1/1200 of the total protein of the extract (if step 5 gave a pure enzyme, which SDS-PAGE would confirm, 4.2.1). And the ideal step, here the affinity column, gives the largest increase in specific activity with the smallest loss in yield; many purifications are designed around one such step.

![Progress of the purification of Example 4.1.1. (A) Specific activity (log scale) after each step: 20, 60, 350, 1100 and 24 000 U mg⁻¹. (B) Yield of activity falls from 100 % to 40 % while the purification factor rises 1200-fold, most of it in the final affinity step](./plots/purification-progress.py)

## 4.2. Electrophoresis

### 4.2.1. SDS-PAGE

**Electrophoresis**, the migration of charged molecules in an electric field ([6.3.21](/6.3.21#sec-21.5)), is the standard analytical method for proteins: it separates and visualizes them in one step, needs only micrograms of material, and reveals the number of proteins in a sample and their sizes. It is usually done in a gel of cross-linked polyacrylamide, which acts as a molecular sieve. In a gel, the migration of a native protein depends on both its charge and its size and shape. The detergent sodium dodecyl sulfate (SDS) removes the dependence on charge and shape: it binds to most proteins in proportion to their mass (about 1.4 g SDS per gram of protein, roughly one SDS molecule per two residues), unfolds them, and coats them with so much negative charge that their own charge becomes negligible. All SDS–protein complexes then have about the same charge-to-mass ratio and a similar rod-like shape, and they migrate through the gel according to chain length alone, small proteins fastest.

In **SDS-PAGE** (SDS–polyacrylamide gel electrophoresis) the sample is usually heated with SDS and a reducing agent (2-mercaptoethanol or dithiothreitol), so that disulfide-linked chains also separate. After the run the proteins are stained (Coomassie blue detects about 0.1 µg per band, silver staining about 1 ng) or transferred to a membrane and detected with antibodies (Western blotting, 7.1.7). Over the useful range of a gel, the logarithm of $M_{\mathrm{r}}$ is approximately linear in the relative mobility, so a lane of standard proteins calibrates the gel and the $M_{\mathrm{r}}$ of an unknown polypeptide can be read off with an uncertainty of about 5–10 % ([6.4.14](/6.4.14#sec-14.5), calibration example there). The method gives the mass of the *subunits*; comparing it with the native mass from size-exclusion chromatography reveals the number of subunits. In a purification, successive samples run side by side show the band of the protein of interest becoming dominant as the others disappear.

### 4.2.2. Isoelectric Focusing and Two-Dimensional Electrophoresis

**Isoelectric focusing** separates proteins by their pI. A pH gradient is established in a gel by a mixture of small amphoteric compounds (ampholytes) or by immobilized buffering groups; a protein migrates until it reaches the position where the pH equals its pI, where it has no net charge and stops. Proteins that differ in pI by as little as 0.01 units can be separated.

Combining isoelectric focusing in one direction with SDS-PAGE at right angles gives **two-dimensional electrophoresis** (O'Farrell, 1975), which separates proteins by two independent properties, pI and mass, and can resolve more than a thousand different proteins of a cell extract on one gel as a pattern of spots. Spots that change with conditions can be cut out and identified by mass spectrometry. Two-dimensional gels were the first tool of **proteomics**, the large-scale study of all the proteins of a cell; they have largely been replaced by liquid chromatography coupled to mass spectrometry (4.3.4), but remain useful for detecting modified forms of a protein, which differ in pI.

## 4.3. Determining the Primary Structure

**Definition 4.3.1** The amino acid sequence of a polypeptide chain, together with the positions of any disulfide bonds, is its **primary structure**.

### 4.3.1. Why Sequences Matter

Frederick Sanger's determination of the sequence of insulin (completed in 1955) showed for the first time that a protein has a precisely defined amino acid sequence, and that this sequence is the same in every molecule. Sequences are now the most basic information about any protein. They determine how the chain folds (7.1.5–7.1.6) and hence what it does; they reveal related proteins and their common ancestors (4.4); they contain signals for location (signal sequences for secretion, transmembrane segments, 7.1.13) and modification (glycosylation and phosphorylation motifs); and they explain disease: in sickle-cell anemia a single change, Glu → Val at position 6 of the β chain of hemoglobin, is enough to alter the behaviour of the whole protein (7.1.7).

Three approaches have been used to determine sequences: direct chemical sequencing of the polypeptide, mass spectrometry, and translation of the DNA sequence of its gene. The first is now used mainly for N-terminal confirmation, the second is the method of choice for the protein itself, and the third gives the great majority of known sequences.

### 4.3.2. Terminal Residues and Edman Degradation

The first step is to determine the amino acid composition (by acid hydrolysis, 6 M HCl at $110\,^\circ\mathrm{C}$ for 24 h, followed by chromatography; Trp is destroyed and Asn and Gln are converted to Asp and Glu, so they are determined separately) and to identify the terminal residues. Sanger labelled the free α-amino group of the N-terminal residue with 1-fluoro-2,4-dinitrobenzene (FDNB); after complete hydrolysis, only the N-terminal amino acid carries the yellow dinitrophenyl label. Dansyl chloride, a fluorescent reagent, does the same with greater sensitivity. Both methods destroy the rest of the chain.

**Edman degradation** ([6.5.33](/6.5.33#sec-33.6.2)) removes one residue at a time from the N-terminus and leaves the rest of the peptide intact. In each cycle the reagent phenyl isothiocyanate (PITC) reacts with the free α-amino group; under anhydrous acid the derivatized N-terminal residue is cleaved off as a cyclic derivative, which is converted to a stable phenylthiohydantoin (PTH) amino acid and identified by chromatography; the shortened peptide is ready for the next cycle. (PITC is the reagent; PTH is the product that is identified.) Automated sequenators perform the cycles in sequence.

The length that can be read is limited by the efficiency of each cycle. If a fraction $p$ of the chains is correctly degraded in each cycle, after $n$ cycles only $p^n$ of the chains are still in phase, while the others give a growing background of residues out of register:

$$
p = 0.95:\ 0.95^{50} = 0.077; \qquad p = 0.99:\ 0.99^{50} = 0.61.
$$
Practical reads are therefore limited to about 30–50 residues, and a protein must first be cut into fragments of this size.

### 4.3.3. Breaking Disulfides and Cutting the Chain

Before a protein is fragmented, its disulfide bonds are broken, both to separate disulfide-linked chains and to prevent fragments from staying joined. Two methods are used: oxidation with performic acid, which converts each cystine into two cysteic acid residues; or reduction with dithiothreitol or 2-mercaptoethanol, followed by alkylation of the free thiols with iodoacetate (giving carboxymethylcysteine) so that the disulfides cannot re-form. The positions of the disulfide bonds are determined in a separate experiment, by cleaving the protein without breaking them and identifying the linked fragments.

The polypeptide is then cleaved with reagents of known specificity:

| Reagent | Cleaves | Notes |
|---|---|---|
| trypsin | C-terminal side of Lys and Arg | not before Pro |
| chymotrypsin | C-terminal side of Phe, Trp and Tyr | not before Pro; slower after Leu, Met |
| endoproteinase Lys-C | C-terminal side of Lys | not before Pro |
| endoproteinase Glu-C (*Staphylococcus aureus* V8 protease) | C-terminal side of Glu (and Asp in phosphate buffer) | |
| endoproteinase Asp-N | N-terminal side of Asp | |
| pepsin | N-terminal side of Leu, Phe, Trp and Tyr | active at acidic pH; less specific |
| cyanogen bromide (CNBr) | C-terminal side of Met | chemical; Met becomes homoserine lactone ([6.5.33](/6.5.33#sec-33.6.1)) |

The fragments from one digest are separated, for instance by HPLC, and each is sequenced. To put them in order, a second sample of the protein is cleaved with a reagent of different specificity; the fragments of the second digest overlap the cleavage sites of the first and so connect its fragments.

![Ordering fragments by overlaps for a hypothetical 24-residue polypeptide. Trypsin cuts after Lys and Arg (dashed lines), giving fragments T1–T5; cyanogen bromide cuts after Met (dotted lines), giving C1–C3. Each CNBr fragment spans one or more trypsin cleavage sites: C1 (GAVLKM) joins T1 to the Met that begins T2, C2 joins T2, T3 and the beginning of T4, and C3 joins the end of T4 to T5. Together with the N-terminal (Gly) and C-terminal (Cys) residues, the overlaps fix the order T1–T2–T3–T4–T5](./plots/sequencing-overlap.py)

**Example 4.3.1** The trypsin fragments of the polypeptide in the figure, in an unknown order, are GC, GAVLK, MSDYR, TMEHLR and WFNPQK; the CNBr fragments are EHLRGC, GAVLKM and SDYRWFNPQKTM. The N-terminal residue is Gly and the C-terminal residue Cys. GAVLKM shows that GAVLK is followed by a fragment beginning with M, namely MSDYR; SDYRWFNPQKTM shows that MSDYR is followed by WFNPQK and then by a fragment beginning with TM, namely TMEHLR; EHLRGC places GC last. The sequence is GAVLKMSDYRWFNPQKTMEHLRGC. Note that the trypsin fragment WFNPQK is not cut before Pro, and that the two fragments beginning with Gly can be distinguished only by the CNBr overlaps.

### 4.3.4. Mass Spectrometry

**Mass spectrometry** measures the mass-to-charge ratio $m/z$ of gas-phase ions with an accuracy of a few parts per million, and it has become the principal method for analysing proteins ([6.4.15](/6.4.15)). Two soft ionization methods bring intact proteins and peptides into the gas phase without fragmenting them: **matrix-assisted laser desorption/ionization** (MALDI), which gives mostly singly charged ions, and **electrospray ionization** (ESI), which sprays a solution from a charged capillary and gives a series of multiply protonated ions $[\mathrm{M} + z\mathrm{H}]^{z+}$ at

$$
\frac{m}{z} = \frac{M + z\,m_{\mathrm{H}}}{z}, \qquad m_{\mathrm{H}} = 1.007\,\mathrm{Da}.
$$
Two neighbouring peaks of the series, $m_1$ (charge $z$) and $m_2 < m_1$ (charge $z + 1$), determine both the charge and the mass: $z = (m_2 - m_{\mathrm{H}})/(m_1 - m_2)$ and $M = z(m_1 - m_{\mathrm{H}})$.

**Example 4.3.2** The ESI spectrum of apomyoglobin contains neighbouring peaks at $m/z = 1131.11$ and $1060.48$. Then $z = (1060.48 - 1.007)/(1131.11 - 1060.48) = 15.0$ for the first peak, and $M = 15 \times (1131.11 - 1.007) = 16\,951.5\,\mathrm{Da}$, the mass of horse-heart apomyoglobin. With a mass accuracy of 1–2 Da, a modification such as a single phosphorylation (+80 Da) or a missing residue is immediately detected.

Mass spectrometry also sequences peptides. In **tandem mass spectrometry** (MS/MS) one peptide ion is selected, fragmented by collisions with an inert gas, mainly at its peptide bonds, and the masses of the fragments are measured. Fragments containing the N-terminus (b ions) and the C-terminus (y ions) form two ladders whose successive differences are the masses of the residues, so the sequence can be read directly; only Leu and Ile (identical mass) and, at low resolution, Gln and Lys (128.059 and 128.095 Da) are hard to distinguish. In practice the protein mixture is digested with trypsin, the peptides are separated by HPLC and passed directly into the mass spectrometer, and the measured spectra are matched against the spectra predicted for all tryptic peptides of the organism's genome-encoded proteins. This "bottom-up" or "shotgun" approach, together with **peptide mass fingerprinting**, identifies thousands of proteins and their modifications in one experiment and is the workhorse of proteomics.

### 4.3.5. Sequences from Genes, and Peptides by Synthesis

Since about 1980 most protein sequences have been deduced from the nucleotide sequences of genes or of complementary DNAs, using the genetic code: sequencing DNA is faster and cheaper than sequencing protein ([7.2](/7.2)). With the genome sequences of tens of thousands of organisms, essentially every protein sequence of these organisms is "known" before the protein has ever been isolated. Protein chemistry remains indispensable, however, because the gene does not show which parts of the chain are removed (signal peptides, propeptides), how it is modified (phosphorylation, glycosylation, disulfides), which of several alternatively spliced forms is made, or whether the predicted reading frame is correct. A short stretch of protein sequence, conversely, can be used to design DNA probes to find the gene.

Peptides can also be made chemically. In solid-phase peptide synthesis (Merrifield, 1962; [6.5.33](/6.5.33#sec-33.7.6)) the C-terminal residue is attached to an insoluble resin, and the chain is built towards the N-terminus by repeated cycles of deprotection of the α-amino group (Fmoc removal) and coupling of the next protected amino acid; synthesis thus proceeds C → N, opposite to biosynthesis on the ribosome (N → C). Because each cycle is incomplete, the yield of full-length product falls as $p^{n-1}$, as in Edman degradation, and direct synthesis is practical up to about 50–100 residues; longer chains are assembled by ligating synthetic fragments (native chemical ligation). Synthetic peptides are used as hormones and drugs (oxytocin, vasopressin), as antigens to raise antibodies, and to incorporate unnatural amino acids or labels at defined positions.

## 4.4. Amino Acid Sequences and Evolution

### 4.4.1. Homologous Proteins

Protein sequences change over evolutionary time by mutation and selection (7.1.1), but the changes are constrained: residues that are essential for structure or function are conserved, others vary. Comparing the sequences of a protein from different organisms, or of related proteins in one organism, therefore reveals both their history and the parts that matter.

**Definition 4.4.1** Proteins (or genes) that descend from a common ancestral sequence are **homologs**. Homologs found in different species, which arose from the ancestral sequence by speciation, are **orthologs**; homologs that arose by duplication of a gene within a genome are **paralogs**.

Homology is a statement about ancestry and is therefore either true or false; it is *inferred* from sequence similarity that is too great to be due to chance. For proteins more than about 100 residues long, more than 30 % identical residues in an alignment usually means homology; between 20 % and 30 % (the "twilight zone") the inference requires statistical tests or structural evidence, because the three-dimensional fold is conserved much longer than the sequence (7.1.5). Orthologs usually have the same function in different species (human and yeast cytochrome *c*); paralogs often have diverged in function (the α and β chains of hemoglobin, myoglobin; trypsin, chymotrypsin and elastase, 7.1.8). Homologs therefore do not necessarily have the same function, and similar function does not imply homology (convergent evolution, such as the serine proteases chymotrypsin and subtilisin, which have the same catalytic triad on unrelated folds).

### 4.4.2. Consensus Sequences and Signature Sequences

**Definition 4.4.2** For a set of aligned homologous sequences, the sequence formed by the residue that occurs most often at each position is the **consensus sequence**.

Consensus sequences are written with conventions for positions that vary: x for any residue, alternatives in brackets ([S/T]). A *sequence logo* displays the same information quantitatively: at each position the letters are stacked with heights proportional to their frequencies, and the height of the whole stack is the information content of the position, $R = \log_2 20 - H$ bits, where $H = -\sum_a p_a \log_2 p_a$ is the Shannon entropy of the residue distribution ($\log_2 20 = 4.32$ bits for a perfectly conserved position; details in [7.8](/7.8)).

![The P-loop (Walker A motif), a consensus sequence shared by many unrelated NTP-binding protein families: an alignment of twelve proteins (small GTPases, G proteins, translation and recombination factors, ATP synthase, motor proteins, ABC transporters) and its sequence logo. The conserved Gly at positions 1 and 6, Lys at 7 and Ser/Thr at 8 wrap around the phosphate groups of the bound nucleotide (consensus G-x-x-x-x-G-K-[S/T]); the intervening positions vary freely](./plots/walker-a-logo.py)

Conserved positions point to residues essential for structure or function. In the P-loop above, the backbone amides of the glycine-rich loop and the side chain of the Lys bind the β- and γ-phosphates of ATP or GTP; the motif identifies nucleotide-binding sites in proteins of unknown function. A *signature sequence* is a segment of sequence characteristic of a whole group of organisms. In the elongation factors EF-Tu of bacteria and EF-1α of archaea and eukaryotes, for example, a short insertion of about a dozen residues is present in all archaeal and eukaryotic sequences and absent from all bacterial ones; such indels are strong markers of evolutionary relationships because they are rare and unlikely to arise twice.

### 4.4.3. Aligning Sequences

Comparing sequences requires aligning them: placing them in register so that homologous residues lie in the same column. Insertions and deletions in one lineage are accommodated by introducing gaps. An alignment is scored by adding the scores of the aligned pairs of residues, taken from a substitution matrix (such as BLOSUM62) that rewards identities and conservative substitutions between similar residues (I/L/V, D/E, K/R, F/Y; the property map of 7.1.3) more than replacements of unlike residues, and by subtracting a penalty for each gap. Algorithms find the best-scoring alignment (dynamic programming), and database searches such as BLAST, run at the National Center for Biotechnology Information (www.ncbi.nlm.nih.gov), find similar sequences among hundreds of millions in seconds and report the probability that a match is due to chance. These methods belong to [Bioinformatics](/7.8).

### 4.4.4. Protein Sequences as a Record of Evolution

Sequence differences accumulate over time. For a given protein family the number of substitutions between two species increases roughly in proportion to the time since they diverged, at a rate characteristic of the protein (slow for histones and cytochrome *c*, fast for fibrinopeptides): this *molecular clock*, first recognized by Zuckerkandl and Pauling (1962) from hemoglobin sequences, allows divergence times to be estimated. Trees built from the sequences of one protein family, such as the chaperonin GroEL in bacteria, reconstruct the history of the organisms carrying them; trees from many concatenated protein sequences and other genomic characters give a consensus tree of life. The picture is complicated by horizontal gene transfer, which is frequent among bacteria and archaea, so that different genes of one organism can tell different histories. Molecular phylogenetics is treated in [Evolutionary Biology](/7.10).

## Summary

| Method | Property exploited | What it gives |
|---|---|---|
| differential centrifugation (Definition 4.1.1) | size and density of particles | subcellular fractions |
| salting out (Definition 4.1.2), isoelectric precipitation | solubility | crude enrichment, concentration |
| dialysis, ultrafiltration | size (small vs large molecules) | buffer exchange, removal of salt |
| ion-exchange chromatography | net charge at the buffer pH ($Z(\mathrm{pH})$, pI) | high-capacity separation; anion exchanger above pI, cation exchanger below |
| size-exclusion chromatography | size of the native protein | native $M$, oligomeric state |
| affinity chromatography | specific binding | large purification in one step; tags |
| assay, specific activity (Definition 4.1.3) | biological activity | purity, yield, purification factor |
| SDS-PAGE | chain length (SDS masks charge and shape) | subunit $M_{\mathrm{r}}$, purity |
| isoelectric focusing, 2D electrophoresis | pI; pI and mass | charge variants; proteome maps |
| Edman degradation, specific cleavage, overlaps | sequential chemistry; cleavage specificity | primary structure (Definition 4.3.1), about 50 residues per run |
| mass spectrometry (ESI, MALDI, MS/MS) | mass-to-charge ratio | exact mass, sequence, modifications; proteomics |
| alignment, consensus, logos (Definition 4.4.2) | sequence similarity | homologs, orthologs, paralogs (Definition 4.4.1); conserved residues; evolution |

Key numbers: about 1.4 g SDS per gram of protein; $\lg M_{\mathrm{r}}$ linear in mobility (±5–10 %); Edman $p^n$ ($0.95^{50} = 0.08$); ESI $m/z = (M + z \times 1.007)/z$; homology likely above 30 % identity over 100 residues.

## Questions

1. A mixture contains three proteins: A ($M_{\mathrm{r}} = 15\,000$, pI 10.5), B ($M_{\mathrm{r}} = 60\,000$, pI 5.0) and C ($M_{\mathrm{r}} = 62\,000$, pI 6.5). Propose a two-step purification of each, giving the type of column and the pH.

   **Answer** Size-exclusion chromatography separates A (small, elutes last) from B and C (similar sizes, elute together). B and C are then separated by ion exchange: at pH 7.5 both are negative, but B (pI 5.0) is more negative and binds a DEAE column more tightly, eluting later in a salt gradient; alternatively, at pH 5.8 C is still positive and binds a CM column, while B is negative and passes through. A could also be isolated in one step on a cation exchanger at pH 8, where it is the only positive protein.

2. In the purification of Example 4.1.1, an additional hydrophobic-interaction step after step 4 gives 60 mg of protein with 110 000 U. Calculate its specific activity, yield and purification factor. Is the step worth including?

   **Answer** Specific activity $110\,000/60 = 1833\,\mathrm{U\,mg^{-1}}$; yield $110\,000/240\,000 = 46\,\%$; purification $1833/20 = 92$-fold (1.7-fold over step 4). The step removes half of the remaining protein but loses 17 % of the activity; it is worth including only if the affinity step alone does not give a pure product, since each step costs yield and time.

3. An ESI spectrum shows neighbouring peaks at $m/z = 1428.9$ and $1319.1$. Determine the charge states and the mass of the protein.

   **Answer** $z = (1319.1 - 1.007)/(1428.9 - 1319.1) = 1318.1/109.8 = 12.0$ for the peak at 1428.9 (and 13 for 1319.1). $M = 12 \times (1428.9 - 1.007) = 17\,135\,\mathrm{Da}$; the other peak gives the same value, $13 \times (1319.1 - 1.007) = 17\,135\,\mathrm{Da}$.

4. Trypsin cleaves a decapeptide into DFR and GMLYASK; chymotrypsin cleaves it into ASKDF, GMLY and R. One cycle of Edman degradation of the intact peptide releases PTH-Gly. What is the sequence, and what would cyanogen bromide give?

   **Answer** Gly is N-terminal, so the tryptic fragment GMLYASK comes first and DFR, which ends in Arg, last: GMLYASKDFR. The chymotryptic fragments confirm it: cleavage after Tyr and Phe gives GMLY, ASKDF and R, and ASKDF spans the junction between the two tryptic fragments. Cyanogen bromide would cleave after Met, giving GM (with the Met converted to homoserine lactone) and LYASKDFR.

5. Human and chimpanzee cytochrome *c* are identical; human and yeast cytochromes *c* differ at about 45 of 104 positions, yet the yeast protein functions in human mitochondria in vitro. What does this say about which residues matter, and are the two proteins orthologs or paralogs?

   **Answer** About 60 % of the positions are conserved over the roughly one billion years since animals and fungi diverged; these residues (the Cys and His that bind the heme, the Met ligand of the iron, the Lys residues that bind cytochrome *c* oxidase and reductase, the Gly and Pro of the fold) are essential, while the others tolerate substitution without loss of function. Human and yeast cytochromes *c* are orthologs: they descend from the cytochrome *c* of the common ancestor by speciation and perform the same function.
