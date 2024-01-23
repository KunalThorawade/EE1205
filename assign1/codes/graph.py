import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0,30)
plt.xlim(-5,25)
plt.ylim(0,30)
y = [5 + 1.75*n for n in x]
plt.stem(x,y)
plt.show()
