import numpy as np

arr = np.arange(-5, 5, .01)

arr = np.arange(5)
print(arr)

xs, ys = np.meshgrid(arr, arr)
print(xs)
print(ys)