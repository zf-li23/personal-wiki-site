# Time scales of biomolecular motion (upper rows) and the magnetic-resonance methods that report on them
# (lower rows), on a common logarithmic axis. Ranges are approximate.
import matplotlib.pyplot as plt

import wikibio as bio
from wikibio import charts

P = bio.P
motions = (("bond vibration", -14, -12.5), ("methyl rotation, side-chain rotamers", -12, -10),
           ("loop motions (fast)", -11, -8), ("overall tumbling of a protein", -9.3, -7),
           ("aromatic ring flips, loop motions (slow)", -6, -2), ("enzyme catalysis, allostery, binding", -6, 0),
           ("local unfolding (opening of H-bonds)", -3, 3), ("global folding / unfolding", -3, 5))
methods = (("spin relaxation R₁, R₂, NOE (model-free S², τe)", -12, -8, "protein"),
           ("RDC (averages all motion up to ~ms)", -12, -3, "dna"),
           ("CPMG relaxation dispersion", -3.7, -2.3, "rna"),
           ("R₁ρ relaxation dispersion", -5, -2.3, "rna"),
           ("CEST", -2.5, -1.3, "enzyme"),
           ("lineshapes, ZZ exchange", -2, 0.5, "enzyme"),
           ("H/D exchange (NMR, MS)", 0, 7, "atp"),
           ("real-time NMR", 0.5, 5, "neutral"),
           ("cw-EPR lineshape of spin labels", -10.5, -6.5, "receptor"),
           ("DEER (frozen snapshot of the ensemble)", -13, 7, "dna2"))
fig, ax = plt.subplots(figsize=(11.0, 6.2))
nm, nme = len(motions), len(methods)
for k, (name, a, b) in enumerate(motions):
    y = nme + 1.5 + (nm - k)
    ax.barh(y, b - a, left=a, height=0.62, color=P.fill("neutral"), edgecolor=P.edge("neutral"), lw=0.8)
    ax.text(b + 0.15, y, name, va="center", fontsize=7.8, color=P.ink())
for k, (name, a, b, tok) in enumerate(methods):
    y = nme - k
    ax.barh(y, b - a, left=a, height=0.62, color=P.fill(tok), edgecolor=P.edge(tok), lw=0.8)
    ax.text(b + 0.15, y, name, va="center", fontsize=7.8, color=P.ink())
ax.axhline(nme + 1.0, color=P.muted(), lw=0.6, ls=":")
ax.text(-14.5, nme + 1.5 + nm + 0.9, "motions", fontsize=8.5, color=P.ink(), weight="bold")
ax.text(-14.5, nme + 0.55, "methods", fontsize=8.5, color=P.ink(), weight="bold")
ticks = list(range(-14, 9, 2))
ax.set_xticks(ticks)
ax.set_xticklabels([r"$10^{%d}$" % t for t in ticks], fontsize=7.5)
for t, lab in ((-12, "ps"), (-9, "ns"), (-6, "μs"), (-3, "ms"), (0, "s"), (3.56, "h")):
    ax.axvline(t, color=P.muted(), lw=0.4, ls=":")
    ax.text(t, nme + nm + 3.4, lab, ha="center", fontsize=7.5, color=P.muted())
ax.set_xlim(-14.6, 12.5)
ax.set_ylim(0.3, nme + nm + 3.8)
ax.set_yticks([])
charts.style_axes(ax, "time scale / s", None)
fig.tight_layout()
