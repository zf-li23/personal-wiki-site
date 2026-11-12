# Sensitivity of the Ross-Macdonald R0 = m a^2 b c p^n / (r (-ln p)) (Eq. 40.1). Baseline m = 10, a = 0.3,
# b = c = 0.5, p = 0.9, n = 10, r = 0.01 (R0 about 75). A: relative R0 when one parameter is reduced by a
# fraction x (m -> (1-x) m, a -> (1-x) a, p -> (1-x) p). B: elasticities from Eq. (40.2).
import numpy as np
import wikibio as bio
from wikibio import charts

P = bio.P
m, a, b, c, p, n, r = 10, 0.3, 0.5, 0.5, 0.9, 10, 0.01


def R0(m=m, a=a, p=p):
    return m * a ** 2 * b * c * p ** n / (r * -np.log(p))


base = R0()
fig, ax = bio.canvas(22, 9.5)
A = charts.axes_at(ax, (2.0, 1.5, 9.6, 7.0))
x = np.linspace(0, 0.5, 200)
A.semilogy(x, R0(m=m * (1 - x)) / base, color=P.edge("neutral"), lw=1.8, label="vector density m (larval control)")
A.semilogy(x, R0(a=a * (1 - x)) / base, color=P.edge("enzyme"), lw=1.8, ls="--", label="human biting rate a (nets, repellents)")
A.semilogy(x, R0(p=p * (1 - x)) / base, color=P.edge("negative"), lw=1.8, ls="-.", label="daily survival p (adulticides)")
A.axhline(1 / base, color=P.muted(), ls=":", lw=1)
A.text(0.49, 1.15 / base, "R0 = 1", ha="right", fontsize=7, color=P.muted())
A.set_ylim(1e-4, 1.5)
A.set_xlabel("Proportional reduction of the parameter")
A.set_ylabel("R0 relative to baseline (log scale)")
A.legend(fontsize=7, frameon=False, loc="lower left")
A.set_title("A  Effect of control on R0", fontsize=8, loc="left")
B = charts.axes_at(ax, (14.0, 1.5, 7.6, 7.0))
names = ["m", "a", "b", "c", "r", "p"]
vals = [1, 2, 1, 1, -1, n + 1 / -np.log(p)]
toks = ["neutral", "enzyme", "neutral", "neutral", "positive", "negative"]
B.bar(names, vals, color=[P.fill(t) for t in toks], edgecolor=[P.edge(t) for t in toks], lw=0.7)
for i, v in enumerate(vals):
    B.text(i, v + (0.4 if v > 0 else -1.2), f"{v:.1f}", ha="center", fontsize=7, color=P.ink())
B.axhline(0, color=P.muted(), lw=0.8)
B.set_ylabel("Elasticity of R0")
B.set_title("B  Elasticities (p = 0.9, n = 10)", fontsize=8, loc="left")
B.set_ylim(-3, 22)
