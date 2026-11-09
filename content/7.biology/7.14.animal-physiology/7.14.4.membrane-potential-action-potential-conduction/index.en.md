---
title: Membrane Potential, Action Potential and Conduction
description: "The Galvani–Volta dispute over animal electricity; the ionic basis of the membrane potential: equilibrium potentials and the Nernst equation (Na⁺, K⁺, Ca²⁺, Cl⁻), the GHK equation and the effect of P_Na/P_K on the resting potential–[K⁺]ₒ curve, the electrogenic contribution of the Na⁺/K⁺-ATPase; the equivalent circuit of the membrane, conductance weighting and driving force, membrane capacitance and how many ions it takes to set up a membrane potential; local potentials and receptor potentials; excitability, threshold potential and the strength–duration relation; phases and ionic mechanism of the action potential, refractory periods, supernormal and subnormal periods, Ca²⁺ action potentials; the compound action potential of Erlanger and Gasser and fiber classification, the squid giant axon, the voltage clamp and the conclusions of Hodgkin and Huxley; the energy cost of restoring Na⁺ and K⁺ gradients; passive cable properties, the two strategies of giant axons and myelin, saltatory conduction and the scaling of conduction velocity; comparisons including giant axons, multiple origins of myelin, and Ca²⁺ action potentials in nematodes and Paramecium."
source_hash: a287838998ef
---

Across the membrane of every living cell there is a potential difference of about $-10$ to $-100\,\mathrm{mV}$; nerve and muscle cells can also reverse this potential within a millisecond and propagate it along the cell membrane at speeds from a few meters per second to more than a hundred. The membrane potential and the action potential are the common basis of information transfer in the nervous system, muscle contraction, glandular secretion and cardiac rhythm, and the precondition for understanding almost every later chapter. This chapter first explains how the membrane potential arises from ion gradients and selective permeability (Sections 4.1–4.3), then treats two kinds of electrical signal: local potentials that decay with distance and all-or-none action potentials (Sections 4.4–4.6), then the history of research on the action potential and the conclusions of Hodgkin and Huxley (Section 4.7), its energy cost (Section 4.8) and conduction (Section 4.9), and finally compares the solutions of other animals (Section 4.10).

The required ion gradients are established by the transport proteins of the previous chapter (Chapter 3). The physics of electrical signals, namely the derivation of the **Nernst–Planck equation** and the **Goldman–Hodgkin–Katz equation**, the **cable equation**, the equations and numerical simulation of the **Hodgkin–Huxley model**, and the electrical properties of myelin, is given in full in biophysics ([7.6.30](/7.6.30)); the resting potential and the pump–leak model are treated in cell biology ([7.3.5](/7.3.5)). This chapter cites only their conclusions and concentrates on experimental facts, parameters and reasoning in physiology. Synaptic transmission and neural circuits are in Chapters 5 and 6, and the cardiac action potential in Chapter 13.

## 4.1. Animal Electricity

In the 1780s Luigi Galvani observed that when a metal scalpel touched the nerve of a dissected frog while a nearby electrical machine discharged, the frog's leg twitched; and when a bow made of two different metals (such as iron and copper) connected the spinal cord to the leg muscle, the leg contracted violently. Galvani believed that "animal electricity" was stored in the tissue like a Leyden jar (an early capacitor), the metal being merely the conductor that released it. Alessandro Volta held instead that the electricity came from the contact of two different metals with a moist, salty tissue and had nothing to do with life; to prove it he removed the frog altogether and stacked zinc and copper disks separated by brine-soaked cardboard, inventing in 1800 the first chemical battery, the voltaic pile.

Each was half right: the bimetallic bow was indeed an external source, but biological tissue itself can also generate electricity. In the middle of the nineteenth century du Bois-Reymond recorded the "current of injury" and the "negative variation" (that is, the action potential) of nerve and muscle, and Helmholtz measured the conduction velocity of the frog nerve at about $27\,\mathrm{m\,s^{-1}}$. In 1902 Bernstein proposed the membrane theory: at rest the membrane is permeable only to $\ce{K+}$, and the membrane potential is close to the equilibrium potential of $\ce{K+}$; in excitation the membrane becomes temporarily permeable to all ions and the potential vanishes. The first half of this theory is correct, and the second half was corrected by Hodgkin and Huxley: in excitation the membrane potential does not merely vanish but reverses (Section 4.7).

## 4.2. The Ionic Basis of the Membrane Potential

### 4.2.1. The Membrane Potential and Some Terms

The membrane potential is the potential difference across the cell membrane, defined as inside relative to outside, $V_{\mathrm{m}} = \psi_{\mathrm{i}} - \psi_{\mathrm{o}}$. Its value is about $-0.1\,\mathrm{V}$, yet it falls across a membrane only $5$–$10\,\mathrm{nm}$ thick, so that the electric field in the membrane is as high as about $10^7\,\mathrm{V\,m^{-1}}$, enough to move the **voltage sensors** of **voltage-gated channels**. The membrane potential of an unstimulated cell is called the **resting membrane potential**: about $-10\,\mathrm{mV}$ in red cells, about $-50$ to $-60\,\mathrm{mV}$ in smooth muscle, about $-70\,\mathrm{mV}$ in neurons, and about $-85$ to $-90\,\mathrm{mV}$ in skeletal and ventricular muscle.

**Definition 4.2.1 (Polarization, Depolarization, Hyperpolarization, Repolarization and Overshoot)** The state in which the membrane is negative inside and positive outside at rest is called polarization. A change of the membrane potential in the positive direction (reduced polarization) is called **depolarization**; a change in the more negative direction is called **hyperpolarization**; the return toward the resting potential after depolarization is called **repolarization**; and the part of an action potential in which the membrane potential crosses zero and becomes positive inside and negative outside is called the **overshoot**.

### 4.2.2. Equilibrium Potentials

Suppose the membrane is permeable to only one ion $\mathrm{X}$. $\ce{K+}$ is concentrated inside the cell and dilute outside and will flow out down its concentration gradient; for every $\ce{K+}$ that leaves, one impermeant anion (protein, organic phosphate) is left behind, the inside of the membrane becomes negative, and this prevents $\ce{K+}$ from flowing out further. When the effect of the potential difference on $\ce{K+}$ just cancels that of the concentration difference, the net movement of $\ce{K+}$ is zero.

**Definition 4.2.2 (Equilibrium Potential)** The membrane potential at which the net transmembrane flux of an ion is zero, that is, at which its electrochemical potential difference $\Delta\tilde\mu_{\mathrm{X}} = 0$, is called the **equilibrium potential** of that ion. Setting Eq. (3.5) of Chapter 3 to zero gives the **Nernst equation**
$$
E_{\mathrm{X}} = -\frac{RT}{z_{\mathrm{X}}F}\ln\frac{[\mathrm{X}]_{\mathrm{i}}}{[\mathrm{X}]_{\mathrm{o}}} = \frac{RT}{z_{\mathrm{X}}F}\ln\frac{[\mathrm{X}]_{\mathrm{o}}}{[\mathrm{X}]_{\mathrm{i}}}. \tag{4.1}
$$

At $37\,{}^\circ\mathrm{C}$, $RT\ln 10/F = 61.5\,\mathrm{mV}$; at about $30\,{}^\circ\mathrm{C}$ it is $60\,\mathrm{mV}$. For a monovalent cation, each tenfold change of the concentration ratio therefore changes the equilibrium potential by about $61.5\,\mathrm{mV}$:
$$
E_{\mathrm{X}} = \frac{61.5\,\mathrm{mV}}{z_{\mathrm{X}}}\log_{10}\frac{[\mathrm{X}]_{\mathrm{o}}}{[\mathrm{X}]_{\mathrm{i}}}\quad (37\,{}^\circ\mathrm{C}).
$$

**Example 4.2.1 (Equilibrium Potentials of Skeletal Muscle)** Mammalian skeletal muscle ($37\,{}^\circ\mathrm{C}$):

| Ion | $[\mathrm{X}]_{\mathrm{o}}/(\mathrm{mmol\,L^{-1}})$ | $[\mathrm{X}]_{\mathrm{i}}/(\mathrm{mmol\,L^{-1}})$ | $[\mathrm{X}]_{\mathrm{o}}/[\mathrm{X}]_{\mathrm{i}}$ | $E_{\mathrm{X}}/\mathrm{mV}$ |
|---|---|---|---|---|
| $\ce{K+}$ | $4.5$ | $155$ | $0.029$ | $-95$ |
| $\ce{Na+}$ | $145$ | $12$ | $12$ | $+67$ |
| $\ce{Ca^2+}$ | $1.0$ | $10^{-4}$ | $10^4$ | $+123$ |
| $\ce{Cl-}$ | $116$ | $4.2$ | $28$ | $-89$ |
| $\ce{HCO3-}$ | $24$ | $12$ | $2$ | $-19$ |

