"""Antibodies. A: domain diagram of immunoglobulin G: two heavy chains (VH, CH1, hinge, CH2, CH3) and
two light chains (VL, CL), interchain disulfide bonds, the papain cleavage sites in the hinge giving
two Fab fragments and one Fc fragment, the N-linked glycan on CH2, and the antigen-binding sites
formed by the hypervariable loops (CDRs) of VH and VL. B: sandwich ELISA. C: ELISA standard curve:
simulated absorbances of standards (duplicates, seed 0) fitted with a four-parameter logistic curve,
and an unknown read back from it."""

import math

import numpy as np
from matplotlib.patches import Circle, FancyBboxPatch
import wikibio as bio
from wikibio import charts, immuno, stats

P = bio.P
fig, ax = bio.canvas(23.0, 9.4)

# A: IgG domains
bio.panel(ax, "A", (0.1, 9.3))
bio.label(ax, (4.2, 9.0), "Immunoglobulin G (H₂L₂, about 150 kDa)", size="small", bold=True)
w, h = 0.62, 0.78
cx, base = 4.2, 0.9
for s in (-1, 1):                                    # Fc: CH3 and CH2 of both heavy chains
    x = cx + s * 0.36
    immuno.domain(ax, (x, base + 0.45), w, h, "antibody", text="CH3")
    immuno.domain(ax, (x, base + 1.35), w, h, "antibody", text="CH2")
    ax.add_patch(Circle((x + s * 0.55, base + 1.45), 0.11, facecolor=P.fill("carbohydrate"),
                        edgecolor=P.edge("carbohydrate"), lw=0.7, zorder=13))
bio.callout(ax, (cx + 0.91, base + 1.45), (cx + 2.0, base + 1.2), "N-glycan", size="tiny")
hinge_y = base + 1.95
for s in (-1, 1):
    ax.plot([cx + s * 0.36, cx + s * 0.55], [hinge_y, hinge_y + 0.55], color=P.edge("antibody"), lw=2.2, zorder=11)
for y in (hinge_y + 0.2, hinge_y + 0.38):            # heavy-heavy disulfides in the hinge
    ax.plot([cx - 0.4, cx + 0.4], [y, y], color=P.edge("highlight"), lw=1.4, zorder=12)
ang = 38.0
u = np.array([math.sin(math.radians(ang)), math.cos(math.radians(ang))])
for s in (-1, 1):
    us = np.array([s * u[0], u[1]])
    nrm = np.array([s * u[1], -u[0]])               # towards the outside of the arm
    start = np.array([cx + s * 0.6, hinge_y + 0.62])
    p1 = start + us * 0.45
    p2 = start + us * 1.35
    immuno.domain(ax, tuple(p1), w, h, "antibody", text="CH1", angle=-s * ang)
    immuno.domain(ax, tuple(p2), w, h, "antibody", text="VH", angle=-s * ang)
    q1 = p1 + nrm * 0.68
    q2 = p2 + nrm * 0.68
    immuno.domain(ax, tuple(q1), w, h, "protein", text="CL", angle=-s * ang)
    immuno.domain(ax, tuple(q2), w, h, "protein", text="VL", angle=-s * ang)
    m = (p1 + q1) / 2 - us * 0.42
    ax.plot(*np.array([p1 - us * 0.4, q1 - us * 0.4]).T, color=P.edge("highlight"), lw=1.4, zorder=13)
    tip = (p2 + q2) / 2 + us * 0.55
    for k in (-1, 0, 1):
        ax.add_patch(Circle(tuple(tip + nrm * 0.22 * k), 0.07, color=P.edge("negative"), zorder=14))
    if s == 1:
        bio.callout(ax, tuple(tip + nrm * 0.22), tuple(tip + np.array([0.9, 0.35])), "CDR loops:\nantigen-binding site",
                    size="tiny")
# papain cleavage marks
for s in (-1, 1):
    ax.plot([cx + s * 0.2, cx + s * 0.95], [hinge_y + 0.03, hinge_y + 0.03], color=P.edge("negative"), lw=1.2,
            ls=(0, (2, 1.5)), zorder=15)
