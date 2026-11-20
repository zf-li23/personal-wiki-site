---
title: "Processes Structuring Communities: Competition, Predation and Disturbance"
description: "How competition, predation and disturbance shape ecological communities: niche differentiation and guilds; null models, checkerboard distributions and the C-score; selective and generalist predators, Paine's starfish, keystone species and community importance, ecosystem engineers; disturbance, gaps, competitive lotteries and gap succession; the intermediate disturbance hypothesis as a successional mosaic and a competition–colonization hierarchy, its evidence and critique; spatial heterogeneity; equilibrium and nonequilibrium views and Huston's dynamic equilibrium."
---

The previous two chapters described communities: their composition, diversity and physical structure ([7.19.31](/7.19.31), [7.19.32](/7.19.32)). This chapter asks what produces that structure. The interactions studied pair by pair in [7.19.22](/7.19.22)–[7.19.29](/7.19.29), competition, predation, parasitism and mutualism, are the first candidates, but whether a pattern seen in a whole community is the work of an interaction is a statistical question that requires a careful null hypothesis (Section 33.1). Predators can increase or decrease the number of species among their prey, depending on what they eat; a few species, keystones and ecosystem engineers, have effects out of all proportion to their abundance (Section 33.2). Disturbance, which kills organisms and frees space, keeps many communities away from the competitive equilibrium that pairwise theory predicts, and the intermediate disturbance hypothesis, one of the most cited and most disputed ideas in ecology, makes a precise prediction about the consequences (Section 33.3). Spatial heterogeneity adds niches (Section 33.4), and the chapter ends with the contrast between equilibrium and nonequilibrium views of communities (Section 33.5). The large-scale patterns of richness, on islands and along gradients, follow in [7.19.34](/7.19.34) and [7.19.35](/7.19.35); the dynamics of communities after disturbance, succession, in [7.19.36](/7.19.36); and the assembly of communities from a regional pool, including neutral theory, in [7.19.37](/7.19.37).

## 33.1. Competition and Community Structure

### 33.1.1. Niche Differentiation and Guilds

**Interspecific competition** ([7.19.22](/7.19.22)) affects communities in three ways that are hard to tell apart in the field. It may be acting now, as a contemporary ecological force; it may have acted in the past by excluding the species that could not coexist with the residents; or it may have acted as an evolutionary force, so that the present species avoid competition because their ancestors evolved apart (the "ghost of competition past", **character displacement**, [7.10.17](/7.10.17)). All three leave the same kinds of pattern: coexisting potential competitors should differ in their niches, the differences should often appear in morphology, and species with little niche difference should rarely occur together.

The classic example of niche differentiation is MacArthur's (1958) study of five warblers of the genus *Setophaga* (then *Dendroica*) that breed together in the spruce forests of Maine and eat insects from the same trees. The Cape May warbler (*S. tigrina*) fed mainly at the tops of the trees, the blackburnian warbler (*S. fusca*) on the outer twigs of the upper crown, the bay-breasted warbler (*S. castanea*) in the middle of the crown near the trunk, and the yellow-rumped warbler (*S. coronata*) low in the trees and on the ground; the species also differed in foraging movements and in the timing of breeding. Such sets of species are the natural units for the study of competition.

**Definition 33.1.1 (Guild)** A **guild** (Root 1967) is a group of species that exploit the same class of environmental resources in a similar way, irrespective of their taxonomic position.

Membership of a guild makes competition likely but does not prove it. Within guilds, differentiation along a single niche axis is often incomplete, and coexistence is achieved by *niche complementarity*: species that overlap on one axis differ on another. Nine species of anemonefish (*Amphiprion*) near Madang, Papua New Guinea, share ten species of host anemone; each fish species is associated with particular anemones, but species that share an anemone species live in different reef zones (nearshore to offshore), and small species can share an individual anemone with a large one (Elliott and Mariscal 2001). Eleven *Macaranga* trees in Borneo are separated by light requirement (from pioneers of large gaps to shade-tolerant understory species) and, among species with similar light requirements, by soil texture (Davies et al. 1998). Five tundra plants in Alaska take up nitrogen in different chemical forms (ammonium, nitrate, glycine), at different depths and at different times of the growing season (McKane et al. 2002).

### 33.1.2. Null Models

The danger in such studies is that some difference between species is always found. Are the observed differences larger or more regular than would arise by chance among species assembled without interactions? The question led, from the late 1970s, to a method that is now standard in community ecology.

**Definition 33.1.2 (Null Model)** A **null model** in community ecology is a procedure that generates communities by randomizing observed data while retaining selected features of them and excluding, by construction, the process under study (for example, interspecific competition); the observed value of a community statistic is compared with its distribution in the randomized communities.

A null model is a statistical null hypothesis in the sense of [3.2](/3.2), and the comparison is a **permutation test** ([3.6](/3.6)): the null distribution is not derived from a formula but simulated. Its delicate part is the choice of what to keep. Lawlor (1980) analyzed the diets of ten North American lizard communities of four to nine species each, with 20 food categories (data of Pianka 1973), using the mean overlap in diet between all pairs of species as the statistic. He generated null communities with four reorganization algorithms of increasing conservatism: RA1 replaced all diet proportions, including zeros, by random numbers, which widens every niche; RA2 randomized only the nonzero proportions, keeping which foods each species eats; RA3 reshuffled each species' observed proportions among the food types, keeping its niche breadth; RA4 reshuffled only the nonzero proportions. In all ten communities the observed overlap was lower than the mean of the null communities under every algorithm, and significantly so under RA1, RA2 and RA4: the diets of the lizards are spaced out more than chance would produce, as competition theory predicts. The weaker result under RA3 illustrates the general rule: the more structure a null model preserves, the harder it is to reject, and a null model that preserves too much may already contain the effect of competition ("Narcissus effect").

