---
title: "Drosophila I: Oogenesis and the Maternal Body Axes"
description: "How the Drosophila egg acquires its axes before fertilization. The syncytial embryo; oogenesis in the egg chamber (germline cysts, nurse cells, follicle cells, ring canals); the two Gurken signals, the polarized microtubule network and the localization of bicoid, oskar, nanos and gurken mRNAs; pole plasm; the anterior, posterior and terminal maternal systems (Bicoid as transcription factor and translational repressor, Nanos and Pumilio repressing hunchback, Caudal, Torso and its local activation); the formation of the Bicoid gradient and its accumulation time; the dorsal-ventral cascade from Pipe through the perivitelline protease cascade and Toll to the nuclear Dorsal gradient, its homology with innate immunity and its threshold readout; and the Sog-Tolloid shuttle that concentrates Dpp at the dorsal midline."
---

The body plan of *Drosophila* is laid down before the embryo has cells. During **oogenesis** the mother places a few messenger RNAs and proteins at defined positions in the egg; after **fertilization** they are translated into gradients that spread through a common cytoplasm and give every nucleus a pair of coordinates, one along the anterior–posterior axis and one along the dorsal–ventral axis. This chapter follows that information from its origin in the egg chamber to the first **zygotic genes** that read it. The genes involved were found as **maternal-effect genes** in the screens of [7.4.20](/7.4.20), whose genetic logic we take as known; here we ask what their products do, how the gradients form and how sharply they can be read. The quantitative theory of a **morphogen** gradient and of **positional information** is that of [7.5.11](/7.5.11); this chapter applies it to the fly and adds the features that only a syncytium allows. The next chapter, [7.5.15](/7.5.15), takes the anterior–posterior coordinate down to segments and segment identity. The dorsal–ventral system reappears in [7.5.16](/7.5.16), where vertebrates use the same pair of molecules, BMP and Chordin, with the axis inverted.

## 14.1. The Fly and Its Early Embryo

*Drosophila melanogaster* develops from egg to adult in about ten days at 25 °C: one day of embryogenesis, three larval instars over about four days, and about four days of metamorphosis in the pupa ([7.5.33](/7.5.33)). The egg is about 500 µm long and 180 µm wide, and its shell already shows the axes: the micropyle, through which the sperm enters, marks the anterior pole, and the two dorsal appendages, respiratory filaments made by the follicle cells, mark the dorsal side.

The embryo begins as a syncytium ([7.5.5](/7.5.5)). The zygotic nucleus divides about every 9 min, without **cytokinesis**; at cycles 8–9 most nuclei migrate to the periphery, and at cycle 10 they form a single layer under the plasma membrane, the syncytial blastoderm. A few nuclei that reach the posterior pole earlier are enclosed by membranes at cycles 9–10 to form the pole cells, the precursors of the germ line. The cycles then lengthen, and in the long interphase of cycle 14, about 2.5 h after fertilization, membranes grow down between the roughly 6000 cortical nuclei and enclose each in a cell: cellularization. The **mid-blastula transition** coincides with this slowing: most zygotic transcription starts in cycles 10–14, and the first patterning genes are among the earliest transcribed. Gastrulation follows at once ([7.5.9](/7.5.9)).

Two consequences of the syncytium matter for patterning. First, proteins translated from localized maternal mRNAs can diffuse from nucleus to nucleus without crossing membranes, so a gradient of a transcription factor can position gene expression directly; this is **syncytial specification**. Second, all of this happens fast, in about two hours, which limits how close to a steady state any gradient can come (14.3).

![The *Drosophila* life cycle and the syncytial embryo. A: at 25 °C embryogenesis takes about one day, the three larval instars about four days and the pupa about four days. B: the first thirteen nuclear cycles are divisions without cytokinesis. At cycle 8 the nuclei, still inside the yolk, begin to migrate outwards; by cycle 10 they lie in a single layer at the cortex, and the pole cells (purple), the future germ line, have budded off at the posterior pole. In the interphase of cycle 14 membranes enclose about 6000 nuclei (cellular blastoderm), and gastrulation begins with the ventral furrow (red). Lateral views, anterior to the left and dorsal up](./plots/early-embryo.py)

The anterior–posterior pattern of the larva is a sequence of non-segmental and segmental regions: the acron at the anterior tip, three head segments that fuse to form the head, three thoracic segments T1–T3, eight abdominal segments A1–A8 and the telson at the posterior tip. The maternal-effect mutations that disrupt this sequence fall into three classes, and a fourth class disrupts the dorsal–ventral axis. Each class deletes a defined region, and this is how the four maternal coordinate systems were first recognized.

| System | Representative genes | Mutant phenotype (embryos of mutant mothers) | Key product |
|---|---|---|---|
| Anterior | *bicoid*, *exuperantia*, *swallow* | head and thorax missing, often replaced by a mirror-image telson | Bicoid, a homeodomain transcription factor |
| Posterior | *oskar*, *vasa*, *tudor*, *nanos*, *pumilio* | abdomen missing; *oskar*, *vasa*, *tudor* also lack pole cells | Nanos, a translational repressor |
| Terminal | *torso*, *torso-like*, *trunk* | acron and telson missing | Torso, a receptor tyrosine kinase |
| Dorsal–ventral | *gurken*, *torpedo*, *pipe*, *Toll*, *dorsal*, *cactus* | dorsalized (all cells dorsal) or ventralized embryos | Dorsal, an NF-κB family transcription factor |

## 14.2. Oogenesis and the Localization of Maternal mRNAs

### 14.2.1. The Egg Chamber

