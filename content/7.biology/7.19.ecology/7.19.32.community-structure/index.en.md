---
title: "Community Structure: Life Forms, Gradients, Classification and Ordination"
description: "The physical and spatial structure of communities. Structural units: life forms and life-form spectra, animal life forms and ecological equivalents, synusiae. Vertical structure (stratification of forests, animals and lakes), horizontal structure (mosaics and their causes), temporal structure (physiognomy, seasonal aspects). Ecotones and edge effects, positive and negative. Interspecific association: 2 × 2 tables, the chi-square test and association coefficients. Gradient analysis, Gaussian species responses and the continuum. Classification: the Chinese vegetation classification (vegetation type groups, vegetation types, formations, associations) and its naming conventions, the Zürich–Montpellier and Anglo-American schools, numerical classification by hierarchical clustering. Ordination: polar ordination, PCA and the horseshoe, CA and DCA and the arch, PCoA and NMDS, constrained ordination (CCA, RDA) and its environmental interpretation."
---

A community is more than a list of species with their abundances ([7.19.31](/7.19.31)): its species are arranged in space and time. Trees, shrubs and herbs form layers; patches of different composition alternate on the ground; the appearance of a grassland changes with the seasons; and from one place to another the composition changes, sharply at some boundaries and gradually along most environmental gradients. This chapter describes this structure and the methods that reveal it. Section 32.1 introduces the structural units, life forms and synusiae; Section 32.2 the vertical, horizontal and temporal structure; Section 32.3 the transition zones between communities; Section 32.4 the association between pairs of species; Section 32.5 gradient analysis and the continuum; Sections 32.6 and 32.7 the two complementary approaches to describing many communities at once, classification and ordination. The multivariate methods are derived in the statistics course ([3.4](/3.4)); here we explain what they do to ecological data and why some of them distort it.

## 32.1. Structural Units: Life Forms and Synusiae

### 32.1.1. Life Forms and Life-Form Spectra

