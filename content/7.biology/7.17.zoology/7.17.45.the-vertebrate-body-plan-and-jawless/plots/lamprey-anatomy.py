# Schematic anatomy of an adult lamprey and of its larva (ammocoete), lateral views with anterior to the
# left; internal organs are drawn inside the body outline. Not to scale; height exaggerated.
import numpy as np
import wikibio as bio
import vertskel as vs

P = bio.P


def outline(x0, length, h, head=0.18, tail=0.82, fin=None):
    """Closed outline of an eel-shaped body: dorsal and ventral profiles from snout to tail tip."""
    x = np.linspace(0, 1, 120)
    half = h * np.where(x < head, np.sqrt(np.clip(x / head, 0, 1)) * 0.85 + 0.15,
                        np.where(x < tail, 1.0, 1 - (x - tail) / (1 - tail) * 0.985))
    xs = x0 + x * length
    top = np.column_stack([xs, half])
    bot = np.column_stack([xs[::-1], -half[::-1]])
    return np.vstack([top, bot])


def body(ax, x0, y0, length, h, token="animal"):
    v = outline(x0, length, h)
    v[:, 1] += y0
    bio.shape(ax, v, token=token, zorder=3)
    return v


fig, ax = bio.canvas(24, 11.5)

# ---------------- A: adult
y0, x0, L, H = 8.3, 2.2, 18.0, 0.85
bio.panel(ax, "A", (0.4, 10.9))
bio.label(ax, (1.0, 10.9), "Adult lamprey", size="title", ha="left")
xs = np.linspace(0, 1, 50)
# dorsal fins and caudal fin
for a, b, hh in ((0.50, 0.62, 0.55), (0.66, 0.82, 0.75)):
    t = np.linspace(0, 1, 30)
    fx = x0 + (a + (b - a) * t) * L
    fy = y0 + H + hh * np.sin(np.pi * t) ** 0.8
    bio.shape(ax, np.vstack([np.column_stack([fx, fy]), [[fx[-1], y0 + H - 0.05], [fx[0], y0 + H - 0.05]]]),
              token="animal", zorder=2)
t = np.linspace(0, 1, 30)
cx = x0 + (0.84 + 0.16 * t) * L
bio.shape(ax, np.vstack([np.column_stack([cx, y0 + 0.2 + 0.55 * np.sin(np.pi * t)]),
                         np.column_stack([cx[::-1], y0 - 0.2 - 0.45 * np.sin(np.pi * t[::-1])])]),
          token="animal", zorder=2)
body(ax, x0, y0, L, H)
# buccal funnel (oral disc) at the front
disc = bio.blob((x0 + 0.05, y0 - 0.35), 0.35, 0.75, wobble=0.02, seed=3)
bio.shape(ax, disc, token="protein", zorder=6)
# notochord and nerve cord
nx = np.linspace(x0 + 2.0, x0 + L - 0.4, 2)
ax.plot(nx, [y0 + 0.05, y0 + 0.05], color=vs.edge("notochord"), lw=5.0, solid_capstyle="round", zorder=7)
ax.plot(nx, [y0 + 0.05, y0 + 0.05], color=vs.color("notochord"), lw=3.6, solid_capstyle="round", zorder=7)
ax.plot([x0 + 1.4, x0 + L - 0.6], [y0 + 0.4, y0 + 0.3], color=P.fill("neuron"), lw=2.2, zorder=7)
brain = bio.blob((x0 + 1.35, y0 + 0.4), 0.55, 0.22, wobble=0.03, seed=5)
bio.shape(ax, brain, token="neuron", zorder=8)
# eye, nasohypophyseal opening, pineal
bio.shape(ax, bio.blob((x0 + 1.6, y0 + 0.2), 0.22, 0.22, wobble=0.0), token="nucleus", zorder=9)
ax.plot([x0 + 1.05], [y0 + H * 0.82], "o", ms=5, color=P.ink(), zorder=9)
nas = bio.blob((x0 + 1.05, y0 + 0.55), 0.18, 0.12, wobble=0.0)
bio.shape(ax, nas, token="receptor", zorder=8)
# oesophagus (dorsal) and branchial tube with gill pouches (ventral)
ax.plot([x0 + 0.6, x0 + 6.5], [y0 - 0.15, y0 - 0.15], color=P.edge("enzyme"), lw=2.4, zorder=7)
ax.plot([x0 + 1.2, x0 + 5.0], [y0 - 0.45, y0 - 0.45], color=P.edge("blood"), lw=2.0, zorder=7)
gill_x = [x0 + 2.4 + 0.42 * k for k in range(7)]
for gx in gill_x:
    bio.shape(ax, bio.blob((gx, y0 - 0.45), 0.17, 0.25, wobble=0.0), token="blood", zorder=8)
    ax.plot([gx], [y0 - 0.45], "o", ms=3.2, color=P.on_fill(), zorder=9)
# heart, liver, intestine, gonad, kidney, anus
bio.shape(ax, bio.blob((x0 + 5.5, y0 - 0.55), 0.35, 0.22, wobble=0.0), token="muscle", zorder=8)
bio.shape(ax, bio.blob((x0 + 6.4, y0 - 0.45), 0.5, 0.28, wobble=0.04, seed=2), token="mitochondrion", zorder=7)
ax.plot([x0 + 6.5, x0 + 0.66 * L], [y0 - 0.2, y0 - 0.45], color=P.edge("enzyme"), lw=3.0, zorder=7)
bio.shape(ax, bio.blob((x0 + 0.52 * L, y0 - 0.12), 1.8, 0.2, wobble=0.03, seed=7), token="highlight", zorder=6)
ax.plot([x0 + 7.2, x0 + 0.66 * L], [y0 + 0.2, y0 + 0.15], color=P.edge("vesicle"), lw=2.0, zorder=6)
ax.plot([x0 + 0.66 * L], [y0 - H * 0.9], "o", ms=4, color=P.ink(), zorder=9)

