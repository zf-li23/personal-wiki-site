---
title: Neurons and Synaptic Transmission
description: "The neuron doctrine; structure and classification of neurons, and glia; neuronal polarity: microtubules and axonal transport, the diffusion barrier of the axon initial segment and the ATP ledger of the two lines of defense; passive decay in dendrites, spatial and temporal summation, Rall's 3/2 law, Murray's and Da Vinci's branching laws; chemical and electrical synapses, transmitter release and the cooperativity of Ca²⁺, transmitters and receptors, EPSPs and IPSPs, synaptic delay and termination of transmitters; short-term plasticity, LTP and LTD; the two protein families of electrical synapses, the nerve nets of cnidarians, the dispute over the origin of the ctenophore nervous system."
source_hash: 35e9ac6eccca
---

Chapter 4 discussed how a single excitable membrane generates and conducts an **action potential** ([7.14.4](/7.14.4)). This chapter widens the view to the whole cell and to the relations between cells: how the **neuron** divides, in form and in molecules, into dendrites that receive input and an axon that sends output, and how this polarity is established and maintained; how dendrites add up thousands of synaptic inputs; how signals pass across a synapse from one cell to the next; and how synaptic efficacy changes with use. These are the common basis of Chapter 6 on neural circuits, Chapter 7 on the organization of the nervous system, and the later chapters on sensation and movement. The development of neurons (axon guidance and synapse formation) is in [7.5.21](/7.5.21), the physics of ion channels and the cable equation in [7.6.30](/7.6.30), and microtubules and motor proteins in [7.3.14](/7.3.14); the computational theory of networks and learning rules is left to computational neuroscience ([7.16](/7.16)).

## 5.1. Neurons and Nervous Tissue

### 5.1.1. The Neuron Doctrine

Under the nineteenth-century microscope, nervous tissue was a tangle of fibers, and the dominant reticular theory held that the nervous system is a continuous syncytial network. In 1873 Golgi invented the silver chromate stain (the "black reaction"), which stains a random few cells completely black and for the first time let the whole form of a single nerve cell be seen. Cajal used this method to observe almost all brain regions systematically and reached the opposite conclusion: each nerve cell is an independent unit, and fibers touch but do not fuse; from morphology he also inferred that signals flow from the dendrites through the cell body to the axon (the "law of dynamic polarization"). The two shared the 1906 Nobel Prize, and Golgi still defended the reticular theory in his Nobel lecture.

**Definition 5.1.1 (Neuron Doctrine)** The **neuron doctrine** holds that the nervous system is made up of discrete cells (neurons); that the neuron is the basic unit of the structure, development and function of the nervous system; and that signals within a neuron flow in one direction, from receiving sites to output sites, and are transmitted between neurons at specialized contacts.

In 1897 Sherrington named this contact the *synapse*. Not until the 1950s did the electron microscope show the gap of about $20\,\mathrm{nm}$ between presynaptic and postsynaptic membranes, finally confirming the neuron doctrine. Exceptions were later found: at electrical synapses the cytoplasm of the two cells communicates directly through **gap junctions** (5.4.1), and the nerve nets of some invertebrates are even true syncytia (5.6).

### 5.1.2. Structure and Classification of Neurons

A typical vertebrate neuron consists of four compartments:

- Cell body: contains the nucleus, rough endoplasmic reticulum (Nissl bodies) and Golgi apparatus, and almost all proteins are synthesized here; the cell body also integrates inputs.
- Dendrites: branches from the cell body, densely studded with transmitter receptors, the main receiving surface; the dendrites of cortical pyramidal cells bear tens of thousands of dendritic spines, each usually carrying one excitatory synapse.
- Axon: usually only one, arising from the axon hillock of the cell body; the first $20$–$60\,\mu\mathrm{m}$ is the axon initial segment (5.2.2), where the action potential starts. The axon can be as long as $1\,\mathrm{m}$ (motor neurons innervating the foot), myelinated or unmyelinated.
- Axon terminals: the branches and swellings (boutons) at the end of the axon, containing synaptic vesicles, are the output sites.

The **resting potential** of central neurons is about $-65\,\mathrm{mV}$, shallower than that of peripheral nerve fibers and skeletal muscle (about $-90\,\mathrm{mV}$) and closer to threshold: such an intermediate state allows the neuron to be pushed toward firing by excitatory inputs and away from threshold by inhibitory inputs. The cell body is large and its internal resistance small, so it is approximately isopotential electrically.

Neurons can be classified by many criteria:

| Criterion | Classes | Examples |
|---|---|---|
| Number of processes | Multipolar, bipolar, pseudounipolar (one process divides into a central and a peripheral branch), unipolar | Motor neurons, retinal bipolar cells, dorsal root ganglion cells, most invertebrate neurons |
| Function | Sensory (afferent), motor (efferent), interneuron | Interneurons make up more than 99% of the neurons in the human body |
| Axonal projection | Projection neurons (between brain regions), local circuit neurons | Cortical pyramidal cells, basket cells |
| Transmitter | Cholinergic, glutamatergic, GABAergic, adrenergic, dopaminergic and so on | |
| Effect on the postsynaptic cell | Excitatory, inhibitory | |

Modern classification also includes the branching morphology of dendrites, electrophysiological firing patterns and single-cell transcriptomes, the last of which distinguishes more than a hundred types in the mouse cortex.

### 5.1.3. Glial Cells

The other large class of cells in nervous tissue is the *glia*. They have processes but no distinction between dendrites and axon, produce no action potentials, are generally connected to one another by **gap junctions**, and their **membrane potential** varies mainly with extracellular $\ce{K+}$ concentration. The commonly repeated statement that "there are ten times as many glia as neurons" has no basis: counted by the isotropic fractionator method the human brain has about $8.6\times10^{10}$ neurons and $8.5\times10^{10}$ non-neuronal cells (including endothelial cells), roughly equal in number (Azevedo et al., 2009; see the figure in [7.14.7](/7.14.7)).

| Type | Location | Main functions |
|---|---|---|
| Astrocytes | Central | Disperse locally accumulated $\ce{K+}$ to distant sites through $\ce{K+}$ channels and gap junctions (spatial buffering); take up glutamate and GABA from the synaptic cleft with EAAT transporters and return them to neurons through the glutamate–glutamine cycle; end-feet ensheathe capillaries, induce and maintain the **blood–brain barrier** and regulate local blood flow; enwrap synapses (the "tripartite synapse"); proliferate after injury to form the glial scar |
| Oligodendrocytes | Central | Form myelin; one cell can wrap one segment each of several tens of axons |
| Schwann cells | Peripheral | Form myelin, one cell wrapping only one internode; unmyelinated fibers are also enclosed by Schwann cells; guide regeneration after axon injury |
| Microglia | Central | Resident macrophages of the central nervous system, derived from myeloid progenitors of the yolk sac; surveillance and phagocytosis, prune synapses marked by complement during development |
| Ependymal cells | Lining of the ventricles and central canal | Cilia propel cerebrospinal fluid; take part in forming the choroid plexus |
| Satellite cells | Peripheral ganglia | Surround the cell bodies of ganglion cells |

