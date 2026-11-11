---
title: Simplified Spiking Neuron Models
description: "Integrate-and-fire models as reductions of conductance-based neurons: the leaky integrate-and-fire model with its analytic f–I curve, rheobase and refractory period; the quadratic integrate-and-fire model as the normal form of a saddle-node on invariant circle and the theta neuron; the exponential integrate-and-fire model; adaptation in the AdEx and Izhikevich models and the firing patterns of cortical cell types; noise-driven firing, the Ornstein–Uhlenbeck approximation, the Siegert formula and the irregularity of cortical spike trains; how to choose a model."
---

A network of $10^5$ Hodgkin–Huxley neurons, each needing a time step of $0.01\,\mathrm{ms}$, is expensive to simulate and impossible to analyze. Most questions about networks, however, depend only on *when* neurons fire, not on the shape of each **action potential**, which is stereotyped. The models of this chapter keep the subthreshold dynamics that decide the timing of spikes and replace the spike itself by an event: when the voltage crosses a threshold, a spike is registered and the voltage is reset. The bifurcation theory of [7.16.6](/7.16.6) and [7.16.7](/7.16.7) tells us which features of the subthreshold dynamics must be kept to preserve the neuron's computational class.

The chapter proceeds from the simplest model, the leaky integrate-and-fire neuron, through models with a nonlinear spike initiation and an adaptation variable, to noise-driven neurons, and ends with a guide to choosing a model. The firing-rate models used for networks are derived from these spiking models in [7.16.15](/7.16.15).

## 8.1. Why Simplify

Three reasons motivate simplified models.

1. *Cost.* Izhikevich (2004) estimated the cost of simulating 1 ms of activity at about 1200 floating-point operations for the HH model, 13 for his two-variable model (Section 8.4) and 5 for the leaky integrate-and-fire model. Large-scale simulations and neuromorphic chips ([7.16.50](/7.16.50)) use the cheap models.
2. *Analysis.* Integrate-and-fire models have closed-form f–I curves, response functions and, with noise, firing statistics; mean-field theories of networks are built on them.
3. *Fitting.* Two-variable models with a few parameters can be fitted to recordings from a neuron and predict the timing of its spikes in response to new inputs as well as a detailed model; in competitions of spike-time prediction, adaptive integrate-and-fire models predicted a large fraction of the spikes of cortical neurons to within a few milliseconds (Jolivet et al. 2008).

