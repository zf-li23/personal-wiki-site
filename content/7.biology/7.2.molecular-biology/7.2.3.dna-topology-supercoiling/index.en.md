---
title: DNA Topology and Supercoiling
description: Linking number, twist and writhe of a closed duplex and the relation Lk = Tw + Wr; linking difference, superhelical density and topoisomers; the free energy and torque of supercoiling; negative supercoiling and strand separation, nucleosomes and the twin-domain model; type I and type II topoisomerases, gyrase and their inhibitors; the helix–coil model of torque-induced melting solved by transfer matrices; the winding problem at a replication fork.
---

The two strands of the **double helix** are wound around each other about once every $10.5\,\mathrm{bp}$, so a human chromosome of $10^8\,\mathrm{bp}$ contains about ten million turns. Every process that separates the strands (replication, transcription, repair, recombination) must therefore deal with this winding. When the ends of a duplex cannot rotate freely, because the molecule is a closed circle or because its ends are held in large protein complexes and chromatin loops, the number of times the strands wind around each other is fixed, and changing the winding in one place forces a compensating change elsewhere. This chapter treats the geometry and topology of such constrained DNA (3.1), the biological consequences of the underwinding that all cells maintain (3.2), the enzymes that change the winding (3.3), a statistical-mechanical model of how underwinding opens DNA at particular sequences (3.4), and the problem posed by a moving replication fork (3.5). The double helix itself and its melting are described in [7.1.11](/7.1.11); the packaging of DNA around histones follows in [7.2.4](/7.2.4).

## 3.1. Topological Invariants of a Closed Duplex

### 3.1.1. Linking Number

A DNA molecule whose two strands are both covalently closed circles, with no break in either backbone, is called covalently closed circular DNA (cccDNA); plasmids, the chromosomes of most bacteria, mitochondrial DNA and many viral genomes are of this kind. Topology, the study of properties unchanged by continuous deformation, applies to such molecules: bending, twisting and thermal motion are continuous deformations, whereas breaking a strand is not.

**Definition 3.1.1 (Linking Number)** The **linking number** $\mathrm{Lk}$ of a closed duplex is the number of times one strand winds around the other: if one strand is taken as the boundary of a surface, $\mathrm{Lk}$ is the number of times the other strand passes through that surface, counted with sign. By convention $\mathrm{Lk}$ is positive for a right-handed duplex.

Equivalently, $\mathrm{Lk}$ is the Gauss linking number of the two closed curves $\boldsymbol{r}_1, \boldsymbol{r}_2$ traced by the strands,

$$
\mathrm{Lk} = \frac{1}{4\pi}\oint\!\!\oint \frac{(\boldsymbol{r}_1 - \boldsymbol{r}_2)\cdot(\mathrm{d}\boldsymbol{r}_1\times\mathrm{d}\boldsymbol{r}_2)}{\lvert \boldsymbol{r}_1 - \boldsymbol{r}_2\rvert^3},
$$
or, more practically, half the number of signed crossings of the two strands in any projection. It is always an integer, and it cannot change unless at least one strand is broken. If a strand is nicked, the strands can rotate freely about each other and $\mathrm{Lk}$ is undefined. A linear DNA whose ends are anchored (in a chromatin loop, or between two proteins that bind tightly) behaves topologically like a closed circle.

### 3.1.2. Twist and Writhe

The linking number is a topological quantity; the shape of the molecule is described by two geometric quantities.

**Definition 3.1.2** The **twist** $\mathrm{Tw}$ of a closed duplex is the number of turns that one strand makes around the axis of the double helix. The **writhe** $\mathrm{Wr}$ is the number of times the axis of the duplex crosses over itself, counted with sign and averaged over all directions of projection. Neither needs to be an integer.

Twist measures the coiling of the strands around the axis; writhe measures the coiling of the axis in space, which is what the eye sees as supercoiling. A duplex lying flat in a plane has $\mathrm{Wr} = 0$.

**Theorem 3.1.1 (Călugăreanu–White–Fuller)** For a closed duplex,

$$
\mathrm{Lk} = \mathrm{Tw} + \mathrm{Wr}. \tag{3.1}
$$

The theorem, proved by Călugăreanu (1959) and White (1969) and introduced into DNA research by Fuller (1971), says that twist and writhe can be exchanged into each other by deformations of the molecule, but their sum is fixed. Underwinding the strands (lowering $\mathrm{Tw}$) at fixed $\mathrm{Lk}$ must be compensated by writhe, and vice versa.

![Linking number = twist + writhe. A: a relaxed planar circle with Lk = Tw = 12 and Wr = 0 (the two strands are drawn in two shades of blue; the darker passes in front). B: the same circle after a strand has been broken, two turns removed and the break resealed; with the axis kept flat the two turns are lost from the twist, Lk = Tw = 10, and the helix is underwound and strained. C: the same molecule (Lk = 10) with the strain taken up by the axis crossing over itself twice: the twist returns to 12 and two negative crossings give Wr = −2, an interwound or plectonemic supercoil. Going from A to B requires breaking a strand; going from B to C requires none.](./plots/topology-ribbons.py)

### 3.1.3. Linking Difference and Superhelical Density

