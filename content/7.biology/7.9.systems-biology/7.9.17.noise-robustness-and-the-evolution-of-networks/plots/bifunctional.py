"""Input-output curves of two phosphorylation circuits (mass-action steady states, model units).
A: monofunctional design: the sensor X phosphorylates the messenger Y with rate constant v (which
increases with the signal) and a separate phosphatase Z dephosphorylates it, so that
Yp = v X Y_T/(v X + Z) (nominal X = 1, Y_T = 10, Z = 1). Each curve changes one protein twofold up or
down; every change moves the curve.
B: bifunctional design (EnvZ-OmpR type), the full model with six species: X autophosphorylates with rate
constant k_a (the input); Xp transfers the phosphoryl group to Y through the complex XpY
(k1 = 10, k-1 = 1, kt = 5); unphosphorylated X dephosphorylates Yp through the complex XYp
(k2 = 10, k-2 = 1, kp = 1, so K2 = 0.2). Steady states for twofold changes of X_T or Y_T (points) all lie
on Yp = k_a K2/kp (dashed), until Yp approaches the available messenger (lowest Y_T, k_a > 20).
C: output at a fixed input against the total messenger level Y_T for both designs."""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
import wikibio as bio
from wikibio import charts

P = bio.P
k1, km1, kt = 10.0, 1.0, 5.0
k2, km2, kp = 10.0, 1.0, 1.0
K2 = (km2 + kp) / k2


def mono(v, X=1.0, YT=10.0, Z=1.0):
    return v * X * YT / (v * X + Z)


def bif(ka, XT=1.0, YT=10.0):
    def rhs(t, z):
        X, Xp, Y, Yp, XpY, XYp = z
        ra = ka * X
        r1 = k1 * Xp * Y - km1 * XpY
        rt = kt * XpY
        r2 = k2 * X * Yp - km2 * XYp
        rp = kp * XYp
        return [-ra + rt - r2 + rp, ra - r1, -r1 + rp, rt - r2, r1 - rt, r2 - rp]

    sol = solve_ivp(rhs, (0, 3000), [XT, 0, YT, 0, 0, 0], method="LSODA", rtol=1e-8, atol=1e-10)
    return sol.y[3, -1]


cases = [("nominal", {}, P.ink(), "-"),
         ("X x2", {"X": 2.0}, charts.line("protein"), "-"), ("X /2", {"X": 0.5}, charts.line("protein"), "--"),
         ("Y_T x2", {"YT": 20.0}, charts.line("highlight"), "-"), ("Y_T /2", {"YT": 5.0}, charts.line("highlight"), "--"),
         ("Z x2", {"Z": 2.0}, charts.line("negative"), "-"), ("Z /2", {"Z": 0.5}, charts.line("negative"), "--")]

fig, axs = plt.subplots(1, 3, figsize=(11, 3.4))
fig.subplots_adjust(left=0.07, right=0.98, bottom=0.17, top=0.86, wspace=0.36)

ax = axs[0]
v = np.logspace(-2, 2, 200)
for lab, kw, col, ls in cases:
    ax.semilogx(v, mono(v, **kw), ls, color=col, lw=1.2, label=lab)
ax.legend(fontsize=6.5, frameon=False, loc="upper left", ncol=2)
ax.set_ylim(0, 24)
charts.style_axes(ax, "input v", "output Yp")
charts.title(ax, "A  Separate kinase and phosphatase")

ax = axs[1]
kas = np.logspace(-1, 1.6, 12)
for lab, kw, col, ls in cases[:5]:
    kw2 = {("XT" if k == "X" else k): val for k, val in kw.items()}
    ax.semilogx(kas, [bif(k, **kw2) for k in kas], "o" + ls, ms=3, lw=0.9, color=col, label=lab)
kk = np.logspace(-1, 1.6, 100)
ax.semilogx(kk, kk * K2 / kp, ":", color=P.muted(), lw=1.2)
ax.legend(fontsize=6.5, frameon=False, loc="upper left")
ax.set_ylim(0, 10)
charts.style_axes(ax, "input k_a", "output Yp")
charts.title(ax, "B  Bifunctional sensor")

ax = axs[2]
YT = np.logspace(0, 2, 25)
ax.semilogx(YT, mono(1.0, YT=YT), color=charts.line("negative"), lw=1.5, label="monofunctional, v = 1")
ax.semilogx(YT, [bif(10.0, YT=y) for y in YT], "o-", ms=3, lw=1.2, color=charts.line("protein"),
            label="bifunctional, k_a = 10")
ax.legend(fontsize=7, frameon=False, loc="upper left")
charts.style_axes(ax, "total messenger Y_T", "output Yp")
charts.title(ax, "C  Dependence on Y_T")
