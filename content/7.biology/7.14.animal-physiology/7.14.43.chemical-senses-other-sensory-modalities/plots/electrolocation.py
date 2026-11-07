"""Active electrolocation: the electric image of a small sphere (quasi-static model).

Fish: a current source +I at the head (x = +5 cm) and a sink -I at the tail (x = -5 cm) in an
unbounded uniform medium of conductivity sigma_w, so phi0 = I/(4 pi sigma_w) (1/r_+ - 1/r_-)
(the real body and skin are ignored). A sphere of radius a = 0.5 cm and conductivity sigma_o
centred at r_0 acquires an induced dipole; outside it the perturbation is
  delta phi = chi a^3 E_0 . (r - r_0) / |r - r_0|^3,   chi = (sigma_o - sigma_w)/(sigma_o + 2 sigma_w),
with E_0 the unperturbed field at r_0 (Rasnow 1996). chi = 1 for a perfect conductor (metal, prey
tissue is weakly conducting) and -1/2 for an insulator (stone, plastic).
A: equipotentials of the fish field in the plane of the body (arbitrary units), sphere at
(2.5, 1.5) cm. B: "electric image" along a line 0.4 cm lateral to the body axis for a
conductor and an insulator at lateral distance 1.5 cm (sphere at x = 2.5 cm); the image is the
lateral component of the perturbing field, which sets the change of current through the skin. C: images of a conductor at lateral
distances 1, 2 and 3 cm, each normalised to its peak: farther objects give weaker and wider images.
"""
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio

P = bio.P
head, tail = np.array([5.0, 0.0]), np.array([-5.0, 0.0])
a = 0.5


def phi0(X, Y):
    rp = np.hypot(X - head[0], Y - head[1])
    rm = np.hypot(X - tail[0], Y - tail[1])
    return 1 / rp - 1 / rm


def E0(x, y):
    E = np.zeros(2)
    for src, q in ((head, 1.0), (tail, -1.0)):
        d = np.array([x, y]) - src
        E += q * d / np.linalg.norm(d) ** 3
    return E


def image(x, y, r0, chi, h=1e-3):
    """Normal (lateral) component of the perturbing field at the skin, -d(delta phi)/dy."""
    return -(dphi(x, y + h, r0, chi) - dphi(x, y - h, r0, chi)) / (2 * h)


def dphi(X, Y, r0, chi):
    E = E0(*r0)
    dx, dy = X - r0[0], Y - r0[1]
    r3 = np.hypot(dx, dy) ** 3
    return chi * a**3 * (E[0] * dx + E[1] * dy) / r3


fig, axs = plt.subplots(1, 3, figsize=(13.5, 4.2), gridspec_kw={"width_ratios": [1.3, 1, 1]})
ax = axs[0]
xs, ys = np.linspace(-10, 10, 400), np.linspace(-6, 6, 260)
X, Y = np.meshgrid(xs, ys)
r0 = (2.5, 1.5)
F = phi0(X, Y) + dphi(X, Y, r0, 1.0)
inside = np.hypot(X - r0[0], Y - r0[1]) < a
F[inside] = np.nan
lev = np.concatenate([-np.logspace(-2.2, 0.3, 12)[::-1], np.logspace(-2.2, 0.3, 12)])
ax.contour(X, Y, F, levels=lev, colors=[P.muted()], linewidths=0.7)
ax.add_patch(plt.matplotlib.patches.Ellipse((0, 0), 11, 1.2, facecolor=P.fill("animal"),
                                            edgecolor=P.edge("animal"), lw=1.2))
ax.add_patch(plt.Circle(r0, a, facecolor=P.fill("rna"), edgecolor=P.edge("rna"), lw=1.2))
ax.text(5.6, -1.0, "head (+)", fontsize=8, color=P.ink())
ax.text(-8.8, -1.0, "tail (-)", fontsize=8, color=P.ink())
ax.text(3.2, 2.0, "conducting sphere", fontsize=8, color=P.edge("rna"))
ax.set_aspect("equal")
ax.set_xlim(-10, 10)
ax.set_ylim(-6, 6)
ax.set_xlabel("x / cm")
ax.set_ylabel("y / cm")
ax.set_title("A  Equipotentials of the discharge", loc="left", fontsize=10)

x = np.linspace(-8, 8, 600)
yline = 0.4
bx = axs[1]
for chi, c, lab in ((1.0, P.edge("rna"), "conductor (χ = 1)"), (-0.5, P.edge("dna"),
                                                                "insulator (χ = -1/2)")):
    bx.plot(x, image(x, yline, (2.5, 1.5), chi), color=c, lw=2, label=lab)
bx.axhline(0, color=P.muted(), lw=0.5)
bx.set_xlabel("Position along the body / cm")
bx.set_ylabel("Change of transskin field (arbitrary units)")
bx.legend(frameon=False, fontsize=8)
bx.set_title("B  Bright and dark images", loc="left", fontsize=10)

cx = axs[2]
for d, c in ((1.0, P.edge("rna")), (2.0, P.edge("enzyme")), (3.0, P.edge("dna"))):
    im = image(x, yline, (2.5, d), 1.0)
    pk = np.abs(im).max()
    half = x[np.abs(im) >= pk / 2]
    cx.plot(x, im / pk, color=c, lw=2,
            label=f"{d:g} cm: peak x{pk / np.abs(image(x, yline, (2.5, 1.0), 1.0)).max():.2f},"
                  f" half-width {half.max() - half.min():.1f} cm")
cx.axhline(0, color=P.muted(), lw=0.5)
cx.set_xlabel("Position along the body / cm")
cx.set_ylabel("Image (normalised to its peak)")
cx.legend(frameon=False, fontsize=7.5, loc="upper left")
cx.set_ylim(-0.6, 1.5)
cx.set_title("C  Distance widens the image", loc="left", fontsize=10)
fig.tight_layout()
