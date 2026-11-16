"""Mean time to extinction against carrying capacity.

Demographic stochasticity: logistic birth-death process with per capita birth rate b = 1 and death rate
d + (b - d) n / K, d = 0.5, so that the expected dynamics are logistic with r = 0.5. The mean time to
extinction from n = K is computed exactly from the first-step formula of Theorem 15.1.2,
T_n = sum_{k=1}^{n} tau_k with tau_k = sum_{i>=k} (lambda_k ... lambda_{i-1}) / (mu_k ... mu_i),
summed up to 6K (time in units of 1/b). Environmental stochasticity: the diffusion approximation of
Lande (1993), T = 2 / (V_e c) [ (K^c - 1) / c - ln K ] with c = 2 r / V_e - 1, for r = 0.5 and
environmental variances V_e = 0.2, 0.4, 0.8 (time in the same units, starting from K). Demographic
stochasticity alone gives times that grow exponentially with K (curving upward on these log axes);
environmental stochasticity gives power laws (straight lines) with exponent c.
"""

import numpy as np

import wikibio as bio
from wikibio import charts as C
from wikibio import quant as Q

P = bio.P
FS = bio.core.FONT
b, d = 1.0, 0.5
r = b - d


def T_demo(K):
    nmax = int(6 * K) + 20
    n = np.arange(1, nmax + 1, dtype=float)
    lam = b * n
    mu = n * (d + (b - d) * n / K)
    # log of products for stability: tau_k = sum_{i>=k} exp(sum_{j=k}^{i-1} ln lam_j - sum_{j=k}^{i} ln mu_j)
    llam, lmu = np.log(lam), np.log(mu)
    cl = np.r_[0, np.cumsum(llam)]
    cm = np.r_[0, np.cumsum(lmu)]
    total = 0.0
    for k in range(1, int(K) + 1):
        i = np.arange(k, nmax + 1)
        terms = (cl[i - 1] - cl[k - 1]) - (cm[i] - cm[k - 1])
        m = terms.max()
        total += np.exp(m) * np.exp(terms - m).sum()
    return total


Ks = np.unique(np.round(np.logspace(0.3, 2.0, 30)).astype(int))
Td = np.array([T_demo(K) for K in Ks])

fig, ax = bio.canvas(18.0, 11.0)
pa = C.axes_at(ax, (2.5, 1.6, 14.0, 8.2))
pa.plot(Ks, Td, "o-", ms=3, lw=1.6, color=Q.line_color("negative"), label="demographic (exact)")
Kc = np.logspace(0.3, 3, 200)
for Ve, tok in [(0.2, "dna"), (0.4, "enzyme"), (0.8, "protein")]:
    c = 2 * r / Ve - 1
    T = 2 / (Ve * c) * ((Kc ** c - 1) / c - np.log(Kc)) if abs(c) > 1e-9 else np.log(Kc) ** 2 / Ve
    pa.plot(Kc, T, lw=1.4, color=Q.line_color(tok), label=f"environmental, V_e = {Ve} (c = {c:.2f})")
pa.set_xscale("log")
pa.set_yscale("log")
pa.set_ylim(1, 1e8)
pa.set_xlim(2, 1000)
C.style_axes(pa, "carrying capacity K", "mean time to extinction (units of 1/b)")
pa.legend(frameon=False, fontsize=FS["tiny"], labelcolor=P.ink(), loc="upper left")
bio.label(ax, (2.5, 10.4), "Demographic versus environmental stochasticity", size="small", bold=True, ha="left")
