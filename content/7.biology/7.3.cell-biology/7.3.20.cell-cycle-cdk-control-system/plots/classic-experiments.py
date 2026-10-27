"""Three classic experiments that revealed the cell-cycle control system (schematic).

(A) Maturation-promoting factor (Masui and Markert 1971; Smith and Ecker 1971). Cytoplasm taken from a mature
Xenopus egg arrested in metaphase of meiosis II and injected into an immature oocyte arrested in G2 of
meiosis I (large nucleus, the germinal vesicle) makes the oocyte break down its germinal vesicle, condense its
chromosomes and assemble a spindle without the hormone progesterone. Cytoplasm from the newly matured oocyte
does the same to a second oocyte (serial transfer, even with protein synthesis blocked): the activity
amplifies itself.
(B) Premature chromosome condensation (Johnson and Rao 1970). An M-phase HeLa cell fused with an interphase
cell (with inactivated Sendai virus or polyethylene glycol) forces the interphase nucleus to condense its
chromatin at once: a G1 nucleus gives long single chromatids, an S-phase nucleus fragmented ("pulverized")
chromatin with gaps where replication forks are active, and a G2 nucleus double chromatids.
(C) Fission yeast cell-division-cycle mutants (Nurse and colleagues, 1970s). Wild-type Schizosaccharomyces
pombe grows by tip extension and divides at about 14 um; temperature-sensitive cdc2 or cdc25 mutants at the
restrictive temperature keep growing without dividing; loss of wee1 makes cells divide at about half the
normal length; a dominant cdc2 allele (cdc2-1w) gives the same wee phenotype; cells lacking both wee1 and
cdc25 are viable and divide at a nearly normal size.
"""

import math

import numpy as np
from matplotlib.patches import Circle, Ellipse, FancyBboxPatch, Wedge

import wikibio as bio

P = bio.P
FT = bio.core.FONT

fig, ax = bio.canvas(27.0, 10.5)


def oocyte(c, r, gv=True, spindle=False):
    ax.add_patch(Circle(c, r, facecolor=P.fill("cytoplasm"), edgecolor=P.edge("cytoplasm"), lw=1.2, zorder=3))
    ax.add_patch(Wedge(c, r, 0, 180, facecolor=P.light("animal"), edgecolor="none", zorder=3.1))
    ax.add_patch(Circle(c, r, facecolor="none", edgecolor=P.edge("cytoplasm"), lw=1.2, zorder=3.2))
    if gv:
        ax.add_patch(Circle((c[0], c[1] + 0.25 * r), 0.36 * r, facecolor=P.fill("nucleus"), edgecolor=P.edge("nucleus"),
                            lw=1.0, zorder=4))
    if spindle:
        x, y = c[0], c[1] + 0.82 * r
        ax.add_patch(Ellipse((x, y), 0.26 * r, 0.12 * r, facecolor=P.light("channel"), edgecolor=P.edge("channel"),
                             lw=0.8, zorder=5))
        ax.plot([x - 0.02 * r, x + 0.02 * r], [y - 0.03 * r, y + 0.03 * r], color=P.edge("chromatin"), lw=2.2, zorder=6)


# ----- A
bio.panel(ax, "A", (0.2, 10.3))
oocyte((1.9, 6.0), 1.2, gv=False, spindle=True)
bio.label(ax, (1.9, 4.3), "mature egg\n(metaphase II)", size="tiny")
oocyte((5.4, 6.0), 1.2, gv=True)
bio.label(ax, (5.4, 4.3), "immature oocyte\n(G2 of meiosis I)", size="tiny")
bio.arrow(ax, (2.9, 7.4), (4.6, 7.4), kind="process", bend=-0.3, color=P.ink())
bio.label(ax, (3.75, 8.25), "inject cytoplasm", size="tiny", color=P.muted())
bio.arrow(ax, (5.4, 4.0 - 0.3), (5.4, 3.0), kind="process", color=P.ink())
oocyte((5.4, 1.65), 1.0, gv=False, spindle=True)
bio.label(ax, (7.35, 1.65), "germinal vesicle\nbreakdown, spindle\n(no progesterone)", size="tiny", ha="left")
bio.arrow(ax, (4.3, 1.5), (2.9, 1.5), kind="process", bend=0.3, color=P.ink(), dashed=True)
oocyte((1.9, 1.65), 1.0, gv=True)
bio.label(ax, (1.9, 0.25), "serial transfer: the\nactivity amplifies itself", size="tiny", color=P.muted())
bio.callout(ax, (5.4, 6.3), (7.35, 8.5), "germinal\nvesicle", size="tiny")
bio.label(ax, (3.6, 9.6), "MPF: a cytoplasmic factor triggers M phase", size="small", bold=True)

# ----- B
bio.panel(ax, "B", (9.3, 10.3))
bio.label(ax, (13.3, 9.6), "PCC: fusion with an M-phase cell", size="small", bold=True)


