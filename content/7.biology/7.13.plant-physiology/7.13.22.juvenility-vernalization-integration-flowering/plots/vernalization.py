# Quantitative description of vernalization (simple model, illustrative parameters).
# A: relative effectiveness r(T) of a day at temperature T: zero below about -2 C, maximal between
#    1 and 7 C, falling to zero at about 12 C (effective range 0-10 C, optimum 1-7 C).
# B: days from sowing to flowering against the duration of cold, D = Dmin + (D0 - Dmin) exp(-V / Vs)
#    with V the accumulated vernalization days; winter type (D0 = 160 d, Vs = 15 d) and spring type
#    (D0 = 70 d, Vs = 5 d), both with Dmin = 55 d.
# C: stabilization of the vernalized state: fraction of plants still vernalized after a devernalizing
#    treatment (3 d at 35 C) given right after cold, rising with the duration of cold (after the
#    pattern of Purvis and Gregory's winter-rye data).
import matplotlib.pyplot as plt
import numpy as np


def r(T):
    T = np.asarray(T, float)
    up = np.clip((T + 2) / 3, 0, 1)
    down = np.clip((12 - T) / 5, 0, 1)
    return np.minimum(up, down)


fig, (ax, bx, cx) = plt.subplots(1, 3, figsize=(11.5, 3.8))
T = np.linspace(-6, 16, 400)
ax.plot(T, r(T), color="#2f6fb5", lw=2.2)
ax.axvspan(1, 7, color="#2f6fb5", alpha=0.12, lw=0)
ax.text(4, 1.06, "optimum", ha="center", fontsize=8, color="#2f6fb5")
ax.set_xlabel("Temperature / °C")
ax.set_ylabel("Vernalizing effectiveness r(T)")
ax.set_ylim(0, 1.15)
ax.set_xlim(-6, 16)

w = np.linspace(0, 10, 300)  # weeks at 4 C, r = 1
V = 7 * w
for name, D0, Vs, col in (("winter type", 160, 15, "#2f6fb5"), ("spring type", 70, 5, "#d9822b")):
    bx.plot(w, 55 + (D0 - 55) * np.exp(-V / Vs), color=col, lw=2.2, label=name)
bx.axhline(55, color="0.5", lw=0.8, ls=":")
bx.text(9.9, 58, "minimum (photoperiod, temperature)", ha="right", fontsize=7, color="0.4")
bx.set_xlabel("Cold treatment at 4 °C / weeks")
bx.set_ylabel("Days to flowering / d")
bx.set_ylim(0, 170)
bx.legend(frameon=False, fontsize=8)

stab = 100 * (1 - np.exp(-((w / 4.0) ** 2)))
cx.plot(w, stab, color="#3a9a5b", lw=2.2)
cx.set_xlabel("Cold treatment at 5 °C / weeks")
cx.set_ylabel("Still vernalized after 35 °C / %")
cx.set_ylim(0, 105)
for a, letter in zip((ax, bx, cx), "ABC"):
    a.spines[["top", "right"]].set_visible(False)
    a.text(-0.2, 1.04, letter, transform=a.transAxes, fontsize=12, weight="bold")
fig.tight_layout()
