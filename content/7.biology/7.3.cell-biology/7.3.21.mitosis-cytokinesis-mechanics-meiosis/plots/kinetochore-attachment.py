"""The kinetochore, kinds of attachment and error correction by Aurora B (schematic).

(A) Layers of a human kinetochore on one sister chromatid: centromeric chromatin with nucleosomes containing
the histone H3 variant CENP-A; the inner kinetochore (CCAN, the constitutive centromere-associated network of
16 proteins including CENP-C and CENP-T); the outer kinetochore (KMN network: Knl1, Mis12 complex and the
Ndc80 complex), whose rod-shaped Ndc80 complexes bind the sides of the microtubule near its plus end; the
fibrous corona (dynein, CENP-E, the RZZ complex and Mad1-Mad2) on unattached kinetochores. Aurora B, part of
the chromosomal passenger complex, sits at the inner centromere between the sisters.
(B) Attachment states: unattached; monotelic (one sister attached); syntelic (both sisters to one pole);
merotelic (one kinetochore to both poles); amphitelic (bi-oriented, correct). Only amphitelic attachment
generates full tension across the sister pair.
(C) The spatial separation model of tension sensing. Without tension the outer kinetochore lies within reach
of Aurora B, which phosphorylates the Ndc80 tail and weakens microtubule binding, so the attachment is
released and tried again; under tension the outer kinetochore is pulled away from the inner centromere, out
of reach, PP1 and PP2A-B56 dephosphorylate Ndc80, and the attachment is stabilized.
"""

import numpy as np
from matplotlib.patches import Circle, Ellipse, FancyBboxPatch, Rectangle

import wikibio as bio
from wikibio import cytoskel as C

P = bio.P
FT = bio.core.FONT

fig, ax = bio.canvas(27.0, 12.0)

# ----- A
bio.panel(ax, "A", (0.2, 11.8))
x0, y0 = 1.0, 2.0
layers = [("centromeric chromatin\n(CENP-A nucleosomes)", "chromatin", 1.6),
          ("inner kinetochore\n(CCAN: CENP-C, CENP-T)", "protein", 1.0),
          ("outer kinetochore\n(KMN: Knl1, Mis12, Ndc80)", "negative", 1.0)]
x = x0
for name, tok, w in layers:
    ax.add_patch(FancyBboxPatch((x, y0), w, 7.0, boxstyle="round,pad=0,rounding_size=0.2", facecolor=P.fill(tok),
                                edgecolor=P.edge(tok), lw=1.0, zorder=3))
    bio.label(ax, (x + w / 2, y0 + 3.5), name.replace("\n", " "), size="tiny", rotation=90, color=P.on_fill(), zorder=6)
    x += w + 0.15
for yy in np.linspace(y0 + 0.8, y0 + 6.2, 5):
    ax.add_patch(Circle((x0 + 0.35, yy), 0.25, facecolor=P.fill("highlight"), edgecolor=P.edge("highlight"), lw=0.8, zorder=4))
# Ndc80 rods and microtubules
xo = x0 + 1.6 + 0.15 + 1.0 + 0.15 + 1.0
for k, ym in enumerate((y0 + 1.8, y0 + 3.6, y0 + 5.4)):
    C.tube(ax, (8.6, ym), (xo + 0.35, ym), width=0.42, plus="none")
    for dy in (-0.32, 0.32):
        ax.plot([xo - 0.2, xo + 0.75], [ym + dy * 1.9, ym + dy], color=P.edge("negative"), lw=1.6, zorder=9)
        ax.add_patch(Circle((xo + 0.78, ym + dy), 0.08, color=P.edge("negative"), zorder=10))
bio.label(ax, (xo + 1.2, y0 + 6.6), "Ndc80 complexes\nbind microtubule sides", size="tiny", ha="left")
bio.label(ax, (7.9, y0 + 0.6), "kinetochore microtubules\n(plus ends embedded)", size="tiny")
ax.add_patch(Ellipse((x0 - 0.4, y0 + 3.5), 0.8, 1.6, facecolor=P.fill("drug"), edgecolor=P.edge("drug"), lw=0.9, zorder=5))
bio.label(ax, (x0 - 0.4, y0 + 3.5), "Aur\nB", size="tiny", bold=True, color=P.on_fill(), zorder=6)
bio.label(ax, (5.3, 11.0), "a kinetochore binds 10–40 microtubules (yeast: 1)", size="tiny", color=P.muted())

