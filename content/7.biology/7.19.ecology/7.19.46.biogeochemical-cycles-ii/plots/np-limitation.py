# Stoichiometric coupling of nitrogen and phosphorus.
# A: growth of a phytoplankton population (relative to its maximum) as a function of nitrate and phosphate
#    under Liebig's law of the minimum (solid contours) and under multiplicative co-limitation (dashed);
#    half-saturation constants 1 umol N/L and 1/16 umol P/L, so that the corner lies on the Redfield line.
# B: a surface-ocean model after Tyrrell (1999): ordinary phytoplankton O (need N and P) and nitrogen
#    fixers F (need only P, grow more slowly) take up nutrients supplied by mixing from deep water whose
#    N:P (12) is below Redfield because of denitrification; remineralization returns N:P = 16.
#    Fixers make up the nitrogen deficit and hold the surface N:P supply close to, but below, 16.
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
import wikibio as bio

P = bio.P
fig, (a, b) = plt.subplots(1, 2, figsize=(10.8, 4.3))
n = np.linspace(0.01, 6, 300)
p = np.linspace(0.001, 6 / 16, 300)
Nn, Pp = np.meshgrid(n, p)
gN, gP = Nn / (Nn + 1), Pp / (Pp + 1 / 16)
lev = [0.2, 0.4, 0.6, 0.8]
cs1 = a.contour(Nn, Pp, np.minimum(gN, gP), levels=lev, colors=[P.ink()], linewidths=1.6)
cs2 = a.contour(Nn, Pp, gN * gP, levels=lev, colors=[P.fill("dna")], linewidths=1.4, linestyles="--")
a.clabel(cs1, fontsize=7, fmt="%.1f")
a.plot(n, n / 16, color=P.edge("negative"), lw=1.2, ls=":")
a.text(4.6, 4.6 / 16 + 0.012, "N:P = 16", fontsize=7.5, color=P.edge("negative"), rotation=28)
a.text(0.3, 0.27, "N-limited", fontsize=8, color=P.ink())
a.text(4.4, 0.03, "P-limited", fontsize=8, color=P.ink())
a.plot([], [], color=P.ink(), lw=1.6, label="law of the minimum")
a.plot([], [], color=P.fill("dna"), lw=1.4, ls="--", label="multiplicative")
a.legend(frameon=False, fontsize=7.5, loc="upper right")
a.set_xlabel("Nitrate / µmol L$^{-1}$")
a.set_ylabel("Phosphate / µmol L$^{-1}$")
a.set_title("A  Single and co-limitation", loc="left", fontweight="bold")

mu_o, mu_f, m = 1.0, 0.5, 0.25          # max growth (1/d), mortality and remineralization (1/d)
kn, kp, s = 0.5, 0.03, 0.02             # half saturation (umol/L), mixing (1/d)
Nd, Pd = 12 * 2.0, 2.0                  # deep nitrate and phosphate (N:P = 12)
def rhs(t, y):
    N, Ph, O, F = np.maximum(y, 0)
    go = mu_o * min(N / (N + kn), Ph / (Ph + kp))
    gf = mu_f * Ph / (Ph + kp)
    upP = go * O + gf * F                # phosphorus units
    rem = m * (O + F)
    return [s * (Nd - N) - 16 * go * O + 16 * rem, s * (Pd - Ph) - upP + rem,
            (go - m - s) * O, (gf - m - s) * F]
sol = solve_ivp(rhs, (0, 400), [Nd, Pd, 0.05, 0.01], max_step=0.5, dense_output=True, method="LSODA")
t = np.linspace(0, 400, 1200)
N, Ph, O, F = sol.sol(t)
ratio = (N + 16 * (O + F)) / (Ph + O + F)        # total N : total P in surface water
b.plot(t, ratio, color=P.ink(), lw=2, label="surface total N:P, with fixers")
sol0 = solve_ivp(rhs, (0, 400), [Nd, Pd, 0.05, 0.0], max_step=0.5, dense_output=True, method="LSODA")
N0, Ph0, O0, F0 = sol0.sol(t)
b.plot(t, (N0 + 16 * O0) / (Ph0 + O0), color=P.muted(), lw=1.6, ls="-.", label="without fixers")
b.axhline(16, color=P.edge("negative"), lw=1, ls=":")
b.axhline(12, color=P.muted(), lw=1, ls="--")
b.text(395, 16.25, "Redfield 16", ha="right", fontsize=7.5, color=P.edge("negative"))
b.text(395, 12.25, "deep water 12", ha="right", fontsize=7.5, color=P.muted())
b.set_ylim(10, 18)
b.set_xlabel("Days")
b.set_ylabel("N:P (molar)")
b2 = b.twinx()
b2.plot(t, F / (O + F), color=P.fill("chloroplast"), lw=1.8, label="share of N fixers")
b2.set_ylim(0, 1)
b2.set_ylabel("Share of N fixers in biomass")
h1, l1 = b.get_legend_handles_labels()
h2, l2 = b2.get_legend_handles_labels()
b.legend(h1 + h2, l1 + l2, frameon=False, fontsize=7.5, loc="lower right")
b.set_title("B  Nitrogen fixers restore N:P", loc="left", fontweight="bold")
for ax in (a, b, b2):
    ax.spines["top"].set_visible(False)
a.spines["right"].set_visible(False)
fig.tight_layout()
