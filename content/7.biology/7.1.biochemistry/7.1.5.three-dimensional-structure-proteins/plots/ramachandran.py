"""Hard-sphere Ramachandran maps computed from scratch.

A blocked residue (acetyl-X-N-methylamide; X = L-Ala or Gly) is built with standard bond lengths and
angles (trans peptide bonds, tau = N-CA-C = 111 deg), every (phi, psi) on a 2-degree grid is scanned,
and a conformation is "fully allowed" if no pair of atoms whose distance depends on phi or psi comes
closer than the normal contact limit of Ramachandran and Sasisekharan, "outer limit" if no pair is
closer than the outer limit. The C-beta methyl is treated as one sphere; C-H and N-H are 1.0 A.
Thin contours: residues per turn n of the regular helix generated when every residue has the same
(phi, psi); n > 0 right-handed, n < 0 left-handed, |n| = 2 is a flat (beta) ribbon.
"""

import itertools

import numpy as np
import wikibio as bio
from wikibio import charts

P = bio.P


def place(a, b, c, bond, angle, torsion):
    """NeRF: atom d bonded to c with bond length, angle b-c-d and torsion a-b-c-d (degrees)."""
    angle, torsion = np.radians(angle), np.radians(torsion)
    bc = c - b
    bc = bc / np.linalg.norm(bc, axis=-1, keepdims=True)
    n = np.cross(b - a, bc)
    n = n / np.linalg.norm(n, axis=-1, keepdims=True)
    m = np.cross(n, bc)
    x = -bond * np.cos(angle) * np.ones_like(torsion)
    y = bond * np.sin(angle) * np.cos(torsion)
    z = bond * np.sin(angle) * np.sin(torsion)
    return c + x[..., None] * bc + y[..., None] * m + z[..., None] * n


def start(shape):
    """First three atoms (C of residue i-1 side: CA0, C0, N1) in a fixed frame."""
    sh = shape + (3,)
    a = np.radians(116.2)
    return (np.broadcast_to(np.array([0.0, 1.4, 0.0]), sh), np.broadcast_to(np.zeros(3), sh),
            np.broadcast_to(np.array([1.329 * np.sin(a), 1.329 * np.cos(a), 0.0]), sh))


def build(phi, psi, gly=False):
    """Atoms of Ac-X-NHMe whose positions matter for the backbone contacts."""
    phi, psi = np.broadcast_arrays(np.asarray(phi, float), np.asarray(psi, float))
    one = np.ones(phi.shape)
    CA0, C0, N1 = start(phi.shape)
    CA1 = place(CA0, C0, N1, 1.458, 121.7, 180.0 * one)
    O0 = place(CA1, N1, C0, 1.231, 123.0, 0.0 * one)
    H1 = place(CA0, C0, N1, 1.0, 119.5, 0.0 * one)
    C1 = place(C0, N1, CA1, 1.525, 111.0, phi)
    N2 = place(N1, CA1, C1, 1.329, 116.2, psi)
    O1 = place(N1, CA1, C1, 1.231, 120.8, psi + 180.0)
    CA2 = place(CA1, C1, N2, 1.458, 121.7, 180.0 * one)
    H2 = place(CA1, C1, N2, 1.0, 119.5, 0.0 * one)
    CB = place(N1, C1, CA1, 1.0 if gly else 1.53, 109.5, 122.7 * one)   # L configuration
    HA = place(N1, C1, CA1, 1.0, 109.5, -118.0 * one)
    return {"CA0": ("C", CA0), "C0": ("C", C0), "O0": ("O", O0), "N1": ("N", N1), "H1": ("H", H1),
            "CA1": ("C", CA1), "HA": ("H", HA), "CB": ("H" if gly else "M", CB), "C1": ("C", C1),
            "O1": ("O", O1), "N2": ("N", N2), "H2": ("H", H2), "CA2": ("C", CA2)}


# normal and outer-limit contact distances (angstrom); M = CH3 group
LIMITS = {"CC": (3.0, 2.9), "CM": (3.2, 3.0), "MM": (3.2, 3.0), "CO": (2.8, 2.7), "MO": (2.8, 2.7),
          "CN": (2.9, 2.8), "MN": (2.9, 2.8), "CH": (2.4, 2.2), "MH": (2.4, 2.2), "OO": (2.7, 2.6),
          "NO": (2.7, 2.6), "HO": (2.4, 2.2), "NN": (2.7, 2.6), "HN": (2.4, 2.2), "HH": (2.0, 1.9)}


def limit(e1, e2):
    return LIMITS.get(e1 + e2) or LIMITS[e2 + e1]


def steric_map(gly, step=2.0):
    g = np.arange(-180.0, 180.0 + step / 2, step)
    PHI, PSI = np.meshgrid(g, g)
    atoms = build(PHI, PSI, gly)
    probes = [build(p, q, gly) for p, q in ((-60, -40), (100, 150), (-150, 60), (30, -120))]
    full = np.ones(PHI.shape, bool)
    outer = np.ones(PHI.shape, bool)
    for a, b in itertools.combinations(atoms, 2):
        ds = [np.linalg.norm(pr[a][1] - pr[b][1]) for pr in probes]
        if max(ds) - min(ds) < 1e-6:     # distance fixed by covalent geometry
            continue
        lo_n, lo_o = limit(atoms[a][0], atoms[b][0])
        d = np.linalg.norm(atoms[a][1] - atoms[b][1], axis=-1)
        full &= d >= lo_n
        outer &= d >= lo_o
    return g, full, outer


