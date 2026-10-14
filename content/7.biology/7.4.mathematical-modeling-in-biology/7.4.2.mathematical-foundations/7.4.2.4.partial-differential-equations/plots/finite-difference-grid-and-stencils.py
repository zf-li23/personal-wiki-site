"""
plot_fd_scheme.py
Schematic of the finite-difference grid and difference stencils
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

def plot_fd_grid():
    """Plot a schematic of the space-time computational grid"""
    fig, ax = plt.subplots(figsize=(10, 6))

    nx = 6
    nt = 5
    dx = 1.0
    dt = 1.0

    # Draw grid lines
    for i in range(nx + 1):
        ax.axvline(x=i*dx, color='gray', linestyle='--', alpha=0.3)
    for n in range(nt + 1):
        ax.axhline(y=n*dt, color='gray', linestyle='--', alpha=0.3)

    # Draw nodes
    for i in range(nx + 1):
        for n in range(nt + 1):
            ax.plot(i*dx, n*dt, 'ko', markersize=4, alpha=0.5)

    # Highlight the computational molecule - explicit scheme
    # u_i^{n+1} depends on u_{i-1}^n, u_i^n, u_{i+1}^n
    cx, cy = 3*dx, 3*dt  # centre point (i, n)

    # Three points on the lower level (n)
    ax.plot([cx-dx, cx, cx+dx], [cy-dt, cy-dt, cy-dt], 'ro-', markersize=8, label='known $t_n$')
    # One point on the upper level (n+1)
    ax.plot(cx, cy, 'bo', markersize=8, label='unknown $t_{n+1}$')

    # Connecting lines
    ax.plot([cx-dx, cx], [cy-dt, cy], 'g-', alpha=0.5)
    ax.plot([cx, cx], [cy-dt, cy], 'g-', alpha=0.5)
    ax.plot([cx+dx, cx], [cy-dt, cy], 'g-', alpha=0.5)

    # Text annotations
    offset = 0.15
    ax.text(cx, cy + offset, '$(x_i, t_{n+1})$', ha='center', color='blue', fontsize=12, fontweight='bold')
    ax.text(cx, cy-dt - offset, '$(x_i, t_n)$', ha='center', color='red', fontsize=12)
    ax.text(cx-dx, cy-dt - offset, '$(x_{i-1}, t_n)$', ha='center', color='red', fontsize=12)
    ax.text(cx+dx, cy-dt - offset, '$(x_{i+1}, t_n)$', ha='center', color='red', fontsize=12)

    # Axis labels
    ax.set_xlabel('Space $x$', fontsize=14)
    ax.set_ylabel('Time $t$', fontsize=14)
    ax.set_title('Finite Difference Method: Schematic of the Explicit Euler Scheme', fontsize=16)

    # Custom ticks
    ax.set_xticks([i*dx for i in range(nx+1)])
    ax.set_xticklabels([f'$x_{i}$' for i in range(nx+1)])
    ax.set_yticks([n*dt for n in range(nt+1)])
    ax.set_yticklabels([f'$t_{n}$' for n in range(nt+1)])

    # Remove top and right spines
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)

    ax.legend(loc='upper right')

    plt.tight_layout()

def plot_stencils():
    """Plot finite-difference stencils for 1D and 2D derivatives"""
    fig, axes = plt.subplots(1, 2, figsize=(12, 5))

    # 1. Central difference for the second derivative (1D Laplacian)
    ax = axes[0]
    ax.set_aspect('equal')
    ax.set_xlim(-2, 2)
    ax.set_ylim(-1, 1)
    ax.axis('off')

    # Points
    points = [(-1, 0), (0, 0), (1, 0)]
    labels = ['$i-1$', '$i$', '$i+1$']
    coeffs = ['$1$', '$-2$', '$1$']

    # Connecting line
    ax.plot([-1, 1], [0, 0], 'k-', lw=2)

    for (x, y), label, coeff in zip(points, labels, coeffs):
        # Node circle
        circle = patches.Circle((x, y), 0.2, facecolor='white', edgecolor='black', linewidth=2)
        ax.add_patch(circle)
        # Node index
        ax.text(x, y - 0.4, label, ha='center', va='top', fontsize=14)
        # Coefficient
        ax.text(x, y, coeff, ha='center', va='center', fontsize=14, fontweight='bold')

    ax.text(0, 0.6, r'$\frac{\partial^2 u}{\partial x^2} \approx \frac{1}{\Delta x^2} \times$', 
            ha='center', fontsize=16)
    ax.set_title('1D central-difference stencil for the second derivative', fontsize=14)

    # 2. Five-point stencil for the 2D Laplacian
    ax = axes[1]
    ax.set_aspect('equal')
    ax.set_xlim(-2, 2)
    ax.set_ylim(-2, 2)
    ax.axis('off')

    # Grid lines
    ax.plot([-1.5, 1.5], [0, 0], 'k--', lw=1, alpha=0.3)
    ax.plot([0, 0], [-1.5, 1.5], 'k--', lw=1, alpha=0.3)

    # Connecting lines (cross)
    ax.plot([-1, 1], [0, 0], 'k-', lw=2)
    ax.plot([0, 0], [-1, 1], 'k-', lw=2)

    points = [(0, 0), (-1, 0), (1, 0), (0, 1), (0, -1)]
    labels = ['$(i,j)$', '$(i-1,j)$', '$(i+1,j)$', '$(i,j+1)$', '$(i,j-1)$']
    coeffs = ['$-4$', '$1$', '$1$', '$1$', '$1$']

    for (x, y), label, coeff in zip(points, labels, coeffs):
        # Node circle
        circle = patches.Circle((x, y), 0.25, facecolor='white', edgecolor='black', linewidth=2)
        ax.add_patch(circle)
        # Node index
        # For the centre point, place the label slightly lower-right to avoid overlap
        if x==0 and y==0:
            ax.text(x + 0.3, y - 0.3, label, ha='left', va='top', fontsize=12)
        elif x == 0: # points on the vertical axis
            ax.text(x + 0.3, y, label, ha='left', va='center', fontsize=12)
        else: # points on the horizontal axis
            ax.text(x, y - 0.4, label, ha='center', va='top', fontsize=12)

        # Coefficient
        ax.text(x, y, coeff, ha='center', va='center', fontsize=14, fontweight='bold')

    ax.text(0, 1.6, r'$\nabla^2 u \approx \frac{1}{h^2} \times$', 
            ha='center', fontsize=16)
    ax.set_title('Five-point stencil for the 2D Laplacian', fontsize=14)

    plt.tight_layout()

plot_fd_grid()
plot_stencils()
