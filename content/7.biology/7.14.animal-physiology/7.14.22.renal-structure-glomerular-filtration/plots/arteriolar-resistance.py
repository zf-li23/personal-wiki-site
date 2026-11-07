# Afferent and efferent arteriolar resistance, GFR and renal blood flow (lumped model of both kidneys).
# Blood flows from the renal artery (Pa) through the afferent resistance Ra into glomerular capillaries at a
# uniform pressure P_GC, loses the filtrate (GFR, computed by integrating the Starling forces along the
# capillary exactly as in the filtration-equilibrium figure: Kf = 25 mL/min/mmHg, P_BS = 10 mmHg, afferent
# protein 6.9 g/dL), and leaves through the efferent resistance Re and the peritubular/venous resistance Rv
# to the renal vein (Pv = 5 mmHg). Hematocrit 0.45, so renal plasma flow RPF = 0.55 RBF.
# Normal state: Pa = 100, P_GC = 50 mmHg, RBF = 1100 mL/min. P_GC is found from the flow balance
#   (Pa - P_GC)/Ra = GFR(P_GC, RPF) + (P_GC - Pv)/(Re + Rv).
# A: raising Re raises P_GC but cuts RBF, so GFR first rises and then falls (biphasic). B: raising Ra lowers
# both. C: autoregulation: Ra adjusts (between 0.6 and 2.6 times normal, myogenic response and
# tubuloglomerular feedback) to hold RBF constant; outside that range, and with Ra fixed (dashed), flow and
# filtration follow pressure passively.
import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import brentq

Kf, PBS, Ca, H, Pv = 25.0, 10.0, 6.9, 0.45, 5.0


def pi(C):
    return 2.1 * C + 0.16 * C ** 2 + 0.009 * C ** 3


def gfr(pgc, rpf):
    if rpf <= 0:
        return 0.0
    f = lambda x, q: [-Kf * max(pgc - PBS - pi(Ca * rpf / q[0]), 0.0)]
    s = solve_ivp(f, (0, 1), [rpf], max_step=0.01)
    return rpf - s.y[0][-1]


RBF0, PGC0, PA0 = 1100.0, 50.0, 100.0
G0 = gfr(PGC0, (1 - H) * RBF0)
Ra0 = (PA0 - PGC0) / RBF0
Rv0 = 10.0 / (RBF0 - G0)
Re0 = (PGC0 - Pv) / (RBF0 - G0) - Rv0


def solve(Pa=PA0, ra=1.0, re=1.0):
    Ra, Re = ra * Ra0, re * Re0
    F = lambda p: (Pa - p) / Ra - gfr(p, (1 - H) * (Pa - p) / Ra) - (p - Pv) / (Re + Rv0)
    p = brentq(F, Pv + 1e-6, Pa - 1e-6)
    rbf = (Pa - p) / Ra
    return rbf, gfr(p, (1 - H) * rbf)


fig, axs = plt.subplots(1, 3, figsize=(12, 3.9))
mult = np.linspace(0.4, 4.0, 46)
for ax, key, title in [(axs[0], "re", "A  Efferent resistance"), (axs[1], "ra", "B  Afferent resistance")]:
    res = np.array([solve(**{key: m}) for m in mult])
    ax.plot(mult, res[:, 1], color="#c0392b", lw=2, label="GFR")
    ax.set_ylim(0, 250)
    ax.set_ylabel("GFR (mL/min)", color="#c0392b")
    ax2 = ax.twinx()
    ax2.plot(mult, res[:, 0], color="#2f6fb5", lw=2, ls="--")
    ax2.set_ylim(0, 2500)
    ax2.set_ylabel("Renal blood flow (mL/min)", color="#2f6fb5")
    ax2.spines["top"].set_visible(False)
    ax.plot([1], [G0], "o", color="#c0392b", ms=5)
    ax.set_xlabel("Resistance (x normal)")
    ax.set_title(title, loc="left", fontsize=11, fontweight="bold")
    ax.spines["top"].set_visible(False)

ax = axs[2]
pa = np.linspace(40, 220, 61)
auto, passive = [], []
for P in pa:
    ra = np.clip((P - PGC0) / RBF0 / Ra0, 0.6, 2.6)
    auto.append(solve(Pa=P, ra=ra))
    passive.append(solve(Pa=P, ra=1.0))
auto, passive = np.array(auto), np.array(passive)
ax.plot(pa, auto[:, 0] / RBF0, color="#2f6fb5", lw=2, label="RBF, autoregulated")
ax.plot(pa, passive[:, 0] / RBF0, color="#2f6fb5", lw=1.2, ls="--", label="RBF, Ra fixed")
ax.plot(pa, auto[:, 1] / G0, color="#c0392b", lw=2, label="GFR, autoregulated")
ax.plot(pa, passive[:, 1] / G0, color="#c0392b", lw=1.2, ls="--", label="GFR, Ra fixed")
ax.axvspan(80, 180, color="#9e9e9e", alpha=0.15, lw=0)
ax.set_ylim(0, 2.5)
ax.set_xlabel("Renal arterial pressure (mmHg)")
ax.set_ylabel("Relative to normal (Pa = 100 mmHg)")
ax.set_title("C  Autoregulation", loc="left", fontsize=11, fontweight="bold")
ax.legend(frameon=False, fontsize=7.5, loc="upper left")
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
fig.tight_layout()
