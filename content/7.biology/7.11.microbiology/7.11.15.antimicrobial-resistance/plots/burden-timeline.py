# A: global deaths in 2019 attributable to and associated with bacterial antimicrobial resistance,
#    compared with HIV/AIDS and malaria (GBD estimates quoted in Murray et al. 2022, Lancet).
# B: year of introduction of an antibiotic (open circle) and year in which resistance to it was first
#    identified (filled circle) for a series of drugs; data from CDC (2013), Antibiotic Resistance
#    Threats in the United States. For penicillin, resistant staphylococci (penicillinase) were known
#    before the drug came into general use.
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio
from wikibio import charts

P = bio.P
fig = plt.figure(figsize=(13.5, 4.8))
gs = fig.add_gridspec(1, 2, width_ratios=[0.8, 1.6], wspace=0.28)

ax = fig.add_subplot(gs[0, 0])
labels = ["AMR-associated", "AMR-attributable", "HIV/AIDS", "malaria"]
vals = [4.95, 1.27, 0.864, 0.643]
toks = ["drug", "negative", "neutral", "neutral"]
y = np.arange(len(vals))[::-1]
ax.barh(y, vals, color=[P.fill(t) for t in toks], edgecolor=[P.edge(t) for t in toks], height=0.6)
for yi, v in zip(y, vals):
    ax.text(v + 0.08, yi, f"{v:.2f}", va="center", fontsize=7.5, color=P.ink())
ax.set_yticks(y)
ax.set_yticklabels(labels)
ax.set_xlim(0, 5.8)
charts.style_axes(ax, "deaths in 2019 / million")
charts.title(ax, "A   Global burden, 2019")

ax = fig.add_subplot(gs[0, 1])
rows = [
    ("penicillin", 1943, 1940, "penicillin-R $\\it{Staphylococcus}$"),
    ("tetracycline", 1950, 1959, "tetracycline-R $\\it{Shigella}$"),
    ("erythromycin", 1953, 1968, "erythromycin-R $\\it{Streptococcus}$"),
    ("methicillin", 1960, 1962, "MRSA"),
    ("gentamicin", 1967, 1979, "gentamicin-R $\\it{Enterococcus}$"),
    ("vancomycin", 1972, 1988, "VRE"),
    ("ceftazidime", 1985, 1987, "ceftazidime-R $\\it{Enterobacteriaceae}$"),
    ("imipenem", 1985, 1996, "KPC-producing $\\it{K.\\ pneumoniae}$"),
    ("levofloxacin", 1996, 1996, "levofloxacin-R pneumococcus"),
    ("linezolid", 2000, 2001, "linezolid-R $\\it{Staphylococcus}$"),
    ("daptomycin", 2003, 2004, "daptomycin-R MRSA"),
    ("ceftaroline", 2010, 2011, "ceftaroline-R $\\it{Staphylococcus}$"),
]
for i, (drug, intro, res, what) in enumerate(rows):
    yy = len(rows) - 1 - i
    ax.plot([intro, res], [yy, yy], color=P.muted(), lw=1.0, zorder=1)
    ax.plot(intro, yy, "o", ms=6.5, mfc=P.surface(), mec=charts.line("dna"), mew=1.4, zorder=3)
    ax.plot(res, yy, "o", ms=6.5, color=charts.line("negative"), zorder=3)
    ax.text(1936.5, yy, drug, ha="right", va="center", fontsize=7.5, color=P.ink())
    ax.text(max(intro, res) + 1.2, yy + (0.33 if drug == "vancomycin" else 0), what, ha="left", va="center", fontsize=6.8, color=P.muted())
ax.plot([1988, 2002], [len(rows) - 6] * 2, color=P.muted(), lw=1.0, ls=":", zorder=1)
ax.plot(2002, len(rows) - 6, "o", ms=6.5, color=charts.line("negative"), zorder=3)
ax.text(2003.2, len(rows) - 6, "VRSA", ha="left", va="center", fontsize=6.8, color=P.muted())
ax.plot([], [], "o", ms=6.5, mfc=P.surface(), mec=charts.line("dna"), mew=1.4, label="drug introduced")
ax.plot([], [], "o", ms=6.5, color=charts.line("negative"), label="resistance identified")
ax.legend(fontsize=7.5, frameon=False, loc="upper right", labelcolor=P.ink())
ax.set_xlim(1937, 2032)
ax.set_ylim(-0.8, len(rows) - 0.3)
ax.set_yticks([])
ax.spines["left"].set_visible(False)
charts.style_axes(ax, "year")
charts.title(ax, "B   Introduction and first resistance")
