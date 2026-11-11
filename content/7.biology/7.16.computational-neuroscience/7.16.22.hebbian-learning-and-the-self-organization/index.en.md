---
title: Hebbian Learning and the Self-Organization of Receptive Fields and Maps
description: The Hebb rule and its instability; subtractive and multiplicative normalization and Oja's rule as principal component analysis; covariance and BCM rules with a sliding threshold; spike-timing-dependent plasticity averaged over spike statistics; competition between the two eyes and the formation of ocular dominance stripes; orientation selectivity and Kohonen maps; competitive and supervised learning.
---

[Chapter 7.16.21](/7.16.21) showed that the wiring of the visual system is refined by correlated activity, that the **NMDA receptor** reports the coincidence of pre- and postsynaptic activity and that the segregation of the eyes and the formation of **ocular dominance columns** depend on competition. This chapter turns these observations into mathematics. The question is what a synaptic rule that uses only local information, the activity of the two neurons it connects, can achieve in a population that is exposed to a statistical ensemble of inputs. The answer is a surprising amount: such rules extract principal components, develop selective receptive fields and generate maps. The cellular mechanisms of long-term plasticity, including the experimental basis of **spike-timing-dependent plasticity**, are treated in [7.16.14](/7.16.14).

Notation: the presynaptic activities form a vector $\boldsymbol{u} = (u_1, \dots, u_{N_u})$ of nonnegative or mean-subtracted **firing rates**, the output rate is $r = \boldsymbol{w}\cdot\boldsymbol{u}$ for the weight vector $\boldsymbol{w}$ (a linear rate model of [7.16.15](/7.16.15), in the limit in which $r$ follows its input instantaneously), $\langle\cdot\rangle$ is the average over the ensemble of inputs, and $Q = \langle\boldsymbol{u}\boldsymbol{u}^{\mathsf T}\rangle$ is the correlation matrix. Its eigenvalues are written $\lambda_\mu$ with eigenvectors $\boldsymbol{e}_\mu$, ordered so that $\lambda_1 \ge \lambda_2 \ge \dots$ (here $\lambda$ is an eigenvalue and not a length constant). Plasticity is slow compared with the dynamics of $r$ and with the presentation of the stimuli, so that the weight change can be replaced by its average over the input ensemble.

## 22.1. The Hebb Rule and Its Instability

**Formula 22.1.1 (Basic Hebb Rule)** In the basic **Hebb rule** the weight of a synapse changes in proportion to the product of the presynaptic and postsynaptic activities,

$$
\tau_w\frac{\mathrm{d}\boldsymbol{w}}{\mathrm{d}t} = r\,\boldsymbol{u}, \qquad \text{averaged:}\quad \tau_w\frac{\mathrm{d}\boldsymbol{w}}{\mathrm{d}t} = \langle r\,\boldsymbol{u}\rangle = Q\boldsymbol{w}, \tag{22.1}
$$
with a time constant $\tau_w$ that is long compared with the time scale of $r$ and with the duration of a single stimulus, so that the weights integrate over many stimuli (in experiments, plasticity develops over minutes to hours).

The form $\langle r\boldsymbol{u}\rangle = Q\boldsymbol{w}$ shows that the Hebb rule is a correlation-based rule: it depends on the inputs only through $Q$. It is a positive-feedback process, since a strengthened synapse increases $r$ and so promotes further strengthening.

**Theorem 22.1.1 (Instability of the Hebb Rule)** Write $\boldsymbol{w}(0) = \sum_\mu c_\mu(0)\boldsymbol{e}_\mu$. The solution of (22.1) is $\boldsymbol{w}(t) = \sum_\mu c_\mu(0)\,\mathrm{e}^{\lambda_\mu t/\tau_w}\boldsymbol{e}_\mu$. If $c_1(0) \ne 0$, the direction of $\boldsymbol{w}(t)$ converges to the principal eigenvector $\boldsymbol{e}_1$ of $Q$, while its length grows without bound, $\lvert\boldsymbol{w}\rvert \propto \mathrm{e}^{\lambda_1 t/\tau_w}$.

**Proof** $Q$ is symmetric and positive semidefinite, so its eigenvectors are an orthogonal basis and its eigenvalues are nonnegative. In this basis (22.1) reads $\tau_w\dot c_\mu = \lambda_\mu c_\mu$, which gives the solution. The ratios $c_\mu/c_1 = (c_\mu(0)/c_1(0))\,\mathrm{e}^{-(\lambda_1 - \lambda_\mu)t/\tau_w}$ vanish for $\mu \ne 1$ if $\lambda_1 > \lambda_\mu$. $\square$

