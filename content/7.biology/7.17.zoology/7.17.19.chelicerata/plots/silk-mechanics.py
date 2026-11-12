# Mechanical properties of spider silks compared with other biological and synthetic materials: tensile
# strength against breaking strain (extensibility), log scales; toughness (energy to break per volume,
# MJ m^-3) written next to each point. Data: Gosline et al. (1999) J. Exp. Biol. 202: 3295, Table 1;
# Darwin's bark spider dragline: Agnarsson et al. (2010) PLoS ONE 5: e11234. Spider dragline (major
# ampullate) silk combines a strength near that of steel with a much larger extensibility, so its toughness
# exceeds that of Kevlar; the capture-spiral (viscid) silk is weaker but stretches about threefold.
import numpy as np
import wikibio as bio
from wikibio import quant

P = bio.P
fig, ax = bio.canvas(16, 10)
data = [  # name, strength GPa, extensibility, toughness MJ m^-3, token, dx, dy (label offsets in canvas units)
    ("Dragline silk ($\\it{Araneus}$)", 1.1, 0.27, 160, "blood", 0.15, 0.25),
    ("Dragline silk ($\\it{Caerostris}$)", 1.6, 0.52, 354, "blood", 0.15, 0.25),
    ("Viscid silk ($\\it{Araneus}$)", 0.5, 2.7, 150, "blood", -0.15, 0.3),
    ("Silkworm silk ($\\it{Bombyx}$)", 0.6, 0.18, 70, "rna", 0.15, -0.3),
    ("Tendon collagen", 0.15, 0.12, 7.5, "enzyme", 0.15, 0.0),
    ("Bone", 0.16, 0.03, 4, "enzyme", 0.15, 0.0),
    ("Elastin", 0.002, 1.5, 2, "enzyme", 0.15, 0.0),
    ("Nylon 6.6", 0.95, 0.18, 80, "neutral", -0.15, 0.3),
    ("Kevlar 49", 3.6, 0.027, 50, "neutral", 0.15, 0.0),
    ("High-tensile steel", 1.5, 0.008, 6, "neutral", 0.15, 0.0),
    ("Synthetic rubber", 0.05, 8.5, 100, "neutral", -0.15, 0.3),
]
p = quant.Plot(ax, (1.8, 1.4, 13.4, 8.0), xlim=(0.005, 15), ylim=(0.001, 6), xlog=True, ylog=True,
               xlabel="Breaking strain (extensibility)", ylabel="Tensile strength / GPa",
               xticks=[0.01, 0.1, 1, 10], yticks=[0.001, 0.01, 0.1, 1])
for name, s, e, t, tok, dx, dy in data:
    p.points([e], [s], tok, r=0.13)
    x, y = p.xy(e, s)
    ha = "left" if dx > 0 else "right"
    bio.label(ax, (x + dx, y + dy), f"{name}: {t:g}", size="tiny", ha=ha)
for tok, txt, k in (("blood", "spider silks", 0), ("rna", "insect silk", 1), ("enzyme", "animal tissues", 2), ("neutral", "synthetic", 3)):
    p.points([0.01], [0.03 / 2.3 ** k], tok, r=0.13)
    x, y = p.xy(0.01, 0.03 / 2.3 ** k)
    bio.label(ax, (x + 0.25, y), txt, size="small", ha="left")
bio.label(ax, (9.0, 9.7), "Numbers: toughness / MJ m⁻³", size="small", color=P.muted())
