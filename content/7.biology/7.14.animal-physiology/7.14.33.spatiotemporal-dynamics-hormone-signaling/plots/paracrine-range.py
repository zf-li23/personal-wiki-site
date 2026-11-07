# Range of a paracrine signal: steady diffusion with first-order removal, lambda = sqrt(D / k).
# A: profiles C(x)/C0 = exp(-x / lambda) from a planar source (an endothelial layer) for NO in tissue
#    (D = 3300 um^2/s; k = 1 and 10 /s, i.e. half-lives of 0.7 s and 70 ms), for NO in blood, where
#    haemoglobin scavenges it (k ~ 1000 /s), and for a small peptide such as somatostatin
#    (D ~ 150 um^2/s, k = 0.01 /s). Shaded: endothelium to the outer media of an arteriole (~0-20 um)
#    and the radius of a pancreatic islet (~50-100 um).
# B: lambda against the removal half-life for the two diffusion coefficients.
import numpy as np

import wikibio as bio
from wikibio import charts

P = bio.P
fig, ax = bio.canvas(24.0, 9.6)

bio.panel(ax, "A", (0.2, 9.5))
pa = charts.axes_at(ax, (2.2, 1.5, 9.0, 6.9))
x = np.linspace(0, 300, 600)
cases = [
    (3300.0, 1000.0, "NO in blood (Hb), λ ≈ 2 µm", "negative", ":"),
    (3300.0, 10.0, "NO, k = 10 /s, λ ≈ 18 µm", "rna", "--"),
    (3300.0, 1.0, "NO, k = 1 /s, λ ≈ 57 µm", "rna", "-"),
    (150.0, 0.01, "peptide, k = 0.01 /s, λ ≈ 120 µm", "dna", "-"),
]
for D, k, lab, tok, ls in cases:
    lam = np.sqrt(D / k)
    pa.plot(x, np.exp(-x / lam), color=charts.line(tok), lw=1.7, ls=ls, label=lab)
pa.axvspan(0, 20, color=P.mix(charts.line("muscle"), P.surface(), 0.78), lw=0, zorder=0)
pa.axvspan(50, 100, color=P.mix(P.muted(), P.surface(), 0.8), lw=0, zorder=0)
pa.text(10, 1.02, "vessel\nwall", fontsize=6.8, color=P.muted(), ha="center", va="bottom")
pa.text(75, 1.02, "islet\nradius", fontsize=6.8, color=P.muted(), ha="center", va="bottom")
leg = pa.legend(loc="upper right", fontsize=7.0, frameon=False)
for txt in leg.get_texts():
    txt.set_color(P.ink())
pa.set_xlim(0, 300)
pa.set_ylim(0, 1.15)
charts.style_axes(pa, "distance from source / µm", "C / C0")
charts.title(pa, "Removal confines a paracrine signal")

bio.panel(ax, "B", (12.6, 9.5))
pb = charts.axes_at(ax, (14.6, 1.5, 8.8, 6.9))
th = np.logspace(-3, 3, 200)  # half-life / s
for D, tok, lab in ((3300.0, "rna", "D = 3300 µm²/s (NO, O₂)"), (150.0, "dna", "D = 150 µm²/s (small peptide)")):
    lam = np.sqrt(D * th / np.log(2))
    pb.loglog(th, lam, color=charts.line(tok), lw=1.8, label=lab)
for y, lab in ((10, "one cell"), (100, "islet / tissue unit"), (1000, "1 mm")):
    pb.axhline(y, color=P.mix(P.muted(), P.surface(), 0.55), lw=0.6, zorder=0)
    pb.text(1.2e-3, y * 1.08, lab, fontsize=6.8, color=P.muted(), ha="left", va="bottom")
leg = pb.legend(loc="lower right", fontsize=7.2, frameon=False)
for txt in leg.get_texts():
    txt.set_color(P.ink())
pb.set_xlim(1e-3, 1e3)
pb.set_ylim(0.3, 5e3)
charts.style_axes(pb, "removal half-life / s", "decay length λ / µm")
charts.title(pb, "λ = √(D/k) grows with the square root of lifetime")
