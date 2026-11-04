# Dose-response in infection: the independent-action model, an empirical 4PL fit, and the range of ID50.
import numpy as np

import wikibio as bio
from wikibio import quant
from wikibio import stats as S

P = bio.P
rng = np.random.default_rng(0)
fig, ax = bio.canvas(19.0, 6.6)

# ---------------------------------------------------------------- A: independent action
bio.panel(ax, "A", (0.1, 6.2))
pA = quant.Plot(ax, (1.3, 1.1, 4.4, 4.2), xlim=(0, 4000), ylim=(0, 1.0),
                xlabel="dose $d$ / cells", ylabel="$P$(infection)",
                xticks=[0, 2000, 4000], yticks=[0, 0.5, 1.0])
d = np.linspace(0, 4000, 400)
for r, tok, name in ((3e-3, "negative", "$r = 3\\times10^{-3}$"),
                     (6.93e-4, "enzyme", "$r = 7\\times10^{-4}$"),
                     (2.5e-4, "dna", "$r = 2.5\\times10^{-4}$")):
    pA.line(d, 1 - np.exp(-r * d), tok, text=name, at=0.78, size="tiny")
    pA.points(np.log(2) / r, 0.5, token=tok, r=0.09)
pA.hline(0.5, dashed=True, text="ID$_{50}$", side="left")
bio.label(ax, (3.5, 0.15), "$P = 1 - \\mathrm{e}^{-rd}$: no threshold dose", size="tiny", color=P.muted())

# ---------------------------------------------------------------- B: log dose and a 4PL fit
bio.panel(ax, "B", (6.6, 6.2))
pB = quant.Plot(ax, (7.9, 1.1, 4.2, 4.2), xlim=(1e1, 1e6), ylim=(0, 1.0), xlog=True,
                xlabel="dose $d$ / cells", ylabel="fraction infected",
                xticks=[(1e1, "10"), (1e3, "$10^3$"), (1e5, "$10^5$")], yticks=[0, 0.5, 1.0])
dd = np.logspace(1, 6, 300)
pB.line(dd, 1 - np.exp(-1e-3 * dd), "enzyme", text="independent\naction", at=0.42, size="tiny", dx=-0.1, dy=0.45, ha="right")

# a simulated challenge experiment: 10 hosts per dose, hosts differing in susceptibility
doses = np.array([10.0, 32, 100, 316, 1000, 3162, 1e4, 3.16e4, 1e5])
ptrue = 1 / (1 + (900.0 / doses) ** 0.55)
obs = rng.binomial(10, ptrue) / 10
fit = S.fit_4pl(doses, obs, p0=[0.0, 1.0, np.log10(900.0), 0.55])
xs = np.logspace(1, 6, 200)
pB.line(xs, S.four_pl(xs, *fit.params), "drug", text="4PL fit", at=0.55, size="tiny")
pB.points(doses, obs, token="drug", r=0.07)
bio.label(ax, (10.0, 0.15), "points: 10 hosts per dose", size="tiny", color=P.muted())

# ---------------------------------------------------------------- C: ID50 across enteric pathogens
bio.panel(ax, "C", (12.9, 6.2))
pC = quant.Plot(ax, (15.1, 1.5, 3.4, 3.6), xlim=(0, 9), ylim=(-0.5, 5.3),
                xlabel="$\\log_{10}$ ID$_{50}$ (ingested cells)", xticks=[0, 3, 6, 9], frame="l")
rows = [("Shigella flexneri", 2.0, True), ("Escherichia coli O157:H7", 2.0, True),
        ("Campylobacter jejuni", 3.0, True), ("Salmonella enterica", 5.0, True),
        ("Vibrio cholerae", 8.0, True), ("the same, with an antacid", 4.0, False)]
for i, (name, v, italic) in enumerate(reversed(rows)):
    y = i * 0.95 - 0.2
    x0 = pC.X(0)
    ax.plot([x0, pC.X(v)], [pC.Y(y), pC.Y(y)], color=P.muted(), lw=0.8, zorder=6)
    pC.points(v, y, token="bacterium", r=0.11)
    bio.label(ax, (x0 - 0.15, pC.Y(y)), name, size="tiny", ha="right", italic=italic)
bio.label(ax, (16.9, 5.9), "seven orders of magnitude, set mostly\nby survival of the gastric acid barrier",
          size="tiny", color=P.muted())
