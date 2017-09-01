from pandas import Series, DataFrame
import numpy as np

frame = DataFrame(np.random.randn(4, 3), columns=list('bde'),
                  index=['Utah', 'Ohio', 'Texas', 'Oregon'])
print(frame)

print(np.abs(frame))

f = lambda x: x.max() - x.min()
print(frame.apply(f))
