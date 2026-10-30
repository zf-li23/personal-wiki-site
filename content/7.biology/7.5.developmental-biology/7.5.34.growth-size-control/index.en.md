---
title: Growth and Size Control
description: "How organisms, organs and cells reach their size. Modes of growth (proliferation, hypertrophy, accretion) and the coupling of growth to division; cell size and organ size; a limit-cycle mitotic oscillator and Kauffman's heat-shock test in Physarum; the statistics of population growth from a synchronous start (fixed, inherited and independent cycle times, the renewal equation and its dominant real root, mother-daughter correlation, an exactly solvable mixed model); intrinsic and extrinsic control of organ size (Twitty's grafts, thymus and spleen, Hippo-YAP, Dpp, cell competition, compensation, a feedback model with a set point); body size (growth hormone and IGFs, insulin and TOR, nutrition and DOHaD); human growth curves and allometry; tumours and teratomas; a contrast with plants."
---

Most of an animal's growth happens after its body plan is laid down. The early embryo hardly grows at all: cleavage divides the egg without enlarging it ([7.5.5](/7.5.5)), and the organ rudiments of [7.5.18](/7.5.18)–[7.5.32](/7.5.32) are laid out at a scale of a millimeter or less. Growth then increases the mass of a human by a factor of about $10^4$ between the end of organogenesis and adulthood, and of a moth caterpillar by the same factor within a few weeks ([7.5.33](/7.5.33)). Different organs grow at different rates and stop at different sizes, yet the result is remarkably reproducible: our two arms differ in length by a few millimeters. This chapter asks how this is achieved, at three levels. At the level of cells, growth is coupled to division, and the **cell cycle** can be described as an oscillator whose properties have been tested by perturbation. At the level of populations of cells, the variability of cycle times erases the synchrony of a cohort of cells, at a rate that can be calculated. At the level of organs and organisms, size is set by a combination of intrinsic programs and systemic signals, nutrition and hormones. The control of the **cell cycle** itself, of cell size (sizers, timers and adders) and the **Hippo pathway** are described in [7.3.20](/7.3.20) and [7.3.22](/7.3.22); here we build on them.

## 34.1. How Animals Grow

**Definition 34.1.1 (Modes of Growth)** Tissues grow by three mechanisms: *proliferation*, an increase in cell number by division; *hypertrophy*, an increase in the size of cells without division (muscle fibers, adipocytes, **neurons**); and *accretion*, an increase in extracellular material (the matrix of bone and cartilage).

The ways in which cells divide are equally varied: cleavage (division without growth), fragmentation into many daughters (a malaria parasite in a red cell), nuclear division without **cytokinesis** in a syncytium (the early insect embryo, the plasmodium of the slime mold *Physarum*), budding of a small daughter (yeast), filamentous growth (fungal hyphae), and fission, the common mode of bacteria, animal and plant cells, in which a cell roughly doubles its mass and divides into two similar daughters.

Cell size varies enormously: a frog egg is $1\,\mathrm{mm}$ across, a small phytoplankton cell $1\,\mathrm{\mu m}$, a red blood cell less than $10\,\mathrm{\mu m}$, while the axon of a motor **neuron** can be a meter long. In most proliferating tissues, growth and division are coupled, so that cells keep their size from one generation to the next, by the mechanisms of **cell size homeostasis** ([7.3.22](/7.3.22)): small cells often grow at a constant rate through the cycle, so that their size correlates with cycle length, whereas larger cells have checkpoints that sense size. The two processes can also be uncoupled. Cells may grow without dividing (adipocytes, postmitotic neurons, Schwann cells forming a myelin sheath after injury) or divide without growing (the cleaving zygote).

Does organ size depend on cell size? In *Caenorhabditis elegans*, whose cell number is fixed, mutations that reduce cell size make smaller organs and worms. In most animals it does not: salamanders of different **ploidy** have cells of different sizes but organs of the same size, made of correspondingly different numbers of cells (Fankhauser 1945), and in a *Drosophila* wing disc made of larger cells, **apoptosis** reduces the number of cells so that the disc reaches its normal size. Organ size is controlled at the level of the tissue, not by counting cells. How the number of cells is apportioned between tissues is visible already in the fly embryo: the first 13 nuclear cycles are synchronous because maternal String (the **Cdc25** phosphatase that activates Cdk1) is uniform; when it runs out in cycle 14, zygotic *string* is transcribed in a mosaic of domains under the control of the segmentation genes, and only cells expressing it divide, so that different regions acquire different numbers of cells.

## 34.2. A Mitotic Oscillator

**Mitosis** starts when some biochemical state reaches a critical value. Older models regarded the **mitogen** as an inhibitor produced at division and diluted as the cell grows; newer ones regard the cycle as an autonomous biochemical oscillation.

**Definition 34.2.1 (Mitotic Oscillator)** A *mitotic oscillator* is a self-sustained biochemical oscillation, a stable **limit cycle** ([2.4.11](/2.4.11)) in the space of concentrations of cell-cycle regulators, whose passage through a threshold triggers **mitosis**.

Let $x$ and $y$ be deviations of two concentrations from their equilibrium, $y$ the activator of mitosis. A linear oscillator, $\dot x=-\omega y$, $\dot y=\omega x$, has neutral orbits, $(x,y)=r(\cos\varphi,\sin\varphi)$ with $\dot\varphi=\omega$, $\dot r=0$, and $\dot x=\alpha x-\omega y$, $\dot y=\omega x+\alpha y$ gives growing or shrinking ones, $\dot r=\alpha r$. Nothing changes if $\alpha$ and $\omega$ depend on $r$: the system $\dot x=\frac{v(r)}rx-w(r)y$, $\dot y=w(r)x+\frac{v(r)}ry$ is equivalent to $\dot r=v(r)$, $\dot\varphi=w(r)$.

