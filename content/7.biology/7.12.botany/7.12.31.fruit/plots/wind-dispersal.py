"""Terminal velocity model of wind dispersal. A: v_t = sqrt(2 (mg/S) / (rho C_D)) against wing loading mg/S
(log-log, slope 1/2) for three drag coefficients; shaded bands mark the rough order of magnitude of
descent speeds of plumed fruits, winged fruits and seeds without appendages. B: mean horizontal
distance x = H u / v_t for release height H = 10 m and wind speed u = 3 m/s.
"""
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio

P = bio.P
rho, H, u = 1.2, 10.0, 3.0
fig, (a, b) = plt.subplots(1, 2, figsize=(10.5, 4.2))
W = np.logspace(-2, 1.5, 200)  # wing loading, N m^-2
cols = [P.edge("dna"), P.edge("plant"), P.edge("rna")]
for cd, col in zip((0.6, 1.0, 1.6), cols):
    v = np.sqrt(2 * W / (rho * cd))
    a.loglog(W, v, color=col, lw=2, label=f"$C_D$ = {cd}")
    b.loglog(W, H * u / v, color=col, lw=2, label=f"$C_D$ = {cd}")
for lo, hi, txt in ((0.2, 0.5, "plumes"), (0.6, 1.5, "wings"), (2.0, 5.0, "no appendage")):
    a.axhspan(lo, hi, facecolor=P.fill("neutral"), alpha=0.22, lw=0, zorder=0)
    a.text(0.012, np.sqrt(lo * hi), txt, va="center", fontsize=8, color=P.ink())
a.set_xlabel("Wing loading $mg/S$ / N m$^{-2}$")
a.set_ylabel("Terminal velocity $v_t$ / m s$^{-1}$")
a.set_title("A  Descent speed", loc="left", fontsize=10)
b.set_xlabel("Wing loading $mg/S$ / N m$^{-2}$")
b.set_ylabel("Mean distance $x$ / m")
b.set_title(f"B  Distance, H = {H:.0f} m, u = {u:.0f} m/s", loc="left", fontsize=10)
a.legend(frameon=False, fontsize=8, loc="lower right")
b.legend(frameon=False, fontsize=8)
for ax in (a, b):
    ax.grid(True, which="major", alpha=0.3)
fig.tight_layout()
