---
title: "Reinforcement Learning II: Policy Gradients, Model-Based Learning and Meta-Learning"
description: "Limits of value-based methods; parameterized policies, the policy gradient theorem with proof, REINFORCE, baselines and variance; the advantage function, advantage actor–critic and the clipped objective of PPO; policy gradients in neurons (Williams' rule as a three-factor rule, node perturbation, birdsong, dopamine and the rate of policy learning); model-based and model-free control, the two-step task and its stay-probability signature, hippocampal and prefrontal substrates of planning; meta-reinforcement learning, Harlow's learning sets and the prefrontal cortex as a learned learning algorithm."
---

The algorithms of [7.16.39](/7.16.39) learn values and derive behavior from them: act greedily, or softly greedily, with respect to $\hat q$. This chapter treats three ideas that go beyond that scheme, each of which has a counterpart in the brain. The first is to learn the policy directly, by following the gradient of expected return with respect to the policy's parameters; the resulting rules have the form of three-factor synaptic plasticity and explain why the **actor–critic** architecture of the **basal ganglia** ([7.16.40](/7.16.40#sec-40.4)) works. The second is to learn a model of the environment and plan with it, which distinguishes goal-directed from habitual behavior and engages the hippocampus and prefrontal cortex. The third is meta-learning: a slow learning process, acting over many tasks, can produce a network whose own activity dynamics implement a fast learning algorithm, a view of the prefrontal cortex that connects animal "learning to learn" with the in-context learning of large artificial networks. Notation follows [7.16.39](/7.16.39) and Sutton and Barto: states $S_t$, actions $A_t$, rewards $R_t$, return $G_t$, value functions $v_\pi$ and $q_\pi$.

## 41.1. Limits of Value-Based Methods

A value-based agent acts by choosing $\arg\max_a \hat q(s, a)$. Three problems follow.

1. *Large and continuous action spaces.* The maximization is a search at every step. For a reaching movement, a continuous vector of muscle commands, the maximum of $\hat q$ over actions cannot be found by enumeration.
2. *Stochastic optimal policies.* A greedy policy is deterministic, and **ε-greedy** or softmax exploration adds randomness that is not tuned to the task. But when the agent cannot distinguish states (partial observability) or plays against an opponent, the optimal policy may be stochastic.
3. *Discontinuity.* An arbitrarily small change of $\hat q$ can switch the greedy action, so learning with function approximation can oscillate between policies instead of converging.

**Example 41.1.1 (An Aliased Corridor)** A corridor has three nonterminal states and a goal, with reward $-1$ per step (an example of Sutton and Barto). In the first and third states "right" moves right and "left" moves left (or stays at the wall), but in the second state the actions are reversed. The agent cannot tell the states apart, so any policy chooses "right" with the same probability $p$ in all of them. Solving the Bellman equation for $v(s_1)$ as a function of $p$ gives the best value $v = -(6 + 4\sqrt2) \approx -11.7$ at $p = 2 - \sqrt2 \approx 0.59$. An ε-greedy agent with $\varepsilon = 0.1$ can only realize $p = 0.95$ or $p = 0.05$, with values $-44$ and $-82$; a deterministic policy never reaches the goal.

:::

The remedy is to parameterize the policy itself, $\pi(a \mid s; \boldsymbol{\theta})$, written $\pi_{\boldsymbol{\theta}}$, and to adjust $\boldsymbol{\theta}$ to increase the expected return. Common parameterizations are a softmax over preferences $h(s, a; \boldsymbol{\theta})$ for discrete actions and a Gaussian with learned mean and variance for continuous actions.

## 41.2. The Policy Gradient Theorem

### 41.2.1. The Theorem

Consider an episodic task with start state $s_0$ and objective $J(\boldsymbol{\theta}) = v_{\pi_{\boldsymbol{\theta}}}(s_0)$. Changing $\boldsymbol{\theta}$ changes both the actions taken in each state and, through them, the distribution of states visited, and the latter depends on the unknown environment. The theorem shows that the gradient does not require the derivative of the state distribution.

**Theorem 41.2.1 (Policy Gradient Theorem)** Let $\eta(s) = \sum_{k=0}^{\infty}\gamma^k\,\mathbb{P}(S_k = s \mid S_0 = s_0, \pi_{\boldsymbol{\theta}})$ be the discounted expected number of visits to $s$. Then
$$
\nabla_{\boldsymbol{\theta}} J(\boldsymbol{\theta}) = \sum_s \eta(s) \sum_a q_\pi(s, a)\,\nabla_{\boldsymbol{\theta}}\pi(a \mid s; \boldsymbol{\theta}) = \mathbb{E}_\pi\Bigl[\sum_{t \ge 0}\gamma^t\,q_\pi(S_t, A_t)\,\nabla_{\boldsymbol{\theta}}\ln\pi(A_t \mid S_t; \boldsymbol{\theta})\Bigr]. \tag{41.1}
$$

