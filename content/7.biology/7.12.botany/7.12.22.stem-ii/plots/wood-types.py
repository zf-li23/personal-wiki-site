# Ring-porous, diffuse-porous and coniferous wood: radial strips at cell level (wikibio.botany), pith on
# the left, bark on the right, three growth rings each. (A) Ring-porous (e.g. Quercus): wide earlywood
# vessels at the start of each year. (B) Diffuse-porous (e.g. Acer): vessels of similar size scattered
# through the ring. (C) Softwood (e.g. Pinus): tracheids only.
import wikibio as bio
from wikibio import botany as B

P = bio.P
fig, ax = bio.canvas(17.0, 19.0)
rows = [("A", "Ring-porous wood", "ring-porous", 12.9), ("B", "Diffuse-porous wood", "diffuse-porous", 6.9), ("C", "Softwood (conifer)", "softwood", 0.9)]
for L, title, kind, y in rows:
    bio.panel(ax, L, (0.2, y + 5.7))
    bio.label(ax, (0.85, y + 5.67), title, size="title", ha="left", va="top")
    s = B.wood_strip(ax, (0.8, y + 0.4, 15.4, 3.6), years=3, kind=kind)
    X = s["x"]
    for name, x0, x1 in (("Pith", *X["pith"]), ("Secondary xylem (3 growth rings)", *X["wood"]), ("Bark", X["cambium"][1], X["cork"][1])):
        ax.plot([x0 + 0.03, x1 - 0.03], [y + 4.2, y + 4.2], color=P.muted(), lw=0.9)
        bio.label(ax, ((x0 + x1) / 2, y + 4.45), name, size="small")
    key = "vessel" if kind != "softwood" else "tracheid"
    bio.callout(ax, s[key], (3.0, y - 0.05), "Vessel" if kind != "softwood" else "Tracheids", size="small")
    bio.callout(ax, (s["ring_x"][1], y + 2.2), (7.0, y - 0.05), "Ring boundary", size="small")
    bio.callout(ax, s["ray"], (10.0, y - 0.05), "Ray", size="small")
    bio.callout(ax, s["cambium"], (13.0, y - 0.05), "Vascular cambium", size="small")
