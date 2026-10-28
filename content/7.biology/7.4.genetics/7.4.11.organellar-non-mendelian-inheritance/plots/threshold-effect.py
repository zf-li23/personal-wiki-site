"""Threshold effect of a heteroplasmic mtDNA mutation (illustrative model).
(A) Residual respiratory-chain activity of a tissue as a function of its mutant fraction h, modelled as a steep
logistic drop at a tissue-specific biochemical threshold (brain 0.6, skeletal muscle 0.75, blood 0.85; values
illustrative). (B) Children of a mother with h0 = 0.5 for a mutation like m.8993T>G (ATP6), with a germline
bottleneck of N = 20 units: exact binomial distribution of the children's heteroplasmy, colored by the expected
clinical class (below 0.7 usually unaffected, 0.7-0.9 milder disease, above 0.9 severe early-onset disease)."""

import numpy as np
from scipy.stats import binom

import wikibio as bio
from wikibio import charts

P = bio.P
FT = bio.core.FONT

fig, ax = bio.canvas(16.0, 7.6)
bio.panel(ax, "A", (0.1, 7.5))
a = charts.axes_at(ax, (1.7, 1.3, 5.8, 5.6))
h = np.linspace(0, 1, 400)
for th, tok, name in ((0.6, "neuron", "brain"), (0.75, "positive", "muscle"), (0.85, "dna", "blood")):
    act = 1 / (1 + np.exp((h - th) / 0.035))
    a.plot(h, act, color=charts.line(tok), lw=1.7, label=f"{name}, threshold {th}")
a.plot(h, 1 - h, color=P.muted(), ls=":", lw=1.0, label="proportional (1 - h)")
a.set_xlim(0, 1)
a.set_ylim(0, 1.05)
a.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="lower left")
charts.style_axes(a, "mutant mtDNA fraction h", "relative OXPHOS activity")

bio.panel(ax, "B", (8.3, 7.5))
b = charts.axes_at(ax, (9.9, 1.3, 5.8, 5.6))
N, h0 = 20, 0.5
k = np.arange(N + 1)
pk = binom.pmf(k, N, h0)
hk = k / N
cls = np.where(hk >= 0.9, "negative", np.where(hk >= 0.7, "highlight", "channel"))
for x, y, c in zip(hk, pk, cls):
    b.bar(x, y, width=0.04, color=charts.line(c))
p_low = pk[hk < 0.7].sum()
p_mid = pk[(hk >= 0.7) & (hk < 0.9)].sum()
p_hi = pk[hk >= 0.9].sum()
for x, s, c in ((0.25, f"unaffected\n{p_low:.3f}", "channel"), (0.78, f"milder\n{p_mid:.3f}", "highlight"),
                (0.95, f"severe\n{p_hi:.5f}", "negative")):
    b.text(x, 0.19, s, fontsize=FT["tiny"], color=charts.line(c), ha="center", va="bottom")
b.axvline(h0, color=P.muted(), ls=":", lw=0.9)
b.set_xlim(-0.03, 1.03)
b.set_ylim(0, 0.24)
charts.style_axes(b, "child's heteroplasmy h (mother 0.5, N = 20)", "probability")
