---
title: Introduction, Nomenclature and Structure
description: The subject and methods of organic chemistry; skeletal formulas, formal charges and curly arrows; functional groups and oxidation states of carbon; systematic nomenclature following the IUPAC 2013 recommendations (substitutive nomenclature, seniority of principal characteristic groups, parent chains and numbering, rings, spiro and bridged compounds), with the correspondence to the Chinese Chemical Society rules of 2017; a review of hybridization and bond parameters; resonance theory, with the rules for writing resonance structures and judging their contributions.
source_hash: cca4e0b8bd95
---

Organic chemistry is the study of the compounds of carbon, chiefly hydrocarbons and their derivatives: their structures, properties, reactions and synthesis. Early in the nineteenth century it was believed that organic substances could be produced only by living organisms under the action of a "vital force". After Wöhler (1828) obtained urea from ammonium cyanate, acetic acid (Kolbe, 1845), fats (Berthelot, 1854) and many other compounds were made from inorganic starting materials, and the word "organic" kept only its historical meaning. Almost all later progress came from structural theory: Kekulé and Couper (1858) proposed the tetravalence of carbon and carbon chains, van 't Hoff and Le Bel (1874) the tetrahedral carbon atom, Lewis (1916) explained the covalent bond by the sharing of electron pairs, Pauling introduced **hybrid orbitals**, electronegativity and resonance theory in the 1930s, and Hückel and Mulliken developed molecular orbital theory. The central idea of organic chemistry is that structure determines properties: the distribution of electrons in a molecule and the spatial arrangement of its atoms determine where and how the molecule reacts.

Contemporary organic chemistry both synthesizes ever more complex molecules and changes the way synthesis is done. From Robinson's one-step synthesis of tropinone (1917) through Woodward's quinine (1944) and strychnine (1954), the Woodward–Eschenmoser synthesis of vitamin B₁₂ (1973) and Kishi's palytoxin (1994, 64 stereocenters), total synthesis has been the proving ground of structural theory and synthetic methodology. Newer directions include continuous-flow synthesis, mechanochemical methods such as ball milling ([6.5.31](/6.5.31)), automated platforms that design and carry out experiments on their own, and algorithmically planned synthetic routes of natural products that have been verified experimentally.

This chapter supplies the language and tools of the whole course. We begin with structural formulas and the curly arrows that describe the flow of electrons (1.2), then functional groups and the oxidation states of carbon (1.3), then systematic nomenclature (1.4), a review of **hybrid orbitals** and bond parameters (1.5; the principles are in [6.1.3](/6.1.3)), and finally resonance theory (1.6). Molecular orbitals and electronic effects are treated in [6.5.2](/6.5.2), acids, bases and the energetics of reactions in [6.5.3](/6.5.3), stereochemistry (conformation and configuration) in [6.5.4](/6.5.4) and [6.5.5](/6.5.5), and structure determination in [6.5.6](/6.5.6).

## 1.1. The Subject and Methods of Organic Chemistry

The position of carbon in the periodic table makes it uniquely suited to building complex molecules. Carbon has four valence electrons, neither loses nor gains electrons easily, and tends to form four **covalent bonds**. The C–C and C–H bonds are both strong (average **bond enthalpies** of about $346$ and $413\,\mathrm{kJ\,mol^{-1}}$), carbon atoms can be joined into chains and rings of any length (catenation), and carbon forms double and triple bonds. The **electronegativity** of carbon (2.55) is close to that of hydrogen (2.20), so the C–H bond is almost nonpolar. The skeleton of an organic molecule is therefore stable at room temperature, and reactions occur mainly at sites that contain heteroatoms (O, N, S, halogens) or π bonds, that is, at functional groups (1.3). More than a hundred million organic compounds have been registered.

The work of organic chemistry falls into four interdependent activities:

| Activity | Goal | Main methods | In this course |
|---|---|---|---|
| Separation | Obtain a single pure compound from a natural or synthetic mixture | Extraction, distillation, recrystallization, column chromatography | [6.4.13](/6.4.13), [6.4.14](/6.4.14) |
| Structure determination | Establish the elemental composition, the connectivity of the atoms and their spatial arrangement | Elemental analysis, mass spectrometry, infrared spectroscopy, nuclear magnetic resonance, single-crystal X-ray diffraction | [6.5.6](/6.5.6) |
| Synthesis | Prepare a compound of known structure by artificial means | Combination of reactions and retrosynthetic analysis | [6.5.20](/6.5.20), [6.5.22](/6.5.22) |
| Mechanistic study | Establish the steps by which a reaction proceeds and the order in which bonds break and form | Identification of products and intermediates, kinetics, isotopic labeling, in situ spectroscopy, computation | [6.5.3](/6.5.3) |

In the nineteenth century structure determination relied on elemental analysis and chemical degradation, and the structure of a complex natural product often took decades to settle. Today mass spectrometry and two-dimensional NMR can solve it in a few days from a few milligrams, and a crystal can give the three-dimensional structure directly by X-ray diffraction.

Studying organic chemistry differs from studying physical chemistry. Organic chemistry is first of all an inductive science, and a great many reactions have to be remembered; but once reactions are organized by structure and by mechanism, they cease to be isolated facts. In analyzing a reaction one should be clear about four things: where the electrons are concentrated in the molecule (electron distribution), how the atoms are arranged in space (stereostructure), where the reactive sites are (the functional group and the $\alpha$ and $\beta$ positions that it influences), and where the electrons flow from and to in the reaction (the curly arrows of 1.2.2).

## 1.2. Structural Formulas and Curly Arrows

### 1.2.1. Structural Formulas

There are several ways to write the structure of an organic molecule. A **Lewis structure** shows all valence electrons. A dash formula draws bonding electron pairs as lines and usually omits lone pairs. A condensed formula writes the atoms attached to a given carbon together, as in $\ce{CH3CH2CH(CH3)OH}$. The most common is the skeletal formula.

**Definition 1.2.1 (Skeletal Formula)** A structural formula that represents the carbon chain by a zigzag line is called a **skeletal formula**. Each end point and each vertex stands for a carbon atom; hydrogen atoms bonded to carbon are not drawn (they are supplied by the tetravalence of carbon); heteroatoms and the hydrogen atoms bonded to them must be written; double and triple bonds are drawn as two and three lines.

For example, ibuprofen and ethyl acetate:

```smiles
CC(C)Cc1ccc(cc1)C(C)C(=O)O
CCOC(C)=O
```

