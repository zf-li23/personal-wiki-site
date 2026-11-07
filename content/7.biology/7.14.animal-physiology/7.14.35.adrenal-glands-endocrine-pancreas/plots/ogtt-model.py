# Oral glucose tolerance test (75 g) with a minimal-model core extended by gut absorption and incretins.
#   dQ1/dt = -ke Q1 ; dQ2/dt = ke Q1 - ka Q2 ; Ra = f ka Q2              (stomach, gut; mmol)
#   dG/dt = -(SG + X) G + SG Gb + Ra / V                                  (plasma glucose, mmol/L)
#   dX/dt = -p2 X + p2 SI (I - Ib)                                        (remote insulin action, 1/min)
#   dI/dt = -n (I - Ib) + beta [phi(G) - phi(Gb)] + iota Ra               (plasma insulin, pmol/L)
# Parameters are illustrative. Three subjects: normal; insulin sensitivity / 4 with beta-cell capacity x 2.5
# (compensated); insulin sensitivity / 4 with beta-cell capacity x 0.4 and fasting glucose 7.5 mmol/L (T2D). C: beta-cell capacity needed to bring
# 2-h glucose to 7.8 mmol/L versus insulin sensitivity (log-log): close to a hyperbola (slope -1).
import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import brentq

dose = 75.0 / 180.16 * 1000  # mmol
ke, ka, f, V = 0.02, 0.035, 0.9, 17.0
SG, p2, Ib, n = 0.012, 0.05, 50.0, 0.14


def phi(G):
    return G**4 / (9.0**4 + G**4)


def run(SI=1.0e-4, beta=200.0, iota=1.5, Gb=5.0, t_end=180.0):
    def rhs(t, y):
        Q1, Q2, G, X, I = y
        Ra = f * ka * Q2
        return [-ke * Q1, ke * Q1 - ka * Q2,
                -(SG + X) * G + SG * Gb + Ra / V,
                -p2 * X + p2 * SI * (I - Ib),
                -n * (I - Ib) + beta * (phi(G) - phi(Gb)) + iota * Ra]

    t = np.linspace(0, t_end, 721)
    sol = solve_ivp(rhs, (0, t_end), [dose, 0, Gb, 0, Ib], t_eval=t, max_step=0.5)
    return t, sol.y[2], sol.y[4]


cases = (
    (dict(), "#2c6fbb", "normal"),
    (dict(SI=0.25e-4, beta=500.0, iota=3.75), "#2e8b57", "SI / 4, beta-cell x 2.5 (compensated)"),
    (dict(SI=0.25e-4, beta=80.0, iota=0.6, Gb=7.5), "#c0392b", "SI / 4, beta-cell x 0.4, fasting 7.5 (T2D)"),
)
fig, axs = plt.subplots(1, 3, figsize=(14, 4.3))
for kw, col, lab in cases:
    t, G, I = run(**kw)
    axs[0].plot(t, G, color=col, lw=2, label=lab)
    axs[1].plot(t, I, color=col, lw=2, label=lab)
for y in (7.8, 11.1):
    axs[0].axhline(y, color="0.6", lw=0.9, ls="--")
axs[0].axvline(120, color="0.75", lw=0.8, ls=":")
axs[0].text(178, 7.95, "7.8", ha="right", fontsize=8, color="0.4")
axs[0].text(178, 11.25, "11.1", ha="right", fontsize=8, color="0.4")
axs[0].set_xlabel("Time after 75 g glucose / min")
axs[0].set_ylabel("Plasma glucose / (mmol/L)")
axs[0].set_title("A  Glucose", loc="left", fontsize=11, fontweight="bold")
axs[1].legend(frameon=False, fontsize=8, loc="upper right")
axs[1].set_xlabel("Time after 75 g glucose / min")
axs[1].set_ylabel("Plasma insulin / (pmol/L)")
axs[1].set_title("B  Insulin", loc="left", fontsize=11, fontweight="bold")

SIs = np.geomspace(0.2e-4, 2.0e-4, 9)
need = []
for SI in SIs:
    g2 = lambda b, SI=SI: run(SI=SI, beta=b, iota=1.5 * b / 200.0, t_end=120.0)[1][-1] - 7.8
    need.append(brentq(g2, 1.0, 3000.0, xtol=0.2))
need = np.array(need)
norm = np.exp(np.interp(0.0, np.log(SIs / 1e-4), np.log(need)))  # capacity needed at normal sensitivity
axs[2].loglog(SIs * 1e4, need / norm, "o-", color="#2c6fbb", lw=1.8, ms=4)
ref = (need[4] / norm) * (SIs[4] / SIs) 
axs[2].loglog(SIs * 1e4, ref, color="0.55", ls="--", lw=1, label="slope -1 (product constant)")
slope = np.polyfit(np.log(SIs), np.log(need), 1)[0]
axs[2].text(0.05, 0.08, f"fitted slope = {slope:.2f}", transform=axs[2].transAxes, fontsize=8.5)
axs[2].set_xlabel("Insulin sensitivity / normal")
axs[2].set_ylabel("Beta-cell capacity needed (relative)")
axs[2].set_title("C  Disposition index", loc="left", fontsize=11, fontweight="bold")
axs[2].legend(frameon=False, fontsize=8, loc="upper right")
fig.tight_layout()
