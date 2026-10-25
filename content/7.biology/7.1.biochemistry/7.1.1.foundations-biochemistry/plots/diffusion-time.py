# Diffusion sets the size of cells: mean time to diffuse a distance x in three dimensions,
# t = x^2 / (6 D), for O2, glucose and a small protein in water (25 C) and for GFP in the
# crowded cytoplasm of a mammalian cell. Shaded bands mark typical bacterial and eukaryotic cell sizes.
import numpy as np
import wikibio as bio
from wikibio import charts as C

species = [
    ("O$_2$ in water", 2.1e-9, "highlight", "-"),
    ("glucose in water", 6.7e-10, "carbohydrate", "-"),
    ("myoglobin in water", 1.1e-10, "protein", "-"),
    ("GFP in cytoplasm", 2.5e-11, "negative", "--"),
]

fig, ax = bio.canvas(15, 9)
a = C.axes_at(ax, (2.0, 1.5, 12.2, 6.9))
x = np.logspace(-8, -1, 300)  # m
for name, D, tok, ls in species:
    a.loglog(x, x**2 / (6 * D), color=C.line(tok), lw=2.0, ls=ls, label=f"{name}, D = {D/10**np.floor(np.log10(D)):.1f}" + r"$\times 10^{%d}$ m$^2$ s$^{-1}$" % np.floor(np.log10(D)))

for lo, hi, text in [(5e-7, 3e-6, "bacteria"), (1e-5, 1e-4, "eukaryotic cells")]:
    a.axvspan(lo, hi, color=bio.P.mix(bio.P.surface(), bio.P.muted(), 0.22), lw=0)
    a.text(np.sqrt(lo * hi), 3e6, text, ha="center", va="top", fontsize=bio.core.FONT["tiny"], color=bio.P.ink())

for t, text in [(1e-3, "1 ms"), (1.0, "1 s"), (3600.0, "1 h"), (86400.0, "1 day")]:
    a.axhline(t, color=bio.P.muted(), lw=0.6, ls=(0, (3, 3)))
    a.text(1.3e-8, t * 1.4, text, fontsize=bio.core.FONT["tiny"], color=bio.P.muted())

a.set_xlim(1e-8, 1e-1)
a.set_ylim(1e-9, 1e7)
a.set_yticks([1e-9, 1e-6, 1e-3, 1, 1e3, 1e6])
a.set_xticks([1e-8, 1e-7, 1e-6, 1e-5, 1e-4, 1e-3, 1e-2, 1e-1],
             ["10 nm", "100 nm", "1 µm", "10 µm", "100 µm", "1 mm", "1 cm", "10 cm"])
C.style_axes(a, "distance x", "mean diffusion time t / s")
leg = a.legend(loc="lower right", fontsize=bio.core.FONT["tiny"], frameon=False)
for txt in leg.get_texts():
    txt.set_color(bio.P.ink())
