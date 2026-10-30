---
title: "Limb I: Initiation, Outgrowth and the Proximo-Distal Axis"
description: "How a vertebrate limb starts and grows out. Limb anatomy and the three axes; the limb field and its position along the body (Hox code, retinoic acid, Tbx5, Tbx4, Pitx1, Islet1; Holt-Oram syndrome); induction by Fgf10 and the Fgf10-Wnt3-Fgf8 feedback loops; the apical ectodermal ridge and its classical experiments; proximo-distal patterning (progress zone, early specification, the two-signal and signal-plus-timer models, the Hox and Meis code); the statistics of estimating a mitotic field (Poisson likelihood, least squares, smoothing kernels, boundary corrections and Toeplitz matrices); contact inhibition of division and its fluctuations; Lewis's reconstruction of the fate map from the field of cell division."
---

The tetrapod limb is the classical system for asking how a field of initially similar mesenchymal cells becomes an organ with a reproducible three-dimensional pattern: a single bone near the body, two in the middle, many at the tip; a thumb on one side and a little finger on the other; knuckles and palms. Limbs are dispensable for embryonic survival, accessible in the chick egg and genetically tractable in the mouse, so almost every kind of experiment of developmental biology, removal, grafting, recombination, bead implantation, misexpression and knockout, has been performed on them. This chapter follows the limb from its specification in the flank to its outgrowth under the apical ectodermal ridge and the patterning of its proximo-distal axis; the next chapter ([7.5.32](/7.5.32)) treats the anterior–posterior and dorso-ventral axes, the digits and limb evolution. The limb uses the signals introduced in [7.5.3](/7.5.3) (FGF, **Wnt signaling pathway**, **Hedgehog signaling pathway**, BMP) and the **Hox genes** of [7.5.17](/7.5.17); the ideas of **positional information** and **morphogen** gradients come from [7.5.11](/7.5.11). The second half of the chapter is quantitative: how to estimate the spatial field of cell division from a few hundred mitoses in a section, whether the field is consistent with contact inhibition, and how a fate map can be reconstructed from the field of growth alone.

## 31.1. Anatomy, Axes and Origins

**Definition 31.1.1 (Limb Segments)** The skeleton of every tetrapod limb consists of three proximo-distal segments: the *stylopod*, a single proximal element (humerus or femur); the *zeugopod*, two parallel elements (radius and ulna, or tibia and fibula); and the *autopod*, the wrist or ankle (carpals, tarsals), metacarpals or metatarsals and the phalanges of the digits.

A limb has three axes. The proximo-distal (PD) axis runs from the shoulder to the finger tips; the anterior–posterior (AP) axis from the thumb (digit 1) to the little finger (digit 5); the dorso-ventral (DV) axis from the back of the hand to the palm. The digits of the chick wing are conventionally numbered 2, 3 and 4 by their position in the five-digit ground plan, although developmental and fossil evidence suggests that they may be digits 1, 2 and 3 in identity; we use the conventional numbering.

**Definition 31.1.2 (Zone of Polarizing Activity)** The **zone of polarizing activity** (ZPA) is a group of mesenchymal cells at the posterior margin of the limb bud that, when grafted to the anterior margin of another bud, induces a mirror-image duplication of the digits; its activity is due to Sonic hedgehog. Besides the apical ectodermal ridge (Definition 31.4.1) it is the second signaling center of the bud; its function is described in [7.5.32](/7.5.32).

![Anatomy of the limb bud and its cell sources (schematic). A: an early chick wing bud in dorsal view (anterior up): mesenchyme of lateral plate origin under an ectodermal jacket, the apical ectodermal ridge (AER) along the distal rim, the progress zone beneath it and the zone of polarizing activity (ZPA) at the posterior margin; the three axes. B: a transverse section of the embryo at the level of the forelimb: the somatic lateral plate mesoderm forms the bones, cartilage, tendons and connective tissue; muscle precursors (Pax3+) delaminate from the ventrolateral lip of the dermomyotome of the adjacent somites and migrate into the bud; neural crest cells give pigment cells and Schwann cells, and motor axons grow in from the neural tube. C: the adult human arm skeleton with its three segments](./plots/limb-anatomy.py)

The bud is built from two tissues. Its core is mesenchyme from the somatic layer of the lateral plate mesoderm, which gives the skeleton, the tendons and the connective tissue, and an ectodermal jacket. Muscle, blood vessels and nerves come from outside. Quail–chick chimeras, in which the somites at limb level of a chick embryo are replaced by quail somites whose nuclei can be recognized, showed that all limb muscle cells are of somitic origin, whereas the cartilage and the connective tissue, including the tendons and muscle connective tissue that pattern the muscles, are of host lateral plate origin ([7.5.24](/7.5.24) for muscle development). Muscle precursors leave the ventrolateral lip of the dermomyotome under the control of Pax3, Lbx1 and the receptor c-Met, whose ligand HGF is expressed in the limb mesenchyme; in Pax3 or c-Met mutant mice the limbs have no muscles. Endothelial cells come from the somites and from local angioblasts, the sensory neurons and the Schwann cells and melanocytes from the **neural crest** ([7.5.20](/7.5.20)), the motor neurons from the ventral **neural tube** ([7.5.21](/7.5.21)).

## 31.2. The Limb Field and Its Position

**Definition 31.2.1 (Limb Field)** A *limb field* is the region of flank mesoderm whose cells are capable of forming a limb on their own: if it is removed, no limb forms; if it is grafted to another site, it forms a limb there.

Harrison's experiments on the salamander *Ambystoma* (1918) mapped the forelimb field as a disc of mesoderm: its center normally forms the free limb, a ring around it the shoulder girdle and flank, and an outer ring normally forms no limb but does so if the inner region is removed. The field regulates. Any half of it, grafted elsewhere, forms a complete limb, and a field split by an inserted barrier forms two complete limbs. This is regulative development ([7.5.1](/7.5.1)) at the level of an organ rudiment. An experiment of nature shows the same: in North American ponds, frogs and salamanders with extra legs are common where tadpoles are infected by the trematode *Ribeiroia ondatrae*, whose cysts split the developing hindlimb buds into fragments that each regulate to form a limb.

Limb buds arise at fixed positions along the body axis, in pairs, never more than four. Their position is not fixed in terms of somite number (a mouse forelimb lies opposite somites 7–12, a chick wing opposite 15–20) but in terms of the Hox code of the axial mesoderm: in fish, amphibians, birds and mammals the forelimb arises at the anterior border of *Hoxc6* expression, at the level of the first thoracic vertebra. Somites from the limb level grafted into the flank enlarge the forelimb bud, and flank somites grafted to limb level reduce it, so the paraxial mesoderm also conveys positional signals.

### 31.2.1. Forelimb or Hindlimb: Tbx5, Tbx4, Pitx1 and Islet1

Four transcription factors distinguish the limb fields before any bud is visible: Tbx5 in the forelimb field, and Tbx4, the homeodomain protein Pitx1 and Islet1 in the hindlimb field. Their roles have been tested by every logical kind of experiment.

| Experiment | Result | Conclusion |
|---|---|---|
| *Tbx5* knockout (mouse, zebrafish, chick) | no forelimb, not even a shoulder girdle | Tbx5 is necessary to initiate the forelimb |
| Lateral plate-specific loss of *Islet1* (mouse) | no hindlimb | Islet1 is necessary to initiate the hindlimb |
| *Tbx4* knockout | chick: no leg; mouse: hindlimb bud forms but arrests | Tbx4 maintains rather than initiates outgrowth in the mouse |
| *Pitx1* misexpressed in the mouse forelimb | muscles, tendons and bones of the arm take on hindlimb character, *Tbx4* and *Hoxc10* are induced | Pitx1 is sufficient for hindlimb identity |
| FGF bead in the chick flank, near the wing | ectopic limb expressing *Tbx5*, develops as a wing | |
| FGF bead near the leg | ectopic limb expressing *Tbx4*, develops as a leg | limb type follows the Tbx gene expressed |
| FGF bead in the middle of the flank | *Tbx5* anteriorly and *Tbx4* posteriorly; a chimeric limb with feathers in front and scales behind | |
| *Tbx4* expressed throughout the chick flank by a virus | FGF-induced limbs in the anterior flank become legs | |

