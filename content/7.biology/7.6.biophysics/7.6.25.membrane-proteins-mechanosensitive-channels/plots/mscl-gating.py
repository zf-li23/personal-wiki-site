"""Gating of MscL by tension and hydrophobic mismatch (the model of Formula 25.4.1).

G(R) = G0 + 2 pi R f - pi R^2 tau with line tension f = K U^2/2, K = 20 kBT/nm^3, closed radius
Rc = 2.3 nm, open radius Ro = 3.5 nm and mismatch U = 0.065 (12 - n) nm for lipids with n carbons per
chain (Wiggins and Phillips 2004). A: free energy against channel radius for n = 18 at zero tension,
at the critical tension and above it; radii below Rc are sterically forbidden, radii above Ro would
separate the helices. B: open probability of the two-state channel, ln(po/pc) = -(dG0 - tau dA)/kBT
with dG0 = 2 pi f (Ro - Rc) and dA = pi (Ro^2 - Rc^2) = 21.9 nm^2, for n = 16, 18, 20 (kBT = 4.1 pN nm).
C: the zero-tension free-energy difference from the model against the values obtained by Perozo and
colleagues (2002) from patch-clamp gating curves of MscL in PC bilayers of the three chain lengths."""

import numpy as np
import matplotlib.pyplot as plt
import wikibio as bio
from wikibio import charts

P = bio.P
K, RC, RO = 20.0, 2.3, 3.5
KBT = 4.1  # pN nm = mN/m * nm^2
DA = np.pi * (RO ** 2 - RC ** 2)


def f_line(n):
    U = 0.065 * (12 - n)
    return 0.5 * K * U ** 2


def dG0(n):
    return 2 * np.pi * f_line(n) * (RO - RC)


def tau_c(n):
    return 2 * f_line(n) / (RO + RC)  # kBT/nm^2


fig, axs = plt.subplots(1, 3, figsize=(10.6, 3.4))
fig.subplots_adjust(wspace=0.36, left=0.06, right=0.98, bottom=0.17, top=0.86)

ax = axs[0]
n = 18
R = np.linspace(RC, RO, 200)
tc = tau_c(n)
for t, ls, lab in ((0.0, "-", r"$\tau = 0$"), (tc, "--", r"$\tau = \tau^*$"), (1.6 * tc, ":", r"$\tau = 1.6\,\tau^*$")):
    G = 2 * np.pi * R * f_line(n) - np.pi * R ** 2 * t
    G0 = 2 * np.pi * RC * f_line(n) - np.pi * RC ** 2 * t
    ax.plot(R, G - G0, color=charts.line("channel"), lw=1.4, ls=ls, label=lab)
ax.axvspan(1.9, RC, color=P.light("neutral"), lw=0)
ax.axvspan(RO, 3.9, color=P.light("neutral"), lw=0)
ax.text(2.1, -14, "steric\nlimit", ha="center", fontsize=bio.core.FONT["tiny"], color=P.muted())
ax.text(3.7, -14, "helices\nseparate", ha="center", fontsize=bio.core.FONT["tiny"], color=P.muted())
ax.axhline(0, color=P.muted(), lw=0.5)
ax.set_xlim(1.9, 3.9)
ax.set_ylim(-17, 15)
ax.legend(frameon=False, fontsize=bio.core.FONT["tiny"], labelcolor=P.ink(), loc="upper left")
charts.style_axes(ax, r"channel radius $R$ / nm", r"$[G(R) - G(R_{\mathrm{c}})]/k_{\mathrm{B}}T$")
charts.title(ax, "A  Free-energy landscape (n = 18)")

ax = axs[1]
tau = np.linspace(0, 6, 400)  # mN/m
for n, tok in ((16, "channel"), (18, "lipid_head"), (20, "negative")):
    t = tau / KBT
    po = 1.0 / (1.0 + np.exp(dG0(n) - t * DA))
    ax.plot(tau, po, color=charts.line(tok), lw=1.4, label=f"PC{n}: " + r"$\tau^*$" + f" = {tau_c(n) * KBT:.1f} mN/m")
ax.set_ylim(-0.02, 1.02)
ax.legend(frameon=False, fontsize=bio.core.FONT["tiny"], labelcolor=P.ink(), loc="lower right")
charts.style_axes(ax, r"membrane tension $\tau$ / (mN m$^{-1}$)", r"open probability $p_{\mathrm{o}}$")
charts.title(ax, "B  Thicker bilayers need more tension")

ax = axs[2]
ns = np.array([16, 18, 20])
exp = np.array([4.0, 9.4, 23.5])
nn = np.linspace(14, 21, 100)
ax.plot(nn, [dG0(v) for v in nn], color=charts.line("channel"), lw=1.4, label=r"model, $\propto (12 - n)^2$")
ax.plot(ns, exp, "o", color=charts.line("negative"), ms=5, label="Perozo et al. 2002")
ax.plot(ns, [dG0(v) for v in ns], "s", color=charts.line("channel"), ms=4)
ax.set_xticks([14, 16, 18, 20])
ax.legend(frameon=False, fontsize=bio.core.FONT["tiny"], labelcolor=P.ink(), loc="upper left")
charts.style_axes(ax, "carbons per lipid chain n", r"$\Delta G(\tau = 0)/k_{\mathrm{B}}T$")
charts.title(ax, "C  Model and experiment")
