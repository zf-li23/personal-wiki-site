---
title: Optimization and Training Techniques
description: Loss landscapes of neural networks; gradient descent on quadratics and the condition number; SGD with momentum and Nesterov acceleration; AdaGrad, RMSProp, Adam with bias correction and AdamW; Lion, Muon and other recent optimizers; learning-rate schedules (step, cosine, warmup-stable-decay) and warmup; vanishing and exploding gradients and gradient clipping; data, batch, layer, instance and group normalization and RMSNorm; dropout and other regularizers; a practical recipe for choosing hyperparameters; implementations in NumPy and PyTorch.
---

**Backpropagation** ([4.7.2](/4.7.2)) tells us the gradient of the loss with respect to every weight; this chapter is about what to do with it. Training a deep network is the minimization of a high-dimensional, non-convex function from noisy gradient estimates, and plain **stochastic gradient descent** is slow on such functions: it zig-zags across narrow ravines, crawls along flat directions and needs a carefully chosen learning rate. Three groups of techniques make training fast and reliable. Better optimizers accumulate information across steps, either the direction of travel (momentum) or the scale of each coordinate (AdaGrad, RMSProp, Adam), and recent methods such as Muon even exploit the matrix structure of the weights. Learning-rate schedules, with a warmup at the start and a decay at the end, adapt the step size to the phase of training. Changes to the network itself, normalization layers and careful control of the gradient flow, make the loss landscape easier to optimize in the first place. The chapter closes with dropout and other regularizers and with a practical recipe for choosing **hyperparameters**.

The mathematics of **gradient descent**, line searches and stochastic gradient descent is developed in [3.5.4](/3.5.4) and [3.5.5](/3.5.5); the concepts of **regularization**, **weight decay**, **early stopping** and hyperparameters come from [4.7.1](/4.7.1). The normalization and optimization choices made here reappear in every later chapter: layer normalization and Adam with warmup are integral parts of the Transformer ([4.7.6](/4.7.6)), and the memory cost of optimizer states matters for large models ([4.7.8](/4.7.8)).

## 4.1. Training as Optimization

### 4.1.1. Loss Landscapes

Training minimizes the **empirical risk** $E(\boldsymbol{\theta}) = \frac{1}{m}\sum_{i=1}^m E_i(\boldsymbol{\theta})$ over the parameters $\boldsymbol{\theta} \in \mathbb{R}^p$, where $p$ ranges from thousands to trillions. Several features of this function shape the methods of this chapter.

- Non-convexity. $E$ is not a **convex function** of the weights: permuting the hidden units of a layer leaves the network function unchanged, so every minimum comes with many equivalent copies, and the segment between two copies usually passes through higher loss. Gradient methods therefore only find critical points, and the question is which ones.
- **Saddle points** rather than bad local minima. At a critical point, the **Hessian matrix** $\nabla^2 E$ has eigenvalues of both signs unless the point is a local minimum. Heuristically, in $p$ dimensions a random critical point has all $p$ eigenvalues positive with tiny probability, and empirical studies (Dauphin et al. 2014) found that critical points with high loss are almost all **saddle points**, while local minima tend to have a loss close to the global one. Plain **gradient descent** slows down near saddle points, where the gradient is small; noise and momentum help to escape them.
- Ill-conditioning. Even near a minimum the curvature differs by orders of magnitude between directions: the **Hessian** of a trained network has a few large eigenvalues and a bulk near zero. Steps that are stable in the steep directions are tiny in the flat ones (§4.1.2).
- Flat and sharp minima. Different minima with the same training loss can differ in width. Minima in wide, flat basins tend to generalize better than sharp ones (Hochreiter and Schmidhuber 1997; Keskar et al. 2017), an observation behind sharpness-aware minimization (Foret et al. 2021), although sharpness is not invariant under reparameterization and the connection is not a theorem.

Li et al. (2018) visualized the landscape by plotting $E(\boldsymbol{\theta}^* + \alpha\boldsymbol{d}_1 + \beta\boldsymbol{d}_2)$ around a trained solution $\boldsymbol{\theta}^*$ along two random directions, normalized filter by filter to the scale of the weights. For a ResNet-56 the surface is smooth and nearly convex around the minimum; removing the **skip connections** makes it chaotic, with many sharp local minima, and the effect grows with depth. Architecture design (**residual connections**, normalization) is thus also landscape design. A further surprise is that the minima found by **SGD** from different initializations are usually connected by simple curves of nearly constant low loss (*mode connectivity*, Garipov et al. 2018; Draxler et al. 2018).

### 4.1.2. Gradient Descent on a Quadratic

Near a minimum, $E$ is approximately quadratic, and the quadratic model explains most of the difficulties of first-order methods. Let $E(\boldsymbol{w}) = \frac12\boldsymbol{w}^{\mathsf T}H\boldsymbol{w}$ with $H$ symmetric positive definite, eigenvalues $0 < \mu = \lambda_{\min} \le \dots \le \lambda_{\max} = L$ and **condition number** $\kappa = L/\mu$. **Gradient descent** with learning rate $\eta$ iterates $\boldsymbol{w}_{t+1} = \boldsymbol{w}_t - \eta H\boldsymbol{w}_t = (I - \eta H)\boldsymbol{w}_t$.

**Proposition 4.1.1** Gradient descent on $E(\boldsymbol{w}) = \frac12\boldsymbol{w}^{\mathsf T}H\boldsymbol{w}$ converges to $\boldsymbol{0}$ from every starting point if and only if $0 < \eta < 2/L$. The best rate is obtained for $\eta = 2/(L + \mu)$, for which
$$
\|\boldsymbol{w}_t\| \le \left(\frac{\kappa - 1}{\kappa + 1}\right)^t\|\boldsymbol{w}_0\| .
$$

**Proof** Write $\boldsymbol{w}_0 = \sum_i c_i\boldsymbol{u}_i$ in an orthonormal eigenbasis of $H$, $H\boldsymbol{u}_i = \lambda_i\boldsymbol{u}_i$. Then $\boldsymbol{w}_t = \sum_i(1 - \eta\lambda_i)^tc_i\boldsymbol{u}_i$, which tends to $\boldsymbol{0}$ for all $c_i$ if and only if $\lvert 1 - \eta\lambda_i\rvert < 1$ for every $i$, that is $0 < \eta\lambda_i < 2$; the binding constraint is $\eta < 2/L$. The norm contracts by the factor $\rho(\eta) = \max_i\lvert 1 - \eta\lambda_i\rvert = \max(\lvert 1 - \eta\mu\rvert, \lvert 1 - \eta L\rvert)$, the **spectral radius** of $I - \eta H$. This maximum of a decreasing and an increasing function of $\eta$ is smallest where $1 - \eta\mu = \eta L - 1$, at $\eta = 2/(L + \mu)$, with value $(L - \mu)/(L + \mu) = (\kappa - 1)/(\kappa + 1)$. $\square$

The learning rate is limited by the steepest direction, and progress along the flattest direction is then governed by $1 - 2/(\kappa + 1) \approx 1 - 2/\kappa$: reducing the error by a factor $\mathrm{e}$ takes about $\kappa/2$ steps. With $\kappa = 10^4$, common in neural networks, this is thousands of steps per factor. Along the steep directions the iterate overshoots and flips sign at every step (for $\eta > 1/L$), the zig-zag across a ravine visible in the figure of §4.3.6. Every method below addresses this either by smoothing the oscillation (momentum), by rescaling the coordinates (adaptive methods, normalization) or by reshaping the landscape (architecture and initialization). In real networks the curvature also changes during training: with a fixed learning rate, full-batch gradient descent tends to increase the largest Hessian eigenvalue until it hovers around $2/\eta$, the *edge of stability* (Cohen et al. 2021), where the loss still decreases in the long run although it is no longer monotone.

### 4.1.3. Stochastic Gradient Descent in Practice

**Stochastic gradient descent** ([3.5.5](/3.5.5)), in its **mini-batch gradient descent** form, replaces $\nabla E$ by the average gradient on a random batch $\mathcal{B}_t$ of $B$ examples,
$$
\boldsymbol{g}_t = \frac{1}{B}\sum_{i \in \mathcal{B}_t}\nabla E_i(\boldsymbol{\theta}_{t-1}), \qquad \boldsymbol{\theta}_t = \boldsymbol{\theta}_{t-1} - \eta_t\boldsymbol{g}_t .
$$
$\boldsymbol{g}_t$ is an unbiased estimate of $\nabla E$ whose covariance is that of a single-example gradient divided by $B$ (for sampling with replacement). Compared with full-batch gradient descent, SGD costs $B/m$ of the computation per step, needs memory only for one batch, can be used online on streaming data, and its noise helps to escape saddle points and sharp minima. Its weaknesses are the ravine behavior of §4.1.2, now with noise, and the need to decrease the learning rate for convergence: with a constant $\eta$ the iterates fluctuate in a region around the minimum whose size grows with $\eta/B$.

The order of the examples matters. If the data are stored in a meaningful order (sorted by class, by date or by source), consecutive batches are not representative and the gradient is biased for long stretches, which can ruin convergence; a classifier trained on MNIST sorted by digit learns to predict the current digit and forgets the others. The standard remedy is to shuffle the **training set** before every epoch and draw batches without replacement. For language models trained on a single pass over trillions of **tokens**, the data mixture is shuffled once and the order of data sources is itself a design choice (curricula that end on high-quality data are common, [4.7.9](/4.7.9)).

## 4.2. Momentum

### 4.2.1. Exponential Moving Averages