**Definition 3.1.3** A closed duplex is **relaxed** when it has the linking number that it would have if it lay flat and unstrained under the given conditions, $\mathrm{Lk}_0 = N/h$, where $N$ is the number of base pairs and $h$ the helical repeat ($h \approx 10.5\,\mathrm{bp}$ per turn for B-DNA in physiological solution). The **linking difference** is $\Delta\mathrm{Lk} = \mathrm{Lk} - \mathrm{Lk}_0$, and the **superhelical density** is

$$
\sigma = \frac{\Delta\mathrm{Lk}}{\mathrm{Lk}_0}.
$$
DNA with $\Delta\mathrm{Lk} \neq 0$ is **supercoiled**: negatively supercoiled (underwound) if $\Delta\mathrm{Lk} < 0$, positively supercoiled (overwound) if $\Delta\mathrm{Lk} > 0$. Molecules that differ only in linking number are **topoisomers**.

$\mathrm{Lk}_0$ is not a topological invariant: it depends on temperature, ionic conditions and bound **ligands** through the helical repeat $h$. The superhelical density is independent of length and is the quantity that cells regulate. Circular DNA purified from bacteria or **eukaryotes** has $\sigma \approx -0.05$ to $-0.07$. Part of this underwinding is taken up by DNA wrapped around proteins; the unconstrained superhelical density in living *E. coli* cells, measured by the rate of crosslinking by psoralen, is about $-0.025$.

**Example 3.1.1** A relaxed closed circle of $2100\,\mathrm{bp}$ has $\mathrm{Lk}_0 = 2100/10.5 = 200$. Removing two turns gives $\mathrm{Lk} = 198$, $\Delta\mathrm{Lk} = -2$ and $\sigma = -2/200 = -0.01$. A $4200\,\mathrm{bp}$ circle with $\mathrm{Lk} = 374$ has $\mathrm{Lk}_0 = 400$ and $\sigma = -26/400 = -0.065$, a typical value for a plasmid isolated from bacteria; with $\mathrm{Lk} = 412$ the same circle would be positively supercoiled with $\sigma = +0.03$.

Topoisomers can be separated by agarose gel electrophoresis: the more writhe a circle has, the more compact it is and the faster it migrates, and topoisomers differing by one unit of $\mathrm{Lk}$ form a ladder of bands. Such gels give the most direct measurement of the helical repeat of DNA in solution.

**Example 3.1.2 (The helical repeat from topoisomer ladders)** Circles of $3990$, $3995$ and $4011\,\mathrm{bp}$ are relaxed completely with a type I topoisomerase (3.3) and run on a gel. The $3990$ and $4011\,\mathrm{bp}$ circles migrate together, but the $3995\,\mathrm{bp}$ circle, only $5\,\mathrm{bp}$ longer than the first, migrates faster. With $h = 10.5$, $\mathrm{Lk}_0 = 380.0$ for $3990\,\mathrm{bp}$ and $382.0$ for $4011\,\mathrm{bp}$, so both can be completely relaxed with integer $\mathrm{Lk}$; for $3995\,\mathrm{bp}$, $\mathrm{Lk}_0 = 380.48$ and every topoisomer has $\lvert\Delta\mathrm{Lk}\rvert \geq 0.48$, hence some writhe and a faster migration. The pattern repeats with a period of $10.5\,\mathrm{bp}$ in length, which is the helical repeat.

Intercalating dyes lower the twist without breaking a strand. Each ethidium ion that slides between two **base pairs** unwinds the helix by about $26^\circ$, so at fixed $\mathrm{Lk}$ it raises the writhe by $26/360 \approx 0.072$. Adding ethidium to a negatively supercoiled circle first relaxes it and then makes it positively supercoiled: a $5\,\mathrm{kb}$ plasmid at $\sigma = -0.06$ ($\Delta\mathrm{Lk} \approx -29$) is relaxed by about $29/0.072 \approx 400$ bound ethidium ions. Low concentrations of intercalators (chloroquine) are added to gels to shift the topoisomers of a sample into the range where they are resolved.

## 3.2. Biological Consequences of Negative Supercoiling

### 3.2.1. Stored Free Energy and Torque

Supercoiling stores elastic free energy. When a nicked circle is resealed by ligase, or relaxed by a topoisomerase, the topoisomers produced have a Boltzmann distribution of $\Delta\mathrm{Lk}$ that is Gaussian with a variance proportional to $N$. From these distributions (Depew and Wang, 1975; Pulleyblank et al., 1975), the free energy of supercoiling of a circle longer than about $2\,\mathrm{kb}$ is

$$
G_{\mathrm{sc}} = \frac{K\,RT}{N}\,(\Delta\mathrm{Lk})^2, \qquad K \approx 1100, \tag{3.2}
$$
and correspondingly $\langle(\Delta\mathrm{Lk})^2\rangle = N/(2K)$ for the relaxed population: for $N = 4000$, the standard deviation of $\Delta\mathrm{Lk}$ is about $1.3$. Written in terms of $\sigma$, $G_{\mathrm{sc}} = (K/h^2)\,RT\,N\sigma^2 \approx 10\,RT\,N\sigma^2$: the energy grows with the square of the superhelical density and in proportion to length. The derivative of $G_{\mathrm{sc}}$ with respect to the angle of rotation $2\pi\,\Delta\mathrm{Lk}$ is a **torque** on the DNA,

