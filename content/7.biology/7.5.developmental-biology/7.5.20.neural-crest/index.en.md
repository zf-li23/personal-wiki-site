---
title: The Neural Crest
description: "The migratory, multipotent cells that leave the borders of the neural plate. Axial regions and derivatives; induction at the neural plate border and the neural crest gene regulatory network; multipotency and fate restriction; delamination by epithelial–mesenchymal transition; mechanisms of migration (contact inhibition of locomotion, co-attraction, chase-and-run) with a particle model; trunk pathways through the anterior sclerotome and their Eph/ephrin and semaphorin guidance; cranial crest, pharyngeal arches, Hox codes and the shape of the face; cardiac and enteric crest, a reaction-diffusion model of gut colonization and Hirschsprung disease; neurocristopathies."
---

When the neural folds fuse ([7.5.18](/7.5.18)), the cells at their crests do not stay in the tube. They lose their epithelial character, leave the dorsal **neural tube** and migrate, often over long distances, through the embryo, where they give rise to an astonishing variety of cell types: the neurons and glia of the peripheral nervous system, the pigment cells of the skin, the chromaffin cells of the adrenal medulla, and in the head most of the bones and cartilage of the face and parts of the heart. The neural crest is a vertebrate innovation; much of what makes the vertebrate head, jaws and sense organs is built from it. It also brings together several themes of the course: induction at a boundary by graded signals ([7.5.11](/7.5.11)), a gene regulatory network that confers a multipotent state, the **epithelial–mesenchymal transition** ([7.3.23](/7.3.23)), collective **cell migration** and guidance by contact repulsion, and a clinical group of diseases, the neurocristopathies. The axon guidance molecules that steer crest cells reappear in [7.5.21](/7.5.21), and the ectodermal placodes, which arise next to the crest at the anterior neural border, in [7.5.22](/7.5.22).

## 20.1. Origin and Properties

**Definition 20.1.1 (Neural Crest)** The **neural crest** is a transient population of cells that arises at the border between the neural plate and the epidermis, undergoes an epithelial–mesenchymal transition during or after neural tube closure, migrates along defined pathways and differentiates into many cell types, including neurons and glia of the peripheral nervous system, melanocytes, **endocrine** cells and, in the head, cartilage, bone and connective tissue.

The crest was described by His (1868) as the "Zwischenstrang", the cord between the neural tube and the epidermis; its derivatives were mapped above all with the quail-chick **chimera** technique of Le Douarin, in which a piece of quail neural tube grafted into a chick embryo is followed by the distinctive **heterochromatin** of quail nuclei (and now by species-specific antibodies), and since then by genetic **lineage tracing** in the mouse (*Wnt1-Cre*, *Sox10-Cre*) and live imaging in zebrafish. Because it is so prolific and gives rise to cell types otherwise typical of **mesoderm**, the crest has been called the fourth **germ layer**.

Crest cells from different levels of the body axis have different fates:

| Axial level | Main derivatives |
|---|---|
| Cranial (forebrain to r6) | craniofacial cartilage and bone, dermis and smooth muscle of the face and neck, odontoblasts of the teeth, sensory neurons of cranial ganglia (with placodes), parasympathetic ganglia, glia, melanocytes, corneal stroma and endothelium |
| Cardiac (otic vesicle to somite 3) | septum of the cardiac outflow tract (aorticopulmonary septum), smooth muscle of the great arteries, parasympathetic innervation of the heart |
| Vagal (somites 1-7) and sacral (caudal to somite 28) | enteric neurons and glia of the gut |
| Trunk | dorsal root ganglia (sensory neurons and satellite glia), sympathetic ganglia, chromaffin cells of the adrenal medulla, Schwann cells, melanocytes |

![The neural crest and its main derivatives. Centre: a transverse section of the trunk just after neural tube closure, with neural crest cells (green) leaving the dorsal neural tube. Around it, the cell types the crest forms at different axial levels: cranial crest gives most of the bone and cartilage of the face and the anterior skull and the odontoblasts of the teeth; cardiac crest the septum of the outflow tract; vagal and sacral crest the enteric nervous system; trunk crest the dorsal root ganglia, the sympathetic chain, the chromaffin cells of the adrenal medulla and Schwann cells; crest from all levels except the cardiac makes the melanocytes of the skin](./plots/crest-derivatives.py)

A major difference between head and trunk is the ability to form skeleton. Cranial crest makes cartilage and bone; trunk crest does not, even when grafted into the head of a host, although it can form cartilage in culture, so the difference is partly intrinsic. Crest cells of jawless vertebrates (lampreys) already have a full gene regulatory network; tunicates, the sister group of vertebrates, have cells at the neural plate border that express crest specifiers and migrate to form pigment cells (Abitua et al. 2012), which suggests that the crest evolved by adding migratory and skeletogenic programmes to a pre-existing border population.

## 20.2. Induction and the Gene Regulatory Network

### 20.2.1. Induction at the Neural Plate Border

The crest forms where neural plate meets epidermis, and the juxtaposition is sufficient: grafting neural plate into epidermis, in chick or axolotl embryos, produces crest cells at the new boundary, contributed by both tissues (Selleck and Bronner-Fraser 1995). The inducing signals combine:

