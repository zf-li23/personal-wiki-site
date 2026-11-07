# Placental O2 transfer with nonlinear hemoglobin binding for three flow geometries
# (illustrative values for a human term pregnancy).
#   Maternal blood: arterial PO2 95 mmHg, Hb 120 g/L, P50 27 mmHg; flow Qm = 500 mL/min.
#   Fetal blood: umbilical arterial PO2 16 mmHg, Hb 170 g/L, P50 19 mmHg (HbF) or 27 (hypothetical HbA);
#   flow Qf = 350 mL/min. Hill coefficient 2.7; O2 content C = 1.34 Hb S(P) + 0.03 P (mL O2 / L).
#   Along the exchanger (x from 0 to 1): Qm dCm/dx = -G (Pm - Pf), Qf dCf/dx = +/- G (Pm - Pf).
#   Concurrent: both streams enter at x = 0. Countercurrent: fetal blood enters at x = 1 (shooting).
#   Pool ("multivillous", human): fetal capillaries pass through well-mixed maternal blood at the uterine
#   venous PO2, which is set by mass balance.
# A: umbilical venous PO2 versus diffusing conductance G. B: fetal O2 uptake for HbF and HbA (pool design).
import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import brentq

n_h = 2.7
Qm, Qf = 0.5, 0.35  # L/min
Pma, Pfa = 95.0, 16.0
grid = np.linspace(0.0, 120.0, 4001)


def content(P, hb, p50):
    P = np.maximum(P, 0.0)
    return 1.34 * hb * P**n_h / (p50**n_h + P**n_h) + 0.03 * P


def inverse(hb, p50):
    c = content(grid, hb, p50)
    return lambda C: np.interp(C, c, grid)


MAT = (120.0, 27.0)


def run(design, G, fetal=(170.0, 19.0)):
    Pm_of, Pf_of = inverse(*MAT), inverse(*fetal)
    Cma, Cfa = content(Pma, *MAT), content(Pfa, *fetal)

    def rhs(sign):
        return lambda x, y: [-G * (Pm_of(y[0]) - Pf_of(y[1])) / Qm, sign * G * (Pm_of(y[0]) - Pf_of(y[1])) / Qf]

    if design in ("concurrent", "countercurrent"):
        # N cells in series; each exchanges g (Pm - Pf) with g = G / N; solve by repeated sweeps
        N = 200
        g = G / N
        Cm = np.full(N + 1, Cma)
        Cf = np.full(N + 1, Cfa)
        w = 0.5 if design == "concurrent" else 0.03
        for _ in range(400 if design == "concurrent" else 8000):
            j = g * (Pm_of(Cm[:-1]) - Pf_of(Cf[:-1] if design == "concurrent" else Cf[1:]))
            Cm_new = Cma - np.concatenate([[0.0], np.cumsum(j)]) / Qm
            if design == "concurrent":
                Cf_new = Cfa + np.concatenate([[0.0], np.cumsum(j)]) / Qf
            else:  # fetal blood enters at cell N and flows toward cell 0
                Cf_new = Cfa + np.concatenate([np.cumsum(j[::-1])[::-1], [0.0]]) / Qf
            Cm = (1 - w) * Cm + w * Cm_new
            Cf = (1 - w) * Cf + w * Cf_new
        Cfv = Cf[-1] if design == "concurrent" else Cf[0]
    else:  # pool
        def balance(Pmv):
            Cf = solve_ivp(lambda x, y: [G * (Pmv - Pf_of(y[0])) / Qf], (0, 1), [Cfa], max_step=0.005).y[0, -1]
            return Qm * (Cma - content(Pmv, *MAT)) - Qf * (Cf - Cfa), Cf
        Pmv = brentq(lambda P: balance(P)[0], Pfa, Pma)
        Cfv = balance(Pmv)[1]
    return Pf_of(Cfv), Qf * (Cfv - Cfa)


Gs = np.geomspace(0.3, 6, 24)  # mL O2 / (min mmHg)
fig, (axa, axb) = plt.subplots(1, 2, figsize=(11.5, 4.4))
for design, col, ls, lab in (("countercurrent", "#c0392b", "-", "countercurrent (rabbit, guinea pig)"),
                             ("pool", "#2c6fbb", "-", "multivillous pool (human)"),
                             ("concurrent", "0.45", "--", "concurrent")):
    pv = [run(design, G)[0] for G in Gs]
    axa.semilogx(Gs, pv, color=col, ls=ls, lw=2, label=lab)
axa.axhline(Pfa, color="0.7", lw=0.8, ls=":")
axa.text(0.32, Pfa + 1, "umbilical artery", fontsize=8, color="0.45")
axa.set_xlabel("Placental diffusing conductance G / (mL O$_2$ min$^{-1}$ mmHg$^{-1}$)")
axa.set_ylabel("Umbilical venous PO$_2$ / mmHg")
axa.set_title("A  Flow geometry and fetal PO$_2$", loc="left", fontsize=11, fontweight="bold")
axa.legend(frameon=False, fontsize=8.5, loc="upper left")

for fetal, col, ls, lab in (((170.0, 19.0), "#2c6fbb", "-", "fetal Hb (P50 19 mmHg)"),
                            ((170.0, 27.0), "#2c6fbb", "--", "adult-type Hb (P50 27 mmHg)")):
    vo2 = [run("pool", G, fetal)[1] for G in Gs]
    axb.semilogx(Gs, vo2, color=col, ls=ls, lw=2, label=lab)
axb.axhspan(20, 30, color="0.9", lw=0)
axb.text(0.35, 25, "fetal O$_2$ consumption at term", fontsize=8, color="0.4", va="center")
axb.set_xlabel("Placental diffusing conductance G / (mL O$_2$ min$^{-1}$ mmHg$^{-1}$)")
axb.set_ylabel("Fetal O$_2$ uptake / (mL/min)")
axb.set_title("B  High-affinity fetal Hb (pool design)", loc="left", fontsize=11, fontweight="bold")
axb.legend(frameon=False, fontsize=8.5, loc="upper left")
fig.tight_layout()
