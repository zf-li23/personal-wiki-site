"""Glucose-stimulated insulin secretion by a pancreatic beta cell. (1) Glucose enters through a glucose
transporter (GLUT2 in rodents, mainly GLUT1 in humans), so the cytosolic concentration follows the blood.
(2) Glucokinase, with a high K0.5 and no product inhibition, phosphorylates it in proportion to the blood
glucose; glycolysis and mitochondrial oxidation raise [ATP]/[ADP]. (3) ATP closes the ATP-sensitive K+ channel
(Kir6.2 pore with SUR1 subunits; sulfonylureas close it, diazoxide and ADP open it). (4) The membrane
depolarizes, opening voltage-gated Ca2+ channels. (5) Ca2+ entry triggers exocytosis of insulin granules
(insulin and C peptide). Incretins (GLP-1, GIP) act through Gs-coupled receptors and cAMP (PKA, Epac2) to
amplify the Ca2+-triggered release, which is why they act only when glucose is high."""

import wikibio as bio
from wikibio import cellbio

P = bio.P
fig, ax = bio.canvas(22.0, 11.0)
ink, neg, pos = P.ink(), P.edge("negative"), P.edge("positive")
MY = 8.0
cellbio.sides(ax, (0.0, 22.0), MY, top="Blood (islet capillary)", bottom="β-cell cytosol", height=(3.0, 8.0),
              label_x=0.3)
bio.bilayer(ax, [(0, MY), (22, MY)])


def step(xy, n):
    bio.box(ax, xy, 0.62, 0.62, token="highlight", text=str(n), size="small", radius=0.31, zorder=30)


# 1 glucose transporter
gx = 2.6
cellbio.carrier(ax, gx, MY, open="out", token="channel", text="GLUT")
bio.molecule(ax, (gx, 10.2), "carbohydrate", text="Glc", r=0.38)
bio.arrow(ax, (gx, 9.75), (gx, 9.0), kind="process", color=ink)
bio.arrow(ax, (gx, 7.0), (gx, 6.1), kind="process", color=ink)
step((1.4, 9.4), 1)
bio.molecule(ax, (gx, 5.6), "carbohydrate", text="Glc", r=0.38)
bio.arrow(ax, (gx, 5.15), (gx, 4.2), kind="process", color=ink)
bio.label(ax, (gx - 0.25, 4.7), "glucokinase", size="tiny", color=P.edge("enzyme"), bold=True, ha="right")
bio.label(ax, (gx, 3.85), "G6P → glycolysis", size="tiny")
step((1.2, 4.2), 2)
bio.mitochondrion(ax, (5.6, 2.3), 3.2, 1.3, angle=8)
bio.arrow(ax, (3.6, 3.5), (4.4, 2.9), kind="process", color=ink)
bio.label(ax, (5.6, 0.9), "pyruvate → citric acid cycle → oxidative phosphorylation", size="tiny", color=P.muted())
bio.label(ax, (7.6, 4.6), "[ATP]/[ADP] ↑", size="normal", bold=True, color=P.edge("atp"))
bio.arrow(ax, (6.6, 3.1), (7.4, 4.2), kind="process", color=ink)

# 3 K_ATP channel
kx = 9.8
cellbio.channel(ax, kx, MY, token="k", text="")
bio.label(ax, (kx, 9.35), "K$_{\\mathrm{ATP}}$ channel (Kir6.2 + SUR1)", size="tiny", bold=True)
bio.ion(ax, (kx + 0.9, 9.0), "k")
bio.label(ax, (kx + 1.45, 9.0), "efflux stops", size="tiny", ha="left", color=neg)
bio.arrow(ax, (8.6, 5.0), (kx - 0.2, 7.2), kind="inhibition", color=neg, lw=1.8)
step((kx - 2.9, 9.35), 3)
bio.box(ax, (kx, 10.4), 3.4, 0.6, token="drug", text="sulfonylureas close it", size="tiny")

# 4 depolarization
bio.label(ax, (12.5, 6.1), "depolarization", size="small", bold=True, color=P.edge("channel"))
bio.arrow(ax, (10.9, 6.9), (14.2, 6.9), kind="activation", color=pos, lw=1.6, bg=P.fill("cytoplasm"))
step((11.0, 6.1), 4)

# 5 Ca channel and exocytosis
cx = 15.2
cellbio.channel(ax, cx, MY, token="ca", text="")
bio.label(ax, (cx, 10.45), "voltage-gated Ca²⁺ channel", size="tiny", bold=True)
cellbio.flux(ax, cx, 9.6, 6.2, species=[("ca", 3)], color=ink)
bio.label(ax, (cx + 0.5, 5.8), "[Ca²⁺] ↑", size="small", bold=True, color=P.edge("ca"))
step((cx - 2.3, 10.45), 5)
for i, (x, y) in enumerate([(16.8, 4.0), (18.0, 3.1), (15.9, 2.6), (19.0, 4.3), (17.3, 1.9), (19.3, 2.2)]):
    bio.vesicle(ax, (x, y), 0.45, token="vesicle", cargo="protein")
bio.label(ax, (17.6, 0.9), "insulin granules (insulin + C peptide)", size="tiny", color=P.muted())
bio.vesicle(ax, (18.6, 7.35), 0.45, token="vesicle", cargo="protein")
bio.arrow(ax, (18.0, 4.9), (18.5, 6.8), kind="process", color=ink)
bio.arrow(ax, (cx + 0.6, 5.6), (16.5, 4.6), kind="activation", color=pos, lw=1.4, bg=P.fill("cytoplasm"))
for k in range(5):
    bio.molecule(ax, (18.0 + 0.45 * k, 9.6 + 0.25 * (k % 2)), "protein", text="", r=0.14)
bio.label(ax, (19.4, 10.45), "insulin secreted", size="small", bold=True)

# incretin
rx = 21.0
bio.receptor(ax, rx, MY, "gpcr", token="receptor", text="GLP-1R")
bio.label(ax, (rx - 0.3, 5.7), "cAMP → PKA,\nEpac2: amplifies", size="tiny", color=P.edge("receptor"), ha="center")
bio.arrow(ax, (rx - 0.5, 5.1), (19.6, 4.6), kind="activation", color=pos, lw=1.4, bg=P.fill("cytoplasm"))
bio.label(ax, (rx, 9.6), "GLP-1, GIP", size="tiny", bold=True, color=P.edge("receptor"))
