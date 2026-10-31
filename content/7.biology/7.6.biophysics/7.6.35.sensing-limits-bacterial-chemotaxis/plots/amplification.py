"""Two amplifiers of the chemotaxis pathway. A: zero-order ultrasensitivity of a modification cycle
(Goldbeter-Koshland function): steady-state fraction of modified substrate against the ratio of the
maximal rates of the converting enzymes, for Michaelis constants K/E_T = 1, 0.1 and 0.01 (both
enzymes equal). B: the effective Hill coefficient ln 81/ln(theta_90/theta_10) of these curves against
K/E_T; the dashed line is the hyperbolic response (n_H = 1). C: the switch of the flagellar motor,
the clockwise bias P_CW = Y^H/(Y^H + K^H) with H = 10.3 and K = 3.1 uM (fit of Cluzel, Surette and
Leibler, 2000), and its logarithmic gain dP_CW/d ln Y = H P_CW(1 - P_CW) (dashed, right axis): a 10 %
change of CheY-P near the midpoint changes the bias by about 25 percentage points."""

import numpy as np
import matplotlib.pyplot as plt
import wikibio as bio
from wikibio import charts

P = bio.P


def gk(theta, K):
    """Fraction modified f solving theta = f (1 - f + K)/((1 - f)(f + K)), K = K/E_T for both enzymes."""
    f = np.linspace(1e-7, 1 - 1e-7, 200001)
    th = f * (1 - f + K) / ((1 - f) * (f + K))
    return np.interp(theta, th, f)


fig, axs = plt.subplots(1, 3, figsize=(10.8, 3.3))
fig.subplots_adjust(wspace=0.55, left=0.06, right=0.93, bottom=0.17, top=0.88)
theta = np.logspace(-1, 1, 400)
ax = axs[0]
for K, tok in ((1.0, "neutral"), (0.1, "receptor"), (0.01, "enzyme")):
    ax.semilogx(theta, gk(theta, K), color=charts.line(tok), lw=1.4, label=rf"$K/E_{{\mathrm{{T}}}} = {K:g}$")
ax.legend(frameon=False, fontsize=7, loc="upper left")
charts.style_axes(ax, r"rate ratio $V_1/V_2$", "fraction modified")
charts.title(ax, "A  zero-order ultrasensitivity")

ax = axs[1]
Ks = np.logspace(-3, 1, 30)
nh = []
for K in Ks:
    f = np.array([0.1, 0.9])
    th = f * (1 - f + K) / ((1 - f) * (f + K))
    nh.append(np.log(81) / np.log(th[1] / th[0]))
ax.loglog(Ks, nh, color=charts.line("enzyme"), lw=1.4)
ax.axhline(1, color=P.muted(), lw=0.7, ls="--")
charts.style_axes(ax, r"$K/E_{\mathrm{T}}$", r"effective Hill coefficient $n_{\mathrm{H}}$")
charts.title(ax, "B  steepness")

ax = axs[2]
Y = np.linspace(0, 8, 400)
H, K = 10.3, 3.1
pcw = Y ** H / (Y ** H + K ** H)
ax.plot(Y, pcw, color=charts.line("flagellum"), lw=1.6)
charts.style_axes(ax, r"CheY-P / $\mu$M", r"CW bias $P_{\mathrm{CW}}$")
ax2 = ax.twinx()
ax2.plot(Y, H * pcw * (1 - pcw), color=charts.line("enzyme"), lw=1.1, ls="--")
charts.style_axes(ax2, None, r"gain $\mathrm{d}P_{\mathrm{CW}}/\mathrm{d}\ln Y$", box=True)
ax2.spines["top"].set_visible(False)
charts.title(ax, "C  motor switch")
