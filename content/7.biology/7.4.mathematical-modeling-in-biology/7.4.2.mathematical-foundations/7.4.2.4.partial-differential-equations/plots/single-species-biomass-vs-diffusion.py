"""
heterogeneous_environment_single_species.py
Finite-difference solution of a single-species model in a heterogeneous environment
Verifies the lemma: non-monotone dependence of population size on the diffusion coefficient
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.sparse import diags
from scipy.sparse.linalg import spsolve
from scipy.optimize import fsolve

class HeterogeneousSingleSpeciesModel:
    """Solver for a single-species model in a heterogeneous environment"""

    def __init__(self, L=10.0, Nx=201):
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

        # Heterogeneous growth-rate function m(x) - non-constant
        self.m = self._growth_rate_function()

        # Compute total resources (manual trapezoidal integration for compatibility)
        self.total_resources = np.sum(self.m) * self.dx - 0.5 * self.dx * (self.m[0] + self.m[-1])

    def _growth_rate_function(self, type='sinusoidal'):
        """Growth-rate function m(x)"""
        if type == 'sinusoidal':
            # Sinusoidal function, mimicking a periodic resource distribution
            return 1.0 + 0.5 * np.sin(2 * np.pi * self.x / self.L)
        elif type == 'gaussian':
            # Gaussian function, mimicking a local resource-rich patch
            center = self.L / 2
            return 1.0 + 0.8 * np.exp(-(self.x - center)**2 / 2)
        elif type == 'step':
            # Step function, mimicking fragmented habitat
            m = np.ones_like(self.x)
            m[self.x < self.L/3] = 0.5
            m[self.x > 2*self.L/3] = 0.5
            return m
        else:
            raise ValueError(f"Unknown growth-rate function type: {type}")

    def construct_laplacian_matrix(self, d):
        """Build the matrix representation of the Laplacian"""
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

    def solve_equilibrium(self, d, method='newton'):
        """Solve the equilibrium equation (2.2)"""
        N = self.Nx
        theta0 = np.ones(N)  # initial guess

        if method == 'newton':
            # Solve the nonlinear equation with Newton's method
            def F(theta):
                A = self.construct_laplacian_matrix(d)
                return A.dot(theta) + theta * (self.m - theta)

            def J(theta):
                # Jacobian matrix
                A = self.construct_laplacian_matrix(d)
                diag_elements = self.m - 2 * theta
                J_matrix = A + diags([diag_elements], [0], format='csr')
                return J_matrix

            # Newton iteration
            theta = theta0.copy()
            for i in range(100):
                F_val = F(theta)
                if np.linalg.norm(F_val) < 1e-10:
                    break
                J_mat = J(theta)
                delta = spsolve(J_mat, -F_val)
                theta += delta
                theta = np.maximum(theta, 0)  # ensure non-negativity
            return theta

        elif method == 'time_evolution':
            # Evolve in time to the equilibrium
            dt = 0.01
            theta = theta0.copy()
            for _ in range(10000):
                A = self.construct_laplacian_matrix(d)
                reaction = theta * (self.m - theta)
                dtheta_dt = A.dot(theta) + reaction
                theta += dt * dtheta_dt
                theta = np.maximum(theta, 0)  # ensure non-negativity
                if np.linalg.norm(dtheta_dt) < 1e-8:
                    break
            return theta

    def calculate_total_biomass(self, d_values):
        """Compute total biomass for different diffusion coefficients"""
        biomasses = []
        thetas = []

        for d in d_values:
            theta = self.solve_equilibrium(d)
            # Manual trapezoidal integration for compatibility
            biomass = np.sum(theta) * self.dx - 0.5 * self.dx * (theta[0] + theta[-1])
            biomasses.append(biomass)
            thetas.append(theta)

        return np.array(biomasses), thetas

    def analyze_dependence_on_d(self):
        """Analyse the dependence of total biomass on the diffusion coefficient"""
        # Range of diffusion coefficients (log scale)
        d_values = np.logspace(-3, 3, 50)

        # Compute total biomass
        biomasses, thetas = self.calculate_total_biomass(d_values)

        # Plot results
        fig, axes = plt.subplots(2, 2, figsize=(14, 10))

        # 1. Total biomass vs diffusion coefficient
        ax = axes[0, 0]
        ax.loglog(d_values, biomasses, 'b-', linewidth=2, label='Total biomass')
        ax.axhline(y=self.total_resources, color='r', linestyle='--', 
                  label=f'Total resources: {self.total_resources:.3f}')
        ax.set_xlabel('Diffusion coefficient (d)', fontsize=12)
        ax.set_ylabel('Total biomass', fontsize=12)
        ax.set_title('Biomass vs Diffusion Coefficient (Lemma 2.1)', fontsize=14)
        ax.legend(fontsize=12)
        ax.grid(True, alpha=0.3, which='both')

        # 2. Difference: total biomass - total resources
        ax = axes[0, 1]
        difference = biomasses - self.total_resources
        ax.semilogx(d_values, difference, 'g-', linewidth=2)
        ax.axhline(y=0, color='r', linestyle='--')
        ax.set_xlabel('Diffusion coefficient (d)', fontsize=12)
        ax.set_ylabel('Biomass - Resources', fontsize=12)
        ax.set_title('Excess Biomass (Lemma 2.1: ∫θ > ∫m)', fontsize=14)
        ax.grid(True, alpha=0.3, which='both')

        # 3. Spatial distribution for different diffusion coefficients
        ax = axes[1, 0]
        selected_indices = [0, 10, 25, 40, 49]  # pick a few diffusion coefficients
        colors = plt.cm.viridis(np.linspace(0, 1, len(selected_indices)))

        for i, idx in enumerate(selected_indices):
            d = d_values[idx]
            theta = thetas[idx]
            ax.plot(self.x, theta, color=colors[i], 
                   label=f'd={d:.3f}', linewidth=1.5, alpha=0.8)

        # Plot the growth-rate function
        ax.plot(self.x, self.m, 'k--', linewidth=2, label='m(x)')
        ax.set_xlabel('Position (x)', fontsize=12)
        ax.set_ylabel('Population density', fontsize=12)
        ax.set_title('Spatial Distribution for Different d', fontsize=14)
        ax.legend(fontsize=10, ncol=2)
        ax.grid(True, alpha=0.3)

        # 4. Find the diffusion coefficient that maximises biomass
        ax = axes[1, 1]
        # Interpolate on the original grid to find the maximum
        from scipy.interpolate import interp1d
        f = interp1d(np.log10(d_values), biomasses, kind='cubic')
        d_fine = np.logspace(-3, 3, 1000)
        bio_fine = f(np.log10(d_fine))

        max_idx = np.argmax(bio_fine)
        d_opt = d_fine[max_idx]
        bio_max = bio_fine[max_idx]

        ax.loglog(d_values, biomasses, 'bo', markersize=6, label='Calculated points')
        ax.loglog(d_fine, bio_fine, 'b-', linewidth=1, alpha=0.5, label='Interpolation')
        ax.loglog(d_opt, bio_max, 'r*', markersize=15, 
                 label=f'Maximum: d={d_opt:.4f}, biomass={bio_max:.4f}')
        ax.set_xlabel('Diffusion coefficient (d)', fontsize=12)
        ax.set_ylabel('Total biomass', fontsize=12)
        ax.set_title(f'Optimal Diffusion Coefficient\nMax biomass at d={d_opt:.3f}', fontsize=14)
        ax.legend(fontsize=10)
        ax.grid(True, alpha=0.3, which='both')

        plt.tight_layout()

        print("\n" + "="*60)
        print("HETEROGENEOUS SINGLE SPECIES MODEL ANALYSIS")
        print("="*60)
        print(f"Total resources (∫m dx): {self.total_resources:.4f}")
        print(f"Minimum biomass (d→0): {biomasses[0]:.4f}")
        print(f"Minimum biomass (d→∞): {biomasses[-1]:.4f}")
        print(f"Maximum biomass: {bio_max:.4f} at d={d_opt:.4f}")
        print(f"Excess biomass at optimum: {bio_max - self.total_resources:.4f}")

        return d_opt, bio_max

def verify_lemma():
    """Verify the lemma: relation between population size and diffusion coefficient"""
    print("Verifying Lemma")

    # Create the model
    model = HeterogeneousSingleSpeciesModel(L=10.0, Nx=201)

    # Analyse the dependence of total biomass on the diffusion coefficient
    d_opt, bio_max = model.analyze_dependence_on_d()

    # Verify the limiting cases of the lemma
    d_values_extreme = np.logspace(-4, 4, 9)
    biomasses_extreme, _ = model.calculate_total_biomass(d_values_extreme)

    print("\n" + "="*60)
    print("VERIFICATION OF LEMMA")
    print("="*60)
    print("Lemma states:")
    print("1. For all d > 0, ∫θ > ∫m")
    print("2. lim_{d→0+} ∫θ = lim_{d→∞} ∫θ = ∫m")
    print("\nNumerical verification:")

    # Check whether ∫θ > ∫m for all d > 0
    all_greater = all(b > model.total_resources for b in biomasses_extreme)
    print(f"1. ∫θ > ∫m for all d > 0: {all_greater}")

    # Check the limiting cases
    print(f"2. lim_{{d→0+}} ∫θ = {biomasses_extreme[0]:.6f}, ∫m = {model.total_resources:.6f}")
    print(f"   Relative error: {abs(biomasses_extreme[0] - model.total_resources)/model.total_resources*100:.2f}%")
    print(f"3. lim_{{d→∞}} ∫θ = {biomasses_extreme[-1]:.6f}, ∫m = {model.total_resources:.6f}")
    print(f"   Relative error: {abs(biomasses_extreme[-1] - model.total_resources)/model.total_resources*100:.2f}%")

verify_lemma()
