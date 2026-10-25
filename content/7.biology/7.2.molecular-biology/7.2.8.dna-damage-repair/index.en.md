---
title: DNA Damage and Repair
description: Spontaneous and induced DNA damage and its rates; mutations, transitions and transversions; direct reversal (photolyase, MGMT, AlkB) and base-excision repair; nucleotide-excision repair and transcription-coupled repair; methyl-directed and eukaryotic mismatch repair; double-strand breaks, nonhomologous end joining and the choice of homologous recombination; damage tolerance by translesion synthesis and the SOS response; the Ames test, repair defects and cancer, synthetic lethality; models of lesion steady states, SOS gene timing and mutation accumulation.
---

The fidelity of **replication** ([7.2.7](/7.2.7)) would be wasted if DNA did not stay intact between replications. It does not: DNA is a large molecule in water at $37^\circ\mathrm{C}$, surrounded by reactive metabolites, and in each human cell it suffers tens of thousands of chemical changes every day. Unlike proteins and RNA, which are replaced from the genetic information when damaged, the genome can be restored only by repairing it, and almost every repair system relies on the same principle: the information lost from one strand is recovered from the complementary strand. This chapter surveys the damage and the mutations it causes (8.1), the repair systems that excise damaged bases (8.2), bulky lesions (8.3) and replication errors (8.4), the repair of double-strand breaks, where no intact complementary strand exists (8.5), the tolerance of damage that cannot be repaired in time (8.6), the connection between repair and cancer (8.7), and simple models of how damage becomes mutation (8.8). The chemistry of the lesions themselves (deamination, depurination, oxidation, photodimers) is described in [7.1.11](/7.1.11); homologous recombination, the most accurate repair of double-strand breaks, has its own chapter ([7.2.9](/7.2.9)); and the consequences of mutations for phenotype and inheritance belong to genetics ([7.4](/7.4)).

## 8.1. Damage and Mutation

### 8.1.1. Lesions and Mutations

**Definition 8.1.1** A **DNA lesion** is a chemical alteration of DNA, such as a modified or missing base, a cross-link or a strand break. A **mutation** is a heritable change in the nucleotide sequence. Substitutions of one base pair for another are **transitions** when a purine replaces a purine (and a pyrimidine a pyrimidine), and **transversions** when a purine replaces a pyrimidine or vice versa; insertions and deletions add or remove nucleotides.

A lesion is not yet a mutation. It becomes one when the DNA is replicated before the lesion is repaired and a polymerase inserts the wrong base opposite it, or when a repair process itself restores the strand incorrectly. A mismatch made by a polymerase is converted into a mutation at the next round of replication, when each strand serves as a template. The race between repair and replication is therefore the central quantitative fact of this chapter (8.8).

### 8.1.2. Sources and Rates of Damage

| Lesion | Typical cause | Approximate number per human cell per day | Consequence if unrepaired |
|---|---|---|---|
| Abasic (AP) site from depurination | Spontaneous hydrolysis of the N-glycosidic bond | $5000$–$10{,}000$ (pyrimidines about $500$) | Polymerases stall or insert A ("A rule") |
| Uracil from cytosine deamination | Spontaneous hydrolysis | $100$–$500$ | G·C → A·T transition |
| Thymine from 5-methylcytosine deamination | Spontaneous hydrolysis at CpG | tens | G·C → A·T transition at CpG (a T·G mismatch, not recognizable as foreign) |
| 8-oxoguanine and other oxidized bases | Reactive oxygen species from respiration | $10^3$ | 8-oxoG pairs with A: G·C → T·A transversion |
| 7-methylguanine, 3-methyladenine, $O^6$-methylguanine | S-adenosylmethionine, alkylating agents | thousands (7-meG), hundreds (3-meA), a few ($O^6$-meG) | 3-meA blocks replication; $O^6$-meG pairs with T: G·C → A·T |
| Cyclobutane pyrimidine dimers, 6–4 photoproducts | Ultraviolet light (UVB) | up to $10^5$ in an exposed skin cell during a day of strong sunlight | Block polymerases; C → T and CC → TT |
| Single-strand breaks | Oxidation, abortive topoisomerase I | $10^4$ | Convert to double-strand breaks at forks |
| Double-strand breaks | Ionizing radiation, collapsed forks, topoisomerase II | $10$–$50$ | Chromosome loss and rearrangement |
| Interstrand cross-links | Aldehydes, cisplatin, nitrogen mustards | $10$ | Block replication and transcription completely |

The numbers are dominated by spontaneous chemistry, not by environmental agents: hydrolysis, oxidation and nonenzymatic methylation are unavoidable consequences of DNA's chemical nature, and their rates in vitro predict the in vivo damage load. Lindahl (1993) called this "the instability and decay of the primary structure of DNA". Of the tens of thousands of daily lesions, fewer than about $1$ in $10^3$–$10^4$ end as mutations; the rest are repaired.

Each repair system deals with a class of lesion, and redundancy is common.

