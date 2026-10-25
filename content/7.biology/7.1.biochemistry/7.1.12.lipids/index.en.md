---
title: Lipids
description: Lipids classified by function. Fatty acids, their nomenclature and how chain length and double bonds set melting points; triacylglycerols as the most concentrated fuel store and waxes; membrane lipids (glycerophospholipids, ether lipids, galactolipids, archaeal ether lipids, sphingolipids, sterols) and their lysosomal degradation; lipids as signals, cofactors and pigments (phosphoinositides, eicosanoids, steroid hormones, fat-soluble vitamins, quinones, dolichols, carotenoids, polyketides); extraction and analysis of lipids.
---

Lipids are defined not by a common structure but by a common property: they are insoluble in water and soluble in nonpolar organic solvents. Their biological roles are as varied as their chemistry. Fats and oils are the main long-term fuel of most organisms; phospholipids, glycolipids and sterols form the barrier of every biological membrane; and other lipids, present in small amounts, are hormones, intracellular messengers, electron carriers, light-absorbing pigments, membrane anchors for proteins and carriers of sugars. Following the thread of Part I (7.1.1), this chapter relates each of these roles to the chemistry behind it: the reduced, anhydrous hydrocarbon chain makes fat the most concentrated fuel; the length and the cis double bonds of a chain set how tightly it packs and hence how fluid a membrane is; and the combination of a polar head with two nonpolar tails makes membrane lipids **amphiphiles** that assemble spontaneously into bilayers (the physical chemistry of amphiphile assembly is treated in [6.3.19](/6.3.19)).

The organic chemistry of esters and fats, including saponification, is in [6.5.19](/6.5.19). The next chapter (7.1.13) builds membranes from the lipids described here; the oxidation of fatty acids follows in 7.1.21 and the biosynthesis of fatty acids, eicosanoids, membrane lipids, cholesterol and steroid hormones in 7.1.26.

## 12.1. Classification

**Definition 12.1.1** A **lipid** is a biological molecule that is insoluble or poorly soluble in water and extractable by nonpolar organic solvents such as chloroform, ether or hexane.

Chemically, most lipids are fatty acids or contain fatty acids esterified or amide-linked to an alcohol (glycerol, sphingosine, a long-chain alcohol), or they are isoprenoids, built from five-carbon isoprene units (sterols, carotenoids, fat-soluble vitamins, quinones). Biochemistry textbooks classify lipids by function; the LIPID MAPS classification used in lipidomics divides them by chemistry into eight categories (fatty acyls, glycerolipids, glycerophospholipids, sphingolipids, sterol lipids, prenol lipids, saccharolipids, polyketides).

![Lipids classified by function. Storage lipids (triacylglycerols and waxes) are the bulk of an adipocyte. Membrane lipids, 5–10 % of the dry mass of most cells, are subdivided by their backbone (glycerol or sphingosine), the link to the tails (ester or ether) and the head group. A third group, present in small amounts, acts as signals, enzyme cofactors and pigments; most of its members are isoprenoids or derived from polyunsaturated fatty acids.](./plots/lipid-classes.py)

## 12.2. Fatty Acids

### 12.2.1. Structure and Nomenclature

**Definition 12.2.1** A **fatty acid** is a carboxylic acid with an unbranched hydrocarbon chain of 4 to 36 carbon atoms. A fatty acid is **saturated** if the chain has no carbon–carbon double bond and **unsaturated** if it has one (monounsaturated) or more (polyunsaturated).

The shorthand gives the number of carbons, the number of double bonds, and the positions of the double bonds counted from the carboxyl carbon (C-1) by the lower-numbered carbon of each double bond, written with Δ: oleic acid is 18:1(Δ⁹), α-linolenic acid 18:3(Δ⁹,¹²,¹⁵). In nutrition the position of the double bond nearest the methyl (ω) end is used instead: α-linolenic acid, eicosapentaenoic acid (EPA, 20:5(Δ⁵,⁸,¹¹,¹⁴,¹⁷)) and docosahexaenoic acid (DHA, 22:6) are ω-3 fatty acids, linoleic and arachidonic acid ω-6 fatty acids.

Natural fatty acids follow three regularities, each with a biochemical cause:

- Most have an even number of carbons, 12 to 24, because they are built from two-carbon units (7.1.26).
- In monounsaturated acids the double bond is usually Δ⁹; further double bonds are at Δ¹² and Δ¹⁵ and are separated by a methylene group, $\ce{-CH=CH-CH2-CH=CH-}$, rarely conjugated. This reflects the specificity of the desaturases that make them; mammals lack Δ¹² and Δ¹⁵ desaturases and so require linoleic and α-linolenic acid in the diet (essential fatty acids, 7.1.26).
- Almost all natural double bonds are cis. Trans fatty acids occur naturally in small amounts in ruminant fat (made by rumen bacteria) and are formed in large amounts by industrial partial hydrogenation (12.2.3).

| Shorthand | Common name | Melting point / °C | Typical sources |
|---|---|---|---|
| 12:0 | lauric | 44.2 | coconut and palm-kernel oil |
| 14:0 | myristic | 53.9 | milk fat, nutmeg |
| 16:0 | palmitic | 63.1 | palm oil, animal fat; the main product of fatty acid synthase |
| 18:0 | stearic | 69.6 | beef fat, cocoa butter |
| 20:0 | arachidic | 76.5 | peanut oil |
| 24:0 | lignoceric | 86.0 | sphingolipids of brain myelin |
| 16:1(Δ⁹) | palmitoleic | about 0.5 | fish oils, animal fat |
| 18:1(Δ⁹) | oleic | 13.4 | olive oil (about 70 %), most fats |
| 18:2(Δ⁹,¹²) | linoleic (ω-6) | 1 to 5 | sunflower, soybean, corn oil |
| 18:3(Δ⁹,¹²,¹⁵) | α-linolenic (ω-3) | −11 | linseed, rapeseed (canola) oil, leaves |
| 20:4(Δ⁵,⁸,¹¹,¹⁴) | arachidonic (ω-6) | −49.5 | membrane phospholipids of animals; precursor of eicosanoids |

