---
title: Translation and the Genetic Code
description: How the genetic code was broken (triplets, frameshift genetics, poly(U), mixed copolymers, triplet binding, repeating copolymers); the structure of the code, its degeneracy, robustness and variants; tRNA, wobble and the minimum set of tRNAs; aminoacyl-tRNA synthetases, identity elements and the double sieve; the ribosome as a ribozyme; initiation in bacteria and eukaryotes, the elongation cycle and termination and recycling; antibiotics and toxins; the energy cost of a peptide bond, kinetic proofreading (Hopfield–Ninio) and the speed, accuracy and economics of translation; processing of the polypeptide and its targeting by signal sequences.
---

Translation turns the sequence of an mRNA into the sequence of a protein. It is the most expensive process in a growing cell, taking most of its energy and, in a fast-growing bacterium, a third of its dry mass in ribosomes, tRNAs and factors, and it is the only step of the central dogma where information changes alphabet. That change needs a dictionary, the genetic code, and an adaptor that reads one alphabet and carries the other, the tRNA charged by its aminoacyl-tRNA synthetase. This chapter follows the logic in that order: how the code was deciphered and what its structure tells (19.1–19.2), how tRNAs read codons and how synthetases load the right amino acid on them (19.3–19.4), the ribosome and its cycle of initiation, elongation and termination (19.5–19.6), the drugs that block it (19.7), the quantitative questions of how a machine whose individual binding steps discriminate only about a hundredfold makes one error in $10^4$, and at what cost (19.8), and finally what happens to the new chain: its processing and its delivery to the right compartment (19.9). The chemistry of the **peptide bond** is in [6.5.33](/6.5.33), folding and **molecular chaperones** in [7.1.6](/7.1.6), and the regulation of translation in [7.2.20](/7.2.20).

## 19.1. Breaking the Code

### 19.1.1. The Adaptor and the Messenger

Three discoveries of the 1950s set the problem. Zamecnik and colleagues gave rats a pulse of radioactive amino acids and found the label first in small ribonucleoprotein particles of the liver cytoplasm, later called ribosomes. Hoagland and Zamecnik then found that amino acids are first activated by ATP and attached to a small, soluble RNA, later called transfer RNA. Crick had predicted such an RNA in his adaptor hypothesis (1955): amino-acid side chains have no shape complementary to bases, so each amino acid should be carried by an adaptor that pairs with the template by hydrogen bonds. The template itself was found last. The rapid induction of enzymes in *E. coli* suggested to Jacob and Monod that genes act through a short-lived intermediate, and in 1961 Brenner, Jacob and Meselson showed that after T4 phage infection new, phage-specific RNA associates with pre-existing ("old") ribosomes, so the ribosome is a nonspecific machine that reads an unstable messenger.

**Definition 19.1.1** **Messenger RNA** (mRNA) is the RNA that carries the sequence of a protein-coding gene to the ribosome, where it serves as the template for translation. Its coding sequence is read in consecutive nucleotide triplets.

### 19.1.2. A Triplet Code Read from a Fixed Start

Twenty amino acids cannot be specified by single bases ($4^1 = 4$) or pairs ($4^2 = 16$); triplets give $4^3 = 64$ words, more than enough, so the code must use at least three bases per amino acid. Three properties were then established by genetics and protein chemistry.

**Example 19.1.1 (The code is read in triplets from a fixed point)** Crick, Brenner and colleagues (1961) used proflavine, which inserts or deletes single base pairs, in the *rIIB* gene of phage T4. A single insertion (+) or deletion (−) destroyed gene function, and so did two insertions; but a + and a − close together, or three insertions (+ + +) or three deletions close together, restored function. The interpretation: the message is read from a fixed starting point in groups of a fixed size; an insertion shifts every downstream group (a frameshift), and three shifts restore the frame. The size of the group is three (or a multiple of three), there are no "commas" between groups, and most triplets must be meaningful, because the stretch between two compensating mutations, read out of frame, still yielded a working protein.

The code is also nonoverlapping: amino-acid replacements in the coat proteins of tobacco mosaic virus mutants and in abnormal human hemoglobins change single residues, never two neighbors, which an overlapping code would require.

**Definition 19.1.2** The **genetic code** is the set of rules by which the nucleotide sequence of an mRNA specifies the amino-acid sequence of a protein. A **codon** is a triplet of consecutive nucleotides that specifies one amino acid or the end of the chain. A **reading frame** is one of the three ways of dividing a nucleotide sequence into consecutive codons; it is set by the start codon and maintained without gaps or overlaps.

An mRNA has three possible reading frames on each strand of its gene; an **open reading frame** ([7.2.2](/7.2.2)) is one that runs a long way without a stop codon.

### 19.1.3. Deciphering the Dictionary

The words were assigned between 1961 and 1966 by biochemistry in cell-free extracts of *E. coli*, which make polypeptides from any added RNA in the presence of ATP, GTP, amino acids and, at high $\ce{Mg^2+}$, without a start signal.

1. Homopolymers. Nirenberg and Matthaei (1961) added poly(U), made with polynucleotide phosphorylase, to 20 extracts, each with one $^{14}\mathrm{C}$-labeled amino acid. Only the tube with $[^{14}\mathrm{C}]$Phe made labeled polypeptide, polyphenylalanine: UUU codes for Phe. Poly(A) gave polylysine and poly(C) polyproline (AAA = Lys, CCC = Pro); poly(G) forms four-stranded structures and was not translated.
2. Random copolymers gave the base composition of codons. Polynucleotide phosphorylase incorporates NDPs in proportion to their concentrations, so the frequency of each triplet can be predicted and compared with the amino acids incorporated (Example 19.1.2).
3. Triplet binding. Nirenberg and Leder (1964) found that a trinucleotide alone causes a specific aminoacyl-tRNA to bind to ribosomes. Ribosome–tRNA complexes are retained on a nitrocellulose filter, free aminoacyl-tRNA passes through; testing each of the 64 trinucleotides with each labeled aminoacyl-tRNA assigned about 50 codons unambiguously.
4. Repeating copolymers. Khorana combined organic synthesis with enzymatic copying to make RNAs of defined repeating sequence (Example 19.1.3), which settled the remaining assignments and showed the stop codons.

**Example 19.1.2 (Composition from a random copolymer)** A random copolymer made from UDP and CDP in the ratio $3:1$ contains UUU with probability $(3/4)^3 \approx 0.42$, each triplet with two U and one C ($\mathrm{UUC}$, $\mathrm{UCU}$, $\mathrm{CUU}$) with probability $(3/4)^2(1/4) \approx 0.14$, each with one U and two C with $0.047$, and CCC with $0.016$. Relative to Phe ($= 100$), Ser and Leu were incorporated at about 30–40 and Pro at about 4–5, as expected if Phe has UUU (and a 2U1C codon), Ser and Leu codons with 2U1C, and Pro mainly C-rich codons. Such data give compositions but not order: they cannot distinguish UUC from UCU.

**Example 19.1.3 (Repeating copolymers)** Khorana's polymers fix the sequence of the possible triplets.

| Template | Triplets in the three frames | Product | Conclusion |
|---|---|---|---|
| $(\mathrm{UC})_n$ | UCU, CUC alternating in every frame | Ser–Leu–Ser–Leu… | UCU and CUC encode Ser and Leu (one each) |
| $(\mathrm{UUC})_n$ | UUC, UCU or CUU, one per frame | polyPhe, polySer and polyLeu | one frame each |
| $(\mathrm{UAUC})_n$ | UAU CUA UCU AUC, repeating | (Tyr–Leu–Ser–Ile)$_n$ | combined with triplet binding: UAU Tyr, CUA Leu, UCU Ser, AUC Ile |
| $(\mathrm{GUAA})_n$ | GUA AGU AAG UAA… | only di- and tripeptides | UAA is a stop codon |

A repeating dinucleotide gives an alternating dipeptide whatever the frame, a repeating trinucleotide gives three homopolymers (one per frame), and a repeating tetranucleotide gives a single repeating tetrapeptide unless one of its four triplets is a stop codon. By 1966 all 64 codons were assigned; the 1968 Nobel Prize went to Nirenberg, Khorana, and Holley, who sequenced the first tRNA.

## 19.2. Structure of the Code

### 19.2.1. The Code Table

| First (5′) | U | C | A | G | Third (3′) |
|---|---|---|---|---|---|
| U | UUU Phe, UUC Phe | UCU Ser, UCC Ser | UAU Tyr, UAC Tyr | UGU Cys, UGC Cys | U, C |
| U | UUA Leu, UUG Leu | UCA Ser, UCG Ser | UAA stop, UAG stop | UGA stop, UGG Trp | A, G |
| C | CUU Leu, CUC Leu | CCU Pro, CCC Pro | CAU His, CAC His | CGU Arg, CGC Arg | U, C |
| C | CUA Leu, CUG Leu | CCA Pro, CCG Pro | CAA Gln, CAG Gln | CGA Arg, CGG Arg | A, G |
| A | AUU Ile, AUC Ile | ACU Thr, ACC Thr | AAU Asn, AAC Asn | AGU Ser, AGC Ser | U, C |
| A | AUA Ile, AUG Met | ACA Thr, ACG Thr | AAA Lys, AAG Lys | AGA Arg, AGG Arg | A, G |
| G | GUU Val, GUC Val | GCU Ala, GCC Ala | GAU Asp, GAC Asp | GGU Gly, GGC Gly | U, C |
| G | GUA Val, GUG Val | GCA Ala, GCG Ala | GAA Glu, GAG Glu | GGA Gly, GGG Gly | A, G |

The columns are the second base. Codons are written $5' \to 3'$; AUG is also the start codon (Met at internal positions), and in bacteria GUG and, rarely, UUG can start a chain, then read as (f)Met.

**Definition 19.2.1** A **stop codon** (nonsense or termination codon) is a codon, UAA, UAG or UGA in the standard code, that specifies no amino acid and signals the end of the polypeptide; the other 61 are sense codons. A **start codon** is the codon at which translation begins, usually AUG. Different codons that specify the same amino acid are **synonymous codons**, and the fact that most amino acids have more than one codon is the **degeneracy** of the code.

