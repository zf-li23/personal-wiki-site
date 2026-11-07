# Filtration along the glomerular capillaries (both kidneys lumped; illustrative, micropuncture-like values).
# Plasma flow Q(x) along the normalized capillary length x in [0, 1] obeys
#   dQ/dx = -Kf (P_GC(x) - P_BS - pi(C)),   C = C_a Q(0) / Q   (protein is not filtered),
# with Kf = 25 mL/min/mmHg (chosen so that equilibrium is reached at normal flow, as in rat micropuncture), P_GC falling from 50 to 48 mmHg, P_BS = 10 mmHg, afferent protein C_a = 6.9 g/dL
# and the Landis-Pappenheimer relation pi = 2.1 C + 0.16 C^2 + 0.009 C^3 (mmHg, C in g/dL).
# A: pressures along the capillary at a renal plasma flow (RPF) of 600 mL/min: the oncotic pressure rises until
# it balances the hydrostatic gradient (filtration equilibrium). B: net filtration pressure for three RPFs.
# C: GFR and filtration fraction against RPF: under filtration equilibrium GFR rises with plasma flow.
import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import solve_ivp

Kf, PBS, Ca = 25.0, 10.0, 6.9


def pi(C):
    return 2.1 * C + 0.16 * C ** 2 + 0.009 * C ** 3


def pgc(x):
    return 50.0 - 2.0 * x


def run(rpf):
    f = lambda x, q: [-Kf * max(pgc(x) - PBS - pi(Ca * rpf / q[0]), 0.0)]
    s = solve_ivp(f, (0, 1), [rpf], dense_output=True, max_step=0.002)
    x = np.linspace(0, 1, 400)
    q = s.sol(x)[0]
    return x, q, pi(Ca * rpf / q)


fig, axs = plt.subplots(1, 3, figsize=(12, 3.9))
x, q, p = run(600.0)
ax = axs[0]
ax.plot(x, pgc(x), color="#c0392b", lw=2, label="$P_{GC}$")
ax.plot(x, PBS + p, color="#2f6fb5", lw=2, label="$P_{BS} + \\pi_{GC}$")
ax.fill_between(x, PBS + p, pgc(x), color="#e08a3c", alpha=0.3, lw=0)
ax.plot(x, PBS + 0 * x, color="#7a7a7a", lw=1.5, ls="--", label="$P_{BS}$")
ax.text(0.04, 43.5, "net filtration\npressure", fontsize=8.5)
ax.set_ylim(0, 55)
ax.set_xlabel("Distance along capillary (afferent to efferent)")
ax.set_ylabel("Pressure (mmHg)")
ax.set_title("A  Starling forces, RPF 600 mL/min", loc="left", fontsize=11, fontweight="bold")
ax.legend(frameon=False, fontsize=8.5, loc="center right")

ax = axs[1]
for rpf, c in [(300, "#7a4fb3"), (600, "#e08a3c"), (1200, "#3c9a5f")]:
    x, q, p = run(rpf)
    ax.plot(x, pgc(x) - PBS - p, color=c, lw=2, label=f"RPF {rpf} mL/min, GFR {rpf - q[-1]:.0f}")
ax.set_ylim(0, 16)
ax.set_xlabel("Distance along capillary")
ax.set_ylabel("Net filtration pressure (mmHg)")
ax.set_title("B  Net filtration pressure", loc="left", fontsize=11, fontweight="bold")
ax.legend(frameon=False, fontsize=8, loc="upper right")

ax = axs[2]
rpfs = np.linspace(100, 1600, 40)
g = np.array([r - run(r)[1][-1] for r in rpfs])
ax.plot(rpfs, g, color="#c0392b", lw=2, label="GFR")
ax.set_xlabel("Renal plasma flow (mL/min)")
ax.set_ylabel("GFR (mL/min)", color="#c0392b")
ax.set_ylim(0, 300)
ax2 = ax.twinx()
ax2.plot(rpfs, 100 * g / rpfs, color="#2f6fb5", lw=2, ls="--")
ax2.set_ylabel("Filtration fraction (%)", color="#2f6fb5")
ax2.set_ylim(0, 30)
ax.axvline(600, color="#9e9e9e", lw=0.8)
ax.set_title("C  GFR depends on plasma flow", loc="left", fontsize=11, fontweight="bold")
for a in list(axs) + [ax2]:
    a.spines["top"].set_visible(False)
for a in axs:
    a.spines["right"].set_visible(False)
fig.tight_layout()
