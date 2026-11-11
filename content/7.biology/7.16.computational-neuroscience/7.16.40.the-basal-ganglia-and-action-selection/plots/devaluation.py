"""Goal-directed versus habitual control: an arbitration model of outcome devaluation (after Daw, Niv and Dayan 2005).

A rat presses a lever for food. Model-free (habit) value Q_MF is a cached value learned by TD and does not
change when the food is devalued unless the devalued outcome is experienced again. The model-based (goal-directed)
value Q_MB is computed from the current value of the outcome (0 after devaluation).
Arbitration: weight on the habit system w(n) = n / (n + n_half), n = number of training sessions, n_half = 6,
modeling the growing reliability of cached values. Response rate in the extinction test = 20 * (w Q_MF + (1 - w) Q_MB) / min.
A: weight w against training. B: test response rates, valued versus devalued outcome, after 2 or 20 sessions.
"""
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio

P = bio.P
n_half = 6.0
n = np.linspace(0, 30, 200)
fig, axs = plt.subplots(1, 2, figsize=(10, 3.6))
axs[0].plot(n, n / (n + n_half), color=P.edge("negative"), lw=2.2, label="habit (model-free) weight $w$")
axs[0].plot(n, n_half / (n + n_half), color=P.edge("dna"), lw=2.2, label="goal-directed weight $1 - w$")
axs[0].set_xlabel("Training sessions")
axs[0].set_ylabel("Weight in control")
axs[0].set_ylim(0, 1)
axs[0].set_title("A  Arbitration shifts with training", loc="left", fontsize=10)
axs[0].legend(frameon=False, fontsize=8)
rates = []
for s in (2, 20):
    w = s / (s + n_half)
    rates.append([20 * (w * 1 + (1 - w) * 1), 20 * (w * 1 + (1 - w) * 0)])
x = np.array([0, 1])
axs[1].bar(x - 0.18, [r[0] for r in rates], 0.36, color=P.fill("positive"), edgecolor=P.edge("positive"), label="valued outcome")
axs[1].bar(x + 0.18, [r[1] for r in rates], 0.36, color=P.fill("negative"), edgecolor=P.edge("negative"), label="devalued outcome")
axs[1].set_xticks(x)
axs[1].set_xticklabels(["limited training\n(2 sessions)", "extended training\n(20 sessions)"])
axs[1].set_ylabel("Lever presses / min (test)")
axs[1].set_ylim(0, 25)
axs[1].set_title("B  Devaluation sensitivity", loc="left", fontsize=10)
axs[1].legend(frameon=False, fontsize=8, loc="upper left")
for a in axs:
    a.grid(True, alpha=0.3)
fig.tight_layout()