The code is degenerate but not ambiguous: a codon has one meaning, an amino acid may have several codons. Its structure is not random.

- Only Met and Trp have a single codon; nine amino acids have two, Ile three, five have four, and Leu, Ser and Arg six (figure, A).
- Synonymous codons are clustered: they usually differ only at the third position. $\mathrm{XYU}$ and $\mathrm{XYC}$ always mean the same, $\mathrm{XYA}$ and $\mathrm{XYG}$ nearly always (the exceptions are AUA/AUG and UGA/UGG). Of all single-base substitutions in sense codons, about 69 % at the third position are synonymous, against 4 % at the first and none at the second (figure, B).
- The second base correlates with chemistry: a U at the second position always gives a hydrophobic amino acid (Phe, Leu, Ile, Met, Val), and charged amino acids have A or G there. Substitutions that do change the amino acid therefore often preserve its character. Measuring this with a hydropathy scale, the standard code comes out better than more than 99 % of random codes with the same block structure (figure, C); with other measures of amino-acid similarity, such as Woese's polar requirement, the code is "one in a million" (Freeland and Hurst, 1998). Whether this reflects selection for error minimization or the history of how amino acids were added to the code is debated ([7.2.23](/7.2.23)).

![Structure of the standard genetic code, computed from the code table. A: degeneracy: two amino acids have one codon, nine two, one (Ile) three, five four and three (Leu, Ser, Arg) six. B: fraction of all single-base substitutions in the 61 sense codons that are synonymous, missense or nonsense, by codon position: the third position is 69 % synonymous, the second never. C: robustness: mean squared change of Kyte–Doolittle hydropathy caused by single-base missense substitutions, for the standard code (red line) and for 20,000 random codes made by reassigning the 20 amino acids among the synonymous codon blocks of the standard code; fewer than 1 % of the random codes do better](./plots/genetic-code.py)

Synonymous codons are not used equally. Each organism has a characteristic codon usage, and highly expressed genes prefer codons read by abundant tRNAs; in *E. coli* the rare Arg codons AGA and AGG slow translation of heterologous genes, which is why "codon-optimized" sequences are used in expression vectors ([7.2.5](/7.2.5)). Synonymous **mutations** are therefore not always neutral: they can change the speed of translation, mRNA stability ([7.2.18](/7.2.18)), splicing signals and cotranslational folding.

### 19.2.2. Variants and Additions

The code is nearly but not absolutely universal. Its variants are reassignments of a few codons, mostly stop codons and rare codons, in small genomes.

| Genome | Change from the standard code |
|---|---|
| Vertebrate mitochondria | UGA = Trp; AUA = Met; AGA and AGG are not read as Arg (they end two open reading frames, probably by a −1 frameshift to a UAG) |
| Yeast mitochondria | UGA = Trp; AUA = Met; CUN = Thr |
| *Mycoplasma*, *Spiroplasma* | UGA = Trp |
| Ciliates (*Tetrahymena*, *Paramecium*) | UAA and UAG = Gln (only UGA is stop) |
| Many *Candida* species | CUG = Ser instead of Leu |

Two further amino acids are inserted by recoding a stop codon in particular mRNAs, and are sometimes counted as the 21st and 22nd ([7.1.3](/7.1.3)). Selenocysteine is encoded by UGA in a few proteins, among them glutathione peroxidases, thioredoxin reductases and bacterial formate dehydrogenase. Its tRNA ($\mathrm{tRNA^{Sec}}$, anticodon UCA) is charged with Ser by seryl-tRNA synthetase, the Ser is converted to selenocysteine on the tRNA, and a special elongation factor (SelB in bacteria, eEFSec with SBP2 in eukaryotes) delivers it only to UGA codons of mRNAs that carry a selenocysteine insertion sequence (SECIS), a stem-loop just downstream of the UGA in bacteria and in the $3'$ UTR in eukaryotes. Pyrrolysine, in some methanogenic archaea and bacteria, is encoded by UAG, is made as a free amino acid and is attached to its own tRNA by a dedicated synthetase, a pair now widely used to add nonnatural amino acids to proteins ([7.2.23](/7.2.23)).

Small viral genomes use the code more than once. The $5386\,\mathrm{nt}$ genome of phage ΦX174 encodes eleven proteins totaling more than its coding capacity in one frame: gene *E* lies within gene *D*, and gene *B* within *A*, read in different frames, and gene *K* overlaps *A* and *C*. Overlapping genes in different frames also occur in λ, SV40, HIV and SARS-CoV-2, and are rare in cellular genomes.

## 19.3. Transfer RNA and Wobble

### 19.3.1. Structure of tRNA

Holley and colleagues (1965) sequenced yeast $\mathrm{tRNA^{Ala}}$ ($77\,\mathrm{nt}$) after seven years of work. All tRNAs, $73$–$93\,\mathrm{nt}$ long, share the same secondary structure, the cloverleaf, and the same L-shaped tertiary structure (Kim, Rich and colleagues and Robertus, Klug and colleagues, 1974, from crystals of yeast $\mathrm{tRNA^{Phe}}$).

**Definition 19.3.1** A **transfer RNA** (tRNA) is an adaptor RNA of $73$–$93\,\mathrm{nt}$ that carries an amino acid esterified to its $3'$-terminal adenosine and recognizes the corresponding codon of an mRNA by base pairing with its **anticodon**, the three nucleotides at positions 34–36 in the loop of its anticodon arm.

The cloverleaf has four arms: the acceptor stem (7 bp, formed by the $5'$ and $3'$ ends, ending in the single-stranded $\mathrm{CCA}$ to whose terminal adenosine the amino acid is attached, [7.2.17](/7.2.17)); the D arm (with dihydrouridine); the anticodon arm; a variable loop (3–21 nt, the main source of length differences); and the TΨC arm (with ribothymidine and pseudouridine). In three dimensions the acceptor and T stems stack into one helix and the D and anticodon stems into another, at right angles, so that the anticodon and the CCA end lie at the two ends of the L, about $7.5\,\mathrm{nm}$ apart: the distance between the decoding center of the small ribosomal subunit and the peptidyl transferase center of the large one. Ten to fifteen percent of tRNA nucleotides are modified; the modifications at positions 34 and 37 tune codon reading.

### 19.3.2. The Wobble Hypothesis

If each sense codon had its own tRNA, a cell would need 61. Purified tRNAs, however, often read several codons: yeast $\mathrm{tRNA^{Ala}}$, with the anticodon $5'$-IGC-$3'$ containing inosine (I) at position 34, reads GCU, GCC and GCA. Crick explained this in 1966.

**Definition 19.3.2 (Wobble Hypothesis)** The **wobble hypothesis** states that the first two bases of a codon pair with the anticodon by standard Watson–Crick pairs, whereas the third base of the codon pairs with the first base of the anticodon (position 34, the wobble position) under a looser steric constraint that allows certain nonstandard pairs.

The allowed pairs (codon and anticodon are antiparallel, so codon position 3 pairs with anticodon position 34):

| Anticodon base 34 | Codon bases read at position 3 | Codons per tRNA |
|---|---|---|
| C | G | 1 |
| A (rare; usually modified to I) | U | 1 |
| U | A, G | 2 |
| G | U, C | 2 |
| I | U, C, A | 3 |

Two consequences follow. Codons that differ in the first or second base need different tRNAs; and a two-codon box ending in U/C or in A/G can be read by one tRNA, so that a minimum of about 31 tRNAs, plus the initiator tRNA, i.e. 32, suffice for the 61 codons. Real cells deviate in both directions: *E. coli* has 86 tRNA genes encoding about 40 species with different anticodons, and human cells several hundred genes for about 50 anticodons; human mitochondria manage with 22 tRNAs, because a modified or unmodified U at position 34 can read all four codons of a family box ("superwobble"). Modifications at position 34 also restrict or redirect wobble: 2-thiouridine derivatives in the tRNAs for Lys, Glu and Gln confine reading to A- and G-ending codons and so prevent misreading of the U- and C-ending codons of the same box (Asn, Asp, His); and in bacteria the conversion of C34 of a minor $\mathrm{tRNA^{Ile}}$ (anticodon CAU) to lysidine makes it read AUA (Ile) instead of AUG (Met). Wobble is in part a trade-off: the third pair binds weakly, so a tRNA leaves the ribosome quickly enough for translation to be fast, but the first two pairs are checked strictly (19.5.2).

## 19.4. Aminoacyl-tRNA Synthetases

### 19.4.1. The Reaction

Each amino acid is attached to its tRNAs by one enzyme, in two steps catalyzed at the same active site:

$$
\ce{aa + ATP <=> aa-AMP + PP_i}, \qquad \ce{aa-AMP + tRNA -> aa-tRNA + AMP}.
$$

In the first, the carboxylate of the amino acid attacks the α-phosphate of ATP, forming an enzyme-bound mixed anhydride, the aminoacyl adenylate; in the second, the $2'$- or $3'$-OH of the terminal adenosine of the tRNA attacks the carbonyl of the adenylate and forms an **ester**. The aminoacyl ester is a high-energy bond ($\Delta_{\mathrm{r}}G'^{\circ} \approx -29\,\mathrm{kJ\,mol^{-1}}$ for hydrolysis), which later drives peptide-bond formation. Inorganic pyrophosphatase hydrolyses the $\mathrm{PP_i}$, so two phosphoanhydride bonds are spent per amino acid and the reaction is irreversible.

```smiles
C[C@H](N)C(=O)OP(=O)(O)OC[C@H]1O[C@@H](n2cnc3c(N)ncnc32)[C@H](O)[C@@H]1O Ala-AMP
```

**Definition 19.4.1** An **aminoacyl-tRNA synthetase** (aaRS) is the enzyme that attaches a specific amino acid to the $3'$ end of its cognate tRNAs, through an aminoacyl adenylate intermediate formed from ATP. There is usually one synthetase per amino acid, which charges all the isoacceptor tRNAs for that amino acid.

The twenty synthetases fall into two unrelated structural classes of ten each, which approach the acceptor stem from opposite sides.

| | Class I | Class II |
|---|---|---|
| Catalytic domain | Rossmann fold, signature motifs HIGH and KMSKS | antiparallel β-sheet, motifs 1–3 |
| Quaternary structure | mostly monomeric | mostly dimeric or tetrameric |
| Approach to the tRNA | minor-groove side of the acceptor stem | major-groove side |
| First attachment | $2'$-OH (then moved to $3'$ by transesterification) | $3'$-OH (PheRS: $2'$-OH) |
| Amino acids | Arg, Cys, Gln, Glu, Ile, Leu, Met, Trp, Tyr, Val | Ala, Asn, Asp, Gly, His, Lys, Phe, Pro, Ser, Thr |

