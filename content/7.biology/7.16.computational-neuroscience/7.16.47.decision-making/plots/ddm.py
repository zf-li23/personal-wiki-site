"""The drift-diffusion model of two-alternative decisions.

dx = A dt + c dW, x(0) = 0, decision when x reaches +theta (correct, for A > 0) or -theta (error);
c = 1, theta = 1 (arbitrary units of evidence), time in s; Euler-Maruyama with dt = 1 ms.
A: 12 sample paths for A = 1 (blue: correct, red: error) and the bounds.
B: psychometric function, fraction correct against drift A: simulation (dots, 2000 trials per
   point) and the analytic result P_c = 1 / (1 + exp(-2 A theta / c^2)) (line, Eq. (47.3)).
C: mean decision time against A: simulation and DT = (theta / A) tanh(A theta / c^2) (line);
   the limit A -> 0 is theta^2 / c^2. Correct and error decision times have the same mean
   in this model (dots: correct, crosses: errors).
D: decision-time distributions for A = 1 (correct and errors, normalized by the total number of
   trials): right-skewed, with the same shape for correct and error responses.
"""
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio

P = bio.P
rng = np.random.default_rng(0)
c, th, dt = 1.0, 1.0, 0.001


def simulate(A, n, tmax=8.0):
    x = np.zeros(n)
    t_dec = np.full(n, np.nan)
    choice = np.zeros(n)
    alive = np.ones(n, bool)
    for k in range(int(tmax / dt)):
        if not alive.any():
            break
        x[alive] += A * dt + c * np.sqrt(dt) * rng.standard_normal(alive.sum())
        hit = alive & (np.abs(x) >= th)
        t_dec[hit] = (k + 1) * dt
        choice[hit] = np.sign(x[hit])
        alive &= ~hit
    return choice, t_dec


fig, axs = plt.subplots(1, 4, figsize=(15, 3.7))
ax = axs[0]
for i in range(12):
    x, xs = 0.0, [0.0]
    while abs(x) < th:
        x += 1.0 * dt + c * np.sqrt(dt) * rng.standard_normal()
        xs.append(x)
    ts = np.arange(len(xs)) * dt
    ax.plot(ts, np.clip(xs, -th, th), lw=1, color=P.edge("dna") if x > 0 else P.edge("negative"))
ax.axhline(th, color=P.ink(), lw=1.5)
ax.axhline(-th, color=P.ink(), lw=1.5)
ax.text(0.02, th + 0.08, "choice 1 (correct)", fontsize=8)
ax.text(0.02, -th - 0.25, "choice 2 (error)", fontsize=8)
ax.set_ylim(-1.4, 1.4)
ax.set_xlabel("Time / s")
ax.set_ylabel("Decision variable x")
ax.set_title("A  Accumulation to bound", loc="left", fontsize=10)

As = np.array([0.0, 0.25, 0.5, 1.0, 1.5, 2.0, 3.0])
pc, dtc, dte = [], [], []
for A in As:
    ch, td = simulate(A, 2000)
    pc.append(np.mean(ch > 0))
    dtc.append(np.nanmean(td[ch > 0]))
    dte.append(np.nanmean(td[ch < 0]) if np.any(ch < 0) else np.nan)
aa = np.linspace(0, 3.2, 200)
axs[1].plot(aa, 1 / (1 + np.exp(-2 * aa * th / c**2)), color=P.edge("dna"), lw=2, label="Theory")
axs[1].plot(As, pc, "o", color=P.edge("negative"), label="Simulation")
axs[1].set_xlabel("Drift A (evidence strength)")
axs[1].set_ylabel("Fraction correct")
axs[1].set_title("B  Psychometric function", loc="left", fontsize=10)
axs[1].legend(frameon=False, fontsize=8, loc="lower right")
dtheo = np.where(aa > 0, th / np.maximum(aa, 1e-9) * np.tanh(aa * th / c**2), th**2 / c**2)
axs[2].plot(aa, dtheo, color=P.edge("dna"), lw=2, label="Theory")
axs[2].plot(As, dtc, "o", color=P.edge("negative"), label="Correct")
axs[2].plot(As, dte, "x", color=P.edge("negative"), ms=7, label="Error")
axs[2].set_xlabel("Drift A")
axs[2].set_ylabel("Mean decision time / s")
axs[2].set_title("C  Chronometric function", loc="left", fontsize=10)
axs[2].legend(frameon=False, fontsize=8, loc="upper right")
ch, td = simulate(1.0, 6000)
bins = np.linspace(0, 3, 41)
w = np.ones(np.sum(ch > 0)) / len(ch) / (bins[1] - bins[0])
axs[3].hist(td[ch > 0], bins, weights=w, color=P.fill("dna"), edgecolor=P.edge("dna"), lw=0.5, label="Correct")
w = np.ones(np.sum(ch < 0)) / len(ch) / (bins[1] - bins[0])
axs[3].hist(td[ch < 0], bins, weights=w, color=P.fill("negative"), edgecolor=P.edge("negative"), lw=0.5, label="Error")
axs[3].set_xlabel("Decision time / s")
axs[3].set_ylabel("Density")
axs[3].set_title("D  Decision-time distributions", loc="left", fontsize=10)
axs[3].legend(frameon=False, fontsize=8)
for a in axs:
    a.grid(True, alpha=0.3)
fig.tight_layout()
