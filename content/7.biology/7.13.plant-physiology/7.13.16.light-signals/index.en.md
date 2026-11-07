---
title: "Light Signals: Photoreceptors and Photomorphogenesis"
description: "Skotomorphogenesis and photomorphogenesis; the plant photoreceptor families; discovery, structure, photoconversion and quantitative photostationary states of phytochrome (photoconversion cross section, relaxation time, two-band model); very low fluence, low-fluence and high-irradiance responses and the reciprocity law; the division of labor between phyA and phyB; nuclear import, PIFs and COP1–SPA; light-requiring seeds and de-etiolation; R:FR under canopies and shade avoidance; cryptochromes, phototropins and chloroplast movement; UVR8; the circadian clock and a three-loop oscillator model; thermomorphogenesis: thermal reversion of phyB and phase separation of ELF3."
source_hash: c0ed9fd1e714
---

Light has two meanings for a plant. It is the energy source of photosynthesis, and it is information about the environment. The first use requires enormous numbers of photons; the second requires very few. An *Arabidopsis* seed can be induced to germinate by red light equivalent to a few seconds of starlight, and the greening of an etiolated seedling is triggered by less than one second of red light in sunlight. Plants use several classes of photoreceptors to measure the presence, spectral composition (light quality), intensity, direction and duration of light, and on this basis decide when to germinate, how fast the stem elongates, which way the leaves face and when to flower. The molecules and photochemistry of the photoreceptors, namely the isomerization of the phytochrome chromophore, the flavin adduct of phototropin and the dimer dissociation of UVR8, were treated in [7.6.18](/7.6.18#sec-18.5.3); photosynthetic pigments and action spectra are in [7.13.7](/7.13.7). This chapter discusses light signaling from the standpoint of plant physiology: the manifestations of photomorphogenesis and the types of response, the quantitative description of phytochrome photostationary states, shade avoidance under canopies, the physiological functions of blue-light and ultraviolet photoreceptors, how light calibrates the endogenous clock, and how phytochrome also serves as a temperature sensor. The synthesis and action of hormones are covered in the preceding three chapters ([7.13.13](/7.13.13), [7.13.14](/7.13.14), [7.13.15](/7.13.15)), and the light signals of this chapter mostly change growth through them; the auxin mechanism of phototropism is in [7.13.19](/7.13.19), the dormancy physiology of light-requiring seeds in [7.13.20](/7.13.20), and photoperiod and flowering in [7.13.21](/7.13.21).

## 16.1. Light as a Developmental Signal

### 16.1.1. Skotomorphogenesis and Photomorphogenesis

When a seed germinates deep in the soil, the seedling must grow to the surface on its stored reserves. It then follows a "push upward" developmental program; as soon as it sees light, it switches to another program aimed at photosynthetic autotrophy.

**Definition 16.1.1 (Skotomorphogenesis and Photomorphogenesis)** The developmental program of a seedling in darkness is called **skotomorphogenesis**, and the resulting seedling is an etiolated seedling: the hypocotyl (or the mesocotyl or coleoptile of monocots) elongates rapidly, an apical hook forms at the tip, the cotyledons stay closed and unexpanded, plastids remain at the etioplast stage containing a prolamellar body and protochlorophyllide, and no chlorophyll is made. The regulation of plant growth, development and differentiation by light is called **photomorphogenesis**; the series of changes by which a seedling that emerges into light switches from skotomorphogenesis to photomorphogenesis is called **de-etiolation**: hypocotyl elongation is inhibited, the hook opens, the cotyledons unfold and enlarge, etioplasts develop into chloroplasts and chlorophyll is synthesized, anthocyanin accumulates, and the expression of a large number of nuclear and plastid genes changes.

Each program has adaptive significance. In darkness, investing the limited reserves in axis elongation gives the greatest chance of bringing the cotyledons above ground; the apical hook protects the shoot apical meristem and the cotyledons from abrasion by soil particles (the formation and maintenance of the hook are controlled by the asymmetric distribution of **ethylene** and **auxin**, [7.13.15](/7.13.15), [7.13.19](/7.13.19)). Once in light, continued elongation would only consume resources, and the seedling instead builds photosynthetic organs. Skotomorphogenesis is a "default program": Section 16.4 shows that at the molecular level a set of negative regulators constantly represses photomorphogenesis in darkness, and the role of light is to lift this repression.

The scope of photomorphogenesis is far greater than de-etiolation. Light regulates seed germination, stem elongation and branching, leaf expansion and orientation, the position of chloroplasts within cells, stomatal opening, phototropism, shade avoidance, the synthesis of anthocyanins and UV-screening compounds, flowering and senescence. **Photoperiodism**, the response of plants to day length, is also part of photomorphogenesis ([7.13.21](/7.13.21)).

### 16.1.2. A Low-Energy Signal

The energy scales of photomorphogenesis and photosynthesis differ enormously. Under full sunlight the **photosynthetically active radiation** at $400$–$700\,\mathrm{nm}$ is about $2000\,\mu\mathrm{mol\,m^{-2}\,s^{-1}}$; leaf photosynthesis approaches saturation only above several hundred $\mu\mathrm{mol\,m^{-2}\,s^{-1}}$ ([7.13.9](/7.13.9)). The phytochrome low-fluence response, in contrast, saturates at a total fluence of about $1000\,\mu\mathrm{mol\,m^{-2}}$, equivalent to less than $2\,\mathrm{s}$ of the red portion of full sunlight; the very low fluence response needs only $10^{-4}$–$10^{-1}\,\mu\mathrm{mol\,m^{-2}}$. This difference between signal responses and energy responses has two consequences. First, the photoreceptors must have a very high amplification capacity: one activated receptor molecule has to trigger a large number of downstream events. Second, what the photoreceptors measure is not the amount of energy but the spectral ratio, direction and timing, which are equally reliable in weak light.

### 16.1.3. The Photoreceptors of Plants

Angiosperms have at least five classes of photoreceptors (Table 16.1). The classical way to identify them is to compare the **action spectrum** of a response with the absorption spectra of candidate pigments ([7.13.7](/7.13.7#sec-7.2.2)): the action spectrum for promotion of lettuce seed germination by red light and its inhibition by far-red light points to a pigment that absorbs red and far-red light, namely **phytochrome**; the action spectrum for phototropic bending of the oat coleoptile has three peaks between $400$ and $500\,\mathrm{nm}$ (about $420$, $450$ and $475\,\mathrm{nm}$, the "three-finger" shape), which is characteristic of flavoproteins and corresponds to **phototropin** and **cryptochrome**. The molecular definitions and primary photochemistry of the receptors are given in [the definition of plant photoreceptors in 7.6.18](/7.6.18#sec-18.5.3).

| Receptor | *Arabidopsis* members | Chromophore | Light absorbed | Main functions |
|---|---|---|---|---|
| Phytochrome | phyA–phyE | Phytochromobilin (linear tetrapyrrole) | Red, far-red (also blue) | Germination, de-etiolation, shade avoidance, flowering, circadian clock, temperature sensing |
| Cryptochrome | cry1, cry2 (cry3 in organelles) | FAD (plus the antenna pigment MTHF) | Blue, UV-A | Inhibition of hypocotyl elongation, cotyledon expansion, flowering, circadian clock |
| Phototropin | phot1, phot2 | Two FMN (LOV domains) | Blue, UV-A | Phototropism, chloroplast movement, stomatal opening, leaf expansion and orientation |
| ZTL family | ZTL, FKF1, LKP2 | FMN (LOV domain) | Blue | Circadian clock (degradation of TOC1), photoperiod (degradation of CDF) |
| UVR8 | UVR8 | No added chromophore; tryptophan | UV-B | UV-B acclimation, flavonoid synthesis, inhibition of elongation |

The "Chromophore" column corrects two common statements. First, the chromophore of higher-plant phytochrome is phytochromobilin (P$\Phi$B), which is synthesized in the plastid from **heme** through biliverdin, exported to the cytoplasm and attached by a thioether bond to a cysteine of the apoprotein autocatalytically; some Chinese-language sources write "phycocyanobilin" instead, but that is the chromophore of the cyanobacterial phytochrome Cph1 and of some algae, and the tetrapyrrole side groups of the two differ. Second, not all "blue/UV-A receptors" use FAD: cryptochromes use **flavin adenine dinucleotide** as the chromophore and the pterin MTHF as an antenna, whereas phototropins and the ZTL family use **flavin mononucleotide** as the chromophore.

The division of the ultraviolet is also written in different ways. The convention of the International Commission on Illumination and ISO 21348 is UV-A $315$–$400\,\mathrm{nm}$, UV-B $280$–$315\,\mathrm{nm}$ and UV-C $100$–$280\,\mathrm{nm}$; the photobiology literature often gives UV-B as $280$–$320\,\mathrm{nm}$, and some Chinese textbooks use $280$–$330\,\mathrm{nm}$. UV-C is completely absorbed by stratospheric ozone and does not reach the ground; the UV-B that does reach the ground makes up only a small fraction of the energy of sunlight, but each photon carries enough energy to damage DNA and proteins.

## 16.2. Phytochrome: Photochemistry and Photostationary States

### 16.2.1. Red/Far-Red Reversibility

Phytochrome was inferred from physiological phenomena before it was extracted. In the early 1950s Borthwick, Hendricks and colleagues at the US Department of Agriculture research center in Beltsville used a spectrograph to study lettuce seed germination and found that red light promotes germination, that subsequent far-red light cancels the effect of red, and that the two can be alternated repeatedly (Table 16.2).

| Light treatment | Germination/% | Light treatment | Germination/% |
|---|---|---|---|
| Dark | Low | R–FR–R–FR | 6 |
| R | 70 | R–FR–R–FR–R | 76 |
| R–FR | 6 | R–FR–R–FR–R–FR | 7 |
| R–FR–R | 74 | | |

The rule is clear: germination depends only on whether the last light given was red (R) or far-red (FR). The simplest explanation is a pigment with two forms that can be photoconverted into each other: Pr, which absorbs red light, is converted into Pfr, which absorbs far-red light, and Pfr on absorbing far-red light returns to Pr; Pfr promotes germination. In 1959 Butler and colleagues, without knowing the molecular nature of the pigment, used this spectral property (after red light the absorbance at $660\,\mathrm{nm}$ falls and that at $730\,\mathrm{nm}$ rises, and after far-red light the reverse) to detect it in extracts of etiolated seedlings, and named it phytochrome. A purified phytochrome solution is blue-green because it absorbs red light.

Photoreversibility (the interconversion of Pr and Pfr by light) is the hallmark of phytochrome, and Table 16.3 lists some phytochrome-regulated responses that are red/far-red reversible. They are distributed across taxa from algae to angiosperms and across developmental stages:

| Response | Examples |
|---|---|
| Germination | Light-requiring seeds of lettuce, tobacco, *Arabidopsis* and others; fern spores |
| De-etiolation | Inhibition of hypocotyl and internode elongation, opening of the hook, expansion of cotyledons, chloroplast development |
| Pigment synthesis | Anthocyanins, chlorophyll precursors |
| Movement | Rotation of the chloroplast in *Mougeotia*; nyctinastic movements of *Mimosa* and others |
| Membrane potential | Excised mung bean root tips become positively charged in red light and stick to glass, and far-red light releases them (the Tanada effect, Tanada 1968) |
| Flowering | A red-light night break in the dark period inhibits flowering of short-day plants, and subsequent far-red light restores it ([7.13.21](/7.13.21)) |

### 16.2.2. Molecule and Photoconversion

Angiosperm phytochrome is a soluble protein of about $125\,\mathrm{kDa}$ that functions as a homodimer (about $250\,\mathrm{kDa}$). The N-terminal half of each subunit is the photosensory module, composed of the PAS, GAF and PHY domains: the chromophore is covalently attached to a cysteine of the GAF domain, GAF has bilin lyase activity, and the PHY domain stabilizes the Pfr conformation. The C-terminal half after the hinge contains two PAS-related domains (PRD, which mediate dimerization and, in phyB, also take part in nuclear import) and a histidine kinase-related domain (HKRD). Bacterial phytochromes are light-regulated histidine kinases belonging to **two-component systems**; plant phytochromes evolved from them but no longer have a functional histidine kinase domain.

After Pr absorbs red light, ring D of the chromophore undergoes Z→E isomerization about the C15=C16 double bond, accompanied by rotation about the C14–C15 single bond ([7.6.18](/7.6.18#sec-18.5.3)). The change in the chromophore is transmitted to the protein: according to the "toggle" model proposed from crystal structures of bacterial and plant phytochromes, the "tongue" region of the PHY domain surrounding the chromophore changes from a β hairpin into an α helix, pulling on the helical spine that connects the domains and changing the conformation of the dimer. Cryo-electron microscopy structures from the 2020s show that dark-state *Arabidopsis* phyB is a head-to-tail, asymmetric dimer, and that the activated phyB dimer binds the APB motif of only one PIF6 molecule (published in *Cell* in 2024). These structural details are still under study, but the physiological conclusion is firm: Pfr is the physiologically active form. In most responses studied, the magnitude of the response is quantitatively related to the amount of Pfr produced by light, and not to the loss of Pr.

### 16.2.3. Quantitative Description of the Photostationary State

The absorption spectra of Pr and Pfr overlap considerably: Pfr also absorbs appreciably in the red, and Pr absorbs weakly in the far-red (Figure 1A). Hence in red light part of the Pfr formed is converted back to Pr by red light, and in far-red light a little Pr is always converted to Pfr. Under continuous irradiation the rates of the photoreactions in the two directions become equal and the system reaches a **photostationary state** (general definition in [6.3.17](/6.3.17)). Let $q(\lambda)$ be the spectral photon flux, and let Pfr revert thermally to Pr in darkness with rate constant $k_{\mathrm{r}}$:

$$
\frac{\mathrm{d}[\mathrm{Pfr}]}{\mathrm{d}t} = k_1[\mathrm{Pr}] - k_2[\mathrm{Pfr}] - k_{\mathrm{r}}[\mathrm{Pfr}],
\tag{16.1}
$$

where the rate constants of photoconversion are given by spectral integrals of the photoconversion cross section $\sigma$:

$$
k_1 = \int q(\lambda)\,\sigma_{\mathrm{r}}(\lambda)\,\mathrm{d}\lambda,\quad
k_2 = \int q(\lambda)\,\sigma_{\mathrm{fr}}(\lambda)\,\mathrm{d}\lambda,\quad
\sigma(\lambda) = \ln 10\;\varepsilon(\lambda)\,\Phi .
\tag{16.2}
$$

Here $\varepsilon$ is the **molar absorption coefficient** and $\Phi$ is the **quantum yield** of photoconversion (about $0.15$ for Pr→Pfr and about $0.07$ for Pfr→Pr, approximate in vitro values). In light the thermal reversion can usually be neglected ($k_{\mathrm{r}} \ll k_1 + k_2$); with $\mathrm{P_{tot}} = [\mathrm{Pr}] + [\mathrm{Pfr}]$, the Pfr fraction at steady state is

$$
\varphi = \frac{[\mathrm{Pfr}]}{\mathrm{P_{tot}}} = \frac{k_1}{k_1 + k_2},
\tag{16.3}
$$

which Chinese textbooks call the photoequilibrium value. Starting from darkness (all Pr), the Pfr fraction approaches $\varphi$ as $\varphi\bigl(1 - \mathrm{e}^{-t/\tau}\bigr)$ with relaxation time $\tau = 1/(k_1 + k_2)$. In monochromatic light the ratio $k_1/k_2 = \varepsilon_{\mathrm{r}}\Phi_{\mathrm{r}}/(\varepsilon_{\mathrm{fr}}\Phi_{\mathrm{fr}})$ is independent of intensity, so $\varphi$ depends only on wavelength: intensity determines only how fast the photostationary state is reached, and light quality determines what $\varphi$ is.

![Absorption spectra of the two forms of phytochrome and the photostationary state. A: Schematic absorption spectra of Pr (peak at 666 nm, shoulder at 610 nm, weaker band at 380 nm) and Pfr (peak at 730 nm, absorption near 670 nm and 400 nm), constructed from band positions in the literature, with band strengths adjusted so that the model reproduces the measured photostationary states; the shaded bands are the commonly used red (R, 655–665 nm) and far-red (FR, 725–735 nm) bands. B: The photostationary state in monochromatic light, $\varphi(\lambda) = \varepsilon_{\mathrm{r}}\Phi_{\mathrm{r}}/(\varepsilon_{\mathrm{r}}\Phi_{\mathrm{r}} + \varepsilon_{\mathrm{fr}}\Phi_{\mathrm{fr}})$ (quantum yields 0.15 and 0.07). In red light $\varphi \approx 0.87$, in far-red light about 0.025, with a steep drop between 700 and 720 nm; in blue light it is about 0.3–0.6. The dashed line is $\varphi \approx 0.6$ for sunlight](./plots/phytochrome-spectra.py)

The measured photostationary state depends on the spectral width of the light source: in saturating red light $\varphi$ is about $0.85$–$0.88$, and in broad-band far-red light about $0.02$–$0.03$, so Pfr cannot be eliminated completely, which determines why the very low fluence response of Section 16.3 cannot be reversed by far-red light. In sunlight $\varphi \approx 0.6$; under canopies it falls as the proportion of far-red light increases (Section 16.6).

**Example 16.2.1** Photoconversion cross section and the time to reach the photostationary state. The molar absorption coefficient of phytochrome Pr at $660\,\mathrm{nm}$ is about $1.2\times10^{5}\,\mathrm{L\,mol^{-1}\,cm^{-1}}$. Since $1\,\mathrm{L\,mol^{-1}\,cm^{-1}} = 0.1\,\mathrm{m^2\,mol^{-1}}$,

$$
\sigma_{\mathrm{r}}(660) = 2.303 \times 1.2\times10^{4}\,\mathrm{m^2\,mol^{-1}} \times 0.15 \approx 4.1\times10^{3}\,\mathrm{m^2\,mol^{-1}} = 4.1\times10^{-3}\,\mathrm{m^2\,\mu mol^{-1}} .
$$

From $\varphi(660) = 0.87$ we obtain $\sigma_{\mathrm{fr}}(660) = \sigma_{\mathrm{r}}(1-\varphi)/\varphi \approx 6.1\times10^{-4}\,\mathrm{m^2\,\mu mol^{-1}}$. In $660\,\mathrm{nm}$ red light of $10\,\mu\mathrm{mol\,m^{-2}\,s^{-1}}$, $k_1 + k_2 = (4.1 + 0.61)\times10^{-3} \times 10 \approx 0.047\,\mathrm{s^{-1}}$ and $\tau \approx 21\,\mathrm{s}$: one minute of irradiation essentially reaches the photostationary state. Integrating the model spectra of Figure 1 over sunlight gives $k_1 + k_2 \approx 2.0\times10^{-3}\,\mathrm{s^{-1}}$ per $1\,\mu\mathrm{mol\,m^{-2}\,s^{-1}}$ of photosynthetically active radiation; in full sunlight ($2000\,\mu\mathrm{mol\,m^{-2}\,s^{-1}}$) $\tau \approx 0.25\,\mathrm{s}$, so the phytochrome pool follows changes in light quality almost instantaneously; at dusk, when the intensity falls below $1\,\mu\mathrm{mol\,m^{-2}\,s^{-1}}$, $\tau$ rises to more than ten minutes, and thermal reversion begins to compete with the photoreactions (Section 16.9). In tissues, screening by chlorophyll and other pigments means that fewer photons reach phytochrome than are incident, especially in green tissue.

### 16.2.4. Dark Reversion and Degradation

In darkness Pfr has two fates: thermal reversion (dark reversion) to Pr, and degradation of the protein. Both reduce Pfr and can be combined into first-order kinetics,

$$
[\mathrm{Pfr}](t) = [\mathrm{Pfr}](0)\,\mathrm{e}^{-(k_{\mathrm{r}} + k_{\mathrm{d}})t},
\tag{16.4}
$$

but their consequences differ: reversion preserves the protein, whereas degradation reduces the total amount of phytochrome. Different phytochromes differ greatly. PhyA is synthesized and accumulates abundantly in the dark and is the most abundant phytochrome in etiolated seedlings; its Pfr form is ubiquitinated and rapidly degraded by the **proteasome**, and transcription of *PHYA* is also repressed by light, so within a few hours after a seedling sees light the amount of phyA falls by one to two orders of magnitude. PhyB–phyE are stable in light, are synthesized in both light and darkness, and make up the bulk of phytochrome in green plants. Thermal reversion of phyB is slow and depends on the state of the dimer: dimers in which both subunits are Pfr (Pfr:Pfr) revert slowly, and Pfr:Pr heterodimers revert quickly; the rate of reversion increases with temperature, which is the basis of temperature sensing by phyB in Section 16.9.

The total amount of phytochrome also varies among tissues: it is higher in meristems (shoot apex and root tip) and much higher in etiolated than in green seedlings; within cells, phytochrome in darkness is in the cytoplasm, and in light most of it enters the nucleus (16.4.1).

Early on, the disappearance of Pfr in the dark was used to explain how plants measure night length (the "hourglass" hypothesis): the Pfr formed in light gradually declines in the dark, and when it falls to a threshold the flowering stimulus is initiated or removed. For example, if the Pfr fraction decays from $0.6$ at dusk with $k = 0.5\,\mathrm{h^{-1}}$, falling to $0.1$ takes only $\ln 6/0.5 \approx 3.6\,\mathrm{h}$, far shorter than the critical night length of about $9$–$15\,\mathrm{h}$ of many short-day plants; moreover, thermal reversion depends on temperature, whereas the critical night length is insensitive to temperature. It is now believed that night length is measured mainly by the circadian clock, and phytochrome only supplies it with light signals (Section 16.8, [7.13.21](/7.13.21)).

### 16.2.5. Division of Labor in the Phytochrome Family

*Arabidopsis* has five phytochrome genes, *PHYA*–*PHYE*, rice has three (*PHYA*, *PHYB*, *PHYC*), and poplar has only two classes. According to stability in light, phytochromes are often divided into two types:

| Property | Type I: phyA | Type II: phyB (and phyC–E) |
|---|---|---|
| Stability in light | Pfr is rapidly degraded; light represses its transcription | Stable |
| Abundance | Highest in etiolated seedlings | Predominant in green plants |
| Nuclear import | Requires FHY1/FHL as carriers; induced by red, far-red and weak broad-band light | Depends on its own PRD region, exposed in the Pfr conformation; induced only by red light and reversed by far-red |
| Main responses | Very low fluence responses; high-irradiance response in continuous far-red | Low-fluence responses (reversible seed germination); de-etiolation in continuous red or white light; shade avoidance |
| Mutant phenotype | Hypocotyl elongation in continuous far-red (as in darkness); seeds cannot be induced to germinate by millisecond light pulses | Long hypocotyls in white and red light (*hy3* is *phyB*), little chlorophyll, resembling plants grown under a canopy |

This division of labor is consistent with the photochemistry and the nuclear import properties of the two. How can phyA perceive far-red light? In far-red light $\varphi$ is only $0.02$–$0.03$, yet each phyA molecule keeps cycling between Pr and Pfr; phyA depends on FHY1 for nuclear import, FHY1 binds only Pfr and dissociates from phyA after import, so a continuing cycle of photoconversion favors the steady transport of phyA into the nucleus; at the same time, the low $\varphi$ keeps Pfr from being degraded extensively. In red light phyA is rapidly degraded as Pfr, and its action is short-lived. PhyD and phyE are structurally close to phyB but not fully redundant with it, and take part in the regulation of petiole and internode elongation and flowering time.

## 16.3. Three Types of Phytochrome Responses

### 16.3.1. Fluence and the Reciprocity Law

Describing a light signal requires distinguishing two quantities. The photon flux density (photon fluence rate) is the number of photons per unit time and unit area, in $\mu\mathrm{mol\,m^{-2}\,s^{-1}}$; the fluence is the total number of photons per unit area over a period of time, that is, the time integral of the photon flux density, in $\mu\mathrm{mol\,m^{-2}}$.

**Definition 16.3.1 (Reciprocity Law)** If the magnitude of a photoreaction depends only on the fluence $F = I t$, and not separately on the photon flux density $I$ and the irradiation time $t$, that is,

$$
R = f(I\,t),
\tag{16.5}
$$
then the reaction is said to obey the **reciprocity law** (the Bunsen–Roscoe law): an increase in intensity can be compensated by a corresponding decrease in irradiation time, and vice versa.

The reciprocity law holds only when photon absorption by the receptor is the rate-limiting step of the whole process. If the irradiation time is longer than the time scale of some step between the receptor and the downstream events, or if a downstream step saturates first, reciprocity fails.

Between the activation of phytochrome and the visible morphological response there is a lag, ranging from several minutes (inhibition of the stem elongation rate by red light in *Chenopodium* and *Arabidopsis*) to several weeks (flowering). Another time scale is the "escape time": the effect of red light can be reversed by far-red light only for a certain period, after which the response "escapes" from photoreversible control. If the morphological response is viewed as a chain of biochemical reactions, the first few steps can still be reversed when Pfr is removed, and beyond a certain step the process proceeds irreversibly to the end; the escape time is the time Pfr needs to complete its primary action, and it ranges among responses from less than a minute to several hours.

### 16.3.2. The Three Classes of Response

According to the fluence required, phytochrome responses fall into three classes (Figure 2).

**Definition 16.3.2 (Types of Phytochrome Responses)** A response induced by fluences in the range $10^{-4}$–$10^{-1}\,\mu\mathrm{mol\,m^{-2}}$ and saturated at about $0.05\,\mu\mathrm{mol\,m^{-2}}$ is called a **very low fluence response** (VLFR); a response that begins at a fluence of about $1\,\mu\mathrm{mol\,m^{-2}}$, saturates at about $1000\,\mu\mathrm{mol\,m^{-2}}$ and is red/far-red reversible is called a **low-fluence response** (LFR); a response that requires prolonged or continuous, stronger illumination, whose magnitude increases with photon flux density until saturation, and that does not obey the reciprocity law is called a **high-irradiance response** (HIR).

Strictly speaking, the first two classes are defined by fluence and only the third by photon flux density (irradiance), which is why their English names differ: very low fluence response, low-fluence response, high-irradiance response. The three classes compare as follows:

| Property | Very low fluence response | Low-fluence response | High-irradiance response |
|---|---|---|---|
| Fluence or intensity | $10^{-4}$–$10^{-1}\,\mu\mathrm{mol\,m^{-2}}$ | $1$–$1000\,\mu\mathrm{mol\,m^{-2}}$ | Continuous irradiation; saturating fluence more than 100 times that of the LFR |
| Pfr fraction required | $< 0.02\,\%$ | A few percent up to the photostationary state | Not determined by a single pulse |
| Reciprocity law | Obeyed | Obeyed (when unsaturated) | Not obeyed |
| Red/far-red reversible | No | Yes | No |
| Action spectrum peak | Red (similar to the LFR) | Red $660\,\mathrm{nm}$ promotes, far-red $720\,\mathrm{nm}$ reverses | Far-red (phyA), red (phyB) and blue |
| Main receptor | phyA | phyB | phyA (FR-HIR), phyB (R-HIR) |
| Examples | Germination of *Arabidopsis* seeds in $0.001$–$0.1\,\mu\mathrm{mol\,m^{-2}}$ red light; promotion of elongation of etiolated oat coleoptiles and inhibition of mesocotyl elongation | Lettuce seed germination; inhibition of hypocotyl elongation; leaf movements; chloroplast rotation in *Mougeotia* | Synthesis of anthocyanins and other flavonoids in dicot seedlings; inhibition of hypocotyl elongation in mustard, lettuce and petunia; flowering induction in henbane; opening of the plumular hook in lettuce; cotyledon enlargement in mustard; ethylene production in sorghum |

Why can the very low fluence response not be reversed by far-red light? The answer lies in the photostationary state: the light that induces it converts less than $0.02\,\%$ of phytochrome to Pfr, whereas after far-red irradiation $2$–$3\,\%$ of phytochrome is still present as Pfr, more than 100 times what the VLFR requires. Far-red light cannot lower Pfr below the VLFR threshold, so it cannot reverse the response; the action spectrum of the VLFR is similar to that of the LFR and *phyA* mutants lose the VLFR, two facts that show it too is a phytochrome response.

The same response can appear as an LFR or an HIR depending on the light history. Anthocyanin synthesis in white mustard (*Sinapis alba*) seedlings behaves as a typical LFR at low fluence: the action spectrum has only a red peak, the response is reversible by far-red light and obeys reciprocity; if etiolated seedlings are given several hours of continuous strong light, the action spectrum shows far-red and blue peaks, the response is no longer reversible, and it is proportional to photon flux density. Many LFRs in de-etiolation fall into this category.

**Example 16.3.1** Estimating the Pfr fraction required by the three classes of response with the cross sections of Example 16.2.1. Starting from all Pr and giving a $660\,\mathrm{nm}$ pulse of fluence $F$,

$$
\frac{[\mathrm{Pfr}]}{\mathrm{P_{tot}}} = \varphi\left(1 - \mathrm{e}^{-(\sigma_{\mathrm{r}} + \sigma_{\mathrm{fr}})F}\right) \approx \sigma_{\mathrm{r}} F \quad (F \text{ small}).
\tag{16.6}
$$

The VLFR threshold $F = 10^{-4}\,\mu\mathrm{mol\,m^{-2}}$ produces only $4.1\times10^{-3} \times 10^{-4} \approx 4\times10^{-7}$, that is, $4\times10^{-5}\,\%$ Pfr; the $0.05\,\mu\mathrm{mol\,m^{-2}}$ at which the VLFR saturates produces about $2\times10^{-4}$, that is, $0.02\,\%$, in agreement with the measured value. The starting point of the LFR, $1\,\mu\mathrm{mol\,m^{-2}}$, produces about $0.4\,\%$; at $F = 1000\,\mu\mathrm{mol\,m^{-2}}$, $(\sigma_{\mathrm{r}} + \sigma_{\mathrm{fr}})F \approx 4.7$ and the Pfr fraction is $0.87 \times (1 - \mathrm{e}^{-4.7}) \approx 0.86$, already at the photostationary state, so the LFR saturates here. If an etiolated cell contains $10^{5}$ phytochrome molecules, saturation of the VLFR corresponds to the activation of only a few dozen molecules, which shows how strong the downstream amplification is.

![Fluence–response relations of the three classes of phytochrome responses (schematic calculated from the photoconversion model). A: The Pfr fraction after a 660 nm red pulse given from darkness, rising linearly with fluence according to Eq. (16.6) and reaching the photostationary state of 87% at about 1000 μmol m⁻²; the dashed line marks the 0.02% needed to saturate the VLFR, and the dotted line the 2.5% remaining after far-red light. B: Response curves of the VLFR (hyperbolic in the Pfr fraction, half-saturated at 0.002%) and the LFR (Hill coefficient 2, half-saturated at 12%); the shaded regions are the typical fluence ranges of the two classes; open circles show the result of far-red light given after red light: far-red lowers Pfr to 2.5%, the LFR returns to near zero, and the VLFR remains saturated. C: The HIR under continuous irradiation at three photon flux densities, with accumulated fluence on the horizontal axis: the higher the intensity, the higher the plateau of the response, so at the same fluence the response differs among intensities, that is, reciprocity is not obeyed. Response parameters are illustrative](./plots/fluence-response.py)

What does the very low fluence response mean in nature? Weed seeds buried in soil are extremely sensitive to light, and less than one second of sunlight when they are turned up to the surface during tillage is enough to induce germination; tilling at night or under shade can markedly reduce the emergence of weeds in fields (Scopel et al., 1991).

## 16.4. Phytochrome Signal Transduction

### 16.4.1. Nuclear Import and Fast Cytoplasmic Responses

Fusions of phytochrome with green fluorescent protein show directly that in darkness phyA–GFP and phyB–GFP are both in the cytoplasm; after illumination they enter the nucleus and form speckles called "photobodies", whose number and size correlate with the strength of the light response. Nuclear import is a prerequisite for phytochrome to control transcription and is also a regulatory point: the PRD region of phyB can act as a **nuclear localization signal**, masked in the Pr conformation and exposed in the Pfr conformation; phyA has no such signal and is carried into the nucleus by FHY1 and its homolog FHL. A study published in *Cell* in 2023 showed that when an emerging seedling sees light, red-light-activated phyB causes a rapid rise in cytosolic $\ce{Ca^2+}$ concentration, and the calcium-dependent protein kinases CPK6/CPK12 recognize the activated phyB and phosphorylate its Ser80 and Ser106, converting it into a form that can enter the nucleus rapidly.

A small fraction of phytochrome remains in the cytoplasm and mediates fast responses on the time scale of seconds: red light causes hyperpolarization of oat coleoptile and root cells within seconds and alters ion fluxes; the Tanada effect also belongs here. These responses underlie the old "membrane hypothesis" of phytochrome action, whereas regulation of transcription after nuclear import underlies the "gene regulation hypothesis"; the two are not contradictory and correspond to two phytochrome pools, in the cytoplasm and in the nucleus. In *Mougeotia*, red light controls the rotation of the chloroplast, and the receptor is a fusion of phytochrome and phototropin (neochrome), which is also found in the fern *Adiantum*, an evolutionary example of "handing a blue-light response over to a red-light receptor".

### 16.4.2. PIFs: Transcription Factors That Maintain Skotomorphogenesis in the Dark

**Definition 16.4.1 (Phytochrome-Interacting Factor)** A class of **basic helix–loop–helix** transcription factors that bind specifically to the Pfr form of phytochrome and act mainly as negative regulators of photomorphogenesis is called **phytochrome-interacting factors** (PIFs). *Arabidopsis* has PIF1 and PIF3–PIF8 among its members.

PIFs accumulate in darkness, activate genes expressed in the dark (including the elongation-promoting auxin biosynthesis gene *YUCCA8*) and repress some light-induced genes, thereby maintaining skotomorphogenesis. The *Arabidopsis* quadruple mutant *pif1 pif3 pif4 pif5* (*pifq*) shows photomorphogenesis even in darkness: the hypocotyl is short and the cotyledons are open. In light, Pfr binds PIFs and promotes their phosphorylation; the phosphorylated PIFs are ubiquitinated and degraded through the **ubiquitin–proteasome system** within minutes to an hour, and the phyB bound to the PIFs is partly degraded with them. Different PIFs favor different processes: PIF1 inhibits seed germination and chlorophyll synthesis, PIF4, PIF5 and PIF7 promote hypocotyl elongation and shade avoidance, and PIF4 is also the hub of thermomorphogenesis (Section 16.9). PIFs are also a meeting point of hormone and light signals: the DELLA proteins of **gibberellin** signaling bind PIFs and inhibit their activity, and BZR1, the transcription factor of **brassinosteroid** signaling, acts together with PIF4 ([7.13.14](/7.13.14), [7.13.15](/7.13.15)).

### 16.4.3. COP1–SPA: An E3 Ubiquitin Ligase in the Dark

Several laboratories independently screened for *Arabidopsis* mutants that show light phenotypes in the dark and obtained three groups of genes, *COP* (CONSTITUTIVE PHOTOMORPHOGENIC), *DET* (DE-ETIOLATED) and *FUS* (FUSCA, named for the dark-red color of the anthocyanin accumulated by the seedlings), collectively called COP/DET/FUS. They encode complexes involved in ubiquitination and proteasomal degradation, such as the COP1–SPA complex and the COP9 signalosome (CSN). COP1 is a component of an E3 ubiquitin ligase and forms a complex with SPA (SUPPRESSOR OF PHYA) proteins. In darkness COP1, assisted by the CSN, is located in the nucleus and ubiquitinates positive regulators of photomorphogenesis, including the bZIP (**leucine zipper**) transcription factors HY5 and HYH, the bHLH protein HFR1, the MYB transcription factor LAF1, and phyA itself; they are then degraded by the proteasome, and skotomorphogenesis becomes the default program.

Light relieves the action of COP1 in two ways. The fast way is direct inhibition of COP1–SPA by photoreceptors: activated phytochromes and cryptochromes bind SPA and cause the COP1–SPA complex to dissociate or be inactivated. The slow way is the export of COP1 from the nucleus after prolonged light (more than 24 h). Once COP1 is inactivated, transcription factors such as HY5 accumulate, bind elements such as the G-box in the promoters of light-regulated genes, activate photomorphogenic genes for chloroplast development and pigment synthesis, and inhibit elongation. COP1 also degrades the flowering regulators CONSTANS (CO) and GIGANTEA (GI), so the same ligase connects light signals to the photoperiod pathway ([7.13.21](/7.13.21)).

This logic is the same as in plant hormone signaling: the **ubiquitin–proteasome system** degrades repressors, and the role of the signal is "derepression" ([7.1.15](/7.1.15#sec-15.5.2), [7.13.13](/7.13.13)). The difference is that hormones mostly promote the degradation of repressors, whereas light both promotes the degradation of a repressor (PIF) and inhibits the ligase that degrades an activator (HY5).

![SBGN activity flow diagram (simplified) of the regulation of photomorphogenesis by light and temperature signals. In darkness PIFs promote the synthesis of and signaling by auxin and brassinosteroids, causing hypocotyl elongation, and COP1–SPA causes degradation of HY5. PhyB-Pfr produced by red light and phyA cycling in far-red light promote the degradation of PIFs and inhibit COP1–SPA; far-red light returns phyB to Pr; blue-light-activated cryptochromes bind SPA and inhibit COP1; UV-B causes UVR8 to dissociate into monomers, and the monomers bind COP1, which then promotes the expression of HY5 instead (dashed). HY5 promotes photomorphogenesis and inhibits elongation. Warmth both accelerates thermal reversion of phyB-Pfr and inactivates the evening complex (containing ELF3), thereby relieving repression of PIF4. Blunt-ended lines are inhibition and open arrowheads are promotion](./plots/light-signaling.py)

### 16.4.4. From Receptor to Phenotype

Phytochrome changes transcription within minutes after nuclear entry (as soon as about $5\,\mathrm{min}$). Microarray and transcriptome analyses show that when etiolated seedlings are transferred to light, the expression of thousands of genes changes, forming a transcriptional cascade: the earliest induced primary response genes mostly encode transcription factors, and their expression does not require new protein synthesis; late secondary response genes do. The promoters of light-regulated genes share no common element but are assembled from many modules, which allows different photoreceptors and different tissues to regulate their own sets of genes separately.

Hormones are the main intermediaries between light signals and growth. In light, the degradation of PIFs reduces the synthesis of and signaling by auxin and brassinosteroids; after etiolated seedlings see light, the content of active gibberellin falls (expression of *GA20ox* and *GA3ox* decreases and that of *GA2ox* rises) and DELLA accumulates; blue light also reduces the contents of free auxin, gibberellin and cytokinin. These changes together inhibit hypocotyl elongation. The opening of the apical hook likewise involves changes in the distribution of ethylene and auxin.

## 16.5. Light-Requiring Seeds and De-etiolation of Seedlings

### 16.5.1. Light-Requiring Seeds

Many small seeds germinate only in light, such as some varieties of lettuce, tobacco, *Arabidopsis* and many weeds; large seeds (such as those of legumes) have abundant reserves, sufficient to support a seedling growing a long way in darkness, and usually do not need light. The significance of light-requiring germination is that seedlings of small seeds can emerge only from very shallow soil layers, and light indicates that a seed lies near the surface; light under a canopy is rich in far-red and has a low $\varphi$, so light-requiring seeds remain dormant under vegetation and wait for gaps or tillage to bring direct light rich in red.

Germination of light-requiring seeds is a typical phyB-mediated low-fluence response (the *Arabidopsis* *phyB* mutant cannot be induced to germinate by low-fluence red light), and buried seeds can also germinate through the very low fluence response of phyA. Mechanistically, phyB-Pfr after nuclear entry promotes the degradation of PIF1 (also called PIL5); in darkness PIF1 represses the gibberellin biosynthesis genes *GA3ox1* and *GA3ox2* and promotes the expression of *GA2ox2* and the abscisic acid biosynthesis genes, so its degradation increases active gibberellin and decreases **abscisic acid** in the embryo, breaking dormancy (the physiology of **seed dormancy** and **seed germination** is in [7.13.20](/7.13.20)). HFR1 is a positive regulator in this pathway; it binds PIF1 to form a heterodimer that cannot bind DNA.

### 16.5.2. Time Course of De-etiolation

De-etiolation is a relay among several photoreceptors. High-resolution growth measurements divide the blue-light inhibition of hypocotyl elongation into several phases (Parks et al., 2001): etiolated *Arabidopsis* seedlings elongate in darkness at about $0.25\,\mathrm{mm\,h^{-1}}$; after blue light is given, the growth rate begins to fall after about $30\,\mathrm{s}$, approaches zero within $30\,\mathrm{min}$, and then stays at a very low rate for days. The *phot1* mutant shows no change in rate during the first $30\,\mathrm{min}$, indicating that the earliest inhibition is mediated by phototropin phot1; the sustained inhibition afterward is maintained mainly by cry1, with a smaller contribution from cry2, and phyA takes part in the early phase. For this reason the *cry1* mutant has long hypocotyls in blue light, whereas the final hypocotyl length of the *phot1* mutant is close to that of the wild type. Before the blue-light inhibition of elongation, hypocotyl cells first undergo membrane depolarization, caused by the opening of anion channels and efflux of $\ce{Cl-}$; the anion channel blocker NPPB abolishes the depolarization and also weakens the inhibition of elongation by blue light.

The effects of blue and red light can be separated experimentally: adding weak blue light to a strong yellow-light background (which establishes a defined $\varphi$) hardly changes $\varphi$ yet reduces the elongation rate of lettuce seedling hypocotyls by more than half, showing a specific blue-light response independent of phytochrome; the time courses also differ: the change in elongation rate mediated by phytochrome appears only after $10$–$90\,\mathrm{min}$, whereas the lag of the blue-light response is less than $1\,\mathrm{min}$.

Chloroplast development has two phases: phytochrome and cryptochrome initiate nuclear gene expression, protochlorophyllide is reduced in light by the light-dependent protochlorophyllide oxidoreductase ([7.13.7](/7.13.7#sec-7.6.1)), thylakoids appear and chlorophyll accumulates; subsequently nuclear and plastid genes are expressed in a coordinated manner and the chloroplast develops fully. Phytochrome also regulates the activity or amount of many enzymes, including Rubisco, PEP carboxylase, nitrate reductase and amylase, shifting metabolism toward photosynthetic autotrophy.

## 16.6. Shade Avoidance

### 16.6.1. Light under the Canopy

A plant canopy acts as a filter. Leaves strongly absorb blue and red light (absorptance about $0.9$), absorb green light somewhat less, and are almost transparent to far-red light above $700\,\mathrm{nm}$, which is mainly transmitted and reflected. Under a canopy the light is therefore not only weak but relatively enriched in far-red. It is commonly described by the ratio of the photon fluxes of red and far-red light, R:FR (the ratio of $655$–$665\,\mathrm{nm}$ to $725$–$735\,\mathrm{nm}$): about $1.15$–$1.2$ in sunlight, and it can fall to $0.05$–$0.2$ in dense forest. Before direct shading occurs, far-red light reflected by neighboring plants already lowers R:FR, so a plant can "foresee" the presence of competitors; shading also lowers the blue:green ratio and UV-B.

How is R:FR converted to $\varphi$? Considering only the red and far-red bands, with photon flux densities $q_{\mathrm{R}}$ and $q_{\mathrm{FR}}$ and $\zeta = q_{\mathrm{R}}/q_{\mathrm{FR}}$, Eqs. (16.2)–(16.3) give

$$
\varphi(\zeta) = \frac{\sigma_{\mathrm{r}}^{\mathrm{R}}\zeta + \sigma_{\mathrm{r}}^{\mathrm{FR}}}{\left(\sigma_{\mathrm{r}}^{\mathrm{R}} + \sigma_{\mathrm{fr}}^{\mathrm{R}}\right)\zeta + \sigma_{\mathrm{r}}^{\mathrm{FR}} + \sigma_{\mathrm{fr}}^{\mathrm{FR}}},
\tag{16.7}
$$

where the superscripts denote the band. This is a hyperbola: as $\zeta \to \infty$, $\varphi$ approaches the red-light limit $0.87$, and as $\zeta \to 0$ it approaches the far-red limit $0.025$; in the range of R:FR below 1, $\varphi$ is most sensitive to R:FR, which is precisely the light environment under canopies.

**Example 16.6.1** Take the cross sections of the model spectra in the two bands (in units of $10^{-3}\,\mathrm{m^2\,\mu mol^{-1}}$): $\sigma_{\mathrm{r}}^{\mathrm{R}} = 4.1$, $\sigma_{\mathrm{fr}}^{\mathrm{R}} = 0.61$, $\sigma_{\mathrm{r}}^{\mathrm{FR}} = 0.053$, $\sigma_{\mathrm{fr}}^{\mathrm{FR}} = 2.07$. For sunlight, $\zeta = 1.15$:

$$
\varphi = \frac{4.1 \times 1.15 + 0.053}{4.71 \times 1.15 + 2.12} = \frac{4.77}{7.54} \approx 0.63 ;
$$

under a canopy with $\zeta = 0.2$: $\varphi = (0.82 + 0.053)/(0.94 + 2.12) \approx 0.29$; for $\zeta = 0.1$, $\varphi \approx 0.18$. A decrease of R:FR to $1/6$ of its value lowers $\varphi$ by more than half. A calculation with the full spectrum (Figure 3B) gives similar results.

![The light environment of shade avoidance and $\varphi$ (model calculation). A: Spectra of sunlight (R:FR = 1.15) attenuated by canopies with leaf area index of 1, 3 and 6, according to the Beer–Lambert law $I = I_0\exp(-0.5\,\mathrm{LAI}\,a(\lambda))$, with leaf absorptance $a$ of about 0.9 in blue and red, about 0.75 in green and about 0.1 in far-red (scattering neglected); a steep step forms between red and far-red. B: The relation between $\varphi$ and R:FR calculated from the full spectra (curve), with dots corresponding to the four lights in A; as R:FR falls from 1.15 to 0.11, $\varphi$ falls from 0.60 to 0.29. C: The internode elongation rate decreases linearly with $\varphi$; plants of open habitats (such as *Chenopodium*) have a large slope and shade-tolerant understory plants a small slope (schematic after the experiments of Morgan and Smith; values are illustrative)](./plots/shade-avoidance.py)

### 16.6.2. The Shade Avoidance Syndrome

**Definition 16.6.1 (Shade Avoidance)** The set of responses in which a plant, on sensing the low R:FR caused by neighboring plants (and the reductions in blue light and UV-B), accelerates the elongation of stems, hypocotyls and petioles, raises its leaves, reduces branching, strengthens **apical dominance** and flowers earlier is called **shade avoidance**.

Every manifestation of shade avoidance serves the purpose of "growing above the neighbors": elongation of internodes and petioles lifts the leaves higher, upward leaf movement (hyponasty) avoids the shade of lower leaves, resources are diverted from branches and roots to the main stem, and leaves become thinner and contain less chlorophyll; if the shade cannot be escaped, earlier flowering can leave seeds before the plant is suppressed. The price is a thin, weak stem and reduced resistance to pests and pathogens (jasmonate defenses are suppressed).

The dependence of elongation on light quality can be described quantitatively. In the 1970s Morgan and Smith changed $\varphi$ by adding supplementary far-red light while keeping photosynthetically active radiation constant, and found that the internode elongation rate of plants of open habitats such as *Chenopodium album* increases linearly as $\varphi$ decreases, whereas shade-tolerant understory plants hardly respond (Figure 3C). This shows that shade avoidance and shade tolerance are two different strategies: in the open it pays to compete with neighbors for height; in the understory no amount of elongation can catch up with the trees, and shade-tolerant plants instead raise their photosynthetic efficiency in weak light.

Plants lacking phyB look like wild-type plants growing under a dense canopy: long stems, long petioles, pale leaves and early flowering. Mechanistically, low R:FR converts phyB to Pr, so PIF4, PIF5 and PIF7 are no longer degraded and are rapidly dephosphorylated and activated (dephosphorylation of PIF7 occurs within minutes), promoting expression of auxin biosynthesis genes such as *YUCCA* in the cotyledons; auxin transported to the hypocotyl promotes cell elongation, with brassinosteroids and gibberellins taking part. Negative feedback factors such as HFR1 and PAR1 prevent excessive elongation. In very deep shade (extremely low R:FR) the far-red high-irradiance response of phyA instead inhibits elongation and acts as a buffer. Cryptochromes sense the decrease in blue light and UVR8 senses the decrease in UV-B, and these also take part in shade avoidance.

### 16.6.3. Agricultural Significance

Crops are usually planted densely, and shade avoidance causes plants to invest resources in stems rather than grain and increases the risk of lodging. Maintaining high yield at high density is one direction of modern breeding: for example, much of the yield gain of modern maize varieties comes from tolerance of high-density planting. When oat *PHYA* was overexpressed by genetic engineering in tobacco, the shade avoidance response of the transgenic plants at high density was weakened (the far-red high-irradiance response of phyA inhibits elongation under a canopy) and the harvest index increased (Robson et al., 1996).

## 16.7. Blue-Light and Ultraviolet Photoreceptors

### 16.7.1. Characteristics of Blue-Light Responses

Blue-light responses occur in higher plants, algae, ferns, fungi and prokaryotes: besides phototropism, they include inhibition of hypocotyl elongation, promotion of chlorophyll and carotenoid synthesis, activation of gene expression, enhanced respiration, anion uptake by algae, and phototaxis of unicellular organisms. The action spectra of blue-light responses have a "three-finger" shape between $400$ and $500\,\mathrm{nm}$, a hallmark that distinguishes them from phytochrome responses and photosynthesis.

Blue-light responses have two temporal features: there is an obvious lag between the signal and the maximum rate of response, and the response persists for several minutes after the light is turned off. For example, etiolated cucumber seedlings lower their growth rate and show a transient membrane depolarization only after a lag of about $25\,\mathrm{s}$; the $\ce{H+}$-ATPase of guard cells is inactivated only gradually within several minutes after a blue-light pulse ([7.13.10](/7.13.10#sec-10.4.2)). Photosynthesis, in contrast, begins almost immediately when the light is turned on and stops immediately when it is turned off. The persistence arises from the photochemical cycle of the photoreceptor: blue light converts the receptor to an active form, which slowly returns to the inactive form in the dark after the light is turned off, and the rate of decay of the response is determined by this dark reversion.

### 16.7.2. Cryptochromes

In 1979 Gressel coined the term "cryptochrome" for a receptor distinct from phytochrome that specifically receives blue and near-ultraviolet light; its chemical nature was then unknown, hence the name ("cryptic"), and it also alludes to the fact that blue-light responses were first studied in cryptogams, plants that do not flower. In 1980 Koornneef and colleagues isolated the *Arabidopsis* *hy4* mutant with a long hypocotyl in white light, whose defect appears specifically in blue light; Ahmad and Cashmore cloned *HY4* in 1993, which is *CRY1*. It encodes a protein of about $75\,\mathrm{kDa}$ homologous to microbial photolyases that repair **pyrimidine dimers** in DNA, but without photolyase activity. Cryptochromes were later found in cyanobacteria, ferns, algae, *Drosophila*, mouse and humans; in animals they are components of the circadian clock ([7.6.33](/7.6.33#sec-33.6.1)).

The N terminus of a cryptochrome is the photolyase homology region (PHR), which binds FAD and the antenna pigment MTHF noncovalently and mediates dimerization; the C-terminal extension (CCE or CCT), absent from photolyases, is required for signal transduction. Blue light reduces the bound FAD to the neutral semiquinone $\mathrm{FADH}^{\bullet}$, which is the active state; the conformational change of the PHR region alters the C terminus and allows it to bind partner proteins. Blue light also causes phosphorylation of cryptochromes and promotes their oligomerization, forming photobodies in the nucleus. Cry1 and cry2 are located in the nucleus and cytoplasm and do not change location with light; cry3 (CRY-DASH type) is located in chloroplasts and mitochondria and has photolyase activity toward damaged single-stranded DNA, but its function remains unclear.

| Property | cry1 | cry2 |
|---|---|---|
| Stability in blue light | Stable | Degraded after phosphorylation |
| Phenotype of overexpression | Enhanced inhibition of hypocotyl elongation by blue light, more anthocyanin | Markedly enhanced cotyledon expansion, hypocotyl only slightly shorter |
| Main functions | Sustained inhibition of hypocotyl elongation; anthocyanin synthesis; blue-light entrainment of the clock | Promotion of flowering (the *cry2* mutant flowers late in long days, Guo et al., 1998); cotyledon expansion |

Cryptochromes signal in two ways. One is inhibition of COP1: blue-light-activated cry1 binds SPA1 through its C terminus, so that COP1–SPA cannot degrade HY5 (16.4.3). *Arabidopsis* overexpressing only the C terminus of cry1 (CCT) shows photomorphogenesis in darkness like the *cop* mutants, because the CCT, no longer constrained by the photosensory region, is constitutively active. The other is direct binding to transcription factors: in blue light cry2 binds the bHLH transcription factor CIB1, which binds the promoter of *FLOWERING LOCUS T* (*FT*) and promotes flowering; cry2 and cry1 also stabilize CO protein in the evening of long days ([7.13.21](/7.13.21)). In addition, the nuclear pool of cry1 mediates membrane depolarization within seconds, one of the fastest responses of cryptochromes.

Phytochromes and cryptochromes act cooperatively in many processes. In *Arabidopsis*, continuous blue or far-red light promotes flowering and red light inhibits it, far-red light acting through phyA and the antagonistic action of red light through phyB; the *cry2* mutant flowers late only when blue and red light are given together, indicating that cry2 promotes flowering by inhibiting the action of phyB, an action that passes through EARLY FLOWERING 3 (ELF3).

### 16.7.3. Phototropins

Winslow Briggs and colleagues screened *Arabidopsis* for *nph* (nonphototropic hypocotyl) mutants that do not bend toward weak blue light and cloned the *NPH1* gene, obtaining the photoreceptor for phototropism, named phototropin (now phot1). Angiosperms have two genes, *PHOT1* and *PHOT2*. Phototropins are located at the plasma membrane and are light-activated serine/threonine protein kinases.

The N terminus of a phototropin has two LOV (light, oxygen, voltage) domains, LOV1 and LOV2, each binding one FMN noncovalently. In the dark the absorption peak of FMN is at about $450\,\mathrm{nm}$; blue light, through a triplet intermediate (LOV660), makes FMN form a covalent adduct with a cysteine and shifts the absorption peak to $390\,\mathrm{nm}$; in the dark the adduct breaks spontaneously and returns to the starting state. LOV2 is required to activate the kinase: mutating the conserved cysteine in LOV1 does not affect phototropism, whereas mutating that in LOV2 abolishes it. In the dark the LOV domain "cages" the C-terminal kinase and keeps it inactive; the photoreaction causes the Jα helix after LOV2 to unfold fully, the kinase is "released" and autophosphorylates on several serines, which is the starting point of all phototropin responses; in the dark it is inactivated by dephosphorylation by type 2A protein phosphatases.

The responses mediated by phototropins together optimize photosynthesis, especially in weak light, and *phot1 phot2* double mutants grow very poorly in weak light:

- **Phototropism**: phot1 is the main phototropic receptor and acts in both weak and strong light; phot2 acts only in strong light. Activation of phototropin causes redistribution of auxin to the shaded side, and its mechanism is described in [7.13.19](/7.13.19).
- Chloroplast movement: in weak light chloroplasts move to the upper and lower walls (periclinal walls) of palisade cells and present their flat face to the light, increasing absorption (accumulation response); in strong light they move to the side walls parallel to the incident light (anticlinal walls) and present their narrow face, reducing absorption and avoiding photodamage (avoidance response); in darkness they move to the bottom of the cell. Both phot1 and phot2 take part in the accumulation response, and the avoidance response depends mainly on phot2: the *phot2* mutant lacks the avoidance response and cannot survive in full sunlight in the field because of photooxidative damage. Chloroplast movement depends on a special chloroplast actin filament (cp-actin): CHUP1 on the chloroplast envelope polymerizes actin at the leading edge of the chloroplast and pushes the chloroplast forward.
- Stomatal opening: phototropin phosphorylates the guard-cell-specific kinase BLUS1, and through PP1 the plasma membrane $\ce{H+}$-ATPase is finally phosphorylated and activated by binding 14-3-3 protein, driving $\ce{K+}$ uptake and stomatal opening ([7.13.10](/7.13.10#sec-10.4.2)). Chinese textbooks once listed zeaxanthin as the blue-light receptor of guard cells; the stomata of the *phot1 phot2* double mutant do not respond to blue light, showing that phototropin is the main receptor, and a role for zeaxanthin is doubtful.
- Leaf expansion and orientation, positioning of the nucleus, and the rapid inhibition of hypocotyl elongation (16.5.2).

ZTL, FKF1 and LKP2 are another class of LOV-domain blue-light receptors, in which the LOV domain is joined to an F-box (the adaptor of SCF-type E3 ligases) and Kelch repeats: in the dark ZTL degrades the clock proteins TOC1 and PRR5 (Section 16.8), and FKF1 degrades CDF1, a transcriptional repressor of *CO*, in the afternoon of long days ([7.13.21](/7.13.21)).

### 16.7.4. The UV-B Receptor UVR8

At high doses UV-B is a stress factor that damages DNA (mainly forming cyclobutane pyrimidine dimers) and generates reactive oxygen species; at the low doses in sunlight it is a developmental signal: it induces the synthesis of UV-screening compounds such as flavonoids and anthocyanins, inhibits hypocotyl elongation, inhibits expansion of leaves and epidermal cells, promotes endoreduplication in epidermal cells, changes stomatal density, takes part in entrainment of the clock, and increases UV-B tolerance. The epidermis can absorb almost all incident UV-B, and the accumulation of screening compounds protects the mesophyll from damage. Before UVR8 was discovered, the chemical nature of the UV-B receptor remained unknown for a long time (Rizzini et al., 2011, showed that UVR8 is a UV-B receptor).

UVR8 is a seven-bladed β-propeller protein with no added chromophore. In the absence of UV-B it exists as a homodimer, with the two subunits held together by a network of salt bridges formed between arginines and acidic residues at the interface; each monomer has 14 tryptophans, and several tryptophans near the interface (mainly W285 and W233) change their charge distribution on absorbing UV-B, the salt bridges break, and the dimer dissociates into active monomers. The monomers enter the nucleus and bind COP1–SPA through their C-terminal region. Notably, COP1 is a positive regulator in UV-B signaling: the UVR8–COP1 complex stabilizes HY5 and promotes transcription of *HY5*, and HY5 in turn regulates most UV-B-induced genes. The RUP1 and RUP2 proteins promote the re-formation of dimers from monomers and switch the signal off.

## 16.8. Light and the Circadian Clock

### 16.8.1. Circadian Rhythms

Many plant processes oscillate with a period of about one day: the daily movement of leaves and petals, stomatal opening and closing, growth rate, rates of photosynthesis and respiration, release of fragrance, and the expression of about one third of genes. When plants are moved from alternating light and dark to continuous light or continuous darkness, these rhythms persist for several days with a period close to but not equal to $24\,\mathrm{h}$. In the 1930s Bünning studied this endogenous rhythm using the leaf movements of the bean and proposed that it takes part in timing the photoperiod ([7.13.21](/7.13.21)).

**Definition 16.8.1 (Circadian Rhythm)** A biological rhythm that persists autonomously in a constant environment, has a period of about $24\,\mathrm{h}$, is temperature-compensated in its period and has a phase that can be reset by environmental signals is called a **circadian rhythm** (approximately daily rhythm). The endogenous oscillator that produces it is called the circadian clock.

A rhythm is described by three parameters: period (the time between adjacent peaks or troughs), phase (some identifiable point in the cycle, such as the position of a peak) and amplitude (the difference between peak and trough). Under constant conditions the rhythm "free-runs", drifting with its own period; in nature the clock is **entrained** to exactly $24\,\mathrm{h}$ by environmental signals (zeitgebers), the most important being the light–dark transitions at dawn and dusk, with temperature cycles also playing a role. The rule for phase resetting by light pulses is: light in the first half of the subjective night delays the phase (the clock treats it as a prolonged dusk of the previous day), light in the second half advances the phase (treated as an early dawn of the new day), and light in the subjective day hardly shifts the phase. This phase response enables the clock to follow the seasonal change in day length. Temperature compensation keeps the $Q_{10}$ of the period close to 1 (**temperature coefficient**, [7.6.33](/7.6.33#sec-33.6.1)); otherwise the clock would run fast or slow in cold or warm weather. The general dynamics of biological clocks, namely delayed negative feedback oscillators, the **repressilator** and the **Hopf bifurcation**, are discussed in [7.6.33](/7.6.33), and here we treat only the plant case.

Light entrains the clock through photoreceptors. In *Arabidopsis* the rhythm of a clock-regulated luciferase reporter gene has a period of about $24.7\,\mathrm{h}$ in continuous white light and lengthens to $30$–$36\,\mathrm{h}$ in continuous darkness; red or blue light alone shortens the period to about $25\,\mathrm{h}$. The stronger the light, the shorter the period, which is opposite to nocturnal animals and consistent with diurnal animals (Aschoff's rule). The *phyA* mutant lengthens the period only in weak red light, the *phyB* mutant shows a timing defect only in strong red light, and cry1 and cry2 are required for blue-light entrainment; four of the five phytochromes, all except phyC, take part in entrainment. ELF3 and TIME FOR COFFEE (TIC) regulate light input to the clock: the *elf3* mutant stops the clock at dusk in continuous light, the *tic* mutant stops it at dawn, and the double mutant loses rhythmicity completely. ELF3 is considered a "gating" factor that makes the clock insensitive to light at night.

### 16.8.2. The Molecular Circuit of the *Arabidopsis* Clock

The *Arabidopsis* clock consists of several interlocked transcription–translation feedback loops:

- Morning loop: the mRNAs of the MYB transcription factors CCA1 and LHY peak at dawn, and light directly induces their transcription. CCA1/LHY repress genes expressed at night, including *TOC1* and the evening complex genes *ELF4* and *LUX*. The pseudo-response regulator proteins PRR9, PRR7 and PRR5, expressed in succession during the day (peaking about 2–4, 6–8 and 8–10 h after dawn, respectively), in turn repress *CCA1*/*LHY*, causing them to decline during the day.
- Evening loop: TOC1 (that is, PRR1) peaks at dusk and represses *CCA1*, *LHY* and many night genes. TOC1 was once thought to be an activator of *CCA1*/*LHY* (Alabadí et al., 2001), but later studies showed that, like the other PRRs, it is a transcriptional repressor. In the dark ZTL degrades TOC1 and PRR5, and GIGANTEA stabilizes ZTL in light, so that protein levels oscillate with light and dark.
- Evening complex: the evening complex formed by ELF3, ELF4 and the MYB transcription factor LUX represses, in the evening and at night, *PRR9*, *LUX* itself, *GI* and the elongation-promoting *PIF4* and *PIF5*.

At the core of these loops is a three-component repressilator: CCA1/LHY repress the evening complex, the evening complex represses the PRRs, and the PRRs repress CCA1/LHY (Pokhilko et al., 2012). Three repressors joined head to tail form an odd number of negative feedbacks, an oscillatory circuit of the kind discussed in [7.6.33](/7.6.33); translation, modification and nuclear import between mRNA and protein supply the necessary delay. With this topology the order of peaks must be morning genes, day genes, night genes, in agreement with observation.

### 16.8.3. A Simplified Model

Write each group of genes in terms of two variables, mRNA $m$ and protein $x$, use Hill functions for repression, and let the light $L(t)$ (1 for light, 0 for dark) accelerate the transcription of *CCA1*/*LHY* and the *PRR*s and the degradation of the evening protein:

$$
\begin{aligned}
\frac{\mathrm{d}m_{\mathrm{L}}}{\mathrm{d}t} &= \frac{v_{\mathrm{L}}\,(1 + a_{\mathrm{L}}L)}{1 + x_{\mathrm{P}}^{\,n}} - d_m m_{\mathrm{L}}, &
\frac{\mathrm{d}m_{\mathrm{P}}}{\mathrm{d}t} &= \frac{v_{\mathrm{P}}\,(1 + a_{\mathrm{P}}L)}{1 + x_{\mathrm{E}}^{\,n}} - d_m m_{\mathrm{P}}, &
\frac{\mathrm{d}m_{\mathrm{E}}}{\mathrm{d}t} &= \frac{v_{\mathrm{E}}}{1 + x_{\mathrm{L}}^{\,n}} - d_m m_{\mathrm{E}}, \\
\frac{\mathrm{d}x_{\mathrm{L}}}{\mathrm{d}t} &= d_p\,(m_{\mathrm{L}} - x_{\mathrm{L}}), &
\frac{\mathrm{d}x_{\mathrm{P}}}{\mathrm{d}t} &= d_p\,(m_{\mathrm{P}} - x_{\mathrm{P}}), &
\frac{\mathrm{d}x_{\mathrm{E}}}{\mathrm{d}t} &= d_p\,\bigl(m_{\mathrm{E}} - (1 + a_{\mathrm{E}}L)\,x_{\mathrm{E}}\bigr),
\end{aligned}
\tag{16.8}
$$

where the subscripts L, P and E stand for CCA1/LHY, the PRRs and the evening complex. The parameters (dimensionless concentrations, rates in $\mathrm{h^{-1}}$, $d_m \approx 1$, $d_p \approx 0.23$, $n = 2$) are chosen so that the free-running period in continuous light is about $24.6\,\mathrm{h}$. The model reproduces several qualitative properties (Figure 4): in 12 h light : 12 h dark, the three groups of mRNA peak in the order morning, day, night, and the rhythm is entrained to $24\,\mathrm{h}$; after transfer to continuous light the rhythm free-runs with its own period and the amplitude gradually decreases; the stronger the light input, the shorter the period. It does not include temperature compensation or the details of the phase response, which require more loops and posttranslational regulation.

![Three-component repressilator model of the *Arabidopsis* clock, numerical solution of Eq. (16.8). A: Entrainment first in 12 h light : 12 h dark (gray is the dark period), then transfer to continuous light (light yellow) after 48 h. The mRNAs of CCA1/LHY (morning), the PRRs (day) and the evening complex (night) peak in succession, each normalized; the dotted lines mark the CCA1/LHY peaks, whose spacing in continuous light is about 24.6 h, so the rhythm gradually shifts later relative to 24 h and the amplitude decreases. B: In continuous light of different intensities, the free-running period shortens from about 26.6 h to 24.6 h as the light input increases. Parameters are illustrative and concentrations dimensionless](./plots/circadian-clock.py)

The clock controls the timing of expression of about one third of genes. CCA1/LHY bind the CCA1-binding sites in the promoters of morning genes, and night genes mostly contain the "evening element". The clock lets plants prepare in advance: the synthesis of photosynthetic proteins begins before dawn, and starch is consumed at night at a linear rate set by the starch reserve so that it runs out exactly at dawn. Plants whose period matches the environmental period fix more carbon by photosynthesis and grow faster ("circadian resonance", Dodd et al., 2005). The clock also "gates" light signals: the same light causes different responses at different times of day, which is the basis of timing the photoperiod (the external coincidence model, [7.13.21](/7.13.21)); the evening complex represses *PIF4* at dusk, concentrating hypocotyl elongation before dawn, and this rhythm interacts with temperature in Section 16.9.

## 16.9. Thermomorphogenesis

### 16.9.1. Morphology in Warmth

**Definition 16.9.1 (Thermomorphogenesis)** The set of responses in which plants change morphology at elevated temperatures that do not cause stress (in *Arabidopsis* from about $22\,^\circ\mathrm{C}$ to $27$–$28\,^\circ\mathrm{C}$) is called **thermomorphogenesis**: elongation of hypocotyls and petioles, upward movement of leaves, thinner leaves and earlier flowering.

Thermomorphogenesis closely resembles shade avoidance in morphology and shares a hub with it at the molecular level: PIF4. Elongated plants with raised leaves are better ventilated, the efficiency of cooling by leaf transpiration increases, and leaves are farther from the heat source at the ground; against the background of global warming, the effect of thermomorphogenesis on crop yield is receiving attention. How do plants sense a difference of a few degrees? Research over the past decade has found several temperature receptors, two of which belong to the light signaling system.

### 16.9.2. PhyB Is a Temperature Receptor

In 2016 two groups reported in the same issue of *Science* that phytochrome B is a temperature receptor (Jung et al.; Legris et al.). The evidence has two parts: first, temperature changes the Pfr/Pr ratio of phyB just as light does, with warmth accelerating the thermal reversion of Pfr to Pr and reducing active phyB; second, mutants lacking phytochrome show the phenotype and transcriptome of warm conditions already at low temperature, that is, the temperature response becomes constitutive. The decrease in active phyB stabilizes PIF4, and PIF4 promotes expression of the auxin biosynthesis gene *YUCCA8* and hypocotyl elongation.

This mechanism can be understood quantitatively with Eq. (16.1). With thermal reversion included, the steady-state Pfr fraction in light is

$$
\frac{[\mathrm{Pfr}]}{\mathrm{P_{tot}}} = \frac{k_1}{k_1 + k_2 + k_{\mathrm{r}}(T)},
\tag{16.9}
$$

where $k_{\mathrm{r}}$ increases with temperature. In full sunlight $k_1 + k_2$ is several per second (Example 16.2.1), and thermal reversion (taking $k_{\mathrm{r}}$ of the order of $10^{-4}\,\mathrm{s^{-1}}$) has almost no effect; in weak light, especially at night, thermal reversion decides the fate of Pfr. At night Pfr decays according to Eq. (16.4), faster at higher temperature (Figure 5B), so phyB "integrates" temperature over the night, and by the time of dawn the level of active phyB reflects the nighttime temperature, just before the period when PIF4 promotes elongation. The real phyB system is more complex than this single-rate model: the physiologically active species is mainly the Pfr:Pfr dimer, whose fraction is approximately proportional to $\varphi^2$, the Pfr:Pr heterodimer reverts faster, and, together with the state of nuclear photobodies, temperature effects can also be measured at intermediate light intensities under shade.

![Competition between photoconversion and thermal reversion of phyB (schematic single-rate model). A: The steady-state Pfr fraction in daylight spectrum as a function of photosynthetically active radiation, according to Eq. (16.9), with $k_1$ and $k_2$ calculated from the model spectra of Figure 1 and the thermal reversion rate constant taken as $2\times10^{-4}\,\mathrm{s^{-1}}$ at 22 °C with $Q_{10} = 3$; in strong light the curves for the three temperatures coincide at $\varphi = 0.6$, and in the weak light of dusk (shaded) the influence of temperature is largest. B: Decay of Pfr in darkness after $\varphi = 0.6$ at dusk: the higher the temperature, the faster the decay. Parameters are illustrative](./plots/phyb-thermal-reversion.py)

### 16.9.3. ELF3 and the Evening Complex

ELF3, the scaffold protein of the evening complex, is also a temperature receptor (Jung et al., 2020, *Nature*). ELF3 has a prion-like domain (a low-complexity sequence rich in glutamine); at $22\,^\circ\mathrm{C}$ ELF3 is diffusely distributed in the nucleus, binds the promoters of target genes such as *PIF4* and represses their transcription; at $27\,^\circ\mathrm{C}$ it undergoes temperature-dependent **liquid–liquid phase separation** and condenses into small speckles (**biomolecular condensates**), leaving the target genes, the repression is relieved, and elongation and flowering genes can be expressed. This process is reversible, and its sensitivity to temperature varies with the length of the polyglutamine repeat in the prion-like domain. The two receptors phyB and ELF3 converge on PIF4: phyB-Pfr promotes the degradation of PIF4, the evening complex represses transcription of *PIF4*, and warmth weakens both (Figure 4).

Other known plant temperature-sensing mechanisms include the following: the lifetime of the light-activated state of the phototropin LOV domain shortens with temperature, and the liverwort *Marchantia polymorpha* uses this to adjust chloroplast position at low temperature (Fujii et al., 2017); a hairpin in the 5′ untranslated region of *PIF7* mRNA loosens in warmth and raises translation efficiency, an **RNA thermometer** (Chung et al., 2020); and nucleosomes containing the histone variant H2A.Z are removed from target genes in warmth. Light and temperature signals are integrated on the same set of proteins, which is also why phytochrome can sense shade and warmth at the same time: the two mean similar situations for a plant and elicit similar responses.

Whether light and temperature receptors also take part in sensing the low temperature of vernalization is suggested by traditional physiological observations but remains unresolved (for vernalization see [7.13.22](/7.13.22)).

## Summary

| Topic | Key points | Quantitative relations |
|---|---|---|
| Skotomorphogenesis and photomorphogenesis (Definition 16.1.1) | Etiolated seedling: axis elongation, hook, closed cotyledons, etioplasts; de-etiolation reverses these; skotomorphogenesis is the default program | LFR saturating fluence $\approx 1000\,\mu\mathrm{mol\,m^{-2}}$, about $1\,\mathrm{s}$ of red light in full sunlight |
| Photoreceptors (Table 16.1) | Phytochrome (red/far-red, phytochromobilin), cryptochrome (blue, FAD), phototropin and ZTL (blue, FMN), UVR8 (UV-B, tryptophan) | Action spectra identify receptors; "three-finger" spectrum of blue-light responses |
| Phytochrome photochemistry (16.2) | Pr ($666\,\mathrm{nm}$) $\rightleftharpoons$ Pfr ($730\,\mathrm{nm}$), Pfr is the active form; Z/E isomerization of C15=C16; photoreversibility | $\varphi = k_1/(k_1+k_2)$; red $0.85$–$0.88$, far-red $0.02$–$0.03$, sunlight about $0.6$; $\sigma_{\mathrm{r}}(660) \approx 4\times10^{-3}\,\mathrm{m^2\,\mu mol^{-1}}$, $\tau = 1/(k_1+k_2)$ |
| phyA and phyB (16.2.5) | phyA light-labile, FHY1 import, VLFR and FR-HIR; phyB light-stable, own NLS, LFR, R-HIR, shade avoidance | phyA decreases by one to two orders of magnitude in light |
| The three response types (Definition 16.3.2) | VLFR not reversible (2–3% Pfr remains after far-red); LFR reversible, obeys reciprocity; HIR depends on intensity, does not obey reciprocity | VLFR $10^{-4}$–$10^{-1}$, LFR $1$–$1000\,\mu\mathrm{mol\,m^{-2}}$; VLFR needs Pfr $< 0.02\,\%$ |
| Signal transduction (16.4) | Nuclear import; PIFs (bHLH) maintain skotomorphogenesis in the dark and are phosphorylated and degraded in light; COP1–SPA degrades HY5 in the dark and is inhibited by photoreceptors; derepression logic | Fastest transcriptional change about $5\,\mathrm{min}$ |
| Light-requiring seeds and de-etiolation (16.5) | phyB–PIF1–GA/ABA; phot1 (first 30 min) → cry1 (sustained) relay in inhibition of elongation | Elongation $0.25\,\mathrm{mm\,h^{-1}}$ in the dark, blue-light lag about $30\,\mathrm{s}$ |
| Shade avoidance (Definition 16.6.1) | Low R:FR → phyB inactive → PIF4/5/7 → auxin; elongation, leaf raising, less branching, early flowering; shade-tolerant plants respond weakly | $\varphi(\zeta)$ hyperbolic, Eq. (16.7); sunlight $\zeta = 1.15$, $\varphi \approx 0.63$; $\zeta = 0.2$, $\varphi \approx 0.29$ |
| Cryptochromes (16.7.2) | Photolyase homology, no enzymatic activity; cry1 inhibits elongation, cry2 promotes flowering (CIB1–*FT*); CCT binds SPA and inhibits COP1 | — |
| Phototropins (16.7.3) | Plasma membrane kinase, LOV2–Jα unfolding releases the kinase; phototropism, chloroplast accumulation and avoidance (phot2, CHUP1), stomatal opening (BLUS1) | FMN absorption peak $450 \to 390\,\mathrm{nm}$ |
| UVR8 (16.7.4) | Tryptophan as chromophore; dimer dissociates to monomers that bind COP1, which then promotes HY5; RUP switches off | — |
| Circadian clock (Definition 16.8.1) | Repressilator CCA1/LHY ⊣ evening complex ⊣ PRR ⊣ CCA1/LHY; TOC1 is a repressor; light entrains through phyA/B and cry1/2; ZTL degrades TOC1 | Period about $24.7\,\mathrm{h}$ in continuous light, longer in continuous darkness; $Q_{10} \approx 1$ |
| Thermomorphogenesis (Definition 16.9.1) | Thermal reversion of phyB (2016) and phase separation of ELF3 (2020) converge on PIF4; also phototropin, the *PIF7* RNA thermometer and H2A.Z | Eq. (16.9): thermal reversion dominates in weak light and at night |

Main equations:

- Photoconversion kinetics: $\mathrm{d}[\mathrm{Pfr}]/\mathrm{d}t = k_1[\mathrm{Pr}] - (k_2 + k_{\mathrm{r}})[\mathrm{Pfr}]$, Eq. (16.1); $k = \int q(\lambda)\sigma(\lambda)\,\mathrm{d}\lambda$, $\sigma = \ln 10\,\varepsilon\Phi$, Eq. (16.2).
- Photostationary state $\varphi = k_1/(k_1+k_2)$, Eq. (16.3); Pfr fraction after a pulse $\varphi(1 - \mathrm{e}^{-(\sigma_{\mathrm{r}}+\sigma_{\mathrm{fr}})F})$, Eq. (16.6).
- Decay in the dark $[\mathrm{Pfr}](t) = [\mathrm{Pfr}](0)\,\mathrm{e}^{-(k_{\mathrm{r}}+k_{\mathrm{d}})t}$, Eq. (16.4); reciprocity law $R = f(It)$, Eq. (16.5).
- Two-band model $\varphi(\zeta)$, Eq. (16.7); steady state with thermal reversion, Eq. (16.9); three-component repressilator of the clock, Eq. (16.8).

## Questions

1. In the lettuce seed experiment of Table 16.2, why is the germination after a treatment ending with red light about 70%–76% rather than 100%, and that after a treatment ending with far-red light about 6%–7% rather than 0? What result is expected if, after the last red light, the seeds are left in the dark for several hours before far-red light is given?

   **Answer** The photostationary state means that red light can convert only about 85%–88% of phytochrome to Pfr, and 2%–3% Pfr remains after far-red light; in addition, individual seeds in the population differ in their threshold for Pfr. So after red light a fraction of seeds always fail to reach the Pfr threshold, and after far-red light a few seeds with very low thresholds (and seeds that germinate without light) still germinate. Germination is determined by the overlap between the Pfr level and the distribution of individual thresholds in the population, and is not all-or-none. If seeds are left in the dark for several hours after red light, Pfr has completed its primary action and the germination of many seeds has "escaped" photoreversible control, so far-red can reverse only part of it; germination will lie between the two extremes and rise as the interval is lengthened.

2. (Calculation) Take $\sigma_{\mathrm{r}}(660) = 4.1\times10^{-3}\,\mathrm{m^2\,\mu mol^{-1}}$ and $\varphi(660) = 0.87$. (a) A red safelight of $0.5\,\mu\mathrm{mol\,m^{-2}\,s^{-1}}$ illuminates etiolated *Arabidopsis* seeds for $5\,\mathrm{s}$. What Pfr fraction is produced? Does it induce a very low fluence response or a low-fluence response? (b) How long must the seeds be illuminated in red light of $5\,\mu\mathrm{mol\,m^{-2}\,s^{-1}}$ for the Pfr fraction to reach 95% of the photostationary value?

   **Answer** (a) The fluence is $F = 0.5 \times 5 = 2.5\,\mu\mathrm{mol\,m^{-2}}$, and the Pfr fraction is $\approx \sigma_{\mathrm{r}}F = 4.1\times10^{-3} \times 2.5 \approx 1.0\times10^{-2}$, about 1%. This far exceeds what is needed to saturate the VLFR (0.02%) and also reaches the starting point of the LFR (about $1\,\mu\mathrm{mol\,m^{-2}}$): the VLFR will be saturated and the LFR partially induced. Experiments on the VLFR must therefore be handled in complete darkness or with a green safelight (the $\sigma_{\mathrm{r}}$ in green light is much smaller), and even green light must have its fluence controlled.

   (b) $\sigma_{\mathrm{fr}}(660) = \sigma_{\mathrm{r}}(1-\varphi)/\varphi = 6.1\times10^{-4}$, and $k_1 + k_2 = (4.1 + 0.61)\times10^{-3} \times 5 = 0.0236\,\mathrm{s^{-1}}$. From $1 - \mathrm{e}^{-t/\tau} = 0.95$, $t = \tau\ln 20 = 3.0/0.0236 \approx 127\,\mathrm{s}$, about 2 min, corresponding to a fluence of about $640\,\mu\mathrm{mol\,m^{-2}}$.

3. (Calculation) In a maize field, R:FR is 1.15 at the top of the canopy and 0.15 on the ground between the rows. Using the cross sections of Example 16.6.1 and Eq. (16.7), calculate $\varphi$ at the two places. If the germination of a weed seed requires $\varphi > 0.4$, can it germinate between the rows? What happens when tillage turns the seed to the surface and exposes it to sunlight for 1 s?

   **Answer** At the top $\varphi \approx 0.63$ (Example 16.6.1). Between the rows $\zeta = 0.15$: numerator $4.1 \times 0.15 + 0.053 = 0.668$, denominator $4.71 \times 0.15 + 2.12 = 2.83$, $\varphi \approx 0.24$, below 0.4, so the seed remains dormant. Turned to the surface and exposed to full sunlight for 1 s: $k_1 + k_2 \approx 4\,\mathrm{s^{-1}}$ (Example 16.2.1), so within 1 s the photostationary state of sunlight, $\varphi \approx 0.6$, is reached; even if the exposure is shorter and only a little Pfr forms, seeds that become extremely sensitive after burial can germinate through the very low fluence response of phyA. This explains the concentrated emergence of weeds after tillage and why tillage at night reduces weeds.

4. (Calculation) Suppose Pfr of phyB reverts thermally in the dark with first-order kinetics, $k_{\mathrm{r}}(22\,^\circ\mathrm{C}) = 2\times10^{-4}\,\mathrm{s^{-1}}$, $Q_{10} = 3$. At dusk $\varphi = 0.6$. Calculate the Pfr fraction 1 h after nightfall at 22 °C and at 28 °C, and the time needed for Pfr to fall to 0.1. What does this mean for understanding thermomorphogenesis?

   **Answer** $k_{\mathrm{r}}(28) = 2\times10^{-4} \times 3^{0.6} \approx 3.9\times10^{-4}\,\mathrm{s^{-1}}$. After 1 h: at 22 °C $0.6\,\mathrm{e}^{-0.72} \approx 0.29$; at 28 °C $0.6\,\mathrm{e}^{-1.39} \approx 0.15$. The time to fall to 0.1 is $t = \ln 6/k_{\mathrm{r}}$: at 22 °C $1.79/(2\times10^{-4}) \approx 9.0\times10^{3}\,\mathrm{s} \approx 2.5\,\mathrm{h}$, and at 28 °C about $1.3\,\mathrm{h}$. Warmth makes active phyB disappear earlier and more completely at night, so PIF4 can accumulate in the second half of the night and elongation before dawn is enhanced. The dependence of the thermal reversion rate on temperature writes temperature information into the dynamics of nighttime Pfr, so phyB acts as an integrator of nighttime temperature.

5. (Open question) Design an experiment in *Arabidopsis* to distinguish the roles of phyA, phyB and cry1 in seedling de-etiolation, stating the light conditions, materials and expected results.

   **Answer** Approach: use monochromatic light to activate the different receptors separately and compare mutants. The materials are wild type, the single mutants *phyA*, *phyB* and *cry1*, and the double mutant *phyA phyB*, germinated in the dark and then transferred to continuous far-red light, continuous red light, continuous blue light and darkness for several days, measuring hypocotyl length, cotyledon opening angle and anthocyanin content. Expected results: in continuous far-red light only the *phyA* mutant elongates as in darkness (the FR-HIR is mediated by phyA); in continuous red light the hypocotyl of the *phyB* mutant is clearly longer and *phyA* is essentially normal; in continuous blue light the hypocotyl of the *cry1* mutant is long and *phyA* and *phyB* have little effect; the double mutant loses the response in both red and far-red light but still responds partly in blue light. Red pulses followed by far-red reversal can be used to distinguish the LFR (phyB) from the irreversible VLFR (phyA), growth measurements with high temporal resolution (infrared imaging) to distinguish the early response mediated by phot1 from the sustained response mediated by cry1, *PHYB-GFP* to observe nuclear import, and Western blots to measure the degradation of PIF3 in different light conditions.
