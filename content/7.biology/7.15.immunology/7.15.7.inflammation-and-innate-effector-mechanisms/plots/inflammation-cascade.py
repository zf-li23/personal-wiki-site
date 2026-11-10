# The acute inflammatory cascade.
# A: a venule above infected tissue. Sentinel cells (macrophage, mast cell) sense bacteria and release
#    mediators; the endothelium is activated, plasma proteins leak out and leukocytes extravasate
#    (rolling, firm adhesion, transmigration). Systemic effects of TNF, IL-1 and IL-6 at the right.
# B: qualitative time course of the cellular infiltrate (no numerical data).
import numpy as np
from matplotlib.patches import Ellipse, Rectangle

import wikibio as bio
from wikibio import immuno, quant

P = bio.P
fig, ax = bio.canvas(19.6, 8.6)

# --- A  local events --------------------------------------------------------------------------------
bio.panel(ax, "A", (0.1, 8.4))
bio.label(ax, (6.0, 8.25), "Local inflammation", size="title", bold=True)

# venule (lumen) and endothelium
ax.add_patch(Rectangle((0.6, 5.6), 11.0, 1.7, facecolor=P.fill("blood"), edgecolor="none", alpha=0.35, zorder=1))
for yy in (5.6, 7.3):
    ax.plot([0.6, 11.6], [yy, yy], color=P.edge("blood"), lw=2.2, zorder=3)
bio.label(ax, (0.65, 7.55), "venule (blood flow →)", size="small", ha="left", color=P.muted())
bio.label(ax, (0.75, 5.05), "tissue", size="small", ha="left", color=P.muted())

# leukocyte adhesion cascade along the lower endothelial wall
steps = [(1.9, 6.25, "flowing"), (3.6, 5.95, "rolling\n(selectins)"), (5.3, 5.88, "firm adhesion\n(integrins)")]
for x, y, t in steps:
    immuno.immune_cell(ax, (x, y), r=0.32, kind="lymphocyte", token="neutral", seed=int(x * 3))
    bio.label(ax, (x, 6.85), t, size="tiny", color=P.ink())
bio.arrow(ax, (2.3, 6.2), (3.15, 6.0), kind="process", shrink=0.05)
bio.arrow(ax, (4.0, 5.95), (4.85, 5.9), kind="process", shrink=0.05)
immuno.immune_cell(ax, (6.7, 5.25), r=0.32, kind="lymphocyte", token="neutral", seed=7)
bio.label(ax, (7.15, 5.15), "transmigration\n(diapedesis)", size="tiny", ha="left")
bio.arrow(ax, (5.55, 5.7), (6.45, 5.45), kind="process")
# neutrophils and monocytes in tissue moving to the focus
immuno.immune_cell(ax, (4.4, 3.5), r=0.32, kind="lymphocyte", token="neutral", seed=11)
bio.label(ax, (4.4, 2.95), "neutrophil", size="tiny")
immuno.immune_cell(ax, (7.6, 3.7), r=0.38, kind="lymphocyte", token="lysosome", seed=12)
bio.label(ax, (7.6, 3.1), "monocyte → macrophage", size="tiny")
bio.arrow(ax, (6.6, 4.9), (4.8, 3.8), kind="process", dashed=True)

# infection focus: bacteria
rng = np.random.default_rng(3)
for i in range(9):
    cx, cy = 2.0 + rng.uniform(-0.8, 0.8), 2.2 + rng.uniform(-0.6, 0.6)
    ax.add_patch(Ellipse((cx, cy), 0.42, 0.2, angle=rng.uniform(0, 180), facecolor=P.fill("bacterium"),
                         edgecolor=P.edge("bacterium"), lw=0.7, zorder=8))
bio.label(ax, (2.0, 1.2), "bacteria (PAMPs)\ndamaged cells (DAMPs)", size="tiny")

# sentinel cells
immuno.immune_cell(ax, (3.9, 1.6), r=0.5, kind="lymphocyte", token="lysosome", seed=2)
bio.label(ax, (3.9, 0.85), "resident macrophage", size="tiny")
immuno.immune_cell(ax, (6.5, 2.0), r=0.5, kind="lymphocyte", token="highlight", seed=4)
for k in range(10):
    a = 2 * np.pi * k / 10
    ax.add_patch(Ellipse((6.5 + 0.35 * np.cos(a), 2.0 + 0.35 * np.sin(a)), 0.1, 0.1,
                         facecolor=P.edge("highlight"), edgecolor="none", zorder=12))
bio.label(ax, (6.5, 1.25), "mast cell", size="tiny")

# mediators acting on the vessel
bio.box(ax, (9.7, 1.55), 3.2, 1.25, "neutral",
        "TNF-α, IL-1β, IL-6\nchemokines (CXCL8, CCL2)\nhistamine, prostaglandins", size="tiny")
bio.arrow(ax, (4.4, 1.7), (8.05, 1.6), kind="process", shrink=0.05)
bio.arrow(ax, (7.0, 2.05), (8.05, 1.9), kind="process", shrink=0.05)
bio.arrow(ax, (9.7, 2.2), (9.7, 5.5), kind="activation")
bio.label(ax, (9.55, 4.45), "vasodilation\npermeability ↑\nE-/P-selectin, ICAM-1", size="tiny", ha="right")
# plasma leak
bio.arrow(ax, (11.35, 5.55), (11.35, 3.55), kind="process", dashed=True)
bio.label(ax, (11.35, 3.05), "plasma: complement,\nantibodies, kinins", size="tiny")

# systemic effects
bio.label(ax, (13.75, 7.75), "Systemic effects of\nTNF, IL-1, IL-6", size="small", bold=True)
for k, (txt, tok) in enumerate((("hypothalamus: PGE2 → fever", "highlight"),
                                ("liver: acute-phase proteins\n(CRP, SAA, MBL, fibrinogen)", "enzyme"),
                                ("bone marrow:\nneutrophil release", "blood"))):
    bio.box(ax, (13.75, 6.45 - k * 1.25), 3.3, 0.95, tok, txt, size="tiny")
bio.arrow(ax, (11.65, 6.45), (12.05, 6.45), kind="process")

# --- B  time course ----------------------------------------------------------------------------------
bio.panel(ax, "B", (15.7, 8.4))
bio.label(ax, (17.8, 8.25), "Infiltrate", size="title", bold=True)
pl = quant.Plot(ax, (16.2, 1.6, 3.1, 5.8), xlim=(0, 6), ylim=(0, 1.15), xlabel="days", ylabel="cells at site (relative)",
                xticks=[0, 1, 2, 3, 4, 5, 6], yticks=[], ylabel_offset=0.3)
t = np.linspace(0, 6, 400)
neut = (t / 0.6) ** 2 * np.exp(-t / 0.35) / ((0.6 / 0.6) ** 2 * np.exp(-0.6 / 0.35)) * 1.0
neut = t ** 2 * np.exp(-t / 0.3)
neut = neut / neut.max()
mono = t ** 3 * np.exp(-t / 0.75)
mono = 0.8 * mono / mono.max()
pl.line(t, neut, "negative", text="neutrophils", at=0.12, dx=0.15, dy=0.05)
pl.line(t, mono, "lysosome")
bio.label(ax, pl.xy(2.3, 0.9), "monocytes /\nmacrophages", size="tiny", color=quant.line_color("lysosome"))
pl.span(4.0, 6.0, "positive", strength=0.25)
bio.label(ax, pl.xy(5.0, 1.08), "resolution", size="tiny", color=P.muted())
