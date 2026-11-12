# Stage-specifying factors in hemimetabolous and holometabolous development (schematic expression levels,
# after Truman & Riddiford 2022 and Belles & Santos 2014). Rows: JH / Kr-h1, Chinmo, Broad, E93; columns are
# stages (embryo, immature instars, pupa, adult). Bars show relative expression (not measured values).
import wikibio as bio
from matplotlib.patches import FancyBboxPatch

P = bio.P
fig, ax = bio.canvas(26, 13.5)

rows = [("JH and Kr-h1", "positive"), ("Chinmo", "plant"), ("Broad", "enzyme"), ("E93", "negative")]


def panel(y0, title, stages, levels):
    """levels: {row name: list of values 0..1 per stage}"""
    bio.label(ax, (0.4, y0 + 5.2), title, size="small", bold=True, ha="left")
    x0, w = 5.2, 20.0
    cw = w / len(stages)
    for k, s in enumerate(stages):
        cx = x0 + (k + 0.5) * cw
        bio.label(ax, (cx, y0 + 4.5), s, size="tiny")
        if k > 0:  # molt mark
            ax.plot([x0 + k * cw] * 2, [y0 + 0.15, y0 + 4.15], color=P.muted(), lw=0.5, ls=(0, (2, 2)), zorder=3)
    for r, (name, tok) in enumerate(rows):
        yy = y0 + 3.5 - r * 1.0
        bio.label(ax, (5.0, yy), name, size="small", ha="right")
        for k, v in enumerate(levels.get(name, [0] * len(stages))):
            if v <= 0:
                continue
            bw = cw * 0.86
            h = 0.7 * v
            ax.add_patch(FancyBboxPatch((x0 + k * cw + (cw - bw) / 2, yy - h / 2), bw, h,
                                        boxstyle="round,pad=0,rounding_size=0.12", facecolor=P.fill(tok),
                                        edgecolor=P.edge(tok), lw=0.8, zorder=6))


hemi = ["embryo", "N1", "N2", "N3", "N4", "N5 (last)", "adult"]
panel(7.0, "A  Hemimetabolous (e.g. cockroach, milkweed bug)", hemi,
      {"JH and Kr-h1": [0.6, 1, 1, 1, 1, 0, 0.8],
       "Broad": [0.4, 0.7, 0.8, 0.9, 1, 0.3, 0],
       "E93": [0, 0, 0, 0, 0, 1, 0.6],
       "Chinmo": [0.8, 0, 0, 0, 0, 0, 0]})
holo = ["embryo", "L1", "L2", "L3 (last)", "pupa", "adult"]
panel(0.6, "B  Holometabolous (e.g. fruit fly, flour beetle)", holo,
      {"JH and Kr-h1": [0.5, 1, 1, 0.25, 0, 0.8],
       "Chinmo": [1, 1, 1, 0.3, 0, 0],
       "Broad": [0, 0, 0, 1, 0.4, 0],
       "E93": [0, 0, 0, 0, 1, 0.6]})
bio.label(ax, (15.2, 0.25), "Schematic relative levels; dashed lines: molts. In adults JH acts as a gonadotropin.",
          size="tiny", color=P.muted())
