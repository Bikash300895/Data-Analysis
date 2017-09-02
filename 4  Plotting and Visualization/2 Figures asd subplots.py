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

# finally showing the plot
plt.show(fig)