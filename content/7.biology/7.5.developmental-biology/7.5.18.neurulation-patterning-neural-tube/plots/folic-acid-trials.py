"""Folic acid and neural tube defects. (A) The MRC Vitamin Study (1991), a randomized trial in women who had
already had an affected pregnancy: recurrence in the arms with folic acid (4 mg per day) and without it, with
Wilson 95% confidence intervals; the relative risk is 0.29 (95% CI 0.12-0.71 by the log method). (B) The China
community intervention (Berry et al. 1999): prevalence of neural tube defects among pregnancies of women who
took 0.4 mg folic acid daily around conception and of those who did not, in a northern high-prevalence region and
a southern region; the absolute benefit is largest where the baseline risk is high."""
import numpy as np
import matplotlib.pyplot as plt
import wikibio as bio
from wikibio import charts

P = bio.P
FT = bio.core.FONT


def wilson(k, n, z=1.96):
    p = k / n
    d = 1 + z * z / n
    c = (p + z * z / (2 * n)) / d
    h = z * np.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / d
    return p, c - h, c + h


fig, (a1, a2) = plt.subplots(1, 2, figsize=(9.6, 3.9), gridspec_kw={"width_ratios": [1, 1.3]})
fig.subplots_adjust(left=0.08, right=0.98, bottom=0.17, top=0.86, wspace=0.32)
arms = [("folic acid", 6, 593, "positive"), ("no folic acid", 21, 602, "negative")]
for i, (name, k, n, tok) in enumerate(arms):
    p, lo, hi = wilson(k, n)
    a1.bar(i, 100 * p, 0.55, color=P.fill(tok), edgecolor=P.edge(tok), lw=1.0)
    a1.errorbar(i, 100 * p, yerr=[[100 * (p - lo)], [100 * (hi - p)]], color=P.ink(), capsize=4, lw=1.0)
    a1.text(i, 100 * hi + 0.25, f"{k}/{n}", ha="center", fontsize=FT["tiny"], color=P.ink())
rr = (6 / 593) / (21 / 602)
se = np.sqrt(1 / 6 - 1 / 593 + 1 / 21 - 1 / 602)
lo, hi = np.exp(np.log(rr) - 1.96 * se), np.exp(np.log(rr) + 1.96 * se)
a1.text(0.5, 6.4, f"RR = {rr:.2f} ({lo:.2f}-{hi:.2f})", ha="center", fontsize=FT["small"], color=P.ink())
a1.set_xticks([0, 1], [a[0] for a in arms])
a1.set_ylim(0, 7.2)
a1.set_xlim(-0.6, 1.6)
charts.style_axes(a1, None, "recurrence of NTD / %")
charts.title(a1, "A  Recurrence (MRC trial)")

regions = ["northern region", "southern region"]
no, yes = [4.8, 1.0], [1.0, 0.6]
x = np.arange(2)
a2.bar(x - 0.18, no, 0.34, color=P.fill("negative"), edgecolor=P.edge("negative"), lw=1.0, label="no folic acid")
a2.bar(x + 0.18, yes, 0.34, color=P.fill("positive"), edgecolor=P.edge("positive"), lw=1.0, label="0.4 mg folic acid")
for xi, a, b in zip(x, no, yes):
    a2.text(xi - 0.18, a + 0.1, f"{a:.1f}", ha="center", fontsize=FT["tiny"], color=P.ink())
    a2.text(xi + 0.18, b + 0.1, f"{b:.1f}", ha="center", fontsize=FT["tiny"], color=P.ink())
    a2.text(xi, max(a, b) + 0.6, f"-{100 * (1 - b / a):.0f}%", ha="center", fontsize=FT["small"], color=P.ink())
a2.set_xticks(x, regions)
a2.set_ylim(0, 6.2)
a2.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="upper right")
charts.style_axes(a2, None, "NTD per 1000 pregnancies")
charts.title(a2, "B  Primary prevention (China)")
