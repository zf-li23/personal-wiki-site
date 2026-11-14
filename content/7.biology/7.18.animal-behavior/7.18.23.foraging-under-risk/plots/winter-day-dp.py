# A state-dependent model of a small bird's winter day, solved by stochastic dynamic programming
# (in the spirit of McNamara and Houston 1990; illustrative parameters). The day has T = 48 periods
# (about 15 min each); reserves x run from 0 (starved) to 40 units. In each period the bird rests
# (uses 1 unit; predation risk 0.0002) or forages (uses 1 unit and finds food worth 4 units with
# probability 0.6; predation risk 0.002 + b x, rising with body mass, b = 0.0004). At dusk it survives the
# night only if x >= 22. Backward induction gives V(x, t) = max over actions of
# (1 - mu) E[V(x', t + 1)], the maximal probability of surviving to the next morning.
# A: the optimal policy (forage in the green region, rest otherwise): the threshold below which the bird
# forages rises through the day. B: mean reserves of 4000 simulated birds that start at 10 units and follow
# the policy (starting reserves 6 to 14 units): reserves are kept low in the morning and built up in the afternoon, for three values of the
# mass-dependent predation cost b. C: proportion of the surviving birds foraging (running mean over five periods).
import numpy as np

import wikibio as bio
from wikibio import quant
from matplotlib.patches import Rectangle

P = bio.P
X, T, XC, G, PG, MUR, MU0 = 40, 48, 22, 4, 0.6, 0.0002, 0.002


def solve(b):
    V = np.zeros((T + 1, X + 1))
    V[T, XC:] = 1.0
    pol = np.zeros((T, X + 1), bool)
    for t in range(T - 1, -1, -1):
        for x in range(1, X + 1):
            xr = x - 1
            xg = min(x - 1 + G, X)
            vr = (1 - MUR) * V[t + 1, xr]
            vf = (1 - (MU0 + b * x)) * (PG * V[t + 1, xg] + (1 - PG) * V[t + 1, xr])
            pol[t, x] = vf > vr
            V[t, x] = max(vf, vr)
    return pol


def simulate(pol, b, n=4000, x0=10):
    rng = np.random.default_rng(1)
    x = rng.integers(x0 - 4, x0 + 5, n)
    alive = np.ones(n, bool)
    mean, frac = [x.mean()], []
    for t in range(T):
        a = pol[t, x] & alive
        frac.append(a[alive].mean())
        mu = np.where(a, MU0 + b * x, MUR)
        alive &= rng.random(n) > mu
        x = np.clip(x - 1 + G * (a & (rng.random(n) < PG)), 0, X)
        alive &= x > 0
        mean.append(x[alive].mean())
    return np.array(mean), np.array(frac)


fig, ax = bio.canvas(28.0, 9.8)
hours = lambda t: 8 + np.asarray(t) * 0.25  # noqa: E731  (day from 08:00 to 20:00)

# ---- A: policy -----------------------------------------------------------------------------------------
pa = quant.Plot(ax, (1.9, 1.8, 7.0, 6.4), (8, 20), (0, 40), xlabel="Time of day / h", ylabel="Reserves x",
                xticks=[8, 11, 14, 17, 20], yticks=[0, 10, 20, 30, 40])
bio.panel(ax, "A", (0.2, 9.6))
pol = solve(0.0004)
fc = P.mix(P.fill("positive"), P.surface(), 0.35 if not P.is_dark() else 0.55)
for t in range(T):
    for x in range(1, X + 1):
        if pol[t, x]:
            x0, y0 = pa.xy(hours(t), x - 0.5)
            x1, y1 = pa.xy(hours(t + 1), x + 0.5)
            ax.add_patch(Rectangle((x0, y0), x1 - x0, y1 - y0, facecolor=fc, edgecolor="none", zorder=pa.z - 1))
pa.hline(XC, token="negative", text="needed at dusk", side="right")
pa.text(10.5, 5.5, "forage", token="positive")
pa.text(11.5, 30, "rest", color=P.muted())

# ---- B: reserves -----------------------------------------------------------------------------------------
pb = quant.Plot(ax, (11.4, 1.8, 6.8, 6.4), (8, 20), (0, 32), xlabel="Time of day / h", ylabel="Mean reserves",
                xticks=[8, 11, 14, 17, 20], yticks=[0, 10, 20, 30])
bio.panel(ax, "B", (9.8, 9.6))
pc = quant.Plot(ax, (21.0, 1.8, 6.4, 6.4), (8, 20), (0, 1.05), xlabel="Time of day / h",
                ylabel="Proportion foraging", xticks=[8, 11, 14, 17, 20], yticks=[0, 0.5, 1])
bio.panel(ax, "C", (19.4, 9.6))
pb.hline(XC, token="negative", text="22", side="right")
for b, tok, style in ((0.0002, "dna", "-"), (0.0004, "positive", "-"), (0.0008, "rna", "--")):
    m, f = simulate(solve(b), b)
    pb.line(hours(np.arange(T + 1)), m, tok, lw=2.0, dashed=style == "--")
    fs = np.convolve(np.r_[f[:2], f, f[-2:]], np.ones(5) / 5, mode="valid")
    pc.line(hours(np.arange(T) + 0.5), fs, tok, lw=1.8, dashed=style == "--")
pb.legend([("low predation cost", "dna", "-"), ("medium", "positive", "-"), ("high", "rna", "--")], at=(12.0, 7.9))
pb.text(19.6, 3.0, "fattening late in the day", ha="right", color=P.muted())
