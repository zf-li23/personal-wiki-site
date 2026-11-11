---
title: Decision-Making
description: "Perceptual decisions and the random-dot motion task; the speed–accuracy trade-off; the drift-diffusion model, its psychometric and chronometric functions and their derivation from first-passage theory; the sequential probability ratio test and the optimality of bounded accumulation; reward rate and the optimal bound; race and leaky competing accumulator models; evidence accumulation in LIP and its causal tests; the Wang attractor network, the reduced Wong–Wang model, its saddle and the critical boundary; value-based choice, orbitofrontal value signals and prospect theory; decision confidence, changes of mind and metacognition."
---

A decision is the point at which the brain stops gathering evidence and commits to an action. Perception, memory and value all feed into it, and in the laboratory its simplest form, choosing between two alternatives on the basis of noisy sensory evidence, has become one of the best-understood links between neurons and cognition. This chapter follows that case from behavior to circuits. We start with the psychophysics of the random-dot motion task and the trade-off between speed and accuracy, formalize it in the drift-diffusion model and show that this model implements the statistically optimal sequential test. We then turn to the neurons of the lateral intraparietal area whose firing rises to a threshold as evidence accumulates, and to attractor networks in which accumulation and commitment emerge from recurrent excitation and competition, the same mechanisms that sustain persistent activity in working memory ([7.16.45](/7.16.45)). The last two sections treat choices between goods, which depend on learned values ([7.16.37](/7.16.37), [7.16.39](/7.16.39)), and the confidence that accompanies a decision. The sensory evidence and its neurometric analysis come from [7.16.18](/7.16.18#sec-18.8) and [7.16.26](/7.16.26#sec-26.2); the statistics of hypothesis testing from [3.2.5](/3.2.5); the stochastic processes from [7.6.5](/7.6.5); and the phase-plane analysis from [7.16.15](/7.16.15) and [2.4.11](/2.4.11).

## 47.1. Perceptual Decisions

### 47.1.1. What a Decision Is

**Definition 47.1.1 (Decision)** A **decision** is a commitment to a proposition, an action or a plan, made on the basis of evidence, prior knowledge and the expected costs and benefits of the possible outcomes. In a *perceptual decision* the evidence concerns the state of the sensory world (is the motion leftward or rightward?) and a choice is objectively correct or wrong; in a *value-based decision* the alternatives are goods or actions that differ in subjective value, and a choice can only be consistent or inconsistent with the decision-maker's preferences.

Two features distinguish a decision from a reflex. It is contingent: a stimulus may favor an action without triggering it, and the action can wait for more information or never occur. And it is free from immediacy: the deliberation unfolds on a timescale of hundreds of milliseconds to seconds, set by the process itself rather than by the stimulus. Both features make decisions a model system for cognition in general.

### 47.1.2. The Random-Dot Motion Task

In the task introduced by Newsome and colleagues ([7.16.18](/7.16.18#sec-18.8)), a monkey views a patch of moving dots in which a fraction $C$, the motion coherence, moves in one of two opposite directions and the rest are replotted at random; it reports the direction with an eye movement to one of two targets. Two versions of the task ask different questions. In the *fixed-duration* version the experimenter controls the viewing time and the monkey answers after a delay; in the *reaction-time* version the monkey answers whenever it is ready, so that its decision time is measured as well as its choice.

Three regularities hold in both humans and monkeys. The fraction correct rises with coherence along a sigmoidal **psychometric function**, from chance at $C = 0$ to nearly perfect above $C \approx 25\%$. The reaction time falls with coherence (the chronometric function): weak motion takes longer to judge, by several hundred milliseconds. And in the fixed-duration task, the coherence needed for a given accuracy falls with viewing time as $1/\sqrt t$, as expected if independent samples of evidence are averaged, but only up to a point, after which longer viewing helps less and less (Kiani, Hanks and Shadlen, 2008). The last observation suggests that the brain does not simply average all the evidence it receives but stops when it has enough.

**Definition 47.1.2 (Speed–Accuracy Trade-Off)** The **speed–accuracy trade-off** is the reciprocal relation between the time taken by a decision and its accuracy: by requiring more evidence before committing, a decision-maker becomes slower and more accurate, and by requiring less, faster and more error-prone.

Instructions to be fast or to be accurate, or payoffs that reward one or the other, move human observers along this trade-off, and reaction times and error rates change together in the way predicted by a change of a single threshold. The model of the next section makes this precise.

## 47.2. The Drift-Diffusion Model

### 47.2.1. Accumulation to a Bound

Suppose that the sensory neurons supply, at each moment, a noisy sample of evidence whose mean favors one alternative: in the motion task, the difference between the rates of MT neurons preferring the two directions. The decision-maker adds up the samples and stops when the sum reaches a criterion.

**Definition 47.2.1 (Drift-Diffusion Model)** In the **drift-diffusion model** (DDM) a decision variable $x(t)$ starts at $x(0) = 0$ and obeys
$$
\mathrm{d}x = A\,\mathrm{d}t + c\,\mathrm{d}W_t, \tag{47.1}
$$
where $W_t$ is a standard **Brownian motion**, $A$ is the drift (the mean momentary evidence, proportional to the stimulus strength, $A = \kappa C$) and $c$ the noise amplitude. The decision is made at the first time $T_{\mathrm{d}}$ at which $x$ reaches $+\theta$ (choice 1) or $-\theta$ (choice 2); the observed reaction time is $T_{\mathrm{d}} + T_{\mathrm{nd}}$, where the non-decision time $T_{\mathrm{nd}}$ covers sensory latency and motor execution (Ratcliff, 1978).

The model is a biased random walk between two absorbing barriers, and its choice and timing statistics are those of a **first-passage time** problem ([Definition 5.6.1](/7.6.5#def-5.6.1)). Both follow in closed form.

**Proposition 47.2.1 (Accuracy and Decision Time of the DDM)** For $A > 0$ (choice 1 correct), the probability of a correct choice and the mean decision time of the DDM are
$$
P_{\mathrm{c}} = \frac{1}{1 + \mathrm{e}^{-2A\theta/c^2}}, \qquad \mathbb{E}[T_{\mathrm{d}}] = \frac{\theta}{A}\tanh\Bigl(\frac{A\theta}{c^2}\Bigr), \tag{47.2}
$$
and the mean decision time is the same for correct and error trials. As $A \to 0$, $P_{\mathrm{c}} \to 1/2$ and $\mathbb{E}[T_{\mathrm{d}}] \to \theta^2/c^2$.

**Proof** Let $u(x)$ be the probability of reaching $+\theta$ before $-\theta$ from $x$, and $T(x)$ the mean exit time. Conditioning on the first step $\mathrm{d}t$, as for the backward equation of [7.6.5](/7.6.5#sec-5.6.1), gives $\frac{c^2}{2}u'' + Au' = 0$ with $u(\theta) = 1$, $u(-\theta) = 0$, and $\frac{c^2}{2}T'' + AT' = -1$ with $T(\pm\theta) = 0$. Write $k = A\theta/c^2$. The first equation gives $u(x) = (1 - \mathrm{e}^{-2A(x + \theta)/c^2})/(1 - \mathrm{e}^{-4k})$, and $u(0) = (1 - \mathrm{e}^{-2k})/(1 - \mathrm{e}^{-4k}) = 1/(1 + \mathrm{e}^{-2k})$. The second has the general solution $T(x) = -x/A + C_1 + C_2\mathrm{e}^{-2Ax/c^2}$; the boundary conditions give $C_2 = -\theta/(A\sinh 2k)$ and $C_1 = \theta/A - C_2\mathrm{e}^{-2k}$, so that $T(0) = \frac{\theta}{A}\bigl[1 - \frac{1 - \mathrm{e}^{-2k}}{\sinh 2k}\bigr] = \frac{\theta}{A}\tanh k$. For the equality of correct and error times, the conditional density of the exit time at $+\theta$ differs from that at $-\theta$ only by the factor $\mathrm{e}^{2A\theta/c^2}$, independent of time (by Girsanov's theorem, or directly from the method of images), so the two conditional distributions coincide. $\square$

![The drift-diffusion model (Definition 47.2.1; $c = 1$, $\theta = 1$, time in seconds; Euler–Maruyama with steps of $1\,\mathrm{ms}$). A: twelve sample paths of the decision variable for drift $A = 1$, ending at the upper bound (blue, correct) or the lower bound (red, error). B: psychometric function, fraction correct against drift (dots: 2000 simulated trials per value; line: Eq. (47.2)). C: chronometric function, mean decision time against drift for correct trials (dots) and errors (crosses), with Eq. (47.2) (line); correct and error trials take the same time on average, and the weakest evidence takes longest. D: distributions of decision times for $A = 1$: both are skewed to the right, with a long tail of slow decisions, and they have the same shape.](./plots/ddm.py)

With three parameters (the gain $\kappa$, the bound $\theta$ and $T_{\mathrm{nd}}$, with $c = 1$ fixing the scale), Eq. (47.2) fits the psychometric and the chronometric functions of monkeys and humans together, with the same parameters for both (Palmer, Huk and Shadlen, 2005). The model's two simplifications show up in finer data. The right-skewed shape of reaction-time distributions is reproduced (figure, D), but errors are often slower than correct responses when accuracy is stressed, and faster when speed is stressed. Both are explained by variability across trials: if the drift varies from trial to trial, errors come preferentially from trials with weak drift, which are slow; if the starting point varies, errors come from trials that started near the wrong bound, which are fast (Ratcliff and McKoon, 2008).

### 47.2.2. Optimality: the Sequential Probability Ratio Test

Why should the brain accumulate to a bound? Statistics gives the answer. Testing between two simple hypotheses with a fixed number of observations, the best test is the **likelihood ratio test** ([Definition 5.3.1](/3.2.5#def-5.3.1)). If observations arrive one at a time and each costs time, one can also choose when to stop.

**Definition 47.2.2 (Sequential Probability Ratio Test)** Given independent observations $e_1, e_2, \dots$ with density $f_1$ under hypothesis $H_1$ and $f_2$ under $H_2$, the **sequential probability ratio test** (SPRT; Wald, 1947) updates the log-likelihood ratio $L_n = \sum_{k=1}^{n}\ln\bigl(f_1(e_k)/f_2(e_k)\bigr)$ after each observation, accepts $H_1$ as soon as $L_n \ge b_1$, accepts $H_2$ as soon as $L_n \le -b_2$, and otherwise takes another observation.

**Theorem 47.2.1 (Optimality of the SPRT)** Among all sequential tests of $H_1$ against $H_2$ whose two error probabilities do not exceed those of a given SPRT, that SPRT minimizes the expected number of observations, both under $H_1$ and under $H_2$ (Wald and Wolfowitz, 1948).

The DDM is the SPRT in continuous time. Under the two hypotheses "drift $+A$" and "drift $-A$", a small increment $\mathrm{d}x$ of Eq. (47.1) is Gaussian with mean $\pm A\,\mathrm{d}t$ and variance $c^2\,\mathrm{d}t$, and its log-likelihood ratio is
$$
\ln\frac{\exp\bigl(-(\mathrm{d}x - A\,\mathrm{d}t)^2/2c^2\,\mathrm{d}t\bigr)}{\exp\bigl(-(\mathrm{d}x + A\,\mathrm{d}t)^2/2c^2\,\mathrm{d}t\bigr)} = \frac{2A}{c^2}\,\mathrm{d}x. \tag{47.3}
$$
The accumulated log-likelihood ratio is therefore $L(t) = 2Ax(t)/c^2$, proportional to the decision variable, and the bounds $\pm\theta$ on $x$ are bounds $\pm b = \pm 2A\theta/c^2$ on $L$. Since a continuous process stops exactly at the bound, the posterior log odds of the chosen hypothesis at the moment of decision are $b$, and the probability of being correct is $1/(1 + \mathrm{e}^{-b})$, which is Eq. (47.2) again. Bounded accumulation of evidence is thus not merely a description of behavior but the solution of a well-posed statistical problem: for any required accuracy it gives the fastest decisions on average.

The neural evidence is striking. Yang and Shadlen (2007) trained monkeys to choose between a red and a green target after seeing four shapes in succession, each shape assigned a fixed weight of evidence, a log-likelihood ratio, about which target was rewarded. The monkeys' choices followed the sum of the four log-likelihood ratios, and neurons in the lateral intraparietal area changed their rate after each shape by an amount proportional to its log-likelihood ratio: the brain adds evidence in units of log odds, as the SPRT does.

### 47.2.3. Setting the Bound

The SPRT fixes the error rates and minimizes time; it does not say which error rate to choose. If correct responses are rewarded and each trial is followed by a fixed interval $T_0$ (non-decision time, inter-trial interval and any penalty), a decision-maker who wants to maximize rewards per unit time maximizes the reward rate
$$
\mathrm{RR}(\theta) = \frac{P_{\mathrm{c}}(\theta)}{\mathbb{E}[T_{\mathrm{d}}](\theta) + T_0}, \tag{47.4}
$$
which has an interior maximum: a low bound wastes trials on errors, a high bound wastes time (Gold and Shadlen, 2002; Bogacz, Brown, Moehlis, Holmes and Cohen, 2006). The optimal bound rises with $T_0$, since a long wait between trials makes each trial precious, and depends on the difficulty. Human participants adjust their bounds in the predicted directions, though most are more cautious than the reward-rate optimum, which is expected if they also value accuracy for its own sake or are uncertain about the parameters. When the difficulty varies unpredictably from trial to trial, the optimal bound is not constant but collapses with elapsed time, because a decision that has taken long is probably a hard one, for which waiting longer gains little (Drugowitsch, Moreno-Bote, Churchland, Shadlen and Pouget, 2012). Neurally, a collapsing bound is equivalent to an *urgency signal*, a rising input added to the accumulators, which is observed in LIP as a component of activity that grows with time independently of the evidence (Churchland, Kiani and Shadlen, 2008).

![The speed–accuracy trade-off in the DDM (Eq. (47.2), $c = 1$). A: fraction correct against mean decision time as the bound $\theta$ is varied from $0.05$ to $2$, for three drifts; dots mark $\theta = 0.5$, $1$ and $1.5$. Each curve is a trade-off: raising the bound buys accuracy with time, at a diminishing rate. B: reward rate (Eq. (47.4)) for $A = 1$ against the bound, for intervals $T_0 = 0.5$, $1$ and $3\,\mathrm{s}$ between decisions; dots mark the optimal bounds, which rise with $T_0$.](./plots/speed-accuracy.py)

### 47.2.4. Race and Competing Accumulators

Two other models make the link to neurons explicit. In a *race model*, two accumulators $y_1, y_2$ each integrate the evidence for one alternative, $\mathrm{d}y_i = I_i\,\mathrm{d}t + c\,\mathrm{d}W_i$, and the first to reach a bound wins. In the *leaky competing accumulator* (Usher and McClelland, 2001) the accumulators also leak and inhibit each other:
$$
\mathrm{d}y_1 = (-ky_1 - wy_2 + I_1)\,\mathrm{d}t + c\,\mathrm{d}W_1, \qquad \mathrm{d}y_2 = (-ky_2 - wy_1 + I_2)\,\mathrm{d}t + c\,\mathrm{d}W_2. \tag{47.5}
$$
The difference $z = y_1 - y_2$ obeys $\mathrm{d}z = \bigl((w - k)z + I_1 - I_2\bigr)\mathrm{d}t + \sqrt2\,c\,\mathrm{d}W$, independently of the sum. If leak and inhibition are balanced, $k = w$, the difference is exactly a DDM with drift $I_1 - I_2$: the competing accumulators implement the optimal test (Bogacz et al., 2006). If leak dominates ($k > w$), $z$ is an **Ornstein–Uhlenbeck process** that forgets early evidence and weights recent evidence more; if inhibition dominates ($k < w$), $z$ is pushed away from zero at an accelerating rate, early evidence is weighted more, and the dynamics resemble the commitment to one of two attractors. The eigenvalue $w - k$ of the difference mode thus decides whether the circuit integrates, forgets or commits, a quantity we meet again in the attractor networks of Section 47.4.

## 47.3. Evidence Accumulation in the Brain

### 47.3.1. LIP Neurons Ramp to a Threshold

Where is the decision variable? Area MT supplies the momentary evidence: its neurons respond to motion in their preferred direction throughout the stimulus, with rates that depend on the current coherence but not on how long the stimulus has lasted ([7.16.26](/7.16.26#sec-26.2.1)). Downstream, neurons in the lateral intraparietal area (LIP) of the posterior parietal cortex behave differently. LIP neurons have response fields, regions of the visual field to which a saccade is planned, and they were first identified by their persistent activity during the delay of memory-guided saccade tasks ([Definition 45.2.1](/7.16.45#def-45.2.1)).

**Definition 47.3.1 (Evidence Accumulation)** **Evidence accumulation** is the integration over time of noisy momentary evidence into a decision variable, which represents the cumulative support for one alternative over another and, in bounded accumulation, terminates the decision when it reaches a criterion level.

Shadlen and Newsome (2001) and Roitman and Shadlen (2002) recorded LIP neurons while monkeys performed the motion task with one target in the response field. About $200\,\mathrm{ms}$ after motion onset, the rate began to rise or fall, at a slope proportional to the coherence and sign of the motion toward or away from the response field; at $0\%$ coherence it drifted up or down depending on the eventual choice. In the reaction-time task, the rate on trials ending with a saccade into the response field reached the same level, about $70\,\mathrm{ms}$ before the saccade, whatever the coherence and reaction time: a threshold. The ramping represents the accumulated evidence, the common level the bound. LIP is not alone: similar build-up activity is found in the frontal eye field, the dorsolateral prefrontal cortex, the superior colliculus and the caudate nucleus, and in rats in the frontal orienting field and posterior parietal cortex (Hanks et al., 2015), which suggests that accumulation is a property of a distributed circuit linked to the planning of the response.

Rodent experiments allow the noise to be dissected. In the Poisson clicks task of Brunton, Botvinick and Brody (2013), rats and humans judged which of two speakers emitted more clicks, presented at random times. Because the experimenter knows every click, the model can be fitted click by click, and it showed that the accumulator itself is nearly noiseless and does not leak; the variability of choices comes from noise in the sensory representation of each click. Accumulation in the brain is therefore close to the perfect integrator of the DDM.

### 47.3.2. Causal Tests and Open Questions

Correlation of LIP activity with the decision variable does not show that LIP computes it. The most direct causal tests stimulate or silence the circuit. Microstimulation of a cluster of MT neurons with a common preferred direction during the reaction-time task made choices toward that direction both more frequent and faster, and choices against it slower, exactly as if the drift $A$ had been increased by a constant (Ditterich, Mazurek and Shadlen, 2003): MT provides the momentary evidence. Microstimulation in LIP had a smaller effect of the same kind, as if a constant had been added to the accumulated evidence (Hanks, Ditterich and Shadlen, 2006). But pharmacological inactivation of LIP, which strongly impaired memory-guided saccades, had almost no effect on choices in the motion task (Katz, Yates, Pillow and Huk, 2016): LIP reflects the decision but is not necessary for it, at least when other areas of the distributed circuit can take over.

A second debate concerns single trials. Averaged over trials, ramping can arise from smooth accumulation or from abrupt steps between a low and a high state that occur at different times on different trials, and models of LIP spike trains initially favored steps (Latimer, Yates, Meister, Huk and Pillow, 2015). With large populations recorded simultaneously, the decision variable can be decoded on single trials, and it shows the continuous, diffusion-like trajectories predicted by bounded accumulation (Steinemann et al., 2024). How the bound is implemented, by a fixed level in LIP, by a threshold in its targets such as the superior colliculus, or by the dynamics of the circuit itself, is the subject of the next section.

## 47.4. Attractor Networks for Decisions

### 47.4.1. The Wang Network

The DDM describes decisions as linear integration followed by an imposed threshold. Wang (2002) proposed that both arise from the dynamics of a cortical circuit like those that sustain working memory. In his spiking network of 2000 integrate-and-fire neurons, two populations of excitatory cells, each 15% of the network, are selective for the two directions; each population excites itself through strong recurrent synapses with slow **NMDA receptor** currents ([7.16.12](/7.16.12#sec-12.3.2)), and both inhibit each other through a common pool of inhibitory interneurons. The motion stimulus drives the two populations in proportion to the evidence for each direction. Their rates first ramp slowly, as the network integrates the difference of its inputs over hundreds of milliseconds; then one population wins, through **positive feedback** and mutual inhibition, and fires at a high rate while the other is suppressed. The winner-take-all state is a choice, and because it is an attractor it persists after the stimulus has ended: the same circuit makes the decision and holds it in working memory.

The network reproduces the psychometric and chronometric functions, the ramping of LIP neurons and their common level before the response, and the effect of microstimulation. Its integration time, which is far longer than the membrane or AMPA time constants, comes from the slow NMDA receptor kinetics, as for persistent activity ([7.16.45](/7.16.45#sec-45.3.2)); with fast recurrent synapses the network decides quickly and inaccurately.

### 47.4.2. The Reduced Wong–Wang Model

Wong and Wang (2006) reduced the network to two variables by a mean-field approximation in which each population is represented by the average gating variable of its NMDA synapses.

**Formula 47.4.1 (Reduced Wong–Wang Model)** The NMDA gating variables $S_1, S_2$ of the two selective populations obey
$$
\frac{\mathrm{d}S_i}{\mathrm{d}t} = -\frac{S_i}{\tau_{\mathrm{S}}} + (1 - S_i)\,\gamma\,H(x_i), \qquad x_i = J_{\mathrm{s}}S_i - J_{\mathrm{c}}S_j + I_0 + I_i + I_{\mathrm{noise}, i}, \quad j \ne i, \tag{47.6}
$$
where $x_i$ is the total synaptic input current to population $i$ and
$$
H(x) = \frac{ax - b}{1 - \exp\bigl(-d(ax - b)\bigr)} \tag{47.7}
$$
is its firing rate, the f–I curve of the integrate-and-fire neurons. $J_{\mathrm{s}}$ is the net self-excitation of a population and $J_{\mathrm{c}}$ the net cross-inhibition (through the inhibitory pool, whose effect is absorbed into these constants), $I_0$ a background input, $I_i = J_{\mathrm{ext}}\mu_0(1 \pm C)$ the stimulus input for coherence $C$, and $I_{\mathrm{noise}, i}$ an Ornstein–Uhlenbeck noise with the time constant of AMPA synapses. Standard values are $\tau_{\mathrm{S}} = 100\,\mathrm{ms}$, $\gamma = 0.641$, $a = 270\,\mathrm{Hz\,nA^{-1}}$, $b = 108\,\mathrm{Hz}$, $d = 0.154\,\mathrm{s}$, $J_{\mathrm{s}} = 0.2609\,\mathrm{nA}$, $J_{\mathrm{c}} = 0.0497\,\mathrm{nA}$, $I_0 = 0.3255\,\mathrm{nA}$, $J_{\mathrm{ext}}\mu_0 = 0.0156\,\mathrm{nA}$, and a decision is read out when one rate exceeds $15\,\mathrm{Hz}$.

The two-dimensional system can be analyzed in the **phase plane**. Without a stimulus, it has three stable fixed points: a symmetric spontaneous state with both populations near $2\,\mathrm{Hz}$ and two asymmetric memory states, one population near $20\,\mathrm{Hz}$ and the other silent, which store a previous choice. When the stimulus is turned on, the spontaneous state disappears, and the symmetric fixed point that remains, at about $11\,\mathrm{Hz}$, is a **saddle**: stable along the direction $S_1 + S_2$ (eigenvalue $-2.6\,\mathrm{s^{-1}}$) and unstable along $S_1 - S_2$ (eigenvalue $+4.4\,\mathrm{s^{-1}}$). From the spontaneous state the trajectory rises along the diagonal toward the saddle and, pushed by the input difference and the noise, is deflected along the unstable direction toward one of two decision states, with one population at $30\,\mathrm{Hz}$. The stable manifold of the saddle separates the basins of the two choices; a biased stimulus moves the saddle and the separatrix so that more initial states, and more noise trajectories, end in the favored attractor.

![The reduced Wong–Wang model (Formula 47.4.1, standard parameters, noise $\sigma = 0.02\,\mathrm{nA}$, Euler–Maruyama with steps of $0.5\,\mathrm{ms}$; stimulus on from $t = 0$). A: firing rates of the two populations in four trials at coherence $6.4\%$ (smoothed over $20\,\mathrm{ms}$): both rise together, then one wins and the other is suppressed, in one of the four trials the population favored by the stimulus loses; the dashed line is the decision threshold of $15\,\mathrm{Hz}$. B: phase plane at zero coherence with the stimulus on: nullclines $\mathrm{d}S_1/\mathrm{d}t = 0$ (blue) and $\mathrm{d}S_2/\mathrm{d}t = 0$ (red), the direction field (gray), the two stable decision states (filled), the saddle (open square) and five noisy trajectories (green) from the spontaneous state, which rise along the diagonal and are deflected toward one or the other decision state before reaching the saddle. C: fraction of choices of population 1 (blue) and mean decision time (red) against coherence, 250 trials per value: the network gives a psychometric function and decides most slowly, in about $420\,\mathrm{ms}$, when the evidence is weakest.](./plots/wong-wang.py)

### 47.4.3. Integration Near the Saddle and the Critical Boundary

How long the network integrates is set by the unstable eigenvalue of the saddle. For an unbiased stimulus the symmetric state $S_1 = S_2 = S^*$ has, by symmetry, the two modes $S_1 + S_2$ and $S_1 - S_2$.

**Proposition 47.4.1 (Modes of the Symmetric State)** At a symmetric fixed point $S^*$ of Eq. (47.6) with equal inputs and no noise, let $x^* = (J_{\mathrm{s}} - J_{\mathrm{c}})S^* + I_0 + I$, and let $\alpha = -1/\tau_{\mathrm{S}} - \gamma H(x^*) + (1 - S^*)\gamma H'(x^*)J_{\mathrm{s}}$ and $\beta = -(1 - S^*)\gamma H'(x^*)J_{\mathrm{c}}$. Then the Jacobian matrix is $\begin{bmatrix}\alpha & \beta\\ \beta & \alpha\end{bmatrix}$, with eigenvector $(1, 1)$ of eigenvalue $\alpha + \beta$ (sum mode) and eigenvector $(1, -1)$ of eigenvalue
$$
\lambda_- = \alpha - \beta = -\frac{1}{\tau_{\mathrm{S}}} - \gamma H(x^*) + (1 - S^*)\,\gamma H'(x^*)\,(J_{\mathrm{s}} + J_{\mathrm{c}}) \tag{47.8}
$$
(difference mode).

**Proof** Differentiate the right side $F_i$ of Eq. (47.6) at the fixed point: $\partial F_i/\partial S_i = -1/\tau_{\mathrm{S}} - \gamma H(x_i) + (1 - S_i)\gamma H'(x_i)J_{\mathrm{s}}$ and $\partial F_i/\partial S_j = -(1 - S_i)\gamma H'(x_i)J_{\mathrm{c}}$, which at $S_1 = S_2 = S^*$ are $\alpha$ and $\beta$. A symmetric $2\times2$ matrix with equal diagonal entries has the stated eigenvectors. $\square$

Near the symmetric state the difference $z = S_1 - S_2$ therefore obeys, to first order, $\dot z = \lambda_-z + (\text{input difference}) + \text{noise}$: the same equation as the difference of the leaky competing accumulators, with $\lambda_-$ in place of $w - k$. At a given operating point, self-excitation and cross-inhibition both increase $\lambda_-$ (Eq. (47.8)); but they also move the symmetric state, and when it is pushed to high rates, where the gain $H'$ is lower relative to the decay terms, $\lambda_-$ falls again. If $\lambda_- < 0$ the symmetric state is stable, and the network does not decide; if $\lambda_-$ is large and positive, the network leaves the saddle within tens of milliseconds, driven mostly by noise, and decides quickly and inaccurately; if $\lambda_-$ is small and positive, the network stays near the saddle for a time of order $1/\lambda_-$, integrates the input difference almost linearly, as a DDM would, and decides slowly and accurately. The boundary $\lambda_- = 0$ in parameter space, at which the decision states appear in a **pitchfork bifurcation** of the symmetric state, is a critical boundary, and networks near it behave as optimal integrators (Roxin and Ledberg, 2008). With the standard parameters $\lambda_- \approx 4.4\,\mathrm{s^{-1}}$, an integration time of about $230\,\mathrm{ms}$.

![Speed and accuracy of the Wong–Wang network near the critical boundary (Formula 47.4.1 with the self-excitation $J_{\mathrm{s}}$ varied, other parameters standard). A: eigenvalues of the symmetric fixed point with the stimulus on (Proposition 47.4.1): the difference mode (blue) is positive, and the symmetric state a saddle, only between about $0.222$ and $0.277\,\mathrm{nA}$: below this range the symmetric low-rate state is stable and the network does not decide, above it the symmetric state with both populations at high rates is stable; the sum mode (dashed) is always stable, and the dotted line marks the standard value. B: fraction correct at coherence $3.2\%$ (blue) and mean decision time (red) from 250 trials per value: close to the lower boundary the network integrates for longer and decides more accurately (91% correct in $1.7\,\mathrm{s}$ at $J_{\mathrm{s}} = 0.225\,\mathrm{nA}$); farther from it, decisions are fast and less accurate (about 68% correct in $0.4\,\mathrm{s}$).](./plots/critical-boundary.py)

The attractor picture explains what the DDM must postulate. The bound is not a separate mechanism but the point of no return beyond which the network is in the basin of a decision state; the commitment is the persistence of that state; and the decision can be reset by a strong nonspecific input that pushes the network back to its spontaneous state, as the saccade or a reward might. It also predicts effects that the linear model does not: evidence presented early in a trial, while the state is near the saddle, has more effect on the choice than evidence presented late, when the network has already committed, a primacy effect seen in monkeys and humans when the stimulus fluctuates (Kiani, Hanks and Shadlen, 2008).

## 47.5. Value-Based Decisions

### 47.5.1. Value Signals in the Brain

Most decisions outside the laboratory are choices between goods, actions or plans that differ in value: an apple or an orange, a sure reward or a gamble. Value is not given by the stimulus; it is assigned by the decision-maker, mostly through learning ([7.16.39](/7.16.39)), and can only be inferred from choices. To measure it in animals, Padoa-Schioppa and Assad (2006) offered monkeys choices between two juices in variable amounts, for example one drop of grape juice against three drops of apple juice; the ratio at which the monkey chose each juice equally often gave the relative value of the juices. Neurons in the orbitofrontal cortex (OFC) encoded three variables: the value of one of the offers (offer value cells), the value of the chosen offer (chosen value cells) and the identity of the chosen juice (chosen juice cells). These signals were independent of the spatial configuration and of the action used to report the choice, and they did not depend on what the other juice on the menu was (Padoa-Schioppa and Assad, 2008), as a common currency for goods should, which also guarantees that choices are transitive.

Values of actions rather than goods are represented in the striatum, where neurons encode the expected reward of a particular movement before the choice is made (Samejima, Ueda, Doya and Kimura, 2005), and are updated by dopaminergic prediction errors ([7.16.40](/7.16.40)). In humans, the BOLD signal of the ventromedial prefrontal cortex tracks the subjective value of many kinds of goods, food, money and social rewards, on a common scale. And LIP neurons, the accumulators of the motion task, also scale with the expected gain of a saccade (Platt and Glimcher, 1999), with a divisive normalization by the values of the other options (Louie, Grattan and Glimcher, 2011) that explains why adding a poor option can change the choice between two good ones.

Value-based choices also show a speed–accuracy relation: choices between items of similar value are slower and less consistent, as if noisy samples of value were accumulated to a bound. In the attentional DDM (Krajbich, Armel and Rangel, 2010) the drift at each moment favors the item that the participant is looking at; the model predicts, and eye-tracking confirmed, that items looked at longer are chosen more often, and that the last fixation tends to be on the chosen item.

### 47.5.2. Risk and Prospect Theory

Choices under risk reveal systematic departures from the maximization of expected value. Most people prefer a sure $100$ dollars to a $50\%$ chance of $200$; yet having received $200$, most prefer a $50\%$ chance of losing all of it to a sure loss of $100$. The two choices are the same in terms of final wealth, but the first is risk-averse and the second risk-seeking.

**Definition 47.5.1 (Prospect Theory)** **Prospect theory** (Kahneman and Tversky, 1979; Tversky and Kahneman, 1992) describes choices between risky options by evaluating outcomes as gains or losses relative to a reference point with a value function that is concave for gains, convex for losses and steeper for losses than for gains,
$$
v(x) = \begin{cases} x^{\alpha}, & x \ge 0,\\ -\lambda(-x)^{\beta}, & x < 0,\end{cases} \tag{47.9}
$$
with typical estimates $\alpha \approx \beta \approx 0.88$ and loss aversion $\lambda \approx 2.25$, and by weighting probabilities with a nonlinear function that overweights small and underweights large probabilities.

With Eq. (47.9) and, for simplicity, unweighted probabilities, the sure gain is worth $100^{0.88} \approx 57.5$ and the gamble $0.5 \times 200^{0.88} \approx 52.9$, so the sure option is preferred; the sure loss is worth $-57.5\lambda$ and the risky loss $-52.9\lambda$, so the gamble is preferred: the curvature of the value function alone produces the reversal. Neural correlates of these components exist: striatal and ventromedial prefrontal responses to gains and losses scale with individual loss aversion (Tom, Fox, Trepel and Poldrack, 2007), and the amygdala is needed for the framing effect, the dependence of choices on whether the same outcomes are described as gains or losses (De Martino, Kumaran, Seymour and Dolan, 2006). The broader questions of foraging, exploration and social choice are taken up in [7.16.37](/7.16.37) and the RL chapters.

## 47.6. Confidence and Metacognition

### 47.6.1. Confidence in the Drift-Diffusion Model

A decision comes with a sense of how likely it is to be right. This confidence guides behavior: whether to check the answer, to wait for a reward or to learn from the outcome.

**Definition 47.6.1 (Decision Confidence)** **Decision confidence** is the decision-maker's estimate of the probability that a choice is correct, given the evidence on which it was based; *metacognition* is the ability to monitor one's own decisions, measured by how well reported confidence discriminates correct from incorrect choices.

In the DDM with a known drift magnitude, every decision terminates at the same log odds $b$, so all decisions would be equally confident. Confidence varies because the difficulty is not known in advance: the same accumulated evidence is weaker support for a choice if it took a long time to accumulate.

**Proposition 47.6.1 (Confidence in the Drift-Diffusion Model)** Let the drift be unknown with prior $A \sim \mathcal{N}(0, \sigma_A^2)$, and let $x(t)$ obey Eq. (47.1). The posterior probability that the drift favors the alternative indicated by the sign of $x$, given $x(t) = x$, is
$$
\mathbb{P}\bigl(\operatorname{sgn}A = \operatorname{sgn}x \mid x(t) = x\bigr) = \Phi\Bigl(\frac{\lvert x\rvert}{c\sqrt{t + c^2/\sigma_A^2}}\Bigr), \tag{47.10}
$$
where $\Phi$ is the standard normal distribution function. At a fixed bound $\lvert x\rvert = \theta$, confidence decreases with decision time.

**Proof** Given $A$, $x(t) \sim \mathcal{N}(At, c^2t)$, so the likelihood is proportional to $\exp\bigl(-(x - At)^2/2c^2t\bigr)$, a Gaussian function of $A$ with precision $t/c^2$ and mean $x/t$. Combining with the prior by **Bayes' theorem**, the posterior of $A$ is Gaussian with precision $1/\sigma_A^2 + t/c^2$ and mean $(x/c^2)/(1/\sigma_A^2 + t/c^2)$. The posterior probability that $A$ has the sign of $x$ is $\Phi(\lvert\text{mean}\rvert/\text{sd}) = \Phi\bigl((\lvert x\rvert/c^2)(1/\sigma_A^2 + t/c^2)^{-1/2}\bigr)$, which simplifies to Eq. (47.10). $\square$

Confidence is thus a function of two quantities that the brain has: the state of the accumulator and the elapsed time. This is what Kiani and Shadlen (2009) found. Monkeys in the motion task were sometimes offered, after the stimulus, a third "sure" target that gave a small but certain reward. They chose it more often when the motion was weak and the viewing time short, and when they declined it, their accuracy was higher than on trials without the option: they used it when uncertain. LIP neurons predicted the choice of the sure target: it was chosen when their rate at the end of the stimulus was intermediate, neither committed to the response field nor away from it. In rats, neurons of the OFC signal confidence before the outcome is known (Kepecs, Uchida, Zariwala and Mainen, 2008), and the time a rat is willing to wait for an uncertain reward, a behavioral report of confidence, depends on the OFC (Lak et al., 2014).

### 47.6.2. Changes of Mind and Metacognition

The accumulator does not stop entirely at the decision. When human participants report a motion decision by moving a handle to one of two targets, they occasionally reverse direction in mid-movement, and these changes of mind are explained by continued accumulation of the evidence that was still in the processing pipeline when the bound was reached, applied against a second bound (Resulaj, Kiani, Wolpert and Shadlen, 2009). Most changes of mind correct errors, as the model predicts, and post-decision evidence also revises confidence.

Metacognitive ability differs between individuals independently of perceptual ability: two observers with the same accuracy can differ in how well their confidence tracks it. Measures based on signal detection theory, such as meta-$d'$ (Maniscalco and Lau, 2012), separate the two, and individual metacognitive sensitivity correlates with the structure and activity of the anterior prefrontal cortex (Fleming, Weil, Nagy, Dolan and Rees, 2010). Confidence links decision-making to awareness: in a decision framework, reporting that one has seen a stimulus is itself a decision about the evidence, with its own bound, and the relation between this view and theories of consciousness is the subject of [7.16.49](/7.16.49).

## Summary

- A decision (Definition 47.1.1) commits to an option on the basis of evidence and value; in perceptual decisions accuracy and reaction time change together with stimulus strength and with a speed–accuracy trade-off (Definition 47.1.2).
- The drift-diffusion model (Definition 47.2.1) accumulates noisy evidence to a bound; first-passage theory gives $P_{\mathrm{c}} = 1/(1 + \mathrm{e}^{-2A\theta/c^2})$ and $\mathbb{E}[T_{\mathrm{d}}] = (\theta/A)\tanh(A\theta/c^2)$ (Proposition 47.2.1), which fit psychometric and chronometric functions together.
- The DDM is the continuous form of the sequential probability ratio test (Definition 47.2.2), which minimizes mean decision time for given error rates (Theorem 47.2.1); the decision variable is proportional to the log-likelihood ratio (Eq. (47.3)), and LIP adds evidence in such units. The bound that maximizes the reward rate (Eq. (47.4)) rises with the time between trials; uncertain difficulty makes it collapse.
- Competing accumulators (Eq. (47.5)) reduce to a DDM when leak equals inhibition; the eigenvalue $w - k$ decides between leaky integration, perfect integration and commitment.
- LIP neurons accumulate evidence (Definition 47.3.1) and reach a common level before the response; MT microstimulation acts as added drift; LIP inactivation spares choices, so accumulation is distributed.
- In the Wang network and its reduced form (Formula 47.4.1), slow NMDA recurrence integrates, and winner-take-all attractors commit and remember. The symmetric state is a saddle whose unstable eigenvalue (Proposition 47.4.1) sets the integration time; near the critical boundary $\lambda_- = 0$ the network is slow, accurate and DDM-like.
- Value-based choice uses OFC signals for the values of goods and striatal action values; prospect theory (Definition 47.5.1) describes risk attitudes by a reference-dependent, loss-averse value function.
- Confidence (Definition 47.6.1) is the posterior probability of being correct; in the DDM it depends on the accumulated evidence and on elapsed time (Proposition 47.6.1), and it is read out from LIP and OFC activity.

| Model | Dynamics of the evidence difference | Bound | Optimal when |
|---|---|---|---|
| DDM | $\mathrm{d}x = A\,\mathrm{d}t + c\,\mathrm{d}W$ | Imposed, $\pm\theta$ | Always (it is the SPRT) |
| Race | Two independent integrators | Imposed, on each | Not in general |
| Leaky competing accumulator | $\mathrm{d}z = ((w - k)z + \Delta I)\,\mathrm{d}t + \cdots$ | Imposed | $k = w$ |
| Wong–Wang attractor network | $\dot z \approx \lambda_-z + \Delta I$ near the saddle | Emergent (basin boundary) | $\lambda_-$ small, near the critical boundary |

## Questions

1. In the DDM with $c = 1$, $A = 1$ and $\theta = 1$, compute the fraction correct and the mean decision time. What are they if the bound is doubled? By what factors do the error rate and the decision time change?

   **Answer** By Eq. (47.2), $P_{\mathrm{c}} = 1/(1 + \mathrm{e}^{-2}) = 0.881$ and $\mathbb{E}[T_{\mathrm{d}}] = \tanh 1 = 0.762\,\mathrm{s}$. With $\theta = 2$, $P_{\mathrm{c}} = 1/(1 + \mathrm{e}^{-4}) = 0.982$ and $\mathbb{E}[T_{\mathrm{d}}] = 2\tanh 2 = 1.93\,\mathrm{s}$. The error rate falls from $0.119$ to $0.018$, by a factor of about 6.6, at the cost of 2.5 times the decision time. For strong evidence ($A\theta \gg c^2$), the error rate falls exponentially with the bound while the time grows only linearly, which is why moderate bounds are efficient.

2. A decision-maker must discriminate drift $+0.5$ from $-0.5$ (with $c = 1$) with an error rate of $5\%$. Compare the mean time needed by the SPRT with the time needed by a test that observes for a fixed duration and then decides by the sign of $x$.

   **Answer** For the SPRT, $1/(1 + \mathrm{e}^{-b}) = 0.95$ gives $b = \ln 19 = 2.94$, hence $\theta = bc^2/(2A) = 2.94$ and $\mathbb{E}[T_{\mathrm{d}}] = (\theta/A)\tanh(A\theta) = 5.89\tanh 1.47 = 5.3\,\mathrm{s}$. For the fixed-duration test, $x(t) \sim \mathcal{N}(0.5t, t)$ and the error rate is $\Phi(-0.5\sqrt t) = 0.05$, so $0.5\sqrt t = 1.645$ and $t = 10.8\,\mathrm{s}$. The sequential test needs about half the time on average, because it stops early on trials in which the evidence happens to be clear; this saving is the content of Theorem 47.2.1.

3. Derive the equation for the difference $z = y_1 - y_2$ of the leaky competing accumulators (47.5). What does the circuit compute when $k > w$, $k = w$ and $k < w$, and how should a decision-maker set $k$ and $w$ if early and late evidence are equally informative?

   **Answer** Subtracting the two equations gives $\mathrm{d}z = (-kz + wz + I_1 - I_2)\,\mathrm{d}t + c(\mathrm{d}W_1 - \mathrm{d}W_2)$, and $W_1 - W_2 = \sqrt2\,W$ for a standard Brownian motion $W$, so $\mathrm{d}z = ((w - k)z + I_1 - I_2)\,\mathrm{d}t + \sqrt2\,c\,\mathrm{d}W$. For $k > w$ the evidence is integrated with a leak of time constant $1/(k - w)$: early evidence is forgotten (recency). For $k = w$ the integration is perfect, a DDM, which weights all evidence equally and is optimal. For $k < w$ the difference grows exponentially once it departs from zero: early evidence decides the outcome (primacy), and the circuit commits like an attractor network. If all evidence is equally informative, the decision-maker should balance leak and inhibition, $k = w$, which is what the near-perfect integration of rats in the clicks task suggests their circuits achieve.

4. In the Wong–Wang model with the standard parameters, the unstable eigenvalue of the saddle is $\lambda_- \approx 4.4\,\mathrm{s^{-1}}$. Estimate how long it takes a difference $S_1 - S_2 = 0.01$, created by noise near the saddle, to grow to $0.3$, and explain why reducing the self-excitation $J_{\mathrm{s}}$ improves accuracy at low coherence.

   **Answer** In the linear approximation $z(t) = z_0\mathrm{e}^{\lambda_-t}$, so $t = \ln(0.3/0.01)/4.4 = 3.4/4.4 \approx 0.77\,\mathrm{s}$; nonlinearity shortens the final approach, and the observed decision times at low coherence are several hundred milliseconds. During this time the input difference is integrated with an effective time constant $1/\lambda_-$; reducing $J_{\mathrm{s}}$ lowers $\lambda_-$ (Eq. (47.8)), lengthening the time spent near the saddle and therefore the time over which the small input difference accumulates relative to the noise, which improves accuracy at the cost of speed. Below the critical value $\lambda_- < 0$, the symmetric state becomes stable and the network no longer decides.

5. Using Proposition 47.6.1 with $c = 1$ and $\sigma_A = 1$, compute the confidence of decisions that reach the bound $\theta = 1$ after $0.5\,\mathrm{s}$ and after $2\,\mathrm{s}$. Why would a model with a known drift predict no difference?

   **Answer** Eq. (47.10) gives $\Phi(1/\sqrt{1.5}) = \Phi(0.82) = 0.79$ at $0.5\,\mathrm{s}$ and $\Phi(1/\sqrt3) = \Phi(0.58) = 0.72$ at $2\,\mathrm{s}$: slow decisions are less confident, as observed. With a known drift magnitude, the log odds at the bound are always $2\lvert A\rvert\theta/c^2$, whatever the time (Eq. (47.3)), so every decision has the same confidence; the decrease with time arises only because elapsed time is evidence that the trial is difficult. The same reasoning motivates collapsing bounds.

6. (Open question) LIP activity correlates with the decision variable, yet inactivating LIP spares choices in the motion task. Propose experiments that would identify which parts of the circuit are necessary for evidence accumulation.

   **Answer** Possible approaches: (a) inactivate several candidate areas (LIP, frontal eye field, superior colliculus, caudate) alone and in combination, with reversible chemogenetic or optogenetic methods, and test whether accumulation (measured by psychophysical reverse correlation of fluctuating stimuli, which reveals the weighting of evidence over time) fails only when several are silenced, as redundancy would predict; (b) perturb briefly at different times during the stimulus: a necessary accumulator should lose the evidence presented before the perturbation, so the effect on choice should depend on when it occurs, whereas a readout area should matter only near the response; (c) record populations simultaneously in several areas and decode the decision variable on single trials, then test whether an area's state predicts the choice before the others; (d) use tasks in which the response modality is not a saccade (for example a reach or a lever), since LIP is tied to eye movements, and test whether accumulation moves to the corresponding motor-planning areas.
