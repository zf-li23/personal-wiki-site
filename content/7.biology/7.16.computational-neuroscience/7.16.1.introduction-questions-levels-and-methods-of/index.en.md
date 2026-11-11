---
title: "Introduction: Questions, Levels and Methods of Neuroscience"
description: "What neuroscience asks and how it answers: nature and nurture (twin studies, prism adaptation of the barn owl's auditory map), the neuron doctrine, the two uses of the membrane potential, functional specialization, maps and parallel processing, Marr's levels of analysis and the three kinds of models, and the logic of observation, measurement and perturbation."
---

Neuroscience asks how a nervous system produces perception, action, memory and thought, and how it comes to be wired the way it is. The questions are old; what has changed in the last two decades is that almost every one of them can now be posed quantitatively. Genetically identified cells can be recorded by the thousands, switched on and off with light, and reconstructed synapse by synapse; theories can be simulated and compared with those data. This chapter sets out the questions, the principles on which the rest of the course builds, and the logic by which experiments and models support conclusions.

The physiology of membranes, synapses and sense organs has been described in [animal physiology](/7.14), and the physics of channels and of the action potential in [biophysics](/7.6.30). This course builds on both: it explains the molecular and circuit mechanisms, the experiments that revealed them, and the mathematical models that connect mechanism to function. Chapters on biological systems alternate with chapters on models, each model placed after the biology it describes and before the chapters that use it.

## 1.1. Nature and Nurture

Behavior results from the interaction of genetic programs with experience. Two examples show how each contribution can be measured.

