"""Carnot cycle of a monatomic ideal gas on the p-V diagram, with an isotherm and an adiabat through the same state."""

import numpy as np
import matplotlib.pyplot as plt

gamma = 5 / 3
nR = 1.0
T1, T2 = 500.0, 300.0
V1, V2 = 1.0, 2.5
V3 = V2 * (T1 / T2) ** (1 / (gamma - 1))
V4 = V1 * (T1 / T2) ** (1 / (gamma - 1))


def iso(V, T):
    return nR * T / V


def adi(V, Va, Ta):
    return nR * Ta / Va * (Va / V) ** gamma


fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4.2))

# left: isotherm versus adiabat through one state
V = np.linspace(0.6, 4, 400)
ax1.plot(V, iso(V, T1), color="C0", lw=1.6, label="isotherm pV = const")
ax1.plot(V, adi(V, 1.5, T1 * 1.0), color="C3", lw=1.6, label=r"adiabat $pV^\gamma$ = const")
ax1.plot([1.5], [iso(1.5, T1)], "o", color="black", ms=4)
ax1.set_xlim(0.6, 4)
ax1.set_ylim(0, 800)
ax1.set_xlabel("V (arbitrary units)")
ax1.set_ylabel("p (arbitrary units)")
ax1.set_title(r"The adiabat is steeper by the factor $\gamma$")
ax1.legend(fontsize=9)

# right: Carnot cycle 1 -> 2 -> 3 -> 4 -> 1
seg = [
    (np.linspace(V1, V2, 200), lambda v: iso(v, T1), "C0"),
    (np.linspace(V2, V3, 200), lambda v: adi(v, V2, T1), "C3"),
    (np.linspace(V3, V4, 200), lambda v: iso(v, T2), "C0"),
    (np.linspace(V4, V1, 200), lambda v: adi(v, V4, T2), "C3"),
]
for Vs, f, col in seg:
    ax2.plot(Vs, f(Vs), color=col, lw=1.8)
    k = len(Vs) // 2
    ax2.annotate("", xy=(Vs[k + 1], f(Vs[k + 1])), xytext=(Vs[k - 1], f(Vs[k - 1])),
                 arrowprops=dict(arrowstyle="->", color=col, lw=1.4))
Vall = np.concatenate([s[0] for s in seg])
pall = np.concatenate([s[1](s[0]) for s in seg])
ax2.fill(Vall, pall, color="C0", alpha=0.12)
for name, (v, p) in {"1": (V1, iso(V1, T1)), "2": (V2, iso(V2, T1)),
                     "3": (V3, iso(V3, T2)), "4": (V4, iso(V4, T2))}.items():
    ax2.plot([v], [p], "o", color="black", ms=3.5)
    ax2.annotate(name, (v, p), (v + 0.1, p + 12), fontsize=10)
ax2.annotate(r"$T_1$", (1.7, iso(1.7, T1) + 15), color="C0", fontsize=10)
ax2.annotate(r"$T_2$", (3.2, iso(3.2, T2) - 45), color="C0", fontsize=10)
ax2.set_xlim(0.5, V3 + 0.5)
ax2.set_ylim(0, 560)
ax2.set_xlabel("V (arbitrary units)")
ax2.set_ylabel("p (arbitrary units)")
ax2.set_title("Carnot cycle: two isotherms and two adiabats")
fig.tight_layout()
