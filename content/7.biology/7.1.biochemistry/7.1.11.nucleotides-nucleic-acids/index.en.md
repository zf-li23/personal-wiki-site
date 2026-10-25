---
title: Nucleotides and Nucleic Acids
description: How the chemical properties of bases and backbone determine the structure and stability of nucleic acids. Nucleotide nomenclature and minor bases; tautomerism, UV absorption, hydrogen-bonding patterns and stacking; why DNA rather than RNA stores genetic information; the evidence that DNA is the genetic material and Chargaff's rules; the B-DNA double helix, A- and Z-DNA, palindromes, hairpins, cruciforms, triplexes and G-quadruplexes; RNA structure; denaturation, melting temperature (Marmur–Doty and nearest-neighbour models) and hybridization; spontaneous damage and DNA methylation; nucleotides as energy carriers, coenzymes and signals.
---

Nucleotides have more roles than any other class of small biomolecule: they are the monomers of DNA and RNA, the energy currency of metabolism (ATP, GTP), parts of coenzymes (NAD, FAD, coenzyme A), and intracellular and extracellular signals (cAMP, cGMP, ATP itself). The chemistry of nucleosides and nucleotides, the N-glycosyl and phosphodiester bonds and the chemical synthesis of oligonucleotides, is in [6.5.33](/6.5.33#sec-33.9); the purine and pyrimidine ring systems are in [6.5.25](/6.5.25). This chapter follows the thread "chemical properties → structure → function" (7.1.1) for nucleic acids: the planar, aromatic bases with fixed patterns of hydrogen-bond donors and acceptors pair in only two ways and stack into a regular helix; the stability of that helix depends on base composition and salt in a way that simple thermodynamic models predict to within a degree; and a single hydroxyl group, the 2′-OH of ribose, decides that RNA is a versatile but labile molecule and DNA a stable archive.

The biological processes that use nucleic acids, the organization of genomes and chromosomes, replication, repair, recombination, transcription, RNA processing and translation, and the laboratory techniques built on them, are the subject of molecular biology ([7.2](/7.2)); this chapter supplies their chemical basis. The synthesis and degradation of nucleotides follow in 7.1.28.

## 11.1. Building Blocks

### 11.1.1. Bases, Nucleosides and Nucleotides

A **nucleotide** has three components: a nitrogenous base (a derivative of **purine** or **pyrimidine**), a pentose, and one or more phosphates; without phosphate it is a **nucleoside** ([6.5.33](/6.5.33#sec-33.9)). The base is attached through an N-β-glycosyl bond from N-9 of purines or N-1 of pyrimidines to C-1′ of the pentose (primes number the sugar atoms), and the phosphate is esterified to C-5′.

**Definition 11.1.1** **Deoxyribonucleic acid** (DNA) is a polymer of 2′-deoxyribonucleotides and **ribonucleic acid** (RNA) a polymer of ribonucleotides, in both cases joined by 3′,5′-phosphodiester bonds. The pentose, not the base, defines the class: a polynucleotide containing 2′-deoxy-D-ribose is DNA even if it contains uracil.

| Base | Nucleoside (ribo / deoxy) | Nucleotide (5′-monophosphate) | Occurs in |
|---|---|---|---|
| adenine (A) | adenosine / deoxyadenosine | adenylate, AMP / dAMP | RNA / DNA |
| guanine (G) | guanosine / deoxyguanosine | guanylate, GMP / dGMP | RNA / DNA |
| cytosine (C) | cytidine / deoxycytidine | cytidylate, CMP / dCMP | RNA / DNA |
| uracil (U) | uridine | uridylate, UMP | RNA |
| thymine (T) | (ribothymidine, rare) / thymidine | thymidylate, dTMP | DNA |

In both nucleic acids the pentose is in the β-furanose form, and its ring is puckered: in B-DNA C-2′ lies out of the plane on the same side as C-5′ (C2′-endo), in RNA and A-form duplexes C-3′ does (C3′-endo); the pucker sets the distance between successive phosphates and so the form of the helix (11.3.2).

Successive nucleotides are joined by **phosphodiester bonds** between the 3′-hydroxyl of one and the 5′-phosphate of the next. All of them point the same way, so a strand has a direction, from the 5′ end (no nucleotide attached at C-5′) to the 3′ end; sequences are always written $5' \to 3'$, left to right. The backbone of alternating sugar and phosphate is hydrophilic; each phosphodiester, with $\mathrm{p}K_{\mathrm{a}} \approx 1$, carries one negative charge at pH 7, neutralized in cells by $\ce{Mg^2+}$ and other cations, polyamines (spermidine, spermine) and the basic residues of proteins such as histones. Short nucleic acids (up to about 50 nucleotides) are called oligonucleotides, longer ones polynucleotides.

### 11.1.2. Minor Bases

Both DNA and RNA contain modified bases, almost always introduced by enzymes after synthesis. In DNA the common ones are methylated: 5-methylcytosine (m⁵C) in plants and animals (11.4.5), N⁶-methyladenine (m⁶A) in bacteria, and 5-hydroxymethylcytosine (hm⁵C), an intermediate of active demethylation in mammalian neurons and stem cells (and a glucosylated base in the DNA of T-even phages, which protects it from host restriction enzymes). RNAs carry more than 150 kinds of modification, most of them in tRNAs and rRNAs: inosine (base hypoxanthine, at the wobble position of some anticodons), pseudouridine (Ψ, uracil attached through C-5 instead of N-1), dihydrouridine, ribothymidine, and 2′-O-methyl ribose. In mRNA, N⁶-methyladenosine is the most abundant internal modification and regulates mRNA stability and translation ([7.2.18](/7.2.18)). Substituents on ring atoms are named by position (5-methylcytosine), those on exocyclic atoms by atom and position (N⁶-methyladenosine, O⁶-methylguanine).

### 11.1.3. Chemical Properties of the Bases

Four properties of the bases explain most of nucleic acid structure.

1. Planarity and aromaticity: The pyrimidines are planar and the purines nearly so. Delocalized π electrons give them strong UV absorption near 260 nm (molar absorption coefficients at pH 7: AMP $15\,400$, GMP $11\,700$, UMP $9\,900$, dTMP $9\,200$, CMP $7\,500\,\mathrm{M^{-1}\,cm^{-1}}$). By the **Lambert–Beer law** ([6.3.17](/6.3.17)), $A_{260} = 1$ corresponds to about $50\,\mathrm{\mu g\,mL^{-1}}$ of double-stranded DNA, $40\,\mathrm{\mu g\,mL^{-1}}$ of RNA and $33\,\mathrm{\mu g\,mL^{-1}}$ of single-stranded DNA; the ratio $A_{260}/A_{280} \approx 1.8$–$2.0$ is the routine check for protein contamination.
2. Tautomers: Each base can exist in several tautomeric forms (**tautomerism**, [6.5.21](/6.5.21)): lactam and lactim for the carbonyl groups (keto and enol forms), amino and imino for the exocyclic amines. At pH 7 the lactam (keto) and amino forms predominate by factors of about $10^4$–$10^5$, and only these give the Watson–Crick pairs. A rare tautomer can mispair: enol-G or imino-C pair as G·T and A·C with near-Watson–Crick geometry, one source of replication errors, which polymerase geometry selection and proofreading reduce ([7.2.7](/7.2.7)).
3. Hydrogen-bonding patterns: Ring nitrogens, carbonyl oxygens and exocyclic amino groups are donors and acceptors arranged in a fixed pattern on each edge of a base. On the Watson–Crick edge adenine presents acceptor–donor (N1, N6-H), thymine donor–acceptor (N3-H, O4); guanine acceptor–donor–donor (O6, N1-H, N2-H), cytosine donor–acceptor–acceptor (N4-H, N3, O2). Only A with T (or U) and G with C complement each other (Figure in 11.3.1).
4. Stacking: At neutral pH the bases are hydrophobic and poorly soluble. In water they stack with their ring planes parallel and $0.34\,\mathrm{nm}$ apart, which buries their faces from water (the **hydrophobic effect**, 7.1.2) and adds **van der Waals forces** and dipole–dipole interactions. Stacking, not hydrogen bonding, provides most of the free energy that holds a duplex together (11.3.1).

### 11.1.4. One Hydroxyl Group Decides the Archive

RNA is hydrolysed rapidly in alkali, DNA is not. The 2′-hydroxyl of ribose, deprotonated, attacks the adjacent phosphorus in an intramolecular displacement and cleaves the phosphodiester, giving a 2′,3′-cyclic phosphate that is then hydrolysed to a mixture of 2′- and 3′-monophosphates. The same chemistry is used by RNase A and by self-cleaving ribozymes. DNA lacks the internal nucleophile, and the half-life of a phosphodiester bond in DNA at pH 7 and 25 °C is estimated at more than 10 million years (for RNA it is of the order of years, and much shorter with metal ions). Three more chemical facts make DNA the better store of information: the deoxyribose N-glycosyl bond is the main weak point of DNA (depurination, 11.4.4) but damage to it can be repaired from the complementary strand; DNA is double-stranded, so the information exists twice; and DNA uses thymine rather than uracil, so that the commonest spontaneous lesion, the deamination of cytosine to uracil, is recognizable as damage (11.4.4). The **RNA world hypothesis** ([7.2.23](/7.2.23)) interprets these differences historically: RNA, able both to carry information and to catalyse reactions, probably came first, and DNA was later adopted as a more durable archive.

## 11.2. DNA Is the Genetic Material

### 11.2.1. The Experiments

Friedrich Miescher isolated a phosphorus-rich acidic substance, "nuclein", from the nuclei of leukocytes in pus in 1869. For seventy years nucleic acids were thought too simple to carry genetic information (the "tetranucleotide hypothesis" held them to be monotonous repeats of the four nucleotides), and proteins were the favoured candidates.

| Year | Experiment | Result |
|---|---|---|
| 1928 | Frederick Griffith: heat-killed virulent (smooth, capsulated) *Streptococcus pneumoniae* mixed with live nonvirulent (rough) cells kills mice, and live virulent bacteria are recovered | a heritable "transforming principle" passes from dead to live cells (**transformation**) |
| 1944 | Oswald Avery, Colin MacLeod and Maclyn McCarty: the purified transforming principle has the composition and properties of DNA; it is destroyed by deoxyribonuclease but not by proteases or ribonuclease | the transforming principle is DNA |
| 1952 | Alfred Hershey and Martha Chase: in phage T2, $^{32}\mathrm{P}$-labelled DNA enters infected *Escherichia coli*, while $^{35}\mathrm{S}$-labelled coat protein stays outside and can be sheared off without preventing phage production | the genetic material of the phage is its DNA |

### 11.2.2. Chargaff's Rules

**Definition 11.2.1** **Chargaff's rules** (Erwin Chargaff, late 1940s) state that (1) the base composition of DNA varies between species, (2) DNA from different tissues of one species has the same composition, which does not change with age, nutrition or environment, and (3) in every cellular DNA the number of adenine residues equals that of thymine and the number of guanine residues that of cytosine: $\mathrm{A} = \mathrm{T}$, $\mathrm{G} = \mathrm{C}$, and hence $\mathrm{A} + \mathrm{G} = \mathrm{T} + \mathrm{C}$.

The third rule holds for double-stranded DNA only; the single-stranded DNA of phage φX174 (A 24.6 %, T 32.7 %, G 24.1 %, C 18.5 %) does not obey it. The base composition is usually summarized by the G + C content, from about 20 % (*Plasmodium falciparum*) to about 75 % (some *Streptomyces*); human DNA has 41 %.

**Example 11.2.1** In DNA from two bacteria, X and Y, adenine makes up 32 % and 17 % of the bases. Assuming double-stranded DNA, X has 32 % T, hence 36 % G + C (18 % G, 18 % C); Y has 17 % T and 66 % G + C (33 % G, 33 % C). If one of them was isolated from a hot spring at 64 °C, it is more likely Y: G·C-rich DNA melts at a higher temperature (11.4.2), although thermophily depends more on proteins, salts and supercoiling than on base composition.

### 11.2.3. From Diffraction to the Double Helix

Rosalind Franklin and Maurice Wilkins obtained X-ray diffraction patterns of DNA fibers (**X-ray diffraction**, [6.4.8](/6.4.8)). Franklin and Raymond Gosling's pattern of the hydrated B form (Photo 51, 1952) showed a cross of layer lines, the signature of a helix, with a strong reflection at $0.34\,\mathrm{nm}$ (the spacing of stacked bases) and a repeat of $3.4\,\mathrm{nm}$ along the axis; the absence of the fourth layer line indicated two strands offset along the axis, and the density suggested two chains per molecule. James Watson and Francis Crick combined these data, Chargaff's rules, and the correct (keto) tautomers of the bases into their model of 1953 (Nature 171:737), published with papers by Wilkins and by Franklin and Gosling in the same issue. The model immediately suggested how DNA could be copied: separate the strands, and use each as a template for a complementary one (semiconservative **replication**, confirmed by Meselson and Stahl in 1958, [7.2.7](/7.2.7)). The derivation of the helix parameters from the fiber diagram belongs to biophysics ([7.6](/7.6)).

## 11.3. Nucleic Acid Structure

### 11.3.1. The B-DNA Double Helix

**Definition 11.3.1** A **base pair** is the hydrogen-bonded pairing of two bases on opposite strands; in a Watson–Crick base pair A pairs with T (or U) through two hydrogen bonds and G with C through three. The **double helix** (B-DNA, the Watson–Crick structure) consists of two antiparallel, complementary polynucleotide strands wound around a common axis into a right-handed helix, with the sugar–phosphate backbones outside and the base pairs stacked inside, nearly perpendicular to the axis.

![The Watson–Crick base pairs. A: adenine pairs with thymine through two hydrogen bonds (dashed; N6–H of A to O4 of T, and N3–H of T to N1 of A). B: guanine pairs with cytosine through three (O6 of G to N4–H of C, N1–H of G to N3 of C, N2–H of G to O2 of C). dR marks C-1′ of deoxyribose. The two glycosyl bonds of a pair lie on the same side, so the edge of the pair facing up lines the major groove of the helix and the opposite edge the minor groove; the distance between the C-1′ atoms is almost the same (about 1.05 nm) for A·T and G·C, so either pair fits the regular helix in either orientation.](./plots/base-pairs.py)

The geometry of the base pairs explains the helix. Because the C-1′ atoms of A·T, T·A, G·C and C·G pairs are equally far apart and their glycosyl bonds make the same angles, any sequence fits one regular backbone, and the information is in the sequence, not the shape. Because both glycosyl bonds of a pair lie on one side, the two backbones are closer together on that side, and the helix has two unequal grooves.

**Definition 11.3.2** The two helical grooves between the backbones of a DNA duplex are the **major groove**, wide and deep in B-DNA (about 1.2 nm wide), into which the edges of the bases carrying N7 of the purines and the C5 and C4 substituents of the pyrimidines face, and the **minor groove**, narrow (about 0.6 nm), lined by N3 of the purines and the C2 substituents of the pyrimidines.

| Parameter | B-DNA |
|---|---|
| diameter | ≈ 2.0 nm |
| rise per base pair | 0.34 nm |
| base pairs per turn | 10.5 in solution (10 in fibers) |
| pitch | ≈ 3.6 nm |
| sugar pucker | C2′-endo |
| glycosyl bond | anti |
| strand orientation | antiparallel |

The grooves are where proteins read the sequence without opening the helix. In the major groove each of the four base pairs presents a distinct pattern of hydrogen-bond acceptors, donors and (for T) a methyl group, so a protein side chain in the major groove can tell A·T from T·A from G·C from C·G; in the minor groove A·T and T·A look almost alike. Sequence-specific DNA-binding proteins (repressors, transcription factors, restriction enzymes) therefore insert α helices or β strands mainly into the major groove; minor-groove binders such as the TATA-binding protein and the antibiotic distamycin recognize the shape and narrowness of A·T-rich minor grooves instead.

The stability of the duplex comes mainly from base stacking and from shielding of the phosphate charges by cations, not from the hydrogen bonds between paired bases: in single strands the bases form equally good hydrogen bonds with water, so pairing gains little hydrogen-bond free energy, whereas stacking of successive base pairs buries their surfaces. Stacking between successive G·C pairs is stronger than between A·T pairs, which is the main reason why G·C-rich DNA is more stable (11.4.2); the third hydrogen bond of G·C contributes less. The hydrogen bonds provide specificity: a mispair costs a hydrogen bond and distorts the stack.

### 11.3.2. A, B and Z Forms

Rotation about the bonds of the backbone, the pucker of the sugar, and rotation about the glycosyl bond (purines can be anti or syn; pyrimidines are almost always anti, because their C-2 carbonyl clashes with the sugar in syn) allow other helices.

**Definition 11.3.3** **B-DNA** is the Watson–Crick form, the most stable form of random-sequence DNA at physiological hydration. **A-DNA** is a wider right-handed duplex with about 11 bp per turn and base pairs tilted about 20° and displaced from the axis, formed by DNA at low water activity and by all RNA duplexes and RNA–DNA hybrids. **Z-DNA** is a left-handed duplex with 12 bp per turn and a zigzag backbone, formed most readily by alternating purine–pyrimidine sequences such as $(\mathrm{CG})_n$, with the purines syn and the pyrimidines anti.

| | A form | B form | Z form |
|---|---|---|---|
| helical sense | right-handed | right-handed | left-handed |
| diameter | ≈ 2.6 nm | ≈ 2.0 nm | ≈ 1.8 nm |
| base pairs per turn | 11 | 10.5 | 12 (6 dinucleotide repeats) |
| rise per base pair | 0.26 nm | 0.34 nm | 0.37 nm |
| base-pair tilt from normal to axis | 20° | 6° | 7° |
| sugar pucker | C3′-endo | C2′-endo | C2′-endo (pyrimidines), C3′-endo (purines) |
| glycosyl bond | anti | anti | anti (pyrimidines), syn (purines) |
| major groove | deep and narrow | wide and deep | almost flat |
| minor groove | wide and shallow | narrow and deep | narrow and deep |
| where | dehydrated DNA, crystals; RNA duplexes; RNA–DNA hybrids | cellular DNA | $(\mathrm{CG})_n$, $(\mathrm{CA})_n$, m⁵C-rich tracts under negative supercoiling |

![A-, B- and Z-DNA drawn from their helix parameters, 24 base pairs each and to the same scale; darker backbone segments are in front. The A form is short and wide with tilted base pairs, the B form is the familiar right-handed helix with a wide major and a narrow minor groove, and the Z form is a slender left-handed helix.](./plots/dna-forms.py)

The forms differ in water content as much as in sequence: removing water favours A, high salt or negative supercoiling (**supercoiled** DNA, [7.2.3](/7.2.3)) favours Z, because the B→Z transition relieves underwinding. Short Z tracts form transiently behind transcribing RNA polymerase; proteins with Zα domains, such as the RNA editing enzyme ADAR1 and the innate-immunity sensor ZBP1, bind Z-DNA and Z-RNA specifically, and their functions in sensing viral and endogenous nucleic acids are an active field of research.

### 11.3.3. Sequence-Dependent Structures

Local sequence can alter the helix or allow other pairings.

- Bends: runs of four or more A residues on one strand (A-tracts) bend the helix, about 18° for six A's; phased A-tracts every 10 bp add up to large curvature, which helps some proteins bind and wrap DNA.
- Palindromes and mirror repeats: a palindrome is an inverted repeat in which the sequence on one strand read $5' \to 3'$ equals that on the other strand read $5' \to 3'$ (twofold symmetry, such as GAATTC, the EcoRI site); a mirror repeat is symmetric within each strand and is not self-complementary.
- Hairpins and cruciforms: a self-complementary sequence in one strand can fold back on itself into a hairpin (a stem and a loop); in duplex DNA, both strands of a palindrome can do so at once to form a cruciform. Cruciforms are unstable in relaxed DNA and are extruded only in negatively supercoiled DNA; RNA hairpins are the commonest RNA structure (11.3.4).
- Triplexes: the purines of a Watson–Crick pair can form additional hydrogen bonds with a third strand through their major-groove (Hoogsteen) positions N7, O6 and N6, giving T·A–T and C⁺·G–C triplets; the C⁺ requires protonation (its $\mathrm{p}K_{\mathrm{a}}$ is raised from 4.2 to above 7.5 in the triplex), so these triplexes form best at low pH in long homopurine–homopyrimidine tracts (H-DNA).
- G-quadruplexes: four guanines form a planar, Hoogsteen-bonded G-quartet around a central $\ce{K+}$ or $\ce{Na+}$ ion, and stacked quartets form a very stable four-stranded structure from G-rich sequences, within one strand or between strands, in several orientations. G-quadruplexes form at the single-stranded G-rich overhang of telomeres and in many promoters (such as that of *MYC*); they have been visualized in human cells with specific antibodies and are targets of experimental anticancer drugs.

**Definition 11.3.4** A **palindrome** in nucleic acids is a region of inverted repeat in which each strand, read $5' \to 3'$, has the same sequence. A **hairpin** is an intrastrand double helix formed by a self-complementary sequence, closed by a loop; a **cruciform** is a pair of hairpins extruded from both strands of a duplex palindrome. **Hoogsteen pairing** is base pairing through the N7 edge of a purine, and **G-quadruplexes** (G tetraplexes) are four-stranded structures built from stacked, Hoogsteen-paired G-quartets.

Many protein-binding sites in DNA, including the recognition sites of type II restriction enzymes and the operators bound by dimeric repressors, are palindromes, matching the twofold symmetry of the dimeric proteins ([7.2.5](/7.2.5)). The predictability of Watson–Crick pairing also makes DNA a construction material: in DNA origami (Rothemund, 2006) a long single strand is folded into a designed two- or three-dimensional shape by hundreds of short "staple" oligonucleotides.

### 11.3.4. RNA Structure

Transcription produces single-stranded RNA. Messenger RNA carries the coding information of one gene (monocistronic, the rule in eukaryotes) or several (polycistronic, common in bacteria and archaea), together with noncoding sequences that start and stop translation and regulate it; transfer RNAs (about 15 % of cellular RNA by mass) are the adaptors of translation; ribosomal RNAs (about 80 %) form the core of the ribosome; and a large variety of other **noncoding RNAs** have catalytic and regulatory roles ([7.2.2](/7.2.2), [7.2.18](/7.2.18)).

A single RNA strand tends to form a right-handed helix of stacked bases, purine–purine stacking being strongest. Any complementary segments pair into antiparallel A-form helices; perfect pairing over long stretches is rare, so RNAs consist of short helices interrupted by bulges, internal loops and hairpin loops, and the hairpin is the most common RNA secondary structure. Three features distinguish RNA pairing from DNA:

- The G·U wobble pair (two hydrogen bonds, shifted geometry) is common in RNA helices and is the basis of wobble pairing between codons and anticodons ([7.2.19](/7.2.19)).
- Certain loop sequences, such as the UUCG tetraloop, are exceptionally stable and nucleate folding.
- The 2′-OH forms hydrogen bonds with bases, phosphates and other riboses, and together with non-Watson–Crick pairs, base triples and coordinated $\ce{Mg^2+}$ it allows compact tertiary structures, such as the L-shaped yeast tRNA^Phe (the first RNA structure solved, 1974), the hammerhead ribozyme of plant viroids and satellite RNAs, and the self-splicing group I intron of *Tetrahymena thermophila*, the first RNA enzyme discovered (Cech, 1982).

RNA duplexes are more stable than DNA duplexes of the same sequence (denaturation needs about 20 °C more), and RNA–DNA hybrids are intermediate; tighter A-form stacking and the hydration network of the 2′-OH groups are thought to contribute, but the physical basis is not fully understood. Because base pairing dominates RNA folding, the secondary structure of an RNA can be predicted by minimizing a free energy built from nearest-neighbour stacking terms like those of 11.4.2 (dynamic programming, as in the programs Mfold and RNAfold; [7.8](/7.8)).

## 11.4. Nucleic Acid Chemistry

### 11.4.1. Denaturation and Renaturation

A solution of native DNA is very viscous. On heating above about 80 °C, or at extremes of pH, the viscosity falls sharply: base stacking and hydrogen bonds are disrupted and the strands unwind and separate, partially or completely, without breaking any covalent bond (**denaturation**, also called melting). Stacked bases absorb less UV light than free ones (the **hypochromic effect**); denaturation therefore raises $A_{260}$ by about 40 % (the **hyperchromic effect**, [6.4.9](/6.4.9)), which is the usual way of following it.

**Definition 11.4.1** The **melting temperature** $T_{\mathrm{m}}$ of a nucleic acid duplex is the temperature at which half of it is denatured (half of the base pairs broken, or for short duplexes half of the strands separated).

When the temperature or pH is returned to normal, separated strands find each other and reanneal (**renaturation**). This happens in two steps: a slow, second-order nucleation, in which complementary sequences meet by random collision and form a short stretch of duplex, and a fast, first-order zippering of the rest. Because nucleation is second order, the half-time of renaturation is inversely proportional to the concentration of each sequence and hence proportional to genome complexity, which is the basis of the classical $C_0t$ analysis of repetitive DNA ([7.2.2](/7.2.2)).

### 11.4.2. What Sets the Melting Temperature

For long DNA under fixed conditions, $T_{\mathrm{m}}$ rises linearly with G + C content, because G·C pairs stack more strongly (11.3.1), and it rises with the logarithm of the cation concentration, because cations screen the repulsion between the phosphates of the two strands, which is larger in the compact duplex than in the separated coils. The transition is sharp, a few degrees wide, because the base pairs open cooperatively in segments of hundreds of base pairs (the **helix–coil transition**). A-T-rich regions melt first and can be seen in electron micrographs as single-stranded bubbles; origins of replication and promoters are A-T-rich for the same reason.

**Formula 11.4.1 (Melting temperature of long DNA)** In standard saline citrate (0.15 M NaCl, 0.015 M sodium citrate, $[\ce{Na+}] = 0.195\,\mathrm{M}$), Marmur and Doty (1962) found
$$
T_{\mathrm{m}}/{}^\circ\mathrm{C} = 69.3 + 0.41\,(\%\mathrm{GC}). \tag{11.1}
$$
At other $\ce{Na+}$ concentrations up to about $0.2\,\mathrm{M}$ (Schildkraut and Lifson, 1965),
$$
T_{\mathrm{m}}/{}^\circ\mathrm{C} = 81.5 + 16.6\lg\!\left([\ce{Na+}]/\mathrm{M}\right) + 0.41\,(\%\mathrm{GC}), \tag{11.2}
$$
which reduces to Eq. (11.1) at $0.195\,\mathrm{M}$. Corrections for formamide, probe length and mismatches, used in designing hybridization experiments, are given in [7.2.5](/7.2.5#sec-5.5.3).

These empirical rules describe long DNA. For oligonucleotides such as PCR primers and hybridization probes, length and sequence matter, and $T_{\mathrm{m}}$ depends on the strand concentration, because duplex formation is bimolecular. The nearest-neighbour model treats the duplex as a sum of stacked doublets.

**Formula 11.4.2 (Nearest-neighbour model)** For a duplex of two different, complementary strands, mixed at equal concentrations to a total strand concentration $C_{\mathrm{T}}$, model hybridization as the **two-state model** $\mathrm{A} + \mathrm{B} \rightleftharpoons \mathrm{AB}$ with
$$
\Delta H^\circ = \Delta H^\circ_{\mathrm{init}} + \sum_{\text{doublets}} \Delta H^\circ_{\mathrm{nn}},\qquad
\Delta S^\circ = \Delta S^\circ_{\mathrm{init}} + \sum_{\text{doublets}} \Delta S^\circ_{\mathrm{nn}},
$$
where each of the ten distinct stacked doublets (AA/TT, AT/TA, …, GC/CG) has tabulated values (SantaLucia's unified parameters, 1998, for $1\,\mathrm{M}$ NaCl). At $T_{\mathrm{m}}$ half of the strands are paired, $[\mathrm{AB}] = [\mathrm{A}] = [\mathrm{B}] = C_{\mathrm{T}}/4$, so $K = 4/C_{\mathrm{T}}$ (with $c^\circ = 1\,\mathrm{M}$), and $\Delta G^\circ = \Delta H^\circ - T\Delta S^\circ = -RT\ln K$ gives
$$
T_{\mathrm{m}} = \frac{\Delta H^\circ}{\Delta S^\circ + R\ln(C_{\mathrm{T}}/4)}. \tag{11.3}
$$
For a self-complementary strand, $C_{\mathrm{T}}/4$ is replaced by $C_{\mathrm{T}}$. Lower salt is accounted for by $\Delta S^\circ([\ce{Na+}]) = \Delta S^\circ(1\,\mathrm{M}) + 0.368\,(N-1)\ln([\ce{Na+}]/\mathrm{M})\ \mathrm{cal\,mol^{-1}\,K^{-1}}$ for $N$ base pairs.

**Example 11.4.1** For the 20-mer TAATACGACTCACTATAGGG (the T7 promoter primer) paired with its complement, the unified parameters give $\Delta H^\circ = -623\,\mathrm{kJ\,mol^{-1}}$ and $\Delta S^\circ = -1.72\,\mathrm{kJ\,mol^{-1}\,K^{-1}}$ in $1\,\mathrm{M}$ NaCl, so $\Delta G^\circ(37\,^\circ\mathrm{C}) = -89\,\mathrm{kJ\,mol^{-1}}$. At $C_{\mathrm{T}} = 0.5\,\mathrm{\mu M}$, $R\ln(C_{\mathrm{T}}/4) = 8.314 \times \ln(1.25 \times 10^{-7}) = -132\,\mathrm{J\,mol^{-1}\,K^{-1}}$, and Eq. (11.3) gives $T_{\mathrm{m}} = 622\,600/(1720 + 132)\,\mathrm{K} = 336\,\mathrm{K} = 63\,^\circ\mathrm{C}$; in $50\,\mathrm{mM}$ $\ce{Na+}$ it falls to $48\,^\circ\mathrm{C}$. The large enthalpy and entropy nearly cancel: $T_{\mathrm{m}}$ is high because $\Delta H^\circ$ is large, and the transition is sharp for the same reason (van 't Hoff, as for protein unfolding in 7.1.6).

![DNA melting. A: melting curves of long DNAs with 30 %, 50 % and 70 % G + C in 0.195 M Na⁺, drawn as cooperative two-state transitions around the midpoints of Eq. (11.1); the absorbance at 260 nm rises by about 40 % (hyperchromic effect). B: melting temperature against G + C content at three Na⁺ concentrations (Eq. (11.2)): each 1 % G + C adds 0.41 °C, and a tenfold lower salt concentration lowers T_m by 16.6 °C. C: nearest-neighbour T_m of the 20-mer of Example 11.4.1 against total strand concentration, in 1 M and 50 mM Na⁺ (Eq. (11.3)); points mark 0.5 µM, a typical primer concentration.](./plots/dna-melting.py)

### 11.4.3. Hybridization

**Definition 11.4.2** The formation of a duplex between complementary single strands of different origin (two DNAs, or DNA and RNA) is called **hybridization**; the extent and stability of hybrid duplexes reflect the similarity of the sequences.

Hybridization between the denatured DNAs of two species measures their overall sequence similarity: human and mouse DNA hybridize extensively, human and yeast DNA hardly at all. Each 1 % of mismatched base pairs lowers $T_{\mathrm{m}}$ by about 1–1.5 °C, so the temperature and salt of hybridization and washing (the **stringency**, [7.2.5](/7.2.5)) decide whether only perfect matches or also related sequences are detected. A labelled probe of known sequence can thus find one gene among millions of fragments, the principle of the **Southern blot** (DNA), Northern blot (RNA), in situ hybridization, microarrays, and the primers of **PCR** and sequencing ([7.2.6](/7.2.6)).

### 11.4.4. Nonenzymatic Damage

Nucleotides undergo slow spontaneous reactions. Each is rare, but a human diploid genome has $6 \times 10^9$ bases, so tens of thousands of lesions arise in every cell every day, and DNA, uniquely among macromolecules, is repaired rather than replaced ([7.2.8](/7.2.8)).

| Reaction | Lesion | Approximate frequency (mammalian cell, per day) | Consequence if not repaired |
|---|---|---|---|
| hydrolysis of the N-glycosyl bond (depurination; depyrimidination about 20 times slower) | abasic (AP) site; the sugar opens to the aldehyde and the strand can break | about $10^4$ (one purine in $10^5$) | blocks replication; polymerases often insert A opposite it |
| hydrolytic deamination of cytosine | uracil in DNA | about 100–500 (one C in $10^7$) | G·C → A·T transition |
| deamination of 5-methylcytosine | thymine (a T·G mismatch) | tens | G·C → A·T at CpG, the commonest point mutation in human disease |
| deamination of adenine and guanine | hypoxanthine, xanthine | about 1/100 of C deamination | A·T → G·C |
| oxidation by reactive oxygen species (mainly hydroxyl radicals) | 8-oxoguanine, thymine glycol, strand breaks | about $10^3$ or more | 8-oxoG pairs with A: G·C → T·A |
| UV (200–400 nm) | cyclobutane pyrimidine dimers (mostly T–T), 6-4 photoproducts | thousands per hour in sun-exposed skin | kink in the helix; C → T at dipyrimidines |
| alkylation (dimethyl sulfate, nitrosamines; endogenous S-adenosylmethionine) | O⁶-methylguanine, N7-methylguanine, 3-methyladenine | | O⁶-meG pairs with T: G·C → A·T |
| nitrous acid ($\ce{HNO2}$, from nitrites and nitrosamines), bisulfite | accelerated deamination of A, C, G | | transitions |
| ionizing radiation | base fragmentation, single- and double-strand breaks | | chromosome breaks and rearrangements |

**Definition 11.4.3** The spontaneous hydrolytic loss of the exocyclic amino group of a base is **deamination**; the hydrolysis of the N-glycosyl bond that releases a purine is **depurination**; the cyclobutane ring formed by UV light between the C-5 and C-6 atoms of two adjacent pyrimidines in one strand is a **pyrimidine dimer**.

Depurination, contrary to an older view, is physiologically important: with about $10^4$ events per cell per day it is the most frequent spontaneous lesion; only in RNA, whose ribose N-glycosyl bond is much more stable, is it insignificant. Cytosine deamination, though rarer, explains the choice of thymine. The uracil it produces is recognized as foreign and excised by uracil–DNA glycosylase; if uracil were a normal base of DNA, a uracil opposite G (from deaminated C) could not be told from a legitimate one opposite A, and deamination would slowly convert G·C pairs into A·T pairs. The exception proves the rule: 5-methylcytosine deaminates to thymine, a normal base, which is repaired less efficiently, and CpG sites mutate about ten times faster than other sites, which has depleted CpG in vertebrate genomes to about a quarter of its expected frequency.

### 11.4.5. DNA Methylation

**Definition 11.4.4** **DNA methylation** is the enzymatic transfer of a methyl group from S-adenosylmethionine (SAM) to a base of DNA, mainly to C-5 of cytosine (5-methylcytosine) or to N⁶ of adenine (N⁶-methyladenine).

Methylation adds no information to the sequence but marks it, and the mark can be read by proteins without opening the helix: the methyl group of m⁵C lies in the major groove, where thymine has its own methyl group.

- Bacteria: restriction–modification systems mark the cell's own DNA at the recognition sites of its restriction enzymes, so that unmethylated phage DNA is cut (**restriction–modification system**, [7.2.5](/7.2.5)). In *E. coli*, Dam methylase methylates A in GATC; for a few minutes after replication only the parental strand is methylated, which tells the mismatch-repair system which strand to correct ([7.2.8](/7.2.8)) and also times the initiation of replication.
- Animals: in mammals about 4–5 % of cytosines, 70–80 % of all CpG dinucleotides, are methylated, symmetrically on both strands. Maintenance methylase (DNMT1) copies the pattern onto the new strand after replication, so the pattern is inherited through cell divisions. Methylation of CpG islands in promoters silences genes; it suppresses transposable elements, inactivates one X chromosome in females and underlies genomic imprinting ([7.2.15](/7.2.15)). Abnormal methylation is common in cancer.
- Plants: cytosines are methylated in CG, CHG and CHH contexts (H = A, C or T), and methylation states can be inherited for many generations as epialleles. In *Arabidopsis thaliana*, hypermethylated, silenced alleles of the floral regulator gene *SUPERMAN* (the *clark kent* epialleles) give flowers with extra stamens and carpels, like *superman* loss-of-function mutants, although the DNA sequence is unchanged.

### 11.4.6. Synthesis, Amplification and Sequencing

Three technologies built on nucleic acid chemistry transformed biology; their chemistry or principle is summarized here and their use in [7.2.5](/7.2.5) and [7.2.6](/7.2.6).

- Chemical synthesis: oligonucleotides are built on a solid support from the 3′ end, adding protected nucleoside phosphoramidites in a four-step cycle (detritylation, coupling, capping, oxidation) with coupling yields above 99 % (**phosphoramidite method**, [6.5.33](/6.5.33#sec-33.9)). Routine oligonucleotides of 20–100 nucleotides cost a few cents to tens of cents (US) per base; chemically synthesized genes and genomes are assembled from such pieces.
- Amplification: in the **polymerase chain reaction**, cycles of denaturation, annealing of two **primers** and extension by a heat-stable DNA polymerase double the target every cycle ($2^{30} \approx 10^9$-fold in 30 cycles). Its specificity is that of hybridization, so primer $T_{\mathrm{m}}$ (Eq. (11.3)) sets the annealing temperature.
- Sequencing: **Sanger sequencing** (1977) terminates DNA synthesis with 2′,3′-dideoxynucleotides, which lack the 3′-OH needed for the next phosphodiester bond; massively parallel short-read sequencing with reversible terminators and long-read single-molecule methods followed. The first human genome (completed 2003) cost about US\$3 billion; a human genome now costs a few hundred dollars, below the "US\$1000 genome" that was a goal in the early 2010s.

## 11.5. Other Functions of Nucleotides

Most of the nucleotides of a cell are not in nucleic acids at all.

- Energy carriers: the 5′-phosphate of a ribonucleotide can carry one or two more phosphates (labelled α, β, γ from the ribose). The α-phosphate is joined by an ester bond, whose hydrolysis yields about $14\,\mathrm{kJ\,mol^{-1}}$ under standard conditions, the β and γ phosphates by phosphoanhydride bonds, each yielding about $30\,\mathrm{kJ\,mol^{-1}}$; why anhydrides release more is the subject of 7.1.16. ATP is the general currency; GTP drives protein synthesis and signalling by G proteins; UTP activates sugars (UDP-glucose, 7.1.19) and CTP activates lipid head groups (CDP-diacylglycerol, 7.1.26). Nucleoside triphosphates are also the activated precursors of RNA and DNA synthesis, which releases pyrophosphate.
- Adenine nucleotides in coenzymes: coenzyme A, NAD and NADP, FAD, and coenzyme B₁₂ (5′-deoxyadenosylcobalamin) all contain adenosine, as does S-adenosylmethionine. In none of them does the adenosine take part in the chemistry; it is a binding handle, and removing it lowers activity by orders of magnitude (the 3′-phosphoadenosine diphosphate part of acetoacetyl-CoA increases its reactivity with β-ketoacyl-CoA transferase $10^6$-fold), a use of binding energy (7.1.8). Evolutionary economy probably explains the choice: once ATP was abundant, its nucleotide-binding domains (the Rossmann fold) could be reused for many coenzymes (**coenzyme**, 7.1.3).
- Regulatory nucleotides: adenosine 3′,5′-cyclic monophosphate (cAMP), made from ATP by adenylyl cyclase, is a second messenger in nearly all cells outside the plant kingdom, and cGMP has similar roles (7.1.14); bacteria make guanosine tetraphosphate (ppGpp) during amino acid starvation, which reprograms transcription away from rRNA and tRNA synthesis (the stringent response, [7.2.11](/7.2.11)), and cyclic di-GMP, which controls the switch between swimming and biofilm growth. In animal cells, cyclic GMP–AMP (cGAMP), made by the sensor cGAS when it detects DNA in the cytosol, activates the innate immune adaptor STING.
- Extracellular signals: neurons and damaged cells release ATP, which opens P2X ion channels and activates P2Y G protein–coupled receptors, signals in taste, pain, inflammation and smooth-muscle contraction. ADP activates the P2Y12 receptor of platelets; the antiplatelet drug clopidogrel blocks it.

## Summary

| Structural feature | Chemical property | Biological consequence |
|---|---|---|
| planar aromatic bases | absorb at 260 nm; stack $0.34\,\mathrm{nm}$ apart | quantitation by $A_{260}$; stacking is the main source of duplex stability (11.3.1) |
| keto and amino tautomers predominate | fixed donor–acceptor pattern; rare tautomers mispair | only A·T and G·C pair (Definition 11.3.1); one origin of replication errors |
| equal C-1′–C-1′ distance of all four pairs, glycosyl bonds on one side | sequence-independent backbone; two unequal grooves | information in the sequence; proteins read the major groove (Definition 11.3.2) |
| 2′-OH in RNA | intramolecular attack on the phosphodiester | RNA labile and catalytic; DNA stable (11.1.4) |
| thymine instead of uracil | C → U deamination recognizable | DNA can be repaired faithfully (11.4.4) |
| antiparallel complementary strands (Chargaff's rules, Definition 11.2.1) | each strand specifies the other | semiconservative replication; hybridization (Definition 11.4.2) |
| sugar pucker, syn/anti glycosyl bond | A, B, Z helices (Definition 11.3.3) | RNA duplexes are A-form; Z-DNA under negative supercoiling |
| self-complementary and G-rich sequences | hairpins, cruciforms, triplexes, G-quadruplexes (Definition 11.3.4) | protein-binding sites; telomeres; RNA secondary structure |
| G·C content, cation concentration, length | $T_{\mathrm{m}} = 81.5 + 16.6\lg[\ce{Na+}] + 0.41(\%\mathrm{GC})$ (Formula 11.4.1); nearest-neighbour $T_{\mathrm{m}} = \Delta H^\circ/[\Delta S^\circ + R\ln(C_{\mathrm{T}}/4)]$ (Formula 11.4.2) | design of primers and probes; A-T-rich origins and promoters |
| major-groove methyl of m⁵C (Definition 11.4.4) | read without unpairing | restriction–modification, strand discrimination, gene silencing and epigenetic inheritance |
| adenosine handle, phosphoanhydrides | binding energy; about $30\,\mathrm{kJ\,mol^{-1}}$ per anhydride | coenzymes, energy currency, signals (11.5) |

| Quantity | Value |
|---|---|
| B-DNA | 2.0 nm wide; 10.5 bp per turn; 0.34 nm per bp; pitch 3.6 nm |
| A-DNA / Z-DNA | 11 bp, 0.26 nm per bp, right-handed / 12 bp, 0.37 nm per bp, left-handed |
| $A_{260} = 1$ | ≈ 50 µg/mL dsDNA, 40 µg/mL RNA, 33 µg/mL ssDNA |
| hyperchromicity on melting | ≈ 40 % |
| $T_{\mathrm{m}}$ | +0.41 °C per 1 % G + C; +16.6 °C per tenfold $[\ce{Na+}]$; RNA duplexes ≈ 20 °C more stable than DNA |
| spontaneous lesions per cell per day | depurination ≈ $10^4$; C deamination ≈ 100–500; oxidative ≈ $10^3$ or more |
| CpG methylation in mammals | 70–80 % of CpG; 4–5 % of all C |

## Questions

1. One strand of a duplex DNA has the sequence 5′-GCGCAATATTTCTCAAAATATTGCGC-3′. Write the complementary strand, identify the special feature of the sequence, and state what alternative structure the double-stranded molecule could form.

   **Answer** The complementary strand, written $5' \to 3'$, is 5′-GCGCAATATTTTGAGAAATATTGCGC-3′. The sequence contains inverted repeats: GCGCAATATT at the 5′ end and its reverse complement AATATTGCGC at the 3′ end (the central TCTCAA/TTGAGA segment is not self-complementary). Each strand can therefore fold back into a hairpin with a stem of 10 bp (GCGCAATATT paired with AATATTGCGC) and a loop formed by the central six nucleotides, and the duplex can extrude a cruciform, which requires negative supercoiling to compensate for the loss of the base pairs in the loops.
2. Explain why the absorbance at 260 nm of a DNA solution rises on heating, and why the rise for a 70 % G + C DNA occurs at a higher temperature than for a 30 % G + C DNA in the same buffer. Predict both melting temperatures in 0.05 M Na⁺.

   **Answer** In the duplex the bases are stacked, and the electronic coupling between stacked chromophores lowers their absorption (hypochromism); when the strands separate and the bases unstack, absorbance rises by about 40 %. G·C pairs stack more strongly than A·T pairs (and have one more hydrogen bond), so more heat is needed to disrupt a G·C-rich duplex. From Eq. (11.2), $81.5 + 16.6\lg 0.05 = 81.5 - 21.6 = 59.9$; adding $0.41 \times 30 = 12.3$ and $0.41 \times 70 = 28.7$ gives $T_{\mathrm{m}} \approx 72\,^\circ\mathrm{C}$ and $89\,^\circ\mathrm{C}$.
3. A PCR primer pair is designed with nearest-neighbour $T_{\mathrm{m}}$ values of 63 °C at 0.5 µM primer in 1 M NaCl. (a) Why does $T_{\mathrm{m}}$ increase with primer concentration? (b) By how much does it change when the concentration is doubled, if $\Delta H^\circ = -623\,\mathrm{kJ\,mol^{-1}}$ and $\Delta S^\circ + R\ln(C_{\mathrm{T}}/4) = -1.85\,\mathrm{kJ\,mol^{-1}\,K^{-1}}$? (c) Why does a 2 °C rise in $T_{\mathrm{m}}$ matter less than a mismatch near the 3′ end of a primer?

   **Answer** (a) Duplex formation is bimolecular; by Le Chatelier's principle a higher strand concentration shifts the equilibrium towards the duplex, so a higher temperature is needed to dissociate half of it: in Eq. (11.3) the term $R\ln(C_{\mathrm{T}}/4)$ becomes less negative. (b) Doubling $C_{\mathrm{T}}$ adds $R\ln 2 = 5.76\,\mathrm{J\,mol^{-1}\,K^{-1}}$ to the denominator: $T_{\mathrm{m}} = 622\,600/(1852 - 5.8) = 337.2\,\mathrm{K}$ instead of $336.2\,\mathrm{K}$, about 1 °C higher. (c) The annealing temperature is chosen a few degrees below $T_{\mathrm{m}}$, so small shifts are tolerated; but DNA polymerase extends only primers whose 3′ terminal nucleotides are paired, so a 3′ mismatch prevents amplification almost completely even if the primer still anneals, which is used deliberately in allele-specific PCR.
4. Why is thymine rather than uracil used in DNA, although uracil is cheaper to make (thymidylate is synthesized from dUMP at the cost of a methyl group)? Why are CpG sites mutational hot spots in mammals?

   **Answer** Cytosine deaminates spontaneously to uracil about a hundred times per cell per day. Because uracil is not a normal DNA base, uracil–DNA glycosylase can remove every U and the repair system restores C from the G on the other strand. If U were a normal base, a U opposite G could not be distinguished from a legitimate U opposite A, and deamination would steadily convert G·C pairs to A·T pairs; the methyl group of thymine labels the legitimate base. At CpG sites cytosine is often methylated, and 5-methylcytosine deaminates to thymine, a normal base; the resulting T·G mismatch is repaired less efficiently, and if replication occurs first the change becomes a C → T transition, so methylated CpGs mutate about ten times faster than other sites.
5. Compare the Watson–Crick B-DNA model with the A form adopted by RNA duplexes. Why can RNA not form a B-form helix, and what consequence does the A form have for proteins that bind double-stranded RNA?

   **Answer** In B-DNA the sugars are C2′-endo, the base pairs sit on the axis nearly perpendicular to it, 10.5 bp per turn and 0.34 nm apart, and the major groove is wide; in the A form the sugars are C3′-endo, which shortens the distance between successive phosphates, so the helix has 11 bp per turn, 0.26 nm rise, base pairs tilted by about 20° and displaced from the axis, a deep, narrow major groove and a shallow minor groove. The 2′-OH of ribose clashes sterically with the neighbouring nucleotide in the C2′-endo pucker and favours C3′-endo, so RNA duplexes are A-form. Their major groove is too narrow for an α helix to read the bases, so double-stranded RNA-binding proteins recognize the shape of the backbone and the 2′-OH groups across the minor groove rather than the sequence; this is why dsRNA recognition (by Dicer, PKR or ADAR) is largely sequence-independent.
6. In Griffith's experiment, heat-killed virulent pneumococci "transform" live nonvirulent cells. Design the control experiments by which Avery, MacLeod and McCarty excluded protein, RNA and polysaccharide as the transforming principle, and explain why Hershey and Chase used $^{32}\mathrm{P}$ and $^{35}\mathrm{S}$.

   **Answer** Fractionate the extract of virulent cells and test each fraction for transforming activity on rough cells; then treat the active fraction with specific enzymes: proteases (trypsin, chymotrypsin) and ribonuclease leave the activity intact, whereas deoxyribonuclease destroys it; the capsular polysaccharide is removed by a specific depolymerase or by precipitation without loss of activity. The active material has the elemental composition (N/P ratio) of DNA, UV absorption at 260 nm, high viscosity and sedimentation of DNA, and gives the diphenylamine reaction of deoxyribose. Hershey and Chase needed labels that distinguish the two candidates: phosphorus is in DNA but not (to any extent) in the phage proteins, sulfur (in Cys and Met) is in protein but not in DNA, so the fate of each component during infection could be followed separately.
