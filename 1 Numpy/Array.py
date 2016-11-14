import numpy as np
data = [[ 0.9526, -0.246 , -0.8856],
        [ 0.5639, 0.2379, 0.9104]]
print(data)
print(type(data))  # list

print(data*10)  # makes array with same data 10 times

data = np.array(data)
print(data)

print(data*10)  # multiply each item with 10
print(data.shape)
print(data.dtype)
print(data.ndim)

data1 = [6, 7.5, 8, 0, 1]
arr1 = np.array(data1)
print(arr1)  # [ 6.   7.5  8.   0.   1. ]
print(type(arr1))
print(arr1.dtype)

arr2 = np.zeros(10)
print(arr2)

arr3 = np.zeros((2,3,2))
print(arr3)

arr4 = np.empty((2,3))  # Garbage value
print(arr4)

arr5 = np.arange(10)  # [0 1 2 3 4 5 6 7 8 9]
print(arr5)

arr6 = np.zeros_like(arr4)
print(arr6)

arr7 = np.ones_like(arr4)
print(arr7)

arr8 = np.ones(5)
print(arr8)
