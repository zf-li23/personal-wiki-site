"""Oxygen binding by myoglobin and hemoglobin.
Mb: hyperbola with p50 = 0.26 kPa. Hb: MWC model with K_R = 0.35 kPa, c = K_R/K_T = 0.01, L = 1e4
(illustrative values giving p50 = 3.5 kPa and n_H = 3.0). Reference hyperbolas: the same p50 as Hb,
and the best possible non-cooperative carrier, p50 = sqrt(p_lung p_tissue).
A: saturation curves and the fraction of capacity released between lungs (13.3 kPa) and tissues (4 kPa).
B: Hill plot, log[theta/(1 - theta)] against log p_O2; the slope at half-saturation is n_H."""

import numpy as np
import wikibio as bio
from wikibio import charts

P = bio.P
KR, c, L = 0.35, 0.01, 1.0e4
p_lung, p_tis = 13.3, 4.0


def mwc(p):
    a = p / KR
    return (a * (1 + a) ** 3 + L * c * a * (1 + c * a) ** 3) / ((1 + a) ** 4 + L * (1 + c * a) ** 4)


def hyp(p, p50):
    return p / (p + p50)


p_opt = np.sqrt(p_lung * p_tis)
curves = [("Myoglobin (p50 = 0.26 kPa)", lambda p: hyp(p, 0.26), "enzyme", "-"),
          ("Hemoglobin (MWC)", mwc, "blood", "-"),
          ("hyperbola, p50 = 3.5 kPa", lambda p: hyp(p, 3.5), "neutral", "--"),
          (f"best hyperbola, p50 = {p_opt:.1f} kPa", lambda p: hyp(p, p_opt), "protein", ":")]

fig, ax = bio.canvas(20.0, 8.0)
bio.panel(ax, "A", (0.1, 7.9))
pa = charts.axes_at(ax, (1.4, 1.3, 7.6, 5.9))
p = np.linspace(0, 16, 500)
for name, f, tok, ls in curves:
    pa.plot(p, f(p), color=charts.line(tok), lw=1.8 if ls == "-" else 1.3, ls=ls, label=name)
for pv, txt in ((p_tis, "tissues"), (p_lung, "lungs")):
    pa.axvline(pv, color=P.muted(), lw=0.6, ls=":")
    pa.text(pv, 1.04, txt, fontsize=bio.core.FONT["tiny"], color=P.ink(), ha="center")
pa.legend(frameon=False, fontsize=bio.core.FONT["tiny"], labelcolor=P.ink(), loc="lower right")
pa.set_xlim(0, 16)
pa.set_ylim(0, 1.08)
charts.style_axes(pa, r"$p_{\mathrm{O_2}}$ / kPa", r"fractional saturation $\theta$")
charts.title(pa, "Binding curves")
# released fraction
ins = charts.axes_at(ax, (9.9, 1.6, 2.2, 5.3))
vals = [f(p_lung) - f(p_tis) for _, f, _, _ in curves]
ins.barh(range(4), vals, color=[P.fill(t) for _, _, t, _ in curves], edgecolor=[charts.line(t) for _, _, t, _ in curves],
         lw=0.8)
for i, v in enumerate(vals):
    ins.text(v + 0.01, i, f"{v * 100:.0f}%", va="center", fontsize=bio.core.FONT["tiny"], color=P.ink())
ins.set_yticks(range(4))
ins.set_yticklabels(["Mb", "Hb", "hyp. 3.5", f"hyp. {p_opt:.1f}"])
ins.invert_yaxis()
ins.set_xlim(0, 0.5)
ins.set_xticks([0, 0.2, 0.4])
charts.style_axes(ins, "released fraction", None)

bio.panel(ax, "B", (13.0, 7.9))
pb = charts.axes_at(ax, (14.4, 1.3, 5.2, 5.9))
lp = np.linspace(-2, 2, 400)
pp = 10 ** lp
for name, f, tok in (("Mb", lambda q: hyp(q, 0.26), "enzyme"), ("Hb", mwc, "blood")):
    th = f(pp)
    pb.plot(lp, np.log10(th / (1 - th)), color=charts.line(tok), lw=1.8, label=name)
# slope-1 asymptotes of Hb: pure T and pure R binding
for K, txt in ((KR / c, "T state"), (KR, "R state")):
    pb.plot(lp, lp - np.log10(K), color=P.muted(), lw=0.7, ls="--")
pb.text(1.25, -1.15, "T state\n(slope 1)", fontsize=bio.core.FONT["tiny"], color=P.ink())
pb.text(-1.2, 1.05, "R state\n(slope 1)", fontsize=bio.core.FONT["tiny"], color=P.ink())
th = mwc(np.array([3.5 * 0.999, 3.5 * 1.001]))
nH = np.diff(np.log10(th / (1 - th)))[0] / np.diff(np.log10([3.5 * 0.999, 3.5 * 1.001]))[0]
pb.text(-0.25, -2.75, f"Hb: $n_\\mathrm{{H}}$ = {nH:.1f} at θ = 0.5\nMb: $n_\\mathrm{{H}}$ = 1", fontsize=bio.core.FONT["tiny"], color=P.ink())
pb.axhline(0, color=P.muted(), lw=0.5)
pb.set_ylim(-3, 3)
pb.set_xlim(-2, 2)
pb.legend(frameon=False, fontsize=bio.core.FONT["tiny"], labelcolor=P.ink(), loc="upper left")
charts.style_axes(pb, r"$\lg(p_{\mathrm{O_2}}/\mathrm{kPa})$", r"$\lg[\theta/(1-\theta)]$")
charts.title(pb, "Hill plot")
