---
title: Cell Motility
description: "Definition and types of cell motility; passive diffusion versus directed movement (x² = 2Dt and x = vt, diffusion time table); low Reynolds number, Stokes drag and the energy budget of swimming; bacterial flagella and eukaryotic cilia, power and recovery strokes, synchronization of ciliary arrays, ventricular flow and mucociliary clearance; directed migration on surfaces: the source–sink model of a gradient λ = √(D/k), relative gradients and the optimal concentration window, receptor counting noise and signal-to-noise ratio, amplification by PI3K/PTEN and the excitable network, weighted integration of multiple cues and winner-take-all; leading-edge protrusion, the molecular clutch, the Bell model and catch bonds, contraction and rear detachment, amoeboid migration; neutrophil homing, wound healing and sperm; convergent evolution of bacterial and eukaryotic motors, ciliary gliding in placozoans and the modes of migration across groups."
source_hash: 914238cb6e18
---

Movement is one of the most conspicuous physiological features of animals, but it begins at the cellular level: sperm swim toward the egg, neutrophils cross the vessel wall to reach a focus of infection, fibroblasts crawl into a wound, and cilia of the tracheal epithelium sweep mucus out of the lung. Cell motility obeys physics quite unlike that of macroscopic movement: at the scale of a cell, water is as viscous as honey, inertia is negligible, and diffusion is fast over micrometers but too slow to be useful over millimeters. This chapter first uses these physical rules to establish why cells must move actively, and how (Sections 2.1–2.3), then treats the two classes of cellular motors, flagella and cilia (Section 2.4), and then, taking directed migration of cells on surfaces as the example, discusses "which way to go" and "how to go" in two steps (Sections 2.5–2.6), and finally covers the role of these mechanisms in physiology and their evolution across groups (Sections 2.7–2.8).

The physical foundations of this chapter are derived in full in biophysics: the **random walk** and diffusion ([7.6.5](/7.6.5)), low **Reynolds number** hydrodynamics and swimming ([7.6.22](/7.6.22)), the mechanics of cell migration and the **molecular clutch model** ([7.6.31](/7.6.31)), and the physical limits of sensing ([7.6.35](/7.6.35)); for the molecular mechanisms, see actin ([7.3.13](/7.3.13)), microtubules and cilia ([7.3.14](/7.3.14)) and cell migration ([7.3.15](/7.3.15)) in cell biology. This chapter cites only their conclusions and concentrates on orders of magnitude and physiological context. Muscle contraction, the "organized form of cell motility", is covered in Chapters 8–10.

## 2.1. Definition and Types of Cell Motility

**Definition 2.1.1 (Cell Motility)** **Cell motility** is the movement of a cell as a whole, or of its components, from one place to another.

Movement of the whole cell includes swimming (bacteria, sperm, ciliates), migration on surfaces or within tissues (leukocytes, fibroblasts, neural crest cells), contraction (muscle cells) and division. Movement of cell components includes intracellular transport (**axonal transport** along **microtubules**, movement of secretory vesicles), chromosome segregation, outgrowth of axons and dendrites, **cytoplasmic streaming** and so on. They are driven by a few classes of molecular machines: myosin moving along **actin filaments**, **kinesin** and dynein moving along microtubules, polymerization and depolymerization of the **cytoskeleton** itself, and, in bacteria, rotary motors driven by ion flow.

## 2.2. Passive Diffusion and Directed Movement

### 2.2.1. Thermal Motion and Diffusion

Cells move even without expending metabolic energy. By the **equipartition theorem**, the mean kinetic energy of a particle of mass $m$ in each direction is $k_{\mathrm{B}}T/2$, that is, $\tfrac{1}{2}mv^2 = \tfrac{1}{2}k_{\mathrm{B}}T$, and the thermal velocity is
$$
v_{\mathrm{th}} = \sqrt{\frac{k_{\mathrm{B}}T}{m}}.
$$
For a bacterium of mass about $1\,\mathrm{pg}$, $v_{\mathrm{th}} \approx 2\,\mathrm{mm\,s^{-1}}$, but this velocity is randomized within about $10^{-7}\,\mathrm{s}$ by collisions with water molecules, and the bacterium actually performs an irregular **random walk**: the direction of displacement is random, the mean displacement is zero, and the **mean squared displacement** grows linearly with time. Along one coordinate axis,
$$
\langle x^2\rangle = 2Dt, \tag{2.1}
$$
where the **diffusion coefficient** $D$ is given by the Stokes–Einstein relation, $D = k_{\mathrm{B}}T/(6\pi\eta R)$, inversely proportional to the particle radius $R$ ([7.6.5](/7.6.5)).

### 2.2.2. Diffusion Is Ineffective over Long Distances

The distance of diffusion grows only with the square root of time: a tenfold increase in distance requires a hundredfold increase in time. The distance of directed movement, $x = vt$, is proportional to time. The table below is calculated from $t = x^2/2D$ in Eq. (2.1).

| Object | $D/(\mu\mathrm{m^2\,s^{-1}})$ | $1\,\mu\mathrm{m}$ | $10\,\mu\mathrm{m}$ | $1\,\mathrm{mm}$ |
|---|---|---|---|---|
| Small molecule (glucose, $\ce{O2}$) | $500$ | $1\,\mathrm{ms}$ | $0.1\,\mathrm{s}$ | $17\,\mathrm{min}$ |
| Protein | $50$ | $10\,\mathrm{ms}$ | $1\,\mathrm{s}$ | $3\,\mathrm{h}$ |
| Virus | $5$ | $0.1\,\mathrm{s}$ | $10\,\mathrm{s}$ | $1\,\mathrm{d}$ |
| Bacterium | $0.5$ | $1\,\mathrm{s}$ | $100\,\mathrm{s}$ | $12\,\mathrm{d}$ |
| Animal cell | $0.05$ | $10\,\mathrm{s}$ | $17\,\mathrm{min}$ | $116\,\mathrm{d}$ |

