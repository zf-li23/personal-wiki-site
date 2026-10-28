# Sturtevant's 1913 map of the Drosophila X chromosome and the modern positions of the same genes
import wikibio as bio
from wikibio import transmission as T

fig, ax = bio.canvas(11, 9)
old = [("y", 0.0), ("w", 1.0), ("v", 30.7), ("m", 33.7), ("r", 57.6)]
new = [("y", 0.0), ("w", 1.5), ("v", 33.0), ("m", 36.1), ("r", 54.5)]
m1 = T.linkage_map(ax, 2.6, 7.6, old, scale=0.115, name="Sturtevant 1913", side="right")
m2 = T.linkage_map(ax, 8.2, 7.6, new, scale=0.115, name="Modern map", side="left")
T.link_maps(ax, m1, m2)
bio.label(ax, (5.4, 0.35), r"positions in cM from yellow ($\it{y}$)", size="small", color=bio.P.muted())
