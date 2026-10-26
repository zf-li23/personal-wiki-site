# The lever rule for a single scaffold that phase-separates (illustrative numbers: saturation concentration
# C_sat = 1 uM, dense-phase concentration C_den = 200 uM, both fixed at a given temperature and salt).
# A: concentration in the dilute phase (solid) and volume fraction of the condensed phase (right axis) against
#    the total concentration. Below C_sat the solution is homogeneous; above it the dilute phase stays at C_sat
#    and the excess goes into a growing volume of condensate, V_den / V = (c - C_sat) / (C_den - C_sat).
#    Dashed: a multicomponent scaffold whose dilute-phase concentration still rises above the threshold
#    (illustrative slope 0.3), as measured for nucleolar NPM1 in cells (Riback and colleagues, 2020): with
#    heterotypic interactions the tie lines are not parallel to the concentration axis of one component.
# B: buffering of cell-to-cell variation. Total concentrations drawn from a lognormal distribution (median
#    2 uM, coefficient of variation 0.4, 20000 cells); in each cell the dilute-phase concentration is
#    min(c, C_sat) for the ideal single-component case. The spread of the total is not transmitted to the
#    dilute phase, which is the prediction of noise buffering by phase separation (Klosin and colleagues, 2020).
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio
from wikibio import charts

P = bio.P
CSAT, CDEN = 1.0, 200.0

fig, axs = plt.subplots(1, 2, figsize=(10.4, 3.9), gridspec_kw={"width_ratios": [1.15, 1.0]})

ax = axs[0]
c = np.linspace(0, 5, 500)
dil = np.minimum(c, CSAT)
het = np.where(c < CSAT, c, CSAT + 0.3 * (c - CSAT))
vfrac = np.clip((c - CSAT) / (CDEN - CSAT), 0, None)
ax.plot(c, c, color=P.muted(), lw=1.0, ls=":", label="no phase separation")
ax.plot(c, dil, color=charts.line("protein"), lw=1.9, label="dilute phase (one component)")
ax.plot(c, het, color=charts.line("protein"), lw=1.3, ls=(0, (4, 2.4)), label="dilute phase (multicomponent)")
ax.axvline(CSAT, color=P.muted(), lw=0.7, ls=(0, (3, 2)))
ax.text(CSAT - 0.06, 4.55, "C_sat", ha="right", fontsize=7, color=P.muted())
ax.set_xlim(0, 5)
ax.set_ylim(0, 5)
charts.style_axes(ax, "total concentration c / µM", "dilute-phase concentration / µM")
ax.legend(fontsize=7, frameon=False, loc="upper left", bbox_to_anchor=(0.2, 1.0))
ax2 = ax.twinx()
ax2.plot(c, 100 * vfrac, color=charts.line("rna"), lw=1.9)
ax2.set_ylim(0, 2.5)
ax2.text(4.1, 100 * (4.1 - CSAT) / (CDEN - CSAT) + 0.12, "condensate\nvolume", fontsize=7,
         color=charts.line("rna"), ha="center", va="bottom")
for name, sp in ax2.spines.items():
    sp.set_visible(name == "right")
    sp.set_color(P.muted())
ax2.tick_params(colors=P.muted(), labelcolor=P.ink(), labelsize=7, width=0.7, length=3)
ax2.set_ylabel("condensed volume fraction / %", fontsize=8, color=P.ink())
ax.set_title("A   Lever rule: the dilute phase is clamped", loc="left", fontsize=9, color=P.ink())

ax = axs[1]
rng = np.random.default_rng(0)
cv = 0.4
s = np.sqrt(np.log(1 + cv ** 2))
tot = 2.0 * np.exp(rng.normal(0, s, 20000))
d = np.minimum(tot, CSAT)
bins = np.linspace(0, 6, 61)
h, _, _ = ax.hist(tot, bins=bins, color=P.fill("neutral"), edgecolor=P.edge("neutral"), lw=0.4, label="total")
ax.hist(d, bins=bins, color=P.fill("protein"), edgecolor=P.edge("protein"), lw=0.4, label="dilute phase")
top = 1.9 * h.max()
ax.set_ylim(0, top)
frac = np.mean(tot > CSAT)
ax.annotate(f"{100 * frac:.0f} % of cells at C_sat\n(bar clipped)", (1.05, top), (1.5, 0.82 * top), fontsize=7,
            color=P.ink(), arrowprops=dict(arrowstyle="-", color=P.muted(), lw=0.7))
cv_t = tot.std() / tot.mean()
cv_d = d.std() / d.mean()
ax.text(3.6, 0.45 * top, f"CV total = {cv_t:.2f}\nCV dilute = {cv_d:.2f}", fontsize=8, color=P.ink())
ax.set_xlim(0, 6)
ax.set_yticks([])
charts.style_axes(ax, "concentration / µM", "number of cells")
ax.legend(fontsize=7, frameon=False, loc="upper right")
ax.set_title("B   Buffering of cell-to-cell variation", loc="left", fontsize=9, color=P.ink())
fig.tight_layout()
