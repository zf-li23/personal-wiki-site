"""Radiation efficiency of small sound sources in air (c = 343 m/s).

A: (ka)^2 / (1 + (ka)^2) for a pulsating sphere of radius a, against frequency, for four radii; dashed lines at
ka = 1. B: frequency at which ka = 1 against source radius, with rough call-frequency ranges of some groups.
"""
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio

P = bio.P
c = 343.0
fig, (a, b) = plt.subplots(1, 2, figsize=(10.5, 3.9))
f = np.logspace(1, 5, 400)
for r, tok, lab in ((0.002, "rna", "2 mm"), (0.01, "positive", "1 cm"), (0.05, "dna", "5 cm"), (0.2, "neutral", "20 cm")):
    ka = 2 * np.pi * f / c * r
    a.semilogx(f, ka ** 2 / (1 + ka ** 2), color=P.edge(tok), lw=1.8, label=f"radius {lab}")
    a.axvline(c / (2 * np.pi * r), color=P.edge(tok), ls="--", lw=0.8)
a.set_xlabel("Frequency / Hz")
a.set_ylabel("Radiation efficiency")
a.set_ylim(0, 1.02)
a.legend(frameon=False, fontsize=8, loc="upper left")
a.set_title("A", loc="left", fontweight="bold")

rad = np.logspace(-3.3, 0, 200)
b.loglog(rad * 100, c / (2 * np.pi * rad), color=P.ink(), lw=1.8)
b.text(25, 600, "ka = 1", fontsize=8)
groups = [("katydids", 0.15, 0.6, 1e4, 4e4, "rna"), ("crickets", 0.3, 1.0, 3e3, 5e3, "positive"),
          ("songbirds", 0.8, 3.0, 2e3, 8e3, "dna"), ("frogs", 0.5, 6.0, 2e2, 4e3, "protein"),
          ("elephants", 20, 60, 10, 200, "neutral")]
for name, x0, x1, f0, f1, tok in groups:
    b.fill_between([x0, x1], f0, f1, color=P.light(tok), alpha=0.85, lw=0)
    b.text(np.sqrt(x0 * x1), np.sqrt(f0 * f1), name, ha="center", va="center", fontsize=7.5, color=P.ink())
b.set_xlabel("Source radius / cm (bars: rough size of sound-radiating structure)")
b.set_ylabel("Frequency / Hz")
b.set_xlim(0.05, 100); b.set_ylim(5, 1e5)
b.text(0.07, 12, "inefficient:\nsource small\nrelative to wavelength", fontsize=7.5, color=P.muted())
b.set_title("B", loc="left", fontweight="bold")
for ax in (a, b):
    for sp in ("top", "right"):
        ax.spines[sp].set_visible(False)
fig.tight_layout()
