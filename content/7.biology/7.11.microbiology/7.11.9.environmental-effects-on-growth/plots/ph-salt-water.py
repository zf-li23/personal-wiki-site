# pH, salt and water activity.
# A: pH optima of example organisms (data from Madigan et al. 2019) on the pH scale, with the classes
#    acidophile (optimum below pH 5.5), neutrophile (5.5 to 7.9) and alkaliphile (8 or above). Whatever the
#    external pH, the cytoplasm is kept near neutrality (band, schematic: about pH 5 to 9 overall, usually 6.5
#    to 8).
# B: growth rate against NaCl concentration for the four salt classes (illustrative curves after the
#    classification): a nonhalophile such as Escherichia coli, a halotolerant organism such as Staphylococcus
#    aureus, a (marine) halophile such as Aliivibrio fischeri with an optimum near 3 %, and an extreme
#    halophile such as Halobacterium with an optimum of 15 to 30 %.
# C: water activity of common materials and the lowest water activity known to allow growth (data from
#    Madigan et al. 2019), with the water activity of NaCl solutions computed from their osmotic coefficients
#    (a_w = exp(-2 m phi M_w), phi from the Pitzer equation for NaCl at 25 C) for comparison: a saturated NaCl
#    solution (6.1 mol/kg) has a_w of about 0.75, the value of salt lakes and salted fish.
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio
from wikibio import charts

P = bio.P
fig, axs = plt.subplots(1, 3, figsize=(14.5, 4.3), gridspec_kw=dict(width_ratios=[1.2, 1.0, 1.15], wspace=0.38))

# ---- A: pH ------------------------------------------------------------------------------------------------
ax = axs[0]
orgs = [("Picrophilus oshimae", 0.7, "A"), ("Acidithiobacillus ferrooxidans", 3.0, "B"),
        ("Rhodopila globiformis", 5.0, "B"), ("Escherichia coli", 7.0, "B"),
        ("Chloroflexus aurantiacus", 8.0, "B"), ("Natronobacterium gregoryi", 10.0, "A")]
for x0, x1, name, tok in ((0, 5.5, "acidophiles", "negative"), (5.5, 8.0, "neutrophiles", "positive"),
                          (8.0, 12, "alkaliphiles", "dna")):
    ax.axvspan(x0, x1, color=P.mix(P.fill(tok), P.surface(), 0.8 if not P.is_dark() else 0.88), lw=0)
    ax.text((x0 + x1) / 2, 6.55, name, ha="center", fontsize=7.5, color=charts.line(tok), weight="bold")
for k, (name, ph, dom) in enumerate(orgs):
    y = 5.6 - k * 0.9
    ax.plot([ph], [y], "o", ms=5, color=P.ink())
    ax.text(ph + (0.25 if ph < 8 else -0.25), y + 0.28, name, fontsize=6.8, style="italic", color=P.ink(),
            ha="left" if ph < 8 else "right")
ax.axhspan(-0.6, 0.1, xmin=0, xmax=1, color="none")
ax.add_patch(plt.Rectangle((6.5, -0.55), 1.5, 0.45, facecolor=P.fill("cytoplasm"), edgecolor=P.edge("cytoplasm"), lw=0.8))
ax.text(7.25, -0.95, "internal pH of most cells", ha="center", fontsize=6.8, color=P.muted())
ax.set_xlim(0, 12)
ax.set_ylim(-1.3, 7.0)
ax.set_yticks([])
ax.set_xticks(range(0, 13, 2))
ax.spines["left"].set_visible(False)
charts.style_axes(ax, "pH optimum for growth", None)
ax.spines["left"].set_visible(False)
charts.title(ax, "A   pH classes")

# ---- B: salt ------------------------------------------------------------------------------------------------
ax = axs[1]
c = np.linspace(0, 30, 400)


def bell(x, lo, opt, hi):
    y = np.where(x <= opt, 1 - ((opt - x) / (opt - lo)) ** 2, 1 - ((x - opt) / (hi - opt)) ** 2)
    return np.where((x > lo) & (x < hi), np.clip(y, 0, None), np.nan)


curves = [("nonhalophile", np.where(c < 4, 1 - (c / 4) ** 2, np.nan), "positive", "Escherichia coli"),
          ("halotolerant", np.where(c < 15, np.where(c < 2, 1.0, 1 - (np.clip(c - 2, 0, None) / 13) ** 1.6), np.nan), "highlight",
           "Staphylococcus aureus"),
          ("halophile", bell(c, 0.4, 3.0, 12), "dna", "Aliivibrio fischeri"),
          ("extreme halophile", bell(c, 9, 20, 31), "negative", "Halobacterium")]
for name, y, tok, sp in curves:
    ax.plot(c, y, color=charts.line(tok), lw=2.0, label=name)
ax.set_xlim(0, 30)
ax.set_ylim(0, 1.25)
ax.set_yticks([0, 0.5, 1])
ax.legend(fontsize=6.8, frameon=False, loc="upper right", ncol=1)
charts.style_axes(ax, "NaCl / %", "growth rate (relative)")
charts.title(ax, "B   Salt classes")

# ---- C: water activity -------------------------------------------------------------------------------------------
ax = axs[2]
items = [(1.000, "pure water"), (0.980, "seawater"), (0.950, "bread"), (0.850, "salami"),
         (0.800, "fruit cake, jams"), (0.750, "salt lakes, salted fish"), (0.700, "cereals, candy, dried fruit"),
         (0.605, "lower limit for growth (xerophilic fungus)")]
for aw, name in items:
    ax.plot([0, 0.09], [aw, aw], color=P.muted(), lw=0.6)
    ax.plot([0.05], [aw], "s", ms=4.5, color=charts.line("dna"))
    ax.text(0.12, aw, f"{aw:.3f}  {name}", va="center", fontsize=6.8, color=P.ink())
# NaCl solutions: Pitzer osmotic coefficient
m = np.linspace(0, 6.1, 200)
A, b, beta0, beta1, Cphi = 0.392, 1.2, 0.0765, 0.2664, 0.00127
I = m
phi = 1 - A * np.sqrt(I) / (1 + b * np.sqrt(I)) + m * (beta0 + beta1 * np.exp(-2 * np.sqrt(I))) + m**2 * Cphi
aw_nacl = np.exp(-2 * m * phi * 0.018015)
ax2 = ax.inset_axes([1.08, 0.0, 0.32, 1.0], transform=ax.transAxes)
ax2.plot(m, aw_nacl, color=charts.line("negative"), lw=1.8)
ax2.set_ylim(0.58, 1.01)
ax2.set_yticks([])
charts.style_axes(ax2, "NaCl / (mol kg$^{-1}$)", None)
ax2.spines["left"].set_visible(False)
ax2.text(6.0, aw_nacl[-1] - 0.02, f"saturated:\n{aw_nacl[-1]:.2f}", ha="right", va="top", fontsize=6.8, color=charts.line("negative"))
ax.set_xlim(0, 1)
ax.set_ylim(0.58, 1.01)
ax.set_xticks([])
ax.spines["bottom"].set_visible(False)
charts.style_axes(ax, None, "water activity $a_{\\mathrm{w}}$")
ax.spines["bottom"].set_visible(False)
charts.title(ax, "C   Water activity")