### 12.2.2. Chain Length, Double Bonds and Packing

The physical properties of fatty acids, and of every lipid that contains them, are set by the length and saturation of the chain. A longer chain has lower solubility in water (lauric acid dissolves to $0.063\,\mathrm{mg\,g^{-1}}$, glucose of similar molecular mass to $1100\,\mathrm{mg\,g^{-1}}$) and a higher melting point. A cis double bond lowers the melting point sharply.

The cause is packing. In a saturated chain free rotation about every C–C bond allows the fully extended all-trans zigzag, the conformation of lowest energy, and extended chains pack side by side in nearly crystalline arrays held by **van der Waals forces** along their whole length; each additional CH₂ adds contact surface and raises the melting point. A cis double bond is rigid and bends the chain by about 30°; bent chains cannot pack tightly, the aggregate is held together more weakly, and less thermal energy is needed to disorder it. A trans double bond leaves the chain nearly straight, so elaidic acid (trans-18:1(Δ⁹)) melts at about 45 °C, much closer to stearic (69.6 °C) than to oleic acid (13.4 °C).

![Melting points of fatty acids. A: saturated fatty acids, from lauric (12:0) to lignoceric acid (24:0); every two carbons raise the melting point by 6–10 °C. B: C18 fatty acids with zero to three cis double bonds (linoleic acid, given as 1–5 °C, drawn as a range): the first cis double bond lowers the melting point by more than 55 °C; elaidic acid, the trans isomer of oleic acid, melts at about 45 °C; arachidonic acid (20:4) is liquid down to −49.5 °C. The dashed line is body temperature.](./plots/fatty-acid-melting.py)

![Packing of fatty acid chains (schematic). A: saturated chains (stearate) are fully extended and pack in nearly crystalline order, in van der Waals contact along their whole length. B: the cis double bond at C-9 of oleate (red) puts a rigid bend into the chain, so that chains mixed with it cannot pack tightly; this is why oils rich in unsaturated fatty acids are liquid at room temperature, and why membranes stay fluid when their lipids carry cis-unsaturated chains (7.1.13).](./plots/chain-packing.py)

The same rule explains the state of natural fats, which are mixtures of triacylglycerols: olive oil, rich in oleate, is liquid at room temperature; butter, with more palmitate and stearate, is soft; beef fat, mostly saturated, is hard. Cells use it to keep their membranes fluid: bacteria and poikilothermic animals grown in the cold make more unsaturated and shorter fatty acids (homeoviscous adaptation, 7.1.13), and the fat in the extremities of cold-water animals is more unsaturated than in their core.

### 12.2.3. Hydrogenation, Trans Fats and Engineered Oils

Unsaturated fats spoil in air: oxygen cleaves the double bonds by radical chain reactions, giving volatile aldehydes and short acids with the smell of rancidity. Industrial partial hydrogenation, used through the twentieth century to make vegetable oils more stable and more solid (margarine, shortening, deep-frying fats), removes double bonds but also isomerizes some of the remaining cis double bonds to trans. Dietary trans fatty acids raise plasma LDL cholesterol and triacylglycerols, lower HDL cholesterol (lipoproteins, 7.1.26) and promote inflammation; they are a well-established risk factor for coronary heart disease. Many countries now limit or prohibit partially hydrogenated oils (the United States since 2018), and the World Health Organization has called for their global elimination.

Fatty acid composition can also be changed genetically. Overexpressing a Δ⁹ acyl-CoA desaturase, which introduces the first double bond into palmitate and stearate, in rapeseed (canola) lowered the saturated fatty acids of the seed oil; other engineered and bred oilseeds produce high-oleic oils (by suppressing the Δ¹² desaturase *FAD2*), which are stable without hydrogenation, or the ω-3 acids EPA and DHA normally obtained from fish.

## 12.3. Storage Lipids

### 12.3.1. Triacylglycerols

**Definition 12.3.1** A **triacylglycerol** (triglyceride, neutral fat) is the triester of glycerol with three fatty acids. A simple triacylglycerol contains one kind of fatty acid (tripalmitin, tristearin, triolein), a mixed one two or three kinds; most natural triacylglycerols are mixed, and when C-1 and C-3 carry different fatty acids C-2 is a chiral centre.

```smiles
CCCCCCCCCCCCCCCC(=O)OCC(COC(=O)CCCCCCCCCCCCCCC)OC(=O)CCCCCCCCCCCCCCC tripalmitin
```

The ester bonds remove the polar groups of both glycerol and the fatty acids, so triacylglycerols are nonpolar, essentially insoluble in water, and less dense than water. In most eukaryotic cells they form a separate phase of lipid droplets in the cytosol, coated by a phospholipid monolayer and proteins (perilipins); in vertebrate adipocytes a single droplet fills almost the whole cell, and in seeds oil bodies supply energy and carbon for germination (7.1.25). Lipases release the fatty acids when they are needed (7.1.21, 7.1.29).

### 12.3.2. Why Fat Is the Long-Term Fuel

Fat has two advantages over polysaccharides as a fuel store, and both follow from its chemistry.

