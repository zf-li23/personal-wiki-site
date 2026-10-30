"""Salamander limb regeneration: stages, lineage restriction, and proximo-distal positional value.

A: stages after amputation through the forearm (skeletal elements colored: humerus, radius and ulna, carpals,
digits): within a day the wound epidermis covers the stump; it thickens into the apical epidermal cap (AEC)
while tissues beneath it dedifferentiate; a blastema accumulates and grows; the missing elements redifferentiate
in proximal-to-distal order. B: lineage tracing of grafted GFP-labeled tissues (axolotl, Kragl and colleagues
2009): each tissue gives back mainly itself (dermal fibroblasts also form cartilage and tendon); connective tissue
and cartilage cells keep their proximo-distal identity (a digit cell contributes only to digits), Schwann cells
do not. C: positional value: amputation at the wrist regenerates the hand; the same amputation followed by
retinoic acid (RA) treatment regenerates a whole limb from the humerus on (proximalization, serial duplication).
"""

from matplotlib.patches import FancyBboxPatch
import wikibio as bio

P = bio.P
LW = bio.core.LINE
fig, ax = bio.canvas(34.0, 17.0)


def rbox(x, y, w, h, tok, z=6, lw=LW * 0.8, light=False):
    ax.add_patch(FancyBboxPatch((x, y - h / 2), w, h, boxstyle=f"round,pad=0,rounding_size={min(w, h) * 0.3}",
                                fc=P.light(tok) if light else P.fill(tok), ec=P.edge(tok), lw=lw, zorder=z))


def skeleton(x, y, upto, scale=1.0, start="humerus", light_from=None):
    """Elements from ``start`` to ``upto`` (humerus, zeugopod, carpals, digits) drawn left to right."""
    order = ["humerus", "zeugopod", "carpals", "digits"]
    i0, i1 = order.index(start), order.index(upto)
    cx = x
    for k in range(i0, i1 + 1):
        name = order[k]
        lt = light_from is not None and k >= order.index(light_from)
        if name == "humerus":
            rbox(cx, y, 2.6 * scale, 0.42 * scale, "humerus", light=lt)
            cx += 2.75 * scale
        elif name == "zeugopod":
            rbox(cx, y + 0.24 * scale, 2.0 * scale, 0.3 * scale, "radius", light=lt)
            rbox(cx, y - 0.24 * scale, 2.0 * scale, 0.3 * scale, "ulna", light=lt)
            cx += 2.15 * scale
        elif name == "carpals":
            for j in range(3):
                rbox(cx + 0.02, y + (j - 1) * 0.36 * scale, 0.45 * scale, 0.28 * scale, "carpals", light=lt)
            cx += 0.6 * scale
        else:
            for j in range(4):
                rbox(cx, y + (j - 1.5) * 0.3 * scale, 1.3 * scale, 0.16 * scale, "phalanges", light=lt)
            cx += 1.4 * scale
    return cx


def skin(x0, x1, y, h, tok="animal", z=3):
    ax.add_patch(FancyBboxPatch((x0, y - h / 2), x1 - x0, h, boxstyle="round,pad=0,rounding_size=0.5",
                                fc=P.light(tok), ec=P.edge(tok), lw=LW, zorder=z))


# A: stages
bio.panel(ax, "A", (0.2, 16.8))
bio.label(ax, (1.4, 16.5), "Stages of regeneration after amputation through the forearm", size="small", bold=True,
          ha="left")
bio.icon(ax, "phylopic/axolotl", at=(30.5, 15.5), height=1.6, color="animal")
stages = ("amputation", "wound epidermis\n(6-12 h)", "AEC + dedifferentiation\n(days 2-5)",
          "blastema\n(days 7-10)", "redifferentiation\n(weeks)")
