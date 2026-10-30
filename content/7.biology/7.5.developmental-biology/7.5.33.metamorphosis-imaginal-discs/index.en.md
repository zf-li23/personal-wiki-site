---
title: Metamorphosis and Imaginal Discs
description: The hormonal reactivation of development after embryogenesis. Amphibian metamorphosis (thyroid hormone, deiodinases, the dual function of the thyroid hormone receptor, regional programs, neoteny); insect molting and metamorphosis (PTTH, ecdysone and 20E, juvenile hormone, the EcR/Usp cascade and the puff model, critical weight and final size); imaginal discs, their eversion and Percus's energy model of leg segments; patterning of the wing disc (Hedgehog, Dpp, Notch, Wingless); compartments, polyclones, the Minute technique and selector genes; the Kauffman-Shymko-Trabert model of compartments as nodal lines of Turing modes (time-dependent diffusivities, Bessel and elliptic eigenfunctions, binary codes and transdetermination, conformal maps); the nonlinear theory of how boundaries become sharp (amplitude equations, a potential for degenerate modes, shocks at nodal lines) and its modern assessment; metamorphosis of the sea urchin pluteus.
---

Many animals pass through a larval stage that is built for a different life from that of the adult: a tadpole swims and filters algae, a frog hops and catches insects; a caterpillar eats leaves, a moth sips nectar and reproduces. The transition between the two is metamorphosis, a second round of development, set off after embryogenesis by hormones, in which larval organs are destroyed and adult organs are built, often from groups of cells set aside in the embryo for the purpose. This chapter treats metamorphosis in amphibians and insects, the two cases where its **endocrine** control is understood, and then the imaginal discs of *Drosophila*, the sacs of epithelium from which the adult fly's appendages are made. The wing disc is where **compartments** were discovered, units of **cell lineage** that also turned out to be units of patterning; and the striking order in which compartment boundaries appear inspired one of the most ambitious mathematical models of development, the Kauffman–Shymko–Trabert (KST) theory, which explained them as nodal lines of Turing modes in a growing tissue. We develop that theory fully, with its nonlinear extension by Percus and Childress, and then confront it with what the molecular analysis of selector genes has shown. The patterning signals of the disc (Hedgehog, Dpp, Wingless, Notch) were introduced in [7.5.3](/7.5.3) and [7.5.15](/7.5.15), the **morphogen** gradients they form in [7.5.11](/7.5.11), and the Turing mechanism in [7.5.12](/7.5.12); the growth control of the disc is continued in [7.5.34](/7.5.34).

## 33.1. Metamorphosis and Molting

**Definition 33.1.1 (Metamorphosis)** **Metamorphosis** is the developmental transition, after embryogenesis and under hormonal control, from a larva to an adult of very different form, physiology and habitat, in which larval tissues are destroyed or remodelled and adult tissues are formed, in part from cells set aside for that purpose.

**Definition 33.1.2 (Molting)** *Molting* (ecdysis) is the periodic shedding of the cuticle of arthropods (and other ecdysozoans), preceded by the secretion of a new, larger cuticle by the epidermis; the stage between two molts is an *instar*. A molt may produce an instar of the same kind (larva to larva) or of a different kind (larva to pupa, pupa to adult).

Insects are classified by the extent of their metamorphosis.

| Type | Life history | Examples |
|---|---|---|
| Ametabolous | the hatchling is a small adult; it molts and grows, without metamorphosis | silverfish |
| Hemimetabolous (incomplete) | nymphs resemble the adult but lack wings and genitalia; wing pads grow outside the body at each molt; the final molt makes the adult | grasshoppers, cockroaches, true bugs |
| Holometabolous (complete) | the larva is radically different; adult structures grow inside the larva from imaginal discs; a non-feeding pupa rebuilds the body | beetles, flies, butterflies, bees |

Complete metamorphosis evolved once, in the common ancestor of the Holometabola, which today comprise most insect species. Among vertebrates, metamorphosis is characteristic of amphibians and occurs in some fish (flatfish, lampreys, eels); many marine invertebrates have planktonic larvae that metamorphose on settlement (Section 33.10).

## 33.2. Amphibian Metamorphosis

### 33.2.1. What Changes

| System | Tadpole | Frog |
|---|---|---|
| Locomotion | tail fin | tetrapod limbs; tail resorbed |
| Respiration | gills, skin; larval haemoglobin | lungs, skin; adult haemoglobin with lower oxygen affinity |
| Nutrition | herbivorous filter feeder; long coiled intestine | carnivore; short gut with a new epithelium; jaws and tongue |
| Excretion | ammonia (ammonotelic) | urea (ureotelic): urea-cycle enzymes induced in the liver |
| Nervous system | lateral line; eyes lateral | lateral line lost; eyes move forward and dorsally, with new ipsilateral retinal projections for binocular vision; new motor **neurons** for the limbs |

The changes are coordinated by one hormone. Gudernatsch (1912) fed tadpoles with mammalian thyroid tissue and they metamorphosed precociously into miniature frogs; Allen (1916) removed the thyroid rudiment of early tadpoles, which never metamorphosed and grew into giant tadpoles. Thyroid hormone is both necessary and sufficient.

### 33.2.2. Thyroid Hormone and Its Receptor

The axis runs from the hypothalamus, whose corticotropin-releasing hormone (CRH) is the main stimulator of pituitary thyrotropin (TSH) in frogs, to the thyroid gland, which secretes thyroxine (T4). T4 is largely a prohormone. In the target cells, type II deiodinase (D2) removes an iodine from its outer ring to make the active tri-iodothyronine (T3), and type III deiodinase (D3) removes an inner-ring iodine to inactivate T3 to T2. The amount of active hormone in each tissue is set locally by the balance of the two enzymes: tissues with high D2 respond early, and tissues that express D3 are protected; tadpoles engineered to overexpress D3 in their tissues never complete metamorphosis.

T3 acts through the thyroid hormone receptors TRα and TRβ, **nuclear receptors** that bind DNA as heterodimers with the retinoid X receptor (RXR) at thyroid **hormone response elements**. They have a dual function. Without hormone, TR/RXR is bound to its target genes and recruits **corepressor** complexes (N-CoR, SMRT with histone deacetylases), which keep the **chromatin** closed; with T3 it releases them and recruits **coactivators** (SRC proteins, p300 with histone acetylases). The dual function explains two observations. Before metamorphosis, unliganded TRα actively represses metamorphic genes, so that the tadpole remains a tadpole and grows; and knockdown of TRα accelerates development of some tissues even in the absence of hormone. The gene for TRβ is itself a direct target of TR, so T3 induces its own receptor: a positive feedback ([7.3.18](/7.3.18)) that makes the response to the rising hormone switch-like.

![Thyroid hormone and amphibian metamorphosis. A: the endocrine axis and the intracellular control: CRH stimulates TSH, TSH the release of T4; in the target cell deiodinase D2 converts T4 to active T3 and D3 inactivates it; T3 bound to TR/RXR turns a repressor into an activator and induces TRβ itself. B: plasma thyroid hormone (schematic) over the Nieuwkoop-Faber stages of *Xenopus*, peaking at metamorphic climax, and the order of responses: limb growth at low levels, tail resorption at the peak](./plots/amphibian-metamorphosis.py)

### 33.2.3. Regional Programs

The same hormone has opposite effects in different tissues, because each tissue reads it with its own competence ([7.5.3](/7.5.3)). The limbs grow and differentiate at low hormone levels, early; the tail is resorbed at the climax. Tail resorption is **programmed cell death** of the muscle, notochord and epidermis, carried out by **caspases** ([7.3.25](/7.3.25)) and **matrix metalloproteinases** induced by T3, and helped by the immune system, which attacks tail cells that express larval antigens (the Ouro proteins). A tail grafted onto the trunk degenerates on schedule, whereas an eye cup grafted into the tail survives the tail's destruction: the response is a property of the tissue. The intestine remodels by **apoptosis** of the larval epithelium and proliferation of adult **stem cells** derived from it; the liver begins to express urea-cycle enzymes; the brain and the eyes are rebuilt.

The sequence of events was first described as a threshold model: early events need little hormone, late events more. Molecularly, timing also depends on the tissue-specific rise of D2 and TRβ and on modulating hormones: corticosterone synergizes with T3, prolactin inhibits its effects. Some salamanders retain the larval form and reproduce as larvae (neoteny, a form of **heterochrony**, [7.5.39](/7.5.39)). The axolotl *Ambystoma mexicanum* has low thyroid hormone, and T4 given to it in the water induces metamorphosis; the mudpuppy *Necturus* does not metamorphose even with hormone, because its tissues have lost competence. Thyroid hormone also controls the late fetal maturation of the mammalian brain, which is why congenital hypothyroidism causes intellectual disability unless treated at birth ([7.14](/7.14)).

## 33.3. Insect Molting and Metamorphosis

### 33.3.1. The Hormones

Two effector hormones control molting and metamorphosis: the steroid 20-hydroxyecdysone (20E) initiates every molt, and the sesquiterpenoid juvenile hormone (JH) decides its kind.