- More energy per carbon: fatty acid carbons are more reduced. The average oxidation number of carbon is −1.75 in palmitic acid ($\ce{C16H32O2}$) and 0 in glucose ($\ce{C6H12O6}$), so complete oxidation of palmitate releases about $39\,\mathrm{kJ\,g^{-1}}$ (standard enthalpy of combustion about $-10\,000\,\mathrm{kJ\,mol^{-1}}$ for $M = 256\,\mathrm{g\,mol^{-1}}$) and that of glucose $15.6\,\mathrm{kJ\,g^{-1}}$ ($-2803\,\mathrm{kJ\,mol^{-1}}$ for $180\,\mathrm{g\,mol^{-1}}$; **standard molar enthalpy of combustion**, [6.1.6](/6.1.6)). In nutrition these are rounded to $37\,\mathrm{kJ\,g^{-1}}$ for fat and $17\,\mathrm{kJ\,g^{-1}}$ for carbohydrate and protein.
- No water: triacylglycerols are anhydrous, whereas glycogen is stored with about 2 g of water per gram.

**Example 12.3.1** A 70 kg adult stores about $400\,000\,\mathrm{kJ}$ as fat (about 11 kg of triacylglycerol), $100\,000\,\mathrm{kJ}$ as protein that can be mobilized (mainly muscle), and only about $2500\,\mathrm{kJ}$ as glycogen in liver and muscle. At a resting energy expenditure of about $8000\,\mathrm{kJ\,d^{-1}}$, the glycogen covers less than a day, the fat about 50 days. Hydrated glycogen stores about $17/3 \approx 6\,\mathrm{kJ}$ per gram of stored mass, so storing $400\,000\,\mathrm{kJ}$ as glycogen would require about $70\,\mathrm{kg}$, the mass of the whole body, instead of $11\,\mathrm{kg}$ of fat.

![Fuel reserves. A: energy released on complete oxidation per gram of stored material; because glycogen is stored with about 2 g of water per gram, hydrated glycogen yields only about 6 kJ per gram of stored mass, against 37 kJ for anhydrous triacylglycerol. B: the fuel reserves of a 70 kg adult (logarithmic scale) and the time each would last at a resting expenditure of 8000 kJ per day.](./plots/fuel-reserves.py)

Glycogen has the opposite advantages: it can be mobilized very fast, its glucose can be used without oxygen (glycolysis, 7.1.18), and the brain can use glucose but not fatty acids; the two stores therefore complement each other (7.1.29). In many animals subcutaneous fat also provides thermal insulation (seals, whales and penguins) and, in hibernating mammals, months of fuel.

### 12.3.3. Waxes

**Definition 12.3.2** A biological **wax** is an ester of a long-chain (C14–C36) saturated or unsaturated fatty acid with a long-chain (C16–C30) alcohol.

Waxes melt at 60–100 °C, higher than triacylglycerols, and are firm and water-repellent at body temperature. In marine plankton they are the main fuel store; beeswax (mainly triacontanyl palmitate) builds the honeycomb; the cuticular waxes of leaves limit evaporation and protect against pathogens and insects; vertebrate skin glands and the preen glands of water birds secrete waxes that keep hair and feathers pliable and waterproof. Lanolin, beeswax, carnauba and jojoba waxes are used in lotions, ointments and polishes.

## 12.4. Structural Lipids in Membranes

The central feature of biological membranes is a lipid bilayer, a barrier to polar molecules and ions (7.1.13). Its lipids are amphipathic: a polar head group and nonpolar tails, which in water associate with each other, driven by the **hydrophobic effect**, while the heads face the water. Four groups of membrane lipids differ in their backbone and in how the tails are attached.

| Group | Backbone | Tails | Head group | Where |
|---|---|---|---|---|
| glycerophospholipids | sn-glycerol 3-phosphate | two fatty acids (ester), or one ether-linked chain | alcohol in phosphodiester | all cellular membranes |
| galactolipids, sulfolipids | glycerol | two fatty acids (ester) | galactose(s) or sulfoquinovose, glycosidic | thylakoids of chloroplasts |
| archaeal ether lipids | sn-glycerol 1-phosphate | isoprenoid chains (ether) | phosphate esters and sugars | archaea |
| sphingolipids | sphingosine | sphingosine chain + one fatty acid (amide) | phosphocholine or sugars | plasma membranes of animals and plants, myelin |
| sterols | steroid nucleus | rigid ring system + side chain | 3-OH | eukaryotic membranes |

### 12.4.1. Glycerophospholipids

**Definition 12.4.1** A **glycerophospholipid** (phosphoglyceride) is a membrane lipid in which two fatty acids are esterified to C-1 and C-2 of sn-glycerol 3-phosphate and a polar alcohol is joined to the phosphate by a phosphodiester bond. The parent compound, without the alcohol, is **phosphatidic acid**; the others are named after the head-group alcohol with the prefix phosphatidyl-.

Glycerol is prochiral, and phospholipids contain only one enantiomer of glycerol phosphate, named sn-glycerol 3-phosphate (stereospecific numbering; it is L-glycerol 3-phosphate, and its C-2 is $R$). In general C-1 carries a saturated C16 or C18 fatty acid and C-2 an unsaturated C18 or C20 fatty acid, so each head-group class consists of many molecular species.

| Glycerophospholipid | Head-group alcohol | Net charge at pH 7 | Notes |
|---|---|---|---|
| phosphatidic acid | none | about −1.5 | intermediate of phospholipid and triacylglycerol synthesis |
| phosphatidylethanolamine | ethanolamine | 0 | inner leaflet of plasma membrane; main phospholipid of *E. coli* |
| phosphatidylcholine (lecithin) | choline | 0 | major phospholipid of eukaryotic membranes, outer leaflet |
| phosphatidylserine | serine | −1 | inner leaflet; exposed on the surface of apoptotic cells as an "eat me" signal |
| phosphatidylglycerol | glycerol | −1 | bacteria, thylakoids, lung surfactant |
| phosphatidylinositol (PI) | myo-inositol | −1 | precursor of the phosphoinositide signals (12.5.1) |
| PI 4,5-bisphosphate | myo-inositol 4,5-bisphosphate | about −4 | inner leaflet; source of IP₃ and DAG |
| cardiolipin (diphosphatidylglycerol) | phosphatidylglycerol | −2 | bacterial membranes and the inner mitochondrial membrane, which reflects the bacterial origin of mitochondria |