This table is the starting point of many physiological designs. Small molecules take only milliseconds to diffuse within a cell, so cells need no "pumping" of metabolites; but $\ce{O2}$ takes more than ten minutes to diffuse $1\,\mathrm{mm}$, so animals larger than about $1\,\mathrm{mm}$ need a circulatory system (Chapter 12). For a cell itself, passive diffusion is tolerable within about $5\,\mu\mathrm{m}$, and over longer distances directed movement is required: a neutrophil crawling at $10\,\mu\mathrm{m\,min^{-1}}$ needs less than 2 hours to travel $1\,\mathrm{mm}$, whereas by diffusion it would need several months.

![Distance covered by diffusion and by directed movement (log–log axes). Solid lines: root-mean-square displacement √(2Dt) along one axis, for diffusion coefficients of 500 (small molecule), 50 (protein), 0.5 (bacterium-sized particle) and 0.05 µm²/s (animal cell); dashed lines: directed movement x = vt for a crawling neutrophil at about 10 µm/min, a swimming bacterium at 25 µm/s and a swimming sperm at 50 µm/s. Diffusion wins over short distances, but the time it needs grows as the square of the distance; the intersection of the solid and dashed lines for the same object is the distance beyond which active movement pays](./plots/diffusion-vs-directed.py)

## 2.3. The World of Low Reynolds Number

### 2.3.1. Viscous Forces Dominate

An object moving in water must overcome two kinds of resistance: the inertial force that accelerates the fluid and the viscous force of internal friction in the fluid. Their ratio is the **Reynolds number** ([7.6.22](/7.6.22))
$$
\operatorname{Re} = \frac{f_{\text{inertial}}}{f_{\text{viscous}}} \sim \frac{\rho v^2L^2}{\eta vL} = \frac{\rho vL}{\eta}, \tag{2.2}
$$
where $v$ is the speed, $L$ the characteristic size, and $\rho$ and $\eta$ the density and viscosity of the liquid (water: $\rho = 10^3\,\mathrm{kg\,m^{-3}}$, $\eta = 10^{-3}\,\mathrm{Pa\,s}$). A human swimmer has $\operatorname{Re} \sim 10^6$, a fish $10^4$–$10^6$; a bacterium $2\,\mu\mathrm{m}$ long swimming at $30\,\mu\mathrm{m\,s^{-1}}$ has $\operatorname{Re} \approx 6\times10^{-5}$; a cell crawling in tissue is smaller still, about $10^{-9}$.

At $\operatorname{Re} \ll 1$ inertia can be ignored altogether: when a bacterium stops rotating its flagella it stops in less than a microsecond, after coasting less than the diameter of an atom. Motion is determined entirely by the forces acting at the moment, with no "coasting"; it also follows that a reciprocal, symmetric stroke (opening and closing like a scallop) cannot produce net displacement (the **scallop theorem**), and cells must swim with helical rotation or asymmetric beating. The drag on an object is proportional to its speed; for a sphere of radius $R$ this is **Stokes' law**
$$
F = 6\pi\eta Rv = 3\pi\eta Lv \quad (L = 2R).
$$

### 2.3.2. Swimming Is Not Expensive

**Example 2.3.1 (Energy Budget of Swimming)** A cell of diameter $L = 1\,\mu\mathrm{m}$ swimming through water at $v = 10\,\mu\mathrm{m\,s^{-1}}$ spends power against viscous drag of
$$
\mathcal{P} = Fv = 3\pi\eta Lv^2 = 3\pi \times 10^{-3} \times 10^{-6} \times (10^{-5})^2\,\mathrm{W} \approx 10^{-18}\,\mathrm{W}.
$$
The hydrolysis of one ATP releases about $10^{-19}\,\mathrm{J}$ (about $20\,k_{\mathrm{B}}T$), and bacterial metabolism produces about $10^7$ ATP per second, a power of about $10^{-12}\,\mathrm{W}$. Swimming itself therefore requires only about one millionth of the metabolic energy. Even allowing for a propulsion efficiency of the flagellum of only about $1\%$, the energy cost of swimming is only about one ten-thousandth (a more precise budget is in [7.6.22](/7.6.22)).

:::

For cells crawling on a surface, fluid drag is even more negligible. A fibroblast of diameter $10\,\mu\mathrm{m}$ moving at $1\,\mu\mathrm{m\,min^{-1}}$ experiences a Stokes drag $6\pi\eta Rv \approx 6\pi \times 10^{-3} \times 5\times10^{-6} \times 1.7\times10^{-8}\,\mathrm{N} \approx 2\times10^{-15}\,\mathrm{N}$, about $2\,\mathrm{fN}$, whereas the traction force such cells exert on the substrate is of the order of nanonewtons, about six orders of magnitude larger. The forces of a crawling cell are not used to "push water aside" but to overcome adhesion to the matrix, deform the cell body and squeeze it through the pores of the tissue (Section 2.6). In three-dimensional tissue, when pores are distinctly smaller than the nucleus, migration requires deformation of the nucleus or degradation of the matrix by proteases.

## 2.4. Flagella and Cilia

### 2.4.1. The Rotary Flagellum of Bacteria

Bacteria swim with the **bacterial flagellum**: a rigid helical filament is driven by a rotary motor at its base and pushes the cell forward like a propeller. The motor is driven by transmembrane flow of $\ce{H+}$ (of $\ce{Na+}$ in some marine bacteria), with energy from the **proton-motive force**; the stator consists of MotA/MotB complexes and the rotor ring of Fli proteins; each revolution requires about 1000 protons, and the speed can reach $100$–$300$ revolutions per second. An *Escherichia coli* cell about $2\,\mu\mathrm{m}$ long swims at $20$–$30\,\mu\mathrm{m\,s^{-1}}$, that is, 10–15 body lengths per second. Reversal of the motor makes the flagellar bundle fly apart, so the cell "tumbles" and changes direction at random, and bacteria achieve chemotaxis in this way ([7.6.35](/7.6.35)).

### 2.4.2. Cilia and Flagella of Eukaryotic Cells

