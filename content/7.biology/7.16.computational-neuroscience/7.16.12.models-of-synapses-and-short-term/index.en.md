---
title: Models of Synapses and Short-Term Plasticity
description: "Reduced models of synaptic transmission for network simulations: current- and conductance-based synapses; delta, exponential, alpha and difference-of-exponentials kernels with their differential equations; first-order kinetic schemes and the NMDA synapse; gap-junction coupling and the synchronization of two neurons; the Tsodyks–Markram model of depression and facilitation, its steady state, filtering and gain control; temporal summation and the effective time constant."
---

The two preceding chapters described how a synapse releases transmitter ([7.16.9](/7.16.9)) and how receptors turn it into a current ([7.16.10](/7.16.10)). A network model of thousands of neurons cannot afford a five-site $\ce{Ca^2+}$ sensor at every terminal and a Markov chain at every receptor cluster; it needs a synapse described by one or two variables that reproduces the time course of the postsynaptic conductance, its dependence on voltage where that matters, and its dependence on the recent history of presynaptic spikes. This chapter collects these reduced models: phenomenological kernels and their equivalent differential equations, first-order kinetic schemes, the gap junction as a coupling term, and the Tsodyks–Markram model of short-term plasticity, which turns the phenomena of [7.16.9](/7.16.9#sec-9.6) into dynamics and shows what they compute. The neurons that receive these inputs are the reduced models of [7.16.8](/7.16.8); the networks built from both follow in [7.16.15](/7.16.15), and short-term facilitation returns as a memory mechanism in [7.16.45](/7.16.45).

## 12.1. Why Model the Synapse

Cognition is carried out by networks, and in a network each neuron influences the others only through its synapses. A synaptic model has to supply, for every presynaptic spike at time $t_k$, the current that it produces in the postsynaptic cell. Two properties make this more than a delay line. First, the response is spread over time (milliseconds for **AMPA receptors**, a hundred milliseconds for **NMDA receptors**), so successive inputs add (**temporal summation**) and the synaptic time constants set the time scale of network dynamics. Second, synapses are plastic: their strength changes with use over milliseconds to seconds (short-term plasticity, 12.5) and over hours to a lifetime (long-term plasticity, [7.16.14](/7.16.14)), which is the basis of learning and of many real-time computations.

Two modeling strategies are used, as for voltage-gated channels. *Phenomenological* models prescribe the shape of the conductance change after a spike directly, chosen to fit recorded currents. *Physiological* (kinetic) models describe the opening of the postsynaptic channels by a rate equation driven by the transmitter concentration, in analogy with the **gating variables** of the **Hodgkin–Huxley model** (12.3). Both enter the membrane equation of the postsynaptic neuron in the same way.

## 12.2. Phenomenological Synapses

### 12.2.1. Current-Based and Conductance-Based Synapses

**Definition 12.2.1 (Conductance-Based and Current-Based Synapses)** In a **conductance-based synapse** the synaptic current is
$$
I_{\mathrm{syn}}(t) = g_{\mathrm{syn}}(t)\,(V - E_{\mathrm{syn}}), \qquad g_{\mathrm{syn}}(t) = \bar g_{\mathrm{syn}}\,s(t), \tag{12.1}
$$
with a dimensionless gating variable $0 \le s \le 1$ driven by presynaptic spikes and the reversal potential $E_{\mathrm{syn}}$ of Definition 10.2.1. In a **current-based synapse** the driving force is replaced by a constant, $I_{\mathrm{syn}}(t) = -\bar I_{\mathrm{syn}}\,s(t)$, so that the current does not depend on the postsynaptic potential.

With the sign convention of this course (outward current positive), the postsynaptic membrane equation reads
$$
C_{\mathrm{m}}\frac{\mathrm{d}V}{\mathrm{d}t} = -g_{\mathrm{L}}(V - E_{\mathrm{L}}) - \sum_j \bar g_j\,s_j(t)\,(V - E_j) + I_{\mathrm{ext}}. \tag{12.2}
$$
The conductance-based form is the physically correct one: an excitatory synapse ($E_{\mathrm{syn}} \approx 0\,\mathrm{mV}$) can never drive $V$ above $E_{\mathrm{syn}}$, an inhibitory synapse near rest acts by **shunting inhibition** (Proposition 10.4.1), and every open synapse increases the total membrane conductance and so shortens the **membrane time constant** (12.6). The current-based form is linear in the inputs and therefore analytically convenient; it is adequate when $V$ stays far from all synaptic reversal potentials, which is roughly true for excitation of a cell below threshold but not for inhibition.

### 12.2.2. Four Kernels

In a phenomenological model each presynaptic spike adds a fixed waveform, and the gating variable is the superposition
$$
s(t) = \sum_k K(t - t_k), \tag{12.3}
$$
where $K(t) = 0$ for $t < 0$. Superposition assumes that the synapse does not saturate and has no history dependence; both assumptions are removed later in the chapter.

**Definition 12.2.2 (Synaptic Kernels)** The four standard kernels (the second-order kernel $(t/\tau_{\mathrm{s}})\mathrm{e}^{1 - t/\tau_{\mathrm{s}}}$ defines the **alpha synapse**), with their equivalent differential equations driven by the spike train $\rho(t) = \sum_k\delta(t - t_k)$, are:

| Kernel | $K(t)$ for $t \ge 0$ | Differential form | Peak time |
|---|---|---|---|
| Delta | $\delta(t)$ | $s = \rho(t)$ (each spike makes an instantaneous jump of $V$) | $0$ |
| Exponential | $\mathrm{e}^{-t/\tau_{\mathrm{s}}}$ | $\tau_{\mathrm{s}}\dot s = -s + \tau_{\mathrm{s}}\rho(t)$ | $0$ |
| Alpha function | $\dfrac{t}{\tau_{\mathrm{s}}}\,\mathrm{e}^{1 - t/\tau_{\mathrm{s}}}$ | $\tau_{\mathrm{s}}\dot s = -s + x$, $\ \tau_{\mathrm{s}}\dot x = -x + \mathrm{e}\,\tau_{\mathrm{s}}\rho(t)$ | $\tau_{\mathrm{s}}$ |
| Difference of exponentials | $N\left(\mathrm{e}^{-t/\tau_{\mathrm{d}}} - \mathrm{e}^{-t/\tau_{\mathrm{r}}}\right)$ | $\tau_{\mathrm{d}}\dot s = -s + x$, $\ \tau_{\mathrm{r}}\dot x = -x + c\,\tau_{\mathrm{r}}\rho(t)$ | $\dfrac{\tau_{\mathrm{r}}\tau_{\mathrm{d}}}{\tau_{\mathrm{d}} - \tau_{\mathrm{r}}}\ln\dfrac{\tau_{\mathrm{d}}}{\tau_{\mathrm{r}}}$ |

In the table the constant $N$ (and $c$ in the differential form) normalizes the peak of the difference of exponentials to 1, with rise time constant $\tau_{\mathrm{r}}$ and decay time constant $\tau_{\mathrm{d}} > \tau_{\mathrm{r}}$.

Each kernel is the impulse response of a linear filter: the exponential kernel of a first-order low-pass filter, the alpha function of two identical first-order filters in series, the difference of exponentials of two filters with different time constants. This is why every kernel can be written as a small system of linear differential equations, which is how it is implemented in simulations: the delta function in the equations means that at each spike the variable jumps, and between spikes it relaxes. Equivalently, for the exponential synapse the update rule from one time step to the next is exact, $s \leftarrow s\,\mathrm{e}^{-\Delta t/\tau_{\mathrm{s}}}$, plus $1$ at each spike; event-driven simulators exploit this to update a synapse only when a spike arrives.

The choice of kernel matters for timing more than for amplitude. With instantaneous rise (delta and exponential), a synaptic input can trigger a spike with zero delay, which gives networks unrealistically fast and precise synchronization; the finite rise of the alpha and difference-of-exponentials kernels removes this artifact. Typical parameters at $35^\circ\mathrm{C}$ are: AMPA $\tau_{\mathrm{r}} \approx 0.2$–$0.5\,\mathrm{ms}$, $\tau_{\mathrm{d}} \approx 2\,\mathrm{ms}$; $\mathrm{GABA_A}$ $\tau_{\mathrm{r}} \approx 0.5\,\mathrm{ms}$, $\tau_{\mathrm{d}} \approx 5$–$10\,\mathrm{ms}$; NMDA $\tau_{\mathrm{r}} \approx 2$–$5\,\mathrm{ms}$, $\tau_{\mathrm{d}} \approx 50$–$150\,\mathrm{ms}$ (the table at the end of [7.16.10](/7.16.10)).

**Example 12.2.1** For $\tau_{\mathrm{r}} = 1\,\mathrm{ms}$ and $\tau_{\mathrm{d}} = 5\,\mathrm{ms}$ the difference of exponentials peaks at $t^* = (5/4)\ln 5 = 2.01\,\mathrm{ms}$, where $\mathrm{e}^{-t^*/5} - \mathrm{e}^{-t^*} = 0.669 - 0.134 = 0.535$, so $N = 1/0.535 = 1.87$. Its integral is $N(\tau_{\mathrm{d}} - \tau_{\mathrm{r}}) = 7.5\,\mathrm{ms}$, compared with $\mathrm{e}\,\tau_{\mathrm{s}}$ for an alpha function and $\tau_{\mathrm{s}}$ for an exponential of the same peak; the integral sets the charge delivered and therefore the size of the postsynaptic potential when $\tau_{\mathrm{m}}$ is long.

:::

![Phenomenological synaptic kernels (Definition 12.2.2) and the postsynaptic potentials they produce. A: conductance waveforms normalized to a peak of 1: exponential ($\tau_{\mathrm{s}} = 5\,\mathrm{ms}$), alpha function ($\tau_{\mathrm{s}} = 2\,\mathrm{ms}$) and difference of exponentials ($\tau_{\mathrm{r}} = 1$, $\tau_{\mathrm{d}} = 5\,\mathrm{ms}$); the delta kernel is drawn as an arrow. B: postsynaptic potentials of a passive conductance-based membrane ($\tau_{\mathrm{m}} = 20\,\mathrm{ms}$, $g_{\mathrm{L}} = 10\,\mathrm{nS}$, $E_{\mathrm{syn}} = 0\,\mathrm{mV}$) for kernels of equal integral ($10\,\mathrm{nS\,ms}$): the shapes differ during the first $10\,\mathrm{ms}$ and converge to the same membrane decay; the delta synapse gives an instantaneous jump. C: the same alpha-synapse input in a membrane at rest and in a high-conductance state with $40\,\mathrm{nS}$ of tonic background conductance ($\tau_{\mathrm{eff}} = 4\,\mathrm{ms}$): the PSP is smaller and, rescaled (dotted), much briefer.](./plots/synaptic-kernels.py)

## 12.3. Kinetic Models

### 12.3.1. First-Order Receptor Binding

The kinetic schemes of [7.16.10](/7.16.10#sec-10.6) can be reduced to two states, closed and open, with an opening rate proportional to the transmitter concentration $T$. Because transmitter is present in the cleft for only about a millisecond, it is sufficient to model it as a rectangular pulse of concentration $T_{\max}$ and duration $t_{\mathrm{p}}$ after each presynaptic spike (Destexhe, Mainen and Sejnowski, 1994).

**Formula 12.3.1 (First-Order Kinetic Synapse)** Let $s$ be the fraction of open postsynaptic channels, $\alpha$ the opening (binding) rate constant and $\beta$ the closing rate. Then
$$
\frac{\mathrm{d}s}{\mathrm{d}t} = \alpha\,T(t)\,(1 - s) - \beta s, \tag{12.4}
$$
with $T(t) = T_{\max}$ for $t_k < t < t_k + t_{\mathrm{p}}$ and $T = 0$ otherwise. During the pulse $s$ relaxes toward $s_\infty = \alpha T_{\max}/(\alpha T_{\max} + \beta)$ with time constant $1/(\alpha T_{\max} + \beta)$; after it, $s$ decays with time constant $1/\beta$.

With $T_{\max} = 1\,\mathrm{mM}$ and $t_{\mathrm{p}} = 1\,\mathrm{ms}$, fits to recorded currents give $\alpha = 1.1\,\mathrm{mM^{-1}\,ms^{-1}}$, $\beta = 0.19\,\mathrm{ms^{-1}}$ for AMPA receptors, $\alpha = 5$, $\beta = 0.18$ for $\mathrm{GABA_A}$ receptors and $\alpha = 0.072$, $\beta = 0.0066$ for NMDA receptors (Destexhe and colleagues, 1998). For AMPA the pulse opens $s_\infty(1 - \mathrm{e}^{-1.29}) = 0.62$ of the channels and the current then decays with $1/\beta = 5\,\mathrm{ms}$; for NMDA the same pulse opens only $7\%$, which then close with $1/\beta = 150\,\mathrm{ms}$. The model is cheap, as cheap as an exponential kernel, but its factor $(1 - s)$ builds in saturation: when spikes arrive faster than the channels close, $s$ approaches $s_\infty$ instead of growing without bound, which the linear kernels of Eq. (12.3) cannot reproduce. Like the kernels, it can be updated analytically from spike to spike.

### 12.3.2. The NMDA Synapse

The NMDA conductance needs two additions: its slow, saturating gating, and its voltage dependence. The **magnesium block** is the factor $B(V)$ of Definition 10.3.3; since unblocking is fast compared with the synaptic time course, it multiplies the instantaneous conductance.

**Formula 12.3.2 (Saturating NMDA Synapse)** A second-order model used in cortical network simulations (Wang, 2002) is
$$
\frac{\mathrm{d}x}{\mathrm{d}t} = -\frac{x}{\tau_{\mathrm{r}}} + \sum_k\delta(t - t_k), \qquad \frac{\mathrm{d}s}{\mathrm{d}t} = -\frac{s}{\tau_{\mathrm{d}}} + a\,x\,(1 - s), \tag{12.5}
$$
$$
I_{\mathrm{NMDA}} = \bar g_{\mathrm{NMDA}}\,s\,B(V)\,(V - E_{\mathrm{NMDA}}),
$$
with $\tau_{\mathrm{r}} = 2\,\mathrm{ms}$, $\tau_{\mathrm{d}} = 100\,\mathrm{ms}$ and $a = 0.5\,\mathrm{ms^{-1}}$.

The variable $x$ represents the transient of bound transmitter; $s$ integrates it with saturation. For a presynaptic neuron firing at rate $r$ the time-averaged $s$ is approximately $r\tau_{\mathrm{d}}/(1 + r\tau_{\mathrm{d}})$ up to a factor, which saturates above about $1/\tau_{\mathrm{d}} = 10\,\mathrm{Hz}$. The long $\tau_{\mathrm{d}}$ makes NMDA-mediated recurrent excitation a slow variable that can integrate inputs over hundreds of milliseconds; this is the basis of the attractor models of working memory and decision making ([7.16.45](/7.16.45), [7.16.47](/7.16.47)). The voltage dependence makes the same synapse a **coincidence detector** in the sense of Definition 10.3.4, the property on which long-term plasticity is built ([7.16.14](/7.16.14)).

## 12.4. Electrical Synapses

An **electrical synapse** has no dynamics of its own: the current through the **gap junction** is proportional to the difference of the two membrane potentials,
$$
I_{1\to2}(t) = g_{\mathrm{c}}\,\bigl(V_1(t) - V_2(t)\bigr) = -I_{2\to1}(t), \tag{12.6}
$$
and enters the membrane equation of each cell with the appropriate sign: $C_{\mathrm{m}}\dot V_2 = \dots + g_{\mathrm{c}}(V_1 - V_2)$. The junction is bidirectional, passive and nonselective, and its conductance is independent of voltage and transmitter (rectifying junctions are the exception). In the steady state it transmits a fraction $k = g_{\mathrm{c}}/(g_{\mathrm{c}} + g_2)$ of a voltage change (Eq. (10.5)); for fast signals the membrane capacitance of the receiving cell attenuates it further.

The main computational effect of gap junctions is synchronization. Consider two leaky integrate-and-fire neurons ([7.16.8](/7.16.8)) driven by slightly different constant currents and coupled by Eq. (12.6). Each spike of neuron 1 transmits a brief depolarizing potential (a spikelet) to neuron 2, which advances its next spike if neuron 2 is close to threshold, and the reset after the spike transmits a hyperpolarization, which delays neuron 2 if it lags far behind; between spikes the junction pulls the two subthreshold trajectories toward each other. The net effect is that the leader is slowed and the follower is accelerated, and the pair locks at a small phase difference (figure below). The analysis of such locking in terms of **phase response curves** is in [7.16.15](/7.16.15#sec-15.6). In the brain, gap junctions between parvalbumin-expressing interneurons of the same class contribute to the synchrony of gamma oscillations, and those of the inferior olive synchronize its subthreshold oscillations; in both cases electrical and chemical coupling act together.

![Synchronization of two leaky integrate-and-fire neurons by an electrical synapse ($\tau_{\mathrm{m}} = 20\,\mathrm{ms}$, $R = 100\,\mathrm{M\Omega}$, threshold $-50\,\mathrm{mV}$, reset $-65\,\mathrm{mV}$; currents $0.200$ and $0.205\,\mathrm{nA}$; a spike is represented by $1\,\mathrm{ms}$ at $+20\,\mathrm{mV}$). A: without coupling the faster neuron 2 (red) drifts relative to neuron 1 (blue). B: with $g_{\mathrm{c}} = 2\,\mathrm{nS}$ (steady coupling coefficient $0.17$) the spikes lock after about ten cycles. C: phase of neuron 2 relative to neuron 1 at each spike of neuron 1: it slides through all values without coupling (gray) and converges to a nearly synchronous state with coupling (green).](./plots/gap-junction-sync.py)

## 12.5. Short-Term Plasticity: The Tsodyks–Markram Model

### 12.5.1. Resources and Utilization

The phenomena of [7.16.9](/7.16.9#sec-9.6), facilitation from residual $\ce{Ca^2+}$ and depression from depletion of the **readily releasable pool**, can be captured by two variables per synapse.

**Definition 12.5.1 (Short-Term Synaptic Plasticity)** **Short-term synaptic plasticity** is the change of the efficacy of a synapse, by synaptic facilitation or synaptic depression (Definition 9.6.2), that depends on the presynaptic spikes of the preceding tens of milliseconds to seconds and decays back to baseline without lasting change.

**Definition 12.5.2 (Tsodyks–Markram Model)** In the **Tsodyks–Markram model** a synapse has a fraction $x \in [0, 1]$ of available resources (vesicles ready for release) and a utilization $u \in [0, 1]$ (the release probability of an available resource). Between spikes $u$ decays to zero with time constant $\tau_{\mathrm{f}}$ and $x$ recovers to one with time constant $\tau_{\mathrm{d}}$; at each presynaptic spike $u$ first increases and then the fraction $u x$ of the resources is released:
$$
\frac{\mathrm{d}u}{\mathrm{d}t} = -\frac{u}{\tau_{\mathrm{f}}} + U(1 - u^-)\sum_k\delta(t - t_k), \qquad
\frac{\mathrm{d}x}{\mathrm{d}t} = \frac{1 - x}{\tau_{\mathrm{d}}} - u^+x^-\sum_k\delta(t - t_k), \tag{12.7}
$$
where $u^-, x^-$ are the values just before and $u^+ = u^- + U(1 - u^-)$ the value just after the jump. The postsynaptic response to spike $k$ is $A\,u^+x^-$, with $A$ the response if all resources were released; it is usually fed into one of the kernels of Definition 12.2.2.

The parameter $U$ is the increment of $u$ per spike and also the release probability of the first spike after a long silence ($u^- = 0$, $x^- = 1$, response $AU$). The model is Eq. (9.5) made dynamic: for two spikes an interval $\Delta t$ apart it gives
$$
\mathrm{PPR} = \left(1 + (1 - U)\,\mathrm{e}^{-\Delta t/\tau_{\mathrm{f}}}\right)\left(1 - U\,\mathrm{e}^{-\Delta t/\tau_{\mathrm{d}}}\right), \tag{12.8}
$$
which is Eq. (9.5) with $p = f = U$, $\tau_{\mathrm{F}} = \tau_{\mathrm{f}}$ and $\tau_{\mathrm{rec}} = \tau_{\mathrm{d}}$. (In the original formulation of Tsodyks and Markram (1997) for depressing synapses $u = U$ was fixed; the facilitating variable was added by Markram, Wang and Tsodyks (1998). Some papers order the jumps differently, which changes the formulas slightly but not the behavior.)

Two regimes are distinguished by the parameters. *Depression-dominated* synapses have large $U$ and $\tau_{\mathrm{d}} \gg \tau_{\mathrm{f}}$; fits to connections between layer 5 pyramidal cells give $U \approx 0.5$, $\tau_{\mathrm{d}} \approx 800\,\mathrm{ms}$, $\tau_{\mathrm{f}} \lesssim 20\,\mathrm{ms}$. *Facilitation-dominated* synapses have small $U$ and $\tau_{\mathrm{f}} \gg \tau_{\mathrm{d}}$, for example pyramidal cell to bitufted interneuron connections and many synapses in the prefrontal cortex, with $U \approx 0.1$, $\tau_{\mathrm{d}} \approx 200\,\mathrm{ms}$ and $\tau_{\mathrm{f}} \approx 1.5\,\mathrm{s}$. Sensory cortices are dominated by depressing excitatory synapses, the prefrontal cortex has many facilitating ones, a difference that the working-memory model of Mongillo, Barak and Tsodyks (2008) exploits ([7.16.45](/7.16.45)).

**Example 12.5.1** For the depressing parameters and a $20\,\mathrm{Hz}$ train ($\Delta t = 50\,\mathrm{ms}$), Eq. (12.8) gives $(1 + 0.5\,\mathrm{e}^{-2.5})(1 - 0.5\,\mathrm{e}^{-0.0625}) = 1.041\cdot0.530 = 0.55$; for the facilitating parameters $(1 + 0.9\,\mathrm{e}^{-1/30})(1 - 0.1\,\mathrm{e}^{-0.25}) = 1.871\cdot0.922 = 1.72$. The first synapse halves its second response, the second synapse almost doubles it, although both consume part of their resources with every spike.

:::

The model is simulated event by event. Between spikes both variables relax exponentially, so the update from one spike to the next is exact:

```python
import numpy as np


def tsodyks_markram(spike_times, U, tau_d, tau_f):
    """Return the efficacy u+ x- of each spike (fraction of resources released)."""
    u, x, t_last = 0.0, 1.0, None
    out = []
    for t in spike_times:
        if t_last is not None:
            dt = t - t_last
            u *= np.exp(-dt / tau_f)                   # facilitation decays
            x = 1.0 - (1.0 - x) * np.exp(-dt / tau_d)  # resources recover
        u = u + U * (1.0 - u)                          # spike raises utilization
        out.append(u * x)                              # released fraction
        x -= u * x                                     # resources consumed
        t_last = t
    return np.array(out)
```

![Responses of the Tsodyks–Markram model (Definition 12.5.2) to ten spikes at $20$ and $50\,\mathrm{Hz}$ followed by a test spike $500\,\mathrm{ms}$ later. Dots: efficacy $u^+x^-$ of each spike, normalized to the first response of the depressing synapse; lines: the postsynaptic currents with a $3\,\mathrm{ms}$ exponential kernel. Top: a depressing synapse ($U = 0.5$, $\tau_{\mathrm{d}} = 800\,\mathrm{ms}$, $\tau_{\mathrm{f}} = 20\,\mathrm{ms}$) depresses to a steady level that is lower at $50\,\mathrm{Hz}$ and recovers only half way within $500\,\mathrm{ms}$. Bottom: a facilitating synapse ($U = 0.1$, $\tau_{\mathrm{d}} = 200\,\mathrm{ms}$, $\tau_{\mathrm{f}} = 1500\,\mathrm{ms}$) grows during the first spikes, then depression catches up; the test spike is larger than any response of the train, because the resources have recovered while the utilization is still elevated.](./plots/tsodyks-markram.py)

### 12.5.2. Steady State and Frequency Dependence

For a regular train with interval $\Delta = 1/r$, the values just after and just before each spike converge to fixed points of the spike-to-spike map:
$$
u^+_\infty = \frac{U}{1 - (1 - U)\,\mathrm{e}^{-\Delta/\tau_{\mathrm{f}}}}, \qquad
x^-_\infty = \frac{1 - \mathrm{e}^{-\Delta/\tau_{\mathrm{d}}}}{1 - (1 - u^+_\infty)\,\mathrm{e}^{-\Delta/\tau_{\mathrm{d}}}}. \tag{12.9}
$$
The first follows from $u^+_{n+1} = U + (1 - U)\,u^+_n\,\mathrm{e}^{-\Delta/\tau_{\mathrm{f}}}$, the second from $x^-_{n+1} = 1 - \bigl(1 - (1 - u^+)x^-_n\bigr)\mathrm{e}^{-\Delta/\tau_{\mathrm{d}}}$, by setting successive values equal.

**Proposition 12.5.1 (Saturation of Depressing Synapses)** At high rates ($\Delta \ll \tau_{\mathrm{d}}$) the steady efficacy per spike of Eq. (12.9) behaves as $u^+_\infty x^-_\infty \approx 1/(r\tau_{\mathrm{d}})$, so the transmitted rate $r\,u^+_\infty x^-_\infty$ approaches $1/\tau_{\mathrm{d}}$, independent of the presynaptic rate.

**Proof** For $\Delta \ll \tau_{\mathrm{d}}$, $1 - \mathrm{e}^{-\Delta/\tau_{\mathrm{d}}} \approx \Delta/\tau_{\mathrm{d}}$ and the denominator of $x^-_\infty$ tends to $u^+_\infty$, so $x^-_\infty \approx \Delta/(\tau_{\mathrm{d}}u^+_\infty)$ and $u^+_\infty x^-_\infty \approx \Delta/\tau_{\mathrm{d}}$. Multiplying by $r = 1/\Delta$ gives $1/\tau_{\mathrm{d}}$. $\square$

The proposition expresses a resource balance: in the steady state as many resources are released per second as recover, and recovery cannot exceed $1/\tau_{\mathrm{d}}$ per second. Above a limiting frequency of order $1/(U\tau_{\mathrm{d}})$, a few hertz for a depressing cortical synapse, the postsynaptic current no longer reports the presynaptic rate. A facilitating synapse obeys the same limit, but because its efficacy first rises with rate, it transmits best in a band of frequencies and acts as a band-pass filter, while a depressing synapse acts as a low-pass filter for efficacy and a high-pass filter for changes of rate (figure below).

![Steady-state transmission in the Tsodyks–Markram model (Eq. (12.9); parameters as in the previous figure). A: efficacy per spike against the rate of a regular train: the depressing synapse (red) falls monotonically, the facilitating synapse (blue) is most effective near $5\,\mathrm{Hz}$. B: transmitted rate $r\,u^+_\infty x^-_\infty$ (released resources per second): the depressing synapse saturates at $1/\tau_{\mathrm{d}} = 1.25\,\mathrm{s^{-1}}$ (dashed, Proposition 12.5.1) above a few hertz, the facilitating synapse saturates at its own, larger $1/\tau_{\mathrm{d}}$ only above about $20\,\mathrm{Hz}$.](./plots/stp-frequency.py)

### 12.5.3. Depression as Gain Control

Saturation has a useful consequence (Abbott, Varela, Sen and Nelson, 1997). If the rate of a depressing input steps from $r_0$ to $r_1$, the efficacy per spike is at first still the steady value for $r_0$, approximately $1/(r_0\tau_{\mathrm{d}})$, while spikes now arrive at $r_1$: the transmitted rate jumps by the factor $r_1/r_0$, then relaxes back to $1/\tau_{\mathrm{d}}$ as the resources readjust. The transient therefore reports the *relative* change of rate, the same for a step from 10 to 20 Hz as from 50 to 100 Hz. A neuron that receives many depressing inputs at different rates is thus equally sensitive to a doubling of any of them, a form of **Weber–Fechner law** at the level of synapses, and the synapse adapts to the mean rate of its input. The same mechanism explains part of the adaptation of cortical responses to sustained stimuli and of the sensitivity to novel stimuli.

![Gain control by a depressing synapse ($U = 0.5$, $\tau_{\mathrm{d}} = 800\,\mathrm{ms}$, $\tau_{\mathrm{f}} = 20\,\mathrm{ms}$). A, B: transmitted rate (release per spike times the instantaneous rate), normalized to its value before the presynaptic rate doubles at $t = 0$, for a step from $10$ to $20\,\mathrm{Hz}$ (A) and from $50$ to $100\,\mathrm{Hz}$ (B): the transient reaches 2 in both cases and decays back to nearly the same steady value. C: the peak of the transient against the ratio $r_1/r_0$ for both starting rates: the points lie on the identity line, so the synapse signals relative changes.](./plots/stp-gain-control.py)

### 12.5.4. What Short-Term Plasticity Computes

Short-term plasticity turns every synapse into a dynamic filter whose properties are set by the identity of the pre- and postsynaptic cells. Among the computational roles that have been proposed and tested in models are: detection of transients and of the onset of bursts (depression); selective transmission of bursts (facilitation), which makes bursts a separate channel of information; gain control and adaptation (12.5.3); decorrelation of input trains; and storage of information for about a second in the facilitation variable $u$ without persistent firing, the "activity-silent" working memory of [7.16.45](/7.16.45). Because $u$ and $x$ change the effective connectivity of a network on the time scale of hundreds of milliseconds, networks with dynamic synapses can show transient population bursts and slow oscillations that static networks do not.

## 12.6. Synapses on an Integrate-and-Fire Neuron

The postsynaptic membrane integrates the synaptic conductance. With a current-based exponential synapse of time constant $\tau_{\mathrm{s}}$ on a passive membrane with time constant $\tau_{\mathrm{m}}$, a single spike gives the postsynaptic potential
$$
V(t) - E_{\mathrm{L}} = \frac{R_{\mathrm{in}}Q}{\tau_{\mathrm{m}} - \tau_{\mathrm{s}}}\left(\mathrm{e}^{-t/\tau_{\mathrm{m}}} - \mathrm{e}^{-t/\tau_{\mathrm{s}}}\right), \qquad t \ge 0, \tag{12.10}
$$
where $Q$ is the total charge, the **convolution** of the synaptic current with the impulse response of the membrane. The PSP is a difference of exponentials whose decay is set by the slower of the two time constants, usually the membrane. Successive PSPs add as long as they arrive within about $\tau_{\mathrm{m}}$ of each other: the **membrane time constant** defines the window of **temporal summation** ([7.14.5](/7.14.5#sec-5.3.2)).

In a conductance-based model this window is not fixed. The total conductance in Eq. (12.2) is $g_{\mathrm{tot}}(t) = g_{\mathrm{L}} + \sum_j\bar g_js_j(t)$, and around any operating point the membrane relaxes with the effective time constant
$$
\tau_{\mathrm{eff}} = \frac{C_{\mathrm{m}}}{g_{\mathrm{tot}}} = \frac{\tau_{\mathrm{m}}}{1 + \sum_j\bar g_js_j/g_{\mathrm{L}}}. \tag{12.11}
$$
In vivo, cortical neurons bombarded by thousands of excitatory and inhibitory inputs have a total conductance three to five times their resting value (the "high-conductance state", Destexhe, Rudolph and Paré, 2003). Their effective time constant is then a few milliseconds instead of $20\,\mathrm{ms}$, PSPs are smaller and briefer (figure in 12.2), and the neuron behaves more like a coincidence detector than like an integrator: background activity sets how a neuron integrates, not only how close it is to threshold. Current-based models miss this effect, which is one reason network models increasingly use conductance-based synapses.

## Summary

- A synapse enters the postsynaptic membrane equation as $I_{\mathrm{syn}} = \bar g_{\mathrm{syn}}s(t)(V - E_{\mathrm{syn}})$ (conductance-based) or with a fixed driving force (current-based, Definition 12.2.1).
- Phenomenological kernels (Definition 12.2.2) prescribe $s(t)$ after each spike; each is the impulse response of a small linear system, simulated by jumps at spikes and relaxation between them.

| Model | Variables | Captures | Misses |
|---|---|---|---|
| Delta, exponential kernel | $s$ | Amplitude, decay | Rise time, saturation |
| Alpha, difference of exponentials | $s, x$ | Rise and decay | Saturation, history |
| First-order kinetics (Formula 12.3.1) | $s$ | Saturation | Desensitization |
| Saturating NMDA (Formula 12.3.2) | $s, x$ and $B(V)$ | Slow integration, coincidence detection | Receptor subtypes |
| Gap junction, Eq. (12.6) | none | Bidirectional coupling, synchrony | Rectification |
| Tsodyks–Markram (Definition 12.5.2) | $u, x$ | Facilitation, depression | Slow forms (PTP), postsynaptic effects |

- In the Tsodyks–Markram model, $U$, $\tau_{\mathrm{d}}$ and $\tau_{\mathrm{f}}$ determine whether a synapse depresses or facilitates; the **paired-pulse ratio** is Eq. (12.8) and the steady state Eq. (12.9).
- Depressing synapses saturate at a transmitted rate $1/\tau_{\mathrm{d}}$ (Proposition 12.5.1) and therefore signal relative changes of rate (gain control); facilitating synapses act as band-pass filters.
- Gap junctions synchronize coupled neurons; synaptic conductances shorten the effective time constant (Eq. (12.11)) and narrow the window of temporal summation.

## Questions

1. Show that the alpha function $K(t) = (t/\tau_{\mathrm{s}})\mathrm{e}^{1 - t/\tau_{\mathrm{s}}}$ is the response of the system in Definition 12.2.2 to one spike at $t = 0$, and that it is the limit of the normalized difference of exponentials as $\tau_{\mathrm{r}} \to \tau_{\mathrm{d}}$.

   **Answer** After the spike $x(t) = \mathrm{e}\,\mathrm{e}^{-t/\tau_{\mathrm{s}}}$. Then $\tau_{\mathrm{s}}\dot s + s = \mathrm{e}\,\mathrm{e}^{-t/\tau_{\mathrm{s}}}$ with $s(0) = 0$; multiplying by $\mathrm{e}^{t/\tau_{\mathrm{s}}}/\tau_{\mathrm{s}}$ gives $\frac{\mathrm{d}}{\mathrm{d}t}(s\,\mathrm{e}^{t/\tau_{\mathrm{s}}}) = \mathrm{e}/\tau_{\mathrm{s}}$, so $s = (\mathrm{e}\,t/\tau_{\mathrm{s}})\mathrm{e}^{-t/\tau_{\mathrm{s}}}$. For the second statement set $\tau_{\mathrm{r}} = \tau_{\mathrm{d}} - \varepsilon$: $\mathrm{e}^{-t/\tau_{\mathrm{r}}} \approx \mathrm{e}^{-t/\tau_{\mathrm{d}}} - \varepsilon\,(t/\tau_{\mathrm{d}}^2)\,\mathrm{e}^{-t/\tau_{\mathrm{d}}}$, so the difference of exponentials is $\varepsilon\,(t/\tau_{\mathrm{d}}^2)\,\mathrm{e}^{-t/\tau_{\mathrm{d}}}$, proportional to $t\,\mathrm{e}^{-t/\tau_{\mathrm{d}}}$; normalizing the peak (at $t = \tau_{\mathrm{d}}$) to 1 gives the alpha function. The peak-time formula also tends to $\tau_{\mathrm{d}}$.

2. A depressing synapse with $U = 0.5$, $\tau_{\mathrm{d}} = 800\,\mathrm{ms}$ and negligible facilitation ($\tau_{\mathrm{f}} \to 0$, so $u^+ = U$) is driven at $40\,\mathrm{Hz}$. Compute the steady efficacy per spike and compare the transmitted rate with $1/\tau_{\mathrm{d}}$.

   **Answer** With $u^+ = U$, $\Delta = 25\,\mathrm{ms}$ and $\mathrm{e}^{-\Delta/\tau_{\mathrm{d}}} = \mathrm{e}^{-0.03125} = 0.9692$: $x^-_\infty = 0.0308/(1 - 0.5\cdot0.9692) = 0.0308/0.5154 = 0.0597$, efficacy $Ux^- = 0.030$, which is $6\%$ of the first response. The transmitted rate is $40\cdot0.030 = 1.19\,\mathrm{s^{-1}}$, close to $1/\tau_{\mathrm{d}} = 1.25\,\mathrm{s^{-1}}$; at $10\,\mathrm{Hz}$ the same calculation gives $x^- = 0.1175/(1 - 0.5\cdot0.8825) = 0.210$, efficacy $0.105$, rate $1.05\,\mathrm{s^{-1}}$: quadrupling the input rate increases the output by only 13%.

3. Two neurons with membrane capacitance $100\,\mathrm{pF}$ and leak conductance $5\,\mathrm{nS}$ receive a tonic excitatory conductance of $10\,\mathrm{nS}$ and a tonic inhibitory conductance of $10\,\mathrm{nS}$ in one condition and none in the other. Compute $\tau_{\mathrm{eff}}$ in both conditions and the width of the window of temporal summation. What does this imply for the integration of synchronous versus asynchronous inputs?

   **Answer** At rest $\tau_{\mathrm{m}} = 100\,\mathrm{pF}/5\,\mathrm{nS} = 20\,\mathrm{ms}$; with background $\tau_{\mathrm{eff}} = 100/(5 + 20) = 4\,\mathrm{ms}$ (Eq. (12.11)). PSPs now decay five times faster and are five times smaller for the same synaptic current. Inputs must arrive within a few milliseconds of each other to summate, so the neuron responds preferentially to synchronous input; asynchronous inputs spread over $20\,\mathrm{ms}$, which would summate at rest, no longer reach threshold together. Background activity thus switches the neuron from integration toward coincidence detection.

4. (Open question) Design an experiment and an analysis that determine $U$, $\tau_{\mathrm{d}}$ and $\tau_{\mathrm{f}}$ for a cortical connection recorded in a paired recording.

   **Answer** Stimulate the presynaptic neuron with trains of 8–10 spikes at several frequencies (for example 10, 20, 40 Hz), each followed by a recovery test spike at several delays (0.1–2 s), and repeat each protocol many times to average the stochastic responses. Fit the model of Definition 12.5.2 (with a free amplitude $A$) to all averaged amplitudes jointly by least squares. The first-response amplitude fixes $AU$; the paired-pulse ratios at short intervals constrain $U$ and $\tau_{\mathrm{f}}$ (Eq. (12.8)); the steady-state levels at different frequencies (Eq. (12.9)) and the recovery curve constrain $\tau_{\mathrm{d}}$. Parameters are identifiable only with several frequencies, because a single train can be fitted by different combinations; check the fit by predicting responses to irregular (Poisson) trains not used in the fit, as Markram and Tsodyks did.