def fused(cx, cy, kind, title):
    for dx in (-0.8, 0.8):
        ax.add_patch(Circle((cx + dx, cy), 1.15, facecolor=P.fill("cytoplasm"), edgecolor="none", zorder=3))
    ax.add_patch(Ellipse((cx, cy), 4.1, 2.5, facecolor="none", edgecolor=P.edge("cytoplasm"), lw=1.1, zorder=3.3))
    # M-phase partner: condensed chromosomes (paired chromatids)
    rr = np.random.default_rng(3)
    for k in range(5):
        x0, y0 = cx - 1.2 + rr.uniform(-0.45, 0.45), cy + rr.uniform(-0.6, 0.6)
        th = rr.uniform(0, math.pi)
        dx, dy = 0.28 * math.cos(th), 0.28 * math.sin(th)
        for o in (-0.05, 0.05):
            ax.plot([x0 - dx + o, x0 + dx + o], [y0 - dy - o, y0 + dy - o], color=P.edge("chromatin"), lw=2.2,
                    solid_capstyle="round", zorder=5)
    # interphase partner: prematurely condensed chromosomes
    x1 = cx + 0.95
    rr = np.random.default_rng(7)
    for k in range(5):
        x0, y0 = x1 + rr.uniform(-0.45, 0.45), cy + rr.uniform(-0.65, 0.65)
        th = rr.uniform(0, math.pi)
        u = np.array([math.cos(th), math.sin(th)])
        if kind == "G1":
            t = np.linspace(-0.55, 0.55, 30)
            pts = np.array([x0, y0]) + t[:, None] * u + 0.08 * np.sin(9 * t)[:, None] * np.array([-u[1], u[0]])
            ax.plot(pts[:, 0], pts[:, 1], color=P.edge("chromatin"), lw=0.9, zorder=5)
        elif kind == "S":
            for t0 in (-0.5, -0.2, 0.15, 0.42):
                p = np.array([x0, y0]) + t0 * u
                ax.plot([p[0], p[0] + 0.13 * u[0]], [p[1], p[1] + 0.13 * u[1]], color=P.edge("chromatin"), lw=1.3,
                        solid_capstyle="round", zorder=5)
        else:
            nrm = np.array([-u[1], u[0]]) * 0.05
            t = np.linspace(-0.5, 0.5, 2)
            for o in (-1, 1):
                pts = np.array([x0, y0]) + t[:, None] * u + o * nrm
                ax.plot(pts[:, 0], pts[:, 1], color=P.edge("chromatin"), lw=0.9, zorder=5)
    bio.label(ax, (cx - 0.95, cy - 1.6), "M", size="small", bold=True, color=P.edge("negative"))
    bio.label(ax, (cx + 0.95, cy - 1.6), kind, size="small", bold=True)
    bio.label(ax, (cx, cy + 1.55), title, size="tiny", color=P.muted())


fused(11.4, 6.6, "G1", "single, long chromatids")
fused(15.6, 6.6, "S", "fragmented ('pulverized')")
fused(13.5, 2.3, "G2", "double chromatids")
bio.label(ax, (16.9, 2.3), "M-phase cytoplasm\ncondenses any\ninterphase nucleus", size="tiny", ha="left", color=P.muted())

# ----- C
bio.panel(ax, "C", (18.6, 10.3))
bio.label(ax, (22.8, 9.6), "Fission yeast cdc mutants", size="small", bold=True)
SC = 0.3  # canvas units per micrometre


def rod(x, y, L_um, nuclei=1, septum=False):
    L, W = L_um * SC, 3.5 * SC
    ax.add_patch(FancyBboxPatch((x, y - W / 2), L, W, boxstyle=f"round,pad=0,rounding_size={W / 2}",
                                facecolor=P.fill("cytoplasm"), edgecolor=P.edge("bacterium"), lw=1.1, zorder=4))
    if nuclei == 1:
        ax.add_patch(Circle((x + L / 2, y), 0.22, facecolor=P.fill("nucleus"), edgecolor=P.edge("nucleus"), lw=0.8, zorder=5))
    else:
        for f in (0.25, 0.75):
            ax.add_patch(Circle((x + f * L, y), 0.2, facecolor=P.fill("nucleus"), edgecolor=P.edge("nucleus"), lw=0.8, zorder=5))
    if septum:
        ax.plot([x + L / 2, x + L / 2], [y - W / 2 + 0.05, y + W / 2 - 0.05], color=P.edge("cell_wall"), lw=1.6, zorder=6)
    return x + L


rows = [("wild type", "divides at about 14 µm", 14.0, True, False),
        ("cdc2ts, cdc25ts (36 °C)", "no division, cells elongate", 25.0, False, True),
        ("wee1–", "divides at about 7 µm ('wee')", 7.0, True, False),
        ("wee1– cdc25Δ", "viable, near-normal size", 12.5, True, False)]
y = 8.3
for name, note, L, sep, long_ in rows:
    bio.label(ax, (19.0, y + 0.55), name, size="tiny", ha="left", italic=name != "wild type", bold=True)
    end = rod(19.0, y - 0.25, L, nuclei=2 if sep else 1, septum=sep)
    bio.label(ax, (19.0, y - 1.0), note, size="tiny", ha="left", color=P.muted())
    y -= 2.05
bio.scale_bar(ax, (19.0, 0.35), 10 * SC, "10 µm", size="tiny")
