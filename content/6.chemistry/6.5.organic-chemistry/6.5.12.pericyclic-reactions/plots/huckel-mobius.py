"""Aromatic transition states (Dewar-Zimmerman). A cyclic array of N orbitals with no phase
inversion (Hueckel array) has levels 2 cos(2 pi k / N); with one phase inversion (Moebius array,
like a twisted strip) the levels are 2 cos((2k + 1) pi / N), in units of |beta| (both computed here
as eigenvalues with numpy). Filling N electrons: Hueckel arrays are closed-shell (aromatic) for
4n + 2 electrons, Moebius arrays for 4n electrons."""

exec(open("orbitals.txt").read())


def ring_levels(n, mobius):
    H = np.zeros((n, n))
    for i in range(n):
        j = (i + 1) % n
        b = -1.0 if (mobius and j == 0) else 1.0  # one sign inversion closes a Moebius ring
        H[i, j] = H[j, i] = b
    return np.sort(np.linalg.eigvalsh(H))[::-1]  # x in E = alpha + x beta, bonding (x > 0) drawn lowest


def basis(ax, n, mobius):
    t = np.linspace(0, 2 * np.pi, n, endpoint=False) - np.pi / 2
    pts = [(1.6 * np.cos(a), 0.95 * np.sin(a)) for a in t]
    for i in range(n):
        a, b = pts[i], pts[(i + 1) % n]
        ax.plot(*zip(a, b), color=ink(), lw=1.2)
    flipped = n // 2 if mobius else -1
    for i, p in enumerate(pts):
        porb(ax, p, -1.0 if i == flipped else 1.0, scale=0.36)
    if mobius:
        a, b = np.array(pts[flipped]), np.array(pts[flipped - 1])
        m = (a + b) / 2
        ax.plot(*m, marker="o", ms=7, mfc="none", mec="#d1495b", mew=1.8)
        ax.text(m[0] + 0.2, m[1] + 0.3, "phase change", ha="left", va="bottom", fontsize=8, color="#d1495b")
    ax.set_title("Moebius array (one sign change)" if mobius else "Hueckel array (no sign change)", fontsize=9.5, color=ink())
    clean(ax, (-2.6, 2.1), (-1.5, 1.5))


def diagram(ax, n, mobius):
    x = ring_levels(n, mobius)
    E = -x  # plot energy upward: bonding levels low
    vals, counts = np.unique(np.round(E, 6), return_counts=True)
    left = n
    for e, g in zip(vals, counts):
        here = min(left, 2 * g)
        fill = [here // g + (1 if k < here % g else 0) for k in range(g)]  # Hund: singly first
        for k in range(g):
            level(ax, (k - (g - 1) / 2) * 0.9, e, w=0.7, n=fill[k])
        left -= here
    closed = (n % 4 == 2) != mobius
    ax.set_title(f"{n} electrons: {'aromatic' if closed else 'antiaromatic'}", fontsize=9.5, color="C2" if closed else "#d1495b")
    ax.axhline(0, color="0.6", lw=0.6, ls=":")
    ax.set_xlim(-1.6, 1.6)
    ax.set_ylim(-2.4, 2.4)
    ax.axis("off")


fig, axes = plt.subplots(2, 3, figsize=(8.8, 5.6))
for r, mob in enumerate((False, True)):
    basis(axes[r, 0], 6, mob)
    diagram(axes[r, 1], 4, mob)
    diagram(axes[r, 2], 6, mob)
fig.tight_layout()
