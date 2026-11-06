# Temperature response of plant respiration and thermal acclimation (models).
# (A) Short-term response normalised to 1 at 20 C: constant Q10 = 2, and a temperature-dependent
# Q10 = 3.09 - 0.043 T (Tjoelker et al. 2001), integrated as d ln R / dT = ln(Q10(T)) / 10; above ~40 C an
# inactivation factor (schematic) bends the curve down.
# (B) Plants acclimated to 15 C and 30 C share the curve shape but differ in base rate (type II acclimation);
# dots: rates at the growth temperature; the line between them gives the long-term apparent Q10.
import matplotlib.pyplot as plt
import numpy as np

T = np.linspace(0, 50, 501)


def rvar(T, Tref=20.0):
    q = 3.09 - 0.043 * T
    lnr = np.cumsum(np.log(q) / 10) * (T[1] - T[0])
    lnr -= np.interp(Tref, T, lnr)
    return np.exp(lnr)


inact = 1 / (1 + np.exp((T - 44) / 2.5))
r2 = 2.0 ** ((T - 20) / 10) * inact
rv = rvar(T) * inact
fig, (a, b) = plt.subplots(1, 2, figsize=(11, 4.2))
a.plot(T, r2, color="0.45", lw=1.8, ls="--", label="Q₁₀ = 2 (constant)")
a.plot(T, rv, color="#c0504d", lw=2.4, label="Q₁₀ = 3.09 − 0.043 T")
a.set_xlabel("Leaf temperature T / °C")
a.set_ylabel("Respiration rate (relative to 20 °C)")
a.set_xlim(0, 50)
a.set_ylim(0, 5)
a.legend(frameon=False, fontsize=9, loc="upper left")
a.set_title("A   Short-term response", loc="left", fontsize=10)

for base, Tg, col, name in ((1.0, 15, "#2f6fb5", "grown at 15 °C"), (0.62, 30, "#d9822b", "grown at 30 °C")):
    r = base * rvar(T) * inact
    b.plot(T, r, color=col, lw=2.2, label=name)
    b.plot(Tg, np.interp(Tg, T, r), "o", color=col, ms=8)
p1 = (15, np.interp(15, T, rvar(T)))
p2 = (30, 0.62 * np.interp(30, T, rvar(T)))
b.plot([p1[0], p2[0]], [p1[1], p2[1]], color="0.3", lw=1.2, ls=":")
q_long = (p2[1] / p1[1]) ** (10 / 15)
b.text(22.5, (p1[1] + p2[1]) / 2 + 0.35, f"long-term Q₁₀ ≈ {q_long:.2f}", ha="center", fontsize=9)
b.set_xlabel("Measurement temperature T / °C")
b.set_ylabel("Respiration rate (relative)")
b.set_xlim(0, 50)
b.set_ylim(0, 5)
b.legend(frameon=False, fontsize=9, loc="upper left")
b.set_title("B   Thermal acclimation", loc="left", fontsize=10)
for ax in (a, b):
    ax.spines[["top", "right"]].set_visible(False)
fig.tight_layout()