$$
\tau = \frac{1}{2\pi}\frac{\partial G_{\mathrm{sc}}}{\partial \Delta\mathrm{Lk}} = \frac{K k_{\mathrm{B}}T}{\pi h}\,\sigma \approx 140\,\sigma\ \mathrm{pN\,nm}. \tag{3.3}
$$

![The energetics of supercoiling. A: the topoisomers formed when circles of 3990 bp and 3995 bp are relaxed, from the Boltzmann distribution of Eq. (3.2); for 3990 bp the relaxed linking number Lk0 = 380.00 is an integer and the most abundant topoisomer has ΔLk = 0, whereas for 3995 bp (Lk0 = 380.48, dashed lines) the two most abundant topoisomers have ΔLk ≈ ±0.5, so every molecule carries some writhe (Example 3.1.2). B: free energy of supercoiling of a 5 kb plasmid (solid, left axis) and the torque of Eq. (3.3) (dashed, right axis) as functions of the superhelical density; the band marks the range of purified cellular DNA, where the stored energy is several hundred kilojoules per mole of plasmid and the torque about −7 to −10 pN nm, close to the torque at which B-DNA begins to melt.](./plots/supercoiling-energy.py)

**Example 3.2.1** A $5\,\mathrm{kb}$ plasmid at $\sigma = -0.06$ has $\Delta\mathrm{Lk} = -0.06\times5000/10.5 \approx -29$ and, by Eq. (3.2), $G_{\mathrm{sc}} \approx 1100\times(29)^2/5000\,RT \approx 180\,RT \approx 470\,\mathrm{kJ\,mol^{-1}}$. Removing one more turn costs $\partial G_{\mathrm{sc}}/\partial\Delta\mathrm{Lk} = 2K RT\,\lvert\Delta\mathrm{Lk}\rvert/N \approx 13\,RT$; conversely, an event that unwinds the helix by one turn (opening about $10\,\mathrm{bp}$, or binding a protein that untwists the DNA) is favored by about $13\,RT \approx 33\,\mathrm{kJ\,mol^{-1}}$. This is comparable to the free energy needed to separate ten base pairs, which is why negative supercoiling promotes strand separation.

### 3.2.2. Strand Separation and Alternative Structures

Because underwinding favors any change that reduces twist, negatively supercoiled DNA opens more easily: promoters form open complexes ([7.2.10](/7.2.10)), origins melt to load helicases ([7.2.7](/7.2.7)), and recombination proteins pair single strands with duplexes ([7.2.9](/7.2.9)) more readily on supercoiled templates. The same free energy stabilizes alternative structures that unwind the helix: **cruciforms** at palindromic sequences, left-handed **Z-DNA** at alternating purine–pyrimidine tracts, and triple-helical H-DNA at mirror-repeat polypurine tracts ([7.1.11](/7.1.11)). These structures are rare in relaxed DNA and appear above a threshold of negative superhelical density. Section 3.4 turns this into a model.

Organisms that live at high temperature face the opposite problem. Hyperthermophilic archaea and bacteria have reverse gyrase, an enzyme that introduces positive supercoils (3.3), and their DNA is relaxed or slightly overwound, which counters thermal melting.

### 3.2.3. Plectonemic and Toroidal Supercoils; Nucleosomes

Writhe takes two forms. In plectonemic (interwound) supercoils the axis wraps around itself, often in branched structures; this is the shape of supercoiled DNA free in solution, and its axis is about 40 % as long as the DNA. In toroidal (solenoidal) supercoils the axis winds in a spiral, as when DNA is wrapped around a protein. The two forms interconvert, and a left-handed toroidal turn contributes negative writhe, like a negative interwound crossing.

In eukaryotic chromatin the DNA wraps 1.65 left-handed toroidal turns around each histone octamer ([7.2.4](/7.2.4)). The negative supercoiling of DNA isolated from eukaryotic cells is almost entirely of this restrained kind: removing the histones from the $5.2\,\mathrm{kb}$ minichromosome of the virus SV40, which carries about 24 nucleosomes, leaves about 24 negative supercoils. Each nucleosome thus restrains a linking difference of about $-1$, rather than the $-1.65$ expected from the number of turns, because the DNA on the nucleosome is slightly overtwisted (about $10.2\,\mathrm{bp}$ per turn) compared with DNA in solution; this mismatch is sometimes called the linking-number paradox. Eukaryotes have no gyrase; the nucleosomes provide negative supercoiling, and topoisomerases keep the unrestrained DNA near relaxed. Bacteria restrain part of their supercoiling with abundant nucleoid proteins (HU, H-NS, Fis) and divide their chromosome into some 400 topologically independent domains of about $10\,\mathrm{kb}$, so that a single nick relaxes only one domain.

### 3.2.4. The Twin-Supercoiled-Domain Model and Supercoiling Homeostasis

