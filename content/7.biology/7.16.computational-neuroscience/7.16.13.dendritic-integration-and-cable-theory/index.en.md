---
title: Dendritic Integration and Cable Theory
description: "How dendrites combine synaptic inputs: the layout of synapses on dendritic trees; steady and transient solutions of the cable equation, boundary conditions, input conductance and electrotonic length; Rall's equivalent cylinder, time-constant peeling and the shape index; the attenuation of conductances and why inhibition on the path to the soma is most effective; multicompartment models; back-propagating action potentials, Ca²⁺ and NMDA spikes, BAC firing and the two-layer model; diffusion and compartmentalization of chemical signals."
---

A cortical pyramidal neuron receives some ten thousand synapses, almost all of them on dendrites that extend hundreds of micrometers to a millimeter from the soma. Whether an input contributes to the output depends on where it lands, when it arrives relative to others, and which voltage-gated channels the dendrite contains on the way. This chapter treats the dendrite first as a passive cable, following Wilfrid Rall, who founded the theory between 1957 and 1970, and then as an active, compartmentalized structure that can perform local nonlinear operations, so that a single neuron behaves more like a small network than like a point. The cable equation itself is derived in [7.6.30](/7.6.30#sec-30.5) and the elementary facts about attenuation, summation and the diameter rules of branches are in [7.14.5](/7.14.5#sec-5.3); here we solve the equation for dendrites and draw its consequences. The passive membrane parameters are those of [7.16.4](/7.16.4), the synaptic conductances those of [7.16.12](/7.16.12), and the dendritic $\ce{Ca^2+}$ signals of this chapter are the triggers of long-term plasticity in [7.16.14](/7.16.14).

## 13.1. Dendritic Trees and the Placement of Synapses

Dendrites are thin (from about $5\,\mu\mathrm{m}$ near the soma to $0.5\,\mu\mathrm{m}$ at the tips), branched and, in many neurons, covered with spines, protrusions of about $1\,\mu\mathrm{m}$ consisting of a head of $0.01$–$0.5\,\mu\mathrm{m^3}$ and a neck of $0.1\,\mu\mathrm{m}$ diameter. Nearly every spine carries one excitatory synapse, and the volume of its head scales with the number of AMPA receptors in its postsynaptic density ([7.16.9](/7.16.9#sec-9.2.3)). A layer 5 pyramidal cell of the rat neocortex has about $10^4$ spines on roughly $10\,\mathrm{mm}$ of dendrite; a cerebellar Purkinje cell has $10^5$ spines in a single planar tree.

Synapses are not distributed at random. Excitatory inputs from different sources are segregated by dendritic domain, and the classes of inhibitory interneurons target different compartments:

| Neuron | Domain | Main input |
|---|---|---|
| CA1 pyramidal cell | Basal dendrites and proximal apical dendrite (strata oriens and radiatum) | Schaffer collaterals from CA3 |
| | Distal apical tuft (stratum lacunosum-moleculare) | Perforant path from entorhinal cortex layer III |
| Layer 5 pyramidal cell | Basal and oblique dendrites | Local and feedforward cortical input |
| | Apical tuft in layer 1 | Feedback from higher cortical areas, higher-order thalamus |
| Inhibitory targets | Soma and proximal dendrites | Parvalbumin-expressing basket cells |
| | Axon initial segment | Chandelier cells |
| | Distal dendrites and tuft | Somatostatin-expressing (Martinotti, O-LM) cells |

This layout means that the integration of inputs from different sources is a question about dendrites. Whether the feedback arriving in layer 1, more than a millimeter from the soma of a large pyramidal cell, can influence its output at all is the problem with which the active properties of 13.6 are concerned.

## 13.2. Solutions of the Cable Equation

### 13.2.1. Electrotonic Units and the Steady State

For a passive cylinder of diameter $d$, specific membrane resistance $R_{\mathrm{m}}$, axial resistivity $R_{\mathrm{i}}$ and capacitance $c_{\mathrm{m}}$, the deviation $V(x, t)$ of the potential from rest obeys the **cable equation** $\lambda^2\partial_x^2V = \tau_{\mathrm{m}}\partial_tV + V$ ([Theorem 30.5.1](/7.6.30#thm-30.5.1)), with **length constant** $\lambda = \sqrt{dR_{\mathrm{m}}/(4R_{\mathrm{i}})}$ and $\tau_{\mathrm{m}} = R_{\mathrm{m}}c_{\mathrm{m}}$. In the dimensionless electrotonic coordinates $X = x/\lambda$ and $T = t/\tau_{\mathrm{m}}$ it becomes
$$
\frac{\partial V}{\partial T} = \frac{\partial^2V}{\partial X^2} - V. \tag{13.1}
$$
Because $\lambda \propto \sqrt d$, a branch of a quarter of the diameter has half the length constant; electrotonically, thin dendrites are long.

**Definition 13.2.1 (Electrotonic Length)** The **electrotonic length** of a cable segment of physical length $\ell$ is $L = \ell/\lambda$; the electrotonic distance between two points of a dendrite is the sum of $\Delta x/\lambda$ over the segments between them.

In the steady state Eq. (13.1) reduces to $V'' = V$, with general solution $V(X) = c_1\mathrm{e}^{-X} + c_2\mathrm{e}^{X}$, and the boundary condition at the far end selects the solution. For a voltage $V_0$ imposed at $X = 0$:

| Far end at $X = L$ | Condition | Steady solution | Input conductance |
|---|---|---|---|
| Semi-infinite cable | $V \to 0$ | $V_0\,\mathrm{e}^{-X}$ | $G_\infty$ |
| Sealed end (no axial current) | $\partial_XV = 0$ | $V_0\dfrac{\cosh(L - X)}{\cosh L}$ | $G_\infty\tanh L$ |
| Killed end (short circuit) | $V = 0$ | $V_0\dfrac{\sinh(L - X)}{\sinh L}$ | $G_\infty\coth L$ |

Here $G_\infty = 1/(r_{\mathrm{i}}\lambda) = \pi d^{3/2}/(2\sqrt{R_{\mathrm{m}}R_{\mathrm{i}}})$ is the input conductance of a semi-infinite cable, the quantity on which **Rall's 3/2 power rule** is based ([Proposition 5.3.1](/7.14.5#prop-5.3.1)). A sealed end, the natural termination of a dendritic tip, reflects current back and keeps the voltage higher than in an infinite cable: with $L = 1$ the far end still has $1/\cosh 1 = 65\%$ of $V_0$, against $37\%$ at the same distance in an infinite cable. Dendrites of most neurons have $L$ between about $0.3$ and $1.5$, so in the steady state they are fairly compact; it is the transient signals that are attenuated strongly.

**Example 13.2.1** A basal dendrite of a pyramidal cell has $d = 1\,\mu\mathrm{m}$, $R_{\mathrm{m}} = 20\,\mathrm{k\Omega\,cm^2}$ and $R_{\mathrm{i}} = 150\,\Omega\,\mathrm{cm}$. Then $\lambda = \sqrt{(10^{-4}\,\mathrm{cm})(2\times10^4\,\Omega\,\mathrm{cm^2})/(600\,\Omega\,\mathrm{cm})} = 0.058\,\mathrm{cm} = 580\,\mu\mathrm{m}$, and a $200\,\mu\mathrm{m}$ branch has $L = 0.35$; a steady voltage at its tip reaches the branch point attenuated by only $1/\cosh 0.35 = 0.94$ if current flows from the base. The opposite direction is different: current injected at the sealed tip must charge the rest of the tree, whose input conductance is much larger than that of the thin branch, so the voltage at the tip is large and that at the base much smaller (13.3.3).

:::

### 13.2.2. Transient Signals

Synaptic potentials last a few milliseconds, comparable to or shorter than $\tau_{\mathrm{m}}$, and for them the cable is a low-pass filter. A sinusoidal input of angular frequency $\omega$ at one end of a semi-infinite cable decays as $\exp\bigl(-X\operatorname{Re}\sqrt{1 + \mathrm{i}\omega\tau_{\mathrm{m}}}\bigr)$, which follows from substituting $V = \hat V(X)\mathrm{e}^{\mathrm{i}\omega t}$ in Eq. (13.1). For $\tau_{\mathrm{m}} = 20\,\mathrm{ms}$ the effective length constant is $\lambda/1.14$ at $10\,\mathrm{Hz}$ and $\lambda/2.61$ at $100\,\mathrm{Hz}$. An EPSP with a rise time of about a millisecond, whose energy lies mostly above $50\,\mathrm{Hz}$, is therefore attenuated far more than a steady voltage (at $X = 1$ the peak falls to about $15\%$, compared with $37\%$ in the steady state), it arrives later, and it is broader. This was the reason that early electrophysiologists, recording only from somata, underestimated distal inputs.

![Passive spread along a cable in electrotonic units. A: steady-state profiles for a voltage imposed at $X = 0$: semi-infinite cable, sealed ends at $L = 1$ and $L = 2$, and a killed end at $L = 1$ (table in 13.2.1). B: a fast EPSP-like transient (alpha-function current with a $1\,\mathrm{ms}$ time constant, $\tau_{\mathrm{m}} = 20\,\mathrm{ms}$) at $X = 0$ and at $X = 0.5$, $1$ and $2$ along a long cable, each normalized to the peak at $X = 0$: attenuated, delayed and broadened. C: peak attenuation of the transient against distance (dots), compared with the steady-state attenuation $\mathrm{e}^{-X}$ (dashed) and the attenuation of sinusoids at $10$ and $100\,\mathrm{Hz}$ (lines): fast signals attenuate more.](./plots/cable-attenuation.py)

## 13.3. Rall's Theory of Dendritic Trees

### 13.3.1. The Equivalent Cylinder

Rall's central insight was that, under conditions that real trees approximately satisfy, the complex geometry of a dendritic tree can be collapsed into a single cable.

**Definition 13.3.1 (Equivalent Cylinder)** The **equivalent cylinder** of a passive dendritic tree is a single cylinder, with the diameter of the trunk and a sealed end at electrotonic length $L$, in which the voltage as a function of electrotonic distance from the soma is the same as in the tree.

**Theorem 13.3.1 (Rall's Equivalence)** Suppose that a passive dendritic tree has uniform $R_{\mathrm{m}}$ and $R_{\mathrm{i}}$, that at every branch point the diameters satisfy $d_{\mathrm{p}}^{3/2} = \sum_k d_k^{3/2}$, and that all terminal branches end with sealed ends at the same electrotonic distance $L$ from the soma. Then, for inputs at the soma, or distributed equally over all branches at the same electrotonic distance, the voltage in the tree as a function of electrotonic distance is the same as in a single sealed cylinder of electrotonic length $L$ with the diameter of the trunk: the tree has an equivalent cylinder (Definition 13.3.1).

**Proof** (Sketch.) In electrotonic coordinates each branch obeys Eq. (13.1). At a branch point the voltage is continuous and the axial currents add; since the axial current of a cylinder is $-G_\infty(d)\,\partial_XV$ with $G_\infty \propto d^{3/2}$, the 3/2 condition makes the sum of the daughter currents equal to the current of a continuation of the parent, provided the daughters carry the same $V(X)$. Symmetric inputs and equal terminal distances make all daughters carry the same $V(X)$, and by uniqueness of the solution of the cable equation with given boundary and initial conditions the tree and the cylinder have the same solution. $\square$

The theorem made dendrites tractable: a motor neuron or pyramidal cell could be characterized by three numbers, the soma, $L$ and $\tau_{\mathrm{m}}$, and the effect of any symmetric input computed analytically. Its conditions are approximations. Measured branching exponents are scattered between $3/2$ and $3$ ([7.14.5](/7.14.5#sec-5.3.3)), terminals end at different distances, and synaptic input is not symmetric; for an input on a single branch the equivalent cylinder no longer applies, and the asymmetry of attenuation (13.3.3) appears.

### 13.3.2. Estimating the Electrotonic Length

For a finite sealed cylinder coupled to an isopotential soma, the voltage transient after a brief current pulse is a sum of exponentials,
$$
V(T) = \sum_{n \ge 0} C_n\,\mathrm{e}^{-t/\tau_n}, \qquad \tau_n = \frac{\tau_0}{1 + (\alpha_n/L)^2}, \tag{13.2}
$$
with $\tau_0 = \tau_{\mathrm{m}}$, obtained by separating variables in Eq. (13.1). For a cylinder with sealed ends at both ends (a soma that is small compared with the dendrites), $\alpha_n = n\pi$; with a large soma, $\alpha_n$ solves a transcendental equation and lies between $(n - \tfrac12)\pi$ and $n\pi$.

**Proposition 13.3.1 (Rall's Formula for $L$)** For a cylinder with sealed ends, the ratio of the two slowest time constants of the transient determines the electrotonic length:
$$
L = \frac{\pi}{\sqrt{\tau_0/\tau_1 - 1}}. \tag{13.3}
$$

**Proof** Set $n = 1$ and $\alpha_1 = \pi$ in Eq. (13.2): $\tau_0/\tau_1 = 1 + \pi^2/L^2$, and solve for $L$. $\square$

The time constants are measured by "peeling": on a semilogarithmic plot the late part of the transient is a straight line with slope $-1/\tau_0$; subtracting it reveals $\tau_1$. Applied to cat motor neurons, Eq. (13.3) gave $L \approx 1$–$1.5$, the first quantitative evidence that dendrites are electrotonically compact enough for distal synapses to matter. The faster components $\tau_n$, $n \ge 1$, describe the equalization of charge between soma and dendrites; they are why a current step charges the soma of a neuron with dendrites faster than a single exponential with $\tau_{\mathrm{m}}$ would. The method assumes uniform $R_{\mathrm{m}}$ and a good electrode seal; leak through the electrode and nonuniform membranes have led to underestimates of $\tau_{\mathrm{m}}$ in older measurements, and modern estimates combine morphological reconstruction with dendritic recordings.

### 13.3.3. Distance, Shape and Direction

Three consequences of cable theory shape how a neuron reads its inputs.

1. *Shape index.* A synapse close to the soma gives a somatic EPSP with a fast rise and a short half-width; a distal synapse gives a slow, broad one. Rall (1967) proposed to read the electrotonic location of a synapse from this pair of numbers, and plots of half-width against rise time ("shape-index plots") were used to locate the synapses of Ia afferents on motor neurons before dendritic recordings were possible.
2. *Local amplitude.* The input impedance of a thin distal branch is high, so a synaptic current produces a much larger local depolarization than at the soma (tens of millivolts for a few synchronous synapses), which brings distal dendrites into the voltage range of NMDA receptors and voltage-gated channels; at the same time the somatic EPSP is small.
3. *Asymmetry.* Voltage attenuation from a distal tip to the soma is much stronger than from the soma to the tip, because the tip feeds a large conductance load while the soma drives a branch that ends in a sealed end. Signals of the soma, such as the **action potential**, spread into dendrites far better than dendritic signals spread toward the soma. A branch point is "transparent" for propagation from parent to daughters if the 3/2 rule holds, but propagation from a daughter into the parent and its sister always meets an impedance increase.

![EPSPs from different dendritic locations in a passive soma-plus-cable model (soma of $20\,\mu\mathrm{m}$, dendrite of $2\,\mu\mathrm{m}$ diameter and $1.5\,\mathrm{mm}$ length in 30 compartments, $R_{\mathrm{m}} = 20\,\mathrm{k\Omega\,cm^2}$, $R_{\mathrm{i}} = 100\,\Omega\,\mathrm{cm}$, so that $\lambda = 1\,\mathrm{mm}$; alpha-function conductance of $0.3\,\mathrm{nS}$ peak at $2\,\mathrm{ms}$, $E_{\mathrm{syn}} = 0\,\mathrm{mV}$). A: somatic EPSPs for inputs at $X = 0.1$ to $1.5$: smaller, later and broader with distance. B: shape-index plot of half-width against $10$–$90\%$ rise time of the somatic EPSP, for inputs from $X = 0.05$ to $1.5$ (color): each location has its own signature. C: peak EPSP at the input site (dashed) and at the soma (solid): local depolarization grows toward the sealed end while the somatic contribution falls.](./plots/multicompartment-epsp.py)

## 13.4. Conductances and the Position of Inhibition

Synapses inject current through a conductance, and a conductance far from the soma does not merely attenuate but interacts with other inputs. The effect is clearest for **shunting inhibition** ($E_{\mathrm{inh}} = E_{\mathrm{L}}$), which produces no potential of its own and acts only by reducing the depolarization caused by excitation elsewhere (Proposition 10.4.1). Where on the tree should such an inhibitory synapse be placed to veto a given excitatory input most effectively?

Let $K_{ab}$ be the steady-state transfer impedance of a passive tree, the voltage at $a$ per unit current injected at $b$; it is symmetric, $K_{ab} = K_{ba}$, and $K_{aa}$ is the input impedance at $a$. Let an excitatory synapse at site $e$ inject a current $I_e$ (taken as fixed for small depolarizations), and a shunting conductance $g$ sit at site $i$.

**Proposition 13.4.1 (On-Path Inhibition)** The relative reduction of the steady somatic depolarization by the shunt is
$$
\frac{\Delta V_s}{V_s} = \frac{gK_{ii}}{1 + gK_{ii}}\,\rho, \qquad \rho = \frac{K_{si}K_{ie}}{K_{se}K_{ii}}. \tag{13.4}
$$
If $i$ lies on the path from $e$ to the soma $s$, then $\rho = 1$; if it lies off that path and its branch joins the path at the point $p$, then $\rho = K_{pi}^2/(K_{pp}K_{ii}) = A_{i\to p}A_{p\to i} < 1$, the product of the voltage attenuations from $i$ to $p$ and back.

**Proof** By linearity the shunt draws a current $gV_i$, and $V_i = K_{ie}I_e - K_{ii}gV_i$, so $V_i = K_{ie}I_e/(1 + gK_{ii})$. The somatic potential is $V_s = K_{se}I_e - K_{si}gV_i$, which gives the reduction $K_{si}gK_{ie}/((1 + gK_{ii})K_{se})$ relative to $K_{se}I_e$, that is Eq. (13.4). In a tree, a point $p$ on the unique path between two sites $a$ and $b$ separates them, and the voltage at $b$ produced by current at $a$ depends on that current only through $V_p$; hence $K_{ba} = K_{bp}K_{pa}/K_{pp}$. If $i$ is on the path from $e$ to $s$, take $p = i$: $K_{se}K_{ii} = K_{si}K_{ie}$ and $\rho = 1$. Otherwise $K_{si} = K_{sp}K_{pi}/K_{pp}$, $K_{ie} = K_{ip}K_{pe}/K_{pp}$ and $K_{se} = K_{sp}K_{pe}/K_{pp}$, so $\rho = K_{pi}^2/(K_{pp}K_{ii})$, and $A_{i\to p} = K_{pi}/K_{ii}$, $A_{p\to i} = K_{ip}/K_{pp}$ are both less than 1. $\square$

The proposition is the steady-state form of the "on-path" theorem of Koch, Poggio and Torre (1983) and of the result that the effective attenuation of a conductance is the product of the voltage attenuations in both directions (Koch, 1984). Inhibition anywhere between the excitatory synapse and the soma, including at the soma itself, is maximally effective; inhibition distal to the excitation, or on a sister branch, is weakened by a two-way attenuation factor.

Because the input impedance $K_{ii}$ is larger in thin distal branches, an on-path shunt placed just proximal to the excitation in the same branch can veto it with a small conductance, while sparing other branches: inhibition can act on single branches. This is one interpretation of why somatostatin-expressing interneurons target distal dendrites, where they can gate specific streams of input (for example the tuft input of 13.1) or dendritic spikes, while parvalbumin-expressing basket cells, on the soma, control the output globally.

![Where shunting inhibition is most effective (steady state, Proposition 13.4.1). A: a passive tree with soma, a $300\,\mu\mathrm{m}$ trunk of $3\,\mu\mathrm{m}$ and two $500\,\mu\mathrm{m}$ daughters satisfying the 3/2 rule; an excitatory conductance of $1\,\mathrm{nS}$ (triangle) on branch A and five possible sites of a shunting conductance (squares, soma circle). B: reduction of the somatic EPSP against the inhibitory conductance: sites on the path from the synapse to the soma (soma, trunk, proximal branch A; nearly superimposed) are most effective; the site distal to the synapse and the site on the sister branch are weaker by the attenuation factor $\rho$.](./plots/on-path-inhibition.py)

## 13.5. Multicompartment Models

Real trees violate the conditions of the equivalent cylinder, have voltage-gated channels and receive asymmetric inputs. They are simulated by dividing the tree into short compartments, each isopotential, connected by axial conductances, the spatial discretization of the cable equation (Dayan and Abbott, ch. 6).

**Formula 13.5.1 (Multicompartment Model)** For compartments $j = 1, \dots, M$ with membrane area $A_j$, the potentials obey
$$
c_{\mathrm{m}}A_j\frac{\mathrm{d}V_j}{\mathrm{d}t} = -\sum_{\mathrm{ion}}g_{\mathrm{ion},j}(V_j - E_{\mathrm{ion}}) - g_{\mathrm{syn},j}(t)(V_j - E_{\mathrm{syn}}) + \sum_{k \sim j}g_{jk}(V_k - V_j) + I_{\mathrm{ext},j}, \tag{13.5}
$$
where $k \sim j$ runs over the neighbors of $j$ and the axial conductance between two cylindrical compartments of diameters $d_j, d_k$ and lengths $\ell_j, \ell_k$ is the inverse of the resistance between their centers, $g_{jk} = 1/\bigl(2R_{\mathrm{i}}\ell_j/(\pi d_j^2) + 2R_{\mathrm{i}}\ell_k/(\pi d_k^2)\bigr)$.

The linear part of Eq. (13.5) is $C\dot{\boldsymbol{V}} = -G\boldsymbol{V} + \dots$ with a sparse, symmetric conductance matrix $G$ that has the structure of the tree. Two practical rules follow from the cable equation: compartments should be shorter than about $0.1\lambda$ at the highest frequency of interest (the "$d_\lambda$ rule" of the simulator NEURON), and implicit integration is needed, since coupling between short compartments is stiff; for a tree the implicit linear system is solved in $O(M)$ operations by Gaussian elimination ordered from the tips to the root (Hines, 1984). Detailed reconstructions with several thousand compartments and a dozen channel types reproduce dendritic recordings well, and at the other extreme two-compartment models (soma plus dendrite, Pinsky and Rinzel, 1994) capture bursting caused by dendritic $\ce{Ca^2+}$ currents. The choice depends on the question, as everywhere in modeling ([7.16.1](/7.16.1)).

## 13.6. Active Dendrites and Nonlinear Integration

### 13.6.1. Back-Propagating Action Potentials

Dendrites contain voltage-gated $\ce{Na+}$, $\ce{K+}$ and $\ce{Ca^2+}$ channels and HCN channels, at densities that vary systematically with distance. Simultaneous patch-clamp recordings from soma and apical dendrite of layer 5 pyramidal cells (Stuart and Sakmann, 1994) showed that the action potential is initiated in the axon and propagates back into the dendrites, actively supported by dendritic $\ce{Na+}$ channels but declining in amplitude and broadening with distance.

**Definition 13.6.1 (Back-Propagating Action Potential)** A **back-propagating action potential** (bAP) is the spread of an action potential, initiated at the axon initial segment, from the soma into the dendritic tree, supported by dendritic voltage-gated $\ce{Na+}$ channels.

The bAP carries information about the output of the neuron back to every synapse: it is the postsynaptic signal of spike-timing-dependent plasticity in many synapses ([7.16.14](/7.16.14)). Its efficacy is regulated. In CA1 pyramidal cells the density of A-type $\ce{K+}$ channels increases about fivefold along the apical dendrite (Hoffman and colleagues, 1997), which limits back-propagation; local depolarization that inactivates these channels, or their phosphorylation by kinases, boosts the bAP, which is one way in which synaptic input can control its own plasticity. Branch points are a second control: as noted in 13.3.3, a spike propagates easily from parent to daughters.

### 13.6.2. Dendritic Spikes

**Definition 13.6.2 (Dendritic Spike)** A **dendritic spike** is a regenerative depolarization generated in a dendrite by local voltage-gated channels or NMDA receptors, which can occur without a somatic action potential: a fast $\ce{Na+}$ spike (about $1$–$2\,\mathrm{ms}$), a $\ce{Ca^2+}$ spike (tens of milliseconds) or an NMDA spike (a plateau of $50$–$100\,\mathrm{ms}$).

NMDA spikes arise from the negative slope conductance produced by the magnesium block ([7.16.10](/7.16.10#sec-10.3.2)). In thin basal and tuft dendrites, which have high input impedance, glutamate released by about 10–20 synapses clustered within some $20$–$40\,\mu\mathrm{m}$ depolarizes the branch enough to relieve the block, the NMDA current grows, and the branch jumps to a plateau near $-20\,\mathrm{mV}$ that lasts as long as glutamate remains bound (Schiller and colleagues, 2000; Major and colleagues, 2008). The same number of synapses scattered over the tree sums almost linearly. Fast $\ce{Na+}$ spikes in the oblique dendrites of CA1 cells similarly respond to synchronous clustered input, and their strength is itself plastic (Losonczy, Makara and Magee, 2008). Dendrites can thus detect spatially clustered and temporally synchronous patterns; whether inputs representing related features cluster on the same branch, as the computation would require, has been found for some inputs in vivo but is not universal.

A large $\ce{Ca^2+}$ spike is generated in an "initiation zone" near the main bifurcation of the apical dendrite of layer 5 pyramidal cells, about $700\,\mu\mathrm{m}$ from the soma, by high-threshold $\ce{Ca^2+}$ channels. Larkum, Zhu and Sakmann (1999) found that a bAP that arrives while the tuft is depolarized by distal input lowers the threshold of this $\ce{Ca^2+}$ spike, which in turn drives a burst of somatic action potentials: *BAC firing* (back-propagation-activated $\ce{Ca^2+}$ spike firing). Neither the somatic spike nor the distal input alone produces the burst; together, within a window of a few milliseconds, they do.

Since the tuft receives feedback from higher cortical areas and the basal dendrites receive feedforward input, BAC firing is a cellular mechanism for associating the two streams: the neuron fires a burst when its bottom-up input is confirmed by top-down context (Larkum, 2013).

A similar coincidence mechanism in CA1, a dendritic plateau potential triggered when entorhinal input to the tuft coincides with CA3 input, drives the one-shot formation of place fields described in [7.16.14](/7.16.14#sec-14.8). Distal input can also gate in the opposite direction: in CA1, coincident Schaffer collateral input enables dendritic spikes initiated by the perforant path in the tuft to propagate to the soma (Jarsky and colleagues, 2005).

### 13.6.3. The Neuron as a Two-Layer Network

If each thin branch thresholds its own input, a neuron with $B$ branches computes something like
$$
r = f_{\mathrm{soma}}\Bigl(\sum_{b=1}^{B}\sigma\bigl(\textstyle\sum_{j \in b}w_j u_j\bigr)\Bigr), \tag{13.6}
$$
with a sigmoidal branch nonlinearity $\sigma$ (the NMDA spike) and a somatic nonlinearity $f_{\mathrm{soma}}$. Poirazi, Brannon and Mel (2003) showed that Eq. (13.6) with a fitted $\sigma$ predicted the firing rate of a detailed multicompartment model of a CA1 cell to stimuli with different spatial arrangements of synapses far better than a single sum ($r = f(\sum_jw_ju_j)$, a point neuron), and that clustered inputs drove the cell more than the same number scattered. In this view a single neuron is a two-layer network of the kind used in machine learning ([7.16.19](/7.16.19)), with a storage capacity that depends on which synapses share a branch.

More recent work fitted deep networks to the input–output relation of a detailed layer 5 pyramidal cell model at millisecond resolution: with NMDA receptors in the dendrites, a temporally convolutional network of five to eight layers was needed, without them one hidden layer sufficed (Beniaguev, Segev and London, 2021). These are statements about models, but they show how much computational power the dendritic nonlinearities could add.

![The two-layer model of a neuron (Eq. (13.6)): eight branches, each passing the number of its active synapses (unit weights) through a sigmoid with threshold 10 and slope 1.5, summed at the soma. A: output of one branch against the number of co-active synapses (solid) and the linear sum of single-synapse responses (dashed): supralinear above threshold, saturating at high drive. B: total output for $N$ active synapses that are clustered (filling one branch after another) or scattered over all branches: clustering is far more effective whenever it pushes branches over threshold. C: 20 synapses on one branch, 10 on each of two branches, or 2–3 on each of eight branches: the same number of inputs gives very different outputs.](./plots/two-layer-model.py)

## 13.7. Chemical Signals in Dendrites

Dendrites also carry chemical signals: $\ce{Ca^2+}$ entering through NMDA receptors and voltage-gated channels, and **second messengers** such as cAMP and $\mathrm{IP_3}$ produced by metabotropic receptors ([7.16.11](/7.16.11)). A substance with diffusion coefficient $D$ that is removed by a first-order process with time constant $\tau_c$ (buffering, pumping, degradation) obeys
$$
\frac{\partial c}{\partial t} = D\frac{\partial^2c}{\partial x^2} - \frac{c}{\tau_c} + J(x, t), \tag{13.7}
$$
where $J$ is the local source: a **reaction-diffusion equation** that is mathematically identical to the cable equation, with $\lambda_c^2 = D\tau_c$ in place of $\lambda^2$ and $\tau_c$ in place of $\tau_{\mathrm{m}}$. The steady spread of a chemical signal therefore decays with the length constant $\lambda_c = \sqrt{D\tau_c}$, and all the results of 13.2 apply.

The numbers are very different from the electrical case. Free $\ce{Ca^2+}$ diffuses with $D \approx 220\,\mu\mathrm{m^2\,s^{-1}}$, but in cytoplasm full of buffers its effective diffusion coefficient is about $10$–$50\,\mu\mathrm{m^2\,s^{-1}}$, and it is removed within $10$–$100\,\mathrm{ms}$; hence $\lambda_c \approx 1$–$2\,\mu\mathrm{m}$, a hundred times shorter than $\lambda$. $\ce{Ca^2+}$ signals are therefore local, and spines add a second barrier: the thin neck slows exchange between spine head and dendrite, with time constants of tens to hundreds of milliseconds, so the $\ce{Ca^2+}$ that enters one spine through its NMDA receptors stays there (Svoboda, Tank and Denk, 1996; Yuste and Denk, 1995). This **compartmentalization** is the basis of the input specificity of long-term potentiation ([7.16.14](/7.16.14#sec-14.2)). Molecules with longer lifetimes spread further: active Ras and RhoA spread about $10\,\mu\mathrm{m}$ from a potentiated spine and can facilitate plasticity at neighbors (Harvey and colleagues, 2008), and cAMP and $\mathrm{IP_3}$ spread over tens of micrometers. The dendrite thus has a hierarchy of compartments, set by the ratio of diffusion to removal: spine heads for $\ce{Ca^2+}$, branch segments for slower messengers, and the whole cell for voltage.

## Summary

- Synapses from different sources and inhibitory interneuron classes target distinct dendritic domains (13.1); where an input lands determines how it is integrated.
- In electrotonic units the cable equation is $\partial_TV = \partial_X^2V - V$ (Eq. (13.1)); its steady solutions depend on the boundary condition (table in 13.2.1), and transients attenuate much more than steady voltages because the cable is a low-pass filter.

| Quantity | Formula | Typical value |
|---|---|---|
| Length constant | $\lambda = \sqrt{dR_{\mathrm{m}}/(4R_{\mathrm{i}})}$ | $0.3$–$1\,\mathrm{mm}$ |
| Electrotonic length (Definition 13.2.1) | $L = \ell/\lambda$ | $0.3$–$1.5$ |
| Input conductance, sealed cable | $G_\infty\tanh L$, $G_\infty \propto d^{3/2}$ | — |
| Electrotonic length from transients | $L = \pi/\sqrt{\tau_0/\tau_1 - 1}$ (Proposition 13.3.1) | — |
| Chemical length constant | $\lambda_c = \sqrt{D\tau_c}$ | $\approx 1\,\mu\mathrm{m}$ for $\ce{Ca^2+}$ |

- Trees obeying the 3/2 rule with equal terminal distances are equivalent to one cylinder (Theorem 13.3.1); distal inputs give small, slow, broad somatic EPSPs but large local depolarizations, and attenuation toward the soma is stronger than away from it.
- A shunting conductance is most effective on the path between excitation and soma; off the path its effect is reduced by the product of the voltage attenuations in both directions (Proposition 13.4.1).
- Multicompartment models (Formula 13.5.1) discretize the cable; compartments shorter than $0.1\lambda$, implicit integration.
- Active dendrites support back-propagating action potentials (Definition 13.6.1) and dendritic spikes (Definition 13.6.2); BAC firing associates feedforward and feedback input, and branch nonlinearities make a neuron resemble a two-layer network (Eq. (13.6)).
- Chemical signals obey the same equation with $\lambda_c = \sqrt{D\tau_c}$ and are compartmentalized in spines and branches (13.7).

## Questions

1. Two dendrites have the same $R_{\mathrm{m}}$ and $R_{\mathrm{i}}$; one has diameter $4\,\mu\mathrm{m}$ and length $800\,\mu\mathrm{m}$, the other $1\,\mu\mathrm{m}$ and $400\,\mu\mathrm{m}$. Which is electrotonically longer? If both are sealed at the end, what fraction of a steady voltage imposed at the base reaches the tip when $\lambda = 1\,\mathrm{mm}$ for the thick dendrite?

   **Answer** $\lambda \propto \sqrt d$, so the thin dendrite has $\lambda = 0.5\,\mathrm{mm}$. Then $L = 0.8$ for the thick dendrite and $L = 0.8$ for the thin one: they are electrotonically equal, although the thin one is half as long. The fraction at the tip is $1/\cosh 0.8 = 0.75$ for both.

2. A neuron with a small soma and dendrites approximated by a sealed cylinder gives a voltage transient with $\tau_0 = 25\,\mathrm{ms}$ and $\tau_1 = 5\,\mathrm{ms}$. Estimate $L$. How would the estimate change if, unknown to the experimenter, the soma membrane had a lower resistance (for example because of electrode leak) than the dendrites?

   **Answer** By Eq. (13.3), $L = \pi/\sqrt{25/5 - 1} = \pi/2 = 1.57$. A somatic leak makes the membrane nonuniform: the slowest time constant $\tau_0$ is then shorter than the true dendritic $\tau_{\mathrm{m}}$ and no longer equal to it, and Eq. (13.3), derived for uniform membranes, gives a biased value of $L$. This is why older measurements with sharp electrodes underestimated $\tau_{\mathrm{m}}$ and misjudged $L$.

3. Using Proposition 13.4.1, explain why an inhibitory synapse on the soma reduces the somatic EPSP from every excitatory synapse by the same fraction, while an inhibitory synapse on a distal branch acts selectively.

   **Answer** The soma lies on the path from every excitatory site to the soma, so $\rho = 1$ for all of them and the reduction is $gK_{ss}/(1 + gK_{ss})$ for every input: somatic inhibition scales the whole somatic response (a global gain change). A distal inhibitory site lies on the path only for excitatory synapses further out on the same branch; for those $\rho = 1$, and because $K_{ii}$ is large in a thin branch, a small $g$ is enough. For excitatory synapses on other branches $\rho = A_{i\to p}A_{p\to i}$ is small, because voltage attenuates strongly from the distal site to the branch point $p$, so they are hardly affected. Distal inhibition can therefore veto one input stream or one branch's dendritic spike.

4. Estimate the chemical length constant of cAMP in a dendrite ($D \approx 300\,\mu\mathrm{m^2\,s^{-1}}$, removal by phosphodiesterases with $\tau_c \approx 1\,\mathrm{s}$) and compare it with that of $\ce{Ca^2+}$. What does this imply for the specificity of plasticity mediated by the two messengers?

   **Answer** $\lambda_c = \sqrt{300\cdot1}\,\mu\mathrm{m} \approx 17\,\mu\mathrm{m}$, more than ten times that of $\ce{Ca^2+}$ ($\approx 1$–$2\,\mu\mathrm{m}$). A cAMP signal generated at one spine reaches the dendritic shaft and dozens of neighboring spines, so plasticity that depends only on cAMP would not be synapse-specific; synapse specificity requires a $\ce{Ca^2+}$-dependent step at the activated spine (or a local tag, [7.16.14](/7.16.14#sec-14.7)), while cAMP and other diffusible messengers can coordinate plasticity within a dendritic segment. In reality, compartmentalization of cAMP is further sharpened by anchoring proteins and local degradation, so the estimate is an upper limit.
