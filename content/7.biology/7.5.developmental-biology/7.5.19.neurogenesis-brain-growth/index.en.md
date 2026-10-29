---
title: Neurogenesis and Brain Growth
description: "How neurons are made and arranged. The layers of the neural tube; neuroepithelial cells, radial glia, intermediate progenitors and outer radial glia, interkinetic nuclear migration and the switch from symmetric to asymmetric division; a model of how division modes set neuron number; inside-out lamination, Reelin, the cerebellum and tangential migration; the expansion of the human cortex, microcephaly and cortical folding; Drosophila neuroblasts, lateral inhibition and asymmetric division; adult neurogenesis and its controversy in humans."
---

The neural tube of [7.5.18](/7.5.18) is a single-layered epithelium patterned into domains. This chapter follows its third axis, from the lumen outwards: how the progenitors lining the lumen divide, how they produce first neurons and then glia, and how the newborn neurons migrate to build the layers and nuclei of the brain. The number of neurons, and therefore the size of the brain, is set by how long progenitors proliferate before they begin to make neurons; the differences between a mouse and a human cortex are largely differences in this schedule and in the kinds of progenitor. We also take the shorter route through the insect nervous system, where neuroblasts are chosen by **lateral inhibition** and produce neurons by stereotyped asymmetric divisions, and end with neurogenesis in the adult brain. The guidance of axons, the formation of synapses and the survival of neurons follow in [7.5.21](/7.5.21); the functioning of circuits and their plasticity are the subject of [7.16](/7.16).

## 19.1. The Layers of the Neural Tube

The wall of the closed neural tube is a pseudostratified epithelium: every cell touches both the luminal (apical) surface and the outer (basal) lamina, but the nuclei lie at different heights, so the sheet looks layered. As neurogenesis begins, the wall becomes truly layered. In the spinal cord and hindbrain, three layers form, here in a human neural tube of about five weeks:

| Layer | Contents | Adult fate |
|---|---|---|
| Ventricular zone (VZ), next to the lumen | dividing progenitors | ependyma lining the ventricles and central canal |
| Mantle (intermediate) zone | cell bodies of newborn neurons and glia | grey matter |
| Marginal zone, outermost | axons and glial processes | white matter (after myelination) |

In the spinal cord the mantle zone divides into the dorsal alar plate (sensory relay neurons) and the ventral basal plate (motor neurons), separated by the sulcus limitans, the anatomical trace of the dorso-ventral patterning of [7.5.18](/7.5.18). In the cerebrum and cerebellum a more elaborate arrangement develops (19.4).

**Definition 19.1.1 (Neuroepithelial Cell)** A **neuroepithelial cell** is a progenitor of the early neural tube that spans the epithelium from the apical to the basal surface, keeps apical junctions and an apical primary cilium, and undergoes **interkinetic nuclear migration**: during each cell cycle its nucleus moves basally in G1, replicates its DNA in S phase at the basal side of the ventricular zone, returns apically in G2 and divides at the apical (ventricular) surface.

Interkinetic nuclear migration explains the pseudostratified appearance: at any moment nuclei are found at every height. It was demonstrated by Sauer (1935) from fixed sections and confirmed by labelling: a short pulse of $^{3}$H-thymidine labels nuclei only at the basal side of the VZ, and the labelled nuclei appear at the surface, in mitosis, a few hours later. Apical movement in G2 depends on dynein and microtubules (and in some tissues actomyosin), basal movement is partly passive crowding. Its function is debated; one suggestion is that it exposes nuclei to opposing apical (Notch) and basal signals for different times, and that the time a nucleus spends near the apical surface affects the fate of its daughters.

## 19.2. Neural Progenitors of the Cortex

![Neural progenitors of the developing neocortex. (A) Interkinetic nuclear migration: in a neuroepithelial or apical radial glial cell, which spans the whole wall, the nucleus moves basally in G1, replicates its DNA (S) at the basal side of the ventricular zone, returns in G2 and divides (M) at the apical, ventricular surface. (B) Lineage relations: neuroepithelial cells (NE) divide symmetrically to expand the pool, then become apical radial glia (aRG). aRG divide asymmetrically, renewing themselves and producing a neuron directly or an intermediate progenitor (IP), which divides once or a few times in the subventricular zone to make neurons. Outer radial glia (oRG), abundant in primates, keep only the basal fibre and divide repeatedly in the outer subventricular zone; at the end of neurogenesis radial glia make astrocytes and oligodendrocyte precursors](./plots/progenitors.py)

When neurogenesis begins in the cerebral cortex (around embryonic day 11 in the mouse, week 6-7 in humans), neuroepithelial cells transform into radial glia. The transition requires retinoic acid from the meninges and FGF10, and the cells acquire astroglial features (glutamate transporters, brain lipid-binding protein, Pax6 expression in the dorsal telencephalon) while keeping their epithelial polarity.

