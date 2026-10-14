"""
advection_competition_model.py
Numerical simulation of a competition model with advection
Verifies the theorem: effect of the advection coefficient on the outcome of competition
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.sparse import diags, csr_matrix
from scipy.sparse.linalg import spsolve

class AdvectionCompetitionModel:
    """Solver for a competition model with advection"""

    def __init__(self, L=10.0, Nx=61):
        """
        Initialise model parameters

        Parameters:
        L : length of the spatial domain
        Nx : number of spatial grid points
        """
        self.L = L
        self.Nx = Nx
        self.x = np.linspace(0, L, Nx)
        self.dx = self.x[1] - self.x[0]

        # Resource distribution function m(x)
        self.m = self._resource_function()

        # Compute the resource gradient
        self.m_grad = np.gradient(self.m, self.dx)

        # Default parameters
        self.d = 1.0  # diffusion coefficient of species u
        self.D = 1.0  # diffusion coefficient of species v

    def _resource_function(self):
        """Resource distribution function m(x) - heterogeneous distribution"""
        # Several local maxima
        m = 1.0 + 0.5 * np.sin(2 * np.pi * self.x / self.L)
        m += 0.3 * np.exp(-(self.x - self.L/4)**2)
        m += 0.3 * np.exp(-(self.x - 3*self.L/4)**2)
        return m

    def construct_advection_diffusion_matrix(self, d, alpha):
        """Build the matrix representation of the diffusion-advection operator
        Uses a conservative upwind scheme to ensure numerical stability
        """
        N = self.Nx
        dx = self.dx

        # 1. Diffusion part (d * u_xx)
        # ------------------------------------------------
        alpha_diff = d / (dx ** 2)
        main_diag = -2 * alpha_diff * np.ones(N)
        upper_diag = alpha_diff * np.ones(N-1)
        lower_diag = alpha_diff * np.ones(N-1)

        # 2. Advection part (- div(alpha * u * grad(m)))
        # ------------------------------------------------

        # Initialise advection variables
        factor = 1.0 / dx
        v_plus = np.zeros(N-1)
        v_minus = np.zeros(N-1)

        if alpha > 1e-10:
            # Compute velocities at cell interfaces v = alpha * m'
            # m has N points, m[0]...m[N-1]
            # there are N-1 interfaces: 0.5, 1.5, ..., N-1.5
            # v_{i+1/2} corresponds to index i (0 to N-2)

            m_diff = np.diff(self.m) # m[i+1] - m[i]
            v_interface = alpha * m_diff / dx

            # Contribution of upwind fluxes to the matrix
            # J_{i+1/2} = max(v,0)*u_i + min(v,0)*u_{i+1}
            # term at i:   - J_{i+1/2} / dx  => -1/dx * (v+ u_i + v- u_{i+1})
            # term at i+1: + J_{i+1/2} / dx  => +1/dx * (v+ u_i + v- u_{i+1})

            v_plus = np.maximum(v_interface, 0)
            v_minus = np.minimum(v_interface, 0)

            factor = 1.0 / dx

            # Contribution to the main diagonal (u_i)
            # from -J_{i+1/2}: -factor * v_plus[i]
            # from +J_{i-1/2}: +factor * v_minus[i-1]
            main_diag[:-1] -= factor * v_plus
            main_diag[1:]  += factor * v_minus

            # Contribution to the upper diagonal (u_{i+1})
            # from -J_{i+1/2}: -factor * v_minus[i] (row i, column i+1)
            upper_diag[:] -= factor * v_minus

            # Contribution to the lower diagonal (u_{i-1})
            # from +J_{i-1/2}: +factor * v_plus[i-1] (row i, column i-1)
            lower_diag[:] += factor * v_plus

        # 3. Boundary conditions (Neumann zero-flux)
        # ------------------------------------------------
        # Boundary correction for the diffusion part
        main_diag[0] += alpha_diff   # u_(-1) = u_1 (mirror) -> -2a u_0 + a u_1 + a u_(-1) -> -2a u_0 + 2a u_1 (Error in std logical?)
        # Std Neumann: (u_1 - u_(-1))/2dx = 0 => u_(-1) = u_1.
        # Laplacian at 0: (u_1 - 2u_0 + u_(-1))/dx^2 = (2u_1 - 2u_0)/dx^2.
        # Original code had: main_diag[0] = -alpha_diff, off_diag=alpha. (-1, 1).
        # This corresponds to forward difference u_xx ~ (u_1 - u_0)/dx^2 ? No.
        # Let's stick to the original diffusion boundary logic which was:
        # main_diag[0] = -alpha_diff (-1), off_diag (1). Sum = 0. Conservative.

        # Reset boundary elements for diffusion to match original simple implementation
        # The original implementation:
        # main_diag[0] = -alpha_diff
        # main_diag[-1] = -alpha_diff
        # This implies flux = 0 at boundary naturally?
        # J_diff = -d du/dx. 
        # Finite volume: div J at 0. J_{1/2} - J_{-1/2}. J_{-1/2}=0.
        # J_{1/2} = -d (u_1 - u_0)/dx.
        # -div J = - (J_{1/2} - 0)/dx = d(u_1-u_0)/dx^2 = alpha(u_1 - u_0).
        # Matrix row 0: -alpha u_0 + alpha u_1. Correct.

        # So we just need to ensure advection flux is also 0 at boundary.
        # J_adv_{-1/2} = 0, J_adv_{N-1/2} = 0.
        # My loops above for advection cover indices 0 to N-2 (interfaces).
        # Interface i=0 corresponds to x_{0.5}.
        # Wait, indices. v_interface has N-1 elements. 0..N-2.
        # i=0 is between node 0 and 1.
        # Node 0 update: - (J_{0.5} - J_{-0.5})/dx.
        # We assume J_{-0.5}=0 (BC).
        # So Node 0 gets -J_{0.5}/dx.
        # J_{0.5} = v+ u_0 + v- u_1.
        # Row 0: coeff u_0 is -v+_0/dx. coeff u_1 is -v-_0/dx.
        # This is handled by `main_diag[:-1] -= ...` (at i=0) and `upper_diag[:] -= ...` (at i=0).
        # Correct.

        # Node N-1 update: - (J_{N-1/2} - J_{N-1.5})/dx.
        # Assume J_{N-1/2}=0.
        # So Node N-1 gets +J_{N-1.5}/dx.
        # J_{N-1.5} corresponds to interface N-2 (last element of v).
        # Row N-1: coeff u_{N-1} is +v-_{N-2}/dx. coeff u_{N-2} is +v+_{N-2}/dx.
        # This is handled by `main_diag[1:] += ...` (at i=N-2 -> index N-1) and `lower_diag[:] += ...` (at i=N-2 -> index N-1).
        # Correct.

        # Reset the diffusion boundary conditions (overwrite the accumulated result above, since I want to keep the original diffusion logic - or add them?)
        # The code above accumulates (main_diag_diff + main_diag_adv).
        # Here main/upper/lower were initialised directly to the diffusion part.
        # Only the boundary of the diffusion part needs correcting.
        # Diffusion part:
        main_diag[0] = -alpha_diff - factor * v_plus[0] 
        main_diag[-1] = -alpha_diff + factor * v_minus[-1]

        # Build the matrix
        A = diags([lower_diag, main_diag, upper_diag], [-1, 0, 1], format='csr')

        return A

    def simulate_advection_competition(self, d, D, alpha, T=1000.0, dt=None):
        """Simulate competition dynamics with advection"""
        # Estimate the maximum gradient
        max_grad_m = np.max(np.abs(self.m_grad))

        # Automatically choose a time step satisfying the stability (CFL) condition
        # Safety factor lowered from 0.4 to 0.2 to prevent numerical overflow in extreme cases
        # 1. Diffusion limit: dt <= 0.5 * dx^2 / D
        max_diff = max(d, D)
        dt_diff = 0.2 * (self.dx ** 2) / max_diff + 1e-12

        # 2. Advection limit: dt <= dx / v_max, where v_max = alpha * |grad(m)|
        if alpha > 1e-6 and max_grad_m > 1e-6:
            v_max = alpha * max_grad_m
            dt_adv = 0.2 * self.dx / v_max
        else:
            dt_adv = 1.0 # very large

        dt_stable = min(dt_diff, dt_adv)

        # If dt is not given or too large, use the stable step
        if dt is None or dt > dt_stable:
            dt = dt_stable

        N = self.Nx
        Nt = int(T / dt)

        # Initial conditions
        u0 = 0.3 * np.ones(N) + 0.05 * np.random.randn(N)
        v0 = 0.3 * np.ones(N) + 0.05 * np.random.randn(N)
        u0 = np.maximum(u0, 0)
        v0 = np.maximum(v0, 0)

        # Build the operator matrices
        A_u = self.construct_advection_diffusion_matrix(d, alpha)  # with advection
        A_v = self.construct_advection_diffusion_matrix(D, 0.0)    # without advection

        # Time evolution
        u = u0.copy()
        v = v0.copy()

        u_history = [u.copy()]
        v_history = [v.copy()]

        # Save every so many steps, about 200 frames in total
        save_interval = max(1, int(Nt / 200))
        check_interval = max(100, int(Nt / 500)) # check for steady state/extinction every so many steps

        for n in range(1, Nt):
            # Reaction terms
            # Clip values to prevent overflow
            u_safe = np.clip(u, 0, 1e5)
            v_safe = np.clip(v, 0, 1e5)

            reaction_u = u_safe * (self.m - u_safe - v_safe)
            reaction_v = v_safe * (self.m - u_safe - v_safe)

            # Update
            u_new = u + dt * (A_u.dot(u) + reaction_u)
            v_new = v + dt * (A_v.dot(v) + reaction_v)

            # Ensure non-negativity
            u = np.maximum(u_new, 0)
            v = np.maximum(v_new, 0)

            # Check the early-stopping condition
            if n % check_interval == 0:
                u_max = np.max(u)
                v_max = np.max(v)

                # 1. Extinction detection
                if u_max < 1e-4 or v_max < 1e-4:
                    # One species has gone extinct; no need to continue
                    # Fill the remaining history with the last frame for plotting
                    remaining_frames = (Nt - n) // save_interval
                    for _ in range(remaining_frames):
                        u_history.append(u.copy())
                        v_history.append(v.copy())
                    break

                # 2. Steady-state detection (optional and more involved; omitted for robustness)

            # Save results
            if n % save_interval == 0:
                u_history.append(u.copy())
                v_history.append(v.copy())

        # Make sure the last step is saved as well
        u_history.append(u.copy())
        v_history.append(v.copy())

        return np.array(u_history), np.array(v_history)

    def analyze_alpha_dependence(self, d=1.0, D=1.0, alpha_values=np.logspace(-2, 2, 20)):
        """Analyse the effect of the advection coefficient α on the outcome of competition"""
        N_alpha = len(alpha_values)
        final_u_mean = np.zeros(N_alpha)
        final_v_mean = np.zeros(N_alpha)
        coexistence_indicator = np.zeros(N_alpha)

        for i, alpha in enumerate(alpha_values):
            print(f"Simulating with α={alpha:.3f} ({i+1}/{N_alpha})")

            # Use a longer T=1000 to ensure competitive exclusion occurs (100 was too short)
            u_history, v_history = self.simulate_advection_competition(d, D, alpha, T=1000.0)

            # Compute the final mean densities
            u_final = u_history[-1]
            v_final = v_history[-1]

            final_u_mean[i] = np.mean(u_final)
            final_v_mean[i] = np.mean(v_final)

            # Determine coexistence: final densities of both species exceed a threshold
            threshold = 0.01
            coexistence_indicator[i] = 1 if (final_u_mean[i] > threshold and 
                                           final_v_mean[i] > threshold) else 0

        return alpha_values, final_u_mean, final_v_mean, coexistence_indicator

    def plot_alpha_dependence(self, d=1.0, D=1.0, show_plot=True):
        """Plot the dependence of the competition outcome on the advection coefficient"""
        alpha_values = np.logspace(-2, 2, 15)
        alpha_vals, u_mean, v_mean, coexistence = self.analyze_alpha_dependence(d, D, alpha_values)

        fig, axes = plt.subplots(2, 3, figsize=(15, 10))

        # 1. Final mean density vs α
        ax = axes[0, 0]
        ax.loglog(alpha_vals, u_mean, 'b-', linewidth=2, label='Species u (with advection)')
        ax.loglog(alpha_vals, v_mean, 'r-', linewidth=2, label='Species v (no advection)')
        ax.set_xlabel('Advection coefficient (α)', fontsize=12)
        ax.set_ylabel('Final mean density', fontsize=12)
        ax.set_title(f'Final Densities vs Advection Coefficient\n(d={d}, D={D})', fontsize=14)
        ax.legend(fontsize=11)
        ax.grid(True, alpha=0.3, which='both')

        # 2. Density ratio u/v
        ax = axes[0, 1]
        ratio = np.zeros_like(u_mean)
        valid = v_mean > 1e-10
        ratio[valid] = u_mean[valid] / v_mean[valid]

        ax.loglog(alpha_vals[valid], ratio[valid], 'g-', linewidth=2)
        ax.axhline(y=1.0, color='k', linestyle='--', alpha=0.5)
        ax.set_xlabel('Advection coefficient (α)', fontsize=12)
        ax.set_ylabel('Final density ratio (u/v)', fontsize=12)
        ax.set_title('Competitive Advantage vs Advection', fontsize=14)
        ax.grid(True, alpha=0.3, which='both')

        # 3. Coexistence regions
        ax = axes[0, 2]
        # Find the coexistence regions
        coexistence_start = None
        coexistence_regions = []

        for i in range(len(alpha_vals)):
            if coexistence[i] == 1:
                if coexistence_start is None:
                    coexistence_start = alpha_vals[i]
            else:
                if coexistence_start is not None:
                    coexistence_regions.append((coexistence_start, alpha_vals[i-1]))
                    coexistence_start = None

        if coexistence_start is not None:
            coexistence_regions.append((coexistence_start, alpha_vals[-1]))

        # Plot the coexistence regions
        for region in coexistence_regions:
            ax.axvspan(region[0], region[1], alpha=0.3, color='green', label='Coexistence')

        ax.loglog(alpha_vals, u_mean, 'b-', linewidth=2, label='Species u')
        ax.loglog(alpha_vals, v_mean, 'r-', linewidth=2, label='Species v')
        ax.set_xlabel('Advection coefficient (α)', fontsize=12)
        ax.set_ylabel('Final mean density', fontsize=12)
        ax.set_title('Coexistence Regions', fontsize=14)
        ax.grid(True, alpha=0.3, which='both')

        # Deduplicate legend entries
        handles, labels = ax.get_legend_handles_labels()
        by_label = dict(zip(labels, handles))
        ax.legend(by_label.values(), by_label.keys(), fontsize=11)

        # 4-6. Spatial distributions for different α
        alpha_examples = [0.01, 1.0, 100.0]
        colors = ['blue', 'green', 'red']

        for i, alpha in enumerate(alpha_examples):
            ax = axes[1, i]

            u_history, v_history = self.simulate_advection_competition(d, D, alpha, T=100.0)
            u_final = u_history[-1]
            v_final = v_history[-1]

            ax.plot(self.x, u_final, color=colors[i], linestyle='-', 
                   linewidth=2, label=f'u (α={alpha})')
            ax.plot(self.x, v_final, color=colors[i], linestyle='--', 
                   linewidth=2, label=f'v (α={alpha})')
            ax.plot(self.x, self.m, 'k:', linewidth=1.5, label='m(x)', alpha=0.7)

            ax.set_xlabel('Position (x)', fontsize=12)
            ax.set_ylabel('Population density', fontsize=12)
            ax.set_title(f'α={alpha}', fontsize=14)
            ax.legend(fontsize=10)
            ax.grid(True, alpha=0.3)

        plt.tight_layout()

        if not show_plot:
            plt.close(fig)

        # Analyse the theorem: coexistence at large α
        print("\n" + "="*60)
        print("ANALYSIS OF THEOREM")
        print("="*60)
        print("Theorem states that when α is sufficiently large,")
        print("both semi-trivial equilibria are unstable and there exists")
        print("at least one stable positive equilibrium (coexistence).")

        # Check for coexistence at large α
        large_alpha_idx = np.where(alpha_vals > 10)[0]
        if len(large_alpha_idx) > 0:
            coexists_at_large_alpha = any(coexistence[large_alpha_idx] == 1)
            print(f"\nCoexistence at large α (α > 10): {coexists_at_large_alpha}")

            if coexists_at_large_alpha:
                print("✓ Theorem is supported by simulation.")
            else:
                print("✗ Theorem is not supported by simulation.")

        return alpha_vals, u_mean, v_mean, coexistence

def explore_diffusion_advection_interaction():
    """Explore the interaction between diffusion and advection"""
    print("\n" + "="*60)
    print("EXPLORING DIFFUSION-ADVECTION INTERACTION")
    print("="*60)

    model = AdvectionCompetitionModel(L=10.0, Nx=101)

    # Different diffusion-coefficient ratios
    diffusion_ratios = [
        (0.5, 1.0, "D > d"),
        (1.0, 1.0, "D = d"),
        (1.0, 0.5, "D < d"),
    ]

    fig, axes = plt.subplots(3, 2, figsize=(14, 15))

    for idx, (d, D, label) in enumerate(diffusion_ratios):
        print(f"\nCase {idx+1}: {label} (d={d}, D={D})")

        # Analyse the α dependence
        alpha_vals, u_mean, v_mean, coexistence = model.plot_alpha_dependence(d, D, show_plot=False)

        # Plot the phase diagram of competition outcomes
        ax1 = axes[idx, 0]
        ax2 = axes[idx, 1]

        # Phase diagram: u vs v
        ax1.loglog(alpha_vals, u_mean, 'b-', linewidth=2, label='Species u')
        ax1.loglog(alpha_vals, v_mean, 'r-', linewidth=2, label='Species v')
        ax1.set_xlabel('Advection coefficient (α)', fontsize=12)
        ax1.set_ylabel('Final mean density', fontsize=12)
        ax1.set_title(f'{label}\nFinal Densities vs α', fontsize=14)
        ax1.legend(fontsize=11)
        ax1.grid(True, alpha=0.3, which='both')

        # Classification of competition outcomes
        ax2.semilogx(alpha_vals, coexistence, 'g-', linewidth=2, drawstyle='steps-post')
        ax2.fill_between(alpha_vals, 0, coexistence, alpha=0.3, color='green')
        ax2.set_xlabel('Advection coefficient (α)', fontsize=12)
        ax2.set_ylabel('Coexistence (1) / Exclusion (0)', fontsize=12)
        ax2.set_title(f'{label}\nCoexistence Regions', fontsize=14)
        ax2.set_yticks([0, 1])
        ax2.set_yticklabels(['Exclusion', 'Coexistence'])
        ax2.grid(True, alpha=0.3, which='both')

        # Mark the critical α values
        if len(alpha_vals) > 1:
            # Find the jump points from 0 to 1
            for i in range(1, len(coexistence)):
                if coexistence[i] != coexistence[i-1]:
                    alpha_crit = alpha_vals[i]
                    ax2.axvline(x=alpha_crit, color='k', linestyle='--', alpha=0.5)
                    ax2.text(alpha_crit, 0.5, f'α={alpha_crit:.2f}', 
                            fontsize=10, ha='center', va='center',
                            bbox=dict(boxstyle='round', facecolor='white', alpha=0.7))

    plt.tight_layout()

explore_diffusion_advection_interaction()