For example $E_{\mathrm{Ca}} = (61.5/2)\log_{10}10^4 = +123\,\mathrm{mV}$; for $\ce{Cl-}$, $z = -1$ and $E_{\mathrm{Cl}} = -61.5\log_{10}27.6 = -89\,\mathrm{mV}$. The resting potential of skeletal muscle is about $-85\,\mathrm{mV}$, close to $E_{\mathrm{K}}$ and $E_{\mathrm{Cl}}$ and far from $E_{\mathrm{Na}}$ and $E_{\mathrm{Ca}}$. In skeletal muscle $\ce{Cl-}$ is almost passively distributed ($E_{\mathrm{Cl}} \approx V_{\mathrm{m}}$); in most neurons KCC2 extrudes $\ce{Cl-}$ and $E_{\mathrm{Cl}}$ is about $-70\,\mathrm{mV}$ or even more negative, which is the basis of inhibitory synapses (Chapter 5).

:::

Changing the extracellular $[\ce{K+}]$ tests this theory. When the resting potential of frog skeletal muscle is plotted against $\log[\ce{K+}]_{\mathrm{o}}$, it is a straight line of slope about $58\,\mathrm{mV}$ per tenfold (frogs have a lower body temperature) over the higher range of $[\ce{K+}]_{\mathrm{o}}$, as the Nernst equation predicts; but at low $[\ce{K+}]_{\mathrm{o}}$ the curve departs from the line and is more positive than $E_{\mathrm{K}}$. This shows that the resting membrane has a small permeability to ions other than $\ce{K+}$.

### 4.2.3. Several Ions Jointly Determine the Membrane Potential: The GHK Equation

The transmembrane current of a single ion $\mathrm{X}$ depends on three factors: the concentrations $[\mathrm{X}]_{\mathrm{o}}$ and $[\mathrm{X}]_{\mathrm{i}}$ on the two sides, the membrane potential $V_{\mathrm{m}}$, and the permeability $P_{\mathrm{X}}$ of the membrane to it; integrating the Nernst–Planck equation under the assumption of a constant field gives the GHK current equation ([7.6.30](/7.6.30)). For a cation, the current is inward when $V_{\mathrm{m}}$ is below its reversal potential and outward when above. If only one ion can pass, the membrane potential at which the current is zero is its equilibrium potential, and the GHK equation reduces to the Nernst equation.

The reversal potential (the potential at which the current is zero) and the equilibrium potential are often numerically the same but differ in concept: the equilibrium potential is a thermodynamic property of an ion's gradient, independent of the channel; the reversal potential is a property of a particular current pathway (a particular channel or transporter). For a channel passing only one ion the two are equal; for a nonselective cation channel (such as the **nicotinic acetylcholine receptor** at the end plate), the reversal potential is about $0\,\mathrm{mV}$, between $E_{\mathrm{Na}}$ and $E_{\mathrm{K}}$, and does not equal the equilibrium potential of any single ion.

At rest the total membrane current is zero ($I_{\mathrm{total}} = 0$), and the potential at which the currents of all ions sum to zero is the resting potential. For $\ce{K+}$, $\ce{Na+}$ and $\ce{Cl-}$, the GHK current equation gives the **Goldman–Hodgkin–Katz equation**
$$
V_{\mathrm{m}} = \frac{RT}{F}\ln\frac{P_{\mathrm{K}}[\ce{K+}]_{\mathrm{o}} + P_{\mathrm{Na}}[\ce{Na+}]_{\mathrm{o}} + P_{\mathrm{Cl}}[\ce{Cl-}]_{\mathrm{i}}}{P_{\mathrm{K}}[\ce{K+}]_{\mathrm{i}} + P_{\mathrm{Na}}[\ce{Na+}]_{\mathrm{i}} + P_{\mathrm{Cl}}[\ce{Cl-}]_{\mathrm{o}}}. \tag{4.2}
$$
It shows that the membrane potential depends not only on the transmembrane concentration gradients of ions but also on the permeability of the membrane to each ion; the most permeant ion "dominates" the membrane potential, which at rest is $\ce{K+}$. $\ce{Na+}$, $\ce{K+}$ and $\ce{Cl-}$ are the main ions forming the membrane potential, and $P_{\mathrm{X}}$ is not constant: the opening and closing of channels makes them vary with time and voltage, which is exactly the source of electrical signals.

Neglecting $\ce{Cl-}$ and letting $\alpha = P_{\mathrm{Na}}/P_{\mathrm{K}}$, Eq. (4.2) becomes
$$
V_{\mathrm{m}} = 61.5\,\mathrm{mV}\,\log_{10}\frac{[\ce{K+}]_{\mathrm{o}} + \alpha[\ce{Na+}]_{\mathrm{o}}}{[\ce{K+}]_{\mathrm{i}} + \alpha[\ce{Na+}]_{\mathrm{i}}}.
$$
For $\alpha = 0$ it is the Nernst equation for $\ce{K+}$. For $\alpha = 0.01$ the curve bends upward away from the Nernst line at low $[\ce{K+}]_{\mathrm{o}}$: here $\alpha[\ce{Na+}]_{\mathrm{o}}$ is comparable to $[\ce{K+}]_{\mathrm{o}}$, and the contribution of $\ce{Na+}$ moves the membrane potential toward $E_{\mathrm{Na}}$; as $\alpha$ increases to $0.03$ and $0.1$ the bending is more marked. At high $[\ce{K+}]_{\mathrm{o}}$ the curves merge and the $\ce{K+}$ term dominates. The resting $\alpha$ of skeletal muscle is about $0.01$ and that of neurons about $0.02$–$0.05$, so the resting potential of neurons is more positive than that of skeletal muscle.

This curve has direct clinical significance. Hyperkalemia (plasma $[\ce{K+}]$ above about $6\,\mathrm{mmol\,L^{-1}}$) depolarizes the resting potential, and sustained depolarization inactivates voltage-gated $\ce{Na+}$ channels, so the excitability and conduction velocity of cardiac muscle first rise and then fall, and in severe cases arrhythmia and cardiac arrest result; hypokalemia hyperpolarizes the resting potential (in cardiac muscle there is also a paradoxical depolarization because of the fall in $\ce{K+}$ channel conductance) and appears as muscle weakness and arrhythmia (Chapter 13).

![Resting potential of mammalian skeletal muscle (37 °C) as a function of extracellular [K⁺], calculated from the GHK equation (neglecting Cl⁻, [K⁺]ᵢ = 155 and [Na⁺]ᵢ = 12 mM; when [K⁺]ₒ is changed it is replaced by Na⁺ so that [K⁺]ₒ + [Na⁺]ₒ = 149.5 mM stays constant). For α = P_Na/P_K = 0 the curve is the Nernst line for K⁺ (61.5 mV per tenfold); the larger α is, the more the curve at low [K⁺]ₒ is pulled toward E_Na; the dashed line is the normal [K⁺]ₒ = 4.5 mM](./plots/ghk-potassium.py)

### 4.2.4. Contribution of the Na⁺/K⁺-ATPase

The resting potential is determined mainly by ion diffusion (passive permeability), and the role of the **Na⁺/K⁺-ATPase** is twofold. Indirectly, it establishes and maintains the concentration gradients of $\ce{Na+}$ and $\ce{K+}$; without it the gradients would disappear within tens of minutes to hours, and the resting potential with them. Directly, it is **electrogenic**: each cycle pumps out 3 $\ce{Na+}$ and pumps in 2 $\ce{K+}$, removing one net positive charge, producing an outward current and making the membrane potential a few millivolts more negative than Eq. (4.2) predicts (about $-4\,\mathrm{mV}$ in skeletal muscle; of a resting potential of $-90\,\mathrm{mV}$, about $-86\,\mathrm{mV}$ comes from diffusion and about $-4\,\mathrm{mV}$ from the pump). In small cells with high membrane resistance (such as the fine processes of some neurons) the direct contribution of the pump can reach more than ten millivolts; after vigorous activity $[\ce{Na+}]_{\mathrm{i}}$ rises, the pump speeds up and can make the membrane transiently hyperpolarized (post-activity hyperpolarization).

## 4.3. The Equivalent Circuit of the Membrane

### 4.3.1. Batteries, Conductances and Capacitance

