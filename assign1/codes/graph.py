mport numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 30)
plt.xlim(-5, 30)
plt.ylim(0, 55)
y = [5 + 1.75 * n for n in x]
plt.stem(x, y)

# Save the plot as an image file
plt.savefig('plot.png')

# Display the saved image using Termux
import subprocess
subprocess.run(['termux-open', 'plot.jpg'])
