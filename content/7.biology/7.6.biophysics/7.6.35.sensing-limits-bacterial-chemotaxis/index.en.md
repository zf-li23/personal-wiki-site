---
title: Physical Limits of Sensing and Bacterial Chemotaxis
description: "How precisely a cell can measure its chemical environment and how a swimming bacterium uses that measurement: counting molecules and the Berg–Purcell limit, receptor patches, binding kinetics and maximum-likelihood sensing, temporal and spatial gradient sensing, mutual information and channel capacity; run-and-tumble motility and chemotactic drift, the chemotaxis network, MWC receptor clusters, the ultrasensitive motor, zero-order and nonequilibrium amplification, Barkai–Leibler adaptation as integral feedback, the Weber–Fechner law and fold-change detection, the search for adaptive circuit topologies, and signaling proteins on a leash."
---

A cell lives by measuring its surroundings: the concentration of a sugar, a hormone, a pheromone, the direction of a gradient. Each measurement is made by a few thousand receptors that bind molecules arriving by diffusion, one at a time and at random. The precision of such a measurement is limited by physics before any biochemistry is considered, just as the precision of a photon counter is limited by the Poisson statistics of photons. This chapter derives those limits and then studies in detail the one sensory system that has been understood quantitatively from receptor to behavior, the chemotaxis of *Escherichia coli*. We count molecules arriving at an absorbing cell and at receptor patches, add binding kinetics and ask what the best estimator can achieve (35.1), apply the results to the sensing of gradients (35.2) and translate them into the language of information theory (35.3). The second half follows the bacterium: how runs and tumbles produce a biased **random walk** (35.4), how a cluster of receptors and a switch-like motor amplify tiny changes (35.5), how methylation of the receptors resets their sensitivity exactly whatever the background (35.6), which circuit architectures can achieve this in general (35.7), and how tethering shapes the response of signaling proteins (35.8).

