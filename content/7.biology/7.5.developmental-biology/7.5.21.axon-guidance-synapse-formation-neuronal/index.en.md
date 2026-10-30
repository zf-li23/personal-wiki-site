---
title: Axon Guidance, Synapse Formation and Neuronal Survival
description: "How neurons wire up. Neuronal polarity and the specification of the axon; myelinating glia; the growth cone, its cytoskeleton and the clutch; intrinsic programmes and the four kinds of guidance cue; crossing the midline (netrin and DCC, Slit and Robo, Robo3) and the physical limits on gradient sensing; the retinotectal map, the chemoaffinity hypothesis, Eph/ephrin gradients and a model of map formation by relative signalling and competition; formation of the neuromuscular junction (agrin, LRP4, MuSK) and of central synapses; naturally occurring neuronal death, neurotrophins and a model of competition for innervation."
---

The previous chapters produced neurons of many kinds, each in its place ([7.5.18](/7.5.18), [7.5.19](/7.5.19)). A nervous system works only if these neurons connect correctly: a motor neuron in the spinal cord must reach one muscle among more than fifty in the limb, a retinal ganglion cell must find its place on a map in the brain. This chapter describes how connections are made, in three steps. Axons grow out, led by their **growth cones**, and are steered by attractive and repulsive cues to their targets; at the target they form synapses; and the neurons whose connections succeed survive while many others die. The molecules involved are few compared with the number of connections, and much of the specificity comes from gradients, combinations, changes in responsiveness over time and competition. The refinement of connections by neural activity and their plasticity in the mature brain are treated in [7.16](/7.16); the cell biology of the **cytoskeleton** and of **cell migration** in [7.3.13](/7.3.13)-[7.3.15](/7.3.15).

## 21.1. The Neuron and Its Glia

**Definition 21.1.1 (Neuron)** A **neuron** is a cell specialized for receiving, integrating and transmitting signals. It has a cell body (soma) with the nucleus, usually several dendrites that receive inputs, and a single axon that conducts action potentials to its targets; the axon ends in terminals that make chemical (or electrical) synapses on other neurons, muscle fibres or gland cells.

A newly born neuron first extends several similar neurites, and only later does one of them become the axon. In cultured hippocampal neurons (Dotti, Sullivan and Banker 1988) the sequence is stereotyped: **lamellipodia** (stage 1), several minor neurites (stage 2), one neurite grows rapidly and becomes the axon (stage 3), the others become dendrites (stages 4-5). Which neurite wins is decided by a competition: cutting the axon of a stage-3 neuron makes another, sufficiently long neurite become the axon, and the winner accumulates the polarity proteins Par-3/Par-6 and aPKC, active Rac and Cdc42 and stable, acetylated **microtubules**; a drug that stabilizes microtubules (taxol) applied to one neurite makes it the axon. In vivo the initial polarity is set by the position of the cell: cortical neurons migrating along **radial glia** ([7.5.19](/7.5.19)) form the axon from their trailing process.

Glia make the myelin sheath, the multilayered wrapping of membrane that insulates axons and allows saltatory conduction. In the peripheral nervous system each Schwann cell, derived from the **neural crest** ([7.5.20](/7.5.20)), myelinates one segment of one axon; the decision to myelinate depends on the amount of neuregulin-1 type III on the axon, so large axons are myelinated and small ones are not. In the central nervous system each oligodendrocyte, derived from the pMN domain and later from other ventral and dorsal **progenitors** of the **neural tube** ([7.5.18](/7.5.18)), myelinates segments of many axons. Myelination begins before birth and continues into adulthood; it is in part activity-dependent. Its failure underlies diseases from the inherited leukodystrophies to multiple sclerosis.

## 21.2. The Growth Cone

**Definition 21.2.1 (Growth Cone)** The **growth cone** is the motile, sensory tip of a growing axon or dendrite (Ramón y Cajal 1890). It consists of a central domain, into which the **microtubules** of the axon extend, and an actin-rich peripheral domain forming a flattened lamellipodial veil from which **filopodia** project; it carries receptors for guidance cues and translates them into directed growth.

The growth cone advances by the coordination of two cytoskeletal systems. In the peripheral domain, actin filaments polymerize at the leading edge and are pulled back towards the centre by myosin II, a continuous retrograde flow (**actin filament**, [7.3.13](/7.3.13)). Advance requires a clutch: adhesion receptors (**integrins** binding **laminin**, cell adhesion molecules such as L1 and N-cadherin binding the surfaces of other cells) engage the actin flow through adaptor proteins; when the clutch holds, retrograde flow slows and polymerization pushes the membrane forward, and microtubules invade the space behind, consolidating the new axon (Mitchison and Kirschner 1988; Suter and Forscher). **Filopodia** sample the environment over tens of micrometres; a growth cone whose filopodia are removed with cytochalasin still advances but cannot turn correctly.

