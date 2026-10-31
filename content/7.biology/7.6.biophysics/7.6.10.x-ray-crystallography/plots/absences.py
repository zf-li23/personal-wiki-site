# Systematic absences reveal screw axes.
# A: projection of a P2_1 crystal down the a axis: a chiral three-atom motif at (x, y, z) and its copy
#    at (-x, y + 1/2, -z), produced by the 2_1 screw axis along b (rotation by 180 deg plus half a cell
#    translation; axes lie at z = 0 and z = 1/2 of every cell); the copy is drawn with open symbols because it lies at -x (below the plane).
# B: intensities |F(0k0)|^2 along the b* axis computed for 30 random atoms (and their symmetry mates)
#    in P2_1 and in P2 (two-fold rotation axis, mate at (-x, y, -z)) with the same coordinates. In P2_1
#    all reflections 0k0 with k odd vanish exactly; in P2 they do not. The general reflections hkl are
#    not affected, so the two space groups have the same Laue symmetry 2/m and are distinguished only
#    by the absences.
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio
from wikibio import charts

P = bio.P
ink, muted = P.ink(), P.muted()
rng = np.random.default_rng(0)

fig, axs = plt.subplots(1, 2, figsize=(11.5, 4.2), gridspec_kw={"width_ratios": [1, 1.3]})
ax = axs[0]
motif = np.array([[0.10, 0.08, 0.15], [0.22, 0.10, 0.30], [0.17, 0.20, 0.38]])   # fractional x, y, z
cols = [charts.line("protein"), charts.line("dna"), charts.line("highlight")]
for i in range(-1, 3):
    for j in range(-1, 2):
        for (x, y, z), c in zip(motif, cols):
            ax.plot(z + i, y + j, "o", color=c, ms=7)
            ax.plot(-z + i, y + 0.5 + j, "o", mfc="none", mec=c, mew=1.5, ms=7)
for i in range(-1, 3):
    ax.axvline(i, color=muted, lw=0.6)
for j in range(-1, 3):
    ax.axhline(j, color=muted, lw=0.6)
for i in np.arange(-1, 2.6, 0.5):
    ax.plot([i, i], [-1.2, 2.2], color=charts.line("negative"), lw=1.6, ls=(0, (6, 2, 1, 2)))
ax.text(1.03, 1.85, r"$2_1$ axis along $\boldsymbol{b}$", fontsize=8, color=charts.line("negative"))
ax.plot([], [], "o", color=muted, ms=6, label=r"$(x, y, z)$")
ax.plot([], [], "o", mfc="none", mec=muted, ms=6, label=r"$(-x, y + \frac{1}{2}, -z)$")
ax.legend(fontsize=8, frameon=True, loc="lower left", framealpha=0.9)
ax.set_xlim(-0.6, 1.6)
ax.set_ylim(-0.6, 2.0)
ax.set_aspect("equal")
ax.set_title("A  P2$_1$ viewed along $\\boldsymbol{a}$", fontsize=9, loc="left", color=ink)
charts.style_axes(ax, "z (fraction of c)", "y (fraction of b)", box=True)

ax = axs[1]
xyz = rng.uniform(0, 1, size=(30, 3))
k = np.arange(1, 21)


def F0k0(mate_shift):
    F = np.exp(2j * np.pi * np.outer(k, xyz[:, 1])).sum(axis=1)
    F += np.exp(2j * np.pi * np.outer(k, xyz[:, 1] + mate_shift)).sum(axis=1)
    return np.abs(F) ** 2 * np.exp(-0.05 * k**2 / 4)


I21, I2 = F0k0(0.5), F0k0(0.0)
ax.bar(k - 0.18, I2 / I2.max(), width=0.36, color=charts.line("neutral"), label="P2")
ax.bar(k + 0.18, I21 / I2.max(), width=0.36, color=charts.line("protein"), label=r"P2$_1$")
for kk in k[k % 2 == 1]:
    ax.text(kk + 0.18, 0.02, "×", ha="center", fontsize=8, color=charts.line("negative"))
ax.set_xticks(k)
ax.legend(fontsize=9, frameon=False)
ax.set_title("B  axial reflections 0k0", fontsize=9, loc="left", color=ink)
charts.style_axes(ax, "k", r"$|F(0k0)|^2$ (relative)")
fig.tight_layout()
