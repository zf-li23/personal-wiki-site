# Whittaker biome diagram (schematic, after Whittaker 1975 and Ricklefs 2008).
# Biome regions are defined by simple boundaries in (mean annual temperature, annual precipitation)
# space and drawn as a classified raster; the upper-left envelope is the limit of observed climates.
# Points: approximate 1991-2020 climate normals of five Chinese cities (rounded).
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap, BoundaryNorm
from matplotlib.patches import Patch
import wikibio as bio

P = bio.P

BIOMES = [  # (name, token)
    ("Tundra", "neutral"),
    ("Boreal forest", "enzyme"),
    ("Temperate grassland / desert", "lipid"),
    ("Woodland / shrubland", "antibody"),
    ("Temperate seasonal forest", "plant"),
    ("Temperate rain forest", "channel"),
    ("Subtropical desert", "membrane"),
    ("Tropical seasonal forest / savanna", "rna"),
    ("Tropical rain forest", "thylakoid"),
]


def envelope(T):
    # upper limit of annual precipitation (cm) observed at a given mean annual temperature
    return np.interp(T, [-15, -5, 4, 10, 20, 24, 30], [25, 90, 210, 300, 420, 450, 450])


def classify(T, Pc):
    c = np.full(T.shape, np.nan)
    tundra = T < -5
    boreal = (T >= -5) & (T < 4)
    temp = (T >= 4) & (T < 20)
    trop = T >= 20
    c[tundra] = 0
    c[boreal & (Pc >= 25)] = 1
    c[boreal & (Pc < 25)] = 2
    g = 30 + 1.0 * (T - 4)
    w = 70 + 2.5 * (T - 4)
    c[temp & (Pc < g)] = 2
    c[temp & (Pc >= g) & (Pc < w)] = 3
    c[temp & (Pc >= w) & (Pc < 220)] = 4
    c[temp & (Pc >= 220)] = 5
    c[trop & (Pc < 60)] = 6
    c[trop & (Pc >= 60) & (Pc < 200)] = 7
    c[trop & (Pc >= 200)] = 8
    c[Pc > envelope(T)] = np.nan
    return c


T = np.linspace(-15, 30, 451)
Pc = np.linspace(0, 460, 461)
TT, PP = np.meshgrid(T, Pc)
C = classify(TT, PP)

cmap = ListedColormap([P.fill(tok) for _, tok in BIOMES])
norm = BoundaryNorm(np.arange(-0.5, len(BIOMES)), len(BIOMES))
fig, ax = plt.subplots(figsize=(9.6, 5.6))
ax.pcolormesh(T, Pc, np.ma.masked_invalid(C), cmap=cmap, norm=norm, shading="auto", rasterized=True)
ax.contour(T, Pc, np.nan_to_num(C, nan=-1), levels=np.arange(-0.5, len(BIOMES)), colors=[P.muted()],
           linewidths=0.6)
ax.plot(T, envelope(T), color=P.ink(), lw=1.2)

cities = [("Harbin", 4.9, 53), ("Beijing", 12.9, 57), ("Urumqi", 7.3, 29), ("Wuhan", 17.0, 127),
          ("Guangzhou", 22.6, 185)]
for name, t, p in cities:
    ax.plot(t, p, "o", ms=5, color=P.ink(), mec=P.surface(), mew=0.8, zorder=5)
    ax.annotate(name, (t, p), xytext=(5, 4), textcoords="offset points", fontsize=8, color=P.ink())

ax.set_xlim(-15, 30)
ax.set_ylim(0, 460)
ax.set_xlabel("Mean annual temperature / °C")
ax.set_ylabel("Annual precipitation / cm")
for s in ("top", "right"):
    ax.spines[s].set_visible(False)
handles = [Patch(facecolor=P.fill(tok), edgecolor=P.edge(tok), label=name) for name, tok in BIOMES]
ax.legend(handles=handles, frameon=False, fontsize=8, loc="upper left", bbox_to_anchor=(1.01, 1.0))
fig.tight_layout()