# ----- B
bio.panel(ax, "B", (10.2, 11.8))
kinds = [("unattached", ()), ("monotelic", ("L",)), ("syntelic", ("LL",)), ("merotelic", ("L", "R", "LR")),
         ("amphitelic", ("L", "R"))]
xs = np.linspace(11.6, 25.4, 5)
yc = 8.3
for (name, att), x in zip(kinds, xs):
    lp, rp = np.array([x - 1.35, yc]), np.array([x + 1.35, yc])
    for p in (lp, rp):
        ax.add_patch(Circle(p, 0.16, facecolor=P.fill("neutral"), edgecolor=P.edge("neutral"), lw=0.8, zorder=6))
    cp = C.chromatid_pair(ax, (x, yc), length=1.4, width=0.2, angle=90, facing=0)
    kr, kl = cp["attach"]  # facing 0 (right) and 180 (left)
    if "L" in att:
        C.mt_line(ax, lp, kl, lw=1.5)
    if "R" in att:
        C.mt_line(ax, rp, kr, lw=1.5)
    if "LL" in att:
        C.mt_line(ax, lp, kl, lw=1.5)
        C.mt_line(ax, lp + np.array([0, 0.1]), kr + np.array([0, 0.25]), lw=1.5)
    if "LR" in att:
        C.mt_line(ax, rp + np.array([0, -0.1]), kl + np.array([0, -0.25]), lw=1.5)
    ok = name == "amphitelic"
    bio.label(ax, (x, yc - 1.15), name, size="tiny", bold=True, color=P.edge("positive") if ok else P.ink())
    bio.label(ax, (x, yc - 1.6), "tension, stable" if ok else ("SAC signal" if name in ("unattached", "monotelic") else
                                                               "low tension: corrected" if name == "syntelic" else
                                                               "tension: escapes SAC"),
              size="tiny", color=P.muted())

# ----- C
bio.panel(ax, "C", (10.2, 5.4))
for i, (title, sep, phos) in enumerate((("low tension", 0.5, True), ("high tension", 1.3, False))):
    cx = 14.0 + i * 8.0
    cy = 2.6
    bio.label(ax, (cx, 4.9), title, size="small", bold=True)
    ax.add_patch(Circle((cx, cy), 1.25 * (0.9 + 0.25 * i), facecolor=P.fill("drug"), alpha=0.25, edgecolor="none", zorder=2))
    ax.add_patch(Ellipse((cx, cy), 0.7, 0.9, facecolor=P.fill("drug"), edgecolor=P.edge("drug"), lw=0.9, zorder=5))
    bio.label(ax, (cx, cy), "Aur B", size="tiny", bold=True, color=P.on_fill(), zorder=6)
    for s in (-1, 1):
        inner = cx + s * 0.65
        outer = cx + s * (0.65 + sep)
        ax.add_patch(Rectangle((inner - 0.12, cy - 0.7), 0.24, 1.4, facecolor=P.fill("protein"), edgecolor=P.edge("protein"),
                               lw=0.8, zorder=4))
        ax.plot([inner, outer], [cy + 0.3, cy + 0.3], color=P.muted(), lw=1.0, ls=":", zorder=4)
        ax.plot([inner, outer], [cy - 0.3, cy - 0.3], color=P.muted(), lw=1.0, ls=":", zorder=4)
        ax.add_patch(Rectangle((outer - 0.12, cy - 0.8), 0.24, 1.6, facecolor=P.fill("negative"), edgecolor=P.edge("negative"),
                               lw=0.8, zorder=4))
        C.mt_line(ax, (outer + s * 0.1, cy), (outer + s * 2.4, cy), lw=1.6)
        if phos:
            ax.add_patch(Circle((outer, cy + 1.05), 0.17, facecolor=P.fill("highlight"), edgecolor=P.edge("highlight"),
                                lw=0.7, zorder=7))
            bio.label(ax, (outer, cy + 1.05), "P", size="tiny", bold=True, color=P.on_fill(), zorder=8)
        if not phos:
            bio.arrow(ax, (outer + s * 1.6, cy - 0.55), (outer + s * 2.4, cy - 0.55), kind="process", color=P.edge("negative"))
    bio.label(ax, (cx, 0.55), "Ndc80 phosphorylated: weak binding, release" if phos else
              "outer kinetochore out of reach: stable binding", size="tiny", color=P.muted())
