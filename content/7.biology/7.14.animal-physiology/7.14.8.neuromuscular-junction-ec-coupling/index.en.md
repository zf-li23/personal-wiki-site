---
title: The Neuromuscular Junction and Excitation–Contraction Coupling
source_hash: 9793cd2e8827
---

Muscle is the principal effector of animals: skeletal muscle makes up about 40% of body weight in humans, and smooth muscle and cardiac muscle together about 10%. A voluntary movement begins with a single **action potential** in a motor neuron and ends with filament sliding, and five steps lie between: the nerve terminal releases transmitter at the **neuromuscular junction**; the sarcolemma generates an action potential; the action potential travels down the transverse tubules into the depth of the cell and triggers the release of $\ce{Ca^2+}$ from the sarcoplasmic reticulum (excitation–contraction coupling); $\ce{Ca^2+}$ opens the switch on the thin filament and the **cross-bridge cycle** makes the filaments slide; and $\ce{Ca^2+}$ is pumped back into the sarcoplasmic reticulum and contraction stops. This chapter covers the first, second, third and fifth steps; the fourth step and the mechanics and energetics of muscle as an engine are the subject of [Chapter 9](/7.14.9), and cardiac muscle, smooth muscle and the muscles of invertebrates are in [Chapter 10](/7.14.10). The neuromuscular junction is the most thoroughly studied **chemical synapse**; its **quantal release**, $\ce{Ca^2+}$ dependence and receptor kinetics are the prototype of the general synaptic transmission treated in [Chapter 5](/7.14.5). For the development of the junction see [7.5.21](/7.5.21), and for the ionic mechanism of the action potential see [Chapter 4](/7.14.4) and [7.6.30](/7.6.30).

## 8.1. Muscle and the Motor Unit

### 8.1.1. Why Muscle Is Needed

Animals that move in their environment, feed, pump blood and propel contents need a tissue that converts chemical energy directly into mechanical work. Muscle meets three kinds of requirements. As a material, it forms by **self-assembly** of proteins, is soft and can deform greatly (a **sarcomere** can shorten by about 40%), and the maximum stress per unit cross-sectional area is about $0.2$–$0.4\,\mathrm{MPa}$. In energetics, it uses ATP directly as fuel, and a whole muscle converts chemical energy into work with an efficiency of about 20%–25%, higher at the optimal speed. In repair, damaged muscle fibers regenerate by the proliferation and fusion of **satellite cells**, and under training the fibers thicken in proportion to load.

An instructive comparison is soft robotics. Most robots today are built of rigid materials and motors, because the kinematics of rigid bodies is easy to model and control precisely, and the power density and lifetime of motors are assured; "artificial muscles" made of pneumatic or dielectric elastomers can reach strains and stresses comparable to those of muscle, but often require an external gas supply or voltages of thousands of volts and can hardly sense or repair themselves. Muscle integrates actuation (the cross-bridges), sensing (**muscle spindles** and **tendon organs**, [Chapter 44](/7.14.44)), energy supply, growth and repair in a single tissue, something artificial systems still cannot do simultaneously.

Muscle is not the only cell type that generates force. A flea jumps within $1\,\mathrm{ms}$ by storing energy slowly in the elastic protein resilin through muscle contraction and then releasing it suddenly ([Chapter 9](/7.14.9)); the closing of the Venus flytrap uses no muscle at all but relies on the elastic instability of the leaf ([7.13.19](/7.13.19)).

