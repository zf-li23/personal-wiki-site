"""Epiboly as the spreading of a thin viscous film (Greenspan's model, as used by Percus and Childress). A
ribbon of cells of fixed cross-section spreads on a substrate it wets; in the quasi-steady approximation the
profile is a parabola h = (1/2a)(1 − x²/a²) and the edge obeys ȧ = K_e (1/a² − θ0), where 1/a² is the contact
angle at the edge and θ0 the equilibrium contact angle (K_e = 1, a(0) = 0.5). A: profiles at successive
times for complete wetting (θ0 = 0). B: the half-width a(t): for θ0 = 0 it is exactly (a0³ + 3K_e t)^(1/3) (dotted), so the edge
slows as t^(−2/3); for θ0 > 0 it approaches θ0^(−1/2). C: the lubrication solution h = h0/(1 − t h0 ∇²T/2η)
for a layer driven by a tension trough in the substrate (T = −exp(−x²), h0 = 0.2, η = 1; blow-up at t = 5): cells accumulate
where ∇²T > 0, and the thin-film approximation fails as the denominator approaches zero."""
import numpy as np
from scipy.integrate import solve_ivp
import wikibio as bio
from wikibio import charts

P = bio.P
fig, ax = bio.canvas(22, 7.4)
Ke = 1.0
sol = {}
for th0 in (0.0, 0.5, 1.5):
    s = solve_ivp(lambda t, a: Ke * (1 / a**2 - th0), (0, 6), [0.5], dense_output=True, rtol=1e-8)
    sol[th0] = s
a = charts.axes_at(ax, (1.6, 1.4, 5.8, 4.8))
x = np.linspace(-2.2, 2.2, 400)
for t, tk in ((0, "neutral"), (0.2, "dna"), (1.0, "positive"), (5.0, "receptor")):
    aa = sol[0.0].sol(t)[0]
    h = np.where(abs(x) < aa, (1 / (2 * aa)) * (1 - (x / aa) ** 2), 0)
    a.plot(x, h, color=charts.line(tk), lw=1.6, label=f"t = {t:g}")
a.set_ylim(0, 1.05)
charts.style_axes(a, "position x", "thickness h")
charts.title(a, "A  Spreading ribbon (θ0 = 0)")
lg = a.legend(fontsize=6.5, frameon=False)
[x_.set_color(P.ink()) for x_ in lg.get_texts()]

b = charts.axes_at(ax, (9.0, 1.4, 5.8, 4.8))
tt = np.linspace(0, 6, 300)
for th0, tk in ((0.0, "receptor"), (0.5, "dna"), (1.5, "positive")):
    b.plot(tt, sol[th0].sol(tt)[0], color=charts.line(tk), lw=1.7, label=f"θ0 = {th0:g}")
    if th0 > 0:
        b.axhline(th0**-0.5, color=charts.line(tk), lw=0.7, ls=(0, (3, 2)))
b.plot(tt, (0.5**3 + 3 * Ke * tt) ** (1 / 3), color=P.muted(), lw=0.8, ls=(0, (1, 1.5)))
charts.style_axes(b, "time t", "half-width a")
charts.title(b, "B  Edge law")
lg = b.legend(fontsize=6.5, frameon=False, loc="lower right")
[x_.set_color(P.ink()) for x_ in lg.get_texts()]

c = charts.axes_at(ax, (16.4, 1.4, 5.0, 4.8))
xx = np.linspace(-3, 3, 400)
T = -np.exp(-xx**2)                        # tension trough
lapT = (2 - 4 * xx**2) * np.exp(-xx**2)    # its second derivative
h0 = 0.2
for t, tk in ((0, "neutral"), (2, "dna"), (3.5, "positive"), (4.5, "receptor")):
    c.plot(xx, h0 / (1 - t * h0 * lapT / 2), color=charts.line(tk), lw=1.6, label=f"t = {t:g}")
c.plot(xx, 0.25 * T + 0.25, color=P.muted(), lw=0.8, ls=(0, (3, 2)))
c.text(1.3, 0.2, "T(x)", fontsize=6.5, color=P.muted())
c.set_ylim(0, 2.2)
charts.style_axes(c, "position x", "thickness h")
charts.title(c, "C  Accretion in a tension trough")
lg = c.legend(fontsize=6.5, frameon=False, loc="upper right")
[x_.set_color(P.ink()) for x_ in lg.get_texts()]
