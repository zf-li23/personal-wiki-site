# Concentration-response analysis of a simulated cell-based assay (seed 3). Three agonists are tested in a
# 1:3 dilution series (10 concentrations from 10 uM); the response (% of a reference full agonist) follows
# a four-parameter logistic curve with Gaussian noise (SD 5 %). True values: A EC50 12 nM, Hill 1.0, full
# agonist; B EC50 400 nM, Hill 1.3, full agonist; C EC50 30 nM, Hill 0.9, partial agonist (Emax 55 %).
# A: the plate layout (triplicates for A and B, duplicates for C, vehicle and reference columns) shaded by
# the simulated response. B: nonlinear least-squares 4PL fits with 95 % confidence bands; EC50 measures
# potency (position on the dose axis), Emax efficacy (height of the plateau). Table: estimates with 95 % CI.
import numpy as np

import wikibio as bio
from wikibio import quant, stats

P = bio.P
fig, ax = bio.canvas(23.6, 11.6)

# ---- simulated experiment --------------------------------------------------------------------------
rng = np.random.default_rng(3)
conc = 1e4 / 3.0 ** np.arange(10)[::-1]          # nM, 0.51 .. 10000
truth = {"A": (0, 100, np.log10(12), 1.0), "B": (0, 100, np.log10(400), 1.3), "C": (0, 55, np.log10(30), 0.9)}
reps = {"A": 3, "B": 3, "C": 2}
tok = {"A": "drug", "B": "channel", "C": "enzyme"}
data, fits = {}, {}
for c, par in truth.items():
    x = np.repeat(conc, reps[c])
    y = stats.four_pl(x, *par) + rng.normal(0, 5.0, len(x))
    data[c] = (x, y)
    fits[c] = stats.fit_4pl(x, y)

# ---- A: assay ----------------------------------------------------------------------------------------
bio.panel(ax, "A", (0.1, 11.45))
bio.label(ax, (0.9, 10.95), "Cell-based assay", size="normal", bold=True, ha="left")
stats.dilution_series(ax, (1.0, 8.3), n=7, token="drug", dx=0.95, factor="1:3")
bio.label(ax, (0.9, 7.85), "10 µM", size="tiny", ha="left", color=P.muted())
bio.label(ax, (7.2, 7.85), "0.5 nM", size="tiny", ha="right", color=P.muted())
bio.arrow(ax, (7.75, 8.9), (8.9, 8.9), kind="process", head=0.2)
bio.icon(ax, "servier/spectrophotometer", at=(10.1, 9.0), height=1.4)
bio.label(ax, (10.1, 7.95), "plate reader", size="tiny", color=P.muted())

# plate: rows A-C compound A, D-F compound B, G-H compound C; columns 1-10 dose (high -> low),
# column 11 vehicle (0 %), column 12 reference agonist at 10 uM (100 %)
vals = np.zeros((8, 12))
rows = {"A": range(0, 3), "B": range(3, 6), "C": range(6, 8)}
for c, rr in rows.items():
    y = data[c][1].reshape(10, reps[c])[::-1]  # high dose first
    for j, r in enumerate(rr):
        vals[r, :10] = y[:, j] / 100
vals[:, 10] = np.clip(rng.normal(0, 0.05, 8), 0, 1)
vals[:, 11] = np.clip(rng.normal(1, 0.05, 8), 0, 1)
cell = 0.5
px, py = 1.6, 1.6
box = stats.well_plate(ax, (px, py), vals, cell=cell, token="drug")
bio.label(ax, (px + box[2] / 2, py + box[3] + 0.3), "96-well plate, luminescence reporter", size="small", va="bottom")
for j in range(12):
    bio.label(ax, (px + 0.11 + (j + 0.5) * cell, py - 0.18), str(j + 1), size="tiny", va="top", color=P.muted())
# row groups
for c, rr in rows.items():
    r0, r1 = min(rr), max(rr)
    ytop = py + box[3] - 0.11 - r0 * cell - 0.06
    ybot = py + box[3] - 0.11 - (r1 + 1) * cell + 0.06
    quant.bracket(ax, (px + box[2] + 0.2, ytop), (px + box[2] + 0.2, ybot), side=1, tick=0.1, color=quant.line_color(tok[c]))
    bio.label(ax, (px + box[2] + 0.45, (ytop + ybot) / 2), c, size="small", bold=True, ha="left", color=quant.line_color(tok[c]))
