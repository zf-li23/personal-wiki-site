# Antigenic variation (gene conversion), phase variation (DNA inversion), and the waves of bacteraemia they cause.
import numpy as np
from matplotlib.patches import Rectangle

import wikibio as bio
from wikibio import quant

P = bio.P
fig, ax = bio.canvas(19.0, 8.0)


def gene_box(x, y, w, text, token, italic=True, h=0.52):
    bio.box(ax, (x + w / 2, y), w, h, token=token, radius=0.08)
    bio.label(ax, (x + w / 2, y), text, size="tiny", italic=italic, color=P.on_fill())


# ================================================================ A: gene conversion
bio.panel(ax, "A", (0.1, 7.75))
bio.label(ax, (4.6, 7.75), "Antigenic variation: gene conversion", size="title", bold=True)
bio.label(ax, (4.6, 7.3), "$\\it{Neisseria\\ gonorrhoeae}$ pilin", size="tiny", color=P.muted())

bio.strand(ax, (0.7, 6.2), (8.9, 6.2), token="dna", wave=0.0, ends=False)
gene_box(0.9, 6.2, 1.9, "pilE (expressed)", "positive")
bio.label(ax, (1.25, 5.7), "promoter", size="tiny", color=P.muted())
bio.arrow(ax, (0.95, 5.95), (1.35, 5.95), kind="process")
for k in range(4):
    gene_box(3.6 + k * 1.35, 6.2, 1.15, "pilS", "neutral")
bio.label(ax, (6.3, 5.7), "10–20 silent cassettes: no promoter, variable segments", size="tiny", color=P.muted())

bio.arrow(ax, (4.3, 6.55), (2.2, 6.55), kind="process", bend=0.30, dashed=True)
bio.label(ax, (3.3, 7.05), "one cassette is copied in", size="tiny", color=P.muted())

bio.arrow(ax, (4.6, 5.25), (4.6, 4.85), kind="process")
for k, col in enumerate(("protein", "enzyme", "receptor", "drug")):
    bio.protein(ax, (2.0 + k * 1.75, 4.3), 1.0, 0.55, col, text=f"pilin {k + 1}", size="tiny")
bio.label(ax, (4.6, 3.6), "a new surface protein; the locus is unchanged, so the switch can repeat indefinitely",
          size="tiny", color=P.muted())

# ================================================================ B: DNA inversion
bio.panel(ax, "B", (9.6, 7.75))
bio.label(ax, (14.3, 7.75), "Phase variation: DNA inversion", size="title", bold=True)
bio.label(ax, (14.3, 7.3), "$\\it{Salmonella}$ flagellin", size="tiny", color=P.muted())

for j, (y, inverted) in enumerate(((6.3, False), (4.5, True))):
    bio.strand(ax, (10.1, y), (18.6, y), token="dna", wave=0.0, ends=False)
    bio.box(ax, (11.1, y), 1.5, 0.52, token="highlight", radius=0.08)
    bio.label(ax, (11.1, y), "promoter", size="tiny", color=P.on_fill())
    bio.arrow(ax, (10.6 if not inverted else 11.6, y + 0.45), (11.6 if not inverted else 10.6, y + 0.45),
              kind="process")
    gene_box(12.2, y, 1.6, "fljB", "positive" if not inverted else "neutral")
    gene_box(14.0, y, 1.6, "fljA", "positive" if not inverted else "neutral")
    gene_box(16.4, y, 1.6, "fliC", "neutral" if not inverted else "positive")
    bio.label(ax, (14.8, y - 0.55), "flagellin phase 2 and a repressor of $\\it{fliC}$" if not inverted
              else "nothing transcribed from the inverted promoter: $\\it{fliC}$ is free",
              size="tiny", color=P.muted())
bio.arrow(ax, (18.9, 6.1), (18.9, 4.8), kind="process", bend=0.35)
bio.arrow(ax, (18.9, 4.8), (18.9, 6.1), kind="process", bend=0.35)
bio.label(ax, (15.6, 5.5), "Hin invertase, ≈$10^{-4}$ per cell per generation", size="tiny", color=P.muted())
bio.label(ax, (14.3, 3.6), "the population always contains both phases: antibody against one leaves the other",
          size="tiny", color=P.muted())

# ================================================================ C: the waves that result
bio.panel(ax, "C", (0.1, 3.0))
bio.label(ax, (9.5, 3.0), "Why variation prolongs an infection: a simple model", size="title", bold=True)

# n variants: each grows logistically on a shared resource; antibody against a variant appears after a
# delay and clears it; a rare switch seeds the next variant while the current one is still abundant.
n, T, dt = 6, 60.0, 0.005
steps = int(T / dt)
r, K, kill, rho, thresh, seed = 1.3, 1.0, 3.0, 0.9, 0.15, 1e-5
x = np.zeros(n)
x[0] = 1e-4
a = np.zeros(n)
seeded = 1
hist = np.zeros((steps, n))
for s in range(steps):
    total = x.sum()
    x = np.clip(x + dt * (r * x * (1 - total / K) - kill * a * x), 0.0, None)
    a = a + dt * rho * (x > thresh) * (a + 0.02) * (1 - a)
    if seeded < n and x[seeded - 1] > 0.35 and x[seeded] == 0.0:
        x[seeded] = seed
        seeded += 1
    hist[s] = x
t = np.arange(steps) * dt

pC = quant.Plot(ax, (1.6, 0.6, 15.8, 1.9), xlim=(0, T), ylim=(0, 1.0),
                xlabel="time / days (arbitrary units)", ylabel="bacteria in blood",
                xticks=[0, 20, 40, 60], yticks=[(0, "0"), (1, "max")])
tokens = ("protein", "enzyme", "receptor", "drug", "dna", "positive")
for i in range(n):
    pC.line(t, hist[:, i], tokens[i], lw=1.5)
pC.line(t, hist.sum(axis=1), "ink", lw=1.0, dashed=True, text="total", at=0.9, size="tiny")
bio.label(ax, (9.5, 2.62), "each colour is one antigenic variant: antibody clears the current one, a rare new variant "
                           "grows, and the infection relapses", size="tiny", color=P.muted())