**Definition 19.2.1 (Radial Glial Cell)** A **radial glial cell** is a neural stem cell of the embryonic brain whose cell body lies in the ventricular zone, with an apical process at the ventricle and a long basal fibre attached to the pial surface. Apical radial glia (aRG) keep both processes and undergo interkinetic nuclear migration; **outer radial glia** (oRG, also called basal radial glia) have lost the apical process, keep the basal fibre and divide in the outer subventricular zone.

**Definition 19.2.2 (Intermediate Progenitor)** An **intermediate progenitor** (IP, basal progenitor) is a transit-amplifying cell produced by radial glia that loses contact with both surfaces, expresses Tbr2 (Eomes), divides in the subventricular zone (SVZ) once or a few times, and generates neurons.

The discovery that radial glia are the neural stem cells overturned a long-held view. Radial glia had been known since the nineteenth century as scaffolds for migrating neurons; retroviral and live imaging lineage experiments (Malatesta et al. 2000; Noctor et al. 2001) showed that the same cells divide asymmetrically to produce neurons that then climb their mother's fibre. Most cortical neurons, however, come indirectly, through intermediate progenitors: a radial glial cell produces an IP, which in rodents divides once to produce two neurons.

The modes of division change with time.

- Symmetric proliferative divisions (one progenitor gives two progenitors) expand the pool before neurogenesis. The cleavage plane is perpendicular to the ventricular surface, both daughters inherit apical membrane and junctions.
- Asymmetric neurogenic divisions (a progenitor and a neuron or IP) dominate neurogenesis. The daughter that inherits the basal fibre and more of the apical domain remains a radial glial cell; the Par complex (Par-3) is partitioned unequally, so that Notch signalling remains active in one daughter (stemness) while the other, with high Delta, differentiates (a version of lateral inhibition between sisters). The mammalian Pins homologue LGN keeps the spindle parallel to the ventricular surface; oblique divisions generate oRG.
- Symmetric neurogenic divisions (two neurons) end the lineage, typically in IPs.
- At the end of neurogenesis radial glia switch to producing astrocytes and oligodendrocyte precursors (the gliogenic switch, driven by Notch and JAK-STAT signalling through cytokines from the newborn neurons), and the last radial glia become ependymal cells or, in the lateral ventricle, adult neural stem cells (19.7).

Each neuron is born at a definite time, and its time of birth correlates with its fate. Neurogenesis in the mouse cortex lasts about six days and some eleven cell cycles, during which the cycle lengthens from about 8 to 18 hours, mostly by lengthening G1; experimentally lengthening G1 (by inhibiting Cdk4/cyclin D1) promotes neurogenic divisions, shortening it delays them.

## 19.3. How Division Modes Set Neuron Number

The total output of a progenitor pool depends on how many of its divisions are proliferative and how many neurogenic. Takahashi, Nowakowski and Caviness measured, cycle by cycle, the fraction of daughter cells that leave the cycle in the mouse cortex, and turned the measurements into a simple model.

**Formula 19.3.1 (The Q-Fraction Model)** Let $P_k$ be the number of progenitors at the start of cycle $k$ and let a fraction $Q_k$ of the $2P_k$ daughters leave the cycle as neurons (or neurogenic IPs, counted by their output), the fraction $1 - Q_k$ re-entering it. Then

$$
P_{k+1} = 2(1 - Q_k)\,P_k,
\qquad
N_{k+1} = N_k + 2Q_k P_k,
\tag{19.1}
$$

so that after $K$ cycles the number of neurons produced per founder progenitor is $N_K = \sum_{k=1}^{K} 2Q_k\prod_{j<k}2(1 - Q_j)$.

**Theorem 19.3.1 (Critical Leaving Fraction)** If $Q_k = q$ is constant, the pool grows if $q < \tfrac12$, stays constant if $q = \tfrac12$ (every division asymmetric on average) and shrinks if $q > \tfrac12$. For $q > \tfrac12$ the total output of a founder before the pool is exhausted is

$$
N_\infty = \sum_{k=0}^{\infty} 2q\,\bigl(2(1 - q)\bigr)^{k} = \frac{2q}{2q - 1}.
$$

**Proof** From Eq. (19.1), $P_k = \bigl(2(1 - q)\bigr)^{k}P_0$, a geometric sequence with ratio $2(1 - q)$, which exceeds, equals or is below 1 according as $q <, =, > \tfrac12$. The neurons produced in cycle $k$ are $2qP_k$; summing the geometric series with ratio $2(1-q) < 1$ gives the formula. $\square$

The threshold $q = \tfrac12$ is the critical point of a branching process ([7.5.36](/7.5.36)): below it the lineage grows exponentially, above it the lineage becomes extinct after producing a finite number of neurons. In the mouse, $Q$ rises from almost 0 at E11 to 1 at E17, passing $\tfrac12$ late, at about the eighth of the eleven cycles; most neurons are produced in the last three or four cycles, when the pool is largest and $Q$ high.

