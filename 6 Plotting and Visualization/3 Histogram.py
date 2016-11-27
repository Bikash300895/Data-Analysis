import matplotlib.pyplot as plt
import numpy as np


# Creating a plot figure object
fig = plt.figure()

# let's add a subplot
ax1 = fig.add_subplot(2,3,1)
# Here we create a 2x2 space, and slecting the first block
ax2 = fig.add_subplot(2, 2, 2)
plt.plot([1.5, 3.5, -2, 1.6])

ax3 = fig.add_subplot(2,2,3)

# adding histogram
mu, sigma = 100, 15
x = mu + sigma*np.random.randn(10000)
n, bins, patches = plt.hist(x, 50, normed=1, facecolor='green', alpha=0.75)

# finally showing the plot
plt.show(fig)