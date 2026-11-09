---
title: Cell Expansion and Growth Kinetics
description: "Growth, differentiation and development; cell wall physiology: microfibril orientation and anisotropic growth, diffuse and tip growth, wall stress; the Lockhart equation, yield threshold and wall extensibility, coupling to water uptake and stress relaxation; the acid growth hypothesis and expansins, other hormones and elongation; growth measurement and growth analysis (RGR = NAR × LAR); the grand period of growth and logistic and Gompertz curves; cardinal temperatures, thermoperiodism and thermal time, effects of light, water and minerals; root–shoot ratio, functional balance and allometry."
source_hash: 70ab51b93d4c
---

Almost all of plant form is shaped by growth. A plant cannot let its cells migrate and fold into shape the way an animal embryo does; every organ results from cells produced by meristems expanding in place, and the direction and rate of that expansion are set by the cell wall that surrounds each cell. This chapter moves from the scale of the cell to that of the whole plant and the stand. We first show how cells enlarge by letting the wall yield under **turgor pressure** (the Lockhart equation, acid growth and expansins). We then show how to measure and describe whole-plant growth (the relative growth rate and its decomposition, the S-shaped curve of the grand period of growth). Finally we treat how temperature, light, water and nutrients modify growth, and the growth proportions between roots and shoots.

