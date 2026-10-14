import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

class ReactionDiffusion2D:
    """Solver for 2D reaction-diffusion equations"""

    def __init__(self, Du, Dv, a, b, L, T, nx=101, ny=101, nt=10000):
        """
        Parameters:
            Du, Dv: diffusion coefficients
            a, b: reaction parameters
            L: side length of the square domain
            T: total time
            nx, ny: number of spatial grid points
            nt: number of time steps
        """
        self.Du = Du
        self.Dv = Dv
        self.a = a
        self.b = b
        self.L = L
        self.T = T
        self.nx = nx
        self.ny = ny
        self.nt = nt

        # Spatial and temporal step sizes
        self.dx = L / (nx - 1)
        self.dy = L / (ny - 1)
        self.dt = T / nt

        # Spatial grid
        self.x = np.linspace(0, L, nx)
        self.y = np.linspace(0, L, ny)
        self.X, self.Y = np.meshgrid(self.x, self.y)

        # Stability check
        s_u = Du * self.dt / (self.dx ** 2 + self.dy ** 2)
        s_v = Dv * self.dt / (self.dx ** 2 + self.dy ** 2)
        if s_u > 0.25 or s_v > 0.25:
            print(f"Warning: stability parameters s_u = {s_u:.3f}, s_v = {s_v:.3f}")
            print(f"Suggestion: decrease dt")

    def laplacian_2d(self, u):
        """Compute the 2D Laplacian (five-point stencil)"""
        # Use zero-flux (Neumann) boundary conditions
        u_padded = np.pad(u, 1, mode='edge')

        # Five-point stencil
        laplacian = (u_padded[2:, 1:-1] + u_padded[:-2, 1:-1] + 
                     u_padded[1:-1, 2:] + u_padded[1:-1, :-2] - 4 * u_padded[1:-1, 1:-1])

        return laplacian / (self.dx * self.dy)

    def reaction_terms(self, u, v):
        """Reaction terms of the Schnakenberg model"""
        f = self.a - u + u**2 * v
        g = self.b - u**2 * v
        return f, g

    def solve_explicit(self, u0_func, v0_func):
        """
        Solve the reaction-diffusion equations with an explicit method

        Parameters:
            u0_func, v0_func: initial condition functions
        """
        # Initialisation
        u = np.zeros((self.nx, self.ny))
        v = np.zeros((self.nx, self.ny))

        for i in range(self.nx):
            for j in range(self.ny):
                u[i, j] = u0_func(self.x[i], self.y[j])
                v[i, j] = v0_func(self.x[i], self.y[j])

        # Store the time evolution
        u_history = [u.copy()]
        v_history = [v.copy()]

        # Time stepping
        for n in range(self.nt):
            # Compute the Laplacian
            laplacian_u = self.laplacian_2d(u)
            laplacian_v = self.laplacian_2d(v)

            # Compute the reaction terms
            f, g = self.reaction_terms(u, v)

            # Update
            u_new = u + self.dt * (self.Du * laplacian_u + f)
            v_new = v + self.dt * (self.Dv * laplacian_v + g)

            # Ensure non-negativity
            u_new = np.maximum(u_new, 0)
            v_new = np.maximum(v_new, 0)

            u, v = u_new, v_new

            # Save every fixed number of steps
            if n % 100 == 0:
                u_history.append(u.copy())
                v_history.append(v.copy())

        return np.array(u_history), np.array(v_history)

# Parameters: Turing pattern conditions
L = 20.0          # side length of the domain
T = 100.0         # total time

# Diffusion coefficients: Dv much larger than Du (necessary for Turing instability)
Du = 0.1
Dv = 1.0

# Reaction parameters
a = 0.1
b = 0.9

# Initial condition: homogeneous steady state plus small random perturbations
u0_homog = a + b
v0_homog = b / (a + b)**2

def u0_perturbed(x, y):
    return u0_homog + 0.01 * np.random.randn()

def v0_perturbed(x, y):
    return v0_homog + 0.01 * np.random.randn()

# Create the solver
solver_rd = ReactionDiffusion2D(Du, Dv, a, b, L, T, nx=101, ny=101, nt=20000)

