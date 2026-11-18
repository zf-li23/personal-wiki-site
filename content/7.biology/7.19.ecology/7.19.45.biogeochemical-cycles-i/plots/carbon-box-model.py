# Four-box linear model of the anthropogenic carbon perturbation (atmosphere, surface ocean,
# deep ocean, land biosphere), in Pg C of excess carbon relative to the preindustrial state.
# A: response of the atmosphere to a unit pulse, compared with the multimodel fit of Joos et al. (2013).
# B: atmospheric CO2 for a stylized emission history and three future pathways.
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
from scipy.linalg import expm
import wikibio as bio

P = bio.P
a0, m0, d0 = 590.0, 900.0, 37000.0       # preindustrial pools (Pg C)
R = 13.0                                   # Revelle (buffer) factor
alpha = R * a0 / m0                        # air-sea equilibrium: a = alpha * m
beta = m0 / d0                             # surface-deep equilibrium: m = beta * d
k = 1.0 / (1.0 + alpha)                    # air-sea exchange: equilibration time about 1 yr
q = 0.07                                   # surface-deep exchange (1/yr)
c, tau = 0.03, 20.0                        # land uptake per Pg C of excess CO2, land turnover time (yr)
A = np.array([[-k - c, k * alpha, 0.0, 1.0 / tau],
              [k, -k * alpha - q, q * beta, 0.0],
              [0.0, q, -q * beta, 0.0],
              [c, 0.0, 0.0, -1.0 / tau]])
f_inf = 1.0 / (1.0 + 1.0 / alpha + 1.0 / (alpha * beta) + c * tau)

fig, (a, b) = plt.subplots(1, 2, figsize=(10.8, 4.3))

t = np.logspace(-1, np.log10(3000), 300)
pulse = np.array([expm(A * s)[:, 0] for s in t])
joos = 0.2173 + 0.2240 * np.exp(-t / 394.4) + 0.2824 * np.exp(-t / 36.54) + 0.2763 * np.exp(-t / 4.304)
a.plot(t, pulse[:, 0], color=P.ink(), lw=2, label="atmosphere (box model)")
a.plot(t, pulse[:, 1] + pulse[:, 2], color=P.fill("dna"), lw=1.6, label="ocean")
a.plot(t, pulse[:, 3], color=P.fill("plant"), lw=1.6, label="land")
a.plot(t, joos, color=P.fill("negative"), lw=1.4, ls="--", label="atmosphere (Joos et al. 2013)")
a.axhline(f_inf, color=P.muted(), lw=0.8, ls=":")
a.text(1.2, f_inf + 0.02, f"equilibrium airborne fraction {f_inf:.2f}", fontsize=7.5, color=P.muted())
a.set_xscale("log")
a.set_xlim(0.1, 3000)
a.set_ylim(0, 1.02)
a.set_xlabel("Years after the pulse")
a.set_ylabel("Fraction of the pulse")
a.legend(frameon=False, fontsize=7.5, loc="center left")
a.set_title("A  Response to a pulse of CO$_2$", loc="left", fontweight="bold")

def emis(y, path):
    if y <= 2023:
        return 11.0 * np.exp((y - 2023) / 60.0)
    if path == 0:
        return 11.0
    if path == 1:
        return max(0.0, 11.0 * (1 - (y - 2023) / 37.0))
    return 11.0 * (1 - (y - 2023) / 27.0) if y < 2050 else -1.0

years = np.linspace(1850, 2200, 1401)
styles = [("emissions constant", "negative", "-"), ("net zero by 2060", "highlight", "-"),
          ("net zero by 2050, then removal", "dna", "-")]
for i, (lab, tok, ls) in enumerate(styles):
    sol = solve_ivp(lambda s, x: A @ x + np.array([emis(s, i), 0, 0, 0]), (1850, 2200), np.zeros(4),
                    t_eval=years, max_step=0.5)
    b.plot(years, 280 + sol.y[0] / 2.124, color=P.fill(tok) if tok != "highlight" else P.edge(tok), lw=1.8,
           ls=ls, label=lab)
b.axvline(2023, color=P.muted(), lw=0.8, ls=":")
b.text(2027, 300, "2023", fontsize=7.5, color=P.muted())
b.set_xlim(1850, 2200)
b.set_ylim(260, 900)
b.set_xlabel("Year")
b.set_ylabel("Atmospheric CO$_2$ / ppm")
b.legend(frameon=False, fontsize=7.5, loc="upper left")
b.set_title("B  Emission pathways", loc="left", fontweight="bold")
for ax in (a, b):
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
fig.tight_layout()