Several human syndromes confirm these roles. Heterozygous loss of *TBX5* causes Holt–Oram syndrome: malformations of the upper limb, typically of the thumb and radial side of the forearm, combined with atrial and ventricular septal defects and conduction defects of the heart, where Tbx5 is also required ([7.5.28](/7.5.28)); the legs are normal. Haploinsufficiency of *PITX1* causes clubfoot, and in Liebenberg syndrome deletions upstream of *PITX1* bring a forelimb enhancer next to the gene, so that it is expressed in the arm and the elbow and wrist take on features of the knee and ankle.

Upstream of Tbx5 lies the axial Hox code, which acts directly on a *Tbx5* enhancer with Hox binding sites, and retinoic acid (RA), made by Raldh2 in the somites and anterior presomitic mesoderm. RA represses *Fgf8* in the trunk; the Fgf8 that remains, in the heart field anteriorly and in the caudal progenitor zone posteriorly, suppresses *Tbx5*. Loss of RA synthesis (in *Raldh2* or *Rdh10* mutants) expands trunk Fgf8 and abolishes the forelimb bud, whereas the hindlimb forms almost normally, so hindlimb initiation uses another, still unidentified, input.

## 31.3. Induction and Outgrowth: Two Feedback Loops

Before the bud appears, the somatic lateral plate is a pseudostratified epithelium. In the limb fields, and only there, it undergoes an **epithelial–mesenchymal transition** under the control of Tbx5 in the forelimb, and the released mesenchyme proliferates under the ectoderm. Fgf10, induced by Tbx5 (through Wnt2b) in the forelimb and by Islet1 and Tbx4 (through Wnt8c in the chick) in the hindlimb, is the key mesenchymal signal: a bead releasing FGF placed in the flank between the limbs induces an extra limb, and *Fgf10* knockout mice have no limbs. Older experiments suggested that the intermediate mesoderm (the mesonephros) induces the bud, since a barrier between them stopped bud outgrowth; but limbs form normally in mutants lacking an intermediate mesoderm source of FGF8, and the current view is that limb initiation is intrinsic to the lateral plate once it has received its axial position.

Fgf10 acts on the overlying ectoderm. It induces *Wnt3* (*Wnt3a* in the chick), which through β-catenin induces *Fgf8*; the *Fgf8*-expressing ectoderm thickens and becomes the apical ectodermal ridge. Fgf8 from the ridge, together with Fgf4, Fgf9 and Fgf17, in turn maintains *Fgf10* in the mesenchyme. The two loops, Tbx5–Wnt2b–Fgf10 within the mesoderm and Fgf10–Wnt3–Fgf8 between mesoderm and ectoderm, make limb outgrowth self-sustaining once started: the decision to make a limb behaves like a **bistability** switch ([7.3.18](/7.3.18)) that, once flipped by axial cues, no longer needs them.

![Positioning and induction of the limb. A: a chick embryo (dorsal view, schematic, anterior up) with somite levels: Tbx5 in the lateral plate of the wing field, Tbx4 and Pitx1 in the leg field; an FGF bead in the flank between them induces a limb that expresses Tbx5 anteriorly and Tbx4 posteriorly. B: the regulatory network (activation arrows open, inhibition bars): RA from the somites represses trunk Fgf8, which would otherwise repress Tbx5; the Hox code and Tbx5 induce Wnt2b and Fgf10 in the forelimb mesenchyme; Fgf10 induces Wnt3 and Fgf8 in the ectoderm, and Fgf8 from the AER maintains Fgf10: two positive loops. C: the mutual activation model of Example 31.3.1: rate of change of the two signals; the nullclines cross three times, so the system has an off state and an on state separated by a threshold](./plots/limb-initiation.py)

**Example 31.3.1 (Mutual Activation as a Switch)** Let $u$ be the level of Fgf10 signaling in the mesenchyme and $w$ that of Fgf8 in the ectoderm, each induced by the other with Hill kinetics and removed at unit rate:

$$
\dot u=s+\frac{a\,w^2}{K^2+w^2}-u,\qquad \dot w=\frac{a\,u^2}{K^2+u^2}-w,
\tag{31.1}
$$
with $s$ a weak input from the axial program (Tbx5). The nullclines $u=s+aw^2/(K^2+w^2)$ and $w=au^2/(K^2+u^2)$ are two sigmoids. For $s=0$ the symmetric steady states satisfy $u=au^2/(K^2+u^2)$, so $u=0$ or $u^2-au+K^2=0$; with $K=1$ the second pair exists only for $a\ge2$. For $a=2.5$ the steady states are $u=w=0$ (stable: no limb), $u=w=0.5$ (a saddle, the threshold) and $u=w=2$ (stable: limb outgrowth). A transient input $s$ large enough to carry the system past the saddle switches it on permanently, which is what grafting an FGF bead does; removing either partner (an *Fgf10* or *Wnt3* knockout) eliminates the on state. Real limb buds add a third player, Shh from the ZPA, to this loop ([7.5.32](/7.5.32)).

## 31.4. The Apical Ectodermal Ridge

**Definition 31.4.1 (Apical Ectodermal Ridge)** The **apical ectodermal ridge** (AER) is a ridge of thickened ectoderm running along the distal margin of the limb bud, at the boundary between dorsal and ventral ectoderm; it is a signaling center that, through FGFs, keeps the mesenchyme beneath it proliferating and undifferentiated and so drives the outgrowth of the limb along the proximo-distal axis.

The AER forms where dorsal and ventral ectoderm meet. In the chick, *Radical fringe* in the dorsal ectoderm creates a Notch signaling boundary, and Engrailed-1 marks the ventral ectoderm; in the mouse, ventral *En1* limits the AER on the ventral side and its loss widens the ridge. Grafting a piece of ventral ectoderm into the dorsal ectoderm of a bud creates a new junction and an extra AER, and in the chick mutant *limbless*, whose limb ectoderm is entirely dorsal, no AER forms and limb development stops after bud initiation. The ectoderm, not the mesoderm, is at fault in *limbless*: limbless mesenchyme covered with normal ectoderm forms a normal limb.

John Saunders and his successors established the functions of the ridge by a series of operations on the chick wing bud. Each was designed to separate the contributions of the ridge and the mesenchyme.

| Operation | Result | Conclusion |
|---|---|---|
| Remove the AER | outgrowth stops; the later the removal, the more distal the level of truncation | the AER is required for outgrowth; proximal structures are laid down first |
| Graft an extra AER onto the bud | supernumerary distal structures | the AER can elicit outgrowth from any limb mesenchyme |
| Put leg mesenchyme under a wing AER | toes at the tip | the mesenchyme, not the AER, determines limb type |
| Put non-limb (flank) mesenchyme under the AER | the AER regresses | the AER is maintained by limb mesenchyme (through Fgf10) |
| Replace the AER by beads releasing FGF4 or FGF8 | almost complete limbs | FGFs are the active AER signal |
| Exchange an old AER for a young one, or vice versa | normal limbs | the AER is permissive: it carries no PD information |
| Implant a quail AER onto *limbless* chick limb bud mesenchyme | a limb develops | the *limbless* mesenchyme is competent |

