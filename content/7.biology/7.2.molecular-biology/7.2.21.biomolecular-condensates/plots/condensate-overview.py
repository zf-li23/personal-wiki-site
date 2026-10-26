# Biomolecular condensates: what they are (schematic, not to scale).
# A: three kinds of large assembly. A macromolecular machine has a fixed stoichiometry and geometry (nm);
#    a condensate is a micrometre-sized, membraneless body held together by many weak, constantly exchanging
#    contacts; a membrane-enclosed organelle is bounded by a lipid bilayer.
# B: multivalency. Two scaffolds with repeated binding modules (blue: five modules, e.g. SH3 domains; orange:
#    five ligands, e.g. proline-rich motifs) connected by flexible linkers form a network once each molecule can
#    bind several partners; clients (green) with one binding site partition into the network but do not
#    build it; molecules exchange with the surroundings (arrow).
# C: the nucleolus as three coexisting liquid phases (Feric and colleagues, 2016): fibrillar centre (FC, rDNA
#    and Pol I), dense fibrillar component (DFC, fibrillarin, early pre-rRNA processing) and granular component
#    (GC, nucleophosmin, assembly of preribosomal particles); nascent rRNA moves outward as it matures.
# D: material states. A liquid droplet (fusion, rapid internal mixing) can mature into a gel and then into
#    a solid with fibrillar (amyloid-like) cross-beta structure, a transition accelerated by disease mutations.
import numpy as np
from scipy.interpolate import make_interp_spline

import wikibio as bio

P = bio.P
fig, ax = bio.canvas(32.0, 9.2)


def chain(ax, pts, token, beads=5, r=0.13, linker="muted"):
    """A flexible multivalent molecule: a smooth linker with `beads` binding modules; returns bead centres."""
    pts = np.asarray(pts, float)
    u = np.linspace(0, 1, len(pts))
    path = make_interp_spline(u, pts, k=min(3, len(pts) - 1))(np.linspace(0, 1, 200))
    ax.plot(path[:, 0], path[:, 1], color=P.muted(), lw=0.9, zorder=8)
    idx = np.linspace(0, len(path) - 1, beads).astype(int)
    cs = path[idx]
    for c in cs:
        bio.molecule(ax, c, token, r=r, zorder=10)
    return cs


# --- A ---
bio.panel(ax, "A", (0.2, 8.9))
# machine
cx = 2.2
for (dx, dy, w, h, i) in ((0, 0.45, 1.3, 0.8, 0), (-0.55, -0.35, 0.9, 0.7, 1), (0.6, -0.4, 1.0, 0.75, 2)):
    bio.protein(ax, (cx + dx, 5.6 + dy), w, h, ("protein", "enzyme", "receptor")[i], wobble=0.05)
bio.label(ax, (cx, 3.85), "≈ 10 nm, fixed parts", size="tiny", color=P.muted())
bio.label(ax, (cx, 3.45), "and geometry", size="tiny", color=P.muted())
# condensate
cx2 = 5.6
bio.shape(ax, bio.blob((cx2, 5.6), 1.45, 1.3, wobble=0.05, seed=4), "nucleolus", zorder=4)
rng = np.random.default_rng(2)
gx, gy = np.meshgrid(np.linspace(-1.0, 1.0, 6), np.linspace(-0.9, 0.9, 5))
pts = np.c_[cx2 + gx.ravel() + rng.uniform(-0.12, 0.12, gx.size), 5.6 + gy.ravel() + rng.uniform(-0.12, 0.12, gx.size)]
pts = pts[((pts[:, 0] - cx2) / 1.15) ** 2 + ((pts[:, 1] - 5.6) / 1.0) ** 2 < 1]
for i in range(len(pts)):
    for j in range(i + 1, len(pts)):
        if np.hypot(*(pts[i] - pts[j])) < 0.5 and rng.random() < 0.6:
            ax.plot(*np.array([pts[i], pts[j]]).T, color=P.edge("nucleolus"), lw=0.6, ls=(0, (2, 1.5)), zorder=6)
for p in pts:
    bio.molecule(ax, p, "protein", r=0.09, zorder=8)
bio.label(ax, (cx2, 3.85), "≈ 0.1–10 µm, no membrane,", size="tiny", color=P.muted())
bio.label(ax, (cx2, 3.45), "weak exchanging contacts", size="tiny", color=P.muted())
bio.label(ax, (cx2, 7.25), "condensate", size="small", bold=True)
# organelle
cx3 = 9.2
bio.vesicle(ax, (cx3, 5.6), 1.25, token="vesicle")
for p in ((cx3 - 0.4, 5.8), (cx3 + 0.35, 5.4), (cx3, 6.0), (cx3 - 0.1, 5.2)):
    bio.molecule(ax, p, "enzyme", r=0.11)
bio.label(ax, (cx3, 7.25), "organelle", size="small", bold=True)
bio.label(ax, (cx3, 3.85), "bounded by a", size="tiny", color=P.muted())
bio.label(ax, (cx3, 3.45), "lipid bilayer", size="tiny", color=P.muted())
bio.label(ax, (cx, 7.25), "machine", size="small", bold=True)

