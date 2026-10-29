---
title: Cleavage and the Blastula
description: "The first divisions of the embryo. The features of cleavage; maternal factors and maternal, zygotic and maternal–zygotic mutants; the maternal-to-zygotic transition and the titration models of its timing; yolk and the patterns of cleavage; cleavage in sea urchins, frogs, zebrafish, chicks and Drosophila; the lattice energy model of blastocoel formation with its cusp and wall profile; mammalian cleavage, compaction and the two lineage decisions (Hippo signalling and the Nanog–Gata6 switch); implantation; twins, chimeras and assisted reproduction."
---

Fertilization ([7.5.4](/7.5.4)) leaves a single large cell with a diploid nucleus and an enormous store of maternal proteins and RNAs. Cleavage turns it, in a few hours or days, into a ball of hundreds or thousands of small cells, the blastula, without growing at all. Three things happen in this period and are the subject of the chapter. The cytoplasm is partitioned among cells, according to geometric rules that depend mostly on the amount and position of yolk, so that **cytoplasmic determinants** localized in the egg end up in particular cells ([7.5.1](/7.5.1), [7.5.6](/7.5.6)). Control passes from the mother's products to the embryo's own **genome** at the maternal-to-zygotic transition, whose timing is measured, at least in part, by titrating maternal factors against the growing amount of DNA. And the first tissue architecture appears: a fluid-filled cavity, the blastocoel, and in mammals the first two lineage decisions, which separate the extraembryonic tissues from the cells that will form the body. The mechanics of the blastocoel is our first mathematical model of morphogenesis, a lattice energy whose local form is the cusp of catastrophe theory ([7.5.10](/7.5.10)); the mammalian decisions are our first examples of how position, polarity, signalling and bistable gene circuits combine to make reproducible proportions of cell types. The chapter ends with the clinical consequences of this period: early pregnancy loss, twinning, chimeras and assisted reproduction. Gastrulation, which the blastula prepares, follows in [7.5.9](/7.5.9).

## 5.1. The Features of Cleavage

**Definition 5.1.1 (Cleavage, Blastula)** **Cleavage** is the series of rapid mitotic divisions that follows fertilization and divides the cytoplasm of the zygote into many smaller cells, the **blastomeres**, without an increase in total mass. Its product, a ball or disc of cells in which gastrulation has not yet begun, is the **blastula**; in most animals it surrounds a fluid-filled cavity, the **blastocoel**.

The period from the formation of the blastula to the beginning of gastrulation is called the blastula stage. Cleavage has five general features.

1. Short cycles: The cleavage cycle of most animals alternates S phase and mitosis with no or very short gap phases: about 8–10 min per nuclear division in *Drosophila*, 15 min in zebrafish, 30 min in *Xenopus*, but 12–24 h in the mouse. The first cycle is usually longer, because it includes the migration and fusion of the pronuclei. The engine is the **cell cycle** oscillator of [7.3.20](/7.3.20) running on maternal stocks of cyclin mRNA, Cdk1 and the components of DNA replication and mitosis, with the checkpoints that later slow the cycle largely inactive.
2. Falling cytoplasm-to-nucleus ratio: Because the cells do not grow, each division halves the volume of cytoplasm per nucleus. In the sea urchin the ratio of cytoplasmic to nuclear volume falls from about 550 in the egg to about 6 at the end of cleavage. This ratio is one of the clocks of the embryo (5.2.3).
3. From equal to unequal divisions: Early cleavages are often equal; later ones are frequently unequal, as in the fourth cleavage of the sea urchin, which produces micromeres (5.4.1).
4. A cavity: Most blastulae enclose a blastocoel (5.5); spiralian embryos and many embryos with large yolk do not (a solid blastula is called a stereoblastula).
5. A quiet genome: In most species the zygotic genome is almost silent during the early cleavages, and development runs on maternal products (5.2).

**Remark 5.1.1 (Rules of Cleavage Geometry)** Nineteenth-century embryologists summarized the geometry of cleavage in empirical rules. Balfour's rule: the speed of cleavage in a region is inversely related to its yolk content, because yolk impedes the furrow. Hertwig's rule: the spindle aligns with the longest axis of the cytoplasm, so the furrow cuts the cell across that axis. The second rule now has a mechanical explanation. Microtubule asters grow from the centrosomes until they reach the cortex, where dynein pulls on them; the pulling force grows with microtubule length, and the spindle settles in the orientation that balances the forces, which in an elongated cell is along its long axis. Sea urchin eggs pushed into rectangular microchambers orient their spindles along the long axis of the chamber, as the rule predicts. Yolk, cortical polarity cues and adhesion to neighbours modify this default.

## 5.2. Maternal Factors and the Maternal-to-Zygotic Transition

### 5.2.1. Maternal Factors and Three Classes of Mutants

The egg is built during **oogenesis** ([7.5.27](/7.5.27)) with everything the embryo will need before it can make its own products: ribosomes, mitochondria, yolk, histones and replication proteins, and thousands of mRNAs, many of them held in a translationally silent state until fertilization or later.

**Definition 5.2.1 (Maternal Factor)** A **maternal factor** is a molecule, usually an mRNA or a protein, made from the mother's genome during oogenesis and stored in the egg, where it acts in the early embryo.

A gene can contribute to the embryo in three ways: maternally only (its product is made during oogenesis but the gene is not transcribed in the embryo), zygotically only, or both. Mutations in such genes give three classes of phenotype, which matter both to experimental design and to genetic counselling (table below). The genetics of the first class, the **maternal-effect genes**, is treated in [7.4.20](/7.4.20) and [7.4.11](/7.4.11); here the point is what each class implies for the cause of early embryonic death.

| Class | Phenotype appears when | What it depends on | Use of testing the embryo |
|---|---|---|---|
| Maternal mutant | the mother is homozygous mutant (her oocytes lack the product) | only the mother's genotype; all her embryos are affected, whatever the father and whatever the embryo's own genotype | none: testing the mother is informative, testing embryos is not |
| Zygotic mutant | the embryo itself is homozygous mutant | both parents' genotypes (each must transmit a mutant allele) | preimplantation testing can select unaffected embryos |
| Maternal–zygotic (MZ) mutant | the mother is homozygous and the embryo is homozygous, so neither source supplies the product | both | the MZ phenotype is often more severe than the maternal or zygotic phenotype alone, because zygotic expression no longer rescues the maternal loss, or maternal stores no longer mask a zygotic requirement |

Two remarks clarify the table. First, a heterozygous mother provides the product to every egg, because the oocyte transcribes the gene before meiosis is complete, from both alleles (a primary oocyte arrested in prophase I carries both homologues, each as two chromatids); only after meiosis do the eggs differ in the allele they carry, too late to matter. Second, in experimental organisms MZ mutants are made deliberately, for example by germ-line replacement in zebrafish, because a zygotic mutant may look normal only because its mother's stores carried it through early development. In humans, maternal-effect mutations in genes of the subcortical maternal complex of the oocyte (*NLRP5*, *PADI6*, *TLE6*, *KHDC3L*) and in *NLRP7* cause recurrent arrest of embryos at cleavage stages, infertility, or recurrent hydatidiform moles in every pregnancy of an affected woman, with any partner: exactly the pattern of a maternal mutant.

### 5.2.2. The Transition and Its Timing

**Definition 5.2.2 (Maternal-to-Zygotic Transition, Zygotic Genome Activation, Mid-Blastula Transition)** The **maternal-to-zygotic transition** (MZT) is the transfer of developmental control from maternal factors to products of the embryo's own genome. It has two arms: the clearance of a large part of the maternal mRNAs and proteins, and **zygotic genome activation** (ZGA), the onset of transcription from the zygotic nuclei. In species with rapid synchronous cleavage, the cell-cycle changes that accompany the major wave of ZGA are called the **mid-blastula transition** (MBT): the cycles lengthen and acquire gap phases, lose their synchrony, and the cells become motile.

ZGA is not a single event. A minor wave of transcription from a few hundred genes precedes the major wave by several cycles, and individual genes start at different times; maternal mRNAs too are removed in waves, some by maternally encoded decay machinery shortly after fertilization, others by zygotic products. A conserved example of the latter is a zygotic **microRNA**: miR-430 in zebrafish and miR-427 in *Xenopus* are transcribed at the major ZGA and target hundreds of maternal mRNAs for deadenylation and decay; miR-309 has the same role in *Drosophila*.

