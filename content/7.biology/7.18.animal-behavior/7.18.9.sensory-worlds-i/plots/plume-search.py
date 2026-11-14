# Two ways of finding an odor source (illustrative individual-based simulations).
# A: run-and-tumble in a smooth, stable gradient (a bacterium): runs at constant speed; the tumble rate
#    falls when the concentration sensed now exceeds that sensed a moment ago (temporal comparison).
# B: surge-and-cast in a turbulent plume (a male moth): the plume is a train of odor filaments released
#    by the source, carried downwind and meandering; on each contact the moth surges upwind, after losing
#    the plume it casts across the wind with growing amplitude.
import numpy as np
import wikibio as bio
from wikibio import charts

P = bio.P
rng = np.random.default_rng(0)
fig, ax = bio.canvas(24, 10.5)

# ---------------- A: run-and-tumble (units: body lengths), source at the origin
pa = charts.axes_at(ax, (1.5, 1.6, 8.6, 7.4))
xx, yy = np.meshgrid(np.linspace(-60, 60, 200), np.linspace(-60, 60, 200))
c = np.exp(-np.hypot(xx, yy) / 30)
pa.contour(xx, yy, c, levels=np.linspace(0.1, 0.9, 9), colors=[P.muted()], linewidths=0.5)


def conc(p):
    return np.exp(-np.hypot(*p) / 30)


for k, tok in enumerate(("channel", "receptor", "enzyme")):
    p = np.array([45.0, -35.0 + 25 * k])
    th = rng.uniform(0, 2 * np.pi)
    path = [p.copy()]
    prev = conc(p)
    for _ in range(700):
        p = p + 1.0 * np.array([np.cos(th), np.sin(th)])
        now = conc(p)
        rate = 0.05 if now > prev else 0.5      # tumble probability per step
        prev = now
        if rng.random() < rate:
            th = rng.uniform(0, 2 * np.pi)
        path.append(p.copy())
    path = np.array(path)
    pa.plot(path[:, 0], path[:, 1], color=charts.line(tok), lw=0.8)
    pa.plot(*path[0], "o", color=charts.line(tok), ms=4)
pa.plot(0, 0, "*", color=P.edge("negative"), ms=12)
pa.set_xlim(-60, 60)
pa.set_ylim(-60, 60)
pa.set_aspect("equal")
charts.style_axes(pa, "x / body lengths", "y / body lengths")
charts.title(pa, "A  Run and tumble in a smooth gradient")

# ---------------- B: surge and cast in a filamentous plume (units: m), wind blows towards +x
U, dt = 1.0, 0.02
src = np.array([0.0, 0.0])
T = 60.0
nfil = int(T / 0.05)
# filaments: released every 0.05 s, advected by the wind plus a slowly meandering crosswind component
t_rel = np.arange(nfil) * 0.05
phase = rng.uniform(0, 2 * np.pi)


def meander(t):
    return 0.12 * np.sin(0.5 * t + phase) + 0.06 * np.sin(1.3 * t + 2 * phase)


fil_noise = rng.normal(0, 1, nfil)


def filaments(t):
    alive = t_rel <= t
    age = t - t_rel[alive]
    x = U * age
    y = meander(t_rel[alive]) * age + 0.1 * np.sqrt(age) * fil_noise[alive]
    r = 0.08 + 0.04 * np.sqrt(age)
    return x, y, r


pb = charts.axes_at(ax, (12.6, 1.6, 10.6, 7.4))
xf, yf, rf = filaments(T)
keep = xf < 16
pb.scatter(xf[keep], yf[keep], s=6, color=P.fill("highlight"), edgecolors="none", alpha=0.9, zorder=1)

for k, (y0, tok) in enumerate(((0.6, "channel"), (-1.2, "receptor"))):
    p = np.array([14.0, y0])
    t, last_hit, mode = 0.0, -10.0, "cast"
    cast_dir, cast_amp, cast_t = 1.0, 0.4, 0.0
    path, hits = [p.copy()], []
    while t < T and np.hypot(*(p - src)) > 0.15:
        t += dt
        x, y, r = filaments(t)
        if np.any(np.hypot(x - p[0], y - p[1]) < r):
            if t - last_hit > 0.3:           # mark the onset of a contact
                hits.append(p.copy())
            last_hit = t
        if t - last_hit < 0.4:               # surge: upwind with a small zigzag
            v = np.array([-0.9, 0.25 * np.sin(12 * t)])
            cast_amp, cast_t = 0.4, 0.0
        else:                                 # cast: crosswind sweeps of growing amplitude
            cast_t += dt
            if cast_t > cast_amp / 0.8:
                cast_dir, cast_t, cast_amp = -cast_dir, 0.0, cast_amp * 1.35
            v = np.array([0.05, 0.8 * cast_dir])
        p = p + v * dt
        path.append(p.copy())
    path = np.array(path)
    pb.plot(path[:, 0], path[:, 1], color=charts.line(tok), lw=1.0, zorder=3)
    pb.plot(*path[0], "o", color=charts.line(tok), ms=4, zorder=4)
    if hits:
        h = np.array(hits)
        pb.plot(h[:, 0], h[:, 1], "o", color=P.edge("negative"), ms=2.2, zorder=4)
pb.plot(0, 0, "*", color=P.edge("negative"), ms=12, zorder=5)
pb.annotate("", xy=(3.5, 2.6), xytext=(0.8, 2.6),
            arrowprops=dict(arrowstyle="-|>", color=P.ink(), lw=1.2))
pb.text(2.15, 2.85, "wind", ha="center", fontsize=bio.core.FONT["tiny"], color=P.ink())
pb.set_xlim(-0.5, 16)
pb.set_ylim(-3.2, 3.2)
pb.set_aspect("equal")
charts.style_axes(pb, "Downwind distance / m", "Crosswind / m")
charts.title(pb, "B  Surge and cast in a turbulent plume")
bio.label(ax, (17.9, 0.35), "yellow: odor filaments; red dots: onsets of odor contacts; star: source", size="tiny",
          color=P.muted())
