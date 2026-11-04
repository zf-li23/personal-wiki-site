"""Cell forms among the former Proteobacteria (schematic, not to a common scale; approximate cell sizes
in the labels). Rods with peritrichous flagella (Escherichia), a single polar flagellum (Pseudomonas) or
a curved rod (Vibrio); diplococci (Neisseria); a stalked cell with a holdfast (Caulobacter); a budding
cell at the tip of a hypha (Hyphomicrobium); a helical cell with a chain of magnetosomes
(Magnetospirillum); a helical cell with a polar tuft of flagella (Helicobacter); a gliding filament
with internal sulfur globules (Beggiatoa); and the small predatory vibrio Bdellovibrio."""
import numpy as np
from matplotlib.patches import Circle, FancyBboxPatch

import wikibio as bio
from wikibio import microbio as M

P = bio.P
fig, ax = bio.canvas(24, 11.5)


def name(x, y, genus, size):
    bio.label(ax, (x, y), genus, size="normal", italic=True)
    bio.label(ax, (x, y - 0.5), size, size="tiny", color=P.muted())


# row 1
M.bacillus(ax, (2.6, 9.0), 2.0, 0.8, gram="-", flagella="peritrichous", flagellum_length=1.0)
name(2.6, 6.9, "Escherichia", "1 x 2 µm")
M.bacillus(ax, (7.6, 9.0), 2.0, 0.7, gram="-", flagella="monotrichous", flagellum_length=1.6)
name(8.0, 6.9, "Pseudomonas", "0.6 x 2 µm")
M.vibrio(ax, (13.0, 9.0), 2.0, 0.65, angle=10, gram="-", flagella="monotrichous", flagellum_length=1.6)
name(13.4, 6.9, "Vibrio", "0.6 x 2 µm")
M.diplococcus(ax, (17.6, 9.0), 0.55, gram="-")
name(17.6, 6.9, "Neisseria", "pairs, 0.8 µm")
# Caulobacter: crescent with stalk and holdfast
M.vibrio(ax, (21.6, 9.6), 1.6, 0.55, angle=90, bend=0.3, gram="-", flagella=None)
ax.plot([21.6, 21.6], [8.9, 7.95], color=P.edge("gram_neg"), lw=2.2, solid_capstyle="round", zorder=7)
ax.add_patch(Circle((21.6, 7.9), 0.12, color=P.edge("carbohydrate"), zorder=8))
bio.callout(ax, (21.65, 8.4), (22.6, 8.1), "stalk", size="tiny")
bio.callout(ax, (21.6, 7.9), (22.6, 7.6), "holdfast", size="tiny")
name(21.6, 6.9, "Caulobacter", "0.5 x 2 µm")

# row 2
# Hyphomicrobium: mother cell, hypha, bud
M.coccus(ax, (1.6, 3.9), 0.5, gram="-")
xs = np.linspace(2.05, 3.9, 30)
ax.plot(xs, 3.9 + 0.12 * np.sin((xs - 2.05) * 2.2), color=P.edge("gram_neg"), lw=2.0, zorder=7)
M.coccus(ax, (4.2, 3.95), 0.35, gram="-")
bio.callout(ax, (4.3, 4.25), (4.9, 4.9), "bud", size="tiny")
name(2.9, 1.9, "Hyphomicrobium", "cell 0.6 x 1.5 µm")
# Magnetospirillum with magnetosome chain
M.spirillum(ax, (6.6, 3.9), (10.4, 3.9), width=0.34, turns=1.5, amplitude=0.35, gram="-", flagella="amphitrichous")
for x in np.linspace(7.9, 9.1, 7):
    ax.add_patch(Circle((x, 3.9 + 0.35 * np.sin(2 * np.pi * 1.5 * (x - 6.6) / 3.8) * 0.2), 0.07,
                        color=P.ink(), zorder=12))
bio.callout(ax, (8.5, 3.95), (8.9, 5.1), "magnetosome chain", size="tiny")
name(8.5, 1.9, "Magnetospirillum", "0.3 x 3 µm")
# Helicobacter
M.spirillum(ax, (12.0, 3.9), (14.4, 3.9), width=0.42, turns=1.2, amplitude=0.3, gram="-", flagella="lophotrichous")
name(13.0, 1.9, "Helicobacter", "0.5 x 3 µm")
# Beggiatoa filament with sulfur globules
x0, y0, w, h = 15.6, 3.55, 0.62, 0.7
for i in range(6):
    ax.add_patch(FancyBboxPatch((x0 + i * (w + 0.04), y0), w, h, boxstyle="round,pad=0,rounding_size=0.12",
                                facecolor=P.fill("gram_neg"), edgecolor=P.edge("gram_neg"), lw=0.9, zorder=8))
    for dx, dy in [(0.18, 0.22), (0.42, 0.45), (0.3, 0.5), (0.45, 0.18)]:
        ax.add_patch(Circle((x0 + i * (w + 0.04) + dx, y0 + dy), 0.06, color=P.fill("highlight"),
                            ec=P.edge("highlight"), lw=0.5, zorder=9))
bio.callout(ax, (16.5, 4.0), (16.4, 5.1), "sulfur globules", size="tiny")
bio.label(ax, (19.75, 3.9), "...", size="normal")
name(17.7, 1.9, "Beggiatoa", "filaments, cells 2-50 µm wide")
# Bdellovibrio, small, next to a prey cell for scale
M.bacillus(ax, (22.2, 4.3), 2.0, 0.8, gram="-", token="neutral")
M.vibrio(ax, (22.7, 3.2), 0.85, 0.32, angle=-20, gram="-", flagella="monotrichous", flagellum_length=0.9)
bio.callout(ax, (21.4, 4.3), (21.0, 5.2), "prey", size="tiny")
name(22.3, 1.9, "Bdellovibrio", "0.3 x 1 µm")