The reasons why muscle was the first tissue studied systematically by humans are also straightforward: its contraction is visible to the naked eye and directly linked to being "alive"; medicine and anatomy (Vesalius's *De humani corporis fabrica*, 1543) needed it; and it was a natural object for mechanics and for philosophical discussion of whether life is a machine. In the 17th century Swammerdam showed that the volume of a muscle does not change during contraction, refuting the ancient hypothesis that nerves pour a gas into the muscle to inflate it; at the end of the 18th century Galvani's frog-leg experiments linked muscle contraction with electricity ([Chapter 4](/7.14.4)).

### 8.1.2. Hierarchical Structure of Skeletal Muscle

| Level | Size | Structural points |
|---|---|---|
| Muscle | Centimeters to tens of centimeters | Attached to bone at both ends through tendons; enclosed by the epimysium |
| Fascicle | About $1\,\mathrm{mm}$ | Many muscle fibers wrapped into a bundle by the perimysium |
| Muscle fiber (muscle cell) | Diameter $10$–$100\,\mu\mathrm{m}$, length several millimeters to more than $10\,\mathrm{cm}$ | Multinucleate syncytium formed by fusion of **myoblasts**; enclosed by the endomysium; the cell membrane is called the sarcolemma |
| Myofibril | Diameter about $1\,\mu\mathrm{m}$ | Formed by sarcomeres joined end to end, running the whole length of the fiber |
| Sarcomere | About $2$–$2.5\,\mu\mathrm{m}$ at rest | Thick filaments (myosin) and thin filaments (actin) interdigitate and produce the striations |

The structure of the **sarcomere** and the **sliding filament theory** are treated in [Chapter 9](/7.14.9); the multinucleate structure of the muscle fiber arises by myoblast fusion, see [7.5.24](/7.5.24).

### 8.1.3. The Motor Unit

Each skeletal muscle fiber of vertebrates (apart from a few tonic fibers, Section 8.8) has only one neuromuscular junction and is innervated by only one motor neuron; conversely, the axon of one motor neuron branches within the muscle and innervates from a few up to a thousand fibers.

**Definition 8.1.1 (Motor Unit)** An α motor neuron and all the muscle fibers innervated by its axonal branches are called a **motor unit**. The motor unit is the smallest unit by which the nervous system controls skeletal muscle: each time the neuron fires an action potential, all its muscle fibers produce one action potential and one contraction.

The number of fibers in a motor unit (the innervation ratio) determines the fineness of control. The motor units of the extraocular muscles contain only about 10 fibers, the small muscles of the hand about 100, and the gastrocnemius of the calf and the postural muscles of the back can have a thousand or more: fine movements need many small motor units, and coarse, forceful movements can be produced with a few large motor units. The fibers of one motor unit belong to the same type ([Chapter 9](/7.14.9)) and are not clustered together but scattered over a region of the muscle cross section (covering from less than 10% to more than 70%), forming only small local clusters; thus the force of a single motor unit is distributed over a large part of the muscle, and when many motor units fire asynchronously the resultant force is smooth. The center grades muscle force by changing the number of motor units recruited and the firing frequency of each unit; the rules of both (the **size principle** and **tetanus**) are discussed in [Chapter 9](/7.14.9).

## 8.2. Structure of the Neuromuscular Junction

When the myelinated axon of a motor neuron reaches the vicinity of a muscle fiber it loses its myelin and divides into several terminal branches, whose ends swell into terminal boutons lying in shallow grooves (synaptic gutters) on the surface of the sarcolemma and covered by terminal Schwann cells. This specialized chemical synapse is the **neuromuscular junction** (NMJ), and the specialized region of the sarcolemma opposite it is called the motor end plate.

| Structure | Features | Significance |
|---|---|---|
| Presynaptic terminal | Contains many synaptic vesicles about $50\,\mathrm{nm}$ in diameter, each holding about $10^4$ molecules of acetylcholine (ACh); rich in mitochondria | Large vesicle pool; mitochondria power vesicle recycling and $\ce{Ca^2+}$ clearance |
| Active zone | Dense bands on the presynaptic membrane, flanked by neatly arranged voltage-gated $\ce{Ca^2+}$ channels ($\mathrm{Ca_V2.1}$) and docked vesicles | $\ce{Ca^2+}$ entry and fusion sites are only tens of nanometers apart, so release is fast and synchronous |
| Synaptic cleft | $20$–$50\,\mathrm{nm}$ wide; the basal lamina in it anchors acetylcholinesterase (AChE) | Short distance, so transmitter diffusion takes only microseconds; AChE in place terminates the signal quickly |
| Junctional folds | The end-plate membrane folds inward to form many secondary clefts directly opposite the active zones | Increase the area of the postsynaptic membrane; the density of ACh receptors at the crests of the folds is about $10^4\,\mu\mathrm{m^{-2}}$, and voltage-gated $\mathrm{Na^+}$ channels ($\mathrm{Na_V1.4}$) are concentrated at the bottom of the folds, lowering the threshold for triggering an action potential near the end plate |
| Position and size of the end plate | Usually in the middle of the fiber, with an area of less than 0.1% of the fiber surface | The action potential propagates from the middle toward both ends, halving the time to reach the ends |

The formation of the end plate depends on agrin released by the motor nerve terminal, which clusters ACh receptors beneath the junction through the LRP4–MuSK receptor complex on the sarcolemma and the scaffold protein rapsyn ([7.5.21](/7.5.21)).

## 8.3. Transmitter Release

### 8.3.1. The Discovery of Chemical Transmission

How a nerve transmits a signal across the gap between it and the muscle was the central problem of neurophysiology in the first half of the 20th century.

| Year | Investigator | Key contribution | Question answered |
|---|---|---|---|
| 1914 | H. H. Dale | Isolated acetylcholine from ergot (fungus) extracts and found its action strong and brief (easily hydrolyzed), divided into muscarinic and nicotinic actions | Is there a substance that can serve as a transmitter? |
| 1921 | O. Loewi | Stimulation of the vagus nerve of a frog heart yielded a perfusate that slowed a second heart ("Vagusstoff") | Do nerves release chemical signals? |
| 1936 | Dale, Feldberg and Vogt | Detected ACh in the perfusate of muscle when the motor nerve was stimulated | What is the transmitter at the neuromuscular junction? |
| Late 1930s | T. P. Feng (Feng Depei) | Changing extracellular $\ce{Ca^2+}$ markedly changed neuromuscular transmission; described post-tetanic potentiation | What regulates release? |
| 1950s–1960s | B. Katz and collaborators | Quantal release; $\ce{Ca^2+}$ must be present when the nerve impulse arrives (Katz and Miledi, 1967) | What is the physical mechanism of release? |
| From 1976 | E. Neher and B. Sakmann | **Patch clamp** recording of the current of single ACh receptor channels | How do receptor channels work? |

Loewi and Dale shared the 1936 Nobel Prize in Physiology or Medicine, Katz received the prize in 1970, and Neher and Sakmann in 1991. The work of T. P. Feng preceded the quantitative studies of Katz and was a pioneering contribution of Chinese physiology in this field; in 1932 he also discovered that the heat production of resting muscle increases when it is stretched (the Feng effect, [Chapter 9](/7.14.9)).

### 8.3.2. The Process of Release

1. The action potential reaches the terminal and opens the $\mathrm{Ca_V2.1}$ (P/Q-type) channels of the active zone. The electrochemical gradient of $\ce{Ca^2+}$ is very large (about $1$–$2\,\mathrm{mmol\,L^{-1}}$ outside, about $0.1\,\mu\mathrm{mol\,L^{-1}}$ inside), and in the "nanodomain" near the channel mouth $[\ce{Ca^2+}]$ rises to tens of $\mu\mathrm{mol\,L^{-1}}$ in less than 1 ms.
2. $\ce{Ca^2+}$ binds to the vesicular $\ce{Ca^2+}$ sensor synaptotagmin, the already assembled **SNARE** proteins complete the membrane fusion, and ACh is released by **exocytosis**. From the action potential to the onset of the end-plate current takes about $0.5\,\mathrm{ms}$, the **synaptic delay**, spent mainly on the opening of $\ce{Ca^2+}$ channels and on fusion.
3. A nerve impulse usually releases about 125–200 vesicles, that is, about $10^6$ ACh molecules.
4. The vesicle membrane is recovered by endocytosis mediated by **clathrin** and refilled: choline acetyltransferase synthesizes ACh in the cytosol from acetyl coenzyme A and choline, and the vesicular ACh transporter pumps it into the vesicles; the choline needed for synthesis comes mainly from the part recovered by the high-affinity choline transporter after ACh has been hydrolyzed in the cleft.

The terminals of one end plate hold about $3\times10^5$ vesicles, enough for only a few thousand impulses. With sustained stimulation above about $100\,\mathrm{Hz}$ for several minutes, the vesicles are exhausted and transmission fails: this is fatigue of the junction. The firing frequency of normal motor neurons is far below this.

Release depends strongly on $\ce{Ca^2+}$. Dodge and Rahamimoff (1967) found that the amount released $m$ is proportional to the fourth power of extracellular $\ce{Ca^2+}$, with $\ce{Mg^2+}$ inhibiting competitively:

$$
m = K\left(\frac{[\ce{Ca^2+}]_{\mathrm{o}}}{1 + [\ce{Ca^2+}]_{\mathrm{o}}/K_1 + [\ce{Mg^2+}]_{\mathrm{o}}/K_2}\right)^4 . \tag{8.1}
$$

The fourth power means that about four $\ce{Ca^2+}$ must act cooperatively to cause one vesicle to fuse, in agreement with the structure of multiple $\ce{Ca^2+}$-binding sites on synaptotagmin and the SNARE complex. It is this steep nonlinearity that confines release to the instant at which the $\ce{Ca^2+}$ channels are open and to the vicinity of the channel mouth.

### 8.3.3. Quantal Release

Fatt and Katz (1952) recorded, at the end plate of unstimulated frog muscle, small depolarizations of about $0.4$–$0.5\,\mathrm{mV}$ appearing at random, about once per second on average; their time course is the same as that of the end-plate potential, they are blocked by curare, and they are increased and prolonged by cholinesterase inhibitors. These are the miniature end-plate potentials (MEPPs). del Castillo and Katz (1954) stimulated the nerve in a solution of low $\ce{Ca^2+}$ and high $\ce{Mg^2+}$, so that the evoked end-plate potentials were small, and found that their amplitudes were only integral multiples of the MEPP: 0, 1, 2, 3 ... units.

**Definition 8.3.1 (Quantal Release)** The transmitter is released in "packets" of essentially fixed size, each packet called a quantum and corresponding to the contents of one synaptic vesicle; the postsynaptic potential evoked by a nerve impulse is the sum of several quantal effects. This mode of release is called **quantal release**. The mean number of quanta $m$ released by one impulse is called the **quantal content**, and the potential $q$ produced by one quantum is called the quantal size.

Quantal release can be written as a statistical model. Suppose the terminal has $N$ releasable sites, each of which independently releases one quantum with probability $p$ per impulse; then the number of quanta released follows a **binomial distribution**. At low $\ce{Ca^2+}$, $p$ is very small and $N$ very large, and the binomial distribution tends to the **Poisson distribution** ([3.1.4](/3.1.4#def-4.1.10)) with mean $m = Np$:

$$
\mathbb{P}(k) = \mathrm{e}^{-m}\frac{m^k}{k!}, \qquad k = 0, 1, 2, \dots \tag{8.2}
$$

This model gives three mutually independent estimates of $m$, and their agreement supports the quantal hypothesis:

- the direct method: $m = \bar V_{\mathrm{EPP}}/\bar q$, the mean end-plate potential divided by the mean MEPP;
- the failures method: from $\mathbb{P}(0) = \mathrm{e}^{-m}$, $m = \ln(N_{\text{trials}}/N_{\text{failures}})$;
- the variance method: the variance of the Poisson distribution equals its mean, so the coefficient of variation of the end-plate potential amplitude satisfies $\mathrm{CV}^2 = 1/m$ (neglecting the variability of the quantal size itself).

**Example 8.3.1** In $0.5\,\mathrm{mmol\,L^{-1}}$ $\ce{Ca^2+}$ and $5\,\mathrm{mmol\,L^{-1}}$ $\ce{Mg^2+}$, 400 stimuli are given, 61 of them without response; the mean end-plate potential is $0.78\,\mathrm{mV}$ and the mean MEPP is $0.40\,\mathrm{mV}$. The failures method gives $m = \ln(400/61) = 1.88$, and the direct method gives $m = 0.78/0.40 = 1.95$; the two agree within statistical error. Eq. (8.2) then predicts that trials with exactly 1 quantum should number about $400\times1.88\,\mathrm{e}^{-1.88} \approx 115$ and trials with 2 quanta about $108$. Such agreement was obtained by del Castillo and Katz and in subsequent experiments on cat and rat junctions.

![Quantal analysis (illustrative parameters, close to the classical frog and cat data). A: simulated end-plate potential amplitudes for 400 stimuli at low Ca²⁺ and high Mg²⁺: the number of quanta released per stimulus follows a Poisson distribution with mean m = 1.9, and each quantum q is about 0.40 mV (standard deviation 0.08 mV); the red line is the peaks predicted by the Poisson model (the peak of k quanta lies at kq, with width increasing as √k), and the dashed bar at zero is the predicted number of failures; the m estimated by the two methods agrees. B: cooperativity of Ca²⁺ in Eq. (8.1): on a double-logarithmic plot the slope tends to 4 at low Ca²⁺, and Mg²⁺ shifts the curve to the right; the gray band is the quantal content of a normal junction (about 100–300). C: safety factor during a 3 Hz stimulus train: the quantal content falls gradually to 60% of the first; the normal junction (safety factor 3) stays above threshold throughout; in myasthenia gravis (fewer receptors reduce the quantal size to 35%) transmission fails from the second stimulus on (×), appearing as fatigable weakness; a cholinesterase inhibitor increases the quantal effect about 1.6-fold and transmission is largely restored](./plots/quantal-release.py)

One quantum opens about 1000–2000 ACh receptor channels, whereas the opening of a single channel produces a depolarization only of the order of microvolts. At normal $\ce{Ca^2+}$ the quantal content of the frog muscle junction is about 200–300, that of mammals about 50–150, and the human junction is smaller (about 20–50), but the junctional folds are deeper and the effect of a single quantum is larger.

**Example 8.3.2 (Nonlinear Summation of End-Plate Potentials)** With a quantal content of 150 and a quantal size of $0.4\,\mathrm{mV}$, linear addition would give an end-plate potential of $60\,\mathrm{mV}$, whereas the measured value (with the action potential blocked) is only about $40\,\mathrm{mV}$. The reason is that depolarization reduces the driving force of the ion flow. Let the reversal potential of the end-plate channels be $E_{\mathrm{r}} \approx 0\,\mathrm{mV}$ and the **resting potential** $V_{\mathrm{r}} = -90\,\mathrm{mV}$; Martin's (1955) correction converts the observed value $v$ into the linear value $v' = v/[1 - v/(E_{\mathrm{r}} - V_{\mathrm{r}})]$; conversely, $v = v'/(1 + v'/90\,\mathrm{mV}) = 60/(1 + 60/90) = 36\,\mathrm{mV}$. In quantal analysis at normal $\ce{Ca^2+}$ this correction must be applied first, otherwise the direct method underestimates $m$.

## 8.4. Acetylcholine Receptors and the End-Plate Potential

### 8.4.1. Receptors and the End-Plate Potential

The receptor at the end plate is the muscle-type **nicotinic acetylcholine receptor** ([7.1.14](/7.1.14)): a ligand-gated cation channel formed by five subunits, $\alpha_2\beta\delta\varepsilon$ in the adult and $\alpha_2\beta\gamma\delta$ in fetal and denervated muscle. The two ACh-binding sites lie at the α–δ and α–ε interfaces, and the channel opens effectively only when both sites are occupied, so the dependence of the open probability on ACh concentration is cooperative (**Hill coefficient** about 2). The channel is almost nonselective between $\mathrm{Na^+}$ and $\mathrm{K^+}$ ($P_{\mathrm{K}}/P_{\mathrm{Na}} \approx 1.1$) and is also permeable to a little $\ce{Ca^2+}$; the single-channel conductance is about $50\,\mathrm{pS}$, the mean open time about $1\,\mathrm{ms}$ and the reversal potential about $0\,\mathrm{mV}$. At $-90\,\mathrm{mV}$ the driving force for $\mathrm{Na^+}$ influx is much greater than that for $\mathrm{K^+}$ efflux, the net current is inward, and the end plate depolarizes.

**Definition 8.4.1 (End-Plate Potential)** The depolarization of the end-plate membrane produced by the activation of receptor channels at the end plate by ACh is called the **end-plate potential** (EPP). It is a local postsynaptic potential: its amplitude is graded and related to the amount of ACh released, it has no refractory period, it can summate, and it decays electrotonically to the surroundings; it does not itself propagate but depolarizes the adjacent sarcolemma to threshold, where voltage-gated $\mathrm{Na^+}$ channels generate a muscle action potential that propagates toward both ends.

In the steady-state approximation the end plate is a voltage divider formed by the receptor conductance $g_{\mathrm{ACh}}$ in parallel with the remaining membrane conductance $g_{\mathrm{m}}$ (for the equivalent circuit see [7.6.30](/7.6.30#sec-30.4.1)),

$$
V = \frac{g_{\mathrm{ACh}}E_{\mathrm{r}} + g_{\mathrm{m}}V_{\mathrm{r}}}{g_{\mathrm{ACh}} + g_{\mathrm{m}}}, \qquad \Delta V = (E_{\mathrm{r}} - V_{\mathrm{r}})\frac{g_{\mathrm{ACh}}}{g_{\mathrm{ACh}} + g_{\mathrm{m}}}, \tag{8.3}
$$
and the depolarization saturates as more channels open; this is the origin of the nonlinear summation in Example 8.3.2.

### 8.4.2. Termination of the Signal

The lifetime of ACh in the cleft is less than $1\,\mathrm{ms}$. Acetylcholinesterase on the basal lamina is one of the fastest enzymes, each active center hydrolyzing about $10^4$ ACh molecules per second; a considerable fraction of ACh is hydrolyzed before it reaches the receptors, and the rest is hydrolyzed soon after dissociating from the receptors. The end-plate current therefore decays within about $1$–$2\,\mathrm{ms}$, and its time course is determined essentially by the rate of channel closing.

**Example 8.4.1 (Diffusion Is Not the Bottleneck)** Take the diffusion coefficient of ACh as $D \approx 4\times10^{-10}\,\mathrm{m^2\,s^{-1}}$; the time to cross a $50\,\mathrm{nm}$ cleft is $t \approx x^2/(2D) = (5\times10^{-8})^2/(8\times10^{-10})\,\mathrm{s} \approx 3\,\mu\mathrm{s}$, two orders of magnitude shorter than the synaptic delay (about $500\,\mu\mathrm{s}$). The speed of the synapse depends on the $\ce{Ca^2+}$ channels, fusion and receptor gating, not on diffusion.

The junction has multiple negative feedbacks so that each nerve impulse produces only one brief end-plate potential, thereby preserving the one-to-one relation between nerve and muscle:

- cholinesterase hydrolyzes ACh and diffusion removes ACh from the cleft;
- receptors continuously exposed to ACh undergo **desensitization**, closing even though ACh is still present;
- $\ce{Ca^2+}$ in the terminal activates $\mathrm{K^+}$ channels that repolarize the terminal, and $\ce{Ca^2+}$ is pumped out or taken up by the endoplasmic reticulum and mitochondria;
- at high-frequency stimulation fewer vesicles are releasable and the amount released falls (short-term depression);
- inactivation of $\mathrm{Na^+}$ channels on the sarcolemma and the refractory period allow one end-plate potential to trigger only one muscle action potential.

### 8.4.3. The Safety Factor

A normal junction releases much more transmitter than is needed to trigger an action potential.

**Definition 8.4.2 (Safety Factor)** The ratio of the amplitude of the end-plate potential to the depolarization needed to trigger a muscle action potential is called the **safety factor** of neuromuscular transmission.

The safety factor in mammals is usually about 3–5, and lower in humans (about 2–3). The safety factor keeps transmission reliable during high-frequency firing, temperature changes and disease, at the cost of releasing several times more transmitter with each impulse.

Panel C illustrates the meaning of the safety factor. In a stimulus train the quantal content falls step by step (fewer releasable vesicles) and reaches about 60% at the 4th–5th stimulus. In a normal junction the end-plate potential is still nearly twice the threshold; but when the safety factor falls to near 1, the same decline makes more and more fibers fail to transmit. This is the manifestation of myasthenia gravis and the principle of its electrodiagnosis (Section 8.7): after repeated effort muscle strength progressively weakens, and with $3\,\mathrm{Hz}$ stimulation of the nerve the compound muscle action potential decrements from one stimulus to the next.

## 8.5. The Skeletal Muscle Action Potential and Excitation–Contraction Coupling

### 8.5.1. The Action Potential of Skeletal Muscle

The action potential of the skeletal muscle fiber has the same mechanism as that of the neuron (opening and inactivation of voltage-gated $\mathrm{Na^+}$ channels, opening of delayed-rectifier $\mathrm{K^+}$ channels, [Chapter 4](/7.14.4)), with different parameters:

| Parameter | Neuron | Skeletal muscle fiber | Notes |
|---|---|---|---|
| Resting potential | $-65$ to $-70\,\mathrm{mV}$ | $-85$ to $-90\,\mathrm{mV}$ | About 70%–80% of the resting conductance of the sarcolemma comes from $\mathrm{Cl^-}$ channels (ClC-1), which stabilize the membrane potential |
| **Threshold potential** | About $-55\,\mathrm{mV}$ | About $-60$ to $-55\,\mathrm{mV}$ | Similar |
| Overshoot peak | $+30$ to $+40\,\mathrm{mV}$ | $+20$ to $+30\,\mathrm{mV}$ | Determined by $\mathrm{Na^+}$ influx |
| Duration | $1$–$2\,\mathrm{ms}$ | $2$–$5\,\mathrm{ms}$ | The capacitance of the transverse tubule membrane slows repolarization somewhat |
| **Absolute refractory period** | About $1\,\mathrm{ms}$ | About $1$–$3\,\mathrm{ms}$ | Slightly longer in skeletal muscle |
| **Conduction velocity** | $1$–$120\,\mathrm{m\,s^{-1}}$ | $3$–$5\,\mathrm{m\,s^{-1}}$ | Muscle fibers are unmyelinated, and velocity increases only with the square root of diameter |
| Function | Transmits information | Triggers contraction | |

The role of ClC-1 is seen most clearly in disease: in patients with myotonia congenita ClC-1 function is lost, the sarcolemmal conductance is reduced, the muscle fiber continues to fire action potentials after a voluntary contraction, and the muscle cannot relax in time. During high-frequency firing $\mathrm{K^+}$ accumulates in the narrow transverse tubules and depolarizes the tubule membrane, which is another reason why the $\mathrm{Cl^-}$ conductance is important: the $\mathrm{Cl^-}$ conductance weakens the effect on **excitability** of the depolarization caused by $\mathrm{K^+}$ accumulation.

The action potential propagates from the end plate in the middle toward both ends. For a fiber $10\,\mathrm{cm}$ long, propagation over $5\,\mathrm{cm}$ at $4\,\mathrm{m\,s^{-1}}$ takes about $12.5\,\mathrm{ms}$, which is not negligible compared with the rise time of the **twitch** of fast muscle (about $10$–$40\,\mathrm{ms}$); this is one reason why the end plate usually lies in the middle of the fiber.

### 8.5.2. Transverse Tubules and Triads

The diameter of a muscle fiber can reach $100\,\mu\mathrm{m}$, yet contraction must begin synchronously over the whole cross section within a few milliseconds after the action potential. A. V. Hill (1949) pointed out that no substance diffusing in from the surface could achieve this.

**Example 8.5.1 (Hill's Diffusion Argument)** The diffusion coefficient of $\ce{Ca^2+}$ in sarcoplasm is at most about $5\times10^{-10}\,\mathrm{m^2\,s^{-1}}$ (the effective value is smaller when it is buffered). Diffusion from the surface to the center of a fiber of radius $50\,\mu\mathrm{m}$ needs $t \approx r^2/(2D) = (5\times10^{-5})^2/(10^{-9})\,\mathrm{s} \approx 2.5\,\mathrm{s}$, about two orders of magnitude longer than the whole time course of a twitch. The activating signal must therefore be conducted electrically into the interior of the cell and release $\ce{Ca^2+}$ in situ near each sarcomere.

The pathway of entry is the transverse tubule (T tubule): tubes formed by periodic invaginations of the sarcolemma, about $20$–$40\,\mathrm{nm}$ in diameter, located in mammals at the junction of the A band and the I band of each sarcomere (two per sarcomere) and in the frog at the Z line; the lumen communicates with the **extracellular fluid**, the tubule membrane can conduct action potentials, and the action potential reaches the center of the fiber in about $1\,\mathrm{ms}$. The **sarcoplasmic reticulum** ([7.3.7](/7.3.7#def-7.5.1)) is the **smooth endoplasmic reticulum** surrounding each myofibril, and it swells into terminal cisternae on both sides of the transverse tubule.

**Definition 8.5.1 (Triad)** The structure formed in skeletal muscle by a transverse tubule and the two terminal cisternae on either side, closely apposed (gap about $12\,\mathrm{nm}$), is called a **triad**. It is the structural unit of excitation–contraction coupling: the voltage sensors on the transverse tubule membrane lie directly opposite the $\ce{Ca^2+}$ release channels on the terminal cisternal membrane. In cardiac muscle the transverse tubule is apposed to only one terminal cisterna, forming a dyad ([Chapter 10](/7.14.10)).

**Definition 8.5.2 (Excitation–Contraction Coupling)** The process that converts the action potential on the sarcolemma (an electrical signal) into a rise of cytosolic $\ce{Ca^2+}$ concentration and thereby initiates filament sliding (mechanical activity) is called **excitation–contraction coupling**. Its structural basis is the transverse tubule–sarcoplasmic reticulum system, and the coupling factor is $\ce{Ca^2+}$.

### 8.5.3. DHPR–RyR1 Mechanical Coupling

```mermaid
flowchart LR
  A["Sarcolemmal action potential"] --> B["Conduction down the T tubule"]
  B --> C["Conformational change of the DHPR voltage sensor"]
  C --> D["Mechanical opening of RyR1"]
  D --> E["Ca²⁺ release from the terminal cisterna"]
  E --> F["Ca²⁺ binds troponin C"]
  F --> G["Cross-bridge cycle, filament sliding"]
  E --> H["SERCA pumps Ca²⁺ back"]
  H --> I["Relaxation"]
```

The **voltage sensor** on the transverse tubule membrane is the dihydropyridine receptor (DHPR), the L-type $\ce{Ca^2+}$ channel $\mathrm{Ca_V1.1}$; the release channel on the terminal cisternal membrane is the ryanodine receptor RyR1, a homotetramer of about $2.2\,\mathrm{MDa}$ and the largest ion channel known. In the triad the RyR1 molecules are arranged in a regular checkerboard array; every second RyR1 has its cytoplasmic domain directly opposite a group of four DHPRs (a "tetrad"). On depolarization the voltage sensor of the DHPR moves (measurable as a charge movement, Schneider and Chandler, 1973) and pulls RyR1 open through direct protein–protein contact (adaptor proteins such as STAC3 are also required). The half of the RyR1 molecules not attached to DHPRs may be opened by $\ce{Ca^2+}$ released nearby, amplifying release. This coupling is also bidirectional: RyR1 in turn enhances the $\ce{Ca^2+}$ current of the DHPR itself.

Because the coupling is mechanical, skeletal muscle contraction does not require entry of extracellular $\ce{Ca^2+}$: in a $\ce{Ca^2+}$-free solution, frog skeletal muscle can still contract normally for some time (until the stores of the sarcoplasmic reticulum are depleted), whereas cardiac muscle stops within a few beats ([Chapter 10](/7.14.10)). The $\ce{Ca^2+}$ current of the DHPR in skeletal muscle is slow and small and is not necessary for the twitch.

Mutations of RyR1 cause malignant hyperthermia: in carriers exposed to halogenated anesthetics or succinylcholine, RyR1 stays open, the sarcoplasmic reticulum releases $\ce{Ca^2+}$ uncontrollably, and the result is muscle rigidity, massive ATP consumption, a sharp rise in heat production, **acidosis** and hyperkalemia, which can be fatal if untreated; the RyR1 inhibitor dantrolene is the specific remedy.

## 8.6. Ca²⁺ Release, Reuptake and Relaxation

The $\ce{Ca^2+}$ released from the sarcoplasmic reticulum by one action potential amounts to about $300$–$400\,\mu\mathrm{mol\,L^{-1}}$ by sarcoplasmic volume, but most of it is bound immediately: the cytosolic free $[\ce{Ca^2+}]$ rises from about $0.05$–$0.1\,\mu\mathrm{mol\,L^{-1}}$ at rest to about $10$–$20\,\mu\mathrm{mol\,L^{-1}}$ within 1–2 ms and falls back within a few milliseconds; the regulatory sites of troponin C, ATP and the abundant parvalbumin in the fast muscle of small mammals take up the released $\ce{Ca^2+}$. Binding of $\ce{Ca^2+}$ to troponin C moves tropomyosin aside and allows the cross-bridges to bind ([Chapter 9](/7.14.9)).

Termination of contraction requires removing $\ce{Ca^2+}$ from the cytosol, by two routes, both active processes:

- Reuptake (the main route): SERCA (sarco/endoplasmic reticulum $\ce{Ca^2+}$-ATPase, SERCA1a in fast muscle and SERCA2a in slow and cardiac muscle) on the sarcoplasmic reticulum membrane pumps two $\ce{Ca^2+}$ into the sarcoplasmic reticulum per ATP hydrolyzed; it is a **P-type ATPase**. It makes up most of the membrane protein of the sarcoplasmic reticulum of fast muscle.
- Extrusion (the minor route): the plasma membrane $\ce{Ca^2+}$-ATPase and the $\mathrm{Na^+}$–$\ce{Ca^2+}$ exchanger on the sarcolemma.

Calsequestrin in the lumen of the sarcoplasmic reticulum is a buffer protein of low affinity ($K_{\mathrm{d}} \approx 1\,\mathrm{mmol\,L^{-1}}$) and high capacity (about 40–50 $\ce{Ca^2+}$ bound per molecule), concentrated in the terminal cisternae. It has two functions: it increases the $\ce{Ca^2+}$ capacity of the sarcoplasmic reticulum, and it keeps the luminal free $\ce{Ca^2+}$ at a submillimolar level, thereby delaying the inhibition of SERCA by high luminal $\ce{Ca^2+}$.

**Example 8.6.1 (The Thermodynamic Limit of SERCA)** Pumping 2 $\ce{Ca^2+}$ from cytosol at $0.1\,\mu\mathrm{mol\,L^{-1}}$ into a sarcoplasmic reticulum with free $\ce{Ca^2+}$ of $0.5\,\mathrm{mmol\,L^{-1}}$ (there is almost no potential difference across the sarcoplasmic reticulum membrane, because it is permeable to $\mathrm{K^+}$ and $\mathrm{Cl^-}$) requires at $37\,^\circ\mathrm{C}$ a free energy of
$$
\Delta G = 2RT\ln\frac{c_{\mathrm{SR}}}{c_{\mathrm{cyt}}} = 2\times2.58\,\mathrm{kJ\,mol^{-1}}\times\ln(5\times10^3) \approx 44\,\mathrm{kJ\,mol^{-1}},
$$
which is smaller than the free energy of ATP hydrolysis in muscle (about $-60\,\mathrm{kJ\,mol^{-1}}$). If all the luminal $\ce{Ca^2+}$ were free (more than ten $\mathrm{mmol\,L^{-1}}$), the concentration ratio would rise to $10^5$, the free energy required would be about $59\,\mathrm{kJ\,mol^{-1}}$, and the pump would come close to stalling. The buffering by calsequestrin allows the sarcoplasmic reticulum to store large amounts of $\ce{Ca^2+}$ without reaching this thermodynamic limit.

The energy cost of the $\ce{Ca^2+}$ pump is considerable: of the ATP consumed by muscle during contraction, about 30%–40% goes to SERCA, most of the rest to the cross-bridge cycle, and a little to the **sodium pump**. Relaxation therefore needs ATP just as contraction does; after death ATP is exhausted, the cross-bridges remain tightly bound to actin, and the muscle stiffens (rigor mortis, [7.3.13](/7.3.13#sec-13.5.2)). After prolonged activity the sarcoplasmic reticulum gradually loses $\ce{Ca^2+}$; when sarcoplasmic reticulum $\ce{Ca^2+}$ falls, STIM1 on the sarcoplasmic reticulum membrane activates Orai1 channels on the sarcolemma, replenishing $\ce{Ca^2+}$ from outside the cell (store-operated $\ce{Ca^2+}$ entry).

![Sarcoplasmic Ca²⁺ transient of a fast muscle fiber (single-compartment model, parameters taken from a mouse fast-muscle model and rounded; µM is µmol/L). Each action potential releases 350 µM Ca²⁺; SERCA takes it up at a rate with Hill coefficient 2; the regulatory sites of troponin C (240 µM) bind fast, and parvalbumin (1500 µM) binds slowly because it must first release Mg²⁺. A: a single twitch: free Ca²⁺ rises to about 17 µM within 2 ms and falls back within about 5 ms; the occupancy of troponin C rises and falls accordingly, and parvalbumin slowly absorbs Ca²⁺. B: with parvalbumin removed, troponin occupancy lasts longer and relaxation is markedly slower; in this kind of fiber halving SERCA activity has little effect, because during a twitch parvalbumin first "takes" Ca²⁺ off troponin and SERCA then slowly pumps it back. C: action potential trains at 10, 30 and 80 Hz: when the interval between stimuli is shorter than the decay time of the transient, the occupancy summates stepwise and at 80 Hz fuses into a sustained high plateau, which is the basis of tetanic contraction (Chapter 9); later action potentials in the train release less (RyR1 inactivation and depletion of the stores)](./plots/calcium-transient.py)

## 8.7. Pharmacology and Diseases of the Neuromuscular Junction

Every step at the junction is acted on by natural toxins, drugs or diseases:

| Step | Drug, toxin or disease | Action | Result |
|---|---|---|---|
| Presynaptic $\ce{Ca^2+}$ channel | Lambert–Eaton myasthenic syndrome (autoantibodies against $\mathrm{Ca_V2.1}$, often with small-cell lung cancer); high $\ce{Mg^2+}$ | Reduced release | Weakness; unlike myasthenia gravis, $\ce{Ca^2+}$ accumulation during high-frequency stimulation transiently increases muscle strength |
| Vesicle fusion | Botulinum toxin (cleaves SNARE proteins such as SNAP-25) | Prevents ACh release | Flaccid paralysis; small doses are used to treat dystonia and for cosmetic purposes |
| Vesicle fusion | α-Latrotoxin (black widow spider) | Causes massive vesicle release until exhaustion | Spasm first, then paralysis |
| ACh synthesis | Hemicholinium-3 | Blocks the high-affinity uptake of choline | Gradual depletion of transmitter |
| ACh receptor | Tubocurarine | Competitive blockade | Muscle relaxation, used in surgical anesthesia (requires artificial ventilation) |
| ACh receptor | α-Bungarotoxin (Chen-Yuan Lee and Chuan-Chiung Chang, 1963) | Binds the α subunit almost irreversibly | Paralysis; later became a tool for labeling and purifying ACh receptors |
| ACh receptor | Succinylcholine | Continuous activation of the receptor | Depolarizing block: $\mathrm{Na^+}$ channels in the sarcolemma around the end plate remain inactivated |
| Cholinesterase | Neostigmine, pyridostigmine (reversible) | Prolong the action of ACh | Treatment of myasthenia gravis; reversal of competitive muscle relaxants |
| Cholinesterase | Organophosphate pesticides, nerve agents (irreversible) | ACh accumulates | Fasciculations first, then depolarizing block and paralysis of respiratory muscles; muscarinic symptoms (miosis, increased secretions); treated with atropine and cholinesterase reactivators |
| ACh receptor (autoimmune) | Myasthenia gravis (mostly anti-ACh receptor antibodies, a few anti-MuSK or anti-LRP4) | Receptors internalized, complement destroys the end-plate folds | Quantal size reduced, safety factor falls to near 1 |

The prevalence of myasthenia gravis is about 1–2 per 10,000 people; the typical manifestations are ptosis, diplopia and other extraocular muscle symptoms, and weakness that worsens with activity and improves with rest: the motor units of the extraocular muscles are small and fire at high frequency, and their safety factor is already low. The mechanism is quantified in panel C: fewer receptors reduce the effect of each quantum, the end-plate potential is only slightly above threshold, and the normal decline of quantal content during a train makes transmission fail. Cholinesterase inhibitors let each ACh molecule stay longer and bind receptors several times, which is equivalent to increasing the quantal size.

## 8.8. Evolution and Comparative Aspects

### 8.8.1. Electric Organs: End Plates Stripped of the Contractile Apparatus

The **electric organs** of the electric ray (*Torpedo*) and the electric eel (*Electrophorus*) are stacks of electrocytes, most of which derive from muscle cells: they have lost the contractile apparatus but retain, and greatly enlarge, one face of the cholinergically innervated end-plate membrane. The nerve impulse simultaneously activates the ACh receptors on this face (electric ray) or ACh receptors plus $\mathrm{Na^+}$ channels (electric eel), making the membrane potentials on the two faces of the electrocyte asymmetric, and with many electrocytes in series the discharge can reach tens to hundreds of volts (for the physical analysis see [7.6.30](/7.6.30#sec-30.8)). The terminals in the electric organ of *Torpedo* are filled with synaptic vesicles and are the classical material for observing synaptic vesicles by freeze-fracture electron microscopy; the density of ACh receptors in this tissue is extremely high, and Changeux et al. (1970) used α-bungarotoxin to identify the ACh receptor protein in the electric organ of *Electrophorus*; several laboratories then purified it from the electric organs of *Torpedo* and *Electrophorus*, making it the first neurotransmitter receptor to be isolated. Electric organs have arisen independently at least six times in fishes, nearly always by modification of muscle (the South American Apteronotidae are the exception, in which they are formed from the axons of motor neurons), showing that the end plate plus series arrangement is a module that evolution readily "reuses".

### 8.8.2. Vertebrates: Twitch Fibers and Tonic Fibers

The skeletal muscle fibers of the trunk and limbs of mammals are almost all "twitch fibers": one end plate per fiber, producing an all-or-none propagating action potential. Some muscles of amphibians, reptiles and birds (and the extraocular muscles, the middle-ear muscles and the intrafusal fibers of muscle spindles of mammals) also have "tonic fibers": they are innervated by several scattered junctions (grape-like terminals), the sarcolemma does not produce a propagating action potential, and the end-plate potentials at the individual junctions cause graded, slow and sustained contraction locally, suited to maintaining posture and to fine control of eye position. Thus "one end plate per fiber with an all-or-none action potential" is not the only scheme of vertebrate muscle but one specialized for fast and reliable movement.

### 8.8.3. Arthropods: Few Neurons, Multiterminal and Polyneuronal Innervation

The muscles of crustaceans and insects are innervated by very few motor neurons: for example, the opener muscle of the crayfish claw is innervated by only one excitatory and one inhibitory neuron. Each muscle fiber receives many terminals of the same neuron along its whole length (multiterminal innervation) and often receives innervation from several neurons (polyneuronal innervation, including fast and slow excitatory neurons and a common inhibitory neuron). The excitatory transmitter is glutamate (ionotropic glutamate receptors) and the inhibitory transmitter is GABA; inhibition acts both on the muscle fiber (increasing the $\mathrm{Cl^-}$ conductance) and on the excitatory terminal itself (presynaptic inhibition, Dudel and Kuffler, 1961). Many fibers produce only graded **local potentials** or $\ce{Ca^2+}$ action potentials. Muscle force is thus graded not by recruiting motor units but by the firing frequency of each neuron, by facilitation, and by the interplay of excitation and inhibition. The glutamatergic junction of the *Drosophila* larva is today one of the main models for studying synaptic development and plasticity.

### 8.8.4. Nematodes: Muscle Sends Out "Processes" to the Nerve

The body wall muscles of *Caenorhabditis elegans* reverse the vertebrate arrangement: it is not motor axons that grow onto the muscle, but each muscle cell that sends out several "muscle arms" to the dorsal and ventral nerve cords, where they form junctions with motor neurons. The excitatory input is cholinergic and the inhibitory input is GABAergic; nematodes have a characteristic ACh receptor subtype sensitive to levamisole, and anthelmintics such as levamisole and pyrantel selectively activate them, paralyzing the worm spastically without affecting the host. Another class of anthelmintic, ivermectin, acts on the glutamate-gated $\mathrm{Cl^-}$ channels characteristic of nematodes and arthropods.

### 8.8.5. Two Modes of Excitation–Contraction Coupling

The mode of coupling that depends on influx of extracellular $\ce{Ca^2+}$ followed by $\ce{Ca^2+}$-induced release from the sarcoplasmic reticulum is found in the muscles of invertebrates and in vertebrate cardiac and smooth muscle; it is the more general and also the more ancient mode, and many invertebrate muscles are excited by $\ce{Ca^2+}$ action potentials. The mode in which the DHPR mechanically gates RyR directly, and the corresponding DHPR tetrads, have so far been found only in the skeletal muscle of vertebrates and their close chordate relatives. Mechanical coupling frees the activation of skeletal muscle from fluctuations of extracellular $\ce{Ca^2+}$ and from the rate of $\ce{Ca^2+}$ influx, which suits fast, repeated contraction; the price is the loss of the means, available in cardiac muscle, of regulating contractile force by the amount of $\ce{Ca^2+}$ influx ([Chapter 10](/7.14.10)).

## Summary

| Step | Key structures and molecules | Quantitative points |
|---|---|---|
| Motor unit (Definition 8.1.1) | α motor neuron + the fibers it innervates | About 10 fibers in extraocular muscle, a thousand in postural muscle |
| Transmitter release | Active zone, $\mathrm{Ca_V2.1}$, SNARE | About 125–200 vesicles per impulse × about $10^4$ ACh; release $\propto [\ce{Ca^2+}]^4$ (Eq. (8.1)); synaptic delay about $0.5\,\mathrm{ms}$ |
| Quantal release (Definition 8.3.1) | One vesicle = one quantum | Poisson distribution (Eq. (8.2)); $m = \ln(N/N_0) = \bar V/\bar q$; MEPP about $0.4\,\mathrm{mV}$ |
| End-plate potential (Definition 8.4.1) | Muscle-type nicotinic receptor, reversal potential about $0\,\mathrm{mV}$ | About $40\,\mathrm{mV}$; nonlinear summation (Example 8.3.2); safety factor about 3 |
| Termination | Acetylcholinesterase, desensitization, diffusion | ACh lifetime $< 1\,\mathrm{ms}$; diffusion across the cleft about $3\,\mu\mathrm{s}$ (Example 8.4.1) |
| Muscle action potential | $\mathrm{Na_V1.4}$, ClC-1 | $-90\,\mathrm{mV}$, $2$–$5\,\mathrm{ms}$, $3$–$5\,\mathrm{m\,s^{-1}}$ |
| Excitation–contraction coupling (Definition 8.5.2) | Transverse tubule, triad (Definition 8.5.1), DHPR–RyR1 mechanical coupling | No extracellular $\ce{Ca^2+}$ needed; diffusion could not accomplish activation (Example 8.5.1) |
| Relaxation | SERCA, calsequestrin, parvalbumin | Free $\ce{Ca^2+}$ $0.1 \to 10$–$20 \to 0.1\,\mu\mathrm{mol\,L^{-1}}$; SERCA accounts for about 30%–40% of energy use (Example 8.6.1) |

Diseases and drugs (Section 8.7) interrupt each of these steps in turn; comparative physiology (Section 8.8) shows that "one end plate per fiber, all-or-none action potential, mechanical coupling" is a specialization of vertebrates for fast and reliable movement, while arthropods and nematodes achieve a different mode of control with few neurons, multiterminal innervation and graded potentials.

## Questions

1. Why is the amplitude of the end-plate potential much greater than that of a single **excitatory postsynaptic potential** on a central neuron? How does this difference relate to the respective functions of the two kinds of synapses?

   **Answer** One nerve impulse releases more than 100 quanta at the end plate, and the end plate has a large area, a high receptor density and junctional folds that enlarge the membrane area, so the end-plate potential reaches about $40\,\mathrm{mV}$, far above what is needed for threshold (safety factor about 3). The function of the neuromuscular junction is reliable one-to-one transmission: each nerve impulse must cause one muscle action potential. The function of central synapses is integration: a single synapse produces a potential of only about $0.1$–$1\,\mathrm{mV}$, and only after many excitatory inputs summate in time and space and are offset by inhibitory inputs is it decided whether the neuron fires ([Chapter 5](/7.14.5)).

2. A nerve is stimulated 250 times in a low-$\ce{Ca^2+}$ solution, and 92 stimuli give no response; the mean MEPP is $0.45\,\mathrm{mV}$. (a) Estimate the quantal content. (b) Predict the mean end-plate potential and the number of trials with exactly 2 quanta. (c) If extracellular $\ce{Ca^2+}$ is doubled (still within the low-concentration range), roughly what does $m$ become?

   **Answer** (a) $m = \ln(250/92) = 1.00$. (b) The mean end-plate potential is $\approx mq = 0.45\,\mathrm{mV}$; $\mathbb{P}(2) = \mathrm{e}^{-1}\cdot1^2/2! = 0.184$, about 46 trials. (c) At low $\ce{Ca^2+}$, $m \propto [\ce{Ca^2+}]^4$ (Eq. (8.1)), so after doubling $m \approx 2^4 = 16$; failures then almost never occur and quantal analysis must use the direct or variance method instead.

3. Why can skeletal muscle still contract in a $\ce{Ca^2+}$-free solution whereas cardiac muscle soon stops beating? What would happen to skeletal muscle if a drug blocked the voltage-sensor movement of the DHPR (rather than its $\ce{Ca^2+}$ current)?

   **Answer** The DHPR of skeletal muscle pulls RyR1 open directly by a conformational change, and all the released $\ce{Ca^2+}$ comes from the sarcoplasmic reticulum, so no $\ce{Ca^2+}$ needs to enter the cell; cardiac muscle needs $\ce{Ca^2+}$ entering through L-type channels to trigger the opening of RyR2 (**calcium-induced calcium release**), and without external calcium there is no trigger signal ([Chapter 10](/7.14.10)). If the movement of the voltage sensor is blocked, RyR1 does not open even though the sarcolemmal action potential is normal, excitation–contraction coupling is interrupted, and the muscle does not contract; blocking only the $\ce{Ca^2+}$ current (as dihydropyridine drugs do in skeletal muscle) has little effect on the twitch.

4. Why does organophosphate poisoning first produce fasciculations and then muscle weakness and even respiratory paralysis?

   **Answer** After cholinesterase is irreversibly inhibited, ACh persists in the cleft: at first the end-plate potential of each nerve impulse is prolonged and can trigger several action potentials on the sarcolemma, and even excite the fiber spontaneously in the absence of impulses, appearing as fasciculations; later the end plate stays depolarized, the voltage-gated $\mathrm{Na^+}$ channels of the sarcolemma around the end plate remain inactivated and can no longer produce action potentials (depolarizing block), the receptors gradually desensitize, transmission is interrupted, and the respiratory muscles such as the diaphragm are paralyzed. Treatment uses atropine to counter the muscarinic effects and a reactivator to restore the enzyme before it "ages", with artificial ventilation when needed.

5. (Open question) Use the data of this chapter to estimate the ATP consumption of $\ce{Ca^2+}$ reuptake in one twitch, compare it with the ATP consumed by the cross-bridges in one twitch, and explain why muscles that contract rapidly and repeatedly (such as the sound-producing muscles of the rattlesnake and the swim-bladder muscles of fishes) often have an extremely well-developed sarcoplasmic reticulum and a very high density of SERCA.

   **Answer** Outline: each action potential releases about $350\,\mu\mathrm{mol\,L^{-1}}$ $\ce{Ca^2+}$ (by sarcoplasmic volume), and SERCA pumps 2 per ATP, so each twitch consumes about $175\,\mu\mathrm{mol\,L^{-1}}$ ATP for reuptake; taking the cross-bridges to account for about 60%–70% of the energy use, their consumption is about 1.5–2.3 times this. The higher the contraction frequency, the more releases and reuptakes per second, and in each contraction $\ce{Ca^2+}$ must be lowered before the next stimulus, otherwise the twitches fuse into tetanus (panel C). Ultrafast muscles that vibrate hundreds of times per second therefore give most of their volume to sarcoplasmic reticulum and mitochondria, have few myofibrils, and have a small twitch force: they trade force for speed. In contrast, the **asynchronous flight muscles** of insects escape the need to cycle $\ce{Ca^2+}$ at each contraction by using delayed stretch activation ([Chapter 10](/7.14.10)).
