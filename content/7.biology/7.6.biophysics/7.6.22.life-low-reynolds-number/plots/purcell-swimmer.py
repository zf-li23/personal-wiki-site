"""Purcell's three-link swimmer, simulated with resistive-force theory (gamma_perp = 2 gamma_par,
links of equal length l, no inertia: total force and torque on the swimmer vanish at every
instant). A: the swimmer at the four corners of its stroke, a square loop in the plane of the
two hinge angles (front arm first, then rear arm, then front back, then rear back). B: path of
the middle link's centre over three strokes for the square loop (it advances along its body axis)
and for a reciprocal stroke (both arms flap together and return along the same path: no net
motion, the scallop theorem). C: net displacement per stroke against the stroke amplitude:
it grows as the square of the amplitude, the area enclosed by the loop in shape space."""

import numpy as np
import matplotlib.pyplot as plt
import wikibio as bio
from wikibio import charts

P = bio.P
l, gpar, gper, nq = 1.0, 1.0, 2.0, 16
s = (np.arange(nq) + 0.5) / nq * l
ds = l / nq


def points(q):
    x, y, ph, a1, a2 = q
    e = lambda t: np.array([np.cos(t), np.sin(t)])
    X = np.array([x, y])
    mid = X[None] + (s - l / 2)[:, None] * e(ph)[None]
    J1, J2 = X + l / 2 * e(ph), X - l / 2 * e(ph)
    front = J1[None] + s[:, None] * e(ph + a1)[None]
    rear = J2[None] - s[:, None] * e(ph - a2)[None]
    tang = [np.tile(e(ph), (nq, 1)), np.tile(e(ph + a1), (nq, 1)), np.tile(e(ph - a2), (nq, 1))]
    return np.vstack([mid, front, rear]), np.vstack(tang)


def body_rate(q, da):
    """Velocities (xdot, ydot, phidot) for prescribed hinge rates da = (a1dot, a2dot)."""
    p0, t = points(q)
    h = 1e-6
    J = []
    for k in range(5):
        dq = np.zeros(5); dq[k] = h
        J.append((points(q + dq)[0] - points(q - dq)[0]) / (2 * h))
    J = np.array(J)  # 5 x N x 2: velocity of each point per unit rate of q_k
    X = q[:2]
    M = np.zeros((3, 5))
    for k in range(5):
        u = J[k]
        ut = np.sum(u * t, axis=1)[:, None] * t
        f = -(gpar * ut + gper * (u - ut)) * ds
        r = p0 - X
        M[:2, k] = f.sum(axis=0)
        M[2, k] = np.sum(r[:, 0] * f[:, 1] - r[:, 1] * f[:, 0])
    return -np.linalg.solve(M[:, :3], M[:, 3:] @ da)


def run(path, steps_per_leg=60):
    q = np.array([0.0, 0.0, 0.0, path[0][0], path[0][1]])
    traj = [q[:2].copy()]
    for (a, b), (c, dd) in zip(path[:-1], path[1:]):
        da = (np.array([c - a, dd - b])) / steps_per_leg
        for _ in range(steps_per_leg):
            k1 = body_rate(q, da)
            qm = q.copy(); qm[:3] += k1 / 2; qm[3:] += da / 2
            k2 = body_rate(qm, da)
            q[:3] += k2; q[3:] += da
            traj.append(q[:2].copy())
    return q, np.array(traj)


A = np.pi / 4
square = [(-A, -A), (A, -A), (A, A), (-A, A), (-A, -A)]
recip = [(-A, -A), (A, A), (-A, -A)]

fig, axs = plt.subplots(1, 3, figsize=(11.0, 3.3), gridspec_kw=dict(width_ratios=[0.75, 1.3, 1]))
fig.subplots_adjust(wspace=0.38, left=0.04, right=0.97, bottom=0.17, top=0.86)

ax = axs[0]
for i, (a1, a2) in enumerate(square[:4]):
    pts, _ = points(np.array([0, -i * 1.9, 0, a1, a2]))
    for k, tok in enumerate(("bacterium", "dna", "blood")):
        seg = pts[k * nq:(k + 1) * nq]
        ax.plot(seg[:, 0], seg[:, 1], color=charts.line(tok), lw=3, solid_capstyle="round")
    ax.text(-2.4, -i * 1.9, f"{i + 1}", fontsize=bio.core.FONT["small"], color=P.ink(), va="center")
ax.text(1.0, 0.75, "front arm", fontsize=bio.core.FONT["tiny"], color=charts.line("dna"))
ax.text(-2.0, 0.75, "rear arm", fontsize=bio.core.FONT["tiny"], color=charts.line("blood"))
ax.set_xlim(-2.6, 1.7); ax.set_ylim(-6.6, 1.2); ax.set_aspect("equal"); ax.axis("off")
charts.title(ax, "A  A non-reciprocal stroke")

ax = axs[1]
qa, tra = run(square + square[1:] + square[1:])
qb, trb = run(recip + recip[1:] + recip[1:])
ax.plot(tra[:, 0], tra[:, 1], color=charts.line("dna"), lw=1.4, label="square loop")
ax.plot(trb[:, 0], trb[:, 1], color=charts.line("negative"), lw=1.4, ls="--", label="reciprocal flapping")
ax.plot(0, 0, "o", color=P.ink(), ms=3)
ax.legend(frameon=False, fontsize=bio.core.FONT["tiny"], labelcolor=P.ink(), loc="lower left")
charts.style_axes(ax, "x / l", "y / l")
charts.title(ax, "B  Three strokes")

ax = axs[2]
amps = np.linspace(0.1, 1.2, 9)
disp = []
for am in amps:
    sq = [(-am, -am), (am, -am), (am, am), (-am, am), (-am, -am)]
    qq, _ = run(sq, 40)
    disp.append(np.hypot(qq[0], qq[1]))
disp = np.array(disp)
ax.plot(amps, disp, "o-", color=charts.line("dna"), ms=4, lw=1.2, label="simulation")
c = disp[1] / amps[1] ** 2
ax.plot(amps, c * amps**2, color=P.muted(), lw=1.0, ls="--", label=r"$\propto$ amplitude$^2$")
ax.legend(frameon=False, fontsize=bio.core.FONT["tiny"], labelcolor=P.ink())
charts.style_axes(ax, "hinge amplitude / rad", "net displacement / l")
charts.title(ax, "C  Area of the loop")