![The growth cone. (A) Structure: microtubules of the axon shaft end in the central domain, with a few exploring the periphery; the peripheral domain is a lamellipodial veil filled with branched actin, from which filopodia (bundled actin) extend. (B) The clutch model: actin polymerizes at the leading edge and is pulled back by myosin II (retrograde flow); when adhesion molecules bind the substrate and engage the actin (the clutch), the flow is slowed and polymerization pushes the membrane forward. (C) Turning: on the side of the cone facing an attractant (for example netrin acting through DCC), Rac and Cdc42 are activated, adhesion engages and the cone advances, so it turns towards the source; a repellent (Slit through Robo, semaphorin through plexin, ephrin through Eph) activates RhoA and disengages the clutch on its side, so the cone turns away or, if the signal is uniform, collapses](./plots/growth-cone.py)

A growth cone turns when the two sides behave differently. Attractive cues raise the activity of Rac and Cdc42 and moderately elevate local Ca²⁺, which stimulate actin polymerization and clutch engagement on the near side; repulsive cues activate RhoA and its kinase ROCK, which increase actomyosin contraction and retraction, or trigger local endocytosis, and a strong uniform repellent makes the whole cone collapse. The same receptor can mediate attraction or repulsion depending on the internal state: high cyclic GMP converts netrin attraction into repulsion, and the ratio of **cAMP** to cGMP sets the polarity of the response to several cues (Ming and Poo). Growth cones also synthesize proteins locally from mRNAs transported into the axon, and asymmetric local translation (β-actin on the attractive side) contributes to turning.

## 21.3. Principles of Axon Guidance

**Definition 21.3.1 (Axon Guidance)** **Axon guidance** is the process by which the growth cone of an axon navigates to its target, by responding to molecular cues in its environment that are either attractive or repulsive and act either at short range, bound to cells or the **extracellular matrix**, or at long range, as diffusible gradients; the response depends on the receptors the neuron expresses, which are set by its identity and change along its path.

### 21.3.1. Intrinsic Programmes

Where an axon goes is decided first by what the neuron is. Motor neurons of the spinal cord project to muscle targets according to their position, and their identity is set before their axons leave the cord. Landmesser and colleagues reversed a short length of chick spinal cord before the axons grew out: the motor neurons, now in the wrong place, still sent their axons to their original muscles, correcting their course at the base of the limb. Their identity is a code of LIM homeodomain transcription factors, combined with Hox codes along the axis ([7.5.18](/7.5.18)).

| Motor column | LIM code | Target |
|---|---|---|
| Medial motor column (MMC) | Isl1, Isl2, Lhx3, Lhx4 | axial (back) muscles |
| Lateral motor column, medial (LMCm) | Isl1, Isl2 | ventral limb muscles |
| Lateral motor column, lateral (LMCl) | Isl2, Lhx1 | dorsal limb muscles |

The code is translated into receptors. LMCl axons express EphA4, which is repelled by ephrin-A in the ventral limb mesenchyme, so they choose the dorsal branch at the base of the limb; LMCm axons express EphB, repelled by ephrin-B in the dorsal mesenchyme, and choose the ventral branch. Misexpressing *Lhx1* in LMCm neurons, or *EphA4*, redirects their axons dorsally (Kania and Jessell 2003). Motor axons also avoid the posterior half of each sclerotome, which expresses ephrin-B and semaphorin-3F, as **neural crest** cells do ([7.5.20](/7.5.20)), so ventral roots are segmented in register with the somites.

### 21.3.2. Four Kinds of Cue

| | Attractive | Repulsive |
|---|---|---|
| Contact (short range) | **laminin**, **fibronectin**; L1, N-CAM, N-cadherin (permissive substrates) | ephrins (on Eph receptors), membrane-bound semaphorins (class 1, 4-7), tenascin, chondroitin sulfate **proteoglycans** |
| Diffusible (long range) | netrin-1 through DCC; Shh through Boc; neurotrophins; Wnt (along the axis) | Slit through Robo; secreted semaphorins (class 3) through neuropilin-plexin; netrin through Unc5 |

Several principles emerge from this table. Cues are bifunctional: netrin attracts axons expressing DCC and repels those expressing Unc5 (in *C. elegans*, UNC-6/netrin attracts ventrally migrating axons and repels dorsally migrating ones). Guidance proceeds in short steps between intermediate targets, at each of which the growth cone changes its receptors. And navigation does not require electrical activity: axons find their targets in animals in which action potentials or neurotransmitter release are blocked; activity matters later, for refinement.

## 21.4. Crossing the Midline

### 21.4.1. Netrin, Slit and Robo

Commissural neurons connect the two sides of the nervous system. In the spinal cord, dI1 commissural neurons in the dorsal cord extend axons ventrally to the **floor plate**, cross it, and then turn anteriorly on the other side, never recrossing. The molecular logic was worked out in flies and mice.

