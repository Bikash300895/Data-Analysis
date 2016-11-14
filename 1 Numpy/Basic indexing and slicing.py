import numpy as np

arr = np.arange(10)

print(arr)
print(arr[5])
print(arr[5:8])

arr[5:7] = 1
print(arr)

# *** array slice are slices of array data is not copied any where ***

arr_slice = arr[5:8]
arr_slice[0] = 111
print(arr)

arr = np.array([[1, 2], [3, 4]])
a = arr[0][0]  # This is a variable
arr[0][0] = 2
print(a)

b = arr[0]  # but this is a pointer
print(b)
arr[0] = [4, 5]
print(b)

print(arr)