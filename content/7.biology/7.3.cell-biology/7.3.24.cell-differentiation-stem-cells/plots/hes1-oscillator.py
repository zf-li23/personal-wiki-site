"""The Hes1 oscillator: delayed negative autoregulation (Monk 2003; data of Hirata and colleagues 2002).

A: Hes1 protein represses transcription of its own gene. Between a change in the protein level and the
resulting change in protein synthesis lies a delay tau (transcription of the gene, splicing, export of the
mRNA and translation, of the order of 10-20 min).
B: the delay differential equations
    dm/dt = alpha_m / (1 + (p(t - tau) / p0)^n) - mu_m m,      dp/dt = alpha_p m - mu_p p,
with m the mRNA and p the protein (molecules per cell), half-lives 24 min (mRNA) and 22 min (protein), so
mu_m = 0.029 and mu_p = 0.031 per min, alpha_m = 1 per min, alpha_p = 1 per min, p0 = 100, n = 5, tau = 18.7 min.
mRNA and protein oscillate with a period of about 2 h, the protein peaking after the mRNA.
C: the period and the peak-to-trough amplitude of the protein for delays from 0 to 40 min: below a
critical delay the steady state is stable (damped oscillations, amplitude zero); above it the oscillation
is sustained (a Hopf bifurcation), and the period grows with the delay, roughly as 2 (tau + 1/mu_m + 1/mu_p)
for long delays.
"""

import numpy as np

import wikibio as bio
from wikibio import charts, quant

P = bio.P
am, ap, mm, mp, p0, n = 1.0, 1.0, np.log(2) / 24, np.log(2) / 22.3, 100.0, 5


def run(tau, T=1500.0, dt=0.05):
    steps = int(T / dt)
    lag = int(round(tau / dt))
    m = np.zeros(steps + 1)
    p = np.zeros(steps + 1)
    m[0], p[0] = 3.0, 100.0
    for i in range(steps):
        pd = p[i - lag] if i >= lag else p[0]
        m[i + 1] = m[i] + dt * (am / (1 + (pd / p0) ** n) - mm * m[i])
        p[i + 1] = p[i] + dt * (ap * m[i] - mp * p[i])
    return np.arange(steps + 1) * dt, m, p


t, m, p = run(18.7, T=2400.0)

fig, ax = bio.canvas(28.0, 9.4)
bio.panel(ax, "A", (0.1, 9.3))
bio.dna(ax, (0.8, 4.0), (6.4, 4.0), style="duplex")
bio.box(ax, (4.2, 4.0), 2.0, 0.55, "dna", text="Hes1", size="small", italic=True)
bio.arrow(ax, (4.2, 4.4), (4.2, 5.7), kind="process")
bio.strand(ax, (3.2, 6.1), (5.4, 6.1), token="mrna")
bio.label(ax, (5.9, 6.1), "mRNA", size="tiny", ha="left")
bio.arrow(ax, (4.2, 6.5), (4.2, 7.6), kind="process")
for k in range(3):
    bio.protein(ax, (3.6 + 0.6 * k, 8.1), 0.5, 0.42, "protein")
bio.label(ax, (5.7, 8.1), "Hes1 protein", size="tiny", ha="left")
bio.arrow(ax, (3.2, 8.1), (2.4, 4.35), kind="inhibition", bend=0.35)
bio.label(ax, (0.5, 6.4), "represses\nits own gene", size="tiny", ha="left")
bio.label(ax, (3.6, 2.9), "delay τ: transcription, splicing,\nexport, translation", size="tiny", color=P.muted())

bio.panel(ax, "B", (8.2, 9.3))
pb = charts.axes_at(ax, (9.6, 1.4, 9.0, 7.4))
sel = (t > 1800) & (t < 2400)
pb.plot(t[sel] - 1800, m[sel], color=quant.line_color("mrna"), lw=2.0, label="Hes1 mRNA m")
pb2 = pb.twinx()
pb2.set_facecolor("none")
pb2.plot(t[sel] - 1800, p[sel], color=quant.line_color("protein"), lw=2.0, label="Hes1 protein p")
charts.style_axes(pb, "time / min", "mRNA (molecules per cell)")
charts.style_axes(pb2, None, "protein (molecules per cell)", box=False)
pb2.spines["right"].set_visible(True)
pb2.spines["right"].set_color(P.muted())
pb2.spines["left"].set_visible(False)
pb.set_xlim(0, 600)
h1, l1 = pb.get_legend_handles_labels()
h2, l2 = pb2.get_legend_handles_labels()
pb.legend(h1 + h2, l1 + l2, frameon=False, fontsize=bio.core.FONT["tiny"], labelcolor=P.ink(), loc="upper right")
charts.title(pb, "Oscillation with a period of about 2 h")

bio.panel(ax, "C", (20.4, 9.3))
pc = charts.axes_at(ax, (21.9, 1.4, 5.6, 7.4))
taus = np.arange(0, 41, 2.0)
per, amp = [], []
for tau in taus:
    tt, mm_, pp = run(tau, T=3000.0, dt=0.1)
    s = tt > 1800
    x = pp[s]
    a = x.max() - x.min()
    amp.append(a)
    pk = np.where((x[1:-1] > x[:-2]) & (x[1:-1] > x[2:]))[0]
    per.append(np.diff(tt[s][1:-1][pk]).mean() if a > 1 and len(pk) > 2 else np.nan)
pc.plot(taus, per, color=quant.line_color("protein"), lw=2.0, marker="o", ms=3)
pc3 = pc.twinx()
pc3.set_facecolor("none")
pc3.plot(taus, amp, color=quant.line_color("neutral"), lw=1.6, ls=(0, (4, 2)))
charts.style_axes(pc, "delay τ / min", "period / min")
charts.style_axes(pc3, None, "protein amplitude (dashed)")
pc3.spines["right"].set_visible(True)
pc3.spines["right"].set_color(P.muted())
pc3.spines["left"].set_visible(False)
pc.set_xlim(0, 40)
pc.axvline(18.7, color=P.muted(), lw=0.8, ls=(0, (2, 2)))
charts.title(pc, "Period grows with the delay")
