# The scalar property of interval timing (simulation of a pacemaker-accumulator model in the spirit of scalar
# expectancy theory, Gibbon 1977; illustrative parameters, seed 0). A: the peak procedure. On occasional
# trials without food, a rat trained with food 15, 30 or 60 s after the onset of a signal responds in a
# high-rate state that starts and stops around the trained time; on each simulated trial the start and stop
# times are T s1 and T s2, with s1 ~ N(0.55, 0.12) and s2 ~ N(1.45, 0.25) (500 trials per interval). The mean
# response rate peaks near T, and the spread grows in proportion to T. B: the same functions with time
# divided by T and rate by its maximum superimpose (superposition), the signature of timing errors that are
# proportional to the interval timed (Weber's law for time). C: temporal bisection: after training to report
# "short" after 2 s and "long" after 8 s, the probability of "long" for intermediate durations, if perceived
# duration is log-normal (s.d. of log duration 0.25) and the animal compares it with the midpoint of the logs:
# the point of subjective equality is the geometric mean, 4 s, as found in rats (Church and Deluty 1977).
import numpy as np
from scipy.stats import norm

import wikibio as bio
from wikibio import quant

P = bio.P
rng = np.random.default_rng(0)
fig, ax = bio.canvas(30.0, 9.4)

t = np.linspace(0, 150, 601)
curves = {}
for T in (15, 30, 60):
    s1 = rng.normal(0.55, 0.12, 500)
    s2 = rng.normal(1.45, 0.25, 500)
    on = (t[None, :] >= (T * s1)[:, None]) & (t[None, :] <= (T * s2)[:, None])
    curves[T] = on.mean(axis=0)
toks = {15: "rna", 30: "protein", 60: "dna"}

pa = quant.Plot(ax, (1.9, 1.8, 7.4, 6.4), (0, 150), (0, 1.05), xlabel="Time since signal onset / s",
                ylabel="Response rate (relative)", xticks=[0, 15, 30, 60, 90, 120, 150], yticks=[0, 0.5, 1])
bio.panel(ax, "A", (0.2, 9.2))
for T, c in curves.items():
    pa.line(t, c, toks[T], lw=2.0)
    pa.text(T + {15: -4, 30: 6, 60: 8}[T], c.max() + 0.03, f"T = {T} s", va="bottom", token=toks[T],
            ha={15: "right", 30: "left", 60: "left"}[T])

pb = quant.Plot(ax, (11.9, 1.8, 7.0, 6.4), (0, 2.5), (0, 1.05), xlabel="Time / T", ylabel="Rate / maximum rate",
                xticks=[0, 0.5, 1, 1.5, 2, 2.5], yticks=[0, 0.5, 1])
bio.panel(ax, "B", (10.2, 9.2))
for T, c in curves.items():
    m = t / T <= 2.5
    pb.line((t / T)[m], (c / c.max())[m], toks[T], lw=1.8, dashed=(T == 30), dotted=(T == 60))
pb.text(1.7, 0.85, "15, 30 and 60 s superimpose", ha="left", size="tiny", color=P.muted())

pc = quant.Plot(ax, (22.0, 1.8, 7.0, 6.4), (np.log10(1.5), np.log10(10)), (0, 1.05), xlabel="Signal duration / s",
                ylabel='Proportion of "long" responses', xticks=[(np.log10(2), "2"), (np.log10(4), "4"), (np.log10(8), "8")],
                yticks=[0, 0.5, 1])
bio.panel(ax, "C", (20.3, 9.2))
d = np.geomspace(1.5, 10, 300)
crit = 0.5 * (np.log(2) + np.log(8))
pc.line(np.log10(d), norm.cdf((np.log(d) - crit) / 0.25), "dna", lw=2.0)
pc.hline(0.5)
pc.vline(np.log10(4), text="geometric mean 4 s")
pc.vline(np.log10(5), token="negative", text="arithmetic 5 s", top=False)
for x in (2, 8):
    pc.points([np.log10(x)], [norm.cdf((np.log(x) - crit) / 0.25)], "dna", r=0.11)