- Attraction to the floor plate. The floor plate secretes netrin-1, purified from chick brain as an activity that attracts commissural axons in **collagen** gels (Serafini et al. 1994, Kennedy et al. 1994), the vertebrate homologue of UNC-6. Its receptor is DCC. In *Netrin1* and *Dcc* **knockout mice** most commissural axons fail to reach the floor plate (Serafini et al. 1996). A modern qualification: conditional **deletion** of netrin-1 from the floor plate alone leaves the projection largely intact in the spinal cord, because netrin-1 made by ventricular-zone **progenitors** is deposited on the pial surface and guides the axons by contact (haptotaxis) along their path (Dominici et al. 2017; Varadarajan et al. 2017). Shh from the floor plate adds attraction through the receptor Boc.
- Silencing repulsion before crossing. The floor plate also secretes Slit, which repels axons expressing Robo1 and Robo2. Before crossing, commissural axons express Robo3 (Rig-1), which antagonizes Robo1/2 signalling and so allows them to approach the floor plate; in *Robo3* knockout mice commissural axons never cross (Sabatier et al. 2004). In *Drosophila* the same problem is solved differently: Commissureless sorts Robo into endosomes before crossing, and *robo* mutant axons cross back and forth repeatedly (hence "roundabout").
- Repulsion after crossing. On crossing, Robo3 is switched off (a different splice form, Robo3.2, is made briefly after crossing), Robo1/2 become active, and Slit repels the axons from the midline; Robo also binds DCC and silences netrin attraction (Stein and Tessier-Lavigne 2001). Responsiveness to class 3 semaphorins is also turned on after crossing: before crossing, the semaphorin receptor plexin-A1 is degraded by calpain, and a floor-plate signal blocks this degradation (Nawabi et al. 2010). The axons are thereby expelled from the midline and cannot recross; a gradient of Wnt4 then turns them anteriorly.

Motor neurons, which express Robo1/2 and the netrin receptor Unc5c but neither Robo3 nor DCC, are repelled by the floor plate and leave the cord through the ventral roots. Mutations of *ROBO3* in humans cause horizontal gaze palsy with progressive scoliosis, in which hindbrain axons fail to cross the midline, and mutations of *DCC* cause congenital mirror movements, in which the corticospinal tract partly fails to cross.

![Crossing the midline of the spinal cord (transverse section, dorsal up). (A) Commissural neurons in the dorsal spinal cord send axons ventrally towards the floor plate. Before crossing, they express the netrin receptor DCC and Robo3, which silences the Slit receptors Robo1 and Robo2; netrin (from the floor plate and, deposited on the pial surface, from ventricular progenitors) attracts them and Shh from the floor plate adds attraction through Boc. After crossing they lose Robo3, Robo1/2 become active and Slit from the floor plate repels them, together with semaphorin-3B acting through neuropilin-2 and plexin-A1, so they cannot recross and they turn longitudinally (anteriorly, guided by a Wnt gradient). Motor neurons express Robo1/2 and Unc5c but neither DCC nor Robo3, are repelled by the floor plate and leave the cord through the ventral root. (B) The receptor states before and after crossing](./plots/midline-crossing.py)

### 21.4.2. How Steep Must a Gradient Be?

A growth cone 10 μm across that reads a diffusible gradient must detect a small difference in concentration between its two sides against the noise of receptor binding. The limit is set by counting statistics, in the spirit of the analysis of bacterial **chemotaxis** by Berg and Purcell.

**Formula 21.4.1 (Limit of Gradient Detection)** Let each half of the growth cone carry $N$ receptors with dissociation constant $K$, so that at concentration $c$ each receptor is occupied with probability $p = c/(c + K)$, and let the cone average over a time $T$ that contains $M = T/\tau$ independent readings, where $\tau$ is the correlation time of receptor occupancy. If the concentration differs by $\delta c$ between the halves, the difference in bound receptors has mean $NM\,p(1-p)\,\delta c/c$ and variance $2NM\,p(1-p)$, so that the signal-to-noise ratio is

$$
\mathrm{SNR} = \frac{\delta c}{c}\sqrt{\frac{N M\,p(1-p)}{2}},
\qquad
\Bigl(\frac{\delta c}{c}\Bigr)_{\min} = \sqrt{\frac{2}{N M\,p(1-p)}}
\tag{21.1}
$$

for detection at $\mathrm{SNR} = 1$. The threshold is lowest at $c = K$, where $p(1-p) = \tfrac14$ and $(\delta c/c)_{\min} = \sqrt{8/(NM)}$.

**Proof** At a single reading, the number of bound receptors on one half is binomial with mean $Np$ and variance $Np(1-p)$; the two halves are independent, so their difference has variance $2Np(1-p)$, and over $M$ independent readings the summed difference has variance $2NMp(1-p)$. The mean difference is $NM\,\delta p$ with $\delta p = \frac{\mathrm{d}p}{\mathrm{d}c}\delta c = \frac{K}{(c+K)^2}\delta c = p(1-p)\frac{\delta c}{c}$. Dividing the mean by the standard deviation gives the formula. $\square$

**Example 21.4.1** With $N = 5000$ receptors per half, $\tau \approx 2\ \mathrm{s}$ and averaging over $T = 100\ \mathrm{s}$ ($M = 50$), the best threshold is $\sqrt{8/250000} \approx 0.6\%$. In an exponential gradient with decay length $\lambda$, the fractional difference across a cone of width $a$ is $a/\lambda$ at every distance: for $a = 10\ \mu\mathrm{m}$ and $\lambda = 200\ \mu\mathrm{m}$, 5%. The gradient is therefore readable wherever the threshold is below 5%, that is where $p(1-p) > 2/(NM\cdot 0.05^2) \approx 0.003$, roughly $3\times10^{-3}K < c < 300K$: for a source concentration of $1000K$, a window from about 0.25 to 2.5 mm from the source. Experiments with defined gradients find that growth cones of dorsal root ganglion neurons respond to fractional differences as small as about 0.1% (Rosoff et al. 2004), close to such limits, and that the maximum guidance distance of diffusible cues is about 1 mm, consistent with the window (Goodhill and Urbach 1999). Long-range guidance in large brains is therefore achieved in steps, by intermediate targets and by cues bound to cells along the path.

