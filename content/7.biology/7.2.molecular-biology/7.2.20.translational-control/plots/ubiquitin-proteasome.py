# The ubiquitin-proteasome system and the N-degron rule.
# A: E1 activates ubiquitin with ATP (adenylate, then a thioester with its active-site Cys), E2 carries it as a
#    thioester, and an E3 ligase binds the substrate's degron and transfers ubiquitin (directly from E2 for RING
#    E3s, through its own Cys for HECT E3s) to a Lys of the substrate; repeated rounds build a Lys48-linked
#    chain. The 26S proteasome recognizes the chain with its 19S regulatory particle (ubiquitin receptors,
#    deubiquitinase Rpn11, a ring of six AAA+ ATPases that unfolds and threads the substrate) and degrades it in
#    the 20S core (alpha7 beta7 beta7 alpha7, proteolytic sites beta1, beta2, beta5) to peptides of 3-25 residues;
#    ubiquitin is recycled.
# B: half-lives of beta-galactosidase variants with different N-terminal residues in yeast (Bachmair, Finley and
#    Varshavsky, 1986, as tabulated by Lehninger): stabilizing residues > 20 h, destabilizing ones 2-30 min.
import matplotlib.pyplot as plt
import numpy as np
import wikibio as bio
from wikibio import charts

P = bio.P
fig = plt.figure(figsize=(12.6, 4.6))
gs = fig.add_gridspec(1, 2, width_ratios=[1.5, 1])
ax = fig.add_subplot(gs[0])
ax.set_xlim(0, 15)
ax.set_ylim(0, 8)
ax.set_aspect("equal")
ax.axis("off")
ax.set_title("A   Ubiquitination and degradation", loc="left", fontsize=9, color=P.ink())


def ub(xy, r=0.22):
    ax.add_patch(bio.core.Circle(xy, r, facecolor=P.fill("highlight"), edgecolor=P.edge("highlight"), lw=0.8, zorder=12))


bio.protein(ax, (1.2, 6.2), 1.4, 0.9, "enzyme", text="E1")
ub((2.05, 6.65))
bio.label(ax, (1.2, 5.4), "ATP → AMP + PPi", size="tiny", color=P.muted())
bio.arrow(ax, (2.1, 6.0), (3.4, 6.0), kind="process")
bio.protein(ax, (4.2, 6.2), 1.4, 0.9, "receptor", text="E2")
ub((5.05, 6.65))
bio.arrow(ax, (5.1, 5.9), (6.2, 5.2), kind="process")
bio.protein(ax, (7.0, 4.6), 1.6, 1.0, "positive", text="E3")
bio.protein(ax, (8.9, 4.4), 1.6, 1.3, "protein", text="substrate")
bio.label(ax, (8.9, 3.45), "degron", size="tiny", color=P.muted())
for i in range(4):
    ub((9.6 + 0.32 * i, 5.3 + 0.36 * i))
bio.label(ax, (11.6, 6.6), "Lys48 chain", size="tiny")
bio.arrow(ax, (9.6, 3.4), (11.1, 3.0), kind="process")
# proteasome: 19S caps and 20S barrel
cx, cy = 12.1, 1.7
for k, (w, tok) in enumerate([(1.5, "neutral"), (1.3, "lysosome"), (1.3, "lysosome"), (1.3, "lysosome"), (1.3, "lysosome"), (1.5, "neutral")]):
    y = cy + 1.25 - k * 0.5
    bio.box(ax, (cx, y), w, 0.42, token=tok, radius=0.1)
bio.label(ax, (cx + 1.0, cy + 1.25), "19S", size="tiny", ha="left")
bio.label(ax, (cx + 1.0, cy + 0.25), "20S core (α β β α)", size="tiny", ha="left")
bio.label(ax, (cx + 1.0, cy - 1.25), "19S", size="tiny", ha="left")
bio.label(ax, (cx, cy - 1.85), "26S proteasome", size="small", bold=True)
bio.arrow(ax, (cx - 0.9, cy - 0.6), (cx - 2.2, cy - 1.3), kind="process")
bio.label(ax, (cx - 3.1, cy - 1.55), "peptides (3–25 aa)", size="tiny")
bio.arrow(ax, (cx + 0.3, cy + 1.5), (cx + 0.9, 4.0), kind="process", dashed=True)
ub((cx + 1.05, 4.2))
bio.label(ax, (cx + 1.4, 4.2), "Ub recycled", size="tiny", color=P.muted(), ha="left")

ax = fig.add_subplot(gs[1])
data = [("Ala, Gly, Met,\nSer, Thr, Val", 20 * 60, "positive"), ("Gln, Ile", 30, "neutral"), ("Glu, Tyr", 10, "neutral"),
        ("Pro", 7, "neutral"), ("Asp, Leu,\nLys, Phe", 3, "negative"), ("Arg", 2, "negative")]
y = np.arange(len(data))
ax.barh(y, [d[1] for d in data], color=[P.fill(d[2]) for d in data], edgecolor=[P.edge(d[2]) for d in data])
ax.set_xscale("log")
ax.set_yticks(y)
ax.set_yticklabels([d[0] for d in data], fontsize=7)
ax.invert_yaxis()
ax.set_xlim(1, 3000)
ax.set_xticks([1, 10, 60, 600])
ax.set_xticklabels(["1 min", "10 min", "1 h", "10 h"])
ax.text(20 * 60 * 1.1, 0, "> 20 h", fontsize=7, va="center", color=P.ink())
charts.style_axes(ax, "half-life in yeast", "N-terminal residue")
ax.set_title("B   The N-degron rule (β-galactosidase)", loc="left", fontsize=9, color=P.ink())
fig.tight_layout()
