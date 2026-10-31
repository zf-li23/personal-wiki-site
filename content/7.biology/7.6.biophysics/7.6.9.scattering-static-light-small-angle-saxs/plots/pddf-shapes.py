# Pair-distance distribution functions p(r) of the four bodies of the Debye-formula figure, from the
# histogram (1 A bins) of the distances between N = 3000 points placed at random in each body,
# normalized to unit area. For each body the radius of gyration is computed from p(r) as
#   Rg^2 = int r^2 p(r) dr / (2 int p(r) dr)
# and printed in the legend; p(r) vanishes beyond the maximum dimension Dmax.
# Dashed: the exact p(r) of a solid sphere of radius R = 50 A, proportional to
# r^2 (1 - 3r/(4R) + r^3/(16 R^3)) for 0 <= r <= 2R.
# Bodies: solid sphere R = 50 A (Dmax = 100 A); hollow sphere, shell 40-50 A (Dmax = 100 A); rod, radius
# 10 A and length 200 A (Dmax = 201 A); dumbbell, two spheres of radius 25 A with centres 70 A apart
# (Dmax = 120 A, second peak near the centre-to-centre distance).
import matplotlib.pyplot as plt
import numpy as np
from scipy.spatial.distance import pdist

import wikibio as bio
from wikibio import charts

P = bio.P


rng = np.random.default_rng(1)
N = 3000


def ball(n, R, z0=0.0):
    v = rng.normal(size=(n, 3))
    v /= np.linalg.norm(v, axis=1)[:, None]
    v *= R * rng.random(n)[:, None] ** (1 / 3)
    v[:, 2] += z0
    return v


def shell(n, r1, r2):
    v = rng.normal(size=(n, 3))
    v /= np.linalg.norm(v, axis=1)[:, None]
    return v * ((r1**3 + (r2**3 - r1**3) * rng.random(n)) ** (1 / 3))[:, None]


def rod(n, R, L):
    phi = 2 * np.pi * rng.random(n)
    rr = R * np.sqrt(rng.random(n))
    return np.column_stack([rr * np.cos(phi), rr * np.sin(phi), L * (rng.random(n) - 0.5)])


def pair_hist(pts, bins):
    return np.histogram(pdist(pts), bins=bins)[0].astype(float)


bodies = (
    ("solid sphere", ball(N, 50.0), "protein"),
    ("hollow sphere", shell(N, 40.0, 50.0), "rna"),
    ("rod", rod(N, 10.0, 200.0), "dna"),
    ("dumbbell", np.vstack([ball(N // 2, 25.0, -35.0), ball(N // 2, 25.0, 35.0)]), "negative"),
)

bins = np.arange(0, 210, 1.0)
rc = 0.5 * (bins[1:] + bins[:-1])
fig, ax = plt.subplots(figsize=(7.2, 4.2))
for name, pts, tok in bodies:
    h = pair_hist(pts, bins)
    p = h / (h.sum() * 1.0)
    rg = np.sqrt((rc**2 * p).sum() / 2)
    ax.plot(rc, p * 100, color=charts.line(tok), lw=1.8, label=f"{name}  (Rg = {rg:.1f} Å)")
R = 50.0
r = np.linspace(0, 2 * R, 300)
pe = r**2 * (1 - 3 * r / (4 * R) + r**3 / (16 * R**3))
pe /= np.trapezoid(pe, r)
ax.plot(r, pe * 100, color=P.ink(), lw=0.9, ls=(0, (3, 2)), label="sphere, exact (Rg = 38.7 Å)")
ax.annotate("second peak:\ninter-lobe distances", xy=(73, 1.2), xytext=(108, 1.15), fontsize=7.5,
            color=P.muted(), arrowprops=dict(arrowstyle="-", color=P.muted(), lw=0.7))
ax.set_xlim(0, 210)
ax.set_ylim(0, None)
ax.legend(fontsize=7.5, frameon=False, loc="upper right")
charts.style_axes(ax, "r / Å", "p(r)  (% per Å)")