![Physical limits on gradient sensing by a growth cone (Formula 21.4.1). (A) The smallest fractional difference in concentration across the growth cone that can be detected with signal-to-noise ratio 1, as a function of the concentration c relative to the dissociation constant K of the receptor, for 5000 receptors on each half of the cone and M independent readings. Sensitivity is best at c = K and is lost when receptors are nearly empty or nearly saturated. (B) A growth cone 10 µm wide in an exponential gradient with decay length 200 µm experiences a fractional difference of 5% everywhere; it can read the gradient only where the threshold of (A) is below 5%, which limits guidance to a window of distances from the source (c0 = 1000 K at the source; shaded: detectable for M = 50)](./plots/gradient-sensing.py)

## 21.5. The Retinotectal Map

### 21.5.1. Chemoaffinity

The axons of retinal ganglion cells leave the eye through the optic nerve, cross (all of them in fish and amphibians, partly in mammals) at the optic chiasm and project to the optic tectum (superior colliculus in mammals), where they form a continuous, topographic map: neighbouring cells in the retina connect to neighbouring sites in the tectum, with the axes inverted (temporal retina to anterior tectum, nasal retina to posterior; dorsal retina to lateral tectum, ventral to medial). Midline choice at the chiasm is itself a guidance decision: ipsilaterally projecting axons from the ventrotemporal retina express EphB1 and are repelled by ephrin-B2 at the chiasm, and their number is set by the transcription factor Zic2; albino mammals, with fewer ipsilateral axons, have impaired binocular vision.

**Definition 21.5.1 (Chemoaffinity Hypothesis)** The **chemoaffinity hypothesis** (Sperry 1963) states that neurons and their targets carry complementary molecular labels, arranged in gradients across the retina and the tectum, and that each axon connects to the target position whose label matches its own.

Sperry's evidence came from regeneration in amphibians and fish, whose optic nerves regrow. When he cut the optic nerve of a newt and rotated the eye by 180°, the regenerating axons returned to their original tectal positions: the animal saw the world upside down and struck downwards at prey above it, and never learned to correct this. The connections were therefore determined by the identity of retinal cells and tectal positions, not by function. The molecules were found by in vitro assays. In the stripe assay (Walter, Bonhoeffer and colleagues 1987), temporal retinal axons growing on alternating stripes of anterior and posterior tectal membranes chose the anterior stripes; heat inactivation of posterior membranes abolished the choice, showing that posterior tectum contains a repellent for temporal axons. The repellents are ephrin-A2 and ephrin-A5, expressed in an anterior-to-posterior increasing gradient in the tectum; the receptors are EphA3 (in the chick) and other EphA receptors, expressed in a nasal-to-temporal increasing gradient in the retina (Cheng, Drescher, Flanagan and colleagues 1995). Temporal axons, with the most EphA, are repelled most strongly and stop in the anterior tectum, where ephrin-A is low; nasal axons, with little EphA, can penetrate to the posterior tectum: a stable connection forms where repulsive signalling is weak. Counter-gradients add precision: ephrin-As are also expressed in the retina, high nasally, and EphAs in the tectum, high anteriorly, and reverse signalling through ephrin-A attracts or repels in turn. The dorso-ventral axis is mapped by EphB receptors and ephrin-B ligands, together with Wnt3 and its receptor Ryk.

### 21.5.2. Relative Signalling and Competition

An axon could find its place by reading an absolute level of ephrin, stopping where repulsion reaches a threshold. Brown et al. (2000) tested this with a knock-in mouse in which *EphA3* was expressed, in addition to the endogenous EphA receptors, in a random half of the retinal ganglion cells (those expressing *Isl2*). If axons read absolute levels, the knock-in axons should simply terminate more anteriorly, forming a shifted map overlapping that of their **wild-type** neighbours. Instead the colliculus contained two complete, interleaved maps: the knock-in axons formed an ordered map in the anterior half, and the wild-type axons were displaced, forming a compressed map in the posterior half. The position of an axon depends on its EphA level relative to the axons it competes with. A model in which axons compete for space while minimizing repulsion reproduces both maps.

**Formula 21.5.1 (Map Formation by Repulsion and Competition)** Let axon $i$ originate at retinal position $u_i$ with receptor level $R_i = R(u_i)$, increasing temporally, and let it terminate at tectal site $v_{\pi(i)}$, where the permutation $\pi$ assigns one site per axon (competition for space) and the ligand level $L(v)$ increases posteriorly. Take the total repulsive energy to be

$$
E(\pi) = \alpha\sum_{i} R_i\,L\bigl(v_{\pi(i)}\bigr),
\tag{21.2}
$$

and let the map evolve by random exchanges of neighbouring axons, accepted with the Metropolis probability $\min(1, \mathrm{e}^{-\Delta E/T})$ (a stochastic search for low-energy maps, Koulakov and Tsigankov 2004). By the rearrangement inequality, $\sum_i R_i L_{\pi(i)}$ is minimized when the largest $R$ is paired with the smallest $L$: the energy minimum is the inverted topographic map, temporal axons anteriorly.

