"""Song learning as reinforcement learning by node perturbation (REINFORCE). A syllable is described by two
acoustic features (pitch, duration, in standardized units). The motor command m (HVC -> RA) is perturbed on each
rendition by LMAN-like exploratory noise xi ~ N(0, sigma^2 I); the bird compares the sung syllable with its
memorized template T and computes a reward R = -|m + xi - T|^2 + noise (auditory feedback plus evaluation,
the dopamine signal to Area X). The command moves in the direction of perturbations that did better than the
running average Rbar: m <- m + alpha (R - Rbar) xi (alpha = 0.02); on average this
climbs the reward gradient at a rate proportional to sigma^2. Three birds: intact (sigma = 0.3), LMAN inactivated
(sigma = 0.06) and deafened (no feedback: R carries no information about the song)."""
import numpy as np

import wikibio as bio
from wikibio import quant

P = bio.P
T = np.array([1.5, 1.0])
m0 = np.array([-1.2, -0.8])


def run(sigma, deaf=False, n=6000, alpha=0.02, seed=0):
    rng = np.random.default_rng(seed)
    m = m0.copy(); rbar = None; path = [m.copy()]; err = []
    for k in range(n):
        xi = rng.normal(0, sigma, 2)
        out = m + xi
        R = (-np.sum((out - T) ** 2) if not deaf else -6.0) + rng.normal(0, 0.2)
        delta = 0.0 if rbar is None else R - rbar
        rbar = R if rbar is None else 0.9 * rbar + 0.1 * R
        m = m + alpha * delta * xi
        err.append(np.sum((m - T) ** 2) ** 0.5)
        if k % 60 == 0:
            path.append(m.copy())
    return np.array(path), np.array(err)


runs = [("Intact", 0.3, False, "dna"), ("LMAN inactivated", 0.06, False, "rna"), ("Deafened", 0.3, True, "negative")]
fig, ax = bio.canvas(24, 10.5)
bio.panel(ax, "A", (0.3, 10.2))
p = quant.Plot(ax, (1.8, 1.6, 8.0, 8.0), xlim=(-2, 2.5), ylim=(-2, 2.5), xlabel="Pitch (standardized)",
               ylabel="Duration (standardized)", xticks=[-2, -1, 0, 1, 2], yticks=[-2, -1, 0, 1, 2])
bio.panel(ax, "B", (11.6, 10.2))
q = quant.Plot(ax, (13.4, 1.6, 9.8, 8.0), xlim=(0, 6000), ylim=(0, 3.5), xlabel="Renditions practiced",
               ylabel="Distance from template", xticks=[0, 2000, 4000, 6000], yticks=[0, 1, 2, 3])
for name, s, deaf, tok in runs:
    path, err = run(s, deaf, seed=1)
    path = np.clip(path, -2, 2.5)
    p.line(path[:, 0], path[:, 1], tok, lw=1.3)
    q.line(np.arange(len(err))[::10], err[::10], tok, lw=1.4)
p.points([T[0]], [T[1]], "highlight", r=0.2)
p.text(T[0] + 0.15, T[1] + 0.3, "template", ha="left")
p.points([m0[0]], [m0[1]], "ink", r=0.1)
p.text(m0[0], m0[1] - 0.3, "subsong", ha="center")
q.legend([(name, tok, "-") for name, s, deaf, tok in runs], at=q.xy(3600, 2.85))
ax.set_ylim(0.2, 10.5)
