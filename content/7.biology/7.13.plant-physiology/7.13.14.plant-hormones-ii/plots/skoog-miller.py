# Skoog-Miller: fate of tobacco pith callus on a grid of auxin and cytokinin concentrations (schematic).
# High auxin/cytokinin ratio -> roots; intermediate -> undifferentiated callus; low -> shoots.
import numpy as np
import wikibio as bio

fig, ax = bio.canvas(13, 10.5)
P = bio.P
x0, y0, cell = 2.2, 1.6, 1.6
levels = ["0.01", "0.1", "1", "10", "100"]   # relative concentration (arbitrary units)
for i in range(5):          # cytokinin index (x)
    for j in range(5):      # auxin index (y)
        cx, cy = x0 + (i + 0.5) * cell, y0 + (j + 0.5) * cell
        r = j - i
        if i <= 1 and j <= 1 and r == 0:
            fate = "little"
        elif r >= 2:
            fate = "roots"
        elif r <= -2:
            fate = "shoots"
        else:
            fate = "callus"
        tok = {"roots": "lipid_head", "shoots": "plant", "callus": "highlight", "little": "neutral"}[fate]
        fc = bio.P.mix(bio.P.fill(tok), bio.P.surface(), 0.55)
        ax.add_patch(__import__("matplotlib.patches", fromlist=["Rectangle"]).Rectangle(
            (cx - cell / 2, cy - cell / 2), cell, cell, facecolor=fc, edgecolor=P.muted(), lw=0.6, zorder=1))
        # callus lump
        lump = bio.blob((cx, cy - 0.35), 0.45, 0.22, wobble=0.12, seed=i * 7 + j)
        if fate != "little":
            bio.shape(ax, lump, token="highlight", lw=0.8, zorder=3)
        else:
            bio.shape(ax, bio.blob((cx, cy - 0.4), 0.2, 0.1, wobble=0.1, seed=3), token="neutral", lw=0.8, zorder=3)
        if fate == "roots":
            for k, dx in enumerate((-0.3, -0.05, 0.25)):
                ax.plot([cx + dx, cx + dx * 1.5], [cy - 0.42, cy - 0.78], color=P.edge("lipid_head"), lw=1.3, zorder=2)
        if fate == "shoots":
            for dx in (-0.22, 0.2):
                ax.plot([cx + dx, cx + dx * 0.8], [cy - 0.2, cy + 0.25], color=P.edge("plant"), lw=1.4, zorder=4)
                bio.shape(ax, bio.blob((cx + dx * 0.8 + 0.12, cy + 0.32), 0.17, 0.08, wobble=0.05, seed=5), token="plant", lw=0.7, zorder=4)
        if fate == "callus":
            bio.shape(ax, bio.blob((cx, cy - 0.15), 0.55, 0.35, wobble=0.14, seed=11 + i + j), token="highlight", lw=0.8, zorder=3)
for k, t in enumerate(levels):
    bio.label(ax, (x0 + (k + 0.5) * cell, y0 - 0.35), t, size="small")
    bio.label(ax, (x0 - 0.35, y0 + (k + 0.5) * cell), t, size="small", ha="right")
bio.label(ax, (x0 + 2.5 * cell, 0.55), "Cytokinin (kinetin), relative concentration (log scale)", size="small")
bio.label(ax, (0.45, y0 + 2.5 * cell), "Auxin (IAA), relative concentration (log scale)", size="small", rotation=90)
for off in (-2, 2):
    xs = np.linspace(x0, x0 + 5 * cell, 200)
    ys = xs - x0 + y0 + (off * 0.5) * cell
    ok = (ys >= y0) & (ys <= y0 + 5 * cell)
    if off == 0:
        continue
    ax.plot(xs[ok], ys[ok], color=P.muted(), lw=0.8, ls="--", zorder=5, clip_on=True)
ax.set_xlim(0, 13)
ax.set_ylim(0, 10.5)
# legend
for k, (tok, t) in enumerate((("lipid_head", "roots"), ("highlight", "callus only"), ("plant", "shoots"), ("neutral", "little growth"))):
    yy = 8.6 - k * 0.8
    bio.box(ax, (10.9, yy), 0.5, 0.4, token=tok, radius=0.08)
    bio.label(ax, (11.35, yy), t, size="small", ha="left")
bio.label(ax, (11.3, 9.5), "Fate", size="small", bold=True)
