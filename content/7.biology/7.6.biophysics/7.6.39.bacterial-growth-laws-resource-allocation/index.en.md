---
title: Bacterial Growth Laws and Resource Allocation
description: "Quantitative laws of bacterial growth and the economics behind them. Balanced exponential growth; Monod's law and the chemostat with its washout. The Schaechter–Maaløe–Kjeldgaard observations; ribosomes making ribosomes and the first growth law; proteome sectors, the second growth law under translation inhibition and the linear cost of useless protein; overlapping replication rounds and cell size. Proteome allocation as an optimization with the optimum at the intersection of two capacity limits; flux-controlled regulation through ppGpp and the response to nutrient shifts; testing optimality with flux balance and with the cost and benefit of the lac proteins. Overflow metabolism as efficient proteome allocation. Growth rate as fitness."
---

A bacterium in a rich medium does little besides grow: *Escherichia coli* in a good broth at $37\,^\circ\mathrm{C}$ doubles every $20$ minutes, and in that time it must duplicate every one of its three million proteins, its chromosome and its envelope. Because growth is the dominant activity, the composition of a growing bacterium is not arbitrary. Measurements over six decades have revealed simple, nearly linear relations between the growth rate and the amounts of **ribosomes**, of metabolic enzymes, of DNA and of mass per cell. These are the **bacterial growth laws**, and they are among the few quantitative laws in biology that hold across conditions and can be derived from a model with a handful of parameters, in the way that the gas laws follow from a simple picture of molecules. This chapter derives them from the economics of the **proteome**: a cell has a fixed amount of protein to spend, ribosomes make all of it (including more ribosomes), and the allocation between the machinery that makes protein and the machinery that feeds it determines how fast the cell can grow.

