# Time scales of the five layers of gene regulation, as order-of-magnitude ranges on one logarithmic time
# axis (seconds). All values are the ones stated in the chapters of course 7.2:
#   chromatin: acetylation relaxes with tau of a few to ten minutes (15.3), BRG1 remodels a mononucleosome
#     over minutes to about 70 min (Example 15.4.1), marks at the IFN-beta promoter appear from about 3 h and
#     H3K9ac lasts at least 19 h (15.5), silenced states are inherited for many cell cycles (15.6-15.8);
#   initiation: nonspecific contacts of LacI last a few ms (Example 22.2.2), residence on a specific site
#     ranges from seconds to hours (22.1.3), one LacI finds its operator in minutes (22.2), an active rRNA gene
#     initiates every 1.5 s (Example 12.6.2);
#   elongation and processing: the cap is added within about 30 nt (17.1), i.e. about a second at
#     20-80 nt/s; 1 kb takes 12-50 s; a median human gene of 25 kb at 1-4 kb/min 6-25 min; dystrophin ~16 h;
#   translation and mRNA: a 300-residue protein takes 15 s to 1.7 min at 3-20 aa/s, translational switches
#     act within minutes (20.1), mRNA half-lives are minutes in E. coli and minutes to days in mammals,
#     median about 9 h (18.1);
#   protein: regulators that must change within an hour are actively degraded, a stable bacterial protein
#     responds in one cell cycle (20-60 min), the median mammalian protein half-life is about 2 d (22.3).
# Dots mark medians. The dotted verticals are the reference units.
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio
from wikibio import charts

P = bio.P
MIN, H, D = 60.0, 3600.0, 86400.0
groups = [
    ("1  Chromatin", "chromatin", [
        ("histone acetylation turnover", 2 * MIN, 10 * MIN, None),
        ("remodeling one nucleosome in vitro", 1 * MIN, 70 * MIN, None),
        ("IFN-β promoter: marks from 3 h, H3K9ac ≥ 19 h", 3 * H, 19 * H, None),
        ("silenced state inherited over cell cycles", 1 * D, 3e7, None),
    ]),
    ("2  Initiation", "dna", [
        ("nonspecific DNA contact (LacI)", 5e-4, 5e-3, None),
        ("residence on a specific site", 1.0, 1e4, None),
        ("search for the operator by one LacI", 1 * MIN, 6 * MIN, None),
        ("interval between initiations, rRNA gene", 1.2, 1.9, 1.5),
    ]),
    ("3  Elongation and processing", "rna", [
        ("capping (first ~30 nt)", 0.4, 1.5, None),
        ("transcribing 1 kb", 12.5, 50, None),
        ("median human gene (25 kb)", 6 * MIN, 25 * MIN, None),
        ("dystrophin (2.2 Mb)", 15 * H, 16.5 * H, 16 * H),
    ]),
    ("4  Translation and mRNA", "trna", [
        ("translating a 300-residue protein", 15, 100, None),
        ("translational switch on existing mRNA", 1 * MIN, 10 * MIN, None),
        ("mRNA half-life, $\\mathit{E.\\ coli}$", 1 * MIN, 10 * MIN, None),
        ("mRNA half-life, mammals", 5 * MIN, 3 * D, 9 * H),
    ]),
    ("5  Protein decay", "protein", [
        ("actively degraded regulators", 10 * MIN, 1 * H, None),
        ("stable bacterial protein: one cell cycle", 20 * MIN, 60 * MIN, None),
        ("protein half-life, mammals (median)", 1.6 * D, 2.4 * D, 2 * D),
    ]),
]

fig, ax = plt.subplots(figsize=(10.6, 7.6))
fig.subplots_adjust(left=0.36, right=0.97, top=0.9, bottom=0.08)
y, ticks, names, heads = 0.0, [], [], []
for head, tok, rows in groups:
    heads.append((y, head, tok))
    y -= 0.9
    for name, lo, hi, med in rows:
        ax.barh(y, hi - lo, left=lo, height=0.62, color=P.fill(tok), edgecolor=charts.line(tok), lw=0.9, zorder=3)
        if med:
            ax.plot([med], [y], "o", color=P.ink(), ms=3.6, zorder=4)
        ticks.append(y)
        names.append(name)
        y -= 1.0
    y -= 0.35

ref = [(1e-3, "1 ms"), (1, "1 s"), (MIN, "1 min"), (H, "1 h"), (D, "1 d"), (365 * D, "1 yr")]
for v, t in ref:
    ax.axvline(v, color=P.muted(), lw=0.6, ls=":", zorder=1)
    ax.text(v, 1.15, t, ha="center", va="bottom", fontsize=7, color=P.muted())
ax.set_xscale("log")
ax.set_xlim(2e-4, 1e8)
ax.set_ylim(y + 0.6, 1.0)
ax.set_yticks(ticks, names)
ax.set_xticks([1e-3, 1e-1, 1e1, 1e3, 1e5, 1e7], ["10⁻³", "10⁻¹", "10¹", "10³", "10⁵", "10⁷"])
ax.minorticks_off()
charts.style_axes(ax, "t / s", None)
ax.tick_params(axis="y", length=0)
ax.spines["left"].set_visible(False)
for yy, head, tok in heads:
    ax.text(-0.02, yy - 0.15, head, transform=ax.get_yaxis_transform(), ha="right", va="center", fontsize=8.5,
            weight="bold", color=charts.line(tok))
ax.text(5.5e7, ticks[3], "→", ha="center", va="center", fontsize=9, color=charts.line("chromatin"))
