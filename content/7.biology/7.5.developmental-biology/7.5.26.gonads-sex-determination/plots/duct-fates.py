"""Secondary sex determination of the internal genital ducts (frontal view)."""
import wikibio as bio
from wikibio import mesoderm as M

fig, ax = bio.canvas(25.6, 9.4)
P = bio.P
for k, sx in enumerate(("indifferent", "male", "female")):
    x = 4.0 + k * 8.4
    a = M.genital_ducts(ax, (x, 4.6), 7.0, sx)
    bio.label(ax, (x - 3.4, 9.0), "ABC"[k] + "  " + ("Indifferent", "Male", "Female")[k], bold=True, ha="left")
    bio.callout(ax, a["sinus"], (x + 1.8, 0.4), "Urogenital sinus")
    if sx == "indifferent":
        bio.callout(ax, a["wolffian"], (x + 2.9, 3.4), "Wolffian")
        bio.callout(ax, a["mullerian"], (x + 3.1, 6.2), "Muellerian")
        bio.callout(ax, a["gonad_l"], (x - 3.0, 7.9), "Gonad")
    elif sx == "male":
        bio.callout(ax, a["gonad"], (x + 3.0, 8.2), "Testis")
        bio.callout(ax, a["epididymis_l"], (x - 3.1, 7.9), "Epididymis")
        bio.callout(ax, a["vas"], (x + 2.9, 3.2), "Vas deferens")
        bio.callout(ax, a["vesicle_l"], (x - 3.1, 1.6), "Seminal vesicle")
    else:
        bio.callout(ax, a["gonad"], (x + 3.0, 8.2), "Ovary")
        bio.callout(ax, a["oviduct_l"], (x - 3.5, 6.6), "Oviduct")
        bio.callout(ax, a["uterus"], (x + 2.8, 3.6), "Uterus")
        bio.callout(ax, a["vagina"], (x - 2.9, 1.5), "Upper vagina")