The chick mutant *eudiplopodia* shows the same logic in a natural setting: an ectopic AER on the dorsal surface of the leg bud produces a second set of toes. In mice, removal of *Fgf4* and *Fgf8* from the ridge abolishes limb development, whereas loss of either alone, or of Fgf9 or Fgf17, has mild effects: the AER FGFs are redundant, and the severity of the skeletal defects increases with each FGF gene removed. The ridge also prevents the mesenchyme immediately beneath it from forming cartilage. Interdigital mesenchyme, which normally dies, can form an extra digit when it is released from this inhibition (for example by local removal of the ectoderm or by a TGF-β bead), so a digit's position is not fixed in the mesenchyme until late.

![Classical experiments on the chick wing bud (schematic outcomes). A: removal of the AER at successively later stages gives limbs truncated at successively more distal levels (stylopod only; stylopod and zeugopod; down to the wrist). B: the progress zone exchanges of Summerbell and Lewis: a young progress zone with its AER grafted onto an old bud adds a second zeugopod and autopod beyond those already formed; an old progress zone on a young bud omits the zeugopod, so digits arise from the humerus.](./plots/aer-experiments.py)

## 31.5. Proximo-Distal Patterning

The limb forms in proximo-distal order: the stylopod condenses first, then the zeugopod, then the autopod. How do cells learn their PD position? The question has been answered three times, and each answer explains different experiments.

### 31.5.1. The Progress Zone Model

**Definition 31.5.1 (Progress Zone)** The *progress zone* (PZ) is the population of proliferating, undifferentiated mesenchymal cells within about $200\,\mathrm{\mu m}$ of the AER, kept in that state by AER signals. In the *progress zone model* (Summerbell, Lewis and Wolpert 1973) cells in the PZ progressively acquire more distal positional values the longer they stay there, and their value is fixed when they leave it.

The model explains the truncations after AER removal: the PZ stops, and the most distal values reached so far are the last to be made. It also explains the grafting experiments of Summerbell and Lewis (1975). A young PZ (with its AER) placed on the stump of an old bud, which has already laid down a stylopod and zeugopod, forms a second zeugopod and autopod beyond them: the young cells have not yet "progressed". An old PZ on a young stump forms only distal structures, and digits arise directly from the humerus: the cells that would have made the zeugopod were missing. Exchanging only the AER has no effect, which locates the timer in the mesenchyme. X-irradiation, which kills a proportion of PZ cells, produces limbs whose proximal elements are reduced or missing while the hand is nearly normal, the pattern of phocomelia: the model attributed this to fewer cells leaving the PZ early. Thalidomide was once thought to act in this way; its effect is now attributed to destruction of developmental transcription factors through its target cereblon ([7.5.38](/7.5.38)).

**Formula 31.5.1 (Exit Time in the Progress Zone)** Let the PZ be a distal layer of fixed thickness $d$ in which cells divide at rate $g$, so that the limb lengthens at the rate $\dot\ell=g\,d$, while proximal cells no longer divide. A cell at distance $y\le d$ from the tip moves away from the tip at the speed $g\,y$, so a cell entering at distance $y_0$ leaves the zone at the time

$$
T(y_0)=\frac1g\ln\frac d{y_0},
\tag{31.2}
$$
after $T g/\ln2=\log_2(d/y_0)$ cell cycles, and comes to rest at the position $\ell(t_{\mathrm{exit}})-d$ from the base, which increases with its exit time. If the positional value is a monotone function of the time spent in the zone, proximal values are laid down first and each segment is formed by cells that started closer to the tip than the cells of the previous one.

The progress zone model faced three difficulties. Dye injected at stage 19 into the chick wing bud $200$–$300\,\mathrm{\mu m}$ from the AER labeled the stylopod, $100$–$200\,\mathrm{\mu m}$ the zeugopod and just under the AER the autopod (Dudley, Ros and Tabin 2002): the segments are already mapped in the early bud, at positions that already reflect their PD order, not mixed in a common pool. Removal of the AER causes the death of the mesenchyme within about $200\,\mathrm{\mu m}$ of the ridge (Rowe, Cairns and Fallon 1982), which by itself can explain the truncations: the distal segments are lost because their precursors die, not because they have not yet been specified. And in mice lacking *Fgf4* and *Fgf8* in the AER, the limbs are truncated by the absence of particular precursors, not by a shortened period of progression.

### 31.5.2. Early Specification and the Two-Signal Model

**Definition 31.5.2 (Two-Signal Model)** In the *two-signal model* the proximo-distal positional values are specified in the early bud by two opposing signals, a proximal one from the flank (retinoic acid) and a distal one from the AER (FGF, with Wnt); proximal cells, high in RA, become stylopod, distal cells, high in FGF, autopod, and cells between them zeugopod. The specified domains then expand by growth, proximal first.

The evidence is of three kinds. RA proximalizes: distal limb mesenchyme exposed to RA and grafted back forms proximal elements, and RA induces the proximal homeobox genes *Meis1* and *Meis2*, whose misexpression distally truncates the limb. FGF distalizes: it represses *Meis1/2* and induces the RA-degrading enzyme Cyp26b1 in the distal mesenchyme, so the RA gradient is shaped by distal destruction as well as proximal supply, an example of opposing gradients ([7.5.11](/7.5.11)); *Cyp26b1* knockout mice have truncated, proximalized limbs. Distal limb cells cultured in combinations of RA, FGF8 and Wnt3a express proximal markers with RA and distal markers with FGF and Wnt, and in proportion to their concentrations (Cooper et al. 2011; Roselló-Díez et al. 2011). The role of RA is debated: mouse embryos lacking RA synthesis, rescued in early development by a low dose of RA, have hindlimbs with normal PD patterning (Cunningham et al. 2013), so a proximal signal other than RA, or a permissive rather than instructive role of RA, cannot be excluded.

**Formula 31.5.2 (Domains Specified by Two Signals)** In a bud of length $\ell_0$, let the proximal signal decay from the base and the distal one from the tip with the same decay length $\lambda$, $R(x)=\mathrm{e}^{-x/\lambda}$ and $F(x)=\mathrm{e}^{-(\ell_0-x)/\lambda}$, and let cells become stylopod where $R>\theta$, autopod where $F>\theta$, zeugopod elsewhere. The stylopod and autopod domains then have the length $\lambda\ln(1/\theta)$ each and the zeugopod

$$
\ell_0-2\lambda\ln\frac1\theta ,
\tag{31.3}
$$
which exists only if $\ell_0>2\lambda\ln(1/\theta)$. If the bud then grows uniformly, $x(t)=x_0\mathrm{e}^{gt}$, all three domains expand in proportion.

The formula makes one prediction that distinguishes the model from the progress zone: the specification of three segments requires a minimum bud size, and the middle segment is the most sensitive to bud length. Limbs of mutants with small early buds tend to lose the zeugopod. Neither model alone explains all the data, and the model now favored by Wolpert and colleagues combines them.

**Definition 31.5.3 (Signal-Plus-Timer Model)** In the *signal-plus-timer model* (Saiz-Lopez et al. 2015), proximal positional value is specified by a high level of the proximal signal, and when distal cells escape it, by distance from the flank and by Cyp26b1 activity, an intrinsic timer in the distal cells starts and specifies successively more distal values, as in the progress zone.

Grafts of GFP-labeled wing bud cells to different sites showed that distal cells change their properties over time, cell-cycle dynamics and Hox expression, independently of their surroundings, and the distal mesenchyme shows oscillatory expression of *hairy2*, a relative of the segmentation-clock genes ([7.5.23](/7.5.23)). Proximal values are then set by a gradient and distal values by a timer: the two mechanisms are not exclusive.

