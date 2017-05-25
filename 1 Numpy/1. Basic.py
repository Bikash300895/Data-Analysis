import numpy as np

# Creating as narray
a = np.arange(15).reshape(3, 5)
print(a)

print(a.shape, a.ndim, a.dtype, a.itemsize, a.size, type(a))
# (3, 5) 2 int32 4 15 <class 'numpy.ndarray'>

b = np.array([(1.5,2,3), (4,5,6)])
print(b)


# Working with complex data type
c = np.array( [ [1,2], [3,4] ], dtype=complex )
print(c)
print(c[0][0])

# initializing with values
print('zeroes',np.zeros((2,2)))
print(np.ones((2,2), dtype=np.int16))
print('empty', np.empty((2,2)))

# arrange
d = np.arange(10,30,5)
print('arrange',d)

e = np.arange(0, 2, .3)
print(e)

# line space
print('linspace', np.linspace(0, 2, 9))
from numpy import pi
x = np.linspace(0, 2*pi, 10)
print(x)

