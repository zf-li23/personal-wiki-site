"""The transferrin cycle and pH-dependent sorting.
(A) Diferric transferrin (two Fe3+) binds the transferrin receptor (TfR1 dimer) at pH 7.4 and enters in a
clathrin-coated pit; in the early endosome (pH about 6) iron is released, reduced to Fe2+ (STEAP3) and
carried into the cytosol (DMT1), while iron-free apotransferrin stays bound to the receptor; the complex
returns to the surface through the recycling endosome, and at pH 7.4 apotransferrin dissociates.
(B) Fraction bound as a function of pH for ligand-receptor pairs of the endocytic pathway (illustrative
Hill-type curves, f = 1/(1 + 10^(n(pH50 - pH))) or its mirror image, with midpoints in the published
ranges): Fe3+ on receptor-bound and on free transferrin, apotransferrin on TfR, LDL on the LDL receptor,
M6P hydrolases on M6P receptors, EGF on EGFR. Shaded: typical lumenal pH of each compartment."""

import numpy as np

import wikibio as bio
from wikibio import charts

P = bio.P
FT = bio.core.FONT
fig, ax = bio.canvas(24.0, 9.6, scale=0.42)
TH = 0.13


def band(pts, token="membrane", zorder=6):
    q, nrm, _ = bio.core.polyline(pts, n=400)
    o, i = q + nrm * TH / 2, q - nrm * TH / 2
    bio.shape(ax, np.vstack([o, i[::-1]]), token, lw=0, zorder=zorder)
    for ln in (o, i):
        ax.plot(ln[:, 0], ln[:, 1], color=P.edge(token), lw=0.8, zorder=zorder + 1)


def tfr(x, y, down=False, holo=False, apo=False, rot=0.0):
    """A TfR dimer standing on a membrane at (x, y); its ligand-binding heads point away from the cytosol."""
    s = -1 if down else 1
    for dx in (-0.12, 0.12):
        ax.plot([x + dx, x + dx], [y - s * 0.12, y + s * 0.45], color=P.edge("receptor"), lw=2.2, zorder=12,
                solid_capstyle="round")
        ax.add_patch(bio.core.Circle((x + dx * 1.6, y + s * 0.6), 0.17, facecolor=P.fill("receptor"),
                                     edgecolor=P.edge("receptor"), lw=0.8, zorder=13))
    if holo or apo:
        c = (x, y + s * 0.98)
        ax.add_patch(bio.core.Circle(c, 0.24, facecolor=P.fill("protein"), edgecolor=P.edge("protein"), lw=0.8, zorder=14))
        if holo:
            for dx in (-0.09, 0.09):
                ax.add_patch(bio.core.Circle((c[0] + dx, c[1]), 0.065, color=P.edge("drug"), lw=0, zorder=15))


def iron(c):
    ax.add_patch(bio.core.Circle(c, 0.07, color=P.edge("drug"), lw=0, zorder=15))


# ---- A: the cycle ------------------------------------------------------------------------------------------
bio.panel(ax, "A", (0.1, 9.5))
bio.shape(ax, [(0.3, 7.4), (10.3, 7.4), (10.3, 9.2), (0.3, 9.2)], "extracellular", lw=0, zorder=1)
band(np.array([[0.3, 7.4], [10.3, 7.4]]))
bio.label(ax, (3.0, 8.95), "Extracellular fluid, pH 7.4", size="tiny", ha="left", color=P.muted())
bio.label(ax, (0.5, 0.35), "Cytosol", size="tiny", ha="left", color=P.muted(), bold=True)
# 1: free diferric Tf and binding
ax.add_patch(bio.core.Circle((1.2, 8.75), 0.24, facecolor=P.fill("protein"), edgecolor=P.edge("protein"), lw=0.8, zorder=14))
for dx in (-0.09, 0.09):
    iron((1.2 + dx, 8.75))
tfr(2.2, 7.4, holo=True)
bio.arrow(ax, (1.5, 8.75), (1.95, 8.5), kind="process", head=0.14)
bio.label(ax, (2.2, 6.75), "1", size="small", bold=True)
# 2: coated vesicle
cv = (3.0, 5.3)
bio.vesicle(ax, cv, 0.62, token="vesicle")
for t in np.linspace(0, 2 * np.pi, 22, endpoint=False):
    ax.add_patch(bio.core.Circle((cv[0] + 0.72 * np.cos(t), cv[1] + 0.72 * np.sin(t)), 0.05, color=P.edge("positive"), lw=0, zorder=9))
ax.plot([cv[0], cv[0]], [cv[1] + 0.62, cv[1] + 0.25], color=P.edge("receptor"), lw=2.2, zorder=12)
ax.add_patch(bio.core.Circle(cv, 0.2, facecolor=P.fill("protein"), edgecolor=P.edge("protein"), lw=0.7, zorder=14))
for dx in (-0.07, 0.07):
    ax.add_patch(bio.core.Circle((cv[0] + dx, cv[1]), 0.055, color=P.edge("drug"), lw=0, zorder=15))
