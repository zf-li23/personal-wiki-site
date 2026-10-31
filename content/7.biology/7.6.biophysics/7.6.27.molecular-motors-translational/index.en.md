---
title: "Molecular Motors I: Translational Motors"
description: "The physics of motors that walk along filaments. Beating diffusion; four classes of motors; the energy scale (force times step against one ATP) and in vitro assays. Rectified Brownian motion: Feynman's ratchet, the absence of current at equilibrium, flashing ratchets, power strokes. Master-equation models: position–state description, the one-state model and its drift and diffusion, generalized detailed balance and the stall force, where the load acts, the two-state model, a kinetic model of kinesin. Dwell-time distributions, the randomness parameter and counting hidden steps. Tight and loose coupling, efficiency and the thermodynamic cost of precision. Teams of motors: load sharing and the tug-of-war model. Muscle: Hill's force–velocity relation and Huxley's cross-bridge model."
---

Diffusion is fast over a micrometer and hopeless over a millimeter. To move cargo along an axon, to separate chromosomes, to contract a muscle or to beat a cilium, cells use **motor proteins**: enzymes that convert the free energy of a chemical reaction, usually ATP hydrolysis, into directed mechanical work. A motor is a machine of a few nanometers that works in a bath where thermal energy is comparable to the energy it spends per step, so its motion is stochastic: it pauses, occasionally steps backward, and moves forward only on average. This chapter develops the physics of the translational motors, those that walk along linear tracks: what limits the force they can exert, why thermal noise cannot be rectified at equilibrium, how kinetic models built from master equations predict force–velocity curves and their dependence on ATP, what the fluctuations of a single motor reveal about its hidden internal steps, how efficient motors are, how teams of motors share loads or fight a tug of war, and how the cross-bridge model of muscle turns molecular kinetics into the force–velocity relation of a whole muscle.

The cell biology of the cytoskeletal motors is in [7.3.13](/7.3.13) (myosin, the **cross-bridge cycle**, duty ratio) and [7.3.14](/7.3.14) (kinesin, dynein, axonal transport, cilia); their mechanochemistry is analysed physically here. The mathematical tools are the **master equation**, the **Fokker–Planck equation** and the **first-passage time** of [7.6.5](/7.6.5), detailed balance and the free energy of ATP hydrolysis from [7.6.3](/7.6.3), and the overdamped mechanics of [7.6.22](/7.6.22). The instruments, optical and magnetic tweezers, are treated in [7.6.17](/7.6.17). Rotary motors, translocation and polymerization motors use the same theory and are the subject of [7.6.28](/7.6.28); the forces of polymerizing filaments are derived in [7.6.26](/7.6.26). The general theory of fluctuations and dissipation in nonequilibrium steady states, of which motors are the prime example, is in [7.6.38](/7.6.38), and the physiology of muscle in [7.14](/7.14).

## 27.1. The Problem of Motors

### 27.1.1. Beating Diffusion

