# Transcriptional bursting: the two-state (telegraph) model simulated with the Gillespie algorithm.
#   gene OFF -> ON at k_on, ON -> OFF at k_off; mRNA made at rate r while ON; each mRNA degraded at gamma = 1
#   (time in units of the mRNA lifetime).
# Constitutive gene (Poisson): always ON, r = 20. Bursty gene: k_on = 0.5, k_off = 20, r = 800, i.e. bursts
# of mean size b = r / k_off = 40 transcripts arriving at frequency about k_on, mean <m> = k_on r / ((k_on +
# k_off) gamma) = 19.5, almost the same as the constitutive gene.
# A: trajectories of mRNA number for the two genes (the bursty gene's ON periods marked by ticks).
# B: steady-state distributions from long simulations (bars) with theory: Poisson(20) for the constitutive
#    gene and, for the bursty gene, the negative binomial of the bursty limit (shape k_on / gamma, mean
#    <m>), whose Fano factor is 1 + b.
# C: Fano factor sigma^2 / <m> against mean burst size b = r / k_off for a family with k_off = 50 and k_on
#    adjusted to keep <m> = 20. Points: simulations; line: exact result for the telegraph model,
#    F = 1 + r k_off / ((k_on + k_off)(k_on + k_off + gamma)); dashed: the bursty limit F = 1 + b.
import math
import random

import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import nbinom, poisson

import wikibio as bio
from wikibio import charts

P = bio.P
rnd = random.Random(0)
GAMMA = 1.0


def telegraph(kon, koff, r, t_end, always_on=False, record=False, burn=20.0):
    """Gillespie simulation; returns the time-weighted histogram of m (and a trajectory if record)."""
    on, m, t = True, 0, 0.0
    hist = {}
    traj = [(0.0, 0, on)] if record else None
    while t < t_end:
        a_sw = 0.0 if always_on else (koff if on else kon)
        a_tx = r if on else 0.0
        a_dg = GAMMA * m
        a0 = a_sw + a_tx + a_dg
        dt = -math.log(1.0 - rnd.random()) / a0
        if t + dt > burn:
            w = min(t + dt, t_end) - max(t, burn)
            if w > 0:
                hist[m] = hist.get(m, 0.0) + w
        t += dt
        u = rnd.random() * a0
        if u < a_sw:
            on = not on
        elif u < a_sw + a_tx:
            m += 1
        else:
            m -= 1
        if record:
            traj.append((t, m, on))
    ks = np.array(sorted(hist))
    ws = np.array([hist[k] for k in ks])
    return ks, ws / ws.sum(), traj


fig, axs = plt.subplots(1, 3, figsize=(13.4, 3.9), gridspec_kw={"width_ratios": [1.4, 1.0, 1.0]})

# --- A ---
ax = axs[0]
_, _, tc = telegraph(0, 0, 20.0, 60.0, always_on=True, record=True, burn=0.0)
_, _, tb = telegraph(0.5, 20.0, 800.0, 60.0, record=True, burn=0.0)
for tr, tok, name in ((tc, "dna", "constitutive"), (tb, "negative", "bursty")):
    tt = np.array([p[0] for p in tr])
    mm = np.array([p[1] for p in tr])
    ax.step(tt, mm, where="post", color=charts.line(tok), lw=1.0, label=name)
ton = [p[0] for p in tb if p[2]]
ax.plot(ton, np.full(len(ton), -4), "|", color=charts.line("negative"), ms=4)
ax.set_xlim(10, 60)
ax.set_ylim(-7, 150)
ax.legend(fontsize=7, frameon=False, loc="upper right")
charts.style_axes(ax, "t / mRNA lifetimes", "mRNA molecules per cell")
ax.set_title("A   Same mean, different dynamics", loc="left", fontsize=9, color=P.ink())

# --- B ---
ax = axs[1]
kc, pc, _ = telegraph(0, 0, 20.0, 3000.0, always_on=True)
kb, pb, _ = telegraph(0.5, 20.0, 800.0, 3000.0)
ax.bar(kc, pc, width=1.0, color=P.fill("dna"), edgecolor="none", alpha=0.75, label="constitutive")
ax.bar(kb, pb, width=1.0, color=P.fill("negative"), edgecolor="none", alpha=0.75, label="bursty")
x = np.arange(0, 120)
ax.plot(x, poisson.pmf(x, 20), color=charts.line("dna"), lw=1.3)
mean_b = 0.5 * 800 / (20.5 * GAMMA)
shape = 0.5 / GAMMA
ax.plot(x, nbinom.pmf(x, shape, shape / (shape + mean_b)), color=charts.line("negative"), lw=1.3)
fano_c = np.sum(kc ** 2 * pc) / np.sum(kc * pc) - np.sum(kc * pc)
fano_b = np.sum(kb ** 2 * pb) / np.sum(kb * pb) - np.sum(kb * pb)
ax.text(45, 0.07, f"Fano: {fano_c:.2f} (Poisson: 1)", fontsize=7, color=charts.line("dna"))
ax.text(45, 0.058, f"Fano: {fano_b:.0f} (exact 37; 1 + b = 41)", fontsize=7, color=charts.line("negative"))
ax.set_xlim(0, 110)
ax.set_ylim(0, 0.1)
ax.legend(fontsize=7, frameon=False, loc="upper right")
charts.style_axes(ax, "mRNA molecules per cell", "probability")
ax.set_title("B   Poisson and negative binomial", loc="left", fontsize=9, color=P.ink())

# --- C ---
ax = axs[2]
KOFF, M = 50.0, 20.0
bs = np.array([1, 2, 5, 10, 20, 40])
fs = []
for b in bs:
    r = b * KOFF
    kon = M * KOFF / (r - M)
    k, p, _ = telegraph(kon, KOFF, r, 1500.0)
    mu = np.sum(k * p)
    fs.append((np.sum(k ** 2 * p) - mu ** 2) / mu)
bb = np.linspace(0.5, 45, 200)
r = bb * KOFF
kon = M * KOFF / (r - M)
exact = 1 + r * KOFF / ((kon + KOFF) * (kon + KOFF + GAMMA))
ok = r > M
ax.plot(bb[ok], exact[ok], color=charts.line("negative"), lw=1.6, label="telegraph model, exact")
ax.plot(bb, 1 + bb, color=P.muted(), lw=1.0, ls=(0, (4, 2.4)), label="bursty limit 1 + b")
ax.plot(bs, fs, "o", color=charts.line("negative"), ms=5, label="Gillespie simulation")
ax.axhline(1, color=P.muted(), lw=0.6, ls=":")
ax.set_xlim(0, 45)
ax.set_ylim(0, 48)
ax.legend(fontsize=7, frameon=False, loc="upper left")
charts.style_axes(ax, "mean burst size b = r / k_off", "Fano factor σ² / ⟨m⟩")
ax.set_title("C   Noise grows with burst size", loc="left", fontsize=9, color=P.ink())
fig.tight_layout()
