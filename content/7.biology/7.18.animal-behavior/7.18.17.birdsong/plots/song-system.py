"""The song system of an oscine songbird in a schematic sagittal view of the brain (anterior to the left).
Motor pathway (blue): HVC -> RA -> nXIIts (tracheosyringeal motor neurons) -> syrinx muscles, with RA also
driving the respiratory premotor nuclei. Anterior forebrain pathway (orange): HVC -> Area X (basal ganglia)
-> DLM (thalamus) -> LMAN -> RA, needed for learning. Auditory areas (pink): Field L -> NCM / CMM.
Dopamine from VTA to Area X (green). Positions are schematic, not to scale."""
import wikibio as bio
from matplotlib.patches import PathPatch
from matplotlib.path import Path

P = bio.P
fig, ax = bio.canvas(22, 11.5)
pts = bio.smooth_closed([(1.2, 6.0), (2.2, 8.6), (5.5, 10.2), (10, 10.4), (13.6, 9.6), (15.6, 8.4), (17.6, 8.2),
                         (19.0, 6.6), (18.6, 5.0), (17.8, 4.2), (17.4, 2.0), (16.2, 1.8), (15.4, 3.6), (12, 4.2),
                         (8, 4.0), (4, 4.3), (1.8, 4.8)])
ax.add_patch(PathPatch(Path(pts), facecolor=P.fill("cytoplasm"), edgecolor=P.edge("neuron"), lw=1.2, zorder=2))
bg = P.fill("cytoplasm")
nuc = {
    "HVC": ((12.6, 9.0), "dna"), "RA": ((13.6, 6.4), "dna"), "nXIIts": ((16.4, 3.2), "dna"),
    "Area X": ((6.4, 6.0), "enzyme"), "DLM": ((9.6, 5.2), "enzyme"), "LMAN": ((6.0, 8.4), "enzyme"),
    "Field L": ((16.4, 6.6), "receptor"), "NCM": ((15.4, 8.5), "receptor"), "VTA": ((12.4, 4.6), "positive"),
}
for k, (xy, tok) in nuc.items():
    bio.box(ax, xy, 0.9 + 0.22 * len(k), 0.8, tok, text=k, size="small", zorder=8)


def link(a, b, tok, bend=0.0, kind="process"):
    bio.arrow(ax, a, b, kind=kind, bend=bend, color=P.edge(tok), lw=1.6, bg=bg, shrink=0.05)


link((12.9, 8.55), (13.4, 6.85), "dna")             # HVC -> RA
link((14.0, 6.0), (16.1, 3.65), "dna")              # RA -> nXIIts
link((11.8, 8.95), (7.4, 6.35), "enzyme", bend=0.15)  # HVC -> X
link((7.3, 5.75), (8.9, 5.25), "enzyme")            # X -> DLM
link((9.3, 5.65), (6.6, 8.0), "enzyme", bend=0.2)   # DLM -> LMAN
link((7.0, 8.55), (12.7, 6.55), "enzyme", bend=-0.25)  # LMAN -> RA
link((16.2, 7.05), (15.6, 8.05), "receptor")         # Field L -> NCM
link((11.6, 4.75), (7.3, 5.6), "positive", bend=-0.1)  # VTA -> X
# syrinx below brainstem
bio.box(ax, (16.6, 0.9), 1.9, 0.75, "muscle", text="syrinx", size="small")
link((16.5, 2.75), (16.6, 1.3), "dna")
bio.label(ax, (18.6, 3.4), "respiratory\nnuclei", size="tiny", color=P.muted())
link((14.2, 6.1), (18.0, 3.9), "dna", bend=-0.2)
# legend
for i, (tok, txt) in enumerate([("dna", "motor pathway: produces song"), ("enzyme", "anterior forebrain pathway: learning, variability"),
                                ("receptor", "auditory areas: tutor memory, feedback"), ("positive", "dopamine: performance evaluation")]):
    y = 2.9 - i * 0.62
    ax.plot([0.8, 1.6], [y, y], color=P.edge(tok), lw=2.0)
    bio.label(ax, (1.8, y), txt, size="tiny", ha="left")
bio.label(ax, (2.2, 10.6), "anterior", size="tiny", color=P.muted())
bio.label(ax, (18.6, 9.6), "posterior", size="tiny", color=P.muted())
ax.set_ylim(0.2, 11.2)
