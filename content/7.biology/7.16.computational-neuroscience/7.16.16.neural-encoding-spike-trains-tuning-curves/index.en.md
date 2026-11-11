---
title: "Neural Encoding: Spike Trains, Tuning Curves and Receptive Fields"
description: Spike trains and firing rates, PSTHs and kernel estimates, tuning curves, Poisson and renewal statistics of spiking (ISI, Fano factor, coefficient of variation), reverse correlation and the spike-triggered average, LNP models and GLMs, and the main types of neural codes.
---

Sensory neurons, from photoreceptors to cortical cells, report the world in sequences of action potentials. The previous chapters explained how a neuron produces these spikes ([7.16.5](/7.16.5), [7.16.8](/7.16.8)) and how networks shape their rates ([7.16.15](/7.16.15)); this chapter turns the question around and asks how the spikes are related to the stimulus. The relation is statistical: the same stimulus repeated many times never gives the same spike train twice. The mathematical tools of this chapter (firing rates, tuning curves, Poisson statistics, reverse correlation and linear–nonlinear models) are the language of the sensory chapters that follow ([7.16.17](/7.16.17)–[7.16.25](/7.16.25)); the inverse problem, reading the stimulus out of the spikes, is the subject of [7.16.26](/7.16.26), and the information that spikes carry is measured in [7.16.20](/7.16.20).

## 16.1. The Problem of Sensory Coding

Every sensory system must represent four attributes of a stimulus: its modality (light, sound, touch, smell), its intensity, its location in space or on the receptor sheet, and its timing (onset, duration, temporal pattern). The physiology of receptors gave the first answers ([7.14.39](/7.14.39)):

| Attribute | How it is represented | Where in this course |
|---|---|---|
| Modality | Which fibers are active: the **labeled line principle** | 7.14.39; olfaction and taste in [7.16.23](/7.16.23) |
| Intensity | Firing rate of each fiber and the number of fibers recruited; compressed by adaptation and saturation | Section 16.2–16.3; [7.16.20](/7.16.20) |
| Location | Which neurons are active: the position of a **receptive field** in a topographic map | Section 16.5; [7.16.18](/7.16.18), [7.16.21](/7.16.21) |
| Timing | Changes of rate in time; rapidly adapting neurons signal change | Section 16.2, Section 16.7 |

Psychophysics provides the other side of the comparison: discrimination thresholds that grow in proportion to intensity (the **Weber–Fechner law**) and magnitude estimates that follow **Stevens' power law** ([7.14.39](/7.14.39#sec-39.2.3)). One aim of quantitative neuroscience is to explain such laws from the statistics of neural responses; the comparison between single-neuron and behavioral discrimination is made precise with signal detection theory in [7.16.26](/7.16.26).

Two difficulties make encoding a statistical problem. First, responses are variable: the trial-to-trial fluctuations of a cortical neuron are comparable to its mean response. Second, natural stimuli have many dimensions (an image has as many as there are pixels), so a neuron cannot be characterized by presenting every stimulus. The two answers are averages over trials (firing rates, tuning curves) and averages over random stimuli (reverse correlation).

## 16.2. Spike Trains and Firing Rates

Action potentials last about $1\,\mathrm{ms}$ and are stereotyped, so all the information they carry is in their times.

**Definition 16.2.1 (Spike Train)** A sequence of spike times $t_1, t_2, \dots, t_n$ recorded in an interval $[0, T]$ is a **spike train**. It is represented by the neural response function

$$
\rho(t) = \sum_{k=1}^{n} \delta(t - t_k),
$$
so that sums over spikes become integrals: $\sum_k h(t - t_k) = \int_0^T h(\tau)\,\rho(t - \tau)\,\mathrm{d}\tau$.

The simplest summary of a spike train is its spike-count rate $n/T$. It discards all temporal structure, and for a stimulus that changes in time we need a rate that is itself a function of time. Because a single train contains only zeros and spikes, the rate must be defined as an average over trials.

**Definition 16.2.2 (Firing Rate)** Let $\langle\cdot\rangle$ denote the average over repeated trials of the same stimulus. The **firing rate** of a neuron at time $t$ is

