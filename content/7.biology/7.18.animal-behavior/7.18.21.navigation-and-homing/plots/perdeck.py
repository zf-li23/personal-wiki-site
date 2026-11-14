"""Perdeck's displacement experiment (Perdeck 1958), schematic (regions placed by approximate latitude and
longitude, no coastlines). About 11 000 starlings migrating west-southwest through the Netherlands in autumn were
caught, ringed and released in Switzerland. Ring recoveries in winter: adults (blue) corrected for the
displacement and flew north-west toward the normal wintering area (southern England, northern France); juveniles
(orange), on their first migration, kept their normal direction and distance and ended in southern France and
Spain, a parallel shift of the normal route. Gray: the normal route."""
import wikibio as bio
from wikibio import quant

P = bio.P
fig, ax = bio.canvas(20, 12)
p = quant.Plot(ax, (2.0, 1.4, 16.8, 10.0), xlim=(-12, 16), ylim=(36, 60), xlabel="Longitude",
               ylabel="Latitude", xticks=[(-10, "10° W"), (0, "0°"), (10, "10° E")],
               yticks=[(40, "40° N"), (45, "45° N"), (50, "50° N"), (55, "55° N")], grid=True, ylabel_offset=1.6)
regions = [((10, 16, 54, 59), "plant", "breeding areas\n(Baltic)"), ((3.5, 7, 51.5, 53.5), "highlight", "capture\n(Netherlands)"),
           ((6, 10, 46, 48), "negative", "release\n(Switzerland)"), ((-6, 2, 48.5, 52), "neutral", "normal wintering area"),
           ((-9, 1, 39, 43.5), "rna", "juveniles' recoveries")]
for (x0, x1, y0, y1), tok, name in regions:
    X0, Y0 = p.xy(x0, y0)
    X1, Y1 = p.xy(x1, y1)
    bio.box(ax, ((X0 + X1) / 2, (Y0 + Y1) / 2), X1 - X0, Y1 - Y0, tok, text=name, size="tiny", radius=0.1)


def arr(a, b, tok, dashed=False, bend=0.0):
    bio.arrow(ax, p.xy(*a), p.xy(*b), kind="process", color=P.edge(tok), lw=1.8, dashed=dashed, bend=bend, shrink=0.02)


arr((11, 54.5), (6.5, 53.3), "neutral", dashed=True)
arr((4, 51.6), (1.5, 50.8), "neutral", dashed=True)
arr((7, 46.5), (0.5, 49.0), "dna", bend=-0.1)
arr((6.5, 46.1), (-1.0, 43.2), "rna", bend=0.1)
p.legend([("normal route", "neutral", "--"), ("adults after displacement", "dna", "-"),
          ("juveniles after displacement", "rna", "-")], at=p.xy(-11, 58.5), size="small")
