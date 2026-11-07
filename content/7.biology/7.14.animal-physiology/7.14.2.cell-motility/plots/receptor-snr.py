# How well can a cell read a gradient from receptor counts?
# N receptors, half at the front and half at the rear; each is occupied with probability
# p = c / (c + Kd), independently. The bound counts are binomial; the front-rear difference caused by a
# relative concentration difference dc/c has mean (N/2) p (1-p) (dc/c) and variance N p (1-p), so the
# signal-to-noise ratio of one snapshot is SNR = (1/2) sqrt(N p (1-p)) (dc/c), largest at c = Kd.
# Averaging over a time T with receptor correlation time tau_b multiplies it by about sqrt(T / tau_b).
# Lines: N = 10^4 receptors, dc/c = 1 %, 2 % and 5 %; dashed: dc/c = 1 % averaged over T/tau_b = 30.
import numpy as np

import wikibio as bio
from wikibio import charts

P = bio.P
fig, ax = bio.canvas(14.0, 9.4)
pa = charts.axes_at(ax, (2.3, 1.5, 11.0, 7.0))
N = 1e4
c = np.logspace(-3, 3, 400)
p = c / (1 + c)
base = 0.5 * np.sqrt(N * p * (1 - p))
for g, tok in ((0.01, "dna"), (0.02, "protein"), (0.05, "rna")):
    pa.loglog(c, base * g, color=charts.line(tok), lw=1.7, label=f"snapshot, ΔC/C = {int(g * 100)} %")
pa.loglog(c, base * 0.01 * np.sqrt(30), color=charts.line("dna"), lw=1.5, ls="--",
          label="ΔC/C = 1 %, averaged over 30 τ_b")
pa.axhline(1, color=P.muted(), lw=0.8, ls=":")
pa.text(1.2e-3, 1.1, "SNR = 1", fontsize=7.5, color=P.muted())
pa.axvline(1, color=P.muted(), lw=0.6, ls=":")
pa.text(1.15, 5, "C = Kd", fontsize=7.5, color=P.muted())
leg = pa.legend(loc="lower center", fontsize=7.5, frameon=False)
for txt in leg.get_texts():
    txt.set_color(P.ink())
pa.set_xlim(1e-3, 1e3)
pa.set_ylim(0.01, 10)
charts.style_axes(pa, "background concentration C / Kd", "signal-to-noise ratio")
charts.title(pa, "Front–rear receptor difference, N = 10⁴ receptors")