![Three models of proximo-distal patterning, simulated. A: progress zone model (Formula 31.5.1): trajectories of cells in a limb whose distal 200 µm (green band, below the tip) proliferate; each cell is coloured by the time it spends in the zone (stylopod short, zeugopod intermediate, autopod long) and comes to rest at a position that increases with its exit time. B: two-signal model (Formula 31.5.2): proximal and distal signals in a bud of 300 µm define three domains, which then expand by uniform growth; a bud shorter than 2λ ln(1/θ) has no zeugopod. C: signal-plus-timer: the proximal signal specifies the stylopod while the distal cells are within its range; once they escape it, a timer specifies zeugopod and then autopod](./plots/pd-models.py)

### 31.5.3. The Hox and Meis Code

The proximo-distal segments correspond to the expression of the 5′ genes of the *Hoxa* and *Hoxd* clusters (paralogues 9–13) and of *Meis1/2*: *Meis* in the stylopod, *Hox9* and *Hox10* paralogues in the stylopod, *Hox11* in the zeugopod, *Hox12* and *Hox13* in the autopod. Removing all copies of one paralogue group deletes the corresponding segment, which is the strongest evidence for the code:

| Genotype (mouse) | Phenotype |
|---|---|
| *Hoxa10*, *Hoxc10*, *Hoxd10* all null | no femur or patella (hindlimb stylopod); forelimbs nearly normal because *Hox9* paralogues are also expressed there |
| *Hoxa11*, *Hoxc11*, *Hoxd11* all null | no zeugopod: no radius and ulna, no tibia and fibula |
| *Hoxa13*, *Hoxd13* null | no autopod |
| Human *HOXD13* polyalanine expansion (homozygous) | synpolydactyly: fused and duplicated digits |
| Human *HOXA13* mutations | hand–foot–genital syndrome |

Hox genes act less as switches of identity than as regulators of the growth and the condensation of the segments; the paralogues are partly redundant, and loss of one group produces a short, fused element rather than a transformation into another segment. Their expression is controlled in two phases by two large regulatory landscapes on either side of the *Hoxd* cluster: an early phase driven by enhancers on the telomeric side activates *Hoxd9–11* in the presumptive zeugopod, and a late phase driven by enhancers on the centromeric side activates *Hoxd13* (and *Hoxd10–12*) in the autopod; the two landscapes are separate topologically associating domains, and cells switch from one to the other ([7.2](/7.2) for chromatin domains). The late, centromeric regulation is tetrapod-specific in part, a point that matters for the evolution of the autopod ([7.5.32](/7.5.32)).

![The proximo-distal code. A: a paddle-stage bud with the nested domains of Meis1/2 (proximal), Hoxa11 (middle) and Hoxa13 (distal; they become mutually exclusive as development proceeds). B: the segments they correspond to. C: knockouts of whole paralogue groups (schematic hindlimbs): without Hox10 the stylopod is missing, without Hox11 the zeugopod, without Hoxa13 and Hoxd13 the autopod](./plots/pd-hox-code.py)

## 31.6. Estimating a Mitotic Field

Are the shape and the pattern of the limb produced by spatial differences in cell division? The early chick wing bud is a loosely packed, apparently uniform mesenchyme with a high mitotic index, about 12 per 100 cells in mitosis. At later stages (Hamburger–Hamilton stage 25, about 4.5 days) the index becomes nonuniform, and it varies inversely with cell density, which rises in the central core where the cartilage condenses. To measure such a field one fixes and sections a bud, divides a section into squares and counts nuclei and mitotic figures. One bud is one sample, the mitoses are few, and the field is to be estimated locally, so the statistics needs care.

**Definition 31.6.1 (Mitotic Index)** The *mitotic index* is the fraction of cells in mitosis. If every cell spends the same time $\tau$ in mitosis and divides once per cycle of length $\gamma$, the index of a large homogeneous population equals $\tau/\gamma$, the fraction of the cycle spent in mitosis, so it measures the local division rate $1/\gamma=m/\tau$.

### 31.6.1. Likelihood

Let the section be divided into squares with centers $x$, containing $\rho(x)$ cells of which $M(x)$ are in mitosis, and let $m(x)$ be the underlying probability that a cell at $x$ is in mitosis. If mitoses in different squares are independent (squares large enough that few mitoses straddle a boundary, and no clustering; there is in fact some evidence for chains of related mitoses), the probability of the observations factorizes, $\mathbb{P}(\{M\}\mid\{m\})=\exp\sum_x\phi(M(x)\mid m(x))$. The field is parametrized by coefficients $c_\lambda$ of basis functions $u_\lambda$, for instance $m=\sum_\lambda c_\lambda u_\lambda$, $(\sum_\lambda c_\lambda u_\lambda)^2$ or $\exp\sum_\lambda c_\lambda u_\lambda$, and the coefficients are found by **maximum likelihood estimation** ([3.2.3](/3.2.3)): $\sum_x\frac{\partial\phi}{\partial m}\frac{\partial m}{\partial c_\lambda}=0$.

**Proposition 31.6.1 (Estimating Equations)** (a) If the counts are Poisson, $M(x)\sim\mathrm{Poi}(m(x)\rho(x))$, and $m=\exp\sum_\lambda c_\lambda u_\lambda$, the maximum likelihood equations are

$$
\sum_x\big(M(x)-m(x)\rho(x)\big)u_\lambda(x)=0\quad\text{for all }\lambda ,
\tag{31.4}
$$
which are nonlinear in the $c_\lambda$ and must be solved numerically. (b) If instead the counts are Gaussian with fixed variance $\sigma^2$ and $m=\sum_\lambda c_\lambda u_\lambda$ is linear, the same equations (31.4) result, and they are now the normal equations of **least squares**, $\partial_{c_\lambda}\sum_x(M-m\rho)^2=0$. (c) With Gaussian counts of the Poisson-compatible variance $\sigma^2(x)=\sigma_0^2+M(x)$ (an intrinsic fluctuation added to the Poisson variance, estimated by the observed count), the equations become the linear weighted system $\sum_x\frac{M(x)-m(x)\rho(x)}{\sigma_0^2+M(x)}u_\lambda(x)=0$.

**Proof** (a) $\phi=M\ln(m\rho)-m\rho-\ln M!$, so $\partial\phi/\partial m=M/m-\rho$, and $\partial m/\partial c_\lambda=m\,u_\lambda$; the product is $(M-m\rho)u_\lambda$. (b) $\phi=-(M-m\rho)^2/(2\sigma^2)+\text{const}$, $\partial\phi/\partial m=\rho(M-m\rho)/\sigma^2$, and $\partial m/\partial c_\lambda=u_\lambda$; with the basis redefined as $\rho u_\lambda$ (or with $\rho$ nearly uniform) this is (31.4). (c) The same with $\sigma^2$ depending on $x$. $\square$

Case (a) is a Poisson **generalized linear model** with log link and offset $\ln\rho$, solved by iteratively reweighted least squares. The simplest version, adequate for the accuracy of the data, uses a fixed variance and parametrizes the expected count itself, $\bar M(x)\equiv m(x)\rho(x)=\sum_\lambda c_\lambda u_\lambda(x)$. Then $\rho$ drops out and the equations are $\sum_x\big(M(x)-\sum_\nu c_\nu u_\nu(x)\big)u_\lambda(x)=0$.

### 31.6.2. Projection and Smoothing Kernels

**Proposition 31.6.2 (Estimation as Projection)** If the $p$ basis functions are orthonormal on the $N$ grid points, $\sum_xu_\lambda^*(x)u_\nu(x)=\delta_{\lambda\nu}$ (complex functions, with the set closed under conjugation), the fixed-variance estimate is the **orthogonal projection** of the data onto their span:

