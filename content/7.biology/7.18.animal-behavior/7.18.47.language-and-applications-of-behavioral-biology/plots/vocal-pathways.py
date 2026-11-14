# Convergent circuits for vocal learning in humans and songbirds (after Jarvis 2004, Petkov and Jarvis
# 2012, Pfenning et al. 2014). Motor pathway (blue): a cortical (pallial) vocal motor area projects
# directly to the brainstem motor neurons of the vocal organ: laryngeal motor cortex (LMC) to nucleus
# ambiguus (nA) and the larynx in humans; HVC to RA to the tracheosyringeal motor nucleus (nXIIts) and the
# syrinx in songbirds. Learning loop (teal): cortex to basal ganglia to thalamus and back (in humans the
# anterior striatum and thalamus; in songbirds Area X, DLM and LMAN). Auditory areas (pink) provide the
# template and feedback. In non-learning primates such as macaques, the direct cortical projection to nA
# is absent or sparse, and calls are produced through midbrain circuits (periaqueductal gray, PAG).
import wikibio as bio

P = bio.P
fig, ax = bio.canvas(24, 11.0)


def column(x, title, nodes, links, organ):
    bio.label(ax, (x + 3.0, 10.4), title, size="normal", bold=True)
    for k, (xy, tok, w) in nodes.items():
        bio.box(ax, (x + xy[0], xy[1]), w, 0.85, tok, text=k, size="small", zorder=8)
    for a, b, tok, bend in links:
        bio.arrow(ax, (x + a[0], a[1]), (x + b[0], b[1]), kind="process", color=P.edge(tok), lw=1.6, bend=bend)
    bio.box(ax, (x + organ[1][0], organ[1][1]), 2.4, 0.85, "muscle", text=organ[0], size="small")


human = {
    "LMC": ((2.2, 8.6), "dna", 1.8), "auditory cortex": ((6.0, 8.6), "receptor", 3.2),
    "anterior striatum": ((0.8, 5.9), "enzyme", 3.0), "thalamus": ((0.8, 4.4), "enzyme", 2.2),
    "nA": ((3.0, 3.2), "dna", 1.4),
}
xh = 1.4
column(xh, "Human (speech)", human,
       [((2.6, 8.17), (3.0, 3.63), "dna", 0.0), ((1.7, 8.17), (1.0, 6.33), "enzyme", 0.0),
        ((0.8, 5.47), (0.8, 4.83), "enzyme", 0.0), ((-0.35, 4.4), (1.3, 8.6), "enzyme", 0.45),
        ((4.4, 8.6), (3.1, 8.6), "receptor", 0.0)], ("larynx", (3.0, 1.2)))
bio.arrow(ax, (xh + 3.0, 2.77), (xh + 3.0, 1.63), kind="process", color=P.edge("dna"), lw=1.6)
bird = {
    "HVC": ((2.0, 8.6), "dna", 1.6), "Field L, NCM": ((6.0, 8.6), "receptor", 2.8),
    "Area X": ((0.6, 5.9), "enzyme", 1.8), "DLM": ((0.6, 4.4), "enzyme", 1.4), "LMAN": ((2.6, 4.4), "enzyme", 1.8),
    "RA": ((4.6, 5.9), "dna", 1.4), "nXIIts": ((4.6, 3.2), "dna", 1.8),
}
xb = 13.2
column(xb, "Songbird (song)", bird,
       [((2.6, 8.17), (4.4, 6.33), "dna", 0.0), ((4.6, 5.47), (4.6, 3.63), "dna", 0.0),
        ((1.6, 8.17), (0.8, 6.33), "enzyme", 0.0), ((0.6, 5.47), (0.6, 4.83), "enzyme", 0.0),
        ((1.3, 4.4), (1.7, 4.4), "enzyme", 0.0), ((3.5, 4.6), (4.2, 5.47), "enzyme", 0.0),
        ((4.6, 8.6), (2.8, 8.6), "receptor", 0.0)], ("syrinx", (4.6, 1.2)))
bio.arrow(ax, (xb + 4.6, 2.77), (xb + 4.6, 1.63), kind="process", color=P.edge("dna"), lw=1.6)
for i, (tok, txt) in enumerate([("dna", "direct cortical (pallial) motor pathway"),
                                ("enzyme", "cortex-basal ganglia-thalamus loop (learning)"),
                                ("receptor", "auditory template and feedback")]):
    y = 2.6 - i * 0.6
    ax.plot([8.0, 8.8], [y, y], color=P.edge(tok), lw=2.0)
    bio.label(ax, (9.0, y), txt, size="tiny", ha="left")
bio.label(ax, (12.0, 0.3), "Macaque (no vocal learning): direct LMC to nA projection absent or sparse; calls via PAG",
          size="tiny", color=P.muted())