| Species | Minor ZGA | Major ZGA (and MBT) | Comment |
|---|---|---|---|
| *Drosophila* | nuclear cycle 7–8 | cycle 14 (about 2.5 h after egg laying, about 6000 nuclei) | cycles 1–10 last about 8 min; cycle 13, 25 min; cycle 14 is asynchronous, 75–175 min, and cellularization occurs in its interphase |
| Zebrafish | about the 64-cell stage | cycle 10 (512 to 1000 cells, about 3 h) | cycle lengthening is gradual over cycles 10–13 |
| *Xenopus* | from about the 256-cell stage | end of cycle 12 (about 4000 cells, about 7 h at 23 °C) | the classical MBT (Newport and Kirschner) |
| Mouse | late zygote | 2-cell stage | no MBT in the strict sense: the cycles are long from the start |
| Human | 1- to 4-cell stage | 4- to 8-cell stage (day 2–3) | development before day 3 runs on maternal products; arrest at this stage is common in vitro |

Sea urchins and *C. elegans* transcribe zygotic genes in some blastomeres from very early cleavage stages, and have no sharp MBT. In amniotes the long cycles make the distinction between the cell-cycle change (MBT) and the transcriptional change (ZGA) disappear.

### 5.2.3. What Measures the Time: Titration Models

Two kinds of mechanism have been proposed for the timing of the major ZGA: a clock that measures time since fertilization, and a counter that measures how many nuclei, or how much DNA, the cytoplasm contains. The classical experiments on *Xenopus* favour the counter for the MBT. Haploid embryos undergo the MBT one cycle later than diploids, and polyspermic or tetraploid ones earlier; constricting an egg so that one half receives no nucleus until later delays the MBT in that half by the corresponding number of cycles; and injecting extra DNA into the egg advances it. All these results say that the MBT occurs at a fixed ratio of DNA to cytoplasm. The natural interpretation is titration: some maternal factor of fixed total amount is progressively bound by the DNA, whose quantity doubles at every cycle, until its free concentration falls below a threshold.

**Formula 5.2.1 (Titration of a Maternal Repressor)** Let a maternal repressor of total amount $R$ (in units of its dissociation constant $K$) bind with equal affinity to sites on the DNA; after $n$ cleavages an embryo of ploidy $p$ contains $S_n = p\,s\,2^n$ sites, $s$ per haploid genome. If binding is at equilibrium, the free repressor $r$ satisfies

$$
r + \frac{S_n\, r}{1 + r} = R,
\qquad
r = \frac{-(1 + S_n - R) + \sqrt{(1 + S_n - R)^2 + 4R}}{2},
\tag{5.1}
$$
and a promoter carrying one site is free of repressor with probability $1/(1 + r)$.

When $R \gg 1$, $r$ stays close to $R - S_n$ until the sites are nearly as numerous as the repressor molecules, then collapses: the onset of transcription is switch-like and occurs at $S_n \approx R$, that is at

$$
n^* \approx \log_2 \frac{R}{p\,s}.
$$

Because $n^*$ depends on $p\,2^n$, halving the ploidy delays the switch by exactly one cycle and doubling it advances it by one (figure below, panel A). What is titrated is still debated, and probably more than one factor is. Histones are a strong candidate in *Xenopus*, zebrafish and *Drosophila*: maternal histones compete with transcription factors for DNA, and lowering the histone concentration advances ZGA while adding histones delays it. A second titration controls the cell cycle itself: the replication initiation factors Cut5 (TopBP1), RecQ4, Treslin and Drf1 are present in amounts that suffice for a limited quantity of DNA; once the DNA exceeds that quantity, origins fire less efficiently, S phase lengthens, the checkpoint kinase Chk1 is activated, and the cycle slows (panel B). In *Drosophila*, degradation of the maternal phosphatase Twine (Cdc25) and activation of Chk1 at cycle 14 add gap phases to the cycle.

Titration does not act alone. Pioneer transcription factors translated from maternal mRNA open chromatin at the first zygotic genes (Zelda in *Drosophila*; Pou5f3, Sox19b and Nanog in zebrafish); their accumulation is time-dependent rather than ratio-dependent. In the zebrafish the capacity of the nuclei to import transcription factors also rises as nuclear pore complexes mature during cleavage, and slowing pore maturation delays ZGA. The MZT is thus timed by several coupled mechanisms, some counting DNA and some measuring time.

**Example 5.2.1** With $R = 1000$ and $s$ chosen so that a diploid embryo reaches $r = 1$ at $n = 12$ (as in *Xenopus*), Formula 5.2.1 gives $S_{12} = 2(R - 1)$, so $p\,s\,2^{12} = 1998$ and $s \approx 0.244$. For a haploid embryo $S_n = 2(R-1)$ requires $2^n = 2 \times 2^{12}$, $n = 13$; for a tetraploid, $n = 11$. The fraction of free promoters rises from 0.1 to 0.9 within about one cycle on either side of the switch.

![Two titration models of the timing of the mid-blastula transition (schematic units). A: a maternal repressor of fixed total amount is bound by sites on the DNA, whose number doubles every cycle; the fraction of promoters free of repressor rises abruptly when the sites approach the repressor in number, one cycle later in haploid and one cycle earlier in tetraploid embryos. B: if a maternal replication factor can serve only a fixed amount of DNA, S phase and hence the cleavage cycle lengthen once the DNA content exceeds that capacity, again at a fixed ratio of DNA to cytoplasm](./plots/zga-titration.py)

## 5.3. Yolk and the Patterns of Cleavage

The pattern of cleavage depends on two properties of the egg: how much yolk it has and where the yolk lies, and the orientation of the spindles, which is set by factors in the egg cortex. The pole of the egg near which the polar bodies are given off is the *animal pole*; the opposite one, where yolk accumulates in yolky eggs, is the *vegetal pole*. A furrow that passes through both poles is *meridional*; one perpendicular to the animal–vegetal axis is *equatorial* (or latitudinal, if displaced from the equator).

**Definition 5.3.1 (Classes of Egg by Yolk)** An egg is **isolecithal** if it has little yolk, evenly distributed (sea urchins, amphioxus, mammals); **mesolecithal** if it has a moderate amount concentrated in the vegetal half (amphibians); **telolecithal** if dense yolk fills all of it except a small disc of cytoplasm at the animal pole (fishes, reptiles, birds, cephalopods); and **centrolecithal** if the yolk lies in the centre, surrounded by a thin layer of cytoplasm (insects).

**Definition 5.3.2 (Holoblastic and Meroblastic Cleavage)** Cleavage is **holoblastic** when the furrows divide the whole egg, and **meroblastic** when they divide only the yolk-free part of it. Meroblastic cleavage is **discoidal** when only a disc of cytoplasm on top of the yolk, the blastodisc, is divided, and **superficial** when nuclear divisions without cytokinesis produce a syncytium whose nuclei migrate to the periphery and are later enclosed in cells.

| Type | Pattern | Examples |
|---|---|---|
| Holoblastic, isolecithal or mesolecithal | radial: tiers of blastomeres stacked directly above each other | sea urchins, amphioxus; amphibians (displaced radial: the third furrow is shifted towards the animal pole) |
| | spiral: oblique spindles; each tier sits over the furrows of the one below, turned clockwise or anticlockwise | molluscs, annelids, nemerteans, polyclad flatworms (Spiralia) |
| | bilateral: the first furrow establishes the plane of bilateral symmetry | tunicates (ascidians) |
| | rotational: the two blastomeres of the 2-cell embryo divide in perpendicular planes | mammals, nematodes |
| Meroblastic, telolecithal | discoidal (radially in fish and birds, bilaterally in cephalopods) | teleost fishes, reptiles, birds |
| Meroblastic, centrolecithal | superficial | most insects |

![Yolk distribution and the main patterns of cleavage. Top: the four classes of egg by the amount and position of yolk (dots: yolk platelets). Middle: holoblastic patterns: radial (sea urchin, 8-cell, side view), displaced radial (frog), spiral (snail, 8-cell seen from the animal pole: the micromeres 1a–1d sit over the furrows between the macromeres A–D, turned clockwise), bilateral (ascidian, 8-cell seen from the vegetal pole, with the yellow crescent in the posterior pair). Bottom: rotational cleavage of mammals inside the zona pellucida, and the two meroblastic patterns, discoidal (furrows cut only the blastodisc) and superficial (syncytial nuclei in the cortex of a centrolecithal egg, with pole cells at the posterior end)](./plots/cleavage-patterns.py)

Yolk is not the whole story: closely related species with similar eggs can cleave differently, and the orientation of spindles is controlled by cortical cues such as those that make spiral cleavage turn right or left ([7.5.6](/7.5.6)). Cleavage pattern is nonetheless a reliable guide to where the cytoplasm of the egg ends up, and therefore to which blastomeres inherit localized determinants.

## 5.4. Cleavage in Non-Mammalian Model Species

### 5.4.1. Sea Urchins

