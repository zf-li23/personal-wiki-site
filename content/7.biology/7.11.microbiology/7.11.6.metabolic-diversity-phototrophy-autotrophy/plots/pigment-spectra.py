"""In vivo absorption maxima of the photosynthetic pigments of bacteria (schematic).

Each row is one pigment (or pigment-protein) as found in living cells; bands are drawn as Gaussians at the
in vivo maxima given by Madigan et al. (2019): chlorophyll a 430 and 680 nm; bacteriochlorophyll a (purple
bacteria) about 360, 590, 805 and 870 nm; bacteriochlorophyll b 835-850 and 1020-1040 nm; bacteriochlorophyll
c 745-755 nm, d 705-740 nm, e 719-726 nm (green sulfur bacteria, chlorosomes); bacteriochlorophyll g
(heliobacteria) 670 and 788 nm; carotenoids 450-550 nm; phycoerythrin 550, phycocyanin 620 and
allophycocyanin 650 nm. Band widths and relative heights are illustrative; only the peak positions are data.
Bacteriochlorophylls c, d, e also absorb in the blue (Soret band, near 430-470 nm), drawn as a smaller band.
"""
import numpy as np

import wikibio as bio
from wikibio import quant

P = bio.P
fig, ax = bio.canvas(16.0, 12.6)

rows = [
    # label, owner, token, [(peak nm, width nm, height)]
    ("Chlorophyll a", "cyanobacteria, algae", "thylakoid", [(430, 18, 1.0), (680, 14, 0.75)]),
    ("Phycoerythrin", "cyanobacteria, red algae", "petal", [(550, 22, 1.0)]),
    ("Phycocyanin", "cyanobacteria", "channel", [(620, 20, 1.0)]),
    ("Allophycocyanin", "cyanobacteria", "dna", [(650, 12, 1.0)]),
    ("Carotenoids", "all phototrophs", "lipid_head", [(455, 18, 0.8), (485, 18, 1.0), (520, 18, 0.7)]),
    ("Bacteriochlorophyll a", "purple bacteria", "protein", [(360, 16, 0.9), (590, 14, 0.3), (805, 14, 0.7), (870, 20, 1.0)]),
    ("Bacteriochlorophyll b", "some purple bacteria", "receptor", [(840, 12, 0.6), (1030, 22, 1.0)]),
    ("Bacteriochlorophyll g", "heliobacteria", "anther", [(670, 14, 0.45), (788, 16, 1.0)]),
    ("Bacteriochlorophyll c", "green sulfur bacteria", "plant", [(455, 22, 0.55), (750, 20, 1.0)]),
    ("Bacteriochlorophyll d", "green sulfur bacteria", "carbohydrate", [(440, 22, 0.55), (725, 20, 1.0)]),
    ("Bacteriochlorophyll e", "brown green sulfur bacteria", "animal", [(465, 24, 0.55), (722, 18, 1.0)]),
]

x0, w = 5.2, 10.3
top, rh = 11.4, 0.92
p = quant.Plot(ax, (x0, top - rh * len(rows), w, rh * len(rows)), xlim=(330, 1080), ylim=(0, len(rows)),
               xlabel="wavelength / nm", xticks=[400, 500, 600, 700, 800, 900, 1000], frame="l", grid=False)
lam = np.linspace(330, 1080, 1200)
for i, (name, owner, tok, bands) in enumerate(rows):
    base = len(rows) - 1 - i
    y = np.zeros_like(lam)
    for c, s, h in bands:
        y += h * np.exp(-0.5 * ((lam - c) / s) ** 2)
    y = 0.82 * y / y.max()
    p.band(lam, np.full_like(lam, base), base + y, token=tok, alpha=0.55)
    p.line(lam, base + y, tok, lw=1.3)
    if name == "Carotenoids":
        p.text(485, base + 0.92, "450-550", size="tiny", token=tok, va="bottom")
        bands = []
    for c, s, h in bands:
        if h >= 0.6:
            yy = base + 0.82 * h / max(b[2] for b in bands)
            p.text(c + s + 4, min(yy, base + 0.82) - 0.05, f"{c}", size="tiny", token=tok, va="bottom", ha="left")
    yc = p.Y(base + 0.38)
    bio.label(ax, (x0 - 0.25, yc + 0.14), name, size="small", ha="right", color=P.edge(tok))
    bio.label(ax, (x0 - 0.25, yc - 0.22), owner, size="tiny", ha="right", color=P.muted())

# visible / near-infrared divide
xv = p.X(700)
ax.plot([xv, xv], [p.Y(0), p.Y(len(rows))], color=P.muted(), lw=0.7, ls=(0, (3, 3)), zorder=4)
bio.label(ax, (p.X(520), top + 0.55), "visible", size="small", color=P.muted())
bio.label(ax, (p.X(890), top + 0.55), "near infrared", size="small", color=P.muted())
