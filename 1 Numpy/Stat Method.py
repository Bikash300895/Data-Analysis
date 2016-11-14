import numpy as np

arr = np.random.randn(5, 4)
print(arr)

print(arr.mean())
print(np.mean(arr))
print(arr.sum())

print(arr.mean(axis=1))
print(arr.sum(0))
