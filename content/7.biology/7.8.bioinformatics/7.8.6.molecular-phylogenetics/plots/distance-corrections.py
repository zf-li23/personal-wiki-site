# Correcting observed differences for multiple substitutions. Pairs of sequences of 3000 sites are simulated
# under the K80 model with transition/transversion rate ratio kappa = 4 and gamma-distributed rates among
# sites (shape alpha = 0.5, eight equiprobable categories), for true distances d from 0.05 to 2.5 expected
# substitutions per site. A: the observed proportion of differing sites p (points) against d, with the
# JC69 expectation (line), which saturates at 3/4. B: distances estimated from the same simulated pairs by
# the p-distance, the JC69 and K80 formulas and the JC69 + Gamma formula with the true alpha; only the
# estimator that models rate variation follows the diagonal, the others underestimate long distances.
import numpy as np
from scipy import stats
import wikibio as bio
from wikibio import charts as C

P = bio.P
rng = np.random.default_rng(0)
kappa, alpha, n = 4.0, 0.5, 3000
# discrete gamma: means of 8 equiprobable categories
K = 8
q = stats.gamma.ppf(np.linspace(0, 1, K + 1), alpha, scale=1 / alpha)
cat = np.array([(stats.gamma.cdf(q[i + 1], alpha + 1, scale=1 / alpha) - stats.gamma.cdf(q[i], alpha + 1, scale=1 / alpha)) * K
                for i in range(K)])


def k80_probs(d):
    """Probabilities of no change, a transition, and either transversion along distance d (K80)."""
    beta = 1.0 / (kappa + 2)            # rates scaled so that the total rate is 1
    a = kappa * beta
    e1, e2 = np.exp(-4 * beta * d), np.exp(-2 * (a + beta) * d)
    ts = 0.25 + 0.25 * e1 - 0.5 * e2
    tv = 0.5 - 0.5 * e1
    return 1 - ts - tv, ts, tv


ds = np.linspace(0.05, 2.5, 30)
obs = []
for d in ds:
    r = cat[rng.integers(0, K, n)]
    p0, ts, tv = k80_probs(d * r)
    u = rng.random(n)
    obs.append((((u > p0) & (u <= p0 + ts)).mean(), (u > p0 + ts).mean()))
P_ts = np.array([o[0] for o in obs])
Q_tv = np.array([o[1] for o in obs])
p = P_ts + Q_tv
with np.errstate(invalid="ignore", divide="ignore"):
    jc = -0.75 * np.log(1 - 4 * p / 3)
    k80 = -0.5 * np.log(1 - 2 * P_ts - Q_tv) - 0.25 * np.log(1 - 2 * Q_tv)
    jcg = 0.75 * alpha * ((1 - 4 * p / 3) ** (-1 / alpha) - 1)

fig, ax = bio.canvas(22.0, 9.0)
a = C.axes_at(ax, (1.8, 1.5, 7.8, 6.8))
b = C.axes_at(ax, (12.8, 1.5, 7.8, 6.8))
xx = np.linspace(0, 2.6, 200)
a.plot(xx, 0.75 * (1 - np.exp(-4 * xx / 3)), color=P.muted(), lw=1.2, label="JC69 expectation")
a.plot(ds, p, "o", ms=3.5, color=C.line("dna"), label="simulated (K80 + Gamma)")
a.axhline(0.75, color=P.muted(), lw=0.8, ls=(0, (3, 2)))
a.text(0.1, 0.77, "saturation 3/4", fontsize=bio.core.FONT["tiny"], color=P.muted())
a.set_xlim(0, 2.6)
a.set_ylim(0, 0.85)
C.style_axes(a, "true distance d (substitutions per site)", "observed proportion p")
a.legend(fontsize=bio.core.FONT["tiny"], frameon=False, labelcolor=P.ink(), loc="lower right")
b.plot([0, 2.6], [0, 2.6], color=P.muted(), lw=0.8, ls=(0, (3, 2)))
for y, tok, lab in [(p, "neutral", "p-distance"), (jc, "dna", "JC69"), (k80, "rna", "K80"),
                    (jcg, "positive", "JC69 + Gamma (alpha = 0.5)")]:
    b.plot(ds, y, "o-", ms=3, lw=1.0, color=C.line(tok), label=lab)
b.set_xlim(0, 2.6)
b.set_ylim(0, 2.8)
C.style_axes(b, "true distance d", "estimated distance")
b.legend(fontsize=bio.core.FONT["tiny"], frameon=False, labelcolor=P.ink(), loc="upper left")
bio.panel(ax, "A", (0.2, 8.7))
bio.panel(ax, "B", (11.2, 8.7))
