"""Dispersal and diversity in a mass-effects metacommunity (after Mouquet and Loreau 2003).

Twelve species compete for space in twelve patches. In each patch all sites are occupied; individuals
die at a constant rate and each vacant site is won by species i with probability proportional to
c_ik R_ik, where c_ik is its competitive ability in patch k and R_ik = (1 - a) P_ik + a mean_{l != k} P_il
is its local seed rain: a fraction a of propagules disperses to other patches. Species i is the best
competitor in patch i, and abilities decline with cyclic distance between patches,
c_ik = exp(-0.35 d_ik), multiplied by a small species-specific factor (fixed random draw) that makes
some species regionally better than others. The deterministic equations
dP_ik/dt = c_ik R_ik / sum_j c_jk R_jk - P_ik are integrated to equilibrium for each a; a species counts
as present where P_ik > 0.001. A: alpha richness (mean per patch), gamma richness (whole
metacommunity) and additive beta diversity gamma - alpha. B: equilibrium relative abundance of all
species in patch 1 (the patch where species 1 is best).
"""

import numpy as np
from scipy.integrate import solve_ivp

import wikibio as bio
from wikibio import charts as C
from wikibio import quant as Q

P = bio.P
FS = bio.core.FONT
rng = np.random.default_rng(3)
fig, ax = bio.canvas(30.0, 12.0)

S = N = 12
d = (np.arange(S)[:, None] - np.arange(N)[None, :]) % S
c = np.clip(np.exp(-0.35 * d) * (1 + 0.06 * rng.standard_normal(S))[:, None], 1e-3, None)


def rhs(t, y, a):
    Pm = y.reshape(S, N)
    R = (1 - a) * Pm + a * (Pm.sum(1, keepdims=True) - Pm) / (N - 1)
    W = c * R
    return (W / W.sum(0, keepdims=True) - Pm).ravel()


As = np.concatenate([[1e-5], np.logspace(-4, 0, 41)])
alpha, gamma, patch1 = [], [], []
for a in As:
    s = solve_ivp(rhs, (0, 4000), np.full(S * N, 1 / S), args=(a,), rtol=1e-7, atol=1e-11, method="LSODA")
    Pm = s.y[:, -1].reshape(S, N)
    alpha.append((Pm > 1e-3).sum(0).mean())
    gamma.append(((Pm > 1e-3).any(1)).sum())
    patch1.append(Pm[:, 0])
alpha, gamma, patch1 = np.array(alpha), np.array(gamma), np.array(patch1)

pa = C.axes_at(ax, (2.6, 1.9, 11.4, 8.4))
pa.semilogx(As, gamma, color=Q.line_color("dna"), lw=1.8, label="gamma (regional)")
pa.semilogx(As, alpha, color=Q.line_color("positive"), lw=1.8, label="alpha (mean per patch)")
pa.semilogx(As, gamma - alpha, color=Q.line_color("rna"), lw=1.8, ls="--", label="beta = gamma - alpha")
pa.set_xlim(1e-4, 1)
pa.set_ylim(0, 13)
C.style_axes(pa, "proportion of propagules dispersing, a", "number of species")
pa.legend(frameon=False, fontsize=FS["tiny"], labelcolor=P.ink(), loc="center left")
bio.panel(ax, "A", (0.5, 11.6))
bio.label(ax, (2.6, 11.2), "Richness at three scales", size="small", bold=True, ha="left")

pb = C.axes_at(ax, (17.4, 1.9, 11.4, 8.4))
for i in range(S):
    tok = "dna" if i == 0 else "muted"
    lab = "species 1 (best in patch 1)" if i == 0 else ("other species" if i == 1 else None)
    pb.semilogx(As, patch1[:, i], color=Q.line_color(tok), lw=1.8 if i == 0 else 0.9, label=lab)
pb.set_xlim(1e-4, 1)
pb.set_ylim(0, 1.02)
C.style_axes(pb, "proportion of propagules dispersing, a", "relative abundance in patch 1")
pb.legend(frameon=False, fontsize=FS["tiny"], labelcolor=P.ink(), loc="upper left", bbox_to_anchor=(0, 0.85))
bio.panel(ax, "B", (15.3, 11.6))
bio.label(ax, (17.4, 11.2), "Local abundances in one patch", size="small", bold=True, ha="left")
