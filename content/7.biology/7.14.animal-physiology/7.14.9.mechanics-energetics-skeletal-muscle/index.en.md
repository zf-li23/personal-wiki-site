---
title: Mechanics and Energetics of Skeletal Muscle
source_hash: f82ecea152bf
---

[Chapter 8](/7.14.8) ended with the rise of cytosolic $\ce{Ca^2+}$; this chapter deals with what happens after $\ce{Ca^2+}$: skeletal muscle as an engine, how much force it produces, how fast it shortens, how much power it delivers, how much energy it consumes, and how the nervous system regulates these quantities. The core consists of three quantitative relations: the length–tension relationship determined by the geometry of the filaments, the force–velocity relationship (the Hill equation) determined by cross-bridge kinetics, and the grading of force by motor units (the size principle and tetanus). The physics of the molecular motor itself (single-molecule force, step size, the Huxley cross-bridge model) is derived in [7.6.27](/7.6.27), the cell biology of actin and myosin is in [7.3.13](/7.3.13), and the regeneration of ATP is in the metabolism chapters of 7.1; here we use only their conclusions and put the emphasis on the physiology of the whole muscle. The length–tension relationship of cardiac muscle (the Frank–Starling mechanism) returns to the results of this chapter in [Chapter 12](/7.14.12), and the features of cardiac and smooth muscle are in [Chapter 10](/7.14.10).

## 9.1. The Sarcomere

