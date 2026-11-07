# Positive feedback in labour (Ferguson reflex), an illustrative model (time in hours):
#   dO/dt = (Ob + alpha S - O) / tauO               plasma oxytocin; cervical stretch S drives its release
#   dU/dt = (R O^n / (K^n + O^n) - U) / tauU        uterine contractile activity; R = oxytocin receptor density
#   dS/dt = (beta U - S) / tauS                     stretch of the cervix by the descending fetus
# Half-life of oxytocin about 4 min (tauO = 0.07 h). With a sigmoid response the loop is bistable:
# a quiescent state and an active (labour) state. As R rises at the end of pregnancy the quiescent
# state disappears (saddle-node) and contractions escalate by themselves. Delivery removes the stretch.
import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import brentq

Ob, alpha, n, K, beta = 0.3, 3.0, 4, 1.0, 1.0
tauO, tauU, tauS = 0.07, 0.15, 0.3


def rhs_factory(R_of_t, deliver_at=None):
    def rhs(t, y):
        O, U, S = y
        b = 0.0 if (deliver_at is not None and t >= deliver_at) else beta
        R = R_of_t(t)
        return [(Ob + alpha * S - O) / tauO, (R * O**n / (K**n + O**n) - U) / tauU, (b * U - S) / tauS]

    return rhs


fig, (axa, axb) = plt.subplots(1, 2, figsize=(11.5, 4.4))

# A: receptor density rises slowly from 0.6 to 1.6 over 40 h; delivery 6 h after the switch
R_ramp = lambda t: 0.6 + 1.0 * min(t / 40.0, 1.0)
t = np.linspace(0, 48, 4801)
sol = solve_ivp(rhs_factory(R_ramp), (0, 48), [Ob, 0.0, 0.0], t_eval=t, max_step=0.01)
U = sol.y[1]
t_on = t[np.argmax(U > 0.3)]
sol2 = solve_ivp(rhs_factory(R_ramp, deliver_at=t_on + 6.0), (0, 48), [Ob, 0.0, 0.0], t_eval=t, max_step=0.01)
axa.plot(t, sol2.y[1] / sol2.y[1].max(), color="#c0392b", lw=2, label="uterine activity U (scaled)")
axa.plot(t, sol2.y[0] / sol2.y[0].max(), color="#2c6fbb", lw=1.6, ls="--", label="oxytocin (scaled)")
axa.plot(t, [R_ramp(x) / 1.6 for x in t], color="0.5", lw=1.2, ls=":", label="receptor density R (scaled)")
axa.axvline(t_on + 6.0, color="0.7", lw=0.8)
axa.text(t_on + 6.3, 0.5, "delivery", fontsize=8.5, color="0.4")
axa.set_xlabel("Time / h")
axa.set_ylabel("Relative level")
axa.set_ylim(0, 1.1)
axa.set_title("A  Rising receptors trigger an explosive switch", loc="left", fontsize=11, fontweight="bold")
axa.legend(frameon=False, fontsize=8.5, loc="center left")

# B: steady states of U versus R (the loop closes through S = beta U, O = Ob + alpha S)
def f(U, R):
    O = Ob + alpha * beta * U
    return R * O**n / (K**n + O**n) - U


Rs = np.linspace(0.3, 1.6, 400)
stable_lo, stable_hi, unstable = [], [], []
for R in Rs:
    grid = np.linspace(0, 2, 2001)
    v = f(grid, R)
    roots = [brentq(f, grid[i], grid[i + 1], args=(R,)) for i in range(len(grid) - 1) if v[i] * v[i + 1] < 0]
    for r in roots:
        slope = (f(r + 1e-5, R) - f(r - 1e-5, R)) / 2e-5
        (stable_lo if (slope < 0 and r < 0.05) else stable_hi if slope < 0 else unstable).append((R, r))
for pts, col, ls, lab in ((stable_lo, "#2c6fbb", "-", "quiescent (stable)"),
                          (stable_hi, "#c0392b", "-", "labour (stable)"),
                          (unstable, "0.5", "--", "threshold (unstable)")):
    if pts:
        a = np.array(pts)
        axb.plot(a[:, 0], a[:, 1], ls, color=col, lw=2, label=lab)
axb.set_xlabel("Oxytocin receptor density R (relative)")
axb.set_ylabel("Steady uterine activity U")
axb.set_title("B  Bistability of the Ferguson loop", loc="left", fontsize=11, fontweight="bold")
axb.legend(frameon=False, fontsize=8.5, loc="upper left")
fig.tight_layout()