# Solve
print("Solving the 2D reaction-diffusion equations...")
u_history, v_history = solver_rd.solve_explicit(u0_perturbed, v0_perturbed)

# Visualisation
fig3, axes3 = plt.subplots(2, 3, figsize=(15, 10))

# Compute the correct frame indices
# Time per frame = save_interval * dt = 100 * (100/20000) = 0.5
frames_per_unit_time = 1.0 / (100 * solver_rd.dt)
target_times = [0, 20, 40, 60, 80, 100]
time_indices = [int(t * frames_per_unit_time) for t in target_times]
# Fix the last index to avoid going out of bounds
if time_indices[-1] >= len(u_history):
    time_indices[-1] = len(u_history) - 1

titles = [f't = {t}' for t in target_times]

for i, (idx, title) in enumerate(zip(time_indices, titles)):
    ax = axes3[i//3, i%3]

    # Make sure the index is valid
    idx = min(idx, len(u_history)-1)

    # Show the distribution of u
    im = ax.imshow(u_history[idx], cmap='RdBu', origin='lower', 
                   extent=[0, L, 0, L], vmin=0.8*u0_homog, vmax=1.2*u0_homog)
    ax.set_xlabel('x', fontsize=12)
    ax.set_ylabel('y', fontsize=12)
    ax.set_title(title, fontsize=14)

    # Add a colour bar
    if i == 5:
        fig3.colorbar(im, ax=ax, shrink=0.8)

fig3.suptitle('Schnakenberg Model: Turing Pattern Formation', fontsize=16)
plt.tight_layout()

# Power spectrum analysis
fig4, axes4 = plt.subplots(1, 2, figsize=(12, 5))

# 2D Fourier transform of the final state
u_final = u_history[-1]
v_final = v_history[-1]

# Remove the mean (DC component) and analyse only the fluctuation pattern
u_fluctuation = u_final - np.mean(u_final)

# Compute the 2D Fourier transform
u_fft = np.fft.fft2(u_fluctuation)
# v_fft = np.fft.fft2(v_final - np.mean(v_final))

# Compute the power spectrum
u_power = np.abs(np.fft.fftshift(u_fft))**2
# v_power = np.abs(np.fft.fftshift(v_fft))**2

# Frequency coordinates
freq_x = np.fft.fftshift(np.fft.fftfreq(u_final.shape[0], d=solver_rd.dx))
freq_y = np.fft.fftshift(np.fft.fftfreq(u_final.shape[1], d=solver_rd.dy))

# Plot the power spectrum of u
im1 = axes4[0].imshow(np.log10(u_power+1), cmap='viridis', origin='lower',
                      extent=[freq_x[0], freq_x[-1], freq_y[0], freq_y[-1]])
axes4[0].set_xlabel('Spatial frequency $k_x$', fontsize=12)
axes4[0].set_ylabel('Spatial frequency $k_y$', fontsize=12)
axes4[0].set_title('Power spectrum of $u$ (log scale)', fontsize=14)
fig4.colorbar(im1, ax=axes4[0])

# Plot the radially averaged power spectrum
kx_grid, ky_grid = np.meshgrid(freq_x, freq_y)
k_radial = np.sqrt(kx_grid**2 + ky_grid**2)

# Compute the radial average by binning
k_bins = np.linspace(0, np.max(k_radial), 50)
k_bin_centers = (k_bins[:-1] + k_bins[1:]) / 2
u_radial_mean = np.zeros(len(k_bin_centers))

for i in range(len(k_bin_centers)):
    mask = (k_radial >= k_bins[i]) & (k_radial < k_bins[i+1])
    if np.any(mask):
        u_radial_mean[i] = np.mean(u_power[mask])

axes4[1].plot(k_bin_centers, u_radial_mean, 'b-', linewidth=2)
axes4[1].set_xlabel('Wavenumber $k$', fontsize=12)
axes4[1].set_ylabel('Radially averaged power', fontsize=12)
axes4[1].set_title('Radial power spectrum', fontsize=14)
axes4[1].grid(True, alpha=0.3)

plt.tight_layout()
