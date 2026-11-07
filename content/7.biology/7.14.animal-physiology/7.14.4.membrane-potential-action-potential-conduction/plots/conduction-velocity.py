# Conduction velocity against axon diameter: two scaling laws and some measured fibres (log-log).
# Lines: unmyelinated axons, v ~ 2 m/s * sqrt(d / 1 um) (mammalian C fibres at 37 C; cooler animals lie
# lower, the squid giant axon at about 18 C falls near v ~ 1 m/s * sqrt(d / um)); myelinated vertebrate
# fibres, v ~ 6 m/s per um of outer diameter (Hursh's rule).
# Points (approximate literature values; temperature differs): mammalian fibre classes C, A-delta,
# A-beta and A-alpha; frog sciatic A fibres; squid giant axon; earthworm medial giant fibre; crayfish
# lateral giant; cockroach giant interneuron; the myelinated medial giant fibre of a penaeid shrimp.
import numpy as np

import wikibio as bio
from wikibio import charts

P = bio.P
fig, ax = bio.canvas(14.0, 9.6)
pa = charts.axes_at(ax, (2.3, 1.5, 11.0, 7.2))
d = np.logspace(-1, 3, 200)
pa.loglog(d, 2 * np.sqrt(d), color=charts.line("neutral"), lw=1.6, ls="--", label="unmyelinated: v ∝ √d")
dm = np.logspace(0, 1.5, 50)
pa.loglog(dm, 6 * dm, color=charts.line("dna"), lw=1.6, ls="--", label="myelinated (vertebrate): v ≈ 6 m/s per µm")
pts = [
    (1.0, 1.0, "C fibre (mammal)", "neutral", "o"),
    (3.0, 15, "Aδ", "dna", "o"),
    (9.0, 50, "Aβ", "dna", "o"),
    (15, 90, "Aα", "dna", "o"),
    (500, 25, "squid giant axon", "rna", "s"),
    (70, 30, "earthworm medial giant", "protein", "^"),
    (150, 15, "crayfish lateral giant", "protein", "v"),
    (45, 7, "cockroach giant interneuron", "highlight", "D"),
    (100, 200, "penaeid shrimp (myelinated)", "positive", "*"),
]
for x, y, lab, tok, m in pts:
    pa.loglog([x], [y], m, ms=7 if m != "*" else 11, color=charts.line(tok), mec=charts.line(tok))
    off = {"squid giant axon": (0.9, 1.35, "right"), "crayfish lateral giant": (1.15, 0.72, "left"),
           "earthworm medial giant": (0.9, 0.66, "right"), "cockroach giant interneuron": (0.85, 0.75, "right"),
           "penaeid shrimp (myelinated)": (0.8, 1.05, "right"), "C fibre (mammal)": (1.25, 0.8, "left")}.get(lab, (0.8, 1.15, "right"))
    pa.text(x * off[0], y * off[1], lab, fontsize=7.5, color=charts.line(tok), ha=off[2])
leg = pa.legend(loc="lower right", fontsize=7.5, frameon=False)
for txt in leg.get_texts():
    txt.set_color(P.ink())
pa.set_xlim(0.1, 2000)
pa.set_ylim(0.3, 400)
charts.style_axes(pa, "axon (or fibre) diameter d / µm", "conduction velocity / (m s⁻¹)")
charts.title(pa, "Two ways to conduct fast: be thick, or be myelinated")
