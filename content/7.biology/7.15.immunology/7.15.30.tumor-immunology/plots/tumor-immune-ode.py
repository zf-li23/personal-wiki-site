# Tumor-effector competition model (Kuznetsov-type predator-prey with effector inactivation; illustrative parameters).
#   dT/dt = a T (1 - b T) - n E T                              T: tumor cells, E: effector (cytotoxic) cells
#   dE/dt = s + p E T / (g + T) - m E T - d E
# s: constant influx of effectors, p: antigen-driven recruitment (saturating in T), m: inactivation of effectors by contact
# with tumor cells (a proxy of exhaustion and checkpoint-mediated inhibition), d: effector loss, n: killing rate.
# A: tumors that start small settle at an immune-controlled equilibrium after damped oscillations (immunoediting's
#    equilibrium phase); a large initial tumor overwhelms the effectors and escapes to the carrying capacity 1/b.
# B: an escaped tumor (T0 = 1e8) at day 50 receives a "checkpoint blockade": inactivation m is reduced by a factor 0.3
#    or 0.1; the system switches from the escape branch to the controlled branch.
import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import solve_ivp

import wikibio as bio
from wikibio import charts

P = bio.P
s, p, g, m0, d, a, b, n = 1.3e4, 0.1245, 2.019e7, 3.422e-10, 0.0412, 0.18, 2e-9, 1.101e-7


def run(T0, tb=1e9, fm=1.0, tend=400):
    def f(t, y):
        m = m0 * (fm if t >= tb else 1.0)
        T, E = y
        return [a * T * (1 - b * T) - n * E * T, s + p * E * T / (g + T) - m * E * T - d * E]

    return solve_ivp(f, (0, tend), [T0, s / d], method="LSODA", rtol=1e-8, atol=1e-3, max_step=0.5, dense_output=True)


t = np.linspace(0, 400, 800)
fig, axs = plt.subplots(1, 2, figsize=(9.5, 3.6))
for T0, tok in ((1e3, "protein"), (1e5, "enzyme"), (1e7, "highlight"), (1e8, "negative")):
    sol = run(T0)
    axs[0].plot(t, np.maximum(sol.sol(t)[0], 1), color=charts.line(tok), lw=1.5, label=f"T0 = {T0:.0e}")
axs[0].axhline(1 / b, color=P.muted(), lw=0.7, ls=":")
axs[0].text(5, 1 / b * 1.25, "carrying capacity 1/b", fontsize=6.5, color=P.muted())
axs[0].set_yscale("log")
axs[0].set_ylim(1e2, 2e9)
axs[0].legend(frameon=False, fontsize=6.5, labelcolor=P.ink(), loc="lower right")
charts.style_axes(axs[0], "time (days)", "tumor cells")
charts.title(axs[0], "A")

for fm, tok, lab in ((1.0, "negative", "no treatment"), (0.3, "enzyme", "m x 0.3 from day 50"), (0.1, "protein", "m x 0.1 from day 50")):
    sol = run(1e8, tb=50, fm=fm)
    axs[1].plot(t, np.maximum(sol.sol(t)[0], 1), color=charts.line(tok), lw=1.5, label=lab)
axs[1].axvline(50, color=P.muted(), lw=0.7, ls=":")
axs[1].set_yscale("log")
axs[1].set_ylim(1e2, 2e9)
axs[1].legend(frameon=False, fontsize=6.5, labelcolor=P.ink(), loc="lower right")
charts.style_axes(axs[1], "time (days)", "tumor cells")
charts.title(axs[1], "B")
fig.tight_layout()