The minimum depends only on the order of the $R_i$, not on their values: if half the axons have $R$ raised by a constant larger than the range of $R$ among the others, all of them rank above all the others, take the anterior half of the tectum in their own order and push the wild-type axons into the posterior half, giving the two interleaved maps of the knock-in mice. In mice **heterozygous** for the knock-in, where the increment is smaller, the maps partly fuse in the region where the two populations have similar EphA levels, as observed (Reber, Burrola and Lemke 2004), a further confirmation that relative, not absolute, signalling is read. The model is a cartoon; in vivo, retinal axons overshoot, form interstitial branches along their length, and the branches at the correct position are stabilized while the others are eliminated, and activity refines the result.

![Formation of the retinotectal map by graded repulsion and competition (Formula 21.5.1, a stochastic model in the spirit of Koulakov and Tsigankov). 120 retinal axons, each with an EphA level that rises from nasal to temporal retina, compete for 120 tectal sites whose ephrin-A level rises from anterior to posterior; the repulsive energy of an axon at a site is the product of the two levels, and Monte Carlo exchanges of neighbouring axons lower the total energy. (A) Starting from a random arrangement, the map becomes ordered and inverted: temporal axons (high EphA) end in the anterior tectum (low ephrin-A), nasal axons in the posterior. (B) The experiment of Brown et al. (2000): in half of the retinal ganglion cells, scattered at random, EphA3 is added. The model, like the mice, forms two interleaved maps: knock-in axons take the anterior half of the tectum in retinotopic order, the wild-type axons are displaced into the posterior half](./plots/retinotectal-model.py)

### 21.5.3. Refinement by Activity

The molecular map is approximate; activity sharpens it. Before vision begins, waves of spontaneous activity sweep across the retina (cholinergic, then glutamatergic retinal waves), so that neighbouring ganglion cells fire together while distant ones do not. Correlated firing strengthens connections of neighbouring axons onto the same target neurons (Hebbian plasticity) and so refines topography and segregates the inputs of the two eyes into layers in the lateral geniculate nucleus and into ocular dominance columns in the visual cortex. Blocking retinal waves or NMDA receptors broadens the terminal arbors; in mice lacking both ephrin-A gradients and retinal waves, the map is almost abolished, so molecular labels and activity act together (Pfeiffenberger et al. 2006). The cellular rules of this plasticity and its critical periods belong to [7.16](/7.16).

## 21.6. Synapse Formation

### 21.6.1. The Neuromuscular Junction

**Definition 21.6.1 (Neuromuscular Junction)** The **neuromuscular junction** (NMJ) is the chemical synapse between a motor neuron and a skeletal muscle fibre, at which acetylcholine released from the axon terminal acts on nicotinic acetylcholine receptors (AChR) concentrated, at densities of about $10^{4}\ \mu\mathrm{m}^{-2}$, in the folded postsynaptic membrane of the muscle.

The NMJ is the best-understood synapse, because it is large and accessible. Before innervation, AChRs are distributed over the whole muscle fibre at low density, with a **prepattern** in its central band. The motor axon terminal induces a dense cluster beneath it:

- Agrin. The neural isoform of the proteoglycan agrin (z⁺ agrin, made by motor neurons) is released into the synaptic **basal lamina**. It binds LRP4 on the muscle, and the LRP4-agrin complex activates the **receptor tyrosine kinase** MuSK; with the adaptor Dok7, MuSK recruits rapsyn, which clusters AChR, and organizes the postsynaptic **cytoskeleton**. Mice lacking agrin, LRP4, MuSK, Dok7 or rapsyn fail to form NMJs and die at birth from failure to breathe (DeChiara et al. 1996; Gautam et al. 1996). LRP4 also signals back to the terminal and promotes presynaptic differentiation.
- Transcription. Subsynaptic nuclei transcribe AChR genes at a higher rate, stimulated by signals from the terminal including neuregulin-1 acting through ErbB receptors (and by MuSK signalling itself); muscle activity represses AChR transcription in the extrasynaptic nuclei, through Ca²⁺ and the transcription factor myogenin. The combination concentrates receptors at the synapse.
- Dispersal. Acetylcholine itself disperses non-synaptic AChR clusters; agrin protects the synaptic clusters from this dispersal. In mice lacking both agrin and acetylcholine synthesis, AChR clusters form, in the prepattern, without nerve-derived agrin (Misgeld et al. 2005; Lin et al. 2005): agrin acts mainly to stabilize clusters against neural dispersal rather than to create them.

The same molecules are targets of disease. Congenital myasthenic syndromes, causing fatigable weakness from birth, result from mutations in AChR subunit genes (most often *CHRNE*), *RAPSN*, *DOK7*, *MUSK*, *AGRN* and *LRP4*; autoimmune myasthenia gravis is caused by antibodies against AChR, MuSK or LRP4.

