# Axial muscles of a teleost (lateral view, transverse section of the tail) and of a lancelet (dorsal view).
# Schematic, not to scale.
import numpy as np
import wikibio as bio
import vertskel as vs

P = bio.P
fig, ax = bio.canvas(25, 11)

# ---------------------------------------------------------------- A: lateral view
bio.panel(ax, "A", (0.3, 10.6))
bio.label(ax, (0.9, 10.6), "Teleost, lateral view", size="title", ha="left")
x0, L, yc = 1.0, 15.0, 6.6
t = np.linspace(0, 1, 160)
half = 1.9 * np.where(t < 0.2, np.sqrt(t / 0.2), np.where(t < 0.62, 1.0, 1 - (t - 0.62) / 0.38 * 0.8))
xs = x0 + t * L
outline = np.vstack([np.column_stack([xs, yc + half]), np.column_stack([xs[::-1], yc - half[::-1]])])
# caudal fin
cf = np.array([(x0 + L - 0.1, yc + 0.35), (x0 + L + 1.6, yc + 1.9), (x0 + L + 1.1, yc), (x0 + L + 1.6, yc - 1.9),
               (x0 + L - 0.1, yc - 0.35)])
bio.shape(ax, cf, token="animal", zorder=2)
bio.shape(ax, outline, token="animal", zorder=3)
# muscle region (behind the head) split by the horizontal septum
m0 = x0 + 0.24 * L
hm = 1.9 * np.where(t < 0.62, 1.0, 1 - (t - 0.62) / 0.38 * 0.8) * 0.93
sel = xs >= m0
ep = np.vstack([np.column_stack([xs[sel], yc + hm[sel]]), np.column_stack([xs[sel][::-1], np.full(sel.sum(), yc)])])
hp = np.vstack([np.column_stack([xs[sel], np.full(sel.sum(), yc)]), np.column_stack([xs[sel][::-1], yc - hm[sel][::-1]])])
bio.shape(ax, ep, token="muscle", zorder=4, lw=0.8)
bio.shape(ax, hp, token="enzyme", zorder=4, lw=0.8)
# red muscle wedge along the septum
rw = np.array([(m0 + 0.5, yc), (x0 + 0.95 * L, yc + 0.08), (x0 + 0.95 * L, yc - 0.08)])
wed = np.vstack([np.column_stack([xs[sel], yc + 0.22 * hm[sel] / 1.77]), np.column_stack([xs[sel][::-1], yc - 0.22 * hm[sel][::-1] / 1.77])])
bio.shape(ax, wed, token="negative", zorder=5, lw=0.6)
# W-shaped myosepta
for xm in np.arange(m0 + 0.5, x0 + L - 0.3, 0.62):
    i = np.argmin(abs(xs - xm))
    h = hm[i]
    w = np.array([(xm - 0.1, yc + h), (xm + 0.3, yc + 0.5 * h), (xm - 0.35, yc), (xm + 0.3, yc - 0.5 * h),
                  (xm - 0.1, yc - h)])
    ax.plot(w[:, 0], w[:, 1], color=P.on_fill(), lw=0.8, zorder=6)
ax.plot([m0, x0 + L], [yc, yc], color=P.ink(), lw=1.1, zorder=7)
bio.shape(ax, vs.oval((x0 + 1.3, yc + 0.5), 0.35, 0.3), token="nucleus", zorder=7)
for p, q, s in [((x0 + 0.55 * L, yc + 1.2), (x0 + 0.5 * L, yc + 3.1), "epaxial muscle"),
                ((x0 + 0.55 * L, yc - 1.2), (x0 + 0.5 * L, yc - 3.0), "hypaxial muscle"),
                ((x0 + 0.78 * L, yc), (x0 + 0.86 * L, yc + 2.9), "horizontal septum (lateral line)"),
                ((x0 + 0.40 * L, yc + 0.12), (x0 + 0.30 * L, yc + 3.1), "red muscle"),
                ((x0 + 0.68 * L + 0.1, yc - 0.9), (x0 + 0.75 * L, yc - 3.0), "myoseptum")]:
    bio.callout(ax, p, q, s, size="tiny")
xc = x0 + 0.8 * L
ax.plot([xc, xc], [yc - 1.9, yc + 1.9], color=P.muted(), lw=0.9, ls=(0, (3, 2)), zorder=8)
bio.label(ax, (xc, yc - 2.15), "B", size="tiny", color=P.muted())

