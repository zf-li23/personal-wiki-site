# Two-pool model of NEP during stand development after a stand-replacing disturbance (Proposition 42.1.1).
# dB/dt = NPP(t) - m B ; dD/dt = m B - k D ; R_H = k D ; NEP = NPP - R_H.
# NPP(t) = 1000 (1 - exp(-t/10)) (0.65 + 0.35 exp(-t/60)) g C m^-2 yr^-1; m = 0.03, k = 0.05 yr^-1;
# B(0) = 50, D(0) = 8000 g C m^-2 (dead wood and soil carbon left by the disturbance).
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
import wikibio as bio

P = bio.P
m, k = 0.03, 0.05


def npp(t):
    return 1000 * (1 - np.exp(-t / 10)) * (0.65 + 0.35 * np.exp(-t / 60))


def rhs(t, y):
    B, D = y
    return [npp(t) - m * B, m * B - k * D]


t = np.linspace(0, 300, 1201)
sol = solve_ivp(rhs, (0, 300), [50, 8000], t_eval=t, rtol=1e-8)
B, D = sol.y
RH = k * D
NEP = npp(t) - RH

fig, (a, b) = plt.subplots(1, 2, figsize=(10.6, 4.3))
a.axhline(0, color=P.muted(), lw=0.8)
a.plot(t, npp(t), color=P.edge("plant"), lw=2, label="NPP")
a.plot(t, RH, color=P.edge("animal"), lw=2, label="heterotrophic respiration $R_H$")
a.plot(t, NEP, color=P.ink(), lw=2.2, label="NEP = NPP − $R_H$")
a.fill_between(t, NEP, 0, where=NEP < 0, color=P.fill("negative"), alpha=0.5, lw=0)
a.fill_between(t, NEP, 0, where=NEP >= 0, color=P.fill("positive"), alpha=0.5, lw=0)
i0 = np.argmax(NEP > 0)
a.annotate(f"source until year {t[i0]:.0f}", (t[i0], 0), xytext=(40, -300), fontsize=8, color=P.ink(),
           arrowprops=dict(arrowstyle="-", color=P.muted(), lw=0.8))
a.set_xlabel("Years since disturbance")
a.set_ylabel("Flux / g C m⁻² yr⁻¹")
a.set_xlim(0, 300)
a.legend(frameon=False, fontsize=8)
a.set_title("A  Fluxes", loc="left", fontweight="bold")

b.plot(t, B / 1000, color=P.edge("plant"), lw=2, label="living biomass $B$")
b.plot(t, D / 1000, color=P.edge("animal"), lw=2, label="dead organic matter $D$")
b.plot(t, (B + D) / 1000, color=P.ink(), lw=1.6, ls="--", label="total $B + D$")
Ns = npp(1e9)
b.axhline(Ns / m / 1000, color=P.edge("plant"), lw=0.8, ls=":")
b.axhline(Ns / k / 1000, color=P.edge("animal"), lw=0.8, ls=":")
b.set_xlabel("Years since disturbance")
b.set_ylabel("Carbon stock / kg C m⁻²")
b.set_xlim(0, 300)
b.legend(frameon=False, fontsize=8, loc="lower right")
b.set_title("B  Pools (dotted: equilibria N*/m, N*/k)", loc="left", fontweight="bold")
for ax in (a, b):
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
fig.tight_layout()