$$
r(t) = \lim_{\Delta t \to 0} \frac{1}{\Delta t}\int_t^{t + \Delta t} \langle\rho(\tau)\rangle\,\mathrm{d}\tau = \langle\rho(t)\rangle,
$$
so that $r(t)\,\Delta t$ is the probability of a spike in a small interval $[t, t + \Delta t)$. Its unit is $\mathrm{Hz}$ (spikes per second).

The limit cannot be taken with finitely many trials; in practice the rate is estimated by counting spikes in bins or by smoothing.

**Definition 16.2.3 (Peri-Stimulus Time Histogram)** The **peri-stimulus time histogram** (PSTH) is the histogram of spike times, aligned to the stimulus onset and pooled over $N$ trials, divided by $N\,\Delta t$, where $\Delta t$ is the bin width. It estimates $r(t)$ as a piecewise constant function.

A smoother estimate replaces the bins by a window function $w(\tau)$ with $\int w(\tau)\,\mathrm{d}\tau = 1$:

$$
r_{\mathrm{est}}(t) = \frac{1}{N}\sum_{\text{trials}}\int w(\tau)\,\rho(t - \tau)\,\mathrm{d}\tau, \tag{16.1}
$$
a **convolution** of the spike train with a kernel, the same construction as **kernel density estimation** in statistics. A Gaussian window $w(\tau) = \mathrm{e}^{-\tau^2/2\sigma_w^2}/\sqrt{2\pi}\sigma_w$ gives a smooth estimate; a causal window such as $w(\tau) = \alpha^2\tau\mathrm{e}^{-\alpha\tau}$ for $\tau > 0$ uses only past spikes, as a downstream neuron must, and resembles the postsynaptic current that a spike produces ([7.16.12](/7.16.12)). The window width is a bias–variance trade-off: narrow windows follow fast changes but are noisy, wide windows are smooth but blur transients.

![Estimating a time-dependent firing rate. A model neuron fires as an inhomogeneous Poisson process (Section 16.4) with a true rate (dashed) of 5 Hz at baseline, a fast transient peaking at 80 Hz 0.2 s after stimulus onset and a sustained response of 45 Hz between 0.5 and 1.2 s. A: raster of 40 trials, one row per trial; the spike times differ on every trial. B: PSTH with 25 ms bins (Definition 16.2.3). C: estimates by Eq. (16.1) with Gaussian windows of standard deviation 5, 20 and 80 ms. The 5 ms estimate follows the transient but fluctuates strongly; the 80 ms estimate is smooth but reduces the 80 Hz transient to 30 Hz](./plots/spike-raster-psth.py)

## 16.3. Tuning Curves

When a stimulus is characterized by a single parameter $s$ (the orientation of a bar, the direction of a movement, the frequency of a tone), the average response is a function of $s$.

**Definition 16.3.1 (Tuning Curve)** The **tuning curve** $f(s)$ of a neuron is its average firing rate, or average spike count divided by the counting time, as a function of a stimulus parameter $s$: $f(s) = \langle r \rangle_s$. The stimulus value that maximizes $f$ is its preferred stimulus $s_{\mathrm{pref}}$.

Four functional forms cover most measured tuning curves:

| Form | Formula | Typical example |
|---|---|---|
| Gaussian | $f(s) = r_{\max}\exp\!\bigl(-\tfrac{(s - s_{\mathrm{pref}})^2}{2\sigma_f^2}\bigr)$ | Orientation in V1 ([7.16.18](/7.16.18)), place fields |
| Rectified cosine | $f(s) = \bigl[r_0 + (r_{\max} - r_0)\cos(s - s_{\mathrm{pref}})\bigr]_+$ | Arm movement direction in motor cortex (Georgopoulos 1982), wind direction in cricket cercal interneurons |
| Von Mises | $f(s) = r_0 + A\,\mathrm{e}^{\kappa\cos(s - s_{\mathrm{pref}})}$ | Circular variables with narrow tuning: head direction ([7.16.44](/7.16.44)) |
| Sigmoid | $f(s) = \dfrac{r_{\max}}{1 + \exp\bigl((s_{1/2} - s)/\Delta_s\bigr)}$ | Binocular disparity ("near" and "far" cells), intensity coding |

