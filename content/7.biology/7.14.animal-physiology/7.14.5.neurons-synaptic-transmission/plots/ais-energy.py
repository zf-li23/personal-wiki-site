"""Why the axon initial segment (AIS) needs a diffusion barrier, and what the two defences cost.

A: time for a membrane protein to diffuse along a length L of axon, tau = L^2 / (2D), in free
membrane (D = 0.1 um^2/s) and inside the AIS, where the submembrane scaffold lowers the effective D
about 50-fold (D = 0.002 um^2/s). The dotted line marks an AIS 40 um long.
B: order-of-magnitude ATP budget (assumptions in the text): building the scaffold once costs
3.1e8 ATP (7.7e7 amino-acid residues x 4 ATP); keeping it costs residues x ln2/t_half x 4 ATP per
second (t_half = 5 d, band 2-10 d); clearing leaked dendritic proteins costs 0.031 molecules/s x
1500 ATP x 20 protein species = 940 ATP/s. Cumulative costs cross after about a week.
"""
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio

P = bio.P
fig, (ax, bx) = plt.subplots(1, 2, figsize=(11, 4.2))

L = np.logspace(0, 2.3, 200)
for D, name, tok in ((0.1, "free membrane, D = 0.1 $\\mu$m$^2$ s$^{-1}$", "neutral"),
                     (0.002, "AIS, D = 0.002 $\\mu$m$^2$ s$^{-1}$", "channel")):
    ax.loglog(L, L ** 2 / (2 * D) / 3600, color=P.edge(tok), lw=2, label=name)
ax.axvline(40, color=P.muted(), lw=1, ls=":")
for y, txt in ((40 ** 2 / 0.2 / 3600, "2.2 h"), (40 ** 2 / 0.004 / 3600, "4.6 d")):
    ax.plot([40], [y], "o", color=P.ink(), ms=5)
    ax.text(44, y, txt, fontsize=8.5, color=P.ink(), va="center")
ax.axhline(24, color=P.muted(), lw=0.8, ls="--")
ax.text(1.1, 27, "1 day", fontsize=8, color=P.muted())
ax.set_xlabel("Distance along the axon $L$ / $\\mu$m")
ax.set_ylabel("Diffusion time $L^2/2D$ / h")
ax.legend(frameon=False, fontsize=8, loc="upper left")
ax.set_title("A  Diffusion would erase polarity in hours", loc="left", fontsize=10)

days = np.linspace(0, 14, 400)
s = days * 86400
residues, build, clear = 7.7e7, 3.1e8, 940.0
def keep(th):
    return residues * np.log(2) / (th * 86400) * 4
bx.fill_between(days, (build + keep(10) * s) / 1e8, (build + keep(2) * s) / 1e8,
                color=P.fill("protein"), alpha=0.35, lw=0, label="scaffold, $t_{1/2}$ = 2-10 d")
bx.plot(days, (build + keep(5) * s) / 1e8, color=P.edge("protein"), lw=2, label="scaffold: build + upkeep ($t_{1/2}$ = 5 d)")
bx.plot(days, clear * s / 1e8, color=P.edge("enzyme"), lw=2, label="clearance of leaked proteins")
tx = build / (clear - keep(5)) / 86400
bx.plot([tx], [clear * tx * 86400 / 1e8], "o", color=P.ink(), ms=5)
bx.text(tx + 0.3, clear * tx * 86400 / 1e8 - 0.6, f"cross at {tx:.0f} d", fontsize=8.5, color=P.ink())
bx.set_xlim(0, 14)
bx.set_ylim(0, 13)
bx.set_xlabel("Time / d")
bx.set_ylabel("Cumulative ATP / $10^8$")
bx.legend(frameon=False, fontsize=8, loc="upper left")
bx.set_title("B  Two defences, comparable cost", loc="left", fontsize=10)
for x in (ax, bx):
    x.grid(True, alpha=0.3, which="both")
fig.tight_layout()
