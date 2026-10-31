---
title: Cell Mechanics, Migration and Mechanosensation
description: "The mechanics of whole cells and tissues: stiffness scales and linear elasticity, cell rheology, measurement by AFM indentation and the Hertz model, micropipette aspiration and traction force microscopy (Boussinesq solution, Fourier-transform traction cytometry), molecular tension sensors, the molecular-clutch model of adhesion and stiffness sensing, durotaxis, mesenchymal and amoeboid migration and the persistent random walk, the gating-spring model and negative stiffness of hair bundles, active amplification near a Hopf bifurcation, collective migration, jamming and models of cell collectives, topological defects, wrinkling and folding of layered tissues, and the nonlinear elasticity of tendon and artery."
---

Cells push, pull and feel. A fibroblast crawling through a wound exerts tens of nanonewtons on its surroundings, a hair cell of the inner ear detects displacements smaller than a nanometer, and a stem cell placed on a soft or a stiff gel chooses a different fate. The previous chapters treated the mechanics of the parts: the flow of water around cells ([7.6.22](/7.6.22)), the elasticity of membranes ([7.6.24](/7.6.24)), the channels that open under tension ([7.6.25](/7.6.25)), the filaments and their polymerization forces ([7.6.26](/7.6.26)), and the motors that pull on them ([7.6.27](/7.6.27)). This chapter puts them together at the scale of the whole cell and of groups of cells. It asks how stiff cells and tissues are and how this is measured (31.1–31.2); how adhesions transmit force and let cells sense the stiffness of their substrate (31.3); what physics governs single-cell migration (31.4); how hair cells convert sub-nanometer motions into electrical signals and amplify them (31.5); how cells migrate collectively and jam (31.6); and what the mechanics of tissues adds (31.7).

