---
title: Spatiotemporal Dynamics of Hormone Signaling
description: "Why hormones are needed: the division of labor between nerves and hormones, and an order-of-magnitude estimate of the resting energy cost of replacing hormones with nerves; the sending end: the one-compartment pulse–clearance model and the trough-to-peak ratio 2^(−T/t½), convection–dispersion turning spikes into wave packets, the receptor desensitization model and the frequency coding of GnRH, prohormones as signal silencing; the transport end: biexponential clearance and the two-compartment model of growth hormone, the physiologically based pharmacokinetic model of thyroid hormone and the effect of binding proteins on half-life, the free hormone hypothesis; the receiving end: local unloading by neutrophil elastase cleavage of CBG, uptake-driven unloading of testosterone, local activation by deiodinases; spatial structure: flow dilution and first-pass extraction in portal systems, the range of paracrine action λ = √(D/k), the islet microcircuit; evolution and comparison: conservation of pulsatile secretion and portal structures, direct innervation of the teleost pituitary."
source_hash: 5937d6123508
---

Chapter 32 described hormones as a chain of processes: secretion, transport, action on receptors and clearance. This chapter places that chain in time and space and uses simple quantitative models to answer several design questions. Since nerves are fast and precise, why are hormones needed at all (Section 33.1)? The blood is a high-speed, strongly diluting channel shared by the whole body; how does the sending end keep a signal readable after dilution and clearance (Section 33.2)? How do binding proteins protect and reshape the signal on its way (Section 33.3)? How does a target tissue unload and activate a hormone in the second or two that the blood takes to flow past (Section 33.4)? When whole-body broadcast is not wanted, how do portal systems and paracrine signaling change the path and range of a signal (Section 33.5)? The mathematics used is first-order kinetics, mass conservation and diffusion: for ordinary differential equations see [2.4](/2.4), for the diffusion equation [2.5.7](/2.5.7), and for clearance and half-life in pharmacokinetics Eqs. (32.1)–(32.3) of Chapter 32. The physiology of the hypothalamic–pituitary portal system and of thyroid hormone is in Chapter 34, CBG and cortisol are in Chapter 35, the pancreatic islets are in Chapter 35, and testosterone and the GnRH pulses are in Chapter 37.

## 33.1. Why Hormones Are Needed

### 33.1.1. The Division of Labor between Nerves and Hormones

