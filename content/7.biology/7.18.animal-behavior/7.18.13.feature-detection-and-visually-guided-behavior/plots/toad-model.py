"""Worm, antiworm and square: Ewert's dummy experiments and a two-channel model.

Stimuli: black bars 2.5 deg wide moved horizontally at constant speed; the edge length L
(2-32 deg) is either parallel to the direction of motion (worm), perpendicular to it
(antiworm), or both edges are L (square). Model (after Ewert's interpretation):
T5(1) tectal neurons sum the extension along the direction of motion (and weakly across it);
TP3 pretectal neurons respond to extension across the direction of motion and to large
objects; T5(2) neurons, the putative prey detectors, are excited by T5(1) and inhibited by TP3.
Behavioral prey-catching rate is taken to be proportional to T5(2). Units are arbitrary;
curve shapes follow the published dummy experiments qualitatively.
"""
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio

P = bio.P
L = np.geomspace(2.5, 32, 60)
w = 2.5


def t51(par, perp):
    return 40 * (1 - np.exp(-(par + 0.5 * perp) / 14))


def tp3(par, perp):
    return 40 * (1 - np.exp(-(perp ** 1.6) * (1 + 0.02 * par) / 60))


def t52(par, perp, k=1.0):
    return np.maximum(0, t51(par, perp) - k * tp3(par, perp))


stim = {"worm": (L, np.full_like(L, w)), "antiworm": (np.full_like(L, w), L), "square": (L, L)}
col = {"worm": P.edge("positive"), "antiworm": P.edge("negative"), "square": P.edge("dna")}
fig, axs = plt.subplots(1, 3, figsize=(11.5, 3.7), sharex=True)
for name, (par, perp) in stim.items():
    axs[0].plot(L, t51(par, perp), color=col[name], lw=2, label=name)
    axs[0].plot(L, tp3(par, perp), color=col[name], lw=1.3, ls="--")
    axs[1].plot(L, t52(par, perp), color=col[name], lw=2, label=name)
    axs[2].plot(L, t52(par, perp, k=0.0), color=col[name], lw=2, label=name)
axs[0].text(20, 6, "dashed: TP3\n(pretectum)", fontsize=7.5, color=P.muted())
axs[0].text(3, 37, "solid: T5(1) (tectum)", fontsize=7.5, color=P.muted())
axs[0].set_title("A  Input channels", loc="left", fontweight="bold", fontsize=10)
axs[1].set_title("B  T5(2) = T5(1) − TP3 ≈ prey catching", loc="left", fontweight="bold", fontsize=10)
axs[2].set_title("C  After a pretectal lesion", loc="left", fontweight="bold", fontsize=10)
for ax in axs:
    ax.set_xscale("log")
    ax.set_xticks([2.5, 4, 8, 16, 32]); ax.set_xticklabels(["2.5", "4", "8", "16", "32"])
    ax.set_xlabel("Edge length L / deg")
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
axs[0].set_ylabel("Response (arbitrary units)")
axs[1].legend(frameon=False, fontsize=8, loc="upper left")
# icons of the three stimuli in panel B
for i, (name, (wd, ht)) in enumerate((("worm", (0.12, 0.025)), ("antiworm", (0.025, 0.12)), ("square", (0.07, 0.07)))):
    x0, y0 = 0.62 + 0.13 * i, 0.82
    axs[1].add_patch(plt.Rectangle((x0, y0), wd, ht, transform=axs[1].transAxes, color=col[name]))
    axs[1].annotate("", (x0 + 0.1, y0 - 0.05), (x0, y0 - 0.05), xycoords="axes fraction",
                    arrowprops=dict(arrowstyle="->", color=P.muted(), lw=0.8))
fig.tight_layout()
