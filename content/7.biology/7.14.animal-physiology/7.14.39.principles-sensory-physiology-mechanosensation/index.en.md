---
title: Principles of Sensory Physiology and Mechanosensation
description: Receptor types and adequate stimuli; labeled lines and univariance; receptor potentials, frequency coding and dynamic range; Weber–Fechner and Stevens laws; adaptation; receptive fields and lateral inhibition; the four-level framework of mechanosensation, Piezo2, cutaneous mechanoreceptors, Pacinian corpuscle, somatosensory pathways and proprioception; mechanosensation across species.
source_hash: 1f2666e7ad6c
---

All that an animal knows about the world begins at its receptors. Photons, sound waves, molecules, temperature, and force must first be converted into electrical signals that neurons can transmit. The sensory organs look very different: the eye, ear, nose, and skin have almost nothing in common. Yet they solve the same set of problems: how to respond to only one kind of stimulus (specificity), how to detect extremely weak signals while accommodating intensities spanning many orders of magnitude (sensitivity and dynamic range), how to report when a stimulus begins and changes (adaptation), and how to report where it is (receptive fields and lateral inhibition). This chapter first presents these principles common to all senses. It then turns to mechanosensation as an example, to see how the mechanics of accessory structures, mechanically gated channels, and neural coding divide the labor in a single act of touch. Action potentials and conduction are discussed in [7.14.4](/7.14.4), and the basic units of neural circuits in [7.14.6](/7.14.6); the membrane mechanics of mechanosensitive channels was treated in biophysics ([7.6.25](/7.6.25)), and only its conclusions are used here. The following chapters cover pain and thermal sensation ([7.14.40](/7.14.40)), vision ([7.14.41](/7.14.41)), hearing and the vestibular sense ([7.14.42](/7.14.42)), and chemical senses ([7.14.43](/7.14.43)); muscle spindles and Golgi tendon organs are discussed in detail in the chapter on motor control ([7.14.44](/7.14.44)).

## 39.1. Receptors and Sensation

### 39.1.1. Types of Receptors

**Definition 39.1.1 (Receptor and Adequate Stimulus)** A structure that converts one form of stimulus energy into a neural signal is called a receptor; the kind of stimulus to which it is most sensitive, with the lowest threshold, is called its **adequate stimulus**.

A receptor may be the ending of a sensory neuron (touch, pain, olfaction) or a specialized epithelial cell that forms a synapse with a sensory neuron (hair cells, taste cells, retinal photoreceptors). By the form of energy of the adequate stimulus, receptors in the human body fall into five classes:

| Type | Adequate stimulus | Examples |
|---|---|---|
| Mechanoreceptor | Pressure, stretch, vibration, acceleration | Cutaneous touch and pressure receptors, **muscle spindles**, baroreceptors, **hair cells** |
| **Thermoreceptor** | Increase or decrease of temperature | Cold receptors, warm receptors |
| **Nociceptor** | Actual or potential tissue damage (intense mechanical, thermal, or chemical stimuli) | Free nerve endings |
| Electromagnetic receptor | Light (in some animals also electric and magnetic fields, [7.14.43](/7.14.43)) | Rods, cones |
| Chemoreceptor | Concentration of chemical substances | Taste cells, olfactory neurons, carotid body, **osmoreceptors** |

By location, receptors are also classified as exteroceptors (body surface, responding to the external environment), interoceptors (viscera and blood vessels, reporting the state of the **internal environment**, such as the baroreceptors of Chapter 16 and the chemoreceptors of Chapter 20), and proprioceptors (muscles, tendons, and joints, reporting the position and movement of the body itself). Some sensations are composite: there is no dedicated "wetness receptor"; the sensation of wetness arises when the central nervous system combines cold and touch-pressure inputs.

### 39.1.2. The Labeled Line Principle

Each receptor is most sensitive to its adequate stimulus, but it is not completely unresponsive to others: pressing on a closed eye produces flashes of light, and electrical stimulation of the auditory nerve produces sounds. What determines the quality of a sensation?

**Definition 39.1.2 (Labeled Line Principle)** The modality of a sensation (vision, hearing, touch, pain, ...) is determined not by the physical form of the stimulus but by the part of the central nervous system to which the activated nerve fibers lead. This is called the **labeled line principle**.

This is the modern statement of the "doctrine of specific nerve energies" proposed by Johannes Müller in the 1830s. Two corollaries deserve attention. First, activating the same pathway by a different means still produces the sensation of that pathway. In *Drosophila* larvae, when class IV multidendritic neurons are made to express a light-sensitive cation channel by **optogenetics**, blue light alone is enough to trigger the rolling escape behavior, identical to the response to the ovipositor of a parasitoid wasp (Hwang et al., 2007); the light does not harm the larva, and what is activated is the "nociception" labeled line. Second, the output of a single receptor carries no information about the kind of stimulus, only about the degree to which it is activated. The response of a cone depends only on the number of photons it absorbs, so a more intense light of a nonoptimal wavelength and a less intense light of the optimal wavelength can evoke exactly the same response. This is called **univariance**; color can be obtained only by the central comparison of the outputs of several classes of cones ([7.14.41](/7.14.41)).

### 39.1.3. Six Principles of Sensory Transduction

| Principle | Content |
|---|---|
| 1. Transduction and detection occur together | The receptor converts environmental energy into a neural signal; transduction is the starting point of sensation |
| 2. Modality specificity | Different receptors correspond to different stimuli; the quality of a sensation is determined by the pathway (labeled line principle); a single receptor is univariant |
| 3. A few general molecular mechanisms | Two classes of mechanisms cover most senses: **G protein–coupled receptor** plus **second messenger** cascades (vision, olfaction, sweet, umami, and bitter taste) and directly gated ion channels (**mechanosensitive channels** for touch, hearing, and proprioception; temperature- and chemically gated TRP channels for thermal sensation and some pain); specialized cellular structures direct the stimulus to the molecules |
| 4. Amplification and local electrical signals | Weak stimuli are amplified to produce graded receptor potentials; the key performance measures are sensitivity and dynamic range |
| 5. Coding by action potentials | Receptor potentials are converted into the frequency and temporal pattern of action potentials, which travel to the central nervous system |
| 6. Sensation is a cognitive process of the center | Receptors only sample; sensation is interpreted and constructed centrally |

