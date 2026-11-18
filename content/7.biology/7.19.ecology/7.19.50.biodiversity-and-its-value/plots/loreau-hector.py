"""The Loreau-Hector partition of the net biodiversity effect, applied to simulated mixtures.

Plants compete by Lotka-Volterra dynamics dN_i/dt = r N_i (K_i - sum_j a_ij N_j) / K_i (r = 1), so that the
monoculture yield of species i is M_i = K_i. Pool of 30 species, K_i lognormal (median 200 g m^-2, log-sd
0.5). Mixtures of S = 2, 4, 8, 16 species drawn at random (100 per level) are sown at equal proportions
p_i = 1/S (initial biomass K_i / S each) and run to t = 300; observed yields Y_O,i are the final biomasses.
Competition is specified in relative-yield units, b_ij = a_ij K_j / K_i (the effect of species j at its
monoculture yield on the relative growth of species i). Two communities:
  complementarity: b_ij = 0.4 for all i != j (strong niche differentiation, no competitive hierarchy: all
  species reach the same relative yield, so SE = 0);
  selection: b_ij = 0.95 (K_j / K_i)^1.5, i != j (nearly complete overlap; species with high K suppress the
  others, so the most productive species dominates the mixture);
  both: b_ij = 0.5 (K_j / K_i)^0.7 (partial niche differentiation and a hierarchy favoring productive species).
Partition (Loreau and Hector 2001): Delta Y = Y_O - Y_E = N mean(Delta RY) mean(M) + N cov(Delta RY, M), with
Delta RY_i = Y_O,i / M_i - p_i, Y_E = sum p_i M_i; the first term is the complementarity effect (CE), the
second the selection effect (SE), covariance with divisor N.
A: means of Delta Y (bars), CE (dots) and SE (diamonds) against S for the three communities.
B: CE against SE for each mixture with S = 8.
"""

import numpy as np
from scipy.integrate import solve_ivp

import wikibio as bio
from wikibio import charts as C
from wikibio import quant as Q

P = bio.P
FS = bio.core.FONT
rng = np.random.default_rng(4)
pool = 30
K = 200 * np.exp(0.5 * rng.standard_normal(pool))


def alpha(kind, k):
    ratio = k[None, :] / k[:, None]          # K_j / K_i
    if kind == "complementarity":
        b = np.full((k.size, k.size), 0.4)
    elif kind == "both":
        b = 0.5 * ratio ** 0.7
    else:
        b = 0.95 * ratio ** 1.5
    np.fill_diagonal(b, 1.0)
    return b / ratio                           # a_ij = b_ij K_i / K_j


def mixture(sub, kind):
    k = K[sub]
    a = alpha(kind, k)
    S = k.size
    f = lambda t, n: n * (k - a @ n) / k
    sol = solve_ivp(f, (0, 300), k / S, method="LSODA", rtol=1e-6, atol=1e-6)
    yo = np.maximum(sol.y[:, -1], 0)
    dry = yo / k - 1 / S
    ce = S * dry.mean() * k.mean()
    se = S * np.mean((dry - dry.mean()) * (k - k.mean()))
    return yo.sum() - k.mean(), ce, se


Ss = [2, 4, 8, 16]
res = {}
for kind in ("complementarity", "both", "selection"):
    res[kind] = {S: np.array([mixture(rng.choice(pool, S, replace=False), kind) for _ in range(100)]) for S in Ss}

fig, ax = bio.canvas(30.0, 11.0)
pa = C.axes_at(ax, (2.4, 1.6, 14.0, 7.4))
xs = np.arange(len(Ss))
toks = {"complementarity": "dna", "both": "plant", "selection": "negative"}
for j, kind in enumerate(("complementarity", "both", "selection")):
    m = np.array([res[kind][S].mean(0) for S in Ss])
    off = -0.27 + 0.27 * j
    c = Q.line_color(toks[kind])
    pa.bar(xs + off, m[:, 0], width=0.25, color=P.light(toks[kind]), edgecolor=c, lw=0.8, label=kind)
    pa.plot(xs + off - 0.05, m[:, 1], "o", color=c, ms=4.5)
    pa.plot(xs + off + 0.05, m[:, 2], "D", color=c, ms=4, mfc=P.surface())
pa.axhline(0, color=P.muted(), lw=0.8)
pa.set_xticks(xs)
pa.set_xticklabels([str(S) for S in Ss])
C.style_axes(pa, "species richness S", "effect on yield (g m⁻²)")
pa.legend(frameon=False, fontsize=FS["tiny"], labelcolor=P.ink(), loc="upper left", title="bars: net effect; dots: CE; diamonds: SE", title_fontsize=FS["tiny"])
bio.panel(ax, "A", (0.6, 10.6))
bio.label(ax, (2.4, 10.2), "Net effect = complementarity (CE) + selection (SE)", size="small", bold=True, ha="left")

pb = C.axes_at(ax, (20.4, 1.6, 8.6, 7.4))
for kind in ("complementarity", "both", "selection"):
    d = res[kind][8]
    pb.plot(d[:, 2], d[:, 1], "o", ms=3.5, color=Q.line_color(toks[kind]), alpha=0.8, label=kind)
pb.axhline(0, color=P.muted(), lw=0.7)
pb.axvline(0, color=P.muted(), lw=0.7)
C.style_axes(pb, "selection effect SE (g m⁻²)", "complementarity effect CE (g m⁻²)")
pb.legend(frameon=False, fontsize=FS["tiny"], labelcolor=P.ink(), loc="upper right")
bio.panel(ax, "B", (18.6, 10.6))
bio.label(ax, (20.4, 10.2), "Mixtures of 8 species", size="small", bold=True, ha="left")