Transport by diffusion over a distance $L$ takes $t \sim L^2/2D$, transport at constant speed $t = L/v$. The two are equal at $L^* = 2D/v$, where the **Péclet number** $vL/D$ is about one. For a vesicle in cytoplasm, with $D \approx 0.01\,\mu\mathrm{m^2\,s^{-1}}$, and a motor speed of $1\,\mu\mathrm{m\,s^{-1}}$, $L^* \approx 20\,\mathrm{nm}$: for any organelle-sized cargo over any cellular distance, a motor wins. A small protein with $D = 10\,\mu\mathrm{m^2\,s^{-1}}$ diffuses across a $10\,\mu\mathrm{m}$ cell in a few seconds, but needs years to diffuse along a meter-long axon, which a motor covers in about ten days ([7.3.14](/7.3.14#sec-14.5.3)). Cells have four ways of beating diffusion: directed transport by motors ($t \propto L$), traveling chemical waves ($t \propto L/\sqrt{kD}$, [7.6.36](/7.6.36)), bulk flow (cytoplasmic streaming, blood), and active positioning by pushing or pulling filaments ([7.6.28](/7.6.28)). Motors are the molecular basis of the first and the engines behind the last two.

### 27.1.2. Four Classes of Motors

| Class | Track or substrate | Examples | Fuel | Step | Typical speed |
|---|---|---|---|---|---|
| Translational | actin filament | myosin II (muscle), myosin V (vesicles), myosin XI (cytoplasmic streaming) | ATP | $5$–$36\,\mathrm{nm}$ | $0.2$–$60\,\mu\mathrm{m\,s^{-1}}$ |
| | microtubule | kinesin-1, kinesin-5 (spindle), cytoplasmic and axonemal dyneins | ATP | $8\,\mathrm{nm}$ | $0.02$–$2\,\mu\mathrm{m\,s^{-1}}$ |
| | nucleic acid | helicases, RNA and DNA polymerases | ATP, NTP incorporation | $0.34\,\mathrm{nm}$ (1 bp) | $10$–$1000\,\mathrm{nt\,s^{-1}}$ |
| Rotary | stator in a membrane | $\mathrm{F_oF_1}$ **ATP synthase**, bacterial flagellar motor | ATP, ion gradient | $120°$, $36°$; about $14°$ | $10$–$1000\,\mathrm{Hz}$ |
| Polymerization | the growing filament itself | actin in lamellipodia and *Listeria* tails, microtubules, ParM | ATP, GTP | $2.7\,\mathrm{nm}$, $0.6\,\mathrm{nm}$ per subunit | $0.1$–$1\,\mu\mathrm{m\,s^{-1}}$ |
| Translocation | a polymer threaded through a pore or ring | protein import (TIM23–mtHsp70), proteasome, DNA packaging in phages | ATP, binding energy | $0.85\,\mathrm{nm}$ (φ29) | $10$–$100\,\mathrm{nm\,s^{-1}}$ |

The classes overlap: RNA polymerase walks along DNA but draws its energy from polymerization, and the phage packaging motor is a ring ATPase that translocates DNA. Even within one family the speeds differ a hundredfold, from kinesin-5, which slides spindle microtubules at about $20\,\mathrm{nm\,s^{-1}}$, to the organelle transporter kinesin-1 at $0.8\,\mu\mathrm{m\,s^{-1}}$, and from myosin V ($0.3\,\mu\mathrm{m\,s^{-1}}$) to the myosin XI of the alga *Chara* ($60\,\mu\mathrm{m\,s^{-1}}$). All cytoskeletal motors share an architecture: a motor domain that binds the track and the nucleotide, a mechanical element (lever arm, neck linker or linker) that amplifies conformational changes of a few ångströms in the nucleotide pocket into displacements of nanometers, and a tail that binds cargo or oligomerizes ([7.3.13](/7.3.13#sec-13.5.2)).

### 27.1.3. The Energy Scale

The unit of molecular work is $k_{\mathrm{B}}T = 4.1\,\mathrm{pN\,nm}$, and the free energy released by hydrolysing one ATP in the cell is about $20$–$25\,k_{\mathrm{B}}T$, $80$–$100\,\mathrm{pN\,nm}$ ([7.6.3](/7.6.3#sec-3.2.4)). This single number bounds every ATP-driven motor.

**Formula 27.1.1 (Thermodynamic Bound on the Force)** A motor that advances a distance $d$ per molecule of fuel, with free energy $\Delta\mu$ released per molecule, cannot move forward against a load larger than

$$
F_{\max} = \frac{\Delta\mu}{d}, \tag{27.1}
$$
since the work $Fd$ done per step cannot exceed the free energy supplied. The ratio $\eta = Fd/\Delta\mu$ is the thermodynamic efficiency of a step against the load $F$.

**Example 27.1.1 (Kinesin and myosin)** For kinesin-1, $d = 8.2\,\mathrm{nm}$ and $\Delta\mu \approx 20\,k_{\mathrm{B}}T = 82\,\mathrm{pN\,nm}$ give $F_{\max} \approx 10\,\mathrm{pN}$. The measured **stall force**, $6$–$7\,\mathrm{pN}$, corresponds to $Fd \approx 55\,\mathrm{pN\,nm}$, so even at stall kinesin converts only about $60\,\%$ of the free energy of ATP into work. Myosin V takes $36\,\mathrm{nm}$ steps and stalls at about $2.5$–$3\,\mathrm{pN}$, $Fd \approx 90$–$110\,\mathrm{pN\,nm}$: close to the whole free energy of one ATP under the conditions of the assay ($\Delta\mu \approx 25\,k_{\mathrm{B}}T$ at low ADP and phosphate). A long step forces a small stall force; a short step allows a large one. RNA polymerase, with $0.34\,\mathrm{nm}$ per nucleotide, stalls at $25$–$30\,\mathrm{pN}$, and the packaging motor of phage φ29, with $0.85\,\mathrm{nm}$ per ATP, at about $57\,\mathrm{pN}$.

![The energy scale of molecular motors. A: stall force against the step per fuel molecule (logarithmic axes). Diagonal lines are constant work per step, Fd = 1, 10 and 20 kBT (kBT = 4.1 pN nm); the shaded region above the 20 kBT line is forbidden for a motor that takes one step per ATP (Formula 27.1.1). Points are representative single-molecule measurements: kinesin-1, yeast cytoplasmic dynein, myosin V, skeletal myosin II (a single power stroke), *E. coli* RNA polymerase and the φ29 packaging motor. B: the work at stall per fuel molecule as a fraction of 20 kBT, including F₁-ATPase (torque 40 pN nm times 120°); in single-molecule assays with little ADP and phosphate the free energy of ATP is closer to 25 kBT, so values slightly above 1 are allowed](./plots/motor-energetics.py)

The force a single head exerts can also be estimated from the top down.

**Example 27.1.2 (Force per myosin head)** A human biceps has a cross-section of roughly $\pi(3\,\mathrm{cm})^2$; thick filaments sit about $60\,\mathrm{nm}$ apart in the myofibrillar lattice, so a cross-section contains about $(3\times10^{-2}/6\times10^{-8})^2 \approx 2.5\times10^{11}$ thick filaments, each with about $300$ heads, some $10^{14}$ heads in parallel. A maximal force of about $100\,\mathrm{N}$ (holding $10\,\mathrm{kg}$) shared among them is $1\,\mathrm{pN}$ per head, of the order of the $2$–$4\,\mathrm{pN}$ measured for a single head in an optical trap; only part of the heads are attached at any moment (**duty ratio**, [7.3.13](/7.3.13#sec-13.5.5)). Sarcomeres in series add their shortening velocities, heads in parallel add their forces.

### 27.1.4. Measuring Motors

Four kinds of in vitro experiment provide the data that the models of this chapter must explain.

1. In the gliding assay (**in vitro motility assay**), motors fixed to a glass surface move fluorescent filaments; the speed is that of unloaded motors working in a team, and the direction of gliding reveals the polarity of the motor.
2. In the bead assay, a single motor carries a micrometer-sized bead held in an optical trap; the trap measures the motor's displacement with nanometer and millisecond resolution and applies a load $F = -\kappa\,\Delta x$, which a feedback loop can hold constant (force clamp). Steps, dwell times, back steps and force–velocity curves come from such measurements ([7.6.17](/7.6.17#sec-17.2)).
3. Single-fluorophore localization (FIONA) tracks a dye on one head with a precision of about $1\,\mathrm{nm}$ ([7.6.12](/7.6.12)). A head of myosin V moves $74\,\mathrm{nm}$ every other step of the molecule, a head of kinesin $16.6\,\mathrm{nm}$: both walk hand over hand (**hand-over-hand mechanism**), not like an inchworm, whose heads would each move one step size.
4. High-speed atomic force microscopy films single motors at video rate; it showed myosin V swinging its lever arm and stepping hand over hand (Kodera and colleagues, 2010).

Engineering adds a fifth: the step of myosin V grows linearly with the number of IQ motifs (light-chain binding sites) in its lever arm, which shows that the lever arm is a rigid rod whose swing sets the step.

![Three single-molecule assays of translational motors (schematics, not to scale). A: gliding assay: motors attached to glass move a microtubule, which glides with its minus end leading when the motors walk toward the plus end; the velocity is that of unloaded motors. B: bead assay: one kinesin-1 carries a bead held in an optical trap; the displacement Δx of the bead from the trap center gives the load F = −κΔx, or a feedback loop clamps F. C: single-fluorophore tracking of myosin V labeled on one head, with a simulated trace of the label: 74 nm steps, each followed by two dwells, because the labeled head moves only on every second step of the molecule (hand-over-hand walking)](./plots/motor-assays.py)

## 27.2. Rectified Brownian Motion

### 27.2.1. Feynman's Ratchet

Can thermal motion alone be rectified into directed motion by an asymmetric structure? Smoluchowski (1912) and Feynman (1962) analysed a device that seems to do so.

**Definition 27.2.1 (Feynman Ratchet)** A *Feynman ratchet* is a thought experiment of a paddle wheel in a gas at temperature $T_1$, connected by an axle to a ratchet wheel with asymmetric teeth and a spring-loaded pawl at temperature $T_2$; molecular impacts on the paddles turn the axle, and the pawl seems to allow rotation in only one direction, so that the device would lift a weight using thermal fluctuations alone.

Feynman's analysis shows that at $T_1 = T_2$ the device does not rotate on average: the pawl itself is subject to thermal fluctuations and lifts off the teeth as often as needed to let the wheel slip backward, and the forward and backward rates, both proportional to $\mathrm{e}^{-\varepsilon/k_{\mathrm{B}}T}$ for a pawl spring energy $\varepsilon$, are equal. With $T_1 > T_2$ the device works as a heat engine whose efficiency is bounded by Carnot's. Directed motion needs a source of free energy, a difference of temperatures or, for motors at uniform temperature, a chemical potential difference. The general statement is a theorem about diffusion in a periodic potential.

**Theorem 27.2.1 (No Current at Equilibrium)** An overdamped Brownian particle in a time-independent periodic potential $U(x + L) = U(x)$, with no external force, has zero mean velocity in its stationary state, however asymmetric $U$ is.

**Proof** The stationary Smoluchowski equation (Formula 5.3.1 of [7.6.5](/7.6.5#sec-5.3.1)) requires a constant probability current $J = -D(p' + \beta U'p) = -D\mathrm{e}^{-\beta U}(\mathrm{e}^{\beta U}p)'$, with $\beta = 1/k_{\mathrm{B}}T$. Hence $(\mathrm{e}^{\beta U}p)' = -(J/D)\mathrm{e}^{\beta U}$. Integrating over one period and using the periodicity of $p$ and $U$, the left side gives $\mathrm{e}^{\beta U(L)}p(L) - \mathrm{e}^{\beta U(0)}p(0) = 0$, so $J\int_0^L\mathrm{e}^{\beta U}\,\mathrm{d}x = 0$. The integral is positive, so $J = 0$, and the stationary state is the Boltzmann distribution $p \propto \mathrm{e}^{-\beta U}$. $\square$

The theorem is the mechanical form of the second law and of detailed balance ([7.6.3](/7.6.3#sec-3.5.2)). It also disposes of **Maxwell's demon** in molecular form ([7.6.2](/7.6.2)): a passive asymmetric structure is not enough. To obtain directed motion the potential must be tilted by a force, or changed in time by an external driving such as the binding and hydrolysis of ATP.

### 27.2.2. Flashing and Tilting Ratchets

**Definition 27.2.2 (Flashing Ratchet)** A *flashing ratchet* is a Brownian particle in an asymmetric periodic potential that is switched on and off, by an external clock or by chemical reactions; diffusion while the potential is off, followed by capture in the nearest well when it is on, produces a net drift toward the steep side of the wells even though the potential has no average slope.

Consider a sawtooth of period $L$ and barrier height $U_0 \gg k_{\mathrm{B}}T$ that rises from each minimum over a short distance $\alpha L$ and falls over $(1-\alpha)L$. While the potential is on, particles collect at the minima. When it is switched off for a time $t_{\mathrm{off}}$, each spreads as a Gaussian of variance $2Dt_{\mathrm{off}}$; when it is switched on again, a particle that has moved more than $\alpha L$ forward falls into the next well, while one has to move $(1-\alpha)L$ backward to fall into the previous one.

**Formula 27.2.1 (Drift of a Flashing Ratchet)** For $U_0 \gg k_{\mathrm{B}}T$ and an on time long enough for relaxation into the wells, the mean velocity is

$$
v \approx \frac{L}{t_{\mathrm{on}} + t_{\mathrm{off}}}\cdot\frac12\left[\operatorname{erfc}\frac{\alpha L}{\sqrt{4Dt_{\mathrm{off}}}} - \operatorname{erfc}\frac{(1-\alpha)L}{\sqrt{4Dt_{\mathrm{off}}}}\right]. \tag{27.2}
$$

The velocity vanishes for a symmetric potential ($\alpha = \frac12$), for very short off times (the particle does not reach the next barrier) and for very long ones (time is wasted), and it has a maximum at $t_{\mathrm{off}} \approx (\alpha L)^2/D$. The energy is supplied by switching: each time the potential is turned on, the particles are lifted to the energies they happen to have, which costs free energy of order $U_0$ per cycle. For a protein, $L = 8\,\mathrm{nm}$ and $D \approx 1\,\mu\mathrm{m^2\,s^{-1}}$ for a tethered head give an optimal off time of microseconds and speeds far above those of real motors, so diffusion of a detached head is not what limits motor speed. A tilting ratchet, in which the potential is fixed but a zero-mean force fluctuates in time, works on the same principle if the fluctuations are not thermal (Magnasco 1993).

![The flashing ratchet (units: period L, diffusion coefficient D, energies in kBT). A: the asymmetric sawtooth (barrier 8 kBT, rising over αL = 0.2L and falling over 0.8L) and the particle densities from a Langevin simulation at the end of the on phase (narrow peaks in the wells) and at the end of the off phase (spread by free diffusion); more particles cross the near barrier on the right than the far one on the left. B: the drift velocity against the off time at fixed on time 0.3 L²/D: simulation of 400 particles (points) and Formula 27.2.1 (line; evaluated, since the barrier is only 8 kBT, with the committor probability of reaching each well from the position at switch-on). The drift has a maximum near t_off ≈ (αL)²/D](./plots/flashing-ratchet.py)

### 27.2.3. Power Strokes and Brownian Ratchets

Two idealizations of motor mechanism are often contrasted. In a **Brownian ratchet** ([7.3.13](/7.3.13#sec-13.4.1)), the motor's motion is thermal, and the chemical energy is spent on rectifying it, by binding that traps forward excursions; the load acts on the diffusive step, and a ratchet can be very efficient only at small speeds. In a power stroke, the chemical reaction itself drives a conformational change that strains an elastic element, and the strain relaxes by moving the load.

**Formula 27.2.2 (Elastic Power Stroke)** If a nucleotide-driven conformational change of size $\delta$ strains an elastic element of stiffness $\kappa$ in a motor bound to its track, the motor exerts at most $F = \kappa\delta$ and, if it detaches when the strain has relaxed to zero, an average force $\langle F\rangle = \kappa\delta/2$ over the working stroke, storing and delivering the work $\frac12\kappa\delta^2$.

For myosin II, a stiffness of about $2\,\mathrm{pN\,nm^{-1}}$ and a stroke of $5\,\mathrm{nm}$ give a peak force of $10\,\mathrm{pN}$ and $25\,\mathrm{pN\,nm}$ of work, a quarter of the free energy of one ATP. The distinction between power stroke and ratchet is less sharp than it seems: every conformational change is a thermally activated transition over a barrier, and the question is only which of the transitions of the cycle carry the load. Kinesin combines both. ATP binding to the front head docks its neck linker, a partial power stroke that throws the rear head forward; the free head then finds its next binding site by diffusion, a ratchet step. Kinetic models of the next section capture both pictures through the way the load enters the rate constants.

## 27.3. Master-Equation Models of Motors

### 27.3.1. The Position–State Description

Motors step along periodic tracks with a period $a$ (8.2 nm for a microtubule, 36 nm for one face of an actin helix), and at each position they can be in several internal states, defined by the nucleotide bound to each head and by the conformation of the mechanical elements. The probability $p_m(n, t)$ of being at site $n$ in internal state $m$ obeys a **master equation** on the state space $\{(n, m)\}$; its parameters are the rate constants between states, and its consequences are the observables: the mean velocity, its dependence on load and ATP, the dispersion of positions, the distribution of dwell times between steps. The program is the reverse of the experiment: speeds, dwells and fluctuations are measured under controlled loads and nucleotide concentrations, and rate constants are fitted. Thermodynamics constrains the fit through detailed balance.

### 27.3.2. The One-State Model

The simplest model has no internal states: the motor hops forward with rate $k_+$ and backward with rate $k_-$. A real motor cannot be a one-state motor (if its internal state never changed, it could not tell forward from backward, and $k_+ = k_-$), but the model is the right description on time scales longer than the internal cycle, with $k_\pm$ the effective rates of complete forward and backward cycles.

**Formula 27.3.1 (Drift and Diffusion of a Stepping Motor)** For a motor that steps $\pm a$ with rates $k_\pm$, the master equation $\dot p(n) = k_+p(n-1) + k_-p(n+1) - (k_+ + k_-)p(n)$ becomes, for distances large compared with $a$, the drift–diffusion equation $\partial_tp = -V\partial_xp + D\partial_x^2p$ with

$$
V = a(k_+ - k_-), \qquad D = \frac{a^2}{2}(k_+ + k_-), \tag{27.3}
$$
and a motor started at $x = 0$ has the Gaussian distribution $p(x, t) = (4\pi Dt)^{-1/2}\exp[-(x - Vt)^2/4Dt]$.

The derivation, a second-order Taylor expansion of the master equation, is in [7.6.5](/7.6.5#sec-5.5.2). A population of motors started together is a pack of sprinters that moves at $V$ and spreads as $\sqrt{2Dt}$.

### 27.3.3. Generalized Detailed Balance and the Stall Force

The ratio $k_+/k_-$ is not free. A forward step that hydrolyses one ATP moves the system from one state to another of lower free energy by $\Delta\mu - Fa$: the motor releases $\Delta\mu$ of chemical free energy and does work $Fa$ against the load.

**Theorem 27.3.1 (Generalized Detailed Balance)** For a tightly coupled motor that hydrolyses one fuel molecule per forward step of length $a$ against a load $F$, and synthesizes one per backward step, the forward and backward rates satisfy

$$
\frac{k_+(F)}{k_-(F)} = \exp\left[\frac{\Delta\mu - Fa}{k_{\mathrm{B}}T}\right], \qquad \Delta\mu = \Delta\mu^\circ + k_{\mathrm{B}}T\ln\frac{[\mathrm{ATP}]}{[\mathrm{ADP}][\mathrm{P_i}]}, \tag{27.4}
$$
and the motor stalls exactly at $F_{\mathrm{s}} = \Delta\mu/a$, the bound of Formula 27.1.1. For a motor with internal states, the same relation holds for the product of rate constants around any cycle that advances by $a$ with one ATP, divided by the product of the reverse rates.

**Proof** Consider the motor, the solution of ATP, ADP and $\mathrm{P_i}$ and the load as one system. If the concentrations were at chemical equilibrium and no load acted, the system would be in thermal equilibrium and every elementary transition would be balanced by its reverse; the ratio of forward to backward rates of each transition equals the Boltzmann factor of the free-energy difference it causes (Theorem 3.5.1 of [7.6.3](/7.6.3#sec-3.5.2)). Rate constants are properties of the molecule and its immediate environment and do not depend on whether the bath is at equilibrium; only the concentration factors and the work against the load change the free-energy difference of a step. A forward cycle changes the free energy of the bath by $-\Delta\mu$ and that of the load by $+Fa$, which gives Eq. (27.4); for a cycle through several internal states the free energies of the intermediate states cancel in the product. At $F = F_{\mathrm{s}}$ the ratio is one and $V = a(k_+ - k_-) = 0$. $\square$

The theorem fixes the ratio but not the rates themselves. How the load is divided between the forward and backward rates depends on where along the reaction coordinate the transition state lies, as in the **Bell model** of bond rupture ([7.6.17](/7.6.17#sec-17.5)).

**Formula 27.3.2 (Load Distribution)** Write $k_+(F) = k_+^0\,\mathrm{e}^{-\theta Fa/k_{\mathrm{B}}T}$ and $k_-(F) = k_-^0\,\mathrm{e}^{(1-\theta)Fa/k_{\mathrm{B}}T}$, with $k_+^0/k_-^0 = \mathrm{e}^{\Delta\mu/k_{\mathrm{B}}T}$ and a load distribution factor $0 \le \theta \le 1$, the fraction of the step that lies before the transition state. Then

$$
V(F) = a\left[k_+^0\,\mathrm{e}^{-\theta Fa/k_{\mathrm{B}}T} - k_-^0\,\mathrm{e}^{(1-\theta)Fa/k_{\mathrm{B}}T}\right]. \tag{27.5}
$$

If the load acts on the forward rate ($\theta = 1$), the speed falls exponentially from the smallest loads. If it acts on the backward rate ($\theta = 0$), the speed stays at $ak_+^0$ until the load approaches stall, where backward steps take over abruptly. Both curves pass through zero at the same $F_{\mathrm{s}}$, and beyond it the motor runs backward, as observed for kinesin and myosin V. The measured force–velocity curve of myosin V, nearly flat under forward and moderate backward loads and steep near stall, resembles the case $\theta \approx 0$ (Gebhardt and colleagues, 2006); pulling forward on myosin V speeds its stepping only slightly, while pulling backward with the same force slows it severalfold, because the load-dependent transition is not the one that consumes ATP (Purcell and colleagues, 2005).

![The one-state motor. A: thirty stochastic trajectories (Gillespie simulation) of a motor stepping 8 nm forward at 100 s⁻¹ and backward at 10 s⁻¹, with the mean Vt and the band Vt ± √(2Dt) of Formula 27.3.1. B: velocity against load from Formula 27.3.2 with Δμ = 8 kBT (a small value, chosen so that all curves remain visible; stall at Δμ/a = 4.1 pN) and the load acting on the forward rate (θ = 1), equally (θ = 0.5) or on the backward rate (θ = 0); negative loads assist the motor. The vertical axis is linear between ±10 nm/s and logarithmic outside. All curves cross zero at the same stall force; their shapes differ](./plots/one-state-model.py)

### 27.3.4. ATP Dependence and the Limits of One State

The same argument places the ATP dependence. The free energy of hydrolysis, Eq. (27.4), changes with $\ln[\mathrm{ATP}]$, and the ATP dependence can sit in the forward rate, $k_+ = k_+'[\mathrm{ATP}]$, or in the backward rate.

**Formula 27.3.3 (One-State ATP Dependence)** A load-free one-state motor whose forward rate carries the ATP dependence moves at $V = a(k_+'[\mathrm{ATP}] - k_-)$, linear in [ATP]; with the ATP dependence in the backward rate instead, $V = a(k_+ - k_-'/[\mathrm{ATP}])$, saturating at high [ATP] but negative at low [ATP].

Neither agrees with experiment. Kinesin's velocity rises linearly at low [ATP] and saturates at high [ATP], the hyperbola of the **Michaelis–Menten equation** with $K_{\mathrm{M}} \approx 50$–$100\,\mu\mathrm{M}$ (Schnitzer and Block, 1997; Visscher and colleagues, 1999): two regimes, each limited by a different transition, need at least two states per site. The Arrhenius form of the one-state rates also fails where the barrier for one direction would vanish. The one-state model is a framework for thinking about loads; the internal cycle is needed for everything else.

### 27.3.5. The Two-State Model

Let a motor at site $n$ be in state $0$ or $1$. It goes from $0$ to $1$ at the same site with rate $u_0$ (for example ATP binding and a conformational change) and back with $w_1$; from state $1$ at site $n$ to state $0$ at site $n + 1$ with $u_1$, completing a step, and back with $w_0$ (from $0$ at $n+1$ to $1$ at $n$).

**Theorem 27.3.2 (Velocity and Diffusion of the Two-State Motor)** In the stationary state the two-state motor moves with

$$
V = a\,\frac{u_0u_1 - w_0w_1}{u_0 + u_1 + w_0 + w_1}, \qquad D = \frac{a^2}{2}\,\frac{u_0u_1 + w_0w_1 - 2(V/a)^2}{u_0 + u_1 + w_0 + w_1}, \tag{27.6}
$$
independently of how the displacement $a$ is divided between the two transitions.

**Proof** Summing the master equations $\dot p_0(n) = u_1p_1(n-1) + w_1p_1(n) - (u_0 + w_0)p_0(n)$ and $\dot p_1(n) = u_0p_0(n) + w_0p_0(n+1) - (u_1 + w_1)p_1(n)$ over $n$ gives a two-state system for the total probabilities $P_0, P_1$, with stationary solution $P_0 = (u_1 + w_1)/\Sigma$, $P_1 = (u_0 + w_0)/\Sigma$, $\Sigma = u_0 + u_1 + w_0 + w_1$. Each completed cycle advances the motor by $a$, so $V = a(P_1u_1 - P_0w_0)$, which simplifies to the first formula; if the transition $0 \to 1$ moves the motor by $\delta$ and $1 \to 0$ by $a - \delta$, the contributions $\delta(P_0u_0 - P_1w_1)$ and $(a-\delta)(P_1u_1 - P_0w_0)$ add to the same result because both fluxes are equal in the stationary state. For $D$, introduce the generating function $\sum_n\mathrm{e}^{sn}p_m(n, t)$: its growth rate $\lambda(s)$, the largest eigenvalue of the $2\times2$ matrix obtained by attaching $\mathrm{e}^{\pm s}$ to the transitions that change $n$, generates the cumulants of the position, $V = a\lambda'(0)$ and $2D = a^2\lambda''(0)$. Differentiating the characteristic equation $(\lambda + u_0 + w_0)(\lambda + u_1 + w_1) = (u_1\mathrm{e}^s + w_1)(u_0 + w_0\mathrm{e}^{-s})$ twice at $s = 0$, $\lambda = 0$, gives the second formula (Derrida, 1983). $\square$

The velocity has the form $V = a(k_+ - k_-)$ with effective rates $k_+ = u_0u_1/\Sigma$ and $k_- = w_0w_1/\Sigma$, and the ratio $k_+/k_- = u_0u_1/w_0w_1$ is fixed by Theorem 27.3.1. With $u_0 = k_{\mathrm{on}}[\mathrm{ATP}]$ and negligible reverse rates, $V = au_1k_{\mathrm{on}}[\mathrm{ATP}]/(k_{\mathrm{on}}[\mathrm{ATP}] + u_1 + w_1)$: the Michaelis–Menten form with $V_{\max} = au_1$ and $K_{\mathrm{M}} = (u_1 + w_1)/k_{\mathrm{on}}$, as for an enzyme whose product is a step. Load enters through whichever rates involve motion, so it changes both $V_{\max}$ and $K_{\mathrm{M}}$. The two-step irreversible version of this model was used for kinesin in [Formula 14.5.1](/7.3.14#fml-14.5.1) of 7.3.14; the reversible version here also describes stall and backward motion, and gives the dispersion $D$ that the next section uses.

### 27.3.6. A Kinetic Model of Kinesin

Three observations on single kinesin molecules require one more ingredient. Load lowers $V_{\max}$ and raises $K_{\mathrm{M}}$ (Visscher and colleagues, 1999): some load acts on ATP binding itself, or on a transition in rapid equilibrium with it. Near stall kinesin takes back steps, and back steps, like forward steps, consume ATP; the ratio of forward to backward steps falls exponentially with load, about $e$-fold per $1\,\mathrm{pN}$, from about $800$ without load to one at the stall force of about $7\,\mathrm{pN}$, which does not depend on [ATP] (Carter and Cross, 2005). And at saturating ATP the randomness parameter is about $1/2$ (Section 27.4), so two comparable transitions remain when ATP binding is fast.

**Formula 27.3.4 (Three-State Model of Kinesin)** Let state $0$ (front head empty) bind ATP at $u_0 = k_{\mathrm{on}}[\mathrm{ATP}]\,\mathrm{e}^{-Fd_0/k_{\mathrm{B}}T}$ and lose it at $k_{\mathrm{off}}$; from the ATP state $1$ let the motor commit to a forward step at $k_1(F) = k_1^0\,\mathrm{e}^{-Fd_1/k_{\mathrm{B}}T}$ or to an ATP-driven backward step at $k_{\mathrm{b}}(F) = k_{\mathrm{b}}^0\,\mathrm{e}^{Fd_{\mathrm{b}}/k_{\mathrm{B}}T}$, and let the stepped state $2$ return to state $0$ at the load-independent rate $k_2$ (hydrolysis and phosphate release). Then

$$
V = \frac{a(k_1 - k_{\mathrm{b}})}{\dfrac{k_{\mathrm{off}} + k_1 + k_{\mathrm{b}}}{u_0} + 1 + \dfrac{k_1 + k_{\mathrm{b}}}{k_2}}, \qquad
F_{\mathrm{s}} = \frac{k_{\mathrm{B}}T}{d_1 + d_{\mathrm{b}}}\ln\frac{k_1^0}{k_{\mathrm{b}}^0}, \tag{27.7}
$$
the velocity is of Michaelis–Menten form in [ATP] with $V_{\max} = a(k_1 - k_{\mathrm{b}})k_2/(k_2 + k_1 + k_{\mathrm{b}})$ and $K_{\mathrm{M}} = \mathrm{e}^{Fd_0/k_{\mathrm{B}}T}(k_{\mathrm{off}} + k_1 + k_{\mathrm{b}})k_2/[k_{\mathrm{on}}(k_2 + k_1 + k_{\mathrm{b}})]$, and the ATP turnover is $V(k_1 + k_{\mathrm{b}})/[a(k_1 - k_{\mathrm{b}})]$.

The formula follows from the stationary balance $P_0u_0 = P_1(k_{\mathrm{off}} + k_1 + k_{\mathrm{b}})$, $P_1(k_1 + k_{\mathrm{b}}) = P_2k_2$, $P_0 + P_1 + P_2 = 1$, with $V = aP_1(k_1 - k_{\mathrm{b}})$. The stall force is where forward and backward commitments are equally likely, which is independent of ATP because both branches start from the same state.

**Example 27.3.1 (Fitting kinesin)** With $a = 8.2\,\mathrm{nm}$, $k_{\mathrm{on}} = 1.5\,\mu\mathrm{M^{-1}\,s^{-1}}$, $k_{\mathrm{off}} = 10\,\mathrm{s^{-1}}$, $k_1^0 = k_2 = 200\,\mathrm{s^{-1}}$, $k_{\mathrm{b}}^0 = k_1^0/800$, $d_0 = 0.8\,\mathrm{nm}$, $d_1 = 1.2\,\mathrm{nm}$ and $d_{\mathrm{b}} = 2.6\,\mathrm{nm}$, Formula 27.3.4 gives $V_{\max} = 820\,\mathrm{nm\,s^{-1}}$ and $K_{\mathrm{M}} = 70\,\mu\mathrm{M}$ without load, $V = 190\,\mathrm{nm\,s^{-1}}$ at $5.6\,\mathrm{pN}$ and $2\,\mathrm{mM}$ ATP, a $K_{\mathrm{M}}$ that rises by about $50\,\%$ up to $6.5\,\mathrm{pN}$, and a stall force of $k_{\mathrm{B}}T\ln800/(3.8\,\mathrm{nm}) = 7.2\,\mathrm{pN}$ at every ATP concentration: the behavior measured in force-clamp experiments. The distances $d_0 + d_1 = 2\,\mathrm{nm}$ and $d_{\mathrm{b}}$ are much smaller than the step: the load acts on short movements of the neck linker and the diffusing head, not on the whole $8\,\mathrm{nm}$ step. A model with four or more states, with alternating head-specific transitions, is needed to fit all the data (Fisher and Kolomeisky, 2001; Clancy and colleagues, 2011), but the three-state model reproduces the main features with few parameters.

![A three-state kinetic model of kinesin-1 (Formula 27.3.4, parameters of Example 27.3.1). A: force–velocity curves at 2 mM and 5 µM ATP (the latter multiplied by 10): both cross zero at the same stall force, 7.2 pN, and the motor runs backward beyond it. B: efficiency at 2 mM ATP, F V divided by the free energy of the ATP turned over (25 kBT per ATP), compared with the tight-coupling efficiency Fa/Δμ: at low load the two agree; near stall, ATP-consuming back steps make the efficiency fall to zero. C: velocity against [ATP] at three loads, Michaelis–Menten curves. D: with load, the maximal velocity falls and the Michaelis constant rises, as measured](./plots/kinesin-model.py)

## 27.4. Dwell Times and the Randomness Parameter

### 27.4.1. Dwell-Time Distributions

A single-molecule trace yields not only an average velocity but a sequence of dwell times between steps. Their distribution reveals the number of transitions in the cycle even when the intermediates are invisible. A single rate-limiting transition of rate $k$ gives the **exponential distribution** $p(t) = k\mathrm{e}^{-kt}$, whose most probable dwell is zero. Two sequential irreversible transitions give the **convolution** of two exponentials.

**Formula 27.4.1 (Dwell Time of a Two-Step Cycle)** If a step requires two sequential irreversible transitions with rates $k_1 \ne k_2$, the dwell time has density

$$
p(t) = \int_0^t k_1\mathrm{e}^{-k_1\tau}\,k_2\mathrm{e}^{-k_2(t - \tau)}\,\mathrm{d}\tau = \frac{k_1k_2}{k_2 - k_1}\left(\mathrm{e}^{-k_1t} - \mathrm{e}^{-k_2t}\right), \tag{27.8}
$$
which rises from zero, peaks at $t^* = \ln(k_2/k_1)/(k_2 - k_1)$ and has mean $1/k_1 + 1/k_2$; for $k_1 = k_2 = k$ it becomes $k^2t\,\mathrm{e}^{-kt}$, and for $n$ equal steps the **gamma distribution** $k^nt^{n-1}\mathrm{e}^{-kt}/(n-1)!$.

The rise at short times is the signature of a hidden step: a dwell cannot be short if two things must happen. For myosin V at low ATP, dwell-time histograms of single-headed constructs and of labeled heads are fitted by Eq. (27.8) with one ATP-dependent rate ($k_1 = k_{\mathrm{on}}[\mathrm{ATP}]$) and one ATP-independent rate ($k_2 \approx 12$–$20\,\mathrm{s^{-1}}$, ADP release from the rear head); under load only $k_2$ changes, which is why load and ATP act on different transitions (Purcell and colleagues, 2005).

**Theorem 27.4.1 (Counting Steps)** If each cycle of a motor consists of $n$ sequential irreversible transitions with rates $k_1, \dots, k_n$, the dwell time $\tau$ has mean $\sum_i1/k_i$ and variance $\sum_i1/k_i^2$, and

$$
n_{\min} \equiv \frac{\langle\tau\rangle^2}{\operatorname{Var}(\tau)} \le n, \tag{27.9}
$$
with equality when all rates are equal.

**Proof** The dwell is a sum of independent exponential waiting times, so means and variances add, and an exponential of rate $k_i$ has mean $1/k_i$ and variance $1/k_i^2$. By the Cauchy–Schwarz inequality, $\left(\sum_i1/k_i\right)^2 \le n\sum_i1/k_i^2$, with equality if all $1/k_i$ are equal. $\square$

The ratio $n_{\min}$ is a lower bound on the number of rate-limiting transitions: fast transitions do not count, and reversible ones can make it smaller, so a measured value of 2 means "at least two comparable steps".

### 27.4.2. The Randomness Parameter

Dwell times can be measured only when steps are resolved. A coarser measure uses the spreading of positions, which is visible even in noisy traces.

**Definition 27.4.1 (Randomness Parameter)** The **randomness parameter** of a motor with step $a$ is

$$
r = \lim_{t\to\infty}\frac{\langle x^2(t)\rangle - \langle x(t)\rangle^2}{a\langle x(t)\rangle} = \frac{2D}{Va}, \tag{27.10}
$$
the ratio of the dispersion of the position to that of a Poisson stepper with the same mean velocity.

For a motor that steps only forward, renewal theory shows that $r = \operatorname{Var}(\tau)/\langle\tau\rangle^2 = 1/n_{\min}$: a single Poisson step gives $r = 1$, a perfectly regular clock $r = 0$, and $n$ equal hidden transitions $r = 1/n$ (Schnitzer and Block, 1995). Backward steps increase $r$. For the one-state motor of Theorem 27.3.1, Eq. (27.3) gives

$$
r = \frac{k_+ + k_-}{k_+ - k_-} = \coth\frac{\Delta\mu - Fa}{2k_{\mathrm{B}}T}, \tag{27.11}
$$
which is close to one far from stall and diverges at stall, where the motor diffuses without drifting. A randomness parameter below one is therefore direct evidence for internal states.

**Example 27.4.1 (Kinesin's hidden steps)** Kinesin's randomness at saturating ATP and low load is about $0.5$; it approaches one at low ATP, where ATP binding is the single rate-limiting step, and rises near stall (Visscher and colleagues, 1999). At least two transitions of comparable rate, each about $2V_{\max}/a \approx 200\,\mathrm{s^{-1}}$, follow ATP binding; that the minimum of $r$, below $0.5$, occurs at intermediate ATP, where ATP binding has slowed to the same rate, shows a third. These are exactly the transitions $k_1$ and $k_2$ of Formula 27.3.4, and the model reproduces the measured pattern without further fitting.

![Dwell times and the randomness parameter. A: dwell-time densities of cycles of n sequential irreversible transitions of equal rate (gamma distributions, randomness r = 1/n), all with mean 10 ms, and a histogram of 3000 simulated dwells of the two-step cycle; the more hidden steps, the narrower the distribution and the rarer short dwells. B: randomness of the kinesin model (Formula 27.3.4) against [ATP] at loads of 1.05 and 5.63 pN, from the exact long-time cumulants of the master equation (lines) and from 3000 simulated runs of 200 cycles each (points). At low ATP one step limits (r → 1); at saturating ATP two equal steps remain (r → 1/2); in between three steps are comparable (r ≈ 0.37); near stall back steps raise r above 1](./plots/dwell-times.py)

## 27.5. Coupling, Efficiency and Precision

### 27.5.1. Tight and Loose Coupling

**Definition 27.5.1 (Tight Coupling)** A motor is *tightly coupled* if it advances by exactly one step per fuel molecule consumed, in both directions: each forward step consumes one ATP and each backward step synthesizes one. It is loosely coupled if fuel can be consumed without a step (futile cycles) or steps can occur without fuel turnover (slips).

A tightly coupled motor obeys Theorem 27.3.1 with a single cycle, stalls at $F_{\mathrm{s}} = \Delta\mu/a$, and is at equilibrium at stall: its efficiency $Fa/\Delta\mu$ tends to one there, although it delivers no power. Kinesin is tightly coupled at low load, one ATP per $8\,\mathrm{nm}$ step (Schnitzer and Block, 1997; Coy and colleagues, 1999), but its back steps under load consume ATP as forward steps do. Its stall force, $7\,\mathrm{pN}$ rather than $\Delta\mu/a \approx 10$–$12\,\mathrm{pN}$, is not an equilibrium but a balance of two ATP-consuming pathways, and at stall the motor burns ATP doing nothing (panel B of the figure in 27.3.6). F₁-ATPase, by contrast, is tightly coupled up to its stall torque and can be driven backward to synthesize ATP ([7.6.28](/7.6.28)). Loose coupling is not inefficiency for its own sake: a motor whose stall is set kinetically can hold a high load without being pushed backward along its track, a property useful for a cargo transporter.

### 27.5.2. Efficiency and Power

The mechanical power of a motor against a load is $FV$, and the chemical power consumed is $\Delta\mu J_{\mathrm{ATP}}$, where $J_{\mathrm{ATP}}$ is the rate of ATP turnover.

**Formula 27.5.1 (Thermodynamic Efficiency)** The efficiency of a motor is $\eta = FV/(\Delta\mu J_{\mathrm{ATP}})$; for a tightly coupled motor $J_{\mathrm{ATP}} = V/a$ and $\eta = Fa/\Delta\mu$. The difference between the chemical power and the mechanical power, $T\dot S = \Delta\mu J_{\mathrm{ATP}} - FV \ge 0$, is dissipated as heat in the bath (the **entropy production** of the motor).

Efficiency and power cannot both be maximal: the efficiency of a tightly coupled motor is largest at stall, where the power vanishes, and the power is largest at intermediate loads. In the kinesin model the efficiency at $2\,\mathrm{mM}$ ATP peaks at about $30\,\%$ near $5\,\mathrm{pN}$ for $\Delta\mu = 25\,k_{\mathrm{B}}T$. Muscle converts about $25$–$40\,\%$ of the free energy of ATP into work at its working loads, and the heat produced is how mammals keep warm when they shiver. The comparison with the Carnot efficiency of a heat engine ([5.2](/5.2)) is misleading: motors are isothermal machines, converting free energy directly, and their efficiency is limited not by temperature but by the speed at which they must run.

### 27.5.3. The Cost of Precision

A motor's steps are random; a more regular motor must dissipate more. For the one-state motor, Eq. (27.11) gives $r\cdot(\Delta\mu - Fa)/k_{\mathrm{B}}T = x\coth(x/2) \ge 2$ with $x = (\Delta\mu - Fa)/k_{\mathrm{B}}T$: a randomness $r$ requires a dissipation of at least $2k_{\mathrm{B}}T/r$ per step. The same inequality, the thermodynamic uncertainty relation (Barato and Seifert, 2015), holds for any Markov process in a nonequilibrium steady state ([7.6.38](/7.6.38)): the relative variance of any current times the total entropy produced is at least $2k_{\mathrm{B}}$. Applied to motors it bounds the efficiency by measurable quantities.

**Formula 27.5.2 (Efficiency Bound from Fluctuations)** For a motor moving at mean velocity $V$ with diffusion coefficient $D$ against a load $F$,

$$
\eta \le \frac{1}{1 + Vk_{\mathrm{B}}T/(DF)}, \tag{27.12}
$$
whatever its internal mechanism (Pietzonka, Barato and Seifert, 2016).

The bound follows from the uncertainty relation $T\dot S \ge k_{\mathrm{B}}TV^2/D$ and $\eta = FV/(FV + T\dot S)$. A motor that is both fast and regular (large $V$, small $D$) cannot be efficient against small loads. For the kinesin model at $4\,\mathrm{pN}$ and $2\,\mathrm{mM}$ ATP, $V = 350\,\mathrm{nm\,s^{-1}}$ and $D = 1060\,\mathrm{nm^2\,s^{-1}}$ ($r = 0.74$) give $\eta \le 0.75$, compared with the actual $0.29$: the bound is loose because the model dissipates much of its free energy in the ATP binding step. The bound requires no model and is used to infer, from fluctuations alone, how much free energy a motor must be spending (Hwang and Hyeon, 2018). The same trade-off between precision and dissipation applies to biochemical clocks such as the cyanobacterial KaiABC oscillator ([7.6.38](/7.6.38)).

## 27.6. Teams of Motors

### 27.6.1. Load Sharing

Most cargoes are carried by several motors, and many motors work only in teams. Suppose $N$ identical motors with linear force–velocity curves $v(f) = v_0(1 - f/F_{\mathrm{s}})$ share a load $F$ equally, so that each carries $F/N$.

**Formula 27.6.1 (Load Sharing)** The team moves at $v(F) = v_0\left(1 - \dfrac{F}{NF_{\mathrm{s}}}\right)$: the stall force adds, the unloaded velocity does not.

This idealization fails in two ways. Load is rarely shared equally: the leading motor of a team bound to a stiff cargo carries most of the load until it detaches, and kinesins rarely cooperate well (Jamison and colleagues, 2010). And the number of bound motors fluctuates, because each motor binds and unbinds stochastically, and unbinding accelerates under load as for a slip bond (**slip bond**, [7.3.23](/7.3.23)). The mean run length of a cargo with up to $N$ motors grows almost geometrically with $N$ ([Formula 14.5.2](/7.3.14#fml-14.5.2) of 7.3.14). For teams of low-duty-ratio motors such as myosin II, continuous motion needs at least about $1/r_{\mathrm{duty}}$ heads ([7.3.13](/7.3.13#sec-13.5.5)): with a duty ratio of $0.04$, some $25$ heads, and $50$–$100$ for smooth sliding; a two-headed processive motor needs a duty ratio above $1/2$ per head.

### 27.6.2. The Tug of War

Many cargoes, endosomes, mitochondria, pigment granules, lipid droplets, carry motors of opposite directionality and move bidirectionally in saltatory runs. Inhibiting either motor often stops movement in both directions (the paradox of co-dependence). A model with purely mechanical interactions explains much of this behavior.

**Definition 27.6.1 (Tug-of-War Model)** In the *tug-of-war model* (Müller, Klumpp and Lipowsky, 2008) a cargo carries $N_+$ plus-end and $N_-$ minus-end motors, of which $n_+$ and $n_-$ are bound. Bound motors of the same team share the load equally, the cargo moves with the velocity at which the forces of the two teams balance, each bound motor unbinds at $\varepsilon(f) = \varepsilon_0\,\mathrm{e}^{f/F_{\mathrm{d}}}$ under its load $f$ and each unbound motor rebinds at $\pi_0$; the state $(n_+, n_-)$ performs a Markov jump process.

**Formula 27.6.2 (Cargo Velocity in a Tug of War)** For linear force–velocity curves with forward velocity $v_{\mathrm{F}}$ below stall and backward velocity $v_{\mathrm{B}}$ (per unit of $f/F_{\mathrm{s}} - 1$) above it, if the plus team is stronger, $n_+F_{\mathrm{s}+} > n_-F_{\mathrm{s}-}$,

$$
v_{\mathrm{c}} = \frac{n_+F_{\mathrm{s}+} - n_-F_{\mathrm{s}-}}{n_+F_{\mathrm{s}+}/v_{\mathrm{F}+} + n_-F_{\mathrm{s}-}/v_{\mathrm{B}-}}, \tag{27.13}
$$
and symmetrically, with $v_{\mathrm{B}+}$ and $v_{\mathrm{F}-}$, if the minus team is stronger; the load on each motor of the winning team is $F_{\mathrm{c}}/n_\pm$ with $F_{\mathrm{c}} = n_+F_{\mathrm{s}+}(1 - v_{\mathrm{c}}/v_{\mathrm{F}+})$.

The model has a dynamical instability. If one motor of a team unbinds, its partners carry more load and unbind faster, so the team loses quickly once it starts to lose: the cargo switches between fast runs in either direction, with brief stalemates, rather than creeping at the average velocity. Because backward-dragged motors move slowly ($v_{\mathrm{B}} \ll v_{\mathrm{F}}$), the stronger team pulls at nearly full speed. The model predicts that small changes in the number of active motors, or in their binding rates, switch the cargo between plus-directed, minus-directed and bidirectional motility, which is how adaptors and phosphorylation regulate melanosome aggregation and dispersion. With the measured parameters of kinesin-1 and of single mammalian dyneins, which are much weaker ($F_{\mathrm{s}} \approx 1\,\mathrm{pN}$), kinesin wins; dynein–dynactin complexes with activating adaptors stall at $4$–$5\,\mathrm{pN}$ and two dyneins on one dynactin compete on more equal terms (Belyy and colleagues, 2016). In some cargoes the motors are coordinated by regulators rather than by mechanics alone; the model is the null hypothesis that experiments test.

![The tug-of-war model (Definition 27.6.1; Gillespie simulation). Both teams have the parameters of kinesin-1 (stall force 6 pN, detachment force 3 pN, unbinding 1 s⁻¹, binding 5 s⁻¹, forward velocity 1 µm/s, backward velocity 6 nm/s) and differ only in direction. A: a cargo with six motors of each kind moves in long runs alternately toward the plus and the minus end, with brief pauses: once one team starts to lose motors, the load on the remaining ones rises and they detach too. B: time-weighted distribution of the cargo velocity over 2000 s for 6 + 6, 7 + 6 and 6 + 7 motors (logarithmic axis): the cargo is almost always moving at full speed in one direction, and one extra motor shifts the mean velocity from 30 nm/s to about ±650 nm/s](./plots/tug-of-war.py)

### 27.6.3. Coordination in Muscle and Cilia

The $10^{14}$ heads of a muscle must satisfy three conditions. They must all pull in the same direction, which the sarcomere guarantees geometrically: thin filaments are anchored with their plus ends at the Z disc, and thick filaments are bipolar (**sarcomere**, [7.3.13](/7.3.13#sec-13.5.3)). They must pull at the same time, which calcium release triggered by an action potential ensures within milliseconds throughout a fiber, by moving tropomyosin off the myosin-binding sites. And they must not hinder each other, which their low duty ratio ensures: a head in skeletal muscle is strongly bound for a few percent of its cycle, so attached heads rarely resist the movement produced by others. Processive motors such as myosin V and kinesin, by contrast, keep each head bound for more than half its cycle and coordinate the two heads through the strain between them.

In cilia and flagella, dyneins attached to one microtubule doublet walk on the next; because the doublets are linked by nexin and anchored at the base, sliding becomes bending ([7.3.14](/7.3.14#sec-14.6.2)), and the beat emerges from the coupling of motor kinetics with the elasticity of the axoneme. A minimal model shows that a team of motors working against an elastic element becomes unstable and oscillates when the load-dependent detachment is strong enough (Jülicher and Prost, 1997): spontaneous oscillation is a generic property of motor ensembles, seen in insect flight muscle and in the hair bundles of the inner ear ([7.6.31](/7.6.31)).

## 27.7. Muscle: From Cross-Bridges to the Force–Velocity Curve

### 27.7.1. Hill's Force–Velocity Relation

Before the molecular players were known, A. V. Hill (1938) measured the heat and work of frog muscle shortening against different loads and found a simple relation.

**Definition 27.7.1 (Hill's Force–Velocity Relation)** *Hill's force–velocity relation* states that a tetanized muscle shortening at velocity $v$ against a load $F$ obeys

$$
(F + a)(v + b) = (F_0 + a)\,b, \qquad v = b\,\frac{F_0 - F}{F + a}, \tag{27.14}
$$
where $F_0$ is the isometric force, $v_{\max} = bF_0/a$ the unloaded shortening velocity, and the constants $a$ and $b$, with $a/F_0 \approx 0.2$–$0.3$ for most vertebrate skeletal muscles, describe the curvature.

The power $Fv$ is largest at $F \approx 0.3F_0$ and $v \approx 0.3v_{\max}$ for $a/F_0 = 0.25$, at about $0.1F_0v_{\max}$; cyclists choose their gears, and the muscles of fish swimming steadily their fiber types, to work near this optimum. Hill interpreted $a$ as a heat coefficient: a shortening muscle liberates extra heat in proportion to the distance shortened (the Fenn effect, Fenn 1923). A muscle stretched while active ($v < 0$) resists with forces up to about $1.8F_0$, beyond the hyperbola, while consuming little ATP: the cross-bridges are pulled off rather than cycling.

### 27.7.2. Huxley's Cross-Bridge Model

A. F. Huxley (1957) explained Hill's relation before the cross-bridge cycle was known biochemically, with a model that is still the template for ensemble models of motors.

**Definition 27.7.2 (Cross-Bridge Model)** In Huxley's *cross-bridge model*, independent myosin heads (cross-bridges) next to an actin filament are characterized by the distance $x$ of the nearest binding site from the head's unstrained position. A head attaches with rate $f(x)$ and detaches with rate $g(x)$; an attached head exerts the elastic force $kx$. Huxley took $f = f_1x/h$ for $0 \le x \le h$ and zero otherwise, $g = g_1x/h$ for $x \ge 0$ and a large constant $g_2$ for $x < 0$, so that heads attach only with positive (pulling) strain and are quickly removed once shortening has driven them to negative strain, with one ATP split per cycle.

If the filaments slide at velocity $v$, attached heads are carried toward smaller $x$, $\mathrm{d}x/\mathrm{d}t = -v$, and the fraction $n(x)$ of attached heads in steady state obeys

$$
-v\frac{\mathrm{d}n}{\mathrm{d}x} = f(x)[1 - n(x)] - g(x)n(x), \qquad n(x > h) = 0. \tag{27.15}
$$

**Formula 27.7.1 (Huxley's Force–Velocity Relation)** The solution of Eq. (27.15) gives the tension $F = \rho k\int xn(x)\,\mathrm{d}x$ ($\rho$ the density of heads per unit length of $x$),

$$
\frac{F}{F_0} = 1 - \frac{v}{\phi}\left(1 - \mathrm{e}^{-\phi/v}\right)\left[1 + \frac12\left(\frac{f_1 + g_1}{g_2}\right)^2\frac{v}{\phi}\right], \qquad \phi = \frac{(f_1 + g_1)h}{2}, \quad F_0 = \frac{\rho kh^2}{2}\,\frac{f_1}{f_1 + g_1}, \tag{27.16}
$$
and the rate of ATP splitting per head $\int f(x)[1 - n(x)]\,\mathrm{d}x$, which increases with $v$.

The mechanism of the curve is visible in $n(x)$. At rest, heads attach in $0 < x < h$ until $n = f_1/(f_1 + g_1)$ and pull with mean strain $h/2$. During shortening, heads are swept toward $x = 0$ before they have all attached, so fewer heads are attached and with less strain; heads carried past $x = 0$ resist until they detach at rate $g_2$, and at $v_{\max}$ their negative force cancels the positive force of the others. The energy liberated rises with velocity because more attachment sites pass through the zone where heads attach. With Huxley's choice $g_1/f_1 = 3/13$ and $g_2/(f_1 + g_1) = 3.9$, the curve is close to a hyperbola with $a/F_0 \approx 0.16$ (Figure B); other choices give $0.25$.

![Huxley's 1957 cross-bridge model (Definition 27.7.2, with g₁/f₁ = 3/13 and g₂/(f₁ + g₁) = 3.919; x in units of the attachment range h). A: steady-state fraction of attached heads n(x) at four shortening velocities (units of φ = (f₁ + g₁)h/2): at rest heads attach throughout the attachment zone; when shortening is fast, fewer heads attach, with less strain, and heads swept to negative x resist. B: the force–velocity relation of the model (Formula 27.7.1) with the best-fitting Hill hyperbola (a/F₀ = 0.16) and the mechanical power, maximal near 0.3F₀. C: the rate of ATP splitting rises with shortening velocity, about fivefold at v_max: the Fenn effect](./plots/huxley-model.py)

The model predicts the steady-state mechanics and energetics of muscle from two rate functions, an achievement that made muscle the first molecular machine with a quantitative theory. Its limitations pointed to the next discoveries. Huxley and Simmons (1971) found that after a quick release a fiber recovers part of its tension within milliseconds, much faster than attachment and detachment: an attached head has at least two bound states, before and after the power stroke, with a strain-dependent equilibrium between them, which is the two-state, load-dependent step of Section 27.3. The 1957 model also predicts that ATP use keeps rising up to $v_{\max}$, while real muscle's energy liberation peaks at intermediate velocities and falls; heads that detach before completing their cycle without splitting ATP, a form of loose coupling, explain the difference. Modern models combine the strain-dependent kinetics of Huxley with the cross-bridge cycle of [7.3.13](/7.3.13#sec-13.5.2) and the cooperative activation of the thin filament by calcium; the physiology of whole muscle, the length–tension relation and heart muscle belong to [7.14](/7.14), and muscle development to [7.5.24](/7.5.24).

### 27.7.3. From Molecules to Muscle

Scaling from one head to a muscle requires only geometry. A sarcomere of length $2.2\,\mu\mathrm{m}$ shortens by twice the filament sliding velocity, since both halves slide; a fiber of length $L$ contains $L/2.2\,\mu\mathrm{m}$ sarcomeres in series, so its shortening velocity in fiber lengths per second is the sliding velocity divided by $1.1\,\mu\mathrm{m}$. A sliding velocity of $6\,\mu\mathrm{m\,s^{-1}}$ (skeletal myosin II in a gliding assay) gives $v_{\max} \approx 5$ lengths per second, as for fast mammalian muscle. The force per cross-section, about $3\times10^5\,\mathrm{N\,m^{-2}}$, is independent of the size of the animal, because it is set by the density of thick filaments and the force per head (Example 27.1.2). Hence the scaling laws of animal locomotion: the force of a muscle grows with its cross-section, the speed with its length, and the power with its volume. Muscles of different speed differ in the myosin isoform they express, whose ADP release rate sets the detachment rate $g$ and hence $v_{\max}$.

## Summary

| Topic | Key relations and results |
|---|---|
| Energy scale (27.1) | $k_{\mathrm{B}}T = 4.1\,\mathrm{pN\,nm}$; ATP $\approx 20$–$25\,k_{\mathrm{B}}T$; $F_{\max} = \Delta\mu/d$ (Formula 27.1.1): kinesin $\le 10\,\mathrm{pN}$, myosin V $\le 3\,\mathrm{pN}$, φ29 about $57\,\mathrm{pN}$; about $1\,\mathrm{pN}$ per head in a biceps (Example 27.1.2) |
| Ratchets (27.2) | Feynman ratchet (Definition 27.2.1); no current at equilibrium in any periodic potential (Theorem 27.2.1); flashing ratchet drift (Definition 27.2.2, Formula 27.2.1); elastic power stroke $\langle F\rangle = \kappa\delta/2$ (Formula 27.2.2) |
| One-state model (27.3) | $V = a(k_+ - k_-)$, $D = \frac{a^2}{2}(k_+ + k_-)$ (Formula 27.3.1); $k_+/k_- = \mathrm{e}^{(\Delta\mu - Fa)/k_{\mathrm{B}}T}$, stall at $\Delta\mu/a$ (Theorem 27.3.1); shape of $V(F)$ set by the load distribution $\theta$ (Formula 27.3.2) |
| Internal states | two-state $V$ and $D$ (Theorem 27.3.2); Michaelis–Menten in ATP; three-state kinesin model with load on ATP binding, forward and backward commitments (Formula 27.3.4, Example 27.3.1) |
| Fluctuations (27.4) | dwell of two steps $\frac{k_1k_2}{k_2-k_1}(\mathrm{e}^{-k_1t} - \mathrm{e}^{-k_2t})$ (Formula 27.4.1); $n_{\min} = \langle\tau\rangle^2/\operatorname{Var}\tau \le n$ (Theorem 27.4.1); randomness $r = 2D/Va$ (Definition 27.4.1), $r = 1/n$ for $n$ equal steps, $\coth[(\Delta\mu - Fa)/2k_{\mathrm{B}}T]$ for one state; kinesin $r \approx 1/2$ (Example 27.4.1) |
| Coupling and efficiency (27.5) | tight coupling (Definition 27.5.1) vs ATP-consuming back steps; $\eta = FV/\Delta\mu J_{\mathrm{ATP}}$ (Formula 27.5.1); $\eta \le [1 + Vk_{\mathrm{B}}T/DF]^{-1}$ (Formula 27.5.2) |
| Teams (27.6) | load sharing $v = v_0(1 - F/NF_{\mathrm{s}})$ (Formula 27.6.1); tug of war (Definition 27.6.1, Formula 27.6.2): instability, saltatory bidirectional runs, switching by team size |
| Muscle (27.7) | Hill $(F + a)(v + b) = (F_0 + a)b$ (Definition 27.7.1); Huxley's cross-bridge model (Definition 27.7.2, Formula 27.7.1): hyperbolic $F$–$v$, Fenn effect; force scales with cross-section, speed with length |

## Questions

1. A vesicle with $D = 0.02\,\mu\mathrm{m^2\,s^{-1}}$ must travel $50\,\mu\mathrm{m}$ from the Golgi to the plasma membrane. Compare the transport times by diffusion and by kinesin-1 at $0.8\,\mu\mathrm{m\,s^{-1}}$, and find the distance at which both take the same time.

   **Answer** Diffusion in one dimension: $t = L^2/2D = 2500/0.04\,\mathrm{s} \approx 6\times10^4\,\mathrm{s}$, about 17 hours (in three dimensions to a shell at that distance, $L^2/6D$, about 6 hours). Kinesin: $50/0.8 \approx 60\,\mathrm{s}$. The times are equal at $L^* = 2D/v = 0.04/0.8\,\mu\mathrm{m} = 50\,\mathrm{nm}$; beyond about the size of the vesicle itself, the motor wins.

2. The φ29 packaging motor translocates $2.5\,\mathrm{bp}$ of DNA per ATP and stalls at $57\,\mathrm{pN}$. What fraction of the free energy of ATP ($\Delta\mu \approx 20\,k_{\mathrm{B}}T$) does it convert into work at stall? Could a motor with the same step stall at $150\,\mathrm{pN}$?

   **Answer** $d = 2.5 \times 0.34\,\mathrm{nm} = 0.85\,\mathrm{nm}$; $F_{\mathrm{s}}d = 48\,\mathrm{pN\,nm}$, about $59\,\%$ of $82\,\mathrm{pN\,nm}$. A stall at $150\,\mathrm{pN}$ would require $128\,\mathrm{pN\,nm} \approx 31\,k_{\mathrm{B}}T$ per ATP, more than one ATP supplies under any physiological conditions: impossible with one step per ATP (Formula 27.1.1), unless the motor hydrolysed more than one ATP per $2.5\,\mathrm{bp}$.

3. Show from Theorem 27.2.1 that a particle in a periodic potential tilted by a constant force $F$ does drift, and find its velocity when $U$ is constant. Why is the tilted ratchet not a perpetuum mobile?

   **Answer** With $V(x) = U(x) - Fx$, the stationary condition becomes $(\mathrm{e}^{\beta V}p)' = -(J/D)\mathrm{e}^{\beta V}$; integrating over a period, the boundary term no longer vanishes because $\mathrm{e}^{\beta V(L)} = \mathrm{e}^{\beta V(0)}\mathrm{e}^{-\beta FL} \ne \mathrm{e}^{\beta V(0)}$, so $J \ne 0$. For constant $U$ the current is the drift $p F/\gamma$, $v = F/\gamma = DF/k_{\mathrm{B}}T$ by the **Einstein–Smoluchowski relation**. The force does work $Fv$ that is dissipated as heat; nothing is extracted from the bath.

4. A one-state motor with $a = 8\,\mathrm{nm}$ moves at $V = 400\,\mathrm{nm\,s^{-1}}$ with $D = 2000\,\mathrm{nm^2\,s^{-1}}$. Find $k_+$, $k_-$ and the free energy dissipated per step, and compare with the randomness of kinesin at saturating ATP.

   **Answer** $k_+ - k_- = V/a = 50\,\mathrm{s^{-1}}$, $k_+ + k_- = 2D/a^2 = 62.5\,\mathrm{s^{-1}}$, so $k_+ = 56.25$, $k_- = 6.25\,\mathrm{s^{-1}}$. Dissipation per step $k_{\mathrm{B}}T\ln(k_+/k_-) = k_{\mathrm{B}}T\ln9 = 2.2\,k_{\mathrm{B}}T$. Its randomness $r = 2D/Va = 1.25$ is above one, because of backward steps; kinesin's $r \approx 0.5$ cannot come from a one-state motor at all and shows internal states.

5. In the two-state model, set $w_0 = w_1 = 0$ and $u_0 = k_{\mathrm{on}}[\mathrm{ATP}]$. Show that the randomness is $r = (u_0^2 + u_1^2)/(u_0 + u_1)^2$ and find its minimum. What would a measured $r = 0.33$ imply?

   **Answer** From Theorem 27.3.2, $2D/a^2 = [u_0u_1 - 2u_0^2u_1^2/\Sigma^2]/\Sigma$ and $V/a = u_0u_1/\Sigma$ with $\Sigma = u_0 + u_1$, so $r = 1 - 2u_0u_1/\Sigma^2 = (u_0^2 + u_1^2)/\Sigma^2$, the result of Theorem 27.4.1 for two steps. It is minimal, $1/2$, at $u_0 = u_1$, i.e. at $[\mathrm{ATP}] = u_1/k_{\mathrm{on}} = K_{\mathrm{M}}$. A value of $0.33$ implies at least three comparable irreversible transitions per step ($n_{\min} = 3$), as in the kinesin model at intermediate ATP.

6. Myosin V dwell times at $10\,\mu\mathrm{M}$ ATP have mean $80\,\mathrm{ms}$ and standard deviation $60\,\mathrm{ms}$. Estimate the number of rate-limiting steps and, assuming two steps with one ATP-dependent rate $k_{\mathrm{on}}[\mathrm{ATP}]$, their rates. How should the distribution change at $1\,\mathrm{mM}$ ATP?

   **Answer** $n_{\min} = 80^2/60^2 = 1.8$: at least two steps. Solve $1/k_1 + 1/k_2 = 0.080\,\mathrm{s}$, $1/k_1^2 + 1/k_2^2 = 0.0036\,\mathrm{s^2}$: with $s = 0.080$ and $q = 1/(k_1k_2)$, $s^2 - 2q = 0.0036$, $q = 0.0014$; $1/k$ are roots of $y^2 - 0.08y + 0.0014 = 0$, $y = 0.054$ and $0.026\,\mathrm{s}$, so rates of about $18.5$ and $38\,\mathrm{s^{-1}}$. If the ATP-dependent rate is $38\,\mathrm{s^{-1}}$ at $10\,\mu\mathrm{M}$ ($k_{\mathrm{on}} \approx 3.8\,\mu\mathrm{M^{-1}\,s^{-1}}$), at $1\,\mathrm{mM}$ it becomes $3800\,\mathrm{s^{-1}}$, negligible, and the dwells become exponential with mean $1/18.5 \approx 54\,\mathrm{ms}$, set by ADP release ($r \to 1$). If instead $18.5\,\mathrm{s^{-1}}$ were the ATP-dependent rate, the high-ATP dwell would be $26\,\mathrm{ms}$; the ATP titration decides.

7. (Experiment design) How would you test whether a newly discovered motor is tightly coupled? Describe two independent measurements.

   **Answer** (i) Measure ATP turnover and velocity in the same conditions: in a single-molecule assay, count steps against ATP consumed (for example, the ATPase rate of motors at known surface density in a gliding assay, or the ATP dependence of the dwell times, which for tight coupling has $K_{\mathrm{M}}$ and turnover consistent with one ATP per step at all loads). The ratio of steps to ATP must be one and independent of load. (ii) Measure the stall force at different values of $\Delta\mu$, varying ADP and $\mathrm{P_i}$: a tightly coupled motor stalls at $F_{\mathrm{s}} = \Delta\mu/a$, so $F_{\mathrm{s}}a$ should track $k_{\mathrm{B}}T\ln([\mathrm{ATP}]/[\mathrm{ADP}][\mathrm{P_i}])$ with slope one, and beyond stall it should synthesize ATP. A stall force that does not depend on $\Delta\mu$ or on [ATP], as for kinesin, indicates a kinetic stall and loose coupling.

8. Using Formula 27.6.2, find the velocity of a cargo pulled by three kinesins ($F_{\mathrm{s}} = 6\,\mathrm{pN}$, $v_{\mathrm{F}} = 1\,\mu\mathrm{m\,s^{-1}}$) against two dyneins ($F_{\mathrm{s}} = 1.1\,\mathrm{pN}$, $v_{\mathrm{B}} = 72\,\mathrm{nm\,s^{-1}}$), and the load on each motor. Why does the load-dependent unbinding make such a state short-lived?

   **Answer** $n_+F_{\mathrm{s}+} = 18$, $n_-F_{\mathrm{s}-} = 2.2\,\mathrm{pN}$; $v_{\mathrm{c}} = 15.8/(18/1 + 2.2/0.072)\,\mu\mathrm{m\,s^{-1}} = 15.8/48.6 = 0.33\,\mu\mathrm{m\,s^{-1}}$. $F_{\mathrm{c}} = 18(1 - 0.33) = 12.1\,\mathrm{pN}$: $4.0\,\mathrm{pN}$ per kinesin and $6.1\,\mathrm{pN}$ per dynein, about 5.5 times its stall force. With $F_{\mathrm{d}} = 0.75\,\mathrm{pN}$ each dynein detaches at $0.27\,\mathrm{e}^{8.1} \approx 900\,\mathrm{s^{-1}}$, within about a millisecond; the second dynein then carries all the load and detaches even faster, and the cargo runs plus-ward at $1\,\mu\mathrm{m\,s^{-1}}$.

9. Derive the isometric tension of Huxley's model (Formula 27.7.1 at $v = 0$) and explain why, in the model, the unloaded shortening velocity $v_{\max}$ is set mainly by $g_2$.

   **Answer** At $v = 0$, Eq. (27.15) gives $n = f/(f + g) = f_1/(f_1 + g_1)$ for $0 < x < h$ and zero elsewhere, so $F_0 = \rho k\int_0^hx\,\mathrm{d}x\,f_1/(f_1 + g_1) = \rho kh^2f_1/[2(f_1 + g_1)]$. At $v_{\max}$ the positive force of heads in $0 < x < h$ is cancelled by heads dragged to $x < 0$, which survive over a distance about $v/g_2$ and pull with force $\propto -x$; a larger $g_2$ removes them sooner, so the cancellation requires a higher velocity. Physiologically $g_2$ corresponds to the rate of ADP release and ATP-induced detachment, which is the step that differs between fast and slow myosin isoforms.

10. Using Hill's equation with $a/F_0 = 0.25$, find the load at which the power is maximal and the maximal power in units of $F_0v_{\max}$. A muscle of $100\,\mathrm{g}$ with $F_0$ per cross-section $3\times10^5\,\mathrm{N\,m^{-2}}$, fiber length $10\,\mathrm{cm}$ and $v_{\max} = 5$ lengths per second: estimate its peak power.

    **Answer** With $u = F/F_0$, $v/v_{\max} = 0.25(1 - u)/(u + 0.25)$ and the power $p(u) = 0.25u(1 - u)/(u + 0.25)$. Setting $p' = 0$: $(1 - 2u)(u + 0.25) = u(1 - u)$, i.e. $u^2 + 0.5u - 0.25 = 0$, $u = 0.309$; then $v/v_{\max} = 0.309$ and $p = 0.095$. The muscle's volume is $10^{-4}\,\mathrm{m^3}$ (density $10^3\,\mathrm{kg\,m^{-3}}$), its cross-section $10^{-3}\,\mathrm{m^2}$, so $F_0 = 300\,\mathrm{N}$ and $v_{\max} = 0.5\,\mathrm{m\,s^{-1}}$; peak power $\approx 0.095\times300\times0.5 \approx 14\,\mathrm{W}$, about $140\,\mathrm{W\,kg^{-1}}$, typical of mammalian skeletal muscle.

11. (Open problem) Kinesin's stall force does not depend on [ATP], but the stall force of a tightly coupled motor should. Design a numerical experiment with Formula 27.3.4 and a tightly coupled two-state model to show the difference, and propose what an optical-trap experiment would measure.

    **Answer** Approach: compute $V(F)$ from Formula 27.3.4 at several [ATP] and find its zero: $F_{\mathrm{s}} = (k_{\mathrm{B}}T/(d_1 + d_{\mathrm{b}}))\ln(k_1^0/k_{\mathrm{b}}^0)$ for all [ATP]. For a tightly coupled two-state model, impose $u_0u_1/(w_0w_1) = \exp[(\Delta\mu - Fa)/k_{\mathrm{B}}T]$ with $\Delta\mu$ from Eq. (27.4); its stall shifts by $(k_{\mathrm{B}}T/a)\ln 10 \approx 1.15\,\mathrm{pN}$ per decade of [ATP] for $a = 8.2\,\mathrm{nm}$. In the trap one measures the stall force (or the force at which forward and backward step frequencies are equal) at [ATP] from $10\,\mu\mathrm{M}$ to $1\,\mathrm{mM}$ and at added ADP or $\mathrm{P_i}$; one also counts whether back steps are accompanied by ATP consumption, for example by their dependence on [ATP]. Kinesin shows ATP-independent stall and ATP-dependent back-step rates, the signature of the loose coupling in the model.