An RNA polymerase moving along DNA must either rotate around the helix, once per $10.5\,\mathrm{bp}$ transcribed, or turn the DNA. A polymerase dragging a nascent RNA with ribosomes and, in bacteria, membrane proteins being inserted cotranslationally cannot rotate freely. Leroy Liu and James Wang (1987) proposed that it then overwinds the DNA ahead of it and underwinds the DNA behind it, producing positive and negative supercoils in two domains that are removed by different topoisomerases.

![A: the twin-supercoiled-domain model. A transcribing RNA polymerase that cannot rotate around the template overwinds the DNA ahead of it (drawn with a tighter helix; positive supercoils, relaxed by gyrase in bacteria and by topoisomerases I and II in eukaryotes) and underwinds the DNA behind it (looser helix; negative supercoils, relaxed by topoisomerase I). B: the superhelical density of a 50 kb domain ahead of a replication fork moving at 1000 bp per second, starting from σ = −0.06 and conserving the linking number except for removal by topoisomerases at r turns per second. Without topoisomerase activity the domain passes through relaxation within about 3 s and becomes strongly overwound within seconds; removing turns at half the rate at which the fork unwinds them only delays this, and only a removal rate equal to the unwinding rate (v/h = 95 turns per second) keeps the linking difference constant (σ then becomes more negative because the remaining duplex shortens).](./plots/twin-domain-fork.py)

The model was confirmed with plasmids in *E. coli*: in mutants lacking topoisomerase I, plasmids transcribing a membrane-protein gene become hypernegatively supercoiled, and when gyrase is inhibited they become positively supercoiled. Transcription is thus itself a major source of supercoiling, and supercoils generated by one gene influence the initiation of its neighbors.

The overall superhelical density of bacterial DNA is held near its set point by negative feedback on the topoisomerase genes: relaxation of DNA stimulates transcription of the gyrase genes *gyrA* and *gyrB* and lowers that of *topA*, which encodes topoisomerase I, whereas excess negative supercoiling does the opposite. Because the promoters of many genes respond to supercoiling, $\sigma$ acts as a global regulator that changes with growth phase, temperature and **osmolarity**.

## 3.3. Topoisomerases

### 3.3.1. A Covalent Mechanism

**Definition 3.3.1 (Topoisomerase)** A **topoisomerase** is an enzyme that changes the linking number of DNA by transiently breaking one strand (**type I topoisomerases**, changing $\mathrm{Lk}$ in steps of 1) or both strands (**type II topoisomerases**, changing $\mathrm{Lk}$ in steps of 2), passing DNA through the break or letting it rotate, and resealing the break.

All topoisomerases break DNA by the same chemistry: an active-site tyrosine attacks a phosphodiester bond and becomes covalently linked to one end of the broken strand by a phosphotyrosine bond, leaving a free hydroxyl at the other end. Because the energy of the phosphodiester bond is conserved in the phosphotyrosine bond, resealing is simply the reverse reaction and requires no ATP; the enzyme holds both ends throughout, so the cleaved DNA is never released. Type II enzymes use ATP, not to cut or reseal, but to drive the large conformational changes that carry one duplex through another.

| Type | Mechanism | Enzymes | Activity |
|---|---|---|---|
| IA | Single-strand break (5′-phosphotyrosine); the other strand is passed through the gap; needs a single-stranded region | Bacterial topo I and III; eukaryotic Top3α, Top3β; reverse gyrase | Relaxes only negative supercoils ($\Delta\mathrm{Lk} = +1$ per cycle); topo III resolves hemicatenanes; reverse gyrase uses ATP to introduce positive supercoils |
| IB | Single-strand break (3′-phosphotyrosine); the free end rotates around the intact strand (controlled rotation) | Eukaryotic Top1, poxvirus topoisomerase | Relaxes positive and negative supercoils, several turns per break; no ATP |
| IC | As IB, different fold | Topo V (*Methanopyrus*) | Relaxation |
| IIA | Double-strand break with a 4-nt stagger (5′-phosphotyrosines); a second duplex is passed through; ATP | Gyrase, topo IV (bacteria); Top2α, Top2β (eukaryotes) | Gyrase introduces negative supercoils; topo IV and Top2 relax both signs and decatenate ($\Delta\mathrm{Lk} = \pm2$) |
| IIB | As IIA, different structure | Topo VI (archaea, plants) | Relaxation, decatenation |

### 3.3.2. Gyrase and Topoisomerase IV

**Definition 3.3.2 (DNA Gyrase)** **DNA gyrase** is the type IIA topoisomerase of bacteria (a GyrA₂GyrB₂ tetramer) that uses ATP hydrolysis to introduce negative supercoils into DNA.

Gyrase wraps about $130\,\mathrm{bp}$ of DNA around itself so that the duplex crosses itself with positive writhe. It cuts the duplex at one end of the wrap (the gate segment) and passes the other end (the transported segment) through the break, inverting the positive crossing into a negative one: $\Delta\mathrm{Lk} = -2$ per cycle, at the cost of two ATP. This wrapping makes gyrase unique among type II enzymes: the others act on crossings that the DNA presents to them and so relax supercoils, but gyrase chooses its own crossing and can drive DNA away from equilibrium. Gyrase also removes positive supercoils ahead of replication forks and transcribing polymerases. Topoisomerase IV, its paralogue (ParC₂ParE₂), prefers to act on crossings between two different molecules and is the main decatenase: it unlinks the two daughter chromosomes at the end of each round of replication ([7.2.7](/7.2.7)). In eukaryotes topoisomerase II performs this function and is essential for the separation of sister chromatids at mitosis.

