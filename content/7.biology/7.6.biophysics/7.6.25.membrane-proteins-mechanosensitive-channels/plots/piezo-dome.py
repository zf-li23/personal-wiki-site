"""A toy elastic dome for Piezo (Theorem 25.6.1).

The channel and the membrane it bends form a spherical cap of fixed area Ad = 700 nm^2 with mean
curvature c, bending energy 2 kappa Ad (c - ci)^2 (preferred curvature ci, kappa = 20 kBT) and projected
area Ap = Ad (1 - Ad c^2 / 4 pi). Tension tau flattens the dome: c = ci / (1 + tau/tau_d) with
tau_d = 8 pi kappa / Ad = 0.72 kBT/nm^2 (2.9 mN/m). Closed state ci = 1/(12 nm), open state
ci = 1/(25 nm); the gating free energy at zero tension is chosen so that the channel is half open at
1.4 mN/m. A: profile of the closed dome (bulging into the cytoplasm) at three tensions. B: projected
area gained relative to zero tension by each state, and the effective area change of gating,
dA_eff = -d(dG)/d(tau), which shrinks as both states flatten. C: log-odds of opening for the dome model
(curved: its slope is dA_eff/kBT) against a two-state channel with constant dA = dA_eff(0) (straight)."""

import numpy as np
import matplotlib.pyplot as plt
import wikibio as bio
from wikibio import charts

P = bio.P
KBT = 4.1
KAP, AD = 20.0, 700.0
CC, CO = 1 / 12.0, 1 / 25.0
TD = 8 * np.pi * KAP / AD  # kBT/nm^2


def curv(ci, t):
    return ci / (1 + t / TD)


def Gstate(ci, t):
    a, b = 2 * KAP, t * AD / (4 * np.pi)
    return AD * a * b * ci ** 2 / (a + b) - t * AD


def proj(c):
    return AD * (1 - AD * c ** 2 / (4 * np.pi))


t_half = 1.4 / KBT
DG0 = -(Gstate(CO, t_half) - Gstate(CC, t_half))


def dG(t):
    return DG0 + Gstate(CO, t) - Gstate(CC, t)


def dA_eff(t):
    return AD ** 2 / (4 * np.pi) * (CC ** 2 - CO ** 2) / (1 + t / TD) ** 2


fig, axs = plt.subplots(1, 3, figsize=(10.6, 3.4))
fig.subplots_adjust(wspace=0.36, left=0.06, right=0.98, bottom=0.17, top=0.86)

ax = axs[0]
for tm, ls in ((0.0, "-"), (1.4, "--"), (5.0, ":")):
    c = curv(CC, tm / KBT)
    R = 1 / c
    cos_th = 1 - AD * c ** 2 / (2 * np.pi)
    rb = R * np.sqrt(1 - cos_th ** 2)
    r = np.linspace(-rb, rb, 200)
    z = -(np.sqrt(R ** 2 - r ** 2) - R * cos_th)
    ax.plot(np.r_[-24, r, 24], np.r_[0, z, 0], color=charts.line("channel"), lw=1.5, ls=ls,
            label=f"{tm:g} mN/m: depth {R * (1 - cos_th):.1f} nm")
ax.text(-23, 0.8, "outside", fontsize=bio.core.FONT["tiny"], color=P.muted())
ax.text(-23, -11.5, "cytoplasm", fontsize=bio.core.FONT["tiny"], color=P.muted())
ax.set_xlim(-24, 24)
ax.set_ylim(-12.5, 11)
ax.legend(frameon=False, fontsize=bio.core.FONT["tiny"], labelcolor=P.ink(), loc="upper right")
charts.style_axes(ax, "r / nm", "z / nm")
charts.title(ax, "A  Tension flattens the dome")

ax = axs[1]
tm = np.linspace(0, 8, 300)
t = tm / KBT
ax.plot(tm, proj(curv(CC, t)) - proj(CC), color=charts.line("channel"), lw=1.4, label="closed state")
ax.plot(tm, proj(curv(CO, t)) - proj(CO), color=charts.line("positive"), lw=1.4, label="open state")
ax.plot(tm, dA_eff(t), color=charts.line("negative"), lw=1.4, ls="--", label=r"$\Delta A_{\mathrm{eff}}$ of gating")
ax.axvline(TD * KBT, color=P.muted(), lw=0.6, ls=":")
ax.text(TD * KBT + 0.15, 250, r"$\tau_{\mathrm{d}}$", fontsize=bio.core.FONT["tiny"], color=P.muted())
ax.legend(frameon=False, fontsize=bio.core.FONT["tiny"], labelcolor=P.ink(), loc="center right")
charts.style_axes(ax, r"tension $\tau$ / (mN m$^{-1}$)", r"area / nm$^2$")
charts.title(ax, "B  Projected area")

ax = axs[2]
tm = np.linspace(0, 4, 400)
t = tm / KBT
lo = -dG(t)
lo2 = dA_eff(0) * (t - t_half)
ax.plot(tm, lo, color=charts.line("channel"), lw=1.4, label="elastic dome")
ax.plot(tm, lo2, color=charts.line("neutral"), lw=1.2, ls=":", label=r"constant $\Delta A = \Delta A_{\mathrm{eff}}(0)$")
ax.axhline(0, color=P.muted(), lw=0.5)
ax.axvline(1.4, color=P.muted(), lw=0.5, ls=":")
ax.set_ylim(-55, 40)
ax.legend(frameon=False, fontsize=bio.core.FONT["tiny"], labelcolor=P.ink(), loc="lower right")
charts.style_axes(ax, r"tension $\tau$ / (mN m$^{-1}$)", r"$\ln[p_{\mathrm{o}}/(1 - p_{\mathrm{o}})]$")
charts.title(ax, "C  Log-odds of opening")
