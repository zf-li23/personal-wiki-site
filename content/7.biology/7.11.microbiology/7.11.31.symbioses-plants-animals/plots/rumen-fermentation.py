"""A: path of food through the ruminant stomach and the guilds of the rumen food web (schematic).
B: energy balance of the overall rumen fermentation (Eq. 31.1), from heats of combustion
(kJ/mol: glucose 2803, acetic 874, propionic 1527, butyric 2183, methane 890)."""
import numpy as np
import wikibio as bio
from wikibio import quant

P = bio.P
fig, ax = bio.canvas(26, 10)

# ---------------- A
bio.panel(ax, "A", (0.2, 9.8))
bio.box(ax, (2.0, 7.6), 2.6, 1.0, "plant", "feed", size="small")
bio.box(ax, (6.4, 7.6), 4.0, 1.6, "bacterium", "reticulorumen\n39 °C, pH 5.5–7, anoxic", size="small")
bio.box(ax, (11.0, 7.6), 2.4, 1.0, "neutral", "omasum", size="small")
bio.box(ax, (14.6, 7.6), 3.4, 1.0, "lysosome", "abomasum (acid)", size="small")
bio.arrow(ax, (3.3, 7.6), (4.4, 7.6), head=0.18)
bio.arrow(ax, (8.4, 7.6), (9.8, 7.6), head=0.18)
bio.arrow(ax, (12.2, 7.6), (12.9, 7.6), head=0.18)
bio.arrow(ax, (6.0, 8.4), (5.0, 8.4), bend=-0.9, head=0.16)
bio.label(ax, (5.5, 9.4), "rumination (cud, saliva HCO₃⁻)", size="tiny", color=P.muted())
bio.label(ax, (14.6, 6.6), "microbial cells digested\n→ protein, vitamins", size="tiny", color=P.muted())

# food web
y1, y2, y3 = 4.6, 2.9, 1.2
bio.box(ax, (2.6, y1), 4.4, 0.9, "carbohydrate", "cellulose, hemicellulose, starch", size="tiny")
bio.box(ax, (2.6, y2), 4.4, 0.9, "enzyme", "fibrolytic & amylolytic bacteria,\nfungi, ciliates", size="tiny")
bio.arrow(ax, (2.6, y1 - 0.45), (2.6, y2 + 0.45), head=0.15)
bio.box(ax, (8.6, y2), 3.6, 0.9, "metabolite", "succinate, lactate", size="tiny")
bio.box(ax, (8.6, y1), 3.6, 0.9, "lipid", "acetate, propionate,\nbutyrate (SCFA)", size="tiny")
bio.box(ax, (8.6, y3), 3.6, 0.9, "h", "H₂ + CO₂", size="tiny")
bio.arrow(ax, (4.8, y2), (6.8, y2), head=0.15)
bio.arrow(ax, (4.8, y2 + 0.3), (6.8, y1 - 0.2), head=0.15)
bio.arrow(ax, (4.8, y2 - 0.3), (6.8, y3 + 0.2), head=0.15)
bio.arrow(ax, (8.6, y2 + 0.45), (8.6, y1 - 0.45), head=0.15)
bio.label(ax, (9.0, (y1 + y2) / 2), "secondary\nfermenters", size="tiny", ha="left", color=P.muted())
bio.box(ax, (14.0, y3), 3.4, 0.9, "virus", "methanogens → CH₄", size="tiny")
bio.arrow(ax, (10.4, y3), (12.3, y3), head=0.15)
bio.label(ax, (14.0, y3 + 0.85), "eructation", size="tiny", color=P.muted())
bio.box(ax, (14.0, y1), 3.4, 0.9, "blood", "absorbed by rumen wall", size="tiny")
bio.arrow(ax, (10.4, y1), (12.3, y1), head=0.15)

# ---------------- B: energy balance
bio.panel(ax, "B", (17.6, 9.8))
glc = 57.5 * 2803
parts = [("acetate", 65 * 874, "lipid"), ("propionate", 20 * 1527, "metabolite"),
         ("butyrate", 15 * 2183, "enzyme"), ("methane", 35 * 890, "virus")]
heat = glc - sum(v for _, v, _ in parts)
parts.append(("heat, microbial ATP", heat, "neutral"))
x0, w = 20.0, 2.0
yb, H = 1.4, 7.2
y = yb
for name, v, tok in parts:
    h = H * v / glc
    bio.shape(ax, [(x0, y), (x0 + w, y), (x0 + w, y + h), (x0, y + h)], token=tok, lw=0.8)
    bio.label(ax, (x0 + w + 0.25, y + h / 2), f"{name} {100 * v / glc:.1f} %", size="tiny", ha="left")
    y += h
bio.label(ax, (x0 + w / 2, yb - 0.45), "energy of fermented glucose", size="tiny")
bio.label(ax, (x0 + w / 2, yb + H + 0.4), "100 %", size="tiny")