```smiles
CCCCCCCCCCCCCCCC(=O)OC[C@H](COP(=O)([O-])OCC[N+](C)(C)C)OC(=O)CCCCCCCCCCCCCCC PC
```

The structure above is 1,2-dipalmitoyl-sn-glycero-3-phosphocholine (DPPC), the main component of lung surfactant, which lowers the surface tension of the alveoli; premature infants who do not yet make enough of it develop respiratory distress syndrome.

**Definition 12.4.2** Ether lipids are glycerophospholipids in which one chain (at C-1) is attached to glycerol by an ether rather than an ester bond. In **plasmalogens** the ether-linked chain has a cis double bond between C-1 and C-2 (a vinyl ether).

About half of the phospholipids of vertebrate heart are plasmalogens, and halophilic bacteria, ciliates and some invertebrates are rich in ether lipids; their resistance to phospholipases may be part of their function, and the vinyl ether of plasmalogens reacts readily with oxidants, which may protect other lipids. Platelet-activating factor (PAF), with an ether-linked alkyl chain at C-1, an acetyl group at C-2 and phosphocholine, is a potent signal: released by basophils and other leukocytes, it aggregates platelets and mediates inflammation and anaphylaxis at nanomolar concentrations.

### 12.4.2. Galactolipids and Sulfolipids

The thylakoid membranes of chloroplasts consist mainly of glycolipids: monogalactosyl- and digalactosyldiacylglycerol (MGDG, DGDG), in which one or two galactose residues are glycosidically linked to C-3 of a 1,2-diacylglycerol, with polyunsaturated acyl chains (mainly 18:3), and the anionic sulfolipid sulfoquinovosyldiacylglycerol (SQDG), whose sulfonated glucose carries a negative charge like a phosphate. These lipids make up 70–80 % of the membrane lipids of vascular plants and are probably the most abundant membrane lipids on Earth. Phosphate is often the limiting nutrient in soil, and using sugars and sulfonate instead of phosphate as head groups conserves it; under phosphate starvation plants replace even some of their extraplastidic phospholipids by DGDG.

### 12.4.3. Archaeal Ether Lipids

Archaea build their membranes from a distinct chemistry. Their chains are isoprenoids (phytanyl, C20, or biphytanyl, C40: a 32-carbon backbone with eight methyl branches), attached to glycerol by ether bonds, and the glycerol has the opposite configuration (sn-glycerol 1-phosphate). In the tetraether lipids of many thermophiles and acidophiles each biphytanyl chain is ether-linked to a glycerol at both ends, so that one molecule spans the membrane and forms a monolayer. Ether bonds resist hydrolysis at high temperature and low pH far better than esters, methyl branches and cyclopentane rings in the chains reduce permeability and keep the membrane in a suitable state, and the spanning molecules cannot separate into two leaflets; these lipids allow archaea to live in boiling springs, acid mine drainage and saturated brines. The difference in glycerol stereochemistry between archaea and bacteria (the "lipid divide") is one of the deepest in biology.

### 12.4.4. Sphingolipids

**Definition 12.4.3** **Sphingolipids** are membrane lipids built on sphingosine (a C18 amino alcohol with a trans double bond, (2S,3R,4E)-2-aminooctadec-4-ene-1,3-diol) instead of glycerol. A fatty acid in amide linkage to the C-2 amino group gives a **ceramide**, the parent of all sphingolipids; they differ in the head group attached to C-1. **Sphingomyelins** carry phosphocholine (or phosphoethanolamine), **cerebrosides** one sugar, globosides two or more neutral sugars, and **gangliosides** an oligosaccharide with one or more sialic acid residues.

```smiles
CCCCCCCCCCCCC/C=C/[C@H]([C@H](COP(=O)([O-])OCC[N+](C)(C)C)NC(=O)CCCCCCCCCCCCCCC)O sphingomyelin
```

C-1 to C-3 of sphingosine correspond to the three carbons of glycerol, and its hydrocarbon chain plays the role of the second fatty acid; the fatty acid of sphingolipids is usually saturated or monounsaturated with 16–24 carbons. Sphingomyelin therefore resembles phosphatidylcholine in shape and charge (both zwitterionic), but its amide and hydroxyl groups can donate hydrogen bonds, and its long saturated chains pack well with cholesterol, which makes it a main component of ordered membrane domains (lipid rafts, 7.1.13) and of myelin, the multilayered membrane that insulates axons.

The glycosphingolipids face the outside of the plasma membrane, where their glycans are recognition sites. Cerebrosides with galactose are typical of neural tissue, those with glucose of other tissues. Gangliosides are named by their number of sialic acids (GM, GD, GT, GQ for 1–4) and their oligosaccharide (GM1, GM2, …); their composition changes during development and in tumors. Cholera toxin enters intestinal cells after binding to GM1, and in Guillain–Barré syndrome antibodies against bacterial glycans cross-react with gangliosides of peripheral nerves and cause paralysis. The ABO blood-group antigens are carried by glycosphingolipids as well as by glycoproteins (7.1.10).

### 12.4.5. Degradation and Storage Diseases

Membrane lipids turn over continuously. Phospholipases of the A type remove one fatty acid ($\mathrm{A_1}$ at C-1, $\mathrm{A_2}$ at C-2), leaving a lysophospholipid; phospholipase C cleaves the bond between glycerol and phosphate, and phospholipase D that between phosphate and the head group. Sphingolipids are degraded in lysosomes by hydrolases that remove the sugars one by one from the nonreducing end down to ceramide. A defect in one of these enzymes causes the partially degraded lipid to accumulate in lysosomes (more than 50 lysosomal storage diseases are known).