$$
c_\lambda=\sum_xu_\lambda^*(x)M(x),\qquad \bar M(x)=\sum_y\Big(\sum_{\lambda=1}^pu_\lambda(x)u_\lambda^*(y)\Big)M(y).
\tag{31.5}
$$

The projection presumes that the true field lies exactly in the span of the chosen $p$ functions. If instead we only believe that it probably lies near it, the sharp projection can be replaced by a weighted average diagonal in the same basis,

$$
\bar M(x)=\sum_yW(x,y)M(y),\qquad W(x,y)=\sum_{\lambda=1}^\infty w_\lambda u_\lambda(x)u_\lambda^*(y),\qquad w_1=1,\ w_\lambda\to0,\ \sum_\lambda w_\lambda=p ,
\tag{31.6}
$$
where $p$ is now an effective number of parameters. The choice of the Fourier basis on a square makes the kernels explicit.

**Theorem 31.6.1 (Fourier Kernels)** On a square of $N=(2L+1)^2$ unit cells with the Fourier basis $u_{\lambda_1\lambda_2}(x)=\frac1{2L+1}\exp\frac{2\pi\mathrm{i}(\lambda_1x_1+\lambda_2x_2)}{2L+1}$:

(a) Truncation to $\lvert\lambda_1\rvert,\lvert\lambda_2\rvert\le K$ ($p=(2K+1)^2$) gives the projection kernel

$$
W(x-y)=\frac1N\prod_{\alpha=1}^2\frac{\sin\frac{2\pi}{2L+1}\big(K+\frac12\big)(x_\alpha-y_\alpha)}{\sin\frac{\pi}{2L+1}(x_\alpha-y_\alpha)},
$$
the two-dimensional Dirichlet kernel, which takes negative as well as positive values.

(b) The smooth weights $w_{\lambda_1\lambda_2}=\cos^{2r}\frac{\pi\lambda_1}{2L+1}\cos^{2r}\frac{\pi\lambda_2}{2L+1}$ give the nonnegative kernel

$$
W(x-y)=\Big(\frac14\Big)^{2r}\binom{2r}{r-(x_1-y_1)}\binom{2r}{r-(x_2-y_2)}
\tag{31.7}
$$
(for $r\le L$), which is the result of $r$ successive nearest-neighbor averagings with weights $\frac14,\frac12,\frac14$ in each direction, and the effective number of parameters is $p\approx N/(\pi r)$.

**Proof** In one dimension with $n=2L+1$ points, $W(d)=\frac1n\sum_\lambda w_\lambda\mathrm{e}^{2\pi\mathrm{i}\lambda d/n}$. (a) For $w_\lambda=1$, $\lvert\lambda\rvert\le K$, the geometric sum is $\sin\big((2K+1)\pi d/n\big)/\sin(\pi d/n)$. (b) Write $\cos^{2r}\theta=4^{-r}\sum_{j=0}^{2r}\binom{2r}{j}\mathrm{e}^{\mathrm{i}(2j-2r)\theta}$ with $\theta=\pi\lambda/n$, so $w_\lambda=4^{-r}\sum_j\binom{2r}{j}\mathrm{e}^{2\pi\mathrm{i}\lambda(j-r)/n}$. Summing over $\lambda$ (a full period, since $\cos^{2r}$ has period $n$ in $\lambda$ up to the sign $(-1)^{2r}=1$) gives $n\,\delta_{d+j-r\equiv0}$, so $W(d)=4^{-r}\binom{2r}{r-d}$ when $\lvert d\rvert\le r\le L$. This is the $r$-fold convolution of $(\frac14,\frac12,\frac14)$, as $(\frac{1+\mathrm{e}^{\mathrm{i}\theta}}{2})^{2r}\mathrm{e}^{-\mathrm{i}r\theta}=\cos^{2r}\frac\theta2$. Finally $\sum_\lambda\cos^{2r}\frac{\pi\lambda}n\approx n\int_0^1\cos^{2r}(\pi s)\,\mathrm{d}s=n\binom{2r}{r}4^{-r}\approx n/\sqrt{\pi r}$, and the product of the two directions gives $p\approx N/(\pi r)$. $\square$

The truncated Fourier projection rings: its negative side lobes can produce negative estimated mitotic indices. Smoothing the cutoff of the weights to a Gaussian tail removes them. The iterated nearest-neighbor average of part (b) is a standard smoothing procedure, and it is in fact what Summerbell and Lewis used in their estimates of the mitotic field of the chick wing bud: Theorem 31.6.1 shows that this ad hoc procedure is a projection estimate with a particular prior on the smoothness of the field.

### 31.6.3. Boundary Corrections and Toeplitz Matrices

One would like to use a standard basis, for instance functions orthonormal on a rectangle enclosing the bud, so that buds can be compared. But the index drops abruptly to zero outside the tissue, a discontinuity of no biological meaning that spoils the fit near the edge. The basis should be orthogonalized on the area $\Omega$ of the bud itself. The estimating equations become $\sum_{x\in\Omega}\big(M(x)-\sum_\nu c_\nu u_\nu(x)\big)u_\lambda^*(x)=0$, with the overlap matrix $T_{\lambda\nu}=\sum_{x\in\Omega}u_\lambda^*(x)u_\nu(x)$ no longer the identity:

$$
\bar M(x)=\sum_{y\in\Omega}\Big(\sum_{\lambda,\nu}u_\nu(x)\big(T^{-1}\big)_{\nu\lambda}u_\lambda^*(y)\Big)M(y).
\tag{31.8}
$$
For a Fourier basis $T_{\lambda\nu}$ depends only on $\lambda-\nu$: it is a finite section of a Toeplitz matrix. A doubly infinite matrix $T_{\lambda\nu}=f(\lambda-\nu)$ is diagonalized by the Fourier transform, $\tilde f(\theta)=\sum_kf(k)\mathrm{e}^{\mathrm{i}k\theta}$, but its $p\times p$ sections $T^{(p)}=QTQ$, with $Q$ the projection onto $1\le\lambda\le p$, have no closed-form inverse. Their asymptotics are classical.

**Theorem 31.6.2 (Szegő Limit Theorem)** Let $T_{\lambda\nu}=f(\lambda-\nu)$ be positive definite with a smooth positive symbol $\tilde f(\theta)$, and let $k(n)=\frac1{2\pi}\int_0^{2\pi}\ln\tilde f(\theta)\,\mathrm{e}^{-\mathrm{i}n\theta}\,\mathrm{d}\theta$ be the Fourier coefficients of $\ln\tilde f$. Then

$$
\ln\det T^{(p)}=p\,k(0)+\sum_{n=1}^\infty n\,k(n)k(-n)+o(1)\qquad(p\to\infty).
$$

The theorem (in its strong form due to Szegő, Kac and Baxter) gives the determinant; the inverse needed in (31.8) follows from it by differentiation, since for any invertible matrix $(A^{-1})_{\lambda\nu}=\partial\ln\det A/\partial A_{\nu\lambda}$. Percus obtained a formal expansion in this way. Writing $\ln D=\ln\det(\bar Q+QTQ)$ with $\bar Q=I-Q$, and switching the matrix on as $\bar Q+Q\mathrm{e}^{t\ln T}Q$, a Maclaurin expansion in $t$ at $t=1$ gives

