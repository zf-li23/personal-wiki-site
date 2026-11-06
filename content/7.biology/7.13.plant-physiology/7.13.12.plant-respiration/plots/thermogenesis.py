# Thermoregulation of a thermogenic inflorescence (heat-balance model; orders of magnitude as for skunk
# cabbage, Symplocarpus). Heat production H (W) comes from respiration through the alternative pathway and is
# controlled by negative feedback on spadix temperature: H = H0 + k (Tset - T), bounded at zero and Hmax.
# Heat loss is proportional to the spadix-air temperature difference: C dT/dt = H - h A (T - Ta).
# Respiration is converted to O2 uptake with about 470 kJ per mol O2.
import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import solve_ivp

m = 5.0                   # g
C = 3.6 * m               # J/K (heat capacity ~ 3.6 J g^-1 K^-1)
hA = 15.0 * 15e-4         # W/K
Tset, H0, k, Hmax = 20.0, 0.30, 0.20, 0.9
days = 2.0


def Ta(t):
    return 3.0 + 7.0 * np.sin(2 * np.pi * (t / 86400 - 0.375))


def heat(T):
    return np.clip(H0 + k * (Tset - T), 0, Hmax)


def rhs(t, y):
    return [(heat(y[0]) - hA * (y[0] - Ta(t))) / C]


t = np.linspace(0, days * 86400, 2000)
sol = solve_ivp(rhs, (0, t[-1]), [19.0], t_eval=t, max_step=300)
T = sol.y[0]
H = heat(T)
o2 = H / 4.7e5 / m * 1e6   # umol O2 g^-1 s^-1

fig, (a, b) = plt.subplots(2, 1, figsize=(8.6, 5.6), sharex=True)
hours = t / 3600
a.plot(hours, Ta(t), color="0.5", lw=1.8, label="air")
a.plot(hours, T, color="#c0504d", lw=2.4, label="spadix")
a.axhline(0, color="0.7", lw=0.6, ls=":")
a.set_ylabel("Temperature / °C")
a.set_ylim(-8, 26)
a.legend(frameon=False, fontsize=9, loc="center right")
a.set_title("A   Spadix and air temperature", loc="left", fontsize=10)
b.plot(hours, o2, color="#2f6fb5", lw=2.2)
b.set_ylabel("O₂ uptake / (µmol g⁻¹ s⁻¹)")
b.set_xlabel("Time / h")
b.set_xlim(0, days * 24)
b.set_xticks(range(0, 49, 6))
b.set_title("B   Respiration rate (heat production)", loc="left", fontsize=10)
for ax in (a, b):
    ax.spines[["top", "right"]].set_visible(False)
fig.tight_layout()
