# Two population-genetic sides of domestication (deterministic models).
# A: spread of a non-shattering allele a under unconscious selection by harvesting and re-sowing.
#    Plants that keep their grain contribute more seed to the next sowing: fitness 1 + s for
#    non-shattering plants (s = 0.03), 1 otherwise. Genotype frequencies with inbreeding coefficient F:
#    AA = p^2 (1 - F) + p F, Aa = 2 p q (1 - F), aa = q^2 (1 - F) + q F. Starting frequency q0 = 0.01.
#    A recessive allele in an outcrossing population (F = 0) spreads extremely slowly at first because
#    it is hidden in heterozygotes; predominant selfing (F = 0.9, as in rice) exposes it.
# B: fraction of neutral heterozygosity retained after a bottleneck of N_b plants lasting d generations,
#    H/H0 = (1 - 1/(2 N_b))^d, approximately exp(-d / (2 N_b)), for three durations.
import matplotlib.pyplot as plt
import numpy as np
import wikibio as bio
from wikibio import charts

s = 0.03


def trajectory(dominance, F, q0=0.01, gens=3000):
    q = q0
    out = np.empty(gens)
    for t in range(gens):
        p = 1 - q
        aa = q * q * (1 - F) + q * F
        het = 2 * p * q * (1 - F)
        AA = 1 - aa - het
        w_aa, w_het = 1 + s, (1 + s) if dominance == "dominant" else (1 + s / 2 if dominance == "additive" else 1.0)
        wbar = AA + het * w_het + aa * w_aa
        q = (aa * w_aa + 0.5 * het * w_het) / wbar
        out[t] = q
    return out


fig, (ax, bx) = plt.subplots(1, 2, figsize=(11, 4.2))
gens = np.arange(1, 3001)
cases = [("dominant", 0.0, "dominant, outcrossing", "plant", "-"),
         ("additive", 0.0, "additive, outcrossing", "protein", "-"),
         ("recessive", 0.0, "recessive, outcrossing", "negative", "-"),
         ("recessive", 0.9, "recessive, selfing (F = 0.9)", "highlight", "--")]
for dom, F, name, token, ls in cases:
    ax.plot(gens, trajectory(dom, F), color=charts.line(token), lw=2.0, ls=ls, label=name)
ax.set_xscale("log")
ax.set_xlim(1, 3000)
ax.set_ylim(0, 1.03)
charts.style_axes(ax, "Generations (years) of harvesting", "Frequency of non-shattering allele")
ax.legend(frameon=False, fontsize=8, loc="upper left")
ax.text(1.3, 0.55, f"s = {s}", fontsize=8, color=bio.P.muted())

nb = np.logspace(1, 5, 300)
for d, token in [(100, "plant"), (1000, "protein"), (3000, "negative")]:
    bx.plot(nb, (1 - 1 / (2 * nb)) ** d, color=charts.line(token), lw=2.0, label=f"d = {d} generations")
bx.set_xscale("log")
bx.set_ylim(0, 1.03)
bx.axhline(0.5, color=bio.P.muted(), lw=0.8, ls=":")
charts.style_axes(bx, "Bottleneck size N$_b$ (plants)", "Heterozygosity retained, H/H$_0$")
bx.legend(frameon=False, fontsize=8, loc="lower right")
for a, letter in zip((ax, bx), "AB"):
    a.text(-0.12, 1.03, letter, transform=a.transAxes, fontsize=12, weight="bold", color=bio.P.ink())
fig.tight_layout()