bio.label(ax, (px + 0.11 + 10.5 * cell, py - 0.62), "vehicle", size="tiny", va="top", color=P.muted(), ha="right")
bio.label(ax, (px + 0.11 + 11.5 * cell, py - 0.62), "  ref.", size="tiny", va="top", color=P.muted(), ha="left")
bio.label(ax, (px + 0.11 + 5 * cell, py - 0.62), "dose 10 µM → 0.5 nM", size="tiny", va="top", color=P.muted())
# colour key
kx, ky = px + 0.2, py + box[3] + 0.95
for i in range(6):
    ax.add_patch(bio.core.Circle((kx + i * 0.32, ky), 0.12, facecolor=P.mix(P.surface(), P.fill("drug"), i / 5),
                                 edgecolor=P.edge("neutral"), lw=0.5))
bio.label(ax, (kx - 0.2, ky), "0", size="tiny", ha="right", color=P.muted())
bio.label(ax, (kx + 5 * 0.32 + 0.2, ky), "100 % response", size="tiny", ha="left", color=P.muted())

# ---- B: concentration-response fits ---------------------------------------------------------------
X0, Y0, W, H = 13.2, 3.6, 9.4, 6.9
bio.panel(ax, "B", (X0 - 2.2, 11.45))
pl = quant.Plot(ax, (X0, Y0, W, H), (0.3, 2e4), (-10, 115), xlog=True, ylabel="Response / % of reference",
                xlabel="Agonist concentration / nM (log scale)",
                xticks=[(0.1 * 10, "1"), 10, 100, 1000, (1e4, "10⁴")], yticks=[0, 25, 50, 75, 100], grid=True)
for c in "ABC":
    stats.draw_4pl(pl, fits[c], tok[c], band_alpha=0.22)
    e = fits[c].ci["EC50"][0]
    half = fits[c].predict(e)
    x, y = pl.xy(e, half)
    ax.plot([x, x], [pl.Y(-10), y], color=quant.line_color(tok[c]), lw=0.8, ls=(0, (2, 1.6)), zorder=pl.z)
    ax.add_patch(bio.core.Circle((x, y), 0.09, color=quant.line_color(tok[c]), zorder=pl.z + 3))
pl.text(2.3e4, fits["A"].predict(2e4) + 2, "A", token=tok["A"], size="small", bold=True, ha="left", va="bottom")
pl.text(2.3e4, fits["B"].predict(2e4) - 2, "B", token=tok["B"], size="small", bold=True, ha="left", va="top")
pl.text(2.3e4, fits["C"].predict(2e4), "C", token=tok["C"], size="small", bold=True, ha="left")
# potency: horizontal shift between A and B at half maximum
eA, eB = fits["A"].ci["EC50"][0], fits["B"].ci["EC50"][0]
bio.arrow(ax, pl.xy(eA * 1.25, 50), pl.xy(eB / 1.25, 50), kind="process", head=0.18, color=P.muted(), lw=1.0)
pl.text((eA * eB) ** 0.5, 53, f"potency: {eB / eA:.0f}× shift", ha="center", va="bottom", color=P.muted())
# efficacy of the partial agonist
topC = fits["C"].ci["top"][0]
quant.bracket(ax, pl.xy(1.9e3, 0), pl.xy(1.9e3, topC), side=1, tick=0.12, color=quant.line_color(tok["C"]))
pl.text(1.9e3 * 1.25, topC / 2, f"efficacy\n$E_{{\\max}}$ = {topC:.0f} %", token=tok["C"], ha="left")
bio.label(ax, (X0 + 0.2, Y0 + H + 0.35), "$y = E_0 + \\dfrac{E_{\\max} - E_0}{1 + (\\mathrm{EC}_{50}/x)^{n_{\\mathrm{H}}}}$",
          size="small", ha="left", va="bottom")

# table of estimates (95 % CI from the fit covariance, t quantile)
ty = 1.55
cols = [X0 - 1.2, X0 + 0.6, X0 + 4.4, X0 + 6.9]
for x, h in zip(cols, ("", "EC$_{50}$ / nM (95% CI)", "$n_{\\mathrm{H}}$", "$E_{\\max}$ / %")):
    bio.label(ax, (x, ty + 0.5), h, size="tiny", ha="left", bold=True)
ax.plot([cols[0], X0 + W], [ty + 0.25, ty + 0.25], color=P.muted(), lw=0.6)
for i, c in enumerate("ABC"):
    f = fits[c]
    yy = ty - i * 0.42
    col = quant.line_color(tok[c])
    e, lo, hi = f.ci["EC50"]
    h = f.ci["hill"]
    t = f.ci["top"]
    for x, s in zip(cols, (c, f"{e:.3g}  ({lo:.3g}–{hi:.3g})", f"{h[0]:.2f} ± {(h[2] - h[1]) / 2:.2f}",
                           f"{t[0]:.0f} ± {(t[2] - t[1]) / 2:.0f}")):
        bio.label(ax, (x, yy), s, size="tiny", ha="left", color=col if s == c else P.ink(), bold=s == c)