The same logic applied to morphology tests community-wide character displacement. Hutchinson (1959) suggested that adjacent species in a guild have body length ratios of about 1.3; null-model reanalyses sustained a minimum size difference in only seven of 18 claimed cases and constant ratios in seven of 21 (Simberloff and Boecklen 1981), and a meta-analysis of plant traits found trait distributions more evenly spaced than expected in only 12 % of 1966 tests (Götzenberger et al. 2012). Some cases are solid, such as the leg lengths of barnacles on the Pacific coast of North America (Marchinko et al. 2004), but competition does not impose a universal spacing, as the theory of limiting similarity ([7.19.23](/7.19.23)) indeed predicts.

### 33.1.3. Checkerboards and the C-Score

Diamond (1975) surveyed the land birds of the Bismarck Archipelago off New Guinea and proposed "assembly rules" for island communities. His most striking evidence was *checkerboard* distributions: two ecologically similar species, such as the cuckoo-doves *Macropygia mackinlayi* and *M. nigrirostris*, each occupy many islands but never the same one. Connor and Simberloff (1979) replied that such patterns might arise by chance among many species and islands, and the ensuing debate, among the sharpest in ecology, produced the methods now used to analyze co-occurrence.

The data form a presence–absence matrix with species as rows and sites (islands) as columns. Two of its features are not evidence of competition and should be kept in the null model: the row sums $R_i$, how many sites each species occupies (some species are widespread, some rare), and the column sums, how many species each site holds (large islands hold more species, [7.19.34](/7.19.34)). The statistic most often used measures how far a pair of species avoids each other.

**Definition 33.1.3 (C-Score)** For species $i$ and $j$ occupying $R_i$ and $R_j$ sites, $S_{ij}$ of them shared, the **C-score** (checkerboard score; Stone and Roberts 1990) of the pair is

$$
C_{ij} = (R_i - S_{ij})(R_j - S_{ij}), \tag{33.1}
$$
the number of checkerboard units, $2\times2$ submatrices $\begin{bmatrix}1&0\\0&1\end{bmatrix}$ or $\begin{bmatrix}0&1\\1&0\end{bmatrix}$, that the pair forms. The C-score of a community is the mean of $C_{ij}$ over all pairs.

$C_{ij}$ is zero when one species occurs only where the other does and is largest, $R_iR_j$, for a perfect checkerboard ($S_{ij} = 0$). Expanding, $C_{ij} = R_iR_j - S_{ij}(R_i + R_j) + S_{ij}^2$; with the row sums fixed, as in the null models below, $C_{ij}$ is a decreasing function of the number of shared sites $S_{ij}$ for $0 \le S_{ij} \le \min(R_i, R_j)$, so a community with an excess of negative associations has a high C-score.

