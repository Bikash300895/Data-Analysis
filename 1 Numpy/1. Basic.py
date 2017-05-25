import numpy as np

# Creating as narray
a = np.arange(15).reshape(3, 5)
print(a)

print(a.shape, a.ndim, a.dtype, a.itemsize, a.size, type(a))
# (3, 5) 2 int32 4 15 <class 'numpy.ndarray'>

