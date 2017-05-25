import matplotlib.pyplot as plt
import numpy as np
from numpy.matlib import randn

# Creating a plot figure object
fig = plt.figure()

# let's add a subplot
ax1 = fig.add_subplot(2,2,1)
# Here we create a 2x2 space, and slecting the first block
ax2 = fig.add_subplot(2, 2, 2)
plt.plot([1.5, 3.5, -2, 1.6])

ax3 = fig.add_subplot(2,2,3)

# adding histogram
mu, sigma = 100, 15
x = mu + sigma*np.random.randn(10000)
n, bins, patches = ax1.hist(x, 50, normed=1, facecolor='green', alpha=0.75)


# Creating a Scatter
ax2.scatter(np.arange(30), np.arange(30) + randn(30))


# finally showing the plot
plt.show(fig)