All optimizers in this chapter keep running averages of gradient statistics. For a sequence $\boldsymbol{x}_1, \boldsymbol{x}_2, \dots$ and $\beta \in [0, 1)$, the *exponential moving average* is defined by $\boldsymbol{a}_0 = \boldsymbol{0}$ and
$$
\boldsymbol{a}_t = \beta\boldsymbol{a}_{t-1} + (1 - \beta)\boldsymbol{x}_t = (1 - \beta)\sum_{k=1}^t\beta^{t-k}\boldsymbol{x}_k .
$$
The weights decay geometrically with age, and the average effectively covers the last $1/(1 - \beta)$ terms: $\beta = 0.9$ averages over about $10$ steps, $\beta = 0.999$ over about $1000$. The weights sum to $1 - \beta^t$, not to $1$, so the average is biased toward the initial value $\boldsymbol{0}$ in the first $1/(1 - \beta)$ steps; Adam corrects this bias (§4.3.3).

### 4.2.2. Momentum

**Gradient descent** forgets the past: each step depends only on the current gradient. In a ravine, consecutive gradients point in nearly opposite directions across the ravine and in consistent directions along it. Averaging them cancels the oscillation and accumulates the consistent component, like a heavy ball rolling down the landscape.

**Definition 4.2.1 (Momentum)** Gradient descent with **momentum** (the heavy-ball method of Polyak 1964) with learning rate $\eta$ and momentum coefficient $\beta \in [0, 1)$ keeps a velocity $\boldsymbol{v}$, initialized to $\boldsymbol{v}_0 = \boldsymbol{0}$, and iterates
$$
\boldsymbol{v}_t = \beta\boldsymbol{v}_{t-1} + \boldsymbol{g}_t, \qquad \boldsymbol{\theta}_t = \boldsymbol{\theta}_{t-1} - \eta\boldsymbol{v}_t ,
$$
where $\boldsymbol{g}_t$ is the (stochastic) gradient at $\boldsymbol{\theta}_{t-1}$. Equivalently, $\boldsymbol{\theta}_t = \boldsymbol{\theta}_{t-1} - \eta\boldsymbol{g}_t + \beta(\boldsymbol{\theta}_{t-1} - \boldsymbol{\theta}_{t-2})$.

