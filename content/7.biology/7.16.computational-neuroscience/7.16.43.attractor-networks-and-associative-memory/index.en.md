---
title: Attractor Networks and Associative Memory
description: "Persistent activity and attractors; Hebb's cell assemblies and Marr's analysis of associative memory; the Amari–Hopfield model, its energy function and convergence; storage capacity by the signal-to-noise argument, the critical load 0.138, spurious states and sparse codes; CA3 as an autoassociative network; sequences, free recall and its scaling law; dense associative memory, modern Hopfield networks and attention; key–value memory."
---

How does a network of neurons hold a memory and recall it from a fragment? The answer proposed by Hebb, made precise by Amari and Hopfield, and tested in the hippocampus is that a memory is a stable pattern of activity, an **attractor** of the network dynamics, stored in the synaptic weights by Hebbian plasticity; recall is the relaxation of the network from a cue to the nearest attractor. This chapter develops that idea quantitatively. We begin with the persistent activity that motivates it, define associative memory and the Amari–Hopfield model, and prove that the dynamics descends an energy function. We then compute how many patterns such a network can store, apply the theory to area CA3 of the hippocampus ([7.16.42](/7.16.42)), extend it to sequences and to the statistics of free recall, and end with the dense associative memories whose capacity exceeds the number of neurons and whose update rule is the attention operation of Transformers. The **Hopfield network** itself, with its Ising-model background, is defined in [7.6.33](/7.6.33#sec-33.7), and the energy functions of symmetric rate networks in [7.16.15](/7.16.15#sec-15.3); here we treat its neuroscience and its statistical mechanics. Attractors of continuous variables, which store a location or a direction rather than a discrete item, are the subject of [7.16.44](/7.16.44), and their use as a **working memory** of [7.16.45](/7.16.45).

## 43.1. Persistent Activity and Attractors

Fuster and Alexander (1971) recorded neurons in the prefrontal cortex of monkeys performing a delayed response task: the monkey saw where food was hidden, waited several seconds behind a screen and then chose. Many neurons fired at an elevated rate throughout the delay, after the cue had disappeared. Funahashi, Bruce and Goldman-Rakic (1989) made the finding spatially specific with an oculomotor delayed-response task: the monkey fixated, a target flashed at one of eight locations, and after a delay of several seconds the monkey made an eye movement to the remembered location. Individual neurons in the dorsolateral prefrontal cortex fired during the delay only when the remembered location was in their "memory field", and errors were preceded by a decay of this activity. Activity that persists after its cause has gone is the simplest neural correlate of a memory ([7.16.45](/7.16.45)).

**Persistent activity** needs an explanation, because single neurons forget their input within tens of milliseconds, the **membrane time constant**, and synapses within a few hundred milliseconds. A recurrent network can do better. Its state follows a dynamical system, and if the system has several stable fixed points, a transient input can switch it from one to another, where it stays. Each stable state is an **attractor** ([Definition 33.2.1](/7.6.33#def-33.2.1)), and the set of initial states that flow to it is its **basin of attraction**. A network with many attractors is a memory: storing a pattern means making it an attractor, and recalling it from a partial cue means starting inside its basin. Attractors come in several kinds, which serve different memories: discrete point attractors for items, the subject of this chapter; continuous families of fixed points, line and **ring attractors**, for continuous variables such as eye position and head direction ([7.16.44](/7.16.44)); limit cycles for rhythms ([7.16.15](/7.16.15)); and chaotic attractors ([7.16.31](/7.16.31)).

## 43.2. Cell Assemblies and Associative Memory

### 43.2.1. Hebb's Cell Assembly

Hebb (1949) proposed both a learning rule and a unit of representation. The rule, **Hebb's rule**, states that a synapse is strengthened when the presynaptic cell repeatedly takes part in firing the postsynaptic cell (Formula 22.1.1). Its consequence in a recurrent network is the assembly.

**Definition 43.2.1 (Cell Assembly)** A **cell assembly** is a group of neurons that have been repeatedly co-active, and that have therefore strengthened their mutual excitatory connections by Hebbian plasticity, so that the activation of part of the group activates the rest and the group as a whole can sustain its activity after the stimulus ends.

An assembly represents a percept or concept by the identity of its members, and it has the two properties needed for memory: it reverberates, which explains persistent activity, and it completes itself from a part, which explains recall from partial cues. Because a neuron can belong to many assemblies, a population of $N$ neurons can represent far more than $N$ items. Hebb's ideas were speculative for decades; the experiments of the last twenty years, from engram cells ([7.16.42](/7.16.42#sec-42.6)) to the optogenetic imprinting of artificial assemblies in mouse visual cortex by repeated co-activation (Carrillo-Reid, Yang, Bando, Peterka and Yuste, 2016), which then responded together to stimulation of a few members, support them.

### 43.2.2. Associative Memory at Marr's Three Levels

Associative memory is a good example of the three levels of description of [7.16.1](/7.16.1), **Marr's levels of analysis**. At the computational level the problem is to recall an item from incomplete or corrupted information about it: to be content-addressable. Computers address memory by location, and searching by content is expensive for them; brains find a face from a glimpse or a word from its meaning effortlessly. At the algorithmic level, one solution is a dynamical system whose fixed points are the stored items, which carries any starting point to the nearest of them. At the implementational level, the dynamical system is a recurrent network of threshold neurons with Hebbian weights.

**Definition 43.2.2 (Associative Memory)** An **associative memory** is a system that stores a set of patterns and, given a cue, retrieves the stored pattern most similar to it. In an *autoassociative* memory the cue is a partial or noisy version of the pattern to be retrieved; in a *heteroassociative* memory a cue pattern retrieves a different pattern associated with it (a key retrieves a value).

The capacity, the robustness to noise in the cue and the size of the basins of the stored patterns are the measures of an associative memory, and the theory below computes them.

## 43.3. The Amari–Hopfield Model

### 43.3.1. The Model

Amari (1972) studied networks of threshold elements that learn patterns and pattern sequences by self-organization and showed that stored patterns are stable states recalled from neighboring patterns; Hopfield (1982) introduced the energy function and the statistical mechanics that made the model a field of physics. We use the notation of this course, with $w_{ij}$ the weight from neuron $j$ to neuron $i$ (written $J_{ij}$ in [7.6.33](/7.6.33#sec-33.7)).

**Formula 43.3.1 (Amari–Hopfield Model)** A network of $N$ binary neurons with states $x_i \in \{-1, +1\}$ (active or silent) stores $K$ patterns $\boldsymbol{\xi}^\mu \in \{-1, +1\}^N$, $\mu = 1, \dots, K$, in the Hebbian weights
$$
w_{ij} = \frac{1}{N}\sum_{\mu=1}^{K}\xi_i^\mu\xi_j^\mu \quad (i \ne j), \qquad w_{ii} = 0, \tag{43.1}
$$
that is $W = \frac{1}{N}\sum_\mu\boldsymbol{\xi}^\mu(\boldsymbol{\xi}^\mu)^{\mathsf T} - \frac{K}{N}I_N$. The neurons are updated asynchronously, one at a time in random order, by
$$
x_i \leftarrow \operatorname{sgn}(h_i), \qquad h_i = \sum_j w_{ij}x_j - \theta_i, \tag{43.2}
$$
with local field $h_i$ and threshold $\theta_i$ (here $\theta_i = 0$, and $\operatorname{sgn}(0) = +1$).

Eq. (43.1) is one-shot learning: each pattern is presented once and adds its outer product to the weights, as Hebbian plasticity would if pattern $\mu$ were imposed on the network. The binary state $x_i = \pm 1$ is related to a 0/1 description of active and silent neurons by $x_i = 2n_i - 1$; the choice of $\pm 1$ makes the arithmetic symmetric. Why is a stored pattern stable? Insert $\boldsymbol{x} = \boldsymbol{\xi}^\nu$ into the local field:
$$
h_i = \frac{1}{N}\sum_{j \ne i}\sum_\mu\xi_i^\mu\xi_j^\mu\xi_j^\nu = \underbrace{\frac{N - 1}{N}\,\xi_i^\nu}_{\text{signal}} + \underbrace{\frac{1}{N}\sum_{\mu \ne \nu}\sum_{j \ne i}\xi_i^\mu\xi_j^\mu\xi_j^\nu}_{\text{crosstalk}}. \tag{43.3}
$$
The signal has the sign of $\xi_i^\nu$ and magnitude close to 1. If the patterns were orthogonal the crosstalk would vanish and every pattern would be a fixed point; random patterns are only nearly orthogonal, and the crosstalk is a sum of $(K - 1)(N - 1)$ random terms of size $1/N$, a noise whose size sets the capacity (Section 43.4). It is useful to describe the state by its overlaps with the patterns,
$$
m_\mu = \frac{1}{N}\sum_i\xi_i^\mu x_i \in [-1, 1], \tag{43.4}
$$
in terms of which $h_i = \sum_\mu\xi_i^\mu m_\mu - (K/N)x_i$: each neuron is pulled toward each pattern in proportion to the current overlap with it. Retrieval of pattern $\nu$ means $m_\nu \to 1$ with the other overlaps of order $1/\sqrt N$.

### 43.3.2. The Energy Function

**Theorem 43.3.1 (Convergence of the Amari–Hopfield Network)** For any symmetric weights $w_{ij} = w_{ji}$ with $w_{ii} \ge 0$, the function
$$
E(\boldsymbol{x}) = -\frac{1}{2}\sum_{i,j}w_{ij}x_ix_j + \sum_i\theta_ix_i \tag{43.5}
$$
does not increase under the asynchronous update (43.2), and decreases strictly whenever a neuron changes its state. Hence every trajectory reaches a fixed point after finitely many changes, and the fixed points are the local minima of $E$ with respect to single flips.

**Proof** Let neuron $k$ change from $x_k$ to $x_k' = \operatorname{sgn}(h_k) = -x_k$. The terms of $E$ that contain $x_k$ are $-x_k\sum_{j \ne k}w_{kj}x_j + \theta_kx_k$ (using the symmetry of $W$) and $-\frac12 w_{kk}x_k^2$, which is constant because $x_k^2 = 1$. With $h_k' = \sum_{j \ne k}w_{kj}x_j - \theta_k$ the field without self-coupling, the change is
$$
\Delta E = -(x_k' - x_k)\,h_k' = -2x_k'h_k'.
$$
Now $h_k' = h_k - w_{kk}x_k = h_k + w_{kk}x_k'$, and both terms have the sign of $x_k'$, so $x_k'h_k' = \lvert h_k\rvert + w_{kk}$ and $\Delta E = -2(\lvert h_k\rvert + w_{kk}) \le 0$. Equality requires $h_k = 0$ and $w_{kk} = 0$; with the convention $\operatorname{sgn}(0) = +1$ such a change goes from $-1$ to $+1$ and can occur at most once per neuron between strict decreases. Since $E$ takes finitely many values on $\{-1, 1\}^N$, it can decrease only finitely often. $\square$

The energy is a **Lyapunov function** of the dynamics, and recall is a descent on an energy landscape whose valleys are the memories. With Hebbian weights and $\theta = 0$, $E = -\frac{N}{2}\sum_\mu m_\mu^2 + \frac{K}{2}$: the energy is lowest when the state has a large overlap with one pattern. Two remarks delimit the theorem. Symmetry is essential: with asymmetric weights the network can cycle (Section 43.6 uses this to store sequences). And the asynchronous order matters: if all neurons are updated simultaneously, the network can end on a two-cycle, alternating between two states; the corresponding Lyapunov function of synchronous dynamics has fixed points and two-cycles as its minima. Biological networks have no global clock, which favors the asynchronous version.

Hopfield (1984) showed that the same holds for graded neurons with continuous dynamics, $\tau\dot u_i = -u_i + \sum_jw_{ij}f(u_j)$ with a monotonic gain $f$, which is a firing-rate network (Formula 15.1.1) with symmetric weights. The energy
$$
E = -\frac{1}{2}\sum_{i,j}w_{ij}r_ir_j + \sum_i\int_0^{r_i}f^{-1}(r)\,\mathrm{d}r, \qquad r_i = f(u_i), \tag{43.6}
$$
satisfies $\dot E = -\sum_i\dot r_i\bigl(\sum_jw_{ij}r_j - u_i\bigr) = -\tau\sum_if'(u_i)\,\dot u_i^2 \le 0$ (Cohen and Grossberg, 1983; Hopfield, 1984), and in the high-gain limit its minima approach those of the binary network. Attractor memory is therefore not an artifact of binary units. Hopfield and Tank (1985) used the same descent to find good solutions of optimization problems, such as the traveling salesman problem, by designing weights whose energy is the cost function.

![Retrieval in the Amari–Hopfield network ($N = 500$, Hebbian weights, asynchronous updates; time in sweeps of $N$ updates). A: $K = 25$ patterns (load $\alpha = 0.05$); the cue is pattern 1 with 30% of its units flipped (overlap 0.4). The overlap with the cued pattern (thick) rises to 1 within about one sweep, while the overlaps with the other 24 patterns (thin) stay near zero: pattern completion. B: the energy (43.5) along the same trajectory decreases monotonically and becomes constant at the fixed point (Theorem 43.3.1). C: final against initial overlap for loads $0.05$, $0.10$ and $0.13$: cues with overlap above a threshold are completed; the threshold, and with it the size of the basin, grows with the load, and near $\alpha_c$ retrieval is no longer perfect. D: asymmetric weights $w_{ij} = N^{-1}\sum_\mu\xi_i^{\mu+1}\xi_j^\mu$ store a cycle of five patterns; with synchronous updates, a cue resembling $\boldsymbol{\xi}^1$ (overlap 0.6) is followed by the exact sequence $\boldsymbol{\xi}^2, \boldsymbol{\xi}^3, \dots$ (Section 43.6).](./plots/hopfield-recall.py)

The core of a simulation is a few lines of NumPy:

```python
import numpy as np

rng = np.random.default_rng(0)
N, K = 500, 25
X = rng.choice([-1.0, 1.0], size=(K, N))       # K random patterns
W = X.T @ X / N                                 # Hebbian outer-product rule
np.fill_diagonal(W, 0.0)

x = X[0].copy()
x[rng.random(N) < 0.3] *= -1                    # noisy cue
for sweep in range(5):                          # asynchronous updates
    for i in rng.permutation(N):
        x[i] = 1.0 if W[i] @ x >= 0 else -1.0
print("overlap with pattern 0:", X[0] @ x / N)
```

## 43.4. Storage Capacity

### 43.4.1. The Signal-to-Noise Argument

How many random patterns can be stored before recall fails? The crosstalk in Eq. (43.3) answers the question to a first approximation.

**Proposition 43.4.1 (Signal-to-Noise Ratio of the Hebbian Network)** Let the $K$ patterns be independent with independent, equiprobable entries $\pm 1$, and let the network be in a stored pattern $\boldsymbol{\xi}^\nu$. For large $N$ and $K$ with load $\alpha = K/N$, the crosstalk $C_i$ in Eq. (43.3), multiplied by $\xi_i^\nu$, is approximately Gaussian with mean 0 and variance $\alpha$, so the probability that a given neuron is unstable (its local field has the wrong sign) is
$$
P_{\mathrm{err}} = \mathbb{P}\bigl(\xi_i^\nu C_i < -1\bigr) \approx \Phi\Bigl(-\frac{1}{\sqrt{\alpha}}\Bigr), \tag{43.7}
$$
where $\Phi$ is the standard normal distribution function.

**Proof** $\xi_i^\nu C_i = N^{-1}\sum_{\mu \ne \nu}\sum_{j \ne i}\xi_i^\nu\xi_i^\mu\xi_j^\mu\xi_j^\nu$ is a sum of $(K - 1)(N - 1)$ terms $\pm 1/N$. For fixed $i$ and $\nu$ the products $\xi_i^\nu\xi_i^\mu\xi_j^\mu\xi_j^\nu$ over $\mu \ne \nu$, $j \ne i$ are independent, equiprobable $\pm 1$ (each contains the factor $\xi_j^\mu$, which appears in no other term). The sum therefore has mean 0 and variance $(K - 1)(N - 1)/N^2 \approx \alpha$, and by the central limit theorem it is approximately $\mathcal{N}(0, \alpha)$. The neuron is unstable when the crosstalk exceeds the signal, $(N - 1)/N \approx 1$, in the opposite direction. $\square$

At $\alpha = 0.1$, Eq. (43.7) gives $P_{\mathrm{err}} = \Phi(-3.16) \approx 0.08\%$; at $\alpha = 0.138$, $0.36\%$; at $\alpha = 0.2$, $1.3\%$ (figure below, B). Two capacity statements follow. If every bit of a pattern must be stable, with probability tending to 1 as $N \to \infty$, then $N P_{\mathrm{err}} \to 0$, which with the Gaussian tail $\Phi(-z) \approx \mathrm{e}^{-z^2/2}/(z\sqrt{2\pi})$ requires $1/\alpha \gtrsim 2\ln N$:
$$
K_{\max} \approx \frac{N}{2\ln N} \quad \text{(each pattern a fixed point)}, \qquad K_{\max} \approx \frac{N}{4\ln N} \quad \text{(all patterns simultaneously)} \tag{43.8}
$$
(McEliece, Posner, Rodemich and Venkatesh, 1987). For $N = 1000$, $N/(2\ln N) \approx 72$. If instead a small fraction of errors is tolerated, the capacity is proportional to $N$, $K_{\max} = \alpha_c N$.

### 43.4.2. The Critical Load and Spurious States

The signal-to-noise argument considers only the first update from an exact pattern. Once a few bits flip, the crosstalk changes, errors can cascade, and the question becomes whether a fixed point with large overlap survives. Amit, Gutfreund and Sompolinsky (1985) solved the model with the replica method of spin-glass theory and found the phase diagram: for $\alpha < \alpha_c \approx 0.138$ the network has retrieval states, fixed points with overlap $m \approx 0.97$–$1$ with each pattern (at $\alpha_c$, about $1.5\%$ of the bits are wrong); at $\alpha_c$ these states disappear discontinuously, the overlap drops to near zero, and the network becomes a spin glass with exponentially many minima unrelated to the patterns. The collapse is visible in simulations of modest size and sharpens as $N$ grows (figure below, A). Information-theoretically, at $\alpha_c$ the network stores about $0.14\,\mathrm{bit}$ per synapse.

![Storage capacity of the Amari–Hopfield network. A: final overlap after starting exactly in a stored pattern and running the asynchronous dynamics to convergence, against the load $\alpha = K/N$, for $N = 200$ (16 networks per point) and $N = 400$ (6 networks); dashed line, $\alpha_c \approx 0.138$. Below $\alpha_c$ the patterns are retrieved almost perfectly; above it the overlap falls steeply, more steeply for the larger network, as expected for a phase transition that is sharp only in the limit $N \to \infty$. B: fraction of unstable units in a stored pattern before any update ($N = 500$, dots) and the signal-to-noise prediction $\Phi(-1/\sqrt\alpha)$ of Proposition 43.4.1 (line).](./plots/hopfield-capacity.py)

Not every attractor is a memory.

**Definition 43.4.1 (Spurious Attractor)** A **spurious attractor** is a stable state of an associative memory network that is not one of the stored patterns. In the Hebbian Amari–Hopfield network they include the reversed patterns $-\boldsymbol{\xi}^\mu$ (an exact consequence of the symmetry $E(\boldsymbol{x}) = E(-\boldsymbol{x})$), mixture states such as $\operatorname{sgn}(\boldsymbol{\xi}^1 + \boldsymbol{\xi}^2 + \boldsymbol{\xi}^3)$ that combine an odd number of patterns, and, at high load, spin-glass states unrelated to any pattern.

The symmetric three-pattern mixture has overlap $1/2$ with each component and is stable at low load; its energy is higher than that of a pure pattern, so with noise in the dynamics (a finite "temperature", equivalent to stochastic neurons with a sigmoidal firing probability) the network escapes from mixtures while still retrieving pure patterns. Mixture states have also been interpreted positively, as the representation of a category formed from its examples (Amari, 1977).

### 43.4.3. Improving the Capacity

The **Hebbian rule** is simple but not optimal. Three modifications raise the capacity, and each has a biological reading.

- *Sparse patterns.* Cortical and hippocampal codes are sparse: a fraction $a \ll 1/2$ of neurons is active in a pattern. With 0/1 neurons, the **covariance rule** $w_{ij} \propto \sum_\mu(\xi_i^\mu - a)(\xi_j^\mu - a)$ (Definition 22.3.1) and a threshold that keeps the activity at $a$, the capacity grows as $\alpha_c \approx 1/(2a\lvert\ln a\rvert)$ for small $a$ (Tsodyks and Feigel'man, 1988), far above $0.138$: for $a = 0.01$, $\alpha_c \approx 11$. Each pattern then carries less information, but the total information stored per synapse approaches the theoretical maximum of $1/(2\ln 2) \approx 0.72\,\mathrm{bit}$.
- *Nonlocal rules.* The pseudo-inverse rule $W = \Xi(\Xi^{\mathsf T}\Xi)^{-1}\Xi^{\mathsf T}$, with $\Xi$ the $N \times K$ matrix of patterns, makes any $K \le N$ linearly independent patterns, even correlated ones, exact fixed points (Personnaz, Guyon and Dreyfus, 1985; Kanter and Sompolinsky, 1987). It is not local, since each weight depends on all patterns, but it can be approached by iterative error-correcting rules.
- *Learned weights.* If the weights are trained by a perceptron rule to make each pattern stable with a margin, the capacity for random patterns reaches $\alpha = 2$, the maximum over all weight matrices (Gardner, 1988), the same bound as for the capacity of a perceptron ([7.16.33](/7.16.33)).

## 43.5. CA3 as an Autoassociative Memory

The anatomy of CA3 ([7.16.42](/7.16.42#sec-42.2)) matches the requirements of the model. Its pyramidal cells are densely interconnected by excitatory recurrent collaterals whose synapses show NMDA-receptor-dependent **long-term potentiation**; the mossy fiber inputs from the dentate gyrus are few and strong, suited to imposing a sparse, pattern-separated pattern on CA3 during storage, while the more numerous but weaker perforant path inputs from the entorhinal cortex can provide the cue during recall (Treves and Rolls, 1992). The theory then predicts the capacity. For a network of diluted connectivity in which each cell receives $C$ recurrent synapses and patterns have sparseness $a$, the number of storable patterns is approximately
$$
K_{\max} \approx k\,\frac{C}{a\ln(1/a)}, \tag{43.9}
$$
with a constant $k$ of order $0.2$–$0.3$ (Treves and Rolls, 1991). With $C \approx 12\,000$ and $a \approx 0.02$, $K_{\max}$ is of order $3 \times 10^4$ patterns for one rat CA3: large, but finite, which is one argument for the transfer of memories out of the hippocampus during consolidation ([7.16.42](/7.16.42#sec-42.7)).

The predictions about function have been tested in several ways. Mice lacking **NMDA receptors** in CA3 fail to recall a location from a reduced set of cues (Nakazawa et al., 2002), the behavioral signature of **pattern completion**. When the shape of an environment is morphed between a square and a circle that the rat has learned to distinguish, hippocampal **place cells** switch abruptly and coherently between two maps (Wills, Lever, Cacucci, Burgess and O'Keefe, 2005), as two attractors with a boundary between their basins would predict (with a different training protocol the change was gradual, Leutgeb et al., 2005, a reminder that the attractors are shaped by learning); and when a rat is "teleported" between two familiar environments by switching the lights, the hippocampal map flickers between the two representations for a few theta cycles before settling (Jezek, Henriksen, Treves, Moser and Moser, 2011). Intracellular recordings in mice in virtual reality showed directly that the membrane potential of CA3 cells has a subthreshold response to visual cues across the track, and that the cue drives firing only near the location of the current activity bump; after a cue shift or a change of context, the representation switched in a way well described by an attractor network of several ring maps with global inhibition (Zhao, Wang, Spruston and Magee, 2020; the model is developed in [7.16.44](/7.16.44)).

The analogy has limits. CA3 represents space, a continuous variable, for which continuous attractors are a better description; the patterns are not random, and correlated patterns interfere more; and the dynamics during recall are tied to theta and gamma oscillations rather than relaxing freely. The Amari–Hopfield model should be read as the simplest member of a family of attractor models, whose shared prediction is the abrupt, cue-insensitive switching between discrete states that the experiments show.

## 43.6. Sequences and Free Recall

### 43.6.1. Storing Sequences

Amari (1972) already noted that asymmetric Hebbian weights store sequences. If the weights associate each pattern with the next,
$$
w_{ij} = \frac{1}{N}\sum_\mu\xi_i^{\mu+1}\xi_j^\mu, \tag{43.10}
$$
then a state equal to $\boldsymbol{\xi}^\mu$ produces the local field $\boldsymbol{h} \approx \boldsymbol{\xi}^{\mu+1}$, and synchronous updates step through the sequence (figure in Section 43.3, D). Asynchronous neurons need a mechanism that holds each pattern for a while before the transition, such as a combination of symmetric weights that stabilize patterns and asymmetric weights acting through slow synapses (Sompolinsky and Kanter, 1986; Kleinfeld, 1986), or adaptation that destabilizes the current pattern ([7.16.44](/7.16.44)). Weights of the form (43.10) are what **spike-timing-dependent plasticity** learns from theta sequences, in which cells fire in the order of the animal's path ([7.16.42](/7.16.42#sec-42.5)), and sequence attractors of this kind are the standard model of hippocampal **replay** and of the chains of neurons that time the song of the zebra finch (premotor nucleus HVC).

### 43.6.2. The Statistics of Free Recall

In free recall, the classical paradigm of human episodic memory, a participant studies a list of words and then reports as many as possible in any order. Two regularities are robust. Recall depends on position in the list (the serial position curve is U-shaped): the first items (primacy effect) and the last items (recency effect, which disappears if recall is delayed by a distracting task) are recalled best. And the number of recalled items grows sublinearly with list length, approximately as a power law $R \propto M^{\beta}$ with $\beta \approx 0.5$ (Murray, Pye and Hockley, 1976), although recognition tests show that almost all items are stored (Standing, 1973): free recall is limited by retrieval, not storage.

Romani, Pinkoviezky, Rubin and Tsodyks (2013) proposed that recall is a walk among attractors. Each item is a sparse pattern in an attractor network; when the current memory is destabilized (by adaptation or oscillating inhibition), the network moves to the item whose pattern overlaps most with it, excluding the one it came from. The resulting walk is deterministic, given the similarity matrix of the items, and eventually enters a cycle, after which no new items are recalled.

**Proposition 43.6.1 (Scaling Law of Free Recall)** If the similarities between $M$ items are independent random numbers and recall moves from each item to the most similar item other than the preceding one, the expected number of distinct items recalled before the walk enters a cycle is, for large $M$,
$$
R \approx \sqrt{\frac{3\pi M}{2}}. \tag{43.11}
$$

The result (Naim, Katkov, Romani and Tsodyks, 2020) is parameter-free: for $M = 16$ it gives $R \approx 8.7$ and for $M = 64$, $R \approx 17$, and it matched the average recall in large online experiments with lists of words or facts without any fitted constant. The square-root law resembles the birthday problem, because the walk ends once it revisits an item, and in a random environment returns become likely after about $\sqrt M$ steps. The model's mechanism also explains the order of recall: successive items tend to be similar, and the more items a walk has visited, the more likely it is to return to one. The serial position effects require a further ingredient, a slowly drifting context signal that is stored with each item. In temporal context models (Howard and Kahana, 2002), the context active at study is partly reinstated at recall, which favors neighbors in time; **event boundaries** reset the context abruptly, so that order memory is better within an event than across events, the pattern found experimentally by Pu, Kong, Ranganath and Melloni (2022). Event structure is taken up again in [7.16.46](/7.16.46).

## 43.7. Dense Associative Memory and Modern Hopfield Networks

### 43.7.1. Higher-Order Energies

The capacity of the classical network is limited because the energy $E = -\frac{N}{2}\sum_\mu m_\mu^2$ changes slowly near a memory: many patterns contribute terms of similar size, and their crosstalk swamps the signal. Krotov and Hopfield (2016) proposed to sharpen each memory's contribution.

**Definition 43.7.1 (Dense Associative Memory)** A **dense associative memory** is a network of $N$ units $x_i = \pm 1$ storing patterns $\boldsymbol{\xi}^\mu$ in the energy
$$
E(\boldsymbol{x}) = -\sum_{\mu=1}^{K}F\bigl(\boldsymbol{\xi}^\mu\cdot\boldsymbol{x}\bigr), \tag{43.12}
$$
with a rapidly growing *separation function* $F$, such as $F(z) = z^n$ or $F(z) = \mathrm{e}^{z}$, and updated asynchronously so that each change lowers the energy: $x_i \leftarrow \operatorname{sgn}\bigl(\sum_\mu[F(\xi_i^\mu + s_i^\mu) - F(-\xi_i^\mu + s_i^\mu)]\bigr)$ with $s_i^\mu = \sum_{j \ne i}\xi_j^\mu x_j$.

For $F(z) = z^2$ the energy is that of the Hebbian network up to a constant. For $n > 2$, expanding $(\boldsymbol{\xi}^\mu\cdot\boldsymbol{x})^n$ produces interactions among $n$ neurons at a time, with weights given by sums of products of $n$ pattern entries; the capacity increases accordingly.

**Proposition 43.7.1 (Capacity of Dense Associative Memory)** For $F(z) = z^n$ and random patterns, the signal-to-noise ratio for the stability of a unit in a stored pattern is approximately $\mathrm{SNR}^2 = N^{n-1}/\bigl((2n - 3)!!\,K\bigr)$, so that the number of patterns that can be stored with error probability $\Phi(-z)$ per unit is
$$
K_{\max} \approx \frac{N^{n-1}}{(2n - 3)!!\,z^2}. \tag{43.13}
$$

**Proof** In pattern $\nu$, flipping unit $i$ changes the term $\mu = \nu$ from $N^n$ to $(N - 2)^n$: the energy gap (signal) is $N^n - (N - 2)^n \approx 2nN^{n-1}$. For $\mu \ne \nu$, $s = \boldsymbol{\xi}^\mu\cdot\boldsymbol{\xi}^\nu$ is approximately $\mathcal{N}(0, N)$, and its contribution to the energy difference for unit $i$ is $F(s + \xi_i^\mu) - F(s - \xi_i^\mu) \approx 2\xi_i^\mu F'(s) = \pm 2ns^{n-1}$, with random sign, mean 0 and variance $4n^2\,\mathbb{E}[s^{2n-2}] = 4n^2(2n - 3)!!\,N^{n-1}$, using the Gaussian moments $\mathbb{E}[s^{2k}] = (2k - 1)!!\,N^k$. Summing $K - 1$ independent such terms gives noise variance $4n^2(2n - 3)!!\,KN^{n-1}$, and the ratio of signal squared to noise variance is $N^{2n-2}/\bigl((2n - 3)!!\,KN^{n-1}\bigr)$. Requiring $\mathrm{SNR} \ge z$ gives Eq. (43.13). For $n = 2$ it reduces to $\mathrm{SNR}^2 = N/K = 1/\alpha$, as in Proposition 43.4.1. $\square$

For $n = 3$ the capacity grows as $N^2$, so that a network of 60 neurons stores more than a hundred patterns (figure below); with $F(z) = \mathrm{e}^z$ it grows exponentially in $N$ (Demircigil, Heusel, Löwe, Upgang and Vermet, 2017). The price is the higher-order interactions, which a biological network does not have as synapses. Krotov and Hopfield (2021) showed that they arise effectively in a two-layer network of $N$ feature neurons and $K$ hidden "memory" neurons, each memory neuron connected to the feature neurons by the weights $\boldsymbol{\xi}^\mu$ and having a steep nonlinearity; eliminating the hidden layer gives Eq. (43.12). Only ordinary pairwise synapses are needed, and the number of memories is then bounded by the number of hidden neurons, as in any lookup table. Mixtures of features and prototypes interpolate between the regimes: networks trained with small $n$ on handwritten digits learn memories that look like local features, and with large $n$, memories that look like whole digits, a transition between feature-matching and prototype theories of recognition. The XOR function, which no network with pairwise symmetric interactions can complete, is stored by $n = 3$ with four memories in three units.

![Dense associative memory. A: $N = 60$ units, random patterns, cue with 10% of the units flipped; fraction of cues retrieved exactly against the number $K$ of stored patterns for the energies $F(z) = z^n$ with $n = 2$ (the classical network), $3$ and $4$. The classical network fails above about $8$ patterns, close to $0.14N$; $n = 3$ stores about $130$ and $n = 4$ about $1000$, both far more than the number of units (dotted line, $K = N$). B: capacity predicted by Proposition 43.7.1 (with $z = 3$) against $N$ for $n = 2$ to $5$: it grows as $N^{n-1}$.](./plots/dense-memory.py)

### 43.7.2. Modern Hopfield Networks and Attention

Ramsauer et al. (2020) took the exponential separation function to continuous states. With the patterns as the columns of $\Xi = [\boldsymbol{\xi}^1, \dots, \boldsymbol{\xi}^K] \in \mathbb{R}^{N\times K}$ and a state $\boldsymbol{x} \in \mathbb{R}^N$, the energy
$$
E(\boldsymbol{x}) = -\frac{1}{\beta}\ln\sum_{\mu=1}^{K}\exp\bigl(\beta\,\boldsymbol{\xi}^\mu\cdot\boldsymbol{x}\bigr) + \frac{1}{2}\boldsymbol{x}\cdot\boldsymbol{x} + \text{const} \tag{43.14}
$$
is minimized iteratively (by the concave–convex procedure, which guarantees descent) by
$$
\boldsymbol{x}^{\mathrm{new}} = \Xi\,\operatorname{softmax}\bigl(\beta\,\Xi^{\mathsf T}\boldsymbol{x}\bigr), \tag{43.15}
$$
where the **softmax function** turns the similarities $\boldsymbol{\xi}^\mu\cdot\boldsymbol{x}$ into weights that sum to 1. Eq. (43.15) is a weighted average of the stored patterns, dominated by the most similar one. For large $\beta$ and well-separated patterns, a single update retrieves the nearest pattern with exponentially small error, and the capacity is exponential in $N$; for small $\beta$ or similar patterns, the fixed point is an average of several patterns, a metastable state.

Eq. (43.15) is the **attention mechanism** of Transformers ([4.7.6](/4.7.6#sec-6.2)): in scaled dot-product attention, a query $\boldsymbol{q}$ is compared with keys $\boldsymbol{k}^\mu$, and the output is the softmax-weighted average of values $\boldsymbol{v}^\mu$,
$$
\operatorname{Attention}(\boldsymbol{q}) = \sum_\mu\boldsymbol{v}^\mu\,\operatorname{softmax}_\mu\Bigl(\frac{\boldsymbol{k}^\mu\cdot\boldsymbol{q}}{\sqrt{d}}\Bigr), \tag{43.16}
$$
which is one step of a modern Hopfield network with $\beta = 1/\sqrt d$ when keys and values coincide, and a heteroassociative version when they differ. A Transformer layer can therefore be read as a memory retrieval in which the tokens of the context are the stored patterns. This reading has been made concrete for the circuits of trained models: "induction heads" copy a token that followed an earlier occurrence of the current token, by computing keys from the previous token, so that a query for the current token retrieves its successor, a sequence association like Eq. (43.10) implemented by attention. Whether the brain implements anything like Eq. (43.15) is open. Kozachkov, Kastanenka and Krotov (2023) showed that a network of neurons and astrocytes, whose processes contact many synapses at once, can compute an attention-like operation, but there is no direct evidence yet.

## 43.8. Key–Value Memory and Heteroassociation

Autoassociative memories retrieve a pattern from a degraded version of itself. Much of memory is heteroassociative: a name retrieves a face, a place retrieves an event. The simplest heteroassociative memory is the linear associator (Anderson, 1972; Kohonen, 1972; Willshaw, Buneman and Longuet-Higgins, 1969 for binary synapses), which stores pairs $(\boldsymbol{k}^\mu, \boldsymbol{v}^\mu)$ in $W = \sum_\mu\boldsymbol{v}^\mu(\boldsymbol{k}^\mu)^{\mathsf T}$ and retrieves $W\boldsymbol{k}^\nu = \lVert\boldsymbol{k}^\nu\rVert^2\boldsymbol{v}^\nu + \sum_{\mu \ne \nu}(\boldsymbol{k}^\mu\cdot\boldsymbol{k}^\nu)\boldsymbol{v}^\mu$, with crosstalk that vanishes for orthogonal keys. Its capacity, like that of the autoassociator, depends on how close to orthogonal the keys are, which is why sparse, decorrelated keys are valuable.

**Definition 43.8.1 (Key–Value Memory)** A **key–value memory** stores each item as two representations, a *key* used to address it and a *value* holding its content; retrieval compares a query with all keys and returns a combination of the values weighted by the match. Keys can be optimized for discriminability and values for fidelity, independently.

The separation is familiar from the index of a book, which helps to find a subject but contains nothing about it. Gershman, Fiete and Irie (2025) argued that memory in the brain is organized in this way: the hippocampus and medial temporal lobe store keys, sparse, pattern-separated indices well suited to addressing, and the neocortex stores the values, distributed representations of content. This "indexing" view, which goes back to Teyler and DiScenna (1986), explains why hippocampal damage impairs the retrieval of episodes whose content is held in cortex, why retrieval failures (tip-of-the-tongue states, memories that return later) are common although the content is intact, and why the sparse random expansion of the dentate gyrus ([7.16.42](/7.16.42#sec-42.2.2)) is useful: it is a hashing of the input into near-orthogonal keys. The same expansion–sparsening motif in the fly **mushroom body** implements **locality-sensitive hashing** of odors ([7.16.23](/7.16.23)), and the plastic synapses from **Kenyon cells** to output neurons then act as the value store, read out under dopaminergic teaching signals ([7.16.38](/7.16.38)).

Biologically plausible learning rules for key–value memories have been derived: keys can be stored by Hebbian plasticity of the input-to-hidden synapses, and values by non-Hebbian or three-factor rules on the hidden-to-output synapses (Tyulmankov, Fang, Vadaparty and Yang, 2021). Key–value memories are also the basis of the **Tolman–Eichenbaum machine**, in which the hippocampus binds sensory content to a structural code from the entorhinal cortex, a model whose memory-retrieval step is an attention operation ([7.16.46](/7.16.46)).

## Summary

- Persistent delay activity in prefrontal cortex suggests that memories are attractors of recurrent networks; Hebb's cell assemblies (Definition 43.2.1) are the original form of the idea, and associative memories (Definition 43.2.2) are content-addressable stores.
- The Amari–Hopfield model (Formula 43.3.1) stores patterns in Hebbian outer-product weights; with symmetric weights and asynchronous updates its energy decreases until a fixed point is reached (Theorem 43.3.1), also for graded neurons (Eq. (43.6)).
- The crosstalk between random patterns gives a bit error rate $\Phi(-1/\sqrt\alpha)$ (Proposition 43.4.1); perfect storage allows $N/(2\ln N)$ patterns, retrieval with few errors up to $\alpha_c \approx 0.138$, beyond which the network becomes a spin glass. Spurious attractors (Definition 43.4.1) include reversed and mixture states. Sparse codes, nonlocal rules and learned weights raise the capacity (up to $2N$).
- CA3, with its dense plastic recurrent collaterals, is modeled as an autoassociative memory of capacity of order $C/(a\ln(1/a))$ patterns; region-specific knockouts and abrupt map switching support the model.
- Asymmetric Hebbian weights store sequences; free recall as a walk among attractors predicts $R \approx \sqrt{3\pi M/2}$ (Proposition 43.6.1), and drifting context explains the serial position effects and the role of event boundaries.
- Dense associative memories (Definition 43.7.1) with energies $F(z) = z^n$ store about $N^{n-1}$ patterns (Proposition 43.7.1); the exponential version for continuous states updates by $\Xi\operatorname{softmax}(\beta\Xi^{\mathsf T}\boldsymbol{x})$, the attention operation.
- Key–value memories (Definition 43.8.1) separate addressing from content; the hippocampus may store keys and the neocortex values.

| Model | Energy / rule | Capacity for random patterns |
|---|---|---|
| Hebbian Amari–Hopfield, perfect recall | $-\frac12\sum w_{ij}x_ix_j$ | $N/(2\ln N)$ |
| Hebbian, small error | same | $0.138N$ |
| Sparse patterns (coding level $a$) | covariance rule | $N/(2a\lvert\ln a\rvert)$ |
| Pseudo-inverse / learned weights | nonlocal / perceptron | $N$ / $2N$ |
| Dense, $F(z) = z^n$ | $-\sum_\mu(\boldsymbol{\xi}^\mu\cdot\boldsymbol{x})^n$ | $\propto N^{n-1}$ |
| Modern Hopfield | log-sum-exp, softmax update | $\propto \mathrm{e}^{cN}$ |

## Questions

1. Show that if a Hopfield network has stored pattern $\boldsymbol{\xi}$, then $-\boldsymbol{\xi}$ is also a fixed point. Is this a problem for memory, and how is it avoided in networks of 0/1 neurons with sparse patterns?

   **Answer** The Hebbian weights are unchanged by $\boldsymbol{\xi}^\mu \to -\boldsymbol{\xi}^\mu$, and with $\theta = 0$ the update $x_i \leftarrow \operatorname{sgn}(\sum_jw_{ij}x_j)$ commutes with $\boldsymbol{x} \to -\boldsymbol{x}$ (except at $h_i = 0$), so $E(-\boldsymbol{x}) = E(\boldsymbol{x})$ and the negatives of all fixed points are fixed points. It is a problem only in that half of the attractors are not memories, and a cue is never close to the reversed pattern unless it is mostly wrong. In networks of 0/1 neurons with sparse patterns and a positive threshold (or global inhibition fixing the activity level at $a$), the reversed pattern would have a fraction $1 - a$ of the neurons active, which the threshold or the inhibition forbids, so the symmetry is broken and reversed states are not attractors.

2. A network of $N = 10\,000$ neurons stores random patterns with the Hebbian rule. Estimate the number of patterns for which (a) a given neuron in a given pattern is unstable with probability $10^{-3}$, (b) all bits of a given pattern are stable with high probability, (c) retrieval with a few percent of errors is possible.

   **Answer** (a) $\Phi(-z) = 10^{-3}$ gives $z \approx 3.09$, so $1/\sqrt\alpha = 3.09$, $\alpha = 0.105$, $K \approx 1050$. (b) By Eq. (43.8), $K \approx N/(2\ln N) = 10\,000/18.4 \approx 540$. (c) Up to $\alpha_c N \approx 1380$ patterns, with about 1.5% of the bits wrong at the limit. The three answers differ by less than a factor of 3 here, but (b) grows more slowly than $N$, so the difference increases with network size.

3. Show by an example of a two-neuron network that the energy (43.5) need not decrease under synchronous updates of all neurons, and that the network can then oscillate.

   **Answer** Take $N = 2$, $w_{12} = w_{21} = -1$, $\theta = 0$, and start at $(1, 1)$. Synchronously, both fields are $-1$, so the state becomes $(-1, -1)$; then both fields are $+1$, and the state returns to $(1, 1)$: a two-cycle, along which $E = -w_{12}x_1x_2 = 1$ stays constant. The energy (43.5) is not a Lyapunov function of synchronous dynamics; the function $L(t) = -\sum_{ij}w_{ij}x_i(t)x_j(t-1)$, which couples successive states, is nonincreasing, and its minima are fixed points and two-cycles (Goles and colleagues). Asynchronous updates, with which only one neuron changes at a time, avoid the cycle: from $(1, 1)$ updating neuron 1 gives $(-1, 1)$, which is a fixed point.

4. In the modern Hopfield update (43.15), take two stored patterns $\boldsymbol{\xi}^1, \boldsymbol{\xi}^2$ with $\boldsymbol{\xi}^1\cdot\boldsymbol{\xi}^1 = \boldsymbol{\xi}^2\cdot\boldsymbol{\xi}^2 = 1$ and $\boldsymbol{\xi}^1\cdot\boldsymbol{\xi}^2 = c$. Starting from $\boldsymbol{x} = \boldsymbol{\xi}^1$, compute the weight of $\boldsymbol{\xi}^2$ after one update. How large must $\beta$ be for the error to be below 1% when $c = 0.5$?

   **Answer** The similarities are $\boldsymbol{\xi}^1\cdot\boldsymbol{x} = 1$ and $\boldsymbol{\xi}^2\cdot\boldsymbol{x} = c$, so the softmax weight of $\boldsymbol{\xi}^2$ is $p_2 = \mathrm{e}^{\beta c}/(\mathrm{e}^{\beta} + \mathrm{e}^{\beta c}) = 1/(1 + \mathrm{e}^{\beta(1 - c)})$. For $p_2 < 0.01$ we need $\mathrm{e}^{\beta(1-c)} > 99$, $\beta > \ln 99/(1 - c) = 4.6/0.5 \approx 9.2$. The required inverse temperature grows as patterns become more similar; for small $\beta$ the update returns a blend of the two patterns, the metastable "averaging" regime that attention layers also use.

5. (Open question) The capacity of the CA3 network, of order $10^4$ patterns, is small compared with the number of episodes in a human life. Propose ways in which the brain could keep the hippocampal memory from saturating, and say how each could be tested.

   **Answer** Possible mechanisms are: (a) transfer and forgetting: consolidation moves memories to the neocortex, and synaptic decay or active forgetting (for example by adult neurogenesis in the dentate gyrus, which remodels the input to CA3) clears the hippocampal store; predicted: increasing neurogenesis after learning should accelerate forgetting of hippocampus-dependent memories, as found in mice (Akers et al., 2014). (b) Palimpsest learning rules with bounded weights, in which new memories overwrite the oldest gracefully instead of causing catastrophic collapse at $\alpha_c$; predicted: memory strength should decline smoothly with the number of intervening memories. (c) Indexing: the hippocampus stores only sparse keys, not content, so each episode costs few bits; predicted: hippocampal representations should carry little detailed content compared with cortical ones. (d) Sparse coding and the large human hippocampus raise the capacity by orders of magnitude (Eq. (43.9) with $C$ and $1/a$ larger). Each can be tested with engram labeling and long-term imaging of the same neurons across many learning episodes.
