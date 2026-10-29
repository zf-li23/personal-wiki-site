"""Dorso-ventral patterning of the spinal cord (transverse section, dorsal up). (A) The roof plate (and, earlier,
the epidermis) secretes BMPs and Wnts; the notochord and then the floor plate secrete Sonic hedgehog. Progenitors
in the ventricular zone form eleven domains, each producing one class of neuron: dP1-dP6 the dorsal interneurons
dI1-dI6, p0-p3 the ventral interneurons V0-V3 and pMN the motor neurons. (B) The code of transcription factors in
the ventral domains: class I genes (Pax6, Irx3, Dbx1, Dbx2) are repressed by Shh signalling, class II genes (Nkx2.2,
Olig2, Nkx6.1) are induced by it; each pair of mutually repressing factors (Nkx2.2-Pax6, Olig2-Irx3, Nkx6.1-Dbx2)
sharpens a boundary. The dorsal domains express Pax3 (all) and Pax7 (dP3-dP6)."""
import wikibio as bio
from wikibio import neurodev as N

fig, ax = bio.canvas(22, 12.2)
P = bio.P
cy, H = 6.5, 8.2
d = N.neural_tube_domains(ax, (4.2, cy), H)
bio.panel(ax, "A", (0.2, 12.0))
names = [n for n, _, _ in N.DV_DOMAINS]
neuron = {"dP1": "dI1", "dP2": "dI2", "dP3": "dI3", "dP4": "dI4", "dP5": "dI5", "dP6": "dI6", "p0": "V0", "p1": "V1",
          "p2": "V2", "pMN": "MN", "p3": "V3"}
xr = d["right"]
for n in names:
    y = d[n][1]
    ax.plot([d[n][0], xr + 0.3], [y, y], color=P.muted(), lw=0.45, zorder=19)
    bio.label(ax, (xr + 0.38, y), n, size="tiny", ha="left")
    bio.label(ax, (xr + 1.25, y), neuron[n], size="tiny", ha="left", color=P.muted())
bio.label(ax, (xr + 0.6, d["top"][1] + 0.2), "domain", size="tiny", color=P.muted())
bio.label(ax, (xr + 1.5, d["top"][1] + 0.2), "neurons", size="tiny", color=P.muted())
# signals
xt = d["roof"][0]
bio.label(ax, (xt, d["top"][1] + 0.95), "BMP, Wnt", size="small", bold=True, color=P.edge("atp"))
bio.arrow(ax, (xt - 0.9, d["top"][1] + 0.1), (xt - 0.9, cy + 1.2), kind="activation", color=P.edge("atp"), lw=1.2)
bio.label(ax, (xt + 1.5, d["notochord"][1]), "Shh", size="small", bold=True, color=P.edge("drug"))
bio.arrow(ax, (xt + 1.0, d["bottom"][1] - 0.1), (xt + 1.0, cy - 1.4), kind="activation", color=P.edge("drug"), lw=1.2)
bio.callout(ax, d["roof"], (xt - 2.4, d["top"][1] + 0.4), "Roof plate")
bio.callout(ax, d["floor"], (xt - 2.4, d["bottom"][1] - 0.2), "Floor plate")
bio.callout(ax, d["notochord"], (xt - 2.0, d["notochord"][1] - 0.6), "Notochord")
bio.callout(ax, d["mantle"], (xt - 2.9, cy + 0.6), "Mantle (neurons)")
bio.callout(ax, (xt + 0.55, cy + 0.5), (xt - 2.9, cy + 1.6), "Ventricular zone")

# (B) transcription factor code
bio.panel(ax, "B", (11.6, 12.0))
yt, yb = cy + 0.40 * H, cy - 0.40 * H
h = (yt - yb) / sum(r for _, _, r in N.DV_DOMAINS)
rng = {}
y = yt
for n, _, r in N.DV_DOMAINS:
    rng[n] = (y - r * h, y)
    y -= r * h
for n in names:
    a, b = rng[n]
    ax.plot([12.2, 21.6], [a, a], color=P.muted(), lw=0.4, ls=":", zorder=2)
    bio.label(ax, (12.0, (a + b) / 2), n, size="tiny", ha="right")
genes = [("Pax3", "dP1", "dP6", "k", "dorsal"), ("Pax7", "dP3", "dP6", "k", "dorsal"), ("Dbx1", "p0", "p0", "neutral", "I"),
         ("Dbx2", "p0", "p1", "neutral", "I"), ("Irx3", "dP1", "p2", "neutral", "I"), ("Pax6", "dP1", "pMN", "neutral", "I"),
         ("Nkx6.1", "p2", "p3", "positive", "II"), ("Olig2", "pMN", "pMN", "positive", "II"), ("Nkx2.2", "p3", "p3", "positive", "II")]
for k, (g, top, bot, tok, cls) in enumerate(genes):
    x = 12.8 + k * 1.0
    y1, y0 = rng[top][1], rng[bot][0]
    bio.box(ax, (x, (y0 + y1) / 2), 0.5, y1 - y0 - 0.04, token=tok, radius=0.12)
    bio.label(ax, (x, yt + 0.55), g, size="tiny", italic=True, rotation=60, ha="left", va="bottom")
bio.label(ax, (15.3, yb - 0.6), "class I (repressed by Shh)", size="tiny", color=P.muted())
bio.label(ax, (19.8, yb - 0.6), "class II (induced)", size="tiny", color=P.edge("positive"))
