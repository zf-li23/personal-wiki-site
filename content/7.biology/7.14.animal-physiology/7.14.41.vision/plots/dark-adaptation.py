"""Dark adaptation after a bleach: rod-cone break from pigment regeneration (schematic model).

Pigment regeneration is rate limited by delivery of 11-cis retinal (Lamb and Pugh 2004):
  dB/dt = -v B / (K_m + B),   B = bleached fraction,  K_m = 0.2,
  v = 0.09 per min for rods, v = 0.5 per min for cones.
Threshold elevation follows the Dowling-Rushton relation, log10(T / T_abs) = k B,
  k = 20 for rods, k = 3 for cones; the absolute cone threshold lies 2.5 log units above the rod one.
Psychophysical threshold = the lower of the two branches.
A: threshold curves after bleaches of 98 %, 60 % and 20 %, plus a rod monochromat-like case
(cones only) for comparison. B: the bleached fractions for the 98 % bleach.
"""
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio

P = bio.P
Km = 0.2
t = np.linspace(0, 40, 4001)
dt = t[1] - t[0]


def regen(B0, v):
    B = np.empty_like(t)
    b = B0
    for i in range(len(t)):
        B[i] = b
        b = max(b - dt * v * b / (Km + b), 0.0)
    return B


fig, (ax, bx) = plt.subplots(1, 2, figsize=(11.5, 4.3), gridspec_kw={"width_ratios": [1.5, 1]})
cols = [P.edge("rna"), P.edge("enzyme"), P.edge("dna")]
for B0, c in zip((0.98, 0.6, 0.2), cols):
    Br, Bc = regen(B0, 0.09), regen(B0, 0.5)
    rod = 20 * Br
    cone = 2.5 + 3 * Bc
    thr = np.minimum(rod, cone)
    ax.plot(t, thr, color=c, lw=2.2, label=f"bleach {int(B0 * 100)} %")
    k = np.argmax(rod < cone)
    if k > 0:
        ax.plot(t[k], thr[k], "o", color=c, ms=5)
    if B0 == 0.98:
        ax.plot(t, cone, color=c, lw=1, ls=":")
        ax.plot(t, np.where(rod < 7, rod, np.nan), color=c, lw=1, ls=":")
        ax.annotate("rod-cone break", (t[k], thr[k]), (t[k] + 4, thr[k] + 1.6), fontsize=8,
                    color=P.ink(), arrowprops=dict(arrowstyle="-", color=P.muted(), lw=0.8))
        ax.text(3.2, 3.6, "cone branch", fontsize=8, color=P.muted())
        ax.text(23, 1.3, "rod branch", fontsize=8, color=P.muted())
ax.axhline(2.5, color=P.muted(), lw=0.6, ls="--")
ax.text(40, 2.55, "cone absolute threshold", fontsize=7.5, color=P.muted(), ha="right",
        va="bottom")
ax.axhline(0, color=P.muted(), lw=0.6, ls="--")
ax.text(40, 0.05, "rod absolute threshold", fontsize=7.5, color=P.muted(), ha="right",
        va="bottom")
ax.set_xlim(0, 40)
ax.set_ylim(-0.3, 7)
ax.set_xlabel("Time in the dark / min")
ax.set_ylabel(r"log$_{10}$ threshold (relative to rod absolute threshold)")
ax.legend(frameon=False, fontsize=8, loc="upper right")
ax.set_title("A  Two branches of the dark-adaptation curve", loc="left", fontsize=10)

Br, Bc = regen(0.98, 0.09), regen(0.98, 0.5)
bx.plot(t, Br, color=P.edge("rna"), lw=2, label="rods")
bx.plot(t, Bc, color=P.edge("dna"), lw=2, label="cones")
bx.set_xlim(0, 40)
bx.set_ylim(0, 1.02)
bx.set_xlabel("Time in the dark / min")
bx.set_ylabel("Bleached fraction of pigment B")
bx.text(8, 0.55, "nearly linear while B >> K$_m$\n(supply of 11-cis retinal limits)", fontsize=8,
        color=P.muted())
bx.legend(frameon=False, fontsize=8)
bx.set_title("B  Pigment regeneration", loc="left", fontsize=10)
fig.tight_layout()
