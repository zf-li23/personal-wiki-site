# Reading an HLA association: odds ratio, relative risk and absolute risk (teaching numbers, not data of a real study).
# A: relation between odds ratio (OR) and relative risk (RR) for four baseline risks p0: RR = OR / (1 - p0 + p0 OR);
#    OR approximates RR only when the disease is rare.
# B: a case-control table with the risk allele in 90% of patients and 8% of controls gives OR ~ 100, yet in a population
#    where the disease affects 0.5% of people the absolute risk of a carrier is only about 5%.
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio
from wikibio import charts

P = bio.P
fig, axs = plt.subplots(1, 2, figsize=(9.5, 3.6))
orr = np.logspace(0, 2.2, 200)
for p0, tok in ((0.001, "protein"), (0.05, "enzyme"), (0.2, "negative"), (0.4, "highlight")):
    rr = orr / (1 - p0 + p0 * orr)
    axs[0].plot(orr, rr, color=charts.line(tok), lw=1.6, label=f"baseline risk {p0:g}")
axs[0].plot(orr, orr, color=P.muted(), lw=0.8, ls="--")
axs[0].set_xscale("log")
axs[0].set_yscale("log")
axs[0].legend(frameon=False, fontsize=6.5, labelcolor=P.ink(), loc="upper left")
axs[0].text(40, 18, "RR = OR", fontsize=6.5, color=P.muted(), rotation=33)
charts.style_axes(axs[0], "odds ratio (OR)", "relative risk (RR)")
charts.title(axs[0], "A")

f_pat, f_ctl, K = 0.90, 0.08, 0.005
OR = (f_pat / (1 - f_pat)) / (f_ctl / (1 - f_ctl))
carr = K * f_pat / (K * f_pat + (1 - K) * f_ctl)
non = K * (1 - f_pat) / (K * (1 - f_pat) + (1 - K) * (1 - f_ctl))
bars = axs[1].bar(["non-carriers", "carriers"], [100 * non, 100 * carr], color=[P.fill("protein"), P.fill("negative")],
                  edgecolor=[P.edge("protein"), P.edge("negative")])
for b_, v in zip(bars, (100 * non, 100 * carr)):
    axs[1].text(b_.get_x() + b_.get_width() / 2, v + 0.2, f"{v:.2f}%", ha="center", fontsize=7, color=P.ink())
axs[1].set_ylim(0, 7)
axs[1].text(0.5, 6.2, f"OR = {OR:.0f}, RR = {carr / non:.0f}", ha="center", fontsize=7, color=P.ink())
charts.style_axes(axs[1], None, "absolute risk of disease (%)")
charts.title(axs[1], "B")
fig.tight_layout()