bio.arrow(ax, (2.45, 6.6), (2.8, 6.15), kind="process", head=0.15)
bio.label(ax, (2.0, 5.3), "2", size="small", bold=True)
bio.label(ax, (3.0, 4.35), "clathrin-coated\nvesicle", size="tiny", color=P.muted())
# 3: early endosome, iron release
ee = (6.0, 3.1)
bio.vesicle(ax, ee, 1.15, token="vesicle")
for ang in (200, 250, 310):
    a = np.radians(ang)
    x, y = ee[0] + 1.15 * np.cos(a), ee[1] + 1.15 * np.sin(a)
    ax.add_patch(bio.core.Circle((x, y), 0.1, facecolor=P.fill("channel"), edgecolor=P.edge("channel"), lw=0.6, zorder=13))
for ang in (40, 95, 150):  # receptor-bound apotransferrin on the lumenal face
    a = np.radians(ang)
    m = np.array(ee) + 1.15 * np.array([np.cos(a), np.sin(a)])
    t = np.array(ee) + 0.62 * np.array([np.cos(a), np.sin(a)])
    ax.plot(*np.c_[m, m + (t - m) * 0.55], color=P.edge("receptor"), lw=2.2, zorder=12, solid_capstyle="round")
    ax.add_patch(bio.core.Circle(t, 0.2, facecolor=P.fill("protein"), edgecolor=P.edge("protein"), lw=0.7, zorder=14))
for p in ((5.3, 2.35), (6.1, 2.15), (6.75, 2.45)):
    iron(p)
bio.arrow(ax, (3.6, 4.8), (5.0, 3.9), kind="process", head=0.15)
bio.label(ax, (6.0, 4.55), "3  pH ≈ 6: Fe³⁺ released", size="tiny", bold=False)
bio.arrow(ax, (5.9, 2.0), (5.6, 1.05), kind="process", head=0.14, color=P.edge("drug"))
bio.label(ax, (5.6, 0.75), "Fe²⁺ (STEAP3, DMT1) → cytosol", size="tiny", color=P.edge("drug"))
bio.label(ax, (7.05, 1.6), "apo-Tf stays\nbound to TfR", size="tiny", color=P.muted(), ha="left")
# 4: recycling endosome and return
re = (8.9, 4.7)
for k, dy in enumerate((-0.25, 0.1, 0.45)):
    band(np.array([[re[0] - 0.75, re[1] + dy], [re[0] + 0.75, re[1] + dy + 0.06 * (k - 1)]]), "vesicle", zorder=7)
bio.label(ax, (re[0], 3.95), "4  recycling\nendosome", size="tiny")
bio.arrow(ax, (7.05, 3.7), (8.2, 4.35), kind="process", head=0.15)
bio.arrow(ax, (9.0, 5.25), (8.4, 6.9), kind="process", head=0.15)
tfr(8.3, 7.4, apo=True)
ax.add_patch(bio.core.Circle((9.4, 8.7), 0.24, facecolor=P.fill("protein"), edgecolor=P.edge("protein"), lw=0.8, zorder=14))
bio.arrow(ax, (8.55, 8.45), (9.1, 8.65), kind="process", head=0.14)
bio.label(ax, (8.3, 6.75), "5", size="small", bold=True)
bio.label(ax, (9.4, 8.2), "apo-Tf\nreleased", size="tiny", color=P.muted())

# ---- B: binding versus pH ---------------------------------------------------------------------------------
bio.panel(ax, "B", (11.6, 9.5))
b = charts.axes_at(ax, (13.0, 1.4, 6.4, 7.4))
pH = np.linspace(4.2, 7.8, 300)


def falls(p50, n):  # bound at high pH, released when the pH falls below p50
    return 1 / (1 + 10 ** (n * (p50 - pH)))


def rises(p50, n):  # bound at low pH, released when the pH rises above p50
    return 1 / (1 + 10 ** (n * (pH - p50)))


for lo, hi, name, al in ((7.2, 7.6, "plasma", 0.4), (6.0, 6.5, "early", 0.4), (5.0, 6.0, "late", 0.18),
                         (4.5, 5.0, "lyso.", 0.4)):
    b.axvspan(lo, hi, color=P.fill("neutral"), alpha=al, lw=0)
    b.text((lo + hi) / 2, 1.07, name, ha="center", fontsize=FT["tiny"], color=P.muted())
curves = [("Fe³⁺ on TfR-bound Tf", falls(6.2, 2.5), "drug", "-"), ("Fe³⁺ on free Tf", falls(5.6, 2.5), "drug", ":"),
          ("apo-Tf on TfR", rises(7.0, 2.5), "protein", "-"), ("LDL on LDLR", falls(6.3, 3.0), "lipid", "-"),
          ("M6P hydrolase on M6PR", falls(5.8, 2.5), "lysosome", "--"), ("EGF on EGFR", falls(5.4, 2.5), "negative", "-.")]
for name, y, tok, ls in curves:
    b.plot(pH, y, color=charts.line(tok), lw=1.7, ls=ls, label=name)
b.set_xlim(4.2, 7.8)
b.set_ylim(0, 1.13)
b.set_yticks([0, 0.5, 1.0])
b.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="center left", bbox_to_anchor=(1.02, 0.5))
charts.style_axes(b, "lumenal pH", "fraction bound")
