---
title: Mutualism, Commensalism and Facilitation
description: "Positive interactions between species: facilitation, mutualism and commensalism; obligate and facultative mutualism, the continuum from mutualism to parasitism and the problem of cheating. Behavioral mutualisms (cleaners, ant-plants, farming of insects and fungi, pollination and seed dispersal, figs and yuccas), mutualisms with microorganisms (gut symbionts, bacteriocyte endosymbionts and new strategies of pest control, photosynthetic symbionts and the coral holobiont, mycorrhizas and mycorrhizal networks, lichens, nitrogen fixation, the nitroplast and endosymbiosis); commensalism, nurse plants and the stress-gradient hypothesis. Models: Lotka–Volterra mutualism, bounded and unbounded, with a Dulac proof; obligate mutualism and its threshold; saturating benefits, uniqueness and global stability, the Allee-type bistability of obligate partners and its saddle-node; mutualism in communities and the nestedness of mutualistic networks."
---

The interactions of the previous chapters, competition ([7.19.22](/7.19.22)–[7.19.23](/7.19.23)), predation ([7.19.24](/7.19.24)–[7.19.27](/7.19.27)) and parasitism ([7.19.28](/7.19.28)), all harm at least one partner. Positive interactions are at least as widespread: almost every plant that dominates a grassland, heath or forest has roots joined to fungi, most reef-building corals depend on algae inside their cells, most flowering plants on animal pollinators, and every vertebrate on the microbes in its gut. This chapter describes these interactions from the ecological side. Section 29.1 defines facilitation, mutualism and commensalism and the ideas that run through all examples: mutualism is reciprocal exploitation, its sign depends on conditions, and it must resist cheating. Sections 29.2 and 29.3 survey mutualisms between animals and plants and with microorganisms, whose cell biology and physiology are treated in [7.11.31](/7.11.31), [7.13.26](/7.13.26) and [7.12.12](/7.12.12) and whose evolution in [7.10.17](/7.10.17). Section 29.4 turns to commensalism and to facilitation among plants along stress gradients. Section 29.5 develops the population models: why the simplest mutualism model explodes, how saturation and obligacy change its dynamics, and how mutualists are organized into networks, a theme continued with food webs in [7.19.38](/7.19.38).

## 29.1. Positive Interactions

### 29.1.1. Facilitation, Mutualism and Commensalism

Interactions are classified by their net effect on each partner, $+$, $0$ or $-$ ([7.19.22](/7.19.22)). Three classes involve no harm to either partner.

