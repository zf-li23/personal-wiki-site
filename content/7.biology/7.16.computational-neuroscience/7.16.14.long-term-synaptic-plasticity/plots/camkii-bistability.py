"""A minimal bistable model of CaMKII autophosphorylation (a Lisman-type switch).

f = fraction of autophosphorylated subunits.
  df/dt = (1 - f) [k_c h(c) + k_a f^2] - V f / (K_M + f),   h(c) = c^4 / (c^4 + K^4)
k_c = 0.5 /s (Ca2+/calmodulin-driven phosphorylation), k_a = 0.5 /s (cooperative
autophosphorylation: a subunit is phosphorylated by an active neighbour), phosphatase (PP1)
with V = 0.04 /s and K_M = 0.1 (saturable), K = 1 uM, baseline Ca2+ 0.1 uM.
A: phosphorylation without Ca2+ drive, k_a (1-f) f^2 (solid), against dephosphorylation
   V f/(K_M+f) for three phosphatase activities (dashed): f = 0 is always a fixed point and, for
   V below about 0.085 /s, a second stable state and an unstable threshold appear.
B: steady states against phosphatase activity V at baseline Ca2+ (solid: stable, dashed: unstable):
   a hysteretic switch (saddle-node bifurcations).
C: a time course at V = 0.04 /s: Ca2+ pulses of 3 uM for 0.3 s (fails), 1 s (succeeds and the
   state persists after Ca2+ returns to baseline), a transient surge of phosphatase (V = 0.3 /s
   for 25 s; as by low-frequency stimulation) that resets the switch, and a 2 s pulse (succeeds
   again). Top: Ca2+ and phosphatase drive; bottom: f.
"""
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio

P = bio.P
kc, ka, KM, K, V0, cb = 0.5, 0.5, 0.1, 1.0, 0.04, 0.1


def h(c):
    return c**4 / (c**4 + K**4)


fig = plt.figure(figsize=(13, 5.2))
gs = fig.add_gridspec(2, 3, height_ratios=[1, 1.0], width_ratios=[1, 1, 1.5])
axA = fig.add_subplot(gs[:, 0])
axB = fig.add_subplot(gs[:, 1])
f = np.linspace(0, 1, 400)
axA.plot(f, ka * (1 - f) * f**2, color=P.edge("positive"), lw=2.2, label="autophosphorylation")
for V, col in ((0.02, P.edge("dna")), (0.04, P.edge("protein")), (0.1, P.edge("negative"))):
    axA.plot(f, V * f / (KM + f), color=col, lw=1.6, ls="--", label=f"dephosphorylation, $V$ = {V:g}")
axA.set_xlabel("Phosphorylated fraction $f$")
axA.set_ylabel("Rate / s$^{-1}$")
axA.set_ylim(0, 0.14)
axA.set_title("A  Rates", loc="left", fontsize=10)
axA.legend(frameon=False, fontsize=7.5, loc="upper right")

Vs = np.linspace(0.005, 0.12, 400)
stable, unstable = [], []
for V in Vs:
    # nonzero steady states: ka (1-f) f (KM+f) = V  ->  cubic in f
    coef = np.poly1d([-ka, ka * (1 - KM), ka * KM, 0.0]) - V  # -ka f^3 + ka(1-KM) f^2 + ka KM f - V
    roots = np.sort([r.real for r in coef.roots if abs(r.imag) < 1e-9 and 0 < r.real < 1])
    if len(roots) == 2:
        unstable.append((V, roots[0]))
        stable.append((V, roots[1]))
stable, unstable = np.array(stable), np.array(unstable)
axB.plot(stable[:, 0], stable[:, 1], color=P.edge("positive"), lw=2.2, label="stable (on)")
axB.plot(unstable[:, 0], unstable[:, 1], color=P.edge("negative"), lw=2.0, ls="--", label="unstable (threshold)")
axB.plot([0, Vs[-1]], [0, 0], color=P.edge("positive"), lw=2.2, label="stable (off)")
# off state is stable for every V > 0
axB.axvline(V0, color=P.muted(), lw=0.8, ls=":")
axB.text(V0 + 0.002, 0.97, "$V$ = 0.04", fontsize=8, color=P.muted(), va="top")
axB.set_xlabel("Phosphatase activity $V$ / s$^{-1}$")
axB.set_ylabel("Steady-state $f$")
axB.set_xlim(0, 0.12)
axB.set_title("B  Bistability", loc="left", fontsize=10)
axB.legend(frameon=False, fontsize=8, loc="center right", bbox_to_anchor=(1.0, 0.45))

dt = 0.005
T = 300.0
t = np.arange(0, T, dt)
c = np.full_like(t, cb)
V = np.full_like(t, V0)
for t0, dur in ((20, 0.3), (60, 1.0), (200, 2.0)):
    c[(t >= t0) & (t < t0 + dur)] = 3.0
V[(t >= 140) & (t < 165)] = 0.3
x = np.zeros_like(t)
fcur = 0.0
for k in range(len(t)):
    x[k] = fcur
    df = (1 - fcur) * (kc * h(c[k]) + ka * fcur**2) - V[k] * fcur / (KM + fcur)
    fcur += dt * df
axT = fig.add_subplot(gs[0, 2])
axT.plot(t, c, color=P.edge("ca"), lw=1.4, label="[Ca$^{2+}$] / $\\mu$M")
axT.plot(t, V * 10, color=P.edge("negative"), lw=1.4, label="phosphatase $V$ (x10)")
axT.set_ylim(0, 3.4)
axT.set_xlim(0, T)
axT.set_ylabel("Drive")
axT.tick_params(labelbottom=False)
axT.legend(frameon=False, fontsize=7.5, loc="upper right", ncol=2)
axT.set_title("C  Switching and reset", loc="left", fontsize=10)
axF = fig.add_subplot(gs[1, 2], sharex=axT)
axF.plot(t, x, color=P.edge("positive"), lw=2.0)
axF.set_xlabel("Time / s")
axF.set_ylabel("$f$")
axF.set_ylim(-0.02, 1.02)
for a in (axA, axB, axT, axF):
    a.grid(True, alpha=0.3)
fig.tight_layout()
