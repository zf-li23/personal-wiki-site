"""Go/NoGo learning in the striatum: the probabilistic selection task (Frank, Seeberger and O'Reilly 2004)
simulated with an opponent actor-critic (after the OpAL model of Collins and Frank 2014).

Training pairs AB, CD, EF with reward probabilities 0.8/0.2, 0.7/0.3, 0.6/0.4 (reward 1, otherwise 0).
Critic (one value per pair): v <- v + 0.1 delta, delta = r - v.
For the chosen stimulus k: Go (D1) weight G_k <- G_k + a_G G_k delta,
                           NoGo (D2) weight N_k <- N_k - a_N N_k delta   (G, N start at 1).
Choice: logistic in the difference of G - N with beta = 2. 360 training trials, 500 simulated subjects.
Dopamine sets the learning asymmetry: normal a_G = a_N = 0.1; low dopamine a_G = 0.02, a_N = 0.2;
high dopamine a_G = 0.2, a_N = 0.02.
Test: 'choose A' = mean probability of choosing A over C, D, E, F; 'avoid B' = mean probability of choosing C..F over B.
"""
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio

P = bio.P
rng = np.random.default_rng(0)
pr = np.array([0.8, 0.2, 0.7, 0.3, 0.6, 0.4])
BETA = 2.0


def run(aG, aN, R=500, T=360):
    G = np.ones((R, 6))
    N = np.ones((R, 6))
    v = np.full((R, 3), 0.5)
    idx = np.arange(R)
    for _ in range(T):
        pair = rng.integers(0, 3, R)
        i, j = 2 * pair, 2 * pair + 1
        act = G - N
        p_i = 1 / (1 + np.exp(-BETA * (act[idx, i] - act[idx, j])))
        k = np.where(rng.random(R) < p_i, i, j)
        r = (rng.random(R) < pr[k]).astype(float)
        delta = r - v[idx, pair]
        v[idx, pair] += 0.1 * delta
        G[idx, k] += aG * G[idx, k] * delta
        N[idx, k] -= aN * N[idx, k] * delta
    act = G - N
    others = [2, 3, 4, 5]
    choose_a = np.mean([1 / (1 + np.exp(-BETA * (act[:, 0] - act[:, x]))) for x in others])
    avoid_b = np.mean([1 / (1 + np.exp(-BETA * (act[:, x] - act[:, 1]))) for x in others])
    return G.mean(axis=0), N.mean(axis=0), choose_a, avoid_b


conds = [("normal", 0.1, 0.1, "dna"), ("low dopamine", 0.02, 0.2, "neutral"), ("high dopamine", 0.2, 0.02, "negative")]
res = {name: run(aG, aN) for name, aG, aN, _ in conds}

fig, axs = plt.subplots(1, 2, figsize=(10, 3.6))
x = np.arange(4)
w = 0.26
for k, (name, _, _, tok) in enumerate(conds):
    G, N, _, _ = res[name]
    vals = [G[0], N[0], G[1], N[1]]
    axs[0].bar(x + (k - 1) * w, vals, w, color=P.fill(tok), edgecolor=P.edge(tok), label=name)
axs[0].axhline(1, color=P.muted(), lw=0.8, ls=":")
axs[0].set_xticks(x)
axs[0].set_xticklabels(["Go(A)", "NoGo(A)", "Go(B)", "NoGo(B)"])
axs[0].set_ylabel("Weight after training")
axs[0].set_title("A  Go and NoGo weights of A (80%) and B (20%)", loc="left", fontsize=10)
axs[0].legend(frameon=False, fontsize=8, loc="upper center", ncol=3)
axs[0].set_ylim(0, 2.9)
for k, (name, _, _, tok) in enumerate(conds):
    _, _, ca, ab = res[name]
    axs[1].bar(np.array([0, 1]) + (k - 1) * w, [ca, ab], w, color=P.fill(tok), edgecolor=P.edge(tok))
axs[1].axhline(0.5, color=P.muted(), lw=0.8, ls=":")
axs[1].set_xticks([0, 1])
axs[1].set_xticklabels(["choose A\n(learned from gains)", "avoid B\n(learned from losses)"])
axs[1].set_ylabel("Test accuracy")
axs[1].set_ylim(0.5, 0.9)
axs[1].set_title("B  Transfer test", loc="left", fontsize=10)
for a in axs:
    a.grid(True, alpha=0.3, axis="y")
fig.tight_layout()