| Disease | Missing enzyme | Accumulating lipid | Main features |
|---|---|---|---|
| Tay–Sachs disease | hexosaminidase A | ganglioside GM2 | neurodegeneration, blindness, death in early childhood |
| Sandhoff disease | hexosaminidases A and B | GM2 and globoside | as Tay–Sachs, with organ involvement |
| GM1 gangliosidosis | β-galactosidase | GM1 | neurodegeneration, skeletal defects |
| Niemann–Pick disease (types A, B) | sphingomyelinase | sphingomyelin | enlarged liver and spleen; neurodegeneration in type A |
| Gaucher disease | glucocerebrosidase | glucosylceramide | enlarged liver and spleen, bone lesions; treated by enzyme replacement |
| Fabry disease | α-galactosidase A | globotriaosylceramide | pain, kidney and heart failure (X-linked) |
| Krabbe disease | galactocerebrosidase | galactosylceramide | loss of myelin |

Tay–Sachs disease is common enough in some populations that carrier screening of prospective parents, followed by DNA testing and prenatal diagnosis, has reduced its incidence by more than 90 % in those communities.

### 12.4.6. Sterols

**Definition 12.4.4** **Sterols** are lipids with the steroid nucleus, four fused rings (three six-membered and one five-membered, labelled A–D), and a hydroxyl group at C-3. **Cholesterol** is the main sterol of animal tissues; plants contain stigmasterol and sitosterol, and fungi ergosterol.

```smiles
C[C@H](CCCC(C)C)[C@H]1CC[C@@H]2[C@@]1(CC[C@H]3[C@H]2CC=C4[C@@]3(CC[C@@H](C4)O)C)C cholesterol
```

The steroid nucleus is nearly planar and rigid; with the 3-OH as a small polar head and the hydrocarbon side chain at C-17, cholesterol is amphipathic and about as long as a C16 fatty acid in its extended form. In a membrane it inserts between the phospholipids, its rigid rings ordering the neighbouring acyl chains and its bulk preventing them from crystallizing, so it makes fluid membranes less fluid and ordered membranes less ordered (7.1.13). Bacteria cannot make sterols; many use hopanoids, pentacyclic isoprenoids made without oxygen, in a similar role. All sterols are synthesized from isoprene units (7.1.26).

Sterols are also precursors. Cholesterol is stored and transported as cholesteryl esters (with a fatty acid on the 3-OH) in lipid droplets and lipoproteins.

**Definition 12.4.5** **Bile acids** are polar derivatives of cholesterol made in the liver, with hydroxyl groups on one face of the steroid nucleus and a shortened side chain ending in a carboxylate (cholate, chenodeoxycholate); conjugated with taurine or glycine they are the bile salts.

Bile acids act as detergents in the intestine, emulsifying dietary fat into **micelles** accessible to pancreatic lipase, and their excretion is the main route by which the body eliminates cholesterol. Steroid hormones are treated in 12.5.3.

## 12.5. Lipids as Signals, Cofactors and Pigments

Storage and membrane lipids are present in large amounts and are largely passive. A third group, present in small quantities, plays active roles: as hormones carried in the blood, as intracellular messengers, as cofactors of electron transfer and glycosylation, and as pigments that absorb visible light.

### 12.5.1. Phosphoinositides and Sphingolipid Messengers

Phosphatidylinositol 4,5-bisphosphate (PIP₂) in the cytoplasmic leaflet of the plasma membrane is a reservoir of two messengers. Hormones such as vasopressin activate a phospholipase C that hydrolyses PIP₂ into inositol 1,4,5-trisphosphate (IP₃), which is water-soluble, diffuses to the endoplasmic reticulum and releases $\ce{Ca^2+}$, and diacylglycerol (DAG), which stays in the membrane and, with $\ce{Ca^2+}$, activates protein kinase C (7.1.14). Phosphorylation of PIP₂ at the 3-position by phosphoinositide 3-kinase gives PIP₃, a docking site that assembles signalling complexes at the membrane, for example in insulin signalling (7.1.15). Each phosphoinositide marks a different membrane (PI4P the Golgi, PI3P early endosomes), so they also act as an address code for membrane traffic (7.3). Sphingolipids give messengers too: ceramide regulates protein kinases and phosphatases in stress responses and apoptosis, and sphingosine 1-phosphate, exported to the blood, controls lymphocyte trafficking through its G protein–coupled receptors (the drug fingolimod, used for multiple sclerosis, targets them).

### 12.5.2. Eicosanoids

**Definition 12.5.1** **Eicosanoids** are signalling molecules derived from C20 polyunsaturated fatty acids, mainly arachidonate (20:4(Δ⁵,⁸,¹¹,¹⁴)) and EPA. The four main classes are the **prostaglandins** (with a five-membered ring), the thromboxanes (with a six-membered ring containing an ether oxygen), the leukotrienes (linear, with three conjugated double bonds) and the lipoxins (linear, with several hydroxyl groups).

Eicosanoids are paracrine hormones: they are made on demand from arachidonate released from membrane phospholipids by phospholipase $\mathrm{A_2}$, act on cells near the site of synthesis through G protein–coupled receptors, and are rapidly inactivated.

| Class | Made by | Effects |
|---|---|---|
| prostaglandins (PGE₂, PGI₂, PGF₂α) | most cells, via cyclooxygenase (COX-1 constitutive, COX-2 induced in inflammation) | fever, pain and inflammation; uterine contraction in menstruation and labour; blood flow; protection of the gastric mucosa; prostacyclin (PGI₂) from endothelium inhibits platelet aggregation |
| thromboxanes (TXA₂) | platelets, via COX-1 | platelet aggregation and vasoconstriction at a clot |
| leukotrienes (LTB₄, LTC₄, LTD₄) | leukocytes, via 5-lipoxygenase | chemotaxis; LTC₄ and LTD₄ contract bronchial smooth muscle (asthma, anaphylaxis) |
| lipoxins | leukocytes and platelets in sequence | resolution of inflammation |

