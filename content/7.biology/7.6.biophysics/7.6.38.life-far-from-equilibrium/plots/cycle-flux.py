# Equilibrium versus nonequilibrium steady state in a three-state cycle A -> B -> C -> A.
# A: two cycles with the same forward rates; on the left the backward rates obey the Kolmogorov
# condition (cycle affinity 0), on the right the cycle is driven (affinity 6 kBT); arrow widths
# are proportional to the net probability flux on each edge, node areas to the stationary probability.
# B: a driven two-dimensional state space (an overdamped particle with a rotational force,
# dx = (-k x + w y) dt + noise, dy = (-k y - w x) dt + noise): stationary density (shading) and the
# circulating probability current (streamlines), the signature of broken detailed balance.
# C: steady-state cycle flux J against the cycle affinity A for the three-state cycle (exact
# formula, Formula 38.1.2), with the linear-response tangent near equilibrium.
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import LinearSegmentedColormap
from matplotlib.patches import Circle

import wikibio as bio
from wikibio import charts

P = bio.P


def steady(kf, kb):
    """Stationary probabilities and net flux of the 3-cycle; kf[i]: i -> i+1, kb[i]: i+1 -> i."""
    W = np.zeros((3, 3))
    for i in range(3):
        j = (i + 1) % 3
        W[j, i] += kf[i]
        W[i, j] += kb[i]
    L = W - np.diag(W.sum(0))
    A = np.vstack([L, np.ones(3)])
    p = np.linalg.lstsq(A, np.r_[0, 0, 0, 1.0], rcond=None)[0]
    J = p[0] * kf[0] - p[1] * kb[0]
    return p, J


kf = np.array([3.0, 1.0, 2.0])
kb_eq = np.array([1.0, 2.0, 3.0])
kb_eq[2] = kf.prod() / (kb_eq[0] * kb_eq[1])  # Kolmogorov: product of forward = product of backward

fig = plt.figure(figsize=(13.5, 4.3))
axA = fig.add_axes([0.02, 0.08, 0.36, 0.8])
axB = fig.add_axes([0.43, 0.15, 0.24, 0.7])
axC = fig.add_axes([0.74, 0.15, 0.24, 0.7])

axA.set_xlim(0, 10.4); axA.set_ylim(0, 5.0); axA.set_aspect("equal"); axA.axis("off")
names = ["A", "B", "C"]
for k, (title, kb, x0) in enumerate((("Equilibrium: A = 0", kb_eq, 2.4), ("Driven cycle: A = 6 kBT", kb_eq * np.exp(-2.0), 7.9))):
    p, J = steady(kf, kb)
    pos = [np.array([x0, 3.8]), np.array([x0 + 1.75, 0.9]), np.array([x0 - 1.75, 0.9])]
    for i in range(3):
        j = (i + 1) % 3
        net = p[i] * kf[i] - p[j] * kb[i]
        a, b = pos[i], pos[j]
        if abs(net) < 1e-9:
            bio.arrow(axA, a, b, kind="process", bend=0.12, color=P.muted(), lw=1.0, shrink=0.62, head=0.2)
            bio.arrow(axA, b, a, kind="process", bend=0.12, color=P.muted(), lw=1.0, shrink=0.62, head=0.2)
        else:
            bio.arrow(axA, a, b, kind="process", bend=0.12, color=charts.line("negative"), lw=1.0 + 9 * net,
                      shrink=0.62, head=0.32)
    for i in range(3):
        r = 0.2 + 0.5 * np.sqrt(p[i])
        axA.add_patch(Circle(pos[i], r, facecolor=P.fill("protein"), edgecolor=P.edge("protein"), lw=1.2, zorder=20))
        axA.text(*pos[i], names[i], ha="center", va="center", fontsize=10, color=P.on_fill(), zorder=21, weight="bold")
    axA.text(x0, 4.85, title.replace("kBT", "$k_{\\mathrm{B}}T$").replace("A =", "$\\mathcal{A}$ ="), ha="center",
             fontsize=9, color=P.ink(), weight="bold")
    axA.text(x0, 2.15, "no net flux" if abs(J) < 1e-9 else f"J = {J:.2f}", ha="center", va="center", fontsize=8,
             color=P.ink())
axA.text(0.0, 4.85, "A", fontsize=10, weight="bold", color=P.ink())

# B: rotational force field in 2D
k, w, D = 1.0, 1.2, 1.0
g = np.linspace(-2.6, 2.6, 121)
X, Y = np.meshgrid(g, g)
rho = np.exp(-k * (X**2 + Y**2) / (2 * D))
rho /= rho.sum()
jx, jy = w * Y * rho, -w * X * rho  # J = F rho - D grad rho; the gradient part cancels the radial force
cmap = LinearSegmentedColormap.from_list("dens", [P.surface(), P.fill("dna")])
axB.contourf(X, Y, rho, levels=12, cmap=cmap)
axB.streamplot(X, Y, jx, jy, color=charts.line("negative"), density=0.8, linewidth=1.0, arrowsize=0.9)
axB.set_aspect("equal")
charts.style_axes(axB, "mode 1 amplitude", "mode 2 amplitude")
charts.title(axB, "B   Circulating probability current")

# C: flux-force relation
As = np.linspace(-8, 12, 300)
Js = []
for A_ in As:
    kb = kb_eq * np.exp(-A_ / 3)
    Js.append(steady(kf, kb)[1])
Js = np.array(Js)
h = 1e-4
L0 = (steady(kf, kb_eq * np.exp(-h / 3))[1] - steady(kf, kb_eq * np.exp(h / 3))[1]) / (2 * h)
axC.plot(As, Js, color=charts.line("negative"), lw=2.0, label="exact")
axC.plot(As, L0 * As, color=P.muted(), lw=1.0, ls="--", label="linear response $J = L\\mathcal{A}$")
axC.axhline(0, color=P.muted(), lw=0.6)
axC.axvline(0, color=P.muted(), lw=0.6)
axC.set_ylim(-1.0, 1.6)
axC.legend(fontsize=7.5, frameon=False, loc="upper left")
charts.style_axes(axC, "cycle affinity $\\mathcal{A}/k_{\\mathrm{B}}T$", "cycle flux $J$")
charts.title(axC, "C   Flux saturates far from equilibrium")
