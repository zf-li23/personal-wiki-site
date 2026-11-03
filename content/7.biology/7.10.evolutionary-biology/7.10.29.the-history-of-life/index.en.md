---
title: "The History of Life: Geological Time and the Fossil Record"
description: "Geological fundamentals (rock types, plate tectonics, stratigraphy), radiometric dating and the geologic time scale of the International Commission on Stratigraphy; fossils, their kinds and preservation, exceptional deposits and the incompleteness of the record; the history of atmospheric oxygen; the Proterozoic and the Ediacaran biota; the Cambrian explosion and the conundrum of its timing; the Paleozoic radiation, the colonization of land by plants, arthropods and tetrapods, and the end-Permian extinction; the Mesozoic world of dinosaurs, early mammals and flowering plants, and the K/Pg impact; the Cenozoic radiation of mammals and birds, the Pleistocene glaciations and the megafaunal extinctions."
---

Phylogenies of living organisms tell us in what order lineages branched; only fossils tell us when, in what environments and with what extinct companions. Fossils record creatures that left no living descendants, episodes of extinction and radiation, and the movements of continents that explain present distributions; they provide the calibrations without which the molecular clock has no absolute time scale ([7.10.24](/7.10.24)), and they reveal combinations of characters, such as the feathered dinosaurs and the fish with limbs, that no living organism shows. This chapter tells the history of multicellular life from the late Proterozoic to the present, after the geological and taphonomic background needed to read the record.

The earlier history, from the origin of life to the first eukaryotes, is in [7.10.27](/7.10.27) and [7.10.28](/7.10.28). The statistical analysis of diversity through time, origination and extinction rates and mass extinctions is in [7.10.31](/7.10.31), the biogeographic consequences of continental drift in [7.10.30](/7.10.30), and the origin of major new forms (mammals, birds, the eye), rates of evolution and trends in [7.10.32](/7.10.32). The detailed phylogeny of plants and animals belongs to botany and zoology; here we follow only the major events. Like Futuyma and Kirkpatrick, we note that this chapter is largely factual; its dates are those of the International Chronostratigraphic Chart (ICS, version 2024/12), which differ by a few million years from those of older textbooks (for example 538.8 rather than 541 or 542 Mya for the base of the Cambrian).

## 29.1. Reading the Rocks

### 29.1.1. Rocks, Plates and Strata

Igneous rocks form from molten magma, extruded by volcanoes or at mid-ocean ridges where new oceanic crust is made. Sedimentary rocks form from deposited and consolidated sediments, produced by the breakdown of older rocks or by precipitation from water. Heat and pressure transform both into metamorphic rocks. Most fossils are found in sedimentary rocks; a few are preserved in amber (fossil resin), in permafrost or in tar.

The lithosphere, the rigid outer layer bearing the continents and the ocean floor, consists of about eight major plates and several minor ones that move over the hotter, more plastic asthenosphere at a few centimeters per year, driven by convection in the mantle. At mid-ocean ridges new crust pushes plates apart; where plates converge, one plunges beneath the other (subduction), causing earthquakes, volcanism and mountain building; where a plate moves over a hot spot, chains of volcanic islands such as Hawaii form. Because oceanic crust is recycled at subduction zones, none older than about 180 million years remains on the ocean floor: older marine rocks survive only where they were deposited on continents or thrust onto them.

Long before radiometric dating, geologists established relative ages with the principle of superposition, that younger sediments are laid on older ones, and matched contemporaneous layers (strata) in different places by their distinctive fossils. Most of the periods of the geological time scale were named in the first half of the nineteenth century in this way, by their fossils, and are still most easily recognized by them.

### 29.1.2. Radiometric Dating

