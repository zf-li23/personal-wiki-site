"""An approximate line attractor for a persistent aggressive state (after Nair et al. 2023).

Linear rate network of N = 50 units, tau dr/dt = -r + W r + b u(t), with W = Q diag(lam, l_2, ..., l_N) Q^T with orthogonal Q,
q the first column and l_k uniform in (0, 0.3). The mode along q has effective time constant tau / (1 - lam).
tau = 1 s; lam = 0.99 gives about 100 s ("integrator"); lam = 0.8 gives 5 s (control).
Input u(t): brief encounters with an intruder (2 s pulses). Readout x = q . r; attack probability
= logistic((x - 1.5) / 0.3). The input vector b has a component along q.
"""
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio

P = bio.P
rng = np.random.default_rng(0)
N, tau, dt = 50, 1.0, 0.05
Q, _ = np.linalg.qr(rng.normal(size=(N, N)))
q = Q[:, 0]
others = rng.uniform(0.0, 0.3, size=N - 1)
b = 0.6 * q + 0.4 * Q[:, 1:] @ rng.normal(size=N - 1) / np.sqrt(N)
t = np.arange(0, 300, dt)
u = np.zeros_like(t)
for t0 in (20, 50, 80):
    u[(t >= t0) & (t < t0 + 2)] = 1.0


def run(lam):
    W = Q @ np.diag(np.concatenate([[lam], others])) @ Q.T
    r = np.zeros(N)
    x = np.empty_like(t)
    for i in range(len(t)):
        r = r + dt / tau * (-r + W @ r + b * u[i])
        x[i] = q @ r
    return x


fig, axs = plt.subplots(2, 1, figsize=(8, 4.6), sharex=True, gridspec_kw=dict(height_ratios=[2, 1.2]))
for lam, tok, lab in [(0.99, "negative", "near-integrator ($\\lambda = 0.99$, $\\tau_{\\mathrm{eff}} = 100$ s)"),
                      (0.8, "dna", "control ($\\lambda = 0.8$, $\\tau_{\\mathrm{eff}} = 5$ s)")]:
    x = run(lam)
    axs[0].plot(t, x, color=P.edge(tok), lw=2, label=lab)
    axs[1].plot(t, 1 / (1 + np.exp(-(x - 1.5) / 0.3)), color=P.edge(tok), lw=2)
for t0 in (20, 50, 80):
    for ax in axs:
        ax.axvspan(t0, t0 + 2, color=P.light("highlight"), zorder=0)
axs[0].text(51, axs[0].get_ylim()[1] * 0.92, "encounters", fontsize=8.5, color=P.muted(), ha="center")
axs[0].set_ylabel("Activity along\nslow mode $x$")
axs[0].legend(frameon=False, fontsize=8, loc="upper right")
axs[1].set_ylabel("P(attack)")
axs[1].set_ylim(-0.03, 1.05)
axs[1].set_xlabel("Time / s")
for ax in axs:
    ax.grid(True, alpha=0.3)
fig.tight_layout()
