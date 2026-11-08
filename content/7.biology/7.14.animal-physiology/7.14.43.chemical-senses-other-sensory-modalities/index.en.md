---
title: Chemical Senses and Other Sensory Modalities
description: "The olfactory epithelium and the turnover of olfactory receptor neurons; the olfactory receptor gene family, the Golf–cAMP–CNG pathway and the Ca²⁺-activated Cl⁻ current; olfactory thresholds and the narrow intensity range; one receptor per neuron and convergence onto glomeruli; olfactory bulb circuits, contrast enhancement and decorrelation by lateral inhibition, and locking to respiration; combinatorial coding and its capacity; divergence and convergence in piriform cortex; the three central olfactory pathways and olfactory adaptation; the vomeronasal organ and pheromones; taste buds and the three types of taste cells; receptors for the five basic tastes (T1R, T2R, OTOP1, ENaC) and ATP as transmitter; labeled-line coding of taste and flavor; the gustatory pathway and conditioned taste aversion; evolution and other modalities: insect ionotropic olfactory receptors, multi-receptor neurons in nematodes, expansion and loss of receptor repertoires; passive and active electroreception, electric images and the jamming avoidance response; magnetoreception; a comparison of animal sensory worlds."
source_hash: 0f4e251f383e
---

The chemical senses are the oldest senses: long before nervous systems existed, bacteria could swim along chemical gradients (**chemotaxis**, [7.6.35](/7.6.35)). Animals use smell to sense molecules that arrive from a distance in air or water, taste to examine the food that enters the mouth, and specialized organs such as the vomeronasal organ to recognize signals from conspecifics. Compared with vision, hearing, and touch, the chemical senses involve almost no physical preprocessing: molecules bind directly to receptors, so the layer of "mechanical computation" in the four-level framework of Chapter 39 is largely missing ([7.14.39](/7.14.39#sec-39.5.1)), and stimuli are discriminated by combinatorial coding across many receptors and by decoding in the central nervous system. This chapter first covers the periphery, the olfactory bulb, and the central pathways of olfaction, then the vomeronasal organ and pheromones, and taste, and finally the evolution of chemical senses and sensory modalities that humans lack, such as electroreception and magnetoreception. The molecular mechanisms of G protein–coupled receptors and second messengers are treated in biochemistry ([7.1.14](/7.1.14)).

## 43.1. The Periphery of Olfaction

### 43.1.1. The Olfactory Epithelium

The human olfactory epithelium lies at the roof of the nasal cavity (the superior nasal concha and the upper part of the septum) and has an area of only about $2$–$5\,\mathrm{cm}^2$. During quiet breathing most inhaled air does not pass over it; only vigorous sniffing sends the airflow upward and carries more odorant molecules to the epithelium. The olfactory epithelium of the dog is more than an order of magnitude larger than that of humans, and the dog has one to two orders of magnitude more olfactory receptor neurons, with a correspondingly greater sensitivity.

**Definition 43.1.1 (Olfactory Epithelium)** The pseudostratified epithelium in the nasal cavity that consists of olfactory receptor neurons, supporting cells, and basal cells, is covered with mucus, and detects odorant molecules is called the **olfactory epithelium**.

The three cell types have distinct roles:

- Olfactory receptor neurons are bipolar neurons. The dendritic tip of each swells into an olfactory knob from which a dozen or so immotile cilia extend and lie flat in the mucus; the olfactory receptors are in the ciliary membrane. The unmyelinated axons at the base pass in bundles through the cribriform plate of the ethmoid bone, form the olfactory nerve (I), and terminate in the olfactory bulb.
- Supporting cells resemble glia: they ensheath the receptor neurons in the epithelium, maintain the ionic composition of the mucus, and metabolize and clear incoming chemicals with **cytochrome P-450** enzymes.
- Basal cells are **stem cells** that divide throughout life and replenish the receptor neurons. Receptor neurons are directly exposed to environmental chemicals and pathogens and live only about 1–2 months; they are among the few mammalian neurons that are renewed throughout life, and each newborn neuron must reconnect its axon to the correct position in the olfactory bulb.

Molecules that can be smelled usually have a small molecular mass (below about $300\,\mathrm{Da}$), are volatile, and are partly soluble in mucus. Odorant-binding proteins in the mucus carry the odorants to the receptors. Odors are inhaled through the nostrils (orthonasal olfaction), but during chewing and swallowing they also travel upward from the back of the mouth through the nasopharynx (retronasal olfaction), which is the main source of "flavor" (Section 43.4.3).

### 43.1.2. Olfactory Receptors and Transduction

Buck and Axel (1991; Nobel Prize 2004) discovered that the olfactory receptors form a very large family of **G protein–coupled receptors**. The mouse has about $1100$ functional olfactory receptor genes, roughly 5 % of its protein-coding genes and the largest mammalian **gene family**; humans have about $350$–$400$ functional genes and roughly as many **pseudogenes**.

All the different receptors use the same intracellular pathway:

1. An odorant binds to a receptor in the ciliary membrane and activates the olfactory-specific G protein $\mathrm{G_{olf}}$;
2. $\mathrm{G_{olf}}$ activates type III **adenylyl cyclase**, and the concentration of **cyclic AMP** rises;
3. cAMP opens cyclic nucleotide–gated (CNG) channels, and $\ce{Na+}$ and $\ce{Ca^2+}$ flow in;
4. The entering $\ce{Ca^2+}$ opens $\ce{Ca^2+}$-activated $\ce{Cl-}$ channels (ANO2). Olfactory receptor neurons keep their intracellular $\ce{Cl-}$ high with the $\ce{Na+}$–$\ce{K+}$–$2\ce{Cl-}$ cotransporter (a **symporter**), so $\ce{Cl-}$ flows out down its gradient and causes further **depolarization**; this step amplifies the current severalfold;
5. The **receptor potential** spreads electrotonically to the soma and axon hillock and triggers action potentials.

This pathway resembles the **phototransduction** cascade of rods ([7.14.41](/7.14.41#sec-41.2.4)) but with the opposite sign: in rods a decrease of the **second messenger** closes CNG channels and causes **hyperpolarization**, whereas in olfactory neurons an increase of the second messenger opens the channels and depolarizes the cell. The **negative feedback** is designed alike: entering $\ce{Ca^2+}$ binds **calmodulin**, lowers the sensitivity of the CNG channel to cAMP, and activates the phosphodiesterase PDE1C and CaMKII (which inhibits adenylyl cyclase), so that the response weakens under sustained stimulation; this is **adaptation** at the receptor level.

Besides the classical olfactory receptors, the olfactory epithelium contains a few other receptor families, such as the trace amine–associated receptors (TAARs) that sense amines. For example, mouse TAAR4 senses 2-phenylethylamine in predator urine and elicits instinctive avoidance without learning.

**Example 43.1.1** The human olfactory threshold for methanethiol is about $1/25$ trillion gram per milliliter of air, that is, $4\times10^{-14}\,\mathrm{g\,mL^{-1}}$. The molar mass of methanethiol is $48\,\mathrm{g\,mol^{-1}}$, so one milliliter of air contains $4\times10^{-14}/48\times6.0\times10^{23} \approx 5\times10^8$ molecules; compared with about $2.5\times10^{19}$ molecules per milliliter of air, this is a volume fraction of about $2\times10^{-11}$. Because the threshold is so low, thiols such as methanethiol are added to odorless natural gas to warn of leaks.

Another feature of olfaction is its narrow intensity range: many odors reach their maximal subjective intensity at 10–50 times the threshold concentration, whereas the intensity ranges of vision (including adaptation, [7.14.41](/7.14.41#sec-41.2.5)) and hearing exceed $10^{10}$ and $10^{12}$ fold, respectively. This fits the main task of olfaction: to judge whether an odor is present and what it is, not to measure its concentration precisely.

### 43.1.3. One Neuron, One Receptor, and the Olfactory Glomerulus

Each olfactory receptor neuron chooses just one of the thousand or so receptor genes to express, and expresses only one **allele** of it. The choice is random, and the receptor protein that is chosen in turn prevents the activation of the other receptor genes by feedback. The olfactory epithelium therefore consists of about a thousand types of neurons, each with a single receptor. Neurons expressing the same receptor are scattered through a large zone of the epithelium, intermixed with other types, but their axons converge on the same location in the olfactory bulb.

**Definition 43.1.2 (Olfactory Glomerulus)** The spherical neuropil, about $50$–$100\,\mu\mathrm{m}$ in diameter, in the superficial layer of the olfactory bulb in which the axon terminals of many olfactory receptor neurons form synapses with the dendrites of a few mitral and tufted cells is called an **olfactory glomerulus**. The axons of neurons that express the same receptor converge on one or two glomeruli in each olfactory bulb (Mombaerts et al., 1996).

The mouse has about 1800 glomeruli per olfactory bulb, roughly twice the number of receptor types. The arrangement of glomeruli is approximately fixed from individual to individual, so each odor evokes a particular activation pattern on the surface of the bulb that can be seen directly by imaging. This is the primary odor map from "receptor type" to "spatial position."

The degree of convergence is high: each glomerulus receives input from thousands of receptor neuron axons (about $25\,000$ according to Guyton), while only about 25 mitral cells and about 60 tufted cells send dendrites into it. A direct benefit of this **convergence** is a better signal-to-noise ratio: if the responses of $N$ neurons are independent with the same noise, averaging them improves the signal-to-noise ratio by a factor of $\sqrt N$, about 70 for $N = 5000$.

## 43.2. The Olfactory Bulb and Central Processing

### 43.2.1. Circuits of the Olfactory Bulb

The circuit of the olfactory bulb has three parts:

1. Input layer: the axons of olfactory receptor neurons form excitatory glutamatergic synapses with the dendrites of mitral and tufted cells in the glomeruli;
2. Output layer: mitral and tufted cells are the principal projection neurons; their axons form the olfactory tract and project to olfactory cortex;
3. Local inhibitory network: periglomerular cells around the glomeruli, and the granule cells (which have no axons) that are the most numerous cells in the deep layer. Granule cells form reciprocal dendrodendritic synapses with the lateral dendrites of mitral cells: a mitral cell releases glutamate onto a granule cell, and the granule cell then releases GABA onto the same mitral cell and its neighboring mitral cells.

This circuit performs three kinds of computation on the input:

- Feedback inhibition and gain control: a strongly activated mitral cell quickly inhibits itself, which prevents excessive activation and extends the range of concentrations that can be encoded;
- **Lateral inhibition**: activated glomeruli inhibit the output of other glomeruli through periglomerular and granule cells, which strengthens strong signals and suppresses weak ones and reduces the overlap between the activation patterns of similar odors; this is contrast enhancement and "decorrelation" (pattern separation);
- Temporal coding: rodents sniff at $2$–$12\,\mathrm{Hz}$, and the firing of mitral and tufted cells is synchronized with the respiratory rhythm; different odors make them fire at different phases of the sniff cycle, so the code for an odor depends not only on which cells are activated but also on the temporal order of activation.

The olfactory bulb also receives many centrifugal fibers from olfactory cortex and from brainstem modulatory systems, which end on granule cells and adjust the output of the bulb according to behavioral state and experience. In rodents, granule cells and periglomerular cells are still generated in adulthood in the subventricular zone of the lateral ventricle and enter the bulb through the rostral migratory stream; this adult neurogenesis takes part in olfactory learning.

### 43.2.2. Combinatorial Coding

A receptor can bind many structurally related molecules, only with different affinities, and an odorant molecule can activate many receptors (Malnic et al., 1999). The identity of an odor is therefore not reported by any single receptor.

**Definition 43.2.1 (Combinatorial Coding)** A coding scheme in which each stimulus activates a set of sensors (or neurons), and the identity of the stimulus is represented by the combination of the activated members and their degrees of activation rather than by any one dedicated sensor, is called **combinatorial coding**. The opposite is the **labeled line principle**, in which each stimulus is reported by a dedicated class of sensors.

As the number of receptor types grows, the capacity of combinatorial coding increases much faster than that of labeled-line coding. With $N$ receptor types a labeled-line code can report only $N$ odors; if each odor is represented by the activation of exactly $k$ receptor types, the number of distinguishable combinations is $\binom{N}{k}$; if any on–off combination can be used, it is $2^N$.

**Example 43.2.1** Take $N = 350$ for humans and $k = 10$: $\binom{350}{10} \approx 6.7\times10^{18}$ (the rough estimate $350^{10}/10! \approx 2.8\times10^{25}/3.6\times10^6 \approx 8\times10^{18}$ is slightly too large). The real capacity is far smaller: receptor responses are graded and noisy, similar molecules activate similar combinations, and the combinations for odor mixtures overlap. How many odors humans can actually discriminate is still debated: the traditional estimate is about ten thousand; a 2014 study extrapolated from mixture-discrimination experiments to $10^{12}$, but this extrapolation is extremely sensitive to the parameters of the experimental design and has been strongly criticized (Meister, 2015).

![Capacity of combinatorial coding and decorrelation by lateral inhibition in the olfactory bulb. A: the number of distinguishable codes for N receptors (logarithmic scale): labeled line N; combinations C(N, k) when each odor activates k receptors (k = 3 and 10); arbitrary on-off combinations 2^N. Vertical lines mark the receptor gene numbers of *Drosophila* (about 50), humans (350–400), and mouse (about 1100). B: 200 glomeruli are arranged along some molecular feature (for example, carbon chain length); an odor activates a Gaussian-shaped stretch of glomeruli (width 18, dashed line is the input); lateral inhibition is modeled as subtracting a Gaussian-weighted average of the surrounding activity (width 30, gain 1) followed by rectification, y = max(x − Kx, 0): the output (solid line) is narrower. C: overlap (cosine similarity) of the activation patterns of two odors as a function of the difference between their features; after lateral inhibition the overlap of similar odors is clearly reduced (from 0.73 to 0.43 at a difference of 20), making them easier to distinguish](./plots/combinatorial-code.py)

After the output of the olfactory bulb enters piriform cortex, the code changes again. The several mitral cells of one glomerulus show **divergence** onto many neurons of piriform cortex, and each piriform neuron in turn shows **convergence** of input from many different glomeruli; these connections show no spatial regularity and are approximately random (Stettler and Axel, 2009). As a result, an odor activates a scattered set of neurons in piriform cortex, and the identities of these sets are linked by learning to the meaning of the odor (food, danger, mate). The olfactory input to the Kenyon cells in the mushroom body of *Drosophila* is likewise approximately random, an example of two independently evolved olfactory systems that use the same computational strategy.

### 43.2.3. Central Olfactory Pathways

The olfactory tract projects through the lateral olfactory stria to a group of structures collectively called the primary olfactory cortex:

| Pathway | Structures | Function |
|---|---|---|
| Lateral (main sensory pathway) | anterior olfactory nucleus, piriform cortex, olfactory tubercle, cortical nucleus of the amygdala, entorhinal cortex | recognition of odors and coding of odor mixtures; emotional value; odor memory via entorhinal cortex and hippocampus; coordination of the two sides |
| Medial (ancient instinctive pathway) | septal area, hypothalamus, and brainstem | feeding, salivation, approach and avoidance, autonomic and emotional responses |
| Thalamic (conscious) pathway | piriform cortex → mediodorsal thalamic nucleus → orbitofrontal cortex | conscious perception, naming, and classification of odors; integration with taste into flavor and evaluation of its reward value |

Olfaction is the only sense whose primary pathway reaches the cortex directly without a thalamic relay; it is directly connected to the amygdala, hippocampus, and other parts of the **limbic system**, which may be why odors can quickly evoke strong emotions and memories of past events. In early-diverging vertebrates such as fishes, most of the telencephalon is concerned with smell. Loss of smell is not uncommon clinically: head trauma can sever the olfactory nerves passing through the cribriform plate; infection with the novel coronavirus caused a great many cases of acute anosmia, with the virus mainly infecting ACE2-expressing supporting cells rather than the receptor neurons themselves; and reduced olfaction is also one of the early signs of **Parkinson's disease** and Alzheimer's disease.

### 43.2.4. Olfactory Adaptation

On continuously smelling the same odor, its perceived intensity decreases rapidly and after a few minutes it can hardly be smelled; this is olfactory **adaptation**. The receptor itself adapts by about 50 % in the first second or so and little thereafter (the $\ce{Ca^2+}$ feedback of Section 43.1.2); psychological adaptation is much larger than receptor adaptation, which shows that most adaptation occurs centrally, possibly through inhibition of the granule cells of the olfactory bulb by centrifugal fibers. Adaptation is specific to the odor: after adapting to one odor, the sensitivity to other odors is essentially unchanged, so a new odor can still be smelled in a room filled with a particular smell.

## 43.3. The Vomeronasal Organ and Pheromones

**Definition 43.3.1 (Pheromone)** A chemical signal that an individual releases to the outside and that, when received by other individuals of the same species, elicits a specific behavioral or physiological response is called a **pheromone** (Karlson and Lüscher, 1959). Those that elicit immediate behavioral responses are called releaser pheromones; those that cause longer-lasting endocrine and developmental changes are called primer pheromones.

The first pheromone to be identified was the sex pheromone bombykol of the female silkworm moth (Butenandt, 1959). The receptors on the antennae of male moths are extremely sensitive to it: a single molecule can make a receptor cell fire, and a few hundred molecules per cubic centimeter of air are enough for the male to start searching for the female upwind.

**Definition 43.3.2 (Vomeronasal Organ)** The pair of tubular chemosensory organs at the base of the nasal septum, whose sensory neurons express receptor families such as V1R and V2R and project through the accessory olfactory bulb to the medial amygdala and hypothalamus, and which mainly detect pheromones and chemical signals of conspecific and heterospecific individuals, is called the **vomeronasal organ**, also known as Jacobson's organ.

The receptors of the vomeronasal organ are also **G protein–coupled receptors**, but transduction opens TRPC2 channels through **phospholipase C** and **diacylglycerol**, unlike in the main olfactory epithelium. Its projections bypass olfactory cortex and go through the amygdala directly to the hypothalamic nuclei that regulate sexual behavior, aggression, and parental behavior, so the responses it elicits are mostly fixed and need no learning. Male mice with a *TRPC2* knockout cannot distinguish males from females, try to mate with both, and no longer attack intruder males (Stowers et al., 2002). Known mouse pheromones include the major urinary proteins (MUPs, which provoke aggression between males) and the peptide ESP1 in male tears (which enhances female receptivity). Pheromones can also be sensed through the main olfactory epithelium; the division of labor between the two is not absolute.

The adult human vomeronasal organ is only a vestigial pit without sensory neurons, and *TRPC2* has become a **pseudogene** in Old World monkeys, apes, and humans (Zhang and Webb, 2003; Liman and Innan, 2003). The timing of this loss is close to that of the reacquisition of **trichromatic vision** in Old World primates ([7.14.41](/7.14.41#sec-41.6.5)), and it has been speculated that visual signals (such as the color of sexual skin) replaced part of chemical communication, but this remains a hypothesis. As for claims about human pheromones, not a single molecule has been rigorously identified to date.

## 43.4. Taste

### 43.4.1. Taste Buds and Taste Cells

The receptor organs of taste are the taste buds. An adult has about $2000$–$10\,000$ taste buds, the number decreasing with age; most are in the papillae on the dorsum of the tongue, and some are on the soft palate, pharynx, and epiglottis. The tongue has three kinds of papillae that contain taste buds: the fungiform papillae at the front of the tongue, the foliate papillae at the rear edges of the sides, and the 8–12 circumvallate papillae arranged in a "V" in front of the tongue root (the largest number of taste buds lies in the walls of the trenches around them); the most numerous filiform papillae have no taste buds and are concerned only with touch.

**Definition 43.4.1 (Taste Bud)** The onion-shaped epithelial chemoreceptor organ that consists of 50–150 taste cells together with supporting cells and basal cells, opens to the oral cavity at its apex through the taste pore, and contacts gustatory afferent fibers at its base is called a **taste bud**.

Taste cells are epithelial cells, not neurons; their apical microvilli reach into the taste pore to contact dissolved chemicals. They live about 1–2 weeks and are continually replaced by basal cells. By morphology and function, taste cells fall into three types:

| Type | Function | Output |
|---|---|---|
| Type I | glia-like; clear transmitters; may take part in some salty taste | — |
| Type II (receptor cells) | express sweet, umami, and bitter receptors (G protein–coupled receptors) | release ATP through CALHM1/3 channels onto P2X receptors of afferent fibers; no conventional synapses |
| Type III (presynaptic cells) | sense sour taste | have conventional **chemical synapses** and release serotonin and other transmitters |

All tastes can be sensed on all regions of the tongue, and the sensitivity of different regions differs only slightly. The widely circulated taste map of "sweet at the tip, sour at the sides, bitter at the back" arose from a misreading of early literature and is not correct.

### 43.4.2. Receptors for the Five Basic Tastes

Humans can distinguish five basic tastes: sweet, umami, bitter, sour, and salty. Their receptors are now largely known:

| Taste | Receptor | Mechanism | Typical stimuli |
|---|---|---|---|
| Sweet | T1R2 + T1R3 heterodimer | class C G protein–coupled receptor | sugars, artificial sweeteners, some proteins |
| Umami | T1R1 + T1R3 heterodimer | same | L-glutamate; potentiated synergistically by inosinate and guanylate |
| Bitter | T2R family (about 25 in humans) | G protein–coupled receptors; one type II cell expresses many T2Rs | alkaloids and thousands of other structurally diverse compounds |
| Sour | OTOP1 proton channel (Tu et al., 2018) | $\ce{H+}$ enters type III cells through the channel, and the resulting intracellular acidification also closes inward-rectifier $\ce{K+}$ channels, depolarizing the cell | acids |
| Salty | at low concentration: epithelial sodium channel ENaC (amiloride-sensitive) | $\ce{Na+}$ flows in directly through the channel | low concentrations of $\ce{NaCl}$ (pleasant); the salty taste of high concentrations goes through bitter and sour cells and causes aversion |

The three G protein–coupled receptors in type II cells share one downstream pathway: the $\beta\gamma$ subunits of G proteins such as gustducin activate phospholipase Cβ2, IP₃ releases $\ce{Ca^2+}$ from the endoplasmic reticulum, $\ce{Ca^2+}$ opens the TRPM5 cation channel, and the cell depolarizes, fires action potentials, and opens CALHM1/3 channels to release ATP.

Thresholds differ greatly among tastes (Guyton): about $0.9\,\mathrm{mmol\,L^{-1}}$ for hydrochloric acid, about $10\,\mathrm{mmol\,L^{-1}}$ for sodium chloride, about $10\,\mathrm{mmol\,L^{-1}}$ for sucrose, but only about $8\,\mu\mathrm{mol\,L^{-1}}$ for quinine. The threshold for bitter is three orders of magnitude lower, in keeping with its function of reporting poisons; the thresholds for sweet and umami are higher, because only concentrations of sufficiently high nutritional value are worth reporting. The significance of the five tastes can be summarized as follows: sweet reports energy (sugars), umami reports protein (amino acids), salty reports electrolytes, and bitter and sour warn of poisons and of spoiled or unripe food. Whether fatty acids (through receptors such as CD36 and GPR120) constitute a "sixth taste" is still disputed.

### 43.4.3. Coding of Taste and Flavor

In the periphery taste essentially follows the **labeled line principle**: each type II or type III cell is sensitive to only one basic taste and signals to the center through dedicated afferent fibers. The strongest evidence comes from genetic experiments in mice: if a receptor that can be activated only by an artificial ligand is expressed in sweet cells, mice come to like drinking this otherwise tasteless ligand; if bitter receptors are expressed in sweet cells, mice come to like bitter substances (Zhao et al., 2003; Mueller et al., 2005). What decides "tasty" or "nasty" is the cell that is activated and its connections, not the receptor itself. Many afferent fibers and central neurons respond to several tastes, so central coding combines labeled lines with across-fiber patterns.

What we ordinarily call "taste" is mostly flavor: the result of integration in orbitofrontal cortex of taste, retronasal olfaction, tactile and thermal sensation in the mouth, and chemesthetic stimuli (capsaicin acting on TRPV1, menthol on TRPM8, and mustard on TRPA1, conducted by the trigeminal nerve, [7.14.40](/7.14.40)). During a cold the nasal mucosa swells and retronasal olfaction is lost, and food becomes "tasteless" although the perception of the five basic tastes is perfectly normal.

### 43.4.4. The Gustatory Pathway

The cell bodies of the primary gustatory afferent neurons lie in the sensory ganglia of three pairs of cranial nerves:

- anterior 2/3 of the tongue: the chorda tympani of the facial nerve (VII), with cell bodies in the geniculate ganglion;
- posterior 1/3 of the tongue: the glossopharyngeal nerve (IX), with cell bodies in the petrosal ganglion;
- tongue root, pharynx, and epiglottis: the vagus nerve (X), with cell bodies in the nodose ganglion.

The central processes of all three enter the solitary tract in the medulla and end in the rostral part of the nucleus of the solitary tract (the gustatory nucleus). Fibers from this nucleus (in rodents first through the parabrachial nucleus of the pons) project to the parvicellular part of the ventral posteromedial thalamic nucleus, then to primary gustatory cortex (anterior insula and frontal operculum), and then to orbitofrontal cortex, where they are integrated with olfactory, visual, and visceral hunger and satiety signals to evaluate the reward value of food: after eating one food to satiety, its taste becomes less pleasant, while the attraction of other foods is unchanged (sensory-specific satiety). The gustatory pathway is more hierarchical than the olfactory one and follows the classical "brainstem–thalamus–cortex" sensory pathway.

The nucleus of the solitary tract and the parabrachial nucleus also send taste signals to the hypothalamus and amygdala and, through local brainstem circuits, elicit reflexes such as salivation, swallowing, or vomiting, as well as the cephalic phase of digestion ([7.14.27](/7.14.27)). The association of taste with visceral malaise can be established in a single experience: an animal that develops gastrointestinal illness some hours after eating a novel food will avoid the taste of that food for a long time. This conditioned taste aversion (Garcia, 1955) does not require taste and malaise to be close together in time, which violates the usual temporal rules of conditioning, and is a dedicated learning mechanism for the special danger of "food poisoning."

## 43.5. Evolution and Other Sensory Modalities

### 43.5.1. The Diversity of Chemical Senses

Insect olfactory receptors are topologically quite different from those of vertebrates: they also have seven transmembrane domains, but with the N terminus inside the cell, and they are not coupled to G proteins; instead each forms a heterotetramer with a highly conserved coreceptor, Orco, constituting a cation channel directly gated by odorants (Sato et al., 2008; Wicher et al., 2008; Butterwick et al., 2018). Insects also have the **ionotropic receptor** (IR) and gustatory receptor (GR) families. Despite the different molecules, the olfactory system of *Drosophila* follows the same organizational logic as that of mammals: each olfactory neuron expresses one receptor (plus Orco), neurons expressing the same receptor converge on the same glomerulus in the antennal lobe (about 50 in all), and the projection neurons of the antennal lobe connect to the mushroom body in an approximately random manner. The two groups of animals arrived independently at the same architecture, from an ancestor that never had glomeruli, which suggests that this architecture may be a good solution to the problem of smell.

The nematode *Caenorhabditis elegans* adopted the opposite strategy: it has about 1300 chemoreceptor genes but only 32 chemosensory neurons, each expressing many receptors. The behavioral response is determined by the neuron, not by the receptor: when ODR-10, the receptor for diacetyl, was moved from the AWA neuron, which mediates attraction, to the AWB neuron, which mediates avoidance, the worm changed from being attracted to diacetyl to avoiding it (Troemel et al., 1997). This is a direct demonstration of the **labeled line principle** at the level of a single neuron.

### 43.5.2. Expansion and Loss of Receptor Repertoires

The sizes of chemoreceptor gene families differ enormously among animals and change rapidly with lifestyle (Niimura et al., 2014):

- The African elephant has about 2000 functional olfactory receptor genes, the most known; the rat has about 1200, the mouse about 1100, the dog about 800, and humans and chimpanzees about 400.
- Toothed whales have lost almost all their olfactory receptor genes and have lost the olfactory bulb; baleen whales retain a few. Primates that depend heavily on vision have a higher proportion of pseudogenes among their olfactory receptor genes.
- The same holds for taste receptors: *Tas1r2* is a pseudogene in cats and many other carnivores, which cannot taste sweetness (Li et al., 2005); the umami receptor gene *Tas1r1* of the giant panda is inactivated, with a timing that roughly matches its switch to a bamboo diet (Zhao et al., 2010); sea lions and dolphins have essentially lost the function of the sweet, umami, and bitter tastes, possibly related to the habit of swallowing food whole.
- A counterexample: birds lost *Tas1r2* in evolution, but hummingbirds remodeled the umami receptor T1R1–T1R3 into a sugar-sensitive receptor and can thus feed on nectar (Baldwin et al., 2014).

When a sense is no longer used, the selection pressure that maintains its receptor genes disappears, and the genes gradually accumulate inactivating mutations. The size of the receptor repertoire thus becomes a "genomic fossil" that records the sensory ecology of a group.

### 43.5.3. Electroreception

**Definition 43.5.1 (Electroreception)** The ability of an animal to detect electric fields in its environment is called **electroreception**. Sensing only electric fields that already exist in the environment (such as the bioelectricity of the muscles and gills of prey) is called passive electroreception; sensing the perturbation by surrounding objects of the electric field set up by the discharge of the animal's own electric organ is called active electroreception.

Passive electroreception is an ancient vertebrate trait found in lampreys, cartilaginous fishes, lungfishes, sturgeons, most salamanders, and monotreme mammals, but it was lost in the main lineage of ray-finned fishes and later reevolved independently in catfishes and in two groups of weakly electric fishes. The ampullae of Lorenzini of sharks and rays are fine tubes that open on the skin and are filled with a highly conductive jelly, which conducts the potential of the skin surface to the ampulla at the bottom of the tube; the receptor cells in the ampullary wall (homologous to **hair cells** but without the mechanotransduction of a hair bundle) detect the voltage difference between the inside and outside of the tube. Their sensitivity reaches about $5\,\mathrm{nV\,cm^{-1}}$ (Kalmijn), equivalent to sensing the field of a $1.5\,\mathrm{V}$ battery connected to two electrodes about $3000\,\mathrm{km}$ apart, enough to find a flatfish buried in sand. The ampullary receptor cells of skates use the L-type voltage-gated $\ce{Ca^2+}$ channel CaV1.3 as the voltage sensor and generate electrical oscillations together with BK channels (Bellono, Leitch, and Julius, 2017): a voltage-gated channel directly serves as the receptor. The bill of the platypus carries about $40\,000$ electroreceptors, used to hunt with its eyes closed in turbid water.

Active electroreception occurs only in two groups of weakly electric fishes, the African mormyrids (elephantfishes) and the South American gymnotiforms (knifefishes), which evolved this ability independently, another example of **convergent evolution**. Their tails carry **electric organs** derived from muscle (in a few cases from nerve) ([7.6.30](/7.6.30#def-30.8.1)), which discharge continuously in pulses or waves and set up a dipole-like electric field around the body; the tuberous electroreceptors in the skin are tuned to the frequency of the fish's own discharge.

**Definition 43.5.2 (Electrolocation)** The ability of a weakly electric fish to determine the position, distance, size, and electrical properties of an object from the change in the distribution of current on the skin (the electric image) caused by the perturbation of its own electric field by the object is called **electrolocation**.

Objects that conduct better than water (other fishes, invertebrates) increase the current on the nearby skin and form a "bright" electric image; insulating objects (stones, plastic) decrease the current and form a "dark" image. For a sphere of radius $a$ and conductivity $\sigma_{\mathrm{o}}$ placed in water of conductivity $\sigma_{\mathrm{w}}$ at a place with local field $\boldsymbol{E}_0$, the perturbation potential outside the sphere is that of an induced dipole:

$$
\delta\varphi(\boldsymbol{r}) = \chi\,a^3\,\frac{\boldsymbol{E}_0\cdot(\boldsymbol{r} - \boldsymbol{r}_0)}{\lvert\boldsymbol{r} - \boldsymbol{r}_0\rvert^3}, \qquad \chi = \frac{\sigma_{\mathrm{o}} - \sigma_{\mathrm{w}}}{\sigma_{\mathrm{o}} + 2\sigma_{\mathrm{w}}}, \tag{43.1}
$$
The contrast factor $\chi$ is $1$ for a perfect conductor and $-1/2$ for an insulator (Rasnow, 1996). The perturbation decays with distance as $a^3/r^3$, and the fish's own field also weakens rapidly with distance, so the range of electrolocation is only about one body length. The farther the object, the weaker and wider its electric image; the ratio of the width to the peak of the image is essentially independent of the size and conductivity of the object, and the fish can use it to judge distance (von der Emde, 1999).

![Electric image of a small sphere in active electrolocation (quasi-static model, Eq. (43.1)). The fish is simplified to a current source at +5 cm (head) and a current sink at −5 cm (tail) in uniform unbounded water; the sphere has a radius of 0.5 cm. A: equipotential lines of the fish's field in the plane of the body (arbitrary units), with the sphere (a conductor) at (2.5, 1.5) cm. B: the lateral component of the perturbation field of the sphere at 0.4 cm outside the body axis (which determines the change of the current through the skin); a conductor (χ = 1) produces a "bright" image with a central increase and a slight decrease on both sides, and an insulator (χ = −1/2) produces a weaker "dark" image of opposite sign. C: electric images of a conductor at lateral distances of 1, 2, and 3 cm (each normalized to its peak): the peak falls rapidly with distance (at 2 cm it is about 4 % of that at 1 cm), and the width increases approximately in proportion to distance](./plots/electrolocation.py)

When two wave-type weakly electric fish meet and their discharge frequencies differ by less than about $10\,\mathrm{Hz}$, their electric fields add to produce a slow beat that interferes with each fish's electrolocation. The South American *Eigenmannia* shifts its own frequency away from that of the other fish; this is the jamming avoidance response (Watanabe and Takeda, 1963; Heiligenberg). The fish does not know the other's frequency; by comparing the relation between the amplitude modulation and the phase modulation of the beat in the electric images at different parts of its body, it can tell whether the other's frequency is higher or lower than its own. This was the first computation in neuroethology to be elucidated completely from receptor to motor output. Strongly electric fishes (such as the electric eel, whose discharge can reach several hundred volts) use their discharges for predation and defense while also retaining weak discharges for electrolocation.

### 43.5.4. Magnetoreception

Many animals use the geomagnetic field for orientation and navigation (**magnetoreception**, [7.6.19](/7.6.19#def-19.3.1)). Night-migrating birds (such as the European robin) have an **inclination compass**: they judge "poleward" or "equatorward" from the angle of inclination of the field lines relative to the ground, not from the north–south polarity of the field (Wiltschko and Wiltschko, 1972). This compass depends on light and is disrupted by weak radiofrequency magnetic fields (Ritz et al., 2004; Engels et al., 2014); these features support the **radical pair mechanism**: **cryptochrome** in the retina (most likely CRY4) forms spin-correlated radical pairs after absorbing light, and the ratio of their products changes with the direction of the magnetic field (Xu et al., 2021). Sea turtles, salmon, spiny lobsters, and others can use the geographic distribution of field strength and inclination as a "magnetic map" to determine their position (Lohmann).

Magnetoreception is an unsolved problem in sensory physiology: no magnetoreceptor cell has yet been confirmed, and the neural pathway by which the signal is conducted is unknown. The iron-containing cells in the pigeon beak once thought to be magnetite receptors were later shown to be macrophages (Treiber et al., 2012). The physics of magnetic fields and the calculation of the radical pair mechanism are in [7.6.19](/7.6.19); the behavior and ecology of magnetic navigation are left to ethology.

### 43.5.5. The Sensory Worlds of Animals

Each animal can sense only a part of the world and lives in a "sensory world" determined by its sense organs (called the Umwelt by Uexküll). The senses covered in Chapters 39–43 can be compared from this angle:

| Stimulus energy | Range sensed by humans | Extensions in other animals | Transduction mechanism |
|---|---|---|---|
| Light | $380$–$760\,\mathrm{nm}$, trichromatic | ultraviolet (birds, insects), polarization (insects, cephalopods), infrared (snake pit organ, thermosensation through TRPA1) | opsin–G protein cascade; TRP channels |
| Sound and vibration | $20\,\mathrm{Hz}$–$20\,\mathrm{kHz}$ | ultrasound and **echolocation** (bats, toothed whales), infrasound (elephants, baleen whales, pigeons), water flow (**lateral line**) | mechanically gated channels of hair cells; chordotonal organs |
| Mechanical contact | six receptor types in the skin | Eimer's organs of the star-nosed mole, whiskers of rodents | mechanically gated channels such as Piezo2 |
| Chemicals | about 400 olfactory receptors, five basic tastes | about 2000 olfactory receptors in elephants, pheromones (vomeronasal organ) | G protein–coupled receptors; insect ligand-gated channels |
| Electric field | none | passive (sharks, platypus) and active (weakly electric fishes) electroreception | voltage-gated $\ce{Ca^2+}$ channels |
| Magnetic field | none | compass and map of birds, sea turtles, fishes | possibly radical pairs of cryptochrome, mechanism unsettled |

The regularity in the table echoes the question at the beginning of Chapter 39: a few classes of transduction molecules (**G protein–coupled receptors**, TRP, Piezo, TMC, and voltage-gated channels) are used again and again, and the diversity of sensory modalities arises mainly from accessory structures and from the way the center processes the signals.

## Summary

| Topic | Key points |
|---|---|
| Olfactory epithelium (Definition 43.1.1) | receptor neurons, supporting cells, basal cells; receptor neurons renewed every 1–2 months; orthonasal and retronasal olfaction |
| Olfactory receptors and transduction | the largest GPCR gene family (about 1100 in mouse, about 400 in humans); $\mathrm{G_{olf}}$ → AC III → cAMP → CNG → $\ce{Ca^2+}$-activated $\ce{Cl-}$ current; $\ce{Ca^2+}$–calmodulin negative feedback |
| Threshold and intensity range (Example 43.1.1) | methanethiol about $4\times10^{-14}\,\mathrm{g\,mL^{-1}}$; intensity range only 10–50 fold |
| Glomerulus (Definition 43.1.2) | one neuron, one receptor; neurons with the same receptor converge on one or two glomeruli; convergence of thousands onto tens improves the signal-to-noise ratio |
| Olfactory bulb | mitral/tufted cell output; dendrodendritic synapses of periglomerular and granule cells; gain control, decorrelation by lateral inhibition, locking to respiration |
| Combinatorial coding (Definition 43.2.1, Example 43.2.1) | $\binom{N}{k}$ is far larger than $N$; divergence and convergence in piriform cortex, approximately random connections |
| Central pathways | lateral (recognition), medial (instinct), via the mediodorsal thalamic nucleus to orbitofrontal cortex (consciousness); direct to cortex without thalamus |
| Adaptation | receptor about 50 %, most of it central; odor-specific |
| Pheromones and the vomeronasal organ (Definitions 43.3.1, 43.3.2) | V1R/V2R, TRPC2; accessory olfactory bulb → amygdala → hypothalamus; human *TRPC2* is a pseudogene |
| Taste buds (Definition 43.4.1) | 2000–10 000; type I, type II (sweet, umami, bitter; ATP), and type III (sour; synapse) cells; no taste map |
| Five basic tastes | T1R2/T1R3 sweet, T1R1/T1R3 umami, T2R bitter, OTOP1 sour, ENaC salty; bitter has the lowest threshold |
| Coding and flavor | peripheral labeled lines (receptor-swap experiments); flavor = taste + retronasal olfaction + trigeminal chemesthesis |
| Gustatory pathway | VII, IX, X → nucleus of the solitary tract → ventral posteromedial thalamic nucleus → insula → orbitofrontal cortex; conditioned taste aversion |
| Evolution | insect receptors are ligand-gated channels but the glomerular logic converges; one neuron with many receptors in nematodes; expansion and loss of receptor repertoires |
| Electroreception (Definitions 43.5.1, 43.5.2) | ampullae of Lorenzini about $5\,\mathrm{nV\,cm^{-1}}$; electrolocation in weakly electric fishes, electric image Eq. (43.1); jamming avoidance response |
| Magnetoreception | inclination compass, light dependence, radical pairs and cryptochrome; magnetic map; receptor cells unknown |

## Questions

1. Olfactory receptor neurons and rods both use CNG channels, but one depolarizes and the other hyperpolarizes on stimulation. Compare the direction of change of the second messenger in the two pathways, and explain why olfactory neurons additionally need $\ce{Ca^2+}$-activated $\ce{Cl-}$ channels.

   **Answer** In rods, light activates PDE6, cGMP falls, CNG channels close, the dark current decreases, and the cell hyperpolarizes; in olfactory neurons, an odorant activates adenylyl cyclase, cAMP rises, CNG channels open, and the cell depolarizes. The cilia of olfactory neurons are very thin and bathed in mucus whose ion concentrations are unstable and whose $\ce{Na+}$ concentration may be low, so the CNG current by itself is small; the entering $\ce{Ca^2+}$ opens $\ce{Ca^2+}$-activated $\ce{Cl-}$ channels, and because the neuron keeps its intracellular $\ce{Cl-}$ high through NKCC1, the efflux of $\ce{Cl-}$ produces an extra depolarizing current that amplifies the signal severalfold and makes transduction less sensitive to changes in the ionic composition of the mucus. This is a "built-in" amplifier that does not depend on the external ionic environment.

2. A glomerulus receives input from about 5000 receptor neurons of the same type but sends output to only about 25 mitral cells. Suppose the response of each receptor neuron to a weak odor is only a very small increase in background firing with independent noise. What effect does this convergence have on the odor detection threshold? What is the cost?

   **Answer** When $N$ independent signals with the same noise are added, the signal grows $N$-fold while the noise (standard deviation) grows only $\sqrt N$-fold, so the signal-to-noise ratio improves by $\sqrt N \approx 70$; an extremely weak odor that no single neuron can detect reliably can therefore be detected at the level of the glomerulus, which is why the olfactory threshold is so low (Example 43.1.1). The cost is that the signals of all neurons with the same receptor are merged and the information about their spatial positions in the epithelium is discarded; but olfaction does not need spatial information in the epithelium (an odor has no "image"), so this cost is almost zero. This differs from the convergence of peripheral rods in the retina, which comes at the expense of spatial resolution.

3. Use Eq. (43.1) to estimate by how much the peak of the electric image produced by a weakly electric fish for a conducting small sphere at $1\,\mathrm{cm}$ decreases when the sphere of the same size is at $2\,\mathrm{cm}$. Why can the fish not judge the distance of an object from the peak of the electric image alone?

   **Answer** The lateral component of the perturbation field is the gradient of $\delta\varphi$, and it decays with the distance from the object roughly as $1/r^4$ (the dipole field is $\propto a^3E_0/r^3$, multiplied by the factor by which the local field $E_0$ itself weakens away from the fish's body and by the sampling of the image on the skin), so doubling the distance reduces the peak by more than an order of magnitude; the model in the figure gives only about 4 % at 2 cm of its value at 1 cm. But the peak also depends on the size of the object ($a^3$) and on its conductivity ($\chi$): a small nearby object and a large distant object may produce the same peak. The width of the image is determined mainly by distance and depends little on size and conductivity, so the fish must use a combination of width and peak (or the ratio of edge slope to peak) to judge distance, as shown by the behavioral experiments of von der Emde.

4. Why is the threshold for bitter about three orders of magnitude lower than that for sweet? If a bitter receptor gene is introduced into the sweet cells of a mouse, how will the mouse respond to bitter substances? What principle of taste coding does this illustrate?

   **Answer** Bitter reports potential poisons, and the cost of a misjudgment is poisoning or even death, so it should be reported at very low concentrations; sweet reports energy, and low concentrations of sugar have little nutritional value and are not worth reporting, and a high threshold also reduces unnecessary "temptation." When bitter receptors are expressed in sweet cells, the mouse actively likes to drink bitter substances (Mueller et al., 2005). This shows that, in the periphery, the quality of taste (good or bad, approach or avoidance) is determined by the activated cell and the central pathway to which it is connected, not by the receptor molecule; this is precisely the labeled line principle: the receptor only determines which molecules can activate the line, and the meaning of the line itself is fixed by its connections.

5. (Open question) Humans have about 400 functional olfactory receptor genes, mice about 1100, and toothed whales almost none. Discuss: what does the number of receptors mean for olfactory ability? Is the loss of receptor genes necessarily "degeneration"?

   **Answer** Key points: (1) The number of receptors determines the "alphabet" of combinatorial coding: the more receptors, the finer the molecular structures that can be distinguished and the more kinds of compounds can be detected; but olfactory ability also depends on the area of the olfactory epithelium, the number of receptor neurons, the processing in the bulb and the center, and the tuning range of the receptors; humans, despite having fewer receptors, have thresholds for some odors not much worse than those of dogs, and the odor-discrimination ability of trained humans has also been underestimated. (2) The number of receptor genes changes rapidly with ecological needs: elephants depend on smell to find food and water and to recognize individuals and have a large receptor repertoire; toothed whales keep their blowhole closed underwater and hardly use airborne olfaction, so maintaining receptor genes brings no selective benefit and the genes are inactivated by the accumulation of neutral mutations. (3) Loss is therefore not necessarily "degeneration" but the result of relaxed selection, often accompanied by the strengthening of other senses (echolocation in toothed whales, trichromatic vision in primates); in a nervous system with limited resources, reducing the investment in a sense that is no longer used may even be an economy. There are also cases of active loss; for example, inactivation of certain receptors may help avoid aversion to specific foods (whether the umami receptor of the giant panda is such a case is still debated).