- an intermediate level of BMP signalling, between the high level of the epidermis and the low level of the neural plate ([7.5.17](/7.5.17)): in *Xenopus*, injection of a BMP antagonist at increasing doses converts animal caps first to crest-like and then to neural fates, and zebrafish mutants with reduced BMP signalling have an expanded border;
- Wnt signals (Wnt6 from the epidermis in chick, Wnt8 from the paraxial mesoderm in frog), without which crest does not form even when BMP is intermediate;
- FGF from the paraxial mesoderm, and Notch signalling at the border.

The process begins earlier than once thought. In the chick the border specifier Pax7 marks prospective crest cells during **gastrulation**, and explants of this region form crest in culture without further contact with neural or mesodermal tissue (Basch et al. 2006), so specification overlaps with **neural induction**.

### 20.2.2. The Network

The signals act through a gene regulatory network that is among the best-defined in vertebrates (Meulemans and Bronner-Fraser; Simões-Costa and Bronner 2015). It has four tiers.

1. Neural plate border specifiers (*Pax3*, *Pax7*, *Msx1*, *Zic1*, *Tfap2a*, *Gbx2*, *Dlx5*) are induced by the border signals; their overlapping expression defines a zone competent to form crest and placodes.
2. Neural crest specifiers (*Snai2* (Slug), *Foxd3*, *Sox9*, *Sox10*, *Ets1*, *Twist1*, *Myc*) are activated by combinations of border specifiers; they define the premigratory crest, maintain its **multipotency** and cross-activate one another.
3. Effector genes of **delamination** and migration (**cadherins**, *RhoB*, metalloproteases, receptors for guidance cues) are their targets.
4. Differentiation genes (*Mitf* for melanocytes, *Phox2b* for autonomic neurons, *ErbB3* and *Mpz* for glia, *Runx2* and *Sox9* for skeleton) are activated as cells reach their destinations and meet local signals.

The architecture has been worked out by gain and loss of function at each tier and by analysis of enhancers. *Sox10* has a cranial-specific enhancer bound directly by Ets1 and Sox9; *Foxd3* is activated by Pax3 and Zic1; Snai2 directly represses the E-cadherin gene. Two features are general. Positive feedback among the specifiers creates a stable state, as in the cross-repressive circuits of [7.5.18](/7.5.18), that persists when the inducing signals are gone. And the same factors are reused downstream: Sox10, needed to maintain multipotent crest, later drives glial and melanocyte differentiation, so its loss removes several lineages at once (20.10).

![The gene regulatory network of the neural crest (SBGN activity flow, simplified after Simões-Costa and Bronner 2015). Signals at the neural plate border (intermediate BMP, Wnt, FGF, Notch) induce the neural plate border specifiers; these activate the neural crest specifiers, which in turn control the effector genes of delamination and migration (Snai2 represses E-cadherin; the cadherin switch to cadherin-6B and -7; RhoB; matrix metalloproteases) and maintain multipotency. Differentiation genes downstream of Sox10 and other specifiers then select particular fates. Arrows: activation; bars: repression](./plots/crest-grn.py)

## 20.3. Multipotency and Fate Restriction

Is a premigratory crest cell multipotent, or is the crest a mixture of committed precursors? Two kinds of experiment address it.

**Example 20.3.1 (Clonal Analysis of Crest Fate)** Bronner-Fraser and Fraser (1988) injected a fluorescent lineage tracer into single premigratory crest cells in the chick dorsal neural tube and examined the labelled clones two days later. Many clones contained several cell types, for example sensory neurons of the dorsal root ganglion, pigment cells and Schwann cells, and some even contributed to the neural tube. In the mouse, multicolour Cre reporters ("confetti") activated sparsely in premigratory crest with *Wnt1-Cre* showed that most premigratory and early migrating crest cells are multipotent, giving rise to neurons, glia and melanocytes in the same clone, and that restriction occurs as they migrate and arrive (Baggiolini et al. 2015). Conversely, some avian trunk crest cells appear restricted to one fate already before leaving the tube (Krispin et al. 2010).

The current view reconciles the two. Crest cells are multipotent but heterogeneous, and fate is decided progressively by intrinsic bias, the time of emigration (early-emigrating trunk cells take the ventral pathway and form neurons and glia, late-emigrating ones the dorsolateral pathway and melanocytes) and the signals met at the destination: BMPs from the dorsal aorta induce sympathetic neurons (*Phox2b*, *Ascl1*), neuregulin favours glia, Wnt and endothelin favour melanocytes. Back-transplantation experiments show that some crest cells moved to an earlier environment can change fate, but this plasticity declines with time. A striking modern finding is that some derivatives arise after a detour: Schwann cell precursors, which travel on growing nerves, also give rise to many melanocytes of the skin (Adameyko et al. 2009), to parasympathetic neurons (Dyachuk et al. 2014) and to most chromaffin cells of the adrenal medulla (Furlan et al. 2017), so the nerve itself serves as a **stem-cell niche** and a route of migration.

## 20.4. Delamination

Leaving the neural tube requires an **epithelial–mesenchymal transition** (EMT): the premigratory crest cells lose their apical-basal polarity and their junctions with neighbouring **neuroepithelial cells**, break through the **basal lamina** and become motile. The steps are controlled by the crest specifiers.

