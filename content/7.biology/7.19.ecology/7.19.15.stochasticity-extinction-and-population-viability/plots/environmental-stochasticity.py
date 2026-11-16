"""Environmental stochasticity: arithmetic versus geometric mean growth.

N_{t+1} = lambda_t N_t with lambda_t independent, equal to 1.5 (good year) or 0.6 (bad year) with
probability 1/2. The arithmetic mean E[lambda] = 1.05 > 1, but E[ln lambda] = (ln 1.5 + ln 0.6)/2 = -0.053 < 0.
A: 300 simulated populations (N0 = 100, seed 0; grey) over 100 years on a log scale; the expected size
N0 1.05^t (red) grows, the median N0 exp(-0.053 t) (blue) declines, and the sample mean (dashed) follows the
expectation only while some rare lucky paths are present in the sample. B: long-run growth rate
E[ln lambda] for log-normal lambda with arithmetic mean 1.05 as a function of the coefficient of variation
of lambda (exact: ln 1.05 - ln(1 + CV^2)/2) and the approximation ln(mean) - CV^2/2; the population
declines once the CV exceeds about 0.32.
"""

import numpy as np

import wikibio as bio
from wikibio import charts as C
from wikibio import quant as Q

P = bio.P
FS = bio.core.FONT
rng = np.random.default_rng(0)
T, R, N0 = 100, 300, 100.0
lam = np.where(rng.random((R, T)) < 0.5, 1.5, 0.6)
N = N0 * np.cumprod(np.c_[np.ones(R), lam], axis=1)
t = np.arange(T + 1)

fig, ax = bio.canvas(30.0, 10.0)
pa = C.axes_at(ax, (2.0, 1.6, 14.0, 6.8))
for k in range(R):
    pa.plot(t, N[k], color=P.muted(), lw=0.3, alpha=0.35)
pa.plot(t, N0 * 1.05 ** t, color=Q.line_color("negative"), lw=1.8, label="expected size N0 1.05^t")
g = 0.5 * (np.log(1.5) + np.log(0.6))
pa.plot(t, N0 * np.exp(g * t), color=Q.line_color("dna"), lw=1.8, label=f"median N0 exp({g:.3f} t)")
pa.plot(t, N.mean(axis=0), color=P.ink(), lw=1.1, ls=(0, (4, 2)), label="mean of the 300 simulations")
pa.set_yscale("log")
pa.set_ylim(1e-2, 1e5)
pa.set_xlim(0, T)
C.style_axes(pa, "year", "population size")
pa.legend(frameon=False, fontsize=FS["tiny"], labelcolor=P.ink(), loc="upper left")
bio.panel(ax, "A", (0.3, 9.6))
bio.label(ax, (2.0, 9.2), "Good and bad years: lambda = 1.5 or 0.6", size="small", bold=True, ha="left")

pb = C.axes_at(ax, (21.0, 1.6, 8.0, 6.8))
cv = np.linspace(0, 0.8, 200)
pb.plot(cv, np.log(1.05) - 0.5 * np.log(1 + cv ** 2), color=Q.line_color("protein"), lw=1.8,
        label="log-normal, exact")
pb.plot(cv, np.log(1.05) - 0.5 * cv ** 2, color=Q.line_color("atp"), lw=1.2, ls=(0, (4, 2)),
        label="ln(mean) - CV^2/2")
pb.axhline(0, color=P.muted(), lw=0.8)
pb.axhline(np.log(1.05), color=P.muted(), lw=0.6, ls=(0, (2, 2)))
pb.text(0.02, np.log(1.05) + 0.006, "ln E[lambda]", fontsize=FS["tiny"], color=P.muted())
cvc = np.sqrt(1.05 ** 2 - 1)
pb.plot([cvc], [0], "o", ms=4, color=Q.line_color("negative"))
pb.text(cvc + 0.02, 0.01, f"CV = {cvc:.2f}", fontsize=FS["tiny"], color=Q.line_color("negative"))
pb.set_xlim(0, 0.8)
C.style_axes(pb, "coefficient of variation of lambda", "E[ln lambda] (long-run growth)")
pb.legend(frameon=False, fontsize=FS["tiny"], labelcolor=P.ink(), loc="lower left")
bio.panel(ax, "B", (19.5, 9.6))
bio.label(ax, (21.0, 9.2), "Variability lowers long-run growth", size="small", bold=True, ha="left")
