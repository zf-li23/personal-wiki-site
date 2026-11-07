"""Efferent pathways of the somatic and autonomic nervous systems, with transmitters and receptors.

Rows from top: somatic motor neuron (one neuron, ACh on muscle-type nicotinic receptors N_M);
parasympathetic (long preganglionic fibre, ganglion in or near the organ, short postganglionic fibre,
ACh on muscarinic receptors M); sympathetic (short preganglionic fibre to a paravertebral or prevertebral
ganglion, long postganglionic fibre, noradrenaline on alpha/beta adrenergic receptors); sympathetic
cholinergic fibres to sweat glands (ACh on M); the adrenal medulla, whose chromaffin cells are modified
postganglionic neurons that release adrenaline (~80 %) and noradrenaline into the blood.
All preganglionic neurons release ACh onto neuronal nicotinic receptors (N_N). Solid lines:
preganglionic (myelinated B fibres) or somatic; dashed: postganglionic (unmyelinated C fibres).
"""
from matplotlib.patches import Circle

import wikibio as bio

P = bio.P
fig, ax = bio.canvas(16, 9.6)
ink, edge = P.ink(), P.edge("neuron")

bio.box(ax, (1.3, 4.7), 2.0, 8.6, token="neuron", text="CNS", size="title")
rows = [
    (8.5, "Somatic motor", None, "skeletal muscle", "muscle", "ACh", "$\\mathrm{N_M}$"),
    (6.8, "Parasympathetic", 10.4, "heart, gut, glands", "neutral", "ACh", "M"),
    (5.1, "Sympathetic", 5.0, "heart, vessels, ...", "neutral", "NA", "$\\alpha$, $\\beta$"),
    (3.4, "Sympathetic (sweat glands)", 5.0, "sweat gland", "neutral", "ACh", "M"),
]
for y, name, gx, target, tok, nt, rec in rows:
    ax.add_patch(Circle((2.55, y), 0.17, facecolor=P.fill("neuron"), edgecolor=edge, lw=1.2, zorder=12))
    bio.label(ax, (2.9, y + 0.42), name, size="small", ha="left", bold=True)
    if gx is None:
        ax.plot([2.7, 12.4], [y, y], color=edge, lw=2.6, zorder=10)
    else:
        ax.plot([2.7, gx - 0.25], [y, y], color=edge, lw=2.6, zorder=10)
        ax.add_patch(Circle((gx, y), 0.28, facecolor=P.fill("neuron"), edgecolor=edge, lw=1.2, zorder=12))
        bio.label(ax, (gx, y - 0.55), "ACh $\\to$ $\\mathrm{N_N}$", size="tiny", color=P.muted())
        ax.plot([gx + 0.28, 12.4], [y, y], color=edge, lw=1.8, ls=(0, (4, 2)), zorder=10)
    bio.box(ax, (13.9, y), 2.8, 0.8, token=tok, text=target, size="small")
    bio.label(ax, (11.6, y + 0.32), f"{nt} $\\to$ {rec}", size="small")

y = 1.5
ax.add_patch(Circle((2.55, y), 0.17, facecolor=P.fill("neuron"), edgecolor=edge, lw=1.2, zorder=12))
bio.label(ax, (2.9, y + 0.42), "Adrenal medulla", size="small", ha="left", bold=True)
ax.plot([2.7, 6.55], [y, y], color=edge, lw=2.6, zorder=10)
bio.box(ax, (7.6, y), 2.1, 0.9, token="highlight", text="chromaffin cell", size="small")
bio.label(ax, (6.1, y - 0.6), "ACh $\\to$ $\\mathrm{N_N}$", size="tiny", color=P.muted())
bio.arrow(ax, (8.7, y), (12.4, y), kind="process", color=P.edge("blood"))
bio.label(ax, (10.6, y + 0.36), "adrenaline 80 %, NA 20 %", size="small")
bio.box(ax, (13.9, y), 2.8, 0.8, token="blood", text="blood", size="small")

bio.label(ax, (5.0, 0.35), "ganglion: paravertebral chain or prevertebral", size="tiny", color=P.muted())
ax.plot([3.2, 4.4], [9.35, 9.35], color=edge, lw=2.6)
bio.label(ax, (4.6, 9.35), "preganglionic / somatic", size="tiny", ha="left")
ax.plot([8.0, 9.2], [9.35, 9.35], color=edge, lw=1.8, ls=(0, (4, 2)))
bio.label(ax, (9.4, 9.35), "postganglionic", size="tiny", ha="left")