The chapter belongs to the "search for principles" of quantitative biology (SH 21.3), and its central question is an optimality question: do cells allocate their resources as well as possible, and if so, how do they know where the optimum is? The molecular biology of translation and the first growth law in its simplest form are in [7.2.19](/7.2.19#sec-19.8.5), the stringent response by which ppGpp controls ribosome synthesis in [7.2.20](/7.2.20), the coordination of growth and division in eukaryotic and bacterial cells in [7.3.22](/7.3.22#sec-22.4), and the metabolic pathways and their regulation in [7.1](/7.1). **Flux balance analysis**, which predicts optimal metabolic fluxes from the stoichiometry of the metabolic network, is developed in [7.6.34](/7.6.34) and used here. The physiology and ecology of microbial growth are the subject of microbiology ([7.11](/7.11)), and the general theory of design principles in networks belongs to systems biology ([7.9](/7.9)).

## 39.1. Exponential Growth and Its Limits

### 39.1.1. Balanced Growth

A culture of bacteria inoculated into fresh medium passes through a lag phase, in which cells adjust their enzymes to the new conditions, an exponential phase, a stationary phase when a nutrient runs out or waste accumulates, and eventually a phase of death. The exponential phase is the reproducible state on which quantitative physiology is built.

**Definition 39.1.1 (Balanced Growth)** A population is in **balanced growth** if every extensive property of the culture (cell number, total protein, RNA, DNA, the amount of each enzyme) increases exponentially at the same rate $\lambda$: $X(t) = X(0)\mathrm{e}^{\lambda t}$, with **doubling time** $\tau = \ln 2/\lambda$ (Campbell 1957).

In balanced growth all intensive properties, such as the RNA per protein, the mass per cell, the fraction of the proteome devoted to any enzyme, are constant in time; they depend only on the conditions, and they can be compared across conditions as functions of $\lambda$. This is what makes the growth rate a natural coordinate for physiology. Balanced growth is reached only after several generations in a constant environment, usually by repeated dilution of the culture so that it stays at low density. Growth rates are quoted per hour: $\lambda = 2.08\,\mathrm{h^{-1}}$ for a $20$-minute doubling, $0.69\,\mathrm{h^{-1}}$ for one hour.

### 39.1.2. Monod's Law

How does the growth rate depend on the concentration of the limiting nutrient? Monod (1942, 1949) measured it for *E. coli* on various sugars and found a hyperbola.

**Formula 39.1.1 (Monod's Law)** In balanced growth limited by a single substrate at concentration $s$,

$$
\lambda(s) = \lambda_{\max}\frac{s}{K_s + s}, \tag{39.1}
$$
where $\lambda_{\max}$ is the growth rate at saturating substrate and $K_s$ the concentration giving half of it. The biomass produced per unit of substrate consumed, the yield $Y$, is approximately constant, so the substrate is consumed at the rate $\lambda x/Y$ by a biomass concentration $x$.

The functional form is that of the **Michaelis–Menten equation**, and the analogy is not accidental: for a sugar taken up by a **transporter** that saturates, the growth rate is proportional to the uptake flux, which is hyperbolic in the external concentration. For *E. coli* growing on glucose, $K_s$ is in the micromolar range, so that the growth rate is nearly independent of the glucose concentration down to a few micromolar, and in a batch culture growth stops abruptly when the glucose is exhausted. Monod's law is a description of the uptake step; it says nothing about why $\lambda_{\max}$ is what it is, which is the question of 39.2. When two sugars are present, *E. coli* uses the preferred one first and switches to the second after a lag, the diauxie that led Monod to the lac **operon** ([7.2.11](/7.2.11)).

### 39.1.3. The Chemostat

In a batch culture the substrate changes continuously and balanced growth holds only transiently. The **chemostat** (Monod 1950; Novick and Szilard 1950) fixes the growth rate instead: fresh medium with substrate concentration $s_0$ flows into a well-mixed vessel at rate $F$, and culture flows out at the same rate, so that the dilution rate $D = F/V$ removes cells and substrate at the rate $D$ per unit volume.

**Formula 39.1.2 (Chemostat Steady State)** With Monod kinetics, the biomass $x$ and the substrate $s$ in the vessel obey

$$
\frac{\mathrm{d}x}{\mathrm{d}t} = (\lambda(s) - D)\,x, \qquad \frac{\mathrm{d}s}{\mathrm{d}t} = D(s_0 - s) - \frac{\lambda(s)}{Y}x. \tag{39.2}
$$
For $D < D_{\mathrm{c}} = \lambda_{\max}s_0/(K_s + s_0)$ the stable steady state has

$$
\lambda(s^*) = D, \qquad s^* = \frac{K_sD}{\lambda_{\max} - D}, \qquad x^* = Y(s_0 - s^*); \tag{39.3}
$$
for $D \ge D_{\mathrm{c}}$ the only steady state is washout, $x^* = 0$, $s^* = s_0$.

At steady state the cells must grow exactly as fast as they are diluted, so the experimenter sets the growth rate by setting the pump. The substrate in the vessel adjusts to whatever concentration makes $\lambda(s^*) = D$; remarkably, $s^*$ does not depend on the feed concentration $s_0$, which only determines how many cells the vessel supports. The linear stability of the nontrivial steady state follows from the Jacobian of Eq. (39.2) ([2.4](/2.4)): both eigenvalues are negative when $D < D_{\mathrm{c}}$, and at $D = D_{\mathrm{c}}$ the two steady states exchange stability in a transcritical bifurcation. The chemostat also selects: a mutant with a slightly lower $K_s$ grows faster than $D$ at the residual $s^*$ of the resident and displaces it, so that long chemostat cultures evolve towards better scavengers, and two species limited by the same substrate cannot coexist (the competitive exclusion principle in its simplest form, [7.19](/7.19)).

![Monod's law and the chemostat. A: growth rate against substrate concentration (Formula 39.1.1, λ_max = 1 per hour, K_s = 0.1 mM, an illustrative value; on a logarithmic axis the hyperbola is a sigmoid with its midpoint at K_s). B: steady states of a chemostat fed with 5 mM substrate as functions of the dilution rate (Formula 39.1.2, yield 0.09 g of dry mass per millimole): the biomass (green) stays nearly constant until it collapses at washout, the residual substrate (dashed, right axis) rises steeply as D approaches λ_max, and the productivity D x* peaks just below washout. C: numerical solution of Eq. (39.2) after inoculation at D = 0.5 per hour: the biomass grows exponentially until it has drawn the substrate down to s*, then stays at its steady state](./plots/monod-chemostat.py)

## 39.2. The Growth Laws

### 39.2.1. Composition Depends on the Growth Rate

Schaechter, Maaløe and Kjeldgaard (1958) grew *Salmonella* Typhimurium in some twenty media of different quality, at growth rates from about $0.4$ to $2.8$ doublings per hour, and measured cell mass, RNA, DNA and the number of nuclei per cell in balanced growth. Two regularities emerged. First, the composition depended only on the growth rate, not on which medium produced it: two different media giving the same $\lambda$ gave the same cells. Second, the RNA content per cell mass increased linearly with the growth rate, and the mass per cell increased exponentially with it. Since most of the RNA (about $85\,\%$) is ribosomal, the first observation says that fast-growing cells are packed with ribosomes; the second, which turned out to reflect the timing of DNA replication (39.2.4), says that fast-growing cells are larger.

### 39.2.2. Ribosomes Making Ribosomes

The linear relation between ribosome content and growth rate follows from the fact that ribosomes make all proteins. Let $M$ be the total protein mass of the culture, $M_R$ the mass of ribosomal proteins (and the proteins that work with them), and $\phi_R = M_R/M$ the ribosomal fraction of the proteome. Each ribosome that is actively translating adds amino acids at the elongation rate $k_{\mathrm{el}}$, so

$$
\frac{\mathrm{d}M}{\mathrm{d}t} = k_{\mathrm{el}}N_R^{\mathrm{act}}\,m_{\mathrm{aa}},
$$
with $N_R^{\mathrm{act}}$ the number of active ribosomes and $m_{\mathrm{aa}}$ the mass of an amino acid. Writing $N_R^{\mathrm{act}} = (M_R - M_R^0)/m_R$, where $m_R$ is the protein mass of one ribosome (about $7500$ amino acids in *E. coli*, [7.2.19](/7.2.19#sec-19.8.5)) and $M_R^0$ accounts for ribosomes that are not translating, and dividing by $M$:

**Formula 39.2.1 (First Growth Law)** In balanced growth,

$$
\lambda = \kappa_t\,(\phi_R - \phi_R^0), \qquad \kappa_t = \frac{k_{\mathrm{el}}m_{\mathrm{aa}}}{m_R} = \frac{k_{\mathrm{el}}}{L_R}, \tag{39.4}
$$
where $L_R$ is the number of amino acids in the proteins of one ribosome and $\phi_R^0$ the fraction of the proteome in inactive ribosomes. When the growth rate is varied by the nutrient quality of the medium, $\phi_R$ is a linear function of $\lambda$ with slope $1/\kappa_t$ (Scott, Gunderson, Mateescu, Zhang and Hwa 2010).

The ribosome is an autocatalyst, and the first growth law is the statement that the growth rate of an autocatalytic system is its catalytic rate times the fraction of the system that is catalyst. With $k_{\mathrm{el}} \approx 20$ amino acids per second, $L_R = 7500$ gives $\kappa_t \approx 9.6\,\mathrm{h^{-1}}$ in units of the ribosomal protein fraction. Even a cell made of nothing but ribosomes could not grow faster than this (doubling time $4.3$ minutes); real cells have $\phi_R \approx 0.3$ at the fastest growth and double in $20$ minutes.

**Example 39.2.1 (Reading the Elongation Rate from the Slope)** Scott and colleagues measured the RNA/protein mass ratio $r$, which is proportional to $\phi_R$ ($\phi_R = \rho r$ with $\rho \approx 0.76$ for *E. coli*), and found $r = r_0 + \lambda/\kappa_t$ with $r_0 \approx 0.087$ and $\kappa_t \approx 4.5\,\mathrm{h^{-1}}$ in units of $r$. To convert, note that about $86\,\%$ of the RNA is rRNA and that one ribosome carries $4566$ nt of rRNA, about $1.5\times10^6\,\mathrm{Da}$, while an average amino acid residue weighs $110\,\mathrm{Da}$. The number of ribosomes per amino acid of protein is then $0.86r\times110/(1.5\times10^6) = 6.3\times10^{-5}r$, and $\lambda = k_{\mathrm{el}}\times6.3\times10^{-5}(r - r_0)$. The measured $\kappa_t = 4.5\,\mathrm{h^{-1}}$ thus corresponds to $k_{\mathrm{el}} = 4.5/(6.3\times10^{-5}\times3600\,\mathrm{s\,h^{-1}}) \approx 20$ amino acids per second, consistent with direct measurements of the elongation rate in fast growth. The offset $r_0$ means that a cell growing very slowly still keeps a reserve of about a tenth of its maximal ribosome content. Dai and colleagues (2016) showed that at slow growth the elongation rate itself falls (to about $8$ amino acids per second) and that part of the ribosomes are inactive, so that $\phi_R^0$ is a reserve that allows a quick response when conditions improve.

### 39.2.3. Proteome Sectors and the Second and Third Laws

The first law describes one side of the economy. The ribosomes must also be fed: amino acids, nucleotides and energy are made by metabolic enzymes and transporters, which also take up proteome. Scott and colleagues partitioned the proteome into three sectors.

**Definition 39.2.1 (Proteome Allocation Model)** In the **proteome allocation** model of bacterial growth, the proteome is divided into a ribosomal sector R (ribosomes and translation factors, fraction $\phi_R$), a metabolic sector P (enzymes and transporters that supply the precursors of protein synthesis, fraction $\phi_P$) and a sector Q of housekeeping proteins whose fraction $\phi_Q$ does not change with the growth rate, so that

$$
\phi_R + \phi_P = 1 - \phi_Q \equiv \phi_{\max}. \tag{39.5}
$$
In balanced growth the flux of precursors supplied by the P sector equals the flux consumed by the R sector: $\lambda = \kappa_t(\phi_R - \phi_R^0) = \kappa_n(\phi_P - \phi_P^0)$, where the **nutritional capacity** $\kappa_n$ measures how much precursor flux a unit of P-sector protein delivers in the given medium.

Eliminating $\phi_P$ with Eq. (39.5) and absorbing $\phi_P^0$ into $\phi_{\max}$, the nutrient side reads $\lambda = \kappa_n(\phi_R^{\max} - \phi_R)$, with $\phi_R^{\max} = \phi_{\max} - \phi_P^0$ the largest ribosomal fraction the cell could have.

**Formula 39.2.2 (The Growth Laws)** In the proteome allocation model,

$$
\phi_R = \phi_R^0 + \frac{\lambda}{\kappa_t} \quad \text{(nutrient quality varied)}, \qquad \phi_R = \phi_R^{\max} - \frac{\lambda}{\kappa_n} \quad \text{(translation inhibited)}, \tag{39.6}
$$
and the growth rate is

$$
\lambda = \frac{\kappa_t\kappa_n}{\kappa_t + \kappa_n}\,(\phi_R^{\max} - \phi_R^0). \tag{39.7}
$$
Expressing a protein that is useless for growth at fraction $\phi_U$ of the proteome reduces $\phi_R^{\max}$ and $\phi_{\max}$ by $\phi_U$ and lowers the growth rate linearly, $\lambda(\phi_U) = \lambda(0)(1 - \phi_U/\phi_{\mathrm{c}})$, with $\phi_{\mathrm{c}} = \phi_R^{\max} - \phi_R^0$ independent of the medium.

The second law is what happens when the translational capacity $\kappa_t$ is lowered by a sublethal dose of an antibiotic that slows the ribosome, such as chloramphenicol. To keep up the supply-demand balance, cells make more ribosomes, and in a given medium $\phi_R$ rises as the growth rate falls, along a line of slope $-1/\kappa_n$ that extrapolates to the same $\phi_R^{\max}$ (measured as $r_{\max} \approx 0.65$) for all media. The growth rate of Eq. (39.7) has the form of two resistances in series: $1/\lambda = (1/\kappa_t + 1/\kappa_n)/(\phi_R^{\max} - \phi_R^0)$, the time per unit of growth being the sum of the time to make protein from precursors and the time to make precursors from nutrients. A cell is fast only if both capacities are high. The third law, the linear cost of useless protein with an intercept near $\phi_{\mathrm{c}} \approx 0.48$ in every medium, was confirmed by expressing β-galactosidase from an inducible plasmid; it measures the cost of any protein in the currency of growth, about a $2\,\%$ loss of growth rate per percent of the proteome.

![The bacterial growth laws from the proteome allocation model (Formula 39.2.2 with r = RNA/protein in place of the ribosomal fraction, r₀ = 0.087, r_max = 0.65, κ_t = 4.5 per hour without drug). A: filled circles are balanced growth in five media of increasing nutrient quality κ_n; they lie on the first-law line of slope 1/κ_t (dashed). In each medium, increasing doses of a translation inhibitor (open squares, κ_t lowered step by step) move the cell up a line of slope −1/κ_n towards r_max: the second law. B: the third law, the linear decrease of growth with the proteome fraction of a useless protein, with the same intercept for all media. C: the cell-cycle side of the growth laws (C = 40 min, D = 20 min): at doubling times shorter than C + D replication rounds overlap, so that a newborn cell carries several origins of replication, 2^((C+D)/τ); the termini grow only as 2^(D/τ), and the ratio of origins to termini, 2^(C/τ), is what marker-frequency sequencing measures](./plots/growth-laws.py)

Finer partitions of the proteome, into six sectors with distinct responses to carbon, nitrogen and translational limitation, were later measured by quantitative proteomics (Hui, Silverman, Chen and colleagues 2015), and they obey the same linear logic: each sector responds linearly to the growth rate in each type of limitation, with signs and slopes that reveal which sector is "the bottleneck" in each case.

### 39.2.4. Growth and the Cell Cycle

The exponential dependence of cell mass on growth rate has a different origin. In *E. coli* at $37\,^\circ\mathrm{C}$, replicating the $4.6\,\mathrm{Mb}$ chromosome takes $C \approx 40\,\mathrm{min}$ (two forks at about $1000\,\mathrm{bp\,s^{-1}}$ each, [7.2.6](/7.2.6)), and the time from the end of replication to division is $D \approx 20\,\mathrm{min}$, both nearly independent of the growth rate above about one doubling per hour. How can a cell divide every $20$ minutes if it needs $60$ minutes from the start of replication to division? Cooper and Helmstetter (1968) showed that it starts new rounds of replication before the previous ones are finished: multifork replication.

**Formula 39.2.3 (Cooper–Helmstetter Model)** If each round of replication is initiated a fixed time $C + D$ before the division that it ends with, a newborn cell growing with doubling time $\tau$ contains on average $2^{(C+D)/\tau}$ origins of replication and $2^{D/\tau}$ termini. If, in addition, initiation occurs when the cell mass per origin reaches a fixed value (Donachie 1968), the mass of a newborn cell is

$$
m_{\mathrm{birth}} = m_{\mathrm{i}}\,2^{(C+D)/\tau} = m_{\mathrm{i}}\,\mathrm{e}^{\lambda(C+D)}. \tag{39.8}
$$

This is the exponential law of Schaechter, Maaløe and Kjeldgaard, with the slope of $\ln m$ against $\lambda$ equal to $C + D \approx 1\,\mathrm{h}$, close to what they found. Single-cell measurements in microfluidic devices have since shown that *E. coli* controls its size by adding a constant mass between birth and division, the **adder** ([7.3.22](/7.3.22#sec-22.4.2)), which is consistent with a constant initiation mass per origin, and that the added size scales with the growth rate in the same exponential way (Taheri-Araghi and colleagues 2015; Si and colleagues 2019). The growth laws of the proteome and the timing of replication are thus two faces of the same physiology: a faster-growing cell is larger, has more chromosomes in progress and more ribosomes per unit of mass.

## 39.3. Optimal Allocation

### 39.3.1. The Optimum at the Corner

The proteome allocation model contains a choice. The cell decides, through the regulation of transcription, what fraction $\chi_R$ of its newly made protein is ribosomal; in balanced growth $\phi_R = \chi_R$. Whatever it chooses, its growth rate is limited by both capacities.

**Proposition 39.3.1 (Optimal Ribosome Allocation)** For fixed $\kappa_t$, $\kappa_n$, $\phi_R^0$ and $\phi_R^{\max}$, the balanced growth rate as a function of the allocation $\phi_R$ is

$$
\lambda(\phi_R) = \min\{\kappa_t(\phi_R - \phi_R^0),\ \kappa_n(\phi_R^{\max} - \phi_R)\},
$$
and it is maximal at the allocation where the two capacities are equal, $\phi_R^* = (\kappa_n\phi_R^{\max} + \kappa_t\phi_R^0)/(\kappa_t + \kappa_n)$, with the growth rate of Eq. (39.7).

**Proof** If the cell makes more ribosomes than the nutrient sector can feed, the ribosomes are starved and growth is limited by the supply, $\lambda = \kappa_n(\phi_R^{\max} - \phi_R)$, which decreases with $\phi_R$; if it makes fewer, precursors accumulate and growth is limited by translation, $\lambda = \kappa_t(\phi_R - \phi_R^0)$, which increases with $\phi_R$. The minimum of an increasing and a decreasing linear function is maximal where they cross. $\square$

The measured first-law line is the locus of these optima as the medium changes: the cells allocate their proteome as the model says they should to grow as fast as possible (SH 21.3.3). The prediction is not trivial: a cell that kept a fixed allocation, set for one medium, would grow more slowly than possible in all others, as panel B of the next figure shows.

### 39.3.2. Regulation by Flux Sensing

The optimum depends on $\kappa_n$, which the cell cannot measure directly: it does not know the "quality" of a medium. Scott, Klumpp, Mateescu and Hwa (2014) showed that the cell does not need to. It suffices to sense the balance between supply and demand through the pool of amino acids (charged tRNA): when the supply exceeds the demand, the pool rises and the cell makes more ribosomes; when the demand exceeds the supply, the pool falls, uncharged tRNA enters the A site of ribosomes, RelA makes ppGpp, and ppGpp represses the synthesis of rRNA and ribosomal proteins ([7.2.20](/7.2.20)). A simple model captures this.

**Formula 39.3.1 (Flux-Controlled Regulation)** Let $a$ be the amino-acid pool per unit protein, translation run at $\lambda = \kappa_t\,g(a)\,(\phi_R - \phi_R^0)$ with $g(a) = a/(a + K)$, the pool be filled by the P sector and drained by translation and dilution, and the ribosomal fraction relax towards the regulated synthesis fraction $\chi_R(a)$:

$$
\frac{\mathrm{d}a}{\mathrm{d}t} = \kappa_n(\phi_R^{\max} - \phi_R) - \lambda(1 + a), \qquad \frac{\mathrm{d}\phi_R}{\mathrm{d}t} = \lambda\,(\chi_R(a) - \phi_R), \qquad \chi_R(a) = \phi_R^0 + (\phi_R^{\max} - \phi_R^0)\frac{a}{a + K_\chi}. \tag{39.9}
$$

The steady state satisfies $\phi_R = \chi_R(a^*)$ with $a^*$ the pool at which supply and demand balance. With a regulation function of suitable shape (here $K_\chi = 0.3$ against $K = 0.05$), the steady-state growth rate is within $1\,\%$ of the best possible allocation over a thirtyfold range of $\kappa_n$: the regulation finds the optimum without knowing $\kappa_n$, because the pool is an internal readout of the mismatch between the two capacities. The dynamics after a nutrient upshift show the same logic: the pool jumps, ribosome synthesis increases at once (the immediate rise of rRNA synthesis after an upshift was observed by Kjeldgaard, Maaløe and Schaechter in 1958), the ribosomal fraction overshoots slightly, and the growth rate settles at the new optimum within about one doubling time. A cell with frozen allocation would accumulate precursors and grow barely faster than before. The same framework explains the kinetics of growth transitions and the lag after a downshift as the time needed to rebuild the depleted sector (Erickson and colleagues 2017).

![Optimal allocation and the regulation that finds it. A: the two capacity constraints in the plane of ribosomal fraction and growth rate: growth cannot exceed the translational capacity (black line) nor the nutritional capacity of the medium (colored lines for three media); the feasible region (shaded) is largest at its corner, where the cell grows fastest (circles, Proposition 39.3.1). B: steady-state growth rate against nutrient quality in the dynamic model of Formula 39.3.1: flux-controlled regulation (green) follows the best possible allocation (thick gray) closely, whereas an allocation frozen at its optimum for one medium (dashed) wastes most of the potential of richer media. C: nutrient upshift from κ_n = 0.6 to 3 per hour at time zero: with regulation, the ribosomal fraction (dotted, scaled by 4) rises and the growth rate overshoots and settles at the new optimum; with allocation frozen, the cell gains little](./plots/allocation.py)

### 39.3.3. Testing Optimality

Two other tests of the hypothesis that bacteria grow optimally come from different directions.

At the level of metabolism, **flux balance analysis** ([7.6.34](/7.6.34)) predicts, from the stoichiometry of the metabolic network of *E. coli* and the measured uptake rates of substrate and oxygen, the fluxes that maximize the production of biomass. Ibarra, Edwards and Palsson (2002) found that *E. coli* growing on glycerol was initially far from the predicted line of optimal growth in the plane of glycerol and oxygen uptake, and that after about $700$ generations of laboratory evolution it had moved onto it, in each of several replicate populations. On glucose it was already near the line. Flux balance gives a line, not a point: it cannot predict the uptake rates themselves, which are limited by the proteome, and the two approaches are combined in models that add proteome costs to flux balance (constrained allocation flux balance and related methods).

At the level of a single protein, Dekel and Alon (2005) measured the cost and the benefit of the lac proteins in *E. coli* growing on glycerol with varying lactose.

**Formula 39.3.2 (Cost and Benefit of a Protein)** With $Z$ the expression of the lac operon relative to the fully induced wild type, the relative growth rate in the presence of lactose at concentration $L$ is approximately

$$
\frac{\lambda(Z, L)}{\lambda_0} = 1 - \frac{\eta_0Z}{1 - Z/M} + \delta Z\frac{L}{K + L}, \tag{39.10}
$$
with a cost that rises faster than linearly as the expression approaches a capacity $M$, and a benefit proportional to the lactose uptake (fitted values about $\eta_0 = 0.02$, $M = 1.8$, $\delta = 0.17$, $K = 0.4\,\mathrm{mM}$). The optimal expression $Z^*(L)$ maximizes this function; it is zero when $\delta L/(K + L) < \eta_0$.

The cost term is the third growth law seen from a single operon, with the nonlinearity that appears when an operon takes a large share of the transcriptional and translational resources. Dekel and Alon then let cells evolve for about $500$ generations at fixed lactose concentrations with the operon fully induced (by IPTG), and found that the expression level evolved towards the value $Z^*(L)$ predicted from the measured cost and benefit, increasing at high lactose and decreasing at low lactose. The prediction is that of an optimum on a **fitness landscape** whose shape is set by physiology; the evolutionary dynamics by which the population climbs it is the subject of [7.6.41](/7.6.41).

## 39.4. Overflow Metabolism

A puzzling feature of fast-growing cells is that they waste carbon. *E. coli* growing aerobically on glucose oxidizes it completely to $\ce{CO2}$ at slow growth, but above a growth rate of about $0.76\,\mathrm{h^{-1}}$ it excretes acetate, although respiration yields several times more ATP per glucose than **fermentation** to acetate. Yeast growing fast on glucose ferments to ethanol in the presence of oxygen (the Crabtree effect), and many proliferating mammalian cells, including cancer cells, convert glucose to lactate in the presence of oxygen (the **Warburg effect**, [7.1.18](/7.1.18)).

**Definition 39.4.1 (Overflow Metabolism)** **Overflow metabolism** is the excretion of partially oxidized products (acetate, ethanol, lactate) by cells growing in the presence of oxygen, in which a fermentative pathway carries part of the carbon flux although the respiratory pathway gives a higher yield of ATP per substrate.

For *E. coli* the acetate excretion rate is zero below a threshold growth rate and increases linearly above it, whatever the carbon source that sets the growth rate. Basan, Hui, Okano and colleagues (2015) explained this threshold-linear law by the proteome. Respiration yields more ATP per glucose, but its enzymes (the **citric acid cycle** and the **respiratory chain**) are large and slow, so that it yields less ATP per unit time per unit of proteome than fermentation, which needs only **glycolysis** and a few enzymes. When the cell grows slowly, protein is not limiting and the carbon-efficient pathway wins; when it grows fast, the biomass sector (ribosomes and biosynthesis) takes so much of the proteome that the energy demand can only be met by adding the proteome-efficient pathway.

**Formula 39.4.1 (Overflow from Proteome Allocation)** Let the energy demand of growth be $e\lambda$, met by respiration and fermentation fluxes $J_r + J_f = e\lambda$ whose enzymes take proteome fractions $J_r/\varepsilon_r$ and $J_f/\varepsilon_f$ ($\varepsilon_f > \varepsilon_r$: fermentation is more proteome-efficient), and let the biomass sector take $b\lambda$ of a total budget $\phi_{\max}$:

$$
\frac{J_r}{\varepsilon_r} + \frac{J_f}{\varepsilon_f} \le \phi_{\max} - b\lambda.
$$
Minimizing the carbon uptake (respiration having the higher yield) gives $J_f = 0$ for $\lambda \le \lambda_{\mathrm{c}} = \phi_{\max}/(e/\varepsilon_r + b)$, and above the threshold

$$
J_f = \frac{e\lambda/\varepsilon_r - (\phi_{\max} - b\lambda)}{1/\varepsilon_r - 1/\varepsilon_f}, \tag{39.11}
$$
a linear increase of fermentation with growth rate, accompanied by a decrease of respiration.

The model predicts more than the threshold. Expressing a useless protein lowers the threshold growth rate, because it shrinks the budget; inhibiting translation, which enlarges the ribosomal sector at a given growth rate, also lowers it. Both predictions were confirmed, and proteomic measurements showed that the respiratory enzymes indeed deliver about half the ATP flux per unit of protein that the fermentative ones do. The interpretation of the **Warburg effect** along the same lines, as a response to proteome or membrane-area constraints in fast-proliferating cells rather than as a defect of mitochondria, is plausible but debated, because mammalian cells are rarely limited by growth rate in the way bacteria are.

![Two optimization problems of bacterial physiology. A: cost and benefit of the lac proteins (Formula 39.3.2 with the fitted parameters of Dekel and Alon): without lactose any expression is a pure cost; at 0.1 mM lactose the optimum is a low expression with a negligible gain; at higher concentrations the optimal expression (circles) approaches and passes the wild-type fully induced level, and overexpression beyond it is punished by the rising cost. B: overflow metabolism from proteome allocation (Formula 39.4.1 with λ_c = 0.76 per hour): below the threshold the cell respires all its glucose; above it, the proteome budget is exhausted (dashed line reaches its maximum) and fermentation, which delivers twice the energy flux per unit of protein, takes over a rising share of the energy supply, so that acetate excretion grows linearly with the growth rate while respiration declines](./plots/cost-benefit.py)

## 39.5. Growth Rate as Fitness

In a well-mixed culture in exponential growth, the strain that grows faster takes over: two strains with growth rates $\lambda_1 > \lambda_2$ change their ratio as $\mathrm{e}^{(\lambda_1 - \lambda_2)t}$, so that the **selection coefficient** per generation of the slower strain is $s = (\lambda_2 - \lambda_1)/\lambda_1$ ([7.4.23](/7.4.23#sec-23.3.1)). The resolution of such competitions is remarkable. A difference of $1\,\%$ in growth rate, invisible in a growth curve, changes the ratio of two strains by a factor $\mathrm{e}$ in a hundred generations, a few weeks of serial transfer. By the third growth law, a protein that takes $0.1\,\%$ of the proteome and does nothing costs about $0.2\,\%$ of growth, which a large population sees clearly (an **effective population size** of $10^8$ makes selection effective against differences of $10^{-8}$, [7.4.23](/7.4.23#sec-23.6)). This is why the expression levels of most proteins can be expected to be near their optima, as Dekel and Alon found for lac, and why the economics of the proteome is a credible principle rather than a metaphor.

Growth rate is not the only component of fitness. In nature bacteria spend much of their time in stationary phase, starving, and survive by switching to a different proteome: the stress response, persistence and sporulation, each a costly insurance against bad times. The trade-off between growth and survival is itself quantitative: cells that grow faster die faster when starved, and the "bet hedging" of persisters, a small fraction of slowly growing cells that survive antibiotics, is optimal when environments change unpredictably. These strategies and their ecology belong to microbiology ([7.11](/7.11)) and evolutionary biology ([7.10](/7.10)). The long-term evolution experiment of Lenski, in which twelve populations of *E. coli* have been propagated daily since 1988, shows that the fitness of a population in a constant environment keeps increasing for tens of thousands of generations, with no plateau yet in sight; the optimization of growth is a process, and the optima of this chapter are the points towards which it moves.

## Summary

- Balanced growth (Definition 39.1.1): all extensive quantities grow at one rate $\lambda = \ln 2/\tau$; intensive properties depend only on $\lambda$.
- Monod's law $\lambda = \lambda_{\max}s/(K_s + s)$ (Formula 39.1.1) describes substrate limitation; in a chemostat the dilution rate sets the growth rate, $s^* = K_sD/(\lambda_{\max} - D)$, with washout at $D_{\mathrm{c}}$ (Formula 39.1.2).
- Growth laws (Formulas 39.2.1–39.2.2):

  | Law | Relation | Origin |
  |---|---|---|
  | first | $\phi_R = \phi_R^0 + \lambda/\kappa_t$ (nutrients varied) | ribosomes make all protein, $\kappa_t = k_{\mathrm{el}}/L_R$ |
  | second | $\phi_R = \phi_R^{\max} - \lambda/\kappa_n$ (translation inhibited) | supply must match demand |
  | combined | $\lambda = \frac{\kappa_t\kappa_n}{\kappa_t+\kappa_n}(\phi_R^{\max} - \phi_R^0)$ | two capacities in series |
  | third | $\lambda = \lambda_0(1 - \phi_U/\phi_{\mathrm{c}})$ | useless protein shrinks the budget |
  | size | $m_{\mathrm{birth}} \propto \mathrm{e}^{\lambda(C+D)}$ | multifork replication, constant initiation mass (Formula 39.2.3) |

- Optimality: the growth rate is maximal where translational and nutritional capacities balance (Proposition 39.3.1); flux sensing through the amino-acid pool and ppGpp finds this optimum without knowing the medium (Formula 39.3.1). Evolution experiments moved *E. coli* to the flux-balance optimum on glycerol and the lac expression to its cost–benefit optimum (Formula 39.3.2).
- Overflow metabolism (Definition 39.4.1) follows from proteome efficiency: fermentation is cheaper in protein per ATP flux, so above $\lambda_{\mathrm{c}} \approx 0.76\,\mathrm{h^{-1}}$ acetate excretion rises linearly (Formula 39.4.1).
- Growth rate is a sensitive measure of fitness: a $1\,\%$ difference decides a competition in a hundred generations.

## Questions

1. An *E. coli* culture in balanced growth doubles every $40$ minutes. What is its growth rate, and by what factor does its protein increase in $3$ hours?

   **Answer** $\lambda = \ln 2/(2/3\,\mathrm{h}) = 1.04\,\mathrm{h^{-1}}$. In $3\,\mathrm{h}$ the protein (like every extensive quantity) increases by $\mathrm{e}^{3.12} = 2^{4.5} = 22.6$.

2. A chemostat with $\lambda_{\max} = 1.2\,\mathrm{h^{-1}}$ and $K_s = 2\,\mu\mathrm{M}$ is fed with $1\,\mathrm{mM}$ glucose. Find the residual glucose at $D = 0.3$ and $0.9\,\mathrm{h^{-1}}$, and the washout dilution rate. Why is the chemostat a good way to select mutants with better transporters?

   **Answer** $s^* = K_sD/(\lambda_{\max} - D)$: at $D = 0.3$, $s^* = 2\times0.3/0.9 = 0.67\,\mu\mathrm{M}$; at $D = 0.9$, $s^* = 2\times0.9/0.3 = 6\,\mu\mathrm{M}$. Washout at $D_{\mathrm{c}} = 1.2\times1000/1002 = 1.198\,\mathrm{h^{-1}}$. The residual substrate is far below $K_s$ at moderate dilution, so the growth rate is nearly proportional to $\lambda_{\max}s/K_s$; a mutant with a lower $K_s$ or a higher affinity transporter grows faster than $D$ at the resident's $s^*$, increases, draws $s$ down further and drives the resident out. The chemostat thus selects directly for scavenging ability at low concentration, and repeated sweeps of such mutants have been observed in long chemostat cultures.

3. Using $k_{\mathrm{el}} = 16$ amino acids per second and $7500$ amino acids of ribosomal protein per ribosome, compute the maximal growth rate of a cell made only of active ribosomes, and the ribosomal fraction needed for a $30$-minute doubling if $\phi_R^0 = 0.05$.

   **Answer** $\kappa_t = 16\times3600/7500 = 7.7\,\mathrm{h^{-1}}$, a doubling time of $\ln 2/7.7 = 0.090\,\mathrm{h} = 5.4\,\mathrm{min}$. For $\tau = 30\,\mathrm{min}$, $\lambda = 1.39\,\mathrm{h^{-1}}$ and $\phi_R = 0.05 + 1.39/7.7 = 0.23$. (Ribosome-associated proteins such as **elongation factors**, included in the R sector, raise the real fraction somewhat.)

4. A strain grows at $1.0\,\mathrm{h^{-1}}$ in glucose medium. A plasmid makes it express a nonfunctional protein at $10\,\%$ of its proteome. Predict its growth rate (with $\phi_{\mathrm{c}} = 0.48$), and the **selection coefficient** of a plasmid-free segregant. How many generations until segregants are $99\,\%$ of a culture started with one segregant per $10^6$ cells?

   **Answer** $\lambda = 1.0\times(1 - 0.1/0.48) = 0.79\,\mathrm{h^{-1}}$. A segregant grows at $1.0\,\mathrm{h^{-1}}$, so it has a growth-rate advantage $\Delta\lambda = 0.21\,\mathrm{h^{-1}}$, a selection coefficient $s = 0.21/0.79 = 0.26$ per generation of the plasmid carriers. The ratio of segregants to plasmid carriers grows as $\mathrm{e}^{0.21\,\mathrm{h^{-1}}\,t}$; it must go from $10^{-6}$ to $99$, a factor $10^8$, which takes $t = \ln10^8/0.21 = 88\,\mathrm{h}$, about $100$ doublings of the segregants. This is why plasmids carrying burdensome genes are lost without selection, and why expression strains are grown with antibiotics.

5. In the proteome allocation model, show that a translation inhibitor that halves $\kappa_t$ always reduces the growth rate by less than half, and compute the reduction for $\kappa_n = \kappa_t$.

   **Answer** From Eq. (39.7), $\lambda \propto \kappa_t\kappa_n/(\kappa_t + \kappa_n)$. Halving $\kappa_t$ gives $\lambda'/\lambda = \frac{(\kappa_t/2)\kappa_n/(\kappa_t/2 + \kappa_n)}{\kappa_t\kappa_n/(\kappa_t + \kappa_n)} = \frac{\kappa_t + \kappa_n}{\kappa_t + 2\kappa_n}$, which lies between $1/2$ (when $\kappa_n \gg \kappa_t$) and $1$ (when $\kappa_n \ll \kappa_t$). For $\kappa_n = \kappa_t$, $\lambda'/\lambda = 2/3$. The cell compensates by making more ribosomes (the second law): the antibiotic's effect is buffered most in poor media, where growth is limited by nutrients rather than translation. This is one reason why antibiotic efficacy depends on the growth conditions (Greulich, Scott, Evans and Allen 2015).

6. With $C = 40\,\mathrm{min}$ and $D = 20\,\mathrm{min}$, how many **replication forks** are active in a newborn *E. coli* cell doubling every $20$ minutes? What does this imply for the **copy number** of genes near the origin compared with those near the terminus?

   **Answer** Origins per newborn cell: $2^{(C+D)/\tau} = 2^3 = 8$; termini: $2^{D/\tau} = 2$. Each of the two chromosome copies therefore carries four origins, that is, two generations of replication rounds in progress, with $2 + 4 = 6$ forks on each, $12$ in the cell. Along each chromosome the copy number of a locus doubles every $\tau$ of replication time from terminus to origin, so a gene near the origin is present at $2^{C/\tau} = 4$ times the dosage of a gene near the terminus. Fast-growing bacteria place their highly expressed genes, such as the rRNA operons, near the origin, which exploits this dosage effect.

7. (Data analysis) You measure the RNA/protein ratio $r$ and the growth rate in five media and find $(\lambda, r) = (0.4, 0.17), (0.7, 0.24), (1.0, 0.31), (1.3, 0.37), (1.6, 0.44)$ (λ in h⁻¹). Then, in the medium with $\lambda = 1.0$, you add chloramphenicol and find $(0.75, 0.39)$ and $(0.5, 0.47)$. Estimate $\kappa_t$, $r_0$, $\kappa_n$ for this medium and $r_{\max}$.

   **Answer** A least-squares fit of the first five points gives slope $0.225\,\mathrm{h}$ and intercept $0.08$: $\kappa_t = 1/0.225 = 4.4\,\mathrm{h^{-1}}$, $r_0 = 0.08$. In the chloramphenicol series of that medium the slope is $(0.47 - 0.31)/(0.5 - 1.0) = -0.32\,\mathrm{h}$ (all three points: $0.31$, $0.39$, $0.47$ at $\lambda = 1.0$, $0.75$, $0.5$ fall on one line), so $\kappa_n = 3.1\,\mathrm{h^{-1}}$, and $r_{\max} = 0.31 + 1.0\times0.32 = 0.63$. Check: Eq. (39.7) gives $\lambda = 4.4\times3.1/(7.5)\times(0.63 - 0.08) = 1.00\,\mathrm{h^{-1}}$.

8. Explain in one paragraph why the existence of a sharp growth-rate threshold for acetate excretion argues against explanations of overflow metabolism based on a saturated respiratory capacity of individual enzymes, and for an explanation based on the proteome budget. What experiment discriminates them?

   **Answer** If respiration were limited by a fixed maximal capacity of the respiratory enzymes, overflow would start at a fixed glucose uptake flux regardless of how the growth rate was set, and the threshold would not move when unrelated proteins were expressed. In the proteome model the threshold is set by the competition for protein between the energy sector and the biomass sector; it depends on the total budget and on how much protein growth needs. Expressing a useless protein (which reduces the budget) or adding a translation inhibitor (which increases the protein needed for biosynthesis at a given growth rate) lowers the threshold growth rate in the proteome model but not in the capacity model. Basan and colleagues did exactly these experiments and found that the threshold moved as the proteome model predicts; quantitative proteomics further showed that respiratory enzymes give less ATP flux per unit protein.

9. (Open question) Suppose that you want to engineer *E. coli* to produce a heterologous protein at $20\,\%$ of its proteome while keeping its growth rate as high as possible in a fixed medium. Using the growth laws, discuss what you could change and what the limits are.

   **Answer** By the third law the burden reduces growth by $\phi_U/\phi_{\mathrm{c}} \approx 0.2/0.48 = 42\,\%$ if the protein simply displaces other sectors in proportion. Options: express it only after growth (two-phase production, with an inducer or a growth-phase promoter), so that biomass accumulates first; reduce the Q-like sectors that are unnecessary in the production medium (deleting unneeded genes, flagella and motility, which take several percent of the proteome), which raises $\phi_{\max}$; improve the nutritional capacity $\kappa_n$ by a richer medium so that a smaller P sector suffices; and avoid translational stress (codon usage, mRNA stability) that would effectively lower $\kappa_t$. Limits: the R and P sectors cannot both be shrunk without lowering $\lambda$ (Eq. (39.7)); overexpression may trigger stress responses and overflow, which waste carbon (Formula 39.4.1); and any burden creates selection for nonproducing mutants, so production strains are genetically unstable over many generations, as computed in Question 4.

10. Monod's law and the Michaelis–Menten equation have the same form. Give one reason why this is expected, and one reason why the $K_s$ of growth need not equal the $K_{\mathrm{M}}$ of the transporter.

    **Answer** Expected: if growth is limited by uptake of the substrate and uptake is mediated by a saturable transporter, the uptake flux, and hence the growth rate at fixed yield, follows $J_{\max}s/(K_{\mathrm{M}} + s)$. Not equal: the cell regulates the number of transporters with the growth conditions (at low substrate it makes more, raising the uptake at a given $s$, an effect that lowers the apparent $K_s$); growth also depends on downstream steps that can saturate first, so that the growth rate saturates before the transporter does (lowering $\lambda_{\max}$ and $K_s$ together); and several transporters with different affinities may operate in parallel (for glucose, the PTS and the Mgl/Gal systems). The apparent $K_s$ is a property of the whole cell's allocation, not of one protein.
