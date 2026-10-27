# A cut-out switch model of Rab5-to-Rab7 conversion on an endosome (after Del Conte-Zerial et al., Mol Syst
# Biol 4:206, 2008). r5 and r7 are the fractions of Rab5 and Rab7 in the GTP-bound, membrane-bound state;
# time in minutes.
#   dr5/dt = (k5 + f5 r5^2/(K5^2 + r5^2)) (1 - r5) - (g5 + h r7^4/(Kh^4 + r7^4)) r5
#   dr7/dt = (k7 + c r5^4/(Kc^4 + r5^4) + f7 r7^2/(K7^2 + r7^2)) (1 - r7) - g7 r7
# f5: Rab5 positive feedback (Rab5-GTP recruits its GEF Rabex-5 through the effector Rabaptin-5); c: Rab5-GTP
# recruits the Rab7 GEF Mon1-Ccz1 (SAND-1); f7: Rab7 self-recruitment; h: Rab7-GTP recruits a Rab5 GAP
# (and Mon1 displaces Rabex-5), the cut-out; g5, g7: basal GAP activity. A: with the cut-out, Rab5 domains rise,
# trigger Rab7 and are switched off; without it (h = 0) both Rabs stay on (a hybrid compartment). B: the time
# of conversion (r7 = r5) as the Rab5-to-Rab7 activation c is varied: weak coupling delays conversion
# steeply, so the time an endosome spends as an early endosome can be tuned.
import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import solve_ivp

from wikibio import quant

k5, f5, K5, g5 = 0.02, 1.0, 0.5, 0.15
k7, Kc, f7, K7, g7, Kh = 0.001, 0.7, 0.6, 0.5, 0.1, 0.4


def rhs(t, y, c, h):
    r5, r7 = y
    return [(k5 + f5 * r5 ** 2 / (K5 ** 2 + r5 ** 2)) * (1 - r5) - (g5 + h * r7 ** 4 / (Kh ** 4 + r7 ** 4)) * r5,
            (k7 + c * r5 ** 4 / (Kc ** 4 + r5 ** 4) + f7 * r7 ** 2 / (K7 ** 2 + r7 ** 2)) * (1 - r7) - g7 * r7]


fig, axs = plt.subplots(1, 2, figsize=(9.5, 3.4))
t = np.linspace(0, 60, 1200)
for h, ls, lab in ((1.5, "-", "with cut-out (Rab7 → Rab5 GAP)"), (0.0, ":", "without cut-out")):
    s = solve_ivp(rhs, (0, 60), [0.05, 0.0], t_eval=t, args=(0.02, h), rtol=1e-8, max_step=0.05)
    axs[0].plot(t, s.y[0], color=quant.line_color("positive"), ls=ls, lw=1.8, label=f"Rab5, {lab}")
    axs[0].plot(t, s.y[1], color=quant.line_color("negative"), ls=ls, lw=1.8, label=f"Rab7, {lab}")
axs[0].set(xlabel="t / min", ylabel="active fraction", title="A  Rab5 → Rab7 conversion", ylim=(0, 1.05))
axs[0].legend(frameon=False, fontsize=7, loc="center right")

cs = np.linspace(0.006, 0.08, 60)
T = []
for c in cs:
    s = solve_ivp(rhs, (0, 400), [0.05, 0.0], args=(c, 1.5), rtol=1e-8, max_step=0.1, dense_output=True)
    tt = np.linspace(1, 400, 8000)
    y = s.sol(tt)
    cross = np.where((y[1] > y[0]) & (y[0] > 0) )[0]
    T.append(tt[cross[0]] if len(cross) else np.nan)
axs[1].plot(cs, T, color=quant.line_color("protein"), lw=1.8)
axs[1].set(xlabel="Rab5 → Rab7 GEF recruitment c / min⁻¹", ylabel="conversion time / min", title="B  Tuning the delay")
for a in axs:
    a.spines[["top", "right"]].set_visible(False)
    a.title.set_fontsize(10)
fig.tight_layout()
