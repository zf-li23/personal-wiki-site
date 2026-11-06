# Soil pH and the availability of mineral nutrients (schematic). The width of each band is proportional to the
# relative availability of the nutrient to roots, drawn after the classic diagrams of Truog (1946, mineral soils)
# and Lucas and Davis (1961, organic soils); the band shapes are qualitative, not measurements. Most nutrients are
# well available between pH 5.5 and 6.5 (shaded). Below about pH 5, Al3+ and Mn2+ become soluble enough to be toxic
# and phosphate is bound by Fe and Al; above about pH 7, Fe, Mn, Zn, Cu and B become less soluble and phosphate is
# precipitated with calcium; molybdenum, in contrast, becomes more available as pH rises.
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio
from wikibio import charts

P = bio.P
pH = np.linspace(4.0, 9.0, 400)


def bump(lo, hi, w_lo=0.5, w_hi=0.5, base=0.15):
    """Relative availability: base + (1 - base) * smooth plateau from lo to hi."""
    up = 1 / (1 + np.exp(-(pH - lo) / w_lo * 2.2))
    down = 1 / (1 + np.exp((pH - hi) / w_hi * 2.2))
    return base + (1 - base) * up * down


rows = [
    ("Nitrogen", bump(5.4, 8.0, 0.5, 0.5, 0.25), "dna"),
    ("Phosphorus", bump(5.6, 7.3, 0.4, 0.35, 0.18), "rna"),
    ("Potassium", bump(5.3, 9.6, 0.5, 0.5, 0.3), "k"),
    ("Sulfur", bump(5.3, 9.6, 0.5, 0.5, 0.3), "highlight"),
    ("Calcium", bump(6.0, 9.6, 0.6, 0.5, 0.15), "ca"),
    ("Magnesium", bump(6.0, 9.6, 0.6, 0.5, 0.15), "mg"),
    ("Iron", bump(3.0, 6.6, 0.5, 0.4, 0.12), "negative"),
    ("Manganese", bump(3.0, 6.7, 0.5, 0.45, 0.12), "protein"),
    ("Zinc", bump(3.0, 7.0, 0.5, 0.5, 0.15), "metabolite"),
    ("Copper", bump(3.0, 7.0, 0.5, 0.5, 0.15), "drug"),
    ("Boron", bump(3.0, 7.0, 0.5, 0.45, 0.2) + 0.25 * np.exp(-((pH - 8.8) / 0.4) ** 2), "carbohydrate"),
    ("Molybdenum", bump(6.6, 11.0, 0.6, 0.5, 0.12), "enzyme"),
]

fig, ax = plt.subplots(figsize=(9.0, 6.2))
ax.axvspan(5.5, 6.5, color=P.fill("positive"), alpha=0.25, lw=0)
n = len(rows)
for i, (name, w, tok) in enumerate(rows):
    y = n - 1 - i
    w = np.clip(w, 0, 1.1) * 0.42
    ax.fill_between(pH, y - w, y + w, color=P.fill(tok), edgecolor=charts.line(tok), lw=0.8)
    ax.text(3.92, y, name, ha="right", va="center", fontsize=8.5, color=P.ink())
# aluminium toxicity
al = 1 / (1 + np.exp((pH - 4.9) / 0.18))
ax.fill_between(pH, -1.4 - 0.42 * al, -1.4 + 0.42 * al, color=P.fill("neutral"), edgecolor=P.edge("neutral"), lw=0.8)
ax.text(3.92, -1.4, "Al$^{3+}$ (toxic)", ha="right", va="center", fontsize=8.5, color=P.ink())
ax.axhline(-0.75, color=P.muted(), lw=0.6)
ax.text(6.0, n - 0.3, "most nutrients\navailable", ha="center", va="bottom", fontsize=7.5, color=P.muted())
ax.set_xlim(4.0, 9.0)
ax.set_ylim(-2.0, n + 0.6)
ax.set_yticks([])
ax.spines["left"].set_visible(False)
charts.style_axes(ax, "soil pH", None)
ax.spines["left"].set_visible(False)
ax.set_xticks([4, 5, 6, 7, 8, 9])
ax.text(4.5, -2.0, "acidic", ha="center", va="top", fontsize=7.5, color=P.muted(), transform=ax.transData)
ax.text(8.5, -2.0, "alkaline", ha="center", va="top", fontsize=7.5, color=P.muted())
