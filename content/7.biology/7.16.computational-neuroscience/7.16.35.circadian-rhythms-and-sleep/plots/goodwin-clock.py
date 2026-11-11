"""Goodwin-type transcription-translation feedback loop as a model of the circadian clock.

dM/dt = 1/(1 + P_n^h) - b M   (mRNA, repressed by nuclear protein P_n)
dP/dt = b (M - P)              (cytoplasmic protein)
dP_n/dt = b (P - P_n)          (nuclear protein)
Equal first-order rates b (per hour); Hill coefficient h. Oscillation requires h > 8 for equal rates
(secant condition); near onset the period is 2 pi / (sqrt(3) b), so b = 0.15 / h gives about 24 h.
A: time courses for b = 0.15 / h, h = 12. B: period against b for h = 10 and 16, with the onset formula.
"""
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio

P = bio.P


def rk4(b, h, T, dt=0.1, keep=None):
    """Integrate many (b, h) pairs at once with fixed-step RK4; return times and M for t >= keep."""
    b = np.asarray(b, float)
    h = np.asarray(h, float)
    y = np.full((3,) + b.shape, 0.5)

    def f(y):
        M, Pc, Pn = y
        return np.array([1.0 / (1.0 + Pn ** h) - b * M, b * (M - Pc), b * (Pc - Pn)])

    n = int(T / dt)
    start = int((keep if keep is not None else 0) / dt)
    out = np.empty((n - start,) + y.shape)
    for i in range(n):
        k1 = f(y)
        k2 = f(y + 0.5 * dt * k1)
        k3 = f(y + 0.5 * dt * k2)
        k4 = f(y + dt * k3)
        y = y + dt / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
        if i >= start:
            out[i - start] = y
    return np.arange(start, n) * dt, out


def periods(t, M):
    res = []
    for j in range(M.shape[1]):
        m = M[:, j]
        if m.max() - m.min() < 1e-3 * m.mean():
            res.append(np.nan)
            continue
        pk = np.where((m[1:-1] > m[:-2]) & (m[1:-1] > m[2:]))[0] + 1
        res.append(np.mean(np.diff(t[pk])) if len(pk) > 2 else np.nan)
    return np.array(res)


fig, axs = plt.subplots(1, 2, figsize=(10, 3.7))
t, Y = rk4(np.array([0.15]), np.array([12.0]), 600.0, keep=480.0)
M, Pc, Pn = Y[:, 0, 0], Y[:, 1, 0], Y[:, 2, 0]
t0 = t - t[0]
for y, lab, tok in [(M, "mRNA $M$", "rna"), (Pc, "cytoplasmic protein $P$", "protein"), (Pn, "nuclear repressor $P_{\\mathrm{n}}$", "negative")]:
    axs[0].plot(t0, y / y.max(), color=P.edge(tok), lw=2, label=lab)
axs[0].set_xlabel("Time / h")
axs[0].set_ylabel("Level (normalized to max)")
axs[0].set_title("A  Delayed negative feedback ($b = 0.15\\,\\mathrm{h^{-1}}$, $h = 12$)", loc="left", fontsize=10)
axs[0].set_xticks(np.arange(0, 121, 24))
axs[0].legend(frameon=False, fontsize=8, loc="lower left")
bs = np.linspace(0.06, 0.4, 18)
B, H = np.meshgrid(bs, [10.0, 16.0])
t, Y = rk4(B.ravel(), H.ravel(), 1400.0, dt=0.1, keep=900.0)
per = periods(t, Y[:, 0, :]).reshape(B.shape)
for row, (h, tok) in enumerate([(10, "dna"), (16, "negative")]):
    axs[1].plot(bs, per[row], "o-", color=P.edge(tok), ms=4, lw=1.6, label=f"Hill coefficient $h = {h}$")
bb = np.linspace(0.05, 0.42, 100)
axs[1].plot(bb, 2 * np.pi / (np.sqrt(3) * bb), color=P.muted(), ls="--", lw=1.2, label="onset: $2\\pi/(\\sqrt{3}\\,b)$")
axs[1].axhline(24, color=P.muted(), lw=0.8, ls=":")
axs[1].set_xlabel("Degradation rate $b$ / h$^{-1}$")
axs[1].set_ylabel("Period / h")
axs[1].set_ylim(0, 75)
axs[1].set_title("B  Faster turnover, shorter period", loc="left", fontsize=10)
axs[1].legend(frameon=False, fontsize=8)
for ax in axs:
    ax.grid(True, alpha=0.3)
fig.tight_layout()
