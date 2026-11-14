# Pressure receiver and pressure-difference receiver (schematic and directivity model).
# A plane sound wave of frequency f arrives from azimuth theta (0 = straight ahead, +90 deg = the side
# of the right ear). Pressure receiver: the tympanum is driven by the outside pressure alone, |p| = 1
# from every direction. Pressure-difference receiver: the inside of the right tympanum receives the
# sound entering at the left ear, attenuated by g and delayed by an internal time tau; the membrane is
# driven by p_out - p_in. Ears d = 1 cm apart, f = 5 kHz, g = 0.8 (illustrative values for a small insect).
import numpy as np
from matplotlib.patches import Rectangle, Circle
import wikibio as bio
from wikibio import charts

P = bio.P
c, d, f, g = 343.0, 0.01, 5000.0, 0.8
w = 2 * np.pi * f
th = np.linspace(-np.pi, np.pi, 721)
tx = d / (2 * c) * np.sin(th)              # arrival time offset of the two ears (right ear leads for theta>0)
p_out = np.exp(1j * w * tx)                # right ear, outside
fig, ax = bio.canvas(25, 10.4)

# --- schematics
def head(x0, y0, closed):
    ax.add_patch(Rectangle((x0, y0), 4.2, 2.0, facecolor=P.fill("animal"), edgecolor=P.edge("animal"), lw=1, zorder=2))
    for xe in (x0, x0 + 4.2):
        ax.plot([xe, xe], [y0 + 0.5, y0 + 1.5], color=P.edge("receptor"), lw=3.2, zorder=4)
    if closed:
        for xe in (x0 + 0.08, x0 + 3.42):
            ax.add_patch(Rectangle((xe, y0 + 0.5), 0.7, 1.0, facecolor=P.fill("extracellular"),
                                   edgecolor=P.edge("neutral"), lw=0.8, zorder=3))
    else:
        ax.add_patch(Rectangle((x0 + 0.08, y0 + 0.7), 4.04, 0.6, facecolor=P.fill("extracellular"),
                               edgecolor=P.edge("neutral"), lw=0.8, zorder=3))
        bio.arrow(ax, (x0 + 0.5, y0 + 1.0), (x0 + 3.7, y0 + 1.0), kind="process", color=P.muted())

head(1.0, 6.4, True)
bio.label(ax, (3.1, 9.2), "A  Pressure receivers", size="small", bold=True)
bio.label(ax, (3.1, 5.9), "closed cavity behind each tympanum", size="tiny", color=P.muted())
head(1.0, 1.8, False)
bio.label(ax, (3.1, 4.6), "B  Pressure-difference receivers", size="small", bold=True)
bio.label(ax, (3.1, 1.3), "air passage links the inner faces", size="tiny", color=P.muted())
bio.label(ax, (3.1, 0.75), "membrane driven by p(out) − p(in)", size="tiny", color=P.muted())
for y in (7.4, 2.8):
    bio.callout(ax, (5.2, y), (6.6, y + 0.9), "tympanum", size="tiny")

# --- directivity (right ear)
pol = charts.axes_at(ax, (10.6, 1.4, 7.2, 7.2), projection="polar")
pol.set_theta_zero_location("N")
pol.set_theta_direction(-1)
curves = [("pressure receiver", np.ones_like(th), "neutral", "-")]
for tau, tok, ls in ((0.0, "channel", "--"), (d / c, "receptor", "-"), (1.6 * d / c, "enzyme", "-")):
    p_in = g * np.exp(1j * w * (-tx - tau))
    curves.append((f"difference, internal delay {tau * 1e6:.0f} µs", np.abs(p_out - p_in), tok, ls))
for name, r, tok, ls in curves:
    pol.plot(th, r, color=charts.line(tok), lw=1.6, ls=ls)
pol.set_rlim(0, 1.9)
pol.set_rticks([0.5, 1, 1.5])
pol.set_xticks(np.deg2rad([0, 90, 180, 270]))
pol.set_xticklabels(["front", "right", "back", "left"])
pol.tick_params(colors=P.muted(), labelcolor=P.ink(), labelsize=bio.core.FONT["tiny"])
pol.grid(color=P.mix(P.muted(), P.surface(), 0.6), lw=0.5)
pol.spines["polar"].set_color(P.muted())
pol.set_facecolor("none")
bio.label(ax, (14.2, 9.85), "C  Drive of the right tympanum by direction", size="small", bold=True)
for k, (name, _, tok, ls) in enumerate(curves):
    yy = 7.6 - 0.55 * k
    ax.plot([19.6, 20.3], [yy, yy], color=charts.line(tok), lw=1.6, ls=ls)
    bio.label(ax, (20.45, yy), name, size="tiny", ha="left")
bio.label(ax, (19.6, 5.0), "ears 1 cm apart, 5 kHz:", size="tiny", ha="left", color=P.muted())
bio.label(ax, (19.6, 4.55), "external time difference", size="tiny", ha="left", color=P.muted())
bio.label(ax, (19.6, 4.1), "at most 29 µs", size="tiny", ha="left", color=P.muted())
