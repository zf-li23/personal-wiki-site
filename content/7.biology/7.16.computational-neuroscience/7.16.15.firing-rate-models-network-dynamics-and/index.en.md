---
title: Firing-Rate Models, Network Dynamics and Oscillations
description: "From spiking neurons to firing-rate equations; linear networks: eigenmodes, selective amplification, integration and non-normal (balanced) amplification; stability of nonlinear networks, linearization and its limits, Lyapunov functions; excitatory–inhibitory networks: the Wilson–Cowan model and its Hopf bifurcation, the inhibition-stabilized network and the paradoxical effect; gamma oscillations by PING and ING; phase response curves, phase reduction and the locking of coupled oscillators; the balanced state."
---

The preceding chapters built the parts of a network: neurons that integrate and fire ([7.16.4](/7.16.4)–[7.16.8](/7.16.8)), synapses with their time courses and short-term dynamics ([7.16.12](/7.16.12)), dendrites that combine inputs ([7.16.13](/7.16.13)) and rules that change synaptic weights ([7.16.14](/7.16.14)). This chapter asks what networks of such neurons do as dynamical systems. Its main tool is the firing-rate model, which replaces spikes by rates and makes networks of thousands of neurons analyzable with linear algebra and the phase plane. We use it to explain how recurrent connections amplify, integrate and select inputs, why cortex is thought to operate in an inhibition-stabilized regime in which stimulating inhibitory neurons lowers their own firing, and how excitatory–inhibitory loops generate oscillations; we then return to spikes to understand how oscillating neurons synchronize. The rate model and the half-center oscillator are introduced in [7.14.6](/7.14.6#sec-6.4), the general theory of planar systems and the Hopf bifurcation in [2.4.11](/2.4.11) and [7.6.33](/7.6.33#sec-33.5), and gene-regulatory versions of the same motifs in [7.9.16](/7.9.16). The networks of this chapter are the starting point for the ring models of visual cortex ([7.16.18](/7.16.18)), Hebbian learning ([7.16.22](/7.16.22)), chaotic and balanced networks ([7.16.31](/7.16.31)) and attractor networks ([7.16.43](/7.16.43)–[7.16.45](/7.16.45)).

## 15.1. From Spikes to Firing Rates

### 15.1.1. The Rate Equation

Let neuron $j$ emit the **spike train** $\rho_j(t) = \sum_k\delta(t - t_{j,k})$, and let its synapses onto neuron $i$ have weight $w_{ij}$ (we write $w_{ij}$ for the connection *from* $j$ *to* $i$, so that the weight matrix $W$ acts on the vector of presynaptic activities from the left). With exponential synaptic kernels of time constant $\tau_{\mathrm{s}}$ ([Definition 12.2.2](/7.16.12#def-12.2.2)), the total synaptic input current of neuron $i$ obeys
$$
\tau_{\mathrm{s}}\frac{\mathrm{d}I_i}{\mathrm{d}t} = -I_i + \sum_j w_{ij}\,\tau_{\mathrm{s}}\rho_j(t). \tag{15.1}
$$
Two approximations turn this into a closed equation (Dayan and Abbott, ch. 7). First, replace each spike train by its **firing rate** $r_j(t)$, the expected value of $\rho_j$; this is accurate when each neuron receives many weakly correlated inputs, so that the sum in Eq. (15.1) averages out the individual spikes, or when $r_j$ is the rate of a population. Second, assume that the output rate follows the input current instantaneously through a gain function, $r_i = F(I_i)$, the steady-state f–I curve of the neuron ([7.16.8](/7.16.8)); this is accurate when $\tau_{\mathrm{s}}$ is longer than the membrane time constant. One then obtains $\tau_{\mathrm{s}}\dot{\boldsymbol{I}} = -\boldsymbol{I} + W F(\boldsymbol{I})$. If instead the synapses are fast and the rate lags its input with a time constant $\tau_{\mathrm{r}}$, one obtains the form used in the rest of this chapter.

**Formula 15.1.1 (Firing-Rate Network)** The rates $\boldsymbol{r} = (r_1, \dots, r_N)$ of a network with weight matrix $W$ and external input $\boldsymbol{h}$ obey
$$
\tau_{\mathrm{r}}\frac{\mathrm{d}\boldsymbol{r}}{\mathrm{d}t} = -\boldsymbol{r} + F\bigl(W\boldsymbol{r} + \boldsymbol{h}\bigr), \tag{15.2}
$$
with $F$ applied componentwise. Common gain functions are the threshold-linear function $F(x) = [x]_+ = \max(x, 0)$ and the sigmoid $F(x) = r_{\max}/(1 + \mathrm{e}^{-(x - \theta)/\sigma})$.

Eq. (15.2) is the **rate model** of [Definition 6.4.1](/7.14.6#def-6.4.1) written for a network. What it gives up is the timing of individual spikes, and with it synchrony, which is the subject of 15.6. What it gains is that the dynamics of a network reduce to a system of $N$ ordinary differential equations whose fixed points and stability can be studied with linear algebra. When $\boldsymbol{r}$ stands for populations of excitatory and inhibitory cells, $\tau_{\mathrm{r}}$ differs between them, and we write $\tau_E$ and $\tau_I$.

## 15.2. Linear Networks

### 15.2.1. Eigenmodes and Selective Amplification

In the range where $F$ is linear (all rates above threshold, gain 1), Eq. (15.2) becomes
$$
\tau\frac{\mathrm{d}\boldsymbol{r}}{\mathrm{d}t} = -\boldsymbol{r} + W\boldsymbol{r} + \boldsymbol{h}. \tag{15.3}
$$
If $W$ is symmetric, it has real **eigenvalues** $\lambda_\mu$ and orthonormal **eigenvectors** $\boldsymbol{e}_\mu$ (here $\lambda$ is an eigenvalue, not a length constant). Writing $\boldsymbol{r} = \sum_\mu c_\mu\boldsymbol{e}_\mu$ decouples the network into independent modes.

**Proposition 15.2.1 (Selective Amplification)** For symmetric $W$ and constant input, the mode amplitudes obey $\tau\dot c_\mu = -(1 - \lambda_\mu)c_\mu + \boldsymbol{h}\cdot\boldsymbol{e}_\mu$. The network is stable if and only if all $\lambda_\mu < 1$; then each mode relaxes with time constant $\tau/(1 - \lambda_\mu)$ to
$$
c_\mu^\infty = \frac{\boldsymbol{h}\cdot\boldsymbol{e}_\mu}{1 - \lambda_\mu}. \tag{15.4}
$$

**Proof** Take the scalar product of Eq. (15.3) with $\boldsymbol{e}_\mu$ and use $\boldsymbol{e}_\mu^{\mathsf T}W = \lambda_\mu\boldsymbol{e}_\mu^{\mathsf T}$ (symmetry): $\tau\dot c_\mu = -c_\mu + \lambda_\mu c_\mu + \boldsymbol{h}\cdot\boldsymbol{e}_\mu$. A linear scalar equation $\dot c = -ac + b$ is stable iff $a > 0$, with fixed point $b/a$. $\square$

Recurrent excitation therefore does two things to an input pattern. It amplifies the components along eigenvectors with $\lambda_\mu$ close to 1, by the factor $1/(1 - \lambda_\mu)$, and suppresses the others; and it slows down those amplified modes by the same factor. A recurrent network acts as a filter in the space of patterns that selects the pattern favored by its connectivity, which is how the ring model of orientation tuning sharpens weakly tuned feedforward input ([7.16.18](/7.16.18)). In the limit $\lambda_1 \to 1$ the time constant diverges: the mode neither decays nor grows, and the network integrates its input along $\boldsymbol{e}_1$ ($\tau\dot c_1 = \boldsymbol{h}\cdot\boldsymbol{e}_1$). Such a line attractor is the classical model of the oculomotor integrator that converts velocity commands into eye position ([7.16.33](/7.16.33)); it requires $\lambda_1$ tuned to 1 within about $1\%$ to give the time constants of tens of seconds observed, a fine-tuning problem.

### 15.2.2. Planar Systems and the E–I Loop

For two populations the stability of Eq. (15.3) is decided by the trace $T = \operatorname{tr}A$ and determinant $\Delta = \det A$ of the system matrix $A$: the eigenvalues are $\lambda_\pm = \bigl(T \pm \sqrt{T^2 - 4\Delta}\bigr)/2$, the fixed point is stable iff $T < 0$ and $\Delta > 0$, and it is a spiral iff $T^2 < 4\Delta$ (the classification of planar linear systems in [2.4.11](/2.4.11#sec-11.5.2)). Consider an excitatory and an inhibitory population with weights $w_{EE}, w_{EI}, w_{IE}, w_{II} \ge 0$, where $w_{EI}$ is the strength of the connection from $I$ to $E$:
$$
\tau_E\dot r_E = -r_E + w_{EE}r_E - w_{EI}r_I + h_E, \qquad \tau_I\dot r_I = -r_I + w_{IE}r_E - w_{II}r_I + h_I. \tag{15.5}
$$
Then
$$
T = \frac{w_{EE} - 1}{\tau_E} - \frac{1 + w_{II}}{\tau_I}, \qquad \Delta = \frac{(1 - w_{EE})(1 + w_{II}) + w_{EI}w_{IE}}{\tau_E\tau_I}. \tag{15.6}
$$
Without recurrent excitation ($w_{EE} = 0$) the trace is always negative and the determinant positive: a negative feedback loop of two first-order elements is always stable. It can ring, a damped oscillation when $w_{EI}w_{IE}$ is large, but it cannot oscillate persistently. Recurrent excitation raises the trace, and when $w_{EE} > 1 + (\tau_E/\tau_I)(1 + w_{II})$ with $\Delta > 0$, the trace becomes positive while the eigenvalues are complex: the fixed point loses stability through a pair of complex eigenvalues crossing the imaginary axis. In the linear system the oscillation then grows without bound; in a network with saturating $F$ it settles on a **limit cycle**, the **Hopf bifurcation** of 15.4.1. Oscillation in an E–I network thus needs a delay (here provided by the two time constants), negative feedback (through $I$) and enough recurrent excitation, the same ingredients as in biochemical oscillators ([7.9.16](/7.9.16#sec-16.4)).

### 15.2.3. Non-Normal Amplification

Cortical connectivity is not symmetric: excitatory neurons make only positive and inhibitory neurons only negative connections (Dale's law), so $W$ has columns of fixed sign. If $W$ is not a **normal matrix** ($WW^{\mathsf T} \ne W^{\mathsf T}W$), its eigenvectors are not orthogonal and the eigenvalues no longer describe the transient dynamics.

**Definition 15.2.1 (Non-Normal Amplification)** **Non-normal amplification** is the transient growth of activity in a linear network whose weight matrix is not normal: although all eigenvalues of $W - I$ have negative real parts, so that every input eventually decays, some initial patterns are transformed into other patterns of much larger norm before decaying, through effectively feedforward connections between non-orthogonal modes.

The simplest example is a feedforward chain. With $W = \begin{bmatrix}0 & 0\\ w & 0\end{bmatrix}$ (unit 1 drives unit 2), both eigenvalues of $W$ are 0, yet after an initial activation $r_1(0) = 1$ the response of unit 2 is $r_2(t) = w\,(t/\tau)\,\mathrm{e}^{-t/\tau}$, which peaks at $w/\mathrm{e}$ at $t = \tau$. Murphy and Miller (2009) showed that E–I networks with strong, balanced connections contain a hidden chain of this kind. For $W = w\begin{bmatrix}1 & -k\\ 1 & -k\end{bmatrix}$ (each population receives the same excitation and inhibition), the eigenvalues are $w(1 - k)$ and $0$, both below 1 for $k > 1$, but a "difference" pattern, $r_E$ above and $r_I$ below baseline, drives the "sum" pattern with feedforward weight $w(1 + k)$. Strong recurrent excitation balanced by strong inhibition therefore amplifies transiently without slowing the dynamics, unlike the selective amplification of 15.2.1. This *balanced amplification* is a candidate explanation for the large, fast transients of cortical responses and for the spontaneous patterns of activity that resemble evoked ones; non-normal dynamics are also central to the rotational dynamics of motor cortex ([7.16.32](/7.16.32)).

## 15.3. Nonlinear Networks and the Limits of Linearization

Eq. (15.2) is nonlinear, and its fixed points $\boldsymbol{r}^*$ solve $\boldsymbol{r}^* = F(W\boldsymbol{r}^* + \boldsymbol{h})$. Near a **fixed point** the dynamics is approximated by the linear system with the **Jacobian matrix**
$$
J = \frac{1}{\tau}\left(-I_N + DW\right), \qquad D = \operatorname{diag}\bigl(F'(W\boldsymbol{r}^* + \boldsymbol{h})\bigr), \tag{15.7}
$$
so a fixed point is stable if all eigenvalues of $J$ have negative real parts and unstable if one has a positive real part (Lyapunov's first method, [2.4.11](/2.4.11#sec-11.3)). The gains $F'$ enter as effective weights: the same network can be stable at a low-rate fixed point, where the neurons are near threshold and $F'$ is small, and unstable at a high-rate one. Linearization fails when an eigenvalue has zero real part, which is the case at every bifurcation point and for centers: the nonlinear terms then decide.

**Example 15.3.1** The system $\dot x = -y - x^3$, $\dot y = x - y^3$ has the fixed point $(0, 0)$ with Jacobian $\begin{bmatrix}0 & -1\\ 1 & 0\end{bmatrix}$, eigenvalues $\pm\mathrm{i}$: the linearization is a center and says nothing about stability. The **Lyapunov function** $V(x, y) = x^2 + y^2$ settles the question: $\dot V = 2x(-y - x^3) + 2y(x - y^3) = -2(x^4 + y^4) < 0$ for $(x, y) \ne (0, 0)$, so the origin is asymptotically stable; trajectories spiral in, slowly.

:::

Lyapunov functions have no general construction, but for one class of networks they are known. If $W$ is symmetric and $F$ is monotonic, the network has an energy function that decreases along all trajectories (Cohen and Grossberg, 1983; Hopfield, 1984), so every trajectory ends at a fixed point: such networks cannot oscillate and are the basis of the **Hopfield network** and of attractor models of memory ([7.16.43](/7.16.43)). Oscillations and chaos therefore require asymmetric connectivity, in particular separate excitatory and inhibitory populations.

## 15.4. Excitatory–Inhibitory Networks

### 15.4.1. The Wilson–Cowan Model

**Definition 15.4.1 (Wilson–Cowan Model)** The **Wilson–Cowan model** describes the fractions $E(t)$ and $I(t)$ of active cells in coupled excitatory and inhibitory populations by
$$
\tau_E\frac{\mathrm{d}E}{\mathrm{d}t} = -E + f\bigl(w_{EE}E - w_{EI}I + h_E\bigr), \qquad \tau_I\frac{\mathrm{d}I}{\mathrm{d}t} = -I + f\bigl(w_{IE}E - w_{II}I + h_I\bigr), \tag{15.8}
$$
with a sigmoidal gain function $f$ (Wilson and Cowan, 1972, in a simplified form without the refractory factor of the original).

The **nullclines** are the curves on which $\dot E = 0$ or $\dot I = 0$. Because the E nullcline $I = (w_{EE}E + h_E - f^{-1}(E))/w_{EI}$ is N-shaped when $w_{EE}$ is large (recurrent excitation creates a region of positive feedback) and the I nullcline is increasing, the model has the same geometry as the FitzHugh–Nagumo neuron ([7.16.6](/7.16.6)): a fixed point on the middle branch of the N is unstable when excitation is strong and inhibition slow, and the trajectory runs around a limit cycle, a population oscillation. Varying the drive $h_E$ moves the fixed point along the E nullcline. Starting from a low-activity state, the fixed point loses stability in a Hopf bifurcation when it reaches the middle branch and regains it in a second Hopf bifurcation at high activity: oscillations exist in a window of intermediate drive, and their frequency depends on the drive (figure below). The same model with other parameters has two stable fixed points (low and high activity), which is the simplest model of bistability in cortex. Wilson–Cowan equations, with populations distributed in space, also produce traveling waves and the stationary patterns proposed to underlie visual hallucinations.

![Oscillations in the Wilson–Cowan model (Definition 15.4.1; $f(x) = 1/(1 + \mathrm{e}^{-(x - 4)})$, $w_{EE} = 10$, $w_{EI} = 10$, $w_{IE} = 8$, $w_{II} = 2$, $\tau_E = 5\,\mathrm{ms}$, $\tau_I = 10\,\mathrm{ms}$, $h_I = 0$). A: phase plane at $h_E = 3$: the N-shaped E nullcline (blue), the I nullcline (red), the unstable fixed point (open circle), and a trajectory (gray) spiraling out onto the limit cycle (purple). B: bifurcation diagram: fixed point $E^*$ (solid where stable, dashed where unstable) and the minimum and maximum of $E$ on the limit cycle (dots) against $h_E$; Hopf bifurcations near $h_E = 1.35$ and $4.5$ bound the oscillatory window. Near the lower bifurcation the cycle appears with large amplitude. C: oscillation frequency against $h_E$ (dots), with the small-amplitude estimate $\operatorname{Im}\lambda/2\pi$ from the Jacobian (line), which is accurate only near the bifurcations.](./plots/wilson-cowan-hopf.py)

### 15.4.2. The Inhibition-Stabilized Network and the Paradoxical Effect

Suppose that recurrent excitation is so strong that the excitatory population on its own would be unstable, its activity exploding or collapsing, and that the network is kept stable only by inhibitory feedback.

**Definition 15.4.2 (Inhibition-Stabilized Network)** An **inhibition-stabilized network** (ISN) is an excitatory–inhibitory network at a stable fixed point at which the excitatory subnetwork alone, with the inhibitory rates held fixed, would be unstable; for the threshold-linear model of Eq. (15.5) with both populations active, this is the condition $w_{EE} > 1$ together with stability of the full system ($T < 0$, $\Delta > 0$ in Eq. (15.6)).

An ISN responds to stimulation of its inhibitory cells in a way that seems to contradict their function.

**Proposition 15.4.1 (Paradoxical Effect)** At a stable fixed point of Eq. (15.5) with both populations above threshold,
$$
\frac{\partial r_I^*}{\partial h_I} = \frac{1 - w_{EE}}{\delta}, \qquad \frac{\partial r_E^*}{\partial h_I} = -\frac{w_{EI}}{\delta}, \qquad \delta = (1 - w_{EE})(1 + w_{II}) + w_{EI}w_{IE} > 0. \tag{15.9}
$$
Hence an increase of the external drive to the inhibitory population decreases the steady-state inhibitory rate if and only if the network is inhibition-stabilized ($w_{EE} > 1$); the excitatory rate decreases in both regimes.

**Proof** The fixed point solves the linear system $\begin{bmatrix}1 - w_{EE} & w_{EI}\\ -w_{IE} & 1 + w_{II}\end{bmatrix}\begin{bmatrix}r_E^*\\ r_I^*\end{bmatrix} = \begin{bmatrix}h_E\\ h_I\end{bmatrix}$, whose determinant is $\delta = \tau_E\tau_I\Delta > 0$ by stability. By Cramer's rule $r_I^* = ((1 - w_{EE})h_I + w_{IE}h_E)/\delta$ and $r_E^* = ((1 + w_{II})h_E - w_{EI}h_I)/\delta$; differentiate with respect to $h_I$. $\square$

**Definition 15.4.3 (Paradoxical Effect)** The **paradoxical effect** is the decrease of the steady-state firing of inhibitory neurons in response to an increase of their external excitatory drive, together with a decrease of excitatory firing; it is the signature of an inhibition-stabilized network.

The mechanism is visible in the phase plane (figure below, A). In an ISN the E nullcline has positive slope, because more inhibition is needed to hold back more excitation. Extra drive to the inhibitory cells transiently raises $r_I$, which lowers $r_E$; because the excitatory cells provide most of the input to the inhibitory ones, the loss of recurrent excitation outweighs the extra drive, and the new fixed point has both rates lower. The inhibitory rate first rises and then settles below its initial value (B). In a network without strong recurrent excitation the same stimulation raises $r_I$ (C).

**Example 15.4.1** With $w_{EE} = 1.5$, $w_{EI} = 2$, $w_{IE} = 4$, $w_{II} = 2$ and $\tau_E = \tau_I = \tau$, the system matrix of Eq. (15.5) is $\begin{bmatrix}0.5 & -2\\ 4 & -3\end{bmatrix}/\tau$ with eigenvalues $(-1.25 \pm 2.22\,\mathrm{i})/\tau$: a stable spiral, although the excitatory subnetwork alone has eigenvalue $+0.5/\tau$. With $h_E = 10$ and $h_I = 1$, $\delta = -0.5\cdot3 + 8 = 6.5$, $r_E^* = (30 - 2)/6.5 = 4.31$ and $r_I^* = (-0.5 + 40)/6.5 = 6.08$. Raising $h_I$ to 5 gives $r_E^* = 3.08$ and $r_I^* = 5.77$: the inhibitory rate falls by $0.31$.

:::

The ISN was proposed as a model of hippocampal and cortical networks by Tsodyks, Skaggs, Sejnowski and McNaughton (1997). Its first experimental support came from surround suppression in cat V1 (Ozeki, Finn, Schaffer, Miller and Ferster, 2009): a large grating suppresses the response of a neuron to a small one, and one would expect this to be caused by increased inhibition; intracellular recordings showed instead that both the excitatory and the inhibitory conductances decreased during suppression, as an ISN predicts when the surround drives inhibitory cells. The direct test is optogenetic: stimulating inhibitory interneurons in mouse cortex in vivo produces the paradoxical decrease of their firing, in every cortical area and behavioral state tested (Sanzeni and colleagues, 2020). Cortex therefore appears to operate with recurrent excitation strong enough to be unstable on its own, stabilized dynamically by inhibition, a regime that makes it fast and sensitive and that the balanced networks of 15.7 and [7.16.31](/7.16.31) take to the limit.

![The paradoxical effect in a threshold-linear E–I network (Eq. (15.5); $\tau_E = 20\,\mathrm{ms}$, $\tau_I = 10\,\mathrm{ms}$, $h_E = 10$; $h_I$ steps from 1 to 5 at $t = 0$). A: phase plane of the inhibition-stabilized network of Example 15.4.1: E nullcline (blue, positive slope), I nullcline before (solid red) and after (dashed) the step, and the two fixed points: the fixed point moves to lower $r_E$ and lower $r_I$. B: time courses in the ISN: $r_I$ rises transiently, then settles below its initial value. C: a network that is not inhibition-stabilized ($w_{EE} = 0.5$, $w_{EI} = 1.5$, $w_{IE} = 3$, $w_{II} = 1$): $r_I$ rises and stays higher.](./plots/isn-paradoxical.py)

## 15.5. Brain Oscillations

### 15.5.1. Rhythms and Their Mechanisms

Extracellular recordings and the **electroencephalogram** show rhythms that are classified by frequency ([7.14.46](/7.14.46#sec-46.3)): delta ($0.5$–$4\,\mathrm{Hz}$, deep sleep), theta ($4$–$8\,\mathrm{Hz}$ in humans; $6$–$10\,\mathrm{Hz}$ in the rodent hippocampus during locomotion and exploration), alpha ($8$–$12\,\mathrm{Hz}$), beta ($13$–$30\,\mathrm{Hz}$) and gamma ($30$–$80\,\mathrm{Hz}$ and above). Oscillations also organize the output of **central pattern generators** for rhythmic movements and appear in primary motor cortex and sensory areas in response to stimuli. They arise in three ways: from pacemaker neurons with intrinsic rhythmic properties ([7.16.7](/7.16.7)), from circuits with reciprocal inhibition such as the **half-center oscillator** ([7.14.6](/7.14.6#sec-6.4.3), [7.16.11](/7.16.11#sec-11.5.2)), and from the excitatory–inhibitory loops of cortex, which generate gamma oscillations.

### 15.5.2. PING and ING

**Definition 15.5.1 (PING and ING)** In the **PING** (pyramidal–interneuron network gamma) mechanism a gamma oscillation is generated by an excitatory–inhibitory loop: a volley of excitatory spikes recruits the inhibitory interneurons, whose inhibition silences the excitatory cells until it decays, after which they fire the next volley. In the **ING** (interneuron network gamma) mechanism the rhythm is generated by mutually inhibiting interneurons alone, driven tonically, which synchronize through their inhibitory synapses.

In both mechanisms the period is set mainly by the decay of inhibition: the excitatory (or inhibitory) cells fire again when the inhibitory conductance has decayed enough, a few $\mathrm{GABA_A}$ decay time constants after each volley, which places the rhythm at $30$–$80\,\mathrm{Hz}$ (figure below). In PING the excitatory cells fire sparsely and irregularly, each skipping many cycles, while the population rhythm is regular; this agrees with recordings, in which individual pyramidal cells fire far below the gamma frequency. The models are distinguished experimentally by the phase relation (in PING the excitatory volley precedes the inhibitory one by a few milliseconds) and by whether the rhythm survives blockade of AMPA receptors on interneurons. Parvalbumin-expressing fast-spiking basket cells are central to both: driving them optogenetically generates gamma oscillations in cortex, with a resonance near $40\,\mathrm{Hz}$, whereas driving pyramidal cells does not (Cardin and colleagues, 2009; Sohal and colleagues, 2009). Gap junctions between these interneurons ([7.16.12](/7.16.12#sec-12.4)) add to their synchrony.

![Gamma oscillations in a spiking network of 400 excitatory and 100 inhibitory leaky integrate-and-fire neurons (conductance-based synapses, AMPA decay $2\,\mathrm{ms}$, $\mathrm{GABA_A}$ decay $8\,\mathrm{ms}$, random connectivity with probability $0.5$, constant drive plus independent noise). A: spike raster over $200\,\mathrm{ms}$ (100 excitatory cells below, all inhibitory cells above): volleys of inhibitory spikes follow the excitatory ones every $18\,\mathrm{ms}$ or so, while each excitatory cell fires on only a few cycles. B: population rates of the two populations ($2\,\mathrm{ms}$ bins). C: power spectrum of the excitatory population rate, with a peak near $55\,\mathrm{Hz}$ that disappears when the connection from excitatory to inhibitory cells is removed (gray): the rhythm is PING. D: frequency of the spectral peak against the decay time constant of inhibition: slower inhibition gives a slower rhythm, from about $65\,\mathrm{Hz}$ at $5\,\mathrm{ms}$ to $30\,\mathrm{Hz}$ at $20\,\mathrm{ms}$.](./plots/ping-gamma.py)

### 15.5.3. What Oscillations Might Do

The functions proposed for oscillations are many and their status varies. Gamma oscillations define windows of excitability every $10$–$30\,\mathrm{ms}$, and coherent oscillations between two areas could gate which signals are transmitted ("communication through coherence", Fries, 2005). Theta oscillations organize the firing of hippocampal place cells, which fire at progressively earlier phases as the animal crosses the field (phase precession, [7.16.42](/7.16.42)), and the nesting of gamma cycles within theta cycles has been proposed as a code for sequences and for the capacity of working memory ([7.16.45](/7.16.45)). Sleep oscillations (slow oscillations, spindles and sharp-wave ripples) coordinate the replay of activity that is thought to consolidate memories ([7.16.35](/7.16.35)). In each case the evidence is mostly correlational, and oscillations may sometimes be a by-product of E–I dynamics rather than a mechanism; manipulating their timing selectively, for example by closed-loop optogenetic stimulation, is the test that separates the two.

## 15.6. Synchronization of Oscillating Neurons

### 15.6.1. Phase Response Curves

Rate models describe populations; to understand how two rhythmically firing neurons, or two oscillating populations, align their spikes, we describe each oscillator by a single phase. A neuron firing periodically with period $T$ moves around a **limit cycle**, and its state can be labeled by the phase $\varphi \in [0, 1)$, the fraction of the period elapsed since the last spike.

**Definition 15.6.1 (Phase Response Curve)** The **phase response curve** (PRC) $Z(\varphi)$ of a periodically firing neuron is the advance of its next spike, as a fraction of the period, caused by a brief input of fixed small size (a current pulse or a synaptic conductance) delivered at phase $\varphi$, normalized by the size of the input. A PRC of **type 1** is nonnegative for all phases: excitatory input only advances the next spike. A PRC of **type 2** has a negative region, usually early in the cycle: excitatory input there delays the next spike.

The PRC is measured directly by delivering pulses at different phases and recording the shift of the next spike. Its type reflects the bifurcation by which the neuron starts to fire ([7.16.7](/7.16.7)). Near a saddle-node on invariant circle bifurcation (class 1 excitability, the theta neuron and the quadratic integrate-and-fire model), the PRC approaches $Z(\varphi) \propto 1 - \cos 2\pi\varphi$, positive everywhere and largest in mid-cycle. Near a Hopf bifurcation (class 2 excitability, the Hodgkin–Huxley model), the PRC approaches $-\sin 2\pi\varphi$ shifted in phase, with a negative lobe after the spike, when depolarization speeds the recovery processes that delay the next spike, and a positive lobe before it (figure below, A). Cortical pyramidal cells mostly have type 1 PRCs and some interneurons type 2; neuromodulators such as acetylcholine can switch a cell from one to the other by modulating its M current (Stiefel, Gutkin and Sejnowski, 2009).

### 15.6.2. Phase Reduction and Locking

If the coupling between two oscillators is weak, each stays near its limit cycle, and the input it receives only shifts its phase. For two identical neurons with intrinsic period $T$, each receiving a synaptic input $\varepsilon\,s(\varphi_{\mathrm{other}})$ that depends on the phase of the other, the phase obeys $\dot\varphi_1 = 1/T + \varepsilon Z(\varphi_1)\,s(\varphi_2)$. Averaging over one cycle (Kuramoto, Ermentrout and Kopell) gives an equation for the slow drift of the phase difference.

**Theorem 15.6.1 (Phase Model of Two Coupled Oscillators)** To first order in the coupling strength $\varepsilon$, the phase difference $\psi = \varphi_2 - \varphi_1$ of two identical, symmetrically coupled oscillators obeys
$$
\frac{\mathrm{d}\psi}{\mathrm{d}t} = \varepsilon\,G(\psi), \qquad G(\psi) = H(-\psi) - H(\psi), \qquad H(\chi) = \int_0^1 Z(\varphi)\,s(\varphi + \chi)\,\mathrm{d}\varphi, \tag{15.10}
$$
where $H$ is the interaction function. The zeros $\psi^*$ of $G$ are the phase-locked states, stable if $G'(\psi^*) < 0$.

**Proof** (Sketch.) Over one cycle the phases advance almost uniformly, $\varphi_i(t) \approx t/T + \theta_i$ with slowly varying $\theta_i$. Averaging $\varepsilon Z(\varphi_1)s(\varphi_2)$ over the period at fixed $\theta_i$ replaces it by $\varepsilon H(\theta_2 - \theta_1)$ (in units of cycles per period); symmetrically, oscillator 2 receives $\varepsilon H(\theta_1 - \theta_2)$. Subtracting the two equations gives Eq. (15.10); a zero $\psi^*$ of $G$ with negative slope attracts nearby $\psi$. The averaging theorem justifies the approximation for small $\varepsilon$. $\square$

**Definition 15.6.2 (Phase-Locked State)** A **phase-locked state** of two or more coupled oscillators is a solution in which all oscillate with a common frequency and their phase differences remain constant; the state with zero phase difference is synchrony, that with a phase difference of half a cycle antiphase.

Because $G$ is odd and periodic, $\psi = 0$ and $\psi = 1/2$ are always phase-locked states; what the PRC decides is which are stable. For a delta synapse ($s$ a pulse at the presynaptic spike) $H(\chi) = Z(-\chi)$, so $G'(0) = 2Z'(0)$: synchrony is stable when the PRC decreases through the spike phase, that is, when input arriving just after the spike delays the next one, which is the type 2 shape. With realistic synaptic time courses the general rule (Hansel, Mato and Meunier, 1995; van Vreeswijk, Abbott and Ermentrout, 1994) is that fast excitation synchronizes type 2 oscillators but drives type 1 oscillators toward antiphase, while inhibition with slow decay synchronizes type 1 oscillators: "when inhibition, not excitation, synchronizes". This is one reason why networks of interneurons (ING) synchronize so readily. For a population of many oscillators with interaction $H(\chi) = \sin 2\pi\chi$ and different natural frequencies, the same reduction gives the **Kuramoto model**, whose transition to partial synchrony is analyzed in [7.9.16](/7.9.16#sec-16.4.7).

![Phase response curves and the locking they predict. A: PRCs measured by the direct method (spike advance per small kick, normalized) for a theta neuron, the normal form of class 1 excitability (blue, type 1, all positive and largest in mid-cycle), and for the Hodgkin–Huxley model at $10\,\mu\mathrm{A\,cm^{-2}}$ (red, type 2, a negative lobe in the first half of the cycle). B: the odd part $G(\psi)$ of the interaction function (Eq. (15.10)) for excitatory coupling through an exponential synapse with a decay of $5\%$ of the period: filled dots are stable, open circles unstable phase-locked states; synchrony is unstable for the theta neurons, which lock in antiphase, and stable for the Hodgkin–Huxley neurons, which also have a stable antiphase state separated by unstable states near $\pm0.4$. C: direct simulation of two coupled neurons of each type started $0.3$ cycles apart: the theta neurons move toward antiphase (spike-time difference $0.5$), the Hodgkin–Huxley neurons toward synchrony, as predicted.](./plots/prc-locking.py)

## 15.7. The Balanced State

Cortical neurons receive thousands of excitatory inputs, each able to depolarize them by about $0.5\,\mathrm{mV}$; if these were not cancelled, a few percent of them active at a few hertz would drive the neuron far above threshold. Yet cortical neurons fire irregularly at low rates. Van Vreeswijk and Sompolinsky (1996) showed that strong excitation and inhibition can cancel dynamically.

**Definition 15.7.1 (Balanced State)** In a network in which each neuron receives $K$ excitatory and $K$ inhibitory inputs with synaptic weights of order $1/\sqrt K$, the **balanced state** is the regime in which the total excitatory and the total inhibitory inputs to each neuron are each of order $\sqrt K$, much larger than the distance from rest to threshold, but cancel to a net mean input of order 1, so that the neurons are driven by the fluctuations of their input and fire irregularly.

The balance is not tuned but emerges. To leading order in $\sqrt K$ the mean inputs must vanish, which for an excitatory and an inhibitory population with external input $r_0$ gives the linear equations
$$
J_{EE}r_E - J_{EI}r_I + J_{E0}r_0 = 0, \qquad J_{IE}r_E - J_{II}r_I + J_{I0}r_0 = 0, \tag{15.11}
$$
with $J_{ab} > 0$ the scaled connection strengths from $b$ to $a$. They have a positive solution, and the balanced state exists, if $J_{E0}/J_{I0} > J_{EI}/J_{II} > J_{EE}/J_{IE}$. The rates are then linear functions of the input, whatever the nonlinearity of the single neurons, and they follow changes of input with a speed limited by the synapses rather than by the membrane time constant. Intracellular recordings in vivo confirm that excitatory and inhibitory conductances are large and track each other closely, with inhibition lagging excitation by a few milliseconds (Okun and Lampl, 2008). Balanced networks, their chaotic dynamics and their relation to the ISN regime are the subject of [7.16.31](/7.16.31).

## Summary

- Firing-rate models (Formula 15.1.1) replace spike trains by rates; they are accurate for asynchronous populations and slow synapses and reduce networks to systems of ordinary differential equations. Weights $w_{ij}$ run from $j$ to $i$.
- In linear networks with symmetric $W$, each eigenmode is amplified by $1/(1 - \lambda_\mu)$ and slowed by the same factor (Proposition 15.2.1); $\lambda \to 1$ gives an integrator. Non-normal connectivity (Definition 15.2.1) amplifies transiently without slowing, as in balanced amplification.
- The stability of nonlinear networks follows from the Jacobian (Eq. (15.7)) except at bifurcation points and centers, where Lyapunov functions (Example 15.3.1) or the full nonlinear analysis are needed; symmetric networks have energy functions and cannot oscillate.
- An E–I loop oscillates only with enough recurrent excitation (Eq. (15.6)); the Wilson–Cowan model (Definition 15.4.1) shows the resulting Hopf bifurcations and limit cycles.
- In an inhibition-stabilized network (Definition 15.4.2), driving the inhibitory cells lowers their rate (Proposition 15.4.1, the paradoxical effect, Definition 15.4.3); cortex behaves this way in vivo.
- Gamma oscillations arise by PING or ING (Definition 15.5.1), with a period set by the decay of inhibition; their functions are debated.
- Phase response curves (Definition 15.6.1) determine, through the phase model (Theorem 15.6.1), which phase-locked states (Definition 15.6.2) are stable: excitation synchronizes type 2, inhibition type 1 oscillators.
- In the balanced state (Definition 15.7.1) large excitation and inhibition cancel dynamically, leaving irregular firing and rates linear in the input (Eq. (15.11)).

| Network | Key condition | Behavior |
|---|---|---|
| Linear, symmetric | $\lambda_\mu < 1$ | Selective amplification; integrator at $\lambda = 1$ |
| Linear, non-normal | Hidden feedforward structure | Transient amplification |
| E–I loop, weak $w_{EE}$ | $T < 0$ | Damped oscillation at most |
| Wilson–Cowan | Strong $w_{EE}$, slow inhibition | Hopf bifurcation, limit cycle |
| ISN | $w_{EE} > 1$, stable | Paradoxical response to driving $I$ |
| Spiking E–I | Fast E, slower I | Gamma by PING |
| Balanced | Weights $\sim 1/\sqrt K$ | Irregular firing, linear rates |

## Questions

1. A symmetric network has eigenvalues $\lambda_1 = 0.95$, $\lambda_2 = 0.5$ and $\lambda_3 = -1$ with $\tau = 10\,\mathrm{ms}$. An input has equal projections on the three eigenvectors. Give the steady-state amplitudes of the three modes relative to the input and their relaxation time constants. What happens if $\lambda_1$ is raised to $1.02$?

   **Answer** By Proposition 15.2.1 the gains are $1/(1 - \lambda)$: $20$, $2$ and $0.5$, and the time constants $\tau/(1 - \lambda)$: $200\,\mathrm{ms}$, $20\,\mathrm{ms}$ and $5\,\mathrm{ms}$. The output is dominated by mode 1, which is also slow: amplification costs speed. If $\lambda_1 = 1.02$, mode 1 is unstable and grows as $\mathrm{e}^{0.02t/\tau}$, doubling every $350\,\mathrm{ms}$, until the nonlinearity of $F$ (saturation or rectification) stops it: the linear analysis no longer applies, and the network may settle in a new, high-activity fixed point.

2. Using Eq. (15.9), show that in the threshold-linear E–I network an increase of the drive to the excitatory population always increases $r_E^*$ at a stable fixed point. Can stimulation of the excitatory cells produce a paradoxical decrease of their rate in this model?

   **Answer** By Cramer's rule $\partial r_E^*/\partial h_E = (1 + w_{II})/\delta$, and $\delta > 0$ at a stable fixed point, so the derivative is positive; also $\partial r_I^*/\partial h_E = w_{IE}/\delta > 0$. In this two-population linear model, stimulation of the excitatory cells never lowers their rate. A paradoxical response of excitatory cells requires additional structure, for example several inhibitory populations with disinhibitory connections (somatostatin cells inhibiting parvalbumin cells), nonlinear gain functions, or stimulation of only a subset of the excitatory cells.

3. Compute the trace and determinant of the linearized system (15.6) for the network without self-connections ($w_{EE} = w_{II} = 0$, $w_{EI} = 2$, $w_{IE} = 3$, $\tau_E = 10\,\mathrm{ms}$, $\tau_I = 5\,\mathrm{ms}$). Is the fixed point a node or a spiral, and with what frequency and decay time does it ring?

   **Answer** $T = -1/10 - 1/5 = -0.3\,\mathrm{ms^{-1}}$ and $\Delta = (1 + 6)/50 = 0.14\,\mathrm{ms^{-2}}$. $T^2 - 4\Delta = 0.09 - 0.56 < 0$: a stable spiral with eigenvalues $-0.15 \pm \mathrm{i}\sqrt{0.14 - 0.0225} = -0.15 \pm 0.343\,\mathrm{i}\,\mathrm{ms^{-1}}$. It rings at $0.343/(2\pi)\,\mathrm{kHz} \approx 55\,\mathrm{Hz}$ with an amplitude decay time of $1/0.15 \approx 6.7\,\mathrm{ms}$, so it rings for only one or two cycles: a damped gamma-like resonance, which needs recurrent excitation (or noise and nonlinearity) to become a sustained oscillation.

4. For a delta-pulse synapse, $H(\chi) = Z(-\chi)$. Using $Z_1(\varphi) = 1 - \cos 2\pi\varphi$ and $Z_2(\varphi) = -\sin 2\pi\varphi$, compute $G(\psi)$ for both and decide whether synchrony and antiphase are stable for excitatory coupling ($\varepsilon > 0$).

   **Answer** $G(\psi) = H(-\psi) - H(\psi) = Z(\psi) - Z(-\psi)$. For $Z_1$, which is even, $G \equiv 0$: with instantaneous pulses the type 1 PRC gives neutral stability, and the synaptic time course or the shape details decide (with a finite synaptic decay, synchrony becomes unstable, as in the figure). For $Z_2$, $G(\psi) = -2\sin 2\pi\psi$; $G'(0) = -4\pi < 0$, so synchrony is stable, and $G'(1/2) = 4\pi > 0$, so antiphase is unstable. Excitatory pulse coupling synchronizes type 2 oscillators.

5. (Open question) How would you test experimentally whether a gamma rhythm in a cortical slice is generated by PING or by ING?

   **Answer** Record pyramidal cells and fast-spiking interneurons simultaneously (or the field potential with unit activity) and measure the phase relation: in PING the pyramidal volley precedes the interneuron volley by a few milliseconds in each cycle, in ING interneurons fire without a preceding excitatory volley. Then block AMPA receptors (or specifically the AMPA receptors on interneurons, genetically): PING should disappear, ING should persist if the interneurons are driven tonically (for example by metabotropic agonists or kainate). Prolonging $\mathrm{GABA_A}$ decay with a benzodiazepine or a barbiturate should slow both rhythms; optogenetic silencing of pyramidal cells at specific phases tests whether their volley is necessary for the next inhibitory volley.
