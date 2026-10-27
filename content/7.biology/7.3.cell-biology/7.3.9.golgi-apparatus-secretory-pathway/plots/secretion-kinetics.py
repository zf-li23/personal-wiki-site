# Constitutive versus regulated secretion, with a two-pool model of insulin granule release. Constitutive
# secretion follows synthesis: release rate = synthesis rate, independent of the stimulus. Regulated
# secretion stores granules; a readily releasable pool R (docked, primed granules) is refilled from a large
# reserve at rate kr (Rmax - R) and released at rate ke R. Glucose raises cytosolic Ca2+ (triggering pathway),
# increasing ke from 0.002 to 0.3 per min, and also increases priming kr from 0.02 to 0.06 per min (amplifying
# pathway). A: the secretion rate ke R after a step of glucose at t = 0: a first phase from the release of the
# pool (minutes) and a sustained second phase limited by refilling, ke kr Rmax / (ke + kr). B: the pool R. Units
# are arbitrary (Rmax = 100 granules).
import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import solve_ivp

import wikibio as bio
from wikibio import quant

Rmax = 100.0


def params(t, amplify=True):
    if t < 0:
        return 0.002, 0.02
    return 0.3, (0.06 if amplify else 0.02)


def rhs(t, y, amplify):
    ke, kr = params(t, amplify)
    return [kr * (Rmax - y[0]) - ke * y[0]]


t = np.linspace(-10, 60, 1400)
fig, axs = plt.subplots(1, 2, figsize=(9.5, 3.4))
R0 = 0.02 * Rmax / (0.02 + 0.002)
for amp, ls, lab in ((True, "-", "triggering + amplifying"), (False, "--", "triggering only")):
    s = solve_ivp(rhs, (-10, 60), [R0], t_eval=t, args=(amp,), max_step=0.02)
    ke = np.where(t < 0, 0.002, 0.3)
    axs[0].plot(t, ke * s.y[0], color=quant.line_color("receptor"), ls=ls, lw=1.8, label=f"regulated ({lab})")
    axs[1].plot(t, s.y[0], color=quant.line_color("receptor"), ls=ls, lw=1.8, label=lab)
axs[0].plot(t, np.full_like(t, 1.0), color=quant.line_color("channel"), lw=1.8, label="constitutive")
axs[0].axvline(0, color=bio.P.muted(), lw=0.8, ls=":")
axs[0].text(0.8, 24, "glucose", fontsize=8, color=bio.P.muted())
axs[0].set(xlabel="t / min", ylabel="secretion rate / granules min⁻¹", title="A  Biphasic regulated secretion")
axs[0].legend(frameon=False, fontsize=7.5, loc="upper right")
axs[1].set(xlabel="t / min", ylabel="readily releasable pool R", title="B  The pool empties and refills partly", ylim=(0, 100))
for a in axs:
    a.spines[["top", "right"]].set_visible(False)
    a.title.set_fontsize(10)
fig.tight_layout()
