"""Render one plot script into light- and dark-themed images (lossless WebP).

Usage:  python render_plot.py <script.py> <out_dir>

Contract (enforced here and by the Node pipeline in scripts/wiki/plots.ts):
  * The script builds figures with matplotlib and leaves them open. Every open
    figure is saved, in creation order, as <out_dir>/<i>-light.webp and <i>-dark.webp
    (lossless WebP: the same pixels as PNG at well under half the size).
  * The script must not call savefig() or matplotlib.use(); plt.show() is a no-op.
  * The script runs twice (once per theme) in a fresh namespace, with the working
    directory set to its own folder and numpy/random seeded with 0.
  * On success <out_dir>/meta.json is written: {"figures": [{"width": px, "height": px}, ...]}
    with the light image's pixel size. On failure the process exits non-zero and the
    traceback goes to stderr.
"""

import json
import os
import random
import runpy
import sys
import traceback

os.environ["MPLBACKEND"] = "Agg"

import matplotlib  # noqa: E402

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
from matplotlib.colors import to_rgba  # noqa: E402
from matplotlib.figure import Figure  # noqa: E402

DPI = 200
# Keep in sync with the CSS tokens in src/styles/index.css (--card in light/dark).
THEMES = {
    "light": {
        "figure.facecolor": "#ffffff",
        "axes.facecolor": "#ffffff",
        "savefig.facecolor": "#ffffff",
    },
    "dark": {
        "figure.facecolor": "#0f172a",
        "axes.facecolor": "#0f172a",
        "savefig.facecolor": "#0f172a",
        "text.color": "#e2e8f0",
        "axes.labelcolor": "#e2e8f0",
        "axes.edgecolor": "#94a3b8",
        "xtick.color": "#cbd5e1",
        "ytick.color": "#cbd5e1",
        "grid.color": "#334155",
        "legend.facecolor": "#0f172a",
        "legend.edgecolor": "#475569",
        "patch.edgecolor": "#e2e8f0",
        "boxplot.boxprops.color": "#e2e8f0",
        "boxplot.whiskerprops.color": "#e2e8f0",
        "boxplot.capprops.color": "#e2e8f0",
        "boxplot.medianprops.color": "#fb923c",
        "boxplot.flierprops.markeredgecolor": "#e2e8f0",
        "hatch.color": "#e2e8f0",
    },
}
DARK_INK = (0.886, 0.910, 0.941)  # replaces explicit near-black ink in dark mode
DARK_SURFACE = (0.059, 0.090, 0.165)  # replaces explicit near-white fills in dark mode

_real_savefig = Figure.savefig


def _forbidden_savefig(*_args, **_kwargs):
    raise RuntimeError("plot scripts must not call savefig(); every open figure is saved automatically")


def _swap(rgba, ink: bool):
    r, g, b, a = rgba
    # Only (near) pure black counts as ink; the dark theme surface (#0f172a) must stay untouched.
    if max(r, g, b) < 0.1:
        return (*DARK_INK, a)
    if not ink and r > 0.95 and g > 0.95 and b > 0.95:
        return (*DARK_SURFACE, a)
    return None


def _recolor(artist, getter, setter, ink):
    get = getattr(artist, getter, None)
    put = getattr(artist, setter, None)
    if get is None or put is None:
        return
    try:
        value = get()
    except Exception:
        return
    if value is None or (isinstance(value, str) and value in ("none", "None", "auto")):
        return
    try:
        if hasattr(value, "ndim") and getattr(value, "ndim", 0) == 2:
            rows = [_swap(tuple(row), ink) or tuple(row) for row in value]
            if any(_swap(tuple(row), ink) for row in value):
                put(rows)
            return
        new = _swap(to_rgba(value), ink)
        if new is not None:
            put(new)
    except (ValueError, TypeError):
        return


def adapt_for_dark(fig):
    """Make explicitly black ink readable and explicitly white fills dark, without touching images."""
    from matplotlib.axes import Axes
    from matplotlib.collections import QuadMesh
    from matplotlib.image import AxesImage

    # Figure/Axes backgrounds come from the theme; images and meshes carry data colours.
    skip = {id(fig.patch)} | {id(ax.patch) for ax in fig.axes}
    for artist in fig.findobj():
        if id(artist) in skip or isinstance(artist, (Figure, Axes, AxesImage, QuadMesh)):
            continue
        _recolor(artist, "get_color", "set_color", ink=True)
        _recolor(artist, "get_markeredgecolor", "set_markeredgecolor", ink=True)
        _recolor(artist, "get_markerfacecolor", "set_markerfacecolor", ink=False)
        _recolor(artist, "get_edgecolor", "set_edgecolor", ink=True)
        if not hasattr(artist, "get_array") or artist.get_array() is None:
            _recolor(artist, "get_facecolor", "set_facecolor", ink=False)


def image_size(path):
    from PIL import Image

    with Image.open(path) as im:
        return im.size


def render(script, out_dir, theme):
    plt.close("all")
    matplotlib.rcdefaults()
    random.seed(0)
    try:
        import numpy as np

        np.random.seed(0)
    except ImportError:
        pass
    sizes = []
    with matplotlib.rc_context(THEMES[theme]):
        runpy.run_path(script, run_name="__main__")
        numbers = plt.get_fignums()
        if not numbers:
            raise RuntimeError("the script left no open matplotlib figure")
        for i, num in enumerate(numbers):
            fig = plt.figure(num)
            if theme == "dark":
                adapt_for_dark(fig)
            out = os.path.join(out_dir, f"{i}-{theme}.webp")
            _real_savefig(fig, out, format="webp", dpi=DPI, bbox_inches="tight", pad_inches=0.08,
                          facecolor=THEMES[theme]["figure.facecolor"],
                          pil_kwargs={"lossless": True, "method": 4})
            w, h = image_size(out)
            sizes.append({"width": w, "height": h})
    plt.close("all")
    return sizes


def main():
    script, out_dir = os.path.abspath(sys.argv[1]), os.path.abspath(sys.argv[2])
    os.makedirs(out_dir, exist_ok=True)
    os.chdir(os.path.dirname(script))
    sys.path.insert(0, os.path.dirname(script))
    # Shared helpers next to this file (wikichem: chemical structures and mechanisms).
    sys.path.insert(1, os.path.dirname(os.path.abspath(__file__)))
    plt.show = lambda *a, **k: None
    plt.savefig = _forbidden_savefig
    Figure.savefig = _forbidden_savefig
    matplotlib.use = lambda *a, **k: None
    try:
        light = render(script, out_dir, "light")
        dark = render(script, out_dir, "dark")
        if len(light) != len(dark):
            raise RuntimeError(f"light and dark runs produced different figure counts ({len(light)} vs {len(dark)})")
    except Exception:
        traceback.print_exc()
        sys.exit(1)
    with open(os.path.join(out_dir, "meta.json"), "w") as f:
        json.dump({"figures": light}, f)


if __name__ == "__main__":
    main()