The two classes of mechanisms in principle 3 each have their strengths. GPCR cascades have enormous amplification (one photoactivated rhodopsin can activate over a hundred **transducin** molecules, [7.14.41](/7.14.41)) but require tens of milliseconds; mechanically gated channels are opened directly by force, and those of hair cells open within microseconds, suiting hearing and touch, which need speed and high temporal resolution, at the cost that amplification must be provided by other mechanisms.

## 39.2. Receptor Potentials and Intensity Coding

### 39.2.1. The Receptor Potential

**Definition 39.2.1 (Receptor Potential)** The graded change of membrane potential produced across the receptor membrane by the opening of transduction channels when a receptor is stimulated is called the **receptor potential**; when it arises at the ending of a sensory neuron and directly triggers action potentials in that neuron, it is also called a generator potential.

The receptor potential is a **local potential** (Definition 4.4.1): its amplitude is graded with stimulus intensity, it can summate, it decays electrotonically along the membrane, and it has no refractory period. Most receptor potentials are depolarizing, because transduction channels are nonselective cation channels, and at the **resting potential** the current is mainly $\ce{Na+}$ influx; vertebrate photoreceptors are an exception, hyperpolarizing in response to light. In the endings of sensory neurons, the receptor potential spreads electrotonically to the first site capable of generating **action potentials** (usually the first node of Ranvier in myelinated fibers), where it is converted into action potentials; in specialized receptor cells, the receptor potential modulates transmitter release, and the postsynaptic afferent fiber generates the action potentials.

### 39.2.2. Frequency Coding and Dynamic Range

The receptor potential varies with stimulus intensity in a characteristic shape: approximately linear for weak stimuli and gradually saturating for strong ones. A common description is

$$
V_{\mathrm{r}} = V_{\max}\frac{S^n}{S^n + S_{1/2}^n}, \tag{39.1}
$$

where $S$ is the stimulus intensity, $S_{1/2}$ is the intensity at which the receptor potential reaches half its maximum, and $n$ is about $1$ (in vision this form is called the Naka–Rushton function, and it has the same form as the binding curve in [7.6.4](/7.6.4)). Over about one order of magnitude around $S_{1/2}$, $V_{\mathrm{r}}$ increases approximately linearly with $\ln S$ (over the two orders of magnitude from $0.1S_{1/2}$ to $10S_{1/2}$, $V_{\mathrm{r}}$ rises from about $9\%$ to $91\%$ of its maximum): the saturating curve compresses a very wide range of stimuli into a limited range of voltage, at the cost of reduced resolution at the strong end.

Once the receptor potential exceeds threshold, the firing frequency of the afferent fiber increases monotonically with it; this is **frequency encoding**. Because of the refractory period, the firing rate of a single fiber does not exceed a few hundred hertz, so the range of intensities a single fiber can encode is limited. Sensory systems extend the dynamic range in three ways:

- Compression: the saturation of Eq. (39.1) makes the receptor potential depend approximately logarithmically on intensity.
- Recruitment (population coding): receptors of different thresholds at the same site share different intensity ranges, and stronger stimuli activate more fibers, similar to the recruitment of **motor units** in the motor system.
- Adaptation: the operating point of the receptor shifts with the background intensity (Section 39.3); through this mechanism vision works over a range of about $10^{10}$ in light intensity ([7.14.41](/7.14.41)).

### 39.2.3. Psychophysics of Intensity

The coding at the level of receptors and fibers ultimately appears as how subjective sensation intensity depends on stimulus intensity. Ernst Weber found in the 1830s that the smallest discriminable change in intensity (the difference threshold $\Delta S$) is approximately a constant fraction of the original intensity $S$; Gustav Fechner inferred from this that sensation intensity is proportional to the logarithm of stimulus intensity.

**Formula 39.2.1 (Weber's Law and Fechner's Law)**

$$
\frac{\Delta S}{S} = k_{\mathrm{W}}, \qquad \psi = c\,\ln\frac{S}{S_0}, \tag{39.2}
$$

where $k_{\mathrm{W}}$ is the Weber fraction, $S_0$ is the absolute threshold, and $\psi$ is the sensation intensity.

