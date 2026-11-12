---
title: Phyla Ctenophora and Placozoa
description: Comb jellies (Ctenophora) — comb plates and their metachronal waves, the apical organ, colloblasts and tentacles, biradial symmetry, gut and anal pores, determinate development, the nerve net and the question of independent neural origins, the orders and the Mnemiopsis invasion; placozoans (Trichoplax and relatives) — few cell types, no neurons or muscles, gliding, external digestion and peptidergic coordination; what both phyla tell us about early animal evolution.
---

Two small phyla sit near the base of the animal tree and have each, at some point, been proposed as the sister group of all other animals. Comb jellies (Ctenophora) are transparent marine predators, from a few millimetres to over a metre long, that swim with eight rows of fused cilia and catch prey with sticky cells; they have nerves, muscles and a gut with anal pores. Placozoans are flat, crawling discs a few millimetres across, built from only a handful of cell types, with no nerves, muscles or gut. Each phylum challenges a simple story of increasing complexity. If ctenophores are the earliest-branching animals, nerves and muscles either evolved twice or were lost in sponges and placozoans; placozoans, conversely, may be simplified descendants of more complex ancestors.

This chapter describes the body plan, feeding and development of ctenophores (§8.1–8.2), the placozoans (§8.3), and what the two phyla imply for early animal evolution (§8.4). Sponges were treated in [7.17.7](/7.17.7), cnidarians follow in [7.17.9](/7.17.9), and the animal tree as a whole is discussed in [7.17.6](/7.17.6).

## 8.1. Ctenophora: The Body Plan

**Definition 8.1.1 (Ctenophora)** The **Ctenophora** (comb jellies) are marine, mostly planktonic metazoans with biradial symmetry, eight meridional rows of comb plates used for swimming, an aboral apical organ with a statocyst, and (in most species) a pair of retractable tentacles armed with colloblasts; they have a gut with a mouth and anal pores, a nerve net, and muscle cells in a gelatinous mesoglea, but no cnidocytes and no sessile polyp stage.

About 130 valid species are described, roughly 90 planktonic and 40 benthic, and many more probably remain undiscovered in the deep sea, because their delicate bodies fragment in nets. Despite this small number, ctenophores can dominate the plankton biomass of coastal waters.

### 8.1.1. Symmetry and Axes

The main axis runs from the mouth (oral pole) to the apical organ (aboral pole). Two planes of symmetry pass through it: the *tentacular plane*, containing the two tentacles, and the *sagittal* (pharyngeal or stomodeal) *plane*, containing the long axis of the flattened pharynx. The animal is therefore divisible into equal halves along two planes only, the condition called **biradial symmetry**: it is a form of **radial symmetry** with only two planes ([7.17.3](/7.17.3)). Strictly, the two halves are related by a 180° rotation rather than by reflection, because some organs, such as the anal pores, are arranged diagonally (rotational symmetry).

### 8.1.2. Comb Plates and Their Coordination

**Definition 8.1.2 (Comb Plate)** A **comb plate** (ctene) is a transverse row of thousands of long cilia, up to 2 mm long in large species, that are joined together by membrane bridges and beat as a single paddle; the comb plates are arranged one behind another in eight meridional comb rows.

Ctenophores are the largest animals that swim by cilia. Each comb row runs along a meridian from near the apical organ toward the mouth. In normal forward swimming the effective stroke of each plate is directed toward the aboral pole, so the animal moves mouth first. The plates of a row do not beat simultaneously but in sequence. A wave of beating, a *metachronal wave*, starts at the aboral end of the row and travels toward the mouth, opposite to the effective stroke (antiplectic metachronism). The iridescent colours that run along swimming ctenophores are not bioluminescence but diffraction of light by the beating cilia.

The rhythm originates in the apical organ. Four groups of balancer cilia support a statolith of calcareous concretions; each balancer is connected by a ciliated groove to two comb rows. When the animal tilts, the statolith presses harder on the lower balancers, which beat faster and accelerate the comb rows on that side, so the animal rights itself (positive or negative geotaxis). Along the row, each plate is triggered mechanically by the water movement of the plate above it, and the nerve net modulates frequency and can arrest or reverse beating, as when the animal backs away from an obstacle.

A simple model captures the pattern. Let plate $k$ (numbered from the aboral end) have the beat phase

$$
\phi_k(t) = 2\pi f t - k\,\Delta\phi, \tag{8.1}
$$

