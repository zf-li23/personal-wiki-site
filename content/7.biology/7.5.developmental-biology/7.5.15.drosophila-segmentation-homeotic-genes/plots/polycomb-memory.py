# Initiation by gap repressors, maintenance by Polycomb: the read-write model of Dodd and colleagues (7.2.15) with a
# transient instruction. A region of N = 60 nucleosomes, each modified for silencing (M), unmodified (U) or modified
# for activity (A); in each step a nucleosome is converted either by recruitment (probability F / (1 + F), towards the
# state of a randomly chosen nucleosome) or by noise, and every 100 sweeps a cell division replaces half of the
# nucleosomes by U. During the first 300 sweeps (shaded) a transcription factor biases the noisy conversions towards
# M (a cell with a gap repressor) or towards A (a cell with an activator); afterwards the bias is removed.
# A: strong feedback (F = 4): both cells remember their initial instruction for many divisions. B: weak feedback
# (F = 1): the instruction is forgotten within a few divisions.
import numpy as np
import wikibio as bio
from wikibio import charts as C

P = bio.P
N, DIV, T, TI = 60, 100, 1500, 300


def run(F, bias, seed):
    rng = np.random.default_rng(seed)
    alpha = F / (1 + F)
    s = np.ones(N, int)
    m, a = [], []
    picks = rng.integers(0, N, size=(T, N, 2))
    us = rng.random((T, N, 3))
    for t in range(T):
        if t % DIV == 0 and t > 0:
            s[rng.random(N) < 0.5] = 1
        for k in range(N):
            i, j = picks[t, k]
            if us[t, k, 0] < alpha:
                if s[j] == 0 and s[i] > 0:
                    s[i] -= 1
                elif s[j] == 2 and s[i] < 2:
                    s[i] += 1
            else:
                p_down = 0.5
                if t < TI:
                    p_down = 0.85 if bias == "M" else 0.15
                if s[i] == 1:
                    s[i] = 0 if us[t, k, 1] < p_down else 2
                elif s[i] == 0 and us[t, k, 2] < (0.3 if (t < TI and bias == "M") else 1.0):
                    s[i] = 1
                elif s[i] == 2 and us[t, k, 2] < (0.3 if (t < TI and bias == "A") else 1.0):
                    s[i] = 1
        m.append(np.mean(s == 0)); a.append(np.mean(s == 2))
    return np.array(m), np.array(a)


fig, ax = bio.canvas(22.0, 10.0)
for k, (F, letter) in enumerate([(4.0, "A"), (1.0, "B")]):
    y = 5.6 - 4.4 * k
    pa = C.axes_at(ax, (1.6, y, 19.4, 3.1))
    pa.axvspan(0, TI, color=P.fill("highlight"), alpha=0.25, lw=0)
    for bias, tok, lab in [("M", "chromatin", "cell with repressor (e.g. Hb at the Ubx locus)"), ("A", "positive", "cell with activator")]:
        m, a = run(F, bias, 3 + k)
        pa.plot(np.arange(T), m - a, color=C.line(tok), lw=0.9, label=lab)
    for d in range(DIV, T, DIV):
        pa.plot([d, d], [1.08, 1.16], color=P.muted(), lw=0.6, clip_on=False)
    pa.set_xlim(0, T)
    pa.set_ylim(-1.05, 1.05)
    pa.set_yticks([-1, 0, 1])
    C.style_axes(pa, "time / sweeps (one division every 100 sweeps)" if k == 1 else None, "M − A")
    if k == 0:
        lg = pa.legend(fontsize=bio.core.FONT["tiny"], frameon=True, labelcolor=P.ink(), loc="center right")
        lg.get_frame().set_facecolor(P.surface()); lg.get_frame().set_edgecolor(P.muted()); lg.get_frame().set_linewidth(0.5)
    pa.text(TI / 2, 0, "instruction", fontsize=bio.core.FONT["tiny"], color=P.muted(), ha="center", va="center")
    bio.panel(ax, letter, (0.2, y + 3.95))
    bio.label(ax, (0.8, y + 3.6), f"F = {F:g}" + ("  (strong feedback: memory)" if F > 2 else "  (weak feedback: no memory)"),
              size="normal", bold=True, ha="left")
