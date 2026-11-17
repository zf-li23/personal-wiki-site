"""Fire regimes with a constant hazard.

A: if every patch burns with constant probability 1/F per year (F = fire cycle), time since fire is exponential:
the fraction of the landscape not burned for at least a years is exp(-a/F); simulated landscape of 5000 patches
over 2000 years for F = 30, 100 and 300 years, with the exponential curves.
B: an obligate seeder (adults killed by fire, recruitment only from seeds released by fire) persists through the
next fire only if that fire comes after the juvenile period J and before the seed bank or the adults are lost
(age L): P = exp(-J/F) - exp(-L/F). Two life histories: a short-lived shrub (J = 5, L = 50 years) and a serotinous
pine (J = 15, L = 250 years). Dots mark the optimum F* = (L - J) / ln(L/J).
"""
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio

P = bio.P
rng = np.random.default_rng(0)
fig, (ax, bx) = plt.subplots(1, 2, figsize=(12.0, 4.6))
a = np.linspace(0, 600, 300)
for F, tok in ((30, "negative"), (100, "highlight"), (300, "plant")):
    age = np.zeros(5000)
    for _ in range(2000):
        age += 1
        age[rng.random(5000) < 1 / F] = 0
    frac = np.array([(age >= x).mean() for x in a])
    ax.plot(a, frac, color=P.edge(tok), lw=0, marker="o", ms=2.2, alpha=0.6)
    ax.plot(a, np.exp(-a / F), color=P.edge(tok), lw=1.8, label=f"fire cycle $F$ = {F} yr")
ax.set_xlim(0, 600)
ax.set_ylim(0, 1.02)
ax.set_xlabel("time since last fire $a$ / yr")
ax.set_ylabel("fraction of landscape unburned for $\\geq a$")
ax.legend(frameon=False, fontsize=8)
ax.set_title("A  Stand-age distribution (dots: simulation)", loc="left", fontsize=10)

F = np.logspace(0, 3.5, 400)
for J, L, tok, lab in ((5, 50, "rna", "shrub: $J$ = 5, $L$ = 50 yr"),
                       (15, 250, "plant", "serotinous pine: $J$ = 15, $L$ = 250 yr")):
    p = np.exp(-J / F) - np.exp(-L / F)
    bx.plot(F, p, color=P.edge(tok), lw=2.0, label=lab)
    fs = (L - J) / np.log(L / J)
    bx.plot(fs, np.exp(-J / fs) - np.exp(-L / fs), "o", color=P.edge(tok), ms=5)
bx.text(1.15, 0.45, "immaturity risk:\nfires too frequent", fontsize=8, color=P.muted())
bx.text(600, 0.5, "senescence risk:\nfires too rare", fontsize=8, color=P.muted())
bx.set_xscale("log")
bx.set_xlim(1, 3000)
bx.set_ylim(0, 1)
bx.set_xlabel("mean fire interval $F$ / yr")
bx.set_ylabel("probability the population survives one fire cycle")
bx.legend(frameon=False, fontsize=8, loc="upper left")
bx.set_title("B  The fire-interval window of an obligate seeder", loc="left", fontsize=10)
for x in (ax, bx):
    for s in ("top", "right"):
        x.spines[s].set_visible(False)
fig.tight_layout()
