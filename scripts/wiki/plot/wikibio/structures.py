"""Common cellular structures drawn natively: ribosome, cytoskeleton, antibody, virus, neuron, synapse.

    ribosome(ax, (x, y))                        large + small subunit
    actin(ax, a, b) / microtubule(ax, a, b)     filaments between two points
    antibody(ax, (x, y), angle=0)               IgG "Y" with heavy and light chains
    virus(ax, (x, y), r, kind="icosahedral")    icosahedral capsid with spikes, or "enveloped"
    neuron(ax, soma, axon_end, ...)             soma, dendrites, myelinated axon, terminals
    synapse(ax, (x, y), ...)                    presynaptic bouton, vesicles, cleft, receptors
"""

import math

import numpy as np
from matplotlib.patches import Circle, Ellipse, FancyBboxPatch, PathPatch, Polygon
from matplotlib.path import Path

from . import palette as P
from .core import LINE, blob, label, smooth_closed


def ribosome(ax, center, size=0.5, token="rrna", zorder=12):
    """A ribosome: large subunit above, small subunit below (size = width of the large subunit)."""
    x, y = center
    big = blob((x, y + size * 0.18), size / 2, size * 0.32, wobble=0.05, seed=11, k=7)
    small = blob((x, y - size * 0.25), size * 0.42, size * 0.18, wobble=0.05, seed=12, k=7)
    for o, tone in ((small, P.light(token)), (big, P.fill(token))):
        ax.add_patch(PathPatch(Path(o, closed=True), facecolor=tone, edgecolor=P.edge(token), lw=LINE * 0.8, zorder=zorder))


def actin(ax, a, b, r=0.05, token="muscle", zorder=9):
    """An actin microfilament: two intertwined strands of globular subunits."""
    a, b = np.asarray(a, float), np.asarray(b, float)
    L = np.linalg.norm(b - a)
    u = (b - a) / L
    n = np.array([-u[1], u[0]])
    k = int(L / (r * 1.8))
    for strand in (0, 1):
        for i in range(k):
            t = (i + 0.5 * strand) * r * 1.8
            off = math.sin(t / (r * 6) * math.pi + strand * math.pi) * r * 0.9
            c = a + u * t + n * off
            ax.add_patch(Circle(c, r, facecolor=P.fill(token) if strand else P.light(token), edgecolor=P.edge(token), lw=0.5, zorder=zorder + strand))


def microtubule(ax, a, b, width=0.25, token="channel", zorder=9):
    """A microtubule: a hollow tube of protofilaments (drawn as a striped band of tubulin dimers)."""
    a, b = np.asarray(a, float), np.asarray(b, float)
    L = np.linalg.norm(b - a)
    u = (b - a) / L
    n = np.array([-u[1], u[0]])
    seg = width * 0.5
    for i in range(int(L / seg)):
        for j, s in enumerate((-0.25, 0.25)):
            c = a + u * (i + 0.5) * seg + n * s * width
            tok = P.fill(token) if (i + j) % 2 else P.light(token)
            ax.add_patch(FancyBboxPatch(tuple(c - u * seg * 0.45 - n * width * 0.22), seg * 0.9, width * 0.44,
                                        boxstyle="round,pad=0,rounding_size=0.03", facecolor=tok, edgecolor=P.edge(token), lw=0.4,
                                        zorder=zorder, transform=ax.transData))


def antibody(ax, center, size=1.0, angle=0.0, token="antibody", light_token="protein", zorder=12):
    """An IgG antibody: two heavy chains (stem and arms) and two light chains (outer arms)."""
    x, y = center
    th = math.radians(angle)
    R = np.array([[math.cos(th), math.sin(th)], [-math.sin(th), math.cos(th)]])

    def seg(p, q, w, tok):
        p, q = np.asarray(p) @ R * size + center, np.asarray(q) @ R * size + center
        d = (q - p) / np.linalg.norm(q - p)
        nn = np.array([-d[1], d[0]]) * w * size / 2
        ax.add_patch(Polygon([p + nn, q + nn, q - nn, p - nn], closed=True, facecolor=P.fill(tok), edgecolor=P.edge(tok),
                             lw=LINE * 0.7, joinstyle="round", zorder=zorder))
        for end in (p, q):
            ax.add_patch(Circle(end, w * size / 2, facecolor=P.fill(tok), edgecolor="none", zorder=zorder))

    for side in (-1, 1):
        seg((side * 0.07, -0.55), (side * 0.07, -0.02), 0.13, token)          # Fc stem
        seg((side * 0.07, -0.02), (side * 0.38, 0.42), 0.13, token)           # heavy-chain arm
        seg((side * 0.26, 0.05), (side * 0.56, 0.48), 0.11, light_token)      # light chain
    ax.plot(*(np.array([[-0.05, -0.1], [0.05, -0.1]]) @ R * size + center).T, color=P.edge(token), lw=LINE * 0.6, zorder=zorder + 1)


