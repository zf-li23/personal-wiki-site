---
title: "Genes and Signals: The Molecular Toolkit of Development"
description: "The molecular means by which cells with one genome become different: genomic equivalence and its exceptions; the levels of differential gene expression (chromatin, DNA methylation, promoters, modular enhancers, transcription factors and networks, splicing, stored maternal mRNAs and translational control, microRNAs, localization); the conserved developmental toolkit; induction, competence (with a model of the competence window), instructive and permissive interactions, reciprocal induction and the genetic and regional specificity of induction; the modes of cell-to-cell signalling (paracrine factors, juxtacrine signals, gap junctions, vesicles, cytonemes) and their range; the eight signalling families of development and their common features; and vulval induction in C. elegans, modelled as a graded paracrine signal combined with Notch-mediated lateral signalling."
---

The previous chapter described how cells become committed to different fates; this one describes the molecules that do it. Two kinds of molecule dominate: transcription factors and the other regulators of gene expression, which decide what a cell makes, and the secreted and membrane-bound signals with their receptors, by which cells instruct one another. Both are covered at the cellular and molecular level elsewhere: gene regulation in [7.2.12](/7.2.12)–[7.2.20](/7.2.20), signalling cascades in [7.3.18](/7.3.18)–[7.3.19](/7.3.19) and [7.1.14](/7.1.14)–[7.1.15](/7.1.15), the maintenance of differentiation in [7.3.24](/7.3.24). Here we summarize what development uses, introduce the concepts that describe how tissues interact (induction, competence, reciprocal induction) and end with an example in which a graded signal and a contact signal together pattern a row of cells.

## 3.1. Genomic Equivalence