The electrical properties of the membrane can be summarized by a circuit:

1. The equilibrium potential of each ion, $E_{\mathrm{Na}}$, $E_{\mathrm{K}}$, $E_{\mathrm{Ca}}$, $E_{\mathrm{Cl}}$, is a battery whose electromotive force comes from the ion gradient;
2. The pathway of each ion (the **ion channel**) is a conductance, $G_{\mathrm{Na}}$, $G_{\mathrm{K}}$, $G_{\mathrm{Ca}}$, $G_{\mathrm{Cl}}$, in series with the corresponding battery;
3. The **lipid bilayer** is a capacitance $C_{\mathrm{m}}$, in parallel with all the ionic branches.

The current of each ion equals its conductance times the driving force,
$$
I_{\mathrm{X}} = G_{\mathrm{X}}(V_{\mathrm{m}} - E_{\mathrm{X}}). \tag{4.3}
$$
The driving force $V_{\mathrm{m}} - E_{\mathrm{X}}$ is the difference between the membrane potential and the equilibrium potential of the ion: the further the equilibrium potential lies from the membrane potential, the larger the driving force; when the equilibrium potential is above the membrane potential the current is negative, that is, a cation flows inward (inward current), and when below, the current is outward. At rest the ionic currents sum to zero, giving
$$
V_{\mathrm{m}} = \sum_{\mathrm{X}}\frac{G_{\mathrm{X}}}{G_{\mathrm{m}}}E_{\mathrm{X}}, \qquad G_{\mathrm{m}} = \sum_{\mathrm{X}}G_{\mathrm{X}}, \tag{4.4}
$$
that is, the membrane potential is the average of the equilibrium potentials weighted in proportion to conductance (the chord conductance equation). It expresses the same thing as the GHK equation: the larger the conductance of an ion, the closer the membrane potential lies to its equilibrium potential.

**Example 4.3.1 (Driving Forces)** Let the resting potential be $-90\,\mathrm{mV}$, using the equilibrium potentials of Example 4.2.1: the driving force for $\ce{K+}$ is $-90 - (-95) = +5\,\mathrm{mV}$ (weakly outward); for $\ce{Na+}$ it is $-90 - 67 = -157\,\mathrm{mV}$ (strongly inward); for $\ce{Ca^2+}$ it is $-90 - 123 = -213\,\mathrm{mV}$ (the strongest inward); for $\ce{Cl-}$ it is $-90 - (-89) = -1\,\mathrm{mV}$, almost zero. The driving forces of $\ce{Ca^2+}$ and $\ce{Na+}$ are largest, but their conductances at rest are very small, so the currents are not large; once the corresponding channels open, they produce strong inward currents.

### 4.3.2. Membrane Capacitance and "How Many Ions Are Needed"

The lipid bilayer is a thin insulating layer with conducting solutions on both sides, forming a parallel-plate capacitor with capacitance per unit area
$$
\frac{C}{A} = \frac{\varepsilon_{\mathrm{r}}\varepsilon_0}{a},
$$
where $a$ is the membrane thickness and $\varepsilon_{\mathrm{r}}$ the relative permittivity of the hydrocarbon core (about $2$–$5$). Taking $a \approx 5\,\mathrm{nm}$ gives $C_{\mathrm{m}} \approx 1\,\mu\mathrm{F\,cm^{-2}}$, the same for almost all biological membranes. Membrane area is proportional to capacitance, so measuring changes in capacitance detects changes in membrane area: when a secretory vesicle fuses with the plasma membrane, each vesicle increases the membrane capacitance by about $1\,\mathrm{fF}$ (a few femtofarads for large chromaffin granules), and membrane capacitance recording has therefore become a powerful tool for studying **exocytosis**. The relation $Q = C_{\mathrm{m}}V$ between charge and voltage tells us how many ions must be separated to set up a membrane potential.

**Example 4.3.2 (How Many $\ce{K+}$ Are Needed to Set Up a Membrane Potential?)** Let the cell be a sphere of diameter $10\,\mu\mathrm{m}$ with $[\ce{K+}]_{\mathrm{o}} = 5$, $[\ce{K+}]_{\mathrm{i}} = 140\,\mathrm{mmol\,L^{-1}}$ and $C_{\mathrm{m}} = 1\,\mu\mathrm{F\,cm^{-2}} = 10^{-14}\,\mathrm{F\,\mu m^{-2}}$. If the resting potential is set up entirely by efflux of $\ce{K+}$, then to reach $-61.5\,\mathrm{mV}$ the charge required per square micrometer of membrane is $Q = 10^{-14} \times 0.0615 = 6.15\times10^{-16}\,\mathrm{C}$, that is, $6.15\times10^{-16}/1.602\times10^{-19} \approx 3800$ $\ce{K+}$ ions. The cell membrane has an area of $4\pi(5\,\mu\mathrm{m})^2 = 314\,\mu\mathrm{m^2}$, requiring $1.2\times10^6$ $\ce{K+}$ in all. The cell volume is $524\,\mu\mathrm{m^3} = 5.24\times10^{-13}\,\mathrm{L}$ and contains $0.14 \times 5.24\times10^{-13} \times 6.02\times10^{23} = 4.4\times10^{10}$ $\ce{K+}$ ions. The fraction is $2.7\times10^{-5}$, about $0.0027\%$.

To then depolarize the membrane potential from $-61.5\,\mathrm{mV}$ to $+35\,\mathrm{mV}$ (a change of $96.5\,\mathrm{mV}$), the positive charge that must enter (in fact $\ce{Na+}$) is about 6000 per square micrometer, about $1.9\times10^6$ for the whole cell, still only $4\times10^{-5}$ of intracellular $\ce{K+}$ and $0.05\%$ of intracellular $\ce{Na+}$ ($12\,\mathrm{mmol\,L^{-1}}$, about $3.8\times10^9$ ions). During repolarization the same number of $\ce{K+}$ flow out. Pumping these $\ce{Na+}$ back, at 3 $\ce{Na+}$ per ATP, takes at least about $6\times10^5$ ATP; a mammalian cell of this size consumes of the order of $10^8$ ATP per second, so the minimum cost of an action potential is less than one hundredth of a second of its energy budget (the actual $\ce{Na+}$ and $\ce{K+}$ currents overlap, and the cost is $1.3$–$4$ times the minimum, see Section 4.8).

This calculation shows that rapid changes of membrane potential require only very few ions to move across the membrane and hardly change ion concentrations inside and outside the cell; the membrane is the important interface for electrical signals, and the ion concentration gradient is a "battery" that can support thousands upon thousands of action potentials. Only in very thin processes (axons and dendritic spines a few tenths of a micrometer in diameter) do the ions moved by each action potential reach more than one percent of the intracellular content, and high-frequency firing then changes local ion concentrations significantly.