The **cilia** and flagella of eukaryotic cells have the same structure (the "9 + 2" **axoneme**) and differ only in length and number: flagella are long and few (a sperm has one, about $50\,\mu\mathrm{m}$ long), cilia short and numerous (each airway epithelial cell has about 200, about $6\,\mu\mathrm{m}$ long). They do not rotate but beat by bending: the **dynein** arms on the outer doublet microtubules of the axoneme hydrolyze ATP and make adjacent doublets slide relative to one another, and constraints and linker proteins at the base convert sliding into bending ([7.3.14](/7.3.14)). How cilia coordinate their regular beating waveform is still an open problem and a field for mathematical and engineering modeling.

To produce net thrust at low Reynolds number, the beat of a cilium is asymmetric:

- The power stroke: the cilium is straight and sweeps backward quickly like an oar, driving a large volume of fluid;
- The recovery stroke: the cilium bends and returns slowly to its starting point close to the cell surface, disturbing little fluid.

The drag on a slender rod moving perpendicular to its length is about twice that for movement parallel to it (the **resistive-force theory** of [7.6.22](/7.6.22)); the two strokes differ in shape and speed, so over one cycle fluid is driven net in the direction of the power stroke. A eukaryotic flagellum (of a sperm) instead sends a bending wave from base to tip, and the propagation of the wave in the fluid produces thrust in the opposite direction.

**Definition 2.4.1 (Ciliary Motility)** The driving of the surrounding fluid, or of the cell itself, by the asymmetric beat of cilia, with alternating power and recovery strokes, is called **ciliary motility**.

An array of cilia fixed on an epithelium drives the adjacent layer of fluid. Neighboring cilia synchronize the frequency and phase of their beating through hydrodynamic coupling (and also through structural links between basal bodies), forming a *metachronal wave* in which successive cilia differ by a fixed phase, like wind passing over a wheat field. The ependymal epithelium of the mammalian brain ventricles is covered with multiciliated cells, whose synchronized beating produces near the ventricular wall a network of flows that are uniform in direction and distributed by region, taking part in the mixing of cerebrospinal fluid and the directed transport of molecules; ciliary orientation is determined by planar cell polarity. The cilia of the oviduct, together with smooth muscle, carry the egg toward the uterus.

### 2.4.3. Mucociliary Clearance

**Definition 2.4.2 (Mucociliary Clearance)** The cilia of the airway epithelium beat in a thin periciliary fluid and move the overlying mucus layer, with the particles and microorganisms adhering to it, toward the pharynx, where it is swallowed or coughed out; this is called **mucociliary clearance**.

The airway surface consists of two fluid layers: a periciliary layer about $7\,\mu\mathrm{m}$ thick and of low viscosity, in which the cilia beat, and above it a viscous mucus layer, which the cilium tips catch during the power stroke. The ciliary frequency is about $10$–$15\,\mathrm{Hz}$ and the speed of tracheal mucus is a few millimeters per minute. The system is extremely sensitive to the thickness of the fluid layers: the thickness of the periciliary layer is regulated by epithelial ion transport (CFTR secretes $\ce{Cl-}$ and ENaC absorbs $\ce{Na+}$, with water following, Chapter 3). In **cystic fibrosis** a CFTR defect thins the fluid layer and thickens the mucus, the cilia cannot beat, and repeated infections result; in primary ciliary dyskinesia (a class of **ciliopathy**) structural defects such as of the dynein arms prevent the cilia from beating, patients have chronic bronchitis and sinusitis, men are infertile because their sperm cannot swim, and about half the patients have **situs inversus** (Kartagener syndrome) because the asymmetric leftward flow generated by cilia at the embryonic node is absent. Smoking reduces the number of cilia and slows their beating.

## 2.5. Directed Migration on Surfaces (I): Choosing a Direction

Many cells do not swim but crawl attached to surfaces: neutrophils, macrophages and lymphocytes patrol the tissues, fibroblasts and keratinocytes repair wounds, **neural crest** cells and **primordial germ cells** in the embryo migrate to distant sites and settle, and tumor cells invade and metastasize. A cell about $10\,\mu\mathrm{m}$ in diameter moves at about $1\,\mu\mathrm{m\,min^{-1}}$ (fibroblasts) to $10$–$20\,\mu\mathrm{m\,min^{-1}}$ (neutrophils), toward the source of a chemical signal (**chemotaxis**), along the orientation of matrix fibers, or toward a stiffer substrate (**durotaxis**). This takes two steps: converting external cues into an internal front–rear polarity of the cell (choosing a direction), and then converting polarity into displacement through the coordinated work of cytoskeleton and adhesion (going forward). This section covers the first step.

### 2.5.1. Generation of Gradients

Chemotactic signals are diffusible molecules: formylated peptides synthesized by bacteria (such as fMLP) guide neutrophils to the focus of infection; C5a, produced by complement activation in tissue damage or infection, attracts neutrophils and monocytes; the chemokine CXCL12, secreted continuously by stromal cells of the bone marrow and lymph nodes, makes **hematopoietic stem cells** and lymphocytes home; and ATP and hydrogen peroxide released by damaged tissue are the earliest "damage signals". **Axon guidance** molecules (Slit, netrin, semaphorin, ephrin) guide **growth cones** in neural development ([7.5.21](/7.5.21)).

A stable gradient needs a source and a sink: the signal is released at the source and diffuses through the tissue while being cleared by degrading enzymes or scavenger receptors.

**Formula 2.5.1 (Source–Sink Model)** Let the signal molecule diffuse with diffusion coefficient $D$ and be cleared with first-order rate constant $k$, let the source maintain a constant concentration $C_0$ at $x = 0$, and let the concentration be zero far away. The steady-state concentration then satisfies $D\,\mathrm{d}^2C/\mathrm{d}x^2 - kC = 0$, with solution
$$
C(x) = C_0\,\mathrm{e}^{-x/\lambda}, \qquad \lambda = \sqrt{\frac{D}{k}}. \tag{2.3}
$$
The decay length $\lambda$ determines the range of the gradient.

This is exactly the **synthesis–diffusion–degradation model** of **morphogen** gradients in developmental biology ([7.5.11](/7.5.11)). By Eq. (2.3), cells can adjust the shape of a gradient by changing the clearance rate $k$: for a chemokine with $D = 100\,\mu\mathrm{m^2\,s^{-1}}$, $k = 0.01\,\mathrm{s^{-1}}$ (half-life about 70 s) gives $\lambda = 100\,\mu\mathrm{m}$. Nor do gradients rely wholly on free diffusion: many chemokines and morphogens bind to **glycosaminoglycans** of the **extracellular matrix**, forming fixed "haptotactic" gradients, or are stored as precursors and released after protease cleavage.

