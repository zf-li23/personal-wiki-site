# Competition of CD28 and CTLA-4 for B7 on an antigen-presenting cell (equilibrium model, illustrative parameters).
# Units: concentrations in units of K_D(CD28-B7). K_D(CTLA-4-B7) = K_D(CD28-B7) / 10 (about one order of magnitude
# tighter binding). Receptors are treated as soluble pools (an effective-concentration approximation of the contact zone):
#   L_free + L_free*R28_free/K28 + L_free*R4_free/K4 = B_total,   R_free = R_total / (1 + L_free/K).
# A: CD28 occupancy (a proxy of costimulation) vs. the amount of CTLA-4 relative to CD28, for three B7 levels.
# B: share of the bound B7 that is held by CTLA-4, at the same B7 levels; the blockade point marks r = 0 (anti-CTLA-4).
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio
from wikibio import charts

P = bio.P
K28, K4, C28 = 1.0, 0.1, 1.0


def solve(btot, r):
    t4 = r * C28
    lo, hi = 0.0, btot
    for _ in range(80):
        x = 0.5 * (lo + hi)
        tot = x + x * (C28 / (1 + x / K28)) / K28 + x * (t4 / (1 + x / K4)) / K4
        if tot > btot:
            hi = x
        else:
            lo = x
    x = 0.5 * (lo + hi)
    o28 = x * (C28 / (1 + x / K28)) / K28
    o4 = x * (t4 / (1 + x / K4)) / K4
    return o28 / C28, o4, o28


r = np.logspace(-2, 1, 120)
fig, axs = plt.subplots(1, 2, figsize=(9.5, 3.6))
toks = {0.3: "protein", 1.0: "enzyme", 3.0: "negative"}
for b, tok in toks.items():
    res = np.array([solve(b, x) for x in r])
    axs[0].plot(r, res[:, 0], color=charts.line(tok), lw=1.6, label=f"B7 = {b:g}")
    share = res[:, 1] / (res[:, 1] + res[:, 2])
    axs[1].plot(r, share, color=charts.line(tok), lw=1.6, label=f"B7 = {b:g}")
    axs[0].plot([0.01], [solve(b, 0)[0]], "o", ms=4, color=charts.line(tok))
for a in axs:
    a.set_xscale("log")
axs[0].set_ylim(0, 1.0)
axs[1].set_ylim(0, 1.0)
axs[0].axvline(0.2, color=P.muted(), lw=0.7, ls=":")
axs[1].axvline(0.2, color=P.muted(), lw=0.7, ls=":")
axs[0].text(0.21, 0.92, "CTLA-4 at 0.2 x CD28", fontsize=6.5, color=P.muted(), ha="left")
axs[0].legend(frameon=False, fontsize=7, labelcolor=P.ink(), loc="upper right")
charts.style_axes(axs[0], "CTLA-4 / CD28 (total receptor ratio)", "CD28 occupancy")
charts.style_axes(axs[1], "CTLA-4 / CD28 (total receptor ratio)", "fraction of bound B7 held by CTLA-4")
charts.title(axs[0], "A")
charts.title(axs[1], "B")
fig.tight_layout()
