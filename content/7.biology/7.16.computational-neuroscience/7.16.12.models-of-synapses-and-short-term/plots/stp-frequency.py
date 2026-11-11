"""Steady-state transmission through depressing and facilitating synapses (Tsodyks-Markram model).

For a regular presynaptic train at rate r (interval D = 1/r) the steady-state values just after a
spike are u+ = U / (1 - (1 - U) exp(-D/tau_f)) and, just before a spike,
x- = (1 - exp(-D/tau_d)) / (1 - (1 - u+) exp(-D/tau_d)).
A: efficacy per spike u+ x- (normalized to the first spike of a depressing synapse).
B: transmitted rate r u+ x- (released resources per second): the depressing synapse saturates at
1/tau_d (dashed), so its output no longer reports the rate itself. Parameters as in the train figure.
"""
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio

P = bio.P
r = np.logspace(-0.5, 2.2, 300)  # Hz
D = 1000.0 / r


def ss(U, td, tf):
    up = U / (1 - (1 - U) * np.exp(-D / tf))
    xm = (1 - np.exp(-D / td)) / (1 - (1 - up) * np.exp(-D / td))
    return up * xm


dep = ss(0.5, 800.0, 20.0)
fac = ss(0.1, 200.0, 1500.0)
fig, axs = plt.subplots(1, 2, figsize=(10.5, 3.9))
ax = axs[0]
ax.semilogx(r, dep / 0.5, color=P.edge("negative"), lw=2.2, label="depressing")
ax.semilogx(r, fac / 0.5, color=P.edge("dna"), lw=2.2, label="facilitating")
ax.set_xlabel("Presynaptic rate / Hz")
ax.set_ylabel("Steady-state efficacy per spike")
ax.set_title("A  Efficacy per spike", loc="left", fontsize=10)
ax.legend(frameon=False, fontsize=8)
ax = axs[1]
ax.loglog(r, r * dep, color=P.edge("negative"), lw=2.2, label="depressing")
ax.loglog(r, r * fac, color=P.edge("dna"), lw=2.2, label="facilitating")
ax.axhline(1000 / 800.0, color=P.edge("negative"), lw=1.0, ls="--")
ax.text(0.4, 1.4, "$1/\\tau_{\\mathrm{d}}$", fontsize=8, color=P.edge("negative"))
ax.set_xlabel("Presynaptic rate / Hz")
ax.set_ylabel("Transmitted rate r u x / s$^{-1}$")
ax.set_title("B  Transmitted rate saturates", loc="left", fontsize=10)
ax.legend(frameon=False, fontsize=8, loc="lower right")
for a in axs:
    a.grid(True, alpha=0.3, which="both")
fig.tight_layout()
