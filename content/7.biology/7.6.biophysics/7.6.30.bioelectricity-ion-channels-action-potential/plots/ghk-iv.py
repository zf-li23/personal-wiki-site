"""Current-voltage relations of ion channels. A, B: the Goldman-Hodgkin-Katz current equation for a
K+-selective (A) and a Na+-selective (B) membrane at 37 C (inside/outside K+ 155/4 mM, Na+ 12/145 mM,
the same permeability for both, current density normalized), compared with the linear (ohmic)
approximation I = g (V - E) whose slope is the GHK slope conductance at the reversal potential. Away
from the reversal potential the GHK current exceeds the linear one on the side where ions flow out of
the concentrated compartment: Goldman rectification. C: the NMDA receptor, a ligand-gated cation
channel (reversal potential near 0 mV), with external Mg2+ block described by the Woodhull model with
the Jahr-Stevens parameters, g(V) = g / (1 + [Mg2+]/3.57 mM * exp(-0.062 V/mV)): at 1 mM Mg2+ the
current is blocked at negative potentials and relieved by depolarization (J-shaped curve); without Mg2+
the relation is nearly linear."""

import numpy as np
import matplotlib.pyplot as plt
import wikibio as bio
from wikibio import charts

P = bio.P
FT = bio.core.FONT
fig, axs = plt.subplots(1, 3, figsize=(10.8, 3.2))
fig.subplots_adjust(wspace=0.38, left=0.07, right=0.98, bottom=0.17, top=0.87)

RT_F = 8.314 * 310.15 / 96485 * 1e3  # mV
V = np.linspace(-150, 120, 400)


def ghk(V, ci, co, z=1):
    u = z * V / RT_F
    u = np.where(np.abs(u) < 1e-9, 1e-9, u)
    return z * u * (ci - co * np.exp(-u)) / (1 - np.exp(-u))


for ax, (ion, ci, co, tok, lab) in zip(axs[:2], [("K", 155, 4, "k", "A  K$^+$ channel"),
                                               ("Na", 12, 145, "na", "B  Na$^+$ channel")]):
    I = ghk(V, ci, co)
    E = RT_F * np.log(co / ci)
    dV = 1e-3
    g = (ghk(E + dV, ci, co) - ghk(E - dV, ci, co)) / (2 * dV)
    ax.plot(V, I, color=charts.line(tok), lw=1.8, label="GHK current equation")
    ax.plot(V, g * (V - E), "--", color=P.muted(), lw=1.2, label=r"linear: $g(V - E)$")
    ax.axhline(0, color=P.muted(), lw=0.6)
    ax.axvline(E, color=P.muted(), lw=0.6, ls=":")
    ax.text(E + 4, ax.get_ylim()[1] * 0.0 + (-25 if ion == "K" else 25), f"E = {E:.0f} mV", fontsize=FT["tiny"],
            color=P.ink())
    ax.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="upper left")
    charts.style_axes(ax, "membrane potential $V$ / mV", "current density (outward +)")
    charts.title(ax, lab)

ax = axs[2]
Vn = np.linspace(-100, 60, 300)
for mg, tok in [(0.0, "neutral"), (1.0, "ca")]:
    I = (Vn - 0.0) / (1 + mg / 3.57 * np.exp(-0.062 * Vn))
    ax.plot(Vn, I, color=charts.line(tok), lw=1.8, label=rf"[Mg$^{{2+}}$]$_{{\mathrm{{o}}}}$ = {mg:g} mM")
ax.axhline(0, color=P.muted(), lw=0.6)
ax.axvline(0, color=P.muted(), lw=0.6)
ax.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="upper left")
charts.style_axes(ax, "membrane potential $V$ / mV", "NMDA current (a.u.)")
charts.title(ax, "C  Mg$^{2+}$ block")
