---
title: "Plant Hormones I: Overview and Auxin"
description: Plant growth substances, plant hormones and plant growth regulators; the nine hormone classes and their shared logic (homeostasis, derepression, dose-response); the discovery of auxin (Darwin, Boysen-Jensen, Paál, Went and the Avena curvature test), its types and antagonists; the TAA-YUC pathway, conjugation and degradation; the chemiosmotic model of polar transport (AUX1/LAX, PIN, ABCB) and its quantitative advection-diffusion description; physiological effects on cell elongation, vascular differentiation, lateral and adventitious roots, flowers and fruit, and parthenocarpy; dose-response and organ sensitivity; synthetic auxins and herbicides.
source_hash: 179c42d8cfee
---

Plants have no nervous system and no glands dedicated to secreting hormones, yet a leaf far from the root tip "knows" that the soil is drying, a shoot apex decides when the axillary buds below it may grow, and a coleoptile illuminated from one side bends toward the light within tens of minutes. This coordination is carried mainly by a group of small molecules present at very low concentrations: the plant hormones. This chapter first presents the general concept of a plant hormone and the logic shared by all of them: how the concentration is set jointly by synthesis, transport, conjugation and degradation, how cells turn concentration into a response through receptors, and why the same hormone can have opposite effects at different concentrations or in different organs (Section 13.1). It then turns to auxin, the first hormone to be discovered and the one studied most deeply: the classic experiments of its discovery (Section 13.2), its biosynthesis and metabolism (Section 13.3), its polar transport, the only directional cell-to-cell transport known for a plant hormone (Section 13.4), its physiological effects and dose-response relations (Section 13.5), and the agricultural use of synthetic auxins and their action as herbicides (Section 13.6).

