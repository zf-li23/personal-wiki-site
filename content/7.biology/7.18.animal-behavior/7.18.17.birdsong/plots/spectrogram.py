"""A synthetic song in the style of a white-crowned sparrow, shown as an oscillogram and a spectrogram, in two
'dialects' that share the introductory whistle and buzz but end in different trills. The sound is synthesized
(sum of frequency-modulated tones and a noisy buzz) and analyzed with a short-time Fourier transform, exactly
as a recording would be."""
import numpy as np
from matplotlib.colors import LinearSegmentedColormap
from scipy.signal import spectrogram

import wikibio as bio
from wikibio import quant

P = bio.P
fs = 22050


def tone(f0, f1, dur, amp=1.0, shape="lin"):
    t = np.arange(int(dur * fs)) / fs
    if shape == "lin":
        f = f0 + (f1 - f0) * t / dur
    else:  # concave down-sweep
        f = f1 + (f0 - f1) * np.exp(-4 * t / dur)
    ph = 2 * np.pi * np.cumsum(f) / fs
    env = np.sin(np.pi * t / dur) ** 0.6
    return amp * env * np.sin(ph)


def gap(d):
    return np.zeros(int(d * fs))


def buzz(fc, bw, dur, rng):
    n = int(dur * fs)
    t = np.arange(n) / fs
    carrier = np.sin(2 * np.pi * np.cumsum(fc + bw * np.sin(2 * np.pi * 110 * t)) / fs)
    return 0.6 * np.sin(np.pi * t / dur) ** 0.5 * carrier * (1 + 0.04 * rng.standard_normal(n))


def song(trill, rng):
    parts = [tone(3500, 3600, 0.45), gap(0.05), tone(4600, 4500, 0.18, 0.8), gap(0.04),
             buzz(4200, 600, 0.30, rng), gap(0.05)]
    if trill == "A":
        for _ in range(7):   # fast trill of short down-sweeps
            parts += [tone(5600, 3200, 0.045, 0.8), gap(0.03)]
    else:
        for _ in range(4):   # slower trill of two-part syllables
            parts += [tone(3000, 4400, 0.06, 0.8), gap(0.012), tone(5200, 4600, 0.05, 0.7), gap(0.05)]
    return np.concatenate(parts + [gap(0.08)])


rng = np.random.default_rng(0)
cmap = LinearSegmentedColormap.from_list("spec", [P.surface(), P.mix(P.ink(), P.surface(), 0.4), P.ink()])
fig, ax = bio.canvas(24, 11.4)
for k, (trill, title) in enumerate([("A", "Dialect A"), ("B", "Dialect B")]):
    x0 = 1.8 + k * 11.6
    s = song(trill, rng)
    t = np.arange(len(s)) / fs
    bio.panel(ax, "AB"[k], (x0 - 1.4, 11.1))
    bio.label(ax, (x0 + 4.6, 10.9), title, size="small", bold=True)
    # oscillogram
    p = quant.Plot(ax, (x0, 8.0, 9.4, 2.2), xlim=(0, 1.7), ylim=(-1.3, 1.3), ylabel="Amplitude", xticks=None, yticks=None)
    step = 6
    m = t <= 1.7
    p.line(t[m][::step], s[m][::step], "dna", lw=0.4)
    # spectrogram
    f, tt, S = spectrogram(s, fs=fs, nperseg=256, noverlap=224)
    keep = f <= 8000
    D = 10 * np.log10(S[keep] + 1e-10)
    D = np.clip(D - D.max(), -45, 0)
    q = quant.Plot(ax, (x0, 1.6, 9.4, 5.6), xlim=(0, 1.7), ylim=(0, 8), xlabel="Time / s", ylabel="Frequency / kHz",
                   xticks=[0, 0.4, 0.8, 1.2, 1.6], yticks=[0, 2, 4, 6, 8])
    X0, Y0 = q.xy(tt[0], 0)
    X1, Y1 = q.xy(tt[-1], 8)
    ax.imshow(D, origin="lower", aspect="auto", cmap=cmap, extent=(X0, X1, Y0, Y1), zorder=4, interpolation="bilinear")
    for (a, b, name) in [(0, 0.45, "whistle"), (0.5, 0.68, "note"), (0.72, 1.02, "buzz"), (1.07, 1.52 if trill == "A" else 1.69, "trill")]:
        xa, _ = q.xy(a, 0); xb, _ = q.xy(b, 0)
        yb = q.Y(7.4)
        ax.plot([xa, xb], [yb, yb], color=P.edge("rna"), lw=1.2, zorder=6)
        bio.label(ax, ((xa + xb) / 2, yb + 0.3), name, size="tiny", color=P.edge("rna"))
ax.set_ylim(0.2, 11.4)