where $f$ is the beat frequency and $\Delta\phi$ the phase lag between neighbouring plates. Plates with equal phase are $2\pi/\Delta\phi$ plates apart, so the wavelength is $\lambda = 2\pi d/\Delta\phi$ for plate spacing $d$, and the wave travels down the row at speed $c = \lambda f$. In this model the frequency, set by the apical organ, controls swimming speed, while the phase lag, set by the mechanical coupling between plates, controls how the plates share the water, as the second figure below illustrates.

![Body plan of a cydippid ctenophore (*Pleurobrachia*). (A) Side view, oral pole down: the apical organ at the aboral pole; the gut (flattened pharynx, stomach and the meridional canals that run beneath the eight comb rows, which are not drawn here) in the transparent mesoglea; the two long tentacles with side branches (tentilla) emerge from deep tentacle sheaths. (B) Aboral view: biradial symmetry, with the tentacular plane (tentacles in their sheaths) and the perpendicular sagittal plane containing the flattened pharynx (dashed); the statocyst of the apical organ lies at the centre.](./plots/ctenophore-body-plan.py)

![The phase model of metachronal coordination along a comb row (Eq. (8.1)), with frequency $f = 15\,\mathrm{Hz}$ and a phase lag of $\pi/4$ between neighbouring plates. (A) Beat angle of each of 24 plates (aboral end on the left) at three instants a fraction of a cycle apart: the pattern of effective strokes (steep) and recovery strokes moves toward the oral end, so at any moment some plates are in their effective stroke. (B) Space–time plot of the effective strokes (dark): each diagonal band is one metachronal wave travelling from aboral to oral; its slope is the wave speed $c = \lambda f$.](./plots/metachronal-wave.py)

### 8.1.3. Tentacles and Colloblasts

**Definition 8.1.3 (Colloblast)** A **colloblast** (lasso cell) is an adhesive cell of the ctenophore tentacle epidermis: a hemispherical head covered with secretory granules that stick to prey, anchored by a straight central filament and a spiral filament that act as a shock absorber.

Colloblasts are unique to ctenophores. Unlike cnidocytes, they are not fired and do not inject venom; they simply glue the prey, and the spiral filament prevents it from tearing loose. A cydippid fishes by swimming in a circle so that its two tentacles, with their fine side branches (tentilla), trail out in a large net; when prey sticks, the tentacle contracts and wipes the prey across the mouth. Colloblasts are formed continuously from stem cells at the base of the tentacle in the tentacle sheath.

Not all ctenophores use tentacles. Lobate ctenophores such as *Mnemiopsis* capture prey on large oral lobes covered with mucus and on ciliated auricles that create feeding currents. Members of the order Beroida have no tentacles at all: *Beroe* swallows other ctenophores whole through its enormous mouth, which it can seal shut with adhesive strips, and bites pieces off larger prey with macrocilia, stiff bundles of cilia that act as teeth. One cydippid, *Haeckelia*, eats hydromedusae and incorporates their undischarged nematocysts into its own tentacles (kleptocnidae), the only ctenophore with stinging capsules.

### 8.1.4. Gut, Muscles and Nervous System

The mouth leads into a long, flattened pharynx (stomodeum) where extracellular digestion begins, and then into a stomach (infundibulum) from which canals branch to the comb rows, the tentacle bases and the pharynx; digestion is completed intracellularly in the canal walls. From the aboral end of the stomach two canals lead to two anal pores beside the apical organ. In *Mnemiopsis* the anus is transient: it forms only when indigestible material is to be released and then disappears (Tamm 2019). Ctenophores thus have a through-gut, but whether the anal pores are homologous to the anus of bilaterians is doubtful; most authors treat them as independent.

The mesoglea contains true muscle cells. They are individual mesenchymal cells, mostly smooth, extending through the jelly and beneath the epidermis, with striated muscle in the fast tentacles of *Euplokamis*. This is a difference from cnidarians, whose muscles are mostly the contractile bases of epithelial cells.

