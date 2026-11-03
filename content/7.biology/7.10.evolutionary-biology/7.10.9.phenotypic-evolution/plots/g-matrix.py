"""The multivariate breeder's equation dz = G beta. A: the additive genetic covariance matrix G of two
traits (variances 1, genetic correlation 0.8) is drawn as its 1-SD ellipse; its leading eigenvector g_max
is the genetic line of least resistance. A selection gradient beta (arrow, pointing along +z1 and -z2)
produces the response G beta = (0.52, 0.20), which is deflected towards g_max: trait 2 increases although
selection favours a smaller value of it, a correlated response to the stronger selection on trait 1. B: approach to an optimum (star) under Gaussian stabilizing
selection, beta = V_s^{-1} (theta - z) with V_s = 20 I, from the origin. Dots mark every 10th generation.
With uncorrelated traits (grey, G = I) the path is straight; with the correlated G (colour) the population
first moves along g_max and approaches the optimum slowly along the direction of little genetic
variation, but it reaches it eventually because G has no zero eigenvalue."""
import numpy as np
import matplotlib.pyplot as plt

import wikibio as bio
from wikibio import charts

P = bio.P
FT = bio.core.FONT
G = np.array([[1.0, 0.8], [0.8, 1.0]])
vals, vecs = np.linalg.eigh(G)

fig, axs = plt.subplots(1, 2, figsize=(10.0, 4.5))
fig.subplots_adjust(left=0.07, right=0.98, bottom=0.12, top=0.9, wspace=0.25)
a = axs[0]
t = np.linspace(0, 2 * np.pi, 300)
circ = np.c_[np.cos(t), np.sin(t)]
ell = circ @ (vecs * np.sqrt(vals)).T
a.fill(ell[:, 0], ell[:, 1], color=P.fill("dna"), alpha=0.35, lw=0)
a.plot(ell[:, 0], ell[:, 1], color=charts.line("dna"), lw=1.2)
gmax = vecs[:, 1] * np.sqrt(vals[1])
a.plot([-1.8 * gmax[0], 1.8 * gmax[0]], [-1.8 * gmax[1], 1.8 * gmax[1]], color=charts.line("dna"), lw=1, ls="--")
a.text(1.75 * gmax[0], 1.75 * gmax[1] + 0.12, "$g_{\\max}$", color=charts.line("dna"), fontsize=FT["small"])
beta = np.array([1.0, -0.6])
resp = G @ beta
a.annotate("", xy=beta, xytext=(0, 0), arrowprops=dict(arrowstyle="-|>", color=charts.line("negative"), lw=1.8))
a.text(beta[0] + 0.05, beta[1] - 0.15, "$\\boldsymbol{\\beta}$", color=charts.line("negative"), fontsize=FT["normal"])
a.annotate("", xy=resp, xytext=(0, 0), arrowprops=dict(arrowstyle="-|>", color=charts.line("plant"), lw=1.8))
a.text(resp[0] + 0.05, resp[1] + 0.08, "$\\Delta\\bar{\\boldsymbol{z}} = G\\boldsymbol{\\beta}$",
       color=charts.line("plant"), fontsize=FT["small"])
a.set_aspect("equal")
a.set_xlim(-2, 2)
a.set_ylim(-2, 2)
a.axhline(0, color=P.muted(), lw=0.5)
a.axvline(0, color=P.muted(), lw=0.5)
charts.style_axes(a, "trait $z_1$", "trait $z_2$")
charts.title(a, "A  Response deflected by genetic correlation")

b = axs[1]
theta = np.array([3.0, -2.0])
Vs = 20.0
for GG, tok, lab in ((np.eye(2), "neutral", "$G = I$"), (G, "plant", "$r_A = 0.8$")):
    z = np.zeros(2)
    path = [z.copy()]
    for _ in range(300):
        z = z + GG @ (theta - z) / Vs
        path.append(z.copy())
    path = np.array(path)
    col = P.muted() if tok == "neutral" else charts.line(tok)
    b.plot(path[:, 0], path[:, 1], color=col, lw=1.6, label=lab)
    b.scatter(path[::10, 0], path[::10, 1], s=9, color=col, zorder=3)
b.scatter([theta[0]], [theta[1]], marker="*", s=160, color=charts.line("highlight"), zorder=4)
b.text(theta[0] + 0.12, theta[1] + 0.12, "optimum", fontsize=FT["tiny"], color=P.ink())
b.set_aspect("equal")
b.set_xlim(-0.5, 3.8)
b.set_ylim(-2.6, 1.2)
b.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="upper right")
charts.style_axes(b, "mean $\\bar z_1$", "mean $\\bar z_2$")
charts.title(b, "B  Path to an optimum")
