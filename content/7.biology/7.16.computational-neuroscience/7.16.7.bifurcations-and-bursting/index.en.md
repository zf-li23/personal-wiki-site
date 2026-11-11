---
title: Bifurcations and Bursting
description: "How neurons switch from rest to spiking: the four codimension-one bifurcations of the resting state (saddle-node, saddle-node on invariant circle, supercritical and subcritical Andronov–Hopf) and the bifurcations of the spiking limit cycle; bistability and hysteresis; the classification of neurons as integrators or resonators, monostable or bistable; bursting as a fast–slow phenomenon named by its pair of bifurcations, with fold/homoclinic bursting analyzed in detail; thalamic relay neurons, pancreatic β cells, Aplysia R15 and respiratory pacemakers."
---

A neuron at rest that receives a slowly increasing current eventually starts to fire. In the language of [7.16.6](/7.16.6), the stable equilibrium that represents rest either disappears or loses its stability, and the trajectory moves to a limit cycle that represents repetitive spiking. A remarkable fact of dynamical systems theory is that, for a system depending on one parameter, there are only four generic ways in which a stable equilibrium can do this. Each has its own fingerprint in the neuron's behavior: whether firing starts at zero or at a finite frequency, whether rest and spiking coexist, whether subthreshold oscillations are present. The bifurcation, rather than the details of the ionic currents, therefore determines the computational properties of a neuron (Izhikevich 2007).