**Definition 33.3.1 (Ecdysone)** *Ecdysone* is the **steroid hormone** secreted by the prothoracic glands of insects that, after conversion to 20-hydroxyecdysone in peripheral tissues, initiates each molt and the metamorphic changes of gene expression, acting through a **nuclear receptor** formed by the ecdysone receptor (EcR) and Ultraspiracle (Usp).

**Definition 33.3.2 (Juvenile Hormone)** *Juvenile hormone* (JH) is the lipid hormone of the corpora allata that, when present at a molt, keeps the epidermis in its current, juvenile state, so that the molt produces another larva; its absence allows the molts to pupa and adult. It acts through the receptor Methoprene-tolerant (Met) and its target Krüppel homolog 1 (Kr-h1).

The pathway starts in the brain. Neurosecretory cells release prothoracicotropic hormone (PTTH), a peptide that acts on the prothoracic gland through the **receptor tyrosine kinase** Torso (the same receptor that patterns the termini of the fly embryo, [7.5.14](/7.5.14)) to stimulate ecdysone synthesis. In a larval molt, a small pulse of 20E commits the epidermis to make new cuticle and a larger one starts the differentiation events of the molt. In the last larval instar the corpora allata stop making JH and the hemolymph acquires JH esterase; when JH has fallen below a threshold, PTTH is released, and a small "commitment" pulse of 20E in the absence of JH reprograms the epidermis to pupal development. A large pulse then triggers the pupal molt. JH appears briefly again before pupation and is absent during adult development, when another pulse of 20E drives the adult molt.

The hormones' roles were discovered by classical experiments of the kind that dominate the history of endocrinology. Wigglesworth, working on the blood-sucking bug *Rhodnius prolixus*, decapitated larvae at different times after their blood meal: those decapitated early never molted, those decapitated after a critical period did, so a head factor released in that period is necessary; joining a decapitated larva to a molting one by a capillary (parabiosis) made it molt, so the factor is blood-borne. Removing the corpora allata from a young larva made it molt prematurely into a small adult, and implanting corpora allata from young larvae into last-instar larvae made them molt into giant extra larval instars: JH is necessary and sufficient for the "status quo".

![Hormonal control of molting and metamorphosis in *Manduca sexta* (schematic). A: PTTH from the brain acts through Torso on the prothoracic gland, which makes ecdysone, converted to 20E peripherally and acting through EcR/Usp; the corpora allata make JH, acting through Met and Kr-h1; JH present at a molt gives another larva, absent a pupa or adult. B: titres in the last larval instar and the pupa: JH falls after the critical weight, a small pulse of ecdysteroid commits the epidermis to pupal development, a large pulse starts the pupal molt; JH reappears briefly before pupation; ecdysteroids drive adult development in the pupa](./plots/insect-hormones.py)

### 33.3.2. The Ecdysone Cascade

20E, like thyroid hormone, acts through **nuclear receptors**: EcR, the homologue of the vertebrate liver X receptor, partnered with Ultraspiracle, the homologue of RXR. The giant polytene chromosomes of the *Drosophila* larval salivary glands show its action directly. Within minutes of exposure to 20E a few bands decondense into "early puffs", sites of intense transcription; hours later, when the early puffs regress, many "late puffs" appear. Protein synthesis inhibitors prevent the late puffs but not the early ones and prolong the early puffs. From these observations Ashburner (1974) inferred a hierarchy: the hormone–receptor complex directly activates a small set of early genes and represses the late genes; the products of the early genes activate the late genes and repress their own. The early genes were later identified as transcription factors: *E74*, *E75* and the *Broad* complex, a family of zinc-finger proteins made by **alternative splicing**, which specifies pupal fates (its isoforms differ between tissues). Their targets include the "secondary-response" genes for cuticle proteins, digestive enzymes and cell death. The JH pathway intersects the cascade: in larvae, JH–Met induces Kr-h1, which represses *Broad* and the adult specifier *E93*; in the absence of JH, 20E induces *Broad* at the larval–pupal transition and *E93* at the pupal–adult transition.

### 33.3.3. Critical Weight and Final Size

How does a larva know when to metamorphose? In *Manduca sexta* the decision is made when the last-instar larva reaches a critical weight, about $5\,\mathrm{g}$, half of its final weight (Nijhout and Williams 1974). Starved larvae beyond critical weight still pupate on schedule; larvae starved below it delay metamorphosis. After critical weight is reached, the corpora allata shut down and JH is cleared, PTTH is released at the next permissive photoperiodic gate, and feeding continues until ecdysone stops it. Final size is then set by growth during this terminal period.

**Formula 33.3.1 (Final Size)** If a larva grows exponentially at rate $g$ during the last instar, reaches the critical weight $M_{\mathrm{c}}$, and continues to grow for the time $\Delta t$ taken to clear JH, wait for the PTTH gate and secrete ecdysone, its final mass is

$$
M_{\mathrm{final}}=M_{\mathrm{c}}\,\mathrm{e}^{g\Delta t}.
\tag{33.1}
$$
Final size depends on three parameters, the threshold $M_{\mathrm{c}}$, the growth rate and the delay, which are separately heritable and separately affected by the environment.

**Example 33.3.1** In *Manduca* at $25\,^\circ\mathrm{C}$, $M_{\mathrm{c}}\approx5\,\mathrm{g}$ and the terminal growth period lasts about two days, during which the larva doubles its mass, so $g\approx0.35\,\mathrm{d^{-1}}$ and $M_{\mathrm{final}}\approx10\,\mathrm{g}$. From hatching (about $1\,\mathrm{mg}$) the larva has grown about ten-thousandfold in five instars. Selection for larger body size in laboratory populations increased all three factors; in *Drosophila* the critical weight is sensed by the prothoracic gland through insulin and TOR signaling, and damage to the imaginal discs delays metamorphosis through the relaxin-like peptide Dilp8, so that the discs can regenerate before the larva pupates ([7.5.34](/7.5.34)).

## 33.4. Imaginal Discs

**Definition 33.4.1 (Imaginal Disc)** An **imaginal disc** is a sac of epithelium in the larva of a holometabolous insect, set aside in the embryo and growing during larval life, that forms a particular adult structure (a wing, a leg, an eye with its antenna, the genitalia) and part of the adjacent body wall at metamorphosis.

The *Drosophila* larva carries 19 discs: nine pairs (eye-antennal, labial, clypeolabral, humeral, three pairs of leg discs, wing and haltere) and one unpaired genital disc. The abdominal epidermis of the adult comes from small nests of histoblasts. Each disc arises in the embryo as a cluster of 20–40 cells; the thoracic discs are specified at the intersection of the Wingless and Dpp stripes, across a **parasegment** boundary, in cells that express *Distal-less*; the ventral part of each cluster becomes a leg disc and, in T2 and T3, a dorsal part expressing *escargot* splits off as the wing or haltere disc (Wolpert 10.1). During larval life the wing disc grows about a thousandfold, to some $5\times10^4$ cells, by 10–11 divisions of 8–10 hours. Disc identity is set by the **Hox genes** ([7.5.15](/7.5.15)): Ultrabithorax makes T3 discs halteres instead of wings, and ectopic Antennapedia transforms the antennal disc into a leg disc. Discs are also highly regulative: when cells are killed or a part is removed, the disc regenerates to the correct size and pattern.

![The imaginal discs of *Drosophila* (schematic, not to scale). A: a third-instar larva with its imaginal discs: eye-antennal, three pairs of leg discs, wing, haltere and genital. B: the adult structures they form, labeled in matching colours; each wing disc forms one wing and the notum of the mesothorax](./plots/imaginal-discs.py)

### 33.4.1. Eversion and an Energy Model of Leg Segments

A mature leg disc is a flat epithelium folded into concentric rings, "reminiscent of a Danish pastry". The center will form the distal tip, the claw; successive rings form the tarsal segments, tibia, femur, trochanter and coxa, and the rim the body wall. The rings are specified along the proximo-distal axis by the levels of Wingless (ventral) and Dpp (dorsal), which together activate *Distal-less* at the center, the intermediate gene *dachshund* in a middle ring and the proximal *homothorax* at the rim. At pupariation the first pulse of 20E stops division in the disc and triggers eversion: the rings telescope out into a tube, mainly by changes in cell shape and by rearrangements of cells, so that each ring becomes a cylindrical segment.

Percus and Childress ask why rings become cylinders of particular proportions. After sorting by adhesion ([7.5.7](/7.5.7)), the disc consists of patches of homogeneous cells, which can be treated as units of a coarser tissue. Consider one segment, a cylinder of radius $y(x)$ and length $L$, made of $N_L$ bands each containing $N_c$ patches, with adhesive excess energy proportional to the boundary length between patches. The circumferential boundaries contribute $\alpha_LN_L/L\equiv\alpha/L$ per unit area, the longitudinal ones $\alpha_cN_c/(2\pi y)\equiv\beta/y$. The elastic energy of bending a thin sheet is, per unit area, $\frac D2\big[(K_1+K_2)^2-2(1-\nu)K_1K_2\big]$, with $D$ the bending modulus, $\nu$ the Poisson ratio and $K_1$, $K_2$ the principal curvatures, which for a surface of revolution are