This is the **Weber–Fechner law**; it has the same mathematical property as fold-change detection in the bacterial chemotaxis network ([7.6.35](/7.6.35#sec-35.6.3)). The Weber fraction differs among senses: about $0.02$ for lifted weights, $0.05$ for loudness, and $0.08$ for brightness. At both very weak and very strong stimulus intensities, the Weber fraction increases.

Fechner's logarithmic law assumes that each "just noticeable difference" represents the same increment of sensation. In the 1950s S. S. Stevens turned to magnitude estimation, in which subjects directly rate sensation intensity, and found a different regularity.

**Definition 39.2.2 (Stevens' Power Law)** The subjective sensation intensity $\psi$ and the stimulus intensity $S$ satisfy

$$
\psi = c\,(S - S_0)^{\beta}, \tag{39.3}
$$
where the exponent $\beta$ differs among senses. This is called **Stevens' power law**.

| Sensation (stimulus) | $\beta$ |
|---|---|
| Brightness (dark-adapted eye, $5^\circ$ spot) | $0.33$ |
| Loudness (sound pressure of a $3\,\mathrm{kHz}$ pure tone) | $0.67$ |
| Visual length | $1.0$ |
| Heaviness | $1.45$ |
| Electric shock (finger, $60\,\mathrm{Hz}$) | $3.5$ |

Senses with $\beta < 1$ compress intensity and can be used over a very wide range; senses with $\beta > 1$ (electric shock, some pain) expand intensity, so that a small increment of a strong stimulus causes a much larger sensation, which suits warning. A power law is a straight line on log–log axes, and the logarithmic law is a straight line on semilog axes; over a limited range both fit data approximately, and their difference lies mainly in the assumptions about how the "quantity of sensation" is measured.

## 39.3. Adaptation

### 39.3.1. Rapidly and Slowly Adapting Receptors

When a constant stimulus acts on a receptor, the firing rate of the afferent fiber is first high and then falls; this is the **adaptation** of the receptor. The speed and extent of adaptation differ among receptors.

**Definition 39.3.1 (Rapidly and Slowly Adapting Receptors)** A receptor that fires only briefly at the onset (sometimes also at the offset) of a sustained stimulus and then quickly stops firing is called a **rapidly adapting receptor**, also called a phasic receptor; a receptor that keeps firing during the stimulus, with its rate falling only slowly, is called a **slowly adapting receptor**, also called a tonic receptor.

The two kinds of receptors convey different information. Slowly adapting receptors report states: **muscle spindles**, joint capsule receptors, baroreceptors, and Merkel disks fire throughout the stimulus, so the central nervous system always knows the length of a muscle, the level of blood pressure, or the degree of pressure on the skin (baroreceptors also "reset" within days, [7.14.16](/7.14.16)). Rapidly adapting receptors report changes: Pacinian corpuscles and hair follicle receptors fire only when a stimulus begins or changes, and their firing rate relates to the rate of change, so they are also called rate receptors. Their value lies in prediction: knowing the speed of rotation of a joint, the central nervous system can anticipate its position in the next instant and correct in advance; when running, with position signals but no rate signals, corrections would always come too late. We do not feel our clothes or a wristwatch, yet notice them when they are removed; this too is the "on–off" response of rapidly adapting receptors.

### 39.3.2. Mechanisms of Adaptation

Adaptation can occur at every step from stimulus to action potential, and different receptors use different combinations:

1. Mechanics of accessory structures: accessory structures dissipate sustained force and pass only changes to the ending. The capsule of the Pacinian corpuscle is the classic example (Section 39.5.4).
2. Transduction molecules: changing the number of sensing molecules (receptor endocytosis), or changing their conformation or activity. Examples are inactivation of mechanically gated channels (Piezo2 inactivates within a few milliseconds); myosin motor slipping in hair cells, which readjusts the tension of the tip links ([7.6.31](/7.6.31#sec-31.5)); phosphorylation of rhodopsin and **arrestin** binding in photoreceptors, together with **negative feedback** by $\ce{Ca^2+}$ ([7.14.41](/7.14.41)); and in olfactory neurons, $\ce{Ca^2+}$–**calmodulin** decreasing the sensitivity of the cyclic nucleotide-gated channel.
3. The encoder: at the site of action potential generation, sustained depolarization gradually inactivates voltage-gated $\ce{Na+}$ channels and activates slow $\ce{K+}$ currents (such as $\ce{Ca^2+}$-activated $\ce{K+}$ currents), lowering the firing rate.

At the level of the system, adaptation shifts the receptor's operating point with the background so that it responds only to relative change; this is one realization of Weber's law, and its dynamical principles (integral feedback and so on) are given in [7.9.16](/7.9.16) and [7.6.35](/7.6.35).

## 39.4. Receptive Fields and Lateral Inhibition

### 39.4.1. Receptive Fields

**Definition 39.4.1 (Receptive Field)** The part of the receptive surface (an area of skin, a region of retina, a range of frequencies, and so on) in which a stimulus can change the activity of a sensory neuron is called the **receptive field** of that neuron.

The receptive field of a primary afferent fiber is determined by the extent covered by its terminal branches; the receptive field of a central neuron is determined by the afferent fibers converging on it, and is usually larger and more complex in shape. The higher the density of receptors in the skin, the smaller the receptive fields and the higher the spatial resolution: in the glabrous skin of the hand, the fingertip has about $140$ rapidly adapting type I fibers and $70$ slowly adapting type I fibers per square centimeter, falling in the palm to about $25$ and $8$, that is, to about a fifth and a ninth (Johansson and Vallbo, 1979).

### 39.4.2. Lateral Inhibition

Density alone is not enough: neighboring receptive fields overlap, and two nearby point stimuli would produce one continuous region of excitation in the central nervous system. Sensory pathways solve this problem with inhibitory interneurons.

**Definition 39.4.2 (Lateral Inhibition)** The inhibition of surrounding neurons by an excited sensory neuron through inhibitory interneurons, which sharpens the edges of the excited region and enhances contrast, is called **lateral inhibition**.

Lateral inhibition gives central neurons receptive fields with a center–surround structure: excitation in the center and inhibition in the surround. Mathematically, it amounts to the **convolution** of the input with a kernel that is "positive in the center and negative in the surround" (the difference of two Gaussians), which filters out the uniform component and highlights spatial variation. The one-dimensional model in the figure shows that lateral inhibition produces a dip between two point stimuli, so that they can be resolved as two points at a smaller separation; the two-point threshold is proportional to the receptive field width, so on the back, where receptors are sparse and receptive fields large, the two-point threshold is far larger than at the fingertip. Lateral inhibition exists at every relay of the dorsal column nuclei, thalamus, and cortex, and is most prominent in the retina ([7.14.41](/7.14.41)); the mechanism of the same name implemented by Notch signaling in development is a different matter ([7.3.24](/7.3.24)), and the two are similar only in logic.

![Lateral inhibition improves two-point discrimination (schematic one-dimensional model). Receptors are spaced 0.25 mm apart, and the receptive field of each afferent fiber is a Gaussian of width σ; the central layer sums the afferent inputs with the same Gaussian weighting and subtracts an inhibitory surround of width 2σ and weight 0.9 (the difference of two Gaussians, with rectified output). A: central activity evoked by two point stimuli (dashed lines) 3.2 mm apart at σ = 1 mm: without lateral inhibition there is almost no dip between the two peaks, and with lateral inhibition the dip is deep. B: depth of the dip between the two peaks (1 − valley/peak) as a function of separation; solid line σ = 1 mm (like the fingertip), dashed line σ = 8 mm (like the back); dots mark the separation at which the dip exceeds 10 %, taken as the two-point threshold. Lateral inhibition reduces the two-point threshold slightly, while the two-point threshold is mainly proportional to the receptive field width.](./plots/two-point.py)

## 39.5. Mechanosensation

### 39.5.1. A Four-Level Framework for Mechanosensation

From the force on the skin to the formation of touch, we can distinguish four levels:

| Level | What it does | In touch |
|---|---|---|
| 1. External stimulus | The physical input | Pressure, vibration, shear, stretch of the skin |
| 2. Mechanical computation | Preprocessing of the mechanical signal by accessory structures: filtering, amplification, conversion of one mechanical quantity into another | Viscoelastic filtering by the dermis and capsules; force transmission by Merkel cells and hair follicles |
| 3. Cellular coding | Transduction channels convert membrane deformation into receptor potentials, and the encoder converts these into action potentials | Opening and inactivation of Piezo2; firing and adaptation at the first node of Ranvier |
| 4. Central processing | Integration and interpretation by relay nuclei and cortex | Dorsal column nuclei, ventral posterior nucleus of the thalamus, somatosensory cortex (Section 39.6) |

The differences in adaptation among mechanoreceptors arise mainly at levels 2 and 3: the capsule of the Pacinian corpuscle rapidly dissipates sustained tension, and together with the fast inactivation of Piezo2 and strong adaptation of the encoder, it reports only transient vibration; the collagen fibers of Ruffini endings transmit tension throughout a stretch, so that the ending fires continuously. The same framework applies to other mechanical senses and to vision: the traveling wave on the cochlear basilar membrane and the mechanics of the hair bundle are the "mechanical computation" of hearing ([7.14.42](/7.14.42)), and image formation by the cornea and lens is the "optical preprocessing" of vision ([7.14.41](/7.14.41)). By contrast, olfaction and taste have almost no level 2: molecules bind directly to receptors, and stimuli are distinguished mainly by combinatorial coding across a large number of receptors and by central decoding ([7.14.43](/7.14.43)).

### 39.5.2. Transduction by Piezo2

The main transduction channel for light touch in mammalian skin is Piezo2 (Coste et al., 2010; Ranade et al., 2014); Pacinian corpuscles, Meissner corpuscles, Merkel disks, hair follicle receptors, and the afferent endings of **muscle spindles** and **Golgi tendon organs** all depend on it. The structure and gating of Piezo channels were discussed in [7.6.25](/7.6.25#sec-25.6.2); here we list only the conclusions needed for physiology:

- Structure: a homotrimer in which each subunit has 38 transmembrane helices; three curved blades surround the central pore like a propeller and bend the surrounding membrane into a nanoscale bowl. Membrane tension flattens the blades and increases the projected area, and the long beam helices transmit this motion to the pore like levers, opening it. Because the change in projected area is large, Piezo opens at the low tensions of the physiological range (a few $\mathrm{mN\,m^{-1}}$) and is a sensitive tension sensor.
- Inactivation: Piezo2 inactivates within a few milliseconds, faster than Piezo1. Inactivation is determined jointly by the helices in the pore, the C-terminal extracellular domain, and other regions; some point mutations slow Piezo inactivation, for example mouse Piezo1 M2241R (corresponding to M2225R in human hereditary xerocytosis), and certain gain-of-function mutations of human *PIEZO2* cause distal arthrogryposis. Fast inactivation is one of the molecular bases of rapid adaptation.
- Loss of function: patients with biallelic loss-of-function mutations in *PIEZO2* have severely impaired vibration sense, fine tactile discrimination, and joint position sense, and have difficulty performing coordinated movements with the eyes closed, but pain and thermal sensation are largely normal (Chesler et al., 2016). This shows that Piezo2 is the main transduction molecule for light touch and proprioception but is not required for nociception (it does act in touch-evoked pain after inflammation, [7.14.40](/7.14.40)).

These receptors share the same transduction molecule; they differ in how force is delivered to the channel. The channel "sees" only the deformation of the membrane, and the accessory structures of level 2 determine which stimuli can cause deformation.

### 39.5.3. Mechanoreceptors of the Skin

| Receptor | Location and structure | Afferent fiber | Adaptation | Receptive field | Most sensitive stimulus |
|---|---|---|---|---|---|
| Free nerve ending | Skin and tissues throughout the body | Aδ, C | Mostly slow | Variable | Crude touch, pressure; thermal and noxious stimuli |
| Meissner corpuscle | Dermal papillae of glabrous skin; several branched endings sandwiched between stacked flattened cells in a capsule | Aβ (rapidly adapting type I) | Fast | Small, sharp borders | Low-frequency vibration (about $5$–$50\,\mathrm{Hz}$), edges, slip between skin and object |
| Merkel disk | Complex of Merkel cells in the basal epidermis and afferent endings | Aβ (slowly adapting type I) | Slow | Small | Sustained pressure, shape and texture, points and edges |
| Hair follicle receptor | Lanceolate endings around the hair follicle | Aβ, Aδ, C | Fast | Medium | Hair deflection, motion of objects across the body surface |
| Ruffini ending | Deep dermis and joint capsule; branched endings in a capsule intertwined with collagen fibers and anchored at both ends | Aβ (slowly adapting type II) | Slow | Large, indistinct borders | Skin stretch, joint angle |
| Pacinian corpuscle | Deep dermis and subcutis, periosteum, mesentery; $1$–$2\,\mathrm{mm}$ long, a single unmyelinated ending surrounded by $20$–$70$ concentric lamellae of flattened cells with fluid between layers | Aβ (rapidly adapting type II) | Very fast | Large | High-frequency vibration (about $40$–$800\,\mathrm{Hz}$, optimum about $250\,\mathrm{Hz}$) |

The glabrous skin of one hand has about $17\,000$ mechanosensory afferent fibers, of which rapidly adapting type I make up about $43\,\%$, slowly adapting type I about $25\,\%$, rapidly adapting type II about $13\,\%$, and slowly adapting type II about $19\,\%$ (Johansson and Vallbo, 1979). The four classes of fibers divide the work. When we pick up a cup, Merkel disks report the position of contact and the shape of the rim, Meissner corpuscles report tiny slips and reflexively increase grip force, Pacinian corpuscles report the vibration transmitted when the cup is set on the table, and Ruffini endings and muscle spindles report the posture of the fingers. Merkel cells themselves also express Piezo2 and, together with the afferent ending, generate slowly adapting firing (Woo et al., 2014; Maksimovic et al., 2014). Hairy skin also contains a class of low-threshold C-fiber mechanoreceptors that respond most strongly to gentle stroking and are related to the affective component of touch.

### 39.5.4. Viscoelastic Filtering

Why, though all use Piezo2 for transduction, is the Pacinian corpuscle sensitive only to fast vibration, whereas the Ruffini ending can report sustained stretch? The answer lies in the **viscoelasticity** of tissue. Collagen and elastic fibers behave like springs (stress $\sigma = E\varepsilon$), tissue fluid like a dashpot ($\sigma = \eta\dot\varepsilon$), with relaxation time $\tau = \eta/E$. A spring and dashpot in series form a **Maxwell viscoelastic liquid**, and in parallel a Kelvin–Voigt solid; the constitutive equations of both are given in [7.6.22](/7.6.22#sec-22.7.1).

**Formula 39.5.1 (Transfer Function of Viscoelastic Elements)** For a sinusoidal deformation $\varepsilon = \varepsilon_0\mathrm{e}^{\mathrm{i}\omega t}$, the ratio of stress to deformation in a Maxwell element is $E\,H(\omega)$,

$$
H(\omega) = \frac{\mathrm{i}\omega\tau}{1 + \mathrm{i}\omega\tau}, \qquad \lvert H(\omega)\rvert = \frac{\omega\tau}{\sqrt{1 + (\omega\tau)^2}}, \tag{39.4}
$$

a first-order high-pass filter: for $\omega\tau \ll 1$, $\lvert H\rvert \approx \omega\tau \to 0$, slow deformations flow away through the dashpot and transmit almost no stress; for $\omega\tau \gg 1$, $\lvert H\rvert \to 1$, fast deformations have no time to flow away and the stress is transmitted almost without attenuation. When a sinusoidal force is applied to a Kelvin–Voigt element, the ratio of deformation to force is $1/[E(1 + \mathrm{i}\omega\tau)]$, a first-order low-pass filter. When $N$ mutually unloaded Maxwell units are in series, the transfer function is approximately the product over the layers,

$$
H_{\mathrm{tot}}(\omega) = \prod_{k=1}^{N}\frac{\mathrm{i}\omega\tau_k}{1 + \mathrm{i}\omega\tau_k}, \tag{39.5}
$$

and the slope on the low-frequency side steepens as the number of layers increases ($20\,\mathrm{dB}$ per decade for each layer).

In the time domain this corresponds to the response to a step deformation: the stress in a Maxwell element jumps at the step and then decays to zero as $\mathrm{e}^{-t/\tau}$, reporting only "change"; under a step force the deformation of a Kelvin–Voigt element gradually approaches a steady state as $1 - \mathrm{e}^{-t/\tau}$ and stays there, reporting "state". Which filter applies depends on which mechanical quantity the ending senses:

- The dermis is high-pass for pressure transmitted to deeper layers: slow pressure is dissipated by the flow of tissue fluid, and only fast pressure reaches the deep Pacinian corpuscles effectively; the superficial Meissner corpuscles and Merkel disks are filtered less.
- The lamellae of the Pacinian corpuscle add a further set of high-pass filters beyond the dermis, so it is sensitive almost only to fast vibration. Inside the capsule, the capacitance of the ending's membrane and the encoder form a low-pass filter, so the whole is a band-pass with a U-shaped threshold versus frequency and an optimum of about $250\,\mathrm{Hz}$ (panel B).
- The Ruffini ending senses the tension in the collagen fibers passing through its capsule, that is, the overall deformation of the skin; only slow stimuli can deform the skin appreciably, so to it the tissue is low-pass, making it a tension sensor for skin stretch and joint angle.
- The Meissner corpuscle senses the relative sliding and shear between lamellae; it adapts rapidly to steps yet does not respond to the high frequencies that drive Pacinian corpuscles, and it works in the low-frequency vibration range of about $5$–$50\,\mathrm{Hz}$.

Eq. (39.5) gives only the qualitative trend. In a real corpuscle the lamellae are coupled through fluid and load one another; the mechanical model of Loewenstein and Skalak (1966) couples the elasticity of the lamellae to the flow of interlamellar fluid and calculates that the capsule rapidly attenuates sustained pressure on its way to the core, while fast displacements pass in almost undiminished; the measured low-frequency slope is much shallower than the product of independent layers predicts.

![Viscoelastic filtering. A: gain |H| = (ωτ/√(1 + (ωτ)²))^N of N identical Maxwell elements in series (N = 1, 5, 20, 60, frequency in units of 1/τ), and gain 1/√(1 + (ωτ)²) of a force-driven Kelvin–Voigt element (low-pass, dashed line); dotted line marks −3 dB. The more layers, the steeper the high-pass and the higher the corner frequency. B: schematic tuning curve of a Pacinian corpuscle: threshold amplitude = 1/|H_capsule H_encoder|, with the capsule taken as an effective second-order high-pass (corner 120 Hz) and the ending membrane and encoder as a first-order low-pass (corner 300 Hz), with the minimum of the intact corpuscle as 0 dB. The threshold of the intact corpuscle is U-shaped with an optimum of about 250 Hz; after removal of the capsule only the low-pass remains, and sensitivity to low-frequency stimuli is greatly increased.](./plots/viscoelastic-filter.py)

**Example 39.5.1 (Decapsulation Experiment)** Loewenstein and Mendelson (1965) used microdissection on Pacinian corpuscles of the cat mesentery to strip most of the lamellae of the capsule, leaving only the bare ending, and compared the responses to a step compression before and after stripping. The intact corpuscle produces one brief generator potential and one action potential at the onset and again at the removal of compression; after removal of the capsule, the generator potential persists during compression and declines slowly, and the "off response" at release disappears, showing that the off response comes from the elastic recoil of the capsule, and that the rapid decay of the generator potential comes from the mechanical filtering of the capsule (level 2). But the bare ending still fires only one or a few action potentials: the encoder at the first node of Ranvier itself adapts strongly (level 3). Rapid adaptation therefore has two independent components, mechanical and electrical.

![Rapid and slow adaptation (schematic model). A: compression rises within 10 ms, is held for 400 ms, and is removed within 10 ms. B: generator potential (normalized). Intact Pacinian corpuscle: the capsule acts as an effective high-pass (τ = 3 ms) and the ending senses the magnitude of core displacement, so a brief potential is produced at the onset and at the end of compression; capsule removed: the bare ending follows the compression, with slow viscous creep (40 % decline over τ = 150 ms) and no off response; slowly adapting ending (Merkel or Ruffini type): low-pass (τ = 15 ms) plus a small dynamic component. C: action potentials. The encoder is a leaky integrate-and-fire model with a spike-triggered adaptation current; adaptation at the first node of Ranvier of the Pacinian corpuscle is strong, and that of the slowly adapting ending is weak. The intact corpuscle fires once at the onset and once at the end; after capsule removal it fires only at the onset, and the sustained generator potential causes only a few action potentials because of encoder adaptation; the slowly adapting ending fires throughout the compression with slowly decreasing frequency.](./plots/adaptation.py)

## 39.6. Central Pathways of Somatosensation

### 39.6.1. Two Ascending Systems

After somatosensory signals enter the spinal cord through the dorsal roots, they ascend in two systems.

**Definition 39.6.1 (Dorsal Column–Medial Lemniscal System and Anterolateral System)** Primary afferent fibers that ascend in the ipsilateral dorsal column after entering the spinal cord, synapse in the gracile and cuneate nuclei of the medulla, and whose second-order fibers cross to the opposite side, form the medial lemniscus, ascend to the ventral posterolateral nucleus of the thalamus, and then project to the somatosensory cortex, constitute the **dorsal column–medial lemniscal system**. Primary afferent fibers that synapse in the dorsal horn of the spinal cord, and whose second-order fibers cross to the opposite side through the anterior white commissure within one or two segments and ascend in the anterolateral funiculus of the spinal cord to the brainstem and thalamus, constitute the **anterolateral system**.

| | Dorsal column–medial lemniscal system | Anterolateral system |
|---|---|---|
| Information carried | Fine touch, precise localization and intensity discrimination of touch, vibration, joint position and movement (conscious proprioception) | Pain, thermal sensation, crude touch and pressure, itch, sexual sensation |
| Primary fibers | Thick myelinated fibers (Aβ, Aα) | Thin fibers (Aδ, C) |
| Site of decussation | Medulla (decussation of the medial lemniscus) | Spinal cord, near the segment of entry |
| Conduction velocity | $30$–$110\,\mathrm{m\,s^{-1}}$ | About $8$–$40\,\mathrm{m\,s^{-1}}$ |
| Spatial localization | Precise, with strict somatotopic arrangement | Crude |
| Thalamic termination | Ventral posterolateral nucleus (face via the trigeminal nerve to the ventral posteromedial nucleus) | Ventral posterolateral nucleus, plus the intralaminar nuclei and brainstem reticular formation |

Fibers in the dorsal column are arranged by body part: fibers from the lower body are medial (gracile fasciculus) and those from the upper body are lateral (cuneate fasciculus); after the synapse, the arrangement rotates in the medial lemniscus, so that at the thalamus the lower body is lateral and the upper body medial. The two systems decussate at different sites, so a hemisection of the spinal cord shows a typical clinical dissociation: loss of fine touch and proprioception on the same side below the lesion, and loss of pain and thermal sensation on the opposite side (Brown-Séquard syndrome).

### 39.6.2. Somatosensory Cortex and Somatotopy

The ventral posterior nuclei of the thalamus project to the primary somatosensory cortex (S1, Brodmann areas 3a, 3b, 1, and 2) in the postcentral gyrus. Area 3a receives mainly proprioceptive input and area 3b cutaneous input; neurons in areas 1 and 2 have larger receptive fields and relate to texture and to the size and shape of objects, respectively; S1 projects in turn to the secondary somatosensory cortex (S2) in the upper bank of the lateral sulcus and to association areas of the parietal lobe (areas 5 and 7), where touch is integrated with visual and motor information.

The parts of the body are arranged in an orderly "map" in S1 (somatotopy; Penfield drew the human map by electrical stimulation during neurosurgery): the contralateral body is laid out inverted from medial to lateral, with the foot and leg on the medial surface of the hemisphere and the trunk, upper limb, hand, face, and tongue successively more lateral. The area each part occupies on the map is unrelated to the actual size of the body part and proportional to the density of receptors: the lips, tongue, and fingers occupy large areas and the trunk only a thin strip. Mountcastle (1957) found in cat S1 that an electrode inserted perpendicularly from the cortical surface meets neurons with the same receptive field location and the same modality (slowly or rapidly adapting), whereas moving the electrode horizontally changes them, which led to the concept of the cortical column. The map is not fixed: after amputation of a monkey's finger, the cortical region that represented it is taken over by input from adjacent fingers (Merzenich et al., 1984), which is one neural basis of "phantom limb" sensation after amputation.

### 39.6.3. Two-Point Discrimination Threshold

**Definition 39.6.2 (Two-Point Discrimination Threshold)** When two points stimulate the skin simultaneously, the smallest distance between them at which the subject perceives two points rather than one is called the **two-point discrimination threshold**.

The two-point discrimination threshold is the classic measure of the spatial resolution of touch: about $2\,\mathrm{mm}$ ($1$–$3\,\mathrm{mm}$) at the fingertip, similar at the lips, about $10\,\mathrm{mm}$ on the palm, and about $30$–$40\,\mathrm{mm}$ on the back. It is determined by the density of receptors and the size of receptive fields, and is sharpened by lateral inhibition at each relay (see the figure in Section 39.4.2); the two-point thresholds of different regions are roughly related to the inverse of the area of the region's representation in S1.

## 39.7. Proprioception

**Definition 39.7.1 (Proprioception)** The sense of the position, movement, and force of the parts of the body, that is, knowing without vision where a limb is and how it is moving, is called **proprioception**.

The receptors of proprioception are mainly **muscle spindles** (muscle length and its rate of change) and **Golgi tendon organs** (muscle tension), and secondarily receptors in joint capsules and ligaments and cutaneous stretch receptors (Ruffini endings). Joint receptors mostly fire strongly only at the two ends of the range of joint motion, so most information about joint angle comes from muscle spindles, and vibrating a tendon (activating the spindles) gives the subject an illusion that the limb is moving. Proprioceptive signals ascend by two routes: through the dorsal column–medial lemniscal system to the thalamus and cortex, forming the conscious sense of position; and through the spinocerebellar tracts to the cerebellum, for motor coordination that does not enter consciousness ([7.14.45](/7.14.45)). Patients lacking Piezo2 have almost no proprioception but can still learn to walk with the help of vision, showing that the central nervous system can partly compensate with other senses. The structure, responses, and reflexes of muscle spindles and Golgi tendon organs are discussed in [7.14.44](/7.14.44).

## 39.8. Evolution and Comparison

Mechanosensation may be the oldest of the senses: bacteria already use the mechanically gated channels MscS and MscL as osmotic safety valves ([7.6.25](/7.6.25#sec-25.5)), whereas animal touch, hearing, and balance repeatedly use a few classes of channels combined with very different accessory structures.

Touch channels of nematodes. *Caenorhabditis elegans* has six touch receptor neurons along its body, and the response to light touch of the body is to move away, forward or backward. A genetic screen by Chalfie and colleagues for touch-defective mutants identified the *mec* genes; MEC-4 and MEC-10 belong to the DEG/ENaC (degenerin/epithelial sodium channel) family, and in in vivo recordings light touch evokes, in under a millisecond, a current through a pore formed by MEC-4 (O'Hagan et al., 2005). The channel is linked to the extracellular matrix and to specialized 15-protofilament microtubules, a "tethered" mode of mechanotransduction.

NOMPC of *Drosophila* and insect sensilla. Mechanosensation in *Drosophila* bristles depends on the TRP family member NOMPC (TRPN1), whose 29 ankyrin repeats connect the channel to **microtubules** and transmit force like a compressed spring ([7.6.25](/7.6.25#sec-25.6.3)). The insect exoskeleton is rigid, and the touch organs are sensilla that pass through the cuticle: trichoid sensilla are excited when the hair is deflected; campaniform sensilla are thin domes in the cuticle that sense the strain of the cuticle itself, densely distributed at leg joints and at the base of the halteres of Diptera, and serve as the insect's "strain gauges"; chordotonal organs (such as Johnston's organ in the antenna) sense stretch and vibration between segments and are also used for hearing. The exoskeleton as an "accessory structure" determines that insects sense contact by measuring strain rather than pressure.

The lateral line of fish and amphibians. The **lateral line** system on the body surface and head of fish is composed of neuromasts, in each of which the hair bundles of **hair cells** extend into a gelatinous cupula. The cupula of a superficial neuromast is directly exposed to the water and is deflected by the flow, reporting flow velocity; canal neuromasts are buried in fluid-filled canals under the skin, and the mechanics of the canal makes them sensitive to the acceleration of the water (that is, the pressure gradient along the canal). The same hair cells, combined with two kinds of accessory structures, yield two filtering properties. The lateral line is used in schooling, rheotaxis, predator avoidance, and prey capture, and its hair cells are homologous to those of the inner ear ([7.14.42](/7.14.42)).

The star-nosed mole. The North American star-nosed mole (*Condylura cristata*) forages in dark wet soil and has 22 fleshy appendages at the tip of its nose, whose surface is densely covered with about $25\,000$ Eimer's organs, innervated by more than $10^5$ myelinated afferent fibers, several times the number of tactile fibers in the human hand (Catania). It scans rapidly with the appendages, and the lowest, central pair acts as a "tactile fovea" and occupies a disproportionately large area of somatosensory cortex; from touching prey to eating it takes as little as about $120\,\mathrm{ms}$, close to the limit of neural conduction and processing speed.

The bill of the duck. In ducks, which filter-feed and forage by touch, the bill is densely supplied with Grandry corpuscles and Herbst corpuscles (the latter resemble Pacinian corpuscles and are also multilayered-capsule rapidly adapting receptors); compared with birds that forage visually, the proportion of mechanosensory neurons in the trigeminal ganglion of ducks is greatly increased, and they commonly express Piezo2 (Schneider et al., 2014).

Whiskers and barrel cortex of rodents. Rats and mice actively sweep their whiskers back and forth at about $5$–$15\,\mathrm{Hz}$ (active touch), and the mechanoreceptors in the follicle of each whisker project through the trigeminal pathway to a separate cell cluster in S1 called a barrel (Woolsey and Van der Loos, 1970): the arrangement of barrels corresponds one to one to the arrangement of whiskers on the snout, the clearest example of somatotopy. If a whisker is removed, the corresponding barrel shrinks in development and adjacent barrels expand, the same as the cortical plasticity in Section 39.6.2.

Comparison. From nematodes to mammals, mechanotransduction channels belong to a few families (DEG/ENaC, TRP, Piezo, TMC), and the great differences among receptors arise mainly from the "mechanical computation" level: capsules, hairs, cupulae, cuticular domes, canals, and whiskers each select the meaningful mechanical signals in the environment and convert them into membrane deformation that channels can sense. This echoes the question at the beginning of the chapter: the morphological diversity of mechanoreceptors is dictated by the fact that mechanical signals must first undergo physical preprocessing.

## Summary

| Topic | Key points |
|---|---|
| Receptors (Definition 39.1.1) | Five classes: mechanical, thermal, nociceptive, electromagnetic, chemical; by location, exteroceptors, interoceptors, proprioceptors |
| Labeled line principle (Definition 39.1.2) | Modality is determined by the pathway, not the stimulus; a single receptor is univariant |
| Six principles of transduction | Transduction, modality specificity, two classes of mechanisms (GPCR and mechanically gated channels), amplification and dynamic range, action potential coding, central interpretation |
| Receptor potential (Definition 39.2.1) | Graded local potential; Eq. (39.1) first linear then saturating; frequency coding, recruitment, and adaptation extend the dynamic range |
| Psychophysics (Formula 39.2.1, Definition 39.2.2) | Weber fraction $\Delta S/S$ constant, $\psi \propto \ln S$; Stevens $\psi \propto S^{\beta}$, from $0.33$ for brightness to $3.5$ for electric shock |
| Adaptation (Definition 39.3.1) | Slowly adapting receptors report state, rapidly adapting receptors report change; mechanisms at three levels: accessory structure, transduction molecule, encoder |
| Receptive fields and lateral inhibition (Definitions 39.4.1, 39.4.2) | Density determines receptive field size, lateral inhibition sharpens borders; two-point threshold proportional to receptive field width |
| Four-level framework (Section 39.5.1) | Stimulus → mechanical computation → cellular coding → central processing; adaptation differences arise at levels 2 and 3 |
| Piezo2 | Trimer with curved blades, opens at low tension, inactivates within milliseconds; its loss abolishes light touch and proprioception, sparing pain |
| Cutaneous receptors | Meissner (RA I, low-frequency vibration and slip), Merkel (SA I, pressure and shape), Ruffini (SA II, stretch), Pacinian (RA II, vibration near $250\,\mathrm{Hz}$), hair follicle, free endings |
| Viscoelastic filtering (Formula 39.5.1) | Maxwell: $H = \mathrm{i}\omega\tau/(1 + \mathrm{i}\omega\tau)$, high-pass; Kelvin–Voigt: low-pass; cascading steepens the high-pass; the decapsulation experiment (Example 39.5.1) separates mechanical and electrical adaptation |
| Central pathways (Definition 39.6.1) | Dorsal column–medial lemniscal system: fine touch and proprioception, decussation in the medulla; anterolateral system: pain, temperature, and crude touch, decussation in the spinal cord |
| Cortex | Somatotopy and columns in S1, with representation area proportional to receptor density, and plastic; two-point threshold (Definition 39.6.2) about $2\,\mathrm{mm}$ at the fingertip and $30$–$40\,\mathrm{mm}$ on the back |
| Evolution | A few channel families (DEG/ENaC, TRP, Piezo, TMC) combined with diverse accessory structures: nematode MEC-4, *Drosophila* NOMPC, campaniform sensilla, lateral line, star-nosed mole, duck bill, whisker–barrel cortex |

## Questions

1. Electrical stimulation of a person's auditory nerve produces the perception of sound; stimulating a cutaneous nerve of a finger with the same current produces a prickling or tingling sensation. Explain with the labeled line principle, and say what this implies for cochlear implants.

   **Answer** The modality of a sensation is determined by the part of the central nervous system to which the activated fibers project, independent of the physical form of the stimulus (Definition 39.1.2). Electric current is not an adequate stimulus for either kind of fiber, but auditory nerve fibers lead to the auditory centers, so a sound results; cutaneous nerves lead to somatosensory centers, producing touch or pain. Cochlear implants exploit exactly this: they need not restore hair cells, only use an electrode array to activate auditory nerve fibers at different sites according to frequency position (place coding in the cochlea, [7.14.42](/7.14.42)), and the brain interprets these electrical stimuli as sounds of different pitch.

2. Suppose the receptor potential satisfies Eq. (39.1) with $n = 1$. When the stimulus intensity increases from $0.1S_{1/2}$ to $10S_{1/2}$, from what to what does the receptor potential change? How does it relate to $\ln S$ over this range?

   **Answer** $V_{\mathrm{r}}/V_{\max} = S/(S + S_{1/2})$: it is $0.091$ at $0.1S_{1/2}$, $0.5$ at $S_{1/2}$, and $0.91$ at $10S_{1/2}$. A hundredfold increase in intensity raises the potential from about 9 % to 91 %. On a logarithmic axis, $\mathrm{d}V_{\mathrm{r}}/\mathrm{d}\ln S = V_{\max}\,S S_{1/2}/(S + S_{1/2})^2$, which is $V_{\max}/4$ at $S = S_{1/2}$ and falls to about $0.08V_{\max}$ at the two ends; hence over about one order of magnitude in the middle, $V_{\mathrm{r}}$ is approximately linear in $\ln S$. This is a cellular-level explanation of Fechner's logarithmic law, though the two ends deviate from it.

3. Use Formula 39.5.1 to explain why, after stripping the capsule, the generator potential of a Pacinian corpuscle in response to sustained compression no longer decays rapidly, yet the action potentials are still only one or a few. If tetrodotoxin is then used to block the $\ce{Na+}$ channels of the ending, what happens to the generator potential?

   **Answer** The capsule is a set of Maxwell-type high-pass filters: sustained compression is a low-frequency stimulus, $\lvert H\rvert \approx \omega\tau \to 0$, and the deformation reaching the core vanishes within a few milliseconds as interlamellar fluid flows, so the generator potential decays rapidly; after stripping the capsule, the sustained deformation acts directly on the ending membrane, and Piezo2 channels (though partly inactivated) maintain a more sustained potential. But action potentials are generated at the first node of Ranvier, where sustained depolarization inactivates voltage-gated $\ce{Na+}$ channels and activates slow $\ce{K+}$ currents, so the encoder itself adapts rapidly and only a few action potentials are still fired (Example 39.5.1). Tetrodotoxin blocks voltage-gated $\ce{Na+}$ channels and not mechanically gated channels, so the action potentials vanish while the generator potential is largely preserved; this is the classic experiment showing that generator potentials and action potentials arise from different mechanisms.

4. A patient has a right-sided hemisection of the spinal cord at thoracic segment 10. What sensations will he lose in the right and left legs, and why?

   **Answer** The primary fibers of the dorsal column–medial lemniscal system ascend in the ipsilateral dorsal column and decussate only in the medulla, so after the right dorsal column is cut, fine touch, vibration sense, and joint position sense are lost in the right leg (ipsilateral, below the level of the lesion). The fibers of the anterolateral system cross to the opposite side within one or two segments of entry and ascend there, so the right anterolateral funiculus carries fibers from the left side of the body; pain and thermal sensation are lost in the left leg (contralateral), while those in the right leg are preserved (their fibers have already crossed to the left). In addition, the right lateral corticospinal tract is cut, and the right leg shows upper motor neuron paralysis ([7.14.45](/7.14.45)). This is Brown-Séquard syndrome.

5. (Open question) The nose of the star-nosed mole, the bill of the duck, and the lateral line of fish all use the strategy of "accessory structure plus a few transduction channels". From the standpoint of signal processing, why is mechanosensation worth investing so much structure in preprocessing, whereas olfaction hardly is?

   **Answer** Key points: mechanical signals have few dimensions (amplitude, frequency, direction, position) and well-defined physical properties (they can be filtered by springs, dampers, resonance, and canals), so passive structures can pick out the useful components (a frequency band, velocity or acceleration, a direction) before transduction, at almost no energy cost and with very short delay, and can protect channels from saturation; mechanical signals also often demand fast reactions (escape, grip, balance), leaving the central nervous system no time for complex computation. Chemical signals have a very large number of dimensions (each molecule is one dimension), molecules cannot easily be distinguished by physical structure, and must be handled by binding to a large number of different receptors, with the central nervous system decoding by combinatorial coding and learning; moreover, the timing demands of odors are usually less stringent. The two senses thus place "computation" in different places: mechanosensation in peripheral structures, olfaction in central neural circuits.
