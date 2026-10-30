"""One cycle of the segmentation clock in the presomitic mesoderm (dorsal view, anterior left): four rows at
successive phases; the last row has formed one more somite and its tail bud has moved posteriorly by one somite
length. Bars below the last row: FGF/Wnt (posterior) and retinoic acid (anterior) signalling."""
import wikibio as bio
from wikibio import mesoderm as M

fig, ax = bio.canvas(21.4, 12.6)
P = bio.P
h = 1.0
ws = h * 1.05
rows = [(0.0, 4, 0.0, "t = 0"), (0.33, 4, 0.0, "t = P/3"), (0.67, 4, 0.0, "t = 2P/3"), (1.0, 5, ws, "t = P")]
for k, (ph, ns, dx, lab) in enumerate(rows):
    y = 10.6 - k * 2.45
    a = M.psm(ax, (2.2 + dx, y), 15.0, h, phase=ph, n_somites=ns, front=0.42, gradients=(k == 3), waves=2.2)
    bio.label(ax, (1.9, y + h / 2), lab, size="small", ha="right")
    if k == 0:
        bio.callout(ax, a["somites"][1], (3.6, y + 1.75), "Somites")
        bio.callout(ax, a["psm"], (11.5, y + 1.75), "Presomitic mesoderm")
        bio.callout(ax, a["tailbud"], (16.6, y + 1.75), "Tail bud")
        bio.callout(ax, a["front"], (7.6, y + 1.75), "Determination front")
    if k == 3:
        bio.label(ax, a["somites"][-1], "SI", size="tiny", color=P.on_fill())
        bio.callout(ax, (a["x_psm0"] + 0.4, a["y_mid"]), (a["x_psm0"] + 0.6, y - 2.15), "S0 (next boundary)")
        bio.label(ax, (18.45, a["fgf"][1]), "FGF/Wnt", size="tiny", ha="left")
        bio.label(ax, (18.45, a["ra"][1]), "Retinoic acid", size="tiny", ha="left")
bio.label(ax, (2.2, 0.35), "anterior", size="tiny", ha="left", color=P.muted())
bio.label(ax, (18.2, 0.35), "posterior", size="tiny", ha="right", color=P.muted())
bio.arrow(ax, (14.0, 9.85), (10.5, 9.85), kind="process", color=P.muted(), lw=0.9)
bio.label(ax, (12.25, 9.55), "clock wave moves anteriorly", size="tiny", color=P.muted())