### 2.5.2. Detectable Gradients

The magnitude of a gradient can be measured in two ways: the absolute gradient $\mathrm{d}C/\mathrm{d}x$, and the relative difference $\Delta C/C$ between the front and rear of the cell. For an exponential gradient, the relative difference across the two ends of a cell of length $L$ is the same everywhere,
$$
\frac{\Delta C}{C} = 1 - \mathrm{e}^{-L/\lambda} \approx \frac{L}{\lambda} \quad (L \ll \lambda).
$$
Experiments show that amoeboid cells (neutrophils, *Dictyostelium*) can sense shallow gradients with a difference of only $1\%$–$2\%$ across the cell; mesenchymal cells such as fibroblasts require much steeper gradients (reportedly about $30\%$), which is related to the difference in their capacity for signal amplification (Section 2.5.4). For $L = 10\,\mu\mathrm{m}$, a relative difference of $2\%$ corresponds to $\lambda \approx 500\,\mu\mathrm{m}$ and $30\%$ to about $30\,\mu\mathrm{m}$.

The concentration itself must also be suitable. At too low a concentration too few receptors are bound and the gradient is lost in noise; at too high a concentration the receptors saturate, the occupancy at both ends approaches 1, and the difference vanishes. When the background concentration is near the **dissociation constant** $K_{\mathrm{d}}$ of the receptor, the receptor occupancy is most sensitive to concentration changes and gradient detection is most efficient. An effective chemotactic signal must therefore be not only steep enough, but also have a background concentration that falls within the receptor's "detectable window" (about $0.1$–$10\,K_{\mathrm{d}}$); a steep gradient (small $\lambda$) has a large front–rear difference, but the concentration falls out of the window within a few $\lambda$, so its range is short. For *Dictyostelium*, the minimum cAMP gradient measured is about $10^{-3}\,\mathrm{nM\,\mu m^{-1}}$, and for gradients above about $10\,\mathrm{nM\,\mu m^{-1}}$ the receptors saturate and the cell loses directionality instead: chemotaxis has an optimal range of gradients.

![Chemotactic gradients from the source–sink model. A: concentration profiles for λ = 30, 100 and 300 µm (source C₀ = 30 nM, logarithmic vertical axis); for D = 100 µm²/s they require clearance rate constants k = D/λ² = 0.11, 0.01 and 0.0011 s⁻¹, respectively. The gray band is the window 0.1–10 Kd within which the receptor (Kd = 1 nM) can read the gradient: the smaller λ is, the sooner the concentration falls out of the window. B: relative concentration difference ΔC/C = 1 − exp(−L/λ) across a cell 10 µm long; amoeboid cells can sense about 1–2%, fibroblasts need about 30%](./plots/gradient-lambda.py)

### 2.5.3. Receptor Counting Noise

Cells sense signals through **G protein–coupled receptors** (chemokine receptors, the fMLP receptor, the C5a receptor; humans have more than 50 chemokines and about 20 classical chemokine receptors) and **receptor tyrosine kinases** (chemotaxis of fibroblasts to PDGF and EGF). Directional information can come only from the difference in receptor occupancy between the front and rear of the cell, and this difference is extremely small.

**Example 2.5.1 (Signal-to-Noise Ratio of Gradient Sensing)** A rough estimate: an immune cell has about $N = 10^4$ receptors; if the concentration at the front is $1\%$ higher than at the rear, at most about 100 extra receptors are occupied, while the thermal fluctuation of the occupancy number is about $\sqrt N = 100$, so the signal-to-noise ratio is about 1.

More carefully, let half the receptors be at the front and half at the rear, each independently occupied with probability $p = C/(C + K_{\mathrm{d}})$. The occupancy numbers at front and rear are binomially distributed; the expected front–rear difference is $\tfrac{N}{2}p(1-p)\,\Delta C/C$ (because $\mathrm{d}p/\mathrm{d}\ln C = p(1 - p)$) and its variance is $Np(1 - p)$, so the signal-to-noise ratio of a single "snapshot" is
$$
\mathrm{SNR} = \frac{1}{2}\sqrt{Np(1-p)}\,\frac{\Delta C}{C} \le \frac{\sqrt N}{4}\,\frac{\Delta C}{C}, \tag{2.4}
$$
with the maximum at $C = K_{\mathrm{d}}$ ($p = 1/2$). For $N = 10^4$ and $\Delta C/C = 1\%$, the maximum signal-to-noise ratio is only $0.25$. The cell averages the occupancy state over time: if the correlation time of the receptor binding state is $\tau_{\mathrm{b}}$ (about the binding–unbinding time, of the order of seconds), an averaging time $T$ is equivalent to $T/\tau_{\mathrm{b}}$ independent snapshots and raises the signal-to-noise ratio by a factor of about $\sqrt{T/\tau_{\mathrm{b}}}$; averaging for 30 s can bring it above 1. This estimate shows three things: sensing a shallow gradient requires time averaging; the background concentration is best near $K_{\mathrm{d}}$ (the optimal window of Section 2.5.2); and with the receptors alone the cell can hardly judge direction reliably, so downstream amplification is needed. The physical limit of sensing accuracy (the **Berg–Purcell limit**) is treated in [7.6.35](/7.6.35).

![Gradient sensing limited by receptor counting noise (Eq. 2.4). N = 10⁴ receptors are divided equally between the front and rear halves of the cell, each occupied with probability p = C/(C + Kd); solid lines show the signal-to-noise ratio of a single snapshot for ΔC/C = 1%, 2% and 5%, maximal at background concentration C = Kd; the dashed line shows the result of averaging over 30 receptor correlation times for ΔC/C = 1%. The dotted line is SNR = 1](./plots/receptor-snr.py)

### 2.5.4. Polarization and Amplification

