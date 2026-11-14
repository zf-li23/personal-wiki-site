# Conformist transmission maintains differences between groups (after Boyd and Richerson 1985). Two groups
# exchange a fraction m of their members each generation; then each naive individual samples three adults of
# its group and adopts a variant. With unbiased copying the frequency p of variant 1 is unchanged by
# transmission; with conformist bias of strength D it becomes p + D p (1 - p) (2 p - 1), so the majority
# variant is adopted more often than its frequency. A: frequencies of variant 1 in two groups starting at
# 0.9 and 0.1 with m = 0.05 per generation. B: the difference between groups after 500 generations against
# the migration rate, for two strengths of conformity.
import numpy as np

import wikibio as bio
from wikibio import quant

P = bio.P


def run(D, m, T, p1=0.9, p2=0.1):
    out = []
    for _ in range(T):
        p1, p2 = (1 - m) * p1 + m * p2, (1 - m) * p2 + m * p1
        p1 = p1 + D * p1 * (1 - p1) * (2 * p1 - 1)
        p2 = p2 + D * p2 * (1 - p2) * (2 * p2 - 1)
        out.append((p1, p2))
    return np.array(out)


fig, ax = bio.canvas(22, 9.6)
T = 60
pa = quant.Plot(ax, (2.0, 1.8, 8.0, 6.6), (0, T), (0, 1), xlabel="Generation", ylabel="Frequency of variant 1",
                xticks=[0, 20, 40, 60], yticks=[0, 0.5, 1])
bio.panel(ax, "A", (0.2, 9.3))
g = np.arange(1, T + 1)
u = run(0.0, 0.05, T)
c = run(0.5, 0.05, T)
pa.line(g, u[:, 0], "neutral", lw=1.8, dashed=True)
pa.line(g, u[:, 1], "neutral", lw=1.8, dashed=True)
pa.line(g, c[:, 0], "dna", lw=2.0)
pa.line(g, c[:, 1], "rna", lw=2.0)
pa.text(40, 0.97, "conformist, group 1", token="dna", ha="left")
pa.text(40, 0.03, "conformist, group 2", token="rna", ha="left")
pa.text(30, 0.56, "unbiased: groups converge", color=P.muted(), ha="left")

pb = quant.Plot(ax, (13.4, 1.8, 7.6, 6.6), (0, 0.2), (0, 1), xlabel="Migration rate m",
                ylabel="Difference between groups", xticks=[0, 0.05, 0.1, 0.15, 0.2], yticks=[0, 0.5, 1])
bio.panel(ax, "B", (11.6, 9.3))
ms = np.linspace(0.0, 0.2, 81)
for D, tok in ((0.3, "rna"), (0.6, "dna")):
    diff = [abs(np.subtract(*run(D, m, 500)[-1])) for m in ms]
    pb.line(ms, diff, tok, lw=2.0)
pb.line(ms, [abs(np.subtract(*run(0.0, m, 500)[-1])) for m in ms], "neutral", lw=1.6, dashed=True)
pb.text(0.12, 0.93, "D = 0.6", token="dna", ha="left")
pb.text(0.035, 0.6, "D = 0.3", token="rna", ha="left")
pb.text(0.1, 0.06, "unbiased (D = 0)", color=P.muted(), ha="left")
