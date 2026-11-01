"""Dose-mortality of flour beetles exposed for five hours to gaseous carbon disulphide (Bliss 1935,
Annals of Applied Biology 22:134; eight concentrations, 481 beetles). Observed proportions killed (circles)
against log10 concentration (mg/L), with binomial regressions under the logit, probit and complementary
log-log links fitted by maximum likelihood. The dotted line marks the logit estimate of the median lethal
concentration, 59.1 mg/L (95 % interval 58.1-60.2). The residual deviances are 11.2 (logit), 10.1 (probit)
and 3.4 (complementary log-log) on 6 degrees of freedom.
"""
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
import wikibio as bio
from wikibio import charts

P = bio.P
FT = bio.core.FONT
x = np.array([1.6907, 1.7242, 1.7552, 1.7842, 1.8113, 1.8369, 1.8610, 1.8839])
n = np.array([59, 60, 62, 56, 63, 59, 62, 60])
k = np.array([6, 13, 18, 28, 52, 53, 61, 60])
links = {
    "logit": (lambda e: 1 / (1 + np.exp(-e)), lambda e: np.exp(-e) / (1 + np.exp(-e)) ** 2, "rna"),
    "probit": (stats.norm.cdf, stats.norm.pdf, "dna"),
    "cloglog": (lambda e: 1 - np.exp(-np.exp(e)), lambda e: np.exp(e - np.exp(e)), "plant"),
}
X = np.column_stack([np.ones(x.size), x])
fits = {}
for name, (F, f, tok) in links.items():
    b = np.array([-30.0, 17.0]) if name != "logit" else np.array([-60.0, 34.0])
    for _ in range(50):
        eta = X @ b
        mu = np.clip(F(eta), 1e-10, 1 - 1e-10)
        d = f(eta)
        w = n * d**2 / (mu * (1 - mu))
        z = eta + (k / n - mu) / d
        b = np.linalg.solve(X.T @ (X * w[:, None]), X.T @ (w * z))
    fits[name] = b
fig, ax = plt.subplots(figsize=(6.4, 3.8))
fig.subplots_adjust(left=0.12, right=0.97, bottom=0.15, top=0.95)
g = np.linspace(1.67, 1.90, 300)
for name, (F, f, tok) in links.items():
    b = fits[name]
    ax.plot(g, F(b[0] + b[1] * g), color=charts.line(tok), lw=1.6, label=name)
ax.plot(x, k / n, "o", ms=6, color=P.fill("neutral"), mec=P.ink(), mew=0.8, label="observed")
ld = -fits["logit"][0] / fits["logit"][1]
ax.axvline(ld, color=P.muted(), lw=0.8, ls=":")
ax.axhline(0.5, color=P.muted(), lw=0.6, ls=":")
ax.text(ld + 0.003, 0.05, f"LD50 = {10 ** ld:.1f} mg/L", fontsize=FT["tiny"], color=P.ink())
ax.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="upper left")
charts.style_axes(ax, "log10 concentration of CS2 / (mg/L)", "proportion killed")
