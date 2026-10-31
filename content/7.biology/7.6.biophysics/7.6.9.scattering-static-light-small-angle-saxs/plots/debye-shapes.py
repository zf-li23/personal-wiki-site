# Scattering curves of four bodies of uniform density computed with the Debye formula
#   I(q) / I(0) = (1 / N^2) sum_j sum_k sin(q r_jk) / (q r_jk),
# evaluated for the points of a cubic lattice (spacing 2.5 to 3 A, several thousand points) filling each
# body; the pair distances are binned in 0.25 A shells.
# Bodies: solid sphere R = 50 A; hollow sphere (shell from 40 to 50 A); rod (cylinder of radius 10 A
# and length 200 A); dumbbell (two spheres of radius 25 A with centres 70 A apart).
# The dashed curve is the exact form factor of the solid sphere, [3 (sin x - x cos x) / x^3]^2 with
# x = qR: the Debye sum reproduces it, including the first minimum at qR = 4.493.
# Dotted guides: pi / (qL), the intermediate region of a long rod, and 9 / [2 (qR)^4], the Porod envelope
# of the sphere (both derived in the text).
import matplotlib.pyplot as plt
import numpy as np
from scipy.spatial.distance import cdist

import wikibio as bio
from wikibio import charts

P = bio.P


def lattice(a, inside, half):
    """Points of a cubic lattice with spacing a inside a body (inside: mask function of x, y, z)."""
    g = np.arange(-half, half + a / 2, a)
    x, y, z = np.meshgrid(g, g, g, indexing="ij")
    m = inside(x, y, z)
    return np.column_stack([x[m], y[m], z[m]])


def pair_hist(pts, bins):
    """Histogram of all distances r_jk (j < k), computed in blocks to keep memory small."""
    h = np.zeros(len(bins) - 1)
    for i in range(0, len(pts), 600):
        d = cdist(pts[i:i + 600], pts[i:])
        h += np.histogram(d[np.triu_indices(d.shape[0], k=1, m=d.shape[1])], bins=bins)[0]
    return h


def R2(x, y, z):
    return x**2 + y**2 + z**2


bodies = (
    ("solid sphere", lattice(3.0, lambda x, y, z: R2(x, y, z) <= 50.0**2, 51), "protein"),
    ("hollow sphere", lattice(3.0, lambda x, y, z: (R2(x, y, z) <= 50.0**2) & (R2(x, y, z) >= 40.0**2), 52),
     "rna"),
    ("rod", lattice(2.5, lambda x, y, z: (x**2 + y**2 <= 10.0**2) & (np.abs(z) <= 100.0), 102), "dna"),
    ("dumbbell", lattice(3.0, lambda x, y, z: (x**2 + y**2 + (z - 35) ** 2 <= 25.0**2)
                         | (x**2 + y**2 + (z + 35) ** 2 <= 25.0**2), 62), "negative"),
)

q = np.logspace(np.log10(0.004), np.log10(0.25), 400)
bins = np.arange(0, 260, 0.25)
rc = 0.5 * (bins[1:] + bins[:-1])
fig, ax = plt.subplots(figsize=(7.2, 4.6))
for name, pts, tok in bodies:
    n = len(pts)
    h = pair_hist(pts, bins)
    I = (n + 2 * (h * np.sinc(np.outer(q, rc) / np.pi)).sum(axis=1)) / n**2
    ax.loglog(q, I, color=charts.line(tok), lw=1.7, label=name)
x = q * 50.0
F = 3 * (np.sin(x) - x * np.cos(x)) / x**3
ax.loglog(q, F**2, color=P.ink(), lw=0.9, ls=(0, (3, 2)), label="sphere, exact")
qa = np.array([0.02, 0.15])
ax.loglog(qa, np.pi / (qa * 200.0), color=P.muted(), lw=1.0, ls=(0, (1, 1.5)))
ax.text(0.03, 0.055, "π/(qL)", color=P.muted(), fontsize=8)
qb = np.array([0.1, 0.25])
ax.loglog(qb, 4.5 / (qb * 50.0) ** 4, color=P.muted(), lw=1.0, ls=(0, (1, 1.5)))
ax.text(0.103, 2.2e-5, "9/[2(qR)⁴]", color=P.muted(), fontsize=8)
ax.axvline(4.493 / 50, color=P.muted(), lw=0.6, ls=":")
ax.text(4.493 / 50 * 0.96, 2e-5, "qR = 4.493", color=P.muted(), fontsize=7, rotation=90, va="bottom", ha="right")
ax.set_xlim(0.004, 0.25)
ax.set_ylim(1e-5, 1.6)
ax.legend(fontsize=7.5, frameon=False, loc="lower left")
charts.style_axes(ax, "q / Å⁻¹", "I(q) / I(0)")
