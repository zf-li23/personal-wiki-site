---
title: "Introduction: Questions, Scales and Models in Biophysics"
description: What biophysics studies and how it is organized (molecular biophysics, cell biophysics, quantitative biology); a short history from the Berlin school, target theory and What Is Life? to structural biology, single molecules and AlphaFold; the length, time and energy scales of life; the cell by the numbers (E. coli as a ruler, order-of-magnitude estimates of proteins, ribosomes, concentrations and times); and how to build a model, with HIV dynamics under therapy as a worked case.
---

Biophysics asks what living matter is made of, how it is put together and how it works, and it answers in the language of physics: forces and energies, probabilities and rates, equations whose parameters can be measured. The questions are biological (how a protein recognizes its target, how a cell senses a gradient, how a genetic circuit keeps time), but the answers are expected to be quantitative and, where possible, to follow from a small number of physical principles. This chapter sets out what the field covers and how this course is organized (1.1), recalls how the field came to be (1.2), introduces the scales of length, time and energy at which life operates (1.3), surveys how gravity, electromagnetic forces, electricity, light and temperature act in living systems and what kinds of order they must explain (1.4), describes the materials of the cell and how far simple estimates go in describing it (1.5), and discusses what a physical model of a biological process is and how one is built, with the dynamics of HIV under therapy as a worked case (1.6). The physics used here is that of the physics courses ([5.2](/5.2) for thermodynamics, [5.5](/5.5) for quantum physics) and of [physical chemistry](/6.3); the biology is that of [biochemistry](/7.1), [molecular biology](/7.2) and [cell biology](/7.3), whose orders of magnitude were collected in [7.2.1](/7.2.1#sec-1.5) and [7.3.1](/7.3.1#sec-1.3); the census of the cell is taken up in detail in [7.6.20](/7.6.20). The next two chapters build the statistical physics on which the rest of the course rests.

## 1.1. What Biophysics Studies

### 1.1.1. Two Meanings of Biophysics

The word is used in two ways, and both are needed.

- *Physics applied to biology*: physical instruments and theories used to answer biological questions. X-ray crystallography, nuclear magnetic resonance, electron microscopy, calorimetry, fluorescence and optical traps measure the structures, energies and motions of biological molecules; the laws of mechanics, electricity and thermodynamics explain how muscles pull, how nerves conduct and how membranes keep ions apart. Here biology supplies the questions and physics the tools, and the emphasis is on the diversity and specificity of living systems.
- *Physics of living matter*: the search for physical principles that are special to living systems, or that living systems reveal most clearly: how molecular machines run far from equilibrium, how cells compute with noisy components, how order at one scale emerges from interactions at a smaller one. Here the emphasis is on simplicity and universality, and the answers are new physics rather than old physics in a new setting.

The two meet constantly: a technique such as single-molecule fluorescence was developed to measure particular molecules and then revealed general facts about fluctuations, and a general theory such as that of kinetic proofreading told experimenters what to measure.

### 1.1.2. Three Directions

A convenient map of the field, used throughout this course, divides it by scale and by the kind of law sought.

| Direction | Scale | Typical questions | Main methods | Chapters |
|---|---|---|---|---|
| Molecular biophysics | $0.1$–$100\,\mathrm{nm}$, ps to s | Structures of proteins, nucleic acids and their complexes; folding, recognition, assembly; how structure produces function | X-ray crystallography, NMR, **cryo-electron microscopy**, scattering, spectroscopy, calorimetry, single-molecule methods, simulation and structure prediction | 7.6.7–7.6.19 |
| Cell biophysics | $10\,\mathrm{nm}$–$100\,\mu\mathrm{m}$, ms to h | Physical behavior with units and magnitudes at the scale of cells: the cell's census, DNA as a polymer, swimming at low Reynolds number, crowding, membrane shape and mechanosensitive channels, filament mechanics, motors, phase separation, bioelectricity, cell mechanics | Microscopy, force measurements, electrophysiology, hydrodynamics, polymer and membrane theory | 7.6.20–7.6.31 |
| Quantitative biology | Molecules to populations | Abstract quantitative regularities: noise in gene expression, the dynamics of genetic circuits, the limits of sensing, adaptation, patterns, the cost of nonequilibrium function, growth laws | Stochastic processes, dynamical systems, information theory, nonequilibrium statistical mechanics, single-cell measurement | 7.6.32–7.6.41 |

Molecular biophysics is to a large extent structural biology, the determination of the three-dimensional structures of biological macromolecules and the physics of the methods used to determine them; it is the largest part of this course because the methods themselves are applied physics (diffraction, spin dynamics, electron optics). Cell biophysics deals with physical quantities that have dimensions, such as forces in piconewtons, viscosities and bending stiffnesses, at the scale of the cell. Quantitative biology is closer to theoretical and mathematical biology: it looks for relations between dimensionless quantities that hold across systems, for example that the precision of a sensor is bounded by the number of molecules it counts, or that the growth rate of a bacterium is proportional to its ribosome content.

### 1.1.3. Plan of the Course

The course has four parts and a summary.

- Foundations (7.6.1–7.6.6): statistical physics of the cell (entropy, free energy, chemical potential, binding and rates), two-state systems and cooperativity, random walks and diffusion, and interactions and electrostatics in water.
- Molecular biophysics (7.6.7–7.6.19): the physical architecture of macromolecules; the experimental methods of structural biology (calorimetry and hydrodynamics, scattering, X-ray crystallography, optical spectroscopy, single-molecule fluorescence, magnetic resonance, cryo-electron microscopy) and computation; then the molecular physics built on them (folding, single-molecule mechanics and recognition) and the interaction of molecules with light and magnetic fields.
- Cell biophysics (7.6.20–7.6.31): the cell by the numbers, the polymer physics of DNA, low Reynolds number, crowding, membranes and mechanosensitive channels, cytoskeletal filaments, molecular motors, self-assembly and phase separation, bioelectricity and cell mechanics.
- Quantitative biology (7.6.32–7.6.41): stochastic kinetics, circuits and complex networks, the physical limits of sensing and chemotaxis, intracellular patterns, active matter, life far from equilibrium, growth laws, robustness, and the physics of sequences and evolution.

A summary chapter (7.6.42) collects the models, methods and numbers.

The course connects to two later ones. [Systems biology](/7.9) treats the design principles of networks (network motifs, the general theory of oscillators and synchronization, the propagation of noise, network inference from omics data); this course treats the physical limits and the mechanistic models of particular systems. [Computational neuroscience](/7.16) treats simplified neuron models, synapses and networks; this course derives the physics of channels, membrane potentials and the Hodgkin–Huxley model.

## 1.2. A Short History

### 1.2.1. The Berlin School

In the 1840s four young physiologists in Berlin, Hermann von Helmholtz, Emil du Bois-Reymond, Ernst von Brücke and Carl Ludwig, set out a program: a vital phenomenon counts as explained only when it is shown to result from the material components of the organism interacting according to the same laws that govern them outside living systems. They made physiology experimental and quantitative. Helmholtz measured the conduction velocity of the frog's nerve in 1850 (about $30\,\mathrm{m\,s^{-1}}$, far slower than electricity in a wire, the first hint that the nerve impulse is not a current in a conductor) and was one of the founders of the law of conservation of energy, which he applied to muscle heat. Adolf Fick, a pupil of Ludwig, wrote the first textbook of medical physics (1856) and the law of diffusion that bears his name (1855). The program was premature: nineteenth-century physics and chemistry could not provide molecular explanations, and of its fields only the mechanics and energetics of muscle and the electrophysiology of nerve continued unbroken into modern biophysics.

### 1.2.2. Radiation, Mutation and the Size of a Gene

The first institutes called "biophysical" appeared in Germany in the 1920s, and until about 1940 their main subject was the action of radiation on organisms. In 1927 Hermann Muller showed that X-rays cause mutations in *Drosophila*. The quantitative analysis of this effect produced the first physical model of the gene.

**Definition 1.2.1 (Target Theory)** **Target theory** describes the biological effect of ionizing radiation by assuming that the effect occurs when one (or a fixed number) of the discrete ionization events produced by the radiation falls within a sensitive volume, the target. Ionizations are scattered at random, so the number of hits in a target of volume $v$ is Poisson distributed with mean $\sigma D$, where $D$ is the dose (ionizations per unit volume) and $\sigma = v$. For a one-hit target the fraction of targets affected is

$$
f(D) = 1 - \mathrm{e}^{-\sigma D} \approx \sigma D \quad (\sigma D \ll 1). \tag{1.1}
$$

The **Poisson distribution** ([3.1.4](/3.1.4)) of hits gives the two signatures of a one-hit target: the effect is linear in dose at low dose, with no threshold, and the response does not depend on how the dose is delivered (fast or slow, by X-rays or γ-rays) once it is expressed as ionizations per volume. A target that needs two hits responds as $1 - \mathrm{e}^{-\sigma D}(1 + \sigma D) \approx (\sigma D)^2/2$, quadratically.

In 1935 Nikolai Timoféeff-Ressovsky, Karl Zimmer and Max Delbrück published an analysis of radiation-induced mutation in *Drosophila* that became known as the "three-man paper". The mutation frequency rose linearly with dose and did not depend on the wavelength of the radiation at equal ionization. Interpreted by Eq. (1.1), the slope gives the volume of the target; it came out as a sphere a few nanometers across, containing about a thousand atoms. Delbrück concluded that a gene is a single molecule, or part of one, whose structure can be changed by a single molecular event; the spontaneous mutation rate and its dependence on temperature fit a stable molecule whose rearrangement must cross an energy barrier of the order of an electronvolt. The conclusion was right, although the numerical size was not: the target volume reflects the spread of damage rather than the extent of a gene.

### 1.2.3. What Is Life?

Erwin Schrödinger gave lectures in Dublin in 1943, published in 1944 as *What Is Life?*, that drew two physical conclusions from this work.

The first concerns the stability of heredity. A system of $N$ particles in thermal equilibrium fluctuates in its macroscopic properties by about $1/\sqrt{N}$ (the "$\sqrt{N}$ rule", the scaling of the **central limit theorem**, [3.1.13](/3.1.13)). If a gene of a thousand atoms behaved like a small gas, it would fluctuate by about 3 %, whereas genes are copied with error rates of $10^{-5}$ to $10^{-8}$ per generation. The order of the gene therefore cannot be the statistical order of large numbers. Schrödinger concluded that the atoms of a gene are held in place like those of a crystal, by chemical bonds, and estimated their stability with a **Boltzmann factor**: a configuration separated from its neighbors by an energy barrier $W$ survives on average

$$
\tau = \tau_0\,\mathrm{e}^{W/k_{\mathrm{B}}T}, \qquad \tau_0 \approx 10^{-13}\text{–}10^{-14}\,\mathrm{s}, \tag{1.2}
$$
the period of a molecular vibration. With $\tau_0 = 10^{-14}\,\mathrm{s}$, a barrier of $30\,k_{\mathrm{B}}T$ gives $0.1\,\mathrm{s}$, $50\,k_{\mathrm{B}}T$ gives about 16 months and $60\,k_{\mathrm{B}}T$ about $30\,000$ years: the exponential converts a modest range of barriers (about $1$–$1.5\,\mathrm{eV}$) into the whole range from unstable to permanent, and quantum mechanics, which makes bond energies discrete and large, is what makes the gene stable. To carry information, these atoms cannot repeat a unit as a crystal does; they must form a sequence without periodicity, an *aperiodic crystal*, like the letters of a text. The double helix and the genetic code, a decade later, were this idea made concrete.

The second conclusion concerns order in general: an organism keeps itself far from equilibrium by "feeding on negative entropy". In modern terms it consumes free energy and exports entropy; this is the subject of [7.6.2](/7.6.2#sec-2.5).

![Three estimates behind the physicists' picture of the gene. A: target theory: with one hit sufficient, the mutated fraction is 1 − e^(−σD), linear at low dose with slope σ and without threshold (solid); a two-hit target responds quadratically (dashed). B: thermal stability after Eq. (1.2), with τ₀ = 10⁻¹⁴ s: barriers of 30, 50 and 60 kBT give mean lifetimes of 0.1 s, 16 months and 30 000 years. C: the √N rule: the relative fluctuation of a system of N independent particles is 1/√N; for about 1000 atoms it is 3 %, many orders of magnitude above observed mutation rates per gene (shaded), so the order of the gene cannot be statistical](./plots/gene-stability.py)

The book drew physicists into biology after the war: Francis Crick, Maurice Wilkins and others named it as an influence. Delbrück himself, with Salvador Luria and Alfred Hershey, built the "phage group" around bacteriophages, the simplest self-replicating systems available, and with Luria designed the **fluctuation test** (1943), which showed by the statistics of resistant colonies that mutations arise before selection rather than in response to it ([7.4.12](/7.4.12)); the analysis of its **Luria–Delbrück distribution** is an early example of a stochastic model deciding a biological question (7.6.32).

### 1.2.4. The Structural Era

From 1950 to 1970 biophysics grew faster than in the previous century, and its center became the structure of molecules. Diffraction had been understood since Max von Laue (1912) and the Braggs (1913). Dorothy Hodgkin solved the structures of penicillin and vitamin B₁₂ (Nobel Prize 1964); Rosalind Franklin's diffraction photograph of hydrated DNA fibers led to the **double helix** of James Watson and Francis Crick (1953); Max Perutz and John Kendrew solved the first protein structures, myoglobin and hemoglobin (1958–1962). At the same time, Alan Hodgkin and Andrew Huxley (1952) reconstructed the nerve impulse from voltage-clamp measurements of ionic currents with a set of differential equations, the first quantitative model of a cellular process that predicted, rather than described, the behavior of the system (7.6.30).

China contributed early to this era: bovine **insulin** was synthesized chemically in Shanghai and Beijing and crystallized in 1965, the first total synthesis of a protein, and the Beijing insulin structure group determined the crystal structure of porcine insulin at $2.5\,\text{Å}$ and later $1.8\,\text{Å}$ in the early 1970s.

The methods multiplied: NMR structures of proteins in solution from 1985, cryo-electron microscopy of vitrified samples from the 1980s and, with direct electron detectors, near-atomic resolution from 2013 (the "resolution revolution"). The **Protein Data Bank**, founded in 1971 with a handful of entries, held about $2.3\times10^5$ experimentally determined structures in 2025.

### 1.2.5. Single Molecules, Numbers and Prediction

From the 1970s three further developments changed the field.

- *Single molecules.* The patch clamp recorded the current through one ion channel (Erwin Neher and Bert Sakmann, 1976); optical traps, invented by Arthur Ashkin (1986), measured the $8\,\mathrm{nm}$ steps of a single kinesin (1993); single-molecule fluorescence followed the turnovers of one enzyme molecule and showed that its rate fluctuates in time (Sunney Xie and colleagues, 1998). A molecule observed one at a time is a stochastic object, and the theory of its fluctuations became part of biophysics.
- *Numbers and theory.* Fluorescent reporters and single-cell measurement made it possible to count molecules in individual cells, and to test quantitative theories of gene regulation, noise, sensing and growth. Physicists brought the habits of their field: simplified models, dimensionless parameters, phase diagrams and the search for regularities across systems. Examples in this course include the robustness of bacterial adaptation (7.6.35), the attractor of the yeast cell-cycle network (7.6.34), and the designability of protein folds in lattice models, which explains why a few folds are used by very many sequences (7.6.16).
- *Prediction.* In 2020 the neural network AlphaFold2 predicted protein structures from sequence with an accuracy comparable to experiment, and soon after, predicted structures for essentially all known protein sequences, more than $2\times10^8$, were made available; the 2024 Nobel Prize in Chemistry recognized structure prediction and protein design (Demis Hassabis, John Jumper, David Baker). The consequence for research is a reversal of order. Structural biology used to explain functions discovered by genetics and cell biology; now one can start from structures, search the predicted structures of a proteome for folds similar to one of known function, and proceed from structure to biochemistry, to cell biology and to genetics (7.6.15).

A report of the US National Academies, *Physics of Life* (2022), summarized the questions of the modern field in four parts: what physics problems organisms must solve (sensing, moving, keeping time), how living systems represent and process information, how macroscopic functions emerge from the interactions of many microscopic constituents, and how living systems navigate the enormous space of their parameters (through evolution, learning and regulation). This course returns to each of them.

## 1.3. Scales of Life

### 1.3.1. Lengths

Biological objects span twelve orders of magnitude in length, from the $0.1\,\mathrm{nm}$ of a chemical bond to the $100\,\mathrm{m}$ of a tree. The physics that matters changes with scale: quantum mechanics below a nanometer, where it fixes bond lengths and energies; statistical mechanics and low-Reynolds-number hydrodynamics from nanometers to micrometers, where thermal motion and viscosity dominate inertia; classical mechanics, gravity and turbulence above a millimeter.

![Lengths of life on a logarithmic scale from 0.1 nm to 100 m, each object at its characteristic size: an atom (0.15 nm), a protein (5 nm), a ribosome (25 nm), an HIV virion (120 nm), *E. coli* (2 µm), a red blood cell (8 µm), an animal cell (10–30 µm), a fruit fly (3 mm), a mouse (9 cm), a human (1.7 m) and a blue whale (25–30 m). Below the axis, the ranges covered by electron microscopy, light microscopy (resolution limited by diffraction to about 200 nm) and the naked eye (above about 0.1 mm)](./plots/length-scales.py)

Three numbers are worth memorizing: a protein is a few nanometers across, a bacterium a few micrometers long, a eukaryotic cell ten to a hundred micrometers across. The ratios are about $10^3$ and $10$, so a bacterium holds millions of proteins and a eukaryotic cell a thousand times more (1.5).

### 1.3.2. Times

Time scales span even more: from $10^{-14}\,\mathrm{s}$ for a bond vibration to $10^{17}\,\mathrm{s}$ for the history of life. As a rule small things are fast, but the correlation is loose: a protein of a few nanometers may fold in microseconds or in minutes, depending on the height of the barriers in its free-energy landscape (7.6.16), and the times of cells (the cell cycle, the circadian day) are set by networks of reactions rather than by size.

![Time scales of life on a logarithmic axis from 1 fs to 4 Gyr (typical orders of magnitude). Below the axis, molecular events: bond vibration (10 fs), rearrangement of hydrogen bonds in water (1 ps), the primary charge separation in a photosynthetic reaction centre (3 ps), side-chain rotation (ns), the fastest protein folding (µs), enzyme turnover and the action potential (ms), a kinesin step (10 ms), a protein diffusing across a eukaryotic cell (s). Above it: transcription of a 2 kb gene (1 min), division of *E. coli* (20 min), the human cell cycle and the circadian day (1 d), the lifetime of a red blood cell (4 months), a human lifetime, the oldest trees (5000 yr), the origin of a species (about 1 Myr) and the history of life on Earth (3.8 Gyr)](./plots/time-scales.py)

### 1.3.3. Energies

The natural unit of energy for molecules in a cell is the **thermal energy** $k_{\mathrm{B}}T$ ([7.2.1](/7.2.1#def-1.5.1)): $4.1\,\mathrm{pN\,nm}$ at $298\,\mathrm{K}$, $4.3\,\mathrm{pN\,nm}$ at $310\,\mathrm{K}$, equivalently $2.5$–$2.6\,\mathrm{kJ\,mol^{-1}}$ or $26\,\mathrm{meV}$. Its expression in piconewton nanometers is the useful one, because molecular forces are piconewtons and molecular displacements nanometers: a force of $4\,\mathrm{pN}$ acting over $1\,\mathrm{nm}$ does work comparable to the thermal energy. By the **Boltzmann distribution** ([5.2.1](/5.2.1)), a state lying $E$ above another is populated with relative probability $\mathrm{e}^{-E/k_{\mathrm{B}}T}$, so an energy compared with $k_{\mathrm{B}}T$ immediately says whether thermal motion matters.

![An energy ladder for the cell at 310 K, in units of the thermal energy (logarithmic axis, with kJ/mol on top and eV marked below): a van der Waals contact (about 1 kBT), a hydrogen bond or salt bridge in water (1–5 kBT), one elementary charge moved across a membrane at 70 mV (2.6 kBT), one proton through ATP synthase at 200 mV (7.5 kBT), the work of a kinesin step (6 pN × 8 nm ≈ 11 kBT), the stability of a folded protein (5–25 kBT), ATP hydrolysis under cellular conditions (about 20 kBT), the binding of a specific transcription factor (15–30 kBT), a visible photon (70–120 kBT) and the C–C and C=C covalent bonds (about 130 and 240 kBT)](./plots/energy-ladder.py)

**Example 1.3.1 (Why covalent bonds do not break by themselves)** Treat a C–C bond as a two-state system: bonded, or broken with energy $\Delta E \approx 140\,k_{\mathrm{B}}T$ higher. At equilibrium the fraction broken is

$$
p_{\mathrm{broken}} = \frac{\mathrm{e}^{-\Delta E/k_{\mathrm{B}}T}}{1 + \mathrm{e}^{-\Delta E/k_{\mathrm{B}}T}} \approx \mathrm{e}^{-140} \approx 10^{-61}.
$$
Even counting every bond in every organism on Earth (fewer than $10^{45}$), not one would be broken thermally at any moment. Covalent bonds are therefore made and broken in cells only by enzymes, which lower the barrier for one particular reaction, while noncovalent interactions of a few $k_{\mathrm{B}}T$ are made and broken all the time: this division of labor between permanent and reversible bonds runs through the whole course.

## 1.4. Physics in Living Systems

Every branch of elementary physics, mechanics, electricity and magnetism, optics and heat, has its counterpart in the living world, both as a subject of study and as a tool. This section surveys them briefly; each returns in a later chapter.

### 1.4.1. Gravity and Buoyancy

Gravity shapes organisms from the outside: the skeleton of a land animal, the trunk of a tree and the stiff walls of plant cells resist it, and its effects grow with size, since weight scales as the cube of a length and the strength of a supporting cross-section only as its square. For a single cell gravity is weak but not negligible. A cell without internal support would flatten under its own weight; in water, buoyancy, osmotic pressure and surface tension largely compensate, and the cytoskeleton of animal cells and the wall of plant cells hold the shape against the remainder. Some aquatic microorganisms use gravity actively: cyanobacteria and some other bacteria build gas vesicles, hollow spindle-shaped shells assembled from a small hydrophobic protein (GvpA) that let gas in and keep water out, and by adjusting their number they rise and sink in the water column toward light and nutrients. At the molecular scale gravity is irrelevant, and the centrifuge replaces it with an acceleration $10^5$ times larger (7.6.8).

### 1.4.2. Electromagnetic Forces and Their Sensing

Of the four fundamental interactions, the strong and weak ones act only inside nuclei and gravity is feeble; everything else in biology, covalent and noncovalent bonds, friction, elasticity, the pressure of one body on another, is electromagnetic. The macroscopic forces that cells and tissues exert are sums of molecular ones: myosin heads pulling on actin generate muscle force ([7.3.13](/7.3.13)), and the contact force of one object on another arises from the repulsion of electron clouds. Forces are sensed by molecules that change conformation under load, most directly by mechanosensitive ion channels, which open when the membrane is stretched and let ions flow (7.6.25); touch, hearing, balance and the gravitropism of roots all rest on such sensors.

Surface tension, another electromagnetic effect, organizes small objects at interfaces. Floating particles attract each other if they deform the liquid surface in the same way (both wetting or both non-wetting), because bringing them together reduces the total area of deformed surface; the effect, named after breakfast cereal clumping in milk (the Cheerios effect), also aggregates small organisms and particles at the surface of water.

### 1.4.3. Electricity

Living cells keep the concentrations of ions inside and outside very different, and their membranes are selectively permeable to them. An ion that can cross the membrane flows down its concentration gradient until the charge it carries builds up an opposing voltage; at balance, the Nernst potential $E = (k_{\mathrm{B}}T/ze)\ln(c_{\mathrm{out}}/c_{\mathrm{in}})$ is reached (derived in [7.6.3](/7.6.3#sec-3.1.5)). For a mammalian cell at $37\,^\circ\mathrm{C}$:

| Ion | Outside / mM | Inside / mM | Ratio out/in | Nernst potential / mV |
|---|---|---|---|---|
| $\ce{Na+}$ | $145$ | $12$ | $12$ | $+67$ |
| $\ce{K+}$ | $4.5$ | $155$ | $0.029$ | $-95$ |
| $\ce{Cl-}$ | $116$ | $4.2$ | $28$ | $-89$ |
| $\ce{Ca^2+}$ | $1.0$ | $10^{-4}$ | $10^4$ | $+123$ |

The resting membrane is most permeable to $\ce{K+}$, so the resting potential, $-70$ to $-90\,\mathrm{mV}$, lies near the potassium potential; the opening of other channels moves it toward their potentials, which is how neurons and muscle cells signal (7.6.30). Some animals add voltages in series. The electric organ of the electric eel consists of thousands of flat cells, electrocytes, stacked like the plates of a battery; when stimulated, each opens sodium channels on one face only, so that the potentials of its two faces no longer cancel and the cell develops about $150\,\mathrm{mV}$ across itself. Thousands of electrocytes in series give several hundred volts, enough to stun prey.

### 1.4.4. Light

Light carries both energy and information. Photosynthesis captures the energy of sunlight in chlorophylls and carotenoids, transfers it to reaction centers within picoseconds and converts it into charge separation and finally into ATP and NADPH ([7.1.24](/7.1.24)); it supplies almost all the free energy of the biosphere ([7.6.2](/7.6.2#sec-2.5.2)). As information, light is read by photoreceptor proteins whose chromophores change shape when they absorb a photon: rhodopsin and the cone opsins in the eye, which together with the outer segments of rods and cones detect single photons and discriminate colors (7.6.18), and in plants the phytochromes (red and far red), the cryptochromes, phototropins and ZEITLUPE (blue light) and UVR8 (ultraviolet B), which control germination, flowering, phototropism and the circadian clock.

### 1.4.5. Temperature

Temperature sets the rates of all reactions: by the Arrhenius equation a rate rises as $\mathrm{e}^{-E_{\mathrm{a}}/RT}$, typically two- to threefold for $10\,\mathrm{K}$ ([7.6.3](/7.6.3#sec-3.5.3)). Organisms respond in two ways. Ectotherms, whose body temperature follows the environment, adjust their activity and behavior; in many reptiles even the sex of the offspring is set by the incubation temperature of the egg (in painted turtles warm nests produce females, cool nests males). Endotherms keep their temperature constant by producing heat metabolically; brown adipose tissue does so deliberately, using the uncoupling protein UCP1 to let protons return across the inner mitochondrial membrane without making ATP, so that the free energy of the proton-motive force is released directly as heat ([7.1.23](/7.1.23#sec-23.5.1)). Temperature is also sensed by molecules, ion channels whose opening has a large enthalpy change (7.6.4). Physiological thermoregulation is treated in [7.14](/7.14).

### 1.4.6. Order: Transport across Scales and Periodicity

Life is ordered, and two kinds of order require physical explanation. The first is the distribution of matter. Molecules spread by diffusion, the macroscopic result of thermal motion, and a diffusing molecule covers a distance $L$ in a time of order $L^2/D$ (7.6.5). For a protein in cytoplasm ($D \approx 10\,\mu\mathrm{m^2\,s^{-1}}$) this is a fraction of a second across a bacterium and tens of seconds across a eukaryotic cell, but $10^{11}\,\mathrm{s}$, three thousand years, along a $1\,\mathrm{m}$ axon. Large cells and organisms therefore rely on directed transport driven by free energy: motors carry cargo along microtubules at about $1\,\mu\mathrm{m\,s^{-1}}$, which covers the axon in two weeks (7.6.27), and the circulation of blood moves oxygen over meters in seconds. The second kind of order is temporal and spatial periodicity: cell cycles, circadian clocks, heartbeats, the segments of an embryo, the spots of a leopard. A system at equilibrium can have spatial order (a crystal) but no sustained oscillation. Rhythms and many patterns are dissipative structures that arise spontaneously, by self-organization, in open systems through which free energy flows (7.6.33, 7.6.36). Both kinds of order rest on the free energy whose role is analyzed in [7.6.2](/7.6.2#sec-2.5).

## 1.5. The Stuff of Life and the Cell by the Numbers

### 1.5.1. Four Classes of Macromolecules

Cells are built from four great classes of macromolecules: nucleic acids, proteins, polysaccharides and lipids (the last forming assemblies rather than covalent polymers). Nucleic acids and proteins are linear polymers written in languages with different alphabets, four nucleotides and twenty amino acids. The combinatorics are enormous: there are $4^{N}$ sequences of $N$ nucleotides and $20^{N}$ of $N$ amino acids, so a protein of 300 residues is one of $20^{300} \approx 10^{390}$ possibilities. A sequence carries information (at most 2 bits per nucleotide and $\log_2 20 = 4.3$ bits per residue), and the physics of the course explains how this one-dimensional information becomes three-dimensional structure (7.6.7, 7.6.16), how it is read with specificity (7.6.17) and how evolution searches the space of sequences (7.6.41).

### 1.5.2. *Escherichia coli* as a Ruler

The bacterium *E. coli*, grown in a defined minimal medium, is the best-measured cell: a rod about $2\,\mu\mathrm{m}$ long and $1\,\mu\mathrm{m}$ wide, with a volume of about $1\,\mu\mathrm{m}^3 = 1\,\mathrm{fL}$ and a mass of about $1\,\mathrm{pg}$, of which about 70 % is water. With a few such numbers, many others can be estimated in a line. An estimate of this kind, built from rounded inputs and simple reasoning to get the right power of ten, is called a *Fermi estimate*; its value lies less in the answer than in the reasoning it forces, which exposes what controls the quantity and whether a proposed mechanism is possible at all.

**Example 1.5.1 (How many proteins in *E. coli*?)** The dry mass is about 30 % of $1\,\mathrm{pg}$, $0.3\,\mathrm{pg}$, and about half of it is protein, $0.15\,\mathrm{pg}$. A typical protein has about 300 residues of $110\,\mathrm{Da}$, a mass of $3.3\times10^4\,\mathrm{Da}$, and $1\,\mathrm{Da} = (1\,\mathrm{g\,mol^{-1}})/N_{\mathrm{A}} = 1.66\times10^{-24}\,\mathrm{g}$, so one protein weighs $5.5\times10^{-20}\,\mathrm{g}$. The number of proteins is

$$
N_{\mathrm{prot}} \approx \frac{1.5\times10^{-13}\,\mathrm{g}}{5.5\times10^{-20}\,\mathrm{g}} \approx 3\times10^6 .
$$
The measured value for a cell doubling every 40 minutes is $2.4\times10^6$.

Two further conversions are used constantly. In a volume of $1\,\mathrm{fL}$, one molecule corresponds to a concentration of

$$
c_1 = \frac{1}{N_{\mathrm{A}}V} = \frac{1}{6.0\times10^{23}\,\mathrm{mol^{-1}}\times10^{-15}\,\mathrm{L}} \approx 1.7\,\mathrm{nM} \tag{1.3}
$$
([7.2.1](/7.2.1#sec-1.5.3)), so a transcription factor present at 10 copies is at about $20\,\mathrm{nM}$; in a human cell of $3000\,\mu\mathrm{m}^3$ one molecule is $0.6\,\mathrm{pM}$. And small numbers fluctuate: at division each of $N$ molecules goes to one daughter or the other with probability $1/2$, the number in a daughter follows a **binomial distribution** with mean $N/2$ and variance $N/4$, and the relative spread is

$$
\frac{\sqrt{N/4}}{N/2} = \frac{1}{\sqrt{N}}, \tag{1.4}
$$
10 % for a protein present at 100 copies. The full census of the cell (its macromolecules, its sizes and its time scales, from the number of ribosomes and the area of its membranes to the time to replicate its genome) is the subject of [7.6.20](/7.6.20); it is used throughout the course.

### 1.5.3. Rules of Thumb

A small set of numbers suffices for most estimates in this course; each is the result of many measurements, and the rest can be derived from them.

| Quantity | Rule of thumb |
|---|---|
| Thermal energy | $k_{\mathrm{B}}T \approx 4\,\mathrm{pN\,nm} \approx 25\,\mathrm{meV} \approx 0.6\,\mathrm{kcal\,mol^{-1}} \approx 2.5\,\mathrm{kJ\,mol^{-1}}$ |
| ATP hydrolysis in the cell | $\approx 20\,k_{\mathrm{B}}T$ |
| Hydrogen bond, van der Waals contact | a few $k_{\mathrm{B}}T$, about $1\,k_{\mathrm{B}}T$ |
| *E. coli* | volume $1\,\mu\mathrm{m}^3$, mass $1\,\mathrm{pg}$, $3\times10^6$ proteins, doubling time $20$–$60\,\mathrm{min}$ |
| One molecule per *E. coli* | $\approx 2\,\mathrm{nM}$ |
| Eukaryotic cell | diameter $10$–$100\,\mu\mathrm{m}$, volume $10^3$–$10^4\,\mu\mathrm{m}^3$ |
| Protein | diameter $\approx 5\,\mathrm{nm}$, mass $\approx 30\,\mathrm{kDa}$ |
| Diffusion coefficient of a protein in cytoplasm | $\approx 10\,\mu\mathrm{m^2\,s^{-1}}$ |
| DNA | $0.34\,\mathrm{nm}$ per base pair, persistence length $50\,\mathrm{nm}$ |
| Membrane | thickness $\approx 4$–$5\,\mathrm{nm}$ |
| Viscosity of water | $10^{-3}\,\mathrm{Pa\,s}$ |
| Motor protein | step $\approx 10\,\mathrm{nm}$, force $\approx 5\,\mathrm{pN}$ |

## 1.6. Models

### 1.6.1. Models as Idealizations

"All models are wrong, but some are useful" (George Box). A physical model of a biological object keeps what matters for a particular question and discards the rest, and the same object is idealized differently for different questions. DNA is a sequence of letters when the question is coding, an elastic rod when it is bent around a nucleosome or looped by a repressor, a random walk when it fills a nucleus, a charged cylinder when it attracts counterions, and a chain of base pairs that can be unzipped when it is replicated (7.6.21, 7.6.6, 7.6.17). None of these is the "true" DNA; each is appropriate to a range of scales and forces.

Biologists already idealize, in cartoons: a diagram of an ion channel as a pore with a gate, of a gene as a box with a promoter and a repressor, of a signaling pathway as arrows. A cartoon selects the features thought essential. Physical modeling begins by turning the cartoon into mathematics: the channel's gate becomes two states with an energy difference and the probability of being open follows from the Boltzmann distribution (7.6.4); the promoter becomes a set of states with binding energies and the expression level follows from their weights (7.2.11); the arrows become rate equations (7.6.33). The mathematics then predicts how the system responds to changes (of voltage, concentration or force) that the cartoon alone cannot quantify.

**Definition 1.6.1 (Coarse-Graining)** **Coarse-graining** is the replacement of a detailed description of a system by a simpler one with fewer degrees of freedom, obtained by grouping or averaging over the variables that are irrelevant on the scale of interest; the effect of the eliminated variables appears only through a few effective parameters of the simpler description.

The idea that each level of description has its own laws, consistent with those of the level below but not derivable from them in practice, was stated by Philip Anderson in "More Is Different" (1972): new properties arise at each level of organization. Such properties, which belong to a collection and not to any of its parts, are called *emergence*. The two attitudes, analyzing a system into its parts (reductionism) and explaining collective behavior from interactions (emergence), correspond to the two halves of physics and to the two halves of biophysics.

| Philosophy | Physics | Biophysics |
|---|---|---|
| Reductionism: understand the whole from its parts | Elementary particle physics | Structural biology, molecular biophysics |
| Emergence: new laws at each level | Condensed-matter physics | Active matter, collective behavior, quantitative and systems biology |

### 1.6.2. The Toolbox of Fundamental Physical Models

Many biological systems near a stable state respond linearly to small perturbations: expand the energy about its minimum and the leading term is quadratic, $E(x) \approx E_0 + \frac{1}{2}kx^2$. This "springiness" of matter is why Hooke's law describes a stretched protein, a bent filament and a deformed membrane alike, and why a few models recur throughout physics and this course.

| Model | Describes | Chapters |
|---|---|---|
| Harmonic spring | Small deformations, thermal fluctuations, optical traps | 7.6.2, 7.6.17 |
| Two-state system | Channels, receptors, folding, binding | 7.6.3, 7.6.4, 7.6.16 |
| Ideal gas and ideal solution | Osmotic pressure, chemical potential, mass action | 7.6.2, 7.6.3 |
| Random walk | Diffusion, polymer conformations | 7.6.5, 7.6.21 |
| Elastic rod and sheet | DNA, cytoskeletal filaments, membranes | 7.6.21, 7.6.24, 7.6.26 |
| Electrostatics in salt water | Screening, counterions, membrane potentials | 7.6.6, 7.6.30 |
| Viscous (low Reynolds number) flow | Swimming, sedimentation, friction | 7.6.8, 7.6.22 |
| Rate equations and master equations | Kinetics, gene expression, noise | 7.6.3, 7.6.32, 7.6.33 |

### 1.6.3. Unifying Ideas and Mathematical Tools

Biology has unifying ideas of its own, and they constrain models as firmly as conservation laws: all organisms are made of cells, which arise only from cells; heredity is carried by sequences of nucleic acids, read through the genetic code by the machinery of the **central dogma**; the forms and functions of organisms are the product of evolution by natural selection acting on variation; and living systems are open systems that transform free energy. A model that violates one of these is wrong whatever its fit to data.

The mathematics needed is modest and recurs: probability theory, especially four distributions, the binomial, Gaussian, Poisson and exponential ([3.1.4](/3.1.4)); ordinary and partial differential equations for how quantities change in time and space ([2.4](/2.4), [2.5](/2.5)); the calculus of extremes, which finds equilibrium states by minimizing an energy or free energy, including the calculus of variations when the unknown is a function such as the shape of a membrane (7.6.24); Fourier analysis for diffraction and imaging (7.6.10, 7.6.14); and numerical computation and simulation in Python ([4.4](/4.4)) when the equations cannot be solved in closed form.

### 1.6.4. Estimates and Being Wrong

A model is built in steps, each of which can be checked against data.

1. State the phenomenon and the quantity to be explained, with its measured value and units.
2. Estimate: list the relevant parameters and their magnitudes, and check by dimensional analysis and Fermi estimates which effects can possibly matter. A good estimate brackets the answer between a lower and an upper bound.
3. Write the simplest model that contains those effects, usually a few states with energies, or a few variables with rate equations, simple enough to be solved with pencil and paper.
4. Solve it (analytically if possible, numerically otherwise) and derive predictions, preferably of a functional form rather than a single number: a dependence on dose, concentration, force or time.
5. Confront the predictions with data, and add only the detail that a failure demands.

Models can be wrong in instructive ways: by using the wrong kind of physics for the problem; by leaving out detail that matters (a model of the mean speed of a swimming bacterium says nothing about how its speed fluctuates); by misjudging which effects dominate; or by giving correct numbers for the wrong reason. The first kind teaches what physics applies, the second is incompleteness, often deliberate, and the last two are the most valuable, because their failure points to a mechanism. The simplest model of all, a spring, illustrates the steps: a bead held by an optical trap has energy $\frac{1}{2}kx^2$; its thermal fluctuations, computed in [7.6.2](/7.6.2#sec-2.3.2), give the stiffness $k$ from the measured variance of $x$ alone, which is how optical traps are calibrated.

### 1.6.5. A Worked Case: HIV Dynamics under Therapy

Before 1995, infection with HIV-1 was thought to be slow: years pass between infection and AIDS, and the amount of virus in the blood stays roughly constant for most of that time. A simple model, combined with an experiment that perturbed the steady state, showed that the constancy hides a very fast turnover, and this changed how the disease is treated.

**Formula 1.6.1 (Basic Model of Viral Dynamics)** Let $T$ be the concentration of uninfected target cells (CD4⁺ T cells), $T^*$ that of productively infected cells and $V$ that of free **virions**. Then

$$
\frac{\mathrm{d}T}{\mathrm{d}t} = \lambda - d_T T - kVT, \qquad
\frac{\mathrm{d}T^*}{\mathrm{d}t} = kVT - \delta T^*, \qquad
\frac{\mathrm{d}V}{\mathrm{d}t} = N\delta T^* - cV, \tag{1.5}
$$
where $\lambda$ is the production rate of target cells, $d_T$ their death rate, $k$ the infection rate constant, $\delta$ the death rate of infected cells, $N$ the number of virions released by an infected cell over its life (its burst size) and $c$ the clearance rate of free virions. The infection persists if one infected cell gives rise to more than one infected cell, $R_0 = Nk\lambda/(d_T c) > 1$, and then the system has a steady state with constant $V$ (stable for the parameter values of HIV infection; stability analysis as in [2.4](/2.4)).

At steady state the production of virions balances their clearance, $N\delta T^* = cV$, and the death of infected cells balances new infections: the plasma level $V$ is constant whatever the speed of the underlying turnover. To measure that speed one must perturb the steady state. In 1995 David Ho, Alan Perelson and colleagues, and independently George Shaw's group, gave patients potent antiretroviral drugs (inhibitors of the viral protease or of **reverse transcriptase**) and measured the decline of plasma virus every few hours.

**Theorem 1.6.1 (Decay of Virus under Complete Inhibition of Infection)** Suppose that at $t = 0$ a drug blocks all new infections ($k = 0$), starting from the steady state $T^*(0) = T^*_0$, $V(0) = V_0$ with $N\delta T^*_0 = cV_0$. Then for $c \ne \delta$

$$
V(t) = V_0\,\frac{c\,\mathrm{e}^{-\delta t} - \delta\,\mathrm{e}^{-ct}}{c - \delta}. \tag{1.6}
$$

**Proof** With $k = 0$ the second equation of (1.5) gives $T^*(t) = T^*_0\mathrm{e}^{-\delta t}$, and the third becomes $\dot V + cV = N\delta T^*_0\mathrm{e}^{-\delta t} = cV_0\mathrm{e}^{-\delta t}$. A particular solution is $V_p = cV_0\mathrm{e}^{-\delta t}/(c - \delta)$; adding the homogeneous solution $A\mathrm{e}^{-ct}$ and imposing $V(0) = V_0$ gives $A = -\delta V_0/(c - \delta)$, which is Eq. (1.6). $\square$

Because $c \gg \delta$ for HIV, Eq. (1.6) has a shoulder of duration about $1/c$ (the virions already present are still being made by infected cells that are not yet affected), after which $V(t) \approx V_0\,\mathrm{e}^{-\delta t}\,c/(c - \delta)$: the slope of $\ln V$ measures the death rate of infected cells, and the curvature at early times measures the clearance of virions. Fitting the data gave a half-life of productively infected cells of about $1.6\,\mathrm{d}$ ($\delta \approx 0.5\,\mathrm{d^{-1}}$) and a half-life of free virions of at most about 6 hours ($c \gtrsim 3\,\mathrm{d^{-1}}$; direct measurements later found 30 to 100 minutes).

![Decay of HIV-1 under potent therapy in a model with three populations of virus-producing cells: cells in the eclipse phase (becoming productive at rate 1 per day), short-lived productive cells (death rate δ₁ = 0.5 per day, 99 % of production) and long-lived infected cells (δ₂ = 0.04 per day, 1 %), with virion clearance c = 3 per day; therapy blocks all new infections at t = 0 and the plasma virus starts at 10⁵ copies/mL. A: the plasma virus shows a shoulder of about a day, a first phase whose slope gives δ₁ (half-life 1.4 d) and a second phase whose slope gives δ₂ (half-life 17 d); dashed, the much faster decay at rate c that would follow if virion production stopped at once. B: the expected number of new virions per day carrying a particular single, double or triple point mutation, Nμ^k with N = 10¹⁰ virions per day and μ = 3 × 10⁻⁵ per base per replication cycle](./plots/hiv-dynamics.py)

**Example 1.6.1 (Turnover and the case for combination therapy)** At steady state the number of virions made per day equals the number cleared, $cV$ times the volume of fluid that contains them. With $V = 10^5\,\mathrm{mL^{-1}}$ and $c = 3\,\mathrm{d^{-1}}$ in about $15\,\mathrm{L}$ of extracellular fluid, production is $3\times10^5\,\mathrm{mL^{-1}\,d^{-1}}\times1.5\times10^4\,\mathrm{mL} \approx 5\times10^9$ virions per day; the estimate from the patients' data was about $10^{10}$ per day, and with the faster clearance measured later the true value is larger still. Reverse transcriptase makes about $3\times10^{-5}$ errors per base per replication cycle, and the genome has about $10^4$ bases, so every possible single point mutation arises some $10^{10}\times3\times10^{-5} = 3\times10^5$ times a day, and any one double mutant about $10^{10}\times(3\times10^{-5})^2 \approx 10$ times a day, before any selection. A single drug, to which one mutation confers resistance, must fail; three drugs, requiring three simultaneous specific mutations ($3\times10^{-4}$ per day), can hold the virus down for years. Combination antiretroviral therapy, introduced in 1996, turned HIV infection from a fatal disease into a chronic one.

The model also showed what it leaves out. After the first phase the decay slows (the second phase in the figure), revealing a small population of longer-lived infected cells, and below the detection limit a reservoir of latently infected resting memory T cells with a half-life of years persists, which is why therapy cannot be stopped. Each departure from the simplest model identified a new biological compartment. The case shows all five steps of 1.6.4: a quantitative phenomenon, estimates, a minimal model, a functional prediction (a two-exponential decay) and a confrontation with data that both measured the parameters and revealed what the model lacked.

## Summary

- Biophysics is both the application of physical methods to biological questions and the search for physical principles of living matter (1.1.1). This course divides it into molecular biophysics (structural biology and the physics of its methods), cell biophysics (dimensional physical behavior at cellular scale) and quantitative biology (abstract quantitative regularities), preceded by statistical-physics foundations (1.1.2–1.1.3).
- History (1.2): the Berlin school (1840s) made physiology physical; target theory (Definition 1.2.1, Eq. (1.1)) and the three-man paper (1935) argued that a gene is a molecule; Schrödinger (1944) explained its stability by the Boltzmann factor of a barrier, Eq. (1.2), and called it an aperiodic crystal; the structural era produced the double helix and the first protein structures; single-molecule methods, quantitative single-cell biology and structure prediction define the present.
- Scales (1.3): lengths from $0.1\,\mathrm{nm}$ to $100\,\mathrm{m}$, times from $10^{-14}$ to $10^{17}\,\mathrm{s}$, and energies measured in $k_{\mathrm{B}}T = 4.1$–$4.3\,\mathrm{pN\,nm}$: noncovalent interactions are a few $k_{\mathrm{B}}T$, ATP hydrolysis about $20\,k_{\mathrm{B}}T$, covalent bonds above $100\,k_{\mathrm{B}}T$ (Example 1.3.1).
- Physics in living systems (1.4): gravity matters for large organisms and for buoyant microorganisms with gas vesicles; all other forces are electromagnetic and are sensed by mechanosensitive molecules; ion gradients set Nernst potentials from $-95\,\mathrm{mV}$ ($\ce{K+}$) to $+123\,\mathrm{mV}$ ($\ce{Ca^2+}$), and electrocytes in series give the electric eel's discharge; light is both energy (photosynthesis) and information (photoreceptors); temperature sets rates and is regulated or exploited (sex determination, brown fat); diffusion times grow as $L^2/D$, so large cells need directed transport, and rhythms require open systems far from equilibrium.
- Stuff and numbers (1.5): four classes of macromolecules, two of them polymer languages with 4 and 20 letters; an *E. coli* cell of $1\,\mathrm{fL}$ holds about $3\times10^6$ proteins (Example 1.5.1); one molecule per cell is about $2\,\mathrm{nM}$, Eq. (1.3); partitioning gives a spread $1/\sqrt{N}$, Eq. (1.4); a dozen rules of thumb support most estimates; the full census is in 7.6.20.
- Models (1.6): the same object is idealized differently for different questions, and cartoons become models when they are made mathematical; coarse-graining (Definition 1.6.1) keeps the variables that control a phenomenon; a handful of physical models (springs, two-state systems, ideal solutions, random walks, elastic rods and sheets, electrostatics, viscous flow, rate equations) and a few mathematical tools recur; a model is built by estimating, writing the simplest version, deriving functional predictions and confronting them with data. The viral dynamics of HIV (Formula 1.6.1, Theorem 1.6.1) measured a virion half-life of hours and an infected-cell half-life of a day and a half, implying about $10^{10}$ virions and every single mutant many times a day, the quantitative case for combination therapy (Example 1.6.1).

## Questions

1. An *E. coli* cell doubling every 40 minutes must make about $3\times10^6$ proteins of 300 residues. Each peptide bond costs about four high-energy phosphate bonds (ATP and GTP). How many such bonds are hydrolyzed per second for protein synthesis, and how does this compare with the number of ATP molecules in the cell (about 3 mM)?

   **Answer** Peptide bonds per cell cycle: $3\times10^6\times300 = 9\times10^8$; phosphate bonds: $4\times9\times10^8 = 3.6\times10^9$ per $2400\,\mathrm{s}$, about $1.5\times10^6\,\mathrm{s^{-1}}$. The ATP pool is $3\times10^{-3}\,\mathrm{M}\times6\times10^{23}\,\mathrm{mol^{-1}}\times10^{-15}\,\mathrm{L} \approx 1.8\times10^6$ molecules: protein synthesis alone would exhaust it in about a second, so ATP must be regenerated continuously, and protein synthesis is the largest single item of the bacterial energy budget.

2. Why does a mutation frequency proportional to dose, independent of the dose rate and of the type of radiation at equal ionization, support the hypothesis that a single ionization within a small volume causes a mutation? What would a two-hit mechanism predict at low dose?

   **Answer** If ionizations are scattered independently and at random, the number in a fixed volume is Poisson distributed with mean proportional to the dose; the probability of at least one is $1 - \mathrm{e}^{-\sigma D} \approx \sigma D$, linear, and depends only on the total number of ionizations, not on when or by what radiation they were produced. If two hits were needed, the low-dose response would be $(\sigma D)^2/2$, quadratic, and spreading the dose over time would reduce it if the first hit could be repaired before the second arrived.

3. Using Eq. (1.2), compute the ratio of the spontaneous mutation rates at $310\,\mathrm{K}$ and $300\,\mathrm{K}$ (the $Q_{10}$) for barriers of $1.0$ and $1.5\,\mathrm{eV}$. Timoféeff-Ressovsky found that spontaneous mutation rates in *Drosophila* rise about fivefold for a $10\,\mathrm{K}$ increase in temperature. What barrier does this imply?

   **Answer** The rate is $1/\tau \propto \mathrm{e}^{-W/k_{\mathrm{B}}T}$, so $Q_{10} = \exp\!\left[\frac{W}{k_{\mathrm{B}}}\left(\frac{1}{300\,\mathrm{K}} - \frac{1}{310\,\mathrm{K}}\right)\right]$. With $k_{\mathrm{B}} = 8.62\times10^{-5}\,\mathrm{eV\,K^{-1}}$ the bracket is $1.075\times10^{-4}\,\mathrm{K^{-1}}$: $W = 1.0\,\mathrm{eV}$ gives $Q_{10} = \mathrm{e}^{1.25} = 3.5$, $W = 1.5\,\mathrm{eV}$ gives $\mathrm{e}^{1.87} = 6.5$. A factor of 5 corresponds to $W = \ln 5/(1.25\,\mathrm{eV^{-1}}) \approx 1.3\,\mathrm{eV}$, about $50\,k_{\mathrm{B}}T$: an energy of chemical rearrangement, and a barrier that by Eq. (1.2) gives lifetimes of years, consistent with a molecular gene.

4. What concentration does one molecule correspond to in a yeast cell (volume about $40\,\mu\mathrm{m}^3$) and in a human cell ($3000\,\mu\mathrm{m}^3$)? A transcription factor binds its site with $K_{\mathrm{d}} = 1\,\mathrm{nM}$. How many copies must a human cell contain for the site to be half occupied, ignoring nonspecific binding?

   **Answer** $c_1 = 1/(N_{\mathrm{A}}V)$: yeast $1/(6.0\times10^{23}\times4\times10^{-14}\,\mathrm{L}) \approx 42\,\mathrm{pM}$; human cell $0.55\,\mathrm{pM}$. Half occupancy needs a free concentration equal to $K_{\mathrm{d}}$, $1\,\mathrm{nM}$, that is $10^{-9}/5.5\times10^{-13} \approx 1800$ copies (in the nucleus, a smaller volume, somewhat fewer). In reality most copies are bound nonspecifically to DNA, and cells contain $10^4$–$10^5$ copies of typical factors.

5. Sister cells receive a protein present at $N$ copies in the mother by independent random partitioning. How large must $N$ be for the coefficient of variation of the daughters' copy numbers to be below 5 %? If, instead, the coefficient of variation measured between sisters is 20 % for a protein present at 1000 copies, what can be concluded?

   **Answer** By Eq. (1.4) the coefficient of variation is $1/\sqrt{N}$; below 5 % requires $N > 400$. For $N = 1000$, partitioning gives $3.2\,\%$; a measured 20 % must come from other sources, such as bursty synthesis after division, unequal division volumes or deterministic asymmetric partitioning, and these can be separated by measuring cells at different times after division (7.6.32).

6. Using $t \sim L^2/D$ with $D = 10\,\mu\mathrm{m^2\,s^{-1}}$, compare the time for a protein made in the cell body of a motor neuron to reach the end of its $1\,\mathrm{m}$ axon by diffusion and by kinesin-driven transport at $1\,\mu\mathrm{m\,s^{-1}}$. At what length do the two take equal time?

   **Answer** Diffusion: $10^{12}/10 = 10^{11}\,\mathrm{s} \approx 3000$ years; transport: $10^6\,\mathrm{s} \approx 12$ days. They are equal when $L^2/D = L/v$, that is $L = D/v = 10\,\mu\mathrm{m}$: below about ten micrometers diffusion is faster, above it directed transport wins, which is why bacteria and small cells rely on diffusion and large eukaryotic cells on motors (the Péclet number of 7.6.5).

7. Estimate the number of ribosomes a bacterium needs to double its protein content in 20 minutes, if each ribosome adds about 20 amino acids per second. Compare with the measured $7\times10^4$ ribosomes of a cell growing that fast, and explain why the fraction of protein in ribosomes must rise with growth rate.

   **Answer** Amino acids to be polymerized: $3\times10^6\times300 = 9\times10^8$ in $1200\,\mathrm{s}$, that is $7.5\times10^5\,\mathrm{s^{-1}}$; at $20\,\mathrm{s^{-1}}$ per ribosome, $3.75\times10^4$ ribosomes. The measured number is about twice as large because ribosomes also make ribosomal proteins, not all are active at any time, and cells growing fast are larger. Since the time to double the proteome is the ratio of the proteome to the synthesis rate, which is proportional to the number of ribosomes, a faster growth rate requires a larger ribosomal fraction: the growth law $\lambda \propto \phi_{\mathrm{R}} - \phi_0$ of 7.6.39.

8. In Eq. (1.6), show that the time at which $V(t)$ has fallen to half its initial value is approximately $t_{1/2} \approx \frac{\ln 2}{\delta} + \frac{1}{c}$ when $c \gg \delta$, and interpret the two terms. Compute it for $\delta = 0.5\,\mathrm{d^{-1}}$, $c = 3\,\mathrm{d^{-1}}$.

   **Answer** For $c \gg \delta$ and $t \gtrsim 1/c$, $V(t) \approx V_0\frac{c}{c - \delta}\mathrm{e}^{-\delta t} \approx V_0(1 + \delta/c)\mathrm{e}^{-\delta t}$; setting this to $V_0/2$ gives $t_{1/2} = [\ln 2 + \ln(1 + \delta/c)]/\delta \approx \ln 2/\delta + 1/c$. The first term is the half-life of infected cells, the second a delay equal to the lifetime of a virion: after the drug acts, virions already in the pipeline are still made and cleared. Numerically $1.39 + 0.33 = 1.72\,\mathrm{d}$; the exact solution of Eq. (1.6) gives $1.75\,\mathrm{d}$.

9. (Open) Classify each of the following as primarily "physics applied to biology" or "physics of living matter", and explain your choice: determining the structure of a membrane transporter by cryo-electron microscopy; deriving a bound on the precision with which a bacterium can measure a concentration; measuring the stall force of a motor protein with an optical trap; explaining why flocks of birds move coherently.

   **Answer** The structure determination applies known physics (electron optics, image formation) to a specific molecule: physics applied to biology. The precision bound is a general physical limit valid for any sensor that counts diffusing molecules, independent of molecular details: physics of living matter (7.6.35). The stall-force measurement uses a physical instrument on one molecule, but its value tests general theories of how motors convert free energy into work, so it belongs to both (7.6.27). Collective motion is emergent behavior of self-propelled agents, whose theory (Vicsek, Toner and Tu) is new statistical physics: physics of living matter (7.6.37).
