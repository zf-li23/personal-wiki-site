# Kinetic proofreading: accuracy, energy and speed.
# A: Hopfield's scheme with thermodynamically consistent reverse rates. Enzyme states E, EX, EX* for a correct
#    (C) and a wrong (D) substrate at equal concentration. E + X <-> EX (k_on = 1, k_off,C = 1),
#    EX <-> EX* (m = 0.01 forward, m_r back), EX* <-> E + X (l_C = 1 out, l_on back), EX* -> product (W = 1e-3).
#    The wrong substrate leaves both bound states q = 100 times faster (f0 = 1/q = 0.01). The driving force of
#    the cycle E -> EX -> EX* -> E is dmu = kT ln[(k_on m l)/(k_off m_r l_on)]; it is split equally between
#    the two reverse rates. The steady-state error J_D/J_C falls from f0 at dmu = 0 (equilibrium) to near f0^2.
# B: speed against accuracy at large dmu, varying the proofreading rate m: more accuracy, slower product.
# C: kinetic proofreading in T-cell activation (McKeithan 1995): a ligand-receptor complex must pass N
#    modification steps (rate k_p = 1 /s each) before it signals; the probability of signalling,
#    (k_p/(k_p + k_off))^N, discriminates ligands by their dwell time 1/k_off ever more sharply as N grows.
import matplotlib.pyplot as plt
import numpy as np
from scipy.linalg import null_space

import wikibio as bio
from wikibio import charts

P = bio.P
kon, koff, lC, Wp, q = 1.0, 1.0, 1.0, 1e-3, 100.0


def fluxes(dmu, m=0.01):
    mr = m * np.exp(-dmu / 2)
    lon = kon * m * lC / (koff * mr) * np.exp(-dmu)
    # states: 0 E, 1 EC, 2 EC*, 3 ED, 4 ED*
    Q = np.zeros((5, 5))

    def add(i, j, r):
        Q[j, i] += r
        Q[i, i] -= r

    for s, (b, bs) in enumerate(((1, 2), (3, 4))):
        qq = 1.0 if s == 0 else q
        add(0, b, kon)
        add(b, 0, koff * qq)
        add(b, bs, m)
        add(bs, b, mr)
        add(bs, 0, lC * qq + Wp)   # leaves unbound, or makes product (enzyme returns to E)
        add(0, bs, lon)
    p = null_space(Q)[:, 0]
    p = p / p.sum()
    return Wp * p[2], Wp * p[4]


fig, axs = plt.subplots(1, 3, figsize=(13.5, 4.1))
dmus = np.linspace(0, 30, 120)
err = np.array([fluxes(d)[1] / fluxes(d)[0] for d in dmus])
axs[0].semilogy(dmus, err, color=charts.line("enzyme"), lw=1.8)
for y, txt in ((1 / q, "f₀ (equilibrium discrimination)"), (1 / q**2, "f₀²")):
    axs[0].axhline(y, color=P.muted(), lw=0.7, ls=":")
    axs[0].text(14, y * 0.72, txt, fontsize=7.5, color=P.muted())
charts.style_axes(axs[0], "driving force of the cycle Δμ / kT", "error J_D / J_C")
charts.title(axs[0], "A   Accuracy is bought with free energy")

ms = np.logspace(-4, 1, 60)
JC, ER = [], []
for m in ms:
    jc, jd = fluxes(30.0, m)
    JC.append(jc)
    ER.append(jd / jc)
axs[1].loglog(ER, np.array(JC) / Wp, color=charts.line("dna"), lw=1.8)
for m0 in (1e-3, 1e-2, 1e-1, 1.0):
    jc, jd = fluxes(30.0, m0)
    axs[1].plot(jd / jc, jc / Wp, "o", color=charts.line("dna"), ms=4)
    axs[1].text(jd / jc * 1.15, jc / Wp, f"m = {m0:g}", fontsize=7, color=P.ink())
charts.style_axes(axs[1], "error J_D / J_C", "speed J_C / W (fraction of enzyme in EC*)")
charts.title(axs[1], "B   Speed–accuracy trade-off")

tau = np.logspace(-2, 2, 300)
kp = 1.0
for N, tok in ((1, "neutral"), (3, "dna"), (6, "rna")):
    axs[2].loglog(tau, (kp / (kp + 1 / tau)) ** N, color=charts.line(tok), lw=1.8, label=f"N = {N}")
for t0 in (0.2, 2.0):
    axs[2].axvline(t0, color=P.muted(), lw=0.6, ls=":")
r = [((kp / (kp + 1 / 2.0)) / (kp / (kp + 1 / 0.2))) ** N for N in (1, 3, 6)]
axs[2].text(0.012, 0.6, "signal ratio for dwell 2 s vs 0.2 s:\n" + ", ".join(f"N={N}: {x:.0f}×" for N, x in zip((1, 3, 6), r)),
            fontsize=7, color=P.ink())
axs[2].set_ylim(1e-8, 2)
charts.style_axes(axs[2], "ligand dwell time 1/k_off / s", "probability of signalling")
axs[2].legend(fontsize=7.5, frameon=False, loc="lower right")
charts.title(axs[2], "C   T-cell receptor proofreading")
fig.tight_layout()