The zigzag of a skeletal formula approximates the real bond angle of an sp³ carbon chain (about $109.5^\circ$). Three-dimensional structure is shown with wedged bonds (toward the viewer) and hashed wedges (away from the viewer); see [6.5.5](/6.5.5#sec-5.3.1).

When drawing a structure one must indicate the **formal charge** correctly: the formal charge of an atom is the number of valence electrons minus the number of electrons in lone pairs minus the number of bonds ([6.1.3](/6.1.3#sec-3.2.2)). The common cases in organic molecules can simply be memorized:

| Atom | Neutral | Positive | Negative |
|---|---|---|---|
| C | 4 bonds | 3 bonds, no lone pair (**carbocation**) | 3 bonds, 1 lone pair (**carbanion**) |
| N | 3 bonds, 1 lone pair | 4 bonds (ammonium, iminium) | 2 bonds, 2 lone pairs (amide anion) |
| O | 2 bonds, 2 lone pairs | 3 bonds, 1 lone pair (oxonium) | 1 bond, 3 lone pairs (alkoxide) |
| Halogen X | 1 bond, 3 lone pairs | 2 bonds, 2 lone pairs (halonium) | no bond, 4 lone pairs (halide) |

A carbon atom with three bonds and one unpaired electron is a neutral **radical** ([6.5.7](/6.5.7#sec-7.1.2)).

### 1.2.2. Curly Arrows

The essence of an organic reaction is the redistribution of electrons: old bonds break and new bonds form. Organic chemistry records where the electrons go with an agreed symbol.

**Definition 1.2.2 (Curly Arrow)** An arc-shaped arrow that describes the movement of electrons is called a **curly arrow**. A double-barbed arrow shows the movement of an electron pair; a single-barbed arrow (fishhook arrow) shows the movement of one electron. The tail points to where the electrons start (a lone pair or a bond) and the head points to where they end up: a head pointing at an atom means that the electrons become a lone pair on that atom; a head pointing between two atoms means that a new bond forms between them.

The rules for writing curly arrows are:

1. An arrow starts from electrons, not from a nucleus or a positive charge: it starts from a lone pair or a bond, never from an H atom or a carbocation.
2. The head must end where the result is a reasonable Lewis structure: an element of the second period (C, N, O) cannot have more than 8 valence electrons. If an atom that already has a full octet receives a new bond, it must lose one bond at the same time, which requires a second arrow.
3. Charge is conserved: the total charge is the same on both sides of each step; the atom at the head of an arrow has its formal charge reduced, and the atom at the tail has its formal charge increased.
4. An arrow represents one electron movement only; several simultaneous movements are drawn as several arrows, joined head to tail (consistent flow of electrons).

![Curly-arrow rule 2: when hydroxide attacks the carbonyl carbon of acetone, the carbon already has an octet, so the C=O π electrons must move onto oxygen at the same time (second arrow); the two arrows run head to tail and give a tetrahedral alkoxide](./plots/carbonyl-addition.py)

![Basic electron movements: (a) nucleophilic attack with simultaneous departure of the leaving group (SN2); (b) departure of the leaving group to give a carbocation; (c) proton transfer; (d) 1,2-methyl shift of a carbocation; (e) homolysis shown with fishhook arrows](./plots/arrow-patterns.py)

Parts (a)–(d) of the figure are the four basic steps of polar reactions, and nearly every ionic mechanism is a combination of them:

| Basic step | Movement of electrons | Example |
|---|---|---|
| Nucleophilic attack | A lone pair or π electrons of an electron-rich center attack an electron-poor center and form a new bond | A carbocation combining with water; addition to a carbonyl group ([6.5.16](/6.5.16#sec-16.2)) |
| Loss of a leaving group | The electron pair of the bond stays entirely with the more electronegative partner (heterolysis) | Ionization of an alkyl halide to a carbocation ([6.5.8](/6.5.8#sec-8.2.3)) |
| Proton transfer | A lone pair of a base takes up a proton, and the electrons of the original X–H bond remain on X | Acid–base reactions ([6.5.3](/6.5.3#sec-3.1.1)) |
| Rearrangement | A group migrates with its bonding pair to an adjacent electron-deficient atom | Carbocation rearrangement ([6.5.30](/6.5.30)) |

What these steps have in common is that electrons flow from electron-rich positions to electron-poor ones: electron-rich species (negatively charged, or having lone pairs or π bonds) attack electron-poor species (positively charged, having empty orbitals, or carrying a partial positive charge). The two kinds of species are called **nucleophiles** and **electrophiles**, respectively; see Definition 8.1.1.

When a covalent bond breaks and the two electrons go to the two atoms one each, the process is called **homolysis**; it produces radicals and is drawn with two fishhook arrows, as in (e). When the bonding pair goes entirely to one partner, the process is called **heterolysis**; it produces ions and is drawn with one double-barbed arrow, as in (b).

### 1.2.3. Classification of Organic Reactions

By outcome, organic reactions are classified as substitution, addition, elimination and rearrangement. By mechanism they are classified as ionic (polar) reactions, radical reactions and **pericyclic reactions** (concerted reactions through a cyclic transition state, [6.5.12](/6.5.12#sec-12.1)). Relating the structural features of the substrate to the two classifications gives a rough map of the reactions in this course:

| Structural feature of the substrate | Attacking reagent | Typical reaction | Chapter |
|---|---|---|---|
| Nonpolar C–C and C–H bonds | Radical | Radical substitution (halogenation) | [6.5.7](/6.5.7) |
| Polar $\mathrm{C}^{\delta+}$–$\mathrm{X}^{\delta-}$ bond (X = halogen, sulfonate) | Electron-rich reagent | Nucleophilic substitution | [6.5.8](/6.5.8) |
| As above, with H on the $\beta$ carbon | Base | Elimination to give C=C | [6.5.9](/6.5.9) |
| C–OH, C–OR (poor leaving groups) | First protonated in acid, or converted to a good leaving group | Substitution, elimination | [6.5.9](/6.5.9), [6.5.10](/6.5.10) |
| Electron-rich C=C, C≡C | Electron-poor reagent ($\ce{H+}$, $\ce{Br2}$, etc.) | Electrophilic addition | [6.5.11](/6.5.11) |
| Aromatic ring | Electron-poor reagent | Electrophilic substitution | [6.5.14](/6.5.14) |
| Polar $\mathrm{C}^{\delta+}$=$\mathrm{O}^{\delta-}$ | Electron-rich reagent | Nucleophilic addition | [6.5.16](/6.5.16) |
| Carbonyl group with a leaving group, $\mathrm{RC(=O)Y}$ | Electron-rich reagent | Addition–elimination, that is, nucleophilic acyl substitution | [6.5.19](/6.5.19) |
| $\alpha$-H of a carbonyl group | Base | Formation of an enolate, then reaction with an electrophile | [6.5.21](/6.5.21) |

![Two polar reactions written with the basic steps: (a) addition of HBr to ethene in two steps, in which the C=C π electrons take the proton (the H–Br bonding pair stays on bromine) and bromide then attacks the carbocation; (b) elimination (E2) from bromoethane in one step, in which ethoxide removes a β-H, the C–H bonding pair becomes the C=C π bond and bromide leaves](./plots/reaction-classes.py)

## 1.3. Functional Groups and Oxidation States of Carbon

### 1.3.1. Functional Groups

**Definition 1.3.1 (Functional Group)** The atom or group of atoms in a molecule that determines the main chemical properties of a class of compounds is called a **functional group**.

Compounds with the same functional group have similar properties, so organic compounds are classified by functional group. A functional group not only reacts itself but also activates the positions next to it (the $\alpha$-H of a carbonyl group, the allylic position of a double bond, the benzylic position of an aromatic ring). The common classes are:

| Class | Functional group | Example | Main chapters |
|---|---|---|---|
| Alkanes | None (only C–C and C–H single bonds) | $\ce{CH3CH2CH3}$ propane | [6.5.4](/6.5.4), [6.5.7](/6.5.7) |
| Alkenes, alkynes | C=C, C≡C | $\ce{CH2=CH2}$ ethene, $\ce{HC#CH}$ ethyne | [6.5.11](/6.5.11) |
| Arenes | Benzene ring and other aromatic rings | $\ce{C6H5CH3}$ toluene | [6.5.13](/6.5.13)–[6.5.15](/6.5.15) |
| Alkyl halides | C–X (X = F, Cl, Br, I) | $\ce{CH3CH2Br}$ bromoethane | [6.5.8](/6.5.8) |
| Alcohols, phenols | C–OH (phenol: OH on an aromatic ring) | $\ce{CH3CH2OH}$ ethanol, $\ce{C6H5OH}$ phenol | [6.5.10](/6.5.10), [6.5.15](/6.5.15) |
| Ethers | C–O–C | $\ce{CH3CH2OCH2CH3}$ diethyl ether | [6.5.10](/6.5.10) |
| Thiols, sulfides | C–SH, C–S–C | $\ce{CH3SH}$ methanethiol | [6.5.26](/6.5.26) |
| Amines | C–N (N is sp³, bearing H or hydrocarbon groups) | $\ce{CH3NH2}$ methanamine | [6.5.23](/6.5.23) |
| Aldehydes, ketones | C=O (aldehyde: the carbonyl carbon bears at least one H) | $\ce{CH3CHO}$ acetaldehyde, $\ce{CH3COCH3}$ acetone | [6.5.16](/6.5.16), [6.5.17](/6.5.17) |
| Carboxylic acids | –COOH | $\ce{CH3COOH}$ acetic acid | [6.5.18](/6.5.18) |
| Carboxylic acid derivatives | –COX, –COOCO–, –COOR, –CONR₂ | Acetyl chloride, acetic anhydride, ethyl acetate, acetamide | [6.5.19](/6.5.19), [6.5.20](/6.5.20) |
| Nitriles | –C≡N | $\ce{CH3CN}$ acetonitrile | [6.5.20](/6.5.20) |
| Nitro compounds | –NO₂ | $\ce{CH3NO2}$ nitromethane | [6.5.24](/6.5.24) |

Common abbreviations for groups are Me (methyl), Et (ethyl), Pr (propyl), $i$-Pr (isopropyl), Bu (butyl), $t$-Bu (*tert*-butyl), Ph (phenyl), Bn (benzyl, $\ce{C6H5CH2-}$), Ac (acetyl, $\ce{CH3CO-}$), Ar (any aryl group) and R (any hydrocarbon group); in sulfonates, Ts (4-methylbenzenesulfonyl, tosyl), Ms (methanesulfonyl, mesyl) and Tf (trifluoromethanesulfonyl, triflyl).

### 1.3.2. Oxidation States of Carbon

To decide whether an organic reaction is a redox reaction, we compare the **oxidation states** of the carbon atoms. The rules are the same as in inorganic chemistry ([6.1.11](/6.1.11)): the electrons of every bond are assigned entirely to the more electronegative atom, and the charge of the atom is then counted (unlike the calculation of formal charge, where each bond is divided equally). For a carbon atom this is equivalent to the following count:

- each bond to an atom more electronegative than carbon (O, N, S, halogen): $+1$; double and triple bonds count 2 and 3;
- each bond to H or to an atom less electronegative than carbon (metals, B, Si): $-1$;
- a C–C bond: $0$; a positive charge on carbon counts $+1$ and a negative charge $-1$.

For example, C is $-4$ in $\ce{CH4}$, $-2$ in $\ce{CH3OH}$, $0$ in $\ce{HCHO}$, $+2$ in $\ce{HCOOH}$ and $+4$ in $\ce{CO2}$. Since organic reactions seldom change C–C bonds, it is more convenient to count how many bonds to heteroatoms a carbon atom has; this gives the oxidation level of carbon:

| Number of bonds to heteroatoms | 0 | 1 | 2 | 3 | 4 |
|---|---|---|---|---|---|
| Level | Alkanes | Alcohols, alkyl halides, amines, ethers | Aldehydes, ketones, imines, geminal dihalides, acetals | Carboxylic acids and derivatives, nitriles, orthoesters | Carbon dioxide, carbonic acid derivatives (urea, phosgene, carbonates) |

C=C and C≡C must also be counted: addition of water does not change the oxidation state, so alkenes are at the same level as alcohols, and alkynes at the same level as aldehydes and ketones. Interconversions within a level are not redox reactions, for example alcohol ⇌ alkyl halide ⇌ ether, aldehyde ⇌ acetal ⇌ imine, ester ⇌ amide ⇌ nitrile. Moving up a level is oxidation (alcohol → aldehyde → carboxylic acid), and moving down is reduction. When an alkene adds water to give an alcohol, the sum of the oxidation states of the two carbons is unchanged ($-2-2 \to -3-1$), so hydration is not a redox reaction, whereas addition of $\ce{Br2}$ to an alkene to give a vicinal dibromide is an oxidation. A simple rule of thumb: addition of hydrogen and removal of oxygen (or of a heteroatom) is reduction, removal of hydrogen and addition of oxygen is oxidation, and addition of $\ce{H2O}$ or $\ce{HX}$ does not change the oxidation state.

**Example 1.3.1** Ethanol is oxidized to acetaldehyde and then to acetic acid (left to right):

```smiles
CCO
CC=O
CC(=O)O
```

The methyl carbon stays at $-3$; the carbon bonded to O goes through $-1$ (ethanol), $+1$ (acetaldehyde) and $+3$ (acetic acid), losing two electrons in each step, so each step needs a two-electron oxidant ([6.5.10](/6.5.10#sec-10.6)).

## 1.4. Systematic Nomenclature

### 1.4.1. The Nomenclature System

The purpose of systematic nomenclature is to let a structure be written unambiguously from a name, and a name unambiguously from a structure. The current international rules are the IUPAC 2013 recommendations on organic nomenclature (*Nomenclature of Organic Chemistry: IUPAC Recommendations and Preferred Names 2013*, rules P-1 to P-10). They prescribe a *preferred IUPAC name* (PIN) for each compound, while permitting other acceptable names and retained trivial names in general use. Chinese names follow the *Principles of Nomenclature of Organic Compounds* of the Chinese Chemical Society (2017), which agrees with IUPAC 2013 on all the main rules. This section gives the general principles that apply to all classes of compounds; the special rules for particular classes are introduced at the beginning of the relevant chapters, and the stereodescriptors ($R$/$S$, $Z$/$E$) are treated in [6.5.5](/6.5.5).

**Definition 1.4.1 (Substitutive Nomenclature)** The method of naming a compound as the product of replacing hydrogen atoms of a parent hydride by atoms or groups is called **substitutive nomenclature**. The unbranched chain or ring hydrocarbon, for example, that serves as the basis of the name is called the **parent hydride**; the one functional group that is chosen by order of seniority and written as the suffix of the name is called the **principal characteristic group**, and all other substituents are written as prefixes.

A name in substitutive nomenclature consists of the following parts, in order:

| Stereodescriptor | Substituent prefixes (alphabetical) | Parent hydride | Unsaturation ending | Principal characteristic group suffix |
|---|---|---|---|---|
| $(2E)$- | 4-hydroxy- | hex | -2-en | -al |

The name is $(2E)$-4-hydroxyhex-2-enal, $\ce{CH3CH2CH(OH)CH=CHCHO}$. Each locant is placed immediately before the part of the name it modifies (hex-2-enal); this is the style of the 2013 recommendations and of the Chinese rules of 2017. The older style placed all locants at the front (2-hexenal) and is still very common in the literature.

Names of the chain parent hydrides:

| Number of carbons | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 20 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Name | methane | ethane | propane | butane | pentane | hexane | heptane | octane | nonane | decane | undecane | dodecane | icosane |

Removing one hydrogen gives a substituent group, whose name is obtained by changing the ending -ane to -yl: methyl, ethyl. When the hydrogen is removed from a carbon in the middle of the chain, the locant is written before -yl: propan-2-yl (commonly called isopropyl). Unsaturation is expressed by the endings -ene and -yne; a compound with both a double and a triple bond is named with -en-…-yne, as in pent-1-en-4-yne.

*Correspondence with the Chinese names.* A Chinese name is built from the same elements in the same order as the English name: stereodescriptor, substituent prefixes, parent hydride, unsaturation, principal characteristic group. The parent hydride is named by one character for the number of carbons (a traditional numeral character for the first ten, ordinary numerals above that) followed by one character for the class, which corresponds to the ending -ane, -ene, -yne and so on; characters for the suffixes (-ol, -al, -one, -oic acid, -amine) take the place of the class character. Locants are written in Arabic numerals joined by hyphens and, as in English, stand immediately before the part they modify, and the prefixes of a Chinese name are arranged in the alphabetical order of the corresponding English names. Because the correspondence is element by element, the tables below give the English names only; a Chinese name can be formed from each by translating every element and keeping the order and the locants.

### 1.4.2. Seniority of Principal Characteristic Groups

When a compound contains several functional groups, only the one of highest seniority is written as the suffix, and the others are written as prefixes. The part of the order prescribed by IUPAC 2013 (P-41) that is relevant to this course is as follows (from highest to lowest):

| Order | Class | Suffix | Prefix |
|---|---|---|---|
| 1 | Carboxylic acids | -oic acid, -carboxylic acid | carboxy |
| 2 | Sulfonic acids | -sulfonic acid | sulfo |
| 3 | Anhydrides | -oic anhydride | none |
| 4 | Esters | alkyl -oate | alkoxycarbonyl |
| 5 | Acid halides | -oyl halide | halocarbonyl |
| 6 | Amides | -amide | carbamoyl |
| 7 | Nitriles | -nitrile, -carbonitrile | cyano |
| 8 | Aldehydes | -al, -carbaldehyde | formyl, oxo |
| 9 | Ketones | -one | oxo |
| 10 | Alcohols, phenols | -ol | hydroxy |
| 11 | Thiols | -thiol | sulfanyl |
| 12 | Amines | -amine | amino |
| 13 | Imines | -imine | imino |

Halogens (fluoro, chloro, bromo, iodo), the nitro group (nitro), alkoxy groups (alkoxy, that is, ethers) and alkylsulfanyl groups can be expressed only as prefixes, never as suffixes. Some remarks:

- The suffixes -carboxylic acid, -carbonitrile and -carbaldehyde are used when the carbon of the functional group cannot be counted in the parent, chiefly when it is attached to a ring: cyclohexanecarboxylic acid; the systematic name of benzaldehyde is benzenecarbaldehyde.
- Esters, acid halides, anhydrides and so on are also often named by *functional class nomenclature*: ethyl acetate, acetyl chloride. Ethers and alkyl halides are also named by class in general use, as diethyl ether and ethyl bromide, but their preferred names are substitutive names (ethoxyethane, bromoethane).
- The prefix "oxo" (=O) is rendered in the 2017 Chinese rules by a term that replaces an older Chinese term; both correspond to the English prefix oxo, and the prefix order of IUPAC 2013 applies in either language.

### 1.4.3. Choosing and Numbering the Principal Chain

For acyclic compounds the principal chain is selected first and then numbered. IUPAC 2013 selects the principal chain by the following criteria in order; when an earlier one decides, the later ones are not considered:

1. the greatest number of principal characteristic groups (suffixes);
2. when a ring and a chain compete, the ring is the parent (see 1.4.4);
3. the longest chain;
4. the greatest number of multiple bonds (double and triple);
5. the greatest number of double bonds;
6. lower locants for principal characteristic groups, multiple bonds and substituents, in that order, according to the numbering rules below;
7. the greatest number of substituents.

The order of criteria 3 and 4 is the largest difference between the 2013 recommendations and the older rules (1979, 1993): the old rules first required the principal chain to contain as many multiple bonds as possible and only then compared length. For example, $\ce{CH2=C(CH2CH2CH3)CH2CH2CH2CH3}$ is now named 4-methylideneoctane (the principal chain is the saturated eight-carbon chain), whereas the old rules gave 2-propylhex-1-ene. The 2017 rules of the Chinese Chemical Society adopt the new order.

In numbering, the following are given the lowest possible locants in turn ("lowest locants" means that the sets are compared term by term and the set with the lower number at the first point of difference is lower, so 2,3,5 is lower than 2,4,4):

1. principal characteristic groups (suffixes);
2. unsaturation (double and triple bonds considered together; if a choice remains, double bonds first);
3. all substituent prefixes together;
4. if a choice still remains, the substituent cited first in alphabetical order.

Substituent prefixes in a name are arranged in the alphabetical order of their English names. The multiplying prefixes di-, tri-, tetra- do not count in the ordering, but the first letter of the name of a compound substituent does (for example (1,2-dimethylpropyl) is alphabetized under d); iso counts, sec- and tert- do not. The Chinese rules of 2017 likewise order the substituents in a Chinese name by the alphabetical order of their English names; the older Chinese rules ordered them by a "sequence rule" from simple to complex, so that 2-methyl-3-ethylpentane, the old name, is now written 3-ethyl-2-methylpentane.

The following examples illustrate these rules (the numbering corresponds to the numbers in the table):

```smiles
CCC(CC)C(C)C 1
CC(O)CC(C)=O 2
CC(N)CC(=O)O 3
C=CCC#C 4
OCC=C 5
CC(=O)N(C)C 6
```

| No. | Name | Remarks |
|---|---|---|
| 1 | 3-ethyl-2-methylpentane | Two five-carbon chains are equally long, so the one with more branches is chosen; ethyl precedes methyl alphabetically |
| 2 | 4-hydroxypentan-2-one | A ketone has priority over an alcohol, the carbonyl group gets the lowest locant and OH is written as a prefix |
| 3 | 3-aminobutanoic acid | The carboxyl carbon is C1 |
| 4 | pent-1-en-4-yne | Both directions give 1,4; the double bond gets the lower locant |
| 5 | prop-2-en-1-ol | The suffix -ol has priority over -ene for the lower locant; trivial name allyl alcohol |
| 6 | $N$,$N$-dimethylacetamide | Substitution on a heteroatom uses the element symbol as the locant |

### 1.4.4. Rings, Spiro Compounds and Bridged Compounds

A monocyclic alkane is named by adding cyclo- before the name of the chain: cyclohexane; as a substituent it is cyclohexyl. IUPAC 2013 prescribes that when a ring and a chain compete for the parent (with the same functional groups), the ring is always the parent and the number of carbons is not compared: $\ce{C6H13-C3H5}$ is hexylcyclopropane, not 1-cyclopropylhexane. In a ring, the numbering gives functional groups, multiple bonds and substituents the lowest locants in turn: 2-chlorocyclohexan-1-one, 3-methylcyclohex-1-ene.

For benzene derivatives, monosubstituted compounds are named by placing the prefix before benzene (chlorobenzene, nitrobenzene); disubstituted compounds use the locants 1,2-, 1,3- and 1,4-, and in general usage also *ortho*-, *meta*- and *para*- (abbreviated $o$-, $m$-, $p$-). Many benzene derivatives have retained names that can also serve as parents for further substitution, such as phenol, aniline and benzoic acid: 4-aminobenzoic acid (*para*-aminobenzoic acid). Benzene as a substituent is phenyl, and $\ce{C6H5CH2-}$ is benzyl. Most fused aromatic hydrocarbons (naphthalene, anthracene, phenanthrene) and heterocycles are named with retained names; see [6.5.13](/6.5.13#sec-13.10) and [6.5.25](/6.5.25#sec-25.1.2).

**Definition 1.4.2 (Spiro Compound)** A compound in which two rings share only one atom (the spiro atom) is called a **spiro compound**. A monospiro alkane is named spiro[$a$.$b$]alkane: the brackets give, in increasing order, the numbers of atoms in each ring on either side of the spiro atom (not counting the spiro atom), and alkane indicates the total number of ring atoms. Numbering begins at the ring atom next to the spiro atom in the smaller ring, goes around the smaller ring, passes through the spiro atom and continues around the larger ring.

**Definition 1.4.3 (Bridged Compound)** A saturated bicyclic or polycyclic compound in which two rings share two or more atoms is called a **bridged compound**. According to the von Baeyer rules, a bicyclic alkane is named bicyclo[$a$.$b$.$c$]alkane: the two shared atoms are called bridgeheads, $a \ge b \ge c$ are the numbers of atoms (not counting the bridgeheads) on the three bridges that connect the two bridgeheads, and alkane indicates the total number of ring atoms. Numbering begins at one bridgehead, proceeds along the largest bridge to the other bridgehead, returns along the next largest bridge, and finally numbers the smallest bridge (starting from the end nearer the first bridgehead).

A fused bicycle (two rings sharing one bond) is the special case $c = 0$ in von Baeyer nomenclature; for example decalin is bicyclo[4.4.0]decane. For bridged systems with three or more rings, the positions of the secondary bridges must also be given; adamantane, for example, is tricyclo[3.3.1.1³,⁷]decane.

```smiles
C1CCC2(C1)CCCCC2 7
C1CC2CC1C2 8
C1CC2C=CC1C2 9
CC1(C)C2CCC1(C)C(=O)C2 10
C1CCC2CCCCC2C1 11
```

| No. | Name | Remarks |
|---|---|---|
| 7 | spiro[4.5]decane | The spiro atom is C5 |
| 8 | bicyclo[2.2.1]heptane | Trivial name norbornane |
| 9 | bicyclo[2.2.1]hept-2-ene | The double bond is on the largest bridge and gets the lowest locant |
| 10 | 1,7,7-trimethylbicyclo[2.2.1]heptan-2-one | Camphor; C7 is the one-carbon bridge |
| 11 | bicyclo[4.4.0]decane | Decalin |

### 1.4.5. Common Trivial Names and Substituent Names

Many simple substituent groups and compounds retain trivial names in general nomenclature. Some of these (such as acetic acid, acetone, phenol, aniline and benzoic acid) are themselves preferred IUPAC names, while others are replaced by systematic names in preferred names:

| Structure | Trivial name | Systematic name |
|---|---|---|
| $\ce{(CH3)2CH-}$ | isopropyl | propan-2-yl |
| $\ce{(CH3)2CHCH2-}$ | isobutyl | 2-methylpropyl |
| $\ce{CH3CH2CH(CH3)-}$ | *sec*-butyl | butan-2-yl |
| $\ce{(CH3)3C-}$ | *tert*-butyl | 2-methylpropan-2-yl |
| $\ce{(CH3)3CCH2-}$ | neopentyl | 2,2-dimethylpropyl |
| $\ce{CH2=CH-}$ | vinyl | ethenyl |
| $\ce{CH2=CHCH2-}$ | allyl | prop-2-en-1-yl |
| $\ce{C6H5CH2-}$ | benzyl | phenylmethyl |
| $\ce{CH3CO-}$ | acetyl | acetyl (retained) |
| $\ce{HCOOH}$, $\ce{CH3COOH}$ | formic acid, acetic acid | retained as preferred names |
| $\ce{CH3COCH3}$ | acetone | retained as the preferred name (propan-2-one) |
| $\ce{CH3CH2OCH2CH3}$ | diethyl ether | ethoxyethane |

Carbon atoms are classified as primary (1°), secondary (2°), tertiary (3°) and quaternary (4°) according to the number of carbon atoms attached to them, and the hydrogen atoms on primary, secondary and tertiary carbons are called primary, secondary and tertiary hydrogens. Alcohols, alkyl halides, carbocations and radicals are likewise classified as primary, secondary or tertiary by the carbon that bears the functional group. The classification of amines as primary, secondary and tertiary is by the number of hydrocarbon groups on nitrogen ([6.5.23](/6.5.23#sec-23.1.1)) and is different.

## 1.5. A Review of Bonding and Hybridization

The bonding geometry of carbon, nitrogen and oxygen in organic molecules can be described uniformly by **hybrid orbitals** and **valence shell electron pair repulsion theory** ([6.1.3](/6.1.3#sec-3.4), [6.1.3](/6.1.3#sec-3.5)). The usual way to determine the hybridization is to write the Lewis structure and count the sum $m$ of the σ bonds and lone pairs on the central atom; $m = 4, 3, 2$ correspond to sp³, sp², sp.

| Hybridization | Geometry | Bond angle | s character | Carbon examples | Heteroatom examples |
|---|---|---|---|---|---|
| sp³ | Tetrahedral | $109.5^\circ$ | 25% | Alkanes | N of amines (trigonal pyramidal), O of alcohols and ethers (bent) |
| sp² | Trigonal planar | $120^\circ$ | 33% | Alkenes, carbonyl groups, benzene ring, carbocations | N of imines, O of carbonyl groups |
| sp | Linear | $180^\circ$ | 50% | Alkynes, nitriles, central carbon of allenes | N of nitriles |

There is one important exception: a lone pair next to a π system and taking part in conjugation occupies a p orbital, and such N and O atoms are sp² hybridized, as in the N of amides, anilines and enamines and the O of furan (1.6.3, [6.5.2](/6.5.2#sec-2.5.1)).

Hybridization affects bond length, bond strength and the electronegativity of the atom. The greater the s character, the closer the hybrid orbital lies to the nucleus, the greater the effective electronegativity of C, the shorter and stronger the C–H bond, and the stronger the acidity of the C–H bond (the $\mathrm{p}K_{\mathrm{a}}$ values of ethane, ethene and ethyne are about 50, 44 and 25, [6.5.3](/6.5.3#sec-3.1.4)). Some typical bond parameters (**bond lengths** and **bond dissociation energies** at 298 K) are:

| Bond | Length / pm | Bond dissociation energy / (kJ mol⁻¹) | Bond | Length / pm | Bond dissociation energy / (kJ mol⁻¹) |
|---|---|---|---|---|---|
| $\ce{CH3CH2-H}$ (sp³ C–H) | 109 | 423 | $\ce{CH3-CH3}$ (C–C) | 153 | 377 |
| $\ce{CH2=CH-H}$ (sp² C–H) | 108 | 463 | $\ce{CH2=CH2}$ (C=C) | 133 | 728 |
| $\ce{HC#C-H}$ (sp C–H) | 106 | 558 | $\ce{HC#CH}$ (C≡C) | 120 | 965 |

(The bond dissociation energy is the enthalpy needed to break one specific bond in a molecule and differs from the mean bond enthalpy of 1.1; see Definition 7.2.2.)

The direction of a **polar bond** is determined by electronegativity. The C–O, C–N and C–X bonds in organic molecules are all polar covalent bonds in which the electrons are displaced toward the heteroatom and carbon carries a partial positive charge $\delta^+$; even with an electronegativity difference above 1.7, the C–F bond is covalent, and "an electronegativity difference above 1.7 means an ionic bond" is only a rough empirical boundary. The polarity of a molecule is determined by the vector sum of the bond dipoles: $\ce{CCl4}$ contains polar bonds but is a nonpolar molecule. The unit of **electric dipole moment** is $\mathrm{C\,m}$, but in organic chemistry the debye is customary ($1\,\mathrm{D} = 3.336\times10^{-30}\,\mathrm{C\,m}$): $\ce{CH3Cl}$ has $1.9\,\mathrm{D}$ and $\ce{CH3CN}$ has $3.9\,\mathrm{D}$.

Carbon is not always tetravalent and four-coordinate. In the iron–molybdenum cofactor of nitrogenase there is a carbon atom bonded to six Fe atoms, and the carbon in $\ce{[C(AuPPh3)6]^2+}$ is also six-coordinate; the bonding of such hypercoordinate carbon involves multicenter bonds and cannot be described by two-center two-electron bonds.

## 1.6. Resonance Theory

### 1.6.1. Why Resonance Theory Is Needed

In a Lewis structure each bonding pair belongs to only two atoms (it is localized). The real structure of many molecules and ions cannot be represented by one such formula:

- In the Lewis structure of the allyl cation $\ce{CH2=CH-CH2+}$ one C–C bond is double and the other single, but the two C–C bonds are found to be equal in length, and the two terminal carbons carry the positive charge equally;
- The two C–O bonds of a carboxylate $\ce{RCOO-}$ have equal lengths (about $126\,\mathrm{pm}$, between the $121\,\mathrm{pm}$ of C=O and the $134\,\mathrm{pm}$ of C–O), and the two oxygens carry the negative charge equally;
- The six C–C bonds of benzene have equal lengths ($139\,\mathrm{pm}$), whereas the Kekulé structure has alternating single and double bonds.

All these systems contain a set of adjacent, mutually parallel p orbitals in which the electrons are delocalized (**delocalized π bonds**, [6.1.3](/6.1.3#sec-3.4.4)). Molecular orbital theory describes delocalization directly ([6.5.2](/6.5.2#sec-2.2)), but organic chemists prefer to think in Lewis structures, and Pauling therefore developed resonance theory.

**Definition 1.6.1 (Resonance Theory)** If a molecule, ion or radical can be written, following the rules of valence, as two or more Lewis structures that have the same positions of the atoms and differ only in the distribution of electrons, its real structure is a superposition of these structures, and this description is called **resonance theory**. Each Lewis structure is called a **resonance structure** (contributing structure), and the real structure is called the **resonance hybrid**. Resonance structures are connected by a double-headed arrow $\leftrightarrow$.

Resonance structures are only a tool of description and do not themselves exist: the resonance hybrid is one definite, single structure and cannot be replaced by any one of the resonance structures.

### 1.6.2. Rules for Writing Resonance Structures

1. The positions of the nuclei and the connectivity are the same in all resonance structures; only the positions of π electrons and lone pairs change, and single (σ) bonds are not broken.
2. Every resonance structure must be a reasonable Lewis structure: an element of the second period has no more than 8 valence electrons (it may have fewer than 8, as in a carbocation).
3. All resonance structures have the same number of unpaired electrons and the same total charge.
4. When one resonance structure is derived from another, curly arrows show the movement of electrons; an arrow starts from a π bond or a lone pair and points to an adjacent atom or bond.

Only four basic types of movement connect resonance structures: π electrons moving toward an adjacent positive charge (or empty orbital), π electrons moving along a conjugated chain, a lone pair moving into an adjacent bond to form a π bond, and single-electron movement (radicals, with fishhook arrows). The five structural units that occur most often in real systems are:

| Structural unit | Movement of electrons | Example |
|---|---|---|
| A lone pair (or negative charge) at the allylic position | The lone pair forms a π bond and the original π bond moves to the terminal position | Enolates, amides, enol ethers |
| A positive charge at the allylic position | A π bond moves toward the positive charge | Allyl cation, benzyl cation |
| A lone pair next to a positive charge | The lone pair forms a π bond and the positive charge moves onto the heteroatom | Protonated carbonyl groups, $\mathrm{H_2\overset{+}{C}{-}OR} \leftrightarrow \mathrm{H_2C{=}\overset{+}{O}R}$ |
| A π bond between different atoms | The π electrons move toward the more electronegative atom | $\mathrm{C{=}O} \leftrightarrow \mathrm{\overset{+}{C}{-}\overset{-}{O}}$ |
| A cyclic conjugated system | The π electrons move around the ring | The two Kekulé structures of benzene |

![Resonance structures and curly arrows: (a) the allyl cation; (b) the two equivalent resonance structures of acetate; (c) acetamide, in which the charge-separated structure on the right is a minor contributor; (d) the enolate of acetone, in which the structure with the negative charge on oxygen is the major contributor](./plots/resonance-examples.py)

To draw all resonance structures of a system, start from a change of "one arrow" and move step by step; drawing directly from long-distance electron movements makes it easy to miss intermediate resonance structures.

![Drawing all resonance structures of the pentadienyl cation one arrow at a time: each step moves one π bond toward the positive carbon, so the positive charge appears on C5, C3 and C1 in turn and never on C2 or C4](./plots/pentadienyl-resonance.py)

### 1.6.3. Contributions of Resonance Structures

Different resonance structures contribute differently to the hybrid: the more stable a resonance structure, the greater its contribution. The rules for judging stability, in order of importance, are:

1. The more atoms have a complete octet, the greater the contribution. For example, of the two resonance structures of protonated acetone, $\mathrm{C{=}\overset{+}{O}H}$ (C and O both have complete octets) contributes more than $\mathrm{\overset{+}{C}{-}OH}$ (C has only 6 valence electrons), although the latter places the positive charge on the less electronegative carbon.
2. The less charge separation, the greater the contribution: a resonance structure without formal charges is the most important; avoid two charges on the same atom.
3. When charges are unavoidable, structures with the negative charge on the more electronegative atom and the positive charge on the less electronegative atom contribute more. Of the two resonance structures of an **enolate**, the one with the negative charge on O contributes more (part (d) of the figure).
4. When the charges are on the same kind of atom, the closer the opposite charges and the farther apart the like charges, the greater the contribution.

![Resonance structures judged by the contribution rules: (a) the charge-separated structure of the carbonyl group puts the negative charge on the more electronegative oxygen and is a minor but real contributor (the C=O bond is polar); (b) the two resonance structures of nitromethane are equivalent, so the two N–O bonds have the same length and each oxygen carries half a negative charge; (c) both resonance structures of diazomethane carry formal charges; in the right one every atom has an octet and the negative charge is on carbon, which explains why the carbon of diazomethane is nucleophilic](./plots/resonance-contributions.py)

The consequences of resonance can be seen in three ways:

- The more equivalent resonance structures there are, and the closer to equivalent they are, the greater the stabilization due to delocalization. The two resonance structures of a carboxylate are exactly equivalent, which is one reason why carboxylic acids are much stronger acids than alcohols ($\mathrm{p}K_{\mathrm{a}}$ 4.76 and 15.9, [6.5.3](/6.5.3#sec-3.1.4)); the two Kekulé structures of benzene are equivalent, and the stabilization is very large ([6.5.13](/6.5.13#sec-13.1.2)).
- Minor resonance structures also have observable consequences. The charge-separated structure of an amide (part (c) of the figure) contributes considerably: the C–N bond of an amide (about $133$–$136\,\mathrm{pm}$) is shorter than that of an amine ($147\,\mathrm{pm}$), the amide group is planar, the barrier to rotation about the C–N bond is about $65$–$90\,\mathrm{kJ\,mol^{-1}}$, and N is hardly basic; these properties determine the structure of peptide chains ([6.5.33](/6.5.33)).
- Resonance structures mark where charge or an unpaired electron may be located, and hence mark the reactive sites. Both terminal carbons of the allyl cation can be attacked by a nucleophile; an enolate can react with electrophiles at both C and O ([6.5.21](/6.5.21#sec-21.4.1)).

### 1.6.4. Common Misconceptions

- A resonance hybrid is not a mixture of resonance structures, and the resonance structures are not in equilibrium: the molecule does not "flip back and forth" between them. This is why $\leftrightarrow$ is used between resonance structures and never the equilibrium arrow $\rightleftharpoons$.
- Resonance is different from **tautomerism**. Tautomers are different compounds that really exist and can be separated (or observed separately by spectroscopy), and their interconversion changes the position of an atom (usually H), for example acetone and its enol prop-1-en-2-ol ([6.5.21](/6.5.21#sec-21.2)); resonance structures differ only in the positions of electrons.
- The energy of the hybrid is lower than that of the hypothetical structure represented by any one resonance structure. This energy difference is called the resonance energy (**delocalization energy**); it cannot be measured directly, but is obtained only by comparison with a chosen reference structure (Definition 2.2.2, [6.5.13](/6.5.13#sec-13.1.2)).
- In the literature only one major resonance structure is often drawn for brevity (benzene is also often drawn as one Kekulé structure), and the reader must supply the delocalization.

![Tautomerism versus resonance: top, acetone and its enol (prop-1-en-2-ol) are two compounds connected by equilibrium arrows, and an H atom changes position; bottom, the two resonance structures of the enolate differ only in the positions of electrons and are connected by a double-headed arrow, and the atoms do not move](./plots/tautomer-vs-resonance.py)

Resonance theory is the language of valence bond theory, and it describes the same delocalization as molecular orbital theory: the number and equivalence of resonance structures qualitatively reflect the shape of the delocalized π molecular orbitals. In [6.5.2](/6.5.2#sec-2.2.2) we use the **Hückel molecular orbital method** to obtain, quantitatively and from the molecular orbital viewpoint, the charge distribution and delocalization stabilization of the allyl cation again.

## Summary

- The core of organic chemistry is structure and mechanism. In analyzing a reaction one must be clear about the electron distribution, the spatial arrangement of atoms, the reactive sites and the destination of the electrons.
- Skeletal formulas omit carbon and the hydrogens on carbon; the formal charge is determined by the number of bonds and lone pairs (C: three bonds and no lone pair is positive, with one lone pair is negative; N: four bonds is positive; O: three bonds is positive and one bond is negative).
- A curly arrow (Definition 1.2.2) starts from electrons and points to their destination, double-barbed for a pair of electrons and fishhook for one electron; polar reactions are combinations of the four basic steps nucleophilic attack, loss of a leaving group, proton transfer and rearrangement; bond cleavage is homolysis or heterolysis.
- Organic compounds are classified by functional group (Definition 1.3.1). The oxidation state of carbon is counted from bonds to heteroatoms and to hydrogen; interconversions within one oxidation level (alcohol ⇌ alkyl halide, aldehyde ⇌ acetal, ester ⇌ amide ⇌ nitrile) are not redox reactions.
- Systematic nomenclature (Definition 1.4.1): choose the principal characteristic group (carboxylic acid > sulfonic acid > anhydride > ester > acid halide > amide > nitrile > aldehyde > ketone > alcohol, phenol > thiol > amine > imine; halogens, nitro and ethers appear only as prefixes) → choose the principal chain (number of suffixes → ring preferred → longest chain → most multiple bonds) → number (suffix → unsaturation → all substituents → alphabetical order) → arrange prefixes alphabetically by English name, with each locant placed immediately before the part it modifies (hex-2-enal). Spiro compounds are spiro[$a$.$b$] (Definition 1.4.2) and bridged compounds are bicyclo[$a$.$b$.$c$] (Definition 1.4.3).
- sp³, sp² and sp hybridization correspond to tetrahedral, trigonal planar and linear geometry; the greater the s character, the greater the electronegativity of carbon and the shorter, stronger and more acidic the C–H bond; a lone pair taking part in conjugation makes N or O sp².
- Resonance theory (Definition 1.6.1): resonance structures differ only in the positions of π electrons and lone pairs; contributions are judged by octets → charge separation → match of charge and electronegativity → distance between charges; the resonance hybrid is a single real structure, and resonance is neither an equilibrium nor tautomerism.

## Questions

1. Identify the atoms that carry a formal charge, and the charge, in the following species: (a) $\ce{CH3O-}$; (b) $\ce{(CH3)3O+}$; (c) $\mathrm{CH_2{=}N{=}N}$ (one resonance structure of diazomethane, with double bonds between the two N atoms and two lone pairs on the terminal N); (d) nitromethane $\ce{CH3NO2}$ (N is double-bonded to one O and single-bonded to the other).

   **Answer** (a) O is $-1$ (1 bond, 3 lone pairs). (b) O is $+1$ (3 bonds, 1 lone pair). (c) The central N is $+1$ (4 bonds) and the terminal N is $-1$ (2 bonds, 2 lone pairs); the total charge is 0. (d) N is $+1$ (4 bonds) and the singly bonded O is $-1$; the total charge is 0, and the two O atoms of the nitro group are equivalent by resonance.
2. Which of the following pairs of structures are resonance structures of each other, and which are different compounds? (a) acetone $\ce{CH3COCH3}$ and prop-1-en-2-ol $\ce{CH2=C(OH)CH3}$; (b) the two structures of nitromethane $\mathrm{CH_3{-}\overset{+}{N}({=}O_a){-}\overset{-}{O}_b}$ and $\mathrm{CH_3{-}\overset{+}{N}({-}\overset{-}{O}_a){=}O_b}$; (c) cyclohexa-1,3-diene and cyclohexa-1,4-diene; (d) $\mathrm{CH_2{=}CH{-}O{-}CH_3}$ and $\mathrm{\overset{-}{C}H_2{-}CH{=}\overset{+}{O}{-}CH_3}$.

   **Answer** (b) and (d) are resonance structures: the positions of the atoms do not change, and only π electrons and lone pairs have moved. (a) are **tautomers**: H has moved from carbon to oxygen, and they are two real compounds. (c) are **constitutional isomers**: the positions of the H atoms on the ring differ, both are real dienes, and they cannot resonate with each other (the two double bonds of the 1,4-diene are separated by an sp³ carbon and are not conjugated).
3. Draw all resonance structures of $\ce{CH2=CH-CH=CH-CH2+}$ (the penta-2,4-dien-1-yl cation) and indicate on which carbons the positive charge may be located; which is more stable, this cation or the allyl cation?

   **Answer** There are three resonance structures: $\mathrm{CH_2{=}CH{-}CH{=}CH{-}\overset{+}{C}H_2} \leftrightarrow \mathrm{CH_2{=}CH{-}\overset{+}{C}H{-}CH{=}CH_2} \leftrightarrow \mathrm{\overset{+}{C}H_2{-}CH{=}CH{-}CH{=}CH_2}$, and the positive charge is distributed over C1, C3 and C5 (every other carbon). The positive charge is delocalized over a larger region with more resonance structures, so this cation is more stable than the allyl cation. The Hückel calculation of [6.5.2](/6.5.2#sec-2.2.4) leads to the same conclusion: C1, C3 and C5 each carry a charge of $+1/3$.
4. Calculate the oxidation states of the carbon atoms that change in the following transformations, and decide which are oxidations, which are reductions and which are not redox reactions: (a) ethene → ethanol; (b) ethanol → bromoethane; (c) acetaldehyde → acetic acid; (d) ethyne → acetaldehyde; (e) acetic acid → ethanol.

   **Answer** (a) The two carbons go $-2, -2 \to -3, -1$; the sum is unchanged, so this is not a redox reaction (hydration). (b) The carbon bonded to O goes $-1 \to -1$ (a C–Br bond also counts $+1$), so this is not a redox reaction (substitution). (c) The carbonyl carbon goes $+1 \to +3$: oxidation. (d) The two carbons go $-1, -1 \to -3, +1$; the sum is unchanged, so this is not a redox reaction (hydration of an alkyne, [6.5.11](/6.5.11#sec-11.5)). (e) $+3 \to -1$: a four-electron reduction (for example with $\ce{LiAlH4}$).
5. Give the systematic names of the following compounds: (a) $\ce{CH3CH(CH3)CH2CH(CH2CH3)CH2CH3}$; (b) $\ce{HOCH2CH2CH2CHO}$; (c) $\ce{CH3CH(Cl)CH=CHCH3}$; (d) $\ce{HC#CCH2CH2OH}$; (e) the compound derived from bicyclo[3.2.1]octane by a carbonyl group at C8; (f) $\ce{NC-CH2CH2-COOH}$.

   **Answer** (a) The principal chain is the six-carbon chain that contains the ethyl group: 4-ethyl-2-methylhexane (numbering from the other end gives 3-ethyl-5-methyl, and at the first point of difference 2 < 3, so 2,4 is chosen). (b) The aldehyde has priority: 4-hydroxybutanal. (c) Numbering gives the double bond the lowest locant (2 < 3): 4-chloropent-2-ene (the configuration of the double bond needs a separate $Z$/$E$ descriptor). (d) The alcohol has priority, and the carbon bearing OH is C1: but-3-yn-1-ol. (e) C8 is the one-carbon bridge: bicyclo[3.2.1]octan-8-one. (f) The carboxylic acid has priority and the cyano group is a prefix: 3-cyanopropanoic acid.
6. Explain why the C1–C2 and C2–C3 bond lengths of buta-1,3-diene are about $134$ and $146\,\mathrm{pm}$, alternating in length, while all six C–C bonds of benzene are $139\,\mathrm{pm}$. Use resonance theory to account for the difference.

   **Answer** Benzene has two exactly equivalent Kekulé resonance structures; each C–C bond is single in one and double in the other, so the six bonds of the hybrid are identical, with a length between that of a single and a double bond. Butadiene has only one major resonance structure, $\ce{CH2=CH-CH=CH2}$. The resonance structure that makes C2–C3 a double bond, $\mathrm{\overset{+}{C}H_2{-}CH{=}CH{-}\overset{-}{C}H_2}$ (or its opposite-charge form), has charge separation and terminal carbons without complete octets, so its contribution is very small. The bond lengths therefore still alternate clearly, and C2–C3 is only slightly shorter than an ordinary C–C single bond (part of the shortening comes from sp² hybridization, [6.5.2](/6.5.2#sec-2.5.1)).
