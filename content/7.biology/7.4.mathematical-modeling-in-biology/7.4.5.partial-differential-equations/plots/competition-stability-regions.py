"""
heterogeneous_competition_model.py
Numerical simulation of a competition model in a heterogeneous environment
Verifies the theorem: effect of diffusion coefficients on the outcome of competition
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.sparse import diags
from scipy.sparse.linalg import spsolve
from scipy.linalg import eigvals

class HeterogeneousCompetitionModel:
    """Solver for a competition model in a heterogeneous environment"""

    def __init__(self, L=10.0, Nx=201, m_type='sinusoidal'):
        """
        Initialise competition model parameters

        Parameters:
        L : length of the spatial domain
        Nx : number of spatial grid points
        m_type : type of resource distribution
        """
        self.L = L
        self.Nx = Nx
        self.x = np.linspace(0, L, Nx)
        self.dx = self.x[1] - self.x[0]

        # Resource distribution function m(x)
        self.m = self._resource_function(m_type)

        # Default parameters
        self.b = 0.8  # competition coefficient
        self.c = 0.9  # competition coefficient

    def _resource_function(self, m_type):
        """Resource distribution function m(x)"""
        if m_type == 'sinusoidal':
            return 1.0 + 0.5 * np.sin(2 * np.pi * self.x / self.L)
        elif m_type == 'gaussian':
            center = self.L / 2
            return 1.0 + 0.8 * np.exp(-(self.x - center)**2 / 2)
        elif m_type == 'step':
            m = np.ones_like(self.x)
            m[self.x < self.L/3] = 0.5
            m[self.x > 2*self.L/3] = 0.5
            return m
        else:
            raise ValueError(f"Unknown resource distribution type: {m_type}")

    def construct_laplacian_matrix(self, d):
        """Build the matrix representation of the Laplacian (Neumann boundary conditions)"""
        N = self.Nx
        alpha = d / (self.dx ** 2)

        # Main diagonal
        main_diag = -2 * alpha * np.ones(N)
        # Off-diagonals
        off_diag = alpha * np.ones(N-1)

        # Neumann boundary conditions: zero-flux boundaries
        main_diag[0] = -alpha  # left boundary
        main_diag[-1] = -alpha  # right boundary

        # Build the tridiagonal matrix
        A = diags([off_diag, main_diag, off_diag], [-1, 0, 1], format='csr')
        return A

    def single_species_equilibrium(self, d):
        """Solve for the single-species equilibrium u* using Newton's method"""
        N = self.Nx
        # Initial guess
        u = np.ones(N) * np.mean(self.m)

        # Newton iterations
        for i in range(20):
            # A corresponds to d * d^2/dx^2
            A = self.construct_laplacian_matrix(d)

            # F(u) = A*u + u*(m-u) = 0
            F = A.dot(u) + u * (self.m - u)

            if np.linalg.norm(F, np.inf) < 1e-10:
                break                

            # Jacobian J = A + diag(m - 2u)
            diag_reaction = diags([self.m - 2*u], [0], format='csr')
            J = A + diag_reaction

            # Solve J * delta = -F
            try:
                delta = spsolve(J, -F)
                u += delta
                u = np.maximum(u, 1e-9) # Enforce positivity
            except Exception:
                break

        return u

    def _integrate(self, y, x):
        """Numerical integration (trapezoidal rule) helper"""
        dx = x[1] - x[0]
        # compatible with 2D array (axis 1) or 1D array
        if y.ndim == 1:
            return np.sum(y) * dx - 0.5 * dx * (y[0] + y[-1])
        else:
            return np.sum(y, axis=1) * dx - 0.5 * dx * (y[:, 0] + y[:, -1])

    def calculate_c_star(self, d_values):
        """Compute c* = inf_{d>0} ∫m / ∫u*"""
        ratios = []

        for d in d_values:
            u_star = self.single_species_equilibrium(d)
            total_m = self._integrate(self.m, self.x)
            total_u = self._integrate(u_star, self.x)
            ratios.append(total_m / total_u)

        c_star = min(ratios)
        d_opt = d_values[np.argmin(ratios)]

        return c_star, d_opt, ratios

    def stability_of_semi_trivial_solution(self, d, D, c):
        """Compute the stability of the semi-trivial solution (u*, 0)"""
        # First compute u*
        u_star = self.single_species_equilibrium(d)

        # Build the linearised operator matrix
        N = self.Nx
        A = self.construct_laplacian_matrix(D)

        # Add the diagonal part of the reaction term
        diag_elements = self.m - c * u_star
        M = A + diags([diag_elements], [0], format='csr')

        # Compute eigenvalues with a dense matrix (more robust than ARPACK)
        M_dense = M.todense()
        evals = eigvals(M_dense)

        # Dynamic stability: look at the largest real part (max Lyapunov exponent)
        # lambda > 0 => unstable (v invades)
        # lambda < 0 => stable (u wins)
        lambda_max = np.max(np.real(evals))

        # To match the original logic (positive => stable in the plots), return -lambda_max
        # so that: metric > 0 -> Stable, metric < 0 -> Unstable
        metric = -lambda_max

        return metric, u_star

    def simulate_competition(self, d, D, b, c, T=100.0, dt=None):
        """
        Simulate the competition dynamics

        Parameter dt: if None, computed automatically from the stability condition
        """
        # Automatically choose a time step that satisfies the stability condition
        # d * dt / dx^2 <= 0.5  =>  dt <= 0.5 * dx^2 / max(d, D)
        max_diff = max(d, D)
        dt_stable = 0.45 * (self.dx ** 2) / max_diff

        if dt is None or dt > dt_stable:
            print(f"Adjusting time step for stability: {dt} -> {dt_stable:.6f} (max D={max_diff})")
            dt = dt_stable

        N = self.Nx
        Nt = int(T / dt)

        # Initial conditions
        u = 0.5 * np.ones(N) + 0.1 * np.random.randn(N)
        v = 0.5 * np.ones(N) + 0.1 * np.random.randn(N)

        # Diffusion matrices
        A_u = self.construct_laplacian_matrix(d)
        A_v = self.construct_laplacian_matrix(D)

        # Precomputed constants
        # Explicit Euler: u_new = u + dt * (A*u + f(u))
        # Matrix A already includes the 1/dx^2 factor

        u_history = []
        v_history = []

        # Save every so many steps, about 200 frames in total
        save_interval = max(1, int(Nt / 200))

        u_history.append(u.copy())
        v_history.append(v.copy())

        for n in range(1, Nt):
            # Reaction terms
            # Clip values to prevent overflow
            u_safe = np.clip(u, 0, 1e5)
            v_safe = np.clip(v, 0, 1e5)

            reaction_u = u_safe * (self.m - u_safe - b * v_safe)
            reaction_v = v_safe * (self.m - c * u_safe - v_safe)

            # Update (A is d * d2/dx2)
            # Note: construct_laplacian_matrix returns d/dx^2 * [1, -2, 1]
            diff_u = A_u.dot(u)
            diff_v = A_v.dot(v)

            u = u + dt * (diff_u + reaction_u)
            v = v + dt * (diff_v + reaction_v)

            # Ensure non-negativity
            u = np.maximum(u, 0)
            v = np.maximum(v, 0)

            # Save results
            if n % save_interval == 0:
                u_history.append(u.copy())
                v_history.append(v.copy())

        # Make sure the last step is saved as well
        u_history.append(u.copy())
        v_history.append(v.copy())

        return np.array(u_history), np.array(v_history)

    def analyze_competition_outcomes(self, d_values, D_values, b, c):
        """Analyse competition outcomes: plot the region Σ"""
        stability_matrix = np.zeros((len(d_values), len(D_values)))

        for i, d in enumerate(d_values):
            for j, D in enumerate(D_values):
                val, _ = self.stability_of_semi_trivial_solution(d, D, c)
                # val > 0: (u*, 0) stable -> u wins
                # val < 0: (u*, 0) unstable -> coexistence or v wins
                stability_matrix[i, j] = 1 if val > 0 else -1

        return stability_matrix

    def plot_competition_dynamics(self, d, D, b, c):
        """Plot the competition dynamics"""
        print(f"Simulating dynamics for d={d}, D={D}...")
        u_history, v_history = self.simulate_competition(d, D, b, c, T=200.0)

        # Compute the stability metric
        # Compare using the integrals at the final time
        u_final_total = np.sum(u_history[-1]) * self.dx
        v_final_total = np.sum(v_history[-1]) * self.dx

        # Define metric: >0 means u wins, <0 means v wins
        metric = (u_final_total - v_final_total) / (u_final_total + v_final_total + 1e-10)

        fig, axes = plt.subplots(2, 3, figsize=(15, 10))

        # 1. Final spatial distribution
        ax = axes[0, 0]
        u_final = u_history[-1]
        v_final = v_history[-1]
        ax.plot(self.x, u_final, 'b-', linewidth=2, label='Species u (d={})'.format(d))
        ax.plot(self.x, v_final, 'r-', linewidth=2, label='Species v (D={})'.format(D))
        ax.plot(self.x, self.m, 'k:', linewidth=1.5, label='Resource m(x)', alpha=0.5)
        ax.set_xlabel('Position (x)', fontsize=12)
        ax.set_ylabel('Population density', fontsize=12)
        ax.set_title(f'Final Distribution (T=200)', fontsize=14)
        ax.legend(fontsize=10)
        ax.grid(True, alpha=0.3)

        # 2. Time evolution (spatial mean)
        ax = axes[0, 1]
        # Plot only if history is non-empty
        if len(u_history) > 0:
            time_points = np.linspace(0, 200, len(u_history))
            u_mean = np.mean(u_history, axis=1)
            v_mean = np.mean(v_history, axis=1)

            ax.plot(time_points, u_mean, 'b-', linewidth=2, label='Mean u')
            ax.plot(time_points, v_mean, 'r-', linewidth=2, label='Mean v')
            ax.set_xlabel('Time', fontsize=12)
            ax.set_ylabel('Mean Density', fontsize=12)
            ax.set_title('Mean Density Dynamics', fontsize=14)
            ax.legend(fontsize=10)
            ax.grid(True, alpha=0.3)

        # 3. Total biomass
        ax = axes[0, 2]
        if len(u_history) > 0:
            u_total = np.sum(u_history, axis=1) * self.dx
            v_total = np.sum(v_history, axis=1) * self.dx

            ax.plot(time_points, u_total, 'b-', linewidth=2, label='Total u')
            ax.plot(time_points, v_total, 'r-', linewidth=2, label='Total v')
            ax.set_xlabel('Time', fontsize=12)
            ax.set_ylabel('Total Biomass', fontsize=12)
            ax.set_title('Total Biomass Dynamics', fontsize=14)
            ax.legend(fontsize=10)
            ax.grid(True, alpha=0.3)

        # 4. Space-time plot for u
        ax = axes[1, 0]
        if len(u_history) > 0:
            # Downsample to avoid slow plotting
            skip = max(1, len(u_history) // 100)
            im = ax.imshow(u_history[::skip], aspect='auto', cmap='Blues', 
                          extent=[0, self.L, 200, 0], vmin=0, vmax=np.max(self.m))
            ax.set_xlabel('Position', fontsize=12)
            ax.set_ylabel('Time', fontsize=12)
            ax.set_title('Spatiotemporal Dynamics of u', fontsize=14)
            plt.colorbar(im, ax=ax, label='Density')

        # 5. Space-time plot for v
        ax = axes[1, 1]
        if len(v_history) > 0:
            skip = max(1, len(v_history) // 100)
            im = ax.imshow(v_history[::skip], aspect='auto', cmap='Reds', 
                          extent=[0, self.L, 200, 0], vmin=0, vmax=np.max(self.m))
            ax.set_xlabel('Position', fontsize=12)
            ax.set_ylabel('Time', fontsize=12)
            ax.set_title('Spatiotemporal Dynamics of v', fontsize=14)
            plt.colorbar(im, ax=ax, label='Density')

        # 6. Phase portrait (u vs v at center)
        ax = axes[1, 2]
        if len(u_history) > 0:
            center_idx = self.Nx // 2
            u_center = u_history[:, center_idx]
            v_center = v_history[:, center_idx]
            ax.plot(u_center, v_center, 'k-', alpha=0.6)
            ax.plot(u_center[0], v_center[0], 'go', label='Start') # Start
            ax.plot(u_center[-1], v_center[-1], 'ro', label='End') # End
            ax.set_xlabel('u(center)', fontsize=12)
            ax.set_ylabel('v(center)', fontsize=12)
            ax.set_title('Phase Portrait (Center point)', fontsize=14)
            ax.grid(True, alpha=0.3)
            ax.legend()

        plt.tight_layout()

        # Return u_final, v_final and metric
        return u_final, v_final, metric

        ax.set_xlabel('Time', fontsize=12)
        ax.set_ylabel('Total biomass', fontsize=12)
        ax.set_title('Total Biomass Over Time', fontsize=14)
        ax.legend(fontsize=11)
        ax.grid(True, alpha=0.3)

        # 4. Phase portrait: total u vs total v
        ax = axes[1, 0]
        ax.plot(u_total, v_total, 'k-', linewidth=1.5, alpha=0.7)
        ax.scatter(u_total[0], v_total[0], color='green', s=100, 
                  label='Start', zorder=5)
        ax.scatter(u_total[-1], v_total[-1], color='red', s=100, 
                  label='End', zorder=5)
        ax.set_xlabel('Total u', fontsize=12)
        ax.set_ylabel('Total v', fontsize=12)
        ax.set_title('Phase Portrait', fontsize=14)
        ax.legend(fontsize=11)
        ax.grid(True, alpha=0.3)

        # 5. Time series of the spatial distribution (heat map)
        ax = axes[1, 1]
        im = ax.imshow(u_history.T, aspect='auto', cmap='Blues',
                      extent=[0, 200, 0, self.L], origin='lower')
        ax.set_xlabel('Time', fontsize=12)
        ax.set_ylabel('Position (x)', fontsize=12)
        ax.set_title('Spatio-temporal Dynamics of u', fontsize=14)
        plt.colorbar(im, ax=ax, label='Density')

        # 6. Stability analysis
        ax = axes[1, 2]
        lambda_val, u_star = self.stability_of_semi_trivial_solution(d, D, c)

        ax.plot(self.x, u_star, 'b-', linewidth=2, label='u* (semi-trivial)')
        ax.plot(self.x, self.m, 'g--', linewidth=1.5, label='m(x)', alpha=0.7)
        ax.fill_between(self.x, 0, u_star, alpha=0.3, color='blue')
        ax.set_xlabel('Position (x)', fontsize=12)
        ax.set_ylabel('Density', fontsize=12)
        ax.set_title(f'Semi-trivial Solution\nMetric = {lambda_val:.4f}', fontsize=14)
        ax.legend(fontsize=11)
        ax.grid(True, alpha=0.3)

        # Determine stability (metric > 0 -> Stable)
        if lambda_val > 1e-6:
            stability = "Stable (u wins)"
            color = 'blue'
        elif lambda_val < -1e-6:
            stability = "Unstable (coexistence or v wins)"
            color = 'red'
        else:
            stability = "Neutral"
            color = 'gray'

        ax.text(0.05, 0.95, stability, transform=ax.transAxes, 
                fontsize=12, verticalalignment='top',
                bbox=dict(boxstyle='round', facecolor=color, alpha=0.3))

        plt.tight_layout()

        return u_final, v_final, lambda_val

def verify_theorem():
    """Verify the theorem: competition outcomes in a heterogeneous environment"""
    print("Verifying Theorem...")

    # Create the model
    model = HeterogeneousCompetitionModel(L=10.0, Nx=201, m_type='sinusoidal')

    # Compute c*
    d_values = np.logspace(-2, 2, 50)
    c_star, d_opt, ratios = model.calculate_c_star(d_values)

    print(f"c* = inf_d ∫m/∫u* = {c_star:.4f} at d={d_opt:.4f}")

    # Choose different values of c for simulation
    b = 0.8  # fix b
    # We choose three representative values:
    # 1. c < c* (clearly smaller; (u*,0) should be mostly unstable)
    # 2. c slightly above c* (a clear stability boundary d=D should be visible)
    # 3. c well above c* (strong competition; the advantage of the slow diffuser is more pronounced)
    c_values = [0.8 * c_star, 1.05 * c_star, 1.3 * c_star]

    fig, axes = plt.subplots(1, 3, figsize=(18, 5)) # changed to a 1x3 layout

    for i, c in enumerate(c_values):
        print(f"\nSimulating with c={c:.3f} (c*={c_star:.3f})")

        # Analyse the stability region Σ
        d_test = np.logspace(-1, 1, 25) # slightly higher resolution
        D_test = np.logspace(-1, 1, 25)

        stability = model.analyze_competition_outcomes(d_test, D_test, b, c)

        # Plot the stability region
        ax = axes[i]
        im = ax.imshow(stability, cmap='RdYlBu', extent=[np.log10(D_test[0]), np.log10(D_test[-1]), 
                                                         np.log10(d_test[0]), np.log10(d_test[-1])],
                      aspect='auto', origin='lower', vmin=-1, vmax=1)

        # Add the d=D line
        x_vals = np.linspace(np.log10(D_test[0]), np.log10(D_test[-1]), 10)
        ax.plot(x_vals, x_vals, 'k--', linewidth=1.5, alpha=0.6, label='d=D')

        ax.set_xlabel('log10(D)', fontsize=12)
        ax.set_ylabel('log10(d)', fontsize=12)
        ax.set_title(f'Stability Region Σ\nc={c:.3f} (ratio={c/c_star:.2f} c*)', fontsize=14)

        # Add a colour bar
        if i == 2:
            cbar = plt.colorbar(im, ax=ax)
            cbar.set_label('Stability of (u*,0)', fontsize=12)
            cbar.set_ticks([-1, 0, 1])
            cbar.set_ticklabels(['Unstable (v invades)', 'Neutral', 'Stable (u persistent)'])

        ax.legend(fontsize=10, loc='upper right')
        ax.grid(True, alpha=0.3)

        # Simulate a specific point
        if c > c_star:
            # Choose a point inside Σ
            d = 0.3
            D = 1.0
            print(f"  Testing point (d={d}, D={D}) in Σ")
        else:
            # Choose a point outside Σ
            d = 1.0
            D = 0.3
            print(f"  Testing point (d={d}, D={D}) outside Σ")

        lambda_val, _ = model.stability_of_semi_trivial_solution(d, D, c)
        print(f"  Metric = {lambda_val:.4f} (positive means stable/u wins)")

    plt.tight_layout()

    # Simulate the special case of the theorem: b=c=1
    print("\n" + "="*60)
    print("SIMULATING THEOREM: b=c=1")
    print("="*60)

    b = 1.0
    c = 1.0

    # Case 1: d < D
    d1, D1 = 0.5, 1.0
    print(f"\nCase 1: d={d1} < D={D1}")
    u_final1, v_final1, lambda1 = model.plot_competition_dynamics(d1, D1, b, c)
    print(f"  Metric = {lambda1:.4f}")

    # Case 2: d > D
    d2, D2 = 1.0, 0.5
    print(f"\nCase 2: d={d2} > D={D2}")
    u_final2, v_final2, lambda2 = model.plot_competition_dynamics(d2, D2, b, c)
    print(f"  Metric = {lambda2:.4f}")

    # Case 3: d = D
    d3, D3 = 1.0, 1.0
    print(f"\nCase 3: d={d3} = D={D3}")
    u_final3, v_final3, lambda3 = model.plot_competition_dynamics(d3, D3, b, c)
    print(f"  Metric = {lambda3:.4f}")

verify_theorem()
