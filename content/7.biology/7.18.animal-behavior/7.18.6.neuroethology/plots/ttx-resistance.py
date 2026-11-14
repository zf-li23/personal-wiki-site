"""Target-site insensitivity to tetrodotoxin (illustrative values).

A: single-site block of Na+ current, I/I0 = 1 / (1 + [TTX]/Kd).
B: racetrack assay; relative crawl speed after a TTX dose D (mass-adjusted units, MAMU),
   s(D) = s0 / (1 + D/D50); resistance = D50.
"""
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio

P = bio.P
c = np.logspace(-10, -3, 300)  # mol/L
fig, (a, b) = plt.subplots(1, 2, figsize=(10, 3.8))
for kd, tok, lab in [(1e-8, "negative", "sensitive, Kd 10 nM"), (3e-7, "highlight", "moderately resistant, 300 nM"),
                     (1e-5, "positive", "highly resistant, 10 µM")]:
    a.plot(c, 1 / (1 + c / kd), color=P.edge(tok), lw=2, label=lab)
a.set_xscale("log")
a.set_xlabel("[TTX] / (mol L$^{-1}$)"); a.set_ylabel("Na$^+$ current remaining, $I/I_0$")
a.set_title("A", loc="left", fontweight="bold")
a.legend(frameon=False, fontsize=8, loc="lower left")
D = np.logspace(-1, 3, 300)
for s0, d50, tok, lab in [(1.0, 2.0, "negative", "population without toxic newts"),
                          (0.9, 200.0, "positive", "population with toxic newts")]:
    b.plot(D, s0 / (1 + D / d50), color=P.edge(tok), lw=2, label=lab)
    b.plot([d50, d50], [0, s0 / 2], color=P.edge(tok), ls="--", lw=0.9)
b.set_xscale("log"); b.set_ylim(0, 1.05)
b.set_xlabel("TTX dose (mass-adjusted units)"); b.set_ylabel("Crawl speed / untreated control")
b.set_title("B", loc="left", fontweight="bold")
b.legend(frameon=False, fontsize=8, loc="lower left")
for ax in (a, b):
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
fig.tight_layout()
