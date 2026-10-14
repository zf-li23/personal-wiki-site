import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve

def renormalization_demo():
    """Demonstration of the renormalization-group operation"""
    fig, axes = plt.subplots(2, 2, figsize=(12, 10))

    # Parameters
    r = 3.5  # In the period-4 region
    x = np.linspace(0, 1, 1000)

    # 1. Original map f(x)
    ax1 = axes[0, 0]
    f = r * x * (1 - x)
    ax1.plot(x, f, 'b-', linewidth=2)
    ax1.plot(x, x, 'k--', linewidth=1)
    ax1.set_xlabel('x', fontsize=12)
    ax1.set_ylabel('f(x)', fontsize=12)
    ax1.set_title(f'Original: f(x), r={r}', fontsize=14)
    ax1.grid(True, alpha=0.3)

    # 2. Second iterate f(f(x))
    ax2 = axes[0, 1]
    ff = r * f * (1 - f)
    ax2.plot(x, ff, 'b-', linewidth=2)
    ax2.plot(x, x, 'k--', linewidth=1)

    # Pick a region around one fixed point (a point of the period-2 orbit)
    # Here we choose the zoom region by hand
    zoom_center = 0.5
    zoom_width = 0.2

    ax2.add_patch(plt.Rectangle((zoom_center-zoom_width/2, zoom_center-zoom_width/2),
                               zoom_width, zoom_width,
                               edgecolor='red', facecolor='none',
                               linestyle='--', linewidth=2))
    ax2.set_xlabel('x', fontsize=12)
    ax2.set_ylabel('f(f(x))', fontsize=12)
    ax2.set_title(f'First iteration: f(f(x))', fontsize=14)
    ax2.grid(True, alpha=0.3)

    # 3. Zoomed region: self-similarity
    ax3 = axes[1, 0]
    # Sample inside the red box
    x_zoom = np.linspace(zoom_center-zoom_width/2, zoom_center+zoom_width/2, 200)
    ff_zoom = r * (r * x_zoom * (1 - x_zoom)) * (1 - r * x_zoom * (1 - x_zoom))

    # Change of coordinates: map the region onto [0,1]
    x_normalized = (x_zoom - (zoom_center-zoom_width/2)) / zoom_width
    # Normalize the function values too
    ff_normalized = (ff_zoom - (zoom_center-zoom_width/2)) / zoom_width

    # For comparison, plot the original f(x) at r=2 (orientation adjusted)
    r_comparison = 2.0
    f_comparison = r_comparison * x_normalized * (1 - x_normalized)

    ax3.plot(x_normalized, -ff_normalized + 1, 'r-', linewidth=2, label='Rescaled f(f(x))')
    ax3.plot(x_normalized, f_comparison, 'b--', linewidth=2, label=f'f(x) with r={r_comparison}')
    ax3.plot(x_normalized, x_normalized, 'k:', linewidth=1)

    ax3.set_xlabel('Rescaled x', fontsize=12)
    ax3.set_ylabel('Rescaled f', fontsize=12)
    ax3.set_title('Renormalization: Self-Similarity', fontsize=14)
    ax3.legend(fontsize=10)
    ax3.grid(True, alpha=0.3)

    # 4. Numerical estimate of the Feigenbaum constant
    ax4 = axes[1, 1]
    ax4.axis('off')

    # Sequence of bifurcation points
    def bifurcation_points(order=6):
        """Approximate the first n bifurcation points"""
        # Known approximate bifurcation points
        # r1: period 1->2 (r=3)
        # r2: period 2->4 (r≈3.4494897)
        # r3: period 4->8 (r≈3.544090)
        # r4: period 8->16 (r≈3.564407)
        # r5: period 16->32 (r≈3.568759)
        # r6: period 32->64 (r≈3.569692)

        r_vals = [3.0, 3.4494897, 3.544090, 3.564407, 3.568759, 3.569692]
        return r_vals[:order]

    r_vals = bifurcation_points(6)

    # Compute the Feigenbaum constant δ
    deltas = []
    for i in range(1, len(r_vals)-1):
        delta = (r_vals[i] - r_vals[i-1]) / (r_vals[i+1] - r_vals[i])
        deltas.append(delta)

    text = "Feigenbaum Constants:\n\n"
    text += "Bifurcation points:\n"
    for i, r_val in enumerate(r_vals):
        period = 2**i
        text += f"  Period {period} → {period*2}: r_{i+1} = {r_val:.6f}\n"

    text += "\nδ (interval ratio):\n"
    for i, delta in enumerate(deltas):
        text += f"  δ_{i+1} = {delta:.4f}\n"

    text += f"\nLimit δ∞ ≈ 4.669201609...\n"
    text += f"Our approx: {deltas[-1]:.4f}"

    ax4.text(0.1, 0.9, text, fontsize=11, verticalalignment='top',
            bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))

    plt.tight_layout()

renormalization_demo()
