# Pulsatile GH and the smooth plasma IGF-1 it drives: a chain of low-pass filters.
# GH secretion: ~10-min bursts, small ones every ~3 h by day and a large one after sleep onset
# (23:00); plasma GH clearance half-life 20 min. Hepatic IGF-1 production follows GH through gene
# expression with a time constant of 6 h; plasma IGF-1 (mostly in the IGFBP-3/ALS ternary complex)
# has a half-life of ~15 h. Units: GH in ng/mL (illustrative), IGF-1 relative to its mean.
# B: amplitude gain of each first-order stage, 1 / sqrt(1 + (omega / k)^2), against the period of
# a sinusoidal input (2 pi / omega).
import numpy as np

import wikibio as bio
from wikibio import charts

P = bio.P
dt = 1.0 / 60.0  # h
t = np.arange(0, 24 * 8, dt)  # run 8 days; show the last two
sec = np.zeros_like(t)
for day in range(8):
    base = 24 * day
    for h in (8, 11, 14, 17, 20):
        sec += 18 * np.exp(-0.5 * ((t - base - h) / 0.08) ** 2)
    sec += 70 * np.exp(-0.5 * ((t - base - 23.5) / 0.1) ** 2)
    sec += 30 * np.exp(-0.5 * ((t - base - 26.0) / 0.1) ** 2)
kgh = np.log(2) / (20 / 60)
tau_m = 6.0
kigf = np.log(2) / 15.0
gh = np.zeros_like(t)
m = np.zeros_like(t)
igf = np.zeros_like(t)
gh[0] = 0.5
m[0] = 1.0
igf[0] = 1.0
for i in range(1, t.size):
    gh[i] = gh[i - 1] + dt * (sec[i - 1] - kgh * gh[i - 1] + 0.35 * kgh)
    m[i] = m[i - 1] + dt * (gh[i - 1] - m[i - 1]) / tau_m
    igf[i] = igf[i - 1] + dt * kigf * (m[i - 1] - igf[i - 1])
sel = t >= 24 * 6
tt = t[sel] - 24 * 6
igf_rel = igf[sel] / igf[sel].mean()
gh_s = gh[sel]

fig, ax = bio.canvas(24.0, 9.6)
bio.panel(ax, "A", (0.2, 9.5))
pa = charts.axes_at(ax, (2.2, 1.5, 9.0, 6.9))
pa.plot(tt, gh_s, color=charts.line("dna"), lw=1.3)
pa.set_ylim(0, gh_s.max() * 1.15)
pa.set_xlim(0, 48)
pa.set_xticks(range(0, 49, 6))
pa.set_xticklabels([f"{(h) % 24:02d}:00" for h in range(0, 49, 6)], rotation=0)
for d0 in (0, 24):
    pa.axvspan(d0 + 23, d0 + 24 + 7 if d0 + 31 <= 48 else 48, color=P.mix(P.muted(), P.surface(), 0.85), lw=0,
               zorder=0)
pa2 = pa.twinx()
pa2.plot(tt, igf_rel, color=charts.line("positive"), lw=1.9)
pa2.set_ylim(0.9, 1.1)
pa.text(0.5, gh_s.max() * 1.08, "GH (t½ 20 min)", color=charts.line("dna"), fontsize=7.5)
pa2.text(47.5, 1.06, f"IGF-1 (t½ ~15 h): ±{(igf_rel.max() - igf_rel.min()) / 2 * 100:.0f}%",
         color=charts.line("positive"), fontsize=7.5, ha="right", va="bottom")
pa.text(29, gh_s.max() * 0.95, "sleep", fontsize=7.0, color=P.muted())
charts.style_axes(pa, "clock time", "plasma GH / (ng mL⁻¹)")
charts.style_axes(pa2, None, "IGF-1 / mean", box=True)
pa2.spines["top"].set_visible(False)
pa2.spines["left"].set_visible(False)
charts.title(pa, "Pulsatile GH, nearly constant IGF-1")

bio.panel(ax, "B", (12.6, 9.5))
pb = charts.axes_at(ax, (14.6, 1.5, 8.8, 6.9))
period = np.logspace(-1, 2.3, 300)  # h
w = 2 * np.pi / period
for k, tok, lab in ((kgh, "dna", "GH clearance (t½ 20 min)"), (1 / tau_m, "protein", "hepatic IGF-1 synthesis (τ 6 h)"),
                    (kigf, "positive", "IGF-1 clearance (t½ 15 h)")):
    pb.loglog(period, 1 / np.sqrt(1 + (w / k) ** 2), color=charts.line(tok), lw=1.6, label=lab)
tot = 1 / np.sqrt(1 + (w / kgh) ** 2) / np.sqrt(1 + (w * tau_m) ** 2) / np.sqrt(1 + (w / kigf) ** 2)
pb.loglog(period, tot, color=P.ink(), lw=1.2, ls="--", label="whole chain")
for p, lab in ((3, "3-h pulses"), (24, "1 day")):
    pb.axvline(p, color=P.muted(), lw=0.7, ls=":")
    pb.text(p * 1.08, 1.3e-3, lab, fontsize=7.0, color=P.muted(), va="bottom")
leg = pb.legend(loc="upper left", fontsize=7.0, frameon=False)
for txt in leg.get_texts():
    txt.set_color(P.ink())
pb.set_xlim(0.1, 200)
pb.set_ylim(1e-3, 1.5)
charts.style_axes(pb, "period of input oscillation / h", "amplitude gain")
charts.title(pb, "Each stage is a first-order low-pass filter")
