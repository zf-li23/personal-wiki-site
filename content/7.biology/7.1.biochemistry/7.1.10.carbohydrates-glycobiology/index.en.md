---
title: Carbohydrates and Glycobiology
description: How the chemistry of sugars determines their biological roles. Biologically important monosaccharide derivatives, glycation and blood glucose; disaccharides and the naming of glycosidic linkages; storage and structural polysaccharides and how α or β linkages make helices or straight fibers; peptidoglycan and glycosaminoglycans; proteoglycans, glycoproteins, glycolipids and lipopolysaccharides; the information density of glycans, the sugar code, lectins and multivalent binding; methods of glycan analysis.
---

Carbohydrates are the most abundant biomolecules on Earth: **photosynthesis** fixes more than $10^{11}$ tonnes of carbon a year, mostly into cellulose and starch, and the oxidation of sugars is the central energy-yielding pathway of most nonphotosynthetic cells. Their chemistry, the configurations and ring forms of monosaccharides, mutarotation, the reducing property and the formation of glycosidic bonds, has been treated in [6.5.32](/6.5.32). This chapter follows the thread of Part I (7.1.1), "chemical properties → structure → function", for sugars: the position and configuration of one glycosidic bond decide whether a glucose polymer is a soluble fuel store or an insoluble fiber; sulfate and carboxylate groups turn polysaccharides into the water-filled, shock-absorbing gels of connective tissue; and the many ways in which a few monosaccharides can be linked and branched make oligosaccharides the densest information carriers among biopolymers, read by sugar-binding **proteins** on every cell surface.

Section 10.1 collects the monosaccharide derivatives that matter in biology, 10.2 the disaccharides and the convention for writing linkages, 10.3 the polysaccharides, 10.4 the glycoconjugates (sugars attached to proteins and **lipids**), 10.5 the sugar code and its readers, and 10.6 the methods of analysis. The **metabolism** of carbohydrates follows in Part II: **glycolysis** (7.1.18), glycogen (7.1.19) and the synthesis of starch, sucrose and cellulose in plants (7.1.25).

## 10.1. Monosaccharides in Biology

### 10.1.1. What Chemistry Has Already Established

The following facts from [6.5.32](/6.5.32) are used throughout.

| Topic | Result | Biological consequence |
|---|---|---|
| Classes | a **monosaccharide** is a polyhydroxy aldehyde (**aldose**) or ketone (**ketose**); **oligosaccharides** and **polysaccharides** are its condensation polymers | the unit of all carbohydrate structures |
| Configuration | D and L refer to the configuration of the chiral carbon farthest from the carbonyl, compared with D-glyceraldehyde; they say nothing about the sign of optical rotation (D-fructose is levorotatory) | almost all biological sugars are D; L-fucose, L-rhamnose and L-iduronate are exceptions made from D precursors |
| Ring forms | pentoses and hexoses cyclize to the six-membered **pyranose** or five-membered **furanose**, drawn as a **Haworth projection**; the pyranose ring adopts a chair conformation | in nucleotides ribose is a furanose; in glucose polymers glucose is a pyranose |
| Anomers | ring closure creates the **anomeric carbon**; its two configurations give α and β **anomers**, which interconvert in solution (**mutarotation**; equilibrium D-glucose ≈ 36 % α, 64 % β) | the anomeric configuration is frozen when the carbon forms a glycosidic bond, and this decides polymer shape (10.3.4) |
| Reducing sugars | a free anomeric carbon is in equilibrium with the open-chain carbonyl and reduces $\ce{Cu^2+}$ (a **reducing sugar**) | the basis of glycation (10.1.3) and of the reducing end of a chain (10.2.1) |
| Glycosides | the hemiacetal at the anomeric carbon condenses with an alcohol to an acetal, a **glycoside**, joined by a **glycosidic bond**; it is stable in base and hydrolysed by acid | all oligo- and polysaccharides; hydrolysis by glycosidases in digestion |

### 10.1.2. Biologically Important Derivatives

In biology the free hexoses are less common than their derivatives, in which a hydroxyl group is replaced or esterified, or a carbon atom is oxidized.

**Definition 10.1.1** A monosaccharide in which a hydroxyl group (usually at C-2) is replaced by an amino group is called an **amino sugar**. A monosaccharide whose terminal $\ce{CH2OH}$ (C-6 of a hexose) is oxidized to a carboxyl group is a **uronic acid**. The nine-carbon acidic sugars derived from N-acetylmannosamine and pyruvate are the **sialic acids**, of which N-acetylneuraminic acid (Neu5Ac) is the most common.

| Derivative | Examples | Where it occurs and what the change does |
|---|---|---|
| sugar phosphates | glucose 6-phosphate, fructose 1,6-bisphosphate, ribose 5-phosphate | negatively charged at pH 7 and not transported across the plasma membrane, so phosphorylation traps a sugar inside the cell; it also activates the sugar for further reactions (Part II) |
| amino sugars | glucosamine (GlcN), N-acetylglucosamine (GlcNAc), N-acetylgalactosamine (GalNAc), N-acetylmuramic acid (MurNAc) | chitin, bacterial cell walls, glycosaminoglycans, glycoproteins; the N-acetyl group adds hydrophobic and hydrogen-bonding surface |
| deoxy sugars | L-fucose (6-deoxy-L-galactose), L-rhamnose (6-deoxy-L-mannose), 2-deoxy-D-ribose | fucose terminates many glycoprotein and glycolipid glycans (blood groups, 10.4.3); rhamnose in plant pectins; deoxyribose in **DNA** (7.1.11) |
| acidic sugars | D-glucuronate (GlcA), L-iduronate (IdoA, the C-5 epimer of GlcA), gluconate, Neu5Ac | carboxylates are ionized at pH 7: negative charge for glycosaminoglycans (10.3.6) and for the termini of cell-surface glycans; glucuronidation makes drugs and **bilirubin** water-soluble for excretion |
| lactones | glucono-δ-lactone; L-ascorbate (**vitamin** C) | ascorbate is a **cofactor** of the hydroxylases that make **collagen** hydroxyproline (7.1.5); primates cannot make it |

