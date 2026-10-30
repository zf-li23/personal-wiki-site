"""The three-stage model of a whole gene: promoter switching, mRNA and protein (Formula 22.5.3).

Reactions per cell: promoter copies switch ON at k_on (g - n) and OFF at k_off n; each ON copy makes
functional mRNA at r Psi; mRNA decays at gamma_m; each mRNA is translated at k_p; protein is removed at
gamma_p. Parameters (E. coli-like, minutes): g = 2; p_on = 0.094 from simple repression by 10 LacI on
O1 (Example 11.6.1); k_off = 0.5; r Psi = 5.4; mRNA half-life 3 min; k_p = 2; removal by dilution only
(doubling time 30 min).
A: protein after induction in 12 cells (light), the mean of 150 cells (dark) and the ODE for the means
(dashed); the dotted line is the steady state given by the product of the factors.
B: protein numbers at 240 min in the 150 cells, with the gamma distribution whose mean and variance
are the predictions (product formula; Lyapunov equation, exact for this linear network).
C: the total protein noise and its three terms (Formula 22.5.3) against the promoter switching rate
lambda = k_on + k_off at fixed p_on, on logarithmic axes: the promoter term dominates when switching is
slow and vanishes when it is fast, where the two-stage result, Eq. (22.10), is recovered."""

import numpy as np
from scipy.integrate import solve_ivp
from scipy.stats import gamma as gamma_dist
import wikibio as bio
from wikibio import charts

P = bio.P
FONT = bio.core.FONT
rng = np.random.default_rng(0)

g, f = 2, 0.094
k_off = 0.5
k_on = k_off * f / (1 - f)
rPsi, gm, kp, gp = 5.4, np.log(2) / 3, 2.0, np.log(2) / 30
n_bar = g * f
m_bar = rPsi * n_bar / gm
p_bar = kp * m_bar / gp


def terms(lam):
    """The protein, mRNA and promoter terms of eta_p^2 at switching rate lam = k_on + k_off."""
    t_p = 1 / p_bar
    t_m = gp / (m_bar * (gm + gp))
    t_n = (1 - f) / n_bar * gm * gp * (lam + gm + gp) / ((gm + gp) * (lam + gm) * (lam + gp))
    return t_p, t_m, t_n


def gillespie(t_rec):
    t, n, m, p, i = 0.0, 0, 0, 0, 0
    out = np.zeros(len(t_rec))
    while i < len(t_rec):
        a = np.array([k_on * (g - n), k_off * n, rPsi * n, gm * m, kp * m, gp * p])
        a0 = a.sum()
        dt = rng.exponential(1 / a0)
        while i < len(t_rec) and t_rec[i] < t + dt:
            out[i] = p
            i += 1
        t += dt
        j = rng.choice(6, p=a / a0)
        n += (j == 0) - (j == 1)
        m += (j == 2) - (j == 3)
        p += (j == 4) - (j == 5)
    return out


t = np.linspace(0, 240, 241)
cells = np.array([gillespie(t) for _ in range(150)])
ode = solve_ivp(lambda _, x: [k_on * (g - x[0]) - k_off * x[0], rPsi * x[0] - gm * x[1], kp * x[1] - gp * x[2]],
                (0, 240), [0, 0, 0], t_eval=t).y[2]
eta2 = sum(terms(k_on + k_off))

fig, ax = bio.canvas(24.0, 8.4)
tiny = FONT["tiny"]

bio.panel(ax, "A", (0.1, 8.3))
a = charts.axes_at(ax, (1.5, 1.0, 6.3, 6.4))
for c in cells[:12]:
    a.plot(t, c, color=P.light("protein"), lw=0.9)
a.plot(t, cells.mean(0), color=charts.line("protein"), lw=2.0, label="mean of 150 cells")
a.plot(t, ode, color=P.ink(), lw=1.2, ls="--", label="ODE for the means")
a.axhline(p_bar, color=charts.line("negative"), lw=1.0, ls=":")
a.text(5, p_bar * 1.04, f"product formula {p_bar:.0f}", fontsize=tiny, color=charts.line("negative"))
a.set_xlim(0, 240)
a.set_ylim(0, None)
a.legend(frameon=False, fontsize=tiny, labelcolor=P.ink(), loc="upper left")
charts.style_axes(a, "time after induction / min", "protein molecules per cell")
charts.title(a, "Dynamics")

bio.panel(ax, "B", (8.9, 8.3))
b = charts.axes_at(ax, (10.3, 1.0, 5.8, 6.4))
s = cells[:, -1]
b.hist(s, bins=25, density=True, color=P.light("protein"), edgecolor=P.edge("protein"), lw=0.5, label="simulation")
var = eta2 * p_bar**2
x = np.linspace(1, s.max() * 1.05, 300)
b.plot(x, gamma_dist.pdf(x, p_bar**2 / var, scale=var / p_bar), color=charts.line("negative"), lw=1.8,
       label="predicted mean and variance")
b.legend(frameon=False, fontsize=tiny, labelcolor=P.ink(), loc="upper right")
b.text(0.97, 0.70, f"$\\eta^2$: predicted {eta2:.2f}\nsimulated {s.var() / s.mean()**2:.2f}",
       transform=b.transAxes, ha="right", fontsize=tiny, color=P.ink())
charts.style_axes(b, "protein molecules at 240 min", "probability density")
charts.title(b, "Distribution")

bio.panel(ax, "C", (17.2, 8.3))
c = charts.axes_at(ax, (18.6, 1.0, 5.3, 6.4))
lam = np.logspace(-2, 2, 300)
tp, tm, tn = (np.array(v) for v in zip(*[terms(l) for l in lam]))
c.loglog(lam, tp + tm + tn, color=P.ink(), lw=2.0, label="total")
c.loglog(lam, tn, color=charts.line("chromatin"), lw=1.6, ls="--", label="promoter")
c.loglog(lam, tm, color=charts.line("rna"), lw=1.6, ls="--", label="mRNA")
c.loglog(lam, tp, color=charts.line("enzyme"), lw=1.6, ls=":", label="protein")
c.axvline(k_on + k_off, color=P.muted(), lw=0.8, ls=":")
c.text((k_on + k_off) * 1.15, 1.5e-3, "panels A, B", fontsize=tiny, color=P.ink())
c.set_xlim(1e-2, 1e2)
c.set_ylim(1e-3, 3)
c.legend(frameon=False, fontsize=tiny, labelcolor=P.ink(), loc="upper right")
charts.style_axes(c, r"switching rate $k_{\mathrm{on}} + k_{\mathrm{off}}$ / min$^{-1}$", r"protein noise $\eta^2$")
charts.title(c, "Where the noise comes from")
