# Stages of B-cell development: location, immunoglobulin gene status, receptor on the surface and the
# main surface markers, with the two checkpoints (pre-BCR and complete BCR) and the selection against
# self-reactivity at the immature stage.
import wikibio as bio
from wikibio import immuno

P = bio.P
fig, ax = bio.canvas(26, 11.2)

stages = [
    ("CLP", "germline", "germline", "none", "c-Kit, IL-7R"),
    ("Pre-pro-B", "germline", "germline", "none", "B220, EBF1"),
    ("Pro-B", "D–J, then\nV–DJ", "germline", "none", "CD19, CD79a/b,\nPAX5, RAG, TdT"),
    ("Large pre-B", "VDJ", "germline", "pre-BCR\n(μ + VpreB/λ5)", "CD19, IL-7R"),
    ("Small pre-B", "VDJ", "V–J", "none (RAG back on)", "CD19, CD25"),
    ("Immature B", "VDJ", "VJ", "IgM", "CD19, CD20"),
    ("Transitional\n(T1 → T2)", "VDJ", "VJ", "IgM > IgD", "CD24, CD93,\nCD21, BAFF-R"),
    ("Mature naive B", "VDJ", "VJ", "IgM + IgD", "CD19, CD20,\nCD21, CD23, MHC II"),
]
x0, dx = 2.9, 3.05
yc = 8.6
rows = [("Heavy chain", 6.55), ("Light chain", 5.55), ("Surface receptor", 4.45), ("Markers", 3.0)]

# compartments
bio.box(ax, (x0 - 0.2 + dx * 2.5, 10.6), dx * 6.0, 0.55, "extracellular", text="Bone marrow (stromal cells: CXCL12, SCF, IL-7)",
        size="small")
bio.box(ax, (x0 + dx * 6.5, 10.6), dx * 1.9, 0.55, "neutral", text="Spleen", size="small")
for name, y in rows:
    bio.label(ax, (0.15, y), name, size="tiny", ha="left", color=P.muted())

for k, (name, h, l, rec, mk) in enumerate(stages):
    x = x0 + k * dx
    kind = "lymphocyte"
    rtok = "antibody" if k >= 5 else ("receptor" if k == 3 else None)
    immuno.immune_cell(ax, (x, yc), r=0.62, kind=kind, token="neutral", receptor_token=rtok,
                       receptors=7 if rtok else 0, seed=k)
    bio.label(ax, (x, yc - 1.0), name, size="tiny", va="top")
    for txt, (_, y) in zip((h, l, rec, mk), rows):
        tok = None
        if txt in ("VDJ", "VJ"):
            tok = "positive"
        elif txt.startswith("D–J") or txt.startswith("V–J"):
            tok = "highlight"
        if tok:
            bio.box(ax, (x, y), 2.4, 0.62 if "\n" not in txt else 0.9, tok, text=txt, size="tiny")
        else:
            bio.label(ax, (x, y), txt, size="tiny", color=P.ink())
    if k < len(stages) - 1:
        bio.arrow(ax, (x + 0.75, yc), (x + dx - 0.75, yc), kind="process", head=0.16)

# checkpoints and selection
for k, text in ((3, "Checkpoint 1:\nfunctional μ chain\n(pre-BCR signal)"), (5, "Checkpoint 2:\ncomplete BCR\n+ self-reactivity test")):
    x = x0 + (k - 0.5) * dx
    ax.plot([x, x], [2.1, 9.7], color=P.edge("negative"), lw=1.4, ls=(0, (4, 3)), zorder=4)
    bio.label(ax, (x, 1.75), text, size="tiny", va="top", color=P.edge("negative"))
bio.label(ax, (x0 + 5 * dx + 1.3, 1.75), "self-reactive: editing,\ndeletion or anergy", size="tiny", va="top", ha="left",
          color=P.muted())