Pharmacology follows from the pathway. Nonsteroidal anti-inflammatory drugs (NSAIDs) inhibit cyclooxygenase: ibuprofen and most others reversibly, aspirin irreversibly by acetylating a Ser residue in the channel of the active site. Because platelets have no nucleus and cannot make new enzyme, a low daily dose of aspirin suppresses platelet thromboxane for their whole lifetime while endothelial cells resynthesize COX and continue to make prostacyclin; this is the basis of aspirin's use in preventing heart attack and stroke. Aspirin-acetylated COX-2 also makes precursors of anti-inflammatory lipoxins. Selective COX-2 inhibitors spare the gastric mucosa but raise cardiovascular risk, because they reduce prostacyclin without reducing platelet thromboxane. Corticosteroids such as prednisone reduce the formation of all eicosanoids, in part by suppressing the release of arachidonate and the induction of COX-2; leukotriene receptor antagonists (montelukast) and 5-lipoxygenase inhibitors are used against asthma. The synthesis of eicosanoids is described in 7.1.26.

### 12.5.3. Steroid Hormones and Plant Lipid Signals

**Definition 12.5.2** **Steroid hormones** are oxidized derivatives of sterols that have lost the alkyl side chain at C-17 (or most of it); they are more polar than cholesterol and act as hormones carried by the blood.

Steroid hormones travel bound to carrier proteins, enter target cells by diffusion and bind intracellular receptors (nuclear receptors, 7.1.15) that regulate transcription; because their affinity is very high, nanomolar or lower concentrations are effective. The adrenal cortex makes cortisol (glucose metabolism, stress, suppression of inflammation and immunity) and aldosterone (salt and water balance by the kidney); the gonads make testosterone and estradiol, which govern sexual development and the secondary sex characteristics; progesterone maintains pregnancy. Synthetic analogues are among the most widely used drugs (prednisone and dexamethasone; contraceptives), and anabolic steroids are prohibited in sport.

Plants have steroid hormones too, the brassinosteroids such as brassinolide, which promote cell elongation and division; mutants that cannot make them are dwarfs with dark, curled leaves, as described for *Arabidopsis*, rice and grape. Unlike animal steroid hormones they are perceived at the cell surface, by the receptor kinase BRI1 (7.1.15). Jasmonate, derived from α-linolenate (18:3) of membrane lipids, triggers defences against insects that chew leaves; jasmonate-deficient tomato mutants are eaten far more by caterpillars. Its volatile methyl ester (the fragrance of jasmine) and thousands of other volatiles, many of them isoprenoids such as geraniol, limonene, β-pinene and menthol, attract pollinators and the predators of herbivores, repel herbivores and signal to neighbouring plants.

### 12.5.4. Isoprenoids: Vitamins, Quinones, Dolichols and Pigments

**Definition 12.5.3** **Isoprenoids** (terpenoids) are compounds built from five-carbon isoprene units ($\ce{CH2=C(CH3)-CH=CH2}$ skeleton), linked head to tail; they include sterols, carotenoids, the fat-soluble vitamins A, D, E and K, ubiquinone and plastoquinone, dolichols, and many plant volatiles.

The fat-soluble vitamins are essential to vertebrates, which cannot make them; they are absorbed with dietary fat and stored in the liver and fatty tissues, so deficiency develops slowly and excess (of A and D) can be toxic.

| Vitamin | Active form and function | Deficiency |
|---|---|---|
| D₃ (cholecalciferol) | made in skin from 7-dehydrocholesterol by UV light; hydroxylated at C-25 in the liver and at C-1α in the kidney to the hormone 1α,25-dihydroxyvitamin D₃ (calcitriol), which acts through a nuclear receptor on calcium absorption in the intestine and calcium handling by kidney and bone. D₂ (ergocalciferol), from UV-irradiated ergosterol, is equivalent | rickets in children, osteomalacia in adults |
| A (retinol) | oxidized to retinal, which bound to opsin forms rhodopsin (light converts 11-cis- to all-trans-retinal, the primary event of vision, 7.1.14), and to retinoic acid, a hormone acting through nuclear receptors (RAR, RXR) in development, differentiation and immunity; made from dietary β-carotene | night blindness, dry eyes and skin, susceptibility to infection; xerophthalmia and child mortality in poor countries |
| E (tocopherols) | lipid-soluble antioxidants in membranes and lipoproteins: the phenolic ring reduces lipid peroxyl radicals and stops the chain oxidation of polyunsaturated fatty acids | rare; fragile erythrocytes, neuropathy |
| K (K₁ phylloquinone of plants, K₂ menaquinones of bacteria) | cofactor of the γ-glutamyl carboxylase that converts Glu to γ-carboxyglutamate in prothrombin and other clotting factors, which lets them bind $\ce{Ca^2+}$ and phospholipid surfaces; the vitamin is regenerated by vitamin K epoxide reductase | bleeding; hemorrhagic disease of the newborn, prevented by an injection of vitamin K at birth |

Warfarin, first used as a rat poison, inhibits vitamin K epoxide reductase and is one of the most widely used oral anticoagulants; its dose varies with variants of the reductase gene *VKORC1* and of the cytochrome P450 that degrades it.

Vitamin A deficiency affects more than 100 million children and causes hundreds of thousands of cases of blindness each year where rice is the staple. Rice grains contain no β-carotene, although the plant makes it in leaves. Golden Rice was engineered by adding two genes to the endosperm, a phytoene synthase (from daffodil in the first version, from maize in Golden Rice 2) and the bacterial phytoene desaturase CrtI (from *Pantoea ananatis*), which together complete the pathway from geranylgeranyl diphosphate to lycopene, which the endogenous enzymes cyclize to β-carotene. Golden Rice 2 provides enough β-carotene in a normal diet to prevent deficiency, and it was approved for cultivation in the Philippines in 2021 (approval was suspended by a court in 2024, an example of how the adoption of such crops depends on regulation as well as on biochemistry).