| System | Lesions | Excised | Key enzymes (*E. coli*; human) |
|---|---|---|---|
| Direct reversal | Pyrimidine dimers, $O^6$-meG, 1-meA, 3-meC | nothing | Photolyase (not in placental mammals); MGMT (Ada, Ogt); AlkB (ALKBH2/3) |
| Base excision (BER) | Small base lesions (U, 8-oxoG, 3-meA, hypoxanthine) | $1$ nucleotide (short patch) or $2$–$10$ (long patch) | Glycosylases, AP endonuclease, Pol I; APE1, Pol β, XRCC1–ligase III |
| Nucleotide excision (NER) | Helix-distorting lesions (dimers, bulky adducts) | $12$–$13\,\mathrm{nt}$; $24$–$32\,\mathrm{nt}$ | UvrA, UvrB, UvrC, UvrD; XPC, TFIIH, XPA, XPG, XPF–ERCC1 |
| Mismatch repair (MMR) | Mismatches, small loops from replication | up to about $1\,\mathrm{kb}$ | MutS, MutL, MutH; MSH2–MSH6, MLH1–PMS2, EXO1 |
| Double-strand break repair | Breaks | — | RecBCD, RecA; Ku, DNA-PKcs, ligase IV (NHEJ); MRN, BRCA1/2, RAD51 (HR) |
| Damage tolerance | Lesions at forks | — | Pol IV, Pol V, RecA (SOS); Pol η, Pol κ, REV1, Pol ζ, PCNA ubiquitylation |

![The excision repair pathways compared, each drawn on the same stretch of DNA (damaged strand on top, template strand below). Direct reversal repairs the lesion in place; base-excision repair removes one base and replaces one nucleotide; nucleotide-excision repair cuts the damaged strand on both sides of a helix-distorting lesion and replaces an oligonucleotide (12–13 nt in E. coli, 24–32 nt in humans); mismatch repair degrades the new strand from a strand signal (a hemimethylated GATC in E. coli or a nick in eukaryotes) through the mismatch, up to about a kilobase. In every case except direct reversal, the gap is filled by a DNA polymerase copying the undamaged strand (light blue) and sealed by DNA ligase. Yellow marks show the site of the lesion or wrong base (removed in the excision pathways), triangles the incisions; lengths are not to scale.](./plots/repair-pathways.py)

## 8.2. Direct Reversal and Base-Excision Repair

### 8.2.1. Direct Reversal

The simplest repair undoes the chemical reaction. DNA photolyases bind cyclobutane pyrimidine dimers and use blue light to split them: a folate or deazaflavin antenna absorbs a photon and transfers the energy to a reduced flavin ($\mathrm{FADH^-}$), whose excited state donates an electron to the dimer; the dimer radical anion splits its cyclobutane ring in nanoseconds, and the electron returns to the flavin. Photolyases are found in bacteria, plants and most animals but not in placental mammals, which rely on nucleotide-excision repair for UV damage. $O^6$-methylguanine–DNA methyltransferase (MGMT; Ada and Ogt in *E. coli*) transfers the methyl group from $O^6$-meG to one of its own cysteines; the methylated protein is inactivated and degraded, so each molecule repairs one lesion, a "suicide" reaction that shows how much the cell is willing to spend on genomic integrity. AlkB and its human homologs ALKBH2 and ALKBH3 are α-ketoglutarate- and $\ce{F\mathrm{e}^2+}$-dependent dioxygenases that oxidize the methyl groups of 1-methyladenine and 3-methylcytosine, releasing them as formaldehyde.

### 8.2.2. Base-Excision Repair

**Definition 8.2.1** **Base-excision repair** (BER) removes a damaged or inappropriate base by cleavage of its N-glycosidic bond by a **DNA glycosylase**, leaving an **AP site** (apurinic or apyrimidinic, abasic site); an AP endonuclease then cuts the backbone at the AP site, the deoxyribose phosphate is removed, and a DNA polymerase and ligase restore the strand using the complementary strand as template.

Each glycosylase recognizes one kind of lesion, which it finds by flipping bases out of the helix into a pocket on the enzyme. Uracil–DNA glycosylase (UNG) removes uracil formed by deamination of cytosine or misincorporated as dUMP; OGG1 removes 8-oxoG opposite C, while MUTYH (MutY) removes the A misinserted opposite 8-oxoG; AAG (alkyladenine glycosylase) removes 3-meA and hypoxanthine. In human short-patch BER, APE1 cuts $5'$ of the AP site, Pol β removes the $5'$-deoxyribose phosphate with its lyase activity and inserts one nucleotide, and XRCC1–ligase III seals the nick; in long-patch BER, Pol δ/ε displaces $2$–$10$ nucleotides, which FEN1 removes. PARP1 ([7.2.4](/7.2.4)) binds single-strand breaks and AP-site incisions and marks them with poly(ADP-ribose), recruiting XRCC1.

