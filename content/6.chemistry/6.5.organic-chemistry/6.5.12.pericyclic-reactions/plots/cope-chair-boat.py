"""Chair and boat transition states of the Cope rearrangement, drawn as projections of idealized
3D six-atom arrays (dashed: the sigma bond being broken, C3-C4, and the one being formed, C1-C6).
For meso-3,4-dimethyl-1,5-hexadiene the chair places one methyl pseudo-equatorial and the other
pseudo-axial, which leads to the (E,Z)-2,6-octadiene (99.7 % at 180 C, Doering and Roth); the boat
would give the (E,E)-isomer (0.3 %). The chair is lower in energy by roughly 25 kJ/mol."""

import numpy as np
import matplotlib.pyplot as plt

ELEV = np.radians(14)
# frame position k (angle 60k degrees) of each carbon C1..C6: the allyl units are C1-C2-C3 and C4-C5-C6
POS = {1: 5, 2: 0, 3: 1, 4: 2, 5: 3, 6: 4}


def project(p):
    x, y, z = p
    return np.array([x, z * np.cos(ELEV) + y * np.sin(ELEV)])


def frame(kind):
    t = np.radians(np.arange(6) * 60.0)
    if kind == "chair":
        z = 0.25 * np.array([1, -1, 1, -1, 1, -1])
    else:
        z = np.array([0.45, 0, 0, 0.45, 0, 0])
    return np.array([[1.25 * np.cos(a), 1.25 * np.sin(a), zz] for a, zz in zip(t, z)])


def subst(a, axial, up):
    """Endpoint of a substituent: axial along z, equatorial roughly outward."""
    if axial:
        return a + np.array([0, 0, 0.85 * up])
    r = np.array([a[0], a[1], 0.0])
    r = r / np.linalg.norm(r)
    return a + 0.85 * r + np.array([0, 0, -0.25 * up])


fig, axes = plt.subplots(1, 2, figsize=(8.4, 3.8))
ink = plt.rcParams["text.color"]
for ax, kind in zip(axes, ("chair", "boat")):
    F = frame(kind)
    A = {c: F[k] for c, k in POS.items()}
    for c in range(1, 7):
        d = c % 6 + 1
        dashed = (c, d) in ((3, 4), (6, 1))
        ax.plot(*zip(project(A[c]), project(A[d])), color=ink, lw=1.0 if dashed else 2.2, ls=(0, (3, 2.5)) if dashed else "-")
        p = project(A[c])
        out = np.array([A[c][0], A[c][1]]) / 1.25
        ax.text(p[0] + 0.42 * out[0], p[1] + 0.25 * out[1] + (0.12 if c in (2, 3, 4) else -0.12), f"C{c}", fontsize=8,
                color=ink, ha="center", va="center")
    for c, axial in ((3, False), (4, kind == "chair")):
        up = 1.0 if (kind == "chair" and A[c][2] > 0) or kind == "boat" else -1.0
        a, b = project(A[c]), project(subst(A[c], axial, up))
        ax.plot(*zip(a, b), color="C3", lw=2.2)
        ax.text(*(b + (b - a) / np.linalg.norm(b - a) * 0.28), "Me", color="C3", fontsize=9, ha="center", va="center")
    ax.set_title("chair TS (favoured): Me eq + Me ax" if kind == "chair" else "boat TS: Me eq + Me eq", fontsize=10, color=ink)
    ax.text(0, -1.55, "(E,Z)-2,6-octadiene, 99.7 %" if kind == "chair" else "(E,E)-2,6-octadiene, 0.3 %",
            ha="center", fontsize=9, color=ink)
    ax.set_xlim(-2.3, 2.3)
    ax.set_ylim(-1.8, 1.8)
    ax.set_aspect("equal")
    ax.axis("off")
fig.tight_layout()
