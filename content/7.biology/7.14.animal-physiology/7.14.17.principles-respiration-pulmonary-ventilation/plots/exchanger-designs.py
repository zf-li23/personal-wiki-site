"""Gas exchanger designs compared with a linear model (Piiper and Scheid).

The medium (water or air) enters at P_I, the blood at the venous P_v; both have constant capacitances, so a
flow carries a "capacity rate" C = flow x capacitance. D* = G / C_blood is the diffusing conductance relative
to the blood capacity rate, r = C_blood / C_medium. Normalised arterial partial pressure
E = (P_a - P_v) / (P_I - P_v):
  concurrent      E = (1 - exp(-D*(1 + r))) / (1 + r)
  ventilated pool E = (1 - exp(-D*)) / (1 + r (1 - exp(-D*)))     (mammalian alveolus: well-mixed gas)
  crosscurrent    E = (1 - exp(-D*)) (1 - exp(-L)) / L,  L = r (1 - exp(-D*))   (bird parabronchus)
  countercurrent  E = (1 - exp(-D*(1 - r))) / (1 - r exp(-D*(1 - r)))       (fish gill; D*/(1 + D*) at r = 1)
A: E against D* for r = 1. B: profiles along the exchanger for D* = 3, r = 1 (concurrent and countercurrent).
C: the limit D* -> infinity as a function of r.
"""
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio

P = bio.P


def concurrent(d, r):
    return (1 - np.exp(-d * (1 + r))) / (1 + r)


def pool(d, r):
    e = 1 - np.exp(-d)
    return e / (1 + r * e)


def cross(d, r):
    e = 1 - np.exp(-d)
    lam = r * e
    return e * (1 - np.exp(-lam)) / lam


def counter(d, r):
    if abs(r - 1) < 1e-9:
        return d / (1 + d)
    k = np.exp(-d * (1 - r))
    return (1 - k) / (1 - r * k)


designs = [
    ("countercurrent (fish gill)", counter, P.edge("blood"), "-"),
    ("crosscurrent (bird parabronchus)", cross, P.edge("enzyme"), "-"),
    ("ventilated pool (mammalian alveolus)", pool, P.edge("dna"), "-"),
    ("concurrent", concurrent, P.muted(), "--"),
]

fig, axs = plt.subplots(1, 3, figsize=(15, 4.2))
ax = axs[0]
d = np.linspace(0.01, 8, 300)
for lab, f, c, ls in designs:
    ax.plot(d, [f(x, 1.0) for x in d], color=c, lw=2, ls=ls, label=lab)
ax.set_xlabel("Relative diffusing conductance $D^* = G/C_{\\mathrm{blood}}$")
ax.set_ylabel("$(P_a - P_v)/(P_I - P_v)$")
ax.set_ylim(0, 1.02)
ax.set_xlim(0, 8)
ax.legend(frameon=False, fontsize=8, loc="lower right")
ax.set_title("A  Efficiency of the four designs, r = 1", loc="left", fontsize=10)

ax = axs[1]
D, r = 3.0, 1.0
x = np.linspace(0, 1, 200)
# concurrent: both flow in +x
pb = (1 - np.exp(-D * (1 + r) * x)) / (1 + r)
pm = 1 - r * pb
ax.plot(x, pm, color=P.muted(), lw=1.6, ls="--", label="concurrent: medium")
ax.plot(x, pb, color=P.muted(), lw=2.4, ls="--", label="concurrent: blood")
# countercurrent with r = 1: linear profiles; blood enters at x = 0, medium at x = 1
pb_c = D * x / (1 + D)
pm_c = (1 + D * x) / (1 + D)
ax.plot(x, pm_c, color=P.edge("dna"), lw=1.6, label="countercurrent: medium")
ax.plot(x, pb_c, color=P.edge("blood"), lw=2.4, label="countercurrent: blood")
ax.annotate("", xy=(0.35, 0.96), xytext=(0.65, 0.96),
            arrowprops=dict(arrowstyle="->", color=P.edge("dna")))
ax.text(0.5, 0.9, "medium (countercurrent)", ha="center", fontsize=8, color=P.edge("dna"))
ax.set_xlabel("Position along the exchanger (blood inlet = 0)")
ax.set_ylabel("$(P - P_v)/(P_I - P_v)$")
ax.set_ylim(0, 1.05)
ax.legend(frameon=False, fontsize=7.5, loc="lower right")
ax.set_title("B  Profiles, D* = 3, r = 1", loc="left", fontsize=10)

ax = axs[2]
rs = np.linspace(0.05, 3, 300)
ax.plot(rs, np.minimum(1, 1 / rs), color=P.edge("blood"), lw=2, label="countercurrent")
ax.plot(rs, (1 - np.exp(-rs)) / rs, color=P.edge("enzyme"), lw=2, label="crosscurrent")
ax.plot(rs, 1 / (1 + rs), color=P.edge("dna"), lw=2, label="pool = concurrent")
ax.set_xlabel("Capacity-rate ratio $r = C_{\\mathrm{blood}}/C_{\\mathrm{medium}}$")
ax.set_ylabel("Limit of $(P_a - P_v)/(P_I - P_v)$ as $D^* \\to \\infty$")
ax.set_ylim(0, 1.02)
ax.legend(frameon=False, fontsize=8)
ax.set_title("C  Upper limits", loc="left", fontsize=10)
for a in axs:
    a.grid(True, alpha=0.3)
fig.tight_layout()
