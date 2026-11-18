"""Pest status and the economically optimal level of control (Section 53.3.1).

A: three species fluctuating around equilibria set by resources and enemies (stochastic Ricker
model ln N_{t+1} = ln N_t + 0.8 (1 - N_t / K_t) + noise): a pest whose equilibrium exceeds the
economic injury level (EIL), a non-pest always below it, and a potential pest held below it by
natural enemies until the enemies are removed in generation 40 (its equilibrium rises from 2 to 8).
B: control intensity u reduces a pest from N0 = 20 to N = N0 exp(-k u) at cost c u, and the crop
loss is V D N (Proposition 53.3.1). With c/k = 1 and V D = 0.25 (money units per pest), the total
cost c u + V D N = (c/k) ln(N0/N) + V D N is smallest at N* = c/(k V D) = 4.
"""

import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio
from wikibio import charts as C

P = bio.P
FS = bio.core.FONT
rng = np.random.default_rng(0)
EIL = 5.0


def ricker(K, T=80):
    n = np.empty(T)
    n[0] = K[0]
    for t in range(1, T):
        n[t] = n[t - 1] * np.exp(0.8 * (1 - n[t - 1] / K[t - 1]) + 0.25 * rng.standard_normal())
    return n


T = 80
fig, axes = plt.subplots(1, 2, figsize=(11.5, 4.0))
ax = axes[0]
tt = np.arange(T)
for K, col, lab in ((np.full(T, 9.0), C.line("negative"), "pest"),
                    (np.full(T, 1.5), C.line("positive"), "non-pest"),
                    (np.where(tt < 40, 2.0, 8.0), C.line("rna"), "potential pest")):
    ax.plot(tt, ricker(K), color=col, lw=1.8, label=lab)
ax.axhline(EIL, color=P.muted(), lw=1, ls=(0, (4, 2)))
ax.text(T - 1, EIL - 0.4, "EIL", color=P.muted(), fontsize=FS["tiny"], ha="right", va="top")
ax.axvline(40, color=P.muted(), lw=0.6, ls=":")
ax.text(41, 17.5, "enemies removed", color=P.muted(), fontsize=FS["tiny"])
ax.set_xlim(0, T - 1)
ax.set_ylim(0, 19)
C.style_axes(ax, "generation", "density")
ax.legend(frameon=False, fontsize=FS["tiny"], labelcolor=P.ink(), loc="upper left")
C.title(ax, "A  Pests, non-pests and potential pests")

ax = axes[1]
N0, ck, VD = 20.0, 1.0, 0.25
N = np.linspace(0.3, N0, 400)
control = ck * np.log(N0 / N)
damage = VD * N
ax.plot(N, control, color=C.line("dna"), lw=2, label="cost of control (c/k) ln(N0/N)")
ax.plot(N, damage, color=C.line("negative"), lw=2, label="crop loss V D N")
ax.plot(N, control + damage, color=P.ink(), lw=2.2, label="total")
ns = ck / VD
ax.plot([ns], [ck * np.log(N0 / ns) + VD * ns], "o", color=P.ink(), ms=6)
ax.axvline(ns, color=P.muted(), lw=0.7, ls=":")
ax.text(ns + 0.3, 5.6, "optimum N* = c / (kVD)", color=P.ink(), fontsize=FS["tiny"])
ax.set_xlim(0, N0)
ax.set_ylim(0, 6)
C.style_axes(ax, "pest density left after control, N", "cost (money units)")
ax.legend(frameon=False, fontsize=FS["tiny"], labelcolor=P.ink(), loc="upper right", bbox_to_anchor=(1, 0.9))
C.title(ax, "B  The economically optimal pest density")
fig.tight_layout()
