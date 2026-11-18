---
title: "Landscape Ecology I: Structure and Pattern"
description: "The concept of landscape from visual aesthetics to Humboldt, Troll and Forman, its characteristics (regionality, heterogeneity, scale dependence, function) and landscape ecology as the study of structure, function and change; the elements of landscape structure: patches by origin, the relation of species richness to patch area, edge and core, interior and edge species, the geometry of core area with the Brunn-Minkowski bound and the ecologically optimal patch, and the number of patches; corridors by origin and width, line and strip corridors and the hedgerow width threshold, connectivity, curvilinearity and functions; the landscape matrix and its criteria, porosity, boundary shape and networks; models of landscape pattern; the characterization of pattern: heterogeneity, grain and extent with the effect of aggregation, landscape diversity, connectivity and fragmentation, contrast and ecotones, gradients and spatial autocorrelation with Moran's I and the semivariogram; landscape metrics, patch shape and fractal dimension, and neutral landscape models."
---

From a hilltop one sees fields, woods, villages, roads, a river and a marsh fitting together into a mosaic that repeats over the plain. Each element is an ecosystem in its own right, but organisms, water, nutrients and disturbances move between them, and the way they are arranged matters: a forest bird may thrive in one large wood and disappear from the same area of forest divided into twenty small ones. Landscape ecology studies this level of organization, above the ecosystem and below the biome. It was introduced to the course in community ecology, where the **ecotone** and the **edge effect** were defined for the boundary between two communities ([7.19.32](/7.19.32#sec-32.3)), and in population ecology, where the dynamics of **metapopulations** in networks of habitat patches were analyzed ([7.19.16](/7.19.16)). This chapter describes the structure of landscapes: the history and meaning of the concept (48.1), the elements of which landscapes are built, patches, corridors and the matrix (48.2), the overall patterns they form (48.3), and the quantitative description of pattern, including heterogeneity, scale, connectivity, spatial autocorrelation and landscape metrics, tested on neutral landscape models (48.4). The next chapter turns to function and change: percolation, connectivity and its measurement, the effects of fragmentation, disturbance spreading through landscapes and species distribution models ([7.19.49](/7.19.49)).

## 48.1. Landscape and Landscape Ecology

### 48.1.1. The History of the Concept

The word landscape (German *Landschaft*, Dutch *landschap*) first meant scenery, a stretch of country seen from one viewpoint, and the painting of it; the concept was aesthetic and visual. At the beginning of the nineteenth century Alexander von Humboldt (1769–1859), the founder of plant geography and comparative climatology, used it as a scientific concept: the total character of a region of the Earth, formed by climate, water, soil, vegetation and human culture together, a functional unit of the Earth's surface. Other disciplines gave it other meanings; in landscape architecture it remained the overall visual impression of an area, without sharp boundaries, valued for its beauty and the harmony of its parts.

The German geographer Carl Troll (1899–1975), studying land use in East Africa from aerial photographs, introduced the term landscape ecology (*Landschaftsökologie*) in 1939 for the combination of the spatial view of geography, which aerial photography made possible, with the functional view of ecology. For several decades the field developed mainly in central and eastern Europe, as a basis for land-use planning. In North America it emerged in the 1980s, with the book *Landscape Ecology* of Richard Forman and Michel Godron (1986) and the growth of remote sensing and geographic information systems. In *Land Mosaics* (1995), Forman (born 1935) defined a landscape as a mosaic of interacting ecosystems that recurs over a kilometres-wide area, a heterogeneous land unit at intermediate scale, and, at the scale of a region, the basic structural unit that does not overlap with others and contrasts strongly with its neighbours.

### 48.1.2. Definition and Characteristics

**Definition 48.1.1 (Landscape)** A **landscape** is a spatially heterogeneous area, typically several to many square kilometres, composed of a cluster of interacting ecosystems (forests, fields, wetlands, settlements, waters) that is repeated in similar form throughout it.

The definition fixes the composition, not the size: for a beetle a landscape may be a few square metres of meadow, for a wolf hundreds of square kilometres. Landscapes have four characteristics:

1. Regionality: a landscape is a concrete area of the Earth's surface with a particular combination of natural and human elements.
2. Heterogeneity: the structure, pattern, function and dynamics of a landscape are uneven in space and time. Heterogeneity measures the variability and complexity of a landscape, and its study distinguishes landscape ecology from earlier ecology, which often assumed homogeneous systems.
3. Scale dependence: as the scale of observation changes, the dominant patterns and processes and their controlling factors change (the scale effect). Landscape ecology pays great attention to scale, so that a question is not posed at a scale at which the answer is biased (48.4.2).
4. Function: a landscape supports the organisms living in it and provides goods and services to people through the flows of energy, matter, organisms and information among its elements.

**Definition 48.1.2 (Landscape Ecology)** **Landscape ecology** is the study of the spatial structure, the interactions and functioning, and the change through time of landscapes; above all of the causes and ecological consequences of spatial heterogeneity across scales.

Landscape ecology has three objects of study (Forman and Godron 1986):

- Landscape structure: the kinds, number, sizes, shapes and spatial arrangement of the elements of a landscape, and their diversity.
- Landscape function: the interactions between structure and ecological processes, the flows of energy, materials and species among the elements.
- Landscape change: the alteration of structure and function over time.

It emphasizes the maintenance and development of spatial heterogeneity, interactions among ecosystems, the conservation and management of populations over large regions, the management of environmental resources, and the effects of people on landscapes. It is therefore close to applied fields: land-use planning, nature reserve design, urban ecology, and ecological restoration, in which the landscape is the unit at which most decisions are made.

## 48.2. Landscape Elements

Landscape structure can be described by three kinds of elements (Forman and Godron 1986): patches, corridors and the matrix. They are defined relative to one another and to the organism or process of interest, and their definitions depend on scale: a forest patch for a bird may be the matrix for a beetle that never leaves it.

### 48.2.1. Patches

**Definition 48.2.1 (Patch)** A **patch** is a relatively homogeneous, nonlinear area that differs in appearance or composition from its surroundings, for example a wood surrounded by fields, a pond in a meadow or a village in farmland.

Patches can be classified by land cover (forest, grassland, wetland, cropland, built-up land) or by origin:

| Type | Origin | Examples | Dynamics |
|---|---|---|---|
| Disturbance patch | A small area of the matrix disturbed | Windthrow gap, burned area, clear-cut, beaver meadow | Short-lived; succession returns it to the matrix |
| Remnant patch | An undisturbed area left after widespread disturbance of the matrix | Unburned grove in a burned forest, woodlot in farmland | Loses species after isolation (relaxation) |
| Environmental resource patch | Local difference in environment or resources | Oasis in a desert, wetland on poorly drained soil, outcrop of serpentine | Long-lived, stable |
| Introduced patch | Planting or construction by people | Plantation, orchard, golf course, village | Maintained by people |
| Regenerated patch | Succession on a disturbed area surrounded by disturbed land | Regrowing forest on an abandoned field | Like remnant patches but younger |
| Ephemeral patch | Brief normal fluctuation of a biotic or abiotic factor | Temporary pond, aggregation of animals, ephemeral flowering | Very short-lived |

The number of species in a patch increases with its area, as on islands ([7.10.30](/7.10.30); [7.19.34](/7.19.34)), but more factors are involved. Forman (1995) summarized the species richness $S$ of an island as a function $S = f(+\text{habitat diversity}, -\text{disturbance}, +\text{area}, -\text{isolation}, +\text{age})$, the sign giving the direction of the effect, and of a patch in a landscape as $S = f(+\text{habitat diversity}, \pm\text{disturbance}, +\text{area}, +\text{age}, +\text{heterogeneity of the matrix}, -\text{isolation}, -\text{discontinuity of the boundary})$: unlike the sea around an island, the matrix around a patch can supply species and be partly used by them, and moderate disturbance can increase richness ([7.19.33](/7.19.33)). Large patches contain more habitats, larger populations with a lower risk of extinction, and species that need large territories (raptors, large carnivores); small patches can serve as stepping stones for dispersal and contain species absent from large patches. Conservation planners combine both ([7.19.34](/7.19.34) discusses the SLOSS debate).

The boundary of a patch differs from its interior. Near the boundary light, temperature, wind, humidity, predators, brood parasites and invasive plants penetrate from the surrounding land; this edge zone has a depth $d$ of tens to hundreds of metres, depending on the factor ([7.19.32](/7.19.32#sec-32.3)). Species that live mainly in the interior, away from the boundary, are interior species; those that prefer the edge zone are edge species. The ratio of interior (core) area to edge area, the interior-to-edge ratio, depends on the size and shape of the patch. When a patch is enlarged, its core grows faster than its edge; when it shrinks, its core shrinks faster than its edge; and a patch that is very small or very narrow consists entirely of edge and contains only edge species and species insensitive to habitat quality. The geometry can be made exact.

**Proposition 48.2.1 (Core Area of a Convex Patch)** Let a patch be a convex region of area $A$ and perimeter $P$, and let its core be the set of points at a distance greater than $d$ from the boundary, with area $A_{\mathrm{c}}$. Then

$$
A - Pd \le A_{\mathrm{c}} \le \bigl(\sqrt{A} - d\sqrt{\pi}\bigr)^2 \quad \text{if } A \ge \pi d^2,
$$
and $A_{\mathrm{c}} = 0$ if $A \le \pi d^2$. The upper bound is attained only by the disk.

**Proof** Let $K$ be the patch and $K_{-t}$ the set of its points at distance greater than $t$ from the boundary; for convex $K$ each $K_{-t}$ is convex and $K_{-t} \subseteq K$, so its perimeter $P(K_{-t}) \le P$. By the coarea formula, since the distance to the boundary has gradient of length 1, $A - A_{\mathrm{c}} = \int_0^d P(K_{-t})\,\mathrm{d}t \le Pd$, the lower bound. For the upper bound, every point of the core is the centre of a disk of radius $d$ contained in $K$, so $K$ contains the Minkowski sum $K_{-d} + dB$ of the core and a disk of radius $d$. By the Brunn–Minkowski inequality in the plane, $\sqrt{\lvert X + Y\rvert} \ge \sqrt{\lvert X\rvert} + \sqrt{\lvert Y\rvert}$ for compact sets $X, Y$, hence $\sqrt{A} \ge \sqrt{A_{\mathrm{c}}} + \sqrt{\pi d^2}$, which gives the bound and shows that the core is empty unless $A > \pi d^2$. Equality in the Brunn–Minkowski inequality for convex sets holds only for homothetic sets, so it requires $K_{-d}$ to be a disk and $K$ the concentric disk of radius larger by $d$. For the disk of radius $R$, $A_{\mathrm{c}} = \pi(R - d)^2 = (\sqrt{A} - d\sqrt{\pi})^2$. $\square$

Among all convex patches of given area the circle therefore has the largest core, and the core of an elongated patch is smaller: a rectangle with sides $a \ge b$ has core $(a - 2d)(b - 2d)$, which vanishes when $b \le 2d$ however long the rectangle is. Since the lower bound involves the perimeter, the ratio $P/(2\sqrt{\pi A})$ of the perimeter to that of a circle of the same area, the shape index of Patton (1975), measures how much a shape departs from compactness: Bowen and Burgess (1981) found median shape indices of forest patches in Ohio landscapes from 1.16, nearly circular, to 1.6, elongated.

![Edge and core of habitat patches with an edge effect penetrating 100 m. A: four patches of 20 ha each, with the edge zone (yellow) and the core (green) computed on a 2 m raster: the circle keeps 37% of its area as core, the square 30%, a 4:1 rectangle 8% and a lobed shape 7%. B: the core fraction against patch area for circles, squares and rectangles of aspect ratio 4 and 16 (dotted line: 20 ha). The circle attains the upper bound of Proposition 48.2.1; elongated patches have no core at all below several tens of hectares, and even patches of 1000 ha lose 10–30% of their area to edge.](./plots/patch-core-area.py)

Shape also affects exchanges with the surroundings: the more convoluted the boundary, the more interaction between the patch and the matrix, the more edge habitat and the fewer interior species. Forman (1995) described the ecologically optimal patch as a compromise: a large, roughly round core that protects the interior and its resources, a boundary with some curvilinear lobes that offer edge habitat, and a few narrow fingers extending into the surroundings that help organisms to disperse in and out.

The number of patches matters too. In general a landscape should keep many patches of a habitat, because the loss of patches usually means a loss of habitat, and because fewer patches mean smaller **metapopulations**, with a higher probability that local populations go extinct and a lower probability that empty patches are recolonized, so that the metapopulation as a whole becomes less stable ([7.19.16](/7.19.16)).

### 48.2.2. Corridors

**Definition 48.2.2 (Corridor)** In landscape ecology, a **corridor** is a linear or strip-shaped landscape element that differs from the land on both sides, such as a hedgerow, a windbreak, a strip of riparian forest, a river, a road or a power line.

The term was introduced in biogeography for routes of continuous habitat between regions ([7.17.69](/7.17.69)); in landscapes it refers to linear elements at a smaller scale. Corridors can be classified by their composition (forest or green corridors, river corridors, road corridors) and, like patches, by their origin: disturbance corridors (a power line through a forest), remnant corridors (a strip of forest left along a stream), environmental resource corridors (a river), introduced or planted corridors (hedgerows, windbreaks, roads) and regenerated corridors (a strip of regrowth along a fence). By width they are divided into:

- line corridors, narrow strips dominated by edge species and strongly influenced by the adjacent land, such as roads, paths, ditches and narrow hedgerows;
- strip corridors, wide enough to have an interior environment with interior species, and edge effects on each side.

The width effect is the dependence of the functions of a corridor on its width. In a frequently cited analysis of the herbaceous flora of hedgerows, very narrow hedgerows (less than 3 m) had almost neither interior nor edge species, hedgerows of 3–12 m contained most edge species but few interior species, and in hedgerows wider than 12 m the number of edge species changed little while the diversity of interior species was more than twice that of narrower ones. For the herbaceous plants of hedgerows, about 12 m is thus a threshold of the width effect, separating line corridors from strip corridors; for forest birds or mammals the required widths are much larger, often hundreds of metres. From the edge depth $d$ of Proposition 48.2.1, a strip has interior habitat only if it is wider than $2d$.

The structure of a corridor determines its use. Its connectivity is measured by the number and length of gaps (breaks) per unit length; gaps impede movement along the corridor to a degree that depends on the mobility of the species, the length of the gap, the contrast between the gap and the corridor, and the sensitivity of the species to that contrast. Its curvilinearity matters: the straighter and shorter a corridor, the faster energy, materials and organisms move through it, but bends provide habitat, shelter species moving along it from the surrounding matrix, and create more heterogeneous habitats, raising the diversity of the corridor itself. Corridors have several functions: they are conduits for movement, habitats (and so sources or sinks of individuals), filters or barriers for organisms crossing them (a road, a fence, a river), and aesthetic and recreational elements of the landscape. Whether corridors increase the movement of organisms between patches enough to justify their cost is an empirical question taken up in [7.19.49](/7.19.49), with the design of wildlife crossings.

### 48.2.3. The Landscape Matrix

**Definition 48.2.3 (Landscape Matrix)** The **landscape matrix** is the most extensive and most connected landscape element, the background in which patches and corridors are embedded, and the element that plays the dominant role in the dynamics of the landscape.

Three criteria are used to identify the matrix (Forman and Godron 1986):

1. Relative area: the matrix covers more area than any other element, usually more than half of the landscape.
2. Connectivity: the matrix is more connected than any other element. An element that is completely connected, forming a network that surrounds all other elements, is regarded as the matrix even if its area is less than half.
3. Control over dynamics: the matrix controls the dynamics of the landscape more than any other element, for instance as the source of seeds that recolonize disturbed patches or of the fires that spread through it.

When the criteria disagree, area is applied first, then connectivity, then control. In a landscape of fields with scattered woods the fields form the matrix; in a forest with clearings the forest does.

The matrix has its own structural properties. Its porosity is the number of patches (holes) per unit area, independent of their size; only patches with closed boundaries are counted. Porosity indicates the degree of isolation of the species of the patches and of their potential genetic differentiation, and it is an aggregate measure of edge effects: a matrix with low porosity is important for animals that must stay away from edges, such as interior forest species when clearings are cut into a forest. The boundary shape of the matrix affects its interaction with the patches: shapes with the smallest perimeter-to-area ratio, such as circles, limit the exchange of energy and matter between the matrix and the patches, and convoluted boundaries promote it. When porosity is high, the matrix becomes a network of corridors, composed of nodes (patches at the intersections) and links (the connecting corridors), whose topology, the number of loops and the connectivity of the nodes, can be analyzed with the tools of graph theory ([1.4.6](/1.4.6); [7.19.49](/7.19.49)).

## 48.3. Landscape Pattern

Landscape pattern is the spatial arrangement of landscape elements of different sizes and shapes: the kinds and numbers of elements and their spatial distribution and configuration. Patches of one type may be distributed at random, regularly or in clumps over the landscape. Three conceptual models are used to describe and analyze pattern, qualitatively and quantitatively:

- The patch–corridor–matrix model (Forman 1995) describes a landscape by the composition and spatial configuration of its patches, corridors and matrix. It is the basis of most landscape planning and of the landscape metrics of 48.4.7.
- The corridor–network model focuses on the network formed by the corridors of a landscape and analyzes and simulates its connectivity, using graph theory and models of movement.
- The boundary–ecotone–gradient model recognizes that boundaries between landscapes, and between landscape elements, can be sharp or gradual: sharp linear boundaries and wide gradual transitions coexist in real landscapes, and which one is seen depends on the scale of observation and analysis. Many environmental variables change continuously (the gradient model of McGarigal and Cushman 2005), and treating them as discrete patches loses information.

## 48.4. Characterizing Landscape Pattern

### 48.4.1. Heterogeneity

Heterogeneity is the central concept of landscape ecology: spatial heterogeneity of the environment at different scales drives biological and physical processes in space, and these processes in turn shape the spatial patterns of the environment and of organisms. Three aspects are distinguished:

- Spatial heterogeneity, the uneven distribution of the elements or properties of a landscape in space, horizontal (a mosaic of patches) or vertical (layers of vegetation and soil).
- Temporal heterogeneity, the variation of the landscape in time, the subject of landscape dynamics.
- Functional heterogeneity, the varied effects of the many ecological entities of a landscape (individuals, populations, communities, ecosystems) on ecological processes and functions; two landscapes with the same map can differ greatly in how organisms use them.

### 48.4.2. Grain and Extent

**Definition 48.4.1 (Grain and Extent)** The spatial scale of an observation or a map is characterized by its **grain**, the size of the smallest unit of observation (the resolution: a quadrat, a pixel of an image), and its **extent**, the size of the whole area observed.

Coarse grain means large units and low resolution; fine grain means small units and high resolution. The two determine what can be seen. For a fixed extent, coarsening the grain blurs the details, small patches disappear, boundaries are smoothed, and the landscape appears more homogeneous; for a fixed grain, increasing the extent includes more kinds of patches and the landscape may appear more heterogeneous. Ecological processes have characteristic scales too, and a pattern measured at an arbitrary grain may have nothing to do with the scale at which organisms perceive their environment. The figure shows a simple case: when a map is aggregated by majority rule, as happens when remote sensing data of coarser resolution are classified, the number of patches falls by orders of magnitude, edge density falls, and even the proportion of the rarer habitat type decreases, because small patches of it are absorbed by the surrounding majority. Landscape metrics are therefore comparable only when computed at the same grain and extent.

![The effect of grain on measured landscape pattern. A fractal neutral landscape of 256 × 256 cells (Hurst exponent 0.5, 35% habitat, with fine-scale noise) is aggregated to coarser grains by majority rule. A–C: the map at grains of 1, 4 and 16 cells. D: habitat proportion, number of patches and edge density relative to their values at the finest grain: the number of patches falls by a factor of more than 1000 and edge density by a factor of 40 between grains 1 and 32, and the habitat proportion falls by about a quarter because scattered habitat cells are lost to the majority class.](./plots/grain-effect.py)

The dependence of measured length on the grain of measurement is extreme for convoluted boundaries. Mandelbrot (1967) asked how long the coast of Britain is and showed that the answer depends on the length $\varepsilon$ of the ruler: for a fractal curve of dimension $D$ between 1 and 2, the measured length is $L(\varepsilon) = c\,\varepsilon^{1 - D}$, which increases without limit as $\varepsilon \to 0$. Milne (1993) measured the coastline of Admiralty Island in Alaska and found $D \approx 1.25$. For bald eagles, whose nests are spaced about 0.8 km apart along the shore, the coastline is about 760 km long; for barnacles, which need about 2 cm of shore each, it is more than 11 000 km. Each organism lives in a landscape whose structure is defined at its own grain.

### 48.4.3. Landscape Diversity

Landscape diversity is the diversity and variability of landscape pattern, closely related to heterogeneity: the diversity of the patches of a landscape in number, size, shape, type and distribution, and of their connections. It is considered at three levels:

- Patch diversity: the number, sizes and shapes of the patches of a landscape and their complexity.
- Patch type diversity: the richness of patch types and the relative areas they occupy, measured, like the diversity of species ([7.19.31](/7.19.31)), by the number $m$ of types and by indices such as the **Shannon index** $H = -\sum_{i=1}^{m} p_i\ln p_i$, where $p_i$ is the proportion of the landscape covered by type $i$, and its evenness $H/\ln m$.
- Pattern diversity: the diversity of the spatial arrangement of patch types, of the connections among patches of the same type, and of the aggregation or dispersion of adjacent patches.

Patch type diversity affects species diversity. Species that need two or more habitats during their daily or annual cycle, such as amphibians that breed in ponds and live in woods, or birds that nest in hedgerows and feed in fields, require landscapes in which these habitats are near each other; such landscape complementation means that a mixed landscape supports more species than either habitat alone. But the effect is not monotonic: dividing a landscape into ever more patch types reduces the area of each, and interior species of the dominant habitat disappear.

### 48.4.4. Connectivity and Fragmentation

**Definition 48.4.2 (Landscape Connectivity)** **Landscape connectivity** is the degree to which a landscape facilitates or impedes the movement of organisms, or of materials, energy or information, among its patches of habitat; structural connectivity refers to the physical continuity of habitat, functional connectivity to the movement of a particular species through the landscape.

**Definition 48.4.3 (Habitat Fragmentation)** **Habitat fragmentation** (landscape fragmentation) is the process, and the resulting state, by which a continuous habitat is broken into smaller and more isolated patches separated by a matrix of different land; it combines loss of habitat area with changes of configuration (more patches, smaller patches, more edge, greater isolation).

Fragmentation can be seen as the negative image of connectivity. Forman (1995) distinguished five spatial processes of land transformation that usually follow one another as a habitat is converted: perforation (holes in a continuous habitat), dissection (the habitat cut by roads or other linear features), fragmentation in the strict sense (division into separate patches), shrinkage (the patches become smaller) and attrition (patches disappear). Habitat loss and fragmentation are the largest causes of the loss of biodiversity on land ([7.19.51](/7.19.51)); how much of their effect is due to the loss of area and how much to the change of configuration is debated, and the next chapter analyzes it with percolation theory ([7.19.49](/7.19.49)).

### 48.4.5. Contrast and Ecotones

Landscape contrast is the degree of difference between adjacent patches in some ecological property relevant to a process, such as the height of vegetation for wind, the temperature of the soil for an ectotherm or the resistance to movement for a mammal. A forest bordering a clear-cut is a high-contrast edge, a forest bordering an old, shrubby field a low-contrast one. Where environmental gradients are gentle and the contrast between adjacent patches is low, a gradual transition zone usually forms, an **ecotone** ([7.19.32](/7.19.32#def-32.3.1)); where they are steep, the boundary is sharp. The width and permeability of a boundary decide how much it filters the movement of organisms and materials, and edges with high contrast produce the strongest **edge effects**.

### 48.4.6. Gradients and Spatial Autocorrelation

A landscape gradient is a regular, gradual change of a landscape property in one or more directions: in elevation, soil nutrients, moisture, temperature, precipitation or human disturbance, from city centre to countryside. Ecotones are typical gradient patterns. An important property of gradients, and of landscapes generally, is spatial autocorrelation.

**Definition 48.4.4 (Spatial Autocorrelation)** **Spatial autocorrelation** is the dependence of the values of a variable at different places on their distance: positive autocorrelation means that nearby places tend to have more similar values than distant ones, negative autocorrelation that they tend to have more dissimilar values.

"Everything is related to everything else, but near things are more related than distant things" (Tobler 1970). Spatial autocorrelation arises from spatially autocorrelated environmental factors (exogenous autocorrelation) and from processes such as dispersal and local interactions (endogenous autocorrelation). It has two consequences: it is information about the scale of the processes that generate pattern, and it violates the independence assumed by standard statistical tests, so that samples that are close together are pseudoreplicates.

Two statistics are used to measure it. **Moran's I** ([7.9.6](/7.9.6#def-6.10.1)) for $n$ observations $x_i$ with spatial weights $w_{ij}$ (for example $w_{ij} = 1$ if $i$ and $j$ are in a given distance class and $0$ otherwise) is

$$
I = \frac{n}{\sum_{i \ne j} w_{ij}}\,\frac{\sum_{i \ne j} w_{ij}(x_i - \bar x)(x_j - \bar x)}{\sum_i (x_i - \bar x)^2},
$$
a correlation coefficient between values at pairs of places; its expectation without autocorrelation is $-1/(n - 1)$, close to $0$. Computed for successive distance classes it gives a correlogram, which typically declines from positive values at short distances to about zero at the distance beyond which values are independent. Geostatistics uses the semivariogram.

**Definition 48.4.5 (Semivariogram)** For a variable $Z$ observed at locations $\boldsymbol{s}$ in a landscape, the **semivariogram** is the function $\gamma(h) = \frac{1}{2}\mathbb{E}\bigl[(Z(\boldsymbol{s}) - Z(\boldsymbol{s} + \boldsymbol{h}))^2\bigr]$ of the distance $h = \Vert\boldsymbol{h}\Vert$, estimated by half the mean squared difference of all pairs of observations separated by about $h$.

**Proposition 48.4.1 (Semivariogram and Covariance)** If $Z$ is second-order stationary and isotropic, with variance $\sigma^2$ and correlation function $\rho(h)$, then $\gamma(h) = \sigma^2(1 - \rho(h))$. In particular $\gamma$ increases from $0$ towards the sill $\sigma^2$ as the correlation decays.

**Proof** $\mathbb{E}[(Z(\boldsymbol{s}) - Z(\boldsymbol{s} + \boldsymbol{h}))^2] = \operatorname{Var}(Z(\boldsymbol{s})) + \operatorname{Var}(Z(\boldsymbol{s} + \boldsymbol{h})) - 2\operatorname{Cov}(Z(\boldsymbol{s}), Z(\boldsymbol{s} + \boldsymbol{h})) = 2\sigma^2 - 2\sigma^2\rho(h)$, since the means are equal. $\square$

A semivariogram is described by three parameters: the nugget, the value extrapolated to $h \to 0$, which reflects measurement error and variation at scales finer than the sampling; the sill, the plateau reached at large distances; and the range, the distance at which the sill is (practically) reached, beyond which observations are uncorrelated. The range estimates the scale of patchiness, and it guides sampling design: samples taken farther apart than the range are effectively independent. Geostatistical interpolation (kriging) uses the semivariogram to predict values at unsampled places.

![Spatial autocorrelation of a landscape variable on a 1 km × 1 km grid of 10 m cells, for two simulated fields (smoothed white noise plus independent measurement error). A, B: fields with short-range and long-range autocorrelation. C: Moran's I correlograms by distance class of 20 m, computed from 3000 randomly sampled cells: positive at short distances, decaying to about zero beyond about 50 m and 300 m respectively. D: empirical semivariograms (points) with fitted Gaussian models (lines); the nuggets reflect the measurement error, the sills the total variance, and the practical ranges, about 56 m and 220 m, the scale of the patches (Proposition 48.4.1).](./plots/spatial-autocorrelation.py)

### 48.4.7. Landscape Metrics

Landscape metrics are numbers that quantify the composition and configuration of a categorical map. Hundreds have been proposed, and the program FRAGSTATS (McGarigal and colleagues, since 1995) computes them at the level of patches, classes (all patches of one type) and the whole landscape. They are highly correlated with each other, and a few kinds suffice for most purposes:

| Aspect | Metric | Definition |
|---|---|---|
| Composition | Percentage of landscape (PLAND) | Area of a class / total area |
| | Shannon landscape diversity (SHDI), evenness (SHEI) | $-\sum_i p_i\ln p_i$; SHDI$/\ln m$ |
| Area and density | Number of patches (NP), patch density | Count; count per unit area |
| | Mean patch size; largest patch index (LPI) | Class area / NP; area of the largest patch / total area |
| Edge | Edge density (ED) | Total length of edge / total area |
| Shape | Shape index | $P/(2\sqrt{\pi A})$ (vector) or $P/(4\sqrt{A})$ (raster), 1 for the most compact shape |
| | Landscape shape index (LSI) | Total edge of a class / minimum possible edge for its area |
| | Perimeter–area fractal dimension | $2\times$ the slope of $\ln P$ against $\ln A$ over patches; 1 for simple, 2 for maximally convoluted shapes |
| Aggregation | Contagion (CONTAG) | $1 + \sum_{i,k} q_{ik}\ln q_{ik}/(2\ln m)$, where $q_{ik}$ is the proportion of adjacent cell pairs of types $i$ and $k$ |
| Isolation | Mean nearest-neighbour distance | Mean distance from each patch to the nearest patch of the same class |
| Core | Core area | Area at distance $> d$ from the edge (Proposition 48.2.1) |

The fractal dimension of patch boundaries follows from Mandelbrot's relation: for patches whose shapes are statistically similar at all sizes, the perimeter measured at a fixed grain scales as $P \propto A^{D/2}$, so $D$ is twice the slope of $\ln P$ against $\ln A$. Patches created by people (fields, plantations) have simple boundaries and $D$ close to 1; natural patches (forest remnants on rugged terrain, wetlands) have more convoluted boundaries. Metrics describe pattern but do not by themselves say anything about process: the same value of edge density can result from very different arrangements, and its ecological meaning depends on the organism. They are most useful for comparing landscapes, or the same landscape over time, at a fixed grain and extent.

### 48.4.8. Neutral Landscape Models

How can one tell whether a pattern is significant? Gardner, Milne, Turner and O'Neill (1987) proposed neutral landscape models: maps generated by a random process with specified properties and no ecological mechanism, against which real landscapes, and the response of ecological processes to pattern, can be compared, as null models are used in community ecology ([7.19.33](/7.19.33)). The simplest is the random map: each cell of a lattice is habitat independently with probability $p$. Random maps are extremely fragmented, with many small patches, and their connectivity changes abruptly near a threshold value of $p$, the percolation threshold ([7.19.49](/7.19.49)). Real landscapes are spatially autocorrelated, and fractal neutral landscapes reproduce this: a continuous random surface with a power-law spectrum, generated by midpoint displacement or by spectral synthesis with a Hurst exponent $H$ between 0 and 1 (low $H$ for rough, fragmented surfaces, high $H$ for smooth, clumped ones), is classified so that a fraction $p$ of the cells becomes habitat (With 1997).

![Neutral landscape models with the same proportion of habitat (40%, green) on 128 × 128 cells: a random map, and two fractal maps generated by spectral synthesis with Hurst exponents H = 0.2 (rough) and H = 0.8 (smooth). Below each map: number of patches (NP, 4-connected), largest patch index (LPI), edge density (ED, edges per cell), landscape shape index of the habitat class (LSI) and contagion. With habitat amount fixed, configuration changes the number of patches by a factor of 60, edge density by a factor of 10 and the size of the largest patch (red outline) by a factor of 50; composition metrics such as the percentage of habitat cannot distinguish these landscapes.](./plots/neutral-landscapes.py)

Neutral models make two points. First, many metrics depend strongly on the proportion of habitat, so that apparent differences in configuration between landscapes may simply reflect different amounts of habitat; comparisons must control for $p$. Second, with the amount of habitat fixed, its configuration, governed here by a single parameter of spatial autocorrelation, determines the number, size, isolation and edge of the patches, and hence the conditions for organisms that must move among them. Whether configuration matters for populations independently of amount is the question of the next chapter.

## Summary

- Landscape (Definition 48.1.1): a heterogeneous area composed of a recurring cluster of interacting ecosystems; the concept passed from visual aesthetics to Humboldt's regional unit, Troll's landscape ecology (1939) and Forman's land mosaics (1986, 1995). Characteristics: regionality, heterogeneity, scale dependence, function. Landscape ecology (Definition 48.1.2) studies structure, function and change.
- Elements: patches (Definition 48.2.1) by origin (disturbance, remnant, environmental resource, introduced, regenerated, ephemeral); richness depends on area, habitat diversity, age, disturbance, isolation, matrix and boundary. Edge depth $d$: interior and edge species; core area of a convex patch $A - Pd \le A_{\mathrm{c}} \le (\sqrt A - d\sqrt\pi)^2$, maximal for the disk (Proposition 48.2.1); shape index $P/(2\sqrt{\pi A})$; the ecologically optimal patch; keep many patches.
- Corridors (Definition 48.2.2): line and strip corridors, width effect (hedgerow threshold about 12 m for herbs; interior requires width $> 2d$), connectivity (gaps), curvilinearity; functions as conduit, habitat, filter or barrier, source and sink.
- Matrix (Definition 48.2.3): largest area, highest connectivity, control over dynamics; porosity, boundary shape, networks of nodes and links.
- Pattern models: patch–corridor–matrix, corridor–network, boundary–ecotone–gradient.
- Characterization: heterogeneity (spatial, temporal, functional); grain and extent (Definition 48.4.1), with metrics changing strongly with grain (aggregation removes small patches and rare classes) and lengths depending on the ruler ($L = c\varepsilon^{1-D}$); landscape diversity at three levels (Shannon index of patch types); connectivity (Definition 48.4.2) and fragmentation (Definition 48.4.3: perforation, dissection, fragmentation, shrinkage, attrition); contrast and ecotones; spatial autocorrelation (Definition 48.4.4), Moran's I, semivariogram with nugget, sill and range, $\gamma(h) = \sigma^2(1 - \rho(h))$ (Proposition 48.4.1).
- Landscape metrics (composition, area, edge, shape, fractal dimension, contagion, isolation, core) are comparable only at the same grain and extent; neutral landscape models (random and fractal) separate the effects of habitat amount and configuration.

## Questions

1. A nature reserve of 100 ha can be designed as a circle or as a rectangle 4 km long. If edge effects penetrate 150 m, compare their core areas. What would you recommend, and when might the long shape be preferable?

   **Answer** Circle: $R = \sqrt{10^6/\pi} = 564\,\mathrm{m}$, core $\pi(564 - 150)^2 = \pi \times 414^2 \approx 53.8\,\mathrm{ha}$, 54% of the area (the bound of Proposition 48.2.1). Rectangle: $4000 \times 250\,\mathrm{m}$; core $(4000 - 300)(250 - 300) < 0$, so there is no core at all: the whole reserve is edge. For interior species the compact design is far better. A long shape may be preferable when the reserve is meant to protect a linear habitat (a river and its riparian forest), to connect two larger reserves as a corridor, or to span an environmental gradient (elevation) so that species can shift their ranges as the climate warms; then a width of several times $2d$ is needed for the corridor to contain interior habitat.

2. Show that for a rectangle with sides $a \ge b$, the core area with edge depth $d$ is less than the bound $(\sqrt{ab} - d\sqrt{\pi})^2$ whenever $b > 2d$, and compute the ratio for $a = b = 400\,\mathrm{m}$ and $d = 50\,\mathrm{m}$.

   **Answer** The core is $(a - 2d)(b - 2d) = ab - 2d(a + b) + 4d^2$ and the bound is $ab - 2d\sqrt{\pi ab} + \pi d^2$. Their difference, bound minus core, is $2d(a + b - \sqrt{\pi ab}) - (4 - \pi)d^2$. Since $a + b \ge 2\sqrt{ab} > \sqrt{\pi}\sqrt{ab}$, the first term is at least $2d(2 - \sqrt\pi)\sqrt{ab} \ge 2d(2 - \sqrt\pi) \cdot b > 4d^2(2 - \sqrt\pi) \approx 0.91d^2$ when $b > 2d$, which exceeds $(4 - \pi)d^2 \approx 0.86d^2$; so the difference is positive. For the square of side 400 m with $d = 50$: core $300^2 = 90\,000\,\mathrm{m^2}$; bound $(400 - 50\sqrt\pi)^2 = (400 - 88.6)^2 = 311.4^2 \approx 96\,970\,\mathrm{m^2}$; the square achieves about 93% of the core of a circle of the same area.

3. Identify the matrix in (a) a landscape of 40% cropland in many separate fields, 35% forest forming one continuous network, and 25% villages and roads; (b) a boreal forest with 10% clear-cuts. Explain using the three criteria.

   **Answer** (a) No element covers more than half. Cropland has the largest area but consists of separate fields, whereas the forest forms a continuous network surrounding the fields; by the second criterion (connectivity), applied when area does not decide, the forest is the matrix, especially if it also controls the dynamics (as a source of seeds, predators or fire). One would check the third criterion: if the dynamics are controlled by farming, an ecologist interested in agricultural pests might still treat cropland as the effective matrix. (b) The forest covers 90%, is continuous and controls dynamics (recolonization of the clear-cuts, fire spread): it is the matrix, and the clear-cuts are disturbance patches that increase its porosity.

4. A survey records soil moisture at 200 points on a grid with 10 m spacing; the semivariogram has a nugget of 0.2, a sill of 1.0 and a range of 40 m. Interpret these values. If you wanted 30 independent samples for a t-test of differences between two treatment areas, how would you arrange them?

   **Answer** The nugget of 0.2 means that 20% of the variance is due to measurement error or to variation at scales below 10 m; the remaining 80% is spatially structured, and moisture is correlated up to about 40 m, the typical size of moist and dry patches. Beyond 40 m the values are effectively uncorrelated. For independent samples within each treatment area, the sampling points should be separated by more than the range, at least 40 m, preferably more; otherwise neighbouring samples are partly redundant (pseudoreplication), the effective sample size is smaller than 30, and the t-test overstates significance. Alternatively one can model the autocorrelation explicitly (generalized least squares with a spatial covariance function).

5. (Open question) A county plans to convert 30% of its farmland to forest to increase carbon storage and biodiversity, and can choose between many small plantations scattered among the fields and a few large blocks connected by hedgerows. Using the concepts of this chapter, discuss the consequences of the two designs for different groups of organisms and processes.

   **Answer** Points to consider: large blocks have much more core area per hectare (Proposition 48.2.1) and support interior forest species (forest songbirds sensitive to nest predation, interior herbs, mammals with large home ranges); with hedgerows wider than about 12 m (and ideally wider than $2d$ for forest animals), they also connect populations. Scattered small plantations create a fine-grained mosaic with much edge: good for edge species, game, pollinators and natural enemies of crop pests that need both woody shelter and fields (landscape complementation), and they increase structural heterogeneity and possibly the spillover of ecosystem services to all fields; but they may be dominated by generalist edge species, increase nest predation, and raise the porosity of the farmland matrix. Carbon storage per hectare is similar at first, but small plantations are more exposed to wind and drought at edges. Their configuration also affects the farmland: hedgerows and small woods reduce wind erosion but shade crops. The answer depends on the target species, the grain at which they perceive the landscape, and the existing matrix; a mixed design (a few large cores plus stepping stones and corridors) is often recommended. The question of whether configuration matters independently of amount is analyzed in [7.19.49](/7.19.49).
