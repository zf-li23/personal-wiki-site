# Local proliferation of lateral roots in a nutrient-rich patch (a simple 2D growth model; after the
# split-root and patch experiments of Drew 1975). A primary root grows down at a constant rate and
# initiates a lateral every 0.8 cm on alternating sides; each lateral grows at a rate proportional to the
# local nitrate concentration and branches (second order) with a probability that increases with it.
# (A) Uniform medium; (B) the same total nitrate concentrated in one patch (shaded): roots proliferate in
# the patch and are suppressed elsewhere (systemic signalling is not modelled, only the local response).
import matplotlib.pyplot as plt
import numpy as np


def grow(conc, seed=0, days=14):
    rng = np.random.default_rng(seed)
    segs = []
    tips = [dict(p=np.array([0.0, 0.0]), d=np.array([0.0, -1.0]), order=0, age=0)]
    since = 0.0
    side = 1
    dt = 0.1
    for _ in range(int(days / dt)):
        new = []
        for tip in tips:
            c = conc(*tip["p"])
            if tip["order"] == 0:
                v = 1.2
            else:
                v = (0.15 + 1.1 * c) / tip["order"]
            ang = rng.normal(0, 0.05 if tip["order"] == 0 else 0.12)
            ca, sa = np.cos(ang), np.sin(ang)
            dvec = np.array([ca * tip["d"][0] - sa * tip["d"][1], sa * tip["d"][0] + ca * tip["d"][1]])
            dvec = dvec + np.array([0, -0.25 if tip["order"] == 0 else -0.012])  # gravitropism (set-point angles)
            dvec /= np.hypot(*dvec)
            q = tip["p"] + v * dt * dvec
            q[1] = min(q[1], -0.05)
            segs.append((tip["p"].copy(), q.copy(), tip["order"]))
            tip["p"], tip["d"] = q, dvec
            tip["age"] += dt
            if tip["order"] == 1 and rng.random() < dt * 1.6 * c ** 2:
                a = rng.choice([-1, 1]) * np.radians(rng.uniform(50, 80))
                nd = np.array([np.cos(a) * dvec[0] - np.sin(a) * dvec[1], np.sin(a) * dvec[0] + np.cos(a) * dvec[1]])
                new.append(dict(p=q.copy(), d=nd, order=2, age=0))
        if tips[0]["p"][1] < -0.5:
            since += 1.2 * dt
            if since > 0.8 and tips[0]["p"][1] > -17:
                since = 0
                side *= -1
                a = np.radians(side * rng.uniform(65, 85))
                new.append(dict(p=tips[0]["p"].copy(), d=np.array([np.sin(a), -np.cos(a)]), order=1, age=0))
        tips += new
    return segs


uniform = lambda x, y: 0.45
def patch(x, y):
    return 0.12 + 2.2 * np.exp(-(((x - 3.2) / 2.2) ** 2 + ((y + 8.0) / 2.0) ** 2))


fig, axs = plt.subplots(1, 2, figsize=(10.5, 5.6))
for ax, conc, title in ((axs[0], uniform, "A   Uniform nitrate"), (axs[1], patch, "B   Nitrate-rich patch")):
    if conc is patch:
        X, Y = np.meshgrid(np.linspace(-11, 11, 200), np.linspace(-19, 1, 200))
        ax.contourf(X, Y, patch(X, Y), levels=[0.6, 1.2, 1.8, 2.5], colors=["#9fd0a8", "#6fbd80", "#43a35c"], alpha=0.45)
    for p, q, o in grow(conc, seed=3):
        ax.plot([p[0], q[0]], [p[1], q[1]], color=("#7a4e2d", "#a8744a", "#c9a06e")[o], lw=(2.4, 1.3, 0.8)[o],
                solid_capstyle="round")
    ax.axhline(0, color="0.5", lw=1)
    ax.set_xlim(-11, 11)
    ax.set_ylim(-19, 1)
    ax.set_aspect("equal")
    ax.set_title(title, loc="left", fontsize=10)
    ax.set_xlabel("x / cm")
axs[0].set_ylabel("Depth / cm")
for ax in axs:
    ax.spines[["top", "right"]].set_visible(False)
fig.tight_layout()