```smiles
CC(=O)N[C@@H]1[C@@H](O)[C@H](O)[C@@H](CO)O[C@H]1O GlcNAc
CC(=O)N[C@@H]1[C@H](C[C@@](O[C@H]1[C@@H]([C@@H](CO)O)O)(C(=O)O)O)O Neu5Ac
```

The two amino-sugar derivatives above are the β anomer of N-acetyl-D-glucosamine and β-N-acetylneuraminic acid. Neu5Ac is a 2-keto acid: its anomeric carbon is C-2, so sialic acids are joined to other sugars through C-2 (α2→3 or α2→6 linkages, 10.4.2), and their carboxylate ($\mathrm{p}K_{\mathrm{a}} \approx 2.6$) gives the outer surface of animal cells much of its negative charge.

### 10.1.3. Reducing Ends in the Blood: Glycation and Glucose Measurement

The aldehyde of open-chain glucose reacts slowly and without **enzymes** with primary amino groups of proteins: a Schiff base (**imine**) forms and rearranges to a stable ketoamine (the Amadori product).

**Definition 10.1.2** The nonenzymatic attachment of a reducing sugar to an amino group of a protein is called **glycation**; it is distinguished from glycosylation, the enzymatic transfer of sugars (Definition 10.4.4).

Because glycation of hemoglobin proceeds at a rate proportional to the glucose concentration and is not reversed, the fraction of **glycated hemoglobin** integrates the blood glucose over the lifetime of an erythrocyte (about 120 days, weighted towards the last few weeks). The monoglycated form HbA1c (glucose on the N-terminal Val of the β chain) is about 5 % of total hemoglobin in healthy people and is the standard measure for diagnosing **diabetes** (≥ 6.5 %) and monitoring its treatment (7.1.29). Further rearrangement and oxidation of glycated proteins give advanced glycation end products (AGEs), which cross-link proteins and activate the **receptor** RAGE; they contribute to the kidney, retinal and vascular damage of chronic hyperglycemia. Point-of-care glucose meters use an enzyme instead: glucose oxidase converts β-D-glucose and $\ce{O2}$ to glucono-δ-lactone and $\ce{H2O2}$, which is measured electrochemically or with a peroxidase-coupled dye (the meter reads $3.9$–$5.6\,\mathrm{mM}$ fasting glucose as normal).

Sweetness is a second example in which the chemistry of a sugar is read by a protein: the sweet-taste receptor is a heterodimer of two **G protein–coupled receptors**, T1R2 and T1R3 (7.1.14). Natural sugars bind both **subunits**, many artificial sweeteners only one; the receptor is stereoselective (L-aspartyl-L-phenylalanine methyl ester, aspartame, is sweet, while its diastereomer with D-phenylalanine is bitter), and the sweetness of different sugars differs by an order of magnitude (fructose is about twice as sweet as sucrose, lactose a fifth as sweet).

## 10.2. Disaccharides

### 10.2.1. Writing a Glycosidic Linkage

A disaccharide forms when a hydroxyl group of one monosaccharide condenses with the anomeric carbon of another. Three facts define the linkage: which carbons are joined, the configuration (α or β) of the anomeric carbon that takes part, and the ring sizes.

**Definition 10.2.1** In an oligo- or polysaccharide, the end whose residue has a free anomeric carbon (not involved in a glycosidic bond) is the **reducing end**; the other ends are nonreducing ends.

By convention an oligosaccharide is written with the nonreducing end on the left. The abbreviated name gives each **residue** (three-letter symbols: Glc, Gal, Man, Fru, GlcNAc, …; pyranose and D understood unless stated) followed by the linkage in parentheses: anomeric configuration, then the carbon of the residue and the carbon of the next residue it is joined to. Maltose is Glc(α1→4)Glc: C-1 of the first glucose, in the α configuration, is joined to O-4 of the second. When both anomeric carbons are joined, a double arrow is used and the configuration of each is given: sucrose is Glc(α1↔2β)Fru. The configuration of the reducing-end residue is not specified, because it still mutarotates. In figures, glycans are drawn in the Symbol Nomenclature for Glycans (SNFG), in which each monosaccharide is a coloured shape (Figure in 10.4.2).

### 10.2.2. The Common Disaccharides

| Disaccharide | Abbreviated name | Reducing? | Source and role |
|---|---|---|---|
| maltose | Glc(α1→4)Glc | yes | product of starch digestion by amylases |
| isomaltose | Glc(α1→6)Glc | yes | **branch point** of glycogen and amylopectin |
| cellobiose | Glc(β1→4)Glc | yes | repeating unit of cellulose |
| lactose | Gal(β1→4)Glc | yes | sugar of milk (about 7 % of human milk) |
| sucrose | Glc(α1↔2β)Fru | no | formed by plants, transported in phloem |
| trehalose | Glc(α1↔1α)Glc | no | insect hemolymph; protects yeasts, tardigrades and resurrection plants against drying and freezing |

Two of these illustrate how a chemical property serves a function. Sucrose and trehalose have no free anomeric carbon: they cannot be oxidized or react with amino groups, which makes them suitable for transporting and storing sugar at high concentrations (sucrose in phloem sap reaches several hundred millimolar). Lactose must be hydrolysed by lactase on the brush border of the small intestine before its monosaccharides are absorbed. In most adult mammals, and in most humans, lactase expression falls after weaning; undigested lactose stays in the lumen, where it holds water by **osmosis** and is fermented by colonic bacteria to gases and short-chain acids, which causes the symptoms of lactose intolerance. Lactase persistence into adulthood is a recent (within the last 10 000 years) genetic adaptation in dairying populations, caused by several independent regulatory **mutations** upstream of the lactase **gene** *LCT*.

## 10.3. Polysaccharides

### 10.3.1. Homopolysaccharides and Heteropolysaccharides

Most carbohydrates in nature are polysaccharides, also called glycans, of molecular mass from about 20 kDa to over $10^8\,\mathrm{Da}$. The boundary between oligo- and polysaccharides is a convention (often "more than about ten residues").

**Definition 10.3.1** A polysaccharide made of only one kind of monomer is a **homopolysaccharide**; one made of two or more kinds is a **heteropolysaccharide**.

