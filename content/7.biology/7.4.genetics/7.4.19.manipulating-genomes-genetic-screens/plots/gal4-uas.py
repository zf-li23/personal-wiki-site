"""Binary expression with the GAL4/UAS system, drawn in SBOL Visual symbols: a driver transgene expressing
the yeast activator Gal4 under a tissue-specific enhancer, and a responder transgene carrying GFP behind
UAS sites. Only cells of offspring that have both transgenes and an active enhancer express the responder."""
import wikibio as bio
from wikibio import genetics as G

P = bio.P
fig, ax = bio.canvas(15.0, 8.4)

bio.label(ax, (0.7, 7.95), "Driver line", size="title", ha="left", bold=True)
d = G.construct(ax, 1.1, 6.9, [
    {"kind": "region", "text": "E", "width": 0.8},
    ("promoter", None),
    ("rbs", None),
    {"kind": "cds", "text": "GAL4", "token": "receptor", "width": 2.2, "italic": True},
    ("terminator", None),
], unit=0.62, gap=0.22)
bio.label(ax, (d[0]["centre"], d[0]["bottom"] - 0.35), "tissue-specific\nenhancer", size="tiny", va="top",
          color=P.muted())

bio.label(ax, (0.7, 3.35), "Responder line", size="title", ha="left", bold=True)
r = G.construct(ax, 1.1, 2.3, [
    {"kind": "operator", "text": "UAS", "width": 1.2},
    ("promoter", None),
    ("rbs", None),
    {"kind": "cds", "text": "gfp", "token": "positive", "width": 2.0, "italic": True},
    ("terminator", None),
], unit=0.62, gap=0.22)
bio.label(ax, (r[0]["centre"], r[0]["bottom"] - 0.35), "Gal4-binding\nsites", size="tiny", va="top", color=P.muted())

bio.protein(ax, (11.4, 5.4), 1.3, 0.7, "receptor", text="Gal4")
bio.arrow(ax, (d[3]["centre"] + 0.3, d[3]["top"] + 0.1), (11.0, 5.85), kind="process", bend=-0.2)
bio.arrow(ax, (10.8, 5.1), (r[0]["centre"] + 0.3, r[0]["top"] + 0.15), kind="activation", bend=-0.42)
bio.label(ax, (12.9, 6.9), "offspring that carry\nboth transgenes", size="small", color=P.muted())
bio.protein(ax, (r[3]["centre"], 0.85), 1.1, 0.7, "positive", text="GFP")
bio.arrow(ax, (r[3]["centre"], r[3]["bottom"] - 0.1), (r[3]["centre"], 1.25), kind="process")
bio.label(ax, (r[3]["centre"] + 2.9, 0.85), "only where the enhancer is active", size="small", color=P.muted())

bio.protein(ax, (12.4, 3.6), 1.5, 0.65, "neutral", text="Gal80$^{\\mathrm{ts}}$")
bio.arrow(ax, (12.0, 3.95), (11.6, 5.0), kind="inhibition", dashed=True)
bio.label(ax, (12.6, 2.7), "blocks Gal4 at 18 °C,\nreleases it at 29 °C", size="tiny", color=P.muted())
