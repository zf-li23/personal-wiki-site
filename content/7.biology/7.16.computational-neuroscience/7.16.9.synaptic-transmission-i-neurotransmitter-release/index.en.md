---
title: "Synaptic Transmission I: Neurotransmitter Release"
description: "The time budget of a chemical synapse; the quantal hypothesis as a binomial model, variance–mean and nonstationary fluctuation analysis; Ca²⁺ entry, the five-site sensor model and nanodomain versus microdomain coupling; SNAREs, synaptotagmin, Munc13/18 and the active zone; clearance, vesicle pools and endocytosis; facilitation, depression and post-tetanic potentiation, and the inverse relation between release probability and the paired-pulse ratio."
---

A neuron communicates with its targets mostly through the **chemical synapse**: an **action potential** arriving at the presynaptic terminal is converted into the fusion of a few synaptic vesicles, and their transmitter is converted back into a current in the postsynaptic cell. This chapter follows the presynaptic half of that conversion. Its central lesson is that release is a probabilistic, quantized and $\ce{Ca^2+}$-controlled process, and that the three parameters of a simple statistical model, the number of release sites $N$, the release probability $p$ and the quantal size $q$, organize almost everything that is known about it, from the experiments of Katz in the 1950s to the molecular machinery of the active zone. The basic physiology of the synapse and the classical quantal experiments at the frog **neuromuscular junction** are in [7.14.5](/7.14.5#sec-5.4) and [7.14.8](/7.14.8#sec-8.3.3), and the electrical properties of the membrane in [7.16.4](/7.16.4) and [7.16.5](/7.16.5); here we treat release quantitatively and at central synapses. The postsynaptic receptors follow in [7.16.10](/7.16.10), slow metabotropic signaling in [7.16.11](/7.16.11), and the phenomena of **short-term plasticity** introduced at the end of this chapter are turned into a dynamical model in [7.16.12](/7.16.12).

## 9.1. The Chemical Synapse and Its Time Budget

Seen in the electron microscope, every chemical synapse has the same parts (Luo, Kandel): a presynaptic bouton filled with clear synaptic vesicles of about $40\,\mathrm{nm}$ diameter, a patch of presynaptic membrane where a few of them are docked, a cleft of $20\,\mathrm{nm}$ at central synapses ($50\,\mathrm{nm}$ at the neuromuscular junction, where it contains a basal lamina), and opposite it a thickening of the postsynaptic membrane, the **postsynaptic density**, which anchors the receptors. A typical bouton in hippocampal area CA1 contains about 200 vesicles and has a single active zone of $0.04$–$0.1\,\mu\mathrm{m^2}$ with five to ten docked vesicles; a motor nerve terminal on one muscle fiber has hundreds of active zones.

**Definition 9.1.1 (Active Zone)** The **active zone** is the specialized region of the presynaptic plasma membrane where synaptic vesicles dock and fuse; it is defined by a dense protein matrix (RIM, Munc13, RIM-binding protein, ELKS, liprin-α, Bassoon and Piccolo) that clusters voltage-gated $\ce{Ca^2+}$ channels and holds vesicles next to them, and it lies exactly opposite the postsynaptic density.

The **synaptic delay** of about $0.5\,\mathrm{ms}$ between the presynaptic action potential and the onset of the postsynaptic current can be divided into steps whose durations are known from paired recordings at large synapses (the squid giant synapse, the calyx of Held in the auditory brainstem, the mossy fiber bouton of the hippocampus) and from capacitance and imaging measurements:

| Step | Duration at $35$–$37^\circ\mathrm{C}$ | Evidence |
|---|---|---|
| Invasion of the terminal by the action potential | $\approx 0.1\,\mathrm{ms}$ | Recordings from boutons and calyces |
| Opening of voltage-gated $\ce{Ca^2+}$ channels (mostly $\mathrm{Ca_V2.1}$, P/Q-type, and $\mathrm{Ca_V2.2}$, N-type) | $0.1$–$0.3\,\mathrm{ms}$; most $\ce{Ca^2+}$ enters during the repolarization of the spike | Presynaptic voltage clamp |
| $\ce{Ca^2+}$ binding to the sensor and fusion of the vesicle | $50$–$200\,\mu\mathrm{s}$ | Delay from $\ce{Ca^2+}$ current to postsynaptic current (Sabatini and Regehr, 1996) |
| Diffusion of transmitter across the cleft | about $1\,\mu\mathrm{s}$ | $t \approx x^2/2D$ ([7.14.5](/7.14.5#sec-5.4.2)) |
| Binding and opening of postsynaptic receptors | $0.1$–$0.2\,\mathrm{ms}$ | Fast application to excised patches |

At room temperature every step is two to three times slower ($Q_{10} \approx 2$–$3$), which is why the classical delays measured in frog and squid preparations are $1$–$2\,\mathrm{ms}$. The budget shows where the time goes: not into diffusion, but into opening channels and fusing membranes. The experiment that isolated the $\ce{Ca^2+}$ step was done at the squid giant synapse with both sides voltage-clamped and $\ce{Na+}$ and $\ce{K+}$ channels blocked (Llinás; Augustine, Charlton and Smith, 1985). A step of the presynaptic membrane to $-25\,\mathrm{mV}$ opened $\ce{Ca^2+}$ channels, $\ce{Ca^2+}$ flowed in and a postsynaptic current followed. A step to $+50\,\mathrm{mV}$, close to the $\ce{Ca^2+}$ **equilibrium potential**, opened even more channels but gave almost no influx and no release; on repolarization a "tail" of $\ce{Ca^2+}$ current flowed through the still-open channels and release followed within about $0.2\,\mathrm{ms}$. Depolarization itself is therefore not the trigger: entry of $\ce{Ca^2+}$ is.

## 9.2. The Quantal Hypothesis

### 9.2.1. Quanta and the Binomial Model

At the frog neuromuscular junction, Fatt and Katz found spontaneous *miniature end-plate potentials* (mEPPs) of about $0.5\,\mathrm{mV}$, and del Castillo and Katz showed that at low $\ce{Ca^2+}$ the evoked **end-plate potential** takes only values close to integer multiples of the mEPP ([7.14.8](/7.14.8#sec-8.3.3)). The electron microscope then supplied the physical quantum, the synaptic vesicle, and the freeze-fracture images of Heuser and Reese (1979), taken from junctions frozen $3$–$5\,\mathrm{ms}$ after a stimulus, caught vesicles in the act of fusion. One quantum at the frog junction contains about 7000 acetylcholine molecules; a glutamatergic vesicle at a central synapse contains a few thousand glutamate molecules. The statistical model behind the quantal hypothesis is general and is the starting point of this section.

**Definition 9.2.1 (Binomial Model of Release)** A synaptic connection is described by $N$ independent release sites, each of which releases one vesicle with probability $p$ when an action potential arrives. The number of released vesicles is then $K \sim \mathrm{Bin}(N, p)$, and the postsynaptic response is $A = \sum_{j=1}^{K} Q_j$, where the quantal amplitudes $Q_j$ are independent with mean $q$ (the quantal size) and coefficient of variation $C_V^{(q)}$. The mean number of released quanta $Np$ is called the **quantal content** of the connection.

The model contains the Poisson model of [7.14.8](/7.14.8) as a limit: when $N \to \infty$ and $p \to 0$ with $Np$ fixed, the **binomial distribution** tends to the **Poisson distribution** with mean $Np$ (which 7.14.8 writes $m$; we keep $m$ for the gating variable of [7.16.5](/7.16.5)). At the neuromuscular junction with hundreds of active zones and low $\ce{Ca^2+}$ the Poisson limit is accurate; at a central connection made by one to ten active zones it is not, and the finite $N$ becomes visible in the statistics.

**Proposition 9.2.1 (Moments of the Quantal Response)** In the binomial model,
$$
\mathbb{E}[A] = Npq, \qquad \operatorname{Var}(A) = Npq^2\left(1 - p + (C_V^{(q)})^2\right), \qquad \mathbb{P}(A = 0) = (1 - p)^N. \tag{9.1}
$$

**Proof** Condition on $K$. Given $K$, $A$ is a sum of $K$ independent quanta, so $\mathbb{E}[A \mid K] = Kq$ and $\operatorname{Var}(A \mid K) = K(C_V^{(q)}q)^2$. By the law of total expectation $\mathbb{E}[A] = q\,\mathbb{E}[K] = Npq$, and by the law of total variance $\operatorname{Var}(A) = \mathbb{E}[\operatorname{Var}(A\mid K)] + \operatorname{Var}(\mathbb{E}[A\mid K]) = Np(C_V^{(q)})^2q^2 + Np(1-p)q^2$. A failure means $K = 0$, which has probability $(1-p)^N$. $\square$

The amplitude distribution is a mixture of $N + 1$ peaks at $0, q, 2q, \dots, Nq$ with binomial weights, each peak broadened by quantal variability (width $\propto \sqrt{k}$) and recording noise (figure below, A). Clear peaks are seen only when $C_V^{(q)}$ and the noise are small, which is why quantal peaks are elusive at most central synapses; then the moments of Eq. (9.1) carry the information instead.

### 9.2.2. Variance–Mean Analysis

Eliminating $p$ between the mean $\mu = Npq$ and the variance in Eq. (9.1) gives a relation that holds for every release probability.

**Proposition 9.2.2 (Variance–Mean Parabola)** If $N$ and $q$ stay fixed while $p$ is changed (for example by changing the extracellular $\ce{Ca^2+}$ concentration), the mean $\mu$ and variance $\sigma^2$ of the response lie on the parabola
$$
\sigma^2 = q'\mu - \frac{\mu^2}{N}, \qquad q' = q\left(1 + (C_V^{(q)})^2\right). \tag{9.2}
$$
Its initial slope is $q'$, it reaches its maximum $Nq'^2/4$ at $\mu = Nq'/2$ (that is, at $p = 1/2$ when $C_V^{(q)}$ is negligible), and it returns to zero at $\mu = Nq'$.

This is multiple-probability fluctuation analysis (Silver, Clements and colleagues, 1998–2000): record many responses at three or more $\ce{Ca^2+}$ concentrations, plot variance against mean and fit Eq. (9.2) through the origin. The initial slope gives the quantal size, the curvature the number of sites, and then $p = \mu/(Nq)$ at each concentration. The analysis needs no visible quantal peaks, only stationarity of $N$ and $q$ during the recording.

**Example 9.2.1** At a cerebellar connection the mean and variance of the EPSC (after subtracting the variance of the baseline noise) are measured at three $\ce{Ca^2+}$ concentrations: $\mu = 32$, $80$ and $128\,\mathrm{pA}$ with $\sigma^2 = 512$, $800$ and $512\,\mathrm{pA^2}$. The first and third points have equal variance, so by the symmetry of the parabola its maximum lies at $\mu = 80\,\mathrm{pA} = Nq'/2$; the maximum value $800 = Nq'^2/4$ then gives $q' = 4\cdot 800/160 = 20\,\mathrm{pA}$ and $N = 160/20 = 8$. Check with the first point: $20\cdot 32 - 32^2/8 = 640 - 128 = 512$. The release probabilities at the three concentrations are $32/160 = 0.2$, $0.5$ and $0.8$, and the quantal content at the highest is $Np = 6.4$.

:::

![Quantal statistics at a central connection with $N = 6$ release sites and quantal size $q = 10\,\mathrm{pA}$ ($C_V^{(q)} = 0.25$, recording noise $1.5\,\mathrm{pA}$). A: amplitude histograms of 600 simulated trials at three release probabilities, with the binomial mixture densities of Definition 9.2.1. At $p = 0.15$ failures dominate and peaks at $q$ and $2q$ are visible (dotted lines at integer multiples of $q$); at higher $p$ the peaks merge and the distribution shifts to the right. B: variance–mean analysis of simulated recordings at nine release probabilities (200 trials each). The parabola fitted through the origin (Eq. (9.2)) recovers $q$ and $N$ close to their true values (dashed).](./plots/quantal-statistics.py)

### 9.2.3. Fluctuations of the Postsynaptic Channels

The same binomial arithmetic applies on the postsynaptic side, with channels in place of vesicles. If $N_{\mathrm{ch}}$ channels each are open with probability $p_{\mathrm{o}}$ and pass a single-channel current $i$, the macroscopic current has mean $I = N_{\mathrm{ch}}p_{\mathrm{o}}i$ and variance $\sigma_I^2 = N_{\mathrm{ch}}p_{\mathrm{o}}(1-p_{\mathrm{o}})i^2$, so that
$$
\sigma_I^2 = iI - \frac{I^2}{N_{\mathrm{ch}}}. \tag{9.3}
$$
Katz and Miledi (1970) were the first to use this idea: applying acetylcholine to the end plate increased the voltage noise of the membrane ("shot noise"), and from the ratio of variance to mean they estimated an elementary conductance of order $10^{-10}\,\mathrm{S}$ lasting about a millisecond, years before single channels could be recorded with the **patch clamp**. In nonstationary fluctuation analysis (Sigworth, 1980) the **open probability** changes in time, during the decay of a synaptic current or during the activation of a voltage-gated current, and many repetitions of the same response give the mean and the variance at each instant; plotting one against the other traces Eq. (9.3) and yields $i$ (hence the **single-channel conductance** $\gamma = i/(V - E_{\mathrm{rev}})$) and $N_{\mathrm{ch}}$. Applied to currents evoked by two-photon uncaging of glutamate onto single dendritic spines, it showed that the number of **AMPA receptors** at a synapse grows in proportion to the volume of the spine head, from a few to more than a hundred (Matsuzaki and colleagues, 2001). Fluctuations, which the macroscopic equations of [7.16.4](/7.16.4) average away, are thus a microscope for counting molecules.

## 9.3. Calcium and Release

### 9.3.1. The Cooperativity of the Ca²⁺ Sensor

Release grows steeply with extracellular $\ce{Ca^2+}$, approximately as its fourth power at low concentrations (Dodge and Rahamimoff, 1967; [Proposition 5.4.1](/7.14.5#prop-5.4.1)). That measurement mixes two steps, $\ce{Ca^2+}$ entry and the response of the sensor to the intracellular concentration. The second step was measured directly at the calyx of Held, a terminal large enough to be patch-clamped and loaded with caged $\ce{Ca^2+}$: a flash of ultraviolet light raises $[\ce{Ca^2+}]_{\mathrm{i}}$ uniformly to a value read by a fluorescent indicator, and the postsynaptic current or the presynaptic capacitance reports release (Bollmann, Sakmann and Borst, 2000; Schneggenburger and Neher, 2000). Release rate rose with the fourth to fifth power of $[\ce{Ca^2+}]_{\mathrm{i}}$ and required about $10$–$25\,\mu\mathrm{M}$ to release the readily releasable pool within a few milliseconds, a concentration that the bulk cytosol never reaches but that exists for a fraction of a millisecond next to open channels.

**Formula 9.3.1 (Five-Site Sensor Model)** Let a vesicle carry a sensor with five $\ce{Ca^2+}$-binding sites, and let $V_j$ denote the state with $j$ sites occupied. Binding is sequential,
$$
V_0 \underset{k_{\mathrm{off}}}{\overset{5k_{\mathrm{on}}c}{\rightleftharpoons}} V_1 \underset{2bk_{\mathrm{off}}}{\overset{4k_{\mathrm{on}}c}{\rightleftharpoons}} V_2 \underset{3b^2k_{\mathrm{off}}}{\overset{3k_{\mathrm{on}}c}{\rightleftharpoons}} V_3 \underset{4b^3k_{\mathrm{off}}}{\overset{2k_{\mathrm{on}}c}{\rightleftharpoons}} V_4 \underset{5b^4k_{\mathrm{off}}}{\overset{k_{\mathrm{on}}c}{\rightleftharpoons}} V_5 \overset{\gamma}{\longrightarrow} \text{fused},
$$
where $c = [\ce{Ca^2+}]_{\mathrm{i}}$, and the factor $b < 1$ makes each bound ion slow the unbinding of the others (cooperativity). The fit to the calyx data gives $k_{\mathrm{on}} \approx 9\times10^7\,\mathrm{M^{-1}\,s^{-1}}$, $k_{\mathrm{off}} \approx 9500\,\mathrm{s^{-1}}$, $b \approx 0.25$ and a fusion rate $\gamma \approx 6000\,\mathrm{s^{-1}}$ (Schneggenburger and Neher, 2000).

At low $c$ the occupancy of $V_5$ is proportional to $c^5$, and the apparent power falls toward 4 and then toward 0 as the sites saturate (figure below, A), which reconciles the cooperativity of about four seen in extracellular titrations with five binding sites. Later models added a slow $\ce{Ca^2+}$-independent fusion from partially bound states to account for spontaneous release, and an allosteric variant (Lou, Scheuss and Schneggenburger, 2005) in which each bound ion multiplies the fusion rate rather than all five being required. Both describe the same essential fact: fusion is a highly nonlinear function of local $\ce{Ca^2+}$, an example of **ultrasensitivity** built from **cooperativity**.

### 9.3.2. Nanodomains and Microdomains

Because the sensor needs tens of micromolar, the distance between the open channel and the vesicle matters as much as the number of channels. Around the mouth of one open channel $\ce{Ca^2+}$ diffuses into the cytosol while buffers bind it; in the linearized buffer approximation (Neher, 1986) the steady profile, established within microseconds, is
$$
c(r) = c_0 + \frac{i_{\mathrm{Ca}}}{4\pi zFDr}\,\mathrm{e}^{-r/\lambda_{\mathrm{B}}}, \qquad \lambda_{\mathrm{B}} = \sqrt{\frac{D}{k_{\mathrm{on}}^{\mathrm{B}}[\mathrm{B}]}}, \tag{9.4}
$$
where $i_{\mathrm{Ca}}$ is the single-channel current, $z = 2$, $D \approx 220\,\mu\mathrm{m^2\,s^{-1}}$ the diffusion coefficient of $\ce{Ca^2+}$, and $\lambda_{\mathrm{B}}$ the length over which a buffer at concentration $[\mathrm{B}]$ with binding rate $k_{\mathrm{on}}^{\mathrm{B}}$ captures the ions. Without buffer the profile falls as $1/r$, the steady solution of the diffusion equation around a point source ([7.6.35](/7.6.35)). For $i_{\mathrm{Ca}} = 0.3\,\mathrm{pA}$, a typical value during an action potential at $2\,\mathrm{mM}$ external $\ce{Ca^2+}$, Eq. (9.4) gives about $28\,\mu\mathrm{M}$ at $20\,\mathrm{nm}$ and $6\,\mu\mathrm{M}$ at $100\,\mathrm{nm}$.

**Definition 9.3.1 (Nanodomain and Microdomain Coupling)** Release is said to have **nanodomain coupling** when the vesicle's sensor lies within about $10$–$30\,\mathrm{nm}$ of one or a few $\ce{Ca^2+}$ channels, so that the local $\ce{Ca^2+}$ of those channels alone triggers fusion, and **microdomain coupling** when the sensor lies $100\,\mathrm{nm}$ or more from a cluster of channels whose overlapping $\ce{Ca^2+}$ domains sum.

The two regimes are distinguished experimentally with exogenous buffers of different speed (Adler and colleagues, 1991; Eggermann and colleagues, 2012). BAPTA and EGTA have similar affinities, but BAPTA binds $\ce{Ca^2+}$ about 40 times faster. In Eq. (9.4) $10\,\mathrm{mM}$ BAPTA shortens $\lambda_{\mathrm{B}}$ to about $7\,\mathrm{nm}$ and blocks release in both regimes, whereas $10\,\mathrm{mM}$ EGTA gives $\lambda_{\mathrm{B}} \approx 50\,\mathrm{nm}$ and blocks only microdomain release (figure below, B and C). By this test the synapses of fast-spiking basket cells, the squid giant synapse and the mature calyx of Held use nanodomain coupling, whereas the immature calyx and some cortical synapses are more loosely coupled. Tight coupling makes transmission fast, temporally precise and energy-efficient, because few channels need to open per vesicle; it also means that a single channel's opening can decide whether a vesicle fuses, and so contributes to the stochasticity of release.

![The $\ce{Ca^2+}$ sensor and the geometry of $\ce{Ca^2+}$ domains. A: peak release rate per vesicle in the five-site model (Formula 9.3.1) after a step of intracellular $\ce{Ca^2+}$; on logarithmic axes the slope is close to 5 at low concentrations (the dashed line has slope 4) and the curve saturates above about $50\,\mu\mathrm{M}$. B: steady $[\ce{Ca^2+}]$ around one open channel (Eq. (9.4), $i_{\mathrm{Ca}} = 0.3\,\mathrm{pA}$) without exogenous buffer and with $10\,\mathrm{mM}$ of the slow buffer EGTA or the fast buffer BAPTA. C: release rate predicted by the model at the local $[\ce{Ca^2+}]$ of B, relative to the unbuffered case, against the channel–sensor distance: EGTA leaves nanodomain coupling (yellow band) nearly intact but suppresses microdomain coupling (gray band) by orders of magnitude; BAPTA suppresses both.](./plots/calcium-sensor.py)

## 9.4. The Molecular Machinery of Release

### 9.4.1. SNAREs

Membrane fusion is driven by the **SNARE** proteins, whose general mechanism of zippering is described in [7.3.8](/7.3.8#sec-8.4.2): synaptobrevin (VAMP2) on the vesicle and syntaxin-1 and SNAP-25 on the plasma membrane form a four-helix bundle that pulls the two bilayers together; NSF and α-SNAP disassemble the complexes after fusion. The decisive evidence at the synapse came from toxins: the clostridial neurotoxins are proteases that each cleave one SNARE at one bond ([7.14.5](/7.14.5#sec-5.4.2)), and each blocks release. Estimates of the number of SNARE complexes needed per fusion event range from one to three, and the energy released by their assembly (tens of $k_{\mathrm{B}}T$ per complex) is comparable to the barrier for fusing two bilayers. SNAREs alone fuse liposomes in minutes; synaptic fusion takes less than a millisecond and is triggered by $\ce{Ca^2+}$. Speed and $\ce{Ca^2+}$ control are supplied by additional proteins.

### 9.4.2. Synaptotagmin, the Ca²⁺ Sensor

**Definition 9.4.1 (Synaptotagmin)** **Synaptotagmin**-1 is a vesicle membrane protein with two cytoplasmic $\ce{Ca^2+}$-binding C2 domains (C2A binding three and C2B two $\ce{Ca^2+}$ ions) that acts as the $\ce{Ca^2+}$ sensor for fast synchronous release: on binding $\ce{Ca^2+}$ its C2 domains insert into the phospholipid membrane and act on the partially zippered SNARE complex to trigger fusion.

Three lines of evidence identify it as the sensor (Südhof and colleagues). Knockout mice lacking synaptotagmin-1 lose the fast synchronous component of release triggered by an action potential, whereas spontaneous release and slow asynchronous release persist or even increase (Geppert and colleagues, 1994). A point mutation in C2A (R233Q) that halves the $\ce{Ca^2+}$ affinity of the protein in vitro, knocked into the mouse, halves the apparent $\ce{Ca^2+}$ affinity of release without changing its cooperativity (Fernández-Chacón and colleagues, 2001): a quantitative match between a biochemical constant and a physiological one, which is the strongest kind of evidence for a molecular mechanism. And the five $\ce{Ca^2+}$ ions bound by the two C2 domains correspond to the five sites of Formula 9.3.1. Synaptotagmin-2 plays the same role at the calyx of Held and the neuromuscular junction; the higher-affinity, slower synaptotagmin-7 mediates asynchronous release and contributes to facilitation (9.6); complexin clamps the SNARE complex so that spontaneous fusion is rare until $\ce{Ca^2+}$ arrives.

### 9.4.3. Priming and the Active Zone

A vesicle must be docked and primed before $\ce{Ca^2+}$ can release it.

**Definition 9.4.2 (Readily Releasable Pool)** The **readily releasable pool** (RRP) of a terminal is the set of docked and primed vesicles that can fuse within milliseconds of a strong $\ce{Ca^2+}$ signal; it is measured as the release evoked by a hypertonic sucrose solution, by a long depolarization or by a high-frequency train, and contains about five to ten vesicles per active zone at small central synapses.

Priming is carried out by Munc18-1 and Munc13. Munc18-1 binds syntaxin-1 and templates the assembly of the SNARE complex, and Munc13 opens the closed conformation of syntaxin so that the complex can form. Deleting either protein abolishes evoked and spontaneous release; strikingly, mice lacking Munc18-1 still build a brain with normal layered structure and synapses before dying at birth (Verhage and colleagues, 2000), which separates the role of transmitter release from that of synapse formation. At the active zone, RIM binds Munc13 (promoting priming), binds RIM-binding protein and the $\ce{Ca^2+}$ channels (recruiting channels to the release site) and binds the vesicle protein Rab3; the active zone thus sets both the size of the RRP ($N$) and the coupling distance that determines $p$ (9.3.2). Super-resolution imaging shows that release sites and postsynaptic receptor clusters are aligned in "nanocolumns" of about $80\,\mathrm{nm}$ (Tang and colleagues, 2016), so that the transmitter of a vesicle lands where the receptors are densest.

| Protein | Location | Role | Loss of function |
|---|---|---|---|
| Synaptobrevin, syntaxin-1, SNAP-25 | Vesicle; plasma membrane | Fusion (SNARE complex) | Cleaved by clostridial toxins; release blocked |
| Synaptotagmin-1 / -2 | Vesicle | $\ce{Ca^2+}$ sensor for synchronous release | Synchronous release lost, asynchronous remains |
| Complexin | Cytosol, on SNAREs | Clamp and activation | Spontaneous release increased, evoked reduced |
| Munc18-1 | Cytosol, on syntaxin | SNARE assembly, priming | No release |
| Munc13 | Active zone | Opens syntaxin, priming | No release |
| RIM, RIM-BP | Active zone | Recruit Munc13 and $\ce{Ca^2+}$ channels | Fewer primed vesicles, looser coupling |

## 9.5. Clearance and the Vesicle Cycle

After fusion the transmitter must be removed from the cleft, and the vesicle membrane must be retrieved and refilled. The **neurotransmitter** is cleared by diffusion out of the cleft, by enzymatic hydrolysis (acetylcholinesterase at cholinergic synapses, [7.14.8](/7.14.8#sec-8.4.2)) and by **transporters**: plasma-membrane transporters driven by the $\ce{Na+}$ gradient take up glutamate (mainly into astrocytes, through EAAT2), GABA, glycine and the monoamines. The time course of glutamate in the cleft was estimated from the displacement of a rapidly dissociating antagonist: after release of one vesicle the concentration peaks at about $1$–$3\,\mathrm{mM}$ and decays with a time constant of about $1\,\mathrm{ms}$ (Clements and colleagues, 1992). Transporters bind glutamate fast but transport it slowly (tens of milliseconds per cycle), so their first action is buffering; their density determines how much glutamate spills over to neighboring synapses and to extrasynaptic NMDA and metabotropic receptors.

Vesicles are refilled by vesicular transporters (VGLUT for glutamate, VGAT for GABA and glycine, VMAT for monoamines, VAChT for acetylcholine) driven by the proton gradient that the vacuolar $\ce{H+}$-ATPase creates across the vesicle membrane; which vesicular transporter a neuron expresses defines its transmitter identity. The membrane is retrieved by several routes that differ in speed:

- clathrin-mediated **endocytosis**, with **clathrin** coats and scission by **dynamin**, taking $10$–$20\,\mathrm{s}$; the *Drosophila* temperature-sensitive dynamin mutant *shibire* empties its terminals of vesicles and becomes paralyzed within minutes at $29^\circ\mathrm{C}$, a classical demonstration that recycling is required to sustain transmission;
- ultrafast endocytosis at the edge of the active zone within $50$–$100\,\mathrm{ms}$ of fusion (Watanabe and colleagues, 2013, by "flash-and-freeze" electron microscopy), followed by regeneration of vesicles from endosomes;
- "kiss-and-run", a transient fusion pore that closes again without full collapse of the vesicle, whose importance at central synapses is debated.

The vesicles of a terminal are commonly divided into the RRP, a recycling pool (about 10–20% of the vesicles) that refills it during moderate activity, and a reserve pool mobilized only by intense stimulation. The RRP of a hippocampal bouton refills with a time constant of several seconds at rest, faster when $\ce{Ca^2+}$ is elevated, and this refilling rate limits the sustained rate of transmission.

## 9.6. Short-Term Plasticity

The amount of transmitter released by an action potential depends on the history of the terminal over the preceding milliseconds to minutes. These changes are a form of **synaptic plasticity** that requires no change of the postsynaptic cell or of gene expression; they arise from the dynamics of presynaptic $\ce{Ca^2+}$ and of the vesicle pools.

**Definition 9.6.1 (Paired-Pulse Ratio)** When two action potentials arrive at a synapse separated by an interval $\Delta t$, the ratio $A_2/A_1$ of the mean amplitudes of the second and first postsynaptic responses is the **paired-pulse ratio** (PPR). The synapse shows **paired-pulse facilitation** if the ratio exceeds 1 and **paired-pulse depression** if it is below 1.

**Definition 9.6.2 (Facilitation, Depression and Post-Tetanic Potentiation)** **Synaptic facilitation** is an increase of release lasting tens to hundreds of milliseconds after one or a few action potentials; **synaptic depression** is a decrease of release during and after repeated activity, recovering over hundreds of milliseconds to seconds; **post-tetanic potentiation** is an increase of release lasting tens of seconds to minutes after a high-frequency train (a tetanus); augmentation is an intermediate component decaying in about $5$–$10\,\mathrm{s}$.

| Component | Decay time constant | Main mechanism |
|---|---|---|
| Facilitation | $10$–$300\,\mathrm{ms}$ | Residual $\ce{Ca^2+}$ acting on a high-affinity sensor (synaptotagmin-7); saturation of local buffers |
| Depression | $0.1$–$10\,\mathrm{s}$ | Depletion of the RRP; also inactivation of $\ce{Ca^2+}$ channels and of release sites, postsynaptic receptor **desensitization** |
| Augmentation | $5$–$10\,\mathrm{s}$ | Accumulated $\ce{Ca^2+}$ |
| Post-tetanic potentiation | $30\,\mathrm{s}$–minutes | $\ce{Ca^2+}$ released slowly from mitochondria; **protein kinase C** activation increasing $p$ and RRP size |

Katz and Miledi (1968) proposed that facilitation is due to residual $\ce{Ca^2+}$ left in the terminal by the first spike, which adds to the $\ce{Ca^2+}$ of the second. Because release depends on about the fourth power of $\ce{Ca^2+}$, a small residue could have a large effect. A quantitative difficulty is that the residual bulk $\ce{Ca^2+}$ (below $1\,\mu\mathrm{M}$) is negligible compared with the tens of micromolar at the sensor; the current view is that it acts on a separate, high-affinity and slow sensor, so that facilitation is still "residual $\ce{Ca^2+}$" but read out by a different molecule (Jackman and colleagues, 2016). Depression, conversely, reflects the finite RRP: a synapse that releases a large fraction of its docked vesicles on the first spike has fewer for the second.

These two mechanisms predict an inverse relation between the initial release probability and the paired-pulse ratio. Let each site release with probability $p$ on the first spike; if a fraction $p$ of the pool has been used and recovers with time constant $\tau_{\mathrm{rec}}$, and the residual $\ce{Ca^2+}$ raises the release probability by $f(1 - p)$ decaying with $\tau_{\mathrm{F}}$, then
$$
\mathrm{PPR} = \frac{\left(1 - p\,\mathrm{e}^{-\Delta t/\tau_{\mathrm{rec}}}\right)\left(p + f(1-p)\,\mathrm{e}^{-\Delta t/\tau_{\mathrm{F}}}\right)}{p}. \tag{9.5}
$$
For small $p$ the ratio exceeds 1 (facilitation dominates); for large $p$ it falls below 1 (depletion dominates). Experiments at single hippocampal boutons, where $p$ varies widely between neighboring terminals of the same axon, confirmed the inverse relation (Dobrunz and Stevens, 1997), and lowering the extracellular $\ce{Ca^2+}$ concentration turns a depressing synapse into a facilitating one (figure below). The PPR is therefore used routinely as an indicator of $p$: a manipulation that changes the PPR is suspected of acting presynaptically. The dynamical version of Eq. (9.5) for trains of spikes, the **Tsodyks–Markram model**, is the subject of [7.16.12](/7.16.12).

**Example 9.6.1** At a synapse with $p = 0.1$ and $\Delta t = 20\,\mathrm{ms}$, with $f = 0.3$, $\tau_{\mathrm{F}} = 50\,\mathrm{ms}$ and $\tau_{\mathrm{rec}} = 500\,\mathrm{ms}$, Eq. (9.5) gives $\mathrm{e}^{-0.4} = 0.67$, $p_2 = 0.1 + 0.3\cdot0.9\cdot0.67 = 0.281$, $x_2 = 1 - 0.1\cdot0.96 = 0.904$ and $\mathrm{PPR} = 0.904\cdot0.281/0.1 \approx 2.5$. With $p = 0.7$ the same parameters give $p_2 = 0.76$, $x_2 = 0.33$ and $\mathrm{PPR} \approx 0.36$. The two synapses could have the same mean first response if the second had seven times fewer sites; they would still transmit very different messages during a burst: the first emphasizes the later spikes of a burst, the second the first spike after a silence.

:::

![Paired-pulse ratio predicted by Eq. (9.5) ($f = 0.3$, $\tau_{\mathrm{F}} = 50\,\mathrm{ms}$, $\tau_{\mathrm{rec}} = 500\,\mathrm{ms}$). A: PPR against the release probability of the first spike for three intervals: synapses with low $p$ facilitate, those with high $p$ depress, and facilitation fades at long intervals. B: PPR at $20\,\mathrm{ms}$ interval against the extracellular $\ce{Ca^2+}$ concentration, with $p = 0.9\,c^4/(c^4 + K^4)$ and $K = 1.5\,\mathrm{mM}$: lowering $\ce{Ca^2+}$ converts depression into facilitation. Inset: two responses normalized to the first at $0.75$ and $2.5\,\mathrm{mM}$ $\ce{Ca^2+}$.](./plots/paired-pulse.py)

Short-term plasticity is not a nuisance superimposed on transmission but a filter. A depressing synapse transmits mainly changes of presynaptic rate (its steady-state output saturates with rate), a facilitating synapse transmits mainly sustained high-frequency bursts; the same axon can make depressing synapses onto one target and facilitating synapses onto another, depending on the molecular composition of each terminal (Markram and colleagues, 1998). Its computational roles, from gain control to the activity-silent working memory of [7.16.45](/7.16.45), are taken up in [7.16.12](/7.16.12).

## Summary

- The synaptic delay of about $0.5\,\mathrm{ms}$ is spent in opening $\ce{Ca^2+}$ channels and in $\ce{Ca^2+}$-triggered fusion, not in diffusion; entry of $\ce{Ca^2+}$, not depolarization, is the trigger (9.1).
- Release is quantal and probabilistic. In the binomial model (Definition 9.2.1) the response has mean $Npq$ and variance $Npq^2(1 - p + (C_V^{(q)})^2)$ (Proposition 9.2.1); varying $p$ traces the variance–mean parabola (Proposition 9.2.2), whose slope and curvature give $q$ and $N$. The same arithmetic applied to channels yields single-channel conductances and receptor numbers (Eq. (9.3)).
- The sensor of fusion binds about five $\ce{Ca^2+}$ ions with cooperativity (Formula 9.3.1) and needs tens of micromolar, available only in the domains around open channels; the coupling distance (Definition 9.3.1), probed with the fast and slow buffers BAPTA and EGTA, sets speed and release probability.
- Fusion is driven by SNAREs, triggered by synaptotagmin (Definition 9.4.1) and prepared by Munc18 and Munc13 at the active zone (Definition 9.1.1), which also positions the $\ce{Ca^2+}$ channels; the readily releasable pool (Definition 9.4.2) is replenished in seconds through several endocytic routes.
- Facilitation (residual $\ce{Ca^2+}$), depression (depletion) and post-tetanic potentiation (Definition 9.6.2) make transmission history-dependent; the paired-pulse ratio (Definition 9.6.1) falls as the initial release probability rises (Eq. (9.5)).

| Quantity | Typical central synapse | Neuromuscular junction |
|---|---|---|
| Release sites $N$ | $1$–$10$ per connection | Hundreds |
| Release probability $p$ | $0.05$–$0.9$, often $0.1$–$0.4$ | Lower per site, but many sites |
| Quantal size $q$ | $5$–$30\,\mathrm{pA}$ | $\approx 0.5\,\mathrm{mV}$ (mEPP) |
| Quantal content $Np$ | $\lesssim 5$ | $50$–$300$ |
| Short-term plasticity | Facilitating or depressing | Depressing |

## Questions

1. Show that in the binomial model the coefficient of variation of the response is $C_V(A) = \sqrt{(1 - p + (C_V^{(q)})^2)/(Np)}$. How does $1/C_V(A)^2$ change if a manipulation changes only $q$, only $p$ or only $N$? Why is this a useful test of the site of action of a manipulation?

   **Answer** From Eq. (9.1), $C_V(A)^2 = \operatorname{Var}(A)/\mathbb{E}[A]^2 = Npq^2(1 - p + (C_V^{(q)})^2)/(Npq)^2$, which gives the formula. It is independent of $q$: a purely postsynaptic change of quantal size (for example more receptors) changes the mean but leaves $C_V$ unchanged, so $1/C_V^2$ stays constant. An increase of $N$ or of $p$ increases $1/C_V^2 = Np/(1 - p + (C_V^{(q)})^2)$ together with the mean. Plotting the relative change of $1/C_V^2$ against the relative change of the mean therefore distinguishes presynaptic changes (points near or above the diagonal) from postsynaptic changes of $q$ (points on the horizontal line); it was used to argue about the locus of expression of long-term potentiation (7.16.14). The test assumes that the binomial model holds and that the manipulation does not change several parameters at once.

2. In a variance–mean analysis, three $\ce{Ca^2+}$ concentrations give $(\mu, \sigma^2) = (15\,\mathrm{pA}, 180\,\mathrm{pA^2})$, $(40, 320)$ and $(60, 288)$. Estimate $q'$, $N$ and the three release probabilities.

   **Answer** With $\sigma^2 = a\mu + b\mu^2$: from the first two points, $180 = 15a + 225b$ and $320 = 40a + 1600b$. Dividing by $\mu$: $12 = a + 15b$ and $8 = a + 40b$, so $b = -4/25 = -0.16$ and $a = 14.4$. The third point checks: $14.4 - 0.16\cdot60 = 4.8 = 288/60$ (with real data a least-squares fit through all points would be used). Thus $q' \approx 14\,\mathrm{pA}$ and $N = 1/0.16 \approx 6$; the maximum response $Nq' \approx 90\,\mathrm{pA}$, so $p \approx 15/90 = 0.17$, $40/90 = 0.44$ and $60/90 = 0.67$.

3. Using Eq. (9.4), estimate how far from a single open channel the local $[\ce{Ca^2+}]$ falls below $10\,\mu\mathrm{M}$ without exogenous buffer, and explain why $10\,\mathrm{mM}$ EGTA hardly affects release at a basket-cell synapse but strongly reduces it at an immature calyx of Held.

   **Answer** Without buffer $c(r) \approx i_{\mathrm{Ca}}/(4\pi zFDr)$. With $i_{\mathrm{Ca}} = 0.3\,\mathrm{pA}$: $4\pi\cdot 2\cdot 96485\,\mathrm{C\,mol^{-1}}\cdot 2.2\times10^{-10}\,\mathrm{m^2\,s^{-1}} = 5.3\times10^{-4}\,\mathrm{C\,m^2\,s^{-1}\,mol^{-1}}$, so $c(r) = 0.3\times10^{-12}/(5.3\times10^{-4}\,r)\,\mathrm{mol\,m^{-3}}$, and $c = 10\,\mu\mathrm{M} = 10^{-2}\,\mathrm{mol\,m^{-3}}$ at $r \approx 57\,\mathrm{nm}$. EGTA binds $\ce{Ca^2+}$ slowly ($\lambda_{\mathrm{B}} \approx 50\,\mathrm{nm}$ at $10\,\mathrm{mM}$): within $20\,\mathrm{nm}$ of the channel most ions reach the sensor before EGTA captures them ($\mathrm{e}^{-20/50} = 0.67$), and because release depends on about the fourth power of $c$ the reduction is modest. At $100$–$200\,\mathrm{nm}$ the factor is $\mathrm{e}^{-2}$ to $\mathrm{e}^{-4}$ on $c$, hence $10^{-3}$ or less on release. Basket-cell terminals couple channels and sensors within about $20\,\mathrm{nm}$ (nanodomain), the immature calyx at $100\,\mathrm{nm}$ or more (microdomain).

4. A drug reduces the mean EPSC by 50% and raises the paired-pulse ratio from 1.1 to 1.6, without changing the amplitude of spontaneous miniature EPSCs. Where does it act? Give an example of such a drug action.

   **Answer** Unchanged miniature amplitude means $q$ is unchanged (postsynaptic receptors are not affected); a lower mean with a higher PPR is the signature of a lower release probability (Eq. (9.5) and the inverse relation between $p$ and PPR). The drug acts presynaptically, most likely by reducing $\ce{Ca^2+}$ entry, for example by activating presynaptic $\mathrm{GABA_B}$ receptors, adenosine $\mathrm{A_1}$ receptors or cannabinoid $\mathrm{CB_1}$ receptors, whose $\mathrm{G}\beta\gamma$ subunits inhibit $\mathrm{Ca_V2}$ channels (7.16.11); because release depends on about the fourth power of $\ce{Ca^2+}$ entry, a reduction of influx by about 16% is enough to halve release.
