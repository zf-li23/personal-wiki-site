"""Estimating narrow-sense heritability by regression of offspring on parents (simulated, seed 2). Each panel
shows 300 families: the breeding values of the parents are normal with variance h^2, environmental
deviations with variance 1 - h^2 (phenotypic variance 1); a child's breeding value is the mean of its
parents' plus a Mendelian sampling term of variance h^2/2. A, B: mean of two offspring against the midparent
value for true h^2 = 0.3 and 0.8; the least-squares slope estimates h^2 (Formula 24.4.2). C: the same data as
in B against one parent only: the slope is h^2/2."""
import numpy as np
import matplotlib.pyplot as plt
import wikibio as bio
from wikibio import charts

P = bio.P
FT = bio.core.FONT
rng = np.random.default_rng(2)


def families(h2, n=300):
    am = rng.normal(0, np.sqrt(h2), n)
    af = rng.normal(0, np.sqrt(h2), n)
    pm = am + rng.normal(0, np.sqrt(1 - h2), n)
    pf = af + rng.normal(0, np.sqrt(1 - h2), n)
    kids = []
    for _ in range(2):
        ak = (am + af) / 2 + rng.normal(0, np.sqrt(h2 / 2), n)
        kids.append(ak + rng.normal(0, np.sqrt(1 - h2), n))
    return pm, pf, np.mean(kids, axis=0)


fig, axs = plt.subplots(1, 3, figsize=(11.5, 3.8))
fig.subplots_adjust(left=0.06, right=0.98, bottom=0.16, top=0.88, wspace=0.28)
data = {h2: families(h2) for h2 in (0.3, 0.8)}
panels = [(axs[0], 0.3, "mid"), (axs[1], 0.8, "mid"), (axs[2], 0.8, "one")]
for k, (ax, h2, kind) in enumerate(panels):
    pm, pf, o = data[h2]
    x = (pm + pf) / 2 if kind == "mid" else pm
    b, c = np.polyfit(x, o, 1)
    ax.scatter(x, o, s=7, color=charts.line("dna"), alpha=0.6, lw=0)
    xs = np.linspace(-3, 3, 10)
    ax.plot(xs, b * xs + c, color=charts.line("rna"), lw=2)
    ax.plot(xs, xs, color=P.muted(), lw=0.8, ls=":")
    target = h2 if kind == "mid" else h2 / 2
    ax.text(0.04, 0.95, f"slope $b = {b:.2f}$\n(expected {target:g})", transform=ax.transAxes, va="top",
            fontsize=FT["tiny"], color=P.ink())
    ax.set_xlim(-3, 3)
    ax.set_ylim(-3, 3)
    xl = "midparent value" if kind == "mid" else "one parent"
    charts.style_axes(ax, xl, "mean of offspring" if k == 0 else None)
    charts.title(ax, f"{'ABC'[k]}  $h^2 = {h2}$, " + ("midparent" if kind == "mid" else "single parent"))