The rule has two defects that any usable model has to repair. The weights grow without limit, whereas **LTP** saturates and synapses do not change sign. And all weights are potentiated at once, if the inputs are positive and correlated, so that the neuron loses selectivity: the principal eigenvector of the correlation matrix of nonnegative activities has all components positive. Simple limits ($0 \le w \le w_{\max}$, saturation) stop the growth but not the loss of selectivity, and they do not produce competition. Competition, so that some synapses must weaken when others strengthen, is the property of the experiments of [7.16.21](/7.16.21#sec-21.4) that we want.

## 22.2. Constraints, Normalization and Oja's Rule

### 22.2.1. Synaptic Normalization

**Definition 22.2.1 (Synaptic Normalization)** **Synaptic normalization** is a constraint that keeps the total strength of the synapses onto a neuron constant (or its norm). It is subtractive if the same amount is subtracted from all synapses, which preserves $\sum_b w_b$, and multiplicative if all synapses are scaled by the same factor, which preserves $\lvert\boldsymbol{w}\rvert$.

Subtractive normalization is $\tau_w\,\mathrm{d}\boldsymbol{w}/\mathrm{d}t = Q\boldsymbol{w} - \bigl(\boldsymbol{n}\cdot Q\boldsymbol{w}/N_u\bigr)\boldsymbol{n}$ with $\boldsymbol{n} = (1, \dots, 1)$: the component of the change along $\boldsymbol{n}$ is removed. If $\boldsymbol{n}$ is an eigenvector of $Q$ (as for translation-invariant correlations), the mean mode is eliminated and the remaining eigenmodes grow as before, so that the pattern with the largest eigenvalue among those with zero mean develops, until the weights reach their bounds, with the result that each weight is either at $0$ or at $w_{\max}$ (a sharp, binary outcome).

Multiplicative normalization leaves the direction of $\boldsymbol{w}$ to evolve as in the **Hebb rule** but scales it, giving a graded outcome that is the principal eigenvector of $Q$ (Miller and MacKay 1994). Both rules require a non-local signal, namely information about the other synapses of the same neuron. Biological candidates are the redistribution of resources among synapses (such as the supply of **AMPA receptors**) and **synaptic scaling** ([7.16.14](/7.16.14)).

### 22.2.2. Oja's Rule

**Definition 22.2.2 (Oja's Rule)** In **Oja's rule** a decay term proportional to the square of the output is added to the Hebb rule,

$$
\tau_w\frac{\mathrm{d}\boldsymbol{w}}{\mathrm{d}t} = r\,\boldsymbol{u} - \alpha r^2\boldsymbol{w}, \tag{22.2}
$$
with a positive constant $\alpha$. The decay depends only on the quantities that are available at the synapse ($r$, and the weight $w_b$ itself), and it implements multiplicative normalization in a local form.

**Theorem 22.2.1 (Oja's Rule Computes the First Principal Component)** If $\lambda_1 > \lambda_2$, the averaged form of (22.2), $\tau_w\dot{\boldsymbol{w}} = Q\boldsymbol{w} - \alpha(\boldsymbol{w}^{\mathsf T}Q\boldsymbol{w})\boldsymbol{w}$, has the stable fixed point $\boldsymbol{w} = \pm\boldsymbol{e}_1/\sqrt{\alpha}$, and all other fixed points are unstable.

**Proof** At a fixed point $Q\boldsymbol{w} = \alpha(\boldsymbol{w}^{\mathsf T}Q\boldsymbol{w})\boldsymbol{w}$, so $\boldsymbol{w}$ is an eigenvector $\boldsymbol{e}_\mu$ with eigenvalue $\lambda_\mu = \alpha\lambda_\mu\lvert\boldsymbol{w}\rvert^2$, hence $\lvert\boldsymbol{w}\rvert^2 = 1/\alpha$ (or $\boldsymbol{w} = 0$). For stability expand $\boldsymbol{w} = \sum_\mu c_\mu\boldsymbol{e}_\mu$: $\tau_w\dot c_\mu = \lambda_\mu c_\mu - \alpha\bigl(\sum_\nu\lambda_\nu c_\nu^2\bigr)c_\mu$. Then $\tau_w\,\mathrm{d}\ln\lvert c_\mu/c_1\rvert/\mathrm{d}t = \lambda_\mu - \lambda_1 < 0$, so that all components $c_\mu/c_1$ with $\mu \ne 1$ decay, and the length is driven to $1/\sqrt\alpha$ by the cubic term. A fixed point at $\boldsymbol{e}_\mu$ with $\mu \ne 1$ is unstable, because the ratio $c_1/c_\mu$ grows. $\square$

The result links Hebbian plasticity with **principal component analysis** ([3.4.5](/3.4.5)): a neuron with a Hebbian synapse and a local normalization learns to compute the projection onto the direction of largest variance of its input, the optimal linear compression of the input in the sense of the mean square error, and with a lateral decorrelating rule a population learns the first several components (Sanger 1989; Oja 1992). For inputs with the statistics of natural images the principal components are Fourier-like patterns, not the localized Gabor shapes of V1 ([7.16.20](/7.16.20#sec-20.5)): second-order correlations are not enough, which is the motivation for the sparse and covariance-like rules.

![Hebbian rules on a correlated two-dimensional input (covariance eigenvalues 1.0 and 0.2, principal axis at $30^\circ$). A: inputs (dots) and the weight trajectories of the basic Hebb rule (rescaled so that it fits on the axes) and of Oja's rule, both from the same initial weights (square); the final points (dots) lie on the principal axis. B: the length $\lvert\boldsymbol{w}\rvert$ against the number of presentations: it diverges exponentially for the Hebb rule and converges to $1/\sqrt\alpha = 1$ for Oja's rule (Theorem 22.2.1). C: the angle between $\boldsymbol{w}$ and the principal axis: both rules align within about 1000 presentations (the curves coincide)](./plots/oja-rule.py)

## 22.3. Covariance and BCM Rules

### 22.3.1. The Covariance Rule

A weakness of the **Hebb rule** is that it potentiates whenever the output is nonzero, so that long-term depression is absent. LTD occurs experimentally for low levels of postsynaptic activity (and, with LTP, forms the basis for the Ca$^{2+}$ control hypothesis of [7.16.14](/7.16.14)). A simple repair is to measure the activities relative to a threshold.

**Definition 22.3.1 (Covariance Rule)** In the **covariance rule** the presynaptic activity is measured relative to its mean, $\tau_w\,\mathrm{d}\boldsymbol{w}/\mathrm{d}t = r\,(\boldsymbol{u} - \langle\boldsymbol{u}\rangle)$, whose average is

$$
\tau_w\frac{\mathrm{d}\boldsymbol{w}}{\mathrm{d}t} = C\boldsymbol{w}, \qquad C = \langle(\boldsymbol{u} - \langle\boldsymbol{u}\rangle)(\boldsymbol{u} - \langle\boldsymbol{u}\rangle)^{\mathsf T}\rangle,
$$
the covariance matrix of the input. (A threshold on the postsynaptic side, $(r - \theta_r)\boldsymbol{u}$, gives the same average for $\theta_r = \langle r\rangle$.)

The averaged rule has the form of (22.1) with $C$ instead of $Q$, so that Theorem 22.1.1 applies: the weights evolve toward the principal eigenvector of the covariance, and, unlike $Q$, this eigenvector has components of both signs and thus can be selective. The rule has both LTP and LTD but is still unstable, and it needs the constraints of Section 22.2.

### 22.3.2. The BCM Rule with a Sliding Threshold

The rule of Bienenstock, Cooper and Munro (1982) makes the threshold itself dynamic, so that stability and selectivity follow without an explicit constraint on the weights.

**Definition 22.3.2 (BCM Rule)** In the **BCM rule** the weight change is a nonlinear function of the postsynaptic activity that changes sign at a threshold $\theta$,

$$
\tau_w\frac{\mathrm{d}\boldsymbol{w}}{\mathrm{d}t} = r\,(r - \theta)\,\boldsymbol{u}, \qquad \theta = \frac{\langle r^2\rangle}{r_0}, \tag{22.3}
$$
where $r_0$ is a constant; in simulations $\theta$ is a running average of $r^2$ with a time constant $\tau_\theta$ that is long compared with the presentation of single stimuli but shorter than $\tau_w$; if the threshold slides more slowly than the weights change, the rule oscillates or becomes unstable. For $r > \theta$ the synapses are potentiated, for $0 < r < \theta$ they are depressed.

The function $\phi(r, \theta) = r(r - \theta)$, which is plotted in the figure, matches the frequency dependence of LTP and LTD, with depression at low frequencies and potentiation at high ones, and the sliding of $\theta$ with the history of the postsynaptic activity corresponds to **metaplasticity** ([7.16.14](/7.16.14)). The feedback of $\theta$ is the source of stability: if the neuron becomes more active, $\theta$ rises and the potentiation turns into depression.

**Theorem 22.3.1 (Selectivity of the BCM Rule)** Let the neuron be presented with $K$ linearly independent patterns $\boldsymbol{u}^{(k)}$ with equal probability, and let $r^{(k)} = \boldsymbol{w}\cdot\boldsymbol{u}^{(k)}$. The fixed points of the averaged rule (22.3) have $r^{(k)} \in \{0, \theta\}$ for every $k$; if $m$ patterns have $r^{(k)} = \theta$, then $\theta = Kr_0/m$. Only the fixed points with $m = 1$ are stable: the neuron responds to exactly one pattern, with $r = \theta = Kr_0$, and not at all to the other $K - 1$ patterns.

**Proof** We prove the fixed-point condition. Because the patterns are linearly independent, the averaged change vanishes only if $r^{(k)}(r^{(k)} - \theta) = 0$ for each $k$. With $m$ patterns at $r = \theta$, $\theta = \langle r^2\rangle/r_0 = m\theta^2/(Kr_0)$, hence $\theta = Kr_0/m$. The stability analysis, which shows that the fixed points with $m \ge 2$ have an unstable direction, is due to Intrator and Cooper (1992). $\square$

The result is that a BCM neuron becomes selective for one of its inputs, which is chosen by the initial conditions, and the most selective state is stable. In the figure, four patterns and $r_0 = 1$ lead to $r = \theta = 4$ for the winning pattern and $0$ for the others. BCM theory has explained the effects of deprivation in the **critical period**: after monocular closure the activity of the deprived input is weak and uncorrelated, its response lies below $\theta$ and it is depressed, whereas after closure of both eyes $\theta$ slides down and the depression is not as strong, which is the observation of [7.16.21](/7.16.21#sec-21.4.2). Dark rearing keeps $\theta$ low and so lengthens the period of high plasticity, as observed (Cooper and Bear 2012).

![The BCM rule (Eq. 22.3) with a sliding threshold. A neuron with 6 inputs is presented with 4 positive, linearly independent patterns with equal probability. A: the responses to the four patterns and the threshold $\theta$ (dashed) during learning: starting from similar responses, one pattern is selected, its response rises to $r = \theta \approx 4 = K r_0$ and the responses to the other three fall to zero. B: the function $\phi(r, \theta) = r(r - \theta)$ for three values of $\theta$. C: the selectivity (difference of the largest and the second largest response divided by their sum) after learning from 40 random initial weight vectors: it is near 1 in every run, while the winning pattern differs from run to run](./plots/bcm-selectivity.py)

## 22.4. Spike-Timing-Dependent Plasticity and Correlation Learning

Experiments on pairs of connected neurons show that the sign of plasticity depends on the order of the spikes: potentiation if the presynaptic spike comes a few milliseconds before the postsynaptic one, depression in the reverse order, with time constants of $10$–$30\,\mathrm{ms}$ ([7.16.14](/7.16.14)). The rate rules above can be obtained from this **spike-timing-dependent plasticity** (STDP) by averaging.

**Formula 22.4.1 (Pair-Based STDP)** Let $s = t_{\mathrm{post}} - t_{\mathrm{pre}}$ be the difference of the spike times of a pair. With the window

$$
W(s) = \begin{cases} A_+\mathrm{e}^{-s/\tau_+}, & s > 0 \quad \text{(pre before post: potentiation)},\\ -A_-\mathrm{e}^{s/\tau_-}, & s < 0 \quad \text{(post before pre: depression)},\end{cases} \tag{22.4}
$$
each pair of spikes changes the weight by $W(s)$ (in units of the maximal weight), and the changes of all pairs are summed (all-to-all interactions).

**Theorem 22.4.1 (Averaged STDP)** Let $\rho_{\mathrm{pre}}(t)$ and $\rho_{\mathrm{post}}(t)$ be the **spike trains**. The expected rate of change of the weight is

$$
\Bigl\langle\frac{\mathrm{d}w}{\mathrm{d}t}\Bigr\rangle = \int_{-\infty}^{\infty}W(s)\,\Gamma(s)\,\mathrm{d}s, \qquad \Gamma(s) = \langle\rho_{\mathrm{pre}}(t)\rho_{\mathrm{post}}(t + s)\rangle .
$$
For independent Poisson trains of rates $r_{\mathrm{pre}}$ and $r_{\mathrm{post}}$, $\Gamma(s) = r_{\mathrm{pre}}r_{\mathrm{post}}$ and the drift is $r_{\mathrm{pre}}r_{\mathrm{post}}(A_+\tau_+ - A_-\tau_-)$. If $A_-\tau_- > A_+\tau_+$, an uncorrelated synapse is weakened on average.

**Proof** The weight change is the sum of $W(t_{\mathrm{post}} - t_{\mathrm{pre}})$ over all pairs, that is $\int\!\!\int\rho_{\mathrm{pre}}(t)\rho_{\mathrm{post}}(t')W(t' - t)\,\mathrm{d}t\,\mathrm{d}t'$ per unit time, and averaging gives the correlation function. For independent Poisson trains $\Gamma$ is constant and the integral of $W$ is $A_+\tau_+ - A_-\tau_-$. $\square$

Two properties follow. First, if the net area of the window is negative, so that the drift of an uncorrelated input is negative, the synapses compete: the postsynaptic **firing rate** is held in check by the depression of the weak synapses, and only the inputs that are correlated with each other, which make the neuron fire, and are therefore followed by postsynaptic spikes within the window, are potentiated (Song, Miller and Abbott 2000). Second, since the potentiation is applied for pre-before-post, STDP is sensitive to the order and not only to the correlation: it favors the inputs that fire first, which are those that predict the postsynaptic spike, and in a population it can shift the responses toward earlier inputs. With slowly varying rates the rule reduces to a correlation rule of the form (22.1) with an additional term proportional to the integral of $W$ ([7.16.14](/7.16.14)).

![Competition under STDP (Formula 22.4.1; one integrate-and-fire neuron with 200 excitatory inputs at 15 Hz, of which inputs 1–100 share a common spike train, correlation coefficient about 0.2, and 101–200 are independent; $A_+ = 0.005$, $A_- = 1.2A_+$, $\tau_\pm = 20\,\mathrm{ms}$, weights between 0 and $g_{\max}$). A: the weights after 600 s: the correlated group has potentiated to the maximum and nearly all independent synapses have been eliminated. B: the mean weight of the two groups against time. C: the STDP window. Net depression ($A_-\tau_- > A_+\tau_+$) is essential: the same simulation with $A_- = A_+$ ends with all synapses at the upper bound](./plots/stdp-competition.py)

## 22.5. Development of Ocular Dominance

[Chapter 7.16.21](/7.16.21#sec-21.4) described the competition of the two eyes for cortical territory. In the model of Miller, Keller and Stryker (1989) and its simplified versions it is a consequence of correlation-based learning with normalization. Let the cortical cell $x$ in a one-dimensional cortex receive input from afferents of the left and the right eye in an arbor, at positions $x + a$ with $\lvert a\rvert \le A$. Afferents from the same eye are correlated, $Q(d)$ decreasing with their distance $d$ in the retina or LGN, and afferents from different eyes are not. The cortical cells interact through a function $B(x - x')$ with short-range excitation and longer-range inhibition. The weights of the two eyes at the afferent positions are $w^{\mathrm{R}}$ and $w^{\mathrm{L}}$; because the sum $w^{\mathrm{R}} + w^{\mathrm{L}}$ is controlled by normalization, we keep it fixed at a constant and follow the difference, $D = w^{\mathrm{R}} - w^{\mathrm{L}} \in [-1, 1]$.

**Formula 22.5.1 (Ocular Dominance Model)** With the correlation rule of Section 22.1 applied to the cortical activity (the input is filtered through the cortical interaction $B$), the difference evolves as

$$
\tau_w\frac{\partial D(x, a)}{\partial t} = \sum_{x'}B(x - x')\sum_{a'}Q\bigl(x + a - x' - a'\bigr)D(x', a'), \tag{22.5}
$$
with $D$ restricted to $[-1, 1]$ (saturation). Initially $D$ is small and random.

**Theorem 22.5.1 (Stripe Period)** If the arbors are wide compared with the correlation distance, so that $\sum_{a'}Q(d + a - a') \approx Q_{\mathrm{tot}}$ for every offset $d$, the modes $D(x, a) = \mathrm{e}^{\mathrm{i}kx}$ grow at the rate $Q_{\mathrm{tot}}\hat B(k)/\tau_w$, where $\hat B$ is the Fourier transform of $B$. The mode of fastest growth has the wave number $k^*$ at which $\hat B$ is maximal, and the ocular dominance stripes initially have period $2\pi/k^*$.

**Proof** Substituting the mode into (22.5) and summing over $a'$ gives $Q_{\mathrm{tot}}\sum_{x'}B(x - x')\mathrm{e}^{\mathrm{i}kx'} = Q_{\mathrm{tot}}\hat B(k)\,\mathrm{e}^{\mathrm{i}kx}$. Linear growth is $\mathrm{e}^{Q_{\mathrm{tot}}\hat B(k)t/\tau_w}$. $\square$

For $B$ a **difference of Gaussians** with excitation of width $\sigma_e$ and inhibition of width $\sigma_i > \sigma_e$, $\hat B(k)$ has a maximum at a nonzero $k^*$, which is why the stripes have a preferred period: the period is set by the range of the intracortical interactions, not by the correlations of the afferents, which only set the overall growth rate, and the lateral inhibition prevents one eye from taking over the whole cortex. The mean of $D$ is the mode $k = 0$ and has a lower growth rate than $k^*$ in this case. Saturation then fixes the stripes with sharp borders and values of $\pm1$.

![Development of ocular dominance stripes (Formula 22.5.1; 96 cortical cells on a ring, arbor of 17 afferent positions, Gaussian afferent correlations of width 2.5, cortical interaction a difference of Gaussians of widths 2 and 7 with relative inhibition 0.25, $D$ clipped to $[-1, 1]$). A: the ocular dominance index of each cortical cell at the start and at later times: weak random differences grow into alternating stripes of dominance of the right and left eyes. B: the final difference $D(x, a)$ for every cortical cell (vertical) and afferent offset (horizontal): domains of each eye with sharp borders, slightly tilted because arbors overlap. C: power spectrum of the ocular dominance index: it is peaked at spatial frequencies of 0.04–0.07 cycles per cell, periods of 14 to 25. Linear theory (Theorem 22.5.1) predicts $k^* = 0.325$, a period of 19.4 cells, for these widths; the stripes seen at the end have a mean period of about 16, because the arbors are only moderately wide](./plots/ocular-dominance.py)

The model reproduces three features of the real cortex: the stripes appear spontaneously from small random differences between the eyes, in agreement with segregation before the critical period; their width is a property of the circuit; and, if one eye is given an advantage (weaker correlation or lower activity), the stripes of the other eye expand, as in monocular deprivation. A positive correlation between the eyes weakens segregation, and for fully correlated inputs there is none; conversely, strabismus, which decorrelates the two eyes, produces a cortex in which almost all cells are monocular (Hubel and Wiesel 1965). The developmental origin of the eye-specific afferent correlations is the **retinal waves** of [7.16.21](/7.16.21#sec-21.5).

## 22.6. Orientation Selectivity and Self-Organizing Maps

### 22.6.1. Receptive Fields from Correlations

The same principle explains how the spatial structure of a receptive field arises. Linsker (1986) showed in a feedforward network of layers with local Gaussian connectivity, driven only by spatially correlated random activity, that a **Hebbian rule** with subtractive normalization produces, layer by layer, center–surround cells and then cells with oriented excitatory and inhibitory regions, without any structured input.

The mechanism is the eigenvector problem of Theorem 22.1.1: the receptive field is the eigenvector of $Q$ that has the largest eigenvalue among the permitted modes, and the symmetry of $Q$ is broken by the shape of the arbor. Miller (1994) extended the analysis to ON-center and OFF-center afferents from the LGN that supply the same cortical cell: competition between the two pathways leads to segregation into ON and OFF subregions side by side, the structure of a **simple cell** ([7.16.18](/7.16.18#sec-18.2.4)).

Orientation selectivity and the maps of orientation appear in the ferret at the time of eye opening, before any patterned visual experience, and are then refined and maintained by experience, which is consistent with the picture of spontaneous activity setting up the first structure.

### 22.6.2. The Kohonen Map

Maps of preferred orientation with **pinwheels** ([7.16.18](/7.16.18#sec-18.3.2)) can be understood with an abstract model of map formation. The cortical sheet is modeled as a grid of units, each with a weight vector $\boldsymbol{w}_i$ in the space of stimulus features.

**Definition 22.6.1 (Self-Organizing Map)** In a **self-organizing map** (Kohonen 1982), each stimulus $\boldsymbol{u}$ selects the unit $c$ with the nearest weight vector, $c = \arg\min_i\lVert\boldsymbol{u} - \boldsymbol{w}_i\rVert$, and all units are moved toward the stimulus in proportion to their closeness to the winner on the sheet:

$$
\boldsymbol{w}_i \leftarrow \boldsymbol{w}_i + \eta\,h(\lVert\boldsymbol{\xi}_i - \boldsymbol{\xi}_c\rVert)\,(\boldsymbol{u} - \boldsymbol{w}_i), \qquad h(d) = \mathrm{e}^{-d^2/2\sigma_h^2}, \tag{22.6}
$$
where $\boldsymbol{\xi}_i$ is the position of unit $i$ on the sheet.

The neighborhood function $h$ plays the role of the cortical interaction $B$: neighboring units learn from the same stimuli and therefore become similar. The map that results preserves the topology of the stimulus space: when the stimulus space has more dimensions than the sheet, such as position, orientation, ocularity and spatial frequency of a visual stimulus, the map folds to cover the space, with the singular points, the pinwheels, as the places where the features change by their full range in a small distance (Durbin and Mitchison 1990; Obermayer, Ritter and Schulten 1990).

Self-organizing maps are abstract: the winner is selected by a global comparison, and the update (22.6) is nonlocal. Their relation to the Hebbian rules is that the winner-take-all selection can be implemented by lateral inhibition and the update by a Hebb rule with decay, as in (22.2), at the winning units. Models of these kinds reproduce the pinwheel density near $\pi$ per squared column spacing and the relations of the orientation and ocular dominance maps (the iso-orientation lines cross the borders of the ocular dominance stripes at right angles).

## 22.7. Competitive and Supervised Learning

The unsupervised rules above find structure in the input without a teacher. In *competitive learning*, an extreme case of the rule of Definition 22.6.1 without neighbors, only the winner of a lateral competition moves its weights toward the input, $\Delta\boldsymbol{w}_c = \eta(\boldsymbol{u} - \boldsymbol{w}_c)$: this is an online version of the $k$-means algorithm ([3.4.11](/3.4.11)) and divides the stimulus space into categories that are represented by single units. The biological basis is the inhibitory competition in cortical networks ([7.16.15](/7.16.15)), with a **Hebbian rule** at the winner.

In supervised learning the weights change to reduce an error between the output and a desired target, as in the delta rule $\Delta\boldsymbol{w} = \eta(r^{\ast} - r)\boldsymbol{u}$ for a target $r^{\ast}$, a close relative of the learning rule of the **perceptron** ([4.7.2](/4.7.2)). It needs a teaching signal. The biological candidates are the climbing fibers of the cerebellum, which carry error signals to the Purkinje cells ([7.16.33](/7.16.33)), and **neuromodulators** that signal reward prediction errors and gate plasticity as a third factor ([7.16.39](/7.16.39)); whether and how the cortex implements error backpropagation across several layers is taken up in [7.16.50](/7.16.50).

The three learning paradigms differ in the information that the synapse needs. A purely Hebbian synapse needs the activities of the pre- and postsynaptic cell; competitive learning needs a signal that identifies the winner; supervised learning needs an error. The development of the visual system, in which all information comes from correlations of spontaneous and sensory activity, is the best example of the first two.

## Summary

| Topic | Key relation |
|---|---|
| Basic Hebb rule (Formula 22.1.1, Theorem 22.1.1) | $\tau_w\dot{\boldsymbol{w}} = Q\boldsymbol{w}$; direction converges to the principal eigenvector of $Q$, the length diverges |
| Normalization (Definition 22.2.1) | Subtractive: removes the mean mode and gives binary weights with competition; multiplicative: keeps $\lvert\boldsymbol{w}\rvert$ and gives a graded outcome |
| Oja's rule (Definition 22.2.2, Theorem 22.2.1) | $\tau_w\dot{\boldsymbol{w}} = r\boldsymbol{u} - \alpha r^2\boldsymbol{w}$ converges to $\boldsymbol{e}_1/\sqrt\alpha$: principal component analysis |
| Covariance rule (Definition 22.3.1) | Replaces $Q$ by the covariance $C$; has LTP and LTD but remains unstable |
| BCM rule (Definition 22.3.2, Theorem 22.3.1) | $r(r - \theta)$ with $\theta = \langle r^2\rangle/r_0$: stable and selective; the neuron responds to one of $K$ patterns, with $r = \theta = Kr_0$ |
| STDP (Formula 22.4.1, Theorem 22.4.1) | Average drift $\int W(s)\Gamma(s)\,\mathrm{d}s$; with $A_-\tau_- > A_+\tau_+$ uncorrelated synapses decay and correlated inputs win |
| Ocular dominance (Formula 22.5.1, Theorem 22.5.1) | Stripes grow from the mode of maximal $\hat B(k)$; period $2\pi/k^*$ set by the intracortical interaction |
| Orientation and maps (Definition 22.6.1) | Receptive fields are eigenvectors of the input correlation; Kohonen maps (neighborhood $h$) preserve topology and create pinwheels |
| Learning paradigms (Section 22.7) | Hebbian: pre and post activity; competitive: winner; supervised: error signal |

## Questions

1. The inputs of a neuron have the correlation matrix $Q = \begin{bmatrix}2 & 1\\ 1 & 2\end{bmatrix}$. Find the long-term weight vector of Oja's rule with $\alpha = 1$ and of the basic **Hebb rule** with subtractive normalization, $\boldsymbol{n} = (1, 1)$.

   **Answer** The eigenvalues of $Q$ are $3$ with $\boldsymbol{e}_1 = (1, 1)/\sqrt2$ and $1$ with $\boldsymbol{e}_2 = (1, -1)/\sqrt2$. Oja's rule gives $\boldsymbol{w} = \pm(1, 1)/\sqrt2$ with $\lvert\boldsymbol{w}\rvert = 1$. For subtractive normalization the mean mode $\boldsymbol{n} \propto \boldsymbol{e}_1$ is removed, so $\boldsymbol{w}$ evolves along $\boldsymbol{e}_2$: the sum $s = w_1 + w_2$ is preserved while the difference $w_1 - w_2$ grows as $\mathrm{e}^{t/\tau_w}$, so that with the weights bounded below by $0$ the rule ends at $(s, 0)$ or $(0, s)$, depending on the sign of the initial difference (if $s \le w_{\max}$): one synapse takes all, which is competition between the two synapses.

2. A BCM neuron is exposed to $K = 3$ equally frequent, linearly independent patterns with $r_0 = 1$. Which fixed points exist, and what are $\theta$ and $\langle r^2\rangle$ in each?

   **Answer** By Theorem 22.3.1, $m$ patterns at $r = \theta$ and the rest at $r = 0$ give $\theta = K r_0/m = 3/m$. For $m = 1$: $\theta = 3$, $\langle r^2\rangle = \tfrac13\cdot9 = 3$, selective and stable. For $m = 2$: $\theta = 3/2$, $r = 3/2$ for two patterns, $\langle r^2\rangle = \tfrac23\cdot\tfrac94 = 3/2$ (unstable). For $m = 3$: $\theta = 1$, $\langle r^2\rangle = 1$ (unstable). In all cases $\theta = \langle r^2\rangle/r_0$, as required.

3. For $A_+ = 0.005$, $A_- = 1.05A_+$ and $\tau_+ = \tau_- = 20\,\mathrm{ms}$, with independent Poisson trains of $15\,\mathrm{Hz}$ pre and postsynaptic rates, what is the mean drift of the weight (in units of $g_{\max}$) per second? How does it change if the postsynaptic rate is doubled?

   **Answer** The integral of the window is $A_+\tau_+ - A_-\tau_- = 0.005\cdot20\,\mathrm{ms}\,(1 - 1.05) = -0.005\,\mathrm{ms}$. With $r_{\mathrm{pre}}r_{\mathrm{post}} = (0.015\,\mathrm{ms^{-1}})^2$ the drift is $-1.1\times10^{-6}\,\mathrm{ms^{-1}} = -1.1\times10^{-3}\,\mathrm{s^{-1}}$. If $r_{\mathrm{post}}$ is doubled, the drift doubles (it is proportional to $r_{\mathrm{post}}$): higher postsynaptic activity increases depression of uncorrelated synapses, a negative feedback that stabilizes the **firing rate**.

4. Derive the wave number $k^*$ at which $\hat B(k) \propto 2\mathrm{e}^{-2k^2} - 0.25\cdot7\,\mathrm{e}^{-49k^2/2}$ is maximal, for the cortical interaction of Section 22.5 ($\sigma_e = 2$, $\sigma_i = 7$, inhibition amplitude $0.25$), and the stripe period.

   **Answer** The Fourier transform of a Gaussian of width $\sigma$ and unit amplitude is $\sigma\sqrt{2\pi}\,\mathrm{e}^{-\sigma^2k^2/2}$, so $\hat B \propto 2\mathrm{e}^{-2k^2} - 1.75\,\mathrm{e}^{-24.5k^2}$. The derivative vanishes when $8k\,\mathrm{e}^{-2k^2} = 85.75\,k\,\mathrm{e}^{-24.5k^2}$ (the factor is $1.75\times49$), that is $\mathrm{e}^{22.5k^2} = 85.75/8 = 10.72$ and $k^{*2} = \ln 10.72/22.5 = 0.1054$. Hence $k^* = 0.325$ and the period is $2\pi/k^* = 19.4$ cells, the value quoted in the figure.

5. (Open question) A correlation-based model and a Kohonen map both produce **orientation maps** with **pinwheels**. Which experimental observations could distinguish between them?

   **Answer** The two models make different assumptions. In the correlation-based model the receptive fields and maps arise from linear, local rules acting on the correlations of the LGN input, and the maps depend on the spatial structure of the afferent arbors and on the intracortical interaction range; the Kohonen model assumes a winner selection and a feature-space embedding. Observations that discriminate include the dependence of the map's wavelength on the cortical interaction range and on the arbor size (measured by the spread of LGN axons), the effect of removing the patterned input on the map in animals raised in the dark (the correlation model predicts a map from spontaneous correlations; the Kohonen model needs a stimulus ensemble in feature space), the relationship between orientation and ocular dominance borders, and the changes of the map under altered visual statistics (stripe-rearing). Since the two models give similar maps for many parameters, quantitative statistics such as the pinwheel density and the spectrum of the map are the usual discriminating measurements.
