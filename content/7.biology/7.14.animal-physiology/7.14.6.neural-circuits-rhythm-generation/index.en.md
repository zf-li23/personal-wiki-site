---
title: Neural Circuits and Rhythm Generation
description: Firing and facilitated zones of a neuronal pool (a threshold-of-6 example); divergence and convergence, reciprocal and recurrent inhibition; afterdischarge (synaptic afterdischarge and reverberating circuits) as a recurrent excitation plus slow negative feedback model; sustained output, baseline and oscillatory output; fatigue and inhibition stabilize circuits; feedforward inhibition as a time gate (τ about 15 ms, window about 2 ms), shunting inhibition τ_eff = τ_m/(1 + g R_in), VIP→SST disinhibition; rate models; central pattern generators, half-center oscillators and adaptation variables; the stomatogastric ganglion, leech heartbeat, mollusc swimming and the segmental CPG of the lamprey.
source_hash: 37148beda271
---

Chapter 5 explained how a single neuron integrates synaptic inputs and passes the signal on to the next cell through a synapse ([7.14.5](/7.14.5)). The functions of the nervous system arise from circuits in which many neurons are wired together in particular patterns. The same neurons, wired differently, can amplify or confine a signal, make the output outlast the input, pick out inputs that are scattered in time, or generate a rhythm on their own in the absence of rhythmic input. This chapter first treats the classical circuit elements in the style of Guyton (neuronal pools, divergence and convergence, reciprocal inhibition, afterdischarge, oscillation), and then uses several phenomenological rate models to show how inhibition controls timing and gain and how rhythms emerge from connectivity. These circuits recur in later chapters: the **baroreceptor reflex** (Chapter 16), the respiratory rhythm (Chapter 20), and spinal reflexes and locomotion (Chapter 44). The models in this course are phenomenological simulations that serve to motivate the physiology; the dynamical-systems analysis (phase plane, bifurcations) and network theory belong to computational neuroscience ([7.16](/7.16)) and ordinary differential equations ([2.4](/2.4)).

## 6.1. Neuronal Pools

### 6.1.1. Stimulus Field, Discharge Zone and Facilitated Zone

**Definition 6.1.1 (Neuronal Pool)** A group of neurons in the central nervous system that are spatially clustered, follow common principles of structure and function, receive the same set of input fibers and send out a set of output fibers is called a **neuronal pool**.

A pool may contain only a few neurons (the ganglia of some invertebrates) or hundreds of millions (the cerebral cortex). Each input fiber branches after entering the pool and forms synapses with many neurons; the region of neurons that it can influence is called its stimulus field. The branches are dense in the central region of the field and become sparse quickly toward the periphery, so a fiber contributes many synapses to neurons near the center of its field and few to neurons at the edge.

**Example 6.1.1 (Discharge Zone and Facilitated Zone)** Suppose each neuron in the pool needs at least 6 excitatory synapses to be active simultaneously in order to fire. Input fiber 1 forms 6 synapses on neuron a and 3 synapses each on b and c; fiber 2 forms 6 synapses on d and also 3 synapses each on b and c.

- Only fiber 1 is excited: a fires; b and c receive only 3 synapses, which is below threshold, but their membrane potentials are closer to threshold, so they are facilitated.
- Only fiber 2 is excited: d fires, and b and c are facilitated.
- Both fibers are excited together: b and c each receive 6 synapses and fire, so the number of activated neurons increases from 2 to 4.

The stimulus field of each fiber is thus divided into two parts: a central discharge zone (activation zone), whose neurons are activated by this fiber alone, and a peripheral facilitated zone, whose neurons are facilitated and can fire only with the cooperation of other inputs. Where the facilitated zones of two fibers overlap, **spatial summation** takes effect. Inhibitory fibers have analogous zones: neurons in the central region are strongly inhibited and those in the periphery are partially inhibited.

### 6.1.2. Divergence and Convergence

**Definition 6.1.2 (Divergence and Convergence)** When the axon of a neuron branches and connects with many postsynaptic neurons, so that the signal from one input is passed to several neurons, the arrangement is called **divergence**; when the axons of many neurons terminate on the same neuron, so that several inputs meet on it, the arrangement is called **convergence**.

