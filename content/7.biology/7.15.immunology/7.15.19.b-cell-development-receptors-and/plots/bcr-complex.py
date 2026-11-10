# The B-cell receptor complex and the coreceptor. Membrane IgM binds antigen but has a three-residue
# cytoplasmic tail; the Igα/Igβ (CD79a/CD79b) heterodimer carries the ITAMs that signal. The coreceptor
# CD21-CD19-CD81 binds C3d on complement-tagged antigen, so one antigen engages both BCR and coreceptor;
# CD19 recruits PI3K. Below the membrane: the core signalling cascade (Lyn, Syk, BTK, BLNK, PLCγ2).
import wikibio as bio
from wikibio import immuno

P = bio.P
fig, ax = bio.canvas(18, 10.5)
ym = 4.6
bio.bilayer(ax, [(0.3, ym), (17.7, ym)])
bio.label(ax, (17.6, ym + 0.75), "Outside", size="tiny", ha="right", color=P.muted())
bio.label(ax, (17.6, ym - 0.75), "Cytoplasm", size="tiny", ha="right", color=P.muted())

# --- BCR: membrane IgM (drawn as the Ig unit) ------------------------------------------------------------
xb = 4.6
immuno.bcr(ax, xb, ym, up=1, size=1.6)
bio.label(ax, (xb - 1.3, ym + 2.4), "mIgM", size="small")
# Igα / Igβ heterodimer
for dxs, name, tok in ((-1.05, "Igα\n(CD79a)", "enzyme"), (1.05, "Igβ\n(CD79b)", "channel")):
    x = xb + dxs
    immuno.domain(ax, (x, ym + 0.75), 0.55, 0.62, tok)
    ax.plot([x, x], [ym + 0.42, ym - 1.6], color=P.edge(tok), lw=3.0, solid_capstyle="round", zorder=11)
    for yy in (ym - 0.9, ym - 1.35):
        ax.plot([x - 0.18, x + 0.18], [yy, yy], color=P.edge("negative"), lw=2.2, zorder=12)
    bio.label(ax, (x + dxs * 0.7, ym + 1.25), name, size="tiny", ha="left" if dxs > 0 else "right")
bio.label(ax, (xb, ym - 2.0), "ITAMs", size="tiny", color=P.edge("negative"))

# --- antigen with C3d, coreceptor ----------------------------------------------------------------------------
ag = (6.95, ym + 2.55)
bio.protein(ax, ag, 1.3, 0.75, "carbohydrate", text="antigen")
c3d = (8.05, ym + 3.0)
bio.protein(ax, c3d, 0.5, 0.4, "drug")
bio.label(ax, (8.05, ym + 3.45), "C3d", size="tiny", va="bottom")
xc = 8.9
# CD21: a chain of short consensus repeats
for k in range(7):
    immuno.domain(ax, (xc - 0.25 + 0.06 * k, ym + 0.35 + 0.38 * k), 0.32, 0.34, "receptor")
ax.plot([xc - 0.25, xc - 0.25], [ym + 0.15, ym - 0.35], color=P.edge("receptor"), lw=2.2, zorder=11)
bio.label(ax, (xc - 0.95, ym + 1.4), "CD21\n(CR2)", size="tiny", ha="right")
# CD19 with its long tail
x19 = xc + 0.75
immuno.domain(ax, (x19, ym + 0.55), 0.5, 0.5, "protein")
immuno.domain(ax, (x19, ym + 1.15), 0.5, 0.5, "protein")
ax.plot([x19, x19], [ym + 0.3, ym - 2.2], color=P.edge("protein"), lw=3.0, solid_capstyle="round", zorder=11)
bio.label(ax, (x19 + 0.4, ym + 1.6), "CD19", size="tiny", ha="left")
# CD81 tetraspanin
x81 = xc + 1.75
bio.protein(ax, (x81, ym + 0.42), 0.55, 0.42, "metabolite")
for dd in (-0.18, -0.06, 0.06, 0.18):
    ax.plot([x81 + dd, x81 + dd], [ym + 0.2, ym - 0.2], color=P.edge("metabolite"), lw=1.6, zorder=11)
bio.label(ax, (x81 + 0.45, ym + 0.75), "CD81", size="tiny", ha="left")
bio.arrow(ax, (ag[0] - 0.65, ag[1] - 0.2), (xb + 0.9, ym + 1.9), kind="link")

# --- signalling below the membrane ------------------------------------------------------------------------------
def node(xy, text, tok="protein", w=1.5):
    bio.box(ax, xy, w, 0.6, tok, text=text, size="tiny")


node((2.4, ym - 2.0), "Lyn (Src family)", "enzyme", 1.9)
node((4.6, ym - 2.9), "Syk", "enzyme")
node((6.7, ym - 2.9), "BLNK (adaptor)", "neutral", 1.9)
node((6.7, ym - 4.0), "BTK", "enzyme")
node((4.6, ym - 4.0), "PLCγ2", "enzyme")
node((x19, ym - 2.9), "PI3K", "enzyme")
node((x19, ym - 4.0), "PIP3 → Akt", "lipid", 1.8)
bio.arrow(ax, (2.6, ym - 1.65), (xb - 1.15, ym - 1.15), kind="process", head=0.14)
bio.arrow(ax, (xb, ym - 2.2), (xb, ym - 2.55), kind="process", head=0.14)
bio.arrow(ax, (5.4, ym - 2.9), (5.75, ym - 2.9), kind="activation", head=0.14)
bio.arrow(ax, (6.7, ym - 3.25), (6.7, ym - 3.65), kind="activation", head=0.14)
bio.arrow(ax, (5.9, ym - 4.0), (5.4, ym - 4.0), kind="activation", head=0.14)
bio.arrow(ax, (x19, ym - 2.25), (x19, ym - 2.55), kind="activation", head=0.14)
bio.arrow(ax, (x19, ym - 3.25), (x19, ym - 3.65), kind="process", head=0.14)
bio.arrow(ax, (x19 - 0.9, ym - 4.0), (7.6, ym - 4.0), kind="activation", head=0.14, dashed=True)
bio.label(ax, (4.6, ym - 4.6), "IP3 → Ca²⁺ (NFAT)\nDAG → PKC (NF-κB), Ras → ERK", size="tiny", va="top")
bio.label(ax, (14.2, ym - 2.6), "Outcome:\nproliferation, survival,\nantigen uptake for\npresentation to T cells", size="tiny",
          ha="left", va="top")
bio.label(ax, (14.2, ym + 2.6), "Coligation of BCR and\ncoreceptor lowers the\nantigen dose needed for\nactivation ~100-fold or more",
          size="tiny", ha="left", va="top")
