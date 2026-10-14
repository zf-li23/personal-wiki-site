import numpy as np
import matplotlib.pyplot as plt

# Define the killer whale matrix
A = np.array([
    [0, 0.0043, 0.1132, 0],
    [0.9775, 0.9111, 0, 0],
    [0, 0.0736, 0.9534, 0],
    [0, 0, 0.0452, 0.9804]
])

stage_names = ['Calf', 'Juvenile', 'Mature', 'Post-reproductive']

# Four initial vectors
initial_vectors = [
    np.array([250, 0, 0, 0]),    # All calves
    np.array([0, 250, 0, 0]),    # All juveniles
    np.array([0, 0, 250, 0]),    # All mature
    np.array([0, 0, 0, 250])     # All post-reproductive
]
labels = ['All calves', 'All juveniles', 'All mature', 'All post-reproductive']
years = 50

# Simulate and plot
plt.figure(figsize=(10, 8))

for i, (x0, label) in enumerate(zip(initial_vectors, labels)):
    # Simulate
    population = np.zeros((4, years+1))
    population[:, 0] = x0
    for t in range(years):
        population[:, t+1] = A @ population[:, t]

    N = np.sum(population, axis=0)
    proportions = population / N

    # Plot stage proportions
    plt.subplot(2, 2, i+1)
    colors = ['c', 'g', 'b', 'r']
    for stage in range(4):
        plt.plot(proportions[stage, :], color=colors[stage], 
                 label=stage_names[stage], linewidth=2)
    plt.xlabel('Time (years)')
    plt.ylabel('Proportion')
    plt.title(f'{label} - Stage proportions')
    if i == 0:
        plt.legend(loc='upper right')
    plt.grid(True)

plt.tight_layout()
