# The course of an infection: a mucosal surface in cross-section, and the six steps with their factors.
import numpy as np
from matplotlib.patches import Rectangle

import wikibio as bio
from wikibio import microbio as M

P = bio.P
fig, ax = bio.canvas(19.0, 9.4)

# ================================================================ top: a mucosal surface
bio.label(ax, (0.4, 9.1), "A mucosal surface and the ways across it", size="title", bold=True, ha="left")

x0, x1 = 0.8, 12.4
ax.add_patch(Rectangle((x0, 4.6), x1 - x0, 1.9, facecolor=P.fill("extracellular"), edgecolor="none", zorder=1))
ax.add_patch(Rectangle((x0, 3.0), x1 - x0, 1.6, facecolor=P.light("protein"), edgecolor="none", zorder=1))
bio.label(ax, (x0 + 0.15, 6.3), "lumen", size="tiny", color=P.muted(), ha="left")
bio.label(ax, (x0 + 0.15, 4.35), "submucosa", size="tiny", color=P.on_fill(), ha="left")

# epithelium: a row of cells, with one M cell
cells = np.arange(x0 + 0.5, x1 - 0.4, 1.05)
m_index = 7
for i, cx in enumerate(cells):
    tok = "receptor" if i == m_index else "animal"
    bio.box(ax, (cx, 5.0), 0.95, 1.25, token=tok, radius=0.12)
bio.callout(ax, (cells[m_index], 5.65), (cells[m_index] + 0.1, 7.6),
            "M cell: samples the lumen,\nthin mucus, a standard way in")

# mucus layer with secretory IgA
mx = np.linspace(x0, x1, 400)
ax.fill_between(mx, 5.65, 5.65 + 0.30 + 0.06 * np.sin(mx * 3.1), color=P.fill("carbohydrate"),
                edgecolor="none", alpha=0.75, zorder=3)
bio.label(ax, (x1 - 0.2, 6.15), "mucus (mucin, secretory IgA): binds and is swept away",
          size="tiny", color=P.muted(), ha="right")

# bacteria: swept away, adhering, crossing at the M cell, spreading below
M.bacillus(ax, (2.0, 7.1), 0.75, 0.3, angle=20, gram="-", flagella="peritrichous")
bio.label(ax, (1.4, 8.1), "swept away", size="tiny", color=P.muted())
for cx in (4.3, 5.1):
    M.coccus(ax, (cx, 5.95), 0.2, gram="+")
bio.callout(ax, (4.7, 5.80), (4.9, 7.5), "adhesins bind\nhost receptors")
M.bacillus(ax, (cells[m_index], 6.1), 0.7, 0.28, angle=-80, gram="-")
bio.arrow(ax, (cells[m_index], 5.75), (cells[m_index], 4.35), kind="process")
M.bacillus(ax, (cells[m_index] + 0.5, 3.9), 0.7, 0.28, angle=15, gram="-")
M.bacillus(ax, (cells[m_index] - 0.9, 3.7), 0.7, 0.28, angle=-10, gram="-")

# a blood vessel below
ax.add_patch(Rectangle((x0 + 0.4, 3.08), x1 - x0 - 0.8, 0.46, facecolor=P.fill("blood"),
                       edgecolor=P.edge("blood"), lw=1.0, zorder=4))
bio.label(ax, (x0 + 1.3, 3.31), "blood and lymph: systemic spread", size="tiny",
          color=P.on_fill(), ha="left", zorder=6)
bio.arrow(ax, (cells[m_index] + 0.2, 3.62), (cells[m_index] + 0.2, 3.3), kind="process")

# a wound at the right end of the epithelium
bio.label(ax, (13.0, 7.9), "Other portals", size="small", bold=True, ha="left")
for k, t in enumerate(["skin: only through wounds, burns,\ncatheters or an arthropod bite",
                       "respiratory tract: the ciliary escalator\nand alveolar macrophages",
                       "gut: acid, bile, enzymes, and the\nresident microbiota (colonization resistance)",
                       "urogenital tract: flushing by urine,\nlow pH of the vagina"]):
    bio.label(ax, (13.0, 7.3 - k * 0.95), "• " + t, size="tiny", ha="left", color=P.ink())

# ================================================================ bottom: the six steps
y = 1.75
stages = [("Entry", "portal of entry;\nsurvive local defences"),
          ("Adhesion", "adhesins bind\nspecific receptors"),
          ("Colonization", "multiply; capsule,\nbiofilm, iron uptake"),
          ("Invasion", "degradative enzymes;\nzipper or trigger uptake"),
          ("Damage", "toxins, enzymes, and\nthe inflammatory response"),
          ("Transmission", "shedding in secretions,\nfaeces, lesions, blood")]
w = 2.75
for i, (title, sub) in enumerate(stages):
    cx = 1.9 + i * 2.95
    bio.box(ax, (cx, y), w, 1.25, token="positive" if i in (0, 5) else "neutral", radius=0.18)
    bio.label(ax, (cx, y + 0.36), title, size="small", bold=True, color=P.on_fill())
    bio.label(ax, (cx, y - 0.22), sub, size="tiny", color=P.on_fill())
    if i:
        bio.arrow(ax, (cx - w / 2 - 0.19, y), (cx - w / 2 - 0.01, y), kind="process")
bio.arrow(ax, (17.3, y - 0.75), (1.9, y - 0.75), kind="process", bend=0.12)
bio.label(ax, (14.6, 0.95), "to the next host", size="tiny", color=P.muted())
