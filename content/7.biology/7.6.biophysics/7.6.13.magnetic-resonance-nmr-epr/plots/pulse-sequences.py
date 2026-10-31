# Pulse sequences drawn schematically (not to scale). Narrow bars: 90 degree pulses; wide bars: 180 degree
# pulses; grey band: broadband decoupling.
# A: inversion recovery (T1) and the CPMG train (T2 and relaxation dispersion): 90x - (tau - 180y - tau)_n.
# B: 1H-15N HSQC: INEPT transfer 1H -> 15N (delays 1/(4J) on each side of simultaneous 180 degree pulses),
#    15N evolution during t1 (a 1H 180 degree pulse in its middle removes the J coupling), reverse INEPT back to
#    1H and acquisition during t2 with 15N decoupling. Product-operator states at points 1-4 are written above.
# C: four-pulse DEER: observer pulses pi/2 - tau1 - pi - (tau1 + tau2) - pi - tau2 - echo at the observer
#    frequency; a pump pi pulse at a second frequency, moved through the interval by the time t, flips the
#    partner spins and modulates the refocused echo.
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

import wikibio as bio
from wikibio import charts

P = bio.P
ink, muted = P.ink(), P.muted()
fig, axs = plt.subplots(3, 1, figsize=(11.0, 8.4), gridspec_kw=dict(height_ratios=[1.0, 1.25, 1.1]))
for ax in axs:
    ax.set_xlim(0, 20)
    ax.axis("off")


def channel(ax, y, x0, x1, name):
    ax.plot([x0, x1], [y, y], color=muted, lw=0.9)
    ax.text(x0 - 0.2, y + 0.15, name, ha="right", va="center", fontsize=9, color=ink)


def pulse(ax, x, y, kind, tok="protein", h=None, label=None):
    w, hh = (0.18, 0.9) if kind == 90 else (0.4, 0.9)
    if h:
        hh = h
    ax.add_patch(Rectangle((x - w / 2, y), w, hh, facecolor=P.fill(tok), edgecolor=P.edge(tok), lw=1.0))
    if label:
        ax.text(x, y + hh + 0.12, label, ha="center", fontsize=7.5, color=ink)


def fid(ax, x0, y, length=3.0, amp=0.6, n=10):
    import numpy as np
    t = np.linspace(0, 1, 300)
    ax.plot(x0 + length * t, y + 0.05 + amp * np.exp(-3 * t) * np.cos(2 * np.pi * n * t), color=charts.line("rna"),
            lw=0.9)


def delay(ax, a, b, y, text):
    ax.annotate("", xy=(a, y), xytext=(b, y), arrowprops=dict(arrowstyle="<->", color=muted, lw=0.7))
    ax.text((a + b) / 2, y - 0.32, text, ha="center", fontsize=7.5, color=ink)


# A: inversion recovery and CPMG
ax = axs[0]
ax.set_ylim(-0.9, 1.9)
channel(ax, 0, 1.0, 8.6, "¹H")
pulse(ax, 1.6, 0, 180, label="180°")
pulse(ax, 4.6, 0, 90, label="90°")
delay(ax, 1.8, 4.5, -0.25, "τ  (vary)")
fid(ax, 4.75, 0, 3.5)
ax.text(4.8, 1.55, r"inversion recovery: $M_z(\tau) = M_0\,(1 - 2\,\mathrm{e}^{-\tau/T_1})$", ha="center", fontsize=8, color=ink)
channel(ax, 0, 11.0, 19.8, "")
pulse(ax, 11.4, 0, 90, label="90°ₓ")
xs = [12.4 + 1.25 * k for k in range(5)]
for k, x in enumerate(xs):
    pulse(ax, x, 0, 180, tok="enzyme", label="180°ᵧ")
delay(ax, 11.5, 12.2, -0.25, "τ")
delay(ax, 12.6, 13.45, -0.25, "2τ")
fid(ax, 18.3, 0, 1.4, n=5)
ax.text(15.3, 1.55, r"CPMG train: echo after each $2\tau$;  $\nu_{\mathrm{CPMG}} = 1/(4\tau)$", ha="center", fontsize=8, color=ink)
charts.title(ax, "A   Measuring T₁ and T₂")

