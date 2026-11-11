---
title: Long-Term Synaptic Plasticity
description: "The synaptic hypothesis of memory and Hebb's postulate; LTP at the CA3–CA1 synapse: induction by NMDA receptors, expression by AMPA receptor insertion, early and late phases; CaMKII autophosphorylation and a bistable switch model; LTD and the calcium control hypothesis, metaplasticity; spike-timing-dependent plasticity and its trace implementation; synaptic scaling; synaptic tagging and capture; behavioral timescale synaptic plasticity and one-shot place fields; neuromodulators as third factors and eligibility traces."
---

**Short-term plasticity** ([7.16.12](/7.16.12)) changes synaptic strength for a second; learning requires changes that last hours to a lifetime. This chapter treats the long-lasting forms of **synaptic plasticity** at the level of synapses and molecules: how a brief pattern of activity is detected, how it is converted into a change of synaptic strength, how that change is made to last although every protein in the synapse is replaced within days, and how the rules depend on the timing of spikes, on the overall activity of the neuron and on neuromodulators. Long-term potentiation and depression, their basic definitions and their place in the physiology of the synapse are in [7.14.5](/7.14.5#sec-5.5); the receptors that detect coincident activity are in [7.16.10](/7.16.10), and the dendritic signals that carry the postsynaptic part of the coincidence in [7.16.13](/7.16.13). The consequences of these rules for networks, receptive fields and maps are worked out mathematically in [7.16.22](/7.16.22); memory systems, the hippocampus and engrams follow in [7.16.38](/7.16.38) and [7.16.42](/7.16.42), and the role of dopamine as a teaching signal in [7.16.39](/7.16.39).

## 14.1. The Synaptic Hypothesis of Memory

Cajal suggested in 1894 that learning might strengthen the connections between neurons, and Hebb (1949) formulated the condition under which this should happen: "When an axon of cell A is near enough to excite a cell B and repeatedly or persistently takes part in firing it, some growth process or metabolic change takes place in one or both cells such that A's efficiency, as one of the cells firing B, is increased." In its modern form, **Hebb's rule** ([Definition 21.6.1](/7.16.21#def-21.6.1)) requires a change that is *local* (it depends only on the activity of the two cells it connects), *conjunctive* (it requires pre- and postsynaptic activity together) and *specific* (it affects only the synapses that took part).

The synaptic hypothesis has two parts (Luo): memory is stored as the pattern of strengths of synaptic connections, and learning modifies these strengths. Neither part can be proved by showing that synapses are plastic; the hypothesis predicts a set of relations between plasticity and behavior, which have been tested one by one (Martin, Grimwood and Morris, 2000):

| Criterion | Prediction | Example of a test |
|---|---|---|
| Detectability | Learning changes synaptic strength in the relevant circuit | Inhibitory avoidance learning potentiates a subset of CA1 synapses and occludes subsequent LTP (Whitlock and colleagues, 2006) |
| Anterograde alteration | Blocking plasticity impairs learning | Infusing the NMDA receptor antagonist APV into the hippocampus impairs spatial learning in the water maze (Morris and colleagues, 1986) |
| Retrograde alteration | Reversing the change erases the memory | Optogenetic LTD of auditory inputs to the amygdala inactivates a conditioned fear memory, and LTP of the same inputs reactivates it (Nabavi and colleagues, 2014) |
| Mimicry | Inducing the change creates a memory | Partly achieved by optogenetic activation and potentiation of defined inputs |

The two forms of plasticity most studied are **long-term potentiation** (LTP) and **long-term depression** (LTD) at the synapse from CA3 Schaffer collaterals to CA1 pyramidal cells in the hippocampus, because the hippocampus is required for the formation of declarative memories ([7.16.42](/7.16.42)) and the synapse is accessible in slices. The rules found there are instructive for other synapses, but each synapse has its own variant.

## 14.2. Long-Term Potentiation at the CA1 Synapse

### 14.2.1. Induction and Its Properties

Bliss and Lømo (1973) stimulated the perforant path of anesthetized rabbits at $10$–$20\,\mathrm{Hz}$ for $10$–$15\,\mathrm{s}$ and found that the field EPSP in the dentate gyrus was enhanced for hours; in chronically implanted animals the enhancement lasted weeks. In slices of CA1, LTP is induced by a tetanus ($100\,\mathrm{Hz}$ for $1\,\mathrm{s}$), by theta-burst stimulation (bursts of four pulses at $100\,\mathrm{Hz}$ repeated at $5\,\mathrm{Hz}$, the frequency of the hippocampal theta rhythm), or by a pairing protocol in which low-frequency presynaptic stimulation is paired with depolarization of the voltage-clamped postsynaptic cell to about $0\,\mathrm{mV}$. The last protocol shows that neither high-frequency presynaptic activity nor postsynaptic spikes are required: what is required is glutamate release together with postsynaptic depolarization.

**Definition 14.2.1 (Properties of LTP)** LTP at the CA1 synapse shows **input specificity** (only the synapses active during induction are potentiated, not inactive synapses on the same cell), cooperativity of induction (a weak input must be strong enough, by the number of fibers recruited, to depolarize the cell) and **associativity** (a weak input that alone cannot induce LTP is potentiated if it is active together with a strong input to the same cell).

All three properties follow from one molecule. The **NMDA receptor** ([Definition 10.3.2](/7.16.10#def-10.3.2)) conducts only when glutamate is bound and the **magnesium block** is relieved by depolarization; it is therefore a **coincidence detector** of the two conditions (Definition 10.3.4), and the $\ce{Ca^2+}$ it admits stays in the activated spine ([7.16.13](/7.16.13#sec-13.7)). Associativity is Hebb's conjunction with the strong input supplying the depolarization; cooperativity is the same conjunction supplied by the weak input itself. The decisive experiments: APV blocks the induction of LTP but not its expression once established (Collingridge, Kehl and McLennan, 1983); chelating postsynaptic $\ce{Ca^2+}$ with BAPTA blocks induction (Lynch and colleagues, 1983), and uncaging $\ce{Ca^2+}$ in the postsynaptic cell potentiates synapses (Malenka and colleagues, 1988). Mice with a deletion of the GluN1 subunit restricted to CA1 pyramidal cells lack LTP at these synapses and have impaired spatial memory (Tsien, Huerta and Tonegawa, 1996).

### 14.2.2. Expression: AMPA Receptors and Spines

LTP is expressed mostly postsynaptically at CA1 synapses, by more and better **AMPA receptors**.

1. *Insertion.* Recombinant GluA1 tagged with GFP is driven into spines by LTP-inducing stimulation (Shi and colleagues, 1999); exocytosis of receptors from recycling endosomes, lateral diffusion and capture by the PSD increase the number of receptors at the synapse (the "slot" picture of [7.16.10](/7.16.10#sec-10.3.3)).
2. *Phosphorylation.* CaMKII phosphorylates GluA1 at Ser831, which increases **single-channel conductance**, and the TARP stargazin, which traps receptors in the PSD; PKA phosphorylates Ser845, which promotes surface delivery.
3. *Unsilencing.* Many young synapses have NMDA but no AMPA receptors; LTP inserts AMPA receptors and converts these silent synapses into functional ones (Isaac, Nicoll and Malenka, 1995; Liao, Hessler and Malinow, 1995).
4. *Structural change.* Glutamate uncaging onto a single spine paired with depolarization enlarges that spine within a minute, and the enlargement persists for hours in proportion to the increase of the AMPA current (Matsuzaki and colleagues, 2004); actin polymerization and new PSD material follow.

Presynaptic expression, an increase of release probability, occurs at other synapses (the mossy fiber synapse onto CA3, where LTP is NMDA receptor–independent and mediated by cAMP and PKA) and contributes under some conditions at CA1; the binomial analysis of [7.16.9](/7.16.9) (Question 1 there) was the tool of this long debate.

### 14.2.3. Early and Late Phases

LTP has phases distinguished by their molecular requirements. *Early LTP* lasts one to three hours and requires only the activation of kinases (CaMKII, PKC, PKA) and the modification and trafficking of existing proteins. *Late LTP*, induced by repeated tetani spaced by minutes, lasts many hours in slices (days in vivo) and requires transcription and translation: blockers of protein synthesis applied during induction leave early LTP intact but abolish the late phase. The signaling pathway to the nucleus involves PKA, the MAP kinase ERK and the transcription factor CREB, and is shared with the long-term facilitation of *Aplysia* sensory synapses ([7.16.38](/7.16.38)). The same distinction separates short-term from long-term memory in behavior, which also depends on protein synthesis during or soon after learning. How proteins made in the soma reach only the potentiated synapses among thousands is the problem of 14.7.

## 14.3. CaMKII: A Molecular Memory?

**Definition 14.3.1 (CaMKII)** **CaMKII** ($\ce{Ca^2+}$/calmodulin-dependent protein kinase II) is a serine/threonine kinase assembled from twelve subunits in two stacked hexameric rings, which is activated by binding of $\ce{Ca^2+}$/**calmodulin**; when two neighboring subunits are active, one phosphorylates the other at Thr286 (in the $\alpha$ isoform), which makes the phosphorylated subunit active even after $\ce{Ca^2+}$ has returned to rest (autonomous activity).

CaMKII is among the most abundant proteins of the PSD (about $2\%$ of forebrain protein), it is necessary for LTP (mice with the point mutation T286A, which prevents autophosphorylation, lack LTP at CA1 synapses and are impaired in spatial learning; Giese and colleagues, 1998), and an activated, constitutively active form is sufficient to potentiate synapses. Its autophosphorylation suggested to Lisman (1985) a solution to a puzzle raised by Crick (1984): how can a memory outlast the molecules that store it? A holoenzyme with many subunits can be bistable. Once enough subunits are phosphorylated, each newly dephosphorylated subunit is rephosphorylated by an active neighbor faster than the phosphatase acts, and new subunits that exchange into the holoenzyme are phosphorylated in turn, so that the state outlives each subunit.

**Formula 14.3.1 (A Minimal CaMKII Switch)** Let $f$ be the fraction of phosphorylated subunits, $c$ the $\ce{Ca^2+}$ concentration and $h(c) = c^4/(c^4 + K^4)$ the activation by $\ce{Ca^2+}$/calmodulin. Then
$$
\frac{\mathrm{d}f}{\mathrm{d}t} = (1 - f)\left[k_{\mathrm{c}}h(c) + k_{\mathrm{a}}f^2\right] - \frac{v_{\mathrm{P}}f}{K_{\mathrm{M}} + f}, \tag{14.1}
$$
where $k_{\mathrm{c}}$ is the $\ce{Ca^2+}$-driven and $k_{\mathrm{a}}f^2$ the cooperative autophosphorylation rate, and the phosphatase PP1 acts with saturable kinetics (maximal rate $v_{\mathrm{P}}$, constant $K_{\mathrm{M}}$).

At resting $\ce{Ca^2+}$, $f = 0$ is always a stable fixed point, and when the phosphatase is weak enough two more fixed points appear in a **saddle-node bifurcation**, a stable "on" state near $f \approx 0.9$ and an unstable threshold between (figure below). A $\ce{Ca^2+}$ pulse that pushes $f$ beyond the threshold switches the synapse on, and it stays on after $\ce{Ca^2+}$ has returned to rest: **bistability** with **hysteresis**, the same structure as the genetic toggle switch of [7.6.33](/7.6.33#sec-33.2.2). The model shows why the duration of the $\ce{Ca^2+}$ signal matters as much as its amplitude, and how a transient surge of phosphatase activity, the signal of LTD (14.4), can switch the synapse off.

![A minimal bistable model of CaMKII autophosphorylation (Formula 14.3.1; $k_{\mathrm{c}} = k_{\mathrm{a}} = 0.5\,\mathrm{s^{-1}}$, $K = 1\,\mu\mathrm{M}$, $K_{\mathrm{M}} = 0.1$, resting $\ce{Ca^2+}$ $0.1\,\mu\mathrm{M}$). A: phosphorylation rate by autophosphorylation (solid) and dephosphorylation rate for three phosphatase activities (dashed); fixed points are their intersections. B: steady states against phosphatase activity $v_{\mathrm{P}}$ (solid: stable, dashed: unstable): for $v_{\mathrm{P}} < 0.085\,\mathrm{s^{-1}}$ the "off" and "on" states coexist. C: time course at $v_{\mathrm{P}} = 0.04\,\mathrm{s^{-1}}$: a $0.3\,\mathrm{s}$ $\ce{Ca^2+}$ pulse of $3\,\mu\mathrm{M}$ fails, a $1\,\mathrm{s}$ pulse switches the kinase on permanently, a $25\,\mathrm{s}$ increase of phosphatase activity (red) resets it, and a $2\,\mathrm{s}$ pulse switches it on again.](./plots/camkii-bistability.py)

Whether the brain uses this switch for maintenance is unresolved. Imaging of CaMKII activity with FRET sensors in single spines showed that its activation after LTP induction lasts only about a minute (Lee and colleagues, 2009), and inhibiting the kinase hours after induction does not reverse LTP in most studies. Current proposals assign the persistent role to a structural complex of CaMKII with the GluN2B subunit of the NMDA receptor, to the atypical protein kinase PKMζ (whose role is supported by inhibitor studies but questioned by knockout mice that retain LTP), or to the persistent enlargement of the spine and its PSD. CaMKII's role in induction is established; its role as the memory itself remains a hypothesis.

## 14.4. Long-Term Depression and the Calcium Control Hypothesis

### 14.4.1. LTD

At the same CA1 synapses, low-frequency stimulation, for example 900 pulses at $1\,\mathrm{Hz}$, produces a lasting depression that also requires NMDA receptors and postsynaptic $\ce{Ca^2+}$ (Dudek and Bear, 1992), and it can reverse previously induced LTP (depotentiation). Its expression mirrors that of LTP: dephosphorylation of GluA1 at Ser845 and clathrin-dependent endocytosis of AMPA receptors. Its signaling uses phosphatases: calcineurin (PP2B), activated by $\ce{Ca^2+}$/calmodulin with high affinity, dephosphorylates inhibitor-1 and thereby releases protein phosphatase 1. Other forms of LTD use metabotropic glutamate receptors and local protein synthesis (in hippocampus and cerebellum, where LTD of parallel fiber synapses onto Purkinje cells is the basis of motor learning in the Marr–Albus–Ito theory, [7.16.33](/7.16.33)), or **endocannabinoids** acting presynaptically ([7.16.11](/7.16.11#sec-11.6)).

### 14.4.2. Calcium Levels Decide the Sign

The finding that both LTP and LTD require NMDA receptors and postsynaptic $\ce{Ca^2+}$ led to the idea that the amount and time course of $\ce{Ca^2+}$, not its source, determine the sign (Lisman, 1989; Artola, Bröcher and Singer, 1990).

**Definition 14.4.1 (Calcium Control Hypothesis)** The **calcium control hypothesis** states that the direction of long-term plasticity at a synapse is set by the postsynaptic $\ce{Ca^2+}$ concentration in its spine: below a threshold $\theta_{\mathrm{d}}$ there is no change, between $\theta_{\mathrm{d}}$ and a higher threshold $\theta_{\mathrm{p}}$ the synapse is depressed, and above $\theta_{\mathrm{p}}$ it is potentiated.

The molecular rationale is the different affinity of the two enzyme systems for $\ce{Ca^2+}$/calmodulin: calcineurin is activated at lower $\ce{Ca^2+}$ than CaMKII, so modest, prolonged signals favor dephosphorylation and large, brief signals favor phosphorylation.

**Formula 14.4.1 (Calcium-Dependent Plasticity Model)** In the model of Shouval, Bear and Cooper (2002) the weight relaxes toward a $\ce{Ca^2+}$-dependent target,
$$
\tau_w\frac{\mathrm{d}w}{\mathrm{d}t} = \Omega(c) - w, \tag{14.2}
$$
where $\Omega(c)$ equals the resting weight for $c < \theta_{\mathrm{d}}$, falls to a minimum between $\theta_{\mathrm{d}}$ and $\theta_{\mathrm{p}}$ and rises to a maximum above $\theta_{\mathrm{p}}$; the spine $\ce{Ca^2+}$ $c(t)$ is computed from NMDA receptor currents (with Eq. (10.2)) and $\ce{Ca^2+}$ removal.

With a single function $\Omega$, Eq. (14.2) reproduces the frequency dependence of plasticity: low-frequency trains keep $c$ in the depression window, high-frequency trains summate $\ce{Ca^2+}$ above $\theta_{\mathrm{p}}$ (figure below). It also predicts the dependence on spike timing (14.5), since a bAP that arrives just after glutamate relieves the magnesium block at the moment the NMDA receptors are bound. The same structure, depression for weak and potentiation for strong postsynaptic activation with a crossover, is the **BCM rule** of rate-based learning ([Definition 22.3.2](/7.16.22#def-22.3.2)).

![The calcium control hypothesis (Formula 14.4.1). A: target weight $\Omega$ against spine $\ce{Ca^2+}$, with the thresholds $\theta_{\mathrm{d}} = 0.35\,\mu\mathrm{M}$ and $\theta_{\mathrm{p}} = 0.55\,\mu\mathrm{M}$; the resting weight is $0.5$. B: spine $\ce{Ca^2+}$ during trains at $1$, $10$ and $50\,\mathrm{Hz}$, each pulse adding $0.45\,\mu\mathrm{M}$ that decays with $50\,\mathrm{ms}$ (dashed lines: thresholds): at $1\,\mathrm{Hz}$ the $\ce{Ca^2+}$ spends little time above $\theta_{\mathrm{d}}$, at $10\,\mathrm{Hz}$ it remains in the depression window, at $50\,\mathrm{Hz}$ it summates above $\theta_{\mathrm{p}}$. C: weight change after 900 pulses ($\tau_w = 40\,\mathrm{s}$) against frequency for two $\ce{Ca^2+}$ amplitudes per pulse: depression at low and intermediate, potentiation at high frequencies; a larger $\ce{Ca^2+}$ influx per pulse moves the crossover to lower frequencies. The decline at $100\,\mathrm{Hz}$ is an artifact of the fixed number of pulses, which then last only $9\,\mathrm{s}$.](./plots/calcium-control.py)

### 14.4.3. Metaplasticity

The thresholds are not fixed. Prior activity, too weak to change synaptic strength itself, changes how a synapse responds to later activity.

**Definition 14.4.2 (Metaplasticity)** **Metaplasticity** is an activity-dependent change in the ability of synapses to undergo subsequent plasticity, such as a shift of the threshold between LTD and LTP, without a change of the current synaptic strength ("the plasticity of synaptic plasticity", Abraham and Bear, 1996).

The clearest example is the visual cortex: after dark rearing, the stimulation frequency at which LTD turns into LTP is lowered, and a few hours of light exposure raise it again (Kirkwood, Rioult and Bear, 1996). One mechanism is a change of NMDA receptor subunits: dark rearing increases the proportion of slowly deactivating GluN2B-containing receptors, which pass more $\ce{Ca^2+}$ per input, the effect of the larger amplitude in panel C of the figure above (Philpot and colleagues, 2001). Metaplasticity of this kind implements the sliding threshold of the **BCM rule**, which makes Hebbian learning stable and competitive ([7.16.22](/7.16.22#sec-22.3)).

## 14.5. Spike-Timing-Dependent Plasticity

### 14.5.1. The Timing Window

Hebb's postulate speaks of cell A "taking part in firing" cell B, which implies causality: A fires before B. Paired recordings showed that synapses read this order.

**Definition 14.5.1 (Spike-Timing-Dependent Plasticity)** **Spike-timing-dependent plasticity** (STDP) is long-term plasticity whose sign and magnitude depend on the interval $\Delta t = t_{\mathrm{post}} - t_{\mathrm{pre}}$ between presynaptic and postsynaptic spikes: repeated pairings with the presynaptic spike a few to some tens of milliseconds before the postsynaptic spike ($\Delta t > 0$) potentiate the synapse, the reverse order ($\Delta t < 0$) depresses it. In the pair-based description each pairing changes the weight by
$$
\Delta w = \begin{cases} A_+\,\mathrm{e}^{-\Delta t/\tau_+}, & \Delta t > 0,\\ -A_-\,\mathrm{e}^{\Delta t/\tau_-}, & \Delta t < 0.\end{cases} \tag{14.3}
$$

Markram, Lübke, Frotscher and Sakmann (1997) found this asymmetry between layer 5 pyramidal cells, Bi and Poo (1998) mapped the window in hippocampal cultures (fits give $\tau_+ \approx 17\,\mathrm{ms}$ and $\tau_- \approx 34\,\mathrm{ms}$), and Zhang and colleagues (1998) confirmed it in vivo in the *Xenopus* tectum. The mechanism at many synapses is the one of 14.4: when the presynaptic spike precedes, glutamate is bound to **NMDA receptors** when the **bAP** arrives and relieves the **magnesium block**, producing a large $\ce{Ca^2+}$ signal; when the bAP precedes, the receptors are not yet bound while the cell is depolarized and the $\ce{Ca^2+}$ signal is moderate. At neocortical synapses the depression component additionally involves presynaptic NMDA receptors, metabotropic glutamate receptors and endocannabinoids (Sjöström, Turrigiano and Nelson, 2003). Windows vary: some synapses have symmetric windows, and in the cerebellum-like electrosensory lobe of mormyrid fish the window is inverted (anti-Hebbian), which allows the circuit to cancel the predictable sensory consequences of the fish's own electric discharge (Bell and colleagues, 1997).

### 14.5.2. Implementation and Limits

Eq. (14.3) is implemented with local traces, as in network simulations, so that no list of past spike times is needed.

**Formula 14.5.1 (Trace Implementation of STDP)** Each synapse keeps a presynaptic trace $x$ and the neuron a postsynaptic trace $y$,
$$
\frac{\mathrm{d}x}{\mathrm{d}t} = -\frac{x}{\tau_+} + \sum_k\delta(t - t^{\mathrm{pre}}_k), \qquad \frac{\mathrm{d}y}{\mathrm{d}t} = -\frac{y}{\tau_-} + \sum_k\delta(t - t^{\mathrm{post}}_k);
$$
at each postsynaptic spike $w \leftarrow w + A_+x$, at each presynaptic spike $w \leftarrow w - A_-y$.

For isolated pairs this reproduces Eq. (14.3) exactly, and for spike trains it sums the window over all pairs. The traces are not only a computational device: $x$ resembles the bound fraction of NMDA receptors and $y$ the depolarization by the bAP. Averaging the pair rule over Poisson spike trains gives a rate-based Hebbian rule whose stability depends on the net area $A_+\tau_+ - A_-\tau_-$ of the window ([7.16.22](/7.16.22#sec-22.4)).

The pair rule is a first approximation. At pairing frequencies above about $20\,\mathrm{Hz}$ both orders potentiate, and with few spikes the rule depends on triplets of spikes rather than pairs (Sjöström, Turrigiano and Nelson, 2001); triplet rules (Pfister and Gerstner, 2006) and voltage-based rules (Clopath and colleagues, 2010) fit these data with a few more parameters and approach the BCM rule at the level of rates. Timing also depends on dendritic location: distal synapses, which the bAP reaches attenuated, may need **dendritic spikes** as the postsynaptic signal ([7.16.13](/7.16.13#sec-13.6)).

![Spike-timing-dependent plasticity (Definition 14.5.1; $\tau_+ = 16.8\,\mathrm{ms}$, $\tau_- = 33.7\,\mathrm{ms}$, $A_+ = 1$, $A_- = 0.55$, so that $A_-\tau_- > A_+\tau_+$ and the window has a slightly negative net area). A: the window (line) and the weight changes computed for isolated pairings with the trace implementation (dots, Formula 14.5.1). B: one pair with the presynaptic spike at $20\,\mathrm{ms}$ and the postsynaptic spike at $30\,\mathrm{ms}$: the presynaptic trace $x$ is read out at the postsynaptic spike and the weight increases by $\mathrm{e}^{-10/16.8} = 0.55$. C: the reverse order: the postsynaptic trace $y$ is read at the presynaptic spike and the weight decreases by $0.55\,\mathrm{e}^{-10/33.7} = 0.41$.](./plots/stdp.py)

## 14.6. Homeostatic Plasticity

Hebbian plasticity is a positive feedback: potentiated synapses drive the neuron more strongly, which favors further potentiation. Without a counteracting force, activity would run away or fall silent ([7.16.22](/7.16.22#sec-22.1)). Turrigiano and colleagues (1998) found such a force in cortical cultures. Blocking activity with tetrodotoxin for two days increased the amplitude of miniature EPSCs, and increasing activity by blocking inhibition with bicuculline decreased it; in both cases the whole distribution of amplitudes was multiplied by a constant factor.

**Definition 14.6.1 (Homeostatic Plasticity and Synaptic Scaling)** **Homeostatic plasticity** is a change of synaptic strength or intrinsic excitability that counteracts a sustained change of a neuron's activity and returns it toward a set point. **Synaptic scaling** is the form in which all excitatory synapses of a neuron are multiplied by a common factor, upward when activity is too low and downward when it is too high.

A simple model of scaling is
$$
\tau_{\mathrm{H}}\frac{\mathrm{d}w_i}{\mathrm{d}t} = w_i\left(1 - \frac{\bar r}{r_{\mathrm{target}}}\right), \tag{14.4}
$$
where $\bar r$ is the **firing rate** of the neuron averaged over hours and $r_{\mathrm{target}}$ its set point. Because the change is proportional to $w_i$, the ratios $w_i/w_j$, which carry the information stored by Hebbian plasticity, are preserved while the total drive is normalized. Scaling is slow (hours to days, $\tau_{\mathrm{H}}$ much longer than Hebbian time scales) and is mediated by changes of AMPA receptor number, signaled by $\ce{Ca^2+}$ through CaMK kinases, by the immediate-early gene product Arc, by retinoic acid and by TNF-α released from glia (Stellwagen and Malenka, 2006). In vivo, firing rates of visual cortical neurons in rats recover over a few days after monocular deprivation, by scaling and by changes of intrinsic excitability (Hengen and colleagues, 2013). A theoretical difficulty is that homeostasis as slow as measured is too slow to stabilize fast Hebbian learning in models; faster compensatory mechanisms such as heterosynaptic plasticity and inhibitory plasticity have been proposed to fill the gap (Zenke, Gerstner and Ganguli, 2017).

## 14.7. Synaptic Tagging and Capture

Late LTP requires new proteins, which are synthesized largely in the soma or in dendritic shafts, yet it remains input specific. Frey and Morris (1997) resolved the paradox with two independent pathways onto the same population of CA1 cells. A strong tetanus to pathway 1 induced late LTP; a weak tetanus to pathway 2 alone induced only early LTP, which decayed within three hours. If the weak tetanus was given up to about one to two hours after the strong one, pathway 2 also showed late LTP, even when protein synthesis was blocked during its own tetanus.

**Definition 14.7.1 (Synaptic Tagging and Capture)** **Synaptic tagging and capture** is the mechanism by which induction of plasticity at a synapse sets a local, protein synthesis–independent, transient "tag" (lasting about one to two hours), while sufficiently strong stimulation anywhere on the neuron triggers the synthesis of plasticity-related proteins that are distributed through the cell but are captured, and stabilize plasticity, only at tagged synapses.

The tag explains input specificity without requiring that proteins be delivered only to the right synapse: specificity lies in the tag, persistence in the proteins. Candidate tags include activated CaMKII and structural changes of the spine; candidate plasticity-related proteins include Arc, Homer1a and AMPA receptor subunits, in part translated locally from dendritic mRNAs. At the level of behavior, *behavioral tagging* has the same logic: a weak learning experience that would be forgotten in a day is retained if it is followed or preceded within an hour by a novel experience that triggers protein synthesis in the hippocampus, an effect that depends on dopamine (Moncada and Viola, 2007; Wang, Redondo and Morris, 2010). Tagging and capture thus provide a mechanism by which the importance of an event, signaled by neuromodulators, decides which of the memories formed around it are kept.

## 14.8. Behavioral Timescale Synaptic Plasticity

The rules above require pre- and postsynaptic activity within tens of milliseconds. Bittner and colleagues (2015, 2017), recording intracellularly from CA1 pyramidal cells of mice running on a treadmill, found a rule with a window of seconds. A single dendritic plateau potential, a $\ce{Ca^2+}$-mediated depolarization of a few hundred milliseconds generated in the apical tuft when entorhinal input coincides with CA3 input ([7.16.13](/7.16.13#sec-13.6.2)), occurring spontaneously or induced by current injection at a location, created a place field at that location within one lap. The field was shifted backward: its peak preceded the location of the plateau, because synapses active up to about three seconds before the plateau, and about one second after it, were potentiated.

**Definition 14.8.1 (Behavioral Timescale Synaptic Plasticity)** **Behavioral timescale synaptic plasticity** (BTSP) is long-term plasticity induced in one trial by a dendritic plateau potential, which potentiates (or, for already strong synapses, depresses) the synapses whose presynaptic inputs were active within a window of several seconds before or after the plateau, independently of postsynaptic spikes.

A window of seconds cannot be implemented by NMDA receptors alone. Models postulate two slow signals: a synaptic eligibility trace set by presynaptic activity and a cell-wide instructive signal set by the plateau, with plasticity proportional to their overlap.

**Formula 14.8.1 (Two-Trace Model of BTSP)** Let $E_i(t)$ be the eligibility trace of synapse $i$, a low-pass filtered version of its presynaptic activity with time constant $\tau_E$ (about $1$–$2\,\mathrm{s}$), and $S(t)$ the instructive signal, the plateau filtered with time constant $\tau_S$ (below $1\,\mathrm{s}$). The weight change in one trial is
$$
\Delta w_i = \eta\,(w_{\max} - w_i)\int E_i(t)\,S(t)\,\mathrm{d}t. \tag{14.5}
$$
Because the presynaptic trace is longer than the instructive one, inputs active before the plateau overlap with it more than inputs active after it, and the learned kernel is asymmetric.

BTSP inverts the logic of Hebbian plasticity: the postsynaptic signal is not the cell's output but an instructive event, triggered largely by input from the entorhinal cortex, which can carry information about goals and reward. In mice learning a reward location, plateau potentials and new place fields concentrate near the reward, so that the representation of the environment is reshaped in a few trials (Grienberger and Magee, 2022). Whether BTSP strengthens existing synapses or recruits silent ones, and how the instructive input is computed, are open questions. BTSP is an example of a three-factor rule, the subject of the next section.

![Behavioral timescale synaptic plasticity (Formula 14.8.1). A CA1 neuron receives 200 inputs, each active at a preferred time of an $8\,\mathrm{s}$ lap (Gaussian, $\sigma = 0.25\,\mathrm{s}$; at constant running speed time and position are equivalent); eligibility traces decay with $\tau_E = 1.5\,\mathrm{s}$, a plateau of $0.4\,\mathrm{s}$ starts at $5\,\mathrm{s}$ and its instructive trace decays with $\tau_S = 0.8\,\mathrm{s}$; initial weights $0.1$. A: activity of one input with preferred time $3.5\,\mathrm{s}$, its eligibility trace, the instructive signal and their overlap (yellow), which drives potentiation although the input was active $1.5\,\mathrm{s}$ before the plateau. B: the learned weights against preferred time after the single plateau: the kernel extends over seconds and is wider before the plateau (dashed: its center). C: the summed input in the lap before and after the plateau: a place field appears in one trial, peaking slightly before the plateau.](./plots/btsp.py)

## 14.9. Third Factors: Neuromodulators and Eligibility Traces

Hebbian rules are unsupervised: they strengthen correlations whether or not they are useful. Learning from consequences requires that a signal about the outcome, arriving later, determine which of the recently active synapses change. **Neuromodulators** such as **dopamine**, **norepinephrine**, **serotonin** and **acetylcholine** ([7.16.11](/7.16.11#sec-11.4)) can serve as such signals.

**Definition 14.9.1 (Three-Factor Learning Rule and Eligibility Trace)** A **three-factor learning rule** is a plasticity rule in which coincident pre- and postsynaptic activity does not change the weight directly but sets a synapse-specific, decaying **eligibility trace** $e_{ij}$, and the weight changes in proportion to the product of the trace and a third, typically neuromodulatory, signal $M(t)$:
$$
\frac{\mathrm{d}e_{ij}}{\mathrm{d}t} = -\frac{e_{ij}}{\tau_e} + H\bigl(\mathrm{pre}_j, \mathrm{post}_i\bigr), \qquad \frac{\mathrm{d}w_{ij}}{\mathrm{d}t} = \eta\,M(t)\,e_{ij}, \tag{14.6}
$$
where $H$ is a Hebbian term (for example the STDP window of Eq. (14.3)).

Experiments have measured eligibility traces directly. In striatal spiny projection neurons, glutamate uncaging paired with postsynaptic spikes enlarged spines only if dopamine was released (optogenetically) between about $0.3$ and $2\,\mathrm{s}$ afterward (Yagishita and colleagues, 2014). In visual cortex, STDP pairings leave traces for LTP and LTD that are converted into lasting changes by norepinephrine (through $\beta$-adrenergic receptors) and serotonin (through 5-HT$_{2\mathrm{C}}$ receptors), respectively, applied within about $5$–$10\,\mathrm{s}$ (He and colleagues, 2015). In hippocampus, dopamine applied minutes after a post-before-pre pairing converts the expected LTD into LTP (Brzosko, Schultz and Paulsen, 2015). If $M(t)$ reports a reward prediction error, as the firing of dopamine neurons does, Eq. (14.6) implements a form of reinforcement learning at the synapse (Izhikevich, 2007; [7.16.39](/7.16.39)); if $M$ reports a target signal, it implements supervised learning, as climbing fibers do for cerebellar Purkinje cells ([7.16.33](/7.16.33)) and plateau potentials for BTSP. The general problem these rules address, assigning credit to synapses for an outcome that occurs later and elsewhere, returns in [7.16.50](/7.16.50).

## Summary

- The synaptic hypothesis of memory predicts detectability, anterograde and retrograde alteration and mimicry; each has been tested at hippocampal and amygdalar synapses (14.1). **Hebb's rule** requires local, conjunctive and specific change.
- LTP at the CA3–CA1 synapse is input specific, cooperative and associative (Definition 14.2.1) because the NMDA receptor detects the coincidence of glutamate release and postsynaptic depolarization; it is expressed by insertion and phosphorylation of AMPA receptors and spine growth, and has a protein synthesis–dependent late phase.
- CaMKII (Definition 14.3.1) is required for induction; its autophosphorylation can make a bistable switch (Formula 14.3.1), although its role in maintenance is debated.
- The amount and time course of spine $\ce{Ca^2+}$ decide between LTD and LTP (Definition 14.4.1, Formula 14.4.1); prior activity shifts the thresholds (metaplasticity, Definition 14.4.2).

| Rule | Signal | Window | Section |
|---|---|---|---|
| Rate-dependent LTP/LTD | Spine $\ce{Ca^2+}$ level | Seconds of stimulation | 14.4 |
| STDP | Order of pre and post spikes | $\pm 10$–$50\,\mathrm{ms}$ | 14.5 |
| Synaptic scaling | Average rate of the neuron | Hours to days | 14.6 |
| Tagging and capture | Local tag, cell-wide proteins | $1$–$2\,\mathrm{h}$ | 14.7 |
| BTSP | Dendritic plateau | Several seconds | 14.8 |
| Three-factor rules | Neuromodulator times eligibility trace | $0.3\,\mathrm{s}$ to minutes | 14.9 |

- STDP (Definition 14.5.1) potentiates for pre-before-post and depresses for post-before-pre pairings; it is implemented with traces (Formula 14.5.1) and extended by triplet and voltage rules.
- Synaptic scaling (Definition 14.6.1) multiplies all weights to keep activity near a set point while preserving their ratios (Eq. (14.4)).
- Synaptic tagging and capture (Definition 14.7.1) reconciles input specificity with cell-wide protein synthesis; BTSP (Definition 14.8.1) and three-factor rules (Definition 14.9.1) bridge the gap between millisecond coincidence and behavioral time scales.

## Questions

1. Explain how the NMDA receptor accounts for the associativity of LTP. Predict what happens to associativity if the weak and strong inputs are separated by $200\,\mathrm{ms}$, and if the strong input is replaced by a train of postsynaptic action potentials that back-propagate weakly into the dendrites where the weak synapses lie.

   **Answer** The weak input releases glutamate that binds NMDA receptors at its own synapses, but its depolarization is too small to relieve the magnesium block; the strong input, active at the same time on the same cell, supplies the depolarization, so $\ce{Ca^2+}$ enters only at the weak synapses that are bound (input specificity) and at the strong ones. With a $200\,\mathrm{ms}$ separation, glutamate has largely unbound from NMDA receptors by the time the depolarization arrives (deactivation in about $50$–$150\,\mathrm{ms}$), and the $\ce{Ca^2+}$ signal is small: associativity requires overlap within roughly $100\,\mathrm{ms}$. If the depolarization is supplied by back-propagating spikes that are strongly attenuated at distal synapses, the relief of the block there is weak and associativity fails at distal synapses, unless the bAP is boosted (for example by local depolarization inactivating A-type channels) or dendritic spikes supply the depolarization.

2. In Formula 14.3.1 with $c$ at rest ($h \approx 0$), show that $f = 0$ is always a fixed point and derive the condition for other fixed points. What does the saturation of the phosphatase ($K_{\mathrm{M}}$ small) contribute?

   **Answer** At $h = 0$, $\dot f = k_{\mathrm{a}}f^2(1 - f) - v_{\mathrm{P}}f/(K_{\mathrm{M}} + f)$, which vanishes at $f = 0$. Other fixed points satisfy $k_{\mathrm{a}}f(1 - f)(K_{\mathrm{M}} + f) = v_{\mathrm{P}}$: the left side is zero at $f = 0$ and $f = 1$ and positive between, so two solutions exist when $v_{\mathrm{P}}$ is below its maximum (a saddle-node bifurcation at the maximum, about $0.085\,\mathrm{s^{-1}}$ for $k_{\mathrm{a}} = 0.5\,\mathrm{s^{-1}}$ and $K_{\mathrm{M}} = 0.1$); the larger is stable and the smaller is the threshold. Near $f = 0$ the linearization is $\dot f \approx -(v_{\mathrm{P}}/K_{\mathrm{M}})f$, so the "off" state is stable. If the phosphatase were linear ($K_{\mathrm{M}} \to \infty$ with $v_{\mathrm{P}}/K_{\mathrm{M}} = k$ fixed), the condition would be $k_{\mathrm{a}}f(1 - f) = k$, which still has two solutions for $k < k_{\mathrm{a}}/4$, so saturation is not strictly necessary in this model; but saturation makes the dephosphorylation rate nearly constant at high $f$, so that autophosphorylation, which grows as $f^2$, can outrun it: saturation widens the range of bistability and makes the "on" state robust to phosphatase fluctuations.

3. With the STDP window of Definition 14.5.1 ($A_+ = 1$, $\tau_+ = 17\,\mathrm{ms}$, $A_- = 0.55$, $\tau_- = 34\,\mathrm{ms}$), compute the expected weight drift per second for uncorrelated pre- and postsynaptic Poisson trains with rates $r_{\mathrm{pre}} = r_{\mathrm{post}} = 10\,\mathrm{Hz}$, counting all pairs. What does the sign imply?

   **Answer** For independent Poisson trains the expected number of pairs per second with $\Delta t \in [s, s + \mathrm{d}s]$ is $r_{\mathrm{pre}}r_{\mathrm{post}}\,\mathrm{d}s$, so the drift is $r_{\mathrm{pre}}r_{\mathrm{post}}\int W(s)\,\mathrm{d}s = 100\,\mathrm{s^{-2}}\cdot(A_+\tau_+ - A_-\tau_-) = 100\cdot(0.017 - 0.0187)\,\mathrm{s} = -0.17\,\mathrm{s^{-1}}$ (in units of $A_+$). The net area is negative: uncorrelated inputs are depressed, while inputs whose spikes tend to precede the postsynaptic spikes (causal inputs) gain from the positive lobe. This makes STDP competitive and selects inputs that predict the output ([7.16.22](/7.16.22#sec-22.4)).

4. Synaptic scaling multiplies all weights by a common factor, whereas the BCM rule shifts the threshold between LTD and LTP. Which preserves the relative strengths of the synapses, and why might a neuron need both?

   **Answer** Scaling (Eq. (14.4)) changes every $w_i$ by the same factor, so ratios $w_i/w_j$ are preserved exactly; it normalizes total drive without erasing the pattern learned by Hebbian plasticity, but it does not itself create selectivity. The sliding threshold of the BCM rule (metaplasticity) changes how future activity is converted into plasticity: when the neuron is very active, LTD becomes more likely and LTP less likely, which introduces competition between inputs and makes the neuron selective, but it acts only on synapses that are active and changes their ratios. A neuron needs a fast mechanism that stabilizes ongoing Hebbian learning and competition (sliding thresholds, heterosynaptic plasticity) and a slow one that keeps its average rate in a functional range over days despite changes of inputs, development or injury (scaling and intrinsic plasticity).
