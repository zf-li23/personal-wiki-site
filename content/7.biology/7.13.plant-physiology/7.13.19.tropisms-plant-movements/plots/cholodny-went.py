# A minimal Cholodny-Went model of phototropic bending of a coleoptile (illustrative parameters).
# Unilateral blue light at t = 0 starts lateral auxin transport in the tip after a short lag; the fraction of
# the auxin stream on the shaded side rises from 0.5 to f_s (0.68, about 2 : 1, the classic tip
# diffusion data) with a time constant of 10 min; total auxin is unchanged. The redistributed stream reaches
# the elongation zone after a transport delay (5 mm at 10 mm/h = 30 min). Elongation rate on each side is a
# saturating function of auxin, r = r_max A / (A + K); the bending rate is (r_shaded - r_lit) / d
# (d = 1.5 mm coleoptile diameter, L = 10 mm elongation zone), integrated to the bending angle.
import matplotlib.pyplot as plt
import numpy as np

t = np.linspace(-20, 180, 2001)
lag, tau, delay = 3.0, 10.0, 30.0


def side_rates(fs, K=0.6, rmax=0.0027):
    f = 0.5 + (fs - 0.5) * np.clip(1 - np.exp(-(t - lag - delay) / tau), 0, None) * (t > lag + delay)
    A_s, A_l = 2 * f, 2 * (1 - f)  # relative auxin, 1 = dark level
    return rmax * A_s / (A_s + K), rmax * A_l / (A_l + K)  # strain rate, min^-1


d, L = 1.5, 10.0  # mm
fig, (a, b) = plt.subplots(1, 2, figsize=(11, 4.2))
rs, rl = side_rates(0.68)
a.plot(t, rs * 6000, color="#c0504d", lw=2.4, label="shaded side")
a.plot(t, rl * 6000, color="#2f6fb5", lw=2.4, label="lit side")
a.axvline(0, color="0.5", lw=0.8, ls=":")
a.text(2, 13, "light on", fontsize=8.5, color="0.4")
a.set_xlabel("Time after onset of unilateral blue light t / min")
a.set_ylabel("Elongation rate / % h⁻¹")
a.set_xlim(-20, 180)
a.set_ylim(0, 14)
a.legend(frameon=False, fontsize=8.5, loc="upper left")
a.set_title("A   Growth of the two flanks", loc="left", fontsize=10)
for fs, col, name in ((0.68, "#c0504d", "f = 0.68 (2 : 1)"), (0.6, "#d9822b", "f = 0.60"), (0.55, "#8f6db3", "f = 0.55")):
    rs, rl = side_rates(fs)
    dt = t[1] - t[0]
    angle = np.degrees(np.cumsum((rs - rl) * L / d) * dt)
    b.plot(t, angle, color=col, lw=2.2, label=f"shaded fraction {name}")
b.axvline(0, color="0.5", lw=0.8, ls=":")
b.set_xlabel("Time t / min")
b.set_ylabel("Bending angle / °")
b.set_xlim(-20, 180)
b.set_ylim(0, 30)
b.legend(frameon=False, fontsize=8.5, loc="upper left")
b.set_title("B   Curvature from differential growth", loc="left", fontsize=10)
for x in (a, b):
    x.spines[["top", "right"]].set_visible(False)
fig.tight_layout()
