"""Transepithelial transport: the distribution of transporters between apical and basolateral membranes.

A: glucose absorption by an enterocyte of the small intestine. Apical SGLT1 brings in 2 Na+ with each
glucose; basolateral GLUT2 lets glucose leave down its gradient into the blood; the basolateral
Na/K pump (3 Na+ out, 2 K+ in per ATP) keeps cytosolic Na+ low; K+ leaves through K+ channels.
Tight junctions seal the lateral spaces between cells and keep the apical and basolateral proteins apart.
B: acid secretion by a gastric parietal cell. Carbonic anhydrase makes H+ and HCO3- from CO2 and water;
the apical H+/K+-ATPase pumps H+ into the lumen in exchange for K+, which returns through apical K+
channels; Cl- follows through apical Cl- channels, so HCl is secreted; HCO3- leaves across the
basolateral membrane in exchange for Cl- (Cl-/HCO3- exchanger), and the Na/K pump works basolaterally.
"""

import numpy as np
from matplotlib.patches import Ellipse, Rectangle
import wikibio as bio
from wikibio import cellbio as CB

P = bio.P
fig, ax = bio.canvas(25.0, 10.2)
MH = CB.MH


def epithelium(x0, lumen_text, blood_text, microvilli):
    w, ytop, ybot = 10.4, 7.2, 2.4
    ax.add_patch(Rectangle((x0 - 0.6, ytop), w + 1.2, 2.3, facecolor=P.fill("extracellular"), edgecolor="none", zorder=0))
    ax.add_patch(Rectangle((x0 - 0.6, 0.4), w + 1.2, ybot - 0.4, facecolor=P.fill("blood"), edgecolor="none", alpha=0.18, zorder=0))
    ax.add_patch(Rectangle((x0 + 0.5, ybot), w - 1.0, ytop - ybot, facecolor=P.fill("cytoplasm"), edgecolor="none", zorder=1))
    bio.bilayer(ax, [(x0 + 0.5, ybot), (x0 + 0.5, ytop), (x0 + w - 0.5, ytop), (x0 + w - 0.5, ybot), (x0 + 0.5, ybot)], spacing=0.26)
    if microvilli:
        for k in range(9):
            cx = x0 + 1.4 + k * 1.0
            if k in (2, 6):
                continue
            ax.add_patch(Rectangle((cx - 0.17, ytop + MH), 0.34, 0.9, facecolor=P.fill("cytoplasm"), edgecolor=P.edge("lipid_head"), lw=0.9, zorder=2))
    # neighbouring cells and tight junctions
    for side in (-1, 1):
        xe = x0 + 0.5 if side < 0 else x0 + w - 0.5
        ax.add_patch(Rectangle((xe + side * 0.45 - (0.35 if side < 0 else 0), ybot), 0.35, ytop - ybot,
                               facecolor=P.fill("cytoplasm"), edgecolor=P.edge("lipid_head"), lw=0.9, zorder=1))
        ax.add_patch(Ellipse((xe + side * 0.2, ytop - 0.35), 0.5, 0.55, facecolor=P.fill("protein"), edgecolor=P.edge("protein"), lw=0.9, zorder=12))
    bio.callout(ax, (x0 + 0.3, ytop - 0.35), (x0 - 0.2, ytop + 1.6), "tight junction", size="tiny")
    bio.label(ax, (x0 + w / 2, ytop + 1.95), lumen_text, size="small", bold=True, color=P.muted())
    bio.label(ax, (x0 + 1.6, 0.8), blood_text, size="small", bold=True, color=P.muted())
    bio.label(ax, (x0 + 1.5, ytop - 0.9), "apical", size="tiny", color=P.muted())
    bio.label(ax, (x0 + 1.5, ybot + 0.9), "basolateral", size="tiny", color=P.muted())
    return ytop, ybot


def tag(xy, text, ha="left"):
    bio.label(ax, xy, text, size="tiny", ha=ha)


def basal_pump(xp, yb):
    """Na/K pump in a basolateral (bottom) membrane: the ATP-binding headpiece faces the cytosol above."""
    CB.carrier(ax, xp, yb, open="in", token="atp", width=1.4)
    bio.protein(ax, (xp + 0.55, yb + 0.95), 0.75, 0.55, "atp", wobble=0.08)
    bio.label(ax, (xp + 1.05, yb + 1.0), "ATP → ADP", size="tiny", ha="left")
    bio.label(ax, (xp + 1.0, yb - 0.05), "Na⁺/K⁺\npump", size="tiny", bold=True, ha="left")
    bio.arrow(ax, (xp - 0.45, yb + 1.3), (xp - 0.45, yb - 1.2), kind="process")
    bio.arrow(ax, (xp - 0.1, yb - 1.2), (xp - 0.1, yb + 1.3), kind="process")
    tag((xp - 0.55, yb - 1.35), "3 Na⁺", ha="right")
    tag((xp - 0.1, yb + 1.5), "2 K⁺", ha="center")


