"""The bipotential gonad and its two fates (transverse sections, dorsal up)."""
import wikibio as bio
from wikibio import mesoderm as M

fig, ax = bio.canvas(22, 9.0)
P = bio.P
for k, f in enumerate(("indifferent", "testis", "ovary")):
    x = 3.6 + k * 7.2
    a = M.gonad(ax, (x, 3.6), 2.0, f)
    bio.label(ax, (x - 3.2, 8.5), "ABC"[k] + "  " + ("Indifferent gonad", "Testis", "Ovary")[k], bold=True, ha="left")
    if f == "indifferent":
        bio.callout(ax, a["wolffian"], (x - 2.6, 7.8), "Wolffian duct")
        bio.callout(ax, a["mullerian"], (x + 2.4, 7.8), "Muellerian duct")
        bio.callout(ax, a["mesonephros"], (x - 3.0, 6.8), "Mesonephros")
        bio.callout(ax, a["germ"], (x + 2.8, 4.4), "Germ cells")
        bio.callout(ax, a["epithelium"], (x + 2.8, 2.6), "Coelomic epithelium")
        bio.callout(ax, a["cords"], (x - 2.9, 3.0), "Sex cords")
    elif f == "testis":
        bio.callout(ax, a["sertoli"], (x + 2.7, 5.5), "Testis cord (Sertoli)")
        bio.callout(ax, a["leydig"], (x - 2.9, 1.0), "Leydig cells")
        bio.callout(ax, a["vessel"], (x + 2.8, 3.0), "Coelomic vessel")
        bio.callout(ax, a["mullerian"], (x + 1.6, 7.9), "Regressing duct")
    else:
        bio.callout(ax, a["granulosa"], (x + 2.8, 4.8), "Follicle (granulosa)")
        bio.callout(ax, a["theca"], (x + 2.8, 2.4), "Theca precursors")
        bio.callout(ax, a["wolffian"], (x - 2.9, 6.7), "Regressing duct")