The chapter rests on several others. Diffusion to an absorbing sphere was derived in [7.6.5](/7.6.5#sec-5.2.3) and the statistical mechanics of the **MWC model** in [7.6.4](/7.6.4#sec-4.5); the swimming of bacteria at low Reynolds number and the rotary flagellar motor are treated in [7.6.22](/7.6.22#sec-22.5) and [7.6.28](/7.6.28), stochastic kinetics in [7.6.32](/7.6.32). The cell biology of signaling, **adaptation** and the circuits that achieve it is in [7.3.18](/7.3.18#sec-18.4.4), the polarity and gradient sensing of crawling cells in [7.3.15](/7.3.15#sec-15.5.5), the **two-component system** of bacteria in [7.1.15](/7.1.15), and the precision of **positional information** read from **morphogen** gradients in [7.5.11](/7.5.11). Entropy and conditional entropy in the sense of information theory are introduced in [4.5.6](/4.5.6), maximum-likelihood estimation and the Fisher information in [3.2.3](/3.2.3). The present chapter treats the physical limits and the mechanism of one system; integral feedback, feed-forward loops and robustness as general design principles of networks belong to [systems biology](/7.9), and the energetic cost of adaptation and amplification is treated systematically in [7.6.38](/7.6.38).

## 35.1. Counting Molecules

### 35.1.1. The Perfect Absorber

A sensor should have four properties: low noise (a good signal-to-noise ratio), high gain (a large response to a small change of the stimulus), a wide dynamic range (it should respond to changes rather than to absolute levels), and robustness (good performance despite variations of its own components). The first is limited most directly by physics. Consider a cell of radius $a$ in a medium in which a ligand has concentration $c$ and **diffusion coefficient** $D$, and suppose the cell's goal is to estimate $c$ during a time $T$.

The simplest sensor is a cell whose whole surface absorbs every molecule that reaches it and counts it. By Formula 5.2.3 of [7.6.5](/7.6.5#fml-5.2.3) the mean flux to a perfectly absorbing sphere is $J = 4\pi Dac$. Molecules arrive independently, so the number $n$ caught in time $T$ is a Poisson process with mean $\bar n = 4\pi DacT$ ([7.6.32](/7.6.32#sec-32.1.2)).

**Theorem 35.1.1 (Precision of a Perfect Absorber)** A sphere of radius $a$ that absorbs and counts all molecules arriving by diffusion during a time $T$, and estimates the concentration as $\hat c = n/(4\pi DaT)$, has relative error

$$
\frac{\delta c}{c} = \frac{1}{\sqrt{4\pi DacT}} .
\tag{35.1}
$$

**Proof** The count $n$ has the **Poisson distribution** with mean $\bar n = 4\pi DacT$, so $\operatorname{Var}(n) = \bar n$. The estimator is unbiased and $\operatorname{Var}(\hat c)/c^2 = \operatorname{Var}(n)/\bar n^2 = 1/\bar n$. $\square$

The error decreases with the square root of everything the cell can control: its size, the averaging time, and the concentration. Berg and Purcell (1977) obtained Eq. (35.1) up to a numerical factor by a different route, counting the molecules present in the volume of the cell and the number of independent such counts during $T$: the volume holds $c a^3$ molecules, which are replaced by diffusion every $a^2/D$, giving $T D/a^2$ independent samples and $(\delta c/c)^2 \sim 1/(ca^3 \cdot TD/a^2) = 1/(DacT)$. Both arguments show that what matters is the number of molecules the cell can see, and that a sensor of size $a$ effectively samples a volume $DaT$ during a time $T$. The relation $\delta c/c \sim (DacT)^{-1/2}$ is called the *Berg–Purcell limit*.

**Example 35.1.1** For *E. coli* ($a \approx 1\,\mu\mathrm{m}$) sensing an amino acid ($D \approx 10^3\,\mu\mathrm{m^2\,s^{-1}}$) at $c = 1\,\mu\mathrm{M} = 600\,\mu\mathrm{m^{-3}}$, the flux is $4\pi \times 10^3 \times 1 \times 600 \approx 7.5\times10^6$ molecules per second, and in $T = 1\,\mathrm{s}$ the relative error is $1/\sqrt{7.5\times10^6} \approx 4\times10^{-4}$. At $1\,\mathrm{nM}$ it is $1.2\,\%$. A bacterium can in principle measure concentrations very precisely; the question is whether its receptors come close to this ideal.

### 35.1.2. Receptor Patches

A real cell does not absorb ligands over its whole surface but only at receptors, each a binding site of size $s \approx 1\,\mathrm{nm}$. How many are needed? The answer, surprisingly, is very few.

**Formula 35.1.1 (Flux to a Sphere with Absorbing Patches)** A sphere of radius $a$ covered by $N$ well-separated absorbing disks of radius $s \ll a$, the rest of its surface reflecting, receives the flux

$$
J = 4\pi Dac\,\frac{Ns}{Ns + \pi a} .
\tag{35.2}
$$
The flux is half of that of a perfect absorber when $N = \pi a/s$.

**Proof** The steady diffusion problem is the electrostatic problem of conductors at zero potential in a medium held at potential $c$ at infinity: the flux is $D$ times the capacitance of the absorber (in units where a sphere has capacitance $4\pi a$). Molecules must first diffuse from infinity to the vicinity of the cell, through an effective "resistance" $1/(4\pi Da)$, and then find one of the disks, through the parallel resistances $1/(4Ds)$ of the $N$ disks ([7.6.5](/7.6.5#fml-5.2.3) gives $J = 4Dsc$ for one disk on a plane). In series,

$$
J = \frac{c}{\dfrac{1}{4\pi Da} + \dfrac{1}{4DsN}} = 4\pi Dac\,\frac{4DsN}{4DsN + 4\pi Da} ,
$$
which is Eq. (35.2). The series form is exact in the limit of many small, uniformly spaced disks and good to a few percent otherwise (Berg and Purcell, 1977; Zwanzig, 1990). $\square$

**Example 35.1.2** With $a = 1\,\mu\mathrm{m}$ and $s = 1\,\mathrm{nm}$, half the maximal flux needs $N = \pi a/s \approx 3100$ receptors, which cover a fraction $N\pi s^2/(4\pi a^2) = Ns^2/4a^2 \approx 0.08\,\%$ of the surface (panel A of the figure). A sum of independent disks would predict half-saturation at $N = \pi a/2s$; the true number is twice as large, because the disks compete for molecules from the same depleted region near the cell. Even so, a sparse array of receptors is nearly as good as a perfectly absorbing cell, and the surface has room for hundreds of receptor types, each catching nearly all the molecules of its ligand that come by. For a large eukaryotic cell ($a = 10\,\mu\mathrm{m}$, ligand $D = 100\,\mu\mathrm{m^2\,s^{-1}}$) and receptors with an association rate constant $k_{\mathrm{on}} = 10\,\mu\mathrm{M^{-1}\,s^{-1}} = 1.7\times10^{-2}\,\mu\mathrm{m^3\,s^{-1}}$, the analogous condition for half-maximal uptake, $Nk_{\mathrm{on}} = 4\pi Da$, gives $N \approx 1.3\times10^4/1.7\times10^{-2} \approx 7.5\times10^5$ receptors, spaced about $40\,\mathrm{nm}$ apart and covering well under $1\,\%$ of the membrane.

A uniform distribution is not what *E. coli* does: its chemoreceptors are packed into dense hexagonal arrays at the poles (35.5.2). For catching molecules the clustering is slightly wasteful; its purpose is cooperativity, which amplifies the response.

### 35.1.3. Receptors with Binding Kinetics

A receptor does not consume its ligand; it binds and releases it. Let a receptor switch between the free state and the bound state with rates $k_+c$ and $k_-$. Its occupancy $n(t) \in \{0, 1\}$ is a two-state Markov process (a **two-state system**, [7.6.4](/7.6.4)), the mean occupancy is $p = c/(c + K_{\mathrm{D}})$ with $K_{\mathrm{D}} = k_-/k_+$, and the cell can estimate $c = K_{\mathrm{D}}p/(1 - p)$ from the time average $\bar n_T = T^{-1}\int_0^Tn(t)\,\mathrm{d}t$.

**Theorem 35.1.2 (Time-Averaging Receptor)** For $T$ much longer than the correlation time $\tau_{\mathrm{c}} = 1/(k_+c + k_-)$ of the occupancy, the time-averaged occupancy has variance $\operatorname{Var}(\bar n_T) = 2p(1 - p)\tau_{\mathrm{c}}/T$, and the concentration inferred from it has relative error

$$
\left(\frac{\delta c}{c}\right)^2 = \frac{2}{k_+c(1 - p)T} .
\tag{35.3}
$$

**Proof** The occupancy relaxes to its mean exponentially with rate $k_+c + k_-$, so its stationary autocorrelation is $\langle\delta n(t)\delta n(t')\rangle = p(1 - p)\mathrm{e}^{-\lvert t - t'\rvert/\tau_{\mathrm{c}}}$, $p(1 - p)$ being the variance of a Bernoulli variable. Then

$$
\operatorname{Var}(\bar n_T) = \frac{1}{T^2}\int_0^T\!\!\int_0^T p(1 - p)\mathrm{e}^{-\lvert t - t'\rvert/\tau_{\mathrm{c}}}\,\mathrm{d}t\,\mathrm{d}t' \approx \frac{2p(1 - p)\tau_{\mathrm{c}}}{T}
$$
for $T \gg \tau_{\mathrm{c}}$. Propagating the error through $c = K_{\mathrm{D}}p/(1 - p)$, $\mathrm{d}c/c = \mathrm{d}p/[p(1 - p)]$, so $(\delta c/c)^2 = 2\tau_{\mathrm{c}}/[Tp(1 - p)]$. Detailed balance, $k_+c(1 - p) = k_-p$, gives $k_+c + k_- = k_+c/p$, hence $\tau_{\mathrm{c}} = p/(k_+c)$, and Eq. (35.3) follows. $\square$

The factor $1 - p$ expresses that a receptor learns about the concentration only while it is free and waiting: a receptor that is almost always occupied ($c \gg K_{\mathrm{D}}$) is saturated and nearly blind. The number $k_+c(1 - p)T$ is the expected number of binding events in time $T$, so Eq. (35.3) says that each binding event is worth half a Poisson count. If binding is limited by diffusion, $k_+ = 4Ds$ for a disk of radius $s$, and $(\delta c/c)^2 = 1/[2Dsc(1 - p)T]$, the Berg–Purcell form with the receptor's own size in place of the cell's.

Two refinements matter. First, a molecule that has just been released is likely to rebind the same receptor, so successive binding events are not independent; a careful treatment of diffusion around a single receptor (Bialek and Setayeshgar, 2005; Kaizu and colleagues, 2014) shows that even with infinitely fast binding kinetics the error cannot fall below a term of order $1/(\pi DscT)$: a receptor cannot do better than counting the molecules diffusing through a volume of its own size. Second, the time average is not the best use of the record, which is the subject of the next section.

### 35.1.4. Maximum-Likelihood Sensing

The record of a receptor is the sequence of its bound and free intervals. Bound intervals have the exponential distribution with rate $k_-$, which does not depend on $c$: they carry no information about the concentration and only add noise to the time average. Free intervals have rate $k_+c$.

**Theorem 35.1.3 (Maximum-Likelihood Receptor)** Let a receptor be observed for a time $T$, during which it spends a total time $T_{\mathrm{f}}$ free and binds $n$ times. The **maximum likelihood estimation** of the concentration is $\hat c = n/(k_+T_{\mathrm{f}})$, and for large $n$ its relative error is

$$
\left(\frac{\delta c}{c}\right)^2 = \frac{1}{\bar n} = \frac{1}{k_+c(1 - p)T} ,
\tag{35.4}
$$
half the variance of the time-averaging estimate, Eq. (35.3).

**Proof** The probability density of the record is a product of exponential densities, $\prod_i k_+c\,\mathrm{e}^{-k_+c\tau_i^{\mathrm{f}}}\prod_jk_-\mathrm{e}^{-k_-\tau_j^{\mathrm{b}}}$ (up to boundary terms for the intervals cut by $0$ and $T$). Its logarithm depends on $c$ only through $n\ln c - k_+cT_{\mathrm{f}}$, which is maximal at $\hat c = n/(k_+T_{\mathrm{f}})$. The **Fisher information** about $\ln c$ is $-\partial^2_{\ln c}(n\ln c - k_+cT_{\mathrm{f}}) = k_+cT_{\mathrm{f}}$, whose expectation is $k_+c(1 - p)T = \bar n$; the variance of the maximum-likelihood estimator of $\ln c$ approaches the inverse of the Fisher information ([3.2.3](/3.2.3)). $\square$

The improvement by a factor of two, found by Endres and Wingreen (2009), is achieved by ignoring the durations of the bound intervals. The ideal absorber of Theorem 35.1.1 is better still, $(\delta c/c)^2 = 1/(k_+cT)$, because it never spends time bound; a receptor that internalizes and degrades its ligand comes close to it. Panel B of the figure compares the three estimators in simulated binding histories. Whether cells exploit the difference is not known; a downstream network that is activated by each binding event and decays slowly would compute something close to the maximum-likelihood estimate.

![Physical limits of concentration sensing. A: flux of ligand to a sphere of radius a = 1 µm carrying N absorbing disks of radius s = 1 nm, relative to a perfect absorber (Formula 35.1.1), and the naive sum of independent disks (dashed); half the maximal flux is reached at N = πa/s ≈ 3100 receptors covering 0.08 % of the surface. B: relative error of the concentration estimated by a single receptor (binding rate k₊c = 2 s⁻¹, unbinding rate 2 s⁻¹) against the averaging time, from 400 simulated binding histories per point: time averaging of the occupancy (Theorem 35.1.2), maximum likelihood from the free intervals (Theorem 35.1.3) and an ideal absorber that counts every arrival (Theorem 35.1.1); lines are the formulas. C: signal-to-noise ratio for detecting a 1 % difference in concentration between the two halves of a cell from a single snapshot of the occupancy of M receptors, against the background concentration (Formula 35.2.2): it is maximal at c = K_D, where M ≈ 4×10⁴ receptors reach a ratio of one](./plots/berg-purcell.py)

### 35.1.5. A Nucleus Reading a Morphogen

The same limits apply to a gene reading a transcription factor. In the early *Drosophila* embryo the anterior–posterior position of each nucleus is encoded by the concentration of the **morphogen** Bicoid, and the gene *hunchback* switches from on to off at mid-embryo, where neighboring nuclei differ in Bicoid concentration by about $10\,\%$ ([7.5.11](/7.5.11)). Measurements of Hunchback in many nuclei showed that its expression reflects the Bicoid concentration with an error of about $10\,\%$ (Gregor, Tank, Wieschaus and Bialek, 2007), so the readout is about as precise as it needs to be to distinguish neighbors. Is $10\,\%$ possible within the roughly $10\,\mathrm{min}$ of a nuclear cycle?

**Example 35.1.3** Treat one Bicoid binding site as a receptor of size $a \approx 3\,\mathrm{nm}$ (about $10\,\mathrm{bp}$), with diffusion-limited binding, $k_+c = 4\pi Dac$. With $D = 5\,\mu\mathrm{m^2\,s^{-1}}$ and $c = 8\,\mathrm{nM} = 4.8\,\mu\mathrm{m^{-3}}$ at mid-embryo, $k_+c = 4\pi \times 5 \times 0.003 \times 4.8 = 0.9\,\mathrm{s^{-1}}$. With $p = 1/2$ and $T = 600\,\mathrm{s}$, Eq. (35.3) gives $(\delta c/c)^2 = 2/(0.9 \times 0.5 \times 600) = 7.4\times10^{-3}$, an error of $9\,\%$; maximum likelihood would give $6\,\%$. The estimate is a lower bound, because binding is slower than diffusion-limited and transcription adds noise. It is also very sensitive to $D$: diffusion coefficients of Bicoid measured by photobleaching ($0.3\,\mu\mathrm{m^2\,s^{-1}}$) and by fluorescence correlation ($7\,\mu\mathrm{m^2\,s^{-1}}$) differ by a factor of twenty, and with the smaller value a single site would need hours ([7.5.11](/7.5.11) uses such parameters). The observed precision therefore suggests that nuclei pool information: several binding sites per enhancer, and averaging over neighboring nuclei, whose Hunchback levels are indeed correlated, reduce the error by the square root of the number of independent detectors.

Precision measurements in development thus tested a physical limit derived for bacteria, and the analysis has become a standard tool for deciding whether a biological readout is limited by molecule counting, by the downstream network, or by neither.

## 35.2. Sensing Gradients

### 35.2.1. Measuring in Time

A swimming bacterium has two ways to find the direction of a gradient. It can compare concentrations at its two ends at one moment, or it can compare concentrations at successive moments while it swims. The Berg–Purcell limit decides between them.

Let the attractant have gradient $g = \mathrm{d}c/\mathrm{d}x$ and the cell swim along it at speed $v$ for a time $T$, comparing the mean concentration over the first half of the run with that over the second. The difference of the means is $\Delta c = gvT/2$. By Eq. (35.1) each half-run measurement has variance $c/(4\pi DaT/2)$, so the difference has variance $c/(\pi DaT)$.

**Formula 35.2.1 (Shortest Useful Run)** A temporal comparison resolves the gradient when $(gvT/2)^2 > c/(\pi DaT)$, that is for runs longer than

$$
T_{\min} = \left(\frac{4c}{\pi Dav^2g^2}\right)^{1/3} .
\tag{35.5}
$$

**Example 35.2.1** For *E. coli* ($a = 1\,\mu\mathrm{m}$, $v = 20\,\mu\mathrm{m\,s^{-1}}$) in a gradient of an amino acid ($D = 10^3\,\mu\mathrm{m^2\,s^{-1}}$) at $c = 1\,\mu\mathrm{M}$ that changes e-fold over $L = c/g = 1\,\mathrm{mm}$, $g = 0.6\,\mu\mathrm{m^{-4}}$ and $T_{\min} = (4 \times 600/(\pi \times 10^3 \times 400 \times 0.36))^{1/3} = 0.17\,\mathrm{s}$; for $L = 10\,\mathrm{mm}$, $T_{\min} = 0.8\,\mathrm{s}$. A run cannot be much longer than a few seconds either: **rotational diffusion** ([7.6.5](/7.6.5#sec-5.3.2)) with $D_{\mathrm{r}} \approx 0.06\,\mathrm{rad^2\,s^{-1}}$ randomizes the direction of a bacterium in about $1/(2D_{\mathrm{r}}) \approx 8\,\mathrm{s}$, after which the comparison no longer refers to a direction. Runs of about $1\,\mathrm{s}$ lie between these limits; Berg and Purcell concluded that the bacterium works near what physics allows.

A spatial comparison across the body is far worse. The concentration difference between the poles of a $2\,\mu\mathrm{m}$ cell is ten times smaller than over a $20\,\mu\mathrm{m}$ run, and because $T_{\min}$ in Eq. (35.5) scales as $(\Delta c)^{-2/3}$, the cell would have to average roughly $10^{2}$ times longer than with a temporal comparison, long beyond the time in which rotational diffusion turns it. This is why bacteria sense in time.

### 35.2.2. Measuring in Space

Eukaryotic cells are larger ($10$–$20\,\mu\mathrm{m}$) and move slowly ($1$–$20\,\mu\mathrm{m\,min^{-1}}$), so a temporal comparison would take minutes, while a spatial one has a long baseline. Neutrophils and *Dictyostelium* amoebae measure gradients across their bodies and respond to differences of $1$–$2\,\%$ between front and back ([7.3.15](/7.3.15#sec-15.5.5)).

**Formula 35.2.2 (Snapshot Gradient Sensing)** A cell of length $L$ with $M$ receptors of dissociation constant $K_{\mathrm{D}}$, which compares the occupancies of its front and back halves at one instant, detects a gradient $g$ with signal-to-noise ratio

$$
\mathrm{SNR} = \frac{gL}{c}\sqrt{Mp(1 - p)} = gL\,\frac{\sqrt{McK_{\mathrm{D}}}}{c + K_{\mathrm{D}}} ,
\tag{35.6}
$$
which is maximal at $c = K_{\mathrm{D}}$, where $\mathrm{SNR} = (gL/c)\sqrt{M}/2$.

**Proof** In a snapshot the number of bound receptors among $M$ is binomial with variance $Mp(1 - p)$, so the occupancy fraction has variance $p(1 - p)/M$; propagating through $c = K_{\mathrm{D}}p/(1 - p)$ gives $(\delta c/c)^2 = 1/[Mp(1 - p)] = (c + K_{\mathrm{D}})^2/(McK_{\mathrm{D}})$. The front–back difference is $gL$ for the two halves, each with $M/2$ receptors, which changes only the numerical prefactor (by a factor of two in the variance); we keep the simpler form. With $p = 1/2$, $\sqrt{p(1 - p)} = 1/2$. $\square$

For a $1\,\%$ gradient across the cell, $\mathrm{SNR} \ge 1$ requires $M \ge (2 \times 100)^2 = 4\times10^4$ receptors (panel C of the figure above). *Dictyostelium* has about $4\times10^4$–$8\times10^4$ cAMP receptors, and its chemotactic accuracy is best near the receptor's $K_{\mathrm{D}}$: it works close to the snapshot limit. Averaging over time improves the ratio by the square root of the number of independent snapshots, $T/\tau_{\mathrm{c}}$, until the limit set by diffusion is reached, and the downstream network must then amplify a difference of a few percent into a front and a back; the mechanisms of local excitation and global inhibition are treated in [7.3.15](/7.3.15#fml-15.5.1) and in 35.7.2.

### 35.2.3. Other Physical Limits

Counting statistics limit every sense. The rods of the retina count photons; the absolute threshold of vision, a few absorbed photons, and the shape of the frequency-of-seeing curve follow from Poisson statistics ([7.6.18](/7.6.18)). Mechanical sensors are limited by thermal motion: a hair bundle of the inner ear of stiffness $\kappa \approx 1\,\mathrm{mN\,m^{-1}}$ fluctuates by $\sqrt{k_{\mathrm{B}}T/\kappa} \approx 2\,\mathrm{nm}$, yet hearing at threshold corresponds to sub-nanometer motions. The ear beats the thermal limit by filtering, because a stimulus of one frequency must compete only with the noise in a narrow band, and by active amplification at the cost of energy ([7.6.31](/7.6.31)). Magnetic and electric senses face analogous bounds ([7.6.19](/7.6.19)).

## 35.3. Information Transmission

### 35.3.1. Mutual Information

The signal-to-noise ratio describes how well a single difference can be detected. To ask how much a cell can know about its environment, we need a measure that does not depend on units or on the form of the response. Information theory provides it ([4.5.6](/4.5.6) introduces entropy and conditional entropy).

**Definition 35.3.1 (Mutual Information)** The **mutual information** between random variables $X$ and $Y$ with joint distribution $p(x, y)$ is

$$
I(X; Y) = \sum_{x, y}p(x, y)\log_2\frac{p(x, y)}{p(x)p(y)} = H(X) - H(X \mid Y) = H(Y) - H(Y \mid X) ,
\tag{35.7}
$$
with sums replaced by integrals for continuous variables. It is measured in bits.

The mutual information is the average reduction of uncertainty about one variable produced by observing the other. It is symmetric, non-negative, zero only if $X$ and $Y$ are independent, and unchanged by any invertible transformation of either variable; it is the **Kullback–Leibler divergence** of the joint distribution from the product of its marginals. Unlike a correlation coefficient it detects non-monotonic and nonlinear dependence.

**Example 35.3.1** A protein X is either highly or weakly expressed. In a medium rich in glucose (probability $0.6$) it is high with probability $0.9$; in poor medium (probability $0.4$) with probability $0.3$. The binary entropy $h(q) = -q\log_2q - (1 - q)\log_2(1 - q)$ gives $H(X \mid \text{rich}) = h(0.9) = 0.47$ and $H(X \mid \text{poor}) = h(0.3) = 0.88$ bits, so $H(X \mid G) = 0.6 \times 0.47 + 0.4 \times 0.88 = 0.63$ bits. Overall X is high with probability $0.6 \times 0.9 + 0.4 \times 0.3 = 0.66$, so $H(X) = h(0.66) = 0.93$ bits and $I(X; G) = 0.93 - 0.63 = 0.29$ bits. (Taking $H(X) = 1$ bit, as if X were high half the time, would overstate the information: the marginal must be computed from the same joint distribution.)

### 35.3.2. Channel Capacity

A signaling pathway maps an input $c$ (a ligand concentration) to an output $g$ (the activity of a transcription factor, the expression of a gene) through a noisy channel described by $p(g \mid c)$. The information it transmits depends also on the statistics of the inputs the cell encounters, $p(c)$.

**Definition 35.3.2 (Channel Capacity)** The **channel capacity** of a channel $p(g \mid c)$ is the largest mutual information between input and output over all input distributions, $C = \max_{p(c)}I(c; g)$.

The capacity counts, roughly, the logarithm of the number of input levels the cell can distinguish reliably: $1$ bit means two states (on and off), $2$ bits four. It can be computed by an iterative algorithm.

**Algorithm 35.3.1 (Blahut–Arimoto Algorithm)** For a channel with discrete inputs $c_i$ and outputs $g_j$ and transition probabilities $Q_{ij} = p(g_j \mid c_i)$:

1. Start from any input distribution with $p_i > 0$, for example uniform.
2. Compute the output distribution $q_j = \sum_ip_iQ_{ij}$ and, for each input, $d_i = \sum_jQ_{ij}\ln(Q_{ij}/q_j)$, the Kullback–Leibler divergence of its output distribution from the average output.
3. Update $p_i \leftarrow p_i\mathrm{e}^{d_i}/\sum_kp_k\mathrm{e}^{d_k}$ and return to step 2.

The mutual information increases at each step and converges to $C$ (Blahut, 1972; Arimoto, 1972); at the optimum all inputs used have the same divergence $d_i = C\ln 2$.

When the noise is small compared with the range of the output, the capacity has a closed form that shows what limits it.

**Theorem 35.3.1 (Capacity in the Small-Noise Limit)** Let the output be Gaussian with mean $\bar g(c)$, a monotonic function, and standard deviation $\sigma(\bar g)$ small compared with the range of $\bar g$. Then

$$
C \approx \log_2\left[\frac{1}{\sqrt{2\pi\mathrm{e}}}\int_{\bar g_{\min}}^{\bar g_{\max}}\frac{\mathrm{d}\bar g}{\sigma(\bar g)}\right] ,
\tag{35.8}
$$
achieved when the mean outputs are distributed as $P^*(\bar g) \propto 1/\sigma(\bar g)$.

**Proof** Because $\bar g(c)$ is monotonic we may use $\bar g$ as the input variable. If the noise is small, the output distribution is the input distribution smoothed over a width $\sigma$, so $H(g) \approx -\int P(\bar g)\log_2P(\bar g)\,\mathrm{d}\bar g$, and the conditional entropy of a Gaussian is $H(g \mid \bar g) = \log_2[\sqrt{2\pi\mathrm{e}}\,\sigma(\bar g)]$. Hence

$$
I \approx -\int P(\bar g)\log_2\left[\sqrt{2\pi\mathrm{e}}\,\sigma(\bar g)P(\bar g)\right]\mathrm{d}\bar g .
$$
Write $P^* = 1/(Z\sigma)$ with $Z = \int\mathrm{d}\bar g/\sigma$. Then $I = \log_2(Z/\sqrt{2\pi\mathrm{e}}) - \int P\log_2(P/P^*)\,\mathrm{d}\bar g$, and the last integral, a Kullback–Leibler divergence, is non-negative and vanishes only for $P = P^*$. $\square$

The result has a simple reading: the number of distinguishable outputs is the number of noise widths that fit into the output range, and the cell should use each output level in proportion to how reliably it can be produced. The shape of the input–output curve does not appear, because any monotonic curve can be compensated by the input distribution; what limits information is the noise at the output, which for gene expression is set by the counting statistics of the molecules (Tkačik, Callan and Bialek, 2008). The figure compares the formula with the exact capacity.

![Information transmission through a noisy input–output relation (input x = ln(c/K), mean output a Hill function with coefficient 5, Gaussian output noise of variance η²(ḡ + 0.02)). A: mean response and one standard deviation for two noise amplitudes. B: channel capacity from the Blahut–Arimoto algorithm (Algorithm 35.3.1, points) and the small-noise formula, Eq. (35.8) (line), against the noise amplitude; the dashed line is the information transmitted by inputs uniform in ln c, which is lower. The formula fails when the noise is no longer small: capacity never falls below what two well-separated inputs (one bit) provide until the noise approaches the output range. C: the distribution of mean outputs generated by the optimal input distribution for η = 0.05 (bars) and the prediction P*(ḡ) ∝ 1/σ(ḡ) (line); the exact optimum places discrete masses, smoothed here by binning](./plots/channel-capacity.py)

### 35.3.3. Measured Channels

Information-theoretic measurements of real pathways give modest numbers. The response of the transcription factor NF-κB to the inflammatory signal TNF in single mammalian cells transmits only about $1$ bit (Cheong and colleagues, 2011): an individual cell can tell whether TNF is present but hardly how much, and a population or repeated stimulation is needed for finer distinctions. The expression of *hunchback* carries about $1.5$ bits about Bicoid, close to the capacity computed from the measured noise (Tkačik, Callan and Bialek, 2008), and the four gap genes together specify the position of a nucleus along the *Drosophila* embryo with an error of about $1\,\%$ of the egg length (Dubuis and colleagues, 2013), roughly the spacing of neighboring cells. The **positional information** of development ([7.5.11](/7.5.11)) can therefore be measured in bits, and in this case it appears to be close to optimal. Whether cells generally maximize transmitted information, and what limits it (receptor numbers, the number of output molecules, the time available), are open questions; information is one of several candidate objectives besides growth rate and robustness ([7.6.40](/7.6.40)).

## 35.4. Run and Tumble

### 35.4.1. The Swimming Behavior

*E. coli* swims with four to eight helical flagella, each driven at its base by a rotary motor ([7.6.28](/7.6.28)). When the motors turn counterclockwise (viewed from behind the cell) the flagella form a bundle that pushes the cell forward in a smooth *run* at $20$–$30\,\mu\mathrm{m\,s^{-1}}$; when one or more motors switch to clockwise rotation, their flagella leave the bundle and the cell *tumbles*, turning in place for about $0.1$–$0.2\,\mathrm{s}$, after which a new run starts in a new direction. Berg and Brown (1972), with a microscope that followed single cells in three dimensions, found runs of about $1\,\mathrm{s}$ distributed exponentially and tumbles that change the direction by $68^\circ$ on average, with a bias towards forward directions.

**Definition 35.4.1 (Run-and-Tumble Motility)** **Run-and-tumble** motility is a pattern of swimming in which straight runs at constant speed, terminated at random with a rate $\lambda$, alternate with brief tumbles that reorient the cell randomly. Chemotaxis by run-and-tumble works by making $\lambda$ depend on the recent history of the concentration that the cell has experienced.

In a uniform environment the motion is a persistent **random walk** with diffusion coefficient $v^2\tau/[3(1 - \alpha)]$ in three dimensions, where $\tau = 1/\lambda$ and $\alpha = \langle\cos\theta\rangle$ is the mean cosine of the turning angle; for *E. coli* this is about $2\times10^2\,\mu\mathrm{m^2\,s^{-1}}$ (Example 5.1.1 of [7.6.5](/7.6.5)). In a gradient of attractant, runs that happen to go up the gradient are extended: the cell suppresses tumbles while the concentration it experiences increases. Runs down the gradient are not shortened much below their normal length. The result is a biased random walk, and the bias is small: a cell typically drifts at a few percent of its swimming speed.

### 35.4.2. Chemotactic Drift

The connection between the modulation of the tumble rate and the drift can be seen in a one-dimensional model.

**Formula 35.4.1 (Drift of a Run-and-Tumble Walker)** Let cells run at speed $v$ to the right or to the left and tumble with rates $\lambda_+$ and $\lambda_-$ respectively, each tumble choosing a new direction at random. In a uniform steady state the mean velocity is

$$
v_{\mathrm{d}} = v\,\frac{\lambda_- - \lambda_+}{\lambda_- + \lambda_+} .
\tag{35.9}
$$
If the tumble rate responds to the logarithmic rate of change of concentration along the path, $\lambda = \lambda_0(1 - \kappa\,\mathrm{d}\ln c/\mathrm{d}t)$, with $\kappa$ a response time, then $\lambda_\pm = \lambda_0(1 \mp \kappa v\,\partial_x\ln c)$ and

$$
v_{\mathrm{d}} = \kappa v^2\,\partial_x\ln c .
\tag{35.10}
$$

**Proof** Let $\rho_\pm$ be the densities of right- and left-moving cells. A tumble sends a cell into either direction with probability $1/2$, so in a spatially uniform state $\mathrm{d}\rho_+/\mathrm{d}t = -\lambda_+\rho_+/2 + \lambda_-\rho_-/2 = 0$, that is $\lambda_+\rho_+ = \lambda_-\rho_-$. With $\rho_+ + \rho_- = \rho$, $\rho_\pm = \rho\lambda_\mp/(\lambda_+ + \lambda_-)$, and the mean velocity $v(\rho_+ - \rho_-)/\rho$ is Eq. (35.9). For a cell moving right $\mathrm{d}\ln c/\mathrm{d}t = v\,\partial_x\ln c$, and inserting $\lambda_\pm$ gives Eq. (35.10). $\square$

Two features of Eq. (35.10) are characteristic of *E. coli*. The drift is proportional to the gradient of $\ln c$, not of $c$: a cell responds to relative changes, so the same fractional gradient gives the same drift at all background levels within its working range. In the continuum description of a population, this response becomes a chemotactic flux $\chi\rho\nabla c$ with sensitivity $\chi \propto 1/c$, the form used in the **Keller–Segel model** ([7.5.13](/7.5.13)). And the response must be to changes in time, which requires the cell to remember the recent past. Measurements of the motor's response to brief pulses of attractant show a biphasic impulse response: tumbling is suppressed for about one second and then slightly enhanced for a few seconds, the two lobes having nearly equal areas (Segall, Block and Berg, 1986). Such a kernel computes approximately a time derivative over a window of about $4\,\mathrm{s}$, consistent with the time limits of Example 35.2.1, and its zero integral is the signature of adaptation (35.6).

![Run-and-tumble chemotaxis simulated in two dimensions. Each cell swims at 20 µm/s, turns at each tumble by a random angle of 68° ± 25° to either side, and diffuses in angle during runs (D_r = 0.1 rad²/s); its tumble rate λ = λ₀(a/a₀)³ (λ₀ = 1 s⁻¹) is set by the activity a of an adapting MWC receptor cluster (Formula 35.5.1), with methylation dm/dt = 0.1 s⁻¹ (a₀ − a), a₀ = 1/3. A: five cells for 400 s in uniform attractant. B: the same in an exponential gradient of MeAsp, c = 0.1 mM e^{x/L} with L = 0.5 mm, increasing to the right; the start is marked by a cross. C: mean displacement along the gradient of 400 cells for L = 0.5, 1 and 2 mm, and (inset) the drift speed against 1/L: drift is proportional to the gradient of ln c, as in Eq. (35.10), and is a few percent of the swimming speed](./plots/run-and-tumble.py)

## 35.5. Amplification

### 35.5.1. The Chemotaxis Network

The signal from the receptors to the motors is carried by six cytoplasmic proteins, the Che proteins, organized as a **two-component system** ([7.1.15](/7.1.15)). The transmembrane chemoreceptors (Tar for aspartate and maltose, Tsr for serine, and three minor ones) form ternary complexes with the adaptor CheW and the histidine kinase CheA. Attractant binding inhibits the autophosphorylation of CheA; CheA transfers its phosphate to the response regulator CheY and to the methylesterase CheB. Phosphorylated CheY diffuses to the motors and binds to the switch protein FliM, increasing the probability of clockwise rotation; the phosphatase CheZ, localized at the receptor array, dephosphorylates CheY within about $0.1$–$1\,\mathrm{s}$, so that CheY-P reports the current kinase activity. The methyltransferase CheR adds methyl groups to four glutamate residues on each receptor, which increases its kinase-activating ability; CheB-P removes them. Because CheB is phosphorylated by the receptor's own kinase, methylation forms a slow negative feedback loop around the fast signaling path.

![The chemotaxis network of *E. coli* as an SBGN activity-flow map: attractant binding inhibits the receptor–CheW–CheA complex; its kinase activity produces CheY-P, which promotes clockwise rotation of the motor and tumbles, and is removed by CheZ; CheR methylation raises receptor activity and CheB-P demethylation lowers it. Because CheB is activated by the receptor's kinase, methylation closes a slow negative feedback loop (dashed box), responsible for adaptation, around the fast amplifying path](./plots/che-pathway.py)

The system has been measured quantitatively at each level. The concentration of CheY-P in single cells and the rotation of a single motor were recorded simultaneously by **fluorescence correlation spectroscopy** and bead tracking (Cluzel, Surette and Leibler, 2000). The kinase activity of the receptor array was measured in vivo by **Förster resonance energy transfer** between fluorescent CheY and CheZ, whose interaction requires phosphorylated CheY, so that the FRET signal reports the rate of CheY phosphorylation (Sourjik and Berg, 2002). These measurements locate the amplification of the pathway at two places, the receptor array and the motor.

### 35.5.2. Receptor Clusters

Cryo-electron tomography shows that *E. coli* packs its several thousand receptor dimers into a hexagonal lattice of trimers of dimers at the cell poles, held together on the cytoplasmic side by rings of CheA and CheW (Briegel and colleagues, 2012). The arrangement is conserved across bacteria with chemotaxis. In FRET measurements, mutant cells that cannot change their methylation respond to attractant with Hill coefficients of up to about ten, although each receptor binds one ligand: the receptors switch together.

**Definition 35.5.1 (Receptor Cluster)** A **receptor cluster** is an array of interacting receptors whose activity states are coupled, so that groups of receptors switch between an active and an inactive conformation together. In the simplest description, the cluster consists of cooperative units of $N$ receptors, each unit described by the **MWC model** ([7.6.4](/7.6.4#sec-4.5)).

**Formula 35.5.1 (MWC Model of a Chemoreceptor Cluster)** For a cooperative unit of $N$ receptors, each binding attractant with dissociation constant $K_{\mathrm{A}}$ in the active and $K_{\mathrm{I}}$ in the inactive state ($K_{\mathrm{I}} < K_{\mathrm{A}}$ for an attractant), the probability of being active is

$$
a = \frac{1}{1 + \mathrm{e}^{N\Delta F}}, \qquad \Delta F(m, c) = f(m) + \ln\frac{1 + c/K_{\mathrm{I}}}{1 + c/K_{\mathrm{A}}} ,
\tag{35.11}
$$
where $\Delta F$ is the free energy difference per receptor between the active and inactive states, in units of $k_{\mathrm{B}}T$, and $f(m)$ its value without ligand, which decreases with the methylation level $m$. Fits to FRET data for Tar and the attractant α-methylaspartate (MeAsp) give $K_{\mathrm{I}} \approx 18\,\mu\mathrm{M}$, $K_{\mathrm{A}} \approx 3\,\mathrm{mM}$, $f(m) \approx \alpha(m_0 - m)$ with $\alpha \approx 1.7$–$2$ and $m_0 \approx 1$, and $N$ from about $6$ to $20$ depending on the receptor composition and methylation (Shimizu, Tu and Berg, 2010; Tu, 2013).

The ligand term is the logarithm of the ratio of the binding polynomials of the two states (Formula 4.5.1 of [7.6.4](/7.6.4)): ligand binding favors the inactive state because it binds more tightly there. Two consequences follow.

**Theorem 35.5.1 (Logarithmic Sensing)** In the window $K_{\mathrm{I}} \ll c \ll K_{\mathrm{A}}$, $\Delta F \approx f(m) + \ln(c/K_{\mathrm{I}})$, so that the activity depends on $c$ only through $\ln c$:

$$
\frac{\partial a}{\partial\ln c} = -Na(1 - a), \qquad \lvert\Delta a\rvert \le \frac N4\left\lvert\frac{\Delta c}{c}\right\rvert .
\tag{35.12}
$$
The response to a fractional change $\Delta c/c$ is independent of the background, and a change of the background by a factor $\gamma$ is exactly compensated by a change $\Delta m = \ln\gamma/\alpha$ of the methylation level.

**Proof** For $c \gg K_{\mathrm{I}}$, $1 + c/K_{\mathrm{I}} \approx c/K_{\mathrm{I}}$; for $c \ll K_{\mathrm{A}}$, $1 + c/K_{\mathrm{A}} \approx 1$. Then $\partial\Delta F/\partial\ln c = 1$ and $\partial a/\partial\ln c = -N\mathrm{e}^{N\Delta F}/(1 + \mathrm{e}^{N\Delta F})^2 = -Na(1 - a)$, whose magnitude is at most $N/4$, attained at $a = 1/2$. With $f = \alpha(m_0 - m)$, replacing $c$ by $\gamma c$ and $m$ by $m + \ln\gamma/\alpha$ leaves $\Delta F$ unchanged. $\square$

The gain of the cluster is thus set by $N$, its maximal sensitivity is reached when the activity is near one half, and the working window spans the ratio $K_{\mathrm{A}}/K_{\mathrm{I}} \approx 170$, about two orders of magnitude of concentration, for each methylation state. Methylation slides the response curve along the $\ln c$ axis without changing its shape (panel A of the figure), which is how the cell extends its range to five orders of magnitude.

![The MWC model of a chemoreceptor cluster (Formula 35.5.1; N = 6, K_I = 18 µM, K_A = 3 mM, f(m) = 1.7(1 − m)). A: activity against MeAsp concentration for methylation levels m = 1 to 4: methylation shifts the response to higher concentrations; the last curve shows that the working range ends at K_A. B: the gain −da/d ln c, at most N/4 (dashed line, Theorem 35.5.1). C: response of clusters adapted to activity a₀ = 1/3 to a twofold increase or decrease of the concentration, against the background: in the window K_I ≪ c ≪ K_A the response depends only on the fold change, the Weber–Fechner law (Definition 35.6.2)](./plots/mwc-cluster.py)

### 35.5.3. The Motor Switch

The second amplifier is the motor. Cluzel, Surette and Leibler (2000) found that the clockwise bias of single motors depends on the CheY-P concentration $Y$ as a Hill function, $P_{\mathrm{CW}} = Y^{\mathsf H}/(Y^{\mathsf H} + K^{\mathsf H})$, with $K \approx 3.1\,\mu\mathrm{M}$ and **Hill coefficient** $H \approx 10$. The logarithmic gain is $\mathrm{d}P_{\mathrm{CW}}/\mathrm{d}\ln Y = HP_{\mathrm{CW}}(1 - P_{\mathrm{CW}})$, up to $2.6$ at the midpoint: a $10\,\%$ change of CheY-P changes the bias by about $25$ percentage points. The switch is a ring of $34$ FliM subunits, each able to bind one CheY-P, and its steep, stochastic switching has been modeled as an allosteric ring in which neighboring subunits couple their conformations (conformational spread, [7.6.28](/7.6.28#sec-28.4.3)), an **Ising model** ([7.6.4](/7.6.4#sec-4.4)) on a ring.

A steep motor is useful only if the CheY-P concentration of each cell lies within its narrow operating range, about $2$–$4\,\mu\mathrm{M}$. Adaptation of the receptor array (35.6) sets the adapted CheY-P level, but it does not set it precisely (Theorem 35.6.1 shows that the adapted level depends on the CheR and CheB concentrations); the motor itself adapts slowly to the CheY-P level by exchanging FliM subunits, which helps to keep it in range (Yuan, Branch, Hosu and Berg, 2012). Adapted motors respond even more steeply, with Hill coefficients near $20$ (Yuan and Berg, 2013). For a two-state equilibrium switch, the Hill coefficient cannot exceed the difference in the number of ligands bound between its two states (the linkage relation, Theorem 4.5.2 of [7.6.4](/7.6.4)); steepness beyond the number of binding sites, or beyond the measured difference in bound CheY-P, would require energy dissipation in the switching mechanism, a possibility discussed with the general bounds in [7.6.38](/7.6.38).

### 35.5.4. Equilibrium and Nonequilibrium Amplification

Amplification, a response steeper than the hyperbola of simple binding, can be achieved in two fundamentally different ways.

| | Equilibrium amplification | Nonequilibrium amplification |
|---|---|---|
| Mechanism | cooperative binding, allostery (MWC, Ising), sequestration, multisite binding | **zero-order ultrasensitivity** of modification cycles, positive feedback, kinetic proofreading, multistep cascades |
| Energy | none | continuous dissipation (ATP, GTP) |
| Steepness limited by | number of coupled sites (the size of the cooperative unit) | free energy dissipated per cycle, number of steps |
| Response | sigmoidal, set by binding energies | can be steeper, asymmetric, with memory and hysteresis |
| Examples | hemoglobin, chemoreceptor arrays | MAPK cascades, phosphorylation cycles, the motor (perhaps) |

The second column rests on a thermodynamic fact. Consider a substrate converted between an unmodified form E and a modified form $\mathrm{E_p}$ by a kinase K (with ATP) and a phosphatase (releasing phosphate), the phosphorylation–dephosphorylation cycle of [7.1.9](/7.1.9) and [7.3.18](/7.3.18).

**Theorem 35.5.2 (No Response at Equilibrium)** If the ratio of ATP to ADP and phosphate is at its equilibrium value, so that the cycle has zero driving force, then the steady-state ratio $[\mathrm{E_p}]/[\mathrm{E}]$ does not depend on the concentration of the kinase or of the phosphatase.

**Proof** At equilibrium every reaction is balanced individually (the **principle of detailed balance**), so the ratio $[\mathrm{E_p}]/[\mathrm{E}]$ equals the equilibrium constant of the overall reaction $\ce{E + ATP <=> E_p + ADP}$ times the activity ratio $[\ce{ATP}]/[\ce{ADP}]$, or equivalently of $\ce{E_p + H2O <=> E + P_i}$; neither involves the enzymes, which are catalysts and do not shift equilibria. $\square$

A phosphorylation cycle can therefore respond to its kinase only because the cell keeps ATP far from equilibrium with its hydrolysis products, about $20\,k_{\mathrm{B}}T$ per molecule ([7.6.3](/7.6.3)). When both converting enzymes work near saturation, $K/E_{\mathrm{T}} \ll 1$ in the notation of the Goldbeter–Koshland function, the steady state switches abruptly from mostly unmodified to mostly modified as the ratio of the enzymes' maximal rates crosses one (panels A and B of the figure); Qian (2007) showed that the steepness of such switches increases with the free energy dissipated per cycle, and Owen, Gingrich and Horowitz (2020) derived general bounds on nonequilibrium sensitivity in terms of the driving force of the cycles ([7.6.38](/7.6.38)). In the chemotaxis network the receptor array amplifies by equilibrium cooperativity, CheA autophosphorylation and CheY phosphorylation consume ATP, and adaptation, as we shall see, depends on the irreversibility of methylation.

![Two amplifiers. A: zero-order ultrasensitivity of a modification cycle (Goldbeter–Koshland function, both enzymes with Michaelis constant K): steady-state fraction of modified substrate against the ratio of the maximal rates for K/E_T = 1, 0.1 and 0.01. B: effective Hill coefficient ln 81/ln(θ₉₀/θ₁₀) of these curves against K/E_T; it grows without bound as the enzymes saturate. C: the clockwise bias of the flagellar motor against CheY-P (Hill coefficient 10.3, K = 3.1 µM) and its logarithmic gain (dashed, right axis)](./plots/amplification.py)

## 35.6. Adaptation

### 35.6.1. The Barkai–Leibler Model

When attractant is added uniformly, *E. coli* stops tumbling and then, over seconds to minutes, returns to its prestimulus tumbling frequency; removing it again produces a burst of tumbling and recovery. The recovery is exact: in the experiments of Alon, Surette, Barkai and Leibler (1999) the adapted tumbling frequency did not depend on the attractant concentration even when the level of CheR was changed fifty-fold. The system shows **perfect adaptation** ([7.3.18](/7.3.18#def-18.4.4)) that is robust, not the result of tuned parameters. Barkai and Leibler (1997) proposed a mechanism that explains why.

**Definition 35.6.1 (Barkai–Leibler Model)** The **Barkai–Leibler model** of chemotactic adaptation describes the receptor activity $a(m, c)$, a fast function of the methylation level $m$ and the attractant concentration $c$, and the slow dynamics of methylation under two assumptions: CheR methylates receptors at a saturated, constant rate $V_R$, and CheB demethylates only active receptors, with Michaelis–Menten dependence on their number:

$$
\frac{\mathrm{d}m}{\mathrm{d}t} = V_R - V_B\,\frac{a}{a + K_B} ,
\tag{35.13}
$$
with $V_R$ and $V_B$ proportional to the concentrations of CheR and CheB.

**Theorem 35.6.1 (Robust Perfect Adaptation)** If $V_B > V_R(1 + K_B)$ and $a$ increases with $m$, then Eq. (35.13) has a unique steady state, which is stable, and the activity in it,

$$
a^* = \frac{K_BV_R}{V_B - V_R} ,
\tag{35.14}
$$
does not depend on the attractant concentration. The adapted activity, and the time needed to reach it, depend on the enzyme concentrations; the precision of adaptation does not.

**Proof** The right-hand side of Eq. (35.13) depends on $m$ and $c$ only through $a$, and vanishes exactly when $a = a^*$; the condition on $V_B$ ensures $a^* < 1$, so for each $c$ there is an $m^*(c)$ with $a(m^*, c) = a^*$ (within the range of $m$ the receptors can reach). Stability: $\partial\dot m/\partial m = -V_BK_B(a + K_B)^{-2}\,\partial a/\partial m < 0$. After a change of $c$, $a$ jumps (fast binding), $m$ relaxes to $m^*(c)$ with rate $\lvert\partial\dot m/\partial m\rvert$, which depends on $V_B$, and $a$ returns to $a^*$, which depends on $V_R/V_B$ but not on $c$. $\square$

![Robust perfect adaptation in the Barkai–Leibler model (Theorem 35.6.1), with the MWC cluster of Formula 35.5.1 and dm/dt = V_R − V_B a/(a + K_B) (V_B = 0.1 s⁻¹, K_B = 0.5, V_R = 0.02 s⁻¹ at the normal CheR level). A: activity after steps of MeAsp from 0 to 0.1 mM, to 1 mM and back to 0.1 mM for cells with 0.5, 1, 2 and 3 times the normal CheR level: each returns exactly to its own prestimulus activity. B: adaptation precision (activity 290 s after the step to 1 mM divided by the prestimulus activity) against the CheR level, for the Barkai–Leibler model and for a model in which CheR is not saturated, so that the methylation rate depends on m as well as on a; precision is then lost. C: the adapted activity a* = K_B V_R/(V_B − V_R) (line, with simulated values) and the time to recover half the response (squares, right axis) both depend on the CheR level, as Alon and colleagues found: precision is robust, the adapted level and the adaptation time are not](./plots/barkai-leibler.py)

The two assumptions are what make the model work. If CheR were not saturated, its rate would depend on $m$; if CheB acted on inactive receptors as well, its rate would depend on $m$ through the number of methylated sites, independently of activity; in either case $\dot m = 0$ would no longer fix $a$ (panel B). Both assumptions have experimental support: CheR binds to a pentapeptide at the receptor tails that tethers it near its substrates, and CheB-P preferentially demethylates active receptors. Precise adaptation is a property of the topology of the network and the saturation of particular reactions, not of the values of rate constants.

**Example 35.6.1** A reduced version of the model makes the phase-plane structure explicit. Let $X$ be unmethylated receptors, $X_{\mathrm{A}}$ methylated active receptors and $X_{\mathrm{I}}$ methylated receptors made inactive by bound ligand, with methylation at the saturated rate $v_RR$, demethylation of active receptors at $v_BBX_{\mathrm{A}}/(K_{\mathrm{M}} + X_{\mathrm{A}})$, and ligand binding $X_{\mathrm{A}} \rightleftharpoons X_{\mathrm{I}}$ with rates $k_{\mathrm{on}}c$ and $k_{\mathrm{off}}$. The equations for $X_{\mathrm{A}}$ and $X_{\mathrm{I}}$ do not involve $X$, and their fixed point is

$$
X_{\mathrm{A}}^* = \frac{K_{\mathrm{M}}v_RR}{v_BB - v_RR}, \qquad X_{\mathrm{I}}^* = \frac{k_{\mathrm{on}}c}{k_{\mathrm{off}}}X_{\mathrm{A}}^* .
$$
A change of $c$ moves the fixed point only along the $X_{\mathrm{I}}$ axis: the number of active receptors, which sets the tumbling rate, is restored exactly.

### 35.6.2. Integral Feedback

Yi, Huang, Simon and Doyle (2000) recognized Eq. (35.13) as an instance of integral feedback, the principle by which thermostats and cruise controls hold their outputs at a set point.

**Definition 35.6.2 (Integral Feedback)** A system with output $y$ is under **integral feedback** if a controller variable $x$ accumulates the deviation of the output from a set point, $\dot x = F(y)$ with $F(y_0) = 0$, and $x$ acts back on the output. At any stable steady state $y = y_0$, whatever the constant disturbances.

In chemotaxis the output is the activity $a$, the set point is $a^*$, and the methylation level is the integral of the error: $m(t) = m(0) + \int_0^tF(a(t'))\,\mathrm{d}t'$ with $F(a) = V_R - V_Ba/(a + K_B)$. Conversely, a linear system with robust perfect adaptation to step inputs must contain integral feedback (the internal model principle of control theory); for nonlinear networks, the analogous requirement is that some variable's rate of change depend only on the output. The general theory, and the incoherent feed-forward loop as the other route to adaptation, are treated in [7.3.18](/7.3.18#fml-18.4.2) and [systems biology](/7.9); 35.7 asks which networks can adapt at all.

### 35.6.3. The Weber–Fechner Law and Fold-Change Detection

Psychophysics found long ago that the smallest perceptible change of a stimulus is proportional to its magnitude (Weber, 1834), and Fechner inferred that sensation grows as the logarithm of the stimulus.

**Definition 35.6.3 (Weber–Fechner Law)** A sensory system obeys the **Weber–Fechner law** if its response to a change of stimulus is proportional to the relative change $\Delta c/c$, that is to $\Delta\ln c$, over its working range.

**Definition 35.6.4 (Fold-Change Detection)** A system shows **fold-change detection** if its entire response to an input $c(t)$, including its time course, is unchanged when the input is multiplied by a constant: the response depends only on $c(t)/c_0$, where $c_0$ is the background to which it was adapted.

Chemotaxis combines the two properties of the receptor cluster. Logarithmic sensing makes the immediate response a function of $\Delta\ln c$ (Theorem 35.5.1), and adaptation removes the background.

**Proposition 35.6.1 (Fold-Change Detection in Chemotaxis)** In the window $K_{\mathrm{I}} \ll c \ll K_{\mathrm{A}}$, with $f(m) = \alpha(m_0 - m)$ and methylation dynamics $\dot m = F(a)$, the activity $a(t)$ produced by the input $\gamma c(t)$ from the state adapted to $\gamma c(0)$ equals that produced by $c(t)$ from the state adapted to $c(0)$, for every $\gamma > 0$.

**Proof** In the window, $a = [1 + \exp(N(\alpha(m_0 - m) + \ln(c/K_{\mathrm{I}})))]^{-1}$ depends on $m$ and $c$ only through $u = \ln c - \alpha m$. Then $\dot u = \mathrm{d}\ln c/\mathrm{d}t - \alpha F(a(u))$ is unchanged by $c \to \gamma c$, and the adapted initial states have the same $u$. The two trajectories of $u$, and of $a$, coincide. $\square$

Panel C of the MWC figure shows the corresponding property of the adapted response. Lazova, Ahmed, Bellomo, Stocker and Shimizu (2011) confirmed fold-change detection in swimming *E. coli* over a range of MeAsp concentrations from about $10\,\mu\mathrm{M}$ to $0.5\,\mathrm{mM}$, failing near the dissociation constants as the model predicts. Fold-change detection also appears in eukaryotic pathways built on incoherent feed-forward loops (Wnt, ERK; Goentoro and colleagues, 2009; Shoval and colleagues, 2010). For navigation, it means that the drift speed depends only on the gradient of $\ln c$ (Eq. (35.10)), so that a bacterium climbs an exponential gradient at constant speed.

### 35.6.4. The Cost of Adaptation

Methylation and demethylation form a cycle driven by the hydrolysis of S-adenosylmethionine, the methyl donor (about one per methyl group). The driving force is essential: in an equilibrium system, the rates of methylation and demethylation of a receptor in a given state would obey detailed balance with respect to the free energies of the states, and the activity-dependent asymmetry of Eq. (35.13), CheR acting on inactive and CheB on active receptors, could not exist. Lan, Sartori, Neumann, Sourjik and Tu (2012) showed with a stochastic model of the methylation cycle that the adaptation error decreases exponentially with the free energy dissipated per cycle, and that the rate of dissipation needed grows with the speed of adaptation and with the logarithm of the required accuracy, an energy–speed–accuracy trade-off. For *E. coli* the cost is a small fraction of the cell's energy budget, but the principle, that sensing with memory and exact adaptation requires dissipation, is general and is treated with kinetic proofreading and molecular motors in [7.6.38](/7.6.38).

## 35.7. Design Principles of Adaptation

### 35.7.1. Searching for Adaptive Topologies

Which networks can adapt? Ma, Trusina, El-Samad, Lim and Tang (2009) answered the question by brute force. They enumerated all $16\,038$ networks of three nodes (an input node A, an output node C and one more node B) in which each of the nine possible links is positive, negative or absent and the input reaches the output; modeled each node as an enzyme activated and deactivated by Michaelis–Menten reactions, with background enzymes where a node lacks a negative input; and sampled $10^4$ parameter sets for each. A network adapts if a step of the input produces a large transient response of C (sensitivity $> 1$) and a small change of its steady state (precision $> 10$, in relative terms). Only $395$ topologies adapted robustly, and almost all of them contained one of two cores:

- a *negative feedback loop with a buffer node* (NFBLB), $\mathrm{A} \to \mathrm{C} \to \mathrm{B} \dashv \mathrm{A}$, in which B is activated by C and deactivated by a background enzyme, both reactions saturated, so that $\dot B \approx k_1C - k_2$ integrates the error of C: integral feedback, as in chemotaxis;
- an *incoherent feed-forward loop with a proportioner node* (IFFLP), $\mathrm{A} \to \mathrm{C}$ and $\mathrm{A} \to \mathrm{B} \dashv \mathrm{C}$, in which B tracks A proportionally and divides it out of the steady state of C, as in [Formula 18.4.2 of 7.3.18](/7.3.18#fml-18.4.2).

Each core imposes conditions on the regime of its reactions, saturation for the buffer and linearity for the proportioner, and larger networks that adapt are built on one of the two. The search did not find a third mechanism; it turned a question of biochemistry into one of network architecture, and the result, a small number of design principles behind many possible implementations, has been confirmed in synthetic circuits.

![The two cores of robust adaptation in Michaelis–Menten networks of three nodes (input I stepped from 0.5 to 0.6 at t = 100). A: negative feedback with a buffer node, A → C → B ⊣ A; the buffer B is activated by C and deactivated by a background enzyme, both with Michaelis constant K. For small K both reactions are saturated, B integrates the error of C, and C returns to its set point. B: incoherent feed-forward loop with a proportioner node, A → C and A → B ⊣ C; B is made at a saturated rate proportional to A and removed by an enzyme with Michaelis constant K_B; for large K_B the removal is linear, B is proportional to A, and the input cancels from the steady state of C. C: adaptation precision against the saturation parameter of each core (K for the feedback, 1/K_B for the feed-forward loop): precision exceeds 10 (dashed) only in the regime that each mechanism requires](./plots/adaptation-search.py)

### 35.7.2. Gradient Sensing in Eukaryotic Cells

Eukaryotic chemotaxis uses the same two principles in space. A *Dictyostelium* amoeba or a neutrophil responds to a uniform increase of attractant with a transient recruitment of signaling proteins (PI3K, Ras activity, PIP₃) to its whole membrane, which then returns to baseline: it adapts. In a gradient it maintains a persistent crescent of activity facing the source, whose strength depends on the relative and not on the absolute gradient. The model of local excitation and global inhibition ([7.3.15](/7.3.15#fml-15.5.1)), in which each patch of membrane activates a local excitor and a fast-diffusing inhibitor that reports the mean occupancy of the whole cell, explains both: it is an incoherent feed-forward loop in which the proportioner is spatially averaged. The physical limits of 35.2.2 then apply to the occupancy difference, and LEGI itself does not amplify: the front–back difference of the response is no larger than that of receptor occupancy, a few percent. Amplification comes downstream, from positive feedback among Ras, PI3K, Rac and actin, which makes the membrane an excitable medium, and from mutual inhibition between front and back; these produce the polarized state of a migrating cell ([7.6.36](/7.6.36) treats the reaction–diffusion mechanisms of polarity). Unlike *E. coli*, eukaryotic cells can sense a gradient without moving, as cells immobilized with latrunculin show.

## 35.8. Signaling on a Leash

Signaling proteins are often built from modules joined by flexible linkers, and many are autoinhibited: a domain of the protein binds intramolecularly to a ligand-binding domain of the same protein and holds it in an inactive state until an external ligand competes it away. The neuronal Wiskott–Aldrich syndrome protein N-WASP, which activates the actin-nucleating Arp2/3 complex at the leading edge of migrating cells, is an example: its output domain is held by an intramolecular interaction that is released when **Cdc42**-GTP and PIP₂ bind ([7.3.15](/7.3.15)). The strength of such a switch depends on the tether.

**Formula 35.8.1 (Effective Concentration of a Tethered Ligand)** A ligand attached to its receptor by a flexible linker behaves as if it were present at the effective concentration

$$
c_{\mathrm{eff}} = \frac{1}{N_{\mathrm{A}}}\left(\frac{3}{2\pi\langle R^2\rangle}\right)^{3/2} ,
\tag{35.15}
$$
where $\langle R^2\rangle$ is the mean squared end-to-end distance of the linker, modeled as a Gaussian chain. A switch with an autoinhibited, a free and a ligand-bound state is active (not autoinhibited) with probability

$$
p_{\mathrm{active}} = \frac{1 + c/K_1}{1 + c_{\mathrm{eff}}/K_2 + c/K_1} ,
\tag{35.16}
$$
where $K_1$ is the dissociation constant of the external ligand at concentration $c$ and $K_2$ that of the intramolecular interaction.

**Proof** For a Gaussian chain, the end-to-end vector has density $(3/(2\pi\langle R^2\rangle))^{3/2}\exp(-3R^2/(2\langle R^2\rangle))$, so the probability density of finding the tethered ligand at the receptor ($R \approx 0$) is the prefactor, a number of molecules per volume; dividing by $N_{\mathrm{A}}$ gives a molar concentration. This is the **J factor** of DNA looping ([7.6.21](/7.6.21)) for a flexible chain. The three states have statistical weights $c_{\mathrm{eff}}/K_2$ (autoinhibited), $1$ (free) and $c/K_1$ (externally bound), relative to the free state, and the active states are the last two. $\square$

**Example 35.8.1** A flexible linker of $50$ residues has a contour length of about $19\,\mathrm{nm}$ and, with a Kuhn length of about $0.8\,\mathrm{nm}$ (a **freely jointed chain**, [7.6.21](/7.6.21)), $\langle R^2\rangle \approx 15\,\mathrm{nm^2}$. Then $(3/(2\pi \times 15))^{3/2} = 5.6\times10^{-3}\,\mathrm{nm^{-3}}$, and since $1\,\mathrm{M}$ corresponds to $0.60\,\mathrm{nm^{-3}}$, $c_{\mathrm{eff}} \approx 9\,\mathrm{mM}$. An intramolecular interaction with $K_2 = 10\,\mu\mathrm{M}$, weak as an interaction between separate proteins, is then favored by $c_{\mathrm{eff}}/K_2 \approx 900$ and keeps the switch $99.9\,\%$ off; an external ligand with $K_1 = 1\,\mu\mathrm{M}$ activates it half-maximally at $c \approx K_1c_{\mathrm{eff}}/K_2 \approx 0.9\,\mathrm{mM}$. Lengthening the linker lowers $c_{\mathrm{eff}}$ as $\langle R^2\rangle^{-3/2}$ and shifts the activation curve to lower ligand concentrations. Dueber, Yeh, Chak and Lim (2003) replaced the natural regulatory domains of N-WASP by a PDZ domain and its peptide ligand and found that such synthetic switches responded to free PDZ ligand as Eq. (35.16) predicts, with thresholds that could be tuned by the linker length and the affinities. Tethering converts weak affinities into strong, tunable switches, and the same physics sets the activity of scaffolded kinases and of multivalent signaling complexes.

## Summary

| Question | Result | Where |
|---|---|---|
| Best possible counting | $(\delta c/c)^2 = 1/(4\pi DacT)$; Berg–Purcell limit $\delta c/c \sim (DacT)^{-1/2}$ | Theorem 35.1.1 |
| Receptor patches | $J = 4\pi Dac\,Ns/(Ns + \pi a)$; half at $N = \pi a/s$, $0.08\,\%$ coverage | Formula 35.1.1 |
| Binding kinetics | time averaging $(\delta c/c)^2 = 2/(k_+c(1 - p)T)$; maximum likelihood $1/\bar n$, twice better | Theorems 35.1.2–35.1.3 |
| Temporal gradient sensing | $T_{\min} = (4c/(\pi Dav^2g^2))^{1/3}$, below the rotational-diffusion time: bacteria sense in time | Formula 35.2.1 |
| Spatial gradient sensing | $\mathrm{SNR} = gL\sqrt{McK_{\mathrm{D}}}/(c + K_{\mathrm{D}})$; $1\,\%$ needs $M \approx 4\times10^4$ | Formula 35.2.2 |
| Information | mutual information, capacity; small noise $C \approx \log_2[(2\pi\mathrm{e})^{-1/2}\int\mathrm{d}\bar g/\sigma]$ | Definitions 35.3.1–35.3.2, Algorithm 35.3.1, Theorem 35.3.1 |
| Chemotactic drift | $v_{\mathrm{d}} = v(\lambda_- - \lambda_+)/(\lambda_- + \lambda_+) = \kappa v^2\partial_x\ln c$ | Formula 35.4.1 |
| Receptor cluster | $a = [1 + \mathrm{e}^{N\Delta F}]^{-1}$; log sensing, gain $\le N/4$ | Formula 35.5.1, Theorem 35.5.1 |
| Amplification | cluster (equilibrium) and motor ($H \approx 10$); cycles respond only away from equilibrium | Theorem 35.5.2 |
| Adaptation | $\dot m = V_R - V_Ba/(a + K_B)$, $a^* = K_BV_R/(V_B - V_R)$, independent of $c$ | Theorem 35.6.1 |
| Weber–Fechner, fold-change detection | log sensing plus integral feedback | Proposition 35.6.1 |
| Adaptive topologies | integral feedback with a buffer node; incoherent feed-forward with a proportioner | 35.7.1 |
| Tethered switches | $c_{\mathrm{eff}} = N_{\mathrm{A}}^{-1}(3/2\pi\langle R^2\rangle)^{3/2}$, $p_{\mathrm{active}} = (1 + c/K_1)/(1 + c_{\mathrm{eff}}/K_2 + c/K_1)$ | Formula 35.8.1 |

- Precision is limited by the number of molecules a sensor sees, about $DacT$; sparse receptors suffice to catch them, binding wastes information while receptors are occupied, and the best estimators use only the waiting times for binding.
- *E. coli* senses in time because it is small and fast, eukaryotic cells in space because they are large and slow; both work near the physical limits.
- The chemotaxis network separates functions in time: fast binding and amplification by a cooperative receptor array and an ultrasensitive motor; slow, robust perfect adaptation by integral feedback through methylation, which together give logarithmic sensing and fold-change detection over five decades of concentration. Amplification and exact adaptation both rely on energy dissipation.

## Questions

1. A receptor binds its ligand with $k_+ = 10^8\,\mathrm{M^{-1}\,s^{-1}}$ and $K_{\mathrm{D}} = 10\,\mathrm{nM}$. Estimate the relative error of a concentration estimate after $1\,\mathrm{s}$ at $c = 10\,\mathrm{nM}$ for one receptor (time averaging and maximum likelihood) and for $10^4$ independent receptors. What limits the second number in reality?

   **Answer** $k_+c = 10^8 \times 10^{-8} = 1\,\mathrm{s^{-1}}$, $p = 1/2$. Time averaging: $(\delta c/c)^2 = 2/(1 \times 0.5 \times 1) = 4$, an error of $200\,\%$; maximum likelihood: $(\delta c/c)^2 = 2$, $140\,\%$. One receptor learns almost nothing in a second. With $10^4$ independent receptors the variance falls $10^4$-fold, to an error of $2\,\%$ and $1.4\,\%$. In reality receptors on one cell are not independent, because they compete for the same molecules diffusing to the cell; the error cannot fall below the whole-cell limit $(4\pi DacT)^{-1/2}$. For $a = 5\,\mu\mathrm{m}$ and $D = 100\,\mu\mathrm{m^2\,s^{-1}}$, $c = 10\,\mathrm{nM} = 6\,\mu\mathrm{m^{-3}}$, $4\pi DacT = 3.8\times10^4$, an error of $0.5\,\%$, so $10^4$ receptors are still below the diffusive limit here.

2. Derive Formula 35.1.1 using the electrostatic analogy, and use it to show that adding receptors beyond $N = \pi a/s$ gives diminishing returns. How many receptors give $90\,\%$ of the maximal flux for $a = 1\,\mu\mathrm{m}$, $s = 1\,\mathrm{nm}$?

   **Answer** The diffusive flux to an absorber held at zero concentration equals $Dc$ times its capacitance; the cell's capacitance in series with that of $N$ parallel disks ($4s$ each) gives Eq. (35.2). Then $J/J_{\max} = x/(1 + x)$ with $x = Ns/\pi a$: from $x = 1$ to $x = 9$ the flux rises only from $50$ to $90\,\%$. $90\,\%$ requires $N = 9\pi a/s \approx 2.8\times10^4$ receptors, still only $0.7\,\%$ of the surface.

3. Why does a receptor that is bound most of the time make a poor concentration sensor, and what is the optimal occupancy for the time-averaging estimator at fixed $K_{\mathrm{D}}$ and $T$? Compare with the optimum for a snapshot of many receptors.

   **Answer** Bound intervals carry no information about $c$ (their duration depends only on $k_-$); information comes from binding events, which occur at rate $k_+c(1 - p)$, and a receptor that is almost always bound produces few of them per unit time relative to its occupancy. With $p = c/(c + K_{\mathrm{D}})$, Eq. (35.3) becomes $(\delta c/c)^2 = 2(c + K_{\mathrm{D}})/(k_+cK_{\mathrm{D}}T) = (2/T)(1/k_+c + 1/k_-)$. It decreases monotonically with $c$: at low concentration binding is rare, and at high concentration the error approaches the floor $2/(k_-T)$, set by the number of unbinding events the receptor can complete. There is no interior optimum for a time-averaging receptor. A snapshot of many receptors is different: $(\delta c/c)^2 = (c + K_{\mathrm{D}})^2/(McK_{\mathrm{D}})$ (Formula 35.2.2) is minimal at $c = K_{\mathrm{D}}$, because a snapshot sees occupancy, not events, and an occupancy near $0$ or $1$ changes little when $c$ changes.

4. Using Formula 35.2.1, estimate the shortest useful run of *E. coli* in a gradient of serine at $c = 10\,\mu\mathrm{M}$ that changes by $10\,\%$ per $100\,\mu\mathrm{m}$. Take $D = 900\,\mu\mathrm{m^2\,s^{-1}}$, $a = 1\,\mu\mathrm{m}$, $v = 25\,\mu\mathrm{m\,s^{-1}}$. Is the run time of *E. coli* adequate?

   **Answer** $c = 10\,\mu\mathrm{M} = 6000\,\mu\mathrm{m^{-3}}$, $g = 0.1c/100\,\mu\mathrm{m} = 6\,\mu\mathrm{m^{-4}}$. $T_{\min} = (4 \times 6000/(\pi \times 900 \times 1 \times 625 \times 36))^{1/3} = (3.8\times10^{-4})^{1/3} \approx 0.07\,\mathrm{s}$. Runs of about $1\,\mathrm{s}$ are much longer, so counting noise is not limiting in such a steep gradient. It becomes limiting in shallow gradients at low concentration: for $c = 10\,\mathrm{nM}$ ($6\,\mu\mathrm{m^{-3}}$) and a gradient of $1\,\%$ per $100\,\mu\mathrm{m}$ ($g = 6\times10^{-4}\,\mu\mathrm{m^{-4}}$), $T_{\min} = (24/(\pi \times 900 \times 625 \times 3.6\times10^{-7}))^{1/3} \approx 3.4\,\mathrm{s}$, comparable to the time in which rotational diffusion randomizes the direction; such gradients are near the limit of detection.

5. Show that the mutual information between input and output of a channel is unchanged if the output is transformed by an invertible function, and explain why this makes information a natural measure for comparing pathways that use different readouts (concentrations, fluorescence, nuclear localization).

   **Answer** For an invertible $h$, $y = h(g)$, the joint and marginal densities transform with the same Jacobian: $p(c, y) = p(c, g)/\lvert h'(g)\rvert$ and $p(y) = p(g)/\lvert h'(g)\rvert$, so the ratio $p(c, y)/[p(c)p(y)]$ in Eq. (35.7) is unchanged, and so is its average. Hence the information does not depend on calibration (fluorescence units, nonlinear reporters) as long as the mapping is one-to-one and deterministic. A signal-to-noise ratio or a variance depends on units and on the linearization point; information compares an NF-κB pathway read by nuclear localization with a gene read by mRNA counts on the same scale, in bits. (Additional noise in the reporter, which is not invertible, can only reduce the measured information, by the data-processing inequality.)

6. Implement the Blahut–Arimoto algorithm for a binary symmetric channel that flips the input with probability $\varepsilon = 0.1$ and check that the capacity is $1 - h(\varepsilon)$. What input distribution is optimal?

   **Answer** By symmetry the optimum is uniform, and $C = 1 - h(0.1) = 1 - 0.469 = 0.531$ bits.

   ```python
   import numpy as np
   Q = np.array([[0.9, 0.1], [0.1, 0.9]])
   p = np.array([0.8, 0.2])
   for _ in range(200):
       q = p @ Q
       d = (Q * np.log(Q / q)).sum(axis=1)
       p = p * np.exp(d); p /= p.sum()
   q = p @ Q
   print(p, (p[:, None] * Q * np.log2(Q / q)).sum())   # [0.5 0.5] 0.531
   ```

7. In the one-dimensional run-and-tumble model, cells tumble with rate $\lambda_0 = 1\,\mathrm{s^{-1}}$ and run at $v = 20\,\mu\mathrm{m\,s^{-1}}$; up the gradient the tumble rate is lowered by $10\,\%$, down the gradient unchanged. Compute the drift speed and the chemotactic efficiency $v_{\mathrm{d}}/v$. Why do bacteria not simply lower the tumble rate further?

   **Answer** $\lambda_+ = 0.9$, $\lambda_- = 1.0\,\mathrm{s^{-1}}$; Eq. (35.9) gives $v_{\mathrm{d}} = 20 \times 0.1/1.9 = 1.05\,\mu\mathrm{m\,s^{-1}}$, $5\,\%$ of the swimming speed. A stronger response requires a larger change of tumble rate per change of $\ln c$, which needs more gain (more noise amplification) and longer runs; but runs longer than the rotational-diffusion time lose their direction, and a cell that suppresses tumbling strongly in response to noise performs worse. Measured drift speeds of *E. coli* are a few micrometers per second, consistent with the estimate.

8. Using Formula 35.5.1 with $N = 6$, $K_{\mathrm{I}} = 18\,\mu\mathrm{M}$ and $K_{\mathrm{A}} = 3\,\mathrm{mM}$, compute the change of activity of a cluster adapted to $a = 1/3$ at a background of $0.1\,\mathrm{mM}$ when the concentration rises by $10\,\%$. By how much must the methylation level change to restore the activity if $\alpha = 1.7$?

   **Answer** $\partial\Delta F/\partial\ln c = c/(c + K_{\mathrm{I}}) - c/(c + K_{\mathrm{A}}) = 0.1/0.118 - 0.1/3.1 = 0.847 - 0.032 = 0.815$. So $\Delta a \approx -Na(1 - a) \times 0.815 \times \ln 1.1 = -6 \times 0.222 \times 0.815 \times 0.0953 = -0.104$, a $31\,\%$ drop of the activity for a $10\,\%$ change of concentration (amplification about $3$ in relative terms). Restoring $\Delta F$ requires $\alpha\Delta m = 0.815 \times 0.0953 = 0.078$, $\Delta m = 0.046$ methyl groups per receptor.

9. Show that the Barkai–Leibler model loses perfect adaptation if CheB demethylates all receptors, $\dot m = V_R - V_B'm/(m + K_m)$, and explain why such a model could still adapt approximately.

   **Answer** Then $\dot m = 0$ fixes $m^* = K_mV_R/(V_B' - V_R)$ independently of $c$, and the adapted activity $a(m^*, c)$ follows the attractant: no adaptation at all. A mixed model, with demethylation of both active and inactive receptors at different rates, has a steady state in which $a$ depends weakly on $c$: approximate adaptation whose precision depends on the ratio of the rates and on the parameters, not robust. Exact adaptation requires that the methylation rate depend on the state only through the output $a$.

10. (Open) Design an experiment to decide whether a eukaryotic cell senses gradients by spatial comparison or by temporal comparison while it moves.

    **Answer** Separate the two cues. Immobilize cells (latrunculin to block actin) in a stable gradient made in a microfluidic device: a polarized response (crescent of PIP₃ or Ras activity facing the source) without movement demonstrates spatial sensing. Conversely, expose motile cells to a spatially uniform concentration that changes in time (flow switching) and measure whether the change biases protrusion or turning; temporal sensing predicts a response to uniform ramps, spatial sensing none beyond the transient of adaptation. Finally, use traveling waves of attractant: *Dictyostelium* moves up the front of a cAMP wave but does not follow it backwards as it passes, which shows that a temporal component (adaptation to rising concentration) is combined with spatial sensing (Nakajima and colleagues, 2014).
