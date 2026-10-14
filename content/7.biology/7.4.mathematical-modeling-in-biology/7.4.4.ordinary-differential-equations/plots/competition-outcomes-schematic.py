"""
competition_phase_diagrams.py
Schematic diagrams of the four outcomes of the Lotka-Volterra competition model
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

def plot_competition_schematic(a, b, case_name, ax):
    """Draw a competition-model schematic, marking the key thresholds"""

    # Set axis ranges
    x_max = max(1.5, 1.2 * max(1, 1/b if b > 0 else 0))
    y_max = max(1.5, 1.2 * max(1, 1/a if a > 0 else 0))

    # Draw axes
    ax.set_xlim(0, x_max)
    ax.set_ylim(0, y_max)

    # Remove tick labels
    ax.set_xticks([])
    ax.set_yticks([])

    # Draw nullclines
    # Species 1 nullcline: x=0 or y=(1-x)/a
    if a > 0:
        x_vals = np.linspace(0, x_max, 100)
        y_xnull = (1 - x_vals) / a
        valid = (y_xnull >= 0) & (y_xnull <= y_max)
        ax.plot(x_vals[valid], y_xnull[valid], 'r-', linewidth=2, label='$dx/dτ=0$')

    # Species 2 nullcline: y=0 or y=1-bx
    x_vals = np.linspace(0, x_max, 100)
    y_ynull = 1 - b * x_vals
    valid = (y_ynull >= 0) & (y_ynull <= y_max)
    ax.plot(x_vals[valid], y_ynull[valid], 'b-', linewidth=2, label='$dy/dτ=0$')

    # Mark key points
    # (1, 0) - carrying capacity of species 1
    ax.plot(1, 0, 'ko', markersize=8)
    # Label placed inside, va='bottom'
    ax.text(1, 0.02*y_max, '$K_1$', ha='center', va='bottom', fontsize=12, fontweight='bold')

    # (0, 1) - carrying capacity of species 2
    ax.plot(0, 1, 'ko', markersize=8)
    # Label placed inside, ha='left'
    ax.text(0.02*x_max, 1, '$K_2$', ha='left', va='center', fontsize=12, fontweight='bold')

    # Intersections of nullclines with the axes
    # Species 1 nullcline meets the y-axis at (0, 1/a)
    if a > 0:
        ax.plot(0, 1/a, 'ro', markersize=6)
        # Label placed inside, ha='left'
        ax.text(0.02*x_max, 1/a, '$K_1/α$', ha='left', va='center', fontsize=12, color='red', fontweight='bold')

    # Species 2 nullcline meets the x-axis at (1/b, 0)
    if b > 0:
        ax.plot(1/b, 0, 'bo', markersize=6)
        # Label placed inside, va='bottom'
        ax.text(1/b, 0.02*y_max, '$K_2/β$', ha='center', va='bottom', fontsize=12, color='blue', fontweight='bold')

    # Mark the coexistence equilibrium (if it exists)
    denominator = 1 - a * b
    if abs(denominator) > 1e-10:
        x_star = (1 - a) / denominator
        y_star = (1 - b) / denominator

        if 0 <= x_star <= x_max and 0 <= y_star <= y_max:
            # Use different markers depending on stability
            # Eigenvalues of the Jacobian
            J11 = 1 - 2*x_star - a*y_star
            J12 = -a * x_star
            J21 = -b * y_star  # Note: assumes ρ=1
            J22 = 1 - 2*y_star - b*x_star

            # Trace and determinant
            trace = J11 + J22
            det = J11 * J22 - J12 * J21

            # Determine stability
            if det > 0 and trace < 0:
                # Stable node or focus
                ax.plot(x_star, y_star, 'go', markersize=10, markeredgecolor='black', markeredgewidth=1)
                ax.text(x_star+0.02*x_max, y_star+0.02*y_max, 'Stable', fontsize=10, color='green')
            elif det < 0:
                # Saddle
                ax.plot(x_star, y_star, 'yo', markersize=10, markeredgecolor='black', markeredgewidth=1)
                ax.text(x_star+0.02*x_max, y_star+0.02*y_max, 'Saddle', fontsize=10, color='orange')
            else:
                ax.plot(x_star, y_star, 'ko', markersize=10)

    # Add vector-field arrows covering the whole plot
    nx, ny = 20, 20
    x_grid = np.linspace(0, x_max, nx)
    y_grid = np.linspace(0, y_max, ny)
    X, Y = np.meshgrid(x_grid, y_grid)

    # Competition model ODEs (simplified, r1=r2=1)
    # dx/dt = x(1 - x - ay)
    # dy/dt = y(1 - y - bx)
    U = X * (1 - X - a * Y)
    V = Y * (1 - Y - b * X)

    # Normalize arrow lengths for readability
    N = np.sqrt(U**2 + V**2)
    # Avoid division by zero
    N[N==0] = 1
    U = U / N
    V = V / N

    # Draw arrows
    ax.quiver(X, Y, U, V, color='gray', alpha=0.3, width=0.003, scale=30, headwidth=4)

    # Titles and labels
    ax.set_xlabel('Species 1 (x = $N_1/K_1$)', fontsize=12)
    ax.set_ylabel('Species 2 (y = $N_2/K_2$)', fontsize=12)
    ax.set_title(f'{case_name}\na = {a}, b = {b}', fontsize=14)
    ax.grid(True, alpha=0.3, linestyle='--')
    ax.legend(fontsize=10, loc='upper right')

    # Add explanatory text
    conditions_text = f'Conditions:\n'
    if a < 1 and b > 1:
        conditions_text += '$K_1 > K_2/β$\n$K_2 < K_1/α$'
    elif a > 1 and b < 1:
        conditions_text += '$K_2 > K_1/α$\n$K_1 < K_2/β$'
    elif a < 1 and b < 1:
        conditions_text += '$K_1 < K_2/β$\n$K_2 < K_1/α$'
    elif a > 1 and b > 1:
        conditions_text += '$K_1 > K_2/β$\n$K_2 > K_1/α$'

    ax.text(0.02, 0.98, conditions_text, transform=ax.transAxes,
           fontsize=10, verticalalignment='top',
           bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))

# Create schematics for the four cases
fig, axes = plt.subplots(2, 2, figsize=(14, 12))

# Case 1: species 1 wins (a < 1, b > 1)
plot_competition_schematic(a=0.5, b=1.5,
                          case_name='(a) Species 1 wins',
                          ax=axes[0, 0])

# Case 2: species 2 wins (a > 1, b < 1)
plot_competition_schematic(a=1.5, b=0.5,
                          case_name='(b) Species 2 wins',
                          ax=axes[0, 1])

# Case 3: unstable coexistence (a > 1, b > 1)
plot_competition_schematic(a=1.5, b=1.5,
                          case_name='(c) Unstable coexistence',
                          ax=axes[1, 0])

# Case 4: stable coexistence (a < 1, b < 1)
plot_competition_schematic(a=0.5, b=0.5,
                          case_name='(d) Stable coexistence',
                          ax=axes[1, 1])

# Adjust subplot spacing, with extra vertical padding (h_pad)
plt.tight_layout(h_pad=3.0)
