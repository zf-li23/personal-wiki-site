# A: position of the ovary relative to the insertion of perianth and stamens: superior ovary
# (hypogynous flower), half-inferior ovary and inferior ovary (epigynous flower). B: placentation types in
# ovary cross-sections: marginal (one carpel), parietal (syncarpous, one locule, ovules on the wall),
# axile (syncarpous, several locules, ovules on the central axis), free-central (one locule, ovules on a
# free central column) and basal (one locule, one ovule at the base).
import wikibio as bio
from wikibio import plant

P = bio.P
fig, ax = bio.canvas(30.0, 9.6)

bio.panel(ax, "A", (0.2, 9.4))
bio.label(ax, (6.3, 9.1), "Position of the ovary", size="normal", bold=True)
TOK = {"ovary": "ovary", "style": "ovary", "petal": "petal", "sepal": "sepal", "anther": "anther", "filament": "anther",
       "receptacle": "neutral"}
for k, (name, note) in enumerate((("Superior", "hypogynous flower"), ("Half-inferior", "perigynous flower"),
                                   ("Inferior", "epigynous flower"))):
    x = 2.2 + 4.5 * k
    if k == 0:
        bio.icon(ax, "wikimedia/ovary-superior", at=(x, 5.0), height=4.4, parts=TOK)
    elif k == 1:
        bio.icon(ax, "wikimedia/ovary-half-inferior", at=(x, 5.0), height=4.4, parts=TOK)
    else:
        bio.icon(ax, "wikimedia/ovary-inferior", at=(x, 5.0), height=4.4, parts=TOK)
    bio.label(ax, (x, 1.75), name + " ovary", size="small", bold=True)
    bio.label(ax, (x, 1.25), "(" + note + ")", size="tiny", color=P.muted())
for k, (tok, text) in enumerate((("ovary", "Ovary"), ("neutral", "Receptacle / floral cup"), ("petal", "Petal"),
                                  ("sepal", "Sepal"), ("anther", "Stamen"))):
    x = 0.6 + [0, 1.9, 6.6, 8.3, 10.0][k]
    bio.box(ax, (x, 0.45), 0.34, 0.34, token=tok, radius=0.06)
    bio.label(ax, (x + 0.3, 0.45), text, size="small", ha="left")

bio.panel(ax, "B", (13.6, 9.4))
bio.label(ax, (21.8, 9.1), "Placentation (ovary in cross-section)", size="normal", bold=True)
types = [("marginal", 1, "Marginal", "1 carpel, 1 locule"), ("parietal", 3, "Parietal", "syncarpous, 1 locule"),
         ("axile", 3, "Axile", "syncarpous, 3 locules"), ("free-central", 5, "Free-central", "1 locule, central column"),
         ("basal", 2, "Basal", "1 locule, 1 basal ovule")]
for k, (pl, n, name, note) in enumerate(types):
    x = 15.6 + 3.25 * k
    plant.ovary(ax, (x, 5.4), 1.3, n=n, placentation=pl, ovules=2 if pl != "basal" else 1, token="ovary")
    bio.label(ax, (x, 3.4), name, size="small", bold=True)
    bio.label(ax, (x, 2.9), note, size="tiny", color=P.muted())
bio.label(ax, (21.8, 1.6), "Apical (pendulous) placentation: one ovule hanging from the top of the locule (mulberry)",
          size="small", color=P.muted())