The other isoprenoid cofactors are carriers in membranes:

- Ubiquinone (coenzyme Q, with 10 isoprene units in mammals) and plastoquinone are lipid-soluble electron and proton carriers that diffuse within the membrane between the complexes of respiration and photosynthesis (7.1.23, 7.1.24); both accept one or two electrons and protons.
- Dolichols (14–24 isoprene units in plants and fungi, 17–21 in animals, 11 in bacteria as undecaprenol) anchor activated sugars to the membrane during glycan synthesis: dolichol phosphate carries the oligosaccharide precursor of N-glycans (7.1.10), and undecaprenol phosphate the disaccharide–peptide units of peptidoglycan (the target of the antibiotic bacitracin).
- Isoprenyl groups (farnesyl, C15; geranylgeranyl, C20) attached to Cys near the C terminus anchor proteins such as Ras to membranes (7.1.13).

Long systems of conjugated double bonds absorb visible light. The carotenoids (more than 700 are known) are yellow, orange and red pigments: they harvest light and protect against photo-oxidation in chloroplasts (7.1.24), colour carrots, tomatoes (lycopene) and the shells of crustaceans, and colour the feathers of birds, which take up carotenoids such as zeaxanthin and canthaxanthin from food; differences between males and females in intestinal uptake and metabolism of the carotenoids produce the differences in plumage, which signal the quality of a mate. Metabolic engineering of the carotenoid pathway in plant cell cultures and crops produces new colours and nutritionally enriched foods.

Polyketides, finally, are lipids synthesized by Claisen condensations like fatty acids but with variable reduction of the keto groups; as secondary metabolites they give their producers an ecological advantage, and many are drugs: the antibiotic erythromycin, the antifungal amphotericin B, and lovastatin, an inhibitor of cholesterol synthesis (statins, 7.1.26).

## 12.6. Working with Lipids

Lipids are insoluble in water, so their analysis starts with organic solvents and separates them by polarity.

- Extraction: neutral lipids (triacylglycerols, waxes, pigments) dissolve in ether, chloroform or hexane; membrane lipids need more polar solvents such as methanol, which also break their interactions with proteins. In the standard method (Folch; Bligh and Dyer) tissue is homogenized in chloroform–methanol–water (initially 1 : 2 : 0.8 by volume, one phase); more water and chloroform split the mixture into a chloroform phase with the lipids and a methanol–water phase with proteins and sugars.
- Separation: in **adsorption chromatography** on silica ([6.4.14](/6.4.14)), neutral lipids elute first with chloroform, uncharged polar lipids (cerebrosides) with acetone, and phospholipids with methanol; thin-layer chromatography on silica separates lipid classes on a plate, the least polar migrating farthest, and HPLC separates molecular species.
- Fatty acid composition: after hydrolysis or transesterification, the fatty acid methyl esters are separated and identified by **gas chromatography** ([6.4.13](/6.4.13)).
- Specific hydrolysis: phospholipases of known specificity (A₂, C, D) release identifiable parts of a phospholipid, which identifies the head group and the fatty acid at each position.
- Lipidomics: electrospray **mass spectrometry** ([6.4.15](/6.4.15)) of a crude extract ("shotgun lipidomics") or after liquid chromatography identifies and quantifies hundreds to thousands of molecular species at once, each by its mass and fragmentation pattern; mass spectrometry imaging maps them in tissue sections.

## Summary

| Structural feature | Chemical property | Biological function |
|---|---|---|
| long hydrocarbon chain, even C number, Δ⁹/Δ¹²/Δ¹⁵ cis bonds (Definition 12.2.1) | insoluble; packing set by length and cis bends | melting point: +6–10 °C per C₂, −55 °C for the first cis bond; membrane fluidity |
| trans double bond | nearly straight chain, packs like a saturated chain | partially hydrogenated fats; cardiovascular risk |
| triester of glycerol (Definition 12.3.1) | nonpolar, anhydrous, highly reduced carbon | 37 kJ/g versus 6 kJ/g for hydrated glycogen; 50 days of reserve (Example 12.3.1); insulation |
| ester of long acid and long alcohol (Definition 12.3.2) | mp 60–100 °C, water-repellent | cuticle, honeycomb, plankton fuel |
| glycerol 3-phosphate + 2 acyl + head group (Definition 12.4.1) | amphipathic; head-group charge | bilayer; surface charge; PI and PS as signals |
| ether linkage, vinyl ether (Definition 12.4.2) | resistant to phospholipases, oxidizable | plasmalogens of heart; PAF |
| galactose and sulfoquinovose heads | phosphate-free | thylakoid membranes |
| isoprenoid ether lipids of sn-glycerol 1-phosphate | hydrolysis-resistant, membrane-spanning | archaeal life in extreme environments |
| sphingosine + amide-linked acid (Definition 12.4.3) | H-bond donors, saturated chains | myelin, rafts; glycan heads for recognition; storage diseases |
| steroid nucleus with 3-OH (Definition 12.4.4) | rigid, planar, amphipathic | buffers membrane fluidity; precursor of bile acids and steroid hormones |
| C20 polyunsaturated precursors (Definition 12.5.1) | oxidized by COX and LOX | local hormones of inflammation, pain, fever, clotting; NSAIDs, low-dose aspirin |
| isoprene units (Definition 12.5.3) | conjugated double bonds, redox-active rings, long hydrophobic tails | vision, calcium hormone, antioxidant, clotting cofactor, membrane electron carriers, sugar carriers, pigments |

