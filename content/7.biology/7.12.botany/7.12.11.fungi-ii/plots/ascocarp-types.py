"""The four types of ascomata in median section: apothecium, perithecium, cleistothecium (with
appendages, as in powdery mildews) and ascostroma (pseudothecium) with bitunicate asci."""
import wikibio as bio
from wikibio import plant

P = bio.P
fig, ax = bio.canvas(26, 9.6)
items = [("apothecium", "A", "Apothecium", (3.2, 5.6), 5.2,
          [("hymenium", (0.4, 8.6), "Hymenium"), ("excipulum", (0.6, 2.2), "Excipulum")]),
         ("perithecium", "B", "Perithecium", (9.6, 5.2), 5.0,
          [("ostiole", (11.8, 8.6), "Ostiole"), ("ascus", (12.2, 3.0), "Ascus")]),
         ("cleistothecium", "C", "Cleistothecium", (15.8, 5.4), 3.6,
          [("appendage", (18.2, 8.6), "Appendage"), ("ascus", (18.4, 2.6), "Ascus")]),
         ("pseudothecium", "D", "Ascostroma (pseudothecium)", (22.4, 5.2), 4.6,
          [("stroma_pt", (25.6, 8.6), "Stroma"), ("locule", (25.6, 2.4), "Locule")])]
for kind, letter, name, c, size, calls in items:
    a = plant.ascocarp(ax, c, size, kind=kind)
    bio.panel(ax, letter, (c[0] - 3.0, 9.4))
    bio.label(ax, (c[0], 0.6), name, size="small", bold=True)
    a["stroma_pt"] = (c[0] - 1.6, c[1] - 0.6)
    for key, xy, txt in calls:
        if key in a:
            bio.callout(ax, a[key], xy, txt)