Polysaccharides differ in four respects: the monomer, the chain length, the linkages, and the degree of branching. Unlike proteins and nucleic acids, they have no defined length or sequence: they are not copied from a template but built by glycosyltransferases, each of which adds one kind of sugar in one kind of linkage. The "program" is the set of enzymes present, and the products are heterogeneous in length and branching.

### 10.3.2. Storage Polysaccharides: Starch and Glycogen

**Definition 10.3.2** **Starch**, the storage polysaccharide of plants, is a mixture of two glucose polymers: **amylose**, unbranched chains of (α1→4)-linked D-glucose (several hundred to several thousand residues), and **amylopectin**, (α1→4)-linked chains with (α1→6) branches every 24–30 residues (up to $10^6$ residues). **Glycogen**, the storage polysaccharide of animals, fungi and bacteria, resembles amylopectin but is branched every 8–12 residues and more compact.

Both occur as granules, in plastids (starch) or in the cytosol (glycogen: up to about 7 % of the wet mass of liver and 1–2 % of skeletal muscle). Branching has a functional reason: a molecule with $n$ branches has $n + 1$ nonreducing ends and only one reducing end, and the enzymes that release glucose (**glycogen phosphorylase**, 7.1.19) act only at nonreducing ends. A highly branched molecule can therefore be mobilized from many ends at once. Branching also makes the polymer more soluble. The reducing end of each glycogen molecule is attached to the protein **glycogenin**, which primes its synthesis (7.1.19, where a simple optimization model shows why the branch frequency and chain length of glycogen are close to the values that maximize stored glucose and rate of release).

Why polymerize at all? Osmotic pressure depends on the number of solute particles, not on their mass (**osmolarity**, 7.1.2), and a polymer of $10^4$–$10^5$ residues counts as one particle.

**Example 10.3.1** Hepatocytes of a fed animal store glycogen equivalent to about $0.4\,\mathrm{M}$ glucose. A glycogen β particle contains about $5 \times 10^4$ glucose residues, so the concentration of glycogen molecules is only about $10\,\mathrm{\mu M}$. By the van 't Hoff relation $\Pi = cRT$ for dilute solutions (**osmotic pressure**, [6.3.5](/6.3.5)), $0.4\,\mathrm{M}$ free glucose would add
$$
\Pi = 400\,\mathrm{mol\,m^{-3}} \times 8.314\,\mathrm{J\,mol^{-1}\,K^{-1}} \times 310\,\mathrm{K} \approx 1.0\,\mathrm{MPa}
$$
to the cytosol, more than the total osmotic pressure of cytosol and plasma (about $0.3\,\mathrm{osmol\,L^{-1}}$, or $0.77\,\mathrm{MPa}$). Water would flow in until the cell lysed. Stored as glycogen the same glucose contributes about $10^{-5}\,\mathrm{M}$ of particles, an osmotic pressure of about $26\,\mathrm{Pa}$, negligible. The cell pays for this with the energy of polymerization: one UTP per glucose incorporated (7.1.19).

### 10.3.3. Structural Polysaccharides: Cellulose and Chitin

**Definition 10.3.3** **Cellulose** is a linear, unbranched homopolysaccharide of (β1→4)-linked D-glucose (about 10 000–15 000 residues per chain), the main component of plant cell walls. **Chitin** is a linear homopolysaccharide of (β1→4)-linked N-acetyl-D-glucosamine, the main component of arthropod exoskeletons and fungal cell walls.

Cellulose and amylose differ only in the configuration of the anomeric carbon in each linkage, α in amylose and β in cellulose; chitin differs from cellulose only in the acetamido group at C-2, which makes it more hydrophobic and gives an additional hydrogen bond between chains. Cellulose is the most abundant biopolymer (wood is about 50 % cellulose, cotton almost pure cellulose), and chitin probably the second (about $10^9$ tonnes made each year). Vertebrates make no cellulase: ruminants, termites and wood-eating insects digest cellulose with the cellulases of symbiotic bacteria, fungi and protists, and the cellulose of human food passes through the small intestine as dietary fiber.

### 10.3.4. The Linkage Decides the Shape

The folding of polysaccharides follows the same principles as that of **polypeptides** (7.1.5). Each pyranose ring is a rigid chair, so the conformation of a chain is determined by the two torsion angles $\phi$ and $\psi$ about the C-1–O and O–C-4′ bonds of each glycosidic linkage; steric clashes between rings and their substituents, the anomeric effect and hydrogen bonds between neighbouring residues allow only a few combinations, just as the **Ramachandran plot** restricts a **peptide**. The result is the central contrast of this chapter.

| | Amylose, glycogen chains (α1→4) | Cellulose, chitin (β1→4) |
|---|---|---|
| geometry at each linkage | each ring turned about $60^\circ$ relative to the previous one | each ring turned $180^\circ$ (flipped) relative to its neighbours |
| shape of one chain | curved; coils into a helix, about 6 residues per turn (V-amylose) or left-handed double helices (in amylopectin) | straight, flat ribbon, stiffened by an intrachain O3–H···O5′ hydrogen bond across every linkage |
| interactions | intrachain hydrogen bonds; hydroxyls exposed to water; the helix core binds polyiodide (blue starch–iodine test) | interchain hydrogen bonds between parallel chains, stacked sheets of 18–36 chains in microfibrils; few hydroxyls left for water |
| physical state | hydrated granules, dispersible in hot water | insoluble, crystalline fibers with tensile strength comparable to steel per unit mass |
| enzymes | α-amylases and phosphorylases, present in almost all organisms | cellulases and chitinases, absent from vertebrates |
| biological role | compact, rapidly mobilized fuel store | load-bearing walls and skeletons |

![Linkage geometry and polymer shape (schematic). A: in amylose each (α1→4)-linked glucose (green hexagon) is turned about 60° relative to the previous one, so the chain winds into a helix of about six residues per turn; residues on the far side are paler, and the hydrophobic core of the helix holds polyiodide ions (purple), the basis of the blue starch–iodine test. B: in cellulose each (β1→4)-linked residue is flipped by 180° (the side of its C-6 group alternates), so the chain is straight; intrachain hydrogen bonds (blue dashes) stiffen each chain, and interchain hydrogen bonds (red dashes) join parallel chains into sheets that pack into microfibrils.](./plots/polysaccharide-conformation.py)

