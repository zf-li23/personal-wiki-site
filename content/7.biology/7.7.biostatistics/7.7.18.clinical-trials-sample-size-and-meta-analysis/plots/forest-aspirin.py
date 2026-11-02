"""Aspirin for the primary prevention of cardiovascular disease: meta-analysis of published trial results.

Each trial contributes the relative effect (risk, rate or hazard ratio) of aspirin vs control on its main
cardiovascular composite end point with its published 95 % interval (definitions differ between trials);
for HOT the standard error is derived from the published 15 % reduction and p = 0.03. TPT: MRC General
Practice Research Framework, Lancet 1998; HOT: Hansson et al., Lancet 1998; PPP: Collaborative Group of the
Primary Prevention Project, Lancet 2001; WHS: Ridker et al., NEJM 2005; ARRIVE: Gaziano et al., Lancet
2018; ASCEND: ASCEND Study Collaborative Group, NEJM 2018; ASPREE: McNeil et al., NEJM 2018.

A: forest plot with inverse-variance fixed-effect and DerSimonian-Laird random-effects summaries (squares
proportional to the weight). B: cumulative fixed-effect meta-analysis in order of publication.
C: major bleeding (HOT: non-fatal major bleeds from counts; WHS: gastrointestinal bleeding requiring
transfusion; ARRIVE: gastrointestinal bleeding; ASCEND, ASPREE: major bleeding), where heterogeneity is
moderate and the random-effects interval is wider.
"""
import matplotlib.pyplot as plt
from matplotlib.ticker import NullFormatter
import numpy as np
import wikibio as bio
from scipy import stats
from wikibio import charts

P = bio.P
FT = bio.core.FONT
Z = stats.norm.isf(0.025)
cv = [("TPT 1998", 0.80, 0.65, 0.99), ("HOT 1998", 0.85, None, 0.03), ("PPP 2001", 0.77, 0.62, 0.95),
      ("WHS 2005", 0.91, 0.80, 1.03), ("ARRIVE 2018", 0.96, 0.81, 1.13), ("ASCEND 2018", 0.88, 0.79, 0.97),
      ("ASPREE 2018", 0.95, 0.83, 1.08)]
a, n1, b, n2 = 129, 9399, 70, 9391
hot_rr = (a / n1) / (b / n2)
hot_se = np.sqrt(1 / a - 1 / n1 + 1 / b - 1 / n2)
bleed = [("HOT 1998", hot_rr, hot_rr * np.exp(-Z * hot_se), hot_rr * np.exp(Z * hot_se)),
         ("WHS 2005", 1.40, 1.07, 1.83), ("ARRIVE 2018", 2.11, 1.36, 3.28), ("ASCEND 2018", 1.29, 1.09, 1.52),
         ("ASPREE 2018", 1.38, 1.18, 1.62)]


def logse(rows):
    y, s = [], []
    for _, e, lo, hi in rows:
        y.append(np.log(e))
        s.append(abs(np.log(e)) / stats.norm.isf(hi / 2) if lo is None else (np.log(hi) - np.log(lo)) / (2 * Z))
    return np.array(y), np.array(s)


def meta(y, s):
    w = 1 / s**2
    m = (w * y).sum() / w.sum()
    q = (w * (y - m) ** 2).sum()
    k = len(y)
    tau2 = max(0.0, (q - (k - 1)) / (w.sum() - (w**2).sum() / w.sum()))
    i2 = max(0.0, (q - (k - 1)) / q) if q > 0 else 0.0
    wr = 1 / (s**2 + tau2)
    mr = (wr * y).sum() / wr.sum()
    return dict(fe=(m, 1 / np.sqrt(w.sum())), re=(mr, 1 / np.sqrt(wr.sum())), q=q, i2=i2, tau2=tau2, w=w)