bio.callout(ax, (cx - 0.95, hinge_y + 0.03), (cx - 2.4, hinge_y - 0.35), "papain\ncleaves here", size="tiny")
bio.label(ax, (cx - 2.5, 5.7), "Fab", size="normal", bold=True)
bio.label(ax, (cx + 2.5, 6.2), "Fab", size="normal", bold=True)
bio.label(ax, (cx - 1.7, base + 0.9), "Fc", size="normal", bold=True)
bio.label(ax, (cx + 2.2, 3.5), "heavy chain", size="tiny", color=P.edge("antibody"), ha="left")
bio.label(ax, (cx + 2.2, 3.1), "light chain", size="tiny", color=P.edge("protein"), ha="left")
bio.label(ax, (cx + 2.2, 2.7), "S–S bonds", size="tiny", color=P.edge("highlight"), ha="left")

# B: sandwich ELISA
bio.panel(ax, "B", (8.4, 9.3))
bio.label(ax, (11.9, 9.0), "Sandwich ELISA", size="small", bold=True)
steps = ["1 capture\nantibody\ncoated", "2 block;\nantigen\nbinds", "3 enzyme-\nlinked detection\nantibody",
         "4 substrate →\ncolour ∝\n[antigen]"]
for k, txt in enumerate(steps):
    x0 = 8.9 + k * 1.85
    y0 = 3.2
    xc = x0 + 0.8
    ax.add_patch(FancyBboxPatch((x0, y0), 1.6, 0.22, boxstyle="round,pad=0,rounding_size=0.05",
                                facecolor=P.fill("neutral"), edgecolor=P.edge("neutral"), lw=0.8))
    bio.structures.antibody(ax, (xc, y0 + 0.82), size=1.0, angle=0)
    if k >= 1:
        bio.protein(ax, (xc, y0 + 1.6), 0.6, 0.45, "drug", text="Ag", size="tiny")
    if k >= 2:
        bio.structures.antibody(ax, (xc, y0 + 2.4), size=1.0, angle=180)
        ax.add_patch(Circle((xc, y0 + 3.1), 0.2, facecolor=P.fill("enzyme"), edgecolor=P.edge("enzyme"), lw=0.8,
                            zorder=14))
        bio.label(ax, (xc, y0 + 3.1), "E", size="tiny", color=P.on_fill(), zorder=15)
    if k == 3:
        for d in range(5):
            ax.add_patch(Circle((xc - 0.4 + 0.2 * d, y0 + 3.6 + 0.14 * (d % 2)), 0.07, color=P.edge("highlight"),
                                zorder=14))
    bio.label(ax, (xc, y0 - 0.25), txt, size="tiny", va="top")
    if k < 3:
        bio.arrow(ax, (x0 + 1.62, y0 + 1.6), (x0 + 1.86, y0 + 1.6), kind="process", head=0.12)

# C: standard curve
bio.panel(ax, "C", (16.3, 9.3))
pc = charts.axes_at(ax, (17.6, 1.4, 5.0, 6.8))
rng = np.random.default_rng(0)
conc = np.repeat(1000.0 / 2.0 ** np.arange(9)[::-1], 2)          # pg/mL, two-fold series
true = (0.06, 2.4, math.log10(120.0), 1.1)
A = stats.four_pl(conc, *true) * (1 + rng.normal(0, 0.04, conc.size))
fit = stats.fit_4pl(conc, A)
xx = np.logspace(0.3, 3.1, 300)
lo, hi = fit.band(xx)
pc.fill_between(xx, lo, hi, color=P.mix(P.fill("enzyme"), P.surface(), 0.55), lw=0)
pc.plot(xx, fit.predict(xx), color=charts.line("enzyme"), lw=1.7)
pc.plot(conc, A, "o", ms=3.3, mfc="none", mec=charts.line("enzyme"), mew=1.0)
bottom, top, lec, hill = fit.params
a_unknown = 1.1
x_unknown = 10 ** (lec - math.log10((top - bottom) / (a_unknown - bottom) - 1) / hill)
pc.plot([xx[0], x_unknown, x_unknown], [a_unknown, a_unknown, 0], color=charts.line("drug"), lw=0.9, ls="--")
pc.text(x_unknown * 1.15, 0.12, f"unknown: {x_unknown:.0f} pg/mL", fontsize=bio.core.FONT["tiny"], color=P.ink())
pc.text(2.4, 2.35, f"EC50 = {10 ** lec:.0f} pg/mL\nHill slope = {hill:.2f}", fontsize=bio.core.FONT["tiny"], color=P.ink(),
        va="top")
pc.set_xscale("log")
pc.set_xlim(xx[0], xx[-1])
pc.set_ylim(0, 2.6)
charts.style_axes(pc, "antigen / (pg/mL)", "absorbance at 450 nm")
charts.title(pc, "Standard curve (4PL fit)")