$$
K_1=\frac{y''}{(1+y'^2)^{3/2}},\qquad K_2=-\frac{1}{y(1+y'^2)^{1/2}} .
$$

**Proposition 33.4.1 (Segments as Energy Minima)** Let a segment of area $A=2\pi\int_0^Ly\sqrt{1+y'^2}\,\mathrm{d}x$ minimize the total energy $\mathcal E=2\pi\int_0^Ly\sqrt{1+y'^2}\,E(y,y',y'')\,\mathrm{d}x$, with $E$ the sum of bending and boundary energies per unit area, at fixed $A$ (Lagrange multiplier $\lambda$) and with $y'(0)=y'(L)=0$ (the segment joins its neighbours smoothly). Then:

(a) the Euler–Lagrange equation of the fourth-order problem $\int f(y,y',y'')\,\mathrm{d}x$ is $f_y-\frac{\mathrm{d}}{\mathrm{d}x}f_{y'}+\frac{\mathrm{d}^2}{\mathrm{d}x^2}f_{y''}=0$, with natural boundary conditions $f_{y'}-\frac{\mathrm{d}}{\mathrm{d}x}f_{y''}=0$ at $x=0,L$;

(b) the cylinder $y\equiv R$ satisfies it provided $\frac D{2R^2}=\lambda+\frac\alpha L$;

(c) if the length of the segment is also free at fixed area, the optimal radius and length are related by

$$
\alpha R^2=L(D+\beta R),\qquad\text{that is}\qquad \frac LR=\frac{\alpha R}{D+\beta R}.
\tag{33.2}
$$

**Proof** (a) Vary $y\to y+\delta y$ and integrate by parts twice: $\delta\int f=\int(f_y-\frac{\mathrm{d}}{\mathrm{d}x}f_{y'}+\frac{\mathrm{d}^2}{\mathrm{d}x^2}f_{y''})\delta y\,\mathrm{d}x+\big[(f_{y'}-\frac{\mathrm{d}}{\mathrm{d}x}f_{y''})\delta y+f_{y''}\delta y'\big]_0^L$, and $\delta y'=0$ at the ends by the boundary conditions. This is the **Euler–Lagrange equation** for second derivatives ([2.4.13](/2.4.13)). (b) For the integrand $f=2\pi y\sqrt{1+y'^2}\,(E+\lambda)$, at $y'=y''=0$ the terms $f_{y'}$ and $\frac{\mathrm{d}}{\mathrm{d}x}f_{y''}$ vanish (they are odd in $y'$ or constant along the cylinder), so the condition reduces to $f_y=0$. With $E=\frac D{2y^2}+\frac\alpha L+\frac\beta y$ on the cylinder, $f=2\pi\big(\frac D{2y}+\lambda y+\frac{\alpha y}L+\beta\big)$ and $f_y=2\pi\big(-\frac D{2y^2}+\lambda+\frac\alpha L\big)=0$. (c) The energy of a cylinder is $\mathcal E=2\pi RL\big(\frac D{2R^2}+\frac\alpha L+\frac\beta R\big)=\frac{DA}{2R^2}+2\pi\alpha R+\frac{\beta A}R$ with $L=A/(2\pi R)$. Setting $\mathrm{d}\mathcal E/\mathrm{d}R=-\frac{DA}{R^3}+2\pi\alpha-\frac{\beta A}{R^2}=0$ and substituting $A=2\pi RL$ gives $\alpha R^2=L(D+\beta R)$. $\square$

The relation (33.2) says that thin segments are short and thick ones long, with $L\propto R^2$ when bending dominates ($\beta R\ll D$) and $L\propto R$ when the longitudinal boundaries dominate; Percus and Childress report that a relation of this kind fits the segments of the *Drosophila* leg "quite well". The analysis is at a very gross level, as they say: eversion is driven by the cellular events described above, including Rho-dependent cell shape changes and the remodelling of the peripodial membrane, and the energy model only asks whether the final shapes are consistent with a minimum of interfacial and bending energy.

![Eversion of the leg disc. A: the third-instar leg disc as concentric rings, the centre expressing Distal-less (claw, tarsus), a middle ring dachshund (tibia, femur) and the rim homothorax (coxa). B: the everted leg: the centre of the disc has telescoped out to become the distal tip. C: Percus's energy model, Proposition 33.4.1 (c): the optimal ratio of length to radius of a segment against its radius for three ratios of longitudinal to circumferential boundary energy](./plots/leg-evagination.py)

## 33.5. Patterning the Wing Disc

The wing disc is patterned by two orthogonal signaling boundaries, each at the border between two compartments (Section 33.6).

Anterior–posterior. *engrailed* is expressed in all posterior cells, from the embryonic **parasegment** onward, and induces *hedgehog*; Engrailed also makes posterior cells unable to respond to Hedgehog. Hedgehog diffuses a few cell diameters into the anterior compartment, where it stabilizes the activator form of Cubitus interruptus and induces *decapentaplegic* (*dpp*) in a narrow stripe of anterior cells along the boundary ([7.5.15](/7.5.15) for the same logic in the embryonic segment). Dpp, a BMP, spreads into both compartments and forms a **morphogen** gradient ([7.5.11](/7.5.11)): high levels activate *spalt* close to the source, lower levels *optomotor-blind* (*omb*) more widely, and Dpp signaling represses *brinker*, which is therefore expressed at the edges. The pattern of veins is laid down at the borders of these domains. Clones of cells lacking the Dpp receptor Thickveins lose *spalt* and *omb* cell-autonomously wherever they lie, showing that Dpp acts directly at a distance; and the gradient expands with the growing disc, a case of scaling maintained by feedback through the expander Pentagone ([7.5.11](/7.5.11)). Dpp signaling is also needed for growth: without it the wing does not grow, and ectopic Dpp causes overgrowth ([7.5.34](/7.5.34)).

Dorso-ventral. In the second instar *apterous* is activated in the dorsal cells. Apterous induces *fringe*, whose glycosyltransferase modifies Notch so that it responds to Delta but not to Serrate; Serrate is made by dorsal cells and Delta by ventral ones, so Notch is activated only in a stripe of cells along the DV boundary, where it induces *wingless*. Wingless and the selector gene *vestigial* define the wing pouch: Vestigial is activated at the boundary by Notch and then propagated outward by a feed-forward recruitment in which Vg-expressing cells send a signal that induces *vg* in their neighbors, while Wingless acts as a long-range **growth factor**. The leg disc uses the same signals differently: Wingless in a ventral sector and Dpp in a dorsal sector together activate *Distal-less* at the center, the future tip of the leg.

![Patterning of the wing disc (schematic, anterior left, notum up). A: compartments and selector genes: engrailed and hedgehog in the posterior compartment, apterous in the dorsal; Hedgehog induces the anterior dpp stripe at the AP boundary, Notch signalling induces wingless at the DV boundary; vestigial marks the pouch. B: the Dpp gradient and its nested targets spalt and optomotor-blind. C: a readout model: exponential Dpp signal from the stripe, two thresholds giving the narrow spalt and wider omb domains, and brinker repressed by Dpp](./plots/wing-disc.py)

## 33.6. Compartments

### 33.6.1. Clonal Analysis

The discovery came from clonal analysis. Garcia-Bellido, Ripoll and Morata (1973) induced **mitotic recombination** by X-rays in larvae heterozygous for a **recessive** cuticle marker (such as *multiple wing hairs*), producing homozygous marked clones, the descendants of a single cell at the time of irradiation ([7.4.9](/7.4.9)). Clones induced after the blastoderm stage were long and irregular in shape but never crossed a line through the middle of the wing, a line that corresponds to no vein or other visible feature. To see the line more clearly they used the Minute technique.

**Definition 33.6.1 (Minute Technique)** In the *Minute technique* marked clones are made **wild type** for a dominant *Minute* mutation (a heterozygous loss of a ribosomal protein gene) in an animal heterozygous for *Minute*. The *Minute*$^+$ clone divides faster than its *Minute*/$+$ neighbors, which it outcompetes and eliminates, so the clone grows very large without changing the size or shape of the final wing.

A single *Minute*$^+$ clone could fill almost the entire anterior or posterior half of the wing, its edge running exactly along the same straight line. The line is a boundary of clonal restriction: once established, cells and their descendants on one side never cross to the other. (The elimination of slow-growing cells by faster neighbours, cell competition, is itself an important mechanism of size control, [7.5.34](/7.5.34).)

**Definition 33.6.2 (Compartment)** A **compartment** is a region of a developing tissue populated by the descendants of a group of founder cells and bounded by a line of clonal restriction that the descendants of cells on either side do not cross, although cells on both sides may share common ancestors from before the boundary formed.

**Definition 33.6.3 (Polyclone)** A *polyclone* (Crick and Lawrence 1975) is the set of all cells of a compartment, the descendants of its founder cells. A founder cell of a compartment is a cell whose descendants all lie in the compartment, while its mother cell had descendants outside it as well (in the other compartment).

Founder cells defined in this way need not all exist at the same time. If we require them to be simultaneous, the founders are simply the cells present on each side when the boundary forms; tracing lineages backward with the second definition gives a much smaller group. The timing of restriction is measured by inducing clones at different times. The anterior–posterior restriction of the wing is already present at the blastoderm stage, when it coincides with the parasegment boundary; the dorso-ventral restriction appears during the second larval instar; later restrictions separate the wing from the notum and divide the notum and the proximal and distal wing.

![Clonal analysis and compartments (schematic adult wings). A: marked clones induced in the larva are long and irregular but never cross the anterior-posterior compartment boundary (dashed). B: a fast-growing Minute⁺ clone fills almost its whole compartment and stops exactly at the boundary. C: a clone induced in the embryo before the boundary forms (yellow) can span both compartments; clones induced in the larva (red) respect it](./plots/compartment-clones.py)

### 33.6.2. Selector Genes and the Boundary

Compartments were later shown to be units of gene expression as well as of lineage.

**Definition 33.6.4 (Selector Gene)** A *selector gene* is a gene, expressed throughout a compartment and in none of its neighbors, whose activity is required for its cells to adopt the identity of that compartment and to respect its boundary.

*engrailed* is the selector of posterior compartments: clones lacking *engrailed* in the posterior compartment develop anterior structures, and they cross the boundary into the anterior compartment. *apterous* is the dorsal selector of the wing. The boundary is kept straight by three mechanisms. Short-range signaling across it (Hedgehog for AP, Notch for DV) gives the boundary cells a distinct state; this state increases the tension of a supracellular actomyosin cable along the boundary, which straightens it and pushes back cells that divide into it (Major and Irvine 2005; Landsberg et al. 2009); and differences in adhesion or affinity between the two populations ([7.5.7](/7.5.7)), for example the leucine-rich-repeat proteins Capricious and Tartan at the DV boundary, keep them from mixing. The compartment boundaries are then used as organizers (Section 33.5): the line of clonal restriction is where the signals that pattern the whole disc are made.

## 33.7. The KST Model: Compartments as Nodal Lines

Before the selector genes were known, the sequence in which compartment boundaries appear suggested a different explanation. Kauffman, Shymko and Trabert (1978) observed that the successive boundaries of the wing disc resemble the successive nodal lines of the eigenfunctions of a vibrating membrane of the disc's shape. A Turing system in a growing tissue becomes unstable to its modes one after another; if each mode, as it grows, is read by the cells as a binary decision (above or below the uniform state), the nodal lines become compartment boundaries and the history of instabilities becomes a binary code of cell states. They called it a "tympanic" theory. It is the most complete model of the idea of [7.5.12](/7.5.12#sec-12.8) that a self-organizing system is steered by the geometry in which it grows.

**Definition 33.7.1 (KST Model)** The *KST model* (Kauffman–Shymko–Trabert) explains **compartmentalization** as a sequence of diffusion-driven instabilities in a growing tissue: as growth or cleavage lowers the effective diffusivities, the Neumann eigenmodes of the tissue's domain become unstable one at a time; the nodal set of each excited mode becomes a compartment boundary, and the sign of the mode on either side sets a binary switch in the cells.

### 33.7.1. Time-Dependent Diffusivities

Consider two **morphogens** $u$, $v$ in a one-dimensional tissue of unit length, linearized about a uniform equilibrium,

$$
u_t-\mu u_{xx}=a_{11}u+a_{12}v,\qquad v_t-\nu v_{xx}=a_{21}u+a_{22}v,
\tag{33.3}
$$
with no-flux boundaries. Cleavage reduces the effective diffusivity: if a path is broken up by $N$ cell membranes per unit length, a molecule's steps are rescaled approximately as $\Delta x\to\Delta x/\sqrt N$, $\Delta t\to\Delta t/\sqrt N$, so $\mu=(\Delta x)^2/\Delta t\to\mu/\sqrt N$; over a period of cleavage a roughly exponential decline is plausible. Growth of the tissue without cleavage acts the same way: on an interval of length $L(t)$ the modes are $\cos(n\pi x/L)$ and $\mu$, $\nu$ always appear in the combinations $\mu/L^2$, $\nu/L^2$, so a tissue that grows is a tissue of fixed size whose diffusivities fall as $L^{-2}$ (a consequence of dimensional analysis). For synchronous division at constant cell size, $L^{-2}$ falls by a factor $\frac12$ per generation in a plane monolayer and by $2^{-2/3}\approx0.63$ in a three-dimensional mass.

**Proposition 33.7.1 (Unstable Window)** For constant $\mu$, $\nu$, the uniform state of (33.3) with $a_{11}+a_{22}<0$ and $\Delta=a_{11}a_{22}-a_{12}a_{21}>0$ is unstable to the mode $\cos kx$ if and only if

$$
Q(k^2)\equiv-\Delta+(\nu a_{11}+\mu a_{22})k^2-\mu\nu k^4>0,
$$
which is possible only if $\nu a_{11}+\mu a_{22}>0$ and $(\nu a_{11}+\mu a_{22})^2>4\mu\nu\Delta$; the growth rate is $2\sigma=a_{11}+a_{22}-(\mu+\nu)k^2+\sqrt{(a_{11}+a_{22}-(\mu+\nu)k^2)^2+4Q(k^2)}$. If $\mu$ and $\nu$ decrease with their ratio $r=\nu/\mu$ fixed, the instability conditions are unchanged, and the window of unstable $k^2$ scales as $1/\mu$: both its ends and the position of its maximum move to larger $k^2$.

**Proof** This is the Turing analysis of Theorem 12.3.1: the trace of the linear operator for mode $k$ is negative, so instability requires a negative determinant, $-Q(k^2)<0$. The two conditions are those for the quadratic $Q$ in $k^2$ to be positive somewhere. Writing $s=\mu k^2$, $Q=-\Delta+(ra_{11}+a_{22})s-rs^2$ depends on $s$ only, so the window in $k^2$ is a fixed window in $s$ divided by $\mu$, and the maximum of $\sigma$ (which also depends only on $s$) is unchanged. $\square$

On the unit interval the modes have $k_n^2=n^2\pi^2$, and as the diffusivities fall the window sweeps upward through them, exciting the modes one after another. The maximal growth rate stays the same; the duration of each mode's excitation lengthens, because the window's ends move apart on the $k^2$ axis, while the spacing of the modes grows linearly in $n$. Eventually several modes lie in the window at once.

**Example 33.7.1 (Mode Selection under Synchronous Cleavage)** Let $(\mu,\nu)=(\mu_0,\nu_0)\theta^m$ in generation $m$, $0<\theta<1$. Then there are constants $A<B$ such that mode $n$ is unstable in generation $m$ exactly when

$$
A<n^2\theta^m<B .
$$
With $A=0.8$, $B=1.2$ and $\theta=2^{-1/2}$ (Percus and Childress, Table 9.1):

| $m$ | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
|---|---|---|---|---|---|---|---|---|---|---|
| $A\theta^{-m}$ | 0.80 | 1.13 | 1.60 | 2.26 | 3.20 | 4.53 | 6.40 | 9.05 | 12.80 | 18.10 |
| $B\theta^{-m}$ | 1.20 | 1.70 | 2.40 | 3.39 | 4.80 | 6.79 | 9.60 | 13.58 | 19.20 | 27.15 |
| unstable $n$ | 1 | — | — | — | 2 | — | 3 | — | 4 | 5 |

A single mode is excited at a time, with gaps, through generation 12 ($n=8$); only in generation 13 are two modes, $n=9$ and $n=10$, unstable together ($n^2\in(72.4,108.6)$). In one dimension it is thus easy to filter out all but one growing mode through many generations; in two dimensions the eigenvalues are much denser, and the separation is less clean. The eigenvalues are not centered in the window, so the growth rates of successive modes differ considerably.

![Sequential excitation of modes as the diffusivities fall (Example 33.7.1). A: growth rate against s = n²θᵐ for two-species Turing kinetics with the diffusivity ratio chosen so that the unstable window spans a factor of 1.5. B: generations and modes; filled squares mark unstable modes. One mode at a time is unstable, with gaps, until generation 13, when modes 9 and 10 are unstable together](./plots/kst-selection.py)

### 33.7.2. Nodal Lines in Two Dimensions

For a planar monolayer filling a domain $\Omega$ (taken fixed, the growth being absorbed into the diffusivities), the modes are the Neumann eigenfunctions of the Laplacian,

$$
\Delta\phi+k^2\phi=0\quad\text{in }\Omega,\qquad\frac{\partial\phi}{\partial\boldsymbol{n}}=0\quad\text{on }\partial\Omega,
\tag{33.4}
$$
the **Helmholtz equation**. On a disc of radius $R$, **separation of variables** in polar coordinates ([2.5.5](/2.5.5)), $\phi=f(r)\,(\cos m\varphi\text{ or }\sin m\varphi)$, gives $f''+f'/r+(k^2-m^2/r^2)f=0$, whose solution regular at the origin is the **Bessel function** $f=J_m(kr)$; the boundary condition requires $J_m'(kR)=0$. For the unit disc the first nonconstant modes are

| $k^2$ | Eigenfunctions | Nodal set |
|---|---|---|
| 3.39 | $J_1(kr)\cos\varphi$, $J_1(kr)\sin\varphi$ | a diameter |
| 9.33 | $J_2(kr)\cos2\varphi$, $J_2(kr)\sin2\varphi$ | two perpendicular diameters |
| 14.68 | $J_0(kr)$ | a circle of radius 0.63 |
| 17.65 | $J_3(kr)\cos3\varphi$, $J_3(kr)\sin3\varphi$ | three diameters |

(the squares of the first zeros of $J_m'$: $1.841$, $3.054$, $3.832$, $4.201$; Percus and Childress list $3.4$, $9.6$, $14.4$, $17.6$). The angular modes are doubly degenerate. A deformation of the boundary splits the degeneracy, and on an ellipse with semi-axes $a>b$ the first mode has the minor axis as its nodal line, the second the major axis; for an eccentricity $e=(1-b^2/a^2)^{1/2}=0.8$ the third mode is a perturbation of $J_2\sin2\varphi$ turned into a second "one-dimensional" harmonic along the long axis, with two nodal lines across it, and is excited before the cross-shaped mode; similarly the next long-axis harmonic, from $J_3$, comes before the continuation of the circular $J_0$ mode. In the KST theory the ellipse represents a domain in which the first few eigenvalues are well separated. For an ellipsoidal shell, such as a blastoderm, the first two nodal surfaces can be read as the anterior–posterior and dorso-ventral divisions.

![Nodal lines of Neumann eigenfunctions, Eq. (33.4). A: the first four nonconstant modes of the unit disc (J₁, J₂, J₀, J₃, with their eigenvalues; the degenerate sin mφ partners are rotated copies). B: the first six nonconstant modes of an ellipse of the same area with eccentricity 0.8 (finite differences): the minor-axis line, the major-axis line, two transverse lines, the cross, three transverse lines, and a more complex sixth mode. Black lines are nodal lines, the candidate compartment boundaries](./plots/kst-modes.py)

### 33.7.3. The Sequence in the Wing Disc

In the first instar the wing disc has a few dozen cells; it grows exponentially through 10 or 11 divisions to about $5\times10^4$ cells (Percus and Childress give $10^2$ to $10^5$). Compartment boundaries formed late, just before pupariation, can be revealed only with fast-growing *Minute*$^+$ clones. Traced back to the disc, the boundaries in the order of their formation are: anterior–posterior (AP), dorso-ventral (DV), the dorsal and ventral thorax–wing boundaries (dtw, vtw), the dorsal and ventral scutum–scutellum boundaries (dsp; vsp, which was a prediction of KST and had not been observed), and the distal–proximal wing boundary (dpw). Kauffman et al. noted that this sequence matches the sequence of nodal lines of an ellipse of eccentricity about 0.8 and of a growth path in a parameter plane that roughly follows the shape changes of the disc. The AP line, the first boundary in the disc, is the second nodal line of the ellipse; in the KST interpretation it recapitulates an anterior–posterior polarity already imposed on the disc by the first division of the ellipsoidal blastoderm.

### 33.7.4. Binary Codes and Transdetermination

The blastoderm is roughly an ellipsoid with axis ratio 3.7 : 1. In a Turing model the easiest modes to excite are then waves along the long axis, and only after a few of them does the first dorso-ventral mode intervene. The observed **fate map** agrees if the dorso-ventral restriction follows three longitudinal ones, distinguished by the fall of diffusivity at cellularization. Four such events can be regarded as an ordered set of binary switches, so that each region of the blastoderm, and the discs that arise from it, carries a code $a_1a_2a_3a_4$, $a_i\in\{0,1\}$, and neighboring compartments differ in one digit.

The code was tested with **transdetermination**. A disc cultured for long periods in the abdomen of adult flies, where it proliferates without metamorphosing, and then implanted into a larva to metamorphose, occasionally forms structures normally made by another disc (genital to leg or antenna, leg to wing, antenna to wing), in preferred directions ([7.3.24](/7.3.24)). If **transdetermination** resets binary switches, its frequency should fall with the number of digits by which the two codes differ. The observed frequencies agreed remarkably well with the predictions of KST, which was taken as evidence for a quantitative measure of developmental distance between cell states.

**Example 33.7.2 (Codes and Distances)** With four switches there are 16 states. In a code in which genital = 0000, leg = 0100, antenna = 0110 and wing = 1110, the Hamming distances are genital–leg 1, leg–antenna 1, antenna–wing 1, genital–wing 3. If each switch flips independently with a small probability $p$ per culture passage, the probability of a direct transition between states at distance $d$ is of order $p^d$, so **transdetermination** from genital to wing should be much rarer than genital to leg, and should usually pass through the intermediate states, as observed. Inferring the code from the frequencies is an inverse problem. All admissible codes agree that adjacent compartments differ in one letter; they differ in the predicted distance between very dissimilar states, but transdeterminations between such states are rare, so the most informative data are the least accurate.

### 33.7.5. Growth, Helmholtz Modes and Conformal Maps

In the toy version of Section 10.5 of Percus and Childress, a single **morphogen** with deviation $a$ from uniformity satisfies near its potential minimum the Helmholtz equation $\Delta a+k^2a=0$ with no flux on the boundary, and the disc grows, $R=R(t)$. Its solutions are $a=J_m(kr)(\cos m\varphi,\sin m\varphi)$ with $kR$ equal to the zeros of $J_m'$. As $R$ grows, $kR$ passes these values in order; once a nodal line has appeared and been fixed by the cells (the boundary is binary: the sign of $a$), new nodal lines simply add to it. The observed outline of the growing disc can be fed into a numerical solution of the Helmholtz equation, and the predicted sequence agrees well with the compartments.

For approximate analytical work the elliptical boundary can be mapped to a circle. Take the ellipse $\frac{X^2}{(1+t)^2}+\frac{Y^2}{(1-t)^2}=1$ in the plane $Z=X+\mathrm{i}Y$, $0<t<1$.

**Proposition 33.7.2 (Helmholtz Problem on an Ellipse)** The Joukowski map $Z=z+t/z$ sends the unit circle $\lvert z\rvert=1$ onto the ellipse and the circle $\lvert z\rvert=\sqrt t$ onto the segment between its foci, so the annulus $\sqrt t<\lvert z\rvert<1$ covers the ellipse cut along the focal segment. In terms of $z=x+\mathrm{i}y$ the Helmholtz problem becomes

$$
\Delta_za+K^2\Big\lvert1-\frac t{z^2}\Big\rvert^2a=0,
\tag{33.5}
$$
with $\partial a/\partial\boldsymbol{n}=0$ on $\lvert z\rvert=1$ and $a(z)=a(t/z)$ (the two sides of the cut are the same points of the ellipse). The eigenvalues are the stationary values of the **Rayleigh quotient**

$$
K^2=\frac{\iint\lvert\nabla_za\rvert^2\,\mathrm{d}x\,\mathrm{d}y}{\iint a^2\,\lvert1-t/z^2\rvert^2\,\mathrm{d}x\,\mathrm{d}y},
$$
the integrals taken over the annulus, so that approximations can be made with simple trial functions.

**Proof** On $\lvert z\rvert=1$, $z=\mathrm{e}^{\mathrm{i}\varphi}$, $Z=(1+t)\cos\varphi+\mathrm{i}(1-t)\sin\varphi$; on $\lvert z\rvert=\sqrt t$, $Z=2\sqrt t\cos\varphi$, the segment between the foci $\pm2\sqrt t$ (since $(1+t)^2-(1-t)^2=4t$). For a **conformal mapping** $Z=F(z)$ ([2.3.8](/2.3.8)), $\Delta_Z=\lvert F'(z)\rvert^{-2}\Delta_z$, because $\Delta=4\partial^2/\partial Z\partial\bar Z$ and $\partial_z=F'\partial_Z$; here $F'(z)=1-t/z^2$, which gives (33.5). The Dirichlet integral is conformally invariant, $\iint\lvert\nabla_Za\rvert^2\,\mathrm{d}X\,\mathrm{d}Y=\iint\lvert\nabla_za\rvert^2\,\mathrm{d}x\,\mathrm{d}y$, while the area element transforms as $\mathrm{d}X\,\mathrm{d}Y=\lvert F'\rvert^2\mathrm{d}x\,\mathrm{d}y$; the Rayleigh quotient of the ellipse therefore takes the stated form, and its stationary points with the natural (Neumann) boundary condition are the eigenfunctions. $\square$

The same transformation can map any simply connected domain of the disc's shape to a disc or an annulus, which is why Percus and Childress note that the problem "can always be converted to a circle or an annulus with the modified Helmholtz equation".

## 33.8. Nonlinear Theory: How Boundaries Become Sharp

The linear theory produces smooth eigenfunctions, whereas compartment boundaries are sharp. Orientation of division along the boundary or differential adhesion might keep them sharp, but these mechanisms lose force when boundaries are identified with nodal lines, where the chemical gradients are not steep. Percus and Childress show that nonlinear kinetics can steepen a Turing gradient into a shock exactly at a nodal line.

### 33.8.1. Amplitude Equation for a Single Mode

Assume synchronized **mitosis** and two species, and suppose that just after a division the domain has simple eigenpairs $\{\lambda_i,\phi_i\}$, $\lambda_0=0$, $\phi_0=1$, $\frac1{\lvert\Omega\rvert}\int\phi_i\phi_j=\delta_{ij}$. Write the system as

$$
u_t-\mu\Delta u-(a_{11}u+a_{12}v)=P(u,v)+M(u,v),\qquad v_t-\nu\Delta v-(a_{21}u+a_{22}v)=Q(u,v)+N(u,v),
$$
with $P$, $Q$ quadratic and $M$, $N$ of third and higher order. One mode, $\phi_1$, is unstable with a small growth rate $\varepsilon$; all other growth rates have negative real parts of order one. Projecting the linear problem on $\phi_1$ gives $\dot{\boldsymbol\alpha}=B\boldsymbol\alpha$ for $\boldsymbol\alpha=\Pi_1(u,v)$, $B=A-\lambda_1\operatorname{diag}(\mu,\nu)$, with eigenvalues $\varepsilon$ (eigenvector $\boldsymbol{p}_1$) and $\sigma<0$; after a transient the solution is along $\boldsymbol{p}_1$ and grows on the time scale $\tau=\varepsilon t$.

**Proposition 33.8.1 (Amplitude Equation)** On the time scale $\tau=\varepsilon t$, after initial transients, $(u,v)=\varepsilon\,\boldsymbol{p}_1m(\tau)\phi_1(x)+O(\varepsilon^2)$, where

$$
\frac{\mathrm{d}m}{\mathrm{d}\tau}=m-\frac{m^2}{m_0},\qquad\frac1{m_0}=-\frac{q_{11}P(\boldsymbol{p}_1)+q_{12}Q(\boldsymbol{p}_1)}{\boldsymbol{q}_1\cdot\boldsymbol{p}_1}\,\Pi_1(\phi_1^2),
\tag{33.6}
$$
$\boldsymbol{q}_1$ being the adjoint eigenvector; all modes orthogonal to $\phi_1$ have amplitudes of order $\varepsilon^2$, driven passively by $m^2$. The amplitude grows to $m_0$, and the time a residual $O(\varepsilon^2)$ component of a newly unstable mode needs to grow to saturation (order $\varepsilon$) after the next division is of order $-\ln\varepsilon/\varepsilon$, an estimate of the division time required by the theory.

The quantity $m$ plays the role of a single Turing morphogen, and quadratic nonlinearity limits its amplitude. The spatial modulation of the dynamics comes from $\phi(x,t)$, the dominant eigenfunction, which may also change slowly with the shape of the domain; cells reading the morphogen therefore acquire a gradient in their kinetics, and the nodal lines, where $\phi=0$, are exceptional points of the nonlinear theory.

### 33.8.2. Degenerate Modes and a Potential

If several modes have nearby growth rates, as for the degenerate angular modes of a disc, let them span a space $S$ of dimension $s$ with orthonormal basis $\phi_1,\dots,\phi_s$, and write $\phi=\sum_i\alpha_i(\tau)\phi_i$. The same reduction gives

$$
\frac{\mathrm{d}\alpha_i}{\mathrm{d}\tau}=\alpha_i-c\sum_{j,k=1}^sc_{ijk}\alpha_j\alpha_k\equiv-\frac{\partial V}{\partial\alpha_i},\qquad c_{ijk}=\frac1{\lvert\Omega\rvert}\int\phi_i\phi_j\phi_k,\qquad V=\frac c3\sum_{i,j,k}c_{ijk}\alpha_i\alpha_j\alpha_k-\frac12\sum_i\alpha_i^2 .
$$

**Theorem 33.8.1 (Selection of the Nodal Set)** $V$ is a **Lyapunov function**: $\frac{\mathrm{d}V}{\mathrm{d}\tau}=-\sum_i\big(\frac{\mathrm{d}\alpha_i}{\mathrm{d}\tau}\big)^2\le0$, so locally stable equilibria are local minima of $V$. At an equilibrium $V=-\frac16\sum_i\alpha_i^2$. The equilibria are solutions of the nonlinear eigenvalue problem $\eta\phi=\mathcal P(\phi^2)$ with $\frac1{\lvert\Omega\rvert}\int\phi^2=1$, $\mathcal P$ the projection onto $S$, and the globally stable one is that with the smallest $\lvert\eta\rvert$.

**Proof** $\frac{\mathrm{d}V}{\mathrm{d}\tau}=\sum_i\frac{\partial V}{\partial\alpha_i}\frac{\mathrm{d}\alpha_i}{\mathrm{d}\tau}=-\sum_i(\frac{\mathrm{d}\alpha_i}{\mathrm{d}\tau})^2$. At equilibrium, multiplying $\alpha_i=c\sum c_{ijk}\alpha_j\alpha_k$ by $\alpha_i$ and summing gives $\sum\alpha_i^2=c\sum c_{ijk}\alpha_i\alpha_j\alpha_k$, so $V=\frac13\sum\alpha_i^2-\frac12\sum\alpha_i^2=-\frac16\sum\alpha_i^2$. Writing the equilibrium as $\alpha_i=\phi$ scaled to unit norm, $\phi=\hat\alpha/\lvert\hat\alpha\rvert$, the equation becomes $\eta\phi=\mathcal P(\phi^2)$ with $\lvert\eta\rvert=[c^2\sum\alpha_i^2]^{-1/2}$; the deepest minimum of $V$ has the largest $\sum\alpha_i^2$, that is the smallest $\lvert\eta\rvert$. $\square$

There are in general several solutions and hence several candidate nodal sets, but the one that evolves is unique: the nonlinearity chooses among degenerate patterns. (This nonlinear eigenvalue problem was introduced by Turing in unpublished work on the symmetry of Radiolaria.) If $\lvert\eta\rvert$ is very small, cubic and higher terms also enter.

### 33.8.3. Boundaries as Shocks

Now let $\boldsymbol{u}(x,t)$ be an $N$-vector of concentrations with slow parametric dependence on position and time, as just derived,

$$
\varepsilon\frac{\mathrm{d}\boldsymbol{u}}{\mathrm{d}t}=\boldsymbol{f}(\boldsymbol{u},x,t),
$$
and look for a bifurcation from an equilibrium $\boldsymbol{u}_0$ near a nodal point $x_0$ at a time $t_0$. The $N+2$ numbers $\boldsymbol{u}_0,x_0,t_0$ are fixed by (i) $\boldsymbol{f}(\boldsymbol{u}_0,x_0,t_0)=0$ ($N$ equations), (ii) $\det A_0=0$ with $A_0=\nabla_{\boldsymbol u}\boldsymbol f$ (one equation), and a last condition below. Expand $\boldsymbol f$ to third order in $\Delta\boldsymbol u=\boldsymbol u-\boldsymbol u_0$ and first order in $\Delta x$, $\Delta t$, with $B_0=\frac12(\nabla\nabla\boldsymbol f)_0$, $C_0=\frac16(\nabla\nabla\nabla\boldsymbol f)_0$, and assume (iii) the null space of $A_0$ is one-dimensional, $A_0\boldsymbol p=0$, $A_0^{\mathsf T}\boldsymbol q=0$, $(\boldsymbol q,\boldsymbol p)=1$; and (iv) $(\boldsymbol q,B_0:\boldsymbol p\boldsymbol p)=0$, the quadratic term vanishes when projected on the null direction. Condition (iv) is the final equation: it selects, among all the cells taking part in the instability, those on the nodal set, where the quadratic nonlinearity of the morphogen vanishes. Its effect is to replace the generic **fold catastrophe** by a **cusp catastrophe** ([7.5.10](/7.5.10)).

With stretched variables $\Delta\boldsymbol u=\varepsilon^\alpha\boldsymbol U$, $\Delta t=\varepsilon^\beta\tau$, $\Delta x=\varepsilon^\gamma\xi$, two cases arise.

**Theorem 33.8.2 (Stationary Shock)** Case 1: if $(\boldsymbol q,\boldsymbol f_t^0)=0$, the consistent scaling is $\alpha=\frac14$, $\beta=\frac12$, $\gamma=\frac34$. Expanding $\boldsymbol U=\boldsymbol U_0+\varepsilon^{1/4}\boldsymbol U_1+\varepsilon^{1/2}\boldsymbol U_2+\cdots$ with $\boldsymbol U_0=\phi\boldsymbol p$, the solvability condition at order $\varepsilon^{1/2}$ gives, after a shift of time origin $\theta=\tau+\text{const}$,

$$
\frac{\mathrm{d}\phi}{\mathrm{d}\theta}=\sigma+(\boldsymbol q,A^0_t\boldsymbol p)\,\theta\,\phi+\lambda\phi^3,\qquad\sigma=(\boldsymbol q,\boldsymbol f^0_x)\,\xi,\quad\lambda=(\boldsymbol q,B_0:(\boldsymbol p\boldsymbol g_1+\boldsymbol g_1\boldsymbol p))+(\boldsymbol q,C_0\vdots\boldsymbol p^3),
\tag{33.7}
$$
with $\boldsymbol g_1$ from the solution $\boldsymbol U_1=\boldsymbol h_1+\boldsymbol g_1\phi^2$. If $(\boldsymbol q,A^0_t\boldsymbol p)>0$ and $\lambda<0$, the solutions for fixed $\sigma$ converge to the stable sheets of the cusp surface $\sigma+(\boldsymbol q,A^0_t\boldsymbol p)\theta\phi+\lambda\phi^3=0$; the developmental paths on the two sides of $\sigma=0$ diverge, and a stationary shock forms at $\sigma=0$, the nodal point.

The ordering requires $1+\alpha-\beta=\beta=3\alpha=\gamma$, which with $\alpha+\beta=3\alpha$ gives the stated exponents (an attempt to retain the term $A^0_x\boldsymbol U\xi$ leads to a contradiction). The equation (33.7) is the normal form of the cusp with $\sigma$ as the splitting and $\theta$ as the normal parameter: for $\theta<0$ there is one equilibrium, a smooth function of $\sigma$; for $\theta>0$ the cusp opens, and cells with $\sigma>0$ follow the upper sheet and those with $\sigma<0$ the lower one, so the morphogen jumps at the nodal point. Numerically integrating (33.7) from $\theta=-3$ shows a linear gradient steepening into a step (figure below).

![A gradient steepens into a shock at a nodal line, Theorem 33.8.2 with (q, A_t p) = 1 and λ = −1. A: profiles φ(σ), σ the distance from the nodal point, at successive times θ, starting from φ = 0 at θ = −3: the smooth gradient becomes a jump at σ = 0. B: the equilibria σ + θφ − φ³ = 0 (the cusp) for σ = −0.05, 0 and +0.05: for θ > 0 the sign of σ selects the upper or the lower stable branch (solid); the middle branch is unstable (dashed)](./plots/kst-shock.py)

Case 2, probably the more representative, has $(\boldsymbol q,\boldsymbol f_t^0)\ne0$, and the time-dependent forcing then dominates the ordering. Introducing $\sigma^*=(\boldsymbol q,\boldsymbol f^0_x)(x-x_0)+(\boldsymbol q,\boldsymbol f^0_t)(t-t_0)=\varepsilon^\delta\sigma$ as a new space–time coordinate and a two-time formalism, consistency requires $\alpha=\frac15$, $\beta=\gamma=\frac25$, $\delta=\frac35$, and (when $(\boldsymbol q,\boldsymbol f^0_x)\ne0$) the compatibility condition becomes

$$
(\boldsymbol q,\boldsymbol f^0_t)\,\frac{\partial\phi}{\partial\sigma}=\sigma+\gamma(\tau-\tau_0)\phi+\lambda\phi^3,
\tag{33.8}
$$
with $\gamma=(\boldsymbol q,\boldsymbol f^0_x)^{-1}\big[(\boldsymbol q,A_t\boldsymbol p)(\boldsymbol q,\boldsymbol f^0_x)-(\boldsymbol q,A^0_x\boldsymbol p)(\boldsymbol q,\boldsymbol f^0_t)\big]$ and $\lambda$ as before. Of the eight combinations of signs of $(\boldsymbol q,\boldsymbol f^0_t)$, $\gamma$ and $\lambda$, only those with $\operatorname{sgn}(\gamma/\lambda)=-1$ and, for each sign of $(\boldsymbol q,\boldsymbol f^0_t)$, one further choice are stable along the path of development: in the others a perturbation $\delta\phi$ of the asymptotic solution grows as $\mathrm{d}\delta\phi/\mathrm{d}\sigma\approx2\gamma(\tau-\tau_0)\delta\phi$. In the admissible case each cell "differentiates" along a transition profile of $\phi$ as the moving front reaches it, and the transition steepens to a shock as $\tau-\tau_0$ grows. Different cells meet the transition at different times: the boundary is a moving wave of differentiation, a "primary wave" in the language of **catastrophe theory**, whose path is, to first order,

$$
\Big(\frac{\mathrm{d}x}{\mathrm{d}t}\Big)_{\mathrm{wave}}=-\frac{(\boldsymbol q,\boldsymbol f^0_t)}{(\boldsymbol q,\boldsymbol f^0_x)}+\frac{\gamma\operatorname{sgn}(\boldsymbol q,\boldsymbol f^0_t)}{(\boldsymbol q,\boldsymbol f^0_x)}\Big\lvert\frac{\gamma}{3\lambda}\Big\rvert^{1/2}(t-t_0)^{1/2} .
$$
Case 2 is incomplete **compartmentalization**: the boundary moves relative to the tissue, and a compartment is established only when all waves of differentiation have stopped. The conclusion of the analysis is that nonlinear chemical kinetics alone can turn the moderate gradients of a Turing instability into abrupt boundaries at nodal lines, where quadratic terms are negligible, and that quadratic nonlinearity is enough for the analytic description.

## 33.9. Assessment

The KST model was an important step: it was the first serious attempt to explain a reproducible sequence of developmental decisions by the dynamics of a reaction–diffusion system in a growing domain, and it made testable predictions (the vsp boundary, transdetermination frequencies). Its biological premises have not survived the molecular analysis of the disc, as Percus and Childress note in their supplementary remarks. The AP compartment boundary of the disc is inherited from the embryonic **parasegment** boundary and maintained by the selector gene *engrailed*; the DV boundary is created by the activation of the selector gene *apterous* in the second instar; both are maintained by short-range signaling (Hedgehog, Notch) and by mechanical tension along the boundary, not by the sign of a Turing mode. The patterning signals that the boundaries emit are **morphogen** gradients with sources, not eigenfunctions. The resemblance between the order of boundaries and the nodal lines of an ellipse is therefore not causal, although it reflects something real: any process that subdivides a growing elongated tissue in a simple way will tend to cut it first across its long axis.

Transdetermination is now understood molecularly as well. It occurs in regenerating discs at sites of high Wingless signaling, which induces genes of other disc identities, and it is associated with a local loss of Polycomb-mediated silencing ([7.5.15](/7.5.15#sec-15.6)) and with JAK/STAT signaling; the preferred directions reflect the overlap of regulatory programs between discs (leg and wing share many genes) rather than a binary code of compartments. Two parts of the theory remain influential. Mode selection by the shape and the growth of a domain is a real phenomenon in other systems, such as the digits ([7.5.32](/7.5.32)) and the skin appendages ([7.5.22](/7.5.22)); and the analysis of how nonlinear kinetics sharpen boundaries anticipated modern work on the precision of boundaries formed by morphogen readout ([7.5.11](/7.5.11)) and on bistable switches. The statistical physics of tissue fluidity and boundary sharpening, the other modern descendant, is treated in [7.5.8](/7.5.8).

## 33.10. Metamorphosis of the Sea Urchin Pluteus

The larva of a sea urchin, the bilaterally symmetric, planktonic pluteus, feeds with ciliated arms supported by the skeletal rods made by the **skeletogenic mesenchyme** ([7.5.6](/7.5.6)). The adult forms inside it from a separate rudiment. On the left side of the larva, the left coelomic pouch (the hydrocoel) meets an **invagination** of the **ectoderm**, the vestibule, and together they form the echinus rudiment, in which the adult's five-fold symmetry appears: five primary podia, the first tube feet, form around the hydrocoel. When the rudiment is complete the larva is competent to metamorphose. Metamorphosis is triggered by cues of a suitable habitat, typically chemical signals from bacterial films and algae on the sea floor; the larva settles, the rudiment everts, and the larval arms and much of the larval tissue are resorbed within about an hour, leaving a small pentaradial juvenile. Thyroid hormone, obtained from the algal food or synthesized by the larva, accelerates the development of the rudiment in several echinoderms, a striking parallel with amphibians. Indirect development of this kind, a larval body that is used and discarded while the adult forms from a set-aside rudiment, is common in marine invertebrates and resembles in logic the imaginal discs of insects.

## Summary

- Metamorphosis (Definition 33.1.1) and molting (Definition 33.1.2); ametabolous, hemimetabolous and holometabolous insects.
- Amphibians: thyroid hormone is necessary and sufficient (Gudernatsch, Allen); CRH → TSH → T4; local activation by D2 and inactivation by D3; TR/RXR represses without hormone and activates with it; TRβ autoinduction; regional programs (limbs early, tail resorption at climax) depend on tissue competence; neoteny (axolotl, *Necturus*).
- Insects: PTTH → Torso → ecdysone → 20E (Definition 33.3.1), EcR/Usp; JH (Definition 33.3.2) through Met and Kr-h1 sets the character of the molt; Wigglesworth's decapitation and parabiosis; Ashburner's early and late puffs (E74, E75, Broad, E93); critical weight and final size $M_{\mathrm{final}}=M_{\mathrm{c}}\mathrm{e}^{g\Delta t}$ (Formula 33.3.1).
- Imaginal discs (Definition 33.4.1): 19 discs, specified at the Wg/Dpp intersection across **parasegment** boundaries; Hox identity; Dll, dac, hth along the leg PD axis; eversion by 20E; segment shape as an energy minimum, $\alpha R^2=L(D+\beta R)$ (Proposition 33.4.1).
- Wing disc: en/hh posterior → Hh → anterior dpp stripe → Dpp gradient (spalt, omb, brinker); ap dorsal → fringe → Notch at the DV boundary → wg, vg.
- Compartments (Definitions 33.6.1–33.6.4): clonal restriction (Garcia-Bellido), the Minute technique, polyclones and founder cells, selector genes (*engrailed*, *apterous*), boundary maintenance by signaling, actomyosin tension and affinity.
- KST model (Definition 33.7.1): falling diffusivities sweep the unstable window through the modes (Proposition 33.7.1, Example 33.7.1); disc and ellipse eigenfunctions and the wing-disc sequence; binary codes and transdetermination (Example 33.7.2); conformal mapping and the Rayleigh quotient (Proposition 33.7.2).
- Nonlinear theory: amplitude equation (Proposition 33.8.1), a potential selecting the nodal set among degenerate modes (Theorem 33.8.1), shocks at nodal lines (Theorem 33.8.2, case 2 as a moving primary wave). Assessment: compartments are made by selector genes and short-range signals, not Turing modes; transdetermination by Wg and loss of PcG silencing.
- Sea urchin: the adult forms from the echinus rudiment of the pluteus; metamorphosis on settlement.

## Questions

1. A tadpole's tail is grafted onto the trunk of another tadpole, and an eye cup is grafted into its tail. What happens to each at metamorphosis, and what does this tell you about the control of tissue responses?

   **Answer** The grafted tail degenerates on schedule, and the eye cup in the tail survives while the tail around it is resorbed. The response to thyroid hormone is a property of the tissue (its competence: receptors, deiodinases, target genes), not of its position or of local signals. The same circulating hormone kills one tissue and builds another.

2. Explain why thyroidectomized tadpoles grow into giant tadpoles, and why knockdown of TRα in the absence of thyroid hormone can accelerate some metamorphic changes.

   **Answer** Without hormone, the metamorphic program is not triggered, but larval growth continues, so the larva keeps growing beyond normal size. Unliganded TRα is not inactive: bound to target genes with **corepressors**, it actively represses them. Removing TRα removes this repression, so some target genes become partially active even without hormone; this is the dual-function model, in which the receptor is a **repressor** in the absence and an activator in the presence of T3.

3. Wigglesworth decapitated *Rhodnius* larvae at different times after a blood meal. Larvae decapitated within 4 days never molted; those decapitated after 8 days molted. What do you conclude, and how would you show that the factor is carried in the blood?

   **Answer** A factor from the head, released between about 4 and 8 days after feeding, is necessary for molting; once released, the head is no longer required (the prothoracic glands, under its control, take over). Joining a decapitated early larva to one decapitated late by a capillary tube, so that they share hemolymph, makes the early one molt: the factor (PTTH, and the ecdysone it induces) is blood-borne. Implanting brains releases the same effect.

4. Using Formula 33.3.1, by how much would final mass change if the growth rate in the terminal period increased by 20 %, or if JH clearance took half a day longer? Which is the more efficient way for selection to increase body size?

   **Answer** With $M_{\mathrm{c}}=5\,\mathrm{g}$, $g=0.35\,\mathrm{d^{-1}}$, $\Delta t=2\,\mathrm{d}$: $M=10\,\mathrm{g}$. With $g'=0.42$: $M=5\mathrm{e}^{0.84}=11.6\,\mathrm{g}$ (+16 %). With $\Delta t=2.5\,\mathrm{d}$: $M=5\mathrm{e}^{0.875}=12.0\,\mathrm{g}$ (+20 %). Increasing $M_{\mathrm{c}}$ by 20 % gives $12\,\mathrm{g}$ directly. All three are comparable at this scale; laboratory selection for large *Manduca* changed all three, and changes of the threshold and the delay act without requiring faster growth, which may be limited by food.

5. Why does a *Minute*$^+$ clone in a *Minute*/$+$ wing fill most of a compartment without changing the size of the wing? What does this imply about the control of wing size?

   **Answer** The clone's cells divide faster than the slow *Minute*/$+$ cells and outcompete them, which are eliminated by cell competition (**apoptosis** of the "loser" cells). The total size is unchanged because it is controlled at the level of the tissue (by morphogen signaling, mechanical feedback and Hippo signaling), not by the division rate of individual cells: when one population grows faster, the other is reduced. Compartment size, not lineage, is controlled.

6. A clone of cells lacking *engrailed* is made in the posterior compartment of the wing. Predict its behavior and the effect on the pattern nearby.

   **Answer** The mutant cells adopt anterior identity: they no longer make Hedgehog, they become able to respond to it, and they cross the AP boundary into the anterior compartment or form an ectopic boundary with their posterior neighbors. Where the clone meets posterior *hedgehog*-expressing cells, the clone's cells receive Hedgehog and express *dpp*, creating a new organizer with ectopic anterior structures in mirror image. This is the evidence that *engrailed* is a selector gene.

7. Verify the row "unstable $n$" of Example 33.7.1 for $m=6$, $7$ and $13$, and correct the value $A\theta^{-9}$.

   **Answer** $\theta^{-m}=2^{m/2}$. $m=6$: window $(6.4,9.6)$ contains $n^2=9$, so $n=3$. $m=7$: $(9.05,13.58)$ contains no square ($9<9.05$, $16>13.58$). $m=13$: $2^{6.5}=90.5$, window $(72.4,108.6)$ contains $81$ and $100$, so $n=9,10$. $A\theta^{-9}=0.8\times2^{4.5}=0.8\times22.63=18.10$, not $18.80$ as printed in the source table.

8. Show that the Neumann eigenvalue of the $J_0$ mode of the unit disc is $14.68$ and that its nodal line is a circle of radius $0.63$. Why is this mode excited after the $J_1$ and $J_2$ modes in a growing disc?

   **Answer** $J_0'=-J_1$, whose first positive zero is $3.8317$, so $k^2=14.68$. The nodal circle is at the first zero of $J_0(kr)$: $kr=2.4048$, $r=2.4048/3.8317=0.628$. In a growing disc, $k^2$ in the unit-disc variables passes the eigenvalues in increasing order; $J_1$ ($3.39$) and $J_2$ ($9.33$) have smaller eigenvalues, so they are excited first. The first ring-shaped boundary (a proximo-distal division of the disc) is therefore predicted only third, after two radial ones.

9. In Theorem 33.8.1, take a two-dimensional degenerate space with $c_{111}=c_{122}=0$ (no cubic coupling of $\phi_1$ with itself and with $\phi_2^2$). What can you say about which nodal set is selected? Relate this to a disc whose modes $\cos m\varphi$ and $\sin m\varphi$ are degenerate.

   **Answer** For the angular modes of a disc, $\int\phi_i\phi_j\phi_k$ involves $\int\cos^a m\varphi\sin^b m\varphi\,\mathrm{d}\varphi$ with $a+b=3$, which vanishes, so all $c_{ijk}$ vanish for $m\ne0$ and the quadratic potential gives no selection: any orientation of the nodal diameters is an equilibrium (rotational symmetry). The orientation is then fixed by small asymmetries of the domain (which split the degeneracy, as for the ellipse), by a **prepattern** ([7.5.12](/7.5.12#sec-12.8)) or by cubic terms, and the amplitude by the cubic nonlinearity. Selection by Theorem 33.8.1 requires nonvanishing triple overlaps, as between radial and angular modes.

10. (Experimental design) How would you test, in a modern laboratory, whether the DV compartment boundary of the wing is the nodal line of a reaction–diffusion mode, and what result would falsify the idea?

    **Answer** A nodal line predicts that the boundary position depends on the shape and size of the disc at the time of its formation, that it moves if diffusivities or kinetics are changed, and that no localized selector gene is required. Tests: change disc shape genetically (mutations that alter the aspect ratio) and ask whether the boundary shifts; express *apterous* in clones in the ventral compartment and ask whether new boundaries form around them (they do: a dorsal clone in ventral territory sorts out and induces wg at its edge), and remove *apterous* (the boundary is lost). The dependence of the boundary on a cell-autonomous selector and its formation around clones of arbitrary shape falsify the nodal-line hypothesis for this boundary.