for i, name in enumerate(stages):
    y = 14.6 - 0.0 * i
    x = 0.6 + 6.6 * i
    # stump
    yc = 13.7
    skin(x, x + 3.8 + (1.6 if i >= 3 else 0.6 if i >= 1 else 0.0), yc, 1.6)
    rbox(x + 0.2, yc, 1.6, 0.42, "humerus")
    rbox(x + 1.95, yc + 0.24, 1.6, 0.3, "radius")
    rbox(x + 1.95, yc - 0.24, 1.6, 0.3, "ulna")
    end = x + 3.8
    if i == 0:
        ax.plot([end, end], [yc - 1.1, yc + 1.1], color=P.edge("negative"), lw=1.2, ls=(0, (3, 2)), zorder=9)
    if i >= 1:
        cap_w = 0.35 if i == 1 else 0.6
        ax.add_patch(FancyBboxPatch((end + (1.6 if i >= 3 else 0.6) - cap_w, yc - 0.8), cap_w, 1.6,
                                    boxstyle="round,pad=0,rounding_size=0.15", fc=P.fill("k"),
                                    ec=P.edge("k"), lw=LW * 0.8, zorder=7))
    if i == 2:
        ax.add_patch(FancyBboxPatch((end - 0.3, yc - 0.6), 0.6, 1.2, boxstyle="round,pad=0,rounding_size=0.2",
                                    fc=P.light("highlight"), ec=P.edge("highlight"), lw=LW * 0.6, ls=(0, (2, 2)),
                                    zorder=6))
    if i == 3:
        ax.add_patch(FancyBboxPatch((end - 0.1, yc - 0.65), 1.4, 1.3, boxstyle="round,pad=0,rounding_size=0.4",
                                    fc=P.fill("highlight"), ec=P.edge("highlight"), lw=LW * 0.8, zorder=6))
    if i == 4:
        rbox(end - 0.2, yc + 0.24, 0.6, 0.26, "radius", light=True)
        rbox(end - 0.2, yc - 0.24, 0.6, 0.26, "ulna", light=True)
        for j in range(3):
            rbox(end + 0.45, yc + (j - 1) * 0.3, 0.3, 0.22, "carpals", light=True)
        for j in range(4):
            rbox(end + 0.8, yc + (j - 1.5) * 0.24, 0.65, 0.12, "phalanges", light=True)
    bio.label(ax, (x + 2.6, 11.9), name, size="tiny")
    if i < 4:
        bio.arrow(ax, (x + 5.6, yc), (x + 6.3, yc), kind="process")
bio.label(ax, (17.0, 10.9), "purple: wound epidermis / AEC; yellow: blastema; pale bones: regenerated", size="tiny",
          color=P.muted())

# B: lineage restriction
bio.panel(ax, "B", (0.2, 9.9))
bio.label(ax, (1.4, 9.6), "Lineage tracing of GFP grafts", size="small", bold=True, ha="left")
rows = (("muscle", "muscle", "muscle", "not kept"),
        ("cartilage", "bone", "cartilage", "kept"),
        ("dermal fibroblasts", "animal", "cartilage, tendon, dermis", "kept"),
        ("Schwann cells", "neuron", "Schwann cells", "not kept"),
        ("epidermis", "k", "epidermis", "-"))
bio.label(ax, (2.0, 8.7), "grafted tissue", size="tiny", bold=True, ha="left")
bio.label(ax, (8.6, 8.7), "contributes to", size="tiny", bold=True, ha="left")
bio.label(ax, (14.6, 8.7), "keeps P-D identity", size="tiny", bold=True, ha="left")
for i, (src, tok, out, mem) in enumerate(rows):
    y = 7.9 - 0.95 * i
    rbox(1.4, y, 0.45, 0.45, tok)
    bio.label(ax, (2.0, y), src, size="tiny", ha="left")
    bio.arrow(ax, (6.6, y), (8.2, y), kind="process")
    bio.label(ax, (8.6, y), out, size="tiny", ha="left")
    col = P.edge("positive") if mem == "kept" else P.edge("negative") if mem == "not kept" else P.muted()
    bio.label(ax, (15.6, y), mem, size="tiny", ha="left", color=col, bold=mem != "-")
bio.label(ax, (9.0, 2.6), "axolotl: muscle comes from satellite cells; newt: from fragmented myofibers", size="tiny",
          color=P.muted())

# C: RA proximalizes
bio.panel(ax, "C", (19.0, 9.9))
bio.label(ax, (20.2, 9.6), "Retinoic acid resets positional value", size="small", bold=True, ha="left")
y1, y2 = 7.6, 4.4
skin(20.0, 28.4, y1, 1.3)
end = skeleton(20.2, y1, "carpals")
ax.plot([end - 0.05, end - 0.05], [y1 - 0.9, y1 + 0.9], color=P.edge("negative"), lw=1.0, ls=(0, (3, 2)), zorder=9)
skeleton(end, y1, "digits", start="digits", light_from="digits")
bio.label(ax, (31.2, y1), "control:\nhand", size="tiny", ha="left")
skin(20.0, 33.8, y2, 1.3)
end = skeleton(20.2, y2, "carpals", scale=0.85)
ax.plot([end - 0.05, end - 0.05], [y2 - 0.9, y2 + 0.9], color=P.edge("negative"), lw=1.0, ls=(0, (3, 2)), zorder=9)
skeleton(end, y2, "digits", start="humerus", scale=0.85, light_from="humerus")
bio.label(ax, (27.0, 2.9), "+ RA: humerus, radius, ulna and hand regenerate from the wrist", size="tiny")
bio.label(ax, (27.0, 2.2), "dashed red line: plane of amputation", size="tiny", color=P.muted())
