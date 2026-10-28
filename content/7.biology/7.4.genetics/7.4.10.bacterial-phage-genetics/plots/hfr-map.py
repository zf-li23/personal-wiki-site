# Circular E. coli map (minutes) with the origins and directions of several Hfr strains
import wikibio as bio
from wikibio import transmission as T

fig, ax = bio.canvas(12, 11)
T.hfr_map(ax, (6.0, 5.4), 3.6,
          markers=[(0, "thr"), (2, "leu"), (6, "pro"), (8, "lac"), (17, "gal"), (27, "trp"), (44, "his"),
                   (63, "cys"), (73, "str"), (80, "mal"), (89, "met")],
          hfrs=[(97, 1, "HfrH"), (14, -1, "Hfr 2"), (36, 1, "Hfr 3"), (58, -1, "Hfr 4"), (85, -1, "Hfr 5")])