| Quantity | Value |
|---|---|
| fatty acid chain length | 4–36 C, mostly 12–24, even |
| energy of oxidation | fat 37 kJ/g; carbohydrate, protein 17 kJ/g; hydrated glycogen ≈ 6 kJ/g |
| reserves of a 70 kg adult | fat 400 000 kJ; protein 100 000 kJ; glycogen 2500 kJ |
| membrane lipids | 5–10 % of the dry mass of most cells |
| galactolipids | 70–80 % of the membrane lipids of vascular plants |
| plasmalogens | about half of heart phospholipids |
| cholesterol | about as long as an extended C16 chain |

## Questions

1. Rank tristearin, triolein, and a triacylglycerol containing one stearate and two oleates by melting point, and explain the ranking. Why would a membrane of a bacterium grown at 10 °C contain more unsaturated fatty acids than at 37 °C?

   **Answer** Tristearin (three saturated C18 chains) packs best and melts highest; the mixed triacylglycerol, with two kinked chains, melts much lower; triolein, with three cis-bent chains, lowest (it is an oil). Packing of straight chains maximizes van der Waals contact, and each cis bend disturbs it. A membrane must stay fluid for its proteins to work; at low temperature saturated chains would order into a gel, so the bacterium makes more unsaturated (and shorter or branched) chains, which lower the melting temperature of its lipids (homeoviscous adaptation).
2. Calculate the average oxidation number of carbon in palmitic acid and in glucose, and use it to explain why fat yields more than twice as much energy per gram as carbohydrate. What second factor makes the difference per gram of stored fuel even larger?

   **Answer** Palmitic acid $\ce{C16H32O2}$: with H = +1 and O = −2, $16x + 32 - 4 = 0$, $x = -1.75$. Glucose $\ce{C6H12O6}$: $6x + 12 - 12 = 0$, $x = 0$. Oxidation to $\ce{CO2}$ (oxidation number +4) therefore removes 5.75 electrons per carbon from palmitate but 4 from glucose, and palmitate has fewer oxygen atoms adding mass without energy; per gram this gives about 39 against 16 kJ. Second, fat is stored anhydrous, whereas glycogen carries about 2 g of water per gram, so per gram of stored mass fat holds about six times more energy.
3. Phosphatidylcholine and sphingomyelin have the same head group. Point out the structural differences between them and explain why sphingomyelin associates preferentially with cholesterol in the outer leaflet of the plasma membrane.

   **Answer** Phosphatidylcholine has a glycerol backbone with two ester-linked fatty acids (often one unsaturated at C-2). Sphingomyelin has a sphingosine backbone: one chain is the hydrocarbon tail of sphingosine itself, with a trans double bond near the head, and the second is a fatty acid in amide linkage, usually long and saturated; at the interface it has an amide N–H and a 3-OH that can donate hydrogen bonds. Long saturated chains pack well against the flat, rigid sterol rings, and the 3-OH of cholesterol can hydrogen-bond to the amide or hydroxyl of sphingomyelin, while its small head group is shielded by the large phosphocholine head (the "umbrella" effect); together these favour sphingomyelin–cholesterol domains in the ordered liquid state (lipid rafts).
4. Explain why a single low daily dose of aspirin inhibits platelet aggregation for days, whereas ibuprofen does not, and why a selective COX-2 inhibitor can increase the risk of thrombosis.

   **Answer** Aspirin acetylates a Ser in the cyclooxygenase active-site channel and inactivates the enzyme irreversibly. Platelets have no nucleus and cannot make new COX-1, so their thromboxane synthesis stays inhibited for their lifespan (about 7–10 days), while nucleated endothelial cells replace the enzyme within hours and continue to make prostacyclin, which inhibits aggregation; the balance shifts towards less clotting. Ibuprofen inhibits reversibly and its effect ends when it is cleared. A selective COX-2 inhibitor reduces endothelial prostacyclin, much of which is made by COX-2, but leaves platelet COX-1 and thromboxane untouched, so the balance shifts towards aggregation and vasoconstriction.
5. A child with an enlarged liver and spleen is found to accumulate glucosylceramide in macrophages. Name the disease, the defective enzyme and the compartment, and explain why intravenous enzyme replacement therapy works for this disease while it does not help the neurological forms of most sphingolipid storage diseases.

   **Answer** Gaucher disease: a deficiency of lysosomal glucocerebrosidase (β-glucosidase), so glucosylceramide accumulates in the lysosomes of macrophages (Gaucher cells) in liver, spleen and bone marrow. The infused enzyme is modified to expose mannose residues on its N-glycans; macrophages take it up through mannose receptors and deliver it to lysosomes, where it degrades the stored lipid (the same targeting principle as the mannose 6-phosphate pathway, 7.1.10). Enzymes do not cross the blood–brain barrier, so the stored lipid in neurons (as in Tay–Sachs disease or the neuronopathic forms of Gaucher disease) is not reached; substrate-reduction drugs that inhibit glucosylceramide synthesis, gene therapy and enzymes engineered to cross the barrier are being developed for these.
6. Why are the fat-soluble vitamins A and D toxic in excess while water-soluble vitamins rarely are? Why does vitamin D deficiency become common at high latitudes, and why does the active hormone require two hydroxylations in different organs?

   **Answer** Fat-soluble vitamins are stored in the liver and adipose tissue and excreted slowly, so large intakes accumulate (vitamin A causes liver damage and birth defects, vitamin D hypercalcemia), while excess water-soluble vitamins are excreted in the urine. Vitamin D₃ is made in the skin by UVB light breaking the B ring of 7-dehydrocholesterol; at high latitudes winter sunlight contains little UVB and clothing covers the skin, so without dietary sources deficiency (rickets) develops. Cholecalciferol itself is inactive: 25-hydroxylation in the liver gives the circulating storage form, and the regulated 1α-hydroxylation in the kidney, stimulated by parathyroid hormone when calcium is low, produces calcitriol only when it is needed; the two steps separate supply from hormonal control.