After receptor activation, the **G protein** βγ subunits and Ras at the front activate PI3K (**phosphoinositide 3-kinase**), which phosphorylates membrane $\mathrm{PIP_2}$ to $\mathrm{PIP_3}$; $\mathrm{PIP_3}$ recruits a **guanine nucleotide-exchange factor** for Rac, and activated Rac activates the **Arp2/3 complex** through the WAVE complex, promoting polymerization of a branched actin network and forming the **lamellipodium**. The phosphatase PTEN dephosphorylates $\mathrm{PIP_3}$ to $\mathrm{PIP_2}$ and is excluded to the rear; at the rear, RhoA phosphorylates the myosin light chain through ROCK and inhibits the light chain phosphatase, enhancing the contraction of **myosin II** (Rac at the front, Rho at the rear, [7.3.15](/7.3.15)).

A system that depends only on local receptor occupancy would be "excited" all over at a uniformly high concentration and could not tell direction. The **local excitation, global inhibition** (LEGI) model offers a solution: receptor activation produces at once a fast, local excitor (such as the activity of Ras-GTP and PI3K) and a slow inhibitor that diffuses through the whole cell (such as PTEN activity), and the response of the cell depends on the difference between the two. With uniform stimulation excitation and inhibition cancel, and the response is transient and adapts back to zero; in a gradient the excitation at the front exceeds the whole-cell average inhibition, and the response persists at the front. LEGI explains why amoeboid cells are sensitive to gradients but adapt to absolute concentration; its equations and properties of adaptation are in [7.3.15](/7.3.15) and [7.6.35](/7.6.35).

LEGI only compares, it does not amplify. Amplification comes downstream: $\mathrm{PIP_3}$ and newly formed F-actin recruit and activate more Ras/Rac signaling molecules, forming **positive feedback**; $\mathrm{PIP_3}$ at the front repels PTEN, and $\mathrm{PIP_2}$ at the rear enriches PTEN, so that front and rear inhibit each other, forming **bistability**. These fast positive and delayed negative feedbacks (RhoA, the turnover of actin) combine into an excitable network similar to the **action potential** (Chapter 4): exceeding a threshold gives an explosive local activation, which is then extinguished by negative feedback, appearing as actin waves propagating on the membrane and repeated extension of pseudopods. The small difference output by LEGI makes the threshold slightly lower at the front, so pseudopods appear more often there. The result of amplification stage by stage is that a receptor difference of about $1\%$ becomes, through the complementary distribution of PI3K/PTEN, a $\mathrm{PIP_3}$ difference of about $5\%$–$10\%$, and then, through the excitable network, a $\mathrm{PIP_3}$ level $5$–$20$ times higher at the front than at the rear, with several-fold differences in Rac activity and actin polymerization. Fibroblasts lack such strong amplification and rely on simpler receptor/PI3K saturation mechanisms, so they need steeper gradients, which suits slow and sustained wound migration.

### 2.5.5. Integration of Multiple Cues

In the physiological environment cells often face several gradients at once. Experiments and models show three rules:

1. Signal hierarchy: when a neutrophil faces opposing gradients of fMLP and CXCL8 (IL-8), it almost always migrates along fMLP, even if that gradient is shallower; the order of priority is that pathogen-derived "end-target signals" (fMLP, C5a) outrank host-derived "intermediate signals" (CXCL8, leukotriene B4). This allows a cell led to the vicinity of an infection by intermediate signals to turn toward the final target.
2. Weighted vector summation: cues that are not exactly opposed are summed linearly. For *Dictyostelium* guided simultaneously by a cAMP chemotactic gradient and a topographic gradient (micropillar spacing), the drift velocity $v_{\mathrm{A}}$ when the cues are aligned, $v_{\mathrm{O}}$ when they oppose, and $v_{\mathrm{T}}$ with the topographic gradient alone satisfy $v_{\mathrm{A}} + v_{\mathrm{O}} \approx 2v_{\mathrm{T}}$, that is, the total direction vector is $\boldsymbol{d} = \omega_{\mathrm{c}}\boldsymbol{c} + \omega_{\mathrm{t}}\boldsymbol{t}$ ($\boldsymbol{c}$ and $\boldsymbol{t}$ are the unit vectors in the directions of the two cues and $\omega$ the weights). The molecular basis of this algebraic summation is that different receptors share downstream effectors (for example, CXCR4 and **integrin** both act on the cytoskeleton through Rac1).
3. Winner-take-all: two signals of opposite direction and similar strength cause "pre-pseudopods" near threshold to appear on both sides at once, and the cell sways from side to side; as soon as activation on one side rises faster, it crosses the excitation threshold first, the explosive actin polymerization quickly consumes the limited G-actin of the whole cell, the raised membrane tension acts as a rapidly propagating global inhibition that suppresses protrusions on the opposite side, and PTEN is pushed to the weaker side. This competition for resources locks the cell into one direction.

## 2.6. Directed Migration on Surfaces (II): Producing Displacement

A cell that has established front–rear polarity must convert the polarity into displacement. Taking adhesion-dependent mesenchymal migration as the example, one migration cycle comprises four steps: leading-edge protrusion, front adhesion, contraction of the cell body, and rear detachment ([7.3.15](/7.3.15)).

### 2.6.1. Leading-Edge Protrusion

Beneath the plasma membrane at the leading edge, the Arp2/3 complex catalyzes the formation of a rapidly turning-over branched actin network, and continued polymerization pushes the membrane outward as lamellipodia (flat) or **filopodia** (finger-like). How does polymerization generate force? The answer of the **Brownian ratchet** model is that thermal fluctuations briefly open a gap between the membrane and the filament end; after a monomer inserts, the filament has grown by one step and the gap cannot reverse, so random fluctuations are rectified into directed advance ([7.3.13](/7.3.13)). The advance speed under an applied load $F$ is
$$
v(F) \approx \delta\left[k_{\mathrm{on}}C\,\mathrm{e}^{-F\delta/k_{\mathrm{B}}T} - k_{\mathrm{off}}\right], \tag{2.5}
$$
where $\delta$ is the length by which each monomer lengthens the filament.

