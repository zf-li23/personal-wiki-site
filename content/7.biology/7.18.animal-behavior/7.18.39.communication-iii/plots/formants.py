"""Formants of a uniform tube closed at one end (vocal tract model): F_i = (2i - 1) c / (4 L), c = 350 m/s.

A: first five formants for tract lengths of 35, 50 and 70 cm. B: formant dispersion c / (2 L) against length.
"""
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio

P = bio.P
c = 350.0
fig, (a, b) = plt.subplots(1, 2, figsize=(10.5, 3.8), gridspec_kw={"width_ratios": [1.1, 1]})
for k, (L, tok) in enumerate(((0.35, "rna"), (0.50, "positive"), (0.70, "dna"))):
    F = [(2 * i - 1) * c / (4 * L) for i in range(1, 6)]
    for i, f in enumerate(F):
        a.plot([k - 0.3, k + 0.3], [f, f], color=P.edge(tok), lw=2.4)
        if k == 2:
            a.text(k + 0.36, f, f"F{i + 1}", va="center", fontsize=7.5, color=P.muted())
    a.text(k, -180, f"L = {L * 100:.0f} cm\nΔF = {c / (2 * L):.0f} Hz", ha="center", va="top", fontsize=8)
a.set_xlim(-0.6, 2.7); a.set_ylim(0, 2300)
a.set_xticks([])
a.set_ylabel("Formant frequency / Hz")
a.set_title("A", loc="left", fontweight="bold")
a.spines["bottom"].set_visible(False)

L = np.linspace(0.2, 0.9, 200)
b.plot(L * 100, c / (2 * L), color=P.ink(), lw=1.8)
b.axvspan(30, 40, color=P.light("rna"), alpha=0.7, lw=0)
b.axvspan(55, 75, color=P.light("dna"), alpha=0.7, lw=0)
b.text(35, 900, "larynx\nat rest", ha="center", fontsize=8)
b.text(65, 900, "larynx\nretracted\n(roar)", ha="center", fontsize=8)
b.annotate("limit set by\nneck and body size", (75, c / 1.5), (78, 520), fontsize=7.5, color=P.muted(),
           arrowprops=dict(arrowstyle="-", color=P.muted(), lw=0.8))
b.set_xlabel("Vocal tract length L / cm")
b.set_ylabel("Formant dispersion ΔF / Hz")
b.set_ylim(150, 950)
b.set_title("B", loc="left", fontweight="bold")
for ax in (a, b):
    for sp in ("top", "right"):
        ax.spines[sp].set_visible(False)
fig.tight_layout()