### 10.3.5. Peptidoglycan

**Definition 10.3.4** **Peptidoglycan** (murein) is the rigid layer of the bacterial cell wall: chains of alternating (β1→4)-linked N-acetylglucosamine and N-acetylmuramic acid, GlcNAc(β1→4)MurNAc, cross-linked through short peptides attached to the lactyl group of MurNAc.

The peptides contain D-amino acids (D-Ala, D-Glu) and, in *Escherichia coli*, diaminopimelic acid; in *Staphylococcus aureus* the cross-links are pentaglycine bridges. The whole wall is one covalent bag-shaped molecule that resists the osmotic pressure of the cytoplasm (several atmospheres in Gram-positive bacteria). Two defenses and drugs attack it: lysozyme, in tears, saliva and egg white, hydrolyses the (β1→4) bond between MurNAc and GlcNAc; penicillin and other β-lactams inhibit the transpeptidases that form the peptide cross-links (7.1.8), so that growing bacteria lyse. Red algae make a structurally analogous sulfated galactan, agar, whose neutral component agarose (a polymer of D-galactose and 3,6-anhydro-L-galactose) forms the gels used for electrophoresis of nucleic acids.

### 10.3.6. Glycosaminoglycans

The extracellular space of animal tissues is filled with a gel, the extracellular matrix, of **fibrous proteins** (collagens, elastin, fibronectin, laminins) embedded in heteropolysaccharides.

**Definition 10.3.5** The **glycosaminoglycans** (GAGs) are unbranched heteropolysaccharides of repeating disaccharide units, one residue of which is GlcNAc or GalNAc and the other (except in keratan sulfate) a uronic acid, GlcA or IdoA; most carry sulfate esters.

| GAG | Repeating unit | Sulfation | Where |
|---|---|---|---|
| hyaluronan | GlcA(β1→3)GlcNAc(β1→4), up to 50 000 repeats ($M_{\mathrm{r}}$ several million) | none; not attached to protein | synovial fluid, vitreous humor, cartilage |
| chondroitin sulfate | GlcA(β1→3)GalNAc(β1→4) | GalNAc 4- or 6-sulfate | cartilage, tendons, aorta |
| dermatan sulfate | IdoA (and GlcA)(α1→3)GalNAc4S | as chondroitin | skin, blood vessels, heart valves |
| keratan sulfate | Gal(β1→4)GlcNAc6S | variable | cornea, cartilage, horn and hair |
| heparan sulfate / heparin | GlcA or IdoA2S (1→4) GlcNS or GlcNAc, many patterns | N- and O-sulfates in domains | cell surfaces and basement membranes / mast cells |

Chemistry explains the mechanical function. Carboxylate and sulfate groups give GAGs one to three negative charges per disaccharide; charge repulsion extends the chains into stiff rods, and the fixed negative charges hold a cloud of counterions. The resulting osmotic swelling (a **Donnan equilibrium**, [6.3.21](/6.3.21)) draws water into the matrix and keeps cartilage under internal pressure, so that it resists compression and springs back like a water-filled cushion. Hyaluronan solutions are highly viscous and lubricate joints; bacterial hyaluronidases and the hyaluronidase on the head of sperm digest it to penetrate tissues and the egg coat. Inherited defects in the lysosomal enzymes that degrade GAGs cause the mucopolysaccharidoses (Hurler, Hunter and Scheie syndromes), in which partially degraded GAGs accumulate.

## 10.4. Glycoconjugates

Besides fuel and structure, oligo- and polysaccharides carry information: they label proteins for transport to an organelle or for destruction, they are recognition sites for growth factors, toxins, viruses and other cells, and on almost every eukaryotic cell they form a carbohydrate coat several nanometres thick, the glycocalyx.

**Definition 10.4.1** A carbohydrate covalently joined to a protein or a lipid is a **glycoconjugate**. The three classes are proteoglycans, glycoproteins, and glycolipids (with the bacterial lipopolysaccharides).

### 10.4.1. Proteoglycans

**Definition 10.4.2** A **proteoglycan** consists of a core protein with one or more covalently attached sulfated glycosaminoglycan chains.

Most GAG chains are attached to a Ser residue of the core protein through a common tetrasaccharide linker, GlcA(β1→3)Gal(β1→3)Gal(β1→4)Xyl(β1→O)-Ser (Figure in 10.4.2). Proteoglycans occur in two forms:

- Membrane proteoglycans: Syndecans have one transmembrane helix and three to five heparan sulfate (and some chondroitin sulfate) chains; glypicans are attached by a glycosylphosphatidylinositol (GPI) anchor (7.1.13). Both can be shed from the surface by proteases or phospholipases, which lets a cell change its surface quickly.
- Matrix aggregates: In cartilage about 100 aggrecan core proteins ($M_{\mathrm{r}} \approx 250\,000$, each carrying about 100 chondroitin sulfate and 30 keratan sulfate chains) bind noncovalently, through link proteins, to one hyaluronan molecule; the aggregate ($M_{\mathrm{r}} > 2 \times 10^8$) with its water of hydration occupies a volume comparable to a bacterial cell.

Heparan sulfate shows how a GAG can carry specific information. Its chains alternate between N-acetylated (NA) domains of unmodified GlcNAc–GlcA and highly sulfated (NS) domains of 3–8 disaccharides, in which GlcNS, IdoA2S and 6-O-sulfates occur in patterns specific to the cell type (at least 32 different disaccharide units are possible). Proteins bind the NS domains through clusters of Arg and Lys residues, and the binding acts in four ways: it changes the conformation of the bound protein (antithrombin, whose affinity for thrombin rises about 2000-fold when heparin bridges the two proteins; therapeutic heparin works this way); it brings two proteins together; it presents a growth factor to its receptor as a coreceptor (fibroblast growth factor must bind heparan sulfate of syndecan before it can signal through the FGF receptor); and it concentrates soluble proteins at the cell surface. Mice lacking the enzyme that sulfates C-2 of iduronate are born without kidneys, and defects in heparan sulfate polymerization (the exostosin genes *EXT1*, *EXT2*) cause multiple hereditary exostoses, benign bone outgrowths.