def virus(ax, center, r=0.6, kind="icosahedral", token="virus", spikes=12, zorder=12):
    """A virus particle: an icosahedral capsid (hexagon outline with facets) or an enveloped virion with spikes."""
    x, y = center
    if kind == "icosahedral":
        hexv = np.array([[x + r * math.cos(math.radians(30 + 60 * i)), y + r * math.sin(math.radians(30 + 60 * i))] for i in range(6)])
        ax.add_patch(Polygon(hexv, closed=True, facecolor=P.fill(token), edgecolor=P.edge(token), lw=LINE, joinstyle="round", zorder=zorder))
        tri = [(hexv[i], hexv[(i + 1) % 6]) for i in range(6)]
        inner = np.array([[x + r * 0.45 * math.cos(math.radians(90 + 120 * i)), y + r * 0.45 * math.sin(math.radians(90 + 120 * i))] for i in range(3)])
        ax.add_patch(Polygon(inner, closed=True, facecolor=P.light(token), edgecolor=P.edge(token), lw=LINE * 0.6, zorder=zorder + 1))
        for i, v in enumerate(hexv):
            ax.plot([v[0], inner[(i // 2) % 3][0]], [v[1], inner[(i // 2) % 3][1]], color=P.edge(token), lw=LINE * 0.5, zorder=zorder + 1)
        return
    if kind == "enveloped":
        for i in range(spikes):
            a = 2 * math.pi * i / spikes
            p, q = (x + r * math.cos(a), y + r * math.sin(a)), (x + r * 1.28 * math.cos(a), y + r * 1.28 * math.sin(a))
            ax.plot([p[0], q[0]], [p[1], q[1]], color=P.edge(token), lw=LINE, zorder=zorder - 1)
            ax.add_patch(Circle(q, r * 0.1, facecolor=P.fill("receptor"), edgecolor=P.edge("receptor"), lw=0.6, zorder=zorder))
        ax.add_patch(Circle(center, r, facecolor=P.fill(token), edgecolor=P.edge(token), lw=LINE * 1.2, zorder=zorder))
        ax.add_patch(Circle(center, r * 0.55, facecolor=P.light(token), edgecolor=P.edge(token), lw=LINE * 0.6, zorder=zorder + 1))
        t = np.linspace(0, 4 * math.pi, 80)
        ax.plot(x + r * 0.32 * np.cos(t) * np.linspace(1, 0.3, 80), y + r * 0.32 * np.sin(t) * np.linspace(1, 0.3, 80),
                color=P.edge("rna"), lw=LINE, zorder=zorder + 2)
        return
    raise ValueError(f"unknown virus kind {kind!r}")


def neuron(ax, soma, axon_end, soma_r=0.45, dendrites=5, myelin=True, terminals=3, token="neuron", seed=4, zorder=10):
    """A neuron: soma with nucleus, branching dendrites, an axon (myelinated with nodes of Ranvier) and terminals."""
    s = np.asarray(soma, float)
    e = np.asarray(axon_end, float)
    rng = np.random.default_rng(seed)
    d = e - s
    L = np.linalg.norm(d)
    u = d / L
    back = -u
    col, edge = P.fill(token), P.edge(token)
    for i in range(dendrites):
        ang = math.atan2(back[1], back[0]) + (i - (dendrites - 1) / 2) * (2.4 / max(1, dendrites - 1))
        _branch(ax, s + soma_r * 0.8 * np.array([math.cos(ang), math.sin(ang)]), ang, soma_r * 2.3, 3, rng, edge, col, zorder)
    ax.add_patch(PathPatch(Path(blob(s, soma_r, soma_r * 0.9, wobble=0.08, seed=seed, k=7), closed=True), facecolor=col, edgecolor=edge, lw=LINE, zorder=zorder + 2))
    ax.add_patch(Circle(s, soma_r * 0.35, facecolor=P.fill("nucleus"), edgecolor=P.edge("nucleus"), lw=LINE * 0.7, zorder=zorder + 3))
    start = s + u * soma_r * 0.9
    stop = e - u * 0.35
    ax.plot([start[0], stop[0]], [start[1], stop[1]], color=edge, lw=LINE * 2.2, solid_capstyle="round", zorder=zorder + 1)
    if myelin:
        seg_len = 0.7
        n_seg = int(np.linalg.norm(stop - start) / (seg_len + 0.12))
        for k in range(n_seg):
            c = start + u * (0.35 + k * (seg_len + 0.12) + seg_len / 2)
            ang = math.degrees(math.atan2(u[1], u[0]))
            ax.add_patch(FancyBboxPatch((-seg_len / 2, -0.13), seg_len, 0.26, boxstyle="round,pad=0,rounding_size=0.12",
                                        facecolor=P.fill("lipid"), edgecolor=P.edge("lipid"), lw=LINE * 0.7, zorder=zorder + 2,
                                        transform=_rot(ax, c, ang)))
    nrm = np.array([-u[1], u[0]])
    for k in range(terminals):
        off = (k - (terminals - 1) / 2) * 0.32
        q = e + nrm * off
        ax.plot([stop[0], q[0]], [stop[1], q[1]], color=edge, lw=LINE * 1.3, zorder=zorder + 1)
        ax.add_patch(Circle(q, 0.12, facecolor=col, edgecolor=edge, lw=LINE * 0.8, zorder=zorder + 2))


def _branch(ax, p, ang, length, depth, rng, edge, col, zorder):
    if depth == 0 or length < 0.12:
        return
    q = p + length * np.array([math.cos(ang), math.sin(ang)])
    ax.plot([p[0], q[0]], [p[1], q[1]], color=edge, lw=LINE * (0.6 + 0.5 * depth), solid_capstyle="round", zorder=zorder)
    for da in (-0.45, 0.45):
        _branch(ax, q, ang + da + rng.uniform(-0.15, 0.15), length * 0.62, depth - 1, rng, edge, col, zorder)


def _rot(ax, center, degrees):
    from matplotlib.transforms import Affine2D

    return Affine2D().rotate_deg(degrees).translate(*center) + ax.transData


def synapse(ax, center, width=3.0, vesicles=9, receptors=5, token="neuron", nt="metabolite", seed=2, zorder=10):
    """A chemical synapse seen in section: presynaptic bouton with vesicles above, cleft, postsynaptic membrane with receptors."""
    x, y = center
    rng = np.random.default_rng(seed)
    pre = smooth_closed(np.array([[x - width / 2, y + 0.25], [x - width * 0.45, y + 1.6], [x, y + 2.1], [x + width * 0.45, y + 1.6], [x + width / 2, y + 0.25], [x, y + 0.12]]))
    ax.add_patch(PathPatch(Path(pre, closed=True), facecolor=P.fill(token), edgecolor=P.edge(token), lw=LINE * 1.1, zorder=zorder))
    post = np.array([[x - width / 2 - 0.2, y - 0.25], [x + width / 2 + 0.2, y - 0.25], [x + width / 2 + 0.2, y - 1.4], [x - width / 2 - 0.2, y - 1.4]])
    ax.add_patch(FancyBboxPatch((x - width / 2 - 0.2, y - 1.4), width + 0.4, 1.15, boxstyle="round,pad=0,rounding_size=0.25",
                                facecolor=P.light(token), edgecolor=P.edge(token), lw=LINE * 1.1, zorder=zorder))
    for _ in range(vesicles):
        c = (x + rng.uniform(-width * 0.32, width * 0.32), y + rng.uniform(0.55, 1.5))
        ax.add_patch(Circle(c, 0.16, facecolor=P.fill("vesicle"), edgecolor=P.edge("vesicle"), lw=0.8, zorder=zorder + 1))
        for _ in range(3):
            ax.add_patch(Circle((c[0] + rng.uniform(-0.07, 0.07), c[1] + rng.uniform(-0.07, 0.07)), 0.025, color=P.edge(nt), lw=0, zorder=zorder + 2))
    for i in range(receptors):
        rx = x + (i - (receptors - 1) / 2) * width / receptors * 0.9
        ax.add_patch(FancyBboxPatch((rx - 0.08, y - 0.38), 0.16, 0.26, boxstyle="round,pad=0,rounding_size=0.06",
                                    facecolor=P.fill("receptor"), edgecolor=P.edge("receptor"), lw=0.7, zorder=zorder + 2))
    for _ in range(7):
        ax.add_patch(Circle((x + rng.uniform(-width * 0.3, width * 0.3), y + rng.uniform(-0.05, 0.08)), 0.03, color=P.edge(nt), lw=0, zorder=zorder + 3))
