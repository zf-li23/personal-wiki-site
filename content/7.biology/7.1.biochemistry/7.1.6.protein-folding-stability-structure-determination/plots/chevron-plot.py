"""Two-state folding kinetics. A: chevron plot, ln k_obs = ln(k_f + k_u) against denaturant, with
ln k_f = ln k_f(H2O) - m_f [D]/RT and ln k_u = ln k_u(H2O) + m_u [D]/RT (k_f(H2O) = 500 s^-1,
k_u(H2O) = 0.05 s^-1, m_f = 7, m_u = 3 kJ/(mol M), 25 C); points: simulated relaxation rates with
5 % noise (seed 0). B: equilibrium fraction unfolded predicted from the kinetic parameters,
K_U = k_u/k_f, compared with simulated equilibrium data. C: relaxation after a jump to 2 M."""

import numpy as np
import wikibio as bio
from wikibio import charts

P = bio.P
RT = 8.314e-3 * 298.15
kf0, ku0, mf, mu = 500.0, 0.05, 7.0, 3.0


def kf(D):
    return kf0 * np.exp(-mf * D / RT)


def ku(D):
    return ku0 * np.exp(mu * D / RT)


rng = np.random.default_rng(0)
fig, ax = bio.canvas(21.0, 7.6)
D = np.linspace(0, 6, 300)

bio.panel(ax, "A", (0.1, 7.5))
pa = charts.axes_at(ax, (1.4, 1.3, 5.6, 5.4))
pa.plot(D, np.log(kf(D) + ku(D)), color=P.ink(), lw=1.7, label=r"$k_\mathrm{obs} = k_\mathrm{f} + k_\mathrm{u}$")
pa.plot(D, np.log(kf(D)), color=charts.line("positive"), lw=1.0, ls="--", label=r"$k_\mathrm{f}$ (folding arm)")
pa.plot(D, np.log(ku(D)), color=charts.line("negative"), lw=1.0, ls="--", label=r"$k_\mathrm{u}$ (unfolding arm)")
Dp = np.arange(0.25, 6.0, 0.25)
kobs = (kf(Dp) + ku(Dp)) * (1 + rng.normal(0, 0.05, Dp.size))
pa.plot(Dp, np.log(kobs), "o", ms=3.4, mfc=charts.line("protein"), mec="none")
Cm = RT * np.log(kf0 / ku0) / (mf + mu)
pa.axvline(Cm, color=P.muted(), lw=0.6, ls=":")
pa.text(Cm + 0.1, 6.6, rf"$C_\mathrm{{m}}$ = {Cm:.2f} M", fontsize=bio.core.FONT["tiny"], color=P.ink())
pa.set_ylim(-4, 7.5)
pa.legend(frameon=False, fontsize=bio.core.FONT["tiny"], labelcolor=P.ink(), loc="lower left")
charts.style_axes(pa, "[urea] / M", r"$\ln(k / \mathrm{s^{-1}})$")
charts.title(pa, "Chevron plot")

bio.panel(ax, "B", (7.5, 7.5))
pb = charts.axes_at(ax, (8.8, 1.3, 5.0, 5.4))
K = ku(D) / kf(D)
pb.plot(D, K / (1 + K), color=P.ink(), lw=1.6, label="predicted from kinetics")
De = np.arange(0.2, 6.0, 0.3)
Ke = ku(De) / kf(De)
pb.plot(De, Ke / (1 + Ke) + rng.normal(0, 0.02, De.size), "s", ms=3.2, mfc=charts.line("receptor"), mec="none",
        label="equilibrium data")
beta = mf / (mf + mu)
pb.text(3.4, 0.25, rf"$\Delta_\mathrm{{U}}G$(H$_2$O) = {RT * np.log(kf0 / ku0):.1f} kJ/mol" + "\n"
        + rf"$m = m_\mathrm{{f}} + m_\mathrm{{u}}$ = {mf + mu:.0f} kJ/(mol M)" + "\n" + rf"$\beta_\mathrm{{T}} = m_\mathrm{{f}}/m$ = {beta:.1f}",
        fontsize=bio.core.FONT["tiny"], color=P.ink())
pb.legend(frameon=False, fontsize=bio.core.FONT["tiny"], labelcolor=P.ink(), loc="center left")
pb.set_ylim(-0.05, 1.05)
charts.style_axes(pb, "[urea] / M", r"fraction unfolded $f_\mathrm{U}$")
charts.title(pb, "Kinetics predicts equilibrium")

bio.panel(ax, "C", (14.4, 7.5))
pc = charts.axes_at(ax, (15.7, 1.3, 5.0, 5.4))
D1 = 2.0
k1 = kf(D1) + ku(D1)
fe = ku(D1) / k1
t = np.linspace(0, 6 / k1, 300)
for f0, tok, name in ((1.0, "positive", "refolding (from 6 M)"), (0.0, "negative", "unfolding (from 0 M)")):
    pc.plot(t * 1e3, fe + (f0 - fe) * np.exp(-k1 * t), color=charts.line(tok), lw=1.6, label=name)
pc.axhline(fe, color=P.muted(), lw=0.6, ls=":")
pc.text(t[-1] * 1e3 * 0.45, fe + 0.04, rf"$\tau = 1/(k_\mathrm{{f}} + k_\mathrm{{u}})$ = {1e3 / k1:.0f} ms",
        fontsize=bio.core.FONT["tiny"], color=P.ink())
pc.legend(frameon=False, fontsize=bio.core.FONT["tiny"], labelcolor=P.ink(), loc="upper right")
pc.set_ylim(-0.05, 1.05)
charts.style_axes(pc, "t / ms", r"fraction unfolded $f_\mathrm{U}$")
charts.title(pc, "Relaxation at 2 M urea")