### 10.4.2. Glycoproteins

**Definition 10.4.3** A **glycoprotein** is a protein with one or more covalently attached oligosaccharides, which are generally branched and much smaller and more diverse than the GAGs of proteoglycans. In **N-linked** glycans the anomeric carbon of a GlcNAc is joined by an N-glycosyl bond to the side-chain amide nitrogen of Asn, in the sequon Asn–X–Ser/Thr (X ≠ Pro); in **O-linked** glycans it is joined by a glycosidic bond to the hydroxyl of Ser or Thr (most often through GalNAc, in mucin-type glycans).

**Definition 10.4.4** The enzymatic attachment of carbohydrate to proteins and lipids, catalysed by glycosyltransferases, is called **glycosylation**.

About half of mammalian proteins are glycosylated; the carbohydrate makes up from 1 % to more than 70 % of the mass. Nearly all secreted and plasma-membrane proteins are glycoproteins, including antibodies and most plasma proteins; mucins, with hundreds of O-linked chains, give mucus its slipperiness. A different, nuclear and cytosolic modification is the single O-GlcNAc on Ser and Thr, added and removed dynamically like a phosphate and in competition with phosphorylation.

All N-glycans share a pentasaccharide core, Man3GlcNAc2, because they are made by transferring a preassembled Glc3Man9GlcNAc2 from the lipid carrier dolichol phosphate (7.1.12) to the nascent polypeptide in the endoplasmic reticulum and then trimming and extending it. Trimming in the ER and early Golgi leaves high-mannose glycans; in the Golgi, GlcNAc, Gal, sialic acid and fucose are added to give complex glycans; hybrid glycans carry one arm of each kind (the pathway and its enzymes belong to protein targeting in 7.3).

![N- and O-linked glycans in the Symbol Nomenclature for Glycans; the reducing end, attached to the protein, is on the right, and each label gives the anomeric configuration and the two carbons joined (β1–4: C-1 of the residue in β configuration joined to C-4 of the next one). A: the symbols: shape gives the class of sugar (circle hexose, square N-acetylhexosamine, triangle deoxyhexose, diamond sialic acid, star pentose, divided diamond uronic acid), colour the stereochemistry (blue gluco, green manno, yellow galacto). B: N-linked glycans on Asn: high-mannose (Man9GlcNAc2) and a complex biantennary glycan with terminal α2–6 sialic acids and core fucose; both contain the core Man3GlcNAc2. C: a sialylated mucin core 1 O-glycan on Ser/Thr, and the Xyl–Gal–Gal–GlcA linker through which glycosaminoglycan chains (here chondroitin repeats) are attached to Ser of a proteoglycan core protein. D: the H (blood group O), A and B antigens on a type 2 chain (they differ only in the residue added to the fucosylated galactose: none, GalNAc or Gal), and sialyl Lewis x, the ligand of the selectins (10.5.2); in short labels only the anomeric configuration and the position on the parent are given.](./plots/glycan-structures.py)

The attached oligosaccharides have general physical effects and specific ones:

- Solubility and protection: The hydrophilic glycans increase solubility, and their bulk and negative charge shield the polypeptide from proteases; clusters of charged O-glycans hold mucins and the stalks of some receptors in an extended, rodlike conformation.
- Folding and quality control: In the ER the glucose residues of the N-glycan precursor mark a folding intermediate for the lectin **chaperones** calnexin and calreticulin; glycoproteins that fail to fold are trimmed and sent for degradation.
- Targeting: Lysosomal hydrolases receive a mannose 6-phosphate tag on their N-glycans in the cis Golgi and are sorted to lysosomes by the mannose 6-phosphate receptor (10.5.2).
- Half-life and recognition: Terminal sialic acids protect plasma glycoproteins and erythrocytes from removal by the liver (10.5.2); specific terminal structures are read by lectins of other cells.

More than 100 congenital disorders of glycosylation are known, most of them affecting N-glycan synthesis; they cause severe defects of physical and mental development, which shows how many proteins depend on correct glycosylation.

### 10.4.3. Glycolipids and Lipopolysaccharides

**Definition 10.4.5** A **glycolipid** is a membrane lipid whose polar head group is a mono- or oligosaccharide. The **lipopolysaccharides** (LPS) are the glycolipids of the outer membrane of Gram-negative bacteria: lipid A (a phosphorylated GlcN disaccharide carrying six or seven fatty acids), a core oligosaccharide, and an O-specific polysaccharide chain.

In animals the main glycolipids are the glycosphingolipids, **cerebrosides**, globosides and the sialic acid–containing **gangliosides** (their lipid part is treated in 7.1.12). Their glycans face the outside of the plasma membrane, and some are identical to those of glycoproteins. The ABO blood groups are the best-known example (Figure in 10.4.2): all three **antigens** are built on the H antigen, Fuc(α1→2)Gal(β1→4)GlcNAc-R, which is the group O structure; the A allele of the *ABO* gene encodes a glycosyltransferase that adds GalNAc(α1→3) to the galactose, the B allele one that adds Gal(α1→3), and the O allele an inactive enzyme. The A and B transferases differ in only four amino acids, two of which determine the sugar donor. People make antibodies against the antigens they lack (presumably induced by similar glycans of gut bacteria), which is why transfusions must be matched.

LPS covers almost the whole surface of *E. coli* and *Salmonella*. The O chains vary between strains and define their serotypes; lipid A (endotoxin) is recognized by the Toll-like receptor TLR4 of macrophages, and large amounts of it released in Gram-negative sepsis cause a dangerous fall in blood pressure (septic shock).

## 10.5. The Sugar Code

### 10.5.1. Glycans Are Information-Dense

**Definition 10.5.1** **Glycobiology** is the study of the structure, biosynthesis and functions of glycans and glycoconjugates. The idea that specific oligosaccharide structures encode biological information, which is read by carbohydrate-binding proteins, is called the **sugar code**.

