# Gibson assembly of two fragments that share a 30 bp terminal overlap (yellow). 1: double-stranded fragments
# A and B; each strand drawn 5'->3' along its arrow. 2: T5 exonuclease removes nucleotides from the 5' ends,
# exposing complementary 3' single-stranded overhangs. 3: the overhangs anneal. 4: a high-fidelity polymerase
# extends the 3' ends across the gaps and Taq DNA ligase seals the nicks, giving a seamless junction. All three
# enzymes work in one tube at 50 C; the heat-labile exonuclease is gradually inactivated.
import numpy as np
import wikibio as bio

P = bio.P
fig, ax = bio.canvas(20.0, 11.0)
OV = 1.2  # overlap length on the canvas


def strand(x0, x1, y, tok, direction, lw=3.0, ov=None):
    ax.plot([x0, x1], [y, y], color=P.edge(tok), lw=lw, solid_capstyle="butt", zorder=8)
    if ov:
        ax.plot(list(ov), [y, y], color=P.edge("highlight"), lw=lw + 1.5, solid_capstyle="butt", zorder=9)
    tip = x1 if direction > 0 else x0
    ax.add_patch(bio.core.Polygon([[tip + 0.18 * direction, y], [tip, y + 0.14], [tip, y - 0.14]], color=P.edge(tok), zorder=9))


y = 9.3
bio.label(ax, (0.3, y + 0.85), "1  fragments with a shared overlap", size="small", bold=True, ha="left")
strand(2.0, 9.0, y + 0.2, "dna", +1, ov=(9.0 - OV, 9.0))
strand(2.0, 9.0, y - 0.2, "dna2", -1, ov=(9.0 - OV, 9.0))
strand(10.5, 17.5, y + 0.2, "positive", +1, ov=(10.5, 10.5 + OV))
strand(10.5, 17.5, y - 0.2, "carbohydrate", -1, ov=(10.5, 10.5 + OV))
bio.label(ax, (19.7, y + 0.85), "A ends and B begins with the same 30 bp", size="tiny", ha="right", color=P.muted())
y = 6.9
bio.label(ax, (0.3, y + 0.85), "2  T5 exonuclease chews 5′ ends", size="small", bold=True, ha="left")
strand(2.0, 9.0, y + 0.2, "dna", +1, ov=(9.0 - OV, 9.0))
strand(2.0, 7.4, y - 0.2, "dna2", -1)
strand(12.1, 17.5, y + 0.2, "positive", +1)
strand(10.5, 17.5, y - 0.2, "carbohydrate", -1, ov=(10.5, 10.5 + OV))
bio.label(ax, (19.7, y + 0.85), "3′ overhangs exposed", size="tiny", ha="right", color=P.muted())
y = 4.5
bio.label(ax, (0.3, y + 0.85), "3  overlaps anneal", size="small", bold=True, ha="left")
strand(2.0, 9.0, y + 0.2, "dna", +1, ov=(9.0 - OV, 9.0))
strand(2.0, 7.4, y - 0.2, "dna2", -1)
strand(9.4, 14.8, y + 0.2, "positive", +1)
strand(7.8, 14.8, y - 0.2, "carbohydrate", -1, ov=(7.8, 9.0))
bio.label(ax, (19.7, y + 0.85), "gaps remain on both strands", size="tiny", ha="right", color=P.muted())
y = 2.1
bio.label(ax, (0.3, y + 0.85), "4  polymerase fills, ligase seals", size="small", bold=True, ha="left")
strand(2.0, 9.4, y + 0.2, "dna", +1, ov=(9.0 - OV, 9.0))
strand(9.4, 14.8, y + 0.2, "positive", +1)
strand(2.0, 7.8, y - 0.2, "dna2", -1)
strand(7.4, 14.8, y - 0.2, "carbohydrate", -1, ov=(7.8, 9.0))
ax.plot([9.0, 9.4], [y + 0.2, y + 0.2], color=P.edge("enzyme"), lw=3.0, zorder=10)
ax.plot([7.4, 7.8], [y - 0.2, y - 0.2], color=P.edge("enzyme"), lw=3.0, zorder=10)
bio.label(ax, (19.7, y + 0.85), "seamless product A–B", size="tiny", ha="right", color=P.muted())
for k, (tok, txt) in enumerate([("highlight", "overlap sequence"), ("enzyme", "new DNA (polymerase)")]):
    ax.plot([2.0 + 5 * k, 2.8 + 5 * k], [0.6, 0.6], color=P.edge(tok), lw=4)
    bio.label(ax, (3.0 + 5 * k, 0.6), txt, size="tiny", ha="left")
bio.label(ax, (12.0, 0.6), "arrowheads mark 3′ ends", size="tiny", ha="left", color=P.muted())
