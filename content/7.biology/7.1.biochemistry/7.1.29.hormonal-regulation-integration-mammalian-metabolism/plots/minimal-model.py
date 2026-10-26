"""Bergman's minimal model of glucose disappearance during an intravenous glucose tolerance test (IVGTT).
dG/dt = -(S_G + X) G + S_G G_b and dX/dt = -p2 X + p2 S_I (I - I_b), with G plasma glucose, X the insulin action
in a remote (interstitial) compartment, S_G glucose effectiveness (0.025/min), p2 its rate constant
(0.025/min), S_I insulin sensitivity, basal G_b = 5 mM and I_b = 60 pmol/L. Insulin: a first-phase bolus
Phi1 at t = 0, then dI/dt = -n (I - I_b) + gamma max(G - G_b, 0), clearance n = 0.15/min. Glucose bolus raises
G to 16 mM at t = 0. Three illustrative subjects:
normal (S_I = 1.0e-4 per min per pmol/L, Phi1 = 500 pmol/L, gamma = 4.5 pmol/L/min per mM);
insulin resistant but compensated by beta cells (S_I four times lower, secretion four times higher);
insulin resistant with beta-cell failure (S_I four times lower, secretion halved: type 2 diabetes).
(A) Plasma glucose; (B) plasma insulin; (C) the hyperbolic relation between insulin sensitivity and the
first-phase insulin response: subjects on the same hyperbola (constant disposition index S_I x Phi1)
tolerate glucose about equally well; falling below it marks beta-cell failure."""

import numpy as np
from scipy.integrate import solve_ivp

import wikibio as bio
from wikibio import charts

SG, P2, GB, IB, N = 0.025, 0.025, 5.0, 60.0, 0.15


def run(si, phi1, gamma, t):
    def f(_, y):
        g, x, i = y
        return [-(SG + x) * g + SG * GB, -P2 * x + P2 * si * (i - IB), -N * (i - IB) + gamma * max(g - GB, 0.0)]
    return solve_ivp(f, (t[0], t[-1]), [16.0, 0.0, IB + phi1], t_eval=t, rtol=1e-8, method="LSODA").y


t = np.linspace(0, 180, 721)
subjects = [("normal", 1.0e-4, 500.0, 4.5, "positive"),
            ("resistant, compensated", 0.25e-4, 2000.0, 18.0, "highlight"),
            ("resistant, β-cell failure", 0.25e-4, 250.0, 2.25, "negative")]
fig, ax = bio.canvas(21.0, 7.6)
a = charts.axes_at(ax, (1.5, 1.3, 5.4, 5.6))
b = charts.axes_at(ax, (8.5, 1.3, 5.4, 5.6))
c = charts.axes_at(ax, (15.5, 1.3, 5.2, 5.6))
for name, si, phi, gam, tok in subjects:
    g, x, i = run(si, phi, gam, t)
    sel = (t >= 10) & (t <= 40)
    kg = -np.polyfit(t[sel], np.log(g[sel] - 0 * GB), 1)[0] * 100
    a.plot(t, g, color=charts.line(tok), lw=2.0, label=f"{name}: $K_\\mathrm{{G}}$ = {kg:.1f} %/min")
    b.plot(t, i, color=charts.line(tok), lw=2.0)
    c.plot([si * 1e4], [phi], "o", ms=8, color=charts.line(tok))
a.axhline(GB, color=bio.P.muted(), lw=0.8, ls="--")
a.set_xlim(0, 180)
a.set_ylim(0, 17)
a.legend(frameon=False, fontsize=bio.core.FONT["tiny"], labelcolor=bio.P.ink(), loc="upper right")
charts.style_axes(a, "t / min", "plasma glucose / mM")
charts.title(a, "A  Glucose after an i.v. bolus")
b.set_xlim(0, 180)
b.set_yscale("log")
b.set_ylim(30, 3000)
charts.style_axes(b, "t / min", "plasma insulin / (pmol L⁻¹)")
charts.title(b, "B  Insulin")
s = np.linspace(0.12, 1.6, 200)
c.plot(s, 500.0 * 1.0 / s, color=bio.P.muted(), lw=1.2, ls="--")
c.text(1.0, 620, "$S_\\mathrm{I}\\,\\Phi_1$ = const", fontsize=bio.core.FONT["tiny"], color=bio.P.muted())
c.set_xlim(0, 1.6)
c.set_ylim(0, 2600)
charts.style_axes(c, "$S_\\mathrm{I}$ / (10⁻⁴ min⁻¹ per pmol L⁻¹)", "first-phase insulin $\\Phi_1$ / (pmol L⁻¹)")
charts.title(c, "C  Disposition index")
