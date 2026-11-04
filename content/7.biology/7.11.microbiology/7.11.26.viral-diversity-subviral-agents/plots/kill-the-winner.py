# Viral control of a microbial community, simulated in a chemostat.
# A: kill the winner. Two bacterial populations compete for one nutrient; population 1 is the better
#    competitor (lower R*) and excludes population 2 when viruses are absent (dotted). With a
#    host-specific lytic virus on each, both persist: each host is held near (D + m)/((beta - 1)phi),
#    which is independent of its competitive ability.
# B: the same model run to steady state over a range of nutrient supply. Host density is pinned by the
#    viruses and hardly changes; the extra production goes into virions, so the virus-to-cell ratio
#    rises with productivity. This is the prediction of a purely lytic model; the fall of the ratio
#    measured in highly productive habitats (piggyback the winner) requires lysogeny.
#
# State: S nutrient (ug/ml), N hosts (1e6 cells/ml), V virions (1e6/ml). Virions decay at rate m.
import numpy as np
from scipy.integrate import solve_ivp

import wikibio as bio
from wikibio import quant

P = bio.P
fig, ax = bio.canvas(17, 7.4)

D, Y = 0.2, 1.0          # dilution rate (per h), yield (1e6 cells per ug nutrient)
BETA, PHI, MDEC = 30.0, 0.02, 0.3   # burst size, adsorption (ml per 1e6 virions per h), virion decay
MU = (1.0, 0.6)          # maximum growth rates
KS = (0.10, 0.25)        # half-saturation constants: population 1 is the better competitor


def two_hosts(t, y, with_virus, S0=6.0):
    S, N1, N2, V1, V2 = y
    mu = [MU[i] * S / (KS[i] + S) for i in range(2)]
    N = [N1, N2]
    V = [V1, V2] if with_virus else [0.0, 0.0]
    dS = D * (S0 - S) - sum(mu[i] * N[i] for i in range(2)) / Y
    dN = [mu[i] * N[i] - PHI * N[i] * V[i] - D * N[i] for i in range(2)]
    dV = [(BETA - 1) * PHI * N[i] * V[i] - (D + MDEC) * V[i] if with_virus else 0.0 for i in range(2)]
    return [dS, dN[0], dN[1], dV[0], dV[1]]


# --- A  kill the winner -----------------------------------------------------------------------------
bio.panel(ax, "A", (0.1, 7.2))
bio.label(ax, (4.6, 7.05), "Kill the winner", size="title", bold=True)

t_end = 250.0
t_eval = np.linspace(0, t_end, 2000)
y0 = [6.0, 0.05, 0.05, 0.02, 0.02]
sol_v = solve_ivp(two_hosts, (0, t_end), y0, args=(True,), t_eval=t_eval, method="LSODA",
                  rtol=1e-7, atol=1e-10)
sol_0 = solve_ivp(two_hosts, (0, t_end), y0, args=(False,), t_eval=t_eval, method="LSODA",
                  rtol=1e-7, atol=1e-10)

pl = quant.Plot(ax, (1.5, 1.65, 6.2, 4.7), xlim=(0, t_end), ylim=(-2.6, 2.0),
                xlabel="time / h", ylabel="$\\log_{10}$ (abundance / $10^6$ ml$^{-1}$)",
                xticks=[0, 50, 100, 150, 200, 250], yticks=[-2, -1, 0, 1, 2])


def lg(v):
    return np.log10(np.maximum(v, 1e-6))


pl.line(sol_v.t, lg(sol_v.y[1]), "bacterium", text="host 1 (better competitor)", at=0.52, dy=0.32)
pl.line(sol_v.t, lg(sol_v.y[2]), "enzyme", text="host 2", at=0.72, dy=-0.36)
pl.line(sol_v.t, lg(sol_v.y[3]), "virus", dashed=True, text="virus 1", at=0.74, dy=0.30)
pl.line(sol_v.t, lg(sol_v.y[4]), "negative", dashed=True, text="virus 2", at=0.90, dy=0.30)
pl.line(sol_0.t, lg(sol_0.y[1]), "muted", dotted=True, text="no viruses: host 1 alone", at=0.62, dy=-0.40)
pl.line(sol_0.t, lg(sol_0.y[2]), "muted", dotted=True, text="no viruses: host 2 excluded",
        at=0.14, dy=-0.45)
bio.label(ax, (4.6, 0.45),
          "each host is pinned at $N^* = (D + m)/[(\\beta - 1)\\varphi]$, not at its competitive optimum",
          size="tiny", color=P.muted())

# --- B  nutrient supply, host density and the virus-to-cell ratio -----------------------------------
bio.panel(ax, "B", (8.95, 6.9))
bio.label(ax, (13.2, 7.05), "Productivity and the virus-to-cell ratio", size="title", bold=True)

S0s = np.logspace(np.log10(1.5), np.log10(120), 18)
hosts, viruses = [], []
tt = np.linspace(1500, 3000, 600)        # average over the last half: some runs settle on a limit cycle
for S0 in S0s:
    r = solve_ivp(two_hosts, (0, 3000), [S0, 0.05, 0.05, 0.02, 0.02], args=(True, S0),
                  method="LSODA", t_eval=tt, rtol=1e-8, atol=1e-11)
    _, N1, N2, V1, V2 = (np.maximum(v, 0.0).mean() for v in r.y)
    hosts.append(N1 + N2)
    viruses.append(V1 + V2)
hosts, viruses = np.array(hosts), np.array(viruses)

pl2 = quant.Plot(ax, (10.6, 1.65, 5.3, 4.7), xlim=(0, 2.1), ylim=(-0.6, 2.4),
                 xlabel="$\\log_{10}$ (nutrient supply / $\\mu$g ml$^{-1}$)",
                 ylabel="$\\log_{10}$ (abundance, or ratio)",
                 xticks=[0, 1, 2], yticks=[0, 1, 2])
x = np.log10(S0s)
pl2.line(x, np.log10(hosts), "bacterium", text="hosts (both populations)", at=0.45, dy=-0.38)
pl2.line(x, np.log10(viruses), "virus", text="virions", at=0.45, dy=0.32)
pl2.line(x, np.log10(viruses / hosts), "negative", dashed=True, text="virus : cell ratio", at=0.62, dy=0.32)
bio.label(ax, (13.2, 0.42),
          "a lytic model predicts a ratio that rises with productivity; the opposite trend seen in\n"
          "productive habitats is the piggyback-the-winner pattern and requires lysogeny",
          size="tiny", color=P.muted())
