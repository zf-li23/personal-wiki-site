# Bell-shaped dose-response of IgE-FcεRI cross-linking by a bivalent antigen (Goldstein-Perelson type model, illustrative).
# Receptors (total R_T per cell, all carrying IgE with the relevant specificity) bind a bivalent antigen at concentration L:
#   single-site binding   C1 = 2 L R / K_D                    (K_D: dissociation constant of one site, L in units of K_D)
#   cross-linking         C2 = (eps / R_T) C1 R               (eps = K_x R_T, dimensionless 2D cross-linking strength)
#   conservation          R_T = R + C1 + 2 C2
# With L measured in K_D and R in R_T: 1 = R (1 + 2L) + 4 eps L R^2 (quadratic in R).
# A: fraction of receptors in cross-linked pairs, 2 C2 / R_T, for three cross-linking strengths eps;
# B: degranulation modelled as a steep (Hill, n = 2) function of the cross-link density; a monovalent hapten (no cross-links)
#    gives no response at any concentration, and the response falls at high antigen although receptors stay occupied.
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio
from wikibio import charts

P = bio.P
L = np.logspace(-3, 3, 400)


def crosslinked(eps, L):
    a = 4 * eps * L
    b = 1 + 2 * L
    R = (-b + np.sqrt(b * b + 4 * a)) / (2 * a)
    c1 = 2 * L * R
    c2 = eps * c1 * R
    return 2 * c2, c1


fig, axs = plt.subplots(1, 2, figsize=(9.5, 3.6))
for eps, tok in ((0.1, "protein"), (1.0, "enzyme"), (10.0, "negative")):
    x, _ = crosslinked(eps, L)
    axs[0].plot(L, x, color=charts.line(tok), lw=1.6, label=f"eps = {eps:g}")
axs[0].set_xscale("log")
axs[0].set_ylim(0, 1.0)
axs[0].legend(frameon=False, fontsize=7, labelcolor=P.ink(), loc="upper left")
charts.style_axes(axs[0], "antigen concentration / K_D", "receptors in cross-linked pairs")
charts.title(axs[0], "A")

x, c1 = crosslinked(1.0, L)
xs = x ** 2 / (x ** 2 + 0.02 ** 2)
axs[1].plot(L, xs, color=charts.line("negative"), lw=1.8, label="degranulation (bivalent antigen)")
axs[1].plot(L, c1 + x, color=P.muted(), lw=1.2, ls="--", label="receptors occupied (any site)")
axs[1].plot(L, np.zeros_like(L), color=charts.line("protein"), lw=1.4, label="monovalent hapten")
axs[1].set_xscale("log")
axs[1].set_ylim(-0.03, 1.05)
axs[1].legend(frameon=False, fontsize=6.5, labelcolor=P.ink(), loc="center left")
charts.style_axes(axs[1], "antigen concentration / K_D", "relative response")
charts.title(axs[1], "B")
fig.tight_layout()