### 3.3.3. Topoisomerases as Drug Targets

Because the cleavage complex is a broken DNA held together by the enzyme, drugs that stabilize it turn a topoisomerase into a DNA-damaging agent. Such topoisomerase poisons are distinguished from catalytic inhibitors that merely block the enzyme.

| Drug class | Target | Action | Use |
|---|---|---|---|
| Quinolones (ciprofloxacin, levofloxacin) | Gyrase and topo IV | Poisons: trap the cleavage complex, producing double-strand breaks when forks collide with it | Antibacterial |
| Aminocoumarins (novobiocin) | GyrB ATPase | Catalytic inhibitors | Antibacterial (now little used) |
| Camptothecins (topotecan, irinotecan) | Top1 | Poisons: bind at the nick and block religation | Anticancer |
| Etoposide, doxorubicin, mitoxantrone | Top2 | Poisons | Anticancer |

Rapidly dividing cells are most sensitive to poisons, since replication forks convert trapped single-strand nicks and cleavage complexes into lethal double-strand breaks. The same mechanism explains a side effect: Top2 poisons occasionally cause chromosomal translocations and secondary leukemias.

## 3.4. The Helix–Coil Model of Torque-Induced Melting

### 3.4.1. The Model

Negative supercoiling does not open DNA uniformly. It opens AT-rich regions first, and the question of where a supercoiled molecule melts is answered by a classical model of statistical mechanics. We treat each base pair as either helical or open.

**Definition 3.4.1 (Helix–Coil Transition)** The **helix–coil transition** is the cooperative conversion of a helical polymer into a disordered coil; for DNA it is the separation of the strands into single-stranded "coil", and in the helix–coil (zipper) model each base pair $n = 1, \dots, N$ is in one of two states $x_n \in \{\mathrm{h}, \mathrm{c}\}$.

The model assigns to each configuration $x = (x_1, \dots, x_N)$ a statistical weight that is a product of local factors:

$$
W(x) = \prod_{n:\,x_n = \mathrm{h}} s_n \times \sigma_{\mathrm{nuc}}^{\,b(x)}, \qquad s_n = \mathrm{e}^{\Delta E_n/RT}, \qquad \sigma_{\mathrm{nuc}} = \mathrm{e}^{-J/RT}, \tag{3.4}
$$
where $\Delta E_n = E_{\mathrm{c}} - E_{\mathrm{h}}$ is the free energy needed to open base pair $n$ (so $s_n$ is the weight of the helical state relative to the open state), $b(x)$ is the number of boundaries between helical and open stretches, and $J$ is the free-energy penalty for each boundary. For example $W(\mathrm{chhhc})/W(\mathrm{ccchh}) = \sigma_{\mathrm{nuc}}^2 s_2s_3s_4/(\sigma_{\mathrm{nuc}}\,s_4s_5)$. The boundary penalty expresses **cooperativity**: the stacking lost at the edges of an open region is paid once per boundary, so opening one long bubble is much cheaper than opening many short ones. The probability of a configuration is $W(x)/Z$, where the **partition function** $Z = \sum_x W(x)$ ([6.3.10](/6.3.10)) is a sum over $2^N$ configurations.

Torque enters through the twist. If the open strands are taken to have zero twist, opening one base pair removes $\theta_0 = 2\pi/h$ of twist; a negative torque of magnitude $\tau$ then does work $\tau\theta_0$ per opened pair, and the cost of opening becomes

$$
\Delta E_n' = \Delta E_n - N_{\mathrm{A}}\,\tau\,\theta_0. \tag{3.5}
$$
We use a two-state parameter set for physiological conditions: $\Delta E_{\mathrm{AT}} = 3.60\,\mathrm{kJ\,mol^{-1}}$, $\Delta E_{\mathrm{GC}} = 7.82\,\mathrm{kJ\,mol^{-1}}$ and $J = 18.8\,\mathrm{kJ\,mol^{-1}}$ at $T = 310\,\mathrm{K}$. In relaxed DNA, $s_{\mathrm{AT}} = 4.0$ and $s_{\mathrm{GC}} = 21$: every pair prefers the helix. A torque of $13\,\mathrm{pN\,nm}$ contributes $N_{\mathrm{A}}\tau\theta_0 = 4.7\,\mathrm{kJ\,mol^{-1}}$, giving $s'_{\mathrm{AT}} = 0.66$ and $s'_{\mathrm{GC}} = 3.4$, while $\sigma_{\mathrm{nuc}} = 6.8\times10^{-4}$ (with $h = 10$, as in the original form of this exercise, $s'_{\mathrm{AT}} = 0.60$ and $s'_{\mathrm{GC}} = 3.09$). Under this torque AT pairs prefer to be open, GC pairs still prefer the helix, and whether a region opens depends on its composition and length.

