"""How often human development fails after implantation.

Outcome of 100 pregnancies detected by a daily urinary hCG assay from implantation (after Wilcox et al. 1988:
about 31 % lost, two thirds of them before clinical recognition); about 3 % of live births carry a major
birth defect. Losses before implantation are not detectable this way and are not included.
"""

import numpy as np
import matplotlib.pyplot as plt
import wikibio as bio
from wikibio import charts

P = bio.P
FT = bio.core.FONT

fig, a = plt.subplots(figsize=(7.4, 3.4))
fig.subplots_adjust(left=0.33, right=0.97, bottom=0.17, top=0.88)

implanted = 100.0
subclinical = 22.0
clinical = 9.0
live = implanted - subclinical - clinical
defect = 0.03 * live
rows = [("implanted (hCG detected)", 0, implanted, "neutral"),
        ("lost before clinical recognition", implanted - subclinical, subclinical, "negative"),
        ("clinically recognized miscarriage", implanted - subclinical - clinical, clinical, "drug"),
        ("live births", 0, live, "positive"),
        ("  with a major birth defect", 0, defect, "highlight")]
for i, (name, left, width, tok) in enumerate(rows):
    y = len(rows) - 1 - i
    a.barh(y, width, left=left, color=P.fill(tok), edgecolor=P.edge(tok), lw=0.8, height=0.62)
    a.text(left + width + 1.5, y, f"{width:.0f}" if width >= 1 else f"{width:.1f}", va="center",
           fontsize=FT["tiny"], color=P.ink())
a.set_yticks(range(len(rows)))
a.set_yticklabels([r[0] for r in rows][::-1])
a.set_xlim(0, 112)
charts.style_axes(a, "per 100 implanted pregnancies")
charts.title(a, "Outcome of pregnancies after implantation")

