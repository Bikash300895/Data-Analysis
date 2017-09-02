import numpy as np

a = np.arange(5)
# shallow copy
b = a

b[0] = -1
print('Shallow copy')
print(a)
print(b)

b = a.copy()
b[0] = -5
print('Deep copy')
print(a)
print(b)