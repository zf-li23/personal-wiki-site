# An energy ladder for the cell at T = 310 K, in units of the thermal energy kBT (logarithmic axis),
# with the same energies in kJ/mol and eV on secondary axes (kBT = 4.28 pN nm = 26.7 meV, RT = 2.58 kJ/mol).
# Ranges are typical: a van der Waals contact, a hydrogen bond or salt bridge in water, one elementary charge
# moved across a membrane at 70 mV, one proton through ATP synthase at 200 mV, the work of one kinesin step
# (6 pN x 8 nm), ATP hydrolysis under cellular conditions, the binding of a specific transcription factor,
# the stability of a folded protein, a visible photon (700 to 400 nm), and a C-C and a C=C covalent bond.
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio
from wikibio import charts

P = bio.P
KT_J = 1.380649e-23 * 310          # J
KT_EV = KT_J / 1.602176634e-19      # eV
RT_KJ = 8.314462618 * 310 / 1000    # kJ/mol

hc = 6.62607015e-34 * 2.99792458e8
items = [
    ("van der Waals contact", 0.5, 1.5, "neutral"),
    ("H-bond / salt bridge in water", 1.0, 5.0, "neutral"),
    ("charge across membrane (70 mV)", 70e-3 / KT_EV, 70e-3 / KT_EV, "na"),
    ("proton through ATP synthase", 0.2 / KT_EV, 0.2 / KT_EV, "h"),
    ("kinesin step (6 pN × 8 nm)", 48 / 4.28, 48 / 4.28, "protein"),
    ("folded protein stability", 5, 25, "protein"),
    ("ATP hydrolysis in the cell", 18, 25, "atp"),
    ("specific protein–DNA binding", 15, 30, "dna"),
    ("visible photon", hc / 700e-9 / KT_J, hc / 400e-9 / KT_J, "highlight"),
    ("C–C covalent bond", 346 / RT_KJ, 346 / RT_KJ, "negative"),
    ("C=C covalent bond", 614 / RT_KJ, 614 / RT_KJ, "negative"),
]

fig, ax = plt.subplots(figsize=(9.5, 4.6))
for i, (name, lo, hi, tok) in enumerate(items):
    y = len(items) - 1 - i
    if hi / lo > 1.05:
        ax.plot([lo, hi], [y, y], color=charts.line(tok), lw=6, solid_capstyle="round")
    else:
        ax.plot([lo], [y], "o", color=charts.line(tok), ms=8)
    ax.text(hi * 1.25, y, name, va="center", fontsize=7.5, color=P.ink())
ax.axvline(1, color=P.muted(), lw=0.8, ls=(0, (3, 3)))
ax.text(1.05, len(items) - 0.4, "thermal energy kBT", fontsize=7, color=P.muted())
ax.set_xscale("log")
ax.set_xlim(0.2, 3000)
ax.set_ylim(-1.5, len(items) - 0.1)
ax.set_yticks([])
charts.style_axes(ax, "E / kBT  (T = 310 K)")
ax.spines["left"].set_visible(False)

ax.set_xticks([1, 10, 100, 1000])
ax.set_xticklabels(["1", "10", "100", "1000"])
top = ax.secondary_xaxis("top", functions=(lambda e: e * RT_KJ, lambda q: q / RT_KJ))
top.set_xlabel("E / (kJ mol⁻¹)", fontsize=8, color=P.ink())
top.set_xticks([1, 10, 100, 1000, 3000])
top.set_xticklabels(["1", "10", "100", "1000", "3000"])
top.tick_params(colors=P.muted(), labelcolor=P.ink(), labelsize=6.8)
top.spines["top"].set_color(P.muted())

# eV scale as a second row of labels below the axis
for ev in (0.01, 0.1, 1, 10):
    e = ev / KT_EV
    ax.plot([e, e], [-1.5, -1.25], color=P.muted(), lw=0.8)
    ax.text(e * 1.08, -1.3, f"{ev:g} eV", ha="left", va="bottom", fontsize=6.8, color=P.muted())
fig.tight_layout()
