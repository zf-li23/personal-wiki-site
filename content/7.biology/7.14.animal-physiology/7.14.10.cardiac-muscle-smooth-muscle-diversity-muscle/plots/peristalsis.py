# Kinematics of earthworm peristaltic crawling (kinematic model after Quillin 1999; illustrative numbers).
# Each segment alternates between an anchoring phase (longitudinal muscle contracted: short and thick, setae
# out, stationary relative to the ground; duration t_s) and an advancing phase (circular muscle contracted:
# long and thin, moving forward; duration t_p). Stride period T = t_s + t_p = 1 s, t_p = 0.4 s, stride length
# S = 0.4 segment lengths. Segment i (i = 0 at the head) starts its advancing phase delta = 0.12 s after
# segment i - 1: the wave of contraction travels from head to tail while the worm moves forward.
# (A) position of 12 segments against time: each moves in steps (stationary while anchored), the steps are
#     phase-shifted down the body and the worm advances S per stride; (B) state of each segment (advancing
#     dark, anchoring light): the diagonal bands are the peristaltic waves running backwards along the body.
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import ListedColormap

N, T, tp, S, delta = 12, 1.0, 0.4, 0.4, 0.12
t = np.linspace(0, 4, 2000)


def g(tau):
    k = np.floor(tau / T)
    u = (tau - k * T) / tp
    ramp = np.where(u < 1, (1 - np.cos(np.pi * np.clip(u, 0, 1))) / 2, 1.0)
    return S * (k + ramp)


fig, (a, b) = plt.subplots(1, 2, figsize=(12, 4.6))
cm = plt.get_cmap("plasma")
for i in range(N):
    x = -i * 1.0 + g(t - i * delta)
    a.plot(t, x, color=cm(0.2 + 0.7 * i / (N - 1)), lw=1.6)
a.text(0.0, 0.35, "head (segment 0)", fontsize=8.5, color="0.45")
a.text(0.0, -(N - 1) - 1.1, "tail (segment 11)", fontsize=8.5, color="0.45")
a.annotate("", xy=(3.9, 1.7), xytext=(3.9, 0.1), arrowprops=dict(arrowstyle="->", color="0.45"))
a.text(3.84, 0.9, "direction\nof travel", ha="right", fontsize=8.5, color="0.45")
a.set_xlabel("Time / s")
a.set_ylim(-12.8, 2.3)
a.set_ylabel("Position of segment / segment lengths")
a.set_title("A   Stepwise advance of each segment", loc="left", fontsize=10)

state = np.zeros((N, len(t)))
for i in range(N):
    tau = t - i * delta
    ph = np.mod(tau, T)
    state[i] = (ph < tp).astype(float)
cmap = ListedColormap(["#d8e6f3", "#2f6fb5"])
b.imshow(state, aspect="auto", origin="upper", extent=[t[0], t[-1], N - 0.5, -0.5], cmap=cmap, interpolation="nearest")
b.set_xlabel("Time / s\ndark: advancing (long, thin);  light: anchored (short, thick)")
b.set_ylabel("Segment number (0 = head)")
b.set_title("B   Waves of contraction run tailwards", loc="left", fontsize=10)
for ax in (a, b):
    ax.spines[["top", "right"]].set_visible(False)
fig.tight_layout()