Skeletal and cardiac muscle show alternating light and dark cross-striations under the microscope, which arise from the repeated arrangement of **sarcomeres** within the myofibrils: the region between two Z lines is one sarcomere, about $2$–$2.5\,\mu\mathrm{m}$ long at rest. The composition of the bands and their changes during contraction are described in [7.3.13](/7.3.13#sec-13.5.3). The geometric quantities used in this chapter (frog muscle) are:

| Structure | Length | Composition |
|---|---|---|
| Thick filament | $1.6\,\mu\mathrm{m}$, with a bare zone of about $0.2\,\mu\mathrm{m}$ in the center (no heads) | About 300 molecules of **myosin II**, whose heads (cross-bridges) extend toward the surrounding thin filaments |
| Thin filament | About $1.0\,\mu\mathrm{m}$ projecting from the Z line (about $1.2$–$1.3\,\mu\mathrm{m}$ in humans) | Filamentous **actin**, tropomyosin, troponin; length set by "ruler" proteins such as nebulin |
| Z line | About $0.05\,\mu\mathrm{m}$ thick | Thin filament ends cross-linked by α-actinin |
| Titin | One molecule spans from the Z line to the M line, about $1\,\mu\mathrm{m}$ long | Molecular mass about $3$–$4\,\mathrm{MDa}$, one of the largest proteins; the string of Ig domains and the PEVK region in the I band stretch like a spring |

The sarcomere contains two kinds of force-generating components: the active component is the cross-bridges, and the passive components are titin and extracellular connective tissue. The former requires $\ce{Ca^2+}$ and ATP; the latter produces tension whenever it is stretched. Together they determine the mechanical behavior of muscle (Section 9.3).

## 9.2. The Sliding Filament Theory

**Definition 9.2.1 (Sliding Filament Theory)** The **sliding filament theory** holds that during muscle contraction the lengths of both the thick and thin filaments remain constant, the thin filaments slide toward the center of the sarcomere between the thick filaments, increasing their overlap and shortening the sarcomere; the sliding is driven by the cyclic interaction of the cross-bridges on the thick filaments with the thin filaments.

The evidence came from two papers in the same 1954 issue of *Nature*. A. F. Huxley and Niedergerke used interference microscopy on living frog muscle fibers, and H. E. Huxley and Hanson used phase-contrast microscopy on isolated myofibrils; both found that during contraction the width of the A band does not change while the I band and the H zone narrow, and when the muscle is stretched the A band is still unchanged while the I band and H zone widen. The width of the A band is the length of the thick filaments, so the thick filaments do not shorten; the changes in the I band and H zone show that what changes is the overlap of the two kinds of filaments. Electron microscopy and X-ray diffraction subsequently confirmed that the lengths of both filaments remain constant during contraction. (H. E. Huxley had studied physics as an undergraduate and during the Second World War tested airborne radar in the Royal Air Force; he later brought techniques of electronics and X-ray diffraction into muscle research.)

The sliding filament theory made testable predictions:

1. the force is proportional to the number of cross-bridges able to work between the thick and thin filaments;
2. the number of working cross-bridges is proportional to the length of overlap of the thin filament with the part of the thick filament bearing heads;
3. with no overlap there is no active tension.

These predictions were confirmed quantitatively in 1966 by Gordon, A. F. Huxley and Julian (Section 9.3). Actin–myosin sliding is not unique to muscle: the contraction of the cell cortex, the contractile ring of cytokinesis and cytoplasmic streaming in plants all rely on the same sliding, and the sliding between microtubules and kinesin or dynein drives the bending of cilia and the elongation of the spindle ([7.3.14](/7.3.14)).

## 9.3. The Length–Tension Relationship

### 9.3.1. The Curve Calculated from Geometry

A single muscle fiber is fixed at different lengths, stimulated tetanically, and the tension it produces is measured:

**Definition 9.3.1 (Length–Tension Relationship)** The relationship between the active tension produced by a muscle (or sarcomere) in isometric contraction and its length, at different initial lengths, is called the **length–tension relationship**. The length at which the maximal active tension is produced is called the optimal length.

Gordon, Huxley and Julian (1966) clamped the sarcomere length in the middle segment of the fiber by an optical method (to prevent the sarcomeres at the ends of the fiber from being stretched first) and obtained a curve made up of straight segments, each of whose break points can be calculated from the filament lengths. Let the thick filament length be $L_{\mathrm{A}} = 1.6\,\mu\mathrm{m}$, the bare zone $b = 0.2\,\mu\mathrm{m}$, the thin filament together with half a Z line $L_{\mathrm{I}} = 1.025\,\mu\mathrm{m}$, and the sarcomere length $s$.

**Proposition 9.3.1 (Break Points of the Length–Tension Curve)** With the above geometry, the active tension $T(s)$ (with the maximum taken as 1) satisfies:

1. $T = 0$ for $s \ge L_{\mathrm{A}} + 2L_{\mathrm{I}} = 3.65\,\mu\mathrm{m}$;
2. for $2L_{\mathrm{I}} + b = 2.25\,\mu\mathrm{m} \le s \le 3.65\,\mu\mathrm{m}$, $T$ falls linearly with $s$:
$$
T(s) = \frac{3.65 - s}{3.65 - 2.25}; \tag{9.1}
$$
3. $T = 1$ (plateau) for $2L_{\mathrm{I}} = 2.05\,\mu\mathrm{m} \le s \le 2.25\,\mu\mathrm{m}$;
4. for $s < 2.05\,\mu\mathrm{m}$, $T$ falls; at $s \approx L_{\mathrm{A}} + 0.05 = 1.65\,\mu\mathrm{m}$ the thick filament abuts the Z line and the fall steepens, reaching zero at about $1.27\,\mu\mathrm{m}$.

**Proof** In half a sarcomere, the distance from the end of the thin filament to the M line is $s/2 - L_{\mathrm{I}}$. (1) When it exceeds the half-length of the thick filament, $L_{\mathrm{A}}/2 = 0.8\,\mu\mathrm{m}$, the two kinds of filaments do not overlap at all, that is, $s > 2(0.8 + 1.025) = 3.65\,\mu\mathrm{m}$. (2) When the end of the thin filament lies over the part of the thick filament bearing heads, that is, $b/2 \le s/2 - L_{\mathrm{I}} \le L_{\mathrm{A}}/2$, the number of heads overlapping the thin filament is proportional to $L_{\mathrm{A}}/2 - (s/2 - L_{\mathrm{I}})$, which changes linearly with $s$ and reaches all the heads, $(L_{\mathrm{A}} - b)/2$, at $s = 2L_{\mathrm{I}} + b = 2.25\,\mu\mathrm{m}$; Eq. (9.1) follows from predictions 1 and 2. (3) Once the end of the thin filament enters the bare zone, further shortening does not increase the overlap with heads and the tension is unchanged, until the thin filaments from the two sides meet at the M line ($s = 2L_{\mathrm{I}} = 2.05\,\mu\mathrm{m}$). (4) At shorter lengths the thin filaments pass the M line into the other half-sarcomere and interfere with the thin filaments there (double overlap), hindering the work of the cross-bridges; after the thick filament abuts the Z line it must also be compressed, and the tension falls rapidly. The first three segments follow rigorously from the geometry; the shape of the fourth requires additional mechanisms (see below) and is an experimental result. $\square$

![Length–tension relationship calculated from the filament geometry. A: active isometric tension of frog muscle (solid line): plateau at 2.05–2.25 µm, descending limb reaching zero at 3.65 µm (Eq. (9.1)), ascending limb steepening at 1.65 µm (thick filament abutting the Z line); the diagrams above show the arrangement of the filaments at the numbered points (thin filaments red, thick filaments purple). Dashed line: the same geometry with the longer human thin filament (about 1.27 µm), with the plateau shifted to 2.6–2.8 µm and the descending limb reaching zero at about 4.2 µm. B: tension of the whole muscle: active tension plus the passive tension of titin and connective tissue (schematic exponential curve); on the descending limb active tension falls faster than passive tension rises, so the total tension has a region in which it decreases with stretch](./plots/length-tension.py)

The close agreement of the descending limb with the geometric prediction is the strongest quantitative evidence for the sliding filament theory. The origin of the ascending limb is more complex: besides the double overlap of the thin filaments and the compression of the thick filaments, the lattice spacing of the filaments increases as the sarcomere shortens and the sensitivity of troponin to $\ce{Ca^2+}$ decreases (length-dependent activation), especially at submaximal activation. The latter mechanism is particularly important in cardiac muscle and is the cellular basis of the Frank–Starling mechanism ([Chapter 12](/7.14.12)).

Filament lengths differ among species, and so does the optimal length: the thin filaments of humans are longer and the optimal sarcomere length is about $2.6$–$2.8\,\mu\mathrm{m}$. In the body, most muscles work near the plateau and on the ascending limb, and the leverage of the skeleton and the range of joint movement mean that sarcomeres are rarely stretched to the far end of the descending limb.

### 9.3.2. Passive Tension and Preload

When a muscle is stretched beyond its resting length it produces tension even when not stimulated, mainly from titin and secondarily from connective tissue such as the endomysium and perimysium (panel B). Passive tension ensures that stretched sarcomeres spring back to their original length and keeps the thick filaments in the center of the sarcomere; cardiac muscle expresses shorter, stiffer titin isoforms, and its passive tension rises steeply at shorter sarcomere lengths, preventing overfilling of the ventricles ([Chapter 10](/7.14.10)).

**Definition 9.3.2 (Preload)** The load borne by a muscle before contraction, which determines its initial length, is called the **preload**.

On the length–tension curve the preload determines the point from which the muscle begins to contract: when the preload brings the initial length close to the optimal length the contractile force is greatest, and a preload that is too small or too large reduces it.

## 9.4. The Cross-Bridge Cycle and the Ca²⁺ Switch

### 9.4.1. The Cross-Bridge

The myosin head is both a motor and an ATPase. Each **cross-bridge cycle** ([7.3.13](/7.3.13#def-13.5.3)) hydrolyzes one ATP: ATP binding detaches the head from actin, hydrolysis recocks the lever arm, phosphate release triggers the **power stroke**, in which the swing of the lever arm moves the thin filament about $5$–$10\,\mathrm{nm}$, and after ADP release the head returns to the tightly bound rigor state. Optical trap measurements give a force of about $3$–$5\,\mathrm{pN}$ and a stroke of about $5$–$11\,\mathrm{nm}$ for a single myosin II head (Finer, Simmons and Spudich, 1994). The **duty ratio** of skeletal muscle myosin is very low (only a few percent to ten-odd percent of the cycle is spent strongly bound), so large numbers of heads in parallel do not drag on one another.

**Example 9.4.1 (Orders of Magnitude from Molecule to Muscle)** Lifting a $10\,\mathrm{kg}$ object takes about $100\,\mathrm{N}$. If each attached head produces about $4\,\mathrm{pN}$, the number of simultaneously attached heads is $100/(4\times10^{-12}) \approx 2.5\times10^{13}$; allowing for the duty ratio, the number of heads participating in the cycle in the muscle is another order of magnitude larger (consistent with the estimate in [7.6.27](/7.6.27#ex-27.1.2)). As for speed, a sarcomere can shorten by at most about $1\,\mu\mathrm{m}$, but a $10\,\mathrm{cm}$ fiber has about $4\times10^4$ sarcomeres in series, and the two halves of each sarcomere slide simultaneously, so a filament sliding speed of only a few micrometers per second lets the fiber shorten at several fiber lengths per second. Heads in parallel add force, and sarcomeres in series add velocity: this is the starting point of the structural design of muscle in Section 9.10.

### 9.4.2. The Ca²⁺ Switch on the Thin Filament

The contraction of skeletal and cardiac muscle is regulated at the thin filament. Every 7 actin subunits are associated with one tropomyosin and one troponin complex: troponin C (TnC) binds $\ce{Ca^2+}$, troponin I (TnI) inhibits the actomyosin interaction, and troponin T (TnT) anchors the complex to tropomyosin. At rest tropomyosin blocks the myosin-binding sites on actin; after $\ce{Ca^2+}$ binds TnC, TnI releases actin, tropomyosin slides into the groove of the actin helix, the sites are exposed, and the cross-bridge cycle begins. The thin filament switches among three states, "blocked, closed and open" (McKillop and Geeves, 1993): bound cross-bridges themselves also push tropomyosin and make neighboring sites open more readily, so activation is cooperative.

The steady-state force–$\ce{Ca^2+}$ relationship can be described by the **Hill equation**:

$$
\frac{F}{F_{\max}} = \frac{[\ce{Ca^2+}]^{n}}{K^{n} + [\ce{Ca^2+}]^{n}}, \tag{9.2}
$$
with $n \approx 2$–$5$ in skeletal muscle and a half-activation concentration of about $1$–$3\,\mu\mathrm{mol\,L^{-1}}$ ($\mathrm{p}\ce{Ca}_{50} \approx 5.5$–$6$). The steep cooperativity makes the muscle go from fully relaxed to fully activated when $\ce{Ca^2+}$ changes by only a few-fold, like a switch; and at rest $\ce{Ca^2+}$ at $0.1\,\mu\mathrm{mol\,L^{-1}}$ produces almost no tension.

## 9.5. Forms of Contraction and Load

When stimulated, a muscle always tends to pull its two attachment points closer; whether it shortens depends on the load.

**Definition 9.5.1 (Isometric and Isotonic Contraction)** A contraction in which the muscle length remains unchanged and only the tension increases is called an **isometric contraction**; a contraction in which the tension remains constant (equal to the load) while the length shortens is called an **isotonic contraction**.

Maintaining posture is mainly isometric contraction, and bodily movement is mostly a combination of the two. A muscle that is stretched by an external force while actively contracting (the quadriceps in descending stairs, cushioning a landing) is said to undergo eccentric contraction: it can produce a force up to 1.5–1.8 times the isometric tension while consuming much less ATP, because the cross-bridges are pulled off rather than completing the cycle; but it is also the form most liable to cause microdamage of muscle fibers and delayed-onset muscle soreness after exercise.

**Definition 9.5.2 (Afterload)** The load encountered by a muscle only after it has begun to contract is called the **afterload**.

Under an afterload, contraction has two phases: first an isometric phase, in which the tension rises until it equals the afterload; then an isotonic phase, in which the muscle shortens at constant tension. The larger the afterload, the longer the isometric phase, the later shortening begins, and the lower the speed and extent of shortening; when the afterload equals the maximal isometric tension the muscle cannot shorten.

These phenomena can be understood with Hill's three-element model: a force-generating contractile element (the cross-bridges), a series elastic element in series with it (tendon, the elasticity of the cross-bridges themselves), and a parallel elastic element in parallel with both (titin, connective tissue). In isometric contraction the contractile element shortens and stretches the series elastic element while the external length is unchanged; under an afterload the muscle does not move the load until the tension reaches the load, because all the shortening of the contractile element is taken up by the series elastic element.

## 9.6. The Force–Velocity Relationship and Power

### 9.6.1. The Hill Equation

A. V. Hill (1938) measured the shortening velocity and heat production of the frog sartorius under different afterloads and obtained the **Hill's force–velocity relation** (for its derivation and its interpretation by the Huxley cross-bridge model see [7.6.27](/7.6.27#sec-27.7.1)):

$$
(F + a)(v + b) = b(F_0 + a), \qquad v = b\,\frac{F_0 - F}{F + a}, \tag{9.3}
$$
where $F_0$ is the maximal isometric tension, $v_{\max} = bF_0/a$ is the maximal shortening velocity with no load, and $a$ and $b$ are constants; the curvature is described by $\alpha = a/F_0$, which is about $0.15$–$0.4$ in vertebrate skeletal muscle and smaller in slow muscle (a more curved relation). Written in dimensionless form with $f = F/F_0$, $v/v_{\max} = \alpha(1 - f)/(f + \alpha)$.

The trade-off between force and velocity arises from cross-bridge kinetics: the faster the shortening, the shorter the time each head spends in the attached, force-generating state, and the more heads are carried to positions where they produce resistance, so both the mean number of attached heads and the force per head decrease.

### 9.6.2. Maximum Power

**Proposition 9.6.1 (Point of Maximum Power)** According to Eq. (9.3), the power $P = Fv$ attains its maximum at
$$
f^{*} = \sqrt{\alpha^2 + \alpha} - \alpha, \tag{9.4}
$$
where $v/v_{\max} = f^{*}$ and $P_{\max} = (f^{*})^2F_0v_{\max}$.

**Proof** $P/(F_0v_{\max}) = \alpha f(1 - f)/(f + \alpha)$. Differentiating with respect to $f$ and setting the derivative to zero, $(1 - 2f)(f + \alpha) - f(1 - f) = 0$, that is, $f^2 + 2\alpha f - \alpha = 0$, whose positive root is Eq. (9.4). Substituting back into $v/v_{\max} = \alpha(1 - f^{*})/(f^{*} + \alpha)$ and using $(f^{*})^2 + 2\alpha f^{*} = \alpha$, we get $\alpha(1 - f^{*}) = \alpha - \alpha f^{*} = (f^{*})^2 + \alpha f^{*} = f^{*}(f^{*} + \alpha)$, so $v/v_{\max} = f^{*}$ and $P_{\max} = f^{*}\cdot f^{*}F_0v_{\max}$. $\square$

For $\alpha = 0.25$, $f^{*} = 0.31$ and $P_{\max} \approx 0.096\,F_0v_{\max}$: the muscle delivers maximum power at about one third of the maximal force and one third of the maximal velocity. A cyclist shifts gears precisely so that the leg muscles work near this speed.

### 9.6.3. Heat Production and Efficiency

Hill's equation originally came from heat measurements. The energy liberated by a contracting muscle (heat plus work) can be divided into: activation heat (related to the release and reuptake of $\ce{Ca^2+}$ and liberated whether or not the muscle shortens), maintenance heat (the continuing consumption of the cross-bridge cycle and $\ce{Ca^2+}$ pumps during isometric contraction), shortening heat, and the work done.

- The Fenn effect (Fenn, 1923): when a muscle shortens and does work, the total energy liberated is greater than in isometric contraction, the excess increasing with the work. A muscle is not a spring that is "wound up" in advance; it mobilizes energy according to the demands of the load. Hill found that the shortening heat is proportional to the distance shortened, the proportionality coefficient being exactly the $a$ in Eq. (9.3), so the extra energy liberated per unit time is $(F + a)v$.
- The Feng effect (T. P. Feng, 1932): when a resting muscle is stretched, heat production (resting metabolism) increases, revealing a link between the mechanical state of muscle and its metabolism.

Mechanical efficiency is defined as the ratio of the work done to the energy consumed. A whole muscle converts the free energy of ATP into work with an efficiency of about 20%–25%, and if the losses in regenerating ATP by oxidative phosphorylation are included, the overall efficiency of human movement is about 20%. Efficiency varies with speed: at low speed the power is small while the maintenance heat is unchanged, so efficiency is low; at high speed the cross-bridge cycle is fast and power falls, so efficiency is again low; efficiency is highest at about $0.2$–$0.3\,v_{\max}$.

![Force–velocity, power and efficiency of slow and fast muscle fibers (schematic parameters). According to the Hill equation, the slow fiber has v_max = 2 L₀/s and a/F₀ = 0.18, and the fast fiber v_max = 8 L₀/s and a/F₀ = 0.30, with the same F₀ (the same specific force). The rate of energy liberation is taken after Hill (1938) as h₀ + (F + a)v, with the isometric maintenance heat h₀ proportional to the speed of the cross-bridge cycle (h₀ = 0.1 F₀ v_max). A: force–velocity curves. B: power, with the dots marking the point of maximum power (Proposition 9.6.1). C: efficiency (work divided by energy liberated, logarithmic velocity axis): the slow fiber is more efficient at low speed and the fast fiber at high speed](./plots/force-velocity.py)

This explains why animals need both fast and slow muscle: fast fibers are necessary for rapid movement, but at low speed (maintaining posture, slow walking) they waste energy, because their cross-bridge cycle is fast and the cost of maintaining tension is high; slow fibers can deliver the required power at low speed with high efficiency. Different fiber types differ in molecular properties (filament length, the detachment rate of the cross-bridges, the number of $\ce{Ca^2+}$ pumps on the sarcoplasmic reticulum), and these differences together determine the speed range to which each is best suited.

## 9.7. Energy Sources

The concentration of ATP in muscle is about $5$–$8\,\mathrm{mmol\,L^{-1}}$, and during vigorous contraction a few $\mathrm{mmol\,L^{-1}}$ are consumed per second, so the ATP on hand lasts only about $1$–$2\,\mathrm{s}$. The ATP concentration is almost unchanged during exercise because there are four sources that act in relay, with increasing capacity and decreasing maximal rate:

| Source | Reaction | Time for which maximal-intensity exercise can be sustained | Features |
|---|---|---|---|
| Free ATP | — | About $1$–$2\,\mathrm{s}$ | Smallest store |
| **Phosphocreatine** | Creatine kinase: $\ce{PCr + ADP -> Cr + ATP}$ | About $5$–$10\,\mathrm{s}$ | Store about $20$–$30\,\mathrm{mmol\,L^{-1}}$, highest rate; also serves as an "energy shuttle" between mitochondria and myofibrils ([7.1.16](/7.1.16)) |
| Anaerobic **glycolysis** | Glycogen → lactate | About $1\,\mathrm{min}$ | Rate about half that of phosphocreatine; produces $\ce{H+}$ and lactate |
| **Oxidative phosphorylation** | Aerobic oxidation of glycogen, glucose and fatty acids | Hours | Lowest rate, limited by oxygen delivery; capacity almost unlimited |

The 100 m sprint therefore relies mainly on phosphocreatine and glycolysis, and the marathon mainly on oxidative metabolism. The ATP used during contraction goes approximately as follows: cross-bridges 60%–70%, SERCA 30%–40%, sodium pump about 5%–10% ([Chapter 8](/7.14.8)). Slow fibers are rich in mitochondria, capillaries and myoglobin (which stores $\ce{O2}$ and facilitates its diffusion within the cell, giving the muscle its red color), whereas fast glycolytic fibers are rich in glycogen and glycolytic enzymes and appear white.

The cause of muscle fatigue is not a single one. In short, vigorous exercise it is mainly the accumulation of inorganic phosphate (which lowers the force of the cross-bridges and precipitates with $\ce{Ca^2+}$ in the sarcoplasmic reticulum), increased $\ce{H+}$ and reduced $\ce{Ca^2+}$ release from the sarcoplasmic reticulum, not lactate itself; in prolonged exercise it is glycogen depletion.

## 9.8. Summation of Contractions

### 9.8.1. Twitch and Tetanus

**Definition 9.8.1 (Twitch and Tetanus)** A brief contraction caused by a single action potential is called a **twitch**. When action potentials arrive successively at a higher frequency, each later contraction falls within the relaxation phase of the previous one and the contractions superpose (incomplete tetanus); at a sufficiently high frequency the individual contractions fuse completely into a smooth, sustained contraction called **tetanus** (complete tetanus).

The action potential lasts only $2$–$5\,\mathrm{ms}$, whereas a twitch lasts $10$–$100\,\mathrm{ms}$ (about $7.5\,\mathrm{ms}$ to peak in the fast extraocular muscles and about $100\,\mathrm{ms}$ in the slow soleus), so the next action potential can arrive before the previous contraction has ended. Superposition occurs because cytosolic $\ce{Ca^2+}$ does not have time to return to the resting level: $\ce{Ca^2+}$ accumulates step by step and troponin stays occupied (panel C of the $\ce{Ca^2+}$ transient figure in [Chapter 8](/7.14.8)). There is also a mechanical reason why a twitch does not reach maximal tension: the $\ce{Ca^2+}$ transient is so brief that the contractile element has not had time to stretch the series elastic element fully before activation has already faded. Tetanic tension is therefore about 3–5 times the twitch. The fusion frequency is about $80$–$100\,\mathrm{Hz}$ in fast muscle and about $20$–$30\,\mathrm{Hz}$ in slow muscle. In the body motor neurons fire at $8$–$40\,\mathrm{Hz}$, so normal contractions are mostly incomplete or complete tetanus, the result of frequency summation.

The twitch of a single muscle fiber is all-or-none, but the whole muscle is not: as the stimulus intensity increases, more and more fibers (motor units) with different thresholds are excited and the contraction strengthens stepwise. This is spatial summation (multiple-fiber summation).

### 9.8.2. The Size Principle

When the center increases its drive, in what order are motor units recruited? Henneman (1957) found in the cat spinal cord that motor neurons are recruited in an orderly way according to size: small ones are excited first and large ones later.

**Definition 9.8.2 (Size Principle)** The recruitment of the motor neurons of a muscle, as synaptic input gradually increases, in order from small to large soma and axon, and their derecruitment in the reverse order, is called the **size principle** (Henneman's principle).

The size principle does not require the center to select neurons one by one; it arises automatically from the physical properties of the neurons themselves.

**Example 9.8.1 (The Ohm's Law Explanation of the Size Principle)** Approximate a motor neuron as a sphere of uniform specific membrane resistance (the contribution of the dendrites changes only the coefficient), with input resistance $R_{\mathrm{in}} = R_{\mathrm{m}}/(4\pi r^2)$. Two neurons have soma diameters of $30\,\mu\mathrm{m}$ and $60\,\mu\mathrm{m}$; the larger has 4 times the surface area and 1/4 the input resistance of the smaller. If both receive the same synaptic current $I$ (common input from the same set of descending and afferent fibers), the depolarization $\Delta V = IR_{\mathrm{in}}$ is 4 times larger on the small neuron than on the large one, and the small neuron reaches threshold first. In reality the large neuron receives somewhat more synaptic current, but not enough to offset the difference in input resistance.

The size principle has three advantages. First, small motor neurons innervate few, slow, fatigue-resistant fibers, and everyday low-intensity activity recruits only these, which is economical and sustainable; the large, fast and fatigable motor units are called upon only when great force is needed. Second, the grading of force is proportional to the current force: at low force each newly recruited unit adds only a small force, and at high force the absolute increment is larger but the relative increment is still small, so fine control is possible at every force level (panel C). Third, the center needs to regulate only the total drive, and the order of recruitment and the increase in frequency are accomplished automatically.

![Recruitment of a motor unit pool according to the size principle (simplified Fuglevand-type model, 1993; schematic parameters). The recruitment thresholds of 120 motor units are exponentially distributed (30-fold range, the last unit recruited at 60% of maximal drive), the maximal tetanic forces differ 100-fold, and the twitch time ranges from 90 ms (smallest unit) to 30 ms (largest unit); above threshold the firing frequency rises from 8 Hz with drive up to 35 Hz, and slow units fuse at lower frequencies. A: firing frequency of every tenth unit as a function of drive: small units are recruited first and reach the maximal frequency first. B: total force (red) and number of recruited units (blue dashed line): in the first 60% of the drive recruitment and rate coding act together, and thereafter only rate coding. C: the increment of force on recruiting each new unit as a percentage of the total force at that moment: apart from the first few units it is only a few percent, so at every force level the grading of force is fine](./plots/recruitment.py)

The size principle holds in most everyday activities but is not without exceptions. With electrical stimulation on the skin surface the order is reversed, because thick axons have a lower threshold to extracellular current and large motor units are excited first; in some extremely fast movements (the paw shake of the cat) fast motor units are activated preferentially and slow ones are inhibited; the loss of motor neurons and reinnervation with aging change the size of motor units, motor units rotate during fatigue, and pain can also disturb recruitment order. Whether these exceptions imply a general "selective recruitment" is still debated, and most can be regarded as perturbations of orderly recruitment. A more recent view holds that the common input from the center acts not on the motor neuron pool of one muscle as a unit but on "functional clusters" spanning several synergist muscles: recruitment within a cluster follows the size principle, whereas motor units of the same muscle belonging to different clusters may show an order opposite to the size principle. This both reduces the burden on the center of coordinating thousands of motor neurons and retains the automaticity of the size principle.

## 9.9. Types of Skeletal Muscle Fibers

Skeletal muscle fibers are classified by the isoform of myosin heavy chain (MyHC) they express; the isoform determines the ATPase activity and the detachment rate of the cross-bridges and thereby $v_{\max}$.

| Property | Type I (slow oxidative) | Type IIA (fast oxidative–glycolytic) | Type IIX (fast glycolytic) |
|---|---|---|---|
| Myosin heavy chain (gene) | β/slow (*MYH7*) | IIa (*MYH2*) | IIx (*MYH1*) |
| Twitch time | Long (about $100\,\mathrm{ms}$) | Short | Shortest |
| $v_{\max}$ (human, relative) | 1 | About 3–5 | About 8–10 |
| Fatigue resistance | High | Fairly high | Low |
| Mitochondria, capillaries, myoglobin | Many (red muscle) | Fairly many | Few (white muscle) |
| Glycogen and glycolytic enzymes | Few | Intermediate | Many |
| Sarcoplasmic reticulum and SERCA | Fewer (SERCA2a) | Many | Most (SERCA1a) |
| Fiber diameter | Smaller | Intermediate | Larger |
| Motor unit | Small, small neuron, recruited first | Intermediate | Large, large neuron, recruited last |

Small mammals also have the still faster type IIB (*MYH4*); human limb muscles do not express IIB, and the "type IIB" of humans in older literature is in fact type IIX. Fiber type is not fixed: cross-innervation experiments (Buller, Eccles and Eccles, 1960) showed that when the nerve to a fast muscle is replaced with the nerve to a slow muscle the fast muscle becomes slow, so the firing pattern of the nerve determines the phenotype of the fiber; endurance training converts type IIX to type IIA, and disuse, denervation and prolonged weightlessness shift fibers toward the fast type; and there are many hybrid fibers expressing two MyHCs at once.

## 9.10. Structural Design of Skeletal Muscle

### 9.10.1. Syncytium and Myonuclear Domain

To increase the force of a fiber, parallel myofibrils must be added, that is, the cross-sectional area of the fiber must be increased. The skeletal muscle fiber is a multinucleate syncytium formed by the fusion of myoblasts ([7.5.24](/7.5.24)), which allows its volume to be far larger than that of an ordinary cell; but each nucleus can support protein synthesis and turnover only for a limited volume of cytoplasm.

**Definition 9.10.1 (Myonuclear Domain)** The volume of cytoplasm for which one nucleus in a muscle fiber is responsible is called the **myonuclear domain**, that is, the ratio of fiber volume to nuclear number $V/N$.

The myonuclear domain in humans and mice is of the order of $10^4\,\mu\mathrm{m}^3$ (for example a fiber of $60\,\mu\mathrm{m}$ diameter has about 100 nuclei per millimeter, a myonuclear domain of about $3\times10^4\,\mu\mathrm{m}^3$), relatively conserved among species. Three-dimensional reconstructions of whole fibers show that the number of nuclei and the volume obey a sublinear power law

$$
N = aV^{\,b}, \qquad b \approx 0.64, \tag{9.5}
$$
so the myonuclear domain $V/N = V^{1-b}/a \propto V^{0.36}$ increases slowly as the fiber grows (the unit of $a$ is $\mu\mathrm{m}^{-3b}$). The myonuclear domain of slow fibers is smaller than that of fast fibers in the same species, possibly because their protein turnover is faster. Mature human fibers range in length from a few millimeters to over ten centimeters and in diameter from $10$ to $100\,\mu\mathrm{m}$, contain hundreds to thousands of nuclei, and the nuclei are evenly arranged beneath the sarcolemma. Growth and repair in the adult are accomplished by the proliferation of **satellite cells** and their fusion with the fiber, adding new nuclei; a fiber that is already thick has little reserve of myonuclear domain and must add new nuclei in order to thicken further. Mutations of the myoblast fusion protein myomaker cause Carey–Fineman–Ziter syndrome, characterized by hypotonia.

### 9.10.2. Intrafascicularly Terminating Fibers and Lateral Force Transmission

The more sarcomeres are in series, the faster and greater the contraction; if all fibers ran through the whole muscle, the speed would be greatest. But fiber length is limited by the myonuclear domain and by development, and the strength of a single fiber is also limited. In fact, in many long muscles (especially in fast fibers) the fibers do not connect to the tendons at both ends but terminate within the fascicle in tapering ends, interdigitating end to end with neighboring fibers (intrafascicularly terminating fibers). In this way many short fibers in series exceed the length limit of a single fiber, and the interdigitated parallel arrangement increases load-bearing capacity within a limited volume.

This structure requires force to be transmitted laterally between fibers. Muscle fibers anchor the Z lines to the endomysium through costameres and exert shear forces on the endomysium during contraction; experiments and modeling both show that most of the force is transmitted laterally to the endomysium in the form of shear, converted by the highly ordered collagen network of the perimysium into longitudinal tension, collected in the epimysium and aponeurosis, and finally output through the parallel collagen fibers of the tendon. Connective tissue does not itself generate force but is the key to the coordinated output of force. Slow fibers are mostly connected directly to the tendon, but this does not make them faster: they are slow because their myosin ATPase is slow; the direct connection only reduces losses along the force transmission path and suits sustained low-intensity contraction.

### 9.10.3. Physiological Cross-Sectional Area and Pennate Muscle

**Definition 9.10.2 (Physiological Cross-Sectional Area)** The sum of the cross-sectional areas of all fibers cut perpendicular to the fiber direction is called the **physiological cross-sectional area** (PCSA) of the muscle, and can be calculated from the muscle volume $V$ (or mass $M$ and density $\rho \approx 1.06\,\mathrm{g\,cm^{-3}}$) and the fiber length $L_{\mathrm{f}}$:

$$
\mathrm{PCSA} = \frac{V}{L_{\mathrm{f}}} = \frac{M}{\rho L_{\mathrm{f}}}. \tag{9.6}
$$

The maximal isometric tension of a muscle is proportional to PCSA, with the specific force $\sigma$ (maximal tension per unit cross-sectional area) as the proportionality coefficient; it is about $20$–$40\,\mathrm{N\,cm^{-2}}$ ($0.2$–$0.4\,\mathrm{MPa}$) in mammalian skeletal muscle, determined by the density of myofibrils and the force of the cross-bridges, and is almost constant among species. When the fibers make a pennation angle $\theta$ with the line of action of the muscle (the direction of the tendon), the force along the tendon is multiplied by $\cos\theta$:

$$
F_0 = \sigma\cdot\mathrm{PCSA}\cdot\cos\theta. \tag{9.7}
$$

**Example 9.10.1** For a pennate muscle of mass $275\,\mathrm{g}$, fiber length $4.4\,\mathrm{cm}$ and pennation angle $28^\circ$ (close to the architecture of the human soleus), $\mathrm{PCSA} = 275/(1.06\times4.4) \approx 59\,\mathrm{cm^2}$. Taking $\sigma = 25\,\mathrm{N\,cm^{-2}}$, the maximal force along the tendon is $F_0 = 25\times59\times\cos28^\circ \approx 1.3\times10^3\,\mathrm{N}$. A parallel-fibered muscle of the same mass with fibers $30\,\mathrm{cm}$ long would have a PCSA of only $8.6\,\mathrm{cm^2}$ and a maximal force of about $220\,\mathrm{N}$, but its shortening velocity and range would be about 6 times those of the former.

Parallel-fibered muscles, whose fibers run parallel to the tendon (sartorius, biceps brachii), have long fibers and many sarcomeres in series, and shorten fast and over a large range; pennate muscles (soleus, vastus lateralis) pack more and shorter fibers into the same volume, with a large PCSA and large force but low speed and range. The loss from $\cos\theta$ is not great (only 13% at $\theta = 30^\circ$), and fibers rotate as they shorten, so that the muscle belly shortens along the line of action faster than the fibers themselves (the architectural "gear ratio"), partly compensating for speed.

![The trade-off between force and velocity in muscle architecture at equal volume (simplified planar model, pennation angle fixed). The three muscles all have a volume of 200 cm³ and a specific force of 25 N cm⁻²: parallel-fibered (fibers 20 cm, θ = 0°), pennate (fibers 8 cm, θ = 20°) and pennate (fibers 4 cm, θ = 30°). The isometric force along the tendon is F₀ = σ(V/L_f)cos θ (Eq. (9.7)); fibers shorten at most 5 fiber lengths per second, and the velocity of the tendon is 1/cos θ times that of the fibers; Hill curvature a/F₀ = 0.25. A: force–velocity curves along the tendon. B: power: the maximal power is the same for all three and determined only by volume (P_max in Proposition 9.6.1 is proportional to F₀ v_max, and F₀ v_max is proportional to volume). C: maximal force, maximal velocity and usable shortening range (about 0.4 L_f / cos θ)](./plots/architecture.py)

Panel B reveals a simple rule: the maximal power is proportional to $F_0v_{\max} \propto (\sigma V/L_{\mathrm{f}})\cdot L_{\mathrm{f}} = \sigma V$ and is determined only by the volume of the muscle. Architecture (fiber length and pennation angle) determines only whether this fixed amount of power is delivered as "large force, low speed" or "small force, high speed", just as a gearbox does not change the power of the engine.

## 9.11. Evolution and Comparative Aspects

### 9.11.1. Conservation of Specific Force and Scaling with Body Size

The specific force of skeletal muscle is similar in different animals, as are sarcomere length and the force of cross-bridges, so muscle force grows with cross-sectional area, speed (in muscle lengths per second) depends only on the myosin isoform, and power grows with volume. A. V. Hill (1950) drew a surprising conclusion from this: geometrically similar animals should jump equally high. Let the body length be $L$; the muscle force is $\propto L^2$, the distance of contraction $\propto L$, the work done $\propto L^3$, and the body weight $\propto L^3$, so the jump height $h = W/(mg)$ is independent of body length. This is roughly the case: the center of mass of a human rises about $0.5\,\mathrm{m}$ in a standing jump, that of a locust about $0.5$–$1\,\mathrm{m}$ and that of a flea about $0.2\,\mathrm{m}$.

But small animals face another limit: time. In a jump the leg can extend only over a distance proportional to body length, and the takeoff time of a small animal is extremely short, demanding a power density beyond the capacity of any muscle.

**Example 9.11.1 (Why the Flea Needs a Catapult)** A flea of $0.45\,\mathrm{mg}$ takes off at about $1\,\mathrm{m\,s^{-1}}$, with kinetic energy $\frac12mv^2 = 2.3\times10^{-7}\,\mathrm{J}$; the takeoff lasts only about $1\,\mathrm{ms}$, so the power is $2.3\times10^{-4}\,\mathrm{W}$. Even if the jumping muscles make up 10% of body weight, the power density required is about $5\times10^{3}\,\mathrm{W\,kg^{-1}}$, an order of magnitude higher than that of the fastest known muscle (a few hundred $\mathrm{W\,kg^{-1}}$).

The solution of fleas and locusts is power amplification: the muscle contracts slowly, stores energy in an elastic structure held by a latch, and then releases it suddenly. The elastic pad in the flea thorax is made of the arthropod elastic protein resilin, which can store and release elastic energy almost without loss (resilience about 97%); at takeoff the energy is transmitted through the trochanter and tibia of the hind legs to the ground (Sutton and Burrows, 2011). In the locust the extensor and flexor tibiae of the hind leg first co-contract for about $0.3\,\mathrm{s}$, storing energy in the semilunar process at the end of the femur and in tendons; after the flexor releases the latch the energy is released within about $30\,\mathrm{ms}$, and the energy of one jump is about $10\,\mathrm{mJ}$. The same principle of "store slowly, release fast" is also seen in the raptorial appendage of the mantis shrimp, the jump of click beetles and the tongue of the chameleon, and the Venus flytrap achieves fast movement without muscle by the elastic instability of the leaf ([7.13.19](/7.13.19)).

### 9.11.2. Red and White Muscle in Fishes

The lateral muscles of fishes separate the different fiber types spatially: slow red muscle (oxidative) is a thin layer at the surface of the flank near the horizontal septum, and fast white muscle (glycolytic) makes up most of the lateral muscle. In slow cruising only the red muscle works, and the white muscle is called upon only in high-speed sprints, an expression of the size principle at the level of the whole muscle. Measurements on carp show that at the swimming speeds at which each is recruited, the shortening velocity of both fiber types stays at about $0.17$–$0.36\,v_{\max}$, exactly the range of highest power and efficiency (Section 9.6): the animal does not ask slow muscle to do fast things or fast muscle to do slow things. When water temperature falls muscle slows down, and a fish recruits white muscle earlier at the same swimming speed. In tuna and lamnid sharks the red muscle lies deep in the flank near the vertebral column and is kept warm by countercurrent heat exchange ([Chapter 31](/7.14.31)), allowing them to sustain high-power swimming in cold water.

### 9.11.3. Variations in Invertebrates

The sarcomere length of arthropod striated muscle varies greatly, from about $2\,\mu\mathrm{m}$ to more than $10\,\mu\mathrm{m}$: muscles with long sarcomeres and long thick filaments (such as the slow fibers of the crab claw closer) have more cross-bridges in parallel per sarcomere and are strong and slow; those with short sarcomeres (such as insect flight muscle) have more sarcomeres in series and are fast. The ratio of thick to thin filaments also varies (6 thin filaments around each thick filament in vertebrates, 6 also in many insect flight muscles, and up to 10–12 in slow crustacean muscle). The basic relations of muscle mechanics hold in all groups, and what varies are these geometric and molecular parameters. The catch muscles of molluscs, the obliquely striated muscles of annelids and nematodes and the asynchronous flight muscles of insects represent larger variations, see [Chapter 10](/7.14.10).

## Summary

| Relation | Formula or conclusion | Mechanism |
|---|---|---|
| Sliding filament theory (Definition 9.2.1) | Filament lengths constant, overlap changes | The cross-bridge cycle slides the thin filaments toward the M line |
| Length–tension (Proposition 9.3.1) | Plateau $2.05$–$2.25\,\mu\mathrm{m}$, descending limb $T = (3.65 - s)/1.40$ (Eq. (9.1)), zero at $3.65\,\mu\mathrm{m}$ (frog) | Force ∝ effective overlap ∝ number of working cross-bridges |
| Ca²⁺ switch | Hill coefficient of $F/F_{\max}$ versus $[\ce{Ca^2+}]$ of $2$–$5$ (Eq. (9.2)) | Cooperativity of troponin–tropomyosin |
| Load (Definitions 9.3.2, 9.5.2) | Preload sets the initial length; afterload sets the shortening velocity | Three-element model |
| Force–velocity (Eq. (9.3)) | $(F + a)(v + b) = b(F_0 + a)$ | Cross-bridge attachment time shortens with speed |
| Maximum power (Proposition 9.6.1) | $f^{*} = v^{*}/v_{\max} = \sqrt{\alpha^2 + \alpha} - \alpha \approx 0.3$ | — |
| Heat production | Fenn effect, Feng effect; efficiency about 20%–25%, peak at $0.2$–$0.3\,v_{\max}$ | Energy mobilized according to load |
| Energy sources | ATP $1$–$2\,\mathrm{s}$, phosphocreatine $5$–$10\,\mathrm{s}$, glycolysis about $1\,\mathrm{min}$, oxidation hours | Capacity increasing, rate decreasing |
| Summation | Tetanus (Definition 9.8.1): $\ce{Ca^2+}$ accumulation, tetanic tension about 3–5 times the twitch; size principle (Definition 9.8.2): $\Delta V = IR_{\mathrm{in}}$ | Rate coding and orderly recruitment |
| Fiber types | I, IIA, IIX (rodents also IIB), determined by MyHC, plastic | Trade-off between speed and economy |
| Structural design | Myonuclear domain (Definition 9.10.1) $N \propto V^{0.64}$; $F_0 = \sigma\cdot\mathrm{PCSA}\cdot\cos\theta$ (Eq. (9.7)); $P_{\max} \propto \sigma V$ | Parallel adds force, series adds velocity |
| Comparison | Geometrically similar animals jump equally high; small animals amplify power by elastic energy storage; fishes divide labor between red and white muscle according to speed | — |

## Questions

1. The thick filament of an animal is $1.6\,\mu\mathrm{m}$ long (bare zone $0.16\,\mu\mathrm{m}$), and the thin filament is $1.12\,\mu\mathrm{m}$ long measured from the center of the Z line. Find the plateau range of its length–tension curve and the sarcomere length at which active tension falls to zero; at a sarcomere length of $3.0\,\mu\mathrm{m}$, what percentage of the maximum is the active tension?

   **Answer** The thin filaments from the two sides meet at the M line when $s = 2\times1.12 = 2.24\,\mu\mathrm{m}$, and the end of the thin filament reaches the edge of the bare zone when $s = 2.24 + 0.16 = 2.40\,\mu\mathrm{m}$, so the plateau is $2.24$–$2.40\,\mu\mathrm{m}$; with no overlap $s = 1.6 + 2.24 = 3.84\,\mu\mathrm{m}$. On the descending limb $T = (3.84 - s)/(3.84 - 2.40)$, and at $s = 3.0\,\mu\mathrm{m}$, $T = 0.84/1.44 = 58\%$.

2. A muscle has $F_0 = 400\,\mathrm{N}$, $v_{\max} = 0.5\,\mathrm{m\,s^{-1}}$ and $a/F_0 = 0.25$. Find its maximum power and the load and velocity at that point; what is the velocity at a load of $200\,\mathrm{N}$?

   **Answer** By Proposition 9.6.1, $f^{*} = \sqrt{0.0625 + 0.25} - 0.25 = 0.309$; at maximum power the load is $0.309\times400 = 124\,\mathrm{N}$, the velocity $0.309\times0.5 = 0.155\,\mathrm{m\,s^{-1}}$, and the power about $19\,\mathrm{W}$. At a load of $200\,\mathrm{N}$, that is $f = 0.5$, $v/v_{\max} = 0.25\times0.5/(0.5 + 0.25) = 0.167$ and $v = 0.083\,\mathrm{m\,s^{-1}}$.

3. Why are almost all skeletal muscle contractions in the intact body tetanic, whereas cardiac muscle never undergoes tetanus?

   **Answer** Motor neurons fire at $8$–$40\,\mathrm{Hz}$, whereas a skeletal muscle twitch lasts tens of milliseconds, the action potential lasts only a few milliseconds and the refractory period is very short, so later action potentials always arrive before the previous contraction has ended, $\ce{Ca^2+}$ accumulates and the contractions summate; contractions in the body are therefore incomplete or complete tetanus. The plateau of the cardiac action potential extends the effective refractory period (about $250\,\mathrm{ms}$) beyond the end of contraction, so a new action potential can arise only after the cardiac muscle has begun to relax, and contractions cannot fuse; this ensures relaxation and filling of the ventricles after every contraction ([Chapter 13](/7.14.13)).

4. Use the size principle to explain why one does not tire easily during prolonged standing but tires quickly when lifting weights. If a drug halved the input resistance of all motor neurons, would the order of recruitment change?

   **Answer** Standing requires only a small force, borne by the small motor units recruited first (type I fibers, oxidative metabolism, fatigue resistant), and motor units can rotate. Lifting weights requires nearly maximal force, which must recruit the large type IIX motor units, which depend on phosphocreatine and glycolysis and fatigue within seconds to tens of seconds. When the input resistance falls in the same proportion, the relative sizes of the neurons are unchanged, the small neurons still reach threshold first for the same input, and the order is unchanged; only a stronger drive is needed to reach threshold.

5. (Open question) Compare two muscles of equal volume: one used for rapid swinging (such as the flight muscle of a bird) and one for maintaining posture (such as the soleus). In terms of fiber type, fiber length and pennation angle, and energy sources, explain how their designs should differ, and explain why a "stronger" muscle is not necessarily "more able to do work".

   **Answer** Key points: rapid swinging requires high $v_{\max}$ and high power: fast fibers (but because bird flight muscle must sustain activity, mostly fast oxidative), fairly long fibers or a small pennation angle for large speed and range, and rich mitochondria for sustained energy supply. Maintaining posture requires large isometric force and high economy: slow fibers, short fibers and a large pennation angle for a large PCSA, and low maintenance heat. From panel B, maximal power is determined only by volume (and by specific force and $v_{\max}/L_{\mathrm{f}}$), and a pennate muscle being "strong" (large $F_0$) merely converts the same power into the form of large force and low speed; the capacity to do work (work = force × distance ∝ PCSA × $L_{\mathrm{f}}$ ∝ volume) is likewise determined by volume and does not increase because $F_0$ is large.