**Example 19.3.1** With the schedule of the figure (logistic $Q_k$ reaching $\tfrac12$ at cycle 8), one founder produces about 300 neurons. Adding one symmetric proliferative cycle before the same schedule doubles the output to about 600, and $n$ extra cycles multiply it by $2^{n}$. Stretching the same shape of schedule over 28 cycles, of the order estimated for the human cortex, gives about $6\times10^{5}$ neurons per founder, three orders of magnitude more, without any change in the mechanism.

![How the schedule of division modes sets the number of cortical neurons (the Q-fraction model, Formula 19.3.1). (A) In the mouse dorsal cortex about 11 cell cycles span neurogenesis (E11-E17); the fraction Q of daughters that leave the cycle rises from about 0 to 1 (here a logistic curve with Q = 0.5 at cycle 8). The progenitor pool P grows while Q < 1/2 and shrinks after; neurons accumulate mostly in the last cycles. (B) Neurons per founder when the schedule is preceded by extra symmetric proliferative cycles (Q = 0): each extra cycle doubles the output. A schedule of the same shape stretched over 28 cycles gives far more neurons than one over 11](./plots/division-mode-model.py)

The exponential sensitivity of neuron number to the timing of the switch is the basis of the radial unit hypothesis (Rakic 1995): the number of founder radial glia, set by the symmetric divisions before neurogenesis, determines the number of radial columns and so the surface area of the cortex, while the number of neurogenic divisions per founder determines its thickness. Primate cortex has expanded enormously in area and only modestly in thickness, which points to an extension of the proliferative phase, and in primates to the additional amplification provided by oRG and IPs in the outer SVZ (19.5). The model is deterministic; the lineages of individual radial glia vary considerably, and their statistics are treated by the stochastic models of [7.5.36](/7.5.36).

## 19.4. Migration and Lamination

### 19.4.1. The Inside-Out Cortex

The neocortex of mammals has six layers, numbered from the surface (layer I, the marginal zone, mostly fibres) to the depth (layer VI); each contains characteristic neurons with characteristic connections (layer IV receives thalamic input, layer V projects to the brainstem and spinal cord, layers II-III connect cortical areas). The layers form in a remarkable order.

**Definition 19.4.1 (Inside-Out Lamination)** **Inside-out lamination** is the pattern of cortical development in which the earliest-born neurons settle in the deepest layers and each later cohort migrates past them to settle more superficially, so that the depth of a neuron's layer is inversely related to its time of birth.

The evidence is birthdating. A single pulse of $^{3}$H-thymidine (or, today, BrdU or EdU) labels heavily only the cells in their last S phase at the time of injection, since cells that continue dividing dilute the label. Angevine and Sidman (1961) injected pregnant mice at different days and found the heavily labelled neurons in deep layers after early injections and in superficial layers after late ones. The first neurons form a preplate, which the arriving neurons of the cortical plate split into the marginal zone above (Cajal-Retzius cells) and the subplate below; the cortical plate then thickens from the inside out.

![Development of the mammalian neocortex (schematic strips of the dorsal telencephalic wall; ventricle at the bottom, pial surface at the top). Early: a pseudostratified neuroepithelium and the preplate of the first-born neurons. Mid-neurogenesis: apical radial glia in the ventricular zone (VZ) with fibres reaching the pia; outer radial glia (basal fibre only, dashed) and intermediate progenitors in the subventricular zone (SVZ); newborn neurons migrate along the glial fibres through the intermediate zone (IZ) into the cortical plate (CP), below the marginal zone (MZ). Late: the cortical plate holds successive cohorts of neurons; each new cohort migrates past the earlier ones, so the earliest-born neurons lie deepest (teal) and the latest-born most superficial (pink): inside-out](./plots/cortex-development.py)

Migrating neurons climb the radial glial fibres (locomotion), and early neurons, when the wall is thin, move by somal translocation along their own leading process. The stop signal is Reelin, a large secreted glycoprotein made by the Cajal-Retzius cells of the marginal zone. In the *reeler* mouse, which lacks Reelin, the layers form roughly outside-in: later neurons fail to pass their predecessors. Reelin acts through the receptors VLDLR and ApoER2 and the adaptor Dab1, which promote detachment from the glial fibre and the final translocation into the top of the cortical plate, in part by regulating N-cadherin and integrin adhesion. Humans with *RELN* mutations have lissencephaly with cerebellar hypoplasia. Defects of migration more generally (mutations of *LIS1*, *DCX*, tubulin genes, affecting the microtubule-dependent movement of the nucleus) cause lissencephaly ("smooth brain") and band heterotopia, with epilepsy and intellectual disability.

