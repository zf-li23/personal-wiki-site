"""Body-weight dynamics under a sustained change in energy intake (one-compartment energy-balance model).

rho dW/dt = I - E(W), with tissue energy density rho = 32 MJ/kg (mixture of fat and lean tissue) and
E(W) = E0 + k (W - W0): the expenditure of a heavier body is larger, k = 92 kJ per kg per day (about 22 kcal/kg/d).
Baseline W0 = 90 kg, I = E0 = 12 MJ/d. At t = 0 intake falls by 2.1 MJ/d (500 kcal/d).
Static rule: 2.1 MJ/d / 32 MJ/kg = 66 g/d forever. Dynamic model: exponential approach to W0 - dI/k with time
constant rho/k (about one year). Adaptive thermogenesis: an extra fall of expenditure of 5 % of E0 that develops with
a 30-day time constant (dashed). B: the energy gap I - E closes as the body becomes lighter.
"""
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio

P = bio.P
rho, k, W0, E0, dI = 32.0, 0.092, 90.0, 12.0, -2.1
t = np.linspace(0, 6 * 365, 2000)
dt = t[1] - t[0]


def sim(adapt):
    W = np.empty_like(t)
    gap = np.empty_like(t)
    w = W0
    for i, ti in enumerate(t):
        E = E0 + k * (w - W0) - adapt * E0 * (1 - np.exp(-ti / 30))
        g = (E0 + dI) - E
        W[i], gap[i] = w, g
        w += dt * g / rho
    return W, gap


Wd, gd = sim(0.0)
Wa, ga = sim(0.05)
static = W0 + dI / rho * t

fig, (ax, bx) = plt.subplots(1, 2, figsize=(12.5, 4.4))
yr = t / 365
ax.plot(yr, static, color=P.muted(), lw=1.4, ls=":", label="static rule (constant loss)")
ax.plot(yr, Wd, color=P.edge("dna"), lw=2, label="dynamic model")
ax.plot(yr, Wa, color=P.edge("rna"), lw=1.8, ls="--", label="with adaptive thermogenesis")
ax.axhline(W0 + dI / k, color=P.edge("dna"), lw=0.8, ls="-.")
ax.text(4.2, W0 + dI / k + 0.8, f"new steady state {W0 + dI / k:.0f} kg", fontsize=8, color=P.edge("dna"))
ax.set_ylim(40, 92)
ax.set_xlabel("Time / years")
ax.set_ylabel("Body mass / kg")
ax.legend(frameon=False, fontsize=8, loc="lower left")
ax.set_title(f"A  Intake cut by 2.1 MJ/d (time constant {rho / k / 365:.1f} yr)", loc="left", fontsize=10)

bx.plot(yr, gd, color=P.edge("dna"), lw=2, label="dynamic model")
bx.plot(yr, ga, color=P.edge("rna"), lw=1.8, ls="--", label="with adaptive thermogenesis")
bx.axhline(0, color=P.muted(), lw=0.8)
bx.set_xlabel("Time / years")
bx.set_ylabel("Energy balance $I - E$ / MJ d$^{-1}$")
bx.legend(frameon=False, fontsize=8, loc="lower right")
bx.set_title("B  The deficit closes as the body becomes lighter", loc="left", fontsize=10)
fig.tight_layout()