Absolute ages come from radioactive decay ([7.10.27](/7.10.27#sec-27.1)). The probability that an unstable parent nucleus decays into a stable daughter per unit time is constant, independent of temperature and chemistry, which makes the number of parent atoms an exponential clock (a first-order process, **half-life** in [6.1.7](/6.1.7)).

**Formula 29.1.1 (Radiometric Age)** Let a mineral contain, at its formation, $N_0$ atoms of a radioactive parent with decay constant $\lambda$ (half-life $t_{1/2} = \ln 2/\lambda$) and no daughter atoms produced by its decay. After time $t$ it contains $N = N_0\mathrm{e}^{-\lambda t}$ parent and $D = N_0 - N$ daughter atoms, and

$$
t = \frac{1}{\lambda}\ln\Bigl(1 + \frac{D}{N}\Bigr) = \frac{t_{1/2}}{\ln 2}\ln\Bigl(1 + \frac{D}{N}\Bigr).
$$

**Proof** Decay at a constant rate per atom, $\mathrm{d}N/\mathrm{d}t = -\lambda N$, gives $N = N_0\mathrm{e}^{-\lambda t}$. Since every decayed parent becomes a daughter, $D = N_0(1 - \mathrm{e}^{-\lambda t})$, so $D/N = \mathrm{e}^{\lambda t} - 1$; solving for $t$ gives the formula. $\square$

After one half-life the ratio of parent to daughter is $1:1$, after two $1:3$, after three $1:7$. Several systems are used, each suited to a range of ages: uranium-238 to lead-206 (half-life $4.47 \times 10^9$ years) and uranium-235 to lead-207 ($7.04 \times 10^8$ years), measured together in zircon crystals, which exclude lead when they crystallize and so give two independent clocks that check each other; potassium-40 to argon-40 ($1.25 \times 10^9$ years) in volcanic rocks; and carbon-14, made in the atmosphere by cosmic rays ($5730$ years), which dates organic remains younger than about 50 000 years by comparison with the initial $^{14}\mathrm{C}/^{12}\mathrm{C}$ ratio of living carbon. Complications, such as daughter atoms present initially or atoms gained or lost later, are handled by isochrons and by concordance between systems. Only igneous minerals (and some volcanic ash beds) can be dated in this way, so the age of a fossil-bearing sedimentary layer is usually bracketed by datable volcanic layers above and below it.

![Radiometric dating (Formula 29.1.1). A: fractions of parent (blue) and daughter atoms (orange) against time in half-lives: the parent halves in each half-life and the daughter-to-parent ratio D/N rises as 1, 3, 7, 15. B: age as a function of the measured ratio D/N for three systems with very different half-lives, ¹⁴C (5730 years), ⁴⁰K→⁴⁰Ar (1.25 Gyr; only 10.7 % of ⁴⁰K decays yield argon, which the curve takes into account) and ²³⁸U→²⁰⁶Pb (4.47 Gyr), on logarithmic axes: each system resolves ages from a small fraction of its half-life to a few half-lives.](./plots/radiometric.py)

### 29.1.3. The Geologic Time Scale

**Definition 29.1.1 (Geologic Time Scale)** The **geologic time scale** is the hierarchical division of Earth history into eons, eras, periods, epochs and ages, defined by the rock record (chronostratigraphic units whose lower boundaries are fixed at reference sections, mostly by first appearances of fossil species) and calibrated in years by radiometric dating; the international standard is maintained by the International Commission on Stratigraphy.

The Hadean (4567–4031 Mya), Archean (4031–2500 Mya) and Proterozoic (2500–538.8 Mya) eons together are informally called the Precambrian, nearly 90 % of Earth history. The Phanerozoic eon ("visible life", 538.8 Mya to the present) is divided into three eras, separated by the two largest mass extinctions: the Paleozoic ("ancient life"), the Mesozoic ("middle life", from 251.9 Mya) and the Cenozoic ("recent life", from 66.0 Mya).

| Era | Period | Base (Mya) | Major events |
|---|---|---|---|
| Neoproterozoic | Cryogenian | 720 | global glaciations ("Snowball Earth"); animal lineages inferred from DNA |
| | Ediacaran | 635 | Ediacaran biota (from about 575 Mya); first sponges and cnidarians |
| Paleozoic | Cambrian | 538.8 | Cambrian explosion; most animal phyla; earliest vertebrates |
| | Ordovician | 486.85 | great diversification of marine invertebrates; first land plants (spores); end-Ordovician mass extinction |
| | Silurian | 443.1 | jawed fishes; vascular plants and arthropods on land |
| | Devonian | 419.62 | "age of fishes"; forests; first tetrapods and insects; late Devonian extinctions |
| | Carboniferous | 358.86 | coal swamps of lycophytes and ferns; winged insects; first amniotes |
| | Permian | 298.9 | Pangaea; synapsids diversify; end-Permian mass extinction |
| Mesozoic | Triassic | 251.902 | recovery; first dinosaurs, mammaliaforms and pterosaurs; end-Triassic extinction |
| | Jurassic | 201.4 | dinosaurs dominant; first birds; Pangaea breaks up |
| | Cretaceous | 143.1 | angiosperms radiate; K/Pg impact and mass extinction at its end |
| Cenozoic | Paleogene | 66.0 | radiation of mammals and birds; cooling from the Eocene, Antarctic ice |
| | Neogene | 23.04 | grasslands spread; apes, first hominins |
| | Quaternary | 2.58 | glacial–interglacial cycles; *Homo sapiens*; megafaunal extinctions |

The Cenozoic is further divided into the epochs Paleocene, Eocene, Oligocene, Miocene, Pliocene, Pleistocene and Holocene (from 11 700 years ago); older literature calls the first five the Tertiary.

![The geologic time scale (International Chronostratigraphic Chart v2024/12, ICS colors). Top: the whole of Earth history by eons and eras, on a linear scale in millions of years; the Phanerozoic is the last eighth. Bottom: the Phanerozoic and the end of the Proterozoic by eras and periods, with the five largest mass extinctions (red triangles: end-Ordovician, late Devonian, end-Permian, end-Triassic, end-Cretaceous) and some major first appearances.](./plots/timescale.py)

## 29.2. Fossils and Their Biases

**Definition 29.2.1 (Fossil)** A **fossil** is any preserved evidence of an organism that lived in the geological past: body fossils (parts of the organism or their mineral replacements, molds and casts), trace fossils (tracks, burrows, borings, coprolites and other records of behavior) and chemical fossils (molecules or isotopic signatures characteristic of organisms).

Body fossils are preserved in several ways: as unaltered hard parts (shells, bones, teeth, wood); by permineralization, in which minerals fill pores and cells; by replacement of the original material by another mineral; as molds, impressions of the organism in sediment, and casts, molds later filled with sediment; as compressions of carbon films, especially of plants; and, rarely, as soft tissues in amber or permafrost. A few fossil species that were widespread, abundant and short-lived serve as *index fossils* for correlating strata (ammonites, graptolites, planktonic foraminifera, conodonts); others, restricted to particular environments, are *facies fossils* that indicate the conditions of deposition (reef corals, freshwater fishes).

The chance that an organism becomes a fossil is very small. It must escape scavengers and decay, which means rapid burial in sediment, usually under water; the rock must then survive compaction, heating, uplift, erosion and subduction for millions of years and finally be exposed and found. Taphonomy, the study of how organisms decay and become fossils, explains the biases that result:

- organisms with mineralized skeletons are far better represented than soft-bodied ones;
- marine organisms are better represented than terrestrial ones, and inhabitants of lakes and rivers better than those of dry land or of humid forests where decay is fast: about 95 % of described fossils are marine, while about 85 % of living described species are terrestrial;
- older intervals are less well represented, because more of their rocks have been destroyed;
- sedimentation is episodic, so any local sequence contains only a fraction of the time and of the species of a region, and a species that evolved elsewhere may appear in a local record fully formed.

About 250 000 fossil species have been described, a small percentage of those that have lived. Yet for some questions the record is adequate: the order in which groups first appear in the fossil record agrees well with their order of branching in phylogenies at the level of families, which suggests that family-level data are a reasonable guide to the major events. The statistical consequences, such as the "pull of the Recent", are treated in [7.10.31](/7.10.31#sec-31.1.2).

Exceptional deposits (Konservat-Lagerstätten) in which soft tissues are preserved, usually by rapid burial in fine sediment without oxygen and early mineralization, open windows on whole communities:

| Deposit | Age | What it preserves |
|---|---|---|
| Doushantuo Formation, Guizhou, China | about 600 Mya | phosphatized algae and cleaving embryos, possibly of animals |
| Mistaken Point, Newfoundland | about 565 Mya | Ediacaran fronds (*Charniodiscus*) and other rangeomorphs in deep water |
| Chengjiang, Yunnan, China | about 518 Mya | early Cambrian arthropods, lobopodians and the earliest vertebrates |
| Burgess Shale, British Columbia | about 508 Mya | middle Cambrian community: *Marrella*, *Opabinia*, *Anomalocaris*, *Hallucigenia*, *Pikaia* |
| Rhynie Chert, Scotland | about 407 Mya | early land plants, fungi and arthropods preserved by silica in hot springs |
| Solnhofen Limestone, Bavaria | about 150 Mya | *Archaeopteryx*, pterosaurs, insects in a lagoon |
| Jehol Biota, Liaoning, China | about 125 Mya | feathered dinosaurs, early birds and mammals, early angiosperms |
| Messel Pit, Germany | about 47 Mya | Eocene mammals with fur and stomach contents, bats, birds |

In the Burgess Shale, of more than 65 000 specimens surveyed, about 86 % of the genera and 98 % of the individuals would not have been preserved in an ordinary deposit with only hard parts: an indication of how much the rest of the record leaves out.

## 29.3. The Proterozoic World

### 29.3.1. The History of Atmospheric Oxygen

The atmosphere was without free oxygen for the first half of Earth history. The **Great Oxidation Event** about 2.4–2.3 Ga ([Definition 27.5.1](/7.10.27#def-27.5.1)) raised oxygen to a level that stayed, through most of the Proterozoic, far below the present 21 %, with deep oceans that remained largely anoxic and often rich in iron or sulfide. A second rise in the late Neoproterozoic and early Paleozoic, the Neoproterozoic oxygenation, brought oxygen in the atmosphere and the deep ocean closer to modern levels; its timing and magnitude are debated, and several pulses may have occurred. Oxygen continued to rise in the Devonian, when the spread of forests increased the burial of organic carbon, and in the Carboniferous it may have exceeded present levels, which is one explanation proposed for the giant insects of that period. The levels before the Phanerozoic are uncertain by orders of magnitude, but the stepwise pattern is well supported.

![The rise of atmospheric oxygen (schematic; after the reviews of Lyons and colleagues 2014 and others). The shaded band shows the qualitative history of the partial pressure of oxygen relative to the present atmospheric level (PAL) on a logarithmic scale: trace levels in the Archean (below about one hundred-thousandth of PAL); the Great Oxidation Event about 2.4–2.3 Ga; low Proterozoic levels, possibly between a thousandth and a tenth of PAL; the Neoproterozoic oxygenation; near-modern Phanerozoic levels. The width of the band expresses uncertainty; the precise curve is not known. Events in the history of life are marked below the axis.](./plots/oxygen.py)

The Proterozoic saw the diversification of eukaryotes ([7.10.28](/7.10.28)), with red and green algae by about 1 Ga. In the Cryogenian (720–635 Mya), the Earth underwent at least two glaciations so extensive that ice sheets reached the tropics at sea level ("Snowball Earth"). Molecular clocks place the origin of animals in or before this period, more than 700 Mya for the divergence of sponges from other animals; molecular fossils of sponge-specific steroids have been reported from rocks older than 635 Mya, but their interpretation is disputed.

### 29.3.2. The Ediacaran Biota

**Definition 29.3.1 (Ediacaran Biota)** The **Ediacaran biota** is the assemblage of large, mostly soft-bodied multicellular organisms known from impressions in rocks of the late Ediacaran period, about 575 to 539 Mya, first described from the Ediacara Hills of South Australia.

Ediacaran fossils are known from about 30 localities on all continents but Antarctica, notably Newfoundland, South Australia, the White Sea coast of Russia and Namibia. They range from millimeters to more than a meter and include fronds (rangeomorphs such as *Charniodiscus*, with a fractal branching pattern), discs, quilted flat forms such as *Dickinsonia*, and the triradial *Tribrachidium*, whose symmetry is unlike that of any later animal. They lacked hard parts, mouthparts and locomotory appendages, and many were preserved as casts on the undersides of sandstone beds, possibly because microbial mats covering the sea floor, undisturbed by grazers and burrowers, mineralized quickly around them ("death masks").

What these organisms were is still debated. Adolf Seilacher proposed that many of them were "vendobionts", a separate, failed experiment in multicellular organization that absorbed nutrients through its surface. Others have been identified as animals: *Dickinsonia* contains cholesterol derivatives characteristic of animals, *Kimberella* is associated with radiating scratch marks that suggest grazing with a mollusc-like feeding organ, and simple horizontal trace fossils of mobile bilaterians appear in the late Ediacaran. Most Ediacaran forms disappeared at or before the base of the Cambrian. The first small skeletal animals, the tubular *Cloudina*, some of whose shells were bored by predators, and the cup-shaped *Namacalathus*, appear at the very end of the Ediacaran, about 550 Mya.

## 29.4. The Cambrian Explosion

**Definition 29.4.1 (Cambrian Explosion)** The **Cambrian explosion** is the rapid appearance in the fossil record, within some 20–25 million years of the early Cambrian (about 539–515 Mya), of most animal phyla and many of their classes, of mineralized skeletons in many lineages, and of a great increase in the size, abundance and diversity of animal body and trace fossils.

For the first ten million years or so of the Cambrian, animal fossils are small and of low diversity (the "small shelly fauna"); then, within about 20 million years, arthropods (trilobites among them), molluscs, brachiopods, echinoderms, sponges, chordates and many forms hard to assign to living phyla appear, followed in the Chengjiang and Burgess Shale deposits by a diverse soft-bodied fauna. Burrows deepen and become complex, and predators appear, among them the large anomalocaridids. The earliest vertebrates, such as *Haikouichthys* from Chengjiang, already had eyes, a notochord and segmented musculature. The term "explosion" is relative: the event spanned tens of millions of years, but it was by far the most dramatic **adaptive radiation** in the history of animals.

It is also a conundrum. Molecular clocks calibrated with many fossils place the divergences among animal phyla well before the Cambrian, by 100 million years or more, yet apart from sponges no living phylum is known with certainty before it. Several explanations, not exclusive, are offered:

- *Preservation.* Precambrian bilaterians were probably small, soft-bodied and living in or on microbial mats, leaving few fossils. The simultaneous appearance of skeletons in many lineages made animals visible, an ecological rather than a phylogenetic event.
- *Environment.* Rising oxygen may have permitted larger bodies, active locomotion and predation; changes in ocean chemistry may have favored biomineralization.
- *Ecology.* Predation and burrowing created selection for armor, eyes and speed and opened new niches, each innovation creating opportunities for others, an ecological feedback that would accelerate diversification.
- *Development.* The genetic toolkit of animal development, including the Hox genes and the major signaling pathways, was already present ([7.5.39](/7.5.39), [7.10.19](/7.10.19)), so that new body plans could be built by changes in regulation.

The molecular clock estimates themselves have narrowed as models and calibrations improved, but a gap between the divergence of lineages and their appearance as recognizable fossils remains ([7.10.24](/7.10.24)). Stephen Jay Gould argued that the Burgess fauna had a greater morphological disparity than any later fauna; later quantitative analyses of arthropods and priapulids found Cambrian disparity similar to that of their living relatives, and many of Gould's "weird wonders" have since been placed in the stem groups of living phyla (**stem group**, [7.10.2](/7.10.2)): *Anomalocaris* and *Opabinia* near the arthropods, *Hallucigenia* among the lobopodians, the relatives of velvet worms.

## 29.5. The Paleozoic

### 29.5.1. Life in the Sea

Many groups that appeared in the Cambrian diversified greatly in the Ordovician (486.85–443.1 Mya), the "Great Ordovician Biodiversification Event", which tripled the number of marine families. Reefs were built by corals, sponges and bryozoans; the largest predators were nautiloid cephalopods and eurypterids (sea scorpions). The Ordovician ended with the first of the five largest mass extinctions, associated with a brief glaciation and fall of sea level. Ammonoids evolved from nautiloids in the Devonian and became among the most diverse of all extinct animal groups. Jawless, armored fishes (ostracoderms) were common in the Silurian; jawed fishes (gnathostomes) appeared in the Silurian, and in the Devonian (419.62–358.86 Mya), the "age of fishes", the placoderms, sharks, ray-finned fishes and lobe-finned fishes (Sarcopterygii, including lungfishes, coelacanths and the ancestors of tetrapods) flourished. Huge reefs of the Silurian and Devonian disappeared in the late Devonian extinctions.

### 29.5.2. The Colonization of Land

Life on land required solutions to desiccation, support, gas exchange and reproduction away from water. Microbial crusts probably covered moist land surfaces long before plants. Land plants, a clade derived from charophyte green algae, appear first as spores and spore-bearing structures of the mid-Ordovician, apparently related to liverworts; small vascular plants without true roots or leaves, such as *Cooksonia*, a few centimeters tall with sporangia at the tips of branching stems, appear in the Silurian. The Rhynie Chert of the early Devonian preserves such plants down to their cells, together with fungi, lichens and arthropods. Within the Devonian, plants evolved roots, wood, leaves and seeds, and by its end there were forests of trees; this increase of terrestrial biomass increased atmospheric oxygen, created soils, accelerated weathering and lowered atmospheric carbon dioxide and temperature.

Arthropods came ashore in two groups, both of marine origin. Trackways of a large arthropod in late Cambrian–early Ordovician dune sands of Ontario suggest early excursions; the oldest definitely terrestrial, air-breathing animal is the millipede *Pneumodesmus newmani* from the Silurian of Scotland, with spiracles. Chelicerates (scorpions, arachnids, mites) and myriapods were followed in the Devonian by the first hexapods, such as the springtail *Rhyniella* from the Rhynie Chert. Insects evolved from crustaceans; winged insects appear in the fossil record in the Carboniferous and diversified rapidly, some to giant size (*Meganeura*, a relative of dragonflies with a wingspan of about 70 cm; the millipede *Arthropleura*, about 2 m long). Insects with complete metamorphosis appear in the late Carboniferous; beetles are known from the early Permian, and hymenopterans and true flies from the Triassic.

Tetrapods evolved from lobe-finned fishes in the late Devonian, and most of their characteristic features evolved in shallow water before they walked on land. The intermediate forms *Panderichthys*, *Tiktaalik roseae* (found in 2004 in northern Canada, about 375 Mya), *Ventastega*, *Acanthostega* and *Ichthyostega* show the sequence of changes, from fins to limbs with digits, and the early limbs had more than five digits: eight in *Acanthostega*, seven in *Ichthyostega* ([7.10.1](/7.10.1), [7.10.32](/7.10.32)). After a gap in the record in the early Carboniferous, diverse tetrapods appear, among them the first amniotes, whose shelled egg freed reproduction from water; by the late Carboniferous the amniotes had split into the synapsids, the lineage leading to mammals, and the reptiles (sauropsids), including the diapsids.

### 29.5.3. Pangaea and the End-Permian Extinction

**Definition 29.5.1 (Pangaea, Gondwana and Laurasia)** **Pangaea** was the supercontinent that united nearly all continental crust from the late Paleozoic to the early Mesozoic (about 335–175 Mya). Its southern part, **Gondwana** (South America, Africa, Madagascar, India, Antarctica and Australia), had existed as a supercontinent since the late Neoproterozoic; its northern part, **Laurasia** (North America, Europe and most of Asia), formed when Pangaea split in the Jurassic.

The idea that continents had once been joined was proposed by Alfred Wegener in the early twentieth century from the fit of coastlines and the similarity of fossils on either side of the Atlantic; it was accepted only in the 1960s, when seafloor spreading and plate tectonics provided a mechanism. In the Carboniferous, extensive tropical swamp forests of lycophyte trees up to 30 m tall, horsetails, tree ferns and seed ferns grew over the continents that were assembling into Pangaea, and their remains form the coal beds of Europe and North America. In the Permian (298.9–251.902 Mya), the assembly of Pangaea built mountain ranges such as the Appalachians and Urals, lowered sea level and made the continental interior arid.

The Permian ended with the greatest mass extinction of all time, in which more than 80 % of the species of marine animals with skeletons became extinct in less than 200 000 years ([Definition 31.4.1](/7.10.31#def-31.4.1), [7.10.31](/7.10.31#sec-31.4.1)). Trilobites, rugose and tabulate corals and many other groups disappeared, brachiopods and crinoids were decimated, and on land many tetrapods, insects and plant communities were affected. The trigger was most probably the eruption of the Siberian Traps, flood basalts covering millions of square kilometers, whose carbon dioxide and other gases caused global warming, ocean acidification and widespread anoxia.

## 29.6. The Mesozoic

During the Mesozoic (251.902–66.0 Mya), Pangaea broke up: the Tethys Sea opened between the north and the south, Laurasia separated from Gondwana, and Gondwana itself fragmented in the Jurassic and Cretaceous, the South Atlantic opening as a narrow seaway. Sea level was high, much of the continents was covered by shallow seas, and the climate was warm: forests grew near the poles, and temperatures peaked in the mid-Cretaceous.

In the sea, marine life recovered slowly from the end-Permian extinction (ammonoids, for example, rose from two to more than a hundred genera by the middle Triassic), was struck again by the end-Triassic extinction, and then radiated again. Modern corals, planktonic foraminifera and the teleost fishes appeared. During the Mesozoic marine revolution, predators that crush or drill shells (crabs, teleosts, predatory snails) diversified, and molluscs evolved thicker shells, spines and narrow apertures in response. Marine reptiles such as the ichthyosaurs, convergent in form with dolphins, and plesiosaurs were the largest predators.

On land, gymnosperms (cycads, conifers, ginkgos) dominated the flora for most of the Mesozoic. The flowering plants (angiosperms) appear in the fossil record in the early Cretaceous, about 130 Mya, and by the mid-Cretaceous, about 100 Mya, many forests were dominated by them; their diversification was accompanied by that of insects, among them pollinators, and of many other groups that live on or among them ([7.10.17](/7.10.17)). The archosaurs radiated: pterosaurs, the first vertebrates with powered flight (the largest with wingspans of about 11 m), crocodylomorphs, and the dinosaurs, which appeared in the late Triassic, about 230 Mya, and became the dominant large land animals of the Jurassic and Cretaceous. Birds are one lineage of theropod dinosaurs: *Archaeopteryx*, about 150 Mya, combines feathers and wings with teeth, a long bony tail and clawed fingers, and the many feathered dinosaurs found in China since the 1990s show that feathers evolved long before flight ([7.10.32](/7.10.32)). Synapsids gave rise in the late Triassic to mammaliaforms; many lineages of Mesozoic mammals, mostly small but ecologically diverse (swimmers, diggers, gliders), have no living descendants, and only three survive: the monotremes, marsupials and placentals.

The Mesozoic ended 66.0 Mya with the K/Pg (Cretaceous–Paleogene, formerly K/T) mass extinction. In 1980 Luis and Walter Alvarez and colleagues reported a clay layer at the boundary, first studied at Gubbio, Italy, enriched in iridium, an element rare in the crust but common in meteorites; the Chicxulub crater, about 180 km across, buried under the Yucatán Peninsula, was identified as the impact site in 1991. The impact, which coincided with the eruptions of the Deccan Traps in India, extinguished the nonavian dinosaurs, pterosaurs, ammonites, most marine reptiles and many groups of plankton, mammals, birds and plants ([7.10.31](/7.10.31#sec-31.4.2)).

## 29.7. The Cenozoic

### 29.7.1. The Modern World Takes Shape

In the Cenozoic the continents moved toward their present positions. Australia separated from Antarctica in the Eocene; India collided with Asia, raising the Himalayas; Africa met southwestern Asia in the Miocene; and the Isthmus of Panama joined North and South America about 2.8 Mya, allowing the exchange of mammals between them, in which many South American groups became extinct ([7.10.30](/7.10.30)). The climate cooled from a warm maximum in the early Eocene, with glaciers forming on Antarctica at the Eocene–Oligocene boundary; grasslands and savannas spread in the Oligocene and Miocene as the climate became drier, and grasses (Poaceae) and daisies (Asteraceae) radiated.

Birds and mammals diversified rapidly after the K/Pg extinction. Most orders of living birds appear in the Paleocene and Eocene, and the songbirds, half of all living birds, radiated in the Miocene. Molecular phylogenies calibrated with many fossils show that the stem lineages of many orders of placental mammals had already diverged in the Cretaceous, more than 80 Mya, while most fossils that belong to modern orders appear after the K/Pg boundary; the end of the dinosaurs is thought to have opened ecological opportunities for an adaptive radiation of mammals in body size and ways of life, although the relative contributions of earlier divergence and later radiation are still debated. Whales evolved in the Eocene from artiodactyls related to hippopotamuses; ruminants radiated in the Miocene with the spread of grasslands; elephants and their relatives, horses and rhinoceroses were more diverse in the past than now. South America, isolated through most of the Cenozoic, had its own radiations of marsupials, xenarthrans (ground sloths, glyptodonts) and several extinct orders of hoofed mammals. Monkeys appear in the Oligocene, apes in the Miocene, and the earliest hominins about 7 Mya ([7.10.33](/7.10.33)).

### 29.7.2. The Pleistocene

From about 2.6 Mya, at the beginning of the Quaternary, the Earth entered a period of repeated glacial and interglacial cycles, paced by periodic changes in the Earth's orbit: about every 41 000 years at first and about every 100 000 years for the last million years. At glacial maxima, ice sheets up to 2 km thick covered northern North America and Europe, sea level fell by more than 100 m, exposing continental shelves and connecting Asia with North America across the Bering Land Bridge and many islands with the continents. The last glacial maximum was about 20 000 years ago, and the ice retreated between about 15 000 and 8000 years ago.

The ranges of species shifted repeatedly toward the equator and back. Many species survived glacial periods in isolated refugia, where some diverged, and recolonized their present ranges only in the last few thousand years ([7.10.30](/7.10.30#sec-30.5)); fossil pollen shows that communities were reshuffled as species moved independently. At the end of the Pleistocene and in the Holocene, a large fraction of the large mammals and birds disappeared everywhere except in Africa: mammoths, mastodons, giant ground sloths, saber-toothed cats, giant beavers, the endemic hoofed mammals of South America, the moas of New Zealand. The timing of extinctions relative to the arrival of humans on each continent and island, and to climate change, together with population models, indicates that both human hunting and climate contributed, with humans playing the larger role on islands and on continents colonized late.

The spread of agriculture after about 11 000 years ago began another reshaping of terrestrial environments, and the current rates of extinction caused by habitat destruction, overexploitation, introduced species and climate change are far above background rates ([7.10.34](/7.10.34)). Whether the present should be recognized as a new epoch, the Anthropocene, was debated for more than a decade; in 2024 the proposal to add it to the time scale was rejected, but the scale of human influence on the biosphere is not in dispute.

![First appearances of some major groups in the fossil record, on the ICS periods of the Phanerozoic (bars run from the first fossils to the present or to extinction; dates approximate, from the text). Marine animals: trilobites (Cambrian to end-Permian), vertebrates (early Cambrian), jawed fishes (Silurian). Land: vascular plants (Silurian), insects (Devonian), tetrapods (late Devonian), amniotes (Carboniferous), dinosaurs (late Triassic; nonavian dinosaurs to the end of the Cretaceous), mammaliaforms (late Triassic), birds (late Jurassic), angiosperms (early Cretaceous), grasslands (Oligocene–Miocene), hominins (late Miocene). Red triangles: the five largest mass extinctions.](./plots/first-appearances.py)

## Summary

| Interval | Main events |
|---|---|
| Methods | strata and superposition; **radiometric dating** (Formula 29.1.1: $t = \lambda^{-1}\ln(1 + D/N)$); **geologic time scale** (Definition 29.1.1) of the ICS |
| Fossil record | **fossils** (Definition 29.2.1): body, trace, chemical; index and facies fossils; biased toward hard parts, marine settings and young rocks; exceptional deposits |
| Oxygen | Great Oxidation Event (2.4–2.3 Ga), low Proterozoic levels, Neoproterozoic oxygenation, near-modern Phanerozoic levels |
| Ediacaran | Snowball Earth glaciations; **Ediacaran biota** (Definition 29.3.1, 575–539 Mya) of uncertain affinities; first skeletons about 550 Mya |
| Cambrian | **Cambrian explosion** (Definition 29.4.1): most phyla within about 20–25 Myr; Chengjiang, Burgess; conundrum of earlier molecular divergence |
| Paleozoic | Ordovician radiation; plants, arthropods, then tetrapods on land; coal forests; **Pangaea** (Definition 29.5.1); end-Permian extinction (Siberian Traps) |
| Mesozoic | breakup of Pangaea into **Laurasia** and **Gondwana**; marine revolution; dinosaurs, birds, mammaliaforms; angiosperms from about 130 Mya; K/Pg impact at 66.0 Mya |
| Cenozoic | radiation of mammals and birds; cooling, grasslands; Panama isthmus; Pleistocene glacial cycles, refugia, megafaunal extinctions; human impact |

## Questions

1. A volcanic ash bed contains zircon with a ratio of $^{206}\mathrm{Pb}$ to $^{238}\mathrm{U}$ of 0.0848. How old is it, taking the half-life of $^{238}\mathrm{U}$ as $4.47 \times 10^9$ years?

   **Answer** By Formula 29.1.1, $t = (t_{1/2}/\ln 2)\ln(1 + D/N) = (4.47 \times 10^9/0.693)\ln 1.0848 \approx 6.45 \times 10^9 \times 0.0814 \approx 5.25 \times 10^8$ years: about 525 Mya, the age of the Chengjiang biota.

2. Why are fossils of marine animals with shells far more common than those of terrestrial or soft-bodied animals, and how do exceptional deposits help to assess this bias?

   **Answer** Fossilization requires rapid burial in sediment and resistance to decay: most sediment accumulates under water, especially in the sea, while on land organisms are scavenged and decay before burial, and soft tissues decay within days or weeks unless conditions are exceptional. Deposits such as the Burgess Shale, where soft tissues were preserved by rapid burial under anoxic conditions, show what an ordinary deposit misses: there about 86 % of the genera and 98 % of the individuals would not have been preserved with hard parts alone.

3. Molecular clocks place the divergence of many animal phyla more than 100 million years before the Cambrian. Give three hypotheses that reconcile this with their sudden appearance in the fossil record.

   **Answer** (a) Precambrian animals were small and soft-bodied, living in microbial mats, and left few fossils; the near-simultaneous origin of skeletons made them visible, which is an ecological, not a phylogenetic event. (b) Environmental changes, especially a rise in oxygen and in ocean chemistry favoring biomineralization, allowed larger, active bodies only at the end of the Proterozoic. (c) Ecological feedback, the evolution of predation and burrowing, created selection for armor and new ways of life and accelerated diversification, with the developmental toolkit already present. The molecular dates may also be overestimated.

4. What evidence supports an asteroid impact as the cause of the K/Pg extinction?

   **Answer** A thin clay layer at the boundary worldwide is enriched in iridium, an element rare in the crust but abundant in meteorites, and contains shocked quartz and spherules formed by impact; the Chicxulub crater, about 180 km across, beneath the Yucatán Peninsula, has the right age; and the extinctions coincide with the layer. The Deccan Traps eruptions were contemporaneous and may have contributed.

5. Why did many species in the Northern Hemisphere achieve their present ranges only in the last few thousand years?

   **Answer** During the last glacial maximum, about 20 000 years ago, ice sheets covered much of northern North America and Europe and climates south of them were colder and drier, so many species survived only in southern or other refugia. As the ice retreated, between about 15 000 and 8000 years ago, species recolonized northern areas by dispersal, each at its own rate, so present ranges and communities date largely from the Holocene.