Myelin lowers the capacitance of the axon and raises its membrane resistance by about two orders of magnitude, so that the action potential can undergo **saltatory conduction** between nodes of Ranvier; the internodal length is about 100 times the outer fiber diameter ($0.2$–$2\,\mathrm{mm}$) and the node is only about $1\,\mu\mathrm{m}$ long. The relation between **conduction velocity** and fiber diameter is in [7.14.4](/7.14.4), and the development of myelination in [7.5.21](/7.5.21).

## 5.2. Neuronal Polarity

### 5.2.1. Microtubules, Motors and Compartments

The morphological polarity of the neuron rests on the arrangement of **microtubules**. Microtubules in the axon have almost all their plus ends pointing outward, stabilized by **microtubule-associated proteins** specific to the axon (tau and others); microtubules in mammalian dendrites have mixed orientations, stabilized by MAP2 and others. **Motor proteins** read this polarity: **kinesin** moves toward the plus end, carrying vesicles and organelles from the cell body to the axon terminal (anterograde), and **dynein** carries endosomes, damaged organelles and neurotrophic signals from target tissue back to the cell body (retrograde); in dendrites of mixed polarity both motors can carry cargo inward. This is **axonal transport**: fast transport at $50$–$400\,\mathrm{mm}$ per day carries membranous organelles; slow transport at $0.2$–$8\,\mathrm{mm}$ per day carries cytoskeletal proteins and soluble enzymes (for the physics of motor teams see [7.3.14](/7.3.14#sec-14.5.3)). Axonal transport is also the route by which some viruses and toxins enter the central nervous system: rabies virus, poliovirus and tetanus toxin are carried retrogradely from peripheral terminals to the cell body, while herpesviruses lie latent in sensory ganglia and travel anterogradely along the axon back to the skin.

Vesicles bearing different membrane proteins are sorted and sent to their own compartments, so that the dendritic membrane carries mainly transmitter receptors (AMPA, NMDA, GABA receptors) and few **voltage-gated sodium channels**, while the axonal membrane is rich in voltage-gated sodium and potassium channels. The electrical division of labor (dendrites integrating passively and in a graded way, the axon conducting actively and without decrement) is thus reduced to an asymmetry in the distribution of membrane proteins.

How does polarity first arise? Cultured hippocampal neurons first extend several similar neurites, of which one wins and becomes the axon ([7.5.21](/7.5.21#sec-21.1)). Let neurite $i$ have length $L_i$ and let the "growth-promoting state" at its distal end be $s_i$ (a combination of microtubule stabilization, membrane supply and accumulation of factors such as shootin1); a minimal model is

$$
\frac{\mathrm{d}L_i}{\mathrm{d}t} = v_0 + \alpha s_i - \mu L_i,
\qquad
\frac{\mathrm{d}s_i}{\mathrm{d}t} = k L_i\left(1 - \frac{\sum_j s_j}{S_{\mathrm{tot}}}\right) - \gamma s_i + \eta_i(t),
$$

where $kL_i$ is a length-dependent **positive feedback** (Toriyama et al. found that shootin1 accumulates at neurite tips in proportion to length), $S_{\mathrm{tot}}$ is a finite resource shared by the whole cell, and $\eta_i$ is a random perturbation. Positive feedback amplifies a small random lead, and the finite resource lets the winner suppress the other neurites, so the symmetric state becomes unstable and only one axon remains; like the model of axons competing for neurotrophic factors in [7.5.21](/7.5.21#sec-21.7.2), this belongs to the winner-take-all mechanism of "positive feedback plus a shared resource".

### 5.2.2. The Axon Initial Segment: A Diffusion Barrier

Transport solves only the problem of how proteins get into place. Membrane proteins sit in a two-dimensionally fluid **lipid bilayer** and diffuse laterally by thermal motion, tending to mix; what, then, prevents dendritic proteins from leaking into the axon?

**Definition 5.2.1 (Axon Initial Segment)** The **axon initial segment** (AIS) is the stretch of axon, about $20$–$60\,\mu\mathrm{m}$ long, immediately following the cell body. Beneath its membrane lies a dense cytoskeleton built around the anchoring protein ankyrin-G, with βIV-spectrin and actin rings of about $190\,\mathrm{nm}$ periodicity, which anchors voltage-gated $\ce{Na+}$ channels (Nav1.6, Nav1.2) and KCNQ (Kv7) channels at high density; it is the site where the action potential starts and the molecular boundary between the somatodendritic and axonal compartments.

The $\ce{Na+}$ channel density of the AIS is tens of times that of the cell body, so after EPSPs are collected at the cell body the threshold is crossed here first, and the action potential propagates both forward along the axon and backward into the cell body and dendrites. The position and length of the AIS also adjust with activity (moving distally and shortening when activity rises), a way of regulating **excitability**.

**Formula 5.2.1 (Time for Diffusion to Smooth Out a Gradient)** The characteristic time for molecules to cross an axial distance $L$ by random walk is ([7.6.5](/7.6.5#sec-5.1.3))

$$
\tau \approx \frac{L^2}{2D}. \tag{5.1}
$$

The lateral **diffusion coefficient** of membrane proteins in a free membrane is about $0.1$–$1\,\mu\mathrm{m^2\,s^{-1}}$. Taking $D = 0.1\,\mu\mathrm{m^2\,s^{-1}}$ and $L = 40\,\mu\mathrm{m}$, $\tau \approx 1600/0.2\,\mathrm{s} \approx 2.2\,\mathrm{h}$: without a barrier, the membrane protein composition of dendrite and axon would mix within a few hours. The only adjustable quantity in Eq. (5.1) is $D$, and the most economical approach is not to fight diffusion over the whole cell but to set up a region of high resistance only at the neck between the two compartments. The submembrane skeleton of the AIS is exactly such a molecular fence: single-molecule tracking shows that the effective diffusion coefficient of lipids and membrane proteins in the AIS is one to two orders of magnitude lower than in the somatic membrane (Nakada et al., 2003). Taking a 50-fold reduction ($D_{\mathrm{AIS}} = 0.002\,\mu\mathrm{m^2\,s^{-1}}$), the crossing time lengthens to about 4.6 days. When ankyrin-G is removed by RNA interference, all components of the AIS disassemble within days, dendritic marker proteins invade the proximal axon, and the axon even grows dendritic spines and turns into a dendrite (Hedstrom, Ogawa and Rasband, 2008).

A barrier only slows leakage and cannot prevent it, so there is a second line of defense: dendritic membrane proteins that stray into the AIS are brought into contact with ankyrin-G, triggering endocytosis, and are sent for degradation rather than recycled to the membrane.

### 5.2.3. The ATP Ledger of the Two Lines of Defense

**Example 5.2.1 (How Much ATP Does Maintaining Polarity Cost?)** The following order-of-magnitude estimate shows that the costs of the two lines of defense are comparable. Assume (all representative values): the AIS has length $L = 40\,\mu\mathrm{m}$ and radius $r = 1\,\mu\mathrm{m}$; inside the barrier $D_{\mathrm{AIS}} = 0.002\,\mu\mathrm{m^2\,s^{-1}}$; a given dendritic protein has an areal density of $100\,\mu\mathrm{m^{-2}}$ at the proximal end and 0 at the axonal end; clearing and degrading one membrane protein costs about 1500 ATP; and about 20 dendritic proteins must be guarded.

1. Leak flux (**Fick's law**, with the "perimeter" of the cross-section $2\pi r = 6.28\,\mu\mathrm{m}$): $J = D_{\mathrm{AIS}}\cdot 2\pi r\cdot \Delta C/L = 0.002\times6.28\times100/40 \approx 0.031\,\mathrm{s^{-1}}$, about one molecule leaking through every 32 seconds. To keep the axonal end at zero, the clearance rate must equal this: $0.031\times1500 \approx 47\,\mathrm{ATP\,s^{-1}}$ per protein, and about $940\,\mathrm{ATP\,s^{-1}}$ for 20 proteins.
2. Size of the skeleton: the membrane area of the AIS is $2\pi rL \approx 251\,\mu\mathrm{m^2}$; with a $190\,\mathrm{nm}$ lattice each unit is about $0.036\,\mu\mathrm{m^2}$, giving about $7.0\times10^3$ units. Each unit contains about 1 ankyrin-G (about 4000 residues), 2 βIV-spectrin (about 2400 each) and 6 actin (375 each), about $1.1\times10^4$ residues, and the whole segment about $7.7\times10^7$ residues.
3. Construction: adding one amino acid costs about 4 ATP (2 for aminoacylation, 2 GTP for elongation), so building it once costs about $3.1\times10^8$ ATP, equal to about 3.8 days of running the clearance system.
4. Maintenance: skeletal proteins turn over with first-order kinetics and **half-life** $t_{1/2}$, and the steady-state rebuilding power is $7.7\times10^7\times(\ln2/t_{1/2})\times4$; for $t_{1/2} = 5\,\mathrm{d}$ this is about $490\,\mathrm{ATP\,s^{-1}}$ (about 1230 for 2 days and about 250 for 10 days).

At steady state the clearance is thus about twice the skeletal maintenance (between 0.8 and 4 times depending on the half-life); including the one-time construction, the cumulative cost of the skeleton is about 4 times that of clearance on the first day, the two are equal after about 8 days, and clearance is slightly higher thereafter.

![The physics and energetics of maintaining polarity at the axon initial segment (AIS). A: the time $L^2/2D$ for a membrane protein to diffuse a distance $L$ along the axon, in a free membrane ($D = 0.1\,\mu\mathrm{m^2\,s^{-1}}$) and in the AIS (the submembrane skeleton lowers the effective diffusion coefficient about 50-fold, $D = 0.002\,\mu\mathrm{m^2\,s^{-1}}$); the dashed lines mark an AIS $40\,\mu\mathrm{m}$ long, which would mix in about 2.2 hours without a barrier and in about 4.6 days with one. B: cumulative ATP cost of Example 5.2.1. The skeleton costs $3.1\times10^8$ ATP to build once and then turns over with a half-life of 5 days (shaded: 2–10 days); clearing the leaked dendritic proteins costs about 940 ATP per second; the two curves cross at about day 8.](./plots/ais-energy.py)

The significance of these numbers lies in comparison, not in absolute values: even if the parameters are off by several-fold, the investments in the two lines of defense remain of the same order of magnitude, and failure of either line would gradually dissolve polarity. Compared with the total energy consumption of the neuron they are both small: a rodent cortical neuron firing at an average of 4 Hz consumes about $3\times10^9$ ATP per second (Attwell and Laughlin, 2001), mainly to restore ion gradients. Polarity is nevertheless sensitive to energy crisis, because clearance depends on ATP-driven membrane trafficking, and the $\ce{Ca^2+}$ raised in ischemia activates calpain, which cuts ankyrin-G and βIV-spectrin directly and disassembles the AIS (Schafer et al., 2009).

## 5.3. Dendrites and Synaptic Integration

### 5.3.1. Attenuation in Passive Dendrites

A cortical pyramidal cell receives about $10^4$ synapses and a spinal motor neuron $10^4$–$10^5$. The depolarization that a single excitatory synapse causes at the cell body is usually only $0.1$–$1\,\mathrm{mV}$, whereas $10$–$20\,\mathrm{mV}$ is needed to go from **resting potential** to threshold: a single synapse almost never causes firing alone, and the output depends on how many inputs are added.

Dendrites are approximately passive cables (the **cable equation**, [7.6.30](/7.6.30#sec-30.5)). As synaptic current flows along the dendrite toward the cell body, part of it leaks out across the membrane, so that:

1. The potential decays with distance, at steady state as $\mathrm{e}^{-x/\lambda}$ (the **length constant** $\lambda$ is usually several hundred micrometers);
2. The farther the origin, the smaller, slower to rise and longer-lasting the potential on arrival at the cell body (low-pass filtering by the cable);
3. Synapses near the cell body contribute most to the somatic potential, and inhibitory synapses lie mostly on the cell body and proximal dendrites, exactly where they control the final output;
4. Excitation and inhibition in the dendrite add as currents and cancel one another.

Passivity is only a first approximation. Many dendrites have **voltage-gated channels**: action potentials propagate back from the AIS into the dendrites (back-propagating action potentials), and distal dendrites can produce local $\ce{Na+}$, $\ce{Ca^2+}$ or NMDA spikes. These active properties can compensate for the attenuation of distal inputs and let a branch perform local nonlinear computation.

### 5.3.2. Spatial and Temporal Summation

**Definition 5.3.1 (Spatial and Temporal Summation)** The addition at the cell body of postsynaptic potentials produced at the same time or nearly the same time by synapses at different sites is called **spatial summation**; the addition of postsynaptic potentials produced successively by the same synapse, before the earlier one has decayed, is called **temporal summation**.

The time course of a postsynaptic potential is determined by the membrane **time constant** $\tau_{\mathrm{m}} = R_{\mathrm{m}}c_{\mathrm{m}}$ (about $10$–$20\,\mathrm{ms}$ in central neurons), and a single postsynaptic potential lasts about $15\,\mathrm{ms}$; the higher the input frequency, the more marked the temporal summation. A common phenomenological description is the α function

$$
V(t) = A\,\frac{t}{\tau}\,\mathrm{e}^{1 - t/\tau}\quad(t \ge 0), \tag{5.2}
$$

which reaches its peak $A$ at $t = \tau$; in the linear approximation the effect of several inputs is the superposition of their α functions. Summation has three outcomes: threshold is crossed and an action potential is triggered at the AIS; threshold is not reached but the membrane potential is brought closer to threshold, so that the next input fires the cell more easily, called facilitation; or excitation and inhibition cancel.

![Summation of postsynaptic potentials (phenomenological model of Eq. (5.2): resting potential $-65\,\mathrm{mV}$, threshold $-50\,\mathrm{mV}$, $\tau = 3\,\mathrm{ms}$). A: temporal summation. The same input (a group of synchronous synapses, $5\,\mathrm{mV}$ at the cell body) arrives three times at intervals of $20\,\mathrm{ms}$, each decaying without adding; at intervals of $4\,\mathrm{ms}$ they add successively and approach threshold. B: spatial summation and attenuation. Inputs located at electrotonic distances $x/\lambda = 0.2$, $0.8$ and $1.6$ reach the cell body with amplitudes reduced as $\mathrm{e}^{-x/\lambda}$ and slower time courses (dashed); their sum (solid) is dominated by the proximal input. C: a suprathreshold group of EPSPs is canceled by an IPSP arriving slightly later, and the sum remains below threshold.](./plots/psp-summation.py)

### 5.3.3. Diameter Laws of Dendritic Branches

Why do dendrites branch with such calibers? For a semi-infinite passive cylinder the input conductance is $G_\infty = 1/(r_{\mathrm{i}}\lambda)$; substituting $r_{\mathrm{i}} = 4R_{\mathrm{i}}/(\pi d^2)$ and $\lambda = \sqrt{dR_{\mathrm{m}}/(4R_{\mathrm{i}})}$ gives

$$
G_\infty = \frac{\pi}{2\sqrt{R_{\mathrm{m}}R_{\mathrm{i}}}}\,d^{3/2}. \tag{5.3}
$$

At a branch point, if the input conductance of the parent branch equals the sum of those of the two daughter branches, current flows as through a uniform cylinder without reflection.

**Proposition 5.3.1 (Rall's 3/2 Law)** The condition for impedance matching at a branch point of a passive dendrite with uniform membrane properties is

$$
d_{\mathrm{m}}^{3/2} = d_1^{3/2} + d_2^{3/2}, \tag{5.4}
$$

and a whole dendritic tree that satisfies it (with all terminals at the same electrotonic distance) is electrically equivalent to one cylinder (Rall's equivalent cylinder).

Rall's measurements on cat spinal motor neurons roughly agreed with Eq. (5.4). But dendrites are not merely cables; they must also be built and continually supplied with material from the cell body. Two other classical rules of branching can be written in the same form $d_{\mathrm{m}}^p = d_1^p + d_2^p$: $p = 3$ is **Murray's law**, which minimizes the sum of transport resistance along the branches and the maintenance cost of the conduits (originally for blood vessels); $p = 2$ is Da Vinci's conservation of cross-sectional area, related to the "pipe model" of plants. For a symmetric bifurcation the ratio of daughter to parent diameter is $2^{-1/p}$, and the three rules give 0.63, 0.71 and 0.79.

Recent high-resolution measurements show that the exponent $p$ of dendrites is scattered between $3/2$ and 3, often close to 2. Liao, Liang and Howard (2021) proposed a correction: terminal branches have a minimum diameter $d_0$ set by their internal microtubules and other structures,

$$
d_{\mathrm{m}}^2 + d_0^2 = d_1^2 + d_2^2, \tag{5.5}
$$

which approaches Da Vinci's law in thick branches and keeps the diameter from becoming thinner in thin branches. These rules show that dendritic form is a compromise among electrical matching, construction and transport costs; the electrical shortcomings are compensated by molecules: the neck of a dendritic spine separates the local electrical and chemical microdomain of the spine head from the dendritic shaft, NMDA receptors and voltage-gated channels give local amplification of distal inputs, and GABAergic inputs locally lower the weight of certain branches.

![Diameter rule at dendritic bifurcations $d_{\mathrm{m}}^p = d_1^p + d_2^p$. A: ratio of daughter to parent diameter for symmetric bifurcation, $2^{-1/p}$: Rall's law ($p = 3/2$, impedance matching of a passive cable) 0.63, Da Vinci's law ($p = 2$, conservation of cross-sectional area) 0.71, Murray's law ($p = 3$, minimal transport cost) 0.79; the shading is the range measured in real dendrites. B: diameters of successive branch orders when a main dendrite of diameter $4\,\mu\mathrm{m}$ bifurcates symmetrically again and again. The rule of Liao et al. (2021) (Eq. (5.5)) adds a minimum terminal diameter $d_0$ (taken here as $0.4\,\mu\mathrm{m}$, for illustration only), and the branches approach $d_0$ without becoming thinner.](./plots/branching-rules.py)

## 5.4. Synaptic Transmission

### 5.4.1. Chemical and Electrical Synapses

**Definition 5.4.1 (Chemical Synapse)** A **chemical synapse** is a junction in which the presynaptic terminal passes the signal to the postsynaptic cell by releasing neurotransmitter: the presynaptic action potential causes $\ce{Ca^2+}$ influx, which triggers synaptic vesicles to release transmitter; the transmitter diffuses across the synaptic cleft of $20$–$40\,\mathrm{nm}$ and binds receptors in the postsynaptic membrane, changing the potential or metabolism of the postsynaptic cell (an electrical–chemical–electrical conversion).

**Definition 5.4.2 (Electrical Synapse)** An **electrical synapse** is a junction between two cells formed by gap junctions: the membranes of the two cells are only $2$–$4\,\mathrm{nm}$ apart, and connexons, each made of six **connexin** subunits, dock to form a continuous channel (pore diameter about $1.5\,\mathrm{nm}$, passing ions and small molecules below about $1\,\mathrm{kDa}$), so that ionic current flows directly from one cell into the other.

| | Chemical synapse | Electrical synapse |
|---|---|---|
| Structure | Cleft $20$–$40\,\mathrm{nm}$, presynaptic vesicles and active zone, postsynaptic receptors | Gap $2$–$4\,\mathrm{nm}$, gap junction channels |
| Delay | At least $0.3$–$0.5\,\mathrm{ms}$ | Almost zero ($< 0.1\,\mathrm{ms}$) |
| Direction | Unidirectional | Mostly bidirectional, some rectifying |
| Sign | Excitatory or inhibitory, depending on the receptor | Can only transmit the depolarization or hyperpolarization itself; the postsynaptic potential is always smaller than the presynaptic |
| Amplification | One vesicle opens thousands of channels; can amplify | No amplification; attenuated by shunting through the conductance of the postsynaptic cell |
| Processing and plasticity | Can filter, amplify and inhibit; many points of plasticity | Less plasticity (can be regulated by phosphorylation and by intracellular pH and $\ce{Ca^2+}$) |
| Energy cost | Transmitter synthesis, vesicle cycling and recovery all consume ATP | Very little |
| Examples | The great majority of synapses in the human central nervous system | Inferior olive, retina, brainstem respiratory neurons, interneuron networks, between cardiac or smooth muscle cells |

Electrical synapses are fast and reliable and suit situations needing synchrony (escape reflexes, making a group of neurons fire together, coordinated contraction of cardiac muscle); the directionality, diversity of sign and adjustability of chemical synapses are the basis on which neural circuits can compute and learn. Synapses therefore serve three functions: determining the direction of signal transmission, acting as a gate that can open and close, and filtering and amplifying signals in time and space.

### 5.4.2. Transmitter Release

In the active zone of the presynaptic terminal, vesicles await release in rows beside voltage-gated $\ce{Ca^2+}$ channels (mostly N-type and P/Q-type in the central nervous system). After the action potential arrives:

1. $\ce{Ca^2+}$ channels open, and a $\ce{Ca^2+}$ nanodomain of tens to hundreds of micromoles per liter forms near the channel mouth;
2. The $\ce{Ca^2+}$ sensor synaptotagmin on the vesicle binds $\ce{Ca^2+}$ and releases the clamp on the assembled **SNARE** protein complex (synaptobrevin on the vesicle with syntaxin and SNAP-25 on the plasma membrane), and the membranes fuse within a fraction of a millisecond, an **exocytosis**;
3. The vesicle membrane is retrieved by clathrin-mediated endocytosis (or by rapid "kiss-and-run" recovery) and reloaded with transmitter.

Release is quantal: each vesicle contains several thousand transmitter molecules and is the basic unit of release; the statistics of **quantal release** and the classical experiments at the **neuromuscular junction** are in [7.14.8](/7.14.8).

**Proposition 5.4.1 (Cooperative Dependence of Release on Ca²⁺)** At the frog neuromuscular junction, the amplitude of the **end-plate potential** at low $\ce{Ca^2+}$ concentrations increases approximately as $[\ce{Ca^2+}]_{\mathrm{o}}^{4}$ (Dodge and Rahamimoff, 1967), that is, about four $\ce{Ca^2+}$ ions act cooperatively to trigger one fusion; this is consistent with the several $\ce{Ca^2+}$ binding sites of synaptotagmin.

The consequence of **cooperativity** is that release is extremely sensitive to $\ce{Ca^2+}$ influx: a 20% reduction in $\ce{Ca^2+}$ influx reduces release by about $1 - 0.8^4 \approx 59\%$. Any factor that changes $\ce{Ca^2+}$ influx (the width of the action potential, presynaptic receptors, extracellular $\ce{Ca^2+}$ and $\ce{Mg^2+}$) strongly modulates release. Several toxins act on the release machinery: the light chains of botulinum and tetanus toxins are zinc-dependent proteases that cut SNARE proteins (types A and E cut SNAP-25; types B, D, F and G and tetanus toxin cut synaptobrevin; type C cuts syntaxin and SNAP-25), preventing vesicle fusion; botulinum toxin acts on motor nerve terminals and causes flaccid paralysis, whereas tetanus toxin is transported retrogradely to inhibitory interneurons of the spinal cord and causes spastic paralysis.

**Definition 5.4.3 (Synaptic Delay)** The shortest time from the action potential in the presynaptic terminal to the onset of the postsynaptic potential is called the **synaptic delay**, about $0.3$–$0.5\,\mathrm{ms}$ at mammalian chemical synapses.

The main part of the delay is the opening of $\ce{Ca^2+}$ channels and vesicle fusion, and diffusion across the cleft takes almost no time: with $D \approx 0.3\,\mu\mathrm{m^2\,ms^{-1}}$, crossing $20\,\mathrm{nm}$ takes only $(0.02)^2/(2\times0.3)\,\mathrm{ms} \approx 0.7\,\mu\mathrm{s}$. Conversely, the central delay of a reflex pathway (the reflex time minus the conduction times in afferent and efferent fibers) divided by the delay of a single synapse gives an estimate of the number of synapses in series in the pathway: Lloyd measured in the cat spinal cord a central delay of less than $1\,\mathrm{ms}$ for the monosynaptic **stretch reflex**, while that of the **flexor reflex** is much longer, showing that the latter passes through several interneurons (Chapter 44).

### 5.4.3. Neurotransmitters and Receptors

**Definition 5.4.4 (Neurotransmitter)** A **neurotransmitter** is a chemical substance that is synthesized by a neuron and stored in presynaptic terminals, released on stimulation in a $\ce{Ca^2+}$-dependent manner, acts on postsynaptic (or presynaptic) receptors, and has a dedicated inactivation mechanism.

| Class | Transmitters | Synthesis and storage | Main actions |
|---|---|---|---|
| Choline | Acetylcholine (ACh) | Synthesized in the terminal by choline acetyltransferase; small clear vesicles | Neuromuscular junction, autonomic ganglia, parasympathetic postganglionic (such as vagal inhibition of the heart), arousal and attention in the central nervous system |
| Amines | Norepinephrine, **epinephrine**, dopamine (catecholamines), serotonin, histamine | Synthesized in the terminal; small dense-core vesicles | Sympathetic postganglionic; central modulatory systems (locus coeruleus, substantia nigra and ventral tegmental area, raphe nuclei, tuberomammillary nucleus) |
| Amino acids | Glutamate (aspartate acts more weakly); GABA, glycine | Synthesized or recycled in the terminal; small clear vesicles | Glutamate is the main excitatory transmitter of the central nervous system; GABA is the main inhibitory transmitter in the brain and glycine in the spinal cord and brainstem |
| Purines | ATP, adenosine | Stored together with other transmitters | Cotransmitter in autonomic nerves; adenosine inhibits release |
| Gases | NO (CO, $\ce{H2S}$) | Synthesized on demand, not stored, diffuse through membranes | Retrograde messenger, vasodilation |
| Neuropeptides | Hypothalamic releasing hormones (TRH, GnRH and others), pituitary peptides (ACTH, TSH and others), peptides acting in gut and brain (gastrin, cholecystokinin, substance P, VIP), opioid peptides, neuropeptide Y and others | Precursors synthesized on ribosomes in the cell body, processed in the Golgi apparatus and packed into large dense-core vesicles, then transported rapidly to the terminal | Small amounts and slow diffusion, but strong and lasting effects, often as modulators |

The difference between small-molecule transmitters and neuropeptides matters in physiology: small-molecule transmitters are synthesized locally in the terminal and vesicles can be recycled and reused quickly, supporting high-frequency transmission; neuropeptides must be replenished from the cell body, their vesicles lie farther from the active zone, and they are usually released in quantity only on high-frequency or burst firing. A neuron often releases a small-molecule transmitter and one or more neuropeptides at once (cotransmission). Dale's principle (named by Eccles) says that a neuron releases the same transmitter at all its terminals, and in the case of cotransmission this should be understood as the same set of transmitters.

Receptors fall into two classes: **ionotropic receptors** are themselves ion channels that open within a fraction of a millisecond on binding transmitter and produce fast postsynaptic potentials lasting a few milliseconds (nicotinic ACh receptors, AMPA/NMDA/kainate glutamate receptors, $\mathrm{GABA_A}$ receptors, glycine receptors, $\mathrm{5\text{-}HT_3}$ receptors, P2X receptors); **metabotropic receptors** are **G protein–coupled receptors** (muscarinic ACh receptors, adrenergic receptors, dopamine receptors, metabotropic glutamate receptors, $\mathrm{GABA_B}$ receptors, almost all neuropeptide receptors), which regulate channels directly through **G proteins** (for example the $\beta\gamma$ subunits opening GIRK potassium channels) or activate **protein kinases** through the **second messengers** cAMP, $\mathrm{IP_3}$/DAG and $\ce{Ca^2+}$ ([7.1.14](/7.1.14)), producing slow postsynaptic potentials lasting hundreds of milliseconds to minutes. Second-messenger systems make postsynaptic changes more complex and longer lasting; they can phosphorylate channels, change the number of receptors and even regulate gene expression, and are therefore an important link in **synaptic plasticity**.

### 5.4.4. Excitatory and Inhibitory Postsynaptic Potentials

**Definition 5.4.5 (Excitatory and Inhibitory Postsynaptic Potentials)** A local potential in which the transmitter depolarizes the postsynaptic membrane and brings it closer to threshold is called an **excitatory postsynaptic potential** (EPSP); a local potential that hyperpolarizes the postsynaptic membrane or stabilizes the membrane potential below threshold is called an **inhibitory postsynaptic potential** (IPSP).

The sign of a postsynaptic potential is determined not by the transmitter but by the position of the reversal potential $E_{\mathrm{rev}}$ of the channels opened relative to threshold. The synaptic current is $I = g_{\mathrm{syn}}(V - E_{\mathrm{rev}})$:

- Cation channels such as AMPA pass $\ce{Na+}$ and $\ce{K+}$ together, with $E_{\mathrm{rev}} \approx 0\,\mathrm{mV}$, far above threshold; on opening, $\ce{Na+}$ influx predominates and causes **depolarization**. Closing $\ce{K+}$ or $\ce{Cl-}$ channels that are open at rest, or increasing the number of excitatory receptors (or decreasing the number of inhibitory receptors) through second messengers, also has an excitatory effect.
- $\mathrm{GABA_A}$ and glycine receptors pass $\ce{Cl-}$; in mature neurons KCC2 holds intracellular $\ce{Cl-}$ low, $E_{\mathrm{Cl}} \approx -70\,\mathrm{mV}$, and $\ce{Cl-}$ influx causes **hyperpolarization**; $\mathrm{GABA_B}$ receptors open $\ce{K+}$ channels through G proteins, and $\ce{K+}$ efflux likewise hyperpolarizes.
- When $E_{\mathrm{Cl}}$ is close to the resting potential, opening of $\ce{Cl-}$ channels hardly changes the membrane potential but increases the membrane conductance and shunts away excitatory currents arriving at the same time; this **shunting inhibition** is discussed in [7.14.6](/7.14.6). Neurons early in development have mainly NKCC1 and high intracellular $\ce{Cl-}$, and GABA depolarizes them instead.

For a typical motor neuron, with **resting potential** $-65\,\mathrm{mV}$ and a threshold at the AIS of about $-45\,\mathrm{mV}$ (between about $-55$ and $-45\,\mathrm{mV}$ in different neurons; the phenomenological model in the figure above uses $-50\,\mathrm{mV}$, and the $-55\,\mathrm{mV}$ in the tables of Chapters 4 and 8 is the typical value for nerve fibers and skeletal muscle), the EPSP from a single presynaptic terminal is usually only $0.5$–$1\,\mathrm{mV}$, and 40–80 terminals excited at the same time or in succession must sum to an EPSP of about $20\,\mathrm{mV}$ to trigger an action potential at the AIS; a single IPSP hyperpolarizes the membrane potential by a few millivolts (for example to $-70\,\mathrm{mV}$).

Synaptic transmission must stop quickly, otherwise the next signal cannot be transmitted. Transmitter has three fates: diffusion out of the cleft; enzymatic breakdown (acetylcholinesterase hydrolyzes ACh in the cleft to choline and acetate, and choline is recovered by the terminal; organophosphate pesticides and nerve agents inhibit this enzyme); and reuptake by transporters (NET, DAT and SERT for monoamines, GAT for GABA, and glutamate taken up mainly by EAAT of astrocytes). Many drugs act on reuptake: cocaine blocks monoamine transporters and selective serotonin reuptake inhibitors are used to treat depression; reserpine inhibits the vesicular monoamine transporter, so that monoamines in the cytosol are broken down by monoamine oxidase and the transmitter in vesicles is depleted.

### 5.4.5. Factors Affecting Synaptic Transmission

- Fatigue: under sustained high-frequency stimulation, releasable presynaptic vesicles are exhausted and postsynaptic receptors desensitize, so transmission gradually weakens; it limits overexcitation of neurons (Chapter 6).
- pH: **alkalosis** raises the excitability of neurons, and a rise of arterial pH from 7.4 to 7.8–8.0 often induces convulsions (hyperventilation can induce epileptic seizures); **acidosis** lowers excitability, and a fall of pH below 7.0 often causes coma ([7.14.25](/7.14.25)).
- Hypoxia: neurons depend almost entirely on aerobic metabolism, and consciousness is lost within seconds of interruption of cerebral blood flow.
- Drugs and poisons: caffeine, theophylline and theobromine (found in coffee, tea and cocoa respectively) block adenosine receptors and raise excitability; strychnine blocks glycine receptors, releasing spinal inhibition and causing convulsions; most anesthetics raise the threshold or enhance $\mathrm{GABA_A}$ receptors and lower excitability.
- Presynaptic modulation: autoreceptors on the terminal (such as $\alpha_2$ adrenergic receptors) and axoaxonic synapses from other neurons change $\ce{Ca^2+}$ influx and thereby the amount released; because of the fourth-power relation, this modulation is very effective.

## 5.5. Synaptic Plasticity

**Definition 5.5.1 (Synaptic Plasticity)** The property that the efficacy of synaptic transmission is strengthened or weakened according to prior activity is called **synaptic plasticity**; by duration it is divided into short-term (milliseconds to minutes) and long-term (hours or longer).

### 5.5.1. Short-Term Plasticity

- Paired-pulse facilitation: for two stimuli tens of milliseconds apart, the postsynaptic potential of the second is larger. The residual $\ce{Ca^2+}$ left by the first stimulus adds to the influx of the second and, through the fourth-power relation, markedly increases release.
- Depression: at synapses with high release probability, continued stimulation exhausts the releasable vesicles and transmission weakens; replenishment takes seconds. The balance between facilitation and depression determines whether a synapse is a "high-pass" or a "low-pass" filter.
- Posttetanic potentiation: after a train of high-frequency (tetanic) stimulation, synaptic transmission is enhanced for tens of seconds to minutes, owing to $\ce{Ca^2+}$ accumulated in the terminal and mobilization of vesicles.
- **Habituation** and sensitization: the gill-withdrawal reflex of *Aplysia* weakens after repeated light touch (habituation), through reduced release at the synapse from sensory to motor neuron; a noxious stimulus to the tail strengthens it (sensitization), through serotonin increasing presynaptic release via cAMP and PKA (Kandel et al.). Repeated sensitization training converts it into long-term memory that depends on gene expression and growth of new synapses.

### 5.5.2. Long-Term Potentiation and Long-Term Depression

**Definition 5.5.2 (Long-Term Potentiation and Long-Term Depression)** A lasting increase of the efficacy of transmission at a group of synapses for hours to weeks after a brief high-frequency stimulation (or paired presynaptic and postsynaptic activity) is called **long-term potentiation** (LTP); a lasting decrease after sustained low-frequency stimulation (such as $1\,\mathrm{Hz}$ for 15 minutes) is called **long-term depression** (LTD).

Bliss and Lømo (1973) first reported LTP in the dentate gyrus of the rabbit hippocampus. LTP in hippocampal area CA1 has three properties:

1. Cooperativity: enough afferent fibers must be excited at the same time;
2. Associativity: when a weak input is paired with a strong input on the same cell, the weak input is also strengthened;
3. Input specificity: only the activated synapses are strengthened.

All three come from the coincidence detection of the NMDA receptor: it needs glutamate binding (presynaptic activity) and at the same time postsynaptic depolarization to relieve the $\ce{Mg^2+}$ block (postsynaptic activity), and on opening lets $\ce{Ca^2+}$ enter the dendritic spine ([7.6.30](/7.6.30#sec-30.3.4)). A strong, fast rise of $\ce{Ca^2+}$ activates CaMKII, inserting more AMPA receptors into the postsynaptic membrane and causing LTP; a weak, prolonged rise of $\ce{Ca^2+}$ activates phosphatases, causing endocytosis of AMPA receptors and LTD. Early LTP needs only modification of existing proteins; late LTP, lasting hours or more, needs new transcription and protein synthesis and is accompanied by enlargement of the dendritic spine. LTD caused in the cerebellum by simultaneous excitation of parallel fibers and **climbing fibers** is a candidate mechanism of motor learning (Chapter 45).

The process by which the nervous system stores information is called memory, and changes of synaptic efficacy are held to be its main structural basis: in vivo, learning can cause synaptic strengthening that resembles LTP and mutually "occludes" it; blocking NMDA receptors impairs spatial learning; and activating or inhibiting specific synaptic pathways by **optogenetics** can artificially create or erase conditioned memories. But how a particular memory is distributed among synapses and groups of neurons remains an open question ([7.14.46](/7.14.46)). The mathematical form of plasticity rules and learning theory belong to computational neuroscience ([7.16](/7.16)).

## 5.6. Evolution and Comparison

Polarity of invertebrate neurons. The neurons of insects, crustaceans and molluscs are mostly unipolar: the cell body lies in the cortex at the periphery of the ganglion and sends one process into the central neuropil, where it gives off branches that both receive input and bear output synapses, and then extends as the axon. Integration takes place in the neurite rather than in the cell body, and receiving and output regions can be interleaved in space. The vertebrate neuron with clearly separated cell body, dendrites and axon is only one scheme for separating input from output. Some chemical synapses of cnidarians (such as scyphozoan jellyfish) have vesicles on both sides and can transmit in both directions.

Two protein families of electrical synapses. Vertebrates and tunicates build gap junctions from **connexin** (no connexin genes have been found in the amphioxus genome, so the family may have arisen only in the common ancestor of these two groups), whereas protostomes, cnidarians and ctenophores use innexin, which has no sequence homology to it; vertebrate pannexin is homologous to innexin but forms channels mainly in single membranes (for example releasing ATP) and rarely forms gap junctions. Both families form channels from subunits with four transmembrane helices, an example of **convergent evolution**. Escape reflexes often depend on electrical synapses to gain time: the synapse from the lateral giant fiber to the motor giant fiber of the crayfish is a rectifying electrical synapse, and the Mauthner cell of the goldfish also receives mixed input from electrical and chemical synapses.

Nerve nets of cnidarians and the peptidergic nervous system. The neurons of *Hydra* and the sea anemone *Nematostella* are arranged in the body wall as a diffuse nerve net, and medusae also have a concentrated nerve ring at the bell margin. Their neurons use neuropeptides as the main signals (peptide families such as RFamide and GLWamide), suggesting that early neural transmission may have been mainly peptidergic and that small-molecule fast-transmitter systems were a later expansion. The placozoan *Trichoplax*, which has no neurons, also has cells that secrete many peptides, and peptide signals coordinate its ciliary movement and feeding; sponges have no neurons or synapses but express many postsynaptic scaffold proteins, and their "neuroid cells" extend processes to contact choanocytes (Musser et al., 2021). Components of the release machinery such as SNARE and synaptotagmin existed before animals appeared.

The dispute over the nervous system of ctenophores. The evidence has three aspects:

1. Phylogeny: analyses based on conserved chromosomal linkage support ctenophores (rather than sponges) as the **sister group** of all other animals (Schultz et al., 2023), but this conclusion is still disputed.
2. Molecular composition: the ctenophore genome lacks many transmitter-synthesizing enzymes and receptors commonly used in the nervous systems of other animals, and glutamate and many neuropeptides may serve as signals (Moroz et al., 2014).
3. Structure: volume electron microscopy reconstruction shows that the neurons of the subepithelial nerve net of the ctenophore *Mnemiopsis* are fused into a syncytium by continuous plasma membrane, with no chemical synapses separating them (Burkhardt et al., 2023), an exception to the neuron doctrine in animals; neurons elsewhere, however, have chemical synapses.

If ctenophores branched off first and their nervous system is not homologous to that of other animals, neurons arose independently at least twice; the other interpretation is that the common ancestor of animals already had neurons and sponges and placozoans lost them later. The present evidence cannot decide between the two.

Transmitters at the **neuromuscular junction**. The NMJ of vertebrate skeletal muscle uses ACh and nicotinic receptors, whereas the excitatory NMJ of insects and crustaceans uses glutamate (so the NMJ of the *Drosophila* larva has become a model for studying glutamatergic synapses), with GABA used by inhibitory motor neurons; the body-wall muscles of *Caenorhabditis elegans* are doubly innervated by cholinergic and GABAergic motor neurons, and the muscle cells themselves extend "muscle arms" to the nerve cord to receive synapses. The independent adoption of the same molecule (ACh, glutamate) for the same kind of synapse in different groups shows that there is no fixed correspondence between transmitter and function.

Giant synapses as experimental preparations. The giant synapse in the stellate ganglion of the squid allows electrodes to be inserted in presynaptic and postsynaptic elements at the same time, and Katz, Miledi and Llinás used it to show that transmitter release is triggered by presynaptic $\ce{Ca^2+}$ influx and that there is a delay of about $0.2\,\mathrm{ms}$ between the $\ce{Ca^2+}$ current and release; the calyx of Held in the mammalian auditory brainstem has played the same role since the 1990s.

## Summary

- The neuron doctrine: the nervous system consists of discrete neurons, with signals flowing in one direction within the cell and transmitted between cells at synapses; electrical synapses and the syncytial nerve net of ctenophores are exceptions. The human brain has about $8.6\times10^{10}$ neurons and about as many non-neuronal cells.
- Polarity is established by the orientation of microtubules (plus ends outward in the axon, mixed in dendrites) and directed transport by motors; the ankyrin-G skeleton of the AIS lowers the effective diffusion coefficient of membrane proteins tens of fold, lengthening $L^2/2D$ from about 2 hours to days (Definition 5.2.1, Formula 5.2.1), and proteins that escape are endocytosed and degraded. The ATP costs of the two lines of defense are both of the order of hundreds to a thousand ATP per second (Example 5.2.1).
- A single EPSP is only $0.1$–$1\,\mathrm{mV}$, and firing depends on spatial and temporal summation (Definition 5.3.1); passive dendrites attenuate and slow distal inputs, and active channels partly compensate. Diameter laws at branch points $d_{\mathrm{m}}^p = d_1^p + d_2^p$: Rall's $p = 3/2$ (impedance matching, Proposition 5.3.1), Da Vinci's $p = 2$, Murray's $p = 3$, with measurements in between.
- The comparison of chemical and electrical synapses is in the table of 5.4.1. Release depends cooperatively on $\ce{Ca^2+}$ to about the fourth power (Proposition 5.4.1), and the synaptic delay is about $0.5\,\mathrm{ms}$ (Definition 5.4.3), which can be used to estimate the number of synapses in a reflex pathway.
- Transmitters fall into small molecules, neuropeptides and gases; receptors into ionotropic (fast) and metabotropic (slow). The sign of a postsynaptic potential is determined by the reversal potential relative to threshold (Definition 5.4.5); transmitters are terminated by diffusion, enzymatic breakdown and reuptake.
- Synaptic plasticity (Definition 5.5.1): paired-pulse facilitation, depression, posttetanic potentiation, habituation and sensitization are short-term; LTP and LTD (Definition 5.5.2) depend on coincidence detection by the NMDA receptor and on the amplitude and time course of $\ce{Ca^2+}$.
- Comparison: invertebrate neurons are mostly unipolar; the connexin and innexin families form gap junctions independently; cnidarians rely mainly on neuropeptides; whether the ctenophore nervous system arose independently remains unresolved; NMJ transmitters differ among groups.

## Questions

1. The threshold of a motor neuron is $20\,\mathrm{mV}$ above the resting potential, the EPSP from a single Ia afferent terminal is about $0.5\,\mathrm{mV}$, and postsynaptic potentials last about $15\,\mathrm{ms}$. Why is it called a "majority vote" device? What happens if all the inputs arrive scattered in time?

   **Answer** By linear superposition, the EPSPs of about $20/0.5 = 40$ terminals must overlap within about one membrane time constant to bring the membrane potential across threshold, so the neuron fires only when a considerable fraction of its inputs are active together. If the inputs are scattered in time (the interval between neighboring inputs far greater than $15\,\mathrm{ms}$), each EPSP decays before the next arrives and the cell never fires, however many inputs there are in total; in fact the spatial distribution also makes distal EPSPs smaller, and inhibitory inputs raise the number needed still further.

2. Use Eq. (5.1) to estimate: if the barrier of the AIS reduced $D$ only 5-fold instead of 50-fold, what would the power of the clearance system in Example 5.2.1 become? What does this show?

   **Answer** The leak flux $J \propto D$; with $D$ 10 times larger the flux becomes about $0.31\,\mathrm{s^{-1}}$, the clearance power per protein about $470\,\mathrm{ATP\,s^{-1}}$ and for 20 proteins about $9400\,\mathrm{ATP\,s^{-1}}$, 10 times the original and far above the maintenance power of the skeleton. The weaker the barrier, the heavier the burden of clearance; the two lines of defense are complementary: a skeleton built once buys a large reduction in the continuing expense of clearance.

3. Why is the postsynaptic potential at an electrical synapse always smaller than the presynaptic potential, whereas a chemical synapse can amplify the signal of a small presynaptic terminal into a significant potential in a large cell?

   **Answer** An electrical synapse is a resistance: current from the presynaptic cell flows through the gap junction into the postsynaptic cell and leaks out again through the membrane conductance of the postsynaptic cell, the two forming a voltage divider, so the postsynaptic potential $=$ presynaptic potential $\times$ coupling coefficient (less than 1); the larger and more conductive the postsynaptic cell, the weaker the coupling. At a chemical synapse the presynaptic side need only supply the depolarization that triggers $\ce{Ca^2+}$ influx, and the energy comes from the ion gradients across the postsynaptic membrane: the several thousand transmitter molecules of one vesicle open thousands of channels, and the size of the current is independent of the electrical properties of the presynaptic terminal, so it can drive a large postsynaptic cell.

4. If extracellular $\ce{Ca^2+}$ falls from $2\,\mathrm{mM}$ to $1.5\,\mathrm{mM}$ (and is far below saturation), by Proposition 5.4.1 release becomes about what fraction of the original? Why does hypocalcemia instead make peripheral nerves and muscles overexcitable (tetany)?

   **Answer** $(1.5/2)^4 \approx 0.32$, so release falls to about one third. The increased excitability in hypocalcemia comes from another mechanism: extracellular $\ce{Ca^2+}$ screens the negative surface charge of the membrane, and when it falls the activation curve of voltage-gated $\ce{Na+}$ channels shifts to more negative potentials, the threshold falls, and axons fire spontaneously (see Chapter 36); for peripheral nerves and muscles this effect outweighs the reduction in transmitter release.

5. (Open question) Some argue that since electrical synapses are faster and cheaper in energy, the nervous system should use electrical synapses as far as possible. Refute this view from the content of this chapter.

   **Answer** Key points: electrical synapses cannot change the sign of the signal (except through an intermediate inhibitory neuron), cannot amplify, and the postsynaptic potential is always attenuated by the conductance of the postsynaptic cell, so they cannot pass the signal of a small cell reliably to a large one; they are bidirectional and cannot guarantee the direction of signal flow; they have few points of regulation and can hardly support activity-dependent plasticity and learning. The delay (about $0.5\,\mathrm{ms}$) and energy cost of chemical synapses buy directionality, diversity of sign and gain, and long-term plasticity, which are exactly the conditions for circuits to compute (Chapter 6) and to remember. Where speed and synchrony are needed and computation is not (escape reflexes, cardiac muscle, certain oscillatory networks), evolution has indeed chosen electrical synapses.