Proteins and nucleic acids are linear chains of one kind of bond; the information in a sequence is the choice of monomer at each position. Oligosaccharides add three more choices at every bond: which hydroxyl of the acceptor is used, which anomeric configuration, and whether a residue carries one or several branches. A simple count makes the difference quantitative.

**Proposition 10.5.1** Suppose $m$ kinds of monosaccharide are available, and each glycosidic bond joins C-1 of the added residue, in one of 2 anomeric configurations, to one of $k$ free hydroxyls of its acceptor. Then the number of distinct linear oligosaccharides of $n$ residues is
$$
N_{\mathrm{lin}}(n) = m^n (2k)^{n-1}, \tag{10.1}
$$
and the number of branched ones (each residue may carry up to $k$ residues on distinct hydroxyls) is the coefficient of $x^n$ in the power series $T(x)$ defined by
$$
T(x) = m\,x\,\bigl(1 + 2T(x)\bigr)^k. \tag{10.2}
$$

**Proof** A linear chain is a choice of monomer for each of the $n$ residues and, for each of the $n - 1$ bonds, of an anomeric configuration and an acceptor position: $m^n (2k)^{n-1}$. For branched chains, a glycan is its reducing-end residue ($m$ choices) together with, for each of the $k$ hydroxyls, either nothing or a bond (2 configurations) to a smaller glycan; this is the recursion (10.2) of the generating function. $\square$

With $m = 20$ and $k = 4$ (C-2, C-3, C-4 and C-6 of a hexopyranose), hexamers number $4^6 = 4096$ for nucleic acids, $20^6 = 6.4 \times 10^7$ for peptides, $2.1 \times 10^{12}$ for linear and $1.5 \times 10^{13}$ for branched oligosaccharides. Allowing in addition pyranose and furanose rings multiplies the count by $2^6$ and gives about $10^{15}$, close to the often-quoted estimate of $1.44 \times 10^{15}$ hexasaccharides by Laine (1994); sulfation and other substituents add further orders of magnitude.

![Possible oligomers of n residues (log scale): nucleic acids (4ⁿ), peptides (20ⁿ), and oligosaccharides from 20 monosaccharides with two anomeric configurations and four acceptor positions per bond, linear (Eq. (10.1)) and branched (Eq. (10.2)); numbers give the counts for hexamers (dashed line). The counts are upper bounds on what chemistry allows; real glycomes are restricted by the glycosyltransferases a cell expresses.](./plots/information-density.py)

The counts are upper bounds. Because glycans are not templated, a cell makes only the structures its set of glycosyltransferases can build, and a few thousand distinct glycan structures account for most of the human glycome. The density of information lies in another fact: each small glycan presents a distinct three-dimensional surface of hydroxyl groups, acetamido groups, carboxylates and hydrophobic patches, a "word" small enough to be read by a single **binding site**.

### 10.5.2. Lectins Read the Code

**Definition 10.5.2** A **lectin** is a protein that binds carbohydrates specifically and reversibly, without modifying them (it is neither an enzyme acting on the sugar nor an antibody).

Plant lectins, abundant in seeds, probably deter herbivores; purified lectins of known specificity are laboratory reagents for detecting, separating and profiling glycans. Animal lectins and the lectins of pathogens mediate the following processes.

| Lectin | Sugar it reads | Function |
|---|---|---|
| asialoglycoprotein receptor (hepatocytes) | terminal Gal or GalNAc exposed when sialic acid is lost | removal of aged plasma glycoproteins (ceruloplasmin) and erythrocytes; the circulating half-life of a protein depends on its terminal sialic acids |
| hepatocyte receptor for GalNAc4S(β1→4)GlcNAc | sulfated glycans of luteinizing hormone and thyrotropin | constant clearance that, with pulsatile secretion, makes the blood levels of these **hormones** pulse |
| mannose 6-phosphate receptor (trans Golgi) | Man6P on N-glycans of lysosomal hydrolases | sorting to lysosomes; the receptor releases its cargo at the low pH of the endosome, when a protonated Arg in the binding site loses the phosphate. Missing Man6P tags (I-cell disease) send the enzymes out of the cell instead |
| selectins (P, E, L) on endothelium and leukocytes | sialyl Lewis x, Neu5Ac(α2→3)Gal(β1→4)[Fuc(α1→3)]GlcNAc, on mucin-like **ligands** | fast-binding, fast-releasing contacts let leukocytes roll along the vessel wall at sites of inflammation before **integrins** arrest them; tumor cells that display sialyl Lewis x use the same pathway to metastasize |
| hemagglutinin of influenza virus | terminal sialic acid; human-adapted strains prefer α2→6, avian strains α2→3 linkages | attachment and entry; the viral neuraminidase cleaves sialic acids to release new virions, and the transition-state analogues oseltamivir and zanamivir inhibit it |
| BabA adhesin of *Helicobacter pylori* | Lewis b, Fuc(α1→2)Gal(β1→3)[Fuc(α1→4)]GlcNAc, of gastric epithelium | adhesion and colonization of the stomach, leading to gastritis and ulcers |
| cholera toxin, B subunit | ganglioside GM1 | entry of the toxin into intestinal cells |
| calnexin, calreticulin (ER) | monoglucosylated N-glycans | folding quality control (10.4.2) |

The specificity of influenza hemagglutinin for the linkage of sialic acid, α2→6 in the human upper airway and α2→3 in the bird gut, is a direct example of a glycosidic linkage acting as information: a few mutations in the receptor-binding site that switch the preference are among the changes needed for an avian virus to spread between humans.

### 10.5.3. Specificity and Multivalency

In their binding sites lectins make hydrogen bonds to the more polar face of a sugar ring (its hydroxyl groups and ring oxygen), often coordinate a hydroxyl to a $\ce{Ca^2+}$ or $\ce{Mn^2+}$ ion, and stack an aromatic **side chain** (often Trp) against the less polar face of the ring, which is formed by axial C–H bonds (an interaction driven by the **hydrophobic effect** and C–H···π contacts). This complementarity gives high specificity but modest affinity: **dissociation constants** of single carbohydrate-binding domains for their ligands are typically micromolar to millimolar.