Each of the two ovaries consists of about 16 ovarioles, assembly lines in which egg chambers mature in sequence. At the anterior tip, in the germarium, two or three germline **stem cells** sit in a **stem-cell niche** formed by somatic cap cells, which keep them undifferentiated by Dpp signalling ([7.3.24](/7.3.24)). Each stem cell divides asymmetrically; the daughter that leaves the niche, the cystoblast, divides four more times with incomplete **cytokinesis**. The result is a cyst of 16 cells connected by ring canals, cytoplasmic bridges stabilized by actin. Because the divisions are synchronous and every bridge persists, two of the 16 cells have four ring canals; one of them becomes the oocyte, and the other 15 become nurse cells. The nurse cells replicate their DNA without dividing until they reach several hundred copies of the genome (**polyploidy**) and transcribe and export into the oocyte most of the RNA, protein and organelles it needs. A monolayer of somatic follicle cells, about 650 at first, surrounds the cyst; it secretes the vitelline membrane and the chorion and, as we will see, carries the dorsal–ventral information of the egg.

Egg chambers pass through 14 stages in about a week. At stage 10 the oocyte occupies the posterior half of the chamber; the follicle cells over it are columnar and those over the nurse cells have stretched into a thin squamous layer. At stage 11 the nurse cells contract and dump their cytoplasm into the oocyte within about half an hour, while the oocyte cytoplasm streams to mix it, and the nurse cells then die.

### 14.2.2. Two Gurken Signals Polarize the Oocyte

The axes of the egg are set by a dialogue between the oocyte and the follicle cells, carried in both directions by the same oocyte product, Gurken, a TGF-α-like ligand of the EGF receptor (encoded in flies by *torpedo*, also called *Egfr*). The receptor is a **receptor tyrosine kinase** that signals through the **MAP kinase cascade**.

1. *First signal, posterior (stages 5–7).* The oocyte nucleus lies at the posterior of the oocyte, and *gurken* mRNA is translated next to it. Gurken reaches only the terminal follicle cells at the posterior end of the chamber, which adopt a posterior fate (the terminal cells at the anterior end, lacking the signal, remain anterior). The posterior follicle cells then send a signal, still unidentified, back to the oocyte. Its effect is to localize the polarity protein Par-1 to the posterior cortex and to exclude **microtubule** **nucleation** from there.
2. *Microtubule reorganization.* The oocyte **microtubules** are nucleated at the anterior and lateral cortex, not from a **centrosome**, so their **minus ends** lie there; their **plus ends** point, on average, posteriorly. The bias is weak: live imaging showed a network in which only slightly more plus ends grow towards the posterior than towards the anterior (Parton and colleagues, 2011). The weak bias is enough, because motor-driven transport averaged over many runs converts it into a net drift.
3. *Second signal, dorsal (stages 8–10).* The nucleus moves along the microtubules to one point of the anterior cortex. Its position is random with respect to the rest of the chamber, and wherever it comes to rest it defines the dorsal side: *gurken* mRNA is now localized in a crescent between the nucleus and the cortex, and Gurken signals to the overlying follicle cells, which become dorsal (14.5).

