import numpy as np
import matplotlib.pyplot as plt

# Read data from result.dat
data = np.genfromtxt('result.dat', skip_header=1)

# Extract columns
n_values = data[:, 0]
amount_values = data[:, 1]

# Plotting
plt.plot(n_values, amount_values, marker='o', linestyle='-', color='b')
plt.xlabel('Years (n)')
plt.ylabel('Amount')
plt.grid(True)
plt.savefig('ytrewq.png')
plt.show()
