# Initiation of bacterial transcription.
# A: four stages drawn schematically: the closed complex (RPc, duplex DNA), the open complex (RPo, about 13 bp
# melted), the initially transcribing complex in which downstream DNA is scrunched into the enzyme while the
# upstream promoter contacts (sigma, dark patch) are kept, and the elongation complex after promoter escape.
# A curved arrow from the scrunched state back to RPo marks abortive release of a short RNA.
# B: the tau plot of the two-step model R + P <=> RPc -> RPo (K_c, k2):
#     tau = 1/k2 + (K_c/k2) / [R],
# for two hypothetical promoters: 1 binds tightly but isomerizes slowly (K_c = 10 nM, k2 = 0.01 /s),
# 2 binds weakly but isomerizes fast (K_c = 1 uM, k2 = 0.1 /s). The intercept is 1/k2 and the slope K_c/k2.
import numpy as np
import wikibio as bio
from wikibio import charts as C
from wikibio import molbio as MB

P = bio.P
fig, ax = bio.canvas(21.0, 9.4)


def state(cx, cy, b0, b1, scrunch=0.0, rna=0.0, sigma=True, title="", body_dx=0.0):
    """One complex: duplex from cx-2 to cx+2, bubble [b0, b1] (relative), optional scrunched bulges."""
    half = 0.13
    xs = np.linspace(cx - 2.1, cx + 2.1, 400)
    hb = 0.32
    up = MB.bubble_profile(xs, cx + b0, cx + b1, hb, ramp=0.25) if b1 > b0 else 0 * xs
    dn = MB.bubble_profile(xs, cx + b0, cx + b1, hb * 0.8, ramp=0.25) if b1 > b0 else 0 * xs
    # polymerase body
    body = bio.core.blob((cx + body_dx, cy + 0.15), 1.55, 0.95, wobble=0.05, seed=3, k=9)
    bio.shape(ax, body, token="enzyme", zorder=3, alpha=0.75)
    if sigma:
        sg = bio.core.blob((cx - 0.95, cy + 0.62), 0.55, 0.32, wobble=0.06, seed=5, k=7)
        bio.shape(ax, sg, token="protein", zorder=4)
        bio.label(ax, (cx - 0.95, cy + 0.62), "σ", size="small", color=P.on_fill(), zorder=6)
    top = MB.track(xs, cy + half + up)
    bot = MB.track(xs, cy - half - dn)
    MB.backbone(ax, top, "dna", lw=1.8, zorder=8)
    MB.backbone(ax, bot, "dna2", lw=1.8, zorder=8)
    # base-pair rungs where closed
    for x in np.arange(cx - 2.0, cx + 2.05, 0.16):
        if b1 > b0 and cx + b0 - 0.05 <= x <= cx + b1 + 0.05:
            continue
        ax.plot([x, x], [cy - half, cy + half], color=P.muted(), lw=0.6, zorder=7)
    if scrunch:
        # scrunched single strands: bulges inside the enzyme
        t = np.linspace(0, 1, 80)
        x0 = cx + b0 + 0.25
        bx = x0 + 0.55 * t
        ax.plot(bx, cy + half + hb + scrunch * np.sin(np.pi * t), color=P.edge("dna"), lw=1.6, zorder=8)
        ax.plot(bx, cy - half - 0.8 * hb - scrunch * np.sin(np.pi * t), color=P.edge("dna2"), lw=1.6, zorder=8)
    if rna:
        x1 = cx + b1 - 0.15
        r = np.c_[np.linspace(x1 - rna, x1, 50), np.full(50, cy - half - 0.8 * hb + 0.12)]
        if rna > 0.9:  # longer RNA leaves through the exit channel
            tail = np.c_[np.linspace(x1 - rna - 0.55, x1 - rna, 30), cy - half - 0.8 * hb + 0.12 - np.linspace(1.05, 0, 30) ** 1.0]
            r = np.vstack([tail, r])
        MB.backbone(ax, r, "rna", lw=2.0, zorder=9)
    bio.label(ax, (cx, cy + 1.45), title, size="small", bold=True)


