# Velocity versus equilibrium (isopycnic) sedimentation, simulated as band positions in a tube.
# The sedimentation velocity is v = s omega^2 x with s proportional to (rho_p - rho_m(x)) (buoyancy).
# A, velocity: a shallow 5-20% sucrose gradient (rho_m 1.02-1.08 g/mL), much less dense than the
#    particles, so s is nearly constant and bands move at rates set by size and shape; the run is stopped
#    before the fastest band reaches the bottom. Three particles of the same density with s = 30, 60, 120 S
#    (scaled units).
# B, equilibrium: a steep gradient (rho_m 1.10-1.28 g/mL across the tube) in which each particle slows as it
#    approaches the depth where rho_m = rho_p and stops there, whatever its size. Illustrative buoyant
#    densities in sucrose: ER microsomes 1.15, mitochondria 1.18, lysosomes 1.21, peroxisomes 1.23 g/mL;
#    each density is shown for a small and a large particle (dashed and solid), which arrive at different
#    times but at the same place.
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio
from wikibio import charts

P = bio.P
x0, x1 = 6.0, 10.0  # cm from the axis: top and bottom of the liquid


def run(s0, rho_p, rho_top, rho_bot, T, n=2000):
    t = np.linspace(0, T, n)
    x = np.empty(n)
    x[0] = x0
    for i in range(n - 1):
        rho_m = rho_top + (rho_bot - rho_top) * (x[i] - x0) / (x1 - x0)
        v = s0 * (rho_p - rho_m) / (rho_p - 1.0) * x[i]
        x[i + 1] = min(x1, x[i] + v * (t[1] - t[0]))
    return t, x


fig, axs = plt.subplots(1, 2, figsize=(11.0, 3.9))
ax = axs[0]
for s0, tok in ((0.003, "protein"), (0.006, "rrna"), (0.012, "mitochondrion")):
    t, x = run(s0, 1.30, 1.02, 1.08, 40)
    ax.plot(t, x, color=charts.line(tok), lw=1.8, label=f"s = {s0 * 1e4:.0f} (relative)")
ax.axvline(30, color=P.muted(), lw=0.8, ls=":")
ax.text(30.5, 6.15, "stop run;\ncollect fractions", fontsize=7, color=P.muted())
ax.set_ylim(x1 + 0.1, x0 - 0.1)
ax.set_xlim(0, 40)
ax.legend(fontsize=7, frameon=False, loc="lower left")
charts.style_axes(ax, "time (arbitrary units)", "position in tube / cm from axis")
ax.set_title("A   Velocity: separation by size and shape", loc="left", fontsize=9, color=P.ink())

ax = axs[1]
for rho, txt, tok in ((1.15, "ER microsomes", "er"), (1.18, "mitochondria", "mitochondrion"),
                      (1.21, "lysosomes", "lysosome"), (1.23, "peroxisomes", "peroxisome")):
    for s0, ls in ((0.035, "--"), (0.1, "-")):
        t, x = run(s0, rho, 1.10, 1.28, 60)
        ax.plot(t, x, color=charts.line(tok), lw=1.6, ls=ls)
    xe = x0 + (rho - 1.10) / (1.28 - 1.10) * (x1 - x0)
    ax.text(61, xe, f"{txt}\nρ = {rho:.2f} g/mL", fontsize=6.8, color=P.ink(), va="center")
ax.set_ylim(x1 + 0.1, x0 - 0.1)
ax.set_xlim(0, 80)
ax.set_xticks([0, 20, 40, 60])
charts.style_axes(ax, "time (arbitrary units)", "position in tube / cm from axis")
ax.set_title("B   Equilibrium: separation by buoyant density", loc="left", fontsize=9, color=P.ink())
fig.tight_layout()
