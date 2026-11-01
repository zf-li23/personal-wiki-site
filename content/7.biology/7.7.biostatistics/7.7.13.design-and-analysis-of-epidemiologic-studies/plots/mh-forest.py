"""Passive smoking and cancer, stratified by the participant's own smoking (518 cases aged 15-59 and 518
controls; Sandler, Everson and Wilcox 1985, Am J Epidemiol 121:37). Odds ratios of exposure to a smoking
spouse for cases vs controls with 95 % Woolf intervals: among non-smokers, among smokers, the crude odds
ratio of the pooled table and the Mantel-Haenszel common odds ratio (Robins-Breslow-Greenland interval).
Square areas are proportional to the inverse variance of the log odds ratio.
"""
import matplotlib.pyplot as plt
import numpy as np
import wikibio as bio
from wikibio import charts

P = bio.P
FT = bio.core.FONT
tabs = [np.array([[120, 111], [80, 155]]), np.array([[161, 117], [130, 124]])]
names = ["non-smokers (n = 466)", "smokers (n = 532)"]
rows = []
for t in tabs:
    a, b, c, d = t.ravel()
    o = a * d / (b * c)
    se = np.sqrt(1 / a + 1 / b + 1 / c + 1 / d)
    rows.append((o, o * np.exp(-1.96 * se), o * np.exp(1.96 * se), 1 / se**2))
pool = tabs[0] + tabs[1]
a, b, c, d = pool.ravel()
o = a * d / (b * c)
se = np.sqrt(1 / a + 1 / b + 1 / c + 1 / d)
crude = (o, o * np.exp(-1.96 * se), o * np.exp(1.96 * se))
# Mantel-Haenszel and the Robins-Breslow-Greenland variance
R = S = PR = PS_QR = QS = 0.0
for t in tabs:
    a, b, c, d = t.ravel()
    n = t.sum()
    r, s = a * d / n, b * c / n
    p, q = (a + d) / n, (b + c) / n
    R += r
    S += s
    PR += p * r
    PS_QR += p * s + q * r
    QS += q * s
mh = R / S
v = PR / (2 * R**2) + PS_QR / (2 * R * S) + QS / (2 * S**2)
mh_ci = (mh * np.exp(-1.96 * np.sqrt(v)), mh * np.exp(1.96 * np.sqrt(v)))
fig, ax = plt.subplots(figsize=(7.4, 2.9))
fig.subplots_adjust(left=0.34, right=0.97, bottom=0.2, top=0.9)
ys = [3, 2]
wmax = max(r[3] for r in rows)
for y, (o, lo, hi, w), name in zip(ys, rows, names):
    ax.plot([lo, hi], [y, y], color=charts.line("rna"), lw=1.3)
    ax.plot(o, y, "s", ms=4 + 7 * np.sqrt(w / wmax), color=P.fill("rna"), mec=charts.line("rna"))
ax.plot([crude[1], crude[2]], [1, 1], color=charts.line("neutral"), lw=1.3)
ax.plot(crude[0], 1, "o", ms=6, color=P.fill("neutral"), mec=charts.line("neutral"))
ax.fill([mh_ci[0], mh, mh_ci[1], mh], [0, 0.22, 0, -0.22], color=P.fill("enzyme"), ec=charts.line("enzyme"), lw=1)
labels = names + ["crude (pooled table)", "Mantel-Haenszel"]
vals = rows + [crude + (0,), (mh,) + mh_ci + (0,)]
ax.set_yticks([3, 2, 1, 0])
ax.set_yticklabels([f"{lab}   {v[0]:.2f} ({v[1]:.2f}, {v[2]:.2f})" for lab, v in zip(labels, vals)],
                   fontsize=FT["tiny"])
ax.axvline(1, color=P.muted(), lw=0.8, ls="--")
ax.set_xscale("log")
ax.set_xticks([0.8, 1, 1.5, 2, 3])
ax.set_xticklabels(["0.8", "1", "1.5", "2", "3"])
ax.set_ylim(-0.6, 3.6)
charts.style_axes(ax, "odds ratio of a smoking spouse, cases vs controls")