**Proof** Write $\nabla$ for $\nabla_{\boldsymbol{\theta}}$ and $p(s' \mid s, a) = \sum_r p(s', r \mid s, a)$. From $v_\pi(s) = \sum_a \pi(a \mid s)\,q_\pi(s, a)$ and the product rule,
$$
\nabla v_\pi(s) = \sum_a \nabla\pi(a \mid s)\,q_\pi(s, a) + \sum_a \pi(a \mid s)\,\nabla q_\pi(s, a).
$$
Since $q_\pi(s, a) = \sum_{s', r}p(s', r \mid s, a)[r + \gamma v_\pi(s')]$ and the environment does not depend on $\boldsymbol{\theta}$, $\nabla q_\pi(s, a) = \gamma\sum_{s'}p(s' \mid s, a)\,\nabla v_\pi(s')$. Writing $\phi(s) = \sum_a \nabla\pi(a \mid s)\,q_\pi(s, a)$ and $P_\pi(s' \mid s) = \sum_a \pi(a \mid s)p(s' \mid s, a)$, this is the recursion $\nabla v_\pi(s) = \phi(s) + \gamma\sum_{s'}P_\pi(s' \mid s)\,\nabla v_\pi(s')$, a Bellman equation for the gradient. Unrolling it from $s_0$,
$$
\nabla v_\pi(s_0) = \sum_{k=0}^{\infty}\gamma^k\sum_s \mathbb{P}(S_k = s \mid s_0)\,\phi(s) = \sum_s \eta(s)\,\phi(s),
$$
which is the first form (the remainder $\gamma^k\,\mathbb{E}[\nabla v_\pi(S_k)]$ vanishes for $\gamma < 1$ with bounded gradients, or because the episode terminates). For the second form, write $\nabla\pi = \pi\,\nabla\ln\pi$: then $\phi(s) = \mathbb{E}_{A \sim \pi(\cdot \mid s)}[q_\pi(s, A)\,\nabla\ln\pi(A \mid s)]$, and summing over $s$ with weights $\eta(s)$ is the expectation over trajectories of $\sum_t\gamma^t(\cdot)$ evaluated at $(S_t, A_t)$. $\square$

The term $\nabla\ln\pi(A_t \mid S_t; \boldsymbol{\theta})$ is the **score function** of the policy: the direction in parameter space that most increases the probability of the action taken. Equation (41.1) says: increase the log-probability of each action in proportion to how good it is. Because $q_\pi(S_t, A_t) = \mathbb{E}[G_t \mid S_t, A_t]$, the sampled return can replace it.

**Algorithm 41.2.1 (REINFORCE)** Generate an episode $S_0, A_0, R_1, \dots, S_{T-1}, A_{T-1}, R_T$ with $\pi_{\boldsymbol{\theta}}$. For each $t = 0, \dots, T - 1$, compute $G_t = \sum_{k=t+1}^{T}\gamma^{k-t-1}R_k$ and update
$$
\boldsymbol{\theta} \leftarrow \boldsymbol{\theta} + \alpha\,\gamma^t\,(G_t - b(S_t))\,\nabla_{\boldsymbol{\theta}}\ln\pi(A_t \mid S_t; \boldsymbol{\theta}),
$$
where $b(s)$ is a baseline, any function of the state that does not depend on the action ($b = 0$ in the original form; Williams, 1992).

REINFORCE is stochastic gradient ascent on $J$: the expected update is $\alpha\nabla J$, so with suitably decreasing step sizes it converges to a local maximum. It is a Monte Carlo method, needing complete episodes, and every action of the episode is credited with the whole subsequent return. For a softmax policy, $\nabla_{\boldsymbol{\theta}}\ln\pi(a \mid s) = \nabla h(s, a) - \sum_b \pi(b \mid s)\nabla h(s, b)$: the preference of the chosen action rises and those of the others fall in proportion to their probabilities.

### 41.2.2. Baselines and Variance

**Proposition 41.2.2 (Baselines Do Not Bias the Gradient)** For any function $b(s)$ that does not depend on the action, $\sum_a b(s)\,\nabla\pi(a \mid s; \boldsymbol{\theta}) = 0$, so replacing $q_\pi(s, a)$ by $q_\pi(s, a) - b(s)$ in Eq. (41.1) leaves the gradient unchanged.

**Proof** $\sum_a b(s)\,\nabla\pi(a \mid s) = b(s)\,\nabla\sum_a\pi(a \mid s) = b(s)\,\nabla 1 = 0$. $\square$

The baseline does not change the expected update, but it can greatly change its variance. If all returns are positive, as when rewards include a constant offset, every action taken is reinforced, and the policy improves only because better actions are reinforced slightly more; the estimate is dominated by the offset. Subtracting a baseline near $v_\pi(s)$ makes the update positive for better-than-average actions and negative for worse ones. The variance-minimizing baseline is a weighted average of the returns, close to $v_\pi(s)$, which is why the state value learned by a critic is the natural choice.

**Example 41.2.1 (A Two-Armed Bandit)** Arm 1 pays $\mathcal{N}(6, 1)$ and arm 2 pays $\mathcal{N}(5, 1)$; the policy is $\pi(\text{arm }1) = \sigma(\theta)$ with the logistic function $\sigma$. The score is $1 - \pi$ for arm 1 and $-\pi$ for arm 2, and the true gradient is $\pi(1 - \pi)(\mu_1 - \mu_2)$, at most $0.25$. At $\pi = 0.5$ the single-sample estimate without baseline has standard deviation $2.8$, more than ten times the gradient; with the baseline $b = v_\pi$ it is $0.5$. Over 300 trials with $\alpha = 0.05$, agents without baseline reach $\pi(\text{arm }1) \approx 0.83$ on average with a wide spread across runs, and agents with a running-average baseline reach $0.91$ with little spread.

:::

![REINFORCE on a two-armed bandit (Example 41.2.1). A: the standard deviation of the single-sample gradient estimate against the probability of the better arm, without baseline (red) and with the baseline $b = v_\pi$ (blue), compared with the true gradient (dashed), which both estimates share. B: learning with $\alpha = 0.05$ (mean and interquartile range of 400 runs): the baseline (a running average of reward with rate 0.1) makes learning faster and far more reliable.](./plots/reinforce-baseline.py)

## 41.3. Actor–Critic Methods

### 41.3.1. The Advantage

**Definition 41.3.1 (Advantage Function)** The **advantage function** of a policy $\pi$ is $\operatorname{adv}_\pi(s, a) = q_\pi(s, a) - v_\pi(s)$, the amount by which taking action $a$ in state $s$, and following $\pi$ thereafter, is better than following $\pi$ from $s$.

With the baseline $b = v_\pi$, the policy gradient becomes $\mathbb{E}_\pi[\sum_t\gamma^t\operatorname{adv}_\pi(S_t, A_t)\nabla\ln\pi(A_t \mid S_t)]$, and the advantage averages to zero over actions, $\sum_a\pi(a \mid s)\operatorname{adv}_\pi(s, a) = 0$. It does not need to be learned separately: the **TD error** estimates it.

**Proposition 41.3.1** If $\hat v = v_\pi$, the TD error $\delta_t = R_{t+1} + \gamma\,v_\pi(S_{t+1}) - v_\pi(S_t)$ satisfies $\mathbb{E}[\delta_t \mid S_t = s, A_t = a] = \operatorname{adv}_\pi(s, a)$.

**Proof** $\mathbb{E}[R_{t+1} + \gamma v_\pi(S_{t+1}) \mid S_t = s, A_t = a] = \sum_{s', r}p(s', r \mid s, a)[r + \gamma v_\pi(s')] = q_\pi(s, a)$, and $v_\pi(S_t) = v_\pi(s)$ is fixed by the conditioning. $\square$

The proposition justifies the actor–critic algorithm of [7.16.40](/7.16.40) (Algorithm 40.4.1): updating the preference of the chosen action by $\alpha_{\mathrm{a}}\delta_t$ is a one-step, bootstrapped estimate of the policy gradient with the critic's value as baseline. In the brain's version, the same dopamine prediction error would serve as the advantage signal for the actor and as the TD error for the critic, which is consistent with the broad similarity of phasic dopamine signals sent to ventral and dorsal striatum.

**Algorithm 41.3.1 (One-Step Advantage Actor–Critic)** With policy parameters $\boldsymbol{\theta}$ and value parameters $\boldsymbol{w}$, in each step choose $A_t \sim \pi(\cdot \mid S_t; \boldsymbol{\theta})$, observe $R_{t+1}, S_{t+1}$, and compute $\delta_t = R_{t+1} + \gamma\,\hat v(S_{t+1}; \boldsymbol{w}) - \hat v(S_t; \boldsymbol{w})$ (with $\hat v = 0$ at terminal states). Then update
$$
\boldsymbol{w} \leftarrow \boldsymbol{w} + \alpha_{\boldsymbol{w}}\,\delta_t\,\nabla_{\boldsymbol{w}}\hat v(S_t; \boldsymbol{w}), \qquad \boldsymbol{\theta} \leftarrow \boldsymbol{\theta} + \alpha_{\boldsymbol{\theta}}\,\delta_t\,\nabla_{\boldsymbol{\theta}}\ln\pi(A_t \mid S_t; \boldsymbol{\theta}).
$$

The one-step TD error has low variance but is biased when $\hat v$ is wrong; $n$-step returns and eligibility traces interpolate between it and the Monte Carlo return, exactly as for prediction ([7.16.39](/7.16.39#sec-39.5.1)). Running many copies of the agent in parallel environments and averaging their gradients (A2C, A3C; Mnih and colleagues, 2016) decorrelates the samples in the way **experience replay** does for **Q-learning**.

### 41.3.2. Trust Regions and PPO

A gradient step that is too large can change the policy so much that the samples on which the estimate was based no longer describe it, and performance collapses. Trust-region methods limit the change of the policy, measured by the ratio $\rho_t = \pi_{\boldsymbol{\theta}}(A_t \mid S_t)/\pi_{\boldsymbol{\theta}_{\mathrm{old}}}(A_t \mid S_t)$ or by the Kullback–Leibler divergence between old and new policies. **Proximal policy optimization** maximizes the clipped objective $\mathbb{E}_t[\min(\rho_t\hat a_t, \operatorname{clip}(\rho_t, 1 - \varepsilon, 1 + \varepsilon)\hat a_t)]$, where $\hat a_t$ estimates the advantage, so that no single round of updates moves an action's probability by more than a factor $1 \pm \varepsilon$ (Schulman and colleagues, 2017). It is the standard algorithm of **reinforcement learning from human feedback** for language models ([4.7.9](/4.7.9#sec-9.3.3)), where the "actions" are tokens and the advantage comes from a learned reward model. The brain has no explicit trust region, but bounded learning rates and the saturation of synaptic weights limit policy changes in a similar way.

## 41.4. Policy Gradients in the Brain

### 41.4.1. Stochastic Neurons and Three-Factor Rules

Williams (1992) introduced REINFORCE for networks of stochastic units, and in that form it is a synaptic learning rule.

**Proposition 41.4.1 (REINFORCE for a Stochastic Neuron)** Let a binary neuron fire ($y = 1$) with probability $p = \sigma(\sum_j w_j x_j)$ given presynaptic activities $x_j$, and let the network receive a reward $R$ that depends on its output. Then the update
$$
\Delta w_j = \eta\,(R - b)\,(y - p)\,x_j
$$
with a baseline $b$ independent of $y$ follows the gradient of $\mathbb{E}[R]$ in expectation.

**Proof** $\ln\mathbb{P}(y) = y\ln p + (1 - y)\ln(1 - p)$, so $\partial\ln\mathbb{P}(y)/\partial w_j = (y - p)x_j$ using $\partial p/\partial w_j = p(1 - p)x_j$. The update is the REINFORCE update for a one-step episode; its expectation is $\eta\,\partial\mathbb{E}[R]/\partial w_j$ by Theorem 41.2.1 with Proposition 41.2.2. $\square$

The rule has the three factors of the **three-factor learning rule** ([7.16.14](/7.16.14#sec-14.9)): presynaptic activity $x_j$, a postsynaptic term $y - p$ that compares the actual spike with its expected probability, and a global modulatory signal $R - b$, a **reward prediction error**. Since rewards arrive later than the spikes that caused them, the product $(y - p)x_j$ must be held in an **eligibility trace**, and the rule becomes the one measured at corticostriatal synapses. For spiking neurons the corresponding term is the derivative of the log-likelihood of the spike train, which gives reward-modulated **STDP** (Pfister, Toyoizumi, Barber and Gerstner, 2006; Izhikevich, 2007).

A related rule perturbs activity directly. In *node perturbation*, each neuron's output is $y_i = \sum_j w_{ij}x_j + \xi_i$ with independent noise $\xi_i \sim \mathcal{N}(0, \sigma^2)$, and $\Delta w_{ij} = \eta\,(R - b)\,\xi_i\,x_j/\sigma^2$, which is REINFORCE for a Gaussian policy. The noise must be known to the synapse, as an injected perturbation separate from the signal. Songbirds seem to use this design: the basal ganglia–forebrain nucleus LMAN injects variability into the song motor nucleus RA, and dopamine signals to Area X evaluate each rendition, so that the song is shaped toward the template by trial and error ([7.16.36](/7.16.36#sec-36.6); Fiete, Fee and Seung, 2007). The limitation of all perturbation rules is that the variance of the gradient estimate grows with the number of perturbed units, so learning slows in proportion to network size (Werfel, Xie and Seung, 2005); they work for low-dimensional skills, not for training large networks, a problem taken up in [7.16.50](/7.16.50).

### 41.4.2. Does Dopamine Teach Values or Policies?

In the standard account, dopamine is a **TD error** used to learn values ([7.16.39](/7.16.39#sec-39.3)); in an actor–critic it also trains the policy. The two roles predict different relations between dopamine and behavior early in learning, before values are known. Coddington, Lindo and Dudman (2021) recorded and manipulated mesolimbic dopamine while naive mice learned to make an action for reward. Dopamine activity at the time of the cue and the action predicted how fast each mouse's behavior changed, the rate of policy learning, better than it matched a reward prediction error of a value-learning model, and optogenetic manipulation changed this rate. They interpreted dopamine as adapting the learning rate of a policy-gradient learner. The debate between value-based and policy-based interpretations is open; both use the same broadcast signal and the same synaptic machinery.

## 41.5. Model-Based and Model-Free Learning

### 41.5.1. Models and Planning

**Definition 41.5.1 (Model-Based and Model-Free Reinforcement Learning)** A *model* of the environment is an estimate of the transition and reward distribution $p(s', r \mid s, a)$, or of its factors $p(s' \mid s, a)$ and $\mathbb{E}[R \mid s, a]$. **Model-based reinforcement learning** learns a model and computes values or actions from it by planning (dynamic programming, tree search or simulated rollouts); **model-free reinforcement learning** learns values or policies directly from experienced rewards, without representing the consequences of actions.

**TD learning**, **Q-learning** and the **actor–critic** are model-free: their values are cached summaries of past rewards. A model-free agent that learns that a lever produces food must relearn its value if the food is devalued, by experiencing the devalued food after pressing; a model-based agent recomputes the value immediately, because its value is derived from "lever leads to food" and "food is now worthless". This is the computational account of the difference between goal-directed actions and habits ([7.16.40](/7.16.40#sec-40.5)). Model-based control is flexible but expensive: planning requires computation at decision time that grows with the depth of the search. Model-free control is cheap at decision time but slow to adapt.

The behavioral evidence for models in animals is old. In latent learning, rats that explored a maze without reward and were later rewarded at the goal learned the route almost immediately, far faster than rats that had never explored (Tolman and Honzik, 1930): exploration had built a model, a **cognitive map** ([7.16.46](/7.16.46)), without reward. At choice points, rats pause and look back and forth, and hippocampal **place cells** sweep ahead along each possible path during these pauses ("vicarious trial and error"; Johnson and Redish, 2007), as if evaluating options by simulation.

### 41.5.2. The Two-Step Task

**Definition 41.5.2 (Two-Step Task)** The **two-step task** (Daw, Gershman, Seymour, Dayan and Dolan, 2011) is a sequential choice task in which a first-stage choice between two options leads probabilistically to one of two second-stage states, each option to one state with probability $0.7$ (common transition) and to the other with $0.3$ (rare transition); in each second-stage state the subject chooses between two options that pay reward with probabilities that drift slowly over trials.

The task separates the two forms of control by the way the outcome of one trial affects the first-stage choice of the next. A model-free learner credits the first-stage choice with the reward obtained, whatever the transition: it tends to repeat a rewarded choice. A model-based learner knows the transition structure. If a rare transition led to reward, the reward says that the reached state is good, and the best way to reach it again is the *other* first-stage choice, which leads there commonly. Model-based control therefore produces an interaction between reward and transition in the probability of repeating ("staying with") the first-stage choice, whereas model-free control produces a main effect of reward only.

![Stay probabilities in the two-step task (Definition 41.5.2) for simulated agents (200 agents, 1000 trials each; learning rate 0.3, inverse temperature 5; reward probabilities drift in $[0.25, 0.75]$). A: a model-free agent (SARSA with eligibility traces, $\lambda = 1$) repeats rewarded choices regardless of the transition. B: a model-based agent, which computes first-stage values from the known transitions and the learned second-stage values, repeats a choice after a reward following a common transition but switches after a reward following a rare one, and the reverse after no reward. C: a hybrid that weights the two values equally shows both a main effect of reward and an interaction, the pattern typical of human participants.](./plots/two-step.py)

Humans show a mixture of both patterns, described by a weight $w$ on model-based values in a hybrid model (Daw and colleagues, 2011). The balance is not fixed. Model-based control is reduced by a concurrent working-memory load and by stress, increased by L-DOPA (Wunderlich, Smittenaar and Dolan, 2012), and correlates with ventral striatal dopamine measured by PET; it is reduced across a range of compulsive disorders (Gillan and colleagues, 2016). Rats trained on a version of the task are largely model-based, and inactivating the orbitofrontal cortex or the dorsal hippocampus abolishes the model-based component while sparing model-free learning (Miller, Botvinick and Brody, 2017). Even the striatal prediction error carries model-based information: in the two-step task, prediction error–related BOLD signals in the ventral striatum reflect both model-free and model-based predictions (Daw and colleagues, 2011), and dopamine transients are required for learning associations between neutral stimuli, which a pure value signal could not teach (Sharpe and colleagues, 2017).

### 41.5.3. Substrates of Planning

Where is the model, and how is it used? Several structures contribute.

| Component | Candidate substrate | Evidence |
|---|---|---|
| State space and transitions | Hippocampus and entorhinal cortex (cognitive map, [7.16.46](/7.16.46)) | **Place cells**, prospective sweeps, deficits in model-based choice after hippocampal inactivation |
| Outcome identity and value | Orbitofrontal cortex | Required for devaluation sensitivity and for inferring values of unexperienced combinations |
| Simulation | Hippocampal **replay** and preplay during rest and at choice points | Replay of paths to goals before they are taken ([7.16.46](/7.16.46#sec-46.6)) |
| Control of planning and working memory | Dorsolateral and medial prefrontal cortex | Activity scaling with planning depth, for example in the Tower of London task |

Planning by simulation links the model to model-free learning. In the Dyna architecture (Sutton, 1990), simulated transitions generated by the model train cached values as if they had been experienced, so that planning and learning use the same update; replay during rest is a candidate implementation ([7.16.46](/7.16.46#sec-46.6)). Recent models make planning itself a learned action. Jensen, Hennequin and Mattar (2024) trained a recurrent network by reinforcement learning to navigate mazes, allowing it to "think" by sampling imagined rollouts from a learned model before acting; the agent learned to plan more when planning was useful, its rollouts resembled hippocampal replay, and human participants paused longer in the same situations in which the agent performed more rollouts. A third route is the **successor representation** ([7.16.46](/7.16.46)), which caches predictions of future states rather than of rewards and so adapts immediately to changes in reward but not to changes in transitions, an intermediate between the two systems.

## 41.6. Meta-Reinforcement Learning

### 41.6.1. Learning to Learn

Harlow (1949) gave monkeys hundreds of object-discrimination problems: in each problem two new objects were presented for a few trials, and one of them always hid a raisin. On early problems the monkeys learned gradually, needing many trials per problem. After a few hundred problems they solved each new problem in one trial: if the first choice was rewarded, they kept choosing that object; if not, they switched ("win–stay, lose–shift" over objects), with trial-2 accuracy above 95%. The monkeys had formed a *learning set*: they had learned the structure common to the problems, and with it a fast strategy for learning within a problem.

**Definition 41.6.1 (Meta-Reinforcement Learning)** **Meta-reinforcement learning** is learning on two time scales over a distribution of related tasks: a slow outer process adjusts the parameters of a learning system across many tasks so as to maximize reward, and as a result the system acquires a fast inner learning procedure that adapts its behavior within a new task, from a few experiences, without further change of the slow parameters.

In machine learning, the inner procedure is often the activity of a recurrent network: a network that receives its previous action and reward as inputs, trained by a standard RL algorithm across many tasks, learns to use its activity as a memory of the current task and to act on it (Duan and colleagues, 2016; Wang and colleagues, 2016). The weights encode what is common to the tasks; the activity encodes what is specific to the current one. Learning in the activity requires no synaptic change and is fast; it is the reinforcement learning counterpart of the **in-context learning** of large language models.

![Learning to learn in Harlow's problems, with a two-level learner. Each problem has two new objects, one always rewarded, and six trials. The inner learner is a delta rule over object values (starting at 0.5) with learning rate $\alpha$ and softmax choice ($\beta = 6$); the outer loop adjusts $\alpha$ across problems by evolution strategies (gradient ascent on mean reward from random perturbations). A: accuracy within a new problem at four stages of outer learning; the learning curve steepens until the problem is solved after one trial, the pattern of Harlow's monkeys. B: trial-2 accuracy rises as the outer loop drives $\alpha$ to 1, the value that is optimal for this family of problems. In meta-reinforcement learning proper, the inner learner is the activity of a recurrent network and the outer loop shapes its weights.](./plots/learning-set.py)

The figure is a minimal illustration: the outer loop tunes a single parameter of a fixed learning rule. What makes meta-learning powerful is that the inner procedure is not fixed in advance, so that the outer loop can discover strategies, such as win–stay, lose–shift, exploration bonuses or inference of hidden task states, that no fixed rule contains.

### 41.6.2. The Prefrontal Cortex as a Meta-Learner

Wang and colleagues (2018) proposed that the prefrontal cortex is such a system. Its recurrent circuits sustain activity over seconds ([7.16.45](/7.16.45)), its inputs include the previous action and reward, and its synapses are trained slowly by dopamine-driven, model-free reinforcement learning (the outer loop). They trained a recurrent network with an advantage actor–critic (Algorithm 41.3.1) on families of tasks and compared its behavior, after training and with frozen weights, with that of animals.

- *Bandits.* Trained on two-armed bandits with randomly drawn reward probabilities, the network solved new bandits from its activity alone, approaching Bayes-optimal performance; when trained on environments that changed at different rates, its effective learning rate was higher in volatile periods, as in humans (Behrens and colleagues, 2007).
- *Two-step task.* Trained only with model-free updates of its weights, the network's behavior showed the model-based signature of Section 41.5.2 (the reward × transition interaction), because its activity had learned the transition structure common to the training tasks: model-based behavior can emerge from model-free learning at the slower time scale.
- *Harlow's task.* In a simulated three-dimensional environment with images as objects, the network acquired the one-trial learning of Harlow's monkeys.
- *Dopamine.* Prediction errors computed by the critic reflected the network's inferences about the hidden task state, as do dopamine responses in reversal tasks.

The model makes a strong claim about the division of labor: dopamine-dependent synaptic plasticity, slow and model-free, trains the prefrontal network, and the network's activity implements a second, faster learning algorithm that need not resemble TD learning. Neurons in monkey prefrontal cortex that encode abstract rules independently of the stimuli to which they apply, for example "choose the same object" versus "choose a different one" (Wallis, Anderson and Miller, 2001), and dorsolateral prefrontal neurons that track the reward history needed for adaptive choice, are consistent with it. The same structure, a slow learner that builds an inductive bias and a fast learner that uses it, recurs in the relation between evolution and individual learning, and between pre-training and in-context learning of artificial networks.

## Summary

- Value-based methods struggle with continuous actions, stochastic optimal policies and discontinuous policy changes (Example 41.1.1); policy-based methods parameterize $\pi(a \mid s; \boldsymbol{\theta})$ directly.
- The policy gradient theorem (Theorem 41.2.1) expresses $\nabla J$ through action values and the score function, without derivatives of the state distribution; REINFORCE (Algorithm 41.2.1) samples it with returns. A state-dependent baseline leaves it unbiased (Proposition 41.2.2) and can reduce the variance by an order of magnitude (Example 41.2.1).
- The advantage function (Definition 41.3.1) is estimated by the TD error (Proposition 41.3.1), which makes the actor–critic a policy-gradient method (Algorithm 41.3.1); PPO limits the change of the policy per update.
- For stochastic neurons, REINFORCE is a three-factor rule: presynaptic activity, the deviation of the postsynaptic response from its expectation, and a reward prediction error (Proposition 41.4.1); node perturbation fits song learning, but its variance grows with network size.
- Model-based learning (Definition 41.5.1) plans with a learned model; the two-step task (Definition 41.5.2) separates it from model-free learning by the reward × transition interaction in stay probabilities. Hippocampus, orbitofrontal and prefrontal cortex support model-based control; replay and learned rollouts implement planning.
- Meta-reinforcement learning (Definition 41.6.1) uses slow learning across tasks to build fast learning within tasks, as in Harlow's learning sets; the prefrontal cortex, trained by dopamine, may implement a learned learning algorithm in its activity.

| Method | Learns | Update signal | Neural interpretation |
|---|---|---|---|
| REINFORCE | Policy | $(G_t - b)\nabla\ln\pi$ | Reward-modulated plasticity of stochastic neurons; node perturbation in song learning |
| Actor–critic, A2C | Policy and $v_\pi$ | TD error as advantage | Dopamine to dorsal (actor) and ventral (critic) striatum |
| PPO | Policy within a trust region | Clipped advantage-weighted ratio | Used for RLHF in language models |
| Model-based | Model, then values by planning | Prediction errors of states and rewards | Hippocampus, OFC, PFC; replay and rollouts |
| Meta-RL | Weights across tasks, activity within a task | Slow RL on weights; inference in activity | Prefrontal recurrent dynamics trained by dopamine |

## Questions

1. For the aliased corridor of Example 41.1.1, derive $v(s_1)$ as a function of $p$ and find its maximum.

   **Answer** Let $v_1, v_2, v_3$ be the values of the three states. With probability $p$ the agent goes right: $v_1 = -1 + p v_2 + (1 - p)v_1$, $v_2 = -1 + p v_1 + (1 - p)v_3$ (actions reversed), $v_3 = -1 + (1 - p)v_2$ (right reaches the goal with value 0). The first equation gives $v_2 = v_1 + 1/p$, the third $v_3 = -1 + (1 - p)v_2$; substituting into the second, $v_1 + 1/p = -1 + p v_1 + (1 - p)[-1 + (1 - p)(v_1 + 1/p)]$, which solves to $v_1 = -\frac{2(2 - p)}{p(1 - p)}$. Setting the derivative to zero gives $p^2 - 4p + 2 = 0$, so $p = 2 - \sqrt2 \approx 0.586$ and $v_1 = -(6 + 4\sqrt2) \approx -11.66$. For $p = 0.95$ the value is $-44.2$, for $p = 0.05$ it is $-82.1$.

2. Show that the variance-minimizing constant baseline for a single-step problem with score $s(A) = \nabla\ln\pi(A)$ (one parameter) is $b^* = \mathbb{E}[R\,s(A)^2]/\mathbb{E}[s(A)^2]$, and compute it for Example 41.2.1 at $\pi = 0.5$.

   **Answer** The estimate is $g = (R - b)s(A)$ with mean independent of $b$, so minimizing $\operatorname{Var}(g)$ is minimizing $\mathbb{E}[(R - b)^2 s^2] = \mathbb{E}[R^2 s^2] - 2b\,\mathbb{E}[R s^2] + b^2\,\mathbb{E}[s^2]$, whose minimum is at $b^* = \mathbb{E}[R s^2]/\mathbb{E}[s^2]$: an average of rewards weighted by the squared score. At $\pi = 0.5$ both scores have magnitude $0.5$, so $b^* = \mathbb{E}[R] = 5.5 = v_\pi$. When the policy is skewed, rare actions have large scores and receive more weight, so $b^*$ moves toward their rewards.

3. In Proposition 41.4.1, suppose the baseline $b$ is replaced by a quantity that depends on the neuron's own output $y$, for example $b = c\,y$. Is the update still unbiased? What does this imply for biological implementations of the reward prediction error?

   **Answer** No. The expected update acquires the term $-\eta\,c\,\mathbb{E}[y(y - p)]x_j = -\eta\,c\,p(1 - p)x_j$, which is nonzero: it drives the weights in a direction unrelated to reward. The baseline must not depend on the action whose probability is being changed. A global prediction error such as the dopamine signal, computed from the state before the action (the critic's value), satisfies this; a teaching signal that partly reflected each neuron's own spiking would bias learning. This is one argument why the prediction should be computed by a separate critic.

4. In the two-step task, a model-based agent receives a reward after choosing $a_1$ and experiencing a rare transition to state C. Explain why it is now more likely to choose $a_2$, and why a model-free agent with $\lambda = 1$ is more likely to choose $a_1$. What would a model-free agent with $\lambda = 0$ do?

   **Answer** The model-based agent updates the value of the option chosen in C; since $a_2$ leads to C with probability 0.7 and $a_1$ only with 0.3, the planned value $\sum_s P(s \mid a)\max_b \hat q(s, b)$ rises more for $a_2$, so it switches. The model-free agent with $\lambda = 1$ updates $\hat q(a_1)$ toward the reward directly and repeats $a_1$. With $\lambda = 0$, $\hat q(a_1)$ is updated toward the second-stage value $\hat q(C, b)$ before the reward is received, so the reward affects the first-stage choice only on later trials, after it has propagated into $\hat q(C, b)$ and then, on a later visit, into the first-stage value of whichever action led to C; the effect is delayed and weaker, but still does not depend on the transition structure.

5. (Open question) The meta-RL account claims that dopamine-driven plasticity trains the prefrontal cortex slowly, while prefrontal activity learns quickly. Propose experiments that could distinguish this account from the alternative that fast learning within a task is itself implemented by synaptic plasticity in prefrontal cortex.

   **Answer** Approach: separate the time scales and the substrates. (i) Train animals on a family of bandit or reversal tasks until they show one-shot adaptation; then block synaptic plasticity locally in prefrontal cortex (for example with NMDA receptor antagonists or blockers of protein synthesis) during new tasks. The meta-RL account predicts that within-task adaptation survives, because it is carried by activity, while learning a new family of tasks is impaired; the alternative predicts the opposite. (ii) Record populations during task switches: meta-RL predicts that the task state is encoded in persistent activity that changes on the trial after a surprising outcome, and that perturbing this activity (brief optogenetic silencing between trials) should erase the within-task learning without affecting later performance on familiar tasks. (iii) Manipulate dopamine during the long training phase versus during new tasks: meta-RL predicts that dopamine is necessary for acquiring the learning set but less necessary for within-task adaptation once it is acquired. (iv) Fit both a recurrent-network model and a synaptic-plasticity model to the neural data and compare how well each predicts trial-by-trial changes of the population state.
