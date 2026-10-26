---
title: Amino Acids and Peptides
description: The common structure and L configuration of amino acids; the 20 standard amino acids classified by their R groups, with a complete property table, structures, side-chain functions and memory aids; UV absorption; uncommon amino acids and post-translational modifications; acid–base behaviour, pKa shifts, isoelectric points and net charge; peptides, biologically active peptides, protein sizes, conjugated proteins and cofactors.
---

Proteins are the most abundant **macromolecules** of all cells and the main agents of biological function: they catalyse reactions (hexokinase, **DNA polymerase**), transport molecules (hemoglobin, lactose permease), form structures (**collagen**, keratin), generate movement (myosin, actin), and they receive, transmit and decode signals. All of this diversity is built from one simple set of 20 amino acids. Each has the same backbone and a different side chain, and the side chains differ in size, shape, charge, hydrogen-bonding capacity, hydrophobic character and chemical reactivity. This chapter is the heart of the thread "chemical properties → structure → function" (7.1.1): what each side chain can do chemically determines how proteins fold (7.1.5–7.1.6), bind **ligands** (7.1.7) and catalyse reactions (7.1.8–7.1.9).

The organic chemistry of amino acids, their configurations, acid–base equilibria, reactions and chemical synthesis, and the chemistry of the **peptide bond** have been treated in [6.5.33](/6.5.33) (where **amino acid**, **zwitterion**, **isoelectric point** and **peptide bond** are defined), and the titration of amino acids in [6.4.2](/6.4.2#sec-2.8.3); here we use those results. Methods for purifying proteins and determining their sequences follow in 7.1.4.

## 3.1. Common Structural Features of Amino Acids

### 3.1.1. The α Carbon and the Side Chain

The amino acids of proteins are α-amino acids: a carboxyl group and an amino group are bonded to the same carbon atom, the α carbon, which also carries a hydrogen atom and a variable group.

**Definition 3.1.1** The variable group attached to the α carbon of an α-amino acid is called its **side chain**, or R group. The 20 α-amino acids specified by the standard genetic code and incorporated into proteins by ribosomes are called the **standard amino acids** (or common amino acids).

Proline is the one exception to the general structure: its side chain is bonded to the α-amino nitrogen as well as to the α carbon, forming a five-membered ring with a secondary amino (imino) group. Two further amino acids, selenocysteine and pyrrolysine, are also inserted by **ribosomes**, but only in a few proteins and by special recoding of **stop codons** (3.3.1); they are not counted among the standard amino acids.

Two numbering conventions are in use. Biochemists label the carbons of the side chain with Greek letters, counting outward from the α carbon: β, γ, δ, ε (so the amino group at the end of the lysine side chain is the ε-amino group). Systematic nomenclature numbers the chain from the carboxyl carbon, C-1, so the α carbon is C-2. For heterocyclic side chains such as that of histidine, numbers are used, and branched side chains carry numbered Greek letters (the two terminal carbons of leucine are δ1 and δ2).

### 3.1.2. Stereochemistry: Amino Acid Residues in Proteins Are L

In all standard amino acids except glycine, whose R group is a second hydrogen atom, the α carbon carries four different groups and is a chiral centre (**chirality**, [6.5.5](/6.5.5#sec-5.2)). Each amino acid therefore exists as two **enantiomers**, designated D and L by Fischer's convention, which relates the configuration to that of D- and L-glyceraldehyde rather than to the direction of optical rotation ([6.5.5](/6.5.5#sec-5.3.3)). The amino acid residues of proteins are, with very rare exceptions, L stereoisomers.

In the Cahn–Ingold–Prelog system the L-amino acids are (*S*), with one exception: L-cysteine is (*R*), because the sulfur of its $\ce{CH2SH}$ group gives the side chain a higher priority than the carboxyl group. Threonine and isoleucine have a second chiral centre in the side chain: the natural forms are (2*S*,3*R*)-threonine and (2*S*,3*S*)-isoleucine.

The exclusive use of one enantiomer is not accidental. Regular, repeating structures such as the **α helix** (7.1.5) can form only from residues of one stereochemical series, and the **active sites** of the **enzymes** that synthesize amino acids are themselves chiral and make only one isomer. D-Amino acids do occur in biology, but outside ribosomal proteins or as later modifications: D-alanine and D-glutamate in the **peptidoglycan** of bacterial cell walls (7.1.10), D-amino acids in **peptide** antibiotics made by nonribosomal peptide synthetases (gramicidin S, bacitracin), D-serine as a co-agonist of NMDA **receptors** in the brain, and D-aspartate formed by slow racemization in long-lived proteins such as those of the eye lens and tooth dentine.

## 3.2. The 20 Standard Amino Acids

### 3.2.1. Five Classes by R Group

The standard amino acids are grouped into five classes according to the polarity of their R groups at pH near 7, that is, their tendency to interact with water. The classification is a matter of judgement for a few residues (glycine, histidine, cysteine and tyrosine fit imperfectly), but it captures what matters for structure.

| Class | Amino acids | What the side chains have in common |
|---|---|---|
| nonpolar, aliphatic (7) | Gly, Ala, Pro, Val, Leu, Ile, Met | hydrocarbon (or thioether) side chains; cluster inside proteins by the **hydrophobic effect** |
| aromatic (3) | Phe, Tyr, Trp | aromatic rings; relatively nonpolar, Tyr and Trp somewhat polar; absorb UV light |
| polar, uncharged (5) | Ser, Thr, Cys, Asn, Gln | hydroxyl, thiol or amide groups that form hydrogen bonds with water |
| positively charged, basic (3) | Lys, Arg, His | protonated amino, guanidinium or imidazolium groups |
| negatively charged, acidic (2) | Asp, Glu | carboxylate groups |

Asparagine and glutamine are the amides of aspartate and glutamate, into which they are hydrolysed by acid or base. Glycine's side chain is too small to contribute to **hydrophobic interactions**, so it is the least hydrophobic member of its class; cysteine is grouped with the polar residues although its hydropathy index is positive, because its thiol is a weak acid that forms weak hydrogen bonds.

### 3.2.2. The Properties Table

The properties that the rest of the course draws on are collected in one table. The hydropathy index used in the table is defined as follows.

**Definition 3.2.1** The **hydropathy index** of an amino acid (Kyte and Doolittle, 1982) is a number on a scale that combines the hydrophobicity and hydrophilicity of its side chain, derived from the Gibbs energy of transfer of the side chain between water and a nonpolar environment and from its frequency at protein surfaces: positive values for hydrophobic side chains (Ile, +4.5), negative values for hydrophilic ones (Arg, −4.5).

| Amino acid | Abbr. | $M_{\mathrm{r}}$ | $\mathrm{p}K_1$ (α-COOH) | $\mathrm{p}K_2$ (α-$\ce{NH3+}$) | $\mathrm{p}K_{\mathrm{R}}$ (R group) | pI | Hydropathy index | Occurrence in proteins / % |
|---|---|---|---|---|---|---|---|---|
| *Nonpolar, aliphatic* | | | | | | | | |
| glycine | Gly G | 75 | 2.34 | 9.60 | | 5.97 | −0.4 | 7.2 |
| alanine | Ala A | 89 | 2.34 | 9.69 | | 6.01 | 1.8 | 7.8 |
| proline | Pro P | 115 | 1.99 | 10.96 | | 6.48 | −1.6 | 5.2 |
| valine | Val V | 117 | 2.32 | 9.62 | | 5.97 | 4.2 | 6.6 |
| leucine | Leu L | 131 | 2.36 | 9.60 | | 5.98 | 3.8 | 9.1 |
| isoleucine | Ile I | 131 | 2.36 | 9.68 | | 6.02 | 4.5 | 5.3 |
| methionine | Met M | 149 | 2.28 | 9.21 | | 5.74 | 1.9 | 2.3 |
| *Aromatic* | | | | | | | | |
| phenylalanine | Phe F | 165 | 1.83 | 9.13 | | 5.48 | 2.8 | 3.9 |
| tyrosine | Tyr Y | 181 | 2.20 | 9.11 | 10.07 | 5.66 | −1.3 | 3.2 |
| tryptophan | Trp W | 204 | 2.38 | 9.39 | | 5.89 | −0.9 | 1.4 |
| *Polar, uncharged* | | | | | | | | |
| serine | Ser S | 105 | 2.21 | 9.15 | | 5.68 | −0.8 | 6.8 |
| threonine | Thr T | 119 | 2.11 | 9.62 | | 5.87 | −0.7 | 5.9 |
| cysteine | Cys C | 121 | 1.96 | 10.28 | 8.18 | 5.07 | 2.5 | 1.9 |
| asparagine | Asn N | 132 | 2.02 | 8.80 | | 5.41 | −3.5 | 4.3 |
| glutamine | Gln Q | 146 | 2.17 | 9.13 | | 5.65 | −3.5 | 4.2 |
| *Positively charged* | | | | | | | | |
| lysine | Lys K | 146 | 2.18 | 8.95 | 10.53 | 9.74 | −3.9 | 5.9 |
| histidine | His H | 155 | 1.82 | 9.17 | 6.00 | 7.59 | −3.2 | 2.3 |
| arginine | Arg R | 174 | 2.17 | 9.04 | 12.48 | 10.76 | −4.5 | 5.1 |
| *Negatively charged* | | | | | | | | |
| aspartate | Asp D | 133 | 1.88 | 9.60 | 3.65 | 2.77 | −3.5 | 5.3 |
| glutamate | Glu E | 147 | 2.19 | 9.67 | 4.25 | 3.22 | −3.5 | 6.3 |

($M_{\mathrm{r}}$ of the free amino acids; the residue in a polypeptide is lighter by 18, the elements of water. $\mathrm{p}K_{\mathrm{a}}$ values of the free amino acids at $25\,^\circ\mathrm{C}$; in proteins the values shift, 3.4.2. Occurrence: average in more than 1150 proteins, after Doolittle, 1989.)

### 3.2.3. Structures

The structures below show the ionization states that predominate at pH 7.0 (histidine is drawn uncharged, although about 10 % of its side chains are protonated at this pH). Nonpolar, aliphatic:

```smiles
[NH3+]CC(=O)[O-] Gly
[NH3+][C@@H](C)C(=O)[O-] Ala
[O-]C(=O)[C@@H]1CCC[NH2+]1 Pro
[NH3+][C@@H](C(C)C)C(=O)[O-] Val
[NH3+][C@@H](CC(C)C)C(=O)[O-] Leu
[NH3+][C@@H]([C@@H](C)CC)C(=O)[O-] Ile
[NH3+][C@@H](CCSC)C(=O)[O-] Met
```

Aromatic:

```smiles
[NH3+][C@@H](Cc1ccccc1)C(=O)[O-] Phe
[NH3+][C@@H](Cc1ccc(O)cc1)C(=O)[O-] Tyr
[NH3+][C@@H](Cc1c[nH]c2ccccc12)C(=O)[O-] Trp
```

Polar, uncharged:

```smiles
[NH3+][C@@H](CO)C(=O)[O-] Ser
[NH3+][C@@H]([C@@H](C)O)C(=O)[O-] Thr
[NH3+][C@@H](CS)C(=O)[O-] Cys
[NH3+][C@@H](CC(N)=O)C(=O)[O-] Asn
[NH3+][C@@H](CCC(N)=O)C(=O)[O-] Gln
```

Positively charged:

```smiles
[NH3+][C@@H](CCCC[NH3+])C(=O)[O-] Lys
[NH3+][C@@H](CCCNC(N)=[NH2+])C(=O)[O-] Arg
[NH3+][C@@H](Cc1c[nH]cn1)C(=O)[O-] His
```

Negatively charged:

```smiles
[NH3+][C@@H](CC(=O)[O-])C(=O)[O-] Asp
[NH3+][C@@H](CCC(=O)[O-])C(=O)[O-] Glu
```

### 3.2.4. From Side-Chain Chemistry to Function

Each side chain brings a particular chemistry into proteins. The table is the reference for the later chapters on structure, binding and catalysis.

| Residue | Key chemical property | Typical structural and functional roles |
|---|---|---|
| Gly | smallest, achiral, most flexible backbone | tight turns and loops; every third residue of collagen (7.1.5); destabilizes α helices |
| Ala | small methyl group | strong helix former; packing in protein cores |
| Val, Leu, Ile | branched hydrocarbon, strongly hydrophobic | protein cores, transmembrane helices (7.1.13); β-branched Val and Ile favour **β sheets** |
| Met | flexible thioether, oxidizable to sulfoxide | initiator residue (AUG); precursor of the methyl donor **S-adenosylmethionine** (7.1.17, 7.1.27) |
| Pro | rigid ring, secondary amine without N–H | breaks α helices; common in turns and in collagen; X–Pro bonds can be cis, and their isomerization limits folding (7.1.6) |
| Phe, Trp | large aromatic rings | hydrophobic cores, stacking, cation–π interactions; Trp absorbs at 280 nm and fluoresces near 350 nm (3.2.6) |
| Tyr | aromatic ring with weakly acidic OH ($\mathrm{p}K_{\mathrm{R}} \approx 10$) | hydrogen bonding; phosphorylation by tyrosine kinases (7.1.15); tyrosyl radicals in **ribonucleotide reductase** (7.1.28) and **photosystem II** (7.1.24) |
| Ser, Thr | hydroxyl group | hydrogen bonds; phosphorylation (7.1.9); O-glycosylation (7.1.10); Ser is the nucleophile of **serine proteases** (7.1.8) |
| Cys | thiol, $\mathrm{p}K_{\mathrm{R}} \approx 8.2$; good nucleophile; soft metal ligand | **covalent catalysis**; Zn²⁺ and Fe–S cluster ligand; **disulfide bonds** in extracellular proteins; redox switches |
| Asn, Gln | amide, donor and acceptor of H bonds | hydrogen-bond networks; N-glycosylation at Asn–X–Ser/Thr (7.1.10); slow deamidation in ageing proteins; Gln is the amide-nitrogen donor of **biosynthesis** (7.1.27) |
| Lys | ε-amino group, $\mathrm{p}K_{\mathrm{R}} \approx 10.5$, positive | salt bridges, **DNA** and phosphate binding; Schiff bases with **pyridoxal phosphate** and in aldolase (7.1.17–7.1.18); acetylation, methylation, **ubiquitination** (3.3.2) |
| Arg | guanidinium, $\mathrm{p}K_{\mathrm{R}} \approx 12.5$, always positive | bidentate hydrogen bonds to phosphates and carboxylates; DNA binding; **substrate** binding |
| His | imidazole, $\mathrm{p}K_{\mathrm{R}} \approx 6$ | the only side chain that both accepts and donates a proton near pH 7: **general acid–base catalysis** (7.1.8), buffering (7.1.2), metal ligand (the proximal His of **heme**, 7.1.7) |
| Asp, Glu | carboxylate, $\mathrm{p}K_{\mathrm{R}} \approx 4$, negative | salt bridges; Ca²⁺ and Mg²⁺ binding; general acid–base catalysis and catalytic nucleophiles (lysozyme, 7.1.8) |

Cysteine deserves a further word. Two cysteine thiols are oxidized to a disulfide-linked dimer, cystine; in proteins such **disulfide bonds** ([6.5.26](/6.5.26#sec-26.8.4)) form between residues of the same chain or of different chains, and they are reduced back to thiols by reagents such as 2-mercaptoethanol or dithiothreitol. Disulfides stabilize proteins secreted into the oxidizing extracellular environment; inside cells, where glutathione keeps the cytosol reducing, they are rare. **Insulin** is the classic example: its A chain (21 residues) and B chain (30 residues) are linked by two interchain disulfides (A7–B7, A20–B19), and the A chain has one intrachain disulfide (A6–A11).

### 3.2.5. Learning the Amino Acids

The 20 structures, abbreviations and properties must be known by heart; three aids make this easier.

*The one-letter code* (devised by Margaret Dayhoff to save memory in early sequence databases) follows rules. For six amino acids the first letter is unique: C, H, I, M, S, V (Cys, His, Ile, Met, Ser, Val). For five others the first letter is shared but goes to the more common amino acid: A, G, L, P, T (Ala, Gly, Leu, Pro, Thr; leucine, for example, is more common than lysine). Four are phonetic: R, F, Y, W ("aRginine", "Fenylalanine", "tYrosine", "tWiptophan"). Four use a letter inside or suggested by the name: D, N, E, Q ("asparDic", "asparagiNe", "glutamEke", "Q-tamine"). Lysine got K, the free letter closest to L. Further symbols are B (Asx, Asp or Asn), Z (Glx, Glu or Gln), X (unknown), U (selenocysteine) and O (pyrrolysine).

*Overlapping properties.* The five-class scheme forces each residue into one box, but several properties overlap: tyrosine is both aromatic and polar, cysteine both small and hydrophobic, histidine aromatic, polar and charged. A Venn diagram shows these overlaps at a glance, and a map of volume against hydropathy shows which residues are similar enough to replace each other in evolution (7.1.4).

![Venn diagram of amino acid properties (after Taylor, 1986): every standard amino acid, in one-letter code, placed in the overlapping sets hydrophobic, polar and small. Cys and Thr belong to all three; His, Lys, Trp and Tyr are both hydrophobic and polar; Pro is only small. Colours: the classes used in sequence alignments (hydrophobic, polar, positive, negative). Subsets: aliphatic I, L, V; aromatic F, W, Y, H; tiny A, G, S, C; charged D, E, H, K, R](./plots/amino-acid-venn.py)

![Property map of the 20 amino acids: residue volume in proteins against the Kyte–Doolittle hydropathy index; squares mark aromatic residues. The hydrophobic aliphatic residues (I, L, V, M) and Phe form one cluster on the right, the charged and amide residues another on the left; Gly, Ser, Thr, Pro and Cys lie near the middle. Residues close together on the map (I/L/V, D/E, K/R, F/Y) are those most often exchanged by conservative substitutions. D, N, E, Q and H are displaced slightly so that their symbols do not overlap](./plots/amino-acid-property-map.py)

*Pairs and families.* Many amino acids come in related pairs: Ser/Thr (hydroxyl), Asp/Glu and Asn/Gln (acid and amide, one $\ce{CH2}$ apart), Val/Leu/Ile (branched), Phe/Tyr (Tyr is hydroxylated Phe, and this is how it is made, 7.1.27), Lys/Arg (long basic chains), Cys/Ser (SH vs OH), Met/Cys (the two sulfur amino acids). Learning the differences within each pair is easier than learning 20 independent structures.

### 3.2.6. Ultraviolet Absorption and Protein Concentration

The aromatic side chains of tryptophan and tyrosine absorb ultraviolet light strongly near 280 nm (phenylalanine absorbs weakly near 257 nm), so most proteins have an absorption maximum at 275–280 nm. By the **Beer–Lambert law** ([6.3.17](/6.3.17#sec-17.2.2)) the absorbance $A = \varepsilon c l$ measures the protein concentration $c$ if the molar absorption coefficient $\varepsilon$ is known. For a protein of known sequence $\varepsilon_{280}$ can be estimated from its composition (Pace et al., 1995):

$$
\varepsilon_{280} \approx \left(5500\,n_{\mathrm{Trp}} + 1490\,n_{\mathrm{Tyr}} + 125\,n_{\mathrm{cystine}}\right)\ \mathrm{L\,mol^{-1}\,cm^{-1}},
$$
where $n$ counts the Trp and Tyr residues and the disulfide bonds.

**Example 3.2.1** Hen egg-white lysozyme (129 residues, $M_{\mathrm{r}} = 14\,300$) contains 6 Trp, 3 Tyr and 4 disulfide bonds, so $\varepsilon_{280} \approx 6(5500) + 3(1490) + 4(125) = 37\,970\,\mathrm{L\,mol^{-1}\,cm^{-1}}$. A solution of $1\,\mathrm{mg\,mL^{-1}}$ ($7.0 \times 10^{-5}\,\mathrm{M}$) in a 1 cm cuvette should therefore have $A_{280} \approx 2.65$; the measured value is 2.64. A protein without Trp and Tyr, by contrast, is nearly invisible at 280 nm and must be measured at 205 nm (peptide bonds) or with a dye-binding assay.

Tryptophan is also fluorescent (excitation at 280–295 nm, emission at 330–350 nm), and its emission shifts and changes intensity when the residue moves between the protein interior and water: the most widely used reporter of protein folding (7.1.6) and ligand binding.

## 3.3. Uncommon Amino Acids and Modifications

### 3.3.1. Uncommon Amino Acids in Proteins

Proteins contain more than 20 kinds of residues. Most of the others are made by modifying standard residues after they have been built into a polypeptide.

| Residue | Formed from | Where it occurs and why |
|---|---|---|
| 4-hydroxyproline, 5-hydroxylysine | Pro, Lys (hydroxylases requiring ascorbate) | collagen; hydroxyproline stabilizes the triple helix, hydroxylysine is a site of cross-links and **glycosylation** (7.1.5; scurvy) |
| 6-*N*-methyllysine | Lys | myosin, **histones** |
| γ-carboxyglutamate | Glu (**vitamin** K-dependent carboxylase) | prothrombin and other blood-clotting proteins; binds Ca²⁺ |
| desmosine | four Lys residues | cross-links of elastin |
| selenocysteine | Ser on a special **tRNA** (Sec) | inserted at UGA **codons** followed by a SECIS element in the **mRNA**; about 25 human selenoproteins, such as glutathione peroxidase |
| pyrrolysine | Lys | inserted at UAG codons in some methanogenic archaea and bacteria (methylamine methyltransferases) |

Selenocysteine and pyrrolysine are exceptions in two respects: they are made from other amino acids (selenocysteine on its tRNA) but they are inserted during **translation**, by reinterpretation of a stop codon. They are sometimes called the 21st and 22nd genetically encoded amino acids.

### 3.3.2. Post-Translational Modifications

**Definition 3.3.1** A covalent change to a protein made after (or during) its synthesis on the ribosome, such as cleavage of the chain or the addition of a chemical group to a side chain or terminus, is called a **post-translational modification**.

Some modifications are permanent (the hydroxylations above, the removal of the initiator Met, the cleavage of **zymogens**, 7.1.9); others are reversible and serve to switch protein activity on and off. The reversible ones are the basis of most regulation and signaling:

| Modification | Residues | Enzymes (add / remove) | Main roles |
|---|---|---|---|
| phosphorylation | Ser, Thr, Tyr (His, Asp in bacteria) | **protein kinases** / phosphatases | enzyme regulation (7.1.9), **signal transduction** (7.1.14–7.1.15) |
| acetylation | Lys ε-amino group, N-terminus | acetyltransferases / deacetylases | **chromatin** and **gene** regulation ([7.2](/7.2)), metabolic enzymes |
| methylation | Lys, Arg | methyltransferases / demethylases | **histone code**, RNA-binding proteins |
| ubiquitination | Lys | ubiquitin ligases / deubiquitinases | targeting to the **proteasome**, signaling (7.1.15, [7.2](/7.2)) |
| ADP-ribosylation | Arg, Ser, Glu, Cys | ADP-ribosyltransferases (also bacterial toxins: cholera, diphtheria) | DNA repair, toxin action (7.1.14) |
| adenylylation (AMPylation) | Tyr | adenylyltransferase | **glutamine synthetase** regulation (7.1.27) |
| lipidation (myristoylation, palmitoylation, prenylation) | N-terminal Gly, Cys | acyl- and prenyltransferases | membrane anchoring (7.1.13) |
| glycosylation | Asn, Ser, Thr | glycosyltransferases (in the ER and Golgi) | folding, sorting, recognition (7.1.10) |

### 3.3.3. Amino Acids That Are Not in Proteins

About 300 further amino acids occur in cells, free or combined, but never in proteins. Several are central metabolites: ornithine and citrulline are intermediates of the **urea cycle** and of arginine biosynthesis (7.1.22); homocysteine and homoserine are intermediates of methionine and threonine **metabolism** (7.1.27); β-alanine is part of **coenzyme A** (7.1.17); γ-aminobutyrate (GABA) and other amino acid derivatives (dopamine, serotonin, histamine) are neurotransmitters and **hormones** (7.1.27).

## 3.4. Amino Acids Can Act as Acids and Bases

### 3.4.1. Zwitterions and Titration Curves

The amino and carboxyl groups, together with the ionizable R groups, are weak acids and bases. An amino acid without an ionizable R group dissolved in water at neutral pH exists predominantly as a dipolar ion, a **zwitterion**, with a protonated amino group and a deprotonated carboxyl group ([6.5.33](/6.5.33#sec-33.2)). It is amphoteric: in acid the carboxylate accepts a proton (giving the cation $\ce{^+H3N-CHR-COOH}$), in base the ammonium group loses one (giving the anion $\ce{H2N-CHR-COO-}$).

The titration curve of glycine has two stages, with midpoints at $\mathrm{p}K_1 = 2.34$ (α-COOH) and $\mathrm{p}K_2 = 9.60$ (α-$\ce{NH3+}$); in each stage glycine buffers effectively, although neither lies near physiological pH. Between them, at pH 5.97, the dominant species is the zwitterion with zero net charge. Amino acids with an ionizable side chain have three stages; their $\mathrm{p}K_{\mathrm{a}}$ values can be read separately from the curve when they lie more than about two pH units apart.

![Acid–base behaviour of amino acids and peptides, computed from pKa values. (A) Titration curves of glycine (two stages), glutamate and histidine (three stages): pH against equivalents of OH⁻ added to the fully protonated forms. Dots mark the pKa values, at the midpoint of each stage, and diamonds the isoelectric points (Gly 5.97, Glu 3.22, His 7.59). (B) Net charge as a function of pH of the tetrapeptide Ala-Glu-Gly-Lys (pI 6.1) and of glucagon (29 residues, pI 7.0), using typical pKa values of groups in peptides; the dashed line marks pH 7.4](./plots/amino-acid-titration.py)

### 3.4.2. The Chemical Environment Shifts pKa

The α-carboxyl group of an amino acid ($\mathrm{p}K_1 \approx 2$) is much more acidic than the carboxyl group of acetic acid ($\mathrm{p}K_{\mathrm{a}} = 4.76$). The nearby positively charged amino group repels the departing proton and stabilizes the carboxylate anion, and the electronegative nitrogen withdraws electrons through the bonds. Conversely, the α-amino group ($\mathrm{p}K_2 \approx 9.6$) is slightly less basic than a simple primary amine (methylammonium, $\mathrm{p}K_{\mathrm{a}} = 10.6$) because of the electron-withdrawing carboxyl group. In peptides the termini are no longer adjacent to each other's charges, and their values move towards those of isolated groups (C-terminal carboxyl about 3.1–3.6, N-terminal amino about 7.7–8.0).

The same effect, magnified, operates in folded proteins: the $\mathrm{p}K_{\mathrm{a}}$ of a side chain depends on nearby charges, hydrogen bonds and how much it is shielded from water (7.1.2). The Glu side chain in a hydrophobic environment may have $\mathrm{p}K_{\mathrm{a}} \approx 6$–$7$; an active-site Cys next to a His can have $\mathrm{p}K_{\mathrm{a}} \approx 4$. The values in the table of 3.2.2 are therefore starting points, not constants of the protein.

### 3.4.3. Isoelectric Point and Net Charge

At its **isoelectric point** pI an amino acid or peptide has zero average net charge; it does not move in an electric field and is often least soluble. For an amino acid without an ionizable R group the pI is the mean of the two $\mathrm{p}K_{\mathrm{a}}$ values, $\mathrm{pI} = (\mathrm{p}K_1 + \mathrm{p}K_2)/2$. In general the rule is: identify the species with zero net charge, then average the two $\mathrm{p}K_{\mathrm{a}}$ values on either side of it, the one at which this species is formed and the one at which it is lost. For glutamate the neutral species exists between $\mathrm{p}K_1$ and $\mathrm{p}K_{\mathrm{R}}$, so $\mathrm{pI} = (2.19 + 4.25)/2 = 3.22$; for histidine it exists between $\mathrm{p}K_{\mathrm{R}}$ and $\mathrm{p}K_2$, so $\mathrm{pI} = (6.00 + 9.17)/2 = 7.59$; likewise lysine 9.74 and arginine 10.76.

For a peptide or protein with many ionizable groups the shortcut fails, but the net charge is easily computed. Each basic group (N-terminus, Lys, Arg, His) carries charge $+1$ times its protonated fraction and each acidic group (C-terminus, Asp, Glu, Cys, Tyr) charge $-1$ times its deprotonated fraction, so

$$
Z(\mathrm{pH}) = \sum_{i\,\in\,\text{basic}} \frac{n_i}{1 + 10^{\,\mathrm{pH} - \mathrm{p}K_i}} - \sum_{j\,\in\,\text{acidic}} \frac{n_j}{1 + 10^{\,\mathrm{p}K_j - \mathrm{pH}}},
$$
where $n_i$ is the number of groups of each type. $Z$ decreases monotonically with pH, and the pI is its single root, found numerically, for instance with `scipy.optimize.brentq` ([4.4.4](/4.4.4#sec-4.2.2)). The calculation, with typical $\mathrm{p}K_{\mathrm{a}}$ values of groups in peptides, gives a useful estimate of the charge of a protein at the pH of an experiment, which decides its behaviour in ion-exchange chromatography and electrophoresis (7.1.4).

**Example 3.4.1** The tetrapeptide Ala-Glu-Gly-Lys has four ionizable groups: the N-terminal amino group ($\mathrm{p}K_{\mathrm{a}} \approx 8.0$), the Glu side chain (4.1), the Lys side chain (10.5) and the C-terminal carboxyl (3.1). At pH 7 the termini and both side chains are ionized: $+1 - 1 + 1 - 1 = 0$. The species with zero charge exists between the dissociation of the Glu side chain and that of the N-terminus, so $\mathrm{pI} \approx (4.1 + 8.0)/2 = 6.05$, in agreement with the root of $Z(\mathrm{pH})$ in the figure above.

## 3.5. Peptides and Proteins

### 3.5.1. Peptide Bonds Link Amino Acids

Two amino acids are joined by a **peptide bond**, a substituted amide linkage formed by condensation between the α-carboxyl group of one and the α-amino group of the other, with loss of water. In water the equilibrium lies on the side of hydrolysis, so the synthesis of peptide bonds requires energy (supplied by aminoacyl-tRNA formation on the ribosome); but the bond is kinetically very stable, with an uncatalysed half-life of hundreds of years at neutral pH and $25\,^\circ\mathrm{C}$, and proteins are hydrolysed in cells only by proteases.

**Definition 3.5.1** A chain of amino acids joined by peptide bonds is a **peptide**; each amino acid unit in it is a **residue**. A peptide of a few residues (up to about 20) is an **oligopeptide**, a longer one a **polypeptide**. A **protein** is a biological macromolecule consisting of one or more polypeptide chains, usually with more than about 50 residues each.

The distinctions are not sharp: polypeptides of $M_{\mathrm{r}}$ below about 10 000 are usually called peptides or polypeptides, larger ones proteins. By convention, peptides are written and named from the residue with the free α-amino group (the amino-terminal or N-terminal residue, on the left) to the residue with the free α-carboxyl group (the C-terminal residue, on the right): Ser-Gly-Tyr-Ala-Leu, or SGYAL, is seryl-glycyl-tyrosyl-alanyl-leucine. In a peptide only the two termini and the ionizable side chains are free to ionize; the α-amino and α-carboxyl groups of internal residues are tied up in peptide bonds.

### 3.5.2. Biologically Active Peptides

Small peptides can be highly active: some are hormones, neurotransmitters, toxins or antibiotics.

| Peptide | Residues | Source and action |
|---|---|---|
| aspartame | 2 (methyl ester) | artificial sweetener (L-Asp-L-Phe-OMe; 7.1.1) |
| glutathione | 3 (γ-Glu-Cys-Gly) | major intracellular thiol; redox buffer, detoxification |
| Met-enkephalin | 5 (YGGFM) | endogenous opioid; binds the same receptors as morphine |
| oxytocin, vasopressin | 9 each (cyclic, one disulfide, C-terminal amide) | posterior pituitary hormones: uterine contraction and milk ejection; water retention by the kidney |
| bradykinin | 9 | vasodilator, **mediator** of inflammation |
| substance P | 11 | neuropeptide that transmits pain signals |
| **glucagon** | 29 | pancreatic hormone that raises blood glucose (7.1.29) |
| insulin | 51 (A 21 + B 30, three disulfides) | pancreatic hormone that lowers blood glucose (7.1.29) |
| sex peptide | 36 | *Drosophila* seminal-fluid peptide that changes female behaviour |
| **α-amanitin** | 8 (bicyclic) | death-cap mushroom toxin; inhibits **RNA polymerase** II |
| conotoxins | 10–40 | cone-snail venoms; block **ion channels** |
| chlorotoxin | 36 | scorpion venom; blocks chloride channels, binds glioma cells |
| bacitracin, polymyxin B, gramicidin S | 10–12 (cyclic, with D-amino acids) | antibiotics made by nonribosomal peptide synthetases: bacitracin against Gram-positive, polymyxin against Gram-negative bacteria |

Many peptide hormones are cut out of larger precursors by proteases and amidated at the C-terminus, which protects them from carboxypeptidases.

### 3.5.3. Proteins: Size and Composition

Polypeptides in cells range from a few residues to tens of thousands. The mass of a protein can be estimated from its number of residues: the average residue in proteins has $M_{\mathrm{r}} \approx 110$ (the frequency-weighted average of the free amino acids, about 128, minus 18 for water). Proteins with several chains are *multisubunit* proteins; if at least two chains are identical the protein is *oligomeric* and its identical units are **protomers** (7.1.5).

| Protein | $M_{\mathrm{r}}$ | Residues | Chains |
|---|---|---|---|
| **cytochrome** *c* (human, with heme) | 12 200 | 104 | 1 |
| ribonuclease A (bovine pancreas) | 13 700 | 124 | 1 |
| lysozyme (hen egg white) | 14 300 | 129 | 1 |
| myoglobin (horse heart, with heme) | 17 600 | 153 | 1 |
| chymotrypsin (bovine pancreas) | 25 200 | 241 | 3 |
| hemoglobin (human) | 64 500 | 574 | 4 |
| serum albumin (human) | 66 500 | 585 | 1 |
| hexokinase (yeast) | 107 900 | 972 | 2 |
| RNA polymerase (*E. coli* **core enzyme**) | 390 000 | about 3 500 | 5 |
| glutamine synthetase (*E. coli*) | 619 000 | 5 628 | 12 |
| titin (human, longest isoform) | 3 800 000 | 34 350 | 1 |

The amino acid composition of proteins is far from uniform: some amino acids occur once or not at all in a given protein, others make up a large fraction (collagen is one-third Gly, histones are rich in Lys and Arg). Composition alone says little about function; what matters is the sequence (7.1.4).

### 3.5.4. Conjugated Proteins and Cofactors

Many proteins contain only amino acids. Others contain additional chemical components that are essential for their function.

**Definition 3.5.2** A protein that contains, in addition to amino acids, a permanently associated chemical component is a **conjugated protein**; a non-amino-acid part that is tightly or covalently bound is called a **prosthetic group**. A **cofactor** is any non-amino-acid component (one or more inorganic ions or an organic or metallo-organic molecule) required for the activity of a protein; an organic or metallo-organic cofactor is called a **coenzyme**.

| Class | Prosthetic group | Example |
|---|---|---|
| **lipoproteins** | **lipids** | **LDL**, whose **apolipoprotein** B carries **cholesterol** (7.1.26) |
| **glycoproteins** | carbohydrates | **immunoglobulin** G (7.1.7, 7.1.10) |
| phosphoproteins | phosphate groups | casein of milk |
| hemoproteins | heme (iron **porphyrin**) | hemoglobin, cytochromes |
| **flavoproteins** | flavin nucleotides (**FAD**, **FMN**) | succinate dehydrogenase |
| metalloproteins | Fe, Zn, Ca, Mo, Cu | ferritin, alcohol dehydrogenase, **calmodulin**, **nitrogenase**, **plastocyanin** |

Whether a cofactor counts as a prosthetic group depends on how tightly it is bound, not on whether the bond is covalent. The heme of cytochrome *c* is attached by two thioether bonds to Cys residues; the heme of myoglobin and hemoglobin is not covalently bound at all but held by coordination of its iron to a histidine and by many hydrophobic contacts, yet it is so tightly bound that it, too, is a prosthetic group. By contrast $\ce{NAD+}$ binds lactate dehydrogenase only transiently, leaving with each turnover as **NADH**; it is a coenzyme acting as a co-substrate. Most coenzymes are derived from vitamins, which is why vitamins are needed in the diet (7.1.17). The protein part of a conjugated protein without its prosthetic group is the apoprotein.

## Summary

| Structural feature | Chemical property | Biological function |
|---|---|---|
| α carbon with $\ce{NH3+}$, $\ce{COO-}$, H and R (Definition 3.1.1) | chiral (except Gly); proteins use L (Cys is *R*) | regular, repeating structures need one stereochemical series |
| nonpolar aliphatic and aromatic R groups | hydrophobic (hydropathy index, Definition 3.2.1) | protein cores, membrane spanning, ligand binding; Trp/Tyr absorb at 280 nm (Example 3.2.1) |
| Ser/Thr/Tyr hydroxyl, Asn/Gln amide | hydrogen bonding; phosphorylation and glycosylation sites | surfaces, active sites, regulation |
| Cys thiol | nucleophile, metal ligand, oxidation to disulfide | catalysis, metal sites, stabilization of extracellular proteins |
| His imidazole ($\mathrm{p}K_{\mathrm{R}} = 6.0$) | partly protonated at pH 7 | acid–base catalysis, buffering, metal ligand |
| Lys, Arg, Asp, Glu | charged at pH 7 | salt bridges, binding of DNA, phosphates and metal ions; Lys modifications |
| Pro ring, Gly hydrogen | rigid, flexible | turns, helix breaking; collagen |
| modified residues (Definition 3.3.1) | added groups | regulation (phosphorylation, acetylation, ubiquitination), clotting (Gla), collagen (Hyp) |
| ionizable groups | $Z(\mathrm{pH})$, pI; $\mathrm{p}K_{\mathrm{a}}$ shifted by environment | separation by charge (7.1.4); tuned catalytic groups |
| peptide chains (Definition 3.5.1) | written N → C; average residue $M_{\mathrm{r}} \approx 110$ | hormones, toxins, antibiotics, proteins of 50–34 000 residues |
| prosthetic groups and cofactors (Definition 3.5.2) | metals, heme, flavins, coenzymes | chemistry that amino acids cannot provide: redox, $\ce{O2}$ binding, group transfer |

Key numbers to remember: $\mathrm{p}K_{\mathrm{R}}$ values Asp 3.65, Glu 4.25, His 6.0, Cys 8.2, Tyr 10.1, Lys 10.5, Arg 12.5; α-COOH about 2, α-$\ce{NH3+}$ about 9–10; $\mathrm{pI} = (\mathrm{p}K_1 + \mathrm{p}K_2)/2$ for neutral side chains; $\varepsilon_{280}$ Trp 5500, Tyr 1490.

## Questions

1. What fraction of free histidine side chains is protonated at pH 7.4? At pH 6.0? Why is His so often found at enzyme active sites?

   **Answer** With $\mathrm{p}K_{\mathrm{R}} = 6.0$, the protonated fraction is $1/(1 + 10^{\mathrm{pH} - 6.0})$: at pH 7.4, $1/(1 + 10^{1.4}) = 3.8\,\%$; at pH 6.0, 50 %. Because its $\mathrm{p}K_{\mathrm{a}}$ is close to physiological pH, an active-site His can exist in either state and switch between them during catalysis; it can act as a general base (accept a proton) in one step and as a general acid (donate it) in the next, which no other side chain does as well near pH 7.

2. Estimate the isoelectric point of (a) aspartate, (b) cysteine, (c) the dipeptide Lys-Asp, using the pKa values of the table in 3.2.2 for the free amino acids and, for the dipeptide, $\mathrm{p}K_{\mathrm{a}} = 8.0$ for the N-terminus, 3.1 for the C-terminus, 3.9 for Asp and 10.5 for Lys.

   **Answer** (a) The neutral form of Asp exists between $\mathrm{p}K_1 = 1.88$ and $\mathrm{p}K_{\mathrm{R}} = 3.65$: pI = 2.77. (b) For Cys the thiol is the second group to dissociate ($\mathrm{p}K_{\mathrm{R}} = 8.18 < \mathrm{p}K_2 = 10.28$), so the neutral form exists between 1.96 and 8.18: pI = 5.07. (c) Lys-Asp has two positive groups (N-terminus, Lys) and two negative ones (C-terminus, Asp). The fully protonated peptide has charge +2; it becomes +1 at 3.1, 0 at 3.9, −1 at 8.0. The zero-charge species lies between 3.9 and 8.0: pI ≈ 5.95.

3. The absorbance at 280 nm of a solution of a protein ($M_{\mathrm{r}} = 30\,000$) with 3 Trp, 10 Tyr and 1 disulfide bond is 0.60 in a 1 cm cell. What is its concentration in mg mL⁻¹?

   **Answer** $\varepsilon_{280} = 3(5500) + 10(1490) + 125 = 31\,525\,\mathrm{L\,mol^{-1}\,cm^{-1}}$; $c = A/(\varepsilon l) = 0.60/31\,525 = 1.9 \times 10^{-5}\,\mathrm{M}$, i.e. $1.9 \times 10^{-5} \times 30\,000\,\mathrm{g\,L^{-1}} = 0.57\,\mathrm{mg\,mL^{-1}}$.

4. Why is L-cysteine (*R*) while L-serine is (*S*), although their structures differ only by S in place of O?

   **Answer** L and D describe the spatial arrangement relative to glyceraldehyde, which is the same for both. *R* and *S* depend on the CIP priorities of the substituents. In serine the order is $\ce{NH3+} > \ce{COO-} > \ce{CH2OH} > \ce{H}$ (at the first point of difference the carboxyl carbon has (O, O, O) against (O, H, H)). In cysteine the $\ce{CH2SH}$ carbon carries sulfur, of higher atomic number than oxygen, so $\ce{CH2SH} > \ce{COO-}$; exchanging the priorities of two groups changes the descriptor from *S* to *R* without any change in geometry.

5. A protein has many Lys and Arg residues and few Asp and Glu. Predict its approximate pI and its net charge at pH 7. Name a class of proteins of this kind and explain how the composition suits their function.

   **Answer** The basic groups outnumber the acidic ones, so the net charge is still positive at pH 7 and becomes zero only when the Lys side chains begin to deprotonate: the pI is high, around 10–11. Histones (and many ribosomal proteins, and lysozyme, pI ≈ 11) are examples. The positive charges of histones bind the negatively charged phosphate backbone of DNA and allow it to be wound into nucleosomes ([7.2](/7.2)).
