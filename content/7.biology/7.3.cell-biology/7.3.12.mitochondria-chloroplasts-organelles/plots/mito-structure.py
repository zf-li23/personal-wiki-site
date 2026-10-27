"""Architecture and dynamics of mitochondria (schematic, not to scale).
(A) Section through a mitochondrion: outer membrane; inner boundary membrane parallel to it; lamellar
cristae joined to the boundary membrane by narrow crista junctions held by MICOS; rows of ATP synthase dimers
at the curved crista rims and respiratory-chain complexes on the flat crista faces; the matrix with nucleoids
of mtDNA and mitoribosomes; TOM and TIM import complexes at a contact between the two membranes; and an ER
tubule at a membrane contact site (ERMES in yeast) that exchanges lipids and Ca2+.
(B) Fusion: outer membranes are tethered and fused by mitofusins (Mfn1/2), then inner membranes by OPA1.
(C) Fission: an ER tubule wraps the mitochondrion and, with actin, preconstricts it; Drp1, recruited by Mff
and MiD49/51, assembles into a ring and constricts it further until it divides."""

import numpy as np

import wikibio as bio

P = bio.P
FT = bio.core.FONT
fig, ax = bio.canvas(23.0, 11.5, scale=0.42)
TH = 0.09


def capsule(c, L, Wd, n=160):
    r = Wd / 2
    a = np.linspace(-np.pi / 2, np.pi / 2, n // 2)
    right = np.c_[c[0] + L / 2 - r + r * np.cos(a), c[1] + r * np.sin(a)]
    left = np.c_[c[0] - L / 2 + r - r * np.cos(a), c[1] - r * np.sin(a)]
    return np.vstack([right, left])


def outline(pts, token, lw=1.0, z=5, fill=None):
    bio.shape(ax, pts, fill or token, lw=0, zorder=z)
    q = np.vstack([pts, pts[:1]])
    ax.plot(q[:, 0], q[:, 1], color=P.edge(token), lw=lw, zorder=z + 1, solid_joinstyle="round")


def crista(x, y_base, depth, down=True, w=0.42, neck=0.14):
    """Lamellar crista seen in section: a neck at the boundary membrane, a body, a rounded rim."""
    s = -1 if down else 1
    ys = y_base + s * np.r_[0.0, 0.3, 0.42]
    tip = y_base + s * depth
    body = [(x - neck / 2, ys[0]), (x - neck / 2, ys[1]), (x - w / 2, ys[2])]
    a = np.linspace(np.pi, 2 * np.pi, 20) if down else np.linspace(np.pi, 0, 20)
    rim = [(x + w / 2 * np.cos(t), tip - s * w / 2 + (w / 2) * np.sin(t) * (1 if down else 1)) for t in a]
    body2 = [(x + w / 2, ys[2]), (x + neck / 2, ys[1]), (x + neck / 2, ys[0])]
    pts = np.array(body + [(x - w / 2, tip - s * w / 2)] + rim + [(x + w / 2, tip - s * w / 2)] + body2)
    outline(pts, "mitochondrion", lw=0.9, z=9)
    # MICOS at the junction
    for dx in (-neck / 2 - 0.05, neck / 2 + 0.05):
        ax.add_patch(bio.core.Circle((x + dx, ys[1] - s * 0.02), 0.055, color=P.edge("drug"), lw=0, zorder=12))
    # ATP synthase dimer at the rim (heads in the matrix)
    rim_y = tip
    for ang in (-35, 35):
        t = np.radians(ang)
        base = np.array([x + 0.12 * np.sin(t), rim_y])
        head = base + 0.32 * np.array([np.sin(t), s * np.cos(t)])
        ax.plot(*np.c_[base, head], color=P.edge("receptor"), lw=1.2, zorder=12)
        ax.add_patch(bio.core.Circle(head, 0.1, facecolor=P.fill("receptor"), edgecolor=P.edge("receptor"), lw=0.5, zorder=13))
    # respiratory complexes on the flat faces
    for yy in np.linspace(ys[2] + s * 0.25, tip - s * 0.55, 3):
        for side in (-1, 1):
            bio.box(ax, (x + side * (w / 2 + 0.05), yy), 0.16, 0.24, "enzyme", radius=0.04, lw=0.5, zorder=12)


# ---- A: section ---------------------------------------------------------------------------------------------
bio.panel(ax, "A", (0.1, 11.4))
C = (6.4, 5.3)
L, Wd = 11.2, 6.4
outline(capsule(C, L, Wd), "mitochondrion", lw=1.6, z=3)
inner = capsule(C, L - 0.55, Wd - 0.55)
outline(inner, "mitochondrion", lw=1.1, z=5, fill="matrix")
top, bot = C[1] + (Wd - 0.55) / 2, C[1] - (Wd - 0.55) / 2
xs = np.linspace(2.6, 10.2, 6)
for k, x in enumerate(xs):
    if k % 2 == 0:
        crista(x, top, 3.2, down=True)
    else:
        crista(x, bot, 3.2, down=False)
# nucleoids and ribosomes
for p in ((3.6, 4.5), (6.3, 6.7), (11.0, 4.1)):
    for k in range(3):
        a = np.linspace(0, 2 * np.pi, 40)
        ax.plot(p[0] + 0.22 * np.cos(a) + 0.07 * k, p[1] + 0.14 * np.sin(a) + 0.04 * k, color=P.edge("dna"), lw=0.9, zorder=11)
    ax.add_patch(bio.core.Circle(p, 0.08, color=P.edge("protein"), lw=0, zorder=12))
for p in ((4.9, 3.4), (5.15, 3.55), (7.6, 6.6), (7.85, 6.75), (2.3, 6.3)):
    bio.ribosome(ax, p, size=0.22)
# TOM/TIM at a contact site (lower left)
bio.box(ax, (1.66, 2.98), 0.32, 0.55, "channel", radius=0.05, zorder=14)
bio.box(ax, (1.92, 3.24), 0.3, 0.5, "positive", radius=0.05, zorder=14)
bio.arrow(ax, (0.8, 2.1), (2.3, 3.6), kind="process", head=0.14, color=P.edge("channel"))
# ER contact (upper right)
er = np.c_[np.linspace(8.0, 12.6, 50), 8.95 + 0.1 * np.sin(np.linspace(0, 4, 50))]
bio.shape(ax, np.vstack([er + (0, 0.22), (er - (0, 0.22))[::-1]]), "er", lw=0.8, zorder=4)
for x in (8.9, 9.5, 10.1):
    ax.plot([x, x], [8.45, 8.73], color=P.edge("drug"), lw=2.0, zorder=6)
# callouts
for (px, py), ty, txt in (((3.9, 8.5), 10.6, "Outer membrane"), ((6.6, 8.36), 10.6, "Intermembrane space"),
                          ((5.2, 8.22), 9.75, "Inner boundary membrane")):
    bio.label(ax, (px, ty), txt, size="tiny")
    bio.callout(ax, (px, py), (px, ty - 0.28), "", size="tiny")
co = [
      ((2.6 + 0.08, top - 0.32), (0.4, 9.4), "Crista junction (MICOS)"),
      ((9.5, 8.6), (12.4, 9.9), "ER contact: lipids, Ca²⁺ (ERMES)"),
      ((7.85, 6.75), (12.4, 7.9), "Mitoribosome"),
      ((11.3, 6.2), (12.4, 6.9), "Matrix"),
      ((10.25, 5.75), (12.4, 5.9), "ATP synthase dimers at the rim"),
      ((10.2, 4.7), (12.4, 4.9), "Crista lumen"),
      ((10.47, 3.55), (12.4, 3.9), "Respiratory complexes (crista face)"),
      ((11.0, 4.1), (12.4, 2.9), "mtDNA nucleoid"),
      ((1.8, 3.1), (0.4, 0.9), "TOM–TIM (protein import)")]
for pt, txt, s in co:
    bio.callout(ax, pt, txt, s, size="tiny")

# ---- B: fusion ---------------------------------------------------------------------------------------------
bio.panel(ax, "B", (16.6, 11.4))
bx = 16.9


def mito_tube(c, L, Wd=0.9, inner=True):
    outline(capsule(c, L, Wd), "mitochondrion", lw=1.1, z=7)
    if inner:
        outline(capsule(c, L - 0.24, Wd - 0.24), "mitochondrion", lw=0.7, z=8, fill="matrix")


y = 10.0
mito_tube((bx + 0.85, y), 1.7)
mito_tube((bx + 2.95, y), 1.7)
for dy in (-0.2, 0.2):
    ax.plot([bx + 1.7, bx + 2.1], [y + dy, y + dy], color=P.edge("negative"), lw=2.2, zorder=9)
bio.label(ax, (bx + 1.9, y + 0.7), "Mfn1/2 tether", size="tiny", color=P.edge("negative"))
y2 = 8.4
outline(capsule((bx + 1.9, y2), 3.8, 0.9), "mitochondrion", lw=1.1, z=7)
outline(capsule((bx + 0.9, y2), 1.55, 0.66), "mitochondrion", lw=0.7, z=8, fill="matrix")
outline(capsule((bx + 2.9, y2), 1.55, 0.66), "mitochondrion", lw=0.7, z=8, fill="matrix")
ax.plot([bx + 1.9, bx + 1.9], [y2 - 0.2, y2 + 0.2], color=P.edge("positive"), lw=2.2, zorder=10)
bio.label(ax, (bx + 1.9, y2 + 0.7), "outer fused; OPA1", size="tiny", color=P.edge("positive"))
y3 = 6.8
mito_tube((bx + 1.9, y3), 3.8)
bio.arrow(ax, (bx + 4.4, y), (bx + 4.4, y2 + 0.3), kind="process", head=0.14, bend=-0.3)
bio.arrow(ax, (bx + 4.4, y2 - 0.1), (bx + 4.4, y3 + 0.3), kind="process", head=0.14, bend=-0.3)
bio.label(ax, (bx + 1.9, y3 - 0.75), "Fusion", size="small", bold=True)

# ---- C: fission --------------------------------------------------------------------------------------------
bio.panel(ax, "C", (16.6, 5.4))
y4 = 4.2
waist = np.r_[np.linspace(-1.9, 1.9, 120)]
half = 0.45 * (1 - 0.6 * np.exp(-(waist / 0.25) ** 2))
up = np.c_[bx + 1.9 + waist, y4 + half]
low = np.c_[bx + 1.9 + waist[::-1], y4 - half[::-1]]
ends_r = np.c_[bx + 1.9 + 1.9 + 0.45 * np.cos(np.linspace(np.pi / 2, -np.pi / 2, 20)), y4 + 0.45 * np.sin(np.linspace(np.pi / 2, -np.pi / 2, 20))]
ends_l = np.c_[bx + 1.9 - 1.9 + 0.45 * np.cos(np.linspace(-np.pi / 2, -3 * np.pi / 2, 20)), y4 + 0.45 * np.sin(np.linspace(-np.pi / 2, -3 * np.pi / 2, 20))]
outline(np.vstack([up, ends_r, low, ends_l]), "mitochondrion", lw=1.1, z=7)
erx = bx + 1.9
bio.shape(ax, [(erx - 0.42, y4 - 1.3), (erx - 0.22, y4 - 1.3), (erx - 0.22, y4 + 1.3), (erx - 0.42, y4 + 1.3)], "er", lw=0.8, zorder=6)
for k in range(6):
    yy = y4 - 0.3 + 0.12 * k
    ax.add_patch(bio.core.Circle((erx + 0.05 + 0.03 * (k % 2), yy), 0.06, color=P.edge("positive"), lw=0, zorder=12))
bio.label(ax, (erx - 0.55, y4 + 1.05), "ER tubule", size="tiny", color=P.edge("er"), ha="right")
bio.label(ax, (erx, y4 - 1.05), "Drp1 ring (Mff, MiD49/51)", size="tiny", color=P.edge("positive"))
y5 = 1.9
mito_tube((bx + 0.8, y5), 1.7)
mito_tube((bx + 3.0, y5), 1.7)
bio.arrow(ax, (bx + 4.4, y4 - 0.2), (bx + 4.4, y5 + 0.3), kind="process", head=0.14, bend=-0.3)
bio.label(ax, (bx + 1.9, y5 - 0.85), "Fission", size="small", bold=True)
