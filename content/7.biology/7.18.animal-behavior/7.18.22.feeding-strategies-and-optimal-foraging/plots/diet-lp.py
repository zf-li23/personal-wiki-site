# Diet choice as linear programming, in the spirit of Belovsky's (1978) model of moose on Isle Royale
# (illustrative numbers, not his estimates). Decision variables: daily intake of terrestrial plants T and of
# aquatic plants A (kg dry mass per day). Constraints: rumen capacity T + 2.5 A <= 20 (aquatic plants are watery
# and fill more of the rumen per kg dry mass); feeding time T / 1.2 + A / 3 <= 11 h; sodium requirement
# 0.1 T + 3 A >= 13 g (aquatic plants are rich in sodium). Objective: maximize energy 12 T + 8 A (MJ per day).
# The feasible diets form the shaded polygon; the energy-maximizing diet lies at a vertex, where the rumen and
# sodium constraints bind (T = 10, A = 4 kg per day, 29 percent aquatic); the time constraint is slack.
import numpy as np
from matplotlib.patches import Polygon

import wikibio as bio
from wikibio import quant

P = bio.P
fig, ax = bio.canvas(17.0, 11.0)
p = quant.Plot(ax, (2.3, 1.8, 10.0, 8.4), (0, 16), (0, 10), xlabel="Terrestrial plants T / kg d⁻¹",
               ylabel="Aquatic plants A / kg d⁻¹", xticks=[0, 4, 8, 12, 16], yticks=[0, 2, 4, 6, 8, 10])
T = np.linspace(0, 16, 200)
rumen = (20 - T) / 2.5
time = 3 * (11 - T / 1.2)
sodium = (13 - 0.1 * T) / 3
# feasible region: A >= sodium, A <= rumen, A <= time, T >= 0
lo = sodium
hi = np.minimum(rumen, time)
ok = hi >= lo
pts = [p.xy(t, a) for t, a in zip(T[ok], hi[ok])] + [p.xy(t, a) for t, a in zip(T[ok][::-1], lo[ok][::-1])]
fill = P.mix(P.fill("positive"), P.surface(), 0.55 if not P.is_dark() else 0.75)
ax.add_patch(Polygon(pts, closed=True, facecolor=fill, edgecolor="none", zorder=p.z - 1))
p.line(T, rumen, "dna", lw=1.8)
p.line(T, time, "atp", lw=1.8)
p.line(T, sodium, "rna", lw=1.8)
p.text(0.3, 8.45, "rumen capacity", ha="left", token="dna")
p.text(9.1, 9.6, "feeding time", ha="right", token="atp")
p.text(14.0, 3.55, "sodium\nrequirement", ha="left", va="bottom", token="rna")
p.text(0.9, 5.4, "feasible\ndiets", ha="left", color=P.muted())
# objective contours 12 T + 8 A = const
for c in (90, 120, 152):
    p.line(T, (c - 12 * T) / 8, "ink", lw=0.8, dashed=True)
p.text(11.55, 1.3, "energy 152 MJ d⁻¹", ha="right")
p.text(7.7, 0.35, "90", ha="left", color=P.muted())
p.text(10.2, 0.35, "120", ha="left", color=P.muted())
p.points([10], [4], "ink", r=0.16)
bio.callout(ax, p.xy(10, 4), p.xy(13.6, 6.4), "optimal diet\nT = 10, A = 4", size="tiny")
# composition bar
x0, y0 = 13.6, 5.6
bio.label(ax, (x0 + 1.4, y0 + 3.2), "Optimal diet", size="small")
h_t, h_a = 2.6 * 10 / 14, 2.6 * 4 / 14
bio.box(ax, (x0 + 1.4, y0 + h_a + h_t / 2), 1.0, h_t, token="plant", text="T", size="small")
bio.box(ax, (x0 + 1.4, y0 + h_a / 2), 1.0, h_a, token="dna", text="A", size="small")
bio.label(ax, (x0 + 2.05, y0 + h_a / 2), "29%", size="tiny", ha="left")
bio.label(ax, (x0 + 2.05, y0 + h_a + h_t / 2), "71%", size="tiny", ha="left")