**Definition 29.1.1 (Facilitation)** *Facilitation* is any interaction between individuals of two species in which at least one gains a net benefit and neither is harmed (Bruno et al. 2003). If both benefit ($+\,+$) the interaction is a **mutualism** ([Definition 17.3.1](/7.10.17#def-17.3.1) of 7.10.17); if one benefits and the other is unaffected ($+\,0$) it is a **commensalism**.

The opposite of commensalism, $-\,0$, is amensalism: a tree that shades a herb without being affected by it, or a fungus whose antibiotics inhibit bacteria without any benefit to itself. Many amensal effects are one-sided competition and are treated with it.

Mutualism must be distinguished from symbiosis, a close physical association in which one partner (the symbiont) lives on or in the body of the other (the host) ([Definition 31.1.1](/7.11.31#def-31.1.1) of 7.11.31). Mutualists may be symbionts (rhizobia in root nodules, algae in corals) or not (a bird that eats fruit and disperses seeds, a bee that pollinates a flower), and symbionts may be mutualists, commensals or parasites. Most mutualisms involve an exchange of goods or services, food, protection or transport, and they typically give at least one partner a capability that it lacks on its own, an expansion of its niche: the gutless worms *Osedax* digest the bones of whale carcasses through heterotrophic bacteria in their root-like tissues, ruminants digest cellulose, and plants obtain nitrogen from the air.

**Definition 29.1.2 (Obligate and Facultative Mutualism)** A mutualism is *obligate* for a partner that cannot survive or reproduce without the other, and *facultative* for a partner that can live alone but does better with the other. An obligate mutualism may be one-sided (obligate for one partner only) or two-sided.

Chinese textbooks call the facultative case protocooperation and reserve the word for symbiosis for obligate partnerships. Leaf-cutter ants and their fungi, figs and fig wasps, aphids and *Buchnera*, and the partners of a lichen are obligate on at least one side; humans and domestic animals, ants and aphids, and most pollination and seed-dispersal systems are facultative. In the Indo-Pacific, gobies (*Cryptocentrus*, *Amblyeleotris*) share burrows dug by nearly blind snapping shrimps (*Alpheus*); the shrimp keeps an antenna on the fish when it leaves the burrow and retreats when the fish flicks its tail at danger, a facultative partnership between a digger and a watchman. Between these extremes lies "ecological obligacy": many plants can live without mycorrhizal fungi in fertilized pots but not in natural soils.

### 29.1.2. Reciprocal Exploitation and Its Instability

A mutualism is not a harmonious partnership but reciprocal exploitation in which each partner gains more than it pays. Nectar, fruit pulp, Beltian bodies and the photosynthate supplied to root symbionts are costs to the plant; the sugar-rich honeydew of aphids is extracted by ants that also restrict the aphids' growth. Three consequences follow, and they recur through this chapter.

- Context dependence. Because benefits and costs vary with conditions, the same association can move along a continuum from mutualism through commensalism to parasitism. Mycorrhizal fungi benefit plants in poor soils and can depress growth in fertilized ones; cleaner fish remove parasites where parasites are abundant but bite their clients' mucus where they are scarce; ants benefit aphids only when predators are present (Section 29.2).
- Cheating. A partner that takes the benefit without paying the cost is favored by selection, and many lineages have become cheaters: orchids that offer no nectar, yucca moths that lay eggs without pollinating, rhizobia that fix little nitrogen.
- Stabilizing mechanisms. Mutualisms persist where cheaters are penalized: by sanctions (soybeans reduce the oxygen supply to nodules whose rhizobia fail to fix nitrogen, Kiers et al. 2003), by partner choice, and by vertical transmission, which ties the fitness of a symbiont to that of its host. These mechanisms are treated in [7.10.17](/7.10.17#sec-17.3).

Mutualism is also a population interaction embedded in a community. The benefit an ant colony gives an acacia depends on which competing ant species occupies the tree; the benefit rhizobia give a legume is largest when the legume competes with grasses for scarce soil nitrogen. The models of Section 29.5 show that this embedding is necessary to understand even the stability of mutualism.

## 29.2. Mutualisms Built on Behavior

The first group of mutualisms involves no intimate symbiosis: each partner behaves in a way that benefits the other.

### 29.2.1. Cleaners and Clients

Many species of fish (in several families, notably the wrasses) and shrimps remove ectoparasites, bacteria and dead tissue from the body surface of "client" fish. Cleaners hold territories with cleaning stations, and clients visit them more often when they carry many parasites. That clients benefit was shown experimentally on the Great Barrier Reef: when the cleaner wrasse *Labroides dimidiatus* was removed from patch reefs, its client *Hemigymnus melapterus* carried 3.8 times more parasitic gnathiid isopods after 12 days, and even within a single day 4.5 times more, although not at dawn, because cleaners feed only by day (Grutter 1999).

The cleaner's preferred food, however, is client mucus and tissue, which are costly for the client to produce (Grutter and Bshary 2003). Where clients carried more ectoparasites, cleaners removed less mucus (Cheney and Côté 2005): the availability of parasites decides whether the association leans toward mutualism or toward parasitism. Clients enforce honesty by leaving or chasing a cleaner that bites, and cleaners behave more cooperatively when observed by potential clients, an example of reputation in a non-human mutualism ([7.18](/7.18)). Branchiobdellidan worms that clean the gills of crayfish show the same continuum in a different way: young crayfish, which molt often and gain little from cleaning, groom the worms off, whereas older crayfish (carapace longer than about 27–30 mm), which molt rarely, never groom and carry many worms (Skelton et al. 2016).

### 29.2.2. Ants and Plants

Belt (1874) observed aggressive ants on Central American acacias with swollen thorns, and Janzen (1967) described the system of the bull's-horn acacia *Vachellia* (formerly *Acacia*) *cornigera* and the ant *Pseudomyrmex ferruginea*. The plant provides hollow thorns for nesting, protein- and lipid-rich Beltian bodies at the leaf tips and extrafloral nectaries; the ants attack herbivores, including browsing mammals, and cut the shoots of neighboring plants. Ant–plant mutualisms have evolved many times: extrafloral nectaries occur in at least 39 plant families. In the Amazon, the tree *Duroia hirsuta* forms single-species stands that can last 800 years, called "devil's gardens" by local people; the "devils" are ants, *Myrmelachista schumanni*, which nest in the trees and kill other plants within the garden by injecting formic acid into their leaves (Frederickson et al. 2005).

Several ant species may compete for the same host. On *Vachellia drepanolobium* in Kenya, four ant species form a dominance hierarchy (*Crematogaster sjostedti* > *C. mimosae* > *C. nigriceps* > *Tetraponera penzigi*). Occupied trees grew faster than unoccupied ones, confirming the mutualism, and takeovers by more dominant ants occurred on trees that grew faster than average (Palmer et al. 2000): the balance sheet of the acacia depends on the competition among its mutualists.

### 29.2.3. Farming Mutualisms

Besides human agriculture, whose crops and livestock vastly exceed the populations their wild ancestors would have reached, farming has evolved in ants, termites and bark beetles: the farmer protects, moves or tends the species it exploits.

- Ants and honeydew producers. Ants tend aphids, scale insects and lycaenid caterpillars for their sugary secretions and protect them from predators. The aphid *Tuberculatus quercicola* on oaks in Hokkaido survived longer in ant-attended colonies when predators were present, but in a predator-free environment ant-attended aphids were smaller and carried fewer embryos than unattended ones (Yao et al. 2000): the mutualism exists only in the presence of the predators. In Mexican coffee plantations, the ant *Azteca sericeasur* tends the green coffee scale *Coccus viridis*; at high scale densities the ants also protect the coffee plants from the much more damaging coffee berry borer (*Hypothenemus hampei*), an indirect "mutualism-dependent mutualism" (Rivera-Salinas et al. 2018).
- Ants and butterflies. Caterpillars of many lycaenids are adopted by ants and milked for secretions in return for protection; others have become social parasites or predators in the ant nest. The large blue *Phengaris* (formerly *Maculinea*) *arion* feeds on wild thyme and then, as a 4 mm caterpillar, is carried into the nest of the red ant *Myrmica sabuleti*, where it eats ant larvae. It became extinct in Britain in 1979; its reintroduction succeeded once grazing kept the turf shorter than about 2 cm, because taller swards cool the soil and favor a congeneric ant in whose nests the caterpillars survive five times less well (Thomas et al. 2009).
- Fungus-farming ants. The attine ants of the New World (more than 230 species) arose from a single origin about 50 million years ago. The earliest "lower agriculture" uses detritus to manure fungi that can also live freely; "higher agriculture" grows domesticated fungi that are never found outside the nests and produce gongylidia, nutritious swollen hyphal tips harvested by the ants. Leaf-cutter ants (*Atta*, *Acromyrmex*, 8–12 million years old) culture the fungus on fresh leaves; a single *Atta cephalotes* nest harvests 50–77 % of the plant species around it, and leaf-cutters can take 17 % of the leaf production of a tropical forest, polyphagous herbivores through a fungus whose gongylidia are the only food of their larvae. The gardens are attacked by specialized pathogenic fungi (*Escovopsis*), and the ants carry on their cuticle actinomycetes (*Pseudonocardia*) whose antibiotics suppress them (Currie 2001), a three-partner mutualism. A departing queen carries a pellet of the fungus to found a new colony.
- Ambrosia beetles (Scolytinae, Platypodinae) carry fungal spores in special pockets into tunnels in dying wood, where the fungi grow and are grazed by the larvae; termites of the Macrotermitinae cultivate wood-digesting fungi in their mounds.

### 29.2.4. Pollination and Seed Dispersal

Most animal-pollinated flowers offer nectar, pollen or both (**pollination**, [7.13.26](/7.13.26#sec-26.4.1); pollination syndromes in [7.12.32](/7.12.32)). Animal pollination evolved because animals can discriminate among flowers and carry pollen between flowers of the same species, whereas wind and water do not. Specialization trades the reliability of a large supply of generalist visitors against the efficiency of transfer by specialists: in the Ranunculaceae, the nectaries of *Ficaria* are open to all, those of *Ranunculus bulbosus* are covered by a flap, and those of *Aquilegia* lie at the end of long spurs accessible only to long-tongued visitors. Darwin predicted from the 30 cm spur of the Madagascan orchid *Angraecum sesquipedale* a moth with a tongue long enough to reach the nectar; the hawkmoth *Xanthopan praedicta*, with a proboscis of about 20–25 cm, was described in 1903. When Nilsson (1988) shortened the spurs of the orchid *Platanthera*, the flowers set fewer seeds, because the moths no longer pressed against the pollinia. Seasonality limits specialization: only short-lived pollinators whose activity matches a single flowering period can depend on one plant; long-lived bats, birds and bee colonies are generalists. Pollinators also carry diseases: anther smut (*Microbotryum violaceum*) is transmitted by visitors to the flowers of white campion.

In brood-site pollination the plant feeds the pollinator's larvae. Figs (*Ficus*, about 750 species) and their pollinating wasps (Agaonidae) are mostly matched one to one (**fig–fig wasp mutualism**). A female wasp enters the closed inflorescence, pollinates the flowers and lays eggs in some of the ovaries, each of which then feeds one larva instead of making a seed; the interests of the partners conflict over the fraction of flowers that become seeds rather than wasps. After controlling for fruit size and the fraction of flowers visited, Herre and West (1997) found the expected negative correlation between seeds and wasps in nine New World fig species. Yucca moths (*Tegeticula*, *Parategeticula*) collect pollen actively, pollinate a flower of another plant and lay eggs in its ovary, where the larvae eat some of the seeds ([7.10.17](/7.10.17#sec-17.3)).

Seeds are dispersed by animals in two ways. Hooked or sticky fruits hitch a ride without rewarding the carrier; fleshy fruits pay frugivores, provided the seeds survive passage through the gut, and are protected by hard seed coats. Among 12 424 North American plant species, 10 % are dispersed by frugivorous birds and mammals, 3.7 % by scatter-hoarding rodents and birds, and 3.9 % by ants (**myrmecochory**), which carry seeds by their lipid-rich appendages (elaiosomes) and discard them in nutrient-rich waste piles (Vander Wall et al. 2017). Seed-dispersal mutualisms are rarely species-specific: a fruit, unlike nectar in a long spur, cannot be reserved for one visitor, and it need only be moved away from the parent. The interactions among the plants and animals of a community form networks; removing invasive shrubs from four mountaintops in the Seychelles increased the number of pollinator species and visits within a year, and fruit set ceased to be limited by pollinator visits (Kaiser-Bunbury et al. 2017; Section 29.5.4).

## 29.3. Mutualisms with Microorganisms

In the second group, one partner, a microorganism, lives more or less permanently in the body or the cells of the other. The cell biology and genomics of these symbioses are treated in [7.11.31](/7.11.31); here we emphasize their ecological consequences.

### 29.3.1. Gut Mutualists

The guts of all vertebrates house a mutualistic microbiota. Fermentation chambers have evolved independently in the rumen and reticulum of ruminants, the forestomachs of kangaroos, the cecum of rabbits and rodents and the colon of horses and elephants ([7.11.31](/7.11.31#sec-31.6)). The microbes receive a steady supply of chewed food in a warm, anaerobic chamber of regulated pH; the host receives short-chain fatty acids from cellulose and starch, which supply more than 60 % of the maintenance energy of cattle and 29–79 % of that of sheep, together with microbial protein and B vitamins. Hindgut fermenters recover the products by eating their own feces: rabbits produce separate soft pellets that provide about 30 % of their nitrogen. The rumen is a community in miniature, with cellulolytic and saccharolytic bacteria, methanogenic archaea, ciliates that eat bacteria and ciliates that eat other ciliates.

The gut metagenome, the genes of the whole gut community (about $3\times10^6$ in humans against some $2\times10^4$ in the human genome), changes faster than the host genome, and its plasticity may help hosts acclimatize: desert woodrats (*Neotoma lepida*) that eat toxic creosote bush carry microbes that detoxify its resins, and the gut communities of brown bears differ between seasons. Insect guts have fewer microbial species but some specialized communities, especially in social insects, where food sharing transmits microbes between nestmates. Lower termites digest wood with cellulolytic flagellates in the hindgut, higher termites with bacteria and archaea alone. Honeybees deprived of their eight dominant gut bacteria grow less and die more often; glyphosate, an herbicide considered harmless to animals because they lack the shikimate pathway that it inhibits, reduced four of these bacteria and made bees more susceptible to the pathogen *Serratia marcescens* (Motta et al. 2018).

### 29.3.2. Bacteriocyte Symbionts and Pest Control

Insects that live on nutritionally unbalanced diets (phloem or xylem sap, vertebrate blood, wood) house maternally transmitted bacteria in specialized cells (**bacteriocytes**). *Buchnera aphidicola* fills about 60 % of the bacteriocyte cytoplasm of aphids and supplies the essential amino acids missing from phloem; aphids freed of it by antibiotics grow slowly and produce few or no offspring ([7.11.31](/7.11.31#sec-31.4)). Each of the four groups of sap-sucking Sternorrhyncha (aphids, psyllids, whiteflies and mealybugs) has its own obligate symbiont acquired once and transmitted vertically ever since, whereas lineages that switched to eating whole plant cells have lost theirs: the benefit is a net benefit, and it disappears with the need. Other endosymbionts defend their hosts: pea aphids carrying *Hamiltonella defensa* resist the parasitoid wasp *Aphidius ervi* through toxins encoded by a bacteriophage of the symbiont (Oliver et al. 2014), and rove beetles (*Paederus*) carrying a *Pseudomonas* symbiont produce the toxin pederin.

Symbionts have become targets and tools of pest control:

- attacking an obligate symbiont: an antimicrobial scorpion venom peptide that kills *Buchnera* delayed reproduction and reduced the survival of pea aphids (Luna-Ramirez et al. 2017);
- introducing a symbiont that blocks a pathogen: the mosquito *Aedes aegypti* does not naturally carry *Wolbachia* ([7.11.31](/7.11.31#sec-31.4.3)); the *w*Mel strain transferred from *Drosophila melanogaster* reduces the replication of dengue virus and spreads through mosquito populations by cytoplasmic incompatibility (Hoffmann et al. 2011), and in a cluster-randomized trial in Yogyakarta, Indonesia, releases reduced the incidence of virologically confirmed dengue by 77 % (Utarini et al. 2021);
- paratransgenesis: the gut bacterium *Rhodococcus rhodnii* of the kissing bug *Rhodnius prolixus* was engineered to secrete an antimicrobial peptide active against *Trypanosoma cruzi*, the agent of Chagas disease that the bug transmits.

### 29.3.3. Photosynthetic Symbionts and the Coral Holobiont

Algae live in host-derived vacuoles of freshwater animals such as *Hydra viridis* and the ciliate *Paramecium bursaria*, supplying maltose and oxygen in exchange for nitrogen compounds from the host's prey. Whether such a partnership is mutualism or exploitation must be measured. *P. bursaria* benefited from its *Chlorella* at high light but paid a cost in the dark, and the algae inside the ciliate did not increase with light as free-living algae did and photosynthesized less efficiently: the host controls its symbionts, a "controlled exploitation" that may be a common route to stable endosymbiosis (Lowe et al. 2016).

In the nutrient-poor, clear waters of tropical reefs, dinoflagellates of the family Symbiodiniaceae (**zooxanthellae**) live in the gastrodermal cells of corals and supply up to 90 % of the coral's energy, while the host supplies inorganic carbon, nitrogen and phosphate ([7.11.31](/7.11.31#sec-31.5.4)). The coral, its algae and about a thousand bacterial taxa in its mucus, tissue and skeleton form a **holobiont**, some of whose bacteria fix nitrogen or produce antibiotics. When sea temperatures exceed the long-term maximum monthly mean for weeks, the symbiosis breaks down and the coral expels its algae or their pigments (**coral bleaching**), a major consequence of global warming ([7.19.47](/7.19.47)). The Caribbean corals *Montastraea annularis* and *M. faveolata* host three genetically distinct algal types: A and B in shallow, bright water and C in deeper, shaded water. In the warm autumn of 1995 bleaching off Panama occurred mainly at intermediate depths, through the selective loss of type C, while type A more than doubled at some sites (Rowan et al. 1997). Bleaching and recovery are therefore shifts in a symbiotic community rather than the breakdown and repair of a two-species association.

### 29.3.4. Mycorrhizas and Mycorrhizal Networks

Most plants do not have roots, they have **mycorrhizas** ([7.13.26](/7.13.26#sec-26.4.3), [7.11.31](/7.11.31#sec-31.3.1)): about 50 000 fungal species form mycorrhizas with about 250 000 plant species, and only a few families, such as the Brassicaceae and Proteaceae, lack them. The fungal hyphae forage in a volume of soil far beyond the reach of root hairs and can supply up to 80 % of a plant's nitrogen and phosphorus in exchange for carbohydrate. Fossils of the earliest land plants, which lacked roots, contain fungi resembling arbuscular mycorrhizal fungi; the colonization of land may have depended on them.

| Type | Plants | Number of plant species | Fungi | Number of fungal taxa |
|---|---|---|---|---|
| **Arbuscular mycorrhiza** | most herbs and grasses, many (especially tropical) trees, hornworts, liverworts | about 200 000 | Glomeromycota | 300–1600 |
| **Ectomycorrhiza** | Pinaceae, many temperate trees and shrubs (Fagaceae, Betulaceae, Dipterocarpaceae) | about 6000 | Basidiomycota, Ascomycota | about 20 000 |
| **Ericoid mycorrhiza** | Ericaceae | about 3900 | mainly Ascomycota | more than 150 |
| Orchid mycorrhiza | orchids | 20 000–35 000 | Basidiomycota | about 25 000 |
| Non-mycorrhizal | Brassicaceae, Crassulaceae, Proteaceae and others | about 51 500 | — | — |

Numbers after van der Heijden et al. (2015).

The types differ in what they do. Arbuscular fungi, few in species but genetically differentiated among host species, mainly improve the uptake of immobile phosphate, but also of nitrogen, resistance to toxic metals and defense against herbivores. Ectomycorrhizal fungi ensheathe the short roots of trees, extract nitrogen and phosphorus from the litter layer, including organic nitrogen by enzymatic digestion, and consume up to 30 % of the host's net photosynthate; when nitrate becomes plentiful, the host diverts its carbon from the fungus and the mycorrhiza degrades, so that the plant supports only as much fungus as it needs. Ericoid fungi of heathlands are saprotrophs that compete with other decomposers for nitrogen and phosphorus locked in organic residues; nitrogen deposition and fire suppression allow grasses to invade heaths. Orchid seedlings lack chlorophyll and depend entirely on their fungi for carbon. A classic photograph shows pine seedlings grown in prairie soil with and without inoculation with ectomycorrhizal fungi: the inoculated seedlings are several times larger, which is why mycorrhizal inoculation is a routine step in afforestation outside the native range of pines.

Because most fungi are not host-specific and most plants host several fungi, neighboring plants are linked by common mycorrhizal networks. Isotope labeling shows that carbon and nutrients can move between plants through these networks, and some experiments suggest that signals of herbivore attack can be transmitted (Babikova et al. 2013). The popular image of a "wood-wide web" through which mother trees feed their seedlings, however, goes beyond the evidence: a review of field studies found that the quantities transferred are usually small, that pathways through soil were often not excluded, and that claims of preferential transfer to kin and of forest-wide resource sharing lack field support (Karst et al. 2023).

### 29.3.5. Lichens

About 20 000 fungi are lichenized (**lichen**, [7.12.12](/7.12.12)). The fungal mycobiont forms almost all of the thallus; the photobiont, a green alga in about 90 % of species and a cyanobacterium (which also fixes nitrogen) in the rest, makes up 3–10 % of the weight and lies in a thin layer under the upper surface, like the chloroplasts of a leaf. Whether the alga benefits is uncertain: all lichenized algae can live free, but some, such as *Trebouxia*, are rare outside lichens. The mycobiont captures the minerals deposited by rain and stemflow, and the synthesis of photobiont cells is regulated by the carbon and nitrogen balance, as the shoot–root balance is in a plant. Together the partners do what neither can alone and extend into habitats closed to higher plants, rock faces, tree bark, arctic and alpine regions, dominating 8–10 % of the land surface. Lichens grow slowly (crustose colonizers of rock 1–5 mm per year) and accumulate the cations that reach them, which makes them sensitive indicators of air pollution by sulfur dioxide, heavy metals and fluoride. The thallus is itself a community, with more than 1800 species of lichenicolous fungi and many bacteria.

### 29.3.6. Nitrogen-Fixing Mutualisms

The ability to fix atmospheric nitrogen (**nitrogen fixation**, [7.1.27](/7.1.27)) is scattered among bacteria and methanogenic archaea, and several lineages have entered mutualisms with eukaryotes: rhizobia (α- and β-Proteobacteria) in the root nodules of most legumes and of the non-legume *Parasponia*; actinomycetes of the genus *Frankia* in the actinorhizal nodules of about 20 genera of mainly woody plants (alder, sea buckthorn, *Casuarina*, *Dryas*, *Ceanothus*); and cyanobacteria (*Nostoc*, *Anabaena*) in hornworts, the water fern *Azolla*, cycads and *Gunnera*. Associative nitrogen fixers such as *Azospirillum* live on root surfaces.

The legume–rhizobium symbiosis, built by a sequence of signals from flavonoids to Nod factors, infection threads and bacteroids, is described in [7.11.31](/7.11.31#sec-31.2) (**root nodule**). Its economics explain its ecology. Reducing soil nitrate to ammonium costs a plant about 12 mol ATP per mole of $\ce{NH3}$, fixation about 13.5 mol, and nodules may consume about 12 % of the plant's photosynthate: fixed nitrogen is bought with energy, a good bargain only when nitrogen is scarce. Nodulated legumes therefore reduce fixation when given nitrate, and in ecosystems enriched by nitrogen deposition the number and size of nodules decline (Regus et al. 2017). In a classic replacement-series experiment with soybean and the grass *Paspalum*, the legume dominated mixtures inoculated with rhizobia but without fertilizer, and the grass dominated whenever nitrate was added (de Wit et al. 1966). Legumes are thus "locally suicidal": when they die, their nitrogen is released within 6–12 months and favors grasses on the same spot. In a grazed pasture, stoloniferous white clover moves through the sward, leaving behind grass-dominated patches and invading patches where grazing has lowered the nitrogen status, so that the symbiosis drives cycles in the patchwork of the community. Nitrogen fixers rarely start successions on open land, because their large, poorly dispersed seeds must carry enough nitrogen to establish, and they rarely persist to the end, because fixation is too expensive in deep shade ([7.19.36](/7.19.36)).

### 29.3.7. From Symbiont to Organelle

The most consequential mutualisms are those that created the eukaryotic cell: mitochondria descend from α-proteobacteria and plastids from cyanobacteria (**endosymbiotic theory**, [7.10.28](/7.10.28)). A third step of this kind is under way in the sea. The nitrogen-fixing cyanobacterium UCYN-A (*Candidatus* Atelocyanobacterium thalassa), long known as a symbiont of the haptophyte alga *Braarudosphaera bigelowii*, divides in step with its host, is partitioned into the daughter cells, and imports proteins encoded by the host nucleus; Coale et al. (2024) argued that it has become an organelle, the "nitroplast", the first known nitrogen-fixing organelle of a eukaryote. The partnership is estimated to have begun about 100 million years ago (Cornejo-Castillo et al. 2016), which dates the making of an organelle out of a mutualism.

## 29.4. Commensalism and Facilitation

### 29.4.1. Commensalism

Commensals benefit from a partner that is not measurably affected. Remoras (Echeneidae, such as *Echeneis naucrates*) attach to sharks with a sucker on the head and ride with them, feeding on scraps; epiphytic orchids, bromeliads, mosses and lichens use tree trunks and branches as a place to live without drawing on the tree. Many commensalisms are habitat commensalisms: trees, kelps, corals and burrowing animals create structures that other species occupy. The threatened Australian crayfish *Gramastacus insolitus* does not dig, and survives the dry season only in the deep burrows of two larger crayfish species (Johnston and Robson 2009). Organisms that create, modify or maintain habitat in this way are called ecosystem engineers (Jones et al. 1994; [7.19.33](/7.19.33)). Feeding commensalisms occur among grazers: Thomson's gazelles in the Serengeti prefer swards previously grazed by wildebeest, whose grazing stimulates nutritious regrowth (McNaughton 1976). In the dry season, however, the same large grazers reduce the forage available to the smaller ones, so that commensalism and competition alternate with the seasons.

Commensalism is hard to prove, because "unaffected" is a statement about the precision of measurement: a remora may impose a small drag, an epiphyte a small load. Symbiotic commensals therefore grade into weak parasites and into mutualists that charge nearly as much as they give.

### 29.4.2. Facilitation among Plants

Facilitation among plants is common where conditions are harsh. Cushion plants of alpine and arctic habitats, low compact mats with deep taproots, buffer soil temperatures, raise humidity and soil moisture and accumulate organic matter and nutrients, and many other plant species grow preferentially inside them, so that cushion plants raise the species richness of harsh habitats (Cavieres et al. 2014). Their effect depends on their own condition: cushions of *Arenaria tetraquetra* in the Sierra Nevada of Spain were large and compact and strongly facilitating at high elevations, but small, loose and weakly facilitating at lower, drier elevations (Schöb et al. 2013). Such *nurse plants* are now used in restoration: planting tree seedlings under existing shrubs in degraded Mediterranean land improves their survival, the opposite of the earlier practice of clearing the shrubs before planting. Intercropping uses the same idea in agriculture: peanut, cowpea or sweet potato secrete organic acids and phosphatases that make phosphorus available to companion crops on acid soils, and legumes supply nitrogen to neighbors (Brooker et al. 2016). In succession, pioneers that improve the soil facilitate later species, which then outcompete them ([7.19.36](/7.19.36)).

### 29.4.3. The Stress-Gradient Hypothesis

Every neighbor both ameliorates and competes. Which effect prevails depends on how much amelioration is worth, and that depends on stress.

**Definition 29.4.1 (Stress-Gradient Hypothesis)** The *stress-gradient hypothesis* (Bertness and Callaway 1994) predicts that the relative importance of facilitation among plants increases, and that of competition decreases, with increasing abiotic stress (heat, cold, drought, salinity, wind) or consumer pressure.

A minimal model makes the logic explicit. Let a target plant alone perform $W_0(s) = 1 - s$ at stress $s \in [0, 1)$. A neighbor reduces the stress it experiences to $s(1 - \varphi)$, with $0 < \varphi < 1$, but takes a fraction $c$ of its resources: $W_1(s) = \bigl(1 - s(1 - \varphi)\bigr)(1 - c)$. The neighbor is a competitor ($W_1 < W_0$) in benign conditions and a facilitator ($W_1 > W_0$) when

$$
s > s^* = \frac{c}{\varphi + c - \varphi c}.
$$
The relative interaction index $\mathrm{RII} = (W_1 - W_0)/(W_1 + W_0)$, an effect size used in field studies, increases with stress, and the switch occurs earlier the stronger the amelioration $\varphi$ and the weaker the competition $c$ (Figure 1).

![A minimal model of the stress-gradient hypothesis with amelioration phi = 0.6 and competitive cost c = 0.25. A: performance of a target plant alone (gray) and with a nurse plant (green); the neighbor is a competitor below s* = 0.36 and a facilitator above it. B: the relative interaction index RII rises from about −0.14 (competition) to strongly positive values (facilitation); stronger amelioration (phi = 0.8, dashed) moves the switch to s* = 0.29](./plots/stress-gradient.py)

In a meta-analysis of 727 tests from terrestrial, marine and freshwater systems, He et al. (2013) found that plant interactions shift toward facilitation (for survival) or toward weaker competition (for growth and reproduction) with increasing stress, consistently across stress types (abiotic, resource, biotic), growth forms, life histories, native and invasive species, and climates, including moist tropical and temperate ones. The hypothesis has been refined: under extreme stress, when neither partner can grow, facilitation may decline again, and when the stress is a resource that the neighbor also consumes (water), amelioration and competition are coupled and the outcome is less predictable (Maestre et al. 2009). The community consequences of facilitation return in [7.19.33](/7.19.33).

## 29.5. Models of Mutualism

### 29.5.1. The Lotka–Volterra Mutualism Model

The obvious model of mutualism changes the signs of the interspecific terms in the **Lotka–Volterra model** of competition ([7.19.22](/7.19.22)):

$$
\frac{\mathrm{d}N_1}{\mathrm{d}t} = r_1N_1\,\frac{K_1 - N_1 + \alpha_{12}N_2}{K_1},\qquad
\frac{\mathrm{d}N_2}{\mathrm{d}t} = r_2N_2\,\frac{K_2 - N_2 + \alpha_{21}N_1}{K_2},
\tag{29.1}
$$
with $r_i, K_i > 0$ for facultative mutualists and benefit coefficients $\alpha_{12}, \alpha_{21} > 0$, the number of individuals of species $i$ whose effect on its own growth is offset by one individual of species $j$. With $x = N_1/K_1$, $y = N_2/K_2$, $\tau = r_1t$, $a = \alpha_{12}K_2/K_1$, $b = \alpha_{21}K_1/K_2$ and $\rho = r_2/r_1$,

$$
\dot x = x(1 - x + ay),\qquad \dot y = \rho y(1 - y + bx).
\tag{29.2}
$$
The **nullclines** are the lines $x = 1 + ay$ and $y = 1 + bx$; both have positive slope, the first with slope $1/a$ and the second with slope $b$ in the $(x, y)$ plane.

**Theorem 29.5.1 (Lotka–Volterra Mutualism)** For (29.2) with $a, b, \rho > 0$ and positive initial densities:

1. if $ab < 1$, every solution converges to the interior equilibrium
$$
x^* = \frac{1 + a}{1 - ab},\qquad y^* = \frac{1 + b}{1 - ab},
$$
at which each species exceeds its carrying capacity;
2. if $ab > 1$, there is no interior equilibrium and both densities grow without bound.

**Proof** The boundary equilibria are $(0, 0)$, $(1, 0)$ and $(0, 1)$. At $(1, 0)$ the **Jacobian matrix** is triangular with eigenvalues $-1$ and $\rho(1 + b) > 0$, so it is a saddle, and similarly $(0, 1)$; the origin is an unstable node. Solving the two nullcline equations gives the interior point above, which is positive if and only if $ab < 1$.

(1) At $(x^*, y^*)$, using $1 - x^* + ay^* = 0$ and $1 - y^* + bx^* = 0$,

$$
J = \begin{bmatrix} -x^* & ax^* \\ \rho by^* & -\rho y^* \end{bmatrix},\qquad
\operatorname{tr}J = -x^* - \rho y^* < 0,\qquad \det J = \rho x^*y^*(1 - ab) > 0,
$$
so the equilibrium is locally asymptotically stable (trace–determinant criterion, [2.4.11](/2.4.11)). Solutions are bounded: for any $\kappa > 1/(1 - ab)$ put $M = \kappa(1 + a)$ and $M' = \kappa(1 + b)$. On the side $x = M$, $0 \le y \le M'$ of the box $[0, M]\times[0, M']$, $1 - M + ay \le 1 - \kappa(1 + a) + a\kappa(1 + b) = 1 - \kappa(1 - ab) < 0$, and similarly on the side $y = M'$; the field points into the box, which is therefore positively invariant, and every solution enters such a box for $\kappa$ large enough. For Dulac's function $B = 1/(xy)$,

$$
\frac{\partial}{\partial x}\Bigl(\frac{1 - x + ay}{y}\Bigr) + \frac{\partial}{\partial y}\Bigl(\frac{\rho(1 - y + bx)}{x}\Bigr) = -\frac1y - \frac{\rho}{x} < 0
$$
in the open quadrant, so there is no closed orbit (Dulac's criterion, [Theorem 11.6.2](/2.4.11#thm-11.6.2) of 2.4.11). By the Poincaré–Bendixson theorem ([Theorem 11.6.1](/2.4.11#thm-11.6.1)) the $\omega$-limit set of a bounded positive solution is an equilibrium; the saddles on the axes attract only solutions on the axes, so every positive solution converges to $(x^*, y^*)$.

(2) If $ab > 1$ the nullcline $y = 1 + bx$ is steeper than $x = 1 + ay$ (slope $b > 1/a$) and lies above it for all $x \ge 0$. The region between them, where $\dot x > 0$ and $\dot y > 0$, is positively invariant: on its lower boundary $x = 1 + ay$ the field points vertically upward into it, on its upper boundary horizontally into it. Every positive solution enters this region (outside it one of the species increases and the other changes monotonically, with no equilibrium to stop it) and, once inside, increases in both coordinates; since there is no equilibrium to converge to, it is unbounded. $\square$

The model with $ab > 1$ was May's (1981) "orgy of mutual benefaction": in the symmetric case $a = b > 1$, $\rho = 1$, $x = y$, the equation $\dot x = x\bigl(1 + (a - 1)x\bigr)$ even reaches infinity in finite time. The weak case is no paradox, but it shows that the Lotka–Volterra form puts the limits on mutualists entirely in their intraspecific competition ($ab < 1$ means that self-limitation outweighs mutual benefit). Real benefits saturate: a plant cannot use more pollinator visits than it has ovules.

If both partners are obligate, their intrinsic growth is negative: $\dot x = x(-1 - x + ay)$, $\dot y = \rho y(-1 - y + bx)$. The nullclines then cross only if $ab > 1$, at

$$
x^* = \frac{1 + a}{ab - 1},\qquad y^* = \frac{1 + b}{ab - 1},
$$
where $\det J = \rho x^*y^*(1 - ab) < 0$: a saddle. Its stable manifold separates initial conditions from which both species go extinct from those from which both explode (Figure 2C). Linear benefits allow obligate mutualists no stable coexistence at all.

![Lotka–Volterra mutualism (Eq. 29.2, rho = 1). Blue: species 1 nullcline x = s + a y; red: species 2 nullcline y = s + b x. A: facultative mutualists with weak benefit (a = 0.5, b = 0.6, ab = 0.3): all trajectories converge to x* = 2.14, y* = 2.29, above both carrying capacities (open circles on the axes are the saddles (1, 0) and (0, 1)). B: strong benefit (a = 1.2, b = 1.1, ab = 1.32): the nullclines diverge and both populations grow without bound. C: obligate mutualists (s = −1, a = 2, b = 1.5): the nullclines cross at a saddle (1.5, 1.25) whose stable manifold (dashed) separates extinction from explosion](./plots/lv-mutualism.py)

### 29.5.2. Saturating Benefits

Wright (1989) and Holland, DeAngelis and Bronstein (2002) let the benefit saturate, as a type II functional response ([7.19.25](/7.19.25)) does:

$$
\frac{\mathrm{d}N_1}{\mathrm{d}t} = N_1\Bigl(r_1 - c_1N_1 + \frac{\beta_1N_2}{h_2 + N_2}\Bigr),\qquad
\frac{\mathrm{d}N_2}{\mathrm{d}t} = N_2\Bigl(r_2 - c_2N_2 + \frac{\beta_2N_1}{h_1 + N_1}\Bigr).
\tag{29.3}
$$
Here $r_i$ is the intrinsic growth rate of species $i$ without its partner (positive if facultative, negative if obligate), $c_i$ the strength of self-limitation, $\beta_i$ the maximal per capita benefit and $h_j$ the partner density at which half of it is reached. Since the benefit is at most $\beta_i$, $\dot N_i \le N_i(r_i + \beta_i - c_iN_i)$, so $N_i$ eventually stays below $(r_i + \beta_i)/c_i + \varepsilon$: all solutions are bounded, whatever the strength of the mutualism. The nullclines are

$$
N_1 = F(N_2) = \frac1{c_1}\Bigl(r_1 + \frac{\beta_1N_2}{h_2 + N_2}\Bigr),\qquad
N_2 = G(N_1) = \frac1{c_2}\Bigl(r_2 + \frac{\beta_2N_1}{h_1 + N_1}\Bigr),
$$
both increasing, concave and bounded.

**Proposition 29.5.1 (Facultative Mutualists)** If $r_1, r_2 > 0$, (29.3) has exactly one interior equilibrium, and it attracts every solution with $N_1(0), N_2(0) > 0$.

**Proof** In the plane $(N_1, N_2)$, the species-1 nullcline is the graph of $N_2 = F^{-1}(N_1)$ on $\bigl(r_1/c_1, (r_1 + \beta_1)/c_1\bigr)$, which is increasing and convex (the inverse of an increasing concave function), equal to $0$ at the left end and tending to $+\infty$ at the right end. The function $\phi = G - F^{-1}$ is therefore concave, positive at $N_1 = r_1/c_1$ (because $G \ge r_2/c_2 > 0$) and tends to $-\infty$ at the right end, so it has exactly one zero: one interior equilibrium $E^*$, at which $\phi$ decreases, that is, the species-2 nullcline is flatter than the species-1 nullcline. At $E^*$

$$
J = \begin{bmatrix} -c_1N_1^* & N_1^*\beta_1h_2/(h_2 + N_2^*)^2 \\ N_2^*\beta_2h_1/(h_1 + N_1^*)^2 & -c_2N_2^* \end{bmatrix};
$$
the trace is negative, and $\det J > 0$ is exactly the condition that the species-1 nullcline is steeper, so $E^*$ is locally stable. The boundary equilibria $(r_1/c_1, 0)$ and $(0, r_2/c_2)$ are saddles (the partner can invade, because its growth rate there is $r_j + \beta_jN_i/(h_i + N_i) > 0$), and the origin is a source. The off-diagonal entries of the Jacobian are positive everywhere: the system is cooperative, and bounded solutions of planar cooperative systems converge to equilibria (they are eventually monotone in each coordinate; Hirsch's theory of monotone systems, or Dulac's criterion with $B = 1/(N_1N_2)$, whose divergence $-c_1/N_2 - c_2/N_1 < 0$ excludes closed orbits). The only equilibrium attracting positive solutions is $E^*$. $\square$

**Proposition 29.5.2 (Obligate Mutualists and the Benefit Threshold)** In the symmetric case $r_i = r < 0$, $c_i = 1$, $\beta_i = \beta$, $h_i = h$, symmetric interior equilibria $N^*$ satisfy $N^2 + (h - r - \beta)N - rh = 0$. They exist if and only if

$$
\beta \ge \beta_c = h - r + 2\sqrt{-rh},
$$
and for $\beta > \beta_c$ there are two: the lower is a saddle and the upper is stable. The origin is always stable. At $\beta = \beta_c$ the two equilibria merge in a **saddle-node bifurcation**.

**Proof** Setting $N_1 = N_2 = N$ in $r - N + \beta N/(h + N) = 0$ and multiplying by $h + N$ gives the quadratic. Since $-rh > 0$, its two roots have positive product, so they are both positive or both negative or complex; they are real and positive when the discriminant $(h - r - \beta)^2 + 4rh \ge 0$ and $\beta > h - r$, that is, when $\beta - h + r \ge 2\sqrt{-rh}$. By the convexity argument of Proposition 29.5.1, now with $\phi$ negative at the left end ($G < 0$ near $N_1 = 0$), the concave $\phi$ has two zeros, at the first of which it increases (the species-2 nullcline is steeper, $\det J < 0$, a saddle) and at the second decreases (a stable node). At the origin the eigenvalues are $r < 0$. $\square$

Obligate mutualists thus show an Allee effect (**Allee effect**, [7.19.10](/7.19.10)) generated by their partners: below the stable manifold of the saddle both decline to extinction, above it both rise to the upper equilibrium (Figure 3). This makes obligate mutualisms vulnerable. If habitat loss or a pollinator decline reduces the effective benefit $\beta$ below $\beta_c$, the upper equilibrium disappears and the pair collapses, and restoring $\beta$ slightly above $\beta_c$ does not bring it back unless the densities are raised above the threshold: **bistability** with hysteresis. A partner population reduced below the threshold by a temporary disturbance also collapses. Facultative mutualists, whose $r_i > 0$, have no threshold.

![Mutualism with saturating benefits (Eq. 29.3, c = h = 1). A: facultative partners (r = 1, beta = 1.5): the bounded, concave nullclines cross once at N* = 2, which attracts all positive solutions. B: obligate partners (r = −0.3, beta = 3): the nullclines cross twice; the lower crossing (0.2, 0.2) is a saddle whose stable manifold (dashed) separates the basin of extinction (near the axes) from that of the stable equilibrium (1.5, 1.5). C: symmetric equilibria against the maximal benefit beta: one stable branch for facultative partners (r = 0.3); for obligate partners (r = −0.3) a stable branch (solid) and a threshold branch (dashed) that meet in a saddle-node at beta_c = 2.40](./plots/saturating-mutualism.py)

Other models give the same qualitative conclusions. Consumer–resource models of mutualism (Holland and DeAngelis 2010) treat each partner as a consumer of a resource produced by the other, with costs of producing it; the net effect then changes sign with partner density, from mutualism at low densities to parasitism at high densities, which also bounds the dynamics. Cropp and Norbury (2018) added an explicit shared nutrient and a variable degree of obligation and reproduced a wide range of outcomes.

### 29.5.3. Mutualism in a Community

Mutualisms embedded in communities behave differently from isolated pairs. In a model of a bee and a plant, the pair persisted only if intraspecific competition outweighed the mutualism, and the more mutualistic the interaction, the less stable; in a five-species assemblage with a second plant and a bird that eats the bees, however, mutualistic links greatly increased the fraction of random parameter sets in which all species persisted (Ringel et al. 1996). Predators and competitors of the mutualists provide the density dependence that the pair lacks. Similarly, a facultative third partner turns a fragile obligate pair into a persistent one (Takimoto and Suzuki 2017), as when *Pseudocalliope* flies, which can feed elsewhere, pollinate yuccas in marginal habitats where yucca moths are scarce.

### 29.5.4. Mutualistic Networks and Nestedness

Pollination and seed-dispersal systems are networks of many plants and many animals. Their structure is described by the interaction matrix, a binary or weighted matrix with plants as rows and animals as columns. Two regularities hold across hundreds of networks. First, specialization is asymmetric: specialists tend to interact with generalists, and specialist–specialist pairs are rare. Second, the matrices are nested (Bascompte et al. 2003).

**Definition 29.5.1 (Nestedness)** A bipartite interaction matrix is *nested* when the partners of less connected species are subsets of the partners of better connected species. Its degree of nestedness is commonly measured by NODF (nestedness based on overlap and decreasing fill; Almeida-Neto et al. 2008): for each pair of rows $i, j$ ordered so that $k_i \ge k_j$ (degrees), let $N_{ij} = 0$ if $k_i = k_j$ and otherwise the percentage of the $k_j$ partners of $j$ that are also partners of $i$; NODF is the mean of $N_{ij}$ over all pairs of rows and all pairs of columns, from 0 (no nestedness) to 100 (perfect nestedness).

A perfectly nested network has a core of generalists that interact with each other and with everyone, and specialists that interact only with the core. Whether a network is significantly nested is judged against null models, random matrices with the same size and number of links (or with the same degrees), as in the null-model analyses of community structure ([7.19.33](/7.19.33)). The simulated network of Figure 4 has NODF = 74, against 29 for random matrices of the same connectance.

![Nestedness of a mutualistic network (simulated). A: a plant–pollinator matrix with 12 plants and 20 pollinators (27.5 % of possible links), rows and columns sorted by degree; filled cells are interactions. The partners of specialists are subsets of those of generalists (NODF = 74). B: a random matrix with the same number of links (NODF = 29). C: NODF in 1000 random matrices with the same connectance (mean 29, maximum 43) and the value of the nested network (red line)](./plots/nestedness.py)

Nestedness has dynamical consequences. Because specialists depend on generalists, which are the species least likely to be lost, nested networks are robust to random species loss but vulnerable to the loss of the generalist core. In models of mutualistic communities with competition among plants and among animals, nestedness reduces effective competition and increases the number of species that can coexist (Bastolla et al. 2009). Food webs of predators and prey, in contrast, are compartmentalized rather than nested; their structure and stability are the subject of [7.19.38](/7.19.38).

## Summary

| Topic | Main points |
|---|---|
| Definitions | Facilitation: $+\,+$ (**mutualism**) or $+\,0$ (**commensalism**) (Definition 29.1.1); obligate and facultative mutualism (Definition 29.1.2); symbiosis is a physical association, not a sign |
| General principles | Reciprocal exploitation; continuum mutualism–commensalism–parasitism; context dependence; cheating, sanctions, partner choice, vertical transmission |
| Behavioral mutualisms | Cleaners (3.8× more parasites without cleaners), ant-plants, farming of aphids and fungi, pollination and seed dispersal, figs and yuccas |
| Microbial mutualisms | Gut fermentation; bacteriocyte symbionts, defensive symbionts, *Wolbachia* and paratransgenesis; zooxanthellae and the **holobiont**, **coral bleaching**; **mycorrhiza** types and networks; **lichen**; **nitrogen fixation** and its cost; the nitroplast and **endosymbiotic theory** |
| Commensalism and facilitation | Remoras, epiphytes, habitat and feeding commensalism; nurse and cushion plants; stress-gradient hypothesis (Definition 29.4.1), switch at $s^* = c/(\varphi + c - \varphi c)$ |
| LV mutualism | Equilibrium $\bigl((1 + a)/(1 - ab), (1 + b)/(1 - ab)\bigr)$ globally stable if $ab < 1$, unbounded growth if $ab > 1$ (Theorem 29.5.1); obligate LV: a saddle only |
| Saturating mutualism | Always bounded; facultative: unique, globally stable equilibrium (Proposition 29.5.1); obligate: threshold, **bistability**, **saddle-node bifurcation** at $\beta_c = h - r + 2\sqrt{-rh}$ (Proposition 29.5.2) |
| Networks | Community context stabilizes mutualism; asymmetric specialization; nestedness and NODF (Definition 29.5.1) |

## Questions

1. Why is "symbiosis" not a synonym of "mutualism"? Give one symbiotic commensalism, one non-symbiotic mutualism and one symbiotic parasitism.

   **Answer** Symbiosis describes a close physical association, whatever its sign; mutualism describes a net effect, $+\,+$, whatever the physical arrangement. Remoras on sharks are symbiotic commensals; a bird dispersing the seeds of fruits it eats is a non-symbiotic mutualist; a tapeworm in a gut is a symbiotic parasite.
2. Ants tending aphids benefit the aphids when predators are present but harm them in a predator-free environment. What does this imply for experiments designed to classify an interaction?

   **Answer** The sign of an interaction is a property of the pair in a given context, not of the species. An experiment must state the conditions under which the effect was measured, and a full description gives the net effect as a function of the context (here, of predator density). Experiments done in simplified environments (cages, greenhouses) can reverse the sign found in nature.
3. Show that in the model (29.2) with $ab < 1$ the equilibrium densities exceed the carrying capacities, and compute $x^*, y^*$ for $a = b = 0.9$. Interpret the result.

   **Answer** $x^* = (1 + a)/(1 - ab) > 1 + a > 1$, and similarly $y^* > 1$. For $a = b = 0.9$: $x^* = y^* = 1.9/0.19 = 10$, ten times the carrying capacity. As $ab \to 1$ the equilibrium diverges: the stabilizing intraspecific competition barely outweighs the mutual benefit, and the model becomes sensitive to small changes of the coefficients, one reason to prefer saturating benefits.
4. In the obligate saturating model with $r = -0.3$, $h = 1$, compute $\beta_c$ and the two equilibria for $\beta = 3$. What happens if a disturbance reduces both populations to $N = 0.15$?

   **Answer** $\beta_c = 1 + 0.3 + 2\sqrt{0.3} = 2.40$. For $\beta = 3$: $N^2 - 1.7N + 0.3 = 0$, $N = 0.2$ (saddle) and $N = 1.5$ (stable). The symmetric point $(0.15, 0.15)$ lies below the saddle, on the extinction side of its stable manifold (on the diagonal the separatrix passes through the saddle itself), so both populations decline to extinction although $\beta > \beta_c$.
5. Explain why legumes are "locally suicidal" and how grazing can sustain a cycle of legume and grass patches in a pasture.

   **Answer** A nodulated legume has an advantage only where soil nitrogen is scarce; when it dies, its nitrogen is released within months and favors grasses, which outcompete it on that spot. Grazing removes grass biomass and nitrogen, so that the nitrogen status of grass patches falls again, and stoloniferous clover can reinvade them. The legume thus moves through the sward, and the pasture is a shifting mosaic of patches at different phases of the cycle.
6. (Open) Design a field experiment to test the stress-gradient hypothesis for shrubs and tree seedlings in a semi-arid region, and say how you would measure the outcome.

   **Answer** Choose sites along a natural gradient of aridity (or manipulate water by irrigation and rain-out shelters), and at each site plant seedlings under shrubs and in the open, with a third treatment in which the shrub canopy is kept but its roots are separated by trenching (to separate amelioration of shade from belowground competition). Measure survival, growth and reproduction, compute the RII or log response ratio for each site, and test whether it increases with aridity (regression or mixed model with site as random effect). Replicate in more than one year, since a wet year changes the effective stress, and record microclimate under and outside the shrubs to quantify the amelioration directly.
