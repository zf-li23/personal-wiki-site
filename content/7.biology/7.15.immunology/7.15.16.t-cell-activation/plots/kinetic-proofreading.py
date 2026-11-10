# Kinetic proofreading of T-cell receptor signalling (McKeithan 1995).
# A TCR-pMHC complex must complete N sequential modification steps (rate kp each) before it signals; if the
# pMHC dissociates (rate koff = 1/tau) at any step, the TCR resets. The fraction of binding events that reach
# the signalling state is (kp tau / (1 + kp tau))^N. Illustrative kp = 1 s^-1.
# A: response per binding event versus dwell time tau for N = 0, 1, 3, 6, 10.
# B: discrimination between a ligand with tau = 3 s and one with tau = 1 s (ratio of responses), and the cost:
#    the fraction of agonist (tau = 3 s) bindings that still signal, as functions of N.
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio
from wikibio import charts

P = bio.P
KP = 1.0
tau = np.logspace(-1, 2, 300)
fig, axs = plt.subplots(1, 2, figsize=(9.8, 3.5))
toks = ["neutral", "dna", "enzyme", "protein", "negative"]
for N, tok in zip((0, 1, 3, 6, 10), toks):
    f = (KP * tau / (1 + KP * tau)) ** N
    axs[0].plot(tau, f, color=charts.line(tok), lw=1.5, label=f"N = {N}")
axs[0].axvspan(1, 3, color=P.fill("highlight"), alpha=0.3, lw=0)
axs[0].text(1.7, 2e-9, "self-like\nvs agonist", fontsize=7, color=P.ink(), ha="center", va="bottom")
axs[0].set_xscale("log")
axs[0].set_yscale("log")
axs[0].set_ylim(1e-9, 2)
axs[0].legend(frameon=False, fontsize=7, labelcolor=P.ink(), loc="lower right")
charts.style_axes(axs[0], "dwell time τ = 1/k_off / s", "fraction of bindings that signal")
charts.title(axs[0], "A")

N = np.arange(0, 16)
ratio = ((KP * 3 / (1 + KP * 3)) / (KP * 1 / (1 + KP * 1))) ** N
ax2 = axs[1]
ax2.semilogy(N, ratio, "o-", ms=3.5, color=charts.line("negative"), lw=1.4, label="discrimination, τ = 3 s vs 1 s")
ax2.semilogy(N, 3.0 ** np.ones_like(N), color=P.muted(), lw=0.8, ls="--")
ax2.text(15, 3.4, "dwell-time ratio (3×)", fontsize=7, color=P.muted(), ha="right", va="bottom")
charts.style_axes(ax2, "number of proofreading steps N", "ratio, or fraction")
ax2.semilogy(N, (KP * 3 / (1 + KP * 3)) ** N, "s-", ms=3, color=charts.line("dna"), lw=1.2,
             label="agonist bindings that signal (τ = 3 s)")
ax2.legend(frameon=False, fontsize=7, labelcolor=P.ink(), loc="upper left")
charts.title(ax2, "B")
fig.tight_layout()
