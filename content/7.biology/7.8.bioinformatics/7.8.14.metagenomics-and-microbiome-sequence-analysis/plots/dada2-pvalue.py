# The abundance p-value of DADA2 for a sequence one substitution away from a more abundant sequence. With
# 250-nt reads at quality Q35, the probability that a read of the parent is converted into this specific
# variant is lambda = (10^-3.5 / 3)(1 - 10^-3.5)^249 = 9.7e-5. If the variant were produced by errors alone,
# its count would be Poisson with mean A * lambda for parent abundance A; the p-value is
# P(X >= a | X >= 1). A: p-value against the observed abundance a of the variant for parents of 10^3, 10^4 and
# 10^5 reads; DADA2's default threshold OMEGA_A = 1e-40 (dashed) declares the variant a new sequence when its
# p-value falls below it, at a = 22, 35 and 76 reads respectively. B: the same threshold as a minimum
# abundance: about 12 reads even for small parents, growing roughly linearly with the expected number of error
# copies once A * lambda >> 1.
import numpy as np
from scipy import stats
import wikibio as bio
from wikibio import charts as C

P = bio.P
lam = 10 ** -3.5 / 3 * (1 - 10 ** -3.5) ** 249
fig, ax = bio.canvas(28.0, 10.4)
a = C.axes_at(ax, (2.2, 1.6, 11.6, 7.8))
toks = ["dna", "enzyme", "rna"]
for A, tok in zip((1e3, 1e4, 1e5), toks):
    mu = A * lam
    k = np.arange(1, 121)
    lp = (stats.poisson.logsf(k - 1, mu) - stats.poisson.logsf(0, mu)) / np.log(10)
    a.plot(k, lp, color=C.line(tok), lw=1.5, label=f"parent {int(A):,} reads (expected {mu:.2f} error copies)")
    kmin = k[np.argmax(lp < -40)]
    a.plot([kmin], [lp[kmin - 1]], "o", color=C.line(tok), ms=4)
    a.text(kmin + 2, lp[kmin - 1] + 3, f"{kmin}", fontsize=bio.core.FONT["tiny"], color=P.ink())
a.axhline(-40, color=P.muted(), lw=0.9, ls=(0, (3, 2)))
a.text(85, -37, "OMEGA_A = 1e-40", fontsize=bio.core.FONT["tiny"], color=P.ink())
a.set_ylim(-140, 2)
a.set_xlim(0, 120)
C.style_axes(a, "reads of the one-substitution variant (a)", "log10 abundance p-value")
a.legend(fontsize=bio.core.FONT["tiny"], frameon=False, labelcolor=P.ink(), loc="lower left")
b = C.axes_at(ax, (17.4, 1.6, 9.8, 7.8))
As = np.logspace(1, 6, 60)
kmins = []
for A in As:
    mu = A * lam
    k = np.arange(1, 3000)
    lp = (stats.poisson.logsf(k - 1, mu) - stats.poisson.logsf(0, mu)) / np.log(10)
    kmins.append(k[np.argmax(lp < -40)])
b.loglog(As, kmins, color=C.line("protein"), lw=1.6, label="minimum a for a new ASV")
b.loglog(As, As * lam, color=P.muted(), lw=1.0, ls=(0, (3, 2)), label="expected error copies A * lambda")
b.set_ylim(0.01, 2000)
C.style_axes(b, "parent abundance A (reads)", "reads")
b.legend(fontsize=bio.core.FONT["tiny"], frameon=False, labelcolor=P.ink(), loc="upper left")
bio.panel(ax, "A", (0.3, 10.0))
bio.panel(ax, "B", (15.6, 10.0))