- Snai2 and other Snail and Zeb family factors repress the gene for E-cadherin; a **cadherin** switch from N-cadherin (and E-cadherin) to the type II cadherins cadherin-6B and cadherin-7 accompanies delamination in the chick; cadherin-6B is in turn cleaved by ADAM proteases, releasing fragments that promote motility.
- RhoB, induced by BMP, and other **Rho GTPase** regulators reorganize the actin **cytoskeleton**.
- Matrix metalloproteases degrade the basal lamina.
- In the trunk, delamination is coupled to the **cell cycle**: crest cells leave in synchrony in G1-S, and BMP signalling, antagonized dorsally by Noggin whose expression falls in a rostro-caudal wave as somites mature, triggers Wnt1 and the EMT (Burstyn-Cohen et al. 2004). Blocking the G1-S transition blocks delamination.

In amniote heads the crest delaminates as the folds close; in the trunk it delaminates after closure, from the dorsal neural tube.

## 20.5. Mechanisms of Migration

### 20.5.1. Contact Inhibition and Collective Migration

Crest cells do not wander individually through the embryo. They move as loose streams or sheets in which cells remain in contact, a mode called collective migration, and this behaviour depends on how they respond to one another.

**Definition 20.5.1 (Contact Inhibition of Locomotion)** **Contact inhibition of locomotion** (CIL) is the behaviour in which a migrating cell, on colliding with another cell, stops extending protrusions at the contact, repolarizes and moves away in another direction. It was described by Abercrombie in fibroblasts (1953) and is distinct from **contact inhibition** of proliferation.

In *Xenopus* and zebrafish crest, CIL is mediated by the non-canonical (PCP) Wnt pathway and N-cadherin: at the contact, Rho is activated and **Rac** inhibited, and the protrusions are lost; at the free edge of the cell, Rac is high and the cell protrudes (Carmona-Fontaine et al. 2008). Cells inside a group, surrounded by neighbours, cannot protrude in any direction, whereas cells at the edge of the group protrude outwards, so the group is driven to spread into free space. To prevent the group from simply dispersing, crest cells secrete complement factor C3a and express its receptor C3aR: this co-attraction keeps them together (Carmona-Fontaine et al. 2011). The combination produces directional migration of the whole group without any external gradient.

**Formula 20.5.1 (A Self-Propelled Particle Model of CIL)** Represent crest cells as particles at positions $\boldsymbol{x}_i$ with a polarity angle $\theta_i$, moving with velocity

$$
\dot{\boldsymbol{x}}_i = v_0\,\boldsymbol{e}(\theta_i) + \sum_{j} \boldsymbol{F}_{\mathrm{rep}}(\boldsymbol{x}_i - \boldsymbol{x}_j) - \sum_{j} \boldsymbol{F}_{\mathrm{att}}(\boldsymbol{x}_i - \boldsymbol{x}_j),
\qquad
\dot\theta_i = k\,\Delta\bigl(\phi_i, \theta_i\bigr)\,\boldsymbol{1}_{\{\text{contact}\}} + \sqrt{2D_{\mathrm{r}}}\,\xi_i(t),
\tag{20.1}
$$

where $\boldsymbol{e}(\theta) = (\cos\theta, \sin\theta)$, $\boldsymbol{F}_{\mathrm{rep}}$ is a short-range repulsion that prevents overlap, $\boldsymbol{F}_{\mathrm{att}}$ a weak attraction over a longer range (co-attraction), $\phi_i$ is the direction pointing away from the cells in contact with $i$, $\Delta(\phi, \theta)$ the signed angle from $\theta$ to $\phi$, $k$ the rate of repolarization and $\xi_i$ white noise with rotational diffusion coefficient $D_{\mathrm{r}}$.

Without CIL ($k = 0$) each particle performs a persistent random walk and the edge of a group spreads diffusively, as $\sqrt{t}$; with CIL the cells at the edge are biased outwards and the edge advances at a steady speed. Models of this kind (Woods et al. 2014; Szabó et al. 2016) reproduce the streaming of crest cells and show that confinement by repulsive territories (20.6) is needed to keep streams narrow.

![Contact inhibition of locomotion makes a group of cells invade free space (self-propelled particle model, Formula 20.5.1). Cells start packed in a band at the left of a channel (x < 0) and move at constant speed in the direction of their polarity, which turns at random and, with CIL, is repolarized away from every cell they touch; soft repulsion prevents overlap and a weak co-attraction keeps the group together. (A) Positions after the same time with CIL (green) and without it (grey, random polarity only). (B) The leading edge (95th percentile of x) moves steadily with CIL and only diffusively without: contact gives the cells at the edge a net outward polarity, so the group spreads as a collective](./plots/cil-simulation.py)

### 20.5.2. Chase and Run

In the *Xenopus* head, cranial crest cells and the adjacent placodal cells interact in a "chase-and-run" (Theveneau et al. 2013). The placodes secrete Sdf1 (Cxcl12), which attracts crest cells through Cxcr4 (**chemotaxis**); when a crest cell touches a placodal cell, CIL-like repulsion makes the placode cells move away. The crest thus chases the placodes, which run, and the two populations move together in the same direction. **Chemotaxis** by crest cells towards VEGF (in chick cranial streams) and the behaviour of leader and trailer cells in the stream (McLennan, Kulesa and colleagues) show that the same principles operate in amniotes, although the details vary.

