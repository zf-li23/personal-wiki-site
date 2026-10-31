"""Open probability of two-state channels. A: a tension-gated channel (MscL-like: energy cost
50 kBT and area change 20 nm^2, so half-open at tau = 50/20 kBT/nm^2 = 10.3 mN/m), compared with a
channel of the same midpoint but half the area change. B: voltage gating, p_o = 1/(1 + exp(-z e
(V - V_half)/kBT)) for gating charges z = 1, 4, 12 at V_half = -40 mV, 25 C. C: the same curves as
ln[p_o/(1 - p_o)] against V: straight lines whose slope z e/kBT gives the gating charge."""

import numpy as np
import matplotlib.pyplot as plt
import wikibio as bio
from wikibio import charts

P = bio.P
kT = 4.114  # pN nm at 25 C
kT_e = 25.69  # mV

fig, axs = plt.subplots(1, 3, figsize=(10.5, 3.3))
fig.subplots_adjust(wspace=0.42, left=0.07, right=0.98, bottom=0.17, top=0.88)

# A: tension (1 kBT/nm^2 = 4.114 mN/m)
ax = axs[0]
tau = np.linspace(6, 14, 400)  # mN/m = pN/nm
for dA, de, tok, lab in ((20.0, 50.0, "channel", r"$\Delta A = 20\,\mathrm{nm^2}$"), (10.0, 25.0, "neutral", r"$\Delta A = 10\,\mathrm{nm^2}$")):
    po = 1 / (1 + np.exp(de - tau * dA / kT))
    ax.plot(tau, po, color=charts.line(tok), lw=1.8, label=lab)
t_half = 50 * kT / 20
ax.axvline(t_half, color=P.muted(), lw=0.6, ls=":")
ax.text(t_half + 0.4, 0.08, rf"$\tau_{{1/2}} = {t_half:.1f}$", fontsize=bio.core.FONT["tiny"], color=P.ink())
ax.legend(frameon=False, fontsize=bio.core.FONT["tiny"], labelcolor=P.ink(), loc="upper left")
charts.style_axes(ax, r"membrane tension $\tau$ / (mN m$^{-1}$)", r"$p_\mathrm{o}$")
charts.title(ax, "A  Tension gating")

# B: voltage
ax = axs[1]
V = np.linspace(-120, 40, 500)
Vh = -40.0
cols = (("neutral", 1), ("k", 4), ("na", 12))
for tok, z in cols:
    po = 1 / (1 + np.exp(-z * (V - Vh) / kT_e))
    ax.plot(V, po, color=charts.line(tok), lw=1.8, label=f"z = {z}")
ax.legend(frameon=False, fontsize=bio.core.FONT["tiny"], labelcolor=P.ink(), loc="upper left")
charts.style_axes(ax, r"membrane potential $V$ / mV", r"$p_\mathrm{o}$")
charts.title(ax, "B  Voltage gating")

# C: Boltzmann (logit) plot
ax = axs[2]
for tok, z in cols:
    lg = z * (V - Vh) / kT_e
    m = np.abs(lg) < 9
    ax.plot(V[m], lg[m], color=charts.line(tok), lw=1.8, label=f"z = {z}: slope {z / kT_e:.3f} per mV")
ax.legend(frameon=False, fontsize=bio.core.FONT["tiny"], labelcolor=P.ink(), loc="upper left")
ax.axhline(0, color=P.muted(), lw=0.5)
ax.set_ylim(-9, 9)
charts.style_axes(ax, r"$V$ / mV", r"$\ln[p_\mathrm{o}/(1-p_\mathrm{o})]$")
charts.title(ax, "C  Reading off the gating charge")
