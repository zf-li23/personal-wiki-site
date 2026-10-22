"""Phase diagram of water on a logarithmic pressure axis, computed from the IAPWS
correlations: saturation pressure (Wagner-Pruss), sublimation pressure and the melting
curves of ices Ih, III, V, VI and VII (IAPWS R14-08). Boundaries between the solid
phases themselves are omitted."""

import numpy as np
import matplotlib.pyplot as plt

Tt, pt = 273.16, 611.657          # triple point (K, Pa)
Tc, pc = 647.096, 22.064e6        # critical point (K, Pa)


def p_sat(T):
    tau = 1 - T / Tc
    a = [-7.85951783, 1.84408259, -11.7866497, 22.6807411, -15.9618719, 1.80122502]
    e = [1, 1.5, 3, 3.5, 4, 7.5]
    return pc * np.exp(Tc / T * sum(ai * tau**ei for ai, ei in zip(a, e)))


def p_sub(T):
    th = T / Tt
    a = [-0.212144006e2, 0.273203819e2, -0.610598130e1]
    b = [0.333333333e-2, 0.120666667e1, 0.170333333e1]
    return pt * np.exp(sum(ai * th**bi for ai, bi in zip(a, b)) / th)


def p_ih(T):
    th = T / Tt
    a = [0.119539337e7, 0.808183159e5, 0.333826860e4]
    b = [0.300000e1, 0.257500e2, 0.103750e3]
    return pt * (1 + sum(ai * (1 - th**bi) for ai, bi in zip(a, b)))


def p_iii(T):
    return 208.566e6 * (1 - 0.299948 * (1 - (T / 251.165) ** 60))


def p_v(T):
    return 350.1e6 * (1 - 1.18721 * (1 - (T / 256.164) ** 8))


def p_vi(T):
    return 632.4e6 * (1 - 1.07476 * (1 - (T / 273.31) ** 4.6))


def p_vii(T):
    th = T / 355.0
    return 2216e6 * np.exp(1.73683 * (1 - 1 / th) - 0.544606e-1 * (1 - th**5) + 0.806106e-7 * (1 - th**22))


fig, ax = plt.subplots(figsize=(7.2, 5.0))
lw = 1.8
T = np.linspace(200, Tt, 200)
ax.plot(T, p_sub(T), color="C0", lw=lw)
T = np.linspace(Tt, Tc, 400)
ax.plot(T, p_sat(T), color="C0", lw=lw)
T = np.linspace(240, Tt, 100)
ax.plot(T, p_sat(T), color="C0", lw=1.2, ls="--")          # supercooled water
for f, T1, T2 in [(p_ih, 251.165, Tt), (p_iii, 251.165, 256.164), (p_v, 256.164, 273.31),
                  (p_vi, 273.31, 355.0), (p_vii, 355.0, 700.0)]:
    T = np.linspace(T1, T2, 200)
    ax.plot(T, f(T), color="C0", lw=lw)

ax.plot([Tt], [pt], "o", color="C3", zorder=5)
ax.annotate("triple point\n273.16 K, 611.657 Pa", (Tt, pt), xytext=(290, 25), fontsize=8,
            arrowprops=dict(arrowstyle="-", color="0.5", lw=0.8))
ax.plot([Tc], [pc], "o", color="C3", zorder=5)
ax.annotate("critical point\n647.096 K, 22.064 MPa", (Tc, pc), xytext=(560, 1.5e5), fontsize=8,
            arrowprops=dict(arrowstyle="-", color="0.5", lw=0.8))
ax.axhline(101325, color="0.6", lw=0.8, ls=":")
ax.text(205, 1.4e5, "101.325 kPa", fontsize=8, color="0.45")
ax.annotate("supercooled\nwater", (250, p_sat(250)), xytext=(212, 2.5e3), fontsize=8,
            arrowprops=dict(arrowstyle="-", color="0.5", lw=0.8))

ax.text(215, 3e6, "ice Ih", fontsize=11)
ax.text(232, 2.6e8, "III", fontsize=9)
ax.text(246, 4.6e8, "V", fontsize=9)
ax.text(262, 1.1e9, "VI", fontsize=9)
ax.text(330, 6e9, "VII", fontsize=10)
ax.text(420, 2e7, "liquid", fontsize=11)
ax.text(470, 1.2e3, "vapor", fontsize=11)
ax.text(660, 3e8, "supercritical\nfluid", fontsize=8, ha="right")

ax.set_yscale("log")
ax.set_xlim(200, 700)
ax.set_ylim(1, 3e10)
ax.set_xlabel(r"$T\,/\,\mathrm{K}$")
ax.set_ylabel(r"$p\,/\,\mathrm{Pa}$")
fig.tight_layout()