### 3.4.2. Exact Solution by Transfer Matrices

The sum over $2^N$ configurations can be done in $O(N)$ operations because the weight (3.4) couples only neighboring base pairs. Let $a_n(x)$ be the total weight of all configurations of pairs $1, \dots, n$ that end with $x_n = x$. Adding pair $n$ multiplies the weight by $s_n$ if it is helical and by $\sigma_{\mathrm{nuc}}$ if its state differs from that of pair $n-1$:

$$
\begin{bmatrix} a_n(\mathrm{h}) & a_n(\mathrm{c}) \end{bmatrix} = \begin{bmatrix} a_{n-1}(\mathrm{h}) & a_{n-1}(\mathrm{c}) \end{bmatrix} M_n, \qquad
M_n = \begin{bmatrix} s_n & \sigma_{\mathrm{nuc}} \\ \sigma_{\mathrm{nuc}}\,s_n & 1 \end{bmatrix}, \tag{3.6}
$$
with $a_1 = (s_1, 1)$; the rows of $M_n$ refer to the state of pair $n-1$ and the columns to that of pair $n$. The partition function is $Z = a_N(\mathrm{h}) + a_N(\mathrm{c})$. Symmetrically, let $b_n(x)$ be the total weight of pairs $n+1, \dots, N$ given $x_n = x$; then $b_N = (1, 1)^{\mathsf T}$ and $b_{n-1} = M_n b_n$. Since the weight factorizes at $n$,

$$
\mathbb{P}(x_n = \mathrm{c}) = \frac{a_n(\mathrm{c})\,b_n(\mathrm{c})}{Z}. \tag{3.7}
$$

**Algorithm 3.4.1 (Base-Pair Opening Probabilities)** Given the sequence, compute $s_n$ from Eq. (3.5) for every pair. Run the forward recursion (3.6) from $n = 1$ to $N$ and the backward recursion from $n = N$ to $1$, normalizing each vector to unit sum after every step to avoid overflow (the normalization constants cancel in Eq. (3.7)). Then evaluate Eq. (3.7) for every $n$.

