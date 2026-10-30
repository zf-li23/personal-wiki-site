"""The growth plate (zones) and the Ihh-PTHrP feedback loop."""
import wikibio as bio
from wikibio import mesoderm as M

fig, ax = bio.canvas(22, 12)
P = bio.P
g = M.growth_plate(ax, (1.0, 0.6, 5.0, 10.6))
bio.panel(ax, "A", (0.3, 11.6))
names = {"epiphysis": "Epiphyseal bone", "resting": "Resting zone", "proliferative": "Proliferative zone",
         "prehypertrophic": "Prehypertrophic", "hypertrophic": "Hypertrophic zone", "metaphysis": "Ossification front, metaphysis"}
for z, t in names.items():
    y0, y1 = g["y_" + z]
    ax.plot([6.15, 6.15], [y0 + 0.05, y1 - 0.05], color=P.muted(), lw=1.0)
    bio.label(ax, (6.35, (y0 + y1) / 2), t, size="small", ha="left")
bio.panel(ax, "B", (11.0, 11.6))
X = 14.1
bx = {"pthrp": (X, 9.8), "prolif": (X, 7.2), "ihh": (X, 4.6), "hyp": (X, 2.0), "ob": (20.2, 4.6)}
txt = {"pthrp": "PTHrP (periarticular cells)", "prolif": "Proliferating chondrocytes", "ihh": "Prehypertrophic cells: Ihh",
       "hyp": "Hypertrophy", "ob": "Perichondrial\nosteoblasts"}
tok = {"pthrp": "positive", "prolif": "dna2", "ihh": "highlight", "hyp": "lipid", "ob": "bone"}
for k, c in bx.items():
    bio.box(ax, c, 5.2 if k != "ob" else 3.3, 1.1 if k != "ob" else 1.4, token=tok[k], text=txt[k], size="small")
bio.arrow(ax, (13.2, 9.2), (13.2, 7.8), kind="activation")
bio.label(ax, (13.05, 8.5), "keeps proliferating", size="tiny", ha="right", color=P.muted())
bio.arrow(ax, (13.2, 6.6), (13.2, 5.2), kind="process")
bio.label(ax, (13.05, 5.9), "cells leave PTHrP range", size="tiny", ha="right", color=P.muted())
bio.arrow(ax, (13.2, 4.0), (13.2, 2.6), kind="process")
bio.arrow(ax, (15.2, 5.2), (15.2, 6.6), kind="activation")
bio.label(ax, (15.35, 5.9), "proliferation", size="tiny", ha="left", color=P.muted())
bio.arrow(ax, (16.75, 4.9), (16.75, 9.7), kind="activation", bend=-0.3)
bio.label(ax, (18.0, 7.6), "raises PTHrP", size="tiny", ha="left", color=P.muted())
bio.arrow(ax, (16.75, 4.35), (18.5, 4.35), kind="activation")
bio.arrow(ax, (11.45, 9.7), (11.45, 2.2), kind="inhibition", bend=-0.18)
bio.label(ax, (10.2, 6.2), "delays hypertrophy", size="tiny", rotation=90, color=P.muted())
