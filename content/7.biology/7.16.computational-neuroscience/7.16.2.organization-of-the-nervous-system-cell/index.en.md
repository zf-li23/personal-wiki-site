---
title: "Organization of the Nervous System: Cell Types, Circuit Motifs and Brain Regions"
description: "The building blocks of nervous systems and how they are arranged: neuronal cell types defined by morphology, physiology, gene expression and connectivity; astrocytes, oligodendrocytes, Schwann cells and microglia; circuit motifs analyzed with a common rate model; the major brain regions with their numbers of neurons, synapses and energy use; and topographic maps with the cortical magnification factor."
---

A nervous system is built from a small number of cell classes, divided into a large number of types, connected by recurring patterns of wiring into regions that each perform specialized functions. This chapter introduces these building blocks at three levels: cells (neurons and glia), circuits (motifs that recur in every nervous system) and regions (the overall plan of the vertebrate brain and its maps). It uses a single mathematical tool, the threshold-linear **rate model**, to show what each circuit motif computes; the model is justified in [7.16.15](/7.16.15), where network dynamics are analyzed in general.

The structure of neurons, their polarity and the anatomy of the brain have been described in [animal physiology](/7.14.5#sec-5.1.2) and [7.14.7](/7.14.7#sec-7.2); the development of the neural tube and the generation of neurons and glia in [7.5](/7.5). This chapter adds the classification of cells, the quantitative logic of circuits, and the numbers.

## 2.1. Neurons and Cell Types

Neurons are polarized cells: dendrites and soma receive input, the **axon initial segment** generates action potentials, and the axon carries them to presynaptic terminals ([7.14.5](/7.14.5#sec-5.2)). Their morphology varies enormously: a cerebellar granule cell has four short dendrites and a soma of 5–8 µm, a Purkinje cell a planar dendritic tree that receives some 150 000 parallel-fiber synapses, a human motor neuron an axon a meter long.

**Definition 2.1.1 (Cell Type)** A **cell type** is a population of cells that share a consistent set of properties distinguishing them from other cells of the same tissue: morphology, intrinsic electrophysiology, gene expression, and synaptic connectivity (inputs and targets).

The four kinds of criteria usually agree, which is why the concept is useful. In the mouse neocortex about 80% of neurons are excitatory glutamatergic cells (mostly pyramidal neurons, classified by layer and by projection target) and about 20% are inhibitory GABAergic interneurons. The interneurons fall into three nonoverlapping groups by marker genes, which also predict their physiology and wiring:

| Group (marker) | Fraction of interneurons | Main morphology | Targets | Firing |
|---|---|---|---|---|
| Parvalbumin (PV) | ~40% | basket and chandelier cells | soma and axon initial segment of pyramidal cells | fast-spiking, little adaptation |
| Somatostatin (SST) | ~30% | Martinotti cells | distal dendrites of pyramidal cells | adapting, low-threshold |
| 5-HT3A receptor (incl. VIP) | ~30% | bipolar, neurogliaform | mostly other interneurons (VIP → SST) | irregular, adapting |

**Single-cell RNA sequencing** has turned classification into a quantitative problem: cells are clustered by their transcriptomes ([3.4](/3.4)), and the clusters are then validated against morphology and physiology (Patch-seq records all three from the same cell). A whole-brain atlas of the mouse lists about 5000 transcriptomic clusters organized hierarchically into some 30 classes and 300 subclasses. The hierarchy matters: the boundaries between classes are sharp, whereas many fine clusters grade into each other along continua, so "type" is not always a discrete concept at the finest level.

## 2.2. Glial Cells

**Definition 2.2.1 (Glial Cell)** **Glial cells** are the non-neuronal cells of the nervous system that support, insulate and regulate neurons. The main classes in vertebrates are **astrocytes**, myelinating cells (**oligodendrocytes** in the central nervous system, **Schwann cells** in the peripheral nervous system) and **microglia**.

In the human brain glia and neurons are about equally numerous overall (the often-quoted ratio of ten to one is incorrect), with the ratio varying among regions: glia outnumber neurons in the cerebral cortex and white matter, while the cerebellum is dominated by small granule neurons. A brief description of each class is given in [7.14.5](/7.14.5#sec-5.1.3); their functions are summarized here (Figure 1).

- *Astrocytes* tile the brain, each occupying its own domain that in the rodent cortex contacts some $10^5$ synapses. Their processes take up glutamate through excitatory amino-acid transporters, ending its action at synapses and preventing excitotoxicity; they buffer extracellular $\ce{K+}$ released during activity and redistribute it through gap-junction-coupled networks; their endfeet cover the capillaries, contribute to the **blood–brain barrier** and couple neural activity to blood flow. A synapse ensheathed by an astrocyte process is called a tripartite synapse.
- *Oligodendrocytes* and *Schwann cells* wrap axons in myelin. An oligodendrocyte myelinates segments of up to dozens of axons; a myelinating Schwann cell wraps a single segment of one axon. Schwann cells also guide regeneration of peripheral axons after injury, which central axons largely fail to do.
- *Microglia* are the resident macrophages of the brain, derived from yolk-sac progenitors that colonize it in the embryo. Their motile processes survey the entire neuropil every few hours; they respond to injury and infection, and during development they eliminate synapses tagged by complement proteins (C1q, C3), a form of activity-dependent pruning.

**Definition 2.2.2 (Myelin and Nodes of Ranvier)** **Myelin** is a multilayered, compacted wrapping of glial plasma membrane around an axon. Myelinated segments (internodes) are separated by short gaps, the **nodes of Ranvier**, where voltage-gated $\ce{Na+}$ channels are concentrated at densities of about $10^3\,\mu\mathrm{m}^{-2}$.

Myelin reduces the capacitance and increases the resistance of the internodal membrane, so that the action potential jumps from node to node in **saltatory conduction** ([7.14.4](/7.14.4#sec-4.9.3)); the physics and the resulting velocity scaling are derived in [7.6.30](/7.6.30#sec-30.7) and simulated in [7.16.5](/7.16.5#sec-5.5).

![The four main classes of glial cells (schematic, not to scale). A: an astrocyte whose processes end on a capillary (endfeet) and ensheath a synapse. B: an oligodendrocyte myelinating segments of several axons in the central nervous system; nodes of Ranvier separate adjacent sheaths. C: myelinating Schwann cells in a peripheral nerve each wrap one segment of one axon; the cross section shows the compact wraps. D: a microglial cell with fine ramified processes](./plots/glia.py)

## 2.3. Circuit Motifs

Nervous systems of very different animals contain the same small patterns of connection, just as electronic circuits are built from a few standard stages.

**Definition 2.3.1 (Circuit Motif)** A **circuit motif** is a pattern of synaptic connections among a few neurons or cell types that recurs across circuits and performs a characteristic transformation of its inputs.

To see what each motif does, we describe each cell by its **firing rate** $r$ and use the same threshold-linear rate model for all of them,

$$
\tau\,\frac{\mathrm{d}r_i}{\mathrm{d}t} = -r_i + \Bigl[\sum_j w_{ij} r_j + u_i(t)\Bigr]_+ ,
$$

where $w_{ij}$ is the weight of the connection from cell $j$ to cell $i$ (positive for excitation, negative for inhibition), $u_i$ an external input, $[x]_+ = \max(x, 0)$ and $\tau = 10\,\mathrm{ms}$. Figure 2 shows the response of each motif to the same step of input.

1. *Feedforward excitation* ($A \to B$) relays a signal with a delay set by $\tau$; chains of feedforward connections carry information from sensory receptors to the cortex, with **convergence** and **divergence** at each stage.
2. *Recurrent excitation* ($B \to B$ with weight $0 < w < 1$) amplifies and prolongs. For a constant input $u$ the steady state is $r = u/(1 - w)$, and the effective time constant is $\tau/(1 - w)$ (Proposition 2.3.1). Recurrent excitation in cortex amplifies weak thalamic input and, when $w$ approaches 1, can sustain activity after the input ends, a mechanism of working memory ([7.16.45](/7.16.45)).
3. **Feedforward inhibition** (input excites both $B$ and an interneuron that inhibits $B$) makes the response transient: $B$ responds only during the delay before inhibition arrives. In the hippocampus and cortex this window is 1–3 ms, which makes pyramidal cells precise **coincidence detectors**.
4. *Recurrent (feedback) inhibition* ($B \to I \dashv B$) reduces the gain to $1/(1 + w_{BI}w_{IB})$, produces an overshoot at onset, and with delays generates oscillations; the gamma rhythm of cortex arises in this way ([7.16.15](/7.16.15)).
5. **Disinhibition** (an input inhibits an interneuron that tonically inhibits $B$) releases $B$; it is the way the basal ganglia select actions and the way VIP interneurons gate cortical pyramidal cells through SST cells.
6. **Reciprocal inhibition** between two cells, combined with a slow adaptation, produces alternation: the **half-center oscillator** that drives rhythmic movements in **central pattern generators**.
7. **Lateral inhibition** among neighbors in a map enhances contrast at edges (Mach bands, first analyzed in the eye of *Limulus* by Hartline and Ratliff).
8. **Convergence** of $N$ independent inputs onto one cell increases the signal proportionally to $N$ and the noise proportionally to $\sqrt N$, so the signal-to-noise ratio grows as $\sqrt N$.

**Proposition 2.3.1 (Gain and Time Constant of Recurrent Excitation)** For a linear cell with self-excitation, $\tau\,\mathrm{d}r/\mathrm{d}t = -r + wr + u$ with $0 \le w < 1$ and constant $u$, the steady state is $r_\infty = u/(1 - w)$ and $r$ approaches it exponentially with time constant $\tau/(1 - w)$. For $w > 1$ the activity grows without bound until a nonlinearity limits it.

**Proof** Writing the equation as $\frac{\tau}{1-w}\,\frac{\mathrm{d}r}{\mathrm{d}t} = -r + \frac{u}{1-w}$ gives the solution $r(t) = r_\infty + (r(0) - r_\infty)\,\mathrm{e}^{-(1-w)t/\tau}$. $\square$

The proposition shows a general trade-off: positive feedback buys gain at the price of slowness. With $w = 0.8$ the gain is 5 and the time constant 50 ms (Figure 2, second panel).

![Eight circuit motifs in the same threshold-linear rate model (τ = 10 ms for every cell; input step from 50 to 250 ms, shaded). Feedforward excitation relays; recurrent excitation (w = 0.8) amplifies fivefold and slows to τ/(1 − w) = 50 ms; feedforward inhibition makes the response transient; feedback inhibition reduces the gain and produces an onset overshoot; disinhibition releases a tonically inhibited cell; reciprocal inhibition with adaptation (time constant 150 ms) produces alternation; lateral inhibition in a row of cells enhances an edge in the input; convergence of N independent inputs increases the drive as N and the noise as √N](./plots/motifs.py)

## 2.4. The Vertebrate Nervous System and Its Regions

The vertebrate central nervous system develops from the neural tube into the spinal cord and three brain vesicles ([7.5](/7.5)); its anatomy is described in [7.14.7](/7.14.7#sec-7.2). The functional division of labor can be summarized in a table:

| Division | Main structures | Principal functions |
|---|---|---|
| Spinal cord | dorsal and ventral horns | sensory input from body, motor output, reflexes and locomotor **central pattern generators** |
| Hindbrain | medulla, pons, cerebellum | breathing, heart rate, sleep–wake switching; motor coordination and learning (cerebellum) |
| Midbrain | tectum (superior and inferior colliculi), tegmentum, substantia nigra, ventral tegmental area | orienting to visual and auditory stimuli; **dopamine** neurons for movement and reward |
| Diencephalon | thalamus, hypothalamus | relay and gating of sensory and motor information to the cortex; homeostasis, hormones, motivated behaviors |
| Telencephalon | cerebral cortex, hippocampus, amygdala, **basal ganglia**, olfactory bulb | perception, planning, language; declarative memory; emotion; action selection; smell |

The cerebral cortex of mammals is a sheet 2–4 mm thick. The **neocortex** has six layers with a canonical flow of information: thalamic input arrives mainly in layer 4, is passed to layers 2/3 (which project to other cortical areas) and to layers 5 and 6 (which project to subcortical targets and back to the thalamus). The surface area grows a thousandfold from mouse to human while the thickness changes by only a factor of two to three: cortical expansion is expansion of area, with the same local circuit repeated.

Numbers set the scale of the problem (Figure 3). The human brain contains about $8.6 \times 10^{10}$ neurons, of which some 80% are in the cerebellum (mostly granule cells) and only 19% in the cerebral cortex; the mouse brain has about $7 \times 10^7$. A cortical neuron receives several thousand synapses. The complete wiring diagram, or **connectome**, is known for *Caenorhabditis elegans* (302 neurons) and for the adult *Drosophila* brain (about 140 000 neurons and $5 \times 10^7$ synapses); for a cubic millimeter of mouse visual cortex it has been reconstructed by electron microscopy ([7.16.3](/7.16.3)).

The brain is expensive. The human brain is 2% of body mass but consumes about 20% of the resting oxygen, a power of about 20 W. Most of the energy is spent on signaling: restoring the ion gradients after action potentials and synaptic currents, and recycling transmitter. A bottom-up budget for rodent cortex gives about $3 \times 10^9$ ATP molecules per neuron per second at a mean **firing rate** of 4 Hz, with synaptic transmission the largest item ([7.14.5](/7.14.5#sec-5.2.3) gives the ATP ledger of the axon). The energy cost limits the mean firing rate to a few spikes per second and favors sparse codes ([7.16.20](/7.16.20)).

![Numbers of nervous systems. A: neurons and chemical synapses of whole nervous systems of *C. elegans*, the adult *Drosophila* brain, the mouse and the human brain (orders of magnitude); dashed lines mark 10, 10³ and 10⁴ synapses per neuron. B: fraction of neurons in the cerebral cortex, the cerebellum and the rest of the brain, with total neuron counts: in both species most neurons are in the cerebellum](./plots/brain-numbers.py)

## 2.5. Maps

**Definition 2.5.1 (Topographic Map)** A **topographic map** is an orderly arrangement of neurons in which neighboring neurons represent neighboring values of a stimulus feature or neighboring positions on a receptor surface. The main examples are *retinotopy* (position on the retina), *somatotopy* (position on the body surface) and *tonotopy* (sound frequency, from position along the cochlea).

Maps come in three forms. In a continuous map, such as the retinotopic map of the primary visual cortex, the represented variable changes smoothly with cortical position. In a discrete map, such as the olfactory bulb, a feature without a natural ordering is represented by discrete units: each glomerulus receives the axons of the sensory neurons that express one **odorant receptor** ([7.16.23](/7.16.23)). Mixed maps combine the two: in the rodent barrel cortex each whisker is represented by a discrete barrel, and the barrels are arranged in the same rows and arcs as the whiskers on the snout.

Maps are not proportional to the receptor surface. The area of cortex devoted to a region of the receptor surface reflects the density of receptors and the behavioral importance of the region: the somatosensory homunculus has large lips and fingertips, and the central retina dominates the visual cortex. The distortion is measured by the magnification factor.

**Definition 2.5.2 (Cortical Magnification Factor)** The linear **cortical magnification factor** $M(E)$ at eccentricity $E$ (angular distance from the center of gaze) is the distance on the cortex, in millimeters, that represents one degree of visual angle.

In human V1, $M(E) \approx M_0/(E + E_2)$ with $M_0 \approx 17.3\,\mathrm{mm}$ and $E_2 \approx 0.75^\circ$ (Horton and Hoyt). The inverse $1/M$ grows linearly with eccentricity, as does the spacing of retinal ganglion cells and the size of receptive fields, so each ganglion cell is represented by roughly the same cortical area wherever it is.

**Example 2.5.1 (The Central Visual Field Occupies Half of V1)** If magnification is isotropic, the cortical area representing the visual field within eccentricity $R$, summed over both hemispheres, is

$$
A(R) = \int_0^R M(E)^2\,2\pi E\,\mathrm{d}E = 2\pi M_0^2\left[\ln\frac{R + E_2}{E_2} + \frac{E_2}{R + E_2} - 1\right].
$$

With the values above, $A(10^\circ) \approx 3300\,\mathrm{mm^2}$ and $A(90^\circ) \approx 7200\,\mathrm{mm^2}$: the central $10^\circ$, about 1% of the area of the visual field, is represented by nearly half of the primary visual cortex.

:::

Maps serve computation. Because neurons that represent similar features are close, local circuits such as **lateral inhibition** and local recurrent excitation operate on similar features with short wires; and because the map is ordered, a bump of activity at one position can represent a continuous variable, the idea behind the continuous attractor networks of [7.16.44](/7.16.44). How maps are wired during development, by molecular gradients and by patterned activity, is the subject of [7.16.21](/7.16.21) and [7.16.22](/7.16.22).

## Summary

| Level | Unit | Key quantitative facts |
|---|---|---|
| Cells | cell types (Definition 2.1.1) | cortex: ~80% excitatory, ~20% inhibitory (PV, SST, 5-HT3AR); ~5000 transcriptomic clusters in the mouse brain |
| Glia | astrocytes, oligodendrocytes, Schwann cells, microglia (Definition 2.2.1) | glia : neurons ≈ 1 : 1 in the human brain; myelin and nodes of Ranvier (Definition 2.2.2) |
| Circuits | motifs (Definition 2.3.1) | recurrent excitation: gain and time constant multiplied by $1/(1-w)$ (Proposition 2.3.1); feedback inhibition: gain $1/(1 + w_{BI}w_{IB})$; convergence: signal-to-noise ratio $\propto \sqrt N$ |
| Regions | spinal cord, hindbrain, midbrain, diencephalon, telencephalon | human: $8.6 \times 10^{10}$ neurons, 80% in cerebellum; ~20 W, 20% of resting metabolism |
| Maps | topographic maps (Definition 2.5.1) | $M(E) \approx 17.3/(E + 0.75)\,\mathrm{mm}/^\circ$ in human V1 (Definition 2.5.2); central $10^\circ$ ≈ half of V1 (Example 2.5.1) |

## Questions

1. A pyramidal cell has $w = 0.9$ recurrent excitation. By what factor are its steady-state response and its time constant changed? What happens if neuromodulation raises $w$ to 1.05?

   **Answer** By Proposition 2.3.1 both are multiplied by $1/(1 - 0.9) = 10$: with $\tau = 10\,\mathrm{ms}$ the effective time constant is 100 ms. At $w = 1.05 > 1$ the linear system is unstable: activity grows exponentially with rate $(w - 1)/\tau$ until saturation or inhibition limits it, which in cortex corresponds to runaway excitation unless balanced by inhibition.

2. Show that feedback inhibition $\tau\dot r_B = -r_B + u - a r_I$, $\tau\dot r_I = -r_I + b r_B$ (linear regime) reduces the steady-state gain to $1/(1 + ab)$, and find the condition for a damped oscillation.

   **Answer** At steady state $r_I = b r_B$ and $r_B = u - ab\,r_B$, so $r_B = u/(1 + ab)$. The Jacobian $\frac{1}{\tau}\begin{bmatrix}-1 & -a\\ b & -1\end{bmatrix}$ has eigenvalues $\lambda = (-1 \pm \mathrm{i}\sqrt{ab})/\tau$: for any $ab > 0$ the approach is a damped oscillation with angular frequency $\sqrt{ab}/\tau$, which explains the onset overshoot in Figure 2. With synaptic delays the oscillation can become sustained.

3. Why does the cerebellum contain most of the brain's neurons yet only about 10% of its mass?

   **Answer** Most cerebellar neurons are granule cells, among the smallest neurons (soma 5–8 µm, four short dendrites, thin unmyelinated parallel-fiber axons), packed at very high density. The cerebral cortex, in contrast, has large pyramidal cells and a large volume of myelinated white matter connecting distant areas.

4. Using Example 2.5.1, estimate the cortical area devoted to the fovea ($E < 1^\circ$).

   **Answer** $A(1) = 2\pi M_0^2\,[\ln(1.75/0.75) + 0.75/1.75 - 1] = 2\pi \cdot 299 \cdot (0.847 + 0.429 - 1) \approx 520\,\mathrm{mm^2}$, about 7% of V1 for 0.01% of the visual field area.