Fate and time of birth are linked: progenitors early in neurogenesis can produce neurons of all layers, while late progenitors are restricted to upper layers. Transplantation experiments in ferrets (McConnell) showed that early progenitors moved into an older host can adopt the host's (later, superficial) fate if transplanted before their last S phase, whereas late progenitors moved into a younger host cannot return to deep-layer fates: competence narrows progressively, as with the temporal series of insect neuroblasts (19.6).

### 19.4.2. Tangential Migration and the Cerebellum

The excitatory (glutamatergic) neurons of the cortex come from the dorsal telencephalon and migrate radially. The inhibitory (GABAergic) interneurons are born in the ventral telencephalon, in the medial and caudal ganglionic eminences, and migrate tangentially over long distances into the cortex, guided by semaphorins (through neuropilin receptors) and other cues, before turning radially into their layers. The reason for this detour is that the dorso-ventral patterning of the telencephalon generates the two neuronal types in different places, while circuits need them mixed.

The cerebellum shows a second germinal zone. Granule cell precursors migrate from the rhombic lip over the surface of the cerebellar anlage to form the external granular layer, where they proliferate in response to Shh secreted by the Purkinje cells beneath; after their last division they migrate inwards, along the fibres of Bergmann glia, past the Purkinje cells to form the internal granular layer. The cerebellum thus forms partly outside-in. Uncontrolled Shh signalling in granule precursors (mutations of *PTCH1*, *SMO*) causes medulloblastoma, the commonest malignant brain tumour of children.

## 19.5. The Growth of the Human Brain

### 19.5.1. Expansion of the Cortex

The human brain has about 86 billion neurons, of which about 16 billion are in the cerebral cortex; the mouse has about 70 million, 14 million cortical. Counts across species show that primate brains scale differently from rodent brains: among primates, neuron number grows almost in proportion to brain mass, whereas rodents add mass faster than neurons (larger, less densely packed neurons). The human brain is a large primate brain with the number of neurons expected for its size.

![Numbers of neurons in the whole brain and in the cerebral cortex of four mammals, counted by the isotropic fractionator (Herculano-Houzel and colleagues; human: Azevedo et al. 2009), against brain mass on logarithmic axes. Among primates neuron number grows almost in proportion to brain mass, whereas rodent brains add mass faster than neurons; the human brain, with about 86 billion neurons of which about 16 billion are cortical, is what a primate brain of its size is expected to be](./plots/neuron-numbers.py)

The developmental basis of the expansion lies in the progenitors. Primates have a large outer subventricular zone, populated by oRG that divide repeatedly, self-renewing and generating IPs that themselves divide several times; this adds proliferative capacity outside the ventricular surface, which is limited in area, and provides additional radial fibres that fan out and so increase the surface of the cortical plate (Hansen et al. 2010; Lui et al. 2011). Human-specific genes contribute:

| Gene | Origin | Effect in models |
|---|---|---|
| *ARHGAP11B* | partial duplication of *ARHGAP11A*, human-specific | expressed in mouse or marmoset cortex, amplifies basal progenitors and induces folding (Florio et al. 2015) |
| *NOTCH2NL* | human-specific Notch2 paralogues (1q21.1) | delays differentiation of radial glia, enlarges organoids; 1q21.1 deletions and duplications cause micro- and macrocephaly |
| *TBC1D3* | hominoid-specific duplications | promotes oRG generation |

Folding follows expansion. A large cortex with a nearly constant thickness must fold to fit the skull, and folding is mechanical: the outer cortical layer grows tangentially faster than the inner layers, and the resulting compressive stress buckles it, much as a stiff skin wrinkles on a soft substrate (gels with a swelling surface layer fold into human-like gyri, Tallinen et al. 2016). Across mammals, folding obeys a simple scaling law.

**Formula 19.5.1 (Universal Scaling of Cortical Folding)** For the cerebral cortices of mammals, the total surface area $A_{\mathrm{t}}$, the exposed (outer) surface area $A_{\mathrm{e}}$ and the cortical thickness $T$ satisfy, to good accuracy,

$$
A_{\mathrm{t}}\,T^{1/2} = k\,A_{\mathrm{e}}^{5/4},
\tag{19.2}
$$

with the same constant $k$ across species and individuals (Mota and Herculano-Houzel 2015), the relation expected for a self-avoiding surface of fixed thickness that minimizes its effective free energy, like crumpled paper. Folding depends on surface area and thickness, not on the number of neurons as such.

### 19.5.2. Microcephaly and the Growing Brain

Microcephaly, a head circumference more than two (severe: three) standard deviations below the mean for age, results when too few neurons are made. Primary hereditary microcephaly (MCPH) is caused by mutations in genes of the centrosome and spindle (*MCPH1*, *WDR62*, *CDK5RAP2*, *ASPM*, *CENPJ*, *STIL*): the brain is small but normally structured, consistent with a premature switch from proliferative to neurogenic divisions or with mitotic delay and death of progenitors, the outcome Formula 19.3.1 predicts. Acquired microcephaly followed the Zika virus epidemic in Brazil in 2015-2016: the virus infects radial glia and other neural progenitors (through the receptor AXL among others), kills them or disturbs their divisions, and in infected human cerebral organoids reduces the progenitor pool; the risk of congenital Zika syndrome is highest for infection in the first trimester.

