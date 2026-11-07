# Single-locus model of resistance evolution to a Bt crop with a non-Bt refuge.
# Insects mate at random across the Bt field (fraction 1 - r of the habitat) and the refuge (fraction r).
# Fitness of genotype g: w_g = r * 1 + (1 - r) * w_Bt(g); w_Bt(SS) = 0.01 (high dose),
# w_Bt(RR) = 1, w_Bt(SR) = w_SS + h (w_RR - w_SS) with h the dominance of resistance (h = 0: fully recessive). No cost of resistance.
# Initial resistance allele frequency q0 = 0.001.
# A: allele frequency over generations for a recessive resistance (h = 0) at three refuge fractions.
# B: generations until q > 0.5 as a function of refuge fraction, for h = 0, 0.1 and 0.5.
import matplotlib.pyplot as plt
import numpy as np
import wikibio as bio
from wikibio import charts

W_SS, W_RR, Q0 = 0.01, 1.0, 0.001


def step(q, r, h):
    p = 1 - q
    w_sr = W_SS + h * (W_RR - W_SS)
    w = np.array([r + (1 - r) * W_SS, r + (1 - r) * w_sr, r + (1 - r) * W_RR])
    f = np.array([p * p, 2 * p * q, q * q])
    return (w[2] * f[2] + 0.5 * w[1] * f[1]) / (w * f).sum()


def trajectory(r, h, gens):
    q = Q0
    out = [q]
    for _ in range(gens):
        q = step(q, r, h)
        out.append(q)
    return np.array(out)


def time_to_half(r, h, cap=5000):
    q = Q0
    for t in range(1, cap + 1):
        q = step(q, r, h)
        if q > 0.5:
            return t
    return cap


fig, (ax, bx) = plt.subplots(1, 2, figsize=(11, 4.2))
gens = 300
x = np.arange(gens + 1)
for r, token in [(0.0, "negative"), (0.05, "highlight"), (0.2, "plant")]:
    label = "no refuge" if r == 0 else f"refuge {int(r * 100)}%"
    ax.plot(x, trajectory(r, 0, gens), color=charts.line(token), lw=2.0, label=label)
ax.set_ylim(0, 1.03)
charts.style_axes(ax, "Generations", "Frequency of resistance allele")
ax.legend(frameon=False, fontsize=8, loc="center right")
ax.text(2, 0.93, "recessive resistance (h = 0)", fontsize=8, color=bio.P.muted())

rs = np.linspace(0, 0.5, 51)
for h, token in [(0, "plant"), (0.1, "protein"), (0.5, "negative")]:
    bx.plot(rs * 100, [time_to_half(r, h) for r in rs], color=charts.line(token), lw=2.0, label=f"h = {h}")
bx.set_yscale("log")
charts.style_axes(bx, "Refuge, share of habitat (%)", "Generations until q > 0.5")
bx.legend(frameon=False, fontsize=8, loc="upper left")
for a, letter in zip((ax, bx), "AB"):
    a.text(-0.12, 1.03, letter, transform=a.transAxes, fontsize=12, weight="bold", color=bio.P.ink())
fig.tight_layout()