Biology compensates with **multivalency**. Lectins are **oligomers** or carry several carbohydrate-binding domains, and glycans are clustered on cell surfaces, so several bonds form at once. The overall strength of such a multivalent interaction is called its avidity, to distinguish it from the affinity of one site.

**Formula 10.5.1 (Avidity of a divalent interaction)** Let one site bind its ligand with **dissociation constant** $K_{\mathrm{d}}$. Once the first site of a divalent lectin is bound, the second ligand of a divalent target is held near the second site at an effective concentration $c_{\mathrm{eff}}$ (set by the geometry and flexibility of the linkers). The second binding step then has the equilibrium constant $c_{\mathrm{eff}}/K_{\mathrm{d}}$, and the dissociation constant of the doubly bound complex is, apart from statistical factors of order 1,
$$
K_{\mathrm{d}}^{(2)} \approx \frac{K_{\mathrm{d}}^{2}}{c_{\mathrm{eff}}}. \tag{10.3}
$$

**Example 10.5.1** For $K_{\mathrm{d}} = 100\,\mathrm{\mu M}$ and $c_{\mathrm{eff}} = 10\,\mathrm{mM}$, Eq. (10.3) gives $K_{\mathrm{d}}^{(2)} \approx 10^{-8}/10^{-2} = 10^{-6}\,\mathrm{M}$: two weak contacts give one micromolar interaction, 100 times tighter than either. With $j$ sites the gain is of order $(c_{\mathrm{eff}}/K_{\mathrm{d}})^{j-1}$, so a pentavalent toxin such as cholera toxin, binding five GM1 molecules, adheres almost irreversibly. Multivalency also sharpens selectivity: a surface with a slightly lower density of ligand forms fewer simultaneous bonds and is bound far less, which is how leukocytes can distinguish inflamed from resting endothelium.

The same reasoning explains why selectin bonds suit rolling: each bond is weak and breaks within a fraction of a second under the shear force of blood flow, but new bonds form continuously at the leading edge of the cell, so the leukocyte is slowed without being stopped.

## 10.6. Working with Carbohydrates

Glycans are harder to analyse than proteins or nucleic acids: they are branched, their linkages vary, and they cannot be amplified or read from a template. The methods combine chemistry, enzymes and physical measurements.

- Release: N-glycans are cut from glycoproteins by peptide-N-glycosidase F (PNGase F) or endoglycosidase H (which cleaves only high-mannose and hybrid glycans and so reports whether a protein has passed through the Golgi); O-glycans are released chemically, by β-elimination in alkali or by hydrazinolysis.
- Composition and linkage: Acid hydrolysis gives the monosaccharides, quantified by chromatography; exhaustive methylation followed by hydrolysis leaves free hydroxyl groups exactly where the residues were linked; exoglycosidases of known specificity remove residues one at a time from the nonreducing ends.
- Structure: **Mass spectrometry** ([6.4.15](/6.4.15)) gives composition and, by fragmentation, sequence and branching; **nuclear magnetic resonance** ([6.4.12](/6.4.12)) gives anomeric configurations and linkage positions. Separation uses ion-exchange, size-exclusion and hydrophilic-interaction chromatography, and lectin affinity columns.
- Function: Glycan microarrays, of synthetic or purified glycans printed on slides, are probed with lectins, antibodies or whole viruses to map binding specificity; automated solid-phase synthesis now provides defined oligosaccharides and GAG fragments for such studies.

The systematic characterization of all glycans of a cell or tissue, including which proteins carry them and at which sites, is called glycomics.

## Summary

| Structural feature | Chemical property | Biological function |
|---|---|---|
| phosphate ester on a sugar (Glc6P) | negative charge, no plasma-membrane transporter | sugar trapped in the cell and activated for metabolism |
| free anomeric carbon (**reducing sugar**) | reacts with amino groups | glycation of hemoglobin, HbA1c as a 3-month glucose record (Definition 10.1.2) |
| both anomeric carbons bonded (sucrose, trehalose) | nonreducing, chemically inert | transport and stress-protection sugars |
| (α1→4) linkages, (α1→6) branches (Definition 10.3.2) | curved chain, helix, hydrated; many nonreducing ends | compact, rapidly mobilized fuel (starch, glycogen); one particle per molecule avoids osmotic lysis (Example 10.3.1) |
| (β1→4) linkages (Definition 10.3.3) | straight ribbons, interchain hydrogen bonds | insoluble fibers: cellulose, chitin |
| GlcNAc–MurNAc chains with D-amino-acid peptide cross-links (Definition 10.3.4) | one covalent mesh | bacterial cell wall; target of lysozyme and β-lactams |
| uronate carboxylates and sulfates (Definition 10.3.5) | high negative charge, extended chains, counterion cloud | hydrated, pressure-resisting matrix; specific protein binding by sulfation patterns (heparan sulfate) |
| N-glycans at Asn–X–Ser/Thr, O-glycans at Ser/Thr (Definition 10.4.3) | large, hydrophilic, branched | solubility, folding control, targeting (Man6P), half-life, recognition |
| terminal sugars of glycolipids and glycoproteins | small variations (one GalNAc or Gal; α2→3 vs α2→6 sialic acid) | blood groups, pathogen tropism, selectin ligands |
| many linkage positions, two anomers, branching (Proposition 10.5.1) | $\sim 10^{13}$–$10^{15}$ possible hexasaccharides | sugar code read by lectins (Definition 10.5.2) |
| clusters of weak lectin–glycan contacts (Formula 10.5.1) | avidity $K_{\mathrm{d}}^2/c_{\mathrm{eff}}$ | strong, selective, reversible cell adhesion (leukocyte rolling) |

| Quantity | Value |
|---|---|
| branch frequency | amylopectin every 24–30, glycogen every 8–12 residues |
| glycogen in fed liver | up to 7 % of wet mass; ≈ 0.4 M glucose equivalent as ≈ 10 µM β particles of ≈ 5 × 10⁴ residues |
| cellulose chain | 10 000–15 000 glucose residues |
| hyaluronan | up to 50 000 disaccharide repeats |
| aggrecan aggregate | ≈ 100 core proteins on one hyaluronan, $M_{\mathrm{r}} > 2 \times 10^8$ |
| HbA1c | ≈ 5 % normal, ≥ 6.5 % diabetic |
| glycosylated mammalian proteins | about half; 1 % to > 70 % carbohydrate by mass |
| hexamers possible | DNA $4.1 \times 10^3$, peptide $6.4 \times 10^7$, oligosaccharide $10^{13}$–$10^{15}$ |
| lectin single-site $K_{\mathrm{d}}$ | µM to mM |

