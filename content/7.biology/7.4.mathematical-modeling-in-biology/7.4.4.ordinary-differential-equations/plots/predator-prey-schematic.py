"""
predator_prey_schematic.py
Nullcline schematics and oscillatory behaviour of predator-prey models
"""

import numpy as np
import matplotlib.pyplot as plt

def plot_predator_prey_schematic(ax, alpha=1.0, beta=1.0, gamma=0.0):
    """Draw a predator-prey model schematic"""

    # Set axis ranges
    x_max = 2.5
    y_max = 2.5

    ax.set_xlim(0, x_max)
    ax.set_ylim(0, y_max)

    # Prey nullcline: x=0 or y=1-γx
    x_vals = np.linspace(0, x_max, 100)

    if gamma == 0:
        # Classic model: y=1
        ax.axhline(1, 0, 1, color='red', linewidth=2, label='Prey nullcline ($dx/dτ=0$)')
    else:
        # With density dependence: y=1-γx
        y_prey_null = 1 - gamma * x_vals
        valid = (y_prey_null >= 0) & (y_prey_null <= y_max)
        ax.plot(x_vals[valid], y_prey_null[valid], 'r-', linewidth=2, label='Prey nullcline ($dx/dτ=0$)')

    # Predator nullcline: y=0 or x=β
    ax.axvline(beta, 0, 1, color='blue', linewidth=2, label='Predator nullcline ($dy/dτ=0$)')

    # Mark the equilibrium
    if gamma == 0:
        # Classic model: (1,1)
        ax.plot(1, 1, 'go', markersize=10, markeredgecolor='black',
               markeredgewidth=1, label='Center equilibrium')
        ax.text(1.05, 1.05, '(1,1)', fontsize=11)
    else:
        # With density dependence: (β, 1-γβ)
        y_star = 1 - gamma * beta
        if y_star > 0:
            ax.plot(beta, y_star, 'go', markersize=10, markeredgecolor='black',
                   markeredgewidth=1, label='Equilibrium')
            ax.text(beta+0.05, y_star+0.05, f'({beta:.1f},{y_star:.1f})', fontsize=11)

    # Add vector-field arrows
    # Create grid
    x_grid, y_grid = np.meshgrid(np.linspace(0.1, x_max-0.1, 12),
                                np.linspace(0.1, y_max-0.1, 12))

    # Compute directions
    dx = x_grid * (1 - gamma*x_grid - y_grid)
    dy = alpha * y_grid * (x_grid - beta)

    # Normalize
    norm = np.sqrt(dx**2 + dy**2)
    mask = norm > 0
    dx[mask] = dx[mask] / norm[mask] * 0.15
    dy[mask] = dy[mask] / norm[mask] * 0.15

    # Draw vector field
    ax.quiver(x_grid, y_grid, dx, dy, color='gray', alpha=0.6,
              angles='xy', scale_units='xy', scale=1, width=0.004)

    # Draw an example trajectory
    if gamma == 0:
        # Classic model: closed orbit
        # Parametric form: x = 1 + A*cos(ωt), y = 1 + B*sin(ωt)
        t = np.linspace(0, 2*np.pi, 200)
        A, B = 0.5, 0.5
        x_traj = 1 + A * np.cos(t)
        y_traj = 1 + B * np.sin(t)
        ax.plot(x_traj, y_traj, 'purple', linewidth=2, alpha=0.8, label='Periodic orbit')
    else:
        # With density dependence: spiral trajectory
        from scipy.integrate import solve_ivp

        def equations(t, state):
            x, y = state
            dxdt = x * (1 - gamma*x - y)
            dydt = alpha * y * (x - beta)
            return [dxdt, dydt]

        # Start near the equilibrium
        if gamma > 0:
            x0, y0 = beta, 1 - gamma*beta
            sol = solve_ivp(equations, [0, 50], [x0*1.2, y0*1.2],
                           method='RK45', rtol=1e-8)
            ax.plot(sol.y[0], sol.y[1], 'purple', linewidth=2, alpha=0.8, label='Trajectory')

    # Label key regions
    # Region I: prey increase, predators decrease
    ax.text(0.05*x_max, 0.5*y_max, 'I: Prey↑, Predator↓',
           fontsize=10, bbox=dict(boxstyle='round', facecolor='yellow', alpha=0.5))

    # Region II: prey increase, predators increase
    ax.text(0.5*x_max, 0.5*y_max, 'II: Prey↑, Predator↑',
           fontsize=10, bbox=dict(boxstyle='round', facecolor='lightgreen', alpha=0.5))

    # Region III: prey decrease, predators increase
    ax.text(0.5*x_max, 0.1*y_max, 'III: Prey↓, Predator↑',
           fontsize=10, bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.5))

    # Region IV: prey decrease, predators decrease
    ax.text(0.05*x_max, 0.1*y_max, 'IV: Prey↓, Predator↓',
           fontsize=10, bbox=dict(boxstyle='round', facecolor='pink', alpha=0.5))

    # Titles and labels
    ax.set_xlabel('Prey population (x)', fontsize=12)
    ax.set_ylabel('Predator population (y)', fontsize=12)

    if gamma == 0:
        title = 'Classic Lotka-Volterra Model\nα = {:.1f}'.format(alpha)
    else:
        title = f'Modified Model with Density Dependence\nα = {alpha:.1f}, β = {beta:.1f}, γ = {gamma:.1f}'

    ax.set_title(title, fontsize=14)
    ax.grid(True, alpha=0.3, linestyle='--')
    ax.legend(fontsize=10, loc='upper right')