# ---------------------------------------------------------------- B: transverse section
bio.panel(ax, "B", (0.3, 2.9))
bio.label(ax, (0.9, 2.9), "Transverse section of the tail", size="title", ha="left")
cx, cy, R = 4.0, 1.25, 1.15
sec = vs.oval((cx, cy), R * 0.75, R)
bio.shape(ax, sec, token="animal", zorder=2)
for sign, tok in ((1, "muscle"), (-1, "enzyme")):
    th = np.linspace(0, np.pi, 60) if sign > 0 else np.linspace(np.pi, 2 * np.pi, 60)
    v = np.vstack([np.column_stack([cx + 0.68 * R * np.cos(th), cy + 0.93 * R * np.sin(th)]), [[cx - 0.68 * R, cy]]])
    bio.shape(ax, v, token=tok, zorder=3, lw=0.7)
    for side in (-1, 1):
        for r in (0.18, 0.3, 0.42):
            c = (cx + side * 0.32 * R, cy + sign * 0.42 * R)
            e = vs.oval(c, r * 0.8, r)
            ax.plot(np.append(e[:, 0], e[0, 0]), np.append(e[:, 1], e[0, 1]), color=P.on_fill(), lw=0.6, zorder=4)
ax.plot([cx - 0.75 * R, cx + 0.75 * R], [cy, cy], color=P.ink(), lw=1.0, zorder=5)
ax.plot([cx, cx], [cy - R, cy + R], color=P.ink(), lw=0.9, zorder=5)
bio.shape(ax, vs.oval((cx, cy), 0.13, 0.13), token="bone", zorder=6, lw=0.7)
bio.shape(ax, vs.oval((cx, cy + 0.3), 0.07, 0.07), token="neuron", zorder=6, lw=0.6)
bio.shape(ax, vs.oval((cx, cy - 0.28), 0.06, 0.06), token="blood", zorder=6, lw=0.6)
for p, q, s in [((cx + 0.4, cy + 0.6), (cx + 2.2, cy + 1.1), "epaxial: nested cones"),
                ((cx + 0.4, cy - 0.6), (cx + 2.2, cy - 1.0), "hypaxial"),
                ((cx + 0.13, cy), (cx + 2.2, cy + 0.05), "vertebra; septum"),
                ((cx, cy + 0.3), (cx - 2.3, cy + 0.9), "spinal cord"),
                ((cx, cy - 0.28), (cx - 2.3, cy - 0.7), "caudal artery, vein")]:
    bio.callout(ax, p, q, s, size="tiny")

# ---------------------------------------------------------------- C: lancelet
bio.panel(ax, "C", (10.3, 2.9))
bio.label(ax, (10.9, 2.9), "Lancelet, dorsal view (no horizontal septum)", size="title", ha="left")
lx0, lL, ly = 11.0, 12.5, 1.2
tt = np.linspace(0, 1, 120)
hw = 0.75 * np.sin(np.pi * np.clip(tt, 0.02, 0.98)) ** 0.6
lv = np.vstack([np.column_stack([lx0 + tt * lL, ly + hw]), np.column_stack([lx0 + tt[::-1] * lL, ly - hw[::-1]])])
bio.shape(ax, lv, token="muscle", zorder=3)
ax.plot([lx0 + 0.2, lx0 + lL - 0.2], [ly, ly], color=vs.edge("notochord"), lw=2.2, zorder=5)
for k, xm in enumerate(np.arange(lx0 + 0.8, lx0 + lL - 0.6, 0.55)):
    i = np.argmin(abs(lx0 + tt * lL - xm))
    h = hw[i]
    for side in (1, -1):
        xo = xm + (0.27 if side < 0 else 0.0)
        ax.plot([xo + 0.25, xo - 0.05], [ly + side * h, ly + side * 0.05], color=P.on_fill(), lw=0.8, zorder=4)
bio.callout(ax, (lx0 + 0.3 * lL, ly - 0.5), (lx0 + 0.35 * lL, ly - 1.4), "V-shaped myomeres, left and right offset by half a segment",
            size="tiny")
bio.callout(ax, (lx0 + 0.8 * lL, ly), (lx0 + 0.85 * lL, ly - 1.3), "notochord", size="tiny")
