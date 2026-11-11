"""State estimation during a one-dimensional reach: prediction, sensation and the Kalman filter.

State s = (x, v) (cm, cm/s), dt = 10 ms. Commanded acceleration a_t: minimum-jerk profile for a
10 cm reach in 600 ms, then hold. Dynamics: x' = x + v dt, v' = v + a dt + w, w ~ N(0, q)
(motor noise, s.d. 0.4 cm/s per step). Measurement (proprioception): y = x + e, e ~ N(0, r),
s.d. 1.0 cm.
Estimators: prediction only (forward model driven by the efference copy, no sensory input),
sensation only (y itself), and the Kalman filter combining both.
A: one trial. B: root-mean-square error of each estimator against time (500 trials).
C: Kalman gain for position and posterior s.d. of the position estimate.
"""
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio

P = bio.P
rng = np.random.default_rng(0)
dt = 0.01
n = 100
t = np.arange(n) * dt
D, Tm = 10.0, 0.6
tau = np.clip(t / Tm, 0, 1)
acc = D / Tm**2 * (60 * tau - 180 * tau**2 + 120 * tau**3) * (t <= Tm)
A = np.array([[1, dt], [0, 1]])
B = np.array([0, dt])
H = np.array([[1.0, 0.0]])
q, r = 0.4**2, 1.0**2
Q = np.diag([0.0, q])


def trial():
    s = np.zeros(2)
    xs, ys = [], []
    for k in range(n):
        xs.append(s[0])
        ys.append(s[0] + rng.normal(0, np.sqrt(r)))
        s = A @ s + B * acc[k] + np.array([0, rng.normal(0, np.sqrt(q))])
    return np.array(xs), np.array(ys)


def kalman(ys):
    m = np.zeros(2)
    Pm = np.diag([1e-4, 1e-4])
    est, gain, sd = [], [], []
    for k in range(n):
        S = H @ Pm @ H.T + r
        K = (Pm @ H.T / S).ravel()
        m = m + K * (ys[k] - m[0])
        Pm = (np.eye(2) - np.outer(K, H)) @ Pm
        est.append(m[0])
        gain.append(K[0])
        sd.append(np.sqrt(Pm[0, 0]))
        m = A @ m + B * acc[k]
        Pm = A @ Pm @ A.T + Q
    return np.array(est), np.array(gain), np.array(sd)


pred = np.zeros(n)
s = np.zeros(2)
for k in range(n):
    pred[k] = s[0]
    s = A @ s + B * acc[k]

err = {"pred": [], "sens": [], "kf": []}
for i in range(500):
    x, y = trial()
    kf, gain, sd = kalman(y)
    err["pred"].append(pred - x)
    err["sens"].append(y - x)
    err["kf"].append(kf - x)
    if i == 0:
        x0, y0, kf0 = x, y, kf

fig, axs = plt.subplots(1, 3, figsize=(13, 3.9))
cP, cS, cK = P.edge("rna"), P.muted(), P.edge("dna")
ax = axs[0]
ax.plot(t * 1000, y0, ".", color=cS, ms=3, label="sensation $y_t$")
ax.plot(t * 1000, x0, color=P.ink(), lw=2.2, label="true position")
ax.plot(t * 1000, pred, color=cP, lw=1.6, ls="--", label="prediction only")
ax.plot(t * 1000, kf0, color=cK, lw=1.8, label="Kalman filter")
ax.set_ylabel("Position / cm")
ax.set_title("A  One reach", loc="left", fontsize=10)
ax.legend(frameon=False, fontsize=8, loc="lower right")
ax = axs[1]
for key, col, lab in (("pred", cP, "prediction only"), ("sens", cS, "sensation only"), ("kf", cK, "Kalman filter")):
    ax.plot(t * 1000, np.sqrt(np.mean(np.array(err[key]) ** 2, axis=0)), color=col, lw=2.0, label=lab)
ax.set_ylabel("RMS error / cm")
ax.set_ylim(0, 1.6)
ax.set_title("B  Error of the estimate", loc="left", fontsize=10)
ax.legend(frameon=False, fontsize=8, loc="upper left")
ax = axs[2]
ax.plot(t * 1000, gain, color=P.edge("positive"), lw=2.0, label="Kalman gain (position)")
ax.plot(t * 1000, sd, color=cK, lw=2.0, ls="--", label="posterior s.d. / cm")
ax.set_ylim(0, 0.5)
ax.set_title("C  Gain and uncertainty", loc="left", fontsize=10)
ax.legend(frameon=False, fontsize=8, loc="center right")
for a in axs:
    a.set_xlabel("Time / ms")
    a.grid(True, alpha=0.3)
fig.tight_layout()
