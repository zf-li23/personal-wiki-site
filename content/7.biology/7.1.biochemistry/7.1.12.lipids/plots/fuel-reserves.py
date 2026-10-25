"""Why fat is the long-term fuel store. A: energy released on complete oxidation per gram of stored
material: triacylglycerol about 37 kJ/g, carbohydrate and protein about 17 kJ/g; glycogen is stored with
about 2 g of water per gram, so a gram of hydrated glycogen stores only about 6 kJ. B: fuel reserves of a
normal 70 kg adult (fat about 400 000 kJ, mobilizable muscle protein about 100 000 kJ, glycogen about
2 500 kJ in liver and muscle), expressed also as days of a resting energy expenditure of 8 000 kJ/day."""

import numpy as np
import wikibio as bio
from wikibio import charts

P = bio.P
fig, ax = bio.canvas(18.0, 7.4)

bio.panel(ax, "A", (0.1, 7.3))
pa = charts.axes_at(ax, (1.8, 1.5, 6.4, 5.2))
names = ["triacylglycerol", "carbohydrate\n(dry)", "protein", "glycogen\n(hydrated)"]
vals = [37, 17, 17, 17 / 3]
toks = ["lipid", "carbohydrate", "protein", "carbohydrate"]
bars = pa.bar(range(4), vals, color=[P.fill(t) for t in toks], edgecolor=[charts.line(t) for t in toks], lw=1.0, width=0.62)
bars[3].set_hatch("///")
for i, v in enumerate(vals):
    pa.text(i, v + 0.8, f"{v:.0f}", ha="center", fontsize=bio.core.FONT["small"], color=P.ink())
pa.set_xticks(range(4), names)
pa.set_ylim(0, 42)
charts.style_axes(pa, None, "energy / (kJ g⁻¹)")

bio.panel(ax, "B", (9.3, 7.3))
pb = charts.axes_at(ax, (12.0, 1.5, 5.4, 5.2))
res = [("fat", 400_000, "lipid"), ("protein", 100_000, "protein"), ("glycogen", 2_500, "carbohydrate")]
y = np.arange(3)
pb.barh(y, [r[1] for r in res], color=[P.fill(r[2]) for r in res], edgecolor=[charts.line(r[2]) for r in res], lw=1.0,
        height=0.6)
pb.set_xscale("log")
for i, (name, kj, tok) in enumerate(res):
    pb.text(kj * 1.25, i, f"{kj:,} kJ ≈ {kj / 8000:.1f} d".replace(".0 d", " d"), va="center", fontsize=bio.core.FONT["tiny"],
            color=P.ink())
pb.set_yticks(y, [r[0] for r in res])
pb.invert_yaxis()
pb.set_xlim(1e3, 3e6)
charts.style_axes(pb, "stored energy / kJ (log scale)", None)