# ---------------- A: enterocyte
bio.panel(ax, "A", (0.1, 10.0))
x0 = 1.0
yt, yb = epithelium(x0, "Intestinal lumen", "Blood", microvilli=True)
xs = x0 + 3.5
CB.carrier(ax, xs, yt, open="out", token="channel", text=None)
bio.label(ax, (xs + 0.95, yt + 0.0), "SGLT1", size="small", bold=True, ha="left")
bio.arrow(ax, (xs - 0.25, yt + 1.2), (xs - 0.25, yt - 1.2), kind="process")
bio.arrow(ax, (xs + 0.25, yt + 1.2), (xs + 0.25, yt - 1.2), kind="process")
tag((xs - 0.4, yt + 1.35), "2 Na⁺", ha="right")
tag((xs + 0.4, yt + 1.35), "glucose")
# GLUT2
xg = x0 + 3.0
CB.carrier(ax, xg, yb, open="in", token="enzyme")
bio.label(ax, (xg - 0.9, yb + 0.0), "GLUT2", size="small", bold=True, ha="right")
bio.arrow(ax, (xg, yb + 1.2), (xg, yb - 1.2), kind="process")
tag((xg + 0.15, yb - 1.35), "glucose")
# Na/K pump
xp = x0 + 5.9
basal_pump(xp, yb)
# K channel
xk = x0 + 8.6
CB.channel(ax, xk, yb, token="k")
bio.arrow(ax, (xk, yb + 1.2), (xk, yb - 1.2), kind="process")
tag((xk + 0.15, yb - 1.35), "K⁺")
bio.label(ax, (x0 + 5.2, 5.0), "[glucose] high", size="tiny", color=P.muted())
bio.label(ax, (x0 + 5.2, 4.55), "[Na⁺] low, V_m ≈ −60 mV".replace("V_m", "Vm"), size="tiny", color=P.muted())

# ---------------- B: parietal cell
bio.panel(ax, "B", (12.9, 10.0))
x0 = 13.6
yt, yb = epithelium(x0, "Gastric lumen (pH ≈ 1)", "Blood", microvilli=False)
xh = x0 + 3.5
CB.pump(ax, xh, yt, token="atp")
bio.label(ax, (xh - 0.95, yt - 0.05), "H⁺/K⁺-\nATPase", size="tiny", bold=True, ha="right")
bio.arrow(ax, (xh - 0.55, yt - 1.6), (xh - 0.55, yt + 1.2), kind="process")
bio.arrow(ax, (xh - 0.2, yt + 1.2), (xh - 0.2, yt - 1.6), kind="process")
tag((xh - 0.65, yt + 1.35), "H⁺", ha="right")
tag((xh - 0.1, yt + 1.35), "K⁺")
xk = x0 + 5.8
CB.channel(ax, xk, yt, token="k")
bio.arrow(ax, (xk, yt - 1.2), (xk, yt + 1.2), kind="process")
tag((xk + 0.15, yt + 1.35), "K⁺")
xc = x0 + 7.5
CB.channel(ax, xc, yt, token="cl")
bio.arrow(ax, (xc, yt - 1.2), (xc, yt + 1.2), kind="process")
tag((xc + 0.15, yt + 1.35), "Cl⁻")
# carbonic anhydrase
bio.label(ax, (x0 + 4.4, 4.7), "CO₂ + H₂O → H⁺ + HCO₃⁻", size="tiny")
bio.label(ax, (x0 + 4.4, 4.25), "(carbonic anhydrase)", size="tiny", color=P.muted())
# Cl-/HCO3- exchanger
xe = x0 + 3.0
CB.carrier(ax, xe, yb, open="in", token="channel")
bio.label(ax, (xe - 0.9, yb), "AE2", size="small", bold=True, ha="right")
bio.arrow(ax, (xe - 0.25, yb + 1.2), (xe - 0.25, yb - 1.2), kind="process")
bio.arrow(ax, (xe + 0.25, yb - 1.2), (xe + 0.25, yb + 1.2), kind="process")
tag((xe - 0.35, yb - 1.35), "HCO₃⁻", ha="right")
tag((xe + 0.35, yb + 1.35), "Cl⁻")
xp = x0 + 6.3
basal_pump(xp, yb)
