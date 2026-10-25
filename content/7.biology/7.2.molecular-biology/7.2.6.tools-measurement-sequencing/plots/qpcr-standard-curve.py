# Quantitative PCR. A: simulated amplification curves for tenfold dilutions of a template (1e1 to 1e6 copies,
# three replicates each) from a logistic model of fluorescence with efficiency E = 0.95 and a plateau; the
# threshold line (dashed) defines the quantification cycle Cq. B: Cq against the logarithm of the input copy
# number; the slope of the regression line is -1/log10(1 + E), which is -3.32 for E = 1 (a tenfold difference
# corresponds to log2(10) = 3.32 cycles), and the efficiency is recovered as E = 10^(-1/slope) - 1.
import numpy as np
import wikibio as bio
from wikibio import charts as C

P = bio.P
rng = np.random.default_rng(0)
E, PLATEAU, THR = 0.95, 1.0, 0.08
cycles = np.arange(0, 46)
inputs = np.array([1e1, 1e2, 1e3, 1e4, 1e5, 1e6])
toks = ["protein", "channel", "enzyme", "carbohydrate", "antibody", "receptor"]

fig, ax = bio.canvas(20.0, 8.2)
a = C.axes_at(ax, (1.6, 1.3, 8.2, 5.6))
cqs, logs = [], []
for N0, tok in zip(inputs, toks):
    for rep in range(3):
        n0 = N0 * np.exp(0.05 * rng.standard_normal())
        N = n0 * (1 + E) ** cycles
        F = PLATEAU * N / (N + 6e12) + 0.004 * rng.standard_normal(len(cycles))
        a.plot(cycles, F, color=C.line(tok), lw=1.2)
        above = np.where(F > THR)[0]
        k = above[0]
        cq = k - 1 + (THR - F[k - 1]) / (F[k] - F[k - 1])
        cqs.append(cq)
        logs.append(np.log10(n0))
a.axhline(THR, color=P.muted(), lw=0.9, ls=(0, (4, 3)))
a.text(0.5, THR * 1.25, "threshold", fontsize=bio.core.FONT["tiny"], color=P.muted())
a.set_xlim(0, 45)
a.set_ylim(0, 1.05)
C.style_axes(a, "cycle", "normalized fluorescence")
for N0, tok in zip(inputs, toks):
    i = int(np.log10(N0))
    a.plot([1.0, 2.6], [0.99 - 0.08 * (6 - i)] * 2, color=C.line(tok), lw=1.6)
    a.text(2.9, 0.99 - 0.08 * (6 - i), f"10$^{i}$ copies", color=P.ink(), fontsize=bio.core.FONT["tiny"], va="center")
bio.panel(ax, "A", (0.1, 8.1))
bio.label(ax, (0.6, 7.75), "Amplification curves of a tenfold dilution series", size="normal", bold=True, ha="left")

b = C.axes_at(ax, (12.2, 1.3, 6.8, 5.6))
logs, cqs = np.array(logs), np.array(cqs)
m, c = np.polyfit(logs, cqs, 1)
xx = np.linspace(0.6, 6.4, 10)
b.plot(xx, m * xx + c, color=P.muted(), lw=1.4)
for N0, tok in zip(inputs, toks):
    s = abs(logs - np.log10(N0)) < 0.4
    b.plot(logs[s], cqs[s], "o", ms=5, mfc=P.fill(tok), mec=C.line(tok), mew=0.9)
eff = 10 ** (-1 / m) - 1
b.text(2.9, 40.5, f"slope = {m:.2f}".replace("-", "−") + f"\n$E = 10^{{-1/\\mathrm{{slope}}}} - 1$ = {eff:.2f}\nideal slope −3.32",
       fontsize=bio.core.FONT["tiny"], color=P.ink(), va="top")
b.set_xlim(0.5, 6.5)
b.set_ylim(14, 42)
b.set_xticks([1, 2, 3, 4, 5, 6])
C.style_axes(b, "lg (input copies)", "$C_q$")
bio.panel(ax, "B", (10.9, 8.1))
bio.label(ax, (11.4, 7.75), "Standard curve", size="normal", bold=True, ha="left")
