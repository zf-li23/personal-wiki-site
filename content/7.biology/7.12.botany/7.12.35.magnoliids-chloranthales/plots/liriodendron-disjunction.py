# The eastern Asia - eastern North America disjunction of the tulip trees (Liriodendron), drawn on a
# simplified longitude-latitude map of the Northern Hemisphere (coastlines strongly generalised). Filled
# areas: approximate ranges of the two living species, L. chinense (southern China, northern Vietnam)
# and L. tulipifera (eastern North America). Triangles: examples of Late Cretaceous to Neogene fossil
# localities of the genus (western North America, Greenland, Iceland, Europe, Japan), showing that it was
# once widespread across the Northern Hemisphere.
import numpy as np
import wikibio as bio

P = bio.P
LON0, LON1, LAT0, LAT1 = -170.0, 180.0, 0.0, 84.0
X0, X1, Y0, Y1 = 1.0, 35.0, 1.4, 9.6


def xy(lon, lat):
    return (X0 + (lon - LON0) / (LON1 - LON0) * (X1 - X0), Y0 + (lat - LAT0) / (LAT1 - LAT0) * (Y1 - Y0))


LAND = {
    "N America": [(-168, 66), (-160, 70), (-140, 70), (-125, 72), (-95, 72), (-80, 73), (-75, 68), (-62, 60),
                  (-56, 52), (-66, 45), (-70, 42), (-76, 35), (-81, 31), (-80, 25), (-82, 28), (-85, 30), (-90, 29),
                  (-97, 27), (-97, 22), (-92, 18), (-87, 21), (-88, 16), (-83, 10), (-78, 8), (-80, 8), (-85, 11),
                  (-92, 15), (-105, 20), (-110, 24), (-115, 30), (-118, 34), (-124, 40), (-124, 48), (-130, 55),
                  (-140, 60), (-150, 60), (-160, 58), (-165, 62)],
    "Greenland": [(-55, 60), (-45, 60), (-35, 66), (-22, 70), (-18, 77), (-25, 82), (-45, 83), (-60, 82), (-70, 78),
                  (-58, 75), (-53, 70)],
    "Iceland": [(-24, 64), (-22, 66), (-15, 66.5), (-13, 65), (-18, 63.5)],
    "Eurasia": [(-10, 36), (-9, 43), (-2, 44), (-5, 48), (-2, 49), (5, 53), (8, 57), (5, 62), (12, 66), (20, 70),
                (30, 71), (40, 68), (50, 69), (60, 70), (70, 73), (80, 73), (100, 77), (110, 76), (130, 72), (140, 72),
                (160, 70), (180, 68), (180, 65), (170, 60), (163, 58), (160, 53), (155, 57), (140, 54), (135, 44),
                (129, 41), (126, 37), (122, 40), (118, 38), (122, 32), (121, 28), (117, 24), (110, 21), (108, 16),
                (106, 10), (103, 9), (100, 13), (98, 8), (103, 1), (99, 4), (98, 16), (94, 17), (92, 22), (88, 22),
                (80, 15), (77, 8), (73, 17), (68, 23), (60, 25), (56, 27), (52, 24), (56, 18), (52, 15), (44, 12),
                (40, 20), (35, 28), (34, 31), (36, 36), (30, 36), (26, 40), (23, 36), (20, 40), (15, 38), (12, 44),
                (6, 43), (3, 42), (0, 38), (-6, 36)],
    "Japan": [(130, 31), (132, 34), (135, 34), (140, 36), (141, 41), (140, 45), (143, 44), (145, 43), (141, 38),
              (140, 35), (136, 33), (131, 33)],
    "Africa": [(-17, 21), (-13, 28), (-6, 36), (10, 37), (11, 33), (20, 31), (32, 31), (34, 28), (43, 12), (51, 11),
               (48, 5), (42, 0), (10, 0), (9, 4), (-8, 4), (-15, 10), (-17, 15)],
    "S America": [(-80, 0), (-78, 8), (-72, 12), (-62, 11), (-52, 5), (-50, 0)],
}
RANGES = {
    "L. chinense": [(103, 24), (106, 22), (110, 22.5), (115, 24), (119, 26), (121, 29), (120, 31.5), (115, 31.8),
                    (110, 32), (105, 31), (103, 28)],
    "L. tulipifera": [(-92, 32), (-88, 30), (-84, 29), (-81, 30), (-79, 33), (-76, 37), (-73, 41), (-72, 43),
                      (-76, 43.5), (-80, 42.5), (-84, 42), (-88, 40), (-91, 37)],
}
FOSSILS = [(-116, 47), (-121, 45), (-50, 70), (-20, 65), (10, 51), (2, 47), (25, 45), (138, 37)]

fig, ax = bio.canvas(36, 11.2)
for lat in (0, 20, 40, 60, 80):
    ax.plot([X0, X1], [xy(0, lat)[1]] * 2, color=P.muted(), lw=0.4, alpha=0.5, zorder=1)
    bio.label(ax, (X0 - 0.15, xy(0, lat)[1]), f"{lat}°N", size="tiny", ha="right", color=P.muted())
for lon in range(-150, 181, 30):
    ax.plot([xy(lon, 0)[0]] * 2, [Y0, Y1], color=P.muted(), lw=0.4, alpha=0.5, zorder=1)
for name, pts in LAND.items():
    ax.fill(*zip(*[xy(*p) for p in pts]), facecolor=P.fill("neutral"), edgecolor=P.edge("neutral"), lw=0.8, zorder=2)
for name, pts in RANGES.items():
    ax.fill(*zip(*[xy(*p) for p in pts]), facecolor=P.fill("plant"), edgecolor=P.edge("plant"), lw=1.3, zorder=4)
for p in FOSSILS:
    ax.scatter(*xy(*p), marker="^", s=60, facecolor=P.fill("highlight"), edgecolor=P.edge("highlight"), lw=1.0,
               zorder=5)
bio.callout(ax, xy(112, 27), (29.2, 3.0), r"$\it{L.\ chinense}$", size="small")
bio.callout(ax, xy(-82, 36), (6.8, 3.2), r"$\it{L.\ tulipifera}$", size="small")
ax.add_patch(__import__("matplotlib").patches.Rectangle((1.2, 10.25), 0.5, 0.35, facecolor=P.fill("plant"),
                                                         edgecolor=P.edge("plant"), lw=1.0))
bio.label(ax, (1.9, 10.42), "Living species", size="small", ha="left")
ax.scatter([7.3], [10.42], marker="^", s=60, facecolor=P.fill("highlight"), edgecolor=P.edge("highlight"))
bio.label(ax, (7.7, 10.42), "Cretaceous-Neogene fossils (examples)", size="small", ha="left")
