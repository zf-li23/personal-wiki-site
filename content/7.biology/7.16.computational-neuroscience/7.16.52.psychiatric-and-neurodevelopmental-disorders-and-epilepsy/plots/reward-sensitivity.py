"""Anhedonia in a reinforcement-learning model: reduced reward sensitivity versus reduced learning rate.

Two-armed bandit, 300 trials: the rich option pays 1 with probability 0.75, the lean option with
probability 0.25. Values are learned with the delta rule q <- q + alpha (rho r - q) (rho: reward
sensitivity, alpha: learning rate) and choices follow a softmax with inverse temperature beta = 5.
Probability of choosing the rich option, averaged over 2000 simulated subjects.
A: reduced reward sensitivity rho (alpha = 0.1): the asymptotic preference falls.
B: reduced learning rate alpha (rho = 1): learning slows but reaches a similar asymptote.
This dissociation is how model fits separate the two accounts (Huys et al. 2013).
"""
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio

P = bio.P
rng = np.random.default_rng(5)
ntr, nsub, beta = 300, 2000, 5.0
pay = np.array([0.75, 0.25])


def sim(rho, alpha):
    q = np.zeros((nsub, 2))
    pr = np.empty(ntr)
    for t in range(ntr):
        p_rich = 1 / (1 + np.exp(-beta * (q[:, 0] - q[:, 1])))
        c = (rng.random(nsub) > p_rich).astype(int)
        r = (rng.random(nsub) < pay[c]).astype(float)
        idx = np.arange(nsub)
        q[idx, c] += alpha * (rho * r - q[idx, c])
        pr[t] = p_rich.mean()
    return pr


def smooth(v, w=9):
    return np.convolve(v, np.ones(w) / w, mode="same")


tr = np.arange(1, ntr + 1)
fig, axs = plt.subplots(1, 2, figsize=(10.5, 3.9), sharey=True)
for rho, col in ((1.0, P.edge("dna")), (0.5, P.edge("protein")), (0.25, P.edge("negative"))):
    axs[0].plot(tr, smooth(sim(rho, 0.1)), color=col, lw=1.8, label=f"$\\rho$ = {rho:g}")
for alpha, col in ((0.1, P.edge("dna")), (0.03, P.edge("protein")), (0.01, P.edge("negative"))):
    axs[1].plot(tr, smooth(sim(1.0, alpha)), color=col, lw=1.8, label=f"$\\alpha$ = {alpha:g}")
axs[0].set_title("A  Reduced reward sensitivity ($\\alpha$ = 0.1)", loc="left", fontsize=10)
axs[1].set_title("B  Reduced learning rate ($\\rho$ = 1)", loc="left", fontsize=10)
axs[0].set_ylabel("P(choose rich option)")
for ax in axs:
    ax.axhline(0.5, color=P.muted(), lw=0.8, ls=":")
    ax.set_xlabel("Trial")
    ax.set_xlim(5, ntr - 5)
    ax.legend(frameon=False, fontsize=8, loc="lower right")
    ax.grid(True, alpha=0.3)
fig.tight_layout()