This chapter opens the group of chapters on growth and development (Chapters 17–24). Wall structure has already been covered in botany ([7.12.3](/7.12.3)) and cell biology ([7.3.23](/7.3.23#sec-23.6)); here we deal only with its physiology, namely how the wall controls growth. The synthesis and signaling of auxin, gibberellins and other hormones are in the three hormone chapters ([7.13.13](/7.13.13), [7.13.14](/7.13.14), [7.13.15](/7.13.15)), and the inhibition of elongation by light is in [7.13.16](/7.13.16). How organs arise at the shoot and root apices is the subject of the next chapter ([7.13.18](/7.13.18)). The water potential concept used here comes from [7.13.2](/7.13.2), and the mathematics of growth curves is the same as that of batch culture of microorganisms ([7.11.8](/7.11.8)).

## 17.1. Growth, Differentiation and Development

### 17.1.1. Three Basic Concepts

**Definition 17.1.1 (Growth, Differentiation and Development)** The irreversible increase of a plant or organ in morphological measures such as volume, mass or cell number is called **growth**; it is a quantitative change. The process by which cells produced by meristems become different from one another in structure, function and physiological and biochemical properties is called **differentiation**; it is a qualitative change. The whole process in which growth and differentiation proceed in an orderly way in time and space, so that organs and the individual are gradually formed and the life cycle is completed, is called **development**.

"Irreversible" is the key word in the definition of growth. A leaf that shrinks by losing water during the day and recovers by taking up water at night does not grow, because this volume change is reversible; the swelling of a seed on imbibition is mainly hydration of colloids and does not count as growth either. Growth is therefore measured by dry mass, cell number or irreversible increase in length. The relations among the three concepts can be summarized as follows.

- Growth is a quantitative change and is the basis; differentiation is a qualitative change; development includes both growth and differentiation and is the orderly quantitative and qualitative change of an organ or the whole plant.
- Growth and differentiation are in turn constrained by developmental stage: a plant can initiate flowering only after reaching a certain stage, and the differentiation of the rice young panicle can proceed only after photoperiodic induction ([7.13.21](/7.13.21)).
- All three are regulated jointly by heredity, hormones and the environment: hormones convey information between cells, and environmental signals such as light, temperature, water and gravity, through intracellular signal transduction, ultimately change growth and differentiation by regulating gene expression.

Starting from the zygote, a plant passes in turn through embryogenesis, **seed germination**, formation of the vegetative body, formation of reproductive organs and flowering and fruiting, and finally senescence and death; this sequence is called a growth and development cycle. Annual plants complete the cycle within one growing season and flower only once (monocarpic); perennials retain many vegetative shoots at each flowering and fruiting (polycarpic).

### 17.1.2. Characteristics of Plant Growth

Plant growth differs from animal growth in three fundamental ways.

1. Growth is concentrated in **meristems**. The **apical meristems** of root and shoot tips elongate the organ (primary growth), while the vascular cambium and cork cambium thicken it ([7.12.4](/7.12.4)). When an initial cell of a meristem divides, one daughter cell keeps the properties of the initial and the other enters differentiation, so the meristem "renews itself".
2. Growth may be determinate or indeterminate. Leaves, flowers and fruits stop growing once they reach a certain size (determinate growth), whereas the apical meristems of roots and shoots can produce new organs indefinitely (indeterminate growth), and some trees live for thousands of years.
3. Increase in volume depends mainly on cell expansion rather than cell division. Meristematic cells are about $10\,\mu\mathrm{m}$ in diameter, and the volume of a mature cell is usually 10–1000 times as large; a vessel element may be more than 10 000 times as large. The bulk of expansion is water uptake by the **vacuole**: the small vacuoles of meristematic cells swell in the elongation zone by taking up water and fuse into a central vacuole, while the cytoplasm increases very little.

The growth of an organ can therefore be divided into three spatially successive phases: the division phase (meristematic zone, in which cell number increases and protoplasm synthesis is vigorous), the elongation phase (elongation zone, in which volume increases rapidly, the contents of nucleic acids, proteins and wall materials rise markedly, the activity of some enzymes increases, and the respiration rate rises 2–6-fold) and the differentiation phase (maturation zone, in which cells form the various tissues). In a root tip these three zones are arranged one after another within a few millimeters ([7.12.20](/7.12.20)). The regulation of the division cycle is essentially the same as in animals (the **cell cycle**, [7.3.20](/7.3.20)), and hormones act mainly at the $\mathrm{G_1/S}$ and $\mathrm{G_2/M}$ checkpoints; this chapter concentrates on cell expansion.

## 17.2. The Cell Wall and Anisotropic Growth

### 17.2.1. Composition of the Primary Wall

A growing cell has only a **primary cell wall**, which is thin (about $0.1$–$1\,\mu\mathrm{m}$) and extensible. After growth stops, some cells deposit a **secondary cell wall** on the inner side of the primary wall, and the secondary wall no longer expands. The primary wall is a fiber-reinforced composite.

| Component | Share of primary wall dry weight | Structure | Role in growth |
|---|---|---|---|
| Cellulose | 20 %–30 % | β-1,4-glucan chains aggregate through hydrogen bonds into **cellulose microfibrils** (about 3 nm in diameter), synthesized at the plasma membrane by **cellulose synthase** complexes | The tension-bearing "reinforcing bars"; determines the direction of expansion |
| Hemicellulose (cross-linking glycans) | 20 %–25 % | Xyloglucan predominates in dicots and glucuronoarabinoxylan in grasses; synthesized in the Golgi apparatus | Binds to microfibrils and regulates the linkages among them |
| Pectin | 10 %–35 % | Acidic polysaccharides rich in galacturonic acid, cross-linked by $\ce{Ca^2+}$ into a gel; synthesized in the Golgi apparatus | Hydrophilic matrix; forms the middle lamella |
| Protein | 5 %–10 % | Structural proteins such as extensins; enzymes such as xyloglucan endotransglucosylase and nonenzymatic proteins such as expansins | Stiffen and loosen the wall |

Wall formation results from the cooperation of several organelles. During cytokinesis, vesicles derived from the Golgi apparatus and the endoplasmic reticulum line up on the equatorial plane along the microtubules of the phragmoplast and fuse to form the cell plate (the middle lamella, which is mainly pectin). Afterward the Golgi apparatus continues to secrete matrix polysaccharides, whereas cellulose is synthesized directly by "rosette"-shaped cellulose synthase complexes in the plasma membrane and extruded into the wall; the substrate UDP-glucose is mostly derived from the breakdown of sucrose by sucrose synthase ([7.13.12](/7.13.12)). Many glucan chains lie in parallel and aggregate into microfibrils through interchain hydrogen bonds, which makes cellulose extremely strong and resistant to chemical degradation.

For how the polysaccharides in the wall are connected, textbooks long used the "tethered network" model: xyloglucan coats the surface of microfibrils and spans the gaps between them, tethering them like cables into a load-bearing network, while pectin forms a second, interpenetrating network. Solid-state NMR results have undermined this model: only about 10 % of the microfibril surface is covered by xyloglucan, pectin is in direct contact with cellulose, and *Arabidopsis* mutants that contain no xyloglucan at all show only a mild phenotype. The prevailing view is now the "biomechanical hotspot" model: most xyloglucan is not load-bearing, and the mechanical properties and extension of the wall are controlled by a few junctions where microfibrils lie in close contact, with xyloglucan trapped in these junctions (Park and Cosgrove 2012). The wall-loosening mechanisms discussed below all act on these junctions.

### 17.2.2. Wall Stress

Turgor pressure produces a tensile stress in the cell wall that is much larger than the pressure itself. Treat an elongating cell as a thin-walled cylinder of radius $r$ and wall thickness $\delta$. Force balance (the same calculation as for a pressure vessel) gives the circumferential and axial stresses in the wall:

$$
\sigma_\theta = \frac{Pr}{\delta}, \qquad \sigma_z = \frac{Pr}{2\delta},
\tag{17.1}
$$

where $P$ is the **turgor pressure** (that is, the **pressure potential** $\Psi_{\mathrm{p}}$, [7.13.2](/7.13.2)). The circumferential stress is twice the axial stress.

**Example 17.2.1 (Wall Stress)** An elongating cortical cell has $r = 10\,\mu\mathrm{m}$, primary wall thickness $\delta = 0.1\,\mu\mathrm{m}$ and turgor pressure $P = 0.5\,\mathrm{MPa}$. By Eq. (17.1), $\sigma_\theta = 0.5 \times 10/0.1 = 50\,\mathrm{MPa}$ and $\sigma_z = 25\,\mathrm{MPa}$. The turgor pressure of growing cells is usually $0.3$–$1.0\,\mathrm{MPa}$, so the wall stress lies between $10$ and $100\,\mathrm{MPa}$, within an order of magnitude of the yield strength of mild steel. By comparison, the forces the cytoskeleton can generate are negligible: animal cells change shape by means of the cytoskeleton, whereas plant cells can change shape only by controlling in which direction and how fast the wall yields.

### 17.2.3. Microfibril Orientation and Anisotropic Growth

Turgor pressure is equal in all directions, but wall extension is anisotropic. Microfibrils resist tension, so the wall can hardly lengthen along the microfibrils and can only extend perpendicular to them, by letting microfibrils slide apart. The direction of cell expansion is therefore determined by the orientation of the newly deposited microfibrils (see the figure below).

- Meristematic cells are isodiametric. If the microfibrils in the primary wall are randomly oriented, the cell expands isotropically and tends toward a sphere.
- In the side walls of elongating cells such as those of the cortex and vascular tissues of stems and roots, microfibrils are deposited circumferentially (transversely) and restrict radial expansion like barrel hoops, so the cell can only elongate along its long axis. Equation (17.1) shows that the circumferential stress is the largest, and transverse microfibrils reinforce exactly this direction.
- The orientation of microfibrils is determined by that of the cortical **microtubules** beneath the plasma membrane: cellulose synthase complexes move along microtubule tracks ([7.3.14](/7.3.14)), and drugs that depolymerize microtubules (such as colchicine and oryzalin) make newly deposited microfibrils disorganized and elongating cells swollen. Within tens of minutes **ethylene** turns the cortical microtubules of etiolated hypocotyl cells from transverse to longitudinal, the microfibrils deposited afterward also become longitudinal, and the cells therefore expand laterally with elongation inhibited; this is the cause of the thickened hypocotyl in the **triple response** ([7.13.15](/7.13.15)). Gibberellins and auxin favor maintaining the transverse arrangement.

According to the multinet growth hypothesis, each newly deposited layer of transverse microfibrils is stretched and thinned as the cell elongates, and the microfibrils in the older outer layers are passively reoriented toward the longitudinal direction; not all cells fit this picture, however, and expansion is controlled mainly by the innermost quarter or so of the wall. In the shoot apex, cortical microtubules also align along the direction of maximal mechanical stress in the tissue, so that the wall is reinforced where the load is greatest, forming a mechanical feedback among wall, cytoskeleton and organ shape (Hamant et al. 2008).

![Microfibril orientation determines the direction of cell expansion (schematic). In each pair, the left cell is an isodiametric meristematic cell, pink arrows indicate that turgor pressure is equal in all directions, and green lines indicate newly deposited cellulose microfibrils in the primary wall; the right cell is the cell after expansion, and double-headed arrows indicate the direction of expansion. A: Microfibrils are randomly oriented, the wall yields equally easily in all directions, and the cell expands isotropically. B: Microfibrils are oriented circumferentially (transversely) and restrict radial expansion like barrel hoops, so the cell elongates along its long axis, the typical case for elongating cells of stems and roots. C: Microfibrils are oriented longitudinally (for example after ethylene turns the cortical microtubules by 90°), so the cell expands laterally with elongation inhibited](./plots/anisotropy.py)

### 17.2.4. Diffuse Growth and Tip Growth

According to where the wall surface expands, cell growth falls into two types.

| | Diffuse growth | Tip growth |
|---|---|---|
| Site of expansion | The entire wall surface (rates may differ among regions) | Only the hemispherical region at the tip of a tubular cell |
| Examples | Most cells: cortical, vascular and mesophyll cells | **Root hairs** and **pollen tubes**; fungal hyphae and moss protonemata |
| Rate | Surface area increases by about 1 %–10 % per hour | The wall at the tip doubles in area within minutes and then moves to the nonexpanding flank |
| Deposition of wall material | Dispersed | Golgi vesicles exocytose at the tip, accompanied by a tip-focused $\ce{Ca^2+}$ gradient and oscillations |
| Main risk | Wall too thick or insufficient expansion | The wall thins and bursts; deposition and expansion must be coordinated precisely |

There are also intermediate cases: the pavement cells of the leaf epidermis of many dicots interlock like jigsaw pieces, and their protruding lobes resemble local tip growth, formed by the small GTPase ROP and its effector proteins organizing actin filaments and microtubules.

## 17.3. The Lockhart Equation

### 17.3.1. Growth as Coupling of Wall Yielding and Water Uptake

The wall is a viscoelastic material. When tension is applied, it first extends elastically (reversibly); the wall of a growing cell, under sufficiently large tension, also extends slowly and irreversibly with time, that is, it undergoes creep, which results from sliding of wall polymers past one another; the walls of mature cells have almost no such property. Cell expansion can be viewed as two coupled steps.

1. Wall relaxation: the linkages among wall polymers are loosened biochemically, and the wall yields and lengthens under the tensile stress produced by turgor. This lowers both the wall stress and the turgor pressure, and is called stress relaxation.
2. Water uptake: the drop in turgor lowers the cell's **water potential** $\Psi_{\mathrm{w}} = \Psi_{\mathrm{s}} + \Psi_{\mathrm{p}}$, creating a water potential difference between the cell and the water source; water flows into the cell, the volume increases and turgor recovers.

Without stress relaxation, synthesis of wall material would only thicken the wall without enlarging the cell (as in the thickening of secondary walls); without water uptake, relaxation would only lower turgor. The water potential of a growing tissue is therefore always slightly lower than that of the supplying xylem, and the difference (the growth-induced water potential) is usually $0.05$–$0.3\,\mathrm{MPa}$. New wall material is continually added, so the wall does not thin even when it expands more than tenfold.

### 17.3.2. The Equation

**Definition 17.3.1 (Lockhart Equation)** When the turgor pressure $P$ exceeds a critical value $Y$, the relative rate of volume expansion of the cell is proportional to the excess turgor:

$$
\frac{1}{V}\frac{\mathrm{d}V}{\mathrm{d}t} = \begin{cases} \phi\,(P - Y), & P > Y, \\ 0, & P \le Y, \end{cases}
\tag{17.2}
$$
where $\phi$ is called the **wall extensibility** (in $\mathrm{h^{-1}\,MPa^{-1}}$) and $Y$ the **yield threshold** (in $\mathrm{MPa}$). This relation is called the Lockhart equation (Lockhart 1965).

Equation (17.2) describes the wall as a Bingham-type viscoplastic material: it does not flow below the yield stress and flows in proportion to the excess above it. The yield threshold of growing tissues is usually $0.1$–$0.5\,\mathrm{MPa}$, which is $0.1$–$0.3\,\mathrm{MPa}$ below the turgor pressure; from diffuse growth rates of 1 %–10 % per hour, $\phi$ is of the order of a few tenths per hour per megapascal. A change in any of turgor, $\phi$ and $Y$ can change the growth rate; hormones and the environment act mainly by changing $\phi$ and $Y$ (the "yielding properties" of the wall) (panel A of the Lockhart-model figure in Section 17.3.3).

The rate of water uptake of the same cell is determined by the water potential difference across the membrane (or through the tissue):

$$
\frac{1}{V}\frac{\mathrm{d}V}{\mathrm{d}t} = L\,(\Psi_{\mathrm{o}} - \Psi_{\mathrm{w}}) = L\,(\Delta\pi - P), \qquad \Delta\pi = \Psi_{\mathrm{o}} - \Psi_{\mathrm{s}},
\tag{17.3}
$$

where $L$ is the volume-normalized relative hydraulic conductance, $\Psi_{\mathrm{o}}$ is the water potential of the source (xylem or external solution), and $\Delta\pi$ is the effective osmotic driving force ($\Psi_{\mathrm{s}}$ is the **solute potential** of the cell). At steady state, wall expansion equals water uptake; equating Eq. (17.2) and Eq. (17.3) and solving gives the steady-state turgor pressure and growth rate:

$$
P^* = \frac{L\,\Delta\pi + \phi\,Y}{L + \phi}, \qquad
\frac{1}{V}\frac{\mathrm{d}V}{\mathrm{d}t} = \frac{\phi L}{\phi + L}\,(\Delta\pi - Y).
\tag{17.4}
$$

Equation (17.4) resembles two "conductances" in series: the smaller of wall extensibility and hydraulic conductance limits growth. In most growing tissues $L \gg \phi$, growth is wall-controlled, and $P^*$ is close to $\Delta\pi$; when hydraulic conductance is low or water is scarce ($L$ small or $\Psi_{\mathrm{o}}$ low), water uptake becomes the limiting factor. Ortega (1985) added an elastic term $\frac{1}{\varepsilon}\frac{\mathrm{d}P}{\mathrm{d}t}$ to Eq. (17.2), where $\varepsilon$ is the **volumetric elastic modulus**, obtaining an extended form that can describe turgor transients:

$$
\frac{1}{V}\frac{\mathrm{d}V}{\mathrm{d}t} = \phi\,(P - Y) + \frac{1}{\varepsilon}\frac{\mathrm{d}P}{\mathrm{d}t}.
\tag{17.5}
$$

### 17.3.3. Measuring the Yield Threshold and Extensibility

By Eq. (17.5), if the water supply is cut off ($\mathrm{d}V/\mathrm{d}t = 0$), the wall still yields, and the turgor pressure falls exponentially to $Y$ according to

$$
P(t) = Y + (P_0 - Y)\,\mathrm{e}^{-t/\tau}, \qquad \tau = \frac{1}{\varepsilon\phi}.
\tag{17.6}
$$
This is the basis of the in vivo stress relaxation method (Cosgrove 1985): a growing stem segment is excised from its water source and placed at saturating humidity to prevent transpiration, and turgor is followed with a pressure chamber or pressure probe; the final value of turgor gives $Y$, and the decay time constant gives $\varepsilon\phi$ (panel B of the figure below). Another method measures the growth rate at different osmotic potentials of the external solution and obtains the slope $\phi$ and the intercept $Y$ from the straight line of $\mathrm{d}V/\mathrm{d}t$ against turgor. Isolated walls (killed by freezing and thawing, with turgor removed) are subjected to constant load in an extensometer and their creep is measured, to study the relaxation mechanism of the wall itself (Section 17.4).

**Example 17.3.1 (Steady-State Growth and Stress Relaxation)** An etiolated hypocotyl segment has $\phi = 0.20\,\mathrm{h^{-1}\,MPa^{-1}}$, $Y = 0.30\,\mathrm{MPa}$, $L = 1.0\,\mathrm{h^{-1}\,MPa^{-1}}$, cell solute potential $\Psi_{\mathrm{s}} = -0.80\,\mathrm{MPa}$, xylem water potential $\Psi_{\mathrm{o}} = -0.10\,\mathrm{MPa}$ and $\varepsilon = 10\,\mathrm{MPa}$.

$\Delta\pi = -0.10 - (-0.80) = 0.70\,\mathrm{MPa}$. By Eq. (17.4), $P^* = (1.0 \times 0.70 + 0.20 \times 0.30)/1.2 = 0.633\,\mathrm{MPa}$, and the relative growth rate is $0.20 \times (0.633 - 0.30) = 0.067\,\mathrm{h^{-1}}$, that is, 6.7 % per hour. The cell water potential is $\Psi_{\mathrm{w}} = -0.80 + 0.633 = -0.167\,\mathrm{MPa}$, which is $0.067\,\mathrm{MPa}$ below that of the xylem; this is the growth-induced water potential difference that drives water uptake. After the water source is cut off, Eq. (17.6) gives $\tau = 1/(10 \times 0.20) = 0.5\,\mathrm{h}$: after 30 min turgor falls to $0.30 + 0.333\,\mathrm{e}^{-1} = 0.42\,\mathrm{MPa}$, and after about 2 h it approaches the yield threshold and growth stops. If auxin doubles $\phi$ and lowers $Y$ to $0.20\,\mathrm{MPa}$, then $P^* = (0.70 + 0.4 \times 0.20)/1.4 = 0.557\,\mathrm{MPa}$ and the growth rate is $0.40 \times 0.357 = 0.143\,\mathrm{h^{-1}}$, about 2.1 times the original, while turgor actually decreases. When auxin promotes growth, turgor falls rather than rises, which is exactly the evidence that wall loosening (rather than osmotic adjustment) drives growth.

:::

![The Lockhart model (illustrative parameters). A: Relative growth rate as a function of turgor pressure (Eq. (17.2)). There is no growth below the yield threshold Y (dot), and above Y the rate rises with slope φ (wall extensibility, in h⁻¹ MPa⁻¹). Acidification (acid growth by auxin) both raises φ and lowers Y, and gibberellin mainly raises φ; the vertical dashed line marks the typical turgor of a growing cell. B: Model coupling wall yielding and water uptake (Eqs. (17.3)–(17.5), parameters as in Example 17.3.1). In the gray interval the water source is cut off and the wall continues to yield at constant volume; turgor (blue) decays exponentially toward the yield threshold (dashed) with time constant τ = 1/(εφ), and the growth rate (red) falls accordingly. When the supply is restored, both quickly return to steady state](./plots/lockhart.py)

## 17.4. The Acid Growth Hypothesis and Expansins

### 17.4.1. Acid Growth

Growing walls extend much faster at acidic pH than at neutral pH. Growing stem segments or coleoptile sections placed in a buffer of pH 4.5–5 grow rapidly without any hormone, and fusicoccin, a fungal toxin that activates the plasma membrane $\ce{H+}$-ATPase, also acidifies the wall and causes rapid growth. Isolated walls show the same property: when the wall of a freeze–thaw-killed etiolated cucumber hypocotyl is clamped in an extensometer under constant load, it extends only briefly at pH 7, but when the buffer is changed to pH 4.5 it immediately begins creeping for several hours (Durachko and Cosgrove 2009).

**Definition 17.4.1 (Acid Growth Hypothesis)** Auxin activates the plasma membrane $\ce{H+}$-ATPase, protons are pumped into the cell wall and the wall pH falls, wall-loosening factors in the wall are activated under acidic conditions, the extensibility of the wall increases, and the cell elongates driven by turgor; this explanation is called the **acid growth hypothesis**.

The evidence for this hypothesis is as follows.

- The time courses agree: in oat coleoptile or soybean hypocotyl segments, auxin-induced acceleration of elongation has a lag of about 10–15 min and reaches a maximal rate 5–10 times the basal rate after 30–60 min; wall acidification (measured with a pH microelectrode) has the same lag and precedes or accompanies the acceleration of elongation (Taiz et al.).
- Sufficiency: acidic buffers and fusicoccin can both replace auxin.
- Necessity: neutral buffers infiltrated into the wall, or inhibitors of the plasma membrane $\ce{H+}$-ATPase (a **P-type ATPase**) such as vanadate, inhibit auxin-induced rapid growth.
- At the initiation of a root hair, the wall pH at the outward bulge of the epidermal cell locally drops to about 4.5.

How auxin activates the proton pump is now fairly well understood. The intracellular TIR1/AFB receptor pathway induces expression of *SAUR* genes, and SAUR proteins inhibit the PP2C.D phosphatases that dephosphorylate the proton pump, so that the penultimate threonine at the C terminus of the pump remains phosphorylated, binds 14-3-3 proteins and keeps the pump active (Spartz et al. 2014); the cell-surface TMK kinases directly phosphorylate and activate the proton pump within minutes of auxin action (Lin et al. 2021). Roots respond to auxin in the opposite way: auxin causes rapid alkalinization of the apoplast in roots and inhibits elongation (Li et al. 2021), consistent with the much higher sensitivity of roots than stems to auxin (Section 17.4.3). For receptor and signal transduction details see [7.13.13](/7.13.13) and [7.1.15](/7.1.15#sec-15.5.2).

Acid growth explains only the rapid phase of auxin action. Auxin-induced elongation can continue for hours to days, which requires continued synthesis of wall material, uptake of solutes (to maintain $\Psi_{\mathrm{s}}$) and gene expression; treatment with inhibitors of RNA and protein synthesis inhibits it after a somewhat longer lag.

### 17.4.2. Expansins

Walls that have been heated or treated with protease lose the capacity for acid growth, which shows that acid growth is not a simple physicochemical property of the wall (such as softening of the pectin gel) but is catalyzed by wall proteins. Reconstitution experiments confirmed this: proteins extracted from growing walls and added to heat-inactivated walls restored acid-induced creep, and the active proteins were named expansins (McQueen-Mason, Durachko and Cosgrove 1992).

**Definition 17.4.2 (Expansin)** A class of proteins located in the cell wall that cause time-dependent irreversible extension (creep) and stress relaxation of the wall at acidic pH without themselves hydrolyzing wall polysaccharides is called **expansins**.

Properties of expansins are as follows.

- They act in catalytic amounts: about 1 part protein (by dry weight) to 5000 parts wall is sufficient; they have no detectable hydrolase or other enzymatic activity; the optimal pH is about 4.5.
- They form a large superfamily, mainly the α-expansin (EXPA) and β-expansin (EXPB) families. EXPA is more effective on dicot walls and acts on cellulose–cellulose junctions that contain xyloglucan; EXPB is more effective on grass walls (the abundant EXPB in grass pollen is one of the main pollen allergens and may help pollen tubes penetrate stigma tissue).
- The mechanism is not fully understood; most evidence indicates that they loosen noncovalent adhesion among wall polysaccharides, and the site of action is exactly the "hotspot" where microfibrils lie in close contact described in Section 17.2.1.
- A few bacteria and fungi also have expansin-like proteins, used to invade plant tissue, possibly acquired from plants by horizontal gene transfer.

Other wall proteins regulate the long-term properties of the wall. Xyloglucan endotransglucosylase/hydrolases (XTH) cut xyloglucan chains and join one end of the cut to another chain, which can integrate newly synthesized xyloglucan into the wall and may keep the wall intact during expansion; pectin methylesterases change the degree of methyl esterification of pectin and thereby affect $\ce{Ca^2+}$ cross-linking and wall stiffness; wall peroxidases cross-link phenolics and extensins, stiffening the wall and stopping growth.

### 17.4.3. Hormones and Elongation: Concentration and Organ

The effects of different hormones on elongation are as follows (mechanisms in the three hormone chapters).

| Hormone | Effect on stem (internode, hypocotyl) elongation | Mode of action |
|---|---|---|
| **Auxin** | Promotes (most obvious in isolated segments) | Fast: wall acidification (acid growth); slow: gene expression, synthesis of wall material |
| **Gibberellin** | Strongly promotes (whole plant, especially dwarf mutants) | Does not acidify the wall, longer lag; raises wall extensibility (related to XTH and others) and promotes cell division; degrades DELLA proteins |
| **Brassinosteroid** | Promotes | Acts synergistically with gibberellin; induces genes for wall-loosening enzymes |
| **Ethylene** | Inhibits elongation, promotes lateral expansion | Changes orientation of cortical microtubules and microfibrils |
| **Abscisic acid**, **jasmonic acid** | Inhibit | Inhibit wall loosening and cell expansion |

The action of auxin depends strongly on concentration and organ. In stem or coleoptile segments depleted of endogenous auxin, elongation increases with the logarithm of the IAA concentration between about $10^{-8}$ and $10^{-5}\,\mathrm{mol\,L^{-1}}$, the effect weakens above about $10^{-5}\,\mathrm{mol\,L^{-1}}$, and above about $10^{-4}\,\mathrm{mol\,L^{-1}}$ it turns into inhibition. In intact roots growth is promoted at $10^{-10}$–$10^{-9}\,\mathrm{mol\,L^{-1}}$ and clearly inhibited already at $10^{-6}\,\mathrm{mol\,L^{-1}}$ (Taiz et al., measured with ethylene synthesis blocked; high concentrations of auxin induce ethylene, which is also one cause of the inhibition). Spraying auxin on intact, normal plants promotes stem elongation only briefly and weakly, because endogenous auxin is already near the optimal concentration. The dose–response curve is discussed fully in [7.13.13](/7.13.13).

## 17.5. Growth Measurement and Growth Analysis

### 17.5.1. Absolute and Relative Growth Rates

Growth can be measured by length, area, volume, fresh weight, dry weight or cell number, but only dry weight directly reflects the accumulation of matter. Let $W$ be dry weight; the absolute growth rate is $\mathrm{d}W/\mathrm{d}t$, which increases as the plant gets larger and is inconvenient for comparing plants of different sizes.

**Definition 17.5.1 (Relative Growth Rate)** The increase per unit dry weight per unit time,

$$
\mathrm{RGR} = \frac{1}{W}\frac{\mathrm{d}W}{\mathrm{d}t} = \frac{\mathrm{d}\ln W}{\mathrm{d}t}
\tag{17.7}
$$
is called the **relative growth rate**, in $\mathrm{d^{-1}}$ or $\mathrm{g\,g^{-1}\,d^{-1}}$.

The mean relative growth rate between two harvests (dry weights $W_1$ and $W_2$ at times $t_1$ and $t_2$) is $\overline{\mathrm{RGR}} = (\ln W_2 - \ln W_1)/(t_2 - t_1)$. When RGR is constant the plant grows exponentially, $\ln W$ is a straight line against time, and RGR is the same quantity as the specific growth rate in exponential growth of microorganisms ([7.11.8](/7.11.8)). Under optimal conditions the RGR of herbaceous seedlings is about $0.1$–$0.4\,\mathrm{d^{-1}}$; fast-growing weeds and crops lie at the upper end, and slow-growing perennials and woody plants at the lower end (Poorter and Remkes 1990). RGR declines as the plant gets larger, because the proportion of supporting organs and roots rises and leaves shade each other.

### 17.5.2. Decomposition of RGR

Classical growth analysis (pioneered by Blackman, Gregory and others in the early twentieth century) decomposes RGR into a physiological and a morphological factor. Let $A$ be the leaf area:

$$
\mathrm{RGR} = \frac{1}{W}\frac{\mathrm{d}W}{\mathrm{d}t} = \underbrace{\frac{1}{A}\frac{\mathrm{d}W}{\mathrm{d}t}}_{\mathrm{NAR}} \times \underbrace{\frac{A}{W}}_{\mathrm{LAR}}, \qquad \mathrm{LAR} = \underbrace{\frac{A}{W_{\mathrm{L}}}}_{\mathrm{SLA}} \times \underbrace{\frac{W_{\mathrm{L}}}{W}}_{\mathrm{LMF}}.
\tag{17.8}
$$

- The *net assimilation rate*, abbreviated NAR ($\mathrm{g\,m^{-2}\,d^{-1}}$), is the net increase in dry matter per unit leaf area per unit time; it integrates leaf photosynthesis minus whole-plant respiration, and is also called the unit leaf rate.
- The *leaf area ratio*, abbreviated LAR ($\mathrm{m^2\,kg^{-1}}$), is the leaf area per unit plant dry weight; it equals the product of specific leaf area (SLA, area per unit leaf dry weight, larger for thinner leaves) and leaf mass fraction (LMF, the fraction of total dry weight that is leaf).

Differences in RGR among species arise mainly from LAR (especially SLA) rather than NAR: fast-growing plants have thin leaves and a large leaf area per unit dry weight (Poorter and Remkes 1990). Under weak light plants increase SLA and LAR to compensate for the decline in NAR. At the stand level, the rate of dry matter accumulation per unit ground area (crop growth rate, CGR) equals $\mathrm{NAR} \times \mathrm{LAI}$; for the meaning of the **leaf area index** see [7.13.9](/7.13.9).

**Example 17.5.1 (Growth Analysis)** A batch of soybean seedlings had a mean dry weight of $0.80\,\mathrm{g}$ and a leaf area of $160\,\mathrm{cm^2}$ on day 14, and a dry weight of $2.10\,\mathrm{g}$ and a leaf area of $370\,\mathrm{cm^2}$ on day 21.

$\overline{\mathrm{RGR}} = \ln(2.10/0.80)/7 = 0.965/7 = 0.138\,\mathrm{d^{-1}}$. Assuming that leaf area and dry weight are approximately linearly related between the two harvests, the mean NAR can be calculated as $\overline{\mathrm{NAR}} = \frac{W_2 - W_1}{t_2 - t_1}\cdot\frac{\ln A_2 - \ln A_1}{A_2 - A_1}$: $= (1.30/7) \times (\ln 2.3125)/(0.0210\,\mathrm{m^2}) = 0.1857 \times 0.8383/0.0210 = 7.4\,\mathrm{g\,m^{-2}\,d^{-1}}$. The mean LAR $\approx \overline{\mathrm{RGR}}/\overline{\mathrm{NAR}} = 0.138/7.4 = 0.0186\,\mathrm{m^2\,g^{-1}} = 18.6\,\mathrm{m^2\,kg^{-1}}$, consistent with the LAR at the two harvests ($0.0200$ and $0.0176\,\mathrm{m^2\,g^{-1}}$).

![Growth analysis (simulated plant, illustrative parameters). A: The logarithm of dry weight W against time: the slope of the curve is the relative growth rate, and red dots mark the mean RGR over two intervals (Eq. (17.7)); RGR declines as the plant gets larger. B: Decomposition of RGR (black) into net assimilation rate NAR and leaf area ratio LAR (Eq. (17.8); the two are normalized by the values indicated and plotted on the right axis): in this example the decline in RGR comes mainly from the decline in LAR (the plant invests more dry matter in stem and roots), while NAR declines slowly because leaves shade each other](./plots/growth-analysis.py)

## 17.6. The Grand Period of Growth

### 17.6.1. The S-Shaped Growth Curve

For a single cell, an organ, a whole plant or a population, the growth rate shows the pattern "slow–fast–slow".

**Definition 17.6.1 (Grand Period of Growth)** The growth rate of a plant organ or whole plant is slow at first, then gradually accelerates, and after reaching a maximum slows and finally stops; this whole course of growth is called the **grand period of growth**. Cumulative growth plotted against time gives an S-shaped growth curve.

A typical plant growth curve can be divided into four phases.

1. Lag phase: cells are dividing and accumulating protoplasm, and volume increases slowly.
2. Logarithmic phase: the amount of growth is proportional to the amount already grown, approximately exponential increase (the relative growth rate is approximately constant).
3. Linear phase: growth proceeds at an approximately constant, maximal rate.
4. Decay phase: with cell maturation, senescence and resource limitation, the growth rate falls to zero.

The causes of the grand period of growth differ at different scales. Organ growth shifts from being dominated by cell division to being dominated by cell expansion and then to cell maturation; whole-plant growth is limited by the growth of photosynthetic area, shading, source–sink relations and developmental stage (vegetative growth slows after flowering); populations are also limited by resources and density.

Growth is irreversible, so measures that promote or control growth in production must be taken before the growth rate reaches its maximum. For example, retardants such as chlormequat that control internode elongation in wheat and rice to prevent lodging must be applied before jointing, and fertilizing and irrigating the new shoots of fruit trees must be done before the period of vigorous shoot growth. The grand periods of different organs of the same plant are timed differently, which is the basis for scheduling field management.

### 17.6.2. Logistic and Gompertz Curves

The most commonly used S-shaped curve is the **logistic growth** curve and its variants:

$$
W(t) = \frac{K}{1 + \mathrm{e}^{-r(t - t_{\mathrm{m}})}}, \qquad \frac{\mathrm{d}W}{\mathrm{d}t} = rW\left(1 - \frac{W}{K}\right),
\tag{17.9}
$$

where $K$ is the final amount of growth, $r$ is the initial relative growth rate and $t_{\mathrm{m}}$ is the inflection point. The growth rate is maximal at $W = K/2$, equal to $rK/4$, and the rate curve is symmetric about the inflection point. Real plant growth curves are often asymmetric, with faster acceleration before the inflection and slower deceleration after it. The Gompertz curve describes this asymmetry:

$$
W(t) = K\exp\!\left[-\mathrm{e}^{-r(t - t_{\mathrm{i}})}\right], \qquad \frac{\mathrm{d}W}{\mathrm{d}t} = rW\ln\frac{K}{W},
\tag{17.10}
$$

The inflection is at $W = K/\mathrm{e} \approx 0.37K$ and the maximal rate is $rK/\mathrm{e}$; its relative growth rate $r\ln(K/W)$ declines linearly with the logarithm of the amount of growth, whereas the relative growth rate of the logistic, $r(1 - W/K)$, declines linearly with the amount of growth itself. The more general Richards curve $W = K[1 + v\,\mathrm{e}^{-r(t - t_{\mathrm{m}})}]^{-1/v}$ has a shape parameter $v$, with $v = 1$ giving the logistic and $v \to 0$ the Gompertz. These curves are fitted by nonlinear least squares and belong to the same family as the four-parameter logistic model in dose–response analysis ([7.7.11](/7.7.11)).

**Example 17.6.1** Maize plant height grows along a logistic curve with $K = 165\,\mathrm{cm}$, $r = 0.11\,\mathrm{d^{-1}}$ and $t_{\mathrm{m}} = 49\,\mathrm{d}$. The maximal growth rate $rK/4 = 4.5\,\mathrm{cm\,d^{-1}}$ occurs on day 49 after sowing, when the plant height is $82.5\,\mathrm{cm}$. The period in which the growth rate is at least half the maximum is given by $W(1 - W/K) \ge K/8$, that is, $W/K \in [0.146, 0.854]$, corresponding to $t_{\mathrm{m}} \pm \ln(5.83)/r = 49 \pm 16\,\mathrm{d}$, or days 33–65. This is the period of rapid height growth, and measures to control internode length should be applied before day 33.

![The grand period of growth (simulated maize plant height data, schematic). A: S-shaped cumulative curve of plant height against time, with logistic (Eq. (17.9), red) and Gompertz (Eq. (17.10), blue, dashed) curves fitted by nonlinear least squares; the legend gives the fitted final plant height K and rate parameter r. B: Growth rate (successive differences of the data and the derivatives of the two fitted curves) shows a single "slow–fast–slow" peak; diamonds mark the maximal rates of the two models: the logistic at K/2, symmetric about the peak, and the Gompertz at K/e, rising quickly before the peak and falling slowly after it](./plots/grand-period.py)

## 17.7. Environmental Effects on Growth

### 17.7.1. Temperature: Cardinal Points, Thermoperiodism and Thermal Time

The response of growth to temperature has three cardinal points: minimum, optimum and maximum temperature. Growth stops outside the minimum and maximum temperatures and is fastest at the optimum. The cardinal temperatures vary with species, organ, developmental stage and origin. Cereals of temperate origin can grow slowly at temperatures near $0\,^\circ\mathrm{C}$, whereas the minimum temperature of tropical rice, maize and cotton is above $10\,^\circ\mathrm{C}$; the optimum for root growth is generally lower than for shoots. The temperature of fastest growth is not necessarily the most favorable for the plant: material is consumed quickly and plants are weak. In agriculture the temperature at which plants grow both fairly fast and robustly is called the coordinated optimum temperature, and it is slightly below the optimum for growth.

The unimodal response of growth rate to temperature is often described by a beta function of the three cardinal temperatures (Yan and Hunt 1999):

$$
r(T) = r_{\max}\left(\frac{T_{\max} - T}{T_{\max} - T_{\mathrm{opt}}}\right)\left(\frac{T - T_{\mathrm{b}}}{T_{\mathrm{opt}} - T_{\mathrm{b}}}\right)^{\frac{T_{\mathrm{opt}} - T_{\mathrm{b}}}{T_{\max} - T_{\mathrm{opt}}}}, \qquad T_{\mathrm{b}} < T < T_{\max},
\tag{17.11}
$$

Using only three biologically meaningful parameters (the base temperature $T_{\mathrm{b}}$, the optimum temperature $T_{\mathrm{opt}}$ and the maximum temperature $T_{\max}$), it describes an asymmetric bell-shaped curve from the minimum to the maximum temperature: above the optimum the rate declines faster than it rises below. Between the minimum and the optimum temperature the rate rises approximately linearly with temperature (panel A of the figure below), which is the basis of the concept of thermal time.

**Definition 17.7.1 (Thermal Time)** Between $T_{\mathrm{b}}$ and the optimum temperature, the rate of development is approximately proportional to $T - T_{\mathrm{b}}$, and the sum of temperature times duration needed to complete a developmental stage is approximately constant. The quantity computed from daily mean temperature,

$$
\mathrm{GDD} = \sum_{i} \max\left(0,\ \bar T_i - T_{\mathrm{b}}\right)
\tag{17.12}
$$
is called the (effective) **thermal time** (also growing degree days), in $^\circ\mathrm{C\,d}$; $T_{\mathrm{b}}$ is called the base temperature (biological zero).

Thermal time replaces "time" with "heat time": across years and sites, the thermal time that a given cultivar needs from sowing to emergence, flowering and maturity is much more stable than the number of calendar days, so thermal time is used to predict phenology and to determine suitable planting regions and sowing dates for cultivars. $T_{\mathrm{b}}$ is commonly taken as $10\,^\circ\mathrm{C}$ for warm-season crops such as maize and rice and as $0$–$5\,^\circ\mathrm{C}$ for wheat. Chinese agrometeorology commonly uses the active accumulated temperature above $10\,^\circ\mathrm{C}$ (the direct sum of daily mean temperatures on days with a mean of at least $10\,^\circ\mathrm{C}$) to delimit thermal zones; it differs from the effective thermal time of Eq. (17.12) and must be specified when cited. Thermal time is also used in population models of seed germination ([7.13.20](/7.13.20)).

**Example 17.7.1 (Thermal Time)** A maize cultivar requires an effective thermal time of $1400\,^\circ\mathrm{C\,d}$ ($T_{\mathrm{b}} = 10\,^\circ\mathrm{C}$) from sowing to physiological maturity. At a site where the mean daily temperature after sowing averages $22\,^\circ\mathrm{C}$ over the growing season, about $1400/(22 - 10) \approx 117\,\mathrm{d}$ is needed; if climate warming raises the mean temperature by $2\,^\circ\mathrm{C}$, $1400/14 = 100\,\mathrm{d}$ is needed, and the growth duration is shortened by about 17 days. A shorter growth duration means less time for grain filling, which is one reason climate warming reduces crop yields in many regions, unless later-maturing cultivars with a higher thermal time requirement are used.

![Temperature and development rate. A: Beta function of the three cardinal temperatures for development rate (Eq. (17.11), T_b = 10 °C, T_opt = 30 °C, T_max = 42 °C, illustrative parameters, red) and the linear approximation used in thermal time (dashed): the two are close between the base and the optimum temperature, and above the optimum the rate falls rapidly. B: Accumulation of effective thermal time (Eq. (17.12), T_b = 10 °C) in a simulated growing season; the dashed line is the 1400 °C d needed for maturity of a cultivar, and dots mark the dates when it is reached: with 2 °C warming throughout the season it is reached about 12 days earlier](./plots/thermal-time.py)

:::

Many plants grow better under a certain variation of day and night temperature than at constant temperature.

**Definition 17.7.2 (Thermoperiodism)** The response of plant growth and development to the periodic variation of day and night temperature is called **thermoperiodism**.

Went (1944) found that tomato grows and sets fruit best at a day temperature of $26\,^\circ\mathrm{C}$ and a night temperature of about $17$–$20\,^\circ\mathrm{C}$, better than at any constant day–night temperature. The usual explanation is that the lower night temperature reduces respiratory consumption and favors accumulation of assimilates and their transport to roots and fruits. In horticulture, day temperature minus night temperature is called DIF: the internode length of many plants (such as chrysanthemum, poinsettia and lily) increases with DIF, and negative DIF (night temperature higher than day temperature, or a brief temperature drop before dawn) shortens internodes and is used in greenhouses instead of chemical retardants to control plant height. The large diurnal temperature range in plateau and desert regions, where crops and melons are of better quality, is also related to thermoperiodism.

### 17.7.2. Light

Light is the energy source for photosynthesis, but its direct effect on elongation growth is inhibitory. Seedlings grown in darkness show **skotomorphogenesis** (etiolation): the hypocotyl or mesocotyl is long and thin, leaves are small and unexpanded, no chlorophyll forms and mechanical tissue is poorly developed; on exposure to light elongation slows rapidly, leaves expand and turn green, and the seedling enters **photomorphogenesis** ([7.13.16](/7.13.16)). This inhibition is mediated by photoreceptors such as **phytochrome** and **cryptochrome** rather than by photosynthesis, and blue and red light are the most inhibitory. Under insufficient light (such as the lower layers of dense stands), internodes are too long, stems are slender and mechanical tissue is poorly developed, so plants lodge easily, while leaf area increases compensatorily and leaves become thinner; a higher proportion of far-red light under shade also causes **shade avoidance**.

Chinese textbooks often say that "blue-violet and ultraviolet light lower growth-promoting substances and raise inhibitors in plants, so alpine plants are dwarfed". We now know that light regulates hormone synthesis and sensitivity through photoreceptors (for example, light lowers the sensitivity of the hypocotyl to gibberellin; see seedling establishment in [7.13.20](/7.13.20)), and that the action of UV-B is mediated by the UVR8 receptor. The dwarf stature of alpine plants results from the combined effects of low temperature, strong wind, short growing season, strong radiation and poor soil, and is to a large extent a genetically determined adaptation rather than just a direct effect of ultraviolet light.

### 17.7.3. Water

Cell expansion is the physiological process most sensitive to water deficit. By Eq. (17.4), when the source water potential $\Psi_{\mathrm{o}}$ falls, $\Delta\pi$ decreases and turgor and growth rate decline with it; when $\Delta\pi$ falls to the yield threshold $Y$, growth stops. Leaf expansion slows noticeably when water potential has fallen by only a few tenths of a megapascal and photosynthesis is not yet affected (Hsiao 1973), so mild drought first reduces leaf area. Water-stressed plants have small, thick leaves, and root growth slows and the roots suberize early, lowering the capacity for water uptake.

Different organs respond differently to water deficit: in maize seedlings at a water potential of about $-1.6\,\mathrm{MPa}$, shoot growth almost completely stops, whereas the primary root still elongates at a considerable rate (Sharp et al. 1988). The root tip maintains turgor by **osmotic adjustment** (accumulation of solutes such as proline, sugars and $\ce{K+}$, [7.13.27](/7.13.27)) and also increases wall extensibility and lowers the yield threshold, which depends on **abscisic acid**; under water deficit, shoot growth is inhibited while the root continues to grow, which raises the root–shoot ratio (Section 17.8) and favors uptake of water from deeper layers. Waterlogging makes roots hypoxic: roots become shorter, lateral roots increase, cell division is inhibited, and reduced substances accumulating in the soil also injure the roots.

### 17.7.4. Mineral Nutrition

Nitrogen has the largest effect on vegetative growth. With ample nitrogen, leaf emergence is earlier, leaves are larger, leaf life span is relatively prolonged and stems grow faster; with excess nitrogen leaves are large and thin, plants grow rank and remain green too long, stems are weak and lodge easily, maturity is delayed and leaf life span is in fact shortened. Ample phosphorus and potassium favor the development of the root system and of mechanical tissue. For the physiological roles of the elements see [7.13.4](/7.13.4), and for the effect of nutrients on root system architecture see [7.13.18](/7.13.18).

## 17.8. Root–Shoot Ratio and Allometry

### 17.8.1. The Root–Shoot Ratio

**Definition 17.8.1 (Root–Shoot Ratio)** The ratio of the dry weight (or fresh weight) of the underground part of a plant to that of the aboveground part, $R/S = W_{\mathrm{root}}/W_{\mathrm{shoot}}$, is called the **root–shoot ratio**.

Roots and shoots are both interdependent and mutually constraining. The water and mineral elements needed for shoot growth are supplied by the root system, and roots also synthesize **cytokinins**, some amino acids and alkaloids (for example nicotine in tobacco is synthesized in the roots) and transport them to the shoot through the xylem; the sugars and vitamin $\mathrm{B_1}$ and others needed for root growth come from the leaves. In drought, abscisic acid synthesized in the roots is carried through the xylem to the leaves and closes the stomata ([7.13.10](/7.13.10)), which is a chemical signal from root to shoot.

The root–shoot ratio varies with the environment, and the farmers' saying "drought grows roots, water grows shoots" summarizes the influence of water.

| Condition | Root–shoot ratio | Reason |
|---|---|---|
| Soil drought | Increases | Roots get water first, and shoot expansion is inhibited first |
| Excess soil water | Decreases | Poor aeration inhibits roots, and the shoot has ample water |
| Nitrogen or phosphorus deficiency | Increases | Assimilates are allocated preferentially to roots |
| Ample nitrogen | Decreases | The shoot grows vigorously and consumes most assimilates |
| Weak light | Decreases | Little photosynthate, supplied preferentially to the shoot |
| Pruning the shoot | Temporarily increases, then recovers | The shoot regenerates, and roots temporarily stop growing |

In production, water and fertilizer are used to regulate the root–shoot ratio. For crops harvested for their underground parts, such as sweet potato, sugar beet, radish and potato, the root–shoot ratio must be raised in the later growth stage by appropriately limiting nitrogen and water and applying more phosphorus and potassium; in vegetable nurseries, seedling hardening (called "squatting seedlings" in Chinese practice) means moderate water restriction at the seedling stage to promote downward rooting.

### 17.8.2. Functional Balance

The environmental response of the root–shoot ratio can be understood in terms of "functional balance" (Brouwer 1963; Davidson 1969): the plant adjusts allocation so that the total rate of resource uptake by roots stays in a fixed proportion to the total rate of carbon fixation by shoots,

$$
W_{\mathrm{root}} \cdot a_{\mathrm{root}} \propto W_{\mathrm{shoot}} \cdot a_{\mathrm{shoot}}, \qquad \frac{W_{\mathrm{root}}}{W_{\mathrm{shoot}}} \propto \frac{a_{\mathrm{shoot}}}{a_{\mathrm{root}}},
\tag{17.13}
$$

where $a_{\mathrm{root}}$ is the rate of water or nitrogen uptake per unit root weight and $a_{\mathrm{shoot}}$ is the photosynthetic rate per unit shoot weight. Whichever resource is relatively scarce, the plant allocates more biomass to the organ that acquires it: water or nitrogen deficiency lowers $a_{\mathrm{root}}$ and raises the root–shoot ratio, and weak light lowers $a_{\mathrm{shoot}}$ and lowers the root–shoot ratio. This agrees completely with the empirical rules in the table above.

**Example 17.8.1** A plant is in functional balance with a root–shoot ratio of 0.30. Halving the soil nitrogen supply reduces the nitrogen uptake rate per unit root weight to 0.6 times the original, with the photosynthetic rate unchanged. By Eq. (17.13), the new equilibrium root–shoot ratio is $0.30/0.6 = 0.50$. If total plant dry weight stays constant ($W = 10\,\mathrm{g}$), root weight increases from $10 \times 0.3/1.3 = 2.3\,\mathrm{g}$ to $10 \times 0.5/1.5 = 3.3\,\mathrm{g}$.

### 17.8.3. Allometry

Different organs of a plant grow at different rates, and the proportions among organs change with plant size. The sizes of two organs often obey the **allometry** equation $y = ax^b$ ([7.5.34](/7.5.34)), a straight line $\ln y = \ln a + b\ln x$ on log–log axes; if the ratio of their relative growth rates is constant, then $b = \mathrm{RGR}_y/\mathrm{RGR}_x$. For root and shoot, $b$ in many species is close to but slightly below 1 during ontogeny, that is, the root–shoot ratio declines slowly as the plant gets larger; in large samples spanning seed plants, the allometric exponent of root mass against shoot mass is close to 1 (Enquist and Niklas 2002). Plant size must be taken into account when comparing root–shoot ratios among treatments: among plants harvested at the same time, if one treatment merely makes plants grow more slowly, their root–shoot ratio will also differ because of size. This "apparent plasticity" must be separated out with the allometry equation; only a comparison at the same plant size can show whether allocation itself has changed.

## Summary

| Level | Content | Key points |
|---|---|---|
| Concepts | Growth, differentiation, development (Definition 17.1.1) | Irreversible quantitative change, qualitative change and the orderly whole process; division, elongation and differentiation phases |
| Wall structure | Cellulose 20 %–30 %, hemicellulose 20 %–25 %, pectin 10 %–35 %, protein 5 %–10 % | The biomechanical hotspot model replaces the tethered network model |
| Direction | Microfibril orientation ← cortical microtubules | Transverse microfibrils → elongation; random → isodiametric; longitudinal (ethylene) → lateral expansion |
| Mode | Diffuse growth and tip growth | Root hairs and pollen tubes show tip growth |
| Rate | Lockhart equation (Definition 17.3.1) | Extensibility $\phi$, yield threshold $Y$; coupled to water uptake; stress relaxation |
| Relaxation | Acid growth hypothesis (Definition 17.4.1), expansin (Definition 17.4.2) | Proton pump, pH 4.5–5, lag of 10–15 min; expansins nonenzymatic, catalytic amounts |
| Hormones | Auxin, gibberellin, brassinosteroid promote; ethylene, abscisic acid, jasmonic acid inhibit | Auxin promotes at $10^{-8}$–$10^{-5}$ in stems and $10^{-10}$–$10^{-9}\,\mathrm{mol\,L^{-1}}$ in roots |
| Measurement | RGR (Definition 17.5.1) = NAR × LAR | Species differences come mainly from LAR (SLA) |
| Time | Grand period of growth (Definition 17.6.1) | Slow–fast–slow; logistic and Gompertz |
| Temperature | Cardinal points, coordinated optimum, thermoperiodism (Definition 17.7.2), thermal time (Definition 17.7.1) | Thermal time predicts phenology |
| Light, water, nitrogen | Light inhibits elongation; expansion is most sensitive to water deficit; nitrogen promotes the shoot | In drought roots tolerate more than shoots |
| Proportions | Root–shoot ratio (Definition 17.8.1), functional balance, allometry | Drought grows roots, water grows shoots; the plant grows the organ that acquires what is scarce |

Main equations:

| Equation | Content |
|---|---|
| Eq. (17.1) $\sigma_\theta = Pr/\delta = 2\sigma_z$ | Wall stress of a cylindrical cell, 10–100 MPa |
| Eq. (17.2) $\frac{1}{V}\frac{\mathrm{d}V}{\mathrm{d}t} = \phi(P - Y)$ | Lockhart equation; $Y$ about 0.1–0.5 MPa |
| Eqs. (17.3), (17.4) $P^* = \frac{L\Delta\pi + \phi Y}{L + \phi}$ | Coupling of wall yielding and water uptake, steady-state turgor and growth rate |
| Eqs. (17.5), (17.6) $\tau = 1/(\varepsilon\phi)$ | Expansion equation with elastic term; in vivo stress relaxation |
| Eq. (17.7) $\mathrm{RGR} = \mathrm{d}\ln W/\mathrm{d}t$ | Relative growth rate, 0.1–0.4 d⁻¹ in seedlings |
| Eq. (17.8) $\mathrm{RGR} = \mathrm{NAR} \times \mathrm{LAR}$, $\mathrm{LAR} = \mathrm{SLA} \times \mathrm{LMF}$ | Growth analysis |
| Eqs. (17.9), (17.10) | Logistic (inflection $K/2$, maximal rate $rK/4$) and Gompertz (inflection $K/\mathrm{e}$) |
| Eq. (17.11) | Beta function of the cardinal temperatures |
| Eq. (17.12) $\mathrm{GDD} = \sum\max(0, \bar T - T_{\mathrm{b}})$ | Effective thermal time |
| Eq. (17.13) $W_{\mathrm{r}}/W_{\mathrm{s}} \propto a_{\mathrm{s}}/a_{\mathrm{r}}$ | Functional balance |

## Questions

1. Why is the observation that "turgor falls rather than rises" when auxin causes segment elongation evidence that wall loosening drives growth? Explain with the Lockhart equation, and state how turgor should change if auxin promoted growth by increasing solute uptake (osmotic adjustment).

   **Answer** At steady state $P^* = (L\Delta\pi + \phi Y)/(L + \phi)$ (Eq. (17.4)). When auxin raises $\phi$ and lowers $Y$, the term $\phi Y$ in the numerator changes little while the denominator increases, so $P^*$ falls toward $Y$, yet the growth rate $\phi L(\Delta\pi - Y)/(\phi + L)$ rises (Example 17.3.1: turgor falls from 0.633 to 0.557 MPa while the growth rate increases to 2.1 times). If auxin merely promoted solute uptake, $\Psi_{\mathrm{s}}$ would fall and $\Delta\pi$ would increase, so both $P^*$ and the growth rate would rise while $\phi$ and $Y$ stayed unchanged. In measurements, segments treated with auxin grow faster while turgor decreases slightly or is unchanged, and acid-induced creep is also seen in isolated walls without turgor or metabolism, which shows that the main change occurs in the yielding properties of the wall.

2. A cylindrical internode cell has a diameter of $30\,\mu\mathrm{m}$, a primary wall thickness of $0.2\,\mu\mathrm{m}$ and a turgor pressure of $0.6\,\mathrm{MPa}$. (a) Find the circumferential and axial wall stresses. (b) If all the microfibrils in the wall are oriented circumferentially, why does the cell elongate axially even though the circumferential stress is larger?

   **Answer** (a) $r = 15\,\mu\mathrm{m}$, $\sigma_\theta = Pr/\delta = 0.6 \times 15/0.2 = 45\,\mathrm{MPa}$, $\sigma_z = 22.5\,\mathrm{MPa}$. (b) The wall is extremely stiff and strong along the microfibrils (the elastic modulus of cellulose is of the order of 100 GPa) and hardly extends at 45 MPa; perpendicular to the microfibrils it is held together only by linkages between the matrix and microfibrils that can be loosened, and the yield stress is much lower. So although the axial stress is only half the circumferential stress, the wall still yields axially (perpendicular to the microfibrils). The transverse microfibrils reinforce exactly the direction of the largest stress, so that the cell does not expand radially.

3. A pressure probe measured the turgor of an excised pea stem segment placed at saturating humidity: $0.62\,\mathrm{MPa}$ at 0 min, $0.45\,\mathrm{MPa}$ at 20 min, $0.36\,\mathrm{MPa}$ at 40 min, and stable at $0.25\,\mathrm{MPa}$ after a long time. Given $\varepsilon = 8\,\mathrm{MPa}$, find the yield threshold and wall extensibility, and estimate the relative growth rate before excision.

   **Answer** By Eq. (17.6), $Y = 0.25\,\mathrm{MPa}$. $P - Y$ is 0.37 MPa at 0 min, 0.20 at 20 min and 0.11 at 40 min; $\ln(0.37/0.20) = 0.615$ and $\ln(0.20/0.11) = 0.598$; taking the mean of 0.607 per 20 min, $\tau = 20/0.607 = 33\,\mathrm{min} = 0.55\,\mathrm{h}$. $\phi = 1/(\varepsilon\tau) = 1/(8 \times 0.55) = 0.23\,\mathrm{h^{-1}\,MPa^{-1}}$. The relative growth rate before excision (at turgor 0.62 MPa) is $\approx \phi(P_0 - Y) = 0.23 \times 0.37 = 0.084\,\mathrm{h^{-1}}$, about 8 % per hour (assuming the stem was at steady state before excision and that turgor had not changed at the moment of excision).

4. Two herbaceous plants grow under the same conditions; plant A has an RGR of $0.25\,\mathrm{d^{-1}}$ and plant B of $0.12\,\mathrm{d^{-1}}$; their NARs are $10$ and $9\,\mathrm{g\,m^{-2}\,d^{-1}}$ and their leaf mass fractions are 0.50 and 0.45, respectively. (a) Find the LAR and specific leaf area of each. (b) Explain in what respect the fast-growing plant is "fast", and discuss the cost of this strategy in infertile, dry habitats.

   **Answer** (a) $\mathrm{LAR} = \mathrm{RGR}/\mathrm{NAR}$: A $0.025\,\mathrm{m^2\,g^{-1}} = 25\,\mathrm{m^2\,kg^{-1}}$, B $13.3\,\mathrm{m^2\,kg^{-1}}$; $\mathrm{SLA} = \mathrm{LAR}/\mathrm{LMF}$: A $50\,\mathrm{m^2\,kg^{-1}}$, B $29.6\,\mathrm{m^2\,kg^{-1}}$. (b) The two have similar assimilation capacity per unit leaf area; A is fast because it has more leaf area per unit dry weight, mainly because its leaves are thin (high SLA). Thin leaves have a low construction cost and a quick photosynthetic return, but a short life span, and are easily damaged mechanically and by herbivores, and the nutrients invested per unit leaf area must be constantly renewed. In infertile or dry habitats, nutrient and water acquisition limits this high-turnover strategy, and the thick, long-lived leaves (low SLA) of slow-growing plants favor nutrient conservation, drought tolerance and resistance to herbivory; this is one end of the "leaf economics spectrum".

5. (Open question) Using the Lockhart equation, thermal time and functional balance models of this chapter, analyze why moderate water restriction (seedling hardening, "squatting seedlings") produces seedlings with a well-developed root system and short, sturdy shoots, and propose a test.

   **Answer** Key points: water restriction lowers soil water potential and xylem water potential $\Psi_{\mathrm{o}}$; by Eq. (17.4) the expansion rate of the shoot (especially leaves and internodes, which have weak osmotic adjustment and a yield threshold that does not fall) first declines; the root tip maintains elongation through osmotic adjustment and ABA-dependent wall loosening (Section 17.7.3); at the same time slower shoot expansion lowers the demand for assimilates, and more sugar is transported to the roots; by functional balance (Eq. (17.13)), the relative scarcity of water raises the root–shoot ratio. The result is a deep, well-developed root system, short internodes and sturdy stems. Test: set up two treatments, full irrigation and mild water restriction (for example soil water content at 75 % and 55 % of field capacity), harvest periodically to determine the dry weights of root, stem and leaf and the leaf area, and calculate RGR, NAR, LAR and the root–shoot ratio, comparing root–shoot ratios at the same plant size with the allometry equation; at the same time measure turgor and solute potential of leaves and root tips and estimate $Y$ and $\phi$ by stress relaxation of excised segments (Eq. (17.6)); after rewatering follow the recovery of shoot growth and the final yield.
