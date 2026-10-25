"""Heterotropic effects on oxygen binding by hemoglobin, in the MWC model of the previous figure
(K_R = 0.35 kPa, c = 0.01); an effector that stabilizes T is represented by a larger L, chosen to
give the stated p50. Numbers on the panels are computed from these curves.
A: Bohr effect, p50 = 3.5 x 10^(-0.48 (pH - 7.4)) kPa; illustrative pH 7.6 in the lungs and 7.2 in
active tissue. B: 2,3-bisphosphoglycerate: p50 = 1.4 (no BPG), 3.5 (5 mM) and 4.3 kPa (8 mM, after
acclimatization); high altitude modelled by a lung p_O2 of 7.5 kPa. C: carbon monoxide: 50 % of all
subunits carry CO (binomially distributed over tetramers; a CO-bound subunit counts as liganded),
compared with an anaemia in which half of the hemoglobin is missing."""

import numpy as np
from scipy.optimize import brentq
from scipy.stats import binom
import wikibio as bio
from wikibio import charts

P = bio.P
KR, c = 0.35, 0.01


def theta(p, L):
    a = p / KR
    return (a * (1 + a) ** 3 + L * c * a * (1 + c * a) ** 3) / ((1 + a) ** 4 + L * (1 + c * a) ** 4)


def L_for(p50):
    return np.exp(brentq(lambda x: theta(p50, np.exp(x)) - 0.5, -5, 40))


def bars(axb, labels, vals, toks):
    axb.barh(range(len(vals)), vals, color=[P.fill(t) for t in toks], edgecolor=[charts.line(t) for t in toks], lw=0.8)
    for i, v in enumerate(vals):
        axb.text(v + 0.01, i, f"{v * 100:.0f}%", va="center", fontsize=bio.core.FONT["tiny"], color=P.ink())
    axb.set_yticks(range(len(vals)))
    axb.set_yticklabels(labels)
    axb.invert_yaxis()
    axb.set_xlim(0, 0.75)
    axb.set_xticks([0, 0.3, 0.6])
    charts.style_axes(axb, "O₂ released", None)


p = np.linspace(0, 16, 400)
fig, ax = bio.canvas(23.0, 8.6)

# A: Bohr effect
bio.panel(ax, "A", (0.1, 8.5))
pa = charts.axes_at(ax, (1.3, 3.3, 5.6, 4.4))
Lp = {}
for pH, tok in ((7.6, "enzyme"), (7.4, "blood"), (7.2, "drug")):
    Lp[pH] = L_for(3.5 * 10 ** (-0.48 * (pH - 7.4)))
    pa.plot(p, theta(p, Lp[pH]), color=charts.line(tok), lw=1.7, label=f"pH {pH}")
for pv in (4.0, 13.3):
    pa.axvline(pv, color=P.muted(), lw=0.6, ls=":")
pa.legend(frameon=False, fontsize=bio.core.FONT["tiny"], labelcolor=P.ink(), loc="lower right")
pa.set_ylim(0, 1.03)
charts.style_axes(pa, r"$p_{\mathrm{O_2}}$ / kPa", r"$\theta$")
charts.title(pa, "Bohr effect")
ba = charts.axes_at(ax, (3.0, 0.7, 3.4, 1.4))
bars(ba, ["pH 7.4 both", "7.6 → 7.2"],
     [theta(13.3, Lp[7.4]) - theta(4.0, Lp[7.4]), theta(13.3, Lp[7.6]) - theta(4.0, Lp[7.2])], ["blood", "drug"])

# B: BPG and altitude
bio.panel(ax, "B", (7.7, 8.5))
pb = charts.axes_at(ax, (8.9, 3.3, 5.6, 4.4))
Lb = {}
for name, p50, tok in (("no BPG", 1.4, "neutral"), ("5 mM BPG", 3.5, "blood"), ("8 mM BPG", 4.3, "protein")):
    Lb[name] = L_for(p50)
    pb.plot(p, theta(p, Lb[name]), color=charts.line(tok), lw=1.7, label=f"{name} (p50 = {p50} kPa)")
for pv, txt in ((4.0, "tissues"), (7.5, "lungs, 4500 m"), (13.3, "lungs, sea level")):
    pb.axvline(pv, color=P.muted(), lw=0.6, ls=":")
    pb.text(pv + 0.25, 0.62, txt, fontsize=bio.core.FONT["tiny"], color=P.ink(), rotation=90, va="center")
pb.legend(frameon=False, fontsize=bio.core.FONT["tiny"], labelcolor=P.ink(), loc="lower right")
pb.set_ylim(0, 1.03)
charts.style_axes(pb, r"$p_{\mathrm{O_2}}$ / kPa", r"$\theta$")
charts.title(pb, "2,3-Bisphosphoglycerate")
bb = charts.axes_at(ax, (11.0, 0.55, 3.0, 1.65))
L5, L8 = Lb["5 mM BPG"], Lb["8 mM BPG"]
bars(bb, ["sea level", "4500 m", "4500 m, 8 mM"],
     [theta(13.3, L5) - theta(4, L5), theta(7.5, L5) - theta(4, L5), theta(7.5, L8) - theta(4, L8)],
     ["blood", "negative", "protein"])

# C: CO versus anaemia
bio.panel(ax, "C", (15.3, 8.5))
pc = charts.axes_at(ax, (16.5, 3.3, 5.8, 4.4))
L0 = Lb["5 mM BPG"]


def o2_with_co(pp, frac=0.5):
    """O2 bound per subunit of total hemoglobin when a fraction of subunits carries CO."""
    a = pp / KR
    total = 0.0
    for k in range(5):
        free = 4 - k
        Z = (1 + a) ** free + L0 * c ** k * (1 + c * a) ** free
        dZ = free * (1 + a) ** (free - 1) + L0 * c ** k * free * c * (1 + c * a) ** (free - 1) if free else 0 * a
        total = total + binom.pmf(k, 4, frac) * a * dZ / Z / 4
    return total


curves = [("normal", lambda q: theta(q, L0), "blood"), ("anaemia, 50% Hb", lambda q: 0.5 * theta(q, L0), "neutral"),
          ("50% subunits as COHb", o2_with_co, "negative")]
for name, f, tok in curves:
    pc.plot(p, f(p), color=charts.line(tok), lw=1.7, label=name)
for pv in (4.0, 13.3):
    pc.axvline(pv, color=P.muted(), lw=0.6, ls=":")
pc.legend(frameon=False, fontsize=bio.core.FONT["tiny"], labelcolor=P.ink(), loc="lower right")
pc.set_ylim(0, 1.03)
charts.style_axes(pc, r"$p_{\mathrm{O_2}}$ / kPa", "O₂ per subunit of total Hb")
charts.title(pc, "Carbon monoxide")
bc = charts.axes_at(ax, (18.6, 0.55, 3.2, 1.65))
bars(bc, ["normal", "anaemia", "COHb 50%"], [f(13.3) - f(4.0) for _, f, _ in curves], [t for _, _, t in curves])