# --- B ---
bio.panel(ax, "B", (11.4, 8.9))
bx, by = 14.6, 5.2
bio.shape(ax, bio.blob((bx, by), 2.7, 2.6, wobble=0.04, seed=7), "nucleolus", zorder=3, alpha=0.55)
blue, orange = [], []
starts = [((12.6, 6.6), (13.4, 7.0), (14.2, 6.5), (15.0, 6.9)), ((12.5, 4.7), (13.3, 5.2), (14.0, 4.6), (14.8, 5.0)),
          ((13.6, 3.3), (14.4, 3.7), (15.2, 3.2), (16.0, 3.6))]
for s in starts:
    blue.append(chain(ax, s, "dna"))
starts2 = [((13.0, 7.3), (13.4, 6.2), (13.2, 5.0), (13.6, 3.9)), ((14.9, 7.4), (15.4, 6.3), (15.0, 5.2), (15.6, 4.0)),
           ((16.4, 6.7), (16.0, 5.7), (16.6, 4.6), (16.3, 3.4))]
for s in starts2:
    orange.append(chain(ax, s, "rna"))
# a few bonds between nearby modules of different kind
allo = np.vstack(orange)
for bc in blue:
    for p in bc:
        d = np.hypot(*(allo - p).T)
        q = allo[np.argmin(d)]
        if d.min() < 0.8:
            ax.plot(*np.array([p, q]).T, color=P.ink(), lw=2.2, zorder=9, solid_capstyle="round")
for p in ((13.9, 5.9), (15.6, 5.6), (14.6, 4.2)):
    bio.molecule(ax, p, "positive", r=0.12, zorder=10)
bio.arrow(ax, (17.0, 7.3), (18.0, 7.9), kind="process", bend=0.1)
bio.arrow(ax, (18.0, 7.5), (17.2, 6.9), kind="process", bend=0.1)
bio.label(ax, (18.3, 8.25), "exchange", size="tiny", color=P.muted())
bio.label(ax, (14.6, 8.25), "multivalent network", size="small", bold=True)
bio.label(ax, (14.6, 1.95), "scaffolds: several binding modules each", size="tiny", color=P.muted())
bio.label(ax, (14.6, 1.55), "thick lines: bonds · client (green): one site, partitions in", size="tiny", color=P.muted())

# --- C ---
bio.panel(ax, "C", (19.4, 8.9))
ccx, ccy = 21.9, 5.2
bio.shape(ax, bio.blob((ccx, ccy), 2.1, 1.9, wobble=0.05, seed=11), "nucleolus", zorder=3)
for (dx, dy, s) in ((-0.7, 0.5, 21), (0.7, 0.3, 22), (0.0, -0.75, 23)):
    bio.shape(ax, bio.blob((ccx + dx, ccy + dy), 0.62, 0.55, wobble=0.08, seed=s), "rna", zorder=5)
    bio.shape(ax, bio.blob((ccx + dx, ccy + dy), 0.3, 0.27, wobble=0.08, seed=s + 5), "dna", zorder=6)
bio.callout(ax, (ccx + 0.0, ccy - 0.75), (ccx - 0.4, 2.55), "FC: rDNA, Pol I", size="tiny")
bio.callout(ax, (ccx + 1.2, ccy + 0.4), (ccx + 2.25, 2.55), "DFC: fibrillarin", size="tiny")
bio.callout(ax, (ccx - 1.6, ccy + 0.9), (ccx - 1.6, 7.75), "GC: nucleophosmin", size="tiny")
bio.arrow(ax, (ccx - 0.7, ccy + 0.5), (ccx - 1.55, ccy + 1.55), kind="process", lw=1.0, head=0.16)
bio.label(ax, (ccx + 0.3, 8.25), "nucleolus: three phases", size="small", bold=True)
bio.label(ax, (ccx + 1.5, 7.75), "pre-rRNA matures outward", size="tiny", color=P.muted())

# --- D ---
bio.panel(ax, "D", (25.2, 8.9))
xs = (26.4, 28.6, 30.8)
names = ("liquid", "gel", "solid (fibrils)")
for i, (x, nm) in enumerate(zip(xs, names)):
    bio.shape(ax, bio.blob((x, 5.4), 0.72, 0.72, wobble=0.04, seed=30 + i), "nucleolus" if i < 2 else "neutral", zorder=4)
    rr = np.random.default_rng(40 + i)
    if i == 0:
        for p in np.c_[x + rr.uniform(-0.45, 0.45, 8), 5.4 + rr.uniform(-0.45, 0.45, 8)]:
            bio.molecule(ax, p, "protein", r=0.07, zorder=6)
    elif i == 1:
        for _ in range(7):
            a = np.c_[x + rr.uniform(-0.5, 0.5, 2), 5.4 + rr.uniform(-0.5, 0.5, 2)]
            ax.plot(*a.T, color=P.edge("protein"), lw=0.9, zorder=6)
    else:
        for k in range(5):
            th = np.pi * k / 5
            d = 0.55 * np.array([np.cos(th), np.sin(th)])
            ax.plot([x - d[0], x + d[0]], [5.4 - d[1], 5.4 + d[1]], color=P.ink(), lw=1.6, zorder=6)
    bio.label(ax, (x, 4.3), nm, size="tiny")
    if i < 2:
        bio.arrow(ax, (x + 0.8, 5.4), (xs[i + 1] - 0.8, 5.4), kind="process", lw=1.0, head=0.15)
bio.label(ax, (28.6, 3.6), "aging; ALS mutations", size="tiny", color=P.muted())
bio.label(ax, (28.6, 3.2), "in FUS, TDP-43, hnRNPA1", size="tiny", color=P.muted())
bio.label(ax, (28.6, 7.25), "material state", size="small", bold=True)
