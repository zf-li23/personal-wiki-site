# Temperature, ethylene and the storage life of fresh produce (illustrative model).
# The rate of deterioration is r(T, E) = r0 Q10^((T - 20) / 10) (1 + a E / (Ke + E)) and the storage
# life is L = 1 / r, with L = 7 d at 20 C in ethylene-free air. Curves: Q10 = 2 and Q10 = 3 without
# ethylene, and Q10 = 3 with 1 uL L^-1 ethylene (a = 2, Ke = 0.3 uL L^-1).
# Shaded: below about 10 C chilling-sensitive produce of tropical origin (banana, cucumber, mango) is
# injured, so their storage life does not keep increasing as the temperature falls.
import matplotlib.pyplot as plt
import numpy as np

T = np.linspace(0, 30, 300)
L20 = 7.0


def life(T, q10, E=0.0, a=2.0, Ke=0.3):
    return L20 / (q10 ** ((T - 20) / 10) * (1 + a * E / (Ke + E)))


fig, ax = plt.subplots(figsize=(7.8, 4.3))
ax.axvspan(0, 10, color="#6fa8dc", alpha=0.14, lw=0)
ax.text(5, 150, "chilling injury\n(tropical produce)", ha="center", fontsize=8, color="#2f6fb5")
ax.plot(T, life(T, 2), color="#3a9a5b", lw=2.2, label="Q₁₀ = 2, no ethylene")
ax.plot(T, life(T, 3), color="#2f6fb5", lw=2.2, label="Q₁₀ = 3, no ethylene")
ax.plot(T, life(T, 3, E=1.0), color="#d93a2b", lw=2.2, ls="--", label="Q₁₀ = 3, ethylene 1 μL L⁻¹")
ax.set_yscale("log")
ax.set_xlabel("Storage temperature / °C")
ax.set_ylabel("Storage life / d")
ax.set_xlim(0, 30)
ax.set_ylim(1, 300)
ax.legend(frameon=False, fontsize=8, loc="upper right")
ax.spines[["top", "right"]].set_visible(False)
fig.tight_layout()