The cell biology is in place and is not repeated: the migration cycle, Rho GTPases, lamellipodia and the qualitative clutch are in [7.3.15](/7.3.15#sec-15.5); integrins, focal adhesions, catch bonds and mechanotransduction in [7.3.23](/7.3.23#sec-23.4); mechanosensitive channels in [7.3.5](/7.3.5#sec-5.7). The viscoelasticity of cells, Maxwell and Voigt models and the weak power-law rheology of the cytoplasm are in [7.6.22](/7.6.22#sec-22.7); the Bell model of force-dependent unbinding in [7.6.17](/7.6.17); the mechanics of embryonic tissues, tissue surface tension, vertex models and the rigidity transition are in [7.5.8](/7.5.8); and the theory of active matter, flocking and active nematics, which describes collective cell motion at large scales, is in [7.6.37](/7.6.37).

## 31.1. The Mechanical Cell

### 31.1.1. Forces and Stiffness in Numbers

The forces of cell mechanics span many decades. A single motor or bond develops a few piconewtons, an adhesion of a fibroblast a few nanonewtons, and the whole cell tens to hundreds of nanonewtons. At the other end, a skeletal muscle develops about $0.3\,\mathrm{MPa}$ of cross-sectional area; since fibers act in parallel, a fiber of $50\,\mu\mathrm{m}$ diameter ($2\times10^{-9}\,\mathrm{m^2}$) produces about $0.6\,\mathrm{mN}$, which is the force of some $10^8$ myosin heads in parallel. Dividing the force of a whole muscle by the number of cells it contains, as if every cell bore an equal share of the load in series, underestimates the force per fiber by orders of magnitude: forces add only over the cross-section.

The stiffness of tissues spans eight decades:

| Material | Young's modulus $E$ |
|---|---|
| Brain, bone marrow, fat | $0.1$–$1\,\mathrm{kPa}$ |
| Single cells (cortex, cytoplasm, at $\sim1\,\mathrm{Hz}$) | $0.1$–$10\,\mathrm{kPa}$ |
| Skeletal muscle (resting) | $8$–$17\,\mathrm{kPa}$ |
| Osteoid (newly formed, unmineralized bone matrix) | $25$–$40\,\mathrm{kPa}$ |
| Cartilage | about $1\,\mathrm{MPa}$ |
| Tendon (linear region) | $1$–$2\,\mathrm{GPa}$ |
| Cortical bone | $10$–$20\,\mathrm{GPa}$ |

Cells respond to these differences. Engler, Discher and colleagues (2006) found that mesenchymal stem cells cultured on collagen-coated gels of brain-like, muscle-like and osteoid-like stiffness expressed neuronal, myogenic and osteogenic markers respectively, and that the effect required nonmuscle myosin II: a cell measures stiffness by pulling.

### 31.1.2. Linear Elasticity

For small deformations a homogeneous, isotropic material is described by two constants. A bar stretched by the stress $\sigma$ strains by $\varepsilon = \sigma/E$, with **Young's modulus** $E$, and contracts laterally by $\nu\varepsilon$, with Poisson's ratio $\nu$; the **shear modulus** is $G = E/2(1 + \nu)$ ([5.1.7](/5.1.7)). Most soft tissues and cells are nearly incompressible over the time of a measurement, so $\nu \approx 0.5$ and $E \approx 3G$. Hydrogels used as substrates (polyacrylamide) have $\nu \approx 0.45$–$0.5$. On longer times water flows through the network (poroelasticity), and on all time scales the response depends on rate: cells are viscoelastic, with storage and loss moduli $G'$ and $G''$ that grow as a weak power of frequency, $G^* \propto (\mathrm{i}\omega)^\beta$ with $\beta = 0.1$–$0.3$ ([7.6.22](/7.6.22#sec-22.7.2)). Their stiffness also grows with their internal prestress, roughly in proportion to it, because a tensed network of filaments resists further deformation by its tension, like a guitar string (Wang, Ingber and colleagues 2002), and with strain, because networks of semiflexible filaments stiffen as their filaments are pulled straight.

## 31.2. Measuring Cell Mechanics

### 31.2.1. AFM Indentation and the Hertz Model

The **atomic force microscope** ([7.6.17](/7.6.17)) indents a cell with a tip at the end of a cantilever of known spring constant (typically $0.01$–$0.1\,\mathrm{N\,m^{-1}}$ for cells) and records force against indentation. For a sphere pressed into an elastic half-space the problem was solved by Hertz (1882).

**Definition 31.2.1 (Hertz Contact Model)** In the **Hertz contact model** a rigid sphere of radius $R$ pressed a depth $\delta$ into an elastic, isotropic half-space with Young's modulus $E$ and Poisson's ratio $\nu$, without friction or adhesion, requires the force
$$
F = \frac{4}{3}\,\frac{E}{1 - \nu^2}\,R^{1/2}\delta^{3/2}, \tag{31.1}
$$
and makes contact over a circle of radius $a = \sqrt{R\delta}$. For a conical tip of half-angle $\alpha$ (Sneddon 1965), $F = (2/\pi)\,[E/(1 - \nu^2)]\tan\alpha\,\delta^2$.

The exponent $3/2$ follows from scaling. The contact radius is set by geometry, $a \approx \sqrt{R\delta}$ (a sphere of radius $R$ intersects a plane a depth $\delta$ below its apex in a circle of that radius); the strain under the tip is of order $\delta/a$; the stress is $E\delta/a$; and the force is stress times contact area, $E(\delta/a)a^2 = Ea\delta = ER^{1/2}\delta^{3/2}$. The full solution supplies the factor $4/3$ and the dependence on $\nu$, which enters through the plane-strain modulus $E/(1 - \nu^2)$.

The model applies when the indentation is small compared with the probe radius and with the thickness of the sample (less than about 10–20 % of the thickness; thin regions of a cell appear stiffer because the glass beneath them is felt), when the material is homogeneous and when the measurement is slow compared with its relaxation. Spherical colloidal probes of a few micrometers average over the cortex and the cytoplasm; sharp pyramidal tips map the stiffness of the cortex and of individual stress fibers. In practice the contact point is not known and is fitted together with $E$.

**Example 31.2.1 (A force curve)** A bead of radius $2.5\,\mu\mathrm{m}$ indents a cell with $E = 2\,\mathrm{kPa}$ and $\nu = 0.5$ by $1\,\mu\mathrm{m}$. By Eq. (31.1), $F = \frac{4}{3}(2000/0.75)(1.58\times10^{-3})(10^{-9})\,\mathrm{N} = 5.6\,\mathrm{nN}$. With a cantilever of $0.05\,\mathrm{N\,m^{-1}}$ this force deflects the cantilever by $110\,\mathrm{nm}$, easily measured by the optical lever; thermal fluctuations of the cantilever, $\sqrt{k_{\mathrm{B}}T/k} = 0.3\,\mathrm{nm}$, set the noise floor.

![AFM indentation and the Hertz model (Definition 31.2.1). A: force–indentation curves of a 2.5 µm spherical probe for cells of 0.5, 2 and 10 kPa (ν = 0.5). B: a synthetic force curve (E = 2 kPa, contact 0.2 µm into the approach, 30 pN noise) fitted with E and contact point free: the fit recovers both. C: logarithmic axes after subtracting the contact point: slope 3/2 for the sphere, slope 2 for a cone of the same modulus](./plots/hertz.py)

### 31.2.2. Aspiration, Twisting and Stretching

Micropipette aspiration draws a cell into a pipette of radius $R_{\mathrm{p}}$ under suction $\Delta p$. For an elastic solid the aspirated length grows linearly, $L/R_{\mathrm{p}} \approx 3\Phi\Delta p/(2\pi E)$ with a wall factor $\Phi \approx 2.1$ (Theret and colleagues 1988); for a liquid drop with a tense cortex, such as a leukocyte or a blastomere, there is a threshold suction given by the Laplace law of the cortical tension, $\Delta p_{\mathrm{c}} = 2T_{\mathrm{c}}(1/R_{\mathrm{p}} - 1/R_{\mathrm{c}})$, above which the cell flows in ([7.5.8](/7.5.8) and Eq. (29.12) of [7.6.29](/7.6.29)). Magnetic twisting cytometry applies a torque to ferromagnetic beads bound to integrins and measures their rotation, giving the frequency-dependent modulus of the cortex over many decades; the optical stretcher deforms suspended cells between two diverging laser beams; and microrheology infers moduli from the thermal or driven motion of embedded particles ([7.6.23](/7.6.23)). Each method probes a different region (cortex, cytoplasm, whole cell) and time scale, and the numbers differ by up to an order of magnitude for the same cells; comparisons are meaningful only within a method.

### 31.2.3. Traction Force Microscopy

A cell crawling on a soft gel deforms it, and the deformation reveals the forces.

**Definition 31.2.2 (Traction Force Microscopy)** **Traction force microscopy** (TFM) determines the tractions (forces per area) that a cell exerts on a substrate of known elasticity from the measured displacements of fiducial markers (fluorescent beads) embedded near the substrate surface, by inverting the elastic equations of the substrate.

For a thick substrate the surface is an elastic half-space, and the displacement produced by a tangential point force is given by the Boussinesq–Cerruti solution,
$$
u_i(\boldsymbol{r}) = \int G_{ij}(\boldsymbol{r} - \boldsymbol{r}')\,T_j(\boldsymbol{r}')\,\mathrm{d}^2r', \qquad G_{ij}(\boldsymbol{r}) = \frac{1 + \nu}{\pi E\,r}\left[(1 - \nu)\delta_{ij} + \nu\frac{r_ir_j}{r^2}\right]. \tag{31.2}
$$
The convolution becomes a product under the two-dimensional **Fourier transform**, and the transform of the Green's function is algebraic.

**Proposition 31.2.1 (Fourier-Transform Traction Cytometry)** In Fourier space, $\tilde u_i(\boldsymbol{k}) = \tilde G_{ij}(\boldsymbol{k})\tilde T_j(\boldsymbol{k})$ with
$$
\tilde G_{ij}(\boldsymbol{k}) = \frac{2(1 + \nu)}{Ek}\left[\delta_{ij} - \nu\frac{k_ik_j}{k^2}\right], \tag{31.3}
$$
so the tractions follow from the measured displacements by inverting a $2\times2$ matrix at each wave vector (Butler, Fredberg and colleagues 2002).

**Proof** The two-dimensional Fourier transforms of $1/r$ and of $r_ir_j/r^3$ are $2\pi/k$ and $(2\pi/k)(\delta_{ij} - k_ik_j/k^2)$. Substituting in Eq. (31.2), $\tilde G_{ij} = [(1 + \nu)/\pi E](2\pi/k)[(1 - \nu)\delta_{ij} + \nu(\delta_{ij} - k_ik_j/k^2)]$, which simplifies to Eq. (31.3). $\square$

The inversion is ill-posed: $\tilde G \propto 1/k$, so its inverse amplifies the short-wavelength noise of the bead positions in proportion to $k$. The standard remedy is regularization, minimizing $\lVert\tilde G\tilde T - \tilde u\rVert^2 + \lambda^2\lVert\tilde T\rVert^2$, which trades spatial resolution (set by the bead density, about $1$–$2\,\mu\mathrm{m}$) against noise. The total force and the strain energy $U = \frac{1}{2}\int\boldsymbol{T}\cdot\boldsymbol{u}\,\mathrm{d}^2r$, the work done by the cell on the substrate, are robust; the peak tractions are not. Fibroblasts on gels of $10\,\mathrm{kPa}$ exert peak tractions of a few hundred pascals to a few kilopascals concentrated at focal adhesions at the cell ends, a contractile force dipole of $10$–$100\,\mathrm{nN}$ per end. In monolayers, force balance on the whole sheet gives the internal stresses between cells from the tractions under them (monolayer stress microscopy, Tambe, Fredberg, Trepat and colleagues 2011), and cells tend to migrate along the direction of maximal principal stress (plithotaxis).

![Traction force microscopy (Definition 31.2.2, Proposition 31.2.1). A: synthetic tractions of a contractile cell (two adhesion zones 34 µm apart pulling inward, peak 600 Pa). B: the substrate displacements (E = 10 kPa, ν = 0.48) from the Boussinesq solution, with 20 nm of noise added. C: tractions recovered by regularized inversion in Fourier space: the total force per end (24 nN) is recovered, but the adhesions are blurred and the peak traction underestimated](./plots/tfm.py)

### 31.2.4. Molecular Tension Sensors

To measure forces on single molecules inside cells, a pair of fluorophores for **Förster resonance energy transfer** ([6.4.10](/6.4.10)) is joined by an elastic linker, such as a spider-silk peptide of known force–extension curve, and the construct is inserted into a load-bearing protein. Stretching the linker increases the distance between the fluorophores and lowers the transfer efficiency $E_{\mathrm{FRET}} = 1/[1 + (r/R_0)^6]$. With a vinculin tension sensor, Grashoff, Schwartz and colleagues (2010) found an average of about $2.5\,\mathrm{pN}$ per vinculin in focal adhesions. A digital alternative are DNA tension gauge tethers, double-stranded DNA linkers that rupture at defined forces between 12 and $56\,\mathrm{pN}$ depending on the geometry of the pull: cells could spread and form adhesions only on tethers rupturing above about $40\,\mathrm{pN}$, which sets the force on a single integrin during adhesion formation (Wang and Ha 2013).

## 31.3. Adhesion and the Molecular Clutch

### 31.3.1. The Clutch

At the leading edge of a migrating cell, actin polymerizes against the membrane and is pulled back by myosin, so that the actin network flows rearward (retrograde flow). Adhesions couple this flow to the substrate, and the coupling determines how much of the polymerization advances the edge and how much force is transmitted. Mitchison and Kirschner (1988) compared the linkage to the clutch of a car.

**Definition 31.3.1 (Molecular Clutch Model)** In the **molecular clutch model**, actin filaments driven rearward by myosin are connected to the extracellular matrix through a population of transient, elastic linkages (clutches: integrins with talin, vinculin and other adaptors) that bind and unbind stochastically; bound clutches are stretched by the moving actin, transmit force to the substrate and slow the flow, and unbind faster under force.

The quantitative model of Chan and Odde (2008) has five ingredients. Motors pull the actin bundle rearward at a speed that falls linearly with the load, $v = v_{\mathrm{u}}(1 - F_{\mathrm{sub}}/n_{\mathrm{m}}F_{\mathrm{m}})$, where $n_{\mathrm{m}}F_{\mathrm{m}}$ is the stall force of $n_{\mathrm{m}}$ motors. Each of $n_{\mathrm{c}}$ clutches binds at rate $k_{\mathrm{on}}$, is a spring of stiffness $k_{\mathrm{c}}$, and unbinds as a **slip bond** at rate $k_{\mathrm{off}}(F) = k_{\mathrm{off}}^0\mathrm{e}^{F/F_{\mathrm{b}}}$ (the **Bell model**). The substrate is a spring of stiffness $k_{\mathrm{sub}}$ in series with the bound clutches, which act in parallel; force balance on the substrate gives its displacement,
$$
x_{\mathrm{sub}} = \frac{k_{\mathrm{c}}\sum_{i\,\mathrm{bound}}x_i}{k_{\mathrm{sub}} + n_{\mathrm{b}}k_{\mathrm{c}}}, \qquad F_{\mathrm{sub}} = k_{\mathrm{sub}}x_{\mathrm{sub}}, \tag{31.4}
$$
where $x_i$ is the position of the actin end of clutch $i$, advancing at speed $v$, and the force on that clutch is $k_{\mathrm{c}}(x_i - x_{\mathrm{sub}})$.

**Algorithm 31.3.1 (Stochastic Simulation of the Clutch)** At each time step $\Delta t$: compute $x_{\mathrm{sub}}$ and $F_{\mathrm{sub}}$ from Eq. (31.4) and the flow speed $v$; advance the actin ends of the bound clutches by $v\Delta t$; unbind each bound clutch with probability $1 - \exp[-k_{\mathrm{off}}(F_i)\Delta t]$; bind each free clutch with probability $1 - \exp(-k_{\mathrm{on}}\Delta t)$, attaching it unstretched at the current substrate position. Record $F_{\mathrm{sub}}$ and $v$. (An exact version draws event times with the **Gillespie algorithm**.)

### 31.3.2. Stiffness Sensing

The simulations show two regimes. On a soft substrate, a given motor displacement builds force slowly (the loading rate is about $k_{\mathrm{sub}}v$), so many clutches bind before the force per clutch reaches $F_{\mathrm{b}}$; when it does, the few clutches that unbind shift their load onto the others, which then unbind faster, and the whole adhesion fails in a cascade. The force rises and collapses periodically (load and fail), and its average is low because each cycle takes long. On a stiff substrate the force on a newly bound clutch rises within milliseconds, faster than other clutches bind, and clutches break one at a time (frictional slippage): traction is again low and retrograde flow is fast. Between these extremes, at a substrate stiffness comparable to the summed stiffness of the clutches that bind during one loading time, traction is maximal and flow minimal.

**Remark 31.3.1 (Where is the optimum?)** A scaling estimate locates the optimal stiffness. On a soft substrate the bound clutches share the load, and the substrate force reaches the value $n_{\mathrm{b}}F_{\mathrm{b}}$ at which clutches start to fail in the loading time $\tau_{\mathrm{load}} \approx n_{\mathrm{b}}F_{\mathrm{b}}/(k_{\mathrm{sub}}v_{\mathrm{u}})$, where $n_{\mathrm{b}} \approx n_{\mathrm{c}}k_{\mathrm{on}}/(k_{\mathrm{on}} + k_{\mathrm{off}}^0)$ is the number of engaged clutches. Traction is maximal when this loading time is comparable to the binding time $1/k_{\mathrm{on}}$: much longer, and the cycles are slow (load and fail); much shorter, and clutches fail before others bind (slippage). Hence $k_{\mathrm{sub}}^* \approx n_{\mathrm{b}}F_{\mathrm{b}}k_{\mathrm{on}}/v_{\mathrm{u}}$, which for the parameters of the figure ($n_{\mathrm{b}} \approx 68$, $F_{\mathrm{b}} = 2\,\mathrm{pN}$, $k_{\mathrm{on}} = 1\,\mathrm{s^{-1}}$, $v_{\mathrm{u}} = 120\,\mathrm{nm\,s^{-1}}$) gives about $1\,\mathrm{pN\,nm^{-1}}$, where the simulations place the maximum. This is of the order of the stiffness of a gel of a few kilopascals probed over the size of an adhesion.

Measured retrograde flow and traction of embryonic chick neurons on gels of different stiffness show this biphasic dependence (Chan and Odde 2008). Many other cells, however, exert monotonically more traction on stiffer substrates. Elosegui-Artola, Roca-Cusachs and colleagues (2016) showed why: above a threshold force talin unfolds and exposes vinculin-binding sites, which reinforces the clutch; with reinforcement the decline at high stiffness is replaced by adhesion growth, and the threshold stiffness at which reinforcement begins can be shifted by the density of matrix ligands and the number of integrins. Catch bonds of integrins ([7.3.23](/7.3.23)) have a similar effect.

![The molecular clutch (Definition 31.3.1, Algorithm 31.3.1; 75 motors of 2 pN, 75 clutches of 5 pN/nm, k_on = 1/s, k_off = 0.1/s·exp(F/2 pN), v_u = 120 nm/s). A: mean traction (solid) and retrograde flow (dashed) against substrate stiffness: traction peaks at an optimal stiffness. B: on a soft substrate (0.1 pN/nm) force builds slowly and collapses in load-and-fail cycles. C: on a stiff substrate (100 pN/nm) clutches break individually as soon as they bind (frictional slippage)](./plots/clutch.py)

### 31.3.3. Directed Migration: Chemotaxis, Haptotaxis, Durotaxis

Cells migrate up gradients of soluble chemoattractants (**chemotaxis**, [7.3.15](/7.3.15)), of bound adhesion ligands (haptotaxis) and of substrate stiffness.

**Definition 31.3.2 (Durotaxis)** **Durotaxis** is directed cell migration up a gradient of substrate stiffness.

Lo, Wang and colleagues (2000) showed that fibroblasts crossing from a soft to a stiff region of a gel continue onto the stiff side and that cells approaching from the stiff side turn back at the boundary. The clutch provides a mechanism: if traction increases with stiffness (in the reinforced regime), the adhesions at the stiffer end of a cell hold more force and survive longer, and a cell that is a tug-of-war between its two ends drifts toward the end that pulls harder. Gradients of a few percent of stiffness across a cell length suffice, as for chemotaxis; the limits of chemical gradient sensing are discussed in [7.6.35](/7.6.35). Cells also respond to the viscoelasticity and stress relaxation of their matrix: on matrices that relax stress quickly, cells spread more, because the matrix yields to the forces they exert and they can remodel it (Chaudhuri, Mooney and colleagues 2016).

## 31.4. The Physics of Single-Cell Migration

### 31.4.1. Mesenchymal and Amoeboid Migration

Single cells migrate in two main modes. Mesenchymal migration, of fibroblasts, osteoblasts, chondrocytes and of cancer cells after an **epithelial–mesenchymal transition**, uses strong adhesion: the cell polarizes, extends actin-rich protrusions (**lamellipodia**, flat sheets of Arp2/3-branched actin; **filopodia**, bundles of parallel filaments; and in invasive cells invadopodia, which secrete matrix metalloproteases), forms adhesions at the front and releases them at the rear. It is slow, $0.1$–$0.5\,\mu\mathrm{m\,min^{-1}}$. Fragments of lamellipodia without nucleus or most organelles still crawl, an indication of how self-contained the machinery is. Amoeboid migration, of amoebae, leukocytes, dendritic cells and some tumor cells, uses weak or no specific adhesion, a highly contractile cortex and often blebs, and is fast, $5$–$20\,\mu\mathrm{m\,min^{-1}}$.

A bleb forms where the membrane detaches from the cortex or the cortex ruptures: the cytoplasm, under hydrostatic pressure from cortical contraction, flows into a spherical protrusion that is initially free of actin; a new cortex then assembles under the bleb membrane and myosin retracts it, or the cell body follows it. The pressure involved follows from the Laplace law for the cortical tension, $\Delta p = 2T_{\mathrm{c}}/R$: for $T_{\mathrm{c}} = 0.5\,\mathrm{mN\,m^{-1}}$ and $R = 10\,\mu\mathrm{m}$, $\Delta p = 100\,\mathrm{Pa}$. In confinement, many cells switch from mesenchymal to amoeboid migration and move without specific adhesions, transmitting force by nonspecific friction between their retrograde cortical flow and the walls of the channel (Bergert, Paluch and colleagues 2015; Liu, Piel and colleagues 2015). Intrinsic factors (low adhesion, high contractility) and extrinsic factors (confinement, nonadhesive substrates) favor the switch; the classical "sol–gel" model of amoebae, in which the front liquefies and the rear gels and contracts, is the qualitative ancestor of these mechanical models.

### 31.4.2. The Persistent Random Walk

Tracked over hours, a cell moves in a straight line for a while and then turns. The simplest model with this property treats the velocity as an **Ornstein–Uhlenbeck process** ([7.6.5](/7.6.5)): it relaxes toward zero with a persistence time $P$ and is kicked randomly, so that its direction is remembered for a time $P$.

**Formula 31.4.1 (Fürth Formula)** For a cell in $d$ dimensions whose velocity is an Ornstein–Uhlenbeck process with mean squared speed $S^2$ and persistence time $P$, the **mean squared displacement** is
$$
\langle r^2(t)\rangle = 2S^2P\left[t - P\left(1 - \mathrm{e}^{-t/P}\right)\right], \tag{31.5}
$$
which is ballistic, $S^2t^2$, for $t \ll P$ and diffusive, $2dDt$ with $D = S^2P/d$, for $t \gg P$.

**Proof** The velocity autocorrelation is $\langle\boldsymbol{v}(t)\cdot\boldsymbol{v}(0)\rangle = S^2\mathrm{e}^{-\lvert t\rvert/P}$. Then $\langle r^2(t)\rangle = \int_0^t\int_0^t\langle\boldsymbol{v}(t_1)\cdot\boldsymbol{v}(t_2)\rangle\,\mathrm{d}t_1\,\mathrm{d}t_2 = 2S^2\int_0^t(t - s)\mathrm{e}^{-s/P}\,\mathrm{d}s$, which evaluates to Eq. (31.5). Expanding for small $t$ gives $S^2t^2$; for large $t$, $2S^2Pt = 2d(S^2P/d)t$. $\square$

Fitting Eq. (31.5) to measured trajectories gives $S$ and $P$; fibroblasts on two-dimensional substrates have $P$ of tens of minutes, neutrophils of a few minutes. Real cells often deviate: their speed and persistence are correlated (faster cells turn less, a universal coupling explained by the advection of polarity cues by actin flow, Maiuri, Voituriez, Piel and colleagues 2015), and in three-dimensional matrices their turning statistics are anisotropic and heavy-tailed. Persistent random walks also describe bacteria swimming by run and tumble ([7.6.35](/7.6.35)).

![Cell migration as a persistent random walk (Formula 31.4.1). A: simulated 10-hour trajectories of slow, persistent mesenchymal-like cells (S = 0.5 µm/min, P = 30 min) and fast amoeboid-like cells (S = 8 µm/min, P = 2 min). B: mean squared displacement of 200 cells of each kind (dots) and the Fürth formula (curves): slope 2 below the persistence time (dotted lines), slope 1 above it](./plots/persistent-walk.py)

## 31.5. Mechanosensation by Hair Cells

### 31.5.1. The Hair Bundle and the Gating Spring

The hair cells of the inner ear and of the lateral line of fish carry on their apical surface a bundle of 20–300 stereocilia, rigid actin-filled rods arranged in rows of increasing height. Deflecting the bundle toward the tallest row stretches the tip links, fine filaments of cadherin-23 and protocadherin-15 about $150\,\mathrm{nm}$ long that connect the tip of each stereocilium to the side of its taller neighbor, and opens mechanotransduction channels at their lower ends; the molecular identity of the channel complex (TMC1/2 with TMIE and other subunits) is discussed in [7.6.25](/7.6.25). The channels open within microseconds, too fast for any chemical messenger: the force is transmitted mechanically to the gate. A displacement of the bundle tip of $1\,\mathrm{nm}$, smaller than the amplitude of its Brownian motion, produces a detectable response at the threshold of hearing.

Howard and Hudspeth (1988) explained the mechanics of the bundle by a model in which each channel is in series with an elastic element.

**Definition 31.5.1 (Gating Spring)** In the **gating-spring** model of hair-cell transduction, each transduction channel is attached to an elastic element (the gating spring, comprising the tip link and its anchors) that is stretched when the bundle is deflected; the tension in the spring biases the channel toward opening, and opening shortens the spring by the gating swing $d$, relaxing its tension by a gating force $z = \kappa_{\mathrm{gs}}\gamma d$ per channel (with gating-spring stiffness $\kappa_{\mathrm{gs}}$ and geometric gain $\gamma$ between bundle and spring displacements).

**Theorem 31.5.1 (Gating Compliance and Negative Stiffness)** For a bundle with $N$ channels, each a **two-state system** with open probability $p_{\mathrm{o}}(x) = 1/\{1 + \exp[-z(x - x_0)/k_{\mathrm{B}}T]\}$ at bundle displacement $x$, and with a stiffness $K_\infty$ of the gating springs and the stereociliary pivots combined, the force needed to hold the bundle at $x$ is
$$
F(x) = K_\infty x - Nz\,p_{\mathrm{o}}(x) + F_0, \tag{31.6}
$$
and its stiffness is
$$
K(x) = \frac{\mathrm{d}F}{\mathrm{d}x} = K_\infty - \frac{Nz^2}{k_{\mathrm{B}}T}\,p_{\mathrm{o}}(1 - p_{\mathrm{o}}). \tag{31.7}
$$
The stiffness is lowest at $p_{\mathrm{o}} = 1/2$ and becomes negative there if $Nz^2/(4k_{\mathrm{B}}T) > K_\infty$.

**Proof** The free energy of the bundle at displacement $x$ with $n$ open channels is $\frac{1}{2}K_\infty x^2 - nz(x - x_0) + \text{const}$, since each open channel relaxes its spring by an amount that lowers the energy by $zx$ (linear in $x$ for small changes). Averaging over the channel states in equilibrium, $F = \partial\langle E\rangle/\partial x = K_\infty x - z\langle n\rangle$, with $\langle n\rangle = Np_{\mathrm{o}}(x)$ and $p_{\mathrm{o}}$ the Boltzmann factor of a two-state system with energy difference $-z(x - x_0)$; this is Eq. (31.6). Differentiating, $\mathrm{d}p_{\mathrm{o}}/\mathrm{d}x = (z/k_{\mathrm{B}}T)p_{\mathrm{o}}(1 - p_{\mathrm{o}})$, which gives Eq. (31.7), and $p_{\mathrm{o}}(1 - p_{\mathrm{o}}) \le 1/4$. $\square$

The decrease of stiffness when channels gate is the mechanical signature of the gating force acting back on the bundle (the reciprocity of [7.6.4](/7.6.4#sec-4.5.3): if force opens channels, opening channels changes the force). It was observed directly: bundles of the bullfrog sacculus are softer near their resting position, and the softening disappears when the tip links are cut (Howard and Hudspeth 1988); in some bundles the force–displacement curve has a region of negative slope (Martin, Mehta and Hudspeth 2000). With $K_\infty \approx 1\,\mathrm{pN\,nm^{-1}}$, $z \approx 0.7\,\mathrm{pN}$ and $N \approx 50$, $Nz^2/4k_{\mathrm{B}}T = 50 \times 0.49/16.4 \approx 1.5\,\mathrm{pN\,nm^{-1}}$, enough for negative stiffness.

![The gating-spring model (Definition 31.5.1, Theorem 31.5.1; K∞ = 1 pN/nm, z = 0.7 pN, kBT = 4.1 pN nm). A: open probability of a transduction channel against bundle displacement. B: force–displacement relations for 0, 25, 50 and 80 channels: gating makes the bundle softer near the operating point and, for many channels, the relation non-monotonic. C: bundle stiffness dF/dx, negative near x0 for N = 50 and 80](./plots/gating-spring.py)

### 31.5.2. Active Amplification Near a Hopf Bifurcation

A region of negative stiffness, combined with an adaptation process that moves the operating point (myosin motors that reposition the upper ends of the tip links, and $\ce{Ca^2+}$ that enters through the channels and promotes their closure), makes the bundle an active oscillator: bundles of the bullfrog sacculus oscillate spontaneously at $5$–$50\,\mathrm{Hz}$ with amplitudes of tens of nanometers. The ear exploits this. An oscillator poised at the boundary between quiescence and oscillation, a **Hopf bifurcation** ([2.4.11](/2.4.11)), responds to weak periodic forces at its characteristic frequency with an enormous gain and to strong forces with a compressed response (Camalet, Duke, Jülicher and Prost 2000; Eguíluz, Ospeck, Choe, Hudspeth and Magnasco 2000).

**Proposition 31.5.1 (Response at a Hopf Bifurcation)** For the normal form $\dot z = (\mu + \mathrm{i}\omega_0)z - \lvert z\rvert^2z + F\mathrm{e}^{\mathrm{i}\omega t}$ with $\mu \le 0$, the steady response $z = r\mathrm{e}^{\mathrm{i}(\omega t + \theta)}$ has amplitude $r$ given by
$$
F^2 = r^2\left[(\mu - r^2)^2 + (\omega - \omega_0)^2\right]. \tag{31.8}
$$
At $\mu = 0$ and $\omega = \omega_0$, $r = F^{1/3}$ for all $F$: the gain $r/F = F^{-2/3}$ diverges for weak stimuli. For $\mu < 0$ the response is linear, $r = F/\lvert\mu\rvert$, for $F \ll \lvert\mu\rvert^{3/2}$, and approaches $F^{1/3}$ above.

**Proof** Substituting the ansatz, $\mathrm{i}\omega r = (\mu + \mathrm{i}\omega_0)r - r^3 + F\mathrm{e}^{-\mathrm{i}\theta}$, that is $F\mathrm{e}^{-\mathrm{i}\theta} = r(r^2 - \mu) + \mathrm{i}r(\omega - \omega_0)$; taking the squared modulus gives Eq. (31.8). At $\mu = 0$, $\omega = \omega_0$: $F^2 = r^6$. For $\mu < 0$ and small $r$, $F^2 \approx r^2\mu^2$. $\square$

The mammalian cochlea shows exactly these signatures: the vibration of the basilar membrane at a given place grows linearly with sound pressure at very low levels and as about the one-third power over the range of normal hearing, it is sharply tuned, and it vanishes when the cochlea dies. It also emits sound spontaneously (otoacoustic emissions), as an oscillator slightly beyond the bifurcation would. In mammals the amplification is attributed largely to the electromotility of outer hair cells, driven by the membrane motor protein prestin, and partly to active bundle motility; the compressive nonlinearity is what lets the ear handle a dynamic range of 120 decibels, a factor of $10^6$ in pressure.

![Active amplification near a Hopf bifurcation (Proposition 31.5.1). A: response amplitude at the characteristic frequency against stimulus force for μ = −0.3, −0.01 and 0: at the bifurcation the response grows as F^(1/3) (dashed) at all forces, amplifying weak stimuli by orders of magnitude and compressing strong ones. B: gain r/F against frequency detuning for a weak stimulus: the critical oscillator is sharply tuned](./plots/hopf-amplifier.py)

## 31.6. Collective Migration and Jamming

### 31.6.1. Modes of Collective Migration

In development, wound healing and cancer invasion, cells often migrate together: epithelial sheets spreading into free space, clusters such as the border cells of the *Drosophila* egg chamber, streams such as the neural crest ([7.5](/7.5)). Collective migration is more directional than single-cell migration: isolated cells may move faster but change direction often, whereas cells in a group align their velocities over several cell diameters and move persistently. Three kinds of interaction couple them: mechanical forces transmitted through cadherin junctions, which hold the sheet together under tension, and through friction between neighbors sliding past each other; chemical signals; and contact inhibition of locomotion, by which cells stop protruding where they touch. Leader cells at the edge of a sheet with large lamellipodia pull on their followers, but traction maps show that force is generated throughout the sheet, not only at its edge: the tractions add up over many cells, and the tension in the sheet grows with distance from the edge (Trepat and colleagues 2009). Since individual cells in a dense sheet show few morphological signs of polarity (some extend cryptic lamellipodia beneath their neighbors), the direction of migration is best read from the tractions. Cells move at about $30\,\mu\mathrm{m\,h^{-1}}$, so the Reynolds number is about $\rho vL/\eta \approx 10^3 \times 10^{-8} \times 10^{-5}/10^{-3} = 10^{-7}$: collective motion is overdamped, and the equations of motion balance forces without inertia.

### 31.6.2. The Jamming Transition

Monolayers of epithelial cells cultured at increasing density slow down: at low density they flow and swirl in vortices several cells across (a mesoscale turbulence), and as density rises the vortices grow and slow, neighbor exchanges cease and the monolayer freezes like a glass (Angelini, Weitz and colleagues 2011).

**Definition 31.6.1 (Jamming Transition)** The **jamming transition** is the change of a disordered collection of particles, cells or other units from a fluid state, in which the units exchange neighbors and the collection flows under small stresses, to a solid-like state, in which each unit is trapped by its neighbors and the collection acquires a yield stress, upon increasing density or decreasing driving.

For frictionless soft disks at zero temperature the transition occurs at the random close packing fraction, $\phi_{\mathrm{J}} \approx 0.84$ in two dimensions (for bidisperse disks) and $\approx 0.64$ for spheres in three. A confluent epithelium, however, has no free space: its packing fraction is always 1. Bi, Manning and colleagues (2015) showed in the vertex model ([7.5.8](/7.5.8#sec-8.10)) that a confluent tissue still has a rigidity transition, controlled not by density but by cell shape: the tissue is solid when the preferred shape index $p_0 = P_0/\sqrt{A_0}$ (perimeter over the square root of area) is below about $3.81$ and fluid above it, and cell motility shifts the boundary (the self-propelled Voronoi model, 2016). The shape index of cells is thus a readout of the state: in airway epithelia from asthmatic donors and under compressive stress, cells elongate and the epithelium unjams (Park, Fredberg and colleagues 2015). Wound healing is unjamming and rejamming: the free space created by a wound lets cells near its edge move and spread, and the tissue jams again when the gap is closed. The turnover of junctions is the main dissipative process that sets the long-time viscosity of a fluid tissue.

![Jamming of self-propelled soft disks (120 bidisperse disks, overdamped, harmonic repulsion, self-propulsion 0.02 with persistence time 10). A: final configurations at packing fractions 0.62 and 0.88, colored by distance moved (bright: far). B: mean squared displacement (center-of-mass drift removed) at five packing fractions: motion becomes increasingly hindered and subdiffusive with density. C: long-time effective diffusion coefficient relative to a free cell: it falls by more than an order of magnitude on approaching φJ ≈ 0.84 (dotted). A small system with short runs, so the transition is smeared](./plots/jamming.py)

Topological defects are a further signature. Elongated cells in a monolayer align with their neighbors like the molecules of a liquid crystal (a **nematic phase**), and the alignment field has point defects around which it rotates by half a turn; only defects of charge $+1/2$ (comet-shaped) and $-1/2$ (three-armed) occur, as in nematic liquid crystals, observed for example in monolayers of C2C12 myoblasts and fibroblasts. Because the cells are active, the defects move: $+1/2$ defects are self-propelled, and in epithelial monolayers compressive stress concentrates at them and triggers the extrusion and death of cells there, a mechanism of tissue homeostasis (Saw, Ladoux and colleagues 2017). The theory of active nematics is in [7.6.37](/7.6.37).

### 31.6.3. Models of Collective Migration

| Model | Variables | Strengths | Typical use |
|---|---|---|---|
| Particle models (active Brownian disks, Vicsek-type) | position and polarity of each cell | simple, many cells; density effects | jamming, flocking, contact inhibition |
| **Cellular Potts model** ([7.3.23](/7.3.23)) | lattice sites labelled by cell identity; energy of adhesion and area, Metropolis updates | arbitrary cell shapes, sorting | cell sorting, fingering at invasion fronts, glassy dynamics |
| Vertex and Voronoi models ([7.5.8](/7.5.8)) | positions of cell vertices or centers; area and perimeter energies | confluent epithelia, shape index, T1 transitions | rigidity transition, tissue folding |
| Phase-field models | a field $\phi_i(\boldsymbol{r}, t)$ per cell, 1 inside, 0 outside | deformable cells off-lattice, subcellular resolution | collisions, alignment, collective oscillations |
| Continuum (active-gel, active-nematic) models | density, velocity, polarity or nematic order, stress | large scales, symmetry-based | flows, defects, wound closure, interface instabilities |

Vertex models, for example, evolve each vertex by an overdamped Langevin equation, $\mu\,\mathrm{d}\boldsymbol{r}_i/\mathrm{d}t = -\partial E/\partial\boldsymbol{r}_i + \boldsymbol{F}_i^{\mathrm{active}} + \boldsymbol{\xi}_i$, with an energy of area elasticity, cortical contractility and junctional tension, a friction coefficient $\mu$ with the substrate, and active and random forces; topological changes are added as rules: T1 transitions (neighbor exchange), T2 transitions (removal of a cell that has shrunk below a threshold, modeling extrusion) and division of cells that exceed a threshold area, usually across their long axis. Continuum models are written from symmetry and conservation laws, with constitutive equations that relate the stress and the traction to velocity, polarity and density; they capture the fingering of advancing monolayer fronts and the dynamics of interfaces between different cell populations, in which topological defects again play a role.

## 31.7. The Mechanics of Tissues

### 31.7.1. Shape, Orientation and Oscillation

Morphogenesis is the result of cells migrating and deforming ([7.5.8](/7.5.8)): forces generated by actomyosin are transmitted through junctions and adhesions, compress, stretch and bend tissues, and are sensed in turn, so that mechanics and signaling form feedback loops. One recurring phenomenon is oscillation. The cells of the *Drosophila* amnioserosa pulse in area with periods of a few minutes during dorsal closure, and the cells of the ventral furrow constrict their apical surfaces in pulses during gastrulation; in both, pulses of myosin are ratcheted so that each contraction is partly stabilized before the next (Martin, Kaschube and Wieschaus 2009; Solon and colleagues 2009). Two classes of model explain such oscillations: mechanochemical feedback, in which tension activates myosin through signaling and myosin generates tension, giving a limit cycle beyond a Hopf bifurcation, and ratchet models, in which a contraction–relaxation cycle is rectified by stabilization.

### 31.7.2. Folding and Wrinkling of Layered Tissues

Many organs are layered tubes: the gut, the airways, blood vessels. When an inner layer grows faster than the outer layer that confines it, or is stiffer than the tissue beneath it, it buckles into folds whose wavelength is set by mechanics.

**Formula 31.7.1 (Wrinkling Wavelength)** A thin elastic film of thickness $h$ and plane-strain modulus $\bar E_{\mathrm{f}} = E_{\mathrm{f}}/(1 - \nu_{\mathrm{f}}^2)$ bonded to a thick, soft substrate of plane-strain modulus $\bar E_{\mathrm{s}}$ wrinkles under compression with wavelength
$$
\lambda = 2\pi h\left(\frac{\bar E_{\mathrm{f}}}{3\bar E_{\mathrm{s}}}\right)^{1/3}, \tag{31.9}
$$
independent of the amount of compression beyond the threshold strain $\varepsilon_{\mathrm{c}} = \frac{1}{4}(3\bar E_{\mathrm{s}}/\bar E_{\mathrm{f}})^{2/3}$.

The wavelength minimizes the sum of the bending energy of the film, which favors long waves ($\propto \bar E_{\mathrm{f}}h^3q^4$), and the elastic energy of the substrate deformed to a depth of about $1/q$, which favors short waves ($\propto \bar E_{\mathrm{s}}q$); setting the derivative of the total with respect to $q$ to zero gives $q^3 \propto \bar E_{\mathrm{s}}/(\bar E_{\mathrm{f}}h^3)$, that is $\lambda \propto h(\bar E_{\mathrm{f}}/\bar E_{\mathrm{s}})^{1/3}$. In the developing chick gut, the mucosa folds into ridges, zigzags and finally villi as the surrounding smooth-muscle layers differentiate and constrain its growth, with wavelengths predicted by this mechanics (Shyer, Tabin, Mahadevan and colleagues 2013). In tubes, the same balance sets the number of mucosal folds; a thickened or stiffened mucosa, as in some diseases, changes the pattern of folds, which is why such models are of interest for pathology. Cylindrical models with an inner stiff layer, a soft submucosa and an outer layer that is either free or fixed by the muscle layers are used to compute these instabilities.

### 31.7.3. Arteries, Tendons, Ligaments and Muscle

Soft tissues are nonlinear, anisotropic and viscoelastic. Their stress–strain curves are J-shaped: soft at small strain and stiffening progressively. In arteries, smooth muscle, elastin and crimped collagen fibers bear the load at small strains, and as the strain grows more and more collagen fibers are straightened and recruited, so that the stiffness rises roughly in proportion to the stress, which is the exponential (Fung) law $\sigma = c(\mathrm{e}^{b\varepsilon} - 1)$, with $\mathrm{d}\sigma/\mathrm{d}\varepsilon = b(\sigma + c)$. The circumferential direction is stiffer and stronger than the axial; in atherosclerotic arteries the circumferential compliance increases and the axial decreases, so that the anisotropy falls, probably because of collagen reorientation, elastin degradation and smooth-muscle degeneration. Veins have similar curves with lower moduli. The nonlinear stiffening protects vessels: a material whose stiffness grows with stress cannot develop the aneurysm-like bulging instability of a balloon, whose membrane softens as it inflates.

Tendons, about 80 % collagen by dry weight in parallel fibrils, have a toe region up to about 2 % strain where the crimp of the fibrils straightens, a linear region with modulus of $1$–$2\,\mathrm{GPa}$ in which the straightened fibrils stretch, and beyond about 4–8 % strain a region of microscopic failure leading to rupture at stresses of $50$–$100\,\mathrm{MPa}$. They store elastic energy efficiently (the Achilles tendon returns most of the work done on it in running), with a hysteresis of about 10 %, and creep and relax stress under sustained load. Ligaments bear loads in more complex directions (the spinal ligaments in tension, compression, torsion and shear). Skeletal muscle shows thixotropy: its passive stiffness depends on its recent history of stretch and contraction, because a small fraction of cross-bridges remains attached in a relaxed muscle and is broken by movement; this is one reason why muscles feel stiff after rest. The physiology of muscle, tendon and bone is in [7.14](/7.14); the development of these tissues in [7.5.24](/7.5.24).

**Proposition 31.7.1 (J-Shaped Curves from Fiber Recruitment)** Let a tissue contain fibers of modulus $E_{\mathrm{f}}$ that bear load only beyond their individual slack strains $\varepsilon_{\mathrm{s}}$, distributed with density $g(\varepsilon_{\mathrm{s}})$. Then the stress is $\sigma(\varepsilon) = \phi E_{\mathrm{f}}\int_0^\varepsilon(\varepsilon - \varepsilon_{\mathrm{s}})g(\varepsilon_{\mathrm{s}})\,\mathrm{d}\varepsilon_{\mathrm{s}}$, with $\phi$ the fiber volume fraction, and the tangent modulus $\mathrm{d}\sigma/\mathrm{d}\varepsilon = \phi E_{\mathrm{f}}\int_0^\varepsilon g\,\mathrm{d}\varepsilon_{\mathrm{s}}$ is the modulus of the fibers times the fraction already recruited.

**Proof** A fiber with slack $\varepsilon_{\mathrm{s}} < \varepsilon$ carries stress $E_{\mathrm{f}}(\varepsilon - \varepsilon_{\mathrm{s}})$ and others carry none; averaging over the slack distribution gives $\sigma$, and differentiating under the integral (the integrand vanishes at the upper limit) gives the tangent modulus. $\square$

The tangent modulus therefore rises from zero to $\phi E_{\mathrm{f}}$ as the cumulative distribution of slack strains, the toe region reflecting the spread of crimp; if the slack distribution has an exponential tail, the stiffness grows in proportion to the stress, which is Fung's law. Failure of fibers beyond a failure strain ends the linear region.

![Nonlinear elasticity of soft tissues. A: tendon stress–strain curve from fiber recruitment (Proposition 31.7.1; 2000 fibers of 1.5 GPa, collagen volume fraction 0.5, slack 2 ± 0.6 %, failure 5–8 % beyond slack): toe region, linear region and failure. B: exponential (Fung) curves for an artery in the circumferential and axial directions (illustrative parameters): stiffness proportional to stress, and anisotropy](./plots/tendon.py)

## Summary

| Topic | Key results | Where |
|---|---|---|
| Scales | Forces: pN (molecules), nN (adhesions), mN (muscle fibers, forces add over cross-section); moduli: brain $0.1$–$1\,\mathrm{kPa}$ to bone $10$–$20\,\mathrm{GPa}$; stem cells read substrate stiffness by pulling | 31.1.1 |
| Elasticity | $E$, $\nu \approx 0.5$, $G = E/2(1 + \nu)$; power-law rheology, prestress and strain stiffening | 31.1.2 |
| AFM | Hertz $F = \frac{4}{3}\frac{E}{1 - \nu^2}\sqrt R\,\delta^{3/2}$ (scaling $a = \sqrt{R\delta}$); cone $\propto\delta^2$; fit contact point | Definition 31.2.1, Example 31.2.1 |
| TFM | Boussinesq Green's function; $\tilde G_{ij} = \frac{2(1 + \nu)}{Ek}(\delta_{ij} - \nu k_ik_j/k^2)$; ill-posed, regularize; tension sensors: vinculin $2.5\,\mathrm{pN}$, integrin $\sim40\,\mathrm{pN}$ | Definition 31.2.2, Proposition 31.2.1, 31.2.4 |
| Clutch | Motors + elastic slip-bond clutches + substrate spring; load-and-fail (soft) vs slippage (stiff); optimal stiffness $k^* \approx n_{\mathrm{b}}F_{\mathrm{b}}k_{\mathrm{on}}/v_{\mathrm{u}}$; talin reinforcement; durotaxis | Definitions 31.3.1–31.3.2, Algorithm 31.3.1, Remark 31.3.1 |
| Migration | Mesenchymal $0.1$–$0.5$, amoeboid $5$–$20\,\mu\mathrm{m\,min^{-1}}$; blebs by Laplace pressure; friction-based migration in confinement; Fürth MSD $2S^2P[t - P(1 - \mathrm{e}^{-t/P})]$ | 31.4.1, Formula 31.4.1 |
| Hair cells | Gating spring: $F = K_\infty x - Nzp_{\mathrm{o}} + F_0$, $K = K_\infty - (Nz^2/k_{\mathrm{B}}T)p_{\mathrm{o}}(1 - p_{\mathrm{o}})$, negative stiffness; Hopf amplifier $r = F^{1/3}$, sharp tuning, 120 dB range | Definition 31.5.1, Theorem 31.5.1, Proposition 31.5.1 |
| Collectives | Overdamped ($\operatorname{Re} \sim 10^{-7}$); traction-based polarity; jamming $\phi_{\mathrm{J}} \approx 0.84$ (2D), shape-index rigidity transition $p_0^* \approx 3.81$; $\pm1/2$ defects and extrusion; model classes | Definition 31.6.1, 31.6.3 |
| Tissues | Oscillations by mechanochemical feedback or ratchets; wrinkling $\lambda = 2\pi h(\bar E_{\mathrm{f}}/3\bar E_{\mathrm{s}})^{1/3}$; J-shaped curves by fiber recruitment, Fung law; tendon $1$–$2\,\mathrm{GPa}$, failure at 50–100 MPa | Formula 31.7.1, Proposition 31.7.1 |

## Questions

1. An AFM with a spherical probe of radius $5\,\mu\mathrm{m}$ indents a cell by $0.5\,\mu\mathrm{m}$ with a force of $1\,\mathrm{nN}$. What is the Young's modulus ($\nu = 0.5$)? If the cell is $3\,\mu\mathrm{m}$ thick at that point, is the Hertz model reliable?

   **Answer** $E = 3F(1 - \nu^2)/(4\sqrt R\,\delta^{3/2}) = 3 \times 10^{-9} \times 0.75/(4 \times 2.24\times10^{-3} \times 3.54\times10^{-10}) \approx 710\,\mathrm{Pa}$. The indentation is 17 % of the thickness and the contact radius $\sqrt{R\delta} = 1.6\,\mu\mathrm{m}$ is half the thickness: the stiff glass beneath is felt and the true modulus is lower than $710\,\mathrm{Pa}$. Reduce the indentation to below 10 % of the thickness or apply a finite-thickness correction.

2. Derive the scaling $F \propto ER^{1/2}\delta^{3/2}$ of the Hertz contact without solving the elasticity equations, and use the same reasoning to explain why a cone gives $F \propto \delta^2$.

   **Answer** Contact radius $a \approx \sqrt{R\delta}$ for a sphere; strain $\sim\delta/a$; stress $\sim E\delta/a$; force $\sim E(\delta/a)a^2 = Ea\delta \propto ER^{1/2}\delta^{3/2}$. For a cone of half-angle $\alpha$, the contact radius is proportional to the depth, $a \approx \delta\tan\alpha$, so the strain is constant ($\sim\cot\alpha$) and $F \sim E\cot\alpha \cdot a^2 \propto E\tan\alpha\,\delta^2$.

3. A cell on a polyacrylamide gel with $E = 8\,\mathrm{kPa}$, $\nu = 0.45$ displaces beads by $0.5\,\mu\mathrm{m}$ over a region about $5\,\mu\mathrm{m}$ across. Estimate the traction and the force. Why does halving the gel stiffness not simply double the displacements in an experiment with real cells?

   **Answer** From Eq. (31.3) at $k \approx 2\pi/(5\,\mu\mathrm{m})$, $\tilde G \approx 2(1.45)/(Ek) \approx 2.9/(8000 \times 1.26\times10^6) \approx 2.9\times10^{-10}\,\mathrm{m\,Pa^{-1}}$, so $T \approx u/\tilde G \approx 0.5\times10^{-6}/2.9\times10^{-10} \approx 1.7\,\mathrm{kPa}$, and over $25\,\mu\mathrm{m^2}$ a force of about $40\,\mathrm{nN}$. For a passive force source, displacements would scale as $1/E$; but cells adapt their tractions to stiffness (clutch dynamics, reinforcement, myosin activity), generally pulling less on softer substrates, so the displacements change less than twofold.

4. In the clutch model, why does the traction fall on very soft and on very stiff substrates? Using Remark 31.3.1, how does the optimal stiffness change if the number of clutches is doubled, or if the motors pull twice as fast?

   **Answer** Soft: loading is slow, clutches engage in large numbers and fail together in long load-and-fail cycles; the mean traction is low because each cycle spends most of its time at low force. Stiff: loading is so fast that clutches break individually, before others bind, and the slipping bundle transmits little force. By $k^* \approx n_{\mathrm{b}}F_{\mathrm{b}}k_{\mathrm{on}}/v_{\mathrm{u}}$, doubling the clutches doubles $k^*$ (the optimum moves to stiffer substrates, because more clutches share the load and take longer to load), while doubling $v_{\mathrm{u}}$ halves it (faster loading). Cells can therefore tune their stiffness optimum by adhesion-protein expression and myosin activity.

5. (Based on a deterministic version of the clutch model.) Actin moves at $v = v_0(1 - F/F_{\mathrm{stall}})$ with $v_0 = 120\,\mathrm{nm\,s^{-1}}$ and $F_{\mathrm{stall}} = 150\,\mathrm{pN}$, connected through one clutch of stiffness $5\,\mathrm{pN\,nm^{-1}}$ (which never unbinds) to a substrate of stiffness $0.01$ or $100\,\mathrm{pN\,nm^{-1}}$. Find the time course of the substrate deformation and the actin speed on both substrates.

   **Answer** The clutch and substrate springs in series have stiffness $k = k_{\mathrm{c}}k_{\mathrm{s}}/(k_{\mathrm{c}} + k_{\mathrm{s}})$: $0.00998$ and $4.76\,\mathrm{pN\,nm^{-1}}$. The force grows as $\mathrm{d}F/\mathrm{d}t = kv_0(1 - F/F_{\mathrm{stall}})$, so $F = F_{\mathrm{stall}}(1 - \mathrm{e}^{-t/\tau})$ with $\tau = F_{\mathrm{stall}}/(kv_0)$: $\tau = 150/(0.00998 \times 120) \approx 125\,\mathrm{s}$ on the soft substrate and $0.26\,\mathrm{s}$ on the stiff one. The actin speed decays as $v_0\mathrm{e}^{-t/\tau}$, and the substrate deformation $F/k_{\mathrm{s}}$ approaches $15\,\mu\mathrm{m}$ (soft) or $1.5\,\mathrm{nm}$ (stiff). Physiologically, on stiff substrates the clutch reaches high force within a fraction of a second, which, once unbinding is allowed, means it breaks quickly (slip) unless it is reinforced; on soft substrates force builds over minutes, longer than the clutch lifetime, so the force at unbinding is small. Allowing unbinding (a slip bond) caps the force on each clutch near $F_{\mathrm{b}}\ln(\cdot)$ and produces the load-and-fail and slippage regimes of the figure.

6. A neutrophil migrates with $S = 10\,\mu\mathrm{m\,min^{-1}}$ and $P = 2\,\mathrm{min}$; a fibroblast with $S = 0.5\,\mu\mathrm{m\,min^{-1}}$ and $P = 30\,\mathrm{min}$. Compute their effective diffusion coefficients in two dimensions and the root-mean-square distance each travels in 1 h and in 1 day.

   **Answer** $D = S^2P/2$: neutrophil $100 \cdot 2/2 = 100\,\mu\mathrm{m^2\,min^{-1}}$; fibroblast $0.25 \cdot 30/2 = 3.75\,\mu\mathrm{m^2\,min^{-1}}$. From Eq. (31.5) at $t = 60\,\mathrm{min}$: neutrophil $2 \cdot 100 \cdot 2(60 - 2) = 23\,200\,\mu\mathrm{m^2}$, rms $152\,\mu\mathrm{m}$; fibroblast $2 \cdot 0.25 \cdot 30[60 - 30(1 - \mathrm{e}^{-2})] = 15(60 - 25.9) = 511\,\mu\mathrm{m^2}$, rms $23\,\mu\mathrm{m}$. At 1 day (1440 min), both diffusive: neutrophil $4Dt = 5.8\times10^5\,\mu\mathrm{m^2}$, rms $0.76\,\mathrm{mm}$; fibroblast $2.2\times10^4\,\mu\mathrm{m^2}$, rms $0.15\,\mathrm{mm}$.

7. For the gating-spring model with $K_\infty = 0.6\,\mathrm{pN\,nm^{-1}}$ and $z = 0.5\,\mathrm{pN}$ at $k_{\mathrm{B}}T = 4.1\,\mathrm{pN\,nm}$, how many channels are needed for negative stiffness? What does negative stiffness imply for a bundle held by a soft fiber versus a stiff one?

   **Answer** $N > 4k_{\mathrm{B}}TK_\infty/z^2 = 4 \times 4.1 \times 0.6/0.25 \approx 39$. With negative stiffness, the force–displacement curve is non-monotonic: a bundle loaded by a stiff probe (displacement clamp) can be held anywhere, revealing the negative slope, whereas under a soft probe (force clamp) the region is unstable and the bundle jumps between the two stable branches. Coupled to adaptation, the instability produces spontaneous oscillations.

8. Show that at a Hopf bifurcation the response to a force at the resonant frequency is $r = F^{1/3}$. If the threshold of hearing corresponds to a basilar-membrane displacement of $0.3\,\mathrm{nm}$ and the response at $60\,\mathrm{dB}$ above threshold is about $30\,\mathrm{nm}$, which law is closer: linear or one-third power?

   **Answer** See Proposition 31.5.1. A $60\,\mathrm{dB}$ increase is a factor of $10^3$ in pressure. A linear system would give $300\,\mathrm{nm}$; the one-third power gives $0.3 \times 10 = 3\,\mathrm{nm}$; the observed factor of 100 corresponds to an exponent $\log 100/\log 1000 = 2/3$. Measured cochlear responses lie between: compressive with exponents of about $0.2$–$0.5$ over the middle range, linear at the lowest levels, where the cochlea is slightly below the bifurcation.

9. Explain why a confluent epithelium can be solid or fluid at the same density, and how the shape index of its cells can be used to tell.

   **Answer** Confluence fixes the packing fraction at 1, so density does not control rigidity. In the vertex model the energy depends on cell area and perimeter; when the preferred shape index $p_0 = P_0/\sqrt{A_0}$ is below about $3.81$ (cortical tension dominating adhesion), cells cannot reach their preferred perimeter without stretching junctions and energy barriers to neighbor exchange are finite: solid. Above it (adhesion dominating), there are many zero-energy shapes, barriers to T1 transitions vanish and the tissue is fluid. The observed shape index of cells tracks the preferred one in the fluid phase and is pinned near $3.81$ in the solid phase, so elongated, irregular cells (shape index above about 3.8) indicate an unjammed tissue.

10. A $20\,\mu\mathrm{m}$-thick epithelial layer with modulus $5\,\mathrm{kPa}$ grows on a mesenchyme of $0.5\,\mathrm{kPa}$ (both incompressible). What wavelength of folds do you expect, and how does it change if the epithelium doubles its thickness?

    **Answer** With equal Poisson ratios the plane-strain factors cancel: $\lambda = 2\pi \times 20\,\mu\mathrm{m} \times (5/(3 \times 0.5))^{1/3} = 125.7 \times 1.494 \approx 190\,\mu\mathrm{m}$. Doubling the thickness doubles the wavelength ($\lambda \propto h$), to about $380\,\mu\mathrm{m}$; doubling the modulus ratio would increase it only by $2^{1/3} = 1.26$.

11. In the fiber-recruitment model, show that an exponential distribution of slack strains, $g(\varepsilon_{\mathrm{s}}) \propto \mathrm{e}^{b\varepsilon_{\mathrm{s}}}$ up to the current strain (equivalently, a population whose recruitment accelerates exponentially), gives the Fung law. What does the toe region of tendon tell you about its microstructure?

    **Answer** With $g = Ab\,\mathrm{e}^{b\varepsilon_{\mathrm{s}}}$ on the recruited range, the tangent modulus is $\phi E_{\mathrm{f}}\int_0^\varepsilon g = \phi E_{\mathrm{f}}A(\mathrm{e}^{b\varepsilon} - 1)$ and $\sigma = \phi E_{\mathrm{f}}(A/b)(\mathrm{e}^{b\varepsilon} - 1 - b\varepsilon)$, which for $b\varepsilon \gg 1$ grows as $\mathrm{e}^{b\varepsilon}$ with $\mathrm{d}\sigma/\mathrm{d}\varepsilon \approx b\sigma$: Fung's law. The extent of the toe region (about 2 % strain) measures the spread of crimp of the collagen fibrils; its shape measures the distribution of their slack lengths, and changes in it report damage or remodeling.

12. (Experimental design) Propose experiments to decide whether a cancer cell line migrates through three-dimensional matrices by a mesenchymal or an amoeboid mechanism, and whether its migration depends on substrate stiffness through a clutch.

    **Answer** Mode: image cells in collagen gels and in confining microchannels with labeled actin, myosin and integrins; mesenchymal cells show elongated shapes with Arp2/3-rich protrusions, focal adhesions and matrix degradation (inhibited by metalloprotease inhibitors, which arrest them), while amoeboid cells are rounded, blebbing, insensitive to protease inhibition and to integrin-blocking antibodies but sensitive to ROCK and myosin inhibition; test migration in nonadhesive (PEG-coated) channels, where only friction-based amoeboid migration works. Clutch: measure traction (TFM) and retrograde actin flow (speckle microscopy) on gels spanning $0.1$–$100\,\mathrm{kPa}$; a biphasic traction and inverse flow indicate an unreinforced clutch, a monotonic increase with talin-dependent adhesion growth indicates reinforcement; perturb clutch parameters (talin or vinculin knockdown, integrin density, myosin inhibition with blebbistatin) and compare the shift of the optimum with simulations of the model.
