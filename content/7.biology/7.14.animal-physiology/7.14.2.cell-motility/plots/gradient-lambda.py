# Chemoattractant gradients from a source-sink model.
# Steady state of D C'' - k C = 0 with a constant source at x = 0 and C -> 0 far away:
# C(x) = C0 exp(-x / lambda), lambda = sqrt(D / k).
# A: profiles for lambda = 30, 100 and 300 um (for D = 100 um^2/s these need degradation constants
#    k = D / lambda^2 = 0.11, 0.01 and 0.0011 s^-1). Shading: the window 0.1 Kd < C < 10 Kd in which receptors
#    (Kd = 1 nM, source concentration C0 = 30 nM) can read a gradient.
# B: relative concentration difference across a cell of length L = 10 um, dC/C = 1 - exp(-L / lambda),
#    which for an exponential profile is the same everywhere. Amoeboid cells (neutrophils,
#    Dictyostelium) read about 1-2 %, fibroblasts need about 30 %.
import numpy as np

import wikibio as bio
from wikibio import charts

P = bio.P
fig, ax = bio.canvas(24.0, 9.4)
C0, KD, L = 30.0, 1.0, 10.0

bio.panel(ax, "A", (0.2, 9.3))
pa = charts.axes_at(ax, (2.2, 1.5, 8.8, 6.7))
x = np.linspace(0, 1000, 500)
pa.axhspan(0.1 * KD, 10 * KD, color=P.mix(P.muted(), P.surface(), 0.85), lw=0)
pa.text(990, 0.13, "readable window 0.1–10 Kd", fontsize=7.5, color=P.ink(), ha="right")
for lam, tok in ((30, "rna"), (100, "protein"), (300, "dna")):
    pa.semilogy(x, C0 * np.exp(-x / lam), color=charts.line(tok), lw=1.7, label=f"λ = {lam} µm")
leg = pa.legend(loc="upper right", fontsize=7.5, frameon=False)
for txt in leg.get_texts():
    txt.set_color(P.ink())
pa.set_xlim(0, 1000)
pa.set_ylim(1e-3, 60)
charts.style_axes(pa, "distance from source x / µm", "concentration / nM")
charts.title(pa, "C(x) = C₀ exp(−x/λ)")

bio.panel(ax, "B", (12.6, 9.3))
pb = charts.axes_at(ax, (14.6, 1.5, 8.8, 6.7))
lam = np.logspace(0.5, 4, 300)
pb.loglog(lam, 100 * (1 - np.exp(-L / lam)), color=charts.line("dna"), lw=1.8)
for val, lab, tok in ((1.5, "amoeboid cells ≈ 1–2 %", "positive"), (30, "fibroblasts ≈ 30 %", "negative")):
    pb.axhline(val, color=charts.line(tok), lw=0.9, ls="--")
    pb.text(9000, val * 1.12, lab, fontsize=7.5, color=charts.line(tok), ha="right")
pb.set_xlim(10 ** 0.5, 1e4)
pb.set_ylim(0.08, 100)
charts.style_axes(pb, "decay length λ / µm", "front–rear difference ΔC/C / %")
charts.title(pb, "Across a 10 µm cell")