The nervous system is a subepidermal nerve net, condensed beneath the comb rows and around the mouth, with a further mesogleal net. Some species have giant axons. Ctenophores lack many of the neurotransmitters and neural genes shared by cnidarians and bilaterians (they use peptides and glutamate but not acetylcholine, serotonin or dopamine), and electron tomography of a young *Mnemiopsis* showed that the neurons of the subepidermal net are fused into a continuous syncytium (Burkhardt et al. 2023). These differences prompted the hypothesis that ctenophore neurons evolved independently of those of other animals (Moroz et al. 2014). The hypothesis remains debated; it is discussed in [7.16.53](/7.16.53#sec-53.1.1).

## 8.2. Ctenophora: Reproduction, Development and Diversity

### 8.2.1. Reproduction and Development

Most ctenophores are simultaneous hermaphrodites, and many can fertilize themselves. Gonads develop in the walls of the meridional canals beneath the comb rows, and gametes are usually spawned through the epidermis. Cleavage is biradial and strictly determinate: each blastomere has a fixed fate, and an embryo from which a blastomere is removed lacks the corresponding parts, a classic example of **determinate cleavage** ([7.17.5](/7.17.5)). Gastrulation occurs by epiboly of the micromeres over the macromeres. Lineage tracing shows that the muscle cells in the mesoglea arise from specific endodermal blastomeres (Martindale & Henry 1999), which raised the question of whether ctenophores have a third germ layer. Most biologists regard ctenophores as diploblastic with an endoderm-derived mesenchyme, and they are usually grouped with the **diploblasts**; the mesoderm of bilaterians is probably not homologous.

Development is direct: the young ctenophore, called a *cydippid larva* because it resembles an adult cydippid, has comb rows and tentacles from hatching and grows into the adult without metamorphosis (lobates and beroids develop their adult features gradually). Ctenophores can reproduce as larvae (dissogeny) and regenerate readily. *Mnemiopsis* can even revert from the adult to the cydippid stage under starvation and then regrow, one of the few known cases of reverse development in animals.

### 8.2.2. Diversity

The traditional division into Tentaculata (with tentacles) and Nuda (without, the Beroida) has been abandoned: molecular trees place the tentacle-less beroids within a clade of tentaculate forms. Current classifications use orders only.

| Order | Characteristics | Examples |
|---|---|---|
| Cydippida (not monophyletic) | Rounded or ovoid; two long branched tentacles in deep sheaths | *Pleurobrachia* (sea gooseberry), *Euplokamis*, *Haeckelia* |
| Lobata | Two large oral lobes and four auricles; tentacles reduced | *Mnemiopsis*, *Bolinopsis*, *Leucothea* |
| Cestida | Body ribbon-shaped, up to 1.5 m long; swims by undulation as well as combs | *Cestum* (Venus's girdle), *Velamen* |
| Beroida | No tentacles; large mouth and pharynx; macrocilia | *Beroe* |
| Platyctenida | Benthic, flattened, creeping on the oral surface; comb rows reduced or lost in adults; brood their young | *Coeloplana*, *Vallicula*, *Lyrocteis* |
| Thalassocalycida | Medusa-like, with a wide bell-shaped oral cavity | *Thalassocalyce* |

Platyctenids look like flatworms or nudibranchs; their pelagic young are typical cydippids, which reveals their identity. Cambrian fossils from Chengjiang and the Burgess Shale, some with many more than eight comb rows and some with skeletal plates, together with sessile Cambrian forms interpreted as stem-group ctenophores, suggest that the earliest ctenophores were more diverse and armoured than living ones, and that the soft, planktonic body of modern ctenophores is derived.

### 8.2.3. Ecology: the *Mnemiopsis* Invasion

Ctenophores are voracious predators of zooplankton, fish eggs and larvae, and can grow and reproduce explosively: a *Mnemiopsis leidyi* weighing a few grams can produce thousands of eggs per day. *Mnemiopsis*, native to the western Atlantic, was introduced into the Black Sea in ballast water in the early 1980s. With abundant food and no predators its biomass reached about a billion tonnes by 1989, it consumed the zooplankton and the eggs and larvae of anchovy, and the Black Sea anchovy fishery collapsed. The arrival of another invader, *Beroe ovata*, which feeds almost exclusively on *Mnemiopsis*, in 1997 reduced the *Mnemiopsis* population and allowed a partial recovery of the ecosystem. *Mnemiopsis* has since spread to the Caspian, Baltic and North Seas.

## 8.3. Placozoa

**Definition 8.3.1 (Placozoa)** The **Placozoa** are minute, flat, marine metazoans without symmetry, gut, nervous system or muscles, consisting of a few thousand cells of about six to nine types arranged as a ciliated lower epithelium, a thin upper epithelium and a middle layer of fibre cells; they glide over surfaces by cilia and digest food externally beneath the body.

### 8.3.1. Discovery and Diversity

*Trichoplax adhaerens* was discovered by F. E. Schulze in 1883 on the walls of a seawater aquarium in Graz. For decades it was dismissed as a larva of a cnidarian, until Karl Grell in the 1970s observed oocytes and early embryos, showed that it was an adult animal, and established the phylum Placozoa (1971). Placozoans have been found throughout tropical and subtropical seas, grazing on biofilms. Their genetic diversity is large: although they look alike, they comprise several genera, including *Hoilungia* (described 2018) and *Polyplacotoma* (2019), a species with long, branching extensions.

### 8.3.2. Body Organization

The body is a flat plate, 1–3 mm across and about 20 µm thick, with a permanent upper and lower side but no anterior–posterior axis; the outline changes constantly. Its cell types are:

| Layer | Cell type | Function |
|---|---|---|
| Lower (ventral) | Ventral epithelial cells, columnar, monociliate | Gliding on the substrate |
| | Lipophil cells | Secrete digestive enzymes onto the food |
| | Gland cells | Secrete mucus and peptides; several express neuropeptides |
| Upper (dorsal) | Dorsal epithelial cells, flat, monociliate | Cover the upper surface; contain the "shiny spheres", possibly defensive |
| Middle | Fibre cells | Branched contractile cells; phagocytose debris and bacteria; contain endosymbiotic bacteria |
| Rim | Crystal cells | Contain an aragonite crystal; sense gravity |

The epithelial cells are joined by adherens junctions, but there is no basement membrane and almost no extracellular matrix. Single-cell transcriptomics has revealed more peptidergic cell types than the classical histology (Sebé-Pedrós et al. 2018). The nuclear genome of *Trichoplax* is small, about 98 Mb with some 11,500 genes, yet it contains most of the transcription factor families and signalling pathways of bilaterians, including the ParaHox gene *Trox-2*, many genes for neuronal function, and a full set of the genes for the cell cycle and apoptosis (Srivastava et al. 2008). The animal is simple, but its genome is not.

![Cross-section through the edge of a placozoan (*Trichoplax*), schematic. The lower epithelium of tall monociliate cells (gliding on the substrate) contains lipophil cells, which release digestive enzymes, and gland cells, some of which secrete peptides; the thin upper epithelium has flat monociliate cells with shiny spheres; between the two layers branched fibre cells form a contractile network; crystal cells with an aragonite crystal lie near the rim. Food (algae, bacteria) beneath the body is digested externally in a pocket formed when the animal lifts its centre.](./plots/trichoplax-section.py)

### 8.3.3. Movement, Feeding and Coordination

Placozoans glide on the cilia of the lower epithelium and change shape by contraction of the fibre cells and the epithelia. When the animal comes to rest on a patch of algae it stops its cilia, presses its rim to the substrate to form a temporary pocket, and secretes enzymes from the lipophil cells; the digested material is taken up by the ventral cells. Feeding is thus by external digestion, an analogue of a stomach formed for a few minutes from the body itself.

Without nerves, these behaviours are coordinated by secreted peptides. Gland cells release neuropeptides that stop or start ciliary beating and make the whole animal flatten, crawl or spin; the effects spread through the body by diffusion over a few hundred micrometres (Senatore et al. 2017; Varoqueaux et al. 2018). The ciliated epithelium itself coordinates gliding through mechanical coupling. The physics of this movement without nerves or muscles is described in [7.14.2](/7.14.2#sec-2.8.2).

### 8.3.4. Reproduction

Placozoans reproduce asexually by binary fission and by budding off small "swarmers" from the upper surface. Sexual reproduction has been seen only in the laboratory, where oocytes develop in the middle layer and embryos die at about the 64-cell stage. Population genetic data showing recombination, and the presence of genes for meiosis and sperm, indicate that sex does occur in nature.

## 8.4. What the Two Phyla Tell Us

The three non-bilaterian phyla treated in this chapter and the previous one, together with the Cnidaria, are the outgroups that allow us to reconstruct the earliest animals. Their relationships are summarized below and in [7.17.6](/7.17.6):

| Phylum | Nerves | Muscle cells | Gut | Cell types | Likely position |
|---|---|---|---|---|---|
| Ctenophora | Yes (nerve net, partly syncytial) | Yes (mesenchymal) | Through-gut with anal pores | Many | Sister to all other animals (favoured) |
| Porifera | No | No (contractile pinacocytes, myocytes) | No | ~10–20 | Sister to all animals except ctenophores (or to all animals) |
| Placozoa | No | No | No (external digestion) | ~6–9 | Sister to Cnidaria + Bilateria (ParaHoxozoa), or to Cnidaria |
| Cnidaria | Yes (nerve net) | Epitheliomuscular cells | Gastrovascular cavity | Many | Sister to Bilateria |

Two conclusions follow whatever the exact order of branching. First, simplicity is not a reliable sign of an early origin: placozoans and sponges possess genes for neurons, synapses and complex development, and at least some of their simplicity is secondary. Second, under the ctenophore-first tree, either nerves and muscles evolved twice (once in ctenophores and once in the ancestor of cnidarians and bilaterians) or they were lost in both sponges and placozoans. The unusual neurochemistry of ctenophores, the syncytial nerve net and the mesenchymal origin of their muscles are consistent with independent origins, but convergent use of a shared ancestral toolkit of secretory cells is equally possible. These two phyla therefore show that the first animals may have been more complex than either.

## Summary

- Ctenophores (Definition 8.1.1) are biradial marine predators with eight rows of comb plates (Definition 8.1.2), an aboral apical organ with a statolith, colloblast-bearing tentacles (Definition 8.1.3), a gut with anal pores, mesenchymal muscle cells and a nerve net; they lack cnidocytes and a polyp stage.
- Comb plates beat in metachronal waves running from aboral to oral, opposite to the effective stroke; in the phase model (Eq. (8.1)) the apical organ sets the frequency and mechanical coupling the phase lag. The statolith on four balancers provides geotaxis.
- Feeding modes: tentacle nets (cydippids), mucous lobes (lobates), engulfing other ctenophores with macrocilia (*Beroe*); *Haeckelia* steals nematocysts.
- Development is biradial, determinate and direct (cydippid larva); muscles derive from endodermal lineages. Six orders; Nuda and Tentaculata abandoned. *Mnemiopsis* in the Black Sea is a textbook marine invasion, controlled by *Beroe ovata*.
- Placozoans (Definition 8.3.1) are flat discs with six to nine cell types, no nerves, muscles, gut or basement membrane; they glide by cilia, digest food externally under the body and coordinate behaviour with secreted peptides. Their small genome contains most bilaterian gene families.
- Ctenophores probably branched first, placozoans are close to cnidarians and bilaterians; the simplicity of sponges and placozoans is at least partly secondary, and nerves may have evolved twice.

## Questions

1. Ctenophores and cnidarians were once united as "Coelenterata". List the main differences between the two groups and explain why they are now placed in separate phyla.

   **Answer** Ctenophores have comb rows and an apical organ (cnidarians have neither), colloblasts instead of cnidocytes, mesenchymal muscle cells rather than epitheliomuscular cells, anal pores, determinate biradial cleavage, direct development without a polyp, and no alternation of polyp and medusa. Molecular phylogenies do not group them: ctenophores branch off at or near the base of the animal tree, whereas cnidarians are the sister group of bilaterians. The shared jelly-like body with a gastrovascular cavity is a grade, not a clade.
2. A comb row of a ctenophore has plates spaced $d = 0.3\,\mathrm{mm}$ apart, beating at $f = 15\,\mathrm{Hz}$ with a phase lag of $\Delta\phi = 0.4\,\mathrm{rad}$ between neighbours. What are the metachronal wavelength and wave speed? What would happen to swimming if all plates beat in phase?

   **Answer** $\lambda = 2\pi d/\Delta\phi = 2\pi \times 0.3/0.4 \approx 4.7\,\mathrm{mm}$ and $c = \lambda f \approx 71\,\mathrm{mm\,s^{-1}}$. If all plates beat in phase, the whole row would push and recover simultaneously, so the animal would surge and then be pulled back during the recovery strokes; staggered beating keeps some plates in their effective stroke at every moment, giving smoother thrust, and neighbouring plates interact hydrodynamically so that each recovers in the wake of the next.
3. *Trichoplax* has no gut. How does it digest its food, and in what sense is this comparable to the gastrovascular cavity of a cnidarian?

   **Answer** It lifts its centre while keeping its rim on the substrate, enclosing algae in a temporary pocket beneath the lower epithelium. Lipophil cells secrete digestive enzymes into the pocket and ventral epithelial cells absorb the products. Like a cnidarian gastrovascular cavity, this creates an enclosed space where extracellular digestion can take place, but the pocket is transient and formed by the whole lower surface rather than a permanent internal cavity lined by endoderm; it illustrates a plausible functional step toward a gut, not a homologous structure.
4. Under the hypothesis that ctenophores are the sister group of all other animals, what are the two alternative explanations for the distribution of neurons among non-bilaterians? What evidence would help decide between them?

   **Answer** Either neurons were present in the last common ancestor of animals and were lost in sponges and placozoans, or they evolved twice, once in ctenophores and once in the ancestor of cnidarians and bilaterians. Evidence for loss would be vestiges of neuronal cell types in sponges and placozoans with gene-regulatory programs homologous to those of neurons; evidence for independent origin would be differences in the core machinery (transmitters, synaptic proteins, developmental regulators) and in the developmental origin of ctenophore neurons. The neuroid cells of sponges, the peptidergic cells of placozoans and the syncytial, transmitter-poor nerve net of ctenophores currently fit both scenarios.
