# How cargo moves through the Golgi stack: predictions of three models for a pulse of cargo that enters the
# cis face at t = 0 (mean transit time 20 min in each case). Cisternal maturation: cargo stays in its cisterna,
# which matures from cis to trans over a nearly fixed time, so exit is delayed and synchronous (Erlang
# distribution with many stages, here 16). Stepwise vesicular transport through four stable cisternae: each
# step is a random, first-order event, so exit follows an Erlang distribution with four stages (a lag, then
# a broad peak). Rapid partitioning (cargo mixes quickly among all cisternae and leaves from any of them):
# exit is first order, exponential without lag. A: probability density of the exit time (curves) and
# histograms of 400 simulated molecules per model. B: the fraction of
# the pulse still in the Golgi; measurements of the export of fluorescent cargo from the Golgi of mammalian
# cells show the exponential behaviour (Patterson et al., Cell 133:1055, 2008), while maturation is seen
# directly in yeast and for large cargo such as procollagen.
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import gamma

from wikibio import quant

mean = 20.0
t = np.linspace(0, 80, 800)
models = [(16, "negative", "cisternal maturation (16 stages)"), (4, "protein", "stepwise vesicles (4 cisternae)"),
          (1, "positive", "rapid partitioning")]
fig, axs = plt.subplots(1, 2, figsize=(9.5, 3.4))
rng = np.random.default_rng(0)
for k, tok, lab in models:
    d = gamma(a=k, scale=mean / k)
    axs[0].plot(t, d.pdf(t), color=quant.line_color(tok), lw=1.8, label=lab)
    axs[1].plot(t, d.sf(t), color=quant.line_color(tok), lw=1.8, label=lab)
    sample = d.rvs(size=400, random_state=rng)
    axs[0].hist(sample, bins=np.arange(0, 81, 4), density=True, color=quant.line_color(tok), histtype="step", lw=0.8)
axs[0].set(xlabel="exit time / min", ylabel="probability density", title="A  When does a cargo molecule leave?")
axs[1].set(xlabel="t / min", ylabel="fraction still in the Golgi", title="B  Export of a pulse", yscale="log", ylim=(1e-3, 1.2))
axs[1].legend(frameon=False, fontsize=7.5, loc="lower left")
for a in axs:
    a.spines[["top", "right"]].set_visible(False)
    a.title.set_fontsize(10)
fig.tight_layout()
