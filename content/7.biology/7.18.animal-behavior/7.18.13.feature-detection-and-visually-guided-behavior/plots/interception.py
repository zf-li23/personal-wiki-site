"""Pursuit versus interception: three guidance laws against a prey flying in a straight line.

Prey: speed 1, starts at (0, 2) heading east. Predator: speed 1.5, starts at the origin.
Pure pursuit: the predator always heads at the prey's present position.
Constant bearing (parallel navigation): the predator turns so that the line of sight to the
prey keeps a constant direction; for a non-manoeuvring prey this is the collision course.
Proportional navigation: turning rate = N x rate of rotation of the line of sight (N = 3),
the law used by guided missiles and, to a good approximation, by falcons.
"""
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio

P = bio.P
dt = 0.002
vp, vq = 1.5, 1.0


def simulate(law, N=3.0, tmax=12):
    q = np.array([0.0, 2.0]); qv = np.array([vq, 0.0])
    p = np.array([0.0, 0.0])
    los = q - p
    h = np.arctan2(los[1], los[0])
    if law == "bearing":
        # solve the collision course once (prey does not manoeuvre)
        u = los / np.linalg.norm(los)
        perp = qv - np.dot(qv, u) * u
        along = np.sqrt(vp ** 2 - np.dot(perp, perp))
        d = perp + along * u
        h = np.arctan2(d[1], d[0])
    P_, Q_ = [p.copy()], [q.copy()]
    lam_old = np.arctan2(los[1], los[0])
    t = 0
    while t < tmax:
        los = q - p
        lam = np.arctan2(los[1], los[0])
        if law == "pursuit":
            h = lam
        elif law == "pn":
            dl = np.angle(np.exp(1j * (lam - lam_old)))
            h = h + N * dl
        lam_old = lam
        p = p + vp * dt * np.array([np.cos(h), np.sin(h)])
        q = q + qv * dt
        P_.append(p.copy()); Q_.append(q.copy())
        t += dt
        if np.linalg.norm(q - p) < 0.02:
            break
    return np.array(P_), np.array(Q_), t


fig, (a, b) = plt.subplots(1, 2, figsize=(10.5, 4.0), gridspec_kw={"width_ratios": [1.6, 1]})
res = {}
for law, col, lab in (("pursuit", P.edge("negative"), "pure pursuit"),
                      ("bearing", P.edge("dna"), "constant bearing"),
                      ("pn", P.edge("rna"), "proportional navigation (N = 3)")):
    pp, qq, T = simulate(law)
    res[lab] = (T, np.sum(np.linalg.norm(np.diff(pp, axis=0), axis=1)), col)
    a.plot(pp[:, 0], pp[:, 1], color=col, lw=2, label=lab)
    if law == "bearing":
        for k in np.linspace(0, len(pp) - 1, 6).astype(int)[:-1]:
            a.plot([pp[k, 0], qq[k, 0]], [pp[k, 1], qq[k, 1]], color=col, lw=0.6, ls=":")
pp, qq, T = simulate("pursuit")
a.plot(qq[:, 0], qq[:, 1], color=P.ink(), lw=1.2, ls="--", label="prey")
a.plot(0, 0, "o", color=P.ink(), ms=5); a.text(0.12, 0.02, "predator start", fontsize=8, color=P.ink())
a.plot(0, 2, "s", color=P.ink(), ms=5); a.text(0.05, 2.15, "prey start", fontsize=8, color=P.ink())
a.set_aspect("equal")
a.set_xlabel("x"); a.set_ylabel("y")
a.legend(frameon=False, fontsize=7.5, loc="lower right")
a.set_title("A", loc="left", fontweight="bold")
labs = list(res)
b.bar(range(3), [res[k][0] for k in labs], color=[res[k][2] for k in labs], width=0.6)
b.set_xticks(range(3)); b.set_xticklabels(["pursuit", "constant\nbearing", "PN"], fontsize=8)
b.set_ylabel("Time to capture")
b.set_title("B", loc="left", fontweight="bold")
for ax in (a, b):
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
fig.tight_layout()
