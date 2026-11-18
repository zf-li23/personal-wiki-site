# A scenario model of a green turtle rookery with temperature-dependent sex determination.
# Incubation temperature T(t) = 29.0 degC in 1990 plus a warming trend and interannual noise; proportion
# female p(T) = 1 / (1 + exp(-(T - 29.3)/0.4)) (the reaction norm of 7.19.4). Adults survive with 0.95
# per year; hatchlings recruit as adults after 30 years; the fraction of a female's clutches that are
# fertilized is 1 - exp(-h M/F) with h = 10 (males mate with many females). Recruitment is scaled so
# that the population is stationary under the temperatures of 1990.
# Scenarios: warming of 0.01, 0.025 and 0.045 degC per year (low, intermediate, high emissions), and the
# intermediate scenario with half of the nests shaded (1.5 degC cooler) from 2030.
import numpy as np
import matplotlib.pyplot as plt
import wikibio as bio

P = bio.P
rng = np.random.default_rng(1)
years = np.arange(1900, 2201)
noise = rng.normal(0, 0.35, years.size)
pf = lambda T: 1 / (1 + np.exp(-(T - 29.3) / 0.4))
sa, lag, h = 0.95, 30, 10.0
p0 = pf(29.0)
fert0 = 1 - np.exp(-h * (1 - p0) / p0)
c = (1 - sa) / (p0 * fert0)                      # recruits per adult female per year (stationary)

def run(rate, shade=False):
    T = 29.0 + rate * np.clip(years - 1990, 0, None) + noise
    p = pf(T)
    if shade:
        p = np.where(years >= 2030, 0.5 * p + 0.5 * pf(T - 1.5), p)
    F = np.ones(years.size)
    M = np.ones(years.size) * (1 - p0) / p0
    births = np.zeros(years.size)
    for i in range(years.size - 1):
        fert = 1 - np.exp(-h * M[i] / F[i])
        births[i] = c * F[i] * fert
        j = i - lag
        rf = births[j] * p[j] if j >= 0 else c * fert0 * p0
        rm = births[j] * (1 - p[j]) if j >= 0 else c * fert0 * (1 - p0)
        F[i + 1] = sa * F[i] + rf
        M[i + 1] = sa * M[i] + rm
    return p, F, M

fig, (a, b, d) = plt.subplots(1, 3, figsize=(13.4, 4.2))
scen = [(0.01, False, "dna", "-", "+0.01 °C per year"), (0.025, False, "highlight", "-", "+0.025 °C per year"),
        (0.045, False, "negative", "-", "+0.045 °C per year"), (0.025, True, "plant", "--", "+0.025, half the nests shaded")]
for rate, shade, tok, ls, lab in scen:
    p, F, M = run(rate, shade)
    col = P.edge(tok) if tok == "highlight" else P.fill(tok)
    k = np.ones(9) / 9
    a.plot(years[4:-4], np.convolve(p, k, "valid") * 100, color=col, lw=1.8, ls=ls, label=lab)
    b.plot(years, M / (M + F) * 100, color=col, lw=1.8, ls=ls)
    d.plot(years, F + M, color=col, lw=1.8, ls=ls)
for ax in (a, b, d):
    ax.set_xlim(1990, 2200)
    ax.set_xlabel("Year")
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
a.set_ylabel("Female hatchlings / % (9-year mean)")
a.set_ylim(0, 102)
a.legend(frameon=False, fontsize=7.5, loc="lower right")
a.set_title("A  Hatchling sex ratio", loc="left", fontweight="bold")
b.set_ylabel("Males among adults / %")
b.set_ylim(0, 80)
b.set_title("B  Adult sex ratio", loc="left", fontweight="bold")
d.set_ylabel("Adults (females in 1990 = 1)")
d.set_yscale("log")
d.set_ylim(0.05, 20)
d.set_title("C  Population size", loc="left", fontweight="bold")
fig.tight_layout()
