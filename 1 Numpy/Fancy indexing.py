import numpy as np

arr = np.empty((8, 4))
print(arr)

for i in range(8):
    arr[i] = i

print(arr)

print(arr[[4, 3, 0, 6]])

arr = np.arange(32).reshape((8, 4))
print(arr)

arr = arr.reshape((2, 16))
print(arr)

arr = arr.reshape(2, 4, 4)
print(arr)

arr = arr.T
print(arr)

# Matrix dot product

arr = np.dot(arr.T, arr)
print(arr)