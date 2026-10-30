"""Stages of nephron formation next to a ureteric bud tip."""
import wikibio as bio
from wikibio import mesoderm as M

fig, ax = bio.canvas(24, 6.4)
P = bio.P
st = ("cap", "aggregate", "vesicle", "comma", "s-shaped", "nephron")
nm = ("Cap mesenchyme", "Pretubular aggregate", "Renal vesicle", "Comma-shaped body", "S-shaped body", "Nephron")
for k, s in enumerate(st):
    x = 2.0 + k * 3.9
    a = M.nephrogenesis(ax, (x, 3.9), 1.25, s)
    bio.label(ax, (x - 1.4, 6.1), "ABCDEF"[k], bold=True, ha="left")
    bio.label(ax, (x + 0.2, 0.35), nm[k], size="small")
    if s == "nephron":
        bio.callout(ax, a["glomerulus"], (x - 1.6, 1.0), "Glomerulus")
        bio.callout(ax, a["loop"], (x + 0.4, 0.9), "Loop")
        bio.callout(ax, a["collecting"], (x + 1.8, 2.0), "Collecting duct")
    if s == "cap":
        bio.callout(ax, a["tip"], (x + 1.6, 5.6), "Bud tip")
