"""Signed hydrogen wave functions in the xz plane, showing radial nodes and nodal planes."""

import numpy as np
import matplotlib.pyplot as plt

# (label, extent in a0, psi(x, z)) with radial parts up to normalization
def psi_2s(x, z):
    r = np.hypot(x, z)
    return (2 - r) * np.exp(-r / 2)


def psi_3s(x, z):
    r = np.hypot(x, z)
    return (27 - 18 * r + 2 * r**2) * np.exp(-r / 3)


def psi_2pz(x, z):
    r = np.hypot(x, z)
    return z * np.exp(-r / 2)


def psi_3pz(x, z):
    r = np.hypot(x, z)
    return (6 - r) * z * np.exp(-r / 3)


def psi_3dz2(x, z):
    r = np.hypot(x, z)
    return (3 * z**2 - r**2) * np.exp(-r / 3)


def psi_3dxz(x, z):
    r = np.hypot(x, z)
    return x * z * np.exp(-r / 3)


PANELS = [
    ("2s", 12, psi_2s), ("3s", 24, psi_3s), ("2p$_z$", 14, psi_2pz),
    ("3p$_z$", 24, psi_3pz), ("3d$_{z^2}$", 24, psi_3dz2), ("3d$_{xz}$", 24, psi_3dxz),
]

fig, axes = plt.subplots(2, 3, figsize=(10.5, 7.2))
for ax, (label, L, f) in zip(axes.flat, PANELS):
    x = np.linspace(-L, L, 501)
    X, Z = np.meshgrid(x, x)
    v = f(X, Z)
    v = v / np.abs(v).max()
    # compress the dynamic range so that the outer lobes stay visible
    w = np.sign(v) * np.abs(v) ** 0.5
    levels = np.linspace(0.08, 1.0, 12)
    ax.contourf(X, Z, w, levels=levels, cmap="Reds")
    ax.contourf(X, Z, -w, levels=levels, cmap="Blues")
    ax.contour(X, Z, v, levels=[0], colors="0.5", linewidths=0.8, linestyles="--")
    ax.plot(0, 0, "+", color="0.3", ms=6)
    ax.set_aspect("equal")
    ax.set_title(label)
    ax.set_xlabel(r"$x\,/\,a_0$")
    ax.set_ylabel(r"$z\,/\,a_0$")
fig.tight_layout()
