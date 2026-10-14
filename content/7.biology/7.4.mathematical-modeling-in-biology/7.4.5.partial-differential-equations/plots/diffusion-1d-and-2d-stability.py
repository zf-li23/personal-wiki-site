import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

class Diffusion1D:
    """Solver for the 1D diffusion equation"""

    def __init__(self, D, L, T, nx=101, nt=1000):
        """
        Parameters:
            D: diffusion coefficient
            L: length of the spatial domain
            T: total time
            nx: number of spatial grid points
            nt: number of time steps
        """
        self.D = D
        self.L = L
        self.T = T
        self.nx = nx
        self.nt = nt

        # Spatial and temporal step sizes
        self.dx = L / (nx - 1)
        self.dt = T / nt

        # Grid
        self.x = np.linspace(0, L, nx)

        # Stability check
        stability = D * self.dt / (self.dx ** 2)
        if stability > 0.5:
            print(f"Warning: stability parameter s = {stability:.3f} > 0.5; the solution may be unstable")
            print(f"Suggestion: decrease dt or increase dx")

    def solve_explicit(self, u0_func, boundary_conditions):
        """
        Solve with the explicit finite-difference method

        Parameters:
            u0_func: initial condition function u0(x)
            boundary_conditions: dict of boundary conditions, e.g. {'left': 'dirichlet', 'right': 'neumann'}

        Returns:
            u: solution array (nt+1, nx)
        """
        # Initialisation
        u = np.zeros((self.nt + 1, self.nx))
        u[0, :] = u0_func(self.x)

        # Diffusion constant
        s = self.D * self.dt / (self.dx ** 2)

        # Time stepping
        for n in range(self.nt):
            # Update interior points
            for i in range(1, self.nx - 1):
                u[n+1, i] = u[n, i] + s * (u[n, i+1] - 2*u[n, i] + u[n, i-1])

            # Boundary conditions
            if boundary_conditions.get('left') == 'dirichlet':
                u[n+1, 0] = boundary_conditions.get('left_value', 0)
            elif boundary_conditions.get('left') == 'neumann':
                # First-order zero-flux boundary condition
                u[n+1, 0] = u[n+1, 1]

            if boundary_conditions.get('right') == 'dirichlet':
                u[n+1, -1] = boundary_conditions.get('right_value', 0)
            elif boundary_conditions.get('right') == 'neumann':
                u[n+1, -1] = u[n+1, -2]

        return u

    def solve_diffusion_growth(self, u0_func, r, K, boundary_conditions):
        """
        Solve the diffusion-growth equation
        """
        # Initialisation
        u = np.zeros((self.nt + 1, self.nx))
        u[0, :] = u0_func(self.x)

        # Diffusion constant
        s = self.D * self.dt / (self.dx ** 2)

        # Time stepping
        for n in range(self.nt):
            # Update interior points
            for i in range(1, self.nx - 1):
                diffusion = s * (u[n, i+1] - 2*u[n, i] + u[n, i-1])
                growth = self.dt * r * u[n, i] * (1 - u[n, i] / K)
                u[n+1, i] = u[n, i] + diffusion + growth

            # Boundary conditions
            if boundary_conditions.get('left') == 'dirichlet':
                u[n+1, 0] = boundary_conditions.get('left_value', 0)
            elif boundary_conditions.get('left') == 'neumann':
                u[n+1, 0] = u[n+1, 1]

            if boundary_conditions.get('right') == 'dirichlet':
                u[n+1, -1] = boundary_conditions.get('right_value', 0)
            elif boundary_conditions.get('right') == 'neumann':
                u[n+1, -1] = u[n+1, -2]

        return u

class Diffusion2D:
    """Solver for the 2D diffusion equation (for demonstrating stability)"""

    def __init__(self, D, L, T, nx=51, nt=1000):
        self.D = D
        self.L = L
        self.nx = nx
        self.ny = nx
        self.nt = nt

        self.h = L / (nx - 1)
        self.dt = T / nt

        self.x = np.linspace(0, L, nx)
        self.y = np.linspace(0, L, nx)
        self.X, self.Y = np.meshgrid(self.x, self.y)

        # Stability parameter
        self.nu = D * self.dt / (self.h ** 2)
        print(f"  [2D Setup] D={D}, dt={self.dt:.4f}, h={self.h:.4f}")
        print(f"  Stability parameter nu = D*dt/h^2 = {self.nu:.4f}")
        if self.nu > 0.25:
            print("  -> Warning: exceeds the 2D explicit-scheme stability limit (0.25)")
        else:
            print("  -> Stability condition satisfied (<= 0.25)")

    def solve_explicit_initial_step(self, u0_func, steps=None):
        """Run only the given number of steps, for demonstration"""
        if steps is None:
            steps = self.nt

        u = u0_func(self.X, self.Y)
        nu = self.nu

        for n in range(steps):
            u_new = u.copy()

            # Compute the Laplacian using slicing
            u_center = u[1:-1, 1:-1]
            u_left   = u[1:-1, :-2]
            u_right  = u[1:-1, 2:]
            u_top    = u[:-2, 1:-1]
            u_bottom = u[2:, 1:-1]

            laplacian = (u_left + u_right + u_top + u_bottom - 4 * u_center)
            u_new[1:-1, 1:-1] = u_center + nu * laplacian

            # Neumann boundary
            u_new[0, :] = u_new[1, :]
            u_new[-1, :] = u_new[-2, :]
            u_new[:, 0] = u_new[:, 1]
            u_new[:, -1] = u_new[:, -2]

            u = u_new

            # If the solution blows up, stop early and return the current state
            if np.max(np.abs(u)) > 1e10:
                # Normalise so the pattern is visible in the plot
                return u

        return u