y = 6.7
bio.panel(ax, "A", (0.1, 9.25))
state(2.6, y, 0, 0, title="Closed (RPc)")
state(7.7, y, -0.45, 0.6, title="Open (RPo)")
state(12.8, y, -0.45, 1.25, scrunch=0.32, rna=0.7, title="Scrunched ITC")
state(18.1, y, -0.2, 0.65, rna=1.3, sigma=False, title="Elongation (EC)", body_dx=0.2)
for a, b in [((4.75, y), (5.55, y)), ((9.85, y), (10.65, y)), ((14.95, y), (15.85, y))]:
    bio.arrow(ax, a, b, kind="process")
bio.label(ax, (5.15, y - 0.4), "isomerization", size="tiny", color=P.muted())
bio.label(ax, (10.25, y - 0.4), "+ NTPs", size="tiny", color=P.muted())
bio.label(ax, (15.4, y - 0.4), "escape", size="tiny", color=P.muted())
# abortive release: curved arrow back from ITC to RPo
bio.arrow(ax, (12.6, y - 1.05), (8.1, y - 1.05), kind="process", bend=-0.25)
bio.label(ax, (10.35, y - 1.75), "abortive release of 2–10 nt RNA (unscrunching)", size="tiny")
# sigma left behind
sg = bio.core.blob((16.6, y + 0.95), 0.45, 0.26, wobble=0.06, seed=5, k=7)
bio.shape(ax, sg, token="protein", zorder=4, alpha=0.6)
bio.label(ax, (16.6, y + 0.95), "σ", size="tiny", color=P.on_fill(), zorder=6)

# --- B: tau plot ------------------------------------------------------------------------------------------
bio.panel(ax, "B", (0.1, 4.1))
b = C.axes_at(ax, (2.2, 0.9, 7.2, 3.0))
inv = np.linspace(0, 0.12, 200)  # 1/[R] in 1/nM
for (Kc, k2, tok, name) in [(10.0, 0.01, "enzyme", r"promoter 1: $K_{\mathrm{c}}$ = 10 nM, $k_2$ = 0.01 s$^{-1}$"),
                            (1000.0, 0.1, "negative", r"promoter 2: $K_{\mathrm{c}}$ = 1 µM, $k_2$ = 0.1 s$^{-1}$")]:
    b.plot(inv, 1 / k2 + Kc / k2 * inv, color=C.line(tok), lw=1.8, label=name)
b.set_xlim(0, 0.12)
b.set_ylim(0, 1300)
C.style_axes(b, r"1/[R] / nM$^{-1}$", "τ / s")
b.legend(fontsize=bio.core.FONT["tiny"], frameon=False, labelcolor=P.ink(), loc="upper left")
b.annotate(r"intercept $1/k_2$", xy=(0.0, 100), xytext=(0.03, 400), fontsize=bio.core.FONT["tiny"], color=P.ink(),
           arrowprops=dict(arrowstyle="-", color=P.muted(), lw=0.7))
# the same promoters as functions of [R]
c = C.axes_at(ax, (12.6, 0.9, 7.2, 3.0))
R = np.logspace(0, 4, 300)  # nM
for (Kc, k2, tok) in [(10.0, 0.01, "enzyme"), (1000.0, 0.1, "negative")]:
    c.semilogx(R, k2 * R / (Kc + R), color=C.line(tok), lw=1.8)
c.set_xlim(1, 1e4)
c.set_ylim(0, 0.105)
C.style_axes(c, "[R] / nM", r"$k_{\mathrm{obs}}$ / s$^{-1}$")
c.text(1.5, 0.088, "promoter 2", fontsize=bio.core.FONT["tiny"], color=C.line("negative"))
c.text(1.5, 0.018, "promoter 1", fontsize=bio.core.FONT["tiny"], color=C.line("enzyme"))