This chapter classifies the transitions between rest and spiking and then uses the same tools to explain *bursting*, the alternation of spike clusters and quiescence that underlies rhythmic motor patterns, sleep oscillations and hormone secretion. The general theory of bifurcations in the plane, including the **Hopf bifurcation**, is in [2.4.11](/2.4.11#sec-11.6.4) and [7.6.33](/7.6.33#sec-33.5.2); all examples here use the $I_{\mathrm{Na,p}} + I_{\mathrm{K}}$ model (Eq. (6.2) of [7.16.6](/7.16.6#sec-6.2)) with different parameter values.

## 7.1. Bifurcations of the Resting State

### 7.1.1. Four Ways to Lose Stability

An equilibrium loses stability when one of the eigenvalues of its Jacobian crosses the imaginary axis. A single real eigenvalue crossing zero leads to a **saddle-node bifurcation**: the stable node collides with a saddle and both disappear. A pair of complex conjugate eigenvalues crossing the imaginary axis leads to an Andronov–Hopf bifurcation: the equilibrium survives but becomes an unstable focus, and a limit cycle of small amplitude appears or disappears. Each case splits into two according to what happens globally (Figure 1).

**Definition 7.1.1 (Saddle-Node on Invariant Circle)** A **saddle-node on invariant circle** bifurcation (SNIC) is a saddle-node bifurcation in which the stable node and the saddle lie on a closed invariant curve formed by the unstable manifold of the saddle; when they merge and disappear, the invariant curve becomes a limit cycle.

**Definition 7.1.2 (Supercritical and Subcritical Andronov–Hopf Bifurcations)** In a **supercritical Andronov–Hopf bifurcation** a stable focus becomes unstable and a stable limit cycle, whose amplitude grows from zero as the square root of the distance from the bifurcation, is born around it. In a **subcritical Andronov–Hopf bifurcation** an unstable limit cycle surrounding a stable focus shrinks to it, and the focus becomes unstable; the trajectory then jumps to a distant attractor.

The four cases can be read from Figure 1:

1. *Saddle-node on invariant circle* (panel A, $I_{\mathrm{Na,p}} + I_{\mathrm{K}}$ model with a high-threshold $\ce{K+}$ current). Rest and threshold merge at $I = 4.51\,\mu\mathrm{A\,cm^{-2}}$; the invariant circle through the saddle is the future spike trajectory. Just above the bifurcation, the trajectory passes slowly through the ghost of the vanished equilibria, so the period diverges and the firing rate starts from zero as $\sqrt{I - I_{\mathrm{c}}}$ (Question 1 of [7.16.6](/7.16.6)).
2. *Saddle-node off the invariant circle* (panel D, same model with a faster $\ce{K+}$ current, $\tau_n = 0.16\,\mathrm{ms}$). The node and the saddle again merge at $I = 4.51$, but a limit cycle already exists away from them, born at $I = 3.1$; when rest disappears, the state jumps to this cycle and fires at a finite frequency. Between 3.1 and 4.51 rest and spiking coexist.
3. *Supercritical Andronov–Hopf* (panel B, low-threshold $\ce{K+}$ current). The resting focus loses stability at $I = 14.6$; small oscillations appear and grow continuously into spikes. Their frequency at the onset is set by the imaginary part of the eigenvalues, about 340 Hz in this fast model.
4. *Subcritical Andronov–Hopf* (panel C). At $I = 48.8$ an unstable cycle collapses onto the resting focus, which becomes unstable, and the trajectory jumps to a large-amplitude spiking cycle that coexists with rest from $I = 42.5$ upward.

![The four bifurcations of the resting state in the $I_\mathrm{Na,p}+I_\mathrm{K}$ model. Each panel shows the equilibrium voltage against the injected current (solid: stable; dashed: unstable) and, where the neuron spikes, the maximum and minimum of $V$ on the limit cycle (dots), obtained by simulation from rest and from a depolarized state. A: saddle-node on invariant circle at 4.5 µA cm⁻²: rest disappears and spiking appears at the same current. B: supercritical Andronov–Hopf bifurcation at 14.6 µA cm⁻²: the oscillation amplitude grows from zero. C: subcritical Andronov–Hopf bifurcation at 48.8 µA cm⁻²: large spikes appear abruptly, and they coexist with the stable rest state down to 42.5 µA cm⁻². D: saddle-node off the invariant circle at 4.5 µA cm⁻² (faster K⁺ current): the spiking cycle already exists from 3.1 µA cm⁻², so rest and spiking coexist](./plots/rest-bifurcations.py)

### 7.1.2. Fingerprints

The four bifurcations have distinct experimental signatures, summarized in the table. They can be distinguished in a neuron by three measurements: the f–I curve near the onset, the response to small pulses (damped oscillations or monotonic decay), and the presence of hysteresis (whether a brief pulse can switch the cell from rest to spiking and back at the same current).

| Bifurcation of rest | Eigenvalues at the bifurcation | Spiking starts at | Subthreshold oscillations | Rest and spiking coexist |
|---|---|---|---|---|
| saddle-node on invariant circle | $\lambda = 0$ | zero frequency | no | no |
| saddle-node (off the circle) | $\lambda = 0$ | finite frequency | no | yes |
| supercritical Andronov–Hopf | $\lambda = \pm\mathrm{i}\omega$ | finite frequency, zero amplitude | yes | no |
| subcritical Andronov–Hopf | $\lambda = \pm\mathrm{i}\omega$ | finite frequency and amplitude | yes | yes |

Close to each bifurcation, every model, whatever its currents, is equivalent (after a change of variables) to a *normal form* that depends only on the type of bifurcation. For the saddle-node this is the quadratic $\dot x = I + x^2$, which is the origin of the quadratic integrate-and-fire neuron of [7.16.8](/7.16.8#sec-8.3); for the Andronov–Hopf bifurcation it is $\dot z = (\mu + \mathrm{i}\omega)z + \sigma z\lvert z\rvert^2$ with complex $z$, supercritical for $\sigma < 0$ and subcritical for $\sigma > 0$. This universality is why the classification is useful: it predicts the neuron's response near the onset of firing from a single qualitative fact.

## 7.2. Bifurcations of the Spiking State

When the current is decreased again, the spiking limit cycle must disappear, and this too happens in a few generic ways:

- *Saddle-node on invariant circle*: the reverse of the bifurcation above; the period diverges as $1/\sqrt{I - I_{\mathrm{c}}}$ and the rate goes to zero.
- *Supercritical Andronov–Hopf*: the cycle shrinks to the equilibrium; amplitude goes to zero, frequency stays finite.
- *Fold limit cycle* (saddle-node of cycles): the stable spiking cycle collides with an unstable cycle and both vanish, at finite amplitude and frequency. It is the companion of the subcritical Andronov–Hopf bifurcation (Figure 1C, at $I = 42.5$).
- *Saddle homoclinic orbit*: the cycle grows until it touches a saddle and becomes a homoclinic orbit, a trajectory that leaves the saddle and returns to it.

**Definition 7.2.1 (Saddle Homoclinic Orbit Bifurcation)** A **saddle homoclinic orbit bifurcation** occurs when a limit cycle passes through a saddle equilibrium, forming an orbit homoclinic to the saddle; on the other side of the bifurcation the cycle no longer exists. Because the trajectory slows down near the saddle, the period of the cycle diverges logarithmically, $T \propto -\ln\lvert I - I_{\mathrm{h}}\rvert$, as the bifurcation is approached.

The homoclinic bifurcation explains panel D of Figure 1: the cycle that exists above $I = 3.1$ is born when it detaches from the saddle. The logarithmic divergence of the period is much milder than the square root of the SNIC, so the rate drops steeply only extremely close to the bifurcation.

When the bifurcations of rest and of spiking occur at different currents, the two states coexist between them, and the state of the neuron depends on its history: this is **hysteresis**. Figure 2A shows it in a staircase of current steps for the model with the subcritical Andronov–Hopf bifurcation: at $45\,\mu\mathrm{A\,cm^{-2}}$ the neuron is silent on the way up and spikes on the way down. Within the bistable range a brief pulse switches the neuron from rest to spiking, and an identical pulse delivered at the right phase of the spike cycle switches it off again (Figure 2B), because the basin of the rest state is the small region enclosed by the unstable cycle (Figure 2C). Such **bistability** gives a single neuron a short-term memory of its input. It occurs, for instance, in spinal motoneurons with persistent inward currents (plateau potentials, [7.16.30](/7.16.30)) and has been proposed as a cellular basis of persistent activity in working memory ([7.16.45](/7.16.45)).

![Bistability near a subcritical Andronov–Hopf bifurcation (same model as Figure 1C). A: a staircase of current steps (grey, labels in µA cm⁻²): at 45 the neuron stays at rest on the way up but continues to spike on the way down; spiking starts above the Hopf point (48.8) and stops below the fold of limit cycles (42.5). B: at a constant 45 µA cm⁻², a brief depolarizing pulse switches the neuron from rest to spiking, and an identical pulse at the right phase switches it back to rest, through damped oscillations. C: the phase plane at 45 µA cm⁻²: the stable focus (rest) is enclosed by a small unstable limit cycle (dashed), the boundary between the basin of rest and the basin of the large spiking cycle](./plots/hysteresis.py)

## 7.3. Neurocomputational Classes

The two properties introduced in [7.16.6](/7.16.6) can now be traced to the bifurcations. Whether a neuron is an integrator or a resonator (Definition 6.5.1) depends on whether the eigenvalues of its rest state near the bifurcation are real (saddle-node) or complex (Andronov–Hopf). Whether it is monostable or bistable depends on whether the bifurcation of rest coincides with the birth of the spiking cycle. The four bifurcations thus fill a two-by-two table (Izhikevich 2007, Chapter 7):

| | coexistence of rest and spiking (bistable) | no coexistence (monostable) |
|---|---|---|
| integrator (no subthreshold oscillations) | saddle-node | saddle-node on invariant circle |
| resonator (subthreshold oscillations) | subcritical Andronov–Hopf | supercritical Andronov–Hopf |

Hodgkin's classes (Definition 6.4.1) are a third, partly overlapping property. Only the SNIC gives class 1 excitability, firing from zero frequency; the other three give class 2. (A saddle homoclinic orbit bifurcation of the spiking cycle can also produce rates that start near zero, but this is rare in neurons.) The typical cortical pyramidal neuron, a class 1 integrator, is near a SNIC; the squid axon and the HH model, class 2 resonators with a narrow bistable range, are near a subcritical Andronov–Hopf bifurcation; fast-spiking interneurons often behave as class 2 resonators or as class 1 neurons with a narrow bistable range. The conductances that move a neuron between classes, such as the A-current ([7.16.5](/7.16.5#sec-5.4)) or a low-threshold $\ce{K+}$ current, do so by changing the bifurcation, and neuromodulators that alter these conductances can switch a neuron's computational class.

**Example 7.3.1 (Diagnosing the Bifurcation)** A neuron is injected with slow ramps of current. Firing starts at 3 Hz on the way up and stops at the same current on the way down; small pulses at rest produce monotonic responses. The bifurcation is a SNIC: monostable (no hysteresis), integrator (no oscillations), class 1 (onset at near-zero rate). If instead firing started at 40 Hz with damped subthreshold ringing at 40 Hz and stopped at a lower current on the way down, the bifurcation would be a subcritical Andronov–Hopf, and the neuron would be expected to respond selectively to inputs at about 40 Hz.

## 7.4. Bursting

### 7.4.1. Fast–Slow Decomposition

Many neurons fire in bursts: clusters of spikes separated by quiescent periods (Figure 3A). The defining feature is two time scales: a fast spike-generating subsystem (time constants of milliseconds) and a slow variable (tens of milliseconds to seconds) that turns spiking on and off.

**Definition 7.4.1 (Bursting and Fast–Slow Decomposition)** **Bursting** is a dynamical regime in which a neuron alternates between repetitive spiking and quiescence. A fast–slow burster has the form $\dot{\boldsymbol{x}} = \boldsymbol{f}(\boldsymbol{x}, y)$, $\dot y = \mu\,g(\boldsymbol{x}, y)$ with $\mu \ll 1$, where $\boldsymbol{x}$ describes the spike-generating currents and $y$ a slow current or concentration. In the **fast–slow decomposition** the slow variable is frozen and treated as a parameter of the fast subsystem $\dot{\boldsymbol{x}} = \boldsymbol{f}(\boldsymbol{x}, y)$, whose bifurcation diagram against $y$ is then traced by the slow drift of $y$.

For bursting to occur, the fast subsystem must have both a stable rest state and a spiking cycle over some range of $y$, and the slow variable must move the system back and forth through this range: spiking drives $y$ in one direction until the spiking state is lost, quiescence drives it back until rest is lost. A burst therefore begins with a bifurcation of the rest state of the fast subsystem and ends with a bifurcation of its spiking state, and Izhikevich named the types of bursting by this pair. With four bifurcations of rest and four of spiking there are sixteen types of "point–cycle" bursters in planar fast subsystems; a few are common.

### 7.4.2. Fold/Homoclinic Bursting

The $I_{\mathrm{Na,p}} + I_{\mathrm{K}}$ model with a fast $\ce{K+}$ current ($g_{\mathrm{K}} = 9$, $\tau_n = 0.152\,\mathrm{ms}$) is bistable over a range of currents, like panel D of Figure 1. Adding a slow, M-type $\ce{K+}$ current $g_{\mathrm{slow}}\,n_{\mathrm{s}}(V - E_{\mathrm{K}})$ with $\tau_{\mathrm{slow}} = 20\,\mathrm{ms}$ turns it into a burster (Figure 3). The geometry is read from panel B, where the slow gate $n_{\mathrm{s}}$ is the bifurcation parameter of the fast subsystem:

- The equilibria of the fast subsystem form a Z-shaped curve. Its lower branch (rest) ends at a fold, a saddle-node bifurcation at $n_{\mathrm{s}} = 0.0035$.
- The spiking cycle exists for $n_{\mathrm{s}}$ below about 0.066, where it ends in a saddle homoclinic orbit bifurcation on the middle branch. Rest and spiking coexist for $0.0035 < n_{\mathrm{s}} < 0.066$.
- During quiescence $V$ is low, $n_{\mathrm{s}}$ decays, and the state drifts left along the rest branch until it falls off the fold: the burst starts. During spiking $n_{\mathrm{s}}$ increases with each spike until the cycle hits the saddle: the burst ends, and the state drops to the rest branch.

The burst is therefore a hysteresis loop of the fast subsystem, driven by the slow variable. At $I = 5\,\mu\mathrm{A\,cm^{-2}}$ each burst contains nine spikes and the bursts recur every 85 ms. The interspike intervals within a burst grow from 0.9 to 2.1 ms, the logarithmic slowing of the cycle as it approaches the homoclinic bifurcation (Definition 7.2.1). This "fold/homoclinic" pattern, also called square-wave bursting because of its plateau, was first analyzed in models of pancreatic β cells (Chay and Keizer 1983; Rinzel 1987).

![Fold/homoclinic (square-wave) bursting in the $I_\mathrm{Na,p}+I_\mathrm{K}+I_\mathrm{K(M)}$ model at $I = 5$ µA cm⁻². A: membrane potential (top) and the slow K⁺ gate $n_\mathrm{s}$ (bottom), which rises during each burst and decays between bursts. B: fast–slow analysis. With $n_\mathrm{s}$ frozen, the fast subsystem has a Z-shaped curve of equilibria (solid: stable rest; dashed: unstable) and, for small $n_\mathrm{s}$, a spiking limit cycle (dots: maximum and minimum of $V$). The burst trajectory (thin line) leaves the rest branch at its lower knee, a fold (saddle-node) bifurcation, spikes while $n_\mathrm{s}$ increases, and stops when the cycle ends in a saddle homoclinic orbit bifurcation](./plots/bursting.py)

### 7.4.3. Other Types

Three other types are common enough to have classical names.

| Type (Izhikevich) | Classical name | Burst starts / ends by | Signature | Example |
|---|---|---|---|---|
| fold / homoclinic | square-wave | saddle-node / saddle homoclinic | bistable; intraburst ISIs lengthen toward the end | pancreatic β cells, pre-Bötzinger neurons |
| circle / circle | parabolic | SNIC / SNIC | rate rises and falls within the burst (ISI as a parabola); needs two slow variables | *Aplysia* R15 neuron |
| subHopf / fold cycle | elliptic | subcritical Andronov–Hopf / fold limit cycle | bistable; subthreshold oscillations of growing amplitude start the burst and decaying ones follow it | rodent trigeminal interneurons, dorsal root ganglion and mesencephalic V neurons |
| fold / circle | triangular | saddle-node / SNIC | rate decreases toward the end of the burst | thalamocortical relay neuron model |

A circle/circle burster cannot be driven by a single slow variable in a planar fast subsystem, because the SNIC curve does not create the needed bistability; two slow variables, one oscillating, are needed (in R15, a slow inward $\ce{Ca^2+}$ current and a $\ce{Ca^2+}$-activated $\ce{K+}$ current). Elliptic bursters, in contrast, are resonators: their bursts can be started or stopped by inputs timed to the subthreshold oscillation. The classical names refer to the shape of the voltage trace, which is not reliable (many subHopf/fold cycle bursters do not look elliptic), so the names by bifurcation are preferred.

## 7.5. Bursting in Physiology

*Thalamic relay neurons.* The interplay of the T-type $\ce{Ca^2+}$ current and $I_{\mathrm{h}}$ ([7.16.5](/7.16.5#sec-5.4)) produces rhythmic bursting at 0.5–4 Hz when the neuron is hyperpolarized: $I_{\mathrm{h}}$ slowly depolarizes the cell, which triggers a low-threshold $\ce{Ca^2+}$ spike crowned by $\ce{Na+}$ spikes; the depolarization deactivates $I_{\mathrm{h}}$ and inactivates $I_{\mathrm{T}}$, the cell hyperpolarizes, $I_{\mathrm{h}}$ reactivates, and the cycle repeats. Neuromodulators of the brainstem arousal systems (acetylcholine, noradrenaline, serotonin) depolarize relay neurons and shift $I_{\mathrm{h}}$, switching them from burst mode to tonic mode at waking ([7.16.35](/7.16.35)). The bursts are not only a sleep phenomenon: in the awake state, bursts after brief hyperpolarization signal the onset of a stimulus with high reliability, acting as a "wake-up call" to the cortex.

*Pancreatic β cells.* In the β cells of the islets of Langerhans ([7.14.35](/7.14.35#sec-35.7)), glucose metabolism raises the ATP/ADP ratio, closes $\mathrm{K_{ATP}}$ channels and depolarizes the cell into a regime of square-wave bursting, with $\ce{Ca^2+}$ spikes on plateaus lasting seconds; the $\ce{Ca^2+}$ entering during the plateaus triggers insulin secretion. The slow variable is a combination of intracellular $\ce{Ca^2+}$ (acting on $\ce{Ca^2+}$-activated $\ce{K+}$ channels) and the ATP/ADP ratio. The fraction of time spent in the active phase increases with glucose, so the cell encodes glucose concentration in its plateau fraction (Chay and Keizer 1983). Sulfonylurea drugs for type 2 diabetes act by closing $\mathrm{K_{ATP}}$ channels and thus shifting the cells further into the bursting regime.

*Pacemakers of rhythmic behavior.* Neurons of the pre-Bötzinger complex of the brainstem, which generates the inspiratory rhythm, burst through a persistent $\ce{Na+}$ current with slow inactivation (and a $\ce{Ca^2+}$-activated nonselective cation current), a fold/homoclinic mechanism in which slow inactivation of $I_{\mathrm{Na,p}}$ is the slow variable (Butera, Rinzel and Smith 1999). Intrinsic bursting of this kind supplies the rhythm of many **central pattern generators**, and in the crab stomatogastric ganglion the AB neuron is a conditional burster whose bursting depends on neuromodulators. How bursting neurons and reciprocal inhibition generate locomotor rhythms is the subject of [7.16.30](/7.16.30).

Bursts carry information differently from single spikes. A burst is transmitted more reliably across synapses with low release probability, because facilitation makes the later spikes of the burst effective ([7.16.12](/7.16.12)), and it may encode stimulus features in the number of spikes it contains. Bursts are also a potent trigger of synaptic plasticity ([7.16.14](/7.16.14)).

## Summary

- A stable rest state can be lost in four generic ways: saddle-node, saddle-node on invariant circle, supercritical and subcritical Andronov–Hopf (Definitions 7.1.1 and 7.1.2); the spiking cycle can be lost through the reverse bifurcations, a fold of limit cycles, or a saddle homoclinic orbit (Definition 7.2.1).
- The bifurcation determines the neuron's computational class: integrator or resonator (real or complex eigenvalues), monostable or bistable (coincident bifurcations or not), class 1 (only the SNIC) or class 2.

| | bistable | monostable |
|---|---|---|
| integrator | saddle-node | SNIC (class 1) |
| resonator | subcritical Andronov–Hopf | supercritical Andronov–Hopf |

- Bistability produces hysteresis and allows brief pulses to switch a neuron between rest and spiking (Figure 2).
- Bursting is a hysteresis loop of a fast subsystem driven by a slow variable (Definition 7.4.1), named by the bifurcations that start and end the burst: fold/homoclinic (square-wave), circle/circle (parabolic), subHopf/fold cycle (elliptic), fold/circle.
- Thalamic relay neurons, β cells and respiratory pacemakers burst through different currents but by the same geometric mechanism.

## Questions

1. Near a saddle homoclinic orbit bifurcation the period of the cycle is approximately $T \approx -\lambda_{\mathrm{u}}^{-1}\ln(I - I_{\mathrm{h}}) + T_0$, where $\lambda_{\mathrm{u}}$ is the unstable eigenvalue of the saddle. Compare the rate at $I - I_{\mathrm{h}} = 10^{-2}$ and $10^{-4}$ (in units of the current scale) with that of a SNIC, whose period is $\pi/\sqrt{I - I_{\mathrm{c}}}$, taking $\lambda_{\mathrm{u}} = 1$ and $T_0 = 1$.

   **Answer** Homoclinic: $T = \ln 100 + 1 = 5.6$ and $\ln 10^4 + 1 = 10.2$, rates $0.18$ and $0.10$. SNIC: $T = \pi/0.1 = 31$ and $\pi/0.01 = 314$, rates $0.032$ and $0.0032$. Reducing the distance by a factor 100 lowers the SNIC rate tenfold but the homoclinic rate less than twofold; the homoclinic onset is practically a jump, which is why it is not counted as class 1 in practice.

2. A neuron fires periodically at 15 Hz when a current is switched on, and small current pulses at rest elicit damped oscillations at 12 Hz. A brief pulse delivered during firing at a particular phase silences the neuron permanently. Identify the bifurcation and the neurocomputational class.

   **Answer** Damped oscillations at rest mean a stable focus: a resonator, so the bifurcation is of Andronov–Hopf type. A pulse can silence the firing at the same current, so rest and spiking coexist: the neuron is bistable. The bifurcation is a subcritical Andronov–Hopf, and the onset at a finite frequency (15 Hz, near the oscillation frequency) makes the neuron class 2.

3. In the fold/homoclinic burster of Figure 3, predict what happens to the number of spikes per burst and the interburst interval when $\tau_{\mathrm{slow}}$ is doubled, assuming the bifurcation diagram of the fast subsystem is unchanged.

   **Answer** The fast subsystem, and therefore the values of $n_{\mathrm{s}}$ at the fold (0.0035) and at the homoclinic bifurcation (0.066), do not depend on $\tau_{\mathrm{slow}}$. Doubling $\tau_{\mathrm{slow}}$ halves the rate at which $n_{\mathrm{s}}$ rises during spiking and decays during quiescence. The burst then takes about twice as long to drive $n_{\mathrm{s}}$ from the fold to the homoclinic point, so it contains about twice as many spikes (at nearly the same intraburst rate), and the silent phase lasts about twice as long. Burst period and spike number both roughly double.

4. (Open question) Explain why bursting requires at least three state variables when the fast subsystem is two-dimensional, and give a physiological example in which the slow variable is not a gating variable.

   **Answer** Spikes need a two-dimensional fast subsystem (an amplifying and a recovery variable, as in [7.16.6](/7.16.6)), and the alternation between rest and spiking needs at least one slow variable that moves the fast subsystem through its bistable range, so at least $2 + 1 = 3$ variables are required. (A planar system cannot burst: its trajectories cannot cross, so it cannot alternate between a fixed point and a cycle.) In pancreatic β cells and many neurons the slow variable is the intracellular $\ce{Ca^2+}$ concentration, which rises during the active phase and activates $\ce{Ca^2+}$-dependent $\ce{K+}$ channels; in respiratory pacemakers the extracellular or intracellular $\ce{Na+}$ concentration acting on the $\ce{Na+}/\ce{K+}$ pump can play the same role.
