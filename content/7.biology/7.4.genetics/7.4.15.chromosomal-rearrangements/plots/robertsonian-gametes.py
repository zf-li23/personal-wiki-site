"""Gametes of a carrier of a balanced Robertsonian translocation 45,XX,der(14;21) and the karyotypes of the
zygotes they give with a normal gamete. B: expected outcomes if the six gametes were equally frequent and
all zygotes survived, compared with approximate empirical risks of Down syndrome at birth (about 10-15 %
for carrier mothers, about 1 % for carrier fathers)."""
import matplotlib.pyplot as plt
import wikibio as bio
from wikibio import charts, cytogenetics as C

P = bio.P
fig, ax = bio.canvas(25, 9.0)
c14 = C.with_token(["p", "o", "q", "q", "q"], "dna")
c21 = C.with_token(["p", "o", "q", "q"], "enzyme")
der = C.with_token(["q", "q"], "enzyme") + [("o", "dna")] + C.with_token(["q", "q", "q"], "dna")
bio.panel(ax, "A", (0.2, 8.8))
bio.label(ax, (0.9, 8.5), "Carrier: 14, 21, der(14;21)", size="small", ha="left")
x = 1.0
for c, nm in ((c14, "14"), (c21, "21"), (der, "der(14;21)")):
    o = C.lettered(ax, (x, 7.7), c, unit=0.36, height=0.28, text=False)
    bio.label(ax, ((o["x0"] + o["x1"]) / 2, 7.25), nm, size="tiny", color=P.muted())
    x = o["x1"] + 0.6
rows = [
    ("Alternate", [c14, c21], "46, normal", "positive"),
    ("Alternate", [der], "45, balanced carrier", "positive"),
    ("Adjacent", [der, c21], "46, +der: Down syndrome", "highlight"),
    ("Adjacent", [c14], "45, monosomy 21: lost", "negative"),
    ("Adjacent", [der, c14], "46, trisomy 14: lost", "negative"),
    ("Adjacent", [c21], "45, monosomy 14: lost", "negative"),
]
bio.label(ax, (1.0, 6.5), "Gamete", size="tiny", color=P.muted(), ha="left")
bio.label(ax, (8.0, 6.5), "Zygote with a normal gamete", size="tiny", color=P.muted(), ha="left")
y = 5.9
for pat, chroms, out, tok in rows:
    xx = 1.0
    for c in chroms:
        o = C.lettered(ax, (xx, y), c, unit=0.3, height=0.24, text=False)
        xx = o["x1"] + 0.3
    bio.label(ax, (5.6, y), pat, size="tiny", color=P.muted(), ha="left")
    bio.box(ax, (10.4, y), 4.8, 0.55, token=tok, text=out, size="tiny")
    y -= 0.85
bio.panel(ax, "B", (14.2, 8.8))
pax = charts.axes_at(ax, (16.0, 1.4, 8.4, 6.4))
cats = ["normal", "carrier", "Down"]
theory = [1 / 3, 1 / 3, 1 / 3]
pax.bar([0, 1, 2], theory, width=0.55, color=P.fill("neutral"), edgecolor=P.edge("neutral"), label="six equal gametes, survivors only")
pax.plot([1.85, 2.15], [0.125, 0.125], color=P.edge("receptor"), lw=2.2, label="observed, carrier mother")
pax.plot([1.85, 2.15], [0.01, 0.01], color=P.edge("dna"), lw=2.2, label="observed, carrier father")
pax.set_xticks([0, 1, 2], cats)
pax.set_ylim(0, 0.5)
charts.style_axes(pax, "liveborn child", "probability")
pax.legend(frameon=False, fontsize=bio.core.FONT["tiny"], labelcolor=P.ink(), loc="upper left")
