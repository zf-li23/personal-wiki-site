import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve

# ========== Part 1: derivative at the steady state ==========
r_values = np.linspace(2, 4, 10000)
derivative = np.zeros_like(r_values)

for i, r in enumerate(r_values):
    if r > 1:
        x_star = 1 - 1/r
        derivative[i] = abs(r * (1 - 2 * x_star))
    else:
        derivative[i] = abs(r)  # For r<=1 the steady state is 0 and the derivative is r

# Find r values where the derivative exceeds 1
unstable_r = r_values[derivative > 1]
if len(unstable_r) > 0:
    print(f'For r > {min(unstable_r):.4f}, the steady-state solution is unstable.')
else:
    print('No unstable solutions found in the given r range.')

# ========== Part 2: analyze the second iterate f(f(x)) ==========
r_range = np.linspace(3, 1 + np.sqrt(6), 50)
tolerance = 1e-6

# Second-iterate function
def ff_x(r, x):
    """f(f(x)) for logistic map"""
    f_x = r * x * (1 - x)
    return r * f_x * (1 - f_x)

# Lists for storing results
fixed_points_list = []
derivatives_list = []

for r in r_range:
    # Equation f(f(x)) - x = 0
    func = lambda x: ff_x(r, x) - x

    # Initial guess
    x_guess1, x_guess2 = 0.5, 0.8

    # Try to find the fixed points
    fixed_points_ff = []
    try:
        x1 = fsolve(func, x_guess1)[0]
        x2 = fsolve(func, x_guess2)[0]

        # Check that these are not fixed points of f(x)
        if (abs(r * x1 * (1 - x1) - x1) > tolerance and 
            abs(r * x2 * (1 - x2) - x2) > tolerance):
            # Ensure the points lie in [0,1]
            if 0 <= x1 <= 1:
                fixed_points_ff.append(x1)
            if 0 <= x2 <= 1 and abs(x2 - x1) > 1e-4:
                fixed_points_ff.append(x2)
    except:
        pass

    fixed_points_list.append(fixed_points_ff)

    # Derivative of f(f(x)) at the fixed points
    derivatives_cell = []
    if fixed_points_ff:
        for x_val in fixed_points_ff:
            # f'(f(x)) * f'(x)
            df_dx = r * (1 - 2 * (r * x_val * (1 - x_val))) * r * (1 - 2 * x_val)
            derivatives_cell.append(df_dx)

    derivatives_list.append(derivatives_cell)

# ========== Part 3: figure (two side-by-side subplots) ==========
fig, axes = plt.subplots(1, 2, figsize=(15, 6))

# Subplot 1: f(f(x)), y=x and the fixed points
ax1 = axes[0]
# Pick a few representative r values (to avoid clutter)
selected_indices = [10, 20, 30, 40]  # Four points from r_range
colors = ['b', 'g', 'm', 'c']  # Colours of the curves

x_plot = np.linspace(0, 1, 1000)
for idx, color in zip(selected_indices, colors):
    r = r_range[idx]
    ff_plot = ff_x(r, x_plot)
    ax1.plot(x_plot, ff_plot, color=color, linewidth=2, 
             label=f'$r={r:.2f}$', alpha=0.7)

    # Plot the fixed points (if any)
    if fixed_points_list[idx]:
        for point in fixed_points_list[idx]:
            ax1.plot(point, point, 'ko', markersize=8, 
                     markerfacecolor='k', markeredgecolor='w', zorder=5)

# Add the diagonal y=x
ax1.plot(x_plot, x_plot, 'r--', linewidth=1.5, alpha=0.5, label='$y=x$')

ax1.set_xlabel('$x$', fontsize=12)
ax1.set_ylabel('$f(f(x))$', fontsize=12)
ax1.set_title('$f(f(x))$ and $y=x$ for selected $r$ values', fontsize=14)
ax1.legend(fontsize=10)
ax1.grid(True, alpha=0.3)
ax1.set_xlim(0, 1)
ax1.set_ylim(0, 1)

# Subplot 2: derivative at the period-2 solution vs r
ax2 = axes[1]

# Collect all (r, derivative) points for plotting
r_plot_points = []
df_plot_points = []

for i, r in enumerate(r_range):
    if derivatives_list[i]:
        for df_dx in derivatives_list[i]:
            r_plot_points.append(r)
            df_plot_points.append(df_dx)

# Plot the derivative vs r
ax2.plot(r_plot_points, df_plot_points, 'b-', linewidth=2, alpha=0.7)

# Mark the stability bounds (|derivative|<1)
ax2.axhline(y=1, color='r', linestyle='--', linewidth=1.5, alpha=0.7, label='Stability bounds')
ax2.axhline(y=-1, color='r', linestyle='--', linewidth=1.5, alpha=0.7)

# Shade the stable region
ax2.fill_between(r_range, -1, 1, alpha=0.2, color='green', label=r'Stable region ($|\lambda|<1$)')

# Mark the theoretical stability boundaries
r_stable_upper = 1 + np.sqrt(6)
ax2.axvline(x=3, color='k', linestyle=':', linewidth=1.5, alpha=0.5, label='$r=3$')
ax2.axvline(x=r_stable_upper, color='k', linestyle=':', linewidth=1.5, alpha=0.5, 
            label=fr'$r=1+\sqrt{{6}}\approx{r_stable_upper:.3f}$')

ax2.set_xlabel('$r$', fontsize=12)
ax2.set_ylabel('Derivative of $f(f(x))$ at fixed points', fontsize=12)
ax2.set_title('Stability analysis for period-2 solutions', fontsize=14)
ax2.legend(fontsize=10)
ax2.grid(True, alpha=0.3)
ax2.set_xlim(3, r_stable_upper)

# Adjust the layout
plt.tight_layout()