Uracil–DNA glycosylase explains a puzzle of the central dogma: why DNA contains thymine rather than uracil. Cytosine deaminates spontaneously to uracil; if U were a normal DNA base, a repair enzyme could not distinguish a deaminated C (U opposite G) from a legitimate U (opposite A). With T as the normal base, every U in DNA is a lesion. The exception confirms the logic: 5-methylcytosine deaminates to thymine, which cannot be recognized as foreign. The T·G mismatch is removed by the glycosylases TDG and MBD4, but less efficiently, and CpG dinucleotides, the sites of cytosine methylation, mutate about ten times faster than other dinucleotides; this has depleted CpG from vertebrate genomes to about a quarter of the expected frequency, except in CpG islands ([7.2.15](/7.2.15)).

## 8.3. Nucleotide-Excision Repair

**Definition 8.3.1** **Nucleotide-excision repair** (NER) removes helix-distorting lesions by cutting the damaged strand on both sides of the lesion with an **excinuclease**, releasing an oligonucleotide that contains it; the gap is filled by a DNA polymerase and sealed by ligase.

NER does not recognize specific chemistry but the distortion of the double helix, so it repairs an enormous range of lesions: pyrimidine dimers, 6–4 photoproducts, benzo[a]pyrene–guanine adducts from tobacco smoke, cisplatin adducts. In *E. coli*, a UvrA$_2$UvrB complex scans DNA; at a lesion UvrA leaves and UvrB clamps the damaged strand, UvrC binds and the complex cuts the fourth or fifth phosphodiester bond $3'$ of the lesion and the eighth $5'$ of it, releasing $12$–$13$ nucleotides with the help of helicase II (UvrD). In humans the dual incision cuts about $6$ nucleotides $3'$ and $20$ nucleotides $5'$ of the lesion, releasing $24$–$32$ nucleotides; the two nucleases are XPG ($3'$ cut) and XPF–ERCC1 ($5'$ cut), and the gap is filled by Pol δ, Pol ε or Pol κ with PCNA.

Damage is found in two ways. In global genome NER the XPC complex (with UV-DDB for dimers, which distort the helix only slightly) detects distortions anywhere in the genome.

**Definition 8.3.2** In **transcription-coupled repair** (TCR), a lesion in the transcribed strand of an active gene is detected because it stalls RNA polymerase, which recruits the NER machinery (through CSB and CSA in humans and the translocase Mfd in *E. coli*). Transcribed strands are therefore repaired several times faster than the rest of the genome, which makes sense: lesions in the template strand block the production of RNA and threaten the cell immediately.

In both branches the helicase TFIIH, which is also a general transcription factor ([7.2.13](/7.2.13)), unwinds about $25$–$30$ base pairs around the lesion; its subunit XPD verifies the lesion as it translocates. The dual role of TFIIH explains why some mutations in its subunits cause both repair and transcription defects.

Defects in global NER cause xeroderma pigmentosum (XP), with seven complementation groups XPA–XPG; patients have a more than thousandfold increased risk of sunlight-induced skin cancer. Defects in transcription-coupled repair (CSA, CSB) cause Cockayne syndrome, with sensitivity to sunlight and progressive neurological degeneration but no increase in cancer: in these patients cells with stalled transcription die rather than accumulate mutations.

## 8.4. Mismatch Repair

### 8.4.1. Methyl-Directed Mismatch Repair in *E. coli*

**Definition 8.4.1** **Mismatch repair** (MMR) corrects mispaired bases and small insertion–deletion loops left by replication, by excising a segment of the newly synthesized strand that contains the mismatch and resynthesizing it on the parental strand as template.

MMR must solve a problem that excision repair of damaged bases does not face: in a G·T mismatch neither base is chemically abnormal, and the repair is useful only if it removes the newly made, wrong base. In *E. coli* and related bacteria the strand signal is methylation. Dam methylase methylates the adenine of $5'$-GATC-$3'$ sites, but only some minutes after the fork has passed, so new DNA is transiently hemimethylated: methylated on the parental strand only. MutS, a dimer that clamps onto the DNA at a mismatch (all mismatches except C·C), recruits MutL in an ATP-dependent reaction; MutS–MutL sliding clamps travel along the DNA, and MutL activates the latent endonuclease MutH at the nearest hemimethylated GATC, which nicks the unmethylated strand $5'$ of the G. From the nick, helicase II unwinds toward the mismatch and an exonuclease of the appropriate polarity (exonuclease I, VII or X for a nick $3'$ of the mismatch; RecJ or exonuclease VII for a nick $5'$ of it) degrades the new strand past the mismatch. Pol III fills the gap and ligase seals it. The GATC site can be up to about $1\,\mathrm{kb}$ away, so the correction of one wrong base can cost the resynthesis of a thousand nucleotides.

The repair is directed by the methyl signal, as shown by experiments with artificial heteroduplexes: a mismatch is corrected according to the methylated strand when the DNA is hemimethylated, is repaired randomly when neither strand is methylated, and is hardly repaired when both are methylated. Dam-deficient and Dam-overproducing strains are both mutators, because in the first every GATC is unmethylated and in the second new strands are methylated too fast.

