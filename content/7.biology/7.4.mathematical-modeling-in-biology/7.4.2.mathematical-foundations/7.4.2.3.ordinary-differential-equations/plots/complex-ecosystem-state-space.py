"""
complex_ecosystem_schematic.py
Schematic of a complex ecosystem (competition + predation)
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from scipy.integrate import solve_ivp

def plot_3d_state_space(ax):
    """Draw a schematic 3D state space"""

    # Set view angle
    ax.view_init(elev=25, azim=45)

    # Create grid
    u1 = np.linspace(0, 1, 20)
    u2 = np.linspace(0, 1, 20)
    v = np.linspace(0, 1, 20)

    # Axis labels
    ax.set_xlabel('Species 1 ($u_1$)', fontsize=12, labelpad=10)
    ax.set_ylabel('Species 2 ($u_2$)', fontsize=12, labelpad=10)
    ax.set_zlabel('Predator ($v$)', fontsize=12, labelpad=10)
    ax.set_title('3D State Space of Complex Ecosystem', fontsize=16)

    # Draw key planes
    # Plane 1: u1 = 0 (species 1 extinct)
    U2, V = np.meshgrid(u2, v)
    ax.plot_surface(np.zeros_like(U2), U2, V, alpha=0.1, color='red')

    # Plane 2: u2 = 0 (species 2 extinct)
    U1, V = np.meshgrid(u1, v)
    ax.plot_surface(U1, np.zeros_like(U1), V, alpha=0.1, color='blue')

    # Plane 3: v = 0 (predator extinct)
    U1, U2 = np.meshgrid(u1, u2)
    ax.plot_surface(U1, U2, np.zeros_like(U1), alpha=0.1, color='green')

    # Draw example trajectories
    # Trajectory 1: competitive exclusion (species 2 goes extinct)
    t1 = np.linspace(0, 4*np.pi, 200)
    u1_traj1 = 0.5 + 0.3 * np.tanh(t1/2) * np.sin(t1)
    # Converges onto the (u1,0,v) plane
    u2_traj1 = 0.4 * np.exp(-0.5*t1)
    v_traj1 = 0.3 + 0.2 * np.cos(t1)
    ax.plot(u1_traj1, u2_traj1, v_traj1, 'r-', linewidth=2.5, label='Competitive exclusion', alpha=0.9)
    # Mark the end point
    ax.scatter(u1_traj1[-1], u2_traj1[-1], v_traj1[-1], color='red', s=50)

    # Trajectory 2: predator-mediated coexistence (inward spiral or closed loop)
    t2 = np.linspace(0, 6*np.pi, 300)
    # Slowly converging spiral
    decay = np.exp(-0.05*t2)
    u1_center, u2_center, v_center = 0.4, 0.4, 0.4
    u1_traj2 = u1_center + 0.2 * decay * np.sin(t2)
    u2_traj2 = u2_center + 0.2 * decay * np.sin(t2 + 2*np.pi/3)
    v_traj2 = v_center + 0.2 * decay * np.sin(t2 + 4*np.pi/3)
    ax.plot(u1_traj2, u2_traj2, v_traj2, 'b-', linewidth=2.5, label='Stable coexistence', alpha=0.9)
    # Mark the centre point
    ax.scatter(u1_center, u2_center, v_center, color='blue', s=50, marker='*')

    # Trajectory 3: chaotic trajectory (Hastings-Powell three-species food chain)
    # Also a generalized Lotka-Volterra system, famous for its complex chaotic attractor
    def ecological_chaos_gen(t_max=5000):
        # Parameters of the well-known "teacup" chaotic attractor (Hastings & Powell, 1991)
        # x: Resource, y: Consumer, z: Top predator

        # Parameters
        a1, b1 = 5.0, 3.0    # resource -> consumer
        a2, b2 = 0.1, 2.0    # consumer -> top predator
        d1 = 0.4             # consumer mortality
        d2 = 0.01            # top predator mortality

        def equations(t, state):
            x, y, z = state
            # Enforce non-negativity
            if x < 0: x = 0
            if y < 0: y = 0
            if z < 0: z = 0

            # Functional responses (Holling type II)
            func1 = a1 * x / (1 + b1 * x)
            func2 = a2 * y / (1 + b2 * y)

            # Dynamics
            # dx/dt = x(1-x) - f1(x)y
            dxdt = x * (1 - x) - func1 * y
            # dy/dt = f1(x)y - f2(y)z - d1*y
            dydt = func1 * y - func2 * z - d1 * y
            # dz/dt = f2(y)z - d2*z
            dzdt = func2 * z - d2 * z

            return [dxdt, dydt, dzdt]

        # Long time span so the chaotic orbit is densely traced
        t_eval = np.linspace(0, t_max, 20000)
        sol = solve_ivp(equations, [0, t_max], [0.5, 0.1, 9.0], t_eval=t_eval, rtol=1e-8, atol=1e-8)

        # Prepare data for plotting
        # Discard the first 20% as transient and keep the attractor shape
        start_idx = int(len(sol.t) * 0.2)

        x_raw = sol.y[0][start_idx:]
        y_raw = sol.y[1][start_idx:]
        z_raw = sol.y[2][start_idx:]

        # Rescale into the current plot coordinates (0-1)
        # In Hastings-Powell, x is in 0-1, y roughly 0-0.5, z roughly 7-10
        u1_out = x_raw
        u2_out = y_raw * 2.0  # Stretch y for visibility
        v_out = (z_raw - 4.0) / 8.0 # Map z into the 0-1 range

        return u1_out, u2_out, v_out

    u1_traj3, u2_traj3, v_traj3 = ecological_chaos_gen(t_max=3000)
    ax.plot(u1_traj3, u2_traj3, v_traj3, 'g-', linewidth=0.6, alpha=0.7, label='Chaos')

    ax.legend(fontsize=10, loc='upper right', bbox_to_anchor=(1.1, 1.0))

    # Remove grey pane fill for a cleaner look
    ax.xaxis.pane.fill = False
    ax.yaxis.pane.fill = False
    ax.zaxis.pane.fill = False

    # Add an explanatory text box
    ax.text2D(0.02, 0.1,
              'System Behaviors:\n'
              '• Red: Exclusion ($u_2 \\to 0$)\n'
              '• Blue: Stable Point\n'
              '• Green: Strange Attractor',
              transform=ax.transAxes, fontsize=10,
              bbox=dict(boxstyle='round', facecolor='white', alpha=0.8, edgecolor='gray'))

# Create the complex ecosystem schematic
fig = plt.figure(figsize=(10, 8))

# 3D state space
ax1 = fig.add_subplot(111, projection='3d')
plot_3d_state_space(ax1)

plt.tight_layout()