What is lost is the mechanism: integrate-and-fire models have no ionic currents and cannot answer questions about channels, drugs or the shape of the spike, and their threshold-and-reset rule is a caricature of the geometry of [7.16.6](/7.16.6#sec-6.2).

## 8.2. The Leaky Integrate-and-Fire Model

### 8.2.1. Definition and the f–I Curve

Below threshold, the membrane of a neuron behaves approximately as the RC circuit of [7.16.4](/7.16.4#sec-4.4). The leaky integrate-and-fire model takes this literally.

**Definition 8.2.1 (Leaky Integrate-and-Fire Model)** The **leaky integrate-and-fire model** (LIF) describes the membrane potential by

$$
\tau_{\mathrm{m}}\frac{\mathrm{d}V}{\mathrm{d}t} = -(V - E_{\mathrm{L}}) + R\,I(t), \qquad V < V_{\mathrm{th}},
$$

where $\tau_{\mathrm{m}}$ is the membrane time constant and $R$ the input resistance; when $V$ reaches $V_{\mathrm{th}}$ a spike is emitted, $V$ is reset to $V_{\mathrm{reset}}$ and held there for an absolute refractory period $\tau_{\mathrm{ref}}$.

The model goes back to Lapicque (1907), who used it to describe the strength–duration relation of nerve stimulation. For a constant current $I$ the subthreshold solution starting from $V_{\mathrm{reset}}$ is $V(t) = E_{\mathrm{L}} + RI + (V_{\mathrm{reset}} - E_{\mathrm{L}} - RI)\,\mathrm{e}^{-t/\tau_{\mathrm{m}}}$, which approaches $E_{\mathrm{L}} + RI$. The neuron fires only if this asymptote lies above threshold.

**Definition 8.2.2 (Rheobase)** The **rheobase** is the smallest constant current that makes a neuron fire; for the LIF neuron it is $I_{\mathrm{th}} = (V_{\mathrm{th}} - E_{\mathrm{L}})/R$.

**Proposition 8.2.1 (f–I Curve of the LIF Neuron)** For a constant current $I > I_{\mathrm{th}}$ the LIF neuron fires periodically with rate

$$
r(I) = \left[\tau_{\mathrm{ref}} + \tau_{\mathrm{m}}\ln\frac{RI + E_{\mathrm{L}} - V_{\mathrm{reset}}}{RI + E_{\mathrm{L}} - V_{\mathrm{th}}}\right]^{-1}, \tag{8.1}
$$

and $r = 0$ for $I \le I_{\mathrm{th}}$.

**Proof** Setting $V(T) = V_{\mathrm{th}}$ in the solution above and solving for $T$ gives the time from reset to threshold, $T = \tau_{\mathrm{m}}\ln[(RI + E_{\mathrm{L}} - V_{\mathrm{reset}})/(RI + E_{\mathrm{L}} - V_{\mathrm{th}})]$. The interspike interval is $T + \tau_{\mathrm{ref}}$, and the rate is its inverse. $\square$

Three features of Eq. (8.1) are worth noting (Figure 1B). Near the rheobase the logarithm diverges, so the rate starts from zero: the LIF neuron is a class 1 neuron. The divergence is only logarithmic, however, so the rate rises extremely steeply above $I_{\mathrm{th}}$, unlike the square-root onset of real class 1 neurons near a **SNIC**. For large currents $\ln(1 + x) \approx x$ gives $r \approx RI/[\tau_{\mathrm{m}}(V_{\mathrm{th}} - V_{\mathrm{reset}})]$ without refractoriness, a linear f–I curve, and with refractoriness the rate saturates at $1/\tau_{\mathrm{ref}}$.

**Example 8.2.1 (A Cortical LIF Neuron)** With $E_{\mathrm{L}} = V_{\mathrm{reset}} = -65\,\mathrm{mV}$, $V_{\mathrm{th}} = -50\,\mathrm{mV}$, $\tau_{\mathrm{m}} = 10\,\mathrm{ms}$ and $R = 10\,\mathrm{M\Omega}$, the rheobase is $15\,\mathrm{mV}/10\,\mathrm{M\Omega} = 1.5\,\mathrm{nA}$. For $I = 2\,\mathrm{nA}$, $RI = 20\,\mathrm{mV}$ and $T = 10\ln(20/5) = 13.9\,\mathrm{ms}$; with $\tau_{\mathrm{ref}} = 2\,\mathrm{ms}$ the rate is $1000/15.9 = 63\,\mathrm{Hz}$ (Figure 1A).

:::

### 8.2.2. Time-Varying Input

For a time-varying current the subthreshold LIF is a linear filter: $V(t) - E_{\mathrm{L}}$ is the convolution of $RI(t)$ with the exponential kernel $\mathrm{e}^{-t/\tau_{\mathrm{m}}}/\tau_{\mathrm{m}}$, a low-pass filter with cutoff $1/(2\pi\tau_{\mathrm{m}})$ ([7.16.4](/7.16.4#sec-4.4)). A sinusoidal current $I(t) = I_0 + I_1\sin(2\pi f t)$ with $I_0$ below rheobase therefore produces spikes near the peaks of the sine when $f$ is low, but the voltage modulation, and with it the firing, is attenuated at frequencies well above $1/(2\pi\tau_{\mathrm{m}}) = 16\,\mathrm{Hz}$. When $I_0$ is above rheobase, the neuron fires periodically and the sinusoidal input locks the spikes to particular phases, a phenomenon analyzed with **phase response curves** in [7.16.15](/7.16.15). The deterministic LIF thus transmits slow signals well and fast ones poorly; noise improves the transmission of fast signals, as Section 8.5 shows.

## 8.3. Nonlinear Integrate-and-Fire Models

### 8.3.1. The Quadratic Model and the Theta Neuron

The LIF has no spike initiation: the voltage approaches threshold with decreasing slope, and the threshold is an imposed rule. In real neurons, and in the models of [7.16.6](/7.16.6), the $\ce{Na+}$ current makes $\mathrm{d}V/\mathrm{d}t$ increase again above a certain voltage, and the "threshold" is the unstable equilibrium where it changes sign. The simplest model with this property is the normal form of the saddle-node bifurcation ([7.16.7](/7.16.7#sec-7.1)).

**Definition 8.3.1 (Quadratic Integrate-and-Fire Model)** The **quadratic integrate-and-fire model** (QIF) is

$$
\tau_{\mathrm{m}}\frac{\mathrm{d}V}{\mathrm{d}t} = a\,(V - E_{\mathrm{L}})(V - V_{\mathrm{c}}) + R\,I, \qquad V \le V_{\mathrm{peak}},
$$

with $a > 0$ and a critical voltage $V_{\mathrm{c}} > E_{\mathrm{L}}$; when $V$ reaches $V_{\mathrm{peak}}$ it is reset to $V_{\mathrm{reset}}$.

At $I = 0$ the model has a stable rest state at $E_{\mathrm{L}}$ and an unstable equilibrium at $V_{\mathrm{c}}$, the threshold (Figure 1C). As $I$ increases they merge in a saddle-node bifurcation, and above it $V$ escapes to infinity in finite time; the reset then closes the orbit into a cycle, so the model is a SNIC in canonical form. In dimensionless form $\dot x = x^2 + I$, the time to go from $-\infty$ to $+\infty$ is $\pi/\sqrt{I}$ (Question 1 of [7.16.6](/7.16.6)), so the rate rises as $\sqrt{I - I_{\mathrm{c}}}$, the correct class 1 onset. The substitution $x = \tan(\theta/2)$ maps the line, with $\pm\infty$ identified, onto a circle and gives the *theta neuron* of Ermentrout and Kopell (1986),

$$
\frac{\mathrm{d}\theta}{\mathrm{d}t} = (1 - \cos\theta) + (1 + \cos\theta)\,I,
$$

in which a spike is the passage of $\theta$ through $\pi$. Because every model near a SNIC can be transformed into this form, the theta neuron is the canonical class 1 neuron, and results proved for it (such as its phase response curve, proportional to $1 - \cos(2\pi\phi)$ with the phase $\phi$ measured from the last spike) hold for all such neurons near the onset of firing.

### 8.3.2. The Exponential Model

The quadratic nonlinearity is the leading term of the $\ce{Na+}$ current near the saddle-node; further from it, the activation of $\ce{Na+}$ channels is better described by an exponential, which is the shape of the foot of the Boltzmann activation curve.

**Definition 8.3.2 (Exponential Integrate-and-Fire Model)** The **exponential integrate-and-fire model** (ExpIF) is

$$
\tau_{\mathrm{m}}\frac{\mathrm{d}V}{\mathrm{d}t} = -(V - E_{\mathrm{L}}) + \Delta_T\,\mathrm{e}^{(V - V_T)/\Delta_T} + R\,I,
$$

with a spike-initiation threshold $V_T$ and a slope factor $\Delta_T$ that measures the sharpness of spike initiation; $V$ is reset when it reaches a peak value (for instance 0 mV).

For $\Delta_T \to 0$ the ExpIF becomes the LIF with threshold $V_T$; for larger $\Delta_T$ the voltage accelerates gradually toward the spike (Figure 1D). The model was introduced by Fourcaud-Trocmé, Hansel, van Vreeswijk and Brunel (2003), who showed that it reproduces the response of conductance-based neurons to fast inputs much better than the LIF. The function $F(V)$ on the right-hand side can be measured directly in a neuron by injecting noisy current and plotting the average $\mathrm{d}V/\mathrm{d}t$ against $V$ (the "dynamic I–V curve"): in cortical pyramidal neurons it is well fitted by the exponential form with a slope factor $\Delta_T$ of one to a few millivolts (Badel et al. 2008).

![Integrate-and-fire models. A: a LIF neuron ($E_\mathrm{L} = V_\mathrm{reset} = -65$ mV, $V_\mathrm{th} = -50$ mV, $\tau_\mathrm{m} = 10$ ms, $R = 10$ MΩ, $\tau_\mathrm{ref} = 2$ ms) during a 2 nA current step: the voltage charges toward $E_\mathrm{L} + RI = -45$ mV and is reset each time it reaches threshold (spikes drawn as vertical lines). B: f–I curves from Eq. (8.1) (lines) and from simulation (dots) without and with a 5 ms refractory period; the rheobase is 1.5 nA, and the refractory period makes the curve saturate. C: the right-hand side $F(V)$ at $I = 0$ for the LIF, ExpIF ($V_T = -55$ mV, $\Delta_T = 2$ mV) and QIF models: the nonlinear models have a second, unstable zero, the threshold. D: the first spike of an ExpIF neuron after a 1.8 nA step for three values of $\Delta_T$: a smaller slope factor gives a sharper spike onset](./plots/lif.py)

## 8.4. Adaptation and Firing Patterns

### 8.4.1. Two-Variable Models

One-variable integrate-and-fire models fire regularly at a rate determined by the current. Real neurons adapt, burst, and fire after a delay, and these patterns require a second, slower variable, the counterpart of the slow $\ce{K+}$ currents of [7.16.5](/7.16.5#sec-5.4). Two models are widely used.

**Definition 8.4.1 (Adaptive Exponential Integrate-and-Fire Model)** The **adaptive exponential integrate-and-fire model** (AdEx; Brette and Gerstner 2005) is

$$
C\frac{\mathrm{d}V}{\mathrm{d}t} = -g_{\mathrm{L}}(V - E_{\mathrm{L}}) + g_{\mathrm{L}}\Delta_T\,\mathrm{e}^{(V - V_T)/\Delta_T} - w + I,
\qquad
\tau_w\frac{\mathrm{d}w}{\mathrm{d}t} = a\,(V - E_{\mathrm{L}}) - w,
$$

and at each spike $V \to V_{\mathrm{reset}}$, $w \to w + b$. The adaptation current $w$ has a subthreshold coupling $a$ (a conductance, like a slow voltage-gated current) and a spike-triggered increment $b$ (like a $\ce{Ca^2+}$-activated $\ce{K+}$ current).

**Definition 8.4.2 (Izhikevich Model)** The **Izhikevich model** (Izhikevich 2003) is the quadratic model with a linear recovery variable $u$, in dimensionless units with $v$ in mV and $t$ in ms:

$$
\frac{\mathrm{d}v}{\mathrm{d}t} = 0.04\,v^2 + 5\,v + 140 - u + I, \qquad \frac{\mathrm{d}u}{\mathrm{d}t} = a\,(b\,v - u),
$$

and when $v \ge 30\,\mathrm{mV}$: $v \to c$, $u \to u + d$. The four parameters are the rate $a$ of the recovery variable, its sensitivity $b$ to subthreshold voltage, the reset voltage $c$ and the spike-triggered increment $d$.

The quadratic $0.04v^2 + 5v + 140$ was fitted to the spike initiation of cortical neurons so that $v$ is in millivolts and the rest state is near $-70\,\mathrm{mV}$. In both models, the subthreshold coupling ($a$ in AdEx, $b$ in the Izhikevich model) determines whether the rest state is a node or a focus, and thus whether the model is an **integrator** or a **resonator** ([7.16.6](/7.16.6#sec-6.5)); a large spike-triggered increment produces adaptation; a high reset produces bursts.

### 8.4.2. Firing Patterns of Cortical Neurons

With different values of $(a, b, c, d)$ the Izhikevich model reproduces the main electrophysiological classes of cortical and thalamic neurons (Figure 2).

| Class | $a$ | $b$ | $c$ / mV | $d$ | Behavior | Cell type ([7.16.2](/7.16.2#sec-2.1)) |
|---|---|---|---|---|---|---|
| regular spiking (RS) | 0.02 | 0.2 | $-65$ | 8 | strong adaptation | most excitatory pyramidal cells |
| intrinsically bursting (IB) | 0.02 | 0.2 | $-55$ | 4 | initial burst, then single spikes | layer 5 pyramidal cells |
| chattering (CH) | 0.02 | 0.2 | $-50$ | 2 | repetitive bursts at 20–40 Hz | layer 2/3 pyramidal cells |
| fast spiking (FS) | 0.1 | 0.2 | $-65$ | 2 | high rate, little late adaptation | PV interneurons |
| low-threshold spiking (LTS) | 0.02 | 0.25 | $-65$ | 2 | adapting, rebound | SST interneurons |
| thalamocortical (TC) | 0.02 | 0.25 | $-65$ | 0.05 | tonic when depolarized, rebound burst after hyperpolarization | thalamic relay neurons |

The mechanisms can be read from the $(v, u)$ plane (Figure 2, bottom). In RS neurons the large $d$ raises $u$ after each spike, so the next approach to threshold is slower, and the rate falls from about 55 Hz to a steady 20 Hz within two spikes. In IB and CH neurons the reset $c$ is high: after the first spikes $v$ is reset above the minimum of the parabolic $v$-nullcline and fires again at once, until the accumulated $u$ pushes the trajectory below it; the CH neuron, with the highest reset and the smallest $d$, repeats this cycle and fires bursts. FS neurons have a fast recovery variable ($a = 0.1$), which forgets the past within 10 ms and allows high sustained rates. The TC parameters ($b = 0.25$, tiny $d$) make $u$ follow $v$ in the subthreshold range, so that hyperpolarization lowers $u$ and its release produces a rebound burst, the integrate-and-fire analog of $I_{\mathrm{T}}$ de-inactivation.

![Firing patterns of the Izhikevich model. Top and middle rows: responses to a current step (grey trace, $I = 10$ from 20 ms) for parameters of regular spiking (RS), intrinsically bursting (IB), chattering (CH), fast spiking (FS) and low-threshold spiking (LTS) neurons; for the thalamocortical (TC) neuron the cell is held hyperpolarized ($I = -10$) and released, which evokes a rebound burst. Bottom row: the $(v, u)$ plane of RS and IB neurons with the parabolic $v$-nullcline at $I = 10$, the $u$-nullcline and the trajectory (resets omitted, reset voltage $c$ dotted): the IB reset lies to the right of the minimum of the parabola, so the neuron fires again immediately; and the instantaneous firing rate during the step for RS, FS and LTS neurons, showing different degrees of adaptation](./plots/izhikevich.py)

Neither model is a quantitative description of a particular neuron without fitting, and the parameter tables are starting points. Their value lies in showing that the variety of firing patterns that classical physiology catalogued arises from a two-dimensional system with a reset, that is, from the interplay of one fast and one slow variable plus the nonlinear reset that a spike performs. More complex patterns (such as the parabolic bursts of [7.16.7](/7.16.7#sec-7.4)) need additional slow variables.

## 8.5. Noise-Driven Firing

### 8.5.1. The Ornstein–Uhlenbeck Approximation

A cortical neuron receives thousands of synaptic inputs per second, each producing a small, brief current. If the inputs are independent and each is small, their sum is approximately a constant mean plus Gaussian **white noise** (the diffusion approximation). The LIF neuron then obeys a **Langevin equation**,

$$
\tau_{\mathrm{m}}\frac{\mathrm{d}V}{\mathrm{d}t} = -(V - E_{\mathrm{L}}) + \mu + \sigma\sqrt{2\tau_{\mathrm{m}}}\,\xi(t), \tag{8.2}
$$

where $\mu = R\bar I$ is the mean input in voltage units, $\xi$ is standard white noise ($\mathbb{E}[\xi(t)\xi(t')] = \delta(t - t')$) and the factor is chosen so that without threshold $V$ is an **Ornstein–Uhlenbeck process** with stationary mean $E_{\mathrm{L}} + \mu$ and standard deviation $\sigma$. With the threshold, the interspike interval is the **first-passage time** of the OU process from $V_{\mathrm{reset}}$ to $V_{\mathrm{th}}$, plus $\tau_{\mathrm{ref}}$. Its mean has a closed form (Siegert 1951):

$$
\frac{1}{r} = \tau_{\mathrm{ref}} + \tau_{\mathrm{m}}\sqrt{\pi}\int_{(V_{\mathrm{reset}} - E_{\mathrm{L}} - \mu)/(\sqrt{2}\sigma)}^{(V_{\mathrm{th}} - E_{\mathrm{L}} - \mu)/(\sqrt{2}\sigma)} \mathrm{e}^{u^2}\bigl(1 + \operatorname{erf}u\bigr)\,\mathrm{d}u, \tag{8.3}
$$

which reduces to Eq. (8.1) as $\sigma \to 0$. This formula is the transfer function used in the mean-field theory of spiking networks ([7.16.15](/7.16.15)).

### 8.5.2. Mean-Driven and Fluctuation-Driven Firing

Equation (8.2) has two regimes (Figure 3). If $\mu$ exceeds the threshold ($\mu > V_{\mathrm{th}} - E_{\mathrm{L}}$), the neuron is *mean-driven*: the voltage ramps deterministically to threshold, the noise only jitters the crossing time, and the **spike train** is nearly periodic with a small **coefficient of variation** $C_V$ of the **interspike intervals**. If $\mu$ is below the threshold, the neuron is *fluctuation-driven*: the voltage hovers around $E_{\mathrm{L}} + \mu$ and reaches threshold only through rare large fluctuations; the intervals are then broadly distributed with a nearly exponential tail, and $C_V$ approaches 1, the value of a **Poisson process**. In Figure 3A, B the two regimes produce the same rate (about 30 Hz), with $C_V = 0.19$ and $0.63$.

Noise also changes the f–I curve: instead of the sharp threshold of Eq. (8.1), the rate rises smoothly from zero below the deterministic rheobase (Figure 3C). The stronger the noise, the more linear the curve near threshold. This smoothing linearizes the neuron's input–output function, allows it to respond to inputs that would be subthreshold without noise, and lets populations of neurons transmit fast signals that a single deterministic neuron would filter out, because the population rate follows the mean input without the delay of charging the membrane to threshold.

**Example 8.5.1 (Why Cortical Neurons Fire Irregularly)** Cortical neurons in vivo fire irregularly, with $C_V$ of interspike intervals close to 1, although in slices they fire regularly to injected constant current. Softky and Koch (1993) argued that a neuron integrating many independent excitatory inputs should be mean-driven and fire regularly. The resolution (Shadlen and Newsome 1994; van Vreeswijk and Sompolinsky 1996) is balance: excitation and inhibition both increase with network activity and largely cancel, so the mean input stays below threshold while the fluctuations remain large. In Eq. (8.2) this is the fluctuation-driven regime, and Figure 3D shows that $C_V$ is large there. The balanced state of cortical networks is analyzed in [7.16.15](/7.16.15) and [7.16.31](/7.16.31).

:::

![The LIF neuron driven by noise (Eq. (8.2); $\tau_\mathrm{m} = 10$ ms, threshold 15 mV above rest, $\tau_\mathrm{ref} = 2$ ms). A: voltage traces of a mean-driven neuron (mean input 15.5 mV, just above threshold, small noise) and a fluctuation-driven neuron (mean input 12 mV, below threshold, large noise) that fire at similar rates. B: their interspike-interval distributions: narrow and nearly periodic versus broad and skewed, with $C_V$ of 0.19 and 0.63. C: firing rate against the mean input for no noise (Eq. (8.1)) and noise of standard deviation 2 and 4 mV: noise smooths the threshold of the f–I curve. D: the coefficient of variation of the interspike intervals: high when the mean input is below threshold, decreasing as the neuron becomes mean-driven](./plots/noisy-lif.py)

## 8.6. Choosing a Model

Models of neurons form a hierarchy, and the right level depends on the question.

| Level | Variables | Keeps | Used for |
|---|---|---|---|
| multicompartment conductance-based | $10^2$–$10^4$ | dendritic geometry, channel distributions | dendritic integration, back-propagation ([7.16.13](/7.16.13)) |
| single-compartment conductance-based (HH, Connor–Stevens) | 4–15 | ionic mechanisms, spike shape | channels, drugs, mutations ([7.16.5](/7.16.5)) |
| planar conductance-based (Morris–Lecar, $I_{\mathrm{Na,p}} + I_{\mathrm{K}}$) | 2 | bifurcation structure, excitability class | mechanisms of excitability ([7.16.6](/7.16.6)) |
| two-variable integrate-and-fire (AdEx, Izhikevich) | 2 + reset | firing patterns, spike timing | large networks with realistic cell types |
| one-variable integrate-and-fire (LIF, QIF, ExpIF) | 1 + reset | spike timing, f–I curve | network theory, mean-field analysis |
| firing-rate model | 1 per population | mean activity | network dynamics, cognition ([7.16.15](/7.16.15)) |

Two rules guide the choice. First, a model should keep the features the question depends on: a study of synchronization should use a model with the right excitability class, because integrators and resonators synchronize differently ([7.16.15](/7.16.15)), whereas a study of memory capacity may use binary units. Second, results should be checked one level up: a conclusion drawn from LIF networks that depends on the precise reset rule, for example, is suspect. Moving down the hierarchy is a reduction, as in [7.16.6](/7.16.6#sec-6.3), and each step should be justified by a separation of time scales or a normal form, not only by convenience.

## Summary

| Model | Equation (subthreshold) | Reset | Onset of firing |
|---|---|---|---|
| LIF (Definition 8.2.1) | $\tau\dot V = -(V - E_{\mathrm{L}}) + RI$ | at $V_{\mathrm{th}}$ | logarithmic, rheobase $(V_{\mathrm{th}} - E_{\mathrm{L}})/R$ (Proposition 8.2.1) |
| QIF, theta neuron (Definition 8.3.1) | $\tau\dot V = a(V - E_{\mathrm{L}})(V - V_{\mathrm{c}}) + RI$ | at $V_{\mathrm{peak}}$ | $\sqrt{I - I_{\mathrm{c}}}$ (SNIC normal form) |
| ExpIF (Definition 8.3.2) | $\tau\dot V = -(V - E_{\mathrm{L}}) + \Delta_T\mathrm{e}^{(V - V_T)/\Delta_T} + RI$ | at peak | sharpness $\Delta_T$ |
| AdEx, Izhikevich (Definitions 8.4.1, 8.4.2) | plus slow $w$ or $u$ | $V$ reset, $w$ or $u$ incremented | adaptation, bursting, rebound |
| noisy LIF | Eq. (8.2), an OU process | at $V_{\mathrm{th}}$ | smooth (Siegert, Eq. (8.3)) |

- Integrate-and-fire models keep spike timing and discard spike shape; their f–I curves and statistics can be computed analytically.
- Nonlinear models (QIF, ExpIF) have a true threshold, an unstable equilibrium, and the QIF is the canonical class 1 neuron.
- A slow adaptation variable and the reset reproduce the firing classes of cortical neurons.
- Noise smooths the f–I curve and makes firing irregular; irregular cortical firing indicates a fluctuation-driven, balanced regime.

## Questions

1. For the LIF neuron of Example 8.2.1 without refractoriness, compute the rate at $I = 1.6$, $3$ and $15\,\mathrm{nA}$, and compare with the linear approximation for large currents.

   **Answer** $T = \tau\ln[RI/(RI - 15\,\mathrm{mV})]$. At 1.6 nA: $10\ln(16/1) = 27.7\,\mathrm{ms}$, $36\,\mathrm{Hz}$. At 3 nA: $10\ln(30/15) = 6.9\,\mathrm{ms}$, $144\,\mathrm{Hz}$. At 15 nA: $10\ln(150/135) = 1.05\,\mathrm{ms}$, $950\,\mathrm{Hz}$. The linear approximation $r \approx RI/[\tau(V_{\mathrm{th}} - V_{\mathrm{reset}})] = RI/(150\,\mathrm{mV\,ms})$ gives 107, 200 and 1000 Hz: it overestimates near threshold and becomes accurate at high currents (where real neurons would be limited by refractoriness).

2. Show that the substitution $x = \tan(\theta/2)$ transforms $\dot x = x^2 + I$ into the theta neuron, and find the period for $I > 0$.

   **Answer** With $x = \tan(\theta/2)$, $\dot x = \tfrac12\sec^2(\theta/2)\,\dot\theta = \dot\theta/(1 + \cos\theta)$. Also $x^2 + I = (1 - \cos\theta)/(1 + \cos\theta) + I$. Multiplying by $1 + \cos\theta$ gives $\dot\theta = (1 - \cos\theta) + (1 + \cos\theta)I$. As $\theta$ goes from $-\pi$ to $\pi$, $x$ goes from $-\infty$ to $\infty$, so the period is $\int_{-\infty}^{\infty}\mathrm{d}x/(x^2 + I) = \pi/\sqrt{I}$.

3. In the Izhikevich model, find the resting potential and the threshold (the two equilibria) for $I = 0$ and $b = 0.2$, and the current at which they merge.

   **Answer** Equilibria satisfy $u = bv$ and $0.04v^2 + (5 - b)v + 140 + I = 0$. For $b = 0.2$, $I = 0$: $0.04v^2 + 4.8v + 140 = 0$, so $v = [-4.8 \pm \sqrt{23.04 - 22.4}]/0.08 = (-4.8 \pm 0.8)/0.08$, i.e. $v = -70\,\mathrm{mV}$ (rest) and $v = -50\,\mathrm{mV}$ (threshold). They merge when the discriminant vanishes: $4.8^2 = 4 \cdot 0.04(140 + I)$, i.e. $I = 144 - 140 = 4$. (Whether this is a saddle-node, and whether firing then starts from zero frequency, depends on $a$ and $b$: for RS parameters the rest state is a node and the model is a class 1 integrator.)

4. A neuron recorded in vivo fires at 10 Hz with $C_V = 0.9$. In the same neuron, a constant injected current that produces 10 Hz gives $C_V = 0.1$. What does this suggest about its synaptic input in vivo, and how could you test it?

   **Answer** The neuron itself is a regular, mean-driven integrator; the high variability in vivo must come from its input, which suggests that the mean synaptic drive is below threshold and firing is driven by fluctuations, as in a balanced network (Example 8.5.1). A test is to measure the subthreshold voltage in vivo: in a fluctuation-driven regime the mean voltage stays several millivolts below threshold with large fluctuations, and spikes are preceded by rapid upward excursions; another is to measure excitatory and inhibitory conductances separately (by voltage clamp at their reversal potentials) and check that they are large and correlated.
