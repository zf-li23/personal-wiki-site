"""A minimal model of the hormonal switch between glycolysis and gluconeogenesis in the liver.

phi = fraction of PFK-2/FBPase-2 phosphorylated by PKA; with first-order kinase (rate kp) and
phosphatase (rate kd), d phi/dt = kp (1 - phi) - kd phi, steady state phi = s / (1 + s), s = kp/kd.
Kinase and bisphosphatase activities of the bifunctional enzyme (uM/min):
  VK = VK0 [(1 - phi) + aK phi],  VB = VB0 [bB (1 - phi) + phi]
  dX/dt = VK [F6P]/(KF + [F6P]) - VB X/(KX + X),   X = [fructose 2,6-bisphosphate] (uM).
Effects on the substrate cycle F6P <-> F1,6BP (relative activities):
  PFK-1 = (f0 + X/Ka)/(1 + X/Ka),  FBPase-1 = 1/(1 + (X/Ki)^n); net flux J = PFK-1 - FBPase-1.
Illustrative parameters: VK0 = 0.15, VB0 = 1.0 uM/min, aK = 0.1, bB = 0.2, [F6P] = 0.05 mM, KF = 0.03 mM,
KX = 5 uM, Ka = 0.5 uM, f0 = 0.05, Ki = 1 uM, n = 1.5. Time course: kd = 0.5 /min; glucagon raises
kp from 0.05 to 5 /min at t = 10 min, insulin and refeeding bring it back at t = 60 min.
"""

import numpy as np
from scipy.integrate import solve_ivp
import wikibio as bio
from wikibio import charts

P = bio.P
VK0, VB0, AK, BB = 0.15, 1.0, 0.1, 0.2
F6P, KF, KX = 0.05, 0.03, 5.0
KA, F0, KI, NI = 0.5, 0.05, 1.0, 1.5


def vk(phi):
    return VK0 * ((1 - phi) + AK * phi) * F6P / (KF + F6P)


def vb_max(phi):
    return VB0 * (BB * (1 - phi) + phi)


def x_ss(phi):
    # VK = VB X/(KX + X)  ->  X = KX VK / (VB - VK)
    k, b = vk(phi), vb_max(phi)
    return KX * k / (b - k)


def pfk1(x):
    return (F0 + x / KA) / (1 + x / KA)


def fbp1(x):
    return 1 / (1 + (x / KI) ** NI)


fig, ax = bio.canvas(24.0, 9.6)

# --- A: steady state against the kinase/phosphatase ratio ----------------------------------------
s = np.logspace(-2, 2, 400)
phi = s / (1 + s)
X = x_ss(phi)
a = charts.axes_at(ax, (1.9, 1.4, 5.8, 6.6))
a.semilogx(s, X, color=charts.line("highlight"), lw=2.0)
a.set_yscale("log")
a.set_ylim(0.03, 10)
a.set_xlim(1e-2, 1e2)
charts.style_axes(a, "PKA / phosphatase activity ratio", r"[F2,6BP] / µM")
a.text(0.012, 5.2, "insulin, fed", fontsize=bio.core.FONT["tiny"], color=P.muted())
a.text(90, 0.035, "glucagon, fasted", fontsize=bio.core.FONT["tiny"], color=P.muted(), ha="right")
bio.panel(ax, "A", (0.4, 9.2))

# --- B: activities of PFK-1 and FBPase-1 and the net flux ---------------------------------------
b = charts.axes_at(ax, (9.8, 1.4, 5.8, 6.6))
b.semilogx(s, pfk1(X), color=charts.line("positive"), lw=2.0, label="PFK-1")
b.semilogx(s, fbp1(X), color=charts.line("negative"), lw=2.0, label="FBPase-1")
b.semilogx(s, pfk1(X) - fbp1(X), color=P.ink(), lw=2.0, ls="--", label="net flux J")
b.axhline(0, color=P.muted(), lw=0.8)
b.set_xlim(1e-2, 1e2)
b.set_ylim(-1.05, 1.05)
charts.style_axes(b, "PKA / phosphatase activity ratio", "relative activity")
b.legend(frameon=False, fontsize=bio.core.FONT["tiny"], labelcolor=P.ink(), loc="lower left")
b.text(0.012, 0.9, "glycolysis", fontsize=bio.core.FONT["tiny"], color=P.muted())
b.text(90, -0.95, "gluconeogenesis", fontsize=bio.core.FONT["tiny"], color=P.muted(), ha="right")
bio.panel(ax, "B", (8.3, 9.2))

# --- C: time course after glucagon and after refeeding -------------------------------------------
KD = 0.5


def kp(t):
    return 5.0 if 10 <= t < 60 else 0.05


def rhs(t, y):
    ph, x = y
    return [kp(t) * (1 - ph) - KD * ph, vk(ph) - vb_max(ph) * x / (KX + x)]


ph0 = 0.05 / (0.05 + KD)
sol = solve_ivp(rhs, (0, 110), [ph0, x_ss(ph0)], max_step=0.1, dense_output=True)
t = np.linspace(0, 110, 1100)
ph_t, x_t = sol.sol(t)
c = charts.axes_at(ax, (17.6, 1.4, 5.8, 6.6))
c.plot(t, ph_t, color=charts.line("protein"), lw=2.0, label="PFK-2/FBPase-2 phosphorylated")
c.plot(t, x_t / x_t.max(), color=charts.line("highlight"), lw=2.0, label="[F2,6BP] (relative)")
c.plot(t, pfk1(x_t) - fbp1(x_t), color=P.ink(), lw=2.0, ls="--", label="net flux J")
c.axhline(0, color=P.muted(), lw=0.8)
c.axvspan(10, 60, color=P.fill("drug"), alpha=0.18, lw=0)
c.text(35, -0.95, "glucagon", ha="center", fontsize=bio.core.FONT["tiny"], color=P.muted())
c.set_xlim(0, 110)
c.set_ylim(-1.05, 1.15)
charts.style_axes(c, "t / min", "fraction or relative value")
c.legend(frameon=False, fontsize=bio.core.FONT["tiny"], labelcolor=P.ink(), loc="upper right",
         bbox_to_anchor=(1.0, 1.22))
bio.panel(ax, "C", (16.1, 9.2))
