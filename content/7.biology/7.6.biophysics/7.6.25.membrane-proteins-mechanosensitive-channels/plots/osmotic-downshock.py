"""Mechanosensitive channels as a safety valve: a toy model of an osmotic downshock (Example 25.5.2).

A wall-less spherical cell (1 fL, like a spheroplast of E. coli) in 400 mM osmolyte is moved at t = 0 to
50 mM. Water enters at dV/dt = Lp A (RT dc - 2 tau / r) with Lp = 3e-13 m s^-1 Pa^-1; the membrane
tension is tau = KA (A/A0 - 1) with KA = 0.2 N/m, and the bilayer ruptures at 12 mN/m. Open channels
release osmolyte at rate N po(tau) p (c_in - c_out), with two-state gating (Formula 4.2.1 of 7.6.4, 25 C;
release by Formula 25.5.1):
MscS tau1/2 = 5.5 mN/m, dA = 8 nm^2, pore permeability 0.3e-18 m^3/s; MscL 10 mN/m, 20 nm^2,
1.4e-18 m^3/s (diffusion through a 3 nm pore 5 nm long). A: tension against time for a cell without
channels, with 20 MscS, and with 20 MscS and 100 MscL. B: internal osmolyte concentration."""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
import wikibio as bio
from wikibio import charts

P = bio.P
RT = 8.314 * 298.0
KBT = 4.11e-21
LP, KA, TLYS = 3e-13, 0.2, 0.012
V0 = 1e-18
R0 = (3 * V0 / (4 * np.pi)) ** (1 / 3)
A0 = 4 * np.pi * R0 ** 2
CIN0, COUT = 400.0, 50.0  # mol/m^3
CH = {"S": (5.5e-3, 8e-18, 0.3e-18), "L": (10e-3, 20e-18, 1.4e-18)}


def po(t, name):
    th, dA, _ = CH[name]
    return 1.0 / (1.0 + np.exp(-(t - th) * dA / KBT))


def rhs(_, y, counts):
    V, N = y
    r = (3 * V / (4 * np.pi)) ** (1 / 3)
    A = 4 * np.pi * r ** 2
    tau = max(KA * (A / A0 - 1.0), 0.0)
    cin = N / V
    dV = LP * A * (RT * (cin - COUT) - 2 * tau / r)
    dN = -sum(n * po(tau, k) * CH[k][2] * (cin - COUT) for k, n in counts.items())
    return [dV, dN]


def tension(V):
    r = (3 * V / (4 * np.pi)) ** (1 / 3)
    return np.maximum(KA * (4 * np.pi * r ** 2 / A0 - 1.0), 0.0)


def lysis(_, y, counts):
    return tension(y[0]) - TLYS


lysis.terminal = True

cases = [({}, "no channels", "negative", "-"),
         ({"S": 20}, "20 MscS", "lipid_head", "--"),
         ({"S": 20, "L": 100}, "20 MscS + 100 MscL", "channel", "-")]

fig, axs = plt.subplots(1, 2, figsize=(9.4, 3.4))
fig.subplots_adjust(wspace=0.3, left=0.08, right=0.98, bottom=0.17, top=0.86)
for i, (counts, lab, tok, ls) in enumerate(cases):
    sol = solve_ivp(rhs, (0, 0.5), [V0, CIN0 * V0], args=(counts,), events=lysis, method="LSODA",
                    max_step=1e-3, rtol=1e-8, atol=[1e-24, 1e-22])
    t = sol.t * 1e3
    axs[0].plot(t, tension(sol.y[0]) * 1e3, color=charts.line(tok), lw=1.4, ls=ls, label=lab)
    axs[1].plot(t, sol.y[1] / sol.y[0], color=charts.line(tok), lw=1.4, ls=ls, label=lab)
    if sol.t_events[0].size:
        te = sol.t_events[0][0] * 1e3
        axs[0].plot(te, TLYS * 1e3, "x", color=charts.line(tok), ms=7, mew=1.6)
        axs[0].annotate(f"lysis at {te:.0f} ms", (te, TLYS * 1e3), xytext=(te + 40 + 110 * i, TLYS * 1e3 + 0.9 - 0.7 * i),
                        fontsize=bio.core.FONT["tiny"], color=P.ink(),
                        arrowprops=dict(arrowstyle="-", color=P.muted(), lw=0.6))
ax = axs[0]
ax.axhspan(TLYS * 1e3, 14, color=P.light("negative"), lw=0)
ax.text(492, 12.6, "bilayer rupture", ha="right", fontsize=bio.core.FONT["tiny"], color=P.ink())
for th, nm in ((5.5, "MscS"), (10.0, "MscL")):
    ax.axhline(th, color=P.muted(), lw=0.6, ls=":")
    ax.text(493, th + 0.2, r"$\tau_{1/2}$ " + nm, ha="right", fontsize=bio.core.FONT["tiny"], color=P.muted())
ax.set_xlim(0, 500)
ax.set_ylim(0, 14)
ax.legend(frameon=False, fontsize=bio.core.FONT["tiny"], labelcolor=P.ink(), loc="lower right")
charts.style_axes(ax, "time after the shock / ms", r"membrane tension / (mN m$^{-1}$)")
charts.title(ax, "A  Tension is clamped below rupture")
ax = axs[1]
ax.axhline(COUT, color=P.muted(), lw=0.6, ls=":")
ax.text(495, COUT + 8, "outside", ha="right", fontsize=bio.core.FONT["tiny"], color=P.muted())
ax.set_xlim(0, 500)
ax.set_ylim(0, 420)
charts.style_axes(ax, "time after the shock / ms", "internal osmolyte / mM")
charts.title(ax, "B  Osmolytes are released")
