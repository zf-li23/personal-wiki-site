---
title: Hearing
description: "The cochlea as a bank of filters: the Greenwood place–frequency map, gammatone filters and equivalent rectangular bandwidths, resolved and unresolved harmonics; speed of hair-cell transduction and electrical tuning by Ca²⁺ and BK channels; the cochlear amplifier as a Hopf oscillator and the cubic distortion products measured as otoacoustic emissions; phase locking, vector strength and its high-frequency limit, the volley principle; timing synapses of the auditory brainstem; sound localization in the barn owl (delay lines, ITD and ILD pathways, the space map) and in mammals (inhibitory timing in the MSO, the two-channel code and its Fisher information); the auditory cortex and the delay and Doppler maps of echolocating bats; central vestibular computations."
---

Hearing is the fastest of the senses. A barn owl hunting in darkness locates a mouse from interaural time differences of a few microseconds, and a human listener separates a voice from background noise by analyzing frequency components that change within milliseconds. The auditory system achieves this with three specializations that this chapter treats quantitatively: a mechanical frequency analyzer, the cochlea, that is actively amplified by its own receptor cells; a code in the auditory nerve that preserves the phase of sound waves up to several kilohertz; and brainstem circuits built for temporal precision, which compute the direction of a sound by comparing the two ears. The physics of sound, the middle ear, the structure of the cochlea, hair-cell transduction, the cochlear amplifier and the basic facts of sound localization and the vestibular system are covered in [7.14.42](/7.14.42); the gating-spring model and the response of a Hopf oscillator are derived in [7.6.31](/7.6.31#sec-31.5). Here we build on them: the cochlea as a bank of filters, distortion products as a signature of the active process, the limits of phase locking, and the neural computation of sound location, which also provides an example of how the Fisher information of [7.16.26](/7.16.26) decides between rival **population codes**. The bifurcation theory behind the cochlear amplifier is that of [7.16.7](/7.16.7).

## 24.1. The Cochlea as a Filter Bank

### 24.1.1. The Place–Frequency Map

The traveling wave of the basilar membrane peaks at a position that depends on frequency, high frequencies near the base and low frequencies near the apex: the **place principle** ([7.14.42](/7.14.42#def-42.3.3)). The map is approximately logarithmic over most of its length. Greenwood (1990) fitted the characteristic frequency at fractional distance $x$ from the apex ($0 \le x \le 1$) for many species with one formula.

**Formula 24.1.1 (Greenwood Function)** The characteristic frequency of the cochlear partition at fractional distance $x$ from the apex is

$$
f(x) = A\bigl(10^{ax} - k\bigr), \tag{24.1}
$$
with $A = 165.4\,\mathrm{Hz}$, $a = 2.1$ and $k = 0.88$ for the human cochlea (length about $35\,\mathrm{mm}$).

At $x = 0$ the formula gives about $20\,\mathrm{Hz}$ and at $x = 1$ about $20.7\,\mathrm{kHz}$, the limits of human hearing. Away from the apex the constant $k$ is negligible, and each doubling of frequency (an octave) occupies a fixed length $\log_{10}2/a \approx 0.14$ of the cochlea, about $5\,\mathrm{mm}$. The logarithmic map matches the logarithmic perception of pitch: musical intervals are frequency ratios, and an interval corresponds to a fixed distance along the cochlea regardless of the key.

### 24.1.2. Auditory Filters

Each point of the basilar membrane, together with the hair cells and nerve fibers there, responds to a band of frequencies around its characteristic frequency, and the cochlea as a whole acts as a bank of overlapping band-pass filters. Psychophysics measures these filters by masking: a tone is masked by noise only within a limited band around it, the critical band. Physiology measures them as **tuning curves** of auditory nerve fibers. Both are well described by a simple impulse response.

**Definition 24.1.1 (Gammatone Filter)** A linear filter with impulse response

$$
g(t) = t^{n-1}\mathrm{e}^{-2\pi bt}\cos(2\pi f_{\mathrm{c}}t + \varphi), \qquad t \ge 0, \tag{24.2}
$$
a sinusoid of frequency $f_{\mathrm{c}}$ under a gamma-distribution envelope of order $n$ and bandwidth parameter $b$, is called a **gammatone filter**.

With $n = 4$ and $b = 1.019\,\mathrm{ERB}(f_{\mathrm{c}})$, a bank of gammatone filters reproduces the shape of human auditory filters estimated from masking (Patterson et al., 1992). The equivalent rectangular bandwidth (ERB), the width of a rectangular filter that passes the same power of white noise, grows with frequency as

$$
\mathrm{ERB}(f) = 24.7\,\mathrm{Hz}\,\Bigl(4.37\,\frac{f}{1\,\mathrm{kHz}} + 1\Bigr) \tag{24.3}
$$
(Glasberg and Moore, 1990): about $133\,\mathrm{Hz}$ at $1\,\mathrm{kHz}$ and $460\,\mathrm{Hz}$ at $4\,\mathrm{kHz}$. The ratio $f/\mathrm{ERB}$, a quality factor, rises from about 3 at $100\,\mathrm{Hz}$ to about 9 at high frequencies, so the filters are relatively sharper at high frequencies. The gammatone is also the impulse response of a cascade of $n$ identical **resonators**, a crude but useful picture of the many coupled oscillating elements along the cochlea. Its envelope rises and decays within a few cycles at high frequency and lasts much longer at low frequency (panel A of the figure below): a filter with bandwidth $B$ cannot respond faster than about $1/B$, the time–frequency uncertainty of Fourier analysis ([2.5](/2.5)).

The filter bank explains a basic fact of pitch perception. A voiced sound such as a vowel is a harmonic complex, the sum of multiples of a fundamental frequency $F_0$. The spacing $F_0$ between harmonics is constant, while the auditory filters widen with frequency, so the lower harmonics (up to about the eighth) fall into separate filters and are *resolved*, each channel following one sinusoid; the higher harmonics fall together into the same filters, which then respond to their sum, an envelope fluctuating at $F_0$ (panel C). Both cues contribute to pitch; the resolved harmonics give the stronger and more precise sensation, which is why cochlear implants, which stimulate a few broad channels and cannot resolve harmonics, convey speech much better than music.

![The cochlea as a bank of gammatone filters (Eq. (24.2), n = 4, b = 1.019 ERB, Eq. (24.3)). A: impulse responses at 250 Hz, 1 kHz and 4 kHz: the higher the center frequency, the shorter the response. B: gains of 16 filters spaced evenly on the ERB-number scale between 100 Hz and 8 kHz: the bandwidth grows with center frequency. C: output of 48 channels (half-wave rectified, each normalized) to a harmonic complex with fundamental 200 Hz (harmonics 1–40, equal amplitude): channels below about 1.5 kHz resolve single harmonics and follow their waveform, while higher channels receive several harmonics at once and respond with one burst per 5 ms period of the fundamental](./plots/gammatone.py)

## 24.2. Hair-Cell Transduction and Electrical Tuning

Mechanoelectrical transduction in the **hair cell** is direct: the tip links pull on the transduction channels (formed by TMC1 and TMC2, together with accessory proteins), and channels open within microseconds, without second messengers ([7.14.42](/7.14.42#sec-42.3.3)). Direct gating is a requirement, not a detail. A cascade of enzymatic steps, as in phototransduction, takes milliseconds and would act as a low-pass filter that removes everything above a few hundred hertz. Even direct gating cannot follow the highest audible frequencies indefinitely: the hair-cell membrane, with capacitance $C$ and conductance $G$, low-pass filters the receptor potential with corner frequency $G/(2\pi C)$, typically several hundred hertz to about one kilohertz. Above it, the alternating part of the receptor potential shrinks and the hair cell signals increasingly by a steady depolarization, which limits phase locking (Section 24.4).

In many nonmammalian vertebrates the hair cell itself is tuned electrically. Crawford and Fettiplace (1981) found that injecting a current step into a turtle cochlear hair cell produces a damped oscillation of membrane potential at a frequency that matches the cell's acoustic characteristic frequency, between tens and a few hundred hertz along the papilla. The resonance arises from voltage-gated $\ce{Ca^2+}$ channels and $\ce{Ca^2+}$-activated $\ce{K+}$ (BK) channels: depolarization opens $\ce{Ca^2+}$ channels, the entering calcium opens BK channels after a delay, and the resulting outward current repolarizes the cell, overshoots, and lets the calcium channels act again. Linearized around rest, this negative feedback with a delay is equivalent to an inductance in parallel with the membrane capacitance, an electrical LC **resonator**. Cells tuned to higher frequencies have more BK channels with faster kinetics, produced by alternative splicing of the *Slo* gene (Fettiplace and Fuchs, 1999). Mammals, whose hearing extends far beyond the frequencies that such channel kinetics can follow, rely instead on mechanical tuning amplified by outer hair cells.

## 24.3. The Active Cochlea

### 24.3.1. Amplification near a Hopf Bifurcation

The **cochlear amplifier** amplifies weak sounds by $40$–$60\,\mathrm{dB}$ near the characteristic frequency, compresses the response to loud sounds, and sharpens tuning; it is powered by the somatic electromotility of outer hair cells, driven by the motor protein prestin, and in nonmammals by active movements of the hair bundle ([7.14.42](/7.14.42#sec-42.3.4)). All three properties follow from a single assumption: that each segment of the cochlear partition is a dynamical system poised close to a **Hopf bifurcation** (Camalet et al., 2000; Eguíluz et al., 2000; Hudspeth, 2014). Near the bifurcation the dynamics reduce to the normal form

$$
\dot z = (\mu + \mathrm{i}\omega_0)z - \lvert z\rvert^2z + F\mathrm{e}^{\mathrm{i}\omega t}, \tag{24.4}
$$
where $z$ is the complex amplitude of the oscillation, $\omega_0$ the characteristic frequency, $\mu$ the distance from the bifurcation ($\mu < 0$ quiescent, $\mu > 0$ spontaneously oscillating) and $F$ the stimulus. At $\mu = 0$ the steady response at $\omega = \omega_0$ grows as $F^{1/3}$, so that a millionfold range of forces is compressed into a hundredfold range of responses, and the gain is largest for the weakest stimuli and falls off steeply with detuning ([7.6.31](/7.6.31#sec-31.5.2)). Spontaneous otoacoustic emissions, narrow-band sounds emitted by many healthy ears, correspond to segments with $\mu > 0$, whose limit cycles radiate sound back through the middle ear; hair bundles of the frog sacculus held in vitro oscillate spontaneously in the same way.

How the cochlea stays near the bifurcation without crossing it is not settled. One proposal is a feedback that adjusts $\mu$ according to the mean activity, analogous to the adaptation of transduction: if the oscillation grows, calcium entry increases and pushes the bundle back towards quiescence (Camalet et al., 2000). Whatever the mechanism, operating at a critical point trades stability for sensitivity, a recurring design in sensory systems.

### 24.3.2. Distortion Products

A system that compresses is nonlinear, and a nonlinear system driven by two tones responds also at combination frequencies. These distortion products are not an artifact of measurement: they are heard as combination tones (described by Tartini in the eighteenth century) and are emitted by the ear as sounds that can be recorded in the ear canal.

**Proposition 24.3.1 (Cubic Distortion Product)** Let the oscillator of Eq. (24.4) be driven by two weak tones, $F(\mathrm{e}^{\mathrm{i}\omega_1t} + \mathrm{e}^{\mathrm{i}\omega_2t})$, with $\mu < 0$. To lowest order in $F$ the response contains, besides the primaries $z_k\mathrm{e}^{\mathrm{i}\omega_kt}$ with

$$
z_k = \frac{F}{\mathrm{i}(\omega_k - \omega_0) - \mu}, \qquad k = 1, 2,
$$
a component at the cubic distortion frequency $2\omega_1 - \omega_2$ with amplitude

$$
\lvert z_{\mathrm{dp}}\rvert = \frac{\lvert z_1\rvert^2\lvert z_2\rvert}{\bigl\lvert\mathrm{i}(2\omega_1 - \omega_2 - \omega_0) - \mu\bigr\rvert}, \tag{24.5}
$$
and similarly at $2\omega_2 - \omega_1$.

**Proof** Without the cubic term, the steady solution is $z = z_1\mathrm{e}^{\mathrm{i}\omega_1t} + z_2\mathrm{e}^{\mathrm{i}\omega_2t}$, and substituting $z = A\mathrm{e}^{\mathrm{i}\omega t}$ into $\dot z = (\mu + \mathrm{i}\omega_0)z + F\mathrm{e}^{\mathrm{i}\omega t}$ gives the $z_k$. Inserting this solution into $\lvert z\rvert^2z = z\,\bar z\,z$ and collecting terms, the product of $z_1\mathrm{e}^{\mathrm{i}\omega_1t}$ twice with $\bar z_2\mathrm{e}^{-\mathrm{i}\omega_2t}$ oscillates at $2\omega_1 - \omega_2$ with coefficient $z_1^2\bar z_2$. This term acts as an additional forcing $-z_1^2\bar z_2\mathrm{e}^{\mathrm{i}(2\omega_1 - \omega_2)t}$, whose linear response is the stated amplitude. $\square$

Equation (24.5) makes two predictions that are borne out (figure below). For weak stimuli the distortion product grows as the cube of the stimulus level, three times faster in decibels than the primaries. And it is proportional to the cube of the gain of the primaries: an oscillator close to the bifurcation, whose $\lvert z_k\rvert$ is large, produces distortion products orders of magnitude stronger than a damped one. This is why distortion-product otoacoustic emissions at $2f_1 - f_2$, evoked with two tones at a ratio $f_2/f_1 \approx 1.2$, are a sensitive clinical test of outer hair cell function: when the amplifier is damaged by noise or ototoxic drugs, $\mu$ becomes strongly negative and the emission disappears long before the passive mechanics change. At high stimulus levels the perturbation expansion fails and the compressive regime of Eq. (24.4) takes over.

![Distortion products of an active oscillator (Eq. (24.4) in dimensionless units, characteristic frequency 1, primaries at 0.95 and 1.05). A: amplitude spectrum of the response of an oscillator just below the bifurcation (μ = −0.01) to two tones of force 10⁻³: besides the primaries f1 and f2, cubic distortion products appear at 2f1 − f2 and 2f2 − f1 (Proposition 24.3.1). B: amplitude of the primary at f1 (solid) and of the distortion product at 2f1 − f2 (dashed) against stimulus force, for the near-critical oscillator and for a damped one (μ = −0.5): for weak stimuli the primaries grow as F and the distortion products as F³; the near-critical oscillator responds more strongly, compresses at higher forces, and emits a distortion product about a hundred times larger](./plots/distortion-product.py)

## 24.4. Coding in the Auditory Nerve

### 24.4.1. Phase Locking

Each inner hair cell is contacted by 10–20 afferent fibers of the spiral ganglion, which differ in spontaneous rate and threshold and together cover the range of sound levels ([7.14.42](/7.14.42#sec-42.3.5)). Frequency is represented in two ways: by which fibers are active (the place code inherited from the cochlea) and by when they fire. Because the hair cell releases transmitter mainly in the depolarizing half of each cycle, fibers fire preferentially at a particular phase of a low-frequency tone, though not necessarily in every cycle.

**Definition 24.4.1 (Phase Locking and Vector Strength)** The tendency of a neuron to fire at a preferred phase of a periodic stimulus is called **phase locking**. If spikes occur at phases $\theta_1, \dots, \theta_N$ of the stimulus cycle, the length of their mean resultant,

$$
\mathrm{VS} = \Bigl\lvert\frac{1}{N}\sum_{k=1}^{N}\mathrm{e}^{\mathrm{i}\theta_k}\Bigr\rvert, \tag{24.6}
$$
is called the **vector strength** (Goldberg and Brown, 1969); it is 1 when all spikes occur at the same phase and near 0 when phases are uniform.

Phase locking declines with frequency. If spikes fire at the preferred phase with a Gaussian timing jitter of standard deviation $\sigma_t$, the phases have a wrapped normal distribution with angular standard deviation $2\pi f\sigma_t$, and

$$
\mathrm{VS} = \exp\bigl[-\tfrac12(2\pi f\sigma_t)^2\bigr]. \tag{24.7}
$$
Vector strength thus falls to $1/2$ at $f = \sqrt{2\ln 2}/(2\pi\sigma_t)$: for $\sigma_t = 0.1\,\mathrm{ms}$ near $1.9\,\mathrm{kHz}$, for $\sigma_t = 0.05\,\mathrm{ms}$ near $3.7\,\mathrm{kHz}$ (figure below). The measured upper limit of phase locking in the auditory nerve is about $4$–$5\,\mathrm{kHz}$ in the cat (Johnson, 1980) and about $9\,\mathrm{kHz}$ in the barn owl (Köppl, 1997), implying a timing jitter of a few tens of microseconds, set by the membrane filtering of the hair cell and the stochastic release at its ribbon synapse. In humans the limit cannot be recorded directly and is debated.

A single fiber cannot fire at every cycle of a $2\,\mathrm{kHz}$ tone, because its refractory period is about $1\,\mathrm{ms}$. The population can still represent the period: different fibers fire on different cycles, each at the preferred phase, so that their pooled activity marks every cycle. This is the volley principle of Wever and Bray (1930). Temporal coding gives frequency discrimination at low frequencies its precision, a few hertz at $1\,\mathrm{kHz}$, much finer than the bandwidth of the auditory filters, and provides the timing on which sound localization depends.

![Phase locking of a model auditory nerve fiber (one spike in 30 % of cycles at a fixed preferred phase plus Gaussian jitter). A: period histograms (spike phases within the stimulus cycle) at 300 Hz, 1 kHz and 3 kHz for a jitter of 0.1 ms, with the vector strength (Eq. (24.6)): the same absolute jitter is a growing fraction of the shorter cycles. B: vector strength against frequency for jitters of 0.05, 0.1 and 0.2 ms; points from simulation, lines Eq. (24.7)](./plots/phase-locking.py)

### 24.4.2. Brainstem Synapses Built for Timing

Every auditory nerve fiber branches to the three divisions of the ipsilateral cochlear nucleus, where distinct **cell types** extract different features of the input:

| Cell type | Input | Response | Information carried |
|---|---|---|---|
| Bushy cell (anteroventral nucleus) | 1–3 giant endbulbs of Held from fibers of one characteristic frequency | follows the phase of the input, often more precisely than the fibers | timing and phase, to the superior olive |
| Stellate (multipolar) cell | many small boutons | regular "chopper" firing, rate grows with level | spectral shape, intensity |
| Octopus cell (posteroventral nucleus) | many fibers of a broad range of frequencies | fires once at stimulus onset, with very small jitter | onsets, broadband transients |
| Fusiform cell (dorsal nucleus) | auditory nerve and multisensory input | complex, inhibited at some frequencies | spectral notches produced by the pinna, elevation |

The neurons of the timing pathway share a set of adaptations. Their large synapses (the endbulb of Held on bushy cells, the calyx of Held on cells of the medial nucleus of the trapezoid body) release many vesicles at once and drive the postsynaptic cell above threshold with a single presynaptic spike. Their **AMPA receptors** contain GluA3 and GluA4 subunits with submillisecond kinetics. And they express low-threshold $\mathrm{K_V1}$ channels that are partly open at rest, giving a **membrane time constant** below $1\,\mathrm{ms}$ instead of the $10$–$20\,\mathrm{ms}$ typical of cortical neurons, together with high-threshold $\mathrm{K_V3}$ channels that make action potentials brief. A short time constant means that inputs are not summed over time: the cell fires only to inputs that arrive nearly together, which turns it into a **coincidence detector**, the computation needed in the superior olive.

## 24.5. Sound Localization

### 24.5.1. The Barn Owl

The barn owl can strike prey in complete darkness guided by sound alone, with an accuracy of $1$–$2^\circ$ in both azimuth and elevation (Konishi, 1973). Its two ears are asymmetric, the left opening higher than the right, so that the **interaural level difference** (ILD) at high frequencies varies with elevation, while the **interaural time difference** (ITD) varies with azimuth ([7.14.42](/7.14.42#def-42.4.1)). The two cues are processed in parallel pathways (Konishi, 2003):

1. ITD: the cochlear nucleus magnocellularis preserves the phase of the input; its axons from the two sides enter the nucleus laminaris from opposite directions and act as delay lines, and laminaris neurons are **coincidence detectors** whose best ITD depends on their position (Carr and Konishi, 1990).
2. ILD: the cochlear nucleus angularis encodes intensity, and the dorsal nucleus of the posterior lateral lemniscus compares the two sides.
3. The two pathways converge in the external nucleus of the inferior colliculus, whose neurons respond only to sound from a restricted region of space. They form a map of auditory space, with azimuth and elevation represented along two axes (Knudsen and Konishi, 1978), and this map projects to the optic tectum, where it is aligned with the visual map.

Two computations in this pathway have been analyzed quantitatively. First, laminaris neurons are ambiguous for pure tones: a detector tuned to ITD $\Delta$ also responds to $\Delta \pm 1/f$. In the inferior colliculus, neurons combine many frequency channels; the true ITD is the only one at which all channels agree, so the side peaks cancel and a single peak remains. Second, space-specific neurons combine ITD and ILD multiplicatively rather than additively: their subthreshold responses to combinations are well fitted by the product of the ITD and ILD **tuning curves** (Peña and Konishi, 2001), which makes the neuron respond sharply to one location instead of to a cross-shaped region. The alignment of the auditory map with the visual map is learned; owls raised with prisms that shift the visual field shift their auditory map to match (Knudsen and Brainard, 1991), a form of supervised plasticity in which vision calibrates hearing.

### 24.5.2. The Jeffress Model

**Definition 24.5.1 (Jeffress Model)** The model of ITD computation in which the inputs from the two ears reach an array of coincidence-detecting neurons through delay lines of systematically varying length, so that each detector fires maximally when the acoustic ITD is compensated by its internal delay and the position of the most active detector represents the azimuth of the sound, is called the **Jeffress model** (Jeffress, 1948).

In signal-processing terms, the array computes the cross-correlation of the two ears' signals. Let the sound reach the left ear at time $t$ and the right ear at $t + \Delta$, and let detector $j$ receive the left input with delay $d_j^{\mathrm{L}}$ and the right input with delay $d_j^{\mathrm{R}}$. If the detector's rate is proportional to the product of its inputs averaged over time, it is

$$
r_j \propto \int x_{\mathrm{L}}(t - d_j^{\mathrm{L}})\,x_{\mathrm{R}}(t - d_j^{\mathrm{R}})\,\mathrm{d}t = C\bigl(\Delta - (d_j^{\mathrm{L}} - d_j^{\mathrm{R}})\bigr), \tag{24.8}
$$
where $x_{\mathrm{L}}, x_{\mathrm{R}}$ are the band-pass filtered, rectified signals of a frequency channel and $C$ their cross-correlation function, which peaks at zero lag. The detector tuned to $d_j^{\mathrm{L}} - d_j^{\mathrm{R}} = \Delta$ responds best: a place code for ITD. For a narrow-band channel, $C$ oscillates at the center frequency, which is the origin of the phase ambiguity discussed above. The owl's nucleus laminaris fits the model closely; the response of an array of such detectors to tones is shown in [7.14.42](/7.14.42#sec-42.4.3).

### 24.5.3. Mammals: Inhibitory Timing and the Two-Channel Code

In mammals the ITD is computed in the medial superior olive (MSO), whose bipolar neurons receive excitation from the bushy cells of both sides on their two dendrites. For many years the MSO was assumed to be a Jeffress array. Recordings in the gerbil (Brand et al., 2002) showed something different. The best ITDs of MSO neurons were not spread across the physiological range but clustered at an interaural phase difference of about $\pi/4$ favoring the contralateral ear, which at low frequencies lies outside the range of ITDs that a gerbil's small head can produce (about $\pm 135\,\mu\mathrm{s}$). Blocking glycinergic inhibition, which reaches the MSO from the medial and lateral nuclei of the trapezoid body with precise timing, shifted the best ITD towards zero, showing that inhibition, not only axonal delay, sets the tuning.

With best ITDs outside the physiological range, the steep flanks of the tuning curves, not their peaks, fall within it. ITD can then be read out by comparing the summed activity of the two MSOs, a two-channel or hemispheric code (McAlpine et al., 2001). The Fisher information of [7.16.26](/7.16.26) makes the comparison precise. For independent Poisson neurons with tuning curves $r_j(\Delta)$ observed for a time $T$, the **Fisher information** about $\Delta$ is

$$
I_{\mathrm{F}}(\Delta) = T\sum_j\frac{r_j'(\Delta)^2}{r_j(\Delta)}, \tag{24.9}
$$
and by the **Cramér–Rao inequality** no unbiased estimator can have a standard deviation smaller than $I_{\mathrm{F}}^{-1/2}$. Each neuron contributes most where its tuning curve is steepest. A place code with peaks inside the range places many neurons at their peaks, where they contribute nothing, near the midline; a two-channel code places the flanks of all neurons at the midline, where behavioral acuity is highest (figure below). Harper and McAlpine (2004) showed that the optimal arrangement depends on head size and frequency: for small heads and low frequencies the period is long compared with the physiological range and two channels are optimal, whereas for large heads or high frequencies (as in the barn owl, whose ITD range is about $\pm 200\,\mu\mathrm{s}$ and which phase-locks up to $9\,\mathrm{kHz}$) best ITDs should be distributed within the range, as in a Jeffress array. The two designs are then not rival theories but two solutions of the same optimization.

![Two codes for interaural time difference in a small mammal (500 Hz tone, physiological range ±135 μs shaded; tuning r = r0 + r1 exp(κ(cos 2πf(ITD − d) − 1)), r0 = 5 Hz, r1 = 100 Hz, κ = 1.5). A: a place code of 20 neurons with best delays spread over the physiological range (thin lines, some shown), and the two channels of a hemispheric code with best ITDs of ±250 μs (phase ±π/4), outside the range. B: the difference between the mean rates of the two channels varies monotonically across the physiological range. C: the Cramér–Rao bound, from the Fisher information (Eq. (24.9)) of 20 independent Poisson neurons counted for 100 ms: the two-channel code is most precise near the midline, where the place code is least precise](./plots/itd-codes.py)

The interaural level difference is computed in the lateral superior olive, which receives excitation from the ipsilateral cochlear nucleus and inhibition from the contralateral ear via the medial nucleus of the trapezoid body, whose calyx of Held synapse converts excitation into inhibition with minimal delay; its output, a sigmoid function of ILD, is again a two-channel code for high frequencies.

## 24.6. Auditory Cortex and Echolocation

The primary auditory cortex is tonotopic, but its neurons respond to far more than the frequency of a tone: to bandwidth, to the direction and rate of frequency sweeps, to amplitude modulation, to combinations of frequencies and to the timing between sounds. A compact description is the spectrotemporal receptive field, the linear filter in time and frequency obtained by reverse correlation with rich sounds (the method of [7.16.16](/7.16.16) applied to a spectrogram). Higher auditory areas respond to increasingly complex sounds, conspecific vocalizations in marmosets and birds, and speech and music in the superior temporal cortex of humans ([7.16.49](/7.16.49)).

The clearest example of a computational map in auditory cortex comes from echolocating bats (Suga, 1990). The mustached bat emits pulses with a long constant-frequency (CF) component, whose second harmonic near $61\,\mathrm{kHz}$ is the strongest, followed by a short downward frequency-modulated (FM) sweep. Two physical relations turn echoes into information about the target:

- Range from delay: an echo returning after a delay $\Delta t$ comes from a target at distance $D = c\,\Delta t/2$; with $c = 343\,\mathrm{m\,s^{-1}}$, each millisecond of delay is $17\,\mathrm{cm}$.
- Velocity from Doppler shift: a target approaching at relative speed $v \ll c$ returns the CF component shifted by $\Delta f \approx 2vf/c$, about $356\,\mathrm{Hz}$ per $\mathrm{m\,s^{-1}}$ at $61\,\mathrm{kHz}$.

In the FM–FM area, neurons respond weakly to a pulse or an echo alone but strongly to an echo that follows the pulse at a particular "best delay", and best delays are mapped systematically along the cortex from about $0.4$ to $18\,\mathrm{ms}$, a map of target range from about $7\,\mathrm{cm}$ to $3\,\mathrm{m}$. In the CF–CF area, neurons respond to combinations of the emitted CF and the Doppler-shifted echo, forming a map of relative velocity. The frequencies around $61\,\mathrm{kHz}$ occupy a disproportionate part of the tonotopic map, an "acoustic fovea", and the bat lowers the frequency of its calls as it approaches a target so that the echo always returns in this range (Doppler-shift compensation). These delay-tuned neurons are built by **coincidence detection** between a delayed response to the pulse and a response to the echo, the same principle as in the Jeffress model on a time scale a thousand times longer.

**Example 24.6.1** A bat flying at $5\,\mathrm{m\,s^{-1}}$ towards a moth $1.2\,\mathrm{m}$ away, which itself moves away at $1\,\mathrm{m\,s^{-1}}$, emits a CF call at $61.0\,\mathrm{kHz}$. The echo delay is $2D/c = 2.4/343\,\mathrm{s} = 7.0\,\mathrm{ms}$, and the relative approach speed is $4\,\mathrm{m\,s^{-1}}$, so the echo returns about $2\times4\times61\,000/343 \approx 1.4\,\mathrm{kHz}$ higher, at $62.4\,\mathrm{kHz}$. To keep the echo at $61\,\mathrm{kHz}$, the bat must lower its call to about $59.6\,\mathrm{kHz}$. The delay is read out by FM–FM neurons with best delay near $7\,\mathrm{ms}$, the speed by CF–CF neurons.

:::

## 24.7. Central Vestibular Computations

The semicircular canals and otolith organs share the hair cells of the cochlea and their transduction machinery; the mechanics of the canals (a torsion pendulum that reports angular velocity over the band of natural head movements) and the vestibular reflexes are covered in [7.14.42](/7.14.42#sec-42.5). Two central computations deserve emphasis because they are examples of the internal models of [7.16.29](/7.16.29). First, the otolith organs cannot distinguish tilt of the head from linear acceleration, since both shear the otolithic membrane in the same way (the equivalence principle). Neurons in the vestibular nuclei and the cerebellar nodulus and uvula resolve the ambiguity by combining otolith signals with an estimate of head orientation obtained by integrating the angular velocity reported by the canals: their responses encode translation even when the otolith signal alone is ambiguous (Angelaki et al., 2004). Second, the vestibulo-ocular reflex needs eye position, which is the time integral of the velocity signal the canals provide; this integration is performed by recurrent circuits in the brainstem, the neural **integrator** analyzed in [7.16.33](/7.16.33), whose gain is calibrated by the cerebellum.

## Summary

- The cochlea maps frequency onto position approximately logarithmically (Formula 24.1.1). Each place acts as a band-pass filter well described by a gammatone (Definition 24.1.1), whose bandwidth grows with frequency (Eq. (24.3)); low harmonics of a voice are resolved, high harmonics are not.
- Hair-cell transduction is fast because gating is direct; the membrane low-pass filter limits the alternating receptor potential at high frequencies. Many nonmammals tune hair cells electrically with $\ce{Ca^2+}$ and BK channels.
- The cochlear amplifier behaves as a set of oscillators near a Hopf bifurcation (Eq. (24.4)): high gain, compression and sharp tuning, spontaneous emissions for $\mu > 0$. Its cubic nonlinearity produces distortion products whose amplitude scales with the cube of the primary gain (Proposition 24.3.1), the basis of a clinical test of outer hair cells.
- Auditory nerve fibers phase-lock (Definition 24.4.1). Timing jitter $\sigma_t$ limits vector strength as Eq. (24.7), so locking fades at a few kilohertz; the volley principle lets a population mark every cycle. Brainstem timing neurons use giant synapses, fast AMPA receptors and low-threshold $\mathrm{K_V1}$ channels to act as coincidence detectors.
- The barn owl computes ITD with delay lines and coincidence detectors (Definition 24.5.1; a cross-correlation, Eq. (24.8)), ILD in a parallel pathway, and combines them multiplicatively into a map of auditory space calibrated by vision.
- Small mammals use inhibition-tuned MSO neurons with best ITDs outside the physiological range and a two-channel code; Fisher information (Eq. (24.9)) shows that this code is optimal for small heads and low frequencies, while a place code is optimal for large heads or high frequencies.
- Auditory cortex represents complex sound features; bats build computational maps of target range ($D = c\Delta t/2$) and velocity (Doppler shift $2vf/c$) by coincidence of pulse and echo responses.
- Central vestibular circuits resolve the tilt–translation ambiguity with internal models and integrate velocity into eye position.

## Questions

1. Using Eq. (24.1), how far apart along the human cochlea are the places tuned to $440\,\mathrm{Hz}$ and $880\,\mathrm{Hz}$? Compare with the width of one auditory filter at $440\,\mathrm{Hz}$ expressed as a length.

   **Answer** Solving $f = A(10^{ax} - k)$ for $x$: $x = \log_{10}(f/A + k)/a$. For $440\,\mathrm{Hz}$, $f/A + k = 2.660 + 0.88 = 3.540$, $x = 0.549/2.1 = 0.2614$; for $880\,\mathrm{Hz}$, $5.320 + 0.88 = 6.200$, $x = 0.792/2.1 = 0.3774$. The difference is $0.116$ of $35\,\mathrm{mm}$, about $4.1\,\mathrm{mm}$ (less than the high-frequency value of $5\,\mathrm{mm}$ because of the constant $k$). The ERB at $440\,\mathrm{Hz}$ is $24.7(4.37\times0.44 + 1) \approx 72\,\mathrm{Hz}$; near $440\,\mathrm{Hz}$, $\mathrm{d}x/\mathrm{d}f = 1/[a\ln 10\,(f + Ak)] = 1/(4.835\times585.6\,\mathrm{Hz}) \approx 3.5\times10^{-4}\,\mathrm{Hz^{-1}}$, so one ERB spans $0.025$ of the cochlea, about $0.9\,\mathrm{mm}$. An octave thus contains roughly four to five auditory filters at this frequency.
2. Show from Proposition 24.3.1 that, for weak stimuli, the level of the distortion product in decibels grows three times as fast as the stimulus level, and explain why the ratio $f_2/f_1$ is kept near $1.2$ in clinical tests.

   **Answer** The $z_k$ are proportional to $F$, so $\lvert z_{\mathrm{dp}}\rvert \propto F^3$ and $20\log_{10}\lvert z_{\mathrm{dp}}\rvert = 3\times20\log_{10}F + \text{const}$: a $10\,\mathrm{dB}$ increase of both primaries raises the distortion product by $30\,\mathrm{dB}$. The amplitude contains $\lvert z_1\rvert^2\lvert z_2\rvert$, which is large only if both primaries are close to the characteristic frequency of the same generating region; if $f_2/f_1$ is too large, the two tones excite different places and $z_1z_2$ at either place is small, so the emission weakens. If the ratio is too close to 1, the distortion product is close in frequency to the primaries and hard to separate from them in the recorded sound. Ratios near $1.2$ maximize the emission in practice.
3. A fiber phase-locks with vector strength $0.5$ to a $2\,\mathrm{kHz}$ tone. What timing jitter does Eq. (24.7) imply? Why can phase locking still be useful for ITD coding when the vector strength is low?

   **Answer** $\exp[-\frac12(2\pi f\sigma_t)^2] = 0.5$ gives $2\pi f\sigma_t = \sqrt{2\ln 2} = 1.177$, so $\sigma_t = 1.177/(2\pi\times2000)\,\mathrm{s} \approx 94\,\mu\mathrm{s}$. Even with this jitter, the mean phase is well defined, and a detector that pools many fibers and many cycles can estimate the mean phase with an error that decreases as $1/\sqrt{N}$ with the number of spikes $N$. **Coincidence detectors** in the MSO or nucleus laminaris receive many inputs and integrate over many cycles, so a weak locking of each fiber still yields a precise population estimate, which is how ITDs of $10$–$20\,\mu\mathrm{s}$ can be resolved with spikes jittered by tens of microseconds.
4. Why does the Fisher information of a neuron with **tuning curve** $r(\Delta)$ vanish at the peak of the curve? What does this imply for the claim that "the most active neuron signals the stimulus"?

   **Answer** By Eq. (24.9), each neuron contributes $T r'(\Delta)^2/r(\Delta)$, and $r' = 0$ at the peak, so small changes of $\Delta$ near the peak do not change the expected count and cannot be detected from it. The most active neuron therefore says that the stimulus is near its preferred value, but its rate is useless for fine discrimination around that value; fine discrimination relies on neurons whose flanks pass through the stimulus. Decoding by the identity of the most active neuron (winner-take-all) is coarse; optimal decoders use the whole population, weighted by the slopes of the tuning curves ([7.16.26](/7.16.26)).
5. (Open question) Design a population model that would let a bat's FM–FM neuron respond best to an echo delayed by $5\,\mathrm{ms}$ after the pulse. What cellular mechanisms could produce the delay?

   **Answer** A coincidence detector needs two inputs that arrive together when the echo follows the pulse by $5\,\mathrm{ms}$: a response to the pulse (FM1, the first harmonic sweep, which is strong in the emitted call) delayed by $5\,\mathrm{ms}$, and an undelayed response to the echo's higher harmonic (FM2–FM4). A multiplicative or thresholded combination of the two then fires only near the right delay, $r \propto \int x_{\mathrm{pulse}}(t - 5\,\mathrm{ms})x_{\mathrm{echo}}(t)\,\mathrm{d}t$, a cross-correlation as in Eq. (24.8). Axonal delays are far too short for milliseconds; plausible mechanisms are a delayed rebound after inhibition (postinhibitory rebound firing after an inhibitory response to the pulse, observed in the inferior colliculus and nuclei of the lateral lemniscus), slow synaptic kinetics, or latency differences between low- and high-threshold neurons. A map of best delays results if the delay varies systematically across neurons, for example by a gradient of inhibitory duration.
