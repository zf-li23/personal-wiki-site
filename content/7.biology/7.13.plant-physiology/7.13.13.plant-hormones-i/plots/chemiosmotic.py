# Chemiosmotic model of polar auxin transport: one cell in a file of auxin-transporting cells.
# Acidic wall (pH ~5.5): ~15% of IAA undissociated (IAAH) diffuses in; IAA- enters with 2 H+ via AUX1/LAX.
# Neutral cytosol (pH ~7.2): IAA- is trapped and leaves only through basally localized PIN carriers (+ ABCB).
import wikibio as bio
from wikibio import P

fig, ax = bio.canvas(15, 12.4)

# cell wall background and three cells of a file
bio.box(ax, (6, 6.2), 6.6, 12.4, token="extracellular", radius=0.01, zorder=1)
bio.box(ax, (6, 11.7), 5.8, 1.9, token="cytoplasm", radius=0.3, zorder=2)
bio.box(ax, (6, 6.2), 5.8, 7.4, token="cytoplasm", radius=0.35, zorder=2)
bio.box(ax, (6, 0.7), 5.8, 1.9, token="cytoplasm", radius=0.3, zorder=2)
bio.vacuole(ax, (6.0, 6.0), 1.6, 1.5)
bio.label(ax, (6.0, 6.0), "Vacuole", size="small")
bio.label(ax, (4.4, 8.75), "Cytosol pH ≈ 7.2", size="small", ha="left")

# upper membrane: uptake
y_top = 9.9
bio.label(ax, (2.55, 10.3), "Cell wall\npH ≈ 5.5", size="small", ha="right")
bio.label(ax, (11.0, 10.85), "IAA⁻ + H⁺ ⇌ IAAH\n(about 15% as IAAH)", size="small", ha="left")
bio.arrow(ax, (10.9, 10.6), (9.4, 10.25), kind="link", color=P.muted(), lw=0.8)
# passive diffusion of IAAH
bio.label(ax, (4.7, 10.45), "IAAH", size="small")
bio.arrow(ax, (4.7, 10.2), (4.7, 8.9), kind="process", dashed=True)
bio.label(ax, (4.75, 8.25), "IAAH → IAA⁻ + H⁺", size="tiny", ha="left")
# AUX1 symport
bio.protein(ax, (7.4, y_top), 1.1, 0.55, token="channel", text="AUX1")
bio.label(ax, (7.4, 10.55), "IAA⁻ + 2H⁺", size="small")
bio.arrow(ax, (7.4, 10.35), (7.4, 9.0), kind="process", zorder=11)

# side membrane: H+-ATPase and nonpolar ABCB
bio.protein(ax, (3.1, 7.6), 0.7, 1.0, token="enzyme", text="H⁺\npump", size="tiny")
bio.label(ax, (3.55, 8.35), "ATP", size="tiny", ha="left")
bio.arrow(ax, (3.5, 7.6), (2.25, 7.6), kind="process", zorder=11)
bio.label(ax, (2.05, 7.95), "H⁺", size="small", ha="right")
for y in (5.2, 3.9):
    bio.protein(ax, (8.9, y), 0.65, 0.9, token="protein", text="ABCB", size="tiny")
bio.arrow(ax, (8.6, 4.55), (10.0, 4.55), kind="process")
bio.label(ax, (10.1, 4.55), "IAA⁻ (ATP-driven,\nnonpolar)", size="tiny", ha="left")

# basal membrane: polar PIN efflux
y_bot = 2.5
for x in (5.0, 7.0):
    bio.protein(ax, (x, y_bot), 1.0, 0.55, token="receptor", text="PIN")
    bio.arrow(ax, (x, 3.4), (x, 1.75), kind="process", zorder=11)
bio.label(ax, (6.0, 3.65), "IAA⁻", size="small")
bio.label(ax, (7.6, 1.95), "into wall, then next cell", size="tiny", ha="left")

# direction of transport
bio.arrow(ax, (13.6, 9.8), (13.6, 2.6), kind="process", lw=3.0, head=0.45)
bio.label(ax, (14.2, 6.2), "Polar auxin transport (shoot → root)", size="small", rotation=90)
bio.label(ax, (9.6, 1.0), "PIN at the basal end\nsets the direction", size="small", ha="left")
