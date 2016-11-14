import numpy as np

names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe'])

print(names)
print(names == 'Bob')

data = np.array([[-0.048, 0.5433, -0.2349,1.2792],
                [-0.047, -2.026 , 0.7719, 0.3103],
                [2.1452, 0.8799, -0.0523, 0.0672],
                [-1.0023, -0.1698, 1.1503, 1.7289]])

data[data < 0] = 0
print(data)