Growth continues after birth. The human brain at birth is about a quarter to a third of its adult volume, and it continues to grow at the fetal rate during the first year or two, a prolonged fetal-type growth that distinguishes humans from other primates. Postnatal growth adds glia, dendrites, synapses and myelin rather than neurons. Synapse density in the cortex peaks in early childhood and is then pruned; myelination proceeds from back to front and is not complete in the prefrontal cortex until the third decade. During adolescence the grey matter of the cortex thins (synaptic pruning and growth of white matter) and the prefrontal cortex matures last, a developmental account of the prolonged maturation of judgement and self-control.

## 19.6. Neurogenesis in *Drosophila*

### 19.6.1. Proneural Clusters and Lateral Inhibition

In *Drosophila* the ventral neuroectoderm, a band of the embryonic ectoderm specified by the dorso-ventral system ([7.5.14](/7.5.14)), gives rise to the ventral nerve cord. Neuroblasts delaminate from it in five waves, each in a characteristic position.

**Definition 19.6.1 (Proneural Cluster and Neuroblast)** A **proneural cluster** is a group of 4-6 contiguous ectodermal cells that express proneural genes, the bHLH transcription factors of the Achaete-Scute complex, and so are competent to become neural. A **neuroblast** is the neural stem cell that a proneural cluster produces: one cell of the cluster, singled out by Delta-Notch signalling, enlarges, delaminates into the interior and divides asymmetrically to produce neurons and glia, while the other cells of the cluster become epidermis.

The position of each proneural cluster, and the identity of its neuroblast, is set by a grid of positional information ([7.5.15](/7.5.15)): segment polarity genes (*wingless*, *engrailed*, *gooseberry*) provide anterior-posterior addresses within each segment, and the columnar genes *vnd*, *ind* and *msh* (homologues of the vertebrate *Nkx2.2*, *Gsh* and *Msx*, expressed in the same ventral-to-dorsal order as their vertebrate counterparts in the neural tube) provide dorso-ventral addresses. Each neuroblast therefore has a unique identity and a unique lineage. The mutant phenotypes give the logic: in *achaete-scute* mutants neuroblasts are missing; in mutants of *Notch* or *Delta* all cells of the cluster become neuroblasts and the embryo has a hypertrophied nervous system and no ventral epidermis (the "neurogenic" phenotype).

**Formula 19.6.1 (Delta-Notch Lateral Inhibition)** Let $n_i$ be the Notch activity and $d_i$ the Delta level of cell $i$, and $\bar d_i$ the mean Delta of its neighbours. In dimensionless form (Collier et al. 1996)

$$
\dot n_i = \frac{\bar d_i^{\,k}}{a + \bar d_i^{\,k}} - n_i,
\qquad
\dot d_i = v\Bigl(\frac{c_i}{1 + b\,n_i^{\,h}} - d_i\Bigr),
\tag{19.3}
$$

where $c_i$ is the competence of the cell (its proneural level), $a, b > 0$, $k, h \ge 1$. The homogeneous state is unstable when the feedback loop gain exceeds a threshold, in which case small differences are amplified: a cell with slightly more Delta inhibits its neighbours, which make less Delta and inhibit it less.

The model is the juxtacrine form of the activator-inhibitor schemes of [7.5.12](/7.5.12), where its linear stability is analysed. Applied to a single cluster in which competence is slightly higher in the centre, it selects one cell. Larger groups of equivalent cells resolve into a pattern of selected cells separated by inhibited ones, as in the regular spacing of the bristles on the fly's notum; a cell is selected when it reaches the threshold, so the outcome depends on small initial biases, which in vivo include higher proneural gene expression in the centre of a cluster, positive autoregulation of the proneural genes and cis-inhibition of Notch by Delta in the same cell.

