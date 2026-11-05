# The endodermis and radial water movement in the root. (A) A radial file of cells from the epidermis
# (with a root hair) through the cortex, endodermis and pericycle to a xylem vessel, drawn as two
# neighbouring files so that the wall between them is a radial wall: the apoplastic path (blue, dashed)
# runs in the walls and is blocked by the Casparian strip (red) in the radial wall of the endodermis; the
# symplastic path (orange) passes from cell to cell through plasmodesmata. (B) An endodermal cell seen
# obliquely: the Casparian strip is a band in the radial and transverse (anticlinal) walls only.
# (C) Developmental states of the endodermis in transverse section: state I, Casparian strip only;
# state II, a suberin lamella lines the whole wall; state III, thick (often lignified) walls laid over it,
# in monocots on the radial and inner tangential walls (U-shaped), with an unthickened passage cell.
import numpy as np
from matplotlib.patches import FancyBboxPatch, Polygon, Rectangle

import wikibio as bio

P = bio.P
fig, ax = bio.canvas(32.0, 14.0)


def cell(x, y, w, h, token="cytoplasm", wall="cell_wall", lw=1.6, z=5):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0,rounding_size=0.25", facecolor=P.fill(token),
                                edgecolor=P.edge(wall), lw=lw, zorder=z))


# ---- A
bio.panel(ax, "A", (0.2, 13.8))
bio.label(ax, (0.85, 13.77), "Apoplastic and symplastic paths", size="title", ha="left", va="top")
names = ["Epidermis", "Cortex", "Cortex", "Cortex", "Endodermis", "Pericycle", "Xylem vessel"]
xs = [1.2, 3.0, 4.9, 6.8, 8.7, 10.1, 11.4]
ws = [1.6, 1.7, 1.7, 1.7, 1.2, 1.1, 1.9]
rows = [(7.3, 2.1), (9.6, 2.1)]  # two neighbouring files; the gap between them is the radial wall
for (y, h) in rows:
    for k, (x, w) in enumerate(zip(xs, ws)):
        tok = {4: "golgi", 5: "metabolite", 6: "extracellular"}.get(k, "cytoplasm")
        if k == 6:
            cell(x, y - 0.25, w, h + 0.5, token="extracellular", wall="xylem", lw=2.6)
        else:
            cell(x, y, w, h, token=tok)
# root hair from the lower epidermal cell
hair = np.array([(1.2, 8.2), (0.3, 8.0), (-0.1, 7.9)])
ax.add_patch(FancyBboxPatch((0.1, 8.0), 1.3, 0.5, boxstyle="round,pad=0,rounding_size=0.25", facecolor=P.fill("cytoplasm"),
                            edgecolor=P.edge("cell_wall"), lw=1.6, zorder=4.9))
# Casparian strips: in the radial wall between the two endodermal cells (and at the outer edges)
for yy in (9.45, 7.15, 11.85):
    ax.add_patch(Rectangle((9.0, yy - 0.12), 0.6, 0.24, facecolor=P.fill("negative"), edgecolor=P.edge("negative"), lw=0.8,
                           zorder=8))
# apoplast path along the radial wall (gap between rows), blocked at the endodermis
ya = 9.45
ax.plot([0.5, 8.85], [ya, ya], color=P.edge("dna"), lw=2.2, ls=(0, (3, 2)), zorder=9)
bio.arrow(ax, (8.6, ya), (9.25, 8.6), kind="process", color=P.edge("dna"), dashed=True)
bio.label(ax, (8.95, ya + 0.55), "blocked", size="tiny", color=P.edge("negative"))
ax.plot([9.7, 12.0], [ya, ya], color=P.edge("dna"), lw=2.2, ls=(0, (3, 2)), zorder=9)
bio.arrow(ax, (11.5, ya), (12.3, ya), kind="process", color=P.edge("dna"), dashed=True)
# symplast path through the lower file, crossing walls at plasmodesmata
yb = 8.35
xsym = [0.6, 2.0, 3.85, 5.75, 7.65, 9.3, 10.65, 11.9]
ax.plot(xsym, [yb] * len(xsym), color=P.edge("rna"), lw=2.4, zorder=9)
for x in (2.9, 4.8, 6.7, 8.6, 10.0):
    ax.plot([x - 0.05, x + 0.05], [yb, yb], color=P.ink(), lw=4, zorder=9.5, solid_capstyle="butt")
bio.arrow(ax, (11.2, yb), (12.3, yb), kind="process", color=P.edge("rna"))
for k, (x, w) in enumerate(zip(xs, ws)):
    if k in (2, 3):
        continue
    bio.label(ax, (x + w / 2, 12.35 if k % 2 == 0 else 12.0), names[k] if k != 1 else "Cortex", size="small")