Here $[x]_+ = \max(x, 0)$. A tuning curve summarizes only the mean; the variability around it is described by the spike-count distribution $\mathbb{P}(n \mid s)$, which together with $f$ is everything a decoder can use ([7.16.26](/7.16.26)). Tuning curves are not fixed properties: attention, adaptation and the behavioral state change their gain or position ([7.16.18](/7.16.18#sec-18.7)).

**Remark 16.3.1** A tuning curve is a slice through a higher-dimensional dependence. A V1 neuron tuned to orientation is also tuned to spatial frequency, position, contrast and often direction; varying one parameter while holding the others at their preferred values gives one tuning curve. Reverse correlation (Section 16.5) characterizes the dependence on all dimensions at once.

## 16.4. Spike Statistics

### 16.4.1. The Poisson Model

The simplest stochastic description of a spike train assumes that spikes occur independently of one another, with probability $r(t)\,\mathrm{d}t$ in each small interval: a **Poisson process** ([7.6.32](/7.6.32#def-32.1.1)) with rate $r(t)$. For neural spike trains it is called homogeneous when $r$ is constant and inhomogeneous when $r$ varies in time.

**Theorem 16.4.1 (Poisson Spike Counts and Intervals)** For a homogeneous Poisson spike train with rate $r$:

1. the number of spikes $n$ in an interval of length $T$ has the **Poisson distribution** $\mathbb{P}_T(n) = \frac{(rT)^n}{n!}\mathrm{e}^{-rT}$, so $\mathbb{E}[n] = \operatorname{Var}(n) = rT$;
2. the *interspike intervals* (ISIs, the times between successive spikes) are independent and follow the **exponential distribution** $p(\tau) = r\mathrm{e}^{-r\tau}$, with mean $1/r$ and standard deviation $1/r$.

For an inhomogeneous Poisson train the count in $[t_1, t_2]$ is Poisson with mean $\int_{t_1}^{t_2} r(t)\,\mathrm{d}t$.

**Proof** Divide $T$ into $M$ bins of width $\Delta t = T/M$. Each bin contains a spike with probability $r\Delta t$ independently, so $n \sim \mathrm{Bin}(M, rT/M)$, which tends to $\mathrm{Poi}(rT)$ as $M \to \infty$. The probability that no spike follows a given spike for a time $\tau$ is $\mathbb{P}_\tau(0) = \mathrm{e}^{-r\tau}$; the density of the next spike is minus its derivative, $r\mathrm{e}^{-r\tau}$. Independence of the intervals follows from the independence of disjoint bins. For a time-dependent rate the bin probabilities are $r(t_i)\Delta t$, and the same limit gives a Poisson count with mean $\sum_i r(t_i)\Delta t \to \int r\,\mathrm{d}t$. $\square$

The theorem gives a simple algorithm for generating spikes: in each time step draw a uniform random number $x_i$ and fire if $x_i < r(t_i)\,\Delta t$; or, for a time-dependent rate, generate a homogeneous train at the maximal rate $r_{\max}$ and keep each spike at time $t$ with probability $r(t)/r_{\max}$ ("thinning"), as in the first figure.

### 16.4.2. Measures of Variability

Two dimensionless numbers summarize the variability of spiking, one for counts and one for intervals.

**Definition 16.4.1 (Coefficient of Variation of Interspike Intervals)** The **coefficient of variation** of the interspike intervals is $C_V = \sigma_\tau/\langle\tau\rangle$, the standard deviation of the intervals divided by their mean.

The **Fano factor** of spike counts in a window of length $T$ is $F(T) = \operatorname{Var}(n)/\mathbb{E}[n]$. By Theorem 16.4.1 a Poisson process has $F = 1$ for every $T$ and $C_V = 1$; a perfectly regular train has $F \to 0$ and $C_V = 0$.

Real neurons are not Poisson at short time scales: after each spike there is an **absolute refractory period** of $1$–$2\,\mathrm{ms}$ and a longer relative refractory period. The simplest correction is a dead time: after each spike the rate is zero for $\tau_{\mathrm{ref}}$ and then returns to its value. More generally, a renewal process is one whose intervals are independent and identically distributed with an arbitrary density $p(\tau)$; a common choice is the **gamma distribution** of order $k$, $p(\tau) \propto \tau^{k-1}\mathrm{e}^{-kr\tau}$, which has mean $1/r$ and $C_V = 1/\sqrt k$ (the interval is a sum of $k$ exponential stages, like a neuron that must accumulate $k$ input events to fire).

**Theorem 16.4.2 (Fano Factor of a Renewal Process)** For a stationary renewal process with interval coefficient of variation $C_V$, the Fano factor of counts satisfies $F(T) \to C_V^2$ as $T \to \infty$.

**Proof** Let $\mu = \langle\tau\rangle$ and $\sigma^2 = \operatorname{Var}(\tau)$. The time $S_n = \tau_1 + \cdots + \tau_n$ of the $n$-th spike has mean $n\mu$ and variance $n\sigma^2$, and by the **central limit theorem** it is approximately normal for large $n$. The event $\{n(T) \geq n\}$ is the event $\{S_n \leq T\}$. Writing $n = T/\mu + x\sqrt{T}$ and expanding, $\mathbb{P}(S_n \leq T) \approx \Phi\bigl(-x\mu^{3/2}/\sigma\bigr)$, so $n(T)$ is approximately normal with mean $T/\mu$ and variance $\sigma^2T/\mu^3$. Hence $F = (\sigma^2T/\mu^3)/(T/\mu) = \sigma^2/\mu^2 = C_V^2$. $\square$

For a dead-time process $\tau = \tau_{\mathrm{ref}} + \mathrm{Exp}$, the mean is $1/r$ and the standard deviation $1/r - \tau_{\mathrm{ref}}$, so $C_V = 1 - r\tau_{\mathrm{ref}}$: refractoriness makes firing more regular at high rates and matters little at low rates.

![Interval and count statistics of three renewal processes with the same rate, 20 Hz. A: ISI distributions from simulation (stepped histograms) and theory (smooth curves): Poisson (exponential, $C_V = 1$), Poisson with a 10 ms dead time ($C_V = 1 - r\tau_{\mathrm{ref}} = 0.8$), and a gamma process of order 4 ($C_V = 0.5$), whose short intervals are rare. B: the Fano factor of spike counts against the counting window. For the Poisson process it equals 1 at every window; for the more regular processes it starts near 1 in short windows (where at most one spike falls in a window) and decreases toward $C_V^2$ (dotted lines) as the window grows, as stated in Theorem 16.4.2](./plots/spike-statistics.py)

### 16.4.3. How Poisson Are Real Neurons?

Cortical neurons firing in vivo come surprisingly close to the Poisson description at time scales longer than the refractory period. Neurons in monkey MT responding to moving random dots have Fano factors between about $1$ and $1.5$ over a wide range of mean counts, with the variance roughly proportional to the mean, and interspike intervals of neurons firing at low rates in vivo have $C_V$ close to $1$ (Softky and Koch 1993; Shadlen and Newsome 1998). This is a puzzle: a neuron that integrates hundreds of independent excitatory inputs over a membrane time constant of $10$–$20\,\mathrm{ms}$ should average out their fluctuations and fire regularly. The resolution is a balance of excitation and inhibition: when large excitatory and inhibitory currents nearly cancel, the mean input stays below threshold and spikes are triggered by fluctuations, which makes their timing irregular ([7.16.15](/7.16.15), [7.16.31](/7.16.31)).

Deviations from Poisson statistics are informative as well:

- Precision: neurons driven by rapidly fluctuating stimuli can fire with millisecond reproducibility from trial to trial (the fly visual neuron H1, retinal ganglion cells, cortical neurons in slices driven by noisy current), with Fano factors well below 1 (Mainen and Sejnowski 1995).
- Bursting: neurons that fire in bursts ([7.16.7](/7.16.7)) have $C_V > 1$ and an excess of short intervals.
- Slow fluctuations of excitability across trials, caused by changes of arousal or attention, raise the Fano factor at long time scales; the Fano factor of cortical neurons falls at stimulus onset (Churchland et al. 2010), a sign that the stimulus quenches such fluctuations.

## 16.5. Reverse Correlation

### 16.5.1. The Spike-Triggered Average

To characterize a neuron without presenting every stimulus, we present a random stimulus $s(t)$ with mean zero and ask what preceded the spikes.

**Definition 16.5.1 (Spike-Triggered Average)** The **spike-triggered average** (STA) of a stimulus is the average value of the stimulus a time $\tau$ before a spike,

$$
C(\tau) = \Bigl\langle \frac{1}{n}\sum_{k=1}^{n} s(t_k - \tau)\Bigr\rangle \approx \frac{1}{\langle n\rangle}\int_0^T \langle\rho(t)\rangle\, s(t - \tau)\,\mathrm{d}t = \frac{1}{\langle r\rangle}Q_{rs}(-\tau),
$$
where $Q_{rs}(\tau) = \frac{1}{T}\int_0^T r(t)\,s(t + \tau)\,\mathrm{d}t$ is the correlation function of the firing rate and the stimulus. The method of computing it is called **reverse correlation**.

The STA is the stimulus feature to which the neuron is sensitive. In space and time it is the spatiotemporal **receptive field** of the neuron: for a retinal ganglion cell stimulated by flickering random checkerboards it shows a center–surround structure that reverses sign over about $100\,\mathrm{ms}$; for a V1 **simple cell**, an oriented Gabor-like pattern ([7.16.18](/7.16.18)).

### 16.5.2. Linear Estimation of the Firing Rate

The STA becomes a predictive model through a linear approximation of the rate,

$$
r_{\mathrm{est}}(t) = r_0 + \int_0^\infty D(\tau)\,s(t - \tau)\,\mathrm{d}\tau, \tag{16.2}
$$
where $D(\tau)$ is a linear kernel (filter) and $r_0$ the background rate. This is the first term of the Volterra–Wiener expansion of the response as a functional of the stimulus.

**Theorem 16.5.1 (Optimal Linear Kernel for White Noise)** Choose $D$ to minimize the mean squared error $\frac{1}{T}\int_0^T (r(t) - r_{\mathrm{est}}(t))^2\,\mathrm{d}t$. If the stimulus is **white noise** with autocorrelation $Q_{ss}(\tau) = \sigma_s^2\delta(\tau)$, the optimal kernel is proportional to the spike-triggered average:

$$
D(\tau) = \frac{Q_{rs}(-\tau)}{\sigma_s^2} = \frac{\langle r\rangle\,C(\tau)}{\sigma_s^2}. \tag{16.3}
$$

**Proof** Setting the functional derivative of the error with respect to $D(\tau)$ to zero gives the normal equation $\int_0^\infty Q_{ss}(\tau - \tau')\,D(\tau')\,\mathrm{d}\tau' = Q_{rs}(-\tau)$ for $\tau \geq 0$. With $Q_{ss}(\tau - \tau') = \sigma_s^2\delta(\tau - \tau')$ the integral reduces to $\sigma_s^2 D(\tau)$. The last equality is Definition 16.5.1. $\square$

For stimuli with correlations, the normal equation must be solved by deconvolution: in the frequency domain $\tilde D(\omega) = \tilde Q_{rs}(-\omega)/\tilde Q_{ss}(\omega)$, the **Wiener filter**. White noise is the convenient choice because it removes this step and because it probes all frequencies equally; natural stimuli, which are strongly correlated ([7.16.20](/7.16.20)), require the deconvolution and a regularization of the small eigenvalues of $Q_{ss}$.

**Example 16.5.1** The linear kernels of the fly motion-sensitive neuron H1, measured with a randomly moving pattern, last about $30\,\mathrm{ms}$ and predict the slow modulation of its rate well; the kernel of a neuron in the electrosensory system of the weakly electric fish *Eigenmannia* is similarly brief. In both cases the linear prediction captures the times of rate changes but not their sizes for strong stimuli, because firing rates cannot be negative and saturate: the response is linear only over a limited range.

## 16.6. Linear–Nonlinear Models

### 16.6.1. The LNP Model

The failure of Eq. (16.2) for strong stimuli is repaired by passing the linear prediction through a static nonlinearity.

**Definition 16.6.1 (Linear–Nonlinear–Poisson Model)** In a **linear–nonlinear–Poisson model** (LNP model) the stimulus is filtered by a linear kernel, $x(t) = \int_0^\infty D(\tau)\,s(t - \tau)\,\mathrm{d}\tau$ (or, for spatiotemporal stimuli, a projection $x = \boldsymbol{k}\cdot\boldsymbol{s}$ onto a receptive field $\boldsymbol{k}$), the result is passed through a nonlinear function $F \geq 0$, and spikes are generated by an inhomogeneous Poisson process with rate $r(t) = F(x(t))$.

The model separates three things a sensory neuron does: select a feature (the filter), convert its strength into a rate (rectification, threshold and saturation, the f–I curve of [7.16.8](/7.16.8)), and add variability. Its parameters can be estimated from white-noise data in two steps.

**Theorem 16.6.1 (STA of an LNP Neuron)** If the stimulus is Gaussian white noise and the neuron is an LNP model with filter $D$ and nonlinearity $F$, the spike-triggered average is proportional to $D$ for any $F$ for which the proportionality constant is nonzero.

**Proof** Consider a discretized stimulus vector $\boldsymbol{s}$ with independent standard normal components, and $x = \boldsymbol{D}\cdot\boldsymbol{s}$. The STA is $\mathbb{E}[F(x)\boldsymbol{s}]/\mathbb{E}[F(x)]$. Decompose $\boldsymbol{s} = \frac{x}{\|\boldsymbol{D}\|^2}\boldsymbol{D} + \boldsymbol{s}_\perp$, where for a Gaussian $\boldsymbol{s}$ the component $\boldsymbol{s}_\perp$ orthogonal to $\boldsymbol{D}$ is independent of $x$ and has mean zero. Then $\mathbb{E}[F(x)\boldsymbol{s}_\perp] = \mathbb{E}[F(x)]\,\mathbb{E}[\boldsymbol{s}_\perp] = \boldsymbol{0}$, so the STA equals $\frac{\mathbb{E}[xF(x)]}{\|\boldsymbol{D}\|^2\mathbb{E}[F(x)]}\boldsymbol{D}$. $\square$

The proof uses the spherical symmetry of the Gaussian distribution: with non-Gaussian stimuli (natural images) the STA is biased toward the stimulus correlations. Once $D$ is known, $F$ is estimated by computing $x(t)$ for the whole stimulus and dividing the histogram of $x$ at spike times by the histogram of all $x$ values (Chichilnisky 2001). The constant in the theorem is zero for symmetric nonlinearities such as $F(x) = x^2$, the case of a V1 **complex cell** that responds to a feature regardless of its sign ([7.16.18](/7.16.18#sec-18.2)); such neurons are characterized by the spike-triggered covariance, whose eigenvectors with changed variance give the relevant filters.

![Reverse correlation on a simulated LNP neuron (Definition 16.6.1). The stimulus is Gaussian white noise in 2 ms steps; the filter is biphasic (a positive lobe peaking at 15 ms followed by a weak negative lobe), the nonlinearity a sigmoid with a maximum of 60 Hz, and 200 s of simulated recording give about 2500 Poisson spikes. A: the spike-triggered average (blue) and the true filter (dashed, scaled), plotted against the time before the spike; as Theorem 16.6.1 states, the STA has the shape of the filter despite the strongly nonlinear $F$. B: the nonlinearity estimated by dividing the number of spikes by the time spent at each value of the filtered stimulus (dots), against the true $F$ (dashed). The scatter at high values comes from the few samples there](./plots/lnp-sta.py)

### 16.6.2. Generalized Linear Models

The LNP model ignores the neuron's own history: refractoriness, adaptation and bursting make the probability of a spike depend on the times of earlier spikes. A **generalized linear model** ([3.3.6](/3.3.6); applied to counts in [7.7.14](/7.7.14)) adds this dependence while keeping the estimation tractable (Truccolo et al. 2005; Pillow et al. 2008):

$$
r(t) = \exp\Bigl(b + \int_0^\infty \boldsymbol{k}(\tau)\cdot\boldsymbol{s}(t - \tau)\,\mathrm{d}\tau + \sum_{t_j < t} h(t - t_j) + \sum_{i}\sum_{t^{(i)}_j < t} c_i(t - t^{(i)}_j)\Bigr), \tag{16.4}
$$
with a stimulus filter $\boldsymbol{k}$, a post-spike filter $h$ (negative at short lags for refractoriness, positive at intermediate lags for bursting) and coupling filters $c_i$ from the spikes of other recorded neurons. The spike train is a point process with conditional intensity $r(t)$, and its log-likelihood

$$
\log L = \sum_k \log r(t_k) - \int_0^T r(t)\,\mathrm{d}t
$$
is concave in all the filter parameters when the link function is exponential (Paninski 2004), so maximum likelihood has a unique optimum that is found by convex optimization. Fitted to simultaneously recorded primate retinal ganglion cells, the coupled GLM predicted the timing of individual spikes and showed that the correlations between neighbors carry information that a model of independent cells misses (Pillow et al. 2008). A neuron with an exponential nonlinearity and a strongly negative post-spike filter is close to a stochastic integrate-and-fire neuron ([7.16.8](/7.16.8)): the GLM is the statistical counterpart of the mechanistic models of the previous part.

## 16.7. Types of Neural Codes

Which features of a spike train carry information? The question has no single answer, but four kinds of code are distinguished.

**Definition 16.7.1 (Rate Code and Temporal Code)** A neuron uses a **rate code** if the information about the stimulus is carried by its spike count, or by its firing rate on a time scale slower than the fastest changes of the stimulus. It uses a **temporal code** if the precise timing of spikes, on a time scale finer than that on which the stimulus changes, carries additional information.

The distinction depends on time scales, not on whether rates change in time: a rate that follows a rapidly changing stimulus is still a rate code. An example of a temporal code is the response of a neuron to a stimulus with a slow envelope in which spikes lock to a fine temporal structure: auditory nerve fibers fire at a particular phase of a low-frequency tone ([7.16.24](/7.16.24)), and the first spike latency of tactile afferents in the human fingertip carries information about the direction of force faster than any rate could (Johansson and Birznieks 2004).

**Definition 16.7.2 (Phase Code)** In a **phase code** information is carried by the timing of spikes relative to an ongoing network oscillation rather than relative to the stimulus.

The best-known example is phase precession in hippocampal place cells: as a rat crosses a place field, the cell fires at progressively earlier phases of the $8\,\mathrm{Hz}$ theta rhythm, so the phase tells where in the field the animal is ([7.16.42](/7.16.42)).

**Definition 16.7.3 (Population Code)** In a **population code** a stimulus variable is represented by the joint activity of many neurons with overlapping **tuning curves**, so that the stimulus can be read out only from the population and not from any single neuron.

Population codes are the rule rather than the exception: the direction of an arm movement is represented by the broadly tuned cells of motor cortex, whose **population vector** points in the direction of movement, and the orientation of a bar by the hundreds of V1 neurons with different preferred orientations. In a population, a further distinction is whether neurons can be treated as independent given the stimulus (an independent-neuron code) or whether their correlations, for example synchronous firing, carry information of their own (a correlation code). Measured **noise correlations** are weak (correlation coefficients of $0.05$–$0.2$) but, summed over many neurons, they can limit the information a population carries; how to decode populations and how much correlations matter is the subject of [7.16.26](/7.16.26).

| Code | What carries the information | Time scale | Example |
|---|---|---|---|
| Rate | Spike count or slowly varying rate | $\gtrsim 50\,\mathrm{ms}$ | Muscle spindle afferents, MT direction |
| Temporal | Precise spike times relative to the stimulus | $1$–$10\,\mathrm{ms}$ | Auditory phase locking, first-spike latency |
| Phase | Spike time relative to an oscillation | Fraction of a cycle | Hippocampal phase precession |
| Population | Pattern across neurons | Any of the above | Motor cortex direction, place cell ensembles |

## Summary

| Concept | Key relation |
|---|---|
| Spike train and firing rate (Definitions 16.2.1, 16.2.2) | $\rho(t) = \sum_k\delta(t - t_k)$, $r(t) = \langle\rho(t)\rangle$, estimated by the PSTH or by kernel smoothing, Eq. (16.1), with a bias–variance trade-off |
| Tuning curve (Definition 16.3.1) | Mean rate as a function of a stimulus parameter: Gaussian, cosine, von Mises, sigmoid |
| Poisson spiking (Theorem 16.4.1) | Counts $\mathrm{Poi}(rT)$, intervals $\mathrm{Exp}(r)$, $F = C_V = 1$ |
| Variability (Definition 16.4.1, Theorem 16.4.2) | Refractoriness and gamma processes reduce $C_V$; for renewal processes $F(T) \to C_V^2$; cortical neurons in vivo have $F \approx 1$–$1.5$, explained by balanced input |
| Reverse correlation (Definition 16.5.1, Theorem 16.5.1) | STA $= Q_{rs}(-\tau)/\langle r\rangle$; for white noise the optimal linear kernel is proportional to the STA |
| LNP model (Definition 16.6.1, Theorem 16.6.1) | Filter, static nonlinearity, Poisson spikes; with Gaussian white noise the STA recovers the filter for any nonlinearity with nonzero constant |
| GLM, Eq. (16.4) | Exponential link with stimulus, spike-history and coupling filters; concave log-likelihood |
| Codes (Definitions 16.7.1–16.7.3) | Rate, temporal, phase and population codes are distinguished by what carries the information and on which time scale |

## Questions

1. A neuron fires as a homogeneous Poisson process at $10\,\mathrm{Hz}$. What is the probability that it fires no spike in a $200\,\mathrm{ms}$ window, and what is the probability that two consecutive spikes are less than $5\,\mathrm{ms}$ apart?

   **Answer** The count in $200\,\mathrm{ms}$ is $\mathrm{Poi}(2)$, so $\mathbb{P}(0) = \mathrm{e}^{-2} \approx 0.135$. Intervals are $\mathrm{Exp}(10\,\mathrm{s^{-1}})$, so $\mathbb{P}(\tau < 0.005\,\mathrm{s}) = 1 - \mathrm{e}^{-0.05} \approx 0.049$: about 5 % of intervals would be shorter than $5\,\mathrm{ms}$, which a real neuron with a few milliseconds of refractoriness would not produce, and a pure Poisson model therefore overestimates short intervals.

2. Show that a dead-time Poisson process with rate $r$ (mean interval $1/r$) and refractory period $\tau_{\mathrm{ref}}$ has $C_V = 1 - r\tau_{\mathrm{ref}}$, and compute its long-window Fano factor at $r = 50\,\mathrm{Hz}$, $\tau_{\mathrm{ref}} = 5\,\mathrm{ms}$.

   **Answer** The interval is $\tau = \tau_{\mathrm{ref}} + X$ with $X$ exponential of mean $1/r - \tau_{\mathrm{ref}}$ (so that the mean interval is $1/r$). The standard deviation of $\tau$ is that of $X$, $1/r - \tau_{\mathrm{ref}}$, so $C_V = (1/r - \tau_{\mathrm{ref}})/(1/r) = 1 - r\tau_{\mathrm{ref}}$. At $r = 50\,\mathrm{Hz}$ and $\tau_{\mathrm{ref}} = 5\,\mathrm{ms}$, $C_V = 0.75$ and, by Theorem 16.4.2, $F \to 0.5625$.

3. Why does the STA of a V1 complex cell measured with white noise come out nearly flat, although the cell responds strongly to the noise? How would you characterize such a cell?

   **Answer** A complex cell responds to an oriented feature regardless of its polarity (a bright bar and a dark bar at the same place both excite it), as if its nonlinearity were even, $F(x) = x^2$ or the **energy model** of [7.16.18](/7.16.18). Then $\mathbb{E}[xF(x)] = 0$ for a symmetric $x$, and the constant in Theorem 16.6.1 vanishes: stimuli with opposite signs cancel in the average. The relevant filters show up instead in the second moment: the spike-triggered covariance $\mathbb{E}[\boldsymbol{s}\boldsymbol{s}^{\mathsf T}\mid\text{spike}] - \mathbb{E}[\boldsymbol{s}\boldsymbol{s}^{\mathsf T}]$ has eigenvectors with increased variance along the quadrature pair of Gabor filters that the cell squares and sums.

4. (Open question) A GLM fitted to a retinal ganglion cell has a post-spike filter that is strongly negative for $2\,\mathrm{ms}$, positive between $5$ and $15\,\mathrm{ms}$, and zero afterwards. What firing pattern does the model produce, and why would a model without the post-spike filter predict a Fano factor that is too large?

   **Answer** The negative part implements refractoriness, and the positive part makes a second spike likely a few milliseconds after the first: the model fires in short bursts of two or three spikes. Without the post-spike filter the model is an inhomogeneous Poisson process given the stimulus, so its count variance equals its mean (Fano factor 1). Real ganglion cells driven by a repeated stimulus fire with high temporal precision and Fano factors well below 1 because refractoriness regularizes their intervals; the negative history term reproduces this reduced variability, while bursting alone would increase it, so the net Fano factor depends on the balance of the two lobes.