![Selection of a single neural precursor from a proneural cluster by lateral inhibition (the Delta-Notch model of Collier et al. 1996, Formula 19.6.1, on a hexagonal sheet of cells). Cells of the cluster (outlined) express proneural genes and can make Delta, with competence highest in the centre; the surrounding cells make a low, constant level of Delta and cannot be selected. Each cell's Notch activity rises with the mean Delta of its six neighbours, and high Notch represses its own Delta. Starting from small random differences (A), feedback amplifies them; the central cell wins, keeps high Delta and low Notch and becomes the neuroblast, and its neighbours are inhibited (B). (C) Delta levels of all cluster cells over time; the winner is drawn in bold](./plots/proneural-selection.py)

### 19.6.2. Asymmetric Division and Temporal Identity

Neuroblasts are stem cells that divide by **asymmetric cell division**. At each mitosis the Par complex (Bazooka/Par-3, Par-6 and aPKC), inherited from the epithelial apical domain, forms an apical crescent, joined by Inscuteable and Pins, which with Mud orients the spindle along the apical-basal axis. aPKC phosphorylates the cell-fate determinants Numb, Prospero and Brat and their adaptor proteins (Miranda, Partner of Numb), which then localize to the basal cortex. The division produces a large apical daughter, the renewed neuroblast, and a small basal ganglion mother cell (GMC) that inherits the determinants: Numb blocks Notch signalling, Prospero enters the nucleus and represses cell-cycle genes and activates neuronal ones, Brat inhibits growth. The GMC divides once more into two neurons or glia. Failure of asymmetric segregation is dangerous: in *brat*, *numb* or *prospero* mutants, both daughters behave as neuroblasts and larval brains form tumours, an early demonstration that loss of asymmetric division can transform stem cells.

The same neuroblast produces different neurons at different times. As it divides, it expresses a temporal sequence of transcription factors, Hunchback, Krüppel, Pdm, Castor and Grainyhead, and each GMC inherits the factor present at its birth, which specifies its neuronal identity (Isshiki et al. 2001). Prolonging Hunchback expression extends the production of early-born neuron types; the sequence advances partly by feedback between the factors and partly by cell division. The temporal series is a second axis of diversity added to the spatial grid: identity = position × birth order, a principle that also applies to the vertebrate cortex (19.4.1) and retina ([7.5.22](/7.5.22)).

![Asymmetric division of a *Drosophila* neuroblast. (A) The neuroblast delaminates inwards from the neuroectoderm. At mitosis the Par complex (Bazooka/Par-3, Par-6, aPKC) and Inscuteable-Pins form an apical crescent; aPKC phosphorylates the fate determinants Numb, Prospero and Brat (with their adaptor Miranda) so that they localize to the basal cortex, and Pins-Mud orients the spindle along the apical-basal axis. (B) The large apical daughter renews the neuroblast; the small basal daughter, the ganglion mother cell (GMC), inherits Numb, Prospero and Brat and divides once more into two neurons or glia. (C) Successive GMCs born from one neuroblast inherit a temporal series of transcription factors (Hunchback, Krüppel, Pdm, Castor, Grainyhead), so birth order gives each neuron a distinct identity](./plots/neuroblast-division.py)

### 19.6.3. Vertebrates

Lateral inhibition also selects neural precursors in vertebrates. In the *Xenopus* neural plate, primary neurons arise in three longitudinal stripes on each side; within each stripe, cells expressing the proneural gene *neurogenin* and *Delta* are scattered among non-neural neighbours, and injection of RNA for dominant-negative Delta increases their number while active Notch decreases it (Chitnis et al. 1995). In the mammalian cortex, Notch signalling keeps radial glia as progenitors. Its effector Hes1 oscillates with a period of about 2-3 hours, driven by delayed negative autoregulation (the same kind of oscillator as the segmentation clock of [7.5.23](/7.5.23)); Hes1 oscillation drives antiphase oscillation of the proneural factors Ascl1 and Neurogenin2 and of Delta. Progenitors in which these factors oscillate remain progenitors, whereas sustained Ascl1 or Neurogenin2 expression drives neuronal differentiation (Imayoshi et al. 2013): the dynamics of the signal, not only its level, carries the decision.

## 19.7. Adult Neurogenesis

**Definition 19.7.1 (Adult Neurogenesis)** **Adult neurogenesis** is the generation of new neurons from neural stem cells in the adult nervous system, followed by their migration, differentiation and integration into existing circuits.

For most of the twentieth century the adult mammalian brain was held to make no new neurons. Altman (1962-1965) found $^{3}$H-thymidine-labelled neurons in the dentate gyrus and olfactory bulb of adult rats, but the finding was largely ignored until Nottebohm showed seasonal neurogenesis in the song-control nuclei of canaries (1980s) and markers and BrdU labelling established it in rodents. Two neurogenic niches are well characterized in rodents.

- The ventricular-subventricular zone (V-SVZ) of the lateral ventricles, where slowly dividing type B cells (descendants of embryonic radial glia, with an apical cilium touching the ventricle) generate transit-amplifying cells and neuroblasts that migrate as chains along the rostral migratory stream to the olfactory bulb, where they become interneurons.
- The subgranular zone of the hippocampal dentate gyrus, which produces granule neurons that integrate into the circuit and contribute to pattern separation in memory; their production is increased by exercise and enriched environments and decreased by stress and age.

In humans the evidence is mixed. Eriksson et al. (1998) found BrdU-labelled neurons in the hippocampus of cancer patients who had received BrdU for diagnosis; Spalding et al. (2013) used the atmospheric $^{14}$C released by nuclear bomb tests in the 1950s-60s as a birth date stamp in neuronal DNA and estimated that about 700 neurons are added to each hippocampus daily, with a modest decline with age, while the human olfactory bulb receives almost no new neurons. Neuroblasts of the V-SVZ seem instead to enter the adjacent striatum (Ernst et al. 2014). Later histological studies disagreed: Sorrells et al. (2018) found few or no immature neurons in the adult human dentate gyrus, whereas Boldrini et al. (2018) and Moreno-Jiménez et al. (2019) found thousands, declining with age and in Alzheimer disease. The disagreement turns largely on the preservation of post-mortem tissue (some markers degrade within hours) and on how immature neurons are identified; single-cell transcriptomic studies since then have also disagreed. The existence of adult hippocampal neurogenesis in humans at a level that matters for function therefore remains an open question, while its existence in rodents is firmly established.

## Summary

| Progenitor | Location | Division | Output |
|---|---|---|---|
| Neuroepithelial cell (Definition 19.1.1) | VZ, spans wall | symmetric, IKNM | more progenitors; radial glia |
| Apical radial glia (Definition 19.2.1) | VZ, spans wall | asymmetric, IKNM | self + neuron or IP; late: glia, ependyma, adult stem cells |
| Outer radial glia | outer SVZ, basal fibre | asymmetric, repeated | self + IPs; abundant in primates |
| Intermediate progenitor (Definition 19.2.2) | SVZ | symmetric neurogenic (1-few rounds) | neurons |
| *Drosophila* neuroblast (Definition 19.6.1) | interior | asymmetric, Par/Numb/Prospero | self + GMC → 2 neurons; temporal series |

- The neural tube becomes ventricular, mantle and marginal layers; interkinetic nuclear migration gives the pseudostratified epithelium (Definition 19.1.1).
- Neuron number is exponentially sensitive to the schedule of division modes (Formula 19.3.1); the leaving fraction $q = \tfrac12$ is critical (Theorem 19.3.1), and extra proliferative cycles multiply output (Example 19.3.1), the basis of the radial unit hypothesis.
- The cortex forms inside-out (Definition 19.4.1); Reelin stops migration (*reeler* is inverted); interneurons migrate tangentially from the ganglionic eminences; the cerebellum has an external germinal layer driven by Shh.
- Human cortical expansion relies on oRG and human-specific genes (*ARHGAP11B*, *NOTCH2NL*); folding obeys $A_{\mathrm{t}}T^{1/2} = kA_{\mathrm{e}}^{5/4}$ (Formula 19.5.1); microcephaly reflects too few neurons (MCPH genes, Zika).
- Lateral inhibition (Formula 19.6.1) selects one neuroblast per proneural cluster; asymmetric division and a temporal series of transcription factors specify lineages.
- Adult neurogenesis (Definition 19.7.1) is established in rodent V-SVZ and dentate gyrus; its extent in humans is disputed.

## Questions

1. A pregnant mouse is injected once with BrdU at E12 and another with EdU at E16; the pups are examined at P7. Where in the cortex do you expect the heavily BrdU-labelled and the heavily EdU-labelled neurons, and why must one look at heavily labelled cells only? What would you see in a *reeler* mouse?

   **Answer** BrdU at E12 labels neurons born then, which settle in deep layers (VI, V); EdU at E16 labels late-born neurons, in superficial layers (II-III). Only cells that divided once after the pulse (or not at all) keep a heavy label; cells that kept dividing dilute it, so the heavily labelled cells mark those in their last S phase at the time of the pulse, which is the birth date. In *reeler* the order is roughly inverted: E16-born neurons end up deep, beneath the earlier-born ones, because later cohorts fail to migrate past their predecessors without the Reelin stop signal.

2. Use Theorem 19.3.1 to compute the output of a founder progenitor with constant leaving fraction $q = 0.6$, and with $q = 0.51$. Interpret the result for a progenitor pool near the critical point.

   **Answer** $N_\infty = 2q/(2q - 1)$: for $q = 0.6$, $1.2/0.2 = 6$ neurons; for $q = 0.51$, $1.02/0.02 = 51$ neurons. Near the critical point $q = \tfrac12$ the output diverges as $1/(2q - 1)$, so small changes in the balance of division modes cause large changes in neuron number; that sensitivity makes the schedule an effective evolutionary lever (and makes the system vulnerable to mutations affecting spindle orientation or cell-cycle length).

3. In the model of Example 19.3.1, the human cortex needs about $1.6\times10^{10}$ neurons. If each founder produced about 300 neurons (the mouse schedule), how many founders would be needed? Compare with the alternative of keeping the founder number of a mouse (roughly $5\times10^{4}$ per hemisphere, an order-of-magnitude assumption) and adding extra cycles; how many would be needed?

   **Answer** $1.6\times10^{10}/300 \approx 5\times10^{7}$ founders. With $10^{5}$ founders in total (two hemispheres) at 300 neurons each one gets $3\times10^{7}$ neurons; the ratio required is about $530 \approx 2^{9}$, so about nine extra symmetric cycles before neurogenesis would suffice. A few extra rounds of proliferation (days of development) thus account for a thousandfold expansion, which is why changes in the timing of the switch, and the extra amplification by oRG and IPs, are plausible routes to the primate cortex.

4. Explain why mutations in the centrosomal protein ASPM cause microcephaly with a normally laminated cortex. Which parameter of Formula 19.3.1 would such mutations change?

   **Answer** ASPM is needed for spindle positioning and for the proper timing of mitosis in neuroepithelial cells and radial glia; without it, more divisions are oblique or delayed, and progenitors leave the cycle (become neurons or IPs) or die prematurely. The progenitor pool is depleted early: $Q_k$ rises sooner, or the pool is reduced by death, so the total output falls exponentially while the program of neuronal identity and migration is intact, which preserves lamination.

5. In *Drosophila*, what phenotype do you expect for embryos lacking *Delta*, and for embryos in which one cell of a proneural cluster has been removed by laser ablation just after the neuroblast was selected? Explain both with Formula 19.6.1.

   **Answer** Without Delta no cell receives inhibition ($\bar d_i = 0$ for all, so $n_i \to 0$), all cells of the cluster keep high proneural activity and become neuroblasts: the neurogenic phenotype, excess neurons and loss of ventral epidermis. If the selected neuroblast is ablated before its neighbours are committed, they lose the inhibitory Delta signal; Notch activity falls, and one of the remaining competent cells is selected instead (replacement), as the experiments of Doe and Goodman showed in grasshopper embryos. Once committed, the neighbours no longer respond.

6. Design an experiment to test whether the temporal identity of a *Drosophila* neuroblast depends on cell division or on an intrinsic clock.

   **Answer** Arrest the neuroblast's division (for example with a mutation in *string*/Cdc25, or by inducible cell-cycle inhibitors) and follow the expression of the temporal factors. If the Hb → Kr transition requires cytokinesis, arrested neuroblasts stay Hb-positive (as Grosskortenhaus et al. 2005 found for this transition); if transitions continue in arrested cells, they are cell-intrinsic and time-dependent (later transitions, Kr → Pdm → Cas, proceed in arrested neuroblasts). The two can also be distinguished by misexpressing a factor in a pulse and checking which progeny are affected.

7. Hes1 oscillates in neural progenitors with a period of about 2-3 hours. Using what you know of delayed negative feedback, explain why a delay is necessary, and why oscillating rather than steady Ascl1 can maintain a progenitor.

   **Answer** A protein that represses its own gene reaches a steady state if feedback is immediate; oscillation requires that repression act on a gene whose product appears only after a delay (transcription, splicing, export, translation) comparable to or longer than the protein's lifetime; for Hes1 the delay is tens of minutes and the half-lives of the mRNA and protein are about 20 minutes, which gives periods of a few hours (a delayed-feedback oscillator, as in [7.5.23](/7.5.23)). Ascl1 driven by repression from Hes1 oscillates in antiphase; short pulses of Ascl1 activate cell-cycle genes but not the slower-accumulating neuronal differentiation programme, whereas sustained Ascl1 accumulates the targets that drive differentiation. The cell thus reads the dynamics, and oscillating Notch signalling between neighbours keeps both in the progenitor state.

8. Two laboratories disagree about whether adult humans make new hippocampal neurons. List three methodological factors that could explain the disagreement and propose a design that would settle it.

   **Answer** Factors: post-mortem interval and fixation (markers such as doublecortin are rapidly degraded), the specificity of markers for immature neurons (DCX and PSA-NCAM are also expressed by other cells), and the age, health and medication of the donors; also the sensitivity of single-nucleus RNA sequencing for rare cell types. A decisive design would combine rapidly fixed tissue (neurosurgical resections or short post-mortem intervals with controlled fixation) with birth dating that does not depend on markers, such as $^{14}$C dating of sorted neuronal nuclei across ages or, prospectively, labelling with nucleoside analogues given for medical reasons, together with standardized marker panels validated in primate tissue.

9. Why might the cerebellum be particularly sensitive to Shh pathway mutations after birth, and what does this predict about the age at which medulloblastoma arises?

   **Answer** Cerebellar granule cell precursors proliferate in the external granular layer after birth (in humans for about the first year) in response to Shh secreted by Purkinje cells; constitutive activation of the pathway (loss of *PTCH1* or *SUFU*, gain of *SMO*) keeps them dividing and blocks their exit from the cycle. Tumours of this subgroup (SHH medulloblastoma) therefore arise when this proliferating population exists: in infants and young children (with a second peak in adults, from residual precursors), and germline *PTCH1* or *SUFU* mutations (Gorlin syndrome) predispose to them in early childhood.
