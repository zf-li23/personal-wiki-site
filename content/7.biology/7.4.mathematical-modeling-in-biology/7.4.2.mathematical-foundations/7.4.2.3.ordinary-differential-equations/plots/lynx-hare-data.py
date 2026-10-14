import numpy as np
import matplotlib.pyplot as plt

years = np.arange(1900, 1921)
hares = np.array([30.0, 47.2, 70.2, 77.4, 36.3, 20.6, 18.1, 21.4, 22.0, 25.4,
                  27.1, 40.3, 57.0, 76.6, 52.3, 19.5, 11.2, 7.6, 14.6, 16.2, 24.7])
lynx = np.array([4.0, 6.1, 9.8, 35.2, 59.4, 41.7, 19.0, 13.0, 8.3, 9.1,
                 7.4, 8.0, 12.3, 19.5, 45.7, 51.1, 29.7, 15.8, 9.7, 10.1, 8.6])

plt.figure(figsize=(10,5))
plt.plot(years, hares, 'b-o', label='Hares (prey)')
plt.plot(years, lynx, 'r-s', label='Lynx (predator)')
plt.xlabel('Year')
plt.ylabel('Population (thousands)')
plt.title('Hudson Bay Company: Snowshoe Hare and Canadian Lynx')
plt.legend()
plt.grid(True, alpha=0.3)