The null model that keeps both row and column sums is the *fixed–fixed* model. Its matrices are generated by repeatedly swapping checkerboard units (a swap $\begin{bmatrix}1&0\\0&1\end{bmatrix}\to\begin{bmatrix}0&1\\1&0\end{bmatrix}$ preserves all margins) or, more efficiently, by the curveball algorithm, in which two rows exchange randomly chosen members of the sets of sites that only one of them occupies. Both are Markov chains on the set of matrices with the given margins ([Definition 9.3.1](/3.5.9#def-9.3.1) of 3.5.9) whose **stationary distribution** is uniform, so a long run samples matrices with the observed margins with equal probability. The result is expressed as a standardized effect size

$$
\mathrm{SES} = \frac{I_{\mathrm{obs}} - \bar I_{\mathrm{null}}}{s_{\mathrm{null}}}, \tag{33.2}
$$
where $I$ is the index, and $\bar I_{\mathrm{null}}$, $s_{\mathrm{null}}$ the mean and standard deviation of its null distribution; $\lvert\mathrm{SES}\rvert > 2$ corresponds roughly to significance at the 5 % level.

![The C-score and a fixed–fixed null model, with simulated data. A: a presence–absence matrix of 18 species on 30 islands in which nine pairs of species have been made to avoid each other (where both members of a pair would occur, one is removed at random), sorted with the most widespread species on top and the richest islands on the left; the checkerboards are not visible to the eye. B: standardized null distributions of the mean C-score, from 1000 matrices with the same row and column sums (curveball algorithm), and the observed values: the structured matrix lies far in the upper tail (SES ≈ 3.7), a matrix generated without interactions within the range of chance (|SES| < 2, gray band)](./plots/c-score-null-model.py)

Gotelli and McCabe (2002) applied the method to 96 published presence–absence matrices of plants, invertebrates and vertebrates. The mean SES of the C-score was clearly positive (the null expectation is zero, with 95 % of values between −2 and 2), and the number of perfect checkerboard pairs was also higher than expected: real communities contain more negative associations than chance produces, most strongly in plants, ants and homeothermic vertebrates and least in other invertebrates, fish and reptiles. The method cannot by itself show that the cause is competition. Two species may avoid each other because they prefer different habitats ("habitat checkerboards"), or because they evolved in different places and have not dispersed into each other's ranges ("historical checkerboards"). Modern analyses therefore include habitat and dispersal information in the null model.

Competition need not be hierarchical, either. If species 1 beats species 2 for one resource, species 2 beats species 3 for another, and species 3 inhibits species 1 directly, for example chemically, the network is *intransitive* (rock–paper–scissors): no species excludes all others, and intransitive loops can maintain diversity, as shown for three strains of *Escherichia coli* that produce, resist or are sensitive to the toxin colicin (Kerr et al. 2002).

## 33.2. Predation and Community Structure

### 33.2.1. Selective and Generalist Predators

The effect of **predation** on the diversity of the prey community depends on whom the predator eats. Consider the simplest module: one predator and two prey that compete for a shared resource. If the predator prefers the competitively dominant prey, it reduces the dominant and allows the inferior competitor to persist: predation increases diversity (*predator-mediated coexistence*, analyzed as a model in [7.19.26](/7.19.26)). If it prefers the inferior competitor, it reinforces competitive exclusion and diversity falls. A **generalist** that takes species in proportion to their abundance, or switches to whichever is commonest, reduces all prey below their **carrying capacity**, weakens competition and promotes coexistence; but at high intensity it begins to eat less palatable species and eliminates them. Hence the common pattern that prey richness is highest at an intermediate intensity of predation or grazing.

Grazing illustrates both outcomes. Darwin (1859) noticed that a mown plot of turf held 20 species, nine of which disappeared when the turf was allowed to grow. Rabbits on English grasslands remove the competitive grasses, and plant richness rises with grazing pressure up to a point and falls when the rabbits are forced to eat unpalatable plants. In the Ethiopian highlands, plots grazed by cattle at intermediate intensity held more plant species than ungrazed plots, where the grass *Bothriochloa insculpta* and other competitive species covered 75–90 % of the ground, or very heavily grazed plots, where grazing-tolerant *Cynodon dactylon* dominated (Mwendera et al. 1997). The outcome depends on productivity: in a meta-analysis of 44 studies, grazing reduced plant richness in all 19 nutrient-poor systems but increased it in 14 of 25 nutrient-rich ones (Proulx and Mazumder 1998). Where resources are scarce, the inferior competitors released by grazing cannot grow fast enough to exploit the opportunity.

Two experiments with selective consumers show the other side. Jane Lubchenco (1978) studied the periwinkle *Littorina littorea* on the coast of New England. In tide pools it prefers the ephemeral green alga *Ulva* (formerly *Enteromorpha*), which is the dominant competitor there; algal richness was low where snails were rare (*Ulva* dominates), highest at intermediate snail densities and low again at high densities (only the inedible red alga *Chondrus crispus* remains). On emergent rock, where *Chondrus* is the dominant competitor and the snail still prefers the ephemeral algae, grazing reduced algal diversity monotonically. The same predator thus increases diversity in one habitat and decreases it in another, because the identity of the dominant competitor differs. In the Bahamas, the lizard *Anolis sagrei* preyed preferentially on rare spider species, and enclosures with lizards held fewer spider species for a given number of individuals than enclosures without them, leaving the small, protected *Metapeira datona* more dominant (Spiller and Schoener 1998).

Density- and distance-dependent attack by seed predators and pathogens near parent trees, the Janzen–Connell mechanism, is a frequency-dependent form of predator-mediated coexistence that is thought to contribute to the diversity of tropical forests; it is treated in [7.19.37](/7.19.37).

### 33.2.2. Paine's Starfish

The most influential experiment on predation and community structure was carried out by Robert Paine (1966) on rocky shores of the Pacific coast of North America. The starfish *Pisaster ochraceus* eats sessile barnacles and mussels as well as limpets, chitons and whelks. Paine removed all starfish from a stretch of shore about 8 m long and 2 m deep and kept it free of them for years, with an adjacent control. Within months the barnacle *Balanus glandula* settled densely; it was then crowded out by the mussel *Mytilus californianus*, which came to monopolize the space. All but one of the macroscopic algae disappeared for lack of space and most of the grazers left. The number of species fell from 15 to eight. *Pisaster* maintains diversity by preying on the competitive dominant, the mussel, and so keeps open the space that the other species need.

The effect was not general along the coast. On exposed shores, where wave action itself removes mussels and creates bare space, predators had little influence on community structure (Menge and Sutherland 1976): disturbance and predation are alternative ways of preventing competitive monopoly, and where one is strong the other matters less.

### 33.2.3. Specialists, Parasites and Biological Control

A specialist predator, especially a monophagous herbivore or parasitoid, is connected to the rest of the community through few links, and its effect is concentrated on its prey. If the prey is a dominant species, the specialist can release the whole community, which is why specialists are the preferred agents of **biological control** ([7.19.53](/7.19.53)). The same property can eliminate a species. On Fiji, the coconut moth *Levuana iridescens* was a serious pest of coconut palms until the tachinid fly *Bessa remota* was introduced from Malaysia in 1925; the moth was controlled within two years and has rarely or never been seen since, and a related native zygaenid, *Heteropan dolens*, which the fly also attacked, seems to have disappeared as well, while the palm leaf miner *Agonoxena argaula*, a competitor of *Levuana*, became more abundant. Whether these were true extinctions is debated, but the case is often cited as a warning that a successful specialist can also harm nontarget species.

Parasites and pathogens have changed whole communities when introduced to naive hosts. The chestnut blight fungus *Cryphonectria parasitica*, introduced from Asia around 1900, removed the American chestnut (*Castanea dentata*), a dominant tree over large parts of eastern North American forests, within half a century, and introduced avian malaria (*Plasmodium relictum*) and avian pox have contributed to the extinction of many endemic Hawaiian birds ([7.19.28](/7.19.28)).

### 33.2.4. Keystone Species

Paine (1969) called *Pisaster* a "keystone" species, after the central stone of an arch, whose removal makes the arch collapse. The concept has since been applied widely, sometimes loosely, and needs a definition with a measure.

**Definition 33.2.1 (Keystone Species)** A **keystone species** is a species whose effect on its community or ecosystem is large and disproportionately large relative to its abundance (Power et al. 1996).

**Definition 33.2.2 (Community Importance)** The **community importance** of species $i$ is the change in a community or ecosystem trait $t$ (species richness, productivity, the abundance of a functional group) when the species is removed, per unit of its relative abundance $p_i$:

$$
\mathrm{CI}_i = \frac{t_{\mathrm{N}} - t_{\mathrm{D}}}{t_{\mathrm{N}}}\cdot\frac{1}{p_i}, \tag{33.3}
$$
where $t_{\mathrm{N}}$ is the trait in the intact community and $t_{\mathrm{D}}$ after the deletion of species $i$ (Power et al. 1996).

A dominant species, such as a forest tree that makes up 60 % of the biomass, may have a large total effect, but its effect per unit abundance is ordinary ($\mathrm{CI} \approx 1$): it is important because it is common. A keystone has $\lvert\mathrm{CI}_i\rvert \gg 1$. For Paine's shore, if *Pisaster* makes up, say, 1 % of the biomass and its removal reduces species richness from 15 to 8, then $\mathrm{CI} = (7/15)/0.01 \approx 47$. The definition also makes clear that the keystone effect can be positive or negative and depends on the trait measured.

Well-studied keystones are of several kinds.

- *Predators.* Sea otters (*Enhydra lutris*) eat sea urchins, which graze kelp. Where otters were hunted out along the Pacific coast of North America, urchins multiplied and turned kelp forests into urchin barrens; where otters returned, the kelp returned with its fish and invertebrates (Estes and Palmisano 1974). The effect passes through two links, a **trophic cascade** ([7.19.39](/7.19.39)).
- *Prey and mutualists.* Keystones need not be at the top of the food chain. Squid and other forage species that link plankton production to fish, seabirds and marine mammals can control the structure of pelagic food webs. Pollinators and seed dispersers on which many plants depend, such as fig wasps for figs and figs in turn for tropical frugivores, are keystone mutualists ([7.19.29](/7.19.29)).
- *Modifiers of habitat.* Beavers, reef-building corals and seagrasses alter the physical environment for whole communities. Seagrass beds support animals of several trophic levels by different mechanisms, providing food, shelter and nursery habitat, so that the biomass of animals at each trophic level is much higher in seagrass meadows than on adjacent bare flats (Chen et al. 2024). These species are better described by the next concept.

### 33.2.5. Ecosystem Engineers

**Definition 33.2.3 (Ecosystem Engineer)** An **ecosystem engineer** is an organism that directly or indirectly controls the availability of resources to other species by causing physical state changes in biotic or abiotic materials, thereby modifying, maintaining or creating habitats (Jones, Lawton and Shachak 1994). *Autogenic* engineers change the environment through their own physical structure (trees, corals, kelp, seagrass); *allogenic* engineers transform other materials from one state to another (beavers, burrowing animals, earthworms).

Beavers (*Castor canadensis*, *C. fiber*) build dams that turn streams into ponds and wetlands, retain sediment and nutrients, raise the water table and create habitat for aquatic plants, invertebrates, amphibians and waterfowl; a landscape with beaver ponds holds more species of herbaceous plants than one without them (Wright et al. 2002). African elephants knock down and debark trees, maintaining open savanna. Engineering is not a trophic interaction, and its importance depends on the extent and persistence of the changes: a beaver dam may alter a valley for decades after its builders have left.

## 33.3. Disturbance

### 33.3.1. Disturbance and Gaps

Competition theory predicts what happens when populations are near their equilibria. Many communities are kept away from equilibrium by events that kill organisms or remove biomass: storms, fire, floods, landslides, the burrowing and trampling of animals, the death of a large tree.

**Definition 33.3.1 (Disturbance)** A **disturbance** is a relatively discrete event in time that removes organisms or otherwise disrupts the community, by changing the availability of space or resources or the physical environment (Pickett and White 1985; Townsend and Hildrew 1994).

A disturbance regime is described by the size of the disturbed patches, their frequency (or the mean return interval), their intensity (the fraction of biomass removed) and their timing relative to the life cycles of the organisms. Disturbance often creates gaps, open patches within an otherwise continuous community, such as a treefall gap in a forest, a cleared patch in a mussel bed or a bare spot in grassland. What happens in a gap depends on how the species differ. In a *dominance-controlled* community some species are better colonists and others better competitors, and gaps are filled by a more or less predictable sequence of species, a small-scale succession. In a *founder-controlled* community, species are equivalent colonists and equivalent competitors, and the first to arrive holds the gap (Yodzis 1986).

### 33.3.2. Competitive Lotteries

**Definition 33.3.2 (Lottery Competition)** **Lottery competition** (a competitive lottery) is competition for space in which vacant sites are captured by whichever juvenile arrives first, the probability of capture by a species being proportional to its supply of propagules, and the winner holds the site for its lifetime (Sale 1977).

The idea arose from coral reef fishes, whose diversity is astonishing: the Great Barrier Reef holds 900–1500 species, and more than 50 resident species can be found on a single patch of reef 3 m across, many with similar diets. Living space is limiting and becomes available unpredictably when a resident dies, and the life cycles match: the species breed often and release many dispersing larvae, the tickets of the lottery. On the upper slope of Heron Reef in the Great Barrier Reef, three herbivorous damselfishes, *Plectroglyphidodon lacrymatus*, *Pomacentrus wardi* and *Eupomacentrus apicalis*, hold adjacent territories in rubble. When residents died, the sites they had held were reoccupied by individuals of the three species as in Table 1 (Sale 1979).

| Resident lost | Reoccupied by *E. apicalis* | by *P. lacrymatus* | by *P. wardi* |
|---|---|---|---|
| *Eupomacentrus apicalis* | 9 | 3 | 19 |
| *Plectroglyphidodon lacrymatus* | 12 | 5 | 9 |
| *Pomacentrus wardi* | 27 | 18 | 29 |

A $\chi^2$ test of independence of the table ([3.6.12](/3.6.12)) gives $\chi^2 = 6.5$ with 4 degrees of freedom, $p = 0.16$: the species of the new occupant does not depend on the species of the previous one, and there is no successional sequence of ownership. Similar lotteries have been proposed for chalk grassland plants, where the tickets are seeds, and for trees in small forest gaps.

Does a lottery maintain diversity? With constant fecundities it does not. The lottery model of Chesson and Warner (1981), Eq. (23.6) of [7.19.23](/7.19.23), shows that the species with the larger mean log fecundity wins unless adults survive between recruitment events and recruitment fluctuates, in which case the **storage effect** gives each species a positive growth rate when rare. With exactly equal species the lottery is neutral and diversity is lost slowly by drift, as in the neutral theory of [7.19.37](/7.19.37). The figure compares these cases in a finite community.

![Competitive lotteries for space in a community of 1000 sites and eight species. Each year every adult dies with probability δ and the vacant sites are won by juveniles in proportion to the fecundity times the number of sites each species holds. A: equal, constant fecundities (δ = 0.2): the lottery is neutral and relative abundances drift until one species holds all sites. B: fecundities that fluctuate independently from year to year (lognormal, standard deviation of the log 1.5, small differences in the mean) with long-lived adults (δ = 0.1): no species wins, as the storage effect predicts. C: number of species present, mean of 20 runs: a 5 % fecundity advantage of one species leads to monopoly within about 1000 years, the neutral lottery loses species slowly, and fluctuating recruitment maintains most species with long-lived adults (δ = 0.1) but not with an annual life cycle (δ = 1)](./plots/lottery-communities.py)

The figure separates two claims that are often confused. A lottery explains why the identity of the occupant of a site is unpredictable; it explains the long-term coexistence of many species only when an additional mechanism, here the storage effect, gives rare species an advantage.

### 33.3.3. Gap Succession

In dominance-controlled communities, a new gap is first invaded by one or a few pioneer species with good dispersal; their activities change conditions and allow mid-successional species to enter, and these are in turn replaced by late-successional, competitively dominant species. The number of species in the gap is low at first, highest in mid-succession and somewhat lower at the end. Unlike a lottery, each stage usually contains several species, and the sequence is predictable. A forest seen at a large scale is a mosaic of such small successions at different stages (Watt 1947), the subject of the next section and of [7.19.36](/7.19.36).

How a gap is filled depends on its size and shape. In mussel beds of *Brachidontes* in Brazil, small gaps were closed by the lateral movement of mussels from the edge, while large gaps were colonized by barnacles and by mussel larvae in their centers, and gaps of different shapes but the same perimeter-to-area ratio were colonized alike: the distance to the nearest source of colonists is what matters (Tanaka and Magalhães 2002). The same applies to forest gaps, in which the centers of large gaps are reached only by long-distance dispersers, and to gaps in grassland created by burrowing animals.

### 33.3.4. The Intermediate Disturbance Hypothesis

**Definition 33.3.3 (Intermediate Disturbance Hypothesis)** The **intermediate disturbance hypothesis** (Connell 1978; earlier Horn 1975) states that species diversity is highest at intermediate frequencies or intensities of disturbance: when disturbance is frequent, only a few pioneer species that colonize quickly and tolerate the disturbance persist; when it is rare, the community approaches competitive equilibrium and the superior competitors exclude the others; in between, both kinds of species persist.

Connell's argument can be made quantitative in two ways.

*A successional mosaic.* Suppose a landscape consists of many patches, each reset to bare ground by disturbances that occur independently in each patch at rate $\delta$ (a Poisson process). A patch of age $a$ holds $s(a)$ species: richness rises as species colonize and falls as the superior competitors exclude the others. A simple form is

$$
s(a) = 1 + (S_0 - 1)\left(1 - \mathrm{e}^{-\lambda a}\right)\mathrm{e}^{-\mu a}, \tag{33.4}
$$
with $S_0$ the regional pool, $\lambda$ the colonization rate and $\mu$ the rate of competitive exclusion ($\mu < \lambda$). Because the time since the last disturbance in a patch is exponentially distributed with mean $1/\delta$, the stationary age distribution of patches has density $\delta\mathrm{e}^{-\delta a}$.

**Proposition 33.3.1 (Richness in a Successional Mosaic)** Under Eq. (33.4) and exponential patch ages, the mean number of species per patch is

$$
\bar s(\delta) = 1 + (S_0 - 1)\,\delta\left(\frac{1}{\delta + \mu} - \frac{1}{\delta + \lambda + \mu}\right),
$$
which tends to 1 both as $\delta \to 0$ and as $\delta \to \infty$ and is maximal at $\delta^* = \sqrt{\mu(\lambda + \mu)}$, the geometric mean of the exclusion rate and the total rate $\lambda + \mu$.

**Proof** $\bar s = \int_0^\infty s(a)\,\delta\mathrm{e}^{-\delta a}\,\mathrm{d}a$, and $\int_0^\infty \mathrm{e}^{-ka}\,\delta\mathrm{e}^{-\delta a}\,\mathrm{d}a = \delta/(\delta + k)$; applying this with $k = \mu$ and $k = \lambda + \mu$ gives the formula. As $\delta \to 0$ the bracket tends to $1/\mu - 1/(\lambda + \mu)$, which multiplied by $\delta$ tends to 0; as $\delta \to \infty$, $\delta\lambda/[(\delta + \mu)(\delta + \lambda + \mu)] \to 0$. Write $g(\delta) = \delta/(\delta + \mu) - \delta/(\delta + \lambda + \mu)$. Then $g'(\delta) = \mu/(\delta + \mu)^2 - (\lambda + \mu)/(\delta + \lambda + \mu)^2$, which vanishes when $(\delta + \lambda + \mu)/(\delta + \mu) = r$ with $r = \sqrt{(\lambda + \mu)/\mu} > 1$. Solving, $\delta(r - 1) = \lambda + \mu - r\mu = r^2\mu - r\mu$, so $\delta^* = r\mu = \sqrt{\mu(\lambda + \mu)}$; $g' > 0$ below and $g' < 0$ above this value. $\square$

The optimum has a direct reading: diversity is highest when the mean interval between disturbances, $1/\delta^*$, is comparable to the time scale of succession, between the time to colonize ($1/\lambda$) and the time to exclusion ($1/\mu$). With $\lambda = 0.2$ and $\mu = 0.02$ per year, $\delta^* \approx 0.066$ per year, a return interval of about 15 years (Figure 3A).

*A competition–colonization hierarchy.* The mosaic model takes the hump in $s(a)$ as given. A model in which coexistence is derived from species traits is Tilman's (1994) hierarchy, introduced in [7.19.16](/7.19.16): $n$ species ranked by competitive ability, species $i$ displacing all species $j > i$ from the sites it colonizes, with colonization rates $c_i$ increasing down the hierarchy and a disturbance mortality $m$ that kills occupants regardless of species,

$$
\frac{\mathrm{d}p_i}{\mathrm{d}t} = c_ip_i\Big(1 - \sum_{j\le i}p_j\Big) - mp_i - p_i\sum_{j<i}c_jp_j. \tag{33.5}
$$

**Proposition 33.3.2 (Disturbance Window for Two Species)** In Eq. (33.5) with two species, the inferior competitor coexists with the superior one if and only if

$$
\frac{c_1^2}{c_2} < m < c_1 .
$$

**Proof** Species 1 is unaffected by species 2 and obeys a **Levins model** with colonization $c_1$ and extinction $m$, so it persists, at $p_1^* = 1 - m/c_1$, if and only if $m < c_1$. If species 1 is absent, species 2 can persist only if $c_2 > m$, which follows from $c_2 > c_1^2/m$ and $m < c_1$, since then $c_2 > c_1 > m$. Species 2, when rare, grows at the per capita rate $c_2(1 - p_1^*) - m - c_1p_1^* = c_2m/c_1 - m - c_1 + m = c_2m/c_1 - c_1$, which is positive if and only if $m > c_1^2/c_2$ (this is Theorem 16.6.1 of [7.19.16](/7.19.16) with $e_1 = e_2 = m$). At the resulting equilibrium $p_2^* = 1 - p_1^* - (m + c_1p_1^*)/c_2 > 0$, and the boundary equilibrium with species 2 absent is unstable, so the two species coexist. $\square$

Low disturbance therefore excludes the poor competitor (it cannot find enough empty sites) and high disturbance excludes the good competitor (it cannot colonize fast enough to replace its losses). With many species the windows overlap, and the number of coexisting species is a hump-shaped function of $m$ (Figure 3B–C). Here intermediate disturbance maintains diversity through a genuine coexistence mechanism, the competition–colonization trade-off.

![Models of the intermediate disturbance hypothesis. A: a successional mosaic (Eq. (33.4), pool of 30 species, colonization λ = 0.2 and exclusion μ = 0.02 per year): mean richness per patch (blue, bottom axis, logarithmic) peaks at δ* = √(μ(λ + μ)) ≈ 0.066 per year (Proposition 33.3.1); gray dashed curve, top axis: richness of a single patch against its age. B: Tilman's competition–colonization hierarchy (Eq. (33.5)) with 20 species whose colonization rates increase by a factor 1.25 per rank: number of species with positive equilibrium occupancy and the effective number of species exp(H′), against disturbance mortality m. C: equilibrium occupancies of all species against m (best competitor at the bottom): disturbance first lets inferior species in, then removes the best competitors one by one. D: the same model with all colonization rates multiplied by a productivity factor g: richness depends only on m/g, so the band of high richness lies along m ∝ g (dashed), Huston's dynamic equilibrium (Section 33.5)](./plots/intermediate-disturbance.py)

*Evidence.* Sousa (1979) studied algae and barnacles on intertidal boulders in southern California, which waves overturn with a frequency that depends on their size: small boulders (moved by forces below 49 N) had a 42 % chance of being moved in a given month, intermediate boulders (50–294 N) 9 % and large boulders (above 294 N) 0.1 %. Over four censuses, small boulders had the most bare space (50–78 %) and the fewest species (mean 1.4–1.9), dominated by the green alga *Ulva* and the barnacle *Chthamalus fissus*; intermediate boulders had the most species (mean 3.4–4.3), with both colonists and competitors; large boulders had fewer (2.3–3.5), with the red alga *Chondracanthus canaliculatus* (formerly *Gigartina canaliculata*) dominating. Invertebrate richness at 54 stream sites of the Taieri River in New Zealand peaked at intermediate frequencies of bed movement (Townsend et al. 1997). Several recent studies, some from China, report the same shape:

- Sea otters digging for clams in eelgrass (*Zostera marina*) meadows create pits and bare patches that are colonized by seedlings, and eelgrass genetic diversity is higher where otters have been present longest, because the disturbance favors sexual recruitment over clonal spread (Foster et al. 2021).
- In farmland of central and eastern Jilin Province, landscapes of intermediate agricultural intensity supported the highest abundance and richness of birds.
- In the Northeast China Tiger and Leopard National Park, understory bird richness was higher in forests grazed by cattle than in ungrazed forests, with grazing acting through the structure and diversity of the understory; on grasslands both exclusion of grazing and overgrazing can degrade pasture, the familiar hump.
- Across the globe, the richness of terrestrial vertebrates, especially birds and mammals, increases with the fraction of productivity consumed by fire (Moritz et al. 2023), and experimental and prescribed burns have shown that fire can increase plant and animal diversity in fire-adapted forests (**fire regime**, [7.19.5](/7.19.5)).

*Critique.* The hypothesis is far from general. Of the studies reviewed by Mackey and Currie (2001) and Hughes et al. (2007), only a minority found a hump; many found monotonic increases or decreases, a few a U shape, and many no relationship. Part of the variation arises because studies sample only part of the range of disturbance. A more fundamental objection was raised by Fox (2013), building on Chesson and Huntly (1997): the verbal mechanisms, that disturbance "reduces competition" or "interrupts competitive exclusion", do not by themselves produce coexistence. The following proposition makes the point for density-independent mortality.

**Proposition 33.3.3 (Disturbance Mortality Alone Is Not a Stabilizing Mechanism)** In the Lotka–Volterra competition model $\dot N_i = r_iN_i(1 - N_i/K_i - \alpha_{ij}N_j/K_i) - mN_i$ ($i \ne j$), a constant density-independent mortality $m < \min(r_1, r_2)$ changes the carrying capacities to $K_i' = K_i(1 - m/r_i)$ but not the competition coefficients. The species coexist stably if and only if $\alpha_{12} < K_1'/K_2' < 1/\alpha_{21}$; if $\alpha_{12}\alpha_{21} \ge 1$ there is no value of $m$ for which they coexist stably.

**Proof** $r_iN_i(1 - N_i/K_i - \alpha_{ij}N_j/K_i) - mN_i = (r_i - m)N_i\big(1 - N_i/K_i' - \alpha_{ij}N_j/K_i'\big)$ with $K_i' = K_i(r_i - m)/r_i$, a Lotka–Volterra system with growth rates $r_i - m > 0$, the same $\alpha_{ij}$ and carrying capacities $K_i'$. By Theorem 22.4.3 of [7.19.22](/7.19.22), stable coexistence requires $\alpha_{12} < K_1'/K_2'$ and $\alpha_{21} < K_2'/K_1'$; the interval $(\alpha_{12}, 1/\alpha_{21})$ is nonempty only if $\alpha_{12}\alpha_{21} < 1$, a condition that does not involve $m$. $\square$

Disturbance that kills individuals at random can therefore shift the balance between competitors (an *equalizing* effect in the language of [7.19.23](/7.19.23)), for example by penalizing the slower-growing species, but it cannot create the stabilization (each species limiting itself more than the other) that coexistence requires. Intermediate disturbance maintains diversity only through mechanisms such as the competition–colonization trade-off (Proposition 33.3.2), the storage effect in fluctuating disturbance regimes, relative nonlinearity of responses, or the spatial mosaic of patches at different successional stages, which is a form of spatial niche partitioning. Fox concluded that the hypothesis should be abandoned; others replied that the empirical pattern and the mosaic and trade-off mechanisms remain useful (Sheil and Burslem 2013). The productive lesson is that "intermediate disturbance" names a pattern, and that each case needs a specific mechanism.

For management the conclusion is practical: excluding all disturbance, such as suppressing every fire or removing all grazing, is not the way to preserve diversity in communities that evolved with disturbance ([7.19.52](/7.19.52)).

## 33.4. Spatial Heterogeneity

A spatially heterogeneous environment offers more kinds of microhabitat, microclimate and refuge, and so a longer resource axis in the sense of MacArthur's model ([7.19.35](/7.19.35)). Heterogeneity may be abiotic, in substrate, topography and soil, or biotic, created by the organisms themselves. The number of freshwater mollusc species increases with the number of substrate types in a lake, and plant richness is higher where soils and landforms change over short distances. MacArthur and MacArthur (1961) measured the diversity of foliage in different layers of deciduous forests in eastern North America, the *foliage height diversity* (the Shannon index of the proportions of foliage in the layers 0–0.6 m, 0.6–7.6 m and above 7.6 m), and found that bird species diversity was much more closely related to it than to the number of plant species: what matters to birds is the vertical structure of the vegetation, not the botanical composition. In grassland and shrubland, where vertical structure is limited, the horizontal patchiness of vegetation is more important. A meta-analysis of 192 studies worldwide found that richness increases with environmental heterogeneity of all kinds, most strongly with vegetation structure and topography, and more clearly in larger study plots (Stein et al. 2013).

Heterogeneity and disturbance interact: disturbance itself creates a patch mosaic, and a landscape that combines patches of different age or type supports more species overall (high **beta diversity**) even if each patch is poor. The measurement and analysis of landscape heterogeneity are the subject of [7.19.48](/7.19.48).

## 33.5. Equilibrium and Nonequilibrium Views

The preceding sections suggest two contrasting views of communities.

| | Equilibrium view | Nonequilibrium view |
|---|---|---|
| Community | Species near a stable equilibrium; global stability | Species composition continually changing; no global equilibrium |
| Changes due to | External perturbations, after which the system returns | Disturbance and variability as normal features |
| Key processes | Competition, niche differentiation, predation at equilibrium | Disturbance, recruitment variability, colonization, chance |
| System | Closed (dynamics determined locally) | Open (immigration from a regional pool) |
| Properties studied | Equilibria and their stability | Resistance, resilience, rates of change |
| Representatives | MacArthur; Lotka–Volterra theory | Connell; Huston; lottery and mosaic models |

The views are less opposed than the table suggests. Most models of the nonequilibrium view have a statistical equilibrium at a larger scale (a stationary distribution of patch states, as in Section 33.3.4 and Horn's model in [7.19.36](/7.19.36)); the difference is the scale at which equilibrium is sought.

Huston (1979) combined the two in his *dynamic equilibrium model*. Diversity depends on the balance between two rates: the rate of competitive displacement, which increases with productivity because populations grow and exclude one another faster, and the frequency or intensity of disturbance that reduces populations. Without disturbance, competitive exclusion is reached quickly in productive environments and diversity is low; at intermediate frequencies of disturbance exclusion is slowed and diversity is high for a long time; with very frequent disturbance diversity falls again. The model predicts that the disturbance level at which diversity peaks increases with productivity, and that in unproductive environments even weak disturbance reduces diversity, consistent with the grazing results of Proulx and Mazumder above. Figure 3D derives this from Eq. (33.5): if all colonization rates scale with a productivity factor $g$, $c_i = gc_i^0$, then dividing Eq. (33.5) by $g$ and rescaling time shows that the equilibria depend only on $m/g$, so lines of equal richness are lines $m \propto g$.

The modern consensus is plurality: competition, predation, mutualism and facilitation ([7.19.29](/7.19.29)), disturbance and chance all act in most communities, and their relative importance changes with productivity, disturbance regime and spatial scale. In a species-rich community of small plants in southern Mexico, detailed population models fitted to more than a million abundance records showed that interspecific interactions, mostly positive, were important during the colonization of empty patches, while established plants were limited mainly by intraspecific competition, and that removing the stochastic colonization of patches reduced predicted abundances by about half (Martorell and Freckleton 2014).

## Summary

| Process | Key results | Section |
|---|---|---|
| Competition | Niche differentiation and complementarity within guilds (Definition 33.1.1); null models (Definition 33.1.2) test whether patterns exceed chance; C-score (Eq. (33.1)) and fixed–fixed randomization show an excess of negative co-occurrence in many communities, but habitat and history can produce the same pattern | 33.1 |
| Predation | Selective predation on the dominant competitor increases diversity, on inferior competitors decreases it; generalists give a hump with intensity; grazing raises richness only in productive systems; Paine's *Pisaster*: 15 → 8 species without the predator | 33.2.1–33.2.3 |
| Keystones and engineers | Keystone: effect disproportionate to abundance, measured by community importance (Eq. (33.3)); sea otters, pollinators, beavers, corals, seagrasses; ecosystem engineers modify habitats physically (Definition 33.2.3) | 33.2.4–33.2.5 |
| Disturbance | Gaps; founder- vs dominance-controlled communities; lotteries (Definition 33.3.2) make occupancy unpredictable but maintain diversity only with a coexistence mechanism such as the storage effect | 33.3.1–33.3.3 |
| Intermediate disturbance | Mosaic model: richness peaks at δ* = √(μ(λ + μ)) (Proposition 33.3.1); competition–colonization window c₁²/c₂ < m < c₁ (Proposition 33.3.2); random mortality alone cannot stabilize (Proposition 33.3.3); evidence mixed | 33.3.4 |
| Heterogeneity and views | More microhabitats, more species (foliage height diversity); equilibrium vs nonequilibrium views; Huston: peak disturbance rises with productivity | 33.4–33.5 |

## Questions

1. Why should a null model for a presence–absence matrix keep the row and column sums fixed? What would be wrong with a null model that places each species on islands at random with equal probability?

   **Answer** The row sums record how widespread each species is and the column sums how many species each island holds. Both have causes other than competition: some species are rare or poor dispersers, and large or near islands hold more species. A null model that ignores the column sums would put as many species on small islands as on large ones, so species would appear to avoid each other simply because many of them are absent from small islands, and checkerboards would be "detected" in any archipelago with islands of different sizes. Keeping both margins isolates the pattern of who occurs with whom, given how common each species is and how rich each island is. The price is that the null model may absorb part of the effect of competition (for example, if competition reduces the richness of small islands), which makes the test conservative.

2. Compute the C-score of the pair of species with distributions $(1,1,0,0,1)$ and $(0,0,1,1,1)$ over five islands, and the maximum possible C-score for two species occupying three islands each out of five.

   **Answer** $R_1 = 3$, $R_2 = 3$, $S_{12} = 1$ (island 5), so $C_{12} = (3 - 1)(3 - 1) = 4$. A perfect checkerboard would need $S_{12} = 0$, which requires six islands; with five islands at least one island is shared, so the maximum is 4 and this pair is as segregated as possible. The general maximum $R_iR_j = 9$ is reached only when $R_i + R_j$ does not exceed the number of sites.

3. A species makes up 0.5 % of the biomass of a lake community. When it is removed experimentally, zooplankton biomass increases from 2.0 to 3.2 g m⁻³. Compute its community importance for this trait. Is it a keystone?

   **Answer** $\mathrm{CI} = [(t_{\mathrm{N}} - t_{\mathrm{D}})/t_{\mathrm{N}}]/p = [(2.0 - 3.2)/2.0]/0.005 = -0.6/0.005 = -120$. Its effect on zooplankton biomass is 120 times larger than expected from its abundance, and negative (it reduces zooplankton, as a planktivorous fish would): by the definition of Power et al. it is a keystone with respect to this trait. A dominant species with the same total effect but 60 % of the biomass would have $\lvert\mathrm{CI}\rvert = 1$.

4. In the mosaic model of Proposition 33.3.1, how does the optimal disturbance rate change if competitive exclusion becomes faster (larger $\mu$), for example because of nutrient enrichment? Relate the answer to Huston's model.

   **Answer** $\delta^* = \sqrt{\mu(\lambda + \mu)}$ increases with $\mu$: if exclusion is faster, disturbance must be more frequent to keep patches in the species-rich mid-successional state. Huston's dynamic equilibrium makes the same prediction: in more productive environments, where populations grow and exclude one another faster, the diversity peak occurs at higher disturbance frequencies, and a disturbance regime that maximized diversity in an unproductive environment becomes "too low" after enrichment, so diversity falls.

5. Explain why Proposition 33.3.3 does not contradict Proposition 33.3.2, although in both models disturbance is a mortality that does not depend on the species.

   **Answer** In the Lotka–Volterra model, competitors interact through a fixed pattern of per capita effects, and a uniform mortality merely rescales growth rates and carrying capacities; the condition for mutual invasibility, $\alpha_{12}\alpha_{21} < 1$, does not involve $m$. In the competition–colonization model, mortality creates empty sites, and the species differ in how they use them: the inferior competitor is a better colonist. Disturbance thus creates a resource (empty space) on which the inferior species has an advantage, and the trade-off makes each species limited by a different factor (species 1 by its colonization rate, species 2 by the space left by species 1). It is this trade-off, not the mortality itself, that stabilizes coexistence.

6. (Open question) Design a field study to test whether a hump-shaped relationship between grazing intensity and plant richness in an alpine meadow reflects the intermediate disturbance hypothesis.

   **Answer** Possible elements: (1) an experimental gradient of grazing intensity (fenced plots with controlled stocking rates or clipping) replicated in sites of different productivity, so that the whole range of disturbance is sampled and Huston's prediction (the peak shifts with productivity) can be tested; (2) measurements of the mechanism, not only of richness: which species increase at intermediate grazing, whether they are competitively inferior but grazing-tolerant or fast colonists (traits such as height, palatability, seed production), and whether the dominant species are preferentially eaten; (3) tests of invasibility, for example sowing seeds of species absent from plots at each intensity, to see whether intermediate grazing allows species to establish when rare; (4) monitoring for several years, because short studies may record transient richness; (5) correct estimation of richness, using rarefaction or Hill numbers, since grazing changes plant density. A hump with no evidence that species can increase when rare would be a pattern without a coexistence mechanism.
