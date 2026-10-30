"""The three kidneys along the nephric duct (lateral view, anterior left) and the human timeline."""
import wikibio as bio
from wikibio import mesoderm as M

fig, ax = bio.canvas(18, 9.2)
P = bio.P
a = M.nephric_series(ax, (0.6, 2.0), 15.5, gonad=True)
bio.callout(ax, a["pronephros"], (1.2, 8.7), "Pronephros (degenerates)")
bio.callout(ax, a["mesonephros"], (6.0, 8.7), "Mesonephros")
bio.callout(ax, a["gonad"], (9.6, 8.7), "Genital ridge")
bio.callout(ax, a["metanephric"], (13.0, 8.7), "Metanephric mesenchyme")
bio.callout(ax, a["ureteric_bud"], (15.6, 6.9), "Ureteric bud")
bio.callout(ax, a["duct"], (5.5, 1.2), "Nephric (Wolffian) duct")
bio.callout(ax, a["cloaca"], (16.6, 1.2), "Cloaca")
bio.label(ax, (8.0, 7.6), "somites", size="tiny", color=P.muted())
ty = 0.35
for x, t in ((1.3, "day 22"), (6.0, "from day 25"), (13.0, "day 28 (bud); nephrons wk 8-36")):
    bio.label(ax, (x, ty), t, size="tiny", color=P.muted())
