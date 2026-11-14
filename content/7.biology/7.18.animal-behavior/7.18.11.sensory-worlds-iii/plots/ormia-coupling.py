# Mechanically coupled ears of the parasitoid fly Ormia ochracea: a two-mode model (after Miles,
# Robert and Hoy 1995; illustrative damping). The two tympana, joined by a cuticular bridge, move as a
# sum of an antiphase "rocking" mode (resonance 7.1 kHz, damping ratio 0.3) and an in-phase "bending"
# mode (30 kHz, damping ratio 0.6). The sound reaches the ears with an acoustic time difference
# dt = (d/c) sin(theta), d = 0.5 mm. The in-phase mode is driven by the mean pressure (about 1), the
# rocking mode by the tiny pressure difference; near 5 kHz the rocking mode is close to resonance and
# the bending mode is not, so the small difference is amplified.
import numpy as np
from matplotlib.patches import Polygon
import wikibio as bio
from wikibio import quant

P = bio.P
d, c = 0.5e-3, 343.0
fr, zr, fb, zb = 7100.0, 0.3, 30000.0, 0.6


def response(f, theta):
    w = 2 * np.pi * f
    dt = d / c * np.sin(theta)
    H = lambda f0, z: 1 / ((2 * np.pi * f0) ** 2 - w ** 2 + 2j * z * (2 * np.pi * f0) * w)
    a, b = np.cos(w * dt / 2), 1j * np.sin(w * dt / 2)
    x1 = H(fb, zb) * a + H(fr, zr) * b          # ear nearer the source
    x2 = H(fb, zb) * a - H(fr, zr) * b
    return np.angle(x1 / x2) / w, 20 * np.log10(np.abs(x1 / x2)), dt


fig, ax = bio.canvas(25, 9.6)

# A: the two modes
def bridge(cx, cy, tilt, lift, title):
    bio.label(ax, (cx, cy + 1.6), title, size="small", bold=True)
    ax.plot([cx - 2.2, cx + 2.2], [cy - 0.9, cy - 0.9], color=P.muted(), lw=0.8)
    ax.add_patch(Polygon([(cx - 0.25, cy - 0.9), (cx + 0.25, cy - 0.9), (cx, cy - 0.35)], closed=True,
                         facecolor=P.fill("neutral"), edgecolor=P.edge("neutral")))
    yl, yr = cy + lift + tilt, cy + lift - tilt
    ax.plot([cx - 1.8, cx + 1.8], [yl, yr], color=P.edge("animal"), lw=3, solid_capstyle="round", zorder=5)
    for x, y, s in ((cx - 1.8, yl, "L"), (cx + 1.8, yr, "R")):
        ax.plot([x - 0.45, x + 0.45], [y, y], color=P.edge("receptor"), lw=4, zorder=6)
        bio.label(ax, (x, y + 0.45), s, size="tiny")
    ax.plot([cx - 1.8, cx + 1.8], [cy, cy], color=P.muted(), lw=0.6, ls=":")


bridge(3.2, 6.6, 0.45, 0.0, "Rocking mode (7.1 kHz)")
bridge(3.2, 2.4, 0.0, 0.45, "Bending mode (30 kHz)")
bio.label(ax, (3.2, 0.5), "tympana 0.5 mm apart, joined by a bridge", size="tiny", color=P.muted())

# B: amplification versus frequency (source at 90 deg)
f = np.linspace(1000, 15000, 400)
mi, ml, dt = response(f, np.pi / 2)
pb = quant.Plot(ax, (8.4, 1.8, 6.8, 6.4), xlim=(1, 15), ylim=(-20, 50), xlabel="Frequency / kHz",
                ylabel="Interaural time difference / µs", xticks=[1, 5, 10, 15], yticks=[-20, 0, 20, 40])
pb.hline(0, dashed=False)
pb.line(f / 1000, mi * 1e6, "receptor", text="tympanal vibration", at=0.42, dy=0.3)
pb.line(f / 1000, dt * 1e6 * np.ones_like(f), "channel", dashed=True, text="acoustic, 1.5 µs", at=0.7, dy=0.25)
pb.vline(5, text="cricket song", token="muted")
bio.label(ax, (11.8, 9.0), "B  Source at 90°", size="small", bold=True)

# C: versus azimuth at 5 kHz
th = np.deg2rad(np.linspace(-90, 90, 181))
mi, ml, dt = response(5000.0, th)
pc = quant.Plot(ax, (17.4, 1.8, 6.8, 6.4), xlim=(-90, 90), ylim=(-40, 40), xlabel="Azimuth / deg",
                ylabel="Time difference / µs", xticks=[-90, -45, 0, 45, 90], yticks=[-40, -20, 0, 20, 40])
pc.line(np.rad2deg(th), mi * 1e6, "receptor", text="tympana", at=0.85, dy=-0.4)
pc.line(np.rad2deg(th), dt * 1e6, "channel", dashed=True, text="acoustic", at=0.88, dy=0.3)
pc.hline(0, dashed=False)
bio.label(ax, (20.8, 9.0), "C  5 kHz", size="small", bold=True)
_, ild90, _ = response(5000.0, np.pi / 2)
bio.label(ax, (20.8, 0.4), f"level difference at 90°: {float(ild90):.1f} dB (acoustic: about 0 dB)", size="tiny",
          color=P.muted())
bio.panel(ax, "A", (0.2, 9.4))
