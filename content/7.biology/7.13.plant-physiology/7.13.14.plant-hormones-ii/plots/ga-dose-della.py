# Gibberellin dose-response through DELLA de-repression (Eqs. 14.1-14.3, illustrative parameters).
# theta = GA^n/(Kd^n + GA^n); DELLA steady state D = s/(k0 + k1 theta); growth G = Gmax/(1 + D/KD).
import matplotlib.pyplot as plt
import numpy as np

ga = np.logspace(-2, 4, 400)   # nmol L^-1
Kd, n = 10.0, 1.0
k0, k1 = 1.0, 20.0
s_wt = 10.0                    # in units of k0 * KD


def model(ga, s=s_wt, k1=k1):
    th = ga ** n / (Kd ** n + ga ** n)
    d = s / (k0 + k1 * th)
    return th, d, 1 / (1 + d)


fig, (a1, a2) = plt.subplots(1, 2, figsize=(10.8, 4.2))
th, d, g = model(ga)
a1.plot(ga, th, color="#4f9a52", lw=2.1, label="GID1 occupancy θ")
a1.plot(ga, d / d.max(), color="#c0504d", lw=2.1, label="DELLA level D* (relative)")
a1.plot(ga, g, color="#2f6fb5", lw=2.6, label="growth rate G / Gmax")
a1.axvspan(1, 30, color="0.85", alpha=0.5, lw=0)
a1.text(5.5, 0.03, "≈ log-linear\nrange", ha="center", fontsize=8.5)
a1.set_xscale("log")
a1.set_xlabel("[GA] / (nmol L$^{-1}$)")
a1.set_ylabel("Relative value")
a1.set_ylim(0, 1.05)
a1.legend(frameon=False, fontsize=8.5, loc="lower right", bbox_to_anchor=(1.0, 0.18))
a1.text(0.012, 0.98, "A", fontsize=12, fontweight="bold", va="top")

for lab, kw, col, ls in (("wild type / GA-deficient + GA", {}, "#2f6fb5", "-"),
                         ("gai, Rht (DELLA not degraded, k1 = 0)", {"k1": 0.0}, "#c0504d", "--"),
                         ("slr1, la cry (no DELLA, s = 0)", {"s": 0.0}, "#4f9a52", "-.")):
    a2.plot(ga, model(ga, **kw)[2], color=col, lw=2.3, ls=ls, label=lab)
a2.set_xscale("log")
a2.set_xlabel("[GA] / (nmol L$^{-1}$)")
a2.set_ylabel("Growth rate G / Gmax")
a2.set_ylim(0, 1.1)
a2.legend(frameon=False, fontsize=8.5, loc="center left", bbox_to_anchor=(0.0, 0.62))
a2.text(0.012, 1.08, "B", fontsize=12, fontweight="bold", va="top")
for a in (a1, a2):
    a.spines[["top", "right"]].set_visible(False)
fig.tight_layout()
