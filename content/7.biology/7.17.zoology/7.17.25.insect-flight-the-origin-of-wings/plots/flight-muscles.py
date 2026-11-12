# Wing movement by direct and indirect flight muscles, schematic transverse sections of a wing-bearing
# segment (left half mirrored). The wing is a lever resting on the pleural wing process (fulcrum, dot);
# its inner end is attached to the tergum. Top row, indirect muscles (most Neoptera): contraction of the
# dorsoventral muscles pulls the tergum down, so the wings rise (upstroke); contraction of the dorsal
# longitudinal muscles (cut across, circles) shortens the segment and bows the tergum up, so the wings
# fall (downstroke). Bottom row, direct downstroke (dragonflies): the basalar muscle pulls on the wing
# base outside the fulcrum (downstroke), the dorsoventral muscles lower the tergum (upstroke).
import numpy as np
import wikibio as bio

P = bio.P
fig, ax = bio.canvas(24, 15)


def section(x0, y0, tergum_y, title, active):
    fx = 2.3
    for s in (-1, 1):
        cx = x0 + s * fx
        ax.plot([cx, cx], [y0, y0 + 2.6], color=P.edge("positive"), lw=3, zorder=4)
        ax.add_patch(__import__("matplotlib").patches.Circle((cx, y0 + 2.75), 0.12, color=P.ink(), zorder=8))
        inner = np.array([x0 + s * 1.7, y0 + tergum_y])
        pivot = np.array([cx, y0 + 2.75])
        u = (pivot - inner) / np.linalg.norm(pivot - inner)
        tip = pivot + u * 3.4
        ax.plot([inner[0], tip[0]], [inner[1], tip[1]], color=P.edge("er"), lw=3, zorder=6, solid_capstyle="round")
    ax.plot([x0 - 1.7, x0 + 1.7], [y0 + tergum_y, y0 + tergum_y], color=P.edge("channel"), lw=4, zorder=6)
    ax.plot([x0 - fx, x0 + fx], [y0, y0], color=P.edge("neutral"), lw=3, zorder=4)
    for name, pts, tok in active:
        if name == "dlm":
            for s in (-0.6, 0.6):
                ax.add_patch(__import__("matplotlib").patches.Circle((x0 + s, y0 + tergum_y - 0.55), 0.42,
                             facecolor=P.fill(tok), edgecolor=P.edge(tok), lw=0.8, zorder=5))
        else:
            for s in (-1, 1):
                a, b = pts(s)
                ax.plot([a[0], b[0]], [a[1], b[1]], color=P.fill(tok), lw=7, zorder=3, solid_capstyle="round")
    bio.label(ax, (x0, y0 + 4.9), title, size="small", bold=True)


def dvm(x0, y0, ty, on):
    return ("dvm", lambda s: ((x0 + s * 1.2, y0 + ty - 0.1), (x0 + s * 1.2, y0 + 0.1)), "muscle" if on else "neutral")


def bas(x0, y0, on):
    return ("bas", lambda s: ((x0 + s * 2.65, y0 + 2.9), (x0 + s * 2.0, y0 + 0.2)), "muscle" if on else "neutral")


rows = [(9.0, "Indirect flight muscles"), (1.6, "Direct downstroke muscles (Odonata)")]
y = 9.0
section(5.5, y, 2.2, "Upstroke: dorsoventral muscles contract", [dvm(5.5, y, 2.2, True), ("dlm", None, "neutral")])
section(17.5, y, 3.2, "Downstroke: dorsal longitudinal muscles contract", [dvm(17.5, y, 3.2, False), ("dlm", None, "muscle")])
y = 1.6
section(5.5, y, 2.2, "Upstroke: dorsoventral muscles contract", [dvm(5.5, y, 2.2, True), bas(5.5, y, False)])
section(17.5, y, 3.2, "Downstroke: basalar muscles contract", [dvm(17.5, y, 3.2, False), bas(17.5, y, True)])
bio.label(ax, (12.0, 14.7), "Indirect flight muscles (flies, bees, beetles, most Neoptera)", size="normal", bold=True)
bio.label(ax, (12.0, 7.3), "Direct flight muscles (dragonflies)", size="normal", bold=True)
bio.label(ax, (12.0, 0.4), "red: contracting muscle; grey: relaxed; dot: pleural wing process (fulcrum)", size="tiny", color=P.muted())