## Questions

1. Amylose and cellulose are both polymers of D-glucose joined 1→4. Explain, starting from the configuration of C-1, why one is a digestible fuel and the other an indigestible fiber.

   **Answer** In amylose C-1 of each residue is α, in cellulose β. With rigid chair rings, the α linkage turns each ring about 60° relative to the previous one, so the chain curves into a helix whose hydroxyl groups remain exposed to water; the β linkage flips each ring by 180°, giving a straight ribbon in which hydroxyls form intrachain and interchain hydrogen bonds, so parallel chains pack into insoluble crystalline microfibrils. Digestion requires an enzyme whose active site fits the linkage: humans have α-amylases and α-glucosidases but no β-glucosidase that attacks cellulose, and the crystalline packing would in any case make most bonds inaccessible.
2. A liver cell contains glycogen equivalent to 0.4 M glucose. (a) Estimate the osmotic pressure this glucose would add at 37 °C if it were free. (b) If each glycogen particle contains $5 \times 10^4$ glucose residues, what is the molar concentration of particles, and what osmotic pressure do they exert? (c) Why do highly branched molecules suit an animal that must release glucose quickly?

   **Answer** (a) $\Pi = cRT = 400 \times 8.314 \times 310\,\mathrm{Pa} \approx 1.0\,\mathrm{MPa}$, more than the whole normal osmotic pressure of cytosol ($\approx 0.77\,\mathrm{MPa}$); the cell would swell and burst. (b) $0.4\,\mathrm{M}/(5 \times 10^4) = 8\,\mathrm{\mu M}$, so $\Pi = 8 \times 10^{-3}\,\mathrm{mol\,m^{-3}} \times 8.314 \times 310\,\mathrm{J\,mol^{-1}} \approx 21\,\mathrm{Pa}$, five orders of magnitude less. (c) Glycogen phosphorylase removes glucose only from nonreducing ends, and a molecule with $n$ branches has $n + 1$ such ends, so many enzyme molecules can work at once; the release rate scales with the number of ends, not with the mass.
3. Write the abbreviated names of lactose and sucrose and predict which reduces Fehling's solution and which can glycate proteins. Why do plants transport sucrose rather than glucose?

   **Answer** Lactose is Gal(β1→4)Glc: the glucose residue has a free anomeric carbon, so lactose is a reducing sugar and can react with amino groups. Sucrose is Glc(α1↔2β)Fru: both anomeric carbons form the glycosidic bond, so it is nonreducing and does not glycate. A nonreducing sugar can be carried at several hundred millimolar in phloem without reacting with proteins or being oxidized, and as a disaccharide it halves the osmotic cost per glucose unit compared with free hexoses; it is also not a substrate of most hexose-consuming enzymes along the way.
4. People of blood group A have anti-B antibodies and group B people anti-A. Using the structures of the H, A and B antigens, explain why group O red cells can be transfused into recipients of any ABO group, and why an O recipient cannot receive A or B cells. What enzymatic treatment could convert A red cells into "universal" cells?

   **Answer** All three antigens share the H structure Fuc(α1→2)Gal(β1→4)GlcNAc-R; A adds GalNAc(α1→3), B adds Gal(α1→3) to the galactose. Group O cells carry only H, which every person makes and tolerates (except the rare Bombay phenotype, which lacks the fucosyltransferase), so no anti-A or anti-B antibody binds them. An O individual lacks both transferases and makes antibodies against both A and B, which would agglutinate A or B cells and activate complement. Removing the terminal α-GalNAc (an α-N-acetylgalactosaminidase) or α-Gal (an α-galactosidase) from the cell surface converts A or B cells into H (O) cells; bacterial enzymes that do this efficiently have been found and are being developed for blood banking.
5. Influenza neuraminidase inhibitors are sugar analogs. Why does inhibiting an enzyme that removes sialic acid stop the spread of the virus, although the virus binds to sialic acid to enter cells?

   **Answer** Hemagglutinin binds sialic acid for attachment and entry, but newly budded virions are covered with sialylated host glycoproteins and are surrounded by sialic acid on the cell surface; without neuraminidase they remain stuck to the producing cell and to one another by their own hemagglutinin. The neuraminidase cleaves the terminal sialic acids so that progeny can leave and spread. Oseltamivir and zanamivir mimic the oxocarbenium-ion transition state of sialic acid hydrolysis and bind the active site competitively; virions are released poorly and aggregate, which limits the infection. Resistance arises from mutations (such as His → Tyr near the site) that prevent the inhibitor from inducing the rearrangement of a Glu residue it needs to bind.
6. A trivalent lectin binds a cluster of three glycans. Each single site has $K_{\mathrm{d}} = 1\,\mathrm{mM}$, and the effective concentration of a neighbouring glycan after the first contact is $c_{\mathrm{eff}} = 5\,\mathrm{mM}$. Estimate the dissociation constant of the trivalent complex and discuss what happens if the glycan spacing on the cell is too large for the lectin to bridge.

   **Answer** Each additional bond contributes a factor $c_{\mathrm{eff}}/K_{\mathrm{d}} = 5$, so $K_{\mathrm{d}}^{(3)} \approx K_{\mathrm{d}}^3/c_{\mathrm{eff}}^2 = 10^{-9}/(2.5 \times 10^{-5})\,\mathrm{M} = 4 \times 10^{-5}\,\mathrm{M} = 40\,\mathrm{\mu M}$, 25 times tighter than one site. If the spacing cannot be bridged, $c_{\mathrm{eff}} \to 0$ for the second and third contacts, the complex is monovalent and $K_{\mathrm{d}}$ stays at 1 mM; the strong dependence on spacing and density is what lets multivalent lectins discriminate surfaces by ligand density.