### 8.4.2. Eukaryotic Mismatch Repair

Eukaryotes have homologs of MutS and MutL but not of MutH or Dam. MutSα (MSH2–MSH6) recognizes base mismatches and one- or two-nucleotide loops; MutSβ (MSH2–MSH3) recognizes larger loops. MutLα (MLH1–PMS2 in humans, MLH1–PMS1 in yeast) has a latent endonuclease that is activated by PCNA. The strand signal is not methylation but the discontinuities of new DNA: the ends of Okazaki fragments on the lagging strand, and on the leading strand the nicks made when RNase H2 removes misincorporated ribonucleotides. PCNA, loaded onto the primer terminus with a fixed orientation, tells MutLα which strand to nick, and EXO1 or strand displacement by Pol δ removes the segment containing the error.

Mismatch repair improves fidelity by a factor of $10^2$–$10^3$ ([7.2.7](/7.2.7#sec-7.7)). Its loss raises mutation rates most strongly in short tandem repeats (microsatellites), where the polymerase slips and forms loops; **microsatellite** instability is the diagnostic signature of MMR-deficient tumors. Inherited heterozygous mutations in *MLH1*, *MSH2*, *MSH6* or *PMS2* cause Lynch syndrome (hereditary nonpolyposis colorectal cancer), the most common inherited colorectal cancer syndrome: loss of the remaining allele in a single cell produces a mutator clone. MMR-deficient tumors carry so many mutations that they display many foreign peptides to the immune system, and since 2017 they have been treated with immune-checkpoint inhibitors regardless of the tissue of origin.

## 8.5. Double-Strand Breaks

A double-strand break leaves no intact complementary strand at the break site. Unrepaired, it causes loss of the acentric chromosome fragment at mitosis; misrepaired, it causes translocations, deletions and the chromosome rearrangements typical of cancer. Two strategies exist: rejoining the ends, and copying the missing information from a homologous duplex.

**Definition 8.5.1** **Nonhomologous end joining** (NHEJ) repairs a double-strand break by ligating the two broken ends directly, after limited processing, without use of a homologous template.

The Ku70–Ku80 heterodimer, a ring that threads onto DNA ends, binds each end within seconds and recruits the kinase DNA-PKcs, which holds the two ends together in a synaptic complex. Incompatible or damaged ends are trimmed by the nuclease Artemis (activated by DNA-PKcs phosphorylation) or filled in by Pol μ or Pol λ, and the complex XRCC4–XLF–DNA ligase IV joins them. NHEJ is fast and available throughout the cell cycle, but it often adds or deletes a few nucleotides at the junction, and when two breaks are present it can join the wrong ends. In mammalian somatic cells it repairs most breaks; by the age of 70 a typical human cell carries some two thousand NHEJ "scars". An alternative, more mutagenic pathway, microhomology-mediated end joining (MMEJ, or alt-EJ), anneals short complementary sequences ($2$–$20\,\mathrm{nt}$) exposed by resection and uses DNA polymerase θ to fill in; it leaves deletions flanked by microhomologies.

Homologous recombination uses the sister chromatid as a template and is therefore accurate; its mechanism is the subject of [7.2.9](/7.2.9). Its first step, resection of the $5'$ ends to expose $3'$ single-stranded tails, decides between the pathways: once resected, ends can no longer be joined by Ku-dependent NHEJ. Resection is initiated by the MRN complex (MRE11–RAD50–NBS1) with CtIP, whose activity requires phosphorylation by CDKs. Resection, and with it homologous recombination, is therefore possible only in S and G2, when a sister chromatid exists; in G1 the protein 53BP1 and its effectors (RIF1, shieldin) protect ends from resection and channel them into NHEJ, while BRCA1 counteracts 53BP1 in S and G2.

Breaks are signaled throughout the nucleus by the DNA damage response. The kinase ATM, activated by MRN at breaks, and ATR, activated by RPA-coated single-stranded DNA at resected ends and stalled forks, phosphorylate hundreds of substrates: the histone variant H2A.X (to γH2A.X, spreading over a megabase around the break; [7.2.4](/7.2.4)), the checkpoint kinases CHK2 and CHK1, and p53, which arrests the cell cycle or triggers apoptosis ([7.3](/7.3)).

## 8.6. Damage Tolerance: Translesion Synthesis and the SOS Response

### 8.6.1. Translesion Synthesis

Lesions that reach a replication fork stall the replicative polymerase. Rather than stop replication, cells use two tolerance strategies: copy across the lesion with a specialized polymerase, or skip it and later copy the information from the sister chromatid (template switching, a recombination process). Both leave the lesion in place, to be repaired later.

**Definition 8.6.1 (Translesion Synthesis)** **Translesion synthesis** (TLS) is the replication of DNA across a lesion that blocks the replicative polymerase, by specialized DNA polymerases with open active sites and no proofreading activity, which insert nucleotides opposite the damaged template base and extend the primer beyond it.

Most TLS polymerases belong to the Y family (bacterial Pol IV and Pol V, eukaryotic Pol η, Pol ι, Pol κ and REV1); the B-family Pol ζ extends from the mismatched or damaged primer terminus. On undamaged DNA they make errors at rates of $10^{-2}$–$10^{-4}$. Mutagenesis depends on the match between lesion and polymerase: Pol η inserts two A residues opposite a thymine–thymine dimer and so bypasses the commonest UV lesion mostly without error, and its loss causes the variant form of xeroderma pigmentosum (XP-V), in which other polymerases bypass the dimers mutagenically. In eukaryotes the switch to TLS is controlled by ubiquitylation of PCNA at lysine 164: monoubiquitylation by RAD6–RAD18 at stalled forks recruits the Y-family polymerases, which bind ubiquitin, and polyubiquitylation channels the fork into template switching.

### 8.6.2. The SOS Response

**Definition 8.6.2 (SOS Response)** The **SOS response** of bacteria is the coordinated induction of about $40$ genes in response to DNA damage. It is controlled by the repressor LexA and by RecA: RecA bound to single-stranded DNA at stalled forks or resected breaks forms an active filament (RecA*) that stimulates the autocatalytic cleavage of LexA, derepressing the genes that LexA represses.

The SOS genes include *uvrA*, *uvrB* and *uvrD* (NER), *recA* and *lexA* themselves, *sulA* (an inhibitor of the cell-division protein FtsZ, which gives time for repair), *dinB* (Pol IV), and *umuD* and *umuC* (Pol V). LexA binds its operators (SOS boxes) with different affinities, and the affinity shapes each gene's response: genes with weak boxes are partly expressed even without damage, are induced only a few fold and stay on until LexA has almost recovered; genes with strong boxes are tightly off, are induced most strongly, but only while LexA is near its minimum, and they shut off first. When the signal builds up gradually, strong-box genes also need LexA to fall further and so are induced later. In vivo the error-free functions (NER, RecA) come first, division arrest follows, and the error-prone polymerase Pol V comes last; the delay of Pol V comes mainly from a second activation step in which RecA* stimulates the cleavage of UmuD to UmuD′, and Pol V is active only as UmuD′$_2$C–RecA–ATP ("Pol V Mut"). When damage is repaired, RecA* disappears, LexA accumulates again, and because *lexA* is itself under LexA control, the system resets rapidly.

![A model of the SOS response (Eq. (8.1)). A: LexA level L (solid) after DNA damage at t = 0; RecA* activity (dashed, scaled to its peak) rises within minutes and decays as the damage is repaired (time constant 40 min). LexA falls to about a fifth of its basal level and then recovers, helped by the derepression of its own gene. B: fold induction of four SOS promoters whose operators differ in affinity K (in units of the basal LexA level), computed as the free-operator fraction 1/(1 + L/K) relative to its basal value; the strongest operators (small K, such as umuDC) give the largest induction. C: the same responses normalized to their maxima: genes with weak operators (large K, such as uvrA) stay induced longest, those with strong operators only around the LexA minimum. Parameters are illustrative.](./plots/sos-response.py)

The model in the figure has two equations. With $L$ the LexA concentration (in units of its basal level), $\gamma$ its loss by growth dilution, $k_{\mathrm{c}}R(t)$ the rate constant of RecA*-stimulated cleavage and $K_L$ the affinity of LexA for its own operator,

$$
\frac{\mathrm{d}L}{\mathrm{d}t} = \frac{\beta}{1 + L/K_L} - \bigl(\gamma + k_{\mathrm{c}}R(t)\bigr)L, \qquad a_i(t) = \frac{1}{1 + L(t)/K_i}, \tag{8.1}
$$
where $a_i$ is the fraction of time the operator of gene $i$ is free. Before damage $L = 1$, so a gene with $K_i = 0.5$ is already active a third of the time and can be induced at most threefold, whereas a gene with $K_i = 0.02$ is active $2\,\%$ of the time and is induced about $1/L$-fold, fivefold when $L$ falls to $0.2$ and up to fiftyfold if LexA is cleared completely, but only during the trough. Graded affinities thus convert a single input, the LexA level, into graded amplitudes and durations; the same design of a regulator with targets of graded affinity, called a single-input module, is a recurring motif of gene networks ([7.9](/7.9)).

## 8.7. Mutagens, Repair and Cancer

### 8.7.1. The Ames Test

Bruce Ames (1970s) used mutation in bacteria as a rapid test for carcinogens. Strains of *Salmonella typhimurium* carrying a mutation in a histidine-biosynthesis gene cannot grow without histidine; a mutagen raises the frequency of reversion mutations that restore the gene, and the number of colonies on histidine-free plates measures its potency. The tester strains are made sensitive: they lack NER (*uvrB*) and part of the lipopolysaccharide coat (so that chemicals enter), and some carry a plasmid with *mucAB*, homologs of *umuDC*, so that lesions are processed mutagenically. Because many carcinogens become reactive only after metabolism (benzo[a]pyrene is converted to an epoxide by cytochrome P450 enzymes), the chemical is incubated with a liver extract. More than $90\,\%$ of known animal carcinogens are mutagenic in the test, and it remains the first screen for new chemicals.

### 8.7.2. Repair Defects and Cancer

Cancer is a disease of mutations in genes that control cell division and death, and defects in repair raise the rate at which such mutations accumulate. Nearly 200 human genes encode repair proteins; inherited defects in many of them cause cancer-predisposition syndromes.

| Syndrome | Defective process (genes) | Main features |
|---|---|---|
| Xeroderma pigmentosum | NER (*XPA*–*XPG*); XP-V: Pol η | Skin cancers on sun-exposed skin, $>1000$-fold risk |
| Cockayne syndrome | Transcription-coupled repair (*CSA*, *CSB*) | Photosensitivity, neurodegeneration, no cancer predisposition |
| Lynch syndrome | MMR (*MLH1*, *MSH2*, *MSH6*, *PMS2*) | Colorectal and endometrial cancer, microsatellite instability |
| Hereditary breast and ovarian cancer | HR (*BRCA1*, *BRCA2*, *PALB2*) | Lifetime breast-cancer risk about $50$–$70\,\%$ |
| Fanconi anemia | Interstrand cross-link repair (about 22 *FANC* genes) | Bone-marrow failure, leukemia, hypersensitivity to cross-linkers |
| Ataxia telangiectasia | Break signaling (*ATM*) | Neurodegeneration, lymphoma, radiosensitivity |
| Bloom syndrome | Dissolution of recombination intermediates (*BLM*) | Sister-chromatid exchanges, many cancers |
| Polymerase proofreading-associated polyposis | Proofreading (*POLE*, *POLD1*) | Colorectal cancer, ultramutated tumors |

The repair defects of tumors are also their weakness. Many anticancer drugs damage DNA (cisplatin cross-links, temozolomide methylates guanine, topoisomerase poisons make breaks; [7.2.3](/7.2.3)), and tumors deficient in the relevant repair are especially sensitive: temozolomide works best against glioblastomas in which the *MGMT* gene is silenced by promoter methylation. A more selective strategy is synthetic lethality: two defects that are each tolerated but lethal together. Cells lacking BRCA1 or BRCA2 depend on PARP-mediated repair of single-strand breaks, because unrepaired single-strand breaks become double-strand breaks at forks, which they cannot repair by recombination; PARP inhibitors (olaparib, approved in 2014) kill BRCA-deficient tumor cells while sparing normal cells, which retain one functional *BRCA* allele. Inhibitors of Pol θ, on which HR-deficient cells also depend, are being developed on the same principle.

## 8.8. From Damage to Mutation: Simple Models

### 8.8.1. Lesion Steady State

If lesions of one kind arise at a constant rate $k_{\mathrm{d}}$ (per genome per unit time) and each is repaired with first-order rate constant $k_{\mathrm{r}}$, the number of lesions $N$ obeys

$$
\frac{\mathrm{d}N}{\mathrm{d}t} = k_{\mathrm{d}} - k_{\mathrm{r}}N, \qquad N(t) = \frac{k_{\mathrm{d}}}{k_{\mathrm{r}}}\bigl(1 - \mathrm{e}^{-k_{\mathrm{r}}t}\bigr) + N(0)\,\mathrm{e}^{-k_{\mathrm{r}}t}, \tag{8.2}
$$
an **ordinary differential equation** whose steady state $N^* = k_{\mathrm{d}}/k_{\mathrm{r}} = k_{\mathrm{d}}\,t_{1/2}/\ln 2$ is reached in a few half-lives. A replication fork passing through the genome meets, on average, all $N^*$ lesions present at the time it arrives. If a fraction $p$ of the lesions met by forks is converted into mutations, the mutation rate per genome per replication is $\mu = pN^*$.

**Example 8.8.1** AP sites arise at about $10^4$ per human cell per day. With a repair half-life of about $2\,\mathrm{h}$, $k_{\mathrm{r}} = \ln 2/(2\,\mathrm{h}) \approx 8.3\,\mathrm{d^{-1}}$ and $N^* \approx 10^4/8.3 \approx 1200$ AP sites per genome at any time. If even $1\,\%$ of the AP sites met by forks gave a mutation, that would be $12$ mutations per S phase, more than the error rate of replication ($6.2\times10^9\times10^{-10} \approx 0.6$ per division). The steady state is therefore sensitive to the repair rate: halving the repair half-life halves $N^*$, and a repair-deficient cell, with $t_{1/2}$ ten times longer, has ten times more lesions waiting for the fork. Cells also slow the fork and activate repair when lesions are frequent (8.5, 8.6), which keeps the effective $p$ small.

![From damage to mutation. A: lesion number for a constant damage rate of 10⁴ lesions per genome per day and repair half-lives of 1, 2 and 8 hours (Eq. (8.2)); the steady state is proportional to the half-life. B: de novo mutations in a child as a function of parental age at conception, approximate linear fits to whole-genome data from Icelandic parent–child trios (Jónsson et al. 2017): about 1.5 additional paternal mutations and 0.4 additional maternal mutations per year of age. The paternal slope reflects both the continuing divisions of spermatogonial stem cells and damage accumulating over time; the maternal slope, in oocytes that do not divide after birth, can only reflect damage. C: somatic mutations in adult human stem cells of colon, small intestine and liver increase linearly with age at about 40 per genome per year in all three tissues (Blokzijl et al. 2016), although the tissues divide at very different rates.](./plots/mutation-accumulation.py)

### 8.8.2. Mutations Accumulate as a Clock

Whole-genome sequencing of single cells, clones and families has turned these estimates into measurements. Germline mutations accumulate with parental age, faster in fathers than in mothers; somatic mutations accumulate linearly with age in every tissue examined. Two features of the data show that damage, not only replication errors, drives mutation. Oocytes, which do not divide after birth, still accumulate mutations with maternal age. And adult stem cells of the colon and the liver, which divide at very different rates, accumulate mutations at nearly the same rate per year. The spectrum of somatic mutations also carries the signatures of their causes: C → T at CpG from deamination of 5-methylcytosine (a "clock-like" signature that increases steadily with age), C → T at dipyrimidines from UV in skin, G → T from tobacco adducts in lung, and characteristic patterns of insertions and deletions in MMR-deficient cells. Reading these mutational signatures from tumor genomes has become a way of inferring which damage and which repair defects shaped each cancer.

## Summary

| Topic | Key points |
|---|---|
| Damage (Definition 8.1.1) | Tens of thousands of lesions per human cell per day, mostly spontaneous: depurination ($10^4$), deamination of C and 5mC, oxidation (8-oxoG), methylation; UV dimers; single- and double-strand breaks ($10^4$, $10$–$50$); lesions become mutations only through replication or misrepair; transitions, transversions, indels |
| Direct reversal | Photolyase (light, $\mathrm{FADH^-}$, not in placental mammals); MGMT (suicide methyl transfer); AlkB (oxidative demethylation) |
| BER (Definition 8.2.1) | Glycosylase (base flipping) → AP site → APE1 → Pol β (one nucleotide) → XRCC1–ligase III; UNG explains T instead of U in DNA; 5mC deamination makes CpG hotspots |
| NER (Definition 8.3.1) | Distortion sensing; excinuclease cuts on both sides: $12$–$13\,\mathrm{nt}$ (UvrABC) or $24$–$32\,\mathrm{nt}$ (XPG, XPF–ERCC1); TFIIH opens; global (XPC) and transcription-coupled (CSB, Mfd; Definition 8.3.2); XP and Cockayne syndrome |
| MMR (Definition 8.4.1) | MutS recognizes, MutL couples, MutH nicks unmethylated GATC on hemimethylated DNA, up to $1\,\mathrm{kb}$ away; eukaryotes: MutSα/β, MutLα endonuclease activated by PCNA, strand signal from nicks; $10^2$–$10^3$ fidelity; microsatellite instability, Lynch syndrome |
| Double-strand breaks | NHEJ (Definition 8.5.1): Ku, DNA-PKcs, Artemis, XRCC4–XLF–ligase IV, error-prone, all phases; MMEJ with Pol θ; HR requires resection by MRN–CtIP (CDK-dependent, S/G2), 53BP1 vs BRCA1; ATM, ATR, γH2A.X, p53 |
| Tolerance | TLS (Definition 8.6.1) by Y-family polymerases, Pol η accurate on T–T dimers; PCNA mono- vs polyubiquitylation; SOS (Definition 8.6.2): RecA* → LexA cleavage → about 40 genes in order of operator affinity, Eq. (8.1); UmuD′$_2$C Pol V last |
| Cancer | Ames test (his⁻ *Salmonella*, liver extract, $> 90\,\%$ of carcinogens); repair syndromes (table in 8.7.2); MGMT silencing and temozolomide; PARP inhibitors and synthetic lethality with BRCA deficiency; checkpoint inhibitors for MMR-deficient tumors |
| Models | $N^* = k_{\mathrm{d}}/k_{\mathrm{r}}$ (Eq. (8.2), Example 8.8.1); germline mutations grow with parental age (paternal about $1.5$, maternal about $0.4$ per year); somatic mutations about $40$ per year in adult stem cells; mutational signatures |

## Questions

1. Explain why a deficiency in uracil–DNA glycosylase increases the frequency of G·C → A·T transitions, and why the same transition is frequent at CpG sites even in cells with normal glycosylase activity.

   **Answer** Deamination of cytosine produces uracil opposite guanine. Normally UNG removes it and BER restores C. Without UNG the U persists, and at the next replication it templates an A, so one daughter has U·A and, after the U is copied again, T·A: a G·C → A·T transition. At CpG sites the cytosine is often methylated, and deamination of 5-methylcytosine gives thymine, a normal base. The resulting T·G mismatch can only be repaired by the slower, mismatch-specific glycosylases TDG and MBD4, and a mismatch-repair system cannot tell which base is wrong. Many such mismatches survive to replication, which makes CpG the most mutable dinucleotide in vertebrate genomes.

2. A mismatch is introduced into a plasmid at a known position $300\,\mathrm{bp}$ from the only GATC site. Predict the outcome of repair in *E. coli* if the plasmid is (a) hemimethylated, methyl group on the strand carrying the correct base; (b) hemimethylated with the methyl group on the other strand; (c) unmethylated; (d) fully methylated.

   **Answer** (a) MutH nicks the unmethylated strand, which carries the wrong base, and the excision removes it: the correct sequence is restored. (b) The strand with the correct base is unmethylated and is "corrected" to match the wrong one: a mutation is fixed. (c) MutH can nick either strand; repair occurs but favors neither, so about half of the plasmids end with each sequence. (d) MutH cannot nick fully methylated GATC; the mismatch is mostly not repaired and is resolved by replication, giving two different daughter plasmids.

3. Patients with Cockayne syndrome and patients with xeroderma pigmentosum are both hypersensitive to sunlight, but only XP patients have a high risk of skin cancer. Explain.

   **Answer** In XP, global genome NER is defective: lesions persist throughout the genome, cells survive, and replication across unrepaired dimers (by error-prone polymerases) produces mutations, including in oncogenes and tumor suppressor genes, hence cancer. In Cockayne syndrome only transcription-coupled repair is defective: global repair still removes most lesions, but RNA polymerases stalled at lesions in transcribed strands are not relieved. Cells with blocked transcription undergo apoptosis or senescence, which causes the photosensitivity and the degeneration of long-lived cells such as neurons, but does not generate a mutator population.

4. Using Eq. (8.1), show that with constant cleavage $k_{\mathrm{c}}R$ the steady-state LexA level falls with increasing damage and that negative autoregulation of *lexA* makes this fall smaller than it would be with constitutive synthesis. Why might autoregulation be advantageous?

   **Answer** At steady state $\beta/(1 + L/K_L) = (\gamma + k_{\mathrm{c}}R)L$. The right side increases with $L$ and with $R$, the left side decreases with $L$, so the intersection moves to smaller $L$ as $R$ increases. With constitutive synthesis $\beta'$ (chosen to give the same basal level), $L = \beta'/(\gamma + k_{\mathrm{c}}R)$ falls in inverse proportion to the total loss rate. With autoregulation, a fall of $L$ increases synthesis, partly compensating: the steady-state level is buffered, and the system responds less to small, transient increases of RecA* (fewer false alarms). Autoregulation also speeds the return of LexA after the damage is repaired, because synthesis is maximal while $L$ is low, and so shortens the period in which error-prone Pol V is expressed.

5. Why are PARP inhibitors toxic to BRCA2-deficient cells but not to cells heterozygous for a *BRCA2* mutation, such as the normal cells of a carrier? Suggest two mechanisms of resistance that tumors could evolve.

   **Answer** PARP inhibitors trap PARP1 on single-strand breaks and prevent their repair; at the next S phase these lesions block or collapse replication forks, generating one-ended double-strand breaks that require homologous recombination. Cells with one functional *BRCA2* allele perform HR and survive; tumor cells that have lost the second allele cannot, and die (synthetic lethality). Tumors become resistant by restoring HR, for example through secondary mutations that restore the *BRCA2* reading frame, or by losing 53BP1 or shieldin, which allows resection and partial HR even without BRCA1; they can also lose PARP1 expression or pump the drug out.

6. (Open question) Germline mutations increase with paternal age by about $1.5$ per year, and with maternal age by about $0.4$ per year. Spermatogonial stem cells divide about every $16$ days throughout adult life, oocytes not at all. Using the replication error rate of $10^{-10}$ per base pair, estimate how many of the paternal mutations per year could be due to replication errors, and discuss what the comparison implies.

   **Answer** At one division per $16$ days there are about $23$ divisions per year. Each division replicates $6.2\times10^9\,\mathrm{bp}$ with about $10^{-10}$ errors per base pair, about $0.6$ errors per division, so about $14$ errors per year, ten times more than the observed paternal increase. The estimate shows that the per-base-pair rate in spermatogonia must be lower than $10^{-10}$, or that most divisions do not contribute to the sampled lineage. Conversely, the maternal slope, with no divisions at all, shows that time-dependent damage alone contributes a substantial fraction. The ratio of paternal to maternal mutations (about $4:1$) is much smaller than the ratio of germline divisions (about $10:1$ or more at typical ages), which points the same way: many germline mutations arise from damage rather than from replication errors. This is an active research question; mutational signatures in the two sexes are used to separate the contributions.
