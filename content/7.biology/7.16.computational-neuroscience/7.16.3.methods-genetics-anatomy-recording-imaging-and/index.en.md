---
title: "Methods: Genetics, Anatomy, Recording, Imaging and Manipulation"
description: "The toolkit of modern neuroscience and the models needed to interpret its data: model organisms and genetic access to cell types; sparse labeling, tracing and electron-microscopic connectomics; extracellular recording and spike sorting, patch clamp; calcium imaging with its convolution model and deconvolution, two-photon imaging; fMRI, the BOLD signal and the hemodynamic response function, EEG, MEG and PET; optogenetic and chemogenetic control; quantitative behavior."
---

Every conclusion in neuroscience rests on a method, and every method measures something other than what we want to know. An extracellular electrode records voltage deflections from several nearby neurons, not spike trains of identified cells; a calcium indicator reports a slow, nonlinear function of spiking; the fMRI signal reflects blood oxygenation seconds after the neural activity that caused it. This chapter surveys the main methods and, for each measurement, the quantitative model that links what is measured to the neural variable of interest. The logic of observation and perturbation, and the scales covered by each method, were introduced in [7.16.1](/7.16.1#sec-1.6).

The molecular tools (transgenes, genome editing, fluorescent proteins) are treated in [molecular biology](/7.2) and [genetics](/7.4); patch clamp and single-channel analysis in [7.6.30](/7.6.30#sec-30.2.3). The statistical methods used below (principal component analysis, clustering, mixture models, deconvolution as a regularized regression, the general linear model) come from [statistics](/3.4) and are linked where they are used.

## 3.1. Genetic Access to Neurons

Genetics is used in neuroscience in two ways: to find the genes that a behavior or a structure depends on, and to gain access to specific cell types in order to label, record or manipulate them.

The **model organisms** of neuroscience were chosen for complementary strengths. The nematode *Caenorhabditis elegans* has 302 neurons with a known connectome and an invariant lineage; the fruit fly *Drosophila melanogaster* has about $10^5$ brain neurons, a rich behavioral repertoire and the most extensive genetic toolkit; the zebrafish larva is transparent, so that activity in the whole brain can be imaged; the mouse is the main mammalian genetic model; and macaque monkeys are used where behavior and brain organization close to those of humans are essential.

**Forward genetics** starts from a phenotype: mutagenize, screen for animals with a defect in a behavior (Benzer's screens in *Drosophila* found the clock gene *period*, and the same strategy yielded the learning mutants *dunce*, from Benzer's laboratory, and *rutabaga*, from Quinn's), then identify the mutated gene. **Reverse genetics** starts from a gene and asks what its loss does, by knockout, knock-in or targeted mutation ([7.4](/7.4)).

Because most genes are used in many cells and at many times, whole-animal knockouts are often uninterpretable. Site-specific recombinases restrict a genetic change to chosen cells and times.

**Definition 3.1.1 (Recombinase-Based Genetic Access)** In the **Cre/loxP** system the recombinase Cre excises or inverts a DNA segment flanked by two loxP sites. Expressing Cre from a cell-type-specific promoter (a *driver line*) and placing a gene or a reporter under loxP control (a *responder*) restricts the genetic change to the cells, and with a ligand-dependent Cre (CreER, activated by tamoxifen) to the time, chosen by the experimenter. In an **intersectional strategy** two recombinases (such as Cre and Flp) are driven by two different promoters and the responder requires both, so that only cells in the intersection of two expression patterns are targeted.

A **conditional knockout** removes a gene only in Cre-expressing cells. In *Drosophila* the binary **GAL4/UAS system** plays the role of driver and responder, with thousands of driver lines covering small subsets of neurons. Recombinase-dependent reporters delivered locally add spatial specificity, and labels transported from axon terminals back to the soma define cells by their projection target, the fourth criterion of a cell type ([7.16.2](/7.16.2#sec-2.1)).

## 3.2. Anatomy: From Single Neurons to Connectomes

Anatomy determines which cells can communicate with which; methods differ in what they label and at what resolution.


- *Sparse labeling.* The Golgi stain labels a few percent of neurons at random; genetic sparse-labeling methods (MARCM in flies, Brainbow in mice) label single neurons of defined types, and whole-brain imaging of such neurons has reconstructed complete axons that branch over much of the brain.
- *Tracing.* Tracers injected at one site are transported along axons, anterogradely (from the cell body to the terminals) or retrogradely (from the terminals to the cell body), and so reveal which regions project to which. Certain viruses spread across synapses in only one direction and mark the neurons directly presynaptic or postsynaptic to a starting population, which turns the question "who talks to whom" into a labeling experiment with cellular resolution.
- *Light microscopy of whole brains.* Tissue clearing renders the brain transparent, and light-sheet or serial two-photon microscopy images it block by block; registered to a common atlas, the images allow cell positions, projections and gene expression to be compared across animals.
- *Electron microscopy.* Light microscopy cannot resolve synapses reliably (a spine neck is 50–100 nm thin, the synaptic cleft 20–30 nm). Serial-section electron microscopy images tissue at about $4 \times 4 \times 40\,\mathrm{nm}$ per voxel, so that every axon and dendrite can be followed through the volume and every synapse located.

**Definition 3.2.1 (Connectome)** A **connectome** is the complete map of the connections of a nervous system or a part of it: a directed graph whose vertices are neurons and whose weighted edges are synaptic connections, usually with the number of synapses (or their size) as the weight.

The connectome of *C. elegans* (302 neurons, about 7000 chemical synapses) was obtained by hand-tracing in the 1980s; the adult *Drosophila* brain (about $1.4 \times 10^5$ neurons and $5 \times 10^7$ synapses) was completed in 2024, and a cubic millimeter of mouse visual cortex (about $10^5$ neurons and $5 \times 10^8$ synapses) was reconstructed in 2025. The scale is set by data volume and proofreading, not by imaging: one cubic millimeter at the resolution above is about $10^{15}$ voxels, a petabyte-scale dataset, and automated segmentation must be corrected by humans because a single merge error joins two neurons into one. A connectome constrains models: it fixes which $w_{ij}$ in a rate model ([7.16.2](/7.16.2#sec-2.3)) are nonzero and reveals motifs, but it does not give the sign or strength of a synapse, the transmitter, the dynamics, or the neuromodulatory context, which must come from other measurements.

## 3.3. Electrophysiology: Recording the Electrical Activity of Neurons

Electrophysiology measures the electrical signals of neurons directly, with a time resolution of a fraction of a millisecond. It comes in two families, depending on whether the electrode is inside or outside the cell.

*Intracellular and whole-cell recording.* A sharp glass micropipette or a patch pipette in the whole-cell configuration measures the membrane potential $V$ of one cell (current clamp) or the membrane current at a fixed $V$ (voltage clamp). **Patch clamp** gives access to subthreshold events, synaptic potentials and the currents of single channels ([7.6.30](/7.6.30#sec-30.2.3)); the whole-cell recording is the standard for characterizing the intrinsic properties of the cell types in [7.16.2](/7.16.2#sec-2.1). Its limits are throughput (one to a few cells at a time, in slices or in head-fixed animals), the dialysis of the cytoplasm by the pipette solution, and stability over hours.

*Extracellular recording.* An electrode in the tissue records the potential generated by the transmembrane currents of nearby cells. The tissue is a conductor, and for a current $I$ leaving a small membrane patch the potential at distance $d$ is that of a point source in a medium of conductivity $\sigma \approx 0.3\,\mathrm{S\,m^{-1}}$,

$$
\phi(d) = \frac{I}{4\pi\sigma d}.
$$

The potential decays as $1/d$, so a spike is large only near the cell. With a peak amplitude of $300\,\mathrm{\mu V}$ at $20\,\mathrm{\mu m}$ and a noise standard deviation of $15\,\mathrm{\mu V}$, a spike is detectable at the usual threshold of $4.5$ noise standard deviations up to $d \approx 90\,\mathrm{\mu m}$ (Figure 1A). Because the number of neurons within distance $d$ grows as $d^3$, an electrode in cortex, which contains about $9 \times 10^4$ neurons per cubic millimeter, has some 270 neurons within that radius, of which only the active ones near the tip give separable spikes (Figure 1B). The recorded signal is therefore a mixture: the high-frequency band (above about 300 Hz) contains spikes of a few neurons, while the low-frequency band (below about 300 Hz) is the local field potential (LFP), the summed synaptic and other slow currents of thousands of neurons. Dense silicon probes with hundreds of recording sites along a shank (Neuropixels) record from many neurons simultaneously across brain regions, and the algorithms below assign each spike to its neuron.

![What an extracellular electrode records. A: the spike amplitude of one neuron falls as $1/d$ with distance from the neuron; the detection (4.5 σ) and sorting (8 σ) thresholds define radii of about 90 and 50 µm. B: the number of neurons within distance $d$ at the density of mouse cortex; about 270 neurons lie within the detection radius and 50 within the radius at which spikes are large enough to be sorted](./plots/recording-volume.py)

The problem of *spike sorting* is to turn the continuous voltage into the spike trains of single neurons. Each neuron produces a stereotyped waveform on each channel, with an amplitude that depends on its position relative to the electrode; the waveforms of different neurons differ, so they can be grouped. The procedure is a pipeline of standard statistical steps ([3.4](/3.4), [3.5](/3.5)).

**Algorithm 3.3.1 (Spike Sorting)** Input: the multichannel voltage $x_c(t)$, band-pass filtered at 300–6000 Hz.

1. *Detection.* Estimate the noise scale robustly as $\hat\sigma = \operatorname{median}(\lvert x\rvert)/0.6745$ (the median is insensitive to the spikes, which occupy a small fraction of samples, and $0.6745$ is the median of $\lvert Z\rvert$ for $Z \sim \mathcal{N}(0,1)$). Mark every downward threshold crossing $x_c < -4.5\hat\sigma$ and cut a window of about 3 ms around the peak.
2. *Features.* Stack the windows into the matrix $W \in \mathbb{R}^{n_{\mathrm{spikes}} \times (n_{\mathrm{channels}} n_{\mathrm{samples}})}$, subtract the mean, and project on the first few principal components of $W$, which capture most of the variance between waveform shapes (principal component analysis, computed by the singular value decomposition).
3. *Clustering.* Fit a **Gaussian mixture model** with $K$ components to the features with the **EM algorithm**: the E-step computes the responsibilities $\gamma_{ik} = \pi_k\mathcal{N}(\boldsymbol{f}_i \mid \boldsymbol{\mu}_k, \Sigma_k)/\sum_l \pi_l \mathcal{N}(\boldsymbol{f}_i \mid \boldsymbol{\mu}_l, \Sigma_l)$ of cluster $k$ for spike $i$, the M-step updates the weights, means and covariances; $K$ is chosen by a model-selection criterion or by merging and splitting clusters manually.
4. *Validation.* A cluster is accepted as a single unit if its waveform is consistent, if its isolation from other clusters is high, and if its spike train has an empty refractory period: the autocorrelogram must show almost no intervals shorter than 2 ms.

Figure 2 applies the algorithm to a synthetic recording of three neurons with different amplitude profiles on four channels. Three clusters appear in the plane of the first two principal components, the cluster templates reproduce the waveforms, and the autocorrelogram of the first cluster has the empty gap at short lags that identifies a single neuron. The remaining difficulties are real: spikes of different neurons overlap in time, waveforms change with electrode drift and bursting (the amplitude of successive spikes in a burst declines), and neurons far from the electrode produce spikes that are indistinguishable from noise. Consequently a "unit" in a recording is often a *multi-unit* signal, and the quality of sorting is reported with metrics such as the fraction of refractory-period violations.

![Spike sorting on a synthetic recording of three neurons on four channels. A: a stretch of one channel with the detection threshold. B: the detected waveforms projected on their first two principal components, colored by the cluster found with a Gaussian mixture model. C: the mean waveform of each cluster on the four channels. D: autocorrelogram of cluster 1; the empty bins at lags below 2 ms show refractoriness, the signature of a single neuron](./plots/spike-sorting.py)

## 3.4. Optical Methods: Imaging Activity

Light allows a field of view of hundreds of micrometers to millimeters to be monitored with cellular resolution and, with genetic targeting, with cell-type specificity. The price is that the indicator is a molecular reporter with its own dynamics.

**Definition 3.4.1 (Calcium Imaging)** In **calcium imaging** the fluorescence of a **genetically encoded calcium indicator** (such as GCaMP, a fusion of green fluorescent protein with calmodulin) is recorded as a proxy of the intracellular $\ce{Ca^2+}$ concentration, which rises by about $10^2$–$10^3\,\mathrm{nM}$ with each action potential because voltage-gated $\ce{Ca^2+}$ channels open during the spike.

The relation between spikes and fluorescence can be written as a convolution. Let $s(t) = \sum_k \delta(t - t_k)$ be the spike train. Each spike increments the calcium concentration by a fixed amount, which then decays with the time constant $\tau_{\mathrm{Ca}}$ of buffering and extrusion; the fluorescence is a (nonlinear) function of calcium. In the linear regime

$$
c(t) = \int_0^\infty \mathrm{e}^{-t'/\tau_{\mathrm{Ca}}}\,s(t - t')\,\mathrm{d}t',
\qquad
F(t) = F_0\bigl[1 + a\,c(t)\bigr] + \varepsilon(t),
$$

and the imaging quantity is $\Delta F/F_0 = a\,c(t) + \varepsilon(t)/F_0$, with $\varepsilon$ Gaussian noise. Sampled at the frame interval $\Delta t$ the same model is a first-order autoregressive process,

$$
c_t = \gamma\,c_{t-1} + s_t, \qquad \gamma = \mathrm{e}^{-\Delta t/\tau_{\mathrm{Ca}}},
$$

with nonnegative integer $s_t$. For the indicator GCaMP6f, $\tau_{\mathrm{Ca}}$ is a few hundred milliseconds; for the slower and more sensitive GCaMP6s it is about a second. The model has two consequences. A single imaging frame does not tell when a spike occurred: events closer than $\tau_{\mathrm{Ca}}$ fuse, so the effective temporal resolution is 50–500 ms rather than the 1 ms of electrophysiology. And $\Delta F/F_0$ is a nonlinear, saturating function of the spike rate, because the indicator binds $\ce{Ca^2+}$ cooperatively (a Hill function with exponent about 2.5), so that single spikes are barely visible in some indicators while bursts saturate.

Inverting the model (deconvolution) estimates $s$ from the measured $F$. The convolution acts as a low-pass filter, so naive inversion amplifies noise; the standard solution is the regularized, nonnegative least-squares problem

$$
\hat{\boldsymbol{s}} = \operatorname*{arg\,min}_{\boldsymbol{s} \ge 0}\;\tfrac12\,\lVert \boldsymbol{y} - a K\boldsymbol{s}\rVert^2 + \lambda\lVert \boldsymbol{s}\rVert_1,
$$

where $\boldsymbol{y}$ is the normalized fluorescence and $K$ the lower-triangular Toeplitz matrix with entries $\gamma^{i-j}$. The $\ell_1$ penalty (as in the Lasso, [3.4](/3.4)) favors sparse spike trains and the constraint $s \ge 0$ forbids negative spikes; the problem is convex and is solved efficiently, with a fast pool-adjacent-violators algorithm for the AR(1) case. Figure 3B shows the result: spike times are recovered to within a frame or two and counts within bursts are underestimated, and the estimate is a spike *rate* more than a spike train.

**Two-photon microscopy** makes calcium imaging possible in scattering tissue. A pulsed infrared laser focused in the sample excites the fluorophore only where two photons arrive nearly simultaneously. Because the excitation probability is proportional to $I^2$ and the intensity of a focused beam falls as the square of the distance from the focus, excitation is confined to a femtoliter volume; infrared light scatters less than visible light, and imaging reaches depths of 500–800 µm in cortex. The scan is serial, so there is a trade-off among field of view, number of cells and frame rate: a typical frame rate is 10–30 Hz for a few hundred cells, or about 1 Hz for $10^5$ cells with specialized microscopes.

*Voltage imaging* with genetically encoded voltage indicators resolves single spikes and subthreshold potentials, but requires sampling at 500–1000 Hz, and the number of photons per sample is small: the signal-to-noise ratio is limited by photon shot noise and grows only as the square root of the photon count, which restricts the field of view, the duration of a recording and the depth.

## 3.5. Imaging the Human Brain

Noninvasive methods measure the human brain with different trade-offs (Figure 1 of [7.16.1](/7.16.1#sec-1.6) gives the scales).

**Definition 3.5.1 (Functional Magnetic Resonance Imaging)** **Functional magnetic resonance imaging** (fMRI) maps brain activity indirectly through the **BOLD signal** (blood-oxygen-level-dependent contrast). Deoxyhemoglobin is paramagnetic and shortens the transverse relaxation time $T_2^*$ of the surrounding water; when neural activity increases, blood flow rises by much more than oxygen consumption, so that the venous blood becomes richer in oxyhemoglobin, the local $T_2^*$ lengthens and the MR signal increases by 1–5%.

The BOLD signal is a slow and spatially blurred report of neural activity. It correlates better with synaptic input, summarized by the local field potential, than with the spike output of the neurons. Its time course after a brief neural event is characterized by the response to an impulse.

**Definition 3.5.2 (Hemodynamic Response Function)** The **hemodynamic response function** (HRF) $h(t)$ is the BOLD response to a brief neural event. It rises after a delay of 1–2 s, peaks after about 5 s, returns below baseline with an undershoot and recovers by about 25–30 s.

The standard HRF is a difference of two gamma densities,

$$
h(t) = \frac{t^{a_1 - 1}\mathrm{e}^{-t/b_1}}{b_1^{a_1}\,\Gamma(a_1)} - c\,\frac{t^{a_2 - 1}\mathrm{e}^{-t/b_2}}{b_2^{a_2}\,\Gamma(a_2)},
\qquad a_1 = 6,\ a_2 = 16,\ b_1 = b_2 = 1,\ c = \tfrac16,
$$

with the time $t$ in seconds (Figure 3C). If the vascular response is linear and time-invariant, the predicted BOLD signal for a neural activity time course $x(t)$ is the convolution $y(t) = (h * x)(t)$, and with noise this is the observation model of the **general linear model** used in nearly all analyses of fMRI data ([3.4](/3.4)): at each voxel $\boldsymbol{y} = X\boldsymbol{\beta} + \boldsymbol{\varepsilon}$, where each column of the design matrix $X$ is a stimulus time course convolved with $h$, and the regression coefficients $\beta_j$ measure how strongly a condition drives the voxel; hypotheses are tested on contrasts $\boldsymbol{c}^{\mathsf T}\boldsymbol{\beta}$ with $t$-statistics, corrected for the many thousands of voxels tested.

Figure 3D shows a block design and two isolated events: the blurring by the HRF means that events less than a few seconds apart cannot be separated, but an event-related design with randomized intervals permits estimating $h$ itself by deconvolution. The linearity holds approximately: responses to stimuli shorter than a few seconds are larger than predicted from the response to a longer one.

fMRI covers the whole brain at a resolution of 1–3 mm (a voxel contains about $10^5$ neurons) and 1–2 s; submillimeter resolution is attainable at high magnetic field in restricted regions, as in the layers of cortex. Because the signal is only a correlate of activity, interpretation of fMRI as evidence for local neural computation requires caution; its strength is in comparing conditions, mapping networks (resting-state correlations, [7.16.49](/7.16.49)) and, with multivariate patterns, decoding ([7.16.26](/7.16.26)).

The **electroencephalogram** (EEG, [7.14.46](/7.14.46#sec-46.3)) records the potential on the scalp and magnetoencephalography (MEG) the magnetic field outside the head, both generated mainly by the synchronous postsynaptic currents of the pyramidal neurons of cortex, aligned perpendicular to the cortical surface. Both have millisecond resolution, but their spatial resolution is of the order of a centimeter, since the skull blurs the potential (EEG) and because the inverse problem of finding the sources from the field outside is ill-posed: infinitely many current distributions produce the same field, and a unique answer requires assumptions such as a small number of dipoles or a minimum-norm solution. EEG and MEG are especially suited to rhythms and to the timing of cognitive events.

Positron emission tomography (PET) detects pairs of gamma rays from the annihilation of positrons emitted by an injected radiotracer; with a tracer of glucose metabolism, or one that binds a receptor or a protein aggregate, it maps metabolism and molecular targets with a resolution of 4–5 mm over minutes.

Intracranial recordings in patients with epilepsy (electrocorticography) fill the gap between scalp and cellular recordings, with millisecond and millimeter resolution on the cortical surface.

![Convolution models of indirect measurements. A: a spike train and the fluorescence of a calcium indicator, modeled as a first-order autoregressive process with a decay time constant of 0.6 s. B: nonnegative deconvolution with an $\ell_1$ penalty recovers the spike train from $\Delta F/F_0$. C: the canonical double-gamma hemodynamic response function. D: a block design and two brief events, and the predicted BOLD signal obtained by convolving the neural activity with the HRF, sampled with a repetition time of 2 s with noise](./plots/calcium-bold.py)

## 3.6. Manipulating the Nervous System

Recording shows what correlates with a behavior; manipulation tests causation, as in the necessity and sufficiency experiments of Definition 1.6.1 in [7.16.1](/7.16.1#sec-1.6). The older tools are lesions (surgical, or chemical with neurotoxins), pharmacology (agonists and antagonists delivered systemically or locally) and electrical stimulation, which excites axons rather than cell bodies and so activates cells indiscriminately, including fibers of passage; they have the drawbacks of lacking cell-type specificity and, for lesions and drugs, temporal precision. Genetically targeted tools remove both limitations.

**Optogenetics** expresses a light-sensitive protein (an opsin) in genetically defined neurons. **Channelrhodopsin**-2, a cation channel from algae that opens when it absorbs blue light, depolarizes the cell within a millisecond; the light-driven proton pump archaerhodopsin and the chloride pump **halorhodopsin**, or light-gated chloride channels, silence it; fibers or implanted LEDs deliver light to deep structures. The photocurrent of a cell is the number of open channels times the single-channel conductance times the driving force, so it follows the light intensity $I$ and the expression level, and light attenuates exponentially in tissue by absorption and scattering,

$$
I(z) = I_0\,\mathrm{e}^{-z/\ell}, \qquad \ell \approx 0.1\text{–}0.2\,\mathrm{mm}\ \text{for blue light},
$$

so that illumination from a fiber reaches the neurons within about a millimeter, and the neurons near the tip are driven harder than those farther away; the region affected is large compared to a single cell and the effect depends on the dose. In practice, the interpretation of an optogenetic experiment requires controls: animals without opsin receiving the same light (heating by light can by itself change firing, and visual systems detect the light), checks that the evoked activity resembles physiological activity in rate and pattern, and recordings to verify that silencing does not provoke rebound excitation after the light is turned off.

**Definition 3.6.1 (Chemogenetics)** **Chemogenetics** controls neurons with an engineered receptor or channel that responds to an otherwise inert synthetic ligand. The standard tool is the DREADD (designer receptor exclusively activated by designer drugs), a modified G-protein-coupled receptor that couples to $G_q$ (excitation, through increased intracellular $\ce{Ca^2+}$) or $G_i$ (silencing, through activation of potassium channels) when the ligand is given.

Chemogenetics and optogenetics are complementary. Optogenetics has the temporal precision of milliseconds and requires a light source in the brain; chemogenetics is noninvasive once expressed (the ligand is injected or given in the drinking water), acts on all expressing cells in a region, and lasts minutes to hours, which suits experiments on states and slow behaviors but cannot be used to test a function that unfolds over seconds. Both permit loss-of-function experiments (silencing the neurons that are active during a behavior) and gain-of-function experiments (activating a cell type to see whether it causes the behavior). A direct test that a set of neurons is *sufficient* is to reactivate exactly the neurons that were active during an experience and ask whether the behavior is reproduced, the logic of engram experiments ([7.16.42](/7.16.42)).

## 3.7. Measuring Behavior

Neural data are interpreted in light of behavior, and the precision of the behavioral measurement limits the whole inference. Classical psychophysics measures the probability of a response as a function of a stimulus parameter and fits a psychometric function; it supplies the quantitative behavioral variables used in the chapters on perception and decision ([7.16.27](/7.16.27), [7.16.47](/7.16.47)).

Markerless pose estimation with deep networks, trained on a few hundred labeled video frames, now provides the positions of body parts at the video frame rate, and unsupervised methods segment the continuous stream of posture into a vocabulary of repeated movement motifs.

Tasks for animals are designed so that the quantity of interest (a decision variable, a memory) can be separated from the sensory and motor events around it, and the same task is often given to humans, so that human imaging and animal recordings can be compared. The cost is that tightly controlled tasks may elicit behavior unlike natural behavior, and recordings in freely moving animals, which are becoming possible with miniature microscopes and wireless probes, complement them.

## Summary

| Method | Measures | Resolution (space, time) | Model linking it to activity |
|---|---|---|---|
| Whole-cell / patch clamp | $V$ or current of one cell | one cell, 0.1 ms | direct |
| Extracellular, spike sorting (Algorithm 3.3.1) | spikes of tens of cells, LFP | 50–100 µm, 0.1 ms | $\phi = I/(4\pi\sigma d)$; PCA + Gaussian mixture |
| Calcium imaging (Definition 3.4.1) | $\Delta F/F_0$ of thousands of cells | 1 µm, 50–500 ms | AR(1) convolution, nonnegative deconvolution |
| fMRI (Definition 3.5.1) | BOLD signal | 1–3 mm, 1–2 s | convolution with the HRF (Definition 3.5.2), general linear model |
| EEG / MEG | scalp potentials, fields | about 1 cm, 1 ms | ill-posed inverse problem |
| Optogenetics, chemogenetics (Definition 3.6.1) | (perturbation) | cell type; ms (opto), minutes (chemo) | light attenuation $\mathrm{e}^{-z/\ell}$ |

- Genetic access (Definition 3.1.1) provides cell-type specificity for labeling, recording and manipulation; the connectome (Definition 3.2.1) provides the wiring but not synaptic strengths or dynamics.
- Every indirect measurement is a convolution of neural activity with a kernel, and the corresponding deconvolution is an ill-posed problem that is regularized by constraints (nonnegativity, sparseness, smoothness).
- Necessity (loss of function) and sufficiency (gain of function) must be tested with controls for the specificity, dose and time course of the manipulation.

## Questions

1. A neuron fires a spike whose extracellular amplitude is $240\,\mathrm{\mu V}$ at $25\,\mathrm{\mu m}$. The noise standard deviation is $20\,\mathrm{\mu V}$. Up to what distance is the spike detected at $4.5\sigma$, and how many cells are within this radius at a density of $10^5\,\mathrm{mm^{-3}}$?

   **Answer** With $\phi \propto 1/d$, the amplitude at $d$ is $240 \cdot 25/d$; setting this equal to $4.5 \cdot 20 = 90\,\mathrm{\mu V}$ gives $d = 6000/90 \approx 67\,\mathrm{\mu m}$. The volume is $\tfrac43\pi (67)^3\,\mathrm{\mu m^3} \approx 1.26 \times 10^6\,\mathrm{\mu m^3}$, and the density is $10^{-4}\,\mathrm{\mu m^{-3}}$, so about 126 cells lie within the radius; the spikes of most of them are not detected because most neurons are silent in any short period and their amplitudes depend on their size and orientation.

2. For the AR(1) calcium model with $\tau_{\mathrm{Ca}} = 0.6\,\mathrm{s}$ and a frame rate of 30 Hz, compute $\gamma$, and the fluorescence after a single spike of unit amplitude $1\,\mathrm{s}$ later, relative to its peak.

   **Answer** $\gamma = \mathrm{e}^{-1/(30 \cdot 0.6)} = \mathrm{e}^{-0.0556} \approx 0.946$. After 1 s (30 frames) the calcium is $\gamma^{30} = \mathrm{e}^{-1/0.6} \approx 0.19$ of its peak, so two spikes 1 s apart overlap substantially and cannot be told apart without deconvolution.

3. Show that the HRF of Definition 3.5.2 peaks near 5 s and that a stimulus of duration 1 s produces a response that peaks later than 5 s.

   **Answer** The first gamma density $t^5\mathrm{e}^{-t}/120$ has its maximum at $t = a_1 - 1 = 5$ s; the undershoot term shifts the peak slightly earlier, to about 5 s. A 1 s stimulus gives $y(t) = \int_0^1 h(t - t')\,\mathrm{d}t'$, which is $h$ averaged over the preceding second, so its peak lies half a second later, near 5.5 s.

4. Explain why an optogenetic silencing experiment in which a behavior stops does not prove that the silenced neurons are necessary for the behavior, and how to strengthen the conclusion.

   **Answer** Silencing may have other effects: heating by light, loss of the output of the neurons to many regions (which then are disturbed), or an unnatural pattern of activity on release. The behavior may also stop because the manipulation is sensed by the animal. Controls with light in animals without opsin, silencing of the same cells during a different behavior that should be unaffected, graded effects that vary with the light dose, and a rescue (reactivation of the downstream targets) support the conclusion that these cells are needed specifically for the behavior.
