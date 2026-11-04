# Routes of transmission: direct and vertical, droplet and aerosol, vehicles, vectors, and the environment.
import numpy as np
from matplotlib.patches import Circle, Rectangle

import wikibio as bio
from wikibio import microbio as M

P = bio.P
rng = np.random.default_rng(0)
fig, ax = bio.canvas(19.0, 8.0)
bio.label(ax, (9.5, 7.75), "How an infection reaches the next host", size="title", bold=True)


def person(x, y, h=1.5, token="animal"):
    """A simple standing figure: head and body."""
    ax.add_patch(Circle((x, y + h * 0.78), h * 0.19, facecolor=P.fill(token), edgecolor=P.edge(token),
                        lw=1.1, zorder=10))
    ax.add_patch(Rectangle((x - h * 0.2, y), h * 0.4, h * 0.56, facecolor=P.fill(token),
                           edgecolor=P.edge(token), lw=1.1, zorder=9))
    return (x, y + h * 0.5)


def title(x, text, sub):
    bio.label(ax, (x, 6.9), text, size="small", bold=True)
    bio.label(ax, (x, 6.45), sub, size="tiny", color=P.muted())


# ---------------------------------------------------------------- 1. direct and vertical
X = 2.4
title(X, "Direct contact", "touch, sexual contact,\nmother to child")
person(X - 0.9, 4.0)
person(X + 0.9, 4.0)
bio.arrow(ax, (X - 0.45, 4.8), (X + 0.45, 4.8), kind="process")
person(X - 0.9, 1.6, h=1.3)
person(X + 0.35, 1.6, h=0.75, token="blood")
bio.arrow(ax, (X - 0.5, 2.1), (X + 0.1, 2.0), kind="process", bend=-0.2)
bio.label(ax, (X, 0.95), "vertical: placenta,\nbirth, milk", size="tiny", color=P.muted())

# ---------------------------------------------------------------- 2. droplet and aerosol
X = 6.6
title(X, "Droplet and aerosol", "particle size is a continuum")
person(X - 1.3, 4.0)
person(X + 1.4, 4.0)
for k in range(8):          # large droplets: fall within a short distance
    ax.add_patch(Circle((X - 0.85 + 0.14 * k, 4.78 - 0.035 * k ** 1.7), 0.085 - 0.004 * k,
                        facecolor=P.fill("blood"), edgecolor="none", alpha=0.85, zorder=11))
for k in range(30):         # aerosols: stay suspended and fill the room
    ax.add_patch(Circle((X - 0.8 + rng.uniform(0, 2.2), 4.9 + rng.uniform(0, 1.2)), 0.045,
                        facecolor=P.fill("virus"), edgecolor="none", alpha=0.8, zorder=11))
bio.label(ax, (X, 3.35), "large droplets fall within a metre or two;\nsmall aerosols stay suspended and "
                         "accumulate\nindoors — hence ventilation", size="tiny", color=P.muted())
bio.label(ax, (X, 1.9), "tuberculosis, pertussis, measles,\ninfluenza, SARS-CoV-2", size="tiny")

# ---------------------------------------------------------------- 3. vehicles
X = 11.6
title(X, "Vehicles", "water, food, blood, fomites")
person(X - 1.7, 4.0)
person(X + 1.7, 4.0)
for k, (dx, text, tok) in enumerate(((-0.8, "water", "channel"), (0.0, "food", "carbohydrate"),
                                     (0.8, "surfaces", "neutral"))):
    bio.box(ax, (X + dx * 1.15, 4.75), 1.05, 0.55, token=tok, radius=0.12)
    bio.label(ax, (X + dx * 1.15, 4.75), text, size="tiny", color=P.on_fill())
bio.arrow(ax, (X - 1.4, 4.4), (X - 1.0, 4.55), kind="process")
bio.arrow(ax, (X + 1.0, 4.55), (X + 1.4, 4.4), kind="process")
bio.label(ax, (X, 3.35), "the agent must survive outside a host:\nspores, non-enveloped viruses, cysts",
          size="tiny", color=P.muted())
bio.label(ax, (X, 2.1), "cholera, typhoid, norovirus,\nhepatitis A, $\\it{Clostridioides\\ difficile}$ spores",
          size="tiny")
bio.label(ax, (X, 1.05), "water and food are monitored with indicator\norganisms, not by seeking each pathogen",
          size="tiny", color=P.muted())

# ---------------------------------------------------------------- 4. vectors and the environment
X = 16.6
title(X, "Vectors and the environment", "an arthropod, or no host-to-host step")
person(X - 1.4, 4.0)
bio.icon(ax, "servier/mosquito", at=(X + 0.5, 4.9), height=1.0)
bio.arrow(ax, (X + 0.1, 4.75), (X - 1.0, 4.75), kind="process")
bio.label(ax, (X + 0.3, 3.9), "biological transmission:\nthe agent replicates\nin the vector", size="tiny",
          color=P.muted(), ha="left")
bio.label(ax, (X, 2.75), "plague, Lyme disease, rickettsioses,\ndengue, malaria", size="tiny")
M.bacillus(ax, (X - 1.5, 1.6), 1.0, 0.38, gram="+")
bio.arrow(ax, (X - 0.9, 1.6), (X - 0.2, 1.6), kind="process")
bio.label(ax, (X + 0.1, 0.95), "soil and water: tetanus, legionellosis\n(no onward transmission)", size="tiny",
          color=P.muted())
