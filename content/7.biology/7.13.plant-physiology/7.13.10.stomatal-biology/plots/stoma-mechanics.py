# Kidney-shaped (most eudicots) and dumbbell-shaped (grasses) guard cells, open and closed, in surface view.
# Faint radial lines sketch the cellulose microfibrils of the kidney type; the thickened ventral wall
# (kidney) and the thick middle portion (dumbbell) are marked. Schematic, not to scale.
import numpy as np

import wikibio as bio
from wikibio import botany as B

P = bio.P
fig, ax = bio.canvas(20, 8.2)

cols = [2.6, 7.4, 12.6, 17.4]
y = 4.3
specs = [("kidney", "open", "A", "Kidney, open"),
         ("kidney", "closed", "B", "Kidney, closed"),
         ("dumbbell", "open", "C", "Dumbbell, open"),
         ("dumbbell", "closed", "D", "Dumbbell, closed")]
for x, (kind, state, letter, title) in zip(cols, specs):
    out = B.stoma(ax, (x, y), 3.6, angle=90, kind=kind, state=state)
    bio.panel(ax, letter, (x - 2.2, 7.6))
    bio.label(ax, (x, 7.55), title, size="small", bold=True)
    if kind == "kidney":
        # radial microfibrils fanning out from the pore across each guard cell
        pw = 0.38 if state == "open" else 0.08
        for side in (-1, 1):
            for phi in np.radians(np.linspace(-62, 62, 9)):
                x0, y0 = pw * np.cos(phi) + 0.06, 0.9 * np.sin(phi)
                x1, y1 = 1.25 * np.cos(phi), 1.6 * np.sin(phi)
                ax.plot([x + side * x0, x + side * x1], [y + y0, y + y1], color=P.muted(), lw=0.55, zorder=8.5)
    w = out.get("wall")
    if w is not None and state == "open":
        tx = x - 1.6 if kind == "kidney" else x + 1.9
        bio.callout(ax, w, (tx, y - 2.6), "thick wall", size="tiny")
bio.callout(ax, (cols[0] + 0.8, y + 1.0), (cols[0] + 1.8, y + 2.5), "microfibrils", size="tiny")
bio.callout(ax, (cols[2] - 0.75, y + 0.6), (cols[2] - 2.1, y + 2.6), "subsidiary cell", size="tiny")
bio.callout(ax, (cols[0] + 0.05, y - 0.4), (cols[0] + 1.9, y - 2.6), "pore", size="tiny")
bio.label(ax, (4.95, 0.55), "Turgor up: thin dorsal walls stretch, cells bow apart", size="tiny", color=P.muted())
bio.label(ax, (15.0, 0.55), "Turgor up: bulbous ends swell, rigid middles are pushed apart", size="tiny", color=P.muted())
