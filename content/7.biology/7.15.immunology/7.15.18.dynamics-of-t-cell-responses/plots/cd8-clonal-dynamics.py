# Programmed expansion, contraction and memory of a CD8 T-cell response (illustrative cohort model).
# Activated cells pass through G = 14 divisions (mean inter-division time 7 h, rate r = 24/7 per day) after a
# lag of 1 day; division stops when antigen is cleared (day 9) and is damped by a ceiling K = 1e7 cells
# (competition for antigen presenting cells and IL-2): rate r (1 - N/K). Cells leaving the division program become
# memory cells with probability phi = 0.08 (death rate 0.01 per day), otherwise effector cells (death rate
# 0.02 per day during the response, 0.5 per day after antigen is cleared). The secondary response is started
# from the memory pool left by the primary one with a shorter lag (0.4 day), fewer divisions (6) and faster
# antigen clearance (day 5).
#   dA_0/dt = -r s A_0,  dA_g/dt = 2 r s A_{g-1} - r s A_g,
#   dE/dt = (1 - phi) 2 r s A_{G-1} - delta_E E,  dM/dt = phi 2 r s A_{G-1} - delta_M M,
#   s = max(0, 1 - N/K) while antigen is present (lag < t < t_clear), else 0.
import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import solve_ivp

import wikibio as bio
from wikibio import charts

P = bio.P
R = 24 / 7.0
K = 1e7
PHI = 0.08
DE, DE0, DM = 0.5, 0.02, 0.01


def run(a0, lag, tmax, ngen=14, t_clear=9.0):
    n = ngen + 2

    def f(t, y):
        A, E, M = y[:ngen], y[ngen], y[ngen + 1]
        N = A.sum() + E + M
        s = max(0.0, 1 - N / K) if lag <= t < t_clear else 0.0
        de = DE if t > t_clear else DE0
        div = R * s * A
        d = np.zeros(n)
        d[:ngen] -= div + de * A * (t > t_clear)
        d[1:ngen] += 2 * div[:-1]
        fin = 2 * div[-1]
        d[ngen] = (1 - PHI) * fin - de * E
        d[ngen + 1] = PHI * fin - DM * M
        return d

    y0 = np.zeros(n)
    y0[0] = a0
    ts = np.linspace(0, tmax, 900)
    sol = solve_ivp(f, (0, tmax), y0, t_eval=ts, rtol=1e-8, atol=1e-6, method="LSODA")
    A, E, M = sol.y[:ngen].sum(0), sol.y[ngen], sol.y[ngen + 1]
    return ts, A + E + M, M


fig, axs = plt.subplots(1, 2, figsize=(10, 3.6))
for f0, tok in ((1e2, "enzyme"), (1e3, "protein"), (1e4, "negative")):
    t, N, M = run(f0, 1.0, 45)
    axs[0].plot(t, N, color=charts.line(tok), lw=1.5, label=f"$10^{{{int(round(np.log10(f0)))}}}$ naive precursors")
    axs[0].plot(t, M, color=charts.line(tok), lw=0.9, ls="--")
axs[0].axhline(K, color=P.muted(), lw=0.7, ls=":")
axs[0].text(44, K * 1.25, "ceiling K", fontsize=7, color=P.muted(), ha="right")
axs[0].set_yscale("log")
axs[0].set_ylim(10, 5e7)
axs[0].legend(frameon=False, fontsize=7, labelcolor=P.ink(), loc="lower right")
charts.style_axes(axs[0], "time after infection / days", "antigen-specific cells (dashed: memory)")
charts.title(axs[0], "A")

t1, N1, M1 = run(1e3, 1.0, 60)
mem = M1[-1]
t2, N2, M2 = run(mem, 0.4, 14, ngen=6, t_clear=5.0)
t1b, N1b, _ = run(1e3, 1.0, 14)
axs[1].plot(t1b, N1b, color=charts.line("protein"), lw=1.5, label="primary (1000 naive cells)")
axs[1].plot(t2, N2, color=charts.line("negative"), lw=1.5, label=f"secondary ($3.9\\times10^5$ memory cells)")
axs[1].axhline(K, color=P.muted(), lw=0.7, ls=":")
axs[1].set_yscale("log")
axs[1].set_ylim(10, 5e7)
axs[1].legend(frameon=False, fontsize=7, labelcolor=P.ink(), loc="lower right")
charts.style_axes(axs[1], "time after (re)infection / days", "antigen-specific cells")
charts.title(axs[1], "B")
fig.tight_layout()