The first two cleavages are meridional and the third equatorial, giving two tiers of four equal cells. At the fourth cleavage the animal tier divides meridionally into eight equal mesomeres, while the vegetal tier divides unequally and equatorially into four large macromeres and four small micromeres at the vegetal pole. At the fifth cleavage the micromeres divide unequally into large and small micromeres; at the sixth the macromeres divide into the tiers $\mathrm{veg}_1$ and $\mathrm{veg}_2$. By the seventh division the embryo is a hollow sphere of about 128 cells, one cell thick, each cell attached on its outer face to the hyaline layer and on its inner face to a basal lamina lining the blastocoel. The cells grow cilia, the blastula rotates inside the fertilization envelope, and cells of the animal hemisphere secrete a hatching enzyme that digests the envelope. The vegetal plate then thickens, the first sign of gastrulation. The fates of these tiers and the role of the micromeres as an organizer are the subject of [7.5.6](/7.5.6).

### 5.4.2. Amphibians

In *Xenopus* the first cleavage begins about 90 min after fertilization, and the next ones follow every 30 min or so. The furrow begins at the animal pole and advances slowly through the yolky vegetal cytoplasm, so that the second cleavage starts in the animal hemisphere before the first is complete in the vegetal one. The third cleavage is equatorial but displaced towards the animal pole, dividing the embryo into four small animal micromeres and four large vegetal macromeres; thereafter the animal cells divide faster and remain smaller. A cavity appears between the cells near the animal pole from the first cleavage onwards and enlarges into the blastocoel, which lies in the animal half of the blastula (figure in 5.4.5). The blastocoel has two functions. It provides the space into which cells move during gastrulation, and it keeps the cells of its roof, the animal cap, apart from the vegetal cells until the right time: when animal cap cells are taken from the roof and placed next to vegetal cells, they form mesoderm instead of ectoderm, because the vegetal cells induce mesoderm ([7.5.16](/7.5.16)). The MBT occurs at the end of the twelfth cycle. Before the first cleavage, the egg cortex rotates by about $30^\circ$ relative to the cytoplasm, away from the sperm entry point; this cortical rotation carries dorsal determinants to the side opposite the sperm entry point, which becomes dorsal ([7.5.16](/7.5.16)).

### 5.4.3. Zebrafish

After fertilization, cytoplasm streams towards the animal pole and forms a blastodisc on top of the yolk cell. The first five cleavages are vertical and meridional and divide only the blastodisc, producing a single layer of 32 cells in a $4 \times 8$ array; the sixth division is horizontal and makes the blastoderm two layers thick. The cycles last about 15 min until the MBT at cycle 10. At about the 512-cell stage the marginal cells of the blastoderm, which have remained open to the yolk cell, collapse into it and release their nuclei and cytoplasm, forming a ring of nuclei within the yolk cell, the yolk syncytial layer (YSL). By the MBT the blastoderm contains three populations:

- the YSL, which spreads under the blastoderm (internal YSL) and stays at its margin (external YSL); it secretes signals that induce mesoderm and endoderm in the overlying cells and provides much of the force for epiboly ([7.5.9](/7.5.9));
- the enveloping layer (EVL), a squamous epithelium one cell thick on the surface, which forms the periderm, a protective covering lost later;
- the deep cells between them, which form the embryo proper.

The deep cells are not yet committed at the MBT; their fates are established during the late blastula and gastrula stages. The blastoderm then thins and begins to spread over the yolk: epiboly, the first movement of gastrulation.

### 5.4.4. Birds

The hen's egg is fertilized in the infundibulum of the oviduct, and cleavage proceeds during the roughly 20 h the egg spends acquiring albumen, shell membranes and shell. The blastodisc, 2–3 mm across, is divided by meridional furrows that do not cut into the yolk; the central cells are thus at first open to the yolk underneath. Later equatorial and vertical divisions make a blastoderm about four cells thick, and the switch to zygotic transcription occurs at about the seventh or eighth division. Fluid secreted between the blastoderm and the yolk forms the subgerminal cavity. The central cells shed their deepest layer, leaving a translucent area pellucida one cell thick over the cavity, which will form most of the embryo; the peripheral ring, still attached to the yolk, is the opaque area opaca. When the egg is laid, the blastoderm contains about 50 000 cells. Shortly afterwards a thickening of the epiblast, Koller's sickle, forms at the posterior edge of the area pellucida, and cells delaminate from the epiblast to form scattered hypoblast islands; a sheet growing forwards from Koller's sickle joins them into a continuous hypoblast. The embryo proper comes entirely from the epiblast; the hypoblast forms extraembryonic tissues and positions the primitive streak ([7.5.9](/7.5.9), [7.5.16](/7.5.16)). The anterior–posterior polarity of the blastoderm is set while the egg rotates in the oviduct: the side that is uppermost as the egg tilts under gravity becomes posterior.

### 5.4.5. *Drosophila*

The zygote nucleus lies in the middle of a centrolecithal egg. The first nine nuclear divisions take about 8 min each and are not followed by cytokinesis, producing a syncytium; at nuclear cycle 8 the nuclei begin to migrate to the cortex, and by cycle 10 most lie in the periphery, forming the syncytial blastoderm. A few nuclei that reach the posterior pole earlier, at cycle 9, are enclosed in cells at once: the pole cells, the germ line, whose fate depends on the **pole plasm** ([7.5.14](/7.5.14), [7.5.27](/7.5.27)). A few nuclei stay in the yolk as yolk nuclei. Four more divisions take place in the cortex, slowing progressively (cycle 13 lasts about 25 min). In the interphase of cycle 14, after 13 nuclear divisions, the plasma membrane grows inwards between the nuclei in two phases, a slow one until the furrow canals pass the nuclei and a fast one after, enclosing about 6000 nuclei in cells: this cellularization takes about an hour and is complete about 3 h after fertilization. Because the nuclei share a cytoplasm until then, transcription factors made from maternal mRNA can diffuse between nuclei and form concentration gradients, such as that of Bicoid: this is **syncytial specification** ([7.5.1](/7.5.1), [7.5.11](/7.5.11), [7.5.14](/7.5.14)).

