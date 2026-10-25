# The nucleosome. A: the histone fold (three helices a1-a3 joined by loops L1, L2, with a disordered
# N-terminal tail) and the assembly path: two folds pair head-to-tail ("handshake") into H3-H4 and H2A-H2B
# dimers; two H3-H4 dimers form the (H3-H4)2 tetramer, which binds two H2A-H2B dimers to give the octamer.
# B: the core particle viewed down the superhelix axis: 147 bp wrapped in 1.65 left-handed turns around the
# octamer (about 11 nm across, 5.7 nm thick), entry and exit DNA close to the dyad, where the linker histone H1
# binds. C: a nucleosome array ("beads on a string") with the base-pair bookkeeping: core 147 bp, chromatosome
# about 167 bp, linker 20-80 bp, repeat length about 200 bp.
import numpy as np
import wikibio as bio
from wikibio import molbio as MB

P = bio.P
H = {"H2A": "antibody", "H2B": "receptor", "H3": "protein", "H4": "carbohydrate", "H1": "neutral"}
fig, ax = bio.canvas(20.0, 10.6)


def fold(x, y, tok, s=1.0, flip=False, tail=True):
    """A schematic histone fold: helices a1 (short), a2 (long), a3 (short) as rounded boxes."""
    sg = -1 if flip else 1
    segs = [(-1.35, 0.35, 0.55, 20), (0.0, 0.0, 1.9, -20), (1.35, 0.35, 0.55, 20)]
    for dx, dy, L, ang in segs:
        c = (x + sg * dx * s, y + dy * s * (1 if not flip else -1))
        w, h = L * s, 0.32 * s
        t = np.radians(ang * sg)
        R = np.array([[np.cos(t), -np.sin(t)], [np.sin(t), np.cos(t)]])
        corners = np.array([[-w / 2, -h / 2], [w / 2, -h / 2], [w / 2, h / 2], [-w / 2, h / 2]]) @ R.T + c
        bio.shape(ax, bio.core.smooth_closed(corners, 40), tok, lw=1.0, zorder=8)
    if tail:
        a = np.array([x - sg * 1.75 * s, y + 0.5 * s * (1 if not flip else -1)])
        pts = np.array([a + np.array([-sg * k * 0.35 * s, 0.12 * s * np.sin(k * 2.2)]) for k in range(6)])
        pts = MB.wavy(pts, amplitude=0.05, wavelength=0.3)
        ax.plot(pts[:, 0], pts[:, 1], color=P.edge(tok), lw=1.4, zorder=8)


# ---- A: histone fold and assembly ------------------------------------------------------------------------
bio.panel(ax, "A", (0.1, 10.5))
bio.label(ax, (0.6, 10.15), "Histone fold and octamer assembly", size="normal", bold=True, ha="left")
fold(2.6, 8.8, H["H3"], s=0.9)
bio.label(ax, (1.45, 9.55), "α1", size="tiny")
bio.label(ax, (2.6, 9.2), "α2", size="tiny")
bio.label(ax, (3.85, 9.55), "α3", size="tiny")
bio.label(ax, (0.55, 8.55), "N-terminal tail", size="tiny", ha="left", color=P.muted())
bio.label(ax, (2.6, 8.1), "L1, L2: loops between helices", size="tiny", color=P.muted())

# dimers (two folds crossing head-to-tail)
for k, (a, b, name) in enumerate([("H3", "H4", "H3–H4"), ("H2A", "H2B", "H2A–H2B")]):
    x0 = 1.9 + 3.2 * k
    fold(x0, 6.55, H[a], s=0.55, tail=False)
    fold(x0, 6.45, H[b], s=0.55, flip=True, tail=False)
    bio.label(ax, (x0, 5.55), name + " dimer", size="small")
bio.arrow(ax, (1.9, 5.25), (1.9, 4.55), kind="process")
bio.label(ax, (2.05, 4.9), "×2", size="tiny", ha="left")
# tetramer
for i, tok in enumerate([H["H3"], H["H4"], H["H3"], H["H4"]]):
    bio.box(ax, (1.25 + 0.43 * i, 3.95), 0.42, 0.7, tok, radius=0.12, zorder=8)
bio.label(ax, (1.9, 3.3), "(H3–H4)$_2$ tetramer", size="small")
bio.arrow(ax, (3.0, 3.95), (4.0, 3.95), kind="process")
bio.label(ax, (3.5, 4.35), "+ 2 H2A–H2B", size="tiny")
# octamer as a disc of eight sectors
c0, r0 = np.array([5.2, 3.95]), 0.9
order = ["H2A", "H2B", "H4", "H3", "H3", "H4", "H2B", "H2A"]
for i, nm in enumerate(order):
    th = np.linspace(np.pi / 2 - i * np.pi / 4, np.pi / 2 - (i + 1) * np.pi / 4, 20)
    v = np.vstack([c0, c0 + r0 * np.c_[np.cos(th), np.sin(th)]])
    bio.shape(ax, v, H[nm], lw=0.9, zorder=8)
bio.label(ax, (5.2, 2.75), "histone octamer", size="small")
# key
for i, nm in enumerate(["H2A", "H2B", "H3", "H4", "H1"]):
    xk = 0.7 + 1.15 * i
    bio.box(ax, (xk, 1.7), 0.32, 0.32, H[nm], radius=0.06)
    bio.label(ax, (xk + 0.24, 1.7), nm, size="tiny", ha="left")
