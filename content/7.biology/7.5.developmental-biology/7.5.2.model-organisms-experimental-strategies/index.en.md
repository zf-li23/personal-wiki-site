---
title: Model Organisms and Experimental Strategies
description: "How developmental biology is done: what makes a good model organism for embryology; C. elegans, Drosophila, zebrafish, killifish, Xenopus, chick, mouse, minipig and marmoset compared, with plants and non-traditional animals; fate maps and lineage tracing from vital dyes and quail–chick chimeras to inducible Cre-loxP, multicolour reporters and CRISPR barcodes, with the birthday-problem estimate of label collisions; single-cell omics; detecting gene expression; forward and reverse genetics and the logic of loss and gain of function (necessity, sufficiency, morpholinos and their pitfalls); embryos, explants and organs in culture; and a timetable of human development with the Carnegie stages."
---

The questions of the previous chapter are answered with a small number of species and a small number of experimental designs. This chapter describes both. It first compares the **model organisms** of developmental biology, which are chosen less for their genetics (as in [7.4.1](/7.4.1#sec-1.3)) than for the accessibility of their embryos. It then describes the methods by which embryologists follow cells (fate maps and lineage tracing), read out gene activity (expression analysis and single-cell omics) and test what a gene does (loss and gain of function), and the experimental systems outside the body (explants, embryo and organ culture). It ends with a timetable of human development, the reference against which the model organisms are compared throughout the course. The general methods of cell biology ([7.3.2](/7.3.2), [7.3.3](/7.3.3)) and of genome manipulation ([7.4.19](/7.4.19), [7.2.24](/7.2.24)) are assumed.

## 2.1. What Makes a Good Model Organism for Development

A **model organism** ([7.3.1](/7.3.1)) is a species studied intensively in the expectation that what is learned from it applies to others; in its narrow sense, a genetically uniform strain whose results can be compared between laboratories. For developmental biology the useful properties are:

- a short life cycle, small size and easy husbandry;
- many embryos, available at a known time;
- embryos that can be seen and manipulated: external development, transparency, large size, tolerance of surgery and injection;
- genetic uniformity (inbred lines) and genetic tools; since **genome editing**, this last requirement has almost ceased to be a limitation.

No species has all of these, and each answers some questions well and others badly. Results from different models are then combined: a mechanism found in one species is tested in others, and what is shared reveals general principles, while what differs reveals how development evolves.

## 2.2. Invertebrate Models

*Caenorhabditis elegans*, a free-living nematode about 1 mm long, can be frozen and revived, completes its life cycle in about 3–3.5 days at $20\,^\circ\mathrm{C}$ and lives 2–3 weeks. It exists as self-fertilizing hermaphrodites and as males. Its body is transparent and its cell number fixed (959 somatic nuclei in the adult hermaphrodite), and every division from zygote to adult has been followed under the microscope, so the complete **cell lineage** is known (Sulston and colleagues, 1977–1983). Genes can be knocked down simply by feeding worms bacteria that express double-stranded RNA (**RNA interference**). Work on *C. elegans* earned the Nobel Prize in 2002 (Brenner, Horvitz, Sulston: organ development and programmed cell death) and 2006 (Fire, Mello: RNA interference). Its main limitation is its distance from vertebrates: it lacks many vertebrate cell types and organs, and its development is highly stereotyped.

*Drosophila melanogaster* is small and cheap, lays many eggs that develop outside the mother and can be observed easily, and goes from egg to fertile adult in about 10 days at $25\,^\circ\mathrm{C}$; adults live a few weeks. Its genetics is the most developed of any animal: high-throughput mutant screens, **balancer chromosomes**, the induction of mutant clones in otherwise normal animals by **mitotic recombination**, and the **GAL4/UAS system** for expressing genes in chosen cells ([7.4.19](/7.4.19)). Nobel Prizes went to Morgan (1933, the chromosome theory), Muller (1946, mutagenesis by X-rays) and Lewis, Nüsslein-Volhard and Wieschaus (1995, the genetic control of early embryonic development). The fly too is far from vertebrates, and its early embryo is a syncytium, an unusual way of patterning (7.5.14).

## 2.3. Vertebrate Models

| Species | Strengths | Limitations |
|---|---|---|
| Zebrafish, *Danio rerio* | small, cheap; about 200 eggs per clutch; fertile at about 3 months, lives 3–5 years; external fertilization and development; transparent embryos for live imaging; large mutagenesis screens, transgenesis, gene knockout | no maternal–embryonic interaction (no placenta); laboratory strains lack sex chromosomes, sex is set by several genes and the environment, and **germ cells** are needed to maintain females, so it is a poor model of **sex determination**; a genome duplication in the teleost ancestor left many genes in two copies |
| African turquoise killifish, *Nothobranchius furzeri* | embryos can enter diapause, so lines can be stored as embryos; sexual maturity in a few weeks; the shortest-lived vertebrate kept in the laboratory (median lifespan of a few months in the GRZ strain) | a young model with few genetic resources; used mainly for aging (7.5.37) |
| African clawed frog, *Xenopus laevis* | many eggs, external development; large eggs (about 1.2 mm) that tolerate surgery and microinjection; axes predictable from the egg; the animal cap assay for induction (7.5.16); oocytes as an expression system | allotetraploid and fertile only after 1–2 years, hence poor for genetics; *Xenopus tropicalis*, a diploid with a generation time of about 5 months, is used for genetics but has smaller embryos |
| Chicken, *Gallus gallus* | many eggs; the embryo develops outside the mother and can be operated on through a window in the shell; grafting, quail–chick **chimeras**, electroporation of DNA into chosen tissues | the first day of development occurs in the oviduct before laying; germ-line genetics is slow |
| Mouse, *Mus musculus* | a mammal whose development resembles that of humans; relatively prolific; many cell lines and antibodies; embryonic stem cells, knockouts and conditional knockouts; large genetic resources | embryos develop inside the mother and are hard to observe; some aspects of physiology and behaviour differ from humans; the early mouse embryo (cylindrical epiblast) has a shape unlike that of most mammals |
| Minipig, *Sus scrofa* | small breeds (below about 40 kg); litters of 6–10; sexually mature at about 6 months, gestation about 114 days; organ anatomy and metabolism close to human; potential donors for xenotransplantation | expensive to keep; long generation time compared with rodents |
| Common marmoset, *Callithrix jacchus* | a small primate (body 19–25 cm, 300–450 g); mature at about 14 months, gestation about 145–150 days, usually twins; physiology, brain and social behaviour closer to human, so disease models are more informative | no inbred lines; few genetic resources; twins exchange blood stem cells in utero, so they are hematopoietic chimeras |

The frog was the classical object of experimental embryology: Spemann's organizer (Nobel Prize 1935) and Gurdon's nuclear transfer (Nobel Prize 2012, shared with Yamanaka) were both done on amphibians, and the large *Xenopus* oocyte was used to express and study membrane channels (Nobel Prize in Chemistry 2003 to Agre and MacKinnon). The mouse is the genetic model of mammals: **gene targeting** in embryonic stem cells earned the Nobel Prize in 2007 (Capecchi, Evans, Smithies), and the reprogramming of mouse fibroblasts to pluripotency the prize of 2012.

![Model organisms of developmental biology. Left: their relationships (a cladogram after current phylogenomic analyses; branch lengths not to scale), with protostomes (orange) and vertebrates (blue) shaded. Right: typical laboratory generation times, egg to egg, on a logarithmic scale; they range over more than three orders of magnitude, from 3.5 days for *C. elegans* to about 25 years for humans. Planarians are propagated mostly by fission and the generation time of *Nematostella* depends on culture conditions](./plots/model-organisms.py)

## 2.4. Plants and Non-Traditional Models

*Arabidopsis thaliana* is the model of flowering plants: small, quick to cycle, self-fertilizing and genetically tractable; rice is the model of monocot crops, with a cycle of 3–5 months, natural self-fertilization (so **near-isogenic lines** are easy to make) and a direct connection between basic research and breeding. Plant development is treated in [7.12](/7.12).

Special phenomena need special animals, and genomics and genome editing have made many of them accessible:

| Animal | Why it is studied |
|---|---|
| sea anemone *Nematostella vectensis* (a cnidarian) | the sister group of bilaterians: the origin of axes and germ layers |
| planarian *Schmidtea mediterranea* | whole-body regeneration from pluripotent stem cells (7.5.35) |
| acoel worm *Hofstenia miamia* | regeneration in a deep-branching bilaterian |
| choanoflagellate *Salpingoeca rosetta* | a unicellular relative of animals that forms colonies: the origin of multicellularity |
| tardigrades | survival of desiccation, freezing and radiation |

## 2.5. Fate Maps and Lineage Tracing

**Definition 2.5.1 (Fate Map and Cell Lineage)** A **fate map** of an embryo at a given stage is a map of what the cells of each region will become in normal development. The **cell lineage** of a cell is the pattern of divisions by which it arose from the zygote and gave rise to its descendants, together with the fates of those descendants.

**Definition 2.5.2 (Lineage Tracing)** **Lineage tracing** is the experimental identification of all the progeny of a single cell or group of cells, by marking the cell so that the mark is passed to all its descendants and to no other cells.

A fate map can be built by marking regions and seeing where their descendants end up; a lineage requires marking single cells. A fate map describes normal development only: it says nothing about what cells could become under other conditions, which is tested by isolation and grafting (7.5.1).

![A fate map of the late blastula of *Xenopus laevis* (lateral view, animal pole up, dorsal side right). The animal half will form ectoderm: epidermis ventrally and the neural plate dorsally. The marginal zone forms mesoderm: notochord dorsally, beneath the future dorsal lip of the blastopore, then somites, and lateral plate and blood ventrally. The vegetal half forms endoderm. The map records normal fates, not potency](./plots/xenopus-fate-map.py)

The methods have changed greatly:

1. Direct observation. In embryos with few, visible cells, lineages can simply be watched: Edwin Conklin followed the tunicate *Styela* in 1905, and the complete *C. elegans* lineage was recorded by **differential interference contrast microscopy**. Modern **light-sheet microscopy** follows every nucleus of a zebrafish or mouse embryo for hours or days.
2. Dye marking. Walther Vogt (1929) applied agar chips soaked in vital dyes (Nile blue, neutral red) to the surface of amphibian embryos and followed the stained patches through **gastrulation**; this gave the first amphibian fate maps. Vital dyes dilute with each division and diffuse, so they mark regions rather than cells. Fluorescent dextrans (which cannot cross membranes) or lipophilic dyes such as DiI injected into a single cell label that cell's clone (a lineage tracer).
3. Interspecies chimeras. Nicole Le Douarin (1969) noticed that quail cells have a large mass of heterochromatin in the nucleolus, which chick cells lack; quail tissue grafted into a chick embryo integrates and develops normally, and its descendants can be identified later, today with a quail-specific antibody. Quail–chick **chimeras** ([7.4.19](/7.4.19)) mapped the migration and derivatives of the **neural crest** (7.5.20) and the origins of blood and germ cells. Genetically marked grafts (from transgenic animals expressing **green fluorescent protein**) serve the same purpose within a species.
4. Genetic labelling. A recombinase expressed in a chosen cell type switches on a reporter permanently. In the standard design, a Cre-expressing line is crossed to a reporter line in which a strong ubiquitous promoter (often at the *Rosa26* locus) is separated from a fluorescent protein gene by a stop cassette flanked by loxP sites; when Cre excises the stop cassette in a cell, that cell and all its descendants express the reporter, whatever they later become (**conditional knockout**, [7.3.3](/7.3.3)). Fusing Cre to a mutated estrogen receptor (CreER) makes it enter the nucleus only after a dose of tamoxifen, which sets the time of labelling, and a low dose labels single, well-separated cells, whose clones can then be followed. Multicolour reporters (Brainbow, Confetti) contain several pairs of incompatible lox sites, so that Cre chooses randomly among three or four fluorescent proteins and neighbouring clones receive different colours.
5. DNA barcodes. A cell can be given a heritable DNA sequence that differs from cell to cell: random sequences delivered by viruses or transposons, or an array of CRISPR target sites that **CRISPR–Cas9** edits progressively, each edit adding a random insertion or deletion. Because edits accumulate over successive divisions and are never reversed, cells that share an edit descend from the cell in which it occurred, and the pattern of shared edits reconstructs the lineage tree (McKenna and colleagues, 2016, in zebrafish). Read by single-cell RNA sequencing, the barcode and the **transcriptome** of the same cell give lineage and cell type together.
6. Natural barcodes. In humans, where nothing can be introduced, **somatic mutations** and **mitochondrial DNA** variants that arise during development serve as markers, and the lineage is reconstructed retrospectively from sequencing.

![Lineage tracing methods. A: a lineage tracer injected into one blastomere is inherited by its clone. B: a quail graft in a chick embryo; quail nuclei are recognized by their condensed nucleolar heterochromatin. C: inducible genetic labelling: a cell-type-specific promoter drives CreER; after tamoxifen, Cre excises the loxP-flanked stop cassette upstream of a reporter at the Rosa26 locus, labelling the cell and all its descendants permanently. D: CRISPR barcodes: an array of target sites accumulates edits (coloured) over successive divisions; shared edits mark common ancestors](./plots/lineage-tracing.py)

### 2.5.1. How Many Labels Are Needed

A label identifies a clone only if no other clone carries the same label. If $n$ clones are labelled independently, each with one of $N$ equally likely labels, the probability that at least two share a label is the birthday problem of probability theory ([Example 1.4.1](/3.1.1#ex-1.4.1)).

**Formula 2.5.1 (Label Collisions)** For $n$ independently labelled clones, each label drawn with probability $p_i$ from a set of labels,

$$
\mathbb{P}(\text{some two clones share a label}) \approx 1 - \exp\Bigl[-\frac{n(n-1)}{2N_{\mathrm{eff}}}\Bigr], \qquad N_{\mathrm{eff}} = \frac{1}{\sum_i p_i^2},
\tag{2.1}
$$
which is exact to first order in $n^2/N_{\mathrm{eff}}$; for $N$ equally likely labels $N_{\mathrm{eff}} = N$, and the exact value is $1-\prod_{k=1}^{n-1}(1-k/N)$.

**Proof** For a given pair of clones the probability of the same label is $\sum_i p_i^2 = 1/N_{\mathrm{eff}}$. There are $n(n-1)/2$ pairs; when collisions are rare they are approximately independent rare events, so the number of colliding pairs is approximately Poisson with mean $n(n-1)/(2N_{\mathrm{eff}})$ (**Poisson distribution**, [3.1.3](/3.1.3)), and the probability of at least one is one minus the probability of none. $\square$

The probability reaches one half when $n \approx 1.18\sqrt{N_{\mathrm{eff}}}$. Three practical consequences follow.

**Example 2.5.1** A four-colour Confetti reporter has $N \le 4$: with only three labelled clones, two share a colour with probability $1 - (3/4)(2/4) = 0.625$. Colour alone therefore cannot distinguish clones; it works only together with sparse labelling, so that clones of the same colour are too far apart to be confused. A random barcode library with $10^6$ equally represented sequences labels a thousand clones with a probability of a collision of about $1 - \mathrm{e}^{-0.5} \approx 0.39$, but the expected number of shared barcodes is only $0.5$, a negligible error. A CRISPR array whose $10^4$ possible outcomes occur with Zipf-like frequencies ($p_i \propto 1/i$; some edits are far more frequent than others) has $N_{\mathrm{eff}} \approx 58$: with only ten clones, collisions are already more likely than not. This is why frequent edits are discounted when trees are built and why recorders with many independent target sites are used.

![The birthday problem of lineage tracing. A: the probability that at least two of n labelled clones carry the same label, for N equally likely labels: 4 (a Confetti reporter), 100, 10⁴ and 10⁶; the probability passes 50 % (dashed line) near n = 1.18√N. B: with unequal label frequencies the effective number of labels N_eff = 1/Σp² matters; for 10⁴ barcodes with Zipf-distributed frequencies N_eff ≈ 58, and collisions become likely with about ten clones (solid), compared with the uniform case (dashed)](./plots/barcode-collision.py)

## 2.6. Single-Cell Omics

Single-cell RNA sequencing measures the transcriptomes of thousands to millions of individual cells. Applied to whole embryos at successive stages, it has produced atlases of zebrafish, *Xenopus*, mouse and human development in which every cell type and its transitional states can be found; ordering cells by the similarity of their transcriptomes (pseudotime) suggests differentiation trajectories, and the ratio of unspliced to spliced transcripts (RNA velocity) suggests the direction of change. Related methods measure chromatin accessibility or DNA methylation in single cells, and spatial transcriptomics measures expression in tissue sections without dissociation. These methods give a great deal of information, but:

- they are technically demanding and expensive, and the integration of data sets from different experiments is difficult;
- reproducibility between experiments is limited, and rare cells may be missed;
- some solid tissues are hard to dissociate into intact single cells, and dissociation itself changes gene expression;
- each cell is measured once, so trajectories are inferred, not observed; similar transcriptomes do not prove descent, which only lineage tracing (Section 2.5) shows;
- spatial position is lost unless measured separately.

The analysis of such data is treated in [7.8](/7.8).

## 2.7. Detecting Gene Expression

| What is detected | Methods | What they tell |
|---|---|---|
| RNA in extracts | Northern blot, dot blot, RT-PCR and quantitative PCR, microarrays, bulk RNA sequencing | which transcripts and how much, in a tissue or stage |
| RNA in single cells | single-cell RNA sequencing | which genes, cell by cell, without position |
| RNA in place | whole-mount in situ hybridization with labelled antisense probes; **fluorescence in situ hybridization** with amplification (hybridization chain reaction) and single-molecule FISH; spatial transcriptomics | where and when a gene is transcribed; single-molecule methods count transcripts |
| RNA in living embryos | tagged RNAs (MS2 stem loops bound by fluorescent coat protein) | the timing of transcription in real time |
| Protein | Western blot; immunostaining (immunofluorescence); fluorescent protein tags and knock-in reporters | which proteins, where, and (in living embryos) how they move |

Expression is evidence of where a gene could act, not of what it does: a gene expressed in a tissue may have no function there, and a gene may act in cells other than those in which its mRNA is found (secreted proteins, maternal products). Function is tested by perturbation.

## 2.8. Testing Gene Function

### 2.8.1. Forward and Reverse Genetics

**Forward genetics** goes from phenotype to gene: one collects spontaneous mutants or induces mutations at random, screens for animals with altered development, and identifies the mutated genes. **Reverse genetics** goes from gene to phenotype: one starts from a gene, perhaps chosen for its expression pattern or its similarity to a gene of known function, and alters it to see what happens ([7.4.1](/7.4.1#sec-1.2)). Forward screens are unbiased and found the patterning genes of *Drosophila* and zebrafish ([7.4.20](/7.4.20)); **reverse genetics** became general with gene targeting and genome editing.

### 2.8.2. Loss and Gain of Function

The two basic perturbations answer two different questions. A **loss-of-function mutation** or knockdown shows whether a gene is necessary for a process; a **gain-of-function mutation**, overexpression, or expression at the wrong place or time shows whether it is sufficient, in that context, to drive the process.

| Loss of function: necessity | Gain of function: sufficiency |
|---|---|
| natural mutants and patients | injection of mRNA or protein |
| random mutagenesis and screens | transgenic overexpression |
| gene knockout and genome editing | ectopic expression with GAL4/UAS or tissue-specific promoters |
| tissue-specific (conditional) knockout | modification of enhancers or promoters (for example, to change where a gene is expressed) |
| knockdown of RNA (RNA interference, morpholinos) or protein (**degron** tags) | grafts of signalling cells or beads soaked in protein |

In embryology the same logic is often summarized as "find it, lose it, move it": a candidate is found where and when it should act (expression), its removal must prevent the process (necessity), and its presence in a new place must cause the process there (sufficiency). An inductive signal is identified only when all three hold; the dorsal-lip graft of Spemann and Mangold (7.5.1) was a "move it" experiment for the organizer, and the identification of the organizer's secreted molecules (7.5.16) required all three for each of them.

**Definition 2.8.1 (Morpholino)** A *morpholino* (morpholino oligonucleotide) is a synthetic antisense oligomer of about 25 bases with a morpholine-ring backbone that binds complementary RNA without causing its degradation and blocks either translation (when it covers the start codon) or splicing (when it covers a splice junction). Injected into an egg or early embryo, it reduces the function of a gene for a few days.

Interpreting these experiments requires care:

- Specificity. Morpholinos can be toxic and act on unintended RNAs (activation of p53 is a common non-specific effect); a morphant phenotype must be confirmed by a second, independent morpholino, by rescue with an mRNA the morpholino cannot bind, and by a mutant. Discrepancies between morphants and mutants may also reflect **genetic compensation** in the mutant (Definition 1.8.1).
- Redundancy. Related genes may substitute for each other (**genetic redundancy**), so a single mutant can be normal while the double mutant has a phenotype.
- Maternal contribution. A zygotic mutant may develop normally because the egg contains mRNA and protein from the mother; removing these requires maternal–zygotic mutants, made from homozygous mutant mothers (**maternal-effect gene**, [7.4.20](/7.4.20)).
- Early requirement. A gene needed early may mask later functions, because mutants die before the later stage; conditional or temporally induced knockouts reveal the later roles.
- Autonomy. Whether a gene acts in the cells that show the defect or in their neighbours is tested with mosaics, in which mutant and normal cells lie side by side (**cell autonomy**, [7.4.20](/7.4.20#sec-20.4.2)).
- Sufficiency is context-dependent. Overexpression shows what a gene can do in cells that are competent to respond, at concentrations that may be unphysiological; a negative result may only show that the cells were not competent.

**Example 2.8.1 (Designing a Test of an Inductive Signal)** To test whether a secreted factor F made by tissue A induces gene Y in neighbouring tissue B: (find) show that F is expressed in A just before Y appears in B, and that B has receptors for F; (lose) in a mutant lacking F, or with an inhibitor of its receptor, or after removing A, Y should not be expressed; restoring F (a bead soaked in F protein in place of A) should rescue Y; (move) a bead with F, or cells expressing F, placed next to B at an ectopic position, or added to explants of B in culture, should induce Y; and the response should require the receptor in B (a mosaic of B cells lacking the receptor should not respond, showing direct action on B).

## 2.9. Embryos, Explants and Organs in Culture

Development can often be studied outside the body, where tissues can be combined, separated and exposed to defined molecules:

- Explants of embryonic tissue. The animal cap of the *Xenopus* **blastula**, the roof of the **blastocoel**, forms only epidermis when cultured alone but forms **mesoderm** when exposed to inducing molecules, and it became the standard assay for inducing factors (7.5.16). Explant recombinations of two tissues (for example epithelium and mesenchyme of an organ rudiment) reveal which instructs which.
- Whole-embryo culture. Mouse embryos can be cultured from the **blastocyst** through **implantation** stages on a substrate, and post-implantation embryos in rotating bottles with controlled oxygen, now from before gastrulation until early organogenesis (about embryonic day 11), which makes live imaging and manipulation possible. Monkey embryos have been cultured through gastrulation.
- Organ culture. Embryonic organ rudiments (kidney, lung, tooth, gut) grow and branch in culture on filters or in gels, and recombination of their components across a filter showed that induction can occur without cell contact (Grobstein, 1950s).
- Injury models in adults: partial removal of the ventricle (zebrafish heart regeneration), nerve crush and muscle injury models (7.5.35).
- Stem-cell-based models: **organoids** and embryo models made from pluripotent stem cells (7.5.36).

## 2.10. A Timetable of Human Development

Human embryos are studied through donated material, imaging and, increasingly, stem-cell models, within ethical limits (embryos may not be cultured beyond 14 days or the appearance of the **primitive streak** in most jurisdictions; 7.5.36). The embryonic period, the first eight weeks after fertilization, is divided into 23 Carnegie stages defined by morphology rather than age; the fetal period follows until birth at about 38 weeks after fertilization (40 weeks of gestational age, which is counted from the last menstrual period).

| Time after fertilization | Carnegie stage | Event |
|---|---|---|
| day 1 | CS1 | zygote; first cleavage at about 24–30 h |
| days 3–4 | CS2 | morula; the zygotic genome becomes fully active at the 4–8-cell stage (7.5.5) |
| days 4–5 | CS3 | blastocyst: inner cell mass and trophectoderm |
| days 6–7 | CS4–5 | hatching from the zona pellucida; implantation begins |
| week 2 | CS5 | bilaminar disc (epiblast and hypoblast); amniotic cavity |
| days 14–15 | CS6 | primitive streak; gastrulation in week 3 (7.5.9) |
| days 18–19 | CS7–8 | neural plate |
| day 20 | CS9 | first somites |
| days 21–22 | CS10 | the heart tube begins to beat; neural folds begin to fuse |
| days 24–26 | CS11 | anterior neuropore closes |
| days 26–28 | CS12 | posterior neuropore closes; upper limb buds |
| days 28–30 | CS13 | lower limb buds |
| day 56 | CS23 | end of the embryonic period; all major organs present |

![The human embryonic period, in days after fertilization (approximate). Coloured bands: preimplantation development, implantation and the bilaminar disc, gastrulation, neurulation and somitogenesis, organogenesis. Marked events with their Carnegie stages: zygote, morula, blastocyst, implantation, primitive streak, neural plate, first somites, heartbeat, closure of the anterior and posterior neuropores, upper and lower limb buds, and the end of the embryonic period at day 56. Gestational age is about two weeks more](./plots/human-timeline.py)

The embryonic period is the time of greatest sensitivity to **teratogens** (7.5.38), because the organs are being formed: an agent that disrupts limb outgrowth acts in weeks 4–6 and has little effect afterwards.

## Summary

- Model organisms are chosen for accessible embryos, short life cycles and genetic tools; each has characteristic strengths and limitations:

| Model | Main strengths | Main limitation |
|---|---|---|
| *C. elegans* | invariant, known lineage; RNAi by feeding | far from vertebrates |
| *Drosophila* | most powerful genetics; mosaics; GAL4/UAS | syncytial early embryo; invertebrate |
| zebrafish | transparent, external embryos; screens | no placenta; duplicated genes |
| *Xenopus* | large embryos for surgery and injection; animal caps | slow genetics (tetraploid *X. laevis*) |
| chick | surgery in ovo; quail–chick chimeras; electroporation | slow germ-line genetics |
| mouse | mammal; gene targeting; conditional knockouts | development inside the mother |
| minipig, marmoset | closer to human anatomy, physiology, behaviour | expensive; few genetic resources |

- A fate map records normal fates (Definition 2.5.1); lineage tracing marks a cell so that only its descendants inherit the mark (Definition 2.5.2): direct observation, dyes, chimeras, Cre-loxP reporters (inducible, multicolour), DNA barcodes, natural somatic mutations.
- Label collisions follow the birthday problem with the effective label number $N_{\mathrm{eff}} = 1/\sum p_i^2$ (Formula 2.5.1, Example 2.5.1); colour reporters need sparse labelling, barcodes need even frequencies.
- Single-cell omics profiles every cell type but infers trajectories; expression analysis shows where a gene could act; perturbation shows what it does.
- Loss of function tests necessity, gain of function sufficiency; "find it, lose it, move it" (Example 2.8.1). Pitfalls: morpholino specificity (Definition 2.8.1), compensation, redundancy, maternal products, early requirements, non-autonomy, context-dependent sufficiency.
- Explants (animal caps), embryo and organ culture and stem-cell models complement work in vivo.
- Human embryonic development spans 23 Carnegie stages in 8 weeks: blastocyst by day 5, implantation from day 6, primitive streak day 14–15, first somites day 20, heartbeat day 21–22, neural tube closed by day 28.

## Questions

1. You want to study (a) how the heart forms its chambers, with live imaging of every cell, (b) the role of the placenta in brain development, (c) the earliest signals that make mesoderm, using purified proteins. Which model would you choose for each, and why?

   **Answer** (a) Zebrafish: its embryos are transparent and develop externally, the heart forms within two days and can be imaged in living embryos, and embryos survive for days without a functioning circulation (they obtain oxygen by diffusion), so even severe heart mutants can be studied. (b) The mouse, the only standard model with a placenta and good genetics; tissue-specific knockouts in the trophoblast lineage separate placental from embryonic effects (or marmoset for a primate). (c) *Xenopus*: animal caps can be cut in large numbers and exposed to defined concentrations of purified proteins, and the response is read by marker genes.

2. What is the difference between a fate map and a lineage, and why does neither tell you whether a cell is determined?

   **Answer** A fate map shows what each region of an embryo normally becomes; it can be built by marking groups of cells. A lineage follows individual cells through their divisions and shows which descendants (and fates) come from each. Both describe normal development: they record what cells do, not what they could do. Whether a cell is determined is tested by changing its environment (isolation, heterotopic grafting); a cell whose descendants all become muscle in normal development may still be able to form other tissues elsewhere.

3. In a mouse experiment, CreER is driven by a promoter active in heart progenitors, and a low dose of tamoxifen labels about 1 % of the progenitors with a single-colour reporter. Later, the heart contains labelled patches. Under what condition can each patch be taken to be one clone, and how would you check it?

   **Answer** Each patch is one clone only if labelled progenitors are rare enough that two labelled clones seldom touch or intermingle. One checks it by titration: the number of patches should decrease in proportion to the tamoxifen dose while their size distribution stays the same (if patches were merged clones, lowering the dose would also shift the size distribution to smaller patches); alternatively use a multicolour reporter at the same dose and show that adjacent patches usually have different colours, or calculate the probability of merging from the observed patch density.

4. A barcoding experiment uses a library of $2\times10^5$ random barcodes, equally represented, to label 5000 cells. How many barcodes are expected to be shared by two or more cells, and is this a problem? What would change if 10 % of the library were a single barcode?

   **Answer** The expected number of colliding pairs is $n(n-1)/(2N) = 5000 \cdot 4999/(4\times10^5) \approx 62$: about 62 barcodes (about 1.2 % of the clones) would be shared by two cells. This would merge 62 pairs of clones, which matters if single clones are compared (it can be reduced by labelling fewer cells or using a larger library). If 10 % of the library is one barcode, about 500 cells receive it, so that barcode is useless for clonal analysis; also $\sum p_i^2 \ge 0.01$, so $N_{\mathrm{eff}} \le 100$ and the pairwise collision rate rises more than a thousandfold (Formula 2.5.1). Such dominant barcodes are excluded, and libraries are sequenced to check evenness.

5. A gene *A* is expressed in the limb bud. Mutant mice lacking *A* have normal limbs. Give four reasons why *A* may still have a function in limb development, and an experiment for each.

   **Answer** (i) Redundancy with a related gene: make double mutants with the paralogue. (ii) Genetic compensation triggered by the mutant mRNA: test an allele that makes no mRNA, measure paralogue expression. (iii) Maternal or early contribution is irrelevant in mammals for limbs, but an earlier or other function may be masked if the limb phenotype is subtle: examine skeletal elements, joints and gene expression in detail, or conditional knockouts at later stages. (iv) The phenotype may appear only under stress or in a **sensitized background** (**modifier screens**, reduced dosage of interacting genes). Finally, the gene may simply have no essential function there; expression does not prove function.

6. Why is a morpholino phenotype rescued by injection of the corresponding mRNA (lacking the morpholino target sequence) stronger evidence of specificity than the same phenotype seen with a second morpholino? What remains unproven?

   **Answer** Two morpholinos could share a non-specific toxic effect (such as p53 activation), so the same phenotype from both is suggestive but not conclusive. Rescue by an mRNA that cannot be bound shows that restoring the gene's product reverses the phenotype, which is expected only if the phenotype is due to the loss of that product. It does not prove that the knockdown is complete or that the phenotype reflects the gene's normal function at normal levels (overexpression from the injected mRNA could compensate for other defects); comparison with a genetic null mutant, considering compensation, is still needed.

7. Describe an experiment to show that a factor is sufficient to induce neural tissue in amphibian **ectoderm**, and the controls that make the result interpretable.

   **Answer** Cut animal caps from blastulae, culture them with the purified factor (or inject its mRNA into animal **blastomeres** before cutting), and assay neural markers (and the absence of mesoderm markers, which shows the induction is direct and not via mesoderm, since mesoderm can itself induce neural tissue). Controls: untreated caps from the same clutch (which should form only epidermis), caps treated with an inactive protein or buffer, a dose series, and checks that caps contain no contaminating marginal zone cells (absence of mesodermal markers). Sufficiency is limited to competent cells: caps taken too late may not respond.

8. Why does the embryonic period (weeks 3–8) carry the highest risk of malformations from **teratogens**, whereas exposure in the first two weeks typically causes either death or no effect?

   **Answer** In weeks 3–8 the organs are being formed by induction, cell migration, proliferation and differentiation in sequence; disrupting a process during its critical window leaves a specific malformation that cannot be repaired later. In the first two weeks the embryo consists of few, still largely undetermined cells that regulate: loss of some cells is compensated by the others (the embryo survives normally), while extensive damage kills the embryo (often before the pregnancy is recognized), the "all-or-none" period.
