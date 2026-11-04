"""Sizes of microorganisms on a log length axis (top) and their surface-to-volume ratios (bottom).
Rods are treated as capsules (cylinder + two hemispheres): S/V = (2/r)(L + 2r)/(L + 4r/3)."""
import numpy as np

import wikibio as bio
from wikibio import charts

P = bio.P
# name, width (um), total length (um), token, italic, label level
ORG = [("circovirus", 0.018, 0.018, "virus", False, 0), ("ribosome", 0.025, 0.025, "rrna", False, 1),
       ("poliovirus", 0.03, 0.03, "virus", False, 2), ("phage T4", 0.09, 0.2, "virus", False, 0),
       ("mimivirus", 0.75, 0.75, "virus", False, 2),
       ("Pelagibacter", 0.2, 0.5, "bacterium", True, 1), ("Mycoplasma", 0.3, 0.3, "bacterium", True, 3),
       ("E. coli", 1.0, 2.0, "bacterium", True, 0), ("budding yeast", 5.0, 5.0, "carbohydrate", False, 1),
       ("diatom", 12.0, 50.0, "plant", False, 2), ("Paramecium", 50.0, 200.0, "protein", True, 0),
       ("Epulopiscium", 80.0, 600.0, "bacterium", True, 1),
       ("Thiomargarita\nnamibiensis", 750.0, 750.0, "bacterium", True, 2.4),
       ("Ca. Thiomargarita\nmagnifica", 15.0, 15000.0, "bacterium", True, 0)]


def sv(w, L):
    r = w / 2
    Lc = max(L - w, 0)
    return (2 / r) * (Lc + 2 * r) / (Lc + 4 * r / 3)


fig, ax = bio.canvas(26, 15)
# ---- A: ladder
bio.panel(ax, "A", (0.2, 14.8))
top = charts.axes_at(ax, (2.2, 8.8, 22.8, 1.2))
top.set_xscale("log")
top.set_xlim(0.01, 30000)
top.set_ylim(0, 1)
top.set_yticks([])
for lo, hi, txt, tok, yy in [(0.0002, 0.2, "electron microscope", "neutral", 0.15), (0.2, 100, "light microscope", "highlight", 0.5),
                             (100, 1e6, "naked eye", "positive", 0.85)]:
    top.axvspan(max(lo, 0.01), hi, ymin=yy - 0.13, ymax=yy + 0.13, color=P.fill(tok), lw=0)
    top.text(np.sqrt(max(lo, 0.01) * min(hi, 30000)), yy, txt, ha="center", va="center", fontsize=6.8, color=P.on_fill())
top.set_xticks([0.01, 0.1, 1, 10, 100, 1000, 10000])
top.set_xticklabels(["10 nm", "100 nm", "1 µm", "10 µm", "100 µm", "1 mm", "1 cm"])
charts.style_axes(top, "length (log scale)", None)
top.spines["left"].set_visible(False)
# markers above the axis, in canvas coordinates
def X(v):
    return 2.2 + (np.log10(v) - np.log10(0.01)) / (np.log10(30000) - np.log10(0.01)) * 22.8


for name, w, L, tok, it, lev in ORG:
    x = X(L)
    y = 10.4 + 0.95 * lev
    ax.plot([x, x], [10.0, y - 0.15], color=P.muted(), lw=0.6)
    ax.plot([x], [10.0], "o", ms=5, color=P.fill(tok), markeredgecolor=P.edge(tok), zorder=8)
    bio.label(ax, (x, y), name, size="tiny", italic=it, va="bottom")
bio.label(ax, (13.6, 14.6), "Longest dimension of microorganisms", size="normal", bold=True)
# ---- B: S/V
bio.panel(ax, "B", (0.2, 6.9))
pax = charts.axes_at(ax, (2.2, 1.2, 22.8, 5.0))
d = np.logspace(-2, 4.3, 200)
pax.plot(d, 6 / d, color=P.muted(), lw=1.0, ls="--")
pax.text(2000, 6 / 2000 * 3.0, "sphere: S/V = 3/r", fontsize=6.8, color=P.muted())
for name, w, L, tok, it, lev in ORG:
    if tok == "rrna":
        continue
    v = sv(w, L)
    pax.plot([L], [v], "o", ms=5, color=P.fill(tok), markeredgecolor=P.edge(tok), zorder=5)
    nm = name.replace("\n", " ")
    off = {"Ca. Thiomargarita magnifica": (0.35, 1.6), "Thiomargarita namibiensis": (1.3, 0.55), "Pelagibacter": (1.2, 2.0), "Mycoplasma": (1.25, 0.5)}.get(nm, (1.25, 1.0))
    pax.text(L * off[0], v * off[1], nm, fontsize=6.3, color=P.ink(), style="italic" if it else "normal",
             ha="left", va="center")
pax.set_xscale("log")
pax.set_yscale("log")
pax.set_xlim(0.01, 30000)
pax.set_ylim(1e-3, 1e3)
pax.set_xticks([0.01, 0.1, 1, 10, 100, 1000, 10000])
pax.set_xticklabels(["10 nm", "100 nm", "1 µm", "10 µm", "100 µm", "1 mm", "1 cm"])
charts.style_axes(pax, "longest dimension", "S/V / µm⁻¹")
