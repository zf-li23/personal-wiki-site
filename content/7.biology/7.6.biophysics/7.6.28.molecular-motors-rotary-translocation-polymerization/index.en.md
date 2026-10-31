---
title: "Molecular Motors II: Rotary Motors, Translocation and Polymerization Motors"
description: "Motors that rotate, thread polymers through holes, or push and pull by growing and shrinking. Rotary motors: the torque bound, measuring rotation; F₁-ATPase with its 120° steps, 80°/40° substeps and near-perfect efficiency measured by drag and by the fluctuation theorem; the torque balance of Fₒ and F₁ that decides between synthesis and hydrolysis; the bacterial flagellar motor and a kinetic model of its torque–speed curve. Translocation motors: the translocation ratchet and its force–velocity relation, chaperone binding and finite stall, protein import and unfolding machines, the φ29 packaging motor, RNA polymerase and helicases; how the position of the load-dependent step shapes force–velocity curves. Polymerization and depolymerization as motors: thermodynamic stall forces, buckling, the two kinetic regimes, kinetochore coupling, and centering by pushing and pulling."
---

The motors of [7.6.27](/7.6.27) walk along linear tracks. The same physics, a stochastic cycle of internal states, coupled to a mechanical coordinate and driven out of equilibrium by a chemical potential difference, also describes machines that look nothing like walkers. Bend the track into a circle and the step becomes a rotation: F₁-ATPase and the bacterial flagellar motor turn by fixed angles per molecule of fuel, and their output is a torque. Thread a polymer through a pore and let something on the far side prevent it from sliding back, and diffusion becomes directed translocation. Let a filament grow against a membrane, or shrink while something holds on to its end, and polymerization itself becomes a motor. This chapter treats these three classes quantitatively: the torques and efficiency of ATP synthase, the torque–speed curve of the flagellar motor, the translocation ratchet, the force–velocity relations of DNA-packaging and nucleic-acid motors, and the forces of growing and shrinking filaments, including the centering of asters in cells.

