"""Succession of the late Cenozoic mammal faunas of China (after Zhang Rongzu's scheme, as summarized in
Chinese zoology textbooks). Time runs upward; the intervals are not to scale.
"""

import wikibio as bio

P = bio.P

fig, ax = bio.canvas(18, 13)

# time column
EPOCHS = [("Pliocene\n(5.3-2.6 Ma)", 0.6, 2.4), ("Early Pleistocene\n(2.6-0.77 Ma)", 2.4, 4.8),
          ("Middle Pleistocene\n(0.77-0.13 Ma)", 4.8, 7.2), ("Late Pleistocene\n(0.13-0.012 Ma)", 7.2, 9.6),
          ("Holocene", 9.6, 11.6)]
for name, y0, y1 in EPOCHS:
    ax.plot([0.3, 17.7], [y0, y0], color=P.muted(), lw=0.6, ls=":")
    bio.label(ax, (0.4, (y0 + y1) / 2), name, size="tiny", ha="left", color=P.muted())
ax.plot([0.3, 17.7], [11.6, 11.6], color=P.muted(), lw=0.6, ls=":")
bio.label(ax, (8.0, 12.3), "North (Palearctic)", size="small", bold=True)
bio.label(ax, (14.4, 12.3), "South (Oriental)", size="small", bold=True)

W, H = 3.6, 1.1
B = {
    "hip": ((11.2, 1.5), 9.0, "bone", "Hipparion fauna (one fauna across Eurasia and Africa;\nsteppe in the north, forest in the south)"),
    "nih": ((8.0, 3.6), W, "lipid", "Nihewan fauna"),
    "gig": ((14.4, 3.6), W, "plant", "Gigantopithecus fauna"),
    "zkd": ((8.0, 6.0), W, "lipid", "Zhoukoudian\n(Peking Man) fauna"),
    "ail": ((14.4, 6.0), W, "plant", "Ailuropoda-Stegodon\nfauna"),
    "sal": ((8.0, 7.85), 3.0, "lipid", "Salawusu fauna"),
    "mam": ((5.1, 9.05), 3.3, "dna2", "Mammuthus-Coelodonta\nfauna (Northeast)"),
    "sdd": ((11.4, 9.05), 3.3, "bone", "Upper Cave fauna\n(North China)"),
    "nea": ((7.8, 10.7), 5.4, "dna2", "Northeast Asian subrealm fauna"),
    "sin": ((14.4, 10.7), W, "positive", "Sino-Indian subrealm fauna"),
}
for key, (c, w, tok, text) in B.items():
    bio.box(ax, c, w, H if key != "hip" else 1.3, token=tok, text=text, size="tiny", radius=0.15)


def link(a, b, dx=0.0, **kw):
    (xa, ya), _, _, _ = B[a]
    (xb, yb), _, _, _ = B[b]
    ha = 0.65 if a == "hip" else H / 2
    bio.arrow(ax, (xa + dx, ya + ha), (xb, yb - H / 2), **kw)


link("hip", "nih", dx=-3.2)
link("hip", "gig", dx=3.2)
link("nih", "zkd")
link("gig", "ail")
link("zkd", "sal")
bio.arrow(ax, (6.5, 7.85), (5.1, 8.5), kind="process")
bio.arrow(ax, (9.5, 7.85), (11.4, 8.5), kind="process")
link("mam", "nea")
link("sdd", "nea")
link("ail", "sin")
# northward extension of the southern fauna in warm phases
bio.arrow(ax, (12.6, 6.3), (9.9, 6.3), kind="process", dashed=True, color=P.edge("plant"))
bio.label(ax, (11.25, 6.75), "reached North China\nin warm phases", size="tiny", color=P.edge("plant"))
bio.label(ax, (17.7, 0.25), "Schematic; intervals not to scale", size="tiny", ha="right", color=P.muted())
