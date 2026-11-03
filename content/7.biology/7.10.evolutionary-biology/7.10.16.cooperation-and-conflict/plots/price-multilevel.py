"""Multilevel partition of the Price equation (Theorem 16.5.1).

Groups of n = 10; number of altruists per group beta-binomial with mean 1/2 and intraclass correlation
rho (alpha = beta = (1/rho - 1)/2; binomial for rho = 0). Fitness w = 1 - c z + b (k - z)/(n - 1), with
c = 1, b = 3. Between-group term Cov_k(W_k, Z_k), within-group term E_k[Cov(w, z)] (population moments),
10 000 groups per value of rho.
"""

import numpy as np
import wikibio as bio
from wikibio import charts as C

P = bio.P
FS = bio.core.FONT
rng = np.random.default_rng(5)
n, b, c, G = 10, 3.0, 1.0, 10000
rhos = np.linspace(0, 0.6, 25)
bet, wit = [], []
for rho in rhos:
    if rho == 0:
        k = rng.binomial(n, 0.5, G)
    else:
        a = (1 / rho - 1) / 2
        k = rng.binomial(n, rng.beta(a, a, G))
    z = (np.arange(n)[None, :] < k[:, None]).astype(float)
    w = 1 - c * z + b * (k[:, None] - z) / (n - 1)
    Z, W = z.mean(1), w.mean(1)
    bet.append(np.mean((W - W.mean()) * (Z - Z.mean())))
    wit.append(np.mean(((w - W[:, None]) * (z - Z[:, None])).mean(1)))
bet, wit = np.array(bet), np.array(wit)
fig, ax = bio.canvas(18.0, 10.0)
p = C.axes_at(ax, (2.6, 1.6, 14.4, 7.4))
p.plot(rhos, bet, color=C.line("protein"), lw=1.9, label="between groups")
p.plot(rhos, wit, color=C.line("negative"), lw=1.9, label="within groups")
p.plot(rhos, bet + wit, color=P.ink(), lw=2.2, label="total change")
p.axhline(0, color=P.muted(), lw=0.8)
p.axvline(c / b, color=P.muted(), lw=0.9, ls=(0, (3, 2)))
p.text(c / b + 0.01, p.get_ylim()[1] * 0.9, "c/b", color=P.muted(), fontsize=FS["tiny"])
p.set_xlim(0, 0.6)
C.style_axes(p, "correlation of altruist status within groups ρ", "contribution to w̄Δz̄")
p.legend(frameon=False, fontsize=FS["tiny"], labelcolor=P.ink(), loc="upper left")
