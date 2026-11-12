# Temperature and development (illustrative parameters).
# A: development rate vs temperature: linear degree-day model (C = 10 C, K = 250 degree-days, Example 29.6.1)
#    and a Briere model v = a T (T - TL) sqrt(TH - T) (TL = 8 C, TH = 36 C, a fitted to the linear model at 20-25 C).
# B: cumulative degree-days above 10 C through the year, single-sine method from approximate monthly climate
#    normals (Beijing, Guangzhou; diurnal range 9 C), with multiples of a 500 degree-day generation.
import numpy as np
import wikibio as bio
from wikibio import quant

P = bio.P
fig, ax = bio.canvas(25, 11)

C, K = 10.0, 250.0
TL, TH = 8.0, 36.0
T = np.linspace(0, 40, 801)
lin = np.clip((T - C) / K, 0, None)


def briere(t, a):
    t = np.asarray(t, float)
    out = np.zeros_like(t)
    m = (t > TL) & (t < TH)
    out[m] = a * t[m] * (t[m] - TL) * np.sqrt(TH - t[m])
    return out


ref = np.array([20.0, 25.0])
a = np.sum((ref - C) / K) / np.sum(briere(ref, 1.0))
pA = quant.Plot(ax, (2.2, 1.7, 8.6, 7.6), xlim=(0, 40), ylim=(0, 0.12), xlabel="Temperature / °C",
                ylabel="Development rate / d⁻¹", xticks=[0, 10, 20, 30, 40], yticks=[0, 0.04, 0.08, 0.12],
                ylabel_offset=1.0)
pA.line(T, lin, "neutral", dashed=True, lw=1.4, )
pA.text(25, 0.1, "linear: K = 250 °C d", token="neutral", ha="right")
pA.line(T, briere(T, a), "enzyme", lw=1.6, text="Brière", at=0.76, dx=0.3, dy=0.3)
pA.points([15, 20, 25, 30], [0.02, 0.04, 0.06, 0.08], "neutral", r=0.1)
pA.vline(C, token="muted", text="C = 10 °C")
bio.label(ax, (6.5, 10.3), "A  Rate–temperature models", size="small", bold=True)

# B: single-sine degree-days per day from interpolated monthly means
mid = np.cumsum([31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]) - np.array([31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]) / 2
normals = {
    "Beijing (40°N)": [-3.1, 0.3, 6.7, 14.8, 20.8, 24.9, 26.7, 25.5, 20.8, 13.7, 5.0, -0.9],
    "Guangzhou (23°N)": [13.6, 14.7, 17.8, 22.0, 25.6, 27.6, 28.8, 28.7, 27.5, 24.8, 20.0, 15.3],
}
days = np.arange(365) + 0.5
phase = np.linspace(0, 2 * np.pi, 97)[:-1]
pB = quant.Plot(ax, (14.2, 1.7, 9.6, 7.6), xlim=(0, 365), ylim=(0, 4800), xlabel="Day of year",
                ylabel="Cumulative degree-days > 10 °C", xticks=[0, 91, 182, 273, 365],
                yticks=[0, 1000, 2000, 3000, 4000], ylabel_offset=1.2)
for k in range(1, 10):
    pB.hline(500 * k, token="muted", dashed=True, lw=0.5)
pB.text(8, 4680, "dashed: multiples of 500 °C d (one generation)", ha="left")
for (name, m), tok in zip(normals.items(), ("channel", "negative")):
    mm = np.array(m)
    tmean = np.interp(days, np.concatenate([mid - 365, mid, mid + 365]), np.concatenate([mm, mm, mm]))
    dd = np.array([np.mean(np.clip(t + 4.5 * np.sin(phase) - C, 0, None)) for t in tmean])
    cum = np.cumsum(dd)
    pB.line(days, cum, tok, lw=1.6)
    yl = 4150 if tok == "negative" else 1650
    pB.text(250 if tok == "negative" else 280, yl, "%s:\n%d °C d, %.1f gen." % (name, cum[-1], cum[-1] / 500),
            token=tok, ha="right" if tok == "negative" else "left")
bio.label(ax, (19.0, 10.3), "B  Degree-days through the year", size="small", bold=True)
