# The energy scale of molecular motors. A: stall force against step size per fuel molecule (log axes);
# diagonal lines are constant work per step F d = 1, 10 and 20 kBT (kBT = 4.1 pN nm); the free energy of
# one ATP in the cell (about 20 kBT, 80-100 pN nm) bounds every ATP-driven motor that takes one step per
# ATP. Values are representative single-molecule measurements (kinesin-1, yeast cytoplasmic dynein,
# myosin V, skeletal myosin II, E. coli RNA polymerase, the phi29 packaging motor; F1 as torque times
# 120 degrees). B: work at stall per fuel molecule, F_s d, as a fraction of 20 kBT.
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio
from wikibio import charts

P = bio.P
kT = 4.1
motors = [  # name, step / nm, stall force / pN, token
    ("kinesin-1", 8.2, 7.0, "enzyme"),
    ("dynein (yeast)", 8.0, 6.0, "protein"),
    ("myosin V", 36.0, 2.5, "myosin"),
    ("myosin II", 5.0, 4.0, "muscle"),
    ("RNA polymerase", 0.34, 25.0, "rna"),
    ("phi29 packaging motor", 0.85, 57.0, "virus"),
]
fig, axs = plt.subplots(1, 2, figsize=(11, 4.2), gridspec_kw={"width_ratios": [1.25, 1]})
ax = axs[0]
d = np.logspace(-1, 2, 50)
for W, lab, xl in ((1, "$Fd$ = 1 $k_\\mathrm{B}T$", 1.5), (10, "10 $k_\\mathrm{B}T$", 55), (20, "20 $k_\\mathrm{B}T$ (one ATP)", 12)):
    ax.loglog(d, W * kT / d, color=P.muted(), lw=0.9 if W < 20 else 1.6, ls="--" if W < 20 else "-")
    ax.text(xl, W * kT / xl * 1.25, lab, fontsize=7.5, color=P.muted(), rotation=-31, ha="left", va="bottom")
ax.fill_between(d, 20 * kT / d, 1e3, color=P.fill("negative"), alpha=0.25, lw=0)
ax.text(30, 60, "forbidden for\none step per ATP", fontsize=7.5, color=P.ink(), ha="center")
for name, dd, F, tok in motors:
    ax.plot(dd, F, "o", color=charts.line(tok), ms=7)
    off = {"myosin II": (1.15, 0.75), "dynein (yeast)": (1.15, 0.72), "kinesin-1": (1.15, 1.08)}.get(name, (1.15, 1.0))
    ax.text(dd * off[0], F * off[1], name.replace("phi29", "φ29"), fontsize=7.5, color=P.ink(), va="center")
ax.set_xlim(0.1, 100); ax.set_ylim(0.3, 300)
charts.style_axes(ax, "step per fuel molecule $d$ / nm", "stall force $F_\\mathrm{s}$ / pN")
charts.title(ax, "A   Force times step is bounded by one ATP")

ax = axs[1]
rows = [(n, dd * F) for n, dd, F, _ in motors if n != "myosin II"] + [("F₁ (40 pN nm × 2π/3)", 40 * 2 * np.pi / 3)]
toks = [t for n, _, _, t in motors if n != "myosin II"] + ["atp_synthase"]
y = np.arange(len(rows))[::-1]
ax.barh(y, [w / (20 * kT) for _, w in rows], color=[P.fill(t) for t in toks], edgecolor=[P.edge(t) for t in toks], lw=0.8)
for yy, (n, w) in zip(y, rows):
    ax.text(w / (20 * kT) + 0.02, yy, f"{w:.0f} pN nm", fontsize=7.5, color=P.ink(), va="center")
ax.set_yticks(y)
ax.set_yticklabels([n.replace("phi29", "φ29") for n, _ in rows])
ax.axvline(1, color=P.muted(), lw=0.9, ls="--")
ax.set_xlim(0, 1.35)
charts.style_axes(ax, "$F_\\mathrm{s}d$ / (20 $k_\\mathrm{B}T$)")
charts.title(ax, "B   Work at stall per fuel molecule")
fig.tight_layout()
