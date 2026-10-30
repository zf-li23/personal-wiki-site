"""Synchronization. (A) Quenching of the free oscillation of a forced van der Pol oscillator (eps = 0.1, omega =
2.5) compared with the averaged prediction. (B, C) A 40 x 12 sheet of phase oscillators with 5% scatter of
natural frequency and nearest-neighbour coupling: order parameter over time and final phases."""
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
import wikibio as bio
from wikibio import charts

P_ = bio.P
FT = bio.core.FONT
fig = plt.figure(figsize=(12.6, 3.9))
gs = fig.add_gridspec(2, 3, width_ratios=[1, 1, 1.25], left=0.06, right=0.99, bottom=0.15, top=0.88, wspace=0.32, hspace=0.55)

a = fig.add_subplot(gs[:, 0])
eps, w = 0.1, 2.5
gs_ = np.linspace(0, 1.8, 10)
amp = []
for g in gs_:
    K = g * (1 - w * w)
    s = solve_ivp(lambda t, y: [y[1], eps * (1 - y[0] ** 2) * y[1] - y[0] + K * np.sin(w * t)], [0, 360], [0.5, 0.0],
                  max_step=0.1, rtol=1e-6, atol=1e-8)
    m = s.t > 260
    y = s.y[0][m] - g * np.sin(w * s.t[m])
    amp.append((y.max() - y.min()) / 2)
gl = np.linspace(0, 1.8, 200)
a.plot(gl, 2 * np.sqrt(np.clip(1 - gl ** 2 / 2, 0, None)), color=P_.ink(), lw=1.3, label="averaging")
a.plot(gs_, amp, "o", color=charts.line("drug"), ms=4, label="numerical")
a.axvline(np.sqrt(2), color=P_.muted(), lw=0.8, ls="--")
a.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P_.ink(), loc="lower left")
charts.style_axes(a, "forced amplitude gamma", "free amplitude a")
charts.title(a, "A  Entrainment by quenching")

nx, ny = 40, 12
rng = np.random.default_rng(1)
om = 2 * np.pi * (1 + 0.05 * rng.standard_normal((ny, nx)))
th0 = rng.uniform(0, 2 * np.pi, (ny, nx))


def run(Kc, T=30.0, dt=0.02):
    th = th0.copy()
    Rs = []
    for k in range(int(T / dt)):
        cpl = np.zeros_like(th)
        cnt = np.zeros_like(th)
        for sh, ax_ in ((1, 0), (-1, 0), (1, 1), (-1, 1)):
            nb = np.roll(th, sh, axis=ax_)
            mask = np.ones_like(th)
            if ax_ == 0:
                mask[0 if sh == 1 else -1, :] = 0
            else:
                mask[:, 0 if sh == 1 else -1] = 0
            cpl += mask * np.sin(nb - th)
            cnt += mask
        th = th + dt * (om + Kc * 2 * np.pi * cpl / cnt)
        if k % 5 == 0:
            Rs.append(abs(np.exp(1j * th).mean()))
    return np.arange(len(Rs)) * dt * 5, np.array(Rs), np.mod(th, 2 * np.pi)


res = {Kc: run(Kc) for Kc in (0.0, 1.0)}
b = fig.add_subplot(gs[:, 1])
for Kc, tok in ((0.0, "negative"), (1.0, "positive")):
    t, R, _ = res[Kc]
    b.plot(t, R, color=charts.line(tok), lw=1.5, label="coupling %.1f" % Kc)
b.set_ylim(0, 1.05)
b.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P_.ink(), loc="center right")
charts.style_axes(b, "time (clock periods)", "order parameter R")
charts.title(b, "B  Synchrony")
for row, (Kc, txt) in enumerate(((0.0, "C  no coupling"), (1.0, "coupled"))):
    c = fig.add_subplot(gs[row, 2])
    c.imshow(res[Kc][2], cmap="twilight", vmin=0, vmax=2 * np.pi, interpolation="nearest", aspect="auto")
    c.set_xticks([])
    c.set_yticks([])
    charts.title(c, txt)
