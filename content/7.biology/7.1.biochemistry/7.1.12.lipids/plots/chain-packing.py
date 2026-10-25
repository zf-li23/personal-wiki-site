"""Packing of fatty acid chains (schematic). A: fully saturated chains (stearate, 18:0) are fully extended
zigzags that pack side by side in nearly crystalline order, every CH2 in van der Waals contact with its
neighbours. B: a cis double bond between C-9 and C-10 (oleate, 18:1(D9), red) puts a rigid bend of
about 30 degrees into the chain; mixed with saturated chains it disrupts the packing, weakens the
interactions and lowers the melting point. Circles are carboxylate head groups."""

import numpy as np
import wikibio as bio
from matplotlib.patches import Circle

P = bio.P
fig, ax = bio.canvas(18.0, 9.0)


def chain(x0, y0, cis=False, n=18, step=0.36, amp=0.13):
    """Zigzag of n carbons hanging down from a head group at (x0, y0); returns the carbon points."""
    d = np.array([0.0, -1.0])
    base = np.array([x0, y0 - 0.3])
    pts = []
    for i in range(n):
        if cis and i == 10:  # the bend at the cis double bond C9=C10
            ang = np.radians(30)
            d = np.array([[np.cos(ang), -np.sin(ang)], [np.sin(ang), np.cos(ang)]]) @ d
        nrm = np.array([-d[1], d[0]])
        pts.append(base + nrm * amp * (1 if i % 2 else -1))
        base = base + d * step
    pts = np.array(pts)
    ax.plot(pts[:, 0], pts[:, 1], color=P.edge("lipid_tail"), lw=2.0, solid_joinstyle="round", zorder=4)
    if cis:
        ax.plot(pts[8:10, 0], pts[8:10, 1], color=P.edge("negative"), lw=3.2, zorder=5)
    ax.add_patch(Circle((x0, y0), 0.25, facecolor=P.fill("lipid_head"), edgecolor=P.edge("lipid_head"), lw=1.0, zorder=6))
    return pts


bio.panel(ax, "A", (0.1, 8.9))
bio.label(ax, (0.9, 8.55), "Saturated: tight packing", bold=True, ha="left")
for k in range(9):
    chain(1.0 + k * 0.78, 7.6)

bio.panel(ax, "B", (9.2, 8.9))
bio.label(ax, (10.0, 8.55), "With cis-unsaturated chains: disorder", bold=True, ha="left")
for x, cis in ((9.9, True), (11.85, False), (12.75, False), (13.65, True), (15.6, False), (16.5, False)):
    chain(x, 7.6, cis=cis)
bio.label(ax, (4.2, 0.55), "mp of stearic acid 69.6 °C", size="small")
bio.label(ax, (13.6, 0.55), "mp of oleic acid 13.4 °C", size="small")
