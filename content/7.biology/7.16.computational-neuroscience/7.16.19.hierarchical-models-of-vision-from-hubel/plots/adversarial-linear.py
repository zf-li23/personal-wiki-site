"""Why high-dimensional linear models are vulnerable to small adversarial perturbations.

A linear unit z = w . x with ||w||_2 = 1 and i.i.d. Gaussian weights in n dimensions. A perturbation
eta with |eta_i| <= eps (L-infinity budget) changes z by w . eta.
 - adversarial (fast gradient sign): eta = -eps sign(w) gives a change of -eps ||w||_1 ~ -eps sqrt(2n/pi);
 - random signs: eta = eps * (random +-1) gives a change of standard deviation eps ||w||_2 = eps.
A: the per-pixel budget eps needed to move z by a margin of 1 (a typical distance from the decision
boundary), against n. B: distribution of the change in z for n = 784 (a 28 x 28 image) and eps = 0.05.
"""
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio

P = bio.P
rng = np.random.default_rng(11)
ns = np.logspace(1, 5, 30).astype(int)
eps_adv, eps_rand = [], []
for n in ns:
    w = rng.normal(size=n)
    w /= np.linalg.norm(w)
    eps_adv.append(1 / np.abs(w).sum())
    eps_rand.append(1.0)

fig, axs = plt.subplots(1, 2, figsize=(11, 4.0))
ax = axs[0]
ax.plot(ns, eps_adv, "o-", color=P.edge("negative"), ms=3.5, lw=1.6, label="adversarial (sign of gradient)")
ax.plot(ns, np.sqrt(np.pi / (2 * ns)), color=P.muted(), lw=1, ls=":", label="sqrt(pi / 2n)")
ax.plot(ns, eps_rand, color=P.edge("dna"), lw=1.6, label="random signs (1 SD)")
ax.set_xscale("log")
ax.set_yscale("log")
ax.set_xlabel("Input dimension n")
ax.set_ylabel("Per-component budget eps for a unit change")
ax.legend(frameon=False, fontsize=8, loc="lower left")
ax.set_title("A  The adversarial budget shrinks as 1/sqrt(n)", loc="left", fontsize=10)

bx = axs[1]
n, eps = 784, 0.05
w = rng.normal(size=n)
w /= np.linalg.norm(w)
rand = np.array([w @ (eps * rng.choice([-1, 1], n)) for _ in range(5000)])
adv = -eps * np.abs(w).sum()
bx.hist(rand, bins=50, color=P.fill("dna"), edgecolor=P.edge("dna"), lw=0.4, label="5000 random perturbations")
bx.axvline(adv, color=P.edge("negative"), lw=2, label=f"adversarial: {adv:.2f}")
bx.set_xlabel("Change of the unit's input w . eta")
bx.set_ylabel("Count")
bx.legend(frameon=False, fontsize=8, loc="upper left")
bx.set_title("B  n = 784, eps = 0.05 per pixel", loc="left", fontsize=10)
fig.tight_layout()
