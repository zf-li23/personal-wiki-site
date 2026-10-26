---
title: A Quantitative View of Gene Expression
description: Gene expression as a sequence of rates. Binding by mass action, occupancy and the observed rate k_obs = k_on[A] + k_off, specificity as residence time; the target-search paradox of the lac repressor, facilitated diffusion by sliding and hopping and the different answers of RNA polymerase, p53 and Cas9; production and removal dY/dt = β − αY, steady state and response time set by degradation and dilution; the gene regulation function and its measurement in single cells (Rosenfeld 2005, binomial partitioning); bursts of mRNA and protein, the telegraph model, the Fano factor and intrinsic and extrinsic noise; autoregulation and response time; speed, accuracy and energy across the central dogma.
---

The preceding chapters described the machinery of gene expression: which molecules bind where, what each enzyme does, and the experiments that showed it. The same knowledge can be expressed in numbers: how tightly and for how long a regulator binds its site, how long it takes to find it, how many proteins a gene makes per hour, how quickly that number can change, and how much it varies from cell to cell. This chapter collects these quantities into a small set of models, each a direct consequence of the law of mass action and of the fact that molecules are few. It treats, in order, binding (22.1) and the search for a **binding site** (22.2), the kinetics of production and removal (22.3), the input–output relation of a regulated **promoter** (22.4), the randomness of expression (22.5), the effect of a gene regulating itself (22.6), and the speed, accuracy and cost of the three transfers of the **central dogma** (22.7). The equilibrium theory of promoter occupancy, the **thermodynamic model**, was developed in [7.2.11](/7.2.11), the kinetics of **mRNA** levels in [7.2.18](/7.2.18#sec-18.1), and the orders of magnitude of molecular biology in [7.2.1](/7.2.1#sec-1.5); they are used here, not repeated. The diffusion theory of target search belongs to biophysics ([7.6](/7.6)), and the dynamics of regulatory networks, their **motifs** and the analysis of noise to systems biology ([7.9](/7.9)); this chapter stops at a single gene.

## 22.1. Binding: Mass Action and Occupancy

### 22.1.1. Equilibrium Occupancy

A transcription factor A binds a site B on DNA in a bimolecular reaction, $\mathrm{A} + \mathrm{B} \rightleftharpoons \mathrm{AB}$, with association rate constant $k_{\mathrm{on}}$ and dissociation rate constant $k_{\mathrm{off}}$. By the **law of mass action** ([6.1.7](/6.1.7)) the equilibrium is characterized by the **dissociation constant** $K_{\mathrm{D}} = k_{\mathrm{off}}/k_{\mathrm{on}}$ ([7.1.7](/7.1.7)), and the probability that the site is occupied, its **fractional saturation**, is
$$
\theta = \frac{[\mathrm{A}]}{[\mathrm{A}] + K_{\mathrm{D}}}, \tag{22.1}
$$
the binding curve of [7.1.7](/7.1.7#def-7.1.2). In a cell the concentrations are numbers of molecules: in an *E. coli* cell of about $1\,\mu\mathrm{m}^3$, one molecule corresponds to about $1.7\,\mathrm{nM}$ ([7.2.1](/7.2.1#sec-1.5.3)), so a site with $K_{\mathrm{D}} = 1\,\mathrm{nM}$ is half occupied by fewer than one free molecule per cell on average. In the **thermodynamic model** the competing nonspecific sites of the genome replace the solvent as the reference state, and $[\mathrm{A}]/K_{\mathrm{D}}$ becomes $(A/N_{\mathrm{NS}})\mathrm{e}^{-\beta\Delta\varepsilon}$ (Formula 11.6.1), but the form of Eq. (22.1) is unchanged.

### 22.1.2. The Kinetics of Binding

**Formula 22.1.1 (Relaxation to Equilibrium)** If A is in excess over B, so that $[\mathrm{A}]$ is constant, the occupancy obeys
$$
\frac{\mathrm{d}\theta}{\mathrm{d}t} = k_{\mathrm{on}}[\mathrm{A}](1 - \theta) - k_{\mathrm{off}}\theta, \tag{22.2}
$$
a **first-order reaction** in $\theta$ with solution, for an initially empty site,
$$
\theta(t) = \theta_{\mathrm{eq}}\left(1 - \mathrm{e}^{-k_{\mathrm{obs}}t}\right), \qquad k_{\mathrm{obs}} = k_{\mathrm{on}}[\mathrm{A}] + k_{\mathrm{off}}, \tag{22.3}
$$
where $\theta_{\mathrm{eq}}$ is given by Eq. (22.1). After the free factor is removed (a chase), the complex dissociates as $\theta(t) = \theta(0)\mathrm{e}^{-k_{\mathrm{off}}t}$.

The observed rate is linear in the concentration of the factor, with slope $k_{\mathrm{on}}$ and intercept $k_{\mathrm{off}}$, and this is how both constants are measured: by following association at several concentrations (by filter binding, surface plasmon resonance or single-molecule fluorescence) and dissociation after a chase. The relaxation is always faster than dissociation alone: at high concentrations of factor, equilibrium is reached quickly even for a site from which the factor dissociates slowly.

**Example 22.1.1 (Is promoter occupancy at equilibrium?)** A factor with $k_{\mathrm{on}} = 10^8\,\mathrm{M^{-1}\,s^{-1}}$ and $K_{\mathrm{D}} = 1\,\mathrm{nM}$ has $k_{\mathrm{off}} = 0.1\,\mathrm{s^{-1}}$, a mean residence time $1/k_{\mathrm{off}}$ of $10\,\mathrm{s}$. At $10\,\mathrm{nM}$ (about six molecules in a bacterium), $k_{\mathrm{obs}} = 1 + 0.1 = 1.1\,\mathrm{s^{-1}}$: the site equilibrates in about a second. Transcription initiation at a typical promoter occurs from once every few seconds to once every few minutes, and a protein's level changes over minutes to hours, so on these time scales the site samples its states many times and the equilibrium occupancy of Eq. (22.1) is a good approximation. This is the assumption behind the thermodynamic model of [7.2.11](/7.2.11). It fails for very tight sites, with residence times comparable to the interval between initiation events or to the cell cycle; then the history of binding, not only its equilibrium, determines expression.

### 22.1.3. Specificity Lies in the Dissociation Rate

For a protein binding a site on DNA, $k_{\mathrm{on}}$ is close to the limit set by diffusion and differs little between the specific site and any other stretch of DNA (22.2): the protein must first collide with the DNA, and the collision rate does not know the sequence. What distinguishes a specific site is how long the protein stays once it is there. A difference $\Delta\Delta G$ in binding free energy between two sites changes $K_{\mathrm{D}}$ by the factor $\mathrm{e}^{\Delta\Delta G/k_{\mathrm{B}}T}$, tenfold for each $RT\ln 10 = 5.9\,\mathrm{kJ\,mol^{-1}}$ ($1.4\,\mathrm{kcal\,mol^{-1}}$) at $37\,^\circ\mathrm{C}$, almost entirely through $k_{\mathrm{off}}$. Specific hydrogen bonds between **side chains** and the edges of **base pairs** in the **major groove** ([7.2.14](/7.2.14)) therefore act by lengthening the residence time: from milliseconds on nonspecific DNA to seconds or minutes on a good site and hours on the tightest sites.

![Binding of a transcription factor A to a single DNA site by mass action (illustrative constants k_on = 10⁸ M⁻¹ s⁻¹, **K_D** = 1 nM, so k_off = 0.1 s⁻¹ and a mean residence time of 10 s). A: site occupancy after mixing at t = 0 for [A] = 0.3, 1, 3 and 10 nM (solid), approaching θ_eq = [A]/([A] + K_D) at rate k_obs = k_on[A] + k_off; dashed: dissociation after removal of free factor at t = 30 s, at the rate k_off whatever [A] was. B: the observed rate is linear in [A], with slope k_on and intercept k_off. C: residence time 1/k_off = 1/(k_on K_D) against K_D for a fixed diffusion-limited k_on: milliseconds on nonspecific DNA (K_D ≈ 10 µM), seconds on a typical specific site (1 nM), hours on a very tight site (1 pM)](./plots/binding-kinetics.py)

## 22.2. Target Search

### 22.2.1. Riggs's Paradox

How fast can a protein find a single site among millions of base pairs? Riggs, Bourgeois and Cohn (1970) answered the question for the lac **repressor** and found that it was faster than seemed possible.

**Example 22.2.1 (The lac repressor binds faster than diffusion allows)** By filter binding of labeled DNA containing the *lac* **operator** ([7.2.11](/7.2.11)), Riggs and colleagues measured, in a low-salt buffer, a dissociation constant of about $10^{-13}\,\mathrm{M}$, a dissociation rate constant $k_{\mathrm{off}} = (6.2 \pm 1.3)\times10^{-4}\,\mathrm{s^{-1}}$ (a half-life of the complex of about $20\,\mathrm{min}$), and an association rate constant $k_{\mathrm{a}} = (7 \pm 0.9)\times10^{9}\,\mathrm{M^{-1}\,s^{-1}}$. The upper limit for a reaction controlled by diffusion is given by the Smoluchowski expression ([6.3.17](/6.3.17); **diffusion-controlled reaction**)
$$
k_{\mathrm{diff}} = 4\pi(D_{\mathrm{A}} + D_{\mathrm{B}})R\,N_{\mathrm{A}},
$$
where $R$ is the reaction radius. For a protein of $D \approx 5\times10^{-11}\,\mathrm{m^2\,s^{-1}}$ and a target that is a few base pairs on one face of the DNA, with an effective radius of a fraction of a nanometer, the estimate is about $10^8\,\mathrm{M^{-1}\,s^{-1}}$ (Riggs's estimate was $1.9\times10^8$). The measured value is about $40$ times larger.

The resolution, suggested by Riggs and colleagues and worked out by Berg, Winter and von Hippel (1981), is that the protein does not need to hit the operator directly from solution. It binds DNA nonspecifically anywhere and then moves along it.

### 22.2.2. Facilitated Diffusion

**Definition 22.2.1 (Target Search)** **Target search** is the process by which a DNA-binding protein finds its specific site in a large excess of nonspecific DNA. In facilitated diffusion, the protein alternates between three-dimensional diffusion in solution and nonspecific binding to DNA, during which it moves by one-dimensional sliding along the helix, by hopping (dissociation and rebinding a short distance away), or by intersegment transfer between two DNA segments brought close by looping.

Sliding enlarges the target. A protein that lands anywhere within about one sliding length of the operator finds it by sliding, so the effective target is not a few base pairs but the stretch of DNA scanned in one nonspecific binding event, the antenna. If the sliding length is $\ell$ base pairs, the association rate approaches $k_{\mathrm{diff}}$ times the ratio of $\ell$ to the size of the target. Two predictions were confirmed: the association rate increases with the length of nonspecific DNA around the operator up to a plateau (the antenna cannot be longer than the DNA), and it falls steeply with increasing salt, which weakens nonspecific binding and shortens sliding. The rate of $7\times10^{9}$ of Example 22.2.1 was measured at low salt, where sliding is long; at physiological ionic strength the in vitro rate is lower.

There is an optimum. A protein that never binds DNA nonspecifically searches only in three dimensions and pays the full cost of hitting a small target. A protein that binds too tightly spends all its time sliding, and one-dimensional diffusion is slow and redundant (a random walk revisits the same sites many times). The search time is shortest when the protein divides its time roughly equally between the two modes, which corresponds to a nonspecific residence time of the order of the time between nonspecific encounters; the derivation of this result, and of the search time as a function of the sliding length, belongs to [7.6](/7.6). This explains why a good transcription factor binds nonspecific DNA neither too weakly nor too strongly, and connects to the design of **σ factors** in [7.2.10](/7.2.10).

**Example 22.2.2 (The search in a living cell)** Elf, Li and Xie (2007) imaged single fluorescent lac repressors in *E. coli*. The repressor spent about $90\,\%$ of its time bound nonspecifically to DNA, with residence times of no more than a few milliseconds per binding event, and diffused along DNA with $D_{1} \approx 0.046\,\mu\mathrm{m^2\,s^{-1}}$. Hammar, Elf and colleagues (2012) measured, from the rate of binding to operators placed close together, a sliding length of about $45\,\mathrm{bp}$, and found that the repressor often slides over its operator without binding. A rough estimate of the search time follows: sliding $45\,\mathrm{bp}$ ($15\,\mathrm{nm}$) takes $\tau_{1} \approx (15\,\mathrm{nm})^2/(2D_1) \approx 2.5\,\mathrm{ms}$; to scan a genome of $4.6\times10^6\,\mathrm{bp}$ in pieces of $45\,\mathrm{bp}$ requires about $10^5$ independent binding events, which at a few milliseconds each (sliding plus the short three-dimensional excursions between them) take a few minutes. One repressor therefore needs minutes to find its operator; a cell with about ten repressor tetramers finds it in tens of seconds. This is fast enough to regulate genes on the time scale of a cell cycle, and it is why repression is reestablished promptly after replication and after **inducer** is removed.

![Target search. A: facilitated diffusion (schematic): a protein reaches the DNA from solution, slides along it while bound nonspecifically (solid wavy segments), hops over short distances or jumps far by three-dimensional diffusion (dashed arcs), and finds the target (highlighted) by sliding when it lands within about one sliding length of it, so the DNA around the site acts as an antenna. B: association rate constants (logarithmic scale): typical protein–protein association and the encounter of a small molecule with an enzyme for comparison; Riggs's diffusion-limited estimate for an operator-sized target (1.9 × 10⁸ M⁻¹ s⁻¹), the measured association of lac repressor with operator DNA in low salt (7.0 × 10⁹), and the antenna estimate, the diffusion limit multiplied by a sliding length of 45 bp (8.6 × 10⁹)](./plots/target-search.py)

### 22.2.3. Three Proteins, Three Answers

Facilitated diffusion is not a universal law; single-molecule experiments on DNA "curtains" (DNA molecules aligned on a **lipid** surface and imaged by total internal reflection fluorescence) and in living cells show that different proteins solve the search differently.

| Protein | Search mechanism observed | Consequence |
|---|---|---|
| *E. coli* **RNA polymerase holoenzyme** | No detectable sliding over long distances on DNA curtains; promoters found by three-dimensional collisions (Wang, Greene and colleagues, 2013) | Polymerase is abundant (thousands per cell) and promoters are many; weak nonspecific binding of the **holoenzyme** ([7.2.10](/7.2.10)) favors rapid sampling |
| p53 | Long one-dimensional diffusion with rotation along the helix, mediated by its **C-terminal domain**; the core **domain** recognizes the site in a conformational switch between a search mode and a recognition mode (Tafvizi, Mirny, van Oijen and colleagues, 2011) | Combines fast scanning with high specificity: the search mode binds weakly, the recognition mode tightly |
| Cas9–guide RNA | Three-dimensional collisions without extended sliding; at each encounter the PAM is checked first, non-PAM sites are rejected within milliseconds, and only at a PAM is the adjacent DNA unwound to test pairing with the guide (Sternberg, Doudna and colleagues, 2014) | The search is slow: a single dCas9 complex in *E. coli* needs about six hours to find one target (Jones, Elf and colleagues, 2017), so effective editing and CRISPR interference require many complexes ([7.2.24](/7.2.24)) |

## 22.3. From Occupancy to Rates: Production and Removal

### 22.3.1. The Basic Equation

Binding determines the probability that a promoter is active; the quantity that matters to the cell is the amount of the gene product. The simplest model treats the promoter activity as a production rate.

**Formula 22.3.1 (Production and Removal)** Let a protein Y be made at rate $\beta$ (molecules per unit time per cell, or concentration per unit time) and removed by first-order processes with rate constant $\alpha = \alpha_{\mathrm{deg}} + \alpha_{\mathrm{dil}}$, the sum of active degradation and dilution by growth ($\alpha_{\mathrm{dil}} = \ln 2/\tau_{\mathrm{cc}}$ for a cell cycle of length $\tau_{\mathrm{cc}}$). Then
$$
\frac{\mathrm{d}Y}{\mathrm{d}t} = \beta - \alpha Y, \tag{22.4}
$$
with **steady state** $Y^* = \beta/\alpha$; after a change of $\beta$ at $t = 0$ from a state $Y_0$,
$$
Y(t) = Y^* + (Y_0 - Y^*)\,\mathrm{e}^{-\alpha t}. \tag{22.5}
$$

The rate $\beta$ is the promoter activity of 22.4: maximal production times the occupancy-dependent factor, multiplied by the number of proteins made per mRNA. The equation is the same as Eq. (18.1) for mRNA ([7.2.18](/7.2.18#sec-18.1)); the new element here is the protein and its dilution.

**Definition 22.3.1 (Response Time)** The **response time** of a gene product is the time needed to cover half of the distance from its initial level to a new steady state after a sudden change in its production; by Eq. (22.5), it is
$$
T_{1/2} = \frac{\ln 2}{\alpha} = \frac{\ln 2}{\alpha_{\mathrm{deg}} + \alpha_{\mathrm{dil}}}, \tag{22.6}
$$
independent of $\beta$.

Three consequences follow. First, the response time is set by removal, not by production: making more protein raises the steady state but does not reach it sooner. Second, most bacterial proteins are stable on the time scale of growth ($\alpha_{\mathrm{deg}} \ll \alpha_{\mathrm{dil}}$), so their response time is one cell cycle, $20$–$60\,\mathrm{min}$ for *E. coli* in rich media; a bacterium can change the level of a stable protein faster only by growing faster or by degrading it actively (as for σ³² and LexA). Third, in a mammalian cell with a doubling time of a day and a median protein half-life of about two days (Schwanhäusser and colleagues, 2011; [7.2.18](/7.2.18#sec-18.1)), most proteins respond on a time scale of a day, much more slowly than their mRNAs; signaling proteins and transcription factors that must change within an hour are actively degraded (by the **ubiquitin**–**proteasome** system, [7.2.20](/7.2.20)). Shut-off follows the same rule: after transcription stops, a stable protein disappears only by dilution, halving each cell cycle.

### 22.3.2. Two Stages

With mRNA $m$ and protein $p$,
$$
\frac{\mathrm{d}m}{\mathrm{d}t} = k_m - \gamma_m m, \qquad \frac{\mathrm{d}p}{\mathrm{d}t} = k_p m - \gamma_p p,
$$
where $k_m$ is the transcription rate, $\gamma_m$ the mRNA decay constant ([7.2.18](/7.2.18)), $k_p$ the translation rate per mRNA and $\gamma_p$ the protein removal constant. The steady state is $m^* = k_m/\gamma_m$, $p^* = k_pk_m/(\gamma_m\gamma_p)$: the protein level is the product of four rates, each a separate point of control (transcription, mRNA stability, translation, protein stability). The ratio $b = k_p/\gamma_m$ is the mean number of proteins made from one mRNA in its lifetime, the translational burst size of 22.5. Because mRNAs usually turn over much faster than proteins ($\gamma_m \gg \gamma_p$), the mRNA follows the promoter quickly and the protein follows with its own, slower response time; the two-stage model then reduces to Eq. (22.4) with $\beta = bk_m$.

![Production–removal dynamics, dY/dt = β − αY, with time in cell cycles. A: simple regulation: production switched on at t = 0 (solid) or off (dashed) for a stable protein removed only by dilution (α = ln 2 per cell cycle, response time T½ = one cell cycle) and for an actively degraded protein with a half-life of 0.2 cell cycle; dots mark T½, which does not depend on β. B: negative autoregulation, dY/dt = β_max/(1 + (Y/K)²) − αY, with β_max five times the production of simple regulation and K = 0.5 chosen so that both circuits reach the same steady state: the strong initial production is cut back as Y rises, and half the steady state is reached about five times faster (T½ = 0.22 against 1). C: positive autoregulation, dY/dt = β₀ + β₁Y⁴/(K⁴ + Y⁴) − αY with β₀ = 0.05, β₁ = 1.3, K = 1, α = ln 2: production (sigmoidal) and removal (straight line) intersect three times, at two stable states (off and on, filled) separated by an unstable threshold (open), so the circuit is bistable](./plots/response-time.py)

## 22.4. The Gene Regulation Function

### 22.4.1. Definition

**Definition 22.4.1 (Gene Regulation Function)** The **gene regulation function** (input function) of a promoter is the rate of production of its gene product as a function of the concentrations of the active transcription factors that control it, measured in the steady state of binding. For a single repressor X and a single activator X it is often well described by Hill functions,
$$
f_{\mathrm{rep}}(X) = \frac{\beta}{1 + (X/K)^n}, \qquad f_{\mathrm{act}}(X) = \frac{\beta\,(X/K)^n}{1 + (X/K)^n}, \tag{22.7}
$$
with maximal rate $\beta$, half-effect concentration $K$ and Hill coefficient $n$.

The thermodynamic model of [7.2.11](/7.2.11) derives such functions from binding energies: for one operator and a weak promoter, the fold change $1/[1 + (R/N_{\mathrm{NS}})\mathrm{e}^{-\beta\Delta\varepsilon_{\mathrm{rd}}}]$ (Formula 11.6.2) is Eq. (22.7) with $n = 1$. A **Hill coefficient** greater than one arises from **cooperativity**: two repressor dimers that bind adjacent operators cooperatively, as CI at $O_{\mathrm{R}}1$ and $O_{\mathrm{R}}2$ of phage λ (Shea–Ackers model, [7.2.11](/7.2.11)), or a repressor that must dimerize before it binds, give $n$ near $2$. The **Hill coefficient** sets the sensitivity: to move the output from $90\,\%$ to $10\,\%$ of its maximum, $X$ must change by the factor $81^{1/n}$, that is $81$-fold for $n = 1$ and $9$-fold for $n = 2$. Promoters with two inputs combine them in AND-like or OR-like functions (the *lac* promoter needs **CAP**–**cAMP** and the absence of repressor, [7.2.11](/7.2.11)); the logic of multi-input functions and of networks built from them is taken up in [7.9](/7.9).

### 22.4.2. Measuring a Gene Regulation Function in Single Cells

**Example 22.4.1 (Rosenfeld and colleagues, 2005)** Rosenfeld, Young, Alon, Swain and Elowitz measured the gene regulation function of the λ $P_{\mathrm{R}}$ promoter in individual living *E. coli* cells. The repressor CI was fused to yellow fluorescent protein and expressed from an inducible promoter; $P_{\mathrm{R}}$ drove a cyan fluorescent protein. After induction, the repressor's synthesis was switched off, and as the cells grew and divided, the stable repressor was diluted by half in each cell cycle. Following a lineage of cells by time-lapse microscopy gave, at each moment, the repressor concentration $X$ (yellow fluorescence) and the production rate of the target, $\mathrm{d}Y/\mathrm{d}t + \alpha Y$ (from the cyan fluorescence $Y$ and its dilution). The target remained off while $X$ was high and turned on when the repressor had been diluted below its half-repression concentration. The function was well fitted by $f_{\mathrm{rep}}$ of Eq. (22.7) with a Hill coefficient of about $2$, consistent with **cooperative binding** of CI dimers to $O_{\mathrm{R}}1$ and $O_{\mathrm{R}}2$, and a half-repression point of the order of a hundred repressor molecules per cell. The gene regulation function itself varied between cells and fluctuated within a cell on the time scale of a cell cycle: two cells with the same repressor concentration produced the target at rates differing by tens of percent. This variability, due to fluctuations in other cellular components (polymerases, **ribosomes**, growth rate), limits how precisely a cell can read the concentration of a transcription factor (22.5.4).

To convert fluorescence into numbers of molecules, Rosenfeld and colleagues used the randomness of cell division.

**Formula 22.4.1 (Counting Molecules by Binomial Partitioning)** If at division each of the $n$ molecules of a mother cell goes independently to either daughter with probability $1/2$, and each molecule contributes fluorescence $\nu$, the fluorescences $y_1$ and $y_2$ of the daughters satisfy
$$
\left\langle (y_1 - y_2)^2 \right\rangle = \nu\,(y_1 + y_2). \tag{22.8}
$$

**Proof** The number $n_1$ received by the first daughter follows the **binomial distribution** $\mathrm{Bin}(n, 1/2)$ ([3.1.4](/3.1.4)), with mean $n/2$ and **variance** $n/4$. Then $y_1 - y_2 = \nu(2n_1 - n)$ has mean zero and variance $4\nu^2 \cdot n/4 = \nu^2 n = \nu(y_1 + y_2)$. $\square$

Fitting the mean squared difference of sister cells against their summed fluorescence gives $\nu$, the fluorescence of one molecule, without ever detecting a single molecule; the method assumes independent partitioning, which fails for proteins that aggregate or attach to the poles or the membrane.

![The gene regulation function and its measurement (simulated, illustrative numbers). A: repression functions f(X) = β/(1 + (X/K)ⁿ) for n = 1, 2 and 4 (logarithmic X axis); dots mark 90 % and 10 % of maximal output, which X must span by the factor 81^(1/n). B: the dilution experiment: a stable fluorescent repressor (dashed, relative to its initial level) is made until t = 0 and then diluted by half each cell cycle; the target output Y (solid, relative to its maximum; K = X(0)/50, n = 2, Y diluted at the same rate) remains low while X ≫ K and rises after X has fallen below K (dotted line). C: binomial partitioning: 3000 simulated divisions of mothers with 20–600 molecules, with fluorescence ν = 50 a.u. per molecule and 0.5 % measurement noise; the mean squared difference of the daughters' fluorescence grows linearly with their sum, and the fitted slope recovers ν, Eq. (22.8)](./plots/gene-regulation-function.py)

## 22.5. Stochastic Gene Expression

### 22.5.1. Molecules Are Made in Bursts

Equation (22.4) describes averages. A gene in a bacterium exists in one or a few copies, its mRNA in a few copies or less, and every event of transcription, translation and degradation is a random encounter of molecules. Isogenic cells in the same environment therefore contain different numbers of each protein, and the differences are not small.

**Example 22.5.1 (Watching proteins being made one at a time)** Yu, Xiao, Ren, Lao and Xie (2006) detected the synthesis of individual protein molecules in living *E. coli*. Single fluorescent proteins in the cytoplasm move too fast to be seen against the cell's autofluorescence, so they fused a fast-maturing yellow fluorescent protein (Venus, which becomes fluorescent within minutes, much faster than wild-type GFP, **green fluorescent protein**) to the membrane protein Tsr, whose diffusion in the membrane is about a hundred times slower. Under a repressed *lac* promoter, each cell expressed only a few molecules per cell cycle, which could be counted and then photobleached, so that each newly made molecule appeared as a new fluorescent spot. Proteins appeared in bursts: several molecules within a few minutes, then none for a long time. The number of molecules per burst followed a geometric distribution with a mean of about four, and bursts occurred about once per cell cycle. Each burst is the translation of one mRNA: the repressed promoter fires rarely, and each short-lived mRNA (lifetime about two minutes) is translated a few times before it is degraded. In the same year Cai, Friedman and Xie (2006) observed bursts of β-galactosidase molecules with a fluorogenic **substrate**. Bursting also occurs at the level of transcription: Golding, Cox and colleagues (2005) counted mRNAs labeled with an MS2–GFP fusion in *E. coli* and found that transcription occurred in bursts separated by long silent periods, and Raj, Tyagi and colleagues (2006), counting single mRNAs by **fluorescence in situ hybridization**, found the same for mammalian genes.

**Definition 22.5.1 (Transcriptional Burst)** A **transcriptional burst** is a period in which a gene produces several transcripts in quick succession, separated from the next by a period of inactivity; bursty expression is characterized by the burst frequency (bursts per unit time) and the burst size (mean number of molecules per burst). Analogously, a translational burst is the set of protein molecules made from one mRNA.

### 22.5.2. The Telegraph Model

The simplest model of bursting lets the promoter switch between an inactive and an active state.

**Formula 22.5.1 (Telegraph Model)** Let the promoter switch from OFF to ON with rate constant $k_{\mathrm{on}}$ and back with $k_{\mathrm{off}}$, let mRNA be made at rate $r$ in the ON state only, and let each mRNA be degraded with rate constant $\gamma$. In the steady state the mean and the Fano factor (Definition 22.5.2) of the number $m$ of mRNAs are
$$
\langle m\rangle = \frac{r}{\gamma}\,\frac{k_{\mathrm{on}}}{k_{\mathrm{on}} + k_{\mathrm{off}}}, \qquad F = \frac{\operatorname{Var}(m)}{\langle m\rangle} = 1 + \frac{r\,k_{\mathrm{off}}}{(k_{\mathrm{on}} + k_{\mathrm{off}})(k_{\mathrm{on}} + k_{\mathrm{off}} + \gamma)}. \tag{22.9}
$$
In the bursty limit $k_{\mathrm{off}} \gg k_{\mathrm{on}}, \gamma$, bursts of mean size $b = r/k_{\mathrm{off}}$ occur at frequency $k_{\mathrm{on}}$, $\langle m\rangle = k_{\mathrm{on}}b/\gamma$, $F \approx 1 + b$, and $m$ follows a **negative binomial distribution** ([3.1.4](/3.1.4)).

**Definition 22.5.2 (Fano Factor)** The **Fano factor** of a random number of molecules is the ratio of its variance to its mean, $F = \operatorname{Var}(n)/\langle n\rangle$; it equals $1$ for the **Poisson distribution** ([3.1.4](/3.1.4)), which describes molecules made one at a time at a constant rate and degraded independently. The noise is the coefficient of variation $\eta = \sigma/\langle n\rangle$, with $\eta^2 = F/\langle n\rangle$.

A constitutive gene, always ON, is the special case $k_{\mathrm{off}} = 0$: its mRNA number is Poisson-distributed, $F = 1$, and its noise falls as $\eta = \langle m\rangle^{-1/2}$. A Fano factor well above one is the signature of bursts, and measured Fano factors of mRNA counts in yeast and mammalian cells are typically between $2$ and $50$. The model can be fitted to counts of single mRNAs, and such fits show how regulation acts: in mammalian cells, analysis of allele-specific single-cell RNA sequencing indicated that **enhancers** mainly increase the burst frequency, while **core promoter** elements set the burst size (Larsson, Sandberg and colleagues, 2019). The model is simulated exactly with the **Gillespie algorithm** ([4.4.7](/4.4.7#sec-7.2)): draw the waiting time to the next event from an **exponential distribution** whose rate is the sum of the rates of all possible events, choose the event with probabilities proportional to its rate, update the state, and repeat.

![Transcriptional bursting in the telegraph model, Gillespie simulations with time in units of the mRNA lifetime (γ = 1). A constitutive gene (always on, r = 20) and a bursty gene (k_on = 0.5, k_off = 20, r = 800: bursts of mean size b = 40 at frequency about 0.5, mean 19.5) have almost the same mean. A: trajectories; ticks mark the on periods of the bursty gene. B: steady-state distributions from long simulations (bars) with Poisson(20) and the negative binomial of the bursty limit (lines); the simulated Fano factors are 1.00 and 39 (exact value from Eq. (22.9), 37; bursty limit 1 + b = 41). C: Fano factor against mean burst size for a family with k_off = 50 and k_on adjusted to keep the mean at 20: simulations (points), the exact result of Eq. (22.9) (solid) and the bursty limit 1 + b (dashed)](./plots/transcriptional-bursting.py)

### 22.5.3. Protein Bursts

The same reasoning applied to translation gives the protein distribution of Example 22.5.1.

**Formula 22.5.2 (Bursty Protein Production)** If mRNAs are made at rate $k_m$, each lives a short time (decay constant $\gamma_m$) and is translated at rate $k_p$, and proteins are removed with rate constant $\gamma_p \ll \gamma_m$, then each mRNA yields a burst of proteins whose size follows a **geometric distribution** with mean $b = k_p/\gamma_m$, and in the steady state the protein number $n$ follows a negative binomial distribution, approximately a **gamma distribution** $\Gamma(a, 1/b)$ for large numbers, with
$$
a = \frac{k_m}{\gamma_p}, \qquad \langle n\rangle = ab, \qquad F = 1 + b, \qquad \eta^2 = \frac{1}{a} + \frac{1}{\langle n\rangle}. \tag{22.10}
$$

The two parameters have direct meanings: $a$ is the number of bursts per protein lifetime and $b$ the number of proteins per burst. They are obtained from a measured distribution by $b = \operatorname{Var}(n)/\langle n\rangle - 1$ and $a = \langle n\rangle/b$, which is how Xie and colleagues compared distributions of more than a thousand *E. coli* proteins measured in single cells (Taniguchi and colleagues, 2010). At low expression, the noise is dominated by the finite number of bursts ($1/a$); proteins made from few, efficiently translated mRNAs are noisier than proteins made from many, poorly translated mRNAs, at the same mean. This is a quantitative reason why translational efficiency and transcription rate are not interchangeable, and why genes that must be expressed precisely tend to be transcribed often and translated less.

![Protein bursts from single mRNAs, a two-stage model simulated with the Gillespie algorithm (time in cell cycles): mRNAs made at 1.2 per cell cycle, degraded at 30 per cell cycle (lifetime about 2 min for a 60-min cycle) and translated at 4 × 30 per cell cycle, so that each mRNA yields on average b = 4 proteins; proteins are stable and diluted by growth (α = ln 2 per cell cycle). A: newly made proteins counted in three cells over three cell cycles, as in the experiment of Yu and colleagues: they appear in steps, each step the proteins of one mRNA. B: distribution of 4000 burst sizes (bars) and the geometric distribution with mean 4 (points). C: steady-state distribution of protein number per cell (bars) and the negative binomial with shape a = k_m/α = 1.73 and mean ab = 6.9 (line); the simulated Fano factor is close to 1 + b = 5](./plots/protein-bursts.py)

### 22.5.4. Intrinsic and Extrinsic Noise

Two kinds of variability add up. The random timing of the reactions of one gene, its bursts and the partition of its molecules at division, is specific to that gene. Fluctuations in shared components, the numbers of polymerases and ribosomes, the cell's size, growth rate and stage of the cell cycle, the concentrations of upstream regulators, affect all genes of a cell together.

**Definition 22.5.3 (Intrinsic and Extrinsic Noise)** **Intrinsic noise** is the part of the cell-to-cell variation in the expression of a gene that arises from the stochastic events of its own expression and would make two identical copies of the gene in the same cell differ; **extrinsic noise** is the part that arises from differences between cells, or over time, in factors that affect both copies equally.

Elowitz, Levine, Siggia and Swain (2002) separated the two by placing two copies of the same promoter, driving cyan and yellow fluorescent proteins, in the same *E. coli* cell. With $c$ and $y$ the two fluorescences in a cell, normalized to equal means, the intrinsic and extrinsic noise are
$$
\eta_{\mathrm{int}}^2 = \frac{\langle (c - y)^2\rangle}{2\langle c\rangle\langle y\rangle}, \qquad \eta_{\mathrm{ext}}^2 = \frac{\langle cy\rangle - \langle c\rangle\langle y\rangle}{\langle c\rangle\langle y\rangle}, \qquad \eta_{\mathrm{tot}}^2 = \eta_{\mathrm{int}}^2 + \eta_{\mathrm{ext}}^2.
$$
Cells with the two colors in different proportions show intrinsic noise; cells that are all bright or all dim in both show extrinsic noise. Intrinsic noise decreased with increasing expression, as expected from Eq. (22.10); extrinsic noise was comparable or larger and, as the gene regulation function of Example 22.4.1 showed, changes slowly, over a cell cycle. Noise is not only an error: it allows a clonal population to diversify (persistence of a fraction of bacteria under antibiotics, competence in *Bacillus subtilis*, the lysis–**lysogeny** decision of phage λ, [7.2.11](/7.2.11)), and in development cells use or suppress it in specific ways. The propagation of noise through networks, its decomposition and its control are subjects of [7.9](/7.9).

## 22.6. Autoregulation and the Response Time

Many transcription factors regulate their own genes. In *E. coli*, a large fraction of the known transcription factors (about $40\,\%$) repress their own promoters. Equation (22.4) with the gene regulation function (22.7) in place of $\beta$ shows what this does.

**Formula 22.6.1 (Autoregulated Gene)** A gene whose product represses its own promoter obeys
$$
\frac{\mathrm{d}X}{\mathrm{d}t} = \frac{\beta_{\max}}{1 + (X/K)^n} - \alpha X, \tag{22.11}
$$
and one whose product activates its own promoter
$$
\frac{\mathrm{d}X}{\mathrm{d}t} = \beta_0 + \frac{\beta_1 (X/K)^n}{1 + (X/K)^n} - \alpha X. \tag{22.12}
$$

With negative autoregulation, a strong promoter ($\beta_{\max} \gg \alpha K$) produces the protein rapidly at first, and production is cut back as $X$ approaches $K$. Compared with a simple gene that reaches the same steady state, the autoregulated gene gets there faster, because its initial rate is higher; the speed-up is roughly the ratio of the maximal to the steady-state production rate. Rosenfeld, Elowitz and Alon (2002) measured a speed-up of about fivefold for an autoregulated TetR repressor in *E. coli*. Turning off is not accelerated: when production stops, $X$ decays at rate $\alpha$ in both cases. The same feedback also makes the steady state less sensitive to fluctuations in production (Becskei and Serrano, 2000).

With positive autoregulation, the steady states are the intersections of the sigmoidal production curve with the removal line $\alpha X$ (**ordinary differential equation**, [2.4.11](/2.4.11) for stability). If $n > 1$ and the feedback is strong enough, there are three: two stable states, off and on, separated by an unstable threshold. The gene is then bistable, and its state is a memory of past signals: a transient pulse of inducer that pushes $X$ over the threshold switches the cell on permanently. Becskei, Séraphin and Serrano (2001) built such a switch in yeast and observed a bimodal population. The maintenance of lysogeny by CI, which activates its own promoter $P_{\mathrm{RM}}$ ([7.2.11](/7.2.11)), is a natural case. Network motifs built from these elements, such as feed-forward loops, toggle switches and oscillators, are the subject of [7.9](/7.9).

## 22.7. Speed, Accuracy and Cost Across the Central Dogma

Each transfer of information in the central dogma is a polymerization with a template, and each faces the same trade-off between speed, accuracy and energy ([7.2.1](/7.2.1#sec-1.5.4)).

| Step | Elongation rate | Error frequency | Selection and correction | Energy per unit (phosphoanhydride bonds) | Chapter |
|---|---|---|---|---|---|
| Replication | *E. coli* $\approx 1000\,\mathrm{nt\,s^{-1}}$; human $15$–$50$ | $10^{-10}$–$10^{-9}$ per bp | Base selection ($10^{-4}$–$10^{-5}$), $3' \to 5'$ exonuclease proofreading ($10^{-2}$), mismatch repair ($10^{-2}$–$10^{-3}$) | $2$ per nucleotide (dNTP → dNMP + PP$_{\mathrm{i}}$, hydrolysis of PP$_{\mathrm{i}}$) | [7.2.7](/7.2.7), [7.2.8](/7.2.8) |
| Transcription | $20$–$80\,\mathrm{nt\,s^{-1}}$ | $10^{-6}$–$10^{-5}$ per nt | Base selection; backtracking and transcript cleavage (GreA/GreB, TFIIS) | $2$ per nucleotide | [7.2.10](/7.2.10), [7.2.13](/7.2.13) |
| Aminoacylation | — | $10^{-5}$–$10^{-4}$ | Double sieve: activation and editing sites of aminoacyl-tRNA synthetases | $2$ per amino acid (ATP → AMP + PP$_{\mathrm{i}}$) | [7.2.19](/7.2.19) |
| Translation | Bacteria $10$–$20\,\mathrm{aa\,s^{-1}}$; eukaryotes $3$–$8$ | $10^{-4}$–$10^{-3}$ per codon | Initial selection and **kinetic proofreading** after GTP hydrolysis by EF-Tu, induced fit of the decoding center | $2$ more per peptide bond (EF-Tu, EF-G), $4$ in total | [7.2.19](/7.2.19) |

Three regularities stand out. First, the discrimination afforded by a single equilibrium binding step is limited by the free-energy difference between right and wrong substrates: the error is at least $\mathrm{e}^{-\Delta\Delta G/k_{\mathrm{B}}T}$, about $10^{-2}$ for a difference of $4.6\,k_{\mathrm{B}}T$ ($12\,\mathrm{kJ\,mol^{-1}}$), the order of the difference between a correct and a mismatched base pair. Every error frequency below this is bought by additional steps of checking that are driven out of equilibrium, by hydrolysis of a nucleoside triphosphate or by an exonuclease that destroys correct products along with wrong ones; kinetic proofreading can square the discrimination at the cost of energy and of discarded correct substrates ([6.3.18](/6.3.18)). Second, accuracy matches the cost of an error: a replication error is inherited by all descendant cells and replication is the most accurate, while a translation error affects one short-lived molecule. Third, accuracy costs speed. A polymerase that waits longer before committing discriminates better (more time for wrong substrates to leave) but works more slowly; mutant ribosomes that are hyperaccurate grow more slowly, and error-prone ones are less fit. Measured rates and errors place each process near a compromise that depends on growth rate and cost of errors, a theme developed quantitatively in [7.6](/7.6) and [7.9](/7.9).

## Summary

| Topic | Key points |
|---|---|
| Binding (Eq. (22.1), Formula 22.1.1, Example 22.1.1) | $\theta = [\mathrm{A}]/([\mathrm{A}] + K_{\mathrm{D}})$, $K_{\mathrm{D}} = k_{\mathrm{off}}/k_{\mathrm{on}}$; $k_{\mathrm{obs}} = k_{\mathrm{on}}[\mathrm{A}] + k_{\mathrm{off}}$; $1\,\mathrm{nM} \approx 0.6$ molecules per bacterium; binding equilibrates in seconds, justifying the thermodynamic model |
| Specificity (22.1.3) | $k_{\mathrm{on}}$ near the diffusion limit for all DNA; specificity through $k_{\mathrm{off}}$, tenfold per $5.9\,\mathrm{kJ\,mol^{-1}}$; residence from ms (nonspecific) to hours |
| Target search (Example 22.2.1, Definition 22.2.1, Example 22.2.2, table in 22.2.3) | Riggs: $k_{\mathrm{a}} = 7\times10^9$ versus $\sim 10^8\,\mathrm{M^{-1}s^{-1}}$ diffusion limit; sliding, hopping, intersegment transfer; antenna $\approx$ sliding length ($45\,\mathrm{bp}$ in vivo), salt and length dependence; optimum at comparable 1D and 3D times; one LacI needs minutes; RNAP by 3D collisions, p53 slides with a search/recognition switch, Cas9 checks PAMs by 3D collisions and needs hours |
| Production and removal (Formula 22.3.1, Definition 22.3.1) | $\mathrm{d}Y/\mathrm{d}t = \beta - \alpha Y$, $Y^* = \beta/\alpha$, $T_{1/2} = \ln 2/(\alpha_{\mathrm{deg}} + \alpha_{\mathrm{dil}})$ independent of $\beta$; stable bacterial proteins respond in one cell cycle; two-stage $p^* = k_pk_m/(\gamma_m\gamma_p)$, $b = k_p/\gamma_m$ |
| Gene regulation function (Definition 22.4.1, Example 22.4.1, Formula 22.4.1) | Hill functions; $n$ from cooperativity, $81^{1/n}$-fold range; λ $P_{\mathrm{R}}$ in single cells, $n \approx 2$, cell-to-cell and temporal variability; binomial partition $\langle(y_1 - y_2)^2\rangle = \nu(y_1 + y_2)$ |
| Bursting (Example 22.5.1, Definitions 22.5.1–22.5.2, Formulas 22.5.1–22.5.2) | Yu 2006: about 4 proteins per burst, about one burst per cell cycle; telegraph model, $F = 1 + rk_{\mathrm{off}}/[(k_{\mathrm{on}} + k_{\mathrm{off}})(k_{\mathrm{on}} + k_{\mathrm{off}} + \gamma)] \approx 1 + b$; proteins: negative binomial/gamma with $a = k_m/\gamma_p$, $b = k_p/\gamma_m$, $\eta^2 = 1/a + 1/\langle n\rangle$; enhancers tune frequency, core promoters size |
| Noise (Definition 22.5.3) | Two-color experiment: $\eta_{\mathrm{int}}^2 = \langle(c-y)^2\rangle/2\langle c\rangle\langle y\rangle$, $\eta_{\mathrm{ext}}^2 = \operatorname{Cov}(c,y)/\langle c\rangle\langle y\rangle$; functions of noise |
| Autoregulation (Formula 22.6.1) | Negative: faster rise (about fivefold for TetR), same decay, less noise; positive with $n > 1$: bistability and memory (CI at $P_{\mathrm{RM}}$) |
| Speed, accuracy, cost (table in 22.7) | Errors $10^{-10}$ (replication), $10^{-5}$ (transcription), $10^{-4}$ (translation); single-step limit $\mathrm{e}^{-\Delta\Delta G/k_{\mathrm{B}}T}$; kinetic proofreading and repair buy accuracy with energy and speed |

## Questions

1. A repressor binds its operator with $k_{\mathrm{on}} = 2\times10^{8}\,\mathrm{M^{-1}\,s^{-1}}$ and $K_{\mathrm{D}} = 0.1\,\mathrm{nM}$. (a) What is the mean residence time on the operator? (b) In a bacterium of $1\,\mu\mathrm{m}^3$ with $10$ free repressors, what are the occupancy and the relaxation time of the operator? (c) An operator mutation weakens binding by $11.8\,\mathrm{kJ\,mol^{-1}}$ at $37\,^\circ\mathrm{C}$; how do the answers change?

   **Answer** (a) $k_{\mathrm{off}} = k_{\mathrm{on}}K_{\mathrm{D}} = 2\times10^{8} \times 10^{-10} = 0.02\,\mathrm{s^{-1}}$, a residence time of $50\,\mathrm{s}$. (b) Ten molecules in $1\,\mu\mathrm{m}^3$ are $10 \times 1.66\,\mathrm{nM} \approx 17\,\mathrm{nM}$; $\theta = 17/(17 + 0.1) = 0.994$; $k_{\mathrm{obs}} = 2\times10^{8} \times 1.7\times10^{-8} + 0.02 = 3.4\,\mathrm{s^{-1}}$, relaxation in about $0.3\,\mathrm{s}$. (c) $11.8\,\mathrm{kJ\,mol^{-1}} = 2 \times 5.9$ is a hundredfold change in $K_{\mathrm{D}}$, to $10\,\mathrm{nM}$, through $k_{\mathrm{off}}$, which becomes $2\,\mathrm{s^{-1}}$ (residence $0.5\,\mathrm{s}$); $\theta = 17/27 = 0.63$, and $k_{\mathrm{obs}} = 3.4 + 2 = 5.4\,\mathrm{s^{-1}}$. Repression falls from about $170$-fold ($1/(1 - \theta)$ for a promoter blocked whenever the operator is occupied) to less than threefold.

2. In Riggs's measurements, the ratio $k_{\mathrm{off}}/k_{\mathrm{a}}$ should equal the dissociation constant. Check this, and explain why the association rate decreased steeply when the salt concentration was raised, while the dissociation constant of nonspecific binding also increased.

   **Answer** $6.2\times10^{-4}/7\times10^{9} = 0.9\times10^{-13}\,\mathrm{M}$, consistent with the measured $K_{\mathrm{D}} \approx 10^{-13}\,\mathrm{M}$. Nonspecific binding of repressor to DNA is mainly electrostatic, between basic residues and the phosphate backbone, with release of counterions from the DNA; raising the salt concentration weakens it strongly. The repressor then stays on nonspecific DNA for shorter times, slides shorter distances, and the antenna that enlarges the target shrinks, so $k_{\mathrm{a}}$ falls toward the three-dimensional diffusion limit. The increase in the nonspecific dissociation constant is the same effect seen at equilibrium.

3. A bacterial protein is stable, and its gene is induced at $t = 0$ in cells dividing every $40\,\mathrm{min}$. (a) When does the protein reach half and $90\,\%$ of its new steady state? (b) To make the response four times faster without changing the steady state, by what factor must the protein's degradation and synthesis rates be changed? (c) What is the cost?

   **Answer** (a) $\alpha = \ln 2/40\,\mathrm{min}$; $T_{1/2} = 40\,\mathrm{min}$ and $T_{90} = \ln 10/\alpha = 3.3 \times 40 \approx 133\,\mathrm{min}$. (b) A fourfold faster response requires $\alpha$ four times larger: $\alpha_{\mathrm{deg}} = 3\alpha_{\mathrm{dil}}$, a half-life against degradation of $13\,\mathrm{min}$; to keep $Y^* = \beta/\alpha$, $\beta$ must also increase fourfold. (c) Three quarters of the protein synthesized is degraded rather than passed on to daughter cells, so the cell spends four times the amino acids and the energy of translation (four phosphoanhydride bonds per peptide bond) on this protein. Fast responses are paid for by turnover; negative autoregulation (22.6) obtains part of the speed-up at a lower cost during the approach to the steady state.

4. Show that in the telegraph model the Fano factor tends to $1$ when switching is fast ($k_{\mathrm{on}}, k_{\mathrm{off}} \gg \gamma$ and $r$ fixed per unit of time in the ON state) and to $1 + b$ in the bursty limit. Which regime does a constitutive bacterial promoter correspond to?

   **Answer** From Eq. (22.9), the excess term is $rk_{\mathrm{off}}/[(k_{\mathrm{on}} + k_{\mathrm{off}})(k_{\mathrm{on}} + k_{\mathrm{off}} + \gamma)]$. With fast switching at a fixed ON fraction $\phi = k_{\mathrm{on}}/(k_{\mathrm{on}} + k_{\mathrm{off}})$, write $k = k_{\mathrm{on}} + k_{\mathrm{off}}$: the term is $r(1 - \phi)/(k + \gamma) \to 0$ as $k \to \infty$, so $F \to 1$ (the promoter is effectively always partly on, and production is Poisson with rate $r\phi$). In the bursty limit $k_{\mathrm{off}} \gg k_{\mathrm{on}}, \gamma$, the term becomes $rk_{\mathrm{off}}/k_{\mathrm{off}}^2 = r/k_{\mathrm{off}} = b$. Many constitutive bacterial promoters show nearly Poisson mRNA statistics (Fano factors close to $1$), corresponding to the first regime; strongly regulated promoters and most eukaryotic genes are bursty.

5. Two genes each make $100$ new protein molecules per cell cycle on average. Gene 1 makes $50$ mRNAs per cell cycle, each translated twice; gene 2 makes $2$ mRNAs per cell cycle, each translated $50$ times. Proteins are stable (removed by dilution). Estimate the noise $\eta$ of each and explain the result.

   **Answer** With $\gamma_p = \ln 2$ per cell cycle, $a = k_m/\gamma_p$: $a_1 = 50/0.69 = 72$, $a_2 = 2/0.69 = 2.9$; $b_1 = 2$, $b_2 = 50$, so both have the same mean $\langle n\rangle = ab = 100/\ln 2 \approx 144$. From Eq. (22.10), $\eta^2 = 1/a + 1/\langle n\rangle$: $\eta_1^2 = 0.014 + 0.007 = 0.021$, $\eta_1 \approx 0.14$; $\eta_2^2 = 0.35 + 0.007 = 0.35$, $\eta_2 \approx 0.59$. Gene 2 is four times noisier because its protein comes in few large bursts: the number of bursts in a protein lifetime, not the number of proteins, determines the noise. Cells can lower noise at constant mean by transcribing more and translating less, at the cost of more transcription.

6. In a two-color experiment, the cyan and yellow fluorescences of $1000$ cells have equal means $\langle c\rangle = \langle y\rangle = 100$, variances $\operatorname{Var}(c) = \operatorname{Var}(y) = 900$ and covariance $\operatorname{Cov}(c, y) = 500$. Compute the intrinsic, extrinsic and total noise.

   **Answer** $\langle(c - y)^2\rangle = \operatorname{Var}(c) + \operatorname{Var}(y) - 2\operatorname{Cov}(c, y) = 900 + 900 - 1000 = 800$ (the means are equal), so $\eta_{\mathrm{int}}^2 = 800/(2 \times 10^4) = 0.04$, $\eta_{\mathrm{int}} = 0.20$. $\eta_{\mathrm{ext}}^2 = 500/10^4 = 0.05$, $\eta_{\mathrm{ext}} \approx 0.22$. $\eta_{\mathrm{tot}}^2 = 0.09$, $\eta_{\mathrm{tot}} = 0.30$, equal to $\sigma/\mu = 30/100$ for either color, as it must be. Extrinsic noise is slightly larger than intrinsic, typical of moderately expressed bacterial genes.

7. Using Eq. (22.12) with $n = 4$, $K = 1$, $\alpha = \ln 2$ and $\beta_0 = 0.05$, find graphically or numerically the range of $\beta_1$ for which the gene is bistable, and describe what happens to a population of cells, all initially off, when $\beta_1$ is raised slowly through this range and then lowered again.

   **Answer** Steady states satisfy $0.05 + \beta_1X^4/(1 + X^4) = 0.693X$. Solving numerically, there is one steady state (off) for $\beta_1 < 1.15$ and three for $1.15 < \beta_1 < 139$ (for $\beta_1 = 1.3$: $X \approx 0.07$, $0.99$ and $1.78$, as in the figure of 22.3); only above about $139$ does the off state disappear. The upper boundary is so high because with $n = 4$ the feedback is negligible at the low state ($X \approx 0.07$, $X^4 \approx 2\times10^{-5}$): the off state is maintained by the basal rate alone. Raising $\beta_1$ slowly from below $1.15$, cells that start off stay off across the whole bistable range (unless noise carries some over the threshold); lowering $\beta_1$ from a state in which cells have been switched on (for example by a pulse of activator), they stay on until $\beta_1 \approx 1.15$ and then jump off. The response therefore shows strong hysteresis: within the bistable range the state of a cell depends on its history, and noise-driven transitions make a population bimodal.

8. The error frequency of translation is about $10^{-4}$ per codon, but the free-energy difference between a cognate and a near-cognate codon–anticodon pair corresponds to a discrimination of only about $10^{-2}$. Explain how the ribosome achieves the lower error frequency and what it costs.

   **Answer** Selection occurs twice, separated by an irreversible step: the aminoacyl-tRNA arrives as a ternary complex with EF-Tu·GTP and is tested once in initial selection; GTP hydrolysis then commits the complex, and after the release of EF-Tu·GDP the tRNA is tested a second time (proofreading) before it can enter the peptidyl transferase center. Because the second test is independent of the first and made possible by the energy of GTP hydrolysis, the discriminations multiply, up to about $10^{-2} \times 10^{-2} = 10^{-4}$; induced fit of the decoding center increases the difference between cognate and near-cognate tRNAs further (kinetic proofreading, [7.2.19](/7.2.19), [6.3.18](/6.3.18)). The cost is the GTP hydrolyzed for each near-cognate tRNA rejected after hydrolysis, and some correct aminoacyl-tRNAs discarded along with wrong ones, which also slows elongation.