The $2'$/$3'$ difference does not matter for translation, because the ester migrates rapidly between the two hydroxyls. Some organisms lack a synthetase and use a two-step route instead: many bacteria and archaea charge $\mathrm{tRNA^{Gln}}$ with Glu and then amidate it ($\mathrm{Glu}\text{-}\mathrm{tRNA^{Gln}} \to \mathrm{Gln}\text{-}\mathrm{tRNA^{Gln}}$, by a transamidase).

### 19.4.2. Recognizing the Right tRNA

A synthetase must also choose among about 40–50 tRNA species, by recognizing the nucleotides and shapes that distinguish its cognate tRNAs, the identity elements, sometimes called the second genetic code. Crystal structures of synthetase–tRNA complexes, sequence comparison of tRNAs charged by the same enzyme and mutagenesis showed that identity elements lie mostly in the anticodon and in the acceptor stem, with the discriminator base 73 next to CCA.

- Anticodon. Changing the anticodon of $\mathrm{tRNA^{Val}}$ from UAC to CAU makes it a substrate for MetRS, and many synthetases (MetRS, GlnRS) contact all three anticodon bases.
- A single base pair. In all organisms examined, the main identity element of $\mathrm{tRNA^{Ala}}$ is the G3·U70 wobble pair in the acceptor stem (Hou and Schimmel, 1988): moving it into $\mathrm{tRNA^{Cys}}$ (which has C3·G70) or $\mathrm{tRNA^{Phe}}$ makes them accept Ala, and a hairpin minihelix of only 7 bp containing G3·U70, with no anticodon, is charged with Ala nearly as efficiently as the whole tRNA. The anticodon-independent recognition of the acceptor stem may be a relic of an operational code that preceded the codon–anticodon code ([7.2.23](/7.2.23)).

Once charged, the amino acid is not checked again: Chapeville, Lipmann, Benzer and colleagues (1962) reduced the Cys of $\mathrm{Cys\text{-}tRNA^{Cys}}$ to Ala with Raney nickel, and the resulting $\mathrm{Ala\text{-}tRNA^{Cys}}$ inserted Ala at Cys codons. The ribosome reads only the anticodon; fidelity of charging is entirely the synthetase's job.

### 19.4.3. Proofreading by the Double Sieve

Amino acids that differ by one methylene group, such as Ile and Val, differ in binding free energy by at most a few $\mathrm{kJ\,mol^{-1}}$. Ile-tRNA synthetase activates Ile about 200 times more often than Val at equal concentrations, which would give one Val at every 200 Ile codons, yet the observed misincorporation of Val for Ile is about 1 in 3000 or less.

**Definition 19.4.2** The **double-sieve mechanism** (Fersht) is the proofreading of aminoacylation by two active sites of a synthetase: a synthetic site that excludes amino acids larger than (or differently shaped from) the cognate one, and an editing site that admits only amino acids smaller than the cognate one and hydrolyses their adenylates (pre-transfer editing) or their esters with tRNA (post-transfer editing).

In IleRS the editing domain, about $3\,\mathrm{nm}$ from the synthetic site, accepts the CCA end carrying Val but not Ile, so the mischarged tRNA is hydrolyzed before it leaves; tRNA binding stimulates the editing of Val-AMP. Synthetases for amino acids without close analogs (for example CysRS, TyrRS) have no editing activity. Editing matters: a mouse with an editing defect in AlaRS (the *sticky* mutation) accumulates misfolded proteins and loses Purkinje neurons, and bacteria with editing-deficient synthetases are sensitive to nonproteinogenic amino acids. With editing, charging errors are typically $10^{-4}$–$10^{-5}$, below the error of decoding by the ribosome (figure of 19.8.4).

![Fidelity of aminoacylation. A: the double sieve of isoleucyl-tRNA synthetase: the synthetic site rejects amino acids larger than Ile (Phe) or of the wrong shape (Leu) and binds Gly and Ala too weakly, but activates Val about 1/200 as often as Ile; the editing site excludes Ile and hydrolyses Val-AMP and Val-tRNA(Ile), so only Ile-tRNA(Ile) leaves. B: typical error frequencies (order of magnitude) at the steps from gene to protein: transcription, aminoacylation, decoding by the ribosome (the largest), frameshifting, and the overall error of about one in 10⁴ residues](./plots/double-sieve.py)

## 19.5. The Ribosome

### 19.5.1. Composition

**Definition 19.5.1** A **ribosome** is the ribonucleoprotein complex that synthesizes proteins on an mRNA template; it consists of a small subunit, which binds the mRNA and decodes it, and a large subunit, which catalyzes peptide-bond formation, and it has three tRNA binding sites, A (aminoacyl), P (peptidyl) and E (exit), spanning both subunits.

| | Bacteria (*E. coli*) | Eukaryotes (cytoplasm, mammals) |
|---|---|---|
| Whole ribosome | 70S, $2.5\,\mathrm{MDa}$ | 80S, $4.2\,\mathrm{MDa}$ |
| Small subunit | 30S: 16S rRNA ($1542\,\mathrm{nt}$) + 21 proteins | 40S: 18S rRNA ($1869\,\mathrm{nt}$) + 33 proteins |
| Large subunit | 50S: 23S ($2904\,\mathrm{nt}$) and 5S ($120\,\mathrm{nt}$) rRNA + 33 proteins | 60S: 28S ($5070\,\mathrm{nt}$), 5.8S ($160\,\mathrm{nt}$) and 5S ($120\,\mathrm{nt}$) rRNA + 47 proteins |
| Mass fraction of RNA | about $2/3$ | about $1/2$ |

The S values are **sedimentation coefficients** and are not additive. The rRNAs are made and processed as described in [7.2.17](/7.2.17); eukaryotic subunits are assembled in the nucleolus with about 200 assembly factors and exported separately. The eukaryotic ribosome has the same conserved core as the bacterial one, with expansion segments of rRNA and additional proteins on its surface; mitochondria and chloroplasts have bacterial-type ribosomes, which is why some antibacterial drugs are toxic to mitochondria. A bacterial cell has $10^4$–$7 \times 10^4$ ribosomes depending on its growth rate (19.8.5), a mammalian cell several million.

### 19.5.2. Functional Centers

The ribosome is a **ribozyme** ([7.1.8](/7.1.8)). Noller and colleagues (1992) found that peptidyl transferase activity of *Thermus* 50S subunits survived extraction of most proteins with SDS, proteinase K and phenol but not RNase treatment. The crystal structure of the *Haloarcula* 50S subunit (Ban, Nissen, Moore and Steitz, 2000) settled the question: no protein lies within about $1.8\,\mathrm{nm}$ of the site where a transition-state analog was bound, which is made entirely of 23S rRNA. Structures of the 30S subunit (Ramakrishnan; Yonath) and of the 70S ribosome with tRNAs (Noller) followed; the 2009 Nobel Prize in Chemistry recognized this work.

**Definition 19.5.2** The **peptidyl transferase center** (PTC) is the active site of the large ribosomal subunit, formed by conserved nucleotides of domain V of 23S (28S) rRNA, where the α-amino group of the aminoacyl-tRNA in the A site attacks the ester carbonyl of the peptidyl-tRNA in the P site, transferring the peptide to the A-site tRNA.

The reaction is accelerated about $10^7$-fold, mostly by positioning the two substrates and excluding water (the rate enhancement is largely entropic, Sievers and colleagues, 2004), with a proton shuttle through the $2'$-OH of the P-site A76; no rRNA base acts as a classical general base. Four other functional regions are needed in each cycle.

- The decoding center of the small subunit, where 16S rRNA nucleotides A1492, A1493 and G530 flip out and inspect the minor groove of the first two codon–anticodon base pairs (Ogle and Ramakrishnan, 2001). Only Watson–Crick geometry fits, which is the structural basis of the strictness at codon positions 1 and 2 and of the tolerance at position 3. Aminoglycoside antibiotics bind here and lock the bases in the "on" position, so near-cognate tRNAs are accepted (19.7).
- The GTPase-associated center of the large subunit (the L7/L12 stalk, protein L11 and the sarcin–ricin loop of 23S rRNA), which binds all translational GTPases (IF2, EF-Tu, EF-G, RF3) at the same place and activates their GTP hydrolysis, so these factors hydrolyze GTP only when correctly bound.
- The exit tunnel, about $10\,\mathrm{nm}$ long and $1$–$2\,\mathrm{nm}$ wide, which holds the last 30–40 residues of the nascent chain; some helices form in it, and specific stalling peptides (SecM, ErmCL) interact with its walls.
- The mRNA channel between the subunits, where the mRNA is kinked by about $45^\circ$ between the A- and P-site codons, which keeps the reading frame.

Translation proceeds $5' \to 3'$ along the mRNA and the chain grows from its N- to its C-terminus. Dintzis (1961) gave reticulocytes a short pulse of $^3\mathrm{H}$-Leu and analyzed tryptic peptides of the completed hemoglobin chains: the label increased from the N- to the C-terminus, since chains completed during the pulse had been nearly finished when it began. Poly(A) with a C at its $3'$ end, $\mathrm{A}_n\mathrm{C}$, gave $\mathrm{Lys}_{n/3}$–Asn, with the AAC codon at the C-terminus.

**Definition 19.5.3** A **polysome** (polyribosome) is an mRNA translated simultaneously by several ribosomes.

Ribosomes initiate as soon as the previous one has cleared the start, and in electron micrographs they are spaced as closely as $80\,\mathrm{nt}$ on actively translated mRNAs; a typical human mRNA carries about 10–20 ribosomes, while about one third of mRNAs carry none at a given time. In bacteria translation begins on the nascent mRNA while it is still being transcribed (Miller spreads of *E. coli* show polysomes attached to the DNA by RNA polymerase), and the leading ribosome is physically coupled to RNA polymerase, which makes **attenuation** ([7.2.11](/7.2.11)) possible.