$$
\ln D=\operatorname{tr}Q\ln T\,Q+\frac12\operatorname{tr}Q\ln T\,\bar Q\ln T\,Q+\cdots,
$$
whose first terms reproduce the two terms of the Szegő formula for a Toeplitz $T$. With $\ln T=\int_0^\infty\big[(1+x)^{-1}-(x+T)^{-1}\big]\mathrm{d}x$ one finds $\frac{\partial}{\partial T_{\nu\lambda}}\operatorname{tr}(B\ln T)=\int_0^\infty\big((x+T)^{-1}B(x+T)^{-1}\big)_{\lambda\nu}\mathrm{d}x$, and hence

$$
\big(T^{(p)}\big)^{-1}=\int_0^\infty(x+T)^{-1}\Big[Q+\tfrac12Q\ln T\,\bar Q+\tfrac12\bar Q\ln T\,Q+\cdots\Big](x+T)^{-1}\,\mathrm{d}x .
$$
The leading term is the inverse of the full matrix restricted to the subspace, and the corrections, which come from the coupling between the retained and the discarded modes, measure how strongly the boundary affects the estimate. The Maclaurin series is not itself an asymptotic expansion (a resummation is needed to make it one), and in practice the small overlap matrix of a few dozen basis functions is simply inverted numerically; the value of the analysis is that it shows how sensitive the estimate is to the data near the edge.

![Estimating a mitotic field from one synthetic section. A: the true field m(x) in a bud-shaped region (lower in the dense central core and proximally). B: the raw index M/ρ in squares of about 40 cells, dominated by Poisson noise. C: iterated nearest-neighbour smoothing (r = 3, Theorem 31.6.1 b), normalized inside the tissue so that the edge is not biased by the zeros outside. D: the Poisson maximum likelihood fit (Proposition 31.6.1 a) with 15 low-order cosine functions, solved by iteratively reweighted least squares. The root-mean-square errors are given above each panel](./plots/mitotic-field.py)

## 31.7. Local Control of Division

If all the data of the chick wing bud are pooled, a least-squares fit of the mitotic index $m$ (in percent) against the inverse of the areal density $\rho$ of nuclei in a section (in $\mathrm{\mu m^{-2}}$) gives approximately

$$
m=-4+\frac{0.13}{\rho}.
\tag{31.9}
$$
At $\rho=0.01\,\mathrm{\mu m^{-2}}$, nuclei about $10\,\mathrm{\mu m}$ apart, this gives $m=9\,\%$, and at $\rho=0.0081$ it gives $12\,\%$. The fluctuations are large but the trend is clear. Experiments in which part of the bud is altered show that the control is local, which excludes a freely diffusing inhibitor of division (the hypothetical "chalones") as its basis. The simplest local mechanism is contact inhibition of division, in which each encounter between cells delays the next division ([7.3.22](/7.3.22) for **contact inhibition** in culture).

**Formula 31.7.1 (Collision Model of Contact Inhibition)** Suppose that at density $\rho$ above a threshold the cell cycle length is proportional to the rate $R$ of cell–cell collisions, $\gamma=kR$. Cells of diameter $a$ moving with mean relative speed $c$ collide at the rate $\pi a^2\rho c$ in a dilute suspension, and at the rate $\pi a^2c\rho/(1-\rho v_0)$ when each cell is confined to its free volume $1/\rho-v_0$, $v_0=\pi a^3/6$. Then the mitotic index $m=\tau/\gamma$ is

$$
m=\frac{\tau}{\pi k a^2c}\Big(\frac1\rho-v_0\Big),
\tag{31.10}
$$
linear in $1/\rho$ with a negative intercept, the form of (31.9).

The qualitative agreement is good, the quantitative one tenuous. The cell size $a$, and so $v_0$, changes with density (nuclei enlarge as the index falls); the speed $c$ is unknown; and the measured areal density in a section of thickness $d$ is not the volume density: a nucleus is counted if its center lies within a slab of thickness about $d+a\cos\vartheta$, with $\vartheta$ an acceptance angle for recognizing a cut nucleus, so $\rho_{\mathrm{obs}}=(d+a\cos\vartheta)\rho$.

The fluctuations give an independent test. In thermodynamic terms the collision rate is a pressure, and the free-volume model corresponds to the equation of state $\beta P=\rho/(1-\rho v_0)$. Consider a volume $\Omega$ of tissue in which the number of cells $N$ fluctuates between nominally identical samples, as in an open system in contact with a reservoir at an effective chemical potential $\mu$.

**Theorem 31.7.1 (Number Fluctuations)** In the grand canonical ensemble, $\mathrm{e}^{\beta P\Omega}=\sum_N\frac{\mathrm{e}^{\beta\mu N}}{N!}Q_N(\Omega)$, the mean and variance of $N$ are $\bar N=\partial(\beta P\Omega)/\partial(\beta\mu)$ and

$$
\overline{N^2}-\bar N^2=\bar N\Big(\frac{\partial\beta P}{\partial\rho}\Big)^{-1};\qquad\text{for }\beta P=\frac\rho{1-\rho v_0}:\quad \operatorname{Var}(N)=\bar N(1-\rho v_0)^2 .
$$
If the cells in mitosis are a random fraction $m$ of the cells with the same interactions, the fluctuation of the observed index in a volume $\Omega$ is

$$
\delta m^2=\frac{m}{\rho\Omega}(1-\rho v_0)^2 .
\tag{31.11}
$$

**Proof** Differentiating the logarithm of the grand partition function twice with respect to $\beta\mu$ gives the mean and the variance: $\operatorname{Var}(N)=\partial\bar N/\partial(\beta\mu)=\frac{\partial\bar N}{\partial(\beta P\Omega)}\frac{\partial(\beta P\Omega)}{\partial(\beta\mu)}=\bar N\frac{\partial\bar N}{\partial(\beta P\Omega)}=\bar N\frac{\partial\rho}{\partial\beta P}$. For the free-volume equation of state $\partial\beta P/\partial\rho=(1-\rho v_0)^{-2}$. For the mitotic cells, $\rho$ is replaced by $m\rho$ and $P$ by the partial pressure $mP$, so $\operatorname{Var}(N_M)=m\rho\Omega(1-\rho v_0)^2$ and $\delta m^2=\operatorname{Var}(N_M)/(\rho\Omega)^2$. $\square$

Without excluded volume the counts would be Poisson ($\delta m^2=m/\rho\Omega$); crowding makes the positions more regular and the counts less variable, by the factor $(1-\rho v_0)^2$. The free-volume equation of state is exact for hard rods on a line (the Tonks gas) and an approximation in two and three dimensions. The observed scatter of the chick limb data agrees with (31.11) quite well, but not well enough to establish the crucial factor $(1-\rho v_0)$. Mesenchymal division in the limb is consistent with contact inhibition; it is not proven by these data. In the modern view, the proliferation of limb mesenchyme is driven by AER FGFs, Wnts and Shh acting as mitogens (Shh, for instance, induces cyclin D1 and the G1 regulator *N-Myc*), and density-dependent control acts through the Hippo–YAP pathway ([7.3.22](/7.3.22)); and live imaging and quantitative modeling of the mouse limb bud (Boehm et al. 2010) showed that the spatial differences in proliferation are too small to shape the bud, which elongates mainly by oriented cell behavior: Wnt5a-dependent orientation of divisions and cell polarity, and FGF-stimulated cell movement toward the AER.

![Contact inhibition and number fluctuations. A: mitotic index against inverse density for simulated sections (points) generated with the collision model, Formula 31.7.1 (binomial counts of about 250 nuclei per sample), and the least-squares line, which recovers an equation of the form (31.9). B: Monte Carlo test of Theorem 31.7.1 for hard rods on a line (the Tonks gas, for which the free-volume equation of state is exact): the variance-to-mean ratio of the number of rods in a window falls with the packing fraction ρv0 as (1 − ρv0)², whereas independent (Poisson) positions would give 1](./plots/contact-inhibition.py)