Differentiated cells of an animal contain, with few exceptions, the same genome as the zygote (**genomic equivalence**, [7.3.1](/7.3.1)). Three lines of evidence established this ([7.3.24](/7.3.24#sec-24.2)): whole plants regenerate from single differentiated cells; nuclei of differentiated frog cells support development of enucleated eggs to tadpoles and adults (Briggs and King 1952; Gurdon 1962, **somatic cell nuclear transfer**); and a mammal, the sheep Dolly (1996), was cloned from an adult udder cell. Differentiated cells can also be reprogrammed to pluripotency by four transcription factors (Yamanaka, 2006). The exceptions are instructive because they are rare: B and T lymphocytes rearrange their antigen-receptor genes (V(D)J recombination, 7.15), mammalian red blood cells and lens fibre cells lose their nuclei, and in some animals the somatic cells eliminate part of the genome (chromatin diminution in the nematode *Parascaris*, discovered by Boveri), while the germ line keeps it whole.

Cell types therefore differ by differential gene expression, which rests on three postulates: every somatic nucleus contains the complete genome; the unused genes are not destroyed or mutated but remain potentially expressible; and only a small fraction of the genome is expressed in each cell type, the fraction differing between cell types.

## 3.2. Levels of Differential Gene Expression

Gene expression is regulated at every step between DNA and active protein. The table lists the levels that development uses most; the mechanisms are treated in [7.2](/7.2).

| Level | Mechanism | Developmental example |
|---|---|---|
| Chromatin | nucleosome position, histone modifications; Polycomb proteins keep developmental regulators silent (H3K27me3), Trithorax proteins keep them active (H3K4me3) | Hox genes remember their expression state through many divisions (7.5.15) |
| DNA methylation | methylation of CpG sequences represses promoters and is copied at replication (**DNA methylation**) | genomic imprinting; X inactivation; global demethylation after fertilization and in germ cells (7.5.27; [7.4.18](/7.4.18)) |
| Promoters | promoters rich in CpG (**CpG island**) are usually unmethylated and broadly active (housekeeping and many developmental genes); CpG-poor promoters are typical of tissue-specific genes | |
| Enhancers | modular **enhancers** bound by combinations of transcription factors activate a gene in particular places and times; each module adds one part of the expression pattern | *Pax6* has separate enhancers for the lens, the cornea, the retina and the pancreas; the stripes of *even-skipped* are driven by separate enhancers (7.5.15) |
| Transcription factors | families with conserved DNA-binding domains: homeodomain (Hox, Pax), basic helix-loop-helix (MyoD, Neurogenin), zinc finger, nuclear receptors, Sox (HMG box), T-box, forkhead; pioneer factors such as FoxA bind closed chromatin and open it for others | **master regulator** genes (MyoD, Pax6/*eyeless*) that can switch on a whole programme ([7.3.24](/7.3.24#sec-24.4.1)); **combinatorial control** |
| Gene regulatory networks | transcription factors regulate each other's genes; feedback loops stabilize states, and the network of a cell type defines it | the sea urchin endomesoderm network (7.5.6) |
| RNA processing | **alternative splicing** makes several proteins from one gene | the *Drosophila* sex-determination cascade ([7.4.6](/7.4.6)); *Dscam* can encode about 38 000 receptor isoforms that give neurons distinct identities |
| mRNA stability and storage | oocytes store maternal mRNAs in a repressed state; their poly(A) tails are lengthened or shortened at the right time; maternal mRNAs are degraded during the maternal-to-zygotic transition | *Xenopus* oocytes: CPEB and maskin repress cyclin B mRNA until maturation; **maternal-to-zygotic transition** (7.5.5) |
| Translation | RNA-binding proteins and **microRNAs** repress translation or promote decay | *bicoid* and *nanos* translation localized in the *Drosophila* egg (7.5.14); *lin-4* and *let-7* time larval stages in *C. elegans* (7.5.6) |
| Localization | mRNAs are transported along the cytoskeleton and anchored in particular regions | *bicoid* at the anterior, *oskar* at the posterior of the fly oocyte; *VegT* in the vegetal *Xenopus* egg |
| Protein | modification, proteolysis, localization and partner binding | Notch is activated by cleavage, β-catenin by escaping degradation |

## 3.3. The Developmental Toolkit

Animals as different as flies and mice build their bodies with a remarkably small and shared set of regulatory genes: a few families of transcription factors (Hox, Pax, Sox, T-box and others) and about eight families of signalling pathways (Section 3.6). The same genes are used again and again, in different combinations, at different times and places within one embryo, and the same genes perform comparable functions in distant animals: *Pax6* and its fly homologue *eyeless* initiate eye development in both, and Hox genes specify positions along the anterior–posterior axis in all bilaterians. This sharing reflects descent from a common ancestor that already had the toolkit (**deep homology**, 7.5.39), and it is the reason why results from flies and worms apply to vertebrates. Evolution has changed bodies mostly by changing where, when and how much these genes are expressed, largely through changes in their enhancers, rather than by inventing new genes.

## 3.4. Induction and Competence

### 3.4.1. Inducer and Responder

**Induction** ([7.3.24](/7.3.24#sec-24.3.2)) needs two partners: an inducing tissue that produces a signal, and a responding tissue that can respond to it.

**Definition 3.4.1 (Competence)** **Competence** is the ability of a cell or tissue to respond to an inductive signal in a particular way. It requires receptors for the signal, the machinery that transduces it and the transcription factors and accessible genes that carry out the response, and it is usually limited in time.

Competence is not passive: it is itself acquired by earlier inductions and then lost. Head ectoderm becomes competent to form a lens because it expresses the transcription factor Pax6, itself induced by earlier signals; when optic vesicles from normal mouse embryos are combined in culture with head ectoderm from *Small eye* mutants, which lack Pax6, no lens forms, whereas mutant optic vesicles induce lenses in normal ectoderm (Fujiwara and colleagues, 1994). The Pax6 requirement in the ectoderm defines its competence; such a transcription factor is called a competence factor.

The classic example of time-limited competence is the response of amphibian ectoderm to mesoderm inducers. Animal caps of *Xenopus* blastulae form mesoderm when exposed to activin or other Nodal-related factors, but caps taken from early gastrulae no longer do, although they still respond to neural inducers for a while longer (7.5.16). The model below shows how a window of competence and the duration of a signal together decide whether a tissue responds.

**Formula 3.4.1 (Competence Window)** Let the competence of the responding cells be $c(t)\in[0,1]$, and let an inducing signal of strength $S(t)$ be integrated by each cell as

$$
R = \int c(t)\,S(t)\,\mathrm{d}t ,
\tag{3.1}
$$
the cell responding when $R$ exceeds its threshold $\theta$. With thresholds distributed log-normally among cells (median $\theta_{\mathrm{m}}$, standard deviation $s$ in $\ln\theta$), the fraction of cells that respond is $\Phi\bigl(\ln(R/\theta_{\mathrm{m}})/s\bigr)$, where $\Phi$ is the standard normal distribution function.

**Example 3.4.1** Take a competence window $c(t) = \sigma\bigl((t-4\,\mathrm{h})/w\bigr)\,\sigma\bigl((10\,\mathrm{h}-t)/w\bigr)$, with $\sigma$ the logistic function and $w = 0.5\,\mathrm{h}$, $\theta_{\mathrm{m}} = 1\,\mathrm{h}$ and $s = 0.3$. A pulse of unit strength lasting 2 h gives $R = 0.34\,\mathrm{h}$ if it starts at 2 h (fewer than $0.1\,\%$ of cells respond), $R \approx 2\,\mathrm{h}$ if it starts at 6 h (nearly all respond) and $R = 0.63\,\mathrm{h}$ if it starts at 9.5 h (about $6\,\%$ respond). A pulse of 1 h never gives more than half the cells; a pulse of 4 h is effective over a wider range of start times, because it only needs to overlap the window long enough.

![Competence limits the response to an inducer in time. A: the competence of a responding tissue rises at about 4 h and falls at about 10 h (Formula 3.4.1); three 2-h pulses of inducer give integrated signals R of 0.34, about 2 and 0.63 h. B: fraction of cells responding against the start time of the pulse, for pulses of 1, 2 and 4 h (thresholds log-normal with median 1 h): the response is possible only when the pulse overlaps the competence window (shaded), and short signals work only in its middle](./plots/competence-window.py)

The model shows why the timing of an experiment matters: a negative result of a graft or of adding a factor may mean that the responding tissue was not, or no longer, competent. It also shows why development can use the same signal at different times for different purposes: what changes is the competence of the cells.

### 3.4.2. Instructive and Permissive Interactions

**Definition 3.4.2 (Instructive and Permissive Interactions)** An inductive interaction is *instructive* when the signal from the inducing cell is needed to initiate a new programme of gene expression in the responding cell, which would not adopt the fate without it. It is *permissive* when the responding cell is already committed and needs only an environment, such as a suitable extracellular matrix or a survival factor, in order to express its fate.

Instructive signals often choose between fates: Wessells formulated the principle that, in the presence of tissue A, responding tissue B develops in a certain way, and in the absence of A it develops differently. Permissive interactions include the need of many epithelia for a **fibronectin**-containing matrix, or of developing neurons for survival factors.

### 3.4.3. Specificity of Induction

Many organs form by the interaction of an epithelium with a mesenchyme (loosely organized cells, often of mesodermal or neural crest origin). Recombination experiments show two kinds of specificity:

- Regional specificity. In the chick, the dermis (mesenchyme) decides which appendages the overlying epidermis forms: back dermis induces feathers, thigh dermis thigh feathers, foot dermis scales and claws, even under epidermis from another region. The inducer carries positional information about the kind of structure.
- Genetic specificity. The responding tissue's genome decides what it can make. When Spemann and Schotté (1932) grafted the flank ectoderm of a frog embryo into the mouth region of a newt, it formed frog mouth parts (a horny jaw and suckers); newt ectoderm in the frog mouth region formed newt teeth. The inducer said "make a mouth"; the ectoderm could only answer with the mouth of its own species.

**Definition 3.4.3 (Reciprocal Induction)** In **reciprocal induction** two tissues induce each other: the responding tissue, once induced, becomes an inducer of the tissue that induced it.

The optic vesicle induces the head ectoderm to form the lens placode, and the developing lens then induces the optic vesicle to form the two-layered optic cup and the neural retina (7.5.22). In the kidney, the ureteric bud induces the metanephric mesenchyme to form nephrons, and the mesenchyme induces the bud to grow and branch (7.5.25). Reciprocal induction makes organs out of cascades of signals that alternate between two partners and coordinates their growth.

![Induction, competence and reciprocal induction in the eye. A: the optic vesicle, an outgrowth of the forebrain, contacts the head ectoderm, which is competent because it expresses Pax6. B: the ectoderm thickens into the lens placode. C: the lens vesicle forms and induces the optic vesicle to fold into the optic cup, with the neural retina inside and the pigmented epithelium outside: each tissue induces the other. D: tissue recombinations in the mouse: ectoderm lacking Pax6 does not form a lens even with a normal optic vesicle, whereas a mutant optic vesicle can induce a lens in normal ectoderm](./plots/lens-induction.py)

Many inductions also need enough responding cells together: the **community effect** ([7.3.24](/7.3.24#sec-24.3.4)), in which cells reinforce each other's response through a secreted signal.

## 3.5. Modes of Signalling

### 3.5.1. Paracrine Factors

**Definition 3.5.1 (Paracrine Factor)** A **paracrine factor** is a secreted signalling protein that diffuses or is transported over a short distance, typically from a few to a few dozen cell diameters, and changes the fate or behaviour of the cells it reaches; most inducers are paracrine factors.

Hormones of the adult act at a distance through the blood (endocrine signalling); in the embryo most signals are **paracrine**, acting on neighbours, and some are **autocrine**, acting also on the cell that made them (the community effect is one consequence). The range of a paracrine factor is set by its diffusion and its removal. If it diffuses with coefficient $D$ and is degraded or captured at rate $k$, its concentration falls with distance over a characteristic length $\lambda = \sqrt{D/k}$ (the **decay length** of 7.5.11); for a protein with an effective $D$ of $1$–$10\,\mu\mathrm{m^2\,s^{-1}}$ in tissue and a lifetime $1/k$ of half an hour to a few hours, $\lambda$ lies between about $40$ and $300\,\mu\mathrm{m}$, a few to a few dozen cell diameters. A paracrine factor whose concentration gradient specifies several fates in order is a **morphogen** (7.5.11).

The binding of paracrine factors to the extracellular matrix, in particular to heparan sulfate proteoglycans, concentrates them, slows their movement and can be necessary for their activity; their range is also shaped by extracellular antagonists that bind them (Noggin, Chordin, Dickkopf, Cerberus) and by their own receptors, which capture them.

### 3.5.2. Juxtacrine Signals, Junctions and Long Protrusions

Signals can also pass between cells without diffusing freely:

- Juxtacrine signalling: a ligand anchored in one cell's membrane binds a receptor in the adjacent cell (**contact-dependent signaling**, [7.3.18](/7.3.18)): Delta–Notch, ephrin–Eph, and binding of cells to the matrix through **integrins**.
- Gap junctions: channels between the cytoplasms of neighbours let ions and small molecules (Ca²⁺, cAMP, IP₃) pass (**gap junction**, [7.3.23](/7.3.23)); they coordinate cells within a tissue, for example the left–right asymmetry of some embryos.
- Extracellular vesicles: vesicles released from the plasma membrane or from multivesicular bodies (**exosome**, [7.3.10](/7.3.10)) carry proteins and RNAs, and can transport otherwise membrane-bound signals such as Wnt and Hedgehog.

**Definition 3.5.2 (Cytoneme)** A *cytoneme* is a thin, actin-based filopodium, up to tens or even hundreds of micrometres long, that extends from a signal-producing or signal-receiving cell and transmits a signal at its contact with the distant partner cell.

Cytonemes were found in the *Drosophila* wing imaginal disc, where cells of the disc extend them towards the cells that produce the morphogen Dpp (Ramírez-Weber and Kornberg, 1999); they also carry Hedgehog, Wnt and FGF, in flies and in vertebrates (zebrafish cells extend Wnt8a-carrying filopodia to their neighbours). Signals carried by cytonemes are delivered to particular cells, which makes the shape of a gradient depend on where the cytonemes reach as well as on diffusion.

![Modes of signalling between embryonic cells. A: paracrine: a secreted factor diffuses to receptors on nearby cells. B: autocrine: the secreting cell responds to its own factor. C: juxtacrine: a membrane-bound ligand binds a receptor on the adjacent cell. D: gap junctions connect the cytoplasms of neighbours. E: extracellular vesicles carry proteins and RNAs between cells. F: a cytoneme, a long filopodium, carries ligand to a distant cell](./plots/signaling-modes.py)

### 3.5.3. Features of Signalling in the Embryo

- The range is limited: a few to a few dozen cell diameters for paracrine factors, one cell for juxtacrine signals; only in the adult, with a circulation, do hormones act over long distances.
- Not all cells respond: only competent cells (Section 3.4).
- Different cells respond to the same signal differently, because their competence differs. In the adult, acetylcholine slows the beating of heart muscle but stimulates the secretion of the salivary glands; in the embryo, Shh specifies the ventral neural tube, the digits of the limb and the growth of the gut, each through the cells' own transcription factors.

## 3.6. The Signalling Families of Development

Most inductive interactions in animals use a handful of pathways, listed in the table. Their biochemistry is in [7.3.19](/7.3.19); here what matters is where development uses them.

| Family | Main ligands | Receptor and transducer | Key developmental uses |
|---|---|---|---|
| Wnt, canonical (**Wnt signaling pathway**) | about 20 Wnts in vertebrates | Frizzled + LRP5/6; inhibition of the destruction complex, **β-catenin** with TCF/LEF | dorsal organizer, posteriorization of the neural plate, neural crest, limb and kidney development, stem-cell niches, proliferation |
| Wnt, non-canonical | Wnt5a, Wnt11 | Frizzled, Ror, Ryk; planar cell polarity (Rho, JNK), Ca²⁺ | convergent extension in gastrulation, orientation of cells and hairs |
| TGF-β superfamily, TGF-β/Nodal/Activin branch (**TGF-β signaling pathway**) | Nodal, Activin, TGF-β, Vg1/GDF1 | type I and II serine/threonine kinase receptors; Smad2/3 with Smad4 | mesoderm and endoderm induction, left–right asymmetry |
| TGF-β superfamily, BMP branch | BMP2/4/7, GDFs, Dpp (fly) | type I and II receptors; Smad1/5/8 (also called Smad9) with Smad4 | dorsal–ventral patterning, epidermis versus neural ectoderm, bone and cartilage, apoptosis between the digits |
| TGF-β superfamily, non-Smad | | TAK1, MAPK, Rho | survival, apoptosis, proliferation, migration |
| FGF and other **receptor tyrosine kinase** ligands | 22 FGFs (FGF11–14 are not secreted and act inside the cell); EGF, PDGF, VEGF, insulin, IGF, HGF | receptor tyrosine kinases; Ras–MAPK, PI3K–Akt, PLCγ; FGFs also via JAK–STAT | maintenance and induction of mesoderm and endoderm, neural induction, limb outgrowth, branching of lung and kidney, blood vessels (VEGF), growth (IGF) |
| Hedgehog (**Hedgehog signaling pathway**) | Shh, Ihh, Dhh | Patched relieves its inhibition of Smoothened; Gli activators instead of repressors, in the **primary cilium** | ventral neural tube, digit identity, growth of bone (Ihh), gut, germ cells (Dhh) |
| Notch (**Notch signaling pathway**) | Delta, Jagged (Serrate) on the neighbour | Notch is cleaved; its intracellular domain enters the nucleus with CSL (RBPJ) | **lateral inhibition** (neurons), boundaries, the somite clock, arterial identity, blood stem cells |
| Eph–ephrin | ephrin-A (GPI-anchored), ephrin-B (transmembrane) | Eph receptor tyrosine kinases; signalling in both directions to Rho GTPases | segment boundaries, cell sorting, guidance of axons and neural crest cells, arteries and veins |
| Hippo (**Hippo pathway**) | not a single ligand: cell contacts, polarity, mechanical tension | kinases Mst and Lats phosphorylate YAP/TAZ and keep them out of the nucleus | organ size, the choice between inner cell mass and trophectoderm (7.5.5), regeneration |

Some signals are not proteins. Retinoic acid, made from vitamin A, diffuses into cells and binds nuclear receptors; it patterns the hindbrain, the trunk and the limbs, and its excess is teratogenic (7.5.38). Steroid and thyroid hormones act through nuclear receptors in sex differentiation and metamorphosis (7.5.26, 7.5.33).

![The signalling pathways of development as activity flows: input, receptor, transducer and nuclear effector for each family, with its main developmental roles. Open arrows denote activation, bars inhibition: Wnt and Hedgehog act by relieving an inhibition (the receptor inhibits a negative regulator), and the Hippo kinases inhibit the transcriptional coactivators YAP and TAZ](./plots/signaling-families.py)

Signalling pathways share a few features:

- Each has many members and many nodes and branches: several ligands, receptors and transducers, often with partly overlapping specificities.
- They interact (**crosstalk**): one pathway regulates the components or the targets of another, and target genes often integrate several pathways at one enhancer (for example, Wnt and BMP targets in the organizer region).
- Their effects are specific to cell type and stage: the same pathway activates different genes in different cells.
- Their activity is shaped by secreted antagonists and by feedback: many pathways induce their own inhibitors (Wnt induces Dickkopf and Axin2, Hedgehog induces Patched, Nodal induces Lefty, Notch induces Hes repressors), which limits the range and duration of the signal.

## 3.7. Integration: Vulval Induction in *C. elegans*

The vulva of the *C. elegans* hermaphrodite, through which eggs are laid, forms from three of six equivalent epidermal precursor cells, P3.p to P8.p, which lie in a row along the ventral side. A single cell of the gonad above them, the anchor cell, induces them. Its signal, LIN-3, is an EGF-like paracrine factor that acts on the receptor tyrosine kinase LET-23 and the Ras–MAPK pathway. The cell nearest the anchor cell, P6.p, adopts the primary (1°) fate and its descendants form the centre of the vulva; its neighbours P5.p and P7.p adopt the secondary (2°) fate and form its flanks; P3.p, P4.p and P8.p adopt the tertiary (3°) fate and fuse with the surrounding epidermis. The 22 cells of the vulva descend from the three induced cells.

Experiments showed that two signals combine:

- Removing the anchor cell with a laser (Kimble, 1981) makes all six cells adopt the 3° fate; mutants lacking LIN-3 or LET-23 have no vulva, whereas mutants with constitutively active Ras (*let-60* gain of function) induce extra vulval tissue (multivulva).
- The anchor cell signal is graded: when the amount of LIN-3 is reduced, the 2° fate appears in cells that would otherwise be 1°, and moving the anchor cell moves the pattern.
- The 1° cell signals laterally. It expresses Delta-like ligands (LAG-2, APX-1, DSL-1) that activate LIN-12, the *C. elegans* Notch, in its neighbours; LIN-12 induces the 2° fate and represses the 1° response, for example by inducing a MAPK phosphatase. In *lin-12* loss-of-function mutants no cell adopts the 2° fate, and adjacent cells can both become 1°; in *lin-12* gain-of-function mutants all six cells adopt the 2° fate, even without the anchor cell.

The pattern is therefore set by a paracrine gradient, which picks the 1° cell, and by juxtacrine lateral signalling, which makes its neighbours 2° and prevents a second 1° cell next to it. The following minimal model reproduces these experiments.

**Formula 3.7.1 (A Minimal Model of Vulval Patterning)** Let $s_i = s_0\exp(-\lvert i-6\rvert/\ell)$ be the LIN-3 signal received by cell $P i.\mathrm{p}$ ($i = 3,\dots,8$), $a_i$ the level of its 1° programme and $n_i = a_{i-1}+a_{i+1}$ the lateral (LIN-12) signal it receives from its neighbours. In dimensionless units,

$$
\frac{\mathrm{d}a_i}{\mathrm{d}t} = \frac{h(s_i)}{1+(n_i/K_n)^2} - a_i, \qquad h(s) = \frac{s^4}{K^4+s^4},
\tag{3.2}
$$
and a cell adopts the 1° fate if $a_i > 1/2$, otherwise the 2° fate if $n_i$ exceeds a threshold (and LIN-12 is functional), otherwise the 3° fate.

**Example 3.7.1** With $s_0 = 1$, $\ell = 0.7$, $K = 0.35$, $K_n = 0.3$ and a 2° threshold $n_i > 0.4$, P6.p receives $s = 1$ and reaches $a \approx 0.98$, while P5.p and P7.p receive $s = 0.24$, so $h \approx 0.18$, and their lateral input from P6.p ($n \approx 0.98$) suppresses their 1° programme tenfold: they become 2°. P4.p and P8.p receive almost neither signal and become 3°. Setting $s_0 = 0$ (anchor cell ablated) gives all 3°; removing the lateral term gives 3° 3° 3° 1° 3° 3°; fixing $n_i$ high (LIN-12 gain of function) gives all 2°. With a uniform excess of LIN-3 ($s_i = 2$) all cells start alike, and lateral inhibition amplifies small differences into an alternating pattern of 1° and 2° cells; without LIN-12 all six become 1°.

![A minimal model of vulval patterning (Formula 3.7.1). Top: LIN-3 from the anchor cell, highest at P6.p. Rows: fates of P3.p–P8.p in the model: 1° (blue), 2° (pink), 3° (grey). The wild type gives 3° 3° 2° 1° 2° 3°; without the anchor cell all are 3°; without LIN-12 there are no 2° fates; with constitutive LIN-12 all are 2°; uniform excess LIN-3 gives alternating 1° and 2° fates by lateral inhibition, and all 1° fates without LIN-12](./plots/vulva-model.py)

The vulva shows in miniature the logic of much of development: a graded paracrine signal gives a coarse spatial cue, juxtacrine signalling refines it into sharp, non-overlapping fates, and the same pathways (EGF, Notch, Wnt, which also acts on the precursors) are reused, here and elsewhere, with different outcomes.

## Summary

- Genomic equivalence holds for almost all cells (exceptions: lymphocytes, enucleated cells, chromatin diminution); cell types differ by differential gene expression.
- Expression is controlled at many levels: chromatin and Polycomb/Trithorax memory, DNA methylation, CpG-rich and CpG-poor promoters, modular enhancers, transcription factor families and networks, splicing, storage and translational control of maternal mRNAs, microRNAs, mRNA localization and protein modification.
- A small conserved toolkit of transcription factors and signalling pathways is reused throughout development and across animals; evolution changes mainly its regulation.
- Induction requires an inducer and a competent responder (Definition 3.4.1); competence is acquired and lost, so the response depends on the overlap of signal and competence window (Formula 3.4.1, Example 3.4.1). Interactions are instructive or permissive (Definition 3.4.2), show regional and genetic specificity, and can be reciprocal (Definition 3.4.3).
- Signals act by paracrine factors (Definition 3.5.1; range $\lambda = \sqrt{D/k}$, tens to hundreds of micrometres), juxtacrine contact, gap junctions, vesicles and cytonemes (Definition 3.5.2).

| Pathway | Effector | Typical use |
|---|---|---|
| Wnt/β-catenin | β-catenin–TCF | axes, organizer, posterior fates, niches |
| Nodal/Activin | Smad2/3 | mesoderm and endoderm, left–right |
| BMP | Smad1/5/8 | dorsal–ventral, epidermis vs neural |
| FGF/RTK | Ras–MAPK | mesoderm, limb outgrowth, branching |
| Hedgehog | Gli | neural tube, digits, bone |
| Notch | NICD–CSL | lateral inhibition, boundaries, clock |
| Eph–ephrin | Rho GTPases | boundaries, sorting, guidance |
| Hippo | YAP/TAZ | organ size, first lineage choice |

- Pathways have many members, cross-talk, cell-type-specific outcomes and built-in negative feedback.
- Vulval induction combines a graded LIN-3/EGF signal (1° fate) with LIN-12/Notch lateral signalling (2° fate) (Formula 3.7.1, Example 3.7.1).

## Questions

1. How would you show that the nucleus of a differentiated cell still contains the genes needed to make all cell types? Why do the low success rates of nuclear transfer from adult cells not contradict genomic equivalence?

   **Answer** Transfer the nucleus into an enucleated egg (or reprogram the cell with transcription factors) and show that it supports the development of a complete, fertile organism or of pluripotent cells that contribute to all tissues; a single such success proves that the genome is complete. Low success rates reflect the difficulty of reprogramming chromatin (DNA methylation, histone marks, the need to replicate rapidly in the egg cytoplasm) and damage during the procedure, not missing genes; a missing gene could never be restored, whereas epigenetic barriers can be overcome in some cases.

2. Optic vesicles of a mutant mouse fail to induce a lens in normal ectoderm in culture, while normal optic vesicles induce lenses in mutant ectoderm. In which tissue does the mutated gene act, and what kind of molecule might it encode?

   **Answer** The gene acts in the inducing tissue, the optic vesicle: normal ectoderm is competent but receives no adequate signal from the mutant vesicle, whereas mutant ectoderm responds normally to a normal vesicle. It could encode a secreted inducer (for example a BMP or FGF made by the optic vesicle), an enzyme needed to make or release it, or a transcription factor required in the optic vesicle for its production. (This is the converse of the *Small eye* recombination, in which Pax6 is needed in the ectoderm.)

3. In the frog–newt mouth experiment, what do the results tell you about the information carried by the inducer and by the responding tissue? Give a modern molecular interpretation.

   **Answer** The inducer specified the region and type of structure (mouth parts), but not the species-specific form, which was determined by the genome of the responding ectoderm. Molecularly, the signals (conserved paracrine factors such as BMPs, FGFs, Shh) are similar in frog and newt; what differs are the target genes and their enhancers in the responding cells, which interpret the signal according to their own regulatory programme: the signal selects a programme, the responding genome supplies its content.

4. Using Formula 3.4.1 with the parameters of Example 3.4.1, estimate the minimum duration of a pulse starting at 5 h that makes half the cells respond. What would happen if the threshold doubled?

   **Answer** Half the cells respond when $R = \theta_{\mathrm{m}} = 1\,\mathrm{h}$. At 5 h the competence is already $c \approx 0.88$ and it is close to 1 from about 6 h, so $\int_5^{5+\tau} c\,\mathrm{d}t \approx \tau - 0.06\,\mathrm{h}$; $R = 1\,\mathrm{h}$ needs $\tau \approx 1.06\,\mathrm{h}$ (numerical integration gives $1.06$). If the median threshold doubled to 2 h, the pulse must last about 2.06 h, and a pulse starting later than about 8 h could not reach it however long it lasted, because the remaining competence $\int_{t_0}^{\infty} c\,\mathrm{d}t \approx 10\,\mathrm{h} - t_0$ is less than 2 h; the window for effective induction narrows.

5. A diffusible factor with $D = 5\,\mu\mathrm{m^2\,s^{-1}}$ is degraded with a half-life of 30 min. How far does it reach, in cell diameters of $10\,\mu\mathrm{m}$, before its concentration falls to $1/\mathrm{e}$, and how would binding to heparan sulfate proteoglycans change this?

   **Answer** $k = \ln 2/1800\,\mathrm{s} = 3.85\times10^{-4}\,\mathrm{s^{-1}}$, so $\lambda = \sqrt{D/k} = \sqrt{5/3.85\times10^{-4}}\,\mu\mathrm{m} \approx 114\,\mu\mathrm{m}$, about 11 cell diameters. Reversible binding to proteoglycans lowers the effective diffusion coefficient (the molecule spends part of its time bound), which shortens the range, and if binding also protects the factor from degradation it lowers $k$, which lengthens it; binding also concentrates the factor near the surface of cells, which can increase signalling locally. The net effect depends on which change dominates.

6. In the vulval model, why does a uniform excess of LIN-3 give alternating 1° and 2° fates rather than six 1° cells? What would you expect in real worms with excess LIN-3, and how would you test the role of LIN-12?

   **Answer** When all cells receive a strong signal, each starts the 1° programme, but each also inhibits its neighbours through the lateral signal; a cell that gets slightly ahead suppresses its neighbours more and is less suppressed in return, so the uniform state is unstable and resolves into alternating 1° cells separated by 2° cells (lateral inhibition, as in Notch–Delta patterning). In worms with excess LIN-3, extra 1° and 2° cells form, producing several vulval invaginations (multivulva), with 2° cells between 1° cells. Combining excess LIN-3 with a *lin-12* loss-of-function mutation should convert the 2° cells to 1° (adjacent 1° cells); mosaic analysis with LIN-12 removed from single cells would show that LIN-12 is needed in the cell that becomes 2°.

7. Why do many signalling pathways induce their own inhibitors? Give two developmental consequences.

   **Answer** Negative feedback limits the strength, duration and range of signalling and makes the output less sensitive to the amount of ligand. Consequences: it allows oscillations when combined with delays (Notch–Hes in the segmentation clock); it sharpens and limits gradients and makes patterns scale or be robust (Nodal induces the faster-diffusing Lefty, forming a reaction–diffusion system that limits Nodal's range and is used in left–right patterning; Hedgehog induces Patched, which captures Hedgehog and shortens its range).

8. The same signal, Shh, specifies the ventral neural tube, the identity of digits and the growth of bone and gut. How is this possible, and how would you show that the difference lies in the responding cells?

   **Answer** Shh activates the same pathway (Patched, Smoothened, Gli) in all these cells, but the cells differ in competence: different transcription factors and chromatin states determine which target genes have accessible enhancers that Gli can activate, and the levels and duration of signalling differ. To show that the difference lies in the responders, expose different tissues (neural plate explants, limb mesenchyme) to the same purified Shh at the same concentration and see that they activate different genes, or graft a Shh source (a bead or Shh-expressing cells) to different tissues: neural cells form ventral neural types, limb mesenchyme forms extra digits.