Mutations in *gurken* (in the mother's germ line) or in *torpedo* (in her follicle cells) therefore affect both axes. Mosaic experiments in which only the germ line or only the follicle cells were mutant (Schüpbach, 1987) showed that *gurken* is required in the oocyte and *torpedo* in the follicle cells: the information flows from germ line to soma, then back.

### 14.2.3. Localizing the Axis mRNAs

Four mRNAs are delivered to defined places, each by elements in its 3′ untranslated region; transplanting the 3′ untranslated region of one mRNA onto the coding sequence of another moves the second mRNA to the place of the first.

- *bicoid* mRNA is made in the nurse cells, bound there by Exuperantia and transported into the oocyte. Inside, it is carried by **dynein**, a minus-end-directed motor, to the anterior cortex, where it remains anchored (with Swallow and Staufen) until **egg activation**. It is the first mRNA whose transport was watched in living egg chambers, by tagging it with stem loops recognized by the bacteriophage MS2 coat protein fused to GFP (Weil and colleagues, 2006). About 90 % of the mRNA ends up in the anterior 20 % of the egg.
- *oskar* mRNA is carried by **kinesin**-1, a plus-end-directed motor, to the posterior pole. Its translation is repressed by Bruno until it arrives; at the posterior, Oskar protein recruits more Oskar mRNA and Par-1, a positive feedback that makes the localization self-sustaining.
- *nanos* mRNA is not actively transported. It diffuses throughout the oocyte, mostly bound by the translational repressors Smaug and Cup, and is trapped and derepressed only where Oskar has assembled pole plasm at the posterior pole.
- *gurken* mRNA is transported to the oocyte nucleus by **dynein** and translated there (14.2.2).

**Definition 14.2.1 (Pole plasm)** The **pole plasm** is the specialized cytoplasm at the posterior pole of the *Drosophila* oocyte and egg, assembled on Oskar protein and containing Vasa, Tudor, *nanos* mRNA and the other components needed both to form the abdomen and to specify the pole cells as **primordial germ cells**; it is the **germ plasm** of the fly ([7.5.27](/7.5.27)).

**Example 14.2.1 (Oskar is sufficient to organize pole plasm)** If the *oskar* coding sequence is fused to the *bicoid* 3′ untranslated region, *oskar* mRNA is transported to the anterior pole instead of the posterior. Embryos from such mothers form pole cells at both poles and an abdomen in the anterior half of the embryo, a mirror image of the normal one, with loss of the head and thorax (Ephrussi and Lehmann, 1992). Two conclusions follow. Oskar is not merely required but sufficient to assemble functional pole plasm wherever it is placed, so the other components (Vasa, Tudor, *nanos* mRNA) are recruited by it rather than being independently localized. And the abdomen-forming activity of the pole plasm acts at a distance, since it suppresses head and thorax development over half the embryo: that activity is Nanos protein (14.3.2).

![Two Gurken signals and the localization of the axis mRNAs during oogenesis. A, stages 6–7: the oocyte nucleus lies at the posterior; Gurken (yellow) signals through Torpedo (EGFR) to the terminal follicle cells, which adopt a posterior fate and signal back to the oocyte (dashed), so that its microtubules are reorganized. B, stages 9–10: the nucleus has moved to an anterior-dorsal corner; Gurken now signals to the overlying follicle cells, which become dorsal. bicoid mRNA (pink) is anchored at the anterior cortex after dynein-dependent transport, oskar mRNA (green) at the posterior pole after kinesin-dependent transport; nanos mRNA is trapped later in the oskar-dependent pole plasm. The nurse cells supply the oocyte through ring canals; the border cells migrate between them towards the oocyte. Sagittal sections, anterior to the left and dorsal up](./plots/egg-chamber.py)

## 14.3. The Anterior–Posterior Axis

### 14.3.1. Bicoid: A Morphogen Made at One Pole

At egg activation the localized *bicoid* mRNA is polyadenylated and translated. The protein spreads into the embryo and is degraded, producing a gradient that is roughly exponential, with a **decay length** of about 100 µm, about 20 % of the egg length. Bicoid is a homeodomain transcription factor that enters the nuclei and activates its targets in a concentration-dependent way, and it has a second activity: it binds the 3′ untranslated region of the uniformly distributed maternal *caudal* mRNA and represses its translation, so that Caudal protein forms the opposite gradient.

Bicoid satisfies the experimental criteria for a morphogen ([7.5.11](/7.5.11)) by the scheme "find it, lose it, move it". It is found in a gradient, highest where the head forms; embryos lacking it form no head and thorax; and when *bicoid* mRNA is injected into the middle of a *bicoid*-deficient embryo, head structures form at the injection site and thorax structures on either side of it, while injection at the posterior pole of a wild-type embryo produces a second head there (Driever and Nüsslein-Volhard, 1988; Driever and colleagues, 1990). Changing the dose shifts the **fate map**: with two extra copies of *bicoid* in the mother, the cephalic furrow and the boundary of zygotic *hunchback* expression move posteriorly, by an amount of the order of the **decay length** times $\ln 2$ per doubling, as an exponential gradient read at a fixed threshold predicts.

The theory of such a gradient (synthesis at a source, diffusion with coefficient $D$, first-order degradation with rate $k$, decay length $\lambda = \sqrt{D/k}$) is developed in [7.5.11](/7.5.11). Two features specific to the fly embryo are taken up here.

**Formula 14.3.1 (Bicoid gradient formation)** Let $c(x, t)$ be the Bicoid concentration at distance $x$ from the anterior pole of an embryo of length $L$, made at rate $s(x)$ in the anterior region where its mRNA is localized. Then

$$
\frac{\partial c}{\partial t} = D\,\frac{\partial^2 c}{\partial x^2} - k\,c + s(x), \qquad \frac{\partial c}{\partial x}(0, t) = \frac{\partial c}{\partial x}(L, t) = 0, \qquad c(x, 0) = 0,
\tag{14.1}
$$

whose steady state away from the source is $c_\infty(x) \propto \cosh[(L - x)/\lambda]$, an exponential $\mathrm{e}^{-x/\lambda}$ when $L \gg \lambda$. For a source concentrated at $x = 0$ in a long embryo, the local accumulation time, the mean time at which $c(x, t)$ approaches $c_\infty(x)$, is

$$
\tau(x) = \frac{1}{2k}\left(1 + \frac{x}{\lambda}\right)
\tag{14.2}
$$

(Berezhkovskii, Sample and Shvartsman, 2010): it grows linearly with the distance from the source, and the time to come within a few percent of the steady state is longer still.

**Example 14.3.1 (Is the Bicoid gradient at steady state?)** Measured values are of the order of $D \approx 1$–$7\,\mathrm{\mu m^2\,s^{-1}}$ (photobleaching measurements, **FRAP**, give the low end and fluorescence correlation the high end) and a protein lifetime $1/k$ of the order of 50 min. With $D = 4\,\mathrm{\mu m^2\,s^{-1}}$ and $1/k = 50\,\mathrm{min}$, $\lambda = \sqrt{4 \times 3\,000}\,\mathrm{\mu m} \approx 110\,\mathrm{\mu m}$, and Eq. (14.2) gives $\tau = 25\,\mathrm{min}$ at the pole, $50\,\mathrm{min}$ at $x = \lambda$ and about $80\,\mathrm{min}$ at mid-embryo. The numerical solution in the figure shows that the anterior half reaches 90 % of its steady value before cellularization, about 150 min after egg activation, and the posterior half does not. Positions far from the source are read while their concentration is still rising, so either the readout is timed, or other gradients (Nanos, Caudal and the gap proteins, [7.5.15](/7.5.15)) take over posteriorly. Both are found.

![Formation of the Bicoid gradient (Formula 14.3.1), solved numerically on a 500 µm embryo with no-flux ends; synthesis in the anterior 10 % starts at egg activation and continues to cellularization. D = 4 µm²/s and a protein lifetime of 50 min give a decay length of 110 µm. A: profiles at successive times, normalized to the steady value at the anterior pole (steady state dashed); the anterior approaches its steady level first. B: time at which the concentration at each position reaches 90 % of its steady value; it grows linearly with distance, as Eq. (14.2) predicts, and beyond about 230 µm (45 % of egg length) is not reached before cellularization (dotted line)](./plots/bicoid-nuclear-cycles.py)

Measurements of a Bicoid–GFP fusion in living embryos added a surprising precision. The nuclear concentration at a given position is the same, within about 10 %, from cycle 10 to cycle 14, although the number of nuclei doubles at each cycle, and it is reproducible between embryos to about the same accuracy; the boundary of zygotic *hunchback* expression, set by a threshold of Bicoid with a **Hill coefficient** of about 5, lies at the same position to within about one nuclear diameter, 2 % of the egg length (Gregor, Tank, Wieschaus and Bialek, 2007). A boundary set by a threshold $c_{\mathrm{T}}$ has positional error $\delta x = \lambda\,\delta c/c$, so 10 % noise in concentration corresponds to about 10 µm: the precision of the pattern is close to what the gradient itself allows, and how the nuclei average out the noise of a few hundred molecules is a central question of the quantitative analysis in [7.5.11](/7.5.11).

**Remark 14.3.1** Early models, including those of Percus and Childress, treated the Bicoid gradient as one-dimensional, a concentration averaged over each cross section of the egg. That is an approximation in two respects. The protein, like its mRNA, is concentrated in the cortical cytoplasm under the membrane, where the nuclei are, while the central yolk contains little; the relevant geometry is a thin shell, and the axial profile of the averaged concentration differs from that in the nuclear layer. And the mRNA itself is not a point source: it forms its own short gradient over the anterior 20 % of the egg and is degraded at cellularization. The source is therefore neither short-lived nor point-like, as Percus and Childress assumed, but it is still localized well enough that Eq. (14.1) with a source term confined to the anterior describes the protein profile.

### 14.3.2. Nanos and the Hunchback Gradient

The posterior system has a single essential task. Maternal *hunchback* mRNA is distributed uniformly; in the posterior, Nanos protein, made from the *nanos* mRNA trapped in the pole plasm and spreading forward in a gradient, binds with Pumilio and Brat to Nanos response elements in the *hunchback* 3′ untranslated region and represses its translation. In the anterior, Bicoid activates transcription of the zygotic *hunchback* gene. The two inputs reinforce each other, and Hunchback protein is high in the anterior half of the embryo and drops steeply near the middle. Nanos is thus a translational repressor, not a transcription factor, contrary to what early modelling literature assumed; its RNA-binding partner Pumilio is the sequence-specific component.

**Example 14.3.2 (What is the posterior system for?)** Embryos of *nanos* mutant mothers lack the abdomen, and in them maternal Hunchback protein is present throughout the embryo. Two hypotheses explain the phenotype: Nanos might be an instructive abdominal signal, or it might act only by removing Hunchback, which represses the abdominal **gap genes** *knirps* and *giant*. The test is the double mutant. Embryos from mothers lacking both maternal *hunchback* and *nanos* activity form a normal abdomen (Hülskamp, Pfeifle and Tautz, 1989; Irish, Lehmann and Akam, 1989). Nanos is therefore dispensable once maternal Hunchback is gone, and its only essential role in abdominal patterning is to keep maternal *hunchback* mRNA from being translated in the posterior. The logic is that of **epistasis analysis** in a switch pathway ([7.4.20](/7.4.20)): *hunchback* is epistatic to *nanos*, so Nanos acts upstream of Hunchback, by repressing it. The posterior system is, in this sense, the inverse of the anterior one: the anterior system provides an activator, the posterior system removes a repressor.

Four maternal protein gradients thus exist at the syncytial blastoderm stage: Bicoid and Hunchback decreasing from the anterior, Nanos and Caudal decreasing from the posterior. Caudal activates posterior **gap genes** and later the hindgut genes.

![The maternal anterior-posterior system. A: in the egg, bicoid mRNA is localized at the anterior pole and nanos mRNA at the posterior pole, while maternal hunchback and caudal mRNAs are uniform. B: after fertilization Bicoid protein forms an anterior gradient, activates zygotic hunchback transcription and represses caudal translation; Nanos protein, with Pumilio and Brat, represses hunchback translation in the posterior. The result is two opposing pairs of gradients: Bicoid and Hunchback anteriorly, Nanos and Caudal posteriorly. C: schematic profiles along the egg](./plots/maternal-gradients.py)

The anterior system itself is evolutionarily recent. *bicoid* arose by duplication of a *Hox3*/*zen*-like gene in higher flies (Cyclorrhapha); in other insects, such as the beetle *Tribolium* and the wasp *Nasonia*, anterior patterning relies on maternal Orthodenticle and Hunchback, and in many short-germ insects on a posterior signal and a segmentation clock instead ([7.5.39](/7.5.39)). Bicoid is therefore not a model of how all insects specify their head, but a striking example of how a single new gene, placed under the control of an existing mRNA-localization system, could take over the role of a whole set of older inputs.

### 14.3.3. The Terminal System

The unsegmented extremities, the acron and the telson, are specified by a separate system that uses local activation of a uniformly distributed receptor. Torso, a receptor tyrosine kinase, is translated from maternal mRNA and present throughout the plasma membrane of the early embryo. Its activating ligand is generated only at the poles: Torso-like, a protein with a membrane-attack-complex/perforin domain, is made by the follicle cells at both ends of the egg chamber and deposited in the vitelline membrane, and it is required for the local processing of Trunk, which is secreted uniformly into the perivitelline space, into an active ligand. Activated Torso signals through the **MAP kinase cascade** and relieves repression by the transcriptional repressor Capicua at the poles, so that the gap genes *tailless* and *huckebein* are expressed in the terminal regions. The same receptor, in the larva, is the receptor for the prothoracicotropic hormone that times metamorphosis ([7.5.33](/7.5.33)).

The design explains two classes of mutant. Loss of *torso*, *torso-like* or *trunk* deletes both termini. Gain-of-function *torso* **alleles**, which make the receptor active without ligand, expand the terminal fates at the expense of the central segments. Because Torso-like is made by somatic follicle cells, mosaic females with mutant follicle cells only at one pole produce embryos lacking only the corresponding terminus: the spatial information resides in the follicle cells, as it does for the dorsal–ventral axis.

## 14.4. Principles of the Maternal Systems

The three anterior–posterior systems and the dorsal–ventral system use three different mechanisms to make a spatial signal.

| Mechanism | System | Localized element | Uniform elements |
|---|---|---|---|
| A localized mRNA makes a diffusing protein | anterior (Bicoid), posterior (Nanos) | *bicoid* mRNA, pole plasm with *nanos* mRNA | maternal *hunchback* and *caudal* mRNAs |
| Local activation of a uniform receptor by an extracellular cue | terminal (Torso), dorsal–ventral (Toll) | Torso-like at the poles; Pipe ventrally | Torso; Toll; Trunk; the protease cascade |
| Regulated nuclear entry of a uniform transcription factor | dorsal–ventral (Dorsal) | Toll activity | Dorsal and Cactus |

In every case the information originates in the arrangement of the egg chamber: the position of the oocyte nucleus, the posterior follicle cells and the terminal follicle cells. The embryo inherits the geometry of its mother's ovary, which is why these genes are **maternal-effect genes**.

## 14.5. The Dorsal–Ventral Axis

### 14.5.1. From Follicle Cells to the Toll Receptor

The second Gurken signal makes the follicle cells over the oocyte nucleus dorsal: EGF receptor signalling in them represses the gene *pipe* (through the transcription factor Mirror). Pipe is a sulfotransferase in the Golgi apparatus, so it is active only in the ventral follicle cells, where it sulfates proteins that are incorporated into the ventral vitelline membrane. After fertilization, these sulfated proteins localize the activation of a cascade of **serine proteases** in the perivitelline space between the vitelline membrane and the embryo: Nudel, Gastrulation defective, Snake and Easter, each activating the next, all present uniformly. Easter cleaves the uniformly distributed Spätzle protein, and cleaved Spätzle is the ligand of Toll, a transmembrane receptor present all around the embryo. A **serine protease** inhibitor (serpin 27A) in the perivitelline fluid limits the cascade to where it is triggered.

Inside the embryo, Toll bound to Spätzle recruits the adaptor MyD88, the adaptor Tube and the kinase Pelle. Their activity leads to phosphorylation of Cactus, an inhibitor that binds Dorsal and holds it in the cytoplasm; phosphorylated Cactus is ubiquitinated and degraded by the **proteasome**, and the released Dorsal enters the nucleus. Since Toll is activated most strongly at the ventral midline and less laterally, Dorsal enters the nuclei in a ventral-to-dorsal gradient, while the total amount of Dorsal is uniform.

The genetic phenotypes follow: loss of any component from *pipe* to *Toll* or *dorsal* gives dorsalized embryos, with Dorsal cytoplasmic everywhere; loss of *cactus* gives ventralized embryos with Dorsal nuclear everywhere; a gain-of-function *Toll* allele, active without ligand, ventralizes. Two experiments located the signal outside the embryo. Perivitelline fluid from wild-type embryos, injected into the perivitelline space of embryos from *pipe* or *nudel* mutant mothers, restores ventral structures, and it does so around the injection site, which then becomes ventral, whatever the original orientation (Stein and colleagues, 1991). The polarity is in the extracellular space, imposed by the eggshell.

### 14.5.2. Toll and Innate Immunity

Toll, Pelle, Cactus and Dorsal are homologous to the components of a pathway of mammalian immunity: the Toll-like receptors and the interleukin-1 receptor, the kinase IRAK, the inhibitor **IκB** and the transcription factor **NF-κB**. Mutant flies that lack Toll signalling as adults are killed by fungal infection, because Toll activates the genes of antifungal peptides in the fat body (Lemaitre and colleagues, 1996). The finding led to the discovery of Toll-like receptors as the sensors of microbial molecules in mammals ([7.15](/7.15)). The developmental and the immune functions use the same core cascade with different inputs: the protease cascade that cleaves Spätzle in the egg is a developmental version of the cascades that cleave it in the haemolymph in response to microbial cell walls.

![From the follicle cells to the nucleus: the dorsal-ventral cascade of the *Drosophila* egg (left) and the homologous pathway of mammalian innate immunity (right, grey). Gurken-EGFR signalling represses pipe in the dorsal follicle cells, so that Pipe sulfates vitelline-membrane proteins only ventrally; the sulfated proteins localize the activation of a protease cascade (Nudel, Gastrulation defective, Snake, Easter) in the perivitelline space, which cleaves Spätzle; cleaved Spätzle activates Toll; Toll recruits MyD88, Tube and the kinase Pelle; Cactus is phosphorylated and degraded, and Dorsal enters the ventral nuclei, where it activates twist and snail and represses dpp and zen. Dotted lines join homologous steps: Toll and the Toll-like receptors, Cactus and IκB, Dorsal and NF-κB](./plots/toll-pathway.py)

### 14.5.3. Reading the Nuclear Dorsal Gradient

Quantitative imaging of nuclear Dorsal in fixed and living embryos showed that its profile across the ventral half is well described by a Gaussian with a small constant background, whose width is about 15 % of the distance from the ventral to the dorsal midline and changes little between embryos (Kanodia and colleagues, 2009; Liberman and colleagues, 2009). Dorsal activates genes ventrally and represses others dorsally, according to the affinity and arrangement of its **binding sites** in their **enhancers** and to the partners present:

- *twist* and *snail*, which need high Dorsal, are expressed in a band about 18 cells wide along the ventral midline, the prospective **mesoderm**; Twist protein then cooperates with Dorsal in activating *snail*, a feed-forward arrangement that sharpens the border;
- *rhomboid* and *vnd* (ventral nervous system defective) in the ventral neuroectoderm, which needs intermediate Dorsal, and is kept out of the **mesoderm** because Snail represses these genes;
- *sog* (short gastrulation) in a broad lateral band, activated by low Dorsal;
- *decapentaplegic* (*dpp*), *zerknüllt* (*zen*) and *tolloid* are repressed by Dorsal, which here recruits **corepressors**, so they are expressed only in the dorsal 40 % of the embryo.

**Formula 14.5.1 (Threshold positions on a Gaussian gradient)** Let nuclear Dorsal, as a function of the fraction $s$ of the distance from the ventral ($s = 0$) to the dorsal ($s = 1$) midline, be

$$
c(s) = A\,\mathrm{e}^{-s^2/(2\sigma^2)} + B .
\tag{14.3}
$$

A target activated above the threshold $T$ (with $B < T < A + B$) is expressed for $s < s_T$, where

$$
s_T = \sigma\sqrt{2\ln\frac{A}{T - B}} .
\tag{14.4}
$$

Unlike for an exponential gradient, the boundaries crowd together far from the midline, where the profile flattens onto the background: $\mathrm{d}s_T/\mathrm{d}\ln T = -\sigma^2 T/[s_T(T - B)]$, so a given relative change of threshold moves a lateral boundary more than a ventral one. This is one reason why the lateral and dorsal genes do not rely on Dorsal alone (14.6).

**Example 14.5.1** With $\sigma = 0.15$, $A = 1$ and $B = 0.05$, a threshold of $T = 0.38$ for *snail* gives $s_T = 0.15\sqrt{2\ln(1/0.33)} = 0.22$. The ventral half of the cycle-14 embryo has about 40 nuclei from midline to midline on each side, so the mesoderm is $0.22 \times 40 \approx 9$ nuclei on each side, about 18 in all, as observed. A threshold of $0.054$ for *sog* gives $s_T = 0.15\sqrt{2\ln(1/0.004)} = 0.50$, but a 10 % change in that threshold moves the boundary by about $0.06$, two to three nuclei: the *sog* border cannot be precise on Dorsal alone.

![The nuclear Dorsal gradient and its readout. A: transverse section of the cellular blastoderm (dorsal up), nuclei coloured by nuclear Dorsal (darkest at the ventral midline). Bands outside the embryo show the expression domains of its targets on both sides: twist and snail in the mesoderm (red), vnd and rhomboid in the ventral neuroectoderm (orange), sog in the lateral neuroectoderm (purple), and dpp, zen and tolloid in the dorsal ectoderm (yellow), where Dorsal is too low to repress them. B: the gradient as a Gaussian with background (Eq. (14.3), σ = 0.15, B = 0.05) on a logarithmic scale, with the activation thresholds of three targets; each boundary lies where the profile crosses the threshold (Eq. (14.4)). Lateral thresholds lie where the profile is flat, so the lateral boundaries are much more sensitive to noise than the ventral one](./plots/dorsal-gradient.py)

## 14.6. The Dpp Activity Gradient and the Shuttle

The dorsal 40 % of the embryo, where Dorsal is too low to repress *dpp*, is subdivided by a second gradient. Dpp is a BMP ([7.3.19](/7.3.19)); its activity, read as phosphorylated Mad (the BMP-activated **Smad**) in the nuclei, is not uniform over the domain where *dpp* is transcribed but forms a narrow peak at the dorsal midline, where the highest level specifies the amnioserosa, an extra-embryonic membrane, and lower levels dorsal epidermis. Dpp is unusually dose-sensitive: embryos with only one functional copy of *dpp* lose dorsal fates and die, and extra copies or injected *dpp* mRNA expand the amnioserosa at the expense of lateral fates, so that a uniformly high dose converts the whole **ectoderm** to amnioserosa.

The peak is made by transport rather than by localized synthesis. Sog, a large secreted protein made in the lateral neuroectoderm, binds Dpp (together with Twisted gastrulation) and prevents it from binding its receptor. The Sog–Dpp complex diffuses, while Dpp alone diffuses poorly because it binds the cell surface. Tolloid, a metalloprotease made in the dorsal domain, cleaves Sog only when it is bound to Dpp, releasing Dpp. Sog enters the dorsal domain from both sides and is destroyed there, so its concentration falls towards the dorsal midline; Dpp that is released far from the midline is soon bound again by Sog and carried further, whereas Dpp released near the midline, where Sog is scarce, stays. The net effect is a flux of Dpp towards the midline, up its own concentration gradient (Holley and colleagues, 1996; Eldar and colleagues, 2002; Shimmi and colleagues, 2005).

**Formula 14.6.1 (The shuttle model)** Let $M$, $S$ and $C$ be the concentrations of free Dpp, free Sog and the Dpp–Sog complex on the coordinate $s$ of Formula 14.5.1. With Dpp made at rate $\eta_M$ in the dorsal domain $\Omega_{\mathrm{d}}$ and Sog at rate $\eta_S$ in the lateral domain $\Omega_{\mathrm{l}}$,

$$
\begin{aligned}
M_t &= D_M M_{ss} - k_{\mathrm{on}} M S + k_{\mathrm{off}} C + \lambda_{\mathrm{t}} \boldsymbol{1}_{\Omega_{\mathrm{d}}} C - k_M M + \eta_M \boldsymbol{1}_{\Omega_{\mathrm{d}}},\\
S_t &= D_S S_{ss} - k_{\mathrm{on}} M S + k_{\mathrm{off}} C - k_S S + \eta_S \boldsymbol{1}_{\Omega_{\mathrm{l}}},\\
C_t &= D_C C_{ss} + k_{\mathrm{on}} M S - k_{\mathrm{off}} C - \lambda_{\mathrm{t}} \boldsymbol{1}_{\Omega_{\mathrm{d}}} C,
\end{aligned}
\tag{14.5}
$$

with no-flux conditions at both midlines. Here $\lambda_{\mathrm{t}}$ is the rate of cleavage of complexed Sog by Tolloid and $k_M$ the rate at which free Dpp is captured by its receptors. The shuttle requires $D_M \ll D_C$ (only the complex is mobile), cleavage confined to complexes, and Sog in excess over Dpp.

The simulation in the figure shows the two consequences. Without Sog, Dpp simply fills the region where it is made. With Sog, it is concentrated at the midline into a peak several times higher than the production would give locally. The same model also explains the dose sensitivity: halving Dpp production lets Sog bind almost all of it, and the peak disappears; doubling it saturates Sog, and the peak widens. In the embryo, positive feedback in the cells that receive the highest signal sharpens the peak further during cycle 14.

![The shuttle that concentrates Dpp at the dorsal midline (Formula 14.6.1), solved on the half-circumference from the ventral (0) to the dorsal (1) midline in dimensionless units. Dpp is made in the dorsal 40 % (yellow band) and hardly diffuses alone; Sog is made in excess in the lateral neuroectoderm (purple band) and diffuses; the Dpp–Sog complex diffuses and is cleaved by Tolloid in the dorsal domain, releasing Dpp. A: free Dpp with Sog (solid) and without it (dashed); without Sog, Dpp fills its expression domain uniformly, with Sog it is carried to and concentrated at the midline. B: half, normal and double Dpp production; with half, Sog binds nearly all Dpp and the peak above the amnioserosa threshold (dotted) is lost, as in dpp heterozygotes, while double production widens the peak](./plots/dpp-shuttle.py)

**Example 14.6.1 (An inverted axis)** Sog is homologous to Chordin, an antagonist of BMP secreted by the vertebrate organizer ([7.5.16](/7.5.16)), and Dpp to BMP2 and BMP4. In flies, BMP signalling is dorsal and the antagonist and the nerve cord ventral; in vertebrates, BMP signalling is ventral and the antagonist and the nerve cord dorsal. The molecules are interchangeable: *Xenopus* Chordin mRNA injected into *Drosophila* embryos promotes ventral (neurogenic) fates, and *sog* mRNA injected into *Xenopus* embryos promotes dorsal fates (Holley and colleagues, 1995). The simplest explanation is that the dorsal–ventral axis was inverted in the lineage leading to vertebrates, a hypothesis that Geoffroy Saint-Hilaire had proposed in 1822 on anatomical grounds; the shared BMP–Chordin system is now among its strongest supports ([7.5.39](/7.5.39)).

## 14.7. A Cartesian Coordinate System

At the end of the maternal phase every nucleus of the syncytial blastoderm has two independent coordinates: an anterior–posterior one, given by the levels of Bicoid, Hunchback, Caudal and the terminal signal, and a dorsal–ventral one, given by nuclear Dorsal and, dorsally, by the Dpp activity gradient. The zygotic genes read the two sets of coordinates separately at first: the gap and **pair-rule genes** are expressed in bands around the circumference, and the Dorsal targets in bands along the length. Organ primordia then arise where particular values of both coordinates coincide, for example the salivary glands where the *Hox* gene *Sex combs reduced* meets low Dpp ventrally, or the leg primordia where the Wingless stripes cross the boundary of Dpp signalling ([7.5.15](/7.5.15), [7.5.33](/7.5.33)). The embryo is, in effect, a sheet of nuclei with a grid drawn on it by the mother.

## Summary

| Topic | Key points |
|---|---|
| Embryo (14.1) | syncytium of 13 nuclear cycles, nuclei at the cortex at cycle 10, pole cells at 9–10, cellularization in cycle 14 (about 6000 cells); four maternal systems: anterior, posterior, terminal, dorsal–ventral |
| Oogenesis (14.2) | germline stem cell → 16-cell cyst with ring canals → oocyte + 15 polyploid nurse cells, follicle epithelium; Gurken–EGFR twice: posterior follicle cells (then microtubule reorganization) and dorsal follicle cells |
| mRNA localization (14.2.3, Definition 14.2.1, Example 14.2.1) | weakly biased microtubules; *bicoid* by dynein to the anterior, *oskar* by **kinesin** to the posterior, *nanos* by diffusion and trapping; Oskar assembles **pole plasm** and is sufficient for abdomen and germ cells |
| Anterior (14.3.1, Formula 14.3.1, Example 14.3.1) | Bicoid: homeodomain TF and translational repressor of *caudal*; "find it, lose it, move it"; $\lambda \approx 100\,\mathrm{\mu m}$; accumulation time $\tau(x) = (1 + x/\lambda)/2k$, the posterior is not at steady state; precision about 2 % of egg length |
| Posterior (14.3.2, Example 14.3.2) | Nanos + Pumilio + Brat repress maternal *hunchback*; *nanos hunchback* double mutants have a normal abdomen; four gradients: Bcd, Hb anterior; Nos, Cad posterior |
| Terminal (14.3.3) | uniform Torso activated at the poles by Trunk processed with Torso-like from terminal follicle cells; MAPK relieves Capicua → *tailless*, *huckebein* |
| Dorsal–ventral (14.5, Formula 14.5.1, Example 14.5.1) | Gurken → no Pipe dorsally; ventral sulfation → protease cascade → Spätzle → Toll → Pelle → Cactus degraded → nuclear Dorsal gradient (Gaussian, $\sigma \approx 0.15$); homologous to TLR → IRAK → IκB → NF-κB; thresholds: *snail* (18 cells), *vnd*, *sog*; *dpp*, *zen* repressed |
| Dpp (14.6, Formula 14.6.1, Example 14.6.1) | Sog–Dpp complexes diffuse, Tolloid cleaves them dorsally: net transport of Dpp to the dorsal midline; dose sensitivity; Sog/Chordin and Dpp/BMP4 across the inverted axis |

## Questions

1. A female fly is homozygous for a null *bicoid* allele. What is the phenotype of her embryos, and how could you rescue them? Predict the result of injecting *bicoid* mRNA into the posterior pole of such an embryo.

   **Answer** Her embryos lack head and thorax, and the anterior is replaced by posterior structures (a telson), whatever their own genotype. Injecting *bicoid* mRNA at the anterior pole restores a normal pattern. Injected at the posterior pole of a *bicoid* embryo, the mRNA makes a gradient from that pole, so head structures form posteriorly; the embryo then has its head at the posterior pole and a telson at the anterior, a reversed pattern, because the polarity follows the source of Bicoid.

2. In Example 14.3.2, why is the double mutant (no maternal *hunchback* and no *nanos*) the decisive experiment, and what result would have shown that Nanos is an instructive abdominal signal?

   **Answer** The single *nanos* mutant cannot distinguish whether the abdomen is missing because an activator (Nanos itself) is absent or because a repressor (maternal Hunchback) is present. Removing Hunchback in the absence of Nanos separates the two: if the abdomen forms, Nanos is not needed for abdominal fate once Hunchback is gone, so its role is only to remove Hunchback. If Nanos were itself instructive, the double mutant would still lack an abdomen, like the *nanos* single mutant.

3. The decay length of Bicoid is about 100 µm. (a) By how much does the boundary at which Bicoid falls to a fixed threshold move when the mother has four copies of *bicoid* instead of two? (b) With 10 % noise in the nuclear Bicoid concentration, what is the positional error of that boundary?

   **Answer** (a) For $c = c_0\mathrm{e}^{-x/\lambda}$ the boundary is at $x_T = \lambda\ln(c_0/T)$; doubling $c_0$ moves it posteriorly by $\lambda\ln 2 \approx 69\,\mathrm{\mu m}$, about 14 % of a 500 µm egg. (b) $\delta x = \lambda\,\delta c/c = 100 \times 0.1 = 10\,\mathrm{\mu m}$, about 2 % of the egg length, roughly one nuclear spacing at cycle 14.

4. Using Eq. (14.2) with $1/k = 50\,\mathrm{min}$ and $\lambda = 110\,\mathrm{\mu m}$, compute the accumulation time at 25 %, 50 % and 75 % of a 500 µm egg. What do the numbers imply for nuclei in the posterior half that read Bicoid at cycle 14?

   **Answer** $\tau = 25\,\mathrm{min} \times (1 + x/\lambda)$: at 125 µm, $25 \times 2.14 = 53\,\mathrm{min}$; at 250 µm, $25 \times 3.27 = 82\,\mathrm{min}$; at 375 µm, $25 \times 4.41 = 110\,\mathrm{min}$. The time to reach 90 % of steady state is roughly twice as long, so posterior nuclei read a concentration that is still rising at cellularization (about 150 min). Their response depends on when they read it, which is why posterior boundaries rely on other inputs (Nanos, Caudal, cross-regulation of the gap genes) and why the Bicoid concentration there is not a reliable coordinate by itself.

5. Design an experiment to decide whether the dorsal–ventral information of the egg lies in the germ line or in the follicle cells, and state the results expected for *gurken*, *torpedo* and *pipe*.

   **Answer** Make mosaic females in which either the germ line or the follicle cells are homozygous mutant (germ-line clones by **mitotic recombination** or pole-cell transplantation, follicle-cell clones by FLP/FRT), and examine their eggs and embryos. *gurken* is required in the germ line: germ-line clones give ventralized eggs and embryos, follicle-cell clones are normal. *torpedo* and *pipe* are required in the follicle cells: clones of follicle cells mutant for *torpedo* are ventral in character even on the dorsal side (they express *pipe*), and a ventral patch of *pipe* mutant follicle cells produces a local loss of ventral fate in the embryo below it. The information therefore flows from oocyte (Gurken) to follicle cells (Torpedo, Pipe) and back to the embryo (Toll).

6. Why are *cactus* mutant embryos ventralized, whereas *dorsal* and *Toll* mutant embryos are dorsalized? Predict the phenotype of embryos from mothers mutant for both *cactus* and *Toll*.

   **Answer** Cactus holds Dorsal in the cytoplasm; Toll signalling degrades Cactus. Without Cactus, Dorsal enters every nucleus, so all cells adopt ventral fates; without Toll or without Dorsal, no nucleus has Dorsal, so all are dorsal. In the double mutant, Toll has no role left, because its only function is to remove Cactus, which is already absent: the embryos are ventralized like *cactus* single mutants, so *cactus* is epistatic to *Toll* and acts downstream of it.

7. With the parameters of Example 14.5.1, how many nuclei wide is the domain in which Dorsal is above $T = 0.12$ (the *vnd* threshold)? By how many nuclei does this boundary move if $T$ changes by 10 %?

   **Answer** $s_T = 0.15\sqrt{2\ln(1/0.07)} = 0.15 \times 2.31 = 0.35$, about 14 nuclei on each side. From $\mathrm{d}s_T/\mathrm{d}\ln T = -\sigma^2 T/[s_T(T - B)] = -0.0225 \times 0.12/(0.35 \times 0.07) = -0.11$, a 10 % change of $T$ moves the boundary by $0.011$, about half a nucleus, much less than the two to three nuclei for *sog*: the ventral half of the gradient, where it is steep relative to its background, can position boundaries precisely, the lateral part cannot.

8. In the shuttle model, what would happen to the Dpp peak (a) in a *tolloid* null mutant, (b) in a *sog* null mutant, and (c) if Dpp alone diffused as fast as the complex? Explain each from Eq. (14.5).

   **Answer** (a) Without Tolloid ($\lambda_{\mathrm{t}} = 0$) Dpp bound by Sog is never released: little free Dpp remains, the peak is lost and the amnioserosa does not form, the observed *tolloid* phenotype. (b) Without Sog there is no carrier: Dpp stays roughly where it is made and the profile is a broad plateau over the dorsal 40 %, lower at the midline than in **wild type**; *sog* mutants lose the amnioserosa peak and the neuroectoderm is reduced. (c) If $D_M = D_C$, released Dpp would diffuse back as fast as it is brought, the net flux towards the midline would vanish and the concentration would be set by local synthesis and decay, again a plateau. Transport up a gradient requires that the carrier, not the cargo, be mobile.

9. Explain in terms of mechanism why the positions of the gap-gene boundaries depend on the dose of *bicoid*, whereas the position of the dorsal midline does not depend on the dose of *pipe* (heterozygous mothers are normal).

   **Answer** Bicoid is an instructive concentration gradient whose absolute level sets the threshold positions, so changing the dose shifts every boundary that reads it directly. The dorsal–ventral pattern is set by the geometry of the follicle cells: where *pipe* is expressed (all ventral follicle cells) is decided by Gurken, and the amount of Pipe per cell mainly affects the amount of sulfation, which is downstream of a protease cascade that amplifies and saturates. Halving Pipe therefore changes the magnitude of the ventral signal little, and the midline remains where the dorsal follicle cells put it. The two systems differ in whether position is encoded in a level or in a spatial domain.

10. (Open question) Percus and Childress treat the gradients of the early insect embryo as solutions of one-dimensional reaction–diffusion equations along the axis. List the biological features of the real embryo that such a model omits, and say for each whether it would change the predicted steady profile, the time course or the precision.

    **Answer** Points to include: (i) the geometry is a cortical shell around a yolky core, so diffusion is effectively two-dimensional on a curved surface and the axial projection averages over very different concentrations (changes the profile near the poles and the effective decay length); (ii) the source is the localized mRNA, itself graded and degraded at cycle 14 (time course and late profile); (iii) nuclei multiply at every cycle and import the protein, and nuclear envelopes break down at mitosis (time course, nuclear versus cytoplasmic concentrations); (iv) cytoplasmic flows during cycles 1–9 (time course); (v) molecular numbers are small, a few hundred to thousands of molecules per nucleus, so noise limits precision; (vi) readout by enhancers with cooperative binding and by other gradients (precision and robustness). A one-dimensional deterministic model captures the order of magnitude of $\lambda$ and the dependence on dose, not the precision or the dynamics.
