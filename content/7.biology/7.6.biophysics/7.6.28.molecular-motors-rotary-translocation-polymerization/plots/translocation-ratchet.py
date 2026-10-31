# The translocation ratchet (Simon, Peskin and Oster 1992). A polymer diffuses (coefficient D) through a pore;
# binding sites spaced d apart are trapped by chaperones on the far side. Units: d = 1, D = 1, kBT = 1; w = F d/kBT
# for a load F opposing translocation.
# A: velocity against load. Perfect ratchet (irreversible, instantaneous binding): v = (D/d) w^2/(e^w - w - 1)
# (Theorem 28.5.1), with Brownian-dynamics points (2000 walkers, reflecting wall at the last bound site,
# reset at x = d). Rapid reversible binding with c/K_d = 100, 10 and 1: drift in the tilted staircase
# potential F x - kBT ln(1 + c/K_d) floor(x/d) (exact formula for a tilted periodic potential); the stall force is
# kBT ln(1 + c/K_d)/d. B: mean time to translocate n sites: free diffusion (n^2 d^2/2D) against the perfect
# ratchet (n d^2/2D).
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio
from wikibio import charts

P = bio.P
rng = np.random.default_rng(0)


def v_perfect(w):
    w = np.asarray(w, float)
    out = np.full_like(w, 2.0)
    m = np.abs(w) > 1e-6
    out[m] = w[m] ** 2 / (np.exp(w[m]) - w[m] - 1)
    return out


def v_reversible(w, G, n=300):
    x = (np.arange(n) + 0.5) / n
    X, Y = np.meshgrid(x, x, indexing="ij")
    dV = w * Y - G * (np.floor(X + Y) - np.floor(X))
    return (1 - np.exp(-(G - w))) / np.exp(dV).mean()


def bd(w, n=2000, T=30.0, dt=1e-3):
    x = np.zeros(n)
    steps = np.zeros(n)
    sq = np.sqrt(2 * dt)
    for _ in range(int(T / dt)):
        x += -w * dt + sq * rng.standard_normal(n)
        x = np.abs(x)  # reflecting wall: the last bound chaperone cannot pass the pore
        hit = x >= 1.0
        steps[hit] += 1
        x[hit] -= 1.0
    return steps.mean() / T


fig, axs = plt.subplots(1, 2, figsize=(11, 4.0))
ax = axs[0]
w = np.linspace(-1, 8, 300)
ax.plot(w, v_perfect(w), color=charts.line("protein"), lw=2.0, label="perfect ratchet")
for cK, tok in ((100, "enzyme"), (10, "dna"), (1, "rna")):
    G = np.log(1 + cK)
    ax.plot(w, [v_reversible(x, G) for x in w], color=charts.line(tok), lw=1.5, label=f"reversible, $c/K_\\mathrm{{d}}$ = {cK:g}")
    ax.plot(G, 0, "|", color=charts.line(tok), ms=10, mew=1.5)
wp = np.array([0.0, 1.0, 2.5, 4.0])
ax.plot(wp, [bd(x) for x in wp], "o", color=charts.line("protein"), ms=5, label="Brownian dynamics")
ax.axhline(0, color=P.muted(), lw=0.6)
ax.set_ylim(-1, 3.2); ax.set_xlim(-1, 8)
ax.legend(fontsize=7.5, frameon=False, loc="upper right")
charts.style_axes(ax, "load $w = Fd/k_\\mathrm{B}T$", "velocity / ($D/d$)")
charts.title(ax, "A   Force–velocity of a translocation ratchet")

ax = axs[1]
n = np.logspace(0, 3, 50)
ax.loglog(n, n**2 / 2, color=charts.line("neutral"), lw=1.8, label="free diffusion, $n^2d^2/2D$")
ax.loglog(n, n / 2, color=charts.line("protein"), lw=1.8, label="perfect ratchet, $nd^2/2D$")
ax.text(30, 40, "speed-up $n$", fontsize=8, color=P.ink())
ax.legend(fontsize=7.5, frameon=False, loc="upper left")
charts.style_axes(ax, "number of binding sites $n$", "translocation time / ($d^2/D$)")
charts.title(ax, "B   Ratcheting turns $n^2$ into $n$")
fig.tight_layout()
