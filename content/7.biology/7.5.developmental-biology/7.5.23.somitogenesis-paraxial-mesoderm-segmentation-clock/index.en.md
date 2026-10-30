---
title: "Somitogenesis: Paraxial Mesoderm and the Segmentation Clock"
description: How the paraxial mesoderm is cut into somites. Paraxial and presomitic mesoderm, axis elongation from neuromesodermal progenitors; the segmentation clock as a delayed negative feedback oscillator (the Lewis model, square-wave limit and period estimate); the theory of oscillators (Lotka-Volterra, limit cycles, van der Pol and the method of averaging, harmonic balance); synchronization by Delta-Notch, entrainment of a forced oscillator and the Kuramoto model; the FGF/Wnt and retinoic acid wavefront, Fisher's equation and an FGF-RA model; the clock-and-wavefront model and somite size; boundary formation and a reaction-diffusion model of condensation; Hox identity; sclerotome, dermomyotome, myotome and syndetome; spondylocostal dysostosis.
---

The vertebrate body is segmented. Vertebrae, ribs, the segmental muscles of the back, the spinal nerves and the intersegmental blood vessels all repeat along the axis, and the repetition is laid down in the embryo by a single tissue, the paraxial mesoderm on either side of the **neural tube**, which is cut into blocks called somites. Somitogenesis is the best-understood example of how an embryo measures time and turns it into space. Each cell of the unsegmented **mesoderm** carries a molecular oscillator, the **segmentation clock** introduced in [7.3.24](/7.3.24#sec-24.5.2); a slowly moving front set by opposing gradients of FGF/Wnt and retinoic acid reads the phase of the clock, and one pair of somites forms per cycle. The chapter treats the biology and the mathematics together, because the problem has been shaped by models from the start: how a gene can oscillate (delayed negative feedback, limit cycles), how neighbouring oscillators synchronize, how a chemical front moves, and how a periodic boundary becomes sharp. It continues the **gastrulation** of [7.5.9](/7.5.9) and the posterior growth zone met in [7.5.18](/7.5.18#sec-18.4); segmentation of the fly ([7.5.15](/7.5.15)) uses an entirely different, simultaneous mechanism. The derivatives of the somites, muscle and the axial skeleton, are the subject of [7.5.24](/7.5.24).

## 23.1. Paraxial Mesoderm and Somites

### 23.1.1. The Subdivisions of the Trunk Mesoderm

After **gastrulation** the trunk **mesoderm** of an amniote lies as a sheet between **ectoderm** and **endoderm**, divided from the midline outward into four bands:

| Band | Position | Main derivatives |
|---|---|---|
| Chordamesoderm (axial **mesoderm**) | midline, beneath the **neural tube** | notochord; the nucleus pulposus of the intervertebral discs |
| Paraxial (somitic) mesoderm | either side of the neural tube | somites: vertebrae and ribs, skeletal muscle of trunk and limbs, dermis of the back, tendons, endothelium of the dorsal aorta; the unsegmented head mesoderm |
| Intermediate mesoderm | lateral to the somites | kidneys, gonads and their ducts, adrenal cortex ([7.5.25](/7.5.25), [7.5.26](/7.5.26)) |
| Lateral plate mesoderm | most lateral, split by the coelom | heart, blood vessels and blood, lining of the body cavities, limb skeleton ([7.5.28](/7.5.28)–[7.5.31](/7.5.31)) |

The mediolateral subdivision is specified by a gradient of BMP signalling, high laterally. Placing Noggin-secreting cells, which antagonize BMP, into the prospective lateral plate of a chick embryo respecifies it as paraxial mesoderm that forms extra somites (Tonegawa and Takahashi 1998). Different BMP levels select transcription factors of the Forkhead family: Foxc1 and Foxc2 in the paraxial mesoderm, Foxf1 in the lateral plate; mice lacking both *Foxc1* and *Foxc2* convert their paraxial mesoderm to intermediate mesoderm.

**Definition 23.1.1 (Paraxial and Presomitic Mesoderm)** The **paraxial mesoderm** is the band of mesoderm on either side of the neural tube and notochord. Its posterior, still unsegmented part is the **presomitic mesoderm** (PSM; in birds the segmental plate): a rod of mesenchymal cells, supplied with new cells from the tail bud at its posterior end and consumed by somite formation at its anterior end.

**Definition 23.1.2 (Somite)** A **somite** is a transient, roughly spherical block of paraxial mesoderm, an epithelial ball of cells around a small central cavity (the somitocoel) containing a few mesenchymal cells, formed in pairs on both sides of the axis in anterior-to-posterior order. The rounded condensations in the PSM that precede them are called somitomeres; in the head the somitomeres never form somites. Somites are numbered by their position relative to the one being formed: the somite that has just separated is SI, older ones SII, SIII and so on; the forming somite is S0 and the prospective somites in the PSM are S-I, S-II, ...

The PSM transcription factors Tbx6 and Mesogenin 1 (Msgn1) define the paraxial identity of the cells that leave the tail bud. Msgn1 is both necessary and sufficient for *Tbx6* expression. The importance of Tbx6 is shown by a striking phenotype: in *Tbx6*$^{-/-}$ mice the cells that should become PSM express the neural genes *Sox2* and *Pax6* and form two ectopic neural tubes flanking the normal one (Chapman and Papaioannou 1998; Takemoto et al. 2011). Tbx6 therefore not only promotes the mesodermal fate but represses the alternative neural fate of a bipotent precursor, the theme of the next section.

### 23.1.2. Numbers and Rhythm

Somites form at a regular, species-specific interval, and the number of somites is fixed for a species. Because development rates vary with temperature, the number of somites is the standard measure of the developmental stage of a vertebrate embryo.

| Species | Period of somite formation | Somite pairs |
|---|---|---|
| Zebrafish (*Danio rerio*, 28 °C) | about 20 min for the first six, then about 30 min | about 30–33 |
| *Xenopus laevis* | about 45 min | about 45 |
| Chick (*Gallus gallus*) | 90 min | about 50–52 |
| Mouse (*Mus musculus*) | about 2 h | about 65 (many in the tail) |
| Human | about 5 h (estimated from PSM cells in culture) | 42–44, of which the last few regress |
| Corn snake (*Pantherophis guttatus*) | about 1.5 h, relative to growth about four times faster than in the mouse | about 315 |

In the human embryo the first somites appear at about day 20 after **fertilization**; from them come 4 occipital, 8 cervical, 12 thoracic, 5 lumbar, 5 sacral and a variable number of coccygeal segments. The first occipital somites contribute to the base of the skull; the head anterior to them is built by unsegmented head mesoderm and the **neural crest** ([7.5.20](/7.5.20)).

The sequence of somite formation is laid down in the PSM before the somites appear. If the PSM is cut transversely, the pieces still segment on schedule; if a piece is rotated by 180° along the anterior-posterior axis, somites form in it in the reverse order, starting at its original anterior end. The PSM is therefore not instructed by a signal from the formed somites; its cells carry an autonomous, already patterned program (Wolpert's experiments in chick). Only the most posterior PSM, beyond a determination level, is still labile, as Section 23.6 shows.

![The presomitic mesoderm and the segmentation clock (dorsal view of the paraxial mesoderm of one side, anterior left). Each row shows the same embryo at a later phase of one clock cycle: formed somites (left), the presomitic mesoderm and the tail bud (right). The shading marks the expression of a cyclic gene such as *lunatic fringe* or *hairy1*. A broad stripe of expression starts in the tail bud and moves anteriorly, narrowing as it goes, because cells oscillate more slowly the further they are from the tail bud; when it reaches the anterior PSM it stops, a boundary forms (bottom row) and one more somite exists. The dashed line is the determination front, where FGF and Wnt signalling (orange bar, high in the tail bud) fall below a threshold and retinoic acid from the somites (green bar) rises. The front, the tail bud and the PSM move posteriorly together as the axis elongates; the cells do not move with the stripes](./plots/psm-cycle.py)

## 23.2. Axis Elongation and the Tail Bud

The anterior paraxial mesoderm is formed during **gastrulation** by **ingression** through the **primitive streak**. The posterior trunk and the tail, however, are built from a growth zone at the posterior end, the tail bud, which contains **neuromesodermal progenitors** (**NMPs**, Definition 18.4.2): bipotent cells that co-express Sox2 and Brachyury and give rise to both the posterior **neural tube** and the paraxial mesoderm. Two antagonistic signalling systems decide their fate.

- Wnt3a and FGF8 from the tail bud maintain the **progenitors** and push them towards **mesoderm**: they activate *Msgn1* and *Tbx6*, which repress *Sox2*.
- Retinoic acid (RA), made by the enzyme Raldh2 in the newly formed somites, represses *Fgf8* and promotes *Sox2* and neural differentiation; FGF in turn induces *Cyp26a1*, the enzyme that degrades RA. In *Raldh2*$^{-/-}$ mouse embryos *Fgf8* expression expands anteriorly.

As the axis elongates, cells leave the progenitor zone, enter the PSM and later find themselves in a somite; the PSM keeps a roughly constant length while it moves backwards, until late in somitogenesis, when it shrinks. How does elongation happen? In the zebrafish tail bud, time-lapse tracking of all nuclei (Lawton et al. 2013) shows NMPs moving collectively from a dorsal medial zone to the tip of the tail bud, slowing down and mixing there, and then turning anteriorly into maturation zones where they switch on *msgn1* and *tbx6* and divide once (driven by a transient pulse of Cdc25a) before joining the PSM. Two mechanical contributions add to this. Notochord cells inflate large **vacuoles** inside a stiff sheath of **collagen** and **laminin**, so that the notochord lengthens towards the tail like a hydrostatic rod, and the PSM, attached to it through **fibronectin** and integrin α5, is pulled along: knockdown of **integrins** α5 and αV makes the notochord buckle as it extends (Dray et al. 2013). In the chick, the PSM cells move randomly with a speed that is graded from high posteriorly to low anteriorly, under FGF control; random motility that is higher at the back expands the posterior tissue and drives elongation without any directed migration (Bénazéraf et al. 2010).

## 23.3. The Segmentation Clock

### 23.3.1. Cyclic Genes

The first evidence for an oscillator came from the chick gene *c-hairy1*, a homologue of the fly pair-rule gene *hairy* (Palmeirim et al. 1997). Its mRNA appeared in different patterns in different embryos of the same stage: broad in the posterior PSM in some, as a narrow anterior stripe in others. The decisive experiment separated time from space. An embryo was cut along the midline; one half was fixed at once and the other cultured for a defined time before fixation. Because both halves had the same pattern at the start, the comparison revealed how the pattern changed with time: a wave of expression started in the posterior PSM, swept anteriorly while narrowing, and arrived at the anterior PSM after 90 minutes, the time taken to form one somite; the next wave started in the tail bud as the previous one finished. The wave is not carried by moving cells: marked cells stay in place while turning the gene on and off.

Many genes oscillate in the PSM, nearly all belonging to three pathways:

| Pathway | Cyclic genes (examples) | Phase |
|---|---|---|
| **Notch signaling pathway** | *Hes7* (mouse), *her1* and *her7* (zebrafish), *hairy1*, *Lunatic fringe* (*Lfng*), *Nrarp*, *Dll1* (oscillating protein) | together |
| **Wnt signaling pathway** | *Axin2*, *Dact1*, *Nkd1* | opposite to Notch targets |
| FGF pathway | *Sprouty2*, *Dusp6*, phosphorylated ERK | with Notch targets |

The core of the oscillator is negative autoregulation of a Hes/Her transcriptional **repressor**. Hes7 represses its own gene; its mRNA and protein are short-lived (half-lives of about 20 min in mouse PSM); in *Hes7*$^{-/-}$ mice oscillations stop and somites are irregular and fused, and stabilizing the protein by a few minutes abolishes oscillation (Hirata et al. 2004). Lunatic fringe, a glycosyltransferase that modifies Notch, oscillates under Hes7 control and periodically inhibits Notch signalling, adding a second loop. Loss of the Notch ligand Delta-like 3 (*Dll3*) disrupts the clock and causes vertebral malformations in mice and humans (23.11).

The period differs between species because the biochemical steps of the loop run at different speeds. When mouse and human **pluripotent** **stem cells** are differentiated into PSM-like cells in culture, both oscillate *HES7*, with periods of about 2–3 h (mouse) and about 5 h (human); the human cells degrade HES7 more slowly and take longer to transcribe, splice and export its mRNA, which accounts for the difference (Matsuda et al. 2020). Cultures of mouse or human PSM cells (and three-dimensional "somitoids") reproduce waves, a front and even boundaries in vitro, which shows that the system organizes itself without the rest of the embryo.

### 23.3.2. A Negative Feedback Loop Needs a Delay

Let $m$ be the amount of mRNA of an autorepressed gene (such as *her1*) in a cell and $p$ the amount of its protein. The protein is made from mRNA and degraded; the mRNA is made at a rate that falls with the protein, which acts as a dimer, and is degraded:

$$
\dot p = am - bp,\qquad \dot m = f(p) - cm,\qquad f(p) = \frac{k}{1 + (p/p_0)^2}.
\tag{23.1}
$$
At low $p$ the mRNA settles at $k/c$; at high $p$ it decays as $\mathrm{e}^{-ct}$. Setting $\tilde p = p/p_0$, $t' = ct$ and $\tilde m = cm/k$ leaves two parameters:

$$
\tilde m' = \frac{1}{1 + \tilde p^{2}} - \tilde m,\qquad \tilde p' = \alpha\tilde m - \beta\tilde p,\qquad \alpha = \frac{ak}{c^{2}p_0},\quad \beta = \frac{b}{c}.
$$

**Proposition 23.3.1** System (23.1) has no periodic solutions: every solution with $m, p \ge 0$ tends to its unique steady state.

**Proof** The steady state lies where the nullclines $\tilde m = 1/(1 + \tilde p^2)$ (decreasing) and $\tilde m = (\beta/\alpha)\tilde p$ (increasing) cross, which happens exactly once. The divergence of the vector field $(am - bp,\ f(p) - cm)$ is $-b - c < 0$ everywhere, so by Bendixson's criterion ([Theorem 11.6.2](/2.4.11#thm-11.6.2)) there is no closed trajectory. The quadrant is invariant and trajectories are bounded ($m \le \max(m(0), k/c)$, and then $p$ is bounded), so by the Poincaré–Bendixson theorem ([Theorem 11.6.1](/2.4.11#thm-11.6.1)) every trajectory tends to the equilibrium. $\square$

Geometrically, the flow on each nullcline points towards the steady state, and a two-variable negative feedback loop can produce only damped oscillations. What is missing is time. Making an mRNA takes a transcription delay $T_m$ (transcription, splicing and export; for *her1* about 12 min) and making a protein a translation delay $T_p$ (about 3 min), steps below the resolution of the model that act as pure delays (Lewis 2003).

**Formula 23.3.1 (Delayed Negative Feedback Oscillator)** With delays $T_m$ and $T_p$, the autorepressed gene obeys

$$
\dot p(t) = a\,m(t - T_p) - b\,p(t),\qquad \dot m(t) = f\bigl(p(t - T_m)\bigr) - c\,m(t).
\tag{23.2}
$$
For the zebrafish gene *her1*, Lewis estimated $a = 4.5\,\mathrm{min^{-1}}$, $b = c = 0.23\,\mathrm{min^{-1}}$ (half-lives of 3 min), $k = 33\,\mathrm{min^{-1}}$, $p_0 = 40$ molecules, $T_m = 12\,\mathrm{min}$, $T_p = 2.8\,\mathrm{min}$. The steady state loses stability in a **Hopf bifurcation** once the total delay is long enough, and the system settles on a **limit cycle**; this is the model of the Hes1 oscillator in [Eq. (24.4)](/7.3.24#eq-24.4) of cell biology, analysed here further.

### 23.3.3. The Square-Wave Limit

Even simpler is a gene product that controls its own source after a single delay $T$: $\dot x(t) = f(x(t - T)) - c\,x(t)$ with $f(x) = k/(1 + x^2)$. Take the extreme of fast turnover, $c \to \infty$ and $k \to \infty$ with $K = k/c$ fixed. Then

$$
\frac{1}{c}\,\dot x(t) = \frac{K}{1 + x(t - T)^{2}} - x(t)
\tag{23.3}
$$
becomes, in the limit, the difference equation $x(t) = K/\bigl(1 + x(t - T)^2\bigr)$: the value at time $t$ is a function of the value one delay earlier. The solution breaks into independent chains $x_0(t), x_0(t + T), x_0(t + 2T), \dots$; the simplest, starting from a constant, holds a value $x_0$ for a time $T$, jumps to $x_1$, holds it for $T$, and so on.

**Proposition 23.3.2 (Square-Wave Oscillation)** The difference equation $x_{n+1} = g(x_n) = K/(1 + x_n^2)$ has a unique fixed point $\bar x$, the root of $\bar x^3 + \bar x = K$. It has a cycle of period two, $x_0 \ne x_1$, if and only if $K > 2$, and then $x_1 = 1/x_0$ with $x_0 + 1/x_0 = K$. For $K < 2$ the fixed point is stable and oscillations die out; at $K = 2$ the fixed point loses stability as $g'(\bar x)$ passes through $-1$.

**Proof** A two-cycle requires $x_1 = K/(1 + x_0^2)$ and $x_0 = K/(1 + x_1^2)$. Eliminating $K$: $x_1(1 + x_0^2) = x_0(1 + x_1^2)$, that is $(x_1 - x_0)(1 - x_0x_1) = 0$, equivalently $x_1 + 1/x_1 = x_0 + 1/x_0$. The root $x_1 = x_0$ is the fixed point; the other is $x_1 = 1/x_0$, and then $K = x_0 + 1/x_0 \ge 2$, with equality only for $x_0 = x_1 = 1$. At the fixed point $g'(\bar x) = -2\bar xK/(1 + \bar x^2)^2 = -2\bar x^2/(1 + \bar x^2)$, using $K = \bar x(1 + \bar x^2)$; $\lvert g'\rvert < 1$ exactly when $\bar x < 1$, that is $K < 2$. $\square$

In the oscillating case the gene is either fully on or nearly off, and each state lasts one delay: a square wave of period $2T$. The steady state, in contrast, is the cube root solution $\bar x$. Finite but large $c$ is a singular perturbation: it raises the order of the equation and smooths the jumps. On the fast time scale $\tau = ct$, with $X(\tau) = x(\tau/c)$, the delayed term is constant during a transition, $X'(\tau) = K/(1 + x_0^2) - X(\tau)$, so that

$$
X(\tau) = x_0\,\mathrm{e}^{-\tau} + x_1(1 - \mathrm{e}^{-\tau}),
$$
an exponential switch of duration about $1/c$ between the two levels.

The two-delay system (23.2) reduces to this case. Define the advanced protein $p_a(t) = p(t + T_p)$; then $\dot m(t) = f\bigl(p_a(t - T_m - T_p)\bigr) - cm(t)$ and $\dot p_a(t) = am(t) - bp_a(t)$, so only the total delay $T = T_m + T_p$ matters. With $\tau = t/T$, $\beta = bT$, $\gamma = cT$, $\kappa = ak/(bcp_0)$, $\psi(\tau) = p_a(T\tau)/p_0$ and $\mu(\tau) = c\,m(T\tau)/k$,

$$
\mu'(\tau) = \frac{\gamma}{1 + \psi(\tau - 1)^{2}} - \gamma\mu(\tau),\qquad \psi'(\tau) = \kappa\beta\mu(\tau) - \beta\psi(\tau).
$$
Here $\kappa = p_{\max}/p_0$, the ratio of the protein level reached without repression, $ak/(bc)$, to the repression threshold. For short lifetimes ($\beta, \gamma \to \infty$), $\mu(\tau) = 1/(1 + \psi(\tau - 1)^2)$ and $\psi = \kappa\mu$, so $\psi(\tau) = \kappa/(1 + \psi(\tau - 1)^2)$: the single-delay system with $K = \kappa$, which oscillates if $\kappa > 2$. In general, eliminating $\mu$ gives the second-order equation

$$
\psi(\tau) + \Bigl(\frac{1}{\beta} + \frac{1}{\gamma}\Bigr)\psi'(\tau) + \frac{1}{\beta\gamma}\psi''(\tau) = \frac{\kappa}{1 + \psi(\tau - 1)^{2}},
\tag{23.4}
$$
which oscillates when $\beta$, $\gamma$ and $\kappa$ are large enough.

**Formula 23.3.2 (Period of the Delayed Feedback Oscillator)** For long-lived but not too long-lived components, the period of (23.2) is approximately

$$
P \approx 2\Bigl(T + \frac{1}{b} + \frac{1}{c}\Bigr),\qquad T = T_m + T_p,
$$
and depends only weakly on the rates $a$ and $k$ and on the threshold $p_0$.

**Proof** Call the left side of (23.4) $\Psi(\tau)$, a smoothed (low-pass filtered) version of $\psi$; $\Psi$ is maximal when $\psi(\tau - 1)$ is minimal. Let $\psi$ have a maximum at $\tau_0$ and the preceding minimum at $\tau_0 - 1 - u$, so that the half-period is $1 + u$; then $\Psi$ is maximal at $\tau_0 - u$, and

$$
0 = \Psi'(\tau_0 - u) = \psi'(\tau_0 - u) + \Bigl(\frac{1}{\beta} + \frac{1}{\gamma}\Bigr)\psi''(\tau_0 - u) + \dots = \Bigl(\frac{1}{\beta} + \frac{1}{\gamma} - u\Bigr)\psi''(\tau_0) + \dots,
$$
using $\psi'(\tau_0) = 0$ and expanding to first order in the small quantities $u$, $1/\beta$, $1/\gamma$. Hence $u = 1/\beta + 1/\gamma$, the half-period is $1 + 1/\beta + 1/\gamma$ in units of $T$, and the full period is $2(T + 1/b + 1/c)$. $\square$

The result is intuitive: in each half-cycle the signal must pass once through the delay and through the two lifetimes, which act as first-order lags. The period is robust to the levels of expression, which is what a clock needs.

**Example 23.3.1 (The *her1* Oscillator)** With Lewis's parameters, $T = 14.8\,\mathrm{min}$ and $1/b = 1/c = 4.35\,\mathrm{min}$, so Formula 23.3.2 gives $P \approx 2(14.8 + 8.7) = 47\,\mathrm{min}$; numerical integration of (23.2) gives 49 min, and the threshold ratio $\kappa = ak/(bcp_0) = 70$ is well above 2. Changing $k$ or $p_0$ by a factor of two changes the period by only a few percent, but changing the delay changes it in proportion. The model period is longer than the observed 30 min, which shows that the true delays and lifetimes in the zebrafish PSM are shorter than these early estimates; in the mouse, the measured lifetimes of Hes7 mRNA and protein (about 20 min each) and delays of about 30 min give periods close to the observed 2 h.

![The delayed negative feedback oscillator. (A) *her1* mRNA (orange) and protein (purple) in Eq. (23.2) with Lewis's parameters: sustained oscillations with a period of about 49 min, the protein lagging the mRNA. (B) Period as a function of the total delay $T = T_m + T_p$ (points, numerical), compared with the estimate $2(T + 1/b + 1/c)$ (solid line) and with $2T$ (dashed); below a total delay of about 5 min the oscillation dies out (Hopf bifurcation). (C) The single-delay equation (23.3) with fast turnover ($c = 20$, delay 1): for $K = 3$ the solution becomes a square wave alternating between $x_0 = 0.38$ and $x_1 = 1/x_0 = 2.62$ (dotted lines); for $K = 1.5$ the oscillation decays to the steady state $\bar x$ with $\bar x^3 + \bar x = K$](./plots/delay-oscillator.py)

## 23.4. Oscillators in General

The **segmentation clock** is one instance of a question older than molecular biology: what kind of dynamics produces a reliable oscillation? A single autonomous equation $\dot x = f(x)$ cannot oscillate, because a value $x_0$ would have to be passed both rising and falling, so $f$ could not be single-valued. Two first-order equations, or one of second order, are the minimum.

### 23.4.1. The Lotka–Volterra Model

**Definition 23.4.1 (Lotka–Volterra Model)** The **Lotka–Volterra model** of a prey population $H$ (hares, with plentiful food) and a predator population $L$ (lynx, eating only hares) is

$$
\dot H = aH - bLH,\qquad \dot L = cHL - dL,
\tag{23.5}
$$
with $a$ the growth rate of the prey, $b$ the rate of predation, $c$ the conversion of prey into predators and $d$ the death rate of predators.

A chemical version is obtained by rescaling $H = (b/c)K$, which gives $\dot K = aK - bLK$, $\dot L = bKL - dL$, the mass-action kinetics of the reactions

$$
A + K \xrightarrow{\ a\ } 2K,\qquad L + K \xrightarrow{\ b\ } 2L,\qquad L \xrightarrow{\ d\ } P,
$$
with a nondepleting food $A$ and an end product $P$, the dead predator. The steady states are $(0, 0)$ and $(H_0, L_0) = (d/c,\ a/b)$. Linearizing about the second,

$$
\begin{pmatrix}\delta\dot H\\ \delta\dot L\end{pmatrix} = \begin{pmatrix}0 & -bd/c\\ ac/b & 0\end{pmatrix}\begin{pmatrix}\delta H\\ \delta L\end{pmatrix},
$$
with eigenvalues $\lambda = \pm\mathrm{i}\sqrt{ad}$: neutral oscillations of frequency $\sqrt{ad}$ and arbitrary amplitude, $\delta H = \alpha\cos(\sqrt{ad}\,t) + \beta\sin(\sqrt{ad}\,t)$ and $\delta L = (c/b)\sqrt{a/d}\,\bigl(\alpha\sin(\sqrt{ad}\,t) - \beta\cos(\sqrt{ad}\,t)\bigr)$. At $(0, 0)$ the eigenvalues are $a$ and $-d$: a saddle.

The nested ellipses of the linear approximation become distorted far from the steady state but remain closed, because the system has a **first integral**. Seek $F(H, L) = g(H) + h(L)$ constant along solutions: $\dot H\,\partial_H F + \dot L\,\partial_L F = 0$ becomes $(a - bL)Hg'(H) + (cH - d)Lh'(L) = 0$, which separates with $g' = c - d/H$ and $h' = b - a/L$:

$$
F(H, L) = cH + bL - d\ln H - a\ln L = \text{const}
$$
([Example 14.1.2](/2.4.14#ex-14.1.2)). Every orbit is a level curve of $F$ around its minimum at $(H_0, L_0)$, hence closed. As a model of a biological clock the Lotka–Volterra system is defective. At fixed parameters it has a continuum of periodic orbits: the amplitude is set by the initial condition and any perturbation moves the system to another orbit, and the period depends on the amplitude and on the parameters. It is structurally unstable: an arbitrarily small change of the equations (for example, a little self-limitation of the prey) destroys the family of closed orbits.

### 23.4.2. Limit Cycles

What a clock needs is an isolated, attracting periodic orbit, a **limit cycle** (Definition 11.6.1 of [2.4.11](/2.4.11#def-11.6.1)). An artificial example is written in polar coordinates,

$$
\dot r = \frac{1 - r^{2}}{r},\qquad \dot\theta = \omega.
\tag{23.6}
$$
Then $\frac{\mathrm{d}}{\mathrm{d}t}r^2 = 2(1 - r^2)$, so $r = (1 - C\mathrm{e}^{-2t})^{1/2}$ and $\theta = \omega t + \theta_0$: every trajectory spirals in or out to the circle $r = 1$ and the frequency is exactly $\omega$, independent of the starting point. In Cartesian form, $\dot x = (1 - x^2 - y^2)x/(x^2 + y^2) - \omega y$ and $\dot y = (1 - x^2 - y^2)y/(x^2 + y^2) + \omega x$. The right dynamics is available, but ad hoc. A classical model with the same property is the van der Pol equation.

**Definition 23.4.2 (van der Pol Oscillator)** The **van der Pol oscillator** is the equation

$$
\ddot x - \varepsilon\,(1 - x^{2})\,\dot x + x = 0,\qquad \varepsilon > 0:
\tag{23.7}
$$
a linear oscillator with a nonlinear damping that is negative (pumping energy in) for $\lvert x\rvert < 1$ and positive for $\lvert x\rvert > 1$. It has a unique stable limit cycle ([Example 11.6.2](/2.4.11#ex-11.6.2)); for small $\varepsilon$ it is nearly sinusoidal, for large $\varepsilon$ a relaxation oscillation.

**Formula 23.4.1 (Method of Averaging)** For small $\varepsilon$, write $x = A(t)\cos\theta(t)$, $\dot x = -A(t)\sin\theta(t)$ (variation of constants), which requires $\dot A\cos\theta - A\dot\theta\sin\theta = -A\sin\theta$. Substituting into (23.7) and solving for $\dot A$ and $\dot\theta$:

$$
\dot A = \varepsilon A\sin^{2}\theta\,(1 - A^{2}\cos^{2}\theta),\qquad \dot\theta = 1 + \varepsilon\sin\theta\cos\theta\,(1 - A^{2}\cos^{2}\theta).
$$
Because $A$ and $\theta - t$ change slowly, the right sides can be averaged over a cycle of $\theta$ (the Krylov–Bogoliubov method). With $\langle\sin^2\theta\rangle = \frac12$, $\langle\sin^2\theta\cos^2\theta\rangle = \frac18$ and $\langle\sin\theta\cos\theta\rangle = \langle\sin\theta\cos^3\theta\rangle = 0$,

$$
\dot A = \frac{\varepsilon}{8}A(2 - A)(2 + A),\qquad \dot\theta = 1,
\tag{23.8}
$$
with solution $A(t) = 2\big/\bigl(1 + C\mathrm{e}^{-\varepsilon t}\bigr)^{1/2}$: the amplitude tends to the limit cycle $A = 2$ from any start, almost exactly the model (23.6).

The averaged equation is a first step; higher accuracy comes from expanding $A$ as a Fourier series in $\theta$ and matching coefficients. The same idea, harmonic balance, applies to the delayed oscillator.

**Example 23.4.1 (Harmonic Balance for the Delayed Oscillator)** Scale time so that the period of the fast-limit oscillator is $2\pi$, so that its delay is $\pi$: $x(t) = K/\bigl(1 + x(t - \pi)^2\bigr)$. Try $x = a + b\cos t$, so $x(t - \pi) = a - b\cos t$, and require the first two Fourier coefficients of both sides to agree (a Galerkin method):

$$
a = \frac{1}{2\pi}\int_0^{2\pi}\frac{K\,\mathrm{d}t}{1 + (a - b\cos t)^{2}},\qquad b = \frac{1}{\pi}\int_0^{2\pi}\frac{K\cos t\,\mathrm{d}t}{1 + (a - b\cos t)^{2}}.
$$
For small $b$ the second equation gives $b = 2aKb/(1 + a^2)^2$ and the first $a(1 + a^2) = K$, so a nonzero $b$ first appears when $2a^2/(1 + a^2) = 1$, at $a = 1$, $K = 2$: the threshold of Proposition 23.3.2. Evaluating the integrals (by residues, or numerically) gives the exact solution $a = \sqrt{K - 1}$, $b = \sqrt{2(K - 2)}$ for $K \ge 2$. At $K = 3$, $b = 1.41$; the exact square wave between $x_0 = 0.382$ and $x_1 = 2.618$ has half-amplitude $1.118$ and first Fourier harmonic $(4/\pi)(1.118) = 1.42$. The one-harmonic approximation recovers both the threshold and the amplitude of the oscillation.

At this level of description the delayed oscillator and the van der Pol oscillator behave alike, and models of the segmentation clock are often written with an effective local oscillator, with suitable parameters, when the question concerns populations of cells.

![Elementary oscillators. (A) Lotka–Volterra model (23.5) with $a = b = c = d = 1$: closed orbits, level curves of the first integral $cH + bL - d\ln H - a\ln L$, around the steady state $(1, 1)$; the amplitude is set by the initial condition. (B) The limit cycle model (23.6): trajectories from inside and outside converge on the circle $r = 1$. (C) The van der Pol oscillator with $\varepsilon = 0.1$ started at $x = 0.2$: the numerical solution (thin) and the amplitude predicted by the method of averaging, $A(t) = 2/(1 + C\mathrm{e}^{-\varepsilon t})^{1/2}$ (thick envelope); the amplitude grows to 2. (D) For $\varepsilon = 5$ the oscillation is a relaxation oscillation with slow phases and fast jumps, far from the averaging regime](./plots/elementary-oscillators.py)

## 23.5. Synchronization

### 23.5.1. Delta–Notch Couples the Clocks

A clock in each cell is not enough: neighbouring cells must keep the same phase, or the boundary will be ragged. In zebrafish the Notch ligand gene *deltaC* oscillates with *her1* and *her7*. Experiments that interfere with Notch signalling show that it is not needed for oscillation but for synchrony. In mutants of *deltaC* (*beamter*), *notch1a* (*deadly seven*) or *deltaD* (*after eight*), and in embryos treated with the γ-secretase inhibitor DAPT, the first somites form normally but posterior boundaries become irregular; *her1* expression, instead of stripes, becomes salt-and-pepper, as if each cell oscillated with its own phase (Jiang et al. 2000). Transplanted cells that start out of phase with their host gradually adopt the host's phase (Horikawa et al. 2006). And when DAPT is applied at different doses and times and then washed out, the position at which defects begin and the time needed to recover fit a model of coupled oscillators that drift apart when coupling is lost and resynchronize when it is restored (Riedel-Kruse et al. 2007). **Lateral inhibition**, the other use of Delta–Notch signalling ([7.3.24](/7.3.24)), would make neighbours different; here, because Delta expression oscillates with the clock, the same signal makes them alike.

### 23.5.2. Entrainment of a Forced Oscillator

To see how a signal from neighbours can impose its rhythm, consider a van der Pol oscillator driven by an external periodic source, a neighbour already oscillating at a somewhat different frequency $\omega$:

$$
\ddot x - \varepsilon(1 - x^{2})\dot x + x = K\sin\omega t .
\tag{23.9}
$$
For $\varepsilon = 0$ the periodic response is $x_0 = \gamma\sin\omega t$ with $\gamma = K/(1 - \omega^2)$. Write $x = y + \gamma\sin\omega t$:

$$
\ddot y - \varepsilon\bigl[1 - (y + \gamma\sin\omega t)^{2}\bigr](\dot y + \omega\gamma\cos\omega t) + y = 0 .
$$
If the frequencies of $y$ and of the drive are incommensurate, average over a cycle of $\omega t$: $\langle(y + \gamma\sin\omega t)^2\rangle = y^2 + \gamma^2/2$, and the terms containing $\cos\omega t$ average to zero to this order, so

$$
\ddot y - \varepsilon\Bigl(1 - \frac{\gamma^{2}}{2} - y^{2}\Bigr)\dot y + y = 0 .
$$
Equivalent linearization with $y = a\cos\theta$, $\dot y = -a\sin\theta$, exactly as in Formula 23.4.1, gives

$$
\dot a = \frac{\varepsilon a}{2}\Bigl(1 - \frac{\gamma^{2}}{2} - \frac{a^{2}}{4}\Bigr),\qquad \dot\theta = 1 .
\tag{23.10}
$$

**Proposition 23.5.1 (Entrainment by a Strong Drive)** To this order, the solution of (23.9) is $x = \gamma\sin\omega t + a\sin(t + \theta_0)$. If $\gamma^2 < 2$, the free oscillation persists with amplitude $a = 2(1 - \gamma^2/2)^{1/2}$ beside the forced one (a quasi-periodic, mixed state). If $\gamma^2 > 2$, then $a \to 0$: the self-oscillation is suppressed and the oscillator follows the rhythm of the drive.

**Definition 23.5.1 (Entrainment)** An oscillator is **entrained** by a periodic signal when it abandons its own frequency and oscillates at the frequency of the signal (or at a fixed rational ratio to it), with a fixed phase difference.

**Remark 23.5.1** Proposition 23.5.1 describes entrainment by quenching: a drive far from resonance must be strong ($\gamma^2 > 2$) to take over. Near resonance, $\omega \approx 1$, much weaker coupling suffices. Averaging the phase difference $\phi$ between oscillator and drive then gives an equation of Adler type, $\dot\phi = \Delta\omega - \kappa\sin\phi$, which locks ($\dot\phi = 0$) when the frequency mismatch $\lvert\Delta\omega\rvert$ is smaller than the coupling $\kappa$; the locked region in the plane of mismatch and coupling is an Arnold tongue. Cells of the PSM, with nearly identical clocks, are in this weak-coupling regime.

### 23.5.3. Populations of Oscillators

The modern description of a tissue of coupled clocks keeps only the phase of each oscillator.

**Definition 23.5.2 (Kuramoto Model)** In the **Kuramoto model**, $N$ oscillators with phases $\theta_i$ and natural frequencies $\omega_i$ drawn from a distribution $g(\omega)$ interact through

$$
\dot\theta_i = \omega_i + \frac{K}{N}\sum_{j=1}^{N}\sin(\theta_j - \theta_i),
$$
and their synchrony is measured by the order parameter $R\,\mathrm{e}^{\mathrm{i}\Phi} = \frac1N\sum_j\mathrm{e}^{\mathrm{i}\theta_j}$, $0 \le R \le 1$. In the limit $N \to \infty$ with a symmetric unimodal $g$, the incoherent state $R = 0$ is stable for $K < K_c = 2/\bigl(\pi g(\bar\omega)\bigr)$ and a partially synchronized state with $R > 0$ appears for $K > K_c$ (stated without proof).

The coupling term can be rewritten as $KR\sin(\Phi - \theta_i)$: each oscillator is pulled towards the mean phase with a strength proportional to the synchrony already achieved, a positive feedback that makes the transition to synchrony collective. In the PSM, coupling acts between neighbours, and the delay of Delta–Notch signalling (the time to make and present Delta) enters as a phase lag; models with coupling delays explain why the collective period of the tissue differs from that of isolated cells, which is observed in dissociated PSM cells (Morelli et al. 2009; Herrgen et al. 2010).

![Synchronization of PSM clocks. (A) The forced van der Pol oscillator (23.9) with $\varepsilon = 0.1$ and drive frequency $\omega = 2.5$: the amplitude of the free oscillation after transients (points, numerical) against the forced amplitude $\gamma$, and the prediction $a = 2(1 - \gamma^2/2)^{1/2}$ of the averaged equation (23.10) (line); beyond $\gamma = \sqrt2$ the free oscillation is quenched and the oscillator follows the drive. (B, C) A sheet of $40 \times 12$ phase oscillators with natural periods scattered by 5% and random initial phases, coupled to their four neighbours: the order parameter $R(t)$ for coupling strength 0 (no Notch signalling) and 1 (B), and the phases after 30 periods (C, colour = phase): without coupling the phases stay disordered (salt-and-pepper, as in Notch pathway mutants); with coupling neighbours lock within a few periods, and the remaining long-wavelength phase gradient across the sheet relaxes slowly, so that $R$ rises steadily towards 1](./plots/synchronization.py)

## 23.6. The Wavefront

### 23.6.1. Opposing Gradients in the PSM

The clock gives every cell a phase; a spatial pattern needs, in addition, a ruler. In the PSM the ruler is a pair of opposing gradients. FGF8 (with FGF4) and Wnt3a signalling are high in the tail bud and decline anteriorly; retinoic acid from the somites is high anteriorly. Cells in the posterior PSM, under high FGF/Wnt, are immature and cannot respond to the clock by forming a boundary; cells that fall below a threshold of FGF/Wnt signalling become competent.

**Definition 23.6.1 (Determination Front)** The **determination front** (wavefront) is the level in the PSM at which falling FGF and Wnt signalling, opposed by rising retinoic acid, make cells competent to respond to the **segmentation clock** and commit them to their segmental fate. It lies several somite lengths posterior to the forming somite (at about S-IV in the chick) and moves posteriorly with the tail bud.

Three experiments located and characterized it (Dubrulle et al. 2001). First, inversion of pieces of chick PSM along the anterior-posterior axis: a piece at the level of S0 to S-III kept its original anterior-posterior polarity, marked by the rostrocaudal pattern of gene expression in the somites that formed from it (it was determined); pieces from S-VI and further back were respecified according to their new position (undetermined); between them, at about S-IV, the result was mixed. Second, beads soaked in FGF8 implanted beside the PSM made the somites forming near them smaller, as if the front had been held back so that cells crossed it later. Third, inhibiting the FGF receptor with SU5402 made somites larger, as if the front had jumped forward. The gradient itself is created in an unusual way: *Fgf8* is transcribed only in the tail bud (an intron probe for nascent transcripts labels only there), and cells that leave the tail bud stop transcribing it, so the amount of *Fgf8* mRNA, and of protein, decays with the time since a cell left; because the tail bud moves steadily backwards, time since leaving becomes distance from the tail bud (Dubrulle and Pourquié 2004). A similar gradient of nuclear **β-catenin** reflects Wnt signalling (Aulehla et al. 2008), and RA produced by Raldh2 in the somites antagonizes both by repressing *Fgf8* transcription, while FGF signalling induces the RA-degrading enzyme Cyp26.

### 23.6.2. Biochemical Waves: Fisher's Equation

How does a sharp boundary between two states arise and move? Suppose a cell can be in a state with or without a molecular species $A$, starting with a small amount $\varepsilon$, and that $A$ is produced autocatalytically from a nondepleting source $S$ and removed in pairs: $S + A \rightleftharpoons 2A$, so

$$
\dot A = kA - k'A^{2}.
$$
This logistic equation has two steady states, $A = 0$ (unstable) and $A_0 = k/k'$ (stable), and the solution $A(t) = A_0/\bigl(1 + (A_0/\varepsilon - 1)\mathrm{e}^{-kt}\bigr)$. Now let $A$ pass between neighbouring cells in a closely packed row, as a monomolecular exchange $A(x - \Delta x) \rightleftharpoons A(x) \rightleftharpoons A(x + \Delta x)$ with rate constant $\gamma_{\mathrm{t}}$:

$$
\dot A(x, t) = kA - k'A^{2} + \gamma_{\mathrm{t}}\bigl[A(x + \Delta x) + A(x - \Delta x) - 2A(x)\bigr].
$$
If $A$ varies slowly from cell to cell, the bracket is $(\Delta x)^2 A_{xx} + \dots$, and with $D = \gamma_{\mathrm{t}}(\Delta x)^2$ the result is a **reaction-diffusion equation**, $A_t = kA - k'A^2 + DA_{xx}$. Here diffusion arises from transfer between cells, a mesoscopic description; Brownian motion of molecules gives the same form, and the value of $D$ is often the only hint as to which process is at work. Scaling $A = A_0 a$, $t = \tau/k$ and $x = (D/k)^{1/2}X$ gives

$$
a_\tau = a - a^{2} + a_{XX}.
\tag{23.11}
$$

**Definition 23.6.2 (Fisher–KPP Equation)** The **Fisher–KPP equation** is $u_t = Du_{xx} + ru(1 - u)$, or (23.11) in scaled form: logistic growth with diffusion (Fisher 1937; Kolmogorov, Petrovsky and Piskunov 1937). Its **traveling wave solutions** $u = U(x - ct)$ connect the stable state $u = 1$ behind the front to the unstable state $u = 0$ ahead of it.

In the somite context, a cell at $a = 1$ (for instance a cell activated in the tail region) transfers $A$ to a resting neighbour at $a = 0$, raises it to 1, and so on down the line: a wave of activation. For $a(X, \tau) = a(\xi)$, $\xi = X - c\tau$,

$$
a'' + ca' + a(1 - a) = 0 .
$$
Near the leading edge, $a \approx 0$ and $a'' + ca' + a = 0$, with solutions $\exp\bigl[\bigl(-\frac c2 \pm \sqrt{c^2/4 - 1}\bigr)\xi\bigr]$. A concentration cannot oscillate below zero, so the roots must be real: $c \ge 2$, the minimal speed derived in [2.5.7](/2.5.7) ($2\sqrt{rD}$ in dimensional form).

**Proposition 23.6.1 (Speed of a Front from a Step)** For the step initial condition $a(X, 0) = 1$ for $X < 0$ and $0$ for $X > 0$, the linearized leading edge $a_\tau = a + a_{XX}$ gives

$$
a_X(X, \tau) = -\frac{1}{\sqrt{4\pi\tau}}\,\mathrm{e}^{\tau - X^{2}/(4\tau)},
$$
and a level $a_X = -u$ moves with speed $\dot X \to 2$ as $\tau \to \infty$.

**Proof** Take the **Laplace transform** in time, $\hat a(X, p) = \int_0^\infty\mathrm{e}^{-p\tau}a(X, \tau)\,\mathrm{d}\tau$ for $p > 1$. Since the transform of $a_\tau$ is $p\hat a - a(X, 0)$,

$$
\hat a'' + (1 - p)\hat a = \begin{cases}-1, & X < 0,\\ 0, & X > 0.\end{cases}
$$
Bounded solutions are $\hat a = 1/(p - 1) + k_3\mathrm{e}^{X\sqrt{p - 1}}$ for $X < 0$ and $\hat a = k_4\mathrm{e}^{-X\sqrt{p - 1}}$ for $X > 0$; continuity of $\hat a$ and $\hat a'$ at $X = 0$ gives $k_4 = -k_3 = 1/\bigl(2(p - 1)\bigr)$. For $X > 0$, $\hat a' = -\mathrm{e}^{-X\sqrt{p - 1}}/\bigl(2\sqrt{p - 1}\bigr)$; since $\mathrm{e}^{-X\sqrt s}/\sqrt s$ is the transform of $\mathrm{e}^{-X^2/(4\tau)}/\sqrt{\pi\tau}$ and the shift $s = p - 1$ multiplies by $\mathrm{e}^{\tau}$, the stated formula follows. Setting $a_X = -u$ gives $\mathrm{e}^{\tau - X^2/(4\tau)} = u\sqrt{4\pi\tau}$, that is

$$
X = 2\tau\Bigl(1 - \frac{1}{\tau}\ln\bigl(u\sqrt{4\pi\tau}\bigr)\Bigr)^{1/2},\qquad \dot X = 2 - \frac{1}{2\tau} + O\Bigl(\frac{\ln\tau}{\tau^{3/2}}\Bigr) \to 2 . \qquad\square
$$

The front set up from a localized start therefore selects the minimal speed. The linear analysis predicts that the front lags a front of exact speed 2 by $\frac12\ln\tau$; for the nonlinear equation the lag is $\frac32\ln\tau$ (Bramson 1983), so the approach to the asymptotic speed is slow in both cases. Such a front is pulled by its leading edge: its speed is set by growth and spread where $a$ is small, and fluctuations in the few cells at the edge matter. By itself a logistic front is therefore a poor ruler for somites, but it shows how a moving boundary between two cell states can be maintained.

### 23.6.3. An FGF–Retinoic Acid Model

The real wavefront involves two antagonistic species. In a frame moving with the tail bud, let $x \ge 0$ be the distance from the tail bud, where FGF ($F$) is held at $F_0$. FGF decays at rate $\gamma$, is inhibited by retinoic acid ($A$) with coefficient $\alpha$, and diffuses; RA is made by a self-enhancing process saturating at 1, inhibited by FGF, and diffuses little:

$$
F_t = -\gamma F - \alpha AF + DF_{xx},\qquad A_t = A(1 - A) - \beta AF .
\tag{23.12}
$$
Without RA, the steady FGF profile is the exponential $F = F_0\mathrm{e}^{-x\sqrt{\gamma/D}}$ of a **morphogen** with **decay length** $\sqrt{D/\gamma}$ ([7.5.11](/7.5.11)), not a sharp boundary. Without diffusion and source, the uniform states are $(F, A) = (0, 0)$, a saddle ($\delta\dot F = -\gamma\delta F$, $\delta\dot A = \delta A$), and $(0, 1)$, stable but uninteresting: RA rises to its maximum everywhere.

**Proposition 23.6.2 (Two-Zone Profile)** In the steady state of (23.12), RA is absent ($A = 0$) where $\beta F > 1$ and equals $A = 1 - \beta F$ where $\beta F < 1$. The boundary $x_0$, where $\beta F = 1$, lies approximately at

$$
x_0 \approx \sqrt{D/\gamma}\,\ln(\beta F_0),
$$
behind it FGF decays with length $\sqrt{D/\gamma}$ and beyond it with the shorter length $\sqrt{D/(\alpha + \gamma)}$; in the anterior zone

$$
\frac{D}{2}F_x^{2} + V(F) = 0,\qquad V(F) = -\frac{\alpha + \gamma}{2}F^{2} + \frac{\alpha\beta}{3}F^{3},
$$
so that FGF arrives at the front with slope $F_x(x_0) = -\beta^{-1}\sqrt{(\alpha + 3\gamma)/(3D)}$.

**Proof** At steady state $A(1 - A - \beta F) = 0$, and the root $A = 0$ is unstable wherever $\beta F < 1$, leaving the two zones. Posteriorly $DF_{xx} = \gamma F$, whose solution decaying from $F_0$ reaches $1/\beta$ at about $\sqrt{D/\gamma}\ln(\beta F_0)$ (the correction from matching is of order $\sqrt{D/\gamma}$). Anteriorly, substituting $A = 1 - \beta F$ gives $DF_{xx} = (\alpha + \gamma)F - \alpha\beta F^2$; multiplying by $F_x$ and integrating from $x$ to $\infty$, where $F = F_x = 0$, gives the energy integral. As $F \to 0$, $F_x \approx -F\sqrt{(\alpha + \gamma)/D}$; at $F = 1/\beta$ the integral gives the stated slope. $\square$

**Remark 23.6.1** The potential $V$ has a minimum at $F^* = (\alpha + \gamma)/(\alpha\beta)$, which might suggest a plateau of FGF at that value. But $F^* > 1/\beta$, outside the zone where the anterior equation holds, and in the mechanical analogy (position $F$, time $x$) the orbit leaving $F = 0$ with zero energy never reaches it. The effect of RA is instead to sharpen the profile at the front, by a factor $\sqrt{(\alpha + \gamma)/\gamma}$ in the decay rate, and to create a steep RA boundary $A = 1 - \beta F$ immediately anterior to it.

The model captures two properties of the real front. It is sharper than a single gradient, because mutual inhibition converts a graded input into two zones. And its position depends only logarithmically on the strength of the source, so that a twofold fluctuation of $F_0$ shifts it by only $\sqrt{D/\gamma}\ln 2$; since the frame moves with the tail bud, the front advances at the speed of axis elongation. Two cautions apply to all models of this kind. The messengers come in families (FGF4 and FGF8, several Wnts, RA and its receptors), so models amalgamate similar species into effective quasi-species, and it is not easy to tell a causal species from one that merely follows in unison. And the origin of $D$, diffusion of protein, transfer between cells or inheritance of mRNA by cells leaving the tail bud, is not sharply defined; the decay of *Fgf8* mRNA in cells moving away from the source produces an exponential profile without any diffusion at all. More detailed models of the clock, the front and their coupling have been developed by the Oxford group (Collier, Maini, Baker and colleagues).

![The wavefront. (A) Steady state of the FGF–RA model (23.12) in the frame of the tail bud ($x = 0$), with $D = \gamma = \beta = 1$, $\alpha = 8$ and $F_0 = 20$: FGF ($F$, orange, log scale) decays with slope $-1$ behind the front, where retinoic acid is absent, and three times faster beyond it; RA ($A$, green, linear scale) rises steeply from the front, where $\beta F = 1$ (dashed line), to 1 anteriorly. (B) The front position (points, numerical) against the source strength $F_0$ on a log axis, and $\sqrt{D/\gamma}\ln(\beta F_0)$ (line): a constant offset, the same logarithmic slope. (C) Fisher's equation (23.11) from a step: profiles at successive times. (D) The speed of the level $a = 0.5$ approaches the minimal speed 2 slowly from below](./plots/fgf-ra-front.py)

## 23.7. The Clock-and-Wavefront Model

**Definition 23.7.1 (Clock-and-Wavefront Model)** In the **clock-and-wavefront model** (Cooke and Zeeman 1976), the cells of the paraxial mesoderm contain an oscillator, smooth and synchronized among neighbours (the clock); a slow front of maturation passes along the axis from anterior to posterior (the wavefront); and cells passing the front undergo a rapid change of state, gated by the phase of the clock, that groups the cells passing during one cycle into one somite.

Cooke and Zeeman proposed the model, before any cyclic gene was known, to explain why somite number is regulated. In *Xenopus* and mouse embryos that are experimentally reduced in size (by removing cells early), the number of somites is normal and each somite is smaller (Tam 1981 in the mouse); a mechanism that counted cells, or that cut blocks of a fixed size, would make fewer somites. The three elements, smooth oscillation, a slow wavefront and rapid cellular change, are each identified today: the Hes/Notch clock, the FGF/Wnt/RA front, and the Mesp2-triggered epithelialization of Section 23.8.

**Formula 23.7.1 (Somite Size and Number)** If the front moves posteriorly at speed $v$ and the clock has period $P$, the length of one somite is

$$
S = vP,
$$
and the number of somites formed during a period of axis elongation of duration $\Theta$ is $N = \Theta/P$. In a frame moving with the tail bud, the frozen phase of a cell that crosses the front is $\phi = 2\pi x/(vP) + \text{const}$, so boundaries (fixed phase) appear every $vP$ along the axis.

The model explains the experiments of Section 23.6: an FGF bead holds the front back locally, so that the next somites are smaller, and an FGF receptor inhibitor lets it advance, so that they are larger, without changing the clock. It explains how snakes have hundreds of vertebrae. In the corn snake the PSM is somewhat longer than in the chick or mouse, but the decisive difference is a faster clock relative to the rate of growth: in snake embryos up to nine stripes of *Lfng* expression are seen at once in the PSM, against one to three in the chick and mouse, and somites are about a third the size (Gomez et al. 2008). It explains the end of segmentation. The posterior **Hox genes**, activated later in the tail bud (Section 23.9), progressively repress Wnt signalling, axis elongation slows while the clock does not, the forming somites catch up with the tail bud, retinoic acid reaches the **progenitors**, and the PSM is exhausted (Denans et al. 2015).

Live imaging has refined the picture. The waves of expression do not simply propagate; they arise because cells slow their oscillation as they mature, so that a phase gradient develops along the PSM, posterior cells being ahead. Two consequences follow. A stripe moves faster when the gradient is shallow. And because the PSM shortens during somitogenesis, the anterior end moves towards the waves, so that the period of somite formation is shorter than the period of the clock in the tail bud, a Doppler effect (Soroldoni et al. 2014). In explants of mouse PSM that scale their pattern to their size, segment boundaries form where the local phase lags a fixed amount behind the tail bud, which suggests that cells read a phase difference rather than an absolute concentration of FGF (Lauschke et al. 2013); the relative roles of the front and of phase gradients are still being worked out.

![The clock-and-wavefront model. (A) Kymograph of a strip of paraxial mesoderm in the frame of the embryo (vertical axis: position along the axis, anterior at the bottom; horizontal axis: time). The tail bud (upper boundary of the coloured region) moves posteriorly at constant speed and the determination front (dashed) follows it at a fixed distance. Within the PSM the colour shows the clock phase of each cell: cells oscillate with a period of 1 in the tail bud and more slowly as they approach the front, so stripes of equal phase move anteriorly and narrow. At the front each cell's phase is frozen; alternating shades of red (anterior to the front) mark the somites, one per cycle, of length $vP$. (B) The phase of four cells born at successive times, plotted against time: each slows down as it nears the front and stops there; their frozen phases differ by $2\pi$ per somite length. (C) Somite length $S = vP$ against clock period $P$ for three speeds of elongation; a faster clock relative to growth gives more, smaller somites, as in snakes](./plots/clock-wavefront.py)

## 23.8. Boundaries and Epithelialization

### 23.8.1. Molecular Events at the Boundary

The clock and the front decide when and where; a set of transcription factors and adhesion molecules then makes the boundary. In the anterior PSM, at the level of S-I, the combination of Notch activity from the clock and of Tbx6 below the front switches on the bHLH transcription factor Mesp2 (Mesp-a/b in zebrafish), first in a somite-wide domain. Mesp2 then represses Notch activity and induces Ripply1/2, which suppresses Tbx6 protein; Mesp2 expression becomes restricted to the anterior (rostral) half of the future somite, and the posterior limit of its domain marks the next boundary. Mesp2 confers rostral identity (with Tbx18), while in the caudal half Notch activity induces *Uncx4.1* and caudal identity; this rostrocaudal polarity of each somite later directs **neural crest** migration and nerve growth through the rostral halves ([7.5.20](/7.5.20)) and the resegmentation of the vertebrae ([7.5.24](/7.5.24)). Mice lacking *Mesp2* form no epithelial somites and their vertebrae are fused, with caudal character throughout.

The boundary itself is a **mesenchymal–epithelial transition** (MET). Mesp activity induces the receptor EphA4 in the cells anterior to the future fissure; EphA4 induces its ligand ephrin-B2 in the cells across the boundary, and the forward and reverse signalling between them repels the two populations, as in the **rhombomeres** of [7.5.18](/7.5.18). Dominant-negative Eph constructs give abnormal boundaries; in the zebrafish *fused somites* mutant (*tbx6*), *ephA4* is absent and *ephrinB2* expressed uniformly, and no boundaries form. Downstream, ephrin-B2 signalling lowers the activity of the GTPase Cdc42 in the peripheral cells of the somitomere, which epithelialize (low Cdc42 is required for epithelialization; forced Cdc42 activity prevents it), while Rac1 is also needed; and it activates **integrin** α5, so that **fibronectin** is assembled into fibrils in the cleft, completing the separation. The transcription factor Paraxis (Tcf15) is needed for the cells of the somite to epithelialize: in its absence somite-sized blocks of mesenchyme form, so segmentation and epithelialization are separable. The epithelial cells are joined by N-**cadherin**. In *Xenopus* a fissure separates a block of cells that rotates by 90°; in zebrafish the furrow spreads mediolaterally; in chick and mouse cells reshuffle at the boundary like a ball and socket. Transplants show that the boundary is instructed by the cells posterior to it: posterior border cells grafted into the middle of the PSM induce an ectopic boundary in the tissue anterior to them, and ordinary PSM cells acquire this ability when activated Notch is electroporated into them (Sato et al. 2002).

### 23.8.2. A Reaction–Diffusion Model of Condensation

Cells leave the region of high FGF at various phases of their cycle, and the next step of their fate, for instance a higher adhesiveness that collects them into tight clusters, is decided then. Quantitative fluctuations are large, so some boundary-sharpening process is needed. The simplest idea is an activator–inhibitor system in which a diffusible species biases the adhesive state of a cell, balanced by a locally produced antagonist. Is such a system compatible with a periodic arrangement of somites?

Consider $a_t = f(a, h) + \varepsilon a_{xx}$, $h_t = g(a, h) + \nu h_{xx}$, whose uniform state $(a_0, h_0)$ is stable without diffusion. By the Turing condition (Theorem 12.3.1), diffusion destabilizes a mode $\cos kx$ when the determinant of $M_k = \begin{pmatrix}f_a - \varepsilon k^2 & f_h\\ g_a & g_h - \nu k^2\end{pmatrix}$ becomes negative; this cannot happen if the Jacobian is symmetric, but biological Jacobians rarely are.

**Example 23.8.1 (Turing's Example)** The reactions $a + h \to 2a$, $\varnothing \to h$, $a \to \varnothing$ give, after scaling (Turing 1952),

$$
a_t = \tfrac{1}{16}a(h - 1) - \tfrac34 + \varepsilon a_{xx},\qquad h_t = -\tfrac{1}{16}ah + 1 + \nu h_{xx},
$$
with uniform state $a_0 = h_0 = 4$ and Jacobian $f_a = \frac{3}{16}$, $f_h = \frac14$, $g_a = -\frac14$, $g_h = -\frac14$. Its eigenvalues are $\lambda = \frac{1}{32}(-1 \pm \mathrm{i}\sqrt{15})$, so the uniform state is stable. With diffusion, a mode is unstable when $\bigl(\frac{3}{16} - \varepsilon k^2\bigr)\bigl(\frac14 + \nu k^2\bigr) > \frac{1}{16}$, that is when $-\frac{1}{64} + \bigl(\frac{3}{16}\nu - \frac14\varepsilon\bigr)k^2 - \varepsilon\nu k^4 > 0$ for some $k^2 > 0$. By Theorem 12.3.1 this holds if and only if $\frac{3}{16}\nu - \frac14\varepsilon > \frac14\sqrt{\varepsilon\nu}$; with $r = \varepsilon/\nu$ this is $4r + 4\sqrt r < 3$, that is $\sqrt r < \frac12$:

$$
\frac{\varepsilon}{\nu} < \frac14 .
$$
The inhibitor $h$ must diffuse at least four times faster than the activator $a$. At threshold the critical wave number is $k_c^2 = 1/(16\varepsilon)$.

The stability of the uniform state without diffusion is mathematically convenient but has no particular biological justification: there is no reason to imagine diffusion being switched on. A model closer to the situation in the anterior PSM has a diffusing substrate $a$, produced uniformly, and a **cell-autonomous**, self-enhancing species $h$ that consumes it (an activator–substrate, or depletion, model of the **Gierer–Meinhardt model** family):

$$
a_t = \mu - h^{2}a + Da_{xx},\qquad h_t = ch^{2}a - \lambda h,
\tag{23.13}
$$
corresponding to $a + 2h \to 3h$, $\varnothing \to a$, $h \to \varnothing$.

**Proposition 23.8.1 (Periodic Steady States of the Depletion Model)** The steady states of (23.13) with $h \ne 0$ satisfy $h = \lambda/(ca)$ and

$$
Da_{xx} = \frac{\lambda^{2}}{c^{2}a} - \mu,\qquad \frac{D}{2}a_x^{2} + V(a) = E,\qquad V(a) = \mu a - \frac{\lambda^{2}}{c^{2}}\ln a .
$$
Since $V$ is convex with a single minimum at $a_m = \lambda^2/(c^2\mu)$, the uniform state, all bounded solutions are periodic in $x$. Near $a_m$, $Da_{xx} + V''(a_m)(a - a_m) = 0$ with $V''(a_m) = c^2\mu^2/\lambda^2$, so that

$$
a = a_m + B\cos\bigl(k_0(x - x_1)\bigr),\qquad k_0 = \frac{c\mu}{\lambda\sqrt D},
$$
with the amplitude $B$ (equivalently the energy $E$) free; orbits of larger amplitude have longer spatial periods.

**Proof** The second equation of (23.13) at steady state gives $h(cha - \lambda) = 0$. Substituting $h = \lambda/(ca)$ into the first, $h^2a = \lambda^2/(c^2a)$. Multiplying $Da_{xx} = V'(a)$ by $a_x$ and integrating gives the energy integral; $V''(a) = \lambda^2/(c^2a^2) > 0$. In the mechanical analogy ($a$ position, $x$ time) a particle in a convex well oscillates, so bounded orbits are periodic; linearizing at the minimum gives $k_0$. $\square$

The spatial oscillator has a wavelength set by the parameters, but its amplitude is not determined at this level, and the family is neutral, like the Lotka–Volterra orbits. Linear stability of the uniform state shows why. Without diffusion it is stable when $c^2\mu^2 > \lambda^3$ (trace $\lambda - c^2\mu^2/\lambda^2 < 0$, determinant $c^2\mu^2/\lambda > 0$); with diffusion of $a$ alone, the determinant of $M_k$ is $c^2\mu^2/\lambda - D\lambda k^2$, negative for every $k > k_0$. Every mode shorter than the wavelength $2\pi/k_0$ grows, the shortest fastest: because $h$ does not diffuse, nothing selects a wavelength, and the instability amplifies differences between single cells. Such a mechanism is a sharpener rather than a ruler: it can turn a graded difference into an all-or-none difference between neighbouring cells, but the spacing must come from elsewhere, from the clock and the front. A small diffusion of $h$, or coupling between cells, restores a band of growing modes and a preferred spacing.

**Remark 23.8.1** One process often produces a pattern and another then takes over and makes it reproducible. In **gastrulation**, anisotropic differential adhesion may suffice to drive **invagination**, but **bottle cells** make it reliable ([7.5.9](/7.5.9)). The same may hold for somites: when chick PSM cells are dissociated and reaggregated, the aggregates form somite-like epithelial balls of the right size without any detectable oscillation of the clock genes, and a model based on differential adhesion and **cell sorting** (the cell Potts model of [7.5.7](/7.5.7)) reproduces them (Dias et al. 2014, "Somites without a clock"). **Self-organization** by adhesion can form somites; the clock and front make them form in order, at the right time and in register on both sides. To what extent present-day embryos rely on the adhesive mechanism is not yet known.

![Condensation and boundary sharpening. (A) Growth rate of mode $k$ in Turing's example (Example 23.8.1) for diffusion ratios $\varepsilon/\nu = 0.1$, $0.25$ and $0.5$ (with $\nu = 1$): a band of unstable modes exists only for $\varepsilon/\nu < 1/4$. (B) The depletion model (23.13) with $\mu = \lambda = 1$, $c = 2$, $D = 1$: growth rate of the uniform state when the self-enhancing species does not diffuse (every mode with $k > k_0 = 2$ grows, up to the rate $\lambda$) and when it diffuses slightly ($D_h = 0.01$, a band of finite width). (C) Phase portrait of the steady states of (23.13), the level curves of $\frac{D}{2}a_x^2 + V(a)$ around the uniform state $a_m = 0.25$: every closed curve is a spatially periodic profile. (D) Three such profiles: small amplitude, nearly a cosine of wave number $k_0$; larger amplitudes, longer periods and sharper peaks of the self-enhancing species $h = \lambda/(ca)$](./plots/condensation.py)

## 23.9. Somite Identity and Hox Genes

Somites look alike but give rise to different structures: cervical vertebrae have no ribs, thoracic vertebrae have ribs, lumbar vertebrae none. Their identity is fixed early, in the PSM. When chick PSM that would form thoracic somites is grafted into the cervical region of a younger embryo, it forms vertebrae with ribs in the neck (Kieny et al. 1972); its fate depends on its origin, not its new surroundings.

The identity is encoded by **Hox genes** ([7.5.15](/7.5.15)). In the paraxial mesoderm they are expressed with spatial **Hox colinearity**: genes at the 3′ end of a cluster anteriorly, those at the 5′ end progressively more posteriorly, and the combination expressed by a somite specifies the kind of vertebra it will form. Loss and **gain of function** confirm the code. In mice lacking *Hoxc8*, the first lumbar vertebra forms a pair of ribs like a thoracic vertebra, and the vertebrae shift anteriorly in character, a **homeotic transformation**; mice lacking all three *Hox10* paralogues (*Hoxa10*, *Hoxc10*, *Hoxd10*) have ribs on all lumbar vertebrae (Wellik and Capecchi 2003). Conversely, expressing *Hoxa10* throughout the PSM eliminates all ribs, and expressing *Hoxb6* throughout gives ribs on every vertebra, a "snake-like" mouse (Carapuço et al. 2005). Both transformations follow from expression in the PSM, not in the somites: cells are instructed in the PSM and execute the instruction later. Across species the Hox code tracks the anatomy rather than the somite number: the anterior limit of *Hoxc6* expression lies at the cervical–thoracic boundary in mouse (somite 12), chick (somite 19) and goose (somite 22), although the number of cervical vertebrae differs (Burke et al. 1995).

The spatial order arises from temporal **colinearity**. In the tail bud, **Hox genes** are activated one after another from the 3′ to the 5′ end of each cluster, as the **chromatin** of the cluster is progressively opened (shown by chromosome conformation capture in the *Hoxd* cluster: Noordermeer et al. 2014). Cells that leave the tail bud early carry the anterior code; cells that leave later carry more posterior genes, and they remember their state. Hox genes may also regulate when cells ingress (Iimura and Pourquié 2006), and the posterior *Hox13* paralogues slow axis elongation and bring segmentation to an end (Section 23.7). Mutations of the **segmentation clock**, but not shifts of the front by FGF, alter Hox expression, so the clock may also coordinate the timing of Hox activation with segment formation.

## 23.10. Somite Compartments and Their Derivatives

A newly formed somite is an epithelial ball of uncommitted cells: any part of it can still form any somitic derivative. Its fates are assigned by signals from the neighbouring tissues, and its compartments appear in a fixed order.

**Definition 23.10.1 (Somite Compartments)** As the somite matures it is subdivided into: the **sclerotome**, the ventromedial part, whose cells undergo an **epithelial–mesenchymal transition** and surround the notochord and **neural tube**, forming the vertebrae and ribs (with its subregions: the arthrotome, forming vertebral joints and the outer intervertebral disc); the **dermomyotome**, the remaining dorsolateral epithelial sheet, which forms muscle precursors, the dermis of the back and brown fat; the **myotome**, a layer of muscle cells that forms beneath the dermomyotome from cells of its edges (lips), the first skeletal muscle of the embryo; and the **syndetome**, a strip of dorsal sclerotome cells next to the myotome that forms the tendons.

![Maturation of the somite (transverse sections of an amniote trunk, dorsal up; derivatives labelled on the right side). (A) Epithelial somite: a ball of radially arranged epithelial cells around the somitocoel, beside the neural tube; the notochord, paired dorsal aortae, intermediate mesoderm and the lateral plate split by the coelom lie below. (B) The ventromedial wall undergoes an epithelial–mesenchymal transition into the sclerotome (dots), which migrates towards the notochord; the dorsolateral wall remains as the epithelial dermomyotome. (C) Mature somite: the myotome forms beneath the dermomyotome from its lips, the syndetome lies between myotome and sclerotome, and sclerotome cells surround the notochord and the ventral neural tube. Signals: Shh from notochord and floor plate (with Noggin) induces sclerotome; Wnts from the dorsal neural tube and the surface ectoderm maintain the dermomyotome and induce the primaxial (epaxial) myotome; BMP4 from the lateral plate, antagonized by Noggin, keeps the lateral (abaxial) lip undifferentiated; NT-3 from the neural tube promotes the dermis; FGF from the myotome induces scleraxis in the syndetome](./plots/somite-maturation.py)

| Signal | Source | Effect on the somite |
|---|---|---|
| Shh, Noggin | notochord, **floor plate** | induce sclerotome (*Pax1*, *Pax9*); a notochord grafted beside the dorsal somite converts dermomyotome into sclerotome |
| Wnt1, Wnt3a | dorsal neural tube | with low Shh, induce *Myf5* in the dorsomedial (primaxial) myotome |
| Wnt6, Wnt7a | surface **ectoderm** | maintain the epithelial dermomyotome; induce *MyoD* laterally |
| BMP4 | lateral plate **mesoderm** | keeps lateral cells undifferentiated (limb and body-wall muscle precursors); antagonized by Noggin from the lips |
| NT-3 | neural tube | EMT of the central dermomyotome into dermis |
| FGF4/8 | myotome | induce *scleraxis* in the syndetome |
| Delta1 on migrating **neural crest** | passing neural crest cells | transient Notch activation in the dorsomedial lip triggers myogenesis (Rios et al. 2011) |

The logic is that of position: the sclerotome forms where Shh is high (next to the notochord), the dorsomedial myotome where Wnt from the neural tube meets moderate Shh, and the lateral muscle precursors where Wnt is present but BMP is blocked. Removing or rotating the neural tube prevents the dermis from forming; removing the notochord abolishes the sclerotome and vertebral bodies. Derivatives also include more than the classic three. The central dermomyotome gives rise to dermis, to muscle **progenitors** and satellite cells, and to brown adipocytes, which share a *Myf5*-expressing precursor with skeletal muscle and are diverted by the transcription factor PRDM16 (Seale et al. 2008). Posterior sclerotome cells form the endothelium of the dorsal aorta and the intersegmental vessels; whether some of these somite-derived endothelial cells give rise to haematopoietic **stem cells** is debated ([7.5.29](/7.5.29)). The medial sclerotome forms the meninges of the spinal cord.

Somites differ between vertebrate groups in proportion. In fish, most of the somite becomes myotome, which forms the large blocks of trunk muscle used in swimming, and the sclerotome is small. In zebrafish the adaxial cells next to the notochord, specified by Hedgehog, migrate laterally through the somite to become the superficial slow-twitch muscle, and a few remain at the horizontal myoseptum as muscle pioneers; the cells behind them form fast muscle. In amniotes the myotome is a thin layer and the sclerotome large. The boundary in the body wall between muscles and dermis derived from somites and those derived from the lateral plate is the lateral somitic frontier; the muscles medial to it (primaxial: deep back and intercostal muscles) develop within somite-derived connective tissue, the abaxial muscles of the limbs and ventral body wall within lateral plate connective tissue ([7.5.24](/7.5.24)).

## 23.11. Segmentation Defects: Spondylocostal Dysostosis

**Definition 23.11.1 (Spondylocostal Dysostosis)** **Spondylocostal dysostosis** (SCD) is a congenital disorder of segmentation of the axial skeleton: multiple vertebrae are malformed (hemivertebrae, block and butterfly vertebrae, fused and irregular segments) along most of the spine, with fused or missing ribs, a short trunk and usually non-progressive scoliosis. Most forms are **autosomal** **recessive** and caused by mutations in genes of the **segmentation clock** and the boundary.

The genes known to cause SCD are *DLL3* (SCD1, the most common), *MESP2*, *LFNG*, *HES7*, *TBX6* and *RIPPLY2*: all members of the Notch-based clock or of the Mesp2–Tbx6–Ripply circuit of the boundary, which is the strongest evidence that the mouse mechanism operates in humans. The vertebrae are malformed because each vertebra is built from the posterior half of one somite and the anterior half of the next ([7.5.24](/7.5.24)); when the rostrocaudal polarity of the somites is disordered, the halves combine irregularly. Milder defects of segmentation cause congenital scoliosis, which affects about 1 in 1000 births. In a Chinese cohort about 10% of congenital scoliosis was explained by compound inheritance at *TBX6*: a rare **null allele** on one chromosome and a common hypomorphic haplotype on the other, which together reduce TBX6 dosage below a threshold (Wu et al. 2015). The environment matters as well: mice **heterozygous** for mutations in **Notch pathway** genes have normal vertebrae, but short-term hypoxia during somitogenesis, which disrupts FGF signalling and the clock, causes vertebral defects in them at high frequency (Sparrow et al. 2012), a gene-environment interaction that may explain the variable penetrance of congenital vertebral malformations.

## Summary

| Element | Mechanism | Key molecules | Model (formula) |
|---|---|---|---|
| PSM and elongation | **NMPs** in the tail bud; Wnt/FGF vs RA; graded motility, notochord push | Brachyury, Sox2, Tbx6, Msgn1, Wnt3a, FGF8, Raldh2, Cyp26 | — |
| Clock | delayed autorepression | Hes7, Her1/7, Lfng, Dll1/3 | Eq. (23.2); period Formula 23.3.2 |
| Synchrony | Delta–Notch coupling between neighbours | DeltaC, Notch1a | forced oscillator Eq. (23.10); Kuramoto model |
| Wavefront | opposing FGF/Wnt and RA gradients; *Fgf8* mRNA decay | FGF8, Wnt3a, RA | Fisher front (Proposition 23.6.1); FGF–RA (Proposition 23.6.2) |
| Somite size and number | clock read by moving front | — | $S = vP$, $N = \Theta/P$ (Formula 23.7.1) |
| Boundary | Mesp2 → Ripply, EphA4/ephrin-B2, MET | Mesp2, Tbx6, Ripply, Uncx4.1, Tbx18, Paraxis, **fibronectin** | depletion model (Proposition 23.8.1) |
| Identity | temporal and spatial **Hox colinearity** | Hox paralogues 6–13 | — |
| Compartments | position relative to signalling tissues | Shh, Wnt, BMP4/Noggin, NT-3, FGF | — |

- The paraxial mesoderm (Definition 23.1.1) segments into somites (Definition 23.1.2) at a species-specific period; the order of segmentation is already fixed in the PSM.
- A two-variable negative feedback loop cannot oscillate (Proposition 23.3.1); with a delay it can (Formula 23.3.1). In the fast limit the oscillation is a square wave, existing for $K > 2$ with $x_1 = 1/x_0$ (Proposition 23.3.2); the period is about $2(T + 1/b + 1/c)$ (Formula 23.3.2; Example 23.3.1).
- The Lotka–Volterra model (Definition 23.4.1) has neutral closed orbits and is a poor clock; limit cycles, such as that of the van der Pol oscillator (Definition 23.4.2), are robust; averaging (Formula 23.4.1) and harmonic balance (Example 23.4.1) estimate their amplitude and the threshold of oscillation.
- Delta–Notch signalling synchronizes the clocks; a strong drive entrains an oscillator (Proposition 23.5.1, Definition 23.5.1), and populations synchronize above a critical coupling (Kuramoto model, Definition 23.5.2).
- The determination front (Definition 23.6.1) is set by opposing gradients. Fisher's equation (Definition 23.6.2) gives fronts of speed 2 (Proposition 23.6.1); mutual inhibition of FGF and RA makes a sharper two-zone profile whose position depends logarithmically on the source (Proposition 23.6.2).
- The clock-and-wavefront model (Definition 23.7.1) gives $S = vP$ (Formula 23.7.1), explains size regulation, FGF bead experiments, snake segment numbers and termination; phase gradients and a Doppler effect refine it.
- Mesp2, Ripply and Eph/ephrin signalling make the boundary; a **cell-autonomous** activator sharpens but does not space the pattern (Example 23.8.1, Proposition 23.8.1); adhesion alone can make somites (Remark 23.8.1).
- **Hox genes**, activated in temporal order, give each somite its identity; signals from neighbouring tissues divide the somite into sclerotome, dermomyotome, myotome and syndetome (Definition 23.10.1); defects of the clock cause spondylocostal dysostosis (Definition 23.11.1).

## Questions

1. In a half-embryo experiment, one half of a chick embryo is fixed at once and the other half cultured for 45 minutes before fixation; both are stained for *c-hairy1*. What difference do you expect, and why does this experiment prove that the PSM contains an oscillator rather than a stable **prepattern**?

   **Answer** At time zero both halves have the same pattern. After 45 minutes (half a cycle) the cultured half shows the expression domain displaced anteriorly and narrowed, or, if the first half showed a stripe in the anterior PSM, a new broad posterior domain. A stable prepattern would look the same in both halves; a pattern that changes in a fixed time while cells do not move (marked cells stay in place) means that each cell turns the gene on and off periodically, with a phase that depends on position. Comparing many pairs at different culture times shows the pattern returning to its starting configuration after 90 minutes, the period of somite formation.

2. Show that the system $\dot p = am - bp$, $\dot m = k/(1 + (p/p_0)^2) - cm$ cannot have a periodic orbit, and explain in words what a transcriptional delay adds.

   **Answer** The divergence $\partial_p(am - bp) + \partial_m(f(p) - cm) = -b - c$ is negative everywhere, so by Bendixson's criterion there is no closed orbit; bounded trajectories tend to the single steady state (Proposition 23.3.1), through damped oscillations at most. A delay means that the protein represses its gene according to its level some time ago. If the delay is long compared with the response times, the protein keeps rising after it has already switched off transcription, overshoots, and then keeps falling after transcription has resumed: the corrections always arrive too late, which sustains the oscillation (mathematically, the delay makes the system infinite-dimensional, so the planar theorems no longer apply).

3. For the fast-turnover delay oscillator $x(t) = K/(1 + x(t - T)^2)$ with $K = 2.5$, find the two levels of the square wave and the steady state. What is the period?

   **Answer** $x_0 + 1/x_0 = 2.5$ gives $x_0 = 0.5$ and $x_1 = 2$ (Proposition 23.3.2); check $K/(1 + 0.25) = 2$ and $K/(1 + 4) = 0.5$. The steady state solves $\bar x^3 + \bar x = 2.5$: $\bar x \approx 1.11$, unstable because $\bar x > 1$. Each level lasts one delay, so the period is $2T$. Harmonic balance gives $a = \sqrt{1.5} = 1.22$, $b = 1$, compared with the mean $1.25$ and first harmonic $(4/\pi)(0.75) = 0.95$ of the square wave.

4. In the mouse, the half-lives of *Hes7* mRNA and protein are each about 20 min, and the total delay is about 30 min. Use Formula 23.3.2 to estimate the period. How would a mutation that prolongs the half-life of Hes7 protein by 10 minutes change the oscillation?

   **Answer** Lifetimes are $1/b = 1/c = 20/\ln 2 \approx 29\,\mathrm{min}$, so $P \approx 2(30 + 29 + 29) \approx 176\,\mathrm{min}$, about 3 h, of the order of the observed 2–3 h (the estimate is an upper scale, because an exponential lag acts faster than its full lifetime). A longer protein lifetime lengthens the period and, more importantly, filters the delayed feedback: the oscillation is damped. This was observed: mice with Hes7 stabilized by about 8 minutes show damped oscillations and fused somites (Hirata et al. 2004).

5. Derive the averaged equation $\dot A = \frac{\varepsilon}{8}A(4 - A^2)$ for the van der Pol oscillator and solve it. What does the averaging predict for the time needed to reach the limit cycle from $A = 0.1$ with $\varepsilon = 0.1$?

   **Answer** With $x = A\cos\theta$, $\dot x = -A\sin\theta$, the equation gives $\dot A = \varepsilon A\sin^2\theta(1 - A^2\cos^2\theta)$; averaging with $\langle\sin^2\theta\rangle = 1/2$ and $\langle\sin^2\theta\cos^2\theta\rangle = 1/8$ gives the result (Formula 23.4.1). Writing $u = A^2$: $\dot u = \frac{\varepsilon}{4}u(4 - u)$, a logistic equation, so $u = 4/(1 + C\mathrm{e}^{-\varepsilon t})$ and $A = 2/(1 + C\mathrm{e}^{-\varepsilon t})^{1/2}$. From $A = 0.1$, $C = 399$; $A$ reaches $1.9$ (95% of the limit) when $C\mathrm{e}^{-\varepsilon t} = 4/3.61 - 1 = 0.108$, at $t = \ln(399/0.108)/0.1 \approx 82$, about 13 periods.

6. Explain why **Notch pathway** mutants in zebrafish form the first few somites normally but posterior somites irregularly. Design an experiment to show that Notch signalling synchronizes the clocks rather than generating them.

   **Answer** At the start of somitogenesis the cells' clocks are started together (they share an initial phase), so the first somites form even without coupling; because the cells have slightly different frequencies and noise, they drift out of phase over several cycles, and only then do boundaries become irregular. Experiments: (i) apply DAPT for a limited time and wash it out: the position of the first defect depends on dose and timing, and normal somites resume after a delay that matches resynchronization (Riedel-Kruse et al. 2007); (ii) image a live reporter of *her1* in single cells of mutant embryos: individual cells still oscillate, with normal periods but random phases (salt-and-pepper); (iii) transplant **wild-type** cells out of phase into a wild-type host and follow their phase: they adopt the host phase, but not in a Notch-deficient host or if they themselves cannot receive Notch.

7. A forced van der Pol oscillator is driven with $\varepsilon = 0.1$, $\omega = 2$ and drive amplitude $K = 4$. Will its own oscillation survive? What amplitude of drive is needed to quench it?

   **Answer** $\gamma = K/(1 - \omega^2) = 4/(-3)$, $\gamma^2 = 1.78 < 2$, so the free oscillation survives with amplitude $a = 2(1 - 0.89)^{1/2} \approx 0.67$, superposed on the forced oscillation of amplitude $1.33$. Quenching requires $\gamma^2 > 2$, that is $\lvert K\rvert > \sqrt2\,\lvert 1 - \omega^2\rvert = 4.24$.

8. Using Formula 23.7.1, a chick forms a somite of about $150\,\mu\mathrm{m}$ every 90 minutes. What is the speed of the front? A bead of FGF8 implanted beside the anterior PSM holds the front at a fixed position for 45 minutes. Predict the sizes of the somites that form in that region.

   **Answer** $v = S/P = 150\,\mu\mathrm{m}/90\,\mathrm{min} \approx 1.7\,\mu\mathrm{m\,min^{-1}}$, about $100\,\mu\mathrm{m\,h^{-1}}$. While the front stands still, cells cross it more slowly: during the clock cycle in which the front is held for half the cycle, only about half the usual length of tissue passes the front, so that somite is about $75\,\mu\mathrm{m}$, smaller. Afterwards the front, released, moves faster to catch up with its normal position relative to the tail bud, and a larger somite forms; the total number is unchanged and the pattern normal further posteriorly. This is what Dubrulle et al. (2001) observed: smaller somites next to FGF beads, larger after SU5402 treatment.

9. In the FGF–RA model (23.12) with $D = \gamma = \beta = 1$, $\alpha = 8$, how far does the front move if the source strength doubles? Why does the front sharpen when RA is present?

   **Answer** By Proposition 23.6.2, $x_0 \approx \sqrt{D/\gamma}\ln(\beta F_0)$, so doubling $F_0$ moves the front away from the tail bud (anteriorly, relative to the tail bud) by $\ln 2 \approx 0.69$ decay lengths; the numerical shift is the same (Figure B). Where RA is present it adds a degradation term $\alpha AF$, so beyond the front FGF decays with rate $\sqrt{(\alpha + \gamma)/D} = 3$ instead of 1; and RA itself rises from 0 to 1 over a distance of order $\sqrt{D/(\alpha + \gamma)} = 1/3$. Mutual inhibition converts two shallow gradients into a step.

10. In Turing's example (Example 23.8.1) with $\nu = 1$, what is the largest activator diffusion coefficient that still allows a pattern, and what wavelength appears at threshold?

    **Answer** The condition is $\varepsilon/\nu < 1/4$, so $\varepsilon < 0.25$. At threshold $k_c^2 = 1/(16\varepsilon) = 1/4$, $k_c = 0.5$, wavelength $2\pi/k_c \approx 12.6$ in the scaled units. Check with Theorem 12.3.1: $\nu f_a + \varepsilon g_h = 3/16 - 1/16 = 1/8$ and $2\sqrt{\varepsilon\nu\det J} = 2\sqrt{0.25/64} = 1/8$, equality.

11. Thoracic PSM is grafted into the cervical region of a younger chick embryo, and in a second experiment cervical PSM is grafted to the thoracic region. Predict the results, and explain what they reveal about when somite identity is specified. How would you test whether the identity depends on Hox expression?

    **Answer** Both grafts keep their original identity: thoracic PSM forms vertebrae with ribs in the neck, cervical PSM forms rib-less vertebrae in the thorax. Identity is therefore specified in the PSM (or earlier, as cells leave the tail bud) and is **cell-autonomous** once established. Tests: examine Hox expression in the graft (it keeps the donor code, for example *Hoxc6* in thoracic tissue); change the code by electroporating a posterior **Hox gene** (such as *Hoxa10*) into the PSM, or knocking down a Hox gene, and score the vertebral identity; the mouse results (Hoxa10 or Hoxb6 throughout the PSM, *Hoxc8* and *Hox10* paralogue knockouts) show that the code instructs identity.

12. (Open) Pairs of somites form in register on both sides of the axis. Suggest which features of the clock-and-wavefront system ensure left–right synchrony, and what goes wrong when retinoic acid signalling is lost.

    **Answer** The clocks on both sides are synchronized because they arise from the same tail bud **progenitors** and the waves start together in the tail bud; the fronts on the two sides are set by the same tail bud source of FGF and Wnt. Left–right asymmetric signals of the lateral plate (Nodal, [7.5.17](/7.5.17)) and FGF could shift the front on one side; retinoic acid buffers the PSM against them. In zebrafish, chick and mouse embryos deficient in RA (*Raldh2* mutants, or RA antagonists), somites form asymmetrically, with the left and right sides out of register, the shift depending on the left–right signalling (Vermot and Pourquié 2005; Kawakami et al. 2005). Thus RA does not only define the front but also protects symmetric segmentation from the left–right machinery.