bio.label(ax, (5.75, 12.0), "", size="small")
ax.plot([0.6, 1.4], [6.4, 6.4], color=P.edge("dna"), lw=2.2, ls=(0, (3, 2)))
bio.label(ax, (1.6, 6.4), "Apoplastic path (in walls)", size="small", ha="left")
ax.plot([0.6, 1.4], [5.8, 5.8], color=P.edge("rna"), lw=2.4)
bio.label(ax, (1.6, 5.8), "Symplastic path (via plasmodesmata)", size="small", ha="left")
ax.add_patch(Rectangle((0.7, 5.08), 0.6, 0.24, facecolor=P.fill("negative"), edgecolor=P.edge("negative"), lw=0.8))
bio.label(ax, (1.6, 5.2), "Casparian strip", size="small", ha="left")
bio.label(ax, (6.5, 4.4), "outside (soil)  ← radial direction →  inside (stele)", size="tiny", color=P.muted())

# ---- B: oblique view of one endodermal cell
bio.panel(ax, "B", (15.0, 13.8))
bio.label(ax, (15.65, 13.77), "Endodermal cell", size="title", ha="left", va="top")
o = np.array([16.8, 6.4])
W, H, D = 3.0, 4.6, np.array([1.6, 1.0])
front = [o, o + (W, 0), o + (W, H), o + (0, H)]
top = [o + (0, H), o + (W, H), o + (W, H) + D, o + (0, H) + D]
side = [o + (W, 0), o + (W, 0) + D, o + (W, H) + D, o + (W, H)]
for poly, tok in ((front, "golgi"), (top, "cytoplasm"), (side, "cytoplasm")):
    ax.add_patch(Polygon(poly, closed=True, facecolor=P.fill(tok), edgecolor=P.edge("cell_wall"), lw=1.4, zorder=5))
band_y0, band_y1 = 0.42, 0.58
side_band = [o + (W, H * band_y0), o + (W, H * band_y0) + D, o + (W, H * band_y1) + D, o + (W, H * band_y1)]
ax.add_patch(Polygon(side_band, closed=True, facecolor=P.fill("negative"), edgecolor=P.edge("negative"), lw=0.8, zorder=6))
t0, t1 = 0.42, 0.58
top_band = [o + (0, H) + D * t0, o + (W, H) + D * t0, o + (W, H) + D * t1, o + (0, H) + D * t1]
ax.add_patch(Polygon(top_band, closed=True, facecolor=P.fill("negative"), edgecolor=P.edge("negative"), lw=0.8, zorder=6))
bio.callout(ax, tuple(o + (W, H * 0.5) + D * 0.5), (24.2, 9.0), "Casparian strip in a radial wall")
bio.callout(ax, tuple(o + (W * 0.7, H) + D * 0.5), (24.2, 12.3), "... and in a transverse wall")
bio.callout(ax, tuple(o + (W * 0.4, H * 0.3)), (24.2, 6.0), "Tangential wall (no strip)")
bio.arrow(ax, (16.4, 5.2), (19.6, 5.2), kind="process", color=P.muted())
bio.label(ax, (18.0, 4.75), "towards stele (radial)", size="tiny", color=P.muted())

# ---- C: three states of the endodermis
bio.panel(ax, "C", (0.2, 3.9))
bio.label(ax, (0.85, 3.87), "Developmental states (transverse section; stele below)", size="title", ha="left", va="top")


def state(x0, kind):
    for k in range(3):
        x = x0 + k * 1.55
        passage = kind == 3 and k == 1
        cell(x, 0.6, 1.4, 1.9, token="golgi", lw=1.0, z=5)
        if kind >= 2 and not passage:
            ax.add_patch(FancyBboxPatch((x + 0.1, 0.7), 1.2, 1.7, boxstyle="round,pad=0,rounding_size=0.2", facecolor="none",
                                        edgecolor=P.edge("lipid"), lw=2.0, zorder=6))
        if kind == 3 and not passage:
            th = 0.38
            for r in ((x + 0.12, 0.72, th, 1.6), (x + 1.28 - th, 0.72, th, 1.6), (x + 0.12, 0.72, 1.16, th)):
                ax.add_patch(Rectangle(r[:2], r[2], r[3], facecolor=P.fill("sclerenchyma"), edgecolor=P.edge("sclerenchyma"),
                                       lw=0.6, zorder=6.5))
        for xx in (x - 0.07, x + 1.47):
            if k == 0 and xx < x or True:
                ax.add_patch(Rectangle((xx - 0.07, 1.4), 0.14, 0.35, facecolor=P.fill("negative"), edgecolor=P.edge("negative"),
                                       lw=0.5, zorder=7))
        if passage:
            bio.label(ax, (x + 0.7, 0.25), "passage cell", size="tiny", color=P.muted())


for x0, kind, t in ((1.0, 1, "I: Casparian strip"), (6.3, 2, "II: + suberin lamella"), (11.6, 3, "III: + thick walls (U-shaped)")):
    state(x0, kind)
    bio.label(ax, (x0 + 2.25, 2.95), t, size="small")
