"""Fixation probability of a single new mutation (p = 1/2N) relative to a neutral one, 2N u, as a function of
the scaled selection coefficient N s. Lines: Kimura's diffusion formula for N = 100 and N = 1000 (they nearly
coincide in the scaled form); dots: 20 000 simulated Wright-Fisher populations of N = 100 per value of s
(95 % Wilson intervals). Dashed: Haldane's approximation u = 2s, that is 2N u = 4 N s. Within the
nearly neutral zone |4Ns| < 1 (shaded) drift dominates; beneficial mutations with 4Ns >> 1 fix with
probability of only about 2s, and deleterious ones are almost never fixed."""
import numpy as np
import matplotlib.pyplot as plt
import wikibio as bio
from wikibio import charts
from wikibio import evolution as evo

P = bio.P
FT = bio.core.FONT
fig, ax = plt.subplots(figsize=(6.8, 4.0))
fig.subplots_adjust(left=0.12, right=0.97, bottom=0.14, top=0.9)
Ns = np.linspace(-3, 10, 400)
for N, tok in ((100, "rna"), (1000, "protein")):
    s = Ns / N
    ax.semilogy(Ns, 2 * N * evo.kimura_u(1 / (2 * N), N, s), color=charts.line(tok), lw=2,
                label=f"Kimura, $N = {N}$")
pos = Ns[Ns > 0.3]
ax.semilogy(pos, 4 * pos, color=P.ink(), lw=1, ls="--", label="$u = 2s$")
N = 100
rng = np.random.default_rng(1)
for x in (-2, -1, 0, 1, 2, 4, 6, 8):
    u, lo, hi = evo.fixation_probability(N, x / N, 1 / (2 * N), reps=20000, rng=rng)
    if u > 0:
        ax.plot([x, x], [2 * N * max(lo, 1e-4), 2 * N * hi], color=P.ink(), lw=0.9)
        ax.scatter([x], [2 * N * u], s=16, color=P.ink(), zorder=4)
ax.axvspan(-0.25, 0.25, color=P.mix(P.surface(), P.muted(), 0.2), lw=0)
ax.axhline(1, color=P.muted(), lw=0.8, ls=":")
ax.text(-2.9, 1.15, "neutral: $u = 1/2N$", fontsize=FT["tiny"], color=P.muted())
ax.set_xlim(-3, 10)
ax.set_ylim(1e-2, 60)
ax.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="lower right")
charts.style_axes(ax, "scaled selection coefficient $Ns$", "$2Nu$ (relative to neutral)")
charts.title(ax, "Fixation of a new mutation")