**Formula 34.2.1 (A Limit-Cycle Oscillator)** With $v(r)$ positive for $r<1$ and negative for $r>1$, for instance $v(r)=a(1-r^2)$ (Goodwin's form, with $w(r)=\omega/(1+r)$) or $v(r)=ar(1-r^2)$, the circle $r=1$ is a stable limit cycle: orbits inside it spiral outward and orbits outside it spiral inward. Shifting the origin so that the true concentrations $X=1+x$, $Y=1+y$ are nonnegative on the cycle, mitosis occurs each time $Y$ rises through a threshold $Y_0<2$.

Is this biochemistry of any relevance? Kauffman and Wille (1975) tested it in the plasmodium of the acellular slime mold *Physarum polycephalum*, a syncytium of millions of nuclei in a common cytoplasm, which divide in perfect synchrony: the whole plasmodium is one spatially homogeneous oscillator. A heat shock shortly before mitosis degrades the enzymes that make $X$ and $Y$ and so moves the state toward the equilibrium point $(1,1)$, the center of the cycle. The model then predicts a characteristic sequence of responses as the shock is made stronger.

**Proposition 34.2.1 (Resetting by Shocks)** Let a shock at a fixed phase before mitosis contract the state toward the center, $r\to(1-s)r$, with $s>1$ carrying it through the center to the opposite side. For the oscillator of Formula 34.2.1 with a threshold $Y_0$ near the top of the cycle: (a) a weak shock delays the next mitosis by an amount that increases with $s$ (the state is on a smaller orbit and needs more time to reach the threshold); (b) beyond a critical strength the orbit passes below the threshold on its first turn and a whole mitosis is skipped, a delay of one period; (c) for $s>1$ the phase is reversed, and as $s$ increases further the delay decreases toward half a period. The transition from (b) to (c) is discontinuous: the phase of the oscillator after a shock of strength $s=1$, which places the state on the singular point, is undefined.

The prediction of a large delay jumping to a smaller one as the shock crosses the center was confirmed: the observations were, in Percus and Childress's words, "totally in accord" with it. The shocks of increasing strength move the system from weak (type 1) to strong (type 0) phase resetting in Winfree's terminology. Today the embryonic cell cycle is indeed understood as a relaxation oscillator based on the positive and negative feedback loops of Cdk1, **Cdc25**, **Wee1** and the **anaphase-promoting complex** ([7.3.20](/7.3.20)), which runs autonomously in *Xenopus* egg extracts, whereas somatic cycles behave less like a free-running oscillator and more like a sequence of checkpoints gated by size and by signals.

![A limit-cycle mitotic oscillator and phase resetting by heat shock (Formula 34.2.1 with v = a r (1 − r²), a = 4, period 1; mitosis when y rises through 0.85; the shock is given about a quarter period before mitosis, at the black square). A: trajectories after shocks of increasing strength (1-4): weak shocks give small delays; a stronger shock leaves the orbit below the threshold for one turn, so a mitosis is skipped; a shock through the centre reverses the phase. B: delay of the next mitosis against shock strength: a gradual increase, a jump to one period, and beyond the centre a fall toward half a period](./plots/mitotic-oscillator.py)

## 34.3. The Statistics of Population Growth

The durations of the phases of the cell cycle fluctuate, even if their means are genetically fixed. What does this imply for the growth of a population of cells that starts synchronized, as after a synchronous division, and how quickly is synchrony lost? We count cells relative to their number at $t=0$, $N(0)=1$, in a homogeneous, nondifferentiating population, the situation of the few bacterial and protozoan experiments available; the branching processes of **stem cells** are treated in [7.5.36](/7.5.36).

### 34.3.1. Fixed and Inherited Cycle Times

If every cycle lasts exactly $\gamma$, $N(t)=2^{\lfloor t/\gamma\rfloor}$, and $\ln N$ grows as a staircase. Suppose instead that cycle times are distributed with density $P(\gamma)$, $P=0$ for $\gamma<\gamma_0$, but that each daughter inherits the exact cycle time of her mother. Each lineage then grows with its own staircase, and

$$
N(t)=\int_0^\infty P(\gamma)\,2^{\lfloor t/\gamma\rfloor}\,\mathrm{d}\gamma=\sum_{\mu=0}^\infty2^\mu\int_{t/(\mu+1)}^{t/\mu}P(\gamma)\,\mathrm{d}\gamma .
\tag{34.1}
$$
The steps are increasingly smeared, and $\ln N(t)\sim(t/\gamma_0)\ln2$: the fastest lineages dominate. Synchrony is never entirely lost. Substituting $\lambda=1/\gamma$ and expanding near the upper limit,

$$
N(t)=\int_0^{1/\gamma_0}\frac1{\lambda^2}P\Big(\frac1\lambda\Big)2^{\lfloor\lambda t\rfloor}\,\mathrm{d}\lambda\approx\frac{\gamma_0^2P(\gamma_0)}t\Big(1+\Big\{\frac t{\gamma_0}\Big\}\Big)2^{\lfloor t/\gamma_0\rfloor}+\cdots,
$$
with $\{x\}=x-\lfloor x\rfloor$ the fractional part (exactly so if $P(\gamma)\propto\gamma^{-2}$ above $\gamma_0$): the growth keeps a sawtooth modulation of period $\gamma_0$.

The residual synchrony is due to the sharp synchronization at $t=0$. Suppose instead that the culture starts from a steady state, maintained by cell death at rate $\lambda$, with all cycles equal to $\gamma$. With $0<\theta<1$ the position in the cycle, the population density $N(\theta,t)$ obeys the conservation law with amplification at division,

$$
\frac{\partial N}{\partial t}+\frac1\gamma\frac{\partial N}{\partial\theta}=-\lambda N,\qquad N(0,t)=2N(1^-,t).
$$

**Proposition 34.3.1 (Steady Age Distribution)** A time-independent solution exists when $\lambda=\ln2/\gamma$; it is

$$
N(\theta)=2^{1-\theta}\ln2\qquad\Big(\int_0^1N\,\mathrm{d}\theta=1\Big),
\tag{34.2}
$$
with twice as many cells at the start of the cycle as at its end. If death is switched off at $t=0$, $N(\theta,t)=2^{1-\theta+t/\gamma}\ln2$ and $N(t)=2^{t/\gamma}$; with a distribution of inherited cycle times, $N(t)=\int P(\gamma)2^{t/\gamma}\mathrm{d}\gamma\approx\frac{\gamma_0^2P(\gamma_0)}t\,\frac{2^{t/\gamma_0}-1}{\ln2}$, with no oscillation at all.

**Proof** At steady state $N'(\theta)=-\lambda\gamma N$, so $N=C\mathrm{e}^{-\lambda\gamma\theta}$, and the division condition $C=2C\mathrm{e}^{-\lambda\gamma}$ requires $\lambda\gamma=\ln2$. Normalization: $\int_0^12^{-\theta}\mathrm{d}\theta=1/(2\ln2)$, so $C=2\ln2$. Without death, the characteristics $\theta-t/\gamma=\text{const}$ carry the profile, and each passage through division doubles it. $\square$

(Percus and Childress write $N(\theta)=2^{-\theta}\ln2$, which integrates to $\frac12$; the normalized profile is twice that.)

### 34.3.2. Independent Cycle Times: the Renewal Equation

Now take the opposite extreme of no inheritance: whatever the mother's cycle, each daughter has a cycle time drawn from the density $g(\gamma)$, $g=0$ for $\gamma\le\gamma_0$, independently. The density of divisions per unit time, $N_M(t)$, is a sum over division histories: a cell that has divided $j$ times, at times $t_1<\dots<t_j$, contributes with probability density $g(t-t_j)g(t_j-t_{j-1})\cdots g(t_1)$, and with multiplicity $2^j$,

$$
N_M(t)=\sum_{j=0}^\infty2^j\int\!\!\cdots\!\!\int g(t-t_j)\cdots g(t_1)\,\mathrm{d}t_1\cdots\mathrm{d}t_j .
$$

**Theorem 34.3.1 (Asymptotic Exponential Growth)** With the **Laplace transform** $\tilde g(p)=\int_0^\infty\mathrm{e}^{-pt}g(t)\,\mathrm{d}t$ ([2.5.6](/2.5.6)),

$$
\tilde N_M(p)=\sum_{j\ge0}2^j\tilde g(p)^{j+1}=\frac{\tilde g(p)}{1-2\tilde g(p)} .
\tag{34.3}
$$
The asymptotic growth is governed by the root of $2\tilde g(p)=1$ with the largest real part. This root, $p_0$, is real and lies between $0$ and $\ln2/\gamma_0$; all other roots have smaller real parts. Hence $N(t)\sim C\mathrm{e}^{p_0t}$, and no vestige of the initial synchrony remains asymptotically.

**Proof** The multiple integral is a $j$-fold convolution, whose transform is $\tilde g^{j+1}$, and the geometric series sums to (34.3). For real $p$, $\tilde g(p)$ decreases from $1$ at $p=0$ to $0$, so $2\tilde g(p)=1$ has exactly one real root $p_0>0$; since $g=0$ below $\gamma_0$, $\tilde g(\ln2/\gamma_0)=\int_{\gamma_0}^\infty\mathrm{e}^{-\gamma\ln2/\gamma_0}g\,\mathrm{d}\gamma<\frac12$, so $p_0<\ln2/\gamma_0$. If $p$ is a complex root with $\operatorname{Re}p\ge p_0$, then $\frac12=\operatorname{Re}\tilde g(p)=\int g(\gamma)\mathrm{e}^{-\gamma\operatorname{Re}p}\cos(\gamma\operatorname{Im}p)\,\mathrm{d}\gamma<\int g(\gamma)\mathrm{e}^{-\gamma p_0}\mathrm{d}\gamma=\frac12$ unless $\operatorname{Im}p=0$, a contradiction. $\square$

**Definition 34.3.1 (Renewal Equation)** The *renewal equation* of a population is the integral equation $B(t)=B_0(t)+\int_0^tK(t-s)B(s)\,\mathrm{d}s$ for the rate of births (here divisions) $B$, with kernel $K$ (here $2g$); its asymptotic growth rate $p_0$ is the real root of the *Euler–Lotka equation* $\int_0^\infty\mathrm{e}^{-pt}K(t)\,\mathrm{d}t=1$.

The renewal equation is the same equation that governs the growth of an age-structured population of organisms, with $K$ the age-specific fecundity times survival ([7.19](/7.19)); Theorem 34.3.1 is the cell-biological version of the result that a population with a nonlattice distribution of ages at reproduction approaches a stable age distribution and exponential growth.

### 34.3.3. Mother–Daughter Correlations

Measurements of synchrony decay in the ciliate *Tetrahymena* fit neither extreme: they require that the cycle times of the two daughters depend on the cycle time $\gamma$ of their mother, $g(\gamma',\gamma''\mid\gamma)$. To include a steady state, allow also a probability $h(\gamma'\mid\gamma)$ that a cell destined to divide after $\gamma$ dies after $\gamma'$. Percus and Childress represent the branching process by a generating functional: each dividing cell of the $\mu$th generation, with cycle $\gamma$ dividing at $t$, is tagged with a weight $f(\gamma,t)$, each dying cell with $\bar f(\gamma,t)$, and the transition to the next generation replaces

$$
T_g:\ f(\gamma,t)\mapsto\iint g(\gamma',\gamma''\mid\gamma)f(\gamma',t+\gamma')f(\gamma'',t+\gamma'')\,\mathrm{d}\gamma'\mathrm{d}\gamma'',\qquad T_h:\ f(\gamma,t)\mapsto\Big(1-\int h\Big)f(\gamma,t)+\int h(\gamma'\mid\gamma)\bar f(\gamma',t-\gamma+\gamma')\,\mathrm{d}\gamma'
$$
(with $T_g\bar f=1$, $T_h\bar f=\bar f$). The generating functional $W=\sum_\mu W_\mu$ then satisfies $W=W_0+T_hT_gW$, and functional differentiation with respect to the tags gives the mean numbers of cells. Writing $h(\gamma)=\int h(\gamma'\mid\gamma)\mathrm{d}\gamma'$ for the total death probability and $g(\gamma\mid\gamma')=\int g(\gamma,\gamma''\mid\gamma')\mathrm{d}\gamma''$ for the cycle distribution of one daughter, the mean density $E(\gamma,t)$ of divisions of cells with cycle $\gamma$ at $t$ and the number $N(\gamma,t)$ of such cells present obey

$$
E(\gamma,t)=(1-h(\gamma))P(\gamma,t)+2(1-h(\gamma))\int g(\gamma\mid\gamma')E(\gamma',t-\gamma)\,\mathrm{d}\gamma',\qquad N(\gamma,t)=\int_t^{t+\gamma}E(\gamma,t')\,\mathrm{d}t' .
\tag{34.4}
$$
These cannot be solved in closed form, but their Laplace transforms $\Gamma(\gamma,p)=\int\mathrm{e}^{-pt}E\,\mathrm{d}t$ satisfy

$$
\Gamma(\gamma,p)=(1-h(\gamma))\tilde P(\gamma,p)+2(1-h(\gamma))\mathrm{e}^{-\gamma p}\int_0^\infty g(\gamma\mid\gamma')\Gamma(\gamma',p)\,\mathrm{d}\gamma',\qquad\tilde N(\gamma,p)=\frac{\mathrm{e}^{\gamma p}-1}p\Gamma(\gamma,p).
$$
All observables grow as $\mathrm{e}^{pt}$ with $p$ the pole of $\Gamma$ with largest real part, which occurs when the homogeneous equation has a solution. A steady state ($p=0$) requires the kernel $\delta(\gamma-\gamma')-2(1-h(\gamma))g(\gamma\mid\gamma')$ to be singular: an eigenvalue problem for the strength of the death rate, which contrasts with the realistic case of a death rate that depends on population size. Without death, direct inheritance $g(\gamma\mid\gamma')=\delta(\gamma-\gamma')$ gives the poles $p=(\ln2+2\pi\mathrm{i}n)/\gamma_0$, the persistent oscillation of Section 34.3.1, and no inheritance gives back Theorem 34.3.1.

**Proposition 34.3.2 (A Solvable Mixed Model)** Let $g(\gamma\mid\gamma')=\beta\delta(\gamma-\gamma')+(1-\beta)g(\gamma)$ for $\gamma,\gamma'\ge\gamma_0$, no death, and a synchronous start $P(\gamma,t)=g(\gamma)\delta(t-\gamma)$. Then

$$
\Gamma(\gamma,p)=\frac{g(\gamma)/(\mathrm{e}^{\gamma p}-2\beta)}{1-2(1-\beta)\int_{\gamma_0}^\infty\frac{g(\gamma')}{\mathrm{e}^{\gamma'p}-2\beta}\,\mathrm{d}\gamma'} .
\tag{34.5}
$$
For $\beta>\frac12$ the synchronized poles $p=(\ln2\beta+2\pi\mathrm{i}n)/\gamma_0$ of the numerator survive, but there is always a real pole with a larger real part, where the denominator vanishes. Synchrony is therefore lost asymptotically for every $\beta<1$.

**Proof** Substituting into the transformed equation, $\Gamma=2\mathrm{e}^{-\gamma p}\big[\beta\Gamma+(1-\beta)g(\gamma)I\big]+g(\gamma)\mathrm{e}^{-\gamma p}$ with $I=\int\Gamma\,\mathrm{d}\gamma'$, so $\Gamma=\frac{g(\gamma)\mathrm{e}^{-\gamma p}}{1-2\beta\mathrm{e}^{-\gamma p}}(1+2(1-\beta)I)$. Integrating over $\gamma$ determines $I$, and substitution gives (34.5). As $p$ decreases from $\infty$ to $(\ln2\beta)/\gamma_0$, the integral in the denominator increases from $0$ to $\infty$ (the integrand diverges at $\gamma=\gamma_0$), so $2(1-\beta)\int\cdots=1$ at some real $p$ in between, larger than the real part of the synchronized poles. $\square$

The resulting $N(t)$ fits experimental data easily, and the same method solves $g(\gamma\mid\gamma')=\beta\delta(\gamma-\gamma')+(1-\beta)g(\gamma-c\gamma')$. The real problem, the distribution of population size at a given time, rather than its mean, remains analytically intractable.

![Loss of synchrony after a synchronous division (Monte Carlo, 4000 cells; gamma-distributed cycle times with mean 1, coefficient of variation 0.15 and minimum 0.6). A: log₂ of the population for a fixed cycle (staircase), fully inherited cycle times, a mixed rule (daughters keep the mother's cycle with probability 0.7) and independent cycle times. B: deviations from the long-time trend: the staircase persists; inherited cycles dephase quickly, leaving only a small residual oscillation at the period of the fastest lineages (Section 34.3.1); with independent cycles the oscillation decays at the rate set by the complex roots of 2g̃(p) = 1 (Theorem 34.3.1)](./plots/population-sync.py)

## 34.4. Organ Size: Intrinsic and Extrinsic Control

**Definition 34.4.1 (Organ Size Control)** *Organ size control* is the set of mechanisms that make an organ stop growing at a characteristic size, by adjusting cell proliferation, cell growth and cell death to information about the organ's own size (intrinsic control) or about the body and its environment (extrinsic control).

### 34.4.1. Grafts and Rudiments

The classical experiments separate the two. Twitty and Schwind (1931) exchanged limb buds between embryos of a small salamander, *Ambystoma punctatum*, and a large one, *A. tigrinum*. A limb bud of the large species grafted onto the small one grew more slowly at first, while the host's feeding was limited, but eventually formed a limb of the large species' size on the small animal, and the reverse graft a small limb on the large one: limb size is intrinsic to the bud. Eyes exchanged between the same species reached intermediate sizes, so eye size depends partly on the host. In mice, several fetal thymus rudiments grafted into one animal each grow to the size of a normal thymus, whereas several fetal spleens together reach only the mass of one spleen (Metcalf 1963–64): the thymus follows an intrinsic program, the spleen is regulated by a systemic signal. The mammalian liver is the extreme of extrinsic control: after removal of two thirds, the remaining lobes grow until the original mass is restored, and a liver transplanted from a large dog into a small one shrinks ([7.5.35](/7.5.35)).

![Modes of growth and the control of organ size (schematic). A: proliferation, hypertrophy and accretion. B: Twitty and Schwind's exchange of limb buds between a small and a large *Ambystoma* species: the grafted limb grows to the size typical of the donor species. C: several fetal thymus rudiments grafted into one mouse each grow to full size; several spleen rudiments together reach the mass of one spleen](./plots/intrinsic-extrinsic.py)

### 34.4.2. Molecular Pathways

The intrinsic size of *Drosophila* **imaginal discs** ([7.5.33](/7.5.33)) has been studied most. Discs transplanted into the abdomen of adult flies grow until they reach their normal size and stop, even in a host with no other discs; a disc of the right size is therefore defined within the disc. The **Hippo pathway** ([7.3.22](/7.3.22)) is the central regulator: mutations in its kinases Hippo and Warts, or overexpression of the transcriptional **coactivator** Yorkie, cause massive overgrowth of the discs, and in mice activation of **YAP**, the Yorkie homologue, in the liver increases its mass about fourfold, reversibly. Hippo signaling responds to cell density and mechanical tension, to the atypical **cadherins** Fat and Dachsous, whose graded expression across the disc may itself encode size, and to **cell polarity**. Dpp signaling is also required: cells lacking Dpp signaling grow poorly, and the Dpp gradient scales with the growing disc ([7.5.11](/7.5.11)). A quantitative study of the wing disc (Wartlick et al. 2011) found that cells divide each time the Dpp signaling level they experience has increased by about 50 %, a rule that produces uniform growth throughout the disc as the scaled gradient rises with time, and stops when the increase can no longer occur. Mechanical feedback models (Shraiman 2005) propose instead that cells near the source, stretched by growth, divide faster and those far from it, compressed, slower, so that tension would equalize growth and stop it.

When part of a disc grows faster, the rest compensates. Fast-growing *Minute*$^+$ clones in a *Minute*/$+$ wing ([7.5.33](/7.5.33#sec-33.6.1)) fill much of a compartment, yet the wing has its normal size: the slow-growing cells are eliminated by **apoptosis**. Wild-type cells next to cells with more Myc likewise lose ("losers") to them ("winners"). This phenomenon, cell competition, makes the final size independent of the growth rate of any one population of cells, and it is likely to be important in the early mammalian embryo and in the expansion of premalignant clones in adult tissues. Damaged discs, finally, communicate with the rest of the body: they secrete Dilp8, which acts on brain neurons and delays the production of **ecdysone**, so that pupation waits until the discs have regenerated, and growth of all discs remains coordinated.

### 34.4.3. A Feedback Model

The classical idea of extrinsic control is a "chalone", a tissue-specific inhibitor of proliferation made by an organ in proportion to its mass. The hepatocyte **growth factor** and the **bile acids**, and for muscle the secreted inhibitor myostatin (GDF8, whose loss doubles muscle mass in cattle, mice and humans), are present-day candidates. The logic is that of integral feedback.

**Proposition 34.4.1 (Set Point by Feedback)** Let an organ of mass $M$ secrete an inhibitor into a well-mixed circulation, $\dot I=pM-kI$, and grow as $\dot M=gM(1-I/I^*)$. The positive steady state $M^*=kI^*/p$, $I=I^*$, is stable for all $g,k>0$; after removal of part of the organ, or grafting of an extra one, the total mass returns to $M^*$.

**Proof** At steady state with $M>0$, $I=I^*$ and $M=kI/p=kI^*/p$. The Jacobian at this point is $\begin{bmatrix}0&-gM^*/I^*\\p&-k\end{bmatrix}$, with trace $-k<0$ and determinant $gpM^*/I^*>0$: both eigenvalues have negative real parts. Since $I$ depends on the total mass, the argument is the same for several organs secreting the same inhibitor. $\square$

The model distinguishes organs like the spleen and liver, which regulate their total mass, from organs like the thymus, whose size is set by an intrinsic program and not by feedback. Note that the set point depends on the ratio of the clearance rate $k$ to the secretion rate $p$, so that body size and the clearance of the inhibitor (by the kidney, for instance) also determine organ size.

![Organ size by feedback versus an intrinsic program (Proposition 34.4.1 with g = 0.3, p = k = 0.5, set point 1; the intrinsic organ grows at the same rate until an internal clock stops it). A: removal of two thirds of the organ at t = 20: the feedback organ regrows to its set point, with a small overshoot; the intrinsically controlled organ does not regenerate. B: grafting an extra half organ: with feedback the total mass returns to the set point, as for several spleens in one mouse; without, the total stays larger, as for several thymus glands](./plots/organ-size-feedback.py)

## 34.5. Body Size: Hormones and Nutrition

In mammals, growth after birth is driven by growth hormone (GH) from the pituitary, which induces insulin-like **growth factor** 1 (IGF-1), mainly in the liver; IGF-1 stimulates the proliferation of **chondrocytes** in the **growth plates** and of many other cells, and GH also acts directly ([7.5.24](/7.5.24) for the **growth plate**; [7.14](/7.14) for the endocrinology). Before birth, IGF-2 is the main growth factor: mice lacking *Igf2* are born at 60 % of normal weight, and since *Igf2* is a paternally expressed imprinted gene, its parent-of-origin expression ties fetal growth to the conflict between maternal and paternal genomes (**genomic imprinting**, [7.4.18](/7.4.18), [7.5.27](/7.5.27)). Variation in this axis explains size differences within species: small dog breeds share a **haplotype** of the *IGF1* gene associated with low serum IGF-1 (Sutter et al. 2007), and humans with mutations in the GH receptor (Laron syndrome) are very short, with low IGF-1. In *Drosophila*, insulin-like peptides from neurosecretory cells of the brain and nutrient sensing by TOR in the fat body play the corresponding roles; mutants of the insulin receptor substrate *chico* are flies of half normal size with normal proportions.

Nutrition modulates these pathways. Malnutrition during fetal life produces a smaller individual of normal proportions, and children who were small at birth have a higher risk later in life of cardiovascular disease and **type 2 diabetes**, whereas excessive birth weight carries a risk of obesity, hypertension and diabetes. This observation of Barker is the basis of the concept of the developmental origins of health and disease (DOHaD, [7.5.38](/7.5.38)). Postnatal malnutrition affects organs differently: in rats underfed after weaning, the skeleton grows normally but the liver and kidneys remain small. In insects, size is set by the critical weight and the duration of the terminal growth period ([7.5.33](/7.5.33#sec-33.3.3)).

## 34.6. Human Growth and Allometry

Human growth has three phases: rapid, decelerating growth in infancy (about $25\,\mathrm{cm}$ in the first year), slow, steady growth in childhood (about $5$–$6\,\mathrm{cm}$ per year), and the pubertal growth spurt, about two years earlier in girls than in boys, which ends with the fusion of the growth plates under the action of estrogen in both sexes. Final height is highly heritable, with a **heritability** of about 0.8 in well-nourished populations ([7.4.24](/7.4.24)), and is influenced by thousands of common variants; the secular increase of height over the last century reflects improved nutrition and health.

**Formula 34.6.1 (Preece–Baines Model)** Height from about two years of age to adulthood is well described by

$$
h(t)=h_1-\frac{2(h_1-h_\theta)}{\mathrm{e}^{s_0(t-\theta)}+\mathrm{e}^{s_1(t-\theta)}},
\tag{34.6}
$$
where $h_1$ is the adult height, $\theta$ a time near the peak of the adolescent spurt, $h_\theta$ the height at $\theta$, and $s_0<s_1$ rate constants of prepubertal and pubertal growth. The velocity $h'(t)$ has a minimum before the spurt (the prepubertal dip) and a maximum near $\theta$.

Different parts of the body grow at different rates. The head of a two-month fetus is half of its length, of a newborn a quarter, of an adult an eighth; the legs grow relatively fast in childhood, the trunk at puberty. Such relative growth is described by a power law.

**Definition 34.6.1 (Allometry)** **Allometry** is the change of the proportions of an organism with its size. Two measurements $x$ and $y$ follow the *allometric equation* $y=ax^b$, a straight line of slope $b$ in logarithmic coordinates; $b=1$ is isometry, $b>1$ positive and $b<1$ negative allometry.

In Huxley's classic example, the major claw of the male fiddler crab grows with $b\approx1.6$ relative to the rest of the body, so that it makes up a larger and larger fraction of a larger crab. Allometric exponents of organs during growth arise naturally if two parts grow exponentially at different specific rates $g_x$ and $g_y$: then $\ln y-\ln y_0=(g_y/g_x)(\ln x-\ln x_0)$, so $b=g_y/g_x$. Across species the same equation describes scaling laws, for example of metabolic rate with body mass ($b\approx\frac34$), which belong to physiology and evolution ([7.14](/7.14), [7.10](/7.10)).

![Human growth and allometry. A: height and height velocity of a boy from the Preece-Baines model (34.6) with typical parameters (adult height 176 cm, θ = 14.5 years): the velocity falls through childhood, dips before puberty and peaks at about 9.5 cm per year. B: head length against body length from the classical proportions (head one half of the body at 2 fetal months, one quarter at birth, one eighth in the adult): negative allometry with slope b ≈ 0.7, compared with isometry and with b = 1.5](./plots/growth-curves.py)

## 34.7. Growth out of Control: Tumors and Teratomas

Continuously dividing cells are the most likely to become malignant: about 85 % of human **cancers** arise in epithelia, which renew throughout life, and **leukemias** in the hematopoietic system. **Proto-oncogenes**, genes such as *RAS* and **receptor tyrosine kinase** genes that promote proliferation, become **oncogenes** by dominant gain-of-function mutations; **tumor suppressor genes**, such as *RB1* (whose loss causes retinoblastoma) and *PTCH1* (the Hedgehog receptor, whose loss causes basal cell **carcinoma** of the skin), act recessively at the cellular level ([7.3.26](/7.3.26), [7.4.21](/7.4.21)). Many of these genes are the developmental regulators of the preceding chapters (Hedgehog, Wnt, Notch, Hippo, the **Hox genes**), active again at the wrong time and place.

A few tumors involve few or no mutations. Teratomas and teratocarcinomas, which are common in the ovary and testis, arise from **germ cells**; in the mouse ovary, an unfertilized egg that is accidentally activated develops parthenogenetically to an epiblast-like stage and then grows into a disorganized tumor with tissues of all three **germ layers**. **Embryonic stem cells** injected into an adult mouse at any site form such tumors, which is why the formation of teratomas is the standard test of **pluripotency** ([7.5.36](/7.5.36)). Conversely, teratocarcinoma cells injected into a **blastocyst** can contribute normal tissues to a **chimera** (Mintz and Illmensee 1975): their malignancy is a property of the environment as much as of the cells, a reminder that **cancer** is also a disease of developmental control.

## 34.8. A Contrast: Plant Growth

Plants grow throughout life from meristems at the tips of shoots and roots, and their architecture is the product of this indeterminate growth. The apical bud suppresses the outgrowth of lateral buds (apical dominance) through the hormone auxin, transported down the stem, and strigolactones and cytokinins; removing the apex releases the lateral buds. Plant cells are enclosed in walls and do not migrate; the tissues grow mainly by the expansion of cells, driven by the turgor of the **vacuole** and controlled by the loosening of the wall, rather than by division, and the length and width of leaves are controlled by separate genes. These mechanisms are the subject of [7.12](/7.12) and [7.13](/7.13).

## Summary

- Growth (Definition 34.1.1) by proliferation, hypertrophy and accretion; growth and division usually coupled (**cell size homeostasis**, [7.3.22](/7.3.22)) but separable; organ size is controlled independently of cell size (salamander **ploidy**, fly discs), and cell numbers are apportioned by zygotic *string* in the fly embryo.
- Mitotic oscillator (Definition 34.2.1, Formula 34.2.1): $\dot r=v(r)$, $\dot\varphi=w(r)$ with a stable limit cycle; heat shocks in *Physarum* give delays that increase, jump by a period and fall toward half a period as the shock crosses the center (Proposition 34.2.1).
- Population statistics: fixed cycle $N=2^{\lfloor t/\gamma\rfloor}$; inherited cycles keep a residual synchrony at the fastest period; steady age distribution $2^{1-\theta}\ln2$ (Proposition 34.3.1); independent cycles lose synchrony, growth rate the real root of $2\tilde g(p)=1$ (Theorem 34.3.1, the Euler–Lotka equation of the renewal equation, Definition 34.3.1); generating functional with mother–daughter correlation and death, Eq. (34.4); the mixed model is solvable and loses synchrony for $\beta<1$ (Proposition 34.3.2).
- Organ size control (Definition 34.4.1): intrinsic (limbs, Twitty and Schwind; thymus) and extrinsic (spleen, liver); Hippo–Yorkie/**YAP**, Dpp and the 50 % rule, mechanical feedback, cell competition and compensation, Dilp8; a feedback model with a set point (Proposition 34.4.1).
- Body size: GH–IGF-1 after birth, IGF-2 before (imprinting), dog *IGF1*, Laron syndrome; insulin and TOR in flies; nutrition and DOHaD.
- Human growth: three phases, the Preece–Baines curve (Formula 34.6.1); allometry $y=ax^b$ (Definition 34.6.1), $b=g_y/g_x$ for exponential growth.
- Tumors: **proto-oncogenes** and tumor suppressors are developmental regulators; teratomas from **germ cells** and ES cells; teratocarcinoma cells normalized in **chimeras**.

## Questions

1. Salamanders of different **ploidy** have organs of the same size made of different numbers of cells. What does this exclude as a mechanism of organ size control, and what does it suggest?

   **Answer** It excludes control by counting a fixed number of cells or divisions (as in *C. elegans*), and control by a fixed program of cell divisions. It suggests that the organ senses a property of the tissue as a whole, its size, mass, the number of molecules of a secreted factor per unit volume, or mechanical stress, and adjusts the number of cells until the property reaches its set value.

2. In the oscillator of Formula 34.2.1, explain why a shock that places the state exactly on the equilibrium point gives an undefined phase, and why this implies that the delay must jump somewhere as the shock strength is increased.

   **Answer** At the center $r=0$ the angle $\varphi$ is undefined, and after an infinitesimal displacement the system leaves the center in a direction set by the displacement, so the eventual phase can be anything. As $s$ passes through 1 the state passes through the center, and the phase on the other side differs by about half a period; since the delay is continuous in $s$ elsewhere, it must jump at $s=1$ (or vary arbitrarily fast near it). This is the phase singularity of Winfree; the observation of a jump in *Physarum* was evidence that the mitotic cycle behaves as a limit-cycle oscillator rather than as an accumulation to a threshold that a shock can only reset to zero.

3. A population has cycle times uniformly distributed between $0.8$ and $1.2$ hours, independent between generations. Find the asymptotic growth rate $p_0$ and compare it with $\ln2/\bar\gamma$.

   **Answer** $\tilde g(p)=\frac{\mathrm{e}^{-0.8p}-\mathrm{e}^{-1.2p}}{0.4p}$. Solving $2\tilde g(p)=1$ numerically gives $p_0\approx0.696\,\mathrm{h^{-1}}$, slightly larger than $\ln2/1=0.693$: with variable cycle times, the population grows a little faster than one with the mean cycle, because short cycles contribute more descendants (by Jensen's inequality, $\mathbb{E}[\mathrm{e}^{-p\gamma}]\ge\mathrm{e}^{-p\bar\gamma}$). The difference is small for a narrow distribution and grows with its variance.

4. Show that the steady age distribution (34.2) implies that the fraction of cells in **mitosis**, if **mitosis** occupies the last fraction $\tau/\gamma$ of the cycle, is larger or smaller than $\tau/\gamma$. Why does this matter for estimating division rates from mitotic indices ([7.5.31](/7.5.31#sec-31.6))?

   **Answer** The fraction is $\int_{1-\tau/\gamma}^12^{1-\theta}\ln2\,\mathrm{d}\theta=2^{\tau/\gamma}-1$, which for small $\tau/\gamma$ is $\approx(\tau/\gamma)\ln2\approx0.69\,\tau/\gamma$: fewer cells are at the end of the cycle than at its beginning, because each division doubles the number of young cells. The mitotic index of an exponentially growing population therefore underestimates $\tau/\gamma$ by about 30 %, and the correction $\gamma=\tau\ln2/\ln(1+m)$ should be used.

5. In Proposition 34.3.2 with $\beta=0.9$, does synchrony persist? What experimental data would distinguish the mixed model from one with a continuous mother–daughter correlation?

   **Answer** No: for every $\beta<1$ there is a real pole with larger real part than the synchronized poles, so the oscillations decay relative to the exponential growth, but for $\beta$ close to 1 the two are close and synchrony decays slowly. To distinguish the models, measure in single-cell lineages (time-lapse) the joint distribution of mother and daughter cycle times: the mixed model predicts a mixture of exact equality and independence, a continuous correlation predicts a smooth joint distribution with correlation coefficient $\beta$ but no atom on the diagonal.

6. Using Proposition 34.4.1, predict what happens to liver size if the clearance of the inhibitor is halved (for example by kidney failure), and if a second, intrinsically controlled organ also secretes the same inhibitor.

   **Answer** $M^*=kI^*/p$: halving $k$ halves the set point, so the liver shrinks to half its mass. If another organ secretes the inhibitor at rate $p'M'$ with $M'$ fixed, the equilibrium requires $pM+p'M'=kI^*$, so $M^*=(kI^*-p'M')/p$: the regulated organ compensates for the other source by being smaller, and it disappears if $p'M'>kI^*$.

7. Design an experiment to determine whether the size of the *Drosophila* wing is controlled by a mechanism intrinsic to the disc or by the whole larva.

   **Answer** Transplant a young wing disc into the abdomen of an adult female, where it grows without metamorphosing, and measure its final size; if it stops at the normal size, the control is intrinsic (this is the classical result). Alternatively, make larvae in which one disc grows slower (for example by expressing a Minute mutation or a cell-cycle inhibitor in that disc only) and measure the other discs and the timing of pupariation: systemic coordination through Dilp8 delays pupariation and slows the other discs, so final proportions are kept.

8. Fit the allometric equation to two measurements of a child: head length $12.5\,\mathrm{cm}$ at a body length of $50\,\mathrm{cm}$, and $21.9\,\mathrm{cm}$ at $175\,\mathrm{cm}$. If the body grows by a factor of 3.5 between these points, by how much does the head grow? What does $b$ mean in terms of growth rates?

   **Answer** $b=\ln(21.9/12.5)/\ln(175/50)=0.561/1.253=0.45$. The head grows by $3.5^{0.45}=1.75$. If both grow exponentially, $b=g_{\mathrm{head}}/g_{\mathrm{body}}$: the head's specific growth rate after birth is less than half that of the body, because the brain, which determines the size of the skull, has done most of its growth before birth.

9. A mutation in *Igf2* is inherited from the father in one family and from the mother in another. Predict the phenotypes, and explain.

   **Answer** *Igf2* is imprinted: only the paternal allele is expressed. A loss-of-function allele inherited from the father reduces fetal growth (small offspring, about 60 % of normal weight in the mouse); inherited from the mother it has no effect, because the maternal allele is silent anyway. This **parent-of-origin effect** is the defining feature of an imprinted gene.

10. Why can a teratocarcinoma cell contribute normal tissue to a chimeric mouse, whereas a **carcinoma** cell with a mutant *RAS* gene cannot? What does this tell you about the nature of the two tumors?

    **Answer** A teratocarcinoma **stem cell** is a pluripotent cell, often genetically normal, whose growth is abnormal because it is in the wrong environment; in a **blastocyst** it receives the normal developmental signals and differentiates normally. A carcinoma cell has mutations that make its proliferation independent of signals (an oncogenic *RAS* constitutively activates the MAPK pathway), so no environment can restore its control. The first is an epigenetic disorder of developmental state, the second a genetic one.