def plot_oscillation_diagram(ax):
    """Draw a schematic time series of predator-prey oscillations"""

    # Generate example oscillation data
    t = np.linspace(0, 40, 400)

    # Prey population: sinusoidal oscillation
    prey_amp = 0.6
    prey_period = 10
    prey = 1 + prey_amp * np.sin(2*np.pi*t/prey_period - np.pi/4)

    # Predator population: cosine oscillation (lagging the prey)
    predator_amp = 0.4
    predator = 1 + predator_amp * np.cos(2*np.pi*t/prey_period - np.pi/4)

    # Plot time series
    ax.plot(t, prey, 'b-', linewidth=2, label='Prey population')
    ax.plot(t, predator, 'r-', linewidth=2, label='Predator population')

    # Mark key features
    # Prey peak
    prey_max_idx = np.argmax(prey)
    ax.plot(t[prey_max_idx], prey[prey_max_idx], 'bo', markersize=8)
    # Label moved to lower left
    ax.annotate('Prey peak', xy=(t[prey_max_idx], prey[prey_max_idx]),
               xytext=(t[prey_max_idx]-8, prey[prey_max_idx]-0.3),
               arrowprops=dict(arrowstyle='->', color='blue'),
               fontsize=10, color='blue', ha='center')

    # Predator peak (lagging the prey)
    predator_max_idx = np.argmax(predator)
    ax.plot(t[predator_max_idx], predator[predator_max_idx], 'ro', markersize=8)
    # Label moved to lower right
    ax.annotate('Predator peak', xy=(t[predator_max_idx], predator[predator_max_idx]),
               xytext=(t[predator_max_idx]+8, predator[predator_max_idx]-0.3),
               arrowprops=dict(arrowstyle='->', color='red'),
               fontsize=10, color='red', ha='center')

    # Phase-lag annotation (placed below)
    lag = t[predator_max_idx] - t[prey_max_idx]
    y_lag_pos = 0.9
    ax.annotate('', xy=(t[prey_max_idx], y_lag_pos),
               xytext=(t[predator_max_idx], y_lag_pos),
               arrowprops=dict(arrowstyle='<->', color='purple', linewidth=1.5))
    ax.text((t[prey_max_idx]+t[predator_max_idx])/2, y_lag_pos - 0.25,
           f'Phase lag\n{lag:.1f} time units',
           ha='center', fontsize=10, color='purple')

    # Shade spans to show the period
    period = prey_period
    for i in range(0, int(t[-1]), period):
        if i + period <= t[-1]:
            ax.axvspan(i, i+period, alpha=0.1, color='gray')
            if i == 0:
                ax.text(i+period/2, 0.2, 'One period', ha='center', fontsize=10)

    ax.set_xlabel('Time (τ)', fontsize=12)
    ax.set_ylabel('Population', fontsize=12)
    ax.set_title('Predator-Prey Oscillations', fontsize=14)
    ax.grid(True, alpha=0.3, linestyle='--')
    ax.legend(fontsize=11, loc='upper right')

    # Add explanatory text
    ax.text(0.02, 0.98, 'Key observations:\n1. Predator lags behind prey\n2. Oscillations are periodic\n3. Amplitude depends on initial conditions',
           transform=ax.transAxes, fontsize=10, verticalalignment='top',
           bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))

# Create predator-prey schematics
fig, axes = plt.subplots(2, 2, figsize=(14, 12))

# Top left: classic Lotka-Volterra model
plot_predator_prey_schematic(axes[0, 0], alpha=1.0, beta=1.0, gamma=0.0)

