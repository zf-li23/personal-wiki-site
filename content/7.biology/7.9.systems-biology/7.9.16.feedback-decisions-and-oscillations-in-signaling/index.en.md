---
title: Feedback, Decisions and Oscillations in Signaling and Development
description: "Network motifs with feedback: positive autoregulation, two-node positive loops (lock-on and toggle), the CI–Cro decision of phage λ, regulated and regulating feedback as cellular memory, transcriptional cascades and developmental timing; ultrasensitivity and the multiplication of response coefficients in kinase cascades, the loop-gain criterion for bistability, oocyte maturation, robust bistability from two positive loops, hybrid transcription–protein motifs and the stability of feed-forward loops; motifs of neuronal networks and multi-input FFLs; how to build an oscillator: two-node loops and noise-induced oscillations, delay oscillators, coupled positive and negative feedback for tunable frequency, Ca²⁺ oscillations in the Li–Rinzel model, cell-cycle and circadian clocks, Kuramoto synchronization; and information encoded in pulse frequency."
---

The motifs of sensory transcription networks ([7.9.15](/7.9.15)) are built to respond reversibly to the present environment, and they avoid feedback. Cells also need to make decisions that outlast the signal that caused them, to switch fate once and for all, and to keep time; for these tasks evolution uses feedback loops, and the networks of development, signaling and neurons are rich in them. This chapter follows the motifs with feedback from transcription networks to protein networks and to oscillators, asking for each what it computes and why one design is used rather than another.

