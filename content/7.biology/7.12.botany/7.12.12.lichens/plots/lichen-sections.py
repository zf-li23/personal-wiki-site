"""Transverse sections of lichen thalli (cell by cell, schematic). A: heteromerous (stratified) thallus with
a green-algal photobiont. B: homoiomerous thallus with Nostoc chains in a gelatinous matrix."""
import wikibio as bio
from wikibio import botany as B

fig, ax = bio.canvas(30, 9)
bio.panel(ax, "A", (0.2, 8.8))
L = B.lichen_section(ax, (0.5, 0.5, 13.5, 7.8))
for k, y, t in [("upper_cortex", 7.6, "Upper cortex"), ("algal_layer", 6.4, "Photobiont layer (green alga)"),
                ("medulla", 4.8, "Medulla"), ("lower_cortex", 3.2, "Lower cortex"), ("rhizine", 1.4, "Rhizine")]:
    bio.callout(ax, L[k], (14.2, y), t)
bio.panel(ax, "B", (20.0, 8.8))
H = B.lichen_section(ax, (20.5, 2.6, 29.5, 7.8), kind="homoiomerous")
for k, xy, t in [("photobiont", (25.0, 1.6), "Nostoc chains"), ("hypha", (21.0, 1.6), "Hyphae"),
                 ("matrix", (28.8, 1.6), "Gelatinous matrix")]:
    if k in H:
        bio.callout(ax, H[k], xy, t)