A related, placode-derived example shows how a migrating group can make its own gradient. The posterior lateral line primordium of zebrafish, a cluster of about 100 cells, migrates along a uniform stripe of Sdf1 (Cxcl12a) from the head to the tail, depositing groups of cells that become the mechanosensory neuromasts. All its cells express the receptor Cxcr4, but the cells at its rear also express Cxcr7 (Ackr3), a decoy receptor that binds and internalizes Sdf1 without signalling. The rear therefore depletes the chemokine, so the front of the group sees more Sdf1 than the back, and the group moves forward along a gradient that it generates itself (Dona et al. 2013; Venkiteswaran et al. 2013). A self-generated gradient of this kind works over arbitrarily long distances, unlike a fixed gradient, whose useful range is limited as in [7.5.21](/7.5.21).

## 20.6. Trunk Neural Crest: Pathways and Derivatives

Trunk crest cells take two pathways.

- The ventral pathway, taken first, runs between the neural tube and the somite and then through the sclerotome. Cells that stop beside the neural tube form the dorsal root ganglia (sensory neurons and satellite glia); cells that continue ventrally form the sympathetic chain ganglia beside the dorsal aorta, the chromaffin cells of the adrenal medulla, and the Schwann cells of the ventral roots.
- The dorsolateral pathway, taken about a day later, runs between the epidermis and the dermomyotome; cells taking it become melanocytes and enter the skin and hair follicles.

The ventral pathway is segmented. Crest cells enter only the anterior (rostral) half of each sclerotome and avoid the posterior half, so the dorsal root ganglia form in register with the somites, and the motor axons that grow out of the neural tube follow the same anterior halves ([7.5.21](/7.5.21)).

**Example 20.6.1 (The Somite, Not the Neural Tube, Segments the Crest)** Is the segmental pattern of crest migration imposed by the neural tube or by the somites? Bronner-Fraser and Stern (1991) rotated a length of unsegmented paraxial mesoderm by 180° about its anterior-posterior axis, so that the future anterior halves of the somites now lay posteriorly. The crest cells, emerging from an unchanged neural tube, still entered the halves that were originally anterior: the property is intrinsic to the somite halves. The posterior halves express repellent molecules: ephrin-B ligands, which act on EphB receptors on crest cells (Krull et al. 1997; Wang and Anderson 1997), and semaphorin-3F, which acts through neuropilin-2; in mice lacking *Nrp2* or *Sema3f*, crest cells stream through both halves. Conversely, rotating the neural tube dorso-ventrally before emigration makes crest cells emerge ventrally and move into the somites dorsally, which shows that the neural tube and notochord also limit where crest cells go.

The switch to the dorsolateral pathway depends on changes in the crest cells themselves. Early crest cells are repelled from the dorsolateral space by ephrins and Slit; melanoblasts, which emerge later, express EphB receptors that now mediate attraction to the ephrin-B in the dermomyotome and the endothelin receptor Ednrb2, which draws them into the dorsolateral space (Harris et al. 2008). The same ligand can thus repel one cell type and attract another, depending on the receptor and its downstream signalling.

![Migration pathways of trunk neural crest cells. (A) Transverse section (dorsal up). Cells taking the ventral pathway (between the neural tube and the somite, then through the sclerotome) form the dorsal root ganglia beside the tube, the sympathetic ganglia beside the dorsal aorta and the chromaffin cells of the adrenal medulla; cells taking the later dorsolateral pathway (between the epidermis and the dermomyotome) become melanocytes. (B) Dorsal view of the same region (anterior up). Ventral-pathway cells enter only the anterior half of each sclerotome, because the posterior half expresses repellent ephrin-B and semaphorin-3F; the dorsal root ganglia and the motor axons are therefore segmented in register with the somites, and rotating a strip of somites by 180 degrees leaves the crest in the original anterior halves](./plots/trunk-migration.py)

## 20.7. Cranial Neural Crest and the Face

### 20.7.1. Streams, Arches and Hox Codes

Cranial crest cells migrate ventro-laterally in three main streams from the hindbrain into the pharyngeal arches, the bulges of mesenchyme, covered by **ectoderm** and lined by **endoderm**, that form on the sides of the head ([7.5.30](/7.5.30)). The streams originate in register with the rhombomeres of [7.5.18](/7.5.18): crest from the midbrain and r1-r2 fills the frontonasal region and the first arch, crest from r4 the second arch, crest from r6-r7 the third and fourth arches. Rhombomeres 3 and 5 produce few crest cells (in part by **apoptosis**, in part by deflecting them into neighbouring streams), and the crest-free territories beside r3 and r5, maintained by ErbB4 signalling and by repellent semaphorins and ephrins in the adjacent mesoderm, keep the streams apart.

The crest carries a **Hox gene** code matching its origin: first-arch crest is Hox-free, second-arch crest expresses *Hoxa2* and *Hoxb2*, more posterior arches add paralogue groups 3 and 4. The code specifies skeletal identity. In mice lacking *Hoxa2*, the skeletal elements of the second arch are replaced by a mirror-image duplication of first-arch elements (an extra malleus, incus and part of the jaw) (Gendron-Maguire et al. 1993; Rijli et al. 1993); conversely, misexpressing *Hoxa2* in first-arch crest transforms jaw elements towards second-arch identity. The Hox-free state of the first arch is required for the jaw, the defining structure of gnathostomes.

