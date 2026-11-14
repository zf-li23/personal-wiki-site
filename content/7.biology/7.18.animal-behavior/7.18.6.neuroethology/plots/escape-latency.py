"""Conduction time and the axon diameter needed for fast escape.

Unmyelinated: v = 1.1 sqrt(d) m/s (d in um; calibrated by the squid giant axon, 500 um, 25 m/s).
Myelinated: v = 6 d m/s (Hursh's rule, mammalian fibers at 37 C).
"""
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio

P = bio.P
d = np.logspace(0, 4, 300)  # um
vu = 1.1 * np.sqrt(d)
vm = 6.0 * d
L = 0.2
fig, (a, b) = plt.subplots(1, 2, figsize=(10, 3.9))
a.axhspan(0, 5, color=P.light("highlight"), zorder=0)
a.text(1.3, 3.2, "fast escape budget", fontsize=8, color=P.muted())
a.plot(d, L / vu * 1e3, color=P.edge("neuron"), lw=2, label="unmyelinated")
m = d <= 30
a.plot(d[m], L / vm[m] * 1e3, color=P.edge("dna"), lw=2, label="myelinated")
a.plot([500], [L / 25 * 1e3], "s", color=P.edge("negative"), ms=7)
a.annotate("squid giant axon", (500, 8), (40, 30), fontsize=8, color=P.ink(),
           arrowprops=dict(arrowstyle="-", color=P.muted(), lw=0.7))
a.set_xscale("log"); a.set_yscale("log")
a.set_xlim(1, 1e4); a.set_ylim(0.5, 300)
a.set_xlabel("Fiber diameter / µm"); a.set_ylabel("Conduction time over 0.2 m / ms")
a.set_title("A", loc="left", fontweight="bold")
a.legend(frameon=False, fontsize=8)
Ls = np.logspace(-2, 0, 200)
v_need = Ls / 2e-3
b.plot(Ls * 100, (v_need / 1.1) ** 2, color=P.edge("neuron"), lw=2, label="unmyelinated")
b.plot(Ls * 100, v_need / 6.0, color=P.edge("dna"), lw=2, label="myelinated")
b.axhline(1000, color=P.muted(), ls="--", lw=0.8)
b.text(1.1, 1300, "1 mm", fontsize=8, color=P.muted())
b.set_xscale("log"); b.set_yscale("log")
b.set_xlabel("Path length / cm"); b.set_ylabel("Diameter for 2 ms conduction / µm")
b.set_title("B", loc="left", fontweight="bold")
b.legend(frameon=False, fontsize=8)
for ax in (a, b):
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
fig.tight_layout()