The usual value is $\beta = 0.9$. The velocity is $1/(1 - \beta)$ times an exponential moving average of the gradients, so under a constant gradient $\boldsymbol{g}$ the step approaches $\eta\boldsymbol{g}/(1 - \beta)$: along consistent directions momentum multiplies the effective learning rate by $10$ for $\beta = 0.9$, while oscillating components largely cancel. (Some libraries write $\boldsymbol{v}_t = \beta\boldsymbol{v}_{t-1} + (1 - \beta)\boldsymbol{g}_t$, which only rescales $\eta$; PyTorch's `SGD(momentum=0.9)` uses the form above.) On quadratics the gain can be quantified.

**Theorem 4.2.1** For $E(\boldsymbol{w}) = \frac12\boldsymbol{w}^{\mathsf T}H\boldsymbol{w}$ with eigenvalues in $[\mu, L]$ and $\kappa = L/\mu$, the heavy-ball method with
$$
\eta = \frac{4}{(\sqrt L + \sqrt\mu)^2}, \qquad \beta = \left(\frac{\sqrt\kappa - 1}{\sqrt\kappa + 1}\right)^2
$$
satisfies $\|\boldsymbol{w}_t\| \le C_t\left(\frac{\sqrt\kappa - 1}{\sqrt\kappa + 1}\right)^t\|\boldsymbol{w}_0\|$ with $C_t$ growing at most linearly in $t$ (Polyak 1964).

The contraction factor per step improves from about $1 - 2/\kappa$ to about $1 - 2/\sqrt\kappa$: for $\kappa = 10^4$, about $50$ instead of $5000$ steps per factor $\mathrm{e}$. The proof diagonalizes $H$ as in Proposition 4.1.1 and analyzes, for each eigenvalue, the $2 \times 2$ linear recurrence for $(w_t, w_{t-1})$, whose eigenvalues all have modulus $\sqrt\beta$ for this choice of parameters. For general non-quadratic functions the heavy-ball method has no such guarantee, but in **deep learning** it is robust and remains, with $\beta = 0.9$ and a decaying learning rate, the optimizer of choice for many convolutional networks.

### 4.2.3. Nesterov Accelerated Gradient

Momentum first computes the gradient and then adds the velocity. Nesterov's variant reverses the order: since the parameters are about to move by $-\eta\beta\boldsymbol{v}_{t-1}$ anyway, it evaluates the gradient at this look-ahead point, which corrects the velocity before an overshoot happens rather than after.

**Definition 4.2.2 (Nesterov Accelerated Gradient)** **Nesterov accelerated gradient** (NAG) iterates
$$
\boldsymbol{v}_t = \beta\boldsymbol{v}_{t-1} + \nabla E\bigl(\boldsymbol{\theta}_{t-1} - \eta\beta\boldsymbol{v}_{t-1}\bigr), \qquad \boldsymbol{\theta}_t = \boldsymbol{\theta}_{t-1} - \eta\boldsymbol{v}_t .
$$

For smooth **convex functions** with $L$-Lipschitz gradient, Nesterov (1983) proved that a schedule $\beta_t = (t - 1)/(t + 2)$ gives $E(\boldsymbol{\theta}_t) - E^* = O(L\|\boldsymbol{\theta}_0 - \boldsymbol{\theta}^*\|^2/t^2)$, against $O(1/t)$ for gradient descent, and that no method using only gradients can do better in the worst case; for strongly convex functions it achieves the $1 - 1/\sqrt\kappa$ rate of Theorem 4.2.1 without requiring a quadratic. Sutskever et al. (2013) showed that momentum and Nesterov momentum with a well-chosen schedule train deep and recurrent networks much better than plain **SGD**. Implementations avoid the second gradient evaluation by a change of variables: PyTorch's `SGD(nesterov=True)` computes $\boldsymbol{v}_t = \beta\boldsymbol{v}_{t-1} + \boldsymbol{g}_t$ and steps by $-\eta(\boldsymbol{g}_t + \beta\boldsymbol{v}_t)$, which is NAG written in terms of the look-ahead point.

## 4.3. Adaptive Learning Rates

Momentum still uses one learning rate for all parameters. But parameters differ enormously in the size of their gradients: the embedding of a rare word receives a gradient only when the word occurs, the weights of different layers have different scales, and the ill-conditioning of §4.1.2 is partly a matter of coordinate scales. Adaptive methods divide the step of each coordinate by a running estimate of the size of its gradients.

### 4.3.1. AdaGrad

**Definition 4.3.1 (AdaGrad)** **AdaGrad** (Duchi, Hazan and Singer 2011) accumulates the squared gradients, $\boldsymbol{s}_0 = \boldsymbol{0}$,
$$
\boldsymbol{s}_t = \boldsymbol{s}_{t-1} + \boldsymbol{g}_t \odot \boldsymbol{g}_t, \qquad \boldsymbol{\theta}_t = \boldsymbol{\theta}_{t-1} - \frac{\eta}{\sqrt{\boldsymbol{s}_t} + \varepsilon} \odot \boldsymbol{g}_t ,
$$
where the square root and the division are taken componentwise and $\varepsilon$ (e.g. $10^{-10}$) prevents division by zero.

Coordinate $i$ has the effective learning rate $\eta/\sqrt{\sum_{k \le t}g_{k,i}^2}$: parameters that have received small or rare gradients take larger steps. This is ideal for sparse problems such as linear models on bag-of-words features or word embeddings, and AdaGrad has regret guarantees for online convex optimization. For deep networks its weakness is that $\boldsymbol{s}_t$ only grows, so the effective learning rate decays like $1/\sqrt t$ even when the landscape changes and larger steps would be useful, and training stalls prematurely.

### 4.3.2. RMSProp

**Definition 4.3.2 (RMSProp)** **RMSProp** (Hinton, lecture notes 2012) replaces AdaGrad's sum by an exponential moving average with decay $\rho$ (typically $0.9$ or $0.99$):
$$
\boldsymbol{s}_t = \rho\boldsymbol{s}_{t-1} + (1 - \rho)\,\boldsymbol{g}_t \odot \boldsymbol{g}_t, \qquad \boldsymbol{\theta}_t = \boldsymbol{\theta}_{t-1} - \frac{\eta}{\sqrt{\boldsymbol{s}_t} + \varepsilon} \odot \boldsymbol{g}_t .
$$

The denominator is now a running root mean square of recent gradients, so the effective learning rate adapts to the current scale of each coordinate and can grow again when gradients shrink. Dividing by the RMS makes the update approximately invariant to rescaling the loss, and its magnitude is roughly $\eta$ per coordinate whatever the gradient scale; in the limit $\rho \to 0$ the update becomes $\eta\operatorname{sgn}(\boldsymbol{g}_t)$, sign descent. RMSProp was never published as a paper; it was introduced in Hinton's Coursera course and became a standard method for recurrent networks and **reinforcement learning** (it trained the original DQN).

### 4.3.3. Adam

Adam combines the two ideas: momentum for the direction and RMSProp for the scale, with a correction for the initialization bias of both moving averages.

**Algorithm 4.3.1 (Adam)** Adam (adaptive moment estimation; Kingma and Ba 2015) with learning rate $\eta$, decay rates $\beta_1, \beta_2 \in [0, 1)$ and $\varepsilon > 0$ (defaults $\beta_1 = 0.9$, $\beta_2 = 0.999$, $\varepsilon = 10^{-8}$) starts from $\boldsymbol{m}_0 = \boldsymbol{v}_0 = \boldsymbol{0}$ and, at step $t = 1, 2, \dots$ with gradient $\boldsymbol{g}_t$, computes

$$
\begin{aligned}
\boldsymbol{m}_t &= \beta_1\boldsymbol{m}_{t-1} + (1 - \beta_1)\boldsymbol{g}_t, &\qquad \hat{\boldsymbol{m}}_t &= \frac{\boldsymbol{m}_t}{1 - \beta_1^t}, \\
\boldsymbol{v}_t &= \beta_2\boldsymbol{v}_{t-1} + (1 - \beta_2)\,\boldsymbol{g}_t \odot \boldsymbol{g}_t, &\qquad \hat{\boldsymbol{v}}_t &= \frac{\boldsymbol{v}_t}{1 - \beta_2^t}, \\
\boldsymbol{\theta}_t &= \boldsymbol{\theta}_{t-1} - \eta\,\frac{\hat{\boldsymbol{m}}_t}{\sqrt{\hat{\boldsymbol{v}}_t} + \varepsilon} . && 
\end{aligned}
$$

$\boldsymbol{m}_t$ estimates the first moment (the mean) and $\boldsymbol{v}_t$ the second moment (the uncentered variance) of each gradient coordinate.

**Proposition 4.3.1** If the gradients $\boldsymbol{g}_1, \dots, \boldsymbol{g}_t$ have a common mean $\mathbb{E}[\boldsymbol{g}_k] = \bar{\boldsymbol{g}}$ and a common second moment $\mathbb{E}[\boldsymbol{g}_k \odot \boldsymbol{g}_k] = \bar{\boldsymbol{s}}$, then $\mathbb{E}[\boldsymbol{m}_t] = (1 - \beta_1^t)\bar{\boldsymbol{g}}$ and $\mathbb{E}[\boldsymbol{v}_t] = (1 - \beta_2^t)\bar{\boldsymbol{s}}$, so that $\hat{\boldsymbol{m}}_t$ and $\hat{\boldsymbol{v}}_t$ are unbiased.

**Proof** Unrolling the recursion, $\boldsymbol{m}_t = (1 - \beta_1)\sum_{k=1}^t\beta_1^{t-k}\boldsymbol{g}_k$, hence by linearity $\mathbb{E}[\boldsymbol{m}_t] = (1 - \beta_1)\bar{\boldsymbol{g}}\sum_{j=0}^{t-1}\beta_1^j = (1 - \beta_1^t)\bar{\boldsymbol{g}}$ by the geometric sum. The same computation applies to $\boldsymbol{v}_t$. $\square$

Without the correction, the first steps would be distorted, and not only by a small factor: at $t = 1$, $\boldsymbol{m}_1 = (1 - \beta_1)\boldsymbol{g}_1$ and $\boldsymbol{v}_1 = (1 - \beta_2)\boldsymbol{g}_1^2$, so the uncorrected step would be $\eta(1 - \beta_1)/\sqrt{1 - \beta_2} \approx 3.16\eta$ per coordinate with the defaults, because $\boldsymbol{v}$ is biased much more strongly than $\boldsymbol{m}$. With the correction the first step is $\eta\operatorname{sgn}(\boldsymbol{g}_1)$ (up to $\varepsilon$), visible in the output of §4.3.5. Several properties explain why Adam became the default optimizer of **deep learning**.

- Scale: each coordinate moves by roughly at most $\eta$ per step, whatever the scale of its gradient, so $\eta$ is a step size in parameter space and one value (around $10^{-3}$ for small networks, $10^{-4}$ to $3 \times 10^{-4}$ for large Transformers) works across many problems.
- Invariance: multiplying the loss by a constant leaves the updates unchanged (up to $\varepsilon$), and the method is invariant to a diagonal rescaling of the parameters.
- Signal-to-noise: the ratio $\hat{\boldsymbol{m}}/\sqrt{\hat{\boldsymbol{v}}}$ is small for coordinates whose gradient is mostly noise and close to $\pm 1$ for consistent ones, an automatic annealing near a minimum.

Adam is not a cure-all. Reddi, Kale and Kumar (2018) constructed convex problems on which it does not converge, because the effective learning rate $\eta/\sqrt{\hat v}$ can increase when a large gradient leaves the averaging window; AMSGrad fixes this by using the running maximum of $\boldsymbol{v}_t$, though the original Adam usually works as well in practice. On image classification with **CNNs**, well-tuned **SGD** with momentum often generalizes slightly better (Wilson et al. 2017), whereas for Transformers Adam is essential: their gradients are heavy-tailed and differently scaled across parameter blocks, and SGD trains them poorly. For large language models the common settings are $\beta_1 = 0.9$, $\beta_2 = 0.95$ (a shorter second-moment window that reacts faster to gradient spikes), $\varepsilon = 10^{-8}$ and a decoupled **weight decay** of $0.1$. Adam stores two extra numbers per parameter, which for a model with $N$ parameters trained in mixed precision accounts for $8N$ of the roughly $16N$ bytes of training state ([4.7.8](/4.7.8)).

### 4.3.4. AdamW and Decoupled Weight Decay

For **gradient descent**, adding the penalty $\frac{\lambda}{2}\|\boldsymbol{\theta}\|^2$ to the loss and shrinking the weights by a factor $1 - \eta\lambda$ at every step are the same thing (**weight decay**, [4.7.1](/4.7.1)). For adaptive methods they are not. Adding $\lambda\boldsymbol{\theta}$ to the gradient before Adam's normalization divides the penalty by $\sqrt{\hat{\boldsymbol{v}}}$, so parameters with large gradients are barely regularized and those with small gradients strongly, which is not what the penalty intends; empirically, $L^2$ **regularization** in Adam is much less effective than in SGD.

**Definition 4.3.3 (AdamW)** **AdamW** (Loshchilov and Hutter 2019) applies weight decay directly to the parameters, outside the adaptive normalization:
$$
\boldsymbol{\theta}_t = \boldsymbol{\theta}_{t-1} - \eta_t\left(\frac{\hat{\boldsymbol{m}}_t}{\sqrt{\hat{\boldsymbol{v}}_t} + \varepsilon} + \lambda\boldsymbol{\theta}_{t-1}\right),
$$
with $\boldsymbol{m}_t$, $\boldsymbol{v}_t$ computed from the gradient of the unregularized loss as in Algorithm 4.3.1.

Every parameter now shrinks at the same relative rate $\eta_t\lambda$ per step, independently of its gradient history, and the optimal $\lambda$ becomes largely independent of the learning rate. AdamW is the standard optimizer for Transformers. In PyTorch, `torch.optim.AdamW(params, lr, weight_decay=λ)` multiplies the weights by $1 - \eta_t\lambda$ before the Adam step, so the decay follows the learning-rate schedule. Biases, normalization gains and often embeddings are usually excluded from weight decay, by passing them in a separate parameter group with `weight_decay=0`.

### 4.3.5. Implementation

The following class implements one Adam step with optional decoupled weight decay, and runs it on the Rosenbrock function $f(x, y) = (1 - x)^2 + 100(y - x^2)^2$, whose minimum $(1, 1)$ lies at the bottom of a curved, narrow valley.

```python
import numpy as np


class Adam:
    """Adam with decoupled weight decay (AdamW when weight_decay > 0)."""

    def __init__(self, params, lr=1e-3, betas=(0.9, 0.999), eps=1e-8, weight_decay=0.0):
        self.params, self.lr, self.eps, self.wd = params, lr, eps, weight_decay
        self.b1, self.b2 = betas
        self.m = [np.zeros_like(p) for p in params]   # first moment (mean of gradients)
        self.v = [np.zeros_like(p) for p in params]   # second moment (mean of squared gradients)
        self.t = 0

    def step(self, grads):
        self.t += 1
        for p, g, m, v in zip(self.params, grads, self.m, self.v):
            m *= self.b1
            m += (1 - self.b1) * g
            v *= self.b2
            v += (1 - self.b2) * g * g
            m_hat = m / (1 - self.b1 ** self.t)        # bias correction
            v_hat = v / (1 - self.b2 ** self.t)
            p -= self.lr * self.wd * p                 # decoupled weight decay (in place)
            p -= self.lr * m_hat / (np.sqrt(v_hat) + self.eps)


def rosenbrock(w):
    x, y = w
    f = (1 - x) ** 2 + 100 * (y - x ** 2) ** 2
    g = np.array([-2 * (1 - x) - 400 * x * (y - x ** 2), 200 * (y - x ** 2)])
    return f, g


for lr in (0.01, 0.05):
    w = np.array([-1.5, 2.0])
    opt = Adam([w], lr=lr)
    for t in range(1, 5001):
        f, g = rosenbrock(w)
        opt.step([g])
        if t in (1, 100, 1000, 5000):
            print(f"lr {lr}  step {t:4d}  w = ({w[0]: .4f}, {w[1]: .4f})  f = {rosenbrock(w)[0]:.2e}")
```

```text
lr 0.01  step    1  w = (-1.4900,  2.0100)  f = 1.06e+01
lr 0.01  step  100  w = (-1.4050,  1.9804)  f = 5.79e+00
lr 0.01  step 1000  w = ( 0.0674,  0.0040)  f = 8.70e-01
lr 0.01  step 5000  w = ( 1.0000,  1.0000)  f = 1.68e-17
lr 0.05  step    1  w = (-1.4500,  2.0500)  f = 6.28e+00
lr 0.05  step  100  w = (-1.2673,  1.6125)  f = 5.14e+00
lr 0.05  step 1000  w = ( 0.9818,  0.9638)  f = 3.33e-04
lr 0.05  step 5000  w = ( 0.9962,  0.9923)  f = 1.56e-05
```

The first step moves each coordinate by exactly the learning rate, as computed after Proposition 4.3.1. The larger learning rate reaches the valley floor sooner but then keeps fluctuating around the minimum, while the smaller one converges to machine precision: with a constant learning rate the final accuracy is limited by the step size, which is what learning-rate decay (§4.4) addresses. The same class reproduces PyTorch's `AdamW` (PyTorch 2.14, CPU) up to floating-point rounding:

```python
import numpy as np
import torch

torch.manual_seed(0)
model = torch.nn.Linear(10, 1)
X, y = torch.randn(256, 10), torch.randn(256, 1)
ref = [p.detach().numpy().copy() for p in model.parameters()]   # NumPy copy of the weights
opt_t = torch.optim.AdamW(model.parameters(), lr=1e-2, weight_decay=0.1)
opt_n = Adam(ref, lr=1e-2, weight_decay=0.1)                      # the class defined above
for step in range(100):
    loss = torch.nn.functional.mse_loss(model(X), y)
    opt_t.zero_grad()
    loss.backward()
    opt_n.step([p.grad.numpy().astype(np.float64) for p in model.parameters()])
    opt_t.step()
diff = max(np.abs(p.detach().numpy() - r).max() for p, r in zip(model.parameters(), ref))
print(f"loss {loss.item():.4f}, max |torch - numpy| = {diff:.1e}")
```

```text
loss 0.8104, max |torch - numpy| = 4.0e-07
```

### 4.3.6. Comparison

The figure runs the methods of this section on an ill-conditioned quadratic and on the Rosenbrock function, each with a learning rate tuned by hand for that problem.

![Five optimizers on two test functions. Left: on a quadratic with condition number 25, gradient descent zig-zags across the valley, momentum and Nesterov overshoot and spiral in, RMSProp and Adam rescale the coordinates and head almost straight to the minimum. Middle and right: on the Rosenbrock function all methods first descend into the curved valley; along the valley floor Adam converges fastest, momentum and Nesterov follow, RMSProp with a constant learning rate stalls at a noise floor, and gradient descent is slowest](./plots/optimizer-trajectories.py)

The picture matches the analysis: momentum helps along the valley, adaptive scaling removes the axis-aligned part of the ill-conditioning, and Adam combines both. It is only a caricature of training a network, where gradients are noisy, the dimension is huge and ill-conditioning is not aligned with the coordinate axes. Benchmarks with careful tuning (Schmidt et al. 2021; the AlgoPerf competition, Dahl et al. 2023) find that differences between well-tuned optimizers are often smaller than the effect of tuning the learning rate and its schedule, and that Adam-type methods are the most robust choice across tasks. In practice: SGD with momentum $0.9$ for convolutional networks if one is prepared to tune the schedule, AdamW for Transformers and as the general default.

### 4.3.7. Lion

Optimizer research remains active because optimizer efficiency translates directly into the cost of training large models. Four directions are prominent in 2026: sign-based methods, orthogonalized updates, matrix preconditioners and schedule-free averaging. Chen et al. (2023) found the following update by a symbolic program search:
$$
\boldsymbol{c}_t = \beta_1\boldsymbol{m}_{t-1} + (1 - \beta_1)\boldsymbol{g}_t, \qquad \boldsymbol{\theta}_t = \boldsymbol{\theta}_{t-1} - \eta\bigl(\operatorname{sgn}(\boldsymbol{c}_t) + \lambda\boldsymbol{\theta}_{t-1}\bigr), \qquad \boldsymbol{m}_t = \beta_2\boldsymbol{m}_{t-1} + (1 - \beta_2)\boldsymbol{g}_t ,
$$
with $\beta_1 = 0.9$, $\beta_2 = 0.99$ and the sign taken componentwise. Lion ("evolved sign momentum") keeps a single state vector instead of Adam's two, and every coordinate moves by exactly $\pm\eta$ (plus decay), so it needs a learning rate $3$ to $10$ times smaller and a weight decay correspondingly larger than AdamW. It matched or slightly improved on AdamW in the original vision and language experiments; later large-scale comparisons found the gains small.

### 4.3.8. Muon

Adam treats a weight matrix as a bag of independent numbers. Muon ("MomentUm Orthogonalized by Newton–Schulz"; Jordan et al. 2024) treats it as a linear map. For each two-dimensional weight matrix $W$ with gradient $G_t$ it computes a momentum matrix $M_t = \mu M_{t-1} + G_t$ (with $\mu = 0.95$, usually in Nesterov form), replaces $M_t$ by its orthogonal polar factor, and steps along it:
$$
O_t = \operatorname{orth}(M_t) = UV^{\mathsf T} \quad\text{where } M_t = U\Sigma V^{\mathsf T}, \qquad W_t = W_{t-1} - \eta\,(s\,O_t + \lambda W_{t-1}),
$$
with $U\Sigma V^{\mathsf T}$ the reduced **singular value decomposition** and $s$ a shape-dependent scale (for example $0.2\sqrt{\max(n_{\mathrm{out}}, n_{\mathrm{in}})}$, which matches the RMS of AdamW updates so that AdamW's learning rate and weight decay can be reused, Liu et al. 2025). Orthogonalization sets all **singular values** of the update to $1$: directions that receive small but consistent gradients are amplified, dominant directions are damped. It has a clean interpretation as steepest descent in the spectral norm.

**Proposition 4.3.2** Let $G \in \mathbb{R}^{m \times n}$ have the reduced **singular value decomposition** $G = U\Sigma V^{\mathsf T}$ with $\Sigma = \operatorname{diag}(\sigma_1, \dots, \sigma_r)$, $\sigma_i > 0$. Among all $\Delta \in \mathbb{R}^{m \times n}$ with spectral norm $\|\Delta\|_2 \le 1$, the Frobenius inner product $\langle G, \Delta\rangle = \operatorname{tr}(G^{\mathsf T}\Delta)$ is minimized by $\Delta = -UV^{\mathsf T}$, with minimum $-\sum_i\sigma_i$.

**Proof** With the columns $\boldsymbol{u}_i$ of $U$ and $\boldsymbol{v}_i$ of $V$, $\langle G, \Delta\rangle = \sum_i\sigma_i\langle\boldsymbol{u}_i\boldsymbol{v}_i^{\mathsf T}, \Delta\rangle = \sum_i\sigma_i\,\boldsymbol{u}_i^{\mathsf T}\Delta\boldsymbol{v}_i$. Each term satisfies $\lvert\boldsymbol{u}_i^{\mathsf T}\Delta\boldsymbol{v}_i\rvert \le \|\boldsymbol{u}_i\|\,\|\Delta\boldsymbol{v}_i\| \le \|\Delta\|_2 \le 1$, so $\langle G, \Delta\rangle \ge -\sum_i\sigma_i$. For $\Delta = -UV^{\mathsf T}$, which has spectral norm $1$, $\boldsymbol{u}_i^{\mathsf T}\Delta\boldsymbol{v}_i = -\boldsymbol{u}_i^{\mathsf T}UV^{\mathsf T}\boldsymbol{v}_i = -1$ by orthonormality, and the bound is attained. $\square$

Gradient descent is the analogous steepest descent in the Frobenius norm (step $-G/\|G\|_{\mathrm{F}}$), and sign descent, the limit of Adam, is steepest descent in the max norm (Bernstein and Newhouse 2024). The spectral norm is the natural norm for a weight matrix because it bounds how much the layer can change its outputs, $\|\Delta\boldsymbol{x}\| \le \|\Delta\|_2\|\boldsymbol{x}\|$. Computing an SVD at every step would be too slow on GPUs, so Muon approximates $UV^{\mathsf T}$ by a few iterations of an odd matrix polynomial $X \leftarrow aX + b(XX^{\mathsf T})X + c(XX^{\mathsf T})^2X$, which acts on each singular value separately and pushes it toward $1$ (a Newton–Schulz iteration with coefficients tuned to converge fast rather than exactly):

```python
import numpy as np


def newton_schulz(G, steps=5, coeffs=(3.4445, -4.7750, 2.0315), eps=1e-7):
    """Approximate the orthogonal polar factor U V^T of G = U S V^T (as in Muon)."""
    a, b, c = coeffs
    X = G / (np.linalg.norm(G) + eps)          # Frobenius normalization: singular values <= 1
    transposed = X.shape[0] > X.shape[1]
    if transposed:                              # iterate on the wide orientation (cheaper)
        X = X.T
    for _ in range(steps):
        A = X @ X.T
        X = a * X + (b * A + c * A @ A) @ X     # odd quintic polynomial applied to singular values
    return X.T if transposed else X


rng = np.random.default_rng(0)
G = rng.standard_normal((64, 32)) @ np.diag(np.logspace(0, -3, 32))   # ill-conditioned "gradient"
O = newton_schulz(G)
U, s, Vt = np.linalg.svd(G, full_matrices=False)
print("singular values of G:      ", np.round(s[[0, 8, 16, 24, 31]], 4))
print("singular values of NS5(G): ", np.round(np.linalg.svd(O, compute_uv=False)[[0, 8, 16, 24, 31]], 3))
print("relative distance to U V^T:", round(np.linalg.norm(O - U @ Vt) / np.linalg.norm(U @ Vt), 3))
```

```text
singular values of G:       [7.3526e+00 1.1990e+00 1.9210e-01 2.7800e-02 6.2000e-03]
singular values of NS5(G):  [1.176 1.073 0.783 0.708 0.249]
relative distance to U V^T: 0.303
```

Five iterations compress a spread of singular values over three orders of magnitude to a range of about $0.25$ to $1.2$; the result is not exactly orthogonal, which turns out not to matter. Muon is applied only to the matrices of hidden layers; embeddings, the output layer, biases and normalization gains are trained with AdamW. It was introduced in 2024 to set speed records for training small language models and was shown to scale by Moonshot AI (Liu et al. 2025), who reported about twice the compute efficiency of AdamW; Moonshot's Kimi K2, a mixture-of-experts model with one trillion parameters released in 2025, was trained with a Muon variant (MuonClip) that also rescales the query and key projections to prevent exploding attention logits. PyTorch includes `torch.optim.Muon` (version 2.14 used in this chapter), with momentum $0.95$, Nesterov momentum and the coefficients above as defaults.

### 4.3.9. Preconditioned and Schedule-Free Methods

Shampoo (Gupta, Koren and Singer 2018) preconditions each weight matrix by inverse fourth roots of the accumulated matrices $\sum G_tG_t^{\mathsf T}$ and $\sum G_t^{\mathsf T}G_t$, a Kronecker-factored approximation of full-matrix AdaGrad; without its accumulation, it reduces to the orthogonalized update of Muon. SOAP (Vyas et al. 2024) runs Adam in the eigenbasis of Shampoo's preconditioner. A distributed implementation of Shampoo won the externally tuned track of the AlgoPerf competition in 2024.

Schedule-free methods (Defazio et al. 2024) replace the learning-rate schedule by a combination of iterate averaging and interpolation that achieves the performance of a tuned decay schedule without specifying the training length in advance; schedule-free AdamW won the self-tuning track of AlgoPerf.

Despite these advances, AdamW remains the most widely used optimizer for large models in 2026, with Muon its most serious challenger.

## 4.4. Learning-Rate Schedules

### 4.4.1. Decay Schedules

The learning rate is the most important **hyperparameter**, and the best value changes during training. Early on, a large learning rate makes fast progress, escapes poor regions and, because of the noise it injects, avoids fitting noise in the data; late in training, a small learning rate is needed to settle into a minimum instead of bouncing around it (the second half of the output of §4.3.5) and to fit finer patterns. You et al. (2019) found that the initial large learning rate suppresses the memorization of noisy data while the decay improves the learning of complex patterns.

**Definition 4.4.1 (Learning-Rate Schedule)** A **learning-rate schedule** is a function $t \mapsto \eta_t$ that sets the learning rate at step $t$ of a run of $T$ steps, usually as a peak rate $\eta_{\max}$ times a profile. The common profiles are:

| Schedule | $\eta_t / \eta_{\max}$ | Typical use |
|---|---|---|
| step decay | $\gamma^{\lfloor t/s\rfloor}$, e.g. $\gamma = 0.1$ every $s$ steps (or at fixed epochs) | ResNets on ImageNet: $\times 0.1$ at epochs 30, 60, 90 |
| exponential decay | $\gamma^t$ | older models, small problems |
| cosine | $r + \frac12(1 - r)\bigl(1 + \cos(\pi t/T)\bigr)$, decaying to the fraction $r$ (often $0.1$ or $0$) | most vision models and Transformers since 2017 |
| inverse square root | $\min\bigl(t/w,\ \sqrt{w/t}\bigr)$ after $w$ warmup steps | the original Transformer; open-ended training |
| warmup-stable-decay (WSD) | warmup, then constant $1$, then a fast decay (linear, cosine or $1 - \sqrt{\cdot}$) to near $0$ over the last 10–20% | language-model pre-training since 2024 |
| reduce on plateau | multiply by $\gamma$ when the validation loss stops improving | small experiments |

The cosine schedule (Loshchilov and Hutter 2017, who also proposed restarting it periodically) decays smoothly and spends most of the run at a moderately high learning rate. Its drawback for large-scale training is that the shape depends on $T$: to train longer one must start over, and intermediate checkpoints are not fully annealed. The *warmup-stable-decay* schedule (Hu et al. 2024, MiniCPM; similar trapezoidal schedules earlier) avoids this: the long constant phase can be continued indefinitely, and a short decay phase from any checkpoint of it produces an annealed model, during which the loss drops sharply. WSD matches or beats cosine at equal compute and makes it cheap to study how the loss depends on the training length; a common interpretation is a "river valley" landscape, in which the high learning rate makes fast progress along the river while bouncing between the hillsides, and the decay descends to the river bed (Wen et al. 2024). The original Transformer used $\eta_t = d_{\mathrm{model}}^{-1/2}\min(t^{-1/2}, t\,w^{-3/2})$ with $w = 4000$, linear warmup followed by inverse-square-root decay.

![Learning-rate schedules over 10000 steps with peak learning rate 1 and 500 warmup steps (left): step decay, exponential decay, linear warmup with cosine decay to 10%, warmup-stable-decay with a linear decay over the last 20%, and the inverse square root schedule of the original Transformer; the first 1500 steps in detail (right)](./plots/lr-schedules.py)

### 4.4.2. Warmup

**Definition 4.4.2 (Learning-Rate Warmup)** **Learning-rate warmup** increases the learning rate from (nearly) zero to its peak value over the first $w$ steps of training, usually linearly, $\eta_t = \eta_{\max}\,t/w$ for $t \le w$, before the decay schedule takes over.

Typical warmups last a few hundred to a few thousand steps (about 1% of a long run). Warmup became standard for three related reasons.

- Large batches. Goyal et al. (2017) trained ResNet-50 on ImageNet in one hour with batches of $8192$ images by scaling the learning rate linearly with the batch size ($\eta = 0.1 \cdot B/256$); this only worked with a gradual warmup over the first five epochs, because at initialization the network changes rapidly and the large learning rate diverges.
- Adaptive optimizers. In the first steps Adam's second-moment estimate $\hat{\boldsymbol{v}}_t$ averages only a few gradients and has a large variance, so the adaptive learning rate $\eta/\sqrt{\hat{\boldsymbol{v}}_t}$ is unreliable; warmup acts as variance reduction (Liu et al. 2020, who proposed RAdam, a version of Adam that rectifies this variance analytically).
- Transformers. Post-norm Transformers ([4.7.6](/4.7.6)) have large gradients near the output at initialization and diverge without warmup (Xiong et al. 2020); pre-norm Transformers are more tolerant but still use a warmup in practice.

Warmup stabilizes training, permits higher peak learning rates, and thereby often accelerates convergence and improves the final result.

### 4.4.3. Learning Rate and Batch Size

The noise of **SGD** has a scale proportional to $\eta/B$: the learning rate times the variance of a batch gradient. Doubling the batch halves the noise, so to first order the same trajectory is obtained by doubling the learning rate, the linear scaling rule of Goyal et al.; equivalently, instead of decaying the learning rate one can increase the batch size during training (Smith et al. 2018). The rule holds up to a critical batch size, beyond which larger batches no longer reduce the number of steps needed and only waste computation (McCandlish et al. 2018); for adaptive optimizers the learning rate scales more like $\sqrt B$ up to that point. The critical batch size grows as the loss decreases, which is why large language models are trained with batches of millions of **tokens**, often increased during training.

## 4.5. Vanishing and Exploding Gradients

### 4.5.1. Products of Jacobians

The **backpropagation** equations (Theorem 2.4.1) give for an **MLP** $\boldsymbol{\delta}^{(l)} = D^{(l)}W^{(l+1)\mathsf T}\boldsymbol{\delta}^{(l+1)}$ with $D^{(l)} = \operatorname{diag}\bigl(\varphi'(\boldsymbol{z}^{(l)})\bigr)$, hence
$$
\boldsymbol{\delta}^{(l)} = D^{(l)}W^{(l+1)\mathsf T}D^{(l+1)}W^{(l+2)\mathsf T}\cdots D^{(L-1)}W^{(L)\mathsf T}\boldsymbol{\delta}^{(L)} .
$$
The error signal reaching layer $l$ is the output error multiplied by $L - l$ Jacobian matrices, and products of many matrices tend to grow or shrink exponentially.

**Proposition 4.5.1** If $\lvert\varphi'\rvert \le \gamma$ and $\|W^{(k)}\|_2 \le \omega$ for all layers, then $\|\boldsymbol{\delta}^{(l)}\| \le (\gamma\omega)^{L-l}\|\boldsymbol{\delta}^{(L)}\|$.

**Proof** The spectral norm is submultiplicative and $\|D^{(k)}\|_2 = \max_j\lvert\varphi'(z^{(k)}_j)\rvert \le \gamma$, $\|W^{(k)\mathsf T}\|_2 = \|W^{(k)}\|_2 \le \omega$; apply this to each factor of the product. $\square$

For the sigmoid, $\gamma = \frac14$, so unless the weights have norm above $4$ the gradient shrinks geometrically with depth; this is why deep sigmoid networks with many layers were so hard to train in the 1990s. Conversely, if the factors typically expand vectors, the gradient grows geometrically.

**Definition 4.5.1 (Vanishing and Exploding Gradients)** A deep network (or a recurrent network unrolled in time) suffers from a **vanishing gradient** when the gradients with respect to the parameters of early layers (or early time steps) are exponentially smaller than those of late ones, so that early layers learn extremely slowly; it suffers from an **exploding gradient** when they are exponentially larger, so that gradient steps become huge and training diverges.

Both are symptoms of the same multiplicative structure, and both affect the forward pass too: activations explode or vanish under the same products. Vanishing gradients make learning slow or impossible for the early layers but do not show up as errors; exploding gradients produce loss spikes, overflow and `NaN` values. Recurrent networks are the extreme case, since the same matrix is multiplied at every time step ([4.7.5](/4.7.5)).

### 4.5.2. Remedies

The techniques of this and the previous chapters can be read as ways to keep the product of Jacobians close to norm-preserving.

| Remedy | How it controls the product | Where |
|---|---|---|
| **ReLU** and its variants | $\varphi' = 1$ on the active half instead of $\le \frac14$ | [4.7.2](/4.7.2) §2.6 |
| variance-preserving **weight initialization** (Xavier, He) | each layer preserves the variance of activations and gradients at initialization | [4.7.2](/4.7.2) §2.7 |
| residual connections | the Jacobian of $\boldsymbol{x} + F(\boldsymbol{x})$ is $I + J_F$, so gradients have an identity path | [4.7.3](/4.7.3) §3.6.5 |
| normalization layers | rescale activations at every layer, decoupling the scale of successive layers | §4.6 |
| gating (LSTM, GRU) | an additive memory path whose Jacobian is a learned diagonal close to $I$ | [4.7.5](/4.7.5) |
| gradient clipping | limits the size of a step when the gradient explodes | §4.5.3 |
| orthogonal initialization | all singular values of $W$ equal to $1$ | recurrent networks, very deep linear analyses |

### 4.5.3. Gradient Clipping

Vanishing gradients require architectural remedies; exploding gradients can also be handled at the optimizer level. Near a "cliff" of the loss surface the gradient is enormous, and a single step along it throws the parameters far away and undoes the progress made so far; it suffices to bound the length of the step.

**Definition 4.5.2 (Gradient Clipping)** **Gradient clipping** by norm with threshold $c > 0$ replaces the gradient $\boldsymbol{g}$ of all parameters by
$$
\tilde{\boldsymbol{g}} = \boldsymbol{g}\cdot\min\left(1, \frac{c}{\|\boldsymbol{g}\|}\right)
$$
before the optimizer step, keeping its direction and limiting its norm to $c$. Clipping by value instead clamps each component to $[-c, c]$, which also changes the direction.

Clipping by the global norm, computed over all parameters together, was introduced for recurrent networks (Mikolov 2012; Pascanu, Mikolov and Bengio 2013) and is standard in training Transformers, typically with $c = 1.0$; in PyTorch it is one call, `torch.nn.utils.clip_grad_norm_(model.parameters(), max_norm=1.0)`, between `loss.backward()` and `opt.step()`, and its return value, the norm before clipping, is a useful quantity to log. Frequent clipping indicates that the learning rate is too high or that there is a problem in the data or the model. In large-model training, loss spikes are also handled by skipping batches with anomalous gradient norms, by rolling back to an earlier checkpoint, and by architectural measures such as normalizing the queries and keys of attention.

## 4.6. Normalization

### 4.6.1. Data Normalization

The simplest way to improve the conditioning of the loss is to preprocess the inputs. For linear regression with squared loss, the **Hessian** is $\frac{1}{m}X^{\mathsf T}X$, whose entries are the second moments of the features. If one feature is measured in meters and another in millimeters, or one has mean $1000$ and standard deviation $1$, the Hessian has eigenvalues of very different sizes, the level sets of the loss are elongated ellipses, and the gradient points mostly across the valley rather than toward the minimum. Standardizing each feature,
$$
x'_j = \frac{x_j - \mu_j}{\sigma_j},
$$
with the mean $\mu_j$ and standard deviation $\sigma_j$ computed on the **training set** (and the same values applied to validation and test data), makes the features centered and of unit scale, and turns the Hessian into the correlation matrix of the features. Whitening goes further and decorrelates the features, for example by **principal component analysis**, so that the Hessian becomes the identity; it is rarely done for high-dimensional inputs. For images the usual normalization subtracts the per-channel mean and divides by the per-channel standard deviation of the training set.

### 4.6.2. Batch Normalization

Normalizing the inputs only helps the first layer. Every hidden layer receives inputs produced by the layers below, whose distribution changes whenever those layers' weights change, and in a deep network a small change in a low layer can be amplified into a large change in the input distribution of a high layer, which then has to readapt. Ioffe and Szegedy (2015) called this *internal covariate shift* and proposed to normalize the inputs of every layer over the mini-batch.

**Definition 4.6.1 (Batch Normalization)** A **batch normalization** layer with parameters $\boldsymbol{\gamma}, \boldsymbol{\beta} \in \mathbb{R}^d$ maps a mini-batch $\boldsymbol{x}_1, \dots, \boldsymbol{x}_m \in \mathbb{R}^d$ (pre-activations of a layer, one row per example) to
$$
\hat{\boldsymbol{x}}_i = \frac{\boldsymbol{x}_i - \boldsymbol{\mu}_{\mathcal{B}}}{\sqrt{\boldsymbol{\sigma}^2_{\mathcal{B}} + \varepsilon}}, \qquad \boldsymbol{y}_i = \boldsymbol{\gamma} \odot \hat{\boldsymbol{x}}_i + \boldsymbol{\beta}, \qquad \boldsymbol{\mu}_{\mathcal{B}} = \frac{1}{m}\sum_{i=1}^m\boldsymbol{x}_i, \quad \boldsymbol{\sigma}^2_{\mathcal{B}} = \frac{1}{m}\sum_{i=1}^m(\boldsymbol{x}_i - \boldsymbol{\mu}_{\mathcal{B}})^2,
$$
all operations componentwise and $\varepsilon$ (e.g. $10^{-5}$) a small constant. At inference time $\boldsymbol{\mu}_{\mathcal{B}}$ and $\boldsymbol{\sigma}^2_{\mathcal{B}}$ are replaced by population estimates, usually exponential moving averages of the batch statistics accumulated during training, so that the layer becomes a fixed affine map.

Each feature is normalized to mean $0$ and variance $1$ over the batch, and the learnable scale $\boldsymbol{\gamma}$ and shift $\boldsymbol{\beta}$ restore the expressive power: with $\boldsymbol{\gamma} = \sqrt{\boldsymbol{\sigma}^2 + \varepsilon}$ and $\boldsymbol{\beta} = \boldsymbol{\mu}$ the layer could undo the normalization. What changes is the parameterization: the mean and scale of the layer's output are now controlled directly by two parameters instead of by a delicate interplay of all weights below. BN is placed after a linear or **convolutional layer** and before the activation; the bias of that layer becomes redundant, since $\boldsymbol{\beta}$ takes its role. In a **convolutional neural network** with **feature maps** of shape $(N, C, H, W)$ the statistics are computed per channel over the batch and all spatial positions ($N \cdot H \cdot W$ values each), so that the normalization respects the translation equivariance of the **convolution**, and $\boldsymbol{\gamma}, \boldsymbol{\beta} \in \mathbb{R}^C$.

Since $\boldsymbol{\mu}_{\mathcal{B}}$ and $\boldsymbol{\sigma}_{\mathcal{B}}$ depend on all examples of the batch, the backward pass must differentiate through them.

**Proposition 4.6.1** For one feature, with $\boldsymbol{g} = \partial E/\partial\boldsymbol{y} \in \mathbb{R}^m$ the upstream gradients over the batch and $s = \sqrt{\sigma^2_{\mathcal{B}} + \varepsilon}$,
$$
\frac{\partial E}{\partial\gamma} = \sum_{i=1}^m g_i\hat x_i, \qquad \frac{\partial E}{\partial\beta} = \sum_{i=1}^m g_i, \qquad \frac{\partial E}{\partial x_i} = \frac{\gamma}{ms}\Bigl(m g_i - \sum_{j=1}^m g_j - \hat x_i\sum_{j=1}^m g_j\hat x_j\Bigr).
$$

**Proof** The first two formulas follow from $y_i = \gamma\hat x_i + \beta$. For the third, $\partial E/\partial\hat x_j = \gamma g_j$, and $\hat x_j = (x_j - \mu)/s$ depends on $x_i$ directly and through $\mu$ and $s$. From $\partial\mu/\partial x_i = 1/m$ and $\partial\sigma^2/\partial x_i = \frac{2}{m}(x_i - \mu)$ (the term from $\partial\mu/\partial x_i$ vanishes because $\sum_j(x_j - \mu) = 0$) we get $\partial s/\partial x_i = (x_i - \mu)/(ms) = \hat x_i/m$, hence
$$
\frac{\partial\hat x_j}{\partial x_i} = \frac{1}{s}\Bigl(\boldsymbol{1}\{i = j\} - \frac1m\Bigr) - \frac{x_j - \mu}{s^2}\cdot\frac{\hat x_i}{m} = \frac{1}{ms}\bigl(m\boldsymbol{1}\{i = j\} - 1 - \hat x_j\hat x_i\bigr).
$$
Multiplying by $\gamma g_j$ and summing over $j$ gives the formula. $\square$

The gradient with respect to the inputs is the upstream gradient with its mean and its component along $\hat{\boldsymbol{x}}$ removed: BN makes the loss invariant to shifting or scaling the inputs of a feature, so the gradient has no component in those directions. The following code checks the formula against finite differences.

```python
import numpy as np


def batchnorm_forward(X, gamma, beta, eps=1e-5):
    """X: (m, d) mini-batch. Normalizes each feature over the batch."""
    mu = X.mean(axis=0)
    var = X.var(axis=0)                       # biased variance, as in training mode
    inv_std = 1.0 / np.sqrt(var + eps)
    X_hat = (X - mu) * inv_std
    return gamma * X_hat + beta, (X_hat, inv_std, gamma)


def batchnorm_backward(G, cache):
    """G = dE/dY. Returns dE/dX, dE/dgamma, dE/dbeta (Proposition 4.6.1)."""
    X_hat, inv_std, gamma = cache
    m = G.shape[0]
    dgamma = (G * X_hat).sum(axis=0)
    dbeta = G.sum(axis=0)
    dX = gamma * inv_std / m * (m * G - dbeta - X_hat * dgamma)
    return dX, dgamma, dbeta


rng = np.random.default_rng(0)
X = rng.normal(3.0, 2.0, size=(16, 4))
gamma, beta = rng.normal(size=4), rng.normal(size=4)
C = rng.normal(size=(16, 4))                      # E = sum(C * Y), so dE/dY = C
Y, cache = batchnorm_forward(X, gamma, beta)
print(f"max |batch mean of Y - beta| = {np.abs((Y - beta).mean(axis=0)).max():.1e}")
dX, dgamma, dbeta = batchnorm_backward(C, cache)
h, num = 1e-6, np.zeros_like(X)
for idx in np.ndindex(X.shape):                    # central differences
    Xp, Xm = X.copy(), X.copy()
    Xp[idx] += h
    Xm[idx] -= h
    num[idx] = (np.sum(C * batchnorm_forward(Xp, gamma, beta)[0])
                - np.sum(C * batchnorm_forward(Xm, gamma, beta)[0])) / (2 * h)
print(f"max |analytic - numerical| = {np.abs(dX - num).max():.1e}")
print(f"max |column sum of dE/dX|  = {np.abs(dX.sum(axis=0)).max():.1e}")
```

```text
max |batch mean of Y - beta| = 4.2e-16
max |analytic - numerical| = 2.8e-09
max |column sum of dE/dX|  = 9.4e-16
```

Batch normalization made very deep networks much easier to train. It stabilizes the gradients, allows learning rates ten times higher, makes training far less sensitive to initialization, and has a mild regularizing effect, because each example's normalization depends on the random other examples in its batch; Inception networks with BN reached the accuracy of their predecessors in 14 times fewer steps. Why it works is less clear than that it works. Santurkar et al. (2018) showed that BN does not actually reduce internal covariate shift in a measurable sense, and that its main effect is to make the loss landscape smoother: the loss and its gradient become more Lipschitz, so larger steps are safe. A related explanation is scale invariance: the output of a BN layer does not change when the weights below it are scaled, so the effective learning rate of those weights is $\eta/\|\boldsymbol{w}\|^2$ and is automatically tuned by **weight decay**.

BN also has drawbacks, all stemming from its dependence on the batch. With small batches (common in detection, segmentation and video, where one image fills a GPU) the batch statistics are noisy and accuracy drops. Training and inference compute different functions, which causes subtle bugs: forgetting to switch to evaluation mode, or a distribution shift between the training batches and test data. Statistics must be synchronized across devices in distributed training. And for sequence models with variable lengths, batch statistics over positions are awkward. These issues motivated normalizations that work on a single example.

### 4.6.3. Layer Normalization

**Definition 4.6.2 (Layer Normalization)** **Layer normalization** (Ba, Kiros and Hinton 2016) normalizes each example over its features: for $\boldsymbol{x} \in \mathbb{R}^d$,
$$
\mu = \frac1d\sum_{j=1}^d x_j, \qquad \sigma^2 = \frac1d\sum_{j=1}^d(x_j - \mu)^2, \qquad \operatorname{LN}(\boldsymbol{x}) = \boldsymbol{\gamma} \odot \frac{\boldsymbol{x} - \mu\boldsymbol{1}}{\sqrt{\sigma^2 + \varepsilon}} + \boldsymbol{\beta},
$$
with learnable $\boldsymbol{\gamma}, \boldsymbol{\beta} \in \mathbb{R}^d$.

The statistics are computed per example (and, in a sequence model, per position), so layer normalization behaves identically in training and inference, works with a batch of one, and handles sequences of any length. It was designed for recurrent networks, where it is applied to the summed inputs at every time step and mitigates vanishing and exploding gradients ([4.7.5](/4.7.5)), and it is a core component of the Transformer, where it normalizes the $d_{\mathrm{model}}$-dimensional vector of each **token** ([4.7.6](/4.7.6)). It is less effective than BN in convolutional networks, where it would normalize over all channels and positions of an image together, although ConvNeXt and vision Transformers use it successfully ([4.7.3](/4.7.3)).

### 4.6.4. Instance and Group Normalization

For a tensor of shape $(N, C, H, W)$ (batch, channels, height, width), normalization methods differ in the set of entries over which the mean and variance are computed.

**Definition 4.6.3 (Instance and Group Normalization)** **Instance normalization** (Ulyanov, Vedaldi and Lempitsky 2016) computes the statistics separately for each example and each channel, over the $H \times W$ spatial positions. **Group normalization** (Wu and He 2018) divides the $C$ channels into $G$ groups of $C/G$ consecutive channels and computes the statistics for each example and each group, over $(C/G) \times H \times W$ entries. Both then apply a per-channel learnable scale and shift as in Definition 4.6.1.

| Method | Statistics computed over | Shared across | Typical use |
|---|---|---|---|
| batch normalization | $N, H, W$ (per channel) | the batch | CNNs for classification with large batches |
| layer normalization | $C, H, W$ (per example), or the feature vector of one token | — | RNNs, Transformers |
| instance normalization | $H, W$ (per example and channel) | — | style transfer, image generation |
| group normalization | $C/G, H, W$ (per example and group) | — | detection, segmentation, small batches, diffusion U-Nets |

Group normalization interpolates between the two per-example methods: with $G = 1$ it is layer normalization, with $G = C$ instance normalization; $G = 32$ is the usual default. Instance normalization removes the contrast and overall color statistics of each image, which is what one wants in style transfer, where these statistics carry the style. Group normalization is independent of the batch size and, at batch size $2$, beats batch normalization by a large margin on ImageNet (Wu and He 2018).

### 4.6.5. RMSNorm

**Definition 4.6.4 (RMSNorm)** **RMSNorm** (root mean square layer normalization; Zhang and Sennrich 2019) rescales a vector $\boldsymbol{x} \in \mathbb{R}^d$ by its root mean square without centering it:
$$
\operatorname{RMSNorm}(\boldsymbol{x}) = \boldsymbol{\gamma} \odot \frac{\boldsymbol{x}}{\operatorname{RMS}(\boldsymbol{x})}, \qquad \operatorname{RMS}(\boldsymbol{x}) = \sqrt{\frac1d\sum_{j=1}^d x_j^2 + \varepsilon},
$$
with a learnable gain $\boldsymbol{\gamma} \in \mathbb{R}^d$ and no shift.

Zhang and Sennrich argued that the success of layer normalization comes from its invariance to rescaling the inputs, not from the centering, and dropping the mean saves computation and one parameter vector with no loss in quality. RMSNorm is the normalization of essentially all large language models since LLaMA (2023), including the Qwen, DeepSeek, Gemma and Mistral families. Variants apply it at additional places, for example to the queries and keys before the attention product (QK-norm, used in Qwen3, OLMo 2 and Gemma 3) to prevent attention logits from growing. Zhu et al. (2025) showed that Transformers can even be trained without normalization layers by replacing them with an elementwise $\boldsymbol{\gamma} \odot \tanh(\alpha\boldsymbol{x}) + \boldsymbol{\beta}$ with a learnable scalar $\alpha$ (dynamic tanh), which mimics the squashing that layer normalization performs on outliers.

### 4.6.6. Normalization in PyTorch

The following code (PyTorch 2.14, CPU) checks the definitions of layer normalization and RMSNorm against the library modules, and shows the difference between training and evaluation mode in batch normalization.

```python
import torch
from torch import nn

torch.manual_seed(0)
x = torch.randn(2, 5, 8) * 3 + 1                 # (batch, sequence, features)
ln, rms = nn.LayerNorm(8), nn.RMSNorm(8, eps=1e-6)
mu, var = x.mean(-1, keepdim=True), x.var(-1, unbiased=False, keepdim=True)
print(torch.allclose(ln(x), (x - mu) / torch.sqrt(var + 1e-5), atol=1e-6))
print(torch.allclose(rms(x), x / torch.sqrt((x ** 2).mean(-1, keepdim=True) + 1e-6), atol=1e-6))

bn = nn.BatchNorm1d(8)                            # expects (batch, features) or (batch, features, length)
h = torch.randn(32, 8) * 2 + 5
bn.train()
y_train = bn(h)                                   # batch statistics; updates running estimates
bn.eval()
y_eval = bn(h)                                    # running estimates: different output
print(f"|mean| in train mode {y_train.mean().abs():.3f}, mean in eval mode {y_eval.mean():.3f}")
print("running mean after one batch:", bn.running_mean[:3])
```

```text
True
True
|mean| in train mode 0.000, mean in eval mode 4.084
running mean after one batch: tensor([0.4716, 0.5170, 0.4862])
```

The running mean starts at $0$ and is updated as $0.9 \cdot \text{old} + 0.1 \cdot \text{batch mean}$ (PyTorch calls $0.1$ the `momentum` of the layer), so after one batch with mean about $5$ it is about $0.5$, and the evaluation-mode output is far from normalized. Running statistics need many batches to converge, and `model.eval()` must be called before evaluation; both are frequent sources of bugs.

## 4.7. Regularization

### 4.7.1. Penalties, Early Stopping and Data Augmentation

A network with millions of parameters can fit its **training set** perfectly, including its noise, and **overfitting** is controlled by **regularization** ([4.7.1](/4.7.1)). The main techniques in **deep learning** are:

- **Early stopping**: return the parameters with the best validation loss ([4.7.1](/4.7.1) §1.4.3). It is nearly free and always worth monitoring, although modern practice often trains to a fixed budget with a decaying learning rate instead.
- Parameter norm penalties: the $L^2$ penalty $\frac\lambda2\|\boldsymbol{\theta}\|^2$, implemented as (decoupled) **weight decay** with $\lambda$ between $10^{-5}$ and $0.1$; the $L^1$ penalty $\lambda\|\boldsymbol{\theta}\|_1$, which produces sparse weights (as in the **Lasso**) but is rarely used for whole networks; and the elastic net, a combination of both. Max-norm constraints, which project the incoming weight vector of each unit back onto a ball $\|\boldsymbol{w}\| \le c$ after each step, work well together with dropout (Srivastava et al. 2014).
- *Data augmentation*: training on randomly transformed copies of the training examples, with transformations that preserve the label, so that the model learns the corresponding invariances and effectively sees more data. For images: random crops, flips, scaling, color jitter, and stronger policies such as RandAugment, Cutout, Mixup (training on convex combinations of pairs of examples and their labels) and CutMix. For text, back-translation and paraphrasing; for speech, SpecAugment.
- Label smoothing (Szegedy et al. 2016): replacing the one-hot target by $(1 - \alpha)\boldsymbol{y} + \alpha/k$ for $k$ classes, with $\alpha \approx 0.1$, which prevents the logits from growing without bound to fit the targets exactly and improves calibration.
- Noise: the gradient noise of small-batch **SGD**, noise added to inputs or weights, and dropout below.

### 4.7.2. Dropout

A large network can fit the training data by brittle co-adaptations, in which a unit is useful only in the presence of specific other units. Dropout breaks them by randomly removing units during training.

**Definition 4.7.1 (Dropout)** **Dropout** with rate $p \in [0, 1)$ (Hinton et al. 2012; Srivastava et al. 2014) multiplies, during training, each activation of a layer by an independent random mask: for an activation vector $\boldsymbol{a}$,
$$
\tilde{\boldsymbol{a}} = \frac{1}{1 - p}\,\boldsymbol{r} \odot \boldsymbol{a}, \qquad r_j \overset{\text{iid}}{\sim} \mathrm{Ber}(1 - p),
$$
drawing a new mask for every example and every step; at inference time the layer is the identity. The factor $1/(1 - p)$, the *inverted* form used by all modern libraries, keeps $\mathbb{E}[\tilde{\boldsymbol{a}}] = \boldsymbol{a}$; the original formulation instead left training unscaled and multiplied the outgoing weights by $1 - p$ at test time.

In the backward pass the same mask is applied to the gradient, so dropped units receive no gradient in that step. Typical rates are $p = 0.5$ for fully connected hidden layers, $0.1$ to $0.2$ for inputs and in Transformers, and lower values for **convolutional layers**, where spatially correlated activations make unit-wise dropout less effective (dropping whole channels works better).

```python
import numpy as np


def dropout(A, p, rng, training=True):
    """Inverted dropout: drop each unit with probability p, scale survivors by 1/(1-p)."""
    if not training or p == 0.0:
        return A, None
    mask = (rng.random(A.shape) >= p) / (1.0 - p)    # the same mask is reused in the backward pass
    return A * mask, mask


rng = np.random.default_rng(0)
A = rng.random((1000, 256))
D, mask = dropout(A, 0.5, rng)
print(f"fraction zeroed {np.mean(D == 0):.3f}, mean before {A.mean():.4f}, after {D.mean():.4f}")
G = np.ones_like(D)            # upstream gradient dE/dD
print("backward = G * mask:", np.allclose(G * mask, np.where(D == 0, 0.0, 2.0)))
```

```text
fraction zeroed 0.500, mean before 0.4999, after 0.5007
backward = G * mask: True
```

There are two complementary views of why dropout regularizes. As an ensemble: a network with $n$ droppable units contains $2^n$ subnetworks that share weights, each training step trains one of them on one example, and the test-time network approximates the geometric mean of their predictions (exactly so for a single **softmax** layer). As adaptive noise: for linear models, dropout is equivalent in expectation to a data-dependent $L^2$ penalty.

**Proposition 4.7.1** Let $\hat y = \frac{1}{1-p}\sum_{j=1}^n w_jr_jx_j$ with independent $r_j \sim \mathrm{Ber}(1 - p)$ (dropout on the inputs of a linear model). Then
$$
\mathbb{E}\bigl[(y - \hat y)^2\bigr] = \bigl(y - \boldsymbol{w}^{\mathsf T}\boldsymbol{x}\bigr)^2 + \frac{p}{1 - p}\sum_{j=1}^n w_j^2x_j^2 .
$$

**Proof** Since $\mathbb{E}[r_j] = 1 - p$, $\mathbb{E}[\hat y] = \boldsymbol{w}^{\mathsf T}\boldsymbol{x}$, and by independence $\operatorname{Var}(\hat y) = \frac{1}{(1-p)^2}\sum_j w_j^2x_j^2\operatorname{Var}(r_j) = \frac{p(1 - p)}{(1 - p)^2}\sum_j w_j^2x_j^2$. The claim is the decomposition $\mathbb{E}[(y - \hat y)^2] = (y - \mathbb{E}\hat y)^2 + \operatorname{Var}(\hat y)$. $\square$

Averaged over the training set, the penalty is $\frac{p}{1-p}\sum_j w_j^2\,\overline{x_j^2}$: a ridge penalty in which each weight is penalized in proportion to the second moment of its input feature (Wager, Wang and Liang 2013), so dropout regularizes rare features less than weight decay would. On MNIST, Srivastava et al. (2014) reduced the error of a standard **MLP** from 1.60% to 1.25% with dropout, and to 0.95% with dropout combined with max-norm constraints and wider layers; dropout in the fully connected layers was also one of the keys to AlexNet's success.

Dropout slows convergence (the gradient is noisier, and training typically takes two to three times as many steps) and interacts badly with batch normalization, whose statistics shift between training and inference when dropout precedes it. Its variants include DropConnect (dropping weights instead of units), spatial dropout (whole channels) and *stochastic depth* or DropPath (Huang et al. 2016), which drops entire residual blocks and is standard in training vision Transformers. Keeping dropout active at test time and averaging several stochastic forward passes (Monte Carlo dropout; Gal and Ghahramani 2016) gives an approximate Bayesian estimate of predictive uncertainty. In large language model pre-training, which usually makes a single pass over a huge dataset, **overfitting** is not the bottleneck and dropout is typically turned off; it remains common in fine-tuning on small datasets.

## 4.8. Choosing Hyperparameters in Practice

### 4.8.1. A Six-Step Recipe

A deep network has many **hyperparameters** ([4.7.1](/4.7.1)): the architecture (number of layers, width), the optimizer and its learning rate, momentum and **weight decay**, the schedule, the batch size, the dropout rate and the data augmentation. The architecture is best chosen by starting from models that are known to work on similar data and tasks, adapting them to the number of examples and the size and complexity of the inputs; the remaining **hyperparameters** can be found systematically. The following recipe is adapted from Stanford's CS231n course (Li, Johnson and Yeung 2019) and Google's *Deep Learning Tuning Playbook* (Godbole et al. 2023).

1. Check the initial loss. With weight decay off, the loss at initialization should match its theoretical value: for a $k$-class classifier with a **softmax function** output and small random weights the predictions are nearly uniform and the **cross-entropy loss** is about $\ln k$ ($2.30$ for ten classes). A different value indicates a bug in the loss or the initialization.
2. Overfit a small subset. Train on a few batches (say 100 examples) without **regularization** and reach 100% training accuracy. This verifies the whole pipeline from data loading to the output. If the loss does not decrease, the learning rate is too low, the initialization is poor or the model is too small; if it explodes to `inf` or `NaN`, the learning rate is too high or the initialization is poor.
3. Find a learning rate that makes the loss go down. On the full **training set**, with a small weight decay, try learning rates on a logarithmic grid (for **SGD** starting from $0.1$ and dividing by $10$; for Adam around $10^{-3}$) and keep those for which the loss drops significantly within the first hundred iterations.
4. Coarse grid, short runs. Train for 1–5 epochs over a few values around the learning rate and weight decay found in step 3 (weight decays such as $10^{-4}$, $10^{-5}$, $0$).
5. Refine the grid, train longer. Take the best settings and train for longer, around 10–20 epochs, without learning-rate decay.
6. Look at the loss curves, diagnose, and return to the appropriate step.

For more hyperparameters, random search on a logarithmic scale is more efficient than a grid ([4.7.1](/4.7.1) §1.4.3), and only one or two hyperparameters should be changed at a time when diagnosing a problem. For large models, hyperparameters are tuned on small proxy models and transferred, which works best with parameterizations designed for transfer such as μP ([4.7.2](/4.7.2) §2.7).

### 4.8.2. Reading Loss Curves

The training loss is noisy from batch to batch and is usually plotted as a running average; the validation loss and accuracy are evaluated periodically. Common patterns and their usual causes:

| Pattern | Likely cause | Action |
|---|---|---|
| loss flat for a long time, then drops suddenly | poor initialization (e.g. saturated units) | better initialization, normalization |
| loss decreases quickly and then plateaus at a high value | learning rate too high to settle | add learning-rate decay |
| loss plateaus early, far from good performance | stuck near a saddle point or in a poor region; model too small | higher learning rate, momentum, larger model |
| large gap between training and validation accuracy, validation loss rising | overfitting | more data or augmentation, stronger regularization, smaller model, early stopping |
| no gap, both accuracies still increasing | underfitting, training too short | train longer, larger model |
| loss spikes or `NaN` | learning rate too high, exploding gradients, bad data | lower learning rate, warmup, gradient clipping, inspect the batch |

Larger models overfit small datasets more easily; when the validation accuracy is still rising together with the training accuracy, the capacity can be increased. Finally, the curves of different runs should be compared at equal computation, not only at equal numbers of steps.

## Summary

- The loss of a neural network is non-convex and ill-conditioned; most problematic critical points are **saddle points**, and architecture (**skip connections**, normalization) shapes how smooth the landscape is. **Gradient descent** on a quadratic converges for $\eta < 2/\lambda_{\max}$ at a rate governed by the **condition number** $\kappa$.
- Momentum, $\boldsymbol{v}_t = \beta\boldsymbol{v}_{t-1} + \boldsymbol{g}_t$, damps oscillations and accumulates consistent directions, improving the rate on quadratics from $1 - 2/\kappa$ to $1 - 2/\sqrt\kappa$; Nesterov momentum evaluates the gradient at the look-ahead point and is optimal for smooth **convex functions**.
- AdaGrad, RMSProp and Adam scale each coordinate by the inverse root of its squared-gradient history. Adam combines this with momentum and corrects the initialization bias of both averages by $1/(1 - \beta^t)$; AdamW decouples **weight decay** from the adaptive scaling and is the default for Transformers. Lion uses the sign of a momentum, and Muon orthogonalizes the momentum of each weight matrix, steepest descent in the spectral norm.
- Learning rates are warmed up linearly (stabilizing Adam and large-batch training) and then decayed, by step, cosine or warmup-stable-decay schedules; the learning rate scales with the batch size up to a critical batch size.
- Gradients through many layers or time steps are products of Jacobians and vanish or explode exponentially; **ReLU**, initialization, residual connections, normalization and gating keep them stable, and gradient clipping by the global norm bounds the steps when they explode.
- Batch normalization standardizes each feature over the mini-batch (with running statistics at inference); layer normalization and RMSNorm normalize each example over its features and are used in RNNs and Transformers; instance and group normalization serve vision tasks with small batches.
- Dropout randomly zeroes units with probability $p$ and rescales the rest by $1/(1-p)$, training an implicit ensemble; for linear models it is a feature-scaled $L^2$ penalty. **Hyperparameters** are found by checking the initial loss, **overfitting** a small subset, finding a working learning rate and refining on coarse-to-fine grids while reading the loss curves.
