import numpy as np
import matplotlib.pyplot as plt

# Define the killer whale matrix
A = np.array([
    [0, 0.0043, 0.1132, 0],
    [0.9775, 0.9111, 0, 0],
    [0, 0.0736, 0.9534, 0],
    [0, 0, 0.0452, 0.9804]
])

# Initial vector
x0 = np.array([10, 60, 110, 70])

# Simulate 50 years
years = 50
population = np.zeros((4, years+1))
population[:, 0] = x0

for t in range(years):
    population[:, t+1] = A @ population[:, t]

# Plot
plt.figure(figsize=(10, 6))
plt.plot(population[0, :], 'c-', label='Calf', linewidth=2)
plt.plot(population[1, :], 'g-', label='Juvenile', linewidth=2)
plt.plot(population[2, :], 'b-', label='Mature', linewidth=2)
plt.plot(population[3, :], 'r-', label='Post-reproductive', linewidth=2)
plt.plot(np.sum(population, axis=0), 'k-', label='Total', linewidth=2)
plt.xlabel('Time (years)')
plt.ylabel('Population size')
plt.title('Killer whale population dynamics (50 years)')
plt.legend()
plt.grid(True)
