"""Selection of tip and stalk cells by VEGF-Dll4-Notch lateral inhibition (Formula 29.3.1). A: steady states of a
row of 20 endothelial cells (colour: Dll4 level, high = tip-cell fate, gold; low = stalk cell, pink) at three
levels of VEGF signalling G. Low VEGF: no cell is activated enough to make Dll4, no sprouting. Intermediate VEGF:
alternating tip and stalk cells. Very high VEGF: every cell makes Dll4, Notch is high everywhere but cannot
overcome the signal, and all cells adopt the tip state; the pattern is lost. B: the contrast between neighbouring
cells (maximum minus minimum Dll4) against G: patterning occurs in a window of VEGF levels."""
import numpy as np
import wikibio as bio
from wikibio import quant

P = bio.P


def run(G, N=20, T=200, dt=0.05, seed=0, n=2, h=4, k=0.3):
    """Steady Dll4 levels of a ring of N cells; G may be an array (one row per value)."""
    G = np.atleast_1d(np.asarray(G, float))[:, None]
    rng = np.random.default_rng(seed)
    D = 0.5 + 0.01 * rng.standard_normal((1, N)).repeat(len(G), 0)
    Nt = 0.5 * np.ones_like(D)
    for _ in range(int(T / dt)):
        R = G / (1 + (Nt / k) ** h)
        D = D + dt * (R**n / (1 + R**n) - D)
        Nt = Nt + dt * ((np.roll(D, 1, axis=1) + np.roll(D, -1, axis=1)) / 2 - Nt)
    return D


fig, ax = bio.canvas(24, 8.5)
bio.panel(ax, "A", (0.2, 8.3))
for j, (G, txt) in enumerate(((0.5, "low VEGF (G = 0.5)"), (5.0, "intermediate VEGF (G = 5)"), (300.0, "very high VEGF (G = 300)"))):
    D = run(G)[0]
    y = 6.6 - 2.4 * j
    x0, x1 = 0.8, 11.0
    w = (x1 - x0) / len(D)
    for i, d in enumerate(D):
        col = P.mix(P.fill("rrna"), P.fill("atp"), float(np.clip(d, 0, 1)))
        ax.add_patch(bio.core.FancyBboxPatch((x0 + i * w + 0.03, y - 0.35), w - 0.06, 0.7, boxstyle="round,pad=0,rounding_size=0.12",
                                             facecolor=col, edgecolor=P.edge("rrna"), lw=0.6, zorder=5))
    bio.label(ax, (x0, y + 0.75), txt, size="small", ha="left")
bio.box(ax, (2.0, 0.5), 0.5, 0.35, "atp")
bio.label(ax, (2.4, 0.5), "high Dll4: tip", size="tiny", ha="left")
bio.box(ax, (6.0, 0.5), 0.5, 0.35, "rrna")
bio.label(ax, (6.4, 0.5), "low Dll4: stalk", size="tiny", ha="left")

bio.panel(ax, "B", (12.6, 8.3))
Gs = np.logspace(-1, 3, 50)
amp = np.ptp(run(Gs), axis=1)
pl = quant.Plot(ax, (14.4, 1.4, 9.0, 6.0), xlim=(-1, 3), ylim=(0, 1.05), xlabel="log10 VEGF signal G", ylabel="Dll4 contrast",
                xticks=[-1, 0, 1, 2, 3], yticks=[0, 0.5, 1])
pl.line(np.log10(Gs), amp, "enzyme")
pl.span(np.log10(Gs[amp > 0.1].min()), np.log10(Gs[amp > 0.1].max()), "highlight", text="tip/stalk pattern", strength=0.35)
