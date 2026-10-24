---
title: Heterocyclic Compounds
description: Classification and nomenclature of heterocycles (trivial names, Hantzsch–Widman names, numbering and fused-ring names); electronic structure of aromatic heterocycles and measures of aromaticity; basicity and acidity of nitrogen heterocycles (pyridine, pyrrole, imidazole and histidine); electrophilic aromatic substitution of five-membered heterocycles and indole and its regioselectivity; electrophilic substitution of pyridine, N-oxides, nucleophilic aromatic substitution, the Chichibabin reaction, substitution after activation, and the Minisci reaction; reduction of heterocycles, Hantzsch esters and NADH, the Diels–Alder reaction of furan and inverse-electron-demand cycloaddition of tetrazines; the Paal–Knorr synthesis, the Fischer indole synthesis, the Hantzsch pyridine and thiazole syntheses; structure, numbering, tautomerism, base pairing, acid–base properties, and reactions of purines and pyrimidines; epoxides and aziridines, lactones and lactams, β-lactam antibiotics and nylon 6.
source_hash: f5ed018229a8
---

Cyclic compounds with ring atoms other than carbon (N, O, S, and so on) form the largest class of organic compounds. The bases of nucleic acids, the side chains of histidine and tryptophan, the porphyrins of chlorophyll and heme, vitamins B1, B2, B6, and B12, the great majority of alkaloids, and about three-fifths of small-molecule drugs all contain heterocycles. This chapter first treats the classification and nomenclature of heterocycles and then concentrates on aromatic heterocycles: their electronic structure and **aromaticity** were discussed in [Section 13.8 of 6.5.13](/6.5.13#sec-13.8), and on that basis we treat basicity, electrophilic and **nucleophilic substitution**, radical substitution, reduction and **cycloaddition**, and methods of synthesis, and then devote a section to the purines and pyrimidines of nucleic acids. The last section treats saturated heterocycles: epoxides and aziridines, lactones and lactams. The general mechanisms of **electrophilic aromatic substitution** and **nucleophilic aromatic substitution** are in [6.5.14](/6.5.14#sec-14.2), the structure and basicity of amines in [6.5.23](/6.5.23#sec-23.4), and the chemistry of nucleosides and nucleic acids in [6.5.33](/6.5.33#sec-33.9).

## 25.1. Classification and Nomenclature

### 25.1.1. Classification

**Definition 25.1.1 (Heterocyclic Compound)** A cyclic compound that contains, among the ring atoms, one or more atoms other than carbon (heteroatoms, most commonly N, O, and S) is called a **heterocyclic compound**.

Heterocycles fall into two classes. The properties of nonaromatic heterocycles (saturated or partly unsaturated rings) resemble those of the corresponding open-chain compounds: tetrahydrofuran is like an ether, piperidine like a secondary amine, and lactones and lactams like esters and amides, except that ring strain makes epoxides and aziridines especially reactive. Aromatic heterocycles obey **Hückel's rule** and have aromatic stabilization; their properties resemble those of benzene with important differences. They are mainly of two kinds: five-membered "heterocyclopentadienes" (pyrrole, furan, thiophene, in which the heteroatom supplies a pair of electrons) and six-membered "azabenzenes" (pyridine, pyrimidine, in which N supplies one electron).

Heterocycles are everywhere in natural products and drugs. The side chains of the essential amino acids histidine (imidazole) and tryptophan (indole) are aromatic heterocycles; the side chain of proline forms a pyrrolidine ring with the α-amino group, but proline is not an essential amino acid. The nitrogen of alkaloids such as morphine, cocaine, and nicotine ([6.5.23](/6.5.23#sec-23.1.3)) is in a heterocycle. Artemisinin is a sesquiterpene lactone with a peroxide bridge (a 1,2,4-trioxane), and Tu Youyou received the 2015 Nobel Prize in Physiology or Medicine for the discovery of artemisinin as a treatment for malaria.

### 25.1.2. Nomenclature

The common aromatic heterocycles all have retained trivial names, which the 2013 IUPAC recommendations and the 2017 rules of the Chinese Chemical Society both keep.

**Definition 25.1.2 (Pyrrole, Pyridine, and Indole)** The five-membered aromatic heterocycle $\ce{C4H4NH}$ with one nitrogen atom is called **pyrrole**; the six-membered aromatic heterocycle $\ce{C5H5N}$ with one nitrogen atom is called **pyridine**; the bicyclic aromatic compound formed by fusing a benzene ring to the C2–C3 bond of the pyrrole ring is called **indole**.

```smiles
c1cc[nH]c1 pyrrole
c1ccoc1 furan
c1ccsc1 thiophene
c1ccc2[nH]ccc2c1 indole
c1ccc2occc2c1 benzofuran
c1ccncc1 pyridine
c1ccc2ncccc2c1 quinoline
c1ccc2cnccc2c1 isoquinoline
```

```smiles
c1c[nH]cn1 imidazole
c1cn[nH]c1 pyrazole
c1cocn1 oxazole
c1cscn1 thiazole
c1cncnc1 pyrimidine
c1cnccn1 pyrazine
c1ccnnc1 pyridazine
c1ncncn1 1,3,5-triazine
c1nncnn1 1,2,4,5-tetrazine
```

| Structure | Name | Structure | Name |
|---|---|---|---|
| Five-membered, 1 N | pyrrole | Five-membered, 2 N | imidazole (1,3), pyrazole (1,2) |
| Five-membered, 1 O | furan | Five-membered, O and N | oxazole (1,3), isoxazole (1,2) |
| Five-membered, 1 S | thiophene | Five-membered, S and N | thiazole |
| Six-membered, 1 N | pyridine | Six-membered, 2 N | pyrimidine (1,3), pyrazine (1,4), pyridazine (1,2) |
| Six-membered, 1 O⁺ | pyrylium | Six-membered, 3 N, 4 N | 1,3,5-triazine, 1,2,4,5-tetrazine |
| Benzo-fused pyrrole | indole | Benzo-fused pyridine | quinoline, isoquinoline |

Some remarks:

- Pyran itself is a nonaromatic compound with one sp³ carbon (2*H*-pyran, 4*H*-pyran); the aromatic system isoelectronic with pyridine is the pyrylium ion $\ce{C5H5O+}$.
- "Diazine" is the general name for the three six-membered rings with two N; 1,2-diazine is called pyridazine.
- Numbering: in a ring with one heteroatom, numbering starts at the heteroatom as 1, with the lowest locants for substituents; indole and quinoline keep fixed numbering (indole N1, C2, C3, with C4–C7 on the benzene ring; the N of isoquinoline is at position 2). With several heteroatoms, the priority heteroatom is numbered 1 in the order O > S > N and the heteroatom locants are as low as possible: oxazole O1, N3, thiazole S1, N3; in imidazole the N bearing H is position 1. The numbering of purine is a special historical numbering (Section 25.8.1).
- Saturated heterocycles may be given trivial names (tetrahydrofuran, pyrrolidine, piperidine, morpholine), replacement names (the prefixes oxa-, aza-, thia- before the name of the carbocycle: 3-methyloxane, that is, 3-methyltetrahydropyran), or Hantzsch–Widman names (ring size and degree of saturation are expressed by the ending, for example the three-membered rings oxirane and aziridine and the four-membered rings oxetane and azetidine).
- A fused ring is named with the prefix "benzo" and the heterocycle name, with a letter in square brackets indicating which bond of the heterocycle is shared: the 1–2 bond is a, the 2–3 bond b, and so on. In benzofuran the benzene ring is fused to the 2,3-bond of furan, and the full name is benzo[*b*]furan (usually shortened to benzofuran); fusion at the 3,4-bond gives benzo[*c*]furan (isobenzofuran).

## 25.2. Electronic Structure and Aromaticity of Aromatic Heterocycles

[Section 13.8 of 6.5.13](/6.5.13#sec-13.8) stated the rule for the electronic structure of aromatic heterocycles: a heteroatom that takes part in a double bond in the ring (the N of pyridine, N3 of imidazole) contributes one p electron to the π system, with the lone pair in an sp² orbital in the plane of the ring; a heteroatom not in a double bond (the NH of pyrrole, the O of furan, the S of thiophene, N1 of imidazole) contributes a pair of p electrons to the π system. Hence:

- The 6 π electrons of a five-membered heterocycle are spread over 5 atoms, the electron density at ring carbon is higher than in benzene, and these are called π-excessive heterocycles, which undergo electrophilic substitution readily;
- The 6 π electrons of pyridine are spread over 6 atoms, and the N, of high **electronegativity**, pulls electrons toward itself, and the electron density at ring carbon is lower than in benzene; this is a π-deficient heterocycle, for which electrophilic substitution is difficult and **nucleophilic substitution** is easy.

The extent of **aromaticity** can be measured by several mutually independent criteria, which give roughly the same order:

| Criterion | Benzene | Thiophene | Pyrrole | Furan |
|---|---|---|---|---|
| Empirical resonance energy / $(\mathrm{kJ\,mol^{-1}})$ | About 150 | About 121 | About 88 | About 67 |
| C2–C3 / C3–C4 bond length / pm | 139 / 139 | 137 / 142 | 138 / 142 | 136 / 143 |
| Degree of bond-length equalization | Complete | High | Moderate | Low |

(The first three resonance energies are the values of [6.5.13](/6.5.13#sec-13.8); pyridine is about 117, close to benzene.) The more electronegative the heteroatom (O > N > S), the less willing its lone pair is to delocalize onto the ring, and the weaker the aromaticity. Another commonly used criterion is the **nucleus-independent chemical shift** (NICS, [Definition 13.4.2 of 6.5.13](/6.5.13#def-13.4.2)), which measures the magnetic shielding caused by the **ring current**: the NICS values of five-membered heterocycles are all fairly large negative numbers, indicating a significant ring current; however, NICS(0) is disturbed by σ bonds, and different criteria do not give exactly the same order in detail, so aromaticity is not a property that can be fully characterized by a single number. In the ¹H NMR spectra of five-membered heterocycles the ring H appear at $\delta$ 6.2–7.4 (pyrrole C2–H 6.7, C3–H 6.2; furan 7.4 and 6.4), and those of pyridine at $\delta$ 7.3–8.6, all in the aromatic region.

The relation between aromaticity and reactivity deserves attention: the weaker the aromaticity, the more readily the ring undergoes reactions that destroy aromaticity (addition, the **Diels–Alder reaction**). Furan has the weakest aromaticity, its electrophilic substitution often "breaks off" into addition (Section 25.4.4), and it is also the best diene among the five-membered heterocycles (Section 25.6.2). But the rate of electrophilic substitution is determined mainly by the ability of the heteroatom to stabilize the positive charge of the **σ complex** (N > O > S), so the order of rates is pyrrole > furan > thiophene, which is not the same as the order of aromaticity (Section 25.4.1).

## 25.3. Basicity and Acidity

### 25.3.1. Basicity of Nitrogen Aromatic Heterocycles

The basicity of nitrogen heterocycles depends on whether the lone pair of N belongs to the aromatic π system ([unified pKa table of 6.5.3](/6.5.3#sec-3.1.4); entries marked * are supplementary CRC data from outside the table):

| Conjugate acid | $\mathrm{p}K_{\mathrm{a}}$ (water, 25 °C) | Site of protonation and reason |
|---|---|---|
| Piperidinium | 11.12 | sp³ N, reference |
| Imidazolium | 6.99 | N3 (pyridine-type N); the positive charge is delocalized symmetrically over both N (amidine-type resonance) |
| Pyridinium | 5.23 | sp² lone pair, 33 % s character, $10^6$ times less basic than an sp³ amine |
| Isoquinolinium* | 5.4 | As pyridine |
| Quinolinium* | 4.9 | As pyridine; the fused benzene ring is slightly electron-withdrawing |
| Thiazolium* | 2.5 | Inductive electron withdrawal by S |
| Pyrimidinium* | 1.3 | Strong electron-withdrawing effect of the second N |
| Oxazolium* | 0.8 | Greater electronegativity of O |
| Pyrrole (protonated at C2) | $-3.8$ | The lone pair of N belongs to the 6π system, and protonation on N would destroy the **aromaticity** |

Imidazole is about 50 times more basic than pyridine: in the imidazolium ion the positive charge is dispersed over the two N by two equivalent resonance structures, with the lone pair of N1 pushing toward N3. The $\mathrm{p}K_{\mathrm{a}}$ of imidazolium (about 7; the histidine side chain is about 6.0 in the free amino acid and varies between 6 and 7 in proteins with the environment) is close to physiological pH, so that imidazole exists in both protonated and unprotonated forms under neutral conditions and can both give and accept protons; histidine is therefore the most common general **acid–base catalysis** group in enzyme active sites. In the catalytic triad (Ser–His–Asp) of serine proteases, the imidazole of His accepts the proton of the serine hydroxyl group, turning it into a strong **nucleophile**, and later gives the proton to the **leaving group** ([6.5.33](/6.5.33#sec-33.8.3)). Proton transfer between the two N of imidazole (**tautomerism**) interconverts 4-substituted and 5-substituted imidazoles, which are usually written as 4(5)-substituted imidazoles.

![The amphoteric nature of imidazole: N3 of imidazole accepts a proton to give the symmetrical imidazolium ion (the two resonance structures are equivalent and the positive charge is delocalized over both N); loss of the N1–H proton gives the imidazolide anion, whose negative charge is likewise delocalized over both N](./plots/imidazole.py)

### 25.3.2. Acidity of N–H

The N–H of pyrrole, indole, and imidazole is weakly acidic: in water about 17.5 for pyrrole and 14.5 for imidazole; in DMSO 23.0 for pyrrole, 21.0 for indole, and 18.6 for imidazole (Tables 3.2 and 3.3). They are slightly more acidic than diphenylamine (25.0 in DMSO), because the negative charge on N can be delocalized over the whole aromatic ring. After deprotonation with NaH, $\ce{KOH}$/DMSO, or $n$-BuLi, the nitrogen anions obtained are good **nucleophiles** and react with alkyl halides and acyl chlorides to give $N$-substituted products (the strongly ionic sodium and potassium salts give mainly N-alkylation in **polar aprotic solvents**, whereas the more covalent Mg salts tend to react at C).

```smiles
c1cc[nH]c1>>c1cc[n-]c1
c1cc[n-]c1.CI>>Cn1cccc1
```

## 25.4. Electrophilic Substitution of Five-Membered Heterocycles and Indole

### 25.4.1. Reactivity and Conditions

Pyrrole, furan, and thiophene are all much more reactive than benzene, in the order pyrrole > furan > thiophene ≫ benzene. For example, the relative rates of trifluoroacetylation are about pyrrole $5\times10^7$ : furan $1.4\times10^2$ : thiophene 1. This order reflects the ability of the heteroatom to donate electrons in the **σ complex** and stabilize the positive charge: N has a lower **electronegativity** than O and bears a positive charge more easily; the 3p orbital of S overlaps poorly with the 2p orbital of carbon. The strong **electrophiles** and strong acids required for electrophilic substitution of benzene are here not only unnecessary but harmful: pyrrole and furan protonate in strong acid and polymerize (forming black resins), so milder reagents are used:

| Reaction | Benzene ([6.5.14](/6.5.14)) | Five-membered heterocycle |
|---|---|---|
| Bromination | $\ce{Br2}$/$\ce{FeBr3}$ | $\ce{Br2}$ at $0\,^\circ\mathrm{C}$, no catalyst needed (pyrrole readily polybrominates; NBS for monobromination) |
| Nitration | Conc. $\ce{HNO3}$/conc. $\ce{H2SO4}$ | Acetyl nitrate ($\ce{HNO3}$/$\ce{Ac2O}$), low temperature |
| Sulfonation | Fuming sulfuric acid | Pyridine–$\ce{SO3}$ complex |
| Acylation | $\ce{RCOCl}$/$\ce{AlCl3}$ | Acid anhydride with a weak **Lewis acid** ($\ce{BF3.OEt2}$, $\ce{SnCl4}$); pyrrole can even be acylated without a catalyst |
| Formylation | Gattermann–Koch ([6.5.14](/6.5.14#sec-14.10)) | Vilsmeier–Haack (DMF/$\ce{POCl3}$) |

Heterocycles that are electron-rich enough can also react with weaker electrophiles: indole undergoes the **Mannich reaction** with formaldehyde and dimethylamine to give gramine; pyrrole, furan, and indole undergo **conjugate addition** to α,β-unsaturated ketones (the aromatic ring acts as the **nucleophile** and attacks the β carbon, a Friedel–Crafts-type **Michael addition**, [6.5.17](/6.5.17#sec-17.6.3)), which can be made asymmetric with chiral catalysts.

### 25.4.2. Five-Membered Heterocycles: Substitution at C2

Electrophilic substitution of pyrrole, furan, and thiophene takes place mainly at C2 (adjacent to the heteroatom, also called the α position). Compare the **σ complexes** of the two attacks: for attack at C2 the positive charge can be distributed over C3, C5, and the heteroatom, giving three resonance structures; for attack at C3 it can be distributed only over C2 and the heteroatom, giving two resonance structures (the C4=C5 double bond is cross-conjugated and cannot take part). In both cases there is an "onium" resonance structure (heteroatom positively charged, all atoms satisfying the **octet rule**), which is the main contributor; the positive charge is delocalized more widely in C2 attack, and the σ complex and the transition state leading to it are more stable (the **Hammond postulate**, [6.5.3](/6.5.3#sec-3.10)).

![Regioselectivity of electrophilic substitution of pyrrole (bromination as the example). Top: attack at C2, the σ complex has three resonance structures with the positive charge on C3, C5, and N; bottom: attack at C3, only two resonance structures (positive charge on C2 and N). In both rows the resonance structure with positively charged N (an iminium ion in which every atom has an octet) contributes most](./plots/pyrrole-sear.py)

When both α positions are occupied, substitution takes place at the β position (C3). The directing effects of substituents already on the ring combine with that of the ring itself: an electron-donating substituent reinforces the original selectivity; an electron-withdrawing group at the 2-position (such as 2-acetylfuran, 2-thiophenecarboxylic acid) directs the new group mainly to C5 (the other α position), whereas for pyrrole a mixture of C4 and C5 products is often obtained and the selectivity drops.

### 25.4.3. Indole: Substitution at C3

Electrophilic substitution of indole takes place at C3, unlike pyrrole. In attack at C3 the positive charge is at C2, directly stabilized by the lone pair of the adjacent N (an iminium ion), and the aromaticity of the benzene ring remains intact; in attack at C2 the positive charge is at C3, and for N to stabilize it the benzene ring has to take part in the resonance, so that the onium resonance structure written destroys the aromaticity of the benzene ring. C3 of indole is so reactive that it reacts with very weak **electrophiles**, at a rate about $10^{13}$ times that of benzene; the side chain of tryptophan, serotonin, and the biosynthesis of many indole alkaloids all make use of the **nucleophilicity** of C3. When C3 is occupied, substitution takes place at C2 (often through attack at C3 followed by a 1,2-shift).

![Regioselectivity of electrophilic substitution of indole. Top: attack at C3, the positive charge is on C2 and is stabilized by the lone pair of N as an iminium ion, with the benzene ring intact; bottom: attack at C2, the positive charge is on C3, and N can share it only if the benzene ring takes part in the resonance (destroying the aromaticity of the benzene ring)](./plots/indole-sear.py)

Benzofuran behaves differently, with electrophilic substitution mainly at C2: O is less able than N to stabilize a positive charge, so the oxonium resonance structure formed in attack at C3 contributes less, whereas attack at C2 gives a C3 cation that is a benzylic-type cation stabilized by the benzene ring; the two are comparable, and experimentally the C2 product predominates; benzothiophene is substituted mainly at C3.

### 25.4.4. Interrupted Electrophilic Substitution

The aromatic stabilization energy of furan is small, and the driving force for the **σ complex** to lose a proton and restore **aromaticity** is weak. If a **nucleophile** is present in the system it first captures the other end of the σ complex and gives an addition product: furan and $\ce{Br2}$ in methanol give 2,5-dimethoxy-2,5-dihydrofuran, a 1,4-addition rather than a substitution. This product is a protected butenedial and a useful synthetic intermediate.

![Interrupted electrophilic substitution of furan (Br₂ in methanol): the lone pair on the ring oxygen pushes the π electrons, which attack bromine at C2; the σ complex is an oxonium ion whose positive charge is stabilized by the oxygen next to C5. The gain in restoring aromaticity is small, so methanol captures C5 instead of a proton being lost, and the result is 1,4-addition; the allylic bromide is then replaced by methanol to give 2,5-dimethoxy-2,5-dihydrofuran](./plots/furan-addition.py)

```smiles
c1ccoc1.CO>>COC1OC(OC)C=C1
```

## 25.5. Reactions of Pyridine

The reactions of pyridine can be summarized in one sentence: the ring behaves like an electron-poor arene (nitrobenzene), and N like a tertiary amine. The lone pair on N is orthogonal to the π system of the ring and shows the properties of an amine: accepting a proton (Section 25.3), forming $N$-alkylpyridinium salts with alkyl halides, being oxidized by peracids to pyridine $N$-oxides, coordinating to metals as a ligand, and acting as a nucleophilic catalyst (DMAP, [6.5.23](/6.5.23#sec-23.4.4)). The ring carbons are reluctant to accept **electrophiles** and ready to accept **nucleophiles**.

### 25.5.1. Electrophilic Substitution

Electrophilic substitution of pyridine is much slower than that of benzene, for two main reasons: the electron-withdrawing effect of N makes the ring electron-poor; more important, the acidic conditions (or **Lewis acid**) used for electrophilic substitution first combine with N to give the positively charged pyridinium ion, which is much harder to attack than pyridine. The estimated relative reactivities (nitration) are about:

| Benzene | Nitrobenzene | Pyridine | $\ce{C6H5NMe3+}$ | Pyridinium ion |
|---|---|---|---|---|
| 1 | About $10^{-6}$ | About $10^{-6}$ | About $10^{-8}$ | About $10^{-20}$ |

(The last two entries are order-of-magnitude estimates extrapolated from kinetic data, and literature values can differ by several orders of magnitude.) Pyridine therefore undergoes electrophilic substitution only under very vigorous conditions and gives only 3-substituted products:

```smiles
c1ccncc1>>O=[N+]([O-])c1cccnc1
c1ccncc1>>OS(=O)(=O)c1cccnc1
c1ccncc1>>Brc1cccnc1
```

(Nitration: $\ce{KNO3}$/fuming sulfuric acid, $300\,^\circ\mathrm{C}$, in very low yield; sulfonation: fuming sulfuric acid with $\ce{HgSO4}$ catalyst, $230\,^\circ\mathrm{C}$; bromination: $\ce{Br2}$/fuming sulfuric acid, $130\,^\circ\mathrm{C}$.)

The C3 selectivity comes from the **σ complex**: for attack at C2 or C4 one resonance structure puts the positive charge on N, which then has only six valence electrons (not an iminium ion with an octet but a nitrogen cation on an atom of high **electronegativity**) and is very unstable; attack at C3 has no such resonance structure. The same principle acts in the opposite way in five-membered heterocycles: there the resonance structure with the positively charged heteroatom (the onium ion) has a lone pair on N taking part in bonding, so N has an octet and the structure is stable. When the ring bears a strong electron-donating group ($\ce{-NH2}$, $\ce{-OH}$, $\ce{-OCH3}$), electrophilic substitution becomes easy, and the position is determined jointly by the donor group and the ring N.

![Why electrophilic substitution of pyridine takes place at C3. Top: attack at C3 (bromination as the example) gives a σ complex with three resonance structures, with the positive charge on C2, C4, and C6 and never on nitrogen. Bottom: attack at C2 gives a σ complex in which one resonance structure puts the positive charge on nitrogen, which then has only six valence electrons and is extremely unstable, so the C2 (and C4) σ complexes are much higher in energy](./plots/pyridine-sear.py)

Pyridine $N$-oxide offers a roundabout route. The O anion of the $N$-oxide can push electrons to positions 2 and 4 of the ring (resonance of $\ce{N+-O-}$), making C4 the site of electrophilic attack: pyridine $N$-oxide is nitrated with $\ce{HNO3}$/$\ce{H2SO4}$ at about $100\,^\circ\mathrm{C}$ in good yield to 4-nitropyridine $N$-oxide, which is deoxygenated with $\ce{PCl3}$ to 4-nitropyridine; the 4-nitro group is easily displaced by **nucleophiles**, so a variety of 4-substituted pyridines becomes accessible.

![Activation of pyridine N-oxide at C4. Top: the lone pair on oxygen forms the N=O bond, and the π electrons of the ring are pushed onto C4 (resonance structure with the negative charge on C4; C2 and C6 are similar); the nitronium ion attacks this electron-rich position at C4. Bottom: the σ complex loses a proton to give 4-nitropyridine N-oxide, from which oxygen is removed with PCl₃](./plots/pyridine-n-oxide.py)

```smiles
[O-][n+]1ccccc1>>[O-][n+]1ccc(cc1)[N+](=O)[O-]
[O-][n+]1ccc(cc1)[N+](=O)[O-]>>[O-][N+](=O)c1ccncc1
```

### 25.5.2. Nucleophilic Aromatic Substitution

Pyridine is an electron-poor aromatic ring, and 2-halopyridines and 4-halopyridines undergo **nucleophilic aromatic substitution** (SNAr, [Section 14.11 of 6.5.14](/6.5.14#sec-14.11)) with alkoxides, amines, and thiolates under fairly mild conditions; the ring N acts like a nitro group *ortho* or *para* on a benzene ring: when the **nucleophile** adds to C2 or C4, the negative charge of the Meisenheimer-type intermediate can be placed on N, an atom of high **electronegativity**. For 3-halopyridines the negative charge cannot be placed on N, and the reaction is much slower. In 2-chloropyrimidine two N activate C2 at the same time, and it is much more reactive than 2-chloropyridine, a reaction commonly used in the synthesis of pyrimidine drugs and nucleobase analogues.

![Nucleophilic aromatic substitution of 2-chloropyridine: methoxide adds to C2 (slow), and the negative charge of the anionic intermediate is delocalized onto C3, C5, and the ring N (the resonance structure with the charge on N contributes most); chloride then leaves, restoring aromaticity, to give 2-methoxypyridine](./plots/pyridine-snar.py)

### 25.5.3. The Chichibabin Reaction

**Definition 25.5.1 (Chichibabin Reaction)** The reaction of pyridine (or another electron-poor nitrogen aromatic heterocycle) with sodium amide on heating, in which the amino group replaces the hydrogen on C2 to give 2-aminopyridine with evolution of hydrogen, is called the **Chichibabin reaction** (Chichibabin 1914).

This is an SNAr that directly replaces H: $\ce{NH2-}$ adds to C2 to give a σ adduct with the negative charge on N; the adduct loses hydride $\ce{H-}$ to restore **aromaticity**. Hydride itself is a very poor **leaving group**; it can leave because it reacts at once with the N–H of the product (or with $\ce{NH3}$ in the system) to release $\ce{H2}$, which makes the reaction irreversible; the product is present as the sodium salt of 2-aminopyridine, and treatment with water gives 2-aminopyridine.

![Mechanism of the Chichibabin reaction: amide ion adds to C2 of pyridine and the π electrons move onto the ring N; the negative charge returns to the ring and the electron pair of the C2–H bond leaves as hydride, restoring aromaticity; hydride removes a proton from the amino group and H₂ is evolved](./plots/chichibabin.py)

**Organolithium reagents** add to C2 of pyridine in the same way (the electronic effect at C2 is the most favorable and it is closest to the Li coordinated to N), giving 1,2-dihydropyridine lithium salts, which on heating eliminate LiH or on air oxidation give 2-alkyl (aryl) pyridines; addition at C4 is a minor path. The Chichibabin reaction is applicable only to reagents of very high **nucleophilicity** (amide ion, organolithiums), because the loss of aromaticity on addition has to be overcome.

### 25.5.4. Substitution after Activation

A more general strategy is first to "activate" the N of pyridine: N is combined with an **electrophile** $\ce{LG+}$ (acylation, sulfonylation, or $N$-oxide formation followed by activation with an electrophile) to give a pyridinium ion. A pyridinium ion is a much stronger electrophile, and **nucleophiles** add to C2 or C4 under mild conditions to give dihydropyridines; LG then leaves as the anion $\ce{LG-}$ with the electron pair of the N–LG bond while the proton of C–H is removed, restoring **aromaticity**. In the whole process LG changes from $\ce{LG+}$ to $\ce{LG-}$, that is, the **activating group** is reduced by two electrons, which come from the original C–H bond (the substrate is oxidized), so the overall result is an oxidative substitution of a C–H bond. Methods developed in recent years, triflyl (Tf) activation, activation of $N$-oxides and sulfonyl oximes, and heterocyclic phosphonium salts (McNally), are all based on this idea and allow late-stage functionalization of the pyridine ring of complex drug molecules.

### 25.5.5. The Minisci Reaction

**Definition 25.5.2 (Minisci Reaction)** The reaction in which a nucleophilic carbon radical (produced, for example, by oxidative decarboxylation of a carboxylic acid) adds to C2 or C4 of a protonated electron-poor nitrogen aromatic heterocycle (pyridine, quinoline, pyrazine, and so on), and oxidation with loss of a proton restores aromaticity, the net result being replacement of a C–H bond by an alkyl group, is called the **Minisci reaction** (Minisci 1968–1971).

The classical conditions are a carboxylic acid, $\ce{AgNO3}$ (catalytic), and ammonium persulfate heated in acidic aqueous solution: $\ce{Ag+}$ is oxidized by persulfate to $\ce{Ag^2+}$, $\ce{Ag^2+}$ oxidizes the carboxylate to the carboxyl radical, and this loses $\ce{CO2}$ to give the alkyl radical (radical **decarboxylation**, [6.5.18](/6.5.18#sec-18.4.2)). The LUMO of the protonated heterocycle is very low and matches well the SOMO of the alkyl radical (a higher-energy radical of high **nucleophilicity**), and addition takes place at C2 and C4 (positions of high positive charge density); the **radical cation** formed in the addition is oxidized by the oxidant and loses a proton, restoring **aromaticity**.

![The Minisci reaction: the tert-butyl radical (generated from pivalic acid by silver-catalyzed oxidative decarboxylation) adds to C2 of protonated 4-methylquinoline, and the radical cation formed is oxidized and loses a proton to give 2-tert-butyl-4-methylquinoline](./plots/minisci.py)

The Minisci reaction is exactly complementary to the **Friedel–Crafts reaction** (alkylation): the latter has an electrophilic **carbocation** attack an electron-rich arene and cannot be used for pyridine; the former has a nucleophilic radical attack an electron-poor arene. It does not require prior functionalization (no halopyridine is needed) and is suited to late-stage introduction of alkyl groups in drug molecules, and it has been widely used in medicinal chemistry. Modern versions use **photoredox catalysis** to generate radicals at room temperature from carboxylic acids, alcohols, alkyl halides, alkyl boronic acids, and so on ([6.5.31](/6.5.31#sec-31.5)); with a chiral phosphoric acid as a catalyst for protonation and hydrogen-bond direction, an enantioselective Minisci reaction is also possible (Phipps, *Science* 2018). The **regioselectivity** is affected by solvent, acid, and radical: in strong acid both C2 and C4 can be attacked, and when both are occupied the other electron-poor positions are attacked.

## 25.6. Reduction and Cycloaddition

### 25.6.1. Reduction

The **aromaticity** of aromatic heterocycles is weaker than that of benzene, and catalytic hydrogenation is easier than for benzene: pyridine is reduced in acid with $\ce{H2}$/Pt or Rh, or with Na/ethanol, to piperidine; furan is hydrogenated over Ni to tetrahydrofuran (one industrial source of THF); pyrrole is harder to reduce; thiophene causes **catalyst poisoning** of precious metals, and treatment with Raney Ni brings about desulfurization to the alkane ([6.5.16](/6.5.16#sec-16.6.2)). In the hydrogenation of benzo-fused heterocycles the heterocyclic part is reduced first and the benzene ring is unchanged: quinoline gives 1,2,3,4-tetrahydroquinoline, and indole is reduced with $\ce{NaBH3CN}$ in acid to indoline (2,3-dihydroindole). The latter reaction shows that the pyrrole ring of indole behaves like an **enamine** ([6.5.16](/6.5.16#sec-16.9.3)): indole is protonated at C3 to give the 3*H*-indolium ion (an iminium ion), and $\ce{NaBH3CN}$ reduces only iminium ions ([Section 23.5.4 of 6.5.23](/6.5.23#sec-23.5.4)).

```smiles
c1ccc2ncccc2c1>>c1ccc2NCCCc2c1
c1ccc2[nH]ccc2c1>>c1ccc2NCCc2c1
```

1,4-Dihydropyridine, the partial reduction product of the pyridine ring, is one of the most important hydride donors in living organisms: the active part of nicotinamide adenine dinucleotide (NADH, NADPH) is 1,4-dihydronicotinamide, which gives a hydrogen on C4 as hydride to a substrate (such as an aldehyde or ketone) and is itself oxidized to the aromatic pyridinium ion $\ce{NAD+}$; aromatization is the driving force of the hydride transfer. The Hantzsch ester commonly used in synthesis (the 1,4-dihydropyridinedicarboxylate of Section 25.7.3) is an analogue of NADH and in **organocatalysis** or photocatalysis serves as a mild hydride (or hydrogen atom) donor for asymmetric transfer hydrogenation of imines and alkenes.

![Hydride transfer from NADH (1-methyl-1,4-dihydronicotinamide as a model) to acetaldehyde (as in alcohol dehydrogenase, where a zinc ion and an acid activate the carbonyl group): the lone pair on nitrogen pushes electrons through the ring, and the electrons of one C–H bond on C4 are transferred together with the hydrogen to the carbonyl carbon, with the π electrons of C=O moving onto oxygen, which is protonated; the ring becomes the aromatic pyridinium ion NAD⁺, and aromatization is the driving force of hydride transfer](./plots/nadh-hydride.py)

### 25.6.2. Cycloaddition

The **aromaticity** of furan is weak, and it is a reactive diene: it undergoes the **Diels–Alder reaction** with maleic anhydride at room temperature ([6.5.12](/6.5.12#sec-12.4.3)) to give 7-oxabicyclo[2.2.1]heptene (oxanorbornene). The reaction is reversible: the kinetic product is the *endo* adduct, which changes on long standing to the thermodynamically more stable *exo* adduct, contrary to the usual **endo rule** of the Diels–Alder reaction. Furan can also trap **benzyne** ([6.5.15](/6.5.15#sec-15.1.4)). Pyrrole, with strong aromaticity, is generally not a diene (*N*-acylpyrroles can be); thiophene is even less reactive.

```smiles
c1ccoc1.O=C1OC(=O)C=C1>>O=C1OC(=O)C2C1C1OC2C=C1
```

Electron-poor nitrogen heterocycles can act as dienes in inverse-electron-demand Diels–Alder reactions (IEDDA): 1,2,4,5-tetrazines have a very low LUMO and react rapidly with electron-rich or strained alkenes (enol ethers, *trans*-cyclooctene); the bicyclic adduct formed releases $\ce{N2}$ (retro-Diels–Alder) to give a dihydropyridazine, which is oxidized to the pyridazine. The rate constants for the reaction of tetrazines with *trans*-cyclooctene can reach $10^3\text{–}10^6\,\mathrm{L\,mol^{-1}\,s^{-1}}$, the fastest **bioorthogonal reactions** ([Section 12.4.4 of 6.5.12](/6.5.12#sec-12.4.4)). Oxazoles can also act as dienes toward alkenes, giving pyridines by addition–elimination; the industrial synthesis of vitamin B6 (pyridoxine) uses this reaction.

## 25.7. Synthesis of Aromatic Heterocycles

The simple aromatic heterocycles are produced in large quantity by industrial methods: furfural is obtained by acid hydrolysis and dehydration of the pentosans of corncobs and bagasse, and decarbonylation of furfural gives furan; pyrrole is obtained from furan and ammonia heated over $\ce{Al2O3}$, or by dehydrogenation of pyrrolidine; thiophene by dehydrocyclization of butane with sulfur at high temperature; pyridine mainly by condensation of aldehydes with ammonia over catalysts (the Chichibabin pyridine synthesis). In the laboratory, substituted aromatic heterocycles are mostly made by condensation of open-chain carbonyl compounds to rings: the heteroatom acts as a **nucleophile** and attacks a carbonyl group, followed by dehydration and aromatization. Three of the most important named reactions follow.

### 25.7.1. The Paal–Knorr Synthesis

**Definition 25.7.1 (Paal–Knorr Synthesis)** The method in which a 1,4-dicarbonyl compound condenses with ammonia or a primary amine in weak acid to give a pyrrole, gives a furan on acid-catalyzed dehydration, and gives a thiophene with a sulfurizing reagent ($\ce{P4S10}$, Lawesson's reagent), is called the **Paal–Knorr synthesis** (Paal and Knorr 1884).

The Paal–Knorr pyrrole synthesis can be viewed as two condensations of an amine with carbonyl groups: the amine attacks one carbonyl group to give a hemiaminal, whose N then attacks the other carbonyl group to form a 2,5-dihydroxypyrrolidine, and two dehydrations followed by aromatization give the pyrrole. Kinetic studies (Amarnath 1991) show that ring closure takes place at the hemiaminal stage and is the **rate-determining step**; the commonly drawn mechanism through an **enamine** followed by ring closure is not consistent with experiment.

![The Paal–Knorr pyrrole synthesis (hexane-2,5-dione and methylamine). Methylamine adds to one carbonyl group, and proton transfer gives the hemiaminal; the N of the hemiaminal attacks the other carbonyl group to form the five-membered ring (rate-determining step); the diol loses water twice to give 1,2,5-trimethylpyrrole](./plots/paal-knorr.py)

The furan synthesis has a similar mechanism: the enol form of one carbonyl group attacks the other protonated carbonyl group to give a cyclic **hemiacetal**, which is dehydrated. In the thiophene synthesis the sulfurizing reagent first replaces carbonyl O by S, followed by a similar ring closure and dehydration. The limitation of the Paal–Knorr synthesis lies in the preparation of the 1,4-dicarbonyl compound itself, which is commonly obtained by the Stetter reaction or by alkylation of an **enolate** with an α-halo ketone ([6.5.21](/6.5.21#sec-21.7)).

```smiles
CC(=O)CCC(C)=O>>Cc1ccc(C)o1
CC(=O)CCC(C)=O>>Cc1ccc(C)s1
```

### 25.7.2. The Fischer Indole Synthesis

**Definition 25.7.2 (Fischer Indole Synthesis)** The method in which an arylhydrazine condenses with an aldehyde or ketone to give an arylhydrazone, which on heating with acid ($\ce{ZnCl2}$, polyphosphoric acid, HCl, or $\ce{H2SO4}$) undergoes a [3,3]-sigmatropic shift and loses ammonia to give an indole, is called the **Fischer indole synthesis** (E. Fischer 1883).

Mechanism (proposed by Robinson in 1918):

1. Phenylhydrazine condenses with a ketone to give the phenylhydrazone ([6.5.16](/6.5.16)), which undergoes **tautomerism** to the ene-hydrazine (the same as the imine–**enamine** tautomerism);
2. The protonated ene-hydrazine undergoes a [3,3]-**sigmatropic rearrangement** ([Section 12.5 of 6.5.12](/6.5.12#sec-12.5)): the weaker N–N bond breaks while a new C–C bond forms (C joined to the *ortho* carbon of the benzene ring), giving a diimine;
3. The benzene ring tautomerizes to restore **aromaticity**, giving an aniline; the N of the aniline attacks the imine carbon to form the five-membered cyclic aminal (2-aminoindoline);
4. Loss of $\ce{NH3}$ and aromatization give the indole.

![The Fischer indole synthesis (phenylhydrazine and acetone). Top: the phenylhydrazone tautomerizes to the ene-hydrazine, which on protonation undergoes the [3,3]-sigmatropic shift (N–N bond cleavage, C–C bond formation) to give the diimine. Bottom: tautomerization of the ring restores aromaticity, the N of the aniline attacks the imine carbon to close the ring, and loss of NH₃ gives 2-methylindole](./plots/fischer-indole.py)

$^{15}\mathrm{N}$-labeling experiments (Allen and Wilson 1943) showed that the N in the indole product is the one attached to the benzene ring and the other N leaves as ammonia, in agreement with this mechanism. An unsymmetrical ketone may give two ene-hydrazines, and the **regioselectivity** of the product depends on the direction of ene-hydrazine formation: under the usual acidic conditions the more substituted ene-hydrazine predominates, and under very strongly acidic conditions (such as polyphosphoric acid, $\ce{P2O5}$/$\ce{H3PO4}$) the proportion of the product from the less substituted ene-hydrazine increases. The Fischer indole synthesis is the most commonly used indole synthesis, and the industrial syntheses of the triptan antimigraine drugs (such as sumatriptan) and of indomethacin use it. Phenylhydrazine is obtained by reduction of a diazonium salt ([6.5.24](/6.5.24#sec-24.4.4)).

```smiles
NNc1ccccc1.CC(C)=O>>Cc1cc2ccccc2[nH]1
NNc1ccccc1.O=C1CCCCC1>>c1ccc2c(c1)[nH]c1CCCCc12
```

### 25.7.3. The Hantzsch Pyridine and Thiazole Syntheses

**Definition 25.7.3 (Hantzsch Pyridine Synthesis)** The four-component reaction in which two molecules of a β-keto ester (or other 1,3-dicarbonyl compound), one molecule of an aldehyde, and one molecule of ammonia condense to give a 1,4-dihydropyridine, which is then oxidized to the pyridine, is called the **Hantzsch pyridine synthesis** (Hantzsch 1881).

The mechanism is assembled from several known reactions: one molecule of ethyl acetoacetate undergoes **Knoevenagel condensation** with the aldehyde ([6.5.22](/6.5.22#sec-22.4.2)) to give an α,β-unsaturated carbonyl compound; another molecule of ethyl acetoacetate forms with ammonia an **enamine** (ethyl β-aminocrotonate); the α carbon of the enamine undergoes **Michael addition** to the unsaturated ketone; finally N attacks the ketone carbonyl group to close the ring and dehydration gives the 1,4-dihydropyridine (the Hantzsch ester). Oxidation of the 1,4-dihydropyridine to the pyridine with $\ce{HNO3}$, DDQ, or $\ce{MnO2}$ has a large driving force from aromatization.

```smiles
CCOC(=O)CC(C)=O.O=Cc1ccccc1>>CCOC(=O)C(=Cc1ccccc1)C(C)=O
CCOC(=O)CC(C)=O.N>>CCOC(=O)C=C(C)N
CCOC(=O)C1=C(C)NC(C)=C(C(=O)OCC)C1c1ccccc1>>CCOC(=O)c1c(C)nc(C)c(C(=O)OCC)c1-c1ccccc1
```

1,4-Dihydropyridines are themselves an important class of drugs: calcium channel blockers such as nifedipine (dimethyl 2,6-dimethyl-4-(2-nitrophenyl)-1,4-dihydropyridine-3,5-dicarboxylate) are used to treat hypertension and angina and are all prepared by the Hantzsch synthesis.

Hantzsch also developed syntheses of pyrroles and thiazoles. The Hantzsch thiazole synthesis uses an α-halo ketone and a thioamide (or thiourea): the S of the thioamide attacks the halogen-bearing carbon (**SN2**), N then attacks the ketone carbonyl group to close the ring, and dehydration gives the thiazole. The thiazolium ring of vitamin B1 (thiamine) ([6.5.16](/6.5.16#sec-16.10.4)) and the 2-aminothiazole of many drugs can be built in this way. The Hantzsch pyrrole synthesis uses an α-halo ketone, a β-keto ester, and ammonia (or a primary amine).

![The Hantzsch thiazole synthesis from chloroacetone and thioacetamide. Top: the soft sulfur atom displaces chloride by SN2. Bottom: after loss of a proton, the nitrogen of the S-alkylisothioamide attacks the ketone carbonyl group in the same molecule to form the five-membered ring; the 4-hydroxythiazoline then loses water and aromatizes to give 2,4-dimethylthiazole](./plots/hantzsch-thiazole.py)

```smiles
CC(=O)CCl.NC(C)=S>>Cc1csc(C)n1
```

### 25.7.4. Other Ring-Forming Methods

The 1,3-dipolar **cycloaddition** ([6.5.12](/6.5.12#sec-12.4.5)) is a general method for five-membered nitrogen heterocycles: azides and alkynes give 1,2,3-triazoles ([6.5.24](/6.5.24#sec-24.8.5)), nitrile oxides and alkynes give isoxazoles, and diazo compounds and alkynes give pyrazoles. Transition-metal-catalyzed cyclizations and multicomponent cyclizations can build highly substituted pyrroles and pyridines in one step from simple starting materials.

## 25.8. Purines and Pyrimidines

Purines and pyrimidines are the parent structures of the nucleic acid bases. This section deals only with their chemistry as heterocycles: structure and numbering, **tautomerism**, the distribution of **hydrogen bond** donors and acceptors, acid–base properties, and several kinds of chemical reactions; the chemistry of nucleosides and nucleotides is in [6.5.33](/6.5.33#sec-33.9), and the biological significance of base pairing in replication, transcription, and mutation is left to biochemistry and molecular biology.

### 25.8.1. Structure and Numbering

**Definition 25.8.1 (Pyrimidine and Purine)** The six-membered aromatic heterocycle $\ce{C4H4N2}$ with its two N in a *meta* (1,3) relationship is called **pyrimidine**; the bicyclic aromatic heterocycle $\ce{C5H4N4}$ formed by fusing a pyrimidine ring to an imidazole ring (sharing the C4–C5 bond of pyrimidine) is called **purine**.

Pyrimidine is numbered by the general rule (N1, C2, N3, C4, C5, C6). Purine keeps its historical numbering: the pyrimidine part is 1–6 and the imidazole part is 7–9, with the two fusion carbons being C4 and C5; in nucleosides, purine through N9 and pyrimidine through N1 form an N-**glycosidic bond** with C1′ of ribose.

The five bases of nucleic acids:

| Base | Parent | Structure | In nucleic acids |
|---|---|---|---|
| Adenine (A) | Purine | 6-Aminopurine | DNA, RNA |
| Guanine (G) | Purine | 2-Amino-1,9-dihydro-6*H*-purin-6-one | DNA, RNA |
| Cytosine (C) | Pyrimidine | 4-Aminopyrimidin-2(1*H*)-one | DNA, RNA |
| Thymine (T) | Pyrimidine | 5-Methylpyrimidine-2,4(1*H*,3*H*)-dione | DNA |
| Uracil (U) | Pyrimidine | Pyrimidine-2,4(1*H*,3*H*)-dione | RNA |

```smiles
Nc1ncnc2[nH]cnc12 A
Nc1nc2[nH]cnc2c(=O)[nH]1 G
Nc1cc[nH]c(=O)n1 C
Cc1c[nH]c(=O)[nH]c1=O T
O=c1cc[nH]c(=O)[nH]1 U
```

Other important purines are hypoxanthine, xanthine, uric acid (the end product of purine metabolism, deposited as sodium urate crystals in the joints in gout), and the purine alkaloids caffeine (1,3,7-trimethylxanthine) and theobromine; the base analogues 5-fluorouracil and 6-mercaptopurine are anticancer drugs, and acyclovir and zidovudine (AZT) are antiviral drugs.

Pyrimidine and purine themselves are aromatic. The bases bearing carbonyl groups (G, C, T, U) are cyclic amides (lactams), whose rings still retain considerable **aromaticity** through amide resonance ($\ce{N-C=O <-> N+=C-O-}$), and they can be regarded as analogues of 2-pyridone: the dipolar resonance structure $\ce{N+=C-O-}$ of 2-pyridone is a 6π pyridinium oxide.

### 25.8.2. Tautomerism

Nitrogen heterocycles bearing $\ce{C=O}$ and $\ce{-NH2}$ show two kinds of **tautomerism**: lactam–lactim tautomerism ($\ce{-NH-C(=O)- <=> -N=C(OH)-}$, equivalent to keto–enol tautomerism) and amino–imino tautomerism ($\ce{-N=C(NH2)- <=> -NH-C(=NH)-}$). Take the simplest model, 2-pyridone: in the gas phase the two forms are present in nearly equal amounts (slightly more 2-hydroxypyridine), whereas in water the lactam form predominates overwhelmingly (about $10^3 : 1$) because it is much more polar and forms stronger **hydrogen bonds** with water; 4-pyridone also exists mainly as the lactam in water.

```smiles
O=c1cccc[nH]1 lactam
Oc1ccccn1 lactim
```

In water the nucleic acid bases exist mainly as lactams (keto forms) and amino forms, and the rare lactim (enol) and imino tautomers account for only about $10^{-4}\text{–}10^{-5}$. This is the chemical basis of base pairing:

![Hydrogen bonds in Watson–Crick base pairs (the sugar replaced by methyl, attached to N9 of the purine and N1 of the pyrimidine; dashed lines join donor and acceptor atoms of hydrogen bonds). Top: adenine–thymine (A–T), two hydrogen bonds: N3–H of T to N1 of A, and an N–H of the 6-amino group of A to C4=O of T. Bottom: guanine–cytosine (G–C), three hydrogen bonds: the 4-amino group of C to C6=O of G, N1–H of G to N3 of C, and the 2-amino group of G to C2=O of C](./plots/base-pairs.py)

- Each base has a definite arrangement of **hydrogen bond** donors (N–H) and acceptors (lone pair on N, oxygen of C=O) on the pairing side: A is "acceptor–donor" (N1, N6–H), T is "donor–acceptor" (N3–H, O4), and the two are complementary and form two hydrogen bonds; G is "acceptor–donor–donor" (O6, N1–H, N2–H), C is "donor–acceptor–acceptor" (N4–H, N3, O2), and they form three hydrogen bonds. The G–C pair is therefore more stable than the A–T pair, and DNA rich in G–C has a higher melting temperature.
- The two base pairs have almost the same geometry (about $1.05\,\mathrm{nm}$ between the two C1′ of the sugars), so the diameter of the double helix is uniform, which was the key to the model built by Watson and Crick in 1953. Their original conjecture also relied on Chargaff's rules and on Donohue's point that the bases exist mainly in the keto forms; if the enol forms were taken, the pairing would be quite different.
- Tautomerism changes the arrangement of donors and acceptors. Rare tautomers (such as enol G or T) can form mispairs geometrically similar to Watson–Crick pairs (G–T, A–C), which is one of the mechanisms of spontaneous mutation proposed by Watson and Crick, and such transient tautomeric base pairs have recently been observed directly by NMR.

### 25.8.3. Acid–Base Properties

Nucleobases have both basic N and acidic N–H (approximate values for nucleosides, supplementary data from outside the tables):

| Position | Property | $\mathrm{p}K_{\mathrm{a}}$ (approx.) |
|---|---|---|
| Adenosine N1 | Protonation (conjugate acid) | 3.5 |
| Cytidine N3 | Protonation (conjugate acid) | 4.2 |
| Guanosine N7 | Protonation (conjugate acid) | 2.2 |
| Guanosine N1–H | Deprotonation | 9.2 |
| Uridine N3–H | Deprotonation | 9.3 |
| Thymidine N3–H | Deprotonation | 9.8 |

At physiological pH the bases are therefore almost all neutral, and the donors and acceptors of the **hydrogen bonds** keep the arrangement above. The bases are less basic than pyridine because the carbonyl groups and the other N of the ring are electron-withdrawing; the acidic N–H are all between two carbonyl groups or between a carbonyl group and a ring N (similar to an imide, phthalimide in [6.5.23](/6.5.23#sec-23.5.2) being 8.3), so the $\mathrm{p}K_{\mathrm{a}}$ is about 9–10. In acid (below about pH 5) N3 of cytosine is protonated, and Hoogsteen pairing of C⁺–G can form, giving non-canonical structures such as triplex DNA and the i-motif.

### 25.8.4. Chemical Reactions

The chemical reactions of the bases determine the types of chemical damage to DNA and are also the mode of action of many drugs and mutagens:

- Alkylation. The position of highest **nucleophilicity** in the bases is N7 of guanine (in the major groove of the double helix, exposed), followed by N3 and N1 of adenine; **SN2**-type alkylating agents such as methyl methanesulfonate and dimethyl sulfate alkylate mainly N7. **SN1**-type alkylating agents, such as the alkyldiazonium ions produced by metabolism of $N$-nitrosamines ([6.5.24](/6.5.24#sec-24.2.2)), attack oxygen atoms more, giving $O^6$-methylguanine, which pairs with T and causes G→A mutations. After N7 alkylation the imidazole ring is positively charged, the N-**glycosidic bond** is weakened, and the base is easily lost (depurination). The nitrogen mustard anticancer drugs are bifunctional alkylating agents that form cross-links between N7 of G on the two strands.
- Deamination. The 4-amino group of cytosine can be hydrolyzed to a carbonyl group, giving uracil (an addition–elimination process: water adds to C4 and $\ce{NH3}$ is then lost); this spontaneous deamination occurs about a hundred times per day in every cell, and nitrous acid greatly accelerates it through **diazotization** ([6.5.24](/6.5.24#sec-24.2.1)); deamination of adenine gives hypoxanthine. Deamination of 5-methylcytosine gives thymine directly, and the repair system cannot tell whether the T is "wrong" or original, so methylated CpG sites are mutation hot spots. The use of T rather than U in DNA is thought to be related to this: U in DNA can arise only from deamination of C and can be specifically recognized and excised.
- Photochemical reactions. Two adjacent thymines undergo [2+2] **photocycloaddition** between their C5=C6 double bonds under ultraviolet light (UV-B, UV-C) ([Section 12.4.2 of 6.5.12](/6.5.12#sec-12.4.2)) to give cyclobutane pyrimidine dimers, which distort the DNA helix and block replication and are the main molecular cause of sunlight-induced skin cancer; another class of products is the (6-4) photoproduct. Photolyases use visible light to open the cyclobutane by transferring an electron to the dimer, repairing this damage.

![Alkylation of guanine at N7 (9-methylguanine as a representative of a nucleoside): N7 is the most nucleophilic position of the bases and is exposed in the major groove of DNA, and its lone pair attacks the methyl carbon of methyl methanesulfonate by SN2, with methanesulfonate leaving; the imidazole ring of 7-methylguaninium is positively charged, the N-glycosidic bond is weakened, and depurination results](./plots/guanine-alkylation.py)

![Hydrolytic deamination of cytosine (1-methylcytosine as a model). Top: after N3 is protonated, water adds to C4, and the π electrons of C4=N3 move onto N3. Bottom: after proton transfer the tetrahedral intermediate collapses, the lone pair on oxygen re-forms C=O, and ammonia leaves, giving uracil; in DNA this turns a C:G base pair into U:G, and repair enzymes recognize the U that should not be in DNA](./plots/cytosine-deamination.py)

```smiles
Cc1c[nH]c(=O)[nH]c1=O.Cc1c[nH]c(=O)[nH]c1=O>>CC12C(NC(=O)NC1=O)C1NC(=O)NC(=O)C21C
Nc1cc[nH]c(=O)n1>>O=c1cc[nH]c(=O)[nH]1
```

## 25.9. Nonaromatic Heterocycles

### 25.9.1. Epoxides and Aziridines

The preparation and ring opening of **epoxides** are in [Section 10.9 of 6.5.10](/6.5.10#sec-10.9) and [6.5.11](/6.5.11#sec-11.8.1): under basic or neutral conditions **nucleophiles** attack the less hindered carbon by **SN2**, and under acidic conditions they attack the carbon better able to stabilize positive charge, with *anti* ring opening in both cases. Epoxides can also be opened by radicals: the low-valent titanium reagent $\ce{Cp2TiCl}$ (Nugent–RajanBabu, 1994) transfers one electron to the C–O bond of the epoxide, and as the Ti–O bond forms the C–O bond undergoes **homolysis** to give the more substituted carbon radical (the more stable radical); this can be reduced by a hydrogen atom donor (such as 1,4-cyclohexadiene), leaving the hydroxyl group on the less substituted carbon, a **regioselectivity** opposite to that of hydride opening with $\ce{LiAlH4}$ (hydride attacks the less hindered carbon, giving the tertiary alcohol), or cyclize onto an alkene in the same molecule; using a radical rearrangement of known rate as a "**radical clock**" shows that the intermediate is a radical.

```smiles
CC1(C)OC1C>>CC(C)C(C)O
```

Aziridine is a three-membered ring with one N and, like an epoxide, has a **ring strain** of about $110\,\mathrm{kJ\,mol^{-1}}$ and is readily opened by nucleophiles to give β-substituted amines; "activated" aziridines with an electron-withdrawing group (sulfonyl, acyl) on N open faster, and aziridines are also activated when N is protonated or coordinated by acid or **Lewis acid**. They are prepared by addition of a nitrene or its equivalent (such as $\ce{PhI=NTs}$ with Cu or Rh catalysis) to alkenes, in analogy to epoxidation of alkenes, and by intramolecular substitution of β-amino alcohols. The three-membered ring makes inversion at N very slow ([Section 23.3.2 of 6.5.23](/6.5.23#sec-23.3.2)). The natural anticancer antibiotic mitomycin C contains an aziridine, which opens after reductive activation in the cell and cross-links the two strands of DNA. Chiral catalysts allow enantioselective ring opening of *meso*-aziridines.

### 25.9.2. Lactones and Lactams

Lactones and lactams are cyclic esters and amides, and Greek letters indicate the carbon on which the hydroxyl or amino group was originally located, according to ring size: β-propiolactone (four-membered ring), γ-butyrolactone (five-membered), δ-valerolactone (six-membered), ε-caprolactone (seven-membered); lactams likewise.

**Definition 25.9.1 (Lactam)** A cyclic amide formed by dehydration between an amino group and a carboxyl group in the same molecule is called a **lactam**.

Five- and six-membered lactones and lactams form spontaneously from hydroxy acids or amino acids; larger rings (macrolides) can be closed efficiently in an intramolecular reaction only at high dilution with the carboxyl group activated by a condensing reagent such as DCC/DMAP, EDCI, or Yamaguchi's reagent, to avoid intermolecular polymerization. Lactones and lactams undergo the general reactions of carboxylic acid derivatives: ring opening by acidic or basic hydrolysis, aminolysis, and reduction with $\ce{LiAlH4}$ to diols or cyclic amines ([6.5.19](/6.5.19#sec-19.7)).

The most commonly used synthesis of β-lactones and β-lactams is the [2+2] **cycloaddition** of ketenes ([Section 12.4.6 of 6.5.12](/6.5.12#sec-12.4.6)): a ketene and an aldehyde give a β-lactone under Lewis acid catalysis; a ketene and an imine give a β-lactam, the Staudinger β-lactam synthesis (Staudinger 1907; not to be confused with the **Staudinger reduction** of azides, [6.5.26](/6.5.26#sec-26.5.5)). The latter actually proceeds stepwise: the N of the imine first attacks the carbonyl carbon of the ketene to give a **zwitterion** intermediate, and the carbon of the **enolate** then attacks the carbon of the iminium ion to close the ring.

```smiles
C=C=O.C(=Nc1ccccc1)c1ccccc1>>O=C1CC(c2ccccc2)N1c1ccccc1
```

The **ring strain** of a β-lactone is large, and a **nucleophile** can open it at two positions: hard nucleophiles (alkoxides, amines) attack the carbonyl group and cleave the acyl–oxygen bond to give β-hydroxy carboxylic acid derivatives; soft nucleophiles (thiolates, halide, organocopper reagents) undergo **SN2** at the β carbon and cleave the alkyl–oxygen bond to give β-substituted carboxylic acids.

The β-lactam is the core structure of antibiotics such as penicillins and cephalosporins. Penicillin (discovered by Fleming in 1928; its structure was established by Hodgkin in 1945 by **X-ray diffraction**) consists of a β-lactam ring fused to a thiazolidine ring; ampicillin and amoxicillin are semisynthetic penicillins with different side chains. Their mechanism of action is an **acyl transfer** reaction: in synthesizing the peptidoglycan of the cell wall, the transpeptidase (penicillin-binding protein) attacks the terminal D-Ala–D-Ala of the peptide chain with the hydroxyl group of an active-site serine; penicillin resembles D-Ala–D-Ala in conformation, and the serine instead attacks the carbonyl group of the β-lactam, opening the ring to give a stable acyl–enzyme, so that the enzyme is irreversibly inhibited, the cell wall cannot be cross-linked, and the bacterium bursts and dies. A β-lactam is a good acylating agent first because of the strain of the four-membered ring and second because the bicyclic skeleton makes N pyramidal so that its lone pair cannot conjugate with the carbonyl group and the stabilization by amide resonance is essentially lost. Bacterial resistance comes mainly from β-lactamases, which hydrolyze the β-lactam ring; β-lactamase inhibitors such as clavulanic acid, used together with penicillin, overcome this resistance.

```smiles
CC1([C@@H](N2[C@H](S1)[C@@H](C2=O)NC(=O)CC3=CC=CC=C3)C(=O)O)C penicillin G
```

ε-Caprolactam is produced industrially from cyclohexanone oxime by the **Beckmann rearrangement** ([6.5.30](/6.5.30#sec-30.5.3)), and its ring-opening polymerization gives nylon 6 (polycaprolactam), produced in millions of tonnes per year for fibers and engineering plastics.

```smiles
ON=C1CCCCC1>>O=C1CCCCCN1
```

## 25.10. Research Frontier

The frontier of heterocyclic chemistry is closely tied to medicinal chemistry. One direction is direct "late-stage functionalization" of existing drug molecules: Minisci-type reactions, pyridine phosphonium salts, and temporary dearomatization of pyridine (for example through Zincke imine or oxazino-pyridine intermediates) have for the first time made it possible to functionalize selectively the *meta* (C3) C–H bond of pyridine, which previously could be done only under the harsh conditions of electrophilic substitution. Another direction is "skeletal editing": inserting, deleting, or replacing one atom in an aromatic heterocycle, for example ring expansion of indole to quinoline or replacement of the N of pyridine by C, which changes the core skeleton of a drug molecule without resynthesis (Levin, Sarpong, and others, since 2021).

## Summary

- Heterocycles (Definition 25.1.1) are divided into nonaromatic heterocycles (properties like the open-chain ethers, amines, esters, and amides, with small rings reactive) and aromatic heterocycles; the common aromatic heterocycles have trivial names (Definition 25.1.2), numbered from the heteroatom, with O > S > N.
- Electronic structure: a heteroatom in a ring double bond supplies one p electron (lone pair in the plane, basic), and one not in a double bond supplies a pair of p electrons. Five-membered heterocycles are π-excessive and pyridine is π-deficient; **aromaticity** benzene > thiophene > pyrrole > furan.
- Basicity (conjugate-acid $\mathrm{p}K_{\mathrm{a}}$): piperidine 11.12 > imidazole 6.99 > pyridine 5.23 > pyrimidine 1.3 > pyrrole $-3.8$; the amphoteric nature of imidazole and its $\mathrm{p}K_{\mathrm{a}}$ near 7 make histidine a general **acid–base catalysis** group of enzymes; the N–H of pyrrole, indole, and imidazole is weakly acidic.
- Comparison of reactivity:

  | | Five-membered heterocycles, indole | Pyridine |
  |---|---|---|
  | **SEAr** | Fast (pyrrole > furan > thiophene ≫ benzene), mild reagents; at C2 for pyrrole, furan, and thiophene, at C3 for indole, at C2 for benzofuran | Very slow, vigorous conditions, C3; $N$-oxide at C4 |
  | **Nucleophilic substitution** | Generally does not occur | **SNAr** of 2- and 4-halopyridines; the Chichibabin reaction (Definition 25.5.1); substitution after activation |
  | Radical substitution | — | The Minisci reaction (Definition 25.5.2), protonated heterocycle + nucleophilic radical, C2/C4 |
  | Reduction | Furan → THF; indole → indoline ($\ce{NaBH3CN}$/acid) | Pyridine → piperidine; 1,4-dihydropyridines (NADH, Hantzsch esters) are hydride donors |
  | **Cycloaddition** | Furan is a good diene (*exo* is the thermodynamic product) | IEDDA of tetrazines (bioorthogonal) |

- Synthesis: the Paal–Knorr synthesis (Definition 25.7.1, 1,4-dicarbonyl → pyrrole, furan, thiophene, ring closure at the hemiaminal stage); the Fischer indole synthesis (Definition 25.7.2, arylhydrazone → ene-hydrazine → [3,3]-**sigmatropic rearrangement** → loss of $\ce{NH3}$); the Hantzsch pyridine synthesis (Definition 25.7.3, Knoevenagel + **enamine** + Michael + ring closure, followed by oxidation of the 1,4-dihydropyridine) and the thiazole synthesis.
- Pyrimidine and purine (Definition 25.8.1): the special numbering of purine, with sugar attached at N9/N1; the bases bearing carbonyl groups are lactams, in water mainly in keto and amino forms, which fixes the donor–acceptor complementarity of A–T (2 **hydrogen bonds**) and G–C (3 hydrogen bonds); rare tautomers cause mispairs; the bases are neutral at physiological pH; N7 alkylation, deamination (C → U, 5-methyl-C → T), and [2+2] photodimerization of thymine are the main types of chemical damage to DNA.
- Nonaromatic heterocycles: ring opening of epoxides and aziridines; lactams (Definition 25.9.1) and lactones; the Staudinger β-lactam synthesis from ketenes and imines; β-lactam antibiotics acylate the serine of the transpeptidase by virtue of **ring strain** and loss of amide resonance; ring-opening polymerization of ε-caprolactam gives nylon 6.

## Questions

1. Decide whether each of the following compounds has **aromaticity**, and state in which kind of orbital the lone pair of each heteroatom lies: (a) thiazole; (b) pyrylium ion; (c) 4*H*-pyran; (d) purine.

   **Answer** (a) Yes. S contributes a pair of p electrons and N one p electron, 6 π electrons in all; the other lone pair of S and the lone pair of N lie in sp² orbitals in the plane of the ring. (b) Yes. $\ce{O+}$ is isoelectronic with the N of pyridine and contributes one p electron to the 6π system, with the remaining lone pair in an sp² orbital in the plane. (c) No. C4 is an sp³ carbon and conjugation is interrupted (nonaromatic). (d) Yes. There are 10 π electrons in all (4*n* + 2, *n* = 2): the N of N9–H contributes a pair of p electrons and N1, N3, and N7 one p electron each, and their lone pairs lie in the plane and are the basic sites.

2. Explain: (a) pyrrole is about $10^9$ times less basic than pyridine yet much more acidic; (b) imidazole is more basic than pyridine; (c) electrophilic substitution of pyridine takes place at C3, whereas **nucleophilic substitution** takes place at C2 and C4.

   **Answer** (a) The lone pair on the N of pyrrole is part of the 6π aromatic system, and protonation on N would destroy the aromaticity; protonation can take place only on C2 (conjugate-acid $\mathrm{p}K_{\mathrm{a}}$ $-3.8$), whereas the lone pair of pyridine lies in an in-plane sp² orbital, and protonation does not affect aromaticity (5.23). After the N–H of pyrrole dissociates, the negative charge is delocalized over the whole aromatic ring (about 17.5 in water), whereas pyridine has no N–H. (b) The positive charge of the imidazolium ion is dispersed over the two N by two equivalent resonance structures (amidine-type resonance), the lone pair of N1 pushing toward N3 and increasing the electron density at N3. (c) For electrophilic attack at C2 or C4 the **σ complex** has a resonance structure with the positive charge on N, which has only six valence electrons and is very unstable, so attack can occur only at C3; for nucleophilic attack at C2 or C4 the anionic intermediate has a resonance structure with the negative charge on the electronegative N, which is stable, and attack at C3 has no such resonance structure.

3. Write the main products: (a) 2-methylfuran with acetic anhydride and $\ce{BF3.OEt2}$; (b) indole with DMF and $\ce{POCl3}$, then hydrolysis; (c) 4-chloropyridine heated with piperidine; (d) 3-methylpyridine heated with $\ce{NaNH2}$; (e) pyridine $N$-oxide with $\ce{HNO3}$/$\ce{H2SO4}$, then $\ce{PCl3}$.

   **Answer** (a) 2-Acetyl-5-methylfuran (substitution at the other α position, C5). (b) Indole-3-carbaldehyde (Vilsmeier–Haack reaction, at C3). (c) 4-(Piperidin-1-yl)pyridine (**SNAr**, with the negative charge able to fall on N). (d) The Chichibabin reaction, giving mainly 2-amino-3-methylpyridine together with 2-amino-5-methylpyridine (both α positions can be attacked, the ratio depending on conditions). (e) 4-Nitropyridine $N$-oxide, which after deoxygenation gives 4-nitropyridine.

4. Synthesize by the Paal–Knorr, Fischer, or Hantzsch method, from suitable starting materials: (a) 1-phenyl-2,5-dimethylpyrrole; (b) 2,3-dimethylindole; (c) diethyl 2,6-dimethyl-4-phenylpyridine-3,5-dicarboxylate; (d) 2-amino-4-methylthiazole.

   **Answer** (a) Hexane-2,5-dione and aniline, heated with acetic acid catalysis (Paal–Knorr). (b) Phenylhydrazine and butan-2-one, heated in $\ce{ZnCl2}$ or acetic acid; under these usual conditions the ene-hydrazine forms mainly toward the more substituted side ($\ce{CH3C(=CHCH3)-NHNHPh}$), and after the [3,3]-shift 2,3-dimethylindole is obtained (the other direction gives 2-ethylindole, the minor product). (c) Two molecules of ethyl acetoacetate, benzaldehyde, and ammonia (or ammonium acetate) condense to the 1,4-dihydropyridine, which is oxidized with $\ce{HNO3}$ or DDQ (Hantzsch). (d) Chloroacetone and thiourea (Hantzsch thiazole synthesis): S undergoes **SN2** at $\ce{CH2Cl}$, N attacks the carbonyl group to close the ring, and dehydration follows.

5. Pyrrole quickly turns into a red resin in dilute hydrochloric acid, whereas thiophene is stable under the same conditions. Explain. Why is pyrrole nitrated with acetyl nitrate and not with mixed acid?

   **Answer** Pyrrole is protonated at C2 (or C3) to give the nonaromatic 2*H*-pyrrolium ion, a reactive **electrophile** (an iminium ion), which is attacked by another electron-rich pyrrole molecule, and repetition gives a polymer. Thiophene has stronger aromaticity and is extremely weakly basic, and is hardly protonated in dilute acid. The strong acid of mixed acid would polymerize or oxidatively decompose pyrrole, and the nitronium ion is too reactive; acetyl nitrate at low temperature supplies a mild electrophilic nitrating agent without strong acid, giving mainly 2-nitropyrrole.

6. In the "activation–**nucleophilic addition**–elimination" route to C–H substitution of a pyridinium ion, the **activating group** $\ce{LG+}$ finally leaves as $\ce{LG-}$. Taking activation with $\ce{Tf2O}$ and addition of the **nucleophile** $\ce{Nu-}$ to C4 as the example, write the steps and say what kind of redox process this is.

   **Answer** (1) The N of pyridine attacks $\ce{Tf2O}$ to give the $N$-trifluoromethanesulfonylpyridinium ion (the equivalent of Tf carrying positive charge, $\ce{Tf+}$) and $\ce{TfO-}$. (2) $\ce{Nu-}$ adds to C4 to give the $N$-Tf-1,4-dihydropyridine. (3) Base removes the proton of C4–H, the electron pair is pushed through the ring toward N, the N–S bond breaks and Tf leaves as the sulfinate $\ce{CF3SO2-}$ ($\ce{Tf-}$), and the ring regains aromaticity to give the 4-substituted pyridine. Sulfur changes from $\ce{Tf+}$ (sulfonyl, S(VI)) to triflinate (S(IV)), so the activating group has been reduced by two electrons; these two electrons come from the electron pair of the original C4–H bond, and C4 of the substrate is oxidized (C–H becomes C–Nu). The whole process is therefore an oxidative C–H substitution with the activating reagent as the oxidant.

7. The rare tautomer of cytosine (the imino form, 4-imino) can form two **hydrogen bonds** with adenine. Explain this mispair in terms of the arrangement of hydrogen-bond donors and acceptors, and explain why treating DNA with nitrous acid induces C→T mutations.

   **Answer** The arrangement of normal cytosine on the pairing face is N4–H (donor), N3 (acceptor), and O2 (acceptor), complementary to O6 (acceptor), N1–H (donor), and N2–H (donor) of G. In the imino tautomer the H has moved from N4 to N3: the pairing face becomes N4 (acceptor, the lone pair of =NH) and N3–H (donor), exactly complementary to N6–H (donor) and N1 (acceptor) of adenine, forming two hydrogen bonds with a geometry similar to the A–T pair, so that A may be inserted opposite C during replication. Nitrous acid brings about **diazotization** of the 4-amino group of cytosine, which is replaced by water (deamination), and C becomes U; U pairs with A, and after replication the original G–C pair has become an A–T pair, that is, a C→T (G→A) transition mutation.

8. Explain why the β-lactam of penicillin is much more easily attacked by the hydroxyl group of serine than an ordinary amide, and how the antibacterial activity should change if the β-lactam of penicillin were replaced by a five-membered γ-lactam.

   **Answer** The lone pair of N in an ordinary amide is conjugated with the carbonyl group (resonance stabilization about $70\text{–}80\,\mathrm{kJ\,mol^{-1}}$), the C–N bond has partial double-bond character, and the electrophilicity of the carbonyl carbon is low. The bicyclic skeleton of penicillin makes the N of the β-lactam pyramidal, its lone pair cannot conjugate coplanarly with the carbonyl group, and resonance stabilization is essentially lost; the strain of the four-membered ring (about $100\,\mathrm{kJ\,mol^{-1}}$) is released on ring opening and further increases the driving force. A γ-lactam has far less strain and its N flattens more easily, so the acylating activity is greatly reduced, and the antibacterial activity is expected to fall markedly or vanish (although active γ-lactam analogues have been designed in recent years, they need some other mode of activation).
