import numpy as np

a = np.arange(10)**3
print(a)

# Slicing
print(a[2:5])

a[2:5] = 0
print(a)

b = np.arange(12).reshape(3,4)
# Transposing
print(b.T)