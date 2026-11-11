"""The four classical neuromodulatory systems of the mammalian brain (schematic, lateral view,
anterior to the right). Each panel shows the source nuclei (dots) and the main projections
(arrows, the color of the system): dopamine from the substantia nigra pars compacta to the dorsal
striatum and from the ventral tegmental area to the ventral striatum and prefrontal cortex;
norepinephrine from the locus coeruleus to the whole forebrain, cerebellum and spinal cord;
serotonin from the raphe nuclei to the forebrain (rostral raphe) and to the spinal cord (caudal
raphe); acetylcholine from the basal forebrain to the cortex and hippocampus and from the
pedunculopontine and laterodorsal tegmental nuclei to the thalamus. Positions are approximate.
"""
import wikibio as bio

P = bio.P
fig, ax = bio.canvas(16, 10.4)

W, H = 8.0, 5.2
panels = [
    ("Dopamine", "drug", (0, H),
     [("SNc", (6.45, 3.3)), ("VTA", (6.75, 3.25))],
     [((6.45, 3.3), (6.6, 4.7), 0.4), ((6.75, 3.25), (7.3, 4.2), -0.3), ((6.75, 3.25), (8.7, 5.0), -0.35)],
     [("striatum", (6.6, 4.85)), ("PFC", (8.9, 5.2))]),
    ("Norepinephrine", "receptor", (W, H),
     [("LC", (5.85, 2.55))],
     [((5.85, 2.55), (8.6, 5.6), -0.45), ((5.85, 2.55), (4.6, 6.0), 0.5), ((5.85, 2.55), (4.6, 2.65), 0.3),
      ((5.85, 2.55), (5.65, 1.1), 0.0), ((5.85, 2.55), (5.3, 3.9), 0.3)],
     [("cortex", (4.3, 6.4)), ("cerebellum", (3.9, 2.2)), ("spinal cord", (6.5, 1.1))]),
    ("Serotonin", "enzyme", (0, 0),
     [("raphe", (6.1, 3.0)), ("", (5.75, 2.2))],
     [((6.1, 3.0), (8.3, 5.9), -0.4), ((6.1, 3.0), (6.4, 4.7), 0.3), ((6.1, 3.0), (5.2, 3.8), 0.3),
      ((5.75, 2.2), (5.65, 0.9), 0.0)],
     [("cortex", (8.8, 6.2)), ("spinal cord", (7.0, 1.1))]),
    ("Acetylcholine", "positive", (W, 0),
     [("BF", (7.35, 3.85)), ("PPT/LDT", (6.2, 3.1))],
     [((7.35, 3.85), (8.4, 6.0), -0.3), ((7.35, 3.85), (5.0, 6.3), 0.45), ((7.35, 3.85), (5.4, 3.85), -0.3),
      ((6.2, 3.1), (6.3, 4.5), 0.35)],
     [("cortex", (8.8, 6.3)), ("hippocampus", (4.4, 3.4)), ("thalamus", (6.1, 4.85))]),
]
for title, tok, (ox, oy), sources, arrows, targets in panels:
    bio.icon(ax, "servier/brain-side", at=(ox + 6.0 * W / 12, oy + 4.0 * H / 8 - 0.1), height=7.0 * H / 8, alpha=0.32)
    sx, sy = W / 12, H / 8
    def tr(p):
        return (ox + p[0] * sx, oy + p[1] * sy - 0.1)
    for a, b, bend in arrows:
        bio.arrow(ax, tr(a), tr(b), kind="process", bend=bend, color=P.edge(tok), lw=1.6)
    for name, p in sources:
        x, y = tr(p)
        ax.plot([x], [y], "o", ms=8, color=P.fill(tok), mec=P.edge(tok), mew=1.2, zorder=20)
        if name == "SNc":
            bio.label(ax, (x - 0.15, y - 0.32), name, size="small", ha="right")
        elif name:
            bio.label(ax, (x + 0.15, y - 0.32), name, size="small", ha="left")
    for name, p in targets:
        bio.label(ax, tr(p), name, size="small", color=P.muted())
    bio.label(ax, (ox + 0.3, oy + H - 0.35), title, size="title", ha="left", color=P.edge(tok), bold=True)
bio.label(ax, (15.7, 0.2), "anterior \u2192", size="tiny", ha="right", color=P.muted())
