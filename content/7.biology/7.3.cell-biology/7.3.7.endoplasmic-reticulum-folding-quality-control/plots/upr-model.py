# A minimal model of ER protein-folding homeostasis. U: unfolded protein in the ER, C: chaperone (BiP-like)
# capacity, both in arbitrary units; time in hours.
#   dU/dt = s * T(U) - kf * C * U - kd * U
#   dC/dt = c0 + beta * U^n / (K^n + U^n) - gamma * C
# s: rate of entry of new client proteins (secretory load); kf: chaperone-assisted folding (and export);
# kd: ERAD; c0: basal chaperone synthesis; beta: UPR-induced synthesis (IRE1/ATF6 transcription), half-
# maximal at U = K; gamma: chaperone turnover; T(U) = 1 / (1 + (U/KP)^2) is PERK translational attenuation
# (T = 1 without PERK). A: response to a step increase of load at t = 5 h. B: steady-state unfolded protein
# against load without UPR, with transcriptional UPR, and with UPR plus PERK; the dashed line is an assumed
# threshold above which persistent stress commits the cell to apoptosis.
import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import solve_ivp

import wikibio as bio
from wikibio import quant

kf, kd, c0, gamma, K, n, KP = 0.5, 0.05, 1.0, 0.5, 1.0, 2, 3.0


def rhs(t, y, s_of_t, beta, perk):
    U, C = y
    s = s_of_t(t)
    T = 1.0 / (1.0 + (U / KP) ** 2) if perk else 1.0
    return [s * T - kf * C * U - kd * U, c0 + beta * U ** n / (K ** n + U ** n) - gamma * C]


def steady(s, beta, perk):
    sol = solve_ivp(rhs, (0, 400), [0.0, c0 / gamma], args=(lambda t: s, beta, perk), rtol=1e-8, atol=1e-10)
    return sol.y[:, -1]


fig, axs = plt.subplots(1, 3, figsize=(11.5, 3.6), gridspec_kw={"width_ratios": [1, 1, 1.15]})
tt = np.linspace(0, 40, 800)
for s1, tok in ((5, "enzyme"), (20, "protein"), (45, "negative")):
    f = lambda t, s1=s1: 1.0 if t < 5 else s1
    sol = solve_ivp(rhs, (0, 40), steady(1.0, 8.0, True), t_eval=tt, args=(f, 8.0, True), rtol=1e-8, max_step=0.05)
    axs[0].plot(tt, sol.y[0], color=quant.line_color(tok), lw=1.8, label=f"s = {s1}")
    axs[1].plot(tt, sol.y[1], color=quant.line_color(tok), lw=1.8, label=f"s = {s1}")
axs[0].axhline(4.0, color=bio.P.muted(), ls="--", lw=1)
axs[0].set(xlabel="t / h", ylabel="unfolded protein U", title="A  Load step at t = 5 h")
axs[1].set(xlabel="t / h", ylabel="chaperone C", title="UPR induces chaperones")
axs[0].legend(frameon=False, fontsize=8)

S = np.linspace(0.5, 60, 80)
for beta, perk, tok, lab in ((0.0, False, "muted", "no UPR"), (8.0, False, "channel", "UPR (IRE1, ATF6)"),
                             (8.0, True, "positive", "UPR + PERK")):
    U = [steady(s, beta, perk)[0] for s in S]
    axs[2].plot(S, U, color=quant.line_color(tok), lw=1.8, label=lab)
axs[2].axhline(4.0, color=bio.P.muted(), ls="--", lw=1)
axs[2].text(0.5, 4.2, "apoptosis threshold", fontsize=8, color=bio.P.muted())
axs[2].set(xlabel="secretory load s", ylabel="steady-state U", title="B  Capacity and its limit", ylim=(0, 12))
axs[2].legend(frameon=False, fontsize=8, loc="upper right")
for a in axs:
    a.spines[["top", "right"]].set_visible(False)
    a.title.set_fontsize(10)
fig.tight_layout()
