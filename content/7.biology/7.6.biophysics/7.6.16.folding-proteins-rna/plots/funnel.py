# The folding funnel in two pictures.
# A: a schematic rugged funnel as a surface over two conformational coordinates: the energy falls towards
#    the native state at the centre, superposed on random roughness (local traps); the radius stands for the
#    breadth of the conformational ensemble.
# B: a one-dimensional projection, the free energy F(Q) as a function of the fraction Q of native contacts,
#    in a mean-field (Bragg-Williams) model: each of N = 50 residues is native (energy -eps) or non-native
#    (entropy s0 = ln 4); partially folded chains pay an interfacial cost a Q (1 - Q); the mixing entropy of
#    choosing which residues are native is included. At the folding temperature T_f the unfolded (Q ~ 0.1)
#    and native (Q ~ 0.9) minima are equal and are separated by a barrier: two-state folding.
import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import argrelmin

import wikibio as bio
from wikibio import charts

P = bio.P
rng = np.random.default_rng(0)

fig = plt.figure(figsize=(12.5, 4.8))
ax3 = fig.add_subplot(1, 2, 1, projection="3d")
r = np.linspace(0, 1, 70)
th = np.linspace(0, 2 * np.pi, 120)
R, TH = np.meshgrid(r, th)
X, Y = R * np.cos(TH), R * np.sin(TH)
# smooth funnel plus random bumps and pits (local minima) that fade towards the native basin
bumps = np.zeros_like(R)
for _ in range(40):
    x0, y0 = rng.uniform(-1, 1, 2)
    if x0 * x0 + y0 * y0 > 1:
        continue
    bumps += rng.choice([-1, 1]) * rng.uniform(0.12, 0.3) * np.exp(-((X - x0) ** 2 + (Y - y0) ** 2) / 0.012)
Z = 1.9 * R**1.3 + bumps * np.clip(R / 0.3, 0, 1) - 0.8 * np.exp(-(R / 0.12) ** 2)
ax3.plot_surface(X, Y, Z, color=P.fill("protein"), edgecolor=P.mix(P.edge("protein"), P.surface(), 0.3), lw=0.15,
                 rstride=1, cstride=1, alpha=1.0, shade=True)
ax3.set_axis_off()
ax3.view_init(elev=24, azim=-58)
ax3.text(0, 0, -1.25, "native state", color=P.ink(), fontsize=8.5, ha="center")
ax3.text(1.05, -0.9, 2.7, "unfolded ensemble", color=P.ink(), fontsize=8.5)
ax3.text2D(0.02, 0.95, "A   A rugged folding funnel (schematic)", transform=ax3.transAxes, fontsize=9, weight="bold",
           color=P.ink())

ax = fig.add_subplot(1, 2, 2)
N, s0, a = 50, np.log(4.0), 3.0
Q = np.linspace(0.005, 0.995, 400)
mix = -(Q * np.log(Q) + (1 - Q) * np.log(1 - Q))


def F(Q, T, eps):
    return N * (-eps * Q - T * s0 * (1 - Q) + a * Q * (1 - Q) - T * mix)


T = 1.0
# the two minima are equal when the energy of a native residue balances the entropy of a non-native one
eps_f = s0 * T
for dT, tok, lab in ((-0.06, "dna", "T < T_f: native favoured"), (0.0, "neutral", "T = T_f"), (0.06, "rna", "T > T_f: unfolded favoured")):
    f = F(Q, T + dT, eps_f)
    ax.plot(Q, f - f.min(), color=charts.line(tok), lw=1.8, label=lab)
f = F(Q, T, eps_f)
m = argrelmin(f)[0]
top = m[0] + np.argmax(f[m[0]:m[-1]])
ax.annotate("", xy=(Q[top], f[top] - f.min()), xytext=(Q[top], f[m[0]] - f.min()),
            arrowprops=dict(arrowstyle="<->", color=P.muted(), lw=0.9))
ax.text(Q[top] + 0.02, (f[top] + f[m[0]]) / 2 - f.min(), f"ΔF‡ ≈ {f[top] - f[m[0]]:.1f} kT", fontsize=8, color=P.ink())
ax.text(Q[top] - 0.12, f[top] - f.min() + 1.1, "transition state", fontsize=7.5, color=P.muted(), ha="center")
ax.set_ylim(-0.5, 14)
charts.style_axes(ax, "fraction of native contacts Q", "F(Q) − F_min  /  kT")
ax.legend(fontsize=7.5, frameon=False, loc="upper center")
charts.title(ax, "B   Projection on Q: two minima and a barrier (N = 50)")
fig.tight_layout()