![Formation of the neuromuscular junction. (A) Before innervation, acetylcholine receptors (AChR) are spread over the muscle fibre, with a faint prepattern in its central band. (B) The motor axon terminal releases agrin, which binds LRP4; LRP4 activates the receptor tyrosine kinase MuSK, which with Dok7 recruits rapsyn and clusters AChR under the terminal, at the crests of the junctional folds of the postsynaptic membrane. Neuregulin and other signals raise transcription of AChR genes in the subsynaptic nuclei, while electrical activity of the fibre represses it in the other nuclei, so receptors become concentrated at the synapse. (C) Polyneuronal innervation at birth is reduced to a single axon per fibre within the first weeks by activity-dependent competition](./plots/nmj-formation.py)

At birth each muscle fibre is innervated by several motor axons; within the first two to three postnatal weeks in rodents all but one withdraw, so that every adult fibre has a single input (synapse elimination). The process is competitive and activity-dependent: blocking activity delays it, and axons that are more active, or whose activity is synchronous with the muscle, tend to win. The model in 21.7 shows how competition for a limited trophic resource can produce such a winner-take-all outcome.

### 21.6.2. Synapses Between Neurons

Synapses between neurons are classified by the parts they join: axodendritic (the majority, many on dendritic spines), axosomatic (often inhibitory), axoaxonic (presynaptic inhibition, for example on the initial segment), dendrodendritic and others. Their formation follows the same logic as at the NMJ, initial adhesive contact followed by mutual induction of pre- and postsynaptic specializations. Dendrites extend **filopodia** that contact axons; adhesion molecules (**cadherins** and protocadherins, SynCAMs, neurexins on the presynaptic side binding neuroligins, LRRTMs and cerebellins on the postsynaptic side) stabilize the contact and recruit the active zone presynaptically and receptor scaffolds (PSD-95 for glutamate receptors, gephyrin for GABA and glycine receptors) postsynaptically. Mutations in neurexin and neuroligin genes (*NRXN1*, *NLGN3*, *NLGN4X*) and in *SHANK3* are associated with autism spectrum disorders. Dendritic spines are small protrusions, each receiving usually one excitatory synapse; a cerebellar Purkinje cell carries up to about 100 000 spines.

