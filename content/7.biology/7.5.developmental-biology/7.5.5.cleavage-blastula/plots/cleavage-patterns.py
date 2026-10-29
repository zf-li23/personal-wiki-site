"""Yolk distribution and the main patterns of cleavage. Top row: the four classes of egg by the amount and
position of yolk (dots: yolk platelets). Middle and bottom rows: holoblastic patterns (radial, displaced
radial of amphibians, spiral seen from the animal pole, bilateral of ascidians seen from the vegetal pole,
rotational of mammals inside the zona pellucida) and meroblastic patterns (discoidal, superficial)."""
import wikibio as bio
from wikibio import embryology as E

P = bio.P
fig, ax = bio.canvas(24, 15.2)
xs = [3.0 + 6.0 * k for k in range(4)]
eggs = [("iso", "Isolecithal", "sea urchin, mammals"), ("meso", "Mesolecithal", "amphibians"),
        ("telo", "Telolecithal", "fish, birds, reptiles"), ("centro", "Centrolecithal", "insects")]
bio.label(ax, (0.3, 14.8), "Yolk distribution", size="title", bold=True, ha="left")
for x, (kind, name, who) in zip(xs, eggs):
    a = E.egg(ax, (x, 12.6), 1.15, kind)
    bio.label(ax, (x, 10.9), name, size="normal", bold=True)
    bio.label(ax, (x, 10.45), who, size="small", color=P.muted())
bio.label(ax, (xs[1] + 1.55, 13.75), "animal", size="tiny", color=P.muted(), ha="left")
bio.label(ax, (xs[1] + 1.55, 11.45), "vegetal", size="tiny", color=P.muted(), ha="left")

bio.label(ax, (0.3, 9.7), "Holoblastic (complete) cleavage", size="title", bold=True, ha="left")
holo = [("radial", "Radial", "sea urchin, 8-cell, side view"), ("unequal", "Displaced radial", "frog, 8-cell, side view"),
        ("spiral", "Spiral (dextral)", "snail, 8-cell, animal view"), ("bilateral", "Bilateral", "ascidian, 8-cell, vegetal view")]
for x, (pat, name, who) in zip(xs, holo):
    a = E.cleavage(ax, (x, 7.55), 1.1, pat)
    bio.label(ax, (x, 5.85), name, size="normal", bold=True)
    bio.label(ax, (x, 5.4), who, size="small", color=P.muted())
    if pat == "spiral":
        for k in "ABCD":
            p = a[k]
            bio.label(ax, (x + (p[0] - x) * 1.55, 7.55 + (p[1] - 7.55) * 1.55), k, size="tiny", color=P.muted())
        bio.label(ax, (a["1a"][0], a["1a"][1]), "1a", size="tiny", color=P.on_fill())
    if pat == "bilateral":
        bio.callout(ax, a["crescent"], (x + 1.55, 6.55), "Yellow\ncrescent", size="tiny")

bio.label(ax, (0.3, 4.6), "Rotational and meroblastic (incomplete) cleavage", size="title", bold=True, ha="left")
mero = [("rotational", "Rotational", "mammals, 4-cell"), ("discoidal", "Discoidal", "fish, birds"),
        ("superficial", "Superficial", "insects: syncytial nuclei")]
for x, (pat, name, who) in zip((xs[0], xs[1], xs[2] + 1.2), mero):
    a = E.cleavage(ax, (x, 2.55), 1.1, pat)
    bio.label(ax, (x, 0.85), name, size="normal", bold=True)
    bio.label(ax, (x, 0.4), who, size="small", color=P.muted())
    if pat == "discoidal":
        bio.callout(ax, a["blastodisc"], (x + 1.7, 3.9), "Blastodisc", size="tiny")
    if pat == "superficial":
        bio.callout(ax, a["pole_cells"], (x + 2.3, 3.4), "Pole cells", size="tiny")
