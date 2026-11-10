# Quantitative precipitin curve from a gelation (Flory-Stockmayer type) model of the antibody-antigen lattice.
# Bivalent antibody (2 sites, 150 kDa), antigen with v identical independent sites (60 kDa), site affinity K = 1e8 / M,
# fixed antibody concentration 1 uM, antigen added. Free-site binding equilibrium  B = K a g  with
#   a = 2[Ab] - B,  g = v[Ag] - B;  p_a = B / (2[Ab]),  p_g = B / (v[Ag])  (fractions of sites bound).
# Branching-process closure: u (w) is the probability that a bond followed from an antigen (antibody) site toward an
# antibody (antigen) leads to a finite branch,
#   w = (1 - p_g + p_g u)^(v - 1),   u = 1 - p_a + p_a w;
# an antibody is in the sol if both of its sites lead to finite branches, an antigen if all v sites do.
# The precipitate is the infinite network (gel) fraction; its mass is plotted against the antigen/antibody molar ratio.
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import brentq

import wikibio as bio
from wikibio import charts

P = bio.P
AB, K, MAB, MAG = 1.0, 1e2, 150.0, 60.0  # concentrations in uM, K in 1/uM (= 1e8 / M), masses in kDa


def gel_masses(ratio, v):
    ag = ratio * AB
    sa, sg = 2 * AB, v * ag
    b = brentq(lambda x: K * (sa - x) * (sg - x) - x, 0, min(sa, sg))
    pa, pg = b / sa, b / sg
    u = w = 0.0
    for _ in range(4000):
        w = (1 - pg + pg * u) ** (v - 1)
        u = 1 - pa + pa * w
    gel_ab = 1 - (1 - pa + pa * w) ** 2
    gel_ag = 1 - (1 - pg + pg * u) ** v
    return gel_ab * AB * MAB + gel_ag * ag * MAG  # ug/ml of precipitate


ratios = np.linspace(0.005, 2.6, 400)
fig, ax = plt.subplots(figsize=(6.4, 3.6))
for v, tok in ((2, "neutral"), (4, "receptor"), (6, "protein")):
    y = [gel_masses(r, v) for r in ratios]
    ax.plot(ratios, y, color=charts.line(tok), lw=1.6, label=f"antigen valence $v = {v}$")
ax.axvspan(0.07, 1.66, color=P.muted(), alpha=0.10, lw=0)
ax.text(0.03, 20, "antibody\nexcess", fontsize=7, color=P.muted(), ha="left")
ax.text(2.1, 20, "antigen excess", fontsize=7, color=P.muted(), ha="center")
ax.text(0.9, 8, "precipitation window ($v = 6$)", fontsize=7, color=P.muted(), ha="center")
ax.set_xlim(0, 2.6)
ax.set_ylim(0, 215)
ax.legend(frameon=False, fontsize=7, labelcolor=P.ink(), loc="upper right")
charts.style_axes(ax, "antigen / antibody (molar ratio)", "precipitate ($\\mu$g/ml)")
fig.tight_layout()
