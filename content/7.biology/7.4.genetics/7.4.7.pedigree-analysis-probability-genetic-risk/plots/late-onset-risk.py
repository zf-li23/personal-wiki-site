"""Age-dependent penetrance and the risk of an unaffected relative (illustrative). A: cumulative probability
F(t) that a carrier of a dominant late-onset allele (as in Huntington disease) has shown symptoms by age t,
modeled as a logistic distribution of the age at onset with mean 45 years and scale 6 years. B: posterior
probability that the child of an affected parent (prior 1/2) is a carrier, given that the child is still
unaffected at age t, (1 - F) / (2 - F), and the corresponding prior risk for that person's own child (half of it)."""
import numpy as np
import matplotlib.pyplot as plt
import wikibio as bio
from wikibio import charts

P = bio.P
FT = bio.core.FONT
t = np.linspace(0, 80, 400)
F = 1 / (1 + np.exp(-(t - 45) / 6))
fig, axs = plt.subplots(1, 2, figsize=(10.0, 3.8))
fig.subplots_adjust(left=0.08, right=0.98, bottom=0.17, top=0.9, wspace=0.28)
a = axs[0]
a.plot(t, F, color=charts.line("negative"), lw=2)
a.set_ylim(0, 1.02)
charts.style_axes(a, "age t / years", "F(t): carriers affected by age t")
charts.title(a, "A  Age-dependent penetrance (illustrative)")
b = axs[1]
post = (1 - F) / (2 - F)
b.plot(t, post, color=charts.line("receptor"), lw=2, label="unaffected child of an affected parent")
b.plot(t, post / 2, color=charts.line("dna"), lw=1.5, ls="--", label="that person's child")
for tt in (30, 45, 60):
    pp = (1 - 1 / (1 + np.exp(-(tt - 45) / 6))) / (2 - 1 / (1 + np.exp(-(tt - 45) / 6)))
    b.plot([tt], [pp], "o", color=charts.line("receptor"), ms=4)
    b.annotate(f"{pp:.2f}", (tt, pp), textcoords="offset points", xytext=(4, 5), fontsize=FT["tiny"], color=P.muted())
b.set_ylim(0, 0.55)
b.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="lower left")
charts.style_axes(b, "age t of the unaffected relative / years", "P(carrier)")
charts.title(b, "B  Posterior carrier probability")
