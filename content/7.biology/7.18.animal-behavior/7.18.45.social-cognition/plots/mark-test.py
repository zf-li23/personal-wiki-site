# The mark test of mirror self-recognition (Gallup 1970) and two sets of results that limit its
# interpretation. A: the procedure. B: children aged 35-54 months who touched or removed a sticker on the
# head after seeing themselves in a mirror (Broesch et al. 2011): US and Canada 84 %, Saint Lucia 58 %,
# Grenada 52 %, Peru 51 %, Fiji 0 %, Kenya 2 of 82 (2 %). C: mean number of touches of a dye mark on the
# face in 30 min by chimpanzees with and without a mirror (Povinelli et al. 1993): 2.5 without, 3.9 with.
import wikibio as bio
from wikibio import quant

P = bio.P
fig, ax = bio.canvas(24, 10.8)
bio.panel(ax, "A", (0.3, 10.4))
steps = [
    ("mirror exposure", "days with a mirror:\nsocial responses, then\nself-directed behavior"),
    ("marking", "under anesthesia, odorless\ndye on brow and ear;\nsham mark as control"),
    ("baseline", "after waking: touches\nof the mark area\nwithout a mirror"),
    ("mirror test", "mirror returned: touches\nof the mark (and smelling\nthe fingers)"),
]
for k, (head, body) in enumerate(steps):
    y = 8.9 - k * 2.25
    bio.box(ax, (2.3, y), 3.0, 0.8, "dna" if k < 3 else "positive", text=head, size="small")
    bio.label(ax, (4.1, y), body, size="tiny", ha="left")
    if k < 3:
        bio.arrow(ax, (2.3, y - 0.45), (2.3, y - 1.8), kind="process", color=P.muted())
bio.label(ax, (2.3, 1.2), "pass: more mark touches\nwith the mirror than without", size="tiny", color=P.edge("positive"))

pb = quant.Plot(ax, (10.6, 2.6, 7.6, 6.8), (-0.6, 5.6), (0, 100), ylabel="Children touching the mark / %",
                xticks=[(0, "US, Canada"), (1, "St Lucia"), (2, "Grenada"), (3, "Peru"), (4, "Fiji"), (5, "Kenya")],
                yticks=[0, 25, 50, 75, 100])
bio.panel(ax, "B", (9.2, 10.4))
vals = [84, 58, 52, 51, 0, 2.4]
for k, v in enumerate(vals):
    pb.bars([k - 0.32, k + 0.32], [max(v, 0.6)], "rna")
    pb.text(k, v + 4, f"{v:.0f}", size="tiny")
bio.label(ax, (14.4, 1.4), "Children aged 35-54 months", size="tiny", color=P.muted())

pc = quant.Plot(ax, (20.4, 2.6, 2.9, 6.8), (-0.7, 1.7), (0, 5), ylabel="Mark touches per 30 min",
                xticks=[(0, "no mirror"), (1, "mirror")], yticks=[0, 1, 2, 3, 4, 5])
bio.panel(ax, "C", (19.0, 10.4))
for k, v in enumerate([2.5, 3.9]):
    pc.bars([k - 0.32, k + 0.32], [v], "neutral" if k == 0 else "positive")
    pc.text(k, v + 0.22, f"{v}", size="tiny")
bio.label(ax, (21.85, 1.4), "Chimpanzees", size="tiny", color=P.muted())
