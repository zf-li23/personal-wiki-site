---
title: Ion Channels and the Passive Electrical Properties of the Membrane
description: "Channel structure and selectivity, the GHK current and Goldman rectification against the ohmic approximation, the resting potential as a conductance-weighted mean, the membrane as an RC circuit (input resistance, membrane time constant, shunting), and stochastic two-state channels with fluctuation analysis."
---

Every electrical signal of a neuron is a flow of ions through **ion channels**, protein pores in the membrane that are selective for particular ions and are opened and closed by voltage, ligands or mechanical force. The membrane itself, a lipid bilayer of about $1\,\mu\mathrm{F\,cm^{-2}}$, is a capacitor that integrates the current those channels carry. This chapter sets up the language of the next four: the structural basis of selectivity, the relation between ion flow and voltage (Nernst, Goldman and the ohmic approximation), the resting potential as a conductance-weighted average, the membrane as an RC circuit, and the stochastic nature of single channels, from which the deterministic conductances of the Hodgkin–Huxley model emerge as averages.

The physics of permeation, the **Nernst equation**, the **Goldman–Hodgkin–Katz equation** and the cable equation are derived in [7.6.30](/7.6.30#sec-30.2); the physiology of the resting and action potentials is in [7.14.4](/7.14.4). Here we use their results, state when they apply, and develop the parts of the theory that the dynamical models of [7.16.5](/7.16.5)–[7.16.8](/7.16.8) need.

## 4.1. Structure and Selectivity of Channels

Channels have two jobs: to let a chosen ion through at nearly the diffusion-limited rate, and to open and close in response to a signal. The two functions are performed by different parts of the protein.

*Selectivity.* The potassium channel passes $\ce{K+}$ about $10^4$ times better than $\ce{Na+}$, although $\ce{Na+}$ is smaller. The reason, revealed by the crystal structure of the bacterial channel KcsA, is the **selectivity filter**, a narrow stretch of the pore lined by backbone carbonyl oxygens of the signature sequence TVGYG. The oxygens are spaced so that they replace the water shell of a dehydrated $\ce{K+}$ ion nearly perfectly; for the smaller $\ce{Na+}$ they are too far apart, so the energy cost of dehydration is not repaid. Several ions occupy the filter at once and their mutual repulsion drives them through at close to $10^8$ ions per second ([7.6.30](/7.6.30#sec-30.2.5)). The sodium channel has a different, smaller filter in which the charged and polar side chains select by size and by interaction with the partly hydrated ion; calcium channels select $\ce{Ca^2+}$ through high-affinity binding sites formed by four glutamates.

*Gating.* The pore is opened by a voltage sensor (the S4 helix of voltage-gated channels carries positive charges that move in the membrane field, producing the gating currents of [7.6.30](/7.6.30#sec-30.3)), by the binding of a ligand (neurotransmitters, intracellular $\ce{Ca^2+}$, cyclic nucleotides) or by membrane tension. The main channel families of neurons are summarized in the table.

| Family | Gating | Examples | Role |
|---|---|---|---|
| Voltage-gated $\ce{Na+}$ | voltage; fast **inactivation** | Na$_\mathrm{v}$1.1–1.9 | action potential upstroke |
| Voltage-gated $\ce{K+}$ | voltage; some inactivate | K$_\mathrm{v}$1–12 (about 40 genes) | repolarization, firing patterns |
| Voltage-gated $\ce{Ca^2+}$ | voltage | Ca$_\mathrm{v}$1 (L), Ca$_\mathrm{v}$2 (N, P/Q), Ca$_\mathrm{v}$3 (T) | transmitter release, **dendritic spikes** |
| Ligand-gated | transmitter | AMPA, NMDA, GABA$_\mathrm{A}$, nicotinic receptors | fast synaptic transmission |
| Hyperpolarization-activated | voltage (opens on hyperpolarization), cyclic nucleotide | HCN | pacemaking, resonance |
| Two-pore-domain $\ce{K+}$ | little (leak) | K2P | resting conductance |
| Mechanosensitive, thermosensitive | tension, temperature | Piezo, TRP | sensory transduction |

The voltage-gated channels form one superfamily of about 140 genes that evolved from a common ancestor; the diversity of firing patterns that the later chapters describe is largely a diversity of this repertoire and of its expression in different **cell types** ([7.16.5](/7.16.5#sec-5.4)).

## 4.2. Currents, Reversal Potentials and Rectification

Ions move through an open channel under two forces: diffusion down the concentration gradient and drift in the electric field. The balance gives the Nernst potential

$$
E_X = \frac{RT}{zF}\ln\frac{[X]_{\mathrm{o}}}{[X]_{\mathrm{i}}},
$$

at which the net current of ion $X$ vanishes (for $\ce{K+}$ with 140 mM inside and 5 mM outside, $E_{\mathrm{K}} = -89\,\mathrm{mV}$ at $37\,^\circ\mathrm{C}$, where $RT/F = 26.7\,\mathrm{mV}$). For a channel whose permeation is independent of other ions and of the voltage, integrating the Nernst–Planck equation across a membrane with a constant field gives the **Goldman–Hodgkin–Katz equation**, which for a single ion is the following current.

**Definition 4.2.1 (GHK Current)** For a membrane with permeability $P_X$ to ion $X$ of valence $z$, the constant-field (GHK) current density is

$$
i_X(V) = P_X\,\frac{z^2F^2}{RT}\,V\,\frac{[X]_{\mathrm{i}} - [X]_{\mathrm{o}}\,\mathrm{e}^{-zFV/RT}}{1 - \mathrm{e}^{-zFV/RT}},
$$

where $V$ is the membrane potential and $[X]_{\mathrm{i}}$, $[X]_{\mathrm{o}}$ are the concentrations inside and outside. The current vanishes at the Nernst potential $E_X$.

**Definition 4.2.2 (Goldman Rectification)** **Goldman rectification** is the deviation of the GHK current-voltage relation from linearity: the current is larger in the direction in which the ion flows down its concentration gradient than in the opposite direction, so that with $[X]_{\mathrm{i}} > [X]_{\mathrm{o}}$ the outward current is larger than the inward current for the same driving force.

Models of neurons almost always use a simpler form, the ohmic (linear) approximation

$$
i_X = g_X\,(V - E_X),
$$

with a conductance $g_X$ that does not depend on $V$ except through gating. Expanding the GHK relation to first order around $V = E_X$ gives the ohmic form, with $g_X$ the slope of the GHK curve at $E_X$. Figure 1 shows how far one can go from $E_X$: for $\ce{K+}$ with $[\ce{K+}]_{\mathrm{o}} = 5\,\mathrm{mM}$ the GHK current is 1.2 times the ohmic prediction at $V - E = +20\,\mathrm{mV}$ and 1.6 times at $+50\,\mathrm{mV}$, but only 0.85 and 0.68 times at $-20$ and $-50\,\mathrm{mV}$; for $\ce{Na+}$ (12 mM inside, 145 mM outside) the inward current is the larger one, 1.45 times the ohmic value at $V - E = -50\,\mathrm{mV}$. 

Within about $10\,\mathrm{mV}$ of $E$ the error is below 10%, which covers the subthreshold range, and with smaller concentration ratios the curves are closer to linear. 

In the Hodgkin–Huxley model, where driving forces reach $100\,\mathrm{mV}$, the empirical gating functions absorb the difference: Hodgkin and Huxley defined $g = i/(V - E)$ from the measured currents. Real channels also deviate from GHK for other reasons: ions interact in the pore, and some channels rectify strongly for reasons unrelated to concentrations, such as block by intracellular $\ce{Mg^2+}$ and polyamines in inward-rectifier $\ce{K+}$ channels.

![The ohmic approximation and the Goldman–Hodgkin–Katz current. A: the $\ce{K+}$ current (140 mM inside, 5 mM outside) is larger outward than inward; the dashed line is the ohmic approximation with the slope of the GHK curve at the reversal potential $E$. B: the $\ce{Na+}$ current (12 mM inside, 145 mM outside). C: ratio of the GHK current to the ohmic current as a function of the driving force; the approximation is good within about 10 mV of $E$ and for ions with similar concentrations on both sides, and it fails for ions with a large concentration ratio](./plots/goldman-rectification.py)

## 4.3. The Resting Potential

In a membrane with several ions, each with a conductance $g_j$ and a **reversal potential** $E_j$, the net membrane current is $\sum_j g_j (V - E_j)$.

**Proposition 4.3.1 (Resting Potential as a Weighted Mean)** In the ohmic approximation the potential at which the net ionic current vanishes is

$$
V_{\mathrm{rest}} = \frac{\sum_j g_j E_j}{\sum_j g_j},
$$

a mean of the reversal potentials weighted by the conductances. The voltage relaxes to $V_{\mathrm{rest}}$ with time constant $C_{\mathrm{m}}/\sum_j g_j$.

**Proof** Setting $\sum_j g_j (V - E_j) = 0$ and solving for $V$ gives the formula; with the capacitive current, $C_{\mathrm{m}}\,\mathrm{d}V/\mathrm{d}t = -\sum_j g_j(V - V_{\mathrm{rest}})$, which is linear with the stated time constant. $\square$

The **resting membrane potential** of a neuron, about $-65\,\mathrm{mV}$, therefore lies near $E_{\mathrm{K}}$ because the conductance at rest is dominated by $\ce{K+}$ (leak) channels; for $g_{\mathrm{K}} : g_{\mathrm{Cl}} : g_{\mathrm{Na}} = 1 : 0.2 : 0.04$, with $E_{\mathrm{K}} = -89$, $E_{\mathrm{Cl}} = -69$ and $E_{\mathrm{Na}} = +66\,\mathrm{mV}$, the formula gives $-81\,\mathrm{mV}$. Real neurons rest at $-60$ to $-70\,\mathrm{mV}$ because the sodium and other leak conductances are larger relative to $g_{\mathrm{K}}$. The result also explains the action potential qualitatively: when the voltage-gated $\ce{Na+}$ conductance rises by a factor of several hundred, $g_{\mathrm{Na}}/g_{\mathrm{K}}$ passes from $0.04$ to 20 or more and $V$ moves toward $E_{\mathrm{Na}}$ (Figure 2D). Because the weights are conductances, the resting potential is insensitive to the pumps: the $\ce{Na+}/\ce{K+}$ pump contributes a small current (about 1–3 mV) but mainly maintains the concentration gradients over minutes.

## 4.4. The Equivalent Circuit and Passive Responses

The lipid bilayer separates two conducting solutions across a gap of about 4 nm, so it is a capacitor with a specific capacitance $c_{\mathrm{m}} \approx 1\,\mu\mathrm{F\,cm^{-2}}$, nearly the same for all cells. The channels in parallel form the conductance, the batteries are the reversal potentials (Figure 2A). For a small patch of membrane of area $A$ (an *isopotential* compartment, justified when the cell is small compared with the length constant of [7.6.30](/7.6.30#sec-30.5)) with a single effective leak conductance $g_{\mathrm{L}}$ and reversal potential $E_{\mathrm{L}}$,

$$
C\,\frac{\mathrm{d}V}{\mathrm{d}t} = -g_{\mathrm{L}}(V - E_{\mathrm{L}}) + I_{\mathrm{ext}}(t),
\qquad C = c_{\mathrm{m}}A,\quad g_{\mathrm{L}} = \frac{A}{R_{\mathrm{m}}},
$$

where $R_{\mathrm{m}}$ is the specific membrane resistance, in $\Omega\,\mathrm{cm^2}$. Two quantities describe the response.

**Definition 4.4.1 (Input Resistance and Membrane Time Constant)** The **input resistance** $R_{\mathrm{in}} = 1/g_{\mathrm{L}} = R_{\mathrm{m}}/A$ is the steady-state voltage change per unit injected current; the **membrane time constant** $\tau_{\mathrm{m}} = R_{\mathrm{in}}C = R_{\mathrm{m}}c_{\mathrm{m}}$ is the time scale on which the voltage relaxes to it.

For a step of current $I_0$ switched on at $t = 0$ the solution is

$$
V(t) = E_{\mathrm{L}} + R_{\mathrm{in}}I_0\bigl(1 - \mathrm{e}^{-t/\tau_{\mathrm{m}}}\bigr),
$$

and for sinusoidal current at frequency $f$ the amplitude of the voltage is $\lvert Z(f)\rvert\,I_0$ with the impedance $\lvert Z\rvert = R_{\mathrm{in}}/\sqrt{1 + (2\pi f\tau_{\mathrm{m}})^2}$: the membrane is a low-pass filter with cutoff $f_{\mathrm{c}} = 1/(2\pi\tau_{\mathrm{m}})$. Note that $\tau_{\mathrm{m}} = R_{\mathrm{m}}c_{\mathrm{m}}$ is independent of size, while $R_{\mathrm{in}}$ and $C$ depend on the area, so that small cells have high input resistance and respond to a given current with a larger voltage change.

**Example 4.4.1 (A Spherical Soma)** A sphere of radius $20\,\mu\mathrm{m}$ with $c_{\mathrm{m}} = 1\,\mu\mathrm{F\,cm^{-2}}$ and $R_{\mathrm{m}} = 5\,\mathrm{k\Omega\,cm^2}$ has area $A = 4\pi a^2 = 5.0\times 10^{-5}\,\mathrm{cm^2}$, hence $C = 50\,\mathrm{pF}$, $R_{\mathrm{in}} = R_{\mathrm{m}}/A = 99\,\mathrm{M\Omega}$ and $\tau_{\mathrm{m}} = 5\,\mathrm{ms}$. A current of $0.1\,\mathrm{nA}$ depolarizes it by $10\,\mathrm{mV}$ with a time constant of $5\,\mathrm{ms}$ (Figure 2B), and the cutoff frequency is $32\,\mathrm{Hz}$ (Figure 2C).

:::

The same circuit explains **shunting inhibition** when the synaptic reversal potential is near rest: an active synaptic conductance $g_{\mathrm{syn}}$ adds in parallel to $g_{\mathrm{L}}$, which reduces both $R_{\mathrm{in}}$ and $\tau_{\mathrm{m}}$ by the factor $g_{\mathrm{L}}/(g_{\mathrm{L}} + g_{\mathrm{syn}})$ (Figure 2B, red). In a cortical neuron receiving thousands of synaptic inputs, the total conductance during activity is several times that at rest, so that $\tau_{\mathrm{m}}$ shrinks from tens of milliseconds to a few milliseconds, a "high-conductance state" in which neurons integrate over short windows. In measurements, $R_{\mathrm{in}}$ and $\tau_{\mathrm{m}}$ are obtained by fitting a single exponential to the voltage response to a small current step; neurons are extended objects, so the response has several exponentials, and the cable theory of [7.16.13](/7.16.13) relates the slowest of them to $\tau_{\mathrm{m}}$.

![The passive membrane. A: equivalent circuit of an isopotential compartment. B: response to a current step for a soma of radius 20 µm (time constant marked by dots); doubling the leak conductance halves both $R_\mathrm{in}$ and $\tau_\mathrm{m}$. C: the impedance magnitude as a function of frequency, a low-pass filter with cutoff 32 Hz. D: the resting potential as the conductance-weighted mean of the reversal potentials as a function of the ratio $g_\mathrm{Na}/g_\mathrm{K}$; during the action potential the ratio increases by orders of magnitude](./plots/rc-membrane.py)

## 4.5. Stochastic Channels and Macroscopic Currents

A single channel does not open gradually: it switches abruptly between a conducting and a nonconducting state, in a random fashion, as recorded in the **patch clamp** ([7.6.30](/7.6.30#sec-30.2.3)). The simplest model is a two-state continuous-time **Markov chain** with a closed state C and an open state O,

$$
\mathrm{C} \underset{\beta}{\overset{\alpha}{\rightleftharpoons}} \mathrm{O},
$$

where $\alpha(V)$ is the opening rate and $\beta(V)$ the closing rate, both in $\mathrm{ms^{-1}}$, the convention of Hodgkin and Huxley and of the rest of this chapter. The dwell times are exponential: the channel stays open for a time with mean $1/\beta$ and closed for a time with mean $1/\alpha$.

**Definition 4.5.1 (Single-Channel Conductance and Open Probability)** The **single-channel conductance** $\gamma$ is the conductance of one open channel (about 10–100 pS, so that the single-channel current at $V - E = 50\,\mathrm{mV}$ is $0.5$–$5\,\mathrm{pA}$). The **open probability** $p_{\mathrm{o}}(t)$ is the probability that a channel is open at time $t$.

The probability obeys the master equation $\mathrm{d}p_{\mathrm{o}}/\mathrm{d}t = \alpha(1 - p_{\mathrm{o}}) - \beta p_{\mathrm{o}}$, whose solution is exponential relaxation to $p_\infty = \alpha/(\alpha + \beta)$ with time constant $\tau = 1/(\alpha + \beta)$. This is the form of the gating equations of the Hodgkin–Huxley model ([7.16.5](/7.16.5#sec-5.2)), with $x_\infty = \alpha_x/(\alpha_x + \beta_x)$ and $\tau_x = 1/(\alpha_x + \beta_x)$, and it shows what a **gating variable** is: the open probability of a gate, or equivalently the fraction of channels with the gate open.

A membrane has many channels. If $N$ identical, independent channels are present, the number open $K(t)$ is a sum of $N$ independent Bernoulli variables with success probability $p_{\mathrm{o}}(t)$, so the macroscopic current $I = i K$ with $i = \gamma(V - E)$ has

$$
\mathbb{E}[I] = N\,p_{\mathrm{o}}\,i,
\qquad
\operatorname{Var}(I) = N\,p_{\mathrm{o}}(1 - p_{\mathrm{o}})\,i^2.
$$

The relative fluctuation is $\sqrt{(1 - p_{\mathrm{o}})/(N p_{\mathrm{o}})}$, which declines as $N^{-1/2}$. With a few channels the current is a random staircase; with hundreds it is smooth with noise, and with $10^3$–$10^4$ channels (a **node of Ranvier**, or the soma of a neuron) the deterministic equation for the open probability (the master equation) is an excellent description (Figure 3A, B). Small compartments, such as the axon terminal or a dendritic spine, contain few channels, and the randomness of the gates matters there.

![Channel noise. A: a single two-state channel switches randomly between closed (C) and open (O) states after a voltage step at $t = 0$ increases the opening rate; three trials. B: the fraction of open channels for $N = 10$, $100$, $1000$ channels in one trial each approaches the deterministic open probability from the master equation. C: nonstationary fluctuation analysis: variance against mean over 300 repeated trials of 200 channels, plotted in normalized units, follows the parabola $p(1-p)$](./plots/single-channel.py)

**Proposition 4.5.1 (Nonstationary Fluctuation Analysis)** If $N$ independent channels with single-channel current $i$ are recorded in many repeated trials, the variance and the mean of the macroscopic current at the same time points satisfy

$$
\sigma^2 = i\,\bar I - \frac{\bar I^2}{N}.
$$

**Proof** With $\bar I = Np_{\mathrm{o}}i$ and $\sigma^2 = Np_{\mathrm{o}}(1-p_{\mathrm{o}})i^2$, eliminating $p_{\mathrm{o}} = \bar I/(Ni)$ gives $\sigma^2 = i\bar I - \bar I^2/N$. $\square$

The plot of variance against mean is a parabola (Figure 3C) whose initial slope is the single-channel current $i$ and which returns to zero at $\bar I = Ni$, when all channels are open. Fitting it gives both $i$, hence $\gamma = i/(V - E)$, and the number of channels $N$ in the patch, without resolving single events; the method works when single-channel recordings are not possible because the channels are too many, too small, or too fast. Applied to synaptic currents, the same argument gives the number of postsynaptic receptors and their conductance ([7.16.10](/7.16.10)).

## Summary

- Channels are selective (the $\ce{K+}$ filter replaces the water shell of the dehydrated ion) and gated by voltage, ligand or force; the neuronal repertoire of voltage-gated channels (Section 4.1) underlies the diversity of firing patterns.
- The GHK current rectifies (Definitions 4.2.1 and 4.2.2); the ohmic form $i = g(V - E)$ is accurate for driving forces up to about 10 mV and is the basis of conductance-based models.
- The resting potential is the conductance-weighted mean of the reversal potentials (Proposition 4.3.1); an increase of $g_{\mathrm{Na}}$ moves $V$ toward $E_{\mathrm{Na}}$.
- An isopotential membrane is an RC circuit: $R_{\mathrm{in}} = R_{\mathrm{m}}/A$, $\tau_{\mathrm{m}} = R_{\mathrm{m}}c_{\mathrm{m}}$ (Definition 4.4.1), a low-pass filter of cutoff $1/(2\pi\tau_{\mathrm{m}})$; synaptic conductance shunts it.
- Two-state gating has $p_\infty = \alpha/(\alpha+\beta)$ and $\tau = 1/(\alpha+\beta)$ (Definition 4.5.1); channel noise has variance $Np(1-p)i^2$ and gives the parabola of Proposition 4.5.1.

## Questions

1. Compute $E_{\mathrm{K}}$ at $37\,^\circ\mathrm{C}$ for $[\ce{K+}]_{\mathrm{o}} = 20\,\mathrm{mM}$ and $[\ce{K+}]_{\mathrm{i}} = 140\,\mathrm{mM}$, and the change of the resting potential if $V_{\mathrm{rest}}$ follows $E_{\mathrm{K}}$ with $g_{\mathrm{Na}}/g_{\mathrm{K}} = 0.04$ and $E_{\mathrm{Na}} = 66\,\mathrm{mV}$ (ignore chloride).

   **Answer** $E_{\mathrm{K}} = 26.7\ln(20/140) = -52\,\mathrm{mV}$ (from $-89\,\mathrm{mV}$ at 5 mM). By Proposition 4.3.1, $V_{\mathrm{rest}} = (E_{\mathrm{K}} + 0.04E_{\mathrm{Na}})/1.04$: $-83\,\mathrm{mV}$ at 5 mM and $-47\,\mathrm{mV}$ at 20 mM, a depolarization of about 36 mV.

2. A neuron has $R_{\mathrm{in}} = 200\,\mathrm{M\Omega}$ and $\tau_{\mathrm{m}} = 20\,\mathrm{ms}$. Find $C$. During synaptic bombardment the conductance triples; how do $R_{\mathrm{in}}$ and $\tau_{\mathrm{m}}$ change?

   **Answer** $C = \tau_{\mathrm{m}}/R_{\mathrm{in}} = 20\,\mathrm{ms}/200\,\mathrm{M\Omega} = 100\,\mathrm{pF}$. Tripling $g$ divides $R_{\mathrm{in}}$ and $\tau_{\mathrm{m}}$ by 3: 67 MΩ and 6.7 ms; the capacitance is unchanged.

3. A channel has opening rate $\alpha = 0.25\,\mathrm{ms^{-1}}$ and closing rate $\beta = 1\,\mathrm{ms^{-1}}$. Find the mean open and closed times, the open probability and the relaxation time constant. For $N = 400$ channels with $\gamma = 20\,\mathrm{pS}$ at $V - E = 50\,\mathrm{mV}$, what are the mean and standard deviation of the stationary current?

   **Answer** Open time $1/\beta = 1\,\mathrm{ms}$, closed time $1/\alpha = 4\,\mathrm{ms}$, $p_\infty = 0.25/1.25 = 0.2$, $\tau = 1/1.25 = 0.8\,\mathrm{ms}$. The single-channel current is $i = 1\,\mathrm{pA}$, so $\bar I = 400 \cdot 0.2 \cdot 1 = 80\,\mathrm{pA}$ and $\sigma = \sqrt{400 \cdot 0.2 \cdot 0.8}\cdot 1\,\mathrm{pA} = 8\,\mathrm{pA}$ (10% of the mean).

4. Fluctuation analysis of a current gives a parabola with initial slope $2\,\mathrm{pA}$ and mean current at the peak $\bar I_{\max} = 120\,\mathrm{pA}$ where the variance is $\sigma^2 = 150\,\mathrm{pA^2}$. Estimate $N$ and the peak open probability.

   **Answer** $i = 2\,\mathrm{pA}$. From $\sigma^2 = i\bar I - \bar I^2/N$: $150 = 240 - 14400/N$, so $N = 14400/90 = 160$. The peak open probability is $\bar I/(Ni) = 120/320 = 0.375$.