## 19.6. The Ribosome Cycle

Protein synthesis has five stages: charging of tRNAs (19.4), initiation, elongation, termination with recycling, and folding with processing (19.9). Initiation is usually the slowest and the most regulated step ([7.2.20](/7.2.20)).

**Definition 19.6.1** **Initiation factors**, **elongation factors** and **release factors** are the proteins that bind the ribosome transiently to catalyze, respectively, the assembly of a ribosome with mRNA and initiator tRNA at the start codon, the delivery of aminoacyl-tRNAs and the movement of the ribosome along the mRNA, and the release of the completed chain at a stop codon. Many of them are GTPases.

### 19.6.1. Initiation in Bacteria

Two tRNAs read AUG in all cells: an initiator, which only starts chains, and an elongator for internal Met. Both are charged by the same MetRS; in bacteria, the methionyl group on the initiator is then formylated by methionyl-tRNA formyltransferase, with $\mathrm{N^{10}}$-formyltetrahydrofolate as donor, giving $\mathrm{fMet\text{-}tRNA^{fMet}}$. Formylation blocks the amino group, which is in any case not needed in the first residue, and makes the initiator a poor substrate for EF-Tu and a good one for IF2. Archaea and eukaryotes use an unformylated $\mathrm{Met\text{-}tRNA_i^{Met}}$. The formyl group, and often the Met, are removed later (19.9.1).

The start codon is found by base pairing between the mRNA and rRNA. Shine and Dalgarno (1974) noticed that the $3'$ end of 16S rRNA, $3'$-AUUCCUCCA…-$5'$, is complementary to a purine-rich sequence upstream of bacterial start codons.

**Definition 19.6.2** The **Shine–Dalgarno sequence** is a purine-rich sequence (consensus AGGAGG) about 5–9 nt upstream of the start codon of a bacterial mRNA that pairs with the anti-Shine–Dalgarno sequence at the $3'$ end of 16S rRNA and so positions the start codon in the P site of the 30S subunit; together with the start codon it forms the ribosome-binding site.

Steitz and Jakes (1975) isolated the 16S rRNA fragment paired with an mRNA initiation region after colicin E3 cleavage, and Hui and de Boer (1987) showed that changing the anti-SD sequence of a specialized ribosome redirects it to mRNAs with the complementary SD. Pairing strength and spacing matter: the optimum spacer is about 7 nt, and sequestering the SD or the start codon in a hairpin blocks initiation (the basis of RNA thermometers and riboswitches, [7.2.18](/7.2.18), [7.2.20](/7.2.20)). A polycistronic mRNA has one ribosome-binding site per cistron; many bacterial mRNAs (and most in some archaea and in *Mycobacterium*) are leaderless, starting directly with AUG.

The 30S initiation complex assembles with three initiation factors:

| Factor | Function |
|---|---|
| IF1 | binds the A site, preventing premature binding of tRNAs there; stimulates IF2 and IF3 |
| IF2 | GTPase; binds $\mathrm{fMet\text{-}tRNA^{fMet}}$ and places it in the P site; after 50S joining, hydrolyzes GTP and leaves |
| IF3 | binds the 30S subunit and prevents it from joining 50S (anti-association); destabilizes complexes with non-initiator tRNAs or non-start codons (fidelity of start-site selection) |

The 30S subunit with IF3, mRNA, IF1, IF2·GTP and $\mathrm{fMet\text{-}tRNA^{fMet}}$ forms the 30S initiation complex; the mRNA and the initiator can bind in either order. The 50S subunit then joins, IF2 hydrolyses its GTP (GTP is needed for IF2 binding at physiological IF2 concentrations, but hydrolysis is needed only for its release), and all factors leave, giving a 70S initiation complex with $\mathrm{fMet\text{-}tRNA^{fMet}}$ in the P site and the second codon in the empty A site. $\mathrm{fMet\text{-}tRNA^{fMet}}$ is the only aminoacyl-tRNA that enters the P site directly, without passing the A site.

**Example 19.6.1 (Puromycin defines the A and P sites)** Puromycin is an analog of the $3'$ end of tyrosyl-tRNA in which the amino acid is linked by an amide rather than an ester. It binds the A site, accepts the peptide from a P-site peptidyl-tRNA and then, being unable to be attacked in turn, leaves with it, so it releases peptidyl-puromycin from any ribosome whose P site is occupied by a peptidyl-tRNA. Before translocation the new peptidyl-tRNA sits in the A site and does not react; after translocation it does. In initiation complexes formed with $[^{35}\mathrm{S}]\mathrm{fMet\text{-}tRNA^{fMet}}$, fMet-puromycin was formed at once, without EF-G, whereas $\mathrm{Met\text{-}tRNA}$ elongator bound in response to AUG did not react: the initiator goes directly to the P site.

![Initiation of translation. A: bacteria: the Shine–Dalgarno sequence (AGGAGG) pairs with the anti-SD sequence near the 3′ end of 16S rRNA, which places the AUG in the P site, about 7 nt downstream; IF2·GTP brings fMet-tRNAfMet, IF1 occupies the A site and IF3 keeps the 30S subunit free of 50S until the start is set. B: eukaryotes: eIF4F (cap-binding eIF4E, scaffold eIF4G, helicase eIF4A) on the m⁷G cap, PABP on the poly(A) tail bound to eIF4G (closed loop), and the 43S complex (40S subunit with eIF1, eIF1A, eIF3 and the ternary complex eIF2·GTP·Met-tRNAi) that scans 5′→3′ to the first AUG in a good Kozak context (gccRccAUGG, with a purine at −3 and G at +4)](./plots/initiation.py)

### 19.6.2. Initiation in Eukaryotes

Eukaryotic mRNAs have no Shine–Dalgarno sequence; the small subunit is recruited to the **5′ cap** ([7.2.17](/7.2.17)) and finds the start codon by scanning, a model proposed by Kozak (1978) from the observation that the AUG closest to the $5'$ end is used in about 90 % of mRNAs.

**Definition 19.6.3** In the **scanning model** of eukaryotic initiation, a 43S complex (the 40S subunit with initiation factors and $\mathrm{Met\text{-}tRNA_i^{Met}}$) binds the capped $5'$ end of an mRNA and moves $3'$ along the $5'$ untranslated region until the anticodon of the initiator tRNA pairs with an AUG in a suitable context; the **Kozak sequence** $\mathrm{gcc}\,\mathrm{R}\,\mathrm{cc}\,\boldsymbol{AUG}\,\mathrm{G}$ (A of AUG $= +1$; R a purine) is the optimal context, in which the purine at $-3$ and the G at $+4$ are the most important positions.

Kozak mutated the positions around the AUG of preproinsulin mRNA and measured translation: a purine at $-3$ or a G at $+4$ was sufficient for efficient initiation, and with both absent many 40S subunits passed the AUG. Passing a weak first AUG and starting at a downstream one is called leaky scanning and is used to make two proteins with different N-termini from one mRNA. A hairpin with a stability below about $-210\,\mathrm{kJ\,mol^{-1}}$ ($-50\,\mathrm{kcal\,mol^{-1}}$ in the original report) between the cap and the AUG blocks scanning, whereas a moderate hairpin just after a weak AUG, which pauses the 40S with the AUG in the P site, improves its use. The steps and factors:

| Factor | Role in initiation |
|---|---|
| eIF1, eIF1A | bind the 40S near the P and A sites; keep the 43S in an open, scanning conformation and reject non-AUG and poor-context start sites; eIF1 is released at the start codon |
| eIF2 | heterotrimeric GTPase ($\alpha\beta\gamma$); as eIF2·GTP binds $\mathrm{Met\text{-}tRNA_i^{Met}}$ (the ternary complex) and brings it to the 40S |
| eIF2B | the **guanine nucleotide-exchange factor** that regenerates eIF2·GTP from eIF2·GDP (the main target of regulation, [7.2.20](/7.2.20)) |
| eIF3 | 13 subunits in mammals; binds the 40S, prevents its joining with 60S, links 43S to eIF4G |
| eIF4F = eIF4E + eIF4G + eIF4A | eIF4E binds the $\mathrm{m^7G}$ cap; eIF4G is a scaffold binding eIF4E, eIF4A, eIF3 and PABP; eIF4A is an ATP-dependent DEAD-box **helicase** that unwinds the $5'$ UTR, stimulated by eIF4B (and eIF4H) |
| eIF5 | the **GTPase-activating protein** of eIF2; at the start codon, release of the $\mathrm{P_i}$ makes the selection irreversible |
| eIF5B | GTPase homologous to IF2; joins the 60S subunit, hydrolyses GTP and leaves together with eIF1A |
| PABP | binds the poly(A) tail and eIF4G, circularizing the mRNA (closed loop); stimulates initiation |

The pathway: eIF1, eIF1A, eIF3 and eIF5 bind the 40S subunit; the ternary complex joins to form the 43S preinitiation complex; eIF4F with eIF4B on the cap recruits it to form the 48S complex; the 48S complex scans; at an AUG in good context, codon–anticodon pairing in the P site closes the 40S, eIF1 leaves, eIF5 causes release of $\mathrm{P_i}$ from eIF2, and eIF2·GDP departs; eIF5B·GTP joins the 60S subunit, hydrolyses GTP and leaves, giving the 80S initiation complex. Cap-binding was found by cross-linking a cap-labeled mRNA to a $24\,\mathrm{kDa}$ protein (eIF4E), and a protein fraction containing it stimulated translation of capped but not uncapped mRNAs. Poliovirus shows that eIF4G is the bridge: the viral protease 2A cleaves eIF4G, separating its eIF4E-binding N-terminal part from the C-terminal part (p100) that binds eIF3 and eIF4A, so host capped mRNAs are no longer translated while the viral RNA, which recruits p100 through an internal ribosome entry site, is ([7.2.20](/7.2.20)).