The configurations of the chain form a **Markov chain** along the sequence, and the algorithm is the forward–backward algorithm of hidden Markov models ([4.6.8](/4.6.8#sec-8.3)) applied to a two-state chain; the course slides formulate the same computation as a backward pass of conditional probabilities $\mathbb{P}(x_n \mid x_{n-1})$ followed by a forward pass of marginal probabilities (Poland, 1978). In physics the model is the one-dimensional Ising model in a site-dependent field.

### 3.4.3. Where Supercoiled DNA Opens

![Torque-induced opening calculated exactly with the helix–coil model (Algorithm 3.4.1) for a synthetic sequence of 5000 bp: random DNA with 50 % GC containing an AT-rich block of 400 bp (89 % AT in the realized sequence) and a shorter one of 90 bp (83 % AT). A: GC fraction in a 50 bp window. B: probability that each base pair is open. Relaxed DNA (τ = 0) is closed everywhere; at a negative torque of 11.5 pN nm the long AT-rich block opens, and at 13 pN nm the short block opens as well while the 50 % GC background remains closed. C: the mean opening probability of each block as the torque is increased; both open over a narrow range of torque, the shorter block at a higher torque because its two boundaries cost the same as those of the long block but are paid for by fewer AT pairs.](./plots/helix-coil-opening.py)

The calculation shows the two features of melting under torque: it is local and it is cooperative. A rough criterion explains where the thresholds lie. Opening a block of $L$ pairs, of which a fraction $f$ are AT, changes the free energy by $L[f\Delta E'_{\mathrm{AT}} + (1-f)\Delta E'_{\mathrm{GC}}] + 2J$, so the block opens when

$$
\tau > \tau^* = \frac{1}{N_{\mathrm{A}}\theta_0}\left[f\Delta E_{\mathrm{AT}} + (1-f)\Delta E_{\mathrm{GC}} + \frac{2J}{L}\right]. \tag{3.8}
$$
For the long block ($f = 0.89$, $L = 400$) this gives $\tau^* \approx 11.6\,\mathrm{pN\,nm}$, for the short block ($f = 0.83$, $L = 90$) about $13.1\,\mathrm{pN\,nm}$, and for DNA of 50 % GC about $16\,\mathrm{pN\,nm}$, in agreement with the full calculation. For pure AT DNA of great length, $\tau^* \approx 10\,\mathrm{pN\,nm}$: single-molecule experiments, which twist DNA with magnetic tweezers, find that negative torque on **B-DNA** cannot exceed about $-10\,\mathrm{pN\,nm}$ because the DNA melts instead. By Eq. (3.3) such torques correspond to $\sigma \approx -0.07$, the upper end of the range found in cells, so physiological supercoiling places DNA close to the threshold at which its AT-richest regions open.

This is how the cell can use supercoiling to direct melting to particular places. Bacterial and yeast replication origins contain AT-rich duplex-unwinding elements next to the initiator **binding sites**, and calculations of stress-induced duplex destabilization (SIDD), which extend this model by fixing $\mathrm{Lk}$ rather than torque, predict that origins and many promoters are among the most easily opened regions of their genomes. The torque-clamped model is a simplification: in a closed domain the first bubble to open relaxes the supercoiling and so raises the threshold for the next one, which makes opening at one site compete with opening at others.

## 3.5. The Winding Problem at a Replication Fork

The *E. coli* replisome unwinds about $1000\,\mathrm{bp}$ per second, removing $1000/10.5 \approx 95$ helical turns per second from the parental duplex. If the chromosome were free to rotate, its unreplicated part would have to spin at 95 revolutions per second, which is impossible for a molecule millions of base pairs long, folded in a nucleoid and attached to membranes. Instead, the linking number of the unreplicated DNA ahead of the fork is conserved, and as the duplex shortens the same linking number is crowded into fewer base pairs.

For a domain of length $L_0$ ahead of the fork, with initial superhelical density $\sigma_0$ and a fork advancing at speed $v$, and with topoisomerases removing $r$ turns per second,

$$
\sigma(t) = \frac{\mathrm{Lk}(0) - rt}{(L_0 - vt)/h} - 1, \qquad \mathrm{Lk}(0) = \frac{(1+\sigma_0)L_0}{h}. \tag{3.9}
$$
For $L_0 = 50\,\mathrm{kb}$, $\sigma_0 = -0.06$ and $r = 0$, the domain is relaxed when the fork has advanced $3\,\mathrm{kb}$, after $3\,\mathrm{s}$, and reaches $\sigma = +0.06$ after less than $6\,\mathrm{s}$; positive supercoiling of this magnitude would stall the fork (panel B of the figure in 3.2.4). The natural negative supercoiling of the template buys only a few seconds. Sustained replication requires topoisomerases to remove positive turns at the rate the fork creates them, about 95 per second per fork; since gyrase removes two turns per catalytic cycle of roughly a second, many gyrase molecules must act ahead of each fork.

Not all of the strain needs to be removed ahead of the fork. If the replisome rotates, positive supercoils ahead are converted into intertwinings of the two daughter duplexes behind the fork (precatenanes), and replication of a circle ends with two daughter circles linked as a catenane. These links are removed by topoisomerase IV in bacteria and topoisomerase II in eukaryotes (3.3.2); without them the daughter chromosomes cannot be segregated.

## Summary

| Topic | Key points |
|---|---|
| Linking number (Definition 3.1.1) | Integer number of windings of one strand around the other in cccDNA or anchored loops; changes only if a strand breaks |
| Twist, writhe (Definition 3.1.2) | Tw: turns of the strands around the axis; Wr: signed self-crossings of the axis; $\mathrm{Lk} = \mathrm{Tw} + \mathrm{Wr}$ (Theorem 3.1.1); twist and writhe interconvert at fixed Lk |
| Superhelical density (Definition 3.1.3) | $\mathrm{Lk}_0 = N/10.5$, $\Delta\mathrm{Lk} = \mathrm{Lk} - \mathrm{Lk}_0$, $\sigma = \Delta\mathrm{Lk}/\mathrm{Lk}_0$; purified cellular DNA $\sigma \approx -0.05$ to $-0.07$, unconstrained in *E. coli* about $-0.025$; topoisomers resolved by gels, helical repeat $10.5\,\mathrm{bp}$ (Example 3.1.2); ethidium unwinds $26^\circ$ |
| Energy and torque | $G_{\mathrm{sc}} = (1100\,RT/N)(\Delta\mathrm{Lk})^2 \approx 10\,RT\,N\sigma^2$ (Eq. (3.2)); $\tau \approx 140\,\sigma\ \mathrm{pN\,nm}$ (Eq. (3.3)); at $\sigma = -0.06$ unwinding one turn is favored by about $13\,RT$ (Example 3.2.1) |
| Consequences | Negative supercoiling promotes melting of promoters and origins, cruciforms, Z-DNA; reverse gyrase in hyperthermophiles; nucleosomes restrain about $-1$ each; about 400 domains in *E. coli*; twin-domain model of transcription; feedback on *gyrA*, *gyrB*, *topA* |
| Topoisomerases (Definition 3.3.1) | Phosphotyrosine intermediate, no ATP for cutting; type IA (5′, strand passage, relaxes −), IB (3′, rotation), IIA (double-strand passage, ATP, $\pm2$), IIB; gyrase (Definition 3.3.2) introduces negative supercoils by wrapping; topo IV and Top2 decatenate |
| Drugs | Poisons trap cleavage complexes: quinolones (gyrase, topo IV), camptothecins (Top1), etoposide and doxorubicin (Top2); novobiocin is a catalytic inhibitor |
| Helix–coil model (Definition 3.4.1) | Weights $s_n = \mathrm{e}^{\Delta E_n/RT}$, boundary penalty $\sigma_{\mathrm{nuc}} = \mathrm{e}^{-J/RT}$, torque term $\Delta E' = \Delta E - N_{\mathrm{A}}\tau\theta_0$; transfer matrices and forward–backward recursion give exact opening probabilities (Algorithm 3.4.1); threshold torque Eq. (3.8): long AT-rich blocks open near $11$–$12\,\mathrm{pN\,nm}$, B-DNA cannot sustain more than about $-10\,\mathrm{pN\,nm}$ |
| Replication fork | $95$ turns per second removed at $1000\,\mathrm{bp\,s^{-1}}$; Eq. (3.9): a $50\,\mathrm{kb}$ domain is overwound within seconds without topoisomerases; precatenanes and decatenation by topo IV and Top2 |

## Questions

1. A $5250\,\mathrm{bp}$ plasmid isolated from *E. coli* has $\mathrm{Lk} = 470$. Calculate $\Delta\mathrm{Lk}$ and $\sigma$. What happens to $\mathrm{Lk}$, $\mathrm{Tw}$ and $\mathrm{Wr}$ when the plasmid is treated (a) with a type I topoisomerase, (b) with DNA gyrase and ATP, (c) with DNase I to make one nick?

   **Answer** $\mathrm{Lk}_0 = 5250/10.5 = 500$, $\Delta\mathrm{Lk} = -30$, $\sigma = -0.06$. (a) Type I topoisomerases raise $\mathrm{Lk}$ in steps of 1 until the plasmid is relaxed: the population ends with $\mathrm{Lk}$ distributed around $500$ (standard deviation about $1.5$ by Eq. (3.2)), $\mathrm{Tw} \approx 500$, $\mathrm{Wr} \approx 0$. (b) Gyrase lowers $\mathrm{Lk}$ in steps of 2, making the plasmid more negatively supercoiled (to $\sigma$ near $-0.1$ in vitro); the extra linking difference appears mostly as negative writhe. (c) After a nick $\mathrm{Lk}$ is undefined; the strands rotate until the twist is that of relaxed DNA, $\mathrm{Tw} \approx 500$, and the writhe disappears: the nicked circle migrates slowly, as an open circle.

2. Why can type I topoisomerase of *E. coli* relax negative but not positive supercoils, while eukaryotic topoisomerase I relaxes both?

   **Answer** Bacterial topoisomerase I is a type IA enzyme: it binds a transiently single-stranded region, cuts one strand and passes the other strand through the gap. Single-stranded regions exist only in underwound DNA, and each passage increases $\mathrm{Lk}$ by one, so the enzyme stops when the DNA is relaxed. Eukaryotic topoisomerase I is a type IB enzyme that nicks duplex DNA and lets the free end rotate around the intact strand, driven by the torsional stress itself; rotation can go in either direction, so the enzyme relaxes both signs of supercoiling.

3. Ethidium bromide is added in increasing amounts to a negatively supercoiled plasmid, and samples are analyzed by gel electrophoresis without ethidium after its removal, and with ethidium in the gel. Describe the migration of the plasmid in the presence of ethidium as its concentration increases.

   **Answer** Bound ethidium lowers the twist, so at constant $\mathrm{Lk}$ the writhe rises from negative values toward zero and then becomes positive. In the presence of ethidium the plasmid therefore first migrates more slowly as it is relaxed, reaches a minimum mobility when $\mathrm{Wr} \approx 0$ (at about 400 bound molecules for a $5\,\mathrm{kb}$ plasmid at $\sigma = -0.06$), and then migrates faster again as it becomes positively supercoiled. After removal of the dye the original negative supercoiling returns, because $\mathrm{Lk}$ never changed. A nicked circle shows none of these changes.

4. Using Eq. (3.8) with the parameters of 3.4.1, estimate the torque needed to open a $60\,\mathrm{bp}$ tract of pure AT and a $60\,\mathrm{bp}$ tract with 50 % GC. What does the comparison imply about the design of replication origins?

   **Answer** $N_{\mathrm{A}}\theta_0 = 6.02\times10^{23}\times2\pi/10.5 = 3.60\times10^{23}$ per mole and radian, so $1\,\mathrm{kJ\,mol^{-1}}$ corresponds to $2.78\,\mathrm{pN\,nm}$. For pure AT: $3.60 + 2\times18.8/60 = 4.23\,\mathrm{kJ\,mol^{-1}}$, $\tau^* \approx 11.7\,\mathrm{pN\,nm}$. For 50 % GC: $5.71 + 0.63 = 6.34\,\mathrm{kJ\,mol^{-1}}$, $\tau^* \approx 17.6\,\mathrm{pN\,nm}$, far beyond what supercoiling can sustain. A short AT-rich element is therefore the first region to melt in a supercoiled domain; origins place such elements next to the binding sites of initiator proteins, which, by binding and bending DNA, add the remaining free energy needed to open it at exactly that position.

5. Explain why quinolones, which target gyrase, kill bacteria much more effectively than a deletion of the gyrase genes would suggest from simple loss of enzyme, and why the human topoisomerase II is not affected at therapeutic doses.

   **Answer** Quinolones are poisons, not just inhibitors: they bind the gyrase–DNA cleavage complex and prevent religation, converting the enzyme into a source of double-strand breaks that are made permanent when replication forks or polymerases collide with the trapped complexes. A small fraction of trapped enzymes is lethal, whereas loss of activity alone would merely slow replication. The drugs bind at the interface between the DNA and **residues** of GyrA and ParC that differ in eukaryotic topoisomerase II, which is why the human enzyme is much less sensitive; resistance arises mainly by mutations at these residues.
