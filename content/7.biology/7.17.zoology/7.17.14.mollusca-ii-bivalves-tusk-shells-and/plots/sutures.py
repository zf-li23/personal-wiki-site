# Suture lines of shelled cephalopods (wikibio.zoomorph.suture; schematic, aperture up) and the time ranges
# in which each type dominates (approximate: orthoceratitic in nautiloids, Ordovician-Recent; goniatitic,
# Devonian-Permian; ceratitic, mainly Middle-Late Triassic (from the Permian); ammonitic, mainly
# Jurassic-Cretaceous (from the Permian)). Below: the ICS periods (wikibio.phylo.geo_scale).
import wikibio as bio
from wikibio import phylo
from wikibio import zoomorph as zm

P = bio.P
fig, ax = bio.canvas(27, 12.4)
EX = [("orthoceratitic", "Orthoceratitic", "nautiloids", (485, 0), "neutral"),
      ("goniatitic", "Goniatitic", "goniatites", (410, 252), "dna"),
      ("ceratitic", "Ceratitic", "ceratites", (260, 201), "positive"),
      ("ammonitic", "Ammonitic", "ammonites", (270, 66), "negative")]
for i, (kind, title, ex, _, tok) in enumerate(EX):
    x0 = 0.9 + i * 6.6
    s = zm.suture(ax, (x0, 9.0), 5.4, kind, lobes=2, amplitude=1.05)
    bio.label(ax, (x0 + 2.7, 11.6), title, size="normal", bold=True)
    bio.label(ax, (x0 + 2.7, 11.1), ex, size="small", color=P.muted())
    if i == 1:
        bio.callout(ax, s["saddle"], (x0 + 3.7, 10.6), "Saddle", size="tiny")
        bio.callout(ax, s["lobe"], (x0 + 2.0, 7.3), "Lobe", size="tiny")
bio.arrow(ax, (26.4, 8.2), (26.4, 10.3), kind="process", head=0.2, lw=1.0)
bio.label(ax, (26.4, 7.9), "towards\naperture", size="tiny", va="top")

# time ranges
X0, X1, A0, A1 = 3.6, 26.2, 500, 0


def pos(a):
    return X0 + (A0 - a) / (A0 - A1) * (X1 - X0)


for i, (kind, title, ex, (old, young), tok) in enumerate(EX):
    y = 5.6 - i * 0.62
    ax.plot([pos(old), pos(young)], [y, y], color=P.edge(tok), lw=6, solid_capstyle="butt", zorder=5)
    bio.label(ax, (X0 - 0.2, y), title, size="small", ha="right")
bottom = phylo.geo_scale(ax, (X0, X1), (A0, A1), y=2.95, ranks=("period",), height=0.5)
for a in (500, 400, 300, 200, 100, 0):
    ax.plot([pos(a), pos(a)], [bottom, bottom - 0.12], color=P.muted(), lw=0.8)
    bio.label(ax, (pos(a), bottom - 0.35), f"{a}", size="tiny", color=P.muted())
bio.label(ax, ((X0 + X1) / 2, bottom - 0.85), "Millions of years ago", size="small")
