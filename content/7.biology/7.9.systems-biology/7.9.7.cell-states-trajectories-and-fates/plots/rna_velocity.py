"""RNA velocity of one gene (simulated). Unspliced (u) and spliced (s) mRNA follow du/dt = alpha - beta u,
ds/dt = beta u - gamma s with beta = 1 and gamma = 0.3 per hour; transcription is on (alpha = 2) for
10 h and then off. 600 cells are sampled at random times between 0 and 25 h, and their molecule counts
are Poisson with 6 molecules per unit of concentration. A: the phase portrait: the upper arc is induction,
the lower arc repression; the steady-state model fits the slope gamma/beta through the origin by least
squares on the cells in the top and bottom 5 % of both u and s (dashed line) and gives each cell the
velocity v = u - (gamma/beta) s (arrows: positive above the line, negative below). B: the same cells
against their true time. C: a failure: cells of two subpopulations whose degradation rates differ
(gamma = 0.3 and 0.9 per hour) share one fitted slope, and many cells of the fast-degrading
subpopulation receive a velocity of the wrong sign."""

import numpy as np
import matplotlib.pyplot as plt
import wikibio as bio
from wikibio import charts

P = bio.P
rng = np.random.default_rng(0)
alpha, beta, ts, c = 2.0, 1.0, 10.0, 6.0


def traj(t, gamma):
    """Analytic u(t), s(t) from u = s = 0, induction until ts, then repression."""
    def on(t):
        u = alpha / beta * (1 - np.exp(-beta * t))
        s = alpha / gamma * (1 - np.exp(-gamma * t)) + alpha / (gamma - beta) * (np.exp(-gamma * t) - np.exp(-beta * t))
        return u, s
    u0, s0 = on(np.minimum(t, ts))
    tau = np.maximum(t - ts, 0)
    u = u0 * np.exp(-beta * tau)
    s = s0 * np.exp(-gamma * tau) + beta * u0 / (gamma - beta) * (np.exp(-beta * tau) - np.exp(-gamma * tau))
    return u, s


def fit_slope(u, s, q=0.05):
    lo_u, hi_u = np.quantile(u, [q, 1 - q])
    lo_s, hi_s = np.quantile(s, [q, 1 - q])
    m = ((u <= lo_u) & (s <= lo_s)) | ((u >= hi_u) & (s >= hi_s))
    return (u[m] @ s[m]) / (s[m] @ s[m])


fig, axs = plt.subplots(1, 3, figsize=(12.6, 3.8))
fig.subplots_adjust(left=0.06, right=0.98, bottom=0.16, top=0.88, wspace=0.3)

gamma = 0.3
t = rng.uniform(0, 25, 600)
u, s = traj(t, gamma)
U = rng.poisson(c * u) / c
S = rng.poisson(c * s) / c
g_hat = fit_slope(U, S)
v = U - g_hat * S
v_true = beta * u - gamma * s
ok = np.mean(np.sign(v) == np.sign(v_true))
print("gamma_hat", round(g_hat, 3), "sign agreement", round(ok, 3))
tt = np.linspace(0, 25, 400)
uu, ss = traj(tt, gamma)
ax = axs[0]
ind = t < ts
ax.scatter(S[ind], U[ind], s=6, color=charts.line("rna"), lw=0, label="induction (t < 10 h)")
ax.scatter(S[~ind], U[~ind], s=6, color=charts.line("dna"), lw=0, label="repression (t > 10 h)")
ax.plot(ss, uu, color=P.ink(), lw=1.0)
xs = np.linspace(0, S.max() * 1.05, 10)
ax.plot(xs, g_hat * xs, "--", color=P.muted(), lw=1.0)
ax.text(xs[-1] * 0.8, g_hat * xs[-1] * 0.8 - 0.55, f"u = {g_hat:.3f} s", fontsize=7.5, color=P.ink())
sel = rng.choice(600, 45, replace=False)
ax.quiver(S[sel], U[sel], v[sel], np.zeros(45), angles="xy", scale_units="xy", scale=0.6,
          color=P.ink(), width=0.004)
ax.legend(frameon=False, fontsize=7.5, loc="upper left", markerscale=2.5)
charts.style_axes(ax, "spliced s", "unspliced u")
charts.title(ax, "A  Phase portrait and steady-state fit")

ax = axs[1]
o = np.argsort(t)
ax.scatter(t, U, s=4, color=charts.line("rna"), lw=0, alpha=0.6)
ax.scatter(t, S, s=4, color=charts.line("dna"), lw=0, alpha=0.6)
ax.plot(tt, uu, color=charts.line("rna"), lw=1.4, label="unspliced u")
ax.plot(tt, ss, color=charts.line("dna"), lw=1.4, label="spliced s")
ax.axvline(ts, color=P.muted(), lw=0.7, ls="--")
ax.text(ts + 0.3, 6.3, "transcription off", fontsize=7.5, color=P.ink())
ax.legend(frameon=False, fontsize=7.5, loc="upper right")
charts.style_axes(ax, "true time (h)", "molecules (scaled)")
charts.title(ax, "B  Kinetics in time")

ax = axs[2]
t2 = rng.uniform(0, 25, 600)
grp = rng.integers(0, 2, 600)
gam = np.where(grp == 0, 0.3, 0.9)
u2 = np.empty(600); s2 = np.empty(600)
for gv in (0.3, 0.9):
    m = gam == gv
    u2[m], s2[m] = traj(t2[m], gv)
U2 = rng.poisson(c * u2) / c
S2 = rng.poisson(c * s2) / c
g2 = fit_slope(U2, S2)
v2 = U2 - g2 * S2
vt2 = beta * u2 - gam * s2
wrong = np.sign(v2) != np.sign(vt2)
print("pooled gamma_hat", round(g2, 3), "wrong sign: slow", round(np.mean(wrong[grp == 0]), 3),
      "fast", round(np.mean(wrong[grp == 1]), 3))
for gv, tok, name in [(0.3, "dna", "gamma = 0.3 per h"), (0.9, "rna", "gamma = 0.9 per h")]:
    m = gam == gv
    ax.scatter(S2[m], U2[m], s=6, color=charts.line(tok), lw=0, label=name)
ax.scatter(S2[wrong], U2[wrong], s=14, facecolor="none", edgecolor=P.ink(), lw=0.5, label="wrong sign of v")
xs = np.linspace(0, S2.max() * 1.05, 10)
ax.plot(xs, g2 * xs, "--", color=P.muted(), lw=1.0)
ax.legend(frameon=False, fontsize=7.5, loc="upper right", markerscale=1.5)
charts.style_axes(ax, "spliced s", "unspliced u")
charts.title(ax, "C  Two kinetic regimes, one slope")
