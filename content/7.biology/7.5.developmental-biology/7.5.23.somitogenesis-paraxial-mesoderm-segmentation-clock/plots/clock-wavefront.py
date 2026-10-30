"""Clock and wavefront: kymograph of a strip of paraxial mesoderm in the embryo frame (tail bud moving at speed v,
front a fixed distance L behind it, cells slowing their clock as they approach the front and freezing there);
phase of single cells; somite length S = vP."""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import to_rgb
import wikibio as bio
from wikibio import charts

P_ = bio.P
FT = bio.core.FONT
v, L, y0, w0, slow = 1.0, 3.0, 4.0, 2 * np.pi, 0.6


def phase(y, t):
    tb = (y - y0) / v
    tau = np.clip(t - tb, 0, L / v)
    return w0 * tb + w0 * (tau - 0.5 * slow * v * tau ** 2 / L), t - tb


fig, axs = plt.subplots(1, 3, figsize=(12.4, 3.9), gridspec_kw={"width_ratios": [1.3, 1, 0.9]})
fig.subplots_adjust(left=0.06, right=0.985, bottom=0.16, top=0.86, wspace=0.32)
T = 6.0
ts = np.linspace(0, T, 300)
ys = np.linspace(0, y0 + v * T + 0.2, 300)
tt, yy = np.meshgrid(ts, ys)
ph, age = phase(yy, tt)
img = np.zeros(tt.shape + (3,))
surf = np.array(to_rgb(P_.surface()))
hi = np.array(to_rgb(P_.fill("highlight")))
base = np.array(to_rgb(P_.light("mesoderm")))
s1, s2 = np.array(to_rgb(P_.fill("mesoderm"))), np.array(to_rgb(P_.light("rrna")))
e = 0.5 * (1 + np.cos(ph))
psm = (age >= 0) & (age < L / v)
img[psm] = base + (hi - base) * e[psm][:, None]
froz = age >= L / v
idx = np.floor(ph / (2 * np.pi)).astype(int) % 2
img[froz & (idx == 0)] = s1
img[froz & (idx == 1)] = s2
img[age < 0] = surf
a = axs[0]
a.imshow(img, origin="lower", aspect="auto", extent=[0, T, ys[0], ys[-1]], interpolation="nearest")
a.plot(ts, y0 + v * ts, color=P_.ink(), lw=1.2)
a.plot(ts, y0 + v * ts - L, color=P_.ink(), lw=1.0, ls="--")
a.text(0.3, y0 + 0.9, "tail bud", fontsize=FT["tiny"], color=P_.ink(), rotation=24)
a.text(3.2, y0 + v * 3.2 - L - 0.95, "front", fontsize=FT["tiny"], color=P_.ink(), rotation=24)
charts.style_axes(a, "time (clock periods)", "position along axis", box=True)
charts.title(a, "A  Kymograph")

b = axs[1]
toks = ["dna", "protein", "enzyme", "drug"]
for k, yb in enumerate((4.5, 5.5, 6.5, 7.5)):
    t = np.linspace((yb - y0) / v, T, 200)
    p, _ = phase(np.full_like(t, yb), t)
    b.plot(t, p / (2 * np.pi), color=charts.line(toks[k]), lw=1.5)
    b.plot(t[0], p[0] / (2 * np.pi), "o", color=charts.line(toks[k]), ms=3)
charts.style_axes(b, "time (clock periods)", "phase (cycles)")
charts.title(b, "B  Single cells slow down and freeze")

c = axs[2]
Pp = np.linspace(0.2, 3.0, 50)
for vv, tok in ((50, "dna"), (100, "protein"), (150, "drug")):
    c.plot(Pp, vv * Pp, color=charts.line(tok), lw=1.5, label="v = %d $\\mu$m/h" % vv)
c.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P_.ink(), loc="upper left")
charts.style_axes(c, "clock period P (h)", "somite length S ($\\mu$m)")
charts.title(c, "C  S = vP")
