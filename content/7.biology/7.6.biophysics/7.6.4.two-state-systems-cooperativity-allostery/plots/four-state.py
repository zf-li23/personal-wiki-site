"""The four-state receptor: an activity variable (inactive/active, energy cost eps of activation)
and a binding variable (empty/bound); the bound ligand stabilises the active state by J (energies
in kBT). A: activity (solid) and occupancy (dashed) against ligand concentration (in units of the
dissociation constant K_I of the inactive receptor): with one site, activity is leak + (ceiling -
leak) x occupancy; for eps = 5, J = 10 it rises from 1/(1 + e^5) to 1/(1 + e^-5), a gain of about
150, and nearly coincides with occupancy; for eps = 2, J = 3 it rises only from 0.12 to 0.73. B: amplification (activity with ligand bound / activity without) against eps for three
couplings; it approaches e^J once eps exceeds J. C: the apparent dissociation
constant of the occupancy curve against eps: it moves from K_A = K_I e^-J (receptor mostly active)
to K_I (mostly inactive), the reciprocal face of the same coupling."""

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import brentq
import wikibio as bio
from wikibio import charts

P = bio.P


def curves(x, eps, J):
    w = np.array([np.ones_like(x), np.exp(-eps) * np.ones_like(x), x, x * np.exp(-(eps - J))])
    Z = w.sum(axis=0)
    return (w[2] + w[3]) / Z, (w[1] + w[3]) / Z


fig, axs = plt.subplots(1, 3, figsize=(10.5, 3.3))
fig.subplots_adjust(wspace=0.42, left=0.07, right=0.98, bottom=0.17, top=0.88)

ax = axs[0]
x = np.logspace(-6, 3, 600)
for eps_, J_, tok in ((5.0, 10.0, "positive"), (2.0, 3.0, "enzyme")):
    occ, act = curves(x, eps_, J_)
    ax.plot(x, occ, color=charts.line(tok), lw=1.0, ls="--")
    ax.plot(x, act, color=charts.line(tok), lw=1.8, label=rf"$\varepsilon = {eps_:.0f}$, $J = {J_:.0f}$")
ax.set_xscale("log")
ax.set_ylim(-0.02, 1.05)
ax.legend(frameon=False, fontsize=bio.core.FONT["tiny"], labelcolor=P.ink(), loc="upper left")
ax.text(3e-6, 0.5, "solid: activity\ndashed: occupancy", fontsize=bio.core.FONT["tiny"], color=P.ink())
charts.style_axes(ax, r"$c/K_\mathrm{I}$", "probability")
charts.title(ax, "A  Leak, ceiling and occupancy")

ax = axs[1]
eps = np.linspace(-4, 16, 300)
for J, tok in ((4.0, "neutral"), (7.0, "enzyme"), (10.0, "positive")):
    amp = (1 + np.exp(eps)) / (1 + np.exp(eps - J))
    ax.plot(eps, amp, color=charts.line(tok), lw=1.8, label=f"J = {J:.0f}")
    ax.axhline(np.exp(J), color=charts.line(tok), lw=0.5, ls=":")
ax.set_yscale("log")
ax.legend(frameon=False, fontsize=bio.core.FONT["tiny"], labelcolor=P.ink(), loc="upper left")
charts.style_axes(ax, r"activation cost $\varepsilon$ / $k_\mathrm{B}T$", "amplification $p_\\mathrm{a}(1)/p_\\mathrm{a}(0)$")
charts.title(ax, r"B  Gain limited by $\mathrm{e}^{J}$")

ax = axs[2]
for J, tok in ((4.0, "neutral"), (7.0, "enzyme"), (10.0, "positive")):
    kapp = [brentq(lambda lx: curves(np.array([10 ** lx]), e, J)[0][0] - 0.5, -12, 6) for e in eps]
    ax.plot(eps, kapp, color=charts.line(tok), lw=1.8, label=f"J = {J:.0f}")
ax.axhline(0, color=P.muted(), lw=0.5)
ax.legend(frameon=False, fontsize=bio.core.FONT["tiny"], labelcolor=P.ink(), loc="lower right")
charts.style_axes(ax, r"$\varepsilon$ / $k_\mathrm{B}T$", r"$\log_{10}(K_\mathrm{app}/K_\mathrm{I})$")
charts.title(ax, "C  Activity tunes affinity")
