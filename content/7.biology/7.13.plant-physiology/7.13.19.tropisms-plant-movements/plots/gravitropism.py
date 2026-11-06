# Quantitative gravitropism. (A) The sine law: the initial bending response of a root or shoot displaced by
# an angle theta from its set-point is proportional to sin(theta) (Sachs); points are simulated measurements.
# (B) Return to the vertical when the bending rate obeys the sine law, d theta / dt = -k sin theta, whose
# solution is tan(theta/2) = tan(theta0/2) exp(-k t) (k = 0.025 min^-1, illustrative); a root placed upside
# down (180 degrees) is unstable and starts only through noise or circumnutation. (C) Stokes sedimentation
# of an amyloplast (density excess 450 kg m^-3) over 10 um, the height of a columella cell, as a function of
# its radius for several effective viscosities of the cytoplasm; the band marks the observed few minutes.
import matplotlib.pyplot as plt
import numpy as np

rng = np.random.default_rng(1)
fig, (a, b, c) = plt.subplots(1, 3, figsize=(13, 4.0))
th = np.linspace(0, 180, 300)
a.plot(th, np.sin(np.radians(th)), color="#2f6fb5", lw=2.4, label="sin θ")
ts = np.arange(10, 180, 15)
a.plot(ts, np.sin(np.radians(ts)) + rng.normal(0, 0.06, ts.size), "o", color="0.3", ms=5, label="simulated data")
a.set_xlabel("Displacement from vertical θ / °")
a.set_ylabel("Initial bending rate (relative)")
a.set_xlim(0, 180)
a.set_ylim(0, 1.2)
a.set_xticks([0, 45, 90, 135, 180])
a.legend(frameon=False, fontsize=8.5, loc="lower center")
a.set_title("A   Sine law", loc="left", fontsize=10)
k = 0.025
t = np.linspace(0, 240, 500)
for th0, col in ((30, "#3a9a5b"), (90, "#2f6fb5"), (150, "#c0504d"), (179, "#8f6db3")):
    thet = 2 * np.degrees(np.arctan(np.tan(np.radians(th0) / 2) * np.exp(-k * t)))
    b.plot(t, thet, color=col, lw=2.2, label=f"θ₀ = {th0}°")
b.set_xlabel("Time t / min")
b.set_ylabel("Tip angle θ / °")
b.set_xlim(0, 240)
b.set_ylim(0, 185)
b.legend(frameon=False, fontsize=8.5, loc="upper right")
b.set_title("B   dθ/dt = −k sin θ", loc="left", fontsize=10)
a_um = np.linspace(0.5, 3, 200)
drho, g, H = 450.0, 9.8, 10e-6
for eta, col in ((1e-3, "0.5"), (1e-2, "#2f6fb5"), (5e-2, "#3a9a5b"), (2e-1, "#c0504d")):
    v = 2 * drho * g * (a_um * 1e-6) ** 2 / (9 * eta)
    c.semilogy(a_um, H / v / 60, color=col, lw=2.2, label=f"η = {eta * 1e3:g} mPa s")
c.axhspan(2, 10, color="#f2c14e", alpha=0.3, lw=0)
c.text(2.95, 3.2, "observed\n(minutes)", ha="right", fontsize=8.5, color="0.35")
c.set_xlabel("Amyloplast radius a / µm")
c.set_ylabel("Time to fall 10 µm / min")
c.set_xlim(0.5, 3)
c.set_ylim(0.01, 1000)
c.legend(frameon=False, fontsize=8, loc="upper right")
c.set_title("C   Statolith sedimentation (Stokes)", loc="left", fontsize=10)
for x in (a, b, c):
    x.spines[["top", "right"]].set_visible(False)
fig.tight_layout()
