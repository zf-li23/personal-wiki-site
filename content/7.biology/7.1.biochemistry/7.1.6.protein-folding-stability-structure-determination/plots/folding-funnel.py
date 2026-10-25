"""A: cross-section of a rugged folding funnel (schematic): free energy against a conformational
coordinate; the width at each level stands for the number of conformations (entropy).
B: biased versus random search in a simple model (after Zwanzig, Szabo and Bagchi, 1992): each of
N = 100 residues is native or in one of nu = 2 non-native conformations; a non-native residue becomes
native at k0 = 1e9 s^-1, and native residues are favoured by U per residue, so the per-residue
equilibrium constant is K = nu exp(-U/RT). The mean first-passage time from the fully non-native
chain to the native state is computed exactly for this birth-death chain."""

import numpy as np
from scipy.special import gammaln
import wikibio as bio
from wikibio import charts

P = bio.P
fig, ax = bio.canvas(20.0, 8.0)

# A: funnel cross-section
bio.panel(ax, "A", (0.1, 7.9))
pa = charts.axes_at(ax, (1.0, 1.0, 8.0, 6.2))
x = np.linspace(-1, 1, 1200)
rng = np.random.default_rng(3)
rug = sum(a * np.sin(f * np.pi * x + ph) for a, f, ph in zip(rng.uniform(0.25, 0.6, 6), (7, 11, 17, 23, 31, 41),
                                                            rng.uniform(0, 6.3, 6)))
G = 10 * np.abs(x) ** 0.8 + rug * (0.3 + 0.7 * np.abs(x))
trap = 1.2 * np.exp(-((x - 0.55) / 0.05) ** 2)
G = G - 2.8 * trap
pa.fill_between(x, G, 12, color=P.mix(P.fill("protein"), P.surface(), 0.65), lw=0)
pa.plot(x, G, color=charts.line("protein"), lw=1.4)
i0 = np.argmin(np.abs(x))
pa.plot(0, G[i0], "o", ms=6, color=charts.line("positive"))
pa.annotate("native state N", (0, G[i0]), (0.18, -0.9), fontsize=bio.core.FONT["tiny"], color=P.ink(),
            arrowprops=dict(arrowstyle="-", color=P.muted(), lw=0.6))
it = np.argmin(np.where(np.abs(x - 0.55) < 0.08, G, 99))
pa.plot(x[it], G[it], "o", ms=5, color=charts.line("negative"))
pa.annotate("kinetic trap\n(misfolded, may aggregate)", (x[it], G[it]), (0.6, 0.7), fontsize=bio.core.FONT["tiny"],
            color=P.ink(), arrowprops=dict(arrowstyle="-", color=P.muted(), lw=0.6))
pa.annotate("", (-0.95, 9.6), (0.95, 9.6), arrowprops=dict(arrowstyle="<->", color=P.muted(), lw=0.8))
pa.text(0, 10.0, "unfolded ensemble: many conformations, high entropy", fontsize=bio.core.FONT["tiny"], color=P.ink(),
        ha="center")
pa.text(-0.98, -0.6, "molten globule:\ncompact, native-like\nsecondary structure", fontsize=bio.core.FONT["tiny"],
        color=P.ink())
pa.annotate("", (-0.12, 1.4), (-0.7, 7.6), arrowprops=dict(arrowstyle="->", color=P.ink(), lw=1.0))
pa.annotate("", (-0.42, 4.3), (-0.72, 1.3), arrowprops=dict(arrowstyle="-", color=P.muted(), lw=0.6))
pa.set_xlim(-1, 1)
pa.set_ylim(-2.5, 11)
pa.set_xticks([])
pa.set_yticks([])
charts.style_axes(pa, "conformational coordinate (width ~ number of conformations)", "free energy G")
charts.title(pa, "Folding funnel (cross-section)")

# B: biased search
bio.panel(ax, "B", (10.6, 7.9))
pb = charts.axes_at(ax, (12.0, 1.3, 7.4, 5.9), yscale="log")


def mfpt(N, K, k0=1e9):
    j = np.arange(N + 1)
    lp = gammaln(N + 1) - gammaln(j + 1) - gammaln(N - j + 1) + j * np.log(K)
    tail = np.logaddexp.accumulate(lp[::-1])[::-1]
    m = np.arange(1, N + 1)
    return np.sum(np.exp(tail[1:] - lp[1:]) / (m * k0))


U = np.linspace(0, 5, 101)
tau = np.array([mfpt(100, 2 * np.exp(-u)) for u in U])
pb.plot(U, tau, color=charts.line("protein"), lw=1.8)
for yv, txt in ((3.15e7 * 13.8e9, "age of the universe"), (1.0, "1 s"), (1e-3, "1 ms")):
    pb.axhline(yv, color=P.muted(), lw=0.6, ls=":")
    pb.text(4.95, yv * 3, txt, fontsize=bio.core.FONT["tiny"], color=P.ink(), ha="right")
u2 = 2.0
t2 = mfpt(100, 2 * np.exp(-u2))
pb.plot(u2, t2, "o", ms=4.5, color=charts.line("positive"))
pb.annotate(f"U = 2RT: {t2:.1f} s", (u2, t2), (2.35, 1e6), fontsize=bio.core.FONT["tiny"], color=P.ink(),
            arrowprops=dict(arrowstyle="-", color=P.muted(), lw=0.6))
pb.annotate("U = 0 (random search): %.0f × 10$^{%d}$ s" % (tau[0] / 10 ** np.floor(np.log10(tau[0])), np.floor(np.log10(tau[0]))), (0, tau[0]), (0.35, tau[0] * 30), fontsize=bio.core.FONT["tiny"],
            color=P.ink())
pb.set_xlim(0, 5)
pb.set_ylim(1e-10, 1e40)
pb.set_yticks([1e-9, 1e0, 1e9, 1e18, 1e27, 1e36])
charts.style_axes(pb, "native bias per residue U / RT", "mean folding time / s")
charts.title(pb, "Biased search solves Levinthal's paradox (N = 100)")
