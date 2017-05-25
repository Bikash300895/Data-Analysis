import numpy as np


a = np.array([[1.0, 2.0], [3.0, 4.0]])
print(a)
print(a.transpose())

# getting inverse
print('inverse', np.linalg.inv(a))

# unit matrix
u = np.eye(2)
print(u)

# matrix product
d = np.dot(a, a)
print('dot product', d)

# trace
print('trace', np.trace(u))

print(np.linalg.eig(a))