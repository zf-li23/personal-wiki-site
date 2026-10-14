import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve

def plot_iterated_functions():
    """Compare iterated maps of different orders"""
    fig, axes = plt.subplots(1, 3, figsize=(18, 5))

    x = np.linspace(0, 1, 1000)

    # Column 1: f(x) for r=2
    r1 = 2.0
    ax1 = axes[0]
    f1 = r1 * x * (1 - x)
    ax1.plot(x, f1, 'b-', linewidth=2, label=f'$f(x)$, r={r1}')
    ax1.plot(x, x, 'k--', linewidth=1, label='$y=x$')
    ax1.set_xlabel('x', fontsize=12)
    ax1.set_ylabel('f(x)', fontsize=12)
    ax1.set_title('Original Map', fontsize=14)
    ax1.legend(fontsize=10)
    ax1.grid(True, alpha=0.3)
    ax1.set_xlim(0, 1)
    ax1.set_ylim(0, 1)

    # Column 2: f(f(x)) for r=3.2
    r2 = 3.2
    ax2 = axes[1]
    f2 = r2 * x * (1 - x)
    ff2 = r2 * f2 * (1 - f2)

    # Mark the fixed points (period-2 orbit)
    # Solve f(f(x)) = x for nonzero roots
    def fixed_points(r):
        """Return the two points of the period-2 orbit"""
        # Solve f(f(x)) - x = 0
        solutions = []
        for guess in [0.2, 0.4, 0.6, 0.8]:
            sol = fsolve(lambda y: r * (r * y * (1 - y)) * (1 - r * y * (1 - y)) - y, guess, full_output=True)
            if sol[2] == 1 and 0 < sol[0][0] < 1:
                solutions.append(sol[0][0])
        return np.unique(np.round(solutions, 6))

    period2_points = fixed_points(r2)

    ax2.plot(x, ff2, 'b-', linewidth=2, label=f'$f(f(x))$, r={r2}')
    ax2.plot(x, x, 'k--', linewidth=1, label='$y=x$')
    # Mark the fixed points
    for point in period2_points:
        ax2.plot([point], [point], 'ro', markersize=8)

    # Highlight the region around x=0.5
    ax2.add_patch(plt.Rectangle((0.3, 0.3), 0.4, 0.4, 
                               edgecolor='red', facecolor='none', 
                               linestyle='--', linewidth=2))

    ax2.set_xlabel('x', fontsize=12)
    ax2.set_ylabel('f(f(x))', fontsize=12)
    ax2.set_title('Period-2: Two Fixed Points', fontsize=14)
    ax2.legend(fontsize=10)
    ax2.grid(True, alpha=0.3)
    ax2.set_xlim(0, 1)
    ax2.set_ylim(0, 1)

    # Column 3: f^{(4)}(x) for r=3.5
    r3 = 3.5
    ax3 = axes[2]

    # Compute f^{(4)}(x)
    def iterate(f, x, n):
        """Iterate the map n times"""
        result = x
        for _ in range(n):
            result = r3 * result * (1 - result)
        return result

    f4 = iterate(lambda y: r3 * y * (1 - y), x, 4)

    ax3.plot(x, f4, 'b-', linewidth=2, label=f'$f^{(4)}(x)$, r={r3}')
    ax3.plot(x, x, 'k--', linewidth=1, label='$y=x$')

    # Highlight the (smaller) region around x=0.5
    ax3.add_patch(plt.Rectangle((0.425, 0.425), 0.15, 0.15,
                               edgecolor='red', facecolor='none',
                               linestyle='--', linewidth=2))

    ax3.set_xlabel('x', fontsize=12)
    ax3.set_ylabel(f'$f^{(4)}(x)$', fontsize=12)
    ax3.set_title('Period-4: Four Fixed Points', fontsize=14)
    ax3.legend(fontsize=10)
    ax3.grid(True, alpha=0.3)
    ax3.set_xlim(0, 1)
    ax3.set_ylim(0, 1)

    plt.tight_layout()

plot_iterated_functions()