**Example 1.1.1 (Twin Studies of Heritability)** Monozygotic twins share all their genes, dizygotic twins on average half; both usually share their family environment. In a **twin study** the correlation of a trait within monozygotic pairs, $r_{\mathrm{MZ}}$, and within dizygotic pairs, $r_{\mathrm{DZ}}$, are compared. Under the additive model with equal shared environments (Falconer's approximation), the **broad-sense heritability** is

$$
h^2 \approx 2(r_{\mathrm{MZ}} - r_{\mathrm{DZ}}).
$$

For IQ, a pooled analysis of more than 10 000 twin pairs gave $r_{\mathrm{MZ}} = 0.86$ and $r_{\mathrm{DZ}} = 0.60$, hence $h^2 \approx 0.52$: about half of the variance of IQ scores within the populations studied is associated with genetic differences. Twin studies give heritabilities of about 0.9 for height and 0.6–0.8 for schizophrenia.

Two cautions follow from the definition. Heritability is a property of a population in an environment, not of an individual or a trait in the abstract: it changes when the environment changes. And the "non-genetic" remainder includes not only experience but also prenatal conditions, somatic mutations and the stochasticity of development; genetically identical animals raised identically still differ in brain wiring and behavior.

:::

Many behaviors are innate: a newly hatched chick crouches when a hawk-shaped silhouette moves overhead but not when the same silhouette moves in the opposite direction and resembles a goose. Others are calibrated by experience during development. The barn owl (*Tyto alba*) hunts in darkness by sound and locates a mouse to within 1–2° in azimuth. The main azimuth cue is the interaural time difference (ITD), the difference between the arrival times of a sound at the two ears, which grows by roughly 2–3 µs per degree. In the midbrain, neurons of the external nucleus of the inferior colliculus (ICX) are tuned to ITD and form a map of auditory space that is aligned with the visual map of the optic tectum.

Knudsen and colleagues fitted young owls with prismatic spectacles that displaced the visual field by 23°. Over several weeks the ITD tuning of ICX neurons shifted by about the amount that realigned the auditory map with the displaced visual world (Figure 1). Removal of the prisms reversed the shift. Owls first fitted as adults adapted little; but adults that had adapted as juveniles readapted quickly to the same prisms, as if the juvenile experience had left an alternative set of connections that could be re-engaged. Anatomically, the axons from the central nucleus of the inferior colliculus to the ICX sprout in the adaptive direction, while the original connections persist. The example shows three general features of nurture in the brain: an instructive signal (here vision) guides the calibration of a second map; plasticity is large during a **critical period** and limited afterward; and learning can leave a lasting physical trace that makes relearning easier. The developmental mechanisms of maps and critical periods are the subject of [7.16.21](/7.16.21).

![Prism adaptation in the barn owl, as an illustrative model. A: ITD tuning of an ICX site that represents a fixed visual location, before prisms and after weeks of prism rearing: the best ITD shifts by about 50 µs, the ITD corresponding to the 23° displacement. B: the shift s(t) modeled as ds/dt = η(D − s) with instructive target D = 50 µs while the prisms are worn and 0 after removal; the learning rate η is high in juveniles, very low in naive adults, and intermediate in adults that adapted as juveniles](./plots/owl-prism.py)

## 1.2. The Neuron Doctrine

At the end of the nineteenth century two views of nervous tissue competed. Camillo Golgi, whose silver-chromate stain revealed the full arbor of a few randomly impregnated cells, held that axons fuse into a continuous network (the reticular theory). Santiago Ramón y Cajal, using the same stain on embryonic and young tissue where fewer elements overlap, argued that each neuron is a separate cell whose processes end freely near other neurons. From the shapes of the cells and the direction in which the processes point, Cajal also inferred the *law of dynamic polarization*: signals flow from dendrites and soma to the axon and on to the next neuron.

The **neuron doctrine** (its statement and the evidence from physiology are in [7.14.5](/7.14.5#sec-5.1.1)) was confirmed in the 1950s, when electron microscopy showed a cleft of 20–30 nm between pre- and postsynaptic membranes at a **chemical synapse**. The doctrine has exceptions that refine rather than refute it: **gap junctions** couple some neurons into electrical syncytia, dendrites of some cells release transmitter, and many neurons release several transmitters. The doctrine remains the organizing assumption of neuroscience: the neuron is the unit of signaling, connectivity is specific, and information flows in a defined direction across synapses.

## 1.3. Information Flow and the Two Uses of the Membrane Potential

A typical vertebrate neuron receives inputs on its dendrites and soma, integrates them, and sends an output along its axon to synaptic terminals. Two kinds of electrical signal carry the information (the ionic basis is in [7.14.4](/7.14.4)):

| | **Local potential** | **Action potential** |
|---|---|---|
| Amplitude | graded with stimulus, 0.1–20 mV | all-or-none, about 100 mV |
| Spread | passive, decays over a **length constant** of 0.1–1 mm | regenerative, conducted without decrement |
| Speed | electrotonic, set by the membrane time constant (1–50 ms) | 0.5–120 m/s |
| Summation | yes, spatial and temporal | no; refractory period |
| Code | analog | digital in amplitude, analog in timing and rate |
| Where | dendrites, soma, sensory endings, short neurons | axons |

The distinction is a design principle. Passive spread is cheap and analog but decays over a fraction of a millimeter; action potentials are energetically costly but carry signals over a meter. Neurons with short processes (retinal bipolar cells, many invertebrate interneurons) work without action potentials. At the synapse the digital signal is converted back into an analog one: the amount of transmitter released, and the postsynaptic potential, are graded. Much of this course is about how these conversions are made and how they compute.

## 1.4. Organizing Principles of the Brain

Three principles recur at every level.

1. *Functional specialization.* Different brain regions perform different functions. The evidence began with lesions (Broca's patient, who lost speech production after damage to the left inferior frontal cortex) and continued with electrical stimulation (Penfield's maps of the motor and somatosensory cortex) and recordings of single neurons. Specialization extends to cell types: within a region, genetically distinct neurons form distinct connections and serve distinct functions ([7.16.2](/7.16.2)).
2. *Maps.* Neighboring neurons often represent neighboring features: positions on the retina or the body surface, sound frequencies, or locations in space. Maps economize on wiring because neurons that compute together are close, and they allow local operations such as **lateral inhibition** to act on neighboring features ([7.16.2](/7.16.2#sec-2.5)).
3. *Massive parallelism.* Neurons are slow: they fire at most a few hundred spikes per second, and a synapse adds about a millisecond of delay. Yet a face is recognized within 150–200 ms, which leaves time for only about a hundred sequential steps of neuronal processing. The brain compensates by computing in parallel: about $8.6 \times 10^{10}$ neurons and some $10^{14}$ synapses in the human brain operate simultaneously, on a power budget of about 20 W.

## 1.5. Levels of Explanation

A nervous system can be described at many scales, from ion channels (nanometers, microseconds) to behavior (meters, years). An explanation at one scale does not replace explanations at another; the question is how they are linked.

**Definition 1.5.1 (Marr's Levels of Analysis)** An information-processing system can be understood at three levels:

1. the **computational level**: what problem the system solves, and why that solution is appropriate to the task;
2. the **algorithmic level**: how the input and output are represented, and by what procedure one is transformed into the other;
3. the **implementation level**: how the representation and the algorithm are realized physically.

The levels are loosely coupled: one computation admits many algorithms, and one algorithm many implementations. But they constrain one another, and in neuroscience the constraints from below matter. Sound localization in the barn owl illustrates all three (Figure 2). The computation is to estimate the azimuth of a sound from the ITD. The algorithm proposed by Jeffress in 1948 is a set of delay lines and coincidence detectors: axons from the two ears reach an array of neurons with systematically varying delays, and the neuron for which the delays compensate the ITD receives coincident input and fires most, so ITD is represented by the position of the most active neuron. The implementation in the owl's brainstem consists of axons from the nucleus magnocellularis that run as delay lines through the nucleus laminaris, whose neurons are coincidence detectors with submillisecond precision ([7.16.24](/7.16.24)). Mammals solve the same computational problem with a different algorithm, by comparing the activity of two broadly tuned populations.

![Marr's three levels of analysis applied to sound localization in the barn owl, and the parts of this course that address each level](./plots/marr-levels.py)

Models in neuroscience can be classified by the question they answer.

**Definition 1.5.2 (Descriptive, Mechanistic and Interpretive Models)** A **descriptive model** summarizes data compactly (a tuning curve, a receptive field filter); a **mechanistic model** explains how a phenomenon arises from components (the Hodgkin–Huxley model of the action potential from channel kinetics); an **interpretive model** explains why the system behaves as it does in terms of function (efficient coding as the reason for the shapes of receptive fields).

The three kinds are complementary and correspond roughly to Marr's levels read from the bottom up. A useful working definition follows: a computation is a representation together with an algorithm that transforms it. The course asks at each step which representation a circuit uses (a rate, a spike time, the position of a bump of activity, a probability distribution) and which operations transform it.

## 1.6. Observation, Measurement and Perturbation

Neuroscience establishes conclusions in two steps: observation and measurement reveal correlations between neural activity and stimuli or behavior; perturbation tests whether those correlations reflect causation.

Observation ranges from anatomy (which cells exist and how they connect) to recordings of activity during behavior. Measurements become quantitative when the variables are defined precisely: firing rate in spikes per second, response as a function of a stimulus parameter, the information that activity carries about a stimulus ([7.16.16](/7.16.16)). A correlation between the activity of a neuron and a behavior, however strong, does not show that the neuron causes the behavior: both may be driven by a third variable, the **confounding** familiar from causal inference.

Perturbation experiments manipulate a candidate cause and measure the effect. Their logic has two complementary forms.

**Definition 1.6.1 (Necessity and Sufficiency Experiments)** A **loss-of-function experiment** removes or silences a component (a gene, a cell type, a brain region) and asks whether a function fails; if it does, the component is *necessary* for the function under the conditions tested. A **gain-of-function experiment** activates or expresses the component where or when it is normally absent and asks whether the function appears; if it does, the component is *sufficient* to produce it in that context.

Neither form alone is conclusive. A loss-of-function effect may be indirect (silencing a region removes excitation from its targets, which then fail for other reasons) or masked by compensation over the days after a lesion; a gain-of-function effect may reflect an unphysiological activity pattern. Strong conclusions combine observation of activity in the intact animal, necessity and sufficiency with temporal precision, and quantitative agreement with a model. The tools that make this possible, especially genetic access to cell types and optogenetic control with millisecond resolution, are described in [7.16.3](/7.16.3).

Each method samples only part of the space of scales (Figure 3): electrophysiology resolves single spikes but samples few cells, imaging samples many cells but with slower indicators, and whole-brain methods trade cellular resolution for coverage. Combining methods across scales, and connecting them with models, is the characteristic strategy of modern neuroscience.

![Approximate spatial (A) and temporal (B) scales accessible to methods of neuroscience. Left bars span spatial scales from resolution to field of view; right bars span temporal scales from resolution to the longest practical recording. Electron microscopy images fixed tissue and has no temporal extent](./plots/scales-methods.py)

## 1.7. The Route of This Course

The course follows the flow of information and the hierarchy of scales. It begins with the cells of the nervous system and with methods, then treats the single neuron: ion channels, the action potential, and the dynamical systems theory that classifies neurons by the bifurcations of their excitability, with the simplified models used in network simulations. Synapses, dendrites and plasticity follow, and then the dynamics of networks. The middle of the course treats sensory systems, each paired with the theory it motivated: the coding of stimuli in spike trains, hierarchical models of vision, information theory and efficient coding, decoding and Bayesian perception, and the analysis of population activity. Motor systems come next, with models of control and of recurrent dynamics. The last parts cover the regulatory systems of the body, motivation and reward with reinforcement learning, memory and cognition with attractor networks, working memory, cognitive maps and decision-making, then representation learning, large-scale networks, learning algorithms in the brain, diseases and the evolution of nervous systems.

## Summary

- Twin studies estimate heritability, $h^2 \approx 2(r_{\mathrm{MZ}} - r_{\mathrm{DZ}})$ (Example 1.1.1), a population quantity that depends on the environment; experience calibrates neural maps, as prism adaptation of the barn owl's auditory map shows, with large plasticity in a critical period and lasting traces.
- The neuron doctrine: neurons are discrete cells connected by synapses, with information flowing from dendrites to axon.
- Graded local potentials carry analog signals over short distances; all-or-none action potentials carry signals over long distances; synapses convert digital signals back into analog ones.
- Organizing principles: functional specialization of regions and cell types, maps of features, and massive parallelism that compensates for slow components.
- Marr's levels (Definition 1.5.1): computation, representation and algorithm, implementation. Models are descriptive, mechanistic or interpretive (Definition 1.5.2).
- Correlation from observation is complemented by perturbation; loss-of-function tests necessity, gain-of-function tests sufficiency (Definition 1.6.1), and each method covers only part of the space of scales.

## Questions

1. In a population, $r_{\mathrm{MZ}} = 0.7$ and $r_{\mathrm{DZ}} = 0.5$ for a behavioral trait. Estimate the heritability and the fraction of variance due to the shared environment, assuming the additive model $r_{\mathrm{MZ}} = h^2 + c^2$, $r_{\mathrm{DZ}} = h^2/2 + c^2$.

   **Answer** Subtracting, $r_{\mathrm{MZ}} - r_{\mathrm{DZ}} = h^2/2 = 0.2$, so $h^2 = 0.4$ and $c^2 = 0.7 - 0.4 = 0.3$. The remaining $1 - h^2 - c^2 = 0.3$ is the non-shared environment (including developmental noise and measurement error).

2. Why could adult owls that had adapted to prisms as juveniles readapt, while naive adults could not? What does this predict about the anatomy?

   **Answer** Juvenile adaptation created a second set of connections (axons from the central nucleus sprouted into the parts of the ICX that represent the shifted locations) while the normal connections were retained. In adulthood, re-engaging existing synapses requires only changes in synaptic strength, which remain possible, whereas growing new axonal connections is limited after the critical period. The prediction, confirmed by anatomical tracing, is that adapted-as-juvenile adults have a broadened, double projection.

3. A drug that blocks a receptor abolishes a learned behavior when injected into region X. List two alternative explanations and an experiment that addresses each.

   **Answer** (i) The drug spreads to neighboring regions: control injections nearby, and a dose–response relation centered on X. (ii) Region X is needed for performance (motivation, motor output) rather than for the memory itself: test an unrelated behavior that uses the same output, or silence X only during learning versus only during recall with temporally precise tools such as optogenetics.

4. Place the following on Marr's levels: (a) "the retina whitens natural images to reduce redundancy"; (b) "a ring network maintains a bump of activity that moves when angular velocity input is applied"; (c) "the bump is held by NMDA-receptor-mediated recurrent excitation in the fly ellipsoid body".

   **Answer** (a) Computational: it states a goal and its justification. (b) Algorithmic: it specifies a representation (bump position) and a procedure (integration of velocity). (c) Implementation: it names the physical substrate.