Divergence is of two kinds. In the amplifying type, a weak signal entering the pool activates more and more neurons: for example, one pyramidal cell can excite hundreds of spinal motor neurons, and each motor neuron innervates hundreds of muscle fibers. In the other type, the same signal is delivered to different target regions: for example, sensory signals in the dorsal column ascend to the cerebellum and the thalamus at the same time. Convergence is also of two kinds. Several terminals from the same source may act on one neuron, compensating for the inability of a single terminal to trigger firing. Inputs from different sources may act on one neuron, so that it integrates several kinds of information: a spinal motor neuron, for example, simultaneously receives input from **muscle spindle** afferents, the cortex, the brainstem, the cerebellum and interneurons of its own segment, and the synapses on its soma and dendrites number $10^4$–$10^5$. Sensory pathways are dominated by divergence, whereas the **final common path** of movement (the motor neuron) is the terminus of convergence.

### 6.1.3. Reciprocal Inhibition and Recurrent Inhibition

Sometimes one input must cause two outputs of opposite sign at the same time: one pool is excited and another is inhibited.

**Definition 6.1.3 (Reciprocal Inhibition)** When an afferent fiber directly excites one neuronal pool and, through a collateral, excites inhibitory interneurons that inhibit another, functionally antagonistic pool, the arrangement is called **reciprocal inhibition**.

The classic example, described by Sherrington, is the extensor and flexor pair. When the quadriceps is stretched, the Ia afferents of its **muscle spindles** monosynaptically excite the quadriceps motor neurons and, through Ia inhibitory interneurons, inhibit the motor neurons of the hamstrings; when the hip flexors contract during a step, the antagonist muscles of the buttock and the back of the leg are inhibited and relax (Chapter 44). Reciprocal inhibition is also one of the means by which the nervous system prevents excessive excitation.

Two other common patterns of inhibition are recurrent inhibition and **lateral inhibition**. Before leaving the spinal cord, the axon of a motor neuron gives off a collateral that excites a Renshaw cell, which in turn uses glycine to inhibit the same group of motor neurons and their neighbors; this is a **negative feedback** that limits the firing frequency of motor neurons. Lateral inhibition inhibits the neurons surrounding an excited center and thereby sharpens the spatial boundaries of sensory signals (Chapter 39).

## 6.2. Sustained Output and Circuit Stability

### 6.2.1. Afterdischarge

**Definition 6.2.1 (Afterdischarge)** The continuation of output from a neuronal pool for some time after the input has stopped is called **afterdischarge**.

Afterdischarge has two sources:

1. Synaptic afterdischarge: certain excitatory transmitters (especially those acting through **metabotropic receptors**, and neuropeptides) produce slow postsynaptic potentials lasting tens of milliseconds to seconds, so that a single input can keep the postsynaptic neuron firing throughout this period.
2. Reverberating (oscillatory) circuits: collaterals of the output neurons return to their own input, directly or through interneurons, forming a **positive feedback** loop in which the signal circulates, so that a single input gives rise to a train of outputs.

Adding facilitatory or inhibitory neurons to the circuit can adjust the strength of the reverberation. Reverberation does not go on forever; it is finally terminated by synaptic fatigue or slow inhibition. Reflex circuits themselves have this structure: the activity of the effector in turn stimulates the receptors in the circuit, maintaining or correcting the original reflex by feedback. The flexor withdrawal reflex, which continues for tens to hundreds of milliseconds after the stimulus has stopped, is an example of afterdischarge (Chapter 44).

A rate model expresses the idea of "recurrent excitation plus slow negative feedback" very clearly. Let $E(t)$ be the mean activity of a population of excitatory neurons and $z(t)$ a slow variable (a composite of synaptic fatigue, adaptation currents and slow inhibition). Then

$$
\tau_E\frac{\mathrm{d}E}{\mathrm{d}t} = -E + F\bigl(w_{EE}E - g z + I_{\mathrm{stim}}(t)\bigr),
\qquad
\tau_z\frac{\mathrm{d}z}{\mathrm{d}t} = -z + E, \tag{6.1}
$$

where $w_{EE}$ is the strength of recurrent excitation, $g$ is the strength of the slow negative feedback, $\tau_z \gg \tau_E$, $F$ is a sigmoidal activation function (6.4.1) and $I_{\mathrm{stim}}$ is a brief stimulus. Without $z$, a sufficiently large $w_{EE}$ gives $E = F(w_{EE}E)$ a stable high-activity fixed point: once the stimulus has pushed the circuit up, the activity is maintained indefinitely (persistent firing, one candidate mechanism of working memory). The variable $z$ accumulates slowly with activity and effectively lowers the recurrent strength from $w_{EE}$ to $w_{EE} - g$; when the high-activity point disappears as a result, the activity stops abruptly. The duration of the afterdischarge increases with $w_{EE}$, and $\tau_z$ sets its time scale; if $w_{EE} - g$ is still sufficient to sustain the high-activity point, the negative feedback cannot terminate it.