# Top right: model with density dependence
plot_predator_prey_schematic(axes[0, 1], alpha=0.8, beta=0.7, gamma=0.3)

# Bottom left: oscillation time series
plot_oscillation_diagram(axes[1, 0])

# Bottom right: limit cycle in the phase plane
ax4 = axes[1, 1]
# Draw a schematic limit cycle
theta = np.linspace(0, 2*np.pi, 200)
# Limit-cycle radius as a function of angle
def get_r_lc(th):
    return 0.6 + 0.1 * np.sin(5*th)

r = get_r_lc(theta)  # Non-circular limit cycle
x_lc = 1 + r * np.cos(theta)
y_lc = 1 + r * np.sin(theta)

ax4.plot(x_lc, y_lc, 'purple', linewidth=2, label='Limit cycle')

# Add inner and outer trajectories, constructed so they approach the limit cycle
# Inner trajectory (spirals outward to the limit cycle)
t_vals = np.linspace(0, 4*np.pi, 500)
# Scale factor grows toward 1 (e.g. from 0.2x to 1.0x the radius)
scale_inner = 1.0 - 0.8 * np.exp(-0.15 * t_vals)
r_inner_base = get_r_lc(t_vals)
r_inner = r_inner_base * scale_inner
x_inner = 1 + r_inner * np.cos(t_vals)
y_inner = 1 + r_inner * np.sin(t_vals)
ax4.plot(x_inner, y_inner, 'green', linewidth=1.5, alpha=0.7, label='Inner trajectory')

# Outer trajectory (spirals inward to the limit cycle)
t_vals_outer = np.linspace(0, 4*np.pi, 500)
theta_outer = t_vals_outer + np.pi  # Offset the phase slightly
# Scale factor shrinks toward 1 (e.g. from 1.8x to 1.0x the radius)
scale_outer = 1.0 + 0.8 * np.exp(-0.15 * t_vals_outer)
r_outer_base = get_r_lc(theta_outer)
r_outer = r_outer_base * scale_outer
x_outer = 1 + r_outer * np.cos(theta_outer)
y_outer = 1 + r_outer * np.sin(theta_outer)
ax4.plot(x_outer, y_outer, 'orange', linewidth=1.5, alpha=0.7, label='Outer trajectory')

# Mark the equilibrium
ax4.plot(1, 1, 'ro', markersize=10, markeredgecolor='black',
        markeredgewidth=1, label='Unstable equilibrium')

# Add vector-field arrows: a rotating flow attracted to the limit cycle
x_grid, y_grid = np.meshgrid(np.linspace(0.2, 1.8, 12), np.linspace(0.2, 1.8, 12))

for i in range(len(x_grid)):
    for j in range(len(y_grid)):
        x, y = x_grid[i, j], y_grid[i, j]
        u, v = x - 1, y - 1
        r_curr = np.sqrt(u**2 + v**2)
        if r_curr == 0: continue

        # Limit-cycle radius at the current angle
        th = np.arctan2(v, u)
        r_target = get_r_lc(th)

        # Radial component (toward the limit cycle)
        radial_strength = 0.8 * (r_target - r_curr)
        u_rad = radial_strength * np.cos(th)
        v_rad = radial_strength * np.sin(th)

        # Tangential component (counter-clockwise rotation)
        tangential_strength = 0.5 * r_curr
        u_tan = -tangential_strength * np.sin(th)
        v_tan = tangential_strength * np.cos(th)

        dx = u_rad + u_tan
        dy = v_rad + v_tan

        norm = np.sqrt(dx**2 + dy**2) + 1e-10
        ax4.arrow(x, y, 0.08*dx/norm, 0.08*dy/norm,
                 head_width=0.03, head_length=0.05, fc='gray', ec='gray', alpha=0.4)

ax4.set_xlim(0, 2)
ax4.set_ylim(0, 2)
ax4.set_xlabel('Prey population (x)', fontsize=12)
ax4.set_ylabel('Predator population (y)', fontsize=12)
ax4.set_title('Ideal Limit Cycle in Phase Plane (Not Lotka-Volterra)', fontsize=14)
ax4.grid(True, alpha=0.3, linestyle='--')
ax4.legend(fontsize=10, loc='upper right')

# Add explanatory text
ax4.text(0.02, 0.98, 'Limit cycle characteristics:\n1. Stable periodic solution\n2. Attracts nearby trajectories\n3. Independent of initial conditions',
        transform=ax4.transAxes, fontsize=10, verticalalignment='top',
        bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))

plt.tight_layout(h_pad=3.0)