![Blastulae of the model species in section, coloured by the germ layer each region will form (animal pole up). Sea urchin: a hollow sphere one cell thick inside the hyaline layer, with a thickened vegetal plate. Frog: a multilayered animal cap over a blastocoel displaced towards the animal pole, the marginal zone (prospective mesoderm) and large yolky vegetal cells (prospective endoderm). Zebrafish: the blastoderm on the yolk cell, covered by the enveloping layer, with the yolk syncytial layer between deep cells and yolk. Chick: the area pellucida over the subgerminal cavity, the area opaca on the yolk, hypoblast islands, and Koller's sickle at the posterior edge. *Drosophila*: the cellular blastoderm around the yolk, with the pole cells at the posterior end. Mouse: the blastocyst, with the inner cell mass divided into epiblast and primitive endoderm](./plots/blastulae.py)

## 5.5. The Formation of the Blastocoel: A Lattice Energy Model

The formation of the blastocoel is the earliest change of form in development and makes a good first example of a mechanical model. The question is why a cleaving egg stops being a solid ball of cells, a morula, and becomes a hollow sphere; and why this happens almost at once and gradually in sea urchins, but late and suddenly in mammals.

### 5.5.1. Two Mechanisms

Two mechanisms have been proposed for the sea urchin, both relying on the attachment of the blastomeres to the hyaline layer that coats the egg. In Dan's osmotic theory the blastomeres secrete macromolecules into the intercellular space, which then takes up water osmotically and pushes the cells, held by the hyaline layer, outwards. In the theory of Gustavson and Wolpert the decisive factor is adhesion: if the cells adhere more strongly to the hyaline layer than to one another, then as they become smaller during cleavage they stay in a single layer spread over the layer, the surface of the layer, and hence the egg, expands, and fluid enters passively. The expansion need not be large: a spherical shell between radii 4 and 5 contains about the same volume as a ball of radius 4. Both mechanisms have a basis in later work. Vertebrate and mammalian blastocoels are inflated by ion pumping: the outer epithelium, sealed by **tight junctions**, transports $\mathrm{Na}^+$ inwards through basolateral $\mathrm{Na}^+/\mathrm{K}^+$-ATPases, and water follows through **aquaporins**. In the mouse, the fluid first accumulates in hundreds of micrometre-sized lumens between the cells, which coarsen into one cavity by a process resembling the ripening of bubbles; the cells that line the cavity have the weakest mutual contacts. Adhesion and its asymmetry determine where the cavity forms, osmotic pressure inflates it. The model below captures the adhesion side.

### 5.5.2. Quasi-Static Equilibrium

We describe the embryo by the cell occupation $\nu_x$ of sites $x$ of a lattice with spacing $a$ of about one cell diameter: $\nu_x = 1$ if a cell is at $x$ and $0$ otherwise. We assume quasi-static equilibrium: the configuration is governed by an energy $E(\{q_\alpha\}, t)$ of the dynamical variables $q_\alpha$, whose explicit time dependence, through slowly changing parameters such as the adhesiveness of the cells, is slow compared with the dynamics. Whatever the dynamics, Newtonian ($\ddot q_\alpha = F_\alpha/m_\alpha$), dominated by drag ($\dot q_\alpha = F_\alpha/\gamma_\alpha$) or unknown, the system then stays at a state where the generalized forces $F_\alpha = -\partial E/\partial q_\alpha$ vanish. Such a state is stable only if a fluctuation does not grow, which for these dynamics requires $\sum_{\alpha\beta} (\partial^2 E/\partial q_\alpha\partial q_\beta)\,\mathrm{d}q_\alpha\,\mathrm{d}q_\beta \ge 0$: $E$ must be at a local minimum.

The energy has four parts:

- adhesion of the cells to the hyaline layer at the boundary, $E_{\mathrm{bd}} = -\gamma\sum_{x \in \mathrm{bd}} \nu_x$;
- adhesion between neighbouring cells, $E_{\mathrm{int}} = -\tfrac{1}{2} J \sum_{\langle x, y\rangle} \nu_x\nu_y$, where the sum is over ordered pairs of nearest neighbours (hence the factor $\tfrac12$) and $J$ is the mean adhesion energy of a contact;
- the constraint that the number of cells is fixed, $\sum_x \nu_x = N$, entered with a Lagrange multiplier $\lambda$ as $E_N = \lambda\left(\sum_x \nu_x - N\right)$;
- fluctuations. Cells move autonomously, contacts vary, and embryos differ; as in thermodynamics, the energy not available to the organized forces is accounted for by an entropy term at an effective temperature $T$,
  $$
  E_T = T\sum_x \bigl[\rho_x\ln\rho_x + (1 - \rho_x)\ln(1 - \rho_x)\bigr],
  $$
  where $\rho_x = \langle\nu_x\rangle$ is now the mean occupation, no longer restricted to $0$ and $1$.

Expanding $E_T$ about its minimum at $\rho = \tfrac12$ in the variable $\sigma_x = 2\rho_x - 1$, which runs from $-1$ (no cell) to $1$ (cell), gives $E_T = T\sum_x(\tfrac12\sigma_x^2 + \tfrac1{12}\sigma_x^4 + \cdots)$ up to a constant. Taking $T$ as the unit of energy and writing $c$ for the number of neighbours of a site, the total energy becomes, up to a constant,

$$
E = \sum_x\left[\frac{1}{12}\sigma_x^4 + \frac12\sigma_x^2 + \left(\frac{\lambda}{2} - \frac{Jc}{4}\right)\sigma_x\right] - \frac{J}{8}\sum_{\langle x,y\rangle}\sigma_x\sigma_y - \frac{\gamma}{2}\sum_{x \in \mathrm{bd}}\sigma_x.
\tag{5.2}
$$

This is the energy of an Ising model of magnetism with a soft spin, which is where the name "spin" for $\sigma$ comes from. Because of the truncated expansion, $\sigma$ is no longer bounded by $\pm1$; its sign indicates whether a cell is more or less likely than not at $x$.

### 5.5.3. Local Theory: The Cusp

Suppose first that the density can adjust locally, away from the boundary, in a region of uniform $\sigma$. Using $\sum_{\langle x,y\rangle}\sigma_x\sigma_y = c\sum_x\sigma^2$ for uniform $\sigma$, the energy per site is

$$
E(\sigma) = \frac{1}{12}\sigma^4 + \left(\frac12 - \frac{Jc}{8}\right)\sigma^2 + \left(\frac{\lambda}{2} - \frac{Jc}{4}\right)\sigma
= \frac{1}{12}\sigma^4 + \frac{u}{2}\sigma^2 + \frac{v}{3}\sigma,
\tag{5.3}
$$
with control parameters $u = 1 - Jc/4$ and $v = 3(\lambda/2 - Jc/4)$.

**Proposition 5.5.1 (Regimes of Blastulation)** The local energy (5.3) has a single minimum if $4u^3 + v^2 > 0$ and two minima separated by a maximum if $4u^3 + v^2 < 0$. In particular, if adhesion is weak ($Jc/4 < 1$, so $u > 0$), there is always one minimum; if it is strong ($u < 0$), there are two for $\lvert v\rvert < 2(-u)^{3/2}$. The lower minimum lies at negative $\sigma$ (cavity) when $v > 0$, that is when $\lambda/2 > Jc/4$, and at positive $\sigma$ (cells) when $v < 0$.

**Proof** The stationary points solve $E'(\sigma) = \tfrac13\sigma^3 + u\sigma + \tfrac13 v = 0$, a cubic $\sigma^3 + 3u\sigma + v = 0$ whose discriminant is $-27(4u^3 + v^2)$: three real roots (two minima and a maximum, since the leading coefficient of $E$ is positive) if $4u^3 + v^2 < 0$, one real root (a minimum) if $4u^3 + v^2 > 0$. Two roots coalesce, and $E''(\sigma) = \sigma^2 + u = 0$ together with $E' = 0$, exactly on the curve $v^2 + 4u^3 = 0$. If $u > 0$ then $4u^3 + v^2 > 0$ for every $v$. Finally, the linear term $\tfrac13 v\sigma$ lowers the energy of the minimum whose $\sigma$ has the sign opposite to $v$. $\square$

The curve $v^2 + 4u^3 = 0$ is the bifurcation set of the **cusp catastrophe**, which we meet again in its general form in [7.5.10](/7.5.10). The Lagrange multiplier $\lambda$, which measures how strongly the fixed number of cells must be accommodated, grows as cleavage proceeds and the cells shrink; $J$ may fall as cells become less adhesive. An embryo therefore moves through the $(u, v)$ plane in the direction of increasing $v$. If $u > 0$ throughout, the interior density decreases continuously through zero and the cavity forms gradually, as in the sea urchin. If $u < 0$, the embryo must cross the wedge in which two states coexist; it stays in the cellular minimum until that minimum disappears at the far edge of the wedge, and then jumps to the cavity state, a sudden change that would describe the mammalian embryo (figure in 5.5.4, panels B and C). Where exactly the jump occurs depends on how the system chooses between coexisting minima, a question taken up in [7.5.10](/7.5.10): at the edge of the wedge if it stays in its minimum as long as that exists (the delay convention), at $v = 0$ if it always occupies the global minimum (the Maxwell convention). The same picture shows that the initial state may change abruptly in evolution, as parameters drift across the cusp.

### 5.5.4. Global Theory: The Wall Profile

The density is not uniform: the boundary is held at $\sigma = 1$ by adhesion to the hyaline layer, and the interior adjusts. Using
$$
-\sum_{\langle x,y\rangle}\sigma_x\sigma_y = \frac12\sum_{\langle x,y\rangle}(\sigma_x - \sigma_y)^2 - c\sum_x\sigma_x^2,
$$
the energy (5.2) with $\sigma = 1$ on the boundary becomes

$$
E = \sum_x\left[\frac{1}{12}\sigma_x^4 + \left(\frac12 - \frac{Jc}{8}\right)\sigma_x^2 + \left(\frac{\lambda}{2} - \frac{Jc}{4}\right)\sigma_x\right] + \frac{J}{16}\sum_{\langle x,y\rangle}(\sigma_x - \sigma_y)^2.
$$

The last term is a positive energy paid wherever the density changes, a surface tension that results from broken cell–cell contacts ([7.5.7](/7.5.7)). Setting $\partial E/\partial\sigma_x = 0$ gives $E'(\sigma_x) = \tfrac{J}{4}\sum_y(\sigma_y - \sigma_x)$, the sum over the $c$ neighbours $y$ of $x$. For a slowly varying field, expanding $\sigma_y$ about $x$ and using that the average over the neighbours of $(y - x)\cdot\boldsymbol{w}$ vanishes and that of $((y-x)\cdot\boldsymbol{w})^2$ is $\tfrac13 a^2\lvert\boldsymbol{w}\rvert^2$, the right-hand side becomes a Laplacian:

**Formula 5.5.1 (Continuum Equation of the Blastula)** In the continuum limit the cell density obeys

$$
E'(\sigma) = \frac{J a^2 c}{12}\,\nabla^2\sigma,
\tag{5.4}
$$
with $E$ the local energy (5.3) and $\sigma = 1$ on the surface of the egg.

Equation (5.4) is the Euler–Lagrange equation ([2.4.13](/2.4.13)) of the functional $\int\bigl[E(\sigma) + \tfrac{1}{24}Ja^2c\lvert\nabla\sigma\rvert^2\bigr]\,\mathrm{d}V$, the continuum version of the energy. Suppose $\sigma$ varies only with the radius and treat the problem as one-dimensional (this fails near the centre, but the profile has usually levelled off by then). Multiplying $E'(\sigma) = \tfrac{1}{12}Ja^2c\,\sigma''$ by $\sigma'$ and integrating gives a **first integral** ([2.4.14](/2.4.14))

$$
\frac{J a^2 c}{24}\left(\frac{\mathrm{d}\sigma}{\mathrm{d}r}\right)^2 - E(\sigma) = K.
\tag{5.5}
$$

The constant $K$ is fixed by the interior: we ask that $\sigma$ level off, $\mathrm{d}\sigma/\mathrm{d}r \to 0$, deep inside, which requires $K = -E(\sigma_{\min})$ at a minimum of $E$. The depth below the surface at which the density has fallen to $\sigma$ is then

$$
d(\sigma) = \ell\int_\sigma^1\frac{\mathrm{d}s}{\sqrt{E(s) - E(\sigma_{\min})}},
\qquad \ell = \left(\frac{Ja^2c}{24}\right)^{1/2}.
$$

The global picture repeats the local one. In the single-minimum regime the density falls from 1 at the surface to the interior minimum within a few adhesion lengths $\ell$: a thin shell of cells over a cavity, which deepens continuously as $\lambda$ increases. In the two-minimum regime, when the minimum near $\sigma = 1$ is only slightly higher than the cavity minimum, the profile stays close to the cellular state for a long distance before dropping: a thick shell, which becomes a thin one when the cellular minimum disappears (figure below, panel D). What matters globally, as locally, is the position of the control parameters relative to the singular set in the $(J, \lambda)$ plane.

**Proposition 5.5.2 (The Multiplier Is Fixed Variationally)** Let $E(\lambda) = \min_q\,[E_0(q) + \lambda g(q)]$, where $g = 0$ expresses a constraint (here, the number of cells). If $\lambda$ is chosen so that $\mathrm{d}E/\mathrm{d}\lambda = 0$, the minimizer satisfies the constraint, and $E$ is then also stationary with respect to $\lambda$.

**Proof** At the minimizer $q(\lambda)$, $\partial(E_0 + \lambda g)/\partial q_\alpha = 0$. Hence $\mathrm{d}E/\mathrm{d}\lambda = g + \sum_\alpha(\partial(E_0 + \lambda g)/\partial q_\alpha)(\mathrm{d}q_\alpha/\mathrm{d}\lambda) = g$, so $\mathrm{d}E/\mathrm{d}\lambda = 0$ is equivalent to $g = 0$. $\square$

The radius $R$ of the egg is itself a variable: $\lambda$ depends on $R$, and the equilibrium requires $\partial E/\partial R = \partial E/\partial\lambda = 0$. The control variables $J$, $N$ and $\gamma$ therefore determine $\lambda$ and $R$, which in turn control the cell distribution. A crude estimate shows the dependence. Let the cells occupy a thin shell of thickness $d$ at radius $R$, of fixed total volume $2\pi V = \tfrac12\cdot 4\pi R^2 d$, so $R^2 d = V$; let the adhesion to the hyaline layer contribute $-\gamma R^2$ and the gradient energy, of order $1/d^2$ per unit volume, $VJ/d^2$. Eliminating $d$,

$$
\Delta E = -\gamma R^2 + \frac{VJ}{d^2} = \frac{J}{V}\left(R^4 - \frac{\gamma V}{J}R^2\right),
$$
which is minimal at $R = (\gamma V/2J)^{1/2}$: the stronger the adhesion to the hyaline layer relative to cell–cell adhesion, the larger the blastula. This is the degenerate case $v = 0$ of the quartic (5.3) in the variable $R$, degenerate because of the radial symmetry; in the variable $R^2$ it is an ordinary quadratic minimization with no control parameters at all.

![The lattice energy model of blastocoel formation. A: the local energy density E(σ) of the coarse-grained cell density (σ = 1: cell, σ = −1: cavity), with one minimum for weak adhesion (u > 0) and two for strong adhesion (u < 0); a positive cavity bias v lowers the cavity minimum. B: the control plane; inside the cusp v² + 4u³ = 0 two minima coexist. A weakly adhesive embryo crosses v = 0 smoothly (gradual cavitation, sea urchin); a strongly adhesive one crosses the bistable wedge (sudden cavitation, mammal). C: the interior density at a minimum along the two paths: continuous for u > 0, an S-shaped curve with a jump for u < 0, at the edge of the wedge under perfect delay or at v = 0 under the Maxwell convention. D: radial profiles from the first integral (5.5), with σ = 1 held at the surface: a thin shell of cells over a cavity, and, for nearly equal minima, a thick shell that empties slowly](./plots/blastocoel-landau.py)

### 5.5.5. What the Model Shows

The model is deliberately crude: it ignores the shapes of cells, osmotic pressure, and the fact that cell number changes. Its value lies in three general lessons that recur through the course. First, a continuous change of parameters can produce either a continuous or a sudden change of form, depending on where the parameters lie relative to a singular set; such qualitative statements survive changes in the details of the model ([7.5.10](/7.5.10)). Second, a local energy with a gradient penalty gives interfaces of finite thickness, set by the ratio of interaction to local energy; the same structure underlies the Cahn–Hilliard description of cell sorting ([7.5.7](/7.5.7)). Third, constraints such as a fixed number of cells enter as Lagrange multipliers whose values are themselves determined by the equilibrium. Whether a given embryo is in the gradual or the sudden regime is an empirical question that the model poses but cannot answer.

## 5.6. Mammalian Cleavage and the First Lineage Decisions

### 5.6.1. Rotational Cleavage and Compaction

Mammalian cleavage is slow, 12–24 h per division, and takes place as the embryo is moved along the oviduct towards the uterus over several days, inside the zona pellucida. The zygotic genome is activated early (5.2.2), so most of cleavage is under zygotic control. The cleavage is rotational: the first division is meridional, and at the second one blastomere divides meridionally and the other equatorially. The divisions are not synchronous, so embryos with odd numbers of cells are common, and blastomeres differ in size; human 2-cell embryos often have blastomeres of unequal size.

**Definition 5.6.1 (Compaction, Morula)** **Compaction** is the flattening of the blastomeres of a mammalian embryo against one another, at the 8-cell stage in the mouse and at about the 8- to 16-cell stage on day 4 in humans, driven by E-**cadherin**-mediated adhesion and actomyosin contractility, which turns a loose cluster of round cells into a tightly packed ball. The compacted embryo before a cavity forms is the **morula**.

Compaction does three things. It makes each outer cell polar: the contact-free, outer surface acquires an apical domain containing the Par3–Par6–aPKC complex (**PAR proteins**, [7.3.15](/7.3.15)) and microvilli, while the surfaces in contact with other cells become basolateral. It seals the outer cells together by **tight junctions**, forming an epithelium that can later pump fluid; and **gap junctions** connect the cells inside. And it creates two positions, inside and outside, in the next divisions: an outer polar cell that divides with its spindle parallel to the surface gives two outer polar cells, while one that divides perpendicular to it gives an outer polar and an inner apolar cell.

### 5.6.2. The First Decision: Inner Cell Mass and Trophectoderm

**Definition 5.6.2 (Blastocyst, Inner Cell Mass, Trophectoderm)** The **blastocyst** is the mammalian blastula: a fluid-filled cavity (the blastocoel) surrounded by the **trophectoderm**, an epithelium of outer cells that will form the fetal part of the placenta and other extraembryonic tissues, with the **inner cell mass** (ICM), a cluster of inner cells attached to the trophectoderm at one pole, from which the embryo proper and some extraembryonic tissues form. The trophectoderm over the ICM is polar, the rest mural.

In the mouse the blastocyst forms at about embryonic day 3.5 (32–64 cells); in humans on day 5 (about 100–200 cells). How do cells choose between the two fates? Three hypotheses have been proposed (table below).

| Hypothesis | Claim | Evidence |
|---|---|---|
| Prepattern | the egg or the 2-cell embryo is already patterned; blastomeres differ in their tendency to contribute to ICM or trophectoderm | in some studies the blastomere of the 2-cell embryo that divides first, or the one attached to the second polar body, contributes preferentially to the ICM; at the 4-cell stage, blastomeres differ in the level of histone arginine methylation (CARM1) and in the kinetics of Sox2 binding, and those with more CARM1 contribute more to the ICM |
| Inside–outside | cells become ICM or trophectoderm according to whether they lie inside or outside | in aggregation chimeras, blastomeres placed inside form ICM and those outside form trophectoderm, whatever their origin; isolated inner cells re-form trophectoderm on their exposed surfaces |
| Polarity | the decision follows the inheritance of the apical domain: cells that inherit it become trophectoderm | outer polar cells express Cdx2; experimentally removing the apical domain or blocking aPKC makes outer cells adopt ICM characteristics |

The three hypotheses are now seen as aspects of one mechanism (figure below). The apical domain of outer cells sequesters angiomotin away from the adherens junctions; without it, the Hippo kinases LATS1/2 are inactive, the co-activator **YAP** enters the nucleus and, with the transcription factor TEAD4, activates *Cdx2* and *Gata3*, which specify trophectoderm and repress *Oct4* (*Pou5f1*) and *Sox2*. In inner cells, surrounded by contacts on all sides, angiomotin at the junctions activates LATS, which phosphorylates YAP and keeps it in the cytoplasm; Sox2 and Oct4 remain, and the cells form the ICM (the **Hippo pathway**, [7.3.22](/7.3.22)). Position is read through polarity, and polarity through the Hippo pathway. Early biases, if they exist, act by influencing the orientation of divisions, and thus which cells end up inside; they do not commit cells, as the regulative capacity of the embryo shows: a single blastomere of a 2-cell or 4-cell mouse embryo can form a complete blastocyst, and cells moved inside or outside change fate until about the 32-cell stage.

**Example 5.6.1 (Chimeras Test Position)** Disaggregate two 8-cell mouse embryos of different genotypes, one carrying a ubiquitous marker, and reaggregate them so that the marked cells are placed either in the centre or on the surface of the composite. If fate follows ancestry, the marked cells should contribute to ICM and trophectoderm in proportion to their number whatever their placement; if fate follows position, centrally placed cells should end up mostly in the ICM. The second result is observed. The design isolates the variable in question (position) while holding the cells' history fixed, and the use of a heritable marker lets the outcome be read at the blastocyst stage.

![The first lineage decision of the mammalian embryo (mouse, 16- to 32-cell stage). Left: a compacted morula in section. Outer cells carry an apical domain (Par6–aPKC, purple) on their free surface; in them the Hippo kinase LATS is inactive, YAP is nuclear and, with TEAD4, activates Cdx2: they become trophectoderm (pink). Inner cells have no apical domain; angiomotin at their junctions (dots) activates LATS, phosphorylated YAP stays in the cytoplasm, and Sox2 and Oct4 persist: they form the inner cell mass (green). Right: the pathway that reads position through polarity](./plots/first-lineage-decision.py)

### 5.6.3. The Second Decision: Epiblast and Primitive Endoderm

Between the 32- and the roughly 100-cell stage, the ICM divides into two populations: the epiblast, which will form the whole embryo (and the amnion and extraembryonic mesoderm), and the primitive endoderm, a layer facing the blastocoel that forms the extraembryonic endoderm of the yolk sac. The decision does not follow position. Early ICM cells co-express the epiblast transcription factor Nanog and the primitive endoderm factor Gata6; over the next divisions the two become mutually exclusive in a random, salt-and-pepper mixture of cells, and only then do the Gata6 cells sort out to the surface of the ICM, by differential adhesion and movement ([7.5.7](/7.5.7)), and die if they fail to. The ratio of the two fates is nonetheless reproducible, about two epiblast cells to three primitive endoderm cells in the mouse at E4.5. Experiments identify the signal that sets it: FGF4, secreted by epiblast cells and received through FGFR1 and FGFR2 and the ERK pathway, is required for primitive endoderm. In *Fgf4* null embryos, or when FGFR or MEK is inhibited, all ICM cells become epiblast; with enough exogenous FGF4, all become primitive endoderm.

**Formula 5.6.1 (Nanog–Gata6 Switch with FGF4 Feedback)** For inner cell $i$, with Nanog $N_i$ and Gata6 $G_i$ in units of their repression thresholds and time in units of the protein lifetime,

$$
\frac{\mathrm{d}N_i}{\mathrm{d}t} = \frac{\alpha}{(1 + G_i^h)(1 + (E_i/K_E)^2)} - N_i,
\qquad
\frac{\mathrm{d}G_i}{\mathrm{d}t} = \frac{\alpha\,(\beta + E_i^2/(1 + E_i^2))}{1 + N_i^h} - G_i,
$$
where $E_i = \sum_j A_{ij}N_j + F$ is the FGF/ERK signal received by cell $i$ from its neighbours $j$ (the matrix $A_{ij}$ averages over cells in contact, since FGF4 is made in proportion to Nanog) plus any exogenous FGF4 $F$, and $\alpha$, $\beta$, $h$, $K_E$ are constants.

Each cell is a **bistable** toggle switch ([7.3.18](/7.3.18)): mutual repression of Nanog and Gata6 with cooperativity $h > 1$ gives two stable states, Nanog-high and Gata6-high. The coupling makes the choice of each cell depend on its neighbours: a cell that drifts towards Nanog sends more FGF4 to its neighbours and pushes them towards Gata6, a form of lateral inhibition that produces a mixture and, because the feedback is negative at the level of the population, regulates its composition. If too many cells become epiblast, FGF4 rises and converts some of the undecided ones, and vice versa. With $\alpha = 2$, $\beta = 0.25$, $h = 3$, $K_E = 1.2$ and weak noise, the model reproduces the mixture, the proportion, and the effects of removing or adding FGF4 (figure below). The same structure explains why the proportion is restored after cells of one type are killed by laser ablation in the ICM. A cell cycle lengthening, the decline of FGF responsiveness with time and the inheritance of states through divisions refine the picture in more detailed models.

![A model of the epiblast–primitive endoderm decision (Formula 5.6.1). A: the network: Nanog and Gata6 repress each other; Nanog cells secrete FGF4, which acts on their neighbours through FGFR and ERK, activating Gata6 and repressing Nanog. B: an inner cell mass of 26 cells after the decision (lines join cells in contact): a salt-and-pepper mixture of epiblast (green) and primitive endoderm (yellow). C: Nanog and Gata6 in every cell over time: the co-expressing state resolves into two classes. D: the fraction of primitive endoderm against FGF4 added to the medium, for wild-type ICMs and ICMs making no FGF4 (Fgf4 null; five simulations per point): without FGF4 all cells become epiblast, and enough exogenous FGF4 converts all of them, as in the experiments](./plots/epiblast-pre-switch.py)

### 5.6.4. Hatching and Implantation

Fluid pumped by the trophectoderm expands the blastocoel (5.5.1). The expanded blastocyst then hatches: it escapes from the zona pellucida through a hole made by trophectoderm proteases (strypsin, or implantation serine protease, in the mouse) and by the expansion itself. The zona has kept the embryo from sticking to the wall of the oviduct; once it is gone, the trophectoderm can adhere to and invade the uterine epithelium.

**Definition 5.6.3 (Implantation)** **Implantation** is the attachment of the blastocyst to the uterine epithelium and its invasion of the uterine wall, which transforms into decidua. It begins on day 6–7 in humans, with the polar trophectoderm over the ICM making the first contact, and at E4.5 in the mouse, with the mural trophectoderm opposite the ICM attaching first.

Trophoblast invasion forms the placenta, which is described with gastrulation in [7.5.9](/7.5.9). Two departures from the normal sequence have clinical and biological interest.

- Ectopic pregnancy: if the blastocyst hatches and implants before reaching the uterus, most often in the oviduct (about 1–2 % of human pregnancies), the trophoblast invades a wall that cannot support a pregnancy; such pregnancies rarely survive more than a few weeks and can rupture the tube with life-threatening bleeding. Risk factors are those that slow transport along the oviduct, such as scarring after infection. Implantation in the abdominal cavity, rare and dangerous, shows that the trophoblast can invade many tissues.
- Delayed implantation (embryonic diapause): in more than a hundred mammals, including mice during lactation, roe deer, mink, seals and bears, the blastocyst stops dividing and floats in the uterus for days to months before implanting, so that birth falls in a favourable season. The arrest is controlled by the mother's hormones and the uterine environment: in mink, low prolactin from the pituitary reduces the polyamines made by the uterus, and restoring polyamines reactivates the blastocysts; in mice, mTOR inhibition and reduced MYC activity in the embryo maintain the dormant state. The giant panda illustrates the consequence: pregnancies last 80–200 days but the fetus develops for only about 45–60 days after a delay of variable length, and the newborn weighs about 100 g (50–150 g), roughly one thousandth of its mother's weight.

**Definition 5.6.4 (Delayed Implantation)** **Delayed implantation**, or embryonic diapause, is a reversible arrest of the blastocyst before implantation, under maternal control, which lengthens gestation without lengthening embryonic development.

## 5.7. Clinical Aspects of Early Development

### 5.7.1. Early Pregnancy Loss

Most human conceptions fail. Of embryos that reach the uterus, perhaps a third or more are lost before the pregnancy is recognized; about 15–20 % of clinically recognized pregnancies end in spontaneous miscarriage (loss before 20 weeks), more than 80 % of them before 12 weeks, after which the risk is low. About half of first-trimester miscarriages have a chromosomally abnormal embryo, most often a trisomy, triploidy or monosomy X, arising mostly from errors of female meiosis whose frequency rises steeply with maternal age (**aneuploidy**, [7.4.16](/7.4.16)); aneuploidy is also common in cleavage-stage embryos themselves, because the first mitoses are error-prone. Other causes are uterine abnormalities and adhesions, cervical insufficiency, uncontrolled diabetes and thyroid disease, the antiphospholipid syndrome, and infections (rubella, cytomegalovirus, *Listeria*, parvovirus B19). Recurrent miscarriage, three or more losses, is in a few percent of couples due to a balanced translocation in one parent, which produces unbalanced gametes ([7.4.15](/7.4.15)). The classes of 5.2.1 matter here: losses caused by a mother's maternal-effect mutation will recur with any partner and cannot be prevented by selecting embryos.

### 5.7.2. Twins and Chimeras

The regulative ability of the early mammalian embryo is shown by twins. Dizygotic twins come from two eggs fertilized by two sperm; monozygotic twins from one embryo that separates into two.

**Definition 5.7.1 (Monozygotic Twins)** **Monozygotic twins** are two individuals developed from a single zygote whose cells separated into two groups, each of which formed a complete embryo; they are genetically identical except for postzygotic mutations.

Monozygotic twins occur in about 3–4 of every 1000 births, with little variation among populations. The extraembryonic membranes they share indicate when the separation happened, because the membranes form in a fixed order: the trophectoderm, which forms the chorion, by day 5, the amnion by about day 8–9 (figure below). About a third have two chorions and two amnions, consistent with separation of blastomeres before day 5; about two thirds share one chorion but have two amnions, consistent with division of the ICM within one blastocyst; about 1 % share a single amnion, consistent with division of the embryonic disc after day 9; and incomplete separation of the axis, around the time of gastrulation, gives conjoined twins, about once in 200 000 live births. Conjoined twins are always of the same sex. Two caveats qualify this classical scheme. Splitting a human embryo before the blastocyst stage is not known to occur naturally, and some dichorionic monozygotic twins may arise later, for instance by the separation of an ICM that later forms two trophoblast vesicles; and twinning after in vitro fertilization, where blastocysts are often transferred after zona manipulation, is several times more frequent and often monochorionic. Some monochorionic twin pairs have been shown to be dizygotic, the two embryos having fused at the blastocyst stage; these are chimeras. Nature makes monozygotic multiples routinely in the nine-banded armadillo, whose single embryo divides after implantation into four, so that every litter consists of identical quadruplets.

![Monozygotic twins and the time of separation (classical interpretation). Separation of blastomeres before the trophectoderm forms gives two chorions and two amnions (dichorionic, about a third of monozygotic twins); division of the inner cell mass gives one chorion and two amnions (about two thirds); division of the embryonic disc after the amnion forms gives one chorion and one amnion (about 1 %); incomplete division later gives conjoined twins](./plots/twinning.py)

The converse of twinning is a **chimera** ([7.4.20](/7.4.20)), an individual made of cells of two zygotes. Mouse chimeras are made by aggregating two morulae or by injecting cells into a blastocyst; they develop normally and have been essential for analysing cell autonomy and for making mice from genetically modified **embryonic stem cells** ([7.3.24](/7.3.24), [7.5.36](/7.5.36)). Embryonic stem cells are derived from the ICM; they are pluripotent, able to form all three germ layers and germ cells, but not trophectoderm. Human chimeras arise naturally from the fusion of dizygotic embryos and occasionally come to attention as individuals with both XX and XY cells, or with two blood types. Interspecies chimeras, such as rat cells in mouse blastocysts or human cells in pig embryos, are being studied as a way to grow human organs; the very low contribution of human cells so far and the ethical problems they raise keep them experimental. Xenotransplantation of human cancer cells into zebrafish embryos, which lack an adaptive immune system at that stage, is used to follow metastasis.

### 5.7.3. Assisted Reproduction

*In vitro fertilization* (IVF), developed by Robert Edwards and Patrick Steptoe (first birth 1978; Nobel Prize to Edwards in 2010), consists of ovarian stimulation, collection of oocytes, fertilization in culture, culture of the embryos for 2–5 days and transfer of one or two embryos to the uterus. Current practice favours the transfer of a single blastocyst on day 5, which reduces multiple pregnancy, and the freezing of the other embryos for later transfer; transfers of frozen embryos into a cycle not disturbed by ovarian stimulation give pregnancy rates as good as or better than fresh transfers. Intracytoplasmic sperm injection (ICSI) injects a single sperm into the egg and overcomes most forms of male infertility. In livestock the same techniques, with embryo splitting at the morula or blastocyst stage, are used to multiply valuable animals and to conserve rare ones; split embryos give smaller offspring and more abnormalities.

**Preimplantation genetic testing** (PGT; **preimplantation genetic diagnosis** in older usage) analyses cells removed from embryos and selects unaffected ones for transfer. Three kinds are distinguished: PGT-M for monogenic disorders, PGT-SR for structural rearrangements, and PGT-A for aneuploidy. Cells can be taken from the polar bodies (which reveal only the maternal contribution), from a blastomere of the 8-cell embryo, or, now most commonly, from the trophectoderm of a blastocyst; the last removes five to ten cells that would not form the embryo and gives more DNA. Three limitations follow from the biology of this chapter. Biopsy is invasive, and studies in mice report long-term effects of blastomere biopsy on weight and behaviour, a reason to prefer trophectoderm biopsy. Many cleavage-stage embryos are mosaic for aneuploid and euploid cells, and trophectoderm cells need not represent the ICM, so a single biopsy can misclassify an embryo; mosaic embryos transferred after counselling often result in healthy births. And PGT-A has not been shown to raise the cumulative live-birth rate per started IVF cycle in most groups of patients. Non-invasive testing of DNA released into the culture medium, and image analysis of embryo development by machine learning, are being evaluated as alternatives.

## Summary

| Topic | Main points |
|---|---|
| Cleavage (Definition 5.1.1) | rapid divisions without growth; S–M cycles on maternal stocks; falling cytoplasm-to-nucleus ratio; blastocoel; quiet genome; spindle geometry (Remark 5.1.1) |
| Maternal control (5.2) | maternal factors (Definition 5.2.1); maternal, zygotic and MZ mutants differ in whose genotype causes the phenotype, which decides whether testing embryos helps |
| MZT (Definition 5.2.2) | clearance of maternal products plus ZGA in waves; MBT in fast cleavers (cycle 14 in *Drosophila*, 10 in zebrafish, 12 in *Xenopus*); 2-cell in mouse, 4- to 8-cell in human |
| Timing (Formula 5.2.1) | titration of a fixed maternal pool by DNA that doubles each cycle gives a switch at a fixed DNA/cytoplasm ratio, shifted one cycle by halving or doubling ploidy; candidates: histones, replication factors; plus pioneer factors and import capacity |
| Cleavage patterns (Definitions 5.3.1–5.3.2) | yolk class (iso-, meso-, telo-, centrolecithal) and spindle orientation decide holoblastic (radial, spiral, bilateral, rotational) or meroblastic (discoidal, superficial) cleavage |
| Species (5.4) | sea urchin micromeres; frog animal cap and blastocoel; zebrafish YSL, EVL, deep cells; chick area pellucida and opaca, hypoblast, Koller's sickle; *Drosophila* syncytium, pole cells, cellularization in cycle 14 |
| Blastocoel model (5.5) | lattice energy (5.2) with adhesion, constraint and entropy; local Landau potential (5.3) with cusp $v^2 + 4u^3 = 0$ (Proposition 5.5.1): gradual versus sudden cavitation; continuum equation (Formula 5.5.1), first integral (5.5) and wall profile; multiplier fixed variationally (Proposition 5.5.2); radius $(\gamma V/2J)^{1/2}$ |
| Mammals (5.6) | rotational, asynchronous cleavage; compaction and polarity (Definition 5.6.1); ICM versus trophectoderm by polarity read through Hippo–YAP–TEAD4–Cdx2 (Definition 5.6.2, Example 5.6.1); epiblast versus primitive endoderm by a Nanog–Gata6 switch coupled by FGF4 (Formula 5.6.1); implantation and diapause (Definitions 5.6.3–5.6.4) |
| Clinic (5.7) | miscarriage mostly from aneuploidy; monozygotic twins (Definition 5.7.1) and membranes; chimeras and ES cells; IVF, ICSI and the limits of PGT |

## Questions

1. A woman has had four pregnancies with two different partners, all ending in arrest of the embryo at the cleavage stage. Which class of mutation in the table of 5.2.1 does this suggest, and would preimplantation testing of her embryos help?

   **Answer** The pattern, independent of the partner and affecting every pregnancy, is that of a maternal mutant: the mother's oocytes lack a product needed for cleavage (for example a component of the subcortical maternal complex such as *PADI6* or *KHDC3L*). The phenotype depends only on her genotype, so all her embryos are affected whatever their own genotype; testing embryos cannot find an unaffected one. Sequencing her genome is informative, and the realistic options are oocyte donation or, in future, correction of the oocyte defect.

2. In Formula 5.2.1, show that when $R \gg 1$ the free repressor falls from close to $R$ to below 1 within about two cycles around $n^*$. What would happen if each nucleus contained more binding sites for the repressor, for example because of an extra chromosome?

   **Answer** For $S_n \ll R$, $r \approx R - S_n$ is large; for $S_n \gg R$, $r \approx R/S_n$, small. At $S_n = R$, (5.1) gives $r^2 + r - R = 0$, $r \approx \sqrt R$. Since $S_n$ doubles each cycle, one cycle before $n^*$ ($S = R/2$) $r \approx R/2$, and one cycle after ($S = 2R$) $r \approx R/(S - R) \approx 1$; two cycles after, $r \approx 1/3$. So promoter occupancy changes from nearly full to about one half within two cycles. More sites per nucleus increases $s$ and lowers $n^* = \log_2(R/ps)$: an extra chromosome adds a few percent of sites and advances the switch by $\log_2(1.03) \approx 0.04$ cycles, negligible; only a doubling of the genome shifts it by a whole cycle, as in the ploidy experiments.

3. Design an experiment that distinguishes a timer (time since fertilization) from a counter (ratio of DNA to cytoplasm) for ZGA in a species of your choice, and state the predictions.

   **Answer** Change the DNA-to-cytoplasm ratio without changing time, or vice versa. (a) Compare haploid, diploid and tetraploid embryos: a counter predicts a one-cycle shift in ZGA per doubling of ploidy, a timer none. (b) Ligate or constrict the egg so that one half receives a nucleus later: a counter predicts that the half with fewer nuclei activates later by the number of cycles it lags; a timer predicts simultaneous activation. (c) Slow the cell cycle (for example with a mild inhibitor of Cdk1) without changing time: a counter predicts activation at the same cycle number but later in time; a timer predicts activation at the same time, at an earlier cycle. Gene-specific readouts are needed, because some genes behave as timed and others as counted.

4. Explain why the third cleavage of the frog egg is displaced towards the animal pole, using the rules of Remark 5.1.1, and why the animal cells remain smaller thereafter.

   **Answer** The vegetal cytoplasm is full of yolk platelets, which the spindle and asters do not penetrate and which slow furrow ingression (Balfour's rule). The cytoplasm free of yolk, in which the asters grow and the spindle forms, is concentrated in the animal half; the spindle of the third division forms there, parallel to the animal–vegetal axis, and the furrow cuts the cell across it, above the equator. The animal cells then have less yolk, form spindles and furrows faster, and divide more often, so they stay smaller.

5. In the local theory of 5.5.3, take $J c = 2$ and find the sign of $u$. How does $v$ have to change for a cavity to form, and is the change gradual or sudden? Repeat for $J c = 8$, and find the range of $v$ over which morula and blastula states coexist.

   **Answer** $u = 1 - Jc/4$. For $Jc = 2$, $u = 0.5 > 0$: one minimum for every $v$, and its position $\sigma_{\min}$ decreases continuously as $v$ increases, crossing $0$ at $v = 0$, so cavitation is gradual; it requires $\lambda/2 > Jc/4$, i.e. $\lambda > 1$. For $Jc = 8$, $u = -1$: two minima coexist for $\lvert v\rvert < 2(-u)^{3/2} = 2$. With perfect delay the embryo starting in the cellular state jumps to the cavity state at $v = 2$; under the Maxwell convention at $v = 0$. In both cases the change is sudden.

6. Derive the first integral (5.5) from (5.4) in one dimension, and estimate the thickness of the cell layer when $E(\sigma) - E(\sigma_{\min}) \approx \tfrac12 k(\sigma - \sigma_{\min})^2$ near the interior minimum.

   **Answer** With $E'(\sigma) = (Ja^2c/12)\sigma''$, multiply by $\sigma'$: $\tfrac{\mathrm{d}}{\mathrm{d}r}E(\sigma) = (Ja^2c/24)\tfrac{\mathrm{d}}{\mathrm{d}r}(\sigma')^2$, so $(Ja^2c/24)(\sigma')^2 - E(\sigma)$ is constant. Near the minimum, $\sigma' = \pm(\sqrt{k/2}/\ell)(\sigma - \sigma_{\min})$, so $\sigma - \sigma_{\min} \propto \exp(-d\sqrt{k/2}/\ell)$: the density approaches its interior value exponentially with decay length $\ell\sqrt{2/k} = (Ja^2c/12k)^{1/2}$. The layer is a few cell diameters thick when $J$ and $k$ are comparable, as in a one-cell-thick blastula wall for moderate adhesion.

7. A mouse embryo is disaggregated at the 4-cell stage and a single blastomere is cultured. It forms a small blastocyst with a normal ICM. What does this show about the first lineage decision? What would you expect if a single blastomere of a 16-cell embryo, taken from the inside, were cultured alone?

   **Answer** The 4-cell blastomere is still able to form both lineages, so fate has not been fixed by inheritance: the decision is made later by position and polarity, as in 5.6.2. An inner 16-cell blastomere cultured alone is outside on all sides; it will polarize, inactivate Hippo signalling on its exposed surface and form trophectoderm on the outside and ICM inside after further divisions, until about the 32-cell stage when inner cells lose this ability. Inner cells isolated at later stages (immunosurgery of the ICM at E3.5) still re-form an outer layer, but of primitive endoderm rather than trophectoderm, showing that the potential to make trophectoderm is lost first.

8. In the Nanog–Gata6 model, what happens to the proportion of epiblast cells if half of the epiblast cells in a late ICM are killed by a laser while the remaining cells are still undecided? Use the feedback in Formula 5.6.1 to explain, and suggest how to test it.

   **Answer** Killing epiblast (Nanog-high) cells lowers the FGF4 produced, so the signal $E_i$ received by the undecided cells falls; their Gata6 production drops and Nanog repression by ERK is relieved, so more of them adopt the epiblast state. The population regulates back towards the normal ratio, as long as there are undecided cells. Test by ablating identified Nanog–GFP cells at about E3.75 and counting the two fates at E4.5, with a control in which FGF/MEK signalling is clamped (inhibitor plus defined exogenous FGF4): with the signal clamped, the compensation should disappear.

9. Explain from the order of formation of the extraembryonic membranes why monozygotic twins with one chorion but two amnions are thought to have separated between days 5 and 9. Why is the time of separation more uncertain than this argument suggests?

   **Answer** The chorion derives from the trophectoderm, which forms by day 5; the amnion forms from the epiblast around days 8–9. Twins sharing one chorion must have come from one trophectoderm, hence one blastocyst, so the separation occurred after day 5; two amnions mean that each twin formed its own amnion, so the separation occurred before the amnion formed. The inference assumes that separation takes place within one structure and that membranes cannot form secondarily or fuse. Fusion of chorions of two blastocysts that implant close together, and the formation of two trophoblast vesicles from one embryo, would break the correspondence, which is why the mechanism of dichorionic monozygotic twinning is debated.

10. (Open question) A couple undergoing IVF are told that one of their blastocysts is mosaic for trisomy 16 in the trophectoderm biopsy. Discuss, using this chapter, what the result means for the embryo proper and what other information would help a decision.

    **Answer** A trophectoderm biopsy samples five to ten cells of a lineage that forms the placenta, not the embryo. Mitotic errors in cleavage make mosaicism common, and aneuploid cells may be confined to the trophectoderm, or may be outcompeted or eliminated from the epiblast by apoptosis (as shown in mouse chimeras of euploid and aneuploid cells). The result therefore does not establish that the fetus is aneuploid, but trisomy 16 confined to the placenta can still impair placental function and growth, and uniparental disomy may arise if the embryo corrects the trisomy by losing one chromosome. Helpful information: the proportion of abnormal cells (low-level mosaicism has better outcomes), the chromosome involved, whether euploid embryos are available, and the availability of prenatal confirmation (amniocentesis rather than chorionic villus sampling, since the latter samples trophoblast-derived tissue).