The dynamical-systems tools are not repeated here: fixed points, **nullclines**, linear stability, the **saddle-node bifurcation**, the **Hopf bifurcation** and the Poincaré–Bendixson theorem are in [2.4.11](/2.4.11) and, applied to the **genetic toggle switch**, the *lac* operon, the **Goodwin oscillator**, the **repressilator** and **relaxation oscillators**, in [7.6.33](/7.6.33); positive feedback, bistability, adaptation and Ca²⁺ oscillations as cell biology are in [7.3.18](/7.3.18#sec-18.4); the cell-cycle oscillator is in [7.3.20](/7.3.20#sec-20.6) and [7.6.34](/7.6.34#sec-34.2.1); and the kinetic modeling and fitting of such networks in general is in [7.9.14](/7.9.14). We begin with developmental transcription networks (16.1), move to signaling networks (16.2) and neurons (16.3), treat the design of oscillators (16.4), and end with information encoded in dynamics (16.5). Noise in these circuits, and the robustness of their behavior, is the subject of [7.9.17](/7.9.17).

## 16.1. Motifs of Developmental Networks

### 16.1.1. Sensory and Developmental Networks

Developmental transcription networks govern the nearly irreversible transitions by which a cell becomes a different cell type. The networks of sea urchins, flies, worms and mammals contain most of the motifs of sensory networks, the feed-forward loop ([7.9.15](/7.9.15#def-15.4.1); mostly of types C1 and I1), autoregulation and single-input modules, and in addition a few motifs that sensory networks lack: many more positive autoregulation loops, two-node positive feedback loops, larger motifs built around them, and long transcriptional cascades (Milo and colleagues, 2004; Levine and Davidson, 2005). They work on the time scale of cell divisions, so slow responses are not a handicap; and they must remember decisions after the inducing signals are gone.

### 16.1.2. Positive Autoregulation: Slow Responses and Memory

**Proposition 16.1.1 (Positive Autoregulation Slows Responses)** Let $\dot X = f(X) - \alpha X$ with $f$ increasing, and compare it with simple regulation $\dot X = \beta - \alpha X$ with the same removal rate and the same steady state $X_{\mathrm{st}}$ ($\beta = f(X_{\mathrm{st}})$). From any initial state $X(0) < X_{\mathrm{st}}$ in the basin of $X_{\mathrm{st}}$, the autoregulated gene stays below the simply regulated one and reaches every level later.

**Proof** For $X < X_{\mathrm{st}}$, $f(X) < f(X_{\mathrm{st}}) = \beta$, so the autoregulated rate is smaller at every level below the steady state. Two solutions from the same initial value cannot cross, since at a crossing the autoregulated one would have the smaller derivative; it therefore lags behind. $\square$

This is the mirror image of Proposition 15.3.1 of [7.9.15](/7.9.15#prop-15.3.1): production that rises with $X$ is initially slow and accelerates as $X$ accumulates. Slow responses also average out rapidly fluctuating inputs (Hornung and Barkai, 2008). With a sigmoidal $f$, the production curve can cross the removal line three times, and the gene is bistable: a low and a high stable state separated by an unstable threshold ([7.6.33](/7.6.33#sec-33.2.1); Formula 22.6.1 of [7.2.22](/7.2.22#sec-22.6)). A transient input that pushes $X$ above the threshold leaves it locked on: long-term memory. When embryonic cells become muscle, the factor MyoD activates its own gene and keeps the muscle program on in all descendants.

In one dimension, adjacent fixed points of $\dot X = F(X)$ alternate in stability, because $F$ changes sign at each simple root; three fixed points therefore mean stable–unstable–stable, and five fixed points (possible with more complex input functions) mean three stable states.

### 16.1.3. Two-Node Positive Loops

A loop of two factors that regulate each other is positive if both arcs have the same sign.

**Definition 16.1.1 (Lock-On and Toggle Loops)** A *double-positive feedback loop* (lock-on loop) is a two-node loop in which two transcription factors activate each other; its stable states, when it is bistable, have both factors on or both off. A *double-negative feedback loop* is a two-node loop in which they repress each other; its stable states have one factor on and the other off, the **genetic toggle switch** of [Definition 33.3.1 of 7.6.33](/7.6.33#def-33.3.1).

Lock-on loops suit factors whose targets belong to the same tissue, toggles factors whose targets belong to alternative fates (PU.1 and GATA1, Cdx2 and Oct4; [7.6.33](/7.6.33#sec-33.3.3)). Why two-node loops, if one-node positive autoregulation can already lock on? One reason is the delay: a lock-on loop switches only after both proteins have accumulated, and therefore ignores brief inputs. Both kinds need nonlinearity.

**Proposition 16.1.2 (A Two-Node Loop Without Cooperativity Is Monostable)** Let $\dot X = f(Y) - \alpha_1X$, $\dot Y = g(X) - \alpha_2Y$, where $f$ and $g$ are both increasing or both decreasing Michaelis–Menten (Hill coefficient $1$) functions, $f(y) = a + by/(K + y)$ or $a + b/(1 + y/K)$ with $a, b, K > 0$, and similarly for $g$. Then the system has exactly one fixed point in the positive quadrant, and it is stable.

**Proof** Fixed points satisfy $X = \phi(X) := f(g(X)/\alpha_2)/\alpha_1$. Each of $f$, $g$ is a Möbius transformation $y \mapsto (py + q)/(ry + s)$ restricted to $y \ge 0$, and so is their composition (with the scaling by $\alpha_1, \alpha_2$); $\phi$ is increasing in both cases (an increasing function of an increasing function, or a decreasing of a decreasing), bounded, and a Möbius map that is increasing and bounded on $[0, \infty)$ is strictly concave there ($\phi'' = -2r\phi'/(rX + s) < 0$). A strictly concave $\phi$ with $\phi(0) > 0$ crosses the diagonal exactly once for $X > 0$, from above, so $\phi'(X^*) < 1$ at the crossing. The Jacobian is $\begin{bmatrix}-\alpha_1 & f'\\ g' & -\alpha_2\end{bmatrix}$ with trace $< 0$ and determinant $\alpha_1\alpha_2 - f'g' = \alpha_1\alpha_2(1 - \phi'(X^*)) > 0$, since $\phi' = f'g'/(\alpha_1\alpha_2)$: the fixed point is stable. $\square$

Bistability therefore needs **cooperativity** in at least one arm, or positive autoregulation of the factors, which many fate determinants have and which can make a loop without cooperative binding bistable (Question 3).

### 16.1.4. The Decision of Phage λ

When phage λ infects *E. coli*, it either replicates and lyses the cell or integrates as a **prophage** and is replicated with the host (**lysogeny**). The molecular switch is described in [7.2.11](/7.2.11): CI represses the lytic promoter $P_{\mathrm{R}}$ and activates its own promoter $P_{\mathrm{RM}}$; Cro represses $P_{\mathrm{RM}}$ and, at higher concentrations, its own promoter. In network terms this is a toggle switch with positive autoregulation of CI and negative autoregulation of Cro. To leave lysogeny, the prophage reads the host's damage signal: single-stranded DNA activates RecA, which stimulates the self-cleavage of CI (and of LexA, starting the **SOS response**). A minimal model makes the logic visible.

**Example 16.1.1 (A Minimal Model of the λ Switch)** In dimensionless units, with $c$ the CI and $r$ the Cro concentration,
$$
\frac{\mathrm{d}c}{\mathrm{d}t} = \frac{4(0.05 + c^2)}{1 + c^2 + 4r^2} - (1 + d)\,c, \qquad \frac{\mathrm{d}r}{\mathrm{d}t} = \frac{3}{1 + 4c^2 + (r/3)^2} - r, \tag{16.1}
$$
where $d$ is the additional removal of CI by RecA-stimulated cleavage. Without damage ($d = 0$) the nullclines cross three times: a lysogenic state ($c = 3.74$, $r = 0.05$), a lytic state ($c = 0.01$, $r = 2.05$) and a saddle between them ($c = 0.89$, $r = 0.71$). As $d$ increases, the lysogenic state and the saddle approach each other and annihilate in a saddle-node bifurcation at $d_{\mathrm{c}} = 0.70$; beyond it every trajectory goes to the lytic state. The lytic state exists for all $d$, so repairing the damage afterwards does not restore lysogeny: induction is irreversible. The model is not fitted to data, but the structure (bistability from a positive loop with cooperativity, an exit by a saddle-node bifurcation triggered by a signal that destabilizes one state) is that of the real switch, whose spontaneous switching rate is below $10^{-7}$ per generation in cells without RecA ([7.2.11](/7.2.11)); the stochastic initial decision after infection is discussed in [7.9.17](/7.9.17).

![A minimal model of the CI–Cro switch of phage λ, Eq. (16.1). A: no damage (d = 0): the CI nullcline (violet) and the Cro nullcline (red) cross at a stable lysogenic state (CI high), a stable lytic state (Cro high) and a saddle (open circle); trajectories (black) from different initial conditions go to one of the two stable states. B: with RecA-stimulated cleavage of CI (d = 1) the lysogenic state has disappeared and every trajectory goes to the lytic state. C: CI at the fixed points against d: the lysogenic branch meets the saddle in a saddle-node bifurcation at d_c = 0.70, while the lytic branch persists for all d](./plots/lambda_switch.py)

### 16.1.5. Regulated and Regulating Feedback: Memory

Two-node loops appear inside three-node motifs that are characteristic of developmental networks (Milo and colleagues, 2004).

**Definition 16.1.2 (Regulating and Regulated Feedback)** In a *regulating-feedback* motif, two mutually regulating factors $X$ and $Y$ both regulate a target $Z$. In a **regulated feedback** motif, a two-node feedback loop between $Y_1$ and $Y_2$ is regulated by an upstream factor $X$.

In the common sign combinations, all paths between two vertices have the same overall sign: a double-positive loop whose two factors both activate (or both repress) $Z$, a toggle whose two factors act on $Z$ with opposite signs. Regulated feedback is a memory element. An input $X$ that is active only transiently can lock a double-positive loop on or flip a toggle, and the new state persists after $X$ has disappeared (figure): the circuit records whether $X$ was active in the past. Such memories maintain cell fates after the developmental signals that specified them are gone. They are a property of the network, not of chromatin ([7.2.15](/7.2.15)), and they need not even involve transcription: in *Drosophila* sex determination, early Sxl protein, made only in XX embryos, splices the later *Sxl* transcript into its productive form, so that Sxl maintains its own synthesis by a positive loop at the level of splicing, a bistable switch that converts a transient signal of the X:A ratio into a permanent state ([7.4.6](/7.4.6)).

![Memory in the regulated-feedback motif (logic input functions, all rates 1, thresholds 0.5). The input X is produced for 0 < t < 3 (shaded) and then decays. A: double-positive loop with OR gates (each Y is made if X or the other Y is above threshold): the transient input switches both Y1 and Y2 on, and they stay on. B: toggle: Y1 and Y2 repress each other, X activates Y1 and represses Y2; starting from the Y2 state, the transient input flips the switch to the Y1 state, which persists](./plots/regulated_feedback.py)

### 16.1.6. Cascades and Developmental Timing

Transcriptional cascades $X \to Y \to Z \to \cdots$ are rare in sensory networks, because each step adds a response time of about $\ln 2/\alpha$, one cell generation for stable proteins. In development, where cell fates are assigned over successive divisions, this is the right time scale, and long cascades are common. Cascades of repressors give timing that is more robust to fluctuations in production rates than cascades of activators (Rappaport, Winter and Barkai, 2005): a repressor whose production stops is diluted by a fixed factor per generation, so the time at which it falls below a threshold depends only logarithmically on its initial level. In *Drosophila* neuroblasts, a temporal cascade of transcription factors (Hunchback, Krüppel, Pdm, Castor) specifies the neurons born in successive divisions, and its timing has been explained by a repressor-decay timer (Averbukh and colleagues, 2018).

## 16.2. Signaling Networks

### 16.2.1. Ultrasensitivity and the Multiplication of Gains

Protein interaction networks work by binding, modification and degradation of existing proteins, in seconds to minutes. Their typical motif for making decisions is the combination of an ultrasensitive module with positive feedback. The sources of **ultrasensitivity** (cooperativity, multisite modification, **zero-order ultrasensitivity**, cascades, stoichiometric inhibitors) are listed in [7.3.18](/7.3.18#sec-18.4.2), and the steady state of the **MAP kinase cascade** is computed in [7.1.15](/7.1.15#sec-15.1.4). The language of **response coefficients** makes the role of each element exact.

**Proposition 16.2.1 (Response Coefficients Multiply Along a Cascade)** Let the steady state of a cascade be $y_1 = f_1(s)$, $y_k = f_k(y_{k-1})$ for $k = 2, \dots, m$, and let $R_k = \mathrm{d}\ln y_k/\mathrm{d}\ln y_{k-1}$ be the local response coefficient of tier $k$ ($y_0 = s$). Then the response coefficient of the whole cascade is
$$
\frac{\mathrm{d}\ln y_m}{\mathrm{d}\ln s} = \prod_{k=1}^{m}R_k. \tag{16.2}
$$

**Proof** The chain rule applied to $\ln y_m = \ln f_m(\exp\ln y_{m-1})$, and so on down the cascade. $\square$

A Hill function $x^n/(K^n + x^n)$ has response coefficient $n/(1 + (x/K)^n)$, equal to $n$ at low input and falling to zero at saturation; a distributive double phosphorylation has $R = 2$ at low input. In the cascade of the figure the three tiers have, at low input, $R = 1$, $2$ and $2$, and the cascade has $R = 4$; the apparent Hill coefficients $\ln 81/\ln(E_{90}/E_{10})$ of the three tiers are $1.0$, $1.7$ and $3.2$. Ultrasensitivity alone gives a steep but reversible response. With positive feedback, it gives bistability, and the condition is again a statement about gains.

**Proposition 16.2.2 (Loop Gain and Instability)** Let $\dot x = F(x, s) - \gamma x$ with $F$ increasing in $x$ (positive feedback), and let $x^* > 0$ be a fixed point. Then $x^*$ is unstable if and only if the logarithmic gain of the loop exceeds one,
$$
\frac{\partial\ln F}{\partial\ln x}\bigg|_{x^*} > 1. \tag{16.3}
$$
Consequently the system can be bistable only if the feedback is ultrasensitive somewhere: if $F(x, s) = s + G(x)$ with $G$ a Hill function of coefficient $n \le 1$, it has a single fixed point.

**Proof** The linearization is $\delta\dot x = (\partial_xF - \gamma)\delta x$, unstable iff $\partial_xF > \gamma$. At the fixed point $\gamma = F/x^*$, so the condition is $x^*\partial_xF/F > 1$. For $G(x) = bx^n/(K^n + x^n)$, $\partial\ln F/\partial\ln x = xG'/(s + G) \le xG'/G = n/(1 + (x/K)^n) < n \le 1$, so no fixed point is unstable; with no unstable fixed point between them, two stable fixed points cannot coexist in one dimension. $\square$

**Example 16.2.1 (Oocyte Maturation)** In *Xenopus* oocytes, progesterone triggers the synthesis of the MAPKKK Mos; Mos activates the cascade Mos → MEK → p42 MAPK, and active MAPK promotes the synthesis and stabilization of Mos. Individual oocytes respond all-or-none and stay mature after progesterone is removed ([Example 18.4.1 of 7.3.18](/7.3.18#ex-18.4.1); Ferrell and Machleder, 1998; Xiong and Ferrell, 2003). In the model of the figure, $\dot M = s + f\,m_3(M) - M$, with the cascade at steady state for the input $M$. For $f = 0.3$ the response is steep but single valued; for $f = 0.5$ it is bistable between $s = 0.085$ and $s = 0.141$, with hysteresis; for $f = 1$ the lower fold lies at $s = -0.20 < 0$, so once switched on the oocyte stays on even without stimulus, an irreversible switch. The cascade is needed: with a single tier ($R \le 1$) Proposition 16.2.2 forbids bistability for any $f$.

![The MAPK cascade and positive feedback (steady-state model with the double-phosphorylation formula of 7.1.15, K = 1). A: active fraction of each tier against the input E, with apparent Hill coefficients 1.0, 1.7 and 3.2. B: local response coefficients of the three tiers and of the whole cascade; the product of the tiers (dashed) coincides with the response coefficient of the cascade (Proposition 16.2.1), which is 4 at low input. C: feedback from MAPK to the synthesis of the top kinase, dM/dt = s + f m₃(M) − M: steady-state MAPK activity against the stimulus s for f = 0 (graded), 0.3 (steep), 0.5 (bistable, with an unstable middle branch, dashed) and 1 (irreversible: the lower fold lies at s < 0)](./plots/mapk_cascade.py)

### 16.2.2. Two Positive Loops Make Bistability Robust

The Cdk1 switch of the cell cycle has two positive loops: active cyclin B–Cdk1 activates its activating phosphatase Cdc25 and inhibits its inhibitory kinase Wee1 (Wee1 phosphorylates Tyr15 of Cdk1, Cdc25 removes the phosphate; [Definition 20.3.3 of 7.3.20](/7.3.20#def-20.3.3)). Why two? Ferrell (2008) proposed an answer with a rate plot. With one loop, the activation rate $k_{25}(a)(1 - a)$ of the active fraction $a$ is a hump (rising with the feedback, falling to zero as the inactive pool is exhausted), while the inactivation rate $w\,a$ is a straight line whose slope is the Wee1 level $w$; three intersections occur only for a narrow range of slopes. With both loops, the inactivation rate $w\,k_{\mathrm{wee}}(a)\,a$ is also humped, falling at high $a$ because active Cdk1 inhibits Wee1, and the two humped curves intersect three times over a much wider range of $w$.

**Example 16.2.2** With activation $(0.01 + H(a))(1 - a)$, $H(a) = a^3/(0.3^3 + a^3)$, and inactivation $w\,a$ (one loop) or $w\,(0.01 + 1 - H(a))\,a$ (two loops), the switch is bistable for $0.277 < w < 1.19$ with one loop, a $4.3$-fold range of Wee1 activity, and for $0.275 < w < 4.99$ with two loops, an $18$-fold range (figure). Because the Wee1 and Cdc25 levels vary between cells and conditions, the wider range makes the existence of the switch, and of the relaxation oscillation built on it (16.4.4), robust. The measured hysteresis of the Cdk1 switch in egg extracts ([Example 20.6.1 of 7.3.20](/7.3.20#ex-20.6.1)) is the experimental basis; the specific factors of robustness depend on the parameters chosen.

![Two positive feedback loops widen the bistable range of the Cdk1 switch. A: one loop (Cdk1 activates Cdc25): the activation rate (green) is a hump and the inactivation rates (dashed, for three Wee1 levels w) are straight lines. B: two loops (Cdk1 also inhibits Wee1): the inactivation rates are humped too. C: active Cdk1 at the fixed points against w on a logarithmic axis (solid: stable, dashed: unstable): the bistable range is 4.3-fold with one loop and 18-fold with two](./plots/robust_bistability.py)

### 16.2.3. Hybrid Motifs

Transcription networks and protein networks are coupled: many signaling pathways end in transcription factors, and transcription makes the proteins of signaling pathways. The combined network has arcs of two kinds, slow transcriptional and fast protein-level, and its motifs mix them (Yeger-Lotem and colleagues, 2004).

**Definition 16.2.1 (Hybrid Motif)** A **hybrid motif** (mixed motif) is a network motif of a network with several types of arcs, here transcriptional regulation and protein–protein interaction, whose arcs are not all of the same type.

The most common hybrid motif is a two-node negative feedback loop in which a transcription factor $X$ activates the gene of a protein $Y$, and $Y$ inhibits $X$ at the protein level, by promoting its degradation or by binding and inactivating it: p53 and its ubiquitin ligase Mdm2, NF-κB and its inhibitor IκBα, and the end products of metabolic pathways that inhibit the first enzyme while repressing the pathway's genes. Purely transcriptional two-node negative loops are rare. Control engineering suggests a reason: a slow process controlled by a fast sensor, like a heater controlled by a thermostat, is stable around its set point, whereas two slow arms in a loop produce overshoot and oscillation, as the next section makes precise (Proposition 16.4.1: the tendency to oscillate is greatest when the two arms have similar time scales). A hybrid feed-forward loop in the mating pathway of budding yeast, in which a transcription factor induces both a kinase and its substrate, acts as a persistence detector and, because the kinase lingers for its lifetime, gives a transient memory of recent pheromone exposure: cells that saw the signal recently respond faster (Doncic and Skotheim, 2013).

Feed-forward loops behave as milder versions of feedback loops: coherent FFLs delay and give transient memory as positive feedback gives lasting memory, incoherent FFLs make pulses and speed responses as negative feedback does. But FFLs cannot oscillate.

**Proposition 16.2.3 (Feed-Forward Networks Are Stable)** Let $\dot x_i = f_i(x_1, \dots, x_{i-1}) - \alpha_ix_i$, $i = 1, \dots, m$, with $\alpha_i > 0$: each variable is regulated only by variables earlier in a fixed order (a network whose arcs form a **directed acyclic graph**, such as any combination of FFLs and cascades), with constant inputs. Then the system has a unique steady state, which is globally asymptotically stable; in particular it has no periodic orbits.

**Proof** The steady state is found recursively, $x_1^* = f_1/\alpha_1$, $x_i^* = f_i(x_1^*, \dots, x_{i-1}^*)/\alpha_i$. The Jacobian is lower triangular with diagonal $-\alpha_i$, so all eigenvalues are negative. Globally, $x_1(t) \to x_1^*$ exponentially; given that $x_1, \dots, x_{i-1}$ converge, $x_i$ obeys a stable linear equation with a convergent input and converges to $x_i^*$. A periodic orbit would contradict convergence. $\square$

## 16.3. Motifs in Neuronal Networks

Network motifs can be sought in any network with a suitable randomized ensemble ([7.9.15](/7.9.15#sec-15.2.2)). The neuronal network of *Caenorhabditis elegans*, about $300$ neurons connected by about $5000$ chemical synapses and mapped by electron microscopy (White, Southgate, Thomson and Brenner, 1986), shares the feed-forward loop with transcription networks as its most significant three-node motif, and three-node feedback cycles are anti-motifs (Milo and colleagues, 2002). This is surprising, since neurons and transcription factors differ in size by three orders of magnitude and in time scale by four. One explanation, that nearby neurons tend to connect and that spatial proximity produces triangles, predicts that three-cycles should be as enriched as FFLs, which they are not (Itzkovitz and Alon, 2005). The alternative is that both networks process noisy signals with noisy components, and evolution converged on similar circuits for similar tasks.

The FFLs are combined differently. Instead of the multi-output FFLs of transcription networks, neurons of *C. elegans* form multi-input FFLs.

**Definition 16.3.1 (Multi-Input Feed-Forward Loop)** A **multi-input feed-forward loop** is a motif in which several input vertices $X_1, \dots, X_n$ each regulate an intermediate vertex $Y$ and an output $Z$, and $Y$ regulates $Z$: a set of FFLs that share $Y$ and $Z$.

In the escape circuit, the sensory neurons for nose touch (FLP) and for noxious chemicals (ASH) both excite the interneuron AVD and the command interneuron AVA, which drives backward movement, and AVD excites AVA. With coherent FFLs whose intermediate neuron sums its inputs, such a circuit is a coincidence detector: two brief stimuli, each too weak to drive the output alone, drive it when they arrive close together in time, because their effects on $Y$ add up within its integration time (Question 6). A related structure, proposed by Melzack and Wall (1965) in the gate-control theory of pain, has large-diameter afferents (touch) that excite both a spinal projection neuron and an inhibitory interneuron that silences it, an incoherent FFL, and small-diameter nociceptive afferents that excite the projection neuron and inhibit the interneuron, a coherent FFL of type 2. Activity of the large fibers closes the gate, which is why rubbing a painful spot helps; the circuitry of the dorsal horn has turned out to be considerably more complex than the original model, but the gating principle has survived. The dynamics of neurons and synapses is the subject of [computational neuroscience](/7.16).

## 16.4. How to Build an Oscillator

### 16.4.1. Negative Feedback Needs Delay

Every biological oscillator contains a negative feedback loop, but a loop is not enough: negative autoregulation, a one-variable system, cannot oscillate at all ([7.6.33](/7.6.33#sec-33.2.3)). With two variables, a negative loop can produce damped oscillations only.

**Proposition 16.4.1 (The Two-Node Negative Loop)** Let $X$ activate $Y$ and $Y$ repress $X$, $\dot X = f(Y) - \alpha_1X$, $\dot Y = g(X) - \alpha_2Y$, with $f$ decreasing and $g$ increasing, and let $\beta_1 = -f'(Y^*) > 0$ and $\beta_2 = g'(X^*) > 0$ at the fixed point. Then the fixed point is stable, with eigenvalues
$$
\lambda_{1,2} = \frac{-(\alpha_1 + \alpha_2) \pm \sqrt{(\alpha_1 - \alpha_2)^2 - 4\beta_1\beta_2}}{2}, \tag{16.4}
$$
and the approach to it is a damped oscillation if and only if $(\alpha_1 - \alpha_2)^2 < 4\beta_1\beta_2$.

**Proof** The Jacobian $\begin{bmatrix}-\alpha_1 & -\beta_1\\ \beta_2 & -\alpha_2\end{bmatrix}$ has trace $-(\alpha_1 + \alpha_2) < 0$ and determinant $\alpha_1\alpha_2 + \beta_1\beta_2 > 0$, so both eigenvalues have negative real parts; they are complex exactly when the discriminant is negative. $\square$

Equal time scales favor oscillation (for $\alpha_1 = \alpha_2$ every negative loop overshoots), and a strong separation of time scales suppresses it, which is why the hybrid loops of 16.2.3 are stable. Sustained oscillations need either a third ingredient, delay or positive feedback, or noise.

### 16.4.2. Noise Can Sustain Damped Oscillations

Lahav and colleagues (2004) imaged p53 and Mdm2 in single human cells after γ-irradiation and saw not damped oscillations but sustained pulses of p53, with Mdm2 pulsing in antiphase, roughly every $5.5\,\mathrm{h}$. The amplitudes of the pulses varied widely from pulse to pulse and cell to cell, while their timing was more regular (Geva-Zatorsky and colleagues, 2006). Such statistics are the signature of a damped oscillator driven by noise: random kicks keep pushing the system away from its stable spiral, and the circuit amplifies the part of the noise near its resonance frequency. The models of p53 used to explain these pulses include delays and more components ([7.6.33](/7.6.33#sec-33.5.5)); the point here is the mechanism by which a circuit that only rings on paper can pulse in a cell.

**Example 16.4.1** For $\dot x = 10/(1 + y^8) - x$, $\dot y = x - y$ (time in removal times), the fixed point $x^* = y^* = 1.27$ has eigenvalues $-1 \pm 2.64\mathrm{i}$: deterministic perturbations decay within about one period. With independent white noise of intensity $\sigma$ added to both equations (a chemical Langevin description, [7.6.32](/7.6.32#sec-32.6.1)), the trajectory pulses indefinitely. In a simulation of $3000$ time units, the heights of the peaks have a coefficient of variation of $0.51$, the intervals between peaks one of $0.36$, and the power spectrum peaks near the frequency $0.38$, a period of $2.6$, whatever the noise strength: doubling $\sigma$ multiplies the spectrum by four without changing its shape, which agrees with the spectrum of the linearized system (the linear noise approximation of [7.6.32](/7.6.32#sec-32.6.2)). Amplitudes that vary more than periods, and grow with the noise, are the diagnostic of noise-induced oscillations.

![Noise-sustained oscillations of a two-node negative loop, dx/dt = 10/(1 + y⁸) − x, dy/dt = x − y, with white noise (Euler–Maruyama, 3000 time units). A: a deterministic perturbation decays to the stable spiral (black), while the noisy trajectory (σ = 0.1, violet) keeps pulsing. B: distributions of peak heights (above x*) and of intervals between peaks, each divided by its mean: heights vary more (CV 0.51) than intervals (CV 0.36). C: power spectra of x for σ = 0.1 and 0.2, divided by σ², and the spectrum of the linearized system (dashed): the resonance, and hence the typical period, does not depend on the noise](./plots/noise_induced.py)

### 16.4.3. Delay Oscillators

With three or more stages, a negative loop can oscillate without noise, if the repression is steep enough and the stages have similar time scales: the secant condition for the Goodwin oscillator and the stability boundary of the repressilator are derived in [7.6.33](/7.6.33#sec-33.5.1). The longer the loop, the weaker the cooperativity required, and an explicit delay (the time to transcribe, splice, export and translate) acts like many stages; the period is then of the order of twice the total delay around the loop. The segmentation clock, in which Hes and Her factors repress their own genes with a delay, is analyzed as a delay oscillator in [7.5.23](/7.5.23#sec-23.3.2). Delay oscillators produce nearly sinusoidal waves whose amplitude and period are both set by the same balance of gain and delay.

### 16.4.4. Coupling Positive and Negative Feedback

The best-studied biological oscillators, the cell cycle, heart pacemaker cells, neurons, have in addition to the negative loop a positive loop: the oscillator motif.

**Definition 16.4.1 (Coupled Positive–Negative Feedback Oscillator)** A **coupled positive–negative feedback oscillator** is an oscillator whose core is a negative feedback loop between an activator $X$ and an inhibitor $Y$ ($X$ activates $Y$, $Y$ inhibits $X$) together with a positive feedback loop on $X$ (positive autoregulation of $X$ or a two-node positive loop through which $X$ enhances its own activity).

Positive feedback helps in two ways. Locally, it destabilizes the fixed point. For $\dot X = f(X, Y) - \alpha_1X$, $\dot Y = g(X) - \alpha_2Y$, with $P = \partial f/\partial X > 0$ the strength of the positive loop, the Jacobian $\begin{bmatrix}P - \alpha_1 & -\beta_1\\ \beta_2 & -\alpha_2\end{bmatrix}$ has trace $P - \alpha_1 - \alpha_2$ and determinant $\alpha_2(\alpha_1 - P) + \beta_1\beta_2$. If the determinant stays positive, the fixed point loses stability when $P$ exceeds $\alpha_1 + \alpha_2$, with complex eigenvalues if $(\alpha_1 - P - \alpha_2)^2 < 4\beta_1\beta_2$ at that point: a Hopf bifurcation, after which bounded trajectories settle on a limit cycle by the Poincaré–Bendixson theorem. This works even when the two arms of the negative loop have very different time scales, the opposite of the condition of Proposition 16.4.1. Globally, strong positive feedback makes $X$ bistable, and the slow inhibitor drives it around the hysteresis loop: a **relaxation oscillator** ([Definition 33.5.3 of 7.6.33](/7.6.33#def-33.5.3)), whose amplitude is fixed by the two folds of the switch and whose period by the speed of the slow variable.

The consequence, pointed out by Tsai and colleagues (2008), is that the frequency of such an oscillator can be tuned over a wide range without changing its amplitude, whereas a negative-feedback-only oscillator loses its oscillation when its frequency is pushed far from the natural value.

**Example 16.4.2** The figure compares a three-stage Goodwin loop with Hill coefficient $12$, tuned through the rate $g$ of its last stage, with the activator–repressor relaxation oscillator of [7.6.33](/7.6.33#sec-33.5.4), tuned through the rate $e$ of its repressor. The Goodwin loop oscillates only for $g$ between about $0.32$ and $3.3$, its period changes from $4.96$ to $2.33$ (a factor of $2.1$), and its amplitude rises from zero and falls back to zero across this range. The relaxation oscillator, as $e$ goes from $0.02$ to $3$, changes its period from $187$ to $1.84$, a factor of $101$, while the amplitude of the activator stays between $150$ and $166$. Cell-cycle times range from about $20\,\mathrm{min}$ in early embryos to days in adult tissues, and the heart rate changes threefold with demand; tunability with a fixed amplitude is what these oscillators need.

![Frequency tuning with negative feedback only and with coupled positive and negative feedback. A: time courses, each normalized to its maximum, of a Goodwin loop (dx₁/dt = 10/(1 + x₃¹²) − x₁, dx₂/dt = x₁ − x₂, dx₃/dt = g(x₂ − x₃)) for g = 0.7 and 2.5 (violet, below) and of the activator–repressor relaxation oscillator of 7.6.33 (with the repressor rate multiplied by e) for e = 1 and 0.3 (green, above, offset). B: amplitude against frequency as g or e is scanned (both relative to their extremes): the negative-feedback loop oscillates in a narrow band of frequencies and its amplitude vanishes at both ends, the coupled oscillator is tuned over two decades at nearly constant amplitude](./plots/coupled_oscillator.py)

:::

The embryonic cell cycle is the canonical case: cyclin synthesis is the slow input, the doubly positive Cdk1 switch (16.2.2) provides the hysteresis, and APC/C, activated by Cdk1 with a delay, destroys cyclin; removing the positive feedback by a Cdk1 mutant that Wee1 cannot inhibit turns sustained oscillations into damped ones (Pomerening, Kim and Ferrell, 2005). The minimal models and their phase planes are in [7.3.20](/7.3.20#sec-20.6.3) and [7.6.34](/7.6.34#sec-34.2.1). How growth and the cell cycle are coordinated so that cells keep their size, the adder and sizer models, is treated in [7.6.39](/7.6.39#sec-39.2.4).

### 16.4.5. Ca²⁺ Oscillations

Cytosolic Ca²⁺ oscillates in many cell types stimulated by hormones that produce IP₃ ([7.1.14](/7.1.14), [7.3.18](/7.3.18#sec-18.4.6)). The oscillator is of the coupled type: Ca²⁺ released through the IP₃ receptor activates the receptor further (Ca²⁺-induced Ca²⁺ release, fast positive feedback), and at higher concentrations inactivates it, slowly (negative feedback). Two-pool models with Ca²⁺-induced release are discussed in [7.3.18](/7.3.18#fml-18.4.3); here the receptor itself is modeled, following De Young and Keizer (1992) in the two-variable reduction of Li and Rinzel (1994).

**Formula 16.4.1 (Li–Rinzel Model)** Let $c$ be the cytosolic Ca²⁺ concentration, $p$ the IP₃ concentration and $h$ the fraction of receptor subunits not inactivated by Ca²⁺. In a closed cell with total Ca²⁺ fixed, the ER concentration is $c_{\mathrm{ER}} = (c_0 - c)/c_1$, and
$$
\begin{aligned}
\frac{\mathrm{d}c}{\mathrm{d}t} &= c_1v_1\,m_\infty^3n_\infty^3h^3\,(c_{\mathrm{ER}} - c) + c_1v_2\,(c_{\mathrm{ER}} - c) - \frac{v_3c^2}{k_3^2 + c^2}, \qquad m_\infty = \frac{p}{p + d_1},\ n_\infty = \frac{c}{c + d_5},\\
\frac{\mathrm{d}h}{\mathrm{d}t} &= a_2\left[Q_2(1 - h) - ch\right], \qquad Q_2 = d_2\,\frac{p + d_1}{p + d_3},
\end{aligned} \tag{16.5}
$$
with release through open receptors (three subunits, each needing IP₃ bound, activating Ca²⁺ bound and no inactivating Ca²⁺), a leak, and SERCA pumping into the ER.

With the standard parameters ($c_0 = 2\,\mu\mathrm{M}$, $c_1 = 0.185$, $v_1 = 6\,\mathrm{s^{-1}}$, $v_2 = 0.11\,\mathrm{s^{-1}}$, $v_3 = 0.9\,\mu\mathrm{M\,s^{-1}}$, $k_3 = 0.1\,\mu\mathrm{M}$, $d_1 = 0.13$, $d_2 = 1.049$, $d_3 = 0.9434$, $d_5 = 0.08234\,\mu\mathrm{M}$, $a_2 = 0.2\,\mu\mathrm{M^{-1}\,s^{-1}}$), the $c$-nullcline in the $(c, h)$ plane is N-shaped and the slow $h$-nullcline crosses its middle branch for IP₃ between about $0.36$ and $0.67\,\mu\mathrm{M}$, where the system oscillates with periods of $10$–$13\,\mathrm{s}$ and amplitudes up to $0.37\,\mu\mathrm{M}$ (figure). Outside this window it rests at a low or a high steady state; the window is bounded by Hopf bifurcations, and within it the frequency rises with the stimulus.

![Ca²⁺ oscillations in the Li–Rinzel model, Eq. (16.5) with the standard parameters. A: cytosolic Ca²⁺ c and the fraction h of receptors not inactivated, at p = 0.5 µM: period 11.5 s. B: the (c, h) phase plane at p = 0.5 µM: the c-nullcline (yellow) is N-shaped because of Ca²⁺-induced Ca²⁺ release, the h-nullcline (red) is the slow inactivation, and the limit cycle (white/black) encircles their intersection on the middle branch. C: period (left axis) and amplitude (right axis) of the oscillation against p: oscillations exist between about 0.36 and 0.67 µM, and the period decreases from 13.0 to 10.3 s across the window](./plots/calcium_oscillation.py)

### 16.4.6. Clocks

Circadian clocks are delayed negative feedback loops with additional loops that stabilize them ([7.6.33](/7.6.33#sec-33.6)). Three of their properties belong to the mathematics of oscillators. Their period is temperature compensated, which requires that the temperature dependences of the rates that set the period cancel. They can be reset by light, because a perturbation applied at a given phase shifts the phase by an amount that depends on that phase, the phase response curve. And they are entrained by the daily cycle: a phase oscillator with natural frequency $\omega$ forced at frequency $\Omega$ with coupling $\kappa$ obeys, for the phase difference, the Adler equation $\dot\phi = (\omega - \Omega) - \kappa\sin\phi$, which locks when $\lvert\omega - \Omega\rvert \le \kappa$ ([Remark 23.5.1 of 7.5.23](/7.5.23#rem-23.5.1); **entrainment**). A clock whose frequency mismatch with the day exceeds its coupling to light cannot lock and drifts out of phase with the environment.

### 16.4.7. Synchronization of Many Oscillators

Tissues contain many oscillators: the neurons of the suprachiasmatic nucleus, the cells of the presomitic mesoderm, pacemaker cells of the heart. If they are coupled, they can synchronize, and the **Kuramoto model** ([Definition 23.5.2 of 7.5.23](/7.5.23#def-23.5.2)) shows that synchronization appears as a phase transition at a critical coupling. Its critical coupling was stated there without proof; for a Lorentzian distribution of natural frequencies the whole branch can be derived.

**Theorem 16.4.1 (Self-Consistency of the Kuramoto Model)** Let the natural frequencies have the Lorentzian density $g(\omega) = \gamma/[\pi(\gamma^2 + \omega^2)]$ (centered at $0$ in a rotating frame), and let $N \to \infty$. A stationary partially synchronized state with order parameter $r > 0$ exists if and only if $K > K_{\mathrm{c}} = 2\gamma$, and then
$$
r = \sqrt{1 - \frac{K_{\mathrm{c}}}{K}}. \tag{16.6}
$$

**Proof** In mean-field form $\dot\theta_i = \omega_i - Kr\sin\theta_i$ (with the mean phase set to $0$). Oscillators with $\lvert\omega\rvert \le Kr$ lock at $\sin\theta = \omega/(Kr)$; the others drift, and by the symmetry of $g$ their stationary distribution contributes nothing to $r = \langle\cos\theta\rangle$ (their $\sin\theta$ terms also cancel). Hence
$$
r = \int_{-Kr}^{Kr}\cos\theta(\omega)\,g(\omega)\,\mathrm{d}\omega = Kr\int_{-\pi/2}^{\pi/2}\cos^2\theta\,g(Kr\sin\theta)\,\mathrm{d}\theta,
$$
substituting $\omega = Kr\sin\theta$. Dividing by $r > 0$ and inserting the Lorentzian, with $a = Kr/\gamma$,
$$
1 = \frac{K}{\pi\gamma}\int_{-\pi/2}^{\pi/2}\frac{\cos^2\theta}{1 + a^2\sin^2\theta}\,\mathrm{d}\theta = \frac{K}{\gamma}\,\frac{\sqrt{1 + a^2} - 1}{a^2} = \frac{K}{\gamma\,(\sqrt{1 + a^2} + 1)},
$$
using $\int_0^{\pi/2}\cos^2\theta/(1 + a^2\sin^2\theta)\,\mathrm{d}\theta = \frac{\pi}{2}(\sqrt{1 + a^2} - 1)/a^2$. Thus $\sqrt{1 + a^2} = K/\gamma - 1$, which has a solution $a > 0$ iff $K > 2\gamma$, and then $a^2 = (K/\gamma - 1)^2 - 1$, so $K^2r^2 = K^2 - 2K\gamma$ and $r^2 = 1 - 2\gamma/K$. $\square$

Near $K_{\mathrm{c}}$, $r \approx \sqrt{(K - K_{\mathrm{c}})/K_{\mathrm{c}}}$: synchrony grows as the square root of the distance from the transition, like the amplitude at a supercritical Hopf bifurcation. In a simulation of $2000$ oscillators with $\gamma = 0.5$ (figure), $r$ is $0.03$–$0.08$ below $K_{\mathrm{c}} = 1$ (the $N^{-1/2}$ fluctuations of a finite population), $0.70$ at $K = 2$ (theory $0.707$) and $0.86$ at $K = 4$ (theory $0.866$); above $K_{\mathrm{c}}$ the oscillators with $\lvert\omega\rvert < Kr$ form a locked cluster, the rest drift.

![Synchronization in the Kuramoto model with Lorentzian natural frequencies (half-width γ = 0.5, N = 2000, mean-field form). A: the order parameter r after transients against the coupling K: simulation (points) and Theorem 16.4.1 (line), with the transition at K_c = 2γ = 1. B: phases of all oscillators (angle) with the rank of |ω| as radius, for K = 0.6 (incoherent) and K = 2 (violet: locked oscillators with |ω| < Kr, which sit at sin θ = ω/(Kr); grey: drifting oscillators)](./plots/kuramoto.py)

## 16.5. Information in Dynamics

Oscillations and pulses are not only clocks: they carry information. Several transcription factors move in and out of the nucleus in pulses whose frequency, rather than amplitude, follows the input. The yeast factor Crz1 enters the nucleus in bursts of about two minutes whose frequency rises with extracellular Ca²⁺ (Cai, Dalal and Elowitz, 2008); ERK activity in mammalian epithelial cells comes in pulses whose frequency increases with EGF and predicts proliferation (Albeck, Mills and Brugge, 2013); NF-κB oscillates in and out of the nucleus through its negative loop with IκBα (Hoffmann, Levchenko, Scott and Baltimore, 2002; Nelson and colleagues, 2004); and p53 conveys the extent of DNA damage in the number of its pulses ([7.6.33](/7.6.33#sec-33.5.5)). Ca²⁺ spikes encode hormone concentration in their frequency ([7.6.33](/7.6.33#sec-33.6.3)).

**Definition 16.5.1 (Frequency Encoding)** A signaling system uses **frequency encoding** (frequency modulation) if the strength of its input is represented by the frequency of pulses of a signaling molecule of nearly fixed amplitude and duration, and amplitude encoding if it is represented by the level of the molecule.

One advantage of frequency encoding is that it preserves the ratios between the expression of target genes with different affinities.

**Example 16.5.1** Two genes are activated by a factor $X$ with $g_i = \beta_iX/(K_i + X)$, $K_1 = 0.1$, $K_2 = 1$. With amplitude encoding, $X \propto s$; as $X$ goes from $0.01$ to $10$, the ratio $g_1/g_2 = (\beta_1/\beta_2)(K_2 + X)/(K_1 + X)$ changes from $9.2\,\beta_1/\beta_2$ to $1.09\,\beta_1/\beta_2$: the high-affinity gene saturates first, and the composition of the response changes with the signal. With frequency encoding, $X$ is either $0$ or $X_{\mathrm{high}} = 10$, and the fraction of time it is high is proportional to $s$; if the targets respond slowly compared with the pulses, the mean production of each gene is $s$ times its rate at $X_{\mathrm{high}}$, and the ratio $g_1/g_2 = 1.09\,\beta_1/\beta_2$ is the same at every signal level. Crz1 target genes with very different promoters responded to Ca²⁺ with proportional changes, as this argument predicts (Cai, Dalal and Elowitz, 2008). The cost is stochastic: at low signal there are few pulses per response time, and the number of pulses fluctuates.

:::

Pulses have a second use: an incoherent feed-forward loop downstream of a constant factor adapts and stops responding ([7.9.15](/7.9.15#sec-15.4.4)), whereas a pulsing factor keeps exciting it. And a target's response to an oscillating factor depends on its own lifetime: a stable protein integrates the pulses, an unstable one follows them (Question 10). The decoding of dynamics by downstream networks, and the information capacity of such channels ([7.6.35](/7.6.35#sec-35.3)), are active research topics.

## Summary

| Motif | Network | Function | Key result |
|---|---|---|---|
| Positive autoregulation | developmental | slow response, bistable memory | Proposition 16.1.1; fixed points alternate in stability |
| Lock-on and toggle loops | developmental | joint or exclusive bistability, fate choice | needs cooperativity or autoregulation (Proposition 16.1.2); λ switch (Example 16.1.1) |
| Regulated feedback | developmental | memory of a transient input | Definition 16.1.2, figure |
| Repressor cascade | developmental | timing over generations | each step $\sim\ln 2/\alpha$ |
| Ultrasensitive cascade + positive feedback | signaling | all-or-none, irreversible switch | gains multiply (Proposition 16.2.1); bistability needs loop gain $> 1$ (Proposition 16.2.2); oocyte (Example 16.2.1) |
| Two positive loops | cell cycle | robust bistability | 4.3- vs 18-fold range (Example 16.2.2) |
| Hybrid negative loop, hybrid FFL | integrated | homeostasis, transient memory | fast arm on a slow arm is stable; FFLs cannot oscillate (Proposition 16.2.3) |
| Multi-input FFL | neuronal | coincidence detection | Definition 16.3.1 |
| Two-node negative loop | p53–Mdm2 | damped oscillation, noise-sustained pulses | Proposition 16.4.1; amplitude CV > period CV (Example 16.4.1) |
| Delay oscillator | clocks, segmentation | sinusoidal oscillation | secant condition ([7.6.33](/7.6.33)) |
| Coupled positive–negative feedback | cell cycle, Ca²⁺, neurons | tunable frequency at fixed amplitude | Definition 16.4.1; Example 16.4.2; Li–Rinzel (Formula 16.4.1) |
| Coupled oscillators | tissues | synchrony | $r = \sqrt{1 - 2\gamma/K}$ (Theorem 16.4.1) |
| Pulsing factors | Crz1, ERK, NF-κB, p53 | frequency encoding, fixed target ratios | Definition 16.5.1, Example 16.5.1 |

- Feedback is what distinguishes these networks from sensory transcription networks: positive loops make decisions and memories, negative loops with delay or with positive feedback make clocks. The sign rule of [7.6.33](/7.6.33#sec-33.1.1), positive loops for multistability and negative loops for oscillation, is made quantitative by the loop gain (Proposition 16.2.2) and by the eigenvalues of the loop (Proposition 16.4.1).
- Feed-forward loops are the stable counterparts of feedback loops: coherent FFLs give delays and transient memory, incoherent FFLs pulses and speed-up, but they cannot oscillate or remember permanently.

## Questions

1. Show that adjacent fixed points of $\dot x = F(x)$ ($F$ smooth, all roots simple) alternate in stability, and design an input function for an autoregulated gene $\dot X = f(X) - X$ with five fixed points.

   **Answer** Between two adjacent simple roots $F$ has a constant sign; a root is stable iff $F' < 0$ there, that is iff $F$ goes from positive to negative. If $F$ is positive just left of a root and negative just right, the next root (approached from the left with $F < 0$) has $F$ going from negative to positive and is unstable, and so on: the signs of $F'$ alternate. Five fixed points need a production curve that crosses the line $X$ five times, for example a sum of two steep sigmoids at different thresholds, $f(X) = 0.1 + 2\,\frac{X^8}{1 + X^8} + 6\,\frac{(X/5)^8}{1 + (X/5)^8}$: the fixed points are $X = 0.100$ (stable), $0.967$ (unstable), $2.10$ (stable), $4.93$ (unstable) and $7.96$ (stable), three stable expression states.

2. Using Proposition 16.1.2, explain why a toggle switch built from two repressors that each bind DNA as monomers at a single site is not bistable, and give two ways in which natural or synthetic toggles obtain bistability.

   **Answer** A single monomer site gives a repression function $a + b/(1 + y/K)$ of Hill coefficient $1$; the composition of two such functions is a concave Möbius map that crosses the diagonal once, so the toggle has one stable fixed point with both genes at intermediate levels. Bistability comes from cooperativity, repressors that dimerize before binding or bind cooperatively to several operators (λ CI at $O_{\mathrm{R}}1$–$O_{\mathrm{R}}2$, LacI tetramers with DNA looping, the Hill coefficients near $2$ used by Gardner and colleagues), or from additional positive autoregulation of the factors, as in many fate determinants and in CI itself.

3. In a double-positive loop without cooperative binding, each factor is activated by its partner and by itself, combined multiplicatively: $\dot X = 4\,\frac{X}{1 + X}\,\frac{Y}{1 + Y} + 0.01 - X$ and the symmetric equation for $Y$. Find the symmetric fixed points and their stability, and conclude whether the loop is bistable.

   **Answer** On the diagonal $X = Y = u$, the fixed points solve $u = 4u^2/(1 + u)^2 + 0.01$: numerically $u = 0.0104$, $0.799$ and $1.201$. At a symmetric point the Jacobian is $\begin{bmatrix}a - 1 & a\\ a & a - 1\end{bmatrix}$ with $a = 4u/(1 + u)^3$, whose eigenvalues are $-1$ (antisymmetric direction) and $2a - 1$ (symmetric direction): $-0.92$, $+0.10$ and $-0.10$. The low and high states are stable and the middle one is a saddle: the loop is bistable. On the diagonal the product of the two Michaelis–Menten terms is $u^2/(1 + u)^2$, effectively a Hill function of order $2$, so positive autoregulation supplies the nonlinearity that cross-regulation without cooperativity lacks (Proposition 16.1.2 does not apply because each rate depends on both variables).

4. In the λ model (16.1), why does the lytic state survive at all $d$ while the lysogenic state disappears, and what would change if Cro were also cleaved upon damage?

   **Answer** The parameter $d$ only increases the removal of CI. In the lytic state CI is already low ($c \approx 0.01$) and its removal hardly matters, while Cro is held high by its own promoter, which CI no longer represses; so increasing $d$ only lowers the already negligible CI further. In the lysogenic state, CI must sustain itself through its positive loop, $4(0.05 + c^2)/(1 + c^2) = (1 + d)c$; for large enough $d$ the removal line rises above the sigmoidal production curve except near $c = 0$, and the state vanishes in a saddle-node bifurcation ($d_{\mathrm{c}} = 0.70$). If Cro were cleaved too, the lytic state would be weakened as well; strong damage could then leave only a state with both low, an "undecided" state, and the switch to lysis would no longer be guaranteed. Real λ avoids this: RecA stimulates the cleavage of CI (and LexA) but not of Cro.

5. Prove from Proposition 16.2.1 that a cascade of $m$ identical tiers, each with response coefficient $R$ at its operating point, has response coefficient $R^m$, and use this to explain why ultrasensitivity grows down the MAPK cascade but cannot grow indefinitely.

   **Answer** By (16.2), with $R_k = R$ for all $k$, the product is $R^m$. Each tier's response coefficient is large only where it is far from saturation; the output of a tier is the input of the next, so the operating points of all tiers must be aligned in the steep part of their curves. Saturation of any tier ($y_k$ near its maximum) gives $R_k \to 0$ and kills the product; hence the high gain of a long cascade is confined to a narrow window of inputs, and noise in the input, amplified by the same gain, limits useful steepness. In the figure the cascade's $R$ is $4$ at low input but falls to near zero once the second tier saturates.

6. (Coincidence detection) A multi-input FFL has inputs $X_1$ and $X_2$, an intermediate $Y$ with $\dot Y = X_1 + X_2 - Y$ and an output $Z$ with $\dot Z = \theta(X_1 + X_2 > 0.5)\,\theta(Y > 0.6) - Z$. Each input is a pulse of height $1$ and duration $0.5$. Does a single pulse produce output? Do two simultaneous pulses? Two pulses separated by $0.2$?

   **Answer** One pulse: $Y(0.5) = 1 - \mathrm{e}^{-0.5} = 0.39 < 0.6$, and after the pulse $Y$ decays, so $Z$ never turns on. Two simultaneous pulses: $\dot Y = 2 - Y$, $Y(t) = 2(1 - \mathrm{e}^{-t})$ crosses $0.6$ at $t = \ln(1/0.7) = 0.36 < 0.5$, so $Z$ is produced from $0.36$ to $0.5$ (and beyond while the second pulse lasts). Pulses at $0$–$0.5$ and $0.2$–$0.7$: $Y(0.2) = 1 - \mathrm{e}^{-0.2} = 0.181$; then $\dot Y = 2 - Y$ from $0.181$: $Y = 2 - 1.819\,\mathrm{e}^{-(t - 0.2)}$ reaches $0.6$ when $\mathrm{e}^{-(t - 0.2)} = 0.770$, $t = 0.461$, still within both pulses, so $Z$ turns on from $0.461$ until the input sum drops below $0.5$ at $t = 0.7$. The circuit responds only to inputs that coincide within roughly the integration time of $Y$.

7. For the two-node negative loop with $\alpha_1 = 1$, compute the minimal feedback strength $\beta_1\beta_2$ needed for damped oscillations when $\alpha_2 = 1$, $10$ and $0.01$, and relate the answer to hybrid motifs.

   **Answer** From Proposition 16.4.1, $\beta_1\beta_2 > (\alpha_1 - \alpha_2)^2/4$: for $\alpha_2 = 1$ any positive strength suffices; for $\alpha_2 = 10$, $\beta_1\beta_2 > 20.25$; for $\alpha_2 = 0.01$, $\beta_1\beta_2 > 0.245$. A hybrid loop, with a protein-level arm much faster than the transcriptional arm, needs a much stronger feedback to overshoot, and is otherwise overdamped: it returns smoothly to its set point, which is the property homeostasis requires.

8. Show that positive autoregulation can turn a two-node negative loop with very different time scales into an oscillator: with $\alpha_1 = 1$, $\alpha_2 = 0.05$ and $\beta_1\beta_2 = 0.2$, find the range of $P$ for which the fixed point is an unstable spiral.

   **Answer** The Jacobian $\begin{bmatrix}P - 1 & -\beta_1\\ \beta_2 & -0.05\end{bmatrix}$ has trace $P - 1.05$ and determinant $0.05(1 - P) + 0.2 = 0.25 - 0.05P$, positive for $P < 5$. Its eigenvalues are complex iff $(P - 1 + 0.05)^2 < 4\beta_1\beta_2 = 0.8$, that is $0.056 < P < 1.84$. The fixed point is an unstable spiral when, in addition, the trace is positive: $1.05 < P < 1.84$, with a Hopf bifurcation at $P = 1.05$. For $1.84 < P < 5$ it is an unstable node, and with saturating feedback the bounded trajectories still go to a limit cycle (Poincaré–Bendixson), now of relaxation type. Without positive feedback ($P = 0$) the loop is stable and, since $0.95^2 > 0.8$, not even oscillatory.

9. In the Kuramoto model with $\gamma = 0.5$, what coupling gives $r = 0.5$? What fraction of the oscillators is then locked?

   **Answer** $r^2 = 1 - 2\gamma/K$: $0.25 = 1 - 1/K$, $K = 4/3$. Locked oscillators have $\lvert\omega\rvert < Kr = 2/3$; for the Lorentzian, $\mathbb{P}(\lvert\omega\rvert < c) = (2/\pi)\arctan(c/\gamma) = (2/\pi)\arctan(4/3) = 0.590$: about $59\,\%$ of the oscillators are locked although $r$ is only $0.5$, because the locked ones are spread over phases $\theta = \arcsin(\omega/Kr)$ between $-90^\circ$ and $90^\circ$.

10. A gene $Y$ is activated by a factor $X(t)$ that oscillates between $0$ and $1$ with period $T$ (on for half of each period), and $\dot Y = X(t) - \alpha Y$. How do the mean and the peak-to-trough amplitude of $Y$ depend on $\alpha T$? What does this imply for genes downstream of pulsing p53?

    **Answer** The mean of $Y$ is always $\langle X\rangle/\alpha = 0.5/\alpha$. Over each half period $Y$ relaxes exponentially towards $1/\alpha$ or $0$; in the periodic regime the maximum and minimum satisfy $Y_{\max} = 1/\alpha - (1/\alpha - Y_{\min})\mathrm{e}^{-\alpha T/2}$ and $Y_{\min} = Y_{\max}\mathrm{e}^{-\alpha T/2}$, so $Y_{\max} - Y_{\min} = \frac{1}{\alpha}\frac{1 - q}{1 + q}$ with $q = \mathrm{e}^{-\alpha T/2}$. For $\alpha T \ll 1$ (stable $Y$) the relative amplitude $(Y_{\max} - Y_{\min})/\langle Y\rangle \approx \alpha T/2$ is small: $Y$ integrates the pulses. For $\alpha T \gg 1$ (unstable $Y$) it approaches $2$: $Y$ follows each pulse. Genes downstream of p53 with long-lived products report the number of pulses (the cumulative dose), those with short-lived products report the pulsing itself, so the same p53 dynamics can produce different expression programs, and sustained p53 (as after UV damage, or with drugs) is read differently from pulses.