![Afterdischarge model with recurrent excitation and slow negative feedback (Eq. (6.1); $\tau_E = 10\,\mathrm{ms}$, $\tau_z = 0.5\,\mathrm{s}$, $F(u) = 1/(1 + \mathrm{e}^{-(u - 0.5)/0.08})$, stimulus duration $50\,\mathrm{ms}$). A: activity for different recurrent strengths at $g = 1$. For $w_{EE} = 0.6$ the activity vanishes when the stimulus ends; the larger $w_{EE}$ is, the longer the activity outlasts the stimulus (afterdischarge), until the slow variable $z$ has accumulated enough to make the high-activity state disappear and the activity stops abruptly. B: afterdischarge duration (time for which $E$ stays above 0.5 after the stimulus ends) as a function of $w_{EE}$. At $g = 1$, once $w_{EE}$ exceeds about 1.75 the negative feedback can no longer terminate the activity (persistent firing, truncated at the end of the 3 s simulation); with stronger negative feedback ($g = 2$) the afterdischarge is shorter and the range in which it can be terminated is wider.](./plots/afterdischarge.py)

### 6.2.2. Sustained Output, Baseline and Oscillation

Some neuronal pools fire continuously even without excitatory input. There are two sources: the neurons themselves are highly excitable (the membrane potential is close to threshold, or there are intrinsic pacemaker currents), or there are reverberating circuits that do not fatigue completely. The significance of continuous firing is that it provides a baseline that can be adjusted up and down: excitatory input raises the firing frequency and inhibitory input lowers it, so a neuron that can only fire (it cannot "fire negatively") is able to transmit information in both directions. The control of the heart and blood vessels by sympathetic **tone** works in this way: an increase or decrease in sympathetic activity changes heart rate and vessel caliber in either direction (Chapters 7 and 16).

Some circuits produce a sustained rhythmic output, for example the respiratory centers. An incoming excitatory signal can raise both the amplitude and the frequency of the rhythm: when the carotid body senses hypoxia, each burst of the respiratory neurons is stronger and the rhythm is faster, which appears as deeper and faster breathing (Chapter 20).

### 6.2.3. Circuit Stability: Fatigue and Inhibition

Divergence and recurrent excitation connect almost every region of the brain, directly or indirectly, with other regions. Without restraint, excitation in one region would spread through the whole brain and form a sustained oscillation, which is what happens in an epileptic seizure. The nervous system maintains stability with two kinds of mechanisms:

- Inhibitory circuits: one is negative feedback to the neurons at the origin of the same pathway (recurrent inhibition); the other is the global inhibition that some neuronal pools exert on wide brain regions, for example the inhibition of the muscle control system by the basal ganglia.
- Synaptic fatigue: when a pathway is overused, synaptic transmission gradually weakens (short-term depression), which attenuates an excessively strong reflex and relatively strengthens weak pathways. On longer time scales the number of postsynaptic receptors is up- or down-regulated, and neurons scale their synaptic strengths globally according to their mean activity (homeostatic synaptic scaling; Turrigiano et al., 1998), keeping activity within a set range.

## 6.3. Control of Timing and Gain by Inhibition

### 6.3.1. Feedforward Inhibition and the Time Window

**Definition 6.3.1 (Feedforward Inhibition)** When an afferent fiber excites both a principal neuron and an inhibitory interneuron, and the latter inhibits the principal neuron after the delay of one additional synapse, the arrangement is called **feedforward inhibition**.

The membrane **time constant** of a single pyramidal cell, $\tau_{\mathrm{m}} \approx 15\,\mathrm{ms}$, determines over how long a period it can add inputs together (the **temporal summation** of Chapter 5). Considering the single cell alone, it should sum any inputs that arrive within $15\,\mathrm{ms}$. Pouille and Scanziani (2001) found in hippocampal CA1 slices that after stimulation of the Schaffer collaterals the effective integration window of the pyramidal cell is only about $2\,\mathrm{ms}$; when GABAergic inhibition is blocked, the window returns to the order of the membrane time constant. The reason lies in the circuit: the afferent fibers also excite parvalbumin (PV)-positive basket cells, which, after the delay of one synapse, $\delta \approx 1$–$2\,\mathrm{ms}$, produce strong inhibition on the soma and proximal dendrites of the pyramidal cell and cut off the tail of the EPSP. Only inputs arriving within $\delta$ can add before the inhibition arrives. Feedforward inhibition turns the pyramidal cell from a forgiving integrator into a precise coincidence detector; the window is set by the circuit parameter $\delta$ rather than the cell parameter $\tau_{\mathrm{m}}$, and the ratio of the two is about 10.

