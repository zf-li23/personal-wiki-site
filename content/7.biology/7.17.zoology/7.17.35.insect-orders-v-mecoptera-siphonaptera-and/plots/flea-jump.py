# Why fleas need a catapult. For a jump with take-off speed v reached over a time t at constant
# acceleration, the mean power per unit body mass is v^2 / (2t) and the peak power is v^2 / t. Values for the
# rabbit flea Spilopsyllus cuniculi: v about 1 m/s and acceleration about 1350 m/s^2, so t = v/a is about
# 0.75 ms (Bennet-Clark and Lucey 1967). Muscle can deliver at most a few hundred watts per kilogram of
# muscle; with jumping muscle a small fraction of body mass, direct muscle action falls short by one to two
# orders of magnitude. Energy stored slowly in a resilin pad and released by a catch removes the limit.
import numpy as np
import wikibio as bio
from wikibio import charts

P = bio.P
fig, ax = bio.canvas(16, 9.5)
a = charts.axes_at(ax, (1.9, 1.4, 13.2, 7.4))
t = np.logspace(-4, -1, 200)  # take-off time, s
for v, tok, lab in ((1.0, "negative", "v = 1.0 m/s (flea)"), (0.5, "enzyme", "v = 0.5 m/s"), (2.0, "protein", "v = 2.0 m/s")):
    a.plot(t * 1e3, v ** 2 / t, color=P.edge(tok), lw=2, label=f"peak power needed, {lab}")
a.axhspan(10, 100, color=P.light("positive"), lw=0)
a.text(70, 25, "muscle acting directly\n(about 10-100 W per kg body mass)", ha="right", va="center", fontsize=7, color=P.ink())
tf = 1.0 / 1350
a.plot([tf * 1e3], [1.0 / tf], "o", color=P.edge("negative"), ms=5)
a.annotate("rabbit flea: t = 0.75 ms,\nabout 1300 W/kg", xy=(tf * 1e3, 1.0 / tf), xytext=(2.0, 6000), fontsize=7,
           color=P.ink(), arrowprops=dict(arrowstyle="-", color=P.muted(), lw=0.7))
a.set_xscale("log")
a.set_yscale("log")
a.set_xlim(0.1, 100)
a.set_ylim(1, 1e5)
a.set_xlabel("Take-off time, t (ms)")
a.set_ylabel("Peak power per body mass (W/kg)")
a.legend(fontsize=7, frameon=False, loc="upper right")