![Fraction of the cell's ions moved by electrical signals. Purple line: the fraction of intracellular K⁺ (140 mM) moved when a spherical cell sets up a −70 mV resting potential by K⁺ efflux, 3C_mV/(eN_A[K⁺]ᵢr); blue line: the fraction of axonal Na⁺ (12 mM) that must at least enter during one action potential (100 mV depolarization), 2C_mΔV/(eN_A[Na⁺]ᵢa). Both are inversely proportional to diameter: negligible in a 10 µm cell, whereas in a thin axon of diameter 0.2 µm each action potential increases Na⁺ by about 2%](./plots/ions-vs-size.py)

:::

The properties of a change of membrane potential (threshold, peak, time course) are determined by four things: the properties of the ion channels in the membrane, the concentrations of charged ions on the two sides of the membrane, the electrical properties of the membrane (resistance and capacitance), and the shape and size of the cell.

## 4.4. Local Potentials

**Definition 4.4.1 (Local Potential)** A change of membrane potential caused in the membrane by a subthreshold stimulus, a synaptic input or a sensory stimulus, whose amplitude varies in a graded way with stimulus strength and which decays with distance and time, is called a **local potential** (also called a graded potential or electrotonic potential). The local potential generated by a receptor cell in response to an adequate stimulus is called a receptor potential (Chapter 39), and that on the postsynaptic membrane a postsynaptic potential (Chapter 5).

Local potentials have four characteristics:

1. Graded: not all-or-none, with amplitude proportional to stimulus strength;
2. Summable: local potentials produced at neighboring sites at the same time add (**spatial summation**), and local potentials produced in succession at the same site add if the earlier one has not yet disappeared (**temporal summation**);
3. Decremental: they spread passively along the membrane (electrotonic spread), with amplitude falling exponentially with distance and delay increasing with distance;
4. Their time course is determined by the electrical properties of the membrane (the time constant $\tau_{\mathrm{m}} = R_{\mathrm{m}}C_{\mathrm{m}}$, usually a few to a few tens of milliseconds).

Hyperpolarizing local potentials are always passive in this way; depolarizing local potentials are also so below threshold, but once threshold is reached they trigger an action potential. The action potential is the opposite: its peak does not change as it propagates along the membrane, only the delay increases with distance. Only cells over very short distances (no more than a few length constants, usually less than $1\,\mathrm{mm}$) can therefore transmit signals by local potentials: the photoreceptors and bipolar cells of the retina, **hair cells** of the inner ear and many interneurons of invertebrates fire no action potentials and transmit information by graded potentials and graded release of **neurotransmitter**. Graded signals can carry more information than all-or-none pulses, but cannot travel far (Chapter 41).

## 4.5. Excitability and Threshold

### 4.5.1. Excitable Cells

**Definition 4.5.1 (Excitability)** The ability of a tissue or cell to produce an action potential on stimulation is called **excitability**; cells that can produce action potentials (neurons, muscle cells, certain glandular cells) are called excitable cells.

For a stimulus to cause excitation it must have three elements: sufficient strength, sufficient duration and a sufficient rate of change of strength. With stimulus duration and rate of change fixed, the smallest stimulus strength that causes excitation is called the threshold strength (threshold); the lower the threshold, the higher the excitability.

### 4.5.2. Threshold Potential

**Definition 4.5.2 (Threshold Potential)** The critical membrane potential to which the membrane must be depolarized to trigger an action potential is called the **threshold potential**. At this potential the inward current produced by the opening of voltage-gated $\ce{Na+}$ channels just exceeds the outward current of $\ce{K+}$ and leak currents, and the depolarization begins to accelerate itself.

The threshold potential is usually $10$–$20\,\mathrm{mV}$ more positive than the resting potential (about $-55\,\mathrm{mV}$ in neurons). A subthreshold stimulus causes a smaller depolarization, few $\ce{Na+}$ channels open, the inward current is canceled by $\ce{K+}$ efflux, and the membrane potential returns to rest; once threshold is exceeded, **positive feedback** forms between $\ce{Na+}$ influx and depolarization (the Hodgkin cycle): depolarization opens more $\ce{Na+}$ channels, more $\ce{Na+}$ influx depolarizes the membrane further, until the membrane potential approaches $E_{\mathrm{Na}}$. The role of a threshold stimulus is to push the membrane potential to the threshold potential, after which the amplitude of the action potential is independent of the stimulus. With electrical stimulation, the cathode (where current flows out of the cell) depolarizes the membrane and can cause excitation; the anode hyperpolarizes the membrane and can only lower excitability.

### 4.5.3. The Strength–Duration Relation

A shorter stimulus needs a greater strength. Treating the membrane as an RC circuit of resistance $R_{\mathrm{m}}$ in parallel with capacitance $C_{\mathrm{m}}$ (time constant $\tau = R_{\mathrm{m}}C_{\mathrm{m}}$), a constant current $I$ of duration $t$ raises the membrane potential by $IR_{\mathrm{m}}(1 - \mathrm{e}^{-t/\tau})$; setting this equal to the depolarization $\Delta V_{\mathrm{th}}$ needed to reach threshold gives the threshold current
$$
I_{\mathrm{th}}(t) = \frac{I_{\mathrm{rh}}}{1 - \mathrm{e}^{-t/\tau}}, \qquad I_{\mathrm{rh}} = \frac{\Delta V_{\mathrm{th}}}{R_{\mathrm{m}}}. \tag{4.5}
$$
The smallest strength required for an infinitely long stimulus, $I_{\mathrm{rh}}$, is called the rheobase; the stimulus duration needed at twice the rheobase is called the *chronaxie*, which by Eq. (4.5) is $t_{\mathrm{c}} = \tau\ln 2$. Chronaxie is a common index for comparing the excitability of different tissues: about $0.1$–$0.3\,\mathrm{ms}$ for myelinated nerve fibers and a few milliseconds for skeletal muscle fibers, which is the basis for electrodiagnosis of neuromuscular disease and for the choice of pulse width in cardiac pacemakers and nerve stimulators. For very short stimuli the charge required, $I_{\mathrm{th}}t \to I_{\mathrm{rh}}\tau$, tends to a constant, so short pulses economize charge.

## 4.6. The Action Potential

### 4.6.1. Phases of the Action Potential

**Definition 4.6.1 (Action Potential)** The rapid, reversible, propagating reversal of the membrane potential of an excitable cell on threshold or suprathreshold stimulation is called an **action potential**. It is all-or-none: it does not occur if the stimulus does not reach threshold, and once threshold is reached its amplitude and shape do not change with stimulus strength.

Taking a nerve fiber as the example, the action potential lasts about $1$–$2\,\mathrm{ms}$:

1. Rising phase (depolarization): the membrane potential rises rapidly from the resting level of about $-70\,\mathrm{mV}$, crosses zero (overshoot) and reaches about $+30\,\mathrm{mV}$, taking about $0.5\,\mathrm{ms}$;
2. Falling phase (repolarization): the membrane potential rapidly returns to near the resting level;
3. Afterpotentials: low-amplitude slow potential changes after the spike, first the depolarizing afterpotential (negative afterpotential) while the membrane potential has not yet fully repolarized, then the hyperpolarizing afterpotential (positive afterpotential) more negative than the resting potential, which can last a few to a few tens of milliseconds.

The spike (rising and falling phases) is the main body of the action potential, and the spike conducted along a nerve fiber is the nerve impulse. The shape of the action potential reflects the function of the cell: that of neurons is short and sharp, suited to high-frequency coding; that of ventricular muscle has a plateau of about $200\,\mathrm{ms}$, ensuring the rhythm of contraction and relaxation (Chapter 13). The waveform is determined by several parameters and several processes and therefore has several points of regulation.

### 4.6.2. Ionic Mechanism

The basic structure of the action potential is one positive feedback and one **negative feedback**.

- Depolarization: when the membrane is depolarized to threshold (about $-55\,\mathrm{mV}$ in nerve fibers and skeletal muscle, between about $-60$ and $-45\,\mathrm{mV}$ depending on the cell type), voltage-gated $\ce{Na+}$ channels open rapidly and $\ce{Na+}$ flows in quickly, driven by its electrochemical gradient (inward current), so the membrane potential rises toward $E_{\mathrm{Na}}$; the channels inactivate automatically in less than $1\,\mathrm{ms}$ after opening. $\ce{Na+}$ channels can be blocked by tetrodotoxin (TTX).
- Repolarization: voltage-gated $\ce{K+}$ channels open with a delay after depolarization (opening progressively once the membrane is depolarized beyond about $-40\,\mathrm{mV}$, more so the stronger the depolarization), $\ce{K+}$ flows out (outward current) and the membrane potential falls; these channels stay open until the membrane potential has returned to negative values and only then close. $\ce{K+}$ channels can be blocked by tetraethylammonium (TEA).
- Afterpotentials: $\ce{K+}$ channels close rather slowly, so after repolarization the $\ce{K+}$ conductance is still above the resting level and the membrane potential is temporarily closer to $E_{\mathrm{K}}$, forming the hyperpolarizing afterpotential; the electrogenic action of the Na⁺/K⁺-ATPase also contributes.

The coordination in time of the positive feedback of $\ce{Na+}$ conductance (opening → depolarization → more opening) with two negative feedbacks (inactivation of $\ce{Na+}$ channels, delayed opening of $\ce{K+}$ channels) determines the "fast up, fast down" shape of the action potential.

### 4.6.3. Refractory Periods

**Definition 4.6.2 (Absolute and Relative Refractory Periods)** For a period after an excitation, no stimulus however strong can evoke another action potential; this is called the **absolute refractory period**. In the period that follows, only a suprathreshold stimulus can evoke an action potential (and one of smaller amplitude); this is called the **relative refractory period**.

The absolute refractory period corresponds to the duration of the spike: $\ce{Na+}$ channels are in the inactivated state and must first repolarize and recover from inactivation ("reactivate") before they can open again, so spikes cannot sum. In the relative refractory period some $\ce{Na+}$ channels have recovered but their number is still insufficient and the $\ce{K+}$ conductance is still high, so the threshold is raised. The absolute refractory period determines the maximum number of action potentials a cell can produce per unit time: about $0.5$–$1\,\mathrm{ms}$ in mammalian myelinated nerve fibers (in theory more than 1000 per second, in practice sustained firing rarely exceeds a few hundred per second), about $2$–$5\,\mathrm{ms}$ in skeletal muscle, and as long as $200$–$250\,\mathrm{ms}$ in ventricular muscle, so that cardiac muscle cannot undergo **tetanic contraction** (Chapter 13). The refractory period also ensures unidirectional propagation of the action potential along the axon: a region that has just been excited is refractory and cannot be excited again by the local current from ahead.

After the relative refractory period some cells have a supernormal period: the negative afterpotential brings the membrane potential closer to threshold, while $\ce{Na+}$ channels have essentially reactivated, so even a subthreshold stimulus can cause excitation; this is followed by a subnormal period: the positive afterpotential hyperpolarizes the membrane, the activity of the Na⁺/K⁺-ATPase is enhanced, and excitability is below normal.

### 4.6.4. $\ce{Ca^2+}$ Action Potentials

$\ce{Ca^2+}$ can also form action potentials. The cytosolic $[\ce{Ca^2+}]$ is about $100\,\mathrm{nmol\,L^{-1}}$ and the extracellular concentration about $1\,\mathrm{mmol\,L^{-1}}$, so $E_{\mathrm{Ca}}$ is as high as $+120\,\mathrm{mV}$ or more, and the opening of voltage-gated $\ce{Ca^2+}$ channels produces an inward cation current. $\ce{Ca^2+}$ channels coexist with $\ce{Na+}$ channels or replace them, and their activation and inactivation are about 10 times slower than those of $\ce{Na+}$ channels, so $\ce{Ca^2+}$ action potentials are broader and rise more slowly. They dominate the depolarization of certain cells: many smooth muscles, cells of the **sinoatrial node** and atrioventricular node of the heart (Chapter 13), the plateau of ventricular muscle, and the dendrites and axon terminals of neurons. $\ce{Ca^2+}$ is at once an electrical and a chemical signal: the $\ce{Ca^2+}$ that enters directly triggers contraction, secretion and gene expression. Disturbance of $\ce{Ca^2+}$ **homeostasis** (such as increased $\ce{Ca^2+}$ influx at rest) can induce spontaneous depolarization and abnormal rhythms.

### 4.6.5. Comparison of Nerve and Skeletal Muscle

| Parameter | Nerve fiber (mammalian) | Skeletal muscle fiber |
|---|---|---|
| Resting potential | $-70\,\mathrm{mV}$ | $-85$ to $-90\,\mathrm{mV}$ |
| Threshold potential | About $-55\,\mathrm{mV}$ | About $-55$ to $-60\,\mathrm{mV}$ |
| Overshoot | About $+30$–$+40\,\mathrm{mV}$ | About $+30$–$+40\,\mathrm{mV}$ |
| Spike duration | $0.5$–$2\,\mathrm{ms}$ | $2$–$5\,\mathrm{ms}$ |
| Absolute refractory period | $0.5$–$1\,\mathrm{ms}$ | $2$–$5\,\mathrm{ms}$ |
| Conduction velocity | $0.5$–$120\,\mathrm{m\,s^{-1}}$ | $3$–$5\,\mathrm{m\,s^{-1}}$ |
| Dominant resting conductance | $\ce{K+}$ | $\ce{Cl-}$ (about $70\%$) and $\ce{K+}$ |
| Special structures | Myelin sheath and nodes of Ranvier | T tubules carry the action potential deep into the fiber (Chapter 8) |

## 4.7. Studying the Action Potential: From the Compound Action Potential to Hodgkin–Huxley

### 4.7.1. Erlanger and Gasser: Compound Action Potentials and Fiber Classification

In the 1920s Joseph Erlanger and Herbert Gasser recorded the electrical activity of nerve trunks with an improved cathode-ray oscilloscope and resolved potential changes on the millisecond scale for the first time. They found that after stimulating a nerve trunk, what was recorded at a distance was not one wave but several peaks arriving in succession.

**Definition 4.7.1 (Compound Action Potential)** The potential recorded with extracellular electrodes, formed by the summation of the action potentials of many nerve fibers in a nerve trunk, is called the **compound action potential**. Unlike the action potential of a single fiber, its amplitude increases in a graded way with stimulus strength (more and more fibers are excited) and at a distance divides into several peaks (different fibers conduct at different velocities).

**Definition 4.7.2 (Conduction Velocity)** The speed at which an action potential propagates along a nerve fiber is called the **conduction velocity**, equal to the distance between two recording points divided by the difference in arrival time of the action potential.

Conduction velocity is related to the diameter of the fiber and to myelination. On this basis Erlanger and Gasser divided the nerve fibers of vertebrates into three classes, A, B and C, class A being further divided into α, β, γ and δ, and received the 1944 Nobel Prize in Physiology or Medicine for it. This work turned the action potential from an abstract phenomenon into a system that could be classified and measured, and related the structure of fibers (diameter, myelin) to conduction velocity and function. There is another classification of sensory afferent fibers by diameter (Lloyd and Hunt, classes I–IV), and the two are often used together.

| Type | Diameter/µm | Myelin | Conduction velocity/(m s⁻¹) | Function |
|---|---|---|---|---|
| Aα (Ia, Ib) | $12$–$20$ | Yes | $70$–$120$ | Skeletal motor neurons, afferents from **muscle spindles** and **tendon organs** |
| Aβ (II) | $6$–$12$ | Yes | $30$–$70$ | Afferents for cutaneous touch and pressure |
| Aγ | $3$–$6$ | Yes | $15$–$30$ | γ motor neurons innervating intrafusal fibers |
| Aδ (III) | $1$–$5$ | Yes | $5$–$30$ | **Fast pain**, cold |
| B | $< 3$ | Yes | $3$–$15$ | Autonomic preganglionic fibers |
| C (IV) | $0.2$–$1.5$ | No | $0.5$–$2$ | **Slow pain**, warmth, autonomic postganglionic fibers |

### 4.7.2. The Squid Giant Axon and the Voltage Clamp

Mammalian nerve fibers are too thin to insert electrodes into. In 1936 J. Z. Young discovered and popularized the giant axon of the squid: it is the efferent fiber of the circuit that contracts the mantle and expels water for escape, up to $0.5\,\mathrm{mm}$ in diameter, into which a wire electrode can be inserted lengthwise and from which the axoplasm can be squeezed out and replaced with perfusate. In 1939 Hodgkin and Huxley first recorded an action potential from the giant axon with an intracellular electrode and found that the peak exceeded zero potential by about $40\,\mathrm{mV}$, refuting Bernstein's "potential vanishes" idea. In 1949 Hodgkin and Katz showed that the amplitude of the overshoot varies with the logarithm of the extracellular $[\ce{Na+}]$ and proposed that the action potential is caused by a transient rise in $\ce{Na+}$ permeability.

The key technique was the **voltage clamp** (developed by Cole and Marmont, refined by Hodgkin, Huxley and Katz): one electrode measures the membrane potential, a feedback amplifier compares it with a set command voltage and, within microseconds, injects an opposing current through another electrode so that the membrane potential is held constant. The injected current equals the membrane current in magnitude and is opposite in sign. The voltage clamp separates "voltage change" from "ionic current": at a fixed voltage the capacitive current appears only at the instant of the step, and what is measured afterward is the pure ionic current, so the dependence of ionic conductances on time and voltage can be studied separately.

TTX and TEA were not available then, and Hodgkin and Huxley separated the currents by ion substitution: replacing most of the extracellular $\ce{Na+}$ with choline shifted $E_{\mathrm{Na}}$, the early inward current changed and the late outward current did not, so that the total current was resolved into a $\ce{Na+}$ current and a $\ce{K+}$ current. Later pharmacological experiments confirmed this resolution: TTX abolishes the early inward current and TEA the late outward current. When the peak current is plotted against clamp voltage, the current–voltage curve of the $\ce{Na+}$ current has a segment of negative slope near threshold: depolarization increases the inward current, which is the electrical expression of positive feedback and the reason a threshold exists.

In the summer of 1947 Hodgkin and Katz measured the effect of extracellular $\ce{Na+}$ on the overshoot at Plymouth; in 1948 Hodgkin, Huxley and Katz got the feedback amplifier of the voltage clamp working, published a short preliminary paper, and spent a long time improving the equipment. In the summer of 1949 they returned to Plymouth and completed within about a month nearly all the experiments of the five papers of 1952. Hodgkin recalled that they could work so fast and leave so few gaps because they had earlier spent a long time thinking and calculating "what kind of system could produce an action potential like that of squid nerve" and knew what had to be measured to reconstruct it; the whole model rested on a few dozen experiments on a handful of giant axons.

### 4.7.3. The Conclusions of Hodgkin and Huxley

The main conclusions of Hodgkin and Huxley (1952) (equations, parameters and simulation in [7.6.30](/7.6.30)):

1. The action potential is produced by $\ce{Na+}$ influx followed by $\ce{K+}$ efflux;
2. The $\ce{Na+}$ conductance activates quickly and inactivates quickly; the $\ce{K+}$ conductance activates with a delay and does not inactivate in the squid axon;
3. Both conductances can be written as the product of a maximal conductance and several gating variables: $g_{\mathrm{Na}} = \bar g_{\mathrm{Na}}m^3h$, $g_{\mathrm{K}} = \bar g_{\mathrm{K}}n^4$. $m$ is the activation gate of the $\ce{Na+}$ channel (opening quickly on depolarization), $h$ is the inactivation gate (closing slowly on depolarization), and $n$ is the activation gate of the $\ce{K+}$ channel (opening slowly on depolarization); each gate switches between open and closed with voltage-dependent rates. This description predicted that channels consist of several independently moving subunits (voltage sensors), which later molecular structures confirmed;
4. This set of differential equations quantitatively reconstructs the shape, threshold, refractory period and conduction velocity of the action potential (calculated $18.8\,\mathrm{m\,s^{-1}}$, measured $21.2\,\mathrm{m\,s^{-1}}$).

The gating variables explain the phenomena above: the threshold is the potential at which the inward current caused by the opening of $m$ begins to exceed the outward current; the refractory period is the period in which $h$ has not yet recovered and $n$ has not yet closed; the positive afterpotential comes from the slow closing of $n$; prolonged subthreshold depolarization closes $h$ and lowers excitability (accommodation and conduction block caused by "sodium channel inactivation"). For this Hodgkin and Huxley shared the 1963 Nobel Prize with Eccles. Their model laid the foundation of membrane electrophysiology, supplied the theoretical framework for the later molecular biology of ion channels, and is the starting point of all later neuron models (integrate-and-fire models, multicompartment models and so on) ([7.16](/7.16)).

## 4.8. Energy for Rebuilding the Na⁺ and K⁺ Gradients

After each action potential, the Na⁺/K⁺-ATPase pumps out the $\ce{Na+}$ that entered and pumps back the $\ce{K+}$ that left. By Example 4.3.2, the minimum number of ions required is determined by membrane capacitance and potential change; the $\ce{Na+}$ that actually enters exceeds the minimum, because during the rising phase $\ce{K+}$ efflux already cancels part of the $\ce{Na+}$ influx: about 4 times the minimum in the cold squid axon, and only about 1.3 times in mammalian axons at body temperature, whose $\ce{Na+}$ channels inactivate faster and whose $\ce{K+}$ channels open later, for more efficient use of energy.

The Na⁺/K⁺-ATPase itself has a high thermodynamic efficiency: in skeletal muscle the work done in pumping out 3 $\ce{Na+}$ and pumping in 2 $\ce{K+}$ is more than $80\%$ of the free energy of hydrolysis of one ATP ([7.6.30](/7.6.30)). Counting from the oxidation of glucose (the efficiency of ATP synthesis by **oxidative phosphorylation** is itself about $40\%$–$60\%$), the overall efficiency of rebuilding the $\ce{Na+}$ and $\ce{K+}$ gradients is about $30\%$–$55\%$, comparable to an efficient heat engine; the rest of the energy becomes heat. This is one source of the heat produced by neural activity and the main reason the brain consumes about $20\%$ of the resting oxygen consumption of the whole body: most of the brain's energy goes to restoring ion gradients after action potentials and synaptic currents. The high energy cost limits the firing frequency the nervous system can sustain, and the "cost per action potential" has therefore become a constraint on neural coding and axon design.

## 4.9. Conduction of the Action Potential

### 4.9.1. The Passive Cable

After an action potential is generated at one place, the excited region is positive inside and negative outside, a potential difference forms between it and the neighboring resting region, and a local current is produced: inside the membrane it flows from the excited to the unexcited region, outside it flows the other way. This current depolarizes the neighboring region, which on reaching threshold produces a new action potential, and so the action potential advances stage by stage (local current theory). The strength of the local current is usually several times that needed to cause excitation (the **safety factor**), so conduction is reliable, and amplitude and shape are unchanged in long-distance conduction.

The spread of local current along the axon follows the **cable equation**. The axon is treated as a leaky cable: the resistance of the extracellular fluid $r_{\mathrm{o}}$ (usually very small and negligible), the axial resistance of the intracellular fluid $r_{\mathrm{i}}$, and the membrane resistance $r_{\mathrm{m}}$ and capacitance $c_{\mathrm{m}}$ (all per unit length). With constant current injection, the change of membrane potential decays exponentially from the injection point to both sides,
$$
V(x) = V_0\,\mathrm{e}^{-\lvert x\rvert/\lambda}, \qquad \lambda = \sqrt{\frac{r_{\mathrm{m}}}{r_{\mathrm{i}}}} = \sqrt{\frac{aR_{\mathrm{m}}}{2R_{\mathrm{i}}}}, \tag{4.6}
$$
where the **length constant** $\lambda$ is the distance over which the potential decays to $1/\mathrm{e}$, $a$ is the axon radius, $R_{\mathrm{m}}$ the membrane resistance per unit area and $R_{\mathrm{i}}$ the resistivity of the cytoplasm; the time course of the potential change is determined by the **time constant** $\tau_{\mathrm{m}} = R_{\mathrm{m}}C_{\mathrm{m}}$. Passive spread is bidirectional and decremental: $\lambda$ of the squid giant axon is about $6\,\mathrm{mm}$ and of a fine dendrite about $1\,\mathrm{mm}$, so a signal cannot propagate passively for a meter ([7.6.30](/7.6.30)). The passive model cannot fully explain the action potential, and conduction over long distances requires the membrane everywhere to regenerate the signal continually.

### 4.9.2. Two Strategies for Speeding Up: Giant Axons and Myelin

The conduction velocity of an action potential depends on how far ahead, and how quickly, the local current can charge the membrane to threshold. By dimensional analysis of the cable equation, the conduction velocity is $v \sim \lambda/\tau_{\mathrm{m}}$ (times a dimensionless factor determined by channel kinetics),
$$
\frac{\lambda}{\tau_{\mathrm{m}}} = \frac{1}{C_{\mathrm{m}}}\sqrt{\frac{a}{2R_{\mathrm{i}}R_{\mathrm{m}}}}. \tag{4.7}
$$
There are three ways to raise the conduction velocity and slow the decay of potential with distance: raising the membrane resistance per unit area $R_{\mathrm{m}}$, lowering the cytoplasmic resistivity $R_{\mathrm{i}}$, and increasing the axon radius $a$. The cytoplasmic resistivity is determined by ionic composition and hard to change, so two strategies evolved.

- Thickening the axon (increasing $a$): $\lambda \propto \sqrt a$ while $\tau_{\mathrm{m}}$ is independent of $a$, so the conduction velocity of an unmyelinated axon is $v \propto \sqrt a$. The giant axons of squid, earthworm and crayfish take this route, at the cost of volume: to raise the speed 10-fold the diameter must increase 100-fold.
- Wrapping in myelin: Schwann cells (peripheral nerves) or oligodendrocytes (central nervous system) wrap their own membrane around the axon in several tens to more than a hundred layers, forming the myelin sheath, and leave bare gaps about $1\,\mu\mathrm{m}$ wide, the nodes of Ranvier, every $0.2$–$2\,\mathrm{mm}$ (about 100 times the fiber diameter). A myelin sheath of $N$ layers is equivalent to $2N$ membranes in series: the membrane resistance of the internodal region increases about $2N$-fold and the capacitance falls to about $1/(2N)$. By Eq. (4.7), if only $R_{\mathrm{m}}$ increased, $\lambda$ would increase but $\tau_{\mathrm{m}}$ would increase equally and the speed would actually fall; the key point of myelin is that it lowers the capacitance at the same time: $\tau_{\mathrm{m}} = R_{\mathrm{m}}C_{\mathrm{m}}$ is almost unchanged, $\lambda$ increases $\sqrt{2N}$-fold, and the charge needed for charging falls to $1/(2N)$, so "high $R_{\mathrm{m}}$, low $C_{\mathrm{m}}$" lets the signal travel both far and fast.

### 4.9.3. Saltatory Conduction

The voltage-gated $\ce{Na+}$ channels of myelinated fibers are highly concentrated at the nodes of Ranvier (densities up to thousands per square micrometer) and almost absent in the internodes. The action potential is generated only at nodes, the internodal region is crossed quickly by passive local current, and excitation "jumps" from one node to the next; this is **saltatory conduction**. It has two benefits: the conduction velocity is greatly increased; and because ions cross the membrane only at nodes and the charge needed to charge the internode is very small, the burden on the Na⁺/K⁺-ATPase is light and the energy cost is greatly reduced. The current arriving from one node at the next is usually still far above threshold, so conduction continues even if one or two damaged nodes are skipped, giving a high safety factor. Unidirectional propagation of the action potential is ensured by the refractory period of the node just excited.

In myelinated fibers the time for a node to reach threshold after current arrives from ahead is about $20$–$50\,\mu\mathrm{s}$, independent of diameter, while the internodal distance is proportional to diameter, so the conduction velocity of myelinated fibers is proportional to diameter, at about $6\,\mathrm{m\,s^{-1}}$ per micrometer of outer diameter (Hursh's rule). The velocity of unmyelinated fibers grows only as $\sqrt d$, and the two curves cross at a very small diameter: by the theoretical estimate of Rushton (1951) the crossover diameter is about $1\,\mu\mathrm{m}$, below which myelination no longer confers a speed advantage, which is roughly the lower limit of the diameter of myelinated fibers in mammalian peripheral nerves (in the central nervous system myelinated axons can be as thin as about $0.2\,\mu\mathrm{m}$, and later estimates also give smaller crossover diameters). A squid giant axon $500\,\mu\mathrm{m}$ in diameter (about $25\,\mathrm{m\,s^{-1}}$) conducts, by Hursh's rule, only as fast as a myelinated fiber of about $4\,\mu\mathrm{m}$ outer diameter; the same cross-sectional area can hold more than ten thousand such myelinated fibers. Demyelinating diseases (multiple sclerosis, Guillain–Barré syndrome) slow or even block conduction, because the exposed internodal membrane has too few $\ce{Na+}$ channels and its capacitance is too large to regenerate the action potential.

![Conduction velocity as a function of fiber diameter (log–log axes). Dashed lines: unmyelinated axons v ∝ √d (taking a mammalian C fiber at 37 °C, about 2 m/s × √(d/µm); animals at lower temperatures lie below it) and vertebrate myelinated fibers v ≈ 6 m/s per micrometer of outer diameter (Hursh's rule). Points are approximate literature values (measured at different temperatures): mammalian C, Aδ, Aβ and Aα fibers; squid giant axon (about 500 µm, about 25 m/s); earthworm giant fibers; crayfish lateral giant fiber; cockroach giant interneuron; myelinated median giant fiber of the penaeid shrimp (about 100 µm, about 200 m/s)](./plots/conduction-velocity.py)

## 4.10. Evolution and Comparison

### 4.10.1. Giant Axons and Escape

Behaviors needing extremely fast responses, such as escape from predators, are carried out by giant axons in many invertebrates. The giant axon of the squid reaches $0.5$–$1\,\mathrm{mm}$ in diameter, formed by the fusion of the axons of many neurons, and conducts at about $20$–$25\,\mathrm{m\,s^{-1}}$, so that the parts of the mantle contract almost simultaneously and expel water in escape; the diameter of the giant axon increases with its length, making contraction of the distal and proximal parts synchronous. The ventral nerve cord of the earthworm has one median giant fiber and two lateral giant fibers (several tens of micrometers in diameter), conducting at about $10$–$30\,\mathrm{m\,s^{-1}}$ and responsible for rapid shortening of the body when the front or the rear is stimulated, respectively; the lateral and medial giant fibers of the crayfish trigger the rapid flick of the tail, and the giant interneurons of the cockroach relay airflow signals sensed by the cerci to the motor centers, causing escape. These circuits put speed first and often use **electrical synapses** (Chapter 5) to shorten delays further.

### 4.10.2. Multiple Origins of Myelin

Myelin is not an invention peculiar to vertebrates. Apart from gnathostomes (lampreys and hagfishes have no myelin), compact or loose myelin-like structures have arisen independently at least in annelids (the multilayered sheath around the giant fibers of earthworms), copepod crustaceans (the compact myelin of calanoid copepods lets them jump away within a few milliseconds) and penaeid shrimps. The myelinated giant fibers of penaeid shrimps have a distinctive structure: there is a gap between the myelin and the axolemma and excitation proceeds through "windows" in the myelin, with a reported conduction velocity above $200\,\mathrm{m\,s^{-1}}$, one of the fastest known nerve conductions. This **convergent evolution** shows that, when body size increases and the demand for response speed rises, "insulation plus nodes" is almost the only solution that cable physics allows.

### 4.10.3. Action Potentials without $\ce{Na+}$

The $\ce{Na+}$ action potential is not the only form of excitable membrane. Voltage-gated $\ce{Ca^2+}$ channels are older than $\ce{Na+}$ channels: the unicellular *Paramecium* uses $\ce{Ca^2+}$ action potentials to control the direction of ciliary beating, so that on hitting an obstacle membrane depolarization causes $\ce{Ca^2+}$ influx, the rise in intracellular $\ce{Ca^2+}$ reverses the cilia, and the cell backs up (the avoidance reaction), linking the **ciliary motility** of Chapter 2 to the electrical signals of this chapter. The genome of *Caenorhabditis elegans* contains no voltage-gated $\ce{Na+}$ channels, and many of its neurons produce only graded potentials; some neurons and muscle cells produce all-or-none action potentials built from L-type $\ce{Ca^2+}$ channels and $\ce{K+}$ channels. The nematode is only about $1\,\mathrm{mm}$ long with short neurites, and graded signals and slow $\ce{Ca^2+}$ signals are sufficient.

The $\ce{Na+}$-selective channels of modern animals very probably evolved from ancestral channels permeable to $\ce{Ca^2+}$: the amino acid combinations by which the $\mathrm{Na_V}$ channels of cnidarians and bilaterians acquired $\ce{Na+}$ selectivity are not the same, suggesting that the transition may have occurred independently more than once. Using $\ce{Na+}$ instead of $\ce{Ca^2+}$ as the main depolarizing ion has clear advantages: $\ce{Na+}$ is at high concentration, currents are large, channel kinetics are fast, and $\ce{Na+}$ is not itself a **second messenger**, so large influx does not disturb intracellular $\ce{Ca^2+}$ signaling.

Plants also have action potentials: in the **stonewort** *Chara* the action potential depolarizes by $\ce{Ca^2+}$-activated $\ce{Cl-}$ efflux and repolarizes by $\ce{K+}$ efflux and lasts several seconds; the trap of the Venus flytrap closes on an action potential triggered by the sensory hairs ([7.13.19](/7.13.19)). The other extreme in animals is the **electric organ**: electric eels and electric rays connect large numbers of electrocytes in series and in parallel, summing the voltage of action potentials to tens to hundreds of volts ([7.6.30](/7.6.30)).

## Summary

| Topic | Relations and values |
|---|---|
| Membrane potential | $V_{\mathrm{m}} = \psi_{\mathrm{i}} - \psi_{\mathrm{o}}$, about $-0.1\,\mathrm{V}$ across $5$–$10\,\mathrm{nm}$; depolarization, hyperpolarization, repolarization, overshoot (Definition 4.2.1) |
| Equilibrium potential (Definition 4.2.2) | $E_{\mathrm{X}} = (RT/zF)\ln([\mathrm{X}]_{\mathrm{o}}/[\mathrm{X}]_{\mathrm{i}})$ (Eq. 4.1), $61.5\,\mathrm{mV}$ per tenfold at $37\,{}^\circ\mathrm{C}$; skeletal muscle $E_{\mathrm{K}} = -95$, $E_{\mathrm{Na}} = +67$, $E_{\mathrm{Ca}} = +123$, $E_{\mathrm{Cl}} = -89\,\mathrm{mV}$ (Example 4.2.1) |
| GHK equation | Eq. (4.2); $\alpha = P_{\mathrm{Na}}/P_{\mathrm{K}}$ makes the curve depart from the Nernst line at low $[\ce{K+}]_{\mathrm{o}}$; reversal potential versus equilibrium potential |
| Na⁺/K⁺-ATPase | Maintains gradients (indirect) + electrogenic (direct, about $-4\,\mathrm{mV}$) |
| Equivalent circuit | $I_{\mathrm{X}} = G_{\mathrm{X}}(V_{\mathrm{m}} - E_{\mathrm{X}})$ (Eq. 4.3); $V_{\mathrm{m}} = \sum(G_{\mathrm{X}}/G_{\mathrm{m}})E_{\mathrm{X}}$ (Eq. 4.4); $C_{\mathrm{m}} \approx 1\,\mu\mathrm{F\,cm^{-2}}$ |
| Number of ions | Setting up $-61.5\,\mathrm{mV}$ takes only about 3800 $\ce{K+}$ per $\mu\mathrm{m^2}$, $0.0027\%$ of the cell's content (Example 4.3.2); fraction $\propto 1/d$ |
| Local potential (Definition 4.4.1) | Graded, summable, decremental, time course set by $\tau_{\mathrm{m}}$; receptor potentials, postsynaptic potentials |
| Excitability and threshold | Excitability (Definition 4.5.1); threshold potential (Definition 4.5.2) $10$–$20\,\mathrm{mV}$ above the resting potential, positive feedback of $\ce{Na+}$; strength–duration $I_{\mathrm{th}} = I_{\mathrm{rh}}/(1 - \mathrm{e}^{-t/\tau})$ (Eq. 4.5), chronaxie $\tau\ln 2$ |
| Action potential (Definition 4.6.1) | All-or-none; $\ce{Na+}$ fast activation and inactivation (TTX), $\ce{K+}$ delayed activation (TEA); refractory periods (Definition 4.6.2), supernormal and subnormal periods; $\ce{Ca^2+}$ action potentials about 10 times slower |
| History | Compound action potential (Definition 4.7.1) and A, B, C fibers; conduction velocity (Definition 4.7.2); giant axon, voltage clamp, ion substitution; $m^3h$ and $n^4$ |
| Energy | Actual $\ce{Na+}$ entry is $1.3$–$4$ times the minimum; pump efficiency $> 80\%$, from glucose $30\%$–$55\%$ |
| Conduction | $\lambda = \sqrt{aR_{\mathrm{m}}/2R_{\mathrm{i}}}$ (Eq. 4.6), $v \sim \lambda/\tau_{\mathrm{m}}$ (Eq. 4.7); unmyelinated $v \propto \sqrt d$, myelinated $v \approx 6\,\mathrm{m\,s^{-1}}$ per µm, crossover about $1\,\mu\mathrm{m}$; the key point of myelin is lowered capacitance |
| Evolution | Giant-axon escape circuits; myelin arose independently at least in vertebrates, annelids, copepods and penaeid shrimps; $\ce{Ca^2+}$ action potentials of *Paramecium* and nematodes; *Chara* and the Venus flytrap; electric organs |

## Questions

1. A neuron has $[\ce{K+}]_{\mathrm{i}} = 140$, $[\ce{K+}]_{\mathrm{o}} = 4$, $[\ce{Na+}]_{\mathrm{i}} = 15$ and $[\ce{Na+}]_{\mathrm{o}} = 145\,\mathrm{mmol\,L^{-1}}$, and at rest $P_{\mathrm{Na}}/P_{\mathrm{K}} = 0.04$ (neglect $\ce{Cl-}$). Find $E_{\mathrm{K}}$, $E_{\mathrm{Na}}$ and the resting potential at $37\,{}^\circ\mathrm{C}$. What is the membrane potential at the peak of the action potential if $P_{\mathrm{Na}}/P_{\mathrm{K}} = 20$ there?

   **Answer** $E_{\mathrm{K}} = 61.5\log_{10}(4/140) = -95\,\mathrm{mV}$; $E_{\mathrm{Na}} = 61.5\log_{10}(145/15) = +61\,\mathrm{mV}$. At rest: $61.5\log_{10}[(4 + 0.04\times145)/(140 + 0.04\times15)] = 61.5\log_{10}(9.8/140.6) = -71\,\mathrm{mV}$. At the peak: $61.5\log_{10}[(4 + 20\times145)/(140 + 20\times15)] = 61.5\log_{10}(2904/440) = +50\,\mathrm{mV}$, close to but below $E_{\mathrm{Na}}$. A large change of membrane potential needs only a change in the ratio of permeabilities, not a change in concentrations.

2. Why does perfusion with a high-$\ce{K+}$ solution (such as $[\ce{K+}]_{\mathrm{o}} = 50\,\mathrm{mmol\,L^{-1}}$) make nerve and cardiac muscle lose excitability rather than become persistently excited?

   **Answer** High $[\ce{K+}]_{\mathrm{o}}$ depolarizes the resting potential (to about $-30\,\mathrm{mV}$ from the figure). The depolarization first brings the membrane briefly close to threshold, but sustained depolarization closes the inactivation gates of voltage-gated $\ce{Na+}$ channels ($h \to 0$), which cannot reactivate; fewer and fewer $\ce{Na+}$ channels are available to open, and the threshold rises until no action potential can be produced (depolarizing block). This is the principle of high-potassium cardioplegic solutions.

3. How long does it take an unmyelinated C fiber $1\,\mu\mathrm{m}$ in diameter and a myelinated Aβ fiber $10\,\mu\mathrm{m}$ in diameter each to carry a signal from the toe to the spinal cord ($1\,\mathrm{m}$)? Use the result to explain why a needle prick is felt first as a sharp pain and a little later as burning pain.

   **Answer** A C fiber conducts at about $1\,\mathrm{m\,s^{-1}}$ and takes about $1\,\mathrm{s}$; an Aβ fiber at about $60\,\mathrm{m\,s^{-1}}$ takes about $17\,\mathrm{ms}$. The Aδ fibers that conduct fast pain (about $15\,\mathrm{m\,s^{-1}}$) take about $70\,\mathrm{ms}$. **Fast pain** (Aδ) therefore arrives before **slow pain** (C), about a second apart, giving "double pain sensation" (Chapter 40).

4. Some say that myelin speeds conduction because it "increases the membrane resistance". Use Eq. (4.7) to explain why this is incomplete.

   **Answer** If only $R_{\mathrm{m}}$ were increased $k$-fold, $\lambda$ would increase $\sqrt k$-fold but $\tau_{\mathrm{m}}$ would increase $k$-fold, and $\lambda/\tau_{\mathrm{m}}$ would actually fall by a factor $\sqrt k$: the potential would spread farther but charge more slowly. Myelin at the same time lowers the membrane capacitance to about $1/(2N)$, so $\tau_{\mathrm{m}}$ is essentially unchanged and $\lambda$ increases $\sqrt{2N}$-fold, so that $\lambda/\tau_{\mathrm{m}}$ increases $\sqrt{2N}$-fold; together with the saltatory conduction made possible by the concentration of $\ce{Na+}$ channels at the nodes of Ranvier, the speed is greatly raised. Low capacitance also means that few ions are needed for charging, so the energy cost is low.

5. Using the strength–duration relation (Eq. 4.5), find the chronaxie of a nerve fiber with membrane time constant $0.5\,\mathrm{ms}$, and the ratio of the threshold current to the rheobase for a stimulus lasting $0.1\,\mathrm{ms}$.

   **Answer** The chronaxie is $t_{\mathrm{c}} = \tau\ln 2 = 0.35\,\mathrm{ms}$. At $t = 0.1\,\mathrm{ms}$, $I_{\mathrm{th}}/I_{\mathrm{rh}} = 1/(1 - \mathrm{e}^{-0.2}) = 1/0.181 = 5.5$.

6. (Open question) *Caenorhabditis elegans* has no voltage-gated $\ce{Na+}$ channels, whereas the mammalian nervous system depends heavily on them. From the standpoints of body size, signal distance, energy and the information content of signals, discuss what kind of nervous system suits graded potentials, $\ce{Ca^2+}$ action potentials and $\ce{Na+}$ action potentials respectively.

   **Answer** Key points: when the signal distance is less than a few length constants (below a millimeter), graded potentials can reach the terminal, encode the size of the signal continuously, carry much information and need no threshold, which suits the nematode, the retina and many insect interneurons; over long distances the signal must be regenerated, and all-or-none action potentials, using **frequency encoding**, are noise-resistant and can travel far. $\ce{Ca^2+}$ action potentials are slow with small currents, but $\ce{Ca^2+}$ is itself a signal and can directly trigger contraction and secretion, suiting muscle, secretory cells and neurons over short distances; $\ce{Na+}$ action potentials are fast with large amplitude and, with large diameter or myelin, can reach speeds of a hundred meters per second, suiting long-distance, fast communication in large animals, but each action potential costs energy to restore the ion gradients, and the high energy consumption of the brain is the consequence.