The molecular mechanisms of hormone receptors and signal transduction (the TIR1/AFB-Aux/IAA co-receptor, DELLA, two-component systems, and so on) were treated in the biochemistry course ([7.1.15](/7.1.15#sec-15.5.2)) and are mentioned here only when needed; the emphasis is on physiological effects, biosynthesis and transport, and quantitative relations such as dose-response. Gibberellins and cytokinins are covered in [7.13.14](/7.13.14); abscisic acid, ethylene, the other hormones and hormone interactions in [7.13.15](/7.13.15). Many developmental processes that involve auxin are developed in later chapters: the acid-growth mechanism of cell elongation ([7.13.17](/7.13.17)), organogenesis and **apical dominance** ([7.13.18](/7.13.18)), phototropism and gravitropism ([7.13.19](/7.13.19)), and abscission ([7.13.24](/7.13.24)).

## 13.1. Plant Growth Substances and Plant Hormones

### 13.1.1. Concepts

**Definition 13.1.1 (Plant Growth Substance)** Small organic compounds that, at very low concentrations, markedly affect plant growth, development and physiological processes are called **plant growth substances**. They include the naturally occurring plant hormones and the synthetic plant growth regulators.

**Definition 13.1.2 (Plant Hormone)** Naturally occurring small molecules that are synthesized in the plant and regulate growth, development and responses to the environment at very low concentrations (typically $10^{-9}$–$10^{-6}\ \mathrm{mol\,L^{-1}}$), either at the site of synthesis or at a site of action reached by transport, are called **plant hormones**.

**Definition 13.1.3 (Plant Growth Regulator)** Synthetic compounds whose physiological activity resembles or opposes that of plant hormones are called **plant growth regulators**.

The word "hormone" was borrowed from animal physiology (for the general definition of a **hormone** see [7.1.29](/7.1.29#def-29.1.1)), but the differences between the two cases are worth remembering:

| | Animal hormones | Plant hormones |
|---|---|---|
| Site of production | Dedicated endocrine glands | No dedicated organs; many tissues synthesize them, mainly meristems, young leaves and developing seeds |
| Distance of action | Mostly long-range, through the circulation (endocrine) | Mostly near the site of synthesis (autocrine, paracrine), but also long-range through the xylem, phloem or directed cell-to-cell transport |
| Effects | One hormone usually has a few target organs | One hormone affects many processes; effects depend strongly on concentration, tissue and developmental stage |
| Control of concentration | Mainly secretion rate and clearance | Synthesis, transport, reversible conjugation, irreversible degradation and compartmentation jointly set the local concentration |

These differences arise from the modular construction of plants (**meristems** divide throughout life and organs are produced repeatedly): what a plant needs is not a central organ but signals that integrate environmental cues and developmental state locally, at every site.

### 13.1.2. The Nine Hormone Classes

Five classes are classical plant hormones: auxin, gibberellin, cytokinin, abscisic acid and ethylene, all established before 1960. Brassinosteroids, jasmonates, salicylic acid and strigolactones were confirmed later, and the nine are commonly grouped together as the plant hormones. There are also peptide signals (such as systemin, CLAVATA3 and other CLE peptides, and phytosulfokine), as well as polyamines, nitric oxide and other substances with hormone-like action; the list is still growing, and "the nine currently recognized" is only a conventional grouping.

| Hormone | Chemical nature | Precursor | Main sites of synthesis | Main mode of transport | Representative effects | Chapter |
|---|---|---|---|---|---|---|
| Auxin (IAA) | Indole derivative | Tryptophan | Shoot apex, young leaves, developing seeds and fruit | Polar transport (cell to cell); phloem | Cell elongation, vascular differentiation, rooting, apical dominance, tropisms | This chapter |
| Gibberellin (GA) | Tetracyclic diterpenoid acid | Geranylgeranyl diphosphate (GGPP) | Young buds and leaves, elongating internodes, developing seeds | Xylem, phloem (mostly as precursors) | Stem elongation, germination, bolting and flowering, fruit growth | [7.13.14](/7.13.14) |
| Cytokinin (CTK) | Adenine derivative | AMP + dimethylallyl diphosphate | Mainly root tips; also shoot apex and seeds | Xylem (root to shoot), phloem | Cell division, shoot differentiation, delay of senescence | [7.13.14](/7.13.14) |
| Abscisic acid (ABA) | Sesquiterpenoid | Carotenoids (C40) | Almost all plastid-containing cells | Xylem, phloem | Stomatal closure, seed maturation and dormancy, stress responses | [7.13.15](/7.13.15) |
| Ethylene | Gas $\ce{C2H4}$ | Methionine | Almost all tissues; especially ripening, senescing and wounded sites | Diffusion through intercellular spaces; precursor ACC through the xylem | Fruit ripening, senescence and abscission, triple response | [7.13.15](/7.13.15) |
| Brassinosteroid (BR) | Sterol | Campesterol | All organs; abundant in pollen and immature seeds | Essentially no long-distance transport | Cell elongation and division, xylem differentiation, skotomorphogenesis | [7.13.15](/7.13.15) |
| Jasmonate (JA) | Oxidized lipid | $\alpha$-Linolenic acid | Chloroplast and peroxisome | Phloem; volatile methyl ester | Defense against insects and necrotrophs, wound response, anther dehiscence | [7.13.15](/7.13.15) |
| Salicylic acid (SA) | Phenolic acid | Chorismate | Plastid (isochorismate pathway) | Phloem | Defense against biotrophs, systemic acquired resistance, thermogenesis | [7.13.15](/7.13.15) |
| Strigolactone (SL) | Terpenoid lactone | $\beta$-Carotene | Mainly roots | Xylem (root to shoot); exuded into the rhizosphere | Inhibition of branching, promotion of arbuscular mycorrhizal symbiosis, germination of parasitic plant seeds | [7.13.15](/7.13.15) |

### 13.1.3. The Shared Logic of Hormone Action

The first common feature is that concentration is set by homeostasis. The effective concentration $c$ of a hormone in a tissue is a balance of inputs and outputs:

$$
\frac{\mathrm{d}c}{\mathrm{d}t} = \underbrace{s + J_{\mathrm{in}} + r}_{\text{synthesis, import, release from conjugates}} - \underbrace{(k_{\mathrm{deg}} + k_{\mathrm{conj}})\,c - J_{\mathrm{out}}}_{\text{degradation, conjugation, export}}
\tag{13.1}
$$

At steady state $c^* = (s + J_{\mathrm{in}} + r - J_{\mathrm{out}})/(k_{\mathrm{deg}} + k_{\mathrm{conj}})$. Equation (13.1) explains several general phenomena. The concentration of a hormone can change by tens of times within hours (for example ABA in a leaf under drought, which requires only an increase in $s$ or a decrease in $k_{\mathrm{deg}}$). An exogenously applied hormone is often quickly "absorbed" because the plant up-regulates conjugation and degradation and so returns $c$ to its steady state; synthetic auxins are effective herbicides precisely because they are poorly conjugated and degraded (Section 13.6). And many hormones feed back negatively on their own synthesis (gibberellin represses its own biosynthetic genes and induces inactivating enzymes, [7.13.14](/7.13.14)), which stabilizes the steady state further.

The second common feature is that receptors turn concentration into response. Plant hormone receptors occupy different cellular locations: those for ethylene and cytokinin are in the endoplasmic reticulum membrane, that for brassinosteroids is at the plasma membrane, and those for auxin, gibberellin, abscisic acid and jasmonate are soluble cytosolic or nuclear proteins. Several pathways share one molecular logic: the hormone does not directly "switch something on" but disables a repressor, that is, it acts by derepression. Auxin, gibberellin, jasmonate and strigolactone all cause transcriptional repressors to be degraded through the **ubiquitin–proteasome system** (SCF-type E3 ligases, the **SCF complex**); abscisic acid and brassinosteroids inactivate a negatively acting phosphatase or kinase; the ethylene and cytokinin receptors derive from bacterial **two-component systems**. These mechanisms are covered in [7.1.15](/7.1.15#sec-15.5.2). A derepression logic lets the plant keep a pathway "off" in the absence of the hormone and still respond sensitively to changes in its concentration.

The third common feature is the dose-response relation. Over a certain range the effect $E$ of a hormone increases with the logarithm of the concentration $c$ and can be described by the **Hill equation** (compare the dose-response curves and **half-maximal effective concentration** in [7.7.11](/7.7.11#sec-11.6)):

$$
E = E_0 + (E_{\max} - E_0)\,\frac{c^{\,n}}{\mathrm{EC}_{50}^{\,n} + c^{\,n}}
\tag{13.2}
$$

$\mathrm{EC}_{50}$ reflects the sensitivity of the tissue and the Hill coefficient $n$ the steepness of the response. An important fact of plant physiology is that the $\mathrm{EC}_{50}$ of one hormone can differ by several orders of magnitude between organs, and that above the optimum the effect declines or even turns into inhibition, so that the dose-response curve is bell-shaped (Section 13.5.2). A statement such as "hormone X promotes process Y" must therefore always be understood together with a concentration and a tissue; in many developmental processes what matters is often a change in the sensitivity of the tissue to the hormone (the abundance of receptors and signaling components), and not only a change in hormone concentration.

## 13.2. The Discovery and Kinds of Auxin

### 13.2.1. From Phototropism to the Avena Curvature Test

Auxin was the first plant hormone to be discovered, and its discovery came from a series of experiments on the bending of grass seedlings toward light.

| Year | Investigator | Experiment | Conclusion |
|---|---|---|---|
| 1880 | C. Darwin and F. Darwin | Canary grass (*Phalaris canariensis*) and oat **coleoptiles** illuminated from one side; removing the tip, or covering the tip with an opaque cap, abolished bending, whereas shading only the region below the tip did not | The tip perceives light and transmits an "influence" downward that makes the lower part bend |
| 1913 | P. Boysen-Jensen | A gelatin block inserted between tip and base still allowed bending; a mica sheet inserted on the shaded side prevented it | The influence can pass through gelatin: it is a diffusible chemical, transmitted down the shaded side |
| 1919 | Á. Paál | A cut tip placed off-center on the cut surface in darkness | The base bends away from the side bearing the tip: the tip produces a growth-promoting substance, and one-sided light distributes it unevenly |
| 1926–1928 | F. W. Went | Cut tips placed on agar blocks, and the blocks placed off-center on decapitated coleoptiles; the curvature is proportional to the amount of substance in the block | A diffusible growth-promoting substance was collected, and a quantitative Avena test was established |
| 1934 | F. Kögl, A. J. Haagen-Smit and others | Isolation and purification from urine and fungal cultures | Identified as indole-3-acetic acid (IAA), later confirmed in plants |

![Four classic experiments in the discovery of auxin (coleoptiles of oat or canary grass; schematic). A: Darwin (1880): an intact coleoptile bends toward one-sided light; it does not bend if the tip is removed or covered with an opaque cap, and it still bends if the region below the tip is shaded. B: Boysen-Jensen (1913): bending still occurs with a gelatin block between tip and base, but not when a mica sheet is inserted on the shaded side. C: Paál (1919): a cut tip placed off-center in the dark makes the coleoptile bend to the opposite side. D: Went (1926–1928): substance from the tip diffuses into an agar block; the block placed off-center on a decapitated coleoptile makes it bend to the opposite side, and the curvature angle $\alpha$ is proportional to the amount of auxin in the block over a certain range](./plots/classic-experiments.py)

Went's method became the first bioassay for a hormone:

**Definition 13.2.1 (Avena Curvature Test)** The **Avena curvature test** is the method in which an agar block containing the substance to be assayed is placed off-center on the cut surface of a decapitated oat coleoptile grown in the dark; after a fixed time (about 1.5–2 h) the angle by which the coleoptile bends toward the opposite side is measured, and auxin activity is determined from the proportionality between curvature and the auxin content of the block over a certain range.

The quantitative basis of the test is a simple linear relation: auxin passes from the agar block into the cells on one side beneath it, the elongation rate on that side increases, and the curvature angle $\alpha$ is approximately proportional to the difference in elongation between the two sides. At low concentrations the increase in elongation is proportional to the amount of auxin, so

$$
\alpha \approx a\,m \qquad (m \text{ below the saturation level}),
\tag{13.3}
$$

where $m$ is the amount of auxin in the agar block and $a$ is determined from a standard curve. Beyond a certain amount the curvature saturates (elongation is close to its maximum). Went also used the test to show that one-sided light causes lateral transport of auxin in the tip toward the shaded side, rather than destruction of auxin on the lit side; this gave rise to the Cholodny–Went theory of phototropism ([7.13.19](/7.13.19)).

**Example 13.2.1** A standard curve for the Avena test is made with IAA solutions: agar blocks containing $0$, $20$, $40$ and $60\ \mathrm{ng}$ of IAA cause curvatures of $0.5^\circ$, $8.3^\circ$, $16.1^\circ$ and $24.2^\circ$, and a block containing $100\ \mathrm{ng}$ causes $29^\circ$. A coleoptile tip is left on an agar block for 2 h, and the block then causes a curvature of $12.0^\circ$. Estimate how much auxin diffuses out of the tip per hour.

**Solution** Over 0–60 ng, curvature is linear in content: a least-squares fit gives a slope $a = 0.395^\circ/\mathrm{ng}$ and an intercept of $0.44^\circ$; the 100 ng point already deviates from the line (saturation) and is not used in the fit. A curvature of $12.0^\circ$ corresponds to $m = (12.0 - 0.44)/0.395 \approx 29\ \mathrm{ng}$, that is about $15\ \mathrm{ng\,h^{-1}}$. A standard curve must be used only within its linear range; when the curvature of a test sample falls in the saturated region, the sample should be diluted and measured again (fitting of standard curves and quantitation ranges are discussed in [7.7.11](/7.7.11#sec-11.5)).

### 13.2.2. Natural Auxins, Synthetic Auxins and Antiauxins

**Definition 13.2.2 (Auxin)** Indole-3-acetic acid and other compounds that, like indole-3-acetic acid, promote elongation of stem and coleoptile segments at low concentrations and can be transported polarly are collectively called **auxins**.

IAA is the most abundant and physiologically most important auxin in plants. Some species contain others: 4-chloroindole-3-acetic acid (4-Cl-IAA, in seeds of legumes such as pea), phenylacetic acid (PAA, often more abundant than IAA but less active and hardly transported polarly), and indole-3-butyric acid (IBA, converted to IAA by $\beta$-oxidation in peroxisomes and regarded as a precursor and storage form of IAA).

The structure of IAA is simple, and many compounds with auxin activity were synthesized early on; what they share is an aromatic ring and a side chain with a negatively charged carboxyl group:

| Class | Compound | Use |
|---|---|---|
| Indoles | Indole-3-butyric acid (IBA) | Rooting of cuttings (most common, safe for plants) |
| Naphthalenes | $\alpha$-Naphthaleneacetic acid (NAA) | Rooting, flower and fruit thinning, prevention of preharvest fruit drop; cheap and stable |
| Phenoxycarboxylic acids | 2,4-Dichlorophenoxyacetic acid (2,4-D), 2-methyl-4-chlorophenoxyacetic acid (MCPA) | Low concentrations induce callus in tissue culture; high concentrations kill broadleaf weeds |
| Benzoic acids | Dicamba | Herbicide |
| Pyridinecarboxylic acids | Picloram | Herbicide, tissue culture |

Compounds that compete with auxin for the receptor and have little or no activity themselves are called antiauxins, for example $\alpha$-(p-chlorophenoxy)isobutyric acid (PCIB). Another group of compounds does not act on the receptor but inhibits polar transport (Section 13.4): 2,3,5-triiodobenzoic acid (TIBA), N-1-naphthylphthalamic acid (NPA, which binds and inhibits PINs directly and also acts on ABCB transporters and their regulators), and 1-naphthoxyacetic acid (1-NOA, which inhibits uptake by AUX1/LAX). Natural flavonoids can also inhibit auxin efflux.

## 13.3. Auxin Biosynthesis, Conjugation and Degradation

### 13.3.1. Sites of Synthesis and the TAA–YUC Pathway

Almost all plant tissues can synthesize small amounts of IAA, but the main sites of synthesis are rapidly dividing and growing tissues: the shoot apical meristem, young leaves, and developing fruit and seeds. The root tip also synthesizes auxin locally, which is important for forming the auxin maximum in the root.

The structure of IAA is close to that of tryptophan. Conversion of tryptophan to IAA requires deamination (transamination), decarboxylation and oxidation of the side chain, and there are several pathways, distinguished by their intermediates:

| Pathway | Key steps and enzymes | Distribution and status |
|---|---|---|
| Indole-3-pyruvic acid (IPyA) pathway | The tryptophan aminotransferases TAA1/TAR convert tryptophan to IPyA; the flavin monooxygenase YUCCA (YUC) oxidatively decarboxylates IPyA to IAA | The main pathway in plants; the YUC step is usually rate-limiting |
| Tryptamine (TAM) pathway | Tryptophan decarboxylase forms tryptamine, which is oxidized to IAA via indole-3-acetaldehyde | Present in some plants; contribution unclear |
| Indole-3-acetaldoxime (IAOx) pathway | CYP79B2/B3 convert tryptophan to IAOx, which gives IAA via indole-3-acetonitrile and nitrilase | Mainly in the Brassicaceae (shares intermediates with indolic glucosinolate synthesis) |
| Indole-3-acetamide (IAM) pathway | Tryptophan monooxygenase (iaaM) and IAM hydrolase (iaaH) | Mainly in bacteria, for example genes on the T-DNA of *Agrobacterium tumefaciens* and in *Pseudomonas savastanoi* |
| Tryptophan-independent pathway | Direct synthesis from indole-3-glycerol phosphate or indole | Inferred from tryptophan-deficient mutants (maize *orp*, *Arabidopsis* *trp* mutants); its existence is still debated |

The IPyA pathway was established through genetics. The dominant *Arabidopsis* mutant *yucca* (overexpressing a *YUC* gene) has elevated free IAA and shows stronger apical dominance, tall inflorescences, and narrow, upward-curled leaves resembling a yucca (*Yucca*); mutants lacking *taa1* together with several *YUC* genes have severe defects in embryo and flower development consistent with auxin deficiency. Biochemical work in 2011 showed that TAA and YUC act in tandem as two steps of the same pathway.

**Remark 13.3.1** Chinese textbooks and competition materials often state that "zinc is a component of tryptophan synthase; zinc deficiency lowers tryptophan, hence IAA, and causes little-leaf disease in fruit trees". Zinc deficiency does lower IAA content and causes small leaves and shortened internodes, but tryptophan synthase is an enzyme with **pyridoxal phosphate** as its cofactor and contains no zinc. The exact step at which zinc deficiency affects auxin is still unclear, and may involve the supply of tryptophan and the oxidation of IAA; it should not be written as "zinc is a component of tryptophan synthase".

### 13.3.2. Conjugation and Degradation

Auxin in a tissue exists in two states. Free IAA is physiologically active and can be transported polarly; conjugated IAA is covalently linked to sugars, inositol, amino acids or peptides and has little or no activity. In many tissues the conjugated form is by far the larger pool: in *Arabidopsis* seedlings free IAA is about 1% of the total, amide conjugates about 90% and ester conjugates about 10%; in maize kernels IAA esters with glucose and inositol predominate.

Conjugates fall into two classes according to their fate:

- Reversible storage forms: esters (IAA-glucose, IAA-inositol) and some amides (IAA-Ala, IAA-Leu), which hydrolases (such as the ILR1/ILL family of *Arabidopsis*) rapidly convert back to free IAA. In germinating maize seeds, IAA-inositol from the kernel is carried to the coleoptile tip and hydrolyzed there, one source of auxin for the early seedling. IBA and its conjugates can also be regarded as storage forms.
- Irreversible precursors of degradation: amide synthetases of the GH3 family link IAA to aspartate or glutamate, and IAA-Asp and IAA-Glu, after further oxidation, no longer release IAA. The *GH3* genes are themselves strongly induced by auxin, forming negative feedback.

Irreversible degradation of IAA is mainly oxidative: the dioxygenase DAO oxidizes IAA (or its conjugates) to 2-oxindole-3-acetic acid (oxIAA), which is then conjugated to glucose; this is the main degradative pathway in *Arabidopsis* and rice. The decarboxylative degradation by "IAA oxidase" (actually a peroxidase), which older textbooks emphasized (product 3-methyleneoxindole), is obvious in vitro but may play little role in vivo. IAA solutions are readily photo-oxidized to indole aldehyde and other products in light (especially in the presence of riboflavin), so IAA stock solutions in the laboratory must be protected from light, and agriculture uses the photostable NAA and IBA.

![Auxin biosynthesis, conjugation and degradation (simplified). Tryptophan is transaminated by TAA to indole-3-pyruvic acid, which YUC oxidatively decarboxylates to IAA (main pathway); IBA is converted to IAA by $\beta$-oxidation in peroxisomes. Reversible conjugation (left): IAA forms esters with glucose and inositol and amides with alanine and leucine, and hydrolases can release IAA again. Irreversible inactivation (right): GH3 links IAA to aspartate and glutamate, and DAO oxidizes IAA to oxIAA, which is then conjugated to glucose. Solid arrows indicate reactions, double-headed arrows reversible conversions](./plots/auxin-metabolism.py)

### 13.3.3. Auxin Homeostasis

The level of free IAA is set jointly by synthesis, release from conjugates, import and export, conjugation and degradation (Eq. (13.1)); in addition, sequestration of IAA in the endoplasmic reticulum affects the amount available for signaling. Auxin is toxic at high concentrations, and without homeostatic control it could quickly reach harmful levels; the strength of this control is seen in plants overexpressing *YUC*, in which synthesis is greatly increased but free IAA rises only a few-fold, because conjugation and oxidation increase in parallel.

**Example 13.3.1 (Turnover of the Auxin Pool)** The steady-state content of free IAA in a tissue is $20\ \mathrm{pmol\,g^{-1}}$ (fresh weight). After synthesis is blocked with a YUC inhibitor, free IAA declines with first-order kinetics and is $5\ \mathrm{pmol\,g^{-1}}$ after $2\ \mathrm{h}$. Find the overall rate constant for removal of free IAA, its half-life, and the rate of synthesis at steady state (assume other inputs are negligible).

**Solution** $c(t) = c_0\mathrm{e}^{-kt}$, $k = \ln(20/5)/2\ \mathrm{h} = 0.693\ \mathrm{h^{-1}}$, and the **half-life** is $t_{1/2} = \ln 2/k = 1.0\ \mathrm{h}$. At steady state synthesis equals removal: $s = k c^* = 0.693 \times 20 \approx 14\ \mathrm{pmol\,g^{-1}\,h^{-1}}$. In other words, the free IAA pool is renewed in about 1.4 h ($1/k$), and the tissue maintains its auxin level only through continued synthesis and import; the rapid fall of auxin in the tissue below the shoot tip after the tip is removed, and the resulting slowing of growth, reflect exactly this. (The numerical values are hypothetical, for illustration.)

## 13.4. Auxin Transport

### 13.4.1. The Phenomenon of Polar Transport

Auxin is the only plant hormone transported between cells in a directional manner that consumes energy.

**Definition 13.4.1 (Polar Auxin Transport)** The energy-dependent, short-distance transport of auxin between parenchyma cells in a fixed direction (in stems, from the morphological apex toward the morphological base) is called **polar auxin transport**.

Characteristics of polar transport:

- The direction is determined by the morphological polarity of the tissue and is independent of gravity: if a stem segment is inverted, auxin is still transported from the morphological apex to the base; if willow or bamboo cuttings are planted upside down, adventitious roots still form at the morphological base.
- It depends on energy: anoxia, lack of sucrose or respiratory inhibitors stop transport.
- The speed is about $5$–$20\ \mathrm{mm\,h^{-1}}$ (about $10\ \mathrm{mm\,h^{-1}}$ in most tissues), much faster than diffusion but far slower than phloem transport (about $0.5$–$1\ \mathrm{m\,h^{-1}}$, [7.13.11](/7.13.11)). The "5–20 cm/h" often seen in Chinese sources is a unit error.
- It is specific: natural and some synthetic auxins are transported, whereas other weak organic acids, inactive analogs and conjugates of IAA are hardly transported.
- It can be blocked by transport inhibitors such as TIBA and NPA.

The classic method of measurement is the donor–receiver agar block method: an agar block containing radioactive IAA is placed at one end of a stem or coleoptile segment and a blank agar block at the other end, and the radioactivity in the receiver block is measured after a certain time. Radioactivity enters the receiver block in quantity only when the donor block is placed at the morphological apex; varying the segment length allows the speed of transport to be calculated from the time of appearance of radioactivity.

The tissues through which transport proceeds differ among organs: in oat coleoptiles, through the parenchyma cells of nonvascular tissue; in the stems of dicots, mainly through parenchyma cells of the vascular bundles (cambium and xylem parenchyma). In the root there is a "fountain-like" circulation: auxin from the shoot is transported through the stele toward the root tip (rootward), collects in the root cap and near the quiescent center, and is carried back through the epidermis and outer cortex to the elongation zone (shootward), with part of it returning to the stele through the cortex. This local circulation of auxin in the root underlies the root's gravitropism and the maintenance of the root apical meristem ([7.13.18](/7.13.18), [7.13.19](/7.13.19)).

### 13.4.2. The Chemiosmotic Model

How does auxin achieve directional transport? The key is that IAA is a weak acid ($\mathrm{p}K_{\mathrm{a}} = 4.75$), while the pH of the cell wall differs from that of the cytosol.

**Definition 13.4.2 (Chemiosmotic Model of Polar Auxin Transport)** The model proposed by Rubery and Sheldrake (1974) and Raven (1975) to explain polar auxin transport is called the **chemiosmotic model of polar auxin transport**: the plasma membrane H⁺-ATPase keeps the cell wall acidic, where part of the IAA is undissociated and lipophilic and can diffuse into the cell, while the anion enters through proton symporters; in the neutral cytosol IAA dissociates into an anion that cannot cross the membrane and is thus "trapped", leaving the cell only through efflux carriers concentrated at one end of the cell on the plasma membrane, which results in a net directional transport.

The extent of acid–base "ion trapping" can be calculated with the **Henderson–Hasselbalch equation**. The undissociated fraction of IAA is

$$
f_{\mathrm{HA}} = \frac{1}{1 + 10^{\,\mathrm{pH} - \mathrm{p}K_{\mathrm{a}}}}.
\tag{13.4}
$$

If only undissociated IAAH can cross the plasma membrane, [IAAH] is equal on the two sides at equilibrium, and the ratio of total auxin concentration inside to that outside is

$$
\frac{c_{\mathrm{in}}}{c_{\mathrm{out}}} = \frac{1 + 10^{\,\mathrm{pH_{in}} - \mathrm{p}K_{\mathrm{a}}}}{1 + 10^{\,\mathrm{pH_{out}} - \mathrm{p}K_{\mathrm{a}}}}.
\tag{13.5}
$$

**Example 13.4.1** The cell wall pH is 5.5, the cytosolic pH is 7.2, and the $\mathrm{p}K_{\mathrm{a}}$ of IAA is 4.75. (a) What fraction of IAA in the cell wall is undissociated? (b) By IAAH diffusion alone, how many-fold can the cell concentrate auxin at equilibrium?

**Solution** (a) $10^{5.5-4.75} = 10^{0.75} = 5.62$, so $f_{\mathrm{HA}} = 1/6.62 = 15\%$ (36% at a cell wall pH of 5). (b) In the cytosol $10^{7.2-4.75} = 10^{2.45} = 282$, and by Eq. (13.5), $c_{\mathrm{in}}/c_{\mathrm{out}} = 283/6.62 \approx 43$. Almost all (99.6%) of the IAA in the cytosol is present as the anion.

If cells only took up auxin and had no efflux pathway, auxin would accumulate in the cells and would not be transported. The second part of the model is asymmetric efflux:

- Uptake: besides passive diffusion of IAAH, symporters of the AUX1/LAX family carry one $\mathrm{IAA^-}$ together with two $\ce{H+}$ into the cell, driven by the proton-motive force, so that the capacity for accumulation is much greater than that of diffusion alone. The root of the *aux1* mutant has lost gravitropism; 1-NOA inhibits this uptake.
- Efflux: the negatively charged $\mathrm{IAA^-}$ in the cytosol tends to leave, driven by the negative membrane potential (the passive direction), but it cannot cross the lipid bilayer directly and needs efflux carriers. PIN proteins (named for the pin-shaped inflorescence of the *Arabidopsis* *pin1* mutant) are polarly localized in the cell; for example, in vascular parenchyma cells of the stem they are concentrated at the basal end of the cell (the end toward the root), so that auxin is passed downward from cell to cell. ABCB transporters (ATP-driven) are mostly nonpolar and cooperate with PINs, preventing re-uptake of exported auxin, which is especially important in small cells; the maize *br2* mutant (defective in ABCB1) has shortened internodes.

![The chemiosmotic model of polar auxin transport. One cell in a file of cells: the plasma membrane H⁺-ATPase pumps H⁺ into the cell wall and keeps it at about pH 5.5; there about 15% of IAA is in the lipophilic undissociated form (IAAH) and can diffuse into the cell, while the anion (IAA⁻) enters by symport with 2 H⁺ through AUX1/LAX. In the cytosol at about pH 7.2 almost all IAA is dissociated into IAA⁻, which cannot cross the membrane and leaves only through PIN efflux carriers concentrated on the plasma membrane at the basal end of the cell (and through nonpolar ABCB transporters), entering the cell wall of the next cell. The polar localization of PIN determines the direction of transport (downward here)](./plots/chemiosmotic.py)

Localization and function of the main members of the *Arabidopsis* PIN family:

| Protein | Main localization | Function | Loss-of-function phenotype |
|---|---|---|---|
| PIN1 | Basal end of vascular parenchyma cells of stem and inflorescence axis; side of shoot apex epidermal cells facing the primordium | Rootward transport in the stem; specification of the positions of leaf and flower primordia ([7.13.18](/7.13.18)) | Pin-shaped inflorescence, no flowers; fused cotyledons |
| PIN2 | Side of root epidermal cells facing the shoot (away from the root tip), and side of cortical cells facing the root tip | Shootward transport and reflux in the root | Loss of root gravitropism |
| PIN3, PIN7 | Root cap columella cells (can relocate with gravity), stem endodermis | Lateral redistribution of auxin in tropic responses | Reduced gravitropism and phototropism |
| PIN4 | Near the root quiescent center | Maintains the auxin maximum at the root tip | Abnormal cell patterning of the root meristem |
| PIN5, PIN8 | Endoplasmic reticulum membrane | Intracellular compartmentation, regulating available auxin | Weak phenotype |

The polarity of PINs is not fixed: they cycle continuously between plasma membrane and endosomes by endocytosis and exocytosis, are returned to specific membrane faces by vesicle trafficking controlled by the guanine-nucleotide exchange factor GNOM, have their polarity regulated through phosphorylation by the protein kinase PINOID and the phosphatase PP2A, and have their activity regulated by the protein kinase D6PK. Auxin itself can induce PIN expression and alter its localization, so that auxin flow can be "self-reinforcing" and converge from diffuse flow into narrow channels; this is the basis of the "canalization" hypothesis of vascular tissue differentiation (Section 13.5.3).

### 13.4.3. Quantitative Description of Transport: The Advection–Diffusion Equation

Treating a file of cells as a continuum, the auxin concentration $c(x,t)$ along the direction of transport $x$ satisfies the advection–diffusion–degradation equation:

$$
\frac{\partial c}{\partial t} = D\frac{\partial^2 c}{\partial x^2} - v\frac{\partial c}{\partial x} - k c,
\tag{13.6}
$$

where $v$ is the effective drift velocity produced by polar transport (determined by the asymmetry of PINs), $D$ is the effective diffusion coefficient (including membrane permeation and nonpolar efflux), and $k$ is the rate constant for losses due to conjugation and degradation. The derivation of the equation and the general properties of the diffusion equation are given in [2.5.1](/2.5.1#sec-1.2); **Fick's law** gives the flux term. For an instantaneous pulse, the solution is a Gaussian peak that moves with velocity $v$, broadens in width as $\sqrt{2Dt}$ and decays in total amount as $\mathrm{e}^{-kt}$.

The relative importance of advection and diffusion can be compared with the Péclet number $\mathrm{Pe} = vL/D$.

**Example 13.4.2** The diffusion coefficient of IAA in water is about $7\times10^{-10}\ \mathrm{m^2\,s^{-1}}$ (about $2.5\ \mathrm{mm^2\,h^{-1}}$). (a) By diffusion alone, how long does it take IAA to move on average $10\ \mathrm{mm}$ and $1\ \mathrm{m}$ (use $t \approx L^2/2D$)? (b) What about polar transport at $10\ \mathrm{mm\,h^{-1}}$? (c) Find the Péclet number for $L = 10\ \mathrm{mm}$.

**Solution** (a) For $10\ \mathrm{mm}$: $t = 100/(2\times2.5) = 20\ \mathrm{h}$; for $1\ \mathrm{m}$: $t = 10^6/5 = 2\times10^5\ \mathrm{h}$, about 23 years. (Obstruction by cell membranes and walls makes the actual effective diffusion even slower.) (b) $10\ \mathrm{mm}$ takes 1 h and $1\ \mathrm{m}$ takes 100 h (about 4 d). (c) $\mathrm{Pe} = 10 \times 10/2.5 = 40 \gg 1$, so transport is dominated by advection. The time for diffusion grows with the square of the distance, whereas the time for directed transport grows linearly with distance, so on scales above a millimeter polar transport is the only feasible way to move auxin over long distances; on the scale of a few cells (tens of micrometers), $\mathrm{Pe} < 1$ and local diffusion is still important.

![An auxin pulse in the one-dimensional advection–diffusion–degradation model (numerical solution of Eq. (13.6)). A: Auxin distribution 1, 2, 4 and 6 h after a pulse entering a stem segment ($x = 0$), with $v = 10\ \mathrm{mm\,h^{-1}}$, effective diffusion coefficient $D = 2.5\ \mathrm{mm^2\,h^{-1}}$ and loss rate constant $k = 0.1\ \mathrm{h^{-1}}$; dashed lines show the distribution with diffusion and loss only ($v = 0$). B: Auxin received over time by "receiver blocks" 10 mm and 30 mm from the source: with polar transport the peaks arrive at about 1 h and 3 h, and the transport speed can be obtained from the difference in arrival times; with diffusion alone almost nothing is received at 30 mm](./plots/auxin-pulse.py)

### 13.4.4. Nonpolar Transport

Most of the IAA synthesized in mature leaves, together with auxin conjugates, enters the phloem and is carried at phloem speed with the mass flow of assimilates to sink organs such as roots and young leaves; the direction depends on the positions of source and sink and not on tissue polarity, and no energy is spent on the transport itself. This pathway carries large amounts at high speed. It coexists in the stem with the "vascular parenchyma channel" of polar transport, and the two can exchange auxin at certain sites: auxin in the phloem can be unloaded into the cambial region or the pericycle, where it takes part in cambial activity and the initiation of lateral roots. Xylem sap also contains a little auxin.

## 13.5. Physiological Effects of Auxin

### 13.5.1. Promotion of Cell Elongation

The earliest recognized action of auxin was promotion of elongation of stem and coleoptile cells. In an intact plant, endogenous auxin is already near the optimum, and spraying exogenous auxin gives only a brief and small increase in growth. After a segment containing the elongation zone is cut out and its endogenous auxin depleted, however, its growth falls quickly to a very low basal level; after IAA is added the growth rate begins to rise after about 10–12 min and reaches 5–10 times the basal rate within 30–60 min. Auxin-induced growth requires energy and protein synthesis and is accompanied within minutes, in coleoptiles, by acidification of the cell wall: this is the basis of the acid-growth theory, in which $\ce{H+}$ pumped out by the plasma membrane H⁺-ATPase activates expansins and loosens the cell wall (for the mechanism and wall mechanics see [7.13.17](/7.13.17)). On a longer time scale, auxin also sustains growth by inducing, through the TIR1/AFB–Aux/IAA–ARF pathway, the expression of early response genes (the *Aux/IAA*, *GH3* and *SAUR* families are induced within minutes to tens of minutes).

In the stems of dicots the growth rate is limited by the outer tissues (epidermis and outer cortex). When a stem segment of an etiolated pea seedling is split lengthwise into two halves, the halves curve outward in buffer (the inner tissue elongates faster) and inward in buffer containing auxin, showing that auxin promotes the elongation of the outer tissues. Auxin coming from the shoot tip must therefore be transferred laterally from the transport stream in the vascular parenchyma cells to the outer tissues.

### 13.5.2. Dose–Response and Organ Sensitivity

Organs differ enormously in their sensitivity to auxin. The classic curves summarized by Thimann (1937) show that the optimum concentration for elongation is about $10^{-10}\ \mathrm{mol\,L^{-1}}$ for roots, about $10^{-8}\ \mathrm{mol\,L^{-1}}$ for buds and about $10^{-5}\ \mathrm{mol\,L^{-1}}$ for stems; below the optimum the effect increases with concentration, above the optimum it declines, and at still higher concentrations growth is inhibited. Stem segments are inhibited above about $10^{-4}\ \mathrm{mol\,L^{-1}}$, a concentration far beyond what roots tolerate: $10^{-10}$–$10^{-9}\ \mathrm{mol\,L^{-1}}$ promotes the growth of intact roots, and $10^{-6}\ \mathrm{mol\,L^{-1}}$ already inhibits it strongly. Chinese textbooks summarize this as the dual nature of auxin action: low concentrations promote and high concentrations inhibit, with sensitivity root > bud > stem.

The bell-shaped dose-response curve can be described by the product of a promoting term and an inhibiting term:

$$
E(c) = E_{\max}\,\frac{c^{\,n_1}}{K_1^{\,n_1} + c^{\,n_1}}\cdot\frac{K_2^{\,n_2}}{K_2^{\,n_2} + c^{\,n_2}},
\tag{13.7}
$$

where $K_1$ is the half-saturating concentration of the promoting action, $K_2 > K_1$ is the half-inhibiting concentration of the inhibiting action, and the optimum lies between the two ($c_{\mathrm{opt}} = \sqrt{K_1K_2}$ when $n_1 = n_2 = n$). A simpler phenomenological description writes the effect as a Gaussian function of $\log c$: $E = E_{\max}\exp\left[-(\log_{10}c - \log_{10}c_{\mathrm{opt}})^2/2w^2\right]$, where $w$ expresses the width of the curve in orders of magnitude. Both forms only describe the phenomenon; the essential point is that the difference between organs is mainly a shift of the curve along the concentration axis (sensitivity) and not a difference in shape.

![Dose-response curves of root, bud and stem growth to auxin (promoting and inhibiting terms of Eq. (13.7), written in product form: growth = (1 + promoting term) × inhibiting term; parameters chosen so that the optimum concentrations are about $10^{-10}$, $10^{-8}$ and $10^{-5}\ \mathrm{mol\,L^{-1}}$, illustrating the classic result of Thimann 1937). The vertical axis is the change in growth relative to no added auxin: positive values are promotion and negative values inhibition. The same concentration (for example $10^{-6}\ \mathrm{mol\,L^{-1}}$, vertical line) can promote stem growth and inhibit root growth at the same time](./plots/dose-response.py)

Where does the inhibition at high concentration come from? One main reason is auxin-induced ethylene synthesis: auxin induces *ACC synthase* genes at the transcriptional level, higher auxin concentrations make the tissue produce ethylene, and ethylene inhibits elongation ([7.13.15](/7.13.15)). Even when ethylene synthesis is blocked, roots remain much more sensitive to auxin than stems, which shows that the difference in sensitivity lies also in receptors and signaling components. In the root, auxin and ethylene promote each other's synthesis and transport and together control the length of the elongation zone.

**Remark 13.5.1** The classic dose-response curves were measured by adding exogenous auxin to segments or to the medium, and the horizontal axis is the concentration of the external solution and not the concentration inside the cell; because of uptake, ion trapping (Example 13.4.1), conjugation and degradation, the two can differ by one or two orders of magnitude. The statement "the optimum concentration for roots is $10^{-10}\ \mathrm{mol\,L^{-1}}$" should therefore be understood only as a relative comparison of sensitivity between organs.

### 13.5.3. Induction of Vascular Differentiation

Auxin induces the differentiation of vascular tissue. Auxin produced by newly formed leaves flows downward by polar transport and induces the formation of vascular bundles beneath them, connecting the leaf veins to the vascular system of the stem. The classic experiment is wound regeneration in the stem of *Coleus*: after a vascular bundle is cut, xylem that bypasses the wound is redifferentiated from parenchyma cells above the wound, and the amount of regeneration is proportional to the amount of auxin coming from the leaves above; removing the leaves above reduces regeneration, and IAA in place of the leaves restores it (Jacobs, 1952). From this Sachs proposed the canalization hypothesis: the flow of auxin induces the cells that carry it to increase their capacity for transport (PIN expression and polarization), so that the flow gradually concentrates into narrow files of cells, and these cells differentiate into vascular tissue. In tissue culture, lower auxin concentrations favor phloem differentiation and higher ones favor xylem differentiation; auxin and cytokinin together maintain the activity of the **vascular cambium**.

### 13.5.4. Lateral Roots and Adventitious Roots

**Lateral roots** originate from **pericycle** cells ([7.12.20](/7.12.20)). Auxin accumulates to a certain level in the founder cells of the pericycle, inducing their asymmetric division, and is needed continuously during the development of the lateral root primordium and its emergence through the cortex and epidermis. Inhibitors of auxin transport, or mutants such as *aux1* and *slr* (a dominant mutation of *IAA14*), form almost no lateral roots, whereas exogenous auxin greatly increases their number.

The formation of **adventitious roots** also depends on auxin. Treating the base of cuttings with IBA or NAA markedly promotes rooting, which is the most important horticultural use of auxin; polar transport of auxin in the stem makes auxin accumulate at the morphological base of the cutting, so that an inverted cutting still roots at its morphological base (Section 13.4.1).

### 13.5.5. Development of Flowers and Fruit

In most plants exogenous auxin inhibits flowering, which may be a secondary effect of auxin-induced ethylene; the Bromeliaceae (pineapple and relatives) are an exception, in which auxin or ethylene strongly promotes flowering, and NAA or ethephon is used in production to induce flowering. In cucurbits such as cucumber, auxin treatment increases the proportion of female flowers, possibly also through ethylene ([7.13.15](/7.13.15)).

Fruit growth depends on auxin supplied by the developing seeds. Nitsch's experiments on strawberry (1950) demonstrated this: the "seeds" of strawberry are achenes on the surface of the enlarged receptacle; when all the achenes are removed the receptacle does not enlarge, when a ring of achenes is removed only the part retaining its achenes enlarges, and when IAA or NAA is applied to a receptacle stripped of achenes it enlarges normally. After pollination, auxin (and gibberellin) in the ovules starts the growth of the ovary, which is also one of the signals by which pollination triggers fruit set ([7.13.23](/7.13.23)). Exogenous auxin can replace pollination and induce **parthenocarpy** in tomato, pepper, cucumber, zucchini, citrus and others; low temperatures in early spring easily cause flower and fruit drop in tomato, and spraying the flowers with auxin preserves flowers and fruit.

### 13.5.6. Apical Dominance, Tropisms and Other Effects

Auxin produced by the shoot tip moves downward and inhibits the growth of axillary buds, the classic explanation of **apical dominance**; it is now known that auxin does not enter the axillary bud directly but acts indirectly, by inhibiting cytokinin synthesis at the node, promoting **strigolactone** synthesis and competing with the bud for transport channels, with the sucrose supply also involved ([7.13.18](/7.13.18)). Phototropism and gravitropism result from the lateral redistribution of auxin ([7.13.19](/7.13.19)). Auxin also keeps leaves on the plant: a stable auxin supply from the leaf makes the abscission zone insensitive to ethylene, and only after the leaf senesces and auxin declines does the abscission zone become sensitive to ethylene and abscission occurs ([7.13.24](/7.13.24)). In addition, auxin promotes cambial activity, epinastic growth of lateral organs and the attraction of assimilates by sink organs (photosynthate accumulates at sites where auxin is applied).

## 13.6. Synthetic Auxins and Herbicides

In the 1940s it was discovered that high concentrations of 2,4-D and MCPA kill broadleaf weeds while damaging grass crops little. They were the first selective organic herbicides and are still widely used. The way synthetic auxins kill can be understood in terms of hormone homeostasis: once IAA exceeds the optimum concentration it is conjugated and oxidized, whereas 2,4-D and similar compounds are poorly recognized by these enzymes and can be absorbed and partly transported polarly, so that a supraoptimal "auxin signal" is maintained in the tissue. They bind the TIR1/AFB receptors (different synthetic auxins prefer different AFB family members; for example picloram acts mainly through AFB5) and continuously degrade Aux/IAA repressors, which triggers a cascade of consequences: the ethylene biosynthetic enzyme ACC synthase is induced and large amounts of ethylene are produced; NCED, the rate-limiting enzyme of abscisic acid synthesis, is induced, and the accumulating ABA closes stomata and stops growth; a burst of reactive oxygen species occurs, tissues become twisted and epinastic, vascular tissue proliferates abnormally, and the plant finally dies.

Reasons why dicots are more sensitive than monocot grasses include: grasses metabolize synthetic auxins more quickly into inactive conjugates; monocots have scattered vascular bundles and lack a vascular cambium that responds strongly to auxin; and there are differences in uptake and transport.

"Agent Orange", used in the Vietnam War, was a mixture of 2,4-D and 2,4,5-T; its serious harm came mainly from the by-product dioxin (2,3,7,8-tetrachlorodibenzo-p-dioxin) contaminating the production of 2,4,5-T, and not from auxin activity itself; 2,4,5-T has since been banned.

Main uses of auxin-type regulators:

| Use | Common agents | Principle |
|---|---|---|
| Rooting of cuttings | IBA, NAA | Promotes initiation of adventitious roots (Section 13.5.4) |
| Fruit set and parthenocarpy | 4-Chlorophenoxyacetic acid, NAA, 2,4-D (low concentration) | Replaces auxin from seeds (Section 13.5.5) |
| Flower and fruit thinning | NAA, naphthaleneacetamide | Higher concentrations induce ethylene and promote drop of young fruit, regulating alternate bearing |
| Prevention of preharvest drop | NAA, 2,4-D | Maintains insensitivity of the abscission zone to ethylene ([7.13.24](/7.13.24)) |
| Flower induction | NAA (Bromeliaceae) | Induces flowering through ethylene |
| Tissue culture | 2,4-D, NAA, IAA | Induces callus and roots (ratio to cytokinin, [7.13.14](/7.13.14)) |
| Weed control | 2,4-D, MCPA, dicamba, picloram | Sustained supraoptimal auxin signal |

## Summary

| Aspect | Key points |
|---|---|
| Concepts | Plant growth substances = plant hormones (endogenous, very low concentrations) + plant growth regulators (synthetic); nine hormone classes: auxin, gibberellin, cytokinin, abscisic acid, ethylene (the classical five), brassinosteroid, jasmonate, salicylic acid, strigolactone |
| Shared logic | Concentration is set by the balance of synthesis, transport, conjugation and degradation (Eq. (13.1)); receptors mostly act by derepression (ubiquitin–proteasome, negatively acting kinases/phosphatases, two-component systems); effects depend on concentration and tissue sensitivity |
| Discovery | Darwin (1880, tip perceives light) → Boysen-Jensen (1913, passes through gelatin) → Paál (1919, off-center tip) → Went (1926–1928, agar blocks and the Avena test) → Kögl and others (1934, IAA) |
| Kinds | Natural: IAA (main), 4-Cl-IAA, PAA, IBA; synthetic: NAA, 2,4-D, MCPA, dicamba, picloram; antiauxin PCIB; transport inhibitors TIBA, NPA, 1-NOA |
| Synthesis | Shoot apex, young leaves, developing seeds and fruit; main pathway tryptophan →(TAA)→ IPyA →(YUC)→ IAA; IAOx pathway (Brassicaceae), IAM pathway (bacteria) |
| Conjugation and degradation | Free form active; conjugates (about 99% in *Arabidopsis*) mostly storage; reversible: IAA-glucose, IAA-inositol, IAA-Ala/Leu; irreversible: GH3 → IAA-Asp/Glu, DAO → oxIAA; photooxidation |
| Transport | Polar transport: morphological apex → base, energy-dependent, about 5–20 mm/h, independent of gravity; chemiosmotic model: IAAH diffusion in the acidic cell wall + AUX1/LAX uptake ($\mathrm{IAA^-}$ + 2 $\ce{H+}$), dissociation and trapping in the cytosol, efflux by polarly localized PIN (+ ABCB); nonpolar transport: phloem, with assimilates |
| Physiological effects | Cell elongation (10 min lag, acid growth); vascular differentiation (canalization); lateral and adventitious roots; fruit set, parthenocarpy; apical dominance; tropisms; delay of abscission; induction of ethylene |
| Dose-response | Optimum for root about $10^{-10}$, bud about $10^{-8}$, stem about $10^{-5}\ \mathrm{mol\,L^{-1}}$; supraoptimal inhibition (partly through ethylene) |
| Applications | Rooting (IBA, NAA), fruit set, thinning, prevention of drop, tissue culture, weed control (2,4-D and others, by escaping homeostatic control) |

Main equations:

| Equation | Content |
|---|---|
| Eq. (13.1) $\frac{\mathrm{d}c}{\mathrm{d}t} = s + J_{\mathrm{in}} + r - (k_{\mathrm{deg}} + k_{\mathrm{conj}})c - J_{\mathrm{out}}$ | Steady state of hormone concentration; $t_{1/2} = \ln 2/k$ |
| Eq. (13.2) Hill equation | Dose-response, $\mathrm{EC}_{50}$ expresses sensitivity |
| Eq. (13.3) $\alpha \approx a m$ | Linear range of the Avena test |
| Eqs. (13.4), (13.5) | Undissociated fraction and ion trapping: IAAH 15% at pH 5.5; about 43-fold concentration at cytosolic pH 7.2 |
| Eq. (13.6) $\partial_t c = D\partial_x^2 c - v\partial_x c - kc$ | Advection–diffusion of polar transport; $\mathrm{Pe} = vL/D$ |
| Eq. (13.7) | Bell-shaped dose-response: promoting term × inhibiting term, $c_{\mathrm{opt}} = \sqrt{K_1K_2}$ |

## Questions

1. The cell wall pH falls from 5.5 to 5.0 (for example when the plasma membrane H⁺-ATPase is activated), while the cytosolic pH stays at 7.2. (a) By IAAH diffusion alone, how does the equilibrium concentration factor of the cell for auxin change? (b) If uptake takes place through AUX1 as $\mathrm{IAA^-}$ + 2 $\ce{H+}$, with a membrane potential of $-120\ \mathrm{mV}$ and a temperature of 25 °C, what is the maximum ratio of $\mathrm{IAA^-}$ concentration inside to outside at equilibrium? What does this result show?

   **Answer** (a) At pH 5.0, $1 + 10^{0.25} = 2.78$ and the factor is $283/2.78 \approx 102$, more than double that at pH 5.5 (about 43-fold). Acidification of the cell wall thus also increases auxin uptake, one link by which auxin transport and growth promote each other. (b) The symport carries a net charge of $+1$ (inward), and at equilibrium $\ln\dfrac{[\mathrm{IAA^-}]_{\mathrm{in}}}{[\mathrm{IAA^-}]_{\mathrm{out}}} = 2\ln\dfrac{[\ce{H+}]_{\mathrm{out}}}{[\ce{H+}]_{\mathrm{in}}} - \dfrac{F\Delta\psi}{RT}$, where $\Delta\psi = \psi_{\mathrm{in}} - \psi_{\mathrm{out}} = -0.120\ \mathrm{V}$. We have $2\times2.2\times\ln10 = 10.1$ (pH difference 2.2) and $F\Delta\psi/RT = -0.120\times96485/(8.314\times298) = -4.67$, so the total $\ln$ ratio is $14.8$ and the ratio is about $2.6\times10^{6}$. This is a thermodynamic upper limit that is far from reached in practice, because efflux and metabolism occur at the same time; but it shows that AUX1 can make the cell a powerful auxin "sink", far exceeding passive ion trapping in uptake, which is also why cells of the root epidermis expressing AUX1 can dominate the direction of auxin flow.

2. The speed of auxin transport is measured with the donor–receiver agar block method: for segments 5, 10, 15 and 20 mm long, radioactivity is first detected in the receiver block after 32, 61, 89 and 122 min. Find the transport speed. What result do you expect if the segment is inverted (donor at the morphological base)?

   **Answer** A linear regression of $t$ on $L$ gives a slope of about $5.95\ \mathrm{min\,mm^{-1}}$, that is, a speed $v \approx 1/5.95\ \mathrm{mm\,min^{-1}} = 10\ \mathrm{mm\,h^{-1}}$; the intercept is about $1.5\ \mathrm{min}$, close to 0 (the time for entering and leaving the segment is very short). Calculating from the slope rather than from $L/t$ of a single segment removes the error from the lag of entering and leaving the segment. When inverted, there is almost no radioactivity in the receiver block (only a little diffusion), because the direction of transport is determined by the polarity of the tissue (localization of PIN at the basal end of cells) and is independent of gravity and of the position of the donor.

3. A researcher claims that 2,4-D kills dicot weeds because "its activity is several thousand times higher than that of IAA". Using Eq. (13.1) and Section 13.6, point out the problem with this claim and design an experiment to test the "homeostatic control" explanation.

   **Answer** The affinity of 2,4-D for TIR1/AFB is not higher than that of IAA (often lower for TIR1); its effectiveness comes mainly from escaping homeostatic control: it is poorly conjugated by GH3 and poorly oxidized by DAO, so its removal rate constant $k$ in the tissue is far smaller than that of IAA, and the same amount taken up maintains a much higher and much longer-lasting effective concentration. Tests: treat leaves with radiolabeled IAA and 2,4-D and compare the decline of the free form over time (finding $k$ and half-life for both) and the formation of conjugates; or compare IAA toxicity in *gh3* multiple mutants (or GH3-overexpressing plants). If the homeostasis explanation is correct, mutants with reduced conjugation capacity should become as sensitive to exogenous IAA as they are to 2,4-D, and GH3-overexpressing plants should be more tolerant of IAA, while their sensitivity to 2,4-D should change less.

4. Explain why $10^{-6}\ \mathrm{mol\,L^{-1}}$ auxin can accelerate stem elongation and inhibit root elongation on the same plant. If the root experiment is repeated in the presence of the ethylene synthesis inhibitor AVG, do you expect the inhibition to disappear completely?

   **Answer** The dose-response curves of different organs differ by several orders of magnitude along the concentration axis: $10^{-6}\ \mathrm{mol\,L^{-1}}$ is below the optimum of the stem (about $10^{-5}$) and lies in the promoting range, but is far above the optimum of the root (about $10^{-10}$) and lies in the inhibiting range. Part of the inhibition comes from auxin-induced ethylene, and AVG, by inhibiting ACC synthase, reduces the inhibition but does not eliminate it completely: even when ethylene synthesis is blocked, auxin above $10^{-6}\ \mathrm{mol\,L^{-1}}$ still inhibits root growth, which shows that the root's own auxin response (signaling components, the response of cell elongation to auxin) also declines at supraoptimal concentrations.

5. (Open question) Using Eq. (13.6), explain why the elongation of the lower part of an oat coleoptile slows markedly within about 1 h after the tip is cut off, and why placing an agar block containing IAA on the cut surface after decapitation restores growth. If the elongation zone of the coleoptile lies 2–10 mm from the cut surface, estimate the time needed to restore growth.

   **Answer** Auxin in the elongation zone is maintained by continued synthesis in the tip and downward polar transport; after decapitation the supply is interrupted, free auxin in the elongation zone decays with the loss rate constant $k$ (a turnover time of the order of 1 h, Example 13.3.1), and growth slows accordingly. IAA from the agar block enters at the cut surface and moves downward at $v \approx 10\ \mathrm{mm\,h^{-1}}$, reaching the elongation zone at 2–10 mm in about $0.2$–$1\ \mathrm{h}$; adding the lag of the growth response to auxin (about 10–15 min), growth is expected to recover gradually within a dozen minutes to an hour after IAA is added, with the parts nearer the cut surface recovering first. Because diffusion broadens the pulse (width $\sim\sqrt{2Dt}$, about 2 mm after 1 h), the recovery is gradual and not a steep front.
