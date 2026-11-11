"""Learning to learn in Harlow's object-discrimination problems: a two-level (meta-learning) illustration.

Each problem: two novel objects, one rewarded (r = 1) and one not (r = 0), six trials; positions are irrelevant.
Inner loop (fast, within a problem): delta-rule values Q of the two objects, starting at 0.5,
  Q <- Q + alpha (r - Q) for the chosen object; choice = softmax with inverse temperature beta.
Outer loop (slow, across problems): evolution strategies on log alpha (beta fixed at 6), population 20,
  perturbation SD 0.15, step 0.02, fitness = mean reward over 6 trials, 200 problems per evaluation, 80 iterations.
Start: alpha = 0.05.
A: accuracy on trials 1-6 of a problem after 0, 12, 22 and 80 outer iterations.
B: trial-2 accuracy (one-shot learning) and the learned alpha across outer iterations.
"""
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio

P = bio.P
rng = np.random.default_rng(0)
N_TRIALS = 6


def accuracy(log_a, n=200, b=6.0):
    a = min(np.exp(log_a), 1.0)
    q = np.full((n, 2), 0.5)  # object 0 is the rewarded one
    acc = np.empty(N_TRIALS)
    for t in range(N_TRIALS):
        p0 = 1 / (1 + np.exp(-b * (q[:, 0] - q[:, 1])))
        c = (rng.random(n) >= p0).astype(int)
        r = (c == 0).astype(float)
        acc[t] = r.mean()
        q[np.arange(n), c] += a * (r - q[np.arange(n), c])
    return acc


theta = np.log(0.05)
hist, snaps = [], {}
for it in range(81):
    if it in (0, 12, 22, 80):
        snaps[it] = np.mean([accuracy(theta) for _ in range(5)], axis=0)
    hist.append((accuracy(theta, n=1000)[1], min(np.exp(theta), 1.0)))
    eps = rng.standard_normal(20)
    fit = np.array([accuracy(theta + 0.15 * e).mean() for e in eps])
    fit = (fit - fit.mean()) / (fit.std() + 1e-9)
    theta = min(theta + 0.02 / 0.15 * (fit @ eps) / 20, 0.0)

fig, axs = plt.subplots(1, 2, figsize=(10, 3.6))
toks = ["neutral", "lipid", "dna", "negative"]
for (it, acc), tok in zip(snaps.items(), toks):
    axs[0].plot(np.arange(1, N_TRIALS + 1), acc, "o-", color=P.edge(tok), lw=2, label=f"after {it} outer iterations")
axs[0].axhline(0.5, color=P.muted(), lw=0.8, ls=":")
axs[0].set_xlabel("Trial within a new problem")
axs[0].set_ylabel("Proportion correct")
axs[0].set_ylim(0.25, 1.02)
axs[0].set_title("A  Learning curves within a problem", loc="left", fontsize=10)
axs[0].legend(frameon=False, fontsize=8, loc="lower right")
h = np.array(hist)
axs[1].plot(h[:, 0], color=P.edge("negative"), lw=2, label="trial-2 accuracy")
axs[1].plot(h[:, 1], color=P.edge("dna"), lw=2, ls="--", label="inner learning rate $\\alpha$")
axs[1].set_xlabel("Outer-loop iteration (slow learning)")
axs[1].set_ylabel("Value")
axs[1].set_ylim(0, 1.02)
axs[1].set_title("B  The fast learner is shaped by slow learning", loc="left", fontsize=10)
axs[1].legend(frameon=False, fontsize=8, loc="lower right")
for a in axs:
    a.grid(True, alpha=0.3)
fig.tight_layout()
