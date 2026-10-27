"""The hematopoietic hierarchy (classical tree model; simplified).

A self-renewing hematopoietic stem cell (HSC) in the bone marrow gives rise to multipotent progenitors
(MPP), which split into a common myeloid progenitor (CMP) and a common lymphoid progenitor (CLP). The CMP
produces megakaryocyte-erythroid progenitors (MEP), the source of red blood cells and of megakaryocytes,
which shed platelets, and granulocyte-macrophage progenitors (GMP), the source of neutrophils, monocytes
(which become macrophages in tissues) and other granulocytes and mast cells; the CLP produces B, T and
natural killer cells (T cells mature in the thymus). Going down the tree, self-renewal and potency are lost
while proliferation and cell numbers increase: the progenitors are transit-amplifying cells. Lineage tracing
in unperturbed mice shows that much steady-state blood production comes from progenitors, and that the
megakaryocyte branch can arise close to the HSC; the tree is a simplification of a more continuous process.
"""

import wikibio as bio

P = bio.P
fig, ax = bio.canvas(24.0, 12.8)


def prog(xy, name, token="neutral", r=0.55):
    bio.cell(ax, xy, r, r, kind="animal", seed=int(xy[1] * 10))
    ax.add_patch(__import__("matplotlib").patches.Circle(xy, r * 0.55, facecolor=P.fill(token), edgecolor=P.edge(token), lw=1.0, zorder=9))
    bio.label(ax, (xy[0], xy[1] - r - 0.3), name, size="tiny")


bio.icon(ax, "servier/hematopoietic-stem-cell", at=(1.6, 6.4), height=1.5)
bio.label(ax, (1.6, 5.3), "HSC", size="small", bold=True)
bio.arrow(ax, (0.95, 7.15), (2.25, 7.15), kind="process", bend=0.55)
bio.label(ax, (1.6, 8.3), "self-renewal", size="tiny", color=P.muted())

nodes = {"MPP": (4.6, 6.4), "CMP": (7.8, 8.7), "CLP": (7.8, 3.2), "MEP": (11.0, 10.4), "GMP": (11.0, 7.4)}
for name, xy in nodes.items():
    prog(xy, name, token={"MPP": "highlight", "CMP": "drug", "CLP": "channel", "MEP": "blood", "GMP": "positive"}[name])
edges = [((1.6, 6.4), "MPP"), ("MPP", "CMP"), ("MPP", "CLP"), ("CMP", "MEP"), ("CMP", "GMP")]
for a, b in edges:
    pa = a if isinstance(a, tuple) else nodes[a]
    pb = nodes[b]
    bio.arrow(ax, (pa[0] + 0.75, pa[1]), (pb[0] - 0.7, pb[1]), kind="process")

terminal = [
    ("MEP", "servier/red-blood-cell", "Red blood cell", 12.2, 0.75),
    ("MEP", "servier/megakaryocyte", "Megakaryocyte", 10.9, 1.1),
    ("GMP", "servier/neutrophil", "Neutrophil", 9.1, 0.9),
    ("GMP", "servier/monocyte", "Monocyte", 7.8, 0.9),
    ("GMP", "bioicons/mast-cell", "Mast cell, eosinophil, basophil", 6.5, 0.9),
    ("CLP", "servier/b-cell", "B cell", 4.4, 0.85),
    ("CLP", "servier/t-cell", "T cell (thymus)", 3.1, 0.85),
    ("CLP", "servier/nk-cell", "NK cell", 1.8, 0.85),
]
X = 15.2
for parent, ic, name, y, h in terminal:
    p = nodes[parent]
    bio.arrow(ax, (p[0] + 0.7, p[1]), (X - 0.7, y), kind="process", color=P.muted(), lw=1.0)
    bio.icon(ax, ic, at=(X, y), height=h)
    bio.label(ax, (X + 0.8, y), name, size="tiny", ha="left")
bio.arrow(ax, (X + 3.3, 10.9), (21.5, 10.9), kind="process", color=P.muted(), lw=1.0)
bio.icon(ax, "servier/platelet", at=(22.2, 10.9), height=0.5)
bio.label(ax, (22.2, 10.35), "Platelets", size="tiny")
bio.arrow(ax, (X + 2.6, 7.8), (21.4, 7.8), kind="process", color=P.muted(), lw=1.0)
bio.icon(ax, "servier/macrophage", at=(22.2, 7.8), height=1.0)
bio.label(ax, (22.2, 7.0), "Macrophage (tissue)", size="tiny")

# gradients of potency and number
y0 = 0.4
for k in range(40):
    t = k / 39
    ax.add_patch(__import__("matplotlib").patches.Rectangle((1.0 + t * 13.0, y0), 13.0 / 40 + 0.01, 0.32,
                 facecolor=P.mix(P.fill("highlight"), P.surface(), t * 0.85), lw=0, zorder=2))
    ax.add_patch(__import__("matplotlib").patches.Rectangle((1.0 + t * 13.0, y0 + 0.45), 13.0 / 40 + 0.01, 0.32,
                 facecolor=P.mix(P.fill("drug"), P.surface(), (1 - t) * 0.85), lw=0, zorder=2))
bio.label(ax, (14.6, y0 + 0.16), "self-renewal, potency", size="tiny", ha="left")
bio.label(ax, (14.6, y0 + 0.61), "proliferation, cell number", size="tiny", ha="left")
