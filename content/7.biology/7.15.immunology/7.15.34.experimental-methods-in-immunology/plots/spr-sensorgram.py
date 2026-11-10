# Simulated SPR sensorgrams for a 1:1 (Langmuir) antibody-antigen interaction.
#   association (analyte concentration C):  R(t) = R_eq (1 - exp(-k_obs t)),  k_obs = k_on C + k_off,  R_eq = R_max C / (C + K_D)
#   dissociation (buffer only):             R(t) = R(t_0) exp(-k_off (t - t_0)),   K_D = k_off / k_on
# Panel A: antibody 1 (k_on = 1e6 /M/s, k_off = 1e-3 /s, K_D = 1 nM) at four concentrations, R_max = 100 RU.
# Panel B: two antibodies with the same K_D = 1 nM but different kinetics, both at 10 nM: antibody 1 (fast on, fast off)
# and antibody 2 (k_on = 1e5 /M/s, k_off = 1e-4 /s, slow on, slow off); equal affinity, very different time courses.
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio
from wikibio import charts

P = bio.P
RMAX, T_ON, T_END = 100.0, 300.0, 1200.0


def sensorgram(kon, koff, conc):
    t = np.linspace(0, T_END, 1500)
    kd = koff / kon
    req = RMAX * conc / (conc + kd)
    kobs = kon * conc + koff
    r_on = req * (1 - np.exp(-kobs * np.minimum(t, T_ON)))
    r0 = req * (1 - np.exp(-kobs * T_ON))
    return t, np.where(t <= T_ON, r_on, r0 * np.exp(-koff * (t - T_ON)))


fig, axs = plt.subplots(1, 2, figsize=(10, 3.6))
ax = axs[0]
for c_nm, tok in ((1, "neutral"), (3, "receptor"), (10, "protein"), (30, "negative")):
    t, r = sensorgram(1e6, 1e-3, c_nm * 1e-9)
    ax.plot(t, r, color=charts.line(tok), lw=1.5, label=f"{c_nm} nM")
ax.axvline(T_ON, color=P.muted(), lw=0.8, ls=":")
ax.text(T_ON / 2, 120, "association", fontsize=7, color=P.muted(), ha="center")
ax.text((T_ON + T_END) / 2, 120, "dissociation (buffer)", fontsize=7, color=P.muted(), ha="center")
ax.set_ylim(0, 130)
ax.legend(frameon=False, fontsize=7, labelcolor=P.ink(), loc="upper right", bbox_to_anchor=(1.0, 0.86), title="antigen", title_fontsize=7)
charts.style_axes(ax, "time / s", "response / RU")
charts.title(ax, "A")

ax = axs[1]
t, r1 = sensorgram(1e6, 1e-3, 10e-9)
t, r2 = sensorgram(1e5, 1e-4, 10e-9)
ax.plot(t, r1, color=charts.line("protein"), lw=1.6, label="antibody 1: $k_{on}=10^6$, $k_{off}=10^{-3}$")
ax.plot(t, r2, color=charts.line("negative"), lw=1.6, label="antibody 2: $k_{on}=10^5$, $k_{off}=10^{-4}$")
ax.axvline(T_ON, color=P.muted(), lw=0.8, ls=":")
ax.set_ylim(0, 130)
ax.legend(frameon=False, fontsize=7, labelcolor=P.ink(), loc="upper right", title="both $K_D = 1$ nM, 10 nM antigen", title_fontsize=7)
charts.style_axes(ax, "time / s", "response / RU")
charts.title(ax, "B")
fig.tight_layout()