# B: HSQC
ax = axs[1]
ax.set_ylim(-1.7, 2.6)
yH, yN = 1.0, -0.7
channel(ax, yH, 1.0, 19.5, "¹H")
channel(ax, yN, 1.0, 19.5, "¹⁵N")
pulse(ax, 1.6, yH, 90, label="90°ₓ")
pulse(ax, 3.2, yH, 180)
pulse(ax, 3.2, yN, 180, tok="enzyme")
pulse(ax, 4.8, yH, 90, label="90°ᵧ")
pulse(ax, 4.8, yN, 90, tok="enzyme")
delay(ax, 1.7, 3.0, yH - 0.25, "1/(4J)")
delay(ax, 3.4, 4.7, yH - 0.25, "1/(4J)")
pulse(ax, 7.0, yH, 180)
delay(ax, 4.9, 6.8, yN - 0.25, "t₁/2")
delay(ax, 7.2, 9.1, yN - 0.25, "t₁/2")
pulse(ax, 9.2, yH, 90)
pulse(ax, 9.2, yN, 90, tok="enzyme")
pulse(ax, 10.8, yH, 180)
pulse(ax, 10.8, yN, 180, tok="enzyme")
delay(ax, 9.3, 10.6, yH - 0.25, "1/(4J)")
delay(ax, 11.0, 12.3, yH - 0.25, "1/(4J)")
fid(ax, 12.5, yH, 5.0, n=14)
ax.add_patch(Rectangle((12.5, yN), 5.0, 0.35, facecolor=P.fill("neutral"), edgecolor=P.edge("neutral"), lw=0.6))
ax.text(15.0, yN + 0.5, "decouple ¹⁵N", ha="center", fontsize=7.5, color=ink)
ax.text(15.0, yH - 0.35, "acquire t₂", ha="center", fontsize=7.5, color=ink)
for x, k, op in ((1.75, "1", r"$-H_y$"), (5.0, "2", r"$2H_zN_y$"), (9.05, "3", r"$2H_zN_y\cos(\Omega_N t_1)$"),
                 (12.45, "4", r"$H_x\cos(\Omega_N t_1)$")):
    ax.text(x, 2.35, f"({k})  {op}", ha="center", fontsize=7.5, color=ink)
    ax.plot([x, x], [-1.3, 2.15], color=muted, lw=0.5, ls=":")
ax.text(3.2, -1.55, "INEPT: H → N", ha="center", fontsize=7.5, color=ink)
ax.text(7.0, -1.55, "¹⁵N chemical shift", ha="center", fontsize=7.5, color=ink)
ax.text(10.8, -1.55, "reverse INEPT: N → H", ha="center", fontsize=7.5, color=ink)
charts.title(ax, "B   ¹H–¹⁵N HSQC")

# C: DEER
ax = axs[2]
ax.set_ylim(-1.6, 2.1)
yo, yp = 0.8, -0.6
channel(ax, yo, 1.0, 19.5, r"$\nu_{\mathrm{obs}}$")
channel(ax, yp, 1.0, 19.5, r"$\nu_{\mathrm{pump}}$")
xo = [2.0, 4.5, 14.0]
pulse(ax, xo[0], yo, 90, tok="rna", label="π/2")
pulse(ax, xo[1], yo, 180, tok="rna", label="π")
pulse(ax, xo[2], yo, 180, tok="rna", label="π")
delay(ax, 2.1, 4.3, yo - 0.25, "τ₁")
delay(ax, 4.7, 13.8, yo - 0.25, "τ₁ + τ₂")
delay(ax, 14.2, 18.6, yo - 0.25, "τ₂")
# Hahn echo at 2 tau1 and refocused echo
import numpy as np
for xc, amp, name in ((7.0, 0.35, "Hahn echo"), (18.8, 0.6, "refocused echo")):
    u = np.linspace(-0.6, 0.6, 100)
    ax.plot(xc + u, yo + 0.05 + amp * np.exp(-(u / 0.18) ** 2) * np.cos(2 * np.pi * u / 0.15),
            color=charts.line("rna"), lw=0.9)
    ax.text(xc, yo + 0.85, name, ha="center", fontsize=7.5, color=ink)
pulse(ax, 9.5, yp, 180, tok="enzyme")
ax.text(10.0, yp + 0.15, "pump π", fontsize=7.5, color=ink)
ax.annotate("", xy=(12.5, yp + 0.45), xytext=(9.8, yp + 0.45),
            arrowprops=dict(arrowstyle="->", color=charts.line("enzyme"), lw=1.0))
delay(ax, 7.0, 9.4, yp - 0.25, "t (stepped)")
ax.text(11.2, -1.45, r"echo amplitude $V(t)$ oscillates at the dipolar frequency $\nu_{\mathrm{dd}} \propto 1/r^3$", ha="center",
        fontsize=8, color=ink)
charts.title(ax, "C   Four-pulse DEER (PELDOR)")
fig.tight_layout()