# Example 1: pure diffusion (1D)
print("Example 1: 1D pure diffusion")
# Modify D to satisfy the stability condition s <= 0.5
# Originally D=0.5, L=10, nx=201 -> dx=0.05, dx^2=0.0025. T=2, nt=500 -> dt=0.004
# s = 0.5 * 0.004 / 0.0025 = 0.8 > 0.5 ( unstable )
# Decrease dt: nt=1000 -> dt=0.002 -> s=0.4 < 0.5
L = 10.0  # length of the spatial domain
T = 2.0   # total time
D = 0.5   # diffusion coefficient

# Initial condition: Gaussian centred in the domain
def u0_gaussian(x):
    return np.exp(-(x - L/2)**2 / 0.5)

# Increase the number of time steps for stability
solver1 = Diffusion1D(D, L, T, nx=201, nt=1000)
u1 = solver1.solve_explicit(u0_gaussian, {'left': 'neumann', 'right': 'neumann'})

# Visualise 1D
fig1, axes1 = plt.subplots(2, 2, figsize=(12, 10))
# Adjust indices to match the new nt
time_indices = [0, 100, 300, 999]
titles = ['Initial distribution', 't = 0.2', 't = 0.6', 't = 2.0']

for i, (idx, title) in enumerate(zip(time_indices, titles)):
    ax = axes1[i//2, i%2]
    ax.plot(solver1.x, u1[idx, :], 'b-', linewidth=2)
    ax.set_xlabel('Position $x$', fontsize=12)
    ax.set_ylabel('Density $u(x,t)$', fontsize=12)
    ax.set_title(title, fontsize=14)
    ax.grid(True, alpha=0.3)
    ax.set_ylim([0, 1.1])

fig1.suptitle('1D Diffusion Equation: Diffusion of Gaussian Initial Condition', fontsize=16)
plt.tight_layout()

# ==========================================
# 2D stability demonstration
# ==========================================
print("\n" + "="*50)
print("Demo: numerical stability analysis of the 2D diffusion equation")
print("="*50)
print("Theoretical condition: D * dt / h^2 <= 0.25")

L_2d = 1.0
nx_2d = 31
h_2d = L_2d / (nx_2d - 1)  # 0.0333
D_2d = 1.0

# Initial condition: central Gaussian peak
def u0_2d(X, Y):
    return np.exp(-((X - L_2d/2)**2 + (Y - L_2d/2)**2) / 0.02)

# Case 1: stable
# D*dt/h^2 = 0.24 <= 0.25
dt_stable = 0.24 * (h_2d**2) / D_2d
T_stable = 0.1
nt_stable = int(T_stable / dt_stable) + 1
print("\nCase 1: stable parameters (nu = 0.24)")
solver_stable = Diffusion2D(D_2d, L_2d, T_stable, nx_2d, nt_stable)
u_stable = solver_stable.solve_explicit_initial_step(u0_2d)

# Case 2: unstable
# D*dt/h^2 = 0.26 > 0.25
dt_unstable = 0.28 * (h_2d**2) / D_2d 
# Keep the time roughly the same; since dt is larger, this suffices
nt_unstable = nt_stable  
T_unstable = dt_unstable * nt_unstable
print("\nCase 2: unstable parameters (nu = 0.28)")
solver_unstable = Diffusion2D(D_2d, L_2d, T_unstable, nx_2d, nt_unstable)
u_unstable = solver_unstable.solve_explicit_initial_step(u0_2d)

# Comparison plot
fig3, axes3 = plt.subplots(1, 3, figsize=(16, 5))

# Initial state
u0 = u0_2d(solver_stable.X, solver_stable.Y)
im0 = axes3[0].imshow(u0, cmap='viridis', origin='lower', extent=[0, L_2d, 0, L_2d])
axes3[0].set_xlabel('x')
axes3[0].set_ylabel('y')
axes3[0].set_title("Initial State $u(x,y,0)$", fontsize=14)
plt.colorbar(im0, ax=axes3[0])

# Stable result
im1 = axes3[1].imshow(u_stable, cmap='viridis', origin='lower', extent=[0, L_2d, 0, L_2d])
axes3[1].set_xlabel('x')
axes3[1].set_title(f"Stable Evolution ($\\nu=0.24$)\n$t={T_stable:.3f}$", fontsize=14)
plt.colorbar(im1, ax=axes3[1])

# Unstable result
vmin, vmax = np.min(u_stable), np.max(u_stable)
# Limit the display range so the pattern is visible
im2 = axes3[2].imshow(u_unstable, cmap='viridis', origin='lower', extent=[0, L_2d, 0, L_2d], vmin=vmin, vmax=vmax)
axes3[2].set_xlabel('x')
axes3[2].set_title(f"Unstable Evolution ($\\nu=0.28$)\n$t={T_unstable:.3f}$", fontsize=14)
plt.colorbar(im2, ax=axes3[2])

# Add explanatory text
plt.figtext(0.5, 0.02, 
            r"Stability Condition: $\frac{D \Delta t}{h^2} \leq \frac{1}{4}$. Violation leads to numerical oscillations (Right).", 
            ha="center", fontsize=12, bbox={"facecolor":"orange", "alpha":0.2, "pad":5})

plt.tight_layout(rect=[0, 0.05, 1, 1])