def forest(ax, rows, y, s, res, tok, xt):
    k = len(rows)
    wmax = res["w"].max()
    for i, (name, *_ ) in enumerate(rows):
        yy = k + 1 - i
        e, lo, hi = np.exp(y[i]), np.exp(y[i] - Z * s[i]), np.exp(y[i] + Z * s[i])
        if rows[i][2] is not None:
            lo, hi = rows[i][2], rows[i][3]  # show the published interval
        ax.plot([lo, hi], [yy, yy], color=charts.line(tok), lw=1.2)
        ax.plot(e, yy, "s", ms=3 + 7 * np.sqrt(res["w"][i] / wmax), color=P.fill(tok), mec=charts.line(tok))
        ax.text(xt, yy, f"{name}   {e:.2f} ({lo:.2f}, {hi:.2f})", ha="right", va="center", fontsize=FT["tiny"], color=P.ink(),
                transform=ax.get_yaxis_transform())
    for yy, key, lab in [(0.8, "fe", "fixed effect"), (-0.4, "re", "random effects")]:
        m, se = res[key]
        lo, hi = np.exp(m - Z * se), np.exp(m + Z * se)
        ax.fill([lo, np.exp(m), hi, np.exp(m)], [yy, yy + 0.3, yy, yy - 0.3], color=P.fill("enzyme"), ec=charts.line("enzyme"))
        ax.text(xt, yy, f"{lab}   {np.exp(m):.2f} ({lo:.2f}, {hi:.2f})", ha="right", va="center", fontsize=FT["tiny"],
                color=P.ink(), weight="bold", transform=ax.get_yaxis_transform())
    ax.axvline(1, color=P.muted(), lw=0.8, ls="--")
    ax.set_xscale("log")
    ax.set_yticks([])
    ax.set_ylim(-1.1, k + 1.8)
    ax.xaxis.set_minor_formatter(NullFormatter())
    ax.text(0.98, 0.99, f"Q = {res['q']:.2f}, I² = {100 * res['i2']:.0f}%, tau² = {res['tau2']:.4f}",
            transform=ax.transAxes, fontsize=FT["tiny"], color=P.muted(), va="top", ha="right")


fig = plt.figure(figsize=(11.5, 6.2))
axA = fig.add_axes([0.25, 0.56, 0.26, 0.38])
axB = fig.add_axes([0.72, 0.30, 0.26, 0.64])
axC = fig.add_axes([0.25, 0.07, 0.26, 0.33])
y, s = logse(cv)
res = meta(y, s)
forest(axA, cv, y, s, res, "dna", -0.03)
axA.set_xticks([0.6, 0.8, 1, 1.25])
axA.set_xticklabels(["0.6", "0.8", "1", "1.25"])
charts.style_axes(axA, "relative effect, aspirin vs control")
charts.title(axA, "A  Main cardiovascular composite", loc="right")
for j in range(1, len(cv) + 1):
    r = meta(y[:j], s[:j])
    m, se = r["fe"]
    yy = len(cv) + 1 - j
    axB.plot([np.exp(m - Z * se), np.exp(m + Z * se)], [yy, yy], color=charts.line("rna"), lw=1.2)
    axB.plot(np.exp(m), yy, "o", ms=4, color=charts.line("rna"))
    axB.text(-0.03, yy, f"+ {cv[j - 1][0]}   {np.exp(m):.2f}", ha="right", va="center", fontsize=FT["tiny"], color=P.ink(),
             transform=axB.get_yaxis_transform())
axB.axvline(1, color=P.muted(), lw=0.8, ls="--")
axB.set_xscale("log")
axB.set_xticks([0.6, 0.8, 1, 1.25])
axB.set_xticklabels(["0.6", "0.8", "1", "1.25"])
axB.set_yticks([])
axB.xaxis.set_minor_formatter(NullFormatter())
axB.set_ylim(0.3, len(cv) + 0.7)
charts.style_axes(axB, "cumulative fixed-effect estimate")
charts.title(axB, "B  Cumulative meta-analysis", loc="right")
yb, sb = logse(bleed)
rb = meta(yb, sb)
forest(axC, bleed, yb, sb, rb, "rna", -0.03)
axC.set_xticks([1, 1.5, 2, 3])
axC.set_xticklabels(["1", "1.5", "2", "3"])
charts.style_axes(axC, "relative effect on bleeding, aspirin vs control")
charts.title(axC, "C  Bleeding", loc="right")
