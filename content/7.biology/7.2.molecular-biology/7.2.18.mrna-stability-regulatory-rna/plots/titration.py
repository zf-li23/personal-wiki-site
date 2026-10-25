# Catalytic versus stoichiometric repression by a small regulatory RNA (dimensionless model).
# Target mRNA (total T, free t) is made at rate alpha and decays at rate beta = 1; the regulator (total R, free
# r) is made at rate alpha_r = 10 and decays at delta = 1; they bind rapidly with dissociation constant K
# (c = t r / K), and the complex is degraded at gamma = 10. Catalytic regulator (miRNA-like, RISC recycled):
# the regulator survives degradation of its target (K = 50: about threefold repression at all alpha). Stoichiometric regulator (bacterial sRNA-like, co-degraded
# with its target by RNase E): the regulator is destroyed with the target, so it is titrated away.
# Steady state: alpha = beta t + gamma c and, for the stoichiometric case, alpha_r = delta r + gamma c.
# A: free target against target transcription rate: catalytic repression lowers the slope; stoichiometric
# repression with tight binding (K = 0.1) gives a threshold-linear response, with almost no free target until
# alpha exceeds alpha_r, and a weaker regulator (K = 10) smooths the threshold.
# B: fold repression (unregulated / regulated free target) for the same cases.
import numpy as np
from scipy.optimize import brentq
import wikibio as bio
from wikibio import quant as Q

P = bio.P
fig, ax = bio.canvas(24.0, 9.0)
beta, delta, gamma, ar = 1.0, 1.0, 10.0, 10.0
alphas = np.linspace(0.05, 30, 300)


def free_target(alpha, K, stoich):
    # unknown t; c and r follow from the steady-state relations
    def c_of(t):
        if stoich:
            # r from alpha_r = delta r + gamma c, c = t r / K -> r = ar / (delta + gamma t / K)
            r = ar / (delta + gamma * t / K)
        else:
            r = ar / delta
        return t * r / K

    f = lambda t: beta * t + gamma * c_of(t) - alpha
    return brentq(f, 0.0, alpha / beta + 1e-9)


bio.panel(ax, "A", (0.1, 8.85))
pa = Q.Plot(ax, (1.8, 1.6, 8.6, 6.6), xlim=(0, 30), ylim=(0, 30), xlabel="target transcription rate α (units of β)",
            ylabel="free target mRNA", xticks=[0, 10, 20, 30], yticks=[0, 10, 20, 30])
pa.line(alphas, alphas / beta, "neutral", dashed=True)
pa.text(26, 28.5, "no regulator", token="neutral", ha="right")
cat = np.array([free_target(a, 50.0, False) for a in alphas])
pa.line(alphas, cat, "dna")
pa.text(29.5, cat[-1] + 1.6, "catalytic (K = 50)", token="dna", ha="right")
for K, tok, dash, ytxt in ((0.1, "negative", False, -2.6), (10.0, "rna", True, 1.4)):
    st = np.array([free_target(a, K, True) for a in alphas])
    pa.line(alphas, st, tok, dashed=dash)
    pa.text(29.5 if K < 1 else 9.4, 3.0 if K < 1 else 13.0, f"stoichiometric (K = {K:g})", token=tok, ha="right")
pa.vline(ar, text=r"$\alpha = \alpha_{\mathrm{r}}$", top=True)

bio.panel(ax, "B", (12.6, 8.85))
pb = Q.Plot(ax, (14.4, 1.6, 8.6, 6.6), xlim=(0.05, 30), ylim=(1, 1e4), ylog=True, xlabel="α (units of β)",
            ylabel="fold repression", xticks=[0, 10, 20, 30], yticks=[(1, "1"), (10, "10"), (100, "100"), (1000, "10³"), (1e4, "10⁴")])
pb.line(alphas, alphas / cat, "dna", text="catalytic", at=0.8, dy=0.35)
for K, tok, dash, at in ((0.1, "negative", False, 0.2), (10.0, "rna", True, 0.12)):
    st = np.array([free_target(a, K, True) for a in alphas])
    pb.line(alphas, np.clip(alphas / np.maximum(st, 1e-12), 1, 1e4), tok, dashed=dash, text=f"stoich., K = {K:g}", at=at, dy=0.35)
pb.vline(ar)
