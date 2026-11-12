# Knipling's model of the sterile insect technique (Eq. 40.5): N' = lambda N N / (N + S), lambda = 5,
# N0 = 1e6, constant releases S at initial ratios 2:1, 4:1, 9:1; compared with an insecticide killing 90%.
import numpy as np
import wikibio as bio
from wikibio import charts

P = bio.P
lam, N0 = 5.0, 1e6
fig, ax = bio.canvas(16, 9.5)
A = charts.axes_at(ax, (1.9, 1.4, 13.3, 7.4))
G = 8
for ratio, tok, ls in [(2, "neutral", "-"), (4, "enzyme", "-"), (9, "positive", "-")]:
    S = ratio * N0
    N = [N0]
    for _ in range(G):
        N.append(lam * N[-1] * N[-1] / (N[-1] + S))
    N = [v if v >= 0.05 else np.nan for v in N]
    A.semilogy(range(G + 1), N, "o", ms=3.5, color=P.edge(tok), lw=1.6, ls=ls, label=f"sterile : wild = {ratio} : 1")
K = [N0 * (lam * 0.1) ** g for g in range(G + 1)]
A.semilogy(range(G + 1), K, "s--", ms=3, color=P.edge("negative"), lw=1.4, label="insecticide, 90% kill")
A.axhline(1, color=P.muted(), lw=0.8, ls=":")
A.text(G, 1.4, "one female; 9 : 1 population extinct by generation 5", ha="right", fontsize=7, color=P.muted())
A.set_ylim(1e-1, 1e8)
A.set_xlabel("Generation")
A.set_ylabel("Wild females (log scale)")
A.legend(fontsize=7, frameon=False, loc="upper right")
