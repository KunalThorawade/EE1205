import numpy as np
import matplotlib.pyplot as plt

# Read data from result.dat
data = np.genfromtxt('result.dat', skip_header=1)

# Extract columns
n_values = data[:, 0]
amount_values = data[:, 1]

# Stem plot
plt.stem(n_values, amount_values, basefmt='b-', linefmt='r-', markerfmt='ro', use_line_collection=True)
plt.xlabel('Years (n)')
plt.ylabel('Amount')
plt.grid(True)
plt.show()
