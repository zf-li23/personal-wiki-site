---
title: Information Theory and Efficient Coding
description: Entropy and mutual information of neural responses; Laughlin's fly interneurons and histogram equalization; whitening and the center-surround receptive field; direct estimation of spike-train information and its bias; sparse coding and the origin of Gabor-like receptive fields; energy cost and sparse firing; tests and limits of the efficient coding hypothesis.
---

The previous chapters described what neurons encode and how it is measured ([7.16.16](/7.16.16), [7.16.18](/7.16.18)). This chapter asks a normative question: why do **receptive fields** and response functions have the shapes they have? Barlow (1961) suggested that sensory systems are adapted to the statistics of the natural world so that they transmit as much information as possible, with as few resources as possible. This idea, the *efficient coding hypothesis*, turns the design of a sensory neuron into an optimization problem whose solution can be compared with recordings. The **entropy** and the **mutual information** are defined in [4.5.6](/4.5.6#def-6.2.1) and [7.6.35](/7.6.35#def-35.3.1); here we use them as tools for neural data. In this chapter $H$ denotes an entropy and $I$ a mutual information, not an enthalpy or a current; information is measured in bits ($\log_2$).

## 20.1. Entropy and Mutual Information of Neural Responses

### 20.1.1. Information in a Response

Let $S$ be a stimulus drawn from a distribution $p(s)$ and $R$ the neural response, for example a spike count, with conditional distribution $p(r \mid s)$. The **entropy** of the response, $H(R) = -\sum_r p(r)\log_2 p(r)$, measures in bits how variable the response is. Because the response varies for two reasons, because the stimulus changes and because the neuron is noisy, the entropy splits into two parts, and only the first carries information about the stimulus.

**Definition 20.1.1 (Information Between Stimulus and Response)** The **mutual information** between stimulus and response is

$$
I(S;R) = H(R) - H(R \mid S) = H(R) - \sum_s p(s)\,H(R \mid s), \tag{20.1}
$$
where $H(R \mid S)$, the average of $H(R \mid s) = -\sum_r p(r \mid s)\log_2 p(r \mid s)$ over stimuli, is the noise entropy: the variability that remains when the stimulus is fixed.

The information is symmetric, $I(S;R) = I(R;S)$, never negative, zero when the response does not depend on the stimulus, and bounded by $H(R)$ and by the entropy of the stimulus. Unlike the correlation coefficient or the variance explained, it makes no assumption about the form of the dependence. The maximum of $I(S;R)$ over stimulus distributions is the **channel capacity** of the neuron. A response with $K$ equally likely values has $H(R) = \log_2 K$ bits, so that a neuron whose spike count could take 8 equally likely values would transmit at most 3 bits.

**Example 20.1.1 (Information in a Poisson Spike Count)** A neuron fires $R$ spikes in a window with mean $\lambda(s)$, with $R \sim \mathrm{Poi}(\lambda)$ ([7.16.16](/7.16.16#sec-16.4)), and the stimulus is such that $\lambda$ is uniformly distributed on $[0, \lambda_{\max}]$. The marginal distribution of $R$ is the uniform mixture of Poisson distributions and the noise entropy is the mean of the entropies of $\mathrm{Poi}(\lambda)$. Evaluating the sums numerically:

| $\lambda_{\max}$ | $H(R)$ (bits) | $H(R \mid S)$ (bits) | $I(S;R)$ (bits) |
|---|---|---|---|
| 5 | 2.93 | 2.42 | 0.51 |
| 20 | 4.62 | 3.46 | 1.16 |
| 100 | 6.78 | 4.64 | 2.14 |

A neuron whose mean count ranges up to 100 spikes transmits only about 2 bits about the stimulus, because Poisson noise ($\operatorname{Var} = \lambda$) makes neighboring rates indistinguishable: the number of distinguishable levels grows only as $\sqrt{\lambda_{\max}}$, and information as $\tfrac12\log_2\lambda_{\max}$ plus a constant. This slow, logarithmic growth is one reason why sensory information is carried by populations of neurons ([7.16.26](/7.16.26)).

For a continuous response the same quantities are defined with integrals (differential entropies), with the difference that a differential entropy depends on the units of measurement and is meaningful only in differences; the mutual information, a difference of two such entropies, is invariant. A case that can be solved exactly is a linear Gaussian channel.

**Theorem 20.1.1 (Gaussian Channel)** Let $R = S + \eta$ with $S \sim \mathcal{N}(0, \sigma_S^2)$ and independent noise $\eta \sim \mathcal{N}(0, \sigma_\eta^2)$. Then

$$
I(S;R) = \frac12\log_2\Bigl(1 + \frac{\sigma_S^2}{\sigma_\eta^2}\Bigr).
$$

**Proof** The differential entropy of $\mathcal{N}(0, \sigma^2)$ is $\tfrac12\log_2(2\pi\mathrm{e}\,\sigma^2)$. The response is normal with variance $\sigma_S^2 + \sigma_\eta^2$, and given $s$ it is normal with variance $\sigma_\eta^2$. Subtracting, $I = \tfrac12\log_2\bigl((\sigma_S^2 + \sigma_\eta^2)/\sigma_\eta^2\bigr)$. $\square$

For a signal with a power spectrum $Q_{ss}(f)$ in additive noise with spectrum $Q_{\eta\eta}(f)$, the theorem applies in each frequency band and the rate of information is $\int_0^{\infty}\log_2\bigl(1 + Q_{ss}(f)/Q_{\eta\eta}(f)\bigr)\,\mathrm{d}f$ bits per second (Shannon). This formula is the basis of the whitening argument of Section 20.3.

## 20.2. Information Maximization and Histogram Equalization

### 20.2.1. Laughlin's Interneurons

Which response function transmits the most information? Consider a noiseless neuron whose response is a monotonic function $r = g(c)$ of a stimulus variable $c$ (contrast, say) and is limited to $[0, r_{\max}]$. The limited response range is the constraint: a neuron cannot fire at an arbitrarily high rate, and, as in an analog-to-digital converter, the response levels should all be used.

**Definition 20.2.1 (Histogram Equalization)** The coding strategy that maps a stimulus variable through its own cumulative distribution function, so that all response levels are used equally often, is called **histogram equalization**.

**Theorem 20.2.1 (Optimality of Histogram Equalization)** Let $c$ have density $p(c)$ with cumulative distribution $F(c)$, and let $r = g(c)$ be increasing and differentiable with values in $[0, r_{\max}]$. The entropy of the response (a differential entropy, to a fixed resolution) is largest for $g(c) = r_{\max}F(c)$, for which the response is uniformly distributed on $[0, r_{\max}]$.

**Proof** The density of $r$ is $p_r(r) = p(c)/g'(c)$ at $r = g(c)$, so

$$
h(R) = -\int p_r\log_2 p_r\,\mathrm{d}r = h(C) + \int p(c)\log_2 g'(c)\,\mathrm{d}c .
$$
Only the last term depends on $g$, and $\int g'(c)\,\mathrm{d}c = r_{\max}$ is fixed. With $q(c) = g'(c)/r_{\max}$, a probability density,
$\int p\log_2 g' = \log_2 r_{\max} + \int p\log_2 q \le \log_2 r_{\max} + \int p\log_2 p$, with equality if and only if $q = p$ (Gibbs' inequality). Hence $g' = r_{\max}p$ and $g = r_{\max}F$. $\square$

The rule says that steep parts of the response function should lie where stimuli are frequent, and that the response is flat where they are rare. Laughlin (1981) tested it on the large monopolar cells of the blowfly compound eye, which respond to contrast with graded potentials. He measured the distribution of contrasts in the natural habitat of the fly with a photodetector, computed its cumulative distribution and compared it with the measured contrast–response curves of the cells. The two agreed closely, without free parameters apart from the response range. The result is an early demonstration that the response properties of a neuron reflect the statistics of its input.

Adaptation can be understood as the continual re-estimation of the distribution: when the stimulus distribution changes, the response function slides and rescales within a few hundred milliseconds in the fly motion-sensitive neuron H1 and in vertebrate ganglion cells (Brenner et al. 2000; Fairhall et al. 2001).

![Optimal coding under two constraints. A: Contrast distribution (a Laplacian of scale 0.25 truncated to $[-1, 1]$, a schematic of natural contrasts) and the response function $r_{\max}F(c)$ of Theorem 20.2.1 against a linear response. B: Histograms of the response in 10 levels for the two codes: the cumulative-distribution code uses all levels equally and attains the maximal entropy $\log_2 10 = 3.32$ bits, the linear code only 2.67 bits. C: Bits transmitted per unit of energy for a binary neuron that spikes in a bin with probability $p$ (Levy and Baxter 1996; Section 20.6), for three ratios $b$ of the cost of a resting bin to the cost of a spike; the optimum (dots) moves to sparse firing as spikes become expensive relative to rest](./plots/histogram-equalization.py)

With noise the optimum changes: levels with a large noise are less informative, and the optimal response function becomes flatter where the noise is large. In the limit of high noise, information is maximized by a steep step at the median, a binary neuron; with little noise it approaches the equalization of Theorem 20.2.1.

## 20.3. Redundancy Reduction and Whitening

### 20.3.1. Natural Images Are Redundant

Barlow's second principle was that neighboring neurons should not transmit the same information. In natural images, neighboring pixels are strongly correlated: the power spectrum of an ensemble of natural images falls with spatial frequency $k$ as $Q_{ss}(k) \propto 1/k^2$ (scale invariance). Transmitting the intensities of the pixels one by one, as a receptor array does, would send the same information many times.

**Definition 20.3.1 (Whitening)** A linear filter with a transfer function $D(k)$ is a **whitening** filter for an ensemble with power spectrum $Q_{ss}(k)$ if its output has a flat spectrum, $\lvert D(k)\rvert^2Q_{ss}(k) = \text{const}$, that is, $\lvert D(k)\rvert \propto Q_{ss}(k)^{-1/2}$.

The outputs of a whitening filter are uncorrelated, so that no neuron repeats what another one says. With $Q_{ss} \propto 1/k^2$, a whitening filter has $\lvert D(k)\rvert \propto k$: it amplifies high spatial frequencies. Its receptive field in space is therefore a center–surround structure, with an excitatory peak and an inhibitory surround that makes the weights sum to approximately zero, as for the difference-of-Gaussians model ([7.16.17](/7.16.17#sec-17.5)).

### 20.3.2. Whitening in Noise

Unlimited amplification of high frequencies cannot be right: at high spatial frequencies the image is weak and sensor noise dominates, and boosting it would waste the capacity of the optic nerve on noise. Atick and Redlich (1990, 1992) combined whitening with noise filtering. Let the input be signal plus white noise with $Q_{\eta\eta}(k) = N$. The optimal noise filter, the **Wiener filter**, is $Q_{ss}/(Q_{ss} + Q_{\eta\eta})$, and whitening is applied to the noisy input, whose spectrum is $Q_{ss} + Q_{\eta\eta}$. The product is

$$
\lvert D(k)\rvert \propto \frac{Q_{ss}(k)}{\bigl(Q_{ss}(k) + Q_{\eta\eta}(k)\bigr)^{3/2}} . \tag{20.2}
$$

For $Q_{ss} \gg Q_{\eta\eta}$ (low frequencies, bright light) this is $Q_{ss}^{-1/2}$, the whitening filter. For $Q_{ss} \ll Q_{\eta\eta}$ (high frequencies, dim light) it is proportional to $Q_{ss}$ and falls with $k$. The filter is therefore band-pass, and its peak moves to lower spatial frequencies as the signal-to-noise ratio decreases: in dim light the optimal filter becomes a low-pass filter, a center without surround that averages over a wide area.

![Optimal retinal filter for natural images in noise, Eq. (20.2), for signal spectrum $A/k^2$ and white noise of power $N$. A: the filter gain against spatial frequency for $A/N = 10^4$, $10^2$ and $1$ (bright to dim light), each normalized to its maximum: the band-pass filter shifts to low frequencies as the signal-to-noise ratio decreases. B: the radial profile of the receptive field (the two-dimensional inverse Fourier transform of the filter), in units of the inverse frequency: the narrow center and the inhibitory surround at high signal-to-noise ratio fade to a broad, purely excitatory center in dim light](./plots/whitening-filter.py)

The prediction matches the physiology: with dark adaptation the inhibitory surround of retinal ganglion cells weakens and the center widens (Barlow, Fitzhugh and Kuffler 1957), so that the cell becomes a spatial integrator at low light levels where photons are scarce. An analogous argument for the temporal domain predicts the biphasic temporal receptive fields of ganglion cells and LGN neurons (Dong and Atick 1995). The theory is nevertheless a prediction of an average filter, not of the retinal cell types or their mosaic (Section 20.7).

## 20.4. Information in Spike Trains

### 20.4.1. The Direct Method

Information measures have the advantage of requiring no assumption about which feature of the **spike train** carries information. Their cost is the need to estimate probabilities of spike patterns. A spike train, binned with resolution $\Delta t$ small enough for at most one spike per bin, is a string of zeros and ones. A block of $L$ bins (a word of duration $T_s = L\Delta t$) has $2^L$ possible values, and the entropy rate of the train is estimated from the distribution $P[B]$ of words $B$ found in the data (Strong, Koberle, de Ruyter van Steveninck and Bialek 1998):

$$
\dot H(T_s) = -\frac{1}{T_s}\sum_B P[B]\log_2 P[B] , \tag{20.3}
$$
which is an upper bound on the true entropy rate that converges for $T_s \to \infty$ if correlations are finite-ranged. The noise entropy is obtained from repetitions of an identical stimulus: for each time $t$ in the stimulus the distribution of words $P[B \mid t]$ over trials gives $H_{\text{noise}} = \langle -\sum_B P[B \mid t]\log_2 P[B \mid t]\rangle_t / T_s$. The information rate is the difference, $\dot I = \dot H - \dot H_{\text{noise}}$, per second or per spike.

**Example 20.4.1 (Poisson Spike Trains)** For a homogeneous Poisson train of rate $r$ the intervals are independent and exponential ([7.16.16](/7.16.16#sec-16.4)), and (20.3) gives, with $\Delta t \ll 1/r$,

$$
\dot H = \frac{r}{\ln 2}\bigl(1 - \ln(r\Delta t)\bigr) \ \text{bits/s}.
$$
For $r = 50\,\mathrm{Hz}$ and $\Delta t = 3\,\mathrm{ms}$ this is about $209\,\mathrm{bits\,s^{-1}}$, or $4.2$ bits per spike (the exact binary entropy $h(0.15)/\Delta t$ gives $203\,\mathrm{bits\,s^{-1}}$). The entropy is higher for faster rates and for a finer resolution, since it counts all patterns the train could have.

For the fly motion-sensitive neuron H1, driven by a time-varying motion stimulus, Strong et al. (1998) found $157\,\mathrm{bits\,s^{-1}}$ of entropy and $79\,\mathrm{bits\,s^{-1}}$ of noise entropy for $\Delta t = 3\,\mathrm{ms}$, an information rate of $78\,\mathrm{bits\,s^{-1}}$, or $1.8$ bits per spike. Values of 1–3 bits per spike are typical of such experiments, and the rates in sensory neurons at the periphery are among the highest, tens to hundreds of $\mathrm{bits\,s^{-1}}$ for single neurons. Such rates are attainable only if spike times are reliable to a few milliseconds, which is part of the evidence that spike timing carries information in these neurons ([7.16.16](/7.16.16#sec-16.7)).

### 20.4.2. Bias

Plug-in estimates of entropy from a finite sample are biased downward: unobserved words are counted as impossible. For $N$ words and $K$ observed distinct values, the leading correction is the Miller–Madow term, $+ (K-1)/(2N\ln 2)$ bits. The bias is linear in $1/N$ when $N$ is much larger than the number of words that carry non-negligible probability, so that extrapolating the estimate to $1/N \to 0$ removes it. When the word length is increased, the number of probable words grows as $2^{L\,h}$, with $h$ the entropy per bin, until the data are undersampled, and then no correction works: the estimate falls off with $L$. In practice $T_s$ is increased until the data run out, and the entropy per word is extrapolated from the intermediate range in which the extrapolation in $1/T_s$ and $1/N$ is still valid (Strong et al. 1998).

![Bias of the direct method. Words of $L$ bins are read from simulated independent bins with spike probability 0.2 (a 100 Hz Poisson train in 2 ms bins), whose true entropy per bin is $h(0.2) = 0.722$ bits (dotted). A: entropy per bin estimated from $N = 2000$ words against $L$ by the plug-in estimate, the Miller–Madow correction and the extrapolation in $1/N$: all agree with the true value up to $L \approx 8$, where $2^{0.72L}$ is well below $N$; beyond $L \approx 12$ the data are undersampled and the estimates fall, the correction only postponing the failure. B: estimates for $L = 16$ against $1/N$, from $N = 250$ to $16\,000$: even for $N = 16\,000$ the plug-in estimate is 6 % too low, and the dependence is not yet linear in $1/N$, so that the extrapolation cannot be trusted](./plots/entropy-bias.py)

The method has an alternative that needs fewer data when the stimulus has a Gaussian distribution. A decoder reconstructs the stimulus from the spike train by linear filtering, and the information is bounded from below by the spectrum of the reconstruction error: $I \ge \int\log_2(Q_{ss}/Q_{\text{err}})\,\mathrm{d}f$ (Bialek and Rieke). The bound is often within a factor of two of the direct estimate and is a measure of how much of the information is in a linearly decodable form (decoding is the subject of [7.16.26](/7.16.26)).

## 20.5. Sparse Coding

### 20.5.1. The Model

Whitening decorrelates responses but leaves higher-order redundancy. The statistics of natural images are not Gaussian: images consist of objects with edges, and a patch contains a few edges in the middle of a uniform background. An efficient code for such images should represent each patch by a few active elements chosen from a large dictionary of features.

**Definition 20.5.1 (Sparse Coding)** In a **sparse coding** model an image patch $\boldsymbol{x}$ is a linear combination of basis functions (the columns $\boldsymbol{\varphi}_i$ of a matrix $\Phi$), plus noise, with coefficients $a_i$ that are mostly zero:

$$
\boldsymbol{x} = \Phi\boldsymbol{a} + \boldsymbol{\nu}, \qquad \hat{\boldsymbol{a}}(\boldsymbol{x}) = \arg\min_{\boldsymbol{a}}\Bigl[\tfrac12\lVert\boldsymbol{x} - \Phi\boldsymbol{a}\rVert^2 + \lambda\sum_i\lvert a_i\rvert\Bigr]. \tag{20.4}
$$
The basis $\Phi$ is learned from the images by minimizing the same cost, averaged over patches, with the columns of $\Phi$ kept at unit length.

The cost is the negative log posterior of a Gaussian likelihood with a Laplace prior $p(a_i) \propto \mathrm{e}^{-\lambda\lvert a_i\rvert/\sigma^2}$, a heavy-tailed distribution that favors few large coefficients. The inference step is a convex problem (the **Lasso**), solved by the iterative shrinkage–thresholding algorithm
$\boldsymbol{a} \leftarrow \mathcal{S}_{\lambda/L}\bigl(\boldsymbol{a} + \Phi^{\mathsf T}(\boldsymbol{x} - \Phi\boldsymbol{a})/L\bigr)$, where $\mathcal{S}_\theta(z) = \operatorname{sgn}(z)\max(\lvert z\rvert - \theta, 0)$ and $L$ is the largest eigenvalue of $\Phi^{\mathsf T}\Phi$. The learning rule is a Hebbian one: $\Delta\Phi = \eta(\boldsymbol{x} - \Phi\boldsymbol{a})\boldsymbol{a}^{\mathsf T}$, the product of the residual (the prediction error) and the activity. The inference step can be implemented by a recurrent network in which neurons with overlapping receptive fields inhibit one another (Rozell et al. 2008), which gives a candidate for the computation of V1 by competition.

### 20.5.2. Gabor-Like Bases

Olshausen and Field (1996) trained this model on whitened patches of natural images and obtained basis functions that were localized in space, oriented and band-pass, like simple-cell receptive fields ([7.16.18](/7.16.18#sec-18.2)), without any assumption of these properties. **Independent component analysis**, which maximizes the statistical independence of the outputs instead of the sparsity, gives very similar filters (Bell and Sejnowski 1997; van Hateren and van der Schaaf 1998), and the distribution of the shapes of the learned filters resembles that recorded in macaque V1. The result is the best-known example of a receptive field derived from an optimization principle and a natural stimulus ensemble.

![Sparse coding of image patches (Eq. 20.4) on synthetic images. Thirty images of $128 \times 128$ pixels are made of 300 overlapping opaque discs and ellipses of random size, orientation and grey level (a "dead leaves" model that yields edges and an approximately $1/k^2$ spectrum), whitened and normalized. A: 64 basis functions learned from $8 \times 8$ patches (1800 batches of 100 patches; $\lambda = 0.4$): most are localized and oriented edge or bar detectors at different positions, orientations and phases, and a few represent the mean luminance. B: the distribution of coefficients, on a logarithmic axis, for the sparse code (80 % of the coefficients exactly zero) and for the projections of the same patches on the principal components (also sparse-looking, with a smaller peak at zero and heavier tails relative to the sparse code at intermediate values)](./plots/sparse-coding.py)

A caveat: the learned bases of such models depend on the choice of patch size, whitening and the number of basis functions, and in the overcomplete case ($M > N$) the code is no longer a rotation of the input. With more basis functions than pixels, the model is closer to V1, which has about two orders of magnitude more neurons than the retinal ganglion cells that supply it.

## 20.6. Energy Constraints and Sparse Firing

Sparse codes are also cheap codes. Neural signaling is expensive ([7.14.46](/7.14.46#sec-46.7)): in gray matter more than half of the energy used goes to restoring ion gradients after postsynaptic currents and action potentials, and a spike costs of the order of $10^8$–$10^9$ ATP molecules, counting the synaptic currents it causes (Attwell and Laughlin 2001; Lennie 2003). Lennie (2003) estimated that, on this budget, no more than about 1 % of cortical neurons can be strongly active at once. An efficient code maximizes information per unit energy and not only information.

**Formula 20.6.1 (Information Per Unit of Energy for a Binary Neuron)** A neuron fires a spike in a time bin with probability $p$. It transmits at most the entropy of its response, $h(p) = -p\log_2p - (1-p)\log_2(1-p)$ bits per bin, and uses energy $\propto b + p$ per bin, in units of the cost of a spike, where $b$ is the cost of the resting bin (maintenance of the resting potential, housekeeping). The efficiency is

$$
\frac{h(p)}{b + p} .
$$
It is maximal at $p^* = 0.38$ for $b = 1$, $0.16$ for $b = 0.1$ and $0.033$ for $b = 0.01$ (Levy and Baxter 1996, as in panel C of the figure above).

When resting costs dominate ($b \gg 1$), it pays to use the neuron as often as possible and $p^*$ tends to $\tfrac12$, the maximum of $h$; when spikes are expensive relative to rest, the optimum is a sparse code with few spikes, and the bits per energy are higher as well (the maximum rises from $0.69$ to $4.9$ bits per unit for $b = 1$ and $b = 0.01$). **Firing rates** of cortical neurons of about $1\,\mathrm{s^{-1}}$ ($p \approx 0.002$–$0.005$ for 2–5 ms bins) and the sparse responses to natural scenes in V1 and in the song-control nucleus of the zebra finch are consistent with this picture. Combining the constraints: sparsity both reduces redundancy and saves energy, and a code that is sparse in this sense does not need to be dense in neurons, since the number of neurons is large but the number that are active is small.

## 20.7. Testing the Efficient Coding Hypothesis, and Its Limits

The hypothesis has been tested in the following ways, with results of different strength.

| Prediction | Test | Result |
|---|---|---|
| Response function equals the cumulative distribution of the stimulus | Fly monopolar cells (Laughlin 1981); adaptation of H1 and ganglion cells to the variance of the stimulus | Quantitative agreement without free parameters; adaptation time scales of $10^2$–$10^3$ ms |
| Retinal filters whiten natural images in noise | Surround strength against light level; spatial and temporal filters of ganglion cells | Qualitative agreement; surround weakens in dim light |
| V1 receptive fields come from sparse or independent components of natural images | Comparison of learned and measured simple-cell shapes (aspect ratio and size of lobes) | Good qualitative agreement, but measured fields have fewer subregions and are more often blob-like than the learned bases (Ringach 2002) |
| Auditory nerve filters are efficient codes of natural sounds | Sparse, time-shift-invariant kernels learned from speech and environmental sounds (Smith and Lewicki 2006) | Reproduces the shapes and the frequency dependence of the cochlear filters |
| Codes are cheap | Firing rates and ATP budget | Mean rates of $\lesssim 1\,\mathrm{s^{-1}}$ in cortex; costs of spikes and synapses are of the right order |

The limits are as important.

- *Relevance.* The hypothesis does not say which information matters. The brain does not need to reproduce the image: it needs to guide behavior. The information bottleneck formulation asks for a representation that keeps as much information as possible about a relevant variable while compressing the input (Tishby, Pereira and Bialek 1999; Chalk, Marre and Tkačik 2018), which gives different predictions. The many ganglion cell types of the retina ([7.16.17](/7.16.17#sec-17.7)) cannot be derived from the linear whitening of a single channel; nonlinear efficient-coding models with several cell populations recover the split into ON and OFF cells (Karklin and Simoncelli 2011), but not yet the full diversity of types, many of which serve specific behaviors.
- *Assumptions.* The predictions depend on the assumed image statistics (which ensemble, at which scale, and whether motion and the eye movements are included) and on the assumed constraint (the number of cells, the noise, or the energy), and several formulations explain the same data.
- *Feedforward and stationary.* The theory concerns the feedforward encoding of a stationary ensemble, while in the cortex feedback and top-down influences are as numerous as feedforward connections ([7.16.18](/7.16.18#sec-18.4)), and the representation changes with attention and task.
- *Readout.* An efficient code is not necessarily a code that can be read out easily: the downstream circuit pays for the decoding as well.

In later chapters, predictive coding ([7.16.48](/7.16.48)) will extend the idea by asking the code to transmit only what the cortex could not predict from its own model.

## Summary

| Topic | Key relation |
|---|---|
| Information (Definition 20.1.1) | $I(S;R) = H(R) - H(R \mid S)$, Eq. (20.1); Poisson noise limits a neuron to about $\tfrac12\log_2\lambda_{\max}$ bits, Example 20.1.1; Gaussian channel $\tfrac12\log_2(1 + \mathrm{SNR})$, Theorem 20.1.1 |
| Histogram equalization (Definition 20.2.1, Theorem 20.2.1) | With a bounded response, the entropy is maximal for $r = r_{\max}F(c)$; Laughlin's fly interneurons follow the cumulative contrast distribution |
| Whitening (Definition 20.3.1, Eq. (20.2)) | Natural images have $Q_{ss} \propto 1/k^2$, the whitening filter has $\lvert D\rvert \propto k$; with noise the filter is $Q_{ss}/(Q_{ss} + Q_{\eta\eta})^{3/2}$, band-pass in bright light and low-pass in dim light |
| Spike-train information (Eq. (20.3), Example 20.4.1) | Entropy rate of words; Poisson train $\dot H = r(1 - \ln r\Delta t)/\ln 2$; fly H1 $78\,\mathrm{bits\,s^{-1}}$, 1.8 bits per spike; plug-in estimates are biased downward when data are limited |
| Sparse coding (Definition 20.5.1, Eq. (20.4)) | $\min\tfrac12\lVert\boldsymbol{x} - \Phi\boldsymbol{a}\rVert^2 + \lambda\lVert\boldsymbol{a}\rVert_1$, Hebbian learning of $\Phi$; yields localized, oriented, band-pass bases like V1 **simple cells** |
| Energy (Formula 20.6.1) | Bits per unit energy $h(p)/(b + p)$ is maximal at small $p$ when spikes are expensive relative to rest |
| Limits | The hypothesis ignores which information is relevant, depends on the assumed ensemble and constraint, and concerns the feedforward stage |

## Questions

1. A neuron has a response $R \in \{0, 1\}$ with $\mathbb{P}(R = 1 \mid S = s_1) = 0.9$ and $\mathbb{P}(R = 1 \mid S = s_2) = 0.1$, and the two stimuli are equally likely. Compute $I(S;R)$.

   **Answer** The marginal is $\mathbb{P}(R = 1) = 0.5$, so $H(R) = 1$ bit. The noise entropy is $h(0.9) = h(0.1) = -0.9\log_20.9 - 0.1\log_20.1 \approx 0.469$ bits for both stimuli. Hence $I = 1 - 0.469 = 0.531$ bits, about half a bit although the neuron is "90 % reliable".

2. Compute the optimal response function of Theorem 20.2.1 for contrasts with the Laplace density $p(c) = \tfrac{1}{2b}\mathrm{e}^{-\lvert c\rvert/b}$ on the real line, and the contrast at which the response is $r_{\max}/2$ and the contrast at which it is $0.9r_{\max}$.

   **Answer** $F(c) = \tfrac12\mathrm{e}^{c/b}$ for $c \le 0$ and $1 - \tfrac12\mathrm{e}^{-c/b}$ for $c \ge 0$, so $r = r_{\max}F(c)$. The half-maximal response is at $c = 0$, the median. $F(c) = 0.9$ gives $\tfrac12\mathrm{e}^{-c/b} = 0.1$, $c = b\ln 5 \approx 1.61\,b$. Contrasts within $\pm 1.6b$ use 80 % of the response range, so that the response saturates at about twice the typical contrast scale.

3. Show that the whitening filter for a one-dimensional signal with the spectrum $Q_{ss}(k) \propto k^{-2}$ followed by a low-pass noise filter of Eq. (20.2) has its maximum at $k^* = \sqrt{A/(2N)}$ when $Q_{ss} = A/k^2$ and $Q_{\eta\eta} = N$. What happens to $k^*$ if the light intensity falls by a factor of 100, assuming that $A$ is proportional to intensity and $N$ is constant?

   **Answer** With $Q_{ss} = A/k^2$, $\lvert D\rvert = (A/k^2)/(A/k^2 + N)^{3/2} = A k/(A + Nk^2)^{3/2}$. Setting $\mathrm{d}\ln\lvert D\rvert/\mathrm{d}k = 1/k - 3Nk/(A + Nk^2) = 0$ gives $A + Nk^2 = 3Nk^2$, $k^* = \sqrt{A/(2N)}$. A hundredfold decrease of $A$ lowers $k^*$ by a factor of 10: the optimal filter is tuned to ten times larger structures, and its receptive field center is about ten times wider.

4. In a direct-method experiment, a neuron fires at 20 Hz and the spike train is binned at $\Delta t = 4\,\mathrm{ms}$. Estimate the entropy rate if the spikes were Poisson, and say why an experimenter who collects 5 minutes of data cannot use words much longer than about 30 bins without correction.

   **Answer** $r\Delta t = 0.08$, so $\dot H = (20/\ln 2)(1 - \ln 0.08) = 28.9\times3.53 \approx 102\,\mathrm{bits\,s^{-1}}$, or $5.1$ bits per spike. In 5 minutes there are $75\,000$ bins, so at most $75\,000$ words of any length. The entropy per bin is $h(0.08) \approx 0.40$ bits, so that a word of $L$ bins has about $2^{0.4L}$ probable values: $2^{12} \approx 4000$ for $L = 30$ and $2^{16} \approx 65\,000$ for $L = 40$. The latter is comparable with the number of words available, so that undersampling becomes severe somewhere between $L = 30$ and $L = 40$, and for words longer than about 30 bins (120 ms) the plug-in estimate must be corrected or the extrapolation of Section 20.4.2 used. For a stimulus-driven train, whose entropy per bin is higher and for which the noise entropy needs many repeats of the same stimulus, the usable length is shorter.

5. (Open question) A student proposes to test the efficient coding hypothesis for the auditory system by learning a sparse code of recorded speech and comparing the basis functions with auditory nerve filters. Which choices of the model will influence the outcome, and what other test could separate efficient coding from alternatives?

   **Answer** The result depends on the corpus (speech only, environmental sounds, or both), on preprocessing (whitening, the range of frequencies), on the number of basis functions and on the sparsity penalty $\lambda$; on the representation (waveform or spectrogram; with waveform and a time-shift-invariant dictionary the learned kernels resemble gammatone cochlear filters). A second test: the model predicts the changes of the code with the statistics of the stimulus, for instance in animals raised in a different acoustic environment, or for species with different vocalizations, and adaptation to altered statistics within a short time. If only the same kernels emerge for every sound ensemble, the hypothesis has no explanatory content; if the kernels depend on the ensemble in the predicted way, it has.