The tools are those of [7.6.27](/7.6.27): Formula 27.1.1 for the thermodynamic bound, generalized detailed balance (Theorem 27.3.1), the two-state model (Theorem 27.3.2) and dwell-time analysis (Section 27.4), together with the **first-passage time** and the Smoluchowski equation of [7.6.5](/7.6.5). The biochemistry of ATP synthase, its binding-change mechanism and rotational catalysis are in [7.1.23](/7.1.23); the **proton-motive force** and the stoichiometry of protons per ATP in [7.6.3](/7.6.3#sec-3.4); the structure of the flagellum in [7.3.14](/7.3.14#sec-14.6.5), and the hydrodynamics of the flagellar motor's load, how its torque is measured with beads, in [7.6.22](/7.6.22#sec-22.5.5). The forces against which the φ29 motor packages DNA are computed in [7.6.21](/7.6.21#sec-21.7.2); the polymerization forces of single filaments, Euler buckling, the Brownian and elastic Brownian ratchets and load sharing in [7.6.26](/7.6.26#sec-26.5); the cell biology of the cytoskeleton in [7.3.13](/7.3.13) and [7.3.14](/7.3.14). The use of the flagellar motor's switching in chemotaxis is the subject of [7.6.35](/7.6.35).

## 28.1. Rotary Motors

### 28.1.1. From Tracks to Rings

A rotary motor has an angular coordinate $\theta$ instead of a position, steps $\Delta\theta$ instead of $a$, and a torque $\tau$ instead of a force; its velocity is the angular velocity $\omega$, often given as a rotation rate in revolutions per second. All results of the position–state description carry over with $Fa \to \tau\Delta\theta$.

**Formula 28.1.1 (Torque Bound)** A rotary motor that turns by $\Delta\theta$ per fuel molecule, with free energy $\Delta\mu$ per molecule, cannot rotate forward against a torque larger than

$$
\tau_{\max} = \frac{\Delta\mu}{\Delta\theta}, \tag{28.1}
$$
and if it is tightly coupled its rates satisfy $k_+/k_- = \exp[(\Delta\mu - \tau\Delta\theta)/k_{\mathrm{B}}T]$, so that it stalls at $\tau_{\max}$ and turns backward, using the load to drive its chemistry in reverse, beyond it.

For F₁, $\Delta\theta = 2\pi/3$ per ATP and $\Delta\mu \approx 20\,k_{\mathrm{B}}T = 82\,\mathrm{pN\,nm}$ give $\tau_{\max} \approx 39\,\mathrm{pN\,nm}$. For a membrane rotor driven by ions, $\Delta\mu$ per ion is $e\Delta p$ (for protons, the **proton-motive force** times the elementary charge; $\Delta p = 150\,\mathrm{mV}$ gives $24\,\mathrm{pN\,nm}$, $5.8\,k_{\mathrm{B}}T$).

### 28.1.2. Watching Rotation

Rotation of molecules a few nanometers across is made visible by attaching something large. In tethered-cell experiments (Silverman and Simon, 1974) a bacterium stuck to glass by a single flagellar stub rotates its whole body, about $10\,\mathrm{Hz}$; beads of different sizes attached to flagellar stubs probe the motor at different loads (Chen and Berg, 2000). For F₁, a fluorescent actin filament attached to the γ subunit of a surface-immobilized $\alpha_3\beta_3\gamma$ complex (Noji, Yasuda, Yoshida and Kinosita, 1997), or a gold nanoparticle imaged by laser dark-field microscopy at tens of kilohertz (Yasuda and colleagues, 2001), reports the angle. In all these experiments the probe's viscous drag is the load: the rotational drag coefficient $\zeta$ of a bead or filament is known from hydrodynamics, the torque is $\zeta\omega$, and changing the probe changes the load ([7.6.22](/7.6.22#sec-22.4.4)). Magnetic beads in rotating magnetic fields (**magnetic tweezers**, [7.6.17](/7.6.17#sec-17.3)) impose rotation from outside and so drive a motor backward.

## 28.2. F₁-ATPase

### 28.2.1. Steps and Substeps

At low ATP, the γ subunit of F₁ rotates counterclockwise (viewed from the membrane side) in discrete $120°$ steps, one per ATP hydrolyzed, consistent with the three catalytic sites of the binding-change mechanism ([7.1.23](/7.1.23#sec-23.3.3)). With small gold beads the steps resolve into two substeps of about $80°$ and $40°$ (Yasuda and colleagues, 2001). The dwell before the $80°$ substep shortens in inverse proportion to [ATP]: it is the wait for ATP binding. The dwell before the $40°$ substep does not depend on [ATP] and contains two sequential events of about $1\,\mathrm{ms}$ each, hydrolysis of ATP bound earlier and release of phosphate; ADP is released during the binding dwell of a later step.

**Formula 28.2.1 (Rotation Rate of F₁)** With ATP binding at $k_{\mathrm{on}}[\mathrm{ATP}]$ and two ATP-independent catalytic events at rates $k_{\mathrm{h}}$ and $k_{\mathrm{p}}$ per $120°$ step, and a probe whose drag is negligible, the mean rotation rate is

$$
\nu = \frac{1}{3}\left(\frac{1}{k_{\mathrm{on}}[\mathrm{ATP}]} + \frac{1}{k_{\mathrm{h}}} + \frac{1}{k_{\mathrm{p}}}\right)^{-1} = \frac{\nu_{\max}[\mathrm{ATP}]}{K_{\mathrm{M}} + [\mathrm{ATP}]}, \qquad \nu_{\max} = \frac{1}{3(1/k_{\mathrm{h}} + 1/k_{\mathrm{p}})}, \quad K_{\mathrm{M}} = \frac{3\nu_{\max}}{k_{\mathrm{on}}}. \tag{28.2}
$$

With $k_{\mathrm{on}} \approx 3\times10^7\,\mathrm{M^{-1}\,s^{-1}}$, $k_{\mathrm{h}} \approx 1000\,\mathrm{s^{-1}}$ and $k_{\mathrm{p}} \approx 700\,\mathrm{s^{-1}}$, $\nu_{\max} \approx 140$ revolutions per second and $K_{\mathrm{M}} \approx 14\,\mu\mathrm{M}$, the values measured with $40\,\mathrm{nm}$ beads. The rise of the catalytic dwell distribution from zero (Formula 27.4.1 of [7.6.27](/7.6.27#sec-27.4.1)) is the evidence that it hides two events; that they are hydrolysis and phosphate release was shown with slowly hydrolyzed ATP analogs and mutants that slow one of them, and by imaging fluorescent nucleotides binding and leaving single F₁ molecules while they rotate (Adachi and colleagues, 2007).

![Simulated rotation of F₁-ATPase observed through a 40 nm gold bead (Formula 28.2.1; ATP binding at 3 × 10⁷ M⁻¹ s⁻¹, two catalytic events at 1000 and 700 s⁻¹, bead relaxation 0.1 ms, Brownian fluctuations 6°, sampling 20 kHz). A: angle against time at 2 µM, 20 µM and 2 mM ATP; at low ATP each 120° step splits into an 80° substep after the binding dwell (full lines at multiples of 120°) and a 40° substep after the catalytic dwell (dotted lines). B: dwell-time distributions at 2 µM ATP (logarithmic axis): the binding dwell is exponential with mean 1/(k_on[ATP]) ≈ 17 ms; the catalytic dwell, about 2.4 ms, rises from zero, the signature of two sequential events. C: rotation rate against [ATP]: Michaelis–Menten with ν_max ≈ 140 rev/s and K_M ≈ 14 µM for a small bead; a 1 µm actin filament, whose rotational drag at 40 pN nm limits the rate to about 6 rev/s, hides the kinetics at high ATP](./plots/f1-stepping.py)

### 28.2.2. Torque and Efficiency

With an actin filament of length $L$ as probe, the rotation rate falls as the filament's rotational drag grows, approximately as $L^{-3}$, and the product $\zeta\omega$ is constant, about $40\,\mathrm{pN\,nm}$ (Yasuda and colleagues, 1998): F₁ produces a constant torque whatever its speed in this range, and the work per step, $40 \times 2\pi/3 \approx 84\,\mathrm{pN\,nm}$, equals the free energy of ATP hydrolysis under the conditions of the experiment within the uncertainties ([7.6.22](/7.6.22#sec-22.4.4), Example 22.4.2). Drag-based torque estimates require the drag coefficient near a surface, which is uncertain by tens of percent. A method that needs no hydrodynamics uses the fluctuations of the probe.

**Formula 28.2.2 (Torque from the Fluctuation Theorem)** For a rotary motor in a nonequilibrium steady state, the probability of observing a rotation $\Delta\theta$ of the probe in a time $\Delta t$, compared with that of $-\Delta\theta$, satisfies for long enough $\Delta t$

$$
\ln\frac{P(\Delta\theta)}{P(-\Delta\theta)} = \frac{\tau\Delta\theta}{k_{\mathrm{B}}T}, \tag{28.3}
$$
where $\tau$ is the torque that the motor exerts on the probe; the slope of $\ln[P(\Delta\theta)/P(-\Delta\theta)]$ against $\Delta\theta$ measures $\tau$ in units of $k_{\mathrm{B}}T$, independently of the probe's drag.

The relation is a steady-state fluctuation theorem: the probe is a Brownian particle driven by the torque, and the entropy produced in the bath by a rotation $\Delta\theta$ is $\tau\Delta\theta/T$ (the **Crooks fluctuation theorem** of [7.6.17](/7.6.17#sec-17.6) is its counterpart for driven protocols; the general theory is in [7.6.38](/7.6.38)). Applied to F₁, it gives torques that, multiplied by $2\pi/3$, are about equal to the free energy of hydrolysis over a wide range of ATP, ADP and phosphate concentrations: F₁ converts nearly all of $\Delta\mu$ into work on the probe (Hayashi and colleagues, 2010). A related measurement of the heat dissipated by the motor's internal transitions, using the violation of the **fluctuation–dissipation theorem** by the probe (the Harada–Sasa relation), found almost no internal dissipation (Toyabe and colleagues, 2010). F₁ at stall is close to a reversible machine.

**Example 28.2.1 (The torque of one ATP)** Under the conditions of a typical F₁ assay, $[\mathrm{ATP}] = 2\,\mathrm{mM}$, $[\mathrm{ADP}] = 10\,\mu\mathrm{M}$ and $[\mathrm{P_i}] = 1\,\mathrm{mM}$, Eq. (27.4) with $\Delta\mu^\circ = 12.3\,k_{\mathrm{B}}T$ ($30.5\,\mathrm{kJ\,mol^{-1}}$ at $298\,\mathrm{K}$) gives $\Delta\mu = 12.3 + \ln[(2\times10^{-3})/(10^{-5}\times10^{-3})] = 12.3 + 12.2 = 24.5\,k_{\mathrm{B}}T = 100\,\mathrm{pN\,nm}$, and Formula 28.1.1 a maximal torque of $100/(2\pi/3) = 48\,\mathrm{pN\,nm}$. At $[\mathrm{ADP}] = 1\,\mathrm{mM}$ the bound falls to $(12.3 + 7.6)\,k_{\mathrm{B}}T/(2\pi/3) = 39\,\mathrm{pN\,nm}$. The measured torques follow these changes, which is evidence of tight coupling.

### 28.2.3. Running Backward: Mechanical Synthesis of ATP

A tightly coupled motor driven beyond stall must reverse its chemistry (Formula 28.1.1). Itoh and colleagues (2004) attached magnetic beads to the γ subunit of single F₁ molecules sealed in femtoliter chambers and rotated them clockwise with a rotating magnetic field: ATP accumulated in the chambers, about one ATP per $120°$ turn at best. Mechanical work alone, with no proton gradient and no $\mathrm{F_o}$, is enough to synthesize ATP. This is the clearest demonstration of the principle of detailed balance for a molecular machine: the same transitions run forward when chemistry drives mechanics and backward when mechanics drives chemistry. In the cell the driving torque comes from $\mathrm{F_o}$.

## 28.3. Fₒ and the Torque Balance of ATP Synthase

### 28.3.1. Torque from the Proton-Motive Force

The c ring of $\mathrm{F_o}$ ($n_c = 8$–$17$ subunits) turns by one subunit, $2\pi/n_c$, per proton passing from the P side to the N side ([7.1.23](/7.1.23#sec-23.3.4)). Applying Formula 28.1.1 to it, and noting that the c ring and γ form one rotor, gives the competition between the two motors of ATP synthase.

**Formula 28.3.1 (Torque Balance of ATP Synthase)** The maximal torques of $\mathrm{F_o}$ and $\mathrm{F_1}$ on their common rotor are

$$
\tau_{\mathrm{o}} = \frac{n_ce\Delta p}{2\pi}, \qquad \tau_1 = \frac{\Delta G_{\mathrm{p}}}{2\pi/3}, \tag{28.4}
$$
with $\Delta G_{\mathrm{p}}$ the free energy of ATP synthesis (the **phosphorylation potential** per molecule). The enzyme synthesizes ATP when $\tau_{\mathrm{o}} > \tau_1$, that is when $(n_c/3)\,e\Delta p > \Delta G_{\mathrm{p}}$, and hydrolyses ATP and pumps protons when $\tau_1 > \tau_{\mathrm{o}}$.

The condition is the thermodynamic requirement of $n_c/3$ protons per ATP ([7.6.3](/7.6.3#sec-3.4.3)), seen as a balance of torques. For animal mitochondria ($n_c = 8$) at $\Delta p = 200\,\mathrm{mV}$, $\tau_{\mathrm{o}} = 8\times32\,\mathrm{pN\,nm}/2\pi = 41\,\mathrm{pN\,nm}$, against $\tau_1 = 40$–$48\,\mathrm{pN\,nm}$ for $\Delta G_{\mathrm{p}} = 50$–$60\,\mathrm{kJ\,mol^{-1}}$: the two motors are almost balanced, and the enzyme works close to equilibrium, as it must to synthesize efficiently. Chloroplasts, with $n_c = 14$, make ATP at a lower proton-motive force. When $\Delta p$ collapses, in hypoxia or with uncouplers, F₁ wins and the enzyme hydrolyses ATP; mitochondria limit the loss with the inhibitor protein IF1 ([7.1.23](/7.1.23#sec-23.4.2)), and fermenting bacteria use the reverse mode deliberately, to maintain a proton-motive force from glycolytic ATP.

A widely used textbook estimate takes a $30°$ step per ion ($n_c = 12$), a fixed membrane potential of $90\,\mathrm{mV}$ and a variable pH difference, and concludes that ATP synthase of *E. coli* reverses when the pH difference falls below about $0.5$, as in alkaline media. The conclusion depends only on $\Delta p$ as a whole: in alkaline media *E. coli* keeps a pH difference near zero or even inverted but raises its membrane potential, so that $\Delta p$, about $140\,\mathrm{mV}$, and synthesis are maintained; and its c ring has ten subunits, not twelve.

![The torque balance of ATP synthase. A: schematic of FₒF₁ in the inner mitochondrial membrane (P side above, matrix below): protons passing through Fₒ turn the c ring and the central stalk with torque τₒ; ATP hydrolysis in F₁ turns them the other way with torque τ₁; the direction of rotation is set by the larger torque. B: τₒ = n_c eΔp/2π (Formula 28.3.1) against the proton-motive force for c rings of 8 (animal mitochondria), 10 (yeast mitochondria, *E. coli*) and 14 subunits (chloroplasts), and the band of τ₁ = ΔG_p/(2π/3) for phosphorylation potentials of 45–60 kJ/mol; where a line lies above the band, the synthase makes ATP. The c₈ enzyme of mitochondria operates near the crossing (shaded: typical mitochondrial Δp)](./plots/synthase-torques.py)

### 28.3.2. A Brownian Ratchet in the Membrane

How does a proton flux produce torque? The c-ring carboxylates face the lipid on most of their path and must be protonated (neutral) to do so; at the interface with subunit a they meet two offset half-channels, one open to the P side and one to the N side, separated by a conserved arginine. A carboxylate that rotates into the P-side half-channel picks up a proton from the acidic side; the ring can then rotate it into the lipid. After nearly a full turn it reaches the N-side half-channel, releases its proton into the alkaline matrix and is attracted by the arginine. Thermal rotation of the ring is permitted in the forward direction and blocked in the reverse direction, because a deprotonated carboxylate cannot enter the lipid and a protonated one cannot pass the arginine: a **Brownian ratchet** whose pawl is protonation (Junge, Lill and Engelbrecht, 1997; Elston, Wang and Oster, 1998). The proton-motive force biases the protonation states through the pH difference, and the membrane potential acts on the charges moving in the channels. Models of this kind reproduce the torque at stall and rotation rates of hundreds of hertz, limited by proton transfer rates. The same principle, with stator units that themselves rotate, drives the flagellar motor.

## 28.4. The Bacterial Flagellar Motor

### 28.4.1. Architecture and Numbers

The flagellar motor of *E. coli* is a ring-shaped rotor of about $45\,\mathrm{nm}$ in the cytoplasmic membrane, with a C ring of about 34 copies of FliG, FliM and FliN on its cytoplasmic face, surrounded by up to eleven stator units that are anchored to the peptidoglycan and conduct protons ([7.3.14](/7.3.14#sec-14.6.5)). Each stator unit is a MotA₅MotB₂ complex; cryo-EM structures (Santiveri and colleagues, 2020; Deme and colleagues, 2020) suggest that proton flow through MotB rotates the MotA pentamer, which engages FliG like a gear. Measurements give:

| Quantity | Value | Method |
|---|---|---|
| Stall torque | $1300$–$2000\,\mathrm{pN\,nm}$ (*E. coli*, full complement of stators) | tethered cells, electrorotation, large beads |
| Maximum speed | about $300\,\mathrm{Hz}$ (*E. coli*, $\ce{H+}$); up to $1700\,\mathrm{Hz}$ (*Vibrio*, $\ce{Na+}$) | small beads, gold particles |
| Steps | 26 per revolution, the periodicity of the FliG ring | bead tracking at very low speed (Sowa and colleagues, 2005) |
| Ion flux | about 1000 protons per revolution | proton flux in *Streptococcus* (Meister, Lowe and Berg, 1987) |
| Stator number | up to 11, dynamically exchanging | resurrection, fluorescence (Reid and colleagues, 2006; Leake and colleagues, 2006) |

In "resurrection" experiments, cells lacking functional stators are induced to make them, and the speed of a tethered cell rises in up to eleven equal increments as stator units are incorporated (Block and Berg, 1984): torque at high load is additive. The motor's free-energy budget at stall shows that it is efficient: $1000$ protons at $e\Delta p = 24\,\mathrm{pN\,nm}$ supply $2.4\times10^4\,\mathrm{pN\,nm}$ per revolution, while $2\pi\times1300\,\mathrm{pN\,nm} = 8\times10^3\,\mathrm{pN\,nm}$ of work per revolution is delivered, about one third. Because the measured flux has large uncertainties and was obtained in another species, efficiencies close to one at stall cannot be excluded, and the high-load torque is independent of temperature and of the substitution of $\ce{H2O}$ by $\ce{D2O}$ (Chen and Berg, 2000), as expected for a motor working near equilibrium with its energy source.

### 28.4.2. A Kinetic Model of the Torque–Speed Curve

The torque–speed curve of the motor ([7.6.22](/7.6.22#sec-22.5.5)) has two regimes: a nearly constant torque up to a knee near $170\,\mathrm{Hz}$ (room temperature), and a steep decline to zero torque at about $300\,\mathrm{Hz}$. The plateau is independent of temperature and isotope; the knee and the maximum speed are not. A two-state cycle per stator with one load-independent and one load-dependent transition reproduces both observations.

**Formula 28.4.1 (Two-State Stator Model)** Let each of $N$ stator units advance the rotor by $\delta = 2\pi/26$ per cycle of a proton-transfer transition (rate scale $k_{\mathrm{c}}$, releasing a fraction $1 - s$ of the free energy $\Delta\mu$ per step) and a power stroke (rate scale $k_{\mathrm{m}}$, releasing $s\Delta\mu - \tau\delta/N$ against its share of the load torque $\tau$). With each transition's free-energy change $\Delta g$ split symmetrically, $u = k\,\mathrm{e}^{\Delta g/2k_{\mathrm{B}}T}$, $w = k\,\mathrm{e}^{-\Delta g/2k_{\mathrm{B}}T}$, the rotation rate is

$$
\nu(\tau) = \frac{\delta}{2\pi}\,\frac{u_{\mathrm{c}}u_{\mathrm{m}}(\tau) - w_{\mathrm{c}}w_{\mathrm{m}}(\tau)}{u_{\mathrm{c}} + u_{\mathrm{m}}(\tau) + w_{\mathrm{c}} + w_{\mathrm{m}}(\tau)}, \tag{28.5}
$$
by Theorem 27.3.2, with stall at $\tau = N\Delta\mu/\delta$; the motor runs at the intersection of $\nu(\tau)$ with the load line $\tau = 2\pi\zeta\nu$.

When the power stroke is fast ($k_{\mathrm{m}} \gg k_{\mathrm{c}}$), the mechanical transition is in rapid equilibrium at high load; the speed is then set by how far the load pushes this equilibrium, the torque stays near its thermodynamic maximum over a wide range of speeds, and it does not depend on the rate of proton transfer: the plateau is thermodynamic. At low load the proton-transfer transition limits the cycle, the speed saturates at about $\delta k_{\mathrm{c}}/2\pi$ and the torque falls steeply: the knee and the maximum speed are kinetic, and they move when proton transfer is slowed by $\ce{D2O}$ or cooling. With the load shared among stators, the stall torque is proportional to $N$, while the zero-load speed, limited by the kinetics of each stator, does not depend on $N$, as observed in resurrection experiments at low load (Yuan and Berg, 2008). The model is minimal: its high-speed decline is steeper than the measured, almost linear fall, which requires elastic coupling between stators and rotor and the stochastic attachment of stators (Meacci and Tu, 2009), and later experiments found that the zero-load speed does increase with stator number under some conditions (Nord and colleagues, 2017).

![A kinetic model of the flagellar motor's torque–speed curve (Formula 28.4.1; N = 8 stators, 26 steps per revolution, Δμ = 48 pN nm per step, i.e. two protons at Δp = 150 mV, s = 0.85, k_m = 10⁵ s⁻¹, k_c = 3000 s⁻¹). A: torque against speed with the load lines of beads of 1, 0.5 and 0.3 µm diameter and a 60 nm gold particle (rotational drag 8πηr³ plus a contribution of the hook); large beads load the motor on its plateau, small particles probe the steep region. B: slowing proton transfer 1.6-fold, as with D₂O, moves the knee and the maximum speed but not the high-load torque. C: the torque for 1, 2, 4 and 8 stators: stall torque proportional to the number of stators, zero-load speed independent of it](./plots/flagellar-motor-model.py)

### 28.4.3. Switching and Remodeling

The motor of *E. coli* runs counterclockwise (seen from outside), forming a flagellar bundle that propels the cell, and switches to clockwise rotation, which breaks up the bundle and makes the cell tumble, when phosphorylated CheY binds the C ring. The switch is ultrasensitive, with a Hill coefficient of about ten in the CheY-P concentration (Cluzel, Surette and Leibler, 2000), and its stochastic switching between two states of a ring of FliM subunits has been modeled as a conformational spread in an Ising-like ring (Duke, Le Novère and Bray, 2001; Bai and colleagues, 2010); the role of switching in chemotaxis is the subject of [7.6.35](/7.6.35). The motor also adapts to its load: stator units bind more stably under high load, so the number of engaged stators rises when the cell swims through viscous media or is stuck to a surface (Lele, Hosu and Berg, 2013), a form of mechanosensing ([7.6.31](/7.6.31)).

## 28.5. Translocation Motors

### 28.5.1. Moving Polymers Through Holes

Unfolded proteins are imported into mitochondria through the TOM and TIM23 complexes, driven on the matrix side by mtHsp70 and its partners; proteins are translocated into the ER lumen through the **Sec61 translocon**, cotranslationally pushed by the ribosome or posttranslationally pulled by the Hsp70 BiP; substrates of the **proteasome**, of ClpXP and of other AAA+ unfoldases are pulled through a central pore of a hexameric ATPase ring and unfolded on the way; tailed phages pump their DNA into the capsid with ring ATPases, and some phages are pulled into the host by the host's **RNA polymerase** transcribing the entering DNA. Two mechanisms are possible: a Brownian ratchet, in which the polymer diffuses through the pore and binding on the far side prevents back-sliding, and a power stroke, in which a motor grips the polymer and pulls.

### 28.5.2. The Translocation Ratchet

**Definition 28.5.1 (Translocation Ratchet)** A *translocation ratchet* is a polymer that diffuses through a pore with diffusion coefficient $D$, carrying binding sites spaced $d$ apart; a protein on the far side binds each site as soon as it emerges and is too large to pass back through the pore, so that the polymer, once a site has crossed, cannot slide back past it.

Diffusion alone would take $t \approx (nd)^2/2D$ to move a polymer of $n$ sites through; with ratcheting, each site needs only to diffuse a distance $d$, and the total time is $n\,d^2/2D$: the speed-up is a factor $n$. A resisting force $F$ (an opposing electric field, the folding of the emerged part, an osmotic pressure) slows the ratchet.

**Theorem 28.5.1 (Velocity of a Perfect Translocation Ratchet)** For irreversible, instantaneous binding, the mean translocation velocity against a load $F$ is

$$
v = \frac{2D}{d}\,\frac{w^2/2}{\mathrm{e}^w - w - 1}, \qquad w = \frac{Fd}{k_{\mathrm{B}}T}, \tag{28.6}
$$
which equals the ideal ratchet velocity $2D/d$ at $F = 0$, decreases as $v \approx (2D/d)(1 - w/3)$ for small loads and as $(D/d)w^2\mathrm{e}^{-w}$ for large ones, and never vanishes.

**Proof** Let $x \in [0, d)$ be the position of the last bound site beyond the pore. Between bindings $x$ performs overdamped diffusion with drift $-F/\gamma = -DF/k_{\mathrm{B}}T$ (**Einstein–Smoluchowski relation**), with a reflecting boundary at $x = 0$ (the bound protein cannot enter the pore); when $x$ reaches $d$ the next site binds and the process restarts at $x = 0$. The mean time per step is the mean first-passage time from $0$ to $d$ in the potential $U(x) = Fx$, from Theorem 5.6.1 of [7.6.5](/7.6.5#sec-5.6.1):

$$
T = \frac1D\int_0^d\mathrm{d}y\,\mathrm{e}^{\beta Fy}\int_0^y\mathrm{e}^{-\beta Fz}\,\mathrm{d}z = \frac{1}{D\beta F}\int_0^d\left(\mathrm{e}^{\beta Fy} - 1\right)\mathrm{d}y = \frac{d^2}{D}\,\frac{\mathrm{e}^w - w - 1}{w^2}.
$$
The velocity is $v = d/T$, which is Eq. (28.6). Expanding $\mathrm{e}^w - w - 1 = w^2/2 + w^3/6 + \dots$ gives the limits. $\square$

A calculation of the steady-state probability current gives the same result; the first-passage formulation shows that the ratchet is the first-passage problem of a diffusing particle against a force. The polymerization ratchet of [7.6.26](/7.6.26#sec-26.5.2) is the same calculation with the monomer size $\delta$ in place of $d$ and the fluctuating gap between filament tip and load in place of $x$ (Peskin, Odell and Oster, 1993).

A perfect ratchet has no stall force, which is unphysical: binding is reversible. If the chaperones bind in rapid equilibrium, each exposed site contributes a binding free energy $k_{\mathrm{B}}T\ln(1 + c/K_{\mathrm{d}})$, where $c$ is the chaperone concentration and $K_{\mathrm{d}}$ its dissociation constant, so the polymer moves in a staircase potential $Fx - k_{\mathrm{B}}T\ln(1 + c/K_{\mathrm{d}})\lfloor x/d\rfloor$.

**Formula 28.5.1 (Stall of an Imperfect Ratchet)** With rapid, reversible binding the translocation ratchet stalls at

$$
F_{\mathrm{s}} = \frac{k_{\mathrm{B}}T}{d}\ln\left(1 + \frac{c}{K_{\mathrm{d}}}\right), \tag{28.7}
$$
the force at which the free energy gained by binding one more site equals the work against the load; its velocity, computed from the drift of a particle in a tilted periodic potential, approaches Eq. (28.6) for $c \gg K_{\mathrm{d}}$ and becomes negative beyond $F_{\mathrm{s}}$.

The free energy of binding is the fuel; the chaperone's ATP cycle, which keeps it in a high-affinity state while bound and recycles it afterwards, maintains $c/K_{\mathrm{d}}$ out of equilibrium.

![The translocation ratchet (units d, D and kBT). A: velocity against load w = Fd/kBT for the perfect ratchet (Theorem 28.5.1, line; Brownian-dynamics simulation of 2000 polymers, points) and for rapid reversible binding with c/K_d = 100, 10 and 1, computed as the drift of a particle in the tilted staircase potential; the reversible ratchets stall at w = ln(1 + c/K_d) (ticks, Formula 28.5.1) and run backward beyond. B: mean translocation time of a polymer with n binding sites: free diffusion (n²d²/2D) against the perfect ratchet (nd²/2D), a speed-up by the factor n](./plots/translocation-ratchet.py)

**Example 28.5.1 (Is diffusion fast enough for protein import?)** For an unfolded polypeptide in the TIM23 channel, take $D \approx 0.01\,\mu\mathrm{m^2\,s^{-1}}$ (a chain confined in a narrow pore, much slower than free diffusion) and binding sites for mtHsp70 about every 10 residues, $d \approx 3.5\,\mathrm{nm}$. The ideal ratchet velocity $2D/d \approx 2\times10^4/3.5\,\mathrm{nm\,s^{-1}} \approx 6\,\mu\mathrm{m\,s^{-1}}$, about $2\times10^4$ residues per second, is two to three orders of magnitude faster than observed import rates of tens to hundreds of residues per second. Diffusion through the pore does not limit import; the binding cycle of Hsp70 and above all the unfolding of folded domains outside the mitochondrion do. Unfolding a domain requires a force of several to tens of piconewtons applied at the pore, more than the stall force of Formula 28.5.1 for any plausible $c/K_{\mathrm{d}}$ and $d$ ($k_{\mathrm{B}}T\ln 100/3.5\,\mathrm{nm} \approx 5\,\mathrm{pN}$). This argument favors an active pulling role of mtHsp70, held at the channel by Tim44, at least for folded precursors; whether import is a ratchet, a power stroke, or a ratchet with entropic pulling (a bound Hsp70 restricts the chain's conformations near the membrane and so exerts an entropic force, De Los Rios and colleagues, 2006) remains debated, and the answer may differ between substrates.

### 28.5.3. Unfolding Machines

AAA+ unfoldases are hexameric rings whose pore loops grip a polypeptide and pull it into the central channel. Optical-trap experiments with ClpXP pulling on a protein tethered to a bead (Aubin-Tam and colleagues, 2011; Maillard and colleagues, 2011) show translocation in steps of about 1–4 nm, a few amino acids per ATP, at speeds of a few nanometers per second against loads up to about $20\,\mathrm{pN}$, and long dwells before the abrupt unfolding of each domain: unfolding is a thermally activated escape over a barrier tilted by the motor's pull, as in the Bell model (**Bell model**, [7.6.17](/7.6.17#sec-17.5)), and the motor may hydrolyze hundreds of ATP before a stable domain gives way. Cryo-EM structures of these rings and of the proteasome's Rpt subunits show a staircase of subunits around the substrate, each hydrolysis moving the bottom subunit to the top: a hand-over-hand mechanism around a ring. Unfolding machines are thus power-stroke motors, and their force–velocity relations, set by the barrier of the substrate rather than by the motor, depend on what they unfold.

### 28.5.4. The Packaging Motor of Phage φ29

The φ29 packaging motor, a pentamer of ASCE ATPases on the portal of the capsid, packages its $19.3\,\mathrm{kb}$ genome in a few minutes. Optical-tweezers measurements show:

- a speed of about $100$–$150\,\mathrm{bp\,s^{-1}}$ at low filling, decreasing as the capsid fills because the internal force rises ([7.6.21](/7.6.21#sec-21.7.2));
- a stall force of about $57\,\mathrm{pN}$ (Smith and colleagues, 2001), among the highest of any molecular motor, corresponding to $57 \times 0.85 = 48\,\mathrm{pN\,nm}$ per ATP, about $60\,\%$ of $\Delta\mu$;
- a dwell–burst cycle: dwells in which ATP binds to the subunits, followed by bursts of $10\,\mathrm{bp}$ composed of four substeps of $2.5\,\mathrm{bp}$ (Moffitt and colleagues, 2009). One subunit per cycle hydrolyzes ATP without translocating DNA and acts as a regulator (Chistol and colleagues, 2012), so that a cycle of five subunits moves $10\,\mathrm{bp}$, close to one turn of the double helix, consistent with the motor contacting the same face of the DNA each cycle;
- at high filling the burst size decreases: the motor adjusts its steps to the load.

A packaging time can be estimated by combining the motor's force–velocity relation $v(F)$ with the resisting force $F(L)$ of the inverse-spool model of [7.6.21](/7.6.21#sec-21.7.2): $t = \int_0^{L}\mathrm{d}L'/v(F(L'))$. At $120\,\mathrm{bp\,s^{-1}}$ with little resistance, the first two thirds of the genome take about two minutes; the last third, against tens of piconewtons, takes as long again, giving the observed total of about five minutes.

### 28.5.5. RNA Polymerase and Helicases

RNA polymerase moves along DNA in single-nucleotide steps of $0.34\,\mathrm{nm}$, resolved in optical traps with ångström precision (Abbondanzieri and colleagues, 2005). Its velocity is almost independent of an opposing force up to about $20\,\mathrm{pN}$ and it stalls at $25$–$30\,\mathrm{pN}$ (Wang and colleagues, 1998). In the two-state picture this shape means that the load acts on a fast transition in rapid equilibrium, the forward–backward sliding of the enzyme by one base pair, while the rate-limiting chemistry (NTP binding and incorporation) is load-independent: polymerase is a Brownian ratchet whose pawl is the incoming NTP, which can bind only in the forward-translocated state. The packaging motor shows the opposite shape: its speed falls gradually from the smallest loads, because the load acts on a slow, rate-limiting transition. Kinesin lies in between. One two-state model with the load placed on a fast or a slow transition reproduces all three shapes (Bustamante and colleagues, 2004).

![Where the load acts determines the shape of a motor's force–velocity curve. A tightly coupled two-transition cycle (Theorem 27.3.2 of 7.6.27) with a load-independent chemical transition (rate k_c) and a mechanical transition whose forward rate k_m exp(−Fd/kBT) carries the load; Δμ = 20 kBT. Velocity relative to its maximum against force relative to the force that halves the velocity. When the loaded transition is much faster than chemistry (k_m/k_c = 1000), it stays in rapid equilibrium and the velocity is flat until the load makes it limiting, then drops steeply (like RNA polymerase); when it is rate-limiting (k_m/k_c = 0.01), the velocity falls gradually from zero load (like the φ29 packaging motor); comparable rates give an intermediate curve (like kinesin)](./plots/force-velocity-shapes.py)

**Helicases** couple ATP hydrolysis to unwinding. A passive helicase moves only into base pairs that have opened by thermal fluctuation; if each base pair costs $\Delta G_{\mathrm{bp}}$ (about $1$–$3\,k_{\mathrm{B}}T$ depending on sequence) and closes rapidly, the fraction of time the next base pair is open is $\mathrm{e}^{-\Delta G_{\mathrm{bp}}/k_{\mathrm{B}}T}$, and the helicase is slowed by this factor relative to its speed on single strands. An active helicase destabilizes the fork with a potential of its own and approaches its single-strand speed (Betterton and Jülicher, 2005). Comparing the speed of a helicase on single-stranded DNA with its unwinding speed on duplexes of varying stability, or under a force that opens the fork, measures how active it is: some helicases are slowed severalfold by GC-rich DNA and accelerated by fork-opening forces (passive), others hardly at all (active).

## 28.6. Polymerization and Depolymerization Motors

### 28.6.1. Polymerization in the Motor Framework

A filament that grows against a barrier is a motor whose step is the elongation $\delta$ per added subunit and whose fuel is the free energy $k_{\mathrm{B}}T\ln(c/c_{\mathrm{c}})$ released per subunit at monomer concentration $c$ and critical concentration $c_{\mathrm{c}}$. Formula 27.1.1 then gives its stall force, $F_{\mathrm{s}} = (k_{\mathrm{B}}T/\delta)\ln(c/c_{\mathrm{c}})$; the kinetic theory of this motor, the Brownian and elastic Brownian ratchets and the sharing of loads among filaments, is developed in [7.6.26](/7.6.26#sec-26.5) and is not repeated here. In the language of this chapter and of [7.6.27](/7.6.27), three points stand out. First, the step is short, $2.7\,\mathrm{nm}$ for actin (two strands of $5.4\,\mathrm{nm}$ subunits) and $0.6\,\mathrm{nm}$ for a microtubule (13 protofilaments of $8\,\mathrm{nm}$ dimers), so stall forces of $7$ and $30\,\mathrm{pN}$ at $c/c_{\mathrm{c}} = 100$ are reached with modest free energies per subunit, as for the φ29 motor with its $0.85\,\mathrm{nm}$ step. Second, the polymerization ratchet is mathematically the translocation ratchet of Theorem 28.5.1 with $\delta$ in place of $d$ and the fluctuating gap between filament tip and load in place of the position of the last bound site; which of the two limits applies, addition of subunits or opening of the gap, decides the shape of the force–velocity curve, exactly as the position of the loaded transition does for the motors of Section 28.5.5. Third, the energy is supplied by keeping the monomer pool away from equilibrium with the polymer, through nucleotide exchange on free subunits and hydrolysis in the filament; a polymerization motor in a closed system at equilibrium ($c = c_{\mathrm{c}}$) cannot push, a direct application of Theorem 27.2.1.

### 28.6.2. Measured Polymerization Forces

Measurements confirm the order of magnitude but show that real filaments are not ideal motors. Single microtubules growing against a barrier slow exponentially with force, with a characteristic force of about $2\,\mathrm{pN}$ rather than $k_{\mathrm{B}}T/\delta \approx 7\,\mathrm{pN}$ (Dogterom and Yurke, 1997), and stall at a few piconewtons (Kerssemakers and colleagues, 2006): the load is borne by only a few of the 13 protofilament ends at a time, and catastrophes intervene. Networks of branched actin grow at a nearly load-independent velocity over a wide range before stalling (Parekh and colleagues, 2005), because the network adapts its density to the load. Euler buckling ([7.6.26](/7.6.26#sec-26.2)) limits the force a single filament can transmit to its tip, which is why the actin of lamellipodia is a dense, cross-linked network of short free ends and why single microtubules push effectively only over short distances.

### 28.6.3. Depolymerization as a Motor

A shrinking microtubule can pull. Chromosomes attached to microtubules in vitro move toward the depolymerizing end without ATP (Koshland, Mitchison and Kirschner, 1988); the free energy of GTP hydrolysis, stored as strain in the GDP lattice, is released when protofilaments peel outward from the end, and a coupler that holds on to the end harvests it. Two mechanisms are envisaged. In Hill's sleeve model (1985), a coupler with many weak binding sites for the lattice diffuses along the microtubule; when the end shrinks, the coupler would lose binding sites, so its diffusion is biased toward the remaining lattice and it follows the end, a ratchet driven by binding energy. In the conformational-wave model, curling protofilaments push against a ring or fibrils around the microtubule, a power stroke; laser-trap measurements estimated about $5\,\mathrm{pN}$ per curling protofilament (Grishchuk and colleagues, 2005). The kinetochore complexes Ndc80 and, in yeast, the Dam1 ring follow shrinking ends against loads of several piconewtons, and their attachment becomes more stable under tension, a **catch bond** that helps the cell select correct, bioriented attachments of chromosomes to the spindle (Akiyoshi and colleagues, 2010; **kinetochore**, [7.3.21](/7.3.21)).

### 28.6.4. Centering by Pushing and Pulling

Microtubules growing from a centrosome placed in a microfabricated chamber push against the walls, and the centrosome moves to the center of the chamber within minutes and returns there when displaced with optical tweezers (Holy and colleagues, 1997); in fission yeast, microtubules pushing against the cell tips center the nucleus (Tran and colleagues, 2001). The mechanism is the length dependence of the pushing force: a microtubule cannot push harder than its buckling force, $\propto 1/L^2$, so the short microtubules on the near side push harder than the long ones on the far side, and the net force restores the center. Pulling can also center if the force per microtubule grows with its length, as when cytoplasmic dynein distributed in the cytoplasm pulls along each microtubule (Kimura and Kimura, 2011), but pulling by a fixed number of force generators at the cortex can destabilize the center and is used to move spindles off-center in asymmetric divisions ([7.5](/7.5)).

![Centering an aster by microtubule forces (two-dimensional toy model: 360 radial microtubules in a circular cell of radius 10 µm). A: geometry with the aster displaced to the right; microtubules toward the near cortex are short. B: net force on the aster against its position. Pushing, with each microtubule limited by its Euler buckling force π²ℓ_pk_BT/l² (ℓ_p = 5 mm), and pulling proportional to length (0.1 pN per µm of microtubule) both give restoring forces with stiffnesses of tens of pN/µm (negative slope through zero); a constant pull per microtubule gives no force in this symmetric geometry](./plots/positioning.py)

### 28.6.5. Bacterial Polymerization Motors

Bacteria use polymerization motors for jobs that eukaryotes give to translational motors. The actin homolog ParM segregates low-copy plasmids: ParM filaments are dynamically unstable, but bundles of antiparallel filaments capped by plasmid-bound ParR–parC complexes at both ends are stabilized and elongate, pushing the two plasmids to opposite poles (Garner, Campbell and Mullins, 2004). The intracellular pathogen *Listeria monocytogenes* moves through the host cytoplasm at about $0.1\,\mu\mathrm{m\,s^{-1}}$ on a comet tail of host actin nucleated by its surface protein ActA ([7.3.13](/7.3.13#sec-13.4.1)); its speed depends only weakly on the size of the bacterium or of beads coated with ActA, contrary to the prediction $v = 2D/\delta$ of a ratchet in which the load's own diffusion opens the gap, which is why models in which the bending of filament tips opens the gap were introduced (Mogilner and Oster, 1996; [7.6.26](/7.6.26#sec-26.5.3)).

## 28.7. Motors Compared

| Motor | Step per fuel | Force or torque at stall | Maximal speed | Work at stall / $\Delta\mu$ | Coupling, mechanism |
|---|---|---|---|---|---|
| Kinesin-1 | $8.2\,\mathrm{nm}$ per ATP | $7\,\mathrm{pN}$ | $0.8\,\mu\mathrm{m\,s^{-1}}$ | about $0.6$ | tight at low load, ATP-driven back steps |
| Myosin V | $36\,\mathrm{nm}$ per ATP | $2.5$–$3\,\mathrm{pN}$ | $0.4\,\mu\mathrm{m\,s^{-1}}$ | about $1$ | lever arm, hand over hand |
| F₁-ATPase | $120°$ per ATP | $40\,\mathrm{pN\,nm}$ | $130\,\mathrm{Hz}$ | about $1$ | tight, reversible |
| Fₒ (c₈ ring) | $45°$ per $\ce{H+}$ | $\approx 40\,\mathrm{pN\,nm}$ at $200\,\mathrm{mV}$ | $\sim 100$–$300\,\mathrm{Hz}$ | close to $1$ | Brownian ratchet |
| Flagellar motor | $14°$ per step | $1300$–$2000\,\mathrm{pN\,nm}$ | $300\,\mathrm{Hz}$ ($1700\,\mathrm{Hz}$ for $\ce{Na+}$) | $\gtrsim 0.3$ | stator power strokes, load-dependent remodeling |
| RNA polymerase | $0.34\,\mathrm{nm}$ per NTP | $25$–$30\,\mathrm{pN}$ | $20$–$80\,\mathrm{nt\,s^{-1}}$ | low | Brownian ratchet, load on a fast step |
| φ29 packaging motor | $0.85\,\mathrm{nm}$ per ATP | $57\,\mathrm{pN}$ | $150\,\mathrm{bp\,s^{-1}}$ | about $0.6$ | ring ATPase, dwell–burst cycle |
| Actin filament / microtubule | $2.7$ / $0.6\,\mathrm{nm}$ per subunit | $\le 7$ / $\le 30\,\mathrm{pN}$ | $\sim 0.1$–$1\,\mu\mathrm{m\,s^{-1}}$ | — | polymerization ratchet |
| Translocation ratchet | $d$ per bound site | $(k_{\mathrm{B}}T/d)\ln(1 + c/K_{\mathrm{d}})$ | $2D/d$ | — | binding free energy |

Three lessons run through the table. The free energy of one fuel molecule sets an upper bound on force times step for every motor, and many motors come within a factor of two of it. The shape of the force–velocity curve tells where in the cycle the load acts, not how strong the motor is. And whether a motor is a power stroke or a ratchet is a question about which transition of its cycle carries the load, decided by single-molecule measurements of steps, dwells and fluctuations.

## Summary

| Topic | Key relations and results |
|---|---|
| Rotary bound (28.1) | $\tau_{\max} = \Delta\mu/\Delta\theta$ (Formula 28.1.1); drag dynamometers and magnetic rotation |
| F₁ (28.2) | 120° steps, 80° (ATP binding) + 40° (hydrolysis, phosphate release) substeps; $\nu = \nu_{\max}[\mathrm{ATP}]/(K_{\mathrm{M}} + [\mathrm{ATP}])$, $\nu_{\max} \approx 130\,\mathrm{Hz}$, $K_{\mathrm{M}} \approx 15\,\mu\mathrm{M}$ (Formula 28.2.1); torque $40\,\mathrm{pN\,nm}$, efficiency near 1 by drag and by $\ln[P(\Delta\theta)/P(-\Delta\theta)] = \tau\Delta\theta/k_{\mathrm{B}}T$ (Formula 28.2.2); forced rotation makes ATP |
| ATP synthase (28.3) | $\tau_{\mathrm{o}} = n_ce\Delta p/2\pi$ vs $\tau_1 = 3\Delta G_{\mathrm{p}}/2\pi$; synthesis iff $(n_c/3)e\Delta p > \Delta G_{\mathrm{p}}$ (Formula 28.3.1); Fₒ is a protonation ratchet |
| Flagellar motor (28.4) | 11 stators, 26 steps per turn, $\sim 1000\,\ce{H+}$ per turn; thermodynamic plateau and kinetic knee from a two-state stator cycle (Formula 28.4.1); stall torque $\propto N$; CheY-P switching, load-dependent stator recruitment |
| Translocation (28.5) | translocation ratchet (Definition 28.5.1), $v = (2D/d)(w^2/2)/(\mathrm{e}^w - w - 1)$ (Theorem 28.5.1), speed-up $n$; reversible binding stalls at $(k_{\mathrm{B}}T/d)\ln(1 + c/K_{\mathrm{d}})$ (Formula 28.5.1); import is not diffusion-limited (Example 28.5.1); unfoldases and φ29 are power-stroke ring motors (57 pN, 10 bp bursts of $4\times2.5\,\mathrm{bp}$) |
| Load and shape | load on a fast step: flat, then abrupt (RNA polymerase); on a slow step: gradual (φ29) |
| Polymerization (28.6) | polymerization as a short-step motor, $F_{\mathrm{s}} = (k_{\mathrm{B}}T/\delta)\ln(c/c_{\mathrm{c}})$: 7 pN (actin), 30 pN (microtubule), theory in 7.6.26; measured forces below ideal; depolymerization couplers (sleeve, curling protofilaments, catch bonds); centering by length-dependent pushing or pulling |

## Questions

1. The c ring of the chloroplast ATP synthase has 14 subunits. At a proton-motive force of $180\,\mathrm{mV}$, what is the maximal torque of $\mathrm{F_o}$, and against what phosphorylation potential can the enzyme still synthesize ATP? Compare with the mitochondrial c₈ enzyme.

   **Answer** $e\Delta p = 0.18\,\mathrm{eV} = 28.8\,\mathrm{pN\,nm}$. $\tau_{\mathrm{o}} = 14\times28.8/2\pi = 64\,\mathrm{pN\,nm}$. Synthesis requires $\Delta G_{\mathrm{p}} < (14/3)\times28.8 = 134\,\mathrm{pN\,nm}$ per molecule, $81\,\mathrm{kJ\,mol^{-1}}$. For c₈: $\tau_{\mathrm{o}} = 37\,\mathrm{pN\,nm}$ and $\Delta G_{\mathrm{p}} < 77\,\mathrm{pN\,nm} = 46\,\mathrm{kJ\,mol^{-1}}$: at $180\,\mathrm{mV}$ the mitochondrial enzyme could not maintain $50\,\mathrm{kJ\,mol^{-1}}$ and needs a larger $\Delta p$ (about $200\,\mathrm{mV}$), while the chloroplast enzyme has a large margin, buying it robustness at the cost of more protons per ATP.

2. A $2\,\mu\mathrm{m}$ actin filament attached to F₁ rotates at $0.8$ revolutions per second. Its rotational drag is $\zeta = 4\pi\eta L^3/\{3[\ln(L/2b) - 0.45]\}$ with $b = 4\,\mathrm{nm}$ and $\eta = 10^{-3}\,\mathrm{Pa\,s}$. Compute the torque and the efficiency if $\Delta\mu = 90\,\mathrm{pN\,nm}$.

   **Answer** $\ln(2000/8) - 0.45 = 5.52 - 0.45 = 5.07$; $\zeta = 4\pi\times10^{-3}\times8\times10^{-18}/(3\times5.07) = 6.6\times10^{-21}\,\mathrm{N\,m\,s}$. $\omega = 2\pi\times0.8 = 5.0\,\mathrm{s^{-1}}$; $\tau = 3.3\times10^{-20}\,\mathrm{N\,m} = 33\,\mathrm{pN\,nm}$. Work per step $33\times2\pi/3 = 69\,\mathrm{pN\,nm}$, efficiency about $77\,\%$; the uncertainty of the drag near a surface (tens of percent) is why the fluctuation-theorem method was developed.

3. In an F₁ experiment the probe angle changes by $\Delta\theta$ in $\Delta t = 1\,\mathrm{ms}$, and $\ln[P(\Delta\theta)/P(-\Delta\theta)]$ is found to increase by $10$ when $\Delta\theta$ increases by one radian. What torque does this imply at $298\,\mathrm{K}$? Why must $\Delta t$ be long compared with the stepping time for Formula 28.2.2 to give the motor's torque?

   **Answer** $\tau = 10\,k_{\mathrm{B}}T$ per radian $= 10\times4.1 = 41\,\mathrm{pN\,nm}$. The probe is coupled to the motor through an elastic linker and the motor steps discretely; on time scales shorter than the stepping and linker relaxation, the probe's displacements reflect the instantaneous linker force and its thermal fluctuations, not the average torque. Only for windows containing many steps does the entropy produced per rotation converge to $\tau\Delta\theta/T$, as in the long-time fluctuation theorem.

4. Using the flagellar motor model (Formula 28.4.1), explain qualitatively why the high-load torque is independent of temperature while the zero-load speed has a $Q_{10}$ of about 2–3. What would you predict for a motor driven by $\ce{Na+}$ when the external $\ce{Na+}$ concentration is lowered tenfold at constant membrane potential?

   **Answer** At high load the cycle is close to equilibrium; the torque is fixed by $N\Delta\mu/\delta$ and the rapid-equilibrium power stroke, which depend on free energies, not on rates, so temperature (through rates) has little effect. At low load the rate of ion transfer limits the cycle and is thermally activated, hence its $Q_{10}$. Lowering external $\ce{Na+}$ tenfold lowers the sodium-motive force by $(k_{\mathrm{B}}T/e)\ln10 \approx 59\,\mathrm{mV}$ (at $25\,^\circ\mathrm{C}$), lowering the plateau torque in proportion to $\Delta\mu$; it also lowers the ion-binding rate on the outside, shifting the knee and the maximum speed. Both are observed for *Vibrio* motors.

5. Derive the small-load expansion $v \approx (2D/d)(1 - w/3)$ from Theorem 28.5.1 and interpret the factor $1/3$ in terms of the mean position of the diffusing site.

   **Answer** $\mathrm{e}^w - w - 1 = (w^2/2)(1 + w/3 + O(w^2))$, so $v = (2D/d)/(1 + w/3) \approx (2D/d)(1 - w/3)$. In the force-free steady state the density of the last site is $p(x) = 2(d - x)/d^2$, with mean $\langle x\rangle = d/3$; to first order the load slows the diffusive crossing by its work over this mean distance, $F\langle x\rangle/k_{\mathrm{B}}T = w/3$, the same factor.

6. A protein is imported through a pore with binding sites every $d = 4\,\mathrm{nm}$; chaperones bind with $K_{\mathrm{d}} = 1\,\mu\mathrm{M}$ at a concentration of $50\,\mu\mathrm{M}$. What is the stall force of the ratchet? Could this ratchet unfold a domain that requires $15\,\mathrm{pN}$?

   **Answer** $F_{\mathrm{s}} = (4.1/4)\ln51\,\mathrm{pN} = 1.03\times3.93 = 4.0\,\mathrm{pN}$. Not by force alone: $15\,\mathrm{pN}$ would require $c/K_{\mathrm{d}} \approx \mathrm{e}^{14.6} \approx 2\times10^6$. A ratchet could still import such a domain by waiting for spontaneous unfolding at the pore and trapping the unfolded chain (the rate is then that of thermal unfolding, possibly very slow), or a motor must pull with a power stroke; distinguishing the two is the debate about mtHsp70.

7. The φ29 motor packages $19.3\,\mathrm{kb}$. Assume a velocity of $120\,\mathrm{bp\,s^{-1}}$ for the first $60\,\%$ of the genome and a linear decline of the velocity to $20\,\mathrm{bp\,s^{-1}}$ at full packaging. Estimate the packaging time and the number of ATP hydrolyzed.

   **Answer** First part: $0.6\times19300/120 = 97\,\mathrm{s}$. Second part: $7720\,\mathrm{bp}$ with $v$ falling linearly from $120$ to $20$; $t = \int\mathrm{d}L/v = (7720/100)\ln(120/20) = 77.2\times1.79 = 138\,\mathrm{s}$. Total about $235\,\mathrm{s}$, about four minutes. At $2.5\,\mathrm{bp}$ per ATP (ignoring the regulatory hydrolysis and the decrease of burst size at high filling, which raise it), about $19300/2.5 = 7700$ ATP, or about $9600$ if five ATP are hydrolysed per $10\,\mathrm{bp}$ cycle.

8. RNA polymerase moves at $15\,\mathrm{nt\,s^{-1}}$ almost independently of load up to $20\,\mathrm{pN}$ and stalls at $25\,\mathrm{pN}$. Using the two-state picture, which transition carries the load, and what is the work per nucleotide at stall compared with $k_{\mathrm{B}}T$?

   **Answer** A flat force–velocity curve until near stall means the load acts on a transition that is fast and in rapid equilibrium (translocation by one base pair), not on the rate-limiting chemistry; only when the load has shifted the translocation equilibrium strongly toward the pre-translocated state does it limit the cycle. The work at stall is $25\times0.34 = 8.5\,\mathrm{pN\,nm} \approx 2\,k_{\mathrm{B}}T$, much less than the free energy of nucleotide incorporation and pyrophosphate hydrolysis: stall is set by the translocation equilibrium (the polymerase backtracks), not by the chemical free energy, a sign of loose coupling.

9. Estimate the maximal force from polymerization of an actin filament at $c = 20\,\mu\mathrm{M}$ with $c_{\mathrm{c}} = 0.1\,\mu\mathrm{M}$, and the maximal unsupported length that can bear it without buckling (pinned ends, $\ell_{\mathrm{p}} = 15\,\mu\mathrm{m}$). What does this imply for the architecture of a lamellipodium?

   **Answer** $F_{\mathrm{s}} = (4.1/2.7)\ln200 = 1.52\times5.30 = 8.0\,\mathrm{pN}$. Buckling: $\pi^2\ell_{\mathrm{p}}k_{\mathrm{B}}T/L^2 = F_{\mathrm{s}}$ gives $L = \pi\sqrt{15000\times4.1/8.0}\,\mathrm{nm} = \pi\times88\,\mathrm{nm} \approx 0.28\,\mu\mathrm{m}$. Free filament ends must be shorter than a few hundred nanometers; the lamellipodium's branched, cross-linked network with short free ends (about $0.1$–$0.2\,\mu\mathrm{m}$) meets this requirement, and the many filaments share the load of the membrane.

10. (Experiment design) Propose an experiment to decide whether a newly discovered ring ATPase that translocates DNA is a Brownian ratchet or a power-stroke motor.

    **Answer** Measure single-molecule force–velocity curves, step sizes and dwell-time distributions in an optical trap at several [ATP], [ADP] and loads, including assisting loads. A ratchet whose load-dependent step is diffusive shows velocities that depend on viscosity (add glycerol or a larger tether) and on the diffusion of the DNA, an assisting load that hardly increases speed, and dwell times whose load dependence sits in an ATP-independent transition; a power stroke shows steps of fixed size coupled to ATP binding or hydrolysis, force-generating transitions identified by their load dependence, and a stall force that tracks $\Delta\mu$ if tightly coupled. Mutants that slow ATP hydrolysis or block subunit communication, and structures in different nucleotide states (cryo-EM), complete the picture.

11. In the centering model (Section 28.6.4), why do pushing forces limited by buckling center an aster, while constant pulling forces at the cortex do not? What changes if the number of force generators at the cortex is limiting?

    **Answer** With pushing, the force per microtubule decreases with its length as $1/L^2$, so the side closer to the cortex pushes harder and pushes the aster back; the net force is restoring. A constant pull per microtubule, with microtubules uniformly distributed in angle, gives the same total pull whatever the position. If the number of cortical generators per area is limiting, each generator engages at most one microtubule; microtubules reaching the near cortex arrive at a higher density per area, so not all can be engaged there while the far cortex, reached by sparser microtubules, may engage nearly all of its microtubules. The net force then depends on the density of generators and can be centering or decentering; asymmetric distributions of active generators are used by the *Caenorhabditis elegans* zygote to displace its spindle posteriorly.
