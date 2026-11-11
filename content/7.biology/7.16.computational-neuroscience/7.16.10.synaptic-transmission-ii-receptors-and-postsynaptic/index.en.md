---
title: "Synaptic Transmission II: Receptors and Postsynaptic Responses"
description: "Criteria for a neurotransmitter; the nicotinic receptor at the end plate, reversal potentials and linear current–voltage relations; AMPA and NMDA receptors, Mg²⁺ block (Jahr–Stevens), Ca²⁺ permeability and coincidence detection; the postsynaptic density; GABA_A and glycine receptors, the Cl⁻ reversal potential, KCC2/NKCC1 and depolarizing GABA, the arithmetic of shunting inhibition; electrical synapses and the coupling coefficient; kinetic schemes, deactivation and desensitization."
---

The presynaptic terminal decides how much transmitter is released ([7.16.9](/7.16.9)); the postsynaptic cell decides what the transmitter means. The same glutamate molecule excites through one receptor and inhibits through another, the same GABA molecule hyperpolarizes an adult neuron and depolarizes an embryonic one, and the NMDA receptor turns the coincidence of presynaptic release and postsynaptic depolarization into a $\ce{Ca^2+}$ signal that underlies **long-term potentiation** ([7.16.14](/7.16.14)). This chapter treats the ionotropic receptors quantitatively: what sets the sign and size of a postsynaptic current, how the current depends on voltage, and how fast receptors open, close and desensitize. The basic distinction between **ionotropic receptors** and **metabotropic receptors**, and the table of transmitter classes, are in [7.14.5](/7.14.5#sec-5.4.3); the biophysics of ligand-gated channels and the molecular basis of $\ce{Mg^2+}$ block are in [7.6.30](/7.6.30#sec-30.3.4). Metabotropic signaling follows in [7.16.11](/7.16.11), and the reduced synaptic models used in network simulations in [7.16.12](/7.16.12).

## 10.1. Neurotransmitters

Loewi's experiment of 1921 established chemical transmission: perfusate from a frog heart whose vagus nerve had been stimulated slowed a second heart, so the nerve acted by releasing a substance ("Vagusstoff", later identified as acetylcholine). Since then about a hundred substances have been shown to act as transmitters. A substance is accepted as a **neurotransmitter** of a given synapse when it satisfies four criteria:

1. it is synthesized in the presynaptic neuron and present in its terminals (with the synthetic enzymes and the vesicular transporter);
2. it is released in a $\ce{Ca^2+}$-dependent manner when the neuron is stimulated, in amounts sufficient to act;
3. applied exogenously at that concentration it mimics the effect of nerve stimulation, including the same reversal potential and the same pharmacology (agonists mimic, antagonists block both);
4. there is a mechanism that terminates its action (an enzyme or a transporter).

The third criterion is the strongest test, because it identifies the receptors as well as the substance. Small-molecule transmitters (acetylcholine, the amino acids glutamate, GABA and glycine, the monoamines, ATP) are packed into small clear vesicles at the **active zone** and act on fast ionotropic as well as slow metabotropic receptors; **neuropeptides** are released from large dense-core vesicles, usually during high-frequency firing, and act on metabotropic receptors only ([7.16.11](/7.16.11)). In the vertebrate central nervous system the division of labor is stark: glutamate mediates almost all fast excitation, GABA (in the brain) and glycine (in the spinal cord and brainstem) almost all fast inhibition, and the monoamines and acetylcholine act mostly as modulators.

| Receptor | Transmitter | Subunits | Permeability | Reversal potential | Notes |
|---|---|---|---|---|---|
| Nicotinic ACh (muscle) | Acetylcholine | Pentamer $\alpha_2\beta\delta\varepsilon$ | $\ce{Na+}$, $\ce{K+}$ (some $\ce{Ca^2+}$) | $\approx 0\,\mathrm{mV}$ | End plate; Cys-loop family |
| AMPA | Glutamate | Tetramer GluA1–4 | $\ce{Na+}$, $\ce{K+}$; $\ce{Ca^2+}$ if GluA2 absent | $\approx 0\,\mathrm{mV}$ | Fast EPSC |
| NMDA | Glutamate + glycine (or D-serine) | Tetramer GluN1 + GluN2A–D | $\ce{Na+}$, $\ce{K+}$, $\ce{Ca^2+}$ | $\approx 0\,\mathrm{mV}$ | $\ce{Mg^2+}$ block; slow |
| Kainate | Glutamate | GluK1–5 | $\ce{Na+}$, $\ce{K+}$ | $\approx 0\,\mathrm{mV}$ | Pre- and postsynaptic |
| $\mathrm{GABA_A}$ | GABA | Pentamer, typically $2\alpha2\beta\gamma$ | $\ce{Cl-}$, $\ce{HCO3-}$ | $E_{\mathrm{Cl}}$, about $-70\,\mathrm{mV}$ in adults | Benzodiazepine site at $\alpha$/$\gamma$ |
| Glycine | Glycine | Pentamer $\alpha$, $\beta$ | $\ce{Cl-}$ | $E_{\mathrm{Cl}}$ | Blocked by strychnine |
| $\mathrm{5\text{-}HT_3}$ | Serotonin | Pentamer | Cations | $\approx 0\,\mathrm{mV}$ | The only ionotropic monoamine receptor |
| P2X | ATP | Trimer | Cations, $\ce{Ca^2+}$ | $\approx 0\,\mathrm{mV}$ | |

## 10.2. The Neuromuscular Junction: Reversal Potential and Driving Force

The end plate is where the rules of postsynaptic currents were worked out ([7.14.8](/7.14.8#sec-8.4.1)). Its receptor, the muscle **nicotinic acetylcholine receptor**, is a pentameric channel whose pore is lined by the M2 helices of the five subunits; rings of negative charge at the pore mouths make it cation-selective, but it hardly distinguishes $\ce{Na+}$ from $\ce{K+}$. Takeuchi and Takeuchi (1960) voltage-clamped the end plate and measured the end-plate current at different holding potentials: the current was inward at rest, decreased linearly with depolarization, vanished near $-15$ to $0\,\mathrm{mV}$ and reversed beyond.

**Definition 10.2.1 (Reversal Potential)** The **reversal potential** $E_{\mathrm{rev}}$ of a postsynaptic current is the membrane potential at which the current through the transmitter-activated channels is zero and above which it changes sign; for a channel permeable to a single ion it equals that ion's **equilibrium potential**, and for a channel permeable to several ions it lies between their equilibrium potentials.

Near $E_{\mathrm{rev}}$ the current is described by a conductance and a driving force, $I_{\mathrm{syn}} = g_{\mathrm{syn}}(V - E_{\mathrm{rev}})$ (outward positive). The linearity of the end-plate current–voltage relation shows that $g_{\mathrm{syn}}$ does not depend on voltage; the value of $E_{\mathrm{rev}}$ tells which ions flow. For a channel conducting $\ce{Na+}$ and $\ce{K+}$ with conductances $g_{\mathrm{Na}}$ and $g_{\mathrm{K}}$, setting the total current to zero gives the weighted average
$$
E_{\mathrm{rev}} = \frac{g_{\mathrm{Na}}E_{\mathrm{Na}} + g_{\mathrm{K}}E_{\mathrm{K}}}{g_{\mathrm{Na}} + g_{\mathrm{K}}}, \tag{10.1}
$$
the same rule that gives the **resting potential** as a weighted average of equilibrium potentials ([7.16.4](/7.16.4)); a more accurate form uses permeabilities in the **Goldman–Hodgkin–Katz equation**.

**Example 10.2.1** In frog muscle, $[\ce{Na+}]_{\mathrm{o}} = 120$, $[\ce{Na+}]_{\mathrm{i}} = 10$, $[\ce{K+}]_{\mathrm{o}} = 2.5$ and $[\ce{K+}]_{\mathrm{i}} = 140\,\mathrm{mM}$, and the ACh receptor has $P_{\mathrm{K}}/P_{\mathrm{Na}} \approx 1.1$. The GHK voltage equation at $20^\circ\mathrm{C}$ ($RT/F = 25.3\,\mathrm{mV}$) gives
$$
E_{\mathrm{rev}} = 25.3\,\mathrm{mV}\cdot\ln\frac{120 + 1.1\cdot2.5}{10 + 1.1\cdot140} = 25.3\,\mathrm{mV}\cdot\ln 0.749 \approx -7\,\mathrm{mV},
$$
in the range measured. Although the channel is equally permeable to both ions, at a resting potential of $-90\,\mathrm{mV}$ the driving force on $\ce{Na+}$ ($V - E_{\mathrm{Na}} \approx -153\,\mathrm{mV}$) is far larger than that on $\ce{K+}$ ($\approx +11\,\mathrm{mV}$), so the net current is a large $\ce{Na+}$ influx.

:::

The reversal potential decides the sign of a synaptic action, not the transmitter: a synapse is excitatory if $E_{\mathrm{rev}}$ lies above the threshold of the cell, so that opening the channels pushes $V$ toward and past threshold, and inhibitory if $E_{\mathrm{rev}}$ lies below threshold, even if it lies above the resting potential (10.4).

## 10.3. Glutamate Receptors

### 10.3.1. AMPA and NMDA Receptors

Glutamate activates three families of ionotropic receptors named after their selective agonists, AMPA, kainate and NMDA, and eight metabotropic receptors (mGluR1–8). The ionotropic receptors are tetramers whose subunits have a large extracellular amino-terminal domain, a clamshell ligand-binding domain that closes around glutamate, three membrane helices and a re-entrant pore loop (topologically an inverted $\ce{K+}$ channel), and a cytoplasmic tail that binds scaffold proteins.

**Definition 10.3.1 (AMPA Receptor)** An **AMPA receptor** is an ionotropic glutamate receptor assembled from GluA1–GluA4 subunits that opens within a fraction of a millisecond of glutamate binding, conducts $\ce{Na+}$ and $\ce{K+}$ with a reversal potential near $0\,\mathrm{mV}$ and mediates the fast component of excitatory postsynaptic currents; receptors containing the edited subunit GluA2(R) are impermeable to $\ce{Ca^2+}$.

**Definition 10.3.2 (NMDA Receptor)** An **NMDA receptor** is an ionotropic glutamate receptor assembled from two GluN1 and two GluN2 (or GluN3) subunits that requires glutamate (bound to GluN2) and the coagonist glycine or D-serine (bound to GluN1) to open, is highly permeable to $\ce{Ca^2+}$, deactivates slowly (tens to hundreds of milliseconds, depending on the GluN2 subunit) and is blocked in a voltage-dependent manner by extracellular $\ce{Mg^2+}$.

The two receptors usually coexist at the same synapse and divide the work. AMPA receptors have low affinity (half-maximal activation near $0.5\,\mathrm{mM}$ glutamate) and unbind glutamate quickly, so their current follows the millisecond transient of glutamate in the cleft and decays in $1$–$3\,\mathrm{ms}$ at central synapses. NMDA receptors bind glutamate a hundred times more tightly (half-maximal activation near $2\,\mu\mathrm{M}$) and hold it: a 1 ms pulse of glutamate applied to an outside-out patch evokes an NMDA current that lasts more than $100\,\mathrm{ms}$, as long as the synaptic NMDA current (Lester and colleagues, 1990), so the slow decay reflects slow unbinding and repeated opening of bound receptors, not lingering transmitter. Several molecular details have large functional consequences: the Q/R site in the pore of GluA2 is edited from glutamine to arginine in almost all GluA2 mRNA, which makes GluA2-containing AMPA receptors impermeable to $\ce{Ca^2+}$ and insensitive to block by intracellular polyamines; GluA2-lacking receptors (in many interneurons, and transiently after some forms of plasticity) are $\ce{Ca^2+}$-permeable and inwardly rectifying. GluN2B-containing NMDA receptors, dominant early in development, deactivate several times more slowly than GluN2A-containing ones, which replace them during maturation.

### 10.3.2. Mg²⁺ Block and Coincidence Detection

At negative potentials extracellular $\ce{Mg^2+}$ enters the NMDA receptor pore and binds at a site deep in the membrane field, from which it rarely passes; depolarization expels it (Mayer, Westbrook and Guthrie, 1984; Nowak and colleagues, 1984). The physical model of this voltage-dependent block is Woodhull's formula ([Formula 30.3.2](/7.6.30#fml-30.3.2)); for synaptic modeling the fit of Jahr and Stevens (1990) is used.

**Definition 10.3.3 (Magnesium Block)** The **magnesium block** of the NMDA receptor is the voltage-dependent occlusion of its pore by extracellular $\ce{Mg^2+}$. The fraction of unblocked receptors is
$$
B(V) = \frac{1}{1 + \dfrac{[\ce{Mg^2+}]_{\mathrm{o}}}{3.57\,\mathrm{mM}}\,\mathrm{e}^{-0.062\,V/\mathrm{mV}}}, \tag{10.2}
$$
and the NMDA current is $I_{\mathrm{NMDA}} = \bar g_{\mathrm{NMDA}}\,s(t)\,B(V)\,(V - E_{\mathrm{NMDA}})$, with $E_{\mathrm{NMDA}} \approx 0\,\mathrm{mV}$ and $s(t)$ the fraction of glutamate-bound open receptors.

At the physiological $1\,\mathrm{mM}$ $\ce{Mg^2+}$ and $-65\,\mathrm{mV}$, $B = 1/(1 + 0.28\,\mathrm{e}^{4.03}) \approx 0.06$: only about one receptor in sixteen conducts. At $-30\,\mathrm{mV}$, $B \approx 0.36$; at $0\,\mathrm{mV}$, $B \approx 0.78$. The product $B(V)(V - E_{\mathrm{NMDA}})$ makes the current–voltage relation nonmonotonic: between about $-100$ and $-30\,\mathrm{mV}$ depolarization increases the inward current (a region of negative slope conductance), which is regenerative and can produce plateau potentials and dendritic NMDA spikes ([7.16.13](/7.16.13)).

![Voltage dependence of glutamate receptor currents. A: unblocked fraction of NMDA receptors, Eq. (10.2), at four extracellular $\ce{Mg^2+}$ concentrations; at rest (dotted line) and $1\,\mathrm{mM}$ $\ce{Mg^2+}$ only about 6% of the receptors conduct. B: peak current–voltage relations for $1\,\mathrm{nS}$ of conductance with $E_{\mathrm{rev}} = 0\,\mathrm{mV}$: the AMPA relation is linear, the NMDA relation at $1\,\mathrm{mM}$ $\ce{Mg^2+}$ has a region of negative slope below about $-30\,\mathrm{mV}$, and becomes linear in $\ce{Mg^2+}$-free solution (dashed).](./plots/nmda-block.py)

**Definition 10.3.4 (Coincidence Detection)** A molecule or a neuron performs **coincidence detection** when its response requires two inputs within a limited time window and is much smaller for either alone; the NMDA receptor is a coincidence detector because current (and $\ce{Ca^2+}$ influx) requires both bound glutamate, signaling presynaptic release, and postsynaptic depolarization relieving the magnesium block.

The time window of the NMDA receptor as a coincidence detector is set by its slow deactivation: glutamate released up to about $100\,\mathrm{ms}$ before a depolarization (a back-propagating spike, a dendritic plateau, or strong synaptic input elsewhere on the cell) can still pass $\ce{Ca^2+}$. This makes the receptor a molecular implementation of the conjunction required by Hebb's postulate, and its $\ce{Ca^2+}$ signal the trigger of long-term potentiation and depression ([7.16.14](/7.16.14)).

In practice the two components are separated pharmacologically (the AMPA antagonist NBQX, the NMDA antagonist APV) or by voltage. At $-70\,\mathrm{mV}$ the EPSC is almost purely AMPA; at $+40\,\mathrm{mV}$ the $\ce{Mg^2+}$ block is relieved, the current is outward and its late part, after the AMPA current has decayed, is due to NMDA receptors. The ratio of the NMDA current at $+40\,\mathrm{mV}$, $50\,\mathrm{ms}$ after stimulation, to the peak AMPA current at $-70\,\mathrm{mV}$ (the NMDA/AMPA ratio) is a standard index of the postsynaptic composition of a synapse, used for example to detect the insertion of AMPA receptors after plasticity or after exposure to drugs of abuse. Synapses that have NMDA but no AMPA receptors are silent at rest and conduct only when depolarized; such "silent synapses" are common early in development and are unsilenced by AMPA receptor insertion.

![AMPA and NMDA components of a simulated EPSC. The AMPA conductance (rise $0.2\,\mathrm{ms}$, decay $2\,\mathrm{ms}$, peak $1\,\mathrm{nS}$) and the NMDA conductance (rise $3\,\mathrm{ms}$, decay $80\,\mathrm{ms}$, peak $0.5\,\mathrm{nS}$, blocked according to Eq. (10.2) at $1\,\mathrm{mM}$ $\ce{Mg^2+}$) are added. A: at $-70\,\mathrm{mV}$ the current is inward and almost entirely AMPA-mediated. B: at $+40\,\mathrm{mV}$ it is outward, and the slow NMDA component dominates after a few milliseconds; the dotted line marks the time at which the NMDA component is usually measured.](./plots/ampa-nmda-epsc.py)

### 10.3.3. The Postsynaptic Density

Receptors are not scattered over the dendrite but concentrated opposite the active zone in a disk of protein a few hundred nanometers wide and about $30$–$50\,\mathrm{nm}$ thick.

**Definition 10.3.5 (Postsynaptic Density)** The **postsynaptic density** (PSD) is the protein-dense specialization beneath the postsynaptic membrane of an excitatory synapse that anchors glutamate receptors and organizes their signaling partners; its core is a lattice of **scaffold proteins**, the PDZ-domain proteins of the PSD-95 family linked to SAPAP, Shank and Homer, which bind the cytoplasmic tails of NMDA receptors, of AMPA receptors (through the auxiliary TARP subunits such as stargazin), of adhesion molecules and of signaling enzymes such as CaMKII.

A PSD contains roughly ten to twenty NMDA receptors, a variable number of AMPA receptors (zero to more than a hundred, scaling with spine volume, [7.16.9](/7.16.9#sec-9.2.3)), and several hundred copies of PSD-95; CaMKII is among the most abundant proteins in the forebrain PSD. AMPA receptors diffuse laterally in the membrane and are captured and released by the scaffold on a time scale of seconds to minutes; changing the number of slots is one way synaptic strength is changed. Inhibitory synapses use a different scaffold, gephyrin, which clusters glycine and $\mathrm{GABA_A}$ receptors.

## 10.4. Inhibition

### 10.4.1. GABA_A and Glycine Receptors

**Definition 10.4.1 ($\mathrm{GABA_A}$ Receptor)** A **$\mathrm{GABA_A}$ receptor** is a pentameric GABA-gated anion channel of the Cys-loop family (most commonly two $\alpha$, two $\beta$ and one $\gamma$ subunit) that conducts mainly $\ce{Cl-}$ and to a lesser extent $\ce{HCO3-}$; it mediates fast synaptic inhibition in the brain and is the target of benzodiazepines, barbiturates, neurosteroids and many general anesthetics, which increase its opening.

Benzodiazepines bind at the $\alpha$–$\gamma$ interface and increase the affinity for GABA, so they amplify synaptic inhibition but do not open the channel by themselves; receptors containing $\delta$ instead of $\gamma$ are extrasynaptic, have high affinity and produce a tonic inhibitory conductance from ambient GABA. The glycine receptor is the analogous anion channel of the spinal cord and brainstem; strychnine blocks it and causes convulsions. The metabotropic $\mathrm{GABA_B}$ receptor, a G protein–coupled receptor that opens GIRK channels and inhibits $\ce{Ca^2+}$ channels, produces slow inhibition ([7.16.11](/7.16.11)).

### 10.4.2. The Chloride Gradient and Depolarizing GABA

Whether a $\ce{Cl-}$ conductance hyperpolarizes depends on $E_{\mathrm{Cl}}$, which is set by $\ce{Cl-}$ transporters: the $\ce{K+}$–$\ce{Cl-}$ cotransporter KCC2 extrudes $\ce{Cl-}$ using the $\ce{K+}$ gradient, and the $\ce{Na+}$–$\ce{K+}$–$2\ce{Cl-}$ **cotransporter** NKCC1 accumulates it using the $\ce{Na+}$ gradient. With the **Nernst equation** for an anion, $E_{\mathrm{Cl}} = (RT/F)\ln([\ce{Cl-}]_{\mathrm{i}}/[\ce{Cl-}]_{\mathrm{o}})$; at $37^\circ\mathrm{C}$ ($RT/F = 26.7\,\mathrm{mV}$) and $[\ce{Cl-}]_{\mathrm{o}} = 130\,\mathrm{mM}$:

| Cell | $[\ce{Cl-}]_{\mathrm{i}}$ | $E_{\mathrm{Cl}}$ | Action of GABA at rest ($-65\,\mathrm{mV}$) |
|---|---|---|---|
| Mature cortical neuron (KCC2 high) | $\approx 7\,\mathrm{mM}$ | $\approx -78\,\mathrm{mV}$ | Hyperpolarizing |
| Neuron with $[\ce{Cl-}]_{\mathrm{i}}$ near passive distribution | $\approx 10\,\mathrm{mM}$ | $\approx -68\,\mathrm{mV}$ | Nearly silent, shunting |
| Immature neuron (NKCC1 high, KCC2 low) | $\approx 25$–$30\,\mathrm{mM}$ | $\approx -40\,\mathrm{mV}$ | Depolarizing |

In immature neurons GABA depolarizes and can even excite, and this depolarization drives the $\ce{Ca^2+}$ signals of early network activity in the developing hippocampus and cortex (Ben-Ari and colleagues); around the first postnatal week in rodents, rising KCC2 expression switches GABA to inhibition (Rivera and colleagues, 1999). Because the $\mathrm{GABA_A}$ receptor also passes $\ce{HCO3-}$ (permeability about 0.2 of that of $\ce{Cl-}$, with $E_{\mathrm{HCO_3}} \approx -12\,\mathrm{mV}$), its reversal potential lies a few millivolts above $E_{\mathrm{Cl}}$. Pathological loss of KCC2, after nerve injury or in some epilepsies, makes inhibition weaker or excitatory and is one mechanism of neuropathic pain and seizures.

### 10.4.3. The Arithmetic of Shunting Inhibition

An inhibitory synapse whose reversal potential equals the resting potential produces no IPSP by itself but still inhibits. In a single compartment with leak conductance $g_{\mathrm{L}}$ at $E_{\mathrm{L}}$, excitatory conductance $g_e$ at $E_e$ and inhibitory conductance $g_i$ at $E_i$, the steady potential is the conductance-weighted average
$$
V = \frac{g_{\mathrm{L}}E_{\mathrm{L}} + g_eE_e + g_iE_i}{g_{\mathrm{L}} + g_e + g_i}. \tag{10.3}
$$

**Proposition 10.4.1 (Shunting Inhibition Is Divisive)** If $E_i = E_{\mathrm{L}}$, the depolarization produced by the excitatory conductance is
$$
\Delta V = \frac{g_e(E_e - E_{\mathrm{L}})}{g_{\mathrm{L}} + g_e + g_i}, \tag{10.4}
$$
so for small inputs ($g_e \ll g_{\mathrm{L}} + g_i$) inhibition divides the EPSP by the factor $1 + g_i/g_{\mathrm{L}}$, whereas a hyperpolarizing inhibition ($E_i < E_{\mathrm{L}}$) adds a negative term $g_i(E_i - E_{\mathrm{L}})/(g_{\mathrm{L}} + g_e + g_i)$ as well.

**Proof** Subtract $E_{\mathrm{L}}$ from both sides of Eq. (10.3): $V - E_{\mathrm{L}} = [g_e(E_e - E_{\mathrm{L}}) + g_i(E_i - E_{\mathrm{L}})]/(g_{\mathrm{L}} + g_e + g_i)$, and set $E_i = E_{\mathrm{L}}$. $\square$

This is the quantitative content of **shunting inhibition** ([7.14.6](/7.14.6#sec-6.3.2)): the inhibitory conductance acts as a short circuit that draws away the excitatory current. Divisive and subtractive inhibition have different computational consequences: the first scales the gain of the input–output relation, the second shifts it. In a passive membrane the steady effect is divisive only for small inputs and becomes partly subtractive once the neuron fires, because the spike threshold clamps $V$ (Holt and Koch, 1997); divisive gain control in vivo arises mostly from network mechanisms such as balanced changes of excitation and inhibition and from noise. Shunting is also strongly local: a conductance acts mostly on the current that must pass it on its way to the soma, which makes the position of inhibitory synapses decisive ([7.16.13](/7.16.13)).

![Shunting and hyperpolarizing inhibition in a single compartment (Eq. (10.3); $g_{\mathrm{L}} = 10\,\mathrm{nS}$, $E_{\mathrm{L}} = -65\,\mathrm{mV}$, $E_e = 0\,\mathrm{mV}$). A: depolarization by an excitatory conductance of $2\,\mathrm{nS}$ against the inhibitory conductance. Shunting inhibition ($E_i = -65\,\mathrm{mV}$) has no effect on its own (dashed line at zero) but reduces the EPSP; hyperpolarizing inhibition ($E_i = -80\,\mathrm{mV}$) adds a hyperpolarization. B: depolarization against excitatory conductance at three levels of shunting inhibition: the initial slope of the input–output curve is divided by $1 + g_i/g_{\mathrm{L}}$.](./plots/shunting.py)

## 10.5. Electrical Synapses

An **electrical synapse** couples two cells through **gap junction** channels, each formed by two hemichannels (connexons) of six **connexin** subunits ([7.14.5](/7.14.5#sec-5.4.1)); in invertebrates the same function is served by the unrelated innexins, and the main neuronal connexin of mammals is Cx36. Current flows in proportion to the voltage difference, $I_{1\to2} = g_{\mathrm{c}}(V_1 - V_2)$, so the coupling is bidirectional and instantaneous. Its strength is measured by the coupling coefficient: injecting current into cell 1 and measuring both cells at steady state gives
$$
k_{12} = \frac{\Delta V_2}{\Delta V_1} = \frac{g_{\mathrm{c}}}{g_{\mathrm{c}} + g_2}, \tag{10.5}
$$
where $g_2$ is the input conductance of cell 2 itself, so a junction appears stronger when the postsynaptic cell is small. Typical coefficients between coupled cortical interneurons are $0.05$–$0.2$. Because cell 2 also has a capacitance, the junction is a low-pass filter: slow potentials pass much better than the brief spike (the coupling coefficient for a spike is often five to ten times smaller than the steady value), and the afterhyperpolarization of a presynaptic spike can be transmitted as an inhibitory signal. Some junctions rectify: the crayfish giant motor synapse, where electrical transmission was discovered, conducts depolarization only from pre- to postsynaptic cell (Furshpan and Potter, 1959).

Electrical synapses are fast, require no transmitter machinery and synchronize. They couple inhibitory interneurons of the same class into networks that fire synchronously (supporting gamma oscillations, [7.16.15](/7.16.15)), couple neurons of the inferior olive whose synchronized subthreshold oscillations time cerebellar climbing-fiber input, and couple rods and cones and some retinal neurons, where coupling averages away noise at the cost of spatial resolution. Many synapses are mixed, with chemical and electrical components at the same contact. The model of gap junction coupling and its synchronizing effect on two spiking neurons is in [7.16.12](/7.16.12).

## 10.6. The Kinetics of Ionotropic Receptors

The time course of a postsynaptic current reflects how receptors bind, open, close and desensitize. Following the approach of [7.6.30](/7.6.30#sec-30.3.3), a receptor is described by a **Markov chain** of discrete states with transition rates that depend on the agonist concentration $T$.

**Formula 10.6.1 (Kinetic Scheme of a Glutamate Receptor)** A minimal scheme for an AMPA receptor that binds two glutamate molecules before opening, and that can desensitize from the doubly bound closed state, is
$$
C_0 \underset{k_{\mathrm{off}}}{\overset{2k_{\mathrm{on}}T}{\rightleftharpoons}} C_1 \underset{2k_{\mathrm{off}}}{\overset{k_{\mathrm{on}}T}{\rightleftharpoons}} C_2 \underset{\alpha}{\overset{\beta}{\rightleftharpoons}} O, \qquad C_2 \underset{k_{\mathrm{r}}}{\overset{k_{\mathrm{d}}}{\rightleftharpoons}} D,
$$
where $O$ is the open state and $D$ a desensitized closed state; the occupancies $\boldsymbol{p}(t)$ obey $\mathrm{d}\boldsymbol{p}/\mathrm{d}t = Q(T)\boldsymbol{p}$, and the current is $I = N_{\mathrm{ch}}\gamma\,p_O(t)\,(V - E_{\mathrm{rev}})$.

Two processes end the response. *Deactivation* is the closing that follows removal of the agonist: when glutamate is cleared within about a millisecond (as in the cleft), the current decays with the rate at which receptors close and unbind, and the decay of the EPSC is essentially the deactivation time course of the receptor (figure below, A, green). **Desensitization** is the closing that occurs in the continued presence of agonist, when receptors enter the bound but closed state $D$; AMPA receptors desensitize within $5$–$10\,\mathrm{ms}$ to a few percent of the peak (red). Recovery from desensitization is slow (tens of milliseconds, B), so desensitization can contribute to depression at synapses where glutamate accumulates during high-frequency firing, such as the calyx of Held. The scheme also explains why the dose–response curve of a receptor is steeper than a simple binding isotherm: with two binding steps before opening, the peak open probability at low $T$ grows as $T^2$, and the curve is fitted by the **Hill equation** with a Hill coefficient between 1 and 2, a signature of **cooperativity** ([7.14.8](/7.14.8#sec-8.4.1)).

![A kinetic scheme of an AMPA-type receptor (Formula 10.6.1, with $k_{\mathrm{on}} = 5\,\mathrm{mM^{-1}\,ms^{-1}}$, $k_{\mathrm{off}} = 4$, $\beta = 8$, $\alpha = 2$, $k_{\mathrm{d}} = 0.8$ and $k_{\mathrm{r}} = 0.015\,\mathrm{ms^{-1}}$). A: open probability during a $1\,\mathrm{ms}$ pulse of $1\,\mathrm{mM}$ glutamate (shaded), similar to synaptic release, which decays by deactivation within a few milliseconds, and during a prolonged application, which decays by desensitization with a time constant of about $8\,\mathrm{ms}$ to a small steady level. B: ratio of the second to the first peak for paired $1\,\mathrm{ms}$ pulses: even a brief pulse desensitizes some receptors, which recover over about $100\,\mathrm{ms}$.](./plots/receptor-kinetics.py)

For network models such detailed schemes are usually too expensive. They are reduced to a single **gating variable** $s(t)$ with first-order kinetics, or replaced by fixed waveforms (exponential, α and difference-of-exponential conductances); these reductions, and the voltage-dependent NMDA conductance in the same form as Definition 10.3.3, are the subject of [7.16.12](/7.16.12).

## Summary

- A neurotransmitter is identified by synthesis, $\ce{Ca^2+}$-dependent release, mimicry by exogenous application and a mechanism of inactivation (10.1). Glutamate, GABA and glycine carry fast signaling; the amines and peptides mostly modulate.
- The sign of a postsynaptic current is set by its reversal potential (Definition 10.2.1) relative to threshold: $I_{\mathrm{syn}} = g_{\mathrm{syn}}(V - E_{\mathrm{rev}})$, with $E_{\mathrm{rev}}$ a conductance-weighted average of the equilibrium potentials of the permeant ions (Eq. (10.1), Example 10.2.1).
- AMPA receptors (Definition 10.3.1) give the fast EPSC; NMDA receptors (Definition 10.3.2) are slow, $\ce{Ca^2+}$-permeable and blocked by $\ce{Mg^2+}$ according to Eq. (10.2), which makes them coincidence detectors (Definition 10.3.4) of presynaptic release and postsynaptic depolarization. The PSD (Definition 10.3.5) anchors them.
- Inhibitory $\mathrm{GABA_A}$ and glycine receptors (Definition 10.4.1) conduct $\ce{Cl-}$; $E_{\mathrm{Cl}}$, set by KCC2 and NKCC1, decides whether GABA hyperpolarizes, shunts or depolarizes. Shunting inhibition divides small EPSPs by $1 + g_i/g_{\mathrm{L}}$ (Proposition 10.4.1).
- Electrical synapses couple cells with coefficient $g_{\mathrm{c}}/(g_{\mathrm{c}} + g_2)$ (Eq. (10.5)), act as low-pass filters and synchronize.
- Receptor kinetics (Formula 10.6.1) separate deactivation, which shapes the EPSC, from desensitization, which shapes the response to prolonged or repeated transmitter.

| Current | Rise | Decay | $E_{\mathrm{rev}}$ | Voltage dependence |
|---|---|---|---|---|
| AMPA | $0.2$–$0.5\,\mathrm{ms}$ | $1$–$5\,\mathrm{ms}$ | $0\,\mathrm{mV}$ | None (GluA2-containing) |
| NMDA | $2$–$10\,\mathrm{ms}$ | $40$–$300\,\mathrm{ms}$ | $0\,\mathrm{mV}$ | $\ce{Mg^2+}$ block, Eq. (10.2) |
| $\mathrm{GABA_A}$ | $0.5$–$1\,\mathrm{ms}$ | $5$–$20\,\mathrm{ms}$ | $-80$ to $-60\,\mathrm{mV}$ (adult) | None |
| $\mathrm{GABA_B}$ (via GIRK) | $30$–$50\,\mathrm{ms}$ | $100$–$300\,\mathrm{ms}$ | $E_{\mathrm{K}}$, about $-90\,\mathrm{mV}$ | Inward rectification |

## Questions

1. The reversal potential of a GABA-activated current in a neuron is $-55\,\mathrm{mV}$, its resting potential $-65\,\mathrm{mV}$ and its spike threshold $-50\,\mathrm{mV}$. Is this synapse excitatory or inhibitory? What would you predict for an EPSP arriving simultaneously with the GABA input?

   **Answer** Opening the GABA channels alone depolarizes the cell toward $-55\,\mathrm{mV}$, but never beyond, so it cannot by itself reach the threshold of $-50\,\mathrm{mV}$: by Definition 10.2.1 the synapse is inhibitory, although its potential change is depolarizing. Combined with an EPSP, the GABA conductance clamps $V$ toward $-55\,\mathrm{mV}$: if the EPSP alone would have carried $V$ above $-55\,\mathrm{mV}$, the added conductance pulls it back and reduces the probability of firing (shunting plus a small depolarization). Only for weak EPSPs that stay below $-55\,\mathrm{mV}$ does the GABA input bring the cell closer to threshold. Such depolarizing but inhibitory GABA is typical of neurons with intermediate $[\ce{Cl-}]_{\mathrm{i}}$.

2. Using Eq. (10.2), compute the ratio of NMDA current at $-30\,\mathrm{mV}$ to that at $-70\,\mathrm{mV}$ for the same bound conductance at $1\,\mathrm{mM}$ $\ce{Mg^2+}$, and compare with the ratio for AMPA receptors. What does this mean for an NMDA synapse onto a dendrite that is depolarized by other inputs?

   **Answer** $B(-30) = 1/(1 + 0.280\,\mathrm{e}^{1.86}) = 1/(1 + 1.80) = 0.357$ and $B(-70) = 1/(1 + 0.280\,\mathrm{e}^{4.34}) = 1/(1 + 21.5) = 0.044$. The currents are proportional to $B(V)\cdot V$: $0.357\cdot(-30) = -10.7$ and $0.044\cdot(-70) = -3.1$, a ratio of about $3.4$: the inward NMDA current increases more than threefold although the driving force has fallen. For AMPA the ratio is $30/70 = 0.43$. A depolarized dendrite therefore responds much more strongly to NMDA input, which makes the response to clustered or coincident inputs supralinear and underlies dendritic NMDA spikes.

3. Two cells are coupled by gap junctions with $g_{\mathrm{c}} = 1\,\mathrm{nS}$; cell 1 has an input conductance (without the junction) of $5\,\mathrm{nS}$ and cell 2 of $20\,\mathrm{nS}$. Compute the coupling coefficients in both directions and explain the asymmetry even though the junction itself is symmetric.

   **Answer** By Eq. (10.5), $k_{12} = 1/(1 + 20) = 0.048$ and $k_{21} = 1/(1 + 5) = 0.17$. The junction conducts equally in both directions, but the same junctional current produces a smaller voltage change in the cell with the larger own conductance (the larger or leakier cell). Asymmetric coupling coefficients therefore do not imply a rectifying junction; rectification is shown only by an asymmetric junctional current–voltage relation measured with both cells clamped.

4. (Open question) In the kinetic scheme of Formula 10.6.1, how would you distinguish experimentally whether the decay of an EPSC is determined by receptor deactivation, by desensitization, or by the clearance of glutamate from the cleft?

   **Answer** Pull an outside-out patch containing the receptors and apply glutamate with a fast piezo-driven perfusion system. A $1\,\mathrm{ms}$ pulse measures deactivation, a long pulse measures desensitization; if the EPSC decay matches the deactivation time constant, clearance is faster than deactivation and does not limit the decay. Clearance is tested at the synapse itself: slowing it (blocking transporters with TBOA, or increasing release so that glutamate accumulates) should prolong the EPSC if clearance limits the decay; a rapidly dissociating competitive antagonist (such as γ-DGG) is displaced more by high glutamate and reports the glutamate transient. Desensitization is tested with drugs that block it (cyclothiazide for AMPA receptors): if they prolong the EPSC or relieve paired-pulse depression, desensitization contributes.
