# Two-time-scale model of calcium homeostasis (time in hours; amounts in mmol).
#   dM/dt = a(D) I - E + O Jr - Jf - U(c, P) + kx (cB - c)       ECF calcium, c = M / V (total plasma Ca)
#   dB/dt = -kx (cB - c)                                          exchangeable bone pool
#   cB = c0 (B / B0) (1 + alpha (P - 1))                          pool equilibrium concentration
#   dP/dt = (Pinf(c) - P) / tauP      inverse sigmoid PTH secretion (relative, 1 = normal)
#   dD/dt = (P - D) / tauD            1,25-dihydroxyvitamin D follows PTH (or is fixed: CKD-like)
#   dO/dt = (P^0.8 D^0.3 - O) / tauO  osteoclast activity
# Parameters are illustrative: V 14 L, c0 2.4 mmol/L, B0 180 mmol, 1/kx = 45 min, tauP 6 min,
# tauD 12 h, tauO 3 days, bone resorption = formation = 12 mmol/day, diet 25 mmol/day, net gut absorption 3.75.
import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import solve_ivp

V, c0, B0 = 14.0, 2.4, 180.0
kx = V / 0.75
tauP, tauD, tauO = 0.1, 12.0, 72.0
Jr = Jf = 12.0 / 24
E = 2.5 / 24
alpha = 0.15


def a_frac(D):
    return 0.6 * D / (D + 1.4)  # 0.25 at D = 1


def Pinf(c):
    return 0.1 + 1.8 / (1.0 + (c / c0) ** 30)


U0 = a_frac(1.0) * 25.0 / 24 - E  # urinary Ca at steady state (mmol/h)


def make_rhs(diet, pth_clamp=False, pool=True, vitd_fixed=False):
    def rhs(t, y):
        M, B, P, D, O = y
        c = M / V
        I = diet(t) / 24.0
        cB = c0 * (B / B0) * (1.0 + alpha * (P - 1.0))
        Jx = kx * (cB - c) if pool else 0.0
        U = U0 * (c / c0) ** 4 / P**0.7
        dM = a_frac(D) * I - E + O * Jr - Jf - U + Jx
        dP = 0.0 if pth_clamp else (Pinf(c) - P) / tauP
        dD = 0.0 if vitd_fixed else (P - D) / tauD
        dO = (P**0.8 * D**0.3 - O) / tauO
        return [dM, -Jx, dP, dD, dO]

    return rhs


y_ss = [c0 * V, B0, 1.0, 1.0, 1.0]
fig = plt.figure(figsize=(13.5, 4.6))
axa = fig.add_subplot(1, 3, 1)
axb = fig.add_subplot(1, 3, 2)
axc = fig.add_subplot(2, 3, 3)
axd = fig.add_subplot(2, 3, 6, sharex=axc)

# A: rapid removal of 7 mmol from the ECF at t = 0
y0 = list(y_ss)
y0[0] -= 7.0
t = np.linspace(0, 6, 600)
for kw, col, ls, lab in ((dict(), "#2c6fbb", "-", "intact"),
                         (dict(pth_clamp=True), "#2e8b57", "-", "PTH clamped at basal"),
                         (dict(pth_clamp=True, pool=False), "#c0392b", "--", "PTH clamped, no bone pool")):
    sol = solve_ivp(make_rhs(lambda t: 25.0, **kw), (0, 6), y0, t_eval=t, max_step=0.01)
    axa.plot(t * 60, sol.y[0] / V, color=col, ls=ls, lw=2, label=lab)
axa.axhline(c0, color="0.6", lw=0.8, ls=":")
axa.set_xlabel("Time after removal of 7 mmol Ca / min")
axa.set_ylabel("Plasma total Ca / (mmol/L)")
axa.set_title("A  Minutes to hours", loc="left", fontsize=11, fontweight="bold")
axa.legend(frameon=False, fontsize=8.5, loc="center right")

# B, C: diet 25 -> 5 mmol/day from day 2
diet = lambda t: 25.0 if t < 48.0 else 5.0
T = 40 * 24.0
t = np.linspace(0, T, 4001)
for kw, col, lab in ((dict(), "#2c6fbb", "normal kidney"), (dict(vitd_fixed=True), "0.5", "1,25(OH)$_2$D cannot rise")):
    sol = solve_ivp(make_rhs(diet, **kw), (0, T), y_ss, t_eval=t, max_step=0.5)
    M, B, P, D, O = sol.y
    d = t / 24
    axb.plot(d, P, color=col, lw=2, label=f"PTH, {lab}")
    if not kw:
        axb.plot(d, D, color=col, lw=1.6, ls="--", label="1,25(OH)$_2$D")
        axb.plot(d, a_frac(D) / a_frac(1.0), color=col, lw=1.4, ls=":", label="gut absorption fraction")
    axc.plot(d, M / V, color=col, lw=2)
    net_bone = np.cumsum((O - 1.0) * Jr) * (t[1] - t[0])  # extra resorption, mmol
    axd.plot(d, net_bone * 40.0 / 1000.0, color=col, lw=2)
axb.axvline(2, color="0.7", lw=0.8, ls=":")
axb.set_xlabel("Time / day (diet Ca 25 -> 5 mmol/day at day 2)")
axb.set_ylabel("Relative level (normal = 1)")
axb.set_title("B  Days: hormones", loc="left", fontsize=11, fontweight="bold")
axb.legend(frameon=False, fontsize=8, loc="center right")
axc.set_ylabel("Plasma Ca\n/ (mmol/L)")
axc.set_ylim(2.3, 2.42)
axc.set_title("C  Plasma Ca and bone loss", loc="left", fontsize=11, fontweight="bold")
plt.setp(axc.get_xticklabels(), visible=False)
axd.set_ylabel("Cumulative extra\nbone Ca loss / g")
axd.set_xlabel("Time / day")
fig.tight_layout()
