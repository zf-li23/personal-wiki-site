"""Numbers of described and accepted species in the main groups of plants, on a logarithmic axis.

Data: Christenhusz & Byng (2016), Phytotaxa 261: 201-217 (counts of accepted species, not estimates
of the total). Their "algae" is a broad count of green, red and other photosynthetic eukaryotic
algae; fungi are not included in their total. Bars are grouped as non-vascular and vascular plants.
"""

import wikibio as bio
from wikibio import charts

P = bio.P
FONT = bio.core.FONT
fig, ax = bio.canvas(16.0, 9.6)
a = charts.axes_at(ax, (5.2, 1.3, 9.6, 7.6))

rows = [
    ("Algae (broad sense)", 44000, "chloroplast", "phylopic/ulva"),
    ("Hornworts", 225, "plant", "phylopic/hornwort"),
    ("Liverworts", 9000, "plant", "phylopic/liverwort"),
    ("Mosses", 12700, "plant", "phylopic/moss"),
    ("Lycophytes", 1290, "positive", "phylopic/clubmoss"),
    ("Ferns", 10560, "positive", "phylopic/fern"),
    ("Gymnosperms", 1079, "positive", "phylopic/pine"),
    ("Angiosperms", 295383, "petal", "phylopic/magnolia"),
]
labels = []
for i, (name, n, tok, _) in enumerate(rows):
    y = len(rows) - 1 - i
    a.barh(y, n, height=0.62, color=P.fill(tok), edgecolor=P.edge(tok), lw=1.0)
    a.text(n * 1.18, y, f"{n:,}", va="center", fontsize=FONT["small"], color=P.ink())
    labels.append(name)
a.set_xscale("log")
a.set_xlim(100, 3e6)
a.set_yticks(range(len(rows)))
a.set_yticklabels(labels[::-1], fontsize=FONT["small"])
a.set_ylim(-0.6, len(rows) - 0.4)
a.axhline(3.5, color=P.muted(), lw=0.6, ls=":")
charts.style_axes(a, "accepted species (log scale)")
a.text(2.2e6, 3.62, "non-vascular plants", ha="right", va="bottom", fontsize=FONT["small"], color=P.muted())
a.text(2.2e6, 3.38, "vascular plants: 308,312 in total", ha="right", va="top", fontsize=FONT["small"], color=P.muted())

# silhouettes beside the labels (literal ids for the build)
icons = ["phylopic/ulva", "phylopic/hornwort", "phylopic/liverwort", "phylopic/moss", "phylopic/clubmoss",
         "phylopic/fern", "phylopic/pine", "phylopic/magnolia"]
y0, y1 = 1.3, 1.3 + 7.6
step = (y1 - y0) / len(rows)
for i, (name, n, tok, ic) in enumerate(rows):
    yc = y1 - (i + 0.5) * step
    bio.icon(ax, ic, at=(1.4, yc), height=0.72, color=tok)
bio.label(ax, (8.0, 9.35), "Known plant species: about 374,000 (Christenhusz & Byng 2016)", size="small",
          color=P.muted())
