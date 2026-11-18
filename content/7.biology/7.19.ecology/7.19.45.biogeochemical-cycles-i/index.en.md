---
title: "Biogeochemical Cycles I: Compartment Models, Water and Carbon"
description: "The general features of matter cycling (cycling versus energy flow, global and local cycles, gaseous and sedimentary cycles, intrasystem cycling) and the pools and turnover times of the elements; compartment models: pools and donor-controlled fluxes, compartmental matrices and their stability, the steady state, the fundamental matrix and the mean transit time, tracer pulses, turnover time versus adjustment time; nutrient budgets of ecosystems, the Hubbard Brook deforestation experiment with a model of the uncoupling of uptake and mineralization, nutrient spiralling in streams and budgets of lakes and oceans; the water cycle, its pools, fluxes and residence times, vegetation and the intensification of the cycle; the carbon cycle: processes and pools, the carbonate system of seawater, the Revelle factor and ocean acidification, the global carbon budget and the missing sink, a four-box model of the anthropogenic perturbation with its pulse response and long-term airborne fraction, regional balances in China and Amazonia, and the science of carbon neutrality and carbon capture and storage."
---

Energy enters an **ecosystem** once, as sunlight, and leaves it as heat; matter stays. The carbon, nitrogen, phosphorus and other elements of which organisms are built are taken up in inorganic form, passed along food chains, released by decomposition and taken up again, so that the same atoms are used over and over while energy flows through. Microbiology has described the metabolisms that transform the elements and defined the **biogeochemical cycle** as the set of transformations and transport processes by which an element moves between its reservoirs ([7.11.30](/7.11.30#def-30.1.1)); the preceding chapters followed energy through producers, consumers and decomposers ([7.19.42](/7.19.42)–[7.19.44](/7.19.44)). This chapter and the next take the ecosystem and global view of the cycles. We first describe their general features (45.1) and then develop the quantitative language in which all of them are described, the compartment model of pools and fluxes, with its linear algebra of stability, turnover and residence times (45.2). With this language we examine the nutrient budgets of ecosystems, from the deforested catchment at Hubbard Brook to streams and lakes (45.3), the water cycle that carries most nutrients (45.4) and the carbon cycle (45.5), whose perturbation by fossil fuels is the cause of current climate change. A box model of the ocean and land sinks explains why a pulse of carbon dioxide stays in the atmosphere for centuries although each molecule is exchanged within a few years. Nitrogen, phosphorus and sulfur follow in [7.19.46](/7.19.46), and the consequences of the carbon perturbation for climate and life in [7.19.47](/7.19.47).

## 45.1. General Features of Matter Cycling

### 45.1.1. Cycling of Matter and Flow of Energy

Matter cycling and energy flow always occur together, because energy is carried through food webs in the chemical bonds of organic compounds, but they differ in three ways.

- Energy is used once. Each joule fixed in photosynthesis is degraded to heat in the respiration of producers, consumers and decomposers and cannot be used again for work ([7.19.43](/7.19.43)). Matter is reused: the nitrogen of a protein becomes ammonium again when the protein is decomposed, and the ammonium can be taken up by another plant.
- The supply differs. Solar energy arrives at a rate that organisms cannot change; nutrients exist in finite amounts, and what is locked up in living and dead biomass is unavailable to others. If dead organic matter were not decomposed, the inorganic pools would be exhausted and production would stop.
- The decomposers are central. Most nutrient release from organic to inorganic form (mineralization) is carried out by the decomposer subsystem, although grazers and their excreta contribute ([7.19.44](/7.19.44)).

Cycling is never perfect. Some of the elements released by decomposition are lost from the ecosystem in drainage water or, for nitrogen and sulfur, as gases, and new supplies arrive from the atmosphere and the weathering of rock. An ecosystem therefore has both an internal cycle and a budget of inputs and outputs (45.3).

### 45.1.2. Global and Local Cycles

The cycles can be studied at two scales. The global biogeochemical cycles concern the largest pools, the atmosphere, the oceans, the soils and the rocks, and the fluxes between them; they are the sum of all local events. Local cycles concern the exchange of elements within one ecosystem, between its plants, animals, decomposers and soil. The movement of an element from the environment through producers, consumers and decomposers back to the environment within one ecosystem is often called the intrasystem cycle (or biological cycle), in contrast to the slow geological cycle of weathering, transport to the sea, sedimentation and uplift.

The global cycles are classified by their main reservoir:

| Type | Main reservoir | Gas phase | Examples | Character |
|---|---|---|---|---|
| Hydrological cycle | Ocean | Water vapour | Water | Driven by solar energy; carries the other cycles |
| Gaseous cycles | Atmosphere and ocean | Yes ($\ce{CO2}$, $\ce{N2}$, $\ce{O2}$) | Carbon, nitrogen, oxygen | Well mixed, globally buffered; local deficits are made up quickly |
| Sedimentary cycles | Rocks and sediments | None or negligible | Phosphorus, calcium, potassium, magnesium, iron | Supplied by weathering; elements lost to the sea return only by geological uplift |
| Mixed | Both | Partly ($\ce{SO2}$, $\ce{H2S}$, dimethyl sulfide) | Sulfur | Atmospheric and lithospheric phases of similar size |

Gaseous cycles are relatively well buffered: an increase of $\ce{CO2}$ in one place is soon dispersed and taken up elsewhere. Sedimentary cycles are less perfect, because an element that is carried to the deep sea is lost from terrestrial life for millions of years. The water cycle is the vehicle of both kinds, since most elements are transported in solution or with eroded particles.

The size of a reservoir and the time an element spends in it differ by many orders of magnitude (Table below, after Odum and Barrett 2005 and later estimates). The small pools of living biomass turn over quickly; the large pools of rocks and deep water turn over slowly. The next section makes the notion of turnover time precise.

| Element | Reservoir | Size | Turnover time |
|---|---|---|---|
| Carbon ($\mathrm{Pg\,C}$) | Atmosphere | 870 | about 4 years |
| | Terrestrial vegetation | 450 | about 10 years (wood: decades) |
| | Soils | 1700 | decades to millennia |
| | Surface ocean | 900 | about 10 years |
| | Deep ocean | 37 000 | about 1000 years |
| | Marine biota | 3 | days to weeks |
| | Carbonate rocks and kerogen | about $10^8$ | $> 10^8$ years |
| Nitrogen ($10^{12}\,\mathrm{g\,N}$) | Atmosphere ($\ce{N2}$) | $4 \times 10^9$ | $10^7$ years |
| | Soil | $3 \times 10^5$ | about 2000 years |
| | Terrestrial biomass | $1.3 \times 10^4$ | about 50 years |
| Phosphorus ($10^{12}\,\mathrm{g\,P}$) | Sediments | $4 \times 10^9$ | $2 \times 10^8$ years |
| | Deep ocean | $8.7 \times 10^4$ | 1500 years |
| | Surface ocean | 2700 | 2.6 years |
| | Terrestrial biota | 3000 | about 50 years |

## 45.2. Compartment Models

### 45.2.1. Pools and Fluxes

To analyze a cycle quantitatively we lump the forms and locations of an element into a few homogeneous boxes and describe the rates at which the element moves between them.

**Definition 45.2.1 (Compartment Model)** A **compartment model** (box model) of an element in a system consists of a finite set of compartments (pools), each characterized by the amount $x_i(t)$ of the element it contains, and of the fluxes $F_{ij}$ from compartment $j$ to compartment $i$, together with the inputs $b_i$ from outside the system and the outputs $F_{0j}$ to outside. Conservation of mass gives

$$
\frac{\mathrm{d}x_i}{\mathrm{d}t} = b_i + \sum_{j \ne i} F_{ij} - \sum_{j \ne i} F_{ji} - F_{0i}.
$$
The model is donor-controlled and linear if every flux is proportional to the amount in the compartment it leaves, $F_{ij} = k_{ij}x_j$, with constant transfer coefficients $k_{ij} \ge 0$.

Each compartment is assumed well mixed: an atom in it is equally likely to leave by any route, whatever its history. Donor control is a reasonable approximation for many flows, such as litterfall (a fraction of the leaves falls each year), leaching (a fraction of the soluble pool is washed out) and decomposition (Olson's model of [7.19.44](/7.19.44)), but not for uptake limited by the recipient (a plant cannot take up more nitrogen than its roots allow) or for fluxes that depend on both compartments, such as the exchange of $\ce{CO2}$ between air and sea (45.5.4). In a linear donor-controlled model the equations take the matrix form

$$
\frac{\mathrm{d}\boldsymbol{x}}{\mathrm{d}t} = A\boldsymbol{x} + \boldsymbol{b}, \qquad a_{ij} = k_{ij}\ (i \ne j), \qquad a_{jj} = -\Bigl(k_{0j} + \sum_{i \ne j} k_{ij}\Bigr). \tag{45.1}
$$
The off-diagonal entries of $A$ are nonnegative, and the sum of the entries of column $j$ is $-k_{0j} \le 0$: everything that leaves compartment $j$ enters another compartment or leaves the system. A matrix with these two properties is called a compartmental matrix.

**Definition 45.2.2 (Turnover Time and Residence Time)** For a compartment at steady state, with content $Q$ and throughput $F$ (the total inflow, equal to the total outflow), the **turnover time** is $T = Q/F$, the time needed to replace an amount equal to the content; its reciprocal $F/Q$ is the turnover rate. The **residence time** is the mean time that an atom entering the compartment remains in it before it leaves.

In a well-mixed donor-controlled compartment the two are equal: atoms leave independently at total rate constant $K = -a_{jj}$, so the time an atom spends in the compartment on one visit is exponentially distributed with mean $1/K$, and at steady state $F = KQ$ gives $T = Q/F = 1/K$. That turnover time equals mean residence time holds much more generally for any system at steady state (Proposition 45.2.2 and the remark after it). If 1000 units are present and 10 enter and leave each hour, the turnover rate is 1% per hour and the turnover time 100 hours. Turnover time is a property of the pool and of the gross flux through it; a large flux through a small pool, such as phosphate in the surface water of a productive lake, means rapid cycling even if the concentration is low. As Pomeroy (1960) put it, a rapid flux of phosphate is more important than its concentration in maintaining high production.

### 45.2.2. Linear Compartment Systems

The general solution of Eq. (45.1) is given by the variation of constants formula with the **matrix exponential** ([2.4.8](/2.4.8#sec-8.3)),

$$
\boldsymbol{x}(t) = \mathrm{e}^{At}\boldsymbol{x}(0) + \int_0^t \mathrm{e}^{A(t-s)}\boldsymbol{b}(s)\,\mathrm{d}s,
$$
so the behavior of the system is decided by the **eigenvalues** of $A$. Compartmental matrices have a simple spectral structure.

**Theorem 45.2.1 (Stability of Compartment Systems)** Let $A$ be a compartmental matrix.

1. Every eigenvalue of $A$ has nonpositive real part, and $\mathrm{e}^{At}$ has nonnegative entries for $t \ge 0$.
2. If from every compartment there is a chain of flows leading out of the system (the system is outflow-connected), every eigenvalue has negative real part. Then $A$ is invertible, $N = (-A)^{-1}$ has nonnegative entries, and for constant inputs every solution tends to the unique steady state $\boldsymbol{x}^* = N\boldsymbol{b} \ge \boldsymbol{0}$.

**Proof** (1) $A$ and $A^{\mathsf T}$ have the same eigenvalues. By the **Gershgorin circle theorem** ([2.1.6](/2.1.6#thm-6.4.1)) applied to $A^{\mathsf T}$, every eigenvalue lies in a disc centered at some $a_{jj} \le 0$ with radius $\sum_{i \ne j} a_{ij} = -a_{jj} - k_{0j} \le \lvert a_{jj}\rvert$, which is contained in the closed left half-plane. For positivity, choose $c$ so large that $A + cI$ has nonnegative entries; then $\mathrm{e}^{At} = \mathrm{e}^{-ct}\mathrm{e}^{(A + cI)t}$ is a positive multiple of a power series with nonnegative terms.

(2) The column sums of $\mathrm{e}^{At}$ are nonincreasing in $t$, because $\frac{\mathrm{d}}{\mathrm{d}t}\boldsymbol{1}^{\mathsf T}\mathrm{e}^{At} = \boldsymbol{1}^{\mathsf T}A\,\mathrm{e}^{At} = -(k_{01}, \dots, k_{0n})\,\mathrm{e}^{At} \le \boldsymbol{0}$: the total mass of a tracer cannot increase. If compartment $j$ is linked to an outflow by a chain $j \to i_1 \to \dots \to i_m$, the term $(A + cI)^m t^m/m!$ of the series gives column $j$ of $\mathrm{e}^{At}$ a positive entry in $i_m$ for every $t > 0$, so that a positive fraction of a tracer started in $j$ is lost by any time $T > 0$. Hence there is $T > 0$ with all column sums of $\mathrm{e}^{AT}$ less than some $\rho < 1$, that is, $\Vert\mathrm{e}^{AT}\Vert_1 \le \rho$ in the column-sum norm. Then $\Vert\mathrm{e}^{AnT}\Vert_1 \le \rho^n \to 0$, so every eigenvalue $\mu$ of $\mathrm{e}^{AT}$ satisfies $\lvert\mu\rvert < 1$; since these eigenvalues are $\mathrm{e}^{\lambda T}$ for the eigenvalues $\lambda$ of $A$, $\operatorname{Re}\lambda < 0$. Consequently $\int_0^\infty \mathrm{e}^{At}\,\mathrm{d}t$ converges and equals $-A^{-1}$, which is nonnegative because the integrand is. For constant $\boldsymbol{b}$, $\boldsymbol{x}(t) - \boldsymbol{x}^* = \mathrm{e}^{At}(\boldsymbol{x}(0) - \boldsymbol{x}^*) \to \boldsymbol{0}$. $\square$

A compartment model without any outflow (a closed system, such as the whole Earth for carbon on timescales of centuries) has column sums zero, so $\boldsymbol{1}^{\mathsf T}A = \boldsymbol{0}^{\mathsf T}$ and $0$ is an eigenvalue: total mass is conserved and a perturbation is never removed, only redistributed (45.5.4).

The matrix $N$ has a direct interpretation. Atoms move independently between compartments, so the fate of one atom is a continuous-time **Markov chain** whose states are the compartments and the outside; the outside is absorbing. If a unit tracer pulse enters compartment $j$ at $t = 0$, the amount $x_i(t) = (\mathrm{e}^{At})_{ij}$ in compartment $i$ is the probability that a tagged atom is in $i$ at time $t$.

**Proposition 45.2.1 (Fundamental Matrix)** In an outflow-connected linear compartment system, an atom entering compartment $j$ spends on average a total time $N_{ij}$ in compartment $i$ before leaving the system, where $N = (-A)^{-1}$. Its mean transit time through the system is the column sum $\tau_j = \sum_i N_{ij}$.

**Proof** The time spent in $i$ is $\int_0^\infty \boldsymbol{1}\{\text{atom in } i \text{ at } t\}\,\mathrm{d}t$; its expectation is $\int_0^\infty (\mathrm{e}^{At})_{ij}\,\mathrm{d}t = N_{ij}$ by Theorem 45.2.1. Summing over $i$ gives the mean total time. $\square$

**Proposition 45.2.2 (Stock, Input and Mean Transit Time)** At the steady state $\boldsymbol{x}^* = N\boldsymbol{b}$ of an outflow-connected system, the total stock equals the input flux times the mean transit time of the input,

$$
\sum_i x_i^* = \sum_j \tau_j b_j = \bar\tau\,\sum_j b_j, \qquad \bar\tau = \frac{\sum_j \tau_j b_j}{\sum_j b_j}.
$$

**Proof** $\boldsymbol{1}^{\mathsf T}\boldsymbol{x}^* = \boldsymbol{1}^{\mathsf T}N\boldsymbol{b} = \sum_j(\sum_i N_{ij})b_j$. $\square$

Thus the turnover time of the whole system, stock divided by input, is the mean transit time of its atoms, and the same holds for each compartment with its own throughput (the result is known in queueing theory as Little's law). Two consequences are worth stating. A system can hold a large stock with a small input only if atoms stay long; and long transit times can come either from slow compartments or from many cycles through fast ones.

### 45.2.3. Tracer Pulses and Cycling

Radioactive and stable isotopes ($^{32}\mathrm{P}$, $^{15}\mathrm{N}$, $^{14}\mathrm{C}$, $^{13}\mathrm{C}$) are added to ecosystems precisely to measure these quantities: the curves of tracer content in each compartment after a pulse are the columns of $\mathrm{e}^{At}$, from which the transfer coefficients can be estimated. As an example, consider the nitrogen of a temperate forest in three compartments: plants ($x_1$), soil organic matter ($x_2$) and available inorganic nitrogen ($x_3$). Plants take up inorganic nitrogen at rate $u x_3$, return it in litter at rate $l x_1$, decomposers mineralize soil organic nitrogen at rate $m x_2$, and inorganic nitrogen is leached at rate $\lambda x_3$, balanced by an input $b$ from deposition and fixation:

$$
A = \begin{bmatrix} -l & 0 & u \\ l & -m & 0 \\ 0 & m & -u - \lambda \end{bmatrix}, \qquad \boldsymbol{b} = \begin{bmatrix} 0 \\ 0 \\ b \end{bmatrix}.
$$
With $u = 4$, $l = 0.16$, $m = 0.02$ and $\lambda = 0.5$ per year and $b = 10\,\mathrm{kg\,N\,ha^{-1}\,yr^{-1}}$, the steady state is $x_1^* = 500$, $x_2^* = 4000$ and $x_3^* = 20\,\mathrm{kg\,N\,ha^{-1}}$, and the internal cycle carries $80\,\mathrm{kg\,N\,ha^{-1}\,yr^{-1}}$, eight times the input. By Proposition 45.2.1 an atom entering the inorganic pool spends on average 50 years in plants, 400 years in soil organic matter and 2 years in the inorganic pool, a mean transit time of 452 years, equal to the total stock divided by the input (Proposition 45.2.2).

The same number can be obtained by counting cycles. Each time an atom is in the inorganic pool it is taken up with probability $p = u/(u + \lambda)$ and leached with probability $1 - p$, so the number of cycles before loss is geometrically distributed with mean $p/(1 - p) = u/\lambda = 8$. Each cycle takes on average $1/l + 1/m + 1/(u + \lambda)$ years, and the final visit to the inorganic pool $1/(u + \lambda)$; the mean transit time is $8(6.25 + 50) + 9 \times 0.22 = 452$ years. The tightness of the internal cycle, measured by $u/\lambda$, multiplies the residence time of the element in the ecosystem, which is why ecosystems that cycle nutrients efficiently can maintain large stocks with small inputs. The fraction of the total throughflow of a system that is due to cycling is Finn's cycling index, used by Odum and others to compare ecosystems; here it is $8/9$ for the flux through the inorganic pool.

![Fate of a tracer in a three-compartment model of forest nitrogen (plants, soil organic matter, inorganic nitrogen; transfer coefficients: uptake 4, litterfall 0.16, mineralization 0.02 and leaching 0.5 per year). A: after a pulse added to the inorganic pool, the tracer passes within months into plants, within a few years into soil organic matter, and leaves the system over centuries; the whole-system curve is the probability that an atom is still present. B: mean time per visit (the turnover time of the compartment) and mean total time spent in each compartment by an atom entering the inorganic pool (the column of the fundamental matrix, Proposition 45.2.1): each compartment is visited about eight or nine times, and the sum of the totals is the mean transit time of 452 years. C: the mean transit time and the mean number of cycles are both inversely proportional to the leaching rate constant; the dotted line marks the value used in A and B.](./plots/compartment-pulse.py)

### 45.2.4. Turnover Time and Adjustment Time

Turnover time and the time a system takes to recover from a perturbation are different quantities, and confusing them is a common error in discussions of carbon dioxide. Every year about $200\,\mathrm{Pg\,C}$ are exchanged between the atmosphere and the land and ocean (photosynthesis and respiration, dissolution and outgassing), against an atmospheric stock of about $870\,\mathrm{Pg\,C}$: the turnover time of atmospheric carbon is about four years, and a $\ce{CO2}$ molecule emitted today will, on average, have been taken up by a leaf or the sea within a few years. Yet an excess of $\ce{CO2}$ added to the atmosphere decays over decades to millennia. The reason is that the exchange is two-way: a molecule taken up by the surface ocean is replaced by another that is released, and the excess is removed only by the net flux, which depends on how quickly the receiving reservoirs can themselves pass the excess on. In a compartment model the gross turnover time is $1/(-a_{11})$ for the atmosphere, whereas the adjustment of a perturbation is governed by all the eigenvalues of $A$, the smallest of which, in magnitude, belong to the slowest reservoirs (the deep ocean, soils) and to the carbonate chemistry of the sea (45.5.4).

## 45.3. Nutrient Budgets of Ecosystems

### 45.3.1. Inputs and Outputs

An ecosystem receives elements from four sources:

- Weathering of rock and soil is the main source of calcium, magnesium, potassium, iron and phosphorus. Chemical weathering, above all carbonation, in which carbonic acid releases cations from minerals, matters more than mechanical weathering; organic acids released by mycorrhizal fungi contribute ([7.11.30](/7.11.30)).
- The atmosphere supplies carbon as $\ce{CO2}$, nitrogen through biological **nitrogen fixation**, and other elements in wetfall (rain, snow and fog, which contain dissolved gases, sea-salt aerosols and dust) and dryfall (settling particles and the uptake of gases). Fog and cloud droplets are particularly concentrated; forest edges intercept more airborne nutrients than interiors, by 17–56% for sulfur, nitrogen and calcium in New York forests (Weathers et al. 2001). Mineral dust is the largest source of atmospheric phosphorus, and Saharan and Sahelian dust fertilizes the Amazon rain forest across the Atlantic.
- Water brings nutrients to floodplains and, from the catchment, to streams, lakes and estuaries.
- Human activities add fertilizers, sewage, and the products of fossil-fuel combustion ($\ce{CO2}$, oxides of nitrogen and sulfur).

Outputs are release to the atmosphere ($\ce{CO2}$ from respiration and fire, methane from anaerobic soils and ruminants, and $\ce{N2}$ and $\ce{N2O}$ from **denitrification**), losses in drainage water to streams and groundwater, mostly in solution except for phosphorus and iron, which travel bound to particles, and harvest and erosion. When inputs exceed outputs, elements accumulate in biomass and soil organic matter, as carbon does during succession; when outputs exceed inputs, the system is being depleted, as phosphorus is during long soil development (Walker and Syers 1976; [7.19.46](/7.19.46)) and as all elements are after severe disturbance.

For elements such as nitrogen and phosphorus, the amounts cycled internally each year are typically an order of magnitude larger than the amounts entering or leaving; the ecosystem is relatively closed for them. For elements supplied far in excess of biological demand, such as sodium, chloride or sulfate in maritime regions, the exchange across the boundary exceeds internal cycling and the ecosystem is relatively open.

### 45.3.2. The Hubbard Brook Experiment

A catchment (watershed) is the area of land drained by one stream; because it loses elements mainly through its stream, its budget can be measured by comparing the chemistry of precipitation with that of the stream water. Bormann, Likens and colleagues used this idea in the Hubbard Brook Experimental Forest, a northern hardwood forest in the White Mountains of New Hampshire, from 1963 onwards: small catchments on impermeable bedrock were gauged for precipitation and stream flow and sampled for chemistry.

In the undisturbed forest, the outputs of most cations in stream water exceeded their inputs in precipitation, the difference coming from weathering of the bedrock at about $70\,\mathrm{g\,m^{-2}\,yr^{-1}}$; but inputs and outputs were small compared with the amounts held in biomass and cycled each year. Nitrogen arrived in precipitation ($6.5\,\mathrm{kg\,ha^{-1}\,yr^{-1}}$) and by fixation (about $14\,\mathrm{kg\,ha^{-1}\,yr^{-1}}$), and only $4\,\mathrm{kg\,ha^{-1}\,yr^{-1}}$, about 0.1% of the nitrogen in living and dead organic matter, left in the stream (denitrification was not measured).

In 1965–1966 all trees in one catchment were felled and left in place, and regrowth was suppressed with herbicide for three years. Stream flow increased by about 40%, because transpiration ceased, and the export of dissolved inorganic substances rose to about 13 times the normal rate. Nitrate export increased most, about 60-fold; potassium 14-fold, calcium 7-fold, magnesium 5-fold and sodium, an element of little biological importance, only 2.5-fold (Likens and Bormann 1975). The concentration of nitrate in the stream exceeded drinking-water standards. The experiment showed that the forest retains its nutrients not by chemistry but by biology: the trees take up the nitrogen that decomposers release, and once uptake stopped, mineralization continued, nitrifying bacteria converted the ammonium to mobile nitrate, and the nitrate was leached. The more tightly an element is cycled by the vegetation, the larger the loss when the cycle is broken.

The model of 45.2.3 reproduces this behavior when the plant compartment is removed: with $u = 0$, the inorganic pool is no longer drained by uptake, and its steady state $(b + m x_2)/\lambda$ rises by a factor of about $(u + \lambda)/\lambda$, the ratio of the internal cycle to the leaching flux. Regrowth restores uptake, and the export returns to its former level within a decade.

![The Hubbard Brook deforestation experiment. A: increase in the export of dissolved ions in stream water from the felled catchment, relative to the forested control catchment, in the years after felling (Likens and Bormann 1975, as summarized by Begon and Townsend 2021); nitrate, the most tightly cycled ion, increased most and sodium least. B: a compartment model of the nitrogen of a forested catchment (as in the figure of 45.2.3, with leaching rate 0.2 per year, input 4 kg N ha⁻¹ yr⁻¹); at time 0 the trees are felled and their nitrogen added to soil organic matter, uptake ceases for three years (herbicide), and runoff and mineralization increase by 40% while the site is open. Nitrate export (blue, logarithmic scale) rises about eighteenfold and declines as the regrowing vegetation (green, right axis) restores uptake; illustrative parameters.](./plots/hubbard-brook.py)

Later work at Hubbard Brook found two slower consequences. Acid deposition had depleted the exchangeable calcium of the soils, so that the recovery of streams from acidification was slow even after sulfur emissions fell ([7.19.46](/7.19.46#sec-46.3)), and the forest stopped accumulating biomass in the 1980s, partly because of calcium limitation; adding calcium silicate to a whole catchment in 1999 restored the growth and health of sugar maples (Battles et al. 2014). Clear-felling in general increases losses of nutrients and soil, and the loss is larger where uptake is stopped for longer (herbicide, conversion to cropland) and where the soil is steep and the rainfall intense.

### 45.3.3. Streams, Lakes and Oceans

Aquatic ecosystems receive most of their nutrients from the catchment, and their budgets are dominated by transport. In streams, only a small fraction of the nutrients carried by the water is taken up by the biofilms of algae, bacteria and fungi on the stream bed, passed to grazing invertebrates and released again; because the water moves downstream in the meantime, an atom's path is a spiral rather than a cycle (nutrient spiralling; Webster and Patten 1979; Newbold et al. 1981). The spiral length $S$ is the distance travelled downstream during one cycle, the sum of the uptake length $S_{\mathrm{w}}$ (the distance travelled in dissolved form before uptake, the reciprocal of the fractional uptake rate per unit length) and the turnover length in the biota. Short spirals indicate tight cycling. In a New Zealand stream, introduced brown trout suppressed grazing invertebrates, allowed algae to grow, and shortened the uptake length of nitrate (Simon et al. 2004).

Lakes with outflows lose nutrients in the outflowing water and to the sediments; lakes without outflows (endorheic lakes) lose water only by evaporation, concentrate salts and nutrients, and are often extremely productive, like the soda lakes of East Africa with their flamingos. For phosphorus the balance between loading, outflow and sedimentation determines the trophic state of a lake, a relation made quantitative by Vollenweider's model ([7.19.46](/7.19.46#sec-46.2.4)). Estuaries and coastal seas receive the nutrients of whole river basins, and rivers draining populated and farmed catchments carry nitrogen mostly as nitrate, whereas pristine rivers carry it mostly in organic form. Damming reduces the export of dissolved silicate to the sea and so affects the diatoms of coastal plankton. The open ocean is the largest endorheic basin: it loses elements only to its sediments, and its surface production depends on the return of nutrients from depth by winter mixing and upwelling ([7.19.42](/7.19.42#sec-42.5.2)). In about a third of the ocean, nitrate remains unused because iron limits phytoplankton, as iron fertilization experiments showed (Boyd et al. 2007).

## 45.4. The Water Cycle

### 45.4.1. Pools and Fluxes

Water is the medium of all other cycles: elements are dissolved and transported in it, and erosion and deposition are driven by it. The cycle is driven by solar energy, which evaporates water mainly from the oceans; winds carry the vapour, which condenses and falls as precipitation, and the water returns to the sea in rivers and groundwater. The water of the Earth is distributed very unevenly (Shiklomanov 1993):

| Reservoir | Volume ($10^3\,\mathrm{km^3}$) | Share of total | Turnover time |
|---|---|---|---|
| Oceans | 1 338 000 | 96.5% | about 3000 years |
| Ice caps, glaciers, permanent snow | 24 100 | 1.74% | about 10 000 years |
| Groundwater | 23 400 | 1.69% | weeks to 10 000 years (active part about 300 years) |
| Lakes | 176 | 0.013% | 10–100 years (fresh) |
| Soil moisture | 16.5 | 0.001% | about 1 month |
| Atmosphere | 12.9 | 0.001% | about 9 days |
| Rivers | 2.1 | 0.0002% | about 2 weeks |
| Living organisms | 1.1 | 0.0001% | about 1 week |

Freshwater lakes and rivers, the water most accessible to people, hold less than 0.01% of the total. The annual fluxes, in $10^3\,\mathrm{km^3\,yr^{-1}}$, are about 413 of evaporation and 373 of precipitation over the oceans, 113 of precipitation and 73 of evapotranspiration over land, and 40 of runoff from land to sea, which balances the net transport of vapour from the oceans to the continents (Trenberth et al. 2007). By Definition 45.2.2 the residence time of water in the atmosphere is $12.9/(373 + 113) \times 365 \approx 10$ days, which is why weather is local and changeable while the oceans are a memory of centuries.

### 45.4.2. Vegetation and the Water Cycle

The hydrological cycle would proceed without life, but vegetation changes its terrestrial branch. A plant lives between two opposite movements of water: one through the plant, from the soil through roots and stem to the leaves and out by **transpiration** ([7.13.3](/7.13.3)), and one from the atmosphere onto the canopy as precipitation, of which part evaporates from wet leaves (interception), part drips through and part runs down the stems. Transpiration returns to the atmosphere water that would otherwise drain to streams, and it is the largest component of terrestrial evapotranspiration, roughly 60% of it globally (Schlesinger and Jasechko 2014). Removing forest therefore increases runoff, as at Hubbard Brook, and in the Amazon basin, where a large part of the rain is recycled transpiration, extensive deforestation is expected to reduce rainfall downwind. Groundwater aquifers with turnover times of centuries are being pumped faster than they are recharged in many agricultural regions, including the North China Plain.

### 45.4.3. An Intensifying Water Cycle

Warming intensifies the water cycle. By the **Clausius–Clapeyron equation** ([5.2](/5.2)) the saturation vapour pressure of water rises by about 7% per kelvin, so a warmer atmosphere holds and transports more water: heavy precipitation events become more intense, and evaporation from soils increases, which deepens droughts where precipitation does not increase. The pattern "wet gets wetter, dry gets drier" holds roughly over the oceans, less clearly over land. Variability in time is increasing as well: since 1900 the day-to-day variability of precipitation has increased over about three quarters of the land area, by about 1.2% per decade in the global average, a change attributed to anthropogenic warming (Zhang et al. 2024). Greater variability means wetter wet periods and drier dry periods, with consequences for floods, droughts and the plants and animals adapted to the old regime ([7.19.47](/7.19.47#sec-47.2)).

## 45.5. The Carbon Cycle

### 45.5.1. Processes and Pools

Carbon makes up about half of the dry mass of organisms, and its cycle is coupled to the flow of energy: carbon enters food webs in photosynthesis and leaves them in respiration. The **carbon cycle** ([7.11.30](/7.11.30#def-30.2.1)) comprises three groups of processes:

1. biological assimilation and dissimilation: photosynthesis by plants and phytoplankton, respiration by all organisms, and, in anoxic habitats, methanogenesis and methane oxidation;
2. the exchange of $\ce{CO2}$ between the atmosphere and the ocean, by dissolution and outgassing, and its transport within the ocean by circulation and by the sinking of organic particles (the biological carbon pump, [7.11.30](/7.11.30#def-30.2.2));
3. the precipitation of carbonates (shells and skeletons of coccolithophores, foraminifera, corals and molluscs) and their burial in sediments, and, on geological timescales, the weathering of silicate and carbonate rocks and volcanic outgassing.

![The global carbon cycle (pools in Pg C, fluxes in Pg C per year; rounded values after IPCC AR6, Canadell et al. 2021, and the Global Carbon Budget 2024, Friedlingstein et al. 2024). Natural gross fluxes between atmosphere, land and ocean are large and nearly balanced: photosynthesis takes up about 120 Pg C per year and respiration and fire return about 117; the ocean takes up about 80 and releases about 77. The human perturbation (red; means for 2014–2023) adds about 9.7 Pg C per year from fossil fuels and cement and 1.1 from land-use change; of this about 5.2 accumulates in the atmosphere, 2.9 is taken up by the ocean and 3.2 by the land. The atmosphere now contains about 280 Pg C more than in 1750. The deep ocean holds about 40 times as much carbon as the atmosphere; carbonate rocks, not shown, hold far more but exchange it only on geological timescales.](./plots/carbon-pools-fluxes.py)

The largest active reservoir is the dissolved inorganic carbon of the deep ocean, about $37\,000\,\mathrm{Pg\,C}$; soils hold about twice as much carbon as the atmosphere, and the northern permafrost another $1400\,\mathrm{Pg\,C}$, frozen and protected from decomposition ([7.11.30](/7.11.30#sec-30.2.1)). Fossil fuels lay inert in the lithosphere until humans began to burn them. The atmospheric concentration of $\ce{CO2}$, about $280\,\mathrm{ppm}$ in 1750, reached about $423\,\mathrm{ppm}$ in 2024; one ppm corresponds to $2.12\,\mathrm{Pg\,C}$. The record begun by Keeling at Mauna Loa in 1958 shows the rise and, superimposed on it, a seasonal oscillation of several ppm: the land of the Northern Hemisphere takes up $\ce{CO2}$ during its summer and releases it in winter, so the planet can be seen to breathe.

### 45.5.2. The Carbonate System of Seawater

The ocean takes up $\ce{CO2}$ because the gas reacts with water and carbonate ions. Dissolved $\ce{CO2}$ is in equilibrium with the gas by **Henry's law** ([6.3.5](/6.3.5)), $[\ce{CO2(aq)}] = K_0\,p_{\ce{CO2}}$, and dissociates in two steps ([6.1.9](/6.1.9#sec-9.3.6)):

$$
\ce{CO2(aq) + H2O <=> H+ + HCO3-}, \qquad \ce{HCO3- <=> H+ + CO3^2-},
$$
with apparent dissociation constants in seawater of $\mathrm{p}K_1^* \approx 5.9$ and $\mathrm{p}K_2^* \approx 9.1$ at 15 °C. At the pH of surface seawater, about 8.1, roughly 90% of the dissolved inorganic carbon (DIC $= [\ce{CO2(aq)}] + [\ce{HCO3-}] + [\ce{CO3^2-}]$) is bicarbonate, about 9% carbonate and only about 1% dissolved $\ce{CO2}$. The ion balance of seawater fixes its total alkalinity, essentially $[\ce{HCO3-}] + 2[\ce{CO3^2-}]$ plus borate, at about $2300\,\mu\mathrm{mol\,kg^{-1}}$. When $\ce{CO2}$ is added at constant alkalinity, the net reaction is

$$
\ce{CO2 + H2O + CO3^2- -> 2HCO3-},
$$
which consumes carbonate ions. The more $\ce{CO2}$ the ocean has absorbed, the fewer carbonate ions remain to react with the next addition, and the less effective the ocean becomes as a sink.

**Definition 45.5.1 (Revelle Factor)** The **Revelle factor** (buffer factor) of seawater is the ratio of the relative change in the partial pressure of $\ce{CO2}$ to the relative change in dissolved inorganic carbon at constant alkalinity,

$$
R = \frac{\Delta p_{\ce{CO2}}/p_{\ce{CO2}}}{\Delta\mathrm{DIC}/\mathrm{DIC}}.
$$

$R$ is about 10 in today's surface ocean, lower in warm and higher in cold waters, and it increases as the ocean absorbs $\ce{CO2}$. Its meaning is that a 10% rise in atmospheric $\ce{CO2}$ is matched at equilibrium by only a 1% rise in the DIC of seawater. The surface ocean contains about 1.5 times as much carbon as the atmosphere, but its capacity to absorb additional carbon is only $1.5/10 \approx 0.15$ of the atmospheric excess; only when the excess is mixed into the deep ocean, 40 times larger, does the ocean absorb most of it (45.5.4).

**Definition 45.5.2 (Ocean Acidification)** **Ocean acidification** is the decrease in the pH of seawater, and in its concentration of carbonate ions and its saturation state with respect to calcium carbonate, caused by the uptake of anthropogenic $\ce{CO2}$.

Surface ocean pH has fallen by about 0.1 units since the eighteenth century, an increase of about 26% in the hydrogen ion activity ($10^{0.1} = 1.26$). The saturation state $\Omega = [\ce{Ca^2+}][\ce{CO3^2-}]/K_{\mathrm{sp}}^*$ of aragonite, the form of calcium carbonate made by corals and pteropods, has fallen correspondingly; where $\Omega < 1$ aragonite tends to dissolve, and calcification becomes energetically costly well before that. Cold, high-latitude waters, which absorb more $\ce{CO2}$ and have lower carbonate concentrations, are approaching undersaturation first. The biological consequences are treated in [7.19.47](/7.19.47#sec-47.3.5).

![The carbonate system of seawater (15 °C, salinity 35, total alkalinity 2300 µmol kg⁻¹; equilibrium with the atmosphere). A: Bjerrum plot of the fractions of dissolved inorganic carbon present as CO₂(aq), bicarbonate and carbonate against pH; the curves cross at the apparent pK values, and surface seawater (shaded) is dominated by bicarbonate. B: surface-ocean pH (left axis) and carbonate ion concentration (right axis) against atmospheric CO₂; pH falls from about 8.17 at the preindustrial 280 ppm to 8.02 at 423 ppm (in equilibrium; the observed value, about 8.05, lags behind) and 7.75 at 850 ppm, a concentration reached by about 2100 under very high emissions, while carbonate ions fall by more than half. C: the Revelle factor rises from about 10 to more than 15 over the same range, so that the ocean becomes a less efficient sink.](./plots/ocean-carbonate.py)

### 45.5.3. Sources, Sinks and the Global Carbon Budget

**Definition 45.5.3 (Carbon Source and Carbon Sink)** A reservoir or ecosystem that releases more carbon (as $\ce{CO2}$ or methane) to the atmosphere than it takes up, over a specified period, is a **carbon source**; one that takes up more than it releases is a **carbon sink**.

The definition refers to net fluxes and to a stated period: a forest is a sink while it grows and accumulates carbon, a source in the years after a fire or clear-cut ([7.19.42](/7.19.42#sec-42.1.3)), and approximately neutral at equilibrium. Since the 1950s, burning of coal, oil and gas has increasingly dominated the emissions, and land-use change, mainly tropical deforestation, contributes a smaller and declining share. The Global Carbon Project now publishes each year a budget in which all terms are estimated independently (Friedlingstein et al. 2024); for 2014–2023, in $\mathrm{Pg\,C\,yr^{-1}}$:

| Term | Mean 2014–2023 | How it is estimated |
|---|---|---|
| Fossil emissions $E_{\mathrm{FOS}}$ (including cement) | $9.7 \pm 0.5$ | Energy statistics |
| Land-use change $E_{\mathrm{LUC}}$ | $1.1 \pm 0.7$ | Bookkeeping models of deforestation and regrowth |
| Growth in the atmosphere $G_{\mathrm{ATM}}$ | $5.2 \pm 0.02$ | Direct measurement |
| Ocean sink $S_{\mathrm{OCEAN}}$ | $2.9 \pm 0.4$ | Ocean models and $p_{\ce{CO2}}$ observations |
| Land sink $S_{\mathrm{LAND}}$ | $3.2 \pm 0.9$ | Dynamic vegetation models |
| Budget imbalance $E_{\mathrm{FOS}} + E_{\mathrm{LUC}} - G_{\mathrm{ATM}} - S_{\mathrm{OCEAN}} - S_{\mathrm{LAND}}$ | $-0.4$ | Residual |

About half of the emissions remain in the atmosphere (the airborne fraction, about 0.45 averaged over decades); the rest is taken up roughly equally by the ocean and the land. The land sink is the most variable term: it weakens in El Niño years, when the tropics are hot and dry and fires increase, which is why the atmospheric growth rate fluctuates from year to year although emissions change smoothly.

Until the 1990s, the land sink could not be estimated independently. When the measured emissions and the measured growth in the atmosphere were combined with the ocean uptake calculated from ocean models, about a quarter of the emitted carbon, 1–2 $\mathrm{Pg\,C\,yr^{-1}}$, was unaccounted for: this was the missing sink (Tans et al. 1990). Atmospheric gradients of $\ce{CO2}$ and its isotopes, forest inventories and eddy-covariance measurements have since located it mainly on land in the Northern Hemisphere and in intact tropical forests, and attributed it to regrowth of forests on abandoned farmland and after past logging, fertilization of plant growth by $\ce{CO2}$ and nitrogen deposition, and longer growing seasons. It is now called the residual land sink, and its future is one of the largest uncertainties in climate projections: $\ce{CO2}$ fertilization saturates as nutrients become limiting, and warming increases respiration, drought and fire.

### 45.5.4. A Box Model of the Anthropogenic Perturbation

The response of the atmosphere to emissions can be understood with a four-box model of the excess carbon (the perturbation from the preindustrial state): atmosphere $a$, surface ocean $m$, deep ocean $d$ and land biosphere $b$, all in $\mathrm{Pg\,C}$. The air–sea flux is proportional to the difference in partial pressure between air and water. By the Revelle factor, a relative increase $m/m_0$ of the DIC of the surface ocean raises its partial pressure of $\ce{CO2}$ by $Rm/m_0$, which equals the relative increase $a/a_0$ of the atmosphere when the two are in equilibrium; hence equilibrium requires $a = \alpha m$ with $\alpha = Ra_0/m_0$. Exchange between the surface and deep ocean is by mixing and circulation, with equilibrium at equal relative excess, $m = \beta d$ with $\beta = m_0/d_0$. The land takes up carbon in proportion to the excess $\ce{CO2}$ (fertilization) and returns it with turnover time $\tau$. With emissions $E(t)$:

$$
\begin{aligned}
\frac{\mathrm{d}a}{\mathrm{d}t} &= E - k(a - \alpha m) - ca + \frac{b}{\tau}, &\qquad \frac{\mathrm{d}m}{\mathrm{d}t} &= k(a - \alpha m) - q(m - \beta d), \\
\frac{\mathrm{d}d}{\mathrm{d}t} &= q(m - \beta d), &\qquad \frac{\mathrm{d}b}{\mathrm{d}t} &= ca - \frac{b}{\tau}.
\end{aligned}
$$
This is a linear compartment system with a compartmental matrix, but it is closed: no flux leaves the four boxes, because on these timescales carbon is removed from the ocean–atmosphere–land system only by the slow reaction with carbonate sediments and silicate rocks (thousands to hundreds of thousands of years).

**Proposition 45.5.1 (Long-Term Airborne Fraction)** In the closed four-box model with positive coefficients, a pulse of $1\,\mathrm{Pg\,C}$ emitted into the atmosphere is eventually distributed among the four boxes in the proportions $1 : 1/\alpha : 1/(\alpha\beta) : c\tau$, so that the fraction remaining in the atmosphere tends to

$$
f_\infty = \frac{1}{1 + \dfrac{1}{\alpha} + \dfrac{1}{\alpha\beta} + c\tau} = \frac{1}{1 + \dfrac{m_0 + d_0}{Ra_0} + c\tau}.
$$

**Proof** The column sums of the matrix are zero, so $a + m + d + b$ is conserved and $0$ is an eigenvalue. The other eigenvalues have negative real parts: by Theorem 45.2.1 they have nonpositive real parts, and the graph of exchanges is strongly connected, so the eigenvalue $0$ is simple (its eigenvector is the unique equilibrium distribution) and no other eigenvalue lies on the imaginary axis, by the same argument applied to the system with a small outflow added. Hence the solution converges to the equilibrium with the same total mass. Setting the derivatives to zero gives $a = \alpha m$, $m = \beta d$ and $b = c\tau a$, so the equilibrium is proportional to $(1, 1/\alpha, 1/(\alpha\beta), c\tau)$, and normalizing the total to 1 gives $f_\infty$. $\square$

With $a_0 = 590$, $m_0 = 900$, $d_0 = 37\,000\,\mathrm{Pg\,C}$ and $R = 13$ (a value appropriate to the perturbed ocean), $1/\alpha \approx 0.12$ and $1/(\alpha\beta) \approx 4.8$; with $c\tau = 0.6$, $f_\infty \approx 0.15$. In other words, even after the deep ocean has fully equilibrated, which takes about a thousand years, some 15–25% of an emission remains in the atmosphere (multimodel estimates are about 20%; Joos et al. 2013), and its removal awaits the dissolution of carbonate sediments and the weathering of rocks. Without the buffer chemistry of seawater ($R = 1$), the ocean would absorb almost all of it. The pulse response of the atmosphere is a sum of exponentials with the eigenvalues of the matrix: a rapid partial equilibration with the surface ocean within about a year, uptake by the land over decades, and mixing into the deep ocean over centuries.

![A four-box model of the anthropogenic carbon perturbation (excess carbon in the atmosphere, surface ocean, deep ocean and land biosphere; Revelle factor 13, air–sea equilibration in about one year, surface–deep exchange 0.07 per year, land uptake 0.03 per year per Pg C of excess with a turnover time of 20 years). A: fraction of a pulse of CO₂ remaining in the atmosphere (black) and taken up by the ocean (blue) and the land (green), compared with the fit to the response of comprehensive carbon cycle models by Joos et al. (2013, dashed); after a thousand years about 15% (model) to 22% (multimodel) remains airborne, the equilibrium airborne fraction of Proposition 45.5.1 (dotted). The land store first increases and then returns part of its carbon as the atmospheric excess declines. B: atmospheric CO₂ for a stylized history of emissions (exponential growth to 11 Pg C per year in 2023) followed by constant emissions, a linear decline to net zero in 2060, and net zero in 2050 followed by net removal of 1 Pg C per year. The concentration stops rising only when emissions approach zero, and declines slowly afterwards as the ocean continues to take up carbon.](./plots/carbon-box-model.py)

The model explains three facts about climate policy. First, a constant rate of emissions does not give a constant concentration; the concentration rises as long as emissions exceed the net uptake, which itself depends on the past rise. Second, the warming caused by $\ce{CO2}$ depends, to a good approximation, on cumulative emissions, because the slow decline of the atmospheric excess after emissions stop is roughly offset by the slow uptake of heat by the deep ocean, so that temperature stays roughly constant when net emissions reach zero ([7.19.47](/7.19.47#sec-47.1.3)). Third, a delay in reducing emissions commits the climate for centuries.

### 45.5.5. Regional Carbon Balances

The regional pattern of sources and sinks shows how land use governs the land sink.

- China. Over the past centuries, clearing of forests for agriculture and fuel made the land of China a net source of carbon. Since the 1980s, afforestation, the regrowth of forests on cut-over land, the restoration of grassland and changes in agricultural management have turned it into a net sink: estimates from inventories, satellite data and models give about $0.2$–$0.3\,\mathrm{Pg\,C\,yr^{-1}}$, most of it in forest biomass (Piao et al. 2009; Fang et al. 2018), offsetting roughly a tenth to a seventh of China's fossil emissions of the 2000s. As the young plantations mature, their sink will decline ([7.19.42](/7.19.42#sec-42.2.3)).
- Amazonia. Intact Amazonian forest was long a sink, but the sink has weakened as tree mortality has increased with drought and heat (Brienen et al. 2015). Aircraft measurements of $\ce{CO2}$ over 2010–2018 showed that the southeastern Amazon, where deforestation exceeds 30% and dry-season warming and drying are strongest, is a net source of carbon even when fire emissions are excluded, and that the basin as a whole is a source when fires are counted (Gatti et al. 2021).
- Northern peatlands and permafrost store large amounts of carbon whose release under warming and drainage is a positive feedback on climate ([7.11.30](/7.11.30#sec-30.8)).

### 45.5.6. Carbon Neutrality: the Science of Mitigation

Because warming depends on cumulative emissions, stabilizing the climate requires that net emissions of $\ce{CO2}$ be reduced to zero. The emissions peak (carbon peaking) is the year after which emissions decline; carbon neutrality (net-zero $\ce{CO2}$ emissions) is reached when anthropogenic emissions are balanced by anthropogenic removals. China has committed to peaking its emissions before 2030 and to carbon neutrality before 2060. The scientific basis of the routes is simple bookkeeping of the carbon cycle: reduce the inputs to the atmosphere, and increase the transfers out of it into long-lived reservoirs.

- Reducing emissions: energy efficiency; replacing coal, oil and gas with wind, solar, hydro and nuclear energy; electrification of transport and heating; reducing emissions from cement and steel; halting deforestation.
- Enhancing biological sinks: afforestation and reforestation, restoration of peatlands and wetlands, "blue carbon" in mangroves, salt marshes and seagrass meadows, and management of soils to increase organic carbon. Biological stores are vulnerable to fire, drought and changes of land use, and they saturate as ecosystems approach equilibrium (Proposition 42.1.1 of [7.19.42](/7.19.42#sec-42.1.3)).
- Carbon capture and storage (CCS): $\ce{CO2}$ is separated from the flue gas of power plants and factories (by absorption in amine solutions, or by burning fuel in oxygen so that the exhaust is almost pure $\ce{CO2}$), compressed and injected into deep geological formations, such as saline aquifers and depleted oil and gas fields, at depths of more than about 800 m, where it is a dense supercritical fluid. It is retained by an impermeable cap rock (structural trapping), as droplets in pore spaces (residual trapping), by dissolution in formation water and, slowly, by reaction with minerals to form carbonates. In reactive basalts, injected $\ce{CO2}$ dissolved in water was more than 95% mineralized within two years (Matter et al. 2016). Combining CCS with bioenergy (BECCS) or with the direct capture of $\ce{CO2}$ from air (DACCS) removes $\ce{CO2}$ from the atmosphere, at large costs in energy and, for BECCS, land.

The ecological questions raised by these routes, the competition of bioenergy plantations with food production and biodiversity and the use of monoculture plantations as carbon sinks, are discussed in [7.19.50](/7.19.50) and [7.19.54](/7.19.54).

## Summary

- Matter cycles while energy flows through ecosystems once; decomposers close the cycles. Global cycles are hydrological, gaseous (C, N, O; buffered) or sedimentary (P, Ca, K; open, closed only by geological uplift); sulfur is mixed. Within ecosystems, internal cycling of N and P is usually an order of magnitude larger than inputs and outputs.
- Compartment models (Definition 45.2.1): $\dot{\boldsymbol{x}} = A\boldsymbol{x} + \boldsymbol{b}$ with a compartmental matrix. Turnover time $T = Q/F$ and residence time (Definition 45.2.2). Eigenvalues have nonpositive real parts, negative if the system is outflow-connected, and the steady state is $\boldsymbol{x}^* = (-A)^{-1}\boldsymbol{b} \ge \boldsymbol{0}$ (Theorem 45.2.1); the fundamental matrix gives the mean time spent in each compartment and the mean transit time (Proposition 45.2.1); total stock = input × mean transit time (Proposition 45.2.2). Tight cycling multiplies residence time ($u/\lambda$ cycles). Gross turnover time and the adjustment time of a perturbation differ (atmospheric $\ce{CO2}$: about 4 years against centuries).
- Nutrient budgets: inputs from weathering, atmosphere (wetfall, dryfall, fixation), water and humans; outputs as gases, in drainage water and by harvest. At Hubbard Brook, felling uncoupled uptake from mineralization and increased nitrate export about 60-fold; streams spiral nutrients downstream; endorheic lakes and the ocean lose elements only to sediments.
- Water: 96.5% in the oceans, less than 0.01% in lakes and rivers; atmospheric residence time about 10 days; transpiration is about 60% of evapotranspiration on land; warming increases the intensity and variability of precipitation (about 7% more vapour per kelvin).
- Carbon: pools (atmosphere 870, vegetation 450, soils 1700, permafrost 1400, deep ocean 37 000 Pg C); the carbonate system of seawater, the Revelle factor (about 10; Definition 45.5.1) and ocean acidification (Definition 45.5.2; pH −0.1 since 1750). Global budget 2014–2023: emissions 10.8, atmosphere 5.2, ocean 2.9, land 3.2 Pg C per year; the former missing sink is the residual land sink.
- Box model: closed four-box system, pulse response with time constants of about 1, 10–100 and 1000 years; long-term airborne fraction $f_\infty = [1 + (m_0 + d_0)/(Ra_0) + c\tau]^{-1} \approx 0.15$–$0.2$ (Proposition 45.5.1). Concentration stabilizes only when net emissions approach zero.
- China's land changed from a historical source to a sink of about 0.2–0.3 Pg C per year; the southeastern Amazon has become a source. Carbon neutrality requires emission reductions, durable sinks and storage (CCS, mineralization).

## Questions

1. A lake contains $50\,\mathrm{kg}$ of phosphorus in its water; inflowing streams bring $20\,\mathrm{kg\,yr^{-1}}$, the outflow removes $8\,\mathrm{kg\,yr^{-1}}$, and the rest settles to the sediments. Assuming a steady state, calculate the turnover time of phosphorus in the water. Phytoplankton take up $2\,\mathrm{kg}$ of phosphate per day from the dissolved pool of $1\,\mathrm{kg}$ and release as much. What is the turnover time of dissolved phosphate, and why are the two turnover times so different?

   **Answer** At steady state the throughput is $20\,\mathrm{kg\,yr^{-1}}$ (inflow = outflow + sedimentation $= 8 + 12$), so the turnover time of phosphorus in the water is $50/20 = 2.5$ years. For dissolved phosphate the throughput is the gross uptake, $2\,\mathrm{kg\,d^{-1}}$, and the turnover time is $1/2$ day, or 12 hours. The first is a turnover with respect to the inputs and outputs of the lake; the second is a turnover within the internal cycle between dissolved phosphate and plankton (and their excretion and decomposition), which is many times faster. By the counting argument of 45.2.3, an atom of phosphorus passes through the plankton about $2.5 \times 365/0.5 \approx 1800$ times before leaving the water, on average. Low phosphate concentrations in productive lakes therefore indicate rapid uptake, not low supply.

2. Show that for the two-compartment model $\dot x_1 = -k_{21}x_1 + k_{12}x_2 + b$, $\dot x_2 = k_{21}x_1 - (k_{12} + k_{02})x_2$, the eigenvalues are real and negative, and compute the mean transit time of an atom entering compartment 1. Interpret the case $k_{12} \gg k_{02}$.

   **Answer** The trace is $-(k_{21} + k_{12} + k_{02}) < 0$ and the determinant $k_{21}(k_{12} + k_{02}) - k_{12}k_{21} = k_{21}k_{02} > 0$; the discriminant $(k_{21} + k_{12} + k_{02})^2 - 4k_{21}k_{02} \ge (k_{21} - k_{02})^2 + k_{12}^2 + 2k_{12}(k_{21} + k_{02}) > 0$ is positive, so both eigenvalues are real and negative. The fundamental matrix is $N = (-A)^{-1} = \frac{1}{k_{21}k_{02}}\begin{bmatrix} k_{12} + k_{02} & k_{12} \\ k_{21} & k_{21} \end{bmatrix}$, so an atom entering compartment 1 spends on average $(k_{12} + k_{02})/(k_{21}k_{02})$ in compartment 1 and $1/k_{02}$ in compartment 2, a mean transit time $\tau_1 = \frac{1}{k_{21}} + \frac{1}{k_{02}} + \frac{k_{12}}{k_{21}k_{02}}$. If $k_{12} \gg k_{02}$, most atoms leaving compartment 2 return to compartment 1; each atom makes on average $k_{12}/k_{02}$ return trips, and the last term dominates. Recycling, not slow compartments, makes the transit time long.

3. Explain why felling a forest increases nitrate losses much more than sodium losses, and predict how the result of the Hubbard Brook experiment would have differed in a forest on deep, nitrogen-poor sandy soil whose vegetation was nitrogen-limited.

   **Answer** Nitrate is the product of nitrification of ammonium released by decomposers; in the intact forest it is taken up almost completely by roots and microorganisms because nitrogen is in short supply relative to demand, so its export is very low and depends entirely on biological uptake. Felling removes the uptake while mineralization continues (even accelerates in the warmer, wetter soil), so export rises by a factor of the order of the ratio of internal cycling to export. Sodium is barely required by plants, is cycled weakly, and is lost at nearly the rate at which it is supplied; felling changes its export mainly through the increase in runoff (here 40%) and in weathering. In a nitrogen-limited forest on poor soil, the soil organic matter would have a high C:N ratio, decomposers would immobilize much of the mineral nitrogen in their own biomass, and nitrification would be slow; the nitrate pulse after felling would be smaller and delayed, while losses of other ions would be governed by the increased water flux through a poorly buffered sandy soil.

4. Using the four-box model, explain (a) why the atmospheric $\ce{CO2}$ excess decays quickly at first and then slowly, (b) why the long-term airborne fraction would be close to $1/(1 + 1/\alpha + c\tau)$, about 0.5, if the deep ocean did not exist, and (c) why the airborne fraction would increase if the Revelle factor rose.

   **Answer** (a) The pulse response is a sum of exponentials with the eigenvalues of the matrix: the largest in magnitude, about $-k(1 + \alpha) \approx -1\,\mathrm{yr^{-1}}$, equilibrates the atmosphere with the surface ocean; but the surface ocean can absorb only about $1/\alpha$ of the excess, so the first decline is small. Then land uptake (decades) and mixing into the deep ocean (centuries, eigenvalue of order $q\beta(1 + 1/\alpha)$) take over, slowly. (b) Without the deep ocean, the total capacity outside the atmosphere is only that of the surface ocean ($1/\alpha \approx 0.12$) and the land ($c\tau$), so with $c\tau = 0.6$ the equilibrium airborne fraction would be $1/(1 + 0.12 + 0.6) \approx 0.58$. The deep ocean, through its size $d_0$, provides most of the long-term capacity. (c) A higher Revelle factor reduces $1/\alpha = m_0/(Ra_0)$ and $1/(\alpha\beta) = d_0/(Ra_0)$, the equilibrium capacities of both ocean boxes, because each unit of carbon added to seawater raises its $p_{\ce{CO2}}$ more; hence $f_\infty$ increases. Since $R$ rises with the amount of $\ce{CO2}$ absorbed, the ocean sink becomes relatively weaker as emissions accumulate, a positive feedback.

5. (Open question) A company proposes to offset its emissions by planting a fast-growing monoculture plantation that will be harvested every 15 years for paper. Analyze, using the concepts of this chapter, whether this is a lasting carbon sink.

   **Answer** Key points: a sink is a net transfer from the atmosphere into a reservoir that lasts; what matters is the change in the total stock of the system (biomass, litter, soil and products), not the gross uptake. A plantation harvested every 15 years accumulates carbon during each rotation but releases most of it when the paper decays or is burned (product turnover times of a few years), so averaged over rotations the long-term stock gain is only the mean standing biomass (about half the maximum), plus or minus changes in soil carbon; soils of managed forests can lose carbon (Noormets et al. 2015). The baseline matters: if the plantation replaces natural forest, it is a net source; if it is planted on degraded farmland, it is a modest sink until a new steady state is reached (Proposition 42.1.1). Permanence (fire, drought, pests in monocultures), leakage (displaced agriculture clearing forest elsewhere), and effects on water use and biodiversity must also be counted. A fossil emission adds carbon whose atmospheric excess persists for centuries (Proposition 45.5.1), whereas a biological store is reversible; offsetting is therefore weaker than avoiding emissions.