![Feedforward inhibition narrows the integration window of a pyramidal cell (passive point neuron: $\tau_{\mathrm{m}} = 15\,\mathrm{ms}$, resting potential $-65\,\mathrm{mV}$, reversal potentials of excitation and inhibition $0$ and $-70\,\mathrm{mV}$; each afferent volley excites the cell directly and, through a disynaptic delay of $1.5\,\mathrm{ms}$, evokes a stronger inhibition; parameters are for illustration only). A: potential evoked by a single volley, without and with feedforward inhibition. B: peak depolarization evoked by two volleys (relative to a single volley) as a function of the interval: without inhibition the two EPSPs sum over about one membrane time constant, whereas with feedforward inhibition only inputs separated by a few milliseconds or less can sum. C: a shunting conductance shortens the effective time constant, $\tau_{\mathrm{eff}} = \tau_{\mathrm{m}}/(1 + g_{\mathrm{shunt}}R_{\mathrm{in}})$ ($R_{\mathrm{in}} = 100\,\mathrm{M\Omega}$, $\tau_{\mathrm{m}} = 10\,\mathrm{ms}$); a $10\,\mathrm{nS}$ shunt halves it.](./plots/feedforward-window.py)

### 6.3.2. Shunting Inhibition

When the reversal potential of an inhibitory channel is close to the **resting potential**, its opening hardly changes the membrane potential but increases the membrane conductance.

**Formula 6.3.1 (Shunting Inhibition)** Let the input resistance of the neuron be $R_{\mathrm{in}}$ (leak conductance $g_{\mathrm{L}} = 1/R_{\mathrm{in}}$), the membrane capacitance $C$, and the membrane time constant $\tau_{\mathrm{m}} = CR_{\mathrm{in}}$. After a shunting conductance $g_{\mathrm{shunt}}$ is added,

$$
\tau_{\mathrm{eff}} = \frac{C}{g_{\mathrm{L}} + g_{\mathrm{shunt}}} = \frac{\tau_{\mathrm{m}}}{1 + g_{\mathrm{shunt}}R_{\mathrm{in}}},
\qquad
\Delta V = \frac{I_{\mathrm{syn}}}{g_{\mathrm{L}} + g_{\mathrm{shunt}}}. \tag{6.2}
$$

A shunt both shortens the integration window and scales down proportionally the subthreshold depolarization produced by the same excitatory current. With $R_{\mathrm{in}} = 100\,\mathrm{M\Omega}$ and $\tau_{\mathrm{m}} = 10\,\mathrm{ms}$, $g_{\mathrm{shunt}} = 10\,\mathrm{nS}$ halves $\tau_{\mathrm{eff}}$ to $5\,\mathrm{ms}$. Shunting inhibition is most effective when it lies between the excitatory synapse and the soma, where it can "veto" distal inputs. For subthreshold potentials it acts divisively, but its effect on firing frequency is often closer to subtractive (Holt and Koch, 1997), because during firing the membrane potential is clamped near threshold.

### 6.3.3. Disinhibition

The inhibition of inhibition is excitation: for two connections of negative sign in series, the net sign of the whole pathway is $(-1)\times(-1) = +1$.

**Definition 6.3.2 (Disinhibition)** When an inhibitory neuron inhibits another inhibitory neuron, thereby releasing a third neuron from the latter's inhibition and increasing its activity, the arrangement is called **disinhibition**.

The disinhibitory circuit in the cortex consists of three classes of interneurons: somatostatin (SST)-positive cells inhibit the distal dendrites of pyramidal cells, and vasoactive intestinal peptide (VIP)-positive cells mainly inhibit SST cells. When VIP cells are activated (for example when an animal starts to run or attends to a stimulus, through input from other brain regions and cholinergic and serotonergic modulation), SST cells are inhibited and the response gain of pyramidal cells to their dendritic input rises markedly; this increase is spatially and feature selective (Pi et al., 2013). The advantage of disinhibition is that it can "open a gate" without directly exciting the principal neurons: only neurons that already receive excitatory input are enhanced. The **basal ganglia** use the same logic: the striatum inhibits the internal segment of the globus pallidus, which tonically inhibits the thalamus; activity of the striatum thus releases the thalamus from inhibition and allows a motor program to be executed (Chapter 45).

