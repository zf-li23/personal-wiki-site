"""Autonomous specification of muscle in ascidians. A: the eight-cell embryo seen from the left (animal pole
up, anterior left); the four pairs of blastomeres are named a4.2, b4.2 (animal) and A4.1, B4.1 (vegetal).
The yellow crescent cytoplasm, segregated into the posterior-vegetal pair B4.1, contains macho-1 mRNA; B4.1
gives rise to most of the larval tail muscle. Other fates are listed for each pair (the notochord and
mesenchyme are specified conditionally, by FGF from neighbouring endoderm). B: the logic of the experiments.
Isolated B4.1 forms muscle (the information is in the cell); depleting macho-1 mRNA abolishes primary muscle
(necessary); injecting macho-1 mRNA into animal blastomeres makes them form muscle (sufficient)."""
import wikibio as bio
from wikibio import embryology as E

P = bio.P
fig, ax = bio.canvas(22, 8.6)
ec, me, en = E.tok("ectoderm"), E.tok("mesoderm"), E.tok("endoderm")
bio.label(ax, (0.4, 8.2), "A  Eight-cell embryo (left side)", size="small", bold=True, ha="left")
cells = {"a4.2": ((3.0, 5.6), ec, "epidermis,\nbrain"), "b4.2": ((5.6, 5.6), ec, "epidermis,\nnerve cord"),
         "A4.1": ((3.0, 3.2), "neutral", "endoderm, notochord,\nnerve cord"), "B4.1": ((5.6, 3.2), me, "muscle, endoderm,\nmesenchyme")}
for k, (name, (xy, t, fate)) in enumerate(cells.items()):
    o = bio.blob(xy, 1.25, 1.15, wobble=0.03, seed=k, k=8)
    bio.shape(ax, o, t, lw=1.1, zorder=5)
    bio.label(ax, (xy[0], xy[1] + 0.25), name, size="small", color=P.on_fill(), bold=True)
cr = bio.blob((5.6, 2.35), 1.0, 0.25, wobble=0.02, seed=9, k=8)
bio.shape(ax, cr, "highlight", lw=0.9, zorder=6)
bio.callout(ax, (6.2, 2.3), (8.2, 1.4), "yellow crescent\n(macho-1 mRNA)", size="tiny")
for name, ((x, y), t, fate) in cells.items():
    bio.label(ax, (x, y - 0.45 if y < 4 else y - 0.35), fate, size="tiny", color=P.on_fill())
bio.label(ax, (1.0, 7.3), "animal", size="tiny", color=P.muted())
bio.label(ax, (1.0, 1.4), "vegetal", size="tiny", color=P.muted())
bio.label(ax, (2.0, 0.6), "anterior", size="tiny", color=P.muted())
bio.label(ax, (6.8, 0.6), "posterior", size="tiny", color=P.muted())

bio.label(ax, (10.6, 8.2), "B  Experiments", size="small", bold=True, ha="left")
rows = [("B4.1 isolated and cultured", me, "muscle forms", "autonomous"),
        ("B4.1 with macho-1 mRNA depleted", "neutral", "no primary muscle", "necessary"),
        ("animal cell injected with macho-1 mRNA", me, "ectopic muscle", "sufficient")]
for k, (exp, t, res, concl) in enumerate(rows):
    y = 6.6 - 2.2 * k
    bio.label(ax, (10.6, y + 0.65), exp, size="tiny", ha="left", color=P.muted())
    o = bio.blob((11.4, y - 0.15), 0.6, 0.55, wobble=0.03, seed=k + 3, k=8)
    bio.shape(ax, o, ec if k == 2 else ("neutral" if k == 1 else me), lw=1.0, zorder=5)
    bio.arrow(ax, (12.4, y - 0.15), (13.8, y - 0.15), kind="process", head=0.18)
    for j in range(4):
        bio.box(ax, (14.4 + 0.55 * j, y - 0.15), 0.48, 0.8, t, None, radius=0.1)
    bio.label(ax, (16.9, y - 0.15), res, size="tiny", ha="left")
    bio.label(ax, (19.4, y - 0.15), concl, size="small", ha="left", bold=True)
