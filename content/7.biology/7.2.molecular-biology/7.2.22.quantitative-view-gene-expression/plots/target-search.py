# Target search by DNA-binding proteins.
# A: facilitated diffusion (schematic). A protein alternates between three-dimensional diffusion in solution
#    (dashed arcs, "hopping" over short distances or jumping far) and one-dimensional sliding along the DNA
#    while bound nonspecifically (solid segments); a landing within about one sliding length of the target
#    (highlighted) leads to it, so the DNA around the site acts as an antenna.
# B: association rate constants on a logarithmic scale. Diffusion-limited collision of the repressor with a
#    single operator-sized target, as estimated by Riggs and colleagues (1.9e8 M^-1 s^-1); the measured
#    association of lac repressor with operator DNA in low salt (7e9 M^-1 s^-1, Riggs, Bourgeois and Cohn,
#    1970); and the antenna estimate: the diffusion limit multiplied by a sliding length of about 45 bp, the
#    value measured in living E. coli (Hammar and colleagues, 2012), 1.9e8 x 45 = 8.6e9 M^-1 s^-1. For
#    comparison: typical protein-protein association (1e5-1e6) and a small molecule meeting an enzyme
#    (about 1e8-1e9).
import numpy as np

import wikibio as bio
from wikibio import charts

P = bio.P
fig, ax = bio.canvas(25.0, 8.0)

# --- A ---
bio.panel(ax, "A", (0.2, 7.8))
y0 = 2.2
bio.dna(ax, (0.8, y0), (13.2, y0), style="duplex")
ax.add_patch(__import__("matplotlib.patches", fromlist=["Rectangle"]).Rectangle(
    (9.3, y0 - 0.35), 0.7, 0.7, facecolor=P.fill("highlight"), edgecolor=P.edge("highlight"), lw=1.0, zorder=10))
bio.label(ax, (9.65, y0 - 0.75), "target", size="tiny")
# trajectory: start in solution, land, slide, hop, slide, jump, land near target, slide to it
pts = [((1.5, 6.4), (2.4, y0 + 0.45), "3d"), ((2.4, y0 + 0.45), (3.6, y0 + 0.45), "1d"),
       ((3.6, y0 + 0.45), (4.3, y0 + 0.45), "hop"), ((4.3, y0 + 0.45), (5.0, y0 + 0.45), "1d"),
       ((5.0, y0 + 0.45), (8.1, y0 + 0.45), "jump"), ((8.1, y0 + 0.45), (9.4, y0 + 0.45), "1d")]
for a, b, kind in pts:
    if kind == "1d":
        xs = np.linspace(a[0], b[0], 60)
        ys = a[1] + 0.07 * np.sin(np.linspace(0, 6 * np.pi, 60))
        ax.plot(xs, ys, color=P.edge("protein"), lw=2.0, zorder=12)
    elif kind == "3d":
        xs = np.linspace(a[0], b[0], 80)
        ys = np.linspace(a[1], b[1], 80) + 0.35 * np.sin(np.linspace(0, 5 * np.pi, 80))
        ax.plot(xs, ys, color=P.muted(), lw=1.2, ls=(0, (3, 2)), zorder=12)
    else:
        h = 0.6 if kind == "hop" else 2.6
        xs = np.linspace(a[0], b[0], 60)
        ys = a[1] + h * np.sin(np.linspace(0, np.pi, 60))
        ys += (0.18 if kind == "jump" else 0) * np.sin(np.linspace(0, 7 * np.pi, 60))
        ax.plot(xs, ys, color=P.muted(), lw=1.2, ls=(0, (3, 2)), zorder=12)
for x in (2.4, 5.0, 8.1):
    bio.protein(ax, (x, y0 + 0.62), 0.55, 0.42, "protein", wobble=0.04, zorder=13)
bio.protein(ax, (9.65, y0 + 0.62), 0.55, 0.42, "protein", wobble=0.04, zorder=13)
bio.label(ax, (3.0, y0 + 1.0), "slide", size="tiny", color=P.edge("protein"))
bio.label(ax, (3.95, y0 + 1.25), "hop", size="tiny", color=P.muted())
bio.label(ax, (6.55, y0 + 3.3), "jump (3D diffusion)", size="tiny", color=P.muted())
bio.label(ax, (1.0, 6.75), "from solution", size="tiny", color=P.muted(), ha="left")
bio.label(ax, (8.75, y0 + 1.0), "slide", size="tiny", color=P.edge("protein"))
quantx = (8.2, 11.1)
ax.plot([quantx[0], quantx[1]], [y0 - 1.05, y0 - 1.05], color=P.ink(), lw=0.9)
for x in quantx:
    ax.plot([x, x], [y0 - 1.15, y0 - 0.95], color=P.ink(), lw=0.9)
bio.label(ax, (9.65, y0 - 1.45), "antenna ≈ sliding length", size="tiny")

# --- B ---
bio.panel(ax, "B", (14.4, 7.8))
bx = charts.axes_at(ax, (16.6, 1.3, 7.8, 5.6))
items = [("protein–protein, typical", 1e5, 1e6, "neutral"), ("small molecule + enzyme", 1e8, 1e9, "neutral"),
         ("diffusion limit, one operator", 1.9e8, None, "dna"), ("lac repressor, measured", 7e9, None, "negative"),
         ("limit × 45 bp antenna", 1.9e8 * 45, None, "positive")]
for i, (name, lo, hi, tok) in enumerate(items[::-1]):
    if hi is None:
        bx.barh(i, np.log10(lo) - 4, left=4, height=0.55, color=P.fill(tok), edgecolor=P.edge(tok), lw=0.8)
        bx.text(np.log10(lo) + 0.08, i, f"{lo:.1e}".replace("e+0", " × 10^").replace("^9", "⁹").replace("^8", "⁸"),
                va="center", fontsize=7, color=P.ink())
    else:
        bx.barh(i, np.log10(hi) - np.log10(lo), left=np.log10(lo), height=0.55, color=P.fill(tok),
                edgecolor=P.edge(tok), lw=0.8)
bx.set_yticks(range(len(items)))
bx.set_yticklabels([it[0] for it in items[::-1]], fontsize=7)
bx.set_xlim(4, 11)
bx.set_xticks(range(4, 12))
bx.set_xticklabels([f"10{s}" for s in "⁴⁵⁶⁷⁸⁹"] + ["10¹⁰", "10¹¹"])
charts.style_axes(bx, "association rate constant / (M⁻¹ s⁻¹)")
