# The proboscis apparatus of a nemertean (schematic longitudinal sections, anterior left, dorsal up; not to
# scale). A: proboscis withdrawn. The proboscis is an inverted tube lying in the rhynchocoel, a fluid-filled
# coelomic cavity above the gut; it opens at the tip of the head through the rhynchodaeum and is anchored at
# the rear by a retractor muscle. The cerebral ganglia form a ring around the rhynchodaeum. B: proboscis
# everted. Contraction of the muscles of the rhynchocoel wall raises the pressure of its fluid and turns the
# proboscis inside out, like the finger of a glove; in hoplonemerteans a calcareous stylet on a basis comes
# to lie at its tip. The retractor muscle pulls it back.
import numpy as np
import wikibio as bio

P = bio.P
fig, ax = bio.canvas(30, 9.0)


def worm(x0, x1, yc, h):
    bio.shape(ax, bio.smooth_closed([[x0, yc + 0.2], [x0 + 0.35, yc + h * 0.8], [x0 + 1.6, yc + h], [x1 - 1.6, yc + h * 0.9],
                                     [x1 - 0.3, yc + h * 0.5], [x1, yc], [x1 - 0.3, yc - h * 0.5], [x1 - 1.6, yc - h * 0.9],
                                     [x0 + 1.6, yc - h], [x0 + 0.35, yc - h * 0.8]]), token="neutral", zorder=5)
    bio.shape(ax, [[x0 + 2.4, yc - 0.75], [x1 - 0.8, yc - 0.75], [x1 - 0.8, yc - 0.15], [x0 + 2.4, yc - 0.15]],
              token="endoderm", zorder=6, lw=0.8)
    ax.plot([x0 + 1.4, x1 - 0.8], [yc - h * 0.65] * 2, color=P.fill("blood"), lw=2.2, zorder=7)   # lateral vessel
    bio.shape(ax, bio.smooth_closed([[x0 + 1.2, yc + 0.55], [x0 + 1.6, yc + 0.85], [x0 + 1.95, yc + 0.55],
                                     [x0 + 1.6, yc + 0.0]]), token="neuron", zorder=12)
    ax.plot([x0 + 1.6, x1 - 1.0], [yc - h * 0.8] * 2, color=P.edge("neuron"), lw=1.4, zorder=7)  # lateral nerve cord


# ---------------- A ----------------
bio.panel(ax, "A", (0.2, 8.8))
bio.label(ax, (7.2, 8.5), "Proboscis withdrawn", size="normal", bold=True)
x0, x1, yc, h = 0.8, 14.2, 4.4, 1.6
worm(x0, x1, yc, h)
bio.shape(ax, [[x0 + 2.0, yc + 0.05], [x1 - 2.2, yc + 0.05], [x1 - 2.2, yc + 1.05], [x0 + 2.0, yc + 1.05]],
          token="coelom", zorder=8, lw=0.9)
ax.plot([x0 + 0.05, x0 + 2.0], [yc + 0.55, yc + 0.55], color=P.edge("ectoderm"), lw=2.4, zorder=9)  # rhynchodaeum
t = np.linspace(x0 + 2.0, x1 - 3.4, 100)
ax.plot(t, yc + 0.55 + 0.12 * np.sin(t * 3), color=P.edge("mesoderm"), lw=3.2, zorder=10)
ax.plot([x1 - 3.4, x1 - 2.2], [yc + 0.55, yc + 0.55], color=P.edge("muscle"), lw=1.6, zorder=10)
bio.callout(ax, (x0 + 0.6, yc + 0.55), (1.2, 7.6), "Rhynchodaeum (opening)")
bio.callout(ax, (x0 + 1.6, yc + 0.75), (4.0, 7.6), "Cerebral ganglia (ring)")
bio.callout(ax, (x0 + 5.0, yc + 0.6), (7.0, 7.6), "Inverted proboscis")
bio.callout(ax, (x0 + 8.0, yc + 0.95), (10.0, 7.6), "Rhynchocoel (coelom)")
bio.callout(ax, (x1 - 2.8, yc + 0.55), (13.4, 7.6), "Retractor muscle")
bio.callout(ax, (x0 + 7.0, yc - 0.45), (6.0, 1.2), "Gut (with anus)")
bio.callout(ax, (x0 + 9.5, yc - h * 0.65), (10.2, 1.2), "Lateral blood vessel")
bio.callout(ax, (x0 + 3.0, yc - h * 0.8), (2.4, 1.2), "Lateral nerve cord")

# ---------------- B ----------------
bio.panel(ax, "B", (15.4, 8.8))
bio.label(ax, (22.8, 8.5), "Proboscis everted", size="normal", bold=True)
x0, x1 = 20.8, 29.6
worm(x0, x1, yc, h)
bio.shape(ax, [[x0 + 2.0, yc + 0.25], [x1 - 2.2, yc + 0.25], [x1 - 2.2, yc + 0.85], [x0 + 2.0, yc + 0.85]],
          token="coelom", zorder=8, lw=0.9)
ax.plot([x1 - 2.2, x1 - 6.0], [yc + 0.55] * 2, color=P.edge("muscle"), lw=1.6, zorder=10)
pts = np.array([[x1 - 6.0, yc + 0.55], [x0 + 1.0, yc + 0.55], [x0 - 1.0, yc + 0.9], [x0 - 2.8, yc + 1.8], [x0 - 4.4, yc + 2.0]])
ax.plot(pts[:, 0], pts[:, 1], color=P.edge("mesoderm"), lw=5.0, zorder=11, solid_capstyle="round")
ax.plot(pts[:, 0], pts[:, 1], color=P.fill("mesoderm"), lw=3.4, zorder=12, solid_capstyle="round")
ax.plot([x0 - 4.4, x0 - 5.0], [yc + 2.0, yc + 2.08], color=P.ink(), lw=2.0, zorder=13, solid_capstyle="round")
for xa in (x0 + 4.0, x0 + 5.6):
    bio.arrow(ax, (xa + 0.6, yc + 1.25), (xa - 0.6, yc + 1.25), kind="process", lw=0.9)
bio.label(ax, (x0 + 4.8, yc + 1.65), "pressure", size="tiny", color=P.muted())
bio.callout(ax, (x0 - 4.9, yc + 2.06), (16.6, 7.6), "Stylet (Hoplonemertea)")
bio.callout(ax, (x0 - 2.0, yc + 1.4), (19.8, 7.6), "Everted proboscis")
bio.callout(ax, (x0 + 7.0, yc + 0.8), (26.6, 7.6), "Rhynchocoel muscles contract")
bio.label(ax, (17.4, 2.0), "Prey (an annelid or crustacean) is wrapped,\nstabbed and drawn to the mouth", size="small",
          color=P.muted(), ha="left")