| | Bacteria | Eukaryotes |
|---|---|---|
| Initiator | $\mathrm{fMet\text{-}tRNA^{fMet}}$ | $\mathrm{Met\text{-}tRNA_i^{Met}}$ |
| Recognition of the start | Shine–Dalgarno pairing with 16S rRNA, several per mRNA | cap binding and scanning to the first good AUG; one start per mRNA (monocistronic) |
| Factors | 3 | at least 12 (more than 25 polypeptides) |
| Energy | 1 GTP (IF2) | 1 GTP (eIF2), 1 GTP (eIF5B), ATP for scanning |

### 19.6.3. Elongation

Elongation adds one amino acid per cycle in three steps (figure), each driven or checked by a GTPase.

1. Decoding. The aminoacyl-tRNA arrives in a ternary complex with EF-Tu·GTP (eukaryotic eEF1A), first in an A/T state in which its anticodon samples the A-site codon while its acceptor end is still held by EF-Tu. EF-Tu is the most abundant protein of *E. coli* (about 5 % of total protein, roughly one copy per tRNA molecule); it protects the ester bond from hydrolysis and excludes uncharged tRNA. Codon–anticodon pairing checked by the decoding center closes the small subunit, which activates the GTPase of EF-Tu at the GTPase center. EF-Tu·GDP has low affinity for aminoacyl-tRNA and leaves; the aminoacyl end swings into the PTC (accommodation). EF-Ts (eEF1B), a nucleotide-exchange factor, regenerates EF-Tu·GTP.
2. Peptidyl transfer. The peptide moves from the P-site tRNA to the aminoacyl-tRNA in the A site, which now carries a peptide one residue longer.
3. Translocation. The tRNAs move spontaneously into hybrid states, with their acceptor ends in the P and E sites of the large subunit and their anticodons still in the A and P sites (A/P and P/E). EF-G·GTP (eukaryotic eEF2) binds, hydrolyses GTP and, by a large conformational change in which its domain IV occupies the A site of the small subunit, moves the mRNA and the anticodon stem-loops by exactly one codon. The deacylated tRNA leaves from the E site, and the A site is free for the next ternary complex.

**Definition 19.6.4** **Ribosomal translocation** is the movement of the mRNA and the two tRNAs bound to it through the ribosome by one codon ($3\,\mathrm{nt}$) after each peptidyl transfer, catalyzed by EF-G (eEF2) with GTP hydrolysis, which brings the peptidyl-tRNA from the A to the P site and the deacylated tRNA from the P to the E site.

![The elongation cycle on the ribosome (bacterial names). 1: decoding: the ternary complex EF-Tu·GTP·Gly-tRNA (anticodon 3′-CCA-5′) samples the GGU codon in the A site, next to the peptidyl-tRNA (Met-Ala-Phe on tRNA-Phe) in the P site; codon–anticodon pairing triggers GTP hydrolysis. 2: after EF-Tu·GDP leaves, the aminoacyl end enters the peptidyl transferase center of 23S rRNA, and the peptide is transferred to Gly-tRNA. 3: the tRNAs move into hybrid A/P and P/E states, and EF-G·GTP binds. 4: GTP hydrolysis by EF-G drives translocation of mRNA and tRNAs by 3 nt; the deacylated tRNA leaves from the E site, and the A site presents the next codon (AAA). One cycle takes about 50 ms in E. coli](./plots/elongation-cycle.py)

**Example 19.6.2 (Roles of GTP in elongation)** The steps were separated with a nonhydrolyzable analog, GDPCP (the β–γ bridge is a methylene). With EF-Tu (in the crude fraction EF-T, which contains EF-Ts) and GDPCP, aminoacyl-tRNA bound to ribosomes in response to its codon, but no peptide bond formed: delivery needs GTP, peptide-bond formation needs its hydrolysis, because EF-Tu must leave. The antibiotic kirromycin, which allows GTP hydrolysis but holds EF-Tu·GDP on the ribosome, also blocks peptide-bond formation, and the structure of the ribosome with kirromycin-stalled EF-Tu captured the A/T state, with the tRNA bent by about $30^\circ$ away from the PTC. Kaziro and colleagues prepared ribosomes with deacylated tRNA in the P site and labeled peptidyl-tRNA in the A site, and measured translocation by the puromycin reactivity of the peptide: EF-G with GTP translocated efficiently, EF-G with GDPCP translocated once but stayed bound. GTP hydrolysis is therefore needed to release EF-G; fast kinetics later showed that hydrolysis precedes and accelerates translocation, about 50-fold, so that it both drives the step and recycles the factor.

The translational GTPases are a family with a common logic, described in [7.1.14](/7.1.14) for signaling G proteins: they bind the ribosome in the GTP form, the ribosome itself is their GTPase-activating protein at one shared site, and GDP release is catalyzed by a separate exchange factor (EF-Ts for EF-Tu, eIF2B for eIF2) or is spontaneous (EF-G, which has low affinity for GDP). EF-G and the class 1 release factors mimic the shape of an EF-Tu·tRNA complex, and EF-Tu, EF-G and the release factors cannot bind the ribosome at the same time.

### 19.6.4. Termination and Recycling

Stop codons are read by proteins, not by tRNAs.

**Definition 19.6.5** A **release factor** is a protein that recognizes a stop codon in the A site and causes hydrolysis of the ester bond between the polypeptide and the P-site tRNA. Class 1 release factors (bacterial RF1 for UAA and UAG, RF2 for UAA and UGA; eukaryotic eRF1 for all three) read the codon and catalyze hydrolysis; class 2 factors (RF3, eRF3) are GTPases that assist them.

Class 1 factors read the stop codon with a "tripeptide anticodon" (Pro-X-Thr in RF1, Ser-Pro-Phe in RF2; the NIKS and YxCxxxF motifs in eRF1) and place a universally conserved Gly-Gly-Gln (GGQ) motif in the PTC, where the backbone amide of the Gln positions a water molecule as the nucleophile; the peptidyl transferase thus transfers the peptide to water instead of to an amino group. The roles of the class 2 factors differ between the domains:

- Bacteria: RF3·GTP binds after the peptide has been released and removes RF1 or RF2; RF3 is not needed for release itself and is dispensable in *E. coli*. Ribosome recycling factor (RRF), which binds the A site, and EF-G·GTP then split the 70S ribosome, and IF3 releases the deacylated tRNA and mRNA from the 30S subunit, ready for the next round.
- Eukaryotes: eRF3·GTP delivers eRF1 to the A site, as EF-Tu delivers a tRNA; GTP hydrolysis by eRF3 places the GGQ of eRF1 in the PTC, and peptide release follows. The ATPase ABCE1 (Rli1 in yeast) then binds, together with eRF1, and splits the 80S ribosome by ATP hydrolysis; eIF1, eIF1A, eIF3 (with eIF3j), or the ligatin and DENR–MCT-1 proteins, release the tRNA and mRNA from the 40S subunit.

Stop codons are occasionally read through by near-cognate tRNAs (about $10^{-4}$–$10^{-3}$ per stop codon, more for UGA followed by C), and some viral and cellular mRNAs use programmed readthrough or frameshifting at slippery sequences to make two proteins. A premature stop codon in a eukaryotic mRNA triggers **nonsense-mediated decay** ([7.2.18](/7.2.18)), and ribosomes stalled without a stop codon are rescued by quality-control systems ([7.2.20](/7.2.20)).

## 19.7. Antibiotics and Toxins

Many antibiotics are natural products that target the bacterial ribosome, the largest target in the cell; their binding sites, mapped by resistance mutations and structures, are mostly rRNA, and they were the tools that defined many of the steps above.

| Agent | Target and action | Organisms affected |
|---|---|---|
| Puromycin | A site of the large subunit; accepts the peptide and causes premature release (Example 19.6.1) | bacteria and eukaryotes |
| Tetracyclines | 30S, A site; block binding of the ternary complex | bacteria |
| Streptomycin and other aminoglycosides (kanamycin, gentamicin) | 30S decoding center (16S rRNA, protein S12); induce misreading at low concentrations; streptomycin blocks initiation at high concentrations | bacteria |
| Chloramphenicol | PTC of 50S (23S rRNA); prevents accommodation of the aminoacyl end in the A site | bacteria, mitochondria |
| Macrolides (erythromycin) | exit tunnel of 50S; block passage of the nascent chain, causing context-specific stalling | bacteria |
| Oxazolidinones (linezolid) | PTC A site of 50S | bacteria |
| Fusidic acid | EF-G on the ribosome after GTP hydrolysis; blocks its release | bacteria |
| Kirromycin | EF-Tu; holds EF-Tu·GDP on the ribosome | bacteria |
| Thiostrepton | GTPase-associated center (L11, 23S rRNA); blocks factor binding | bacteria |
| Cycloheximide | E site of the 60S subunit; blocks elongation (translocation) | eukaryotes |
| Anisomycin | PTC of the 60S subunit | eukaryotes |
| Harringtonine, lactimidomycin | stall ribosomes at start codons; used to map initiation sites by **ribosome profiling** ([7.2.6](/7.2.6)) | eukaryotes |
| Diphtheria toxin | ADP-ribosylates diphthamide, a modified His of eEF2, using $\mathrm{NAD^+}$; one molecule can kill a cell | eukaryotes |
| Ricin, Shiga toxin | N-glycosidases that remove adenine A4324 from the sarcin–ricin loop of 28S rRNA, inactivating the GTPase center | eukaryotes |

The bacterial selectivity of most antibiotics rests on differences between bacterial and eukaryotic rRNAs at their sites; the residual toxicity of aminoglycosides (hearing loss) and chloramphenicol (bone marrow) comes from binding to mitochondrial ribosomes.

## 19.8. A Quantitative View: Energy, Accuracy and Speed

### 19.8.1. The Energy Account

**Formula 19.8.1 (Cost of a peptide bond)** The formation of each peptide bond between specified amino acids consumes at least four phosphoanhydride bonds: two in aminoacylation ($\ce{ATP -> AMP + PP_i}$, $\ce{PP_i -> 2P_i}$), one GTP hydrolyzed by EF-Tu and one by EF-G. Initiation (IF2), termination (RF3) and recycling (EF-G with RRF) add about three per chain, and proofreading adds more for every rejected aminoacyl-tRNA (19.8.2).