**Example 2.6.1 (Advance Speed and Stall Force of an Actin Filament)** Take $\delta = 2.7\,\mathrm{nm}$ (each subunit lengthens the double-helical filament by $2.7\,\mathrm{nm}$), $k_{\mathrm{on}} = 11.6\,\mu\mathrm{M^{-1}\,s^{-1}}$, free monomer $C = 10\,\mu\mathrm{M}$ and $k_{\mathrm{off}} = 1\,\mathrm{s^{-1}}$. Without load, $v = 2.7\,\mathrm{nm} \times 115\,\mathrm{s^{-1}} \approx 0.3\,\mu\mathrm{m\,s^{-1}}$, about $19\,\mu\mathrm{m\,min^{-1}}$, of the same order as the leading-edge speed of fast cells. Setting $v = 0$ gives the **stall force** $F_{\mathrm{s}} = (k_{\mathrm{B}}T/\delta)\ln(k_{\mathrm{on}}C/k_{\mathrm{off}}) = (4.1/2.7) \times \ln 116\,\mathrm{pN} \approx 7\,\mathrm{pN}$. The leading edge has several hundred filament ends per square micrometer, of which only the fraction with suitable orientation and length that are in a growing state push the membrane; branching and **nucleation** continually supply new ends, and **capping proteins** limit the elongation of existing filaments and regulate network turnover.

:::

Protrusion of the leading edge does not mean advance of the cell. If the polymerizing network is not coupled to the outside, the resistance of the membrane pushes the whole network backward, forming retrograde actin flow, and the cell stays in place.

### 2.6.2. Front Adhesion: The Molecular Clutch

What converts retrograde flow into traction is adhesion. Small nascent adhesions first form between the new leading edge and the substrate, and some of them mature under tension into **focal adhesions**, which connect the actin network to the extracellular matrix through **integrin**, talin and vinculin. According to the **molecular clutch model** ([7.6.31](/7.6.31)), each connection behaves like a spring that bears a force $F_{\mathrm{c}} = k_{\mathrm{c}}\Delta x$ ($\Delta x$ is the relative displacement between network and substrate): with too few connections the network flows freely backward and there is no traction; with intermediate numbers retrograde flow slows, the internal tension is transmitted to the substrate and the cell advances; if adhesion is too strong and turns over too slowly the cell is pinned in place. Migration speed therefore has a biphasic dependence on adhesion strength, first rising and then falling.

The lifetime of a single connection under force is described by the **Bell model** ([7.6.17](/7.6.17)):
$$
k_{\mathrm{off}}(F) = k_0\,\mathrm{e}^{F/F_{\mathrm{b}}}, \qquad F_{\mathrm{b}} = \frac{k_{\mathrm{B}}T}{x_{\mathrm{b}}},
$$
where $x_{\mathrm{b}}$ is the distance from the bound state to the transition state (a few tenths of a nanometer, with $F_{\mathrm{b}}$ of a few to a few tens of piconewtons). This is a **slip bond**, "the harder it is pulled, the easier it breaks"; but the bond between integrin and ligands such as **fibronectin** has a lifetime that instead lengthens at low to moderate force, behaving as a **catch bond** ([7.3.23](/7.3.23)), and talin unfolded under force exposes more vinculin binding sites, so that adhesion is strengthened under load. Adhesion is thus a dynamical system that continually assembles, strengthens and turns over under force, and is the basis on which cells sense matrix stiffness (**durotaxis**).

### 2.6.3. Contraction of the Cell Body and Rear Detachment

After the leading edge has established load-bearing adhesions, the cell must still bring its cell body forward. Nonmuscle myosin II is the driver of this step: upstream RhoA–ROCK raises its contractility, and downstream **stress fibers**, **cortical tension** and mature adhesions organize local cytoskeletal activity into forces at the scale of the cell. The total contractile force can be written roughly as $F \approx N_{\mathrm{myo}}f_{\mathrm{myo}}$, the sum of a large number of cooperatively loaded myosin units (a few piconewtons each). Measured by **traction force microscopy**, traction is unevenly distributed across the front, middle and rear of the cell and is continually established, fluctuates and is redistributed through the migration cycle; contractile tension is transmitted to the substrate through focal adhesions, and the mechanical load in turn promotes stabilization of focal adhesions and thickening of stress fibers, forming feedback.

If the old adhesions at the rear are all retained, contraction pulls on both front and rear at once, and the cell restrains itself and stays put. Rear detachment is not passive rupture but regulated disassembly: FAK–Src signaling promotes turnover of the adhesion complex; the $\ce{Ca^2+}$-dependent protease calpain cleaves talin and FAK; and dynamic microtubules repeatedly target focal adhesions and recycle integrins by endocytosis mediated by **clathrin** and **dynamin**. Only if the traction at the front and the contraction in the middle and rear are not cancelled by old anchorage can the migration cycle close.

### 2.6.4. Amoeboid Migration

**Definition 2.6.1 (Amoeboid Migration)** Movement of a cell under conditions of weak adhesion, or without typical focal adhesions, mainly through contraction of the cortical actomyosin, deformation of the cell, and friction with and geometric interlocking against the surroundings, is called **amoeboid migration**.

The fast movement of leukocytes in the **interstitium** and the movement of *Dictyostelium* and many protists belong to this class. Compared with mesenchymal migration, its front protrusions are often "blebs" as well as pseudopods pushed out by actin polymerization: the local cortex detaches from the plasma membrane, intracellular hydrostatic pressure pushes the membrane out, and actin then repolymerizes inside the protrusion. Force transmission no longer relies on specific integrin adhesion but on nonspecific friction and on squeezing in narrow spaces; overall it relies more on posterior contraction by RhoA–ROCK–myosin II driving cytoplasmic flow forward, and the attachments at the tail are brief and weak and detach quickly. Amoeboid migration is fast ($10$–$20\,\mu\mathrm{m\,min^{-1}}$) and depends little on the matrix, which suits immune cells patrolling various tissues. The same cell can switch between the two modes according to the environment (strength of adhesion, degree of confinement, matrix stiffness), called plasticity of migration; this plasticity of tumor cells makes it hard for a single antimetastatic drug (such as a protease inhibitor) to work.

## 2.7. Physiological Contexts

### 2.7.1. Recruitment of Neutrophils

