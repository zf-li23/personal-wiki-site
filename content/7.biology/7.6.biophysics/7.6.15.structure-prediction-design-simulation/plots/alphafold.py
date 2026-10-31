# The flow of information in AlphaFold2 (schematic; block counts as in the 2021 model).
# A query sequence is used to search sequence databases (multiple sequence alignment, MSA, of N
# homologous sequences) and structure databases (templates). The Evoformer (48 blocks) updates two
# representations that exchange information in every block: the MSA representation (N x L), by
# attention along rows (residues) and columns (sequences), and the pair representation (L x L), by
# "triangle" updates that enforce consistency of distances among triples of residues. The structure
# module (8 blocks) treats every residue as a rigid frame (rotation and translation) and moves the frames
# with invariant point attention; side-chain torsion angles complete the all-atom model. The whole
# output is fed back three times (recycling). Outputs: coordinates, a per-residue confidence (pLDDT) and
# the predicted aligned error between residue pairs (PAE).
import matplotlib.pyplot as plt  # noqa: F401
import numpy as np

import wikibio as bio

P = bio.P
fig, ax = bio.canvas(26, 9)
muted = P.muted()

bio.box(ax, (2.0, 4.5), 3.0, 1.1, token="neutral", text="query sequence\n(L residues)", size="small")
bio.box(ax, (6.6, 6.6), 3.4, 1.3, token="dna", text="MSA\nN sequences × L", size="small")
bio.box(ax, (6.6, 2.4), 3.4, 1.3, token="metabolite", text="templates\n(PDB structures)", size="small")
bio.arrow(ax, (3.5, 4.8), (4.9, 6.4), kind="process")
bio.arrow(ax, (3.5, 4.2), (4.9, 2.6), kind="process")
bio.label(ax, (3.5, 6.3), "database\nsearch", size="tiny", color=muted)

# Evoformer
ax.add_patch(plt.Rectangle((9.4, 0.9), 6.6, 7.2, fill=False, ec=P.edge("protein"), lw=1.2, ls=(0, (4, 2))))
bio.label(ax, (12.7, 8.45), "Evoformer (48 blocks)", size="small", bold=True)
bio.box(ax, (12.7, 6.4), 5.2, 1.4, token="dna", text="MSA representation\n(N × L × c)", size="small")
bio.box(ax, (12.7, 2.6), 5.2, 1.4, token="protein", text="pair representation\n(L × L × c)", size="small")
bio.arrow(ax, (11.8, 5.6), (11.8, 3.4), kind="process")
bio.arrow(ax, (13.6, 3.4), (13.6, 5.6), kind="process")
bio.label(ax, (11.6, 4.5), "outer product\n(coevolution)", size="tiny", ha="right", color=muted)
bio.label(ax, (13.8, 4.5), "pair bias in\nattention", size="tiny", ha="left", color=muted)
bio.label(ax, (12.7, 7.4), "row and column attention", size="tiny", color=muted)
bio.label(ax, (12.7, 1.55), "triangle updates (i–j, j–k, i–k)", size="tiny", color=muted)
bio.arrow(ax, (8.3, 6.6), (10.1, 6.5), kind="process")
bio.arrow(ax, (8.3, 2.4), (10.1, 2.5), kind="process")

# Structure module
ax.add_patch(plt.Rectangle((17.0, 1.6), 4.4, 5.8, fill=False, ec=P.edge("enzyme"), lw=1.2, ls=(0, (4, 2))))
bio.label(ax, (19.2, 7.75), "structure module (8 blocks)", size="small", bold=True)
bio.box(ax, (19.2, 5.6), 3.8, 1.2, token="enzyme", text="residue frames\n(rotation + translation)", size="small")
bio.box(ax, (19.2, 3.3), 3.8, 1.2, token="enzyme", text="invariant point\nattention", size="small")
bio.arrow(ax, (19.2, 4.0), (19.2, 4.9), kind="process")
bio.arrow(ax, (15.3, 6.0), (17.3, 5.6), kind="process")
bio.arrow(ax, (15.3, 2.8), (17.3, 3.2), kind="process")
bio.label(ax, (16.3, 6.4), "single rep.", size="tiny", color=muted)

# output: a small backbone trace
t = np.linspace(0, 1, 120)
xs = 23.6 + 1.3 * np.cos(9 * t) * (0.6 + 0.4 * t)
ys = 4.6 + 2.6 * (t - 0.5) + 0.5 * np.sin(9 * t)
pl = np.clip(0.4 + 0.6 * np.sin(np.pi * t) ** 0.5, 0, 1)
for k in range(len(t) - 1):
    tok = "dna" if pl[k] > 0.85 else ("positive" if pl[k] > 0.7 else "highlight")
    ax.plot(xs[k:k + 2], ys[k:k + 2], color=P.edge(tok), lw=2.2, solid_capstyle="round")
bio.arrow(ax, (21.4, 4.5), (22.1, 4.5), kind="process")
bio.label(ax, (23.6, 1.6), "3D coordinates\ncoloured by pLDDT; PAE", size="small")
bio.label(ax, (23.6, 8.0), "pLDDT: blue high,\ngreen medium, yellow low", size="tiny", color=muted)

# recycling
bio.arrow(ax, (23.6, 7.4), (12.7, 8.8), kind="process", bend=-0.08, dashed=True)
bio.label(ax, (18.6, 8.75), "recycling (×3)", size="tiny", color=muted)
