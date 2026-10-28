"""Bayesian risk in a hereditary breast-cancer family. A: the pedigree, with ages at diagnosis and current
ages. B: the posterior probability that an untested daughter of a carrier is a carrier, as a function of her
age while she remains unaffected. C: her remaining risk of breast cancer to age 80, with and without a
negative test for the familial variant. Penetrance values are illustrative, in the range reported for
BRCA1 carriers and for the general population."""
import numpy as np
import matplotlib.pyplot as plt
import wikibio as bio
from wikibio import charts
from wikibio import genetics as G

P = bio.P
FT = bio.core.FONT
fig = plt.figure(figsize=(12.4, 4.6))
axp = fig.add_axes([0.0, 0.02, 0.34, 0.96])
axp.set_xlim(0, 6.4)
axp.set_ylim(0, 5.2)
axp.set_aspect("equal")
axp.axis("off")

ped = G.Pedigree()
ped.person("I-1", "M", note="d. 70")
ped.person("I-2", "F", status="affected", note="breast, 52")
ped.person("II-1", "M")
ped.person("II-2", "F", status="affected", note="breast, 42")
ped.person("II-3", "F", status="affected", note="ovary, 55")
ped.person("III-1", "F", consultand=True, note="45 y, well")
ped.person("III-2", "M", note="40 y")
ped.union("I-1", "I-2", children=["II-2", "II-3"])
ped.union("II-1", "II-2", children=["III-1", "III-2"])
G.pedigree(axp, ped, origin=(2.0, 4.4), dx=1.2, dy=1.9, size=0.46, token="receptor", gen_x=0.7)
bio.label(axp, (3.2, 5.05), "A  A family with a $\\it{BRCA1}$ variant", size="small", bold=True)

# penetrance curves (illustrative)
age = np.arange(20, 81)
def pen(a, scale):
    return scale / (1 + np.exp(-(a - 50) / 9.0))
car = pen(age, 0.65) - pen(20, 0.65)
pop = pen(age, 0.12) - pen(20, 0.12)

b = fig.add_axes([0.42, 0.18, 0.26, 0.70])
post = 0.5 * (1 - car) / (0.5 * (1 - car) + 0.5 * (1 - pop))
b.plot(age, post, color=charts.line("receptor"), lw=2)
b.axhline(0.5, color=P.muted(), lw=0.7, ls=":")
b.text(22, 0.515, "prior 1/2", fontsize=FT["tiny"], color=P.muted())
k = list(age).index(45)
b.plot([45], [post[k]], "o", color=charts.line("receptor"), ms=5)
b.annotate(f"at 45 y: {post[k]:.2f}", (45, post[k]), textcoords="offset points", xytext=(8, 6),
           fontsize=FT["tiny"], color=P.muted())
b.set_ylim(0, 0.6)
charts.style_axes(b, "current age, still unaffected", "P(carrier)")
charts.title(b, "B  Posterior carrier probability")

c = fig.add_axes([0.77, 0.18, 0.21, 0.70])
rem_car = (car[-1] - car[k]) / (1 - car[k])
rem_pop = (pop[-1] - pop[k]) / (1 - pop[k])
vals = [post[k] * rem_car + (1 - post[k]) * rem_pop, rem_pop, rem_pop]
labels = ["untested", "negative test", "population"]
cols = ["receptor", "dna", "neutral"]
c.bar(np.arange(3), vals, width=0.6, color=[P.fill(t) for t in cols], edgecolor=[P.edge(t) for t in cols], lw=0.9)
for i, v in enumerate(vals):
    c.text(i, v + 0.008, f"{v:.0%}", ha="center", fontsize=FT["tiny"], color=P.ink())
c.set_xticks(np.arange(3))
c.set_xticklabels(labels, fontsize=FT["tiny"])
c.set_ylim(0, max(vals) * 1.3)
charts.style_axes(c, None, "risk from 45 to 80 years")
charts.title(c, "C  Remaining risk")