## 31.8. Reconstructing the Fate Map from the Field of Growth

The AER experiments of Section 31.4 led to a conclusion that Percus and Childress state in its classical form: the mesenchyme of the early bud is already restricted to form a limb, and successive restrictions to proximal, then more distal, element types peel off in a fixed temporal sequence as long as the cells are near the AER; thereafter division is under the control of the local environment and shaping is by contact. If this is so, one should be able to reconstruct where each segment came from, without marking a single cell, from the field of cell division $m(x,t)$ alone. Julian Lewis (1975) did this for the chick wing.

**Formula 31.8.1 (Lewis's Reconstruction)** Let $x$ be the distance from the AER along the proximo-distal axis, $A(x,t)$ the transverse area of the bud, $\rho$ the cell density and $m/\tau$ the rate of division per cell. If the bud elongates without mixing, the volume between the AER and a cell increases only by the division of the cells within it, so the distance of the cell from the AER obeys

$$
\frac{\mathrm{d}x}{\mathrm{d}t}=\frac1{A(x,t)\rho(x,t)}\int_0^xA(x',t)\rho(x',t)\frac{m(x',t)}{\tau}\,\mathrm{d}x' .
\tag{31.12}
$$
Integrating backward in time from the positions of the segment boundaries at a late stage gives the positions of their progenitors in the early bud; integrating $m/\tau$ along each trajectory gives the number of divisions each progenitor undergoes while it is within a given distance of the AER.

**Proof** The number of cells between the AER and the moving cell, $\int_0^xA\rho\,\mathrm{d}x'$, changes only by division (there is no flux of cells across a material point), so $\frac{\mathrm{d}}{\mathrm{d}t}\int_0^{x(t)}A\rho\,\mathrm{d}x'=\int_0^xA\rho\frac m\tau\mathrm{d}x'$. If $A\rho$ changes slowly in time compared with the motion, the left-hand side is $A(x)\rho(x)\dot x$. $\square$

Lewis used the measured mitotic fields and an influence distance of $300\,\mathrm{\mu m}$ from the AER. The result was strikingly regular: each of the five element types (humerus, radius and ulna, wrist, metacarpals, phalanges) spends one more cell cycle within $300\,\mathrm{\mu m}$ of the AER than its proximal neighbour. In the progress zone model this is a counting mechanism: the PD clock, read only in the mesenchyme under the influence of the AER, advances by one value per division.

**Example 31.8.1** Let the division rate within the influence zone be uniform, $m/\tau=k$, and $A\rho$ constant. Then (31.12) gives $\dot x=kx$ inside the zone, so a cell starting at $x_0$ leaves it, at $x=X=300\,\mathrm{\mu m}$, after the time $k^{-1}\ln(X/x_0)$, during which it divides $\log_2(X/x_0)$ times. A progenitor with one more division in the zone started at half the distance from the AER. Progenitors of the five segments therefore lie at $X/2$, $X/4$, …, $X/32$: the early fate map is logarithmic, compressed toward the AER, and a fixed number of divisions per segment is equivalent to a geometric spacing of the progenitors, independent of the absolute rate $k$.

![Lewis's reconstruction of the fate map, Formula 31.8.1, for a model field of division (rate high within 300 µm of the AER, lower and declining proximally). A: distance from the AER against time for five progenitors, one per segment, started at successively halved distances from the AER and followed with Eq. (31.12); the shaded band is the zone of AER influence. B: the number of cell cycles each progenitor spends in the zone: successive segments differ by one division (Example 31.8.1), and their progenitors in the early bud lie at roughly geometric distances from the AER](./plots/lewis-fate-map.py)

The modern data do not support a division-counting clock. Direct lineage tracing in the mouse (genetic marking of *Hoxa13*-expressing cells) and the dye-labeling of the chick bud (Section 31.5.1) show that the segments are already partly segregated in the early bud and that their progenitors occupy broad, overlapping regions rather than the narrow geometric layers of Example 31.8.1. The specification of the stylopod by a proximal signal and of distal values by an intrinsic timer (Definition 31.5.3) can produce the same proximal-first sequence without counting divisions. Lewis's calculation remains a model of how much can be inferred from the kinematics of growth, and the reason why the field of division had to be measured accurately.

Percus and Childress also note the third, anterior–posterior level of pattern: the number of digits depends on the width of the AER and the digit identities on a diffusible signal from a posterior zone of polarizing activity, whose dissociation and mixing with the rest of the mesenchyme gives a symmetric pattern, and the ZPA and AER maintain each other. These are the subject of the next chapter.

## Summary

- Anatomy (Definition 31.1.1): stylopod, zeugopod, autopod; three axes (PD, AP, DV). The skeleton and connective tissue come from the somatic lateral plate, the muscles from the somites (quail–chick chimeras), nerves and pigment cells from the neural tube and neural crest.
- Limb field (Definition 31.2.1): a regulative field (Harrison; half-fields form whole limbs; trematode-induced extra limbs). Position by the axial Hox code (forelimb at the anterior border of *Hoxc6*) and RA–Fgf8 antagonism; identity by Tbx5 (forelimb; Holt–Oram syndrome), Tbx4, Pitx1 and Islet1 (hindlimb); FGF beads in the flank induce limbs whose type follows the local Tbx gene.
- Induction: EMT of the somatopleure (Tbx5); Fgf10 in the mesenchyme, Wnt3 and Fgf8 in the ectoderm; two positive loops make outgrowth self-sustaining, a switch with an off and an on state (Example 31.3.1).
- AER (Definition 31.4.1): formed at the DV ectodermal boundary (*Radical fringe*, *En1*; *limbless*, *eudiplopodia*); required for outgrowth, permissive (old and young AERs equivalent), maintained by limb mesenchyme, replaceable by FGF beads; FGF4/8 redundant.
- PD patterning: progress zone model (Definition 31.5.1, Formula 31.5.1; PZ exchanges, irradiation), early specification (dye labeling, cell death after AER removal) and the two-signal model (Definition 31.5.2, Formula 31.5.2: RA and Meis proximally, FGF, Wnt and Cyp26b1 distally), and the signal-plus-timer synthesis (Definition 31.5.3). The Hox code: Hox9/10 stylopod, Hox11 zeugopod, Hox12/13 autopod, with two-phase regulation of *Hoxd*.
- Mitotic field (Section 31.6): Poisson likelihood and least squares (Proposition 31.6.1), projection estimates (Proposition 31.6.2), smoothing kernels (Theorem 31.6.1: iterated nearest-neighbor averaging = $\cos^{2r}$ weights), boundary corrections, Toeplitz sections and the Szegő theorem (Theorem 31.6.2).
- Local control: $m\approx-4+0.13/\rho$; the collision model (Formula 31.7.1) and the fluctuation formula $\delta m^2=m(1-\rho v_0)^2/\rho\Omega$ (Theorem 31.7.1) are consistent with contact inhibition; today, mitogens and oriented cell behavior dominate the explanation of limb bud growth.
- Lewis's reconstruction (Formula 31.8.1): each segment spends one more division in the AER zone; this corresponds to a geometric early fate map (Example 31.8.1); lineage tracing does not support a division-counting clock.

## Questions

1. What would you conclude if a forelimb field, split by a barrier into an anterior and a posterior half, produced one anterior half-limb and one posterior half-limb rather than two complete limbs? Which property of the limb field does Harrison's actual result demonstrate?

   **Answer** Half-limbs would mean that each part of the field is already determined to form its own part of the limb (mosaic behavior), so the pattern would be fixed by the position of cells in the field. Harrison found complete limbs from each half: the field is regulative, each half re-establishes the whole pattern, so cells are specified but not determined at the field stage, and the pattern depends on interactions within the tissue rather than on prior assignment.

2. An FGF bead implanted in the chick flank between the wing and the leg induces a limb with wing features anteriorly and leg features posteriorly. Design two experiments that test whether Tbx5 and Tbx4 are the cause rather than markers of limb type.

   **Answer** Gain of function: express *Tbx4* throughout the flank (for example by a retrovirus) before implanting the bead in the anterior flank; if limb type follows Tbx expression, the induced limb becomes a leg (this is the observed result). Conversely express *Tbx5* in the posterior flank or in the leg field and expect wing-like limbs. Loss of function: block Tbx5 (dominant-negative construct or morpholino) in the anterior part of the field and expect loss of the anterior wing features or of the induced limb. In the mouse, the equivalent tests showed that Pitx1 rather than Tbx4 is the stronger determinant of hindlimb identity.

3. Show from Example 31.3.1 that with $s=0$, $K=1$ the mutual-activation system has an on state only if $a\ge2$, and find the on state for $a=3$. What does the threshold $a=2$ mean biologically?

   **Answer** Symmetric steady states satisfy $u=au^2/(1+u^2)$: $u=0$ or $u^2-au+1=0$, with real positive roots only if $a^2\ge4$. For $a=3$: $u=(3\pm\sqrt5)/2$, $0.38$ (saddle) and $2.62$ (stable on state). The parameter $a$ is the maximal induction of each signal by the other relative to its removal; below 2 the loop is too weak to sustain itself, so a limb bud needs both a sufficient gain of the Fgf10–Fgf8 loop and an initial push past the saddle (from Tbx5 or an FGF bead).

4. Old and young AERs are interchangeable, but old and young progress zones are not. Explain how each result is predicted by the progress zone model, and why the old-PZ-on-young-bud experiment cannot by itself distinguish it from the two-signal model.

   **Answer** In the progress zone model the timer is in the mesenchyme, so exchanging AERs changes nothing, whereas an old PZ carries cells with distal values and a young one cells that can still progress, giving deletions and duplications. In the two-signal model, too, the old PZ consists of cells already specified as distal (autopod) by FGF, and a young PZ contains cells that will still form zeugopod as the bud grows and they escape the RA signal. Both models attribute PD value to the mesenchyme; they differ in how it was acquired (time in the zone versus signals early), which the grafts do not test. Fate mapping of the early bud and the cell death after AER removal discriminate between them.

5. In the progress zone model of Formula 31.5.1 the PZ is $200\,\mathrm{\mu m}$ thick and cells divide every $12\,\mathrm{h}$ in it. A cell that will form the tip of the digits must spend about $60\,\mathrm{h}$ in the zone. Where must it have been at the start? Is the answer biologically reasonable?

   **Answer** $g=\ln2/12\,\mathrm{h}^{-1}=0.0578\,\mathrm{h^{-1}}$; $T=60\,\mathrm{h}$ requires $y_0=d\,\mathrm{e}^{-gT}=200\times2^{-5}=6.25\,\mathrm{\mu m}$, within one cell diameter of the AER. A strict progress zone model therefore requires the most distal fates to come from a very thin subridge layer, which is implausible given cell mixing and the large distal fate-map domains observed; this is one of the quantitative arguments against a pure timing model.

6. For the two-signal model, Formula 31.5.2, take $\lambda=60\,\mathrm{\mu m}$ and $\theta=0.1$. What is the minimum bud length for which a zeugopod domain exists, and how long is it in a bud of $300\,\mathrm{\mu m}$? How would a mutation that halves $\lambda$ for the distal signal only affect the domains?

   **Answer** Each end domain is $\lambda\ln10=138\,\mathrm{\mu m}$, so the zeugopod exists only for $\ell_0>276\,\mathrm{\mu m}$, and in a $300\,\mathrm{\mu m}$ bud it is $24\,\mathrm{\mu m}$ long. With $\lambda_F=30\,\mathrm{\mu m}$ the autopod domain shrinks to $69\,\mathrm{\mu m}$ and the zeugopod grows to $300-138-69=93\,\mathrm{\mu m}$: a shorter-range distal signal enlarges the middle segment at the expense of the hand. The sensitivity of the middle segment to bud size and to the two ranges is a testable prediction.

7. Prove that $r$ successive averagings with weights $(\frac14,\frac12,\frac14)$ produce the kernel $4^{-r}\binom{2r}{r-d}$, and compute its variance. How many smoothing passes reduce the Poisson standard deviation of a single square's index by a factor of 4 (in two dimensions)?

   **Answer** One pass is the distribution of $(B-1)$ with $B\sim\mathrm{Bin}(2,\frac12)$; $r$ passes convolve $r$ such, giving $B_r-r$ with $B_r\sim\mathrm{Bin}(2r,\frac12)$, whose probability at $d$ is $\binom{2r}{r+d}4^{-r}=\binom{2r}{r-d}4^{-r}$; variance $2r\cdot\frac14=r/2$ per direction. The variance of a weighted mean of independent counts is reduced by $\sum W^2$; in one direction $\sum_d\binom{2r}{r-d}^24^{-2r}=\binom{4r}{2r}4^{-2r}\approx1/\sqrt{2\pi r}$, in two directions $\approx1/(2\pi r)$. A factor 4 in standard deviation is a factor 16 in variance: $2\pi r\approx16$, $r\approx2.5$, so three passes, at the price of blurring over about $\sqrt{r/2}\approx1.2$ squares in each direction.

8. Why does the truncated Fourier projection (Theorem 31.6.1 a) sometimes give negative mitotic indices, and how do the smooth weights avoid this? What is the price?

   **Answer** The Dirichlet kernel has negative side lobes; near a steep change in the counts, such as the tissue edge or an empty region, a positive count weighted negatively pushes the estimate below zero (Gibbs ringing). The $\cos^{2r}$ weights decline smoothly to zero, so the kernel is a binomial, nonnegative everywhere, and a nonnegative combination of nonnegative counts cannot be negative. The price is resolution: the smooth kernel blurs features over a wider range for the same effective number of parameters, and fine structure, such as a narrow zone of high division under the AER, is underestimated.

9. Using (31.9), at what density would the mitotic index vanish, and what nuclear spacing does that correspond to? In the collision model, what is $v_0$ in terms of this density, and what does a negative index at still higher density mean?

   **Answer** $m=0$ at $\rho=0.13/4=0.0325\,\mathrm{\mu m^{-2}}$, a spacing $1/\sqrt\rho\approx5.5\,\mathrm{\mu m}$, roughly nuclei in contact. In (31.10) the index vanishes at $\rho=1/v_0$ (cells filling the volume), so the fitted intercept corresponds to close packing (with the areal density standing in for the volume density). A negative index is meaningless: the linear law applies only above the low-density threshold and below close packing, where division stops altogether.

10. In Example 31.8.1, suppose the division rate in the AER zone doubles at a later stage. Does the conclusion "one more division per segment" depend on the rate? What would an experiment that slows division in the distal mesenchyme (for example a cell-cycle inhibitor applied with a bead) predict in a counting model and in the two-signal model?

    **Answer** No: the number of divisions in the zone is $\log_2(X/x_0)$ whatever $k$ is, because both the time to leave and the divisions scale with $1/k$. A counting model predicts that slowing division delays but does not change the sequence of segments, each still made after the same number of divisions, so the final pattern is normal if growth eventually completes (and truncated if the limb runs out of time). The two-signal model predicts that the domains are already specified, so slowing growth makes all segments smaller in proportion, with the middle segment most at risk because it depends on the bud exceeding the length $2\lambda\ln(1/\theta)$.
