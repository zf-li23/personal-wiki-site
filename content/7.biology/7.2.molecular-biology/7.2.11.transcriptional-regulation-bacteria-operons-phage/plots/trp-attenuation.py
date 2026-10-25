# Attenuation in the trp leader, drawn as arc diagrams of the nascent leader RNA (5' left, 3' right): the
# four segments 1-4 (segment 1 contains the two Trp codons of the leader peptide, the leader stop codon lies
# between 1 and 2), the U8 tract after segment 4, and arcs joining the segments that pair.
# A: Trp abundant: the ribosome reaches the stop codon and covers segment 2; 3:4 forms (terminator), and the
#    polymerase terminates.
# B: Trp scarce: the ribosome stalls at the Trp codons on segment 1; 2:3 forms (antiterminator), 3:4 cannot,
#    and the polymerase continues into trpE.
# C: no translation: 1:2 (pause hairpin) and 3:4 form, and transcription terminates.
import numpy as np
import wikibio as bio

P = bio.P
fig, ax = bio.canvas(20.0, 13.2)
seg = {1: (3.6, 4.8), 2: (5.6, 6.8), 3: (8.0, 9.2), 4: (9.8, 11.0)}
tok = {1: "positive", 2: "highlight", 3: "protein", 4: "negative"}


def row(y, pairs, ribo, title, letter, terminated):
    bio.panel(ax, letter, (0.1, y + 3.3))
    bio.label(ax, (0.7, y + 3.05), title, size="small", bold=True, ha="left")
    end = 11.8 if terminated else 17.6
    ax.plot([1.2, end], [y, y], color=P.edge("rna"), lw=2.2, solid_capstyle="round", zorder=4)
    bio.label(ax, (1.0, y), "5′", size="tiny", bold=True, ha="right")
    for k, (a, b) in seg.items():
        bio.box(ax, ((a + b) / 2, y), b - a, 0.42, token=tok[k], text=str(k), size="tiny", radius=0.06, zorder=6)
    bio.label(ax, (11.4, y - 0.45), "U8", size="tiny", color=P.edge("rna"))
    # Trp codons and stop codon marks
    for x in (4.0, 4.3):
        ax.plot([x, x], [y - 0.32, y - 0.5], color=P.ink(), lw=1.0)
    bio.label(ax, (4.15, y - 0.72), "UGG UGG", size="tiny", color=P.muted())
    ax.plot([5.2, 5.2], [y - 0.32, y - 0.5], color=P.ink(), lw=1.0)
    bio.label(ax, (5.2, y - 0.72), "stop", size="tiny", color=P.muted())
    for (i, j, name) in pairs:
        xa, xb = np.mean(seg[i]), np.mean(seg[j])
        th = np.linspace(np.pi, 0, 80)
        r = (xb - xa) / 2
        ax.plot((xa + xb) / 2 + r * np.cos(th), y + 0.25 + 0.9 * r * np.sin(th) / max(r, 1e-9) * min(r, 1.6),
                color=P.edge(tok[j]), lw=1.6, zorder=5)
        bio.label(ax, ((xa + xb) / 2, y + 0.45 + 0.9 * min(r, 1.6)), name, size="tiny")
    if ribo is not None:
        rb = bio.core.blob((ribo, y + 0.05), 0.75, 0.55, wobble=0.05, seed=2, k=8)
        bio.shape(ax, rb, token="rrna", zorder=7)
        bio.label(ax, (ribo, y + 0.05), "ribosome", size="tiny", color=P.on_fill(), zorder=8)
    if terminated:
        pol = bio.core.blob((13.0, y + 0.6), 0.85, 0.6, wobble=0.05, seed=4, k=8)
        bio.shape(ax, pol, token="enzyme", zorder=3, alpha=0.8)
        bio.label(ax, (13.0, y + 0.6), "RNAP", size="tiny", color=P.on_fill(), zorder=8)
        bio.arrow(ax, (13.9, y + 0.9), (14.8, y + 1.5), kind="process")
        bio.label(ax, (16.5, y + 0.6), "termination at the attenuator", size="tiny")
    else:
        pol = bio.core.blob((17.8, y), 0.85, 0.6, wobble=0.05, seed=4, k=8)
        bio.shape(ax, pol, token="enzyme", zorder=3, alpha=0.8)
        bio.label(ax, (17.8, y), "RNAP", size="tiny", color=P.on_fill(), zorder=8)
        bio.label(ax, (14.6, y + 0.35), "trpE …", size="tiny", italic=True)
        bio.arrow(ax, (18.8, y), (19.6, y), kind="process")


row(9.4, [(3, 4, "3:4 terminator")], 6.2, "Trp abundant", "A", True)
row(5.2, [(2, 3, "2:3 antiterminator")], 4.15, "Trp scarce", "B", False)
row(1.0, [(1, 2, "1:2 pause"), (3, 4, "3:4 terminator")], None, "No translation", "C", True)
