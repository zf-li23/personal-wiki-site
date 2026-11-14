"""The East Asian-Australasian Flyway as a schematic (not a map: regions are placed by approximate latitude and
longitude, without coastlines). Routes: bar-tailed godwits (Limosa lapponica baueri) fly nonstop from western
Alaska to New Zealand and eastern Australia in autumn (about 11 000-13 500 km in 8-11 days) and return in spring
via the Yellow Sea, where they refuel for 5-6 weeks; great knots (Calidris tenuirostris) breed in north-eastern
Siberia, stage in the Yellow Sea in both seasons and winter in northern Australia; the spoon-billed sandpiper
(Calidris pygmaea) breeds in Chukotka and winters in southern China and the Gulf of Martaban. Distances along
great circles are given for orientation only."""
import numpy as np

import wikibio as bio
from wikibio import quant

P = bio.P
fig, ax = bio.canvas(22, 13)
p = quant.Plot(ax, (1.8, 1.4, 18.6, 11.0), xlim=(90, 200), ylim=(-50, 72), xlabel="Longitude (degrees east)",
               ylabel="Latitude", xticks=[(90, "90° E"), (120, "120° E"), (150, "150° E"), (180, "180°"), (200, "160° W")],
               yticks=[(-40, "40° S"), (-20, "20° S"), (0, "0°"), (20, "20° N"), (40, "40° N"), (60, "60° N")], grid=True, ylabel_offset=1.7)
regions = [((150, 168, 62, 71), "plant", "NE Siberia, Chukotka"), ((185, 198, 58, 68), "plant", "W Alaska"),
           ((115, 131, 33, 41), "highlight", "Yellow Sea, Bohai"), ((100, 112, 12, 24), "neutral", "SE Asia"),
           ((118, 140, -22, -12), "neutral", "N Australia"), ((143, 154, -40, -26), "neutral", "E Australia"),
           ((168, 179, -47, -35), "neutral", "New Zealand")]
for (x0, x1, y0, y1), tok, name in regions:
    X0, Y0 = p.xy(x0, y0)
    X1, Y1 = p.xy(x1, y1)
    bio.box(ax, ((X0 + X1) / 2, (Y0 + Y1) / 2), X1 - X0, Y1 - Y0, tok, text=name, size="tiny", radius=0.1)


def route(pts, tok, dashed=False, bend=0.0):
    for a, b in zip(pts[:-1], pts[1:]):
        bio.arrow(ax, p.xy(*a), p.xy(*b), kind="process", color=P.edge(tok), lw=1.6, dashed=dashed, bend=bend, shrink=0.02)


route([(186, 61), (172, -35)], "rna", bend=-0.08)                       # godwit autumn nonstop
route([(173, -36), (127, 37)], "rna", dashed=True, bend=-0.12)          # godwit spring to Yellow Sea
route([(127, 41), (186, 63)], "rna", dashed=True, bend=-0.15)
route([(156, 62), (122, 41)], "dna", bend=0.1)                          # great knot
route([(122, 33), (128, -12)], "dna", bend=0.1)
route([(162, 64), (124, 40.5)], "enzyme", dashed=True, bend=0.2)          # spoon-billed sandpiper
route([(118, 34), (108, 24)], "enzyme", dashed=True)
p.legend([("bar-tailed godwit: autumn (nonstop)", "rna", "-"), ("bar-tailed godwit: spring", "rna", "--"),
          ("great knot", "dna", "-"), ("spoon-billed sandpiper", "enzyme", "--")], at=p.xy(92, -28), size="small")
