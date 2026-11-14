# The marginal value theorem applied to load size and copulation time (illustrative parameters).
# A: a starling's loading curve, the cumulative number of leatherjackets in its beak after searching for t s,
# g(t) = 9 (1 - exp(-0.03 t)); for a round-trip travel time tau the load that maximizes the rate of delivery
# g(t) / (tau + t) is found by the tangent from (-tau, 0) (tau = 10 s and 60 s). B: the predicted optimal load
# as a function of round-trip time: the continuous optimum (line) and the best whole number of prey (steps),
# the form of the prediction tested by Kacelnik (1984) with parent starlings collecting mealworms 8 to 600 m
# from the nest. C: male dung flies (Parker 1970): proportion of a female's eggs fertilized as a function of
# copulation time, f(t) = 1 - exp(-0.064 t); with an average of 156.5 min spent guarding a female and finding
# the next one, the tangent gives an optimal copulation of about 41 min, close to the observed 36 min.
import numpy as np

import wikibio as bio
from wikibio import behaviour as bh
from wikibio import quant

P = bio.P
fig, ax = bio.canvas(28.0, 9.8)
g = bh.gain(9.0, 0.03)

# ---- A ------------------------------------------------------------------------------------------------
pa = quant.Plot(ax, (1.9, 1.8, 7.4, 6.4), (-60, 100), (0, 10), xlabel="Time / s",
                ylabel="Load (leatherjackets)", xticks=[-60, -30, 0, 50, 100], yticks=[0, 2, 4, 6, 8, 10])
bio.panel(ax, "A", (0.2, 9.6))
pa.span(-60, 0, "neutral", strength=0.82)
pa.text(-30, 9.7, "round trip", va="top", color=P.muted())
pa.text(50, 9.7, "searching at the site", va="top", color=P.muted())
res = bh.mvt_panel(pa, g, [10.0, 60.0], ["dna", "rna"])
for (tau, ts, rs), tok, xy in zip(res, ("dna", "rna"), ((26, 3.1), (52, 5.4))):
    pa.text(xy[0], xy[1], f"τ = {tau:g} s: load {float(g(ts)):.1f}", ha="left", token=tok)

# ---- B ------------------------------------------------------------------------------------------------
pb = quant.Plot(ax, (11.8, 1.8, 6.4, 6.4), (0, 100), (0, 8), xlabel="Round-trip travel time τ / s",
                ylabel="Optimal load", xticks=[0, 25, 50, 75, 100], yticks=[0, 2, 4, 6, 8])
bio.panel(ax, "B", (10.2, 9.6))
taus = np.linspace(0.5, 100, 200)
cont = [float(g(bh.mvt_optimum(g, t, 400)[0])) for t in taus]
pb.line(taus, cont, "dna", lw=1.6, dashed=True)
n = np.arange(1, 9)
tn = -np.log(1 - n / 9.0) / 0.03          # time needed to collect n prey
best = [n[np.argmax(n / (t + tn))] for t in taus]
pb.steps(taus, best, "positive", lw=2.2)
pb.text(55, 4.3, "best whole load", ha="left", token="positive")
pb.text(40, 7.3, "continuous optimum", ha="left", token="dna")
pb.text(98, 0.6, "far sites: bigger loads", ha="right", color=P.muted())

# ---- C ------------------------------------------------------------------------------------------------
f = bh.gain(1.0, 0.0636)
pc = quant.Plot(ax, (21.2, 1.8, 6.3, 6.4), (-160, 90), (0, 1.1), xlabel="Time / min",
                ylabel="Proportion of eggs fertilized", xticks=[-150, -100, -50, 0, 50], yticks=[0, 0.5, 1.0])
bio.panel(ax, "C", (19.6, 9.6))
pc.span(-160, 0, "neutral", strength=0.82)
pc.text(-80, 1.07, "guard + search, S = 156.5", va="top", color=P.muted())
r2 = bh.mvt_panel(pc, f, [156.5], ["negative"])
_, ts, rs = r2[0]
pc.text(-75, 0.86, f"predicted optimum {ts:.0f} min", ha="left", token="negative")
pc.vline(36, token="ink")
pc.text(44, 0.12, "observed\n36 min", ha="left")