def helix_turns(phi, psi):
    """Signed residues per turn of the uniform chain with these (phi, psi) and trans peptides."""
    phi, psi = np.broadcast_arrays(np.asarray(phi, float), np.asarray(psi, float))
    one = np.ones(phi.shape)
    pts = list(start(phi.shape))
    geom = {"C": (1.525, 111.0, phi), "N": (1.329, 116.2, psi), "CA": (1.458, 121.7, 180.0 * one)}
    for name in ["CA", "C", "N", "CA", "C", "N", "CA", "C"]:
        b, a, t = geom[name]
        pts.append(place(pts[-3], pts[-2], pts[-1], b, a, t))

    def frame(k):
        N, CA, C = pts[2 + 3 * k], pts[3 + 3 * k], pts[4 + 3 * k]
        e1 = (C - CA) / np.linalg.norm(C - CA, axis=-1, keepdims=True)
        v = N - CA
        e2 = v - np.sum(v * e1, -1, keepdims=True) * e1
        e2 /= np.linalg.norm(e2, axis=-1, keepdims=True)
        return CA, np.stack([e1, e2, np.cross(e1, e2)], -1)

    o1, F1 = frame(0)
    o2, F2 = frame(1)
    R = F2 @ np.swapaxes(F1, -1, -2)
    theta = np.arccos(np.clip((np.trace(R, axis1=-2, axis2=-1) - 1) / 2, -1, 1))
    axis = np.stack([R[..., 2, 1] - R[..., 1, 2], R[..., 0, 2] - R[..., 2, 0], R[..., 1, 0] - R[..., 0, 1]], -1)
    axis /= np.linalg.norm(axis, axis=-1, keepdims=True) + 1e-12
    rise = np.sum((o2 - o1) * axis, -1)
    return 360.0 / np.maximum(np.degrees(theta), 1e-6) * np.sign(rise), rise


fig, ax = bio.canvas(19.0, 9.6)
pale = P.mix(P.fill("protein"), P.surface(), 0.55)
grid = np.arange(-180.0, 181.0, 3.0)
GP, GQ = np.meshgrid(grid, grid)
nturn, rise = helix_turns(GP, GQ)
marks = [("αR", -57, -47), ("3₁₀", -49, -26), ("β (anti)", -139, 135), ("β (par)", -119, 113),
         ("PPII", -75, 145), ("αL", 57, 47)]

for k, (gly, title) in enumerate(((False, "L-Alanine"), (True, "Glycine"))):
    g, full, outer = steric_map(gly)
    pax = charts.axes_at(ax, (1.6 + k * 9.4, 1.3, 7.3, 7.3))
    pax.contourf(g, g, outer.astype(float), levels=[0.5, 1.5], colors=[pale], zorder=1)
    pax.contourf(g, g, full.astype(float), levels=[0.5, 1.5], colors=[P.fill("protein")], zorder=2)
    masked = np.where((np.abs(nturn) < 2.05) | (np.abs(rise) < 0.4), np.nan, nturn)
    for lev, ls in ((-3.0, "--"), (3.0, "--"), (3.6, "-"), (-3.6, "-")):
        pax.contour(GP, GQ, masked, levels=[lev], colors=[P.muted()], linewidths=0.7, linestyles=ls, zorder=3)
    for name, p, q in marks:
        pax.plot(p, q, "o", ms=4.2, mfc=P.ink(), mec="none", zorder=5)
        dx = 8 if p < 0 else -8
        pax.annotate(name, (p, q), (p + dx * (1 if name not in ("αR", "3₁₀") else -1), q + 9),
                     fontsize=bio.core.FONT["tiny"], color=P.ink(), zorder=6,
                     bbox=dict(boxstyle="round,pad=0.12", fc=P.surface(), ec="none", alpha=0.8),
                     ha="left" if (dx > 0) == (name not in ("αR", "3₁₀")) else "right")
    pax.set_xlim(-180, 180)
    pax.set_ylim(-180, 180)
    pax.set_xticks(range(-180, 181, 90))
    pax.set_yticks(range(-180, 181, 90))
    pax.axhline(0, color=P.muted(), lw=0.5, zorder=0)
    pax.axvline(0, color=P.muted(), lw=0.5, zorder=0)
    charts.style_axes(pax, "φ / °", "ψ / °", box=True)
    charts.title(pax, f"{title}: {full.mean() * 100:.0f}% allowed, {outer.mean() * 100:.0f}% at outer limit")
    bio.panel(ax, "AB"[k], (0.1 + k * 9.4, 9.45))

# legend
ly = 0.35
for i, (col, text) in enumerate(((P.fill("protein"), "no contact below normal limit"),
                                 (pale, "allowed at the outer limit"))):
    x = 1.6 + i * 5.2
    ax.add_patch(bio.core.FancyBboxPatch((x, ly - 0.17), 0.5, 0.34, boxstyle="round,pad=0,rounding_size=0.05",
                                         facecolor=col, edgecolor=P.edge("protein"), lw=0.6))
    bio.label(ax, (x + 0.7, ly), text, size="tiny", ha="left")
ax.plot([11.6, 12.3], [ly, ly], color=P.muted(), lw=0.8)
ax.plot([14.9, 15.6], [ly, ly], color=P.muted(), lw=0.8, ls="--")
bio.label(ax, (12.45, ly), "n = ±3.6", size="tiny", ha="left")
bio.label(ax, (15.75, ly), "n = ±3 residues/turn", size="tiny", ha="left")