With about $30.5\,\mathrm{kJ\,mol^{-1}}$ per bond, at least $4 \times 30.5 = 122\,\mathrm{kJ\,mol^{-1}}$ is spent on a bond whose hydrolysis releases only about $21\,\mathrm{kJ\,mol^{-1}}$, so the net standard free-energy change is about $-100\,\mathrm{kJ\,mol^{-1}}$ (with cellular concentrations, much more negative). The excess is not needed to make a peptide bond, which needs only one activated ester, but to make the right one: two of the four bonds pay for the irreversible charging and editing, two for the irreversible, proofreading-capable delivery and the directed movement of the ribosome. The cost is large: an *E. coli* cell doubling in $40\,\mathrm{min}$ makes about $3 \times 10^6$ proteins of about 300 residues, i.e. about $4 \times 10^9$ phosphoanhydride bonds for translation, the largest item of its energy budget (estimates range from about half to most of the ATP and GTP spent on biosynthesis).

![The economics of translation. A: fraction of chains without any wrong residue, (1 − ε)^L, against chain length for per-residue errors ε = 10⁻³, 10⁻⁴ and 10⁻⁵, with a typical bacterial protein (300 aa), a large protein (1000 aa) and titin (about 34,000 aa) marked: at ε = 10⁻⁴, 97 % of 300-residue and 90 % of 1000-residue chains are perfect. B: phosphoanhydride bonds spent per peptide bond: two for aminoacylation, one each for EF-Tu and EF-G, about 0.01 per bond for initiation, termination and recycling of a 300-residue chain, and an illustrative few percent for rejected ternary complexes and editing. C: the bacterial growth law (Scott, Hwa and colleagues, 2010): the RNA/protein mass ratio, proportional to the ribosome content, increases linearly with growth rate as r = r₀ + λ/κ_t (r₀ = 0.087, κ_t = 4.5 h⁻¹ for E. coli under nutrient variation); doubling times are marked at the top](./plots/translation-economics.py)

### 19.8.2. Kinetic Proofreading

Translation errors arise mostly in decoding, where a tRNA with a near-cognate anticodon (one mismatch) competes with the cognate one. The difference in their binding free energy, $\Delta\Delta G$, is a few $\mathrm{kcal\,mol^{-1}}$ at most. If a single binding step selected the tRNA at equilibrium, the error ratio would be set by a **Boltzmann factor**:

$$
f_0 = \frac{K_{\mathrm{D},C}}{K_{\mathrm{D},D}} = \mathrm{e}^{-\Delta\Delta G/k_{\mathrm{B}}T}, \tag{19.1}
$$

where $C$ and $D$ denote the correct and the wrong substrate at equal concentrations. With $\Delta\Delta G \approx 4.6\,k_{\mathrm{B}}T$ ($11\,\mathrm{kJ\,mol^{-1}}$), $f_0 \approx 10^{-2}$, a hundred times more errors than observed. Hopfield (1974) and Ninio (1975) independently showed how a cell can do better by spending energy: **kinetic proofreading** ([6.3.18](/6.3.18)).

