# Recruitment of a motor-unit pool by the size principle (a simplified Fuglevand-type model, 1993; illustrative).
# 120 motor units; unit i (i = 1 smallest) has recruitment threshold RT_i = exp(ln 30 * i / 120) (arbitrary
# excitation units, the last unit recruited at 60 % of maximal excitation), peak tetanic force
# P_i = exp(ln 100 * i / 120) and twitch contraction time T_i from 90 ms (smallest) down to 30 ms (largest).
# Above threshold a unit fires at 8 Hz + 1 Hz per unit of excess excitation, up to 35 Hz. Its force is
# P_i r^2.5 / (r^2.5 + r50^2.5) with r50 = 0.6 / T_i (slow units fuse at lower rates).
# (A) firing rates of every tenth unit against excitation; (B) total force (relative to maximum) and the
#     number of recruited units; (C) the force step added by each newly recruited unit, as a fraction of the
#     force already present: after the first few units it stays at a few per cent, so force is graded in
#     steps that remain small relative to the force already produced (fine control at every level).
import matplotlib.pyplot as plt
import numpy as np

n = 120
i = np.arange(1, n + 1)
RT = np.exp(np.log(30) * i / n)
Emax = RT[-1] / 0.6
Pk = np.exp(np.log(100) * i / n)
T = 0.090 * Pk ** (-np.log(3) / np.log(100))
r50 = 0.6 / T
E = np.linspace(0, Emax, 1500)


def rates(e):
    fr = np.where(e >= RT, np.minimum(8 + 1.0 * (e - RT), 35.0), 0.0)
    return fr


def force(e):
    fr = rates(e)
    return np.sum(Pk * fr**2.5 / (fr**2.5 + r50**2.5))


F = np.array([force(e) for e in E])
Fmax = F[-1]
fig, (a, b, c) = plt.subplots(1, 3, figsize=(13.5, 4.2))
cmap = plt.get_cmap("plasma")
for k in range(0, n, 10):
    fr = np.where(E >= RT[k], np.minimum(8 + (E - RT[k]), 35.0), np.nan)
    a.plot(E / Emax * 100, fr, color=cmap(0.15 + 0.75 * k / n), lw=1.6)
a.set_xlabel("Excitatory drive / % of maximum")
a.set_ylabel("Firing rate / Hz")
a.set_ylim(0, 40)
a.text(3, 37, "small units first", fontsize=8.5, color="0.45")
a.text(70, 12, "largest units", fontsize=8.5, color="0.45")
a.set_title("A   Rate coding of each unit", loc="left", fontsize=10)

nrec = np.array([np.sum(RT <= e) for e in E])
b.plot(E / Emax * 100, F / Fmax * 100, color="#c0504d", lw=2.4, label="total force")
b.set_xlabel("Excitatory drive / % of maximum")
b.set_ylabel("Force / % of maximum", color="#c0504d")
b2 = b.twinx()
b2.plot(E / Emax * 100, nrec, color="#2f6fb5", lw=1.8, ls="--", label="units recruited")
b2.set_ylabel("Number of units recruited", color="#2f6fb5")
b2.set_ylim(0, 130)
b.axvline(60, color="0.5", lw=0.8, ls=":")
b.text(61, 8, "recruitment\ncomplete;\nrate coding only", fontsize=8.5, color="0.45")
b.set_title("B   Force grading", loc="left", fontsize=10)

steps = []
for k in range(1, n):
    e0 = RT[k] - 1e-6
    f0 = force(e0)
    f1 = force(RT[k] + 1e-6)
    steps.append((f1 - f0) / f0 * 100)
c.semilogy(i[1:], steps, ".", color="#2f6fb5", ms=4)
c.set_xlabel("Recruitment order of the unit")
c.set_ylabel("Force step on recruitment / % of present force")
c.set_ylim(0.1, 100)
c.set_title("C   Relative force step", loc="left", fontsize=10)
for x in (a, c):
    x.spines[["top", "right"]].set_visible(False)
b.spines[["top"]].set_visible(False)
b2.spines[["top"]].set_visible(False)
fig.tight_layout()
