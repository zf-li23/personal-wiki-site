---
title: "Reinforcement Learning I: Prediction Errors, Temporal Differences and Dopamine"
description: "From the Rescorla–Wagner rule and blocking to temporal-difference learning and the dopamine reward prediction error; Markov decision processes, returns, value functions, the Bellman equations, optimal policies, value and policy iteration; model-free learning by Monte Carlo, TD(0), SARSA and Q-learning with ε-greedy exploration; function approximation, deep Q-networks and experience replay; distributional reinforcement learning, expectiles and the diversity of dopamine neurons."
---

**Reinforcement learning** is learning what to do from the consequences of actions: an agent in an environment observes states, takes actions and receives rewards, and must find a way of acting that maximizes the reward accumulated over time. It is the computational theory of conditioning ([7.16.38](/7.16.38#sec-38.2)) and, since the discovery that dopamine neurons signal **reward prediction errors** ([7.16.37](/7.16.37#sec-37.4)), one of the most successful bridges between an algorithm and its neural implementation. The general idea and its use in game playing appear in [4.5.3](/4.5.3#sec-3.6); since no page of this site develops the theory, this chapter defines its core objects completely: the Markov decision process, value functions and the Bellman equations, dynamic programming, and the model-free algorithms TD learning, SARSA and Q-learning. We start, as the history did, with the psychology of Pavlovian learning, follow the temporal-difference idea to the dopamine data, and then build the formal theory. Learning policies directly, model-based planning and meta-learning are the subject of [7.16.41](/7.16.41); the basal ganglia circuits that use these signals of [7.16.40](/7.16.40).

## 39.1. From Psychology to Algorithm: the Rescorla–Wagner Rule

### 39.1.1. The Rule

**Pavlovian conditioning** had been thought to depend on the contiguity of CS and US. Experiments in the 1960s showed that contiguity is not enough: what matters is whether the CS provides information about the US. In blocking (Kamin, 1969), animals first learn that a tone predicts a shock; when a light is then added to the tone and the compound is paired with the same shock, the animals learn almost nothing about the light, although it is paired with the shock as often as the tone was. The shock is already predicted, so the light adds nothing.

**Definition 39.1.1 (Rescorla–Wagner Rule)** In the **Rescorla–Wagner rule** (1972), each conditioned stimulus $i$ has an associative strength $V_i$, and on each trial the strength of every stimulus present changes by
$$
\Delta V_i = \alpha_i \beta \Bigl(\lambda - \sum_{j \in \text{present}} V_j\Bigr),
$$
where $\lambda$ is the maximal strength the US supports ($\lambda = 0$ on trials without US), $\alpha_i$ the salience of stimulus $i$ and $\beta$ a learning rate set by the US.

The rule has three key features: the change is driven by a prediction error, the difference between the outcome $\lambda$ and the summed prediction; the prediction is shared by all stimuli present, so they compete for associative strength; and the rule is identical to the delta rule (least-mean-squares rule) of adaptive filtering and to stochastic gradient descent on the squared error $\frac12(\lambda - \sum_j V_j)^2$ with linear features, which links conditioning to supervised learning (**stochastic gradient descent**, [3.5.5](/3.5.5)).

![The Rescorla–Wagner rule (Definition 39.1.1, $\alpha\beta = 0.2$). A: acquisition of associative strength over 30 CS–US pairings and extinction over 30 trials with the CS alone; both approach their asymptote exponentially. B: blocking. After pretraining A+, the added stimulus X gains almost no strength when the compound AX is reinforced (red), whereas after pretraining with an unrelated stimulus B it gains half of the available strength (blue).](./plots/rescorla-wagner.py)

### 39.1.2. What It Explains and What It Does Not

The rule accounts for blocking, overshadowing (a more salient stimulus gains more of the shared strength), conditioned inhibition (a stimulus that signals the absence of an otherwise expected US acquires negative strength), the effect of US magnitude on the asymptote, and the partial reinforcement of trials with $\lambda$ sometimes 0 and sometimes 1, where $V$ fluctuates around the probability of reinforcement. It fails for spontaneous recovery after extinction ([7.16.37](/7.16.37#sec-37.2.3)), latent inhibition (preexposure to a CS slows later learning) and, most importantly, for everything that depends on time within a trial: the rule treats a trial as a single event and so cannot explain why a CS must precede the US, why longer CS–US intervals give weaker learning, or second-order conditioning, in which a CS paired with a previously conditioned CS (and never with the US) acquires value. All of these require a theory of prediction in time.

## 39.2. Temporal-Difference Learning

### 39.2.1. Predicting the Future Sum of Rewards

Sutton and Barto (1990) reformulated conditioning as the problem of predicting, at each moment $t$, the discounted sum of future rewards
$$
G_t = R_{t+1} + \gamma R_{t+2} + \gamma^2 R_{t+3} + \cdots = \sum_{k=0}^{\infty}\gamma^k R_{t+k+1}, \tag{39.1}
$$
where $0 \le \gamma \le 1$ is a discount factor. The quantity satisfies a recursion, $G_t = R_{t+1} + \gamma G_{t+1}$: the prediction at time $t$ should equal the next reward plus the discounted prediction at time $t + 1$. Its violation is the learning signal.

**Definition 39.2.1 (Temporal-Difference Error)** Let $\hat v(s)$ be an estimate of the expected discounted future reward from state $s$. The **temporal-difference error** (TD error) on the transition from $S_t$ to $S_{t+1}$ with reward $R_{t+1}$ is
$$
\delta_t = R_{t+1} + \gamma\,\hat v(S_{t+1}) - \hat v(S_t),
$$
and **temporal-difference learning** updates the estimate of the state left by $\hat v(S_t) \leftarrow \hat v(S_t) + \alpha\,\delta_t$, with learning rate $\alpha$ (the TD(0) rule).

TD learning bootstraps: it improves a prediction using another prediction, without waiting for the final outcome. In conditioning, the "state" is the stimulus history within a trial. A common representation, the complete serial compound or tapped delay line, assigns one feature to each time step since the CS onset, so that the value at time $t$ after the CS is a learned weight $w_k$ for $k = t - t_{\mathrm{CS}}$.

### 39.2.2. TD Learning in Conditioning

In the simulation below, a cue is followed by reward 2 s later in every trial. On the first trial the reward is unpredicted, and $\delta$ is positive at the time of the reward. The update raises the value of the time step just before the reward, so on the next trial a smaller positive error appears one step earlier, at the transition into that state; over trials the error propagates backward until it reaches the cue. Because the time of cue onset is itself unpredictable (the pre-cue state has value 0), the error at the cue remains positive, $\delta = \gamma\,\hat v(\text{cue})$, while the error at the reward vanishes. If the reward is then omitted, the value of the state before the reward is not followed by reward, and $\delta = 0 - \hat v < 0$ at the expected time of reward. These are the three properties of **dopamine** responses ([7.16.37](/7.16.37#sec-37.4)).

![Temporal-difference learning of a cue–reward association (TD(0) with a tapped delay line, $\gamma = 0.98$, $\alpha = 0.2$, time step $0.1\,\mathrm{s}$; cue at 0, reward $R = 1$ at $2\,\mathrm{s}$). A: the TD error on each of 200 training trials (red positive, blue negative); the error moves step by step from the reward to the cue. B: single trials; on the first trial the error occurs at reward (gray), after training at the cue ($\delta = \gamma^{20} \approx 0.67$, blue), and when the reward is omitted after training a negative error appears at the expected time of reward (red, dashed).](./plots/td-dopamine.py)

TD learning also explains the phenomena that defeated the Rescorla–Wagner rule. Second-order conditioning arises because a cue that predicts a valued cue produces a positive TD error at its own onset and acquires value without any reward; the decline of learning with longer CS–US intervals arises because discounting and the representation of time spread the prediction over more states; and the requirement that the CS precede the US arises because only states before the reward are updated. Two predictions are specific to TD. First, the backward propagation of the error during learning, one step per trial in the tapped-delay-line model, should be visible in dopamine responses during training; recordings of dopamine axons in mice trained on a cue–reward task found such a gradual shift (Amo and colleagues, 2022), although its form depends on the representation of time. Second, if the reward is delivered earlier than expected, there should be a positive error at the new time and a negative error at the usual time, as found by Hollerman and Schultz (1998).

## 39.3. Dopamine and the TD Error

**Remark 39.3.1 (The Dopamine TD Hypothesis)** The phasic firing of midbrain dopamine neurons, relative to their baseline, approximates the TD error $\delta_t$ of an estimate $\hat v$ of future reward computed elsewhere in the brain; dopamine release in the striatum and cortex acts as the third factor that gates plasticity of the synapses whose activity encodes the current state, implementing $w \leftarrow w + \alpha\,\delta_t\,e$ with an eligibility trace $e$ (Schultz, Dayan and Montague, 1997).

The evidence is the set of experiments described in [7.16.37](/7.16.37#sec-37.4): the transfer of the response from reward to cue, the pause at omission, the scaling with probability and magnitude, the absence of responses to blocked stimuli, and the causal effects of optogenetic bursts and pauses in place of prediction errors. The mechanistic link is the **three-factor learning rule** with an **eligibility trace** ([7.16.14](/7.16.14#sec-14.9)): corticostriatal synapses active in a state leave a trace, and **dopamine** arriving within about a second converts it into potentiation (positive $\delta$) or depression (negative $\delta$) through $\mathrm{D_1}$ and $\mathrm{D_2}$ receptors ([7.16.40](/7.16.40)). The hypothesis is a working model rather than an established fact: dopamine neurons also signal novelty, salience and movement, some ramp up as a goal approaches (which can be read as a TD error under state uncertainty or as a value signal), and their responses to a fully predicted reward are reduced but often not abolished.

## 39.4. Markov Decision Processes

### 39.4.1. Definitions

Conditioning is prediction without control. To choose actions, the agent needs a model of how its actions affect states and rewards.

**Definition 39.4.1 (Markov Decision Process)** A **Markov decision process** (MDP) consists of a set of states $\mathcal{S}$, a set of actions $\mathcal{A}$, and a transition and reward distribution $p(s', r \mid s, a) = \mathbb{P}(S_{t+1} = s', R_{t+1} = r \mid S_t = s, A_t = a)$, which satisfies the Markov property: the distribution of the next state and reward depends only on the current state and action, not on earlier history. A **policy** $\pi(a \mid s)$ is the probability of choosing action $a$ in state $s$.

The interaction produces a trajectory $S_0, A_0, R_1, S_1, A_1, R_2, \dots$. Tasks that end in a terminal state are episodic; others are continuing. The *return* $G_t$ is the discounted sum of future rewards, Eq. (39.1); a discount factor $\gamma < 1$ keeps it finite in continuing tasks and expresses a preference for earlier rewards (an exponential discount, whereas humans and animals often discount hyperbolically).

**Definition 39.4.2 (Value Functions)** The **value function** of a policy $\pi$ is the expected return from each state, $v_\pi(s) = \mathbb{E}_\pi[G_t \mid S_t = s]$, and the **action-value function** is the expected return after taking action $a$ in state $s$ and following $\pi$ thereafter, $q_\pi(s, a) = \mathbb{E}_\pi[G_t \mid S_t = s, A_t = a]$; they are related by $v_\pi(s) = \sum_a \pi(a \mid s)\,q_\pi(s, a)$.

We write value functions in lower case, following Sutton and Barto, to avoid confusion with the membrane potential $V$; learned estimates are written $\hat v$ and $\hat q$.

### 39.4.2. The Bellman Equations

**Theorem 39.4.1 (Bellman Equation)** For any policy $\pi$, the value function satisfies
$$
v_\pi(s) = \sum_a \pi(a \mid s) \sum_{s', r} p(s', r \mid s, a)\,\bigl[r + \gamma\,v_\pi(s')\bigr] \quad \text{for all } s \in \mathcal{S}, \tag{39.2}
$$
and for finite $\mathcal{S}$ and $\gamma < 1$, $v_\pi$ is its unique solution.

**Proof** By $G_t = R_{t+1} + \gamma G_{t+1}$ and the Markov property, $v_\pi(s) = \mathbb{E}_\pi[R_{t+1} + \gamma G_{t+1} \mid S_t = s] = \sum_a \pi(a \mid s)\sum_{s', r}p(s', r \mid s, a)\,(r + \gamma\,\mathbb{E}_\pi[G_{t+1} \mid S_{t+1} = s'])$, and the inner expectation is $v_\pi(s')$. In vector form Eq. (39.2) reads $\boldsymbol{v} = \boldsymbol{r}_\pi + \gamma P_\pi \boldsymbol{v}$, where $P_\pi$ is the state transition matrix under $\pi$ (a stochastic matrix) and $\boldsymbol{r}_\pi$ the expected one-step rewards. The map $T\boldsymbol{v} = \boldsymbol{r}_\pi + \gamma P_\pi\boldsymbol{v}$ is a contraction in the maximum norm, $\|T\boldsymbol{u} - T\boldsymbol{v}\|_\infty \le \gamma\|\boldsymbol{u} - \boldsymbol{v}\|_\infty$, because each row of $P_\pi$ is a probability distribution; by the Banach fixed-point theorem it has a unique fixed point, equivalently $\boldsymbol{v} = (I - \gamma P_\pi)^{-1}\boldsymbol{r}_\pi$. $\square$

A policy $\pi_*$ is optimal if $v_{\pi_*}(s) \ge v_\pi(s)$ for all $s$ and all $\pi$. Optimal policies exist for finite MDPs, and all share the optimal value functions $v_*(s) = \max_\pi v_\pi(s)$ and $q_*(s, a) = \max_\pi q_\pi(s, a)$.

**Theorem 39.4.2 (Bellman Optimality Equation)** The optimal value functions satisfy
$$
v_*(s) = \max_a \sum_{s', r} p(s', r \mid s, a)\,\bigl[r + \gamma\,v_*(s')\bigr], \qquad q_*(s, a) = \sum_{s', r} p(s', r \mid s, a)\,\Bigl[r + \gamma \max_{a'} q_*(s', a')\Bigr], \tag{39.3}
$$
and any policy that is greedy with respect to $q_*$, choosing in each state an action that maximizes $q_*(s, a)$, is optimal.

The optimality equation replaces the average over the policy by a maximum. It is again a contraction (the maximum of contractions with the same modulus), so it has a unique solution, but it is nonlinear. Its importance is that it turns a search over policies into a local consistency condition: knowing $q_*$, the agent acts optimally by a one-step choice, without looking ahead.

**Theorem 39.4.3 (Policy Improvement Theorem)** If two policies satisfy $q_\pi(s, \pi'(s)) \ge v_\pi(s)$ for all states $s$, with $\pi'$ deterministic, then $v_{\pi'}(s) \ge v_\pi(s)$ for all $s$. In particular, the policy that is greedy with respect to $q_\pi$ is at least as good as $\pi$.

**Proof** Expanding repeatedly, $v_\pi(s) \le q_\pi(s, \pi'(s)) = \mathbb{E}[R_{t+1} + \gamma v_\pi(S_{t+1}) \mid S_t = s, A_t = \pi'(s)] \le \mathbb{E}_{\pi'}[R_{t+1} + \gamma\,q_\pi(S_{t+1}, \pi'(S_{t+1})) \mid S_t = s] \le \cdots \le \mathbb{E}_{\pi'}[R_{t+1} + \gamma R_{t+2} + \gamma^2 R_{t+3} + \cdots \mid S_t = s] = v_{\pi'}(s)$. $\square$

### 39.4.3. Dynamic Programming

When the model $p(s', r \mid s, a)$ is known, the Bellman equations can be solved by **dynamic programming**, iterating them as update rules.

**Algorithm 39.4.1 (Policy Iteration)** Start from any policy $\pi_0$. Repeat: (1) policy evaluation, solve Eq. (39.2) for $v_{\pi_k}$ (exactly, or by iterating $\hat v \leftarrow \boldsymbol{r}_{\pi_k} + \gamma P_{\pi_k}\hat v$ to convergence); (2) policy improvement, set $\pi_{k+1}(s) = \arg\max_a \sum_{s', r}p(s', r \mid s, a)[r + \gamma v_{\pi_k}(s')]$; stop when the policy no longer changes.

**Algorithm 39.4.2 (Value Iteration)** Start from any $\hat v_0$ and repeat, for all states, $\hat v_{k+1}(s) = \max_a \sum_{s', r}p(s', r \mid s, a)[r + \gamma\,\hat v_k(s')]$ until the change is small; then act greedily with respect to the final estimate.

By Theorem 39.4.3, each improvement step of policy iteration gives a policy at least as good as the last, and since a finite MDP has finitely many deterministic policies, policy iteration terminates at an optimal policy, typically in few iterations. Value iteration is the iteration of the contraction in Eq. (39.3) and converges geometrically, with error decreasing as $\gamma^k$. In a gridworld with a single rewarded goal, value iteration spreads value outward from the goal by one step per sweep, as the TD error spread backward in time in Section 39.2.2: dynamic programming is the model-based counterpart of TD learning.

![Dynamic programming and learning in a $6 \times 6$ gridworld (walls in gray, goal G with reward 1, $\gamma = 0.9$, deterministic moves). A–C: state values after 1, 4 and 20 sweeps of value iteration (Algorithm 39.4.2); value spreads from the goal one step per sweep, and after convergence the greedy policy (arrows) leads around the wall by a shortest path, with $v_*(s) = \gamma^{d(s) - 1}$ for a state at distance $d(s)$ from the goal. D: without a model, Q-learning (blue) and SARSA (red) with $\alpha = 0.5$ and ε-greedy exploration ($\varepsilon = 0.1$) learn from experience; the number of steps to reach the goal from the bottom-left corner falls from hundreds to near the shortest path within about 20 episodes (mean of 50 runs; with $\varepsilon = 0.1$ exploration keeps it slightly above 10).](./plots/gridworld.py)

## 39.5. Model-Free Learning

### 39.5.1. Monte Carlo and TD Prediction

Animals rarely know the transition probabilities of their world. Model-free methods learn values directly from experienced transitions. The **Monte Carlo method** updates the estimate of each visited state toward the return actually obtained, $\hat v(S_t) \leftarrow \hat v(S_t) + \alpha[G_t - \hat v(S_t)]$; it needs complete episodes and has high variance, because $G_t$ sums many random rewards, but it is unbiased. TD(0) (Definition 39.2.1) replaces $G_t$ by the one-step target $R_{t+1} + \gamma\,\hat v(S_{t+1})$; it learns online and has lower variance, but its target is biased by the current estimate. The two are the extremes of a family: TD($\lambda$) uses an exponentially weighted mixture of $n$-step returns, implemented online with an **eligibility trace** $e(s)$ for each state that is incremented on visits and decays by $\gamma\lambda$ per step, so that each TD error updates all recently visited states in proportion to their trace (Sutton, 1988). Eligibility traces are what three-factor synaptic rules provide in the brain ([7.16.14](/7.16.14#sec-14.9)).

| Method | Target | Needs model | Bias | Variance | Online |
|---|---|---|---|---|---|
| Dynamic programming | $\sum p(s', r \mid s, a)[r + \gamma\,\hat v(s')]$ | Yes | Bootstrap | None | — |
| Monte Carlo | $G_t$ | No | None | High | No |
| TD(0) | $R_{t+1} + \gamma\,\hat v(S_{t+1})$ | No | Bootstrap | Low | Yes |
| TD($\lambda$) | Mixture of $n$-step returns | No | Intermediate | Intermediate | Yes (traces) |

### 39.5.2. Control: SARSA and Q-Learning

To choose actions without a model, the agent must learn action values, since state values give a policy only through a one-step look-ahead that requires the model.

**Algorithm 39.5.1 (SARSA)** In each step, from state $S_t$ take action $A_t$ chosen from the current estimate $\hat q$ (for example ε-greedily), observe $R_{t+1}$ and $S_{t+1}$, choose $A_{t+1}$ in the same way, and update
$$
\hat q(S_t, A_t) \leftarrow \hat q(S_t, A_t) + \alpha\bigl[R_{t+1} + \gamma\,\hat q(S_{t+1}, A_{t+1}) - \hat q(S_t, A_t)\bigr].
$$

**Algorithm 39.5.2 (Q-Learning)** In each step, from state $S_t$ take an action $A_t$ chosen by any policy that keeps exploring (for example ε-greedy with respect to $\hat q$), observe $R_{t+1}$ and $S_{t+1}$, and update
$$
\hat q(S_t, A_t) \leftarrow \hat q(S_t, A_t) + \alpha\Bigl[R_{t+1} + \gamma \max_{a'}\hat q(S_{t+1}, a') - \hat q(S_t, A_t)\Bigr]
$$
(Watkins, 1989).

SARSA (named after the quintuple $S_t, A_t, R_{t+1}, S_{t+1}, A_{t+1}$) is on-policy: it learns the value of the policy it follows, including its exploratory actions. Q-learning is off-policy: its target uses the best next action whatever action is actually taken, so it learns $q_*$ by sampling Eq. (39.3). For a finite MDP, Q-learning converges to $q_*$ with probability 1 if every state–action pair is visited infinitely often and the learning rates satisfy $\sum_t \alpha_t = \infty$, $\sum_t \alpha_t^2 < \infty$ (Watkins and Dayan, 1992), conditions of stochastic approximation. The difference matters when exploration is costly: next to a cliff, SARSA learns a safer path that accounts for its own occasional random steps, Q-learning the optimal path that it then occasionally falls from.

### 39.5.3. Exploration

An agent that always acts greedily on its current estimates may never discover better actions. Balancing the use of current knowledge against the gathering of new information is the *exploration–exploitation trade-off*, studied in its simplest form in the **multi-armed bandit** ([4.5.3](/4.5.3#sec-3.5.1)).

**Definition 39.5.1 (ε-Greedy and Softmax Policies)** An **ε-greedy policy** chooses an action with maximal estimated value with probability $1 - \varepsilon$ and a uniformly random action with probability $\varepsilon$. A **softmax policy** chooses action $a$ with probability $\pi(a \mid s) = \mathrm{e}^{\beta \hat q(s, a)}/\sum_{b}\mathrm{e}^{\beta \hat q(s, b)}$, where the inverse temperature $\beta$ sets the degree of exploitation.

The softmax rule (the **softmax function** of [4.5.4](/4.5.4)) explores in proportion to value: nearly equal options are chosen nearly equally, clearly worse ones rarely. It fits human and animal choices in bandit tasks well, and its parameters $\alpha$ and $\beta$ are the standard quantities estimated in computational psychiatry. More directed strategies add an exploration bonus for uncertain options (upper confidence bounds) or sample actions in proportion to their posterior probability of being best (Thompson sampling); humans use both random and directed exploration, and **neuromodulators**, **norepinephrine** in particular, have been proposed to set the balance.

## 39.6. Function Approximation and Deep Q-Networks

Tables of values are useless when states are many: the game of Go has about $10^{170}$ legal positions, and the sensory states of an animal are continuous and never exactly repeated. Values must then be represented by a parameterized function $\hat q(s, a; \boldsymbol{w})$ that generalizes across similar states. With linear features $\boldsymbol{x}(s, a)$, $\hat q = \boldsymbol{w}^{\mathsf T}\boldsymbol{x}$ and the TD update becomes $\boldsymbol{w} \leftarrow \boldsymbol{w} + \alpha\,\delta_t\,\boldsymbol{x}(S_t, A_t)$, a three-factor rule in which $\boldsymbol{x}$ is presynaptic activity, the action selected is the postsynaptic factor and $\delta_t$ the neuromodulatory third factor. With nonlinear networks, TD learning is no longer guaranteed to converge: the target moves as the weights change ("shooting at a moving target"), successive samples are strongly correlated, and the combination of function approximation, bootstrapping and off-policy learning can diverge.

**Definition 39.6.1 (Deep Q-Network and Experience Replay)** A **deep Q-network** (DQN) is a deep neural network that maps a state (for example the pixels of a video game screen) to estimated action values $\hat q(s, \cdot\,; \boldsymbol{w})$ and is trained by Q-learning with two stabilizing devices: **experience replay**, in which transitions $(S_t, A_t, R_{t+1}, S_{t+1})$ are stored in a memory buffer and the network is trained on random minibatches drawn from it, and a target network, a periodically updated copy $\boldsymbol{w}^-$ of the weights used to compute the targets $R_{t+1} + \gamma\max_{a'}\hat q(S_{t+1}, a'; \boldsymbol{w}^-)$.

With these devices a single architecture learned 49 Atari games from pixels and score, reaching human-level performance in many of them (Mnih and colleagues, 2015). Replay decorrelates the training samples and reuses rare experiences; the target network makes the regression problem approximately stationary. The analogy with the brain was explicit in its design: during rest and sleep, hippocampal **place cells** replay sequences of past experience in compressed form (Wilson and McNaughton, 1994; Lee and Wilson, 2002), and **replay** has been proposed to train cortical and striatal value representations offline, prioritizing surprising experiences as prioritized replay does in machine learning. Replay and its role in planning return in [7.16.46](/7.16.46) and [7.16.41](/7.16.41). Gradient-based training of the network itself (**backpropagation**, [4.5.4](/4.5.4)) has no established biological counterpart, a problem discussed in [7.16.50](/7.16.50).

## 39.7. Distributional Reinforcement Learning

The value function is an expectation, but the return is a random variable: the same expected value can come from a certain moderate reward or from a gamble between nothing and a large reward. Learning the whole distribution of returns improves deep reinforcement learning (Bellemare, Dabney and Munos, 2017), and a simple mechanism for it turned out to be present in dopamine neurons.

**Definition 39.7.1 (Distributional TD Learning)** In **distributional TD learning** with asymmetric learning rates, a population of value predictors $\hat v_i$ is updated with the TD errors $\delta_{i,t} = R_{t+1} + \gamma\,\hat v_{j}(S_{t+1}) - \hat v_i(S_t)$ (with $\hat v_j$ a sample from the population), each scaling positive errors by $\alpha_i^+$ and negative errors by $\alpha_i^-$; the asymmetry $\tau_i = \alpha_i^+/(\alpha_i^+ + \alpha_i^-)$ makes predictor $i$ optimistic ($\tau_i > 1/2$) or pessimistic ($\tau_i < 1/2$).

**Proposition 39.7.1** For a fixed reward distribution in a single state, the predictor with asymmetry $\tau$ converges in expectation to the $\tau$-expectile $e_\tau$ of the distribution, the unique solution of
$$
\tau\,\mathbb{E}\bigl[(R - e_\tau)_+\bigr] = (1 - \tau)\,\mathbb{E}\bigl[(e_\tau - R)_+\bigr];
$$
$e_{1/2}$ is the mean, and $e_\tau$ increases from the minimum to the maximum of the distribution as $\tau$ goes from 0 to 1.

**Proof** The expected update is $\mathbb{E}[\Delta\hat v] = \alpha^+\mathbb{E}[(R - \hat v)_+] - \alpha^-\mathbb{E}[(\hat v - R)_+]$, which is zero exactly at the stated equation after dividing by $\alpha^+ + \alpha^-$. The left side decreases and the right side increases with $\hat v$, so the zero is unique and the fixed point is stable; for $\tau = 1/2$ the equation reads $\mathbb{E}[R - e] = 0$. $\square$

![Distributional TD learning (Definition 39.7.1) for a bimodal reward distribution (probability 0.6 of a small reward near 0.1, otherwise a reward near 0.8). A: the distribution with the values learned by 15 predictors whose asymmetries $\tau_i$ range from 0.05 (blue, pessimistic) to 0.95 (red, optimistic); the predictors spread across the distribution, whereas the mean (dashed) lies where hardly any reward occurs. B: the learned values agree with the exact expectiles of the distribution (Proposition 39.7.1).](./plots/distributional.py)

Dabney and colleagues (2020) tested this in VTA dopamine neurons of mice receiving rewards of variable size. Each neuron has a reversal point, the reward size at which its response changes from excitation to inhibition; in a classical TD model all neurons would share the same reversal point, the mean. Instead the reversal points were spread out, and they were correlated with the asymmetry of each neuron's responses to positive and negative errors as Proposition 39.7.1 predicts: neurons that responded more strongly to positive than to negative errors had higher reversal points. Decoding the population as a set of expectiles recovered the shape of the reward distribution, including its bimodality. Diversity among dopamine neurons, previously treated as noise, thus becomes a representation of uncertainty. The idea has been extended to multidimensional reward distributions and has been proposed to underlie individual differences in optimism and their disturbance in depression.

## Summary

- The Rescorla–Wagner rule (Definition 39.1.1) is error-driven learning with a shared prediction; it explains blocking and overshadowing but not timing, second-order conditioning or spontaneous recovery.
- TD learning (Definition 39.2.1) predicts the discounted future reward (Eq. (39.1)) by bootstrapping; the TD error moves from reward to the earliest predictive cue and becomes negative when a predicted reward is omitted, matching dopamine responses (Remark 39.3.1), with three-factor plasticity as the mechanism.
- An MDP (Definition 39.4.1) defines value functions (Definition 39.4.2) that satisfy the Bellman equation (Theorem 39.4.1, a contraction with a unique solution) and the Bellman optimality equation (Theorem 39.4.2); greedy improvement never makes a policy worse (Theorem 39.4.3). Policy iteration and value iteration (Algorithms 39.4.1–39.4.2) solve known MDPs.
- Model-free methods learn from samples: Monte Carlo (unbiased, high variance), TD(0) (biased, low variance), TD($\lambda$) with eligibility traces; SARSA (on-policy) and Q-learning (off-policy, converges to $q_*$) learn action values (Algorithms 39.5.1–39.5.2); ε-greedy and softmax policies (Definition 39.5.1) explore.
- Function approximation generalizes across states but destabilizes bootstrapping; deep Q-networks (Definition 39.6.1) use experience replay and target networks, with an analogy to hippocampal replay.
- Distributional TD learning (Definition 39.7.1) with asymmetric learning rates represents the return distribution by expectiles (Proposition 39.7.1), which explains the spread of reversal points across dopamine neurons.

| Algorithm | Learns | Update target | Neural counterpart (hypothesized) |
|---|---|---|---|
| Rescorla–Wagner | CS strengths | $\lambda$ | US-driven prediction error |
| TD(0) | $v_\pi$ | $R_{t+1} + \gamma\,\hat v(S_{t+1})$ | Dopamine burst and pause, corticostriatal plasticity |
| SARSA | $q_\pi$ | $R_{t+1} + \gamma\,\hat q(S_{t+1}, A_{t+1})$ | Action-value coding in striatum |
| Q-learning | $q_*$ | $R_{t+1} + \gamma\max_{a'}\hat q(S_{t+1}, a')$ | Some dopamine responses reflect the best rather than the chosen option |
| Value iteration | $v_*$ | Model-based backup | Planning, replay ([7.16.41](/7.16.41)) |
| Distributional TD | Return distribution | Asymmetric TD errors | Diversity of dopamine neurons |

## Questions

1. Show that the Rescorla–Wagner rule is stochastic gradient descent on a squared prediction error, and use this to explain overshadowing: two stimuli A and B of saliences $\alpha_A > \alpha_B$ are always presented together and reinforced. What are the asymptotic strengths?

   **Answer** With features $x_i = 1$ if stimulus $i$ is present and 0 otherwise, the prediction is $\sum_i V_i x_i$ and the loss is $L = \frac12(\lambda - \sum_i V_i x_i)^2$; $-\partial L/\partial V_i = (\lambda - \sum_j V_j x_j)x_i$, so the rule is a gradient step with a stimulus-specific learning rate $\alpha_i\beta$. For the compound AB, both are updated with the same error $\lambda - V_A - V_B$; at the asymptote the error is zero, $V_A + V_B = \lambda$. The ratio of increments is constant, $\Delta V_A/\Delta V_B = \alpha_A/\alpha_B$, so starting from zero $V_A/V_B = \alpha_A/\alpha_B$ throughout, and $V_A = \lambda\alpha_A/(\alpha_A + \alpha_B)$, $V_B = \lambda\alpha_B/(\alpha_A + \alpha_B)$: the more salient stimulus overshadows the other.

2. In the TD simulation (Section 39.2.2), why does the error at the cue converge to $\gamma^{20}$ rather than to 1? What would happen if the cue were itself predicted by an earlier, perfectly reliable warning signal?

   **Answer** After learning, $\hat v$ at $k$ steps after the cue equals $\gamma^{19 - k}$ for the 20 steps before reward (reward at step 20 after the cue, counted from the step at which it is received), so the value of the cue state is $\gamma^{19}$, and the TD error at the transition from the unpredictive pre-cue state (value 0) into the cue state is $0 + \gamma\,\hat v(\text{cue}) = \gamma^{20} \approx 0.67$: the cue is worth the discounted reward. If an earlier warning signal reliably predicted the cue, the pre-cue state would acquire value and the error at the cue would vanish, moving to the warning signal: the error always appears at the earliest reliable predictor, as dopamine responses do in experiments with sequential cues.

3. For a two-state MDP with a single action in each state, $s_1 \to s_2$ with reward 0 and $s_2 \to s_2$ with reward 1, compute $v(s_1)$ and $v(s_2)$ for $\gamma = 0.9$ by solving the Bellman equation, and show how many sweeps of value iteration from $\hat v = 0$ are needed to bring $\hat v(s_2)$ within 1% of its value.

   **Answer** $v(s_2) = 1 + 0.9\,v(s_2)$ gives $v(s_2) = 10$, and $v(s_1) = 0 + 0.9\cdot10 = 9$. Value iteration gives $\hat v_k(s_2) = 1 + 0.9\,\hat v_{k-1}(s_2) = 10(1 - 0.9^k)$; the error is $10 \cdot 0.9^k$, below $0.1$ when $0.9^k < 0.01$, i.e. $k \ge 44$. The convergence rate $\gamma^k$ is the contraction modulus of Theorem 39.4.1.

4. A dopamine neuron has asymmetry $\tau = 0.8$. A cue predicts reward 0 or 1 with equal probability. What is its reversal point, and how would its responses at reward time differ from those of a neuron with $\tau = 0.5$?

   **Answer** The expectile satisfies $0.8\cdot\frac12(1 - e) = 0.2\cdot\frac12 e$, so $0.8(1 - e) = 0.2e$ and $e = 0.8$. The optimistic neuron's prediction is 0.8: a reward of 1 evokes a small positive error ($+0.2$, scaled by $\alpha^+$), no reward a large negative error ($-0.8$, scaled by $\alpha^-$, which is small). The balanced neuron ($e = 0.5$) responds with $+0.5$ and $-0.5$. Across trials the optimistic neuron's responses average to zero because its larger learning rate for positive errors compensates for their smaller size; its reversal point 0.8 lies above the mean 0.5, which is what Dabney and colleagues observed in the neurons with stronger responses to positive errors.
