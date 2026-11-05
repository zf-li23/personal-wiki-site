"""Types of sori and indusia in ferns: pinnules seen from below (abaxial side). Green: lamina; light brown:
sporangia; cream: indusia (true or false)."""
import wikibio as bio
from wikibio import plant

P = bio.P
fig, ax = bio.canvas(17, 15.6)
rows = [
    [("round", None, "Round, naked", "Polypodium, Pyrrosia"), ("round", "reniform", "Reniform indusium", "Dryopteris"),
     ("round", "peltate", "Peltate indusium", "Cyrtomium, Polystichum"), ("linear", "linear", "Linear indusium", "Asplenium"),
     ("costal", "linear", "Costal, opening inward", "Blechnum")],
    [("marginal", "false", "Marginal, false indusium", "Pteris"), ("terminal", "cup", "Vein ends, cup", "Dennstaedtia"),
     ("terminal", "false", "Reflexed flaps", "Adiantum"), ("acrostichoid", None, "Covering the lamina", "Acrostichum")],
]
for r, row in enumerate(rows):
    y = 8.8 - r * 7.8
    for i, (s, ind, t, g) in enumerate(row):
        x = 1.7 + i * 3.4 + (1.7 if r == 1 else 0)
        plant.pinnule(ax, (x, y), 5.0, angle=90, sorus=s, indusium=ind)
        bio.label(ax, (x, y - 0.4), t, size="tiny")
        bio.label(ax, (x, y - 0.85), g, size="tiny", italic=True, color=P.muted())
