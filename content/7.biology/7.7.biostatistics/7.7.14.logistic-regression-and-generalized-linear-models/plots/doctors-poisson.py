"""Poisson regression for coronary deaths among British male doctors in ten years of follow-up (Doll and
Hill 1966; tabulated in Breslow and Day 1987). A: observed death rates per 100 000 person-years (points)
and the fitted rates (lines) of the model log(deaths) = log(person-years) + b0 + b1 age + b2 age^2 +
b3 smoke + b4 smoke x age, with age coded 1-5 for the ten-year groups (residual deviance 1.6 on 5 df).
B: the fitted smoker/non-smoker rate ratio exp(b3 + b4 age) with a 95 % band, and the observed
age-specific ratios.
"""
import matplotlib.pyplot as plt
import numpy as np
import wikibio as bio
from wikibio import charts

P = bio.P
FT = bio.core.FONT
age = np.tile(np.arange(1, 6), 2).astype(float)
smoke = np.r_[np.ones(5), np.zeros(5)]
deaths = np.array([32, 104, 206, 186, 102, 2, 12, 28, 28, 31], float)
py = np.array([52407, 43248, 28612, 12663, 5317, 18790, 10673, 5710, 2585, 1462], float)
X = np.column_stack([np.ones(10), age, age**2, smoke, smoke * age])
b = np.array([np.log(deaths.sum() / py.sum()), 0, 0, 0, 0])
for _ in range(50):
    mu = py * np.exp(X @ b)
    b = b + np.linalg.solve(X.T @ (X * mu[:, None]), X.T @ (deaths - mu))
mu = py * np.exp(X @ b)
cov = np.linalg.inv(X.T @ (X * mu[:, None]))
labels = ["35-44", "45-54", "55-64", "65-74", "75-84"]
fig, axs = plt.subplots(1, 2, figsize=(9.8, 3.6))
fig.subplots_adjust(left=0.08, right=0.98, bottom=0.17, top=0.87, wspace=0.3)
a = np.linspace(1, 5, 100)
ax = axs[0]
for s, tok, name, m in ((1, "rna", "smokers", "o"), (0, "dna", "non-smokers", "s")):
    sel = smoke == s
    ax.plot(age[sel], deaths[sel] / py[sel] * 1e5, m, ms=6, color=P.fill(tok), mec=charts.line(tok), label=name)
    eta = b[0] + b[1] * a + b[2] * a**2 + s * (b[3] + b[4] * a)
    ax.plot(a, np.exp(eta) * 1e5, color=charts.line(tok), lw=1.5)
ax.set_yscale("log")
ax.set_xticks(range(1, 6))
ax.set_xticklabels(labels, fontsize=FT["tiny"])
ax.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="lower right")
charts.style_axes(ax, "age / years", "deaths per 100 000 person-years")
charts.title(ax, "A  Observed and fitted rates")
ax = axs[1]
L = np.column_stack([np.zeros((a.size, 3)), np.ones(a.size), a])
est = L @ b
se = np.sqrt(np.einsum("ij,jk,ik->i", L, cov, L))
ax.fill_between(a, np.exp(est - 1.96 * se), np.exp(est + 1.96 * se), color=P.fill("rna"), alpha=0.35, lw=0)
ax.plot(a, np.exp(est), color=charts.line("rna"), lw=1.7)
obs = (deaths[:5] / py[:5]) / (deaths[5:] / py[5:])
ax.plot(range(1, 6), obs, "o", ms=5, color=P.fill("neutral"), mec=P.ink(), mew=0.7)
ax.axhline(1, color=P.muted(), lw=0.8, ls="--")
ax.set_yscale("log")
ax.set_yticks([0.5, 1, 2, 5, 10])
ax.set_yticklabels(["0.5", "1", "2", "5", "10"])
ax.set_xticks(range(1, 6))
ax.set_xticklabels(labels, fontsize=FT["tiny"])
charts.style_axes(ax, "age / years", "rate ratio, smokers vs non-smokers")
charts.title(ax, "B  Fitted rate ratio exp(b3 + b4 age)")