Chemokines released at a focus of infection and **selectins** upregulated on endothelial cells make neutrophils in the bloodstream roll on the venular wall (selectin–ligand bonds are catch bonds, which bind more firmly under blood shear flow); on contact with chemokines on the endothelial surface, integrins (LFA-1, Mac-1) are activated from inside and bind firmly to ICAM-1, the cell stops and spreads, passes through the junctions between endothelial cells, and then migrates along the gradient in the tissue at about $20\,\mu\mathrm{m\,min^{-1}}$ to the focus of infection, where it phagocytoses bacteria guided by end-target signals such as fMLP (the physiology of leukocytes is in Chapter 11, and the immunological mechanisms in [7.15](/7.15)).

### 2.7.2. Wound Healing

Within minutes of skin injury, gradients of ATP and hydrogen peroxide released by damaged cells (extending to about $200\,\mu\mathrm{m}$ in zebrafish) summon leukocytes; PDGF, TGF-β and other factors secreted by platelets and macrophages then make fibroblasts migrate into the wound by the mesenchymal mode at about $1\,\mu\mathrm{m\,min^{-1}}$, while epidermal keratinocytes cover the wound surface by collective migration.

### 2.7.3. Sperm

Human sperm swim at about $25$–$70\,\mu\mathrm{m\,s^{-1}}$, and the frequency of the bending wave of the flagellum is about $10$–$20\,\mathrm{Hz}$. In the female reproductive tract, after **capacitation** sperm switch to high-amplitude, asymmetric "hyperactivated" beating and may use chemotaxis (progesterone secreted by cumulus cells activates the sperm-specific $\ce{Ca^2+}$ channel CatSper), thermotaxis, rheotaxis (swimming against flow) and other cues to approach the egg; in externally fertilizing species such as sea urchins, peptides released by the egg cause clear chemotaxis of sperm (for fertilization see [7.5.4](/7.5.4)).

## 2.8. Evolution and Comparison

### 2.8.1. Convergent Evolution: Different Solutions to the Same Problem

Bacteria and eukaryotic cells both swim with a "hair", but the two are not homologous in any way. The bacterial flagellum is a rotary motor driven by transmembrane ion flow, and the filament is a passive propeller; the flagellum of archaea (the **archaellum**) also rotates but is driven by ATP and is homologous to the bacterial **type IV pilus**, a third independent invention. The eukaryotic cilium is an ATP-driven internal bending machine, with the whole axoneme doing work. Under the constraint of low Reynolds number, a rotating helix and an asymmetric beat are the two basic ways of breaking the scallop theorem, and natural selection found each separately.

### 2.8.2. *Trichoplax*: Coordinated Movement without Nerves or Muscles

The placozoan *Trichoplax adhaerens* has only a few cell types and no neurons or muscles, yet it can glide on a substrate, turn and stop to feed. It glides by the beating of thousands of cilia of the ventral epithelium; several neuropeptides secreted by gland cells can stop the cilia from beating or change the mode of movement of the whole animal, the signals diffusing through the tissue so that distant cilia change their activity in a coordinated way, and the movement pattern also switches between random wandering and directed or rotating movement. This is a primitive form of "chemical signals coordinating ciliary motility" and suggests that before the nervous system appeared, animals could already integrate whole-body movement through secreted signals.

### 2.8.3. Models of Migration and the Distribution of Migration Modes

*Dictyostelium* (a social amoeba) aggregates toward a source of cAMP when starved, with pulses of cAMP relayed through the cell population, a classical system for studying chemotaxis and LEGI ([7.5.13](/7.5.13)). The epidermal keratocytes of fish scales keep an almost constant shape and glide at more than ten micrometers per minute, an ideal model for studying lamellipodial mechanics.

Pseudopodial movement based on actin polymerization is widely distributed among the major groups of eukaryotes (amoebae, slime molds, foraminiferans, and the immune cells of animals) and is very probably an ancestral eukaryotic trait. Choanoflagellates (the closest unicellular relatives of animals) normally swim with a flagellum and can switch to amoeboid crawling when confined in narrow spaces, suggesting that the migratory plasticity of animal cells may have preceded **multicellularity**. **Apicomplexan** parasites (*Plasmodium*, *Toxoplasma*) glide by using myosin A beneath the plasma membrane to pull on transmembrane adhesion proteins, at speeds of several micrometers per second; **myxobacteria** and diatoms each have their own distinctive gliding mechanisms. In animals the function of ciliary motility shifts gradually from "propelling the individual" to "propelling fluid": from the ciliary bands used for swimming by larvae to the multiciliated epithelia that move fluid in the airway, brain ventricles and oviduct of the adult.

## Summary

| Topic | Relations and values |
|---|---|
| Cell motility (Definition 2.1.1) | Whole cell (swimming, migration, contraction, division) and components (transport, chromosome segregation, axon growth) |
| Diffusion | $\langle x^2\rangle = 2Dt$ (Eq. 2.1); distance ×10 needs time ×100; $1\,\mathrm{mm}$ takes about $17\,\mathrm{min}$ for a small molecule and about $100\,\mathrm{d}$ for an animal cell; directed movement is needed beyond about $5\,\mu\mathrm{m}$ |
| Low Reynolds number | $\operatorname{Re} = \rho vL/\eta$ (Eq. 2.2); bacteria $\sim 10^{-5}$; no inertia, reciprocal motion is ineffective; Stokes drag $3\pi\eta Lv$ |
| Energy | Swimming power $\sim 10^{-18}\,\mathrm{W}$ versus metabolism $\sim 10^{-12}\,\mathrm{W}$ (Example 2.3.1); fluid drag on a crawling cell about fN, traction about nN |
| Motors | Bacterial flagellum: rotary motor driven by the proton-motive force, $20$–$30\,\mu\mathrm{m\,s^{-1}}$; cilia and eukaryotic flagella: dynein-driven bending, power and recovery strokes (Definition 2.4.1), synchronized metachronal waves; mucociliary clearance (Definition 2.4.2) |
| Gradients | Source–sink $C = C_0\mathrm{e}^{-x/\lambda}$, $\lambda = \sqrt{D/k}$ (Formula 2.5.1); $\Delta C/C \approx L/\lambda$; amoeboid cells about $1\%$–$2\%$, fibroblasts about $30\%$; background concentration near $K_{\mathrm{d}}$ is optimal |
| Noise | $\mathrm{SNR} \le (\sqrt N/4)(\Delta C/C)$ (Eq. 2.4); for $N = 10^4$ and $1\%$ a snapshot gives $0.25$, so time averaging and downstream amplification are needed |
| Amplification and integration | PI3K/PTEN complementary at front and rear; LEGI compares; positive-feedback excitable network amplifies $5$–$20$-fold; signal hierarchy, weighted vector summation, winner-take-all |
| Displacement | Brownian ratchet $v(F)$ (Eq. 2.5), stall force about $7\,\mathrm{pN}$ (Example 2.6.1); biphasic dependence of the molecular clutch; Bell model and catch bonds; myosin II contraction; regulated rear detachment; amoeboid migration (Definition 2.6.1) |
| Evolution | Three independent origins of bacterial, archaeal and eukaryotic motors; chemically coordinated ciliary gliding in *Trichoplax*; ancient origin of pseudopodial movement and plasticity of migration |

