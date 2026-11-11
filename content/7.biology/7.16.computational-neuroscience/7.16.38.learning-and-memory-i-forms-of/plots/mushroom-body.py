"""Aversive olfactory conditioning in a mushroom body model with a dopamine-gated three-factor rule.

500 Kenyon cells (KCs); each odor activates a random 5% of them (odor A' shares half of A's KCs, B is unrelated).
Two output neurons: an approach MBON (M+) and an avoidance MBON (M-), output = sum of w_i over active KCs / 25.
Initial weights 1. Training: odor A paired with punishment; a punishment-signaling dopamine neuron innervating
the M+ compartment depresses the synapses of active KCs: w_i <- w_i (1 - eta) for active i, eta = 0.3.
Preference toward an odor = tanh(2 (M+ - M-)) (positive = approach, negative = avoidance).
A: preference for A, A' and B over 8 training trials. B: MBON responses to each odor after training.
"""
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio

P = bio.P
rng = np.random.default_rng(0)
N, k, eta = 500, 25, 0.3


def code(base=None, overlap=0):
    x = np.zeros(N, bool)
    if base is None:
        x[rng.choice(N, k, replace=False)] = True
        return x
    keep = rng.choice(np.where(base)[0], overlap, replace=False)
    x[keep] = True
    rest = rng.choice(np.where(~base)[0], k - overlap, replace=False)
    x[rest] = True
    return x


A = code()
A2 = code(A, overlap=k // 2)
B = code()
odors = [("odor A (trained)", A, "negative"), ("odor A' (similar)", A2, "highlight"), ("odor B (novel)", B, "dna")]
w_plus = np.ones(N)
w_minus = np.ones(N)


def mbon(x):
    return w_plus[x].sum() / k, w_minus[x].sum() / k


def pref(x):
    mp, mm = mbon(x)
    return np.tanh(2 * (mp - mm))


n_trials = 8
hist = {name: [pref(x)] for name, x, _ in odors}
for trial in range(n_trials):
    w_plus[A] *= 1 - eta
    for name, x, _ in odors:
        hist[name].append(pref(x))

fig, axs = plt.subplots(1, 2, figsize=(10, 3.6), gridspec_kw=dict(width_ratios=[1.4, 1]))
for name, x, tok in odors:
    axs[0].plot(range(n_trials + 1), hist[name], "o-", color=P.edge(tok), ms=4, lw=1.8, label=name)
axs[0].axhline(0, color=P.muted(), lw=0.8)
axs[0].set_xlabel("Training trial (odor A + punishment)")
axs[0].set_ylabel("Preference (approach > 0)")
axs[0].set_ylim(-1.05, 0.3)
axs[0].set_title("A  Learning and generalization", loc="left", fontsize=10)
axs[0].legend(frameon=False, fontsize=8, loc="lower left")
xs = np.arange(3)
mp = [mbon(x)[0] for _, x, _ in odors]
mm = [mbon(x)[1] for _, x, _ in odors]
axs[1].bar(xs - 0.18, mp, 0.36, color=P.fill("positive"), edgecolor=P.edge("positive"), label="approach MBON")
axs[1].bar(xs + 0.18, mm, 0.36, color=P.fill("negative"), edgecolor=P.edge("negative"), label="avoidance MBON")
axs[1].set_xticks(xs)
axs[1].set_xticklabels(["A", "A'", "B"])
axs[1].set_ylabel("MBON response (rel.)")
axs[1].set_ylim(0, 1.3)
axs[1].set_title("B  Output after training", loc="left", fontsize=10)
axs[1].legend(frameon=False, fontsize=8, loc="upper center", ncol=2)
for a in axs:
    a.grid(True, alpha=0.3)
fig.tight_layout()