**Formula 19.8.2 (Hopfield's scheme)** Let a substrate $X \in \{C, D\}$ bind the enzyme with rate constant $k_{\mathrm{on}}$ (the same for both) and dissociate with $k_{\mathrm{off},X}$; let the complex $EX$ be converted, irreversibly and at the same rate $m$ for both, into a second state $EX^*$ (for EF-Tu, by GTP hydrolysis), from which $X$ either dissociates with rate constant $l_X$ or is used to make product with rate constant $W$; let both dissociation steps discriminate by the same factor, $k_{\mathrm{off},D}/k_{\mathrm{off},C} = l_D/l_C = \mathrm{e}^{\Delta\Delta G/k_{\mathrm{B}}T} \equiv q$. In steady state, the rate of product formation from $X$ is $k_{\mathrm{on}}[X]\,\dfrac{m}{k_{\mathrm{off},X} + m}\,\dfrac{W}{l_X + W}$, so the error ratio is
$$
f = \frac{k_{\mathrm{off},C} + m}{k_{\mathrm{off},D} + m}\cdot\frac{l_C + W}{l_D + W} \;\to\; \frac{1}{q^2} = f_0^2 \quad (m \ll k_{\mathrm{off},C},\ W \ll l_C). \tag{19.2}
$$
With $n$ independent proofreading stages of this kind, each driven by an irreversible step, $f \to f_0^{\,n+1}$.

**Proof** In steady state the flux into $EX^*$ equals the flux out of $EX$ through $m$. Binding gives $EX$ at rate $k_{\mathrm{on}}[E][X]$, and each $EX$ is converted with probability $m/(k_{\mathrm{off},X} + m)$, the ratio of the competing first-order rates. Each $EX^*$ makes product with probability $W/(l_X + W)$. The product of the two probabilities times the binding rate is the production rate; taking the ratio for $D$ and $C$ with $[C] = [D]$ cancels $k_{\mathrm{on}}[E][X]$ and gives Eq. (19.2). In the limits stated, each factor tends to $1/q$; a further stage multiplies by another factor of the same form. $\square$

The scheme works because the irreversible step erases the memory of the first selection: a wrong substrate that has passed the first test gets a second, independent chance to leave, and since the step is irreversible (driven by GTP hydrolysis far from equilibrium), it cannot return to $EX$ and re-equilibrate with the correct one. Without the energy input, the second state would be in equilibrium with the first and the discrimination would not multiply; this is the thermodynamic content of the idea ([6.3.18](/6.3.18)). The figure checks the formula by following $10^5$ simulated binding events, each a sequence of random choices between the competing first-order steps, as in a **Gillespie algorithm** ([4.4.7](/4.4.7)).

The price is paid in speed and energy. The limits in Eq. (19.2) mean that most correct substrates are also rejected: the fraction of $EC^*$ that makes product is $W/(l_C + W)$, so each correct product costs on average $1 + l_C/W$ irreversible steps, and the rate of correct product formation is reduced by the same factor. Accuracy close to $f_0^2$ thus requires $W \ll l_C$, many futile cycles and slow production (figure, C). Real enzymes work at an intermediate point.

![Kinetic proofreading. A: Hopfield's scheme with one proofreading stage: reversible binding (k_on, k_off,X), an irreversible energy-consuming step (m, GTP hydrolysis), and a second state from which the substrate can still dissociate (l_X) or be used (W); both dissociation rates differ by the factor exp(ΔΔG/kT) between correct and wrong substrates. B: error ratio against ΔΔG for no, one and two proofreading stages from Eq. (19.2) (solid, with m/k_off,C = W/l_C = 0.05) and the ideal limits exp(−(n+1)ΔΔG/kT) (dashed); points: simulation of single binding events for one stage. C: the price of accuracy for one stage at ΔΔG = 4.6 kT (f₀ = 0.01): lowering the commitment rate W relative to the rejection rate l_C brings the error from 10⁻² towards 10⁻⁴, at a cost of 1 + l_C/W GTP per correct product](./plots/kinetic-proofreading.py)

### 19.8.3. Two Selection Stages on the Ribosome

Pre-steady-state kinetics of *E. coli* ribosomes (Thompson; Rodnina and Wintermeyer and colleagues) identified the two stages of Hopfield's scheme in decoding. In initial selection, before GTP hydrolysis by EF-Tu, a near-cognate ternary complex dissociates much faster from the codon-recognition complex than a cognate one and, more importantly, activates the GTPase of EF-Tu orders of magnitude more slowly, because the decoding center closes the 30S subunit only around Watson–Crick pairs. This induced-fit step makes initial selection better than the binding energies alone would allow. In proofreading, after GTP hydrolysis and the departure of EF-Tu, a near-cognate aminoacyl-tRNA accommodates slowly and is often rejected, while a cognate one accommodates in a few milliseconds. GTP hydrolysis by EF-Tu is the irreversible step that separates the two stages, as in Formula 19.8.2. Together they give errors of about $10^{-4}$–$10^{-3}$ for most near-cognate competitors, with the largest errors at particular codon–anticodon mismatches such as G·U at the first or second position.

The balance between speed and accuracy is set genetically. Mutations in ribosomal protein S12 (*rpsL*) that confer streptomycin resistance make ribosomes hyperaccurate and slow (restrictive), whereas *ram* mutations in S4 and S5 increase errors and speed (ribosomal ambiguity); EF-Tu mutants that hydrolyze GTP faster also increase errors. An *E. coli* ribosome adds about 15–20 amino acids per second at $37^\circ\mathrm{C}$, a eukaryotic one about 5, with an error of about one in $10^4$.

### 19.8.4. How Many Proteins Are Correct?

**Formula 19.8.3 (Error-free chains)** If errors occur independently with probability $\varepsilon$ per residue, the number of wrong residues in a chain of $L$ residues follows the **binomial distribution** ([3.1.4](/3.1.4)), and the fraction of chains without any error is
$$
p_0 = (1 - \varepsilon)^L \approx \mathrm{e}^{-\varepsilon L}. \tag{19.3}
$$

For $\varepsilon = 10^{-4}$, $p_0 = 0.97$ for $L = 300$, $0.905$ for $L = 1000$ (about 91 % of 1000-residue proteins are perfect), and only $0.03$ for titin ($L \approx 34{,}000$). The error rate thus limits the length of proteins that can be made reliably, and long proteins are often assembled from several chains or tolerate errors at most positions. Most errors are conservative replacements by near-cognate tRNAs and many are harmless; a defective protein molecule is degraded, and errors are not inherited. Errors are more costly in other ways: Drummond and Wilke (2008) argued that the cost of misfolding of mistranslated proteins explains why highly expressed proteins evolve slowly and use optimal codons.

### 19.8.5. The Speed of the Ribosome and the Growth of a Cell

At 15–20 residues per second, a 300-residue protein takes about $15$–$20\,\mathrm{s}$ in *E. coli* (Lehninger's figure: 100 residues in about $5\,\mathrm{s}$), and $1$–$2\,\mathrm{min}$ in a mammalian cell. Initiation on a strong bacterial mRNA occurs every few seconds, so that a polysome carries a ribosome every 100–200 nt, near the closest packing allowed by a footprint of about $30\,\mathrm{nt}$.

Because ribosomes make all proteins, including ribosomal proteins, the elongation rate bounds the growth rate. A ribosome contains about $7500$ amino acids of protein; at 20 per second it takes about $6\,\mathrm{min}$ to make the protein of one ribosome. Even a cell consisting only of ribosomes could therefore not double faster than about $6\,\mathrm{min}$; *E. coli* in rich medium, which devotes about 30–40 % of its protein to ribosomes and the translation apparatus, doubles in about $20\,\mathrm{min}$. More generally, if a fraction $\phi_R$ of the cell's protein is ribosomal and each ribosome makes protein at rate $k_{\mathrm{el}}$ (residues per unit time), the protein mass $M$ grows as $\mathrm{d}M/\mathrm{d}t = k_{\mathrm{el}}N_R$ with $N_R \propto \phi_R M$, which gives a **steady state** of exponential growth with rate
$$
\lambda = \kappa\,(\phi_R - \phi_{R,0}), \tag{19.4}
$$
where $\kappa$ is proportional to $k_{\mathrm{el}}$ and $\phi_{R,0}$ accounts for ribosomes that are inactive or not elongating at full speed. Measurements of the RNA/protein ratio of *E. coli* in different media confirmed this linear relation (Scott, Hwa and colleagues, 2010; figure, C); when translation is slowed by antibiotics such as chloramphenicol, cells instead increase their ribosome content as growth slows, a second line that fixed the proteome allocation of bacteria into sectors and made the growth law a quantitative model of bacterial physiology ([7.11](/7.11)). The ppGpp-mediated stringent response, which reduces rRNA synthesis when uncharged tRNAs accumulate in the A site, is one mechanism by which cells set $\phi_R$ according to the supply of amino acids ([7.2.20](/7.2.20)).

## 19.9. From Polypeptide to Functional Protein

### 19.9.1. Processing of the Nascent Chain

The chain begins to fold and to be modified while it is still emerging from the exit tunnel. In bacteria the chaperone trigger factor binds the ribosome next to the tunnel exit, and in eukaryotes the nascent-polypeptide-associated complex (NAC) does so; downstream, the Hsp70 and chaperonin systems take over ([7.1.6](/7.1.6)). The common **post-translational modifications** ([7.1.3](/7.1.3)) include:

| Modification | Enzyme and rule | Examples and function |
|---|---|---|
| Removal of the formyl group and of Met | peptide deformylase (bacteria), then methionine aminopeptidase if the second residue is small (Gly, Ala, Ser, Thr, Cys, Pro, Val) | determines the N-terminal residue and thus, in part, the half-life ([7.2.20](/7.2.20)); deformylase is an antibiotic target |
| N-terminal acetylation | N-terminal acetyltransferases (NatA–NatF), cotranslational | about 80 % of human soluble proteins |
| Removal of signal sequences and propeptides | signal peptidase (19.9.2); prohormone convertases | proinsulin → insulin; zymogens of digestive proteases |
| Disulfide bonds | protein disulfide isomerase in the ER | secreted and extracellular proteins |
| Glycosylation | oligosaccharyltransferase (N-linked, cotranslational in the ER); Golgi glycosyltransferases (O-linked) | **glycoproteins** ([7.1.10](/7.1.10)) |
| Lipid attachment | N-myristoylation of Gly2 (cotranslational), palmitoylation of Cys, prenylation of CaaX boxes, GPI anchors | membrane association of Src, Ras, heterotrimeric G proteins |
| Phosphorylation, methylation, acetylation of side chains | **protein kinases** and other enzymes | regulation ([7.1.14](/7.1.14)) |
| γ-carboxylation of Glu | vitamin K–dependent carboxylase | blood-clotting factors (Ca²⁺ binding) |
| Attachment of prosthetic groups | heme, biotin, lipoate, flavin | cytochromes, carboxylases |

### 19.9.2. Signal Sequences and the SRP Cycle

All proteins of a cell (except the few encoded by organelles) begin their synthesis on free cytosolic ribosomes, and the information that sends them elsewhere is in the protein. Blobel and Dobberstein (1975) proposed the signal hypothesis: secretory proteins carry an N-terminal signal that directs the ribosome making them to the ER membrane and the chain through it; Blobel later (1980) generalized it to the idea that every protein carries signals for its location (Nobel Prize 1999). The first evidence was that immunoglobulin light chain made in vitro without membranes was about $1.5\,\mathrm{kDa}$ larger than the secreted chain, and that adding microsomes during, but not after, translation produced the mature size inside the vesicles.

**Definition 19.9.1** A **signal sequence** (signal peptide) is an N-terminal segment of 13–36 residues that targets a protein to the endoplasmic reticulum in eukaryotes, or to the plasma membrane for secretion in bacteria; it has a positively charged n-region, a hydrophobic h-region of 7–15 residues and a polar c-region ending in a small residue (often Ala) before the cleavage site, and is usually removed by signal peptidase on the far side of the membrane.

**Definition 19.9.2** The **signal recognition particle** (SRP) is the ribonucleoprotein, in mammals the $300\,\mathrm{nt}$ 7SL RNA and six proteins (SRP9, 14, 19, 54, 68 and 72), that binds a signal sequence as it emerges from the ribosome, slows elongation, and brings the ribosome to the SRP receptor on the ER membrane.

The SRP cycle (figure): the hydrophobic groove of the M domain of SRP54 binds the signal sequence, and the Alu domain reaches into the elongation-factor binding site and slows translation, which gives time for targeting. SRP54 and the SRP receptor α subunit are GTPases; their GTP-bound forms bind each other, the ribosome is transferred to the Sec61 translocon ($\alpha\beta\gamma$), and reciprocal GTP hydrolysis dissociates SRP from its receptor for another round. The chain is threaded through the aqueous pore of Sec61 as it is made (cotranslational translocation); a lateral gate in Sec61α lets hydrophobic segments enter the lipid bilayer as transmembrane helices. In the lumen, signal peptidase cuts off the signal, oligosaccharyltransferase transfers a preassembled $\mathrm{Glc_3Man_9GlcNAc_2}$ oligosaccharide from dolichol pyrophosphate to Asn in Asn-X-Ser/Thr (X not Pro), forming an **N-linked glycan** ([7.1.10](/7.1.10)), and chaperones and protein disulfide isomerase fold the protein. Tunicamycin, an analog of UDP-GlcNAc, blocks the first step of dolichol-linked oligosaccharide synthesis and so prevents N-glycosylation.

![Cotranslational targeting to the endoplasmic reticulum. 1: the signal sequence (n-, h- and c-regions) of a nascent chain emerges from the ribosome. 2: SRP (7SL RNA with SRP54 binding the signal) binds and slows elongation. 3: SRP·GTP docks on the SRP receptor (SR·GTP) in the ER membrane, the ribosome is transferred to the Sec61 translocon, and GTP hydrolysis by SRP54 and SRα releases SRP, which is recycled. 4: translation resumes and the chain is threaded through Sec61 into the lumen, where signal peptidase (SPase) removes the signal and oligosaccharyltransferase adds N-linked glycans](./plots/srp-targeting.py)

### 19.9.3. Other Destinations

Each destination has its own signal and machinery. What happens to proteins after they enter the ER, their sorting in the Golgi apparatus, vesicle traffic, secretion and endocytosis, and the import machinery of organelles are the subject of cell biology ([7.3](/7.3)); the signals themselves are listed here.

| Destination | Signal | Import or sorting machinery |
|---|---|---|
| ER (secretory pathway) | N-terminal signal sequence or first transmembrane segment | SRP, SR, Sec61 (cotranslational); small proteins post-translationally by Sec62/63 |
| ER retention | C-terminal KDEL (Lys-Asp-Glu-Leu) | KDEL receptor returns escaped proteins from the Golgi |
| Lysosome | mannose 6-phosphate on N-linked glycans, recognized by a patch on the folded protein | GlcNAc-phosphotransferase (with UDP-GlcNAc) and uncovering enzyme in the Golgi; M6P receptors. Deficiency of the phosphotransferase (I-cell disease) makes cells secrete their hydrolases |
| Mitochondrial matrix | N-terminal amphipathic helix (presequence), cleaved | TOM and TIM complexes, membrane potential, matrix Hsp70; unfolded import post-translationally |
| Chloroplast stroma | N-terminal transit peptide, cleaved | TOC and TIC complexes |
| Peroxisome | C-terminal Ser-Lys-Leu (PTS1) or N-terminal PTS2 | Pex5 or Pex7; folded proteins are imported |
| Nucleus | internal nuclear localization signal, not cleaved (SV40 T antigen: PKKKRKV) | importins, nuclear pore, Ran-GTP gradient |
| Bacterial periplasm and outer membrane | N-terminal signal sequence like the eukaryotic one | SecB (chaperone keeping the chain unfolded), SecA (ATPase motor), SecYEG; or Tat for folded proteins |
| Bacterial inner membrane | hydrophobic transmembrane segment | bacterial SRP (Ffh with 4.5S RNA) and receptor FtsY, cotranslational |

The bacterial and eukaryotic signal sequences are interchangeable in many cases, and SecYEG is homologous to Sec61: cotranslational targeting is one of the oldest features of cells. The common principle is that sorting signals are read by soluble receptors that bring their cargo to a membrane translocase, and that energy (GTP, ATP or the membrane potential) makes the transport directional; post-translational import requires chaperones (Hsp70, SecB) to keep proteins unfolded.

## Summary

- The code (Definition 19.1.2): a triplet, nonoverlapping, comma-free code read from a fixed start (Example 19.1.1); deciphered with cell-free translation of homopolymers, random copolymers (Example 19.1.2), triplet binding and repeating copolymers (Example 19.1.3). 61 sense codons, 3 stop codons, AUG as start (Definition 19.2.1); degenerate (synonymous codons mostly differ at position 3), robust to point errors, nearly universal (mitochondrial and nuclear variants; selenocysteine at UGA, pyrrolysine at UAG).
- tRNA (Definition 19.3.1): cloverleaf, L shape with anticodon and CCA end $7.5\,\mathrm{nm}$ apart; wobble at codon position 3 (Definition 19.3.2), so about 32 tRNAs suffice.
- Aminoacyl-tRNA synthetases (Definition 19.4.1): $\ce{aa + ATP -> aa-AMP + PP_i}$, then transfer to the tRNA; two classes of ten; identity elements in the anticodon and acceptor stem (G3·U70 of $\mathrm{tRNA^{Ala}}$); the ribosome does not check the amino acid; double-sieve editing (Definition 19.4.2) lowers charging errors to $10^{-4}$–$10^{-5}$.
- Ribosome (Definition 19.5.1): 70S = 30S + 50S, 80S = 40S + 60S; A, P and E sites; a ribozyme: peptidyl transferase center of 23S rRNA (Definition 19.5.2); decoding center (A1492, A1493, G530), GTPase center, exit tunnel. Synthesis N → C, mRNA read $5' \to 3'$, on polysomes (Definition 19.5.3).
- Initiation (Definition 19.6.1): bacteria: fMet-tRNA, Shine–Dalgarno pairing (Definition 19.6.2), IF1–3, IF2·GTP. Eukaryotes: cap, eIF4F, closed loop, 43S scanning to an AUG in Kozak context (Definition 19.6.3), eIF2·GTP·Met-tRNAi, eIF2B, eIF5, eIF5B.
- Elongation: EF-Tu·GTP delivery and decoding; peptidyl transfer; hybrid states and EF-G-driven translocation by 3 nt (Definition 19.6.4); GTP hydrolysis is needed to release EF-Tu before peptide-bond formation and to drive translocation (Example 19.6.2).
- Termination (Definition 19.6.5): RF1 (UAA, UAG), RF2 (UAA, UGA), eRF1 (all), GGQ motif; RF3 removes RF1/2, eRF3 delivers eRF1; recycling by RRF + EF-G (bacteria), ABCE1 (eukaryotes).
- Inhibitors (19.7) define and block each step; bacterial selectivity comes from rRNA differences.
- Quantities: at least 4 phosphoanhydride bonds per peptide bond (Formula 19.8.1); equilibrium discrimination $f_0 = \mathrm{e}^{-\Delta\Delta G/k_{\mathrm{B}}T}$ (Eq. (19.1)); kinetic proofreading multiplies discrimination at the price of futile GTP hydrolysis and speed (Formula 19.8.2, Eq. (19.2)); error $\sim 10^{-4}$, error-free fraction $(1-\varepsilon)^L$ (Formula 19.8.3); 15–20 residues per second in *E. coli*; growth rate proportional to ribosome content (Eq. (19.4)).
- After synthesis: N-terminal processing, cotranslational folding and modification; signal sequences (Definition 19.9.1) and SRP (Definition 19.9.2) target ribosomes to Sec61; other signals for lysosomes, mitochondria, chloroplasts, peroxisomes and the nucleus ([7.3](/7.3)).

## Questions

1. Crick and Brenner found that three closely spaced insertions restored *rIIB* function but that one insertion and one deletion far apart did not. Explain both results, and what the experiment showed about the fraction of triplets that encode amino acids.

   **Answer** Each insertion shifts the reading frame downstream by one nucleotide; three shift it by three, restoring the original frame after the third mutation. Between the first and the third mutation the sequence is read out of frame, so a few amino acids are wrong; the protein still works only if that region tolerates changes and if none of the out-of-frame triplets is a stop codon. A + and a − far apart leave a long out-of-frame region, which almost certainly contains a stop codon or so many wrong residues that the protein is inactive. That the region between nearby compensating mutations could be read in a wrong frame without hitting a stop showed that most triplets have meaning, i.e. that the code is degenerate rather than using 20 of 64 triplets.

2. A random copolymer is made from ADP and CDP in the ratio $5:1$. Which amino acids should be incorporated, and in what proportions relative to Lys?

   **Answer** Triplet frequencies: AAA $(5/6)^3 = 0.579$; each of AAC, ACA, CAA $(5/6)^2(1/6) = 0.116$; each of ACC, CAC, CCA $0.023$; CCC $0.0046$. AAA = Lys; AAC = Asn, ACA = Thr, CAA = Gln (each $0.116/0.579 = 20$ % of Lys); ACC = Thr, CAC = His, CCA = Pro ($4$ % each); CCC = Pro ($0.8$ %). Relative to Lys = 100: Asn 20, Gln 20, Thr 24, His 4, Pro 4.8.

3. How many different tRNAs are minimally required to read the four Leu codons of the CUN box and the two Leu codons UUA and UUG, according to the wobble rules? Which anticodons could they have?

   **Answer** Three. CUU, CUC and CUA can be read by one tRNA with anticodon $5'$-IAG-$3'$ (I pairs with U, C and A), and CUG by one with $5'$-CAG-$3'$ (or both CUA and CUG by $5'$-UAG-$3'$, with IAG or GAG reading CUU and CUC). UUA and UUG differ from CUN in the first base and need a separate tRNA, $5'$-UAA-$3'$, whose U34 reads A and G. (Modified U34 can read all four CUN codons, as in mitochondria.)

4. Why is proofreading by aminoacyl-tRNA synthetases necessary even though the ribosome checks codon–anticodon pairing with great care?

   **Answer** The ribosome checks only the anticodon, not the amino acid attached to the tRNA (the $\mathrm{Ala\text{-}tRNA^{Cys}}$ experiment). An amino acid misattached to a tRNA is therefore inserted at the codon of the tRNA, and the synthetase is the only place where the identity of the amino acid is checked. For amino acids that differ only by a methylene group, the binding energy allows a discrimination of about 200, so a second, editing step is needed to reach errors of $10^{-4}$ or less.

5. Using Eq. (19.2), compute the error ratio of a proofreading scheme with $q = 100$, $m/k_{\mathrm{off},C} = 0.1$ and $W/l_C = 0.1$. How many GTP are hydrolyzed per correct product, and how much of the maximal accuracy $f_0^2$ is achieved?

   **Answer** First factor: $(1 + 0.1)/(100 + 0.1) = 0.0110$; second: $(1 + 0.1)/(100 + 0.1) = 0.0110$; $f = 1.21 \times 10^{-4}$, close to the limit $f_0^2 = 10^{-4}$ (compared with $f_0 = 10^{-2}$ without proofreading). Each GTP hydrolysis converts one $EC$ into $EC^*$, of which a fraction $W/(l_C + W) = 0.1/1.1 = 0.091$ makes product, so about $1/0.091 = 11$ GTP are hydrolyzed per correct product (plus the small number spent on wrong substrates). Raising $W/l_C$ to $1$ would cost only 2 GTP per product but give $f = 1.1 \times 10^{-2} \times 2 \times 10^{-2} = 2.2 \times 10^{-4}$.

6. Explain why a nonhydrolyzable GTP analog allows binding of aminoacyl-tRNA to the A site but blocks peptide-bond formation, while EF-G with the analog allows a single translocation.

   **Answer** EF-Tu·GTP binds aminoacyl-tRNA and the ribosome; its GTP form is needed for delivery, and the analog is a GTP form. Peptide-bond formation requires the acceptor end of the tRNA to leave EF-Tu and move into the PTC, which happens only after EF-Tu has hydrolysed GTP and changed to its low-affinity GDP form; with GDPCP, EF-Tu stays and holds the tRNA in the A/T state. EF-G·GDPCP can bind the pre-translocation ribosome in its hybrid state and move the tRNAs once (more slowly, because hydrolysis accelerates the movement), but it cannot leave without hydrolysis, so the next ternary complex cannot bind and there is no second round.

7. A mutant *E. coli* lacks RF2. Which stop codons can still be used, and which genes would be affected? What would happen to proteins encoded by genes ending in UGA?

   **Answer** RF1 still reads UAA and UAG, so genes ending in these codons terminate normally. Genes ending in UGA (about 30 % of *E. coli* genes) are read through by near-cognate tRNAs (such as $\mathrm{tRNA^{Trp}}$) or ribosomes stall at the stop codon and are rescued by tmRNA and alternative rescue factors ([7.2.20](/7.2.20)); proteins with C-terminal extensions or tags for degradation result. RF2 is in fact essential in *E. coli*; its own synthesis is autoregulated by a programmed +1 frameshift at an in-frame UGA early in its gene, which RF2 itself terminates.

8. Estimate the minimal doubling time of a bacterium in which all protein is ribosomal, if a ribosome contains 7500 residues of protein and elongates at 20 residues per second. Why is the real minimal doubling time of *E. coli* about three times longer?

   **Answer** Each ribosome makes its own protein in $7500/20 = 375\,\mathrm{s} \approx 6.3\,\mathrm{min}$; with exponential growth, $\lambda = 20/7500\,\mathrm{s^{-1}} = 9.6\,\mathrm{h^{-1}}$, a doubling time of $\ln 2/\lambda \approx 4.3\,\mathrm{min}$. In a real cell, ribosomal proteins are at most about a third of the protein, the rest being metabolic enzymes, transporters and structural proteins that the ribosomes must also make, and part of the ribosomes are not elongating at full speed (the $\phi_{R,0}$ of Eq. (19.4)); this lowers $\lambda$ roughly threefold, to the observed doubling time of about $20\,\mathrm{min}$.

9. (Open question) Design an experiment, using a reporter and drugs listed in 19.7, to test whether a particular mRNA is translated by scanning from the cap or by internal initiation.

   **Answer** Possible design: insert the $5'$ UTR in question into a bicistronic reporter between two luciferase coding sequences (Renilla first, firefly second, separated by a stop codon and the test UTR); cap-dependent translation makes only the first, and the second is made only if the UTR allows internal initiation. Controls: an empty or inert spacer (no second product) and a known IRES (positive control); a hairpin before the first cistron to block scanning from the cap (the second product should persist if it is internally initiated); and northern blots or RT-qPCR across the junction to exclude cryptic promoters or splicing that would produce a monocistronic second mRNA, a classic artifact. Inhibitors can separate mechanisms: cleavage of eIF4G by poliovirus 2A protease, or eIF4A inhibitors, reduce cap-dependent translation but spare many IRESs. Ribosome profiling with harringtonine can map the initiation sites directly.
