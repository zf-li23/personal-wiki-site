# Order-of-magnitude model of clonal expansion (Example 1.3.1): n(t) = n0 * 2**((t - t_lag)/tau) after a lag,
# for several precursor numbers n0, compared with the effector size n* needed and with an unchecked
# bacterium doubling every hour. Parameters are literature orders of magnitude, used for illustration.
import numpy as np

import wikibio as bio
from wikibio import quant

P = bio.P
fig, ax = bio.canvas(14.0, 8.0)

T_LAG, TAU_H, N_STAR = 1.0, 7.0, 1e6
t = np.linspace(0, 8, 800)
pl = quant.Plot(ax, (2.0, 1.4, 10.6, 5.9), xlim=(0, 8), ylim=(1, 1e10), ylog=True,
                xlabel="time after antigen entry / days", ylabel="cells (log scale)",
                xticks=[0, 1, 2, 3, 4, 5, 6, 7, 8],
                yticks=[(1, "1"), (1e2, "10²"), (1e4, "10⁴"), (1e6, "10⁶"), (1e8, "10⁸"), (1e10, "10¹⁰")], grid=True)
for n0, tok in ((10, "dna2"), (100, "dna"), (1000, "protein")):
    n = n0 * 2.0 ** (np.maximum(t - T_LAG, 0) * 24 / TAU_H)
    pl.line(t, np.minimum(n, 1e10), tok, lw=2.0)
    tstar = T_LAG + np.log2(N_STAR / n0) * TAU_H / 24
    pl.points([tstar], [N_STAR], tok, r=0.11)
    pl.text(tstar - 0.1, N_STAR * 2.5, f"{tstar:.1f} d", size="tiny", ha="right", va="bottom",
            color=quant.line_color(tok))
    pl.text(0.66, n0 * 1.6, f"$n_0$ = {n0}", size="tiny", ha="center", va="bottom", color=quant.line_color(tok))
pl.hline(N_STAR, "muted", text="effector size $n^*$", side="left")
b = 10 * 2.0 ** (t * 24 / 1.0)
pl.line(t[b < 1e10], b[b < 1e10], "muted", lw=1.2, dashed=True)
pl.text(1.4, 3e9, "bacterium, doubling\nevery 1 h (unchecked)", size="tiny", ha="left", color=P.muted())
bio.label(ax, (7.3, 7.75), "Lag 1 d, then one division every 7 h", size="small")
