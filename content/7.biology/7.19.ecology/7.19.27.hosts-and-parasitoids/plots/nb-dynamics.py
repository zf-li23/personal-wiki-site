"""The Nicholson-Bailey model H' = lam H exp(-a P), P' = c H (1 - exp(-a P)) (Section 27.2).

A: lam = 2, a = 0.05, c = 1, started 5 % above the host equilibrium: host and parasitoid numbers
oscillate with growing amplitude (log scale); after about 30 generations the hosts crash.
B: the same trajectory in the phase plane (log axes): an outward spiral around the equilibrium (dot).
C: the eigenvalues of the linearization (Theorem 27.2.1) are complex with modulus
sqrt(lam ln lam / (lam - 1)) > 1 for every lam > 1 (solid; dashed: the unit circle), and the
period of the oscillation, 2 pi / arg(eigenvalue), in generations (right axis).
"""

import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio
from wikibio import charts as C

P = bio.P
FS = bio.core.FONT
lam, a, c = 2.0, 0.05, 1.0
Ps = np.log(lam) / a
Hs = lam * np.log(lam) / ((lam - 1) * a * c)
H, Q = [Hs * 1.05], [Ps]
for _ in range(29):
    e = np.exp(-a * Q[-1])
    H.append(lam * H[-1] * e)
    Q.append(c * H[-2] * (1 - e))
H, Q = np.array(H), np.array(Q)
host, para = C.line("positive"), C.line("negative")

fig, axes = plt.subplots(1, 3, figsize=(13.5, 4.3))
ax = axes[0]
t = np.arange(H.size)
ax.semilogy(t, H, "-o", ms=2.5, color=host, lw=1.2, label="hosts H")
ax.semilogy(t, Q, "-s", ms=2.5, color=para, lw=1.2, label="parasitoids P")
ax.axhline(Hs, color=host, lw=0.6, ls=(0, (2, 2)))
ax.axhline(Ps, color=para, lw=0.6, ls=(0, (2, 2)))
ax.set_ylim(1e-3, 3e3)
ax.legend(fontsize=FS["tiny"], frameon=False, loc="lower left")
C.style_axes(ax, "Generation t", "Number (log scale)")
C.title(ax, "A  Diverging oscillations")

ax = axes[1]
ax.loglog(H[:-1], Q[:-1], "-", color=P.muted(), lw=0.7)
ax.loglog(H[:-1], Q[:-1], "o", color=P.ink(), ms=2.2)
ax.plot(Hs, Ps, "o", ms=7, mfc=P.surface(), mec=P.ink())
ax.annotate("t = 0", (H[0], Q[0]), (H[0] * 1.6, Q[0] * 0.5), fontsize=FS["tiny"], color=P.ink(),
            arrowprops=dict(arrowstyle="-", color=P.muted(), lw=0.6))
C.style_axes(ax, "Hosts H", "Parasitoids P")
C.title(ax, "B  Outward spiral")

ax = axes[2]
L = np.linspace(1.01, 20, 400)
s = np.log(L) / (L - 1)
tr, det = 1 + s, L * s
mod = np.sqrt(det)
theta = np.arccos(tr / (2 * mod))
ax.plot(L, mod, color=P.ink(), lw=1.5, label="|eigenvalue|")
ax.axhline(1, color=P.muted(), lw=0.8, ls=(0, (3, 2)))
ax.set_ylim(0.9, 2.0)
C.style_axes(ax, "Host rate of increase λ", "Modulus of eigenvalues")
ax2 = ax.twinx()
ax2.plot(L, 2 * np.pi / theta, color=C.line("dna"), lw=1.2, ls=(0, (4, 2)), label="period")
ax2.set_ylim(0, 14)
C.style_axes(ax2, None, "Period of oscillation (generations)")
ax2.spines["right"].set_visible(True)
ax2.spines["right"].set_color(P.muted())
h1, l1 = ax.get_legend_handles_labels()
h2, l2 = ax2.get_legend_handles_labels()
ax.legend(h1 + h2, l1 + l2, fontsize=FS["tiny"], frameon=False, loc="upper center")
C.title(ax, "C  Linear instability for all λ > 1")
fig.tight_layout()
