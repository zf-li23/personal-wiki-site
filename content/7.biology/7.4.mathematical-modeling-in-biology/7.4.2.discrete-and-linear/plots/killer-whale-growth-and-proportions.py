import numpy as np
import matplotlib.pyplot as plt

# Define the killer whale matrix
A = np.array([
    [0, 0.0043, 0.1132, 0],
    [0.9775, 0.9111, 0, 0],
    [0, 0.0736, 0.9534, 0],
    [0, 0, 0.0452, 0.9804]
])

x0 = np.array([10, 60, 110, 70])
years = 50
population = np.zeros((4, years+1))
population[:, 0] = x0

for t in range(years):
    population[:, t+1] = A @ population[:, t]

N = np.sum(population, axis=0)
growth_rate = N[1:] / N[:-1]
proportions = population / N

# Compute the dominant eigenvalue
eigenvalues, _ = np.linalg.eig(A)
lambda1 = np.max(np.real(eigenvalues))

# Create four subplots
plt.figure(figsize=(16, 10))

# Subplot 1: total population size
plt.subplot(2, 2, 1)
plt.plot(N, 'k-', linewidth=2)
plt.xlabel('Time (years)')
plt.ylabel('Total population N(t)')
plt.title('Total population size over time')
plt.grid(True)

# Subplot 2: annual growth rate
plt.subplot(2, 2, 2)
plt.plot(range(1, years+1), growth_rate, 'b-', linewidth=2)
plt.axhline(y=lambda1, color='r', linestyle='--', label=f'λ={lambda1:.4f}')
plt.xlabel('Time (years)')
plt.ylabel('Annual growth rate λ(t)')
plt.title('Annual growth rate over time')
plt.legend()
plt.grid(True)

# Subplot 3: stage proportions
plt.subplot(2, 2, 3)
plt.plot(proportions[0, :], 'c-', label='Calf', linewidth=2)
plt.plot(proportions[1, :], 'g-', label='Juvenile', linewidth=2)
plt.plot(proportions[2, :], 'b-', label='Mature', linewidth=2)
plt.plot(proportions[3, :], 'r-', label='Post-reproductive', linewidth=2)
plt.xlabel('Time (years)')
plt.ylabel('Proportion')
plt.title('Stage proportions over time')
plt.legend()
plt.grid(True)

stage_names = ['Calf', 'Juvenile', 'Mature', 'Post-reproductive']

# Subplot 4: log population size
plt.subplot(2, 2, 4)
for i in range(4):
    plt.semilogy(population[i, :], label=stage_names[i], linewidth=2)
plt.semilogy(N, 'k-', label='Total', linewidth=2)
plt.xlabel('Time (years)')
plt.ylabel('Log population size')
plt.title('Log population size over time')
plt.legend()
plt.grid(True)

plt.tight_layout()