![Cranial neural crest streams and the Hox code of the pharyngeal arches (schematic lateral view, anterior left). Crest from the midbrain and rhombomeres r1-r2 fills the frontonasal region and the first pharyngeal arch, crest from r4 the second arch, crest from r6-r7 the third and fourth arches; r3 and r5 release few crest cells, so the streams stay separate. The crest carries a Hox code matching its origin: the first arch is Hox-free, the second expresses Hoxa2 (and Hoxb2), the third and fourth add group 3 and 4 genes. The code selects the skeletal derivatives: first arch, the jaws (Meckel's cartilage, maxilla, malleus and incus); second arch, the stapes and hyoid; third and fourth arches, the rest of the hyoid and the laryngeal cartilages](./plots/cranial-streams.py)

**Example 20.7.1 (Prepattern or Plasticity?)** Noden (1983) transplanted premigratory first-arch crest of the chick into the position of second-arch crest. The grafted cells migrated into the second arch but formed a duplicate first-arch skeleton (an extra jaw), suggesting that cranial crest is prepatterned before it migrates. Later experiments qualified this conclusion. When small groups of crest cells, rather than a whole region, were transplanted in the mouse or chick, they adopted the Hox code and fate of their new neighbours (Trainor and Krumlauf 2000), and Noden's graft had included the isthmus, an organizer ([7.5.18](/7.5.18)) that respecified the host tissue. The current view is that crest identity is plastic and maintained by interactions: by community signals among crest cells, by signals from the pharyngeal endoderm (which can induce specific cartilage elements when grafted, Couly et al. 2002) and from the ectoderm.

### 20.7.2. Coordinating Face and Brain

The face grows from five prominences around the stomodeum: the frontonasal prominence (crest from the forebrain and midbrain) and paired maxillary and mandibular prominences (first-arch crest). The form of the face is built by the crest but instructed partly by its neighbours. The forebrain and the facial ectoderm secrete Shh: an ectodermal signalling centre at the boundary between Shh and Fgf8 expression (the frontonasal ectodermal zone) directs the outgrowth of the upper beak, and grafting it ectopically induces an extra beak (Hu, Marcucio and Helms 2003). Because the face depends on Shh from the brain, defects of forebrain patterning produce facial defects, the spectrum of holoprosencephaly with cyclopia at its extreme ([7.5.22](/7.5.22)).

Species-specific shape, by contrast, is carried by the crest itself. Quail crest grafted into duck embryos produces quail-like beaks on duck heads and vice versa, and the grafted crest imposes its own timing of gene expression on the host tissue (Schneider and Helms 2003). Among Darwin's finches, beak depth and width correlate with the level and timing of *Bmp4* expression in the beak mesenchyme and beak length with **calmodulin** (Abzhanov et al. 2004, 2006); experimentally raising BMP4 in chick beak mesenchyme deepens the beak. Small quantitative changes in crest signalling thus produce the evolutionary variation of the face.

## 20.8. Cardiac Neural Crest

Crest from the level between the otic vesicle and the third somite (the posterior hindbrain) migrates through pharyngeal arches 3, 4 and 6 into the outflow tract of the heart, where it forms the aorticopulmonary septum that divides the single outflow vessel (truncus arteriosus) into the aorta and pulmonary trunk, as well as smooth muscle of the arch arteries ([7.5.28](/7.5.28)). Ablating this crest in chick embryos (Kirby et al. 1983) leaves a persistent truncus arteriosus and defects of the arch arteries; secondarily the myocardium is affected as well. In the mouse, mutations of *Pax3* (*Splotch*) remove cardiac crest and cause similar defects. In humans, **deletion** of 22q11.2 (DiGeorge and velocardiofacial syndrome) causes outflow tract defects (interrupted aortic arch, truncus arteriosus, tetralogy of Fallot), absence or hypoplasia of the thymus and parathyroids and facial anomalies, all structures that depend on crest in the posterior arches. The main gene responsible, *TBX1*, is expressed not in the crest but in the pharyngeal endoderm, mesoderm and ectoderm, which shows that crest defects can be caused by the environment the crest migrates through.

## 20.9. Enteric Neural Crest and Hirschsprung Disease

### 20.9.1. Colonization of the Gut

The enteric nervous system, which controls the motility and secretion of the gut and contains about 500 million neurons in humans, derives from vagal crest (somite levels 1-7), with a minor contribution from sacral crest to the distal hindgut. Vagal crest cells enter the foregut and migrate caudally inside the gut mesenchyme as a wave, colonizing the whole gut in a rostro-caudal sequence: in the mouse from E9.5 to E14.5, in humans from the fourth to the seventh week. Two signalling systems are essential. GDNF, secreted by the gut mesenchyme, acts through the **receptor tyrosine kinase** RET and its co-receptor GFRα1 on crest cells, promoting their proliferation, survival and migration; endothelin-3 from the mesenchyme acts through the receptor EDNRB, keeping cells proliferative and undifferentiated. Mice lacking *Ret*, *Gdnf* or *Gfra1* have no enteric neurons below the stomach; *Edn3* and *Ednrb* mutants lack them in the distal colon (and, because the same signal acts on melanoblasts, have pigmentation defects).

### 20.9.2. A Model of Colonization

A striking observation is that the colonizing wave advances mainly through proliferation at its front: the cells just behind the wavefront divide most, and the speed of the front depends on the proliferation rate as much as on cell motility. This is exactly the behaviour of the Fisher–KPP equation ([7.5.12](/7.5.12), [2.5.7](/2.5.7)), whose **traveling wave solution** advances at a speed determined by growth and diffusion together.

**Formula 20.9.1 (Colonization as an Invasion Wave)** Let $n(x, t)$ be the density of crest cells, scaled by its carrying capacity, along a gut of length $L(t)$, with cells entering at $x = 0$. If cells move randomly with diffusion coefficient $D$, proliferate logistically at rate $r$, and the gut grows uniformly at rate $\dot L$,

$$
\frac{\partial n}{\partial t} + \frac{\dot L}{L}\,\frac{\partial (x n)}{\partial x} = D\,\frac{\partial^{2} n}{\partial x^{2}} + r\,n(1 - n),
\tag{20.2}
$$

the second term on the left describing the advection and dilution of cells by uniform tissue growth. On a fixed domain, the reaction-diffusion equation ($\dot L = 0$) has travelling waves of every speed $c \ge c^{*} = 2\sqrt{rD}$, and a front started from a step propagates at the minimal speed $c^{*}$ ([2.5.7](/2.5.7)). The whole gut is colonized if the front, which moves at about $c^{*}$ plus the growth velocity $x_{\mathrm{f}}\dot L/L$ of the tissue at its position, reaches the distal end before the gut stops growing; if proliferation or motility is reduced, the front can fall behind the growing end.

Landman, Newgreen, Simpson and colleagues (2003-2007) combined such models with explant experiments in the chick and mouse. Two predictions were confirmed: cell proliferation at the front is the main driving force, and reducing proliferation (or the number of cells entering the gut) slows the wave so much that the distal gut is never colonized, even though each cell remains motile. In the model, halving $r$ reduces the front speed by $1/\sqrt{2}$, about 30%, but the effect on colonization is larger because the gut keeps growing. Individual cells, tracked by live imaging, move in chains with frequent changes of direction (Young et al. 2014), consistent with a diffusive description at the scale of the population.

![Colonization of the growing gut by enteric neural crest cells as a reaction-diffusion invasion (Formula 20.9.1). Cells enter at the oral end (x = 0), diffuse (D = 0.004 mm²/h) and proliferate logistically, while the gut grows uniformly from 1 mm at 0.025 mm/h, which also stretches the colonized region and dilutes the cells. (A) Position of the invasion front (density half the carrying capacity) and gut length over time, for three proliferation rates (front speeds 2 sqrt(rD) of 0.040, 0.025 and 0.020 mm/h): with the highest rate the front catches up with the end of the gut, with lower rates it falls behind and the distal gut stays uncolonized (aganglionic, as in Hirschsprung disease) for longer or permanently. (B) Density profiles at 120 h; the dotted line marks the end of the gut](./plots/enteric-wave.py)

### 20.9.3. Hirschsprung Disease

Hirschsprung disease is congenital absence of enteric ganglia (aganglionosis) in a continuous segment of the distal bowel, always including the rectum and extending proximally for variable length (short-segment in about 80% of cases, long-segment, or total colonic aganglionosis). The aganglionic segment cannot relax, producing functional obstruction and dilation of the bowel above it (megacolon); affected newborns fail to pass meconium. It occurs in about 1 in 5000 births, with a male excess of about four to one. The distal location follows from the direction of colonization: whatever slows the wave leaves the end of the gut empty. *RET* coding mutations account for about half of familial and a fifth of sporadic cases, and a common variant in a *RET* enhancer bound by SOX10 greatly increases risk; *EDNRB*, *EDN3*, *SOX10* and *GDNF* mutations account for others. **Penetrance** is incomplete and depends on sex and other loci, as expected if the outcome depends on whether colonization finishes in time, a threshold on a continuous variable. Treatment is surgical removal of the aganglionic segment ("pull-through"); transplantation of enteric neural progenitors, including those derived from human pluripotent **stem cells**, is being developed.

## 20.10. Neurocristopathies

**Definition 20.10.1 (Neurocristopathy)** A **neurocristopathy** is a disease caused by abnormal specification, migration, differentiation or death of neural crest cells (Bolande 1974); because one population gives rise to many tissues, neurocristopathies typically combine defects of unrelated organs, such as pigmentation, hearing and gut innervation.

| Condition | Gene(s) | Crest defect | Main features |
|---|---|---|---|
| Hirschsprung disease | *RET*, *EDNRB*, *EDN3*, *SOX10* | enteric colonization | distal aganglionosis |
| Waardenburg syndrome (types 1-4) | *PAX3*, *MITF*, *SOX10*, *EDNRB/EDN3* | melanocyte development (and enteric in type 4) | white forelock, heterochromia of the iris, sensorineural deafness (loss of melanocytes of the inner ear), Hirschsprung in type 4 |
| Piebaldism | *KIT* | melanoblast migration and survival | congenital patches of unpigmented skin and hair |
| 22q11.2 deletion (DiGeorge) | *TBX1* (environment of the crest) | cardiac and pharyngeal crest | outflow tract defects, thymic and parathyroid hypoplasia, facial anomalies |
| Treacher Collins syndrome | *TCOF1*, *POLR1C/D* | p53-dependent apoptosis of crest cells (defective **ribosome biogenesis**) | hypoplasia of the cheekbones and jaw, ear malformations |
| CHARGE syndrome | *CHD7* | crest and placodes | coloboma, heart defects, choanal atresia, ear anomalies |
| Neuroblastoma | *PHOX2B*, *ALK*; *MYCN* amplification | sympathoadrenal precursors | childhood tumour of the adrenal and sympathetic chain |
| Familial dysautonomia | *ELP1* | sensory and autonomic neurons | reduced pain sensation, autonomic crises |

Treacher Collins syndrome is instructive: TCOF1 (treacle) is needed in all cells for ribosomal RNA synthesis, but crest progenitors, which proliferate rapidly, are particularly sensitive, and their deficit activates **p53** and apoptosis; in mouse models, inhibiting p53 prevents the craniofacial defects (Jones et al. 2008), showing that a defect in a general cellular process can produce a tissue-specific malformation.

## Summary

| Region | Pathway | Derivatives | Key genes and signals |
|---|---|---|---|
| Cranial | streams r2, r4, r6 into arches 1-4 | facial skeleton, cranial ganglia, teeth (odontoblasts) | Hox code (*Hoxa2*), Shh and FGF from brain and ectoderm, BMP4 |
| Cardiac | arches 3, 4, 6 to outflow tract | aorticopulmonary septum | *Pax3*; *TBX1* in the environment |
| Vagal/sacral | through the gut mesenchyme | enteric neurons and glia | RET/GDNF, EDNRB/EDN3 |
| Trunk, ventral | anterior sclerotome | DRG, sympathetic ganglia, adrenal medulla, Schwann cells | ephrin-B, Sema3F (posterior halves); BMP for sympathetic fate |
| Trunk, dorsolateral | under the epidermis | melanocytes | EphB, Ednrb2, KIT, MITF |

- The neural crest (Definition 20.1.1) arises at the neural plate border from intermediate BMP, Wnt and FGF signals; a four-tier network (border specifiers, crest specifiers, effectors, differentiation genes) makes the state stable.
- Premigratory crest cells are largely multipotent (Example 20.3.1); fates are restricted progressively, and Schwann cell precursors are a second source of melanocytes, parasympathetic neurons and chromaffin cells.
- Delamination is an EMT driven by Snail factors and the cadherin switch; migration is collective, driven by contact inhibition of locomotion (Definition 20.5.1, Formula 20.5.1), co-attraction and chase-and-run.
- The somite, not the neural tube, segments trunk crest migration (Example 20.6.1); cranial crest identity follows a Hox code that is plastic (Example 20.7.1); species-specific face shape is carried by the crest.
- Enteric colonization is an invasion wave driven by proliferation at the front (Formula 20.9.1, speed about $2\sqrt{rD}$); reduced RET or EDNRB signalling leaves the distal gut aganglionic (Hirschsprung disease).
- Neurocristopathies (Definition 20.10.1) combine defects of pigmentation, hearing, heart, face and gut.

## Questions

1. Design a quail-chick chimera experiment to show that the sympathetic ganglia of the trunk derive from the neural crest, and explain the controls needed to exclude contamination by other tissues.

   **Answer** Replace a short length of chick neural tube (with its dorsal crest, at the level of somites 18-24) by the equivalent quail neural tube before crest emigration, then identify quail cells by nuclear heterochromatin or the QCPN antibody in the host's sympathetic ganglia a few days later. Controls: graft quail neural tube from which the dorsal part has been removed (no quail cells should appear in the ganglia), check that the graft did not include somite or ectoderm (histology of the graft at the time of grafting), and confirm that quail cells in the ganglia express neuronal and sympathetic markers (tyrosine hydroxylase). Reciprocal chick-to-quail grafts confirm the result.

2. Explain why intermediate, rather than high or low, BMP signalling is needed to induce neural crest, and predict what happens to the crest in a zebrafish mutant with weakened BMP signalling (such as *swirl*/*bmp2b* **hypomorphs**) and in one with excess BMP signalling (*chordino*).

   **Answer** High BMP specifies epidermis, low BMP neural plate; the border, where BMP falls through intermediate values, expresses border specifiers that need a moderate level together with Wnt. In weak BMP mutants the zone of intermediate signalling moves ventrally and broadens, and the crest (and the neural plate) expands; in *chordino*, which lacks the BMP antagonist and has a ventralized embryo, the neural plate and the intermediate zone shrink, and the crest is reduced, displaced dorsally. The position of the crest is a threshold readout of the BMP gradient.

3. Using Formula 20.9.1 on a fixed domain, estimate the time needed for enteric crest to colonize a 20 mm gut if $r = 0.05\ \mathrm{h}^{-1}$ and $D = 0.01\ \mathrm{mm^2\,h^{-1}}$. By what factor does it lengthen if a *RET* hypomorph reduces proliferation by half?

   **Answer** $c^{*} = 2\sqrt{rD} = 2\sqrt{0.05\times0.01} = 0.0447\ \mathrm{mm\,h^{-1}}$, so $20/0.0447 \approx 450\ \mathrm{h}$, about 19 days (the real gut grows during colonization, and its early part is short, so the real time is less). Halving $r$ reduces $c^{*}$ by $\sqrt 2$: about 630 h, 40% longer. On a growing gut, where colonization must finish before a developmental deadline (when the gut mesenchyme stops supporting migration), this delay can leave the distal segment aganglionic, explaining the distal location and incomplete penetrance of Hirschsprung disease.

4. Crest cells inside a dense group cannot move, yet the group as a whole migrates. Explain this using contact inhibition of locomotion, and predict the behaviour of a group in which C3a signalling is blocked, and of a single isolated crest cell.

   **Answer** CIL suppresses protrusions at contacts, so internal cells, surrounded by neighbours, are effectively immobilized, while edge cells protrude into free space and move outwards; the group expands in the direction of free space. Co-attraction (C3a/C3aR) pulls cells back together, so without it edge cells separate and the group disperses into single cells with poor directionality. A single isolated crest cell has no contacts and performs a persistent random walk with no preferred direction: directional migration is an emergent property of the group.

5. In the somite rotation experiment of Example 20.6.1, what result would have indicated that the neural tube, not the somite, sets the segmental pattern? Which molecular experiment confirms the conclusion actually reached?

   **Answer** If the neural tube controlled segmentation, crest cells would have emerged at fixed positions opposite each segment of the tube and entered the somite halves now lying opposite those positions, i.e. the halves that are now anterior regardless of their origin. Instead they entered the originally anterior halves. Molecularly: ephrin-B (and Sema3F) are expressed in posterior sclerotome halves; blocking Eph-ephrin interactions with soluble ephrin-B or knocking out *Nrp2*/*Sema3f* makes crest cells enter both halves, while beads or cells presenting ephrin-B exclude crest cells from regions they normally enter.

6. Noden's graft of first-arch crest into the second arch produced an extra jaw. Propose an experiment to decide whether the crest was intrinsically prepatterned or respecified by an organizer included in the graft.

   **Answer** Graft first-arch crest dissected free of the isthmus (rhombomere 1 crest without the midbrain-hindbrain boundary) and compare with grafts that include the isthmus; also graft small groups or single labelled cells rather than large regions. If the cells are prepatterned, any first-arch crest makes first-arch structures in the second arch; if they are plastic, small groups and isthmus-free grafts adopt *Hoxa2* expression and second-arch fates. Trainor and Krumlauf found the latter; additionally implanting an FGF8 bead with isthmus-free grafts should reproduce the duplication if FGF8 from the isthmus mediated it.

7. Why do patients with Waardenburg syndrome type 4 have both deafness and Hirschsprung disease, and why does piebaldism not cause deafness as often?

   **Answer** Type 4 is caused by mutations in *SOX10*, *EDNRB* or *EDN3*, which are needed by both melanocyte precursors and enteric crest. Melanocytes of the stria vascularis of the cochlea (intermediate cells) are essential for the endocochlear potential, so their absence causes sensorineural deafness; enteric crest deficiency causes aganglionosis. *KIT* mutations in piebaldism mainly affect migration and survival of melanoblasts in the skin; the cochlear melanocytes are often spared, and enteric crest does not depend on KIT, so deafness is rare and the gut is normal. The combinations of features map onto the shared requirements of crest lineages.

8. Treacher Collins syndrome is caused by mutations in a gene needed in all cells for ribosome biogenesis. Why are the defects restricted to the face, and how did mouse experiments test this explanation?

   **Answer** Cranial crest progenitors proliferate very rapidly and require high rates of ribosome production; reduced TCOF1 causes **nucleolar stress**, stabilizes p53 and triggers apoptosis of these cells before and during migration, so fewer crest cells populate the first and second arches, which form the cheekbones, jaws and ears. Other tissues tolerate the reduced capacity. In *Tcof1* heterozygous mice, crossing in a *Trp53* mutation or inhibiting p53 chemically prevented the apoptosis and rescued the craniofacial defects (Jones et al. 2008), confirming that cell death mediated by p53 causes the tissue specificity.

9. (Open) Crest-like cells exist in tunicates, but cartilage-forming crest is found only in vertebrates. Propose comparative experiments (in lamprey, tunicate and gnathostome embryos) to identify how the skeletogenic programme was added to the crest network.

   **Answer** Compare the expression and regulation of crest specifiers and skeletogenic genes (*Sox9*, *Runx2*, *Col2a1*) in border cells of tunicates (*Ciona*), lampreys and chick or mouse; map the enhancers of these genes (ATAC-seq, reporter assays across species) to find whether skeletogenic genes acquired enhancers bound by crest specifiers (such as Twist or Ets1) in vertebrates; test sufficiency by expressing vertebrate factors (for example Twist) in tunicate border cells and asking whether they become migratory mesenchyme that expresses cartilage genes (Abitua et al. showed that Twist misexpression makes *Ciona* border cells migrate). Loss of function in lamprey (CRISPR) would show which components are needed for cartilage there.