lab = [((x0 - 0.2, y0 - 0.9), (x0 - 0.6, y0 - 2.1), "buccal funnel with horny teeth"),
       ((x0 + 1.05, y0 + 0.55), (x0 + 0.6, y0 + 2.0), "nasohypophyseal opening and sac"),
       ((x0 + 1.35, y0 + 0.55), (x0 + 3.0, y0 + 2.3), "brain"),
       ((x0 + 1.6, y0 + 0.2), (x0 + 4.6, y0 + 2.0), "eye"),
       ((gill_x[3], y0 - 0.6), (x0 + 3.6, y0 - 2.1), "7 gill pouches on the branchial tube"),
       ((x0 + 3.5, y0 - 0.15), (x0 + 6.0, y0 + 1.9), "oesophagus"),
       ((x0 + 5.5, y0 - 0.7), (x0 + 6.6, y0 - 2.1), "heart"),
       ((x0 + 6.6, y0 - 0.5), (x0 + 9.0, y0 - 2.1), "liver"),
       ((x0 + 0.52 * L, y0 - 0.3), (x0 + 0.52 * L + 0.6, y0 - 2.1), "gonad (single)"),
       ((x0 + 0.40 * L, y0 + 0.2), (x0 + 0.40 * L - 0.3, y0 + 2.2), "kidney"),
       ((x0 + 0.58 * L, y0 + 0.05), (x0 + 0.62 * L, y0 + 2.3), "notochord"),
       ((x0 + 0.75 * L, y0 + 0.32), (x0 + 0.77 * L, y0 + 2.6), "nerve cord"),
       ((x0 + 0.66 * L, y0 - H * 0.9), (x0 + 0.66 * L + 1.0, y0 - 2.1), "anus, urogenital papilla")]
for p, q, s in lab:
    bio.callout(ax, p, q, s, size="tiny")

# ---------------- B: ammocoete
y1, x1, L1, H1 = 2.7, 2.2, 13.0, 0.6
bio.panel(ax, "B", (0.4, 4.8))
bio.label(ax, (1.0, 4.8), "Larva (ammocoete)", size="title", ha="left")
t = np.linspace(0, 1, 60)
fx = x1 + (0.45 + 0.55 * t) * L1
bio.shape(ax, np.vstack([np.column_stack([fx, y1 + H1 + 0.35 * np.sin(np.pi * t) ** 0.6]),
                         np.column_stack([fx[::-1], y1 - 0.1 - 0.3 * np.sin(np.pi * t[::-1]) ** 0.6])]),
          token="animal", zorder=2)
body(ax, x1, y1, L1, H1)
hood = bio.blob((x1 + 0.25, y1 - 0.1), 0.45, 0.55, wobble=0.03, seed=9)
bio.shape(ax, hood, token="protein", zorder=6)
ax.plot([x1 + 1.4, x1 + L1 - 0.3], [y1 + 0.05, y1 + 0.05], color=vs.color("notochord"), lw=3.0, zorder=7)
ax.plot([x1 + 1.0, x1 + L1 - 0.4], [y1 + 0.3, y1 + 0.25], color=P.fill("neuron"), lw=1.8, zorder=7)
bio.shape(ax, bio.blob((x1 + 1.1, y1 + 0.15), 0.12, 0.12, wobble=0.0), token="neutral", zorder=9)
for k in range(7):
    gx = x1 + 1.6 + 0.38 * k
    ax.plot([gx, gx], [y1 - 0.45, y1 + 0.0], color=P.fill("blood"), lw=2.4, zorder=8)
bio.shape(ax, bio.blob((x1 + 2.5, y1 - 0.48), 1.0, 0.08, wobble=0.0), token="er", zorder=9)
ax.plot([x1 + 4.4, x1 + 0.7 * L1], [y1 - 0.15, y1 - 0.3], color=P.edge("enzyme"), lw=2.6, zorder=7)
blab = [((x1 + 0.2, y1 - 0.6), (x1 - 0.4, y1 - 1.7), "oral hood (no teeth, no disc)"),
        ((x1 + 1.1, y1 + 0.15), (x1 + 0.8, y1 + 1.6), "eye beneath the skin"),
        ((x1 + 2.6, y1 - 0.2), (x1 + 3.1, y1 + 1.6), "pharynx with 7 pairs of gill slits"),
        ((x1 + 2.5, y1 - 0.55), (x1 + 3.6, y1 - 1.7), "endostyle (becomes thyroid)"),
        ((x1 + 0.7 * L1, y1 + 0.8), (x1 + 0.72 * L1, y1 + 1.6), "continuous median fin fold"),
        ((x1 + 0.55 * L1, y1 - 0.22), (x1 + 0.55 * L1 + 0.5, y1 - 1.7), "straight gut")]
for p, q, s in blab:
    bio.callout(ax, p, q, s, size="tiny")
bio.label(ax, (17.4, 3.2), "3-7 years filter feeding\nburied in mud,\nthen metamorphosis", size="small",
          color=P.muted(), ha="left")