Electron microscopic reconstruction of every synapse in a block of tissue, the connectome, shows how specific connections are. In a saturated reconstruction of a small volume of mouse neocortex (Kasthuri et al. 2015), axons often passed close to dendrites without forming synapses, so that physical proximity does not predict connection (contrary to Peters' rule), and some axons formed several synapses on the same dendrite while others formed one: connectivity is selected, not random. The complete connectome of the *Drosophila* brain (about 140 000 neurons, 2024) and that of *C. elegans* provide reference wiring diagrams against which the developmental rules can be tested.

## 21.7. Neuronal Survival

### 21.7.1. Naturally Occurring Cell Death

In many parts of the developing nervous system about half of the neurons produced die, by **apoptosis** ([7.3.25](/7.3.25)), at the time their axons reach their targets. Hamburger and Levi-Montalcini showed that the target controls the number: removing a limb bud from a chick embryo increases the death of the motor and sensory neurons that would have innervated it, and grafting an extra limb reduces their death (Hollyday and Hamburger 1976). Death matches the size of each neuronal population to that of its target, removes neurons that made errors, and eliminates transient populations.

**Definition 21.7.1 (Neurotrophic Factor Hypothesis)** The **neurotrophic factor hypothesis** states that developing neurons depend for their survival on trophic factors produced in limited amounts by their target tissues, that neurons compete for these factors, and that those receiving too little die by **apoptosis**.

The prototype is nerve **growth factor** (NGF). Levi-Montalcini and Cohen found that a mouse sarcoma implanted into chick embryos caused sympathetic and sensory ganglia to grow and to innervate the tumour; snake venom and then mouse salivary gland were richer sources, and the active protein was purified. Antibodies against NGF injected into newborn mice destroy the sympathetic chain (immunosympathectomy), and NGF applied to one side of a compartmented culture supports axon growth only on that side (Campenot chambers), showing that the factor acts locally on axons and that its signal is carried retrogradely to the cell body by endosomes containing the receptor. The neurotrophin family comprises NGF, BDNF, NT-3 and NT-4, acting through the receptor tyrosine kinases TrkA (NGF), TrkB (BDNF, NT-4) and TrkC (NT-3), and through the common receptor p75NTR, which, bound by uncleaved proneurotrophins, can promote death instead.

Different neurons need different neurotrophins, and the same neuron may switch dependence with age. Proprioceptive sensory neurons need NT-3 and TrkC (in *Ntf3* **knockout mice** they are absent), nociceptors need NGF and TrkA; sympathetic neurons depend on NGF, and early trigeminal sensory neurons first on BDNF and NT-3 and later on NGF. Other factors, such as GDNF (through RET), CNTF and HGF, support motor neurons and others. Mutations of *NTRK1* (TrkA) cause congenital insensitivity to pain with anhidrosis, since the nociceptors and the sympathetic innervation of sweat glands are lost. Neurotrophins are not only **survival factors**: they guide growth cones (attracting or repelling, depending on the neuron), promote branching and regulate synaptic plasticity.

### 21.7.2. A Model of Competition

Competition for a neurotrophin can explain both how the number of neurons is matched to the target and how a muscle fibre ends up with a single axon, if the growth of an axon terminal depends nonlinearly on the factor it takes up.

**Formula 21.7.1 (Competition for a Neurotrophic Factor)** Let $a_i$ be the size of the terminal of axon $i$ on a target (for example its amount of receptor), and $N$ the concentration of neurotrophin, released by the target at rate $\sigma$ and degraded at rate $\delta$. With uptake by each axon proportional to its size, $u_i = a_i\,N/(K + N)$, and growth of each axon a cooperative function of its uptake,

$$
\dot a_i = \alpha\,\frac{u_i^{2}}{\theta^{2} + u_i^{2}} - \gamma\,a_i,
\qquad
\dot N = \sigma - \delta N - \beta\,\frac{N}{K + N}\sum_i a_i,
\tag{21.3}
$$

(a simplified form of the model of van Ooyen and Willshaw 1999), the axons compete through the shared, depleted resource $N$.

Because a larger terminal takes up more factor and grows faster (positive feedback through the cooperative growth term), while all terminals draw on the same pool, the symmetric state in which all axons are equal is unstable when the supply is small: a slight initial advantage is amplified, one axon takes over and the others retract. When the supply is large, $N$ stays high, growth saturates for all axons and they coexist. The number of surviving axons rises stepwise with $\sigma$. The model predicts that increasing the trophic supply should maintain multiple innervation, as observed when neurotrophins or GDNF are overexpressed in muscle (Nguyen et al. 1998), and that the outcome depends on the form of the growth function: with a linear dependence of growth on uptake, the axons coexist at any supply.

![Competition for a neurotrophic factor can eliminate all but one input (Formula 21.7.1, a simplified version of the model of van Ooyen and Willshaw 1999). Five axons innervate one target, which releases a neurotrophin at rate sigma; the neurotrophin is degraded and taken up by the axons in proportion to their size, and each axon grows at a rate that depends cooperatively on its uptake and is lost at a constant rate. (A) At low release rate one axon, initially only slightly larger than the others, takes over the target and the others retract: single innervation, as at the adult neuromuscular junction. (B) At high release rate all axons survive and coexist. (C) Number of surviving axons after a long time as a function of the release rate: the number of inputs the target can support rises with its supply of neurotrophin, and below a minimum supply none survives](./plots/competition-model.py)

## Summary

| Step | Mechanism | Molecules | Key experiment |
|---|---|---|---|
| Axon specification | competition among neurites | Par complex, Rac/Cdc42, stable **microtubules** | axon cut: another neurite becomes axon |
| Growth cone motility | actin flow + clutch; microtubule invasion | **integrins**, L1, N-cadherin, myosin II | **filopodia** removed: no turning |
| Target choice | intrinsic LIM code → receptors | Isl1/2, Lhx1, EphA4, EphB | spinal cord reversal; *Lhx1* misexpression |
| Midline crossing | attraction then repulsion | netrin/DCC, Slit/Robo, Robo3, Sema3B/PlexinA1 | *Robo3* knockout: no crossing |
| Topographic map | graded repulsion, relative signalling, competition | EphA/ephrin-A, EphB/ephrin-B | eye rotation; stripe assay; *EphA3* knock-in |
| NMJ | agrin-LRP4-MuSK-Dok7-rapsyn; synaptic transcription | AChR, neuregulin | *Agrin*/*Musk* knockouts |
| Survival | limited neurotrophin from targets | NGF/TrkA, BDNF/TrkB, NT-3/TrkC, p75 | limb removal and addition; anti-NGF |

- The neuron (Definition 21.1.1) specifies one neurite as the axon by local competition; Schwann cells and oligodendrocytes myelinate it.
- The growth cone (Definition 21.2.1) advances by actin flow and a clutch and turns by asymmetric Rac/Cdc42 or RhoA activity.
- Axon guidance (Definition 21.3.1) combines four kinds of cue (contact or diffusible, attractive or repulsive) with an intrinsic code that sets receptors; responses switch at intermediate targets such as the **floor plate**.
- Gradient reading is limited by receptor noise (Formula 21.4.1): best at $c \approx K$, guidance over about a millimetre (Example 21.4.1).
- Retinotectal maps follow chemoaffinity (Definition 21.5.1) through EphA/ephrin-A gradients read relative to competitors (Formula 21.5.1), then are refined by activity.
- The NMJ (Definition 21.6.1) forms by agrin-LRP4-MuSK signalling, synaptic transcription and dispersal of non-synaptic receptors; polyneuronal innervation is eliminated.
- About half of developing neurons die; survival depends on target-derived neurotrophins (Definition 21.7.1), and competition with cooperative growth explains single innervation (Formula 21.7.1).

## Questions

1. Sperry rotated the eye of a newt by 180° after cutting the optic nerve. Describe the behaviour of the animal after regeneration and explain why this result supports chemoaffinity rather than a functional, learned matching of retina and tectum.

   **Answer** The regenerated axons reconnected to their original tectal positions, so the visual field was inverted: the newt struck downwards at a lure held above it and backwards at one in front, and it never corrected this with experience. If connections were established by function (adjusted until behaviour was correct), the animal should have adapted; instead the projection was dictated by the original identity of each ganglion cell, implying fixed molecular labels in retina and tectum.

2. In the stripe assay, temporal retinal axons prefer anterior tectal membranes, while nasal axons grow equally on both. Explain this with the EphA and ephrin-A gradients, and predict the result if posterior membranes are treated with phosphatidylinositol-specific phospholipase C (which removes GPI-anchored proteins).

   **Answer** Temporal axons have high EphA and are repelled by the high ephrin-A of posterior membranes, so they avoid posterior stripes; nasal axons have low EphA and are insensitive at the ephrin levels of either membrane. Ephrin-As are GPI-anchored, so PI-PLC treatment removes them and abolishes the repulsion: temporal axons grow on both stripes, as was found (and as heat treatment did).

3. Using Formula 21.4.1, how many receptors per half would a growth cone need to detect a 1% difference in one reading ($M = 1$) at $c = K$? How does averaging over 100 s with $\tau = 1\ \mathrm{s}$ change this?

   **Answer** $(\delta c/c)_{\min} = \sqrt{8/(NM)} = 0.01$ gives $NM = 8\times10^{4}$: with $M = 1$, $N = 80\,000$ receptors per half, more than a growth cone plausibly has. With $M = 100$, $N = 800$ suffices. Temporal averaging is essential, and it costs time: a growth cone advancing at 50 μm/h integrates over a few minutes, during which it moves only a few micrometres, so the gradient is effectively constant during the measurement.

4. In mice in which *EphA3* is knocked in to half of the retinal ganglion cells, two maps form. What would you predict if *EphA3* were knocked in to all ganglion cells, and why does this result argue against reading absolute ephrin levels?

   **Answer** If every axon gains the same increment of EphA, the ordering of $R_i$ is unchanged, so by the competition argument the map is unchanged and covers the whole tectum; an absolute-threshold model would predict that all axons terminate more anteriorly, leaving the posterior tectum empty. The normal map with uniform knock-in, together with the two maps with **mosaic** knock-in, shows that position depends on relative EphA levels among competing axons (and on competition for space).

5. Netrin-1 attracts commissural axons, and *Netrin1* **knockout mice** have severe commissural defects. Why did the finding that floor-plate-specific deletion of *Netrin1* leaves spinal commissural axons largely normal change the interpretation, and what experiment demonstrated the alternative?

   **Answer** It showed that floor-plate netrin is not needed as a long-range chemoattractant in the spinal cord; the defect of the global knockout must come from netrin made elsewhere. Conditional deletion from ventricular-zone **progenitors** (with *Nestin-Cre* or *Sox2-Cre*) reproduced the defects, and netrin-1 protein was found deposited along the pial surface beside the path of the axons, acting as a short-range, haptotactic substrate (Dominici et al. 2017; Varadarajan et al. 2017). The textbook diffusible-gradient model is therefore at least incomplete in the spinal cord, though long-range attraction by floor-plate netrin operates in parts of the hindbrain.

6. Predict the trajectory of commissural axons in *Robo3* knockout mice and in mice lacking *Robo1* and *Robo2*, and explain both.

   **Answer** Without Robo3, Robo1/2 are active from the start; commissural axons are repelled by floor-plate Slit and never cross, projecting ipsilaterally. Without Robo1 and Robo2, axons cross but are not expelled from the midline: many stall in the **floor plate** or recross, and their longitudinal trajectories are disorganized. Robo3 thus switches the response to Slit from off to on at the right time.

7. In the competition model (Formula 21.7.1), explain why a cooperative dependence of growth on uptake is needed for single innervation, and propose an experiment that tests the model's prediction about trophic supply.

   **Answer** With linear growth, $\dot a_i = \alpha' u_i - \gamma a_i = a_i(\alpha' N/(K+N) - \gamma)$, all axons have the same per-capita growth rate, so their ratios never change and they coexist; cooperativity makes the per-capita rate increase with size, so larger terminals gain an advantage and differences are amplified. Test: increase trophic factor supply at the NMJ (**transgenic** overexpression of GDNF or neurotrophin in muscle) and measure the persistence of polyneuronal innervation; the model predicts delayed or prevented elimination (found for GDNF overexpression), and conversely reducing the factor should accelerate elimination.

8. Limb-bud removal increases death of motor neurons, while an extra limb reduces it. Design the experiment and the quantification, and explain how it supports the neurotrophic factor hypothesis rather than an intrinsic death programme.

   **Answer** In chick embryos at stage 18, before motor axons reach the limb, remove one hindlimb bud (or graft an extra bud next to it); at E10, after the period of motor neuron death, count motor neurons in the lumbar lateral motor column on both sides in serial sections (stereological counting, with the contralateral side as control). Removal leaves far fewer neurons, an extra limb more (Hollyday and Hamburger 1976). An intrinsic programme would kill a fixed fraction regardless of the target; the dependence on target size shows that the target supplies a limiting **survival factor**, later identified with neurotrophic factors.

9. A child has congenital myasthenic syndrome with a mutation in *DOK7*. Explain where in the pathway the defect lies and why weakness is fatigable.

   **Answer** Dok7 is the adaptor that is required for MuSK activation and for anchoring the AChR clusters via rapsyn downstream of agrin-LRP4. Its loss gives small, simplified NMJs with fewer clustered AChRs; the safety factor of transmission (excess of endplate potential over threshold) is low. With repetitive stimulation acetylcholine release per impulse declines (normal rundown), and at junctions with a low safety factor the endplate potential falls below threshold, so muscle fibres drop out and weakness increases with use.
