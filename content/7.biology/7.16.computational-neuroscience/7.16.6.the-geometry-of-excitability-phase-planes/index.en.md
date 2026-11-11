---
title: "The Geometry of Excitability: Phase Planes and Classes of Neurons"
description: "Neurons as dynamical systems: the phase line of the persistent sodium model and the threshold as an unstable equilibrium; the phase plane of the I_Na,p + I_K model with nullclines, Jacobian classification and the separatrix as threshold; reduction of the Hodgkin–Huxley model to two variables, the FitzHugh–Nagumo and Morris–Lecar models; Hodgkin's three classes of excitability; integrators and resonators."
---

The Hodgkin–Huxley model of [7.16.5](/7.16.5) reproduces the action potential, but its four variables hide the reason why a neuron has a threshold, why some neurons start firing at arbitrarily low rates and others at 50 Hz, and why some respond to the timing of their inputs and others only to their sum. These are questions about the *geometry* of the model's trajectories, and they can be answered exactly in one and two dimensions, where the state of the neuron is a point on a line or in a plane. This chapter, following Izhikevich's *Dynamical Systems in Neuroscience*, builds up from a one-variable model to the two-variable models that capture the essence of excitability, and introduces the vocabulary of the next two chapters.

The mathematics (equilibria and their stability, the **phase plane**, **nullclines**, linearization by the **Jacobian matrix**, **limit cycles**) is developed in [2.4.11](/2.4.11#sec-11.5) and applied to gene circuits in [7.6.33](/7.6.33#sec-33.3); here we use it without proofs. All models in this chapter use the units of [7.16.5](/7.16.5): $V$ in mV, $t$ in ms, conductances in $\mathrm{mS\,cm^{-2}}$, currents in $\mu\mathrm{A\,cm^{-2}}$, $c_{\mathrm{m}} = 1\,\mu\mathrm{F\,cm^{-2}}$.

## 6.1. One-Dimensional Dynamics

### 6.1.1. The Persistent Sodium Model

The simplest excitable model has one variable, $V$, and one voltage-gated current, the **persistent sodium current** of [7.16.5](/7.16.5#sec-5.4), whose activation is so fast that we may set $m = m_\infty(V)$:

$$
c_{\mathrm{m}}\frac{\mathrm{d}V}{\mathrm{d}t} = I - g_{\mathrm{L}}(V - E_{\mathrm{L}}) - g_{\mathrm{Na}}\,m_\infty(V)(V - E_{\mathrm{Na}}) =: F(V), \qquad m_\infty(V) = \frac{1}{1 + \mathrm{e}^{(V_{1/2} - V)/k}}, \tag{6.1}
$$

with $g_{\mathrm{L}} = 8$, $E_{\mathrm{L}} = -80$, $g_{\mathrm{Na}} = 20$, $E_{\mathrm{Na}} = 60$, $V_{1/2} = -20$, $k = 15$. A one-dimensional system is completely described by the graph of $F$ (Figure 1A): its zeros are the equilibria, $V$ increases where $F > 0$ and decreases where $F < 0$, so the flow on the *phase line* always moves toward a zero with negative slope and away from a zero with positive slope.

**Proposition 6.1.1 (Stability on the Phase Line)** An equilibrium $V^*$ of $\dot V = F(V)$ with $F'(V^*) < 0$ is asymptotically stable and one with $F'(V^*) > 0$ is unstable; small deviations evolve as $\mathrm{e}^{\lambda t}$ with $\lambda = F'(V^*)/c_{\mathrm{m}}$.

At $I = 0$, $F$ has three zeros: a stable rest state at $-65.9\,\mathrm{mV}$, an unstable equilibrium at $-56.5\,\mathrm{mV}$ and a stable "excited" state at $+17.7\,\mathrm{mV}$. The unstable equilibrium is the threshold: a brief stimulus that leaves $V$ below it decays to rest, one that leaves $V$ above it grows to the excited state (Figure 1C). This is the simplest answer to the question "what is a threshold?": a repelling point that separates the **basins of attraction** of two attractors. The model is **bistable**, and since it has no recovery variable it cannot return from the excited state; it describes the upstroke of an action potential, or the up and down states of neurons with strong persistent inward currents, but not a spike.

### 6.1.2. The Saddle-Node Bifurcation

As $I$ increases, the graph of $F$ moves up; at $I = 4.3$ the rest state and the threshold merge at $V = -61.1\,\mathrm{mV}$ and disappear (Figure 1B). This is a **saddle-node bifurcation**, the generic way in which an equilibrium is lost when a single parameter changes ([7.6.33](/7.6.33#sec-33.2.2)). Near it $F(V) \approx a(I - I_{\mathrm{sn}}) + b(V - V_{\mathrm{sn}})^2$, and two consequences follow that recur throughout the next chapters. First, just below the bifurcation the threshold lies close to rest, so excitability is high. Second, just above it the trajectory passes slowly through the "ghost" of the vanished equilibria: the passage time scales as $\pi/\sqrt{ab(I - I_{\mathrm{sn}})}$, which tends to infinity at the bifurcation. This slow passage is the origin of the long latencies and the low **firing rates** of class 1 neurons (Section 6.4).

![The persistent sodium model, a one-dimensional excitable system. A: the right-hand side $F(V)$ of Eq. (6.1) for three values of the current $I$ (µA cm⁻²): zeros are equilibria (filled: stable; open: unstable), and the flow is to the right where $F > 0$. B: bifurcation diagram: equilibrium voltages against $I$; the rest state and the unstable threshold merge in a saddle-node bifurcation at $I = 4.3$ µA cm⁻². C: time courses at $I = 0$ from initial voltages just below and above the unstable equilibrium (dotted line at −56.5 mV): the voltage returns to rest or jumps to the depolarized state](./plots/phase-line.py)

## 6.2. Two-Dimensional Dynamics

### 6.2.1. The $I_{\mathrm{Na,p}} + I_{\mathrm{K}}$ Model

Adding a $\ce{K+}$ current with a first-order activation gate $n$ gives the neuron a way back from the excited state:

$$
\begin{aligned}
c_{\mathrm{m}}\frac{\mathrm{d}V}{\mathrm{d}t} &= I - g_{\mathrm{L}}(V - E_{\mathrm{L}}) - g_{\mathrm{Na}}\,m_\infty(V)(V - E_{\mathrm{Na}}) - g_{\mathrm{K}}\,n\,(V - E_{\mathrm{K}}),\\
\frac{\mathrm{d}n}{\mathrm{d}t} &= \frac{n_\infty(V) - n}{\tau_n},
\end{aligned} \tag{6.2}
$$

with $g_{\mathrm{K}} = 10$, $E_{\mathrm{K}} = -90$, $\tau_n = 1\,\mathrm{ms}$, and $n_\infty$ a Boltzmann function with $V_{1/2} = -25$, $k = 5$ (a high-threshold $\ce{K+}$ current). This model, like the HH model, has a fast amplifying variable ($V$, through the instantaneous $\ce{Na+}$ activation) and a slower resonant or recovery variable ($n$). Almost every spiking model, including the HH model after reduction (Section 6.3), has this structure, and the $I_{\mathrm{Na,p}} + I_{\mathrm{K}}$ model has the advantage that every bifurcation discussed in [7.16.7](/7.16.7) occurs in it for suitable parameters.

The **nullclines** organize the phase plane (Figure 2A). The $V$-nullcline, where $\dot V = 0$, is the curve

$$
n = \frac{I - g_{\mathrm{L}}(V - E_{\mathrm{L}}) - g_{\mathrm{Na}}m_\infty(V)(V - E_{\mathrm{Na}})}{g_{\mathrm{K}}(V - E_{\mathrm{K}})},
$$

which has the cubic (N-like) shape typical of excitable membranes: the middle branch with positive slope exists because the $\ce{Na+}$ current is regenerative. The $n$-nullcline is the activation curve $n = n_\infty(V)$. Above the $V$-nullcline $V$ decreases, below it $V$ increases; to the right of the $n$-nullcline $n$ increases. Equilibria are the intersections.

### 6.2.2. Linear Stability and the Threshold

At an equilibrium $(V^*, n^*)$, small deviations obey the linearized system with the Jacobian matrix

$$
J = \begin{bmatrix} \dfrac{\partial \dot V}{\partial V} & \dfrac{\partial \dot V}{\partial n} \\[2mm] \dfrac{\partial \dot n}{\partial V} & \dfrac{\partial \dot n}{\partial n} \end{bmatrix}
= \begin{bmatrix} -g'(V^*)/c_{\mathrm{m}} & -g_{\mathrm{K}}(V^* - E_{\mathrm{K}})/c_{\mathrm{m}} \\[2mm] n_\infty'(V^*)/\tau_n & -1/\tau_n \end{bmatrix},
$$

where $g'(V^*)$ is the slope of the instantaneous current–voltage curve (leak plus $\ce{Na+}$ plus $\ce{K+}$ at fixed $n$). The eigenvalues classify the equilibrium as a node, saddle or focus ([2.4.11](/2.4.11#sec-11.5.2)); in terms of $\operatorname{tr}J$ and $\det J$, it is a saddle if $\det J < 0$, stable if $\det J > 0$ and $\operatorname{tr}J < 0$, and a focus (damped or growing oscillations) if $(\operatorname{tr}J)^2 < 4\det J$.

**Example 6.2.1 (Three Equilibria at $I = 0$)** For the parameters above the nullclines intersect three times. At $V^* = -66.0\,\mathrm{mV}$ the eigenvalues are $-1.72$ and $-1.02\,\mathrm{ms^{-1}}$: a stable node, the resting state. At $V^* = -56.1\,\mathrm{mV}$ they are $+2.00$ and $-0.96\,\mathrm{ms^{-1}}$: a **saddle**. At $V^* = -27.3\,\mathrm{mV}$ they are $3.47 \pm 3.13\mathrm{i}\,\mathrm{ms^{-1}}$: an unstable focus, surrounded by a stable limit cycle, the repetitive spiking that the model would show if it could reach it. The model is again bistable: rest and spiking coexist.

:::

What plays the role of the threshold in the plane? The saddle has a one-dimensional stable manifold, the set of states that converge to it, and this curve divides the plane into the basin of the rest state and the basin of the limit cycle (Figure 2A, dashed). A stimulus that moves the state across the stable manifold of the saddle produces a spike; one that does not, decays. The threshold is therefore a *curve* in the $(V, n)$ plane, not a voltage: the voltage threshold for a brief pulse depends on the value of $n$ at that moment, which is why it rises after a spike (when $n$ is high) and falls after hyperpolarization (when $n$ is low). A separatrix of this kind is the general form of the threshold in models with a saddle.

The model behaves very differently when its $\ce{K+}$ current activates at lower voltages. With $n_\infty$ shifted to $V_{1/2} = -45\,\mathrm{mV}$ (and $E_{\mathrm{L}} = -78\,\mathrm{mV}$), the nullclines intersect only once, at $V^* = -60.9\,\mathrm{mV}$, and the eigenvalues there are $-0.66 \pm 1.46\mathrm{i}\,\mathrm{ms^{-1}}$: the rest state is a stable focus. A perturbation now produces damped oscillations with period $2\pi/1.46 = 4.3\,\mathrm{ms}$ (Figure 2C), and there is no saddle and no sharp threshold. We return to this difference in Section 6.5.

![Phase plane of the $I_\mathrm{Na,p}+I_\mathrm{K}$ model (Eq. (6.2)) at $I = 0$. A: the $V$-nullcline (cubic) and the $n$-nullcline (activation curve) intersect at a stable node (rest, filled), a saddle and an unstable focus (open); the arrows show the vector field; the dashed curve is the stable manifold of the saddle, which acts as the threshold. Three trajectories start after brief voltage jumps to −60, −58 and −52 mV (with $n$ at rest): the first two return to rest, the third crosses the threshold and makes a large excursion around the unstable focus, an action potential. B: the corresponding voltage time courses. C: the same model with a low-threshold K⁺ current, whose single equilibrium is a stable focus: perturbations of ±8 mV produce damped oscillations](./plots/nap-k-plane.py)

## 6.3. Reduction of the Hodgkin–Huxley Model

### 6.3.1. Fast–Slow Separation

Three observations reduce the four-dimensional HH model to two variables (Rinzel 1985). First, $\tau_m$ is an order of magnitude smaller than $\tau_h$ and $\tau_n$, so $m$ is practically at its steady state: $m \approx m_\infty(V)$. Second, along trajectories of the full model $h$ and $n$ are strongly anticorrelated, because they have similar time constants and opposite voltage dependences; a linear fit gives $h \approx 0.89 - 1.1\,n$. Third, with these substitutions the remaining variables are the fast $V$ and the slow $n$:

$$
c_{\mathrm{m}}\frac{\mathrm{d}V}{\mathrm{d}t} = I - \bar g_{\mathrm{Na}}\,m_\infty(V)^3(0.89 - 1.1n)(V - E_{\mathrm{Na}}) - \bar g_{\mathrm{K}}\,n^4(V - E_{\mathrm{K}}) - g_{\mathrm{L}}(V - E_{\mathrm{L}}),
\qquad \frac{\mathrm{d}n}{\mathrm{d}t} = \frac{n_\infty(V) - n}{\tau_n(V)}.
$$

The reduced model produces a spike of nearly the right amplitude and the right recovery (Figure 3A, B). Its upstroke is faster than in the full model, because $m$ now follows $V$ instantaneously. The phase plane has the same structure as that of the $I_{\mathrm{Na,p}} + I_{\mathrm{K}}$ model: an N-shaped $V$-nullcline and a monotonic $n$-nullcline crossing it once on its left branch.

### 6.3.2. FitzHugh–Nagumo and Morris–Lecar

Two caricatures of this geometry have become standard.

**Definition 6.3.1 (FitzHugh–Nagumo Model)** The **FitzHugh–Nagumo model** is the dimensionless system

$$
\frac{\mathrm{d}v}{\mathrm{d}t} = v - \frac{v^3}{3} - w + I, \qquad \frac{\mathrm{d}w}{\mathrm{d}t} = \varepsilon\,(v + a - b w),
$$

with a cubic $v$-nullcline, a linear $w$-nullcline and a small $\varepsilon$ (typically $a = 0.7$, $b = 0.8$, $\varepsilon = 0.08$); $v$ plays the role of the membrane potential and $w$ of the recovery variable.

FitzHugh (1961) obtained the model by simplifying the van der Pol oscillator ([2.4.11](/2.4.11#sec-11.6.3)) so that it has a stable rest state; Nagumo built it as an electronic circuit with a tunnel diode. For $I = 0$ the nullclines cross on the left branch of the cubic and the system is excitable: a sufficiently large perturbation of $v$ makes a large excursion, jumping to the right branch, sliding up it slowly, jumping back and returning to rest (Figure 3C, D). For $I = 0.5$ the intersection lies on the middle branch, the equilibrium is unstable and the trajectory is a **relaxation oscillator** ([7.6.33](/7.6.33#sec-33.5.4)): slow drifts along the outer branches alternate with fast jumps.

**Definition 6.3.2 (Morris–Lecar Model)** The **Morris–Lecar model** describes a membrane with an instantaneous $\ce{Ca^2+}$ conductance and a delayed $\ce{K+}$ conductance:

$$
\begin{aligned}
C\frac{\mathrm{d}V}{\mathrm{d}t} &= I - g_{\mathrm{L}}(V - E_{\mathrm{L}}) - g_{\mathrm{Ca}}\,m_\infty(V)(V - E_{\mathrm{Ca}}) - g_{\mathrm{K}}\,w\,(V - E_{\mathrm{K}}),\\
\frac{\mathrm{d}w}{\mathrm{d}t} &= \varphi\,\frac{w_\infty(V) - w}{\tau_w(V)},
\end{aligned}
$$

with $m_\infty = \tfrac12[1 + \tanh((V - V_1)/V_2)]$, $w_\infty = \tfrac12[1 + \tanh((V - V_3)/V_4)]$ and $\tau_w = 1/\cosh((V - V_3)/(2V_4))$.

Morris and Lecar (1981) wrote it for the barnacle giant muscle fiber, whose action potential is carried by $\ce{Ca^2+}$. Mathematically it is the conductance-based model closest to FitzHugh–Nagumo, and with two standard parameter sets (Rinzel and Ermentrout 1989) it shows the two main classes of excitability (Section 6.4).

![Two-dimensional models of the action potential. A: the Rinzel reduction of the Hodgkin–Huxley model in the $(V, n)$ plane, with its nullclines at $I = 0$; the projection of the full four-variable trajectory after a 20 µA cm⁻², 0.5 ms pulse (grey) and the trajectory of the reduced model from the same state (colour). B: the voltage of the full and reduced models: the reduced spike has a faster upstroke but the same amplitude and recovery. C: the FitzHugh–Nagumo phase plane: the cubic $v$-nullcline for $I = 0$ and $I = 0.5$, the linear $w$-nullcline, an excitable excursion at $I = 0$ (blue) and the relaxation limit cycle at $I = 0.5$ (red). D: the corresponding time courses of $v$](./plots/reduction.py)

## 6.4. Classes of Excitability

### 6.4.1. Hodgkin's Classification

In 1948, before the voltage clamp, Hodgkin injected steady currents into single crab axons and found three types of behavior. The classification remains the standard description of how neurons encode a constant input.

**Definition 6.4.1 (Classes of Excitability)** A neuron has **class 1 excitability** if repetitive firing in response to a constant current starts at an arbitrarily low frequency, so that the f–I curve is continuous; **class 2 excitability** if repetitive firing starts at a nonzero frequency that changes little with the current; and *class 3 excitability* if a constant current produces a single spike (or none) and repetitive firing occurs only for transient or very strong inputs.

Most cortical pyramidal neurons are class 1, as are the neurons with an **A-current** in [7.16.5](/7.16.5#sec-5.4); the squid axon and many fast-spiking interneurons are class 2 (the HH model starts firing at about 58 Hz); class 3 neurons, such as some brainstem auditory neurons, respond to the onsets of inputs, which suits them for timing. The f–I curve is the neuron's input–output function, and its shape at the onset is decided by the bifurcation through which the rest state disappears.

The Morris–Lecar model illustrates both main classes (Figure 4A, B). With the class 1 parameters the rest state disappears at $I \approx 40\,\mu\mathrm{A\,cm^{-2}}$ in a saddle-node bifurcation on the limit cycle, the mechanism of Section 6.1.2 in two dimensions: just above the bifurcation the trajectory spends a long time near the ghost of the equilibrium, and the firing rate rises from zero as $\sqrt{I - I_{\mathrm{c}}}$. With the class 2 parameters the rest state loses stability at $I \approx 94\,\mu\mathrm{A\,cm^{-2}}$ through a subcritical **Hopf bifurcation**; large-amplitude spiking already exists from $I \approx 89\,\mu\mathrm{A\,cm^{-2}}$ and starts at about 7 Hz, a nonzero frequency of the order set by the imaginary part of the eigenvalues. The four bifurcations of the rest state and the full correspondence with the classes are the subject of [7.16.7](/7.16.7#sec-7.1).

### 6.4.2. Thresholds Without a Saddle

In class 2 models without a saddle, such as FitzHugh–Nagumo at $I = 0$, there is no separatrix and, strictly speaking, no threshold: the size of the response grows continuously, but very steeply, with the stimulus. Trajectories that start in a narrow band follow the unstable middle branch of the $V$-nullcline for a while before turning to rest or to a spike, and the resulting responses of intermediate size are called *canards*. Their band is exponentially thin when the recovery variable is slow ($\varepsilon \to 0$), so that in practice the response looks all-or-none; experimentally, graded spikes of intermediate amplitude were indeed found in the squid axon at high temperatures, where the separation of time scales is weaker. The practical lesson is that a threshold is a property of the trajectory, not of a voltage: it can be a point (Section 6.1), a curve (Section 6.2) or a thin band of trajectories.

## 6.5. Integrators and Resonators

The second fundamental distinction concerns the response to *weak* inputs, and it depends on the eigenvalues of the rest state.

**Definition 6.5.1 (Integrator and Resonator)** A neuron is an **integrator** if its resting state is a stable node, so that small perturbations decay monotonically, and a **resonator** if its resting state is a stable focus, so that small perturbations produce damped oscillations at a preferred frequency.

The difference determines how a neuron combines its inputs (Figure 4C). An integrator adds inputs whose effects overlap in time: the closer two excitatory pulses are, the smaller the second pulse needs to be to fire the cell, so integrators act as **coincidence detectors** with a window of the order of the **membrane time constant**, and their threshold is sharp (the saddle of Section 6.2). A resonator responds best to inputs that arrive at its own period: a second pulse one period (3.2 ms in the figure) after the first adds in phase with the subthreshold oscillation and needs to be smaller than a single pulse, whereas a pulse half a period later arrives when the voltage swings down and needs to be larger. Resonators therefore prefer input at particular frequencies and can be selectively addressed by a rhythmic signal.

Several counterintuitive properties of resonators follow from the same geometry. An inhibitory pulse can fire a resonator (postinhibitory rebound spike, as in the anode-break excitation of the HH model, [7.16.5](/7.16.5#sec-5.3)), because the oscillation that follows it overshoots the threshold; an excitatory pulse can delay or even prevent a spike if it arrives at the wrong phase; and a resonator may have no fixed voltage threshold at all. Integrators show none of these effects. The distinction is independent of Hodgkin's classes in principle, but in practice class 1 neurons are usually integrators and class 2 neurons resonators, for reasons explained by the bifurcations in [7.16.7](/7.16.7#sec-7.3). In the brain, subthreshold oscillations and resonance at 4–10 Hz are prominent in entorhinal stellate cells and in many interneurons, produced by $I_{\mathrm{h}}$ and $I_{\mathrm{M}}$, which act as resonant **gating variables** in the sense of this chapter.

![Classes of excitability and the integrator–resonator distinction. A: f–I curves of the Morris–Lecar model: with the class 1 parameters (saddle-node on invariant circle) the firing rate rises continuously from zero; with the class 2 parameters (Hopf) it jumps to about 7 Hz at the onset. B: the voltage just above the onset of firing for each parameter set: the class 1 neuron spends most of the cycle in a slow approach to threshold. C: pairs of brief voltage jumps in the $I_\mathrm{Na,p}+I_\mathrm{K}$ model: the size of the second jump needed to fire the cell, relative to the size needed for a single jump, against the interval between the jumps. For an integrator (high-threshold K⁺ current) the needed jump decreases monotonically as the interval shrinks; for a resonator (low-threshold K⁺ current, near a Hopf bifurcation) it oscillates and is smallest when the interval equals the period of the subthreshold oscillation, 3.2 ms](./plots/classes.py)

## Summary

| Concept | One dimension | Two dimensions |
|---|---|---|
| State | $V$ on a phase line | $(V, n)$ in the phase plane |
| Equilibria | zeros of $F(V)$ | intersections of the nullclines |
| Stability | sign of $F'(V^*)$ (Proposition 6.1.1) | eigenvalues of $J$: node, saddle, focus (Example 6.2.1) |
| Threshold | unstable equilibrium | stable manifold of a saddle, or a thin band of trajectories (canard) |
| Loss of rest | saddle-node bifurcation | saddle-node (on or off a limit cycle) or Hopf |

- Spiking models have a fast amplifying variable and a slow recovery variable; the HH model reduces to this form with $m = m_\infty(V)$ and $h \approx 0.89 - 1.1n$, and FitzHugh–Nagumo and Morris–Lecar (Definitions 6.3.1 and 6.3.2) are its canonical caricatures.
- Class 1 neurons start firing at zero frequency (saddle-node on the cycle), class 2 at a nonzero frequency (Hopf), class 3 do not fire repetitively (Definition 6.4.1).
- Integrators (stable node) add coincident inputs; resonators (stable focus) prefer inputs at their own frequency and can fire after inhibition (Definition 6.5.1).

## Questions

1. For the one-dimensional model $\dot V = I + (V - V_{\mathrm{sn}})^2$ (time and voltage rescaled), find the equilibria for $I < 0$, determine their stability, and compute the time needed to go from $V = -\infty$ to $V = +\infty$ for $I > 0$.

   **Answer** For $I < 0$ the equilibria are $V^* = V_{\mathrm{sn}} \mp \sqrt{-I}$; $F'(V^*) = 2(V^* - V_{\mathrm{sn}}) = \mp 2\sqrt{-I}$, so the lower one is stable (rest) and the upper one unstable (threshold). For $I > 0$, $\int_{-\infty}^{\infty} \mathrm{d}V/(I + (V - V_{\mathrm{sn}})^2) = \pi/\sqrt{I}$. If the trajectory is reset after reaching $+\infty$ (a spike), the firing rate is $\sqrt{I}/\pi$: it rises from zero as the square root of the distance from the bifurcation, the signature of class 1 excitability.

2. At an equilibrium of a two-dimensional model, $\operatorname{tr}J = -0.5\,\mathrm{ms^{-1}}$ and $\det J = 2\,\mathrm{ms^{-2}}$. Is the equilibrium an integrator or a resonator? Estimate the frequency of its subthreshold oscillations and their decay time.

   **Answer** The eigenvalues are $\lambda = -0.25 \pm \mathrm{i}\sqrt{2 - 0.0625} = -0.25 \pm 1.39\mathrm{i}\,\mathrm{ms^{-1}}$, a stable focus, hence a resonator. The oscillation frequency is $1.39/(2\pi)\,\mathrm{kHz} \approx 220\,\mathrm{Hz}$ and the amplitude decays with time constant $1/0.25 = 4\,\mathrm{ms}$.

3. Explain with the phase plane of Figure 2A why the voltage threshold for a brief depolarizing pulse is higher immediately after an action potential.

   **Answer** A brief pulse moves the state horizontally, changing $V$ but not $n$. After a spike $n$ is elevated, and the stable manifold of the saddle, which separates the basins, lies further to the right at larger $n$ (it bends toward higher $V$ as $n$ increases). A horizontal jump from the elevated state must therefore be larger to cross it, so the voltage threshold is raised until $n$ has relaxed; this is the relative refractory period in geometric form.

4. A FitzHugh–Nagumo neuron at rest ($I = 0$, $\varepsilon = 0.08$) receives either a brief hyperpolarizing jump of $v$ or a long hyperpolarizing current ($I = -0.5$ for 100 time units) that is then switched off. Use the nullclines to predict which of the two can produce a rebound spike.

   **Answer** After a brief jump to the left, $v$ returns to the left branch of the cubic in a time of order 1, much faster than $w$ (time scale $1/\varepsilon \approx 12$), so the state comes back to rest with $w$ almost unchanged and no spike results (simulations confirm this for jumps up to $\Delta v = -3$). During a long hyperpolarizing current, the $v$-nullcline is lowered and the state settles at a new equilibrium with a smaller $w$. When the current is switched off, the nullcline returns to its original position, and the state, with its low $w$, now lies below the knee of the cubic: $v$ is pushed to the right branch and the cell fires one spike before returning to rest (anode-break excitation, as in the HH model). The recovery variable must have time to change: rebound requires a hyperpolarization that lasts longer than the recovery time scale.