bio.label(ax, (0.55, 1.05), "Tails ≈ 28% of core-histone mass;", size="tiny", ha="left", color=P.muted())
bio.label(ax, (0.55, 0.65), "Lys + Arg ≈ 1/4 of residues", size="tiny", ha="left", color=P.muted())

# ---- B: core particle, top view ---------------------------------------------------------------------------
bio.panel(ax, "B", (7.0, 10.5))
bio.label(ax, (7.5, 10.15), "Core particle (view down the superhelix axis)", size="normal", bold=True, ha="left")
cB = np.array([10.4, 5.9])
for i, nm in enumerate(order):
    th = np.linspace(np.pi / 2 - i * np.pi / 4, np.pi / 2 - (i + 1) * np.pi / 4, 30)
    v = np.vstack([cB, cB + 1.75 * np.c_[np.cos(th), np.sin(th)]])
    bio.shape(ax, v, H[nm], lw=0.9, zorder=6)
# DNA: 1.65 turns, a slight spiral so both gyres are visible; enters and leaves near the dyad (bottom)
turns = 1.65
phi = np.linspace(0, 2 * np.pi * turns, 600)
start = -np.pi / 2 - np.pi * turns  # symmetric about the dyad at the bottom
ang = start + phi
rad = 2.6 - 0.62 * phi / phi[-1]
pts = cB + np.c_[rad * np.cos(ang), rad * np.sin(ang)]
# linker DNA leaving tangentially
t0 = np.array([-np.sin(ang[0]), np.cos(ang[0])])
t1 = np.array([-np.sin(ang[-1]), np.cos(ang[-1])])
lin_in = np.array([pts[0] - t0 * s for s in np.linspace(2.4, 0, 20)])
lin_out = np.array([pts[-1] + t1 * s for s in np.linspace(0, 2.4, 20)])
MB.backbone(ax, np.vstack([lin_in, pts, lin_out]), "dna", lw=6.0, zorder=9)
bio.protein(ax, cB + np.array([0.0, -2.75]), 0.9, 0.55, H["H1"], text="H1", size="tiny")
ax.plot([cB[0], cB[0]], [cB[1] + 2.9, cB[1] - 3.4], color=P.muted(), lw=0.8, ls=(0, (4, 3)), zorder=12)
bio.label(ax, (cB[0] + 0.12, cB[1] + 3.15), "dyad axis", size="tiny", ha="left", color=P.muted())
bio.callout(ax, tuple(cB + np.array([2.5, 0.8])), (13.6, 8.9), "147 bp in 1.65")
bio.label(ax, (13.7, 8.5), "left-handed turns", size="small", ha="left")
bio.callout(ax, tuple(lin_out[-6]), (13.6, 2.6), "linker DNA")
bio.callout(ax, tuple(cB + np.array([0.6, 0.9])), (13.6, 7.6), "histone octamer")
bio.label(ax, (10.4, 1.55), "≈ 11 nm across, 5.7 nm thick; DNA contacts the octamer", size="tiny", color=P.muted())
bio.label(ax, (10.4, 1.15), "where its minor groove faces inward, about every 10 bp (14 sites)", size="tiny", color=P.muted())

# ---- C: nucleosome array ------------------------------------------------------------------------------------
bio.panel(ax, "C", (16.0, 10.5))
bio.label(ax, (16.5, 10.15), "Beads on a string", size="normal", bold=True, ha="left")
ys = [8.9, 6.4, 4.0]
for y in ys:
    ax.plot([16.4, 19.6], [y, y], color=P.edge("dna"), lw=3.0, solid_capstyle="round", zorder=5)
    for xb in (17.15, 18.85):
        bio.shape(ax, bio.core.smooth_closed(np.array([[xb - 0.5, y - 0.38], [xb + 0.5, y - 0.38], [xb + 0.5, y + 0.38],
                                                       [xb - 0.5, y + 0.38]]), 60), H["H3"], lw=1.0, zorder=7)
        ax.plot([xb - 0.5, xb + 0.5], [y + 0.22, y - 0.22], color=P.edge("dna"), lw=2.6, zorder=8)
        ax.plot([xb - 0.5, xb + 0.5], [y - 0.05, y - 0.45], color=P.edge("dna"), lw=2.6, zorder=8, alpha=0.6)
bio.label(ax, (18.0, 8.15), "core 147 bp + linker", size="tiny")
bio.label(ax, (18.0, 7.8), "repeat ≈ 160–240 bp", size="tiny")
bio.protein(ax, (17.15, 6.4 - 0.55), 0.45, 0.3, H["H1"], text=None)
bio.protein(ax, (18.85, 6.4 - 0.55), 0.45, 0.3, H["H1"], text=None)
bio.label(ax, (18.0, 5.25), "+ H1: chromatosome ≈ 167 bp", size="tiny")
bio.label(ax, (18.0, 3.25), "MNase cuts linkers first:", size="tiny")
bio.label(ax, (18.0, 2.9), "ladder of multiples of ~200 bp", size="tiny")
bio.label(ax, (18.0, 2.1), "Wrapping shortens DNA", size="tiny", color=P.muted())
bio.label(ax, (18.0, 1.75), "about 6- to 7-fold", size="tiny", color=P.muted())
ax.plot([18.0, 18.0], [4.3, 3.7], color=P.edge("negative"), lw=1.6, zorder=9)
bio.label(ax, (18.0, 4.55), "MNase", size="tiny", color=P.edge("negative"))
