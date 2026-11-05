"""Plastid types and their interconversion (schematic). All plastids develop from the proplastids of
meristematic cells. In light a proplastid becomes a chloroplast; in darkness it becomes an etioplast,
which turns green within hours of illumination. Non-pigmented leucoplasts store starch (amyloplasts),
lipids (elaioplasts) or protein (proteinoplasts). Chromoplasts accumulate carotenoids; they usually arise
from chloroplasts (ripening tomato and pepper) or from leucoplasts (carrot root, many petals), rarely
straight from proplastids. Solid arrows: the usual routes; dashed arrows: reversals (amyloplasts greening
in light, as in potato tubers and the aerial roots of Chlorophytum; chromoplasts re-greening, as in
regreening citrus; plastids dedifferentiating in callus). Senescent leaves turn chloroplasts into
gerontoplasts.
"""

import wikibio as bio

P = bio.P
fig, ax = bio.canvas(25.0, 12.0)


def node(xy, token, title, sub, w=4.6, h=1.6):
    bio.box(ax, xy, w, h, token=token, text=None)
    bio.label(ax, (xy[0], xy[1] + 0.28), title, size="normal", color=P.on_fill(), bold=True)
    bio.label(ax, (xy[0], xy[1] - 0.34), sub, size="tiny", color=P.on_fill())


N = {
    "pro": ((4.0, 6.0), "neutral", "Proplastid", "meristem; few internal membranes"),
    "chl": ((12.5, 9.8), "chloroplast", "Chloroplast", "thylakoids, grana; photosynthesis"),
    "eti": ((12.5, 6.0), "highlight", "Etioplast", "dark-grown; prolamellar body"),
    "leu": ((12.5, 2.2), "vacuole", "Leucoplasts", "amyloplast / elaioplast / proteinoplast"),
    "chr": ((21.0, 6.0), "atp", "Chromoplast", "carotenoids: globules, fibrils, crystals"),
    "ger": ((21.0, 10.4), "animal", "Gerontoplast", "senescent leaf; thylakoids dismantled"),
}
for k, (xy, tk, t, s) in N.items():
    node(xy, tk, t, s)


def go(a, b, text, xy, dashed=False, bend=0.0, kind="process"):
    bio.arrow(ax, a, b, kind=kind, dashed=dashed, bend=bend)
    if text:
        bio.label(ax, xy, text, size="tiny", color=P.muted())


go((6.3, 6.7), (10.2, 9.5), "light", (7.7, 8.65))
go((6.3, 6.0), (10.2, 6.0), "dark", (8.25, 6.35))
go((6.3, 5.3), (10.2, 2.5), "storage cells", (7.4, 3.4))
go((12.5, 6.8), (12.5, 9.0), "light (hours)", (13.85, 7.9))
go((14.8, 9.6), (18.7, 6.6), "fruit ripening (tomato, pepper)", (18.4, 8.6))
go((14.8, 2.4), (18.7, 5.4), "carrot root, petals", (18.0, 3.4))
go((14.8, 10.3), (18.7, 10.4), "senescence", (16.75, 10.75))
go((14.2, 3.0), (14.2, 9.0), "", (0, 0), dashed=True, bend=-0.3)
bio.label(ax, (16.75, 5.25), "greening in light", size="tiny", color=P.muted())
bio.label(ax, (16.75, 4.9), "(potato tuber, aerial roots)", size="tiny", color=P.muted())
go((19.5, 6.85), (14.0, 9.05), "", (0, 0), dashed=True, bend=0.25)
bio.label(ax, (16.9, 7.15), "re-greening (citrus)", size="tiny", color=P.muted())
go((10.2, 10.3), (3.6, 6.85), "", (0, 0), dashed=True, bend=-0.3)
bio.label(ax, (4.6, 10.6), "dedifferentiation", size="tiny", color=P.muted())
bio.label(ax, (4.6, 10.25), "(callus culture)", size="tiny", color=P.muted())
bio.label(ax, (12.5, 0.55), "Leucoplasts are colourless; amyloplasts of the root cap act as statoliths", size="tiny", color=P.muted())
