import numpy as np
import matplotlib.pyplot as plt

# Read data from result.dat file
data = np.loadtxt("result.dat", skiprows=1)

# Extract columns
n_values = data[:, 0]
amounts = data[:, 1]

# Plot the results
plt.plot(n_values, amounts, marker='o', linestyle='-', color='b')
plt.xlabel('Years (n)')
plt.ylabel('Amount')
plt.grid(True)
plt.show()
