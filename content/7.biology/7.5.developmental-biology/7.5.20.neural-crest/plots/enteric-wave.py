"""Colonization of the growing gut by enteric neural crest cells as a reaction-diffusion invasion (Formula 20.9.1,
after Landman, Simpson, Newgreen and colleagues). Cells enter at the oral end (x = 0), diffuse (D = 0.004 mm^2/h)
and proliferate logistically, while the gut grows uniformly from 1 mm at 0.025 mm/h, which also stretches the
colonized region and dilutes the cells. (A) Position of the invasion front (density half the carrying capacity)
and gut length over time, for three proliferation rates (front speeds 2 sqrt(rD) of 0.040, 0.025 and 0.020 mm/h):
with the highest rate the front catches up with the end of the gut, with lower rates it falls behind and the
distal gut stays uncolonized (aganglionic, as in Hirschsprung disease) for longer or permanently. (B) Density
profiles at 120 h; the dotted line marks the end of the gut."""
import numpy as np
import matplotlib.pyplot as plt
from scipy.linalg import solve_banded
import wikibio as bio
from wikibio import charts

P_ = bio.P
FT = bio.core.FONT
D, L0, g, T, M = 0.004, 1.0, 0.025, 140.0, 400


def run(r, dt=0.05):
    xi = np.linspace(0, 1, M)
    dx = xi[1]
    n = np.zeros(M)
    n[0] = 1.0
    t, ts, front, prof = 0.0, [], [], None
    while t < T:
        L = L0 + g * t
        # uniform growth in the Lagrangian coordinate xi = x / L: diffusion rescaled by 1/L^2, dilution by L'/L.
        # Reaction explicit, diffusion implicit (backward Euler, tridiagonal), Dirichlet n = 1 at xi = 0, no flux at 1.
        # a density cutoff: below about one cell per segment there is nobody to divide (otherwise the tail of the
        # continuum solution grows ahead of the real front)
        rhs = n + dt * (r * n * (1 - n) * (n > 1e-3) - g / L * n)
        k = D / L ** 2 * dt / dx ** 2
        ab = np.zeros((3, M))
        ab[0, 1:] = -k
        ab[1, :] = 1 + 2 * k
        ab[2, :-1] = -k
        ab[1, 0], ab[0, 1] = 1.0, 0.0
        rhs[0] = 1.0
        ab[2, -2] = -2 * k
        n = solve_banded((1, 1), ab, rhs)
        t += dt
        ts.append(t)
        front.append((xi[n > 0.5].max() if (n > 0.5).any() else 0.0) * L)
        if prof is None and t >= 120:
            prof = (xi * L, n.copy(), L)
    return np.array(ts), np.array(front), prof


fig, (a, b) = plt.subplots(1, 2, figsize=(10.0, 3.8))
fig.subplots_adjust(left=0.07, right=0.98, bottom=0.16, top=0.88, wspace=0.28)
tt = np.linspace(0, T, 200)
a.plot(tt, L0 + g * tt, color=P_.muted(), lw=1.4, ls="--", label="gut length")
for r, tok in ((0.1, "cl"), (0.04, "antibody"), (0.025, "negative")):
    ts, fr, (x, n, L) = run(r)
    a.plot(ts, fr, color=charts.line(tok), lw=1.7, label=f"front, r = {r} per h")
    b.plot(x, n, color=charts.line(tok), lw=1.7, label=f"r = {r} per h")
    b.axvline(L, color=P_.muted(), lw=0.7, ls=":")
a.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P_.ink(), loc="upper left")
charts.style_axes(a, "time / h", "position along the gut / mm")
charts.title(a, "A  Front versus gut growth")
b.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P_.ink(), loc="upper right")
charts.style_axes(b, "position along the gut / mm", "cell density (relative)")
charts.title(b, "B  Profiles at 120 h")
