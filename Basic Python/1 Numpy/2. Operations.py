import numpy as np

a = np.array([20, 30, 40, 50])
b = np.arange(4)
# Size must be the same
c = a-b
print(c)

# comparision is done through all data
print(a<35)
# [ True  True False False]

# Some built in operation
print(a.sum())
print(a.max())
print(a.min())

# Operation row or column wise
b = np.arange(12).reshape(3,4)
print(b)
print(b.sum(axis=0))


# universal functions
print(np.sqrt(b[0]))