## Questions

1. About how long does insulin take to diffuse from a capillary to a cell $10\,\mu\mathrm{m}$ away? What happens if the capillary spacing in the tissue becomes $1\,\mathrm{mm}$? (Take $D = 100\,\mu\mathrm{m^2\,s^{-1}}$ for insulin.)

   **Answer** $t = x^2/2D = (10)^2/200\,\mathrm{s} = 0.5\,\mathrm{s}$. A hundredfold increase in distance increases the time $10^4$-fold, to about $5000\,\mathrm{s}$, more than an hour, far longer than hormones need to act. Capillary spacing in metabolically active tissues is therefore only a few tens of micrometers, so that diffusion distance and the design of the circulation match each other (Chapter 15).

2. A cell $10\,\mu\mathrm{m}$ in diameter moves through water at $20\,\mu\mathrm{m\,s^{-1}}$; calculate its Reynolds number. If it suddenly stops propelling itself, about how far will it coast?

   **Answer** $\operatorname{Re} = \rho vL/\eta = 10^3 \times 2\times10^{-5} \times 10^{-5}/10^{-3} = 2\times10^{-4}$. The decay time of inertia is $\tau = m/(6\pi\eta R)$; with $m = \rho\cdot\frac{4}{3}\pi R^3 = 5.2\times10^{-13}\,\mathrm{kg}$ and $6\pi\eta R = 9.4\times10^{-8}\,\mathrm{kg\,s^{-1}}$, $\tau \approx 5.6\,\mu\mathrm{s}$; the coasting distance is $v\tau \approx 0.1\,\mathrm{nm}$, about the size of an atom. At the scale of a cell motion is determined entirely by the forces acting at the moment.

3. A chemokine has diffusion coefficient $D = 80\,\mu\mathrm{m^2\,s^{-1}}$ and is cleared by scavenger receptors on cell surfaces at $k = 0.02\,\mathrm{s^{-1}}$. Find the decay length of the gradient and the relative concentration difference across a neutrophil $15\,\mu\mathrm{m}$ long. What happens if scavenger receptors in the tissue are halved?

   **Answer** $\lambda = \sqrt{D/k} = \sqrt{4000} \approx 63\,\mu\mathrm{m}$; $\Delta C/C = 1 - \mathrm{e}^{-15/63} \approx 21\%$, a very strong gradient for a neutrophil. When $k$ is halved, $\lambda$ increases by a factor of $\sqrt2$ to about $89\,\mu\mathrm{m}$ and the relative difference falls to about $15\%$: the gradient is shallower but its range is greater; at the same time the background concentration at a distance rises and may saturate the receptors.

4. Using Eq. (2.4), explain why a fourfold increase in the number of receptors raises the signal-to-noise ratio only twofold. What else can the cell do to improve the accuracy of gradient sensing?

   **Answer** The signal (the difference of the front and rear occupancy numbers) is proportional to $N$, and the noise (the standard deviation of the binomial distribution) to $\sqrt N$, so the signal-to-noise ratio is $\propto \sqrt N$. Other means: averaging over time (signal-to-noise ratio $\propto \sqrt{T/\tau_{\mathrm{b}}}$), at the cost of a slower response; tuning the background concentration to near $K_{\mathrm{d}}$, or expressing receptors of different affinities to cover a wider concentration range; receptor adaptation (LEGI), so that the cell always works in the sensitive range; comparing concentrations at different times while moving (temporal comparison, the strategy of bacteria); and nonlinear amplification downstream (which cannot improve the signal-to-noise ratio but can turn a weak difference into a clear decision).

5. Why does the speed of mesenchymal migration first rise and then fall with adhesion strength? Under what circumstances does a cell switch to amoeboid migration?

   **Answer** Migration needs traction (front adhesion converts retrograde actin flow into pulling force on the matrix) and release (rear adhesion detaches in time). If adhesion is too weak retrograde flow cannot be "clutched" and traction is insufficient; if adhesion is too strong the rear cannot detach, front and rear restrain each other, and the cell is anchored. At intermediate strength the two balance and the speed is maximal. When adhesion is very weak (integrins blocked, matrix lacking ligands), when the cell is in a highly confined three-dimensional space (narrow channels), or when RhoA–ROCK contractility is very high, the cell switches to amoeboid migration relying on cortical contraction, blebbing protrusions and friction.

6. (Open question) Why do patients with primary ciliary dyskinesia have chronic respiratory infections, male infertility and situs inversus at the same time? Explain from the structure and function of cilia.

   **Answer** All three are caused by defects in the axoneme of motile cilia (such as loss of the outer dynein arms). Airway cilia cannot beat, mucociliary clearance fails, pathogens and particles are retained, and bronchitis, bronchiectasis and sinusitis follow; the axoneme of sperm flagella is the same as that of cilia, so sperm cannot swim; the single motile cilia at the embryonic node rotate clockwise and produce a leftward flow that establishes left–right asymmetric signaling, and when the cilia do not move the left–right decision becomes random, so about half the patients have **situs inversus**. Involvement of the oviductal cilia in women may reduce fertility.