The spatial structure of a plant community is built from two units: the life forms of its species and the synusiae, groups of species of the same life form. A **life form** ([Definition 32.1.1](/7.12.32#def-32.1.1) of 7.12.32) is the outward form that a plant shows as a result of its adaptation to the environment; plants of the same life form resemble each other in appearance and in their mode of adaptation. Raunkiær's classification, by the position and protection of the renewal buds in the unfavorable season, is described in [7.12.32](/7.12.32): phanerophytes (buds more than 25 cm above the ground, subdivided by height into mega-, meso-, micro- and nanophanerophytes: more than 30 m, 8–30 m, 2–8 m and 25 cm–2 m), chamaephytes (buds above the soil but below 25 cm), hemicryptophytes (buds at the soil surface, aerial parts dying back), cryptophytes or geophytes (buds below ground in bulbs, tubers or rhizomes, or under water) and therophytes (annuals that survive as seeds).

The *life-form spectrum* of a flora or a community is the percentage of its species in each life form, computed from a complete species list. Comparing spectra reveals climate (Figure 1): phanerophytes dominate in humid tropical regions (61 % in the Seychelles, against 46 % in Raunkiær's "normal spectrum" of about 1000 species drawn at random from world floras); hemicryptophytes dominate where a long cold season kills aboveground shoots (50 % in Denmark, 60 % in Spitsbergen, where chamaephytes protected by snow are also frequent); therophytes, which avoid drought as seeds, dominate in deserts and in regions with a long dry summer (42 % in the Libyan desert and in Mediterranean Italy). Within China, the proportion of phanerophytes declines from tropical rain forest through subtropical evergreen broad-leaved forest and temperate deciduous forest to boreal coniferous forest, and therophytes increase toward the arid northwest. Spectra are usually counted by species; weighted by cover or biomass they describe the vegetation rather than the flora.

![Raunkiær life-form spectra (percentages of species): the normal spectrum and five regions with different climates. Phanerophytes dominate the humid tropics (Seychelles), hemicryptophytes regions with a long cold season (Denmark, Spitsbergen), therophytes regions with long dry seasons (Libyan desert, Mediterranean Italy). Data: Raunkiær's classic spectra, as compiled in Chinese ecology textbooks](./plots/life-form-spectra.py)

Similar climates on different continents produce similar life forms through convergent evolution: the stem succulents of American cacti and African euphorbias, the sclerophyllous shrubs of Mediterranean climates in California, Chile, South Africa and Australia. Species that occupy similar niches in similar communities of different regions are called *ecological equivalents*. Life forms are a key to the classification of vegetation at the highest levels ([7.19.41](/7.19.41)), because they reflect the climate rather than the flora.

Animals also have life forms, defined by mode of locomotion and life: flyers (bats), gliders (flying squirrels), swimmers (whales, seals), burrowers (moles) and runners (deer, horses), each with corresponding morphology, physiology and behavior. Animal life forms do not determine the physiognomy of terrestrial communities, but they structure animal communities: in fish of coral reefs, for example, body shape and fin design correspond to positions in the water column and to feeding modes. In aquatic communities the plankton forms no large structure, and only benthic communities, such as coral reefs and beds of sea fans, have a physiognomy built by animals.

### 32.1.2. Synusiae

**Definition 32.1.1 (Synusia)** A **synusia** is a structural part of a plant community composed of species of the same life form or of similar ecological requirements, which occupies a particular space in the community and has its own microenvironment; it is a "functional community" within the community.

The term was introduced by Gams (1918), who distinguished three levels: synusiae of the first order (stands of one species, that is, populations), of the second order (species of one life form) and of the third order (associations of several life forms, that is, communities). The modern concept corresponds to Gams's second order. The Russian geobotanist Sukachev emphasized that each synusia has a characteristic composition, a common ecology and biology of its species, and, above all, its own microenvironment, which is part of the environment of the whole community. A mixed coniferous–broad-leaved forest in northeastern China consists of five main synusiae: evergreen coniferous trees (*Pinus*, *Picea*, *Abies*), deciduous broad-leaved trees (*Acer*, *Tilia*, *Betula*, *Populus*, *Ulmus*), deciduous shrubs, perennial herbs, and mosses and lichens. A synusia is not the same as a layer: coniferous and broad-leaved trees form two synusiae in one tree layer, and only in a layer occupied by a single life form do layer and synusia coincide. Spring ephemerals of a deciduous forest, which flower and fruit before the canopy closes, form a synusia separated from the summer herbs in time rather than in space.

## 32.2. Vertical, Horizontal and Temporal Structure

### 32.2.1. Vertical Structure

**Definition 32.2.1 (Stratification)** The **stratification** of a community is its vertical division into layers occupied by organisms of different height or rooting depth (in plants) or by organisms that live at different heights or depths (in animals).

In forests the layers are usually the tree (canopy) layer, a subcanopy, the shrub layer, the herb layer and the ground layer of mosses and lichens; climbers and epiphytes, which belong to no layer, are interlayer plants. Stratification is primarily a consequence of light: the canopy absorbs most of the incoming radiation, and light decreases roughly exponentially with leaf area index below it (the **Beer–Lambert law** of [7.19.3](/7.19.3)), so that each layer is occupied by species adapted to the light it receives, from sun plants above to shade-tolerant plants below ([7.12.32](/7.12.32)). The arrangement of layers is ultimately determined by the life forms of the species. Stratification is clearest in temperate deciduous forests, simpler in boreal coniferous forests (a dense evergreen canopy and a moss layer), and most complex in tropical rain forests, where emergent trees rise above a continuous canopy and several lower tree layers grade into each other. Forestry calls the aboveground layering of a forest its stand structure: single-storied or multistoried.

Communities are also stratified below ground: roots of different species reach different depths, the largest root biomass is usually near the surface, and roots extend deeper in drier climates. Stratification increases the efficiency with which a community uses light, water and nutrients and the amount of organic matter it produces, and the complexity of stratification is a good indicator of environmental conditions; it is a product of competition and selection among species and of the environment they create.

Animals are stratified too, mainly because the layers offer different food and secondarily because they have different microclimates. MacArthur (1958) showed that five species of warblers (*Setophaga*) that feed in the same spruce trees in New England forage in different parts of the crowns: the Cape May warbler mostly in the outer tips near the top, the bay-breasted warbler in the middle, the yellow-rumped warbler in the lower parts and on the ground, a vertical partitioning that reduces competition ([7.19.23](/7.19.23)). Soil animals are stratified by depth in litter and soil.

Lakes are stratified physically. In summer a temperate lake forms an upper warm, mixed layer (epilimnion), a layer of rapidly decreasing temperature (metalimnion, containing the **thermocline**) and a cold, dense bottom layer near $4\,^\circ\mathrm{C}$ (hypolimnion), above the sediments (**thermal stratification**, [7.19.3](/7.19.3)). Plankton are distributed vertically according to light, temperature, food and oxygen; many zooplankton species migrate daily, descending to deep dark water by day, where visual predators cannot see them, and rising to feed on phytoplankton near the surface at night (diel vertical migration), and their distribution changes with the seasons.

### 32.2.2. Horizontal Structure

Within a community the individuals of each species are distributed unevenly in space, and the community shows a patchwork structure.

- A mosaic is the horizontal differentiation within one community: patches dominated by different synusiae or species, each forming a small community (microcoenosis), with dimensions of decimeters to meters, within which neighboring plants interact.
- A *complex* is the interspersion of fragments of different communities, with patches of meters to tens of meters, for example of steppe and meadow on a slope with small depressions.

The causes are the dispersal and growth habits of the species (clonal spread, seed shadows, [7.19.16](/7.19.16)), the heterogeneity of the environment (microtopography, soil compaction, moisture, salinity, depth and stoniness, light gaps, the activity of animals and people) and the interactions among species (facilitation, competition, allelopathy). The more heterogeneous the environment, the more complex the horizontal structure. The spatial pattern of individual species, random, regular or clumped, is analyzed with the methods of [7.19.8](/7.19.8).

### 32.2.3. Temporal Structure

Many environmental factors vary with a regular rhythm, daily and seasonal, and so do the composition and structure of communities. The *physiognomy* of a community, its overall appearance, determined by the life forms and synusiae of its dominants, is the first criterion for recognizing vegetation types (forest, grassland, desert; and within forests, coniferous, deciduous broad-leaved, evergreen broad-leaved, rain forest). Its seasonal variation is the *seasonal aspect*: a temperate steppe shows four or five aspects a year, as different species flower in sequence. The timing of biological events is the subject of **phenology** ([7.19.4](/7.19.4)). Animals add to the temporal structure through migration, hibernation and aestivation ([7.19.19](/7.19.19)) and through daily rhythms: the diurnal and nocturnal faunas of a forest are almost distinct communities.

## 32.3. Ecotones and Edge Effects

Some communities are separated by clear boundaries, at the edge of a lake, where soils change abruptly (outcrops of serpentine or limestone), or where people have cut a forest; most grade into each other.

**Definition 32.3.1 (Ecotone)** An **ecotone** is a transition zone between two or more communities (or between biomes), whose characteristics are determined by the spatial and temporal scale and the strength of the interactions between the adjacent systems.

Ecotones occur at all scales: the forest–grassland transition of a woodland edge, the alpine treeline, the forest–steppe zone between the boreal forest and the steppes, the mangroves and salt marshes between land and sea. An ecotone often contains species of both adjacent communities, together with species characteristic of the ecotone itself (edge species), because its environment is heterogeneous and offers more kinds of resources and shelter.

**Definition 32.3.2 (Edge Effect)** The **edge effect** is the tendency for the number of species and the density of some populations to be greater in an ecotone than in the adjacent communities; more broadly, any change in the abiotic conditions or in the biota near the boundary between two habitats.

Leopold (1933) made the edge effect a principle of game management: game species such as deer, grouse and rabbits, which feed in open habitat and shelter in cover, are most abundant where the two interdigitate, and managers increased edge to increase game. Edges also have negative effects, which became evident when forests were fragmented by agriculture and roads (**habitat fragmentation**, [7.19.49](/7.19.49)).

- Nest predation and brood parasitism. Songbirds nesting near forest edges suffer more predation by generalist predators from the open land (crows, jays, raccoons) and more parasitism by brown-headed cowbirds; experiments with artificial nests showed predation rates much higher in small fragments and near edges (Wilcove 1985), with most effects within about 50 m of the edge (Paton 1994). Attractive edges can become an **ecological trap** ([7.18](/7.18)).
- Microclimate. Edges are hotter, drier, windier and brighter than the forest interior. In the Biological Dynamics of Forest Fragments Project near Manaus, Amazonia, edge effects on microclimate, tree mortality and the composition of plant and animal communities penetrated tens to hundreds of meters into the forest, some more than 300 m (Laurance et al. 2002), so that small fragments consist entirely of "edge".
- Species of the forest interior, which avoid edges, decline as the ratio of edge to area increases.

Ecotones are also places where change becomes visible first: shifts of the alpine treeline and of the boundary between tundra and boreal forest are among the indicators of climate warming. The ecology of edges and of the patches they bound is continued in landscape ecology ([7.19.48](/7.19.48)).

## 32.4. Interspecific Association

Do two species occur together more or less often than expected by chance? Positive association may mean that one species depends on the other (a parasite and its host, a nurse plant and its beneficiary, [7.19.29](/7.19.29)) or that both prefer the same conditions; negative association may mean competition, allelopathy or different requirements.

**Definition 32.4.1 (Interspecific Association)** Two species are positively (negatively) *associated* if they occur together in sampling units more (less) often than expected if their occurrences were independent.

Association is assessed from presence and absence in $N$ quadrats, summarized in a $2\times2$ **contingency table** ([3.6.12](/3.6.12)):

| | species B present | species B absent | total |
|---|---|---|---|
| species A present | $a$ | $b$ | $a + b$ |
| species A absent | $c$ | $d$ | $c + d$ |
| total | $a + c$ | $b + d$ | $N$ |

Under independence the expected number of quadrats with both species is $(a + b)(a + c)/N$. The test statistic

$$
\chi^2 = \frac{N(ad - bc)^2}{(a + b)(c + d)(a + c)(b + d)},
$$
with Yates's continuity correction $\chi^2 = N\bigl(\lvert ad - bc\rvert - N/2\bigr)^2/\bigl[(a + b)(c + d)(a + c)(b + d)\bigr]$ for small samples, is compared with the **chi-square distribution** with one degree of freedom (critical value 3.84 at the 5 % level). The sign of $ad - bc$ gives the direction: positive association if $ad > bc$, negative if $ad < bc$. The strength is measured by the association coefficient

$$
V = \frac{ad - bc}{\sqrt{(a + b)(c + d)(a + c)(b + d)}},
$$
the **phi coefficient** of the table, between $-1$ and $1$, with $\chi^2 = NV^2$; Ochiai's index $a/\sqrt{(a + b)(a + c)}$ and Jaccard's index $a/(a + b + c)$, which ignore joint absences ($d$), are alternatives that do not depend on the number of quadrats where neither species occurs.

**Example 32.4.1** In 100 quadrats, species A and B occur together in $a = 30$, A alone in $b = 10$, B alone in $c = 15$, and neither in $d = 45$. The expected number of joint occurrences is $40\cdot45/100 = 18$, far below the observed 30. Then $ad - bc = 1350 - 150 = 1200$, $\chi^2 = 100\cdot1200^2/(40\cdot60\cdot45\cdot55) = 24.2$ (Yates: 22.3), much larger than 3.84, and $V = 1200/\sqrt{5\,940\,000} = 0.49$: a significant, moderately strong positive association. Ochiai's index is $30/\sqrt{40\cdot45} = 0.71$ and Jaccard's $30/55 = 0.55$.

:::

Association depends on the size of the sampling unit: two species that never grow in the same square decimeter (negative association at a fine scale) may both be restricted to the same moist hollows (positive association at the scale of square meters). It also depends on the number of quadrats in which neither occurs: adding plots in unsuitable habitat increases $d$ and creates spurious positive association. For many species, the associations among all pairs are examined with null models that preserve species frequencies and site richness ([7.19.33](/7.19.33)), because with many pairs some will be significant by chance.

## 32.5. Gradients and the Continuum

### 32.5.1. Gradient Analysis

**Definition 32.5.1 (Gradient Analysis)** *Gradient analysis* (direct gradient analysis) describes the abundance of species, and the composition of communities, as functions of environmental gradients measured or chosen by the investigator, such as elevation, moisture or soil pH.

In the classic study of the vegetation of the Great Smoky Mountains, Tennessee, Whittaker (1956) mapped the vegetation types of the mountains (cove forest, hemlock forest, oak–chestnut forest, heath balds, spruce–fir forest and others) on a diagram of elevation against topographic moisture. Seen as types, the vegetation seemed sharply divided. When he plotted the abundance of individual tree species (as percentage of stems) along the moisture gradient at a given elevation, the picture changed: each species had its own bell-shaped distribution, with its own optimum and breadth, the distributions overlapped broadly, and there were no boundaries at which groups of species replaced each other together. Curtis and McIntosh (1951), working on the forests of Wisconsin, arranged stands by a "continuum index" computed from the importance values of species with different positions along a successional and moisture gradient, and reached the same conclusion. These results support Gleason's individualistic concept ([7.19.31](/7.19.31)).

A gradient of species distributions of this kind is called a *coenocline*. Its simplest model is the Gaussian response curve of species $i$:

$$
y_i(x) = h_i\exp\Bigl[-\frac{(x - u_i)^2}{2t_i^2}\Bigr],
$$
with optimum $u_i$, tolerance $t_i$ (the breadth of the ecological amplitude, [7.19.2](/7.19.2)) and maximum abundance $h_i$; on the log scale the response is a parabola, and the model can be fitted by Poisson or logistic regression with $x$ and $x^2$ as predictors (ter Braak and Looman 1986). Real responses are often skewed, flat-topped or bimodal (when a competitor displaces a species from the middle of its range), but the Gaussian model captures the essential feature: species respond individually and turn over along gradients. The rate of turnover is a measure of **beta diversity** along the gradient; Whittaker measured it in "half-changes", the distance along the gradient over which the similarity of samples falls by half.

The main weakness of gradient analysis is that the choice of the gradient is subjective. The investigator chooses a factor that appears to matter and arranges the species along it, but the factor may merely be correlated with what really matters. Ordination (Section 32.7) lets the data reveal the main gradients of composition, which are then interpreted.

![A simulated coenocline and three ordinations of the same 40 sites (colours from purple to yellow: true position on the gradient). A: Gaussian responses of 20 species along one gradient. B: principal component analysis bends the gradient into a horseshoe, the two ends folding toward each other. C: correspondence analysis bends it into an arch, the second axis being a quadratic function of the first and the ends compressed. D: one-dimensional nonmetric multidimensional scaling of Bray–Curtis dissimilarities recovers the order of the sites almost exactly (Spearman correlation 0.999 with the true positions)](./plots/coenocline-ordination.py)

## 32.6. Classification of Communities

### 32.6.1. Two Approaches

Two ways of describing many communities correspond to the two concepts of [7.19.31](/7.19.31). If communities are discrete units, they can be classified like species, into types with names and hierarchical ranks (the association unit theory, or organismic approach). If they vary continuously, it is better to arrange them along gradients, by ordination. In practice vegetation has both continuous and discontinuous aspects: ordination emphasizes continuity and classification discontinuity, but an ordination in which samples form separate clusters also classifies, and a classification that allows overlap also shows continuity, so the two are best used together. Classification remains indispensable for maps, inventories and conservation planning, which need named units.

### 32.6.2. The Chinese Vegetation Classification

Chinese vegetation science, influenced by the Russian school, classifies plant communities by their combined characteristics: species composition, physiognomy and structure, geographic distribution, dynamics and habitat, with different emphasis at different ranks. The higher units are based on physiognomy, structure and ecological–geographic characteristics, the middle and lower units on species composition.

**Definition 32.6.1 (Units of Vegetation Classification)** The principal units of the Chinese system are three, with auxiliary units above and below each:

- a *vegetation type group* unites communities whose constructive species have similar life forms (in a broad sense) and whose physiognomy is similar (coniferous forest, broad-leaved forest, grassland, desert); a **vegetation type** unites communities whose constructive species have the same or similar life forms and similar relations to heat and water (cold-temperate coniferous forest, deciduous broad-leaved forest, temperate steppe); vegetation subtypes are distinguished within a type by dominant or indicator synusiae, reflecting climatic subzones or substrate (temperate steppe: meadow steppe, typical steppe and desert steppe, from semi-humid to arid);
- a formation group unites, within a type or subtype, formations whose constructive species are closely related (of one or related genera), have similar life forms or similar habitats (bunchgrass meadow steppe, rhizomatous-grass meadow steppe, forb meadow steppe); a **plant formation** unites communities with the same constructive species or co-constructive species (all communities dominated by *Stipa grandis* form the *Stipa grandis* formation; others are the *Larix gmelinii* formation and the *Leymus chinensis* formation); subformations are distinguished in formations of wide ecological amplitude by subdominant synusiae and habitat (in the *Leymus chinensis* steppe formation: *L. chinensis* with mesophytic forbs, or meadow steppe; with xerophytic bunchgrasses, typical steppe; with saline mesophytic forbs, saline steppe);
- an association group unites associations with similar synusial structure and the same dominants or co-dominants in the dominant and subdominant synusiae; the **plant association** is the basic unit, comparable to the species in taxonomy, and unites communities with the same synusial structure and the same dominants or co-dominants in every synusia (*L. chinensis* + *S. grandis* + *Carex korshinskyi* steppe and *L. chinensis* + *S. grandis* + *Bupleurum scorzonerifolium* steppe are different associations); subassociations reflect small differences within an association caused by habitat or age.

Associations are named by listing the dominant or constructive species of each layer from top to bottom, joined by "–" between layers and "+" between co-dominants of one layer, preceded by "Ass.": Ass. *Larix gmelinii* – *Rhododendron dauricum* – *Pyrola incarnata* is a larch forest with an understory of rhododendron and a herb layer of red-flowered wintergreen. If the uppermost layer is not dominant but a companion species, "<" is used. Formations are named after their constructive species (Form. *Leymus chinensis*; Form. *Castanopsis chinensis* + *Cryptocarya chinensis* for a co-dominated subtropical forest), and units above the formation by physiognomy and ecology.

On this basis *Vegetation of China* (1980) divided the vegetation of the country into 10 vegetation type groups (coniferous forest; broad-leaved forest; scrub and grass-scrub; steppe and savanna; desert, including succulent thorn scrub; tundra; alpine sparse vegetation; meadow; swamp; aquatic vegetation), 29 vegetation types and more than 560 formations, with innumerable associations. A revised system with updated units and criteria was published by Guo et al. (2020). Other schools differ. The Zürich–Montpellier school of Braun-Blanquet (1928) classifies by floristic composition alone, from associations up to classes, by arranging relevé tables to find character species and differential species, and dominates European phytosociology. The Anglo-American school of Clements and Tansley classified communities by their successional relations, distinguishing climax communities from the seral stages that lead to them ([7.19.36](/7.19.36)).

### 32.6.3. Numerical Classification

Since the 1960s, computers have made it possible to classify communities objectively from quantitative data. The steps are: choose the sampling units and the attributes (presence, cover, importance value), transform and standardize the data, compute a similarity or dissimilarity between every pair of samples, and group the samples.

- Dissimilarities: for presence–absence data, the **Jaccard distance** or the Sørensen dissimilarity; for abundance data, the **Bray–Curtis dissimilarity** $\sum_k\lvert y_{ik} - y_{jk}\rvert/\sum_k(y_{ik} + y_{jk})$ ([7.8.14](/7.8.14)), which ignores joint absences, ranges from 0 to 1 and is preferred to Euclidean distance for species data, because two sites that both lack a species are not thereby similar.
- Agglomerative **hierarchical clustering** ([3.4.11](/3.4.11)) repeatedly merges the two most similar groups and records the result in a **dendrogram**; groups are defined by cutting it at a chosen level. Average linkage (UPGMA), which joins groups at the mean dissimilarity between their members, and Ward's method are common in ecology.
- Divisive methods split the samples successively; TWINSPAN (two-way indicator species analysis, Hill 1979) divides along the first axis of a correspondence analysis and identifies indicator species for each division, imitating the phytosociological table.

The rotifer communities of 31 lakes on the North Island of New Zealand were classified in this way into eight groups. Lakes in the same group were not necessarily close to each other, so the classification was not a disguised map, and it required no prior choice of the environmental factors that might matter; the groups were then related to the lakes' trophic state (Duggan et al. 2001). Numerical classification is also used to test traditional classifications, many of which it has largely confirmed.

![Numerical classification of 30 simulated samples from three community types (squares: true type). A: the site-by-species abundance matrix in the order of the dendrogram (shading: log(1 + n)). B: UPGMA dendrogram of Bray–Curtis dissimilarities; cutting at 0.6 recovers the three types](./plots/cluster-dendrogram.py)

## 32.7. Ordination

### 32.7.1. The Idea

**Definition 32.7.1 (Ordination)** *Ordination* arranges sampling units (sites, samples) in a low-dimensional space so that units similar in species composition lie close together and dissimilar units far apart; the axes of the space are then interpreted as the main gradients of community composition.

The term goes back to Ramensky (1930, German *Ordnung*), and was introduced in English by Goodall (1954). Geometrically, each sample is a point in a space with one axis per species; ordination projects this cloud of points onto two or three axes that preserve as much of its structure as possible. Arranging samples by species is normal (Q) analysis; arranging species by their occurrence in samples is inverse (R) analysis. Ordination of samples by their composition alone, followed by interpretation of the axes in terms of environment, is *indirect ordination* (indirect gradient analysis); arranging samples by measured environmental variables is direct gradient analysis (Section 32.5); constrained ordination combines the two.

### 32.7.2. Methods of Indirect Ordination

- Polar ordination (Bray and Curtis 1957), of the Wisconsin school, chooses the two most dissimilar samples as the ends of an axis and places every other sample by its dissimilarities to them. It is simple and, because the endpoints are chosen by the investigator, sometimes handles nonlinear data well, but it has been largely replaced.
- **Principal component analysis** ([3.4.5](/3.4.5)) finds orthogonal axes of maximal variance of the species abundances, which are linear combinations of the species. Yang Hanxi (1981) ordinated 40 plots of 32 species of *Leymus chinensis* steppe in Hulunbuir, Inner Mongolia, by PCA; the first two components (44.3 % of the variance) separated three clusters, corresponding to three association groups. PCA assumes that species respond linearly to the gradients, which is true only for short gradients. Along a long gradient, species with Gaussian responses appear and disappear, sites at the two ends have no species in common, and PCA bends the gradient into a horseshoe whose ends curve toward each other, so that distant sites appear close (Figure 2B).
- **Correspondence analysis** (reciprocal averaging; Hill 1973), derived for contingency tables ([3.4](/3.4)), assumes unimodal responses: site scores are weighted averages of species scores and vice versa, and the first axis maximizes the dispersion of species scores. It recovers the order along a single long gradient well, but its second axis is often a quadratic function of the first, the *arch effect*, and the ends of the axis are compressed (Figure 2C).
- Detrended correspondence analysis (DCA; Hill and Gauch 1980) removes the arch by dividing the first axis into segments and centering the second axis within each, and rescales the axes so that species turnover is uniform, in units of standard deviations of species response: a gradient of 4 SD corresponds approximately to a complete turnover of species. DCA was the most popular ordination of the 1980s and 1990s, and its gradient length is still used to decide between linear methods (PCA, RDA; for gradients shorter than about 3 SD) and unimodal methods (CA, CCA; for longer ones). Its detrending is an arbitrary correction, however, and can distort data with two real gradients.
- **Principal coordinates analysis** and **nonmetric multidimensional scaling** ([3.4.6](/3.4.6)) start from a matrix of dissimilarities, usually Bray–Curtis. PCoA finds coordinates whose Euclidean distances reproduce the dissimilarities as well as possible; NMDS (Kruskal 1964) reproduces only their rank order, minimizing a stress function by iteration, and is the most robust to nonlinear responses. Its axes have no intrinsic meaning and its solution depends on the number of dimensions chosen and on the starting configuration, so several starts are compared (Figure 2D). Differences in composition among groups of samples are tested by **PERMANOVA** ([7.8.14](/7.8.14)).

### 32.7.3. Constrained Ordination and Environmental Interpretation

Since the mid-1980s, community analysis has entered a phase of "environmental interpretation": relating the patterns of composition quantitatively to measured environmental variables. Canonical correspondence analysis (CCA; ter Braak 1986) constrains the axes of correspondence analysis to be linear combinations of environmental variables, so that the ordination shows the variation in composition that the measured environment explains; redundancy analysis (RDA) does the same for PCA. Environmental variables are displayed as arrows whose direction and length show their correlation with the axes, and permutation tests assess their significance.

Two studies show ordination used to generate and to test hypotheses. A CCA of the rotifer communities of 31 New Zealand lakes (78 species) showed that composition varied along a first axis of eutrophication (total phosphorus, chlorophyll, transparency) and a second axis of dissolved oxygen and temperature (Duggan et al. 2002): a predictable association of species occurs under given conditions, and the correlations suggest hypotheses about causes, which correlation alone cannot establish. An NMDS of mallee-heath vegetation at 45 sites in southwestern Australia (305 species) tested the prediction that composition reflects the time since the last fire, and found that recently burned sites differed predictably from sites unburned for longer; an ordination of the same sites by the cover of plant functional traits (resprouting, seed storage, height, longevity) separated the fire-age classes even more clearly (Gosper et al. 2012). Ordination by traits rather than taxa links community structure to function ([7.19.37](/7.19.37)). The success of constrained ordination depends on having measured the relevant variables, which is its main limitation.

## Summary

| Topic | Key points |
|---|---|
| Structural units | **Life form** and life-form spectra (Figure 1: phanerophytes in humid tropics, hemicryptophytes in cold, therophytes in dry climates); ecological equivalents; animal life forms; synusia (Definition 32.1.1), not the same as a layer |
| Vertical structure | Stratification (Definition 32.2.1): forest layers set by light and life forms, root stratification; warblers in spruce; lake layers and diel vertical migration |
| Horizontal and temporal structure | Mosaic vs complex; causes of heterogeneity; physiognomy and seasonal aspect; **phenology** |
| Ecotones | **Ecotone** (Definition 32.3.1); **edge effect** (Definition 32.3.2): more species at edges (Leopold), but nest predation, parasitism and microclimate effects (up to more than 300 m in Amazonia) |
| Association | $2\times2$ table, $\chi^2 = N(ad - bc)^2/[(a+b)(c+d)(a+c)(b+d)]$, $V = $ phi coefficient (Example 32.4.1: $\chi^2 = 24.2$, $V = 0.49$); scale dependence |
| Gradients | Gradient analysis (Definition 32.5.1); Whittaker's Smoky Mountains; Gaussian responses and coenoclines; individualistic continuum |
| Classification | Chinese system: vegetation type group – vegetation type – formation – association (Definition 32.6.1); 10 type groups, 29 types, > 560 formations (1980); naming; Braun-Blanquet; numerical classification with Bray–Curtis and UPGMA |
| Ordination | Definition 32.7.1; polar ordination, PCA (horseshoe), CA (arch), DCA (detrending, SD units), PCoA, NMDS (rank order, stress); CCA, RDA and environmental interpretation |

## Questions

1. Why do life-form spectra reveal climate better than lists of the dominant species? Give an example of two floras with no species in common but similar spectra.

   **Answer** Life forms are adaptations to the unfavorable season, and similar climates select similar forms by convergence regardless of phylogeny, whereas the dominant species depend on the history of the flora. The Mediterranean-climate regions of California and central Chile share few species but both have high proportions of therophytes and of sclerophyllous phanerophytes (chamaephytes and nanophanerophytes); the deserts of North America and southern Africa share no succulents but both have stem succulents and many therophytes.
2. A forest has two tree species in the same canopy layer, one evergreen coniferous and one deciduous broad-leaved. How many layers and how many synusiae does this part of the forest contain? Explain.

   **Answer** One layer, two synusiae. Layers are defined by height, synusiae by life form and ecological requirements; the evergreen conifer and the deciduous broad-leaved tree belong to different life forms with different seasonal behavior and different microenvironments under their crowns, so they form separate synusiae within one layer.
3. In 80 quadrats, species A occurs in 20, species B in 40, and both in 4. Test for association and compute $V$.

   **Answer** $a = 4$, $b = 16$, $c = 36$, $d = 24$. Expected $a$ under independence: $20\cdot40/80 = 10$. $ad - bc = 96 - 576 = -480$. $\chi^2 = 80\cdot480^2/(20\cdot60\cdot40\cdot40) = 18\,432\,000/1\,920\,000 = 9.6 > 3.84$ (Yates: $80\cdot440^2/1\,920\,000 = 8.07$), a significant negative association; $V = -480/\sqrt{1\,920\,000} = -0.35$.
4. Explain why PCA of species abundances along a long gradient produces a horseshoe, and what features of NMDS with Bray–Curtis dissimilarity reduce the problem.

   **Answer** PCA uses Euclidean distances on abundances and finds linear axes. With unimodal responses, samples at the two ends of a long gradient share no species; their Euclidean distance is then not larger than that between moderately distant samples (all are "completely different"), and the configuration that best preserves these distances in two dimensions is curved, with the ends bent back toward the middle. Bray–Curtis dissimilarity ignores joint absences, and NMDS preserves only the rank order of dissimilarities, so saturated values at 1 do not force a curve as strongly; in one dimension the order along the gradient is recovered (Figure 2D), although in two dimensions some bending can remain because dissimilarities saturate.
5. (Open) You have species cover data from 200 plots across a mountain range and measurements of elevation, aspect, soil depth and grazing intensity. Outline an analysis that both classifies the vegetation and relates it to the environment.

   **Answer** Points to cover: transform cover (square root or log) and compute Bray–Curtis dissimilarities; classify by hierarchical clustering (UPGMA or Ward) or TWINSPAN, choose the number of groups (for instance by indicator species analysis or silhouette widths), and name the groups by dominant species in the Chinese convention; ordinate by NMDS (several starts, stress) and overlay the clusters to see whether they are discrete or segments of a continuum; check gradient length by DCA and choose CCA or RDA for constrained ordination with the four variables, test them by permutation, and partition the variance among elevation, soil and grazing; fit Gaussian or GAM response curves for the main species along elevation; beware of spatial autocorrelation and of correlations among predictors (grazing may follow elevation).
