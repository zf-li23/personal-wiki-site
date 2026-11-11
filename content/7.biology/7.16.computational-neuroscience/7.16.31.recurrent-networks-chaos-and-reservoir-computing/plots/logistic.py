"""The logistic map x_{n+1} = r x_n (1 - x_n): period doubling, chaos and the Lyapunov exponent.

A: bifurcation diagram: for each r, iterate 600 times from x0 = 0.3, discard the first 400 and
   plot the remaining iterates.
B: Lyapunov exponent lambda(r) = (1/n) sum ln |r (1 - 2 x_k)| over 4000 iterates after a transient:
   negative on periodic orbits (zero at bifurcations), positive in the chaotic regime, with windows
   of periodicity (period 3 near r = 3.83).
C: sensitive dependence at r = 3.9: distance between two orbits started 1e-10 apart grows as
   exp(lambda n) until it saturates at the size of the attractor.
"""
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio

P = bio.P
r = np.linspace(2.5, 4.0, 1500)
x = 0.3 * np.ones_like(r)
pts_r, pts_x = [], []
for k in range(600):
    x = r * x * (1 - x)
    if k >= 400:
        pts_r.append(r.copy())
        pts_x.append(x.copy())
lam = np.zeros_like(r)
for k in range(4000):
    x = r * x * (1 - x)
    lam += np.log(np.abs(r * (1 - 2 * x)) + 1e-300)
lam /= 4000

fig, axs = plt.subplots(1, 3, figsize=(13, 3.9))
ax = axs[0]
ax.plot(np.concatenate(pts_r), np.concatenate(pts_x), ",", color=P.edge("dna"), alpha=0.35)
ax.set_xlabel("$r$")
ax.set_ylabel("$x_n$ (after transient)")
ax.set_title("A  Period doubling to chaos", loc="left", fontsize=10)
for rr, lab in ((3.0, "2-cycle"), (3.449, "4-cycle"), (3.5699, "chaos")):
    ax.axvline(rr, color=P.muted(), lw=0.6, ls=":")
    ax.text(rr + 0.008, 0.03, lab, fontsize=7, color=P.muted(), ha="left", va="bottom", rotation=90)
ax.set_ylim(0, 1.08)
ax = axs[1]
ax.plot(r, lam, color=P.edge("dna"), lw=0.8)
ax.axhline(0, color=P.ink(), lw=0.8)
ax.set_ylim(-1.5, 0.8)
ax.set_xlabel("$r$")
ax.set_ylabel("Lyapunov exponent $\\lambda$")
ax.set_title("B  Lyapunov exponent", loc="left", fontsize=10)
ax.annotate("period-3 window", xy=(3.83, -1.1), xytext=(3.0, -1.25), fontsize=8, color=P.muted(),
            arrowprops=dict(arrowstyle="-", color=P.muted(), lw=0.8))
ax = axs[2]
a, b = 0.3, 0.3 + 1e-10
d = []
for n in range(80):
    d.append(abs(a - b))
    a = 3.9 * a * (1 - a)
    b = 3.9 * b * (1 - b)
lam39 = lam[np.argmin(abs(r - 3.9))]
n = np.arange(80)
ax.semilogy(n, d, "o-", color=P.edge("negative"), ms=2.5, lw=1.0, label="$|x_n - x_n'|$")
ax.semilogy(n, 1e-10 * np.exp(lam39 * n), color=P.muted(), ls="--", lw=1.2, label=f"$10^{{-10}}\\,e^{{\\lambda n}}$, $\\lambda$ = {lam39:.2f}")
ax.set_ylim(1e-12, 3)
ax.set_xlabel("Iteration $n$")
ax.set_ylabel("Distance between orbits")
ax.set_title("C  Sensitive dependence ($r$ = 3.9)", loc="left", fontsize=10)
ax.legend(frameon=False, fontsize=8, loc="lower right")
for a_ in axs:
    a_.grid(True, alpha=0.3)
fig.tight_layout()