In evolution, chemical signals preceded nerves ([Chapter 32](/7.14.32#sec-32.9.1)), but this does not mean that today's hormone system is merely a historical remnant. Comparing the performance of the two systems, each has strengths that the other cannot replace:

| | Nerves | Hormones |
|---|---|---|
| Speed | Milliseconds (spinal withdrawal reflex $50$–$100\,\mathrm{ms}$) | Seconds to days (epinephrine takes about $1\,\mathrm{min}$, one circulation, to act after entering the blood) |
| Spatial precision | Point to point; can contract just one muscle | Broadcast; every cell with the receptor reads it (cortisol receptors are found almost everywhere in the body) |
| Duration | Ends when firing stops | Determined by the half-life, up to several days |
| Mode of action | Mainly changes membrane potential and intracellular $\ce{Ca^2+}$ | Can also change gene expression and remodel the long-term state of cells |
| Infrastructure | Every target needs a dedicated axon, maintained for life | Borrows the existing circulatory system |

The stress response shows the division of labor between the two most clearly: about $0.1\,\mathrm{s}$ after danger appears, sympathetic nerves have already accelerated the heart and constricted vessels; seconds later, epinephrine released by the adrenal medulla extends this state to the whole body through the blood; minutes later cortisol begins to rise and, within hours, changes gene expression in liver, muscle and immune cells through nuclear receptors. The three signals relay one another on three time scales. The secretion of cortisol is itself a neuroendocrine cascade (hypothalamic CRH → pituitary ACTH → adrenal cortex), in which nerves are responsible only for triggering the most upstream stage.

### 33.1.2. The Cost of Replacing Hormones with Nerves (Order-of-Magnitude Estimates)

Could nerves replace hormones? Considering only the running cost (the energy used each time a signal is sent), the two differ little: the energy for synthesizing and secreting a batch of hormone molecules and for firing a train of action potentials along an axon is of the same order. The real difference lies in the resting cost: a neural pathway must maintain the ion gradients across its membrane even when it does not fire, and consumes energy continuously as long as it exists, whereas the "wiring" of the hormone system is the circulation that is there anyway, and the only extra fixed cost is the glands themselves. The following examples estimate the order of magnitude of this difference with explicitly stated assumptions.

**Example 33.1.1 (Replacing the Action of Progesterone on the Myometrium with Nerves)** Assume:

1. The myometrium at term weighs about $1000\,\mathrm{g}$ ($10^{-3}\,\mathrm{m^3}$), a smooth muscle cell has a volume of about $2000\,\mu\mathrm{m^3}$, and there are about $5\times10^{11}$ cells;
2. The myometrium is single-unit smooth muscle with gap junctions between cells, and one autonomic axon, through varicosities and electrical coupling, can effectively innervate about $10^4$ cells, requiring $5\times10^7$ axons;
3. An axon is about $0.4\,\mathrm{m}$ long from the spinal cord or ganglion to the uterus and $0.5\,\mu\mathrm{m}$ in diameter (a thin unmyelinated C fiber); each axon corresponds to a cell body $30\,\mu\mathrm{m}$ in diameter;
4. Resting energy consumption density: for axons take $3\times10^{22}$ ATP $\mathrm{m^{-3}\,s^{-1}}$ (the order of the resting maintenance cost of myelinated white matter, an underestimate for unmyelinated fibers), for cell bodies take $5\times10^{22}$ ATP $\mathrm{m^{-3}\,s^{-1}}$ ($15\%$ of the total consumption of gray matter, about $3\times10^{23}$).

The total axon length is $L = 5\times10^7 \times 0.4 = 2\times10^7\,\mathrm{m}$ and the total volume $L\pi r^2 = 2\times10^7 \times \pi(0.25\times10^{-6})^2 \approx 3.9\times10^{-6}\,\mathrm{m^3}$; the total volume of cell bodies is $5\times10^7 \times \tfrac{4}{3}\pi(15\,\mu\mathrm{m})^3 \approx 7\times10^{-7}\,\mathrm{m^3}$. The resting energy consumption is
$$
3.9\times10^{-6} \times 3\times10^{22} + 7\times10^{-7}\times 5\times10^{22} \approx 1.5\times10^{17}\ \text{ATP s}^{-1},
$$
that is, about $1.5\times10^{17}\times 86400/(6.0\times10^{23}) \approx 0.02\,\mathrm{mol}$ of ATP per day, about $11\,\mathrm{g}$ (the molar mass of ATP is $507\,\mathrm{g\,mol^{-1}}$). The cost of a single local target is not large, about $0.03\%$ of the whole-body daily ATP turnover (about $40\,\mathrm{kg}$, $80\,\mathrm{mol}$).

**Example 33.1.2 (Extension to All Hormones)** Assume further:

1. The human body has about 40 well-studied hormones, of which about 15 act on almost all tissues (cortisol, $\mathrm{T_3}$/$\mathrm{T_4}$, insulin, glucagon, epinephrine, leptin, IGF-1, etc.) and about 25 act on local targets (estimated as in Example 33.1.1);
2. Each systemic hormone needs a peripheral efferent network covering the whole body (the networks cannot be shared, because the commands differ), whose size is taken as the total length of the peripheral nerve fibers of the body, about $3.4\times10^5\,\mathrm{km}$ (a rough estimate: about $5\times10^5\,\mathrm{km}$ for the whole body minus about $1.6\times10^5\,\mathrm{km}$ of cerebral white matter), with the fiber diameter again taken as $0.5\,\mu\mathrm{m}$; the integrating circuits in the brain are neglected.

The axon volume of 15 peripheral networks is $15 \times 3.4\times10^8 \times \pi(0.25\times10^{-6})^2 \approx 1.0\times10^{-3}\,\mathrm{m^3}$, about $1\,\mathrm{L}$, comparable to the volume of the whole brain (about $1.3\,\mathrm{L}$); the resting energy consumption is about $1.0\times10^{-3}\times3\times10^{22} = 3\times10^{19}$ ATP $\mathrm{s^{-1}}$, about $4.3\,\mathrm{mol}$ per day. Adding the 25 local targets (about $0.5\,\mathrm{mol}$), the total is about $5\,\mathrm{mol}$ of ATP per day, about $6\%$ of the whole-body ATP turnover, comparable to the entire energy consumption of the heart or the kidney (each about $7\%$–$10\%$ of resting metabolism).

For comparison, the total mass of the dedicated endocrine glands of the body is about $50\,\mathrm{g}$; at the resting metabolic rate per unit mass of the liver (about $200\,\mathrm{kcal\,kg^{-1}\,d^{-1}}$), this is about $10\,\mathrm{kcal}$ per day. A resting metabolism of about $1700\,\mathrm{kcal}$ per day for the whole body corresponds to about $80\,\mathrm{mol}$ of ATP, that is, about $21\,\mathrm{kcal}$ of metabolic energy per mole of ATP, so $10\,\mathrm{kcal}$ is about $0.5\,\mathrm{mol}$ of ATP, less than one-tenth of the neural scheme, and this is the entire metabolism of the glands, not only the "resting" part.

The conclusions of these two examples hold only in order of magnitude and are sensitive to the assumptions: the energy consumption is proportional to the square of the axon radius, so halving the radius reduces the result to one-quarter; the total length of fibers in the body and the classification of the hormones are rough estimates. But two points do not depend on the details. First, the cost comes mainly from the systemic hormones, because if broadcast action were replaced by point-to-point wiring, the wiring would have to be as large as the whole nervous system. Second, a more stringent constraint than energy may be volume: 15 whole-body networks would need about $1\,\mathrm{L}$ of extra axons, for which there is no room anatomically. The essential advantage of the hormone system is that it borrows the blood as a common channel and accomplishes whole-body broadcast with a few tens of grams of glands.

### 33.1.3. Nerves Retreat When Hormones Take Over

The division of labor between the two systems is also redrawn with development and with changes of physiological state. In the pregnant uterus of the guinea pig and of humans, the adrenergic nerve fibers of the myometrium degenerate in large numbers during pregnancy and gradually recover after delivery; animal experiments show that this denervation is caused by the high levels of sex hormones in pregnancy. During pregnancy, the resting state of the myometrium and its final contraction are coordinated mainly by humoral signals such as progesterone, estrogen and oxytocin (Chapter 38), and the original sympathetic innervation is withdrawn.

## 33.2. The Sending End: Pulsatile Secretion

### 33.2.1. The One-Compartment Pulse–Clearance Model

Many hormones are not secreted continuously but are released in bursts: GnRH has a pulse about every $1$–$2\,\mathrm{h}$ and LH pulses follow; growth hormone has large pulses after sleep onset; insulin oscillates with a period of $5$–$10\,\mathrm{min}$; and cortisol has a pulse about once an hour superimposed on the circadian rhythm.

**Definition 33.2.1 (Pulsatile Secretion)** The entry of a hormone into the blood in intermittent, brief concentrated releases rather than at a constant rate is called **pulsatile secretion**.

Regard the plasma as a well-mixed pool in which the hormone is cleared by first-order kinetics (rate constant $k = \ln 2/t_{1/2}$), and each pulse raises the concentration by $A$ in a very short time:

**Formula 33.2.1 (One-Compartment Pulse–Clearance Model)**
$$
\frac{\mathrm{d}C}{\mathrm{d}t} = \sum_n A\,\delta(t - t_n) - kC. \tag{33.1}
$$
Between two pulses the concentration decays as $\mathrm{e}^{-kt}$. If the pulses occur at a fixed interval $T$, then in the periodic steady state the trough $C_{\mathrm{t}}$ before each pulse and the peak $C_{\mathrm{p}}$ after it satisfy $C_{\mathrm{p}} = C_{\mathrm{t}} + A$ and $C_{\mathrm{t}} = C_{\mathrm{p}}\mathrm{e}^{-kT}$, giving
$$
C_{\mathrm{p}} = \frac{A}{1 - \mathrm{e}^{-kT}}, \qquad C_{\mathrm{t}} = \frac{A\,\mathrm{e}^{-kT}}{1 - \mathrm{e}^{-kT}}, \qquad \frac{C_{\mathrm{t}}}{C_{\mathrm{p}}} = \mathrm{e}^{-kT} = 2^{-T/t_{1/2}}. \tag{33.2}
$$
The mean concentration over a period is $\bar C = A/(kT)$, the same as the steady-state concentration for continuous infusion at the same mean rate $A/T$. Pulses do not change the mean level; they change the waveform: the ratio of the peak to the mean, $kT/(1 - \mathrm{e}^{-kT})$, increases with $T/t_{1/2}$.

**Example 33.2.1** A hormone with a half-life of $15\,\mathrm{min}$ and a pulse interval of $120\,\mathrm{min}$ has $T/t_{1/2} = 8$ and a trough-to-peak ratio of $2^{-8} \approx 0.0039$: the trough is only $0.4\%$ of the peak, the target cells see a clear "on–off" signal, and the peak is about $5.6$ times the mean. If the pulse interval equals the half-life, the trough-to-peak ratio is $0.5$ and the signal is already close to continuous stimulation.

The body can therefore choose the form of a signal through $T/t_{1/2}$: peptides with short half-lives (GnRH has a half-life of only a few minutes in portal blood) together with pulse intervals of the order of hours produce clear pulses; hormones with long half-lives ($\mathrm{T_4}$) are almost constant in the blood even if secretion fluctuates. The GH–IGF-1 system of Chapter 34 uses precisely a long-half-life secondary signal to "smooth out" the pulses.

![The one-compartment pulse–clearance model (Eq. 33.1). A: plasma concentration (in units of the mean concentration, time in units of the half-life) for the same mean secretion rate and pulse intervals of 1, 2 and 8 half-lives; the dotted line is the steady-state level for continuous infusion at the same rate. B: the trough-to-peak ratio $2^{-T/t_{1/2}}$ (blue, left axis; 0.5, 0.25 and 0.0039 for T = t½, 2t½ and 8t½) and the peak-to-mean ratio (orange dashed line, right axis) as functions of $T/t_{1/2}$](./plots/pulse-clearance.py)

### 33.2.2. Convection–Dispersion: Spikes Become Wave Packets

The one-compartment model assumes that plasma mixes instantly. In reality, a bolus of hormone leaving the site of secretion advances with the blood flow along paths of different lengths (branching of vessels, the velocity difference between the axis and the wall in laminar flow), and by the time it reaches a distant site it has been broadened. With the coordinate $x$ along the direction of flow, it can be described by the one-dimensional convection–dispersion–clearance equation:
$$
\frac{\partial C}{\partial t} + v\frac{\partial C}{\partial x} = D_{\mathrm{eff}}\frac{\partial^2 C}{\partial x^2} - kC + \sum_n A\,\delta(x)\,\delta(t - t_n), \tag{33.3}
$$
where $v$ is the mean flow velocity and the effective dispersion coefficient $D_{\mathrm{eff}}$ summarizes the broadening caused by path differences and mixing (it is not molecular diffusion). The solution for a single pulse is a Gaussian wave packet that moves with the blood and gradually widens (the fundamental solution of the heat equation, [2.5.7](/2.5.7)):
$$
C(x, t) = \frac{A}{\sqrt{4\pi D_{\mathrm{eff}} t}}\exp\left[-\frac{(x - vt)^2}{4D_{\mathrm{eff}}t}\right]\mathrm{e}^{-kt}. \tag{33.4}
$$
The center of the packet advances with velocity $v$, its width grows as $\sqrt{2D_{\mathrm{eff}}t}$, and its peak height falls as $t^{-1/2}\mathrm{e}^{-kt}$. What reaches the target tissue is therefore not a spike but a delayed, broadened, lowered wave packet with a tail; the response to a train of pulses is the superposition of such packets.

The indicator-dilution curve in measuring cardiac output by dye injection is just such a wave packet: a bolus injected into a vein, on reaching the artery after passing through the heart and lungs, has broadened into a peak lasting more than ten seconds. By comparison, a hormone pulse itself lasts minutes and the intervals are tens of minutes to hours, so the broadening in transport is far smaller than the interval between pulses and the peak–trough structure is preserved. Only when the pulse interval becomes as short as the broadening by the circulation (or the time constant of clearance) is the signal smoothed into a continuous background.

### 33.2.3. The Troughs between Pulses: Avoiding Receptor Desensitization

Many receptors undergo **desensitization** under continuous stimulation at a high concentration: the receptor is phosphorylated and uncoupled from G proteins, or internalized, or the downstream pathway is inhibited by negative feedback ([7.1.14](/7.1.14#sec-14.2.4)). It is described with two variables: the fraction of activated receptors $R_{\mathrm{a}}$ and the degree of desensitization $D$ ($0$ is fully sensitive, $1$ fully desensitized).

**Formula 33.2.2 (Receptor Activation–Desensitization Model)**
$$
\frac{\mathrm{d}R_{\mathrm{a}}}{\mathrm{d}t} = k_{\mathrm{on}}C(1 - R_{\mathrm{a}}) - k_{\mathrm{off}}R_{\mathrm{a}}, \qquad \frac{\mathrm{d}D}{\mathrm{d}t} = k_{\mathrm{d}}R_{\mathrm{a}}(1 - D) - k_{\mathrm{r}}D, \tag{33.5}
$$
and the effective signal is $S = R_{\mathrm{a}}(1 - D)$. Here $k_{\mathrm{on}}$ and $k_{\mathrm{off}}$ are the rate constants of binding and dissociation, $k_{\mathrm{d}}$ is the rate constant of desensitization induced by activated receptors, and $k_{\mathrm{r}}$ is the rate constant of recovery.

Under continuous stimulation $R_{\mathrm{a}}$ stays high and $D$ tends to the steady state $k_{\mathrm{d}}R_{\mathrm{a}}/(k_{\mathrm{d}}R_{\mathrm{a}} + k_{\mathrm{r}})$, and the effective signal is depressed; under pulsatile stimulation every peak can activate the receptors, and in the trough that follows $D$ recovers at the rate $k_{\mathrm{r}}$, so that the system is resensitized when the next pulse arrives. The trough is therefore not a waste of signal but a necessary window for resetting the receptor system. The output of the target cell (such as the release of LH) is usually a threshold-type function of the signal, and a signal depressed under continuous stimulation may never reach the threshold at all.

![Receptor desensitization under pulsatile and continuous stimulation (Eq. 33.5; integrated in minutes, schematic parameters $k_{\mathrm{on}} = k_{\mathrm{off}} = 1\,\mathrm{min^{-1}}$, $k_{\mathrm{d}} = 0.2\,\mathrm{min^{-1}}$, $k_{\mathrm{r}} = 0.03\,\mathrm{min^{-1}}$). A: one 6-min square pulse per hour (shaded, scaled down), mean concentration 1 (in units of $K_{\mathrm{d}}$); B: continuous infusion with the same mean concentration. Blue: activated receptors $R_{\mathrm{a}}$; red dashed line: degree of desensitization D; green: effective signal S. Between pulses D recovers, and every pulse produces a peak signal of about 0.7; under continuous infusion D rises to about 0.77 and S falls to about 0.12. If the output of the cell is a threshold function $R = S^4/(S^4 + 0.3^4)$ (dotted line, the threshold), the cumulative output over 10 h under pulsatile stimulation is about 2.7 times that under continuous stimulation](./plots/receptor-desensitization.py)

**Example 33.2.2 (The Necessity of GnRH Pulses)** In 1978 Knobil and colleagues destroyed the arcuate nucleus of the hypothalamus of rhesus monkeys, abolishing endogenous GnRH, and the pituitary secretion of LH and FSH stopped. When GnRH was infused in pulses of a few minutes once an hour, the secretion of gonadotropins returned to normal; when the same total amount was infused continuously instead, secretion was suppressed again within a few days; and it reappeared when the pulses were restored. Clinically, continuously acting GnRH analogues (such as leuprolide) are used to "switch off" the pituitary–gonadal axis in the treatment of prostate cancer, endometriosis and precocious puberty, whereas pulsatile administration of GnRH with a portable pump can treat the infertility caused by hypothalamic amenorrhea. The same molecule has opposite effects with different modes of administration.

### 33.2.4. Frequency Coding

One and the same hormone can also carry different instructions in the frequency of its pulses. GnRH is the clearest example: faster pulses (about once every $30$–$60\,\mathrm{min}$) favor the transcription of the LH β subunit gene and the secretion of LH, and slower pulses (about once every $2$–$3\,\mathrm{h}$) favor the FSH β subunit gene, so that the changing GnRH pulse frequency during the menstrual cycle takes part in changing the ratio of LH to FSH (Chapter 37). The mechanism is that the different steps inside the cell have different time constants: every pulse drives the receptor, second messengers, transcription factors and gene expression, and in the trough they recover at their own rates; when the frequency changes, the fast and slow processes accumulate in different ways and the downstream output differs accordingly.

Another example is growth hormone in the rat: males have a large pulse about every $3.5\,\mathrm{h}$ with levels almost falling to zero between pulses, whereas females secrete almost continuously at a higher baseline. Hepatocytes read this temporal pattern rather than the mean concentration: pulsatile GH repeatedly activates the transcription factor STAT5b and induces the male-specific cytochrome P450 (CYP2C11), whereas continuous GH induces the female-specific isozymes. After hypophysectomy, giving GH with a male or female infusion pattern can turn hepatic gene expression toward the corresponding sex.

### 33.2.5. Precursors: Signal Silencing

Some hormones are secreted as low-activity precursors and are activated only in the target tissue. The thyroid secretes mainly $\mathrm{T_4}$ (thyroxine), whereas what binds the thyroid hormone receptor is mainly $\mathrm{T_3}$: $\mathrm{T_4}$ has one more iodine atom at the 5′ position of the outer ring, which lowers its affinity for the receptor about tenfold relative to $\mathrm{T_3}$. The point of the precursor is not to prolong the half-life: the half-life of $\mathrm{T_4}$ in blood of a week comes mainly from protection by binding proteins (Section 33.3), not from greater stability of the molecule itself. The point of the precursor is to keep the signal "silent" during transport: $\mathrm{T_4}$ flows throughout the body but does not cause a strong response in tissues without an activating enzyme; activation occurs only in cells that express deiodinases (Section 33.4.4), and each tissue can decide independently how strong a thyroid hormone signal it receives. Vitamin $\mathrm{D_3}$ (hydroxylated twice to become calcitriol, Chapter 36) and angiotensinogen (cleaved by renin and ACE, Chapter 24) also follow this strategy: signals that must be transported over long distances, whose receptors are widely distributed and which act strongly once activated are often transported as precursors.

## 33.3. The Transport End: Binding Proteins and Clearance

### 33.3.1. Biexponential Clearance of Growth Hormone and the Two-Compartment Model

When a bolus of GH is injected intravenously into a subject, the measured plasma concentration is not a straight line on a semilogarithmic plot but two segments, first fast and then slow, which can be fitted well with a biexponential function:
$$
[\mathrm{GH}](t) = A_1\mathrm{e}^{-\lambda_1 t} + A_2\mathrm{e}^{-\lambda_2 t}. \tag{33.6}
$$
The fast phase ($\lambda_1$) mainly reflects the distribution of GH from plasma to the extravascular space and its binding to binding proteins, and the slow phase ($\lambda_2$) mainly reflects irreversible clearance. This corresponds to a two-compartment model: the central compartment is free GH in plasma (amount $x_1$), the peripheral compartment is GH bound to growth hormone–binding protein (GHBP, the cleaved extracellular domain of the GH receptor) or distributed extravascularly (amount $x_2$), the two compartments exchange reversibly, and only free GH in the central compartment is cleared (receptor-mediated endocytosis, glomerular filtration, hepatic degradation):

**Formula 33.3.1 (Two-Compartment Model)**
$$
\frac{\mathrm{d}x_1}{\mathrm{d}t} = -(k_{10} + k_{12})x_1 + k_{21}x_2, \qquad \frac{\mathrm{d}x_2}{\mathrm{d}t} = k_{12}x_1 - k_{21}x_2. \tag{33.7}
$$
The negatives of the two eigenvalues of the coefficient matrix are the $\lambda_1$ and $\lambda_2$ of Eq. (33.6), satisfying $\lambda_1 + \lambda_2 = k_{10} + k_{12} + k_{21}$ and $\lambda_1\lambda_2 = k_{10}k_{21}$; the half-life of each phase is $\ln 2/\lambda_i$. A molecule stays on average $\mathrm{MTT}_1 = 1/k_{10}$ in the central compartment and $\mathrm{MTT}_2 = k_{12}/(k_{21}k_{10})$ in the peripheral compartment, and its mean residence time in the body is
$$
\mathrm{MRT} = \mathrm{MTT}_1 + \mathrm{MTT}_2 = \frac{1}{k_{10}}\left(1 + \frac{k_{12}}{k_{21}}\right). \tag{33.8}
$$
$k_{12}/k_{21}$ is the equilibrium distribution ratio of the two compartments, that is, the ratio of bound to free GH. The more binding ($k_{12}$ larger or $k_{21}$ smaller), the longer each molecule spends in a state in which it cannot be cleared, and the longer the MRT; this is the kinetic expression of $t_{1/2} \propto 1/f$ in Eq. (32.3). About $40\%$ of the 22 kDa GH in plasma is bound to high-affinity GHBP, and the half-life of GH is about $20$–$25\,\mathrm{min}$.

![The two-compartment model of growth hormone (Eq. 33.7; schematic parameters $k_{10} = 0.06$, $k_{12} = 0.05$, $k_{21} = 0.08\,\mathrm{min^{-1}}$). A: after an intravenous bolus, the central compartment (free plasma GH, blue) first falls rapidly (fast phase t½ about 4 min) and then falls together with the peripheral compartment (bound or extravascular, purple) in the slow phase (t½ about 23 min); the blue dashed line is the extrapolation of the slow phase and the dotted line is the total amount in the body. B: doubling $k_{12}$ (more binding), the initial fall is faster (more molecules enter the peripheral compartment) but the slow phase becomes slower, and the mean residence time MRT is prolonged from 27 min to 38 min (Eq. 33.8)](./plots/gh-two-compartment.py)

### 33.3.2. A Physiologically Based Pharmacokinetic Model of Thyroid Hormone

Thyroid hormone acts on almost all tissues of the body and must be transported over long distances through the systemic circulation. In plasma it binds to three thyroid hormone–binding proteins: thyroxine-binding globulin (TBG, highest affinity and lowest concentration), transthyretin (TTR, also called thyroxine-binding prealbumin) and albumin (lowest affinity and highest concentration). The human physiologically based pharmacokinetic (PBK) model of Bagga and colleagues (2023) divides the body into four parts, systemic blood, thyroid, liver and "rest of body," the last three each divided into intravascular and extravascular subcompartments; in the blood subcompartment it tracks 11 molecular species: free $\mathrm{T_4}$, $\mathrm{T_3}$, the three binding proteins and six complexes, with binding and dissociation following the law of mass action and only free $\mathrm{T_4}$ and $\mathrm{T_3}$ in tissue cleared by first-order metabolism. The steady-state distribution given by the model is:

| | Free | TBG-bound | TTR-bound | Albumin-bound |
|---|---|---|---|---|
| $\mathrm{T_4}$ | $0.016\%$ | $75.0\%$ | $17.2\%$ | $7.8\%$ |
| $\mathrm{T_3}$ | $0.30\%$ | $75.3\%$ | $4.9\%$ | $19.6\%$ |

The binding proteins are far from saturated: TBG is less than $20\%$ saturated, TTR about $0.3\%$ and albumin about $0.001\%$. This gives the system a large buffering capacity: when structurally similar exogenous compounds (endocrine disruptors) compete for binding, the proportion of free hormone changes little.

The model also gives several quantitative conclusions:

- About $40\%$ of the thyroid hormone is metabolized in the liver and $60\%$ in the other tissues. The total $\mathrm{T_4}$ delivered by the blood to the liver is about $1.3\times10^3\,\mathrm{pmol\,s^{-1}}$, of which free $\mathrm{T_4}$ is only about $0.2\,\mathrm{pmol\,s^{-1}}$; the exchange of $\mathrm{T_4}$ between liver blood and liver tissue is about $64\,\mathrm{pmol\,s^{-1}}$ (in) and $63\,\mathrm{pmol\,s^{-1}}$ (back), and less than $1\%$ of the $\mathrm{T_4}$ entering liver tissue is metabolized, the rest returning to the blood; of that entering the other tissues only about $7\%$ is metabolized. As long as plasma free hormone is stable, the steady-state concentration of hormone in the tissues is therefore insensitive to perturbations of local metabolism.
- When a tracer amount of $\mathrm{T_4}$ is added to the blood, the tracer changes in four stages: rapid distribution into the intravascular space of the liver and the other tissues (the concentration falls to about $2/3$), distribution into liver tissue, distribution into the other tissues (the first three stages are completed within about a day), and finally the metabolic phase. From the slope of the metabolic phase the half-life of $\mathrm{T_4}$ is about $6.3\,\mathrm{d}$ and that of $\mathrm{T_3}$ about $24\,\mathrm{h}$, in agreement with the clinically measured values of about $7\,\mathrm{d}$ and about $1\,\mathrm{d}$.
- When TBG, TTR and albumin are removed in turn, the stage of distribution of $\mathrm{T_4}$ to the tissues comes earlier and the half-life shortens; when all three are removed, blood and tissue equilibrate within a few minutes and the half-life of $\mathrm{T_4}$ shortens to about $4.8\,\mathrm{d}$.

The last point deserves careful explanation. By Eq. (32.3), as the free fraction rises from about $0.02\%$ to $100\%$, the half-life should seem to shorten several thousandfold, but it actually shortens by only about one-quarter. The reason is that Eq. (32.3) assumes a constant volume of distribution, whereas thyroid hormone also binds to a large number of intracellular proteins inside tissue cells: most of the $\mathrm{T_4}$ in the body is in any case stored in the tissues. The whole-body half-life equals $\ln 2 \times$ total amount in the body / metabolic rate; removing the plasma binding proteins removes only the plasma part of the reserve (about one-third of the extrathyroidal $\mathrm{T_4}$ pool), and the free concentration at the site of metabolism is determined by tissue binding and changes little. The main role of plasma binding proteins is therefore not to prolong the half-life but to keep a large reserve in the blood that can be called upon at any time, and to deliver the hormone uniformly to the whole body: without binding proteins, free hormone flowing through the first tissue would be taken up extensively and downstream tissues would receive less.

There is also a counterintuitive result in the model: when the three binding proteins are removed, the half-life of $\mathrm{T_3}$ does not shorten but is prolonged from about $24\,\mathrm{h}$ to about $27\,\mathrm{h}$. This is because the metabolic rate constant of $\mathrm{T_3}$ in the liver is about $5.4$ times that in the other tissues; without plasma binding proteins the tracer distributes quickly among the tissues, after which $\mathrm{T_3}$ in the liver declines faster, and the tracer gradually concentrates in the other tissues, where metabolism is slow (the ratio of the two contents ends at about $37:1$), so that the whole-body half-life approaches the half-life of $\mathrm{T_3}$ of the other tissues themselves (about $30\,\mathrm{h}$). The speed of whole-body clearance depends on where the hormone mainly resides, and not only on the free fraction.

### 33.3.3. The Free Hormone Hypothesis

**Definition 33.3.1 (Free Hormone Hypothesis)** The hypothesis that only hormone that is free in plasma (not bound to protein) can enter cells, bind receptors and be metabolized, so that the biological activity of a hormone is determined by its free concentration and not by its total concentration, is called the **free hormone hypothesis**.

It explains many phenomena of Chapter 32: feedback regulates free hormone (Example 32.7.1), and an increase or decrease of binding protein changes only the total amount; clinically, free $\mathrm{T_4}$ reflects thyroid function better than total $\mathrm{T_4}$. But it is an approximation. In a steady-state tissue with slow exchange, the free concentration does determine tissue uptake; in the second or two during which the blood flows past, if tissue uptake is extremely fast, bound hormone can dissociate rapidly in the capillary and be taken up, and the amount actually entering the tissue far exceeds the expectation from the free concentration (Section 33.4.3). Binding proteins may also be modified in a tissue-specific way (Section 33.4.2) or taken directly into cells by endocytosis (for example, SHBG enters some target cells through megalin). For a given tissue, the hormone actually available depends on the relation among four quantities: the free fraction, the dissociation rate, the capillary transit time and the rate of tissue uptake.

## 33.4. The Receiving End: Local Unloading and Local Activation

### 33.4.1. Binding Equilibrium and the Free Fraction

The binding and dissociation of hormone and protein are usually completed within milliseconds to seconds, and are approximately at equilibrium at any point in the microcirculation:
$$
[\mathrm{H}]_{\mathrm{free}}\,[\mathrm{BP}]_{\mathrm{free}} = K_{\mathrm{d}}\,[\mathrm{H{\cdot}BP}]. \tag{33.9}
$$
When the binding protein is far from saturated ($[\mathrm{BP}]_{\mathrm{free}} \approx [\mathrm{BP}]_{\mathrm{total}}$),
$$
[\mathrm{H}]_{\mathrm{free}} = \frac{[\mathrm{H}]_{\mathrm{total}}}{1 + [\mathrm{BP}]_{\mathrm{free}}/K_{\mathrm{d}}}. \tag{33.10}
$$
The larger the denominator, the higher the proportion held in the bound state. If a target tissue can locally increase $K_{\mathrm{d}}$ (lower the affinity) or speed up the uptake of free hormone, it can raise the local free concentration without changing the secretion of the whole body or the total plasma concentration.

### 33.4.2. Local Unloading: Elastase Cleavage of CBG

About $80\%$–$90\%$ of the cortisol in plasma is bound to corticosteroid-binding globulin (CBG), about $5\%$–$10\%$ to albumin, and only about $5\%$ is free. CBG is a glycoprotein of about $52\,\mathrm{kDa}$ belonging to the serine protease inhibitor (serpin) family; the complex hardly crosses the capillary wall, ensuring that cortisol is not lost at will during transport. At sites of inflammation, activated neutrophils release neutrophil elastase, which cleaves the reactive center loop on the surface of CBG; after cleavage the serpin undergoes an irreversible conformational change and its affinity for cortisol falls by about an order of magnitude. The free cortisol that is released is a small lipophilic molecule that quickly crosses the endothelium into the inflamed tissue, where it exerts its anti-inflammatory action (the affinity of CBG also falls as temperature rises in fever).

**Example 33.4.1 (Local Amplification Factor)** Define the ratio of the free concentration in the target region to that in the normal region as the local amplification factor $\alpha$. By Eq. (33.10), for the same total cortisol and CBG concentrations,
$$
\alpha = \frac{1 + [\mathrm{CBG}]/K_{\mathrm{d}}}{1 + [\mathrm{CBG}]/K_{\mathrm{d}}^*}.
$$
Take $[\mathrm{CBG}] = 700\,\mathrm{nmol\,L^{-1}}$, $K_{\mathrm{d}} = 30\,\mathrm{nmol\,L^{-1}}$ for intact CBG and $K_{\mathrm{d}}^* = 320\,\mathrm{nmol\,L^{-1}}$ after cleavage (Nguyen et al., 2014):
$$
\alpha = \frac{1 + 700/30}{1 + 700/320} = \frac{24.3}{3.19} \approx 7.6.
$$
With the total blood flow and the total cortisol level unchanged, cleavage of CBG can raise local free cortisol severalfold.

Eq. (33.10) neglects two points: cortisol occupies part of the CBG (total cortisol during the day is about $150$–$550\,\mathrm{nmol\,L^{-1}}$, not small relative to $700\,\mathrm{nmol\,L^{-1}}$ of CBG), and binding to albumin. An exact solution of the binding equilibrium (figure below) shows that both partial saturation of CBG and buffering by albumin reduce the amplification factor: at a total cortisol of $400\,\mathrm{nmol\,L^{-1}}$ the factor is about $4.9$ considering CBG alone and about $3.5$ when albumin is included. The conclusion is unchanged in order of magnitude: local cleavage of the binding protein is a mechanism of "targeted delivery" in which the total amount of cortisol is unchanged, yet the inflamed site receives severalfold more free hormone.

![Free fraction of cortisol and the affinity of CBG. Total CBG 700 nM; the dashed lines also account for low-affinity binding to albumin (bound/free ratio 1.5). A: free fraction as a function of the $K_{\mathrm{d}}$ of CBG (total cortisol 100 nM and 400 nM); dotted lines mark intact CBG (30 nM) and CBG cleaved by neutrophil elastase (320 nM). B: local amplification factor α = free concentration (cleaved) / free concentration (intact) as a function of total cortisol; the dotted line is the approximation 7.63 that neglects saturation and albumin, and the shading is the usual daytime range. The higher the total cortisol and the more saturated the CBG, the smaller the amplification factor](./plots/cortisol-free-fraction.py)

### 33.4.3. Uptake-Driven Unloading: Testosterone

Changing the structure of the binding protein can be done only in particular microenvironments. Another way of unloading does not require changing the binding protein: as long as target cells take up or metabolize free hormone fast enough, the free concentration in the capillary is driven close to zero, the binding equilibrium is broken, and bound hormone dissociates in large amounts in the second or two during which the blood flows past (Le Chatelier's principle).

About $2\%$ of plasma testosterone is free, about $40\%$–$50\%$ is loosely bound to albumin, and the rest is tightly bound to SHBG. Albumin has a low affinity and fast dissociation; SHBG has a high affinity and slow dissociation. When blood flows through a tissue that takes up testosterone very quickly (liver, brain, skeletal muscle, target tissues expressing 5α-reductase and many androgen receptors), free testosterone enters the cells quickly, the free concentration in the lumen tends to zero, the reverse reaction of the albumin–testosterone complex can be neglected, and dissociation becomes a one-way first-order process:
$$
\frac{\mathrm{d}[\mathrm{T{\cdot}Alb}]}{\mathrm{d}t} = -k_{\mathrm{off}}[\mathrm{T{\cdot}Alb}] \quad\Rightarrow\quad \frac{[\mathrm{T{\cdot}Alb}]_\tau}{[\mathrm{T{\cdot}Alb}]_0} = \mathrm{e}^{-k_{\mathrm{off}}\tau}. \tag{33.11}
$$

**Example 33.4.2 (Unloading in Target and Nontarget Tissues)** Take the dissociation rate constant of albumin–testosterone $k_{\mathrm{off}} \approx 2\,\mathrm{s^{-1}}$ (Zheng et al., 2015) and a capillary transit time $\tau = 1\,\mathrm{s}$. In a target tissue with extremely fast uptake, the proportion of albumin-bound testosterone released in one pass is
$$
\eta_{\mathrm{target}} = 1 - \mathrm{e}^{-k_{\mathrm{off}}\tau} = 1 - \mathrm{e}^{-2} \approx 86\%.
$$
In a nontarget tissue with neither rapid metabolism nor many receptors, free testosterone is cleared only at a background rate; take $k_{\mathrm{clear}} \approx 3.3\times10^{-3}\,\mathrm{s^{-1}}$, and the proportion of free testosterone lost in one pass is
$$
1 - \mathrm{e}^{-k_{\mathrm{clear}}\tau} = 1 - \mathrm{e}^{-3.3\times10^{-3}} \approx 0.33\%,
$$
and the binding equilibrium in the vessel is hardly perturbed; to make up this small loss, the testosterone released from the albumin-bound state is only about $2\% \times 0.33\% \approx 0.007\%$ of the total testosterone. The same blood flowing through the two kinds of tissue releases proportions that differ by more than four orders of magnitude: unloading takes place where the hormone is needed, and elsewhere the binding protein protects the hormone from being consumed.

In the 1970s and 80s Pardridge measured the uptake by the rat brain of steroids in a single pass through the carotid artery and found that far more testosterone and estradiol entered the brain than expected from the free fraction; most of the albumin-bound part could be taken up, whereas the SHBG-bound part was essentially not taken up in the brain, and a considerable portion of it could be taken up in the liver. This is just the prediction of Eq. (33.11): whether unloading occurs depends on the product of the dissociation rate constant and the transit time, and on the uptake capacity of the tissue. It is also where the free hormone hypothesis (Definition 33.3.1) needs revision: for tissues with fast uptake, the "available hormone" is the free plus the albumin-bound part, and not only the free part.

### 33.4.4. Local Activation and Peripheral Clearance: Deiodinases

Free hormone that has been unloaded diffuses in all directions, both diluting the target region and possibly causing false signals elsewhere. The thyroid hormone system solves this problem with local activation: what is delivered to the tissues is mainly the low-activity $\mathrm{T_4}$ (Section 33.2.5), and three selenium-containing iodothyronine deiodinases inside the cell decide its fate:

| Enzyme | Reaction | Main distribution | Physiological role |
|---|---|---|---|
| Type I (D1) | Outer- and inner-ring deiodination; mainly clears $\mathrm{rT_3}$ and also produces $\mathrm{T_3}$ | Liver, kidney (proximal tubule), thyroid | Produces part of plasma $\mathrm{T_3}$; recovers iodine |
| Type II (D2) | Outer-ring deiodination: $\mathrm{T_4} \to \mathrm{T_3}$ | Brain (astrocytes, tanycytes), pituitary thyrotrophs, brown fat, skeletal muscle, cochlea | Produces $\mathrm{T_3}$ inside the cell for use by that cell |
| Type III (D3) | Inner-ring deiodination: $\mathrm{T_4} \to \mathrm{rT_3}$, $\mathrm{T_3} \to \mathrm{T_2}$ (both inactive) | Placenta, fetal tissues, brain, skin | Local inactivation; protects the fetus and certain tissues |

The Michaelis constant of D2 is about $1\,\mathrm{nmol\,L^{-1}}$, about two orders of magnitude higher than the free $\mathrm{T_4}$ of plasma (about $10$–$25\,\mathrm{pmol\,L^{-1}}$); the enzyme is far from saturated, and the rate of product formation $v \approx (V_{\max}/K_{\mathrm{m}})[\mathrm{T_4}]$ is proportional both to the amount of enzyme and to the substrate concentration. The amount of enzyme thus becomes a tissue-specific "gain": for the same plasma $\mathrm{T_4}$, a cell with more D2 obtains more $\mathrm{T_3}$; the amount of enzyme can be raised over a wide range without saturation (in the cold, sympathetic nerves increase D2 in brown fat severalfold through cAMP, local $\mathrm{T_3}$ rises accordingly and promotes nonshivering thermogenesis, Chapter 31). In addition, after binding its substrate $\mathrm{T_4}$, D2 is ubiquitinated and degraded: the more $\mathrm{T_4}$, the less D2, which gives the intracellular generation of $\mathrm{T_3}$ some buffering against fluctuations in plasma $\mathrm{T_4}$. At the same time D3 inactivates excess $\mathrm{T_4}$ and $\mathrm{T_3}$ in the surrounding tissues. The combination of "activation at the center, inactivation in the surroundings" keeps the highly active $\mathrm{T_3}$ mainly near the cell that produces it. The D2 of the pituitary thyrotrophs themselves also means that the feedback signal sensed by the pituitary is the $\mathrm{T_3}$ it makes itself from $\mathrm{T_4}$ (Chapter 34).

## 33.5. Spatial Structure: Portal Systems and Paracrine Signaling

### 33.5.1. Portal Systems and Flow Dilution

**Definition 33.5.1 (Portal System)** A vascular arrangement in which venous blood from one capillary bed passes directly, not through the heart, by way of a vein (a portal vein) into a second capillary bed is called a **portal system**.

The significance of a portal system can be explained by mass conservation. Let a flux $J$ of hormone enter a blood flow $Q$ per unit time; in the steady state the concentration increment in one pass is
$$
\Delta C \approx \frac{J}{Q}. \tag{33.12}
$$
For the same secretory flux, if it enters a portal flow that is small, instead of first returning to the heart and mixing with the venous return of the whole body, the ratio of the concentration increments seen by the downstream organs is
$$
\frac{\Delta C_{\mathrm{portal}}}{\Delta C_{\mathrm{systemic}}} \approx \frac{Q_{\mathrm{systemic}}}{Q_{\mathrm{portal}}}. \tag{33.13}
$$
A portal system does not increase the amount secreted but changes the order in which the signal is received: the downstream organ reads the hormone first, at a much higher concentration, before it is diluted through the whole body, and can process, amplify or clear it before it enters the general circulation.

### 33.5.2. The Hypothalamic–Pituitary Portal System

**Definition 33.5.2 (Hypothalamo-Hypophyseal Portal System)** The vascular pathway in which the axon terminals of hypothalamic neuroendocrine cells release releasing and inhibiting hormones into the primary capillary plexus in the median eminence, and the blood flows through the portal veins of the pituitary stalk to the secondary capillary plexus of the anterior pituitary, is called the **hypothalamo-hypophyseal portal system**.

**Example 33.5.1** Taking the blood flow of the anterior pituitary as about $0.8\,\mathrm{mL\,g^{-1}\,min^{-1}}$ and the gland as about $0.6\,\mathrm{g}$, the flow is about $0.5\,\mathrm{mL\,min^{-1}}$; the cardiac output is about $5000\,\mathrm{mL\,min^{-1}}$. By Eq. (33.13), for the same hypothalamic secretion, the concentration increment seen by the anterior pituitary when the hormone enters the portal system directly is about $10^4$ times that when it enters the systemic circulation. This agrees with measurement: in sheep, when portal blood and peripheral blood are sampled simultaneously, GnRH pulses in portal blood can reach tens of picograms per milliliter and correspond one to one to the LH pulses in peripheral blood, whereas GnRH in peripheral blood is barely detectable (Clarke and Cummins, 1982).

The hypothalamus therefore needs to secrete only nanogram amounts of releasing hormone to control the anterior pituitary; the anterior pituitary, as an amplifying node, then sends the signal into the whole body (Chapter 32). This "upstream targeted delivery" of the portal system also means that the concentration of hypothalamic hormones in peripheral blood does not reflect their secretion.

### 33.5.3. The Pancreatic–Hepatic Portal Vein and First-Pass Extraction

Insulin and glucagon secreted by the islets enter the portal vein and reach the liver first. The insulin concentration at the entrance of the liver is about
$$
C_{\mathrm{portal}} \approx C_0 + \frac{J_{\mathrm{ins}}}{Q_{\mathrm{portal}}},
$$
where $C_0$ is the concentration of arterial blood flowing into the pancreas. The liver extracts and degrades part of the insulin in a single pass; with an extraction fraction $E$ (about $50\%$–$60\%$ in the fasting state, varying with the insulin pulses), the flux entering the systemic circulation is $(1 - E)J_{\mathrm{ins}}$ and the increment seen by peripheral tissues is about $(1 - E)J_{\mathrm{ins}}/Q_{\mathrm{systemic}}$.

**Definition 33.5.3 (First-Pass Effect)** The phenomenon in which a substance absorbed or secreted into the portal vein is taken up and metabolized on its first pass through the liver, reducing the amount that reaches the systemic circulation, is called the **first-pass effect**.

The portal vein flow (about $1\,\mathrm{L\,min^{-1}}$) is about one-fifth of the cardiac output, and with first-pass extraction as well, the insulin increment seen by the liver is about $5/(1 - E) \approx 10$ times that seen by peripheral tissues; the measured portal insulin concentration is about $2$–$3$ times the peripheral concentration (the peripheral concentration also contains a recirculating basal amount). The physiological significance of this design is that after a meal the liver reads the insulin signal first and most strongly, rapidly increasing glycogen synthesis and inhibiting gluconeogenesis and hepatic glucose output, whereas the peripheral muscle and fat read a weaker signal that has been "filtered" by the liver. Subcutaneous injection of insulin bypasses the portal vein, and for the liver to receive a sufficient signal the peripheral concentration must be above the physiological level, which is one reason why insulin therapy easily causes hypoglycemia and weight gain. The same first-pass effect lowers the bioavailability of many oral drugs (Chapter 29).

### 33.5.4. Where There Is No Portal System

A portal system is not an inevitable structure between organs that are "close and hormonally connected." The ovary and uterus are adjacent, and ovarian hormones strongly affect the uterus, yet there is no portal system: estrogen and progesterone must also act on the hypothalamus–pituitary, the mammary gland, bone, brain and liver, so they are systemic signals, and delivering them specifically to the uterus would weaken this function; the relation between the two is also not a one-way "upstream secretion, downstream processing" but periodic and bidirectional. A local shortcut can nevertheless exist without a portal system: in ruminants such as the sheep, prostaglandin $\mathrm{F_{2\alpha}}$ secreted by the uterus is delivered directly to the ipsilateral ovary by countercurrent exchange between the utero-ovarian vein and the ovarian artery that coils around it, causing luteolysis (Chapter 37). The thyroid and parathyroid glands lie close together, and PTH and calcitonin both regulate blood calcium, yet there is no portal system: what the parathyroid needs to read is the calcium of the blood of the whole body, not a signal released locally by the thyroid, and the target organs of both (bone, kidney, intestine) are distant.

These examples suggest the conditions under which a portal system is applicable: the upstream signal has a particularly high value to the downstream; the downstream needs to read or process it ahead of other tissues; and there is a clear one-way relation between the two. The hypothalamus–pituitary and the pancreas (and gut)–liver both meet these conditions.

### 33.5.5. The Range of Paracrine Action

A **paracrine** signal does not enter the blood but reaches neighboring cells by diffusing through the interstitial fluid, and is degraded, taken up or carried away by the blood flow on the way. Its range is determined by the competition between diffusion and clearance: let the signal diffuse with diffusion coefficient $D$ and be cleared with first-order rate constant $k$, with the concentration near the source held at $C_0$; the steady-state concentration decays with distance as $C(x) = C_0\mathrm{e}^{-x/\lambda}$, with decay length
$$
\lambda = \sqrt{\frac{D}{k}}, \tag{33.14}
$$
which is the source–sink model of the chemotactic gradient in Chapter 2 (Eq. (2.3)). For a point source in three dimensions the steady-state solution is $C(r) \propto \mathrm{e}^{-r/\lambda}/r$, which decays faster, but the characteristic length is still $\lambda$.

**Example 33.5.2 (Nitric Oxide)** NO is a small gaseous molecule with a diffusion coefficient in tissue of about $3300\,\mu\mathrm{m^2\,s^{-1}}$. It is cleared in tissue mainly by reactive oxygen species and heme proteins, with a half-life of about $0.1$–$1\,\mathrm{s}$ ($k \approx 1$–$10\,\mathrm{s^{-1}}$); by Eq. (33.14), $\lambda \approx 18$–$57\,\mu\mathrm{m}$: NO released by the endothelium is sufficient to reach a few layers of smooth muscle cells (the media of an arteriole is about $10$–$20\,\mu\mathrm{m}$ thick) but does not reach distant vessels. In blood, hemoglobin inside red cells reacts with NO extremely fast ($k \sim 10^3\,\mathrm{s^{-1}}$) and $\lambda$ is only about $2\,\mu\mathrm{m}$, so NO cannot act as a circulating hormone. As soon as the local stimulus (shear stress of blood flow, acetylcholine) disappears, NO is cleared in about a second and the relaxation stops accordingly ([Chapter 15](/7.14.15)).

![The range of paracrine signals (Eq. 33.14). A: steady-state concentration profiles near a planar source (an endothelial layer): NO in tissue ($D = 3300\,\mu\mathrm{m^2\,s^{-1}}$, $k = 1$ and $10\,\mathrm{s^{-1}}$), NO in blood cleared by hemoglobin ($k \approx 1000\,\mathrm{s^{-1}}$), and a small peptide (such as somatostatin, $D \approx 150\,\mu\mathrm{m^2\,s^{-1}}$, $k = 0.01\,\mathrm{s^{-1}}$); shading marks the arteriolar wall (about 0–20 µm) and the radius of an islet (about 50–100 µm). B: decay length λ as a function of the clearance half-life; λ is proportional to the square root of the lifetime](./plots/paracrine-range.py)

The design principle of paracrine signaling can be summarized as local release, short-distance diffusion and rapid clearance, which together confine the signal to the tissue unit that needs it. By Eq. (33.14), changing the clearance rate is a direct means of regulating the range: expression of degrading enzymes, binding of the signal by the extracellular matrix and washout by local blood flow can all compress or widen $\lambda$.

### 33.5.6. The Paracrine Microcircuit of the Islet

An islet is not a group of cells that respond independently to blood glucose but a small local feedback network (diameter about $100$–$200\,\mu\mathrm{m}$, just within the range of peptide paracrine signals):

- Somatostatin secreted by δ cells inhibits the secretion of α cells and β cells, acting as a local "brake" that limits the overshoot of insulin and glucagon; urocortin 3 secreted by β cells stimulates δ cells, forming a negative feedback loop.
- Insulin, $\ce{Zn^2+}$ and GABA secreted by β cells inhibit α cells: when blood glucose rises, the secretion of glucagon is suppressed as insulin increases.
- Glucagon secreted by α cells (and a little GLP-1) acts on the GLP-1 receptor and the glucagon receptor of β cells, enhancing glucose-stimulated insulin secretion.

The direction of blood flow in the islet and the arrangement of the cells affect the strength of these interactions; in human islets the three cell types are intermingled, whereas in rodents the β cells are in the center and the α and δ cells at the periphery, so the way in which paracrine signaling is organized differs among species. The blood glucose of the body is a whole-body variable, but before releasing hormones into the blood the islet first integrates and corrects in a local network, making the output more stable (see Chapter 35 for details).

### 33.5.7. Local Communication without Paracrine Signaling

Closeness does not necessarily mean the use of paracrine signaling. Diffusion takes time: from the diffusion time $t \approx x^2/(2D)$ ([Chapter 2](/7.14.2#sec-2.2.1)), a peptide molecule needs about $10^4/(2\times150) \approx 30\,\mathrm{s}$ to diffuse $100\,\mu\mathrm{m}$, whereas a transmitter crosses a $20\,\mathrm{nm}$ synaptic cleft in only about $1\,\mu\mathrm{s}$. Diffusion also produces gradients and "bystander" effects. Therefore:

- when millisecond speed and one-to-one directionality are needed, a chemical synapse is used: the transmitter diffuses only across an extremely narrow cleft and is then taken up again or degraded;
- when strict one-to-one recognition is needed, contact-dependent signaling is used: the immune synapse between a T cell and an antigen-presenting cell recognizes antigen through direct contact of receptors and ligands on the membranes, and diffusible cytokines play only a supporting role, avoiding mistaken activation of neighboring bystander cells;
- when rapid synchronization of a group of cells is needed, gap junctions are used: islet β cells are coupled through connexin Cx36, which synchronizes the $\ce{Ca^2+}$ oscillations and insulin secretion of the whole islet, something paracrine signaling cannot do.

Endocrine signaling, portal systems, paracrine signaling, synapses and gap junctions form a continuous spectrum: the shorter and more dedicated the path of the signal, the higher the speed and precision and the smaller the range covered. The body chooses one or several of them according to the needs of each task for speed, precision and coverage.

## 33.6. Evolution and Comparison

### 33.6.1. Conservation of Pulsatile Secretion and Portal Systems

Pulsatile secretion is widespread among vertebrates. In mammals (sheep, rhesus monkey, humans and others), the pulses of GnRH and LH have been measured directly, and pulsatile secretion of LH has also been reported in birds and teleosts; the sexually dimorphic pattern of growth hormone secretion (Section 33.2.4) is most pronounced in rats and mice, and weaker differences also exist in humans. This suggests that pulse coding is an ancient feature of vertebrate endocrine axes, possibly related to the synchronous firing of the GnRH neuronal network and the universality of receptor desensitization.

Portal structures are also ancient. The hepatic portal vein is found in all vertebrates: blood from the digestive tract passes through the liver first, which serves the common need to absorb nutrients and to deal with toxins. The renal portal vein is found in fish, amphibians, reptiles and birds: venous blood from the hindlimbs and tail first passes through the capillaries around the renal tubules before returning to the heart; mammals have no renal portal vein.

### 33.6.2. The Teleost Pituitary: Direct Innervation

The way in which the hypothalamus controls the anterior pituitary differs among vertebrates, which provides a set of natural experiments for the "path design" of Section 33.5:

| Group | Pathway from hypothalamus to adenohypophysis |
|---|---|
| Lampreys (cyclostomes) | No median eminence or portal system and no direct innervation; products of the neurohypophysis diffuse through connective tissue to the adenohypophysis |
| Cartilaginous fish, lungfish, tetrapods | Median eminence and portal system (as in mammals) |
| Teleosts (most) | No typical median eminence or portal system; axons of hypothalamic neurons extend directly into the adenohypophysis and terminate near endocrine cells |

The direct innervation of teleosts amounts to changing the delivery of the "upstream control signal" from portal delivery to an almost synaptic one: the releasing hormone diffuses from the axon terminal directly to neighboring adenohypophyseal cells, with a shorter path and a more concentrated signal, and different cell populations can be controlled separately. The different pathways solve the same problem (letting a minute hypothalamic signal reach the adenohypophysis at a high concentration), only teleosts solve it by neural means and tetrapods by vascular means.

## Summary

The design of hormone signals can be organized in four links: sending, transport, reception and spatial structure:

| Link | Problem | Mechanism and model | Example |
|---|---|---|---|
| Why needed | Nerves are fast and precise but every target needs a dedicated line | Order-of-magnitude estimate of resting cost (Examples 33.1.1, 33.1.2) | If systemic hormones were replaced by nerves, about 1 L of axons and about 6% of ATP turnover would be needed |
| Sending | Remain readable after dilution and clearance; avoid desensitization; carry more information | Pulse–clearance, trough-to-peak ratio $2^{-T/t_{1/2}}$ (Eq. 33.2); convection–dispersion wave packet (Eq. 33.4); desensitization model (Eq. 33.5); frequency coding; precursor silencing | GnRH pulses (Example 33.2.2); sexual dimorphism of GH; $\mathrm{T_4}$ |
| Transport | Protect, buffer and deliver uniformly | Two-compartment model and MRT (Eqs. 33.7, 33.8); PBK model; free hormone hypothesis (Definition 33.3.1) | GH and GHBP; half-life of thyroid hormone 6.3 d / 4.8 d |
| Reception | Unload within a second or two and keep a high local concentration | Lowering affinity (Example 33.4.1, α ≈ 7.6); uptake-driven one-way dissociation (Eq. 33.11, 86% vs 0.33%); local activation by deiodinases | CBG and inflammation; testosterone; D2 |
| Space | When whole-body broadcast is not needed | Flow dilution in portal systems $\Delta C \approx J/Q$ (Eqs. 33.12, 33.13) and the first-pass effect (Definition 33.5.3); paracrine $\lambda = \sqrt{D/k}$ (Eq. 33.14) | Hypothalamic–pituitary portal system (about $10^4$-fold); pancreas–liver; NO (λ about 20–60 µm); islet microcircuit |

- Evolution: pulsatile secretion and the hepatic portal vein are widely conserved among vertebrates; the pathway controlling the anterior pituitary has three schemes: diffusion (lampreys), a portal system (tetrapods) and direct innervation (teleosts).

## Questions

1. The half-life of cortisol is about $70\,\mathrm{min}$ and it has a pulse about every $60$–$90\,\mathrm{min}$ superimposed on the circadian rhythm; ACTH has a half-life of about $10\,\mathrm{min}$ and a similar pulse interval. Compare the trough-to-peak ratios of the two with Eq. (33.2), and explain why plasma fluctuations of cortisol are smoother than those of ACTH.

   **Answer** Take the pulse interval $T = 70\,\mathrm{min}$. ACTH: $T/t_{1/2} = 7$, trough-to-peak ratio $2^{-7} \approx 0.008$, falling almost to zero, so the pulses are very sharp. Cortisol: $T/t_{1/2} = 1$, trough-to-peak ratio $0.5$, so the trough is still half the peak. A hormone with a long half-life acts as a low-pass filter on a pulsatile input, so the amplitude of the cortisol pulses is compressed and the period appears longer. In addition, the cortisol secretion caused by each ACTH pulse itself lasts for a while, smoothing out the fluctuations further.

2. Use the model of Eq. (33.5) to explain why, for the same mean GnRH concentration, continuous administration suppresses LH secretion while pulsatile administration maintains it. Under what parameter conditions does the difference vanish?

   **Answer** Under continuous administration $R_{\mathrm{a}}$ is constant, and the desensitization $D$ tends to $k_{\mathrm{d}}R_{\mathrm{a}}/(k_{\mathrm{d}}R_{\mathrm{a}} + k_{\mathrm{r}})$; if $k_{\mathrm{d}}R_{\mathrm{a}} \gg k_{\mathrm{r}}$, $D$ approaches 1 and the effective signal $S = R_{\mathrm{a}}(1 - D)$ is very small, and together with the threshold property of the output, LH secretion almost stops. Under pulsatile administration, $R_{\mathrm{a}}$ falls to zero between pulses and $D$ recovers as $\mathrm{e}^{-k_{\mathrm{r}}t}$; if the trough lasts $\gtrsim 1/k_{\mathrm{r}}$, $D$ is already small when each pulse arrives and a large peak signal can be produced. When desensitization is very weak ($k_{\mathrm{d}} \ll k_{\mathrm{r}}$), continuous stimulation does not raise $D$ either and the difference vanishes; when recovery is very slow ($1/k_{\mathrm{r}}$ much longer than the pulse interval), there is no time to recover between pulses, pulsatile administration also gradually desensitizes, and the difference again vanishes. The pulse interval must therefore be matched to the time constant of recovery.

3. In Example 33.4.2, if the capillary transit time is shortened to $0.5\,\mathrm{s}$ (as when blood flow speeds up during exercise), what does the proportion of albumin-bound testosterone released in one pass in the target tissue become? What does this imply for the total amount of testosterone the target tissue receives per minute?

   **Answer** $\eta = 1 - \mathrm{e}^{-2\times0.5} = 1 - \mathrm{e}^{-1} \approx 63\%$. The proportion released per pass falls, but the blood volume flowing through per unit time doubles, and the total released per minute is proportional to $Q\eta$: $2 \times 0.63 = 1.26$, which is about $47\%$ more than the original $1 \times 0.86$. In general, when $k_{\mathrm{off}}\tau \gg 1$ almost everything is released and the amount released per minute is proportional to the blood flow $Q$ (flow limited); when $k_{\mathrm{off}}\tau \ll 1$, $\eta \approx k_{\mathrm{off}}\tau$ and $\tau = V_{\mathrm{cap}}/Q$ ($V_{\mathrm{cap}}$ the capillary volume), so the amount released per minute $Q\eta \approx k_{\mathrm{off}}V_{\mathrm{cap}}$ is independent of the blood flow (dissociation limited).

4. A hypothalamic releasing hormone is secreted with flux $J$. Estimate the ratio of the concentrations seen by the anterior pituitary when it enters the pituitary portal system directly ($Q = 0.5\,\mathrm{mL\,min^{-1}}$) and when it enters the internal jugular vein and reaches the pituitary through the systemic circulation. If the hormone has a half-life in plasma of only $5\,\mathrm{min}$, what further problems would the systemic scheme bring?

   **Answer** By Eq. (33.13) the ratio is about $Q_{\mathrm{systemic}}/Q_{\mathrm{portal}} = 5000/0.5 = 10^4$. To obtain the same concentration in the systemic circulation, the amount secreted would have to increase about ten-thousandfold. In addition, once in the systemic circulation the hormone would distribute throughout the body, act on other tissues carrying receptors (many releasing hormones have receptors elsewhere too) and be cleared by the various organs; a short half-life makes the steady-state concentration lower still. A pulsatile signal that enters the general circulation is also broadened and lowered by mixing (Eq. 33.4), and frequency coding is hard to preserve. The portal system solves the three problems of concentration, specificity and temporal fidelity at once.

5. (Open question) Use Eq. (33.14) to discuss why paracrine signals within the islet (somatostatin, insulin) can act within the islet but rarely affect the adjacent exocrine pancreas. If a mutation slowed the degradation of the somatostatin secreted by δ cells tenfold, what would you expect to happen?

   **Answer** Approach: somatostatin is a small peptide with $D$ of about $150\,\mu\mathrm{m^2\,s^{-1}}$; in the islet it is degraded by peptidases and carried away quickly by the abundant capillary blood flow, so the effective $k$ is large and $\lambda$ is comparable to the radius of the islet (about $50$–$100\,\mu\mathrm{m}$), and the concentration decays rapidly beyond the edge of the islet; in addition the distribution of receptors limits the range of action. Insulin has an extremely high concentration within the islet and leaves through the portal vein after entering the capillaries, so the concentration around the exocrine tissue is much lower (the direction of blood flow of the islet–acinar portal system also has an influence). If degradation were slowed tenfold, $\lambda$ would increase by about $\sqrt{10} \approx 3$ times, the range of somatostatin would extend over the whole islet and reach neighboring acini and other islets, the secretion of insulin and glucagon would be suppressed more strongly, and the gain of blood glucose regulation would fall (postprandial hyperglycemia, a weakened glucagon response to hypoglycemia); the secretion of exocrine pancreatic enzymes and bicarbonate might also be inhibited. In practice, patients with somatostatinoma develop diabetes, steatorrhea and gallstones, which can serve as a reference for this reasoning.
