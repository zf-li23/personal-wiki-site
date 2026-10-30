---
title: Stem Cells, Embryo Models and Organoids
description: "Stem cells from the point of view of development and medicine. Cell lines from the blastocyst: naive and primed pluripotency, TSC, XEN, haploid ES cells; niches as they form in development; mesenchymal stromal cells; the stochastic dynamics of stem-cell fate: spleen colonies, the birth–death process and its generating function, the Galton–Watson process, extinction, limit laws, critical branching and neutral drift; cancer stem cells; blastoids, gastruloids and ETX embryos and the 14-day rule; organoids and organ reconstruction; cell therapy and its risks."
---

The **stem cell** of [7.3.24](/7.3.24) was defined by two properties, self-renewal and the ability to give rise to differentiated cells, and its potency, niche and molecular regulation were introduced there. This chapter takes the view of development and of medicine. Stem cells are made in the embryo, and the first pluripotent lines were derived from it: we start with the cell lines that can be grown from the blastocyst ([7.5.5](/7.5.5)) and with niches as they form in development. We then treat a question that the regeneration experiments of [7.5.35](/7.5.35) pose quantitatively, following Percus and Childress: is the fate of a stem cell decided by chance or by control? The answer requires the theory of branching processes, which also explains the neutral drift of clones in adult tissues and the critical leaving fraction of cortical progenitors ([7.5.19](/7.5.19)). The last sections turn to the newest models of development, embryo models and organoids, which build embryo- and organ-like structures from stem cells, and to cell therapy. Generating functions are introduced in [3.1.11](/3.1.11), Markov chains in [7.3.24](/7.3.24#sec-24.6.4), and the cancer biology to which cancer stem cells belong in [7.3.26](/7.3.26).

## 36.1. Stem Cells in Development

A stem cell can divide asymmetrically, giving one stem cell and one committed daughter, or symmetrically, giving two stem cells or two committed cells; a population can therefore self-renew even if no single division is asymmetric, as long as on average half the daughters remain stem cells ("population asymmetry"). Potency ranges from totipotent (the zygote and early blastomeres, which also make extraembryonic tissues) through pluripotent (the epiblast, all embryonic lineages including the germ line) and multipotent (hematopoietic stem cells) to unipotent (spermatogonial stem cells). In the embryo, pluripotency is a transient state lasting a few days; stem-cell lines capture such transient states and make them self-renewing in culture, and much of what is known about the states themselves comes from these lines. The properties that the clinical literature calls "stemness" are self-renewal, the capacity to differentiate into one or more cell types, and heterogeneity within a population of the same origin.

## 36.2. Cell Lines from the Blastocyst

### 36.2.1. Embryonic Stem Cells: Naive and Primed

**Embryonic stem cells** ([7.3.24](/7.3.24#sec-24.7.1)) were derived from the mouse inner cell mass in 1981 (Evans and Kaufman; Martin) and from human blastocysts in 1998 (Thomson). Injected into a host blastocyst, mouse ES cells contribute to all tissues of the resulting **chimera**, including the germ line, so that genetically modified ES cells give modified mice. Mouse ES cells grown in serum with the cytokine LIF (which activates STAT3) are heterogeneous; in defined medium with two inhibitors, of MEK (blocking FGF4–ERK signaling, which drives differentiation) and of GSK3 (stabilizing β-catenin, which relieves repression by TCF3), they are homogeneous and self-renew in a "ground state" (Ying and colleagues 2008). The epiblast changes after implantation, and cells derived from the post-implantation epiblast (epiblast stem cells, EpiSCs; Brons and colleagues, Tesar and colleagues 2007) are pluripotent in a different way.

**Definition 36.2.1 (Naive and Primed Pluripotency)** **Naive pluripotency** is the state of the pre-implantation epiblast and of mouse ES cells: self-renewal depends on LIF–STAT3 and is supported by MEK and GSK3 inhibition, both X chromosomes are active in female cells, DNA is globally hypomethylated, colonies are dome-shaped, and the cells contribute to chimeras after injection into a blastocyst. **Primed pluripotency** is the state of the post-implantation epiblast and of EpiSCs: self-renewal depends on FGF2 and Activin/Nodal, X inactivation has begun, the cells are poised for lineage specification, grow as flat colonies and rarely contribute to blastocyst chimeras (they integrate into post-implantation embryos instead).

Conventional human ES cells resemble primed mouse EpiSCs, in morphology, signaling and gene expression; naive human cells can be obtained with special media (combinations of LIF and inhibitors of MEK, PKC, ROCK and other kinases), and they can make trophoblast, which mouse naive cells cannot. The difference matters for embryo models (36.6), which require naive-like cells.

### 36.2.2. Extraembryonic Lines

The other two lineages of the late blastocyst give their own lines. Trophoblast stem cells (TSCs; Tanaka and colleagues 1998) are derived from the polar trophectoderm in FGF4 with heparin and fibroblast-conditioned medium (TGF-β and Activin); on FGF withdrawal they differentiate into giant cells and other trophoblast types, and in chimeras they contribute only to the placenta. Extraembryonic endoderm (XEN) stem cells (Kunath and colleagues 2005) come from the primitive endoderm and contribute to the parietal endoderm of the yolk sac. Human TSCs were derived in 2018 (Okae and colleagues). Together, ES, TS and XEN cells represent the three lineages of the blastocyst, the building blocks of embryo models.

![Stem-cell lines from the mouse blastocyst. Embryonic stem cells (naive, dome-shaped colonies) from the epiblast, trophoblast stem cells from the trophectoderm and XEN cells from the primitive endoderm; epiblast stem cells (primed, flat colonies) from the epiblast after implantation. Under each line: the culture conditions and what the cells contribute to after injection into a host blastocyst](./plots/blastocyst-lines.py)

### 36.2.3. Haploid ES Cells and Uniparental Mice

Mammals are diploid, and haploid embryos die; but haploid ES cells can be derived from haploid blastocysts and grown. Parthenogenetic haploid ES cells come from oocytes activated without fertilization (with strontium chloride, which completes the second meiotic division; Leeb and Wutz, Elling and colleagues 2011); androgenetic haploid ES cells come from oocytes whose nucleus is replaced by a sperm nucleus, or from zygotes whose female pronucleus is removed (Li Wei, Zhou Qi and colleagues; Yang Hui, Li Jinsong and colleagues 2012). Only lines with an X chromosome survive: a haploid genome with only a Y lacks essential X-linked genes. Haploid cells have one copy of each gene, so a single mutation has a visible phenotype and forward genetic screens are as easy as in yeast. Androgenetic haploid ES cells injected into an oocyte can replace a sperm ("artificial spermatids") and give semi-cloned mice; their efficiency is low because the paternal imprints ([7.4.18](/7.4.18)) are unstable in culture, and deleting the imprinting control regions of *H19* and *Gtl2* (the *H19*-DMR and IG-DMR) raised it greatly. With further imprint edits the same groups made mice with two mothers that were viable and fertile, and bipaternal mice that were born but died soon (Li and colleagues 2018); bipaternal mice reaching adulthood required correcting about twenty imprinted regions (Li and colleagues 2025). Imprinting is thus the main barrier to uniparental reproduction in mammals. Haploid lines readily become diploid in culture, and the proportion of abnormal cells is high, so they must be purified repeatedly by sorting for DNA content.

## 36.3. Niches in Development and the Adult

The **stem-cell niche** ([7.3.24](/7.3.24#sec-24.6.2)) is built during development, often from the same signals that pattern the embryo.

- *Drosophila* germline stem cells. At the tip of each ovariole, two or three germline stem cells are attached by E-cadherin to the cap cells of the somatic niche, which secrete the BMPs Dpp and Gbb; BMP signaling represses the differentiation gene *bag of marbles* (*bam*) in the adjacent cells only. A stem cell divides with its spindle perpendicular to the niche, so that one daughter stays and the other, one cell diameter away, escapes BMP, expresses *bam* and becomes a cystoblast (Xie and Spradling 1998, 2000). Emptied niches are refilled by division of the remaining stem cell, or even by dedifferentiation of cystoblasts: the niche, not the lineage, defines the stem cell.
- Mouse ventricular–subventricular zone. Adult neural stem cells (B1 cells) touch the ventricle with a primary cilium at the center of a pinwheel of ependymal cells and contact blood vessels with a basal process. They are set aside from embryonic radial glia between E13.5 and E15.5, become quiescent, and are reactivated in the adult to make olfactory bulb interneurons (Fuentealba and colleagues 2015): the adult niche preserves a slowed-down embryonic lineage ([7.5.19](/7.5.19)).
- Hematopoietic stem cells. HSCs are generated in the embryo from hemogenic endothelium of the dorsal aorta, colonize the fetal liver and, around birth, the bone marrow ([7.5.29](/7.5.29)). In the marrow they reside mostly next to sinusoidal blood vessels, maintained by stem cell factor (SCF, the KIT ligand) and CXCL12 from perivascular leptin-receptor-positive stromal cells and endothelial cells (Ding and Morrison 2012, 2013).
- Intestinal crypt: Lgr5 cells between Paneth cells, with Wnt from the subepithelial mesenchyme ([7.3.24](/7.3.24#sec-24.6.4)).

Adult stem cells differ from pluripotent lines in being restricted to the lineages of their tissue, usually quiescent or slowly cycling, and long-lived; they accumulate somatic mutations at a roughly constant rate of about 40 single-nucleotide substitutions per year in human colon, small intestine and liver stem cells (Blokzijl and colleagues 2016), which links them to cancer (36.5) and to aging ([7.5.37](/7.5.37)).

### 36.3.1. Mesenchymal Stromal Cells

"Mesenchymal stem cells" (MSCs) are fibroblast-like cells that grow out of bone marrow, adipose tissue, umbilical cord and many other tissues when they are plated. Because they are defined by culture rather than by function in vivo, the International Society for Cellular Therapy proposed minimal criteria (Dominici and colleagues 2006): adherence to plastic; expression of CD73, CD90 and CD105 and absence of CD45, CD34, CD14 or CD11b, CD79a or CD19 and HLA-DR; and differentiation in vitro into osteoblasts, adipocytes and chondrocytes. Few such cultures meet the criterion of a stem cell, self-renewal and multilineage differentiation of single cells in vivo, and the term mesenchymal stromal cell is now preferred. A rigorous in vivo counterpart exists for bone: skeletal stem cells, identified by lineage tracing and clonal transplantation, that make bone, cartilage and marrow stroma but not fat or muscle outside the skeleton (Chan and colleagues 2015). MSC preparations differ between donors (umbilical cord cells from different fetuses respond differently to the same signal) and between tissues. Most of their effects in repair are indirect: they secrete growth factors and immunomodulatory molecules or recruit immune cells, rather than differentiating into the tissue.

## 36.4. Stochastic Dynamics of Stem-Cell Fate

### 36.4.1. Spleen Colonies and *Hydra* Interstitial Cells

Till and McCulloch (1961) injected bone marrow cells into irradiated mice and found nodules in the spleen after about ten days, each a clone derived from one cell, containing several blood lineages: the first assay of hematopoietic stem cells (colony-forming units, spleen, CFU-S). To ask how the stem cells within a colony are regulated, Till, McCulloch and Siminovitch (1964) dissociated single colonies and reinjected the cells into secondary hosts, which measures the number of stem cells in each colony. The numbers were remarkably variable, many colonies containing no stem cells and a few containing very many. They compared the distribution with simulations in which each stem cell, independently of the others and of its surroundings, makes two stem cells with probability $p$ and two differentiated cells with probability $q = 1 - p$, and found good agreement: the stem-cell population appeared to be under purely stochastic control. A similar question was asked in *Hydra*, where the interstitial stem cells make neurons and nematocytes, the remaining cell types belonging to the separate epithelial lineages (David and MacWilliams 1978). Interstitial cells were seeded into aggregates of tissue whose own interstitial cells had been killed with nitrogen mustard, and the clones they formed were counted; along the body column the proportions of nerve cells, nematoblasts and interstitial cells imply a self-renewal probability between only 0.6 and 0.7.

In such assays only the stem cells of a clone are counted, so a division that yields two stem cells adds one stem cell (a "birth") and a division that yields two differentiated cells removes one (a "death"). Two models bracket the timing of divisions: constant rates (exponential waiting times) and a fixed cycle.

### 36.4.2. The Birth–Death Process

**Definition 36.4.1 (Birth–Death Process)** In the linear **birth–death process**, each of the $N$ stem cells present at time $t$ independently gives two stem cells at rate $p$ and two differentiated cells at rate $q$. The probability $P_N(t)$ of having $N$ stem cells obeys the master equation

$$
\dot P_N = p(N - 1)P_{N-1} + q(N + 1)P_{N+1} - (p + q)NP_N,\qquad P_N(0) = \delta_{N,1}.
\tag{36.1}
$$

**Theorem 36.4.1 (Solution by Generating Function)** For $p \ne q$, the generating function $Q(x, t) = \sum_{N\ge0}x^NP_N(t)$ is

$$
Q(x, t) = \frac{q\bigl(\mathrm{e}^{(p-q)t} - 1\bigr) - \bigl(q\,\mathrm{e}^{(p-q)t} - p\bigr)x}{\bigl(p\,\mathrm{e}^{(p-q)t} - q\bigr) - p\bigl(\mathrm{e}^{(p-q)t} - 1\bigr)x},
$$
so that, with $E = \mathrm{e}^{(p-q)t}$,

$$
P_0(t) = \frac{q(1 - E^{-1})}{p - qE^{-1}},\qquad
P_N(t) = \frac{(p - q)^2E}{p(E - 1)(pE - q)}\left(\frac{1 - E^{-1}}{1 - (q/p)E^{-1}}\right)^{N}\quad(N \ge 1),
$$
$$
\mathbb{E}[N(t)] = E,\qquad \operatorname{Var}(N(t)) = \frac{p + q}{p - q}\,E\,(E - 1).
$$

**Proof** Multiply (36.1) by $x^N$ and sum: since $\sum Nx^NP_N = x\,\partial_xQ$, the three terms give $px^2\partial_xQ + q\,\partial_xQ - (p + q)x\,\partial_xQ$, so

$$
\partial_tQ = (px - q)(x - 1)\,\partial_xQ,\qquad Q(x, 0) = x .
$$
This first-order equation says that $Q$ is constant along the characteristics $\mathrm{d}x/\mathrm{d}t = -(px - q)(x - 1)$. Equivalently $t$ as a function of $Q$ at fixed $x$ satisfies $(\partial t/\partial x)_Q = -1/\bigl((px - q)(x - 1)\bigr)$; integrating with partial fractions from $x = Q$ (where $t = 0$),

$$
t = \frac1{p - q}\Big(\ln\frac{1 - x}{q - px} - \ln\frac{1 - Q}{q - pQ}\Big),
$$
which solved for $Q$ gives the formula. Expanding in powers of $x$ gives $P_0$ (the value at $x = 0$) and a geometric series for $N \ge 1$. The moments follow from $\mathbb{E}[N] = \partial_xQ(1, t)$ and $\mathbb{E}[N(N - 1)] = \partial_x^2Q(1, t)$, or more quickly from the moment equations: differentiating (36.1) gives $\frac{\mathrm{d}}{\mathrm{d}t}\mathbb{E}[N] = (p - q)\mathbb{E}[N]$ and $\frac{\mathrm{d}}{\mathrm{d}t}\mathbb{E}[N^2] = 2(p - q)\mathbb{E}[N^2] + (p + q)\mathbb{E}[N]$, whose solutions with $N(0) = 1$ are $E$ and $E^2 + \frac{p+q}{p-q}E(E - 1)$. $\square$

**Corollary 36.4.1 (Extinction and the Limit Law)** For $p > q$:

1. The *extinction probability* is $P_0(\infty) = q/p$: a clone dies out with probability $q/p$ even though its mean grows exponentially. The probabilities $P_N(\infty)$ of each finite size $N \ge 1$ tend to 0, while $\sum_{N\ge1}P_N(\infty) = 1 - q/p$: surviving clones grow without bound.
2. In the scaled variable $w = N/\mathbb{E}[N(t)]$, the distribution tends to

$$
P(w) = \frac qp\,\delta(w) + \Big(1 - \frac qp\Big)^2\mathrm{e}^{-(1 - q/p)w},
$$
an atom at zero (the extinct clones) and an exponential law for the survivors.
3. The ratio $r^2 = \operatorname{Var}(N)/\bigl(\mathbb{E}[N](\mathbb{E}[N] - 1)\bigr) = (p + q)/(p - q)$ is constant in time and measurable from a single sample of clones, and in terms of it

$$
P(w) = \frac{r^2 - 1}{r^2 + 1}\,\delta(w) + \Big(\frac2{1 + r^2}\Big)^2\mathrm{e}^{-2w/(1 + r^2)} .
$$

**Proof** (1) As $t \to \infty$, $E \to \infty$ and $P_0 \to q/p$, while $P_N \sim (p-q)^2/(p^2E)\,(1 - (p - q)/(pE))^N \to 0$ for each fixed $N$. (2) With $N = wE$, $\bigl(1 - (p - q)/(pE)\bigr)^{wE} \to \mathrm{e}^{-(1 - q/p)w}$ and $E\,P_{wE} \to (1 - q/p)^2\mathrm{e}^{-(1 - q/p)w}$; the atom is the limit of $P_0$. (3) Theorem 36.4.1 gives $r^2$ directly, and $1 - q/p = 2(p - q)/(2p) = 2/(1 + r^2)$ since $1 + r^2 = 2p/(p - q)$. $\square$

The scaled law depends on one combination of parameters, and this is what Till and colleagues could test: experimental, simulated and theoretical cumulative distributions agreed closely. Their conclusion, that hematopoietic stem cells decide stochastically, was influential, though Percus and Childress note that the extinct clones (which give no spleen colonies) may not have been properly accounted for. The model itself is not realistic in one respect: with constant rates, the probability density of the first division at time $T$ is $\rho(T) = p\,\mathrm{e}^{-pT}$, so the most likely time to divide is immediately after the previous division, whereas real cells need a minimum time to complete the cycle.

![Stem-cell clones in the birth-death process (p = 1, q = 0.4, time in units of 1/p). A: distribution of the number of stem cells at t = 4: exact formula of Theorem 36.4.1 (bars) and 20 000 Gillespie simulations (points); 38 % of clones are already extinct, and the rest are spread geometrically. B: the survival probability falls towards 1 - q/p = 0.6 (point: simulation at t = 4). C: at t = 8 the sizes of surviving clones, divided by the mean size, follow the exponential limit law of Corollary 36.4.1](./plots/birth-death-clones.py)

The simulations use the **Gillespie algorithm**: in each step the waiting time to the next event is drawn from an exponential distribution with rate $(p + q)N$, and the event is a birth with probability $p/(p + q)$ ([4.4.7](/4.4.7)).

### 36.4.3. Fixed Cycles: The Galton–Watson Process

The opposite extreme is a fixed cycle length, taken as the unit of time: at the end of each generation every stem cell gives either two stem cells (probability $p$) or two differentiated cells ($q = 1 - p$). More generally a stem cell may leave $k$ stem-cell descendants after one period with probability $p_k$. This is the oldest branching process, introduced by Galton and Watson (1874) to explain the extinction of family names carried by sons.

**Definition 36.4.2 (Galton–Watson Process)** A **Galton–Watson process** is a sequence of population sizes $Z_0 = 1, Z_1, Z_2, \dots$ in which each individual of generation $n$, independently, leaves $k$ individuals in generation $n + 1$ with probability $p_k$. Its offspring generating function is $f(x) = \sum_kp_kx^k = \mathbb{E}[x^{Z_1}]$, with mean $m = f'(1)$ and second factorial moment $Q = f''(1)$. For the stem-cell model, $f(x) = q + px^2$, $m = 2p$, $Q = 2p$. A **branching process** in general is a stochastic process in which individuals reproduce independently according to the same law; Definition 36.4.1 is its continuous-time version.

In the chemical-kinetics notation of reactions per generation, $S \xrightarrow{p} 2S$ and $S \xrightarrow{q} 2E$ suggest the deterministic law $\dot S = (p - q)S$: growth, decay or steady state according as $p >, <, = q$. The fluctuations that this law ignores dominate when the population is small, as it is at the start of every clone. Give each stem cell a tag $x$: a population of $N$ stem cells is weighted $x^N$, and one generation replaces each $x$ by $f(x)$.

**Theorem 36.4.2 (Iteration of the Generating Function)** The generating function of $Z_n$ is the $n$-fold iterate, $f_n(x) = \mathbb{E}[x^{Z_n}] = f(f(\cdots f(x)\cdots))$, with $f_{a+b} = f_a \circ f_b$. Its moments are

$$
\mathbb{E}[Z_n] = m^n,\qquad f_n''(1) = \mathbb{E}[Z_n(Z_n - 1)] = Q\,m^{n-1}\frac{m^n - 1}{m - 1}\quad(m \ne 1),
$$
and for $f = q + px^2$ the relative standard deviation is

$$
\frac{\sqrt{\operatorname{Var}(Z_n)}}{\mathbb{E}[Z_n]} = \Big(\frac{2 - m}{m - 1}\Big)^{1/2}\bigl(1 - m^{-n}\bigr)^{1/2} \to \Big(\frac{2 - m}{m - 1}\Big)^{1/2}.
$$

**Proof** Conditional on $Z_n = N$, $Z_{n+1}$ is a sum of $N$ independent copies of $Z_1$, so $\mathbb{E}[x^{Z_{n+1}} \mid Z_n] = f(x)^{Z_n}$ and $f_{n+1}(x) = f_n(f(x))$ (a random sum, [3.1.11](/3.1.11#sec-11.1.2)); hence $f_n$ is the iterate. Differentiating $f_{n+1} = f \circ f_n$ at $x = 1$, where $f_n(1) = 1$: $f_{n+1}'(1) = f'(1)f_n'(1) = m\,f_n'(1)$, so $f_n'(1) = m^n$; and $f_{n+1}''(1) = f''(1)f_n'(1)^2 + f'(1)f_n''(1) = Qm^{2n} + mf_n''(1)$, a linear recursion with $f_0'' = 0$ whose solution is the formula. For $f = q + px^2$, $Q = m$, so $\operatorname{Var}(Z_n) = f_n'' + f_n' - f_n'^2 = m^n(m^n - 1)\bigl(\frac1{m-1} - 1\bigr)$; dividing by $m^{2n}$ gives the result. $\square$

The variance ratio $\operatorname{Var}(Z_n)/\bigl(\mathbb{E}[Z_n](\mathbb{E}[Z_n] - 1)\bigr) = (2 - m)/(m - 1)$ is again constant in time, the counterpart of $r^2$ in Corollary 36.4.1.

**Theorem 36.4.3 (Extinction Probability)** The probability $P_0(n) = f_n(0)$ that the clone is extinct by generation $n$ obeys $P_0(n + 1) = f(P_0(n))$, $P_0(0) = 0$, and increases to the smallest fixed point of $f$ in $[0, 1]$. If $m \le 1$ (and $p_1 < 1$) this fixed point is 1 and extinction is certain; if $m > 1$ it is a root $x^* < 1$. For $f = q + px^2$ with $p > \tfrac12$, $x^* = q/p$. A fixed point $x_0$ is stable if $\lvert f'(x_0)\rvert < 1$ and unstable if $\lvert f'(x_0)\rvert > 1$; here $f'(1) = 2p > 1$ (unstable) and $f'(q/p) = 2q < 1$ (stable).

**Proof** $P_0(n + 1) = f_{n+1}(0) = f(f_n(0))$. Since $f$ is increasing on $[0, 1]$ and $P_0(1) = f(0) \ge 0 = P_0(0)$, induction gives an increasing sequence bounded by any fixed point $x^*$ (if $P_0(n) \le x^*$ then $P_0(n + 1) = f(P_0(n)) \le f(x^*) = x^*$); it converges to a fixed point, hence to the smallest. $f$ is convex with $f(1) = 1$; if $f'(1) = m \le 1$, then $f(x) > x$ on $[0, 1)$ (strict convexity when $p_k > 0$ for some $k \ge 2$), so 1 is the only fixed point; if $m > 1$, $f(x) < x$ just below 1 and $f(0) \ge 0$, so there is a fixed point in $[0, 1)$. For $f = q + px^2$, $px^2 - x + q = (px - q)(x - 1) = 0$ gives $x = 1$ and $q/p$. Near a fixed point, $\Delta_{n+1} = f'(x_0)\Delta_n + \cdots$, which gives the stability criterion; and directly, $q/p - P_0(n + 1) = p\bigl(q/p + P_0(n)\bigr)\bigl(q/p - P_0(n)\bigr) < 2q\bigl(q/p - P_0(n)\bigr)$, a geometric approach with ratio below $2q < 1$. $\square$

![Extinction in the Galton-Watson process with f(x) = q + p x^2. A-C: cobweb diagrams of P0(t + 1) = f(P0(t)) from P0(0) = 0: for p = 0.4 (m = 0.8) and p = 0.5 (m = 1) the iteration climbs to the fixed point 1, extinction is certain; for p = 0.6 (m = 1.2) it stops at the stable fixed point q/p = 2/3. D: the probability of extinction by generation t; in the critical case it approaches 1 only as 1 - 2/t](./plots/galton-watson.py)

The extinction probability is the same as in the birth–death model, $q/p$; the two models differ in their finite-time distributions, but, remarkably, hardly in their scaled limit. For the full distribution one needs $f_n$, which is rarely available in closed form. Its scaled limit satisfies a functional equation.

**Theorem 36.4.4 (Limit Laws)** Let $\sigma^2 = \operatorname{Var}(Z_1)$.

1. Subcritical ($m < 1$): the population dies out, and the conditional distribution $\mathbb{P}(Z_n = k \mid Z_n > 0)$ converges to a limit law (Yaglom).
2. Critical ($m = 1$, $0 < \sigma^2 < \infty$): $\mathbb{P}(Z_n > 0) \sim 2/(\sigma^2n)$, $\mathbb{E}[Z_n \mid Z_n > 0] \sim \sigma^2n/2$, and $\mathbb{P}\bigl(Z_n/n > z \mid Z_n > 0\bigr) \to \mathrm{e}^{-2z/\sigma^2}$; equivalently $\frac1n\Big(\frac1{1 - f_n(x)} - \frac1{1 - x}\Big) \to \frac{\sigma^2}2$ for $x \in [0, 1)$.
3. Supercritical ($m > 1$, $\sigma^2 < \infty$): $W_n = Z_n/m^n$ converges to a random variable $W$ with $\mathbb{P}(W = 0) = x^*$ and $\mathbb{E}[W] = 1$, whose Laplace transform $\varphi(s) = \mathbb{E}[\mathrm{e}^{-sW}]$ is the solution of

$$
\varphi(ms) = f\bigl(\varphi(s)\bigr),\qquad \varphi(0) = 1,\quad \varphi'(0) = -1 .
$$
For $0 \le x < 1$, $f_n(x) \to x^*$, and if $\gamma = f'(x^*) > 0$ the approach is geometric: $\bigl(f_n(x) - x^*\bigr)/\gamma^n$ converges to a nonzero limit.

**Proof** We prove the functional equation and the critical law, the parts used below. (3) $\varphi_n(s) = \mathbb{E}[\mathrm{e}^{-sZ_n/m^n}] = f_n(\mathrm{e}^{-s/m^n})$, so $\varphi_{n+1}(ms) = f_{n+1}(\mathrm{e}^{-s/m^n}) = f(\varphi_n(s))$; the convergence of $W_n$ (a martingale bounded in $L^2$ when $\sigma^2 < \infty$) lets us pass to the limit. The normalization follows from $\mathbb{E}[W] = 1$. (2) Write $f(x) = 1 - (1 - x) + \frac{\sigma^2}2(1 - x)^2 + o\bigl((1 - x)^2\bigr)$ (using $f'(1) = 1$, $f''(1) = \sigma^2$). With $y_n = 1 - f_n(x) \to 0$, $y_{n+1} = y_n - \frac{\sigma^2}2y_n^2 + o(y_n^2)$, so $\frac1{y_{n+1}} - \frac1{y_n} \to \frac{\sigma^2}2$ and, by averaging (Cesàro), $\frac1{ny_n} \to \frac{\sigma^2}2$. At $x = 0$ this gives $\mathbb{P}(Z_n > 0) = y_n \sim 2/(\sigma^2 n)$. The conditional generating function of $Z_n/n$ follows by applying the same limit with $x = \mathrm{e}^{-s/n}$, which gives $\mathbb{E}[\mathrm{e}^{-sZ_n/n} \mid Z_n > 0] \to 1/(1 + \sigma^2s/2)$, the Laplace transform of an exponential with mean $\sigma^2/2$. $\square$

If $\varphi$ is known, so is its inverse, and $f = \varphi \circ m \circ \varphi^{-1}$, a nonlinear similarity transformation; then $f_n(x) = \varphi\bigl(m^n\varphi^{-1}(x)\bigr)$, explicit for every $n$. Exactly solvable cases are rare:

- $f(x) = 2x^2 - 1 = \cos(2\arccos x)$ iterates to $f_n(x) = \cos(2^n\arccos x)$, but its "probabilities" are not all nonnegative, so it is not a branching process.
- The linear fractional (modified geometric) law, $f(x) - 1 = \dfrac{m(x - 1)}{1 - \frac{Q}{2m}(x - 1)}$, has $f(1) = 1$, $f'(1) = m$, $f''(1) = Q$ and corresponds to $p_k \propto \big(\tfrac{Q}{Q+2m}\big)^k$ for $k \ge 1$. Since compositions of linear fractional maps are linear fractional, with $F(X) = \alpha X/(1 - \beta X)$ giving $F_n(X) = \alpha^nX/\bigl(1 - \beta\frac{\alpha^n - 1}{\alpha - 1}X\bigr)$,

$$
f_n(x) = 1 + \frac{m^n(x - 1)}{1 - \frac Q{2m}\frac{m^n - 1}{m - 1}(x - 1)} .
$$
In continuous time the birth–death process has exactly such a generating function (Theorem 36.4.1); its scaled limit is the Poisson-like law of Corollary 36.4.1, $\varphi(s) = (p - q + qs)/(p - q + ps)$.

**Example 36.4.1 (A Linear Fractional Approximation)** For $f = q + px^2$, write $f(x) - 1 = m(x - 1) + p(x - 1)^2 = m(x - 1)\bigl(1 + \frac12(x - 1)\bigr) \approx \dfrac{m(x - 1)}{1 - \frac12(x - 1)}$, which is the linear fractional law with $Q = m$. Iterating it gives $f_n(x) \approx 1 + m^n(x - 1)\big/\bigl(1 - \frac12\frac{m^n - 1}{m - 1}(x - 1)\bigr)$. This approximation reproduces $f_n(1)$, $f_n'(1)$ and $f_n''(1)$ exactly; it gives $P_0(\infty) \approx 3 - 2m = 1 - 4\varepsilon$ for $p = \frac12 + \varepsilon$, against the exact $q/p = (1 - 2\varepsilon)/(1 + 2\varepsilon) = 1 - 4\varepsilon + O(\varepsilon^2)$; and for large $n$, $P_N \approx \frac{4(m-1)^2}{m^n}\mathrm{e}^{-2(m-1)N/m^n}$. In terms of $r^2 = (2 - m)/(m - 1)$ and $w = N/m^n$, this is

$$
P(w) \approx \frac{r^2 - 1}{r^2 + 1}\,\delta(w) + \Big(\frac2{1 + r^2}\Big)^2\mathrm{e}^{-2w/(1 + r^2)},
$$
the same function of $r^2$ as in Corollary 36.4.1. The fixed-cycle and constant-rate models therefore predict nearly the same scaled distribution of clone sizes once each is expressed through its measured mean and variance, and Monte Carlo simulations of both, and the spleen-colony data, gave almost the same cumulative curves. The shape of the clone-size distribution does not discriminate between models of cycle timing; it tests only the assumption of independent, random fate decisions.

**Proposition 36.4.1 (Expansion Near Criticality)** Let $r = m - 1$ be small and write $f(x) = x + rU(x)$, so that $U(1) = 0$ and $U'(1) = 1$. The inverse $S = \varphi^{-1}$ satisfies $S(f(\varphi)) = (1 + r)S(\varphi)$, and to first order in $r$

$$
S(\varphi) = -U(\varphi)\exp\Big(\int_1^{\varphi}\frac{1 - U'(u)}{U(u)}\,\mathrm{d}u\Big)\bigl(1 + O(r)\bigr).
$$
For $f = q + px^2$ ($r = p - q$, $U = (px - q)(x - 1)/r$), including the first correction,

$$
S(\varphi) = \frac{r(1 - \varphi)}{p\varphi - q}\Big(1 + r\ln\frac{p\varphi - q}{r}\Big) + O(r^3),\qquad
\varphi(s) = \frac qp + \frac rp\,\frac r{r + ps} + \frac{r^3s}{(r + ps)^2}\ln\frac r{r + ps} + \cdots .
$$

**Proof** Expanding $S(\varphi + rU) = S + rUS' + \frac12r^2U^2S'' + \cdots = (1 + r)S$ gives $US' + \frac r2U^2S'' + \cdots = S$. At leading order $US_0' = S_0$, so $S_0 = C\exp\int\mathrm{d}u/U$; using $\int\frac{\mathrm{d}u}U = \ln\lvert U\rvert + \int\frac{1 - U'}U\,\mathrm{d}u$ and the normalization $S \approx 1 - \varphi$ near $\varphi = 1$ gives the general formula. For the example, $1/U = 1/(\varphi - 1) - p/(p\varphi - q)$ (partial fractions with $p - q = r$), so $S_0 = r(1 - \varphi)/(p\varphi - q)$, which is the linear fractional approximation. Writing $S = S_0(1 + rw)$, the terms of order $r$ give $US_0w' = -\frac12U^2S_0''$, i.e. $w' = -\frac12US_0''/S_0 = p/(p\varphi - q)$, so $w = \ln\bigl((p\varphi - q)/r\bigr)$, which vanishes at $\varphi = 1$ as the normalization requires. Inverting to first order in the correction gives $\varphi(s)$. $\square$

**Remark 36.4.1** The correction is small: for $p = 0.55$ ($r = 0.1$) and $s = 1$ it changes $\varphi$ from 0.8462 (linear fractional) to 0.8417, against 0.8420 from iterating $f$ numerically; for $p = 0.75$ ($r = 0.5$) the values are 0.600, 0.527 and 0.536. In Percus and Childress the correction appears without the factor $r$ in front of the logarithm (and correspondingly with $r^2$ instead of $r^3$ in $\varphi$), which overstates it by a factor $1/r$; the derivation above and the numerical check fix the coefficient. The same book states the birth–death variance as $E(E - 1)/(p - q)$, which holds only if time is measured so that $p + q = 1$; the general factor is $(p + q)/(p - q)$, and the delta-function weight in the $r^2$ form must read $(r^2 - 1)/(r^2 + 1)$, so that it equals $q/p$.

### 36.4.4. Criticality, Homeostasis and Neutral Drift

An adult tissue in steady state must keep its stem-cell number constant, so on average half the daughters of stem-cell divisions must remain stem cells: $m = 1$. The stem-cell pool of a homeostatic tissue is a critical branching process, and Theorem 36.4.4(2) has striking consequences. The number of labeled stem cells summed over all clones stays constant, but individual clones are lost at a rate that makes the surviving fraction fall as $2/(\sigma^2n)$, while the surviving clones grow linearly, with mean size $\sigma^2n/2$, and their sizes, scaled by the mean, become exponentially distributed. Lineage tracing in mouse tail epidermis found exactly these signatures: the number of labeled clones fell, the mean size of the surviving ones grew linearly with time, and their scaled size distribution was exponential (Clayton and colleagues 2007), consistent with a single progenitor population whose divisions give two progenitors, one of each kind, or two differentiating cells with probabilities $r$, $1 - 2r$, $r$ (with $r \approx 0.08$). In intestinal crypts the stem-cell pool is spatially confined, and the same critical dynamics on a ring of about 16 cells give **neutral drift** ([7.3.24](/7.3.24#sec-24.6.4)) to monoclonality. The cortical progenitors of [7.5.19](/7.5.19) illustrate the other two regimes: a pool that expands while the fraction leaving the cycle is below one half, and exhausts itself once it is above.

![Clones in a critical branching process (each division gives two stem cells or two differentiated cells with probability 1/2; 200 000 simulated clones). A: the fraction of clones that still contain stem cells falls as 2/t. B: the mean size of surviving clones grows linearly, as t/2, although the mean over all clones stays 1. C: at t = 50 the sizes of surviving clones scaled by their mean are exponentially distributed (Theorem 36.4.4(2)); these are the signatures of neutral competition among equivalent stem cells](./plots/critical-clones.py)

**Example 36.4.2 (Stochastic or Controlled?)** Pure stochasticity with $m$ exactly 1 is unstable: any deviation of $p$ from $\frac12$ makes the pool grow or decay exponentially, and fluctuations in a small pool drive it to extinction in a time of order its size. Homeostasis therefore needs feedback: the probability of self-renewal must fall when the pool is large and rise when it is small, for example $p(N) = \frac12 + \kappa(1 - N/K)$. The mean-field equation $\dot N = (2p(N) - 1)\nu N = 2\kappa\nu N(1 - N/K)$ (with division rate $\nu$) then has a stable steady state at $N = K$, around which the pool fluctuates with variance of order $K/\kappa$, and each clone still drifts neutrally within it. In *Hydra*, David and MacWilliams (1978) found that the self-renewal probability of interstitial cells depends on their local density, not on a global feedback from the whole animal: control is real, but local. The conclusions of the spleen-colony experiments and of *Hydra* are reconciled by this picture: fate decisions are random at the level of each division, and their probability is regulated by the niche.

## 36.5. Cancer Stem Cells

**Definition 36.5.1 (Cancer Stem Cell)** A **cancer stem cell** is a cell within a tumor that can self-renew and regenerate the heterogeneity of the tumor, operationally one that can initiate a tumor on transplantation (usually into immunodeficient mice) when other cells of the same tumor cannot.

In acute myeloid leukemia, only a rare CD34⁺CD38⁻ fraction initiated leukemia in immunodeficient mice (Bonnet and Dick 1997), and similar hierarchies were reported in breast, brain and colon cancers. The concept matters for therapy: conventional chemotherapy and radiotherapy kill dividing cells, and slowly cycling cancer stem cells with active drug efflux and DNA repair may survive and regrow the tumor. In the language of 36.4, a treatment succeeds only if it drives the clonogenic population to extinction, and the extinction probability is very sensitive to the surviving fraction of such cells. Three caveats limit the concept. The frequency of tumor-initiating cells depends on the assay: in more permissive, more immunodeficient mice about one in four human melanoma cells formed tumors (Quintana and colleagues 2008), so for some cancers "stemness" is common. Cancer cells are plastic, and non-stem cells can reacquire stem properties (dedifferentiation), especially under therapy. And drugs aimed at stem-cell pathways (Wnt, Notch, Hedgehog) risk damaging the normal stem cells that use the same pathways, such as those of the gut, skin and blood.

## 36.6. Embryo Models

Stem cells placed in the right conditions organize themselves into structures resembling embryos, an approach that complements the study of embryos and overcomes the scarcity of human embryos at the stages when many pregnancies fail.

**Definition 36.6.1 (Stem-Cell-Based Embryo Model)** A **stem-cell-based embryo model** (embryoid) is a structure assembled in vitro from one or more kinds of stem cells, cultured with appropriate signals, that self-organizes to reproduce the cell types and spatial organization of an embryo at a particular stage. A **blastoid** models the blastocyst, a **gastruloid** models gastrulation and axis formation, and a neuruloid models neurulation; integrated models (ETX embryos, SEMs) contain both embryonic and extraembryonic lineages and model the whole conceptus.

An older term, the embryoid body, denotes an aggregate of ES cells that differentiates into derivatives of the three germ layers without organized structure; the models below are organized.

- Gastruloids. About 300 mouse ES cells aggregated in a U-shaped well and given a pulse of the Wnt agonist CHIR99021 break symmetry, express Brachyury at one end and elongate over five days into a structure with an anteroposterior axis, a posterior "tail bud", colinear Hox gene activation along the axis ([7.5.15](/7.5.15)) and derivatives of the three germ layers, but no brain and no extraembryonic tissues (van den Brink and colleagues 2014; Beccari and colleagues 2018). Embedded in a low concentration of Matrigel they form somites with a segmentation clock ([7.5.23](/7.5.23)) and a neural tube. Human gastruloids make somites with the human clock period of about 5 h.
- Micropatterned colonies. Human ES cells confined to discs about 500 µm across and given BMP4 form concentric rings, from the center ectoderm, mesoderm, endoderm and an outer trophectoderm-like ring (Warmflash and colleagues 2014): the edge of the colony, where receptors are accessible and inhibitors (Noggin) are lost, sets up a gradient of BMP activity, a direct test of positional information ([7.5.11](/7.5.11)).
- Blastoids. Mouse ES cells combined with trophoblast stem cells in microwells form blastocyst-like cysts (Rivron and colleagues 2018); naive human pluripotent cells alone, which can make trophoblast, form human blastoids that can attach to endometrial cells (Liu, Yu, Kagawa and colleagues 2021–2022).
- ETX embryos and SEMs. Mouse ES cells assembled with TSCs and with XEN cells (or with ES cells induced to express *Gata4*, which make visceral endoderm) form egg-cylinder-like structures that gastrulate and develop to about E8.5, with neural folds, somites, a gut tube and a beating heart (Sozen and colleagues 2018; Amadei and colleagues, Tarazi and colleagues 2022). Human models of the post-implantation conceptus with amnion, yolk sac and trophoblast-like cells have been made from naive or genetically induced pluripotent cells (2023).
- Non-human primates. Cynomolgus monkey embryos have been cultured beyond implantation to about day 20, through gastrulation and early neurulation (Niu, Ma and colleagues 2019; Zhai, Gong and colleagues 2023), and monkey blastoids transferred to surrogate mothers initiated pregnancies that were soon lost (Li and colleagues 2023).

![Stem-cell-based embryo models and the stages they mimic. Top: developmental time line (mouse embryonic day / human day) with the 14-day limit on culturing human embryos. A: blastoid from ES and trophoblast stem cells. B: gastruloid from about 300 ES cells after a Wnt pulse: an elongated axis with Brachyury-positive posterior end, somite-like blocks (red) and a gut-like tube (yellow). C: an ETX/SEM embryo from ES, trophoblast stem and extraembryonic endoderm cells: an egg-cylinder-like structure that develops to neural folds and a heart tube. D: a micropatterned human ES-cell colony treated with BMP4 forms rings of ectoderm, mesoderm, endoderm and trophectoderm-like cells](./plots/embryo-models.py)

The models are not embryos. They are inefficient (often only a few percent of aggregates form correct structures), lack some parts (gastruloids have no anterior brain and no extraembryonic tissues), do not develop beyond early organogenesis, and none has developed to term. Their value is experimental: they can be made in large numbers, imaged, manipulated genetically and mechanically, and they separate what cells can do by themselves from what needs the extraembryonic tissues or the mother.

**Remark 36.6.1 (The 14-Day Rule)** Many countries forbid culturing human embryos beyond 14 days after fertilization or the appearance of the primitive streak, whichever is earlier, following the Warnock report (1984): after this point twinning is no longer possible and the embryo is an individual, and the first structure of the nervous system is about to form. Until 2016 the limit was hypothetical, because embryos could not be grown so long. The International Society for Stem Cell Research guidelines (2021) dropped the 14-day rule as an absolute limit, asking for case-by-case review of proposals to go further, and their update of 2025 brought all stem-cell-based embryo models under oversight and stated that they must not be transferred to a uterus or grown to the point of viability. The ethical status of models that become ever more complete is unresolved: if a model could develop like an embryo, the grounds for treating it differently would disappear.

## 36.7. Organoids and Organ Reconstruction

The **organoid** ([7.3.24](/7.3.24#sec-24.6.6)) is the organ-level counterpart of an embryo model: a three-dimensional structure grown from adult tissue stem cells or pluripotent cells that self-organizes into several cell types of an organ with some of its function. Adult-stem-cell organoids (intestine, stomach, liver, pancreas, lung, prostate, many tumors) start from one Lgr5-like cell and are mostly epithelial; pluripotent-cell organoids (brain, retina, kidney, inner ear) recapitulate developmental steps and contain several tissues. Their self-organization reproduces development: an aggregate of mouse ES cells forms an optic vesicle that invaginates into a two-layered optic cup by itself (Eiraku and colleagues 2011).

**Example 36.7.1 (A Kidney from Two Populations)** The metanephric kidney forms by reciprocal induction between the ureteric bud and the metanephric mesenchyme, which come from different parts of the intermediate mesoderm ([7.5.25](/7.5.25)). Takasato and colleagues (2014, 2015) differentiated human pluripotent cells first to primitive streak (with the Wnt agonist CHIR99021) and then to intermediate mesoderm (with FGF9). A short Wnt pulse gave mainly anterior intermediate mesoderm, the source of the ureteric epithelium; a long one gave posterior intermediate mesoderm, the source of the nephron progenitors. Dissociating and reaggregating a mixture of both produced kidney organoids with collecting-duct epithelium, nephrons segmented into glomeruli, proximal and distal tubules, and interstitium and endothelium. The design applied the developmental fate map: the timing of one signal decided which of two neighboring progenitor populations was made.

Organoids are used to model diseases (cystic fibrosis, microcephaly, Zika infection, polycystic kidney disease), to test drugs on a patient's own cells, for toxicology, and as a source of tissue for transplantation in the future. Their limitations are those of the models above: they contain fewer cell types than the organ, lack vasculature, nerves and immune cells, remain fetal in maturity, vary from batch to batch, and culture conditions change cell properties. Assembloids that combine organoids of different brain regions, co-culture with endothelial cells, and transplantation into animals, where host vessels invade, address some of these.

Whole organs need a scaffold. Perfusing an organ with detergent (sodium dodecyl sulfate) removes all cells and leaves the extracellular matrix with its vascular channels; reseeded with cells, decellularized rat hearts contracted (Ott and colleagues 2008), and decellularized rat livers reseeded with hepatocytes and transplanted performed some liver functions for hours (Uygun and colleagues 2010). The alternative sources are other species. Pigs with gene edits that remove carbohydrate antigens recognized by human antibodies, add human complement and coagulation regulators and inactivate porcine endogenous retroviruses have provided hearts and kidneys transplanted into patients since 2022, some functioning for months. Interspecies chimeras could grow human organs in animals: rat pancreas was grown in mice lacking *Pdx1* by injecting rat ES cells into mouse blastocysts (blastocyst complementation; Kobayashi and colleagues 2010), but human cells contribute very little to pig or monkey embryos (Wu and colleagues 2017; Tan and colleagues 2021), and such chimeras raise ethical questions about human cells in the brain or germ line of animals.

## 36.8. Cell Therapy and Its Risks

The one long-established stem-cell therapy is hematopoietic stem-cell transplantation, practiced since the 1950s–1960s for leukemias, immunodeficiencies and marrow failure. Epidermal and limbal stem cells cultured as sheets restore skin and corneal surface (the limbal product Holoclar was approved in the European Union in 2015; for epidermis see [7.3.24](/7.3.24#sec-24.6.5)). Products based on mesenchymal stromal cells have been approved in several countries: Hearticellgram-AMI (bone-marrow MSCs for acute myocardial infarction, South Korea 2011), Prochymal (remestemcel-L, for steroid-refractory graft-versus-host disease in children, Canada 2012), Temcell (Japan 2015), Alofisel (adipose MSCs for perianal fistulas in Crohn's disease, European Union 2018, withdrawn in 2024 after a confirmatory trial failed) and Ryoncil (remestemcel-L, United States 2024, for pediatric steroid-refractory acute graft-versus-host disease). Their efficacy for other indications, such as Crohn's disease, diabetes or heart disease, has generally not been demonstrated. Pluripotent-cell derivatives are in clinical trials: retinal pigment epithelium from iPS cells for macular degeneration (Takahashi and colleagues from 2014), dopaminergic neuron progenitors from ES or iPS cells for Parkinson's disease, which survived, produced dopamine and caused no tumors in phase 1/2 trials (2025), and islets from chemically induced pluripotent cells that made a patient with type 1 diabetes insulin-independent (Wang and colleagues 2024).

| Risk | Origin | Example or safeguard |
|---|---|---|
| Tumor formation | residual undifferentiated pluripotent cells (teratomas); genetically abnormal cells; reactivation of reprogramming factors | iPS-derived neural progenitors grafted into injured mouse spinal cords formed tumors months later (Nori and colleagues 2015); sorting out undifferentiated cells, karyotyping, suicide genes |
| Uncontrolled differentiation | the graft makes the wrong cell types or migrates | neural stem cells forming glia instead of neurons; ectopic tissue |
| Immune rejection | allogeneic cells; immunogenicity of iPS derivatives | HLA-matched banks; immunosuppression; autologous cells |
| Contamination | culture media, animal products, unwanted cells, pathogens, activation of latent viruses | good manufacturing practice, xeno-free media |
| Genetic change in culture | selection for culture-adapted cells | recurrent gains of 20q11.21 (*BCL2L1*) and *TP53* mutations in human PSCs; genome monitoring |
| Unproven treatments | clinics selling untested "stem cell" injections | blindness after intravitreal injection of adipose cells (Kuriyan and colleagues 2017) |

Stem-cell therapy is thus a field where the claims run ahead of the evidence; every product needs the same controlled trials of efficacy and safety as a drug, with particular attention to the long-term fate of living cells that cannot be withdrawn once given.

## Summary

| Topic | Key points |
|---|---|
| Lines from the embryo | ES cells, naive vs primed pluripotency (Definition 36.2.1), EpiSC; TSC and XEN; haploid ES cells, imprinting as the barrier to uniparental mice |
| Niches | *Drosophila* GSC niche (BMP represses *bam*, oriented division), V-SVZ B1 cells set aside from embryonic radial glia, perivascular HSC niche; MSC criteria and their limits |
| Birth–death process | master equation (36.1); generating function, extinction $q/p$, mean $\mathrm{e}^{(p-q)t}$, variance $\frac{p+q}{p-q}E(E-1)$ (Theorem 36.4.1); exponential scaled law with atom at zero (Corollary 36.4.1) |
| Galton–Watson | iterated $f$, moments (Theorem 36.4.2); extinction = smallest fixed point, stability via $f'$ (Theorem 36.4.3); subcritical, critical ($2/\sigma^2n$, exponential) and supercritical limits, $\varphi(ms) = f(\varphi(s))$ (Theorem 36.4.4) |
| Approximations | linear fractional law reproduces the Poisson-case shape (Example 36.4.1); near-critical expansion (Proposition 36.4.1, Remark 36.4.1) |
| Homeostasis | critical branching: clone loss $\propto 1/t$, linear growth of survivors, exponential scaled sizes; neutral drift; stochastic fate with local regulation (Example 36.4.2) |
| Cancer stem cells | Definition 36.5.1; therapy as extinction; assay dependence and plasticity |
| Embryo models | Definition 36.6.1: gastruloids, micropatterns, blastoids, ETX/SEM; not embryos; 14-day rule (Remark 36.6.1) |
| Organoids and therapy | self-organization following development (Example 36.7.1); scaffolds, xenotransplants, chimeras; approved therapies and the risks table |

## Questions

1. Naive mouse ES cells injected into a blastocyst make chimeras; primed EpiSCs rarely do, but they integrate when grafted into a post-implantation epiblast. What does this say about pluripotency, and how would you test whether a new human pluripotent line is naive?

   **Answer** Pluripotency is not one state: the ability to contribute to all lineages depends on matching the developmental stage of the host, so naive and primed cells correspond to pre- and post-implantation epiblast. Since human chimeras in human embryos are not permissible, tests use proxies: transcriptome comparison with single-cell data of human pre-implantation epiblast; two active X chromosomes in female lines and global DNA hypomethylation; dependence on LIF/MEK-inhibition rather than FGF/Activin; ability to make trophoblast and to form blastoids; and contribution to interspecies chimeras (mouse or monkey embryos), with its limits.

2. Why do androgenetic haploid ES cells support development poorly when injected into oocytes, and why did deleting the *H19* and IG differentially methylated regions help?

   **Answer** Mammalian development requires both a maternal and a paternal set of imprints. Sperm-derived haploid cells should carry paternal imprints (*H19* and *Gtl2* regions methylated), but in culture they lose methylation at these imprinting control regions, so the semi-cloned embryo expresses *H19* and *Gtl2* from both alleles and lacks the paternal pattern, as in a gynogenetic embryo, which fails. Deleting the two control regions fixes the expression pattern in the paternal configuration regardless of methylation, restoring correct dosage of *Igf2*/*H19* and *Dlk1*/*Gtl2* and greatly improving development.

3. In the birth–death process with $p = 1\ \mathrm{d^{-1}}$ and $q = 0.4\ \mathrm{d^{-1}}$, compute the probability that a clone is extinct at 4 days and the mean and standard deviation of its size. What fraction of the stem cells after 4 days belongs to surviving clones?

   **Answer** $E = \mathrm{e}^{0.6\times4} = 11.02$. $P_0 = 0.4(1 - 1/11.02)/(1 - 0.4/11.02) = 0.4 \times 0.909/0.964 = 0.377$. Mean $= 11.0$; variance $= (1.4/0.6)\times 11.02 \times 10.02 = 257.8$, standard deviation $16.1$ (larger than the mean). All stem cells belong to surviving clones, by definition; the mean size of the surviving clones is $11.0/(1 - 0.377) = 17.7$. The large variance relative to the mean, with a third of the clones extinct, is what the spleen-colony data showed.

4. Show that for the Galton–Watson process with $f(x) = q + px^2$ and $p = 0.6$ the probability of extinction by generation 3 is about 0.55, and find the limit.

   **Answer** $P_0(1) = f(0) = 0.4$; $P_0(2) = 0.4 + 0.6 \times 0.16 = 0.496$; $P_0(3) = 0.4 + 0.6 \times 0.496^2 = 0.4 + 0.6 \times 0.246 = 0.548$. The limit is the smallest fixed point $q/p = 0.4/0.6 = 2/3$; the approach is geometric with ratio $f'(2/3) = 2 \times 0.6 \times 2/3 = 0.8$.

5. Why does the distribution of clone sizes not distinguish between the constant-rate and the fixed-cycle model, and what measurement would?

   **Answer** Expressed through the measured mean and the variance ratio $r^2$, both give, for large clones, the same law: an atom of extinct clones with weight $(r^2 - 1)/(r^2 + 1)$ and an exponential with mean $(1 + r^2)/2$ for the survivors (Corollary 36.4.1, Example 36.4.1). The models differ in the timing of individual divisions, which affects small clones and the time course, not the scaled shape. Discriminating measurements are direct: live imaging of cell-cycle durations and of the fates of sister cells (fixed or variable cycle; correlation between sisters), or clone-size distributions at early times when clones contain few cells.

6. In a critical stem-cell population ($m = 1$, $\sigma^2 = 1$), 1000 stem cells are labeled individually at time 0. Estimate how many labeled clones remain after 100 generations, their mean size, and the total number of labeled stem cells. How do these change if $m = 1.01$?

   **Answer** Critical: survivors $\approx 1000 \times 2/(\sigma^2 n) = 1000 \times 2/100 = 20$; mean size $\approx \sigma^2n/2 = 50$ (more precisely about 51); total $\approx 20 \times 50 = 1000$, unchanged on average. With $m = 1.01$ the population grows as $1.01^{100} = 2.7$ on average; the surviving fraction tends to $1 - x^*$, where for $f = q + px^2$ with $p = 0.505$, $x^* = q/p = 0.495/0.505 = 0.980$, so at least about $2\%$ survive permanently (about 20 clones, a little more at $n = 100$), each about $2.7 \times 1000/20 \approx 135$ cells: a 1% bias doubles to triples the total in 100 generations, which is why homeostasis requires regulation.

7. Gastruloids form an anteroposterior axis with colinear Hox expression and somites, but no brain and no extraembryonic tissues. What does this tell us about the requirements for axis formation in the mouse embryo?

   **Answer** Symmetry breaking, axial elongation, the posterior Wnt/Brachyury program, Hox colinearity and the segmentation clock can be generated by embryonic cells alone, given a Wnt pulse; they do not require the extraembryonic tissues (visceral endoderm, trophectoderm) or the uterus. The anterior visceral endoderm, which secretes Wnt and Nodal antagonists in the embryo, is needed for anterior (brain) identity, so its absence explains the missing head; adding extraembryonic endoderm (as in ETX/SEM models) or anterior signals restores more anterior structures. The models also show which features depend on mechanical constraints of the egg cylinder and which do not.

8. Explain the logic of the kidney organoid protocol of Example 36.7.1, and why a protocol that makes only nephron progenitors gives organoids without collecting ducts.

   **Answer** The ureteric bud (collecting ducts) and the metanephric mesenchyme (nephrons) arise from different parts of the intermediate mesoderm: cells that leave the primitive streak early become anterior intermediate mesoderm (ureteric lineage), cells that stay longer become posterior intermediate mesoderm (nephron lineage). The duration of Wnt stimulation sets how long cells stay in the streak-like state and hence which population forms; mixing both reproduces the two interacting tissues, and their reciprocal induction then builds the organ. Nephron progenitors alone can form nephrons (induced by Wnt), but no cell can make the collecting duct tree, which comes only from the ureteric lineage.

9. List the risks of a therapy using dopaminergic neurons derived from iPS cells for Parkinson's disease, and the measures that reduce each.

   **Answer** Tumors from residual pluripotent cells or proliferating neural progenitors (sorting for floor-plate progenitor markers, testing for undifferentiated cells, karyotyping and genome sequencing, long-term follow-up with imaging); graft-induced dyskinesias from serotonergic or inappropriate neurons (purity of the dopaminergic population); rejection (HLA-matched or autologous cells, immunosuppression); poor survival or integration (cell dose, placement in the putamen); genetic changes during culture (monitoring recurrent mutations such as *TP53*); disease spread to the graft (α-synuclein pathology seen in fetal grafts after a decade). Efficacy and safety must be shown in controlled trials.

10. (Open question) Should stem-cell-based models of the human embryo that contain extraembryonic tissues be governed by the 14-day rule? Argue both sides and propose a criterion.

    **Answer** For: if a model contains all lineages and could in principle develop, its moral status may approach that of an embryo, and the rationale of the rule (individuation, onset of the nervous system) applies to its developmental stage, not to its origin. Against: current models lack parts, are inefficient and cannot develop to term; restricting them like embryos would block research that reduces the use of real embryos. Possible criterion: regulate by developmental potential and stage reached (equivalence to the primitive streak, presence of neural tissue), not by derivation; prohibit transfer to a uterus and culture beyond agreed stages without specific review, as the ISSCR guidelines do.