## 6.4. Generation of Rhythm

### 6.4.1. From Hodgkin–Huxley to Rate Models

The dynamics of a single neuron are described by equations of the Hodgkin–Huxley type ([7.6.30](/7.6.30#sec-30.6)), but to understand how circuits of many neurons generate rhythms and afterdischarge, what matters is not how each channel opens and closes but the mean activity of a population of neurons.

**Definition 6.4.1 (Rate Model)** A model that describes the activity of a population of neurons by its mean firing rate $x(t)$, satisfying

$$
\tau\frac{\mathrm{d}x}{\mathrm{d}t} = -x + F\Bigl(\sum_j w_j x_j + I\Bigr) \tag{6.3}
$$
is called a **rate model**: $\tau$ is the time constant of the change of activity (a composite of membrane and synaptic time constants), $-x$ expresses the decay of activity in the absence of input, $w_j$ is the strength of the connection from other populations (positive for excitation, negative for inhibition), $I$ is the external input, and $F$ is the activation function that converts total input into firing rate (for example the rectifier $F(u) = \max(0, u)$ or a sigmoid).

Wilson and Cowan (1972) used rate equations for a pair of excitatory and inhibitory populations to study cortical oscillations and multistability. Eq. (6.3) sacrifices the timing information of single action potentials in exchange for low-dimensional dynamics that can be analyzed intuitively; the model of 6.2.1 and the models below all belong to this class. Negative feedback needs a delay to produce oscillation, and positive feedback coupled with negative feedback can produce relaxation oscillations; these general principles are discussed in [7.9.16](/7.9.16#sec-16.4).

### 6.4.2. Central Pattern Generators

Breathing, chewing, swallowing, walking, swimming and flying are all rhythmic movements. Where does their rhythm come from? One possibility is a reflex chain: the sensory feedback of each step triggers the next. Another is that the center itself generates the rhythm.

**Definition 6.4.2 (Central Pattern Generator)** A neural circuit that, in the absence of rhythmic sensory input or descending commands, can autonomously generate rhythmic motor output with fixed phase relationships is called a **central pattern generator** (CPG).

The evidence comes from deafferentation experiments. Graham Brown (1911) found that in a cat whose dorsal roots had been cut and all sensory feedback removed, the spinal cord could still produce an alternating flexor–extensor stepping rhythm; Wilson (1961) found that a deafferented locust could still produce the flight rhythm, only at a lower frequency. The rhythmic motor nerve output produced by an isolated spinal cord or ganglion under pharmacological activation is called "fictive locomotion" and is the standard preparation for studying CPGs. Sensory feedback and descending commands are not unimportant: they start and stop the CPG and regulate its frequency and phase, so that movement is adapted to load and terrain.

CPGs generate rhythm in two ways:

- Pacemaker type: one neuron or a group of neurons has intrinsic oscillation (for example by alternating dominance of a persistent $\ce{Na+}$ current, a low-threshold $\ce{Ca^2+}$ current and a $\ce{Ca^2+}$-activated $\ce{K+}$ current) and drives other neurons in the network. The respiratory rhythm of the preBötzinger complex in the medulla is thought to combine pacemaker properties with network action (Chapter 20).
- Network type: no single neuron oscillates, and the rhythm arises from the pattern of connections, the synaptic strengths and delays, and activity-dependent adaptation. The simplest is the half-center oscillator.

### 6.4.3. Half-Center Oscillators

**Definition 6.4.3 (Half-Center Oscillator)** A circuit in which two neurons (or two groups) inhibit each other, each receives a sustained excitatory drive, and the two alternate in activity when some slow process (adaptation, synaptic fatigue, postinhibitory rebound) makes the active side gradually lose its advantage is called a **half-center oscillator**.

Graham Brown (1914) proposed this concept to explain the alternation of flexors and extensors. In a rate model:

**Formula 6.4.1 (Rate Model of the Half-Center Oscillator)** Let $x_A$ and $x_B$ be the activities of the two half-centers and $a_A$ and $a_B$ their adaptation variables,

$$
\begin{aligned}
\tau_x\frac{\mathrm{d}x_A}{\mathrm{d}t} &= -x_A + F(I_0 - w_I x_B - g a_A), &
\tau_a\frac{\mathrm{d}a_A}{\mathrm{d}t} &= -a_A + x_A, \\
\tau_x\frac{\mathrm{d}x_B}{\mathrm{d}t} &= -x_B + F(I_0 - w_I x_A - g a_B), &
\tau_a\frac{\mathrm{d}a_B}{\mathrm{d}t} &= -a_B + x_B,
\end{aligned}
\tag{6.4}
$$

where $I_0$ is the sustained background excitation, $w_I$ is the strength of mutual inhibition, $g$ is the strength with which adaptation inhibits the cell's own activity, and $\tau_a > \tau_x$.

With mutual inhibition only ($g = 0$), the side that gains the upper hand continues to suppress the other, and the system rests in a "winner-take-all" steady state without oscillating. When sufficiently strong slow adaptation is added, the following happens: while A is active, $a_A$ rises gradually and the effective drive of A, $I_0 - g a_A$, falls; when its output becomes too low to suppress B, B is released from inhibition and becomes active ("escape"), in turn inhibits A, and starts to accumulate its own adaptation; and so on cyclically. The period is determined mainly by $\tau_a$ and $g$: the stronger the adaptation, the sooner the active side loses its advantage, and the shorter the period and the smaller the amplitude. This rhythm is not a property of any one neuron; it results from the joint action of mutual inhibition, sustained drive and slow negative feedback. In addition to adaptation, biological half-centers often use postinhibitory rebound (the hyperpolarization-activated current $I_{\mathrm{h}}$) and short-term depression of the inhibitory synapses to achieve alternation.

![Half-center oscillator (Formula 6.4.1; $F(u) = \max(0, u)$, $I_0 = 1$, $w_I = 2$, $\tau_x = 50\,\mathrm{ms}$, $\tau_a = 0.6\,\mathrm{s}$, A initially slightly dominant). A: at $g = 2$ the two half-centers are active alternately, like flexor and extensor; the dashed line is the adaptation variable of A, which accumulates while A is active until A loses its advantage and B becomes active. B: period and amplitude as functions of the adaptation strength $g$. Below about $g = 1.1$ mutual inhibition produces only a winner-take-all steady state (shaded); beyond it a rhythm appears, and the stronger the adaptation, the shorter the period and the smaller the amplitude.](./plots/half-center.py)

Phase-plane and bifurcation analysis can give the conditions for the appearance of oscillation rigorously and distinguish the two switching mechanisms, "escape" and "release"; these belong to computational neuroscience ([7.16](/7.16)); the stability theory of ordinary differential equations is in [2.4](/2.4).

## 6.5. Evolution and Comparative Aspects

CPGs are among the most successful areas of comparative neurophysiology, and many basic principles were discovered in invertebrates, whose neurons are few and can be identified one by one.

The crustacean stomatogastric ganglion. The stomatogastric ganglion of lobsters and crabs has only about 30 neurons and produces two rhythms: the pyloric rhythm (about $1\,\mathrm{Hz}$, controlling the filtering movements of the pyloric part of the stomach) and the slower gastric mill rhythm. The core of the pyloric rhythm is a pacemaker neuron (AB) and two PD neurons coupled to it through **electrical synapses**, and the remaining neurons are arranged in fixed phases by inhibitory synapses. This small circuit gives three general conclusions:

1. Neuromodulators reconfigure circuits: more than 30 amine and neuropeptide modulators change the intrinsic currents and synaptic strengths of the neurons, can combine the same set of neurons into different rhythms, and can even "borrow" neurons belonging to one circuit for another (Marder et al.). The anatomical wiring diagram alone does not determine the output of the circuit.
2. Degeneracy: in a model network simulated for twenty million parameter combinations, very different combinations of conductances and synaptic strengths were found to produce almost identical pyloric rhythms (Prinz, Bucher and Marder, 2004); the mRNA levels of **ion channels** in the same neuron of different individuals can differ several-fold. Functional stability does not require fixed parameters.
3. Temperature compensation: the frequency of the crab pyloric rhythm increases with temperature ($Q_{10}$ about 2), but the phase relationships of the firing of the neurons remain almost unchanged between $7$ and $23\,^\circ\mathrm{C}$, so the stomach of a **poikilotherm** works normally at different water temperatures.

The leech heartbeat. The two lateral heart tubes of the leech contract rhythmically (one in a rear-to-front peristaltic wave, the other nearly synchronously, the two switching every few tens of beats); the rhythm arises from two pairs of mutually inhibiting heart interneurons in the third and fourth ganglia: each pair is a half-center oscillator, and the mechanism of alternation is the postinhibitory-rebound $I_{\mathrm{h}}$ current and the low-threshold $\ce{Ca^2+}$ current (Calabrese et al.). This is an example in which a half-center oscillator has been fully analyzed at the cellular level.

Mollusc swimming. When the sea slug *Tritonia* is touched by a starfish, it escapes by swimming with a series of dorsal–ventral flexions of the whole body; the excitation, inhibition and delays among three classes of identifiable interneurons (the dorsal swim interneuron DSI, C2 and the ventral swim interneuron VSI) are sufficient to generate this rhythm (Getting). In this circuit the serotonergic DSI acts as both transmitter and modulator and strengthens the synapses of C2, an example of "intrinsic neuromodulation".

Lamprey swimming. The spinal cord of the lamprey has about 100 segments, and each segment (even a fragment of one or two segments) can produce a left–right alternating rhythm; the left–right alternation depends on glycinergic **reciprocal inhibition** across the midline (Grillner et al.). The phase lag between adjacent segments is about 1% of the period, independent of frequency, so a wavelength of about one body length is always maintained along the body, and the wave travelling from head to tail propels the body forward. The traveling wave of the chain of segmental CPGs is discussed in Chapter 44.

Comparison. From molluscs, annelids and arthropods to vertebrates, rhythm circuits reuse the same set of building blocks: mutually inhibiting half-centers, intrinsic pacemaker currents, slow adaptation or rebound, and the regulation of these by neuromodulators. The locomotor CPGs of vertebrates lie in the spinal cord and are started and speed-controlled by motor regions of the brainstem; the CPGs of invertebrates lie in the segmental ganglia and are started by command neurons of the cephalic ganglia. That phyla have independently evolved similar principles suggests that rhythm generation is constrained to a few dynamical schemes.

## Summary

| Circuit element | Structure | Function |
|---|---|---|
| Neuronal pool (Definition 6.1.1) | The stimulus field of an input fiber is divided into a discharge zone and a facilitated zone (Example 6.1.1) | Spatial summation; grading and selection of signals |
| Divergence and convergence (Definition 6.1.2) | One to many; many to one | Amplification and distribution; integration of several sources |
| Reciprocal inhibition (Definition 6.1.3) | Afferent excites one pool and, through inhibitory interneurons, inhibits the antagonist pool | Coordination of antagonist muscles; prevents excessive excitation |
| Recurrent inhibition, lateral inhibition | Output inhibits itself or its neighbors through interneurons | Limits firing frequency; sharpens boundaries |
| Afterdischarge (Definition 6.2.1) | Slow synaptic potentials; reverberating circuits | Turns a brief input into a sustained output (Eq. (6.1)) |
| Sustained output and oscillation | Intrinsic excitability or incompletely fatiguing reverberation | A baseline adjustable in both directions; rhythm |
| Feedforward inhibition (Definition 6.3.1) | Afferent excites the principal cell and inhibits it after a delay $\delta$ | Integration window shortened from $\tau_{\mathrm{m}} \approx 15\,\mathrm{ms}$ to $\delta \approx 2\,\mathrm{ms}$ |
| Shunting inhibition (Formula 6.3.1) | Conductance with reversal potential near rest | $\tau_{\mathrm{eff}} = \tau_{\mathrm{m}}/(1 + gR_{\mathrm{in}})$; divisively reduces subthreshold potentials |
| Disinhibition (Definition 6.3.2) | Inhibitory neuron inhibits an inhibitory neuron | Selective opening of pathways (VIP→SST→pyramidal cell, basal ganglia) |
| Half-center oscillator (Definition 6.4.3) | Mutual inhibition + sustained drive + slow adaptation (Formula 6.4.1) | Alternating rhythm; the basic building block of the CPG (Definition 6.4.2) |

- Circuit stability depends on inhibitory circuits, synaptic fatigue and homeostatic synaptic scaling; without them, epileptiform spread and oscillation appear.
- The rate model (Definition 6.4.1) describes circuits by the mean activity of populations; the afterdischarge model shows that recurrent excitation causes sustained activity and slow negative feedback terminates it; the half-center model shows that without slow adaptation there is only winner-take-all.
- Small invertebrate circuits revealed neuromodulatory reconfiguration, degeneracy of parameters and temperature compensation; the chain of segmental CPGs of the lamprey produces a traveling wave of constant wavelength.

## Questions

1. In Example 6.1.1, suppose there is also an inhibitory interneuron between fiber 1 and fiber 2, such that when fiber 1 is excited it produces on b and c an inhibition equivalent to 2 excitatory synapses. Which neurons fire when both fibers are excited together? What does this illustrate?

   **Answer** Neurons b and c each receive a net excitation of $3 + 3 - 2 = 4$ synapses, below the threshold of 6, and do not fire; only a and d fire. The inhibition "trims away" the facilitated zones, so that the stimulus fields of the two inputs no longer merge in the middle, and the output keeps two separate foci: this is the principle by which **lateral inhibition** sharpens spatial resolution.

2. In Eq. (6.1), if the slow variable is removed ($g = 0$) and $w_{EE}$ is sufficiently large, what happens after the stimulus ends? Which physiological phenomenon might use this property? Why is it also dangerous?

   **Answer** $E = F(w_{EE}E)$ has a low and a high stable point (**bistability**); once the stimulus has pushed the system to the high-activity point, the activity is maintained indefinitely after the stimulus ends. This can serve as a mechanism of short-term memory (the persistent firing of the prefrontal cortex in delayed-response tasks). The danger is that there is no termination mechanism: any chance strong input could "lock" the circuit in the high-activity state and, through divergence, spread to other regions, like an epileptic seizure; real circuits therefore always have fatigue, adaptation or inhibitory feedback.

3. Estimate: the membrane time constant of a hippocampal pyramidal cell is $15\,\mathrm{ms}$ and the disynaptic delay of feedforward inhibition is $1.5\,\mathrm{ms}$. If two excitatory inputs arrive $5\,\mathrm{ms}$ apart, can they sum with and without feedforward inhibition, respectively? How would blocking $\mathrm{GABA_A}$ receptors change the response of the cell to temporally imprecise input?

   **Answer** Without feedforward inhibition, the first EPSP still retains most of its amplitude after $5\,\mathrm{ms}$ (a decay factor of the order of $\mathrm{e}^{-5/15} \approx 0.72$), and the two can sum. With feedforward inhibition, the inhibition evoked by the first input arrives after $1.5\,\mathrm{ms}$, truncates its EPSP and depresses the membrane potential, and the second input can hardly add to it (in panel B the gain is 1 for intervals beyond about $4\,\mathrm{ms}$). Blocking $\mathrm{GABA_A}$ receptors restores the window to the order of $\tau_{\mathrm{m}}$, and the cell then also responds to temporally scattered background input and loses its temporal precision (exactly as in the experiment of Pouille and Scanziani).

4. What mainly determines the period of the half-center oscillator (Formula 6.4.1)? If an animal wants to walk faster, which "parameters" can it adjust?

   **Answer** The period is determined by the time the active side needs to lose its advantage, that is, by the time constant $\tau_a$ and the strength $g$ of the adaptation variable, and by the relative size of the drive $I_0$ and the mutual inhibition $w_I$: the faster and stronger the adaptation and the weaker the drive (the closer to the switching threshold), the shorter the period. In organisms the counterparts are as follows. Modulators change the adaptation currents (such as the $\ce{Ca^2+}$-activated $\ce{K+}$ current) or $I_{\mathrm{h}}$. The descending drive from brainstem motor regions changes $I_0$ (in the model, a stronger drive makes each half-center last longer, so an increase in frequency also requires the cooperation of adaptation or inhibition). Sensory feedback (such as hip angle and load) advances or delays the switch at particular phases of the gait cycle.

5. (Open question) Studies of the stomatogastric ganglion show that many different parameter combinations can produce the same rhythm. What does this imply for studying neural circuits by "knocking out one gene and observing the phenotype"?

   **Answer** Key points: if a function can be realized by many parameter combinations, then after one component is removed the circuit may recover function through compensatory changes in other conductances (during development or under homeostatic regulation), so that the phenotype is mild or absent; this does not show that the component plays no role in the normal circuit. Conversely, different individuals may respond differently to the same perturbation, depending on where in parameter space they originally lie. It is therefore necessary to measure several parameters and their correlations in many individuals, to understand "functionally equivalent parameter sets" together with models, and to attend to the difference between acute and chronic manipulations.